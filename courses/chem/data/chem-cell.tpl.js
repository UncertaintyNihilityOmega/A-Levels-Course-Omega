/* widgets/chem-cell.js: a standard cell built from two half-cells (cell potential, polarity, electron flow, overall equation,
   ΔG⦵) and a Nernst tab. The half-cell data (E⦵ values) are generated from FACTS.md, never typed.
   Attributes: data-left="Zn", data-right="Cu" (ids such as Zn, Cu, Ag, H (or SHE), Fe3, I2, MnO4; labels such as "Cu2+/Cu" also work),
   data-tab="cell" or "nernst". */
(function () {
  'use strict';

  /*HC*/

  const MINUS = '−';
  const F = 9.65e4;
  const SUPMAP = { '⁺': '+', '⁻': '-', '²': '2', '³': '3', '⁴': '4', '₂': '2', '₃': '3', '₄': '4', '₇': '7' };
  const norm = s => String(s).replace(/[⁺⁻²³⁴₂₃₄₇]/g, c => SUPMAP[c] || c).replace(/[\s()]/g, '').toLowerCase();
  const LOOK = {};
  HC.forEach(h => {
    [h.id, h.label, h.label.replace(/\s*\(.*\)/, '')].forEach(k => { LOOK[norm(k)] = h; });
  });
  ['she', 'h2', 'hydrogen', 'h+', 'h+/h2'].forEach(k => { LOOK[k] = HC.find(h => h.id === 'H'); });
  const find = name => LOOK[norm(name)] || null;
  const byId = id => HC.find(h => h.id === id);

  const side = list => list.map(t => (t[0] > 1 ? t[0] : '') + t[1]).join(' + ');
  const gcd = (a, b) => (b ? gcd(b, a % b) : a);
  const lcm = (a, b) => a * b / gcd(a, b);
  const sgnV = v => (Math.abs(v) < 0.005 ? '0.00' : (v < 0 ? MINUS : '+') + Math.abs(v).toFixed(2)) + ' V';
  const sgnV3 = v => (v < 0 ? MINUS : '+') + Math.abs(v).toFixed(3) + ' V';

  function overall(p, q) {   // p is reduced, q is oxidised
    const n = lcm(p.z, q.z), a = n / p.z, b = n / q.z;
    const m = new Map();
    const add = (list, mult, sign) => list.forEach(t => m.set(t[1], (m.get(t[1]) || 0) + sign * t[0] * mult));
    add(p.lhs, a, -1); add(p.rhs, a, 1); add(q.rhs, b, -1); add(q.lhs, b, 1);
    const re = [], pr = [];
    m.forEach((v, s) => { if (v < 0) re.push([-v, s]); else if (v > 0) pr.push([v, s]); });
    return { n, a, b, eq: side(re) + ' → ' + side(pr) };
  }

  W.register('chem-cell', function (el, opts) {
    const { body } = W.frame(el, 'Standard cell and Nernst equation', 'Pick two half-cells, or change a concentration');
    const msgs = [];
    const err = W.h('div', { class: 'w-err', role: 'status' });

    function pick(key, fb) {
      const raw = opts[key];
      if (raw === undefined || raw === '') return byId(fb);
      const h = find(raw);
      if (!h) { msgs.push('data-' + key + ' = "' + raw + '" is not a half-cell in this widget, so ' + byId(fb).label + ' is shown instead.'); return byId(fb); }
      return h;
    }
    const st = { left: pick('left', 'Zn'), right: pick('right', 'Cu'), tab: 'cell', nh: null, lox: 0, lred: 0 };
    if (opts.tab !== undefined && opts.tab !== '') {
      const t = String(opts.tab).toLowerCase();
      if (t === 'cell' || t === 'nernst') st.tab = t;
      else msgs.push('data-tab must be "cell" or "nernst". Showing the cell tab.');
    }
    st.nh = [st.left, st.right, byId('Cu')].find(h => h.nernst);

    // ---- tabs
    const tabs = {};
    const tabBox = W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'View' });
    [['cell', 'Cell'], ['nernst', 'Nernst']].forEach(t => {
      const b = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: t[1], onclick: () => { st.tab = t[0]; update(); } });
      tabs[t[0]] = b; tabBox.appendChild(b);
    });
    body.appendChild(tabBox);

    // ---- cell pane
    const cellPane = W.h('div', {});
    function makeSelect(label, value, onchange) {
      const sel = W.h('select', { 'aria-label': label });
      HC.forEach(h => sel.appendChild(W.h('option', { value: h.id, text: h.label + '  (' + (h.E > 0 ? '+' : (h.E < 0 ? MINUS : '')) + Math.abs(h.E).toFixed(2) + ' V)' })));
      sel.value = value;
      sel.onchange = () => onchange(sel.value);
      return { sel, el: W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: label }), sel) };
    }
    const selL = makeSelect('Left half-cell', st.left.id, v => { st.left = byId(v); update(); });
    const selR = makeSelect('Right half-cell', st.right.id, v => { st.right = byId(v); update(); });
    cellPane.appendChild(W.h('div', { class: 'w-row' }, selL.el, selR.el));

    const geo = {};
    const drawCell = function (ctx, w, h, col) {
      {
        if (!(w > 60 && h > 120)) return;
        const L = st.left, R = st.right;
        const same = L.id === R.id;
        const diff = Math.round((R.E - L.E) * 100) / 100;
        const tie = same || diff === 0;
        const rightPos = diff > 0;               // right half-cell is the positive electrode
        const bw = Math.max(80, Math.min(150, w * 0.36));
        const cxL = w * 0.27, cxR = w * 0.73;
        const wireY = 38, bridgeY = 94, bTop = 106, bBot = h - 72, liqTop = bTop + 22;
        ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.textBaseline = 'alphabetic';
        const halo = (s, x, y, align, color, font) => {
          ctx.font = font || ('12px ' + col.font); ctx.textAlign = align || 'center';
          ctx.lineWidth = 4; ctx.strokeStyle = col.card; ctx.strokeText(s, x, y);
          ctx.fillStyle = color || col.ink; ctx.fillText(s, x, y);
        };
        const fit = (s, x, y, color, maxw) => {
          let fs = 12; ctx.font = fs + 'px ' + col.font;
          while (fs > 8 && ctx.measureText(s).width > maxw) { fs -= 1; ctx.font = fs + 'px ' + col.font; }
          halo(s, x, y, 'center', color, fs + 'px ' + col.font);
        };
        // beakers and liquids
        [[cxL, L], [cxR, R]].forEach(pair => {
          const cx = pair[0];
          ctx.fillStyle = col.sc2; ctx.globalAlpha = 0.16;
          ctx.fillRect(cx - bw / 2, liqTop, bw, bBot - liqTop); ctx.globalAlpha = 1;
          ctx.strokeStyle = col.ink2; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(cx - bw / 2, bTop); ctx.lineTo(cx - bw / 2, bBot); ctx.lineTo(cx + bw / 2, bBot); ctx.lineTo(cx + bw / 2, bTop); ctx.stroke();
        });
        // electrodes
        const exL = cxL - bw * 0.14, exR = cxR + bw * 0.14;
        ctx.fillStyle = col.ink3;
        ctx.fillRect(exL - 3.5, 62, 7, bBot - 16 - 62);
        ctx.fillRect(exR - 3.5, 62, 7, bBot - 16 - 62);
        // salt bridge (hollow U tube)
        const bxL = cxL + bw * 0.30, bxR = cxR - bw * 0.30, bLow = liqTop + 34;
        const uPath = () => { ctx.beginPath(); ctx.moveTo(bxL, bLow); ctx.lineTo(bxL, bridgeY + 8); ctx.quadraticCurveTo(bxL, bridgeY, bxL + 8, bridgeY); ctx.lineTo(bxR - 8, bridgeY); ctx.quadraticCurveTo(bxR, bridgeY, bxR, bridgeY + 8); ctx.lineTo(bxR, bLow); };
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 10; uPath(); ctx.stroke();
        ctx.strokeStyle = col.card; ctx.lineWidth = 6; uPath(); ctx.stroke();
        halo('salt bridge', w / 2, bridgeY - 14, 'center', col.ink2);
        // wires and voltmeter
        const mr = 24, mx = w / 2;
        ctx.strokeStyle = col.ink; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(exL, 62); ctx.lineTo(exL, wireY); ctx.lineTo(mx - mr, wireY); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(exR, 62); ctx.lineTo(exR, wireY); ctx.lineTo(mx + mr, wireY); ctx.stroke();
        ctx.fillStyle = col.card; ctx.beginPath(); ctx.arc(mx, wireY, mr, 0, 6.2832); ctx.fill(); ctx.stroke();
        halo((tie ? '0.00' : Math.abs(diff).toFixed(2)) + ' V', mx, wireY + 4, 'center', col.ink, 'bold 12px ' + col.font);
        // polarity signs and electron arrows
        if (!tie) {
          const xNeg = rightPos ? exL : exR, xPos = rightPos ? exR : exL;
          halo(MINUS, xNeg + (rightPos ? -11 : 11), 56, 'center', col.sc, 'bold 15px ' + col.font);
          halo('+', xPos + (rightPos ? 11 : -11), 56, 'center', col.red, 'bold 15px ' + col.font);
          const dir = rightPos ? 1 : -1;            // electrons flow from the negative electrode to the positive one
          ctx.strokeStyle = col.red; ctx.lineWidth = 2;
          [[xNeg, mx - dir * mr], [mx + dir * mr, xPos]].forEach(seg => {
            const xm = (seg[0] + seg[1]) / 2;
            if (Math.abs(seg[1] - seg[0]) > 26) {
              ctx.beginPath(); ctx.moveTo(xm - dir * 7, wireY - 5); ctx.lineTo(xm, wireY); ctx.lineTo(xm - dir * 7, wireY + 5); ctx.stroke();
            }
          });
          halo('e⁻', (xNeg + mx - dir * mr) / 2, wireY - 10, 'center', col.red);
        }
        // labels under each beaker
        [[cxL, L, rightPos], [cxR, R, !rightPos]].forEach(t => {
          const cx = t[0], hc = t[1], isNeg = t[2];
          const maxw = w * 0.46;
          fit(hc.elec, cx, bBot + 16, col.ink, maxw);
          fit(hc.sol, cx, bBot + 31, col.ink2, maxw);
          if (!tie) fit(isNeg ? MINUS + ' oxidation' : '+ reduction', cx, bBot + 47, isNeg ? col.sc : col.red, maxw);
        });
        fit('all ions 1.00 mol dm⁻³, gases 101 kPa, 298 K', w / 2, h - 6, col.ink2, w - 12);
        geo.label = 'Cell: ' + L.label + ' and ' + R.label + (tie ? ', no potential difference' : ', cell voltage ' + Math.abs(diff).toFixed(2) + ' V');
      }
    };
    const read = W.readout([['pos', 'Positive electrode'], ['neg', 'Negative electrode'], ['flow', 'Electrons flow'], ['ecell', 'E⦵cell'], ['eq', 'Overall equation'], ['dg', 'ΔG⦵ = −nFE⦵cell'], ['feas', 'Feasible?']]);
    const cellOut = W.h('div', {}, read.el);
    const note1 = W.h('div', { class: 'w-note', text: 'Try Zn and Cu, then swap them over: the voltage stays the same but the positive electrode moves to the other side. Then choose two ion half-cells such as Fe³⁺/Fe²⁺ and I₂/I⁻.' });
    cellOut.appendChild(note1);
    body.appendChild(cellPane);

    // ---- Nernst pane
    const nPane = W.h('div', {});
    const nOpts = HC.filter(h => h.nernst);
    const selN = W.h('select', { 'aria-label': 'Half-cell for the Nernst equation' });
    nOpts.forEach(h => selN.appendChild(W.h('option', { value: h.id, text: h.label + '  (E⦵ ' + (h.E < 0 ? MINUS : '+') + Math.abs(h.E).toFixed(2) + ' V, z = ' + h.z + ')' })));
    selN.value = st.nh.id;
    selN.onchange = () => { st.nh = byId(selN.value); update(); };
    nPane.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Half-cell' }), selN)));
    const concFmt = v => W.fmt(Math.pow(10, v), 3) + ' mol dm⁻³';
    const sOx = W.slider({ label: 'Concentration of the oxidised form', min: -4, max: 1, step: 0.1, value: 0, fmt: concFmt, oninput: v => { st.lox = v; update(); } });
    const sRed = W.slider({ label: 'Concentration of the reduced form', min: -4, max: 1, step: 0.1, value: 0, fmt: concFmt, oninput: v => { st.lred = v; update(); } });
    const redWrap = W.h('div', {}, sRed.el);
    const solidNote = W.h('div', { class: 'w-note', text: 'The reduced form is the solid metal, so its concentration is taken as 1.' });
    nPane.appendChild(sOx.el); nPane.appendChild(redWrap); nPane.appendChild(solidNote);
    const nGeo = {};
    const drawNernst = function (ctx, w, h, col) {
      {
        if (!(w > 80 && h > 80)) return;
        const hc = st.nh, k = 0.059 / hc.z;
        const redLog = hc.kind === 'metal' ? 0 : st.lred;
        const x0 = -4.5, x1 = 1.5;
        const eAt = x => hc.E + k * (x - redLog);
        let ylo = Math.min(eAt(x0), eAt(x1), hc.E), yhi = Math.max(eAt(x0), eAt(x1), hc.E);
        const padY = Math.max(0.02, (yhi - ylo) * 0.12); ylo -= padY; yhi += padY;
        const M = { l: 48, r: 14, t: 16, b: 38 };
        const X = x => M.l + (w - M.l - M.r) * (x - x0) / (x1 - x0);
        const Y = e => h - M.b - (h - M.b - M.t) * (e - ylo) / (yhi - ylo);
        ctx.font = '11px ' + col.font; ctx.textBaseline = 'alphabetic'; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
        ctx.lineWidth = 1; ctx.strokeStyle = col.rule; ctx.fillStyle = col.ink2;
        for (let x = -4; x <= 1; x++) {
          ctx.beginPath(); ctx.moveTo(X(x), h - M.b); ctx.lineTo(X(x), M.t); ctx.stroke();
          ctx.textAlign = 'center'; ctx.fillText(String(x).replace('-', MINUS), X(x), h - M.b + 14);
        }
        let yt = W.ticks(ylo, yhi, 4);
        if (!Array.isArray(yt) || !yt.length) yt = [ylo, (ylo + yhi) / 2, yhi];
        yt.forEach(v => {
          if (v < ylo || v > yhi) return;
          ctx.beginPath(); ctx.moveTo(M.l, Y(v)); ctx.lineTo(w - M.r, Y(v)); ctx.stroke();
          ctx.textAlign = 'right'; ctx.fillText(W.fix(v, 2).replace('-', MINUS), M.l - 5, Y(v) + 4);
        });
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(M.l, M.t); ctx.lineTo(M.l, h - M.b); ctx.lineTo(w - M.r, h - M.b); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ctx.fillText('log₁₀([oxidised] / mol dm⁻³)', (M.l + w - M.r) / 2, h - 6);
        ctx.textAlign = 'left'; ctx.fillText('E / V', 6, 12);
        ctx.save(); ctx.beginPath(); ctx.rect(M.l, M.t, w - M.l - M.r, h - M.t - M.b); ctx.clip();
        // E⦵ guide
        ctx.setLineDash([5, 4]); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(M.l, Y(hc.E)); ctx.lineTo(w - M.r, Y(hc.E)); ctx.stroke(); ctx.setLineDash([]);
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.6;
        ctx.beginPath(); ctx.moveTo(X(x0), Y(eAt(x0))); ctx.lineTo(X(x1), Y(eAt(x1))); ctx.stroke();
        const px = X(st.lox), py = Y(eAt(st.lox));
        ctx.strokeStyle = col.red; ctx.lineWidth = 1.2; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(px, h - M.b); ctx.lineTo(px, py); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(px, py, 5, 0, 6.2832); ctx.fill();
        ctx.restore();
        ctx.font = '12px ' + col.font; ctx.lineWidth = 4; ctx.strokeStyle = col.card;
        const lab = 'E⦵ = ' + sgnV(hc.E);
        ctx.textAlign = 'right'; ctx.strokeText(lab, w - M.r - 2, Y(hc.E) - 5 > M.t + 10 ? Y(hc.E) - 5 : Y(hc.E) + 14);
        ctx.fillStyle = col.ink2; ctx.fillText(lab, w - M.r - 2, Y(hc.E) - 5 > M.t + 10 ? Y(hc.E) - 5 : Y(hc.E) + 14);
        nGeo.label = 'Graph of E against log of the oxidised concentration for ' + hc.label + ': a straight line, currently ' + sgnV3(eAt(st.lox));
      }
    };
    const read2 = W.readout([['eq', 'Half-equation'], ['e0', 'E⦵'], ['ratio', '[oxidised] / [reduced]'], ['e', 'E = E⦵ + (0.059/z) log([ox]/[red])']]);
    const nOut = W.h('div', {}, read2.el);
    nOut.appendChild(W.h('div', { class: 'w-note', text: 'Each tenfold change in the concentration of the oxidised form moves E by 0.059/z volts. At 1.00 mol dm⁻³ (and 1.00 for the reduced form) E equals E⦵.' }));
    body.appendChild(nPane);
    const cv = W.canvas(body, { height: 280, draw(ctx, w, h, col) { if (st.tab === 'cell') drawCell(ctx, w, h, col); else drawNernst(ctx, w, h, col); } });
    cv.cv.setAttribute('role', 'img');
    const cv2 = cv;
    body.appendChild(cellOut);
    body.appendChild(nOut);
    body.appendChild(err);

    function update() {
      Object.keys(tabs).forEach(k => tabs[k].setAttribute('aria-selected', String(k === st.tab)));
      cellPane.style.display = st.tab === 'cell' ? '' : 'none';
      nPane.style.display = st.tab === 'nernst' ? '' : 'none';
      cellOut.style.display = st.tab === 'cell' ? '' : 'none';
      nOut.style.display = st.tab === 'nernst' ? '' : 'none';
      err.textContent = msgs.join(' ');
      if (st.tab === 'cell') {
        const L = st.left, R = st.right;
        selL.sel.value = L.id; selR.sel.value = R.id;
        const same = L.id === R.id;
        const diff = Math.round((R.E - L.E) * 100) / 100;
        if (same) {
          read.set('pos', '—'); read.set('neg', '—'); read.set('flow', 'no electrons flow');
          read.set('ecell', '0.00 V (same half-cell on both sides: no potential difference)');
          read.set('eq', 'none'); read.set('dg', '0 kJ mol⁻¹'); read.set('feas', 'there is no reaction');
        } else {
          const p = diff >= 0 ? R : L, q = diff >= 0 ? L : R;
          const o = overall(p, q);
          const ec = Math.round((p.E - q.E) * 100) / 100;
          read.set('pos', p.label + '  (E⦵ ' + sgnV(p.E) + ', reduction)');
          read.set('neg', q.label + '  (E⦵ ' + sgnV(q.E) + ', oxidation)');
          read.set('flow', 'in the wire, from the ' + q.label + ' half-cell to the ' + p.label + ' half-cell');
          read.set('ecell', sgnV(p.E) + ' − (' + sgnV(q.E) + ') = ' + sgnV(ec));
          read.set('eq', o.eq + '   (n = ' + o.n + (o.n === 1 ? ' electron)' : ' electrons)'));
          const dg = -o.n * F * ec / 1000;
          read.set('dg', ec === 0 ? '0 kJ mol⁻¹' : (dg < 0 ? MINUS : '+') + W.fmt(Math.abs(dg), 3) + ' kJ mol⁻¹   (n = ' + o.n + ', F = 9.65 × 10⁴ C mol⁻¹)');
          read.set('feas', ec > 0 ? 'yes under standard conditions (E⦵cell is positive), though it may be slow' : 'the two E⦵ values are equal, so neither direction is favoured');
        }
        cv.cv.setAttribute('aria-label', geo.label || 'Cell diagram');
        cv.redraw();
      } else {
        const hc = st.nh, k = 0.059 / hc.z;
        const isMetal = hc.kind === 'metal';
        redWrap.style.display = isMetal ? 'none' : '';
        solidNote.style.display = isMetal ? '' : 'none';
        const redLog = isMetal ? 0 : st.lred;
        const E = hc.E + k * (st.lox - redLog);
        read2.set('eq', side(hc.lhs) + ' + ' + (hc.z === 1 ? '' : hc.z) + 'e⁻ ⇌ ' + side(hc.rhs));
        read2.set('e0', sgnV(hc.E) + '   (z = ' + hc.z + ')');
        read2.set('ratio', W.fmt(Math.pow(10, st.lox), 3) + ' / ' + (isMetal ? '1 (solid)' : W.fmt(Math.pow(10, redLog), 3)));
        read2.set('e', sgnV3(E) + '   (' + sgnV(hc.E) + ' + ' + W.fmt(k, 3) + ' × ' + W.fix(st.lox - redLog, 1).replace('-', MINUS) + ')');
        cv2.cv.setAttribute('aria-label', nGeo.label || 'Nernst graph');
        cv2.redraw();
      }
    }
    update();
  });
})();
