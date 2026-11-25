/* fm-topple: a solid on a rough plane that you tilt (9231 Paper 3, toppling and sliding).
   data-shape="cuboid|cylinder|cone"   the solid; default cuboid
   data-width="6"      cuboid: width of the base along the slope; cylinder and cone: radius of the base (cm, 1 to 20)
   data-height="10"    height of the solid (cm, 2 to 40)
   data-mu="0.6"       coefficient of friction between the solid and the plane (0.05 to 2)
   data-alpha="20"     starting angle of the plane, in degrees (0 to 60)
   The centre of mass G is h/2 above the base for the cuboid and the cylinder and h/4 above it for the cone. The solid
   topples about the lower edge of its base when tan α > a/h_G (a = half the base, h_G = height of G) and slides when
   tan α > μ. The smaller critical angle is reached first as α increases.
   The geometry is plain functions, exported for Node tests (data/test_fm_topple.js). */
(function () {
  'use strict';
  const RAD = Math.PI / 180, DEG = 180 / Math.PI;
  const SHAPES = ['cuboid', 'cylinder', 'cone'];
  const LIM = { w: [1, 20], h: [2, 40], mu: [0.05, 2], alpha: [0, 60] };
  const W = typeof window !== 'undefined' ? window.W : undefined;

  /* ---- pure helpers ---- */
  function geometry(shape, w, h) {
    // a: distance along the slope from the lower edge of the base to the point of the base under G (half the base);
    // hG: height of G above the base; base: length of the base along the slope
    if (shape === 'cuboid') return { a: w / 2, hG: h / 2, base: w };
    if (shape === 'cylinder') return { a: w, hG: h / 2, base: 2 * w };
    return { a: w, hG: h / 4, base: 2 * w };
  }
  function critical(shape, w, h, mu) {
    const g = geometry(shape, w, h);
    const alphaT = Math.atan(g.a / g.hG) * DEG;
    const alphaS = Math.atan(mu) * DEG;
    const first = Math.abs(alphaT - alphaS) < 1e-9 ? 'both' : (alphaS < alphaT ? 'slides' : 'topples');
    return { alphaT, alphaS, first, a: g.a, hG: g.hG, base: g.base };
  }
  function footU(shape, w, h, alpha) {
    // where the vertical through G meets the plane, measured up the slope from the lower edge of the base
    const g = geometry(shape, w, h);
    return g.a - g.hG * Math.tan(alpha * RAD);
  }
  function stateAt(shape, w, h, mu, alpha) {
    const c = critical(shape, w, h, mu);
    const t = Math.tan(alpha * RAD);
    const outside = t > c.a / c.hG + 1e-12;     // G's vertical line has left the base
    const slipping = t > mu + 1e-12;            // friction needed exceeds mu R
    const result = alpha > Math.min(c.alphaT, c.alphaS) + 1e-9 ? c.first : 'stable';
    return { result, outside, slipping, crit: c };
  }
  const core = { geometry, critical, footU, stateAt };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting ---- */
  const d1 = (x) => (Math.round(x * 10) / 10).toFixed(1);
  const g3 = (x) => String(parseFloat(Number(x).toPrecision(3)));
  const clampNum = (v, lim) => Math.min(lim[1], Math.max(lim[0], v));
  function parseNum(src, lim, dflt, name, warn) {
    if (src == null || String(src).trim() === '') return dflt;
    const v = Number(src);
    if (!isFinite(v)) { warn.push(`data-${name} should be a number, so ${dflt} is used.`); return dflt; }
    if (v < lim[0] || v > lim[1]) { warn.push(`data-${name} should be from ${lim[0]} to ${lim[1]}, so ${clampNum(v, lim)} is used.`); return clampNum(v, lim); }
    return v;
  }

  W.register('fm-topple', function (el, o) {
    const warn = [];
    let shape = String(o.shape || 'cuboid').trim().toLowerCase();
    if (SHAPES.indexOf(shape) < 0) { warn.push('data-shape should be cuboid, cylinder or cone, so cuboid is used.'); shape = 'cuboid'; }
    const start = {
      shape,
      w: parseNum(o.width, LIM.w, 6, 'width', warn),
      h: parseNum(o.height, LIM.h, shape === 'cone' ? 20 : 10, 'height', warn),
      mu: parseNum(o.mu, LIM.mu, 0.6, 'mu', warn),
      alpha: parseNum(o.alpha, LIM.alpha, 20, 'alpha', warn),
    };
    const st = Object.assign({}, start);

    const { body } = W.frame(el, 'Toppling or sliding?', 'Tilt the plane and see which happens first');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    const setErr = (t) => { errBox.textContent = t; errBox.style.display = t ? '' : 'none'; };
    setErr(warn.join(' '));
    body.append(errBox);

    /* ---- controls ---- */
    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Shape of the solid' });
    const tabBtns = {};
    SHAPES.forEach((s) => {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': s === st.shape ? 'true' : 'false', onclick: () => { st.shape = s; syncTabs(); update(); } }, s.charAt(0).toUpperCase() + s.slice(1));
      tabBtns[s] = b; tabs.append(b);
    });
    function syncTabs() { SHAPES.forEach((s) => tabBtns[s].setAttribute('aria-pressed', s === st.shape ? 'true' : 'false')); }
    body.append(W.h('div', { class: 'w-row' }, tabs));

    const sAlpha = W.slider({ label: 'Angle of the plane α (degrees)', min: LIM.alpha[0], max: LIM.alpha[1], step: 0.5, value: st.alpha, fmt: (v) => d1(+v) + '°', oninput: (v) => { st.alpha = +v; update(); } });
    const sMu = W.slider({ label: 'Coefficient of friction μ', min: LIM.mu[0], max: LIM.mu[1], step: 0.05, value: st.mu, fmt: (v) => (+v).toFixed(2), oninput: (v) => { st.mu = +v; update(); } });
    const sW = W.slider({ label: 'Base: width (cuboid) or radius (cylinder, cone), cm', min: LIM.w[0], max: LIM.w[1], step: 0.5, value: st.w, fmt: (v) => g3(+v), oninput: (v) => { st.w = +v; update(); } });
    const sH = W.slider({ label: 'Height of the solid, cm', min: LIM.h[0], max: LIM.h[1], step: 0.5, value: st.h, fmt: (v) => g3(+v), oninput: (v) => { st.h = +v; update(); } });
    body.append(sAlpha.el, sMu.el, sW.el, sH.el);
    const resetBtn = W.h('button', { type: 'button', class: 'btn btn-sm btn-sec', 'aria-label': 'Reset the solid, friction and angle to their starting values', onclick: () => {
      Object.assign(st, start); sAlpha.set(st.alpha); sMu.set(st.mu); sW.set(st.w); sH.set(st.h); syncTabs(); update();
    } }, 'Reset');
    body.append(W.h('div', { class: 'w-row' }, resetBtn));

    const cv = W.canvas(body, { height: 340, draw, label: 'Side view of a solid on a tilted plane', describe });
    const R = W.readout([
      ['alpha', 'Plane angle α, tan α'],
      ['top', 'Toppling (tan α > a ÷ height of G)'],
      ['slide', 'Sliding (tan α > μ)'],
      ['first', 'As α increases, first'],
    ]);
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, 'Try it: raise α with μ = 0.8 and watch the cone slide first. Then set μ to 1.5: the dashed vertical line through G leaves the base and the cone topples. G is ¼ of the height up for a cone and ½ for the other solids; a is the half-width or radius of the base.'));

    /* ---- model ---- */
    let model = null;
    function update() {
      const s = stateAt(st.shape, st.w, st.h, st.mu, st.alpha);
      model = s;
      const c = s.crit;
      R.set('alpha', `${d1(st.alpha)}°, tan α = ${g3(Math.tan(st.alpha * RAD))}`);
      R.set('top', s.outside
        ? `G is outside the base: topples (tan α > ${g3(c.a / c.hG)}, critical angle ${d1(c.alphaT)}°)`
        : `G is above the base: no toppling yet (critical angle ${d1(c.alphaT)}°)`);
      R.set('slide', s.slipping
        ? `slides (tan α > μ = ${g3(st.mu)}, critical angle ${d1(c.alphaS)}°)`
        : `friction holds (critical angle ${d1(c.alphaS)}°)`);
      R.set('first', c.first === 'both'
        ? `both at ${d1(c.alphaT)}°: the two critical angles are equal`
        : c.first === 'slides'
          ? `it slides at ${d1(c.alphaS)}° (tan⁻¹ μ), before it would topple at ${d1(c.alphaT)}°`
          : `it topples at ${d1(c.alphaT)}° (tan⁻¹ of a ÷ h_G), before it would slide at ${d1(c.alphaS)}°`);
      cv.redraw();
    }
    function describe() {
      if (!model) return 'No picture yet.';
      const c = model.crit;
      const word = model.result === 'stable' ? 'It stays in place: the vertical through G meets the plane inside the base and friction holds.'
        : model.result === 'slides' ? 'It slides down the plane.'
          : model.result === 'topples' ? 'It topples over its lower edge.' : 'It slides and topples at the same angle.';
      return `Side view of a ${st.shape} on a plane at ${d1(st.alpha)} degrees, friction coefficient ${g3(st.mu)}. The critical angle for toppling is ${d1(c.alphaT)} degrees and for sliding ${d1(c.alphaS)} degrees. ${word}`;
    }

    /* ---- drawing ---- */
    function draw(ctx, w, h, c) {
      if (!(w > 80 && h > 80) || !model) return;
      const pad = { l: 10, r: 10, t: 30, b: 12 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      if (!(pw > 40 && ph > 40)) return;
      const g = geometry(st.shape, st.w, st.h);
      const D = Math.hypot(g.base, st.h);
      if (!(D > 0)) return;
      const Px = pad.l + pw * 0.5, Py = pad.t + ph * 0.66;
      const s = 0.92 * Math.min(pw / 2, ph * 0.62) / D;
      const ar = st.alpha * RAD, ta = Math.tan(ar);
      const res = model.result;
      const tip = (res === 'topples' || res === 'both') ? 22 : 0;
      const shift = res === 'slides' ? 0.5 * g.base * s : 0;
      const thb = (st.alpha + tip) * RAD;
      const ox = Px - shift * Math.cos(ar), oy = Py + shift * Math.sin(ar);
      const T = (u, v) => [ox + s * (u * Math.cos(thb) - v * Math.sin(thb)), oy - s * (u * Math.sin(thb) + v * Math.cos(thb))];
      const halo = (txt, x, y, col, align, bold) => {
        ctx.font = `${bold ? 700 : 600} 12px ${c.font}`; ctx.textBaseline = 'middle'; ctx.textAlign = align || 'left';
        ctx.lineWidth = 3; ctx.strokeStyle = c.card; ctx.lineJoin = 'round'; ctx.strokeText(txt, x, y);
        ctx.fillStyle = col; ctx.fillText(txt, x, y);
      };
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, 0, pw, h); ctx.clip();
      // the plane, with the ground under it shaded
      const yAt = (x) => Py - ta * (x - Px);
      ctx.fillStyle = c.ink3; ctx.globalAlpha = 0.14;
      ctx.beginPath(); ctx.moveTo(pad.l, yAt(pad.l)); ctx.lineTo(pad.l + pw, yAt(pad.l + pw)); ctx.lineTo(pad.l + pw, h); ctx.lineTo(pad.l, h); ctx.closePath(); ctx.fill();
      ctx.globalAlpha = 1;
      ctx.strokeStyle = c.ink; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(pad.l, yAt(pad.l)); ctx.lineTo(pad.l + pw, yAt(pad.l + pw)); ctx.stroke();
      // a horizontal reference and the angle
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(Px - 0.9 * D * s, Py); ctx.lineTo(Px, Py); ctx.stroke(); ctx.setLineDash([]);
      if (st.alpha > 0.4) {
        const rr = Math.min(40, 0.35 * D * s);
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.arc(Px, Py, rr, Math.PI, Math.PI + ar); ctx.stroke();
        halo('α', Px - rr - 12, Py - 2, c.ink2, 'right');
      }
      // the solid
      const pts = st.shape === 'cone' ? [[0, 0], [g.base, 0], [g.a, st.h]] : [[0, 0], [g.base, 0], [g.base, st.h], [0, st.h]];
      ctx.beginPath();
      pts.forEach((p, i) => { const q = T(p[0], p[1]); i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1]); });
      ctx.closePath();
      ctx.fillStyle = c.sc; ctx.globalAlpha = 0.16; ctx.fill(); ctx.globalAlpha = 1;
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2; ctx.stroke();
      if (st.shape !== 'cuboid') {
        const a0 = T(g.a, 0), a1 = T(g.a, st.h);
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 4]);
        ctx.beginPath(); ctx.moveTo(a0[0], a0[1]); ctx.lineTo(a1[0], a1[1]); ctx.stroke(); ctx.setLineDash([]);
      }
      // the base, heavier, when the solid sits on the plane
      if (tip === 0) {
        const b0 = T(0, 0), b1 = T(g.base, 0);
        ctx.strokeStyle = c.sc; ctx.lineWidth = 4; ctx.lineCap = 'round';
        ctx.beginPath(); ctx.moveTo(b0[0], b0[1]); ctx.lineTo(b1[0], b1[1]); ctx.stroke(); ctx.lineCap = 'butt';
      }
      // centre of mass and the vertical through it
      const G = T(g.a, g.hG);
      const gx = G[0], gy = G[1];
      const yPl = yAt(gx);
      if (yPl > gy) {
        const outside = model.outside;
        ctx.strokeStyle = outside ? c.red : c.ink2; ctx.lineWidth = outside ? 2 : 1.4; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(gx, gy); ctx.lineTo(gx, yPl); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = outside ? c.red : c.ink2;
        ctx.beginPath(); ctx.arc(gx, yPl, 3, 0, 2 * Math.PI); ctx.fill();
        if (tip === 0) halo(outside ? 'outside the base' : 'inside the base', gx + (outside ? -6 : 6), yPl + 14, outside ? c.red : c.ink2, outside ? 'right' : 'left');
      }
      ctx.fillStyle = c.red; ctx.beginPath(); ctx.arc(gx, gy, 4.5, 0, 2 * Math.PI); ctx.fill();
      halo('G', gx + 8, gy - 4, c.ink, 'left', true);
      // the pivot: the lower edge of the base
      const pv = T(0, 0);
      ctx.fillStyle = c.ink; ctx.beginPath(); ctx.arc(pv[0], pv[1], 3.4, 0, 2 * Math.PI); ctx.fill();
      halo('pivot', pv[0] - 8, pv[1] + 14, c.ink2, 'right');
      // sliding: show the direction
      if (res === 'slides') {
        const m0 = T(g.base / 2, 0), dx = -Math.cos(ar), dy = Math.sin(ar);
        ctx.strokeStyle = c.ink; ctx.fillStyle = c.ink; ctx.lineWidth = 2;
        const x0 = m0[0] + 8 * Math.sin(ar), y0 = m0[1] + 8 * Math.cos(ar);
        const x1 = x0 + dx * 38, y1 = y0 + dy * 38;
        ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x1 - dx * 9 - dy * 5, y1 - dy * 9 + dx * 5); ctx.lineTo(x1 - dx * 9 + dy * 5, y1 - dy * 9 - dx * 5); ctx.closePath(); ctx.fill();
      }
      ctx.restore();
      // the verdict, in words
      const verdict = res === 'stable' ? 'Stays put: G above the base'
        : res === 'slides' ? 'SLIDES: friction runs out first'
          : res === 'topples' ? 'TOPPLES: G is outside the base' : 'SLIDES and TOPPLES together';
      halo(verdict, pad.l + 2, 14, res === 'stable' ? c.ok : c.red, 'left', true);
    }

    update();
  });
})();
