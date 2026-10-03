/* widgets-math.js — maths widgets for Zero to A*.
   graph · unitcircle · stats · iteration · argand · normal · discrete · projectile
   Plain ES2020, no libraries, no eval. Uses helpers from core.js (window.W). */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;

  /* ================= shared helpers ================= */
  let uid = 0;
  const nextId = (p) => `wm-${p}-${++uid}`;
  const num = (v, d) => { const n = parseFloat(v); return isFinite(n) ? n : d; };
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const isOn = (v) => v != null && !/^(0|false|no|off)$/i.test(String(v).trim());
  const reduced = () => { try { return matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } };
  const SUBD = '₀₁₂₃₄₅₆₇₈₉';
  const sub = (n) => String(n).replace(/\d/g, (d) => SUBD[+d]);
  const show = (el, on) => { el.style.display = on ? '' : 'none'; };
  /** decimals implied by a slider step (0.1 → 1, 0.25 → 2, 5 → 0) */
  function dpOf(step) {
    const s = String(step);
    if (/e-/i.test(s)) return Math.min(8, +s.split(/e-/i)[1]);
    const i = s.indexOf('.');
    return i < 0 ? 0 : Math.min(8, s.length - i - 1);
  }
  /** "a,b" → [a,b] (a<b); null if missing; 'bad' if unreadable */
  function pair(s) {
    if (s == null || String(s).trim() === '') return null;
    const p = String(s).replace(/[−–]/g, '-').split(',').map((t) => parseFloat(t));
    return p.length >= 2 && isFinite(p[0]) && isFinite(p[1]) && p[1] > p[0] ? [p[0], p[1]] : 'bad';
  }
  /** split at sep when not inside brackets */
  function splitTop(s, sep) {
    const out = []; let depth = 0, cur = '';
    for (const ch of String(s)) {
      if (ch === '(') depth++; else if (ch === ')') depth--;
      if (ch === sep && depth <= 0) { out.push(cur); cur = ''; } else cur += ch;
    }
    out.push(cur);
    return out;
  }
  /** short coloured line used in legends (colour = CSS variable) */
  function swatch(cssVar, dashed) {
    return W.h('span', { 'aria-hidden': 'true', style: {
      display: 'inline-block', flex: 'none', width: '18px', height: '0', borderTop: `3px ${dashed ? 'dashed' : 'solid'} ${cssVar}`,
      borderRadius: '2px', verticalAlign: 'middle' } });
  }
  /** segmented buttons (.w-tabs). items: [[value, text], …] */
  function tabs(items, value, onchange, label) {
    const el = W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': label });
    let cur = value;
    const btns = items.map(([v, text]) => {
      const b = W.h('button', { type: 'button', class: 'w-tab', role: 'tab', 'aria-selected': String(v === value) }, text);
      b.addEventListener('click', () => { set(v); onchange(v); });
      el.append(b);
      return b;
    });
    function set(v) { cur = v; items.forEach(([iv], i) => btns[i].setAttribute('aria-selected', String(iv === v))); }
    return { el, set, get: () => cur };
  }
  /** pointer position in canvas CSS pixels (allows for the frame border) */
  function ptPos(state, e) {
    const r = state.cv.getBoundingClientRect();
    const sx = state.w && r.width ? state.w / r.width : 1, sy = state.h && r.height ? state.h / r.height : 1;
    return { x: (e.clientX - r.left) * sx, y: (e.clientY - r.top) * sy };
  }
  /** wrap a draw function so an unexpected error never leaves a broken canvas state */
  function safeDraw(fn) {
    return function (ctx, w, h, c) {
      try { fn(ctx, w, h, c); } catch (e) { console.error(e); try { if (ctx.reset) ctx.reset(); } catch (_) { /* ignore */ } }
    };
  }
  /** text with a halo in the sheet colour so it stays legible over grid lines and curves */
  function haloText(ctx, c, text, x, y, color) {
    ctx.save();
    ctx.lineJoin = 'round'; ctx.lineWidth = 3.5; ctx.strokeStyle = c.sheet;
    ctx.strokeText(text, x, y);
    ctx.fillStyle = color || c.ink;
    ctx.fillText(text, x, y);
    ctx.restore();
  }
  function dot(ctx, c, x, y, r, fill) {
    ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fillStyle = fill; ctx.fill();
    ctx.lineWidth = 2; ctx.strokeStyle = c.sheet; ctx.stroke();
  }
  /** redraw W.axes tick labels (same positions) with a halo, on top of curves. A = W.axes result, v = view given to W.axes */
  function topLabels(ctx, c, A, v, w, h, fx, fy) {
    const pad = A.pad;
    const ax = v.y0 <= 0 && v.y1 >= 0 ? A.Y(0) : h - pad.b;
    const ay = v.x0 <= 0 && v.x1 >= 0 ? A.X(0) : pad.l;
    ctx.save();
    ctx.font = `11px ${c.mono || 'monospace'}`;
    ctx.lineJoin = 'round'; ctx.lineWidth = 3; ctx.strokeStyle = c.sheet; ctx.fillStyle = c.ink3;
    const put = (s, x, y) => { ctx.strokeText(s, x, y); ctx.fillText(s, x, y); };
    ctx.textAlign = 'center'; ctx.textBaseline = 'top';
    for (const t of A.xt) if (t !== 0) put(fx ? fx(t) : W.fmt(t, 4), A.X(t), Math.min(h - pad.b + 5, ax + 5));
    ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
    for (const t of A.yt) if (t !== 0) put(fy ? fy(t) : W.fmt(t, 4), Math.max(pad.l - 5, ay - 5), A.Y(t));
    ctx.restore();
  }

  /* ================= 1. graph — function plotter ================= */
  const FN_START = /^(?:arcsin|arccos|arctan|asin|acos|atan|sinh|cosh|tanh|sin|cos|tan|sec|cosec|csc|cot|sqrt|cbrt|abs|ln|log|exp|floor|ceil|round|sign|min|max)/;
  /** a*x^2 + b*x → ax² + bx (for legends) */
  function prettyFn(src) {
    let s = String(src).trim().replace(/\*\*/g, '^');
    s = s.replace(/\^(?:\((-?\d+)\)|(-?\d+)(?![\d.]))/g, (m, a, b) => W.sup(a != null ? a : b));
    s = s.replace(/\s*\*\s*(?=[a-zA-Zπ(√])/g, (m, off, str) => (FN_START.test(str.slice(off + m.length)) ? ' ' : ''));
    s = s.replace(/\*/g, '×').replace(/pi/g, 'π').replace(/sqrt/g, '√').replace(/-/g, '−');
    return s;
  }
  const stripLhs = (s) => String(s).replace(/^\s*(?:y\s*[₀-₉\d]*|[fgh]\s*\(\s*x\s*\))\s*=\s*/i, '');

  /** trace one curve into the current path, breaking at gaps, asymptotes and jumps */
  function traceCurve(ctx, f, x0, dx, N, X, Y) {
    const CL = 1e6;
    const PY = (y) => clamp(Y(y), -CL, CL);
    const pyd = (u, v) => Math.abs(clamp(Y(u), -1e9, 1e9) - clamp(Y(v), -1e9, 1e9));
    // last finite x near the boundary of the domain, between good (finite) and bad (not finite)
    const edge = (good, bad) => {
      let gy = f(good);
      for (let k = 0; k < 44; k++) {
        const m = (good + bad) / 2;
        if (m === good || m === bad) break;
        const v = f(m);
        if (isFinite(v)) { good = m; gy = v; } else bad = m;
      }
      return [good, gy];
    };
    // a big step between neighbouring samples: bisect; if the step does not shrink, it is a discontinuity
    const jump = (xa, ya, xb, yb) => {
      const d0 = pyd(ya, yb);
      let d = d0;
      for (let k = 0; k < 18 && d >= 2; k++) {
        const xm = (xa + xb) / 2, ym = f(xm);
        if (!isFinite(ym)) return [xa, ya, xb, yb];
        if (pyd(ya, ym) >= pyd(ym, yb)) { xb = xm; yb = ym; } else { xa = xm; ya = ym; }
        d = pyd(ya, yb);
      }
      return d >= 2 && d > d0 * 0.3 ? [xa, ya, xb, yb] : null;
    };
    let have = false, lx = NaN, ly = NaN, prevX = NaN;
    for (let i = 0; i <= N; i++) {
      const x = x0 + i * dx, y = f(x);
      if (!isFinite(y)) {
        if (have) { const e = edge(lx, x); ctx.lineTo(X(e[0]), PY(e[1])); have = false; }
        prevX = x;
        continue;
      }
      if (!have) {
        if (i > 0) { const e = edge(x, prevX); ctx.moveTo(X(e[0]), PY(e[1])); ctx.lineTo(X(x), PY(y)); } else ctx.moveTo(X(x), PY(y));
        have = true;
      } else if (pyd(ly, y) >= 2) {
        const j = jump(lx, ly, x, y);
        if (j) { ctx.lineTo(X(j[0]), PY(j[1])); ctx.moveTo(X(j[2]), PY(j[3])); }
        ctx.lineTo(X(x), PY(y));
      } else ctx.lineTo(X(x), PY(y));
      lx = x; ly = y; prevX = x;
    }
  }

  W.register('graph', function (el, o) {
    const id = nextId('g');
    const edit = isOn(o.edit);
    let deg = isOn(o.deg);
    const deg0 = deg;
    const H = Math.round(clamp(num(o.h, 320), 160, 900));
    const warn = [];
    let xr = pair(o.x), yr = pair(o.y);
    if (xr === 'bad') { warn.push('data-x should look like "-5,5", so x runs from −10 to 10.'); xr = null; }
    if (yr === 'bad') { warn.push('data-y should look like "-5,5", so the y-range is chosen automatically.'); yr = null; }
    if (!xr) xr = deg ? [-360, 360] : [-10, 10];
    const MAXF = edit ? 3 : 4;
    let srcs = String(o.fns || o.fn || o.f || '').split(';').map((s) => s.trim()).filter(Boolean);
    if (srcs.length > MAXF) { warn.push(`Only the first ${MAXF} functions are drawn.`); srcs = srcs.slice(0, MAXF); }
    if (!srcs.length && !edit) srcs = ['x^2'];
    const labels = String(o.labels || '').split(';').map((s) => s.trim());
    const decl = Object.create(null);
    for (const p of W.parseParams(o.params || '')) {
      if (!/^[a-zA-Z]$/.test(p.name) || p.name === 'x' || p.name === 'e') continue;
      let { value, min, max, step } = p;
      if (!(max > min)) { min = -5; max = 5; }
      if (!(step > 0)) step = 0.1;
      decl[p.name] = { value, min: Math.min(min, value), max: Math.max(max, value), step };
    }
    const COLV = ['sc', 'sc2', 'red', 'ink2'];
    const CSSV = ['var(--sc)', 'var(--sc2)', 'var(--red)', 'var(--ink-2)'];
    const nSlots = edit ? 3 : srcs.length;
    const F = [];
    for (let i = 0; i < nSlots; i++) F.push({ src: srcs[i] || '', f: null, vars: null, err: '' });
    const fname = (i) => (nSlots === 1 ? 'y' : 'y' + sub(i + 1));
    const params = Object.create(null);
    const scope = {};
    let pts = [];

    const { body } = W.frame(el, edit ? 'Graph plotter' : 'Graph', edit ? 'type up to three functions of x' : 'drag to pan · scroll or pinch to zoom');

    /* ---- top: editable functions or legend ---- */
    const top = W.h('div', { style: { display: 'grid', gap: '8px' } });
    const errEls = [];
    const legendEls = [];
    if (edit) {
      const PH = ['e.g. x^2 - 3x + 1', 'e.g. 2sin(x)', 'e.g. 1/x'];
      for (let i = 0; i < nSlots; i++) {
        const inp = W.h('input', { type: 'text', id: `${id}-f${i}`, value: F[i].src, placeholder: PH[i], spellcheck: 'false',
          autocomplete: 'off', autocapitalize: 'off', 'aria-label': `Function ${i + 1}: y${i + 1} in terms of x`, style: { fontFamily: 'var(--f-mono)' } });
        const err = W.h('div', { class: 'w-err', role: 'status' });
        show(err, false);
        errEls.push(err);
        inp.addEventListener('input', () => { F[i].src = inp.value; parseFn(i); showErr(i); syncParams(); setAria(); cv.redraw(); });
        top.append(W.h('div', { style: { display: 'grid', gap: '3px' } },
          W.h('div', { style: { display: 'grid', gridTemplateColumns: '18px auto minmax(0, 1fr)', alignItems: 'center', gap: '8px' } },
            swatch(CSSV[i]), W.h('label', { for: inp.id, class: 'w-lab', style: { whiteSpace: 'nowrap' } }, `${fname(i)} =`), inp),
          err));
      }
    } else {
      const lg = W.h('div', { class: 'w-row', style: { gap: '6px 20px', alignItems: 'center' } });
      for (let i = 0; i < nSlots; i++) {
        const t = W.h('span', {});
        legendEls.push(t);
        lg.append(W.h('span', { style: { display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '.95rem' } }, swatch(CSSV[i]), t));
      }
      top.append(lg);
    }
    const errAll = W.h('div', { class: 'w-err', role: 'status' });
    show(errAll, false);
    body.append(top, errAll);

    /* ---- canvas ---- */
    const cv = W.canvas(body, { height: H, draw: safeDraw(draw) });
    const wrap = cv.wrap;
    wrap.tabIndex = 0;
    wrap.setAttribute('role', 'img');
    wrap.style.cursor = 'crosshair';

    /* ---- readout + view buttons ---- */
    const readout = W.h('div', { class: 'w-val', style: { flex: '1 1 15rem', minHeight: '1.5em', display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '2px 16px' } });
    const btn = (text, label, fn) => W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', 'aria-label': label, title: label, onclick: fn }, text);
    const ctlBox = W.h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '6px', alignItems: 'center' } });
    let degTabs = null;
    if (edit) {
      degTabs = tabs([['rad', 'Radians'], ['deg', 'Degrees']], deg ? 'deg' : 'rad', (v) => setDeg(v === 'deg'), 'Angle unit for trig functions');
      ctlBox.append(degTabs.el);
    }
    ctlBox.append(
      btn('−', 'Zoom out', () => zoomCentre(1.25)),
      btn('+', 'Zoom in', () => zoomCentre(0.8)),
      btn('Reset view', 'Reset view', resetView));
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'center', justifyContent: 'space-between' } }, readout, ctlBox));

    /* ---- sliders ---- */
    const sliderRow = W.h('div', { class: 'w-row' });
    body.append(sliderRow);
    const note = W.h('div', { class: 'w-note' });
    body.append(note);

    /* ---- parsing ---- */
    function parseFn(i) {
      const s = F[i];
      s.f = null; s.vars = null; s.err = '';
      const raw = stripLhs(s.src);
      if (!raw.trim()) return;
      try { const r = W.parse(raw, { degrees: deg }); s.f = r.f; s.vars = r.vars; } catch (e) { s.err = String(e.message || 'could not read this'); }
    }
    function parsePts() {
      pts = [];
      const bad = [];
      for (const raw of String(o.points || '').split(';').map((s) => s.trim()).filter(Boolean)) {
        let t = raw;
        if (/^\(.*\)$/.test(t) && splitTop(t, ',').length === 1) t = t.slice(1, -1);
        const parts = splitTop(t, ',');
        if (parts.length !== 2) { bad.push(`point "${raw}" should be written x,y`); continue; }
        try {
          const px = W.parse(parts[0], { degrees: deg }), py = W.parse(parts[1], { degrees: deg });
          pts.push({ px: px.f, py: py.f, vars: new Set([...px.vars, ...py.vars]) });
        } catch (e) { bad.push(`point "${raw}": ${e.message}`); }
      }
      return bad;
    }
    function showErr(i) {
      const s = F[i];
      if (edit) {
        errEls[i].textContent = s.err ? `Can't read ${fname(i)}: ${s.err}. Use * or brackets if unsure, e.g. 3*(x+1)^2.` : '';
        show(errEls[i], !!s.err);
      }
    }
    function showAllErr(extra) {
      const msgs = warn.slice();
      if (!edit) F.forEach((s, i) => { if (s.err) msgs.push(`Can't read ${fname(i)} = ${s.src}: ${s.err}.`); });
      if (extra) msgs.push(...extra);
      errAll.textContent = msgs.join(' ');
      show(errAll, msgs.length > 0);
    }
    function addParam(name) {
      const d = decl[name] || { value: 1, min: -5, max: 5, step: 0.1 };
      const dp = dpOf(d.step);
      const p = { value: d.value };
      p.ui = W.slider({ label: name, min: d.min, max: d.max, step: d.step, value: d.value, fmt: (v) => W.fix(v, dp),
        oninput: (v) => { p.value = v; cv.redraw(); } });
      p.ui.input.setAttribute('aria-label', `Parameter ${name}`);
      params[name] = p;
    }
    function syncParams() {
      const used = new Set();
      for (const s of F) if (s.vars) for (const v of s.vars) if (v !== 'x') used.add(v);
      for (const p of pts) for (const v of p.vars) if (v !== 'x') used.add(v);
      for (const name of used) if (!params[name]) addParam(name);
      for (const name of Object.keys(params).sort()) { sliderRow.append(params[name].ui.el); show(params[name].ui.el, used.has(name)); }
      show(sliderRow, used.size > 0);
      note.textContent = edit
        ? 'Type functions using x (e.g. 2x^2 - 3, sin(x), sqrt(x), 1/(x-2)). Any other letter gets its own slider. Drag to pan, scroll or pinch to zoom, hover or tap to read values.'
        : used.size
          ? `Move the slider${used.size > 1 ? 's' : ''} for ${[...used].sort().join(', ')} and watch how the curve changes. Hover or tap the graph to read off values; drag to pan, scroll or pinch to zoom.`
          : 'Hover or tap the graph to read off values. Drag to pan, scroll or pinch to zoom.';
    }
    function fillScope() { for (const k in params) scope[k] = params[k].value; }
    const evalFn = (fn) => (x) => { scope.x = x; try { const v = fn(scope); return typeof v === 'number' ? v : NaN; } catch (e) { return NaN; } };
    function labelOf(i) {
      if (labels[i]) return labels[i];
      const s = stripLhs(F[i].src);
      return `${fname(i)} = ${F[i].err ? s : prettyFn(s)}`;
    }
    function setAria() {
      const list = F.map((s, i) => (s.f ? labelOf(i) : null)).filter(Boolean);
      wrap.setAttribute('aria-label', `Graph of ${list.length ? list.join('; ') : 'no functions yet'}. Arrow keys pan, plus and minus zoom, 0 resets the view.`);
      legendEls.forEach((t, i) => { t.textContent = labelOf(i); });
    }

    F.forEach((_, i) => { parseFn(i); showErr(i); });
    const ptErr = parsePts();
    syncParams();
    showAllErr(ptErr);
    setAria();

    /* ---- view ---- */
    function autoY() {
      fillScope();
      const ys = [];
      for (const s of F) {
        if (!s.f) continue;
        const f = evalFn(s.f);
        for (let i = 0; i <= 240; i++) { const y = f(xr[0] + (xr[1] - xr[0]) * i / 240); if (isFinite(y)) ys.push(y); }
      }
      if (!ys.length) return [-10, 10];
      ys.sort((a, b) => a - b);
      let lo = ys[Math.floor((ys.length - 1) * 0.03)], hi = ys[Math.ceil((ys.length - 1) * 0.97)];
      if (!(hi - lo > 1e-9)) { lo -= 1; hi += 1; }
      const m = (hi - lo) * 0.12; lo -= m; hi += m;
      if (lo > 0 && lo < (hi - lo) * 0.6) lo = -(hi - lo) * 0.06;
      if (hi < 0 && -hi < (hi - lo) * 0.6) hi = (hi - lo) * 0.06;
      return [lo, hi];
    }
    if (!yr) yr = autoY();
    const home0 = { x0: xr[0], x1: xr[1], y0: yr[0], y1: yr[1] };
    const homeView = () => {
      if (deg === deg0) return Object.assign({}, home0);
      const k = deg ? 180 / Math.PI : Math.PI / 180;
      const r90 = (v) => (deg ? Math.round(v / 90) * 90 : v);
      return { x0: r90(home0.x0 * k), x1: r90(home0.x1 * k), y0: home0.y0, y1: home0.y1 };
    };
    let view = homeView();
    let geom = null, hover = null;

    function setDeg(on) {
      if (on === deg) return;
      deg = on;
      const k = on ? 180 / Math.PI : Math.PI / 180;
      view.x0 *= k; view.x1 *= k;
      F.forEach((_, i) => { parseFn(i); showErr(i); });
      parsePts();
      syncParams();
      cv.redraw();
    }
    function resetView() { view = homeView(); cv.redraw(); }
    function okSpan(a, b) { const s = b - a; return s > 1e-7 && s < 1e8; }
    function zoomAt(px, py, k) {
      if (!geom) return;
      const g = geom;
      const mx = view.x0 + (px - g.L) / (g.R - g.L) * (view.x1 - view.x0);
      const my = view.y1 - (py - g.T) / (g.B - g.T) * (view.y1 - view.y0);
      const nv = { x0: mx + (view.x0 - mx) * k, x1: mx + (view.x1 - mx) * k, y0: my + (view.y0 - my) * k, y1: my + (view.y1 - my) * k };
      if (okSpan(nv.x0, nv.x1) && okSpan(nv.y0, nv.y1)) view = nv;
    }
    function zoomCentre(k) { if (geom) { zoomAt((geom.L + geom.R) / 2, (geom.T + geom.B) / 2, k); cv.redraw(); } }
    function panPx(dx, dy) {
      if (!geom) return;
      const ux = (view.x1 - view.x0) / (geom.R - geom.L), uy = (view.y1 - view.y0) / (geom.B - geom.T);
      view.x0 -= dx * ux; view.x1 -= dx * ux; view.y0 += dy * uy; view.y1 += dy * uy;
    }

    /* ---- pointer, wheel and keyboard ---- */
    const ptrs = new Map();
    let dragged = false, start = null, pinch = null;
    wrap.addEventListener('pointerdown', (e) => {
      if (e.button != null && e.button > 0) return;
      try { wrap.setPointerCapture(e.pointerId); } catch (err) { /* ignore */ }
      const p = ptPos(cv, e);
      ptrs.set(e.pointerId, p);
      if (ptrs.size === 1) { start = p; dragged = false; }
      if (ptrs.size === 2) { dragged = true; pinch = null; hover = null; }
    });
    wrap.addEventListener('pointermove', (e) => {
      const p = ptPos(cv, e);
      if (!ptrs.has(e.pointerId)) {
        if (e.pointerType === 'mouse' || e.pointerType === 'pen') { hover = p; cv.redraw(); }
        return;
      }
      const last = ptrs.get(e.pointerId);
      ptrs.set(e.pointerId, p);
      if (ptrs.size === 1) {
        if (!dragged && Math.hypot(p.x - start.x, p.y - start.y) > 5) { dragged = true; wrap.style.cursor = 'grabbing'; hover = null; }
        if (dragged) { panPx(p.x - last.x, p.y - last.y); cv.redraw(); }
      } else if (ptrs.size === 2) {
        const [a, b] = [...ptrs.values()];
        const d = Math.hypot(a.x - b.x, a.y - b.y), m = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
        if (pinch && pinch.d > 10 && d > 10) { zoomAt(pinch.m.x, pinch.m.y, pinch.d / d); panPx(m.x - pinch.m.x, m.y - pinch.m.y); cv.redraw(); }
        pinch = { d, m };
      }
    });
    const endPtr = (e) => {
      if (!ptrs.has(e.pointerId)) return;
      ptrs.delete(e.pointerId);
      if (ptrs.size < 2) pinch = null;
      if (ptrs.size === 0) {
        wrap.style.cursor = 'crosshair';
        if (e.type === 'pointerup' && (!dragged || e.pointerType === 'mouse')) { hover = ptPos(cv, e); cv.redraw(); }
      }
    };
    wrap.addEventListener('pointerup', endPtr);
    wrap.addEventListener('pointercancel', endPtr);
    wrap.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse' && !ptrs.size) { hover = null; cv.redraw(); } });
    wrap.addEventListener('wheel', (e) => {
      e.preventDefault();
      let dy = e.deltaY;
      if (e.deltaMode === 1) dy *= 16; else if (e.deltaMode === 2) dy *= 400;
      const p = ptPos(cv, e);
      zoomAt(p.x, p.y, Math.exp(clamp(dy, -250, 250) * 0.0016));
      hover = p;
      cv.redraw();
    }, { passive: false });
    wrap.addEventListener('dblclick', resetView);
    wrap.addEventListener('keydown', (e) => {
      if (!geom) return;
      const sx = (geom.R - geom.L) * 0.1, sy = (geom.B - geom.T) * 0.1;
      const k = e.key;
      if (k === 'ArrowLeft') panPx(sx, 0); else if (k === 'ArrowRight') panPx(-sx, 0);
      else if (k === 'ArrowUp') panPx(0, sy); else if (k === 'ArrowDown') panPx(0, -sy);
      else if (k === '+' || k === '=') { zoomCentre(0.8); e.preventDefault(); return; }
      else if (k === '-' || k === '_') { zoomCentre(1.25); e.preventDefault(); return; }
      else if (k === '0' || k === 'Home') { resetView(); e.preventDefault(); return; }
      else return;
      e.preventDefault();
      cv.redraw();
    });

    /* ---- drawing ---- */
    function draw(ctx, w, h, c) {
      fillScope();
      ctx.font = `11px ${c.mono}`;
      let lw = 0;
      for (const v of W.ticks(view.y0, view.y1, Math.max(4, Math.round(h / 45)))) lw = Math.max(lw, ctx.measureText(W.fmt(v, 4)).width);
      const pad = { l: Math.max(36, Math.ceil(lw) + 12), r: 16, t: 12, b: 26 };
      const span = view.x1 - view.x0;
      const sx = deg && span >= 150 ? 90 : 1;
      const av = { x0: view.x0 / sx, x1: view.x1 / sx, y0: view.y0, y1: view.y1 };
      const fxl = deg ? (v) => W.fmt(v * sx, 4) + '°' : null;
      const A = W.axes(ctx, w, h, av, c, { pad, xlabel: deg ? 'x (°)' : 'x', ylabel: 'y', fx: fxl });
      const X = (x) => A.X(x / sx), Y = A.Y;
      const L = pad.l, R = w - pad.r, T = pad.t, B = h - pad.b;
      geom = { L, R, T, B };
      ctx.save();
      ctx.beginPath(); ctx.rect(L, T, R - L, B - T); ctx.clip();
      const N = Math.max(60, Math.round(R - L));
      ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      F.forEach((s, i) => {
        if (!s.f) return;
        ctx.beginPath();
        traceCurve(ctx, evalFn(s.f), view.x0, span / N, N, X, Y);
        ctx.strokeStyle = c[COLV[i]]; ctx.lineWidth = 2.4; ctx.stroke();
      });
      ctx.restore();
      topLabels(ctx, c, A, av, w, h, fxl, null);
      ctx.save();
      ctx.beginPath(); ctx.rect(L - 6, T - 6, R - L + 12, B - T + 12); ctx.clip();
      // marked points
      const P = [];
      for (const p of pts) { try { const x = p.px(scope), y = p.py(scope); if (isFinite(x) && isFinite(y)) P.push([x, y]); } catch (e) { /* skip */ } }
      ctx.font = `12px ${c.mono}`;
      for (const [x, y] of P) {
        const u = X(x), v = Y(y);
        if (u < L - 6 || u > R + 6 || v < T - 6 || v > B + 6) continue;
        dot(ctx, c, u, v, 4.5, c.ink);
        if (P.length <= 4) {
          const t = `(${W.fmt(x, 3)}, ${W.fmt(y, 3)})`, tw = ctx.measureText(t).width;
          const right = u + 8 + tw < R - 2, up = v - 22 > T;
          ctx.textAlign = right ? 'left' : 'right'; ctx.textBaseline = up ? 'bottom' : 'top';
          haloText(ctx, c, t, right ? u + 8 : u - 8, up ? v - 6 : v + 6, c.ink);
        }
      }
      // crosshair
      let hv = null;
      if (hover && hover.x >= L && hover.x <= R && hover.y >= T - 4 && hover.y <= B + 4) {
        const raw = view.x0 + (hover.x - L) / (R - L) * span;
        const st = Math.pow(10, Math.floor(Math.log10(span / (R - L) * 3)));
        const hx = +(Math.round(raw / st) * st).toPrecision(12);
        const xs = Math.round(X(hx)) + 0.5;
        const vals = F.map((s) => (s.f ? evalFn(s.f)(hx) : null));
        ctx.lineWidth = 1; ctx.setLineDash([4, 4]); ctx.strokeStyle = c.ink3;
        ctx.beginPath(); ctx.moveTo(xs, T); ctx.lineTo(xs, B); ctx.stroke();
        const ax = clamp(X(0), L, R);
        ctx.globalAlpha = 0.55;
        vals.forEach((v, i) => {
          if (v == null || !isFinite(v)) return;
          const yp = Math.round(Y(v)) + 0.5;
          if (yp < T || yp > B) return;
          ctx.strokeStyle = c[COLV[i]]; ctx.beginPath(); ctx.moveTo(ax, yp); ctx.lineTo(xs, yp); ctx.stroke();
        });
        ctx.globalAlpha = 1; ctx.setLineDash([]);
        vals.forEach((v, i) => { if (v != null && isFinite(v)) { const yp = Y(v); if (yp >= T - 5 && yp <= B + 5) dot(ctx, c, X(hx), yp, 4.5, c[COLV[i]]); } });
        hv = { x: hx, dp: Math.max(0, -Math.floor(Math.log10(st) + 1e-9)), vals };
      }
      ctx.restore();
      renderReadout(hv);
    }
    function renderReadout(hv) {
      readout.textContent = '';
      if (!hv) { readout.append(W.h('span', { style: { color: 'var(--ink-3)' } }, 'Hover or tap the graph to read off values')); return; }
      readout.append(W.h('b', { style: { fontWeight: 600 } }, `x = ${W.fix(hv.x, hv.dp)}${deg ? '°' : ''}`));
      hv.vals.forEach((v, i) => {
        if (v == null) return;
        readout.append(W.h('span', { style: { display: 'inline-flex', alignItems: 'center', gap: '6px', whiteSpace: 'nowrap' } },
          swatch(CSSV[i]), `${fname(i)} = ${isFinite(v) ? W.fmt(v, 4) : 'undefined'}`));
      });
    }
  });

  /* ================= 2. unitcircle ================= */
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; }
  /** whole degrees → multiple of π as text ('π/6', '5π/4', '2π'), or null if not a simple fraction */
  function piFrac(d) {
    if (!Number.isInteger(d)) return null;
    if (d === 0) return '0';
    const g = gcd(d, 180), p = d / g, q = 180 / g;
    if (q > 12) return null;
    const ps = p === 1 ? '' : p === -1 ? '−' : String(p).replace('-', '−');
    return q === 1 ? `${ps}π` : `${ps}π/${q}`;
  }
  /** exact sin/cos/tan for multiples of 30° and 45° */
  function trigExact(d) {
    const m = ((d % 360) + 360) % 360;
    if (m % 30 !== 0 && m % 45 !== 0) return null;
    const ref = m <= 90 ? m : m <= 180 ? 180 - m : m <= 270 ? m - 180 : 360 - m;
    const S = { 0: '0', 30: '1/2', 45: '√2/2', 60: '√3/2', 90: '1' };
    const C = { 0: '1', 30: '√3/2', 45: '√2/2', 60: '1/2', 90: '0' };
    const T = { 0: '0', 30: '√3/3', 45: '1', 60: '√3', 90: null };
    const gs = m > 180 ? '−' : '', gc = m > 90 && m < 270 ? '−' : '';
    const gt = (gs === '') !== (gc === '') ? '−' : '';
    const put = (s, g) => (s == null ? null : s === '0' ? '0' : g + s);
    return { sin: put(S[ref], gs), cos: put(C[ref], gc), tan: put(T[ref], gt) };
  }
  function exactTxt(ex, v) {
    if (!isFinite(v) || Math.abs(v) > 1e12) return 'undefined';
    if (ex == null) return W.fix(v, 4);
    if (ex.includes('√')) return `${ex} ≈ ${W.fix(v, 4)}`;
    if (ex.includes('/')) return `${ex} = ${W.fmt(v, 4)}`;
    return ex;
  }

  W.register('unitcircle', function (el, o) {
    let th = Math.round(num(o.angle, 30));
    th = ((th % 360) + 360) % 360;
    let rad = isOn(o.rad);
    const angTxt = (d) => { if (!rad) return `${d}°`; const f = piFrac(d); return f ? `${f} rad` : `${W.fix(d * Math.PI / 180, 3)} rad`; };

    const { body } = W.frame(el, 'Unit circle', 'drag the point round the circle');
    const cv = W.canvas(body, { height: 300, draw: safeDraw(draw) });
    const wrap = cv.wrap;
    wrap.tabIndex = 0;
    wrap.setAttribute('role', 'img');
    wrap.style.cursor = 'pointer';
    const sl = W.slider({ label: 'Angle θ', min: 0, max: 360, step: 1, value: th, fmt: angTxt, oninput: (v) => { th = v; update(); } });
    sl.input.setAttribute('aria-label', 'Angle theta in degrees');
    const unit = tabs([['deg', 'Degrees'], ['rad', 'Radians']], rad ? 'rad' : 'deg', (v) => { rad = v === 'rad'; sl.set(th); update(); }, 'Angle unit');
    sl.el.style.flex = '3 1 14rem';
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'center' } }, sl.el, unit.el));
    const sDeg = W.stat('θ in degrees'), sRad = W.stat('θ in radians');
    const sSin = W.stat('sin θ', true), sCos = W.stat('cos θ'), sTan = W.stat('tan θ'), sQ = W.stat('Quadrant (CAST)');
    sSin.el.firstChild.prepend(swatch('var(--sc)'), ' ');
    sCos.el.firstChild.prepend(swatch('var(--sc2)'), ' ');
    body.append(W.h('div', { class: 'w-out' }, sDeg.el, sRad.el, sSin.el, sCos.el, sTan.el, sQ.el));
    body.append(W.h('div', { class: 'w-note' },
      'The point on the circle is (cos θ, sin θ): cos θ is how far across, sin θ how far up. CAST shows which ratios are positive in each quadrant. Compare 30°, 150°, 210° and 330°.'));

    function quadrant(m) {
      if (m === 0 || m === 360) return 'on the +x axis';
      if (m === 90) return 'on the +y axis';
      if (m === 180) return 'on the −x axis';
      if (m === 270) return 'on the −y axis';
      return m < 90 ? '1st · A: all +' : m < 180 ? '2nd · S: sin +' : m < 270 ? '3rd · T: tan +' : '4th · C: cos +';
    }
    function update() {
      const r = th * Math.PI / 180;
      const s = Math.sin(r), c = Math.cos(r);
      const ex = trigExact(th);
      const frac = piFrac(th);
      sDeg.set(`${th}°`);
      sRad.set(frac && frac !== '0' ? `${frac} ≈ ${W.fix(r, 4)}` : W.fix(r, 4));
      sSin.set(exactTxt(ex && ex.sin, s));
      sCos.set(exactTxt(ex && ex.cos, c));
      sTan.set(ex ? (ex.tan == null ? 'undefined' : exactTxt(ex.tan, s / c)) : (Math.abs(c) < 1e-9 ? 'undefined' : W.fix(s / c, 4)));
      sQ.set(quadrant(th));
      wrap.setAttribute('aria-label', `Unit circle with angle ${th} degrees: sin = ${W.fix(s, 4)}, cos = ${W.fix(c, 4)}. Drag or use arrow keys to change the angle.`);
      cv.redraw();
    }

    let G = null; // geometry from last draw
    function draw(ctx, w, h, c) {
      const wide = w >= 540;
      const S = wide ? 300 : Math.min(300, w);
      const wantH = wide ? 300 : S + 140;
      if (Math.abs(h - wantH) > 1) { wrap.style.height = wantH + 'px'; return; }
      const cx = wide ? S / 2 : w / 2, cy = S / 2, R = S / 2 - 42;
      const t = th * Math.PI / 180, cs = Math.cos(t), sn = Math.sin(t);
      const px = cx + R * cs, py = cy - R * sn;
      // strip geometry
      let sx0, sx1, sy0, amp;
      if (wide) { sx0 = S + 30; sx1 = w - 20; sy0 = cy; amp = R; } else { sx0 = 34; sx1 = w - 18; sy0 = S + 58; amp = 46; }
      const SX = (d) => sx0 + d / 360 * (sx1 - sx0);
      G = { wide, S, cx, cy, R, sx0, sx1 };
      const m = th % 360;
      const quad = m > 0 && m < 90 ? 0 : m > 90 && m < 180 ? 1 : m > 180 && m < 270 ? 2 : m > 270 && m < 360 ? 3 : -1;

      // active quadrant tint
      if (quad >= 0) {
        ctx.save(); ctx.globalAlpha = 0.08; ctx.fillStyle = c.sc;
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, R, -quad * Math.PI / 2, -(quad + 1) * Math.PI / 2, true); ctx.closePath(); ctx.fill();
        ctx.restore();
      }
      // projection from the point to the sine strip (drawn first, underneath)
      const qx = SX(th), qy = sy0 - amp * sn;
      if (wide) {
        ctx.save(); ctx.setLineDash([5, 5]); ctx.strokeStyle = c.sc; ctx.globalAlpha = 0.5; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(qx, qy); ctx.stroke(); ctx.restore();
      }
      // axes
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(cx - R - 20, Math.round(cy) + 0.5); ctx.lineTo(cx + R + 20, Math.round(cy) + 0.5);
      ctx.moveTo(Math.round(cx) + 0.5, cy - R - 20); ctx.lineTo(Math.round(cx) + 0.5, cy + R + 20);
      ctx.stroke();
      ctx.font = `11px ${c.mono}`; ctx.fillStyle = c.ink3;
      ctx.textAlign = 'left'; ctx.textBaseline = 'top'; ctx.fillText('1', cx + R + 4, cy + 4);
      ctx.textAlign = 'right'; ctx.fillText('−1', cx - R - 4, cy + 4);
      ctx.textAlign = 'left'; ctx.textBaseline = 'bottom'; ctx.fillText('1', cx + 5, cy - R - 3);
      ctx.textBaseline = 'top'; ctx.fillText('−1', cx + 5, cy + R + 3);
      ctx.font = `italic 13px ${c.font}`;
      ctx.textAlign = 'left'; ctx.textBaseline = 'middle'; ctx.fillText('x', cx + R + 25, cy);
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom'; ctx.fillText('y', cx, cy - R - 23);
      // circle
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();
      // CAST letters in the corners
      const CAST = [['A', 'all +', 1, -1], ['S', 'sin +', -1, -1], ['T', 'tan +', -1, 1], ['C', 'cos +', 1, 1]];
      ctx.textAlign = 'center';
      CAST.forEach(([L, txt, sx, sy], i) => {
        const lx = cx + sx * (R + 16), ly = cy + sy * (R + 12);
        const on = i === quad;
        ctx.font = `${on ? 700 : 600} 16px ${c.font}`; ctx.textBaseline = 'middle';
        haloText(ctx, c, L, lx, ly - 5, on ? c.sc : c.ink3);
        ctx.font = `10.5px ${c.mono}`; ctx.textBaseline = 'top';
        haloText(ctx, c, txt, lx, ly + 5, on ? c.sc : c.ink3);
      });
      // angle arc
      if (th > 0) {
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.4;
        ctx.beginPath(); ctx.arc(cx, cy, 24, 0, -t, true); ctx.stroke();
        const a2 = t / 2;
        ctx.font = `italic 14px ${c.font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        haloText(ctx, c, 'θ', cx + 38 * Math.cos(a2), cy - 38 * Math.sin(a2), c.ink2);
      }
      // triangle: cos leg, sin leg, hypotenuse
      ctx.lineCap = 'round';
      ctx.strokeStyle = c.ink; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(px, py); ctx.stroke();
      if (Math.abs(cs) > 0.12 && Math.abs(sn) > 0.12) {
        const dxs = -Math.sign(cs) * 9, dys = Math.sign(sn) * 9;
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(px + dxs, cy); ctx.lineTo(px + dxs, cy - dys); ctx.lineTo(px, cy - dys); ctx.stroke();
      }
      ctx.lineWidth = 3.5;
      ctx.strokeStyle = c.sc2; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(px, cy); ctx.stroke();
      ctx.strokeStyle = c.sc; ctx.beginPath(); ctx.moveTo(px, cy); ctx.lineTo(px, py); ctx.stroke();
      ctx.font = `600 12px ${c.mono}`;
      if (Math.abs(cs) > 0.02) {
        ctx.textAlign = 'center'; ctx.textBaseline = sn >= 0 ? 'top' : 'bottom';
        haloText(ctx, c, 'cos θ', cx + R * cs / 2, cy + (sn >= 0 ? 6 : -6), c.sc2);
      }
      if (Math.abs(sn) > 0.02) {
        if (Math.abs(sn) < 0.3) {
          // short leg: label just beyond the point instead
          ctx.textAlign = 'center'; ctx.textBaseline = sn >= 0 ? 'bottom' : 'top';
          haloText(ctx, c, 'sin θ', px, py + (sn >= 0 ? -11 : 11), c.sc);
        } else {
          const tw = ctx.measureText('sin θ').width, lim = wide ? S : w - 2;
          let right = cs >= 0;
          if (right && px + 8 + tw > lim) right = false;
          if (!right && px - 8 - tw < 2) right = true;
          ctx.textAlign = right ? 'left' : 'right'; ctx.textBaseline = 'middle';
          haloText(ctx, c, 'sin θ', px + (right ? 8 : -8), cy - R * sn / 2, c.sc);
        }
      }
      // hypotenuse length 1
      if (Math.abs(sn) > 0.25 && Math.abs(cs) > 0.25) {
        const k = sn * cs >= 0 ? 1 : -1;
        const nx = -sn * k, ny = cs * k;
        ctx.font = `12px ${c.mono}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        haloText(ctx, c, '1', cx + R * cs / 2 + nx * 11, cy - R * sn / 2 - ny * 11, c.ink2);
      }
      dot(ctx, c, px, py, 7.5, c.sc);

      // sine strip
      ctx.strokeStyle = c.rule2; ctx.lineWidth = 1;
      ctx.beginPath();
      for (let d = 0; d <= 360; d += 90) { const x = Math.round(SX(d)) + 0.5; ctx.moveTo(x, sy0 - amp); ctx.lineTo(x, sy0 + amp); }
      for (const v of [-1, 1]) { const y = Math.round(sy0 - v * amp) + 0.5; ctx.moveTo(sx0, y); ctx.lineTo(sx1, y); }
      ctx.stroke();
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(sx0, Math.round(sy0) + 0.5); ctx.lineTo(sx1 + 4, Math.round(sy0) + 0.5);
      ctx.moveTo(Math.round(sx0) + 0.5, sy0 - amp - 8); ctx.lineTo(Math.round(sx0) + 0.5, sy0 + amp + 4); ctx.stroke();
      ctx.font = `11px ${c.mono}`; ctx.fillStyle = c.ink3;
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      ctx.fillText('1', sx0 - 5, sy0 - amp); ctx.fillText('−1', sx0 - 5, sy0 + amp); ctx.fillText('0', sx0 - 5, sy0);
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (let d = 90; d <= 360; d += 90) ctx.fillText(rad ? piFrac(d) : `${d}°`, SX(d), sy0 + amp + 6);
      ctx.font = `italic 13px ${c.font}`; ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      ctx.fillText('θ', sx1 + 7, sy0);
      ctx.textAlign = 'left'; ctx.textBaseline = 'bottom'; ctx.fillStyle = c.sc;
      ctx.fillText('y = sin θ', sx0 + 6, sy0 - amp - 4);
      // faint full curve, then traced part 0..θ
      const curve = (d0, d1) => { ctx.beginPath(); for (let d = d0; d <= d1 + 1e-9; d += 2) { const x = SX(d), y = sy0 - amp * Math.sin(d * Math.PI / 180); d === d0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y); } ctx.lineTo(SX(d1), sy0 - amp * Math.sin(d1 * Math.PI / 180)); };
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2; ctx.globalAlpha = 0.3; curve(0, 360); ctx.stroke(); ctx.globalAlpha = 1;
      if (th > 0) { ctx.lineWidth = 2.6; curve(0, th); ctx.stroke(); }
      ctx.strokeStyle = c.sc; ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.moveTo(qx, sy0); ctx.lineTo(qx, qy); ctx.stroke();
      dot(ctx, c, qx, qy, 5.5, c.sc);
    }

    // dragging: on the circle (angle from the centre) or along the sine strip
    let mode = null;
    function setFrom(e) {
      if (!G) return;
      const p = ptPos(cv, e);
      let d;
      if (mode === 'circle') {
        const dx = p.x - G.cx, dy = G.cy - p.y;
        if (Math.hypot(dx, dy) < 6) return;
        d = Math.round(Math.atan2(dy, dx) * 180 / Math.PI);
        d = ((d % 360) + 360) % 360;
      } else {
        d = Math.round(clamp((p.x - G.sx0) / (G.sx1 - G.sx0), 0, 1) * 360);
      }
      if (d !== th) { th = d; sl.set(th); update(); }
    }
    wrap.addEventListener('pointerdown', (e) => {
      if (!G || (e.button != null && e.button > 0)) return;
      const p = ptPos(cv, e);
      mode = (G.wide ? p.x < G.S + 10 : p.y < G.S) ? 'circle' : 'strip';
      try { wrap.setPointerCapture(e.pointerId); } catch (err) { /* ignore */ }
      setFrom(e);
    });
    wrap.addEventListener('pointermove', (e) => { if (mode) setFrom(e); });
    const stop = () => { mode = null; };
    wrap.addEventListener('pointerup', stop);
    wrap.addEventListener('pointercancel', stop);
    wrap.addEventListener('keydown', (e) => {
      const step = e.shiftKey ? 15 : 1;
      let d = th;
      if (e.key === 'ArrowRight' || e.key === 'ArrowUp') d += step;
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') d -= step;
      else return;
      e.preventDefault();
      th = ((d % 360) + 360) % 360; sl.set(th); update();
    });
    update();
  });

  /* ================= 3. stats — summary statistics, box plot, dot plot ================= */
  /** exact-looking number: strips float noise (0.30000000000000004 → 0.3), true minus sign */
  const fx = (v) => (isFinite(v) ? String(parseFloat(v.toPrecision(10))).replace(/-/g, '−').replace('e+', ' × 10^') : '—');
  function medianOf(a) { const n = a.length; if (!n) return NaN; const m = n >> 1; return n % 2 ? a[m] : (a[m - 1] + a[m]) / 2; }
  function ordinal(n) { const s = ['th', 'st', 'nd', 'rd'], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }
  /** place short labels in up to 3 rows above y so they never overlap. items: {x, text, color, font} */
  function placeLabels(ctx, c, items, y, rowH) {
    const rows = [];
    for (const it of items.slice().sort((a, b) => a.x - b.x)) {
      ctx.font = it.font;
      const wdt = ctx.measureText(it.text).width;
      let r = 0;
      while (r < 3 && rows[r] != null && rows[r] > it.x - wdt / 2 - 5) r++;
      if (r >= 3) r = 2;
      rows[r] = it.x + wdt / 2;
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      haloText(ctx, c, it.text, it.x, y - r * rowH, it.color);
    }
  }

  W.register('stats', function (el, o) {
    const id = nextId('st');
    const init = String(o.values || '3, 5, 7, 7, 9, 12, 15, 21').split(/[\s,;]+/).filter(Boolean).join(', ');
    const { body } = W.frame(el, 'Summary statistics', 'type or paste your own data');
    const ta = W.h('textarea', { id: `${id}-d`, rows: 2, spellcheck: 'false', autocomplete: 'off', style: { fontFamily: 'var(--f-mono)', resize: 'vertical' } });
    ta.value = init;
    ta.addEventListener('input', update);
    const btn = (text, fn) => W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', onclick: fn }, text);
    body.append(
      W.h('div', { class: 'w-ctl' }, W.h('label', { for: ta.id }, 'Data: numbers separated by commas or spaces'), ta),
      W.h('div', { class: 'w-row', style: { gap: '8px' } },
        btn('Sort the data', () => { const p = parseData(); if (p.xs.length) { ta.value = p.xs.slice().sort((a, b) => a - b).map((v) => fx(v).replace('−', '-')).join(', '); update(); } }),
        btn('Add an outlier', () => { const p = parseData(); if (p.xs.length) { const st = compute(p.xs); const v = Math.ceil(st.q3 + 3 * Math.max(st.iqr, 1)); ta.value = ta.value.replace(/[\s,;]*$/, '') + ', ' + v; update(); } }),
        btn('Reset', () => { ta.value = init; update(); })));
    const err = W.h('div', { class: 'w-err', role: 'status' });
    show(err, false);
    body.append(err);
    const cv = W.canvas(body, { height: 270, draw: safeDraw(draw) });
    cv.wrap.style.touchAction = 'pan-y';
    cv.wrap.setAttribute('role', 'img');
    const T = {};
    const mk = (k, label, hi) => (T[k] = W.stat(label, hi)).el;
    const rowA = W.h('div', { class: 'w-out' }, mk('n', 'n'), mk('sum', 'Σx'), mk('sum2', 'Σx²'), mk('mean', 'Mean x̄', true), mk('sd', 'σ (divide by n)'), mk('s', 's (divide by n − 1)'));
    const rowB = W.h('div', { class: 'w-out' }, mk('min', 'Min'), mk('q1', 'Q₁ (lower quartile)'), mk('med', 'Median Q₂', true), mk('q3', 'Q₃ (upper quartile)'), mk('max', 'Max'));
    const rowC = W.h('div', { class: 'w-out' }, mk('mode', 'Mode'), mk('range', 'Range'), mk('iqr', 'IQR = Q₃ − Q₁'));
    const work = W.h('div', { class: 'w-val', style: { display: 'grid', gap: '2px', lineHeight: '1.55', padding: '6px 0 6px 12px', borderLeft: '3px solid var(--sc-mid)' } });
    body.append(rowA, rowB, rowC, work, W.h('div', { class: 'w-note' },
      'Quartile method: Q₁ is the median of the lower half and Q₃ the median of the upper half; when n is odd the median is left out of both halves. ' +
      'Outliers lie more than 1.5 × IQR beyond the quartiles (red dashed fences). Try “Add an outlier” and watch the mean move more than the median.'));

    function parseData() {
      const toks = ta.value.replace(/[−–]/g, '-').split(/[\s,;]+/).filter(Boolean);
      const xs = [], bad = [];
      for (const t of toks) { const v = Number(t); if (isFinite(v)) xs.push(v); else bad.push(t); }
      return { xs: xs.slice(0, 5000), bad, cut: xs.length > 5000 };
    }
    function compute(xs) {
      const a = xs.slice().sort((p, q) => p - q), n = a.length;
      let sum = 0, sum2 = 0;
      for (const v of a) { sum += v; sum2 += v * v; }
      const mean = sum / n;
      let ss = 0;
      for (const v of a) ss += (v - mean) * (v - mean);
      const h = n >> 1;
      const lower = n === 1 ? a : a.slice(0, h), upper = n === 1 ? a : a.slice(n % 2 ? h + 1 : h);
      const q1 = medianOf(lower), q3 = medianOf(upper), iqr = q3 - q1;
      const lf = q1 - 1.5 * iqr, uf = q3 + 1.5 * iqr;
      const inside = a.filter((v) => v >= lf && v <= uf);
      const cnt = new Map();
      for (const v of a) cnt.set(v, (cnt.get(v) || 0) + 1);
      let mf = 0;
      for (const k of cnt.values()) mf = Math.max(mf, k);
      const modes = [...cnt.entries()].filter(([, k]) => k === mf).map(([v]) => v);
      return { a, n, sum, sum2, mean, sd: Math.sqrt(ss / n), s: n > 1 ? Math.sqrt(ss / (n - 1)) : NaN, med: medianOf(a), lower, upper, q1, q3, iqr, lf, uf,
        out: a.filter((v) => v < lf || v > uf), wl: inside.length ? inside[0] : q1, wh: inside.length ? inside[inside.length - 1] : q3,
        modes, mf, distinct: cnt.size, min: a[0], max: a[n - 1] };
    }
    const list = (arr) => (arr.length <= 12 ? arr.map(fx).join(', ') : `${arr.slice(0, 5).map(fx).join(', ')}, …, ${arr.slice(-3).map(fx).join(', ')}`);

    let S = null;
    function update() {
      const p = parseData();
      const msgs = [];
      if (p.bad.length) msgs.push(`Ignored ${p.bad.length === 1 ? 'an entry that is' : `${p.bad.length} entries that are`} not a number: ${p.bad.slice(0, 4).map((t) => `“${t}”`).join(', ')}${p.bad.length > 4 ? ' …' : ''}.`);
      if (p.cut) msgs.push('Only the first 5000 values are used.');
      if (!p.xs.length) msgs.push('Enter at least one number to see the statistics.');
      err.textContent = msgs.join(' ');
      show(err, msgs.length > 0);
      S = p.xs.length ? compute(p.xs) : null;
      if (!S) {
        for (const k in T) T[k].set('—');
        work.textContent = '';
        cv.wrap.setAttribute('aria-label', 'No data yet');
        cv.redraw();
        return;
      }
      const n = S.n;
      T.n.set(String(n)); T.sum.set(fx(S.sum)); T.sum2.set(fx(S.sum2));
      T.mean.set(W.fmt(S.mean, 4)); T.sd.set(W.fmt(S.sd, 4)); T.s.set(n > 1 ? W.fmt(S.s, 4) : 'needs n ≥ 2');
      T.min.set(fx(S.min)); T.q1.set(fx(S.q1)); T.med.set(fx(S.med)); T.q3.set(fx(S.q3)); T.max.set(fx(S.max));
      T.range.set(fx(S.max - S.min)); T.iqr.set(fx(S.iqr));
      let mode;
      if (n === 1) mode = fx(S.a[0]);
      else if (S.mf === 1 || S.modes.length === S.distinct) mode = 'none';
      else if (S.modes.length <= 3) mode = `${S.modes.map(fx).join(S.modes.length === 2 ? ' and ' : ', ')} (×${S.mf})`;
      else mode = `${S.modes.length} values tie`;
      T.mode.set(mode);
      // the working, in words
      const h = n >> 1;
      work.textContent = '';
      const line = (...kids) => work.append(W.h('div', {}, ...kids));
      if (n === 1) {
        line('With one value, the median and both quartiles equal it.');
      } else {
        const medTxt = n % 2
          ? `Median = ${fx(S.med)}, the ${ordinal(h + 1)} value (left out of both halves)`
          : `Median = ${fx(S.med)}, the mean of the ${ordinal(h)} and ${ordinal(h + 1)} values (${fx(S.a[h - 1])} and ${fx(S.a[h])})`;
        line(`Lower half (${S.lower.length}): ${list(S.lower)}  →  Q₁ = ${fx(S.q1)}`);
        line(medTxt);
        line(`Upper half (${S.upper.length}): ${list(S.upper)}  →  Q₃ = ${fx(S.q3)}`);
      }
      line(`Fences: Q₁ − 1.5 × IQR = ${fx(S.lf)},  Q₃ + 1.5 × IQR = ${fx(S.uf)}.  `,
        W.h('b', { style: { color: S.out.length ? 'var(--red)' : 'inherit', fontWeight: 600 } },
          S.out.length ? `Outlier${S.out.length > 1 ? 's' : ''}: ${list(S.out)}` : 'No outliers'));
      cv.wrap.setAttribute('aria-label', `Box plot and dot plot of ${n} values: min ${fx(S.min)}, lower quartile ${fx(S.q1)}, median ${fx(S.med)}, upper quartile ${fx(S.q3)}, max ${fx(S.max)}, mean ${W.fmt(S.mean, 4)}.`);
      cv.redraw();
    }

    function draw(ctx, w, h, c) {
      if (!S) {
        ctx.fillStyle = c.ink3; ctx.font = `13px ${c.font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('Type some numbers above to see the plots', w / 2, h / 2);
        return;
      }
      const L = 22, R = w - 26, axisY = h - 30;
      let lo = S.min, hi = S.max;
      if (!(hi - lo > 1e-12)) { lo -= 1; hi += 1; } else { const p = (hi - lo) * 0.06; lo -= p; hi += p; }
      const X = (v) => L + (v - lo) / (hi - lo) * (R - L);
      const boxY = 64, bh = 15, dTop = boxY + bh + 22, dBase = axisY - 2;
      const ticks = W.ticks(lo, hi, Math.max(3, Math.round((R - L) / 64)));
      // grid and number line
      ctx.strokeStyle = c.rule2; ctx.lineWidth = 1;
      ctx.beginPath();
      for (const t of ticks) { const x = Math.round(X(t)) + 0.5; ctx.moveTo(x, 10); ctx.lineTo(x, axisY); }
      ctx.stroke();
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.3;
      ctx.beginPath(); ctx.moveTo(L - 10, Math.round(axisY) + 0.5); ctx.lineTo(R + 8, Math.round(axisY) + 0.5);
      for (const t of ticks) { const x = Math.round(X(t)) + 0.5; ctx.moveTo(x, axisY); ctx.lineTo(x, axisY + 5); }
      ctx.stroke();
      ctx.fillStyle = c.ink3; ctx.font = `11px ${c.mono}`; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (const t of ticks) ctx.fillText(W.fmt(t, 4), X(t), axisY + 8);
      ctx.font = `italic 13px ${c.font}`; ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      ctx.fillText('x', R + 12, axisY);
      // outlier fences
      ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = c.red; ctx.globalAlpha = 0.6; ctx.lineWidth = 1.3;
      for (const f of [S.lf, S.uf]) if (f > lo && f < hi) { const x = Math.round(X(f)) + 0.5; ctx.beginPath(); ctx.moveTo(x, boxY - bh - 8); ctx.lineTo(x, boxY + bh + 8); ctx.stroke(); }
      ctx.restore();
      // mean line through both plots
      const xb = X(S.mean);
      ctx.save(); ctx.setLineDash([5, 4]); ctx.strokeStyle = c.sc2; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(xb, boxY - bh - 4); ctx.lineTo(xb, axisY); ctx.stroke(); ctx.restore();
      // box plot
      const x1 = X(S.q1), x3 = X(S.q3), xm = X(S.med), xl = X(S.wl), xh = X(S.wh);
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.6;
      ctx.beginPath();
      ctx.moveTo(xl, boxY); ctx.lineTo(x1, boxY); ctx.moveTo(x3, boxY); ctx.lineTo(xh, boxY);
      ctx.moveTo(xl, boxY - 9); ctx.lineTo(xl, boxY + 9); ctx.moveTo(xh, boxY - 9); ctx.lineTo(xh, boxY + 9);
      ctx.stroke();
      ctx.fillStyle = c.sc; ctx.globalAlpha = 0.15; ctx.fillRect(x1, boxY - bh, x3 - x1, 2 * bh); ctx.globalAlpha = 1;
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2; ctx.strokeRect(x1, boxY - bh, Math.max(0.5, x3 - x1), 2 * bh);
      ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(xm, boxY - bh); ctx.lineTo(xm, boxY + bh); ctx.stroke();
      ctx.strokeStyle = c.red; ctx.lineWidth = 2;
      for (const v of S.out) { ctx.beginPath(); ctx.arc(X(v), boxY, 4.5, 0, Math.PI * 2); ctx.stroke(); }
      placeLabels(ctx, c, [
        { x: x1, text: 'Q₁', color: c.sc, font: `600 12px ${c.mono}` },
        { x: xm, text: 'Q₂', color: c.sc, font: `600 12px ${c.mono}` },
        { x: x3, text: 'Q₃', color: c.sc, font: `600 12px ${c.mono}` },
        { x: xb, text: 'x̄', color: c.sc2, font: `italic 600 14px ${c.font}` }], boxY - bh - 5, 15);
      // dot plot: stacks of equal (or very close) values
      const avail = dBase - dTop;
      let r = 5.5, groups = [];
      for (let it = 0; it < 4; it++) {
        groups = [];
        let g = null;
        for (const v of S.a) {
          const x = X(v);
          if (g && x - g.x < 2 * r) g.vals.push(v); else { g = { x, vals: [v] }; groups.push(g); }
        }
        const tall = Math.max(...groups.map((q) => q.vals.length));
        if (tall * 2 * r <= avail || r <= 1.6) break;
        r = Math.max(1.6, avail / (2 * tall));
      }
      for (const g of groups) {
        g.vals.forEach((v, i) => {
          const y = dBase - r - i * 2 * r;
          if (y < dTop - r) return;
          ctx.beginPath(); ctx.arc(g.x, y, Math.max(1.2, r - 0.8), 0, Math.PI * 2);
          ctx.fillStyle = v < S.lf || v > S.uf ? c.red : c.sc; ctx.fill();
        });
      }
    }
    update();
  });
  /* ================= iteration — x(n+1) = F(x(n)) staircase and table ================= */
  W.register('iteration', function (el, o) {
    const DEF_F = '(2x+5)^(1/3)';
    const warn = [];
    let rng = pair(o.range);
    if (rng === 'bad') { warn.push('data-range should look like "1,3", so the range 1 to 3 is used.'); rng = null; }
    if (!rng) rng = o.f || o.fn ? [0, 4] : [1, 3];
    const lo = rng[0], hi = rng[1];
    const NMAX = 30;
    let nSteps = Math.round(clamp(num(o.n, 8), 1, NMAX));
    let x0 = clamp(num(o.x0, o.f || o.fn ? (lo + hi) / 2 : 2), lo, hi);
    let src = stripLhs(String(o.f || o.fn || DEF_F));
    let fn = null, err = '';
    const scope = {};
    const evalF = (x) => { scope.x = x; try { const v = fn(scope); return typeof v === 'number' ? v : NaN; } catch (e) { return NaN; } };

    function parseF() {
      fn = null; err = '';
      if (!src.trim()) { err = 'Type F(x), for example (2x+5)^(1/3).'; return; }
      try {
        const r = W.parse(src, {});
        const bad = [...(r.vars || [])].filter((v) => v !== 'x');
        if (bad.length) { err = `F can only use the letter x, not ${bad.join(', ')}.`; return; }
        fn = r.f;
      } catch (e) { err = String(e.message || 'could not read this'); }
    }

    const { body } = W.frame(el, 'Iteration', 'x₍ₙ₊₁₎ = F(xₙ): follow the staircase to the root');
    const cv = W.canvas(body, { height: 300, draw: safeDraw(draw) });
    cv.wrap.setAttribute('role', 'img');
    const fIn = W.field({ label: 'F(x) =', value: src, type: 'text', width: '16rem', placeholder: 'e.g. (2x+5)^(1/3)', oninput: (v) => { src = stripLhs(String(v)); update(); } });
    fIn.input.setAttribute('aria-label', 'The function F of x in the iteration');
    fIn.input.setAttribute('spellcheck', 'false'); fIn.input.setAttribute('autocomplete', 'off');
    const stepX = hi - lo > 50 ? 0.1 : hi - lo >= 1 ? 0.01 : 0.001;
    const sx0 = W.slider({ label: 'Start x₀', min: lo, max: hi, step: stepX, value: x0, fmt: (v) => W.fix(v, 3), oninput: (v) => { x0 = v; update(); } });
    sx0.input.setAttribute('aria-label', 'Starting value x zero');
    const sn = W.slider({ label: 'Steps', min: 1, max: NMAX, step: 1, value: nSteps, fmt: (v) => String(v), oninput: (v) => { nSteps = Math.round(v); update(); } });
    sn.input.setAttribute('aria-label', 'Number of iteration steps');
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'end' } }, fIn.el, sx0.el, sn.el));
    const errEl = W.h('div', { class: 'w-err', role: 'status' });
    show(errEl, false);
    body.append(errEl);
    const verdict = W.stat('What happens', true);
    const lim = W.stat('Last value');
    body.append(W.h('div', { class: 'w-out' }, verdict.el, lim.el));
    const grid = W.h('div', { style: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(10.5rem, 1fr))', gap: '2px 12px', fontFamily: 'var(--f-mono)', fontSize: '0.85rem' }, 'aria-label': 'Table of iterates' });
    body.append(grid);
    body.append(W.h('div', { class: 'w-note' }, 'The staircase starts on the x-axis at x₀, goes up to the curve y = F(x), across to the line y = x, and repeats. Where the staircase closes in, F(x) = x: that is the root. Try x₀ near the ends of the range, or the rearrangement (x^3-5)/2, which runs away.'));
    if (warn.length) body.append(W.h('div', { class: 'w-err' }, warn.join(' ')));

    const big = (v) => (Math.abs(v) >= 1e6 || (v !== 0 && Math.abs(v) < 1e-4)) ? W.fmt(v, 4) : W.fix(v, 6);
    let xs = [];
    let stopped = '';
    function run() {
      xs = [x0]; stopped = '';
      if (!fn) return;
      for (let i = 0; i < nSteps; i++) {
        const v = evalF(xs[xs.length - 1]);
        if (!isFinite(v)) { stopped = 'undefined'; break; }
        xs.push(v);
        if (Math.abs(v) > 1e12) { stopped = 'huge'; break; }
      }
    }
    function describe() {
      if (!fn) return ['Check F(x)', ''];
      const n = xs.length - 1;
      if (stopped === 'undefined') return [`F is not defined at x${sub(n)} = ${W.fix(xs[n], 4)}, so the sequence stops`, W.fix(xs[n], 6)];
      const last = xs[n];
      if (stopped === 'huge' || Math.abs(last) > 1e6) return ['The values grow without limit: it diverges', ''];
      if (n < 2) return ['Add steps to see the pattern', big(last)];
      const d = [];
      for (let i = 1; i <= n; i++) d.push(xs[i] - xs[i - 1]);
      const dl = Math.abs(d[d.length - 1]);
      if (dl < 5e-7 * Math.max(1, Math.abs(last))) return [`Converges: the root is about ${W.fix(last, 5)}`, big(last)];
      const tail = d.slice(-4);
      const alt = tail.length >= 2 && tail.every((v, i) => i === 0 || v * tail[i - 1] < 0);
      const shrink = Math.abs(d[d.length - 1]) < Math.abs(d[Math.max(0, d.length - 4)]);
      if (shrink) return [alt ? 'Closing in on a limit, alternating either side: add steps' : 'Closing in on a limit: add steps to see more decimals', big(last)];
      return [alt ? 'The values jump either side and do not settle: it does not converge' : 'The values move away from the start: it does not converge', big(last)];
    }
    function update() {
      parseF();
      show(errEl, !!err);
      errEl.textContent = err;
      run();
      const [msg, lastTxt] = describe();
      verdict.set(msg);
      lim.set(lastTxt || '—');
      grid.textContent = '';
      xs.forEach((v, i) => grid.append(W.h('div', {}, `x${sub(i)} = ${isFinite(v) ? big(v) : '—'}`)));
      cv.wrap.setAttribute('aria-label', `Staircase diagram for the iteration F(x) = ${src}, starting at x ${W.fix(x0, 3)}. ${msg}.`);
      cv.redraw();
    }

    function draw(ctx, w, h, c) {
      const pad = { l: 38, r: 14, t: 10, b: 26 };
      const view = { x0: lo, x1: hi, y0: lo, y1: hi };
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 'x', ylabel: 'y' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      // y = x
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.6; ctx.setLineDash([6, 5]);
      ctx.beginPath(); ctx.moveTo(X(lo), Y(lo)); ctx.lineTo(X(hi), Y(hi)); ctx.stroke(); ctx.setLineDash([]);
      // y = F(x)
      if (fn) {
        const N = Math.max(60, Math.round(w - pad.l - pad.r));
        ctx.beginPath();
        traceCurve(ctx, evalF, lo, (hi - lo) / N, N, X, Y);
        ctx.strokeStyle = c.sc; ctx.lineWidth = 2.4; ctx.lineJoin = 'round'; ctx.stroke();
      }
      // staircase
      if (fn && xs.length > 1) {
        ctx.beginPath();
        ctx.moveTo(X(xs[0]), Y(lo));
        for (let i = 0; i < xs.length - 1; i++) {
          const a = xs[i], b = xs[i + 1];
          ctx.lineTo(X(a), Y(b));
          ctx.lineTo(X(b), Y(b));
        }
        ctx.strokeStyle = c.sc2; ctx.lineWidth = 1.6; ctx.lineJoin = 'round'; ctx.stroke();
        // points on y = x with labels for the first few
        ctx.font = `12px ${c.font}`; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
        xs.slice(0, 8).forEach((v, i) => {
          if (!isFinite(v)) return;
          ctx.beginPath(); ctx.arc(X(v), Y(v), i === 0 ? 4 : 3, 0, Math.PI * 2);
          ctx.fillStyle = i === 0 ? c.red : c.sc2; ctx.fill();
          if (i < 4) haloText(ctx, c, 'x' + sub(i), X(v) + 5, Y(v) - 4, c.ink2);
        });
        const lastV = xs[xs.length - 1];
        if (isFinite(lastV) && Math.abs(lastV - xs[xs.length - 2]) < 1e-4 * (hi - lo)) {
          ctx.beginPath(); ctx.arc(X(lastV), Y(lastV), 7, 0, Math.PI * 2);
          ctx.strokeStyle = c.red; ctx.lineWidth = 2; ctx.stroke();
        }
      }
      ctx.restore();
    }
    update();
  });

  /* ================= argand — complex numbers: operations and loci ================= */
  W.register('argand', function (el, o) {
    const warn = [];
    const xy = (s, dflt, name) => {
      if (s == null || String(s).trim() === '') return dflt.slice();
      const p = String(s).replace(/[−–]/g, '-').split(',').map((t) => parseFloat(t));
      if (p.length >= 2 && isFinite(p[0]) && isFinite(p[1])) return [clamp(p[0], -6, 6), clamp(p[1], -6, 6)];
      warn.push(`${name} should look like "3,2", so ${dflt.join(',')} is used.`);
      return dflt.slice();
    };
    const angleOf = (s, dflt) => {
      if (s == null || String(s).trim() === '') return dflt;
      try { const v = W.parse(String(s), {}).f({}); if (typeof v === 'number' && isFinite(v)) return v; } catch (e) { /* fall through */ }
      warn.push('data-alpha should be a number of radians such as 0.785 or pi/4, so pi/4 is used.');
      return dflt;
    };
    const mraw = String(o.mode || 'ops').trim().toLowerCase();
    const mode = mraw === 'locus' ? 'locus' : 'ops';
    if (o.mode && mraw !== 'ops' && mraw !== 'locus') warn.push('data-mode should be "ops" or "locus", so "ops" is used.');

    const PI = Math.PI;
    const snap = (v) => Math.round(clamp(v, -6, 6) * 10) / 10;
    const z0 = (v) => (Math.abs(v) < 1e-9 ? 0 : v);
    const nf = (v) => W.fmt(z0(v), 3);
    const cstr = (z) => {
      const re = z0(z[0]), im = z0(z[1]);
      if (im === 0) return nf(re);
      const imS = Math.abs(im) === 1 ? '' : W.fmt(Math.abs(im), 3);
      if (re === 0) return (im < 0 ? '−' : '') + imS + 'i';
      return `${nf(re)} ${im < 0 ? '−' : '+'} ${imS}i`;
    };
    const modOf = (z) => Math.hypot(z[0], z[1]);
    const argOf = (z) => { if (Math.hypot(z[0], z[1]) < 1e-12) return NaN; const t = Math.atan2(z[1], z[0]); return t <= -PI + 1e-12 ? PI : t; };
    const cmul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
    const cdiv = (a, b) => { const d = b[0] * b[0] + b[1] * b[1]; return d < 1e-12 ? null : [(a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d]; };
    const argTxt = (t) => (isFinite(t) ? W.fmt(z0(t), 3) : '—');

    // ---- state
    let z1 = xy(o.z1, [3, 2], 'data-z1'), z2 = xy(o.z2, [1, -1], 'data-z2');
    let res = 'mul';
    const lraw = String(o.locus || 'circle').trim().toLowerCase();
    let type = ['circle', 'bisector', 'arg'].includes(lraw) ? lraw : 'circle';
    if (mode === 'locus' && o.locus && type !== lraw) warn.push('data-locus should be circle, bisector or arg, so circle is used.');
    const DEF = { circle: { a: [3, 2], b: [0, 0], k: 2, al: PI / 4 }, bisector: { a: [1, 0], b: [0, 1], k: 2, al: PI / 4 }, arg: { a: [1, 1], b: [0, 0], k: 2, al: PI / 4 } };
    let a = xy(o.a, DEF[type].a, 'data-a'), b = xy(o.b, DEF[type].b, 'data-b');
    let kk = clamp(num(o.k, 2), 0.2, 6);
    let alpha = clamp(angleOf(o.alpha, PI / 4), -PI, PI);
    const relMap = { '=': '=', '<': '<', '<=': '<=', '≤': '<=', '>': '>', '>=': '>=', '≥': '>=' };
    let rel = relMap[String(o.rel || '=').trim()] || '=';
    const RELS = [['=', '='], ['<', '<'], ['<=', '≤'], ['>', '>'], ['>=', '≥']];
    const relSym = () => (RELS.find((r) => r[0] === rel) || RELS[0])[1];

    const { body } = W.frame(el, 'Argand diagram', mode === 'ops' ? 'Drag z₁ and z₂ (or use the sliders) and watch the results' : 'Move the centre, radius or angle and see the locus and its equation');
    const cv = W.canvas(body, { height: 340, draw: safeDraw(draw) });
    cv.wrap.setAttribute('role', 'img');
    const mk = (label, min, max, step, val, fmt, on) => {
      const s = W.slider({ label, min, max, step, value: val, fmt, oninput: on });
      s.input.setAttribute('aria-label', label);
      return s;
    };
    const f1 = (v) => W.fix(v, 1), f2 = (v) => W.fix(v, 2);
    const errEl = W.h('div', { class: 'w-err', role: 'status' });
    show(errEl, false);

    let geo = null;   // last drawing geometry for dragging
    let sl = {};
    let resTabs = null, typeTabs = null, relTabs = null;
    let rowsEl = null, tile1 = null, tile2 = null, tile3 = null;

    if (mode === 'ops') {
      sl.r1 = mk('Re z₁', -6, 6, 0.1, z1[0], f1, (v) => { z1[0] = v; update(); });
      sl.i1 = mk('Im z₁', -6, 6, 0.1, z1[1], f1, (v) => { z1[1] = v; update(); });
      sl.r2 = mk('Re z₂', -6, 6, 0.1, z2[0], f1, (v) => { z2[0] = v; update(); });
      sl.i2 = mk('Im z₂', -6, 6, 0.1, z2[1], f1, (v) => { z2[1] = v; update(); });
      body.append(W.h('div', { class: 'w-row' }, sl.r1.el, sl.i1.el), W.h('div', { class: 'w-row' }, sl.r2.el, sl.i2.el));
      resTabs = tabs([['add', 'z₁ + z₂'], ['mul', 'z₁ z₂'], ['div', 'z₁ ÷ z₂'], ['conj', 'z₁*']], res, (v) => { res = v; update(); }, 'Result to draw');
      body.append(W.h('div', { class: 'w-row' }, W.h('span', { class: 'w-lab' }, 'Draw'), resTabs.el));
      body.append(errEl);
      rowsEl = W.h('table', { 'aria-label': 'Values, moduli and arguments' });
      body.append(W.h('div', { style: { overflowX: 'auto' } }, rowsEl));
      body.append(W.h('div', { class: 'w-note' }, 'Look at the moduli and arguments in the table: for z₁z₂ the moduli multiply and the arguments add; for z₁ ÷ z₂ the moduli divide and the arguments subtract. Arguments are in radians, in the range −π to π.'));
    } else {
      typeTabs = tabs([['circle', '|z − a| = k'], ['bisector', '|z − a| = |z − b|'], ['arg', 'arg(z − a) = α']], type, (v) => {
        type = v; const d = DEF[v]; a = d.a.slice(); b = d.b.slice(); kk = d.k; alpha = d.al;
        sl.ar.set(a[0]); sl.ai.set(a[1]); sl.br.set(b[0]); sl.bi.set(b[1]); sl.k.set(kk); sl.al.set(alpha);
        update();
      }, 'Type of locus');
      relTabs = tabs(RELS, rel, (v) => { rel = v; update(); }, 'Equality or inequality');
      body.append(W.h('div', { class: 'w-row' }, typeTabs.el));
      sl.ar = mk('Re a', -6, 6, 0.1, a[0], f1, (v) => { a[0] = v; update(); });
      sl.ai = mk('Im a', -6, 6, 0.1, a[1], f1, (v) => { a[1] = v; update(); });
      sl.br = mk('Re b', -6, 6, 0.1, b[0], f1, (v) => { b[0] = v; update(); });
      sl.bi = mk('Im b', -6, 6, 0.1, b[1], f1, (v) => { b[1] = v; update(); });
      sl.k = mk('Radius k', 0.2, 6, 0.1, kk, f1, (v) => { kk = v; update(); });
      sl.al = mk('Angle α (rad)', -PI, PI, 0.01, alpha, f2, (v) => { alpha = v; update(); });
      body.append(W.h('div', { class: 'w-row' }, sl.ar.el, sl.ai.el, sl.br.el, sl.bi.el, sl.k.el, sl.al.el));
      body.append(W.h('div', { class: 'w-row' }, W.h('span', { class: 'w-lab' }, 'Shade'), relTabs.el));
      body.append(errEl);
      tile1 = W.stat('Locus', true); tile2 = W.stat('Cartesian equation'); tile3 = W.stat('Shaded region');
      body.append(W.h('div', { class: 'w-out' }, tile1.el, tile2.el, tile3.el));
      body.append(W.h('div', { class: 'w-note' }, '“=” draws the locus only. “<” and “>” shade one side with a dashed boundary (not included); “≤” and “≥” use a solid boundary (included). For arg(z − a) the shading uses the principal argument, −π to π.'));
    }
    if (warn.length) body.append(W.h('div', { class: 'w-err' }, warn.join(' ')));

    // ---- maths
    function results() {
      return { add: [z1[0] + z2[0], z1[1] + z2[1]], mul: cmul(z1, z2), div: cdiv(z1, z2), conj: [z1[0], -z1[1]] };
    }
    const cmp = (l, r) => (rel === '<' ? l < r : rel === '<=' ? l <= r : rel === '>' ? l > r : rel === '>=' ? l >= r : false);
    function inside(x, y) {
      if (type === 'circle') return cmp(Math.hypot(x - a[0], y - a[1]), kk);
      if (type === 'bisector') return cmp(Math.hypot(x - a[0], y - a[1]), Math.hypot(x - b[0], y - b[1]));
      const t = argOf([x - a[0], y - a[1]]);
      return isFinite(t) && cmp(t, alpha);
    }
    const sq = (v, n) => (z0(v) === 0 ? `${n}²` : `(${n} ${v > 0 ? '−' : '+'} ${W.fmt(Math.abs(v), 3)})²`);
    const shift = (n, v) => (z0(v) === 0 ? n : `${n} ${v > 0 ? '−' : '+'} ${W.fmt(Math.abs(v), 3)}`);
    const lin = (m, c) => {
      const ms = z0(m) === 0 ? '' : Math.abs(m - 1) < 1e-9 ? 'x' : Math.abs(m + 1) < 1e-9 ? '−x' : `${W.fmt(m, 3)}x`;
      if (!ms) return nf(c);
      return z0(c) === 0 ? ms : `${ms} ${c < 0 ? '−' : '+'} ${W.fmt(Math.abs(c), 3)}`;
    };
    function describe() {
      const ac = cstr(a), bc = cstr(b), s = relSym();
      if (type === 'circle') {
        const inn = rel === '<' || rel === '<=', out = rel === '>' || rel === '>=';
        return [`${rel === '=' ? 'Circle' : (inn ? 'Disc' : 'Outside of a circle')}: centre ${ac}, radius ${W.fmt(kk, 3)}`,
          `${sq(a[0], 'x')} + ${sq(a[1], 'y')} ${s} ${W.fmt(kk * kk, 3)}`,
          rel === '=' ? 'none (line only)' : (inn ? 'inside the circle' : out ? 'outside the circle' : '')];
      }
      if (type === 'bisector') {
        const p = b[0] - a[0], q = b[1] - a[1], r = (b[0] * b[0] + b[1] * b[1] - a[0] * a[0] - a[1] * a[1]) / 2;
        if (Math.hypot(p, q) < 1e-9) return [`a and b are the same point`, 'every z satisfies it', ''];
        const eqn = Math.abs(q) < 1e-9 ? `x ${s} ${W.fmt(r / p, 3)}` : `y = ${lin(-p / q, r / q)}`;
        const near = rel === '<' || rel === '<=' ? 'the side nearer a' : rel === '>' || rel === '>=' ? 'the side nearer b' : 'none (line only)';
        return [`Perpendicular bisector of the line from ${ac} to ${bc}`, rel !== '=' && Math.abs(q) >= 1e-9 ? `${eqn} (boundary)` : eqn, near];
      }
      const cs = Math.cos(alpha), sn = Math.sin(alpha);
      const eqn = Math.abs(cs) < 1e-9 ? `x = ${nf(a[0])}, y ${sn > 0 ? '>' : '<'} ${nf(a[1])}`
        : `${shift('y', a[1])} = ${W.fmt(Math.tan(alpha), 3)}(${shift('x', a[0])}), x ${cs > 0 ? '>' : '<'} ${nf(a[0])}`;
      return [`Half-line from ${ac} at angle ${W.fmt(alpha, 3)} rad (${W.fmt(alpha * 180 / PI, 3)}°), not including ${ac}`, eqn,
        rel === '=' ? 'none (line only)' : (rel === '<' || rel === '<=') ? 'arguments below α (anticlockwise from −π)' : 'arguments above α'];
    }

    function update() {
      let msg = '';
      if (mode === 'ops') {
        const r = results();
        const rows = [['z₁', z1], ['z₂', z2], ['z₁ + z₂', r.add], ['z₁ z₂', r.mul], ['z₁ ÷ z₂', r.div], ['z₁*', r.conj]];
        const keys = [null, null, 'add', 'mul', 'div', 'conj'];
        rowsEl.textContent = '';
        rowsEl.append(W.h('thead', {}, W.h('tr', {}, W.h('th', {}, ''), W.h('th', {}, 'Value'), W.h('th', {}, '|z|'), W.h('th', {}, 'arg z'))));
        const tb = W.h('tbody', {});
        rows.forEach(([name, z], i) => {
          const hl = keys[i] && keys[i] === res;
          tb.append(W.h('tr', { style: hl ? { fontWeight: '700' } : {} },
            W.h('td', {}, name), W.h('td', {}, z ? cstr(z) : 'undefined'), W.h('td', {}, z ? W.fmt(modOf(z), 3) : '—'), W.h('td', {}, z ? argTxt(argOf(z)) : '—')));
        });
        rowsEl.append(tb);
        if (res === 'div' && !r.div) msg = 'z₂ = 0, so z₁ ÷ z₂ is undefined.';
        if (modOf(z1) < 1e-9 || modOf(z2) < 1e-9) msg = (msg ? msg + ' ' : '') + 'A number equal to 0 has no argument.';
        cv.wrap.setAttribute('aria-label', `Argand diagram with z1 = ${cstr(z1)} and z2 = ${cstr(z2)}. z1 plus z2 is ${cstr(r.add)}, z1 times z2 is ${cstr(r.mul)}.`);
      } else {
        const [d1, d2, d3] = describe();
        tile1.set(d1); tile2.set(d2); tile3.set(d3 || '—');
        if (type === 'bisector' && Math.hypot(b[0] - a[0], b[1] - a[1]) < 1e-9) msg = 'a and b are the same point, so move b away from a to see the bisector.';
        cv.wrap.setAttribute('aria-label', `Argand diagram. ${d1}. Equation ${d2}.`);
        show(sl.br.el, type === 'bisector'); show(sl.bi.el, type === 'bisector');
        show(sl.k.el, type === 'circle'); show(sl.al.el, type === 'arg');
      }
      errEl.textContent = msg;
      show(errEl, !!msg);
      cv.redraw();
    }

    // ---- drawing
    function arrow(ctx, x0, y0, x1, y1, col, lw, dash) {
      const dx = x1 - x0, dy = y1 - y0, L = Math.hypot(dx, dy);
      if (L < 2) return;
      ctx.save();
      ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = lw; ctx.setLineDash(dash || []);
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke(); ctx.setLineDash([]);
      if (!dash) {
        const ux = dx / L, uy = dy / L, hl = Math.min(10, L * 0.4);
        ctx.beginPath(); ctx.moveTo(x1, y1);
        ctx.lineTo(x1 - ux * hl + uy * hl * 0.45, y1 - uy * hl - ux * hl * 0.45);
        ctx.lineTo(x1 - ux * hl - uy * hl * 0.45, y1 - uy * hl + ux * hl * 0.45);
        ctx.closePath(); ctx.fill();
      }
      ctx.restore();
    }
    function arcAt(ctx, x, y, r, theta) {
      ctx.beginPath(); ctx.arc(x, y, r, 0, -theta, theta > 0); ctx.stroke();
    }
    function label(ctx, c, text, x, y, color, w, pad) {
      const tw = ctx.measureText(text).width;
      haloText(ctx, c, text, clamp(x, pad.l + 2, w - pad.r - tw - 2), clamp(y, pad.t + 12, 400), color);
    }

    function draw(ctx, w, h, c) {
      const pad = { l: 34, r: 14, t: 10, b: 26 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      let R = 7;
      const r = results();
      if (mode === 'ops') {
        const pts = [z1, z2].concat(r[res] ? [r[res]] : []);
        const m = Math.max(...pts.map((p) => Math.max(Math.abs(p[0]), Math.abs(p[1]))));
        R = Math.max(4, Math.ceil(m + 0.5));
      }
      const asp = pw / ph;
      const view = { x0: -R * asp, x1: R * asp, y0: -R, y1: R };
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 'Re', ylabel: 'Im' });
      const X = A.X, Y = A.Y, sc = pw / (view.x1 - view.x0);
      geo = { pad, w, h, view, X, Y, pw, ph };
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
      ctx.font = `13px ${c.font}`; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      if (mode === 'ops') {
        const o0 = [X(0), Y(0)];
        const p1 = [X(z1[0]), Y(z1[1])], p2 = [X(z2[0]), Y(z2[1])];
        const rz = r[res];
        if (res === 'add' && rz) {
          const ps = [X(rz[0]), Y(rz[1])];
          arrow(ctx, p1[0], p1[1], ps[0], ps[1], c.ink3, 1.4, [5, 4]);
          arrow(ctx, p2[0], p2[1], ps[0], ps[1], c.ink3, 1.4, [5, 4]);
        }
        if (rz) {
          const pr = [X(rz[0]), Y(rz[1])];
          arrow(ctx, o0[0], o0[1], pr[0], pr[1], c.red, 2.4);
          ctx.strokeStyle = c.red; ctx.lineWidth = 1.2; ctx.setLineDash([3, 3]);
          if (res === 'mul' || res === 'div' || res === 'conj') arcAt(ctx, o0[0], o0[1], 26, argOf(rz) || 0);
          ctx.setLineDash([]);
          const nm = { add: 'z₁ + z₂', mul: 'z₁z₂', div: 'z₁ ÷ z₂', conj: 'z₁*' }[res];
          label(ctx, c, nm, pr[0] + 7, pr[1] - 7, c.red, w, pad);
        }
        arrow(ctx, o0[0], o0[1], p1[0], p1[1], c.sc, 2.4);
        arrow(ctx, o0[0], o0[1], p2[0], p2[1], c.sc2, 2.4);
        [[p1, c.sc, 'z₁'], [p2, c.sc2, 'z₂']].forEach(([p, col, nm]) => {
          ctx.beginPath(); ctx.arc(p[0], p[1], 5, 0, PI * 2); ctx.fillStyle = col; ctx.fill();
          ctx.strokeStyle = c.sheet; ctx.lineWidth = 1.5; ctx.stroke();
          label(ctx, c, nm, p[0] + 8, p[1] + 16, col, w, pad);
        });
      } else {
        // shading by sampling
        if (rel !== '=' && !(type === 'bisector' && Math.hypot(b[0] - a[0], b[1] - a[1]) < 1e-9)) {
          ctx.globalAlpha = 0.16; ctx.fillStyle = c.sc;
          const st = 3;
          for (let px = pad.l; px < pad.l + pw; px += st) {
            for (let py = pad.t; py < pad.t + ph; py += st) {
              const x = view.x0 + (px + st / 2 - pad.l) / pw * (view.x1 - view.x0);
              const y = view.y1 - (py + st / 2 - pad.t) / ph * (view.y1 - view.y0);
              if (inside(x, y)) ctx.fillRect(px, py, st, st);
            }
          }
          ctx.globalAlpha = 1;
        }
        // boundary
        ctx.strokeStyle = c.sc; ctx.lineWidth = 2.4; ctx.lineJoin = 'round';
        ctx.setLineDash(rel === '<' || rel === '>' ? [8, 6] : []);
        const ax = X(a[0]), ay = Y(a[1]);
        if (type === 'circle') {
          ctx.beginPath(); ctx.arc(ax, ay, kk * sc, 0, PI * 2); ctx.stroke();
          ctx.setLineDash([3, 3]); ctx.lineWidth = 1.2; ctx.strokeStyle = c.ink3;
          ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(ax + kk * sc, ay); ctx.stroke();
        } else if (type === 'bisector') {
          const p = b[0] - a[0], q = b[1] - a[1], L = Math.hypot(p, q);
          if (L > 1e-9) {
            const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = -q / L, dy = p / L;
            ctx.beginPath(); ctx.moveTo(X(mx - 40 * dx), Y(my - 40 * dy)); ctx.lineTo(X(mx + 40 * dx), Y(my + 40 * dy)); ctx.stroke();
          }
        } else {
          ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(X(a[0] + 40 * Math.cos(alpha)), Y(a[1] + 40 * Math.sin(alpha))); ctx.stroke();
          ctx.setLineDash([]); ctx.lineWidth = 1.2; ctx.strokeStyle = c.ink3;
          ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(ax + 60, ay); ctx.stroke();
          ctx.strokeStyle = c.red; ctx.lineWidth = 1.6; arcAt(ctx, ax, ay, 30, alpha);
          label(ctx, c, 'α', ax + 34 * Math.cos(alpha / 2), ay - 34 * Math.sin(alpha / 2) + 4, c.red, w, pad);
        }
        ctx.setLineDash([]);
        // points a (and b)
        const dotAt = (pt, nm, hollow) => {
          ctx.beginPath(); ctx.arc(X(pt[0]), Y(pt[1]), 5, 0, PI * 2);
          ctx.fillStyle = hollow ? c.sheet : c.red; ctx.fill(); ctx.strokeStyle = hollow ? c.sc : c.sheet; ctx.lineWidth = hollow ? 2 : 1.5; ctx.stroke();
          label(ctx, c, nm, X(pt[0]) + 8, Y(pt[1]) + 16, c.ink2, w, pad);
        };
        dotAt(a, 'a', type === 'arg');
        if (type === 'bisector') dotAt(b, 'b', false);
      }
      ctx.restore();
    }

    // ---- dragging (mouse and pen; touch uses the sliders so the page can still scroll)
    let drag = null;
    function handles() {
      if (mode === 'ops') return [{ pt: z1, s: [sl.r1, sl.i1] }, { pt: z2, s: [sl.r2, sl.i2] }];
      return type === 'bisector' ? [{ pt: a, s: [sl.ar, sl.ai] }, { pt: b, s: [sl.br, sl.bi] }] : [{ pt: a, s: [sl.ar, sl.ai] }];
    }
    const st = { cv: cv.cv, get w() { return geo ? geo.w : 0; }, get h() { return geo ? geo.h : 0; } };
    cv.cv.addEventListener('pointerdown', (e) => {
      if (!geo || e.pointerType === 'touch') return;
      const p = ptPos(st, e);
      let best = null, bd = 18;
      handles().forEach((hd) => { const d = Math.hypot(geo.X(hd.pt[0]) - p.x, geo.Y(hd.pt[1]) - p.y); if (d < bd) { bd = d; best = hd; } });
      if (!best) return;
      drag = best;
      try { cv.cv.setPointerCapture(e.pointerId); } catch (_) { /* ignore */ }
      e.preventDefault();
    });
    cv.cv.addEventListener('pointermove', (e) => {
      if (!drag || !geo) return;
      const p = ptPos(st, e);
      const x = geo.view.x0 + (p.x - geo.pad.l) / geo.pw * (geo.view.x1 - geo.view.x0);
      const y = geo.view.y1 - (p.y - geo.pad.t) / geo.ph * (geo.view.y1 - geo.view.y0);
      drag.pt[0] = snap(x); drag.pt[1] = snap(y);
      drag.s[0].set(drag.pt[0]); drag.s[1].set(drag.pt[1]);
      update();
    });
    const endDrag = () => { drag = null; };
    cv.cv.addEventListener('pointerup', endDrag);
    cv.cv.addEventListener('pointercancel', endDrag);
    update();
  });

  /* ================= normal distribution helpers ================= */
  const SQ2PI = Math.sqrt(2 * Math.PI);
  const npdf = (z) => Math.exp(-0.5 * z * z) / SQ2PI;
  /** Φ(z) by the power series φ(z)(z + z³/3 + z⁵/15 + …): accurate to about 1e-15 for |z| < 8 */
  function ncdf(z) {
    if (!isFinite(z)) return z > 0 ? 1 : 0;
    if (z > 8.5) return 1;
    if (z < -8.5) return 0;
    const a = Math.abs(z);
    let term = a, sum = a;
    for (let n = 1; n < 500; n++) { term *= a * a / (2 * n + 1); sum += term; if (term < 1e-17 * sum) break; }
    const half = npdf(a) * sum;
    return z >= 0 ? 0.5 + half : 0.5 - half;
  }
  /** inverse of Φ by bisection */
  function ninv(p) {
    if (!(p > 0 && p < 1)) return NaN;
    let lo = -9, hi = 9;
    for (let i = 0; i < 100; i++) { const m = (lo + hi) / 2; if (ncdf(m) < p) lo = m; else hi = m; }
    return (lo + hi) / 2;
  }
  const minus = (s) => String(s).replace(/-/g, '−');

  /* ================= normal — shaded areas, z-values and the inverse ================= */
  W.register('normal', function (el, o) {
    const warn = [];
    let mu = num(o.mu, 0), sg = num(o.sigma, 1);
    if (!(sg > 0)) { warn.push('data-sigma must be positive, so 1 is used.'); sg = 1; }
    sg = clamp(sg, 1e-3, 1e6);
    const raw = String(o.mode || 'between').trim().toLowerCase();
    let mode = ['between', 'below', 'above', 'inverse'].includes(raw) ? raw : 'between';
    if (o.mode && mode !== raw) warn.push('data-mode should be between, below, above or inverse, so "between" is used.');
    let a = num(o.a, mu - sg), b = num(o.b, mu + sg);
    let pIn = clamp(num(o.p, 0.9), 0.0001, 0.9999);
    let tail = String(o.tail || 'below').toLowerCase() === 'above' ? 'above' : 'below';
    let dpS = 1;
    const stepFor = () => Math.pow(10, Math.floor(Math.log10(sg / 20)));
    const dpFor = () => Math.max(0, -Math.floor(Math.log10(stepFor())));

    const { body } = W.frame(el, 'Normal distribution', 'Shade an area, read the probability and the z-values');
    const cv = W.canvas(body, { height: 260, draw: safeDraw(draw) });
    cv.wrap.setAttribute('role', 'img');
    const errEl = W.h('div', { class: 'w-err', role: 'status' });
    show(errEl, false);

    const muF = W.field({ label: 'Mean μ', value: String(mu), type: 'number', step: 'any', width: '7rem', oninput: (v) => { const x = parseFloat(v); if (isFinite(x)) { mu = x; msg = ''; rescale(); update(); } else setMsg('Type a number for the mean.'); } });
    const sgF = W.field({ label: 'Standard deviation σ', value: String(sg), type: 'number', step: 'any', width: '7rem', oninput: (v) => { const x = parseFloat(v); if (isFinite(x) && x > 0) { sg = clamp(x, 1e-3, 1e6); msg = ''; rescale(); update(); } else setMsg('σ must be a positive number.'); } });
    muF.input.setAttribute('aria-label', 'Mean mu'); sgF.input.setAttribute('aria-label', 'Standard deviation sigma');
    const modeTabs = tabs([['between', 'Between a and b'], ['below', 'Below a'], ['above', 'Above a'], ['inverse', 'Find x from p']], mode, (v) => { mode = v; update(); }, 'What to find');
    const sa = W.slider({ label: 'a', min: mu - 4 * sg, max: mu + 4 * sg, step: stepFor(), value: a, fmt: (v) => W.fix(v, dpS), oninput: (v) => { a = v; update(); } });
    const sb = W.slider({ label: 'b', min: mu - 4 * sg, max: mu + 4 * sg, step: stepFor(), value: b, fmt: (v) => W.fix(v, dpS), oninput: (v) => { b = v; update(); } });
    sa.input.setAttribute('aria-label', 'Lower bound a'); sb.input.setAttribute('aria-label', 'Upper bound b');
    const pF = W.field({ label: 'Probability p', value: String(pIn), type: 'number', step: 'any', width: '7rem', oninput: (v) => { const x = parseFloat(v); if (isFinite(x) && x > 0 && x < 1) { pIn = x; msg = ''; update(); } else setMsg('p must be between 0 and 1.'); } });
    pF.input.setAttribute('aria-label', 'Probability p');
    const tailTabs = tabs([['below', 'P(X < x) = p'], ['above', 'P(X > x) = p']], tail, (v) => { tail = v; update(); }, 'Which tail');
    const rowMS = W.h('div', { class: 'w-row', style: { alignItems: 'end' } }, muF.el, sgF.el);
    const rowAB = W.h('div', { class: 'w-row' }, sa.el, sb.el);
    const rowP = W.h('div', { class: 'w-row', style: { alignItems: 'end' } }, pF.el, tailTabs.el);
    body.append(W.h('div', { class: 'w-row' }, modeTabs.el), rowMS, rowAB, rowP, errEl);
    const tP = W.stat('Probability', true), tX = W.stat('Value of x', true), tZ = W.stat('z-values'), tS = W.stat('Statement');
    body.append(W.h('div', { class: 'w-out' }, tP.el, tX.el, tZ.el, tS.el));
    body.append(W.h('div', { class: 'w-note' }, 'Standardise with z = (x − μ)/σ, then Φ(z) is the area to the left. Try μ = 50, σ = 8 and compare with your table. In the last mode, give the probability and read off x.'));
    if (warn.length) body.append(W.h('div', { class: 'w-err' }, warn.join(' ')));

    let msg = '';
    function setMsg(t) { msg = t; show(errEl, !!t); errEl.textContent = t; }
    function rescale() {
      const st = stepFor(); dpS = dpFor();
      [sa, sb].forEach((s) => { s.input.min = mu - 4 * sg; s.input.max = mu + 4 * sg; s.input.step = st; });
      a = clamp(a, mu - 4 * sg, mu + 4 * sg); b = clamp(b, mu - 4 * sg, mu + 4 * sg);
      sa.set(a); sb.set(b);
    }
    const fx = (v) => minus(W.fmt(v, 4));
    const zf = (x) => (x - mu) / sg;
    let region = [0, 0], line = [];
    function update() {
      show(errEl, !!msg);
      show(rowAB, mode !== 'inverse'); show(sb.el, mode === 'between');
      show(rowP, mode === 'inverse');
      show(tP.el, mode !== 'inverse'); show(tX.el, mode === 'inverse');
      let lo = a, hi = b;
      if (mode === 'between' && b < a) { lo = b; hi = a; }
      if (mode === 'between') {
        const pr = ncdf(zf(hi)) - ncdf(zf(lo));
        region = [lo, hi]; line = [lo, hi];
        tP.set(W.fmt(pr, 4)); tZ.set(`${minus(W.fmt(zf(lo), 3))} and ${minus(W.fmt(zf(hi), 3))}`); tS.set(`P(${fx(lo)} < X < ${fx(hi)})`);
      } else if (mode === 'below') {
        region = [-Infinity, a]; line = [a];
        tP.set(W.fmt(ncdf(zf(a)), 4)); tZ.set(minus(W.fmt(zf(a), 3))); tS.set(`P(X < ${fx(a)})`);
      } else if (mode === 'above') {
        region = [a, Infinity]; line = [a];
        tP.set(W.fmt(1 - ncdf(zf(a)), 4)); tZ.set(minus(W.fmt(zf(a), 3))); tS.set(`P(X > ${fx(a)})`);
      } else {
        const z = ninv(tail === 'below' ? pIn : 1 - pIn), x = mu + z * sg;
        region = tail === 'below' ? [-Infinity, x] : [x, Infinity]; line = [x];
        tX.set(fx(x)); tZ.set(minus(W.fmt(z, 4))); tS.set(tail === 'below' ? `P(X < x) = ${W.fmt(pIn, 4)}` : `P(X > x) = ${W.fmt(pIn, 4)}`);
      }
      cv.wrap.setAttribute('aria-label', `Normal curve with mean ${W.fmt(mu, 4)} and standard deviation ${W.fmt(sg, 4)}. ${tS.el.textContent}. Result ${mode === 'inverse' ? tX.el.textContent : tP.el.textContent}.`);
      cv.redraw();
    }

    function draw(ctx, w, h, c) {
      const pad = { l: 14, r: 14, t: 12, b: 30 };
      const x0 = mu - 4 * sg, x1 = mu + 4 * sg, ymax = npdf(0) / sg * 1.12;
      const view = { x0, x1, y0: 0, y1: ymax };
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 'x', ylabel: '', fy: () => '' });
      const X = A.X, Y = A.Y;
      const f = (x) => npdf((x - mu) / sg) / sg;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      const lo = Math.max(region[0], x0), hi = Math.min(region[1], x1);
      if (hi > lo) {
        ctx.beginPath(); ctx.moveTo(X(lo), Y(0));
        const N = 120;
        for (let i = 0; i <= N; i++) { const x = lo + (hi - lo) * i / N; ctx.lineTo(X(x), Y(f(x))); }
        ctx.lineTo(X(hi), Y(0)); ctx.closePath();
        ctx.globalAlpha = 0.28; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1;
      }
      ctx.beginPath();
      const N = Math.max(80, Math.round(w));
      for (let i = 0; i <= N; i++) { const x = x0 + (x1 - x0) * i / N; if (i) ctx.lineTo(X(x), Y(f(x))); else ctx.moveTo(X(x), Y(f(x))); }
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2.4; ctx.lineJoin = 'round'; ctx.stroke();
      // mean marker
      ctx.setLineDash([4, 4]); ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(X(mu), Y(0)); ctx.lineTo(X(mu), Y(f(mu))); ctx.stroke(); ctx.setLineDash([]);
      ctx.font = `12px ${c.font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      haloText(ctx, c, 'μ', X(mu), Y(f(mu)) - 3, c.ink2);
      // bounds
      ctx.strokeStyle = c.red; ctx.lineWidth = 1.8;
      const names = mode === 'between' ? ['a', 'b'] : mode === 'inverse' ? ['x'] : ['a'];
      const ls = mode === 'between' ? [Math.min(a, b), Math.max(a, b)] : line;
      ls.forEach((v, i) => {
        if (v < x0 || v > x1) return;
        ctx.beginPath(); ctx.moveTo(X(v), Y(0)); ctx.lineTo(X(v), Y(f(v))); ctx.stroke();
        haloText(ctx, c, names[i] || '', X(v), Y(f(v)) - 3, c.red);
      });
      ctx.restore();
    }
    rescale();
    update();
  });

  /* ================= discrete — binomial, geometric and Poisson bar charts ================= */
  W.register('discrete', function (el, o) {
    const warn = [];
    const raw = String(o.dist || 'binomial').trim().toLowerCase();
    let dist = ['binomial', 'geometric', 'poisson'].includes(raw) ? raw : 'binomial';
    if (o.dist && dist !== raw) warn.push('data-dist should be binomial, geometric or poisson, so binomial is used.');
    let n = clamp(Math.round(num(o.n, 10)), 1, 50);
    let p = clamp(num(o.p, dist === 'geometric' ? 0.25 : 0.3), 0.01, 0.99);
    let lam = clamp(num(o.lambda, 3), 0.1, 30);
    let rg = String(o.range || '').replace(/[−–]/g, '-').split(',').map((t) => parseInt(t, 10));
    if (o.range && !(rg.length >= 2 && isFinite(rg[0]) && isFinite(rg[1]))) warn.push('data-range should look like "0,2", so a default range is used.');
    let ra = isFinite(rg[0]) ? rg[0] : (dist === 'geometric' ? 1 : 0), rb = isFinite(rg[1]) ? rg[1] : ra + 2;
    let overlay = isOn(o.overlay);

    function kmaxOf() {
      if (dist === 'binomial') return n;
      if (dist === 'poisson') return Math.min(80, Math.ceil(lam + 6 * Math.sqrt(lam) + 8));
      return Math.round(clamp(Math.ceil(Math.log(0.002) / Math.log(1 - p)), 10, 40));
    }
    const kmin = () => (dist === 'geometric' ? 1 : 0);
    function pmf() {
      const kmax = kmaxOf(), out = [];
      if (dist === 'binomial') {
        const q = 1 - p; let v = Math.pow(q, n);
        for (let k = 0; k <= n; k++) { out.push([k, v]); v = v * (n - k) / (k + 1) * p / q; }
      } else if (dist === 'poisson') {
        let v = Math.exp(-lam);
        for (let k = 0; k <= kmax; k++) { out.push([k, v]); v = v * lam / (k + 1); }
      } else {
        for (let r = 1; r <= kmax; r++) out.push([r, Math.pow(1 - p, r - 1) * p]);
      }
      return out;
    }
    const meanOf = () => (dist === 'binomial' ? n * p : dist === 'poisson' ? lam : 1 / p);
    const varOf = () => (dist === 'binomial' ? n * p * (1 - p) : dist === 'poisson' ? lam : (1 - p) / (p * p));

    const { body } = W.frame(el, 'Discrete distributions', 'Binomial, geometric and Poisson: change the parameters and the range');
    const cv = W.canvas(body, { height: 270, draw: safeDraw(draw) });
    cv.wrap.setAttribute('role', 'img');
    const distTabs = tabs([['binomial', 'Binomial'], ['geometric', 'Geometric'], ['poisson', 'Poisson']], dist, (v) => {
      dist = v;
      if (v === 'geometric') { p = clamp(p, 0.01, 0.99); if (ra < 1) ra = 1; if (rb < ra) rb = ra; }
      fixRange(); update();
    }, 'Distribution');
    const sN = W.slider({ label: 'n (trials)', min: 1, max: 50, step: 1, value: n, fmt: (v) => String(v), oninput: (v) => { n = Math.round(v); fixRange(); update(); } });
    const sP = W.slider({ label: 'p (probability of success)', min: 0.01, max: 0.99, step: 0.01, value: p, fmt: (v) => W.fix(v, 2), oninput: (v) => { p = v; fixRange(); update(); } });
    const sL = W.slider({ label: 'λ (mean rate)', min: 0.1, max: 30, step: 0.1, value: lam, fmt: (v) => W.fix(v, 1), oninput: (v) => { lam = v; fixRange(); update(); } });
    const sA = W.slider({ label: 'a (from)', min: 0, max: 50, step: 1, value: ra, fmt: (v) => String(v), oninput: (v) => { ra = Math.round(v); update(); } });
    const sB = W.slider({ label: 'b (to)', min: 0, max: 50, step: 1, value: rb, fmt: (v) => String(v), oninput: (v) => { rb = Math.round(v); update(); } });
    [[sN, 'Number of trials n'], [sP, 'Probability of success p'], [sL, 'Mean rate lambda'], [sA, 'Range from a'], [sB, 'Range to b']].forEach(([s, t]) => s.input.setAttribute('aria-label', t));
    const ovTabs = tabs([['off', 'No overlay'], ['on', 'Normal overlay']], overlay ? 'on' : 'off', (v) => { overlay = v === 'on'; update(); }, 'Normal curve overlay');
    const rowOv = W.h('div', { class: 'w-row' }, W.h('span', { class: 'w-lab' }, 'Compare'), ovTabs.el);
    body.append(W.h('div', { class: 'w-row' }, distTabs.el), W.h('div', { class: 'w-row' }, sN.el, sP.el, sL.el), W.h('div', { class: 'w-row' }, sA.el, sB.el), rowOv);
    const tR = W.stat('P(a ≤ X ≤ b)', true), tM = W.stat('Mean'), tV = W.stat('Variance'), tG = W.stat('P(X > b)'), tO = W.stat('Normal approximation');
    body.append(W.h('div', { class: 'w-out' }, tR.el, tM.el, tV.el, tG.el, tO.el));
    body.append(W.h('div', { class: 'w-note' }, 'The shaded bars are the values a to b. For the binomial and Poisson, switch on the normal overlay: the approximation uses a continuity correction (a − 0.5 to b + 0.5), and works well when the bell shape fits the bars.'));
    if (warn.length) body.append(W.h('div', { class: 'w-err' }, warn.join(' ')));

    function fixRange() {
      const kmax = kmaxOf(), lo = kmin();
      [sA, sB].forEach((s) => { s.input.min = lo; s.input.max = kmax; });
      ra = clamp(ra, lo, kmax); rb = clamp(rb, lo, kmax);
      if (rb < ra) rb = ra;
      sA.set(ra); sB.set(rb);
    }
    function probRange(lo, hi) {
      if (dist === 'geometric') { const q = 1 - p; return Math.pow(q, lo - 1) - Math.pow(q, hi); }
      let s = 0;
      for (const [k, v] of pmf()) if (k >= lo && k <= hi) s += v;
      return s;
    }
    function update() {
      show(sN.el, dist === 'binomial');
      show(sP.el, dist !== 'poisson');
      show(sL.el, dist === 'poisson');
      show(rowOv, dist !== 'geometric');
      show(tO.el, dist !== 'geometric' && overlay);
      let lo = ra, hi = rb;
      if (hi < lo) { const t = lo; lo = hi; hi = t; }
      tR.set(W.fmt(probRange(lo, hi), 4));
      tM.set(W.fmt(meanOf(), 4));
      show(tV.el, dist !== 'geometric'); show(tG.el, dist === 'geometric');
      if (dist === 'geometric') tG.set(W.fmt(Math.pow(1 - p, hi), 4));
      else tV.set(W.fmt(varOf(), 4));
      if (dist !== 'geometric') {
        const mu = meanOf(), sd = Math.sqrt(varOf());
        tO.set(W.fmt(ncdf((hi + 0.5 - mu) / sd) - ncdf((lo - 0.5 - mu) / sd), 4));
      }
      const label = dist === 'binomial' ? `B(${n}, ${W.fmt(p, 2)})` : dist === 'poisson' ? `Po(${W.fmt(lam, 3)})` : `Geo(${W.fmt(p, 2)})`;
      cv.wrap.setAttribute('aria-label', `Bar chart of ${label}. P(${lo} ≤ X ≤ ${hi}) = ${tR.el.textContent}.`);
      cv.redraw();
    }

    function draw(ctx, w, h, c) {
      const pad = { l: 44, r: 12, t: 12, b: 30 };
      const data = pmf(), kmax = kmaxOf(), lo0 = kmin();
      let lo = ra, hi = rb; if (hi < lo) { const t = lo; lo = hi; hi = t; }
      let ymax = Math.max(...data.map((d) => d[1]));
      const mu = meanOf(), sd = Math.sqrt(varOf());
      if (overlay && dist !== 'geometric') ymax = Math.max(ymax, npdf(0) / sd);
      ymax = Math.min(1, ymax * 1.15);
      const view = { x0: lo0 - 0.7, x1: kmax + 0.7, y0: 0, y1: ymax };
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 'x', ylabel: 'P(X = x)' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      const bw = Math.max(1.5, (X(1) - X(0)) * 0.78);
      for (const [k, v] of data) {
        const inR = k >= lo && k <= hi;
        ctx.fillStyle = inR ? c.sc : c.ink3; ctx.globalAlpha = inR ? 0.9 : 0.4;
        ctx.fillRect(X(k) - bw / 2, Y(v), bw, Y(0) - Y(v));
      }
      ctx.globalAlpha = 1;
      if (overlay && dist !== 'geometric') {
        ctx.beginPath();
        const N = 160;
        for (let i = 0; i <= N; i++) { const x = view.x0 + (view.x1 - view.x0) * i / N, y = npdf((x - mu) / sd) / sd; if (i) ctx.lineTo(X(x), Y(y)); else ctx.moveTo(X(x), Y(y)); }
        ctx.strokeStyle = c.red; ctx.lineWidth = 2; ctx.stroke();
      }
      ctx.restore();
    }
    fixRange();
    update();
  });

  /* ---------- resultant: add up to four forces and see the resultant ---------- */
  W.register('resultant', function (el, o) {
    const MAXF = 4;
    const warn = [];
    const rows = [];
    String(o.forces || '').split(';').forEach((part) => {
      const m = part.trim().match(/^(-?[\d.]+)\s*@\s*(-?[\d.]+)$/);
      if (m && rows.length < MAXF) rows.push([m[1], m[2]]);
    });
    if (!rows.length) {
      if (o.forces) warn.push('data-forces should look like "12@0; 10@120", so an example is used.');
      rows.push(['12', '0'], ['10', '120']);
    }
    while (rows.length < MAXF) rows.push(['', '']);
    let balance = isOn(o.balance);
    const rad = Math.PI / 180;
    const clean = (v) => (Math.abs(v) < 1e-9 ? 0 : v);
    const norm = (a) => { let d = a % 360; if (d > 180) d -= 360; if (d <= -180) d += 360; return clean(d); };
    let model = { list: [], X: 0, Y: 0, R: 0, dir: 0 };

    const { body } = W.frame(el, 'Resultant of forces', 'Give up to four forces as a size and an angle from the positive x-axis');
    const cv = W.canvas(body, { height: 280, draw: safeDraw(draw) });
    cv.wrap.setAttribute('role', 'img');
    const errEl = W.h('div', { class: 'w-err', role: 'status' });
    show(errEl, false);
    const fields = rows.map((r, i) => {
      const f = W.field({ label: `F${i + 1} (N)`, value: r[0], type: 'number', step: 'any', width: '6rem', placeholder: '–', oninput: () => update() });
      const a = W.field({ label: `Angle ${i + 1} (°)`, value: r[1], type: 'number', step: 'any', width: '6rem', placeholder: '–', oninput: () => update() });
      f.input.setAttribute('aria-label', `Force ${i + 1} in newtons`);
      a.input.setAttribute('aria-label', `Angle of force ${i + 1} in degrees from the positive x-axis`);
      return { f, a };
    });
    const chk = W.h('input', { type: 'checkbox', 'aria-label': 'Add the balancing force', onchange: (e) => { balance = e.target.checked; update(); } });
    chk.checked = balance;
    const chkRow = W.h('label', { class: 'w-ctl', style: { flexDirection: 'row', alignItems: 'center', gap: '0.5rem' } }, chk, 'Add the balancing force');
    body.append(W.h('div', { class: 'w-row' }, ...fields.slice(0, 2).flatMap((x) => [x.f.el, x.a.el])), W.h('div', { class: 'w-row' }, ...fields.slice(2).flatMap((x) => [x.f.el, x.a.el])), W.h('div', { class: 'w-row' }, chkRow));
    const tX = W.stat('ΣX (N)'), tY = W.stat('ΣY (N)'), tR = W.stat('Resultant (N)', true), tD = W.stat('Direction'), tB = W.stat('Balancing force');
    body.append(W.h('div', { class: 'w-out' }, tX.el, tY.el, tR.el, tD.el, tB.el), errEl);
    body.append(W.h('div', { class: 'w-note' }, 'Change a size or an angle and watch ΣX and ΣY. Tick the box to draw the force that would hold the object in equilibrium. Leave a row empty to remove that force.'));
    if (warn.length) body.append(W.h('div', { class: 'w-err' }, warn.join(' ')));

    function update() {
      const list = [], bad = [];
      fields.forEach((r, i) => {
        const fs = r.f.input.value.trim(), as = r.a.input.value.trim();
        if (fs === '' && as === '') return;
        const f = parseFloat(fs), a = parseFloat(as);
        if (!isFinite(f) || !isFinite(a)) { bad.push(i + 1); return; }
        if (f < 0) { bad.push(i + 1); return; }
        list.push({ f: clamp(f, 0, 1e6), a, n: i + 1 });
      });
      if (bad.length) { errEl.textContent = `Force ${bad.join(', ')}: enter a size of 0 or more and an angle, or leave the row empty.`; show(errEl, true); } else show(errEl, false);
      let X = 0, Y = 0;
      list.forEach((q) => { X += q.f * Math.cos(q.a * rad); Y += q.f * Math.sin(q.a * rad); });
      X = clean(X); Y = clean(Y);
      const R = Math.hypot(X, Y), scale = Math.max(1, ...list.map((q) => q.f));
      const zero = R < 1e-9 * scale;
      const dir = zero ? 0 : norm(Math.atan2(Y, X) / rad);
      model = { list, X, Y, R: zero ? 0 : R, dir, zero };
      tX.set(minus(W.fmt(X, 3))); tY.set(minus(W.fmt(Y, 3)));
      tR.set(zero ? '0' : W.fmt(R, 3));
      tD.set(zero ? 'none' : minus(W.fix(dir, 1)) + '°');
      tB.set(!balance ? 'hidden' : zero ? 'none needed' : `${W.fmt(R, 3)} N at ${minus(W.fix(norm(dir + 180), 1))}°`);
      cv.wrap.setAttribute('aria-label', list.length ? `Force diagram. Sum of x-components ${W.fmt(X, 3)} newtons, sum of y-components ${W.fmt(Y, 3)} newtons, resultant ${zero ? 'zero' : W.fmt(R, 3) + ' newtons'}.` : 'No forces entered.');
      cv.redraw();
    }

    function arrow(ctx, x0, y0, x1, y1, color, lw, dash) {
      const dx = x1 - x0, dy = y1 - y0, len = Math.hypot(dx, dy);
      if (len < 1) return;
      ctx.save();
      ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = lw; ctx.setLineDash(dash || []);
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
      ctx.setLineDash([]);
      const ux = dx / len, uy = dy / len, hl = Math.min(10, len * 0.5);
      ctx.beginPath(); ctx.moveTo(x1, y1);
      ctx.lineTo(x1 - hl * ux + hl * 0.45 * uy, y1 - hl * uy - hl * 0.45 * ux);
      ctx.lineTo(x1 - hl * ux - hl * 0.45 * uy, y1 - hl * uy + hl * 0.45 * ux);
      ctx.closePath(); ctx.fill();
      ctx.restore();
    }
    function draw(ctx, w, h, c) {
      const pad = { l: 38, r: 14, t: 14, b: 28 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      let ext = 1;
      model.list.forEach((q) => { ext = Math.max(ext, q.f); });
      ext = Math.max(ext, model.R) * 1.25;
      const unit = Math.min(pw, ph) / (2 * ext);
      const view = { x0: -pw / 2 / unit, x1: pw / 2 / unit, y0: -ph / 2 / unit, y1: ph / 2 / unit };
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 'x (N)', ylabel: 'y (N)' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
      ctx.font = `600 12px ${c.font || 'sans-serif'}`;
      model.list.forEach((q) => {
        const fx = q.f * Math.cos(q.a * rad), fy = q.f * Math.sin(q.a * rad);
        arrow(ctx, X(0), Y(0), X(fx), Y(fy), c.sc, 2.4);
        haloText(ctx, c, `F${q.n}`, X(fx) + 6, Y(fy) - 6, c.sc);
      });
      if (balance && !model.zero && model.R > 0) {
        const bx = -model.X, by = -model.Y;
        arrow(ctx, X(0), Y(0), X(bx), Y(by), c.ok, 2.4, [6, 4]);
        haloText(ctx, c, 'balancing', X(bx) + 6, Y(by) + 14, c.ok);
      }
      if (!model.zero && model.R > 0) {
        arrow(ctx, X(0), Y(0), X(model.X), Y(model.Y), c.red, 3.2);
        haloText(ctx, c, 'resultant', X(model.X) + 6, Y(model.Y) + 14, c.red);
      }
      ctx.beginPath(); ctx.arc(X(0), Y(0), 3.5, 0, 6.2832); ctx.fillStyle = c.ink; ctx.fill();
      if (model.zero && model.list.length) haloText(ctx, c, 'resultant is zero: equilibrium', pad.l + 8, pad.t + 18, c.ok);
      ctx.restore();
    }
    update();
  });

  /* ---------- projectile: launch a particle and read the numbers ---------- */
  W.register('projectile', function (el, o) {
    const warn = [];
    let v = clamp(num(o.speed, 20), 1, 60), ang = clamp(num(o.angle, 45), 0, 90), h0 = clamp(num(o.height, 0), 0, 20);
    let g = [10, 9.8, 9.81].includes(num(o.g, 10)) ? num(o.g, 10) : 10;
    if (o.g && g !== num(o.g, 10)) warn.push('data-g should be 10, 9.8 or 9.81, so 10 is used.');
    const rad = Math.PI / 180;
    const reduce = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    let t = 0, anim = null, hist = [];
    const calc = (vv, aa, hh, gg) => {
      const vx = vv * Math.cos(aa * rad), vy = vv * Math.sin(aa * rad);
      const T = (vy + Math.sqrt(vy * vy + 2 * gg * hh)) / gg;
      return { vx, vy, h: hh, g: gg, T, R: vx * T, H: hh + vy * vy / (2 * gg) };
    };
    let P = calc(v, ang, h0, g);

    const { body } = W.frame(el, 'Projectile motion', 'Choose the launch speed, angle and height, then launch');
    const cv = W.canvas(body, { height: 270, draw: safeDraw(draw) });
    cv.wrap.setAttribute('role', 'img');
    const sV = W.slider({ label: 'Speed (m s⁻¹)', min: 1, max: 60, step: 1, value: v, fmt: (x) => String(x), oninput: (x) => { stop(); v = x; recalc(); } });
    const sA = W.slider({ label: 'Angle (°)', min: 0, max: 90, step: 1, value: ang, fmt: (x) => String(x), oninput: (x) => { stop(); ang = x; recalc(); } });
    const sH = W.slider({ label: 'Launch height (m)', min: 0, max: 20, step: 0.5, value: h0, fmt: (x) => W.fix(x, 1), oninput: (x) => { stop(); h0 = x; recalc(); } });
    const sT = W.slider({ label: 'Time t (s)', min: 0, max: Math.max(0.1, P.T), step: 0.01, value: 0, fmt: (x) => W.fix(x, 2), oninput: (x) => { stop(); t = x; refresh(); } });
    [[sV, 'Launch speed'], [sA, 'Launch angle'], [sH, 'Launch height'], [sT, 'Time']].forEach(([s, a]) => s.input.setAttribute('aria-label', a));
    const gTabs = tabs([['10', 'g = 10'], ['9.8', 'g = 9.8'], ['9.81', 'g = 9.81']], String(g), (x) => { stop(); g = parseFloat(x); recalc(); }, 'Value of g');
    const bGo = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => launch() }, 'Launch');
    const bClr = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { hist = []; cv.redraw(); } }, 'Clear paths');
    body.append(W.h('div', { class: 'w-row' }, sV.el, sA.el, sH.el), W.h('div', { class: 'w-row' }, W.h('span', { class: 'w-lab' }, 'Gravity'), gTabs.el, bGo, bClr), W.h('div', { class: 'w-row' }, sT.el));
    const tR = W.stat('Range (m)', true), tTf = W.stat('Time of flight (s)'), tH = W.stat('Max height (m)'), tVx = W.stat('Horizontal velocity'), tVy = W.stat('Vertical velocity'), tSp = W.stat('Speed');
    body.append(W.h('div', { class: 'w-out' }, tR.el, tTf.el, tH.el, tVx.el, tVy.el, tSp.el));
    body.append(W.h('div', { class: 'w-note' }, 'Press Launch to fire the particle; earlier paths stay as faint curves so you can compare angles. Try 45° and 30°, then add some launch height. The velocity readings are at the chosen time t.'));
    if (warn.length) body.append(W.h('div', { class: 'w-err' }, warn.join(' ')));

    function stop() { if (anim) { cancelAnimationFrame(anim); anim = null; } }
    function recalc() {
      P = calc(v, ang, h0, g);
      sT.input.max = Math.max(0.1, P.T); t = Math.min(t, P.T); sT.set(t);
      refresh();
    }
    function refresh() {
      const vy = P.vy - P.g * t;
      tR.set(W.fmt(P.R, 3)); tTf.set(W.fmt(P.T, 3)); tH.set(W.fmt(P.H, 3));
      tVx.set(W.fmt(P.vx, 3) + ' m s⁻¹'); tVy.set(minus(W.fmt(vy, 3)) + ' m s⁻¹'); tSp.set(W.fmt(Math.hypot(P.vx, vy), 3) + ' m s⁻¹');
      cv.wrap.setAttribute('aria-label', `Trajectory of a projectile launched at ${W.fmt(v, 3)} metres per second at ${W.fmt(ang, 3)} degrees from a height of ${W.fmt(h0, 3)} metres. Range ${W.fmt(P.R, 3)} metres, maximum height ${W.fmt(P.H, 3)} metres.`);
      cv.redraw();
    }
    function launch() {
      stop();
      const last = hist[hist.length - 1];
      if (!last || last.vx !== P.vx || last.vy !== P.vy || last.h !== P.h || last.g !== P.g) { hist.push(Object.assign({}, P)); if (hist.length > 6) hist.shift(); }
      if (reduce) { t = P.T; sT.set(t); refresh(); return; }
      const start = performance.now(), dur = clamp(P.T * 600, 900, 3000);
      const step = (now) => {
        const f = Math.min(1, (now - start) / dur);
        t = P.T * f; sT.set(t); refresh();
        anim = f < 1 ? requestAnimationFrame(step) : null;
      };
      anim = requestAnimationFrame(step);
    }
    const pos = (p, tt) => [p.vx * tt, p.h + p.vy * tt - 0.5 * p.g * tt * tt];
    function draw(ctx, w, h, c) {
      const pad = { l: 44, r: 14, t: 12, b: 30 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      let xm = P.R, ym = P.H;
      hist.forEach((p) => { xm = Math.max(xm, p.R); ym = Math.max(ym, p.H); });
      xm = Math.max(xm, 1) * 1.06; ym = Math.max(ym, 1) * 1.15;
      const unit = Math.min(pw / xm, ph / ym);
      const view = { x0: 0, x1: pw / unit, y0: 0, y1: ph / unit };
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 'x (m)', ylabel: 'y (m)' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
      const path = (p, color, lw, alpha) => {
        ctx.beginPath();
        for (let i = 0; i <= 80; i++) { const [x, y] = pos(p, p.T * i / 80); if (i) ctx.lineTo(X(x), Y(Math.max(0, y))); else ctx.moveTo(X(x), Y(y)); }
        ctx.globalAlpha = alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.stroke(); ctx.globalAlpha = 1;
      };
      hist.forEach((p) => path(p, c.ink3, 1.6, 0.55));
      path(P, c.sc, 2.6, 1);
      const [bx, by] = pos(P, Math.min(t, P.T));
      ctx.beginPath(); ctx.arc(X(bx), Y(Math.max(0, by)), 5.5, 0, 6.2832); ctx.fillStyle = c.red; ctx.fill();
      ctx.restore();
    }
    recalc();
  });

})();
