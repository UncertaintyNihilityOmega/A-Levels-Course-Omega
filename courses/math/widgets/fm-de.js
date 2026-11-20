/* fm-de: the solution of a y'' + b y' + c y = 0 (a constant-coefficient second order equation, 9231 Paper 2) with y(0) and y'(0) given.
   data-a="1"             coefficient of y'' (fixed; 0.1 to 10), default 1
   data-b="2" data-c="5"  the sliders' starting values (b from -4 to 10, c from -6 to 30)
   data-y0="1" data-v0="0"  y(0) and y'(0) (from -100 to 100)
   Shows the auxiliary equation, its roots, the form of the complementary function, the exact solution through (0, y0) with gradient v0
   and its graph for 0 <= x <= 10. No numerical solver: each case uses its formula (data/test_fm_de.js compares them with RK4).
   Try: <div class="widget" data-w="fm-de" data-a="1" data-b="2" data-c="5" data-y0="1" data-v0="0"></div> */
(function () {
  'use strict';
  const W = typeof window !== 'undefined' ? window.W : undefined;
  const TAU = 2 * Math.PI;

  /* ---- pure helpers (tested in Node) ---- */
  function solve(a, b, c, y0, v0) {
    // the exact solution of a y'' + b y' + c y = 0 with y(0) = y0, y'(0) = v0
    const disc = b * b - 4 * a * c;
    const scale = Math.max(1, b * b, Math.abs(4 * a * c));
    if (Math.abs(disc) <= 1e-9 * scale) {
      const m = -b / (2 * a), A = y0, B = v0 - m * y0;
      return { kind: 'repeated', disc: 0, m, p: m, q: 0, A, B, re: m, f: (x) => (A + B * x) * Math.exp(m * x) };
    }
    if (disc > 0) {
      const s = Math.sqrt(disc), m1 = (-b + s) / (2 * a), m2 = (-b - s) / (2 * a);
      const B = (v0 - m1 * y0) / (m2 - m1), A = y0 - B;
      return { kind: 'real', disc, m1, m2, A, B, re: Math.max(m1, m2), f: (x) => A * Math.exp(m1 * x) + B * Math.exp(m2 * x) };
    }
    const p = -b / (2 * a), q = Math.sqrt(-disc) / (2 * a);
    const A = y0, B = (v0 - p * y0) / q;
    return { kind: 'complex', disc, p, q, A, B, re: p, f: (x) => Math.exp(p * x) * (A * Math.cos(q * x) + B * Math.sin(q * x)) };
  }
  function grows(s) {
    // does the solution grow without bound as x increases?
    if (s.kind === 'repeated') return s.m > 1e-9 || (Math.abs(s.m) <= 1e-9 && Math.abs(s.B) > 1e-9);
    if (s.kind === 'real') return (s.m1 > 1e-9 && Math.abs(s.A) > 1e-12) || (s.m2 > 1e-9 && Math.abs(s.B) > 1e-12);
    return s.p > 1e-9 && Math.hypot(s.A, s.B) > 1e-12;
  }
  function sample(f, x0, x1, n) {
    const out = [];
    for (let i = 0; i <= n; i++) { const x = x0 + (x1 - x0) * i / n; out.push([x, f(x)]); }
    return out;
  }
  function viewRange(s, y0) {
    // vertical range for 0 <= x <= 10: follows the solution; a growing one is capped and flagged
    const pts = sample(s.f, 0, 10, 400).filter((p) => isFinite(p[1]));
    let lo = 0, hi = 0, early = Math.max(1, Math.abs(y0));
    pts.forEach((p) => { if (p[0] <= 1.5) early = Math.max(early, Math.abs(p[1])); lo = Math.min(lo, p[1]); hi = Math.max(hi, p[1]); });
    const cap = 8 * early, g = grows(s);
    let capped = false;
    if (g && Math.max(hi, -lo) > cap) { capped = true; hi = Math.min(hi, cap); lo = Math.max(lo, -cap); }
    if (!(hi - lo > 1e-9)) { hi = 1; lo = -1; }
    const span = hi - lo;
    return { y0: lo - 0.1 * span, y1: hi + 0.2 * span, capped, grows: g };
  }
  const core = { solve, grows, viewRange, sample };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting ---- */
  const MINUS = '−';
  function num3(x) {
    if (!isFinite(x)) return '—';
    if (Math.abs(x) >= 1e6 || (x !== 0 && Math.abs(x) < 1e-4)) return Number(x).toExponential(2).replace('-', MINUS);
    let v = parseFloat(Number(x).toPrecision(3));
    if (Object.is(v, -0)) v = 0;
    return String(v).replace('-', MINUS);
  }
  function coefStr(k, rest) {
    // "1.5 e^(…)": a coefficient in front of a term; 1 and -1 are written as nothing and a minus
    if (rest === '') return num3(k);
    return Math.abs(k - 1) < 5e-4 ? rest : Math.abs(k + 1) < 5e-4 ? MINUS + rest : num3(k) + ' ' + rest;
  }
  function joinTerms(terms) {
    // terms: [[coefficient, text]] with text '' for a constant; zero coefficients are dropped
    const live = terms.filter((t) => Math.abs(t[0]) > 5e-4);
    if (!live.length) return '0';
    let out = '';
    live.forEach((t, i) => {
      const s = coefStr(Math.abs(t[0]), t[1]);
      if (i === 0) out += (t[0] < 0 ? MINUS : '') + s;
      else out += (t[0] < 0 ? ' ' + MINUS + ' ' : ' + ') + s;
    });
    return out;
  }
  const expo = (m) => Math.abs(m) < 5e-4 ? '' : Math.abs(m - 1) < 5e-4 ? 'e^x' : Math.abs(m + 1) < 5e-4 ? 'e^(' + MINUS + 'x)' : 'e^(' + num3(m) + 'x)';
  function polyStr(a, b, c) {
    const part = (k, v) => (Math.abs(k - 1) < 5e-4 && v ? v : num3(Math.abs(k)) + v);
    let s = part(a, 'm²');
    s += (b < 0 ? ' ' + MINUS + ' ' : ' + ') + part(Math.abs(b), 'm');
    s += (c < 0 ? ' ' + MINUS + ' ' : ' + ') + num3(Math.abs(c));
    return s + ' = 0';
  }
  function describeSolution(s) {
    if (s.kind === 'real') {
      if (s.m1 < -1e-9 && s.m2 < -1e-9) return `roots ${num3(s.m1)} and ${num3(s.m2)}: no oscillation, the solution dies away`;
      if (s.re > 1e-9) return `roots ${num3(s.m1)} and ${num3(s.m2)}: a positive root, so the solution grows without bound`;
      return `roots ${num3(s.m1)} and ${num3(s.m2)}: a root of 0, so the solution settles to a constant or dies away`;
    }
    if (s.kind === 'repeated') {
      if (s.m < -1e-9) return `repeated root ${num3(s.m)}: critical damping, no oscillation, the solution dies away`;
      if (s.m > 1e-9) return `repeated root ${num3(s.m)}: the solution grows without bound`;
      return 'repeated root 0: the solution is a straight line y = A + Bx';
    }
    const rr = `roots ${num3(s.p)} ± ${num3(s.q)}i`;
    if (s.p < -1e-9) return rr + ': oscillations that die away';
    if (s.p > 1e-9) return rr + ': oscillations that grow without bound';
    return rr + ': oscillations of constant amplitude';
  }
  function cfText(s) {
    if (s.kind === 'real') return 'y = A' + (expo(s.m1) ? ' ' + expo(s.m1) : '') + ' + B' + (expo(s.m2) ? ' ' + expo(s.m2) : '');
    if (s.kind === 'repeated') return 'y = (A + Bx)' + (expo(s.m) ? ' ' + expo(s.m) : '');
    return 'y = ' + (expo(s.p) ? expo(s.p) + ' ' : '') + `(A cos ${num3(s.q)}x + B sin ${num3(s.q)}x)`;
  }
  function solText(s) {
    if (s.kind === 'real') return 'y = ' + joinTerms([[s.A, expo(s.m1)], [s.B, expo(s.m2)]]);
    if (s.kind === 'repeated') {
      const e = expo(s.m);
      const inner = joinTerms([[s.A, ''], [s.B, 'x']]);
      if (Math.abs(s.B) <= 5e-4 || Math.abs(s.A) <= 5e-4) return 'y = ' + joinTerms([[s.A, e], [s.B, e ? 'x ' + e : 'x']]);
      return 'y = (' + inner + ')' + (e ? ' ' + e : '');
    }
    const e = expo(s.p);
    const inner = joinTerms([[s.A, 'cos ' + num3(s.q) + 'x'], [s.B, 'sin ' + num3(s.q) + 'x']]);
    if (!e) return 'y = ' + inner;
    return 'y = ' + (inner.indexOf(' ') < 0 ? e + ' ' + inner : e + '(' + inner + ')');
  }

  /* ---- input parsing ---- */
  function parseNum(v, dflt, lo, hi, name, warn) {
    if (v == null || String(v).trim() === '') return dflt;
    const n = Number(String(v).replace(MINUS, '-'));
    if (!isFinite(n) || n < lo || n > hi) { warn.push(`${name} should be a number from ${lo} to ${hi}, so ${dflt} is used.`); return dflt; }
    return n;
  }

  W.register('fm-de', function (el, o) {
    const warn = [];
    const a = parseNum(o.a, 1, 0.1, 10, 'data-a', warn);
    let b = parseNum(o.b, 2, -4, 10, 'data-b', warn);
    let c = parseNum(o.c, 5, -6, 30, 'data-c', warn);
    let y0 = parseNum(o.y0, 1, -100, 100, 'data-y0', warn);
    let v0 = parseNum(o.v0, 0, -100, 100, 'data-v0', warn);
    const start = { b, c, y0, v0 };
    const aName = a === 1 ? '' : num3(a);

    const { body } = W.frame(el, 'Second order equation: ' + (aName ? aName + ' ' : '') + 'y″ + b y′ + c y = 0', 'Slide b and c, set the starting values y(0) and y′(0)');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    const setErr = (t) => { errBox.textContent = t; errBox.style.display = t ? '' : 'none'; };
    setErr(warn.join(' '));
    body.append(errBox);

    const bS = W.sliderNum({ label: 'b (the coefficient of y′)', min: -4, max: 10, step: 0.1, value: b, oninput: (v) => { b = Number(v); update(); } });
    const cS = W.sliderNum({ label: 'c (the coefficient of y)', min: -6, max: 30, step: 0.1, value: c, oninput: (v) => { c = Number(v); update(); } });
    body.append(bS.el, cS.el);
    const y0F = W.field({ label: 'y(0)', value: String(y0), type: 'number', step: '0.1', width: '6em' });
    const v0F = W.field({ label: 'y′(0), the gradient at the start', value: String(v0), type: 'number', step: '0.1', width: '6em' });
    const resetBtn = W.h('button', { type: 'button', class: 'btn btn-sm btn-sec', 'aria-label': 'Reset b, c, y(0) and y′(0) to their starting values' }, 'Reset');
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } }, y0F.el, v0F.el, resetBtn));

    let model = null, view = null;
    const cv = W.canvas(body, { height: 300, draw, label: 'Graph of the solution of the second order equation', describe });
    const R = W.readout([['ae', 'Auxiliary equation'], ['roots', 'Roots'], ['cf', 'Complementary function'], ['sol', 'Solution through the start'], ['case', 'What it does']]);
    body.append(R.el);
    const note = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.append(note);
    body.append(W.h('div', { class: 'w-note' },
      'Try it: with b = 0 and c > 0 the solution oscillates for ever; b > 0 makes the oscillation die away; b < 0 makes it grow. Make b² = 4ac (b = 4, c = 4 with a = 1) for the repeated root, and keep c below that for two real roots and no oscillation. Dashed curves, when shown, are the envelope the oscillation stays inside.'));

    function readFields() {
      const yy = Number(y0F.input.value), vv = Number(v0F.input.value);
      if (y0F.input.value.trim() === '' || !isFinite(yy) || Math.abs(yy) > 100) return 'Type y(0) as a number from −100 to 100.';
      if (v0F.input.value.trim() === '' || !isFinite(vv) || Math.abs(vv) > 100) return 'Type y′(0) as a number from −100 to 100.';
      y0 = yy; v0 = vv;
      return '';
    }
    const onType = () => { const m = readFields(); setErr(m); if (!m) update(); };
    y0F.input.addEventListener('input', onType);
    v0F.input.addEventListener('input', onType);
    resetBtn.addEventListener('click', () => {
      b = start.b; c = start.c; y0 = start.y0; v0 = start.v0;
      bS.set(b); cS.set(c); y0F.input.value = String(y0); v0F.input.value = String(v0);
      setErr(''); update();
    });

    function update() {
      model = solve(a, b, c, y0, v0);
      view = viewRange(model, y0);
      R.set('ae', polyStr(a, b, c));
      if (model.kind === 'real') R.set('roots', `m = ${num3(model.m1)} or m = ${num3(model.m2)}  (two distinct real roots)`);
      else if (model.kind === 'repeated') R.set('roots', `m = ${num3(model.m)}  (repeated)`);
      else R.set('roots', `m = ${num3(model.p)} ± ${num3(model.q)}i  (complex)`);
      R.set('cf', cfText(model));
      R.set('sol', solText(model));
      R.set('case', describeSolution(model));
      note.textContent = view.capped ? 'The solution grows without bound, so the vertical range is capped and the curve leaves the picture.' : '';
      cv.redraw();
    }
    function describe() {
      if (!model) return 'No picture yet.';
      return `Graph of y against x from 0 to 10 for ${describeSolution(model)}. It starts at y = ${num3(y0)} with gradient ${num3(v0)}. ${solText(model)}.${view && view.capped ? ' It grows without bound, so the vertical range is capped.' : ''}`;
    }

    function draw(ctx, w, h, col) {
      if (!(w > 60 && h > 60) || !model || !view) return;
      const pad = { l: 46, r: 14, t: 18, b: 26 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      if (!(pw > 20 && ph > 20)) return;
      const A = W.axes(ctx, w, h, { x0: 0, x1: 10, y0: view.y0, y1: view.y1 }, col, { pad, xlabel: 'x', ylabel: 'y' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
      // envelope for oscillations
      if (model.kind === 'complex') {
        const Rr = Math.hypot(model.A, model.B);
        if (Rr > 1e-9) {
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([5, 4]);
          [1, -1].forEach((sg) => {
            ctx.beginPath();
            for (let i = 0; i <= 120; i++) {
              const x = 10 * i / 120, v = sg * Rr * Math.exp(model.p * x);
              if (!isFinite(v)) continue;
              i ? ctx.lineTo(X(x), Y(v)) : ctx.moveTo(X(x), Y(v));
            }
            ctx.stroke();
          });
          ctx.setLineDash([]);
        }
      }
      // initial gradient
      ctx.strokeStyle = col.sc2; ctx.lineWidth = 1.4; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(X(0), Y(y0)); ctx.lineTo(X(1.2), Y(y0 + 1.2 * v0)); ctx.stroke(); ctx.setLineDash([]);
      // the solution
      ctx.strokeStyle = col.sc; ctx.lineWidth = 2.2; ctx.lineJoin = 'round';
      ctx.beginPath();
      let pen = false;
      sample(model.f, 0, 10, Math.max(60, Math.min(500, Math.floor(pw)))).forEach((p) => {
        if (!isFinite(p[1])) { pen = false; return; }
        const yy = Math.max(-1e6, Math.min(1e6, p[1]));
        const px = X(p[0]), py = Y(yy);
        if (!pen) { ctx.moveTo(px, py); pen = true; } else ctx.lineTo(px, py);
      });
      ctx.stroke();
      ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(0), Y(y0), 4.2, 0, TAU); ctx.fill();
      ctx.restore();
    }

    update();
  });
})();
