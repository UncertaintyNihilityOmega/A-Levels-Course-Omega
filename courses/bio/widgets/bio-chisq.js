/* widgets/bio-chisq.js: a chi-squared working table for genetic crosses. Used in bio.dihybrid.
   Enter the observed counts and the expected ratio (or the expected numbers: they are used as a ratio, so numbers that add up to the total give the same answer).
   Shows class, O, E, O - E, (O - E)^2, (O - E)^2 / E, then chi-squared, df = classes - 1, the critical value at p = 0.05 (df 1 to 10, FACTS.md) and the conclusion in exam wording.
   Attributes: data-obs = "315,108,101,32", data-ratio = "9:3:3:1" (default 1:1:1:1 for the number of classes), data-names = "round yellow,..." (optional class names).
   Pure functions are exported for data/test_bio-chisq.js. */
(function () {
  'use strict';

  const CRIT = [3.84, 5.99, 7.81, 9.49, 11.07, 12.59, 14.07, 15.51, 16.92, 18.31];   // chi-squared at p = 0.05, df 1 to 10
  const MAXCLASSES = 11;

  function numList(s) {
    return String(s == null ? '' : s).split(/[\s,;:\/]+/).filter(function (x) { return x !== ''; });
  }
  // observed counts: whole numbers >= 0; returns {ok, values, msg}
  function parseObs(s) {
    const parts = numList(s);
    if (!parts.length) return { ok: false, msg: 'Type the observed counts, separated by commas (for example 315, 108, 101, 32).' };
    const v = [];
    for (let i = 0; i < parts.length; i++) {
      const x = Number(parts[i]);
      if (!isFinite(x) || parts[i] === '') return { ok: false, msg: '“' + parts[i] + '” is not a number. Use whole numbers separated by commas.' };
      if (x < 0) return { ok: false, msg: 'A count cannot be negative.' };
      if (Math.floor(x) !== x) return { ok: false, msg: 'Counts must be whole numbers (the test uses numbers of individuals, not percentages).' };
      v.push(x);
    }
    if (v.length < 2) return { ok: false, msg: 'Give at least two classes.' };
    if (v.length > MAXCLASSES) return { ok: false, msg: 'This table handles up to ' + MAXCLASSES + ' classes (10 degrees of freedom).' };
    if (v.reduce(function (a, b) { return a + b; }, 0) <= 0) return { ok: false, msg: 'The counts add up to zero. Enter some observed numbers.' };
    return { ok: true, values: v };
  }
  // expected ratio or expected numbers: positive numbers
  function parseRatio(s, n) {
    const parts = numList(s);
    if (!parts.length) { const e = []; for (let i = 0; i < n; i++) e.push(1); return { ok: true, values: e }; }
    const v = [];
    for (let i = 0; i < parts.length; i++) {
      const x = Number(parts[i]);
      if (!isFinite(x)) return { ok: false, msg: '“' + parts[i] + '” is not a number. Write the ratio like 9:3:3:1.' };
      if (x <= 0) return { ok: false, msg: 'Every part of the expected ratio must be greater than zero.' };
      v.push(x);
    }
    if (v.length !== n) return { ok: false, msg: 'There are ' + n + ' observed classes but ' + v.length + ' parts in the expected ratio. They must match.' };
    return { ok: true, values: v };
  }
  function calc(obs, weights) {
    const total = obs.reduce(function (a, b) { return a + b; }, 0), wsum = weights.reduce(function (a, b) { return a + b; }, 0);
    const exp = weights.map(function (w) { return total * w / wsum; });
    const terms = obs.map(function (o, i) { return (o - exp[i]) * (o - exp[i]) / exp[i]; });
    const chi = terms.reduce(function (a, b) { return a + b; }, 0);
    const df = obs.length - 1;
    const crit = CRIT[df - 1];
    return { total: total, exp: exp, terms: terms, chi: chi, df: df, crit: crit, sig: chi > crit + 1e-12, equal: Math.abs(chi - crit) < 1e-12 };
  }
  function num(x) { if (Math.abs(x) >= 1e7) return x.toExponential(2); return Math.abs(x - Math.round(x)) < 1e-9 ? String(Math.round(x)) : String(Math.round(x * 100) / 100); }
  function conclusion(r) {
    const c = r.chi.toFixed(2);
    if (r.sig || r.equal) {
      return 'χ² (' + c + ') is ' + (r.equal ? 'equal to' : 'greater than') + ' the critical value (' + r.crit + ') at p = 0.05 with ' + r.df + ' degrees of freedom. There is a significant difference between the observed and expected numbers: it is unlikely to be due to chance. The null hypothesis is rejected, so the results do not fit the expected ratio.';
    }
    return 'χ² (' + c + ') is less than the critical value (' + r.crit + ') at p = 0.05 with ' + r.df + ' degrees of freedom. There is no significant difference between the observed and expected numbers: any difference is due to chance. The null hypothesis is accepted, so the results fit the expected ratio.';
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { parseObs: parseObs, parseRatio: parseRatio, calc: calc, conclusion: conclusion, CRIT: CRIT, num: num };
  if (typeof W === 'undefined') return;

  W.register('bio-chisq', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Chi-squared test', 'Observed against expected counts, step by step');
    const st = { obs: String(opts.obs || '315, 108, 101, 32'), ratio: String(opts.ratio == null || opts.ratio === '' ? '9:3:3:1' : opts.ratio), names: [] };
    if (typeof opts.names === 'string') st.names = opts.names.split(',').map(function (x) { return x.trim(); });
    let last = null;

    const obsIn = W.h('input', { type: 'text', value: st.obs, 'aria-label': 'Observed counts, separated by commas', style: { width: '100%', maxWidth: '100%', boxSizing: 'border-box' }, inputmode: 'numeric' });
    const ratIn = W.h('input', { type: 'text', value: st.ratio, 'aria-label': 'Expected ratio, for example 9:3:3:1', style: { width: '100%', maxWidth: '100%', boxSizing: 'border-box' } });
    body.appendChild(W.h('div', { class: 'w-row' },
      W.h('label', { class: 'w-ctl', style: { flex: '2 1 11em', minWidth: 0 } }, W.h('span', { class: 'w-lab', text: 'Observed counts' }), obsIn),
      W.h('label', { class: 'w-ctl', style: { flex: '1 1 8em', minWidth: 0 } }, W.h('span', { class: 'w-lab', text: 'Expected ratio' }), ratIn)));
    const err = W.h('div', { class: 'w-err', role: 'status', 'aria-live': 'polite' });
    const out = W.h('div');
    const verdict = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.appendChild(err);
    body.appendChild(out);
    body.appendChild(verdict);

    const cv = W.canvas(body, {
      height: 190, label: 'Bar chart of observed and expected counts',
      describe: function () {
        if (!last) return 'No chart: the inputs are not valid yet.';
        return 'Pairs of bars for each class, observed (O) and expected (E). ' + last.obs.map(function (o, i) { return 'Class ' + (i + 1) + ': O ' + num(o) + ', E ' + num(last.exp[i]); }).join('; ') + '.';
      },
      draw: function (ctx, w, h, c) {
        if (!(w > 0) || !(h > 0) || w < 160 || h < 120) return;
        if (!last) {
          ctx.save(); ctx.font = '13px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
          ctx.fillText('Fix the numbers above to see the bars.', w / 2, h / 2); ctx.restore();
          return;
        }
        const n = last.obs.length, L = 38, R = 8, T = 18, B = 34;
        const pw = w - L - R, ph = h - T - B;
        if (!(pw > 0) || !(ph > 0)) return;
        const ymax = Math.max.apply(null, last.obs.concat(last.exp)) * 1.12 || 1;
        const Y = function (v) { return T + ph - ph * v / ymax; };
        ctx.save();
        ctx.font = '11px ' + (c.font || 'sans-serif');
        ctx.fillStyle = c.ink2; ctx.strokeStyle = c.ink3 || c.ink2; ctx.lineWidth = 1;
        let ticks = [];
        try { ticks = W.ticks(0, ymax, 4); } catch (e) { ticks = [0, ymax]; }
        ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
        ticks.forEach(function (t) {
          if (t < 0 || t > ymax) return;
          ctx.strokeStyle = c.rule; ctx.beginPath(); ctx.moveTo(L, Y(t)); ctx.lineTo(w - R, Y(t)); ctx.stroke();
          ctx.fillStyle = c.ink2; ctx.fillText(num(t), L - 4, Y(t));
        });
        ctx.strokeStyle = c.ink2; ctx.beginPath(); ctx.moveTo(L, T); ctx.lineTo(L, T + ph); ctx.lineTo(w - R, T + ph); ctx.stroke();
        const slot = pw / n, bw = Math.max(4, Math.min(34, slot * 0.38));
        ctx.textAlign = 'center';
        last.obs.forEach(function (o, i) {
          const cx = L + slot * (i + 0.5);
          const e = last.exp[i];
          ctx.fillStyle = c.sc; ctx.fillRect(cx - bw - 1, Y(o), bw, T + ph - Y(o));
          ctx.fillStyle = c.card; ctx.fillRect(cx + 1, Y(e), bw, T + ph - Y(e));
          ctx.strokeStyle = c.ink; ctx.lineWidth = 1.5; ctx.strokeRect(cx + 1, Y(e), bw, T + ph - Y(e));
          ctx.fillStyle = c.ink; ctx.textBaseline = 'bottom';
          ctx.fillText('O', cx - bw / 2 - 1, Y(o) - 2);
          ctx.fillText('E', cx + bw / 2 + 1, Y(e) - 2);
          ctx.textBaseline = 'top'; ctx.fillStyle = c.ink2;
          const nm = (st.names[i] || String(i + 1));
          ctx.fillText(nm.length > Math.max(3, Math.floor(slot / 6)) ? nm.slice(0, Math.max(2, Math.floor(slot / 6) - 1)) + '…' : nm, cx, T + ph + 6);
        });
        ctx.restore();
      }
    });
    body.appendChild(W.h('div', { class: 'w-note', text: 'O = observed, E = expected. Whole numbers only: the test uses counts, not percentages. Type the numbers from a question to check your working, or the tomato counts 275, 98, 79, 28.' }));

    function cell(txt, hdr) { return W.h(hdr ? 'th' : 'td', { style: { padding: '3px 5px', textAlign: hdr ? 'center' : 'right', fontSize: '12px' } }, txt); }

    function update() {
      err.textContent = ''; out.textContent = ''; verdict.textContent = ''; last = null;
      const o = parseObs(obsIn.value);
      if (!o.ok) { err.textContent = o.msg; cv.redraw(); return; }
      const r = parseRatio(ratIn.value, o.values.length);
      if (!r.ok) { err.textContent = r.msg; cv.redraw(); return; }
      const res = calc(o.values, r.values);
      last = { obs: o.values, exp: res.exp };
      const tb = W.h('table', { style: { width: '100%', maxWidth: '100%' } });
      tb.setAttribute('aria-label', 'Chi-squared working table');
      tb.appendChild(W.h('thead', {}, W.h('tr', {}, ['class', 'O', 'E', 'O − E', '(O − E)²', '(O − E)²/E'].map(function (t) { return cell(t, true); }))));
      const tbody = W.h('tbody');
      o.values.forEach(function (ov, i) {
        const d = ov - res.exp[i];
        tbody.appendChild(W.h('tr', {}, [
          W.h('td', { style: { padding: '3px 5px', textAlign: 'left', fontSize: '12px', overflowWrap: 'anywhere' }, text: st.names[i] || ('class ' + (i + 1)) }),
          cell(num(ov)), cell(num(res.exp[i])), cell(num(d)), cell(num(d * d)), cell(res.terms[i].toFixed(3))]));
      });
      tbody.appendChild(W.h('tr', {}, [
        W.h('td', { style: { padding: '3px 5px', textAlign: 'left', fontSize: '12px', fontWeight: '600' }, text: 'total' }),
        cell(num(res.total)), cell(num(res.total)), cell(''), cell(''), W.h('td', { style: { padding: '3px 5px', textAlign: 'right', fontSize: '12px', fontWeight: '600' }, text: res.terms.reduce(function (a, b) { return a + b; }, 0).toFixed(3) })]));
      tb.appendChild(tbody);
      out.appendChild(W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: 0 } }, tb));
      const mk = function (label, val, hi) { const s = W.stat(label, hi); s.set(val); return s.el; };
      const row = W.h('div', { class: 'w-out' }, mk('χ²', res.chi.toFixed(2), true), mk('degrees of freedom', String(res.df)), mk('critical value (p = 0.05)', String(res.crit)));
      out.appendChild(row);
      verdict.textContent = conclusion(res);
      cv.redraw();
    }
    obsIn.addEventListener('input', update);
    ratIn.addEventListener('input', update);
    update();
  });
})();
