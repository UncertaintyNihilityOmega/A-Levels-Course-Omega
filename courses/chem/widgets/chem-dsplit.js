/* widgets/chem-dsplit.js: splitting of the 3d orbitals in an octahedral or tetrahedral complex, electrons, promotion and colour.
   Attributes: data-geom="oct" | "tet", data-ion="Cu2+" (Sc3+ Ti3+ V3+ Cr3+ Mn2+ Fe2+ Fe3+ Co2+ Ni2+ Cu2+ Zn2+),
   data-ligand="H2O" | "NH3" | "Cl-" | "CN-".
   The d-electron count is computed from Z and the charge (4s electrons leave first). The gap is a relative scale only
   ("relative units, not to scale"); the colour words are illustrative and come from the gap alone. */
(function () {
  'use strict';

  const SUPMAP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '+': '⁺', '-': '⁻' };
  const sup = s => String(s).replace(/[0-9+\-]/g, c => SUPMAP[c]);

  const IONS = [
    ['Sc', 21, 3], ['Ti', 22, 3], ['V', 23, 3], ['Cr', 24, 3], ['Mn', 25, 2], ['Fe', 26, 2], ['Fe', 26, 3],
    ['Co', 27, 2], ['Ni', 28, 2], ['Cu', 29, 2], ['Zn', 30, 2]
  ];
  const ionKey = i => i[0] + i[2] + '+';
  const ionLabel = i => i[0] + sup(i[2] + '+');

  const LIGANDS = [
    { key: 'Cl-', label: 'Cl⁻ (chloride)', rel: 0.8 },
    { key: 'H2O', label: 'H₂O (water)', rel: 1.0 },
    { key: 'NH3', label: 'NH₃ (ammonia)', rel: 1.25 },
    { key: 'CN-', label: 'CN⁻ (cyanide)', rel: 2.0 }
  ];
  const TET = 0.6;      // the tetrahedral gap is smaller (relative units)

  // d electrons from Z and charge: atom 3d(Z-20) 4s2 with the Cr and Cu exceptions; 4s electrons are lost first
  function dElectrons(z, q) {
    let nd = z - 20, s4 = 2;
    if (z === 24) { nd = 5; s4 = 1; }
    if (z === 29) { nd = 10; s4 = 1; }
    for (let k = 0; k < q; k++) { if (s4 > 0) s4 -= 1; else nd -= 1; }
    return Math.max(0, Math.min(10, nd));
  }

  // illustrative bands from the relative gap
  const BANDS = [
    { max: 0.45, abs: 'infrared (little visible light)', seen: 'pale or colourless in this model' },
    { max: 1.10, abs: 'red / orange', seen: 'blue / blue-green' },
    { max: 1.40, abs: 'orange / yellow', seen: 'blue / violet' },
    { max: 1.80, abs: 'yellow / green', seen: 'violet / red' },
    { max: 2.30, abs: 'green / blue', seen: 'red / orange' },
    { max: 99, abs: 'blue / violet', seen: 'orange / yellow' }
  ];
  const band = r => BANDS.find(b => r < b.max) || BANDS[BANDS.length - 1];

  // fill n electrons into k orbitals: singly first, then pair. Returns [{up, down}] per orbital
  function fill(n, k) {
    const o = [];
    for (let i = 0; i < k; i++) o.push({ up: false, down: false });
    const m = Math.min(n, 2 * k);
    for (let e = 0; e < m; e++) { if (e < k) o[e].up = true; else o[e - k].down = true; }
    return { orbs: o, used: m };
  }

  W.register('chem-dsplit', function (el, opts) {
    const { body } = W.frame(el, 'Splitting of the d orbitals', 'Choose a shape, a metal ion and a ligand to see the gap, the electrons and the colour');
    const msgs = [];
    let geom = 'oct', ion = IONS[9], lig = LIGANDS[1];

    if (opts.geom !== undefined && opts.geom !== '') {
      const g = String(opts.geom).toLowerCase();
      if (g === 'oct' || g === 'octahedral') geom = 'oct';
      else if (g === 'tet' || g === 'tetrahedral') geom = 'tet';
      else msgs.push('data-geom must be "oct" or "tet". Showing octahedral.');
    }
    if (opts.ion !== undefined && opts.ion !== '') {
      const f = IONS.find(i => ionKey(i) === String(opts.ion));
      if (f) ion = f;
      else msgs.push('data-ion = "' + W.esc(String(opts.ion)) + '" is not available here (try Ti3+, Fe2+, Cu2+, Zn2+). Showing Cu²⁺.');
    }
    if (opts.ligand !== undefined && opts.ligand !== '') {
      const f = LIGANDS.find(l => l.key === String(opts.ligand) || l.key.replace('-', '') === String(opts.ligand));
      if (f) lig = f;
      else msgs.push('data-ligand must be H2O, NH3, Cl- or CN-. Showing water.');
    }

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const selG = W.h('select', { 'aria-label': 'Shape of the complex' },
      W.h('option', { value: 'oct', text: 'Octahedral (6 ligands)' }), W.h('option', { value: 'tet', text: 'Tetrahedral (4 ligands)' }));
    const selI = W.h('select', { 'aria-label': 'Metal ion' });
    IONS.forEach((i, k) => selI.appendChild(W.h('option', { value: String(k), text: ionLabel(i) })));
    const selL = W.h('select', { 'aria-label': 'Ligand' });
    LIGANDS.forEach((l, k) => selL.appendChild(W.h('option', { value: String(k), text: l.label })));
    body.appendChild(W.h('div', { class: 'w-row' },
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Shape' }), selG),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Metal ion' }), selI),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Ligand' }), selL)));
    body.appendChild(err);

    const title = W.h('div', { style: { fontWeight: '600', margin: '4px 0' } });
    body.appendChild(title);

    let model = null;     // computed in update()
    const cvs = W.canvas(body, {
      height: 270,
      draw(ctx, w, h, col) {
        if (!model || !(w > 60) || !(h > 60)) return;          // survives zero size
        const sw = w < 420 ? 14 : 18, gap = 4;
        const nU = model.nU, nL = model.nL;
        const cy = h * 0.5 + 6;
        const G = 36 + 96 * Math.min(model.rel / 2.0, 1.2);      // pixels for the gap
        const yUp = Math.max(46, cy - G * nL / 5), yLow = Math.min(h - 44, cy + G * nU / 5);
        const yFree = (nU * yUp + nL * yLow) / 5;
        ctx.font = '12px ' + col.font;
        ctx.textBaseline = 'alphabetic';
        // energy axis
        ctx.strokeStyle = col.ink3; ctx.fillStyle = col.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(12, h - 14); ctx.lineTo(12, 28); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(12, 22); ctx.lineTo(8, 30); ctx.lineTo(16, 30); ctx.closePath(); ctx.fill();
        ctx.textAlign = 'left'; ctx.fillText('energy', 4, 14);
        const x0 = 30, xs = w * 0.50;
        const slotX = (x, i) => x + i * (sw + gap);
        const el1 = (x, y, up, colr) => {                      // one electron arrow in a slot centred on x at level y
          ctx.strokeStyle = colr; ctx.lineWidth = 1.6;
          ctx.beginPath();
          if (up) { ctx.moveTo(x, y - 2); ctx.lineTo(x, y - 16); ctx.moveTo(x - 3, y - 13); ctx.lineTo(x, y - 17); ctx.lineTo(x + 3, y - 13); }
          else { ctx.moveTo(x, y - 16); ctx.lineTo(x, y - 2); ctx.moveTo(x - 3, y - 5); ctx.lineTo(x, y - 1); ctx.lineTo(x + 3, y - 5); }
          ctx.stroke();
        };
        const level = (x, y, st) => {
          ctx.strokeStyle = col.ink; ctx.lineWidth = 2.2;
          ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + sw, y); ctx.stroke();
          if (st.up && st.down) { el1(x + sw / 2 - 3, y, true, col.ink); el1(x + sw / 2 + 3, y, false, col.ink); }
          else if (st.up) el1(x + sw / 2, y, true, col.ink);
          else if (st.down) el1(x + sw / 2, y, false, col.ink);
        };
        // free ion: five levels at the average energy
        model.free.orbs.forEach((st, i) => level(slotX(x0, i), yFree, st));
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ctx.fillText('free ion', x0 + (5 * (sw + gap) - gap) / 2, yFree + 20);
        ctx.fillText('same energy', x0 + (5 * (sw + gap) - gap) / 2, yFree + 34);
        // connectors
        const xFreeEnd = x0 + 5 * (sw + gap) - gap + 4;
        ctx.strokeStyle = col.rule2; ctx.lineWidth = 1; ctx.setLineDash([4, 3]);
        ctx.beginPath(); ctx.moveTo(xFreeEnd, yFree); ctx.lineTo(xs - 6, yUp); ctx.moveTo(xFreeEnd, yFree); ctx.lineTo(xs - 6, yLow); ctx.stroke();
        ctx.setLineDash([]);
        // split levels
        model.up.orbs.forEach((st, i) => level(slotX(xs, i), yUp, st));
        model.low.orbs.forEach((st, i) => level(slotX(xs, i), yLow, st));
        const cU = xs + (nU * (sw + gap) - gap) / 2, cL = xs + (nL * (sw + gap) - gap) / 2;
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ctx.fillText('higher set (' + nU + ')', cU, yUp - 22);
        ctx.fillText('lower set (' + nL + ')', cL, yLow + 18);
        // gap arrow
        const xa = Math.min(w - 40, xs + 3 * (sw + gap) + 18);
        ctx.strokeStyle = col.sc; ctx.fillStyle = col.sc; ctx.lineWidth = 1.8;
        const ym = (yUp + yLow) / 2;
        ctx.beginPath(); ctx.moveTo(xa, ym - 4); ctx.lineTo(xa, yUp + 2); ctx.moveTo(xa, ym + 4); ctx.lineTo(xa, yLow - 2); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xa, yUp); ctx.lineTo(xa - 4, yUp + 8); ctx.lineTo(xa + 4, yUp + 8); ctx.closePath(); ctx.fill();
        ctx.beginPath(); ctx.moveTo(xa, yLow); ctx.lineTo(xa - 4, yLow - 8); ctx.lineTo(xa + 4, yLow - 8); ctx.closePath(); ctx.fill();
        ctx.textAlign = 'left'; ctx.fillText('ΔE', xa + 7, ym + 4);
        // promotion
        if (model.promo) {
          const sx = slotX(xs, model.promo.from) + sw / 2, tx = slotX(xs, model.promo.to) + sw / 2;
          ctx.strokeStyle = col.red; ctx.fillStyle = col.red; ctx.lineWidth = 1.6; ctx.setLineDash([4, 3]);
          ctx.beginPath(); ctx.moveTo(sx + 6, yLow - 18); ctx.lineTo(tx + 6, yUp + 4); ctx.stroke(); ctx.setLineDash([]);
          const ang = Math.atan2((yUp + 4) - (yLow - 18), tx - sx);
          ctx.beginPath(); ctx.moveTo(tx + 6, yUp + 4);
          ctx.lineTo(tx + 6 - 8 * Math.cos(ang - 0.4), yUp + 4 - 8 * Math.sin(ang - 0.4));
          ctx.lineTo(tx + 6 - 8 * Math.cos(ang + 0.4), yUp + 4 - 8 * Math.sin(ang + 0.4)); ctx.closePath(); ctx.fill();
          // the promoted electron sits above the upper level, offset so it does not hide the electrons already there
          if (model.up.orbs[model.promo.to].up) el1(slotX(xs, model.promo.to) + sw / 2 + 4, yUp, false, col.red);
          else el1(slotX(xs, model.promo.to) + sw / 2, yUp, true, col.red);
        }
      }
    });
    cvs.cv.setAttribute('role', 'img');

    const read = W.readout([['d', 'd electrons'], ['sets', 'Electrons in lower / higher set'], ['col', 'Coloured?'],
      ['de', 'Relative ΔE'], ['abs', 'Light absorbed (illustrative)'], ['seen', 'Colour seen (illustrative)']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Try Cu²⁺ with water, then ammonia, then tetrahedral with chloride, then Zn²⁺. Electrons fill the lower set first. A larger ΔE means higher-frequency light is absorbed. The scale is relative (not to scale), and the colours are illustrative: they come from the gap alone, so they fit copper(II) with water best and show the trend rather than the exact colour of every ion.' }));

    function update() {
      const z = ion[1], q = ion[2];
      const d = dElectrons(z, q);
      const oct = geom === 'oct';
      const nL = oct ? 3 : 2, nU = oct ? 2 : 3;
      const free = fill(d, 5);
      const low = fill(d, nL);
      const up = fill(Math.max(0, d - 2 * nL), nU);
      // promotion: from the highest-numbered occupied orbital of the lower set to the first upper orbital with a free place
      let promo = null;
      if (d > 0 && d < 10) {
        let from = -1;
        for (let i = nL - 1; i >= 0; i--) { if (low.orbs[i].up || low.orbs[i].down) { from = i; break; } }
        let to = -1;
        for (let i = 0; i < nU; i++) { if (!up.orbs[i].up) { to = i; break; } }
        if (to < 0) for (let i = 0; i < nU; i++) { if (!up.orbs[i].down) { to = i; break; } }
        if (from >= 0 && to >= 0) promo = { from, to };
      }
      const rel = lig.rel * (oct ? 1 : TET);
      const coloured = d > 0 && d < 10;
      model = { nU, nL, free, low, up, promo: coloured ? promo : null, rel };
      const lowN = Math.min(d, 2 * nL), upN = Math.max(0, d - 2 * nL);
      const b = band(rel);
      title.textContent = ionLabel(ion) + ' with ' + lig.label.split(' ')[0] + ', ' + (oct ? 'octahedral' : 'tetrahedral');
      read.set('d', String(d));
      read.set('sets', lowN + ' / ' + upN);
      read.set('col', coloured ? 'yes (a partly filled d sub-shell lets an electron be promoted)' : (d === 0 ? 'no (d⁰: no d electrons to promote)' : 'no (d¹⁰: no vacant place in the higher set)'));
      read.set('de', rel.toFixed(2) + ' (relative units, not to scale)');
      read.set('abs', coloured ? b.abs : 'none in the visible');
      read.set('seen', coloured ? b.seen : 'colourless');
      cvs.cv.setAttribute('aria-label', 'Energy level diagram for ' + title.textContent + ': ' + d + ' d electrons; ' + (coloured ? 'an electron can be promoted across the gap' : 'no electron can be promoted') + '.');
      selG.value = geom; selI.value = String(IONS.indexOf(ion)); selL.value = String(LIGANDS.indexOf(lig));
      err.textContent = msgs.join(' ');
      cvs.redraw();
    }
    selG.addEventListener('change', () => { geom = selG.value; msgs.length = 0; update(); });
    selI.addEventListener('change', () => { ion = IONS[Number(selI.value)] || ion; msgs.length = 0; update(); });
    selL.addEventListener('change', () => { lig = LIGANDS[Number(selL.value)] || lig; msgs.length = 0; update(); });
    update();
  });
})();
