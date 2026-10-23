/* widgets/chem-equilibrium.js: Le Chatelier explorer and Kc calculator.
   Attributes: data-system="haber" | "contact" | "hi" | "ester" (unknown names fall back to haber with a note),
               data-tab="lc" (Le Chatelier, default) | "kc" (Kc from data). */
(function () {
  'use strict';

  const SUBS = { '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉' };
  const MINUS = '−';
  const SUPD = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  const sup = v => String(v).replace(/[0-9-]/g, ch => SUPD[ch]);
  const unit = dn => {            // unit of Kc from the change in moles, dn
    if (dn === 0) return 'no unit';
    const e = dn, f = -3 * dn;
    return 'mol' + (e === 1 ? '' : sup(e)) + ' dm' + (f === 1 ? '' : sup(f));
  };
  function num3(x) {              // 3 significant figures, standard form for very large or small values
    if (!isFinite(x)) return '—';
    if (x === 0) return '0';
    const ax = Math.abs(x);
    if (ax >= 1e4 || ax < 1e-3) {
      const e = Math.floor(Math.log10(ax));
      let m = x / Math.pow(10, e);
      let ms = m.toPrecision(3);
      if (Math.abs(parseFloat(ms)) >= 10) { ms = (m / 10).toPrecision(3); return ms + ' × 10' + sup(e + 1); }
      return ms + ' × 10' + sup(e);
    }
    return x.toPrecision(3);
  }
  const mol = x => (Math.round(x * 1000) / 1000).toString();

  const SYSTEMS = {
    haber: {
      name: 'Haber process', sp: ['N₂', 'H₂', 'NH₃', ''], co: [1, 3, 2, 0], gas: true, dh: -1,
      p0: 0.35, kc: { init: [1, 3, 0, 0], pick: 2, eq: 0.6, v: 2 }
    },
    contact: {
      name: 'Contact process', sp: ['SO₂', 'O₂', 'SO₃', ''], co: [2, 1, 2, 0], gas: true, dh: -1,
      p0: 0.65, kc: { init: [2, 1, 0, 0], pick: 2, eq: 1.6, v: 5 }
    },
    hi: {
      name: 'Hydrogen iodide', sp: ['H₂', 'I₂', 'HI', ''], co: [1, 1, 2, 0], gas: true, dh: -0.3,
      p0: 0.65, kc: { init: [1, 1, 0, 0], pick: 2, eq: 1.5, v: 1 }
    },
    ester: {
      name: 'Esterification', sp: ['CH₃COOH', 'C₂H₅OH', 'CH₃COOC₂H₅', 'H₂O'], co: [1, 1, 1, 1], gas: false, dh: 0,
      p0: 0.67, kc: { init: [0.6, 0.6, 0, 0], pick: 2, eq: 0.4, v: 1 }
    }
  };
  const phase = s => (s.gas ? '(g)' : '(l)');
  function eqString(s, co, sp, ph) {
    const part = idx => idx.filter(i => co[i] > 0).map(i => (co[i] > 1 ? co[i] : '') + sp[i] + ph).join(' + ');
    return part([0, 1]) + ' ⇌ ' + part([2, 3]);
  }

  W.register('chem-equilibrium', function (el, opts) {
    const { body } = W.frame(el, 'Chemical equilibrium', 'Change a condition and see which way the position moves, or calculate Kc');
    const notes = [];
    let key = String(opts.system || 'haber').toLowerCase();
    if (!SYSTEMS[key]) { notes.push('data-system "' + opts.system + '" is not one of haber, contact, hi, ester, so the Haber process is shown.'); key = 'haber'; }
    let tab = 'lc';
    if (opts.tab !== undefined && opts.tab !== '') {
      const t = String(opts.tab).toLowerCase();
      if (t === 'kc') tab = 'kc'; else if (t !== 'lc') notes.push('data-tab must be "lc" or "kc", so the Le Chatelier tab is shown.');
    }
    let sys = SYSTEMS[key];
    const bad = W.h('div', { class: 'w-err', role: 'status', text: notes.join(' ') });

    // ---------- system select and tabs
    const sel = W.h('select', { 'aria-label': 'Reaction' });
    Object.keys(SYSTEMS).forEach(k => sel.appendChild(W.h('option', { value: k, text: SYSTEMS[k].name })));
    sel.value = key;
    const tabLc = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Le Chatelier' });
    const tabKc = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Kc from data' });
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Reaction' }), sel), W.h('div', { class: 'w-tabs', role: 'tablist' }, tabLc, tabKc)));
    const eqLine = W.h('div', { class: 'w-note', style: { fontSize: '1rem', color: 'var(--ink)' } });
    const infoLine = W.h('div', { class: 'w-note' });
    body.appendChild(eqLine);
    body.appendChild(infoLine);
    body.appendChild(bad);

    const panelLc = W.h('div', { style: { minWidth: '0' } });
    const panelKc = W.h('div', { style: { minWidth: '0' } });
    body.appendChild(panelLc);
    body.appendChild(panelKc);

    // =================== TAB 1: Le Chatelier ===================
    const st = { p: sys.p0, before: sys.p0, last: null };
    const gasL = () => sys.co[0] + sys.co[1];
    const gasR = () => sys.co[2] + sys.co[3];
    const result = W.h('div', { style: { margin: '10px 0 6px' } });
    const arrow = W.h('div', { style: { fontSize: '1.15rem', fontWeight: '700' }, role: 'status' });
    const kline = W.h('div', { style: { fontWeight: '600', margin: '2px 0 6px' } });
    const why = W.h('div', { style: { lineHeight: '1.5' } });
    result.appendChild(arrow); result.appendChild(kline); result.appendChild(why);

    const actions = [
      ['t+', 'raise temperature'], ['t-', 'lower temperature'], ['p+', 'raise pressure'], ['p-', 'lower pressure'],
      ['r+', 'add a reactant'], ['r-', 'remove a reactant'], ['q+', 'add a product'], ['q-', 'remove a product'], ['cat', 'add a catalyst']
    ];
    const btns = {};
    const btnRow = W.h('div', { class: 'w-row', style: { gap: '6px' } });
    actions.forEach(a => {
      const b = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', text: a[1] });
      b.onclick = () => apply(a[0]);
      btns[a[0]] = b; btnRow.appendChild(b);
    });
    const reset = W.h('button', { class: 'btn btn-sm', type: 'button', text: 'start again' });
    reset.onclick = () => { st.p = sys.p0; st.before = sys.p0; st.last = null; show(); };
    btnRow.appendChild(reset);
    panelLc.appendChild(btnRow);
    panelLc.appendChild(result);

    let cvs = null;
    const cvsHost = W.h('div', {});
    panelLc.appendChild(cvsHost);
    const canvasSpec = {
      height: 215,
      draw(ctx, w, h, col) {
        ctx.font = '13px ' + col.font; ctx.textBaseline = 'alphabetic';
        const left = 40, bottom = h - 44, top = 34, H = bottom - top;
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left, bottom); ctx.lineTo(left, 16); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(left - 4, 23); ctx.lineTo(left, 15); ctx.lineTo(left + 4, 23); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(left, bottom); ctx.lineTo(w - 8, bottom); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.textAlign = 'left';
        ctx.fillText('relative amounts (not to scale)', left + 8, 22);
        const groups = [{ nm: 'reactants', b: 1 - st.before, a: 1 - st.p }, { nm: 'products', b: st.before, a: st.p }];
        const bw = Math.max(20, Math.min(46, (w - left) * 0.12));
        const cx = [left + (w - left) * 0.27, left + (w - left) * 0.73];
        groups.forEach((g, i) => {
          const hb = g.b * H, ha = g.a * H;
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 2; ctx.setLineDash([4, 3]);
          ctx.strokeRect(cx[i] - bw - 4, bottom - hb, bw, hb);
          ctx.setLineDash([]);
          ctx.fillStyle = i === 0 ? col.sc2 : col.sc;
          ctx.fillRect(cx[i] + 4, bottom - ha, bw, ha);
          ctx.fillStyle = col.ink; ctx.textAlign = 'center';
          ctx.fillText(g.nm, cx[i], bottom + 17);
        });
        // legend, right-aligned on the first row
        ctx.textAlign = 'center'; ctx.fillStyle = col.ink2;
        ctx.fillText('dashed = before, solid = after', (left + w) / 2, h - 6);
      }
    };
    function ensureCanvas() {
      if (!cvs) { cvs = W.canvas(cvsHost, canvasSpec); cvs.cv.setAttribute('role', 'img'); }
    }

    function shiftOf(action) {
      // returns {dir: +1 right, -1 left, 0 none, small: bool, why, k: 'up' | 'down' | 'same'}
      const dh = sys.dh, gl = gasL(), gr = gasR();
      const exo = dh < 0, thermo = dh !== 0, tiny = Math.abs(dh) < 0.5 && dh !== 0;
      switch (action) {
        case 't+': case 't-': {
          const up = action === 't+';
          if (!thermo) return { dir: 0, k: 'tiny', why: 'The enthalpy change of this reaction is close to zero, so a change of temperature hardly moves the position and Kc hardly changes.' };
          const dirUp = exo ? -1 : 1;                        // raising T: left if the forward reaction is exothermic
          const dir = up ? dirUp : -dirUp;
          const towards = dir > 0 ? 'right' : 'left';
          const direction = (dir > 0) === exo ? 'exothermic' : 'endothermic';
          return {
            dir, small: tiny, k: (dir > 0) ? 'up' : 'down',
            why: (up ? 'Raising' : 'Lowering') + ' the temperature moves the position in the ' + direction + ' direction (to the ' + towards + '), ' + (up ? 'which absorbs heat' : 'which releases heat') + ', to minimise the change. The forward reaction is ' + (exo ? 'exothermic' : 'endothermic') + (tiny ? ' but only slightly, so the shift is small' : '') + '.'
          };
        }
        case 'p+': case 'p-': {
          const up = action === 'p+';
          if (!sys.gas) return { dir: 0, k: 'same', why: 'Everything here is a liquid, so changing the pressure has almost no effect on the position.' };
          if (gl === gr) return { dir: 0, k: 'same', why: 'There are ' + gl + ' mol of gas on each side, so the system cannot reduce a pressure change by moving: the position does not change.' };
          const fewerRight = gr < gl;
          const dir = (up === fewerRight) ? 1 : -1;
          return {
            dir, k: 'same',
            why: 'There are ' + gl + ' mol of gas on the left and ' + gr + ' mol on the right. ' + (up ? 'Increasing' : 'Decreasing') + ' the pressure moves the position towards the side with ' + (up ? 'fewer' : 'more') + ' moles of gas (' + (dir > 0 ? 'right' : 'left') + '), to minimise the change.'
          };
        }
        case 'r+': return { dir: 1, k: 'same', why: 'Adding a reactant moves the position to the right, to use up some of the added reactant. Kc is unchanged: only temperature changes K.' };
        case 'r-': return { dir: -1, k: 'same', why: 'Removing a reactant moves the position to the left, to replace some of the reactant removed. Kc is unchanged.' };
        case 'q+': return { dir: -1, k: 'same', why: 'Adding a product moves the position to the left, to use up some of the added product. Kc is unchanged.' };
        case 'q-': return { dir: 1, k: 'same', why: 'Removing a product moves the position to the right, to replace some of the product removed. Kc is unchanged.' };
        default: return { dir: 0, k: 'same', why: 'A catalyst speeds up the forward and reverse reactions equally. The position and Kc do not change, but equilibrium is reached sooner.' };
      }
    }

    function apply(action) {
      const r = shiftOf(action);
      st.before = st.p;
      const step = r.small ? 0.04 : 0.13;
      st.p = Math.min(0.96, Math.max(0.04, st.p + r.dir * step));
      st.last = r;
      show();
    }

    function show() {
      const r = st.last;
      if (!r) {
        arrow.textContent = 'Press a button to make a change to the system at equilibrium.';
        kline.textContent = '';
        why.textContent = '';
      } else {
        arrow.textContent = r.dir > 0 ? 'Position moves to the right → (more products)' : (r.dir < 0 ? 'Position moves to the left ← (more reactants)' : (r.k === 'tiny' ? 'The position hardly moves' : 'No change in the position of equilibrium'));
        kline.textContent = r.k === 'up' ? 'Kc increases (only a change of temperature changes Kc).' : (r.k === 'down' ? 'Kc decreases (only a change of temperature changes Kc).' : (r.k === 'tiny' ? 'Kc hardly changes (ΔH is close to zero).' : 'Kc is unchanged.'));
        why.textContent = r.why;
      }
      if (!cvs) return;
      cvs.cv.setAttribute('aria-label', 'Bar chart of relative amounts of reactants and products before and after the change: reactants ' + Math.round((1 - st.before) * 100) + ' to ' + Math.round((1 - st.p) * 100) + ', products ' + Math.round(st.before * 100) + ' to ' + Math.round(st.p * 100) + ' (relative units).');
      cvs.redraw();
    }

    panelLc.appendChild(W.h('div', { class: 'w-note', text: 'Try: raise the pressure for the Haber process, then raise the temperature. Which change moves the position the other way? Then add a catalyst and compare it with the others.' }));

    // =================== TAB 2: Kc from data ===================
    const kc = { co: [1, 3, 2, 0], init: [1, 3, 0, 0], pick: 2, eq: 0.6, v: 2 };
    const coF = [], initF = [], names = ['A', 'B', 'C', 'D'];
    const rowCo = W.h('div', { class: 'w-row' });
    const rowInit = W.h('div', { class: 'w-row' });
    for (let i = 0; i < 4; i++) {
      coF[i] = W.field({ label: 'coefficient of ' + names[i], value: kc.co[i], type: 'number', step: 1, width: '112px', oninput: () => update() });
      initF[i] = W.field({ label: 'initial mol of ' + names[i], value: kc.init[i], type: 'number', step: 0.01, width: '112px', oninput: () => update() });
      rowCo.appendChild(coF[i].el); rowInit.appendChild(initF[i].el);
    }
    const pickSel = W.h('select', { 'aria-label': 'Species whose equilibrium amount is known' });
    const eqF = W.field({ label: 'its equilibrium amount (mol)', value: kc.eq, type: 'number', step: 0.01, width: '110px', oninput: () => update() });
    const vF = W.field({ label: 'volume (dm³)', value: kc.v, type: 'number', step: 0.1, width: '92px', oninput: () => update() });
    pickSel.onchange = () => { kc.pick = Number(pickSel.value); update(); };
    const rowEq = W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'known at equilibrium' }), pickSel), eqF.el, vF.el);
    const kcErr = W.h('div', { class: 'w-err', role: 'status' });
    const table = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0', fontSize: '.85rem' } });
    const kcOut = W.h('div', { style: { fontWeight: '700', fontSize: '1.05rem', margin: '8px 0 2px' }, role: 'status' });
    const kcExpr = W.h('div', { class: 'w-note' });
    panelKc.appendChild(W.h('div', { class: 'w-note', text: 'Species A and B are the reactants and C and D the products. Set the coefficient of D to 0 to leave it out.' }));
    panelKc.appendChild(rowCo); panelKc.appendChild(rowInit); panelKc.appendChild(rowEq);
    panelKc.appendChild(kcErr); panelKc.appendChild(table); panelKc.appendChild(kcOut); panelKc.appendChild(kcExpr);
    panelKc.appendChild(W.h('div', { class: 'w-note', text: 'The table works out how far the reaction has gone from the amount you know, then divides by the volume to get concentrations.' }));

    function readNum(f, lo, hi, what, intOnly) {
      const raw = String(f.input.value).trim();
      if (raw === '') return { err: what + ' is empty.' };
      const v = Number(raw.replace(MINUS, '-'));
      if (!isFinite(v)) return { err: what + ' must be a number.' };
      if (intOnly && Math.abs(v - Math.round(v)) > 1e-9) return { err: what + ' must be a whole number.' };
      if (v < lo || v > hi) return { err: what + ' must be between ' + lo + ' and ' + hi + '.' };
      return { v };
    }

    function update() {
      const errs = [];
      const co = [], init = [];
      for (let i = 0; i < 4; i++) {
        const lo = i === 3 ? 0 : 1;
        const c = readNum(coF[i], lo, 3, 'The coefficient of ' + names[i], true);
        if (c.err) errs.push(c.err); else co[i] = c.v;
        const n0 = readNum(initF[i], 0, 100, 'The initial amount of ' + names[i], false);
        if (n0.err) errs.push(n0.err); else init[i] = n0.v;
      }
      const v = readNum(vF, 0.01, 1000, 'The volume', false); if (v.err) errs.push(v.err);
      const e = readNum(eqF, 0, 100, 'The equilibrium amount', false); if (e.err) errs.push(e.err);
      // refresh the species choice (only species that exist)
      const present = [0, 1, 2, 3].filter(i => co[i] > 0);
      const keep = pickSel.value === '' ? kc.pick : Number(pickSel.value);
      pickSel.innerHTML = '';
      present.forEach(i => pickSel.appendChild(W.h('option', { value: String(i), text: names[i] })));
      pickSel.value = present.indexOf(keep) >= 0 ? String(keep) : String(present[0] === undefined ? 0 : present[0]);
      kc.pick = Number(pickSel.value);
      if (errs.length) { kcErr.textContent = errs.join(' '); table.innerHTML = ''; kcOut.textContent = ''; kcExpr.textContent = ''; return; }

      const nu = [-co[0], -co[1], co[2], co[3]];
      const i0 = kc.pick;
      const xi = (e.v - init[i0]) / nu[i0];
      const eqn = [0, 1, 2, 3].map(i => init[i] + nu[i] * xi);
      const neg = eqn.findIndex((x, i) => co[i] > 0 && x < -1e-9);
      if (neg >= 0) {
        kcErr.textContent = 'These numbers give a negative equilibrium amount of ' + names[neg] + ' (' + mol(eqn[neg]) + ' mol). Change the known amount or the initial amounts so that no species runs out.';
        table.innerHTML = ''; kcOut.textContent = ''; kcExpr.textContent = ''; return;
      }
      kcErr.textContent = '';
      const conc = eqn.map(x => x / v.v);
      const rows = [
        ['initial / mol', init.map((x, i) => co[i] > 0 ? mol(x) : '–')],
        ['change / mol', nu.map((x, i) => co[i] > 0 ? (x * xi >= 0 ? '+' : MINUS) + mol(Math.abs(x * xi)) : '–')],
        ['equilibrium / mol', eqn.map((x, i) => co[i] > 0 ? mol(Math.max(0, x)) : '–')],
        ['equilibrium / mol dm' + sup(-3), conc.map((x, i) => co[i] > 0 ? num3(Math.max(0, x)) : '–')]
      ];
      const t = W.h('table', {});
      const head = W.h('tr', {}, W.h('th', { text: '' }));
      [0, 1, 2, 3].forEach(i => { if (co[i] > 0) head.appendChild(W.h('th', { text: names[i] + (sys.sp[i] ? ' (' + sys.sp[i] + ')' : '') })); });
      t.appendChild(head);
      rows.forEach(r => {
        const tr = W.h('tr', {}, W.h('td', { text: r[0] }));
        [0, 1, 2, 3].forEach(i => { if (co[i] > 0) tr.appendChild(W.h('td', { text: r[1][i] })); });
        t.appendChild(tr);
      });
      table.innerHTML = ''; table.appendChild(t);

      const num = conc[2] ** co[2] * (co[3] > 0 ? conc[3] ** co[3] : 1);
      const den = conc[0] ** co[0] * conc[1] ** co[1];
      const dn = co[2] + co[3] - co[0] - co[1];
      const expr = 'Kc = ' + [2, 3].filter(i => co[i] > 0).map(i => '[' + names[i] + ']' + (co[i] > 1 ? sup(co[i]) : '')).join('') + ' / ' + [0, 1].map(i => '[' + names[i] + ']' + (co[i] > 1 ? sup(co[i]) : '')).join('');
      kcExpr.textContent = expr + '   (change in moles = ' + (dn > 0 ? '+' : (dn < 0 ? MINUS : '')) + Math.abs(dn) + ')';
      if (den === 0) {
        kcOut.textContent = 'A reactant has run out at equilibrium, so Kc cannot be calculated from these numbers.';
      } else {
        kcOut.textContent = 'Kc = ' + num3(num / den) + (dn === 0 ? ' (no unit)' : ' ' + unit(dn));
      }
    }

    // ---------- switching system and tab
    function setSystem(k) {
      key = k; sys = SYSTEMS[k];
      eqLine.textContent = eqString(sys, sys.co, sys.sp, phase(sys)) + (sys.dh < 0 ? ' ΔH negative (forward reaction exothermic)' : (sys.dh > 0 ? ' ΔH positive' : ' ΔH close to zero'));
      infoLine.textContent = sys.gas ? 'Moles of gas: ' + gasL() + ' on the left, ' + gasR() + ' on the right.' : 'All the species are liquids, so pressure has little effect.';
      st.p = sys.p0; st.before = sys.p0; st.last = null;
      btns['p+'].disabled = !sys.gas; btns['p-'].disabled = !sys.gas;
      // Kc tab preset
      kc.co = sys.co.slice(); kc.init = sys.kc.init.slice(); kc.pick = sys.kc.pick; kc.eq = sys.kc.eq; kc.v = sys.kc.v;
      for (let i = 0; i < 4; i++) { coF[i].input.value = kc.co[i]; initF[i].input.value = kc.init[i]; }
      eqF.input.value = kc.eq; vF.input.value = kc.v; pickSel.value = '';
      kc.pick = sys.kc.pick;
      update();
      show();
    }
    function setTab(t) {
      tab = t;
      panelLc.style.display = t === 'lc' ? '' : 'none';
      panelKc.style.display = t === 'kc' ? '' : 'none';
      tabLc.setAttribute('aria-selected', t === 'lc' ? 'true' : 'false');
      tabKc.setAttribute('aria-selected', t === 'kc' ? 'true' : 'false');
      if (t === 'lc') { ensureCanvas(); show(); }
    }
    tabLc.onclick = () => setTab('lc');
    tabKc.onclick = () => setTab('kc');
    sel.onchange = () => setSystem(sel.value);

    setSystem(key);
    setTab(tab);
    // start in a useful state: show the effect of the first sensible change
    if (tab === 'lc') apply(sys.gas && gasL() !== gasR() ? 'p+' : 't+');
  });
})();
