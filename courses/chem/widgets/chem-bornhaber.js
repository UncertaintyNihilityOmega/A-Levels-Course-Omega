/* widgets/chem-bornhaber.js: a Born–Haber cycle drawn as a level diagram to scale, with every term editable and one term
   found by Hess's law. Attributes: data-compound="NaCl" (NaCl, KCl, MgO, MgCl2, CaO, Na2O, custom), data-unknown="latt"
   (hf, at_m, at_x, ie1, ie2, ea1, ea2, latt). Ionisation energies are the Data section values (generated from FACTS.md);
   the other terms are example data for the worked examples of the chapter, not official values. */
(function () {
  'use strict';

  const IE = {"Na": [494, 4560], "K": [418, 0], "Mg": [736, 1450], "Ca": [590, 1150]};

  const MINUS = '−';
  // example data (kJ mol-1) used in the chapter: edit them to match a question
  // fields: hf, at_m, at_x (per mole of X atoms), ea1, ea2, latt; ie1, ie2 come from IE
  const PRESETS = {
    NaCl: { m: 'Na', x: 'Cl', cm: 1, cx: 1, hf: -411, at_m: 107, at_x: 122, ea1: -349, ea2: 0, latt: -785, ie: 'Na' },
    KCl: { m: 'K', x: 'Cl', cm: 1, cx: 1, hf: -437, at_m: 89, at_x: 122, ea1: -349, ea2: 0, latt: -717, ie: 'K' },
    MgO: { m: 'Mg', x: 'O', cm: 2, cx: 2, hf: -602, at_m: 148, at_x: 249, ea1: -141, ea2: 798, latt: -3842, ie: 'Mg' },
    MgCl2: { m: 'Mg', x: 'Cl', cm: 2, cx: 1, hf: -641, at_m: 148, at_x: 122, ea1: -349, ea2: 0, latt: -2521, ie: 'Mg' },
    CaO: { m: 'Ca', x: 'O', cm: 2, cx: 2, hf: -635, at_m: 178, at_x: 249, ea1: -141, ea2: 798, latt: -3459, ie: 'Ca' },
    Na2O: { m: 'Na', x: 'O', cm: 1, cx: 2, hf: -414, at_m: 107, at_x: 249, ea1: -141, ea2: 798, latt: -2522, ie: 'Na' }
  };
  const ORDER = ['NaCl', 'KCl', 'MgO', 'MgCl2', 'CaO', 'Na2O', 'custom'];
  const UNKNOWNS = ['hf', 'at_m', 'at_x', 'ie1', 'ie2', 'ea1', 'ea2', 'latt'];
  const SUB = { '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄' };
  const SUP = { 1: '', 2: '²', 3: '³' };
  const sub = n => (n > 1 ? String(n).replace(/\d/g, d => SUB[d]) : '');
  const gcd = (a, b) => (b ? gcd(b, a % b) : a);
  const signed = v => (Math.abs(v) < 1e-9 ? '0' : (v < 0 ? MINUS : '+') + (Math.abs(v - Math.round(v)) < 1e-9 ? String(Math.abs(Math.round(v))) : Math.abs(v).toFixed(1)));
  const plain = v => (Math.abs(v - Math.round(v)) < 1e-9 ? String(Math.round(v)) : v.toFixed(1));

  W.register('chem-bornhaber', function (el, opts) {
    const { body } = W.frame(el, 'Born–Haber cycle', 'Edit any value, or choose which term to calculate');
    const msgs = [];
    const err = W.h('div', { class: 'w-err', role: 'status' });

    let key = 'NaCl';
    if (opts.compound !== undefined && opts.compound !== '') {
      const k = ORDER.find(c => c.toLowerCase() === String(opts.compound).toLowerCase());
      if (k) key = k; else msgs.push('data-compound = "' + opts.compound + '" is not one of NaCl, KCl, MgO, MgCl2, CaO, Na2O or custom. Showing NaCl instead.');
    }
    const st = { key, m: 'Na', x: 'Cl', cm: 1, cx: 1, unknown: 'latt', vals: {} };
    if (opts.unknown !== undefined && opts.unknown !== '') {
      if (UNKNOWNS.indexOf(String(opts.unknown)) >= 0) st.unknown = String(opts.unknown);
      else msgs.push('data-unknown must be one of ' + UNKNOWNS.join(', ') + '. Calculating the lattice energy instead.');
    }

    function load(k) {
      const p = PRESETS[k === 'custom' ? 'NaCl' : k];
      st.key = k;
      st.m = k === 'custom' ? 'M' : p.m; st.x = k === 'custom' ? 'X' : p.x;
      st.cm = p.cm; st.cx = p.cx;
      const ie = IE[p.ie] || [0, 0];
      st.vals = { hf: p.hf, at_m: p.at_m, at_x: p.at_x, ie1: ie[0], ie2: ie[1] || 0, ea1: p.ea1, ea2: p.ea2, latt: p.latt };
      if (k === 'custom') { st.vals.ie2 = 1450; st.vals.ea2 = 798; }
    }
    load(st.key);

    // ---- derived structure
    function struct() {
      const g = gcd(st.cm, st.cx);
      const nM = st.cx / g, nX = st.cm / g;
      const formula = st.m + sub(nM) + (st.x.length > 0 ? st.x : '') + sub(nX);
      const terms = [
        { k: 'at_m', mult: nM, name: 'ΔHat(' + st.m + ')', eq: st.m + '(s) → ' + st.m + '(g)' },
        { k: 'at_x', mult: nX, name: 'ΔHat(' + st.x + ')', eq: '½' + st.x + '₂(g) → ' + st.x + '(g)' },
        { k: 'ie1', mult: nM, name: 'IE₁(' + st.m + ')', eq: st.m + '(g) → ' + st.m + '⁺(g) + e⁻' }
      ];
      if (st.cm >= 2) terms.push({ k: 'ie2', mult: nM, name: 'IE₂(' + st.m + ')', eq: st.m + '⁺(g) → ' + st.m + '²⁺(g) + e⁻' });
      terms.push({ k: 'ea1', mult: nX, name: 'EA₁(' + st.x + ')', eq: st.x + '(g) + e⁻ → ' + st.x + '⁻(g)' });
      if (st.cx >= 2) terms.push({ k: 'ea2', mult: nX, name: 'EA₂(' + st.x + ')', eq: st.x + '⁻(g) + e⁻ → ' + st.x + '²⁻(g)' });
      terms.push({ k: 'latt', mult: 1, name: 'ΔHlatt', eq: (nM > 1 ? nM : '') + st.m + SUP[st.cm] + '⁺(g) + ' + (nX > 1 ? nX : '') + st.x + SUP[st.cx] + '⁻(g) → ' + formula + '(s)' });
      const hfEq = (nM > 1 ? nM : '') + st.m + '(s) + ' + (nX === 1 ? '½' : (nX > 2 ? nX / 2 : '')) + st.x + '₂(g) → ' + formula + '(s)';
      return { nM, nX, formula, terms, hfEq };
    }

    // ---- controls
    const sel = W.h('select', { 'aria-label': 'Compound' });
    ORDER.forEach(c => sel.appendChild(W.h('option', { value: c, text: c === 'custom' ? 'custom (choose the charges)' : c.replace(/(\d)/g, d => SUB[d]) })));
    sel.value = st.key;
    const selCm = W.h('select', { 'aria-label': 'Charge on the cation' });
    [1, 2].forEach(c => selCm.appendChild(W.h('option', { value: String(c), text: c + '+' })));
    const selCx = W.h('select', { 'aria-label': 'Charge on the anion' });
    [1, 2].forEach(c => selCx.appendChild(W.h('option', { value: String(c), text: c + '−' })));
    const customBox = W.h('div', { class: 'w-row' },
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Cation charge' }), selCm),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Anion charge' }), selCx));
    const selU = W.h('select', { 'aria-label': 'Term to calculate' });
    const selWrap = W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Calculate this term' }), selU);
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Compound' }), sel), selWrap));
    body.appendChild(customBox);

    const fields = {};
    const fieldRow = W.h('div', { class: 'w-row' });
    body.appendChild(fieldRow);
    const FNAMES = { hf: 'ΔHf', at_m: 'ΔHat(metal)', at_x: 'ΔHat(non-metal), per mole of atoms', ie1: 'IE₁', ie2: 'IE₂', ea1: 'EA₁', ea2: 'EA₂', latt: 'ΔHlatt' };
    UNKNOWNS.forEach(k => {
      const f = W.field({ label: FNAMES[k] + ' (kJ mol⁻¹)', value: String(st.vals[k]), type: 'number', step: 1, width: '110px', oninput: () => { read(k); update(); } });
      fields[k] = f;
      fieldRow.appendChild(f.el);
    });
    body.appendChild(err);

    function read(k) {                         // read an edited field into the state
      const raw = String(fields[k].input.value).replace(MINUS, '-').trim();
      st.vals[k] = raw === '' ? NaN : Number(raw);
    }

    sel.onchange = () => { load(sel.value); st.unknown = 'latt'; syncFields(); update(); };
    selCm.onchange = () => { st.cm = Number(selCm.value); update(); };
    selCx.onchange = () => { st.cx = Number(selCx.value); update(); };
    selU.onchange = () => { st.unknown = selU.value; update(); };

    function syncFields() {
      UNKNOWNS.forEach(k => { fields[k].input.value = String(st.vals[k]); });
    }

    // ---- canvas
    const geo = {};
    const cvs = W.canvas(body, {
      height: 360,
      draw(ctx, w, h, col) {
        if (!(w > 120 && h > 120)) return;
        const S = geo.S;
        ctx.textBaseline = 'alphabetic'; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
        if (!S) {
          ctx.font = '13px ' + col.font; ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
          ctx.fillText('Enter a number in every white box.', w / 2, h / 2);
          return;
        }
        const halo = (s, x, y, align, color) => {
          ctx.textAlign = align || 'left'; ctx.lineWidth = 4; ctx.strokeStyle = col.card; ctx.strokeText(s, x, y);
          ctx.fillStyle = color || col.ink; ctx.fillText(s, x, y);
        };
        const nLev = S.levels.length, nArr = S.steps.length + 1;
        let fs = 12; ctx.font = fs + 'px ' + col.font;
        const maxLab = () => Math.max.apply(null, S.levels.map(l => ctx.measureText(l.label).width));
        while (fs > 8 && maxLab() > w * 0.5) { fs -= 1; ctx.font = fs + 'px ' + col.font; }
        const lx = Math.min(w * 0.55, maxLab() + 12);
        const xa0 = lx + 12, dx = Math.max(10, (w - 14 - xa0) / nArr);
        const top = 30, bot = h - 16;
        const emin = Math.min.apply(null, S.levels.map(l => l.E)), emax = Math.max.apply(null, S.levels.map(l => l.E));
        const Y = e => (emax === emin ? (top + bot) / 2 : bot - (bot - top) * (e - emin) / (emax - emin));
        const ax = i => xa0 + i * dx;            // i = 0: formation arrow; i = 1..: the steps
        // label positions, spread so that they do not overlap
        const order = S.levels.map((l, i) => i).sort((a, b) => Y(S.levels[a].E) - Y(S.levels[b].E));
        const ly = {};
        let prev = -1e9;
        order.forEach(i => { const y = Math.max(Y(S.levels[i].E), prev + 15); ly[i] = y; prev = y; });
        let over = ly[order[order.length - 1]] - (h - 6);
        if (over > 0) { let next = h - 6; for (let t = order.length - 1; t >= 0; t--) { ly[order[t]] = Math.min(ly[order[t]], next); next = ly[order[t]] - 15; } }
        // levels: short stubs across the arrows that touch them, with a faint guide to the label
        S.levels.forEach((lv, i) => {
          const touch = [];
          if (i === 0 || i === nLev - 1) touch.push(0);
          if (i >= 1) touch.push(i);               // step i arrives
          if (i <= nLev - 2) touch.push(i + 1);    // step i+1 leaves
          const xs = Math.min.apply(null, touch.map(ax)) - 6, xe = Math.max.apply(null, touch.map(ax)) + 6;
          const y = Y(lv.E);
          ctx.strokeStyle = col.rule2 || col.rule; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
          ctx.beginPath(); ctx.moveTo(lx - 2, ly[i] - 4); ctx.lineTo(xs, y); ctx.stroke(); ctx.setLineDash([]);
          ctx.strokeStyle = i === nLev - 1 ? col.ink : col.ink; ctx.lineWidth = 3;
          ctx.beginPath(); ctx.moveTo(xs, y); ctx.lineTo(xe, y); ctx.stroke();
          ctx.font = fs + 'px ' + col.font;
          halo(lv.label, lx - 4, ly[i], 'right', col.ink);
        });
        // arrows
        const arrow = (x, y0, y1, color, lw) => {
          ctx.strokeStyle = color; ctx.lineWidth = lw;
          ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y1); ctx.stroke();
          const d = y1 > y0 ? 1 : -1;
          if (Math.abs(y1 - y0) > 10) { ctx.beginPath(); ctx.moveTo(x - 4, y1 - d * 7); ctx.lineTo(x, y1); ctx.lineTo(x + 4, y1 - d * 7); ctx.stroke(); }
        };
        ctx.font = '10px ' + col.font;
        S.steps.forEach((s, i) => {
          const y0 = Y(S.levels[i].E), y1 = Y(S.levels[i + 1].E);
          const color = s.unknown ? col.red : (s.v >= 0 ? col.sc : col.sc2);
          arrow(ax(i + 1), y0, y1, color, s.unknown ? 3 : 2);
          halo(String(i + 1), ax(i + 1) + 3, (y0 + y1) / 2 + 3, 'left', s.unknown ? col.red : col.ink2);
        });
        arrow(ax(0), Y(0), Y(S.levels[nLev - 1].E), S.hfUnknown ? col.red : col.ink2, S.hfUnknown ? 3 : 2);
        halo('f', ax(0) + 3, (Y(0) + Y(S.levels[nLev - 1].E)) / 2 + 3, 'left', S.hfUnknown ? col.red : col.ink2);
        ctx.font = '11px ' + col.font;
        halo('drawn to scale: higher up means more enthalpy', w - 6, 11, 'right', col.ink3);
      }
    });
    cvs.cv.setAttribute('role', 'img');

    const tbl = W.h('table', { style: { width: '100%' } });
    body.appendChild(tbl);
    const sumLine = W.h('div', { class: 'w-note', role: 'status' });
    body.appendChild(sumLine);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Ionisation energies are the Data section values; the other numbers are example data from the chapter, not official values: edit them to match your question. Try MgO (two ionisation energies, and a second electron affinity that is positive), then calculate a different unknown term.' }));

    function update() {
      const s = struct();
      // unknown select options
      const avail = ['hf'].concat(s.terms.map(t => t.k));
      if (avail.indexOf(st.unknown) < 0) st.unknown = 'latt';
      selU.textContent = '';
      avail.forEach(k => selU.appendChild(W.h('option', { value: k, text: FNAMES[k] === 'ΔHat(metal)' ? 'ΔHat(' + st.m + ')' : (k === 'at_x' ? 'ΔHat(' + st.x + ')' : FNAMES[k]) })));
      selU.value = st.unknown;
      customBox.style.display = st.key === 'custom' ? '' : 'none';
      selCm.value = String(st.cm); selCx.value = String(st.cx);
      UNKNOWNS.forEach(k => {
        const used = k === 'hf' || s.terms.some(t => t.k === k);
        fields[k].el.style.display = used ? '' : 'none';
        fields[k].input.disabled = k === st.unknown;
        fields[k].input.setAttribute('aria-label', FNAMES[k] + ' in kilojoules per mole' + (k === st.unknown ? ' (calculated)' : ''));
      });
      // validity of every known value
      const known = ['hf'].concat(s.terms.map(t => t.k)).filter(k => k !== st.unknown);
      const bad = known.filter(k => !isFinite(st.vals[k]));
      err.textContent = msgs.join(' ') + (bad.length ? ' Every white box needs a number (not blank, not text).' : '');
      if (bad.length) {
        geo.S = null; geo.label = 'Born–Haber cycle: waiting for numbers';
        tbl.textContent = ''; sumLine.textContent = '';
        cvs.cv.setAttribute('aria-label', geo.label); cvs.redraw();
        return;
      }
      // solve for the unknown (formation enthalpy = sum of the multiplied terms)
      const mult = {}; s.terms.forEach(t => { mult[t.k] = t.mult; });
      const sumKnown = s.terms.filter(t => t.k !== st.unknown).reduce((a, t) => a + t.mult * st.vals[t.k], 0);
      if (st.unknown === 'hf') st.vals.hf = sumKnown;
      else st.vals[st.unknown] = (st.vals.hf - sumKnown) / mult[st.unknown];
      fields[st.unknown].input.value = plain(st.vals[st.unknown]);
      // levels
      const steps = s.terms.map(t => ({ k: t.k, v: t.mult * st.vals[t.k], unknown: t.k === st.unknown, t }));
      const levels = [];
      let E = 0, mState = 's', xState = 'mol', free = 0, ions = 0, anions = 0;
      const lab = () => {
        const nM = s.nM, nX = s.nX;
        const mp = mState === 's' ? (nM > 1 ? nM : '') + st.m + '(s)' :
          (mState === 'g' ? (nM > 1 ? nM : '') + st.m + '(g)' : (nM > 1 ? nM : '') + st.m + SUP[ions] + '⁺(g)');
        const xp = xState === 'mol' ? (nX === 1 ? '½' : (nX > 2 ? nX / 2 : '')) + st.x + '₂(g)' :
          (xState === 'g' ? (nX > 1 ? nX : '') + st.x + '(g)' : (nX > 1 ? nX : '') + st.x + SUP[anions] + '⁻(g)');
        return mp + (free > 0 ? ' + ' + (free > 1 ? free : '') + 'e⁻' : '') + ' + ' + xp;
      };
      levels.push({ E: 0, label: lab() });
      steps.forEach(stp => {
        E += stp.v;
        if (stp.k === 'at_m') mState = 'g';
        else if (stp.k === 'at_x') xState = 'g';
        else if (stp.k === 'ie1') { mState = 'ion'; ions = 1; free += s.nM; }
        else if (stp.k === 'ie2') { ions = 2; free += s.nM; }
        else if (stp.k === 'ea1') { xState = 'an'; anions = 1; free -= s.nX; }
        else if (stp.k === 'ea2') { anions = 2; free -= s.nX; }
        levels.push({ E, label: stp.k === 'latt' ? s.formula + '(s)' : lab() });
      });
      geo.S = { levels, steps, hfUnknown: st.unknown === 'hf' };
      // table
      tbl.textContent = '';
      const row = (cells, hi, head) => {
        const tr = W.h('tr', {});
        cells.forEach((c, i) => tr.appendChild(W.h(head ? 'th' : 'td', { text: c, style: Object.assign({ textAlign: i === 3 ? 'right' : 'left' }, hi ? { color: 'var(--red)', fontWeight: '700' } : {}) })));
        tbl.appendChild(tr);
      };
      row(['Step', 'Term', 'Change', 'kJ mol⁻¹'], false, true);
      row(['f', 'ΔHf', s.hfEq, signed(st.vals.hf)], st.unknown === 'hf');
      steps.forEach((stp, i) => row([String(i + 1), stp.t.name + (stp.t.mult > 1 ? ' × ' + stp.t.mult : ''), stp.t.eq, signed(stp.v)], stp.unknown));
      const total = steps.reduce((a, x) => a + x.v, 0);
      sumLine.textContent = 'Sum of steps 1 to ' + steps.length + ' = ' + signed(total) + ' kJ mol⁻¹, which equals ΔHf = ' + signed(st.vals.hf) + ' kJ mol⁻¹ (Hess\'s law). The term being calculated is shown in the highlighted row and the thick arrow' + (st.unknown === 'hf' ? '.' : ' (step ' + (steps.findIndex(x => x.unknown) + 1) + ').');
      geo.label = 'Born–Haber cycle for ' + s.formula + ' drawn to scale with ' + steps.length + ' steps; calculated term ' + FNAMES[st.unknown] + ' = ' + signed(st.vals[st.unknown]) + ' kilojoules per mole';
      cvs.cv.setAttribute('aria-label', geo.label);
      cvs.redraw();
    }
    update();
  });
})();
