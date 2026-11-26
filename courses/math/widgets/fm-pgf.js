/* fm-pgf: a probability generating function beside its distribution (9231 Paper 4, Further Statistics).
   data-dist="binomial"   binomial | geometric | poisson | uniform. Default binomial.
   data-params="n=6,p=0.3"  binomial: n (1 to 30), p (0.05 to 0.95); geometric: p (0.1 to 0.9); poisson: lambda (0.5 to 8);
                            uniform on 1..n: n (2 to 20). Missing or invalid values fall back to the defaults.
   data-sum="1"           start with the "sum of two independent copies" switch on (optional).
   Top panel: the bar chart of P(X = x). Bottom panel: G(t) for 0 <= t <= 1.2 with the tangent at t = 1, whose gradient is E(X) = G'(1).
   Readouts: G(t) written out, G(1) = 1, E(X) and Var(X) from G' and G'' (the MF19 formulas), and from the usual formulas (they agree).
   The "sum of two" switch multiplies by a second independent copy (its own parameters) and shows the sum's distribution and PGF.
   data/test_fm_pgf.js tests the numbers: pmf sums, G(1) = 1, E and Var from G against the pmf and the standard formulas, the product rule.
   Try: <div class="widget" data-w="fm-pgf" data-dist="binomial" data-params="n=6,p=0.3"></div> */
(function () {
  'use strict';
  const W = typeof window !== 'undefined' ? window.W : undefined;
  const MINUS = '−';

  /* ---- pure helpers (tested in Node) ---- */
  const LIMITS = {
    binomial: { n: [1, 30, 6, true], p: [0.05, 0.95, 0.3, false] },
    geometric: { p: [0.1, 0.9, 0.25, false] },
    poisson: { lambda: [0.5, 8, 2, false] },
    uniform: { n: [2, 20, 6, true] },
  };
  const DISTS = ['binomial', 'geometric', 'poisson', 'uniform'];

  function parseParams(dist, text, warn) {
    const lim = LIMITS[dist];
    const out = {};
    Object.keys(lim).forEach((k) => { out[k] = lim[k][2]; });
    if (text == null || String(text).trim() === '') return out;
    String(text).split(',').forEach((part) => {
      const bits = part.split('=');
      if (bits.length !== 2) { if (part.trim()) warn.push('Could not read "' + part.trim() + '" in data-params.'); return; }
      const key = bits[0].trim().toLowerCase().replace('λ', 'lambda');
      const v = Number(bits[1].trim());
      if (!lim[key]) { warn.push('data-params: "' + key + '" is not a parameter of the ' + dist + ' distribution.'); return; }
      const [lo, hi, , isInt] = lim[key];
      if (!isFinite(v) || v < lo || v > hi || (isInt && Math.round(v) !== v)) {
        warn.push('data-params: ' + key + ' should be ' + (isInt ? 'a whole number ' : 'a number ') + 'from ' + lo + ' to ' + hi + ', so ' + lim[key][2] + ' is used.');
        return;
      }
      out[key] = v;
    });
    return out;
  }

  const CAP = 30;
  function pmf(dist, pr, cap) {
    const lim = cap || CAP;
    let a = [];
    if (dist === 'binomial') {
      const n = pr.n, p = pr.p, q = 1 - p;
      a = [Math.pow(q, n)];
      for (let x = 0; x < n; x++) a.push(a[x] * (n - x) / (x + 1) * p / q);
    } else if (dist === 'uniform') {
      a = [0];
      for (let x = 1; x <= pr.n; x++) a.push(1 / pr.n);
    } else if (dist === 'poisson') {
      const l = pr.lambda;
      a = [Math.exp(-l)];
      for (let x = 1; x <= lim; x++) {
        a.push(a[x - 1] * l / x);
        if (x > l && 1 - a.reduce((s, v) => s + v, 0) < 1e-4) break;
      }
    } else {
      const p = pr.p, q = 1 - p;
      a = [0];
      let s = 0;
      for (let x = 1; x <= lim; x++) {
        const v = Math.pow(q, x - 1) * p;
        a.push(v); s += v;
        if (1 - s < 1e-3) break;
      }
    }
    return a;
  }
  function pgf(dist, pr, t) {
    if (dist === 'binomial') return Math.pow(1 - pr.p + pr.p * t, pr.n);
    if (dist === 'poisson') return Math.exp(pr.lambda * (t - 1));
    if (dist === 'geometric') { const q = 1 - pr.p; return q * t < 1 ? pr.p * t / (1 - q * t) : NaN; }
    let s = 0;
    for (let x = 1; x <= pr.n; x++) s += Math.pow(t, x);
    return s / pr.n;
  }
  // G'(1) and G''(1) from the derivatives of the closed forms (not from the standard mean and variance)
  function dG(dist, pr) {
    if (dist === 'binomial') { const n = pr.n, p = pr.p; return [n * p, n * (n - 1) * p * p]; }
    if (dist === 'poisson') return [pr.lambda, pr.lambda * pr.lambda];
    if (dist === 'geometric') { const p = pr.p, q = 1 - p; return [1 / p, 2 * q / (p * p)]; }
    const n = pr.n; return [(n + 1) / 2, (n - 1) * (n + 1) / 3];
  }
  function meanVarFromG(g1, g2) { return [g1, g2 + g1 - g1 * g1]; }
  function meanVarFormula(dist, pr) {
    if (dist === 'binomial') return [pr.n * pr.p, pr.n * pr.p * (1 - pr.p)];
    if (dist === 'poisson') return [pr.lambda, pr.lambda];
    if (dist === 'geometric') return [1 / pr.p, (1 - pr.p) / (pr.p * pr.p)];
    return [(pr.n + 1) / 2, (pr.n * pr.n - 1) / 12];
  }
  function meanVarFromPmf(a) {
    const s = a.reduce((u, v) => u + v, 0);
    const m = a.reduce((u, v, x) => u + x * v, 0) / s;
    const e2 = a.reduce((u, v, x) => u + x * x * v, 0) / s;
    return [m, e2 - m * m];
  }
  function convolve(a, b) {
    const out = new Array(a.length + b.length - 1).fill(0);
    for (let i = 0; i < a.length; i++) for (let j = 0; j < b.length; j++) out[i + j] += a[i] * b[j];
    return out;
  }
  // G(t) = G1(t) G2(t); G'(1) and G''(1) by the product rule, using G1(1) = G2(1) = 1
  function sumD(d1, d2) { return [d1[0] + d2[0], d1[1] + 2 * d1[0] * d2[0] + d2[1]]; }
  function upperT(dist, pr) {
    if (dist !== 'geometric') return 1.2;
    return Math.min(1.2, 1 / (1 - pr.p) - 0.015);
  }
  const core = { parseParams, pmf, pgf, dG, meanVarFromG, meanVarFormula, meanVarFromPmf, convolve, sumD, upperT, LIMITS, DISTS };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting ---- */
  function num(x, dp) {
    if (!isFinite(x)) return '—';
    let s = (Math.round(x * Math.pow(10, dp)) / Math.pow(10, dp)).toFixed(dp);
    if (parseFloat(s) === 0) s = (0).toFixed(dp);
    return s.replace('-', MINUS);
  }
  function tidy(x, dp) {
    return num(x, dp === undefined ? 3 : dp).replace(/(\.\d*?)0+$/, '$1').replace(/\.$/, '');
  }
  function sup(n) { return W.sup ? W.sup(String(n)) : '^' + n; }
  function closed(dist, pr) {
    if (dist === 'binomial') return '(' + tidy(1 - pr.p) + ' + ' + tidy(pr.p) + 't)' + sup(pr.n);
    if (dist === 'geometric') return tidy(pr.p) + 't / (1 − ' + tidy(1 - pr.p) + 't)';
    if (dist === 'poisson') return 'e^(' + tidy(pr.lambda) + '(t − 1))';
    return '(t + t² + … + t' + sup(pr.n) + ') / ' + pr.n;
  }
  function name(dist, pr) {
    if (dist === 'binomial') return 'B(' + pr.n + ', ' + tidy(pr.p) + ')';
    if (dist === 'geometric') return 'Geo(' + tidy(pr.p) + ')';
    if (dist === 'poisson') return 'Po(' + tidy(pr.lambda) + ')';
    return 'uniform on 1 to ' + pr.n;
  }

  W.register('fm-pgf', function (el, o) {
    const warn = [];
    let dist = DISTS.indexOf(String(o.dist || 'binomial').toLowerCase()) >= 0 ? String(o.dist || 'binomial').toLowerCase() : 'binomial';
    if (o.dist && DISTS.indexOf(String(o.dist).toLowerCase()) < 0) warn.push('data-dist should be binomial, geometric, poisson or uniform, so binomial is used.');
    const params = {};
    DISTS.forEach((d) => { params[d] = parseParams(d, d === dist ? o.params : '', d === dist ? warn : []); });
    const params2 = {};
    DISTS.forEach((d) => { params2[d] = Object.assign({}, params[d]); });
    // the second copy starts a little different, so the sum is not just a doubling
    params2.binomial.n = Math.max(1, Math.min(30, params.binomial.n > 3 ? params.binomial.n - 2 : params.binomial.n + 2));
    params2.poisson.lambda = Math.min(8, Math.max(0.5, params.poisson.lambda > 1.5 ? params.poisson.lambda - 1 : params.poisson.lambda + 1));
    params2.geometric.p = Math.min(0.9, params.geometric.p < 0.5 ? params.geometric.p + 0.15 : params.geometric.p - 0.15);
    params2.uniform.n = Math.max(2, Math.min(20, params.uniform.n > 4 ? params.uniform.n - 2 : params.uniform.n + 2));
    let sumOn = o.sum === '1' || o.sum === 'true' || o.sum === 'on';

    const { body } = W.frame(el, 'A PGF beside its distribution', 'Change the distribution and its parameters; the tangent at t = 1 has gradient E(X)');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Distribution' });
    const tabBtns = DISTS.map((d) => {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': String(d === dist) }, d === 'poisson' ? 'Poisson' : d[0].toUpperCase() + d.slice(1));
      b.addEventListener('click', () => { dist = d; buildSliders(); update(); });
      tabs.append(b);
      return [d, b];
    });
    const sumBtn = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': String(sumOn) }, 'Sum of two independent copies');
    sumBtn.addEventListener('click', () => { sumOn = !sumOn; buildSliders(); update(); });
    body.append(W.h('div', { class: 'w-row' }, tabs, W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Sum of two' }, sumBtn)));

    const slWrap = W.h('div', { class: 'w-row' });
    body.append(slWrap);
    function buildSliders() {
      slWrap.textContent = '';
      const mk = (store, key, label) => {
        const lim = LIMITS[dist][key];
        const s = W.slider({ label, min: lim[0], max: lim[1], step: lim[3] ? 1 : (key === 'lambda' ? 0.1 : 0.05), value: store[dist][key],
          fmt: (v) => (lim[3] ? String(Math.round(Number(v))) : tidy(Number(v), 2)),
          oninput: (v) => { store[dist][key] = Number(v); update(); } });
        slWrap.append(s.el);
      };
      const names = { n: 'n', p: 'p', lambda: 'λ' };
      Object.keys(LIMITS[dist]).forEach((k) => mk(params, k, (sumOn ? 'First: ' : '') + names[k]));
      if (sumOn) Object.keys(LIMITS[dist]).forEach((k) => mk(params2, k, 'Second: ' + names[k]));
    }
    buildSliders();

    const note = W.h('div', { class: 'w-note' });
    body.append(note);
    const c1 = W.canvas(body, { height: 190, draw: drawBars, label: 'Bar chart of the distribution', describe: describeBars });
    const c2 = W.canvas(body, { height: 210, draw: drawG, label: 'Graph of the probability generating function with its tangent at t = 1', describe: describeG });
    const R = W.readout([['G', 'G(t)'], ['G1', 'G(1)'], ['G12', "G′(1) and G″(1)"], ['E', 'E(X) from G′(1)'], ['V', 'Var(X) from G″(1) + G′(1) − {G′(1)}²'], ['F', 'E(X) and Var(X) from the usual formulas'], ['S', 'The sum is']]);
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, 'Try: binomial n = 6, p = 0.3. Drag p up and watch the tangent steepen (E(X) = np). Switch to the sum of two copies with the same p: the sum is binomial again, with n added. Try different values of p for the two copies: the PGF is still the product, but the sum is no longer a binomial distribution. Curves are drawn for 0 ≤ t ≤ 1.2 (a geometric PGF stops at t = 1/q).'));

    function state() {
      const pr = params[dist];
      const a1 = pmf(dist, pr);
      const d1 = dG(dist, pr);
      if (!sumOn) {
        return { a: a1, d: d1, f: (t) => pgf(dist, pr, t), tmax: upperT(dist, pr), G: closed(dist, pr), form: meanVarFormula(dist, pr), what: '—' };
      }
      const pr2 = params2[dist];
      const a2 = pmf(dist, pr2, 20);
      const d2 = dG(dist, pr2);
      const f1 = meanVarFormula(dist, pr), f2 = meanVarFormula(dist, pr2);
      let what = 'not a standard distribution, but its PGF is still G₁(t) G₂(t)';
      if (dist === 'binomial' && Math.abs(pr.p - pr2.p) < 1e-9) what = 'binomial B(' + (pr.n + pr2.n) + ', ' + tidy(pr.p) + '): the PGF is (q + pt) to the power ' + (pr.n + pr2.n);
      if (dist === 'poisson') what = 'Poisson Po(' + tidy(pr.lambda + pr2.lambda) + '): e to the power ' + tidy(pr.lambda + pr2.lambda) + '(t − 1)';
      return {
        a: convolve(a1, a2), d: sumD(d1, d2), f: (t) => pgf(dist, pr, t) * pgf(dist, pr2, t), tmax: Math.min(upperT(dist, pr), upperT(dist, pr2)),
        G: '[' + closed(dist, pr) + '] × [' + closed(dist, pr2) + ']', form: [f1[0] + f2[0], f1[1] + f2[1]], what,
      };
    }
    function describeBars() {
      const s = state();
      const mv = meanVarFromG(s.d[0], s.d[1]);
      return (sumOn ? 'Bar chart of the sum of two independent variables' : 'Bar chart of ' + name(dist, params[dist])) + ', with ' + s.a.length + ' possible values and mean ' + num(mv[0], 2) + '.';
    }
    function describeG() {
      const s = state();
      return 'The generating function rises through the point (1, 1). The tangent there has gradient G prime of 1, which is the mean ' + num(s.d[0], 3) + '.';
    }
    function update() {
      tabBtns.forEach(([d, b]) => b.setAttribute('aria-pressed', String(d === dist)));
      sumBtn.setAttribute('aria-pressed', String(sumOn));
      const s = state();
      const mv = meanVarFromG(s.d[0], s.d[1]);
      const lab = sumOn ? 'X + Y' : 'X';
      note.textContent = sumOn ? 'Showing S = X + Y, where X and Y are independent ' + (dist === 'poisson' ? 'Poisson' : dist) + ' variables with the first and second parameters above.' : 'Showing X ~ ' + name(dist, params[dist]) + (dist === 'geometric' ? ' (the number of trials up to the first success).' : '.');
      R.set('G', s.G);
      R.set('G1', 'G(1) = ' + num(s.f(1), 3));
      R.set('G12', 'G′(1) = ' + num(s.d[0], 3) + ', G″(1) = ' + num(s.d[1], 3));
      R.set('E', 'E(' + lab + ') = ' + num(mv[0], 3));
      R.set('V', 'Var(' + lab + ') = ' + num(mv[1], 3));
      R.set('F', 'E = ' + num(s.form[0], 3) + ', Var = ' + num(s.form[1], 3) + (Math.abs(s.form[0] - mv[0]) < 1e-9 && Math.abs(s.form[1] - mv[1]) < 1e-9 ? ' (they agree)' : ' (differ)'));
      R.set('S', sumOn ? s.what : 'not used (switch on the sum of two copies)');
      c1.redraw(); c2.redraw();
    }

    function drawBars(ctx, w, h, col) {
      if (!(w > 120 && h > 100)) return;
      const s = state();
      const a = s.a;
      const xmax = a.length - 1;
      let ymax = 0;
      a.forEach((v) => { if (v > ymax) ymax = v; });
      if (!(ymax > 0) || !isFinite(ymax)) return;
      // own axes: the y-axis sits at the left edge, so it never cuts the bar at x = 0
      const padL = 44, padR = 12, padT = 24, padB = 26;
      const plotW = w - padL - padR, plotH = h - padT - padB;
      if (!(plotW > 40 && plotH > 40)) return;
      const yTop = ymax * 1.15;
      const X = (x) => padL + (x + 0.5) / (xmax + 1) * plotW;
      const Y = (v) => padT + plotH - v / yTop * plotH;
      const base = Y(0);
      ctx.font = '11px ' + col.font; ctx.textBaseline = 'middle'; ctx.textAlign = 'right';
      ctx.lineWidth = 1;
      const tickStep = ymax > 0.5 ? 0.25 : ymax > 0.2 ? 0.1 : ymax > 0.1 ? 0.05 : 0.02;
      for (let v = 0; v <= yTop + 1e-9; v += tickStep) {
        ctx.strokeStyle = col.rule; ctx.beginPath(); ctx.moveTo(padL, Y(v)); ctx.lineTo(w - padR, Y(v)); ctx.stroke();
        ctx.fillStyle = col.ink3; ctx.fillText(tidy(v, 2), padL - 6, Y(v));
      }
      ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.4;
      ctx.beginPath(); ctx.moveTo(padL, padT); ctx.lineTo(padL, base); ctx.lineTo(w - padR, base); ctx.stroke();
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      const every = Math.max(1, Math.ceil(24 / Math.max(1, (X(1) - X(0)))));
      for (let x = 0; x <= xmax; x += every) { ctx.fillStyle = col.ink3; ctx.fillText(String(x), X(x), base + 6); }
      ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic'; ctx.fillStyle = col.ink2;
      ctx.fillText('P(X = x)', padL + 6, padT - 8);
      ctx.textAlign = 'right'; ctx.fillText('x', w - padR, base + 20); ctx.textAlign = 'left';
      const bw = Math.max(1, (X(1) - X(0)) * 0.72);
      ctx.fillStyle = col.sc;
      a.forEach((v, x) => {
        if (!(v > 0)) return;
        const top = Y(v);
        ctx.globalAlpha = 0.85;
        ctx.fillRect(X(x) - bw / 2, top, bw, base - top);
        ctx.globalAlpha = 1;
      });
      const step = X(1) - X(0);
      const dp = step >= 34 ? 3 : step >= 22 ? 2 : 0;
      if (dp) {
        ctx.font = '11px ' + col.font; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
        a.forEach((v, x) => {
          if (!(v >= 0.0005)) return;
          const txt = num(v, dp);
          ctx.lineWidth = 3; ctx.strokeStyle = col.card; ctx.strokeText(txt, X(x), Y(v) - 4);
          ctx.fillStyle = col.ink; ctx.fillText(txt, X(x), Y(v) - 4);
        });
      }
      ctx.textAlign = 'left';
    }

    function drawG(ctx, w, h, col) {
      if (!(w > 120 && h > 100)) return;
      const s = state();
      const g1 = s.d[0];
      const tmax = s.tmax;
      if (!(tmax > 0.1)) return;
      const gEnd = s.f(Math.min(1.2, tmax));
      const gTop = isFinite(gEnd) ? gEnd : 3;
      const ymax = Math.max(1.6, Math.min(4, gTop * 1.05));
      const view = { x0: 0, x1: 1.2, y0: 0, y1: ymax };
      const ax = W.axes(ctx, w, h, view, col, { xlabel: 't', ylabel: 'G(t)', nx: 6, ny: 4, fx: (v) => tidy(v, 1), fy: (v) => tidy(v, 1) });
      if (!ax || !ax.X || !ax.Y) return;
      const { X, Y } = ax;
      const left = X(0), right = X(1.2), top = Y(ymax), base = Y(0);
      if (!(right > left + 10) || !(base > top + 10)) return;
      ctx.save();
      ctx.beginPath(); ctx.rect(left, top, right - left, base - top + 1); ctx.clip();
      ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      // vertical line at t = 1
      ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(X(1), base); ctx.lineTo(X(1), Y(1)); ctx.moveTo(left, Y(1)); ctx.lineTo(X(1), Y(1)); ctx.stroke();
      ctx.setLineDash([]);
      // tangent at t = 1
      ctx.strokeStyle = col.red; ctx.lineWidth = 2; ctx.setLineDash([7, 4]);
      ctx.beginPath(); ctx.moveTo(X(0), Y(1 - g1)); ctx.lineTo(X(1.2), Y(1 + 0.2 * g1)); ctx.stroke();
      ctx.setLineDash([]);
      // curve
      ctx.strokeStyle = col.sc; ctx.lineWidth = 2.8;
      const n = 120;
      ctx.beginPath();
      let started = false;
      for (let i = 0; i <= n; i++) {
        const t = tmax * i / n;
        const v = s.f(t);
        if (!isFinite(v)) continue;
        if (!started) { ctx.moveTo(X(t), Y(v)); started = true; } else ctx.lineTo(X(t), Y(v));
      }
      ctx.stroke();
      ctx.restore();
      // asymptote marker for the geometric PGF
      if (tmax < 1.2) {
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 4]);
        ctx.beginPath(); ctx.moveTo(X(tmax + 0.015), base); ctx.lineTo(X(tmax + 0.015), top); ctx.stroke(); ctx.setLineDash([]);
      }
      // the point (1, 1)
      ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(X(1), Y(1), 4, 0, 2 * Math.PI); ctx.fill();
      ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic'; ctx.textAlign = 'left';
      const halo = (txt, x, y) => { ctx.lineWidth = 3; ctx.strokeStyle = col.card; ctx.strokeText(txt, x, y); ctx.fillStyle = col.ink; ctx.fillText(txt, x, y); };
      const lines = ['curve: G(t)' + (tmax < 1.2 ? ' (stops at t = 1/q)' : ''), 'tangent at t = 1:', 'gradient G′(1) = E(X) = ' + num(g1, 2)];
      lines.forEach((txt, i) => halo(txt, left + 8, top + 36 + 16 * i));
      halo('(1, 1)', Math.min(X(1) + 8, right - 44), Math.min(Y(1) + 18, base - 6));
    }

    update();
  });
})();
