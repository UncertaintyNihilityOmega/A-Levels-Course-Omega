/* widgets/bio-diversity.js: Simpson's index of diversity, the Lincoln index and Spearman's rank correlation. Used in bio.biodiversity.
   Formulae (FACTS.md): D = 1 - sum (n/N)^2; N = n1 x n2 / m2; rs = 1 - 6 sum D^2 / (n^3 - n), ranks 1 = smallest, ties get the mean rank.
   Attributes: data-mode = simpson | lincoln | spearman (anything else shows simpson).
     simpson: data-a, data-b (counts separated by commas or spaces, up to 10 species); lincoln: data-n1, data-n2, data-m2;
     spearman: data-x, data-y (numbers separated by commas or spaces, 3 to 15 pairs), data-crit (critical value).
   Bad or missing values fall back to the example data with a note. Pure functions are exported for data/test_bio-diversity.js. */
(function () {
  'use strict';

  const MAXSP = 10, MAXPAIRS = 15, MAXCOUNT = 1000000;
  const DEF_SPECIES = ['clover', 'buttercup', 'dandelion', 'plantain', 'yarrow'];
  const DEF_A = [14, 11, 9, 12, 8], DEF_B = [52, 4, 0, 3, 1];
  const DEF_LIN = { n1: 37, n2: 45, m2: 9 };
  const DEF_X = [4.1, 4.5, 4.9, 5.2, 5.2, 5.8, 6.3, 6.6, 7.0, 7.4];
  const DEF_Y = [6, 5, 9, 8, 12, 10, 15, 18, 16, 20];
  const DEF_CRIT = 0.648;

  // ------------------------------------------------------------------ pure functions
  function parseList(str, integer) {
    const s = String(str == null ? '' : str).replace(/−/g, '-');
    const toks = s.split(/[\s,;]+/).filter(function (t) { return t.length > 0; });
    const vals = [];
    for (let i = 0; i < toks.length; i++) {
      if (!/^[-+]?(\d+\.?\d*|\.\d+)$/.test(toks[i])) return { vals: [], err: '"' + toks[i].slice(0, 12) + '" is not a number.' };
      const x = parseFloat(toks[i]);
      if (!isFinite(x) || Math.abs(x) > 1e9) return { vals: [], err: 'A value is too large.' };
      if (integer && (x < 0 || Math.floor(x) !== x)) return { vals: [], err: 'Counts must be whole numbers, 0 or more.' };
      vals.push(x);
    }
    return { vals: vals, err: '' };
  }

  // a count typed in a box: whole number from 0 to MAXCOUNT
  function parseCount(str) {
    const s = String(str == null ? '' : str).trim();
    if (s === '') return { v: NaN, err: 'Enter a whole number, 0 or more.' };
    if (!/^\d+$/.test(s)) return { v: NaN, err: 'Counts must be whole numbers, 0 or more.' };
    const v = parseInt(s, 10);
    if (v > MAXCOUNT) return { v: NaN, err: 'Use counts of at most ' + MAXCOUNT + '.' };
    return { v: v, err: '' };
  }

  // Simpson's index: counts is an array of whole numbers
  function simpsonOf(counts) {
    let N = 0, richness = 0;
    for (let i = 0; i < counts.length; i++) { N += counts[i]; if (counts[i] > 0) richness++; }
    const parts = counts.map(function (n) {
      const frac = N > 0 ? n / N : 0;
      return { n: n, frac: frac, sq: frac * frac };
    });
    let sumsq = 0;
    parts.forEach(function (p) { sumsq += p.sq; });
    return { N: N, richness: richness, parts: parts, sumsq: sumsq, D: N > 0 ? 1 - sumsq : null };
  }

  function simpsonText(s1, s2, name1, name2) {
    if (s1.D === null || s2.D === null) return 'Enter at least one individual at each site to compare them.';
    const dd = s1.D - s2.D;
    if (Math.abs(dd) < 0.0005) return 'The two sites have the same diversity: D is ' + f3(s1.D) + ' at both.' + sizeNote(s1, s2);
    const hi = dd > 0 ? { s: s1, name: name1 } : { s: s2, name: name2 };
    const lo = dd > 0 ? { s: s2, name: name2 } : { s: s1, name: name1 };
    let why;
    if (hi.s.richness === lo.s.richness) why = ' Both sites have ' + hi.s.richness + ' species, so the difference is due to evenness: the individuals are spread more evenly among the species at ' + hi.name + '.';
    else if (hi.s.richness > lo.s.richness) why = ' ' + hi.name + ' has more species (' + hi.s.richness + ' compared with ' + lo.s.richness + '), and D also depends on how evenly the individuals are spread.';
    else why = ' ' + hi.name + ' has fewer species (' + hi.s.richness + ' compared with ' + lo.s.richness + ') but a higher D, because its individuals are spread more evenly: D depends on evenness as well as the number of species.';
    return hi.name + ' has the higher D (' + f3(hi.s.D) + ' compared with ' + f3(lo.s.D) + '), so it is the more diverse site.' + why + sizeNote(s1, s2);
  }

  function sizeNote(s1, s2) {
    const big = Math.max(s1.N, s2.N), small = Math.min(s1.N, s2.N);
    if (small > 0 && big / small > 2) return ' The sample sizes differ by more than a factor of 2, so compare the sites with care.';
    return '';
  }

  // Lincoln index: returns {err} or {N, raw}
  function lincoln(n1, n2, m2) {
    if (![n1, n2, m2].every(function (v) { return isFinite(v) && Math.floor(v) === v && v >= 0; })) return { err: 'Enter whole numbers, 0 or more, in all three boxes.' };
    if (n1 < 1) return { err: 'n₁ must be at least 1: you need to mark some animals first.' };
    if (n2 < 1) return { err: 'n₂ must be at least 1: you need a second sample.' };
    if (m2 === 0) return { err: 'm₂ = 0: no marked animals were recaptured, so the Lincoln index cannot be calculated (dividing by zero). Catch a larger second sample or mark more animals.' };
    if (m2 > n2) return { err: 'm₂ cannot be larger than n₂: the marked animals are part of the second sample.' };
    if (m2 > n1) return { err: 'm₂ cannot be larger than n₁: you can only recapture animals that you marked.' };
    const raw = n1 * n2 / m2;
    return { N: Math.round(raw), raw: raw, share: m2 / n2 };
  }

  function rankList(v) {
    const idx = v.map(function (x, i) { return i; }).sort(function (a, b) { return v[a] - v[b] || a - b; });
    const r = new Array(v.length);
    let i = 0;
    while (i < idx.length) {
      let j = i;
      while (j + 1 < idx.length && v[idx[j + 1]] === v[idx[i]]) j++;
      const mean = (i + j + 2) / 2;       // ranks i+1 .. j+1
      for (let k = i; k <= j; k++) r[idx[k]] = mean;
      i = j + 1;
    }
    return r;
  }

  // Spearman's rank correlation of paired numbers
  function spearman(xs, ys) {
    const n = xs.length;
    if (n !== ys.length) return { err: 'There must be the same number of x and y values.' };
    if (n < 3) return { err: 'Enter at least 3 pairs.' };
    const rx = rankList(xs), ry = rankList(ys);
    const D = rx.map(function (a, i) { return a - ry[i]; });
    const D2 = D.map(function (d) { return d * d; });
    let sumD2 = 0;
    D2.forEach(function (d) { sumD2 += d; });
    const allx = xs.every(function (x) { return x === xs[0]; }), ally = ys.every(function (y) { return y === ys[0]; });
    if (allx || ally) return { err: 'All the ' + (allx ? 'x' : 'y') + ' values are the same, so there is no ranking to correlate.' };
    const denom = n * n * n - n;
    const hasTies = rx.some(function (a, i) { return rx.indexOf(a) !== i; }) || ry.some(function (a, i) { return ry.indexOf(a) !== i; });
    return { n: n, rx: rx, ry: ry, D: D, D2: D2, sumD2: sumD2, denom: denom, rs: 1 - 6 * sumD2 / denom, ties: hasTies };
  }

  function spearmanText(res, crit) {
    if (!res || res.err) return '';
    const rs = res.rs, size = Math.abs(rs);
    const dir = rs > 0 ? 'positive' : (rs < 0 ? 'negative' : 'no');
    let t = 'rₛ = ' + f3(rs) + '. ';
    if (crit === null) return t + 'Enter the critical value you are given for n = ' + res.n + ' pairs to see the conclusion.';
    if (size > crit) t += 'The size of rₛ (' + f3(size) + ') is greater than the critical value (' + f3(crit) + '), so there is a significant ' + dir + ' correlation: reject the null hypothesis. This does not show that one variable causes the other.';
    else t += 'The size of rₛ (' + f3(size) + ') is less than the critical value (' + f3(crit) + '), so the correlation is not significant: accept the null hypothesis that there is no correlation.';
    if (res.n <= 5) t += ' Check: Spearman’s test needs more than 5 pairs.';
    if (res.ties) t += ' Check: tied ranks are given the mean rank; with many ties the formula is only approximate.';
    return t;
  }

  function f3(x) {
    if (x === null || !isFinite(x)) return '–';
    let s = x.toFixed(3);
    if (s === '-0.000') s = '0.000';
    return s.replace('-', '−');
  }
  function fnum(x) {
    if (!isFinite(x)) return '–';
    return String(parseFloat(x.toPrecision(6))).replace('-', '−');
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { parseList: parseList, parseCount: parseCount, simpsonOf: simpsonOf, simpsonText: simpsonText, lincoln: lincoln, rankList: rankList, spearman: spearman, spearmanText: spearmanText, f3: f3, MAXSP: MAXSP, MAXPAIRS: MAXPAIRS };
  }
  if (typeof W === 'undefined') return;

  // ------------------------------------------------------------------ canvas helpers
  function tag(ctx, c, txt, x, y, align, color, size) {
    ctx.save();
    ctx.font = (size || 12) + 'px ' + (c.font || 'sans-serif');
    ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
    ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
    ctx.strokeText(txt, x, y);
    ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y);
    ctx.restore();
  }

  function legendItem(color, text) {
    return W.h('span', { style: { display: 'inline-flex', alignItems: 'center', gap: '6px', marginRight: '14px' } },
      W.h('span', { 'aria-hidden': 'true', style: { display: 'inline-block', width: '12px', height: '12px', background: color, border: '1px solid var(--ink-2)' } }),
      W.h('span', { text: text }));
  }

  function removeBtn(label) {
    return W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', 'aria-label': label, text: '×' });
  }

  W.register('bio-diversity', function (el, opts) {
    opts = opts || {};
    const mode = opts.mode === 'lincoln' || opts.mode === 'spearman' ? opts.mode : 'simpson';
    const titles = {
      simpson: ['Simpson’s index of diversity', 'Compare two sites: D = 1 − Σ(n/N)²'],
      lincoln: ['The Lincoln index', 'Estimate a population size by mark-release-recapture'],
      spearman: ['Spearman’s rank correlation', 'Rank the pairs, find rₛ and compare it with the critical value']
    };
    const { body } = W.frame(el, titles[mode][0], titles[mode][1]);
    const notes = [];
    if (opts.mode != null && opts.mode !== mode) notes.push('The mode given to this widget was not recognised, so the Simpson’s index tool is shown.');
    const err = W.h('div', { class: 'w-err', 'aria-live': 'polite' });

    // ================================================================== SIMPSON
    function buildSimpson() {
      let rows = DEF_SPECIES.map(function (nm, i) { return { name: nm, a: String(DEF_A[i]), b: String(DEF_B[i]) }; });
      let startNote = '';
      if (opts.a != null || opts.b != null) {
        const pa = parseList(opts.a, true), pb = parseList(opts.b, true);
        if (pa.err || pb.err || pa.vals.length === 0 || pa.vals.length !== pb.vals.length || pa.vals.length > MAXSP) {
          startNote = 'The counts given to this widget could not be used (give the same number, 1 to ' + MAXSP + ', of whole numbers for each site), so the example is shown.';
        } else rows = pa.vals.map(function (v, i) { return { name: 'species ' + (i + 1), a: String(v), b: String(pb.vals[i]) }; });
      }
      if (startNote) notes.push(startNote);
      const names = { a: 'Meadow', b: 'Lawn' };
      const idA = W.uid('dvA'), idB = W.uid('dvB');
      const inA = W.h('input', { id: idA, type: 'text', value: names.a, maxlength: '20', autocomplete: 'off', style: { width: '9em' } });
      const inB = W.h('input', { id: idB, type: 'text', value: names.b, maxlength: '20', autocomplete: 'off', style: { width: '9em' } });
      body.appendChild(W.h('div', { class: 'w-row' },
        W.h('div', { class: 'w-ctl' }, W.h('label', { class: 'w-lab', for: idA, text: 'Name of site 1' }), inA),
        W.h('div', { class: 'w-ctl' }, W.h('label', { class: 'w-lab', for: idB, text: 'Name of site 2' }), inB)));

      const tbody = W.h('tbody');
      const thA = W.h('th', { scope: 'col' }), thB = W.h('th', { scope: 'col' });
      body.appendChild(W.h('div', { style: { overflowX: 'auto' } },
        W.h('table', { style: { width: '100%' } },
          W.h('thead', null, W.h('tr', null,
            W.h('th', { scope: 'col', text: 'Species' }), thA, thB, W.h('th', { scope: 'col' }, W.h('span', { class: 'sr-only', text: 'Remove' })))),
          tbody)));
      const bAdd = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Add a species' });
      const bReset = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset to the example' });
      body.appendChild(W.h('div', { class: 'w-row' }, bAdd, bReset));
      body.appendChild(err);
      notes.forEach(function (t) { body.appendChild(W.h('div', { class: 'w-note', text: t })); });

      // results table
      const cNa = {}, resTb = W.h('tbody');
      const hA = W.h('th', { scope: 'col' }), hB = W.h('th', { scope: 'col' });
      [['N', 'Individuals, N'], ['S', 'Species (richness)'], ['sum', 'Σ(n/N)²'], ['D', 'D = 1 − Σ(n/N)²']].forEach(function (r) {
        const a = W.h('td'), b = W.h('td');
        cNa[r[0]] = [a, b];
        resTb.appendChild(W.h('tr', null, W.h('th', { scope: 'row', text: r[1] }), a, b));
      });
      body.appendChild(W.h('table', { style: { width: '100%', marginTop: '8px' } },
        W.h('thead', null, W.h('tr', null, W.h('td', { 'aria-hidden': 'true' }), hA, hB)), resTb));
      const concl = W.h('p', { class: 'w-note', 'aria-live': 'polite', style: { fontWeight: '600' } });
      body.appendChild(concl);

      // working for one site
      let which = 0;
      const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Show the working for' });
      const tb0 = W.h('button', { type: 'button', class: 'w-tab' }), tb1 = W.h('button', { type: 'button', class: 'w-tab' });
      tabs.appendChild(tb0); tabs.appendChild(tb1);
      body.appendChild(W.h('div', { class: 'w-lab', text: 'Working, step by step' }));
      body.appendChild(tabs);
      const workBody = W.h('tbody');
      body.appendChild(W.h('div', { style: { overflowX: 'auto' } },
        W.h('table', { style: { width: '100%' } },
          W.h('thead', null, W.h('tr', null, W.h('th', { scope: 'col', text: 'Species' }), W.h('th', { scope: 'col', text: 'n' }), W.h('th', { scope: 'col', text: 'n/N' }), W.h('th', { scope: 'col', text: '(n/N)²' }))),
          workBody)));
      const workSum = W.h('p', { class: 'w-note' });
      body.appendChild(workSum);

      let cur = null;       // {s1, s2, valid}
      function describe() {
        if (!cur || !cur.valid) return 'No graph: enter whole-number counts for each species.';
        return 'Grouped bar chart of the share of individuals, n divided by N, for each of ' + rows.length + ' species at the two sites. ' +
          names.a + ' has D ' + f3(cur.s1.D) + ' and ' + names.b + ' has D ' + f3(cur.s2.D) + '.';
      }
      function draw(ctx, w, h, c) {
        if (!(w > 0) || !(h > 0)) return;
        if (w < 160 || h < 110) return;
        if (!cur || !cur.valid) { tag(ctx, c, 'Enter whole-number counts', w / 2, h / 2, 'center', c.ink2); return; }
        const L = 44, R = 10, T = 22, Bt = 40, k = rows.length;
        const all = cur.s1.parts.concat(cur.s2.parts).map(function (p) { return p.frac; });
        let top = Math.max(0.2, Math.max.apply(null, all));
        top = Math.min(1, Math.ceil(top * 5) / 5);
        const Y = function (v) { return T + (1 - v / top) * (h - T - Bt); };
        ctx.save();
        ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
        ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
        for (let i = 0; i <= 2; i++) {
          const v = top * i / 2;
          ctx.beginPath(); ctx.moveTo(L, Y(v)); ctx.lineTo(w - R, Y(v)); ctx.stroke();
          ctx.fillText(String(parseFloat(v.toFixed(2))), L - 5, Y(v));
        }
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(L, T - 4); ctx.lineTo(L, h - Bt); ctx.lineTo(w - R, h - Bt); ctx.stroke();
        ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
        ctx.fillText('n/N', L + 6, 14);
        ctx.restore();
        const slot = (w - L - R) / k, bw = Math.max(2, Math.min(24, slot * 0.38));
        for (let i = 0; i < k; i++) {
          const cx = L + slot * (i + 0.5);
          [[cur.s1.parts[i].frac, c.sc, -bw], [cur.s2.parts[i].frac, c.sc2 || c.ink2, 0]].forEach(function (b) {
            const y0 = Y(0), y1 = Y(b[0]);
            ctx.fillStyle = b[1]; ctx.globalAlpha = 0.85;
            ctx.fillRect(cx + b[2], y1, bw, Math.max(0, y0 - y1)); ctx.globalAlpha = 1;
            ctx.strokeStyle = c.ink; ctx.lineWidth = 1;
            ctx.strokeRect(cx + b[2], y1, bw, Math.max(0, y0 - y1));
          });
          tag(ctx, c, String(i + 1), cx, h - Bt + 14, 'center', c.ink2, 11);
        }
        tag(ctx, c, 'species number', w - R, h - 4, 'right', c.ink2, 11);
      }
      const cv = W.canvas(body, { height: 230, label: 'Grouped bar chart of n divided by N for each species at the two sites', describe: describe, draw: draw });
      const leg = W.h('div', { class: 'w-note' });
      body.insertBefore(leg, cv.wrap.nextSibling);
      body.appendChild(W.h('div', { class: 'w-note', text: 'Try it: make the counts more equal at one site and watch its D rise towards 1; put almost all the individuals in one species and watch D fall towards 0. D depends on how many species there are and on how evenly the individuals are spread.' }));

      function renderRows(focusIdx, focusWhat) {
        tbody.textContent = '';
        rows.forEach(function (r, i) {
          const nm = W.h('input', { type: 'text', value: r.name, maxlength: '24', autocomplete: 'off', 'aria-label': 'Name of species ' + (i + 1), style: { width: '100%', minWidth: '4.5em' } });
          const ca = W.h('input', { type: 'number', min: '0', step: '1', value: r.a, 'aria-label': 'Species ' + (i + 1) + ' count at site 1', style: { width: '100%', maxWidth: '4.6em', minWidth: '2.8em' } });
          const cb = W.h('input', { type: 'number', min: '0', step: '1', value: r.b, 'aria-label': 'Species ' + (i + 1) + ' count at site 2', style: { width: '100%', maxWidth: '4.6em', minWidth: '2.8em' } });
          const rm = removeBtn('Remove species ' + (i + 1));
          nm.addEventListener('input', function () { r.name = nm.value; calc(); });
          ca.addEventListener('input', function () { r.a = ca.value; calc(); });
          cb.addEventListener('input', function () { r.b = cb.value; calc(); });
          rm.addEventListener('click', function () {
            if (rows.length <= 1) { err.textContent = 'Keep at least one species.'; return; }
            rows.splice(i, 1); renderRows(Math.min(i, rows.length - 1), 'rm'); calc();
          });
          r._el = { nm: nm, rm: rm };
          tbody.appendChild(W.h('tr', null, W.h('td', null, nm), W.h('td', null, ca), W.h('td', null, cb), W.h('td', null, rm)));
        });
        if (focusWhat === 'rm' && rows[focusIdx]) rows[focusIdx]._el.rm.focus();
        if (focusWhat === 'name' && rows[focusIdx]) rows[focusIdx]._el.nm.focus();
      }

      function calc() {
        names.a = (inA.value || '').trim() || 'Site 1';
        names.b = (inB.value || '').trim() || 'Site 2';
        thA.textContent = names.a; thB.textContent = names.b; hA.textContent = names.a; hB.textContent = names.b;
        tb0.textContent = names.a; tb1.textContent = names.b;
        tb0.setAttribute('aria-pressed', String(which === 0)); tb1.setAttribute('aria-pressed', String(which === 1));
        let msg = '';
        const ca = [], cb = [];
        rows.forEach(function (r, i) {
          const pa = parseCount(r.a), pb = parseCount(r.b);
          if (!msg && pa.err) msg = 'Species ' + (i + 1) + ', ' + names.a + ': ' + pa.err;
          if (!msg && pb.err) msg = 'Species ' + (i + 1) + ', ' + names.b + ': ' + pb.err;
          ca.push(pa.v); cb.push(pb.v);
        });
        err.textContent = msg;
        if (msg) {
          cur = { valid: false };
          ['N', 'S', 'sum', 'D'].forEach(function (k) { cNa[k][0].textContent = '–'; cNa[k][1].textContent = '–'; });
          concl.textContent = ''; workBody.textContent = ''; workSum.textContent = '';
          cv.redraw();
          return;
        }
        const s1 = simpsonOf(ca), s2 = simpsonOf(cb);
        cur = { valid: true, s1: s1, s2: s2 };
        [s1, s2].forEach(function (s, j) {
          cNa.N[j].textContent = String(s.N);
          cNa.S[j].textContent = String(s.richness);
          cNa.sum[j].textContent = s.N > 0 ? f3(s.sumsq) : '–';
          cNa.D[j].textContent = s.N > 0 ? f3(s.D) : '–';
        });
        concl.textContent = simpsonText(s1, s2, names.a, names.b);
        const s = which === 0 ? s1 : s2;
        workBody.textContent = '';
        s.parts.forEach(function (p, i) {
          workBody.appendChild(W.h('tr', null, W.h('td', { text: rows[i].name || ('species ' + (i + 1)) }), W.h('td', { text: String(p.n) }),
            W.h('td', { text: s.N > 0 ? f3(p.frac) : '–' }), W.h('td', { text: s.N > 0 ? f3(p.sq) : '–' })));
        });
        workSum.textContent = s.N > 0
          ? (which === 0 ? names.a : names.b) + ': N = ' + s.N + '; Σ(n/N)² = ' + f3(s.sumsq) + '; D = 1 − ' + f3(s.sumsq) + ' = ' + f3(s.D) + '.'
          : 'Enter at least one individual to calculate D.';
        leg.textContent = '';
        leg.appendChild(legendItem('var(--sc)', names.a + ' (left bar)'));
        leg.appendChild(legendItem('var(--sc2)', names.b + ' (right bar)'));
        cv.redraw();
      }

      inA.addEventListener('input', calc); inB.addEventListener('input', calc);
      tb0.addEventListener('click', function () { which = 0; calc(); });
      tb1.addEventListener('click', function () { which = 1; calc(); });
      bAdd.addEventListener('click', function () {
        if (rows.length >= MAXSP) { err.textContent = 'This tool takes up to ' + MAXSP + ' species.'; return; }
        rows.push({ name: 'species ' + (rows.length + 1), a: '0', b: '0' });
        renderRows(rows.length - 1, 'name'); calc();
      });
      bReset.addEventListener('click', function () {
        rows = DEF_SPECIES.map(function (nm, i) { return { name: nm, a: String(DEF_A[i]), b: String(DEF_B[i]) }; });
        inA.value = 'Meadow'; inB.value = 'Lawn';
        renderRows(0, 'name'); calc();
      });
      renderRows(0, null);
      calc();
    }

    // ================================================================== LINCOLN
    function buildLincoln() {
      let start = { n1: DEF_LIN.n1, n2: DEF_LIN.n2, m2: DEF_LIN.m2 };
      if (opts.n1 != null || opts.n2 != null || opts.m2 != null) {
        const a = parseCount(opts.n1), b = parseCount(opts.n2), c = parseCount(opts.m2);
        const test = a.err || b.err || c.err ? { err: 'x' } : lincoln(a.v, b.v, c.v);
        if (test.err) notes.push('The values given to this widget could not be used, so the example is shown.');
        else start = { n1: a.v, n2: b.v, m2: c.v };
      }
      const f1 = W.field({ label: 'n₁: number caught, marked and released', value: start.n1, type: 'number', step: 1, width: '7em', oninput: calc });
      const f2 = W.field({ label: 'n₂: number caught in the second sample', value: start.n2, type: 'number', step: 1, width: '7em', oninput: calc });
      const f3_ = W.field({ label: 'm₂: number of those that were marked', value: start.m2, type: 'number', step: 1, width: '7em', oninput: calc });
      body.appendChild(W.h('div', { class: 'w-row' }, f1.el, f2.el, f3_.el));
      const bReset = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset to the example' });
      body.appendChild(W.h('div', { class: 'w-row' }, bReset));
      body.appendChild(err);
      notes.forEach(function (t) { body.appendChild(W.h('div', { class: 'w-note', text: t })); });

      const ro = W.readout([['N', 'Estimated population, N'], ['work', 'Working'], ['share', 'Share marked in the second sample, m₂ ÷ n₂'], ['tot', 'Share marked in the population, n₁ ÷ N']]);
      body.appendChild(ro.el);
      let cur = null;
      function describe() {
        if (!cur || cur.err) return 'No graph: the Lincoln index cannot be calculated from these values.';
        return 'Two bars. The whole population of about ' + cur.N + ' animals, of which ' + Math.round(cur.n1 / cur.raw * 1000) / 10 + ' percent are marked, and the second sample of ' + cur.n2 + ', of which ' + Math.round(cur.share * 1000) / 10 + ' percent are marked. The two shares are equal, which is the idea behind the formula.';
      }
      function draw(ctx, w, h, c) {
        if (!(w > 0) || !(h > 0)) return;
        if (w < 160 || h < 110) return;
        if (!cur || cur.err) { tag(ctx, c, 'Enter valid numbers to see the bars', w / 2, h / 2, 'center', c.ink2); return; }
        const L = 14, R = 14, bh = 26;
        const bw = w - L - R;
        const bars = [
          ['Whole population: marked share n₁ ÷ N = ' + pct(cur.n1 / cur.raw), cur.n1 / cur.raw, 20],
          ['Second sample: marked share m₂ ÷ n₂ = ' + pct(cur.share), cur.share, 20 + bh + 52]
        ];
        bars.forEach(function (b) {
          const y = b[2] + 14;
          tag(ctx, c, b[0], L, y - 6, 'left', c.ink, 12);
          ctx.fillStyle = c.rule; ctx.globalAlpha = 0.5; ctx.fillRect(L, y, bw, bh); ctx.globalAlpha = 1;
          ctx.fillStyle = c.sc; ctx.fillRect(L, y, Math.max(0, bw * Math.min(1, b[1])), bh);
          ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5; ctx.strokeRect(L, y, bw, bh);
        });
        tag(ctx, c, 'filled part = marked animals (each bar is 100%)', L, h - 8, 'left', c.ink2, 11);
      }
      function pct(v) { return String(Math.round(v * 1000) / 10) + '%'; }
      const cv = W.canvas(body, { height: 200, label: 'Two bars showing that the marked share of the whole population equals the marked share of the second sample', describe: describe, draw: draw });
      body.appendChild(W.h('div', { class: 'w-lab', text: 'The assumptions behind the estimate' }));
      const ul = W.h('ul', { style: { margin: '4px 0 8px 18px', padding: '0' } });
      ['The marked animals mix randomly with the rest of the population.',
        'The population is closed: no births, deaths, immigration or emigration between the samples.',
        'The marks are not lost, and do not harm the animals or make them easier for predators to see.',
        'Every animal has an equal chance of being caught in the second sample.'].forEach(function (t) { ul.appendChild(W.h('li', { text: t })); });
      body.appendChild(ul);
      body.appendChild(W.h('div', { class: 'w-note', text: 'Try it: keep n₁ and n₂ fixed and raise m₂. More marked animals in the second sample means a smaller estimate, because the marked animals must then be a larger share of the population. m₂ is always the divisor.' }));

      function calc() {
        const a = parseCount(f1.input.value), b = parseCount(f2.input.value), c = parseCount(f3_.input.value);
        let r;
        if (a.err || b.err || c.err) r = { err: 'Enter whole numbers, 0 or more, in all three boxes.' };
        else r = lincoln(a.v, b.v, c.v);
        err.textContent = r.err || '';
        if (r.err) {
          cur = { err: r.err };
          ['N', 'work', 'share', 'tot'].forEach(function (k) { ro.set(k, '–'); });
          cv.redraw();
          return;
        }
        cur = { N: r.N, raw: r.raw, share: r.share, n1: a.v, n2: b.v, m2: c.v };
        ro.set('N', String(r.N));
        ro.set('work', a.v + ' × ' + b.v + ' ÷ ' + c.v + ' = ' + fnum(r.raw) + (Math.floor(r.raw) === r.raw ? '' : ', so about ' + r.N));
        ro.set('share', pct(r.share));
        ro.set('tot', pct(a.v / r.raw));
        cv.redraw();
      }
      bReset.addEventListener('click', function () {
        f1.input.value = String(DEF_LIN.n1); f2.input.value = String(DEF_LIN.n2); f3_.input.value = String(DEF_LIN.m2);
        calc(); f1.input.focus();
      });
      calc();
    }

    // ================================================================== SPEARMAN
    function buildSpearman() {
      let pairs = DEF_X.map(function (x, i) { return { x: String(x), y: String(DEF_Y[i]) }; });
      let crit0 = String(DEF_CRIT);
      if (opts.x != null || opts.y != null) {
        const px = parseList(opts.x, false), py = parseList(opts.y, false);
        if (px.err || py.err || px.vals.length !== py.vals.length || px.vals.length < 3 || px.vals.length > MAXPAIRS) {
          notes.push('The values given to this widget could not be used (give the same number, 3 to ' + MAXPAIRS + ', of numbers for x and y), so the example is shown.');
        } else pairs = px.vals.map(function (x, i) { return { x: String(x), y: String(py.vals[i]) }; });
      }
      if (opts.crit != null) {
        const cv0 = parseFloat(opts.crit);
        if (isFinite(cv0) && cv0 > 0 && cv0 <= 1) crit0 = String(cv0); else if (String(opts.crit).trim() !== '') notes.push('The critical value given to this widget could not be used, so the example value is shown.');
      }
      const tbody = W.h('tbody');
      body.appendChild(W.h('div', { style: { overflowX: 'auto' } },
        W.h('table', { style: { width: '100%' } },
          W.h('thead', null, W.h('tr', null, W.h('th', { scope: 'col', text: '#' }), W.h('th', { scope: 'col', text: 'x' }), W.h('th', { scope: 'col', text: 'y' }), W.h('th', { scope: 'col' }, W.h('span', { class: 'sr-only', text: 'Remove' })))),
          tbody)));
      const bAdd = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Add a pair' });
      const bReset = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset to the example' });
      body.appendChild(W.h('div', { class: 'w-row' }, bAdd, bReset));
      const fc = W.field({ label: 'Critical value you are given (p = 0.05)', value: crit0, type: 'number', step: 0.001, width: '8em', oninput: calc });
      body.appendChild(W.h('div', { class: 'w-row' }, fc.el));
      body.appendChild(err);
      notes.forEach(function (t) { body.appendChild(W.h('div', { class: 'w-note', text: t })); });

      let cur = null, curN = 0;
      function describe() {
        if (!cur || cur.err) return 'No graph: enter at least 3 pairs of numbers.';
        return 'Scatter graph of ' + cur.n + ' pairs of x and y values. Spearman’s rank correlation r s is ' + f3(cur.rs) + '.';
      }
      let px = [], py = [];
      function draw(ctx, w, h, c) {
        if (!(w > 0) || !(h > 0)) return;
        if (w < 160 || h < 120) return;
        if (!cur || cur.err) { tag(ctx, c, 'Enter at least 3 pairs of numbers', w / 2, h / 2, 'center', c.ink2); return; }
        const L = 48, R = 14, T = 20, Bt = 34;
        let x0 = Math.min.apply(null, px), x1 = Math.max.apply(null, px), y0 = Math.min.apply(null, py), y1 = Math.max.apply(null, py);
        if (!(x1 > x0)) { x0 -= 1; x1 += 1; } if (!(y1 > y0)) { y0 -= 1; y1 += 1; }
        const padx = (x1 - x0) * 0.08, pady = (y1 - y0) * 0.08;
        x0 -= padx; x1 += padx; y0 -= pady; y1 += pady;
        const X = function (v) { return L + (v - x0) / (x1 - x0) * (w - L - R); };
        const Y = function (v) { return T + (1 - (v - y0) / (y1 - y0)) * (h - T - Bt); };
        ctx.save();
        ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
        ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
        (W.ticks(y0, y1, 4) || []).forEach(function (v) {
          if (v < y0 || v > y1) return;
          ctx.beginPath(); ctx.moveTo(L, Y(v)); ctx.lineTo(w - R, Y(v)); ctx.stroke();
          ctx.fillText(fnum(v), L - 5, Y(v));
        });
        ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        (W.ticks(x0, x1, 5) || []).forEach(function (v) {
          if (v < x0 || v > x1) return;
          ctx.beginPath(); ctx.moveTo(X(v), T); ctx.lineTo(X(v), h - Bt); ctx.stroke();
          ctx.fillText(fnum(v), X(v), h - Bt + 5);
        });
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(L, T - 4); ctx.lineTo(L, h - Bt); ctx.lineTo(w - R, h - Bt); ctx.stroke();
        ctx.restore();
        px.forEach(function (v, i) {
          ctx.beginPath(); ctx.arc(X(v), Y(py[i]), 4.5, 0, 2 * Math.PI);
          ctx.fillStyle = c.sc; ctx.fill(); ctx.lineWidth = 1.5; ctx.strokeStyle = c.card; ctx.stroke();
        });
        tag(ctx, c, 'y', L + 6, 12, 'left', c.ink2, 11);
        tag(ctx, c, 'x', w - R, h - 6, 'right', c.ink2, 11);
      }
      const cv = W.canvas(body, { height: 230, label: 'Scatter graph of the y values against the x values', describe: describe, draw: draw });

      const ro = W.readout([['n', 'Number of pairs, n'], ['s', 'Σ D²'], ['d', 'n³ − n'], ['rs', 'rₛ = 1 − 6ΣD² ÷ (n³ − n)']]);
      body.appendChild(ro.el);
      const concl = W.h('p', { class: 'w-note', 'aria-live': 'polite', style: { fontWeight: '600' } });
      body.appendChild(concl);
      body.appendChild(W.h('div', { class: 'w-lab', text: 'Working: ranks (smallest = 1; tied values share the mean rank)' }));
      const workBody = W.h('tbody');
      body.appendChild(W.h('div', { style: { overflowX: 'auto' } },
        W.h('table', { style: { width: '100%' } },
          W.h('thead', null, W.h('tr', null, ...['x', 'y', 'rank x', 'rank y', 'D', 'D²'].map(function (t) { return W.h('th', { scope: 'col', text: t }); }))),
          workBody)));
      body.appendChild(W.h('div', { class: 'w-note', text: 'Try it: make two x values equal and see them share a rank; reverse the order of the y values and watch rₛ change sign. Always draw the scatter graph first. Null hypothesis: there is no correlation between x and y.' }));

      function renderRows(focusIdx, what) {
        tbody.textContent = '';
        pairs.forEach(function (p, i) {
          const ix = W.h('input', { type: 'number', step: 'any', value: p.x, 'aria-label': 'Pair ' + (i + 1) + ', x value', style: { width: '4.6em' } });
          const iy = W.h('input', { type: 'number', step: 'any', value: p.y, 'aria-label': 'Pair ' + (i + 1) + ', y value', style: { width: '4.6em' } });
          const rm = removeBtn('Remove pair ' + (i + 1));
          ix.addEventListener('input', function () { p.x = ix.value; calc(); });
          iy.addEventListener('input', function () { p.y = iy.value; calc(); });
          rm.addEventListener('click', function () {
            if (pairs.length <= 3) { err.textContent = 'Keep at least 3 pairs.'; return; }
            pairs.splice(i, 1); renderRows(Math.min(i, pairs.length - 1), 'rm'); calc();
          });
          p._el = { ix: ix, rm: rm };
          tbody.appendChild(W.h('tr', null, W.h('td', { text: String(i + 1) }), W.h('td', null, ix), W.h('td', null, iy), W.h('td', null, rm)));
        });
        if (what === 'rm' && pairs[focusIdx]) pairs[focusIdx]._el.rm.focus();
        if (what === 'x' && pairs[focusIdx]) pairs[focusIdx]._el.ix.focus();
      }

      function calc() {
        const xs = [], ys = [];
        let msg = '';
        pairs.forEach(function (p, i) {
          const sx = String(p.x).trim(), sy = String(p.y).trim();
          if (sx === '' && sy === '') return;
          const vx = parseFloat(sx), vy = parseFloat(sy);
          if (sx === '' || sy === '' || !isFinite(vx) || !isFinite(vy)) { if (!msg) msg = 'Pair ' + (i + 1) + ': enter a number for both x and y (or clear both boxes).'; return; }
          xs.push(vx); ys.push(vy);
        });
        if (!msg && xs.length > MAXPAIRS) msg = 'This tool takes up to ' + MAXPAIRS + ' pairs.';
        let res = null;
        if (!msg) { res = spearman(xs, ys); if (res.err) msg = res.err; }
        err.textContent = msg;
        workBody.textContent = '';
        if (msg) {
          cur = { err: msg };
          ['n', 's', 'd', 'rs'].forEach(function (k) { ro.set(k, '–'); });
          concl.textContent = '';
          cv.redraw();
          return;
        }
        cur = res; px = xs; py = ys;
        ro.set('n', String(res.n));
        ro.set('s', fnum(res.sumD2));
        ro.set('d', String(res.denom));
        ro.set('rs', f3(res.rs));
        let crit = null;
        const cs = String(fc.input.value).trim();
        if (cs !== '') {
          const cvv = parseFloat(cs);
          if (!isFinite(cvv) || cvv <= 0 || cvv > 1) { err.textContent = 'The critical value should be a number between 0 and 1.'; }
          else crit = cvv;
        }
        concl.textContent = spearmanText(res, crit);
        for (let i = 0; i < res.n; i++) {
          workBody.appendChild(W.h('tr', null, W.h('td', { text: fnum(xs[i]) }), W.h('td', { text: fnum(ys[i]) }), W.h('td', { text: fnum(res.rx[i]) }),
            W.h('td', { text: fnum(res.ry[i]) }), W.h('td', { text: fnum(res.D[i]) }), W.h('td', { text: fnum(res.D2[i]) })));
        }
        cv.redraw();
      }

      bAdd.addEventListener('click', function () {
        if (pairs.length >= MAXPAIRS) { err.textContent = 'This tool takes up to ' + MAXPAIRS + ' pairs.'; return; }
        pairs.push({ x: '', y: '' });
        renderRows(pairs.length - 1, 'x'); calc();
      });
      bReset.addEventListener('click', function () {
        pairs = DEF_X.map(function (x, i) { return { x: String(x), y: String(DEF_Y[i]) }; });
        fc.input.value = String(DEF_CRIT);
        renderRows(0, 'x'); calc();
      });
      renderRows(0, null);
      calc();
    }

    if (mode === 'lincoln') buildLincoln();
    else if (mode === 'spearman') buildSpearman();
    else buildSimpson();
  });
})();
