/* fm-polar: a polar curve r = f(θ) traced on a polar grid, with the sector area ½∫r² dθ.
   data-r "1+cos(t)"      r as a function of t (= θ); same expression syntax as the graph widget; r < 0 gives no point
   data-range "0,2*pi"    θ from, to (expressions allowed, pi is known)
   data-area "0,pi"       optional: shade the sector from the first value to the slider's θ; the slider starts at the second
   data-presets "cardioid,circle,rose,spiral"   buttons to show (also limacon, lemniscate)
   Try: <div class="widget" data-w="fm-polar" data-r="1+cos(t)" data-range="0,2*pi"></div> */
(function () {
  'use strict';
  const PI = Math.PI, TAU = Math.PI * 2;
  const W = typeof window !== 'undefined' ? window.W : undefined;

  /* ---- pure helpers (tested in Node) ---- */
  function simpsonHalfRSquared(r, A, B, n) {
    // ½ ∫ r² dθ over [A, B]; places where r is not finite or r < 0 contribute 0 (the r ≥ 0 convention)
    if (!(B > A)) return 0;
    n = Math.max(2, 2 * Math.round((n || 400) / 2));
    const g = (t) => { const v = r(t); return isFinite(v) && v >= 0 ? v * v : 0; };
    const h = (B - A) / n;
    let s = g(A) + g(B);
    for (let i = 1; i < n; i++) s += g(A + i * h) * (i % 2 ? 4 : 2);
    return 0.5 * s * h / 3;
  }
  function niceStep(R) {
    const raw = R / 4, p = Math.pow(10, Math.floor(Math.log10(raw))), m = raw / p;
    return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p;
  }
  function asPiMultiple(v) {
    // "= (k/m)π" when v/π is a simple fraction, else ''
    const q = v / PI;
    for (let m = 1; m <= 16; m++) {
      const k = Math.round(q * m);
      if (k !== 0 && Math.abs(q - k / m) < 1e-5) {
        const num = Math.abs(k);
        const coeff = m === 1 ? (num === 1 ? '' : String(num)) : `${num}/${m}`;
        return (k < 0 ? '−' : '') + coeff + 'π';
      }
    }
    return '';
  }
  const core = { simpsonHalfRSquared, niceStep, asPiMultiple };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  const PRESETS = {
    cardioid: { label: 'Cardioid', r: '1+cos(t)', range: [0, TAU] },
    circle: { label: 'Circle', r: '2*cos(t)', range: [-PI / 2, PI / 2] },
    rose: { label: 'Rose', r: 'cos(2*t)', range: [0, TAU] },
    spiral: { label: 'Spiral', r: 't/4', range: [0, 4 * PI] },
    limacon: { label: 'Limaçon', r: '1+2*cos(t)', range: [0, TAU] },
    lemniscate: { label: 'Lemniscate', r: 'sqrt(cos(2*t))', range: [0, TAU] },
  };
  const DEFAULT = 'cardioid';

  const norm = (s) => String(s == null ? '' : s).replace(/[−–]/g, '-').replace(/π/g, 'pi').replace(/θ/g, 't')
    .replace(/\bpi\b/g, '(' + PI + ')');
  function compile(src) {
    const r = W.parse(norm(src), {});
    return (t) => { const v = r.f({ t }); return typeof v === 'number' ? v : NaN; };
  }
  function evalNumber(src) {
    const v = W.parse(norm(src), {}).f({});
    if (typeof v !== 'number' || !isFinite(v)) throw new Error('not a number');
    return v;
  }
  function parseRange(s) {
    const parts = String(s).split(',');
    if (parts.length !== 2) throw new Error('needs two values like 0,2*pi');
    const a = evalNumber(parts[0]), b = evalNumber(parts[1]);
    if (!(b > a)) throw new Error('the second value must be larger than the first');
    return [a, b];
  }
  const fx = (v, d) => {
    if (isFinite(v) && Math.abs(v) >= 1e6) return v.toExponential(2);
    if (isFinite(v) && Math.abs(v) < 0.5 * Math.pow(10, -d)) v = 0;   // no "−0.000"
    return W.fix(v, d);
  };
  const fmtPi = (t) => { const v = (t / PI).toFixed(2); return (v === '-0.00' ? '0.00' : v).replace('-', '−') + 'π'; };

  W.register('fm-polar', function (el, o) {
    const warns = [];
    const wanted = String(o.presets || 'cardioid,circle,rose,spiral').split(',').map((s) => s.trim().toLowerCase()).filter((k) => PRESETS[k]);
    const presetKeys = wanted.length ? wanted : ['cardioid', 'circle', 'rose', 'spiral'];

    let src, fn, range, areaStart = null, areaOn = false, theta;
    let activePreset = null;

    // initial curve
    src = String(o.r || '').trim();
    if (src) {
      try { fn = compile(src); const t0 = fn(0.5); if (typeof t0 !== 'number') throw new Error('not a number'); }
      catch (e) { warns.push(`Can't read r = ${src}: ${(e && e.message) || 'check the expression'}. Showing a cardioid instead.`); src = ''; }
    }
    if (!src) { src = PRESETS[DEFAULT].r; fn = compile(src); }
    let match = null;
    for (const k of Object.keys(PRESETS)) if (PRESETS[k].r === src.replace(/\s+/g, '')) match = k;
    range = match ? PRESETS[match].range.slice() : [0, TAU];
    activePreset = match && presetKeys.indexOf(match) >= 0 ? match : null;
    if (o.range != null && String(o.range).trim() !== '') {
      try { range = parseRange(o.range); } catch (e) { warns.push(`data-range should look like "0,2*pi" (${e.message}). Using 0 to 2π.`); range = [0, TAU]; }
    }
    if (o.area != null && String(o.area).trim() !== '') {
      try {
        const ar = parseRange(o.area);
        areaStart = Math.max(range[0], ar[0]); areaOn = true;
        theta = Math.min(range[1], ar[1]);
      } catch (e) { warns.push(`data-area should look like "0,pi" (${e.message}). Ignored.`); }
    }
    if (theta == null) theta = range[1];

    const { body } = W.frame(el, 'Polar curve', 'r as a function of the angle θ');

    /* ---- view ---- */
    const view = { R: 1, step: 0.5 };
    function sampleCount() { return Math.max(200, Math.min(2400, Math.round(720 * (range[1] - range[0]) / TAU))); }
    function fitView() {
      let R = 0;
      const n = sampleCount();
      for (let i = 0; i <= n; i++) { const v = fn(range[0] + (range[1] - range[0]) * i / n); if (isFinite(v) && v > R) R = v; }
      if (!(R > 1e-9) || !isFinite(R)) R = 1;
      view.step = niceStep(R);
      view.R = Math.ceil(R * 1.04 / view.step) * view.step;
    }

    /* ---- controls ---- */
    const row = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } });
    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose a curve' });
    const tabBtns = {};
    for (const k of presetKeys) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false' }, PRESETS[k].label);
      b.addEventListener('click', () => usePreset(k));
      tabBtns[k] = b; tabs.append(b);
    }
    row.append(tabs);
    body.append(row);

    const exprField = W.field({ label: 'r = (use t for θ)', value: src, type: 'text', width: '16em' });
    exprField.input.setAttribute('autocomplete', 'off');
    exprField.input.setAttribute('spellcheck', 'false');
    body.append(W.h('div', { class: 'w-row' }, exprField.el));

    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    const showWarns = () => { errBox.textContent = warns.join(' '); errBox.style.display = warns.length ? '' : 'none'; };
    body.append(errBox);

    // step = span / N, so the last step lands exactly on the end of the range (2π, not 6.28)
    const stepFor = () => { const sp = range[1] - range[0]; return sp / Math.max(1, Math.round(sp / 0.01)); };
    const sl = W.slider({ label: 'Angle θ', min: range[0], max: range[1], step: stepFor(), value: theta,
      fmt: (v) => fmtPi(+v), oninput: (v) => { v = +v; if (v >= range[1] - stepFor() * 0.51) v = range[1]; theta = clampT(v); update(); } });
    body.append(sl.el);

    const play = W.h('button', { type: 'button', class: 'btn btn-sm', 'aria-label': 'Play the animation' }, 'Play');
    const toStart = W.h('button', { type: 'button', class: 'btn btn-sm btn-sec', 'aria-label': 'Reset θ to the start of the range' }, 'Reset');
    const areaBox = W.h('input', { type: 'checkbox' });
    areaBox.checked = areaOn;
    const areaLab = W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, areaBox, W.h('span', { class: 'w-lab' }, 'Shade the area ½∫r² dθ'));
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'center' } }, play, toStart, areaLab));

    const cv = W.canvas(body, { height: 330, draw, label: 'Polar curve r = f(θ)', describe });
    const R = W.readout([['th', 'θ'], ['r', 'r'], ['xy', '(x, y)'], ['area', 'Shaded area']]);
    body.append(R.el);
    const status = W.h('div', { class: 'w-note', 'aria-live': 'polite' }, '');
    body.append(status);
    body.append(W.h('div', { class: 'w-note' }, 'Drag the θ slider or press Play: the curve is drawn as θ grows. Tick "Shade the area" to see the sector swept from the start of the range to θ, with its area. Points where r < 0 are not drawn (the r ≥ 0 convention).'));

    function clampT(v) { return Math.max(range[0], Math.min(range[1], v)); }

    /* ---- actions ---- */
    function setCurve(newSrc, newRange, fromPreset) {
      let f2;
      try { f2 = compile(newSrc); const t0 = f2(0.5); if (typeof t0 !== 'number') throw new Error('not a number'); }
      catch (e) { return `Can't read r = ${newSrc}: ${(e && e.message) || 'check the expression'}`; }
      fn = f2; src = newSrc;
      if (newRange) range = newRange;
      areaStart = null;
      sl.input.min = String(range[0]); sl.input.max = String(range[1]); sl.input.step = String(stepFor());
      theta = range[1]; sl.set(theta);
      fitView();
      activePreset = fromPreset || null;
      for (const k of presetKeys) tabBtns[k].setAttribute('aria-pressed', String(k === activePreset));
      update();
      return '';
    }
    function usePreset(k) {
      anim.stop(); playing = false; play.textContent = 'Play';
      warns.length = 0; showWarns();
      exprField.input.value = PRESETS[k].r;
      setCurve(PRESETS[k].r, PRESETS[k].range.slice(), k);
      cv.setLabel && cv.setLabel(`Polar curve r = ${PRESETS[k].r}`);
    }
    exprField.input.addEventListener('input', () => {
      const s = exprField.input.value.trim();
      anim.stop(); playing = false; play.textContent = 'Play';
      warns.length = 0;
      if (!s) { warns.push('Type an expression such as 1+cos(t) or 2*sin(3*t).'); showWarns(); return; }
      const msg = setCurve(s, null, null);
      if (msg) warns.push(msg + '. Keeping the previous curve.');
      showWarns();
    });
    areaBox.addEventListener('change', () => { areaOn = areaBox.checked; update(); });
    let lastTs = null;
    let playing = false;
    const isRunning = () => playing;
    const anim = W.animate(() => {
      const now = (typeof performance !== 'undefined' ? performance.now() : Date.now());
      if (lastTs == null) lastTs = now;
      const dt = Math.min(0.1, Math.max(0, (now - lastTs) / 1000));   // seconds, whatever unit W.animate passes
      lastTs = now;
      theta += dt * (range[1] - range[0]) / 7;
      if (theta >= range[1]) { theta = range[1]; sl.set(theta); update(); play.textContent = 'Play'; playing = false; return false; }
      sl.set(theta); update();
      return true;
    }, { still: () => { theta = range[1]; sl.set(theta); update(); } });
    play.addEventListener('click', () => {
      if (isRunning()) { anim.stop(); playing = false; play.textContent = 'Play'; return; }
      if (theta >= range[1] - 1e-9) { theta = range[0]; sl.set(theta); }
      lastTs = null;
      if (W.reducedMotion && W.reducedMotion()) { anim.start(); return; }   // the end state is drawn at once
      playing = true;
      play.textContent = 'Pause';
      anim.start();
    });
    toStart.addEventListener('click', () => { anim.stop(); playing = false; play.textContent = 'Play'; theta = range[0]; sl.set(theta); update(); });

    /* ---- readout, description ---- */
    let lastNeg = null;
    function areaNow() {
      const A = areaStart != null ? areaStart : range[0];
      return simpsonHalfRSquared(fn, A, theta, 400);
    }
    function update() {
      const r = fn(theta);
      const ok = isFinite(r) && r >= 0;
      R.set('th', `${fmtPi(theta)}  (${fx(theta, 3)} rad)`);
      R.set('r', isFinite(r) ? (ok ? fx(r, 3) : `${fx(r, 3)}: no point`) : 'not defined');
      R.set('xy', ok ? `(${fx(r * Math.cos(theta), 3)}, ${fx(r * Math.sin(theta), 3)})` : 'no point');
      if (areaOn) {
        const a = areaNow(), pm = asPiMultiple(a);
        R.set('area', `½∫ r² dθ ≈ ${fx(a, 4)}${pm ? ` = ${pm}` : ''}`);
      } else R.set('area', 'off');
      const neg = !ok;
      if (neg !== lastNeg) { status.textContent = neg ? 'r < 0 or r not defined here: no point (r ≥ 0 convention).' : ''; lastNeg = neg; }
      cv.redraw();
    }
    function describe() {
      const r = fn(theta), ok = isFinite(r) && r >= 0;
      return `Polar curve r = ${src} for θ from ${fmtPi(range[0])} to ${fmtPi(range[1])}, traced up to θ = ${fmtPi(theta)}. `
        + (ok ? `The point is at r = ${fx(r, 3)}, (x, y) = (${fx(r * Math.cos(theta), 3)}, ${fx(r * Math.sin(theta), 3)}). ` : 'There is no point at this angle (r is negative or not defined). ')
        + (areaOn ? `Shaded sector area ${fx(areaNow(), 4)}.` : '');
    }

    /* ---- drawing ---- */
    function draw(ctx, w, h, c) {
      if (!(w > 0 && h > 0)) return;
      const cx = w / 2, cy = h / 2;
      const rad = Math.max(10, Math.min(w, h) / 2 - 24);
      const k = rad / view.R;
      const P = (r, t) => [cx + r * Math.cos(t) * k, cy - r * Math.sin(t) * k];
      ctx.save();
      ctx.font = `11px ${c.font || 'sans-serif'}`;
      // grid circles
      ctx.lineWidth = 1; ctx.strokeStyle = c.rule2 || c.rule;
      for (let r = view.step; r <= view.R * 1.0001; r += view.step) { ctx.beginPath(); ctx.arc(cx, cy, r * k, 0, TAU); ctx.stroke(); }
      // rays every π/6
      ctx.strokeStyle = c.rule;
      for (let j = 0; j < 12; j++) { const a = j * PI / 6; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + rad * Math.cos(a), cy - rad * Math.sin(a)); ctx.stroke(); }
      // initial line
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + rad, cy); ctx.stroke();
      // labels
      ctx.fillStyle = c.ink2; ctx.textBaseline = 'middle';
      ctx.textAlign = 'left'; ctx.fillText('0', cx + rad + 5, cy);
      ctx.textAlign = 'center'; ctx.fillText('π/2', cx, cy - rad - 9); ctx.fillText('3π/2', cx, cy + rad + 10);
      ctx.textAlign = 'right'; ctx.fillText('π', cx - rad - 5, cy);
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (let r = view.step; r <= view.R * 1.0001; r += view.step) {
        if (r * k > rad - 16) break;   // keep clear of the "0" label at the end of the initial line
        ctx.fillText(W.fmt(r, 3), cx + r * k, cy + 3);
      }
      // "initial line": beyond the outermost ring, never over the curve or the tick labels
      ctx.fillStyle = c.ink2;
      if (w / 2 - rad >= 84) {
        ctx.textAlign = 'left'; ctx.textBaseline = 'middle'; ctx.fillText('initial line', cx + rad + 20, cy);
      } else if (w / 2 - rad >= 18 && cy - 70 > 0) {
        ctx.save(); ctx.translate(cx + rad + 16, cy - 38); ctx.rotate(-PI / 2);
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText('initial line', 0, 0); ctx.restore();
      }
      ctx.textAlign = 'right'; ctx.textBaseline = 'top'; ctx.fillStyle = c.ink2; ctx.fillText('O', cx - 3, cy + 3);

      const n = sampleCount(), span = range[1] - range[0];
      const pts = [];
      for (let i = 0; i <= n; i++) { const t = range[0] + span * i / n; const r = fn(t); pts.push([t, r, isFinite(r) && r >= 0]); }
      // shaded sector
      if (areaOn) {
        const A = areaStart != null ? areaStart : range[0];
        if (theta > A) {
          ctx.fillStyle = c.sc; ctx.globalAlpha = 0.25;
          ctx.beginPath(); let open = false;
          const m = Math.max(2, Math.ceil(n * (theta - A) / span));
          for (let i = 0; i <= m; i++) {
            const t = A + (theta - A) * i / m, r = fn(t);
            if (isFinite(r) && r >= 0) { const q = P(r, t); if (!open) { ctx.moveTo(cx, cy); open = true; } ctx.lineTo(q[0], q[1]); }
            else if (open) { ctx.closePath(); open = false; }
          }
          if (open) ctx.closePath();
          ctx.fill(); ctx.globalAlpha = 1;
        }
      }
      // faint full curve, then traced part
      const trace = (upTo, style, lw) => {
        ctx.strokeStyle = style; ctx.lineWidth = lw; ctx.lineJoin = 'round';
        ctx.beginPath(); let pen = false;
        for (const [t, r, ok] of pts) {
          if (t > upTo + 1e-12) break;
          if (!ok) { pen = false; continue; }
          const q = P(r, t);
          if (pen) ctx.lineTo(q[0], q[1]); else { ctx.moveTo(q[0], q[1]); pen = true; }
        }
        ctx.stroke();
      };
      ctx.globalAlpha = 0.28; trace(range[1], c.sc, 1.4); ctx.globalAlpha = 1;
      trace(theta, c.sc, 2.4);
      // current point and the ray OP
      const rNow = fn(theta);
      if (isFinite(rNow) && rNow >= 0) {
        const q = P(rNow, theta);
        ctx.strokeStyle = c.sc2; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(q[0], q[1]); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = c.red; ctx.beginPath(); ctx.arc(q[0], q[1], 4.5, 0, TAU); ctx.fill();
      } else {
        // no point: show the direction of the ray only, as a short tick on the rim
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([2, 4]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + rad * Math.cos(theta), cy - rad * Math.sin(theta)); ctx.stroke(); ctx.setLineDash([]);
      }
      ctx.restore();
    }

    /* ---- go ---- */
    fitView();
    showWarns();
    for (const k2 of presetKeys) tabBtns[k2].setAttribute('aria-pressed', String(k2 === activePreset));
    sl.set(theta);
    update();
  });
})();
