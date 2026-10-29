/* widgets/bio-sarcomere.js: one sarcomere drawn to scale. Used in bio.synapses.
   Model filament lengths (stated on screen): thin (actin) filaments 1.0 um from each Z line; thick (myosin) filaments 1.6 um, centred on the
   M line. So A band = 1.6 um, I band = L - 1.6, H zone = max(0, L - 2.0) and the overlap of thin and thick filaments (both ends) = 3.6 - L (at most 1.6, the A band, when the thin filaments meet or overlap below 2.0 um).
   Rules: without calcium ions tropomyosin blocks the binding sites, so the sarcomere cannot shorten below its relaxed length (data-len);
   with calcium ions and ATP it can shorten or relax freely; with calcium ions but no ATP the heads stay attached (rigor): length is frozen.
   Attributes: data-len = relaxed length in um (default 2.5, 2.2 to 3.0); data-start (starting length), data-ca="1", data-atp="0" set the starting state. Pure functions exported for data/test_bio-sarcomere.js. */
(function () {
  'use strict';

  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const numOr = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? clamp(x, lo, hi) : d; };
  const THIN = 1.0, THICK = 1.6, LMIN = 1.8, LMAX = 3.4;

  function bands(L) {
    return {
      A: THICK,
      I: Math.max(0, L - THICK),
      H: Math.max(0, L - 2 * THIN),
      overlap: Math.min(THICK, 2 * Math.max(0, Math.min(THIN, L / 2 + THICK / 2) - Math.max(0, L / 2 - THICK / 2)))
    };
  }
  // effective length for the slider value L, the relaxed length L0, calcium and ATP; hold = length frozen in rigor
  function effLen(L, L0, ca, atp, hold) {
    if (!isFinite(L)) L = L0;
    L = clamp(L, LMIN, LMAX);
    if (!ca) return { len: Math.max(L, L0), mode: 'relaxed' };
    if (!atp) return { len: isFinite(hold) ? clamp(hold, LMIN, LMAX) : Math.max(L, L0), mode: 'rigor' };
    return { len: L, mode: 'active' };
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { bands, effLen, numOr, clamp, THIN, THICK, LMIN, LMAX };
  if (typeof W === 'undefined') return;

  W.register('bio-sarcomere', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'A sarcomere in a muscle', 'A model drawn to scale: change the length and read the bands');
    const L0 = numOr(opts.len, 2.5, 2.2, 3.0);
    const S = { L: numOr(opts.start, L0, LMIN, LMAX), ca: opts.ca === '1', atp: opts.atp !== '0', hold: NaN };
    if (S.ca && !S.atp) S.hold = S.L;

    function cur() { return effLen(S.L, L0, S.ca, S.atp, S.hold); }

    function tag(ctx, c, txt, x, y, align, color, size) {
      ctx.save();
      ctx.font = (size || 12) + 'px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'center'; ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }
    function bracket(ctx, c, x0, x1, y, up) {
      ctx.save(); ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.2;
      const d = up ? 5 : -5;
      ctx.beginPath(); ctx.moveTo(x0, y + d); ctx.lineTo(x0, y); ctx.lineTo(x1, y); ctx.lineTo(x1, y + d); ctx.stroke();
      ctx.restore();
    }

    function describe() {
      const e = cur(), b = bands(e.len);
      return 'Drawing of one sarcomere between two Z lines, ' + e.len.toFixed(2) + ' micrometres long, with thin actin filaments from each Z line and thick myosin filaments in the middle. ' +
        'The I band is ' + b.I.toFixed(2) + ' micrometres, the A band ' + b.A.toFixed(2) + ' and the H zone ' + b.H.toFixed(2) + '. ' +
        (S.ca ? (S.atp ? 'Calcium ions are present: tropomyosin is moved aside and myosin heads form cross-bridges.' : 'Calcium ions are present but there is no ATP: the heads stay attached (rigor).') : 'No calcium ions: tropomyosin covers the binding sites and no cross-bridges form.');
    }

    function draw(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 200 || h < 170) return;
      const pad = 22, s = (w - 2 * pad) / LMAX, cx = w / 2;
      const e = cur(), L = e.len, b = bands(L);
      const Zl = cx - L * s / 2, Zr = cx + L * s / 2;
      const A0 = cx - THICK * s / 2, A1 = cx + THICK * s / 2;
      const kv = clamp(s / 60, 1, 2);
      const yTop = 70, rowsThin = [yTop, yTop + 22 * kv, yTop + 44 * kv], rowsThick = [yTop + 11 * kv, yTop + 33 * kv];
      const zTop = yTop - 18, zBot = yTop + 44 * kv + 12;
      // brackets and letters
      if (b.H > 0.02) { bracket(ctx, c, cx - b.H * s / 2, cx + b.H * s / 2, 20, true); tag(ctx, c, 'H', cx, 15, 'center', c.ink, 13); }
      [[Zl, A0, 'I'], [A0, A1, 'A'], [A1, Zr, 'I']].forEach(function (t) {
        if (t[1] - t[0] > 3) { bracket(ctx, c, t[0], t[1], 46, true); tag(ctx, c, t[2], (t[0] + t[1]) / 2, 40, 'center', c.ink, 13); }
      });
      // thin filaments (with binding sites and tropomyosin)
      const dirs = [[Zl, 1], [Zr, -1]];
      rowsThin.forEach(function (y) {
        dirs.forEach(function (d) {
          const x0 = d[0], x1 = d[0] + d[1] * THIN * s;
          ctx.save();
          ctx.strokeStyle = c.sc2; ctx.lineWidth = 2.5;
          ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
          ctx.strokeStyle = c.sc2; ctx.lineWidth = 1;
          for (let k = 1; k * 9 < THIN * s; k++) { const x = x0 + d[1] * k * 9; ctx.beginPath(); ctx.moveTo(x, y - 3); ctx.lineTo(x, y + 3); ctx.stroke(); }
          // tropomyosin: over the filament when there is no calcium, pulled to the side when calcium is bound to troponin
          ctx.strokeStyle = c.ink3; ctx.lineWidth = 3.5; ctx.lineCap = 'round';
          if (!S.ca) { ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke(); }
          else { ctx.setLineDash([2, 6]); ctx.beginPath(); ctx.moveTo(x0, y + 4 * kv + 2); ctx.lineTo(x1, y + 4 * kv + 2); ctx.stroke(); }
          ctx.restore();
        });
      });
      // thick filaments with heads
      rowsThick.forEach(function (y, ri) {
        ctx.save();
        ctx.fillStyle = c.card; ctx.strokeStyle = c.sc; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.rect(A0, y - 4, A1 - A0, 8); ctx.fill(); ctx.stroke();
        ctx.lineWidth = 1.5;
        let k = 0;
        for (let x = A0 + 5; x < A1 - 2; x += 9, k++) {
          if (Math.abs(x - cx) < 0.1 * s) continue;                     // bare zone
          const left = x < cx, inOverlap = left ? (x <= Zl + THIN * s) : (x >= Zr - THIN * s);
          const up = (k % 2 === 0);
          const edge = y + (up ? -4 : 4), ty = y + (up ? -11 * kv : 11 * kv);
          ctx.strokeStyle = c.sc;
          ctx.beginPath(); ctx.moveTo(x, edge);
          if (S.ca && inOverlap) ctx.lineTo(x + (left ? -4 : 4), ty); else ctx.lineTo(x, y + (up ? -4 - 3 * kv : 4 + 3 * kv));
          ctx.stroke();
        }
        ctx.restore();
      });
      // Z lines and M line
      ctx.save();
      ctx.strokeStyle = c.ink; ctx.lineWidth = 4; ctx.lineCap = 'butt';
      [Zl, Zr].forEach(function (x) { ctx.beginPath(); ctx.moveTo(x, zTop + 8); ctx.lineTo(x, zBot); ctx.stroke(); });
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.2; ctx.setLineDash([4, 3]);
      ctx.beginPath(); ctx.moveTo(cx, zTop + 8); ctx.lineTo(cx, zBot); ctx.stroke();
      ctx.restore();
      const yl = zBot + 18;
      tag(ctx, c, 'Z line', Zl, yl, 'center', c.ink2, 11);
      tag(ctx, c, 'Z line', Zr, yl, 'center', c.ink2, 11);
      tag(ctx, c, 'M line', cx, yl + 14, 'center', c.ink2, 11);
      // length arrow
      const ya = yl + 42;
      ctx.save(); ctx.strokeStyle = c.red; ctx.fillStyle = c.red; ctx.lineWidth = 1.8;
      ctx.beginPath(); ctx.moveTo(Zl + 4, ya); ctx.lineTo(Zr - 4, ya); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(Zl, ya); ctx.lineTo(Zl + 8, ya - 4); ctx.lineTo(Zl + 8, ya + 4); ctx.closePath(); ctx.fill();
      ctx.beginPath(); ctx.moveTo(Zr, ya); ctx.lineTo(Zr - 8, ya - 4); ctx.lineTo(Zr - 8, ya + 4); ctx.closePath(); ctx.fill();
      ctx.restore();
      tag(ctx, c, 'sarcomere ' + L.toFixed(2) + ' µm', cx, ya - 7, 'center', c.red, 12);
    }

    const cv = W.canvas(body, {
      height: 250,
      label: 'Drawing of one sarcomere to scale with its bands labelled, showing thin and thick filaments and the effect of calcium ions and ATP',
      describe: describe,
      draw: draw
    });

    const sl = W.sliderNum({ label: 'Sarcomere length / µm (short: contracted, long: stretched)', min: LMIN, max: LMAX, step: 0.05, value: S.L,
      oninput: function () { S.L = numOr(sl.get(), L0, LMIN, LMAX); update(true); } });
    body.appendChild(W.h('div', { class: 'w-row' }, sl.el));

    function check(label, onchange) {
      const input = W.h('input', { type: 'checkbox' });
      input.onchange = function () { onchange(input.checked); };
      const lab = W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, input, W.h('span', { class: 'w-lab', text: label }));
      return { el: lab, input: input };
    }
    const cCa = check('Calcium ions present (troponin binds them)', function (v) {
      S.ca = v;
      if (!v) { S.hold = NaN; S.L = Math.max(S.L, L0); sl.set(S.L); }
      update(true);
    });
    const cAtp = check('ATP available', function (v) {
      if (!v) S.hold = cur().len; else S.hold = NaN;
      S.atp = v; update(true);
    });
    cAtp.input.checked = S.atp; cCa.input.checked = S.ca;
    body.appendChild(W.h('div', { class: 'w-row' }, cCa.el, cAtp.el));

    const ro = W.readout([['L', 'Sarcomere (Z line to Z line)'], ['I', 'I band (actin only)'], ['A', 'A band (myosin filaments)'], ['H', 'H zone (myosin only)'], ['O', 'Thin and thick overlap']]);
    body.appendChild(ro.el);
    const msg = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.appendChild(msg);
    body.appendChild(W.h('div', { class: 'w-note', text: 'A model drawn to scale, using these filament lengths: thin (actin) filaments 1.0 µm from each Z line, thick (myosin) filaments 1.6 µm. Try: (1) with no calcium, slide to the shortest length; (2) switch calcium on and shorten the sarcomere, watching the I band and H zone but not the A band; (3) switch ATP off: the heads cannot detach, so the length is frozen (rigor).' }));

    function update(redraw) {
      const e = cur(), b = bands(e.len);
      if (Math.abs(e.len - S.L) > 1e-9) { S.L = e.len; sl.set(S.L); }
      Array.prototype.forEach.call(sl.el.querySelectorAll('input'), function (i) { i.disabled = e.mode === 'rigor'; });
      ro.set('L', e.len.toFixed(2) + ' µm');
      ro.set('I', b.I.toFixed(2) + ' µm');
      ro.set('A', b.A.toFixed(2) + ' µm (never changes)');
      ro.set('H', b.H > 0 ? b.H.toFixed(2) + ' µm' : '0.00 µm (gone)');
      ro.set('O', b.overlap.toFixed(2) + ' µm');
      msg.textContent = e.mode === 'relaxed' ?
        'No calcium ions: tropomyosin covers the binding sites on actin, so no cross-bridges form. The sarcomere cannot shorten below its relaxed length (' + L0.toFixed(1) + ' µm); it can only be stretched.' :
        (e.mode === 'active' ? 'Calcium ions bound to troponin have moved tropomyosin aside. Myosin heads bind actin (cross-bridges) and pull the thin filaments inwards; ATP lets each head detach and recock. Slide the length down: the I band and H zone shorten, the A band does not.' :
          'Rigor: calcium ions are present but there is no ATP, so the myosin heads stay attached to actin and cannot detach. The filaments are locked: the sarcomere can neither shorten further nor relax.');
      if (redraw !== false) cv.redraw();
    }
    update();
  });
})();
