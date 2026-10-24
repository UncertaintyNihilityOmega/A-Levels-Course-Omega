/* widgets/chem-nmr.js: ¹H and ¹³C NMR spectra of 13 small molecules.
   Attributes: data-mol="ethanol" (see PRESETS); data-mode="h" or "c".
   Every shift is a typical value inside the Cambridge Data booklet range for that environment (FACTS.md, "Data booklet values"):
   ¹H: alkane 0.9-1.7; next to C=O 2.2-3.0; next to ring 2.3-3.0; next to O or Cl 3.2-4.0; ArH 6.0-9.0; aldehyde 9.3-10.5;
       ROH 0.5-6.0; RCOOH 9.0-13.0.
   ¹³C: alkyl 0-50; next to a ring 25-50; next to C=O 30-65; next to halogen 30-60; next to O 50-70; arene 110-160; ester/acid C=O 160-185; ketone/aldehyde C=O 190-220.
   Splitting follows the n + 1 rule with n = hydrogens on adjacent carbons (O-H hydrogens neither split nor are split). The gap between
   the lines of a multiplet is drawn far wider than in a real spectrum. Line heights in the ¹³C view carry no meaning. */
(function () {
  'use strict';

  // h: signals {g group, d shift, n hydrogens, adj neighbouring H, r booklet range, ex exchangeable, pat override};
  // c: signals {g, d, k carbons, r}; segs: [text, h index, c index (number or array)]
  const PRESETS = {
    ethanol: {
      name: 'ethanol', segs: [['CH₃', 0, 0], ['CH₂', 1, 1], ['OH', 2, null]],
      h: [{ g: 'CH₃', d: 1.2, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'CH₂', d: 3.7, n: 2, adj: 3, r: '3.2–4.0' }, { g: 'O–H', d: 2.6, n: 1, adj: 0, r: '0.5–6.0', ex: true }],
      c: [{ g: 'CH₃', d: 18, k: 1, r: '0–50' }, { g: 'CH₂OH', d: 58, k: 1, r: '50–70' }]
    },
    'propan-1-ol': {
      name: 'propan-1-ol', segs: [['CH₃', 0, 0], ['CH₂', 1, 1], ['CH₂', 2, 2], ['OH', 3, null]],
      h: [{ g: 'CH₃', d: 0.9, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'middle CH₂', d: 1.6, n: 2, adj: 5, r: '0.9–1.7' }, { g: 'CH₂O', d: 3.6, n: 2, adj: 2, r: '3.2–4.0' }, { g: 'O–H', d: 2.5, n: 1, adj: 0, r: '0.5–6.0', ex: true }],
      c: [{ g: 'CH₃', d: 10, k: 1, r: '0–50' }, { g: 'middle CH₂', d: 26, k: 1, r: '0–50' }, { g: 'CH₂OH', d: 64, k: 1, r: '50–70' }]
    },
    'propan-2-ol': {
      name: 'propan-2-ol', segs: [['(', null, null], ['CH₃', 0, 0], [')₂', null, null], ['CH', 1, 1], ['OH', 2, null]],
      h: [{ g: 'two CH₃', d: 1.2, n: 6, adj: 1, r: '0.9–1.7' }, { g: 'CH', d: 3.9, n: 1, adj: 6, r: '3.2–4.0' }, { g: 'O–H', d: 2.4, n: 1, adj: 0, r: '0.5–6.0', ex: true }],
      c: [{ g: 'two CH₃', d: 25, k: 2, r: '0–50' }, { g: 'CHOH', d: 64, k: 1, r: '50–70' }]
    },
    ethanal: {
      name: 'ethanal', segs: [['CH₃', 0, 0], ['CHO', 1, 1]],
      h: [{ g: 'CH₃', d: 2.2, n: 3, adj: 1, r: '2.2–3.0' }, { g: 'CHO', d: 9.8, n: 1, adj: 3, r: '9.3–10.5' }],
      c: [{ g: 'CH₃', d: 31, k: 1, r: '30–65' }, { g: 'CHO', d: 200, k: 1, r: '190–220' }]
    },
    propanone: {
      name: 'propanone', segs: [['(', null, null], ['CH₃', 0, 0], [')₂', null, null], ['CO', null, 1]],
      h: [{ g: 'two CH₃', d: 2.2, n: 6, adj: 0, r: '2.2–3.0' }],
      c: [{ g: 'two CH₃', d: 30, k: 2, r: '30–65' }, { g: 'C=O', d: 205, k: 1, r: '190–220' }]
    },
    butanone: {
      name: 'butanone', segs: [['CH₃', 1, 1], ['CO', null, 3], ['CH₂', 2, 2], ['CH₃', 0, 0]],
      h: [{ g: 'CH₃ of ethyl', d: 1.0, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'CH₃CO', d: 2.2, n: 3, adj: 0, r: '2.2–3.0' }, { g: 'CH₂CO', d: 2.4, n: 2, adj: 3, r: '2.2–3.0' }],
      c: [{ g: 'CH₃ of ethyl', d: 8, k: 1, r: '0–50' }, { g: 'CH₃CO', d: 30, k: 1, r: '30–65' }, { g: 'CH₂', d: 37, k: 1, r: '30–65' }, { g: 'C=O', d: 209, k: 1, r: '190–220' }]
    },
    'ethanoic acid': {
      name: 'ethanoic acid', segs: [['CH₃', 0, 0], ['COOH', 1, 1]],
      h: [{ g: 'CH₃', d: 2.3, n: 3, adj: 0, r: '2.2–3.0' }, { g: 'COOH', d: 11.5, n: 1, adj: 0, r: '9.0–13.0', ex: true }],
      c: [{ g: 'CH₃', d: 30, k: 1, r: '30–65' }, { g: 'COOH', d: 178, k: 1, r: '160–185' }]
    },
    'ethyl ethanoate': {
      name: 'ethyl ethanoate', segs: [['CH₃', 1, 1], ['COO', null, 3], ['CH₂', 2, 2], ['CH₃', 0, 0]],
      h: [{ g: 'CH₃ of ethyl', d: 1.3, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'CH₃CO', d: 2.3, n: 3, adj: 0, r: '2.2–3.0' }, { g: 'OCH₂', d: 3.9, n: 2, adj: 3, r: '3.2–4.0' }],
      c: [{ g: 'CH₃ of ethyl', d: 14, k: 1, r: '0–50' }, { g: 'CH₃CO', d: 30, k: 1, r: '30–65' }, { g: 'OCH₂', d: 60, k: 1, r: '50–70' }, { g: 'C=O', d: 171, k: 1, r: '160–185' }]
    },
    'methyl propanoate': {
      name: 'methyl propanoate', segs: [['CH₃', 0, 0], ['CH₂', 1, 1], ['COO', null, 3], ['CH₃', 2, 2]],
      h: [{ g: 'CH₃ of ethyl', d: 1.1, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'CH₂CO', d: 2.3, n: 2, adj: 3, r: '2.2–3.0' }, { g: 'OCH₃', d: 3.7, n: 3, adj: 0, r: '3.2–4.0' }],
      c: [{ g: 'CH₃ of ethyl', d: 9, k: 1, r: '0–50' }, { g: 'CH₂', d: 31, k: 1, r: '30–65' }, { g: 'OCH₃', d: 52, k: 1, r: '50–70' }, { g: 'C=O', d: 175, k: 1, r: '160–185' }]
    },
    '1-chloropropane': {
      name: '1-chloropropane', segs: [['CH₃', 0, 0], ['CH₂', 1, 1], ['CH₂Cl', 2, 2]],
      h: [{ g: 'CH₃', d: 1.0, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'middle CH₂', d: 1.7, n: 2, adj: 5, r: '0.9–1.7' }, { g: 'CH₂Cl', d: 3.5, n: 2, adj: 2, r: '3.2–4.0' }],
      c: [{ g: 'CH₃', d: 11, k: 1, r: '0–50' }, { g: 'middle CH₂', d: 26, k: 1, r: '0–50' }, { g: 'CH₂Cl', d: 47, k: 1, r: '30–60' }]
    },
    methylbenzene: {
      name: 'methylbenzene', segs: [['C₆H₅', 1, [1, 2, 3, 4]], ['CH₃', 0, 0]],
      h: [{ g: 'CH₃', d: 2.3, n: 3, adj: 0, r: '2.3–3.0' }, { g: 'ring H', d: 7.2, n: 5, adj: 4, r: '6.0–9.0', pat: [1, 2, 3, 2, 1] }],
      c: [{ g: 'CH₃', d: 25, k: 1, r: '25–50' }, { g: 'ring C para to CH₃', d: 125, k: 1, r: '110–160' }, { g: 'ring C meta (two)', d: 128, k: 2, r: '110–160' }, { g: 'ring C ortho (two)', d: 129, k: 2, r: '110–160' }, { g: 'ring C bonded to CH₃', d: 138, k: 1, r: '110–160' }]
    },
    'propanoic acid': {
      name: 'propanoic acid', segs: [['CH₃', 0, 0], ['CH₂', 1, 1], ['COOH', 2, 2]],
      h: [{ g: 'CH₃', d: 1.1, n: 3, adj: 2, r: '0.9–1.7' }, { g: 'CH₂CO', d: 2.4, n: 2, adj: 3, r: '2.2–3.0' }, { g: 'COOH', d: 11.5, n: 1, adj: 0, r: '9.0–13.0', ex: true }],
      c: [{ g: 'CH₃', d: 9, k: 1, r: '0–50' }, { g: 'CH₂', d: 31, k: 1, r: '30–65' }, { g: 'COOH', d: 181, k: 1, r: '160–185' }]
    },
    benzene: {
      name: 'benzene', segs: [['C₆H₆', 0, 0]],
      h: [{ g: 'all six H', d: 7.3, n: 6, adj: 0, r: '6.0–9.0' }],
      c: [{ g: 'all six C', d: 128, k: 6, r: '110–160' }]
    }
  };
  const ORDER = Object.keys(PRESETS);
  const FORMULA = {
    ethanol: 'CH₃CH₂OH', 'propan-1-ol': 'CH₃CH₂CH₂OH', 'propan-2-ol': '(CH₃)₂CHOH', ethanal: 'CH₃CHO', propanone: '(CH₃)₂CO',
    butanone: 'CH₃COCH₂CH₃', 'ethanoic acid': 'CH₃COOH', 'ethyl ethanoate': 'CH₃COOCH₂CH₃', 'methyl propanoate': 'CH₃CH₂COOCH₃',
    '1-chloropropane': 'CH₃CH₂CH₂Cl', methylbenzene: 'C₆H₅CH₃', 'propanoic acid': 'CH₃CH₂COOH', benzene: 'C₆H₆'
  };

  function lineName(adj) {
    return ['singlet', 'doublet', 'triplet', 'quartet'][adj] || 'multiplet';
  }
  function abbr(adj) { return ['s', 'd', 't', 'q'][adj] || 'm'; }
  function pascal(k) {
    const row = [1];
    for (let i = 0; i < k; i++) { const next = [1]; for (let j = 1; j < row.length; j++) next.push(row[j - 1] + row[j]); next.push(1); row.length = 0; next.forEach(v => row.push(v)); }
    return row;
  }
  function pattern(s) { return s.pat ? s.pat : pascal(s.adj); }

  W.register('chem-nmr', function (el, opts) {
    const { body } = W.frame(el, 'NMR spectra', 'Choose a molecule, then look at its ¹H or ¹³C spectrum');
    const msgs = [];
    const get = k => (opts[k] === undefined ? '' : String(opts[k]).trim());
    let mol = 'ethanol';
    if (get('mol')) {
      const m = get('mol').toLowerCase();
      if (PRESETS[m]) mol = m;
      else msgs.push('There is no molecule "' + get('mol').slice(0, 24) + '" in this tool, so ethanol is shown.');
    }
    let mode = 'h';
    if (get('mode')) {
      const m = get('mode').toLowerCase();
      if (m === 'c' || m === 'h') mode = m;
      else msgs.push('data-mode "' + get('mode').slice(0, 12) + '" is not h or c, so the ¹H spectrum is shown.');
    }
    let d2o = false;
    let sel = -1;
    let geom = [];          // pixel x of each drawn signal, for clicking

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const tabH = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: '¹H NMR', onclick: () => { mode = 'h'; sel = -1; update(); } });
    const tabC = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: '¹³C NMR', onclick: () => { mode = 'c'; sel = -1; update(); } });
    const select = W.h('select', { 'aria-label': 'Molecule' });
    ORDER.forEach(k => select.appendChild(W.h('option', { value: k, text: k + '  ' + FORMULA[k] })));
    select.value = mol;
    select.addEventListener('change', () => { mol = select.value; sel = -1; update(); });
    const chk = W.h('input', { type: 'checkbox', 'aria-label': 'Shake with D₂O' });
    chk.addEventListener('change', () => { d2o = chk.checked; sel = -1; update(); });
    const d2oRow = W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, chk, W.h('span', { class: 'w-lab', text: 'shake with D₂O' }));
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Spectrum' }, tabH, tabC),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Molecule' }), select), d2oRow));

    const formulaLine = W.h('div', { style: { fontSize: '1.05em', margin: '4px 0 6px', minHeight: '1.4em' } });
    body.appendChild(formulaLine);

    const cvs = W.canvas(body, {
      height: 250,
      draw(ctx, w, h, col) {
        geom = [];
        if (!(w > 120 && h > 120)) return;
        const padL = 12, padR = 14, padT = 8, padB = 38;
        const pw = w - padL - padR, ph = h - padT - padB;
        if (!(pw > 80 && ph > 80)) return;
        const P = PRESETS[mol];
        const hMode = mode === 'h';
        let sigs = hMode ? P.h.map((s, i) => ({ s: s, i: i })).filter(o => !(d2o && o.s.ex)) : P.c.map((s, i) => ({ s: s, i: i }));
        const top = hMode ? Math.max(8, Math.ceil(Math.max.apply(null, P.h.map(s => s.d)) + 1)) : 220;
        const X = d => padL + (top - d) / top * pw;
        const yAxis = padT + ph;
        ctx.textBaseline = 'alphabetic';
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(padL - 4, yAxis); ctx.lineTo(padL + pw + 6, yAxis); ctx.stroke();
        // ticks
        const step = hMode ? (pw / top >= 26 ? 1 : 2) : 50;
        ctx.fillStyle = col.ink2; ctx.font = '11px ' + col.font; ctx.textAlign = 'center';
        for (let v = 0; v <= top + 1e-9; v += step) {
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(X(v), yAxis); ctx.lineTo(X(v), yAxis + 4); ctx.stroke();
          ctx.fillText(String(v), X(v), yAxis + 16);
        }
        ctx.fillText('δ / ppm', padL + pw / 2, h - 5);
        // labels first (to know how many rows are needed)
        ctx.font = '11px ' + col.font;
        const items = sigs.map(o => {
          const s = o.s;
          const text = hMode ? s.d.toFixed(1) + '  ' + s.n + 'H ' + abbr(s.adj) : String(s.d) + (s.k > 1 ? '  ×' + s.k : '');
          return { o: o, x: X(s.d), text: text, tw: ctx.measureText(text).width };
        }).sort((a, b) => a.x - b.x);
        const rowRight = [];
        items.forEach(it => {
          let r = 0;
          while (rowRight[r] !== undefined && it.x - it.tw / 2 < rowRight[r] + 4) r++;
          rowRight[r] = it.x + it.tw / 2;
          it.row = r;
        });
        const rows = Math.max(1, rowRight.length);
        const labTop = padT + 12;
        const lineBase = yAxis;
        const maxPx = Math.max(24, ph - (rows * 14 + 16));
        // heights
        let unit = 1;
        if (hMode) {
          let mx = 0;
          sigs.forEach(o => { const pat = pattern(o.s), tot = pat.reduce((a, b) => a + b, 0); mx = Math.max(mx, o.s.n * Math.max.apply(null, pat) / tot); });
          unit = mx > 0 ? maxPx * 0.8 / mx : 1;
        }
        const sp = Math.max(3, Math.min(6, pw / 60));
        // TMS
        if (hMode) {
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 2;
          const tx = X(0);
          ctx.beginPath(); ctx.moveTo(tx, lineBase); ctx.lineTo(tx, lineBase - Math.min(maxPx * 0.5, 40)); ctx.stroke();
          ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
          ctx.fillText('TMS', Math.min(tx, padL + pw - 10), lineBase - Math.min(maxPx * 0.5, 40) - 4);
        }
        items.forEach(it => {
          const s = it.o.s, isSel = it.o.i === sel;
          let lines;
          if (hMode) {
            const pat = pattern(s), tot = pat.reduce((a, b) => a + b, 0);
            lines = pat.map((p, j) => ({ dx: (j - (pat.length - 1) / 2) * sp, hh: unit * s.n * p / tot }));
          } else lines = [{ dx: 0, hh: maxPx * 0.6 }];
          ctx.strokeStyle = isSel ? col.ink : col.sc;
          ctx.lineWidth = isSel ? 3.5 : 2.2; ctx.lineCap = 'butt';
          let tallest = 0;
          lines.forEach(l => {
            const hh = Math.max(2, l.hh);
            tallest = Math.max(tallest, hh);
            ctx.beginPath(); ctx.moveTo(it.x + l.dx, lineBase); ctx.lineTo(it.x + l.dx, lineBase - hh); ctx.stroke();
          });
          const ly = labTop + it.row * 14;
          // leader from label to the top of the signal
          const topY = lineBase - tallest;
          if (topY - ly > 8) {
            ctx.strokeStyle = col.rule2 || col.rule; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(it.x, ly + 3); ctx.lineTo(it.x, topY - 3); ctx.stroke();
          }
          ctx.fillStyle = isSel ? col.ink : col.ink2;
          ctx.font = (isSel ? 'bold ' : '') + '11px ' + col.font;
          ctx.textAlign = 'center';
          ctx.fillText(it.text, Math.max(padL + it.tw / 2, Math.min(it.x, padL + pw - it.tw / 2 + 6)), ly);
          geom.push({ x: it.x, i: it.o.i });
        });
      }
    });
    cvs.cv.setAttribute('role', 'img');
    cvs.cv.setAttribute('aria-label', 'NMR spectrum of the chosen molecule; use the buttons below to select a signal');
    cvs.cv.addEventListener('click', ev => {
      const r = cvs.cv.getBoundingClientRect();
      const x = ev.clientX - r.left;
      let best = null, bd = 1e9;
      geom.forEach(g => { const d = Math.abs(g.x - x); if (d < bd) { bd = d; best = g; } });
      if (best && bd <= 18) { sel = best.i; update(); }
    });

    const btnRow = W.h('div', { class: 'w-row', style: { marginTop: '6px' } });
    body.appendChild(btnRow);
    const read = W.readout([['count', 'Signals'], ['sel', 'Selected']]);
    body.appendChild(read.el);
    body.appendChild(err);
    const note = W.h('div', { class: 'w-note' });
    body.appendChild(note);

    function selText(P) {
      const list = mode === 'h' ? P.h : P.c;
      const s = list[sel];
      if (!s) return 'click a signal, or use a button above, to see where it comes from';
      if (mode === 'h') {
        const lines = s.adj + 1;
        return 'δ ' + s.d.toFixed(1) + ': ' + s.n + ' H on ' + s.g + ' · ' + lineName(s.adj) + (s.adj >= 4 ? ' (' + lines + ' lines)' : '') +
          ' because ' + (s.ex ? 'O–H hydrogens are not split' : s.adj + ' neighbouring H, and ' + s.adj + ' + 1 = ' + lines) + ' · Data booklet range ' + s.r;
      }
      return 'δ ' + s.d + ': ' + (s.k > 1 ? s.k + ' equivalent carbons, ' : '') + s.g + ' · Data booklet range ' + s.r;
    }

    function update() {
      const P = PRESETS[mol];
      tabH.setAttribute('aria-selected', mode === 'h' ? 'true' : 'false');
      tabC.setAttribute('aria-selected', mode === 'c' ? 'true' : 'false');
      d2oRow.style.display = mode === 'h' ? 'flex' : 'none';
      select.value = mol;
      // formula with the chosen signal highlighted
      formulaLine.textContent = '';
      P.segs.forEach(sg => {
        const idx = mode === 'h' ? sg[1] : sg[2];
        const on = sel >= 0 && (Array.isArray(idx) ? idx.indexOf(sel) >= 0 : idx === sel);
        const sp = W.h('span', { text: sg[0] });
        if (on) { sp.style.fontWeight = '700'; sp.style.color = 'var(--sc)'; sp.style.textDecoration = 'underline'; }
        formulaLine.appendChild(sp);
      });
      formulaLine.appendChild(W.h('span', { class: 'w-lab', style: { marginLeft: '10px' }, text: P.name }));
      // buttons for each signal
      btnRow.textContent = '';
      const list = mode === 'h' ? P.h : P.c;
      list.forEach((s, i) => {
        if (mode === 'h' && d2o && s.ex) return;
        const label = mode === 'h' ? 'δ ' + s.d.toFixed(1) : 'δ ' + s.d;
        const b = W.h('button', { class: 'btn btn-sm' + (i === sel ? '' : ' btn-sec'), type: 'button', text: label, 'aria-label': 'Signal at ' + label + ' ppm, ' + s.g, onclick: () => { sel = i; update(); } });
        btnRow.appendChild(b);
      });
      // readout
      if (mode === 'h') {
        const shown = P.h.filter(s => !(d2o && s.ex)).length;
        const nH = P.h.reduce((a, s) => a + s.n, 0);
        read.set('count', shown + ' signal' + (shown === 1 ? '' : 's') + ' from ' + nH + ' hydrogen atoms' + (d2o && shown < P.h.length ? ' (the O–H signal has gone with D₂O)' : ''));
      } else {
        const nC = P.c.reduce((a, s) => a + s.k, 0);
        read.set('count', P.c.length + ' peak' + (P.c.length === 1 ? '' : 's') + ' from ' + nC + ' carbon atoms');
      }
      if (sel >= 0 && mode === 'h' && d2o && P.h[sel] && P.h[sel].ex) sel = -1;
      read.set('sel', selText(P));
      note.textContent = mode === 'h'
        ? 'Letters: s singlet, d doublet, t triplet, q quartet, m multiplet; then the number of hydrogens. The gaps inside each group of lines are drawn much wider than real ones. Try ticking D₂O.'
        : 'Each peak is one carbon environment, so equivalent carbons share one peak. Heights carry no meaning here. Shifts are typical values inside the Data booklet ranges.';
      err.textContent = msgs.join(' ');
      cvs.redraw();
    }
    update();
  });
})();
