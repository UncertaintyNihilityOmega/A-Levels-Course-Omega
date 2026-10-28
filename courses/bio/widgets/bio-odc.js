/* widgets/bio-odc.js: oxygen dissociation curve of adult haemoglobin and the Bohr shift (data-pco2="5.3", kPa).
   Used in bio.oxygen. MODEL curve (same function as the :::plot lines and checks/bio.oxygen.py):
   saturation / % = 100 p^n / (P50^n + p^n), n = 2.7, P50 = 3.4 kPa at pCO2 5.3 kPa,
   P50 = 3.4 + 0.25 (pCO2 - 5.3) kPa with pCO2 limited to 4-10 kPa. The values illustrate the shape and the shift;
   they are not data for questions.
   Optional test attributes: data-lungs (pO2 of the lungs marker, 8-14 kPa, default 13), data-tissue (1-8 kPa, default 4).
   Pure functions are exported for data/test_bio-odc.js. */
(function () {
  'use strict';

  const N = 2.7, P50_REF = 3.4, PCO2_REF = 5.3, XMAX = 14;
  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? clamp(x, lo, hi) : d; };
  const p50 = pco2 => P50_REF + 0.25 * (clamp(pco2, 4, 10) - PCO2_REF);
  function sat(p, pco2) {
    if (!(p > 0)) return 0;
    const k = Math.pow(p50(pco2), N), q = Math.pow(p, N);
    return 100 * q / (k + q);
  }
  const pct = x => String(Math.round(x));
  // unloaded: difference of the two readings as shown (rounded), so the readout adds up on screen
  const unloaded = (pl, pt, pco2) => Math.round(sat(pl, pco2)) - Math.round(sat(pt, pco2));

  if (typeof module !== 'undefined' && module.exports) module.exports = { p50, sat, unloaded, num, clamp };
  if (typeof W === 'undefined') return;

  W.register('bio-odc', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Oxygen dissociation curve', 'Change the pCO₂ and move the two markers');
    const S = {
      pco2: num(opts.pco2, PCO2_REF, 4, 10),
      lungs: num(opts.lungs, 13, 8, 14),
      tissue: num(opts.tissue, 4, 1, 8),
      A: null, busy: false
    };

    // ---- controls: every marker also has a slider, so nothing needs dragging ----
    const sC = W.sliderNum({ label: 'pCO₂ / kPa', min: 4, max: 10, step: 0.1, value: S.pco2,
      oninput: function () { if (S.busy) return; S.pco2 = num(sC.get(), PCO2_REF, 4, 10); update(); } });
    const sL = W.sliderNum({ label: 'Lungs marker, pO₂ / kPa', min: 8, max: 14, step: 0.5, value: S.lungs,
      oninput: function () { if (S.busy) return; S.lungs = num(sL.get(), 13, 8, 14); update(); } });
    const sT = W.sliderNum({ label: 'Tissue marker, pO₂ / kPa', min: 1, max: 8, step: 0.5, value: S.tissue,
      oninput: function () { if (S.busy) return; S.tissue = num(sT.get(), 4, 1, 8); update(); } });
    body.appendChild(W.h('div', { class: 'w-row' }, sC.el));
    body.appendChild(W.h('div', { class: 'w-row' }, sL.el, sT.el));

    function tag(ctx, c, txt, x, y, align) {
      ctx.save();
      ctx.font = '12px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left';
      ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 4;
      ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = c.ink;
      ctx.fillText(txt, x, y);
      ctx.restore();
    }
    function curve(ctx, A, pco2, color, width, dash) {
      ctx.save();
      ctx.strokeStyle = color; ctx.lineWidth = width; ctx.lineJoin = 'round';
      if (dash) ctx.setLineDash(dash);
      ctx.beginPath();
      for (let i = 0; i <= 140; i++) {
        const x = XMAX * i / 140, px = A.X(x), py = A.Y(sat(x, pco2));
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.restore();
    }
    function guide(ctx, c, x0, y0, x1, y1) {
      ctx.save();
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
      ctx.restore();
    }

    function draw(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 150 || h < 120) return;
      const view = { x0: 0, x1: XMAX, y0: 0, y1: 105 };
      const A = W.axes(ctx, w, h, view, c, { pad: { l: 44, r: 14, t: 26, b: 46 }, nx: 7, ny: 4 });
      if (!A) return;
      ctx.save();
      ctx.font = '12px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.textBaseline = 'alphabetic';
      ctx.textAlign = 'left'; ctx.fillText('saturation of haemoglobin / %', 4, 14);
      ctx.textAlign = 'right'; ctx.fillText('partial pressure of oxygen / kPa', A.X(XMAX), h - 6);
      ctx.restore();
      S.A = { X: A.X, Y: A.Y, x0: A.X(0), x1: A.X(XMAX) };
      ctx.save();
      ctx.beginPath(); ctx.rect(A.X(0), A.Y(105), A.X(XMAX) - A.X(0), A.Y(0) - A.Y(105)); ctx.clip();
      curve(ctx, A, PCO2_REF, c.ink3, 2, [6, 4]);
      curve(ctx, A, S.pco2, c.sc, 3.5);
      ctx.restore();

      const yl = A.Y(sat(S.lungs, S.pco2)), yt = A.Y(sat(S.tissue, S.pco2));
      const xl = A.X(S.lungs), xt = A.X(S.tissue), xa = A.X(0), ya = A.Y(0);
      guide(ctx, c, xl, yl, xl, ya); guide(ctx, c, xl, yl, xa, yl);
      guide(ctx, c, xt, yt, xt, ya); guide(ctx, c, xt, yt, xa, yt);
      // bracket on the y axis: the oxygen unloaded between the two markers
      const bx = xa + 7;
      ctx.save();
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(bx, yl); ctx.lineTo(bx, yt); ctx.moveTo(bx - 4, yl); ctx.lineTo(bx + 4, yl);
      ctx.moveTo(bx - 4, yt); ctx.lineTo(bx + 4, yt); ctx.stroke();
      ctx.restore();
      // markers: a ring for the lungs, a square for the tissue
      ctx.save();
      ctx.lineWidth = 2.5; ctx.strokeStyle = c.card;
      ctx.fillStyle = c.ink;
      ctx.beginPath(); ctx.arc(xl, yl, 7, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
      ctx.fillStyle = c.red;
      ctx.beginPath(); ctx.rect(xt - 6.5, yt - 6.5, 13, 13); ctx.fill(); ctx.stroke();
      ctx.restore();
      const right = xl > A.X(XMAX) - 56;
      tag(ctx, c, 'lungs', right ? xl - 12 : xl + 12, yl + 20, right ? 'right' : 'left');
      tag(ctx, c, 'tissue', Math.max(xa + 20, xt - 10), yt - 12, 'right');
    }

    const c = W.canvas(body, {
      height: (el.clientWidth || 600) < 480 ? 290 : 320,
      label: 'Model oxygen dissociation curve with a lungs marker and a tissue marker',
      describe: function () {
        const sl = sat(S.lungs, S.pco2), st = sat(S.tissue, S.pco2);
        return 'Model S-shaped curves of percentage saturation of haemoglobin against pO₂ from 0 to 14 kPa. The solid curve is for a pCO₂ of ' +
          S.pco2.toFixed(1) + ' kPa; the dashed curve is the reference at ' + PCO2_REF + ' kPa. The lungs marker is at ' + S.lungs +
          ' kPa, ' + pct(sl) + '% saturated. The tissue marker is at ' + S.tissue + ' kPa, ' + pct(st) + '% saturated. ' +
          unloaded(S.lungs, S.tissue, S.pco2) + ' percentage points of saturation are unloaded between them.';
      },
      draw: draw
    });

    const ro = W.readout([['c', 'pCO₂'], ['l', 'Saturation at the lungs marker'], ['t', 'Saturation at the tissue marker'],
      ['u', 'Oxygen unloaded'], ['d', 'Compared with pCO₂ 5.3 kPa']]);
    body.appendChild(ro.el);
    const ex = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.appendChild(ex);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Solid curve: the pCO₂ you set. Dashed curve: the reference at pCO₂ 5.3 kPa. The bracket on the vertical axis spans the oxygen unloaded between the markers. Model curve: the values illustrate the shape and the shift and are not data for questions.' }));

    function update() {
      const u = unloaded(S.lungs, S.tissue, S.pco2), u0 = unloaded(S.lungs, S.tissue, PCO2_REF);
      const st = Math.round(sat(S.tissue, S.pco2)), st0 = Math.round(sat(S.tissue, PCO2_REF));
      ro.set('c', S.pco2.toFixed(1) + ' kPa');
      ro.set('l', pct(sat(S.lungs, S.pco2)) + '% at ' + S.lungs + ' kPa');
      ro.set('t', pct(sat(S.tissue, S.pco2)) + '% at ' + S.tissue + ' kPa');
      ro.set('u', u + ' percentage points');
      ro.set('d', (u - u0 > 0 ? '+' : u - u0 < 0 ? '−' : '') + Math.abs(u - u0) + ' percentage points');
      let msg;
      if (S.pco2 > PCO2_REF + 0.05) {
        msg = 'Higher pCO₂ → curve shifts right → more O₂ released at the same pO₂ (Bohr shift). At the tissue marker the saturation is ' + st + '% instead of ' + st0 + '%.';
      } else if (S.pco2 < PCO2_REF - 0.05) {
        msg = 'Lower pCO₂ → curve shifts left → haemoglobin holds O₂ more tightly, as in the lungs. At the tissue marker the saturation is ' + st + '% instead of ' + st0 + '%.';
      } else {
        msg = 'This is the reference curve. Higher pCO₂ → curve shifts right → more O₂ released at the same pO₂ (Bohr shift): raise the pCO₂ slider to see it.';
      }
      ex.textContent = msg;
      c.redraw();
    }
    function sync() {
      S.busy = true;
      sL.set(S.lungs); sT.set(S.tissue); sC.set(S.pco2);
      S.busy = false;
    }

    // dragging the markers (the sliders do the same without a mouse)
    W.drag(c.wrap, {
      hit: function (x, y) {
        if (!S.A || !(S.A.x1 > S.A.x0)) return null;
        let best = null, bd = 1e9;
        [['lungs', S.lungs], ['tissue', S.tissue]].forEach(function (k) {
          const d = Math.hypot(x - S.A.X(k[1]), y - S.A.Y(sat(k[1], S.pco2)));
          if (d < bd) { bd = d; best = k[0]; }
        });
        return bd <= 20 ? { k: best } : null;
      },
      move: function (t, x) {
        if (!S.A || !(S.A.x1 > S.A.x0)) return;
        const p = Math.round((x - S.A.x0) / (S.A.x1 - S.A.x0) * XMAX * 10) / 10;
        if (t.k === 'lungs') S.lungs = clamp(p, 8, 14); else S.tissue = clamp(p, 1, 8);
        sync(); update();
      },
      end: function () {}
    });

    update();
  });
})();
