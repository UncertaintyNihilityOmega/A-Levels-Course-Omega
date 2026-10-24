/* widgets/chem-titration.js: pH titration curves for a strong or weak acid titrated with a strong or weak base.
   Attributes: data-acid="strong|weak", data-base="strong|weak", data-ca="0.100" (acid, mol dm-3, 0.010 to 1.00),
   data-cb="0.100" (base in the burette, 0.010 to 1.00), data-va="25.0" (acid in the flask, cm3, 5 to 50),
   data-pka="4.76" (optional: shows the pKa control and the half-equivalence point; A Level pages only).
   Model: charge balance [H+] + [Na+ or BH+] = [OH-] + [A-], solved for [H+] by bisection on log10[H+]
   (the same model as data/titration_model.py, which the chapter checks use). Kw = 1.00e-14.
   The weak base is fixed like ammonia (pKb 4.75). The "steep part" is the pH range covered within 2% of the
   equivalence volume either side (0.5 cm3 in a 25.0 cm3 titration). */
(function () {
  'use strict';

  const KW = 1.00e-14;
  const PKA_DEFAULT = 4.76, PKB = 4.75;
  const MINUS = '−';
  const INDICATORS = [
    { id: 'none', name: 'no indicator', lo: 0, hi: 0, from: '', to: '' },
    { id: 'mo', name: 'methyl orange', lo: 2.9, hi: 4.6, from: 'red', to: 'yellow' },
    { id: 'bpb', name: 'bromophenol blue', lo: 3.0, hi: 4.5, from: 'yellow', to: 'blue' },
    { id: 'tb', name: 'thymol blue', lo: 8.0, hi: 9.6, from: 'yellow', to: 'blue' },
    { id: 'tp', name: 'thymolphthalein', lo: 9.3, hi: 10.5, from: 'colourless', to: 'blue' }
  ];

  // pH after vb cm3 of base has been added to va cm3 of acid
  function phAt(vb, s) {
    const V = (s.va + vb) / 1000;
    const ta = s.ca * s.va / 1000 / V;
    const tb = s.cb * vb / 1000 / V;
    const Ka = Math.pow(10, -s.pka);
    const KaBH = KW / Math.pow(10, -PKB);
    const f = lh => {
      const h = Math.pow(10, lh);
      const a = s.aStrong ? ta : ta * Ka / (Ka + h);
      const b = s.bStrong ? tb : tb * h / (h + KaBH);
      return h + b - KW / h - a;
    };
    let lo = -16, hi = 2;
    for (let i = 0; i < 80; i++) {
      const mid = (lo + hi) / 2;
      if (f(mid) > 0) hi = mid; else lo = mid;
    }
    return -(lo + hi) / 2;
  }

  W.register('chem-titration', function (el, opts) {
    const { body } = W.frame(el, 'pH titration curve', 'Choose a strong or weak acid and base, then try the indicators');
    const msgs = [];
    const hasPka = opts.pka !== undefined && opts.pka !== '';

    function num(key, lo, hi, fb, what) {
      const raw = opts[key];
      if (raw === undefined || raw === '') return fb;
      const v = Number(String(raw).replace(MINUS, '-'));
      if (!isFinite(v)) { msgs.push('data-' + key + ' must be a number (' + what + '). Showing ' + fb + ' instead.'); return fb; }
      if (v < lo || v > hi) { msgs.push('data-' + key + ' = ' + raw + ' is outside ' + lo + ' to ' + hi + ' (' + what + '), so it was moved to the nearest allowed value.'); return Math.min(hi, Math.max(lo, v)); }
      return v;
    }
    function kind(key, fb) {
      const raw = opts[key];
      if (raw === undefined || raw === '') return fb;
      const v = String(raw).toLowerCase().trim();
      if (v === 'strong' || v === 'weak') return v;
      msgs.push('data-' + key + ' must be "strong" or "weak". Showing "' + fb + '" instead.');
      return fb;
    }

    const state = {
      aStrong: kind('acid', 'strong') === 'strong',
      bStrong: kind('base', 'strong') === 'strong',
      ca: num('ca', 0.01, 1.0, 0.100, 'concentration of the acid in mol dm⁻³, from 0.010 to 1.00'),
      cb: num('cb', 0.01, 1.0, 0.100, 'concentration of the base in mol dm⁻³, from 0.010 to 1.00'),
      va: num('va', 5, 50, 25.0, 'volume of acid in cm³, from 5 to 50'),
      pka: hasPka ? num('pka', 2, 12, PKA_DEFAULT, 'pKa of the weak acid, from 2 to 12') : PKA_DEFAULT,
      vb: 0,
      ind: 'none'
    };
    state.vb = state.ca * state.va / state.cb * 0.5;

    const err = W.h('div', { class: 'w-err', role: 'status' });

    // ---- controls
    function makeSelect(label, items, value, onchange) {
      const sel = W.h('select', { 'aria-label': label });
      items.forEach(it => sel.appendChild(W.h('option', { value: it[0], text: it[1] })));
      sel.value = value;
      sel.onchange = () => onchange(sel.value);
      return { sel, el: W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: label }), sel) };
    }
    const selAcid = makeSelect('Acid in the flask', [['strong', 'strong (like HCl)'], ['weak', hasPka ? 'weak (pKa below)' : 'weak (like ethanoic acid)']], state.aStrong ? 'strong' : 'weak', v => { state.aStrong = v === 'strong'; update(); });
    const selBase = makeSelect('Base in the burette', [['strong', 'strong (like NaOH)'], ['weak', 'weak (like ammonia)']], state.bStrong ? 'strong' : 'weak', v => { state.bStrong = v === 'strong'; update(); });
    const selInd = makeSelect('Indicator', INDICATORS.map(i => [i.id, i.id === 'none' ? 'none' : i.name + ' (' + i.lo + '–' + i.hi + ')']), 'none', v => { state.ind = v; update(); });

    const sCa = W.sliderNum({ label: 'Acid concentration (mol dm⁻³)', min: 0.01, max: 1, step: 0.005, value: state.ca, oninput: v => { state.ca = v; update(true); } });
    const sVa = W.sliderNum({ label: 'Volume of acid in the flask (cm³)', min: 5, max: 50, step: 0.5, value: state.va, oninput: v => { state.va = v; update(true); } });
    const sCb = W.sliderNum({ label: 'Base concentration (mol dm⁻³)', min: 0.01, max: 1, step: 0.005, value: state.cb, oninput: v => { state.cb = v; update(true); } });
    const sPka = W.sliderNum({ label: 'pKa of the weak acid', min: 2, max: 12, step: 0.05, value: state.pka, oninput: v => { state.pka = v; update(); } });
    const sVb = W.slider({ label: 'Volume of base added (cm³)', min: 0, max: 100, step: 0.1, value: state.vb, fmt: v => W.fix(v, 1), oninput: v => { state.vb = v; update(); } });

    body.appendChild(W.h('div', { class: 'w-row' }, selAcid.el, selBase.el, selInd.el));
    body.appendChild(sCa.el); body.appendChild(sVa.el); body.appendChild(sCb.el);
    const pkaWrap = W.h('div', {}, sPka.el);
    body.appendChild(pkaWrap);
    body.appendChild(sVb.el);
    body.appendChild(err);

    // ---- model values
    let model = null;
    function compute() {
      const s = { aStrong: state.aStrong, bStrong: state.bStrong, ca: state.ca, cb: state.cb, va: state.va, pka: state.pka };
      const veq = s.ca * s.va / s.cb;
      const pts = [];
      const N = 360;
      for (let i = 0; i <= N; i++) {
        const u = -1 + 2 * i / N;
        const v = veq * (1 + Math.sign(u) * Math.pow(Math.abs(u), 3));
        pts.push([v, phAt(v, s)]);
      }
      const phEq = phAt(veq, s);
      const d = 0.02 * veq;
      const lo = phAt(veq - d, s), hi = phAt(veq + d, s);
      model = { s, veq, pts, phEq, ph0: phAt(0, s), steepLo: lo, steepHi: hi, sharp: hi - lo >= 2.0, phEnd: phAt(2 * veq, s) };
    }

    // ---- canvas
    const M = { l: 44, r: 14, t: 14, b: 40 };
    function halo(ctx, col, s, x, y, align, color) {
      ctx.textAlign = align || 'left';
      ctx.lineWidth = 4; ctx.strokeStyle = col.card; ctx.lineJoin = 'round';
      ctx.strokeText(s, x, y);
      ctx.fillStyle = color || col.ink; ctx.fillText(s, x, y);
    }
    const cvs = W.canvas(body, {
      height: 330,
      draw(ctx, w, h, col) {
        if (!model) return;
        const xmax = 2 * model.veq;
        const px0 = M.l, px1 = w - M.r, py0 = h - M.b, py1 = M.t;
        const X = v => px0 + (px1 - px0) * v / xmax;
        const Y = p => py0 - (py0 - py1) * p / 14;
        ctx.font = '12px ' + col.font;
        ctx.textBaseline = 'alphabetic';
        ctx.lineCap = 'round'; ctx.lineJoin = 'round';

        // grid and tick numbers
        ctx.lineWidth = 1;
        for (let p = 0; p <= 14; p += 2) {
          ctx.strokeStyle = col.rule; ctx.beginPath(); ctx.moveTo(px0, Y(p)); ctx.lineTo(px1, Y(p)); ctx.stroke();
          ctx.fillStyle = col.ink2; ctx.textAlign = 'right'; ctx.fillText(String(p), px0 - 6, Y(p) + 4);
        }
        let xt = W.ticks(0, xmax, 5);
        if (!Array.isArray(xt) || !xt.length) xt = [0, xmax / 2, xmax];
        xt.forEach(v => {
          if (v < 0 || v > xmax * 1.0001) return;
          ctx.strokeStyle = col.rule; ctx.beginPath(); ctx.moveTo(X(v), py0); ctx.lineTo(X(v), py1); ctx.stroke();
          ctx.fillStyle = col.ink2; ctx.textAlign = 'center'; ctx.fillText(W.fmt(v, 3), X(v), py0 + 16);
        });
        // pH 7 line
        ctx.setLineDash([5, 4]); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(px0, Y(7)); ctx.lineTo(px1, Y(7)); ctx.stroke(); ctx.setLineDash([]);

        // indicator band
        const ind = INDICATORS.find(i => i.id === state.ind);
        if (ind && ind.id !== 'none') {
          ctx.save(); ctx.globalAlpha = 0.22; ctx.fillStyle = col.sc2;
          ctx.fillRect(px0, Y(ind.hi), px1 - px0, Y(ind.lo) - Y(ind.hi)); ctx.restore();
          ctx.strokeStyle = col.sc2; ctx.lineWidth = 1.2;
          ctx.beginPath(); ctx.moveTo(px0, Y(ind.hi)); ctx.lineTo(px1, Y(ind.hi)); ctx.moveTo(px0, Y(ind.lo)); ctx.lineTo(px1, Y(ind.lo)); ctx.stroke();
          halo(ctx, col, ind.name, px1 - 4, Y(ind.hi) - 4, 'right', col.ink);
        }

        // axes
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.6;
        ctx.beginPath(); ctx.moveTo(px0, py0); ctx.lineTo(px0, py1 - 4); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(px0, py0); ctx.lineTo(px1 + 4, py0); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ctx.fillText('volume of base added / cm³', (px0 + px1) / 2, h - 6);
        ctx.save(); ctx.translate(12, (py0 + py1) / 2); ctx.rotate(-Math.PI / 2); ctx.textAlign = 'center'; ctx.fillText('pH', 0, 0); ctx.restore();

        // curve (clipped to the plot)
        ctx.save(); ctx.beginPath(); ctx.rect(px0, py1 - 2, px1 - px0 + 2, py0 - py1 + 4); ctx.clip();
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.6;
        ctx.beginPath();
        model.pts.forEach((p, i) => { const x = X(p[0]), y = Y(p[1]); if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y); });
        ctx.stroke();
        // steep part highlighted
        ctx.strokeStyle = col.red; ctx.lineWidth = 3.6;
        ctx.beginPath();
        let started = false;
        model.pts.forEach(p => {
          if (p[0] >= model.veq * 0.98 && p[0] <= model.veq * 1.02) { const x = X(p[0]), y = Y(p[1]); if (started) ctx.lineTo(x, y); else { ctx.moveTo(x, y); started = true; } }
        });
        ctx.stroke();
        ctx.restore();

        // equivalence point
        ctx.setLineDash([4, 4]); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(X(model.veq), py0); ctx.lineTo(X(model.veq), Y(model.phEq)); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(X(model.veq), Y(model.phEq), 4, 0, 2 * Math.PI); ctx.fill();
        const ly = Math.min(py0 - 12, Y(model.phEq) + 18);
        halo(ctx, col, 'equivalence point', X(model.veq) + 9, ly, 'left', col.ink);
        halo(ctx, col, W.fix(model.veq, 1) + ' cm³, pH ' + W.fix(model.phEq, 2), X(model.veq) + 9, ly + 15, 'left', col.ink2);

        // half-equivalence (A Level pages: weak acid, strong base, pKa given)
        if (hasPka && !state.aStrong && state.bStrong) {
          const vh = model.veq / 2, ph = phAt(vh, model.s);
          ctx.fillStyle = col.sc2; ctx.beginPath(); ctx.arc(X(vh), Y(ph), 3.6, 0, 2 * Math.PI); ctx.fill();
          halo(ctx, col, 'half-equivalence: pH ' + W.fix(ph, 2), X(vh) + 8, Y(ph) + 17, 'left', col.ink);
        }

        // the reader's point
        const pv = phAt(state.vb, model.s);
        ctx.fillStyle = col.card; ctx.strokeStyle = col.ink; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(X(state.vb), Y(pv), 5, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
      }
    });
    cvs.cv.setAttribute('role', 'img');

    const read = W.readout([['eq', 'Equivalence volume'], ['pheq', 'pH at equivalence'], ['ph0', 'Initial pH'], ['steep', 'Steep part (within 2% of the equivalence volume)'], ['now', 'At the volume you chose'], ['ind', 'Indicator']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Start with a strong acid and a strong base. Then make the acid weak, then the base weak, and pick an indicator: its shaded band must lie within the steep part of the curve.' }));

    function indicatorText(ind) {
      if (ind.id === 'none') return 'none chosen';
      if (!model.sharp) return ind.name + ' is not suitable: there is no sharp change in pH, so the colour changes gradually over a large volume. Use a pH meter.';
      const lo = Math.max(ind.lo, model.steepLo), hi = Math.min(ind.hi, model.steepHi);
      const inside = Math.max(0, hi - lo) / (ind.hi - ind.lo);
      if (inside >= 0.9) return ind.name + ' (' + ind.lo + '–' + ind.hi + ') is suitable: its range lies within the steep part, so the end point is the equivalence point.';
      const mid = (ind.lo + ind.hi) / 2;
      if (mid < model.steepLo) return ind.name + ' (' + ind.lo + '–' + ind.hi + ') is not suitable: it changes colour below the steep part, early and gradually, long before the equivalence point.';
      if (mid > model.steepHi) return ind.name + ' (' + ind.lo + '–' + ind.hi + ') is not suitable: it changes colour above the steep part, only after the equivalence point has passed.';
      return ind.name + ' (' + ind.lo + '–' + ind.hi + ') is not suitable: only part of its range lies in the steep part, so the colour change is spread over too many drops.';
    }
    function colourNow(ind, pv) {
      if (ind.id === 'none') return '';
      if (pv < ind.lo) return ' Colour now: ' + ind.from + '.';
      if (pv > ind.hi) return ' Colour now: ' + ind.to + '.';
      return ' Colour now: mixed (' + ind.from + ' changing to ' + ind.to + ').';
    }

    function update(rescale) {
      err.textContent = msgs.join(' ');
      pkaWrap.style.display = (hasPka && !state.aStrong) ? '' : 'none';
      compute();
      const maxV = 2 * model.veq;
      sVb.input.max = String(maxV);
      sVb.input.step = String(Math.max(0.01, Math.round(maxV / 400 * 100) / 100));
      if (rescale) state.vb = model.veq * 0.5;
      if (state.vb > maxV) state.vb = maxV;
      sVb.set(state.vb);
      const pv = phAt(state.vb, model.s);
      const ind = INDICATORS.find(i => i.id === state.ind);
      read.set('eq', (model.veq >= 1000 ? String(Math.round(model.veq)) : Number(model.veq).toPrecision(3)) + ' cm³');
      read.set('pheq', W.fix(model.phEq, 2) + (model.phEq > 7.05 ? ' (above 7)' : (model.phEq < 6.95 ? ' (below 7)' : ' (neutral)')));
      read.set('ph0', W.fix(model.ph0, 2));
      read.set('steep', model.sharp ? 'pH ' + W.fix(model.steepLo, 1) + ' to ' + W.fix(model.steepHi, 1) : 'none: pH changes only from ' + W.fix(model.steepLo, 1) + ' to ' + W.fix(model.steepHi, 1));
      read.set('now', W.fix(state.vb, 1) + ' cm³ added: pH ' + W.fix(pv, 2) + (state.vb < model.veq - 1e-9 ? ' (acid in excess)' : (state.vb > model.veq + 1e-9 ? ' (base in excess)' : ' (equivalence)')));
      read.set('ind', indicatorText(ind) + colourNow(ind, pv));
      cvs.cv.setAttribute('aria-label', 'Titration curve, ' + (state.aStrong ? 'strong' : 'weak') + ' acid with ' + (state.bStrong ? 'strong' : 'weak') + ' base: starts at pH ' + W.fix(model.ph0, 2) + ', equivalence at ' + W.fmt(model.veq, 3) + ' cm³ and pH ' + W.fix(model.phEq, 2) + '.');
      cvs.redraw();
    }

    update(false);
  });
})();
