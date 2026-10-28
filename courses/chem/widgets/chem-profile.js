/* widgets/chem-profile.js: reaction pathway (enthalpy profile) diagram with ΔH, activation energy and a catalyst.
   Attributes: data-dh="-90" (ΔH, -400 to 400 kJ/mol), data-ea="120" (activation energy, 10 to 410),
   data-cat="0" or "1" (start with a catalyst), data-labels="N2 + 3H2,2NH3" (reactant and product labels, plain text). */
(function () {
  'use strict';

  const MINUS = '−';
  const SUB = { '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉' };
  // N2 + 3H2 -> N₂ + 3H₂ (digits that follow a letter or a bracket become subscripts)
  function subs(s) {
    return String(s).replace(/([A-Za-z)\]])(\d+)/g, (m, a, d) => a + d.replace(/\d/g, ch => SUB[ch]));
  }
  const signed = v => (v < 0 ? MINUS + Math.abs(v) : (v > 0 ? '+' + v : '0'));

  W.register('chem-profile', function (el, opts) {
    const { body } = W.frame(el, 'Reaction pathway diagram', 'Change ΔH and the activation energy, then add a catalyst');

    const state = { dh: -90, ea: 120, cat: false, eaCat: 60, catTouched: false };
    const msgs = [];
    let nameR = 'reactants', nameP = 'products';

    // ---- read the attributes, with friendly messages for bad ones
    function num(key, lo, hi, fallback, what) {
      const raw = opts[key];
      if (raw === undefined || raw === '') return fallback;
      const v = Number(String(raw).replace(MINUS, '-'));
      if (!isFinite(v)) { msgs.push('data-' + key + ' must be a number (' + what + '). Showing ' + fallback + ' instead.'); return fallback; }
      if (v < lo || v > hi) { msgs.push('data-' + key + ' = ' + v + ' is outside ' + lo + ' to ' + hi + ', so it was moved to the nearest allowed value.'); return Math.min(hi, Math.max(lo, v)); }
      return v;
    }
    state.dh = Math.round(num('dh', -400, 400, -90, 'ΔH in kJ mol⁻¹, from −400 to 400') / 10) * 10;
    state.ea = Math.round(num('ea', 10, 410, 120, 'activation energy in kJ mol⁻¹, from 10 to 410') / 10) * 10;
    if (opts.cat !== undefined && opts.cat !== '') {
      const c = String(opts.cat).toLowerCase();
      if (c === '1' || c === 'true' || c === 'yes') state.cat = true;
      else if (c === '0' || c === 'false' || c === 'no') state.cat = false;
      else msgs.push('data-cat must be 0 or 1. Showing the reaction without a catalyst.');
    }
    if (opts.labels !== undefined && opts.labels !== '') {
      const parts = String(opts.labels).split(',').map(s => s.trim()).filter(Boolean);
      if (parts.length === 2 && parts[0].length <= 22 && parts[1].length <= 22) { nameR = subs(parts[0]); nameP = subs(parts[1]); }
      else msgs.push('data-labels needs two short names separated by one comma, such as "N2 + 3H2,2NH3". Using "reactants" and "products".');
    }

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const clampNote = W.h('div', { class: 'w-note', role: 'status', style: { display: 'none' } });

    // ---- controls
    const sDh = W.sliderNum({ label: 'Enthalpy change ΔH (kJ mol⁻¹)', min: -400, max: 400, step: 10, value: state.dh, oninput: v => { state.dh = v; update('dh'); } });
    const sEa = W.sliderNum({ label: 'Activation energy Eₐ (kJ mol⁻¹)', min: 10, max: 410, step: 10, value: state.ea, oninput: v => { state.ea = v; update('ea'); } });
    const sCat = W.sliderNum({ label: 'Eₐ with the catalyst (kJ mol⁻¹)', min: 5, max: 405, step: 5, value: 60, oninput: v => { state.eaCat = v; state.catTouched = true; update('cat'); } });
    const chk = W.h('input', { type: 'checkbox', 'aria-label': 'Add a catalyst' });
    chk.checked = state.cat;
    chk.onchange = () => { state.cat = chk.checked; if (state.cat && !state.catTouched) state.eaCat = defaultCat(); update('cat'); };
    const chkRow = W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, chk, W.h('span', { class: 'w-lab', text: 'add a catalyst' }));

    body.appendChild(sDh.el);
    body.appendChild(sEa.el);
    body.appendChild(W.h('div', { class: 'w-row' }, chkRow));
    const catWrap = W.h('div', {}, sCat.el);
    body.appendChild(catWrap);
    body.appendChild(err);
    body.appendChild(clampNote);

    const defaultCat = () => Math.max(5, Math.round(state.ea / 2 / 5) * 5);

    // ---- canvas
    function geometry(w, h) {
      const x0 = 34, top = 62, bottom = h - 26, labelRoom = 24;
      const vmin = Math.min(0, state.dh), vmax = state.ea;
      const k = (bottom - labelRoom - top) / Math.max(1, vmax - vmin);
      const Y = v => top + (vmax - v) * k;
      const xd = w - 34;                          // x of the ΔH arrow
      const lw = Math.max(34, Math.min(80, 0.15 * w));   // length of the reactant and product levels
      const xr0 = x0 + 58, xr1 = xr0 + lw, xp1 = xd - 16, xp0 = xp1 - lw;
      const xm = (xr1 + xp0) / 2;
      return { x0, top, bottom, Y, xd, xr0, xr1, xp0, xp1, xm };
    }

    function hump(ctx, g, yr, yp, ypk) {
      const kx = 0.45 * (g.xm - g.xr1);
      ctx.beginPath();
      ctx.moveTo(g.xr1, yr);
      ctx.bezierCurveTo(g.xr1 + kx, yr, g.xm - kx, ypk, g.xm, ypk);
      ctx.bezierCurveTo(g.xm + kx, ypk, g.xp0 - kx, yp, g.xp0, yp);
      ctx.stroke();
    }

    function arrowV(ctx, x, yMid, y1, y2) {   // double-headed vertical arrow from the middle outwards, with chord heads
      const head = (yTip, dir) => {
        ctx.beginPath(); ctx.moveTo(x, yMid); ctx.lineTo(x, yTip); ctx.stroke();
        if (Math.abs(yTip - yMid) > 12) {
          ctx.beginPath(); ctx.moveTo(x - 4, yTip - dir * 8); ctx.lineTo(x, yTip); ctx.lineTo(x + 4, yTip - dir * 8); ctx.stroke();
        }
      };
      head(y1, y1 < yMid ? -1 : 1);
      head(y2, y2 < yMid ? -1 : 1);
    }

    function text(ctx, col, s, x, y, align, color) {
      ctx.textAlign = align || 'left';
      ctx.lineWidth = 4; ctx.strokeStyle = col.card; ctx.lineJoin = 'round';
      ctx.strokeText(s, x, y);
      ctx.fillStyle = color || col.ink; ctx.fillText(s, x, y);
    }

    const cvs = W.canvas(body, {
      height: 310,
      draw(ctx, w, h, col) {
        const g = geometry(w, h);
        const { x0, top, bottom, Y } = g;
        const yr = Y(0), yp = Y(state.dh), ypk = Y(state.ea), ycat = Y(state.eaCat);
        ctx.font = '13px ' + col.font;
        ctx.textBaseline = 'alphabetic';
        ctx.lineCap = 'round';
        // axes
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.6;
        ctx.beginPath(); ctx.moveTo(x0, bottom); ctx.lineTo(x0, 10); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x0 - 4, 17); ctx.lineTo(x0, 9); ctx.lineTo(x0 + 4, 17); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x0, bottom); ctx.lineTo(w - 8, bottom); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(w - 16, bottom - 4); ctx.lineTo(w - 8, bottom); ctx.lineTo(w - 16, bottom + 4); ctx.stroke();
        ctx.fillStyle = col.ink2;
        ctx.textAlign = 'left'; ctx.fillText('enthalpy', x0 + 8, 18);
        ctx.textAlign = 'right'; ctx.fillText('progress of reaction', w - 12, bottom + 18);

        // reactant and product levels
        ctx.strokeStyle = col.ink; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(g.xr0, yr); ctx.lineTo(g.xr1, yr); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(g.xp0, yp); ctx.lineTo(g.xp1, yp); ctx.stroke();
        // guides (dashed)
        ctx.setLineDash([5, 4]); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(g.xr1, yr); ctx.lineTo(g.xd + 8, yr); ctx.stroke();
        if (state.dh !== 0) { ctx.beginPath(); ctx.moveTo(g.xp1, yp); ctx.lineTo(g.xd + 8, yp); ctx.stroke(); }
        ctx.beginPath(); ctx.moveTo(x0 + 10, ypk); ctx.lineTo(g.xm - 4, ypk); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x0 + 10, yr); ctx.lineTo(g.xr0, yr); ctx.stroke();
        if (state.cat) { ctx.beginPath(); ctx.moveTo(x0 + 40, ycat); ctx.lineTo(g.xm - 4, ycat); ctx.stroke(); }
        ctx.setLineDash([]);

        // the humps
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.6;
        hump(ctx, g, yr, yp, ypk);
        if (state.cat) {
          ctx.strokeStyle = col.sc2; ctx.lineWidth = 2.4; ctx.setLineDash([7, 5]);
          hump(ctx, g, yr, yp, ycat);
          ctx.setLineDash([]);
        }

        // Ea arrow(s) and ΔH arrow
        ctx.strokeStyle = col.red; ctx.lineWidth = 2;
        const xa = x0 + 16;
        arrowV(ctx, xa, (yr + ypk) / 2, ypk + 1, yr - 1);
        if (state.cat) { ctx.strokeStyle = col.sc2; arrowV(ctx, x0 + 46, (yr + ycat) / 2, ycat + 1, yr - 1); }
        ctx.strokeStyle = col.ok; ctx.lineWidth = 2;
        if (state.dh !== 0) arrowV(ctx, g.xd, (yr + yp) / 2, yr + (yp > yr ? 2 : -2), yp + (yp > yr ? -2 : 2));

        // short labels beside the arrows
        text(ctx, col, 'Eₐ', xa + 8, Math.min((yr + ypk) / 2 + 4, yr - 6), 'left', col.red);
        text(ctx, col, state.dh === 0 ? 'ΔH = 0' : 'ΔH', g.xd + 8, (yr + yp) / 2 + 4, state.dh === 0 ? 'right' : 'left', col.ok);

        // names of the levels: above the higher level, below the lower one
        const upperIsR = state.dh <= 0;
        text(ctx, col, nameR, (g.xr0 + g.xr1) / 2, upperIsR ? yr - 8 : yr + 18, 'center', col.ink);
        text(ctx, col, nameP, (g.xp0 + g.xp1) / 2, upperIsR && state.dh !== 0 ? yp + 18 : (state.dh === 0 ? yp - 8 : yp - 8), 'center', col.ink);

        // values in the top band
        ctx.font = '13px ' + col.font;
        let ty = 18;
        const rows = [['ΔH = ' + signed(state.dh) + ' kJ mol⁻¹', col.ok], ['Eₐ = ' + state.ea + ' kJ mol⁻¹', col.red]];
        if (state.cat) rows.push(['Eₐ (catalysed) = ' + state.eaCat + ' kJ mol⁻¹', col.sc2]);
        rows.forEach(r => { text(ctx, col, r[0], w - 12, ty, 'right', r[1]); ty += 16; });
      }
    });
    cvs.cv.setAttribute('role', 'img');
    cvs.describe = () => 'Enthalpy against progress of reaction. The reactants (' + nameR + ') start at 0 and the products (' + nameP + ') end ' + (state.dh < 0 ? 'lower, at ' : state.dh > 0 ? 'higher, at ' : 'at the same level, ') + signed(state.dh) + ' kJ per mole. The curve rises to a peak '
      + state.ea + ' kJ per mole above the reactants (the activation energy).' + (state.cat ? ' A dashed curve shows the catalysed route with a lower peak, ' + state.eaCat + ' kJ per mole above the reactants; ΔH is the same.' : '');

    const read = W.readout([['type', 'Type of reaction'], ['dh', 'Enthalpy change ΔH'], ['ea', 'Eₐ forward'], ['rev', 'Eₐ reverse = Eₐ − ΔH'], ['cat', 'With the catalyst']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Try ΔH = −90 and Eₐ = 120, then tick the catalyst: only the hump gets lower, never ΔH. Make ΔH positive (an endothermic reaction) and watch the reverse reaction become easy.' }));

    function update(who) {
      // clamping rules
      let note = '';
      if (state.dh >= state.ea) {
        state.ea = state.dh + 10;
        sEa.set(state.ea);
        note = 'The activation energy must be larger than ΔH for an endothermic reaction (the peak is above the products), so Eₐ was raised to ' + state.ea + ' kJ mol⁻¹.';
      }
      const lo = Math.max(state.dh, 0) + 5, hi = state.ea - 5;
      if (!state.catTouched) state.eaCat = defaultCat();
      if (state.eaCat > hi || state.eaCat < lo) {
        state.eaCat = Math.min(Math.max(state.eaCat, lo), Math.max(lo, hi));
        if (state.cat) note = (note ? note + ' ' : '') + 'The catalysed Eₐ must be lower than Eₐ and above ΔH, so it was set to ' + state.eaCat + ' kJ mol⁻¹.';
      }
      sCat.set(state.eaCat);
      catWrap.style.display = state.cat ? '' : 'none';
      clampNote.textContent = note;
      clampNote.style.display = note ? '' : 'none';
      err.textContent = msgs.join(' ');

      const exo = state.dh < 0, endo = state.dh > 0;
      read.set('type', exo ? 'exothermic (ΔH negative: products lower than reactants)' : (endo ? 'endothermic (ΔH positive: products higher than reactants)' : 'ΔH = 0: no net energy change'));
      read.set('dh', signed(state.dh) + ' kJ mol⁻¹');
      read.set('ea', state.ea + ' kJ mol⁻¹');
      read.set('rev', (state.ea - state.dh) + ' kJ mol⁻¹');
      read.set('cat', state.cat ? 'forward Eₐ ' + state.eaCat + ' kJ mol⁻¹, reverse Eₐ ' + (state.eaCat - state.dh) + ' kJ mol⁻¹, ΔH unchanged at ' + signed(state.dh) + ' kJ mol⁻¹' : 'no catalyst');
      cvs.setLabel('Reaction pathway diagram: ' + (exo ? 'exothermic' : (endo ? 'endothermic' : 'thermoneutral')) + (state.cat ? ', with a catalyst' : ''));
      cvs.redraw();
    }

    if (state.cat) state.eaCat = defaultCat();
    sCat.set(state.eaCat);
    update('init');
  });
})();
