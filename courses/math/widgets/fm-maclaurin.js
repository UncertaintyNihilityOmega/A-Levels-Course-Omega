/* fm-maclaurin: a function and its Maclaurin polynomial of degree n, drawn together.
   data-f "sin"      exp | sin | cos | ln1p | atan | sinh | cosh | tan   (default sin)
   data-n "3"        degree of the polynomial, 0 to 15
   data-x "-4,4"     the x window (default depends on the function)
   The coefficients are exact (the series formulas, not numerical differentiation); the polynomial is drawn dashed.
   Try: <div class="widget" data-w="fm-maclaurin" data-f="sin" data-n="3" data-x="-6,6"></div> */
(function () {
  'use strict';
  const W = typeof window !== 'undefined' ? window.W : undefined;
  const MAXN = 15;

  /* ---- pure helpers (tested in Node) ---- */
  const gcd = (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) { const t = a % b; a = b; b = t; } return a || 1; };
  const fact = (k) => { let r = 1; for (let i = 2; i <= k; i++) r *= i; return r; };
  const TAN = { 1: [1, 1], 3: [1, 3], 5: [2, 15], 7: [17, 315], 9: [62, 2835], 11: [1382, 155925], 13: [21844, 6081075], 15: [929569, 638512875] };
  const FUNCS = {
    exp:  { label: 'eˣ', name: 'eˣ', f: Math.exp, x: [-3, 3], x0: 1 },
    sin:  { label: 'sin x', name: 'sin x', f: Math.sin, x: [-7, 7], x0: 2 },
    cos:  { label: 'cos x', name: 'cos x', f: Math.cos, x: [-7, 7], x0: 2 },
    ln1p: { label: 'ln(1 + x)', name: 'ln(1 + x)', f: (x) => (x > -1 ? Math.log(1 + x) : NaN), x: [-0.95, 3], x0: 0.5, valid: [-1, 1, false, true] },
    atan: { label: 'tan⁻¹x', name: 'tan⁻¹x', f: Math.atan, x: [-3, 3], x0: 0.8, valid: [-1, 1, true, true] },
    sinh: { label: 'sinh x', name: 'sinh x', f: Math.sinh, x: [-3, 3], x0: 1 },
    cosh: { label: 'cosh x', name: 'cosh x', f: Math.cosh, x: [-3, 3], x0: 1 },
    tan:  { label: 'tan x', name: 'tan x', f: Math.tan, x: [-1.4, 1.4], x0: 0.8, valid: [-Math.PI / 2, Math.PI / 2, false, false] },
  };
  // coefficient of x^k as [numerator, denominator] (reduced, numerator carries the sign); [0, 1] when it is zero
  function coef(fn, k) {
    let num = 0, den = 1;
    const odd = k % 2 === 1;
    switch (fn) {
      case 'exp': num = 1; den = fact(k); break;
      case 'sin': if (odd) { num = ((k - 1) / 2) % 2 ? -1 : 1; den = fact(k); } break;
      case 'cos': if (!odd) { num = (k / 2) % 2 ? -1 : 1; den = fact(k); } break;
      case 'sinh': if (odd) { num = 1; den = fact(k); } break;
      case 'cosh': if (!odd) { num = 1; den = fact(k); } break;
      case 'ln1p': if (k >= 1) { num = k % 2 ? 1 : -1; den = k; } break;
      case 'atan': if (odd) { num = ((k - 1) / 2) % 2 ? -1 : 1; den = k; } break;
      case 'tan': if (odd && TAN[k]) { num = TAN[k][0]; den = TAN[k][1]; } break;
      default: break;
    }
    if (num === 0) return [0, 1];
    const g = gcd(num, den);
    return [num / g, den / g];
  }
  function coefList(fn, n) {
    const out = [];
    for (let k = 0; k <= n; k++) { const c = coef(fn, k); if (c[0] !== 0) out.push({ k, num: c[0], den: c[1] }); }
    return out;
  }
  function evalPoly(fn, n, x) {
    let s = 0;
    for (let k = 0; k <= n; k++) { const c = coef(fn, k); if (c[0] !== 0) s += (c[0] / c[1]) * Math.pow(x, k); }
    return s;
  }
  const SUP = { 0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹' };
  const sup = (k) => String(k).split('').map((d) => SUP[d] || d).join('');
  function termText(t) {
    const a = Math.abs(t.num);
    if (t.k === 0) return String(a) + (t.den !== 1 ? '/' + t.den : '');
    const body = (a === 1 ? '' : String(a)) + 'x' + (t.k === 1 ? '' : sup(t.k));
    return body + (t.den !== 1 ? '/' + t.den : '');
  }
  // "x − x³/6 + x⁵/120 − x⁷/5040 + …": the first four non-zero terms up to degree n
  function polyText(fn, n, maxTerms) {
    const list = coefList(fn, n);
    if (!list.length) return '0';
    const m = maxTerms || 4;
    const show = list.slice(0, m);
    let s = '';
    show.forEach((t, i) => { s += i === 0 ? (t.num < 0 ? '−' : '') : (t.num < 0 ? ' − ' : ' + '); s += termText(t); });
    if (list.length > m) s += ' + …';
    return s;
  }
  const core = { coef, coefList, evalPoly, polyText, sup, FUNCS, MAXN, gcd };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- the widget ---- */
  const fmt = (v) => {
    if (!isFinite(v)) return 'not defined';
    if (Math.abs(v) >= 1e6) return v.toExponential(2);
    if (Math.abs(v) < 5e-7) return '0';
    return W.fmt(v, 5);
  };
  const fmtX = (v) => W.fix(Math.abs(v) < 5e-4 ? 0 : v, 2).replace('-', '−');

  function parseWindow(s) {
    const p = String(s).split(',').map((t) => Number(t.trim().replace(/[−–]/g, '-')));
    if (p.length !== 2 || !p.every((v) => isFinite(v)) || !(p[1] > p[0]) || p[1] - p[0] > 200) throw new Error('needs two numbers like -4,4');
    return p;
  }

  W.register('fm-maclaurin', function (el, o) {
    const warns = [];
    let key = String(o.f || 'sin').trim().toLowerCase();
    if (!FUNCS[key]) { if (o.f) warns.push(`Unknown function "${o.f}". Showing sin x.`); key = 'sin'; }
    let n = 3;
    if (o.n != null && String(o.n).trim() !== '') {
      const v = Math.round(Number(o.n));
      if (isFinite(v)) n = Math.max(0, Math.min(MAXN, v)); else warns.push('data-n should be a whole number from 0 to 15. Using 3.');
    }
    let fixedWin = null;
    if (o.x != null && String(o.x).trim() !== '') {
      try { fixedWin = parseWindow(o.x); } catch (e) { warns.push(`data-x should look like "-4,4" (${e.message}). Using the default window.`); }
    }
    let win = (fixedWin || FUNCS[key].x).slice();
    let x0v = Math.max(win[0], Math.min(win[1], FUNCS[key].x0));

    const { body } = W.frame(el, 'Maclaurin polynomial', 'A function and its polynomial of degree n');

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose a function' });
    const tabBtns = {};
    for (const k of Object.keys(FUNCS)) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false' }, FUNCS[k].label);
      b.addEventListener('click', () => choose(k));
      tabBtns[k] = b; tabs.append(b);
    }
    body.append(W.h('div', { class: 'w-row' }, tabs));

    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    const showWarns = () => { errBox.textContent = warns.join(' '); errBox.style.display = warns.length ? '' : 'none'; };
    body.append(errBox);

    const sN = W.slider({ label: 'Degree n', min: 0, max: MAXN, step: 1, value: n, fmt: (v) => String(Math.round(+v)), oninput: (v) => { n = Math.max(0, Math.min(MAXN, Math.round(+v))); update(); } });
    body.append(sN.el);
    const sX = W.slider({ label: 'Point x₀', min: win[0], max: win[1], step: 0.01, value: x0v, fmt: (v) => fmtX(+v), oninput: (v) => { x0v = +v; update(); } });
    body.append(sX.el);

    // legend (DOM, so it never sits on a curve)
    const sample = (dash, cls) => {
      const ns = 'http://www.w3.org/2000/svg';
      const s = document.createElementNS(ns, 'svg');
      s.setAttribute('width', '34'); s.setAttribute('height', '10'); s.setAttribute('viewBox', '0 0 34 10'); s.setAttribute('aria-hidden', 'true');
      const l = document.createElementNS(ns, 'line');
      l.setAttribute('x1', '1'); l.setAttribute('x2', '33'); l.setAttribute('y1', '5'); l.setAttribute('y2', '5');
      l.setAttribute('stroke-width', '2.6'); if (dash) l.setAttribute('stroke-dasharray', '6 4');
      l.style.stroke = cls === 2 ? 'var(--sc2)' : 'var(--sc)';
      s.append(l);
      return s;
    };
    const lgF = W.h('span', { class: 'w-lab' }, '');
    const lgP = W.h('span', { class: 'w-lab' }, '');
    const legend = W.h('div', { class: 'w-row', style: { alignItems: 'center', gap: '14px' } },
      W.h('span', { style: { display: 'inline-flex', alignItems: 'center', gap: '6px' } }, sample(false, 1), lgF),
      W.h('span', { style: { display: 'inline-flex', alignItems: 'center', gap: '6px' } }, sample(true, 2), lgP));
    body.append(legend);

    /* ---- view ---- */
    const view = { y0: -1, y1: 1 };
    function fitView() {
      const F = FUNCS[key].f;
      const N = 400;
      let lo = Infinity, hi = -Infinity;
      const lim = key === 'tan' ? 6 : 1e6;
      for (let i = 0; i <= N; i++) {
        const v = F(win[0] + (win[1] - win[0]) * i / N);
        if (isFinite(v) && Math.abs(v) <= lim) { if (v < lo) lo = v; if (v > hi) hi = v; }
      }
      if (!isFinite(lo) || !isFinite(hi)) { lo = -1; hi = 1; }
      if (key === 'exp' || key === 'cosh') lo = Math.min(lo, 0);
      let span = hi - lo;
      if (!(span > 1e-9)) { lo -= 1; hi += 1; span = hi - lo; }
      view.y0 = lo - span * 0.1;
      view.y1 = hi + span * 0.1;
    }
    fitView();

    const cv = W.canvas(body, { height: 300, draw, label: 'Maclaurin polynomial and the function', describe });

    const polyBox = W.h('div', { class: 'w-note', style: { overflowWrap: 'anywhere' } }, '');
    body.append(polyBox);
    const R = W.readout([['f', 'f(x₀)'], ['p', 'Polynomial at x₀'], ['e', 'Error f(x₀) − p(x₀)'], ['v', 'Series valid at x₀?']]);
    body.append(R.el);
    const status = W.h('div', { class: 'w-note', 'aria-live': 'polite' }, '');
    body.append(status);
    body.append(W.h('div', { class: 'w-note' }, 'Slide the degree up and watch the dashed polynomial hug the curve near 0, then spread outwards. Only degrees that add a term change the curve: for sin x, degree 2 gives the same polynomial as degree 1, and the line under the readout says when this happens. Move x₀ to see the error. For ln(1 + x) and tan⁻¹x the polynomial leaves the curve outside the range of validity, however large n is.'));

    function choose(k) {
      key = k;
      win = (fixedWin || FUNCS[k].x).slice();
      x0v = Math.max(win[0], Math.min(win[1], FUNCS[k].x0));
      sX.input.min = String(win[0]); sX.input.max = String(win[1]); sX.set(x0v);
      fitView();
      for (const kk of Object.keys(FUNCS)) tabBtns[kk].setAttribute('aria-pressed', String(kk === key));
      cv.setLabel && cv.setLabel(`Graph of ${FUNCS[key].name} and its Maclaurin polynomial`);
      update();
    }

    /* ---- readout ---- */
    function validityAt(x) {
      const v = FUNCS[key].valid;
      if (!v) return 'yes (all x)';
      const inside = (x > v[0] || (v[2] && x === v[0])) && (x < v[1] || (v[3] && x === v[1]));
      return inside ? 'yes' : 'no: outside the range of validity';
    }
    function rangeText() {
      const v = FUNCS[key].valid;
      if (!v) return 'valid for all x';
      if (key === 'tan') return 'valid for |x| < π/2';
      return `valid for ${fmtX(v[0])} ${v[2] ? '≤' : '<'} x ${v[3] ? '≤' : '<'} ${fmtX(v[1])}`;
    }
    function update() {
      const F = FUNCS[key].f;
      const fv = F(x0v), pv = evalPoly(key, n, x0v);
      lgF.textContent = `y = ${FUNCS[key].name}`;
      lgP.textContent = `degree ${n} polynomial`;
      polyBox.textContent = `Polynomial: ${polyText(key, n, 4)}   (${rangeText()})`;
      R.set('f', fmt(fv));
      R.set('p', fmt(pv));
      R.set('e', isFinite(fv) ? fmt(fv - pv) : 'not defined');
      R.set('v', validityAt(x0v));
      const c = coef(key, n);
      status.textContent = n === 0 ? `Degree 0 is the constant term, f(0) = ${fmt(F(0))}.`
        : c[0] === 0 ? `Degree ${n}: the coefficient of x${sup(n)} is 0, so this is the same polynomial as degree ${n - 1}.`
          : `Degree ${n} adds the term in x${sup(n)}.`;
      cv.redraw();
    }
    function describe() {
      const F = FUNCS[key].f;
      const fv = F(x0v), pv = evalPoly(key, n, x0v);
      return `Graph of ${FUNCS[key].name} (solid) and its Maclaurin polynomial of degree ${n} (dashed), for x from ${fmtX(win[0])} to ${fmtX(win[1])}. `
        + `Polynomial: ${polyText(key, n, 4)}. At x = ${fmtX(x0v)}: function ${fmt(fv)}, polynomial ${fmt(pv)}. ${rangeText()}.`;
    }

    /* ---- drawing ---- */
    function draw(ctx, w, h, c) {
      if (!(w > 0 && h > 0)) return;
      const pad = { l: 42, r: 16, t: 14, b: 26 };
      if (!(w > pad.l + pad.r + 20 && h > pad.t + pad.b + 20)) return;
      const F = FUNCS[key].f;
      const A = W.axes(ctx, w, h, { x0: win[0], x1: win[1], y0: view.y0, y1: view.y1 }, c, { pad, xlabel: 'x', ylabel: 'y' });
      const X = A.X, Y = A.Y;
      const L = pad.l, T = pad.t, Rr = w - pad.r, B = h - pad.b;
      ctx.save();
      ctx.beginPath(); ctx.rect(L, T, Rr - L, B - T); ctx.clip();
      // range of validity
      const v = FUNCS[key].valid;
      if (v) {
        const xa = Math.max(L, X(Math.max(v[0], win[0]))), xb = Math.min(Rr, X(Math.min(v[1], win[1])));
        if (xb > xa) {
          ctx.globalAlpha = 0.10; ctx.fillStyle = c.sc; ctx.fillRect(xa, T, xb - xa, B - T); ctx.globalAlpha = 1;
        }
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 4]);
        for (const xv of [v[0], v[1]]) {
          if (xv > win[0] && xv < win[1]) { const px = Math.round(X(xv)) + 0.5; ctx.beginPath(); ctx.moveTo(px, T); ctx.lineTo(px, B); ctx.stroke(); }
        }
        ctx.setLineDash([]);
        if (xb - xa > 90) {
          ctx.font = `11px ${c.font || 'sans-serif'}`; ctx.fillStyle = c.ink2; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
          ctx.fillText('series valid here', (xa + xb) / 2, T + 3);
        }
      }
      const N = Math.max(120, Math.round(Rr - L));
      const clampY = (py) => Math.max(-2000, Math.min(h + 2000, py));
      // the function
      ctx.lineJoin = 'round';
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2.6;
      ctx.beginPath(); let pen = false, prevPy = 0;
      for (let i = 0; i <= N; i++) {
        const x = win[0] + (win[1] - win[0]) * i / N, y = F(x);
        if (!isFinite(y)) { pen = false; continue; }
        const py = Y(y);
        if (pen && Math.abs(py - prevPy) > (B - T) * 3) { pen = false; }   // a pole of tan x: break the line
        if (pen) ctx.lineTo(X(x), clampY(py)); else { ctx.moveTo(X(x), clampY(py)); pen = true; }
        prevPy = py;
      }
      ctx.stroke();
      // the polynomial, dashed
      ctx.strokeStyle = c.sc2; ctx.lineWidth = 2.2; ctx.setLineDash([7, 5]);
      ctx.beginPath(); pen = false;
      for (let i = 0; i <= N; i++) {
        const x = win[0] + (win[1] - win[0]) * i / N, y = evalPoly(key, n, x);
        if (!isFinite(y)) { pen = false; continue; }
        const py = clampY(Y(y));
        if (pen) ctx.lineTo(X(x), py); else { ctx.moveTo(X(x), py); pen = true; }
      }
      ctx.stroke(); ctx.setLineDash([]);
      // the point x0
      const fv = F(x0v), pv = evalPoly(key, n, x0v);
      const px = X(x0v);
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
      ctx.beginPath(); ctx.moveTo(Math.round(px) + 0.5, T); ctx.lineTo(Math.round(px) + 0.5, B); ctx.stroke(); ctx.setLineDash([]);
      if (isFinite(fv) && Math.abs(fv) < 1e6) {
        ctx.fillStyle = c.red; ctx.beginPath(); ctx.arc(px, Y(fv), 4.5, 0, Math.PI * 2); ctx.fill();
      }
      if (isFinite(pv) && Math.abs(Y(pv)) < 1e5) {
        ctx.strokeStyle = c.sc2; ctx.lineWidth = 2; ctx.fillStyle = c.card || c.sheet;
        ctx.beginPath(); ctx.arc(px, Y(pv), 5.5, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      }
      ctx.restore();
    }

    for (const kk of Object.keys(FUNCS)) tabBtns[kk].setAttribute('aria-pressed', String(kk === key));
    showWarns();
    update();
  });
})();
