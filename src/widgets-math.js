/* widgets-math.js — maths widgets for Zero to A*.
   graph · unitcircle · stats · normal · binomial · projectile
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
})();
