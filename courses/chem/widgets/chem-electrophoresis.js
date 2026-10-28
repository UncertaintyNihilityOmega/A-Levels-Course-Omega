/* widgets/chem-electrophoresis.js: electrophoresis of amino acids on a strip at a chosen pH.
   Attributes: data-ph="7" (1 to 13), data-mix="gly,lys,asp" (any of gly, ala, lys, asp, glu).
   Net charge comes from typical group pKa values (an approximate model, not exam data); at the isoelectric point it is zero.
   Distance moved is proportional to charge divided by (relative size)^(2/3), so a bigger charge moves further and a
   bigger molecule moves less. Positive species move to the cathode (left), negative species to the anode (right). */
(function () {
  'use strict';

  // a = acidic group (COOH, loses H+ to become -1), b = basic group (NH3+, +1 until it loses H+); pKa values are typical textbook values
  const AA = {
    gly: { name: 'Glycine', short: 'Gly', pI: 5.97, mr: 75.0, g: [['a', 2.34], ['b', 9.60]] },
    ala: { name: 'Alanine', short: 'Ala', pI: 6.00, mr: 89.0, g: [['a', 2.34], ['b', 9.66]] },
    lys: { name: 'Lysine', short: 'Lys', pI: 9.74, mr: 146.0, g: [['a', 2.18], ['b', 8.95], ['b', 10.53]] },
    asp: { name: 'Aspartic acid', short: 'Asp', pI: 2.77, mr: 133.0, g: [['a', 1.88], ['a', 3.65], ['b', 9.60]] },
    glu: { name: 'Glutamic acid', short: 'Glu', pI: 3.22, mr: 147.0, g: [['a', 2.19], ['a', 4.25], ['b', 9.67]] }
  };
  const ORDER = ['gly', 'ala', 'lys', 'asp', 'glu'];
  const DEFAULT_MIX = ['gly', 'lys', 'asp'];
  const VMAX = 2 / Math.pow(133.0, 2 / 3);        // the largest speed in the model (aspartic acid, charge -2), used to scale distances

  function charge(a, ph) {
    let q = 0;
    a.g.forEach(([t, pk]) => {
      if (t === 'b') q += 1 / (1 + Math.pow(10, ph - pk));
      else q -= 1 / (1 + Math.pow(10, pk - ph));
    });
    return q;
  }
  function speed(a, ph) { return charge(a, ph) / Math.pow(a.mr, 2 / 3); }
  function signed(x) { const s = W.fix(Math.abs(x) < 0.005 ? 0 : x, 2); return (x > 0.004 ? '+' : '') + s; }

  W.register('chem-electrophoresis', function (el, opts) {
    const { body } = W.frame(el, 'Electrophoresis of amino acids', 'Choose a mixture and a pH, then run the strip');
    const msgs = [];
    const get = k => (opts[k] === undefined ? '' : String(opts[k]).trim());

    let ph = 7;
    if (get('ph') !== '') {
      const v = Number(get('ph'));
      if (!isFinite(v)) msgs.push('data-ph must be a number from 1 to 13. Showing pH 7.');
      else if (v < 1 || v > 13) { ph = Math.min(13, Math.max(1, v)); msgs.push('data-ph must be between 1 and 13. Showing pH ' + ph + '.'); }
      else ph = Math.round(v * 10) / 10;
    }
    let mix = DEFAULT_MIX.slice();
    if (get('mix') !== '') {
      const parts = get('mix').toLowerCase().split(/[\s,;]+/).filter(Boolean);
      const good = [], bad = [];
      parts.forEach(p => { if (AA[p]) { if (good.indexOf(p) < 0) good.push(p); } else bad.push(p.slice(0, 10)); });
      if (bad.length) msgs.push('data-mix has unknown codes (' + W.esc(bad.join(', ')) + '). Use gly, ala, lys, asp or glu.');
      if (good.length) mix = ORDER.filter(k => good.indexOf(k) >= 0); else if (bad.length) msgs.push('Showing glycine, lysine and aspartic acid.');
    }

    const err = W.h('div', { class: 'w-err', role: 'status' });

    // controls
    const sl = W.slider({ label: 'pH of the buffer', min: 1, max: 13, step: 0.1, value: ph, fmt: v => W.fix(Number(v), 1), oninput: v => { ph = Number(sl.input.value); msgs.length = 0; update(true); } });
    body.appendChild(W.h('div', { class: 'w-row' }, sl.el));
    const boxes = {};
    const boxRow = W.h('div', { class: 'w-row' });
    ORDER.forEach(k => {
      const cb = W.h('input', { type: 'checkbox' });
      cb.checked = mix.indexOf(k) >= 0;
      cb.addEventListener('change', () => {
        mix = ORDER.filter(x => boxes[x].checked);
        msgs.length = 0;
        update(true);
      });
      boxes[k] = cb;
      boxRow.appendChild(W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, cb, W.h('span', { class: 'w-lab', text: AA[k].name })));
    });
    body.appendChild(boxRow);
    const runBtn = W.h('button', { class: 'btn btn-sm', type: 'button', text: 'Run' });
    const resetBtn = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: 'Back to the start line' });
    body.appendChild(W.h('div', { class: 'w-row' }, runBtn, resetBtn));
    body.appendChild(err);

    // state
    let progress = 1, t0 = 0;

    const ease = p => (p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2);
    const cvs = W.canvas(body, {
      height: 176,
      draw(ctx, w, h, col) {
        if (!(w > 120) || !(h > 80)) return;                   // survives zero size
        const padX = 38, stripY = 68, stripH = 46;
        const x0 = padX, x1 = w - padX, xm = (x0 + x1) / 2, half = (x1 - x0) / 2 - 14;
        ctx.textBaseline = 'alphabetic';
        // strip
        ctx.fillStyle = col.card; ctx.strokeStyle = col.rule2; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.rect(x0, stripY, x1 - x0, stripH); ctx.fill(); ctx.stroke();
        // electrodes
        ctx.fillStyle = col.ink3;
        ctx.fillRect(x0 - 12, stripY - 8, 8, stripH + 16);
        ctx.fillRect(x1 + 4, stripY - 8, 8, stripH + 16);
        ctx.fillStyle = col.ink; ctx.font = 'bold 14px ' + col.font; ctx.textAlign = 'center';
        ctx.fillText('−', x0 - 8, stripY - 14);
        ctx.fillText('+', x1 + 8, stripY - 14);
        ctx.font = '11px ' + col.font; ctx.fillStyle = col.ink2;
        ctx.fillText('cathode', x0 - 8, stripY + stripH + 22);
        ctx.fillText('anode', x1 + 8, stripY + stripH + 22);
        // start line
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 3]);
        ctx.beginPath(); ctx.moveTo(xm, stripY - 4); ctx.lineTo(xm, stripY + stripH + 4); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ctx.fillText('start line', xm, stripY + stripH + 22);
        // spots
        const cols = [col.sc, col.sc2, col.red, col.ok, col.ink2];
        const pr = ease(Math.max(0, Math.min(1, progress)));
        const n = mix.length;
        const placed = [];
        mix.forEach((k, i) => {
          const a = AA[k];
          const frac = Math.max(-0.95, Math.min(0.95, speed(a, ph) / VMAX * 1.2));
          // a positive charge (frac > 0) moves LEFT to the cathode, a negative charge moves RIGHT to the anode
          const px = xm - frac * half * pr;
          const py = stripY + stripH / 2;
          ctx.fillStyle = cols[ORDER.indexOf(k) % cols.length];
          ctx.beginPath(); ctx.arc(px, py, 8, 0, Math.PI * 2); ctx.fill();
          ctx.strokeStyle = col.ink; ctx.lineWidth = 1; ctx.stroke();
          // each label sits above its own spot; spots that sit close together get labels on higher rows
          let lvl = 0;
          while (lvl < 3 && placed.some(p => p.l === lvl && Math.abs(p.x - px) < 34)) lvl++;
          if (lvl >= 3) lvl = i % 3;
          placed.push({ x: px, l: lvl });
          ctx.fillStyle = col.ink; ctx.font = '12px ' + col.font; ctx.textAlign = 'center';
          ctx.fillText(a.short, px, stripY - 14 - 16 * lvl);
        });
        if (n === 0) {
          ctx.fillStyle = col.ink2; ctx.textAlign = 'center'; ctx.font = '12px ' + col.font;
          ctx.fillText('choose at least one amino acid', xm, stripY + stripH / 2 + 4);
        }
        // pH label
        ctx.fillStyle = col.ink2; ctx.textAlign = 'left'; ctx.font = '12px ' + col.font;
        ctx.fillText('buffer at pH ' + W.fix(ph, 1), 4, h - 8);
      }
    });
    cvs.cv.setAttribute('role', 'img');
    cvs.describe = () => {
      if (!mix.length) return 'An empty strip: no amino acid chosen.';
      const spots = mix.map(k => {
        const q = charge(AA[k], ph);
        if (progress < 0.01) return AA[k].name + ' on the start line';
        return AA[k].name + (Math.abs(q) < 0.01 ? ' stays at the start line' : q > 0 ? ' has moved left towards the cathode' : ' has moved right towards the anode');
      });
      return 'A strip with the cathode (−) on the left, the anode (+) on the right and a start line in the middle, in a buffer at pH ' + W.fix(ph, 1) + '. ' + spots.join('; ') + '.';
    };

    const read = W.readout(ORDER.map(k => [k, AA[k].name]));
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Try pH 1, then 7, then 13. Positive species move to the cathode (−) and negative species to the anode (+). Set the pH to an isoelectric point (for example 5.97 for glycine) and that spot stays on the start line. Charges are approximate (typical group pKa values), and the distance moved depends on both charge and size.' }));

    const anim = W.animate(() => {
      const p = Math.min(1, (performance.now() - t0) / 2200);
      progress = p;
      cvs.redraw();
      if (p >= 1) W.say(body, 'Run finished at pH ' + W.fix(ph, 1) + '. ' + (cvs.describe() || ''));
      return p < 1;
    }, { still() { progress = 1; cvs.redraw(); W.say(body, 'Run finished at pH ' + W.fix(ph, 1) + '. ' + cvs.describe()); } });

    function describe(k) {
      const a = AA[k], q = charge(a, ph);
      let how;
      const small = Math.abs(q) < 0.3;
      if (Math.abs(q) < 0.01) how = 'no net charge: stays at the start line';
      else if (q > 0) how = (small ? 'slightly ' : '') + 'positive: moves ' + (small ? 'slowly ' : '') + 'towards the cathode (−)' + (q > 1.5 ? ', fast' : '');
      else how = (small ? 'slightly ' : '') + 'negative: moves ' + (small ? 'slowly ' : '') + 'towards the anode (+)' + (q < -1.5 ? ', fast' : '');
      return 'isoelectric point (about) ' + W.fix(a.pI, 2) + '; charge (approximate) ' + signed(q) + ': ' + how;
    }

    function update(reset) {
      sl.set(ph);
      ORDER.forEach(k => { boxes[k].checked = mix.indexOf(k) >= 0; });
      ORDER.forEach(k => read.set(k, mix.indexOf(k) >= 0 ? describe(k) : 'not in the mixture'));
      err.textContent = msgs.join(' ');
      progress = 1;
      cvs.setLabel('Electrophoresis strip at pH ' + W.fix(ph, 1) + ' with ' + (mix.length ? mix.map(k => AA[k].name).join(', ') : 'no amino acids'));
      cvs.redraw();
    }
    runBtn.addEventListener('click', () => { progress = 0; t0 = performance.now(); anim.start(); });
    resetBtn.addEventListener('click', () => { anim.stop(); progress = 0; cvs.redraw(); });
    update(false);
  });
})();
