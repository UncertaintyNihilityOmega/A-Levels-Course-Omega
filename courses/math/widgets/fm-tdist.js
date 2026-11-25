/* fm-tdist: the t-distribution against the normal, with the critical region of a t-test (9231 Paper 4, Further Statistics).
   data-v="9"        degrees of freedom: a whole number 1 to 60, or "inf" for the normal. Default 9.
   data-alpha="0.05" significance level: 0.1, 0.05, 0.02 or 0.01. Default 0.05.
   data-tails="2"    1 (upper tail) or 2 (both tails). Default 2.
   data-t="2.9"      a test statistic to mark (optional, a number from -50 to 50). Default: none.
   Shows the N(0, 1) density (dashed) and the t density (solid), the critical region shaded on the t curve with the critical value
   labelled, the statistic marked if given, the MF19 column to read (p = 1 - alpha/tails), the critical value (3 d.p., from the
   incomplete beta function, so it matches the printed table), the normal critical value, the p-value of the statistic and the decision.
   data/test_fm_tdist.js tests the numbers against the MF19 rows nu = 1, 5, 10, 30 and against numerical integration.
   Try: <div class="widget" data-w="fm-tdist" data-v="9" data-alpha="0.05" data-tails="2" data-t="2.9"></div> */
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
  function betacf(a, b, x) {
    const FPMIN = 1e-300;
    let qab = a + b, qap = a + 1, qam = a - 1, c = 1, d = 1 - qab * x / qap;
    if (Math.abs(d) < FPMIN) d = FPMIN;
    d = 1 / d;
    let h = d;
    for (let m = 1; m <= 400; m++) {
      const m2 = 2 * m;
      let aa = m * (b - m) * x / ((qam + m2) * (a + m2));
      d = 1 + aa * d; if (Math.abs(d) < FPMIN) d = FPMIN;
      c = 1 + aa / c; if (Math.abs(c) < FPMIN) c = FPMIN;
      d = 1 / d; h *= d * c;
      aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2));
      d = 1 + aa * d; if (Math.abs(d) < FPMIN) d = FPMIN;
      c = 1 + aa / c; if (Math.abs(c) < FPMIN) c = FPMIN;
      d = 1 / d;
      const del = d * c; h *= del;
      if (Math.abs(del - 1) < 1e-14) break;
    }
    return h;
  }
  function betai(a, b, x) {
    if (x <= 0) return 0;
    if (x >= 1) return 1;
    const bt = Math.exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * Math.log(x) + b * Math.log(1 - x));
    return x < (a + 1) / (a + b + 2) ? bt * betacf(a, b, x) / a : 1 - bt * betacf(b, a, 1 - x) / b;
  }
  function gammp(a, x) {
    // regularised lower incomplete gamma P(a, x)
    if (x <= 0) return 0;
    if (x < a + 1) {
      let ap = a, sum = 1 / a, del = sum;
      for (let n = 0; n < 500; n++) { ap += 1; del *= x / ap; sum += del; if (Math.abs(del) < Math.abs(sum) * 1e-15) break; }
      return sum * Math.exp(-x + a * Math.log(x) - lgamma(a));
    }
    let b = x + 1 - a, c = 1e300, d = 1 / b, h = d;
    for (let i = 1; i < 500; i++) {
      const an = -i * (i - a); b += 2;
      d = an * d + b; if (Math.abs(d) < 1e-300) d = 1e-300;
      c = b + an / c; if (Math.abs(c) < 1e-300) c = 1e-300;
      d = 1 / d; const del = d * c; h *= del;
      if (Math.abs(del - 1) < 1e-15) break;
    }
    return 1 - Math.exp(-x + a * Math.log(x) - lgamma(a)) * h;
  }
  function normPdf(x) { return Math.exp(-x * x / 2) / Math.sqrt(2 * Math.PI); }
  function normCdf(x) {
    const g = gammp(0.5, x * x / 2);
    return x >= 0 ? 0.5 * (1 + g) : 0.5 * (1 - g);
  }
  function tPdf(x, v) {
    if (!isFinite(v)) return normPdf(x);
    return Math.exp(lgamma((v + 1) / 2) - lgamma(v / 2) - 0.5 * Math.log(v * Math.PI) - (v + 1) / 2 * Math.log(1 + x * x / v));
  }
  function tCdf(x, v) {
    if (!isFinite(v)) return normCdf(x);
    if (x === 0) return 0.5;
    const ib = betai(v / 2, 0.5, v / (v + x * x));
    return x > 0 ? 1 - 0.5 * ib : 0.5 * ib;
  }
  function tInv(p, v) {
    // the t with P(T <= t) = p, for 0.5 <= p < 1
    if (!(p >= 0.5 && p < 1)) return NaN;
    let lo = 0, hi = 2000;
    for (let i = 0; i < 90; i++) {
      const mid = (lo + hi) / 2;
      if (tCdf(mid, v) < p) lo = mid; else hi = mid;
    }
    return (lo + hi) / 2;
  }
  function critical(alpha, tails, v) { return tInv(1 - alpha / tails, v); }
  function pValue(t, tails, v) {
    // tails 2: P(|T| >= |t|); tails 1: P(T >= t)
    return tails === 2 ? 2 * (1 - tCdf(Math.abs(t), v)) : 1 - tCdf(t, v);
  }
  function decide(t, tails, crit) {
    if (t == null || !isFinite(t)) return null;
    return tails === 2 ? Math.abs(t) > crit : t > crit;
  }
  function halfWidth(crit, t) {
    const need = Math.max(4.5, 1.3 * (isFinite(crit) ? crit : 0), t != null && isFinite(t) ? 1.3 * Math.abs(t) : 0);
    return Math.min(16, need);
  }
  const core = { lgamma, betai, normCdf, tPdf, tCdf, tInv, critical, pValue, decide, halfWidth };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting and input ---- */
  function n3(x) {
    if (!isFinite(x)) return '—';
    let s = (Math.round(x * 1000) / 1000).toFixed(3);
    if (parseFloat(s) === 0) s = '0.000';
    return s.replace('-', MINUS);
  }
  function fmtT(x) { return String(+x.toFixed(3)); }
  function pFmt(p) {
    if (!isFinite(p)) return '—';
    if (p < 0.0005) return 'less than 0.001';
    return p.toFixed(3);
  }
  const ALPHAS = [0.1, 0.05, 0.02, 0.01];
  function parseV(v, warn) {
    if (v == null || String(v).trim() === '') return 9;
    const s = String(v).trim().toLowerCase();
    if (s === 'inf' || s === '∞' || s === 'infinity') return Infinity;
    const n = Number(s);
    if (!isFinite(n) || n < 1 || n > 60 || Math.round(n) !== n) { warn.push('data-v should be a whole number from 1 to 60 or "inf", so 9 is used.'); return 9; }
    return n;
  }
  function parseAlpha(v, warn) {
    if (v == null || String(v).trim() === '') return 0.05;
    const n = Number(String(v).replace('%', ''));
    const a = n > 1 ? n / 100 : n;
    const hit = ALPHAS.find((x) => Math.abs(x - a) < 1e-9);
    if (hit == null) { warn.push('data-alpha should be 0.1, 0.05, 0.02 or 0.01, so 0.05 is used.'); return 0.05; }
    return hit;
  }
  function parseTails(v, warn) {
    if (v == null || String(v).trim() === '') return 2;
    const n = Number(v);
    if (n !== 1 && n !== 2) { warn.push('data-tails should be 1 or 2, so 2 is used.'); return 2; }
    return n;
  }
  function parseT(v, warn) {
    if (v == null || String(v).trim() === '') return null;
    const n = Number(String(v).replace(MINUS, '-'));
    if (!isFinite(n) || n < -50 || n > 50) { warn.push('data-t should be a number from −50 to 50, so no statistic is shown.'); return null; }
    return n;
  }

  W.register('fm-tdist', function (el, o) {
    const warn = [];
    let nu = parseV(o.v, warn);
    let alpha = parseAlpha(o.alpha, warn);
    let tails = parseTails(o.tails, warn);
    let tStat = parseT(o.t, warn);

    const { body } = W.frame(el, 'The t-distribution and its critical region', 'Change the degrees of freedom, the level and the tails; add a test statistic');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const vLabel = (v) => (isFinite(v) ? String(v) : '∞');
    const nuS = W.slider({ label: 'Degrees of freedom ν', min: 1, max: 60, step: 1, value: isFinite(nu) ? nu : 60, fmt: (v) => String(Math.round(Number(v))),
      oninput: (v) => { nu = Math.round(Number(v)); update(); } });
    const infBtn = W.h('button', { type: 'button', class: 'btn btn-sm btn-sec', 'aria-pressed': String(!isFinite(nu)), 'aria-label': 'Infinite degrees of freedom (the normal distribution)' }, '∞');
    infBtn.addEventListener('click', () => {
      if (isFinite(nu)) nu = Infinity; else nu = Math.round(Number(nuS.get()));
      update();
    });
    body.append(nuS.el, W.h('div', { class: 'w-row' }, infBtn));

    function group(label, items, get, set) {
      const g = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': label });
      const btns = items.map(([val, txt]) => {
        const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': String(get() === val) }, txt);
        b.addEventListener('click', () => { set(val); update(); });
        g.append(b);
        return [val, b];
      });
      return { el: g, refresh: () => btns.forEach(([val, b]) => b.setAttribute('aria-pressed', String(get() === val))) };
    }
    const aG = group('Significance level', [[0.1, '10%'], [0.05, '5%'], [0.02, '2%'], [0.01, '1%']], () => alpha, (v) => { alpha = v; });
    const tG = group('Number of tails', [[1, 'One-tailed (upper)'], [2, 'Two-tailed']], () => tails, (v) => { tails = v; });
    body.append(W.h('div', { class: 'w-row' }, aG.el, tG.el));
    const tF = W.field({ label: 'Test statistic t (optional)', type: 'number', step: 0.01, value: tStat == null ? '' : String(tStat), width: '8em',
      oninput: () => {
        const raw = String(tF.input.value).trim();
        const n = Number(raw);
        tStat = raw === '' || !isFinite(n) ? null : Math.max(-50, Math.min(50, n));
        update();
      } });
    body.append(W.h('div', { class: 'w-row' }, tF.el));

    const legend = W.h('div', { class: 'w-note' });
    body.append(legend);
    const cv = W.canvas(body, { height: 300, draw, label: 'The t density against the normal density, with the critical region shaded', describe });
    const R = W.readout([['col', 'MF19 column'], ['crit', 'Critical value'], ['norm', 'Normal critical value'], ['p', 'p-value of the statistic'], ['dec', 'Decision']]);
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, 'Try: set ν = 9, 5%, two-tailed, and type t = 2.0: the t-test does not reject, though a normal test at 1.960 would. Then slide ν up to 60 or press ∞ and watch the two curves, and the two critical values, merge. The p-value is for comparison: the printed table can only bracket it.'));

    function state() {
      const crit = critical(alpha, tails, nu);
      const p = tStat == null ? null : pValue(tStat, tails, nu);
      const dec = decide(tStat, tails, crit);
      return { crit, normCrit: critical(alpha, tails, Infinity), p, dec, col: 1 - alpha / tails };
    }
    function describe() {
      const s = state();
      return `Density of the t-distribution with ${vLabel(nu)} degrees of freedom (solid) and of the normal (dashed). Significance level ${alpha * 100} per cent, ${tails === 1 ? 'one-tailed' : 'two-tailed'}: critical value ${n3(s.crit)}${tails === 2 ? ' and its negative' : ''}, shaded. ${tStat == null ? '' : 'The test statistic ' + n3(tStat) + (s.dec ? ' is in the critical region.' : ' is not in the critical region.')}`;
    }
    function update() {
      const s = state();
      infBtn.setAttribute('aria-pressed', String(!isFinite(nu)));
      if (isFinite(nu)) nuS.set(nu);
      nuS.input.disabled = !isFinite(nu);
      aG.refresh(); tG.refresh();
      legend.textContent = 'Dashed curve: N(0, 1). Solid curve: t with ν = ' + vLabel(nu) + '. Shaded: the critical region' + (tails === 2 ? ', in both tails.' : ', in the upper tail.');
      R.set('col', `p = ${s.col.toFixed(s.col * 1000 % 1 === 0 ? 3 : 4).replace(/0+$/, '').replace(/\.$/, '')} (ν = ${vLabel(nu)})`);
      R.set('crit', (tails === 2 ? '±' : '') + n3(s.crit));
      R.set('norm', (tails === 2 ? '±' : '') + n3(s.normCrit));
      if (tStat == null) { R.set('p', 'type a statistic to see it'); R.set('dec', '—'); }
      else {
        R.set('p', pFmt(s.p));
        const cmp = tails === 2 ? `|t| = ${fmtT(Math.abs(tStat))} ${s.dec ? '>' : '≤'} ${n3(s.crit)}` : `t = ${fmtT(tStat).replace('-', MINUS)} ${s.dec ? '>' : '≤'} ${n3(s.crit)}`;
        R.set('dec', s.dec ? `${cmp}: reject H₀` : `${cmp}: do not reject H₀`);
      }
      cv.redraw();
    }

    /* ---- drawing ---- */
    function draw(ctx, w, h, col) {
      if (!(w > 140 && h > 120)) return;
      const s = state();
      const H = halfWidth(s.crit, tStat);
      if (!(H > 0) || !isFinite(H)) return;
      const view = { x0: -H, x1: H, y0: 0, y1: 0.46 };
      const ax = W.axes(ctx, w, h, view, col, { xlabel: 't', ylabel: 'density', ny: 3, fy: () => '' });
      if (!ax || !ax.X || !ax.Y) return;
      const { X, Y } = ax;
      const left = X(-H), right = X(H), top = Y(0.46), base = Y(0);
      if (!(right > left + 10) || !(base > top + 10)) return;
      ctx.save();
      ctx.beginPath(); ctx.rect(left, top, right - left, base - top + 1); ctx.clip();
      ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      const steps = 260;
      const xs = [];
      for (let i = 0; i <= steps; i++) xs.push(-H + 2 * H * i / steps);
      // shaded critical region on the t curve
      const shade = (a, b) => {
        if (!(b > a)) return;
        ctx.beginPath(); ctx.moveTo(X(a), base);
        const n = 90;
        for (let i = 0; i <= n; i++) { const x = a + (b - a) * i / n; ctx.lineTo(X(x), Y(tPdf(x, nu))); }
        ctx.lineTo(X(b), base); ctx.closePath();
        ctx.globalAlpha = 0.35; ctx.fillStyle = col.red; ctx.fill(); ctx.globalAlpha = 1;
      };
      shade(Math.min(s.crit, H), H);
      if (tails === 2) shade(-H, Math.max(-s.crit, -H));
      // normal curve (dashed)
      ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.8; ctx.setLineDash([6, 4]);
      ctx.beginPath(); xs.forEach((x, i) => { i ? ctx.lineTo(X(x), Y(normPdf(x))) : ctx.moveTo(X(x), Y(normPdf(x))); }); ctx.stroke();
      ctx.setLineDash([]);
      // t curve (solid)
      ctx.strokeStyle = col.sc; ctx.lineWidth = 2.8;
      ctx.beginPath(); xs.forEach((x, i) => { i ? ctx.lineTo(X(x), Y(tPdf(x, nu))) : ctx.moveTo(X(x), Y(tPdf(x, nu))); }); ctx.stroke();
      // critical lines
      ctx.strokeStyle = col.red; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]);
      const critXs = tails === 2 ? [s.crit, -s.crit] : [s.crit];
      critXs.forEach((c) => { if (Math.abs(c) <= H) { ctx.beginPath(); ctx.moveTo(X(c), base); ctx.lineTo(X(c), Y(0.41)); ctx.stroke(); } });
      ctx.setLineDash([]);
      ctx.restore();
      // labels (outside the clip)
      ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic';
      const halo = (txt, x, y, align) => {
        ctx.textAlign = align; ctx.lineWidth = 3; ctx.strokeStyle = col.card; ctx.strokeText(txt, x, y); ctx.fillStyle = col.ink; ctx.fillText(txt, x, y);
      };
      critXs.forEach((c) => {
        if (Math.abs(c) <= H) halo((c < 0 ? MINUS : '') + n3(Math.abs(c)), X(c), Y(0.435), 'center');
        else halo('critical value ' + (c < 0 ? MINUS : '') + n3(Math.abs(c)) + ' is off the scale', c > 0 ? right - 6 : left + 6, Y(0.435), c > 0 ? 'right' : 'left');
      });
      if (tStat != null) {
        const tx = Math.max(-H, Math.min(H, tStat));
        ctx.strokeStyle = col.ink; ctx.lineWidth = 2.2;
        ctx.beginPath(); ctx.moveTo(X(tx), base); ctx.lineTo(X(tx), Y(0.25)); ctx.stroke();
        ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(X(tx), Y(0.25), 4, 0, 2 * Math.PI); ctx.fill();
        const outside = Math.abs(tStat) > H;
        const txt = 't = ' + (tStat < 0 ? MINUS : '') + fmtT(Math.abs(tStat)) + (outside ? ' (off the scale)' : '');
        const half = ctx.measureText(txt).width / 2 + 4;
        halo(txt, Math.max(left + half, Math.min(right - half, X(tx))), Y(0.25) - 9, 'center');
      }
      ctx.textAlign = 'left';
    }

    update();
  });
})();
