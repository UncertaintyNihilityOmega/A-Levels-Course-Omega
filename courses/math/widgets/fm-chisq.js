/* fm-chisq: the chi-squared distribution with the critical region of a chi-squared test (9231 Paper 4, Further Statistics).
   data-v="4"        degrees of freedom: a whole number 1 to 30. Default 4.
   data-alpha="0.05" significance level (upper tail): 0.1, 0.05, 0.025, 0.01 or 0.005 (or "5%"). Default 0.05.
   data-x2="7.2"     a test statistic X² to mark (optional, a number from 0 to 200). Default: none.
   Shows the density of chi-squared with v degrees of freedom, the upper critical region shaded with the critical value labelled
   (3 d.p., as printed in the MF19 table), the statistic marked if given, the MF19 column to read (p = 1 - alpha), P(X > X²) and the
   decision in words. MF19 prints v = 1 to 25 and then 30, 40, ...; for v = 26 to 29 the widget says so.
   data/test_fm_chisq.js tests the numbers against the MF19 rows v = 1, 2, 4, 10, 25 and against numerical integration.
   Try: <div class="widget" data-w="fm-chisq" data-v="5" data-alpha="0.05" data-x2="4.5"></div> */
(function () {
  'use strict';
  const W = typeof window !== 'undefined' ? window.W : undefined;
  const MINUS = '−';

  /* ---- pure helpers (tested in Node) ---- */
  function lgamma(x) {
    const c = [57.1562356658629235, -59.5979603554754912, 14.1360979747417471, -0.491913816097620199,
      0.339946499848118887e-4, 0.465236289270485756e-4, -0.983744753048795646e-4, 0.158088703224912494e-3,
      -0.210264441724104883e-3, 0.217439618115212643e-3, -0.164318106536763890e-3, 0.844182239838527433e-4,
      -0.261908384015814087e-4, 0.368991826595316234e-5];
    let y = x, tmp = x + 5.24218750000000000;
    tmp = (x + 0.5) * Math.log(tmp) - tmp;
    let ser = 0.999999999999997092;
    for (let j = 0; j < 14; j++) ser += c[j] / ++y;
    return tmp + Math.log(2.5066282746310005 * ser / x);
  }
  // regularised incomplete gamma: returns {p: P(a, x), q: Q(a, x) = 1 - P}
  function gammaPQ(a, x) {
    if (!(x > 0)) return { p: 0, q: 1 };
    const lead = Math.exp(-x + a * Math.log(x) - lgamma(a));
    if (x < a + 1) {
      let ap = a, sum = 1 / a, del = sum;
      for (let n = 0; n < 1000; n++) { ap += 1; del *= x / ap; sum += del; if (Math.abs(del) < Math.abs(sum) * 1e-16) break; }
      const p = Math.min(1, sum * lead);
      return { p, q: 1 - p };
    }
    let b = x + 1 - a, c = 1e300, d = 1 / b, h = d;
    for (let i = 1; i < 1000; i++) {
      const an = -i * (i - a); b += 2;
      d = an * d + b; if (Math.abs(d) < 1e-300) d = 1e-300;
      c = b + an / c; if (Math.abs(c) < 1e-300) c = 1e-300;
      d = 1 / d; const del = d * c; h *= del;
      if (Math.abs(del - 1) < 1e-16) break;
    }
    const q = Math.min(1, lead * h);
    return { p: 1 - q, q };
  }
  function chiPdf(x, v) {
    if (x < 0) return 0;
    if (x === 0) return v === 2 ? 0.5 : v === 1 ? Infinity : 0;
    return Math.exp((v / 2 - 1) * Math.log(x) - x / 2 - (v / 2) * Math.LN2 - lgamma(v / 2));
  }
  function chiCdf(x, v) { return x <= 0 ? 0 : gammaPQ(v / 2, x / 2).p; }
  function upperTail(x, v) { return x <= 0 ? 1 : gammaPQ(v / 2, x / 2).q; }
  function chiInv(p, v) {
    // the x with P(X <= x) = p, for 0 < p < 1
    if (!(p > 0 && p < 1)) return NaN;
    let lo = 0, hi = Math.max(10, v * 4 + 40);
    while (chiCdf(hi, v) < p && hi < 1e6) hi *= 2;
    for (let i = 0; i < 100; i++) {
      const mid = (lo + hi) / 2;
      if (chiCdf(mid, v) < p) lo = mid; else hi = mid;
    }
    return (lo + hi) / 2;
  }
  function critical(alpha, v) { return chiInv(1 - alpha, v); }
  function decide(x2, crit) { return x2 == null || !isFinite(x2) ? null : x2 > crit; }
  function inTable(v) { return (v >= 1 && v <= 25) || v === 30; }
  function xMax(v, crit, x2) {
    const base = v + 4 * Math.sqrt(2 * v);
    let m = Math.max(base, 1.3 * (isFinite(crit) ? crit : 0));
    if (x2 != null && isFinite(x2)) m = Math.max(m, Math.min(1.25 * x2, 2.5 * m));
    return m;
  }
  function yMax(v) {
    if (v === 1) return 0.8;
    if (v === 2) return 0.55;
    return 1.3 * chiPdf(v - 2, v);
  }
  const core = { lgamma, gammaPQ, chiPdf, chiCdf, upperTail, chiInv, critical, decide, inTable, xMax, yMax };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting and input ---- */
  function n3(x) {
    if (!isFinite(x)) return '—';
    return (Math.round(x * 1000) / 1000).toFixed(3);
  }
  function fmtX(x) { return String(+x.toFixed(3)); }
  function pFmt(p) {
    if (!isFinite(p)) return '—';
    if (p < 0.0005) return 'less than 0.001';
    return p.toFixed(3);
  }
  const ALPHAS = [[0.1, '10%'], [0.05, '5%'], [0.025, '2.5%'], [0.01, '1%'], [0.005, '0.5%']];
  function parseV(v, warn) {
    if (v == null || String(v).trim() === '') return 4;
    const n = Number(String(v).trim());
    if (!isFinite(n) || n < 1 || n > 30 || Math.round(n) !== n) { warn.push('data-v should be a whole number from 1 to 30, so 4 is used.'); return 4; }
    return n;
  }
  function parseAlpha(v, warn) {
    if (v == null || String(v).trim() === '') return 0.05;
    const raw = String(v).trim();
    const n = Number(raw.replace('%', ''));
    const a = raw.indexOf('%') >= 0 || n > 1 ? n / 100 : n;
    const hit = ALPHAS.find((x) => Math.abs(x[0] - a) < 1e-9);
    if (!hit) { warn.push('data-alpha should be 0.1, 0.05, 0.025, 0.01 or 0.005, so 0.05 is used.'); return 0.05; }
    return hit[0];
  }
  function parseX2(v, warn) {
    if (v == null || String(v).trim() === '') return null;
    const n = Number(String(v).trim());
    if (!isFinite(n) || n < 0 || n > 200) { warn.push('data-x2 should be a number from 0 to 200, so no statistic is shown.'); return null; }
    return n;
  }
  function pcol(alpha) { return String(+(1 - alpha).toFixed(4)); }

  W.register('fm-chisq', function (el, o) {
    const warn = [];
    o = o || {};
    let nu = parseV(o.v, warn);
    let alpha = parseAlpha(o.alpha, warn);
    let xStat = parseX2(o.x2, warn);

    const { body } = W.frame(el, 'The chi-squared distribution and its critical region', 'Change the degrees of freedom and the level; add a test statistic');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const nuS = W.slider({ label: 'Degrees of freedom ν', min: 1, max: 30, step: 1, value: nu, fmt: (v) => String(Math.round(Number(v))),
      oninput: (v) => { nu = Math.round(Number(v)); update(); } });
    body.append(nuS.el);

    const aG = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Significance level (upper tail)' });
    const aBtns = ALPHAS.map(([val, txt]) => {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': String(alpha === val) }, txt);
      b.addEventListener('click', () => { alpha = val; update(); });
      aG.append(b);
      return [val, b];
    });
    body.append(W.h('div', { class: 'w-row' }, aG));
    const xF = W.field({ label: 'Test statistic X² (optional)', type: 'number', step: 0.01, value: xStat == null ? '' : String(xStat), width: '8em',
      oninput: () => {
        const raw = String(xF.input.value).trim();
        const n = Number(raw);
        xStat = raw === '' || !isFinite(n) ? null : Math.max(0, Math.min(200, n));
        update();
      } });
    body.append(W.h('div', { class: 'w-row' }, xF.el));

    const legend = W.h('div', { class: 'w-note' });
    body.append(legend);
    const cv = W.canvas(body, { height: 280, draw, label: 'The chi-squared density with its upper critical region shaded', describe });
    const R = W.readout([['col', 'MF19 column'], ['crit', 'Critical value'], ['p', 'P(X > X²)'], ['dec', 'Decision']]);
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, 'Try: set ν = 5 and 5%, then type X² = 4.5 (do not reject) and 12 (reject). Raise ν with the slider: the curve moves right and the critical value grows. For a goodness-of-fit test ν = classes − 1 − parameters estimated; for a table ν = (rows − 1)(columns − 1).'));

    function state() {
      const crit = critical(alpha, nu);
      const p = xStat == null ? null : upperTail(xStat, nu);
      return { crit, p, dec: decide(xStat, crit) };
    }
    function describe() {
      const s = state();
      return `Density of the chi-squared distribution with ${nu} degrees of freedom. Significance level ${+(alpha * 100).toFixed(1)} per cent, upper tail: critical value ${n3(s.crit)}, shaded to its right. ${xStat == null ? '' : 'The test statistic ' + fmtX(xStat) + (s.dec ? ' is in the critical region.' : ' is not in the critical region.')}`;
    }
    function update() {
      const s = state();
      nuS.set(nu);
      aBtns.forEach(([val, b]) => b.setAttribute('aria-pressed', String(val === alpha)));
      legend.textContent = 'Curve: chi-squared with ν = ' + nu + '. Shaded: the upper critical region (area ' + +(alpha * 100).toFixed(1) + '%). Dashed line: the critical value.';
      R.set('col', 'p = ' + pcol(alpha) + (inTable(nu) ? '' : ' (ν = ' + nu + ' is not printed in MF19, which goes 25, 30, 40, …)'));
      R.set('crit', n3(s.crit));
      if (xStat == null) { R.set('p', 'type a statistic to see it'); R.set('dec', '—'); }
      else {
        R.set('p', pFmt(s.p));
        const cmp = `X² = ${fmtX(xStat)} ${s.dec ? '>' : '≤'} ${n3(s.crit)}`;
        R.set('dec', s.dec ? `${cmp}: reject H₀` : `${cmp}: do not reject H₀`);
      }
      cv.redraw();
    }

    /* ---- drawing ---- */
    function draw(ctx, w, h, col) {
      if (!(w > 140 && h > 120)) return;
      const s = state();
      const XM = xMax(nu, s.crit, xStat);
      const YM = yMax(nu);
      if (!(XM > 0) || !isFinite(XM) || !(YM > 0)) return;
      const view = { x0: 0, x1: XM, y0: 0, y1: YM };
      const ax = W.axes(ctx, w, h, view, col, { xlabel: 'x', ylabel: '', ny: 3, fy: () => '' });
      if (!ax || !ax.X || !ax.Y) return;
      const { X, Y } = ax;
      const left = X(0), right = X(XM), top = Y(YM), base = Y(0);
      if (!(right > left + 10) || !(base > top + 10)) return;
      ctx.save();
      ctx.beginPath(); ctx.rect(left, top, right - left, base - top + 1); ctx.clip();
      ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      const yc = (x) => Math.min(YM * 1.05, chiPdf(x, nu));
      const x0 = XM * 0.002;
      const steps = 240;
      // shaded critical region
      if (s.crit < XM) {
        ctx.beginPath(); ctx.moveTo(X(s.crit), base);
        const n = 90;
        for (let i = 0; i <= n; i++) { const x = s.crit + (XM - s.crit) * i / n; ctx.lineTo(X(x), Y(yc(x))); }
        ctx.lineTo(X(XM), base); ctx.closePath();
        ctx.globalAlpha = 0.35; ctx.fillStyle = col.red; ctx.fill(); ctx.globalAlpha = 1;
      }
      // the density
      ctx.strokeStyle = col.sc; ctx.lineWidth = 2.8;
      ctx.beginPath();
      for (let i = 0; i <= steps; i++) { const x = x0 + (XM - x0) * i / steps; i ? ctx.lineTo(X(x), Y(yc(x))) : ctx.moveTo(X(x), Y(yc(x))); }
      ctx.stroke();
      // critical line
      if (s.crit <= XM) {
        ctx.strokeStyle = col.red; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(X(s.crit), base); ctx.lineTo(X(s.crit), Y(YM * 0.92)); ctx.stroke();
        ctx.setLineDash([]);
      }
      ctx.restore();
      // labels (outside the clip)
      ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic';
      const halo = (txt, x, y, align) => {
        ctx.textAlign = align; ctx.lineWidth = 3; ctx.strokeStyle = col.card; ctx.strokeText(txt, x, y); ctx.fillStyle = col.ink; ctx.fillText(txt, x, y);
      };
      // the vertical-axis label sits at the top right, clear of the curve (for v = 1 and 2 the curve fills the top left)
      halo('density', right - 6, top + 14, 'right');
      if (s.crit <= XM) {
        const t = n3(s.crit);
        const half = ctx.measureText(t).width / 2 + 4;
        halo(t, Math.max(left + half, Math.min(right - half, X(s.crit))), Y(YM * 0.92) - 5, 'center');
      }
      if (xStat != null) {
        const tx = Math.min(XM, xStat);
        const yy = Y(YM * 0.55);
        ctx.strokeStyle = col.ink; ctx.lineWidth = 2.2;
        ctx.beginPath(); ctx.moveTo(X(tx), base); ctx.lineTo(X(tx), yy); ctx.stroke();
        ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(X(tx), yy, 4, 0, 2 * Math.PI); ctx.fill();
        const txt = 'X² = ' + fmtX(xStat) + (xStat > XM ? ' (off the scale)' : '');
        const half = ctx.measureText(txt).width / 2 + 4;
        halo(txt, Math.max(left + half, Math.min(right - half, X(tx))), yy - 9, 'center');
      }
      ctx.textAlign = 'left';
    }

    update();
  });
})();
