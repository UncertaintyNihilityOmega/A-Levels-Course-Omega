/* widgets/bio-rq.js: respiratory quotient (RQ) calculator. Used in bio.energy.
   Tab 1 "From a formula": the reader enters a substrate CxHyOz (C, H and O only). The widget balances complete oxidation
     CxHyOz + (x + y/4 - z/2) O2 -> x CO2 + (y/2) H2O   and gives RQ = x / (x + y/4 - z/2) to 2 d.p. with a verdict.
   Tab 2 "From respirometer readings": d1 = movement with KOH (mm towards the tube), d2 = movement without KOH
     (mm, positive = towards the tube, negative = away), r = capillary radius (mm).
     O2 taken in = pi r^2 d1, CO2 produced = pi r^2 (d1 - d2), RQ = (d1 - d2) / d1. Start values give RQ 0.70.
   Attributes: data-mode="formula|respirometer" (default formula); test attributes data-x, data-y, data-z, data-d1, data-d2, data-r.
   Pure functions are exported for data/test_bio-rq.js. */
(function () {
  'use strict';

  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const numOr = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? clamp(x, lo, hi) : d; };
  const SUB = '₀₁₂₃₄₅₆₇₈₉';
  const sub = s => String(s).replace(/\d/g, c => SUB[+c]);
  const trim = v => String(Math.round(v * 100) / 100);
  const coef = v => (Math.abs(v - 1) < 1e-9 ? '' : trim(v) + ' ');

  function formulaText(x, y, z) {
    return 'C' + (x > 1 ? sub(x) : '') + (y > 0 ? 'H' + (y > 1 ? sub(y) : '') : '') + (z > 0 ? 'O' + (z > 1 ? sub(z) : '') : '');
  }

  // complete oxidation of CxHyOz; x, y, z are numbers of atoms
  function balance(x, y, z) {
    if (![x, y, z].every(isFinite)) return { ok: false, msg: 'Enter whole numbers for the atoms of carbon, hydrogen and oxygen.' };
    if (![x, y, z].every(v => v === Math.floor(v))) return { ok: false, msg: 'Use whole numbers of atoms (a molecule cannot have half an atom).' };
    if (x < 1) return { ok: false, msg: 'A respiratory substrate needs at least one carbon atom.' };
    if (y < 0 || z < 0) return { ok: false, msg: 'The numbers of atoms cannot be negative.' };
    if (x > 100 || y > 300 || z > 100) return { ok: false, msg: 'Keep to at most 100 carbon, 300 hydrogen and 100 oxygen atoms.' };
    const o2 = x + y / 4 - z / 2;
    if (!(o2 > 0)) {
      return { ok: false, msg: 'This molecule already holds more oxygen than complete oxidation needs (x + y/4 − z/2 = ' + trim(o2) +
        '), so no O₂ is taken in. Try fewer oxygen atoms.' };
    }
    const h2o = y / 2;
    const eq = formulaText(x, y, z) + ' + ' + coef(o2) + 'O₂ → ' + coef(x) + 'CO₂' + (h2o > 0 ? ' + ' + coef(h2o) + 'H₂O' : '');
    return { ok: true, o2, h2o, rq: x / o2, eq };
  }

  function verdict(rq) {
    if (!(rq > 0) || !isFinite(rq)) return '';
    if (rq > 1.05) return 'RQ > 1: more CO₂ is produced than O₂ is taken in. In a living organism this suggests some anaerobic respiration, or a substrate richer in oxygen than carbohydrate, such as an organic acid.';
    if (rq >= 0.95) return 'RQ ≈ 1: the substrate is a carbohydrate.';
    if (rq >= 0.75) return 'RQ between 0.75 and 0.95: a mixture of substrates (protein is about 0.9, a person at rest about 0.8).';
    if (rq >= 0.65) return 'RQ ≈ 0.7: the substrate is a lipid.';
    return 'RQ below 0.65: lower than a typical lipid (about 0.7).';
  }

  // respirometer: r in mm, d1 and d2 in mm (d2 positive = towards the tube)
  function respiro(r, d1, d2) {
    if (![r, d1, d2].every(isFinite) || !(r > 0)) return { ok: false, msg: 'Enter a capillary radius above zero and numbers for both readings.' };
    if (!(d1 > 0)) return { ok: false, msg: 'No oxygen was taken in (d₁ = 0), so the RQ cannot be calculated.' };
    if (d2 > d1) return { ok: false, msg: 'd₂ cannot be larger than d₁: the carbon dioxide produced would be negative. Check the readings.' };
    const k = Math.PI * r * r;
    return { ok: true, vo2: k * d1, vnet: k * d2, vco2: k * (d1 - d2), rq: (d1 - d2) / d1 };
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { balance, verdict, respiro, formulaText, numOr, clamp };
  if (typeof W === 'undefined') return;

  const PRESETS = [
    { name: 'glucose', f: [6, 12, 6] },
    { name: 'tripalmitin (lipid)', f: [51, 98, 6] },
    { name: 'oleic acid', f: [18, 34, 2] },
    { name: 'malic acid', f: [4, 6, 5] }
  ];

  W.register('bio-rq', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Respiratory quotient', 'RQ = CO₂ produced ÷ O₂ taken in');
    const S = {
      mode: opts.mode === 'respirometer' ? 'respirometer' : 'formula',
      x: Math.round(numOr(opts.x, 6, 1, 100)), y: Math.round(numOr(opts.y, 12, 0, 300)), z: Math.round(numOr(opts.z, 6, 0, 100)),
      d1: numOr(opts.d1, 40, 0, 60), d2: numOr(opts.d2, 12, -20, 60), r: numOr(opts.r, 0.5, 0.2, 1)
    };

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Way to find the RQ' });
    const TT = { formula: 'From a formula', respirometer: 'From respirometer readings' };
    const tb = {};
    ['formula', 'respirometer'].forEach(function (m) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': m === S.mode ? 'true' : 'false', text: TT[m] });
      b.onclick = function () { setMode(m); };
      tb[m] = b; tabs.appendChild(b);
    });
    body.appendChild(W.h('div', { class: 'w-row' }, tabs));
    const panel = W.h('div');
    body.appendChild(panel);

    function tag(ctx, c, txt, x, y, align, bold) {
      ctx.save();
      ctx.font = (bold ? 'bold ' : '') + '12px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }

    // ------------------------------------------------------------------ formula tab
    function buildFormula() {
      const fx = W.field({ label: 'C atoms (x)', value: S.x, type: 'number', step: 1, width: 80, oninput: read });
      const fy = W.field({ label: 'H atoms (y)', value: S.y, type: 'number', step: 1, width: 80, oninput: read });
      const fz = W.field({ label: 'O atoms (z)', value: S.z, type: 'number', step: 1, width: 80, oninput: read });
      panel.appendChild(W.h('div', { class: 'w-row' }, fx.el, fy.el, fz.el));
      const pr = W.h('div', { class: 'w-row', role: 'group', 'aria-label': 'Preset substrates' });
      PRESETS.forEach(function (p) {
        const b = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: p.name });
        b.onclick = function () { fx.input.value = p.f[0]; fy.input.value = p.f[1]; fz.input.value = p.f[2]; read(); };
        pr.appendChild(b);
      });
      panel.appendChild(pr);
      const err = W.h('div', { class: 'w-err', role: 'status', 'aria-live': 'polite' });
      panel.appendChild(err);
      const cv = { o2: 0, rq: 0, ok: false };
      const c = W.canvas(panel, {
        height: 132,
        label: 'Number line of RQ from 0.5 to 1.5 with typical values for lipid, protein and carbohydrate and a marker for the RQ you calculated',
        describe: function () {
          return cv.ok ? 'RQ number line from 0.5 to 1.5. Typical values: lipid about 0.7, protein about 0.9, carbohydrate 1.0. Your substrate has an RQ of ' + cv.rq.toFixed(2) + '.'
            : 'RQ number line from 0.5 to 1.5. No valid substrate entered, so there is no marker.';
        },
        draw: function (ctx, w, h, col) {
          if (!(w > 0) || !(h > 0) || w < 150 || h < 100) return;
          const x0 = 22, x1 = w - 22, lo = 0.5, hi = 1.5, X = v => x0 + (v - lo) / (hi - lo) * (x1 - x0), ay = 82;
          ctx.save();
          ctx.strokeStyle = col.ink2; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(x0, ay); ctx.lineTo(x1, ay); ctx.stroke();
          ctx.font = '11px ' + (col.font || 'sans-serif'); ctx.fillStyle = col.ink2; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
          for (let v = 0.5; v <= 1.5001; v += 0.25) {
            ctx.beginPath(); ctx.moveTo(X(v), ay); ctx.lineTo(X(v), ay + 5); ctx.stroke();
            ctx.fillText(v.toFixed(2), X(v), ay + 17);
          }
          ctx.restore();
          // reference values, stacked in levels so labels never overlap
          const refs = [['lipid 0.7', 0.7], ['protein 0.9', 0.9], ['carbohydrate 1.0', 1.0]];
          const placed = [];
          refs.forEach(function (r) {
            ctx.font = '12px ' + (col.font || 'sans-serif');
            const tw = ctx.measureText(r[0]).width, cx = X(r[1]);
            let l = 0;
            while (l < 3 && placed.some(p => p.l === l && !(cx + tw / 2 + 6 < p.a || cx - tw / 2 - 6 > p.b))) l++;
            placed.push({ l, a: cx - tw / 2, b: cx + tw / 2 });
            const ty = ay - 14 - l * 16;
            ctx.save(); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([3, 3]);
            ctx.beginPath(); ctx.moveTo(cx, ay); ctx.lineTo(cx, ty + 4); ctx.stroke(); ctx.restore();
            tag(ctx, col, r[0], clamp(cx, tw / 2 + 2, w - tw / 2 - 2), ty, 'center');
          });
          if (cv.ok) {
            const m = clamp(cv.rq, lo, hi), mx = X(m);
            ctx.save();
            ctx.fillStyle = col.red; ctx.strokeStyle = col.card; ctx.lineWidth = 2.5;
            ctx.beginPath(); ctx.arc(mx, ay, 7, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
            ctx.restore();
            tag(ctx, col, 'your RQ ' + cv.rq.toFixed(2) + (cv.rq > hi || cv.rq < lo ? ' (off the scale)' : ''), clamp(mx, 60, w - 60), ay + 40, 'center', true);
          }
        }
      });
      const ro = W.readout([['eq', 'Balanced equation'], ['o2', 'O₂ needed per molecule'], ['rq', 'RQ']]);
      panel.appendChild(ro.el);
      const vd = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
      panel.appendChild(vd);
      panel.appendChild(W.h('div', { class: 'w-note', text: 'Complete oxidation of CxHyOz: O₂ needed = x + y/4 − z/2, CO₂ = x, H₂O = y/2. Try glucose, then a lipid, then malic acid, and compare each RQ with the typical values.' }));

      function read() {
        S.x = parseFloat(fx.get()); S.y = parseFloat(fy.get()); S.z = parseFloat(fz.get());
        const b = balance(S.x, S.y, S.z);
        cv.ok = b.ok;
        if (b.ok) {
          cv.rq = b.rq; cv.o2 = b.o2;
          err.textContent = '';
          ro.set('eq', b.eq); ro.set('o2', trim(b.o2)); ro.set('rq', b.rq.toFixed(2));
          vd.textContent = verdict(b.rq);
        } else {
          err.textContent = b.msg;
          ro.set('eq', '–'); ro.set('o2', '–'); ro.set('rq', '–');
          vd.textContent = '';
        }
        c.redraw();
      }
      read();
    }

    // ------------------------------------------------------------------ respirometer tab
    function buildResp() {
      const sA = W.sliderNum({ label: 'd₁: movement with KOH / mm (towards tube)', min: 0, max: 60, step: 1, value: S.d1,
        oninput: function () { S.d1 = numOr(sA.get(), 40, 0, 60); update(); } });
      const sB = W.sliderNum({ label: 'd₂: movement without KOH / mm (negative = away)', min: -20, max: 60, step: 1, value: S.d2,
        oninput: function () { S.d2 = numOr(sB.get(), 12, -20, 60); update(); } });
      const sR = W.sliderNum({ label: 'Capillary radius / mm', min: 0.2, max: 1, step: 0.05, value: S.r,
        oninput: function () { S.r = numOr(sR.get(), 0.5, 0.2, 1); update(); } });
      panel.appendChild(W.h('div', { class: 'w-row' }, sA.el));
      panel.appendChild(W.h('div', { class: 'w-row' }, sB.el));
      panel.appendChild(W.h('div', { class: 'w-row' }, sR.el));
      const err = W.h('div', { class: 'w-err', role: 'status', 'aria-live': 'polite' });
      panel.appendChild(err);
      const R = { v: respiro(S.r, S.d1, S.d2) };
      const c = W.canvas(panel, {
        height: 200,
        label: 'Capillary tube of a respirometer showing where the drop of fluid moved with potassium hydroxide and without it',
        describe: function () {
          return 'Two rows. With potassium hydroxide the drop moved ' + S.d1 + ' mm towards the tube. Without it the drop moved ' + Math.abs(S.d2) + ' mm ' +
            (S.d2 >= 0 ? 'towards' : 'away from') + ' the tube.' + (R.v.ok ? ' RQ ' + R.v.rq.toFixed(2) + '.' : '');
        },
        draw: function (ctx, w, h, col) {
          if (!(w > 0) || !(h > 0) || w < 150 || h < 120) return;
          const pl = 16, pr = 16, sc = (w - pl - pr) / 90, X = d => pl + (65 - d) * sc;
          const rows = [[h * 0.30, S.d1, 'with KOH: d₁ = ' + S.d1 + ' mm', col.sc], [h * 0.68, S.d2, 'without KOH: d₂ = ' + S.d2 + ' mm', col.sc2 || col.ink2]];
          ctx.save();
          ctx.font = '11px ' + (col.font || 'sans-serif'); ctx.textBaseline = 'alphabetic';
          // start line and ticks
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([4, 4]);
          ctx.beginPath(); ctx.moveTo(X(0), h * 0.30 - 22); ctx.lineTo(X(0), h * 0.68 + 18); ctx.stroke();
          ctx.setLineDash([]);
          rows.forEach(function (r) {
            const y = r[0];
            ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.5;
            ctx.beginPath(); ctx.rect(X(65), y - 5, X(-25) - X(65), 10); ctx.stroke();
            ctx.fillStyle = col.ink2;
            ctx.fillRect(X(65) - 4, y - 12, 4, 24);
          });
          ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
          const yb = h * 0.68 + 36;
          for (let d = -20; d <= 60; d += 20) {
            ctx.strokeStyle = col.ink2; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(X(d), yb - 16); ctx.lineTo(X(d), yb - 11); ctx.stroke();
            ctx.fillText(String(d), X(d), yb);
          }
          ctx.textAlign = 'left'; ctx.fillStyle = col.ink3; ctx.fillText('← towards tube', pl, h - 6);
          ctx.textAlign = 'right'; ctx.fillText('away →', w - pr, h - 6);
          ctx.restore();
          rows.forEach(function (r) {
            const y = r[0], xe = X(clamp(r[1], -25, 65));
            ctx.save();
            ctx.strokeStyle = r[3]; ctx.fillStyle = r[3]; ctx.lineWidth = 2.5;
            if (Math.abs(xe - X(0)) > 12) {
              const dir = xe < X(0) ? -1 : 1;
              ctx.beginPath(); ctx.moveTo(X(0) + dir * 9, y); ctx.lineTo(xe - dir * 9, y); ctx.stroke();
              ctx.beginPath(); ctx.moveTo(xe - dir * 9, y); ctx.lineTo(xe - dir * 15, y - 4); ctx.lineTo(xe - dir * 15, y + 4); ctx.closePath(); ctx.fill();
            }
            ctx.lineWidth = 2; ctx.fillStyle = col.card;
            ctx.beginPath(); ctx.arc(X(0), y, 6, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
            ctx.fillStyle = r[3];
            ctx.beginPath(); ctx.arc(xe, y, 6, 0, 2 * Math.PI); ctx.fill();
            ctx.restore();
            tag(ctx, col, r[2], pl + 4, y - 16, 'left');
          });
          tag(ctx, col, 'start', X(0), h * 0.30 - 26, 'center');
        }
      });
      const ro = W.readout([['o2', 'O₂ taken in (πr²d₁)'], ['net', 'Net volume decrease (πr²d₂)'], ['co2', 'CO₂ produced (πr²(d₁ − d₂))'], ['rq', 'RQ']]);
      panel.appendChild(ro.el);
      const vd = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
      panel.appendChild(vd);
      panel.appendChild(W.h('div', { class: 'w-note', text: 'With KOH the carbon dioxide is absorbed, so d₁ shows O₂ only. Without KOH the drop shows the net change, so CO₂ = O₂ − net. The radius cancels in the RQ: change it and watch only the volumes change. Start values give RQ 0.70, the lipid value.' }));

      function update() {
        R.v = respiro(S.r, S.d1, S.d2);
        const v = R.v;
        if (v.ok) {
          err.textContent = '';
          ro.set('o2', v.vo2.toFixed(1) + ' mm³'); ro.set('net', (v.vnet >= 0 ? '' : '−') + Math.abs(v.vnet).toFixed(1) + ' mm³' + (v.vnet >= 0 ? ' (towards tube)' : ' (away from tube)'));
          ro.set('co2', v.vco2.toFixed(1) + ' mm³'); ro.set('rq', v.rq.toFixed(2));
          vd.textContent = verdict(v.rq);
        } else {
          err.textContent = v.msg;
          ['o2', 'net', 'co2', 'rq'].forEach(k => ro.set(k, '–'));
          vd.textContent = '';
        }
        c.redraw();
      }
      update();
    }

    function setMode(m) {
      S.mode = m;
      Object.keys(tb).forEach(function (k) { tb[k].setAttribute('aria-pressed', k === m ? 'true' : 'false'); });
      build();
    }
    function build() {
      panel.textContent = '';
      if (S.mode === 'respirometer') buildResp(); else buildFormula();
    }
    build();
  });
})();
