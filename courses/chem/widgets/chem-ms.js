/* widgets/chem-ms.js: mass spectrometry tools.
   Tab 1, Molecular ion: type a formula (C, H, N, O, Cl, Br) and see the molecular-ion cluster: M from the lightest isotopes,
   [M+1] from carbon-13 at 1.1 % per carbon atom, and the Cl (3 : 1) and Br (1 : 1) patterns for the [M+2], [M+4] ... peaks.
   Tab 2, Ar from isotopes: up to four isotope masses and abundances, giving the relative atomic mass and a spectrum.
   Attributes: data-formula="C2H5Br"; data-tab="ar" (opens the Ar calculator).
   Simplified: only the molecular-ion region is drawn; other isotopes (2H, 15N, 17O) are ignored. */
(function () {
  'use strict';

  const MASS = { C: 12, H: 1, N: 14, O: 16, Cl: 35, Br: 79 };
  const SUB = { '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9' };
  const SUPS = '⁺';
  const EXAMPLES = ['C2H5Br', 'C2H5Cl', 'CH2Cl2', 'CH2Br2', 'CH2BrCl', 'C3H7Cl', 'C4H10', 'C3H6O', 'C6H14'];
  const PRESETS = {
    chlorine: { label: 'chlorine', rows: [[35, 75.8], [37, 24.2]] },
    magnesium: { label: 'magnesium', rows: [[24, 79], [25, 10], [26, 11]] },
    boron: { label: 'boron', rows: [[10, 20], [11, 80]] },
    neon: { label: 'neon', rows: [[20, 90.5], [21, 0.3], [22, 9.2]] },
    silicon: { label: 'silicon', rows: [[28, 92.2], [29, 4.7], [30, 3.1]] }
  };

  function parseFormula(text) {
    let s = String(text || '').trim();
    s = s.replace(/[₀-₉]/g, c => SUB[c]).replace(/\s+/g, '');
    if (!s) return { err: 'Type a formula such as C2H5Br.' };
    if (s.length > 40) return { err: 'That formula is too long. Try one with fewer atoms.' };
    const counts = { C: 0, H: 0, N: 0, O: 0, Cl: 0, Br: 0 };
    const re = /([A-Z][a-z]?)(\d*)/y;
    let pos = 0;
    while (pos < s.length) {
      re.lastIndex = pos;
      const m = re.exec(s);
      if (!m || m[0] === '') return { err: 'I cannot read "' + s.slice(pos, pos + 6) + '". Use capital letters for the elements, for example C2H5Br.' };
      const sym = m[1];
      if (!(sym in MASS)) return { err: '"' + sym + '" is not allowed here. This tool uses only C, H, N, O, Cl and Br.' };
      const k = m[2] === '' ? 1 : parseInt(m[2], 10);
      if (!(k >= 0 && k <= 99)) return { err: 'Use between 0 and 99 atoms of each element.' };
      counts[sym] += k;
      pos += m[0].length;
    }
    const total = Object.keys(counts).reduce((a, k) => a + counts[k], 0);
    if (total === 0) return { err: 'The formula has no atoms.' };
    if (counts.Cl + counts.Br > 6) return { err: 'Up to six chlorine and bromine atoms in total, please.' };
    if (counts.C > 40) return { err: 'Up to 40 carbon atoms, please.' };
    return { counts: counts };
  }

  function cluster(counts) {
    // polynomial in steps of two mass units
    let poly = [1];
    const mul = (a, b) => {
      const r = new Array(a.length + b.length - 1).fill(0);
      a.forEach((x, i) => b.forEach((y, j) => { r[i + j] += x * y; }));
      return r;
    };
    for (let i = 0; i < counts.Cl; i++) poly = mul(poly, [0.75, 0.25]);
    for (let i = 0; i < counts.Br; i++) poly = mul(poly, [0.5, 0.5]);
    const top = Math.max.apply(null, poly);
    let M = 0;
    Object.keys(counts).forEach(k => { M += MASS[k] * counts[k]; });
    const peaks = [];
    poly.forEach((p, j) => {
      const h = 100 * p / top;
      peaks.push({ mz: M + 2 * j, h: h, kind: 'main', j: j });
      if (counts.C > 0) peaks.push({ mz: M + 2 * j + 1, h: h * 0.011 * counts.C, kind: 'iso', j: j });
    });
    return { M: M, peaks: peaks, nHal: counts.Cl + counts.Br };
  }

  function fmtH(h) { if (!(h > 0)) return '0'; return h >= 99.95 ? '100' : h.toPrecision(3); }
  function fmtAr(x) { return W.fix(x, 1); }

  W.register('chem-ms', function (el, opts) {
    const { body } = W.frame(el, 'Mass spectrum tools', 'Molecular-ion peaks, and Ar from isotope abundances');
    const msgs = [];
    const get = k => (opts[k] === undefined ? '' : String(opts[k]).trim());
    let tab = 'ion';
    if (get('tab')) {
      const t = get('tab').toLowerCase();
      if (t === 'ar') tab = 'ar';
      else if (t !== 'ion') msgs.push('data-tab "' + get('tab').slice(0, 16) + '" is not ar, so the molecular ion tab is shown.');
    }
    let formula = get('formula') || 'C2H5Br';

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const tabIon = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Molecular ion', onclick: () => setTab('ion') });
    const tabAr = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Ar from isotopes', onclick: () => setTab('ar') });
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Tool' }, tabIon, tabAr)));

    // ---- ion tab controls ----
    const ionBox = W.h('div');
    const fField = W.field({ label: 'Formula', value: formula, type: 'text', placeholder: 'C2H5Br', width: '120px', oninput: () => { formula = fField.input.value; update(); } });
    const exSel = W.h('select', { 'aria-label': 'Example formulas' }, W.h('option', { value: '', text: 'choose an example' }));
    EXAMPLES.forEach(x => exSel.appendChild(W.h('option', { value: x, text: x })));
    exSel.addEventListener('change', () => { if (exSel.value) { formula = exSel.value; fField.input.value = formula; exSel.value = ''; update(); } });
    ionBox.appendChild(W.h('div', { class: 'w-row' }, fField.el, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Examples' }), exSel)));
    const ionRead = W.readout([['formula', 'Formula'], ['m', 'M⁺ (lightest isotopes)'], ['peaks', 'Peaks (m/e : height as % of tallest)'], ['carbon', 'Carbon atoms from [M+1]']]);
    ionBox.appendChild(ionRead.el);

    // ---- Ar tab controls ----
    const arBox = W.h('div');
    const preSel = W.h('select', { 'aria-label': 'Example element' });
    Object.keys(PRESETS).forEach(k => preSel.appendChild(W.h('option', { value: k, text: PRESETS[k].label })));
    preSel.appendChild(W.h('option', { value: 'custom', text: 'my own numbers' }));
    arBox.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Element' }), preSel)));
    const massF = [], abF = [];
    for (let i = 0; i < 4; i++) {
      massF.push(W.field({ label: 'Mass ' + (i + 1), value: '', type: 'number', step: 'any', width: '84px', oninput: () => { preSel.value = 'custom'; update(); } }));
      abF.push(W.field({ label: 'Abundance ' + (i + 1), value: '', type: 'number', step: 'any', width: '96px', oninput: () => { preSel.value = 'custom'; update(); } }));
      arBox.appendChild(W.h('div', { class: 'w-row' }, massF[i].el, abF[i].el));
    }
    const arRead = W.readout([['sum', 'Σ(mass × abundance)'], ['tot', 'Σ abundance'], ['ar1', 'Ar (1 d.p.)'], ['ar3', 'Ar (3 s.f.)']]);
    arBox.appendChild(arRead.el);
    function loadPreset(k) {
      const rows = PRESETS[k].rows;
      for (let i = 0; i < 4; i++) {
        massF[i].input.value = rows[i] ? rows[i][0] : '';
        abF[i].input.value = rows[i] ? rows[i][1] : '';
      }
    }
    preSel.addEventListener('change', () => { if (preSel.value !== 'custom') { loadPreset(preSel.value); update(); } });
    loadPreset('chlorine');

    // ---- picture ----
    let scene = { bars: [], xmin: 0, xmax: 1, ymax: 100, ylabel: '' };
    const cvs = W.canvas(body, {
      height: 230,
      draw(ctx, w, h, col) {
        if (!(w > 80 && h > 80)) return;
        const padL = 44, padR = 12, padT = 18, padB = 34;
        const pw = w - padL - padR, ph = h - padT - padB;
        if (!(pw > 20 && ph > 20)) return;
        const sc = scene;
        const X = v => padL + (v - sc.xmin) / (sc.xmax - sc.xmin) * pw;
        const Y = v => padT + ph - v / sc.ymax * ph;
        ctx.textBaseline = 'alphabetic';
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(padL, padT); ctx.lineTo(padL, padT + ph); ctx.lineTo(padL + pw, padT + ph); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.font = '11px ' + col.font; ctx.textAlign = 'right';
        [0, 0.5, 1].forEach(f => {
          const v = f * sc.ymax;
          ctx.fillText(W.fmt(v, 3), padL - 5, Y(v) + 4);
          ctx.strokeStyle = col.rule; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(padL, Y(v)); ctx.lineTo(padL + pw, Y(v)); ctx.stroke();
        });
        ctx.save();
        ctx.translate(12, padT + ph / 2); ctx.rotate(-Math.PI / 2);
        ctx.textAlign = 'center'; ctx.fillText(sc.ylabel, 0, 0);
        ctx.restore();
        ctx.textAlign = 'center';
        ctx.fillText('m/e', padL + pw / 2, h - 4);
        const perUnit = pw / (sc.xmax - sc.xmin);
        const showAll = perUnit >= 26;
        sc.bars.forEach(b => {
          const x = X(b.mz);
          const y = Y(Math.max(0, b.h));
          const yt = b.h > 0 ? Math.min(y, padT + ph - (sc.minBar || 1)) : padT + ph;
          ctx.strokeStyle = b.kind === 'iso' ? col.ink3 : col.sc;
          ctx.lineWidth = 4; ctx.lineCap = 'butt';
          ctx.beginPath(); ctx.moveTo(x, padT + ph); ctx.lineTo(x, yt); ctx.stroke();
          if (sc.valueLabels && b.h > 0 && perUnit >= 13) {
            ctx.fillStyle = col.ink2; ctx.font = '10px ' + col.font; ctx.textAlign = 'center';
            ctx.fillText(fmtH(b.h), x, Math.max(10, yt - 3));
          }
          ctx.fillStyle = col.ink;
          if (b.kind === 'main' || showAll) {
            ctx.font = '11px ' + col.font; ctx.textAlign = 'center';
            ctx.fillText(String(b.mz), x, padT + ph + 14);
          }
        });
      }
    });
    cvs.cv.setAttribute('role', 'img');
    body.appendChild(err);
    ionBox.appendChild(W.h('div', { class: 'w-note', text: 'Simplified: only the molecular-ion region is drawn, and only ¹³C (1.1 % per carbon atom), ³⁵Cl : ³⁷Cl = 3 : 1 and ⁷⁹Br : ⁸¹Br = 1 : 1 are included. Try C2H5Br, then CH2Cl2, then CH2BrCl and compare the patterns.' }));
    arBox.appendChild(W.h('div', { class: 'w-note', text: 'Ar = Σ(mass × abundance) ÷ Σ abundance. Choose an element, then change a number to see how the mean moves towards the more abundant isotope. Abundances can be percentages or relative heights.' }));
    body.appendChild(ionBox);
    body.appendChild(arBox);

    function setTab(t) { tab = t; update(); }

    function updateIon() {
      const p = parseFormula(formula);
      if (p.err) {
        err.textContent = p.err;
        return;
      }
      const c = p.counts;
      const cl = cluster(c);
      const main = cl.peaks.filter(x => x.kind === 'main');
      const lo = cl.M - 1.5, hi = cl.M + 2 * cl.nHal + (c.C > 0 ? 2.5 : 1.5);
      scene = { bars: cl.peaks, xmin: lo, xmax: hi, ymax: 100, ylabel: 'relative abundance / %', minBar: 6, valueLabels: true };
      const f = [];
      ['C', 'H', 'N', 'O', 'Cl', 'Br'].forEach(k => { if (c[k] > 0) f.push(k + (c[k] > 1 ? c[k] : '')); });
      ionRead.set('formula', f.join(''));
      ionRead.set('m', cl.M + (cl.nHal ? ' (all ' + (c.Cl ? '³⁵Cl' : '') + (c.Cl && c.Br ? ' and ' : '') + (c.Br ? '⁷⁹Br' : '') + ')' : ''));
      ionRead.set('peaks', cl.peaks.map(x => x.mz + ' : ' + fmtH(x.h) + (x.kind === 'iso' ? ' ([+1])' : '')).join('; '));
      if (c.C > 0) {
        const m0 = main[0].h, m1 = cl.peaks.find(x => x.kind === 'iso' && x.j === 0).h;
        ionRead.set('carbon', W.fix(100 * m1 / (1.1 * m0), 1) + ' (n = 100 × ' + fmtH(m1) + ' / (1.1 × ' + fmtH(m0) + '))');
      } else ionRead.set('carbon', 'no carbon atoms, so no [M+1] peak');
    }

    function updateAr() {
      const rows = [];
      let bad = '';
      for (let i = 0; i < 4; i++) {
        const ms = massF[i].input.value.trim(), as = abF[i].input.value.trim();
        if (ms === '' && as === '') continue;
        const m = Number(ms), a = Number(as);
        if (ms === '' || as === '' || !isFinite(m) || !isFinite(a)) { bad = 'Row ' + (i + 1) + ' needs both a mass and an abundance.'; continue; }
        if (m <= 0 || a < 0) { bad = 'Row ' + (i + 1) + ': the mass must be above 0 and the abundance cannot be negative.'; continue; }
        rows.push({ m: m, a: a });
      }
      const tot = rows.reduce((s, r) => s + r.a, 0);
      if (!rows.length || !(tot > 0)) {
        err.textContent = bad || 'Enter at least one isotope mass and a positive abundance.';
        scene = { bars: [], xmin: 0, xmax: 1, ymax: 100, ylabel: '' };
        ['sum', 'tot', 'ar1', 'ar3'].forEach(k => arRead.set(k, '–'));
        return;
      }
      err.textContent = bad;
      const sum = rows.reduce((s, r) => s + r.m * r.a, 0);
      const ar = sum / tot;
      arRead.set('sum', W.fmt(sum, 6));
      arRead.set('tot', W.fmt(tot, 6) + (Math.abs(tot - 100) > 0.05 ? ' (used as relative values)' : ''));
      arRead.set('ar1', fmtAr(ar));
      arRead.set('ar3', W.fmt(ar, 3));
      const lo = Math.min.apply(null, rows.map(r => r.m)) - 1.5, hi = Math.max.apply(null, rows.map(r => r.m)) + 1.5;
      const mx0 = Math.max.apply(null, rows.map(r => r.a));
      const mag = Math.pow(10, Math.floor(Math.log10(mx0 > 0 ? mx0 : 1)));
      const mx = Math.ceil(mx0 / mag - 1e-9) * mag;
      scene = { bars: rows.map(r => ({ mz: r.m, h: r.a, kind: 'main' })), xmin: lo, xmax: hi, ymax: mx, ylabel: 'abundance (as entered)' };
    }

    function update() {
      err.textContent = tab === 'ion' ? '' : '';
      tabIon.setAttribute('aria-selected', tab === 'ion' ? 'true' : 'false');
      tabAr.setAttribute('aria-selected', tab === 'ar' ? 'true' : 'false');
      ionBox.style.display = tab === 'ion' ? '' : 'none';
      arBox.style.display = tab === 'ar' ? '' : 'none';
      if (tab === 'ion') updateIon(); else updateAr();
      if (msgs.length && !err.textContent) err.textContent = msgs.join(' ');
      cvs.redraw();
    }
    update();
  });
})();
