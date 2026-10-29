/* widgets/bio-ttest.js: a t-test for two samples. Used in bio.variation.
   Formula (kit and FACTS.md): t = |mean1 - mean2| / sqrt(s1^2/n1 + s2^2/n2), s with n - 1, df = n1 + n2 - 2,
   critical value at p = 0.05 (two-tailed) from the table of FACTS.md for df 1-30 (for more df the table in the question is used).
   The error bars are mean +/- 2 SE, the syllabus approximation to the 95% confidence interval.
   Attributes: data-a, data-b (numbers separated by commas or spaces); bad or missing values fall back to the example leaf lengths.
   Pure functions are exported for data/test_bio-ttest.js. */
(function () {
  'use strict';

  // t critical values at p = 0.05, two-tailed, df 1-30 (index = df)
  const CRIT = [null, 12.71, 4.30, 3.18, 2.78, 2.57, 2.45, 2.36, 2.31, 2.26, 2.23, 2.20, 2.18, 2.16, 2.14, 2.13, 2.12, 2.11, 2.10, 2.09, 2.09,
    2.08, 2.07, 2.07, 2.06, 2.06, 2.06, 2.05, 2.05, 2.05, 2.04];
  const MAXN = 100;
  const DEF_A = '42, 45, 38, 44, 47, 41, 43, 46';
  const DEF_B = '52, 49, 55, 51, 48, 54, 50, 53';

  // parse "1, 2.5 3" into numbers; returns {vals, err}
  function parseList(str) {
    const s = String(str == null ? '' : str).replace(/−/g, '-');
    const toks = s.split(/[\s,;]+/).filter(function (t) { return t.length > 0; });
    const vals = [];
    for (let i = 0; i < toks.length; i++) {
      if (!/^[-+]?(\d+\.?\d*|\.\d+)(e[-+]?\d+)?$/i.test(toks[i])) return { vals: [], err: '"' + toks[i].slice(0, 12) + '" is not a number. Use numbers separated by commas or spaces.' };
      const x = parseFloat(toks[i]);
      if (!isFinite(x)) return { vals: [], err: 'Use numbers separated by commas or spaces.' };
      vals.push(x);
    }
    if (vals.length < 2) return { vals: vals, err: 'Enter at least 2 numbers.' };
    if (vals.length > MAXN) return { vals: [], err: 'Use at most ' + MAXN + ' numbers in a sample.' };
    return { vals: vals, err: '' };
  }

  function stats(v) {
    const n = v.length;
    let sum = 0;
    for (let i = 0; i < n; i++) sum += v[i];
    const mean = sum / n;
    let ss = 0;
    for (let i = 0; i < n; i++) ss += (v[i] - mean) * (v[i] - mean);
    const s = n > 1 ? Math.sqrt(ss / (n - 1)) : 0;
    return { n: n, mean: mean, ss: ss, s: s, se: s / Math.sqrt(n) };
  }

  // the t-test of two parsed samples
  function ttest(a, b) {
    const A = stats(a), B = stats(b);
    const df = A.n + B.n - 2;
    const den = Math.sqrt(A.s * A.s / A.n + B.s * B.s / B.n);
    let t, nospread = false;
    if (den === 0) { nospread = true; t = A.mean === B.mean ? 0 : Infinity; }
    else t = Math.abs(A.mean - B.mean) / den;
    const crit = df >= 1 && df <= 30 ? CRIT[df] : null;
    let sig = null;
    if (crit !== null && isFinite(t)) sig = t > crit;
    else if (crit !== null && t === Infinity) sig = true;
    const ratio = Math.max(A.s, B.s) > 0 ? Math.max(A.s, B.s) / Math.max(1e-12, Math.min(A.s, B.s)) : 1;
    return { A: A, B: B, df: df, t: t, crit: crit, sig: sig, nospread: nospread, ratio: ratio };
  }

  function fmt(x, sf) {
    if (!isFinite(x)) return x > 0 ? 'infinity' : 'undefined';
    if (x === 0) return '0';
    const a = Math.abs(x);
    if (a >= 1e5 || a < 1e-3) return x.toPrecision(sf || 3);
    return String(parseFloat(x.toPrecision(sf || 3)));
  }

  function conclusion(r) {
    if (r.nospread) return r.t === 0 ? 'Both samples have no spread and the same mean, so t = 0 and there is no difference.' :
      'Every value in each sample is the same, so there is no spread and t cannot be calculated. Add more realistic data.';
    if (r.crit === null) return 'With ' + r.df + ' degrees of freedom the table in this widget does not apply: compare t = ' + fmt(r.t) + ' with the critical value for ' + r.df + ' degrees of freedom in the table given in the question.';
    if (r.sig) return 'The calculated t (' + fmt(r.t) + ') is greater than the critical value (' + fmt(r.crit) + ') at p = 0.05 with ' + r.df + ' degrees of freedom, so reject the null hypothesis: there is a significant difference between the means. The difference is unlikely to be due to chance.';
    return 'The calculated t (' + fmt(r.t) + ') is less than the critical value (' + fmt(r.crit) + ') at p = 0.05 with ' + r.df + ' degrees of freedom, so accept the null hypothesis: there is no significant difference between the means. The difference could be due to chance.';
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { parseList: parseList, stats: stats, ttest: ttest, conclusion: conclusion, fmt: fmt, CRIT: CRIT, DEF_A: DEF_A, DEF_B: DEF_B };
  if (typeof W === 'undefined') return;

  W.register('bio-ttest', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'The t-test', 'Compare the means of two samples');

    let startA = parseList(opts.a), startB = parseList(opts.b);
    let fallbackNote = '';
    if (opts.a != null || opts.b != null) {
      if (startA.err || startB.err) fallbackNote = 'The values given to this widget could not be used (' + (startA.err || startB.err) + ') so the example is shown.';
    }
    const txtA = (opts.a != null && !startA.err && !startB.err) ? String(opts.a) : DEF_A;
    const txtB = (opts.b != null && !startA.err && !startB.err) ? String(opts.b) : DEF_B;

    const idA = W.uid('ttA'), idB = W.uid('ttB');
    function area(id, label, value) {
      const ta = W.h('textarea', { id: id, rows: 2, spellcheck: 'false', style: { width: '100%', minWidth: '0', boxSizing: 'border-box', fontFamily: 'inherit', resize: 'vertical' } });
      ta.value = value;
      const wrap = W.h('div', { class: 'w-ctl', style: { flex: '1 1 220px', minWidth: '0' } },
        W.h('label', { class: 'w-lab', for: id, text: label }), ta);
      return { ta: ta, wrap: wrap };
    }
    const aA = area(idA, 'Sample A: numbers separated by commas or spaces', txtA);
    const aB = area(idB, 'Sample B: numbers separated by commas or spaces', txtB);
    body.appendChild(W.h('div', { class: 'w-row', style: { alignItems: 'flex-start' } }, aA.wrap, aB.wrap));
    const bReset = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset to the example' });
    const bSwap = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Swap A and B' });
    body.appendChild(W.h('div', { class: 'w-row' }, bReset, bSwap));
    const err = W.h('div', { class: 'w-err', 'aria-live': 'polite' });
    body.appendChild(err);
    if (fallbackNote) body.appendChild(W.h('div', { class: 'w-note', text: fallbackNote }));

    let cur = null;   // the latest valid result

    function describe() {
      if (!cur) return 'No graph: enter at least two numbers in each sample.';
      const A = cur.A, B = cur.B;
      return 'Dot plot of two samples. Sample A has ' + A.n + ' values, mean ' + fmt(A.mean) + ', with an error bar of plus or minus 2 standard errors from ' + fmt(A.mean - 2 * A.se) + ' to ' + fmt(A.mean + 2 * A.se) +
        '. Sample B has ' + B.n + ' values, mean ' + fmt(B.mean) + ', from ' + fmt(B.mean - 2 * B.se) + ' to ' + fmt(B.mean + 2 * B.se) + '. ' + (cur.sig === null ? '' : (cur.sig ? 'The means differ significantly.' : 'The means do not differ significantly.'));
    }

    function tag(ctx, c, txt, x, y, align, color) {
      ctx.save();
      ctx.font = '12px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }

    function draw(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0)) return;
      if (w < 160 || h < 120) return;
      if (!cur) { tag(ctx, c, 'Enter at least 2 numbers in each sample', w / 2, h / 2, 'center', c.ink2); return; }
      const A = cur.A, B = cur.B;
      const L = 46, R = 12, T = 14, Bt = 36;
      const all = a_.concat(b_);
      let lo = Math.min(Math.min.apply(null, all), A.mean - 2 * A.se, B.mean - 2 * B.se);
      let hi = Math.max(Math.max.apply(null, all), A.mean + 2 * A.se, B.mean + 2 * B.se);
      if (!(hi > lo)) { lo -= 1; hi += 1; }
      const pad = (hi - lo) * 0.08; lo -= pad; hi += pad;
      const Y = function (v) { return T + (hi - v) / (hi - lo) * (h - T - Bt); };
      const X = function (i) { return L + (i + 0.5) / 2 * (w - L - R); };
      ctx.save();
      ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      const ticks = W.ticks(lo, hi, 5) || [];
      ticks.forEach(function (v) {
        if (v < lo || v > hi) return;
        ctx.beginPath(); ctx.moveTo(L, Y(v)); ctx.lineTo(w - R, Y(v)); ctx.stroke();
        ctx.fillText(fmt(v, 3), L - 5, Y(v));
      });
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(L, T - 4); ctx.lineTo(L, h - Bt); ctx.lineTo(w - R, h - Bt); ctx.stroke();
      ctx.restore();
      [[A, a_, 0, c.sc, 'A'], [B, b_, 1, c.sc2 || c.sc, 'B']].forEach(function (g) {
        const S = g[0], vals = g[1], i = g[2], col = g[3], name = g[4];
        const cx = X(i);
        const half = Math.min(60, (w - L - R) / 4 - 10);
        // individual values as open circles, spread sideways by rank to avoid overlap
        const sorted = vals.slice().sort(function (p, q) { return p - q; });
        sorted.forEach(function (v, k) {
          const dx = ((k % 3) - 1) * 9;
          ctx.beginPath(); ctx.arc(cx + Math.max(-half, Math.min(half, dx)), Y(v), 3.2, 0, 2 * Math.PI);
          ctx.strokeStyle = col; ctx.lineWidth = 1.5; ctx.globalAlpha = 0.65; ctx.stroke(); ctx.globalAlpha = 1;
        });
        // error bar: mean +/- 2 SE
        const yl = Y(S.mean - 2 * S.se), yh = Y(S.mean + 2 * S.se), xb = cx + half + 10 > w - R ? cx + half - 10 : cx + half * 0.55;
        ctx.strokeStyle = c.ink; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(xb, yl); ctx.lineTo(xb, yh); ctx.moveTo(xb - 5, yl); ctx.lineTo(xb + 5, yl); ctx.moveTo(xb - 5, yh); ctx.lineTo(xb + 5, yh); ctx.stroke();
        ctx.beginPath(); ctx.arc(xb, Y(S.mean), 5, 0, 2 * Math.PI); ctx.fillStyle = col; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = c.card; ctx.stroke();
        tag(ctx, c, 'Sample ' + name, cx, h - Bt + 18, 'center', c.ink);
      });
      ctx.save();
      ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.textAlign = 'left';
      ctx.fillText('value', L + 6, T + 4);
      ctx.restore();
    }
    let a_ = [], b_ = [];
    const cv = W.canvas(body, {
      height: 250,
      label: 'Dot plot of the two samples, with the mean of each and an error bar of plus or minus two standard errors',
      describe: describe,
      draw: draw
    });
    body.appendChild(W.h('div', { class: 'w-note', text: 'Open circles are the individual values. The filled dot is the mean and the bar is the mean plus or minus 2 standard errors (the approximate 95% confidence interval).' }));

    const ro = W.readout([['a', 'Sample A: n, mean, s, SE'], ['b', 'Sample B: n, mean, s, SE'], ['t', 't'], ['df', 'Degrees of freedom'], ['c', 'Critical value (p = 0.05)']]);
    body.appendChild(ro.el);
    const concl = W.h('p', { class: 'w-note', 'aria-live': 'polite', style: { fontWeight: '600' } });
    body.appendChild(concl);
    const warn = W.h('div', { class: 'w-note' });
    body.appendChild(warn);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Try it: make sample B much closer to sample A, or widen the spread of one sample, and watch t fall. Null hypothesis: there is no significant difference between the means. The t-test is for continuous, roughly normal data with similar standard deviations.' }));

    function line(S) { return 'n = ' + S.n + ', mean = ' + fmt(S.mean, 4) + ', s = ' + fmt(S.s, 3) + ', SE = ' + fmt(S.se, 3); }

    function update() {
      const pa = parseList(aA.ta.value), pb = parseList(aB.ta.value);
      const msg = pa.err ? 'Sample A: ' + pa.err : (pb.err ? 'Sample B: ' + pb.err : '');
      err.textContent = msg;
      if (msg) {
        cur = null; a_ = []; b_ = [];
        ro.set('a', '–'); ro.set('b', '–'); ro.set('t', '–'); ro.set('df', '–'); ro.set('c', '–');
        concl.textContent = ''; warn.textContent = '';
        cv.redraw();
        return;
      }
      a_ = pa.vals; b_ = pb.vals;
      cur = ttest(a_, b_);
      ro.set('a', line(cur.A)); ro.set('b', line(cur.B));
      ro.set('t', cur.nospread && cur.t === Infinity ? 'cannot be calculated' : fmt(cur.t, 3));
      ro.set('df', cur.df + ' (n₁ + n₂ − 2)');
      ro.set('c', cur.crit !== null ? fmt(cur.crit) + ' (df ' + cur.df + ')' : 'use the table given (df ' + cur.df + ')');
      concl.textContent = conclusion(cur);
      warn.textContent = cur.ratio > 2 && !cur.nospread ? 'Check: the larger standard deviation is more than twice the smaller, so a t-test may not be suitable for these samples.' : '';
      cv.redraw();
    }
    aA.ta.addEventListener('input', update);
    aB.ta.addEventListener('input', update);
    bReset.addEventListener('click', function () { aA.ta.value = txtA; aB.ta.value = txtB; update(); aA.ta.focus(); });
    bSwap.addEventListener('click', function () { const t = aA.ta.value; aA.ta.value = aB.ta.value; aB.ta.value = t; update(); bSwap.focus(); });
    update();
  });
})();
