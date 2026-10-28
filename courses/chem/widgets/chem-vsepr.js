/* widgets/chem-vsepr.js: 3D VSEPR model. Pick a molecule, or set the bonding pairs (2 to 6) and lone pairs (0 to 3).
   Attributes: data-preset="NH3" (BF3 CO2 CH4 NH3 H2O SF6 PF5 NH4+ H3O+ BeCl2 PCl5 SO2), or data-bp="3" data-lp="1". */
(function () {
  'use strict';

  const SUBS = { '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆' };

  // key "bonding,lone" -> arrangement of the pairs, shape name, bond angle text, examples, lone-pair order
  const SHAPES = {
    '2,0': { arr: 'linear', shape: 'linear', angle: '180°', ex: 'CO₂, BeCl₂', t: 2 },
    '3,0': { arr: 'trigonal planar', shape: 'trigonal planar', angle: '120°', ex: 'BF₃, CO₃²⁻, NO₃⁻', t: 3 },
    '2,1': { arr: 'trigonal planar', shape: 'non-linear', angle: 'a little under 120°', ex: 'SO₂', t: 3, lone: [1], lab: { 120: '<120°' } },
    '4,0': { arr: 'tetrahedral', shape: 'tetrahedral', angle: '109.5°', ex: 'CH₄, NH₄⁺, SiCl₄, SO₄²⁻', t: 4, lab: { 109: '109.5°' } },
    '3,1': { arr: 'tetrahedral', shape: 'pyramidal', angle: '107°', ex: 'NH₃, H₃O⁺, PCl₃', t: 4, lone: [2], lab: { 109: '107°' } },
    '2,2': { arr: 'tetrahedral', shape: 'non-linear', angle: '104.5°', ex: 'H₂O', t: 4, lone: [2, 1], lab: { 109: '104.5°' } },
    '5,0': { arr: 'trigonal bipyramidal', shape: 'trigonal bipyramidal', angle: '120° and 90°', ex: 'PF₅, PCl₅', t: 5 },
    '4,1': { arr: 'trigonal bipyramidal', shape: 'see-saw', angle: 'about 120° and 90° (squeezed a little)', ex: 'SF₄', t: 5, lone: [3], lab: { 120: '≈120°', 90: '≈90°' } },
    '3,2': { arr: 'trigonal bipyramidal', shape: 'T-shaped', angle: 'about 90°', ex: 'ClF₃', t: 5, lone: [3, 2], lab: { 90: '≈90°' } },
    '2,3': { arr: 'trigonal bipyramidal', shape: 'linear', angle: '180°', ex: 'XeF₂', t: 5, lone: [3, 2, 4] },
    '6,0': { arr: 'octahedral', shape: 'octahedral', angle: '90°', ex: 'SF₆', t: 6 },
    '5,1': { arr: 'octahedral', shape: 'square pyramidal', angle: 'about 90°', ex: 'BrF₅', t: 6, lone: [5], lab: { 90: '≈90°' } },
    '4,2': { arr: 'octahedral', shape: 'square planar', angle: '90°', ex: 'ICl₄⁻, XeF₄', t: 6, lone: [5, 4] }
  };

  // id, label, bonding, lone, central atom, outer atom, angle text (optional), note
  const PRESETS = [
    ['BF3', 'BF₃', 3, 0, 'B', 'F', '', 'Boron has only 6 electrons around it.'],
    ['CO2', 'CO₂', 2, 0, 'C', 'O', '', 'Each C=O double bond counts as one region of electron density.'],
    ['CH4', 'CH₄', 4, 0, 'C', 'H', '', ''],
    ['NH3', 'NH₃', 3, 1, 'N', 'H', '', 'The lone pair repels the bonding pairs more strongly, so the angle closes from 109.5° to 107°.'],
    ['H2O', 'H₂O', 2, 2, 'O', 'H', '', 'Two lone pairs close the angle further, to 104.5°.'],
    ['SF6', 'SF₆', 6, 0, 'S', 'F', '', 'Sulfur has 12 electrons around it: an expanded octet.'],
    ['PF5', 'PF₅', 5, 0, 'P', 'F', '', 'Two axial bonds (up and down) and three equatorial bonds.'],
    ['NH4+', 'NH₄⁺', 4, 0, 'N', 'H', '', 'Four bonding pairs, one of them a dative bond, but all four are identical.'],
    ['H3O+', 'H₃O⁺', 3, 1, 'O', 'H', 'about 107°', 'Like ammonia: three bonding pairs and one lone pair.'],
    ['BeCl2', 'BeCl₂', 2, 0, 'Be', 'Cl', '', 'Beryllium has only 4 electrons around it.'],
    ['PCl5', 'PCl₅', 5, 0, 'P', 'Cl', '', 'Same shape as PF₅.'],
    ['SO2', 'SO₂', 2, 1, 'S', 'O', '', 'Each S=O counts as one region. With the lone pair there are three regions, so the molecule is non-linear.']
  ];

  function sub(s) { return String(s).replace(/[0-9]/g, c => SUBS[c]); }
  function lookupPreset(raw) {
    const k = String(raw).replace(/[₀-₆]/g, c => '0123456'.charAt('₀₁₂₃₄₅₆'.indexOf(c))).replace(/\s+/g, '').replace(/⁺/g, '+').toLowerCase();
    return PRESETS.find(p => p[0].toLowerCase() === k || p[0].toLowerCase() === k + '+' || p[0].toLowerCase().replace('+', '') === k) || null;
  }

  // unit vectors for the t pair positions (x right, y into the page, z up)
  function positions(t) {
    const c = a => Math.cos(a * Math.PI / 180), s = a => Math.sin(a * Math.PI / 180);
    if (t === 2) return [[1, 0, 0], [-1, 0, 0]];
    if (t === 3) return [[1, 0, 0], [c(120), s(120), 0], [c(240), s(240), 0]];
    if (t === 4) { const r = Math.sqrt(8 / 9); return [[0, 0, 1], [r, 0, -1 / 3], [r * c(120), r * s(120), -1 / 3], [r * c(240), r * s(240), -1 / 3]]; }
    if (t === 5) return [[0, 0, 1], [0, 0, -1], [1, 0, 0], [c(120), s(120), 0], [c(240), s(240), 0]];
    return [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];
  }

  function angleBetween(u, v) {
    const d = u[0] * v[0] + u[1] * v[1] + u[2] * v[2];
    return Math.acos(Math.max(-1, Math.min(1, d))) * 180 / Math.PI;
  }

  W.register('chem-vsepr', function (el, opts) {
    const { body } = W.frame(el, 'VSEPR shapes', 'Choose a molecule or set the pairs, then drag the picture to turn it');

    let bp = 3, lp = 1, preset = PRESETS[3];   // ammonia
    let msg = '';

    // ----- start state from the data attributes -----
    if (opts.preset !== undefined && opts.preset !== '') {
      const p = lookupPreset(opts.preset);
      if (p) { preset = p; bp = p[2]; lp = p[3]; }
      else msg = 'The preset "' + String(opts.preset).slice(0, 20) + '" is not in the list. Showing ammonia instead; pick another from the list.';
    } else if ((opts.bp !== undefined && opts.bp !== '') || (opts.lp !== undefined && opts.lp !== '')) {
      const b = opts.bp === undefined || opts.bp === '' ? 2 : Number(opts.bp);
      const l = opts.lp === undefined || opts.lp === '' ? 0 : Number(opts.lp);
      if (Number.isInteger(b) && Number.isInteger(l) && b >= 2 && b <= 6 && l >= 0 && l <= 3 && SHAPES[b + ',' + l]) { bp = b; lp = l; preset = null; }
      else {
        const gave = [];
        if (opts.bp !== undefined && opts.bp !== '') gave.push(String(opts.bp).slice(0, 12) + ' bonding pairs');
        if (opts.lp !== undefined && opts.lp !== '') gave.push(String(opts.lp).slice(0, 12) + ' lone pairs');
        msg = 'This tool takes 2 to 6 bonding pairs and 0 to 3 lone pairs, with at most 6 pairs in all (you gave ' + gave.join(' and ') + '). Showing ammonia instead.';
      }
    }

    // ----- controls -----
    const selP = W.h('select', { 'aria-label': 'Molecule or ion' });
    selP.appendChild(W.h('option', { value: '', text: 'Set the pairs myself' }));
    PRESETS.forEach(p => selP.appendChild(W.h('option', { value: p[0], text: p[1] })));
    const selB = W.h('select', { 'aria-label': 'Bonding pairs' });
    for (let k = 2; k <= 6; k++) selB.appendChild(W.h('option', { value: String(k), text: String(k) }));
    const selL = W.h('select', { 'aria-label': 'Lone pairs' });
    for (let k = 0; k <= 3; k++) selL.appendChild(W.h('option', { value: String(k), text: String(k) }));
    const left = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', 'aria-label': 'Turn the model left' }, '◀ Turn');
    const right = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', 'aria-label': 'Turn the model right' }, 'Turn ▶');
    body.appendChild(W.h('div', { class: 'w-row' },
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Molecule or ion' }), selP),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Bonding pairs' }), selB),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Lone pairs' }), selL)));
    const err = W.h('div', { class: 'w-err', role: 'status' });
    body.appendChild(err);

    // ----- the 3D picture -----
    const v = W.view3d({ yaw: 1.2, pitch: 0.5, scale: 90 });
    let model = null;     // current geometry
    const cvs = W.canvas(body, {
      height: 300,
      draw(ctx, w, h, col) {
        if (!model) return;
        const R = 1;
        v.scale = Math.min(w, h) * 0.36;
        const C = v.project(0, 0, 0, w, h);
        const P = model.dirs.map(d => v.project(d[0] * R, d[1] * R, d[2] * R, w, h));
        ctx.textBaseline = 'alphabetic';

        // faint outline of the ideal arrangement
        ctx.save();
        ctx.setLineDash([4, 4]); ctx.strokeStyle = col.rule2; ctx.lineWidth = 1;
        for (let i = 0; i < model.dirs.length; i++) for (let j = i + 1; j < model.dirs.length; j++) {
          if (angleBetween(model.dirs[i], model.dirs[j]) < 125) {
            ctx.beginPath(); ctx.moveTo(P[i][0], P[i][1]); ctx.lineTo(P[j][0], P[j][1]); ctx.stroke();
          }
        }
        ctx.restore();

        // items sorted far to near (larger depth = further away)
        const items = [];
        items.push({ d: C[2], fn() {
          ctx.lineWidth = 3; ctx.strokeStyle = col.sc; ctx.fillStyle = col.card;
          ctx.beginPath(); ctx.arc(C[0], C[1], 15, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
          ctx.fillStyle = col.ink; ctx.font = '600 14px ' + col.font; ctx.textAlign = 'center';
          ctx.fillText(model.centre, C[0], C[1] + 5);
        } });
        model.dirs.forEach((dir, i) => {
          const p = P[i];
          if (model.lone[i]) {
            items.push({ d: 100, fn() {
              // a lobe along the direction: ellipse centred half way along the pair direction
              const mx = (C[0] + p[0]) / 2, my = (C[1] + p[1]) / 2;
              const dx = p[0] - C[0], dy = p[1] - C[1];
              const len = Math.hypot(dx, dy);
              const minor = 0.22 * v.scale;
              const major = Math.max(len / 2 * 1.05, minor);
              const rot = len < 1 ? 0 : Math.atan2(dy, dx);
              ctx.save();
              ctx.globalAlpha = 0.38; ctx.fillStyle = col.sc2;
              ctx.beginPath(); ctx.ellipse(mx, my, major, minor, rot, 0, 2 * Math.PI); ctx.fill();
              ctx.globalAlpha = 0.95; ctx.strokeStyle = col.sc2; ctx.lineWidth = 1.5; ctx.stroke();
              ctx.restore();
              ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(mx - 3, my, 1.8, 0, 2 * Math.PI); ctx.arc(mx + 3, my, 1.8, 0, 2 * Math.PI); ctx.fill();
            } });
          } else {
            items.push({ d: p[2], fn() {
              ctx.lineWidth = 3; ctx.strokeStyle = col.ink3;
              ctx.beginPath(); ctx.moveTo(C[0], C[1]); ctx.lineTo(p[0], p[1]); ctx.stroke();
              const r = Math.max(9, 12 - 2.5 * p[2]);
              ctx.lineWidth = 1.5; ctx.strokeStyle = col.ink2; ctx.fillStyle = col.card;
              ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
              ctx.fillStyle = col.ink; ctx.font = '600 ' + (model.outer.length > 1 ? 10 : 12) + 'px ' + col.font; ctx.textAlign = 'center';
              ctx.fillText(model.outer, p[0], p[1] + 4);
            } });
          }
        });
        items.sort((a, b) => b.d - a.d).forEach(it => it.fn());

        // bond-angle arcs: one per kind of angle among the bonded atoms
        const bonded = model.dirs.filter((d, i) => !model.lone[i]);
        const seen = {};
        let drawn = 0;
        for (let i = 0; i < bonded.length; i++) for (let j = i + 1; j < bonded.length; j++) {
          const a = angleBetween(bonded[i], bonded[j]);
          const key = Math.round(a);
          if (key >= 175 || seen[key] || drawn >= 2) continue;
          seen[key] = true; drawn++;
          const u = bonded[i], q = bonded[j], th = a * Math.PI / 180, sn = Math.sin(th);
          const ra = 0.5;
          ctx.strokeStyle = col.red; ctx.lineWidth = 2; ctx.beginPath();
          for (let k = 0; k <= 16; k++) {
            const t = k / 16, f1 = Math.sin((1 - t) * th) / sn, f2 = Math.sin(t * th) / sn;
            const pt = v.project(ra * (f1 * u[0] + f2 * q[0]), ra * (f1 * u[1] + f2 * q[1]), ra * (f1 * u[2] + f2 * q[2]), w, h);
            if (k === 0) ctx.moveTo(pt[0], pt[1]); else ctx.lineTo(pt[0], pt[1]);
          }
          ctx.stroke();
          const um = [u[0] + q[0], u[1] + q[1], u[2] + q[2]], ml = Math.hypot(um[0], um[1], um[2]) || 1;
          const M = v.project(ra * um[0] / ml, ra * um[1] / ml, ra * um[2] / ml, w, h);
          let ox = M[0] - C[0], oy = M[1] - C[1];
          const ol = Math.hypot(ox, oy);
          if (ol < 6) { ox = 0; oy = -1; } else { ox /= ol; oy /= ol; }
          const lp2 = [M[0] + ox * 20, M[1] + oy * 16];
          ctx.fillStyle = col.red; ctx.font = '600 12px ' + col.font; ctx.textAlign = 'center';
          const label = (model.shape.lab && model.shape.lab[key]) || (key + '°');
          ctx.fillText(model.angleOverride && drawn === 1 && Object.keys(seen).length === 1 ? model.angleOverride : label, lp2[0], lp2[1] + 4);
        }
        if (bonded.length === 2 && Math.round(angleBetween(bonded[0], bonded[1])) >= 175) {
          ctx.fillStyle = col.red; ctx.font = '600 12px ' + col.font; ctx.textAlign = 'center';
          ctx.fillText('180°', C[0], C[1] - 26);
        }
      }
    });
    cvs.cv.setAttribute('role', 'img');
    cvs.describe = () => {
      if (!model) return '';
      const s = model.shape;
      return 'A 3D model of a central ' + model.centre + ' atom with ' + bp + ' bonding pair' + (bp === 1 ? '' : 's') + ' (shown as bonds to ' + model.outer + ' atoms) and ' + lp + ' lone pair' + (lp === 1 ? '' : 's') + ' (shown as shaded lobes with two dots). The pairs form a '
        + s.arr + ' arrangement, so the shape is ' + s.shape + ' with bond angle ' + (preset && preset[6] ? preset[6] : s.angle) + '. The turn buttons rotate the view.';
    };
    W.orbit(cvs.wrap, v, cvs.redraw);
    body.appendChild(W.h('div', { class: 'w-row' }, left, right));

    const read = W.readout([['pairs', 'Electron pairs'], ['arr', 'Arrangement of the pairs'], ['shape', 'Shape'], ['angle', 'Bond angle'], ['ex', 'Examples'], ['note', 'Note']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Add a lone pair to CH₄ and watch the angle close. Shaded lobes with two dots are lone pairs; the labelled arcs show bond angles. With six pairs, add a lone pair, then a second one, and see where it goes.' }));

    function update() {
      const key = bp + ',' + lp;
      const s = SHAPES[key] || SHAPES['3,1'];
      const t = bp + lp;
      const dirs = positions(t);
      const lone = dirs.map(() => false);
      (s.lone || []).slice(0, lp).forEach(i => { lone[i] = true; });
      // pad the lone-pair list when lp is larger than the list (cannot happen for the table, kept for safety)
      model = {
        dirs, lone, shape: s,
        centre: preset ? preset[4] : 'X',
        outer: preset ? preset[5] : 'A',
        angleOverride: preset && preset[6] ? preset[6].replace('about ', '≈') : ''
      };
      const nm = preset ? preset[1] : null;
      selP.value = preset ? preset[0] : '';
      selB.value = String(bp);
      selL.value = String(lp);
      read.set('pairs', t + ' (' + bp + ' bonding + ' + lp + ' lone)');
      read.set('arr', s.arr);
      read.set('shape', s.shape);
      read.set('angle', preset && preset[6] ? preset[6] : s.angle);
      read.set('ex', nm ? nm + (s.ex && s.ex.indexOf(nm) < 0 ? '  (also ' + s.ex + ')' : '') : s.ex);
      read.set('note', preset && preset[7] ? preset[7] : (lp === 0 ? 'No lone pairs: the shape has the same name as the arrangement.' : (s.shape === 'linear' || s.shape === 'square planar') ? 'The lone pairs are spread symmetrically, so their pushes balance and the bond angles are not squeezed.' : 'Lone pairs repel more than bonding pairs, so the angles close a little.'));
      err.textContent = msg;
      cvs.setLabel('3D VSEPR model: ' + (nm ? nm.replace(/[₀-₆]/g, c => '0123456'.charAt('₀₁₂₃₄₅₆'.indexOf(c))).replace('⁺', '+') + ', ' : '') + s.shape);
      cvs.redraw();
    }

    // keep bp + lp <= 6 and lone pairs only where a common shape exists
    function fix(changed) {
      let note = '';
      if (lp === 3 && bp !== 2) {
        if (changed === 'lp') { bp = 2; note = 'Three lone pairs fit only with two bonding pairs here (a linear molecule such as XeF₂).'; }
        else { lp = Math.min(2, 6 - bp); note = 'Three lone pairs are used only with two bonding pairs, so the lone pairs were reduced to ' + lp + '.'; }
      }
      if (bp + lp > 6) {
        if (changed === 'lp') { bp = 6 - lp; note = 'A central atom here holds at most 6 pairs in all, so the bonding pairs were reduced to ' + bp + '.'; }
        else { lp = 6 - bp; note = 'A central atom here holds at most 6 pairs in all, so the lone pairs were reduced to ' + lp + '.'; }
      }
      msg = note;
    }

    selP.addEventListener('change', () => {
      const p = PRESETS.find(q => q[0] === selP.value);
      if (p) { preset = p; bp = p[2]; lp = p[3]; } else { preset = null; }
      msg = '';
      update();
    });
    selB.addEventListener('change', () => { bp = Number(selB.value); preset = null; fix('bp'); update(); });
    selL.addEventListener('change', () => { lp = Number(selL.value); preset = null; fix('lp'); update(); });
    left.addEventListener('click', () => { v.yaw -= 0.4; cvs.redraw(); });
    right.addEventListener('click', () => { v.yaw += 0.4; cvs.redraw(); });
    update();
  });
})();
