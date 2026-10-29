/* widgets/bio-hardy.js: the Hardy-Weinberg calculator and a genetic drift simulation. Used in bio.selection.
   Calculate tab: enter any one of q^2 (recessive phenotype), p^2 (homozygous dominant) or 2pq (heterozygotes) as a frequency (0.04),
   a percentage (4%) or "1 in N"; the widget gives q, p, p^2, 2pq, q^2 with the working. 2pq = f has two solutions (q and p swapped); the smaller q is shown.
   Drift tab: Wright-Fisher model of one gene with two alleles, no selection, random mating, constant population of N diploid individuals.
   Each generation the 2N alleles are a random sample (with replacement) of the 2N alleles of the previous generation. 5 replicate populations,
   50 generations, N = 10, 100 or 1000, starting frequency chosen by the reader (default 0.5); "Run again" uses a new seed.
   Attributes: data-q2 (starting value for the Calculate tab, any format above), data-tab = calc | drift, data-n = 10 | 100 | 1000.
   Pure functions are exported for data/test_bio-hardy.js. */
(function () {
  'use strict';

  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const GENS = 50, REPS = 5;

  // "0.04", "4%", "1 in 2500", "1/2500", "1:2500" -> {f, err}
  function parseFreq(str) {
    let s = String(str == null ? '' : str).trim().toLowerCase().replace(/,/g, '.').replace(/\s+/g, ' ');
    if (!s) return { f: NaN, err: 'Enter a frequency such as 0.04, a percentage such as 4%, or "1 in 2500".' };
    let m = /^1\s*(?:in|:|\/)\s*(\d+(?:\.\d+)?)$/.exec(s);
    if (m) {
      const N = parseFloat(m[1]);
      if (!(N >= 1)) return { f: NaN, err: 'In "1 in N", N must be at least 1.' };
      return { f: 1 / N, err: '' };
    }
    m = /^(\d+(?:\.\d+)?|\.\d+)\s*%$/.exec(s);
    if (m) {
      const f = parseFloat(m[1]) / 100;
      if (f > 1) return { f: NaN, err: 'A percentage must be between 0% and 100%.' };
      return { f: f, err: '' };
    }
    m = /^(\d+(?:\.\d+)?|\.\d+)$/.exec(s);
    if (m) {
      const f = parseFloat(m[1]);
      if (f > 1) return { f: NaN, err: 'A frequency must be between 0 and 1 (use 4% or "1 in 25" for other forms).' };
      return { f: f, err: '' };
    }
    return { f: NaN, err: 'Could not read "' + s.slice(0, 20) + '". Use 0.04, 4% or "1 in 2500".' };
  }

  // known: 'q2' | 'p2' | 'h' (2pq); f in [0,1] -> {p, q, p2, h, q2, work, note, err}
  function solve(known, f) {
    if (!isFinite(f) || f < 0 || f > 1) return { err: 'The frequency must be between 0 and 1.' };
    let q, p, work = [], note = '';
    if (known === 'q2') {
      q = Math.sqrt(f); p = 1 - q;
      work.push('q² = ' + fmt(f) + ', so q = √' + fmt(f) + ' = ' + fmt(q));
      work.push('p = 1 − q = 1 − ' + fmt(q) + ' = ' + fmt(p));
    } else if (known === 'p2') {
      p = Math.sqrt(f); q = 1 - p;
      work.push('p² = ' + fmt(f) + ', so p = √' + fmt(f) + ' = ' + fmt(p));
      work.push('q = 1 − p = 1 − ' + fmt(p) + ' = ' + fmt(q));
    } else {
      if (f > 0.5) return { err: '2pq cannot be more than 0.5, because the largest value of 2pq is when p = q = 0.5.' };
      q = (1 - Math.sqrt(1 - 2 * f)) / 2; p = 1 - q;
      work.push('2pq = ' + fmt(f) + ' with p = 1 − q gives 2q(1 − q) = ' + fmt(f) + ', which is a quadratic in q');
      work.push('q = ' + fmt(q) + ' and p = ' + fmt(p));
      note = 'Two pairs of allele frequencies give this 2pq: p and q can be swapped. The smaller value is shown as q.';
    }
    const p2 = p * p, h = 2 * p * q, q2 = q * q;
    work.push('p² = ' + fmt(p2) + ', 2pq = 2 × ' + fmt(p) + ' × ' + fmt(q) + ' = ' + fmt(h) + ', q² = ' + fmt(q2));
    return { p: p, q: q, p2: p2, h: h, q2: q2, work: work, note: note, err: '' };
  }

  function fmt(x) {
    if (!isFinite(x)) return '?';
    if (x === 0) return '0';
    const a = Math.abs(x);
    if (a < 1e-4) return x.toExponential(2).replace('e-', ' × 10⁻').replace(/\+/, '');
    return String(parseFloat(x.toPrecision(3)));
  }

  // one allele with frequency p0 in a population of n diploid individuals (2n alleles): GENS generations, REPS replicates
  function drift(n, p0, gens, reps, rand) {
    const out = [], twoN = 2 * n;
    for (let r = 0; r < reps; r++) {
      let k = Math.round(p0 * twoN);
      const line = [k / twoN];
      for (let g = 1; g <= gens; g++) {
        const pf = k / twoN;
        if (k === 0 || k === twoN) { line.push(pf); continue; }
        let c = 0;
        for (let i = 0; i < twoN; i++) if (rand() < pf) c++;
        k = c; line.push(k / twoN);
      }
      out.push(line);
    }
    return out;
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { parseFreq: parseFreq, solve: solve, drift: drift, fmt: fmt, clamp: clamp, GENS: GENS, REPS: REPS };
  if (typeof W === 'undefined') return;

  W.register('bio-hardy', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Hardy–Weinberg and genetic drift', 'Allele and genotype frequencies in a population');
    const S = {
      tab: opts.tab === 'drift' ? 'drift' : 'calc',
      known: 'q2', text: '0.04', N: 10000,
      n: [10, 100, 1000].indexOf(parseInt(opts.n, 10)) >= 0 ? parseInt(opts.n, 10) : 100,
      p0: 0.5, seed: 7, lines: null
    };
    const start = opts.q2 != null ? parseFreq(opts.q2) : null;
    if (start && !start.err) S.text = String(opts.q2).trim();
    const note0 = opts.q2 != null && start && start.err ? 'The value given to this widget could not be used (' + start.err + ') so 0.04 is shown.' : '';

    function tag(ctx, c, txt, x, y, align, color) {
      ctx.save();
      ctx.font = '12px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'View' });
    const bCalc = W.h('button', { type: 'button', class: 'w-tab', text: 'Calculate' });
    const bDrift = W.h('button', { type: 'button', class: 'w-tab', text: 'Drift' });
    tabs.appendChild(bCalc); tabs.appendChild(bDrift);
    body.appendChild(tabs);
    const boxCalc = W.h('div'), boxDrift = W.h('div');
    body.appendChild(boxCalc); body.appendChild(boxDrift);

    // each tab is built the first time it is shown, so a hidden tab never holds a blank canvas
    let res = null, updateCalc = null, runDrift = null, setNPressed = null, builtCalc = false, builtDrift = false;

    // ------------------------------------------------------------------ Calculate
    function buildCalc() {
    const selId = W.uid('hwk'), txtId = W.uid('hwv'), nId = W.uid('hwn');
    const sel = W.h('select', { id: selId }, W.h('option', { value: 'q2', text: 'q² (recessive phenotype, aa)' }),
      W.h('option', { value: 'p2', text: 'p² (homozygous dominant, AA)' }), W.h('option', { value: 'h', text: '2pq (heterozygotes, Aa)' }));
    const txt = W.h('input', { id: txtId, type: 'text', value: S.text, autocomplete: 'off', style: { width: '9em' } });
    const nIn = W.h('input', { id: nId, type: 'number', min: '1', max: '100000000', step: '1', value: String(S.N), style: { width: '8em' } });
    boxCalc.appendChild(W.h('div', { class: 'w-row' },
      W.h('div', { class: 'w-ctl' }, W.h('label', { class: 'w-lab', for: selId, text: 'You know' }), sel),
      W.h('div', { class: 'w-ctl' }, W.h('label', { class: 'w-lab', for: txtId, text: 'Its value: 0.04, 4% or 1 in 2500' }), txt),
      W.h('div', { class: 'w-ctl' }, W.h('label', { class: 'w-lab', for: nId, text: 'Population size (for numbers of people)' }), nIn)));
    const err = W.h('div', { class: 'w-err', 'aria-live': 'polite' });
    boxCalc.appendChild(err);
    if (note0) boxCalc.appendChild(W.h('div', { class: 'w-note', text: note0 }));

    function describeCalc() {
      if (!res) return 'No graph: enter a valid frequency.';
      return 'Bar chart of the three genotype frequencies. AA ' + fmt(res.p2) + ', Aa ' + fmt(res.h) + ', aa ' + fmt(res.q2) + '.';
    }
    function drawCalc(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 160 || h < 100) return;
      if (!res) { tag(ctx, c, 'Enter a frequency between 0 and 1', w / 2, h / 2, 'center', c.ink2); return; }
      const L = 46, R = 12, T = 34, Bt = 44;
      const Y = v => T + (1 - v) * (h - T - Bt);
      ctx.save();
      ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      [0, 0.25, 0.5, 0.75, 1].forEach(function (v) {
        ctx.beginPath(); ctx.moveTo(L, Y(v)); ctx.lineTo(w - R, Y(v)); ctx.stroke();
        ctx.fillText(String(v), L - 5, Y(v));
      });
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(L, T - 4); ctx.lineTo(L, h - Bt); ctx.lineTo(w - R, h - Bt); ctx.stroke();
      ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText('frequency', L + 6, 12);
      ctx.restore();
      const bars = [['AA', 'p²', res.p2, c.sc], ['Aa', '2pq', res.h, c.sc2 || c.sc], ['aa', 'q²', res.q2, c.red]];
      const slot = (w - L - R) / 3, bw = Math.min(70, slot * 0.6);
      bars.forEach(function (b, i) {
        const cx = L + slot * (i + 0.5), top = Y(b[2]), bot = Y(0);
        ctx.fillStyle = b[3]; ctx.globalAlpha = 0.8;
        ctx.fillRect(cx - bw / 2, top, bw, Math.max(1, bot - top)); ctx.globalAlpha = 1;
        ctx.strokeStyle = c.ink; ctx.lineWidth = 1.5; ctx.strokeRect(cx - bw / 2, top, bw, Math.max(1, bot - top));
        tag(ctx, c, fmt(b[2]), cx, top - 5, 'center', c.ink);
        tag(ctx, c, b[0], cx, h - Bt + 16, 'center', c.ink);
        tag(ctx, c, b[1], cx, h - Bt + 31, 'center', c.ink2);
      });
    }
    const cvC = W.canvas(boxCalc, {
      height: 220,
      label: 'Bar chart of the three genotype frequencies p squared, 2pq and q squared',
      describe: describeCalc, draw: drawCalc
    });
    const roC = W.readout([['q', 'q (recessive allele, a)'], ['p', 'p (dominant allele, A)'], ['p2', 'p² (AA)'], ['h', '2pq (Aa, carriers)'], ['q2', 'q² (aa)'], ['num', 'Numbers in the population']]);
    boxCalc.appendChild(roC.el);
    const workC = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    boxCalc.appendChild(workC);
    boxCalc.appendChild(W.h('div', { class: 'w-note', text: 'Try it: enter 1 in 2500 as q², then change to 4% and see how few carriers there are compared with the number of people who show the recessive phenotype. The model assumes a large population, random mating, no mutation, no migration and no selection.' }));

    updateCalc = function () {
      const pf = parseFreq(txt.value);
      const nn = Math.max(1, Math.round(parseFloat(nIn.value) || 0));
      res = null;
      let msg = pf.err;
      if (!msg) {
        const r = solve(sel.value, pf.f);
        if (r.err) msg = r.err; else res = r;
      }
      err.textContent = msg;
      if (!res) {
        ['q', 'p', 'p2', 'h', 'q2', 'num'].forEach(function (k) { roC.set(k, '–'); });
        workC.textContent = '';
        cvC.redraw();
        return;
      }
      roC.set('q', fmt(res.q)); roC.set('p', fmt(res.p)); roC.set('p2', fmt(res.p2)); roC.set('h', fmt(res.h)); roC.set('q2', fmt(res.q2));
      const cnt = function (x) { return Math.round(x * nn).toLocaleString('en-GB'); };
      roC.set('num', 'in ' + nn.toLocaleString('en-GB') + ': AA ' + cnt(res.p2) + ', Aa ' + cnt(res.h) + ', aa ' + cnt(res.q2));
      workC.textContent = res.work.join('. ') + '.' + (res.note ? ' ' + res.note : '');
      cvC.redraw();
    };
    sel.addEventListener('change', updateCalc);
    txt.addEventListener('input', updateCalc);
    nIn.addEventListener('input', updateCalc);
    }

    // ------------------------------------------------------------------ Drift
    function buildDrift() {
    const nSel = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Population size' });
    const nBtns = [10, 100, 1000].map(function (v) {
      const b = W.h('button', { type: 'button', class: 'w-tab', text: 'N = ' + v });
      b.addEventListener('click', function () { S.n = v; runDrift(); setNPressed(); b.focus(); });
      nSel.appendChild(b); return b;
    });
    setNPressed = function () { nBtns.forEach(function (b, i) { b.setAttribute('aria-pressed', [10, 100, 1000][i] === S.n ? 'true' : 'false'); }); };
    const sP = W.sliderNum({ label: 'Starting frequency of allele A', min: 0.1, max: 0.9, step: 0.05, value: S.p0,
      oninput: function () { S.p0 = clamp(parseFloat(sP.get()) || 0.5, 0.1, 0.9); runDrift(); } });
    const bRun = W.h('button', { type: 'button', class: 'btn btn-sm', text: 'Run again' });
    bRun.addEventListener('click', function () { S.seed += 1; runDrift(); bRun.focus(); });
    boxDrift.appendChild(W.h('div', { class: 'w-row' }, nSel, bRun));
    boxDrift.appendChild(W.h('div', { class: 'w-row' }, sP.el));

    function describeDrift() {
      if (!S.lines) return 'No graph yet.';
      const fixed = S.lines.filter(function (l) { return l[GENS] === 0 || l[GENS] === 1; }).length;
      return 'Graph of the frequency of allele A in ' + REPS + ' populations of ' + S.n + ' individuals over ' + GENS + ' generations, all starting at ' + S.p0 + '. ' +
        fixed + ' of the ' + REPS + ' populations have lost or fixed the allele by generation ' + GENS + '.';
    }
    function drawDrift(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 180 || h < 120 || !S.lines) return;
      const L = 46, R = 12, T = 18, Bt = 34;
      const X = g => L + g / GENS * (w - L - R), Y = v => T + (1 - v) * (h - T - Bt);
      ctx.save();
      ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      [0, 0.25, 0.5, 0.75, 1].forEach(function (v) {
        ctx.beginPath(); ctx.moveTo(L, Y(v)); ctx.lineTo(w - R, Y(v)); ctx.stroke();
        ctx.fillText(String(v), L - 5, Y(v));
      });
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      [0, 10, 20, 30, 40, 50].forEach(function (g) {
        ctx.beginPath(); ctx.moveTo(X(g), T); ctx.lineTo(X(g), h - Bt); ctx.stroke();
        ctx.fillText(String(g), X(g), h - Bt + 5);
      });
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(L, T - 4); ctx.lineTo(L, h - Bt); ctx.lineTo(w - R, h - Bt); ctx.stroke();
      ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText('frequency of allele A', L + 6, T - 4);
      ctx.textAlign = 'right';
      ctx.fillText('generation', w - R, h - 4);
      ctx.restore();
      const pal = (W.palette ? W.palette(el).series : null) || [c.sc, c.sc2 || c.sc, c.red, c.ok || c.sc, c.ink2];
      ctx.save();
      ctx.beginPath(); ctx.rect(L, T - 2, w - L - R, h - T - Bt + 4); ctx.clip();
      S.lines.forEach(function (line, i) {
        ctx.strokeStyle = pal[i % pal.length]; ctx.lineWidth = 2; ctx.lineJoin = 'round';
        ctx.beginPath();
        line.forEach(function (v, g) { if (g === 0) ctx.moveTo(X(g), Y(v)); else ctx.lineTo(X(g), Y(v)); });
        ctx.stroke();
        const last = line[GENS];
        if (last === 0 || last === 1) {
          ctx.fillStyle = pal[i % pal.length]; ctx.beginPath(); ctx.arc(X(GENS), Y(last), 4, 0, 2 * Math.PI); ctx.fill();
        }
      });
      ctx.restore();
    }
    const cvD = W.canvas(boxDrift, {
      height: 250,
      label: 'Graph of the frequency of allele A over 50 generations in five populations',
      describe: describeDrift, draw: drawDrift
    });
    const capD = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    boxDrift.appendChild(capD);
    boxDrift.appendChild(W.h('div', { class: 'w-note', text: 'Each line is one population. A dot at the end of a line shows that the allele was lost (frequency 0) or fixed (frequency 1). The model has random mating, no mutation, no migration and no selection: the only thing that changes the frequency is chance (Wright–Fisher sampling of the 2N alleles in each generation). Try N = 10, then N = 1000.' }));

    runDrift = function () {
      const r = W.rng(S.seed * 7919 + S.n);
      S.lines = drift(S.n, S.p0, GENS, REPS, r);
      const fixed = S.lines.filter(function (l) { return l[GENS] === 0 || l[GENS] === 1; }).length;
      const spread = S.lines.map(function (l) { return l[GENS]; });
      capD.textContent = 'N = ' + S.n + ': after ' + GENS + ' generations ' + fixed + ' of the ' + REPS + ' populations have lost or fixed the allele. Final frequencies: ' +
        spread.map(function (v) { return fmt(v); }).join(', ') + '.';
      cvD.redraw();
    };
    }

    // ------------------------------------------------------------------ tabs
    function show(tab) {
      S.tab = tab;
      boxCalc.style.display = tab === 'calc' ? '' : 'none';
      boxDrift.style.display = tab === 'drift' ? '' : 'none';
      bCalc.setAttribute('aria-pressed', tab === 'calc' ? 'true' : 'false');
      bDrift.setAttribute('aria-pressed', tab === 'drift' ? 'true' : 'false');
      if (tab === 'calc') {
        if (!builtCalc) { buildCalc(); builtCalc = true; }
        updateCalc();
      } else {
        if (!builtDrift) { buildDrift(); builtDrift = true; }
        runDrift(); setNPressed();
      }
    }
    bCalc.addEventListener('click', function () { show('calc'); bCalc.focus(); });
    bDrift.addEventListener('click', function () { show('drift'); bDrift.focus(); });
    show(S.tab);
  });
})();
