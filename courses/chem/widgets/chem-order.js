/* widgets/chem-order.js: order of reaction. Draws [A] against time (with the first four half-lives marked) and rate against [A]
   for a reaction of order 0, 1 or 2, from the rate constant k and the starting concentration [A]0.
   Attributes: data-order="0|1|2" (default 1), data-k="0.10" (0.01 to 1.00; units follow the order), data-a0="1.00" (mol dm-3, 0.10 to 2.00).
   Model: order 0  [A] = [A]0 - k t (until it reaches 0);  order 1  [A] = [A]0 exp(-k t);  order 2  [A] = [A]0 / (1 + k [A]0 t).
   Half-life marks: the time at which [A] first reaches [A]0/2, [A]0/4, [A]0/8 and [A]0/16, and the gaps between them. */
(function () {
  'use strict';

  const SUPD = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  const sup = n => String(n).replace(/[0-9-]/g, c => SUPD[c]);
  const K_MIN = 0.01, K_MAX = 1.00, A_MIN = 0.10, A_MAX = 2.00;
  const KUNITS = ['mol dm⁻³ s⁻¹', 's⁻¹', 'mol⁻¹ dm³ s⁻¹'];
  const EQ = ['rate = k', 'rate = k[A]', 'rate = k[A]²'];
  const WORD = ['order 0', 'order 1', 'order 2'];

  function sci(x) {
    if (!isFinite(x)) return '—';
    if (x === 0) return '0';
    const ax = Math.abs(x);
    if (ax >= 0.01 && ax < 1000) return W.fmt(x, 3);
    const e = Math.floor(Math.log10(ax));
    return (x / Math.pow(10, e)).toFixed(2) + ' × 10' + sup(e);
  }

  function makeModel(n, k, a0) {
    const conc = t => n === 0 ? Math.max(0, a0 - k * t) : n === 1 ? a0 * Math.exp(-k * t) : a0 / (1 + k * a0 * t);
    const T = i => n === 0 ? a0 * (1 - Math.pow(2, -i)) / k : n === 1 ? i * Math.LN2 / k : (Math.pow(2, i) - 1) / (k * a0);
    const halves = [1, 2, 3, 4].map(i => T(i) - T(i - 1));
    const tmax = n === 0 ? a0 / k : T(4) * (n === 1 ? 1.12 : 1.06);
    const rate = a => k * Math.pow(a, n);
    return { n, k, a0, conc, T, halves, tmax, rate };
  }

  W.register('chem-order', function (el, opts) {
    const { body } = W.frame(el, 'Order of reaction', 'See how the order changes the graphs and the half-lives');
    const msgs = [];

    function num(key, lo, hi, fb, what) {
      const raw = opts[key];
      if (raw === undefined || raw === '') return fb;
      const v = Number(String(raw).replace('−', '-'));
      if (!isFinite(v)) { msgs.push('data-' + key + ' must be a number (' + what + '). Showing ' + fb + ' instead.'); return fb; }
      if (key === 'k' && v <= 0) { msgs.push('data-k must be greater than 0: a rate constant of 0 would mean that nothing happens. Showing ' + fb + ' instead.'); return fb; }
      if (v < lo || v > hi) { msgs.push('data-' + key + ' = ' + raw + ' is outside ' + lo + ' to ' + hi + ' (' + what + '), so it was moved to the nearest allowed value.'); return Math.min(hi, Math.max(lo, v)); }
      return v;
    }

    const state = { order: 1, k: 0.10, a0: 1.00 };
    if (opts.order !== undefined && opts.order !== '') {
      const o = Number(opts.order);
      if (o === 0 || o === 1 || o === 2) state.order = o;
      else msgs.push('data-order must be 0, 1 or 2. Showing first order instead.');
    }
    state.k = num('k', K_MIN, K_MAX, 0.10, 'rate constant, 0.01 to 1.00');
    state.a0 = num('a0', A_MIN, A_MAX, 1.00, 'starting concentration in mol dm⁻³, 0.10 to 2.00');

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const tabs = [0, 1, 2].map(n => W.h('button', { class: 'w-tab', type: 'button', 'aria-pressed': 'false', text: 'Order ' + n, onclick: () => { state.order = n; update(); } }));
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Order of reaction' }, tabs)));

    const sK = W.sliderNum({ label: 'Rate constant k', min: K_MIN, max: K_MAX, step: 0.01, value: state.k, oninput: v => { setK(v); } });
    const sA = W.sliderNum({ label: 'Starting concentration [A]₀ (mol dm⁻³)', min: A_MIN, max: A_MAX, step: 0.05, value: state.a0, oninput: v => { setA(v); } });
    body.appendChild(sK.el);
    body.appendChild(sA.el);
    body.appendChild(err);

    let typed = '';
    function setK(v) {
      if (!isFinite(v) || v < K_MIN || v > K_MAX) { typed = 'k must be between ' + K_MIN + ' and ' + K_MAX.toFixed(2) + '.'; state.k = Math.min(K_MAX, Math.max(K_MIN, isFinite(v) ? v : state.k)); }
      else { typed = ''; state.k = v; }
      update();
    }
    function setA(v) {
      if (!isFinite(v) || v < A_MIN || v > A_MAX) { typed = '[A]₀ must be between ' + A_MIN.toFixed(2) + ' and ' + A_MAX.toFixed(2) + ' mol dm⁻³.'; state.a0 = Math.min(A_MAX, Math.max(A_MIN, isFinite(v) ? v : state.a0)); }
      else { typed = ''; state.a0 = v; }
      update();
    }

    const M = { l: 50, r: 14, t: 16, b: 40 };
    function halo(ctx, col, s, x, y, align, color) {
      ctx.textAlign = align || 'left';
      ctx.lineWidth = 4; ctx.strokeStyle = col.card; ctx.lineJoin = 'round';
      ctx.strokeText(s, x, y);
      ctx.fillStyle = color || col.ink; ctx.fillText(s, x, y);
    }

    // shared frame: axes, grid and tick numbers for a view {x1, y1} starting at 0
    function frame(ctx, w, h, col, x1, y1, xlabel, ylabel) {
      const px0 = M.l, px1 = w - M.r, py0 = h - M.b, py1 = M.t;
      const X = v => px0 + (px1 - px0) * v / x1;
      const Y = v => py0 - (py0 - py1) * v / y1;
      ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic'; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
      let yt = W.ticks(0, y1, 4); if (!Array.isArray(yt) || !yt.length) yt = [0, y1];
      let xt = W.ticks(0, x1, 5); if (!Array.isArray(xt) || !xt.length) xt = [0, x1];
      ctx.lineWidth = 1;
      yt.forEach(v => {
        if (v < 0 || v > y1 * 1.0001) return;
        ctx.strokeStyle = col.rule; ctx.beginPath(); ctx.moveTo(px0, Y(v)); ctx.lineTo(px1, Y(v)); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.textAlign = 'right'; ctx.fillText(sci(v), px0 - 6, Y(v) + 4);
      });
      xt.forEach(v => {
        if (v < 0 || v > x1 * 1.0001) return;
        ctx.strokeStyle = col.rule; ctx.beginPath(); ctx.moveTo(X(v), py0); ctx.lineTo(X(v), py1); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center'; ctx.fillText(sci(v), X(v), py0 + 16);
      });
      ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(px0, py0); ctx.lineTo(px0, py1 - 4); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(px0, py0); ctx.lineTo(px1 + 4, py0); ctx.stroke();
      ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
      ctx.fillText(xlabel, (px0 + px1) / 2, h - 6);
      ctx.save(); ctx.translate(11, (py0 + py1) / 2); ctx.rotate(-Math.PI / 2); ctx.textAlign = 'center'; ctx.fillText(ylabel, 0, 0); ctx.restore();
      return { X, Y, px0, px1, py0, py1 };
    }

    let m = makeModel(state.order, state.k, state.a0);

    const cvsT = W.canvas(body, {
      height: 250,
      draw(ctx, w, h, col) {
        if (!(w > 120) || !(h > 120)) return;
        const f = frame(ctx, w, h, col, m.tmax, m.a0 * 1.1, 'time / s', '[A] / mol dm⁻³');
        // half-life guides
        ctx.setLineDash([5, 4]); ctx.lineWidth = 1.2; ctx.strokeStyle = col.ink3;
        for (let i = 1; i <= 4; i++) {
          const t = m.T(i), a = m.a0 / Math.pow(2, i);
          ctx.beginPath(); ctx.moveTo(f.px0, f.Y(a)); ctx.lineTo(f.X(t), f.Y(a)); ctx.lineTo(f.X(t), f.py0); ctx.stroke();
        }
        ctx.setLineDash([]);
        // curve
        ctx.save(); ctx.beginPath(); ctx.rect(f.px0, f.py1 - 2, f.px1 - f.px0 + 2, f.py0 - f.py1 + 4); ctx.clip();
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.8; ctx.beginPath();
        const N = 200;
        for (let i = 0; i <= N; i++) { const t = m.tmax * i / N; const x = f.X(t), y = f.Y(m.conc(t)); if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y); }
        ctx.stroke(); ctx.restore();
        // dots and interval labels
        for (let i = 1; i <= 4; i++) {
          const t = m.T(i), a = m.a0 / Math.pow(2, i);
          ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(f.X(t), f.Y(a), 3.6, 0, 2 * Math.PI); ctx.fill();
          const xa = f.X(m.T(i - 1)), xb = f.X(t);
          if (xb - xa >= 60 && f.py0 - f.Y(a) >= 26) halo(ctx, col, sci(m.halves[i - 1]) + ' s', (xa + xb) / 2, f.Y(a) + 15, 'center', col.ink);
        }
      }
    });
    cvsT.cv.setAttribute('role', 'img');
    cvsT.describe = () => {
      const shape = m.n === 0 ? 'a straight line falling to zero' : m.n === 1 ? 'an exponential decay' : 'a curve falling steeply then levelling off';
      return 'Concentration [A] against time in seconds, ' + shape + ', starting at ' + W.fmt(m.a0, 3) + ' mol dm⁻³. Dots mark [A]₀/2, /4, /8 and /16 at ' + [1, 2, 3, 4].map(i => sci(m.T(i)) + ' s').join(', ') + '. Successive half-lives: ' + m.halves.map(sci).join(', ') + ' s.';
    };

    const cvsR = W.canvas(body, {
      height: 230,
      draw(ctx, w, h, col) {
        if (!(w > 120) || !(h > 120)) return;
        const rmax = Math.max(m.rate(m.a0), 1e-12) * 1.2;
        const f = frame(ctx, w, h, col, m.a0 * 1.05, rmax, '[A] / mol dm⁻³', 'rate / mol dm⁻³ s⁻¹');
        ctx.save(); ctx.beginPath(); ctx.rect(f.px0, f.py1 - 2, f.px1 - f.px0 + 2, f.py0 - f.py1 + 4); ctx.clip();
        ctx.strokeStyle = col.sc2; ctx.lineWidth = 2.8; ctx.beginPath();
        const N = 80;
        for (let i = 0; i <= N; i++) { const a = m.a0 * i / N; const x = f.X(a), y = f.Y(m.rate(a)); if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y); }
        ctx.stroke(); ctx.restore();
        const px = f.X(m.a0), py = f.Y(m.rate(m.a0));
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(px, py, 3.8, 0, 2 * Math.PI); ctx.fill();
        halo(ctx, col, 'rate at [A]₀', Math.min(px - 8, f.px1 - 4), py - 10, 'right', col.ink);
        halo(ctx, col, EQ[m.n], f.px0 + 8, f.py1 + 14, 'left', col.ink2);
      }
    });
    cvsR.cv.setAttribute('role', 'img');
    cvsR.describe = () => 'Rate against [A], ' + (m.n === 0 ? 'a horizontal line' : m.n === 1 ? 'a straight line through the origin' : 'a parabola through the origin') + ' for ' + EQ[m.n] + '. At the starting concentration ' + W.fmt(m.a0, 3) + ' mol dm⁻³ the rate is ' + sci(m.rate(m.a0)) + ' mol dm⁻³ s⁻¹.';

    const read = W.readout([['eq', 'Rate equation'], ['k', 'Rate constant, k'], ['hl', 'First half-life'], ['hls', 'Successive half-lives'], ['r0', 'Rate at t = 0']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'For first order, change [A]₀: the half-life stays the same. For second order it doubles from one half-life to the next, and for zero order it halves.' }));

    function update() {
      m = makeModel(state.order, state.k, state.a0);
      tabs.forEach((b, i) => b.setAttribute('aria-pressed', i === state.order ? 'true' : 'false'));
      const lab = sK.el.querySelector('label');
      if (lab) lab.textContent = 'Rate constant k (' + KUNITS[state.order] + ')';
      const rng = sK.el.querySelector('input[type="range"]');
      if (rng) rng.setAttribute('aria-label', 'Rate constant k, ' + KUNITS[state.order]);
      err.textContent = (msgs.join(' ') + ' ' + typed).trim();
      read.set('eq', EQ[state.order] + ' (' + WORD[state.order] + ')');
      read.set('k', W.fmt(state.k, 3) + ' ' + KUNITS[state.order]);
      read.set('hl', sci(m.halves[0]) + ' s');
      const pattern = state.order === 1 ? 'constant' : state.order === 2 ? 'doubling' : 'halving';
      read.set('hls', m.halves.map(sci).join(', ') + ' s (' + pattern + ')');
      read.set('r0', sci(m.rate(m.a0)) + ' mol dm⁻³ s⁻¹');
      cvsT.setLabel('[A] against time for ' + WORD[state.order] + ' (half-lives ' + pattern + ')');
      cvsR.setLabel('Rate against [A] for ' + WORD[state.order]);
      cvsT.redraw();
      cvsR.redraw();
    }
    update();
  });
})();
