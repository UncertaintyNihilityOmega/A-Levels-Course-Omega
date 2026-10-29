/* widgets/bio-limiting.js: limiting factors of photosynthesis. Used in bio.limiting.
   Model (arbitrary units, stated on screen): rate P(I) from a smooth minimum of the light-limited rate a*I and the
   maximum rate Pmax(C, T):
     Pmax(C, T) = 112 * C/(C + 0.072) * f(T)/f(25),   f(T) = 2^(T/10) / (1 + exp((T - 35)/2.5))
     P = [ (aI + Pmax) - sqrt((aI + Pmax)^2 - 4*theta*aI*Pmax) ] / (2*theta),   a = 1.6, theta = 0.9
   so at 25 degrees C Pmax is 40 at 0.04 % CO2 and 70 at 0.12 % CO2, the values behind the plots in the chapter.
   Attributes: data-co2 (% , 0.01 to 0.15, default 0.04), data-temp (degrees C, 5 to 45, default 25).
   Pure functions are exported for data/test_bio-limiting.js. */
(function () {
  'use strict';

  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const numOr = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? clamp(x, lo, hi) : d; };
  const AMAX = 112, KC = 0.072, SLOPE = 1.6, THETA = 0.9;
  const f = T => Math.pow(2, T / 10) / (1 + Math.exp((T - 35) / 2.5));
  const F25 = f(25);
  let FMAX = 0, TOPT = 25;
  for (let t = 0; t <= 60; t += 0.1) { const v = f(t); if (v > FMAX) { FMAX = v; TOPT = t; } }

  const cfac = C => C / (C + KC);
  const tfac = T => f(T) / F25;
  const pmax = (C, T) => AMAX * cfac(C) * tfac(T);
  function rate(I, C, T) {
    const pm = pmax(C, T), a = SLOPE * Math.max(I, 0), s = a + pm;
    return (s - Math.sqrt(Math.max(s * s - 4 * THETA * a * pm, 0))) / (2 * THETA);
  }
  // which factor limits the rate at light intensity I
  function limiting(I, C, T) {
    const pm = pmax(C, T);
    if (!(I > 0)) return { kind: 'dark' };
    const q = SLOPE * I / pm;
    if (q < 0.6) return { kind: 'light' };
    const cn = cfac(C), tn = f(T) / FMAX;
    const other = cn <= tn ? 'co2' : (T < TOPT ? 'cold' : 'hot');
    return { kind: q > 1.6 ? 'other' : 'both', other: other };
  }
  const niceTop = v => { const steps = [20, 25, 40, 50, 60, 80, 100, 120, 150]; for (let i = 0; i < steps.length; i++) if (steps[i] >= v) return steps[i]; return Math.ceil(v / 50) * 50; };

  if (typeof module !== 'undefined' && module.exports) module.exports = { pmax, rate, limiting, tfac, cfac, numOr, clamp, niceTop, TOPT };
  if (typeof W === 'undefined') return;

  W.register('bio-limiting', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Limiting factors in photosynthesis', 'Model curves in arbitrary units');
    const S = {
      C0: numOr(opts.co2, 0.04, 0.01, 0.15), T0: Math.round(numOr(opts.temp, 25, 5, 45)),
      I: 12
    };
    S.C = S.C0; S.T = S.T0;
    let last = null;

    function tag(ctx, c, txt, x, y, align, color) {
      ctx.save();
      ctx.font = '12px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }

    function describe() {
      const pm = pmax(S.C, S.T), r = rate(S.I, S.C, S.T);
      return 'Model graph of rate of photosynthesis against light intensity from 0 to 100 arbitrary units, at ' + S.C.toFixed(2) +
        ' percent carbon dioxide and ' + S.T + ' degrees Celsius. The rate rises in a straight line at low light, then bends and levels off near a maximum of ' +
        pm.toFixed(0) + ' units. The marker is at light intensity ' + S.I.toFixed(0) + ', where the rate is ' + r.toFixed(0) + ' units.';
    }

    function draw(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 150 || h < 110) { last = null; return; }
      const pm = pmax(S.C, S.T), pr = pmax(S.C0, S.T0);
      const v = { x0: 0, x1: 100, y0: 0, y1: niceTop(1.1 * Math.max(pm, pr)) };
      const A = W.axes(ctx, w, h, v, c, { xlabel: 'light intensity / arbitrary units', ylabel: 'rate / arbitrary units', nx: 5, ny: 4 });
      if (!A) { last = null; return; }
      const px0 = A.X(0), px1 = A.X(100), py0 = A.Y(0), py1 = A.Y(v.y1);
      last = { px0: px0, px1: px1 };
      ctx.save();
      ctx.beginPath(); ctx.rect(px0, py1, px1 - px0, py0 - py1); ctx.clip();
      const curve = function (C, T, color, width, dash) {
        ctx.save();
        ctx.strokeStyle = color; ctx.lineWidth = width; ctx.setLineDash(dash || []);
        ctx.beginPath();
        for (let i = 0; i <= 100; i++) {
          const x = A.X(i), y = A.Y(rate(i, C, T));
          if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke(); ctx.restore();
      };
      const moved = Math.abs(pm - pr) > 0.5;
      if (moved) curve(S.C0, S.T0, c.ink3, 2, [5, 4]);
      // maximum (plateau) of the current curve
      ctx.save();
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
      ctx.beginPath(); ctx.moveTo(px0, A.Y(pm)); ctx.lineTo(px1, A.Y(pm)); ctx.stroke(); ctx.restore();
      curve(S.C, S.T, c.sc, 3);
      // marker
      const r = rate(S.I, S.C, S.T), mx = A.X(S.I), my = A.Y(r);
      ctx.save();
      ctx.strokeStyle = c.red; ctx.lineWidth = 1.5; ctx.setLineDash([2, 3]);
      ctx.beginPath(); ctx.moveTo(mx, my); ctx.lineTo(mx, py0); ctx.stroke(); ctx.restore();
      ctx.beginPath(); ctx.arc(mx, my, 6, 0, 2 * Math.PI);
      ctx.fillStyle = c.red; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = c.card; ctx.stroke();
      ctx.restore();
      tag(ctx, c, 'maximum rate', px1 - 4, A.Y(pm) - 6, 'right', c.ink2);
      if (moved) {
        const ly = py0 - 36;
        ctx.save(); ctx.strokeStyle = c.sc; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(px1 - 150, ly); ctx.lineTo(px1 - 128, ly); ctx.stroke();
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 2; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(px1 - 150, ly + 18); ctx.lineTo(px1 - 128, ly + 18); ctx.stroke(); ctx.restore();
        tag(ctx, c, 'these settings', px1 - 122, ly + 4, 'left', c.ink);
        tag(ctx, c, 'start settings', px1 - 122, ly + 22, 'left', c.ink2);
      }
    }

    const cv = W.canvas(body, {
      height: 280,
      label: 'Model graph of the rate of photosynthesis against light intensity, with a marker that shows which factor limits the rate',
      describe: describe,
      draw: draw
    });

    const sI = W.sliderNum({ label: 'Light intensity (marker) / arbitrary units', min: 0, max: 100, step: 1, value: S.I,
      oninput: function () { S.I = numOr(sI.get(), 20, 0, 100); update(); } });
    const sC = W.sliderNum({ label: 'Carbon dioxide / % of the air', min: 0.01, max: 0.15, step: 0.01, value: S.C,
      oninput: function () { S.C = numOr(sC.get(), 0.04, 0.01, 0.15); update(); } });
    const sT = W.sliderNum({ label: 'Temperature / °C', min: 5, max: 45, step: 1, value: S.T,
      oninput: function () { S.T = Math.round(numOr(sT.get(), 25, 5, 45)); update(); } });
    body.appendChild(W.h('div', { class: 'w-row' }, sI.el));
    body.appendChild(W.h('div', { class: 'w-row' }, sC.el));
    body.appendChild(W.h('div', { class: 'w-row' }, sT.el));

    const presets = W.h('div', { class: 'w-row', role: 'group', 'aria-label': 'Preset settings' });
    [['Start settings', null], ['Cold day, 10 °C', [S.C0, 10]], ['Glasshouse, 0.12 % CO₂, 28 °C', [0.12, 28]], ['Too hot, 42 °C', [S.C0, 42]]].forEach(function (p) {
      const b = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: p[0] });
      b.onclick = function () {
        const t = p[1] || [S.C0, S.T0];
        S.C = t[0]; S.T = t[1]; sC.set(S.C); sT.set(S.T); update();
      };
      presets.appendChild(b);
    });
    body.appendChild(presets);

    const ro = W.readout([['i', 'Light intensity'], ['r', 'Rate at this light'], ['m', 'Maximum rate'], ['l', 'Limiting factor']]);
    body.appendChild(ro.el);
    const msg = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.appendChild(msg);
    body.appendChild(W.h('div', { class: 'w-note', text: 'A model, not data, in arbitrary units. Drag the marker or use the slider: on the rising part of the curve light limits the rate; where it has levelled off, carbon dioxide or temperature does. Change them and watch the maximum rate move.' }));

    function words(L, C, T) {
      switch (L.kind) {
        case 'dark': return ['none yet (no light)', 'In the dark there is no light-dependent stage, so no ATP or reduced NADP are made and the rate is zero in this model.'];
        case 'light': return ['light', 'Light is limiting: the curve is still rising, so more light means more ATP and reduced NADP and a higher rate.'];
        case 'both': return ['light, and ' + (L.other === 'co2' ? 'CO₂' : 'temperature') + ' close behind', 'Near the bend: light is about to stop limiting, and ' + (L.other === 'co2' ? 'carbon dioxide' : 'temperature') + ' is about to take over.'];
        default:
          if (L.other === 'co2') return ['carbon dioxide', 'Carbon dioxide is limiting: the curve has levelled off, so more light will not help. Only more CO₂ (fixed by rubisco) would raise the maximum rate.'];
          if (L.other === 'cold') return ['temperature (too cold)', 'Temperature is limiting: the curve has levelled off. The enzymes of the Calvin cycle work slowly in the cold, so warming the leaf would raise the maximum rate.'];
          return ['temperature (too hot)', 'Temperature is limiting: the curve has levelled off at a low maximum because the enzymes are being denatured. More light cannot help.'];
      }
    }

    function update() {
      const L = limiting(S.I, S.C, S.T), t = words(L, S.C, S.T);
      ro.set('i', S.I.toFixed(0) + ' arbitrary units');
      ro.set('r', rate(S.I, S.C, S.T).toFixed(0) + ' units');
      ro.set('m', pmax(S.C, S.T).toFixed(0) + ' units');
      ro.set('l', t[0]);
      msg.textContent = t[1];
      cv.redraw();
    }

    W.drag(cv.wrap, {
      hit: function (x, y) { return last && x >= last.px0 - 12 && x <= last.px1 + 12 ? 'pt' : null; },
      move: function (thing, x) {
        if (!last || !(last.px1 > last.px0)) return;
        S.I = clamp(Math.round((x - last.px0) / (last.px1 - last.px0) * 100), 0, 100);
        sI.set(S.I); update();
      },
      end: function () {}
    });
    update();
  });
})();
