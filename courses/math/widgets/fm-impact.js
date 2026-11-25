/* fm-impact: oblique impact of a smooth sphere with a fixed wall, or of two smooth spheres (9231 Paper 3, Further Mechanics).
   data-mode="wall|spheres"  default wall.
   wall:    data-u="5"   speed before impact in m/s, 0.5 to 20. data-angle="40"  angle between the velocity and the wall, 1 to 89 degrees.
            data-e="0.6" coefficient of restitution, 0 to 1.  data-m="1" mass in kg, 0.1 to 10 (only the impulse and the energies need it).
   spheres: data-m1 data-m2 (kg, 0.1 to 10), data-u1 data-u2 (m/s, 0 to 20), data-angle1 data-angle2 (the direction of each velocity, in degrees
            measured from the line of centres, which points from A to B; A: -85 to 85, B: -180 to 180), data-e.
   Perpendicular components are unchanged; along the normal (or the line of centres) momentum is conserved and Newton's law applies.
   Defaults wall: u 5, angle 40, e 0.6, m 1. Defaults spheres: m1 2, m2 3, u1 10, angle1 30, u2 0, angle2 0, e 0.5.
   data-components="on" starts with the dashed components shown (default off).
   data/test_fm_impact.js tests the formulas. Try:
   <div class="widget" data-w="fm-impact" data-mode="wall" data-u="5" data-angle="40" data-e="0.6"></div> */
(function () {
  'use strict';
  const W = typeof window !== 'undefined' ? window.W : undefined;
  const RAD = Math.PI / 180, TAU = 2 * Math.PI;
  const MINUS = '−';

  /* ---- pure helpers (tested in Node) ---- */
  function normDeg(a) {
    let x = ((a + 180) % 360 + 360) % 360 - 180;      // in [-180, 180)
    if (x === -180) x = 180;
    return x;
  }
  function wallImpact(u, alphaDeg, e, m) {
    m = m == null ? 1 : m;
    const a = alphaDeg * RAD;
    const par = u * Math.cos(a), perp = u * Math.sin(a), perpAfter = e * perp;
    const speed = Math.hypot(par, perpAfter);
    const beta = Math.atan2(perpAfter, par) / RAD;             // angle with the wall after the impact
    const keB = 0.5 * m * u * u, keA = 0.5 * m * speed * speed;
    return { par, perp, perpAfter, speed, beta, impulse: m * (1 + e) * perp, keBefore: keB, keAfter: keA, keLost: keB - keA };
  }
  function spheresImpact(m1, m2, u1, th1, u2, th2, e) {
    const a = [u1 * Math.cos(th1 * RAD), u1 * Math.sin(th1 * RAD)];
    const b = [u2 * Math.cos(th2 * RAD), u2 * Math.sin(th2 * RAD)];
    const approach = a[0] - b[0];
    const keB = 0.5 * m1 * u1 * u1 + 0.5 * m2 * u2 * u2;
    if (!(approach > 1e-12)) {
      return { collides: false, approach, a, b, v1: a, v2: b, s1: u1, s2: u2, d1: normDeg(th1), d2: normDeg(th2), impulse: 0, keBefore: keB, keAfter: keB, keLost: 0 };
    }
    const M = m1 + m2, P = m1 * a[0] + m2 * b[0];
    const v1x = (P - m2 * e * approach) / M, v2x = (P + m1 * e * approach) / M;
    const v1 = [v1x, a[1]], v2 = [v2x, b[1]];
    const keA = 0.5 * m1 * (v1[0] * v1[0] + v1[1] * v1[1]) + 0.5 * m2 * (v2[0] * v2[0] + v2[1] * v2[1]);
    return {
      collides: true, approach, a, b, v1, v2,
      s1: Math.hypot(v1[0], v1[1]), s2: Math.hypot(v2[0], v2[1]),
      d1: Math.atan2(v1[1], v1[0]) / RAD, d2: Math.atan2(v2[1], v2[0]) / RAD,
      impulse: m2 * (v2x - b[0]), keBefore: keB, keAfter: keA, keLost: keB - keA
    };
  }
  const core = { normDeg, wallImpact, spheresImpact };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting and input ---- */
  function n3(x) {
    if (!isFinite(x)) return '—';
    let v = parseFloat(Number(x).toPrecision(3));
    if (Object.is(v, -0) || Math.abs(v) < 1e-9) v = 0;
    return String(v).replace('-', MINUS);
  }
  function d1(x) {
    if (!isFinite(x)) return '—';
    let v = Math.round(x * 10) / 10;
    if (Object.is(v, -0)) v = 0;
    return String(v.toFixed(1)).replace('-', MINUS) + '°';
  }
  function parseNum(v, dflt, lo, hi, name, warn) {
    if (v == null || String(v).trim() === '') return dflt;
    const n = Number(String(v).replace(MINUS, '-'));
    if (!isFinite(n) || n < lo || n > hi) { warn.push(`${name} should be a number from ${lo} to ${hi}, so ${dflt} is used.`); return dflt; }
    return n;
  }
  const MODES = [['wall', 'Sphere and wall'], ['spheres', 'Two spheres']];

  W.register('fm-impact', function (el, o) {
    const warn = [];
    let mode = MODES.some((x) => x[0] === o.mode) ? o.mode : 'wall';
    if (o.mode != null && String(o.mode).trim() !== '' && mode !== o.mode) warn.push('data-mode should be wall or spheres, so wall is used.');
    const S = {
      wall: {
        u: parseNum(o.u, 5, 0.5, 20, 'data-u', warn),
        alpha: parseNum(o.angle, 40, 1, 89, 'data-angle', warn),
        e: parseNum(o.e, 0.6, 0, 1, 'data-e', warn),
        m: parseNum(o.m, 1, 0.1, 10, 'data-m', warn)
      },
      sph: {
        m1: parseNum(o.m1, 2, 0.1, 10, 'data-m1', warn),
        m2: parseNum(o.m2, 3, 0.1, 10, 'data-m2', warn),
        u1: parseNum(o.u1, 10, 0, 20, 'data-u1', warn),
        a1: parseNum(o.angle1, 30, -85, 85, 'data-angle1', warn),
        u2: parseNum(o.u2, 0, 0, 20, 'data-u2', warn),
        a2: parseNum(o.angle2, 0, -180, 180, 'data-angle2', warn),
        e: parseNum(o.e, 0.5, 0, 1, 'data-e', warn)
      }
    };
    let comps = String(o.components || '').toLowerCase() === 'on';

    const { body } = W.frame(el, 'Oblique impact', 'Choose a wall or two spheres, change the numbers and watch the velocities before and after');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose the situation' });
    const tabBtns = {};
    MODES.forEach(([k, label]) => {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': String(k === mode) }, label);
      b.addEventListener('click', () => setMode(k));
      tabBtns[k] = b; tabs.append(b);
    });
    body.append(W.h('div', { class: 'w-row' }, tabs));

    const mk = (label, min, max, step, value, set) => W.sliderNum({ label, min, max, step, value, oninput: (v) => { set(Number(v)); update(); } });
    const wallBox = W.h('div', {});
    const wS = {
      u: mk('Speed u before the impact (m/s)', 0.5, 20, 0.5, S.wall.u, (v) => { S.wall.u = v; }),
      alpha: mk('Angle α between the velocity and the wall (degrees)', 1, 89, 1, S.wall.alpha, (v) => { S.wall.alpha = v; }),
      e: mk('Coefficient of restitution e', 0, 1, 0.01, S.wall.e, (v) => { S.wall.e = v; }),
      m: mk('Mass of the sphere (kg)', 0.1, 10, 0.1, S.wall.m, (v) => { S.wall.m = v; })
    };
    Object.values(wS).forEach((s) => wallBox.append(s.el));
    const spBox = W.h('div', {});
    const pS = {
      m1: mk('Mass of A (kg)', 0.1, 10, 0.1, S.sph.m1, (v) => { S.sph.m1 = v; }),
      m2: mk('Mass of B (kg)', 0.1, 10, 0.1, S.sph.m2, (v) => { S.sph.m2 = v; }),
      u1: mk('Speed of A before (m/s)', 0, 20, 0.5, S.sph.u1, (v) => { S.sph.u1 = v; }),
      a1: mk('Direction of A, from the line of centres (degrees)', -85, 85, 1, S.sph.a1, (v) => { S.sph.a1 = v; }),
      u2: mk('Speed of B before (m/s)', 0, 20, 0.5, S.sph.u2, (v) => { S.sph.u2 = v; }),
      a2: mk('Direction of B, from the line of centres (degrees)', -180, 180, 1, S.sph.a2, (v) => { S.sph.a2 = v; }),
      e: mk('Coefficient of restitution e', 0, 1, 0.01, S.sph.e, (v) => { S.sph.e = v; })
    };
    Object.values(pS).forEach((s) => spBox.append(s.el));
    body.append(wallBox, spBox);

    const cbId = W.uid('fmi-comp');
    const cb = W.h('input', { type: 'checkbox', id: cbId });
    cb.checked = comps;
    cb.addEventListener('change', () => { comps = cb.checked; update(); });
    const cbRow = W.h('label', { class: 'w-ctl', for: cbId, style: { display: 'flex', alignItems: 'center', gap: '8px' } }, cb, W.h('span', { class: 'w-lab' }, 'Show components (dashed)'));
    body.append(W.h('div', { class: 'w-row' }, cbRow));

    const cv = W.canvas(body, { height: 290, draw, label: 'Oblique impact diagram', describe });
    const R = W.readout([['bef', 'Before'], ['aft', 'After'], ['imp', 'Impulse'], ['ke', 'Kinetic energy'], ['note', 'Components']]);
    body.append(R.el);
    const noteEl = W.h('div', { class: 'w-note' });
    body.append(noteEl);
    const TRY = {
      wall: 'Try: set e = 1 and the angle after equals the angle before; set e = 0 and the sphere slides along the wall. The dashed horizontal component never changes.',
      spheres: 'Try: make the masses equal, set e = 1, let B start at rest and change the direction of A: the two paths after the impact are always at 90° to each other. Then lower e.'
    };
    function setNote() {
      noteEl.textContent = 'Smooth surfaces, so the impulse acts along the normal to the wall, or along the line of centres. Speeds in m s⁻¹, masses in kg. ' + TRY[mode];
    }

    /* ---- results ---- */
    function wallRes() { const s = S.wall; return wallImpact(s.u, s.alpha, s.e, s.m); }
    function sphRes() { const s = S.sph; return spheresImpact(s.m1, s.m2, s.u1, s.a1, s.u2, s.a2, s.e); }
    function update() {
      if (mode === 'wall') {
        const s = S.wall, r = wallRes();
        R.set('bef', `${n3(s.u)} m s⁻¹ at ${d1(s.alpha)} to the wall`);
        R.set('aft', `${n3(r.speed)} m s⁻¹ at ${d1(r.beta)} to the wall`);
        R.set('imp', `${n3(r.impulse)} N s, perpendicular to the wall`);
        R.set('ke', `before ${n3(r.keBefore)} J, after ${n3(r.keAfter)} J, lost ${n3(r.keLost)} J`);
        R.set('note', `parallel to the wall ${n3(r.par)} m s⁻¹ before and after (unchanged); perpendicular ${n3(r.perp)} before, ${n3(r.perpAfter)} after (× e, reversed)`);
      } else {
        const s = S.sph, r = sphRes();
        R.set('bef', `A ${n3(s.u1)} m s⁻¹ at ${d1(s.a1)}; B ${n3(s.u2)} m s⁻¹ at ${d1(normDeg(s.a2))} (from the line of centres)`);
        if (!r.collides) {
          R.set('aft', 'No impact: A is not approaching B along the line of centres, so nothing changes.');
          R.set('imp', '0 N s');
          R.set('ke', `${n3(r.keBefore)} J, unchanged`);
          R.set('note', 'The spheres are not closing along the line of centres.');
        } else {
          R.set('aft', `A ${n3(r.s1)} m s⁻¹ at ${d1(r.d1)}; B ${n3(r.s2)} m s⁻¹ at ${d1(r.d2)}`);
          R.set('imp', `${n3(r.impulse)} N s along the line of centres`);
          R.set('ke', `before ${n3(r.keBefore)} J, after ${n3(r.keAfter)} J, lost ${n3(r.keLost)} J`);
          R.set('note', `perpendicular components unchanged: A ${n3(r.a[1])}, B ${n3(r.b[1])} m s⁻¹; along the line, A ${n3(r.a[0])} to ${n3(r.v1[0])}, B ${n3(r.b[0])} to ${n3(r.v2[0])} m s⁻¹`);
        }
      }
      cv.redraw();
    }
    function describe() {
      if (mode === 'wall') {
        const s = S.wall, r = wallRes();
        return `A sphere hits a smooth wall at ${n3(s.u)} metres per second, ${d1(s.alpha)} to the wall, with e = ${n3(s.e)}. After the impact it moves at ${n3(r.speed)} metres per second, ${d1(r.beta)} to the wall. The component parallel to the wall, ${n3(r.par)}, is unchanged; the perpendicular component falls from ${n3(r.perp)} to ${n3(r.perpAfter)}.`;
      }
      const s = S.sph, r = sphRes();
      if (!r.collides) return `Two spheres, masses ${n3(s.m1)} and ${n3(s.m2)} kilograms, that are not approaching along the line of centres, so there is no impact.`;
      return `Two smooth spheres, masses ${n3(s.m1)} and ${n3(s.m2)} kilograms, with e = ${n3(s.e)}. After the impact A moves at ${n3(r.s1)} metres per second at ${d1(r.d1)} to the line of centres and B at ${n3(r.s2)} metres per second at ${d1(r.d2)}. Kinetic energy lost ${n3(r.keLost)} joules.`;
    }

    /* ---- drawing ---- */
    function arrow(ctx, x0, y0, x1, y1, col, lw, head, dash) {
      const dx = x1 - x0, dy = y1 - y0, len = Math.hypot(dx, dy);
      if (!(len > 1)) return;
      ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = lw;
      ctx.setLineDash(dash || []);
      const hh = Math.min(head, len * 0.6), ux = dx / len, uy = dy / len;
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1 - ux * hh * 0.7, y1 - uy * hh * 0.7); ctx.stroke();
      ctx.setLineDash([]);
      ctx.beginPath(); ctx.moveTo(x1, y1);
      ctx.lineTo(x1 - hh * ux + hh * 0.45 * uy, y1 - hh * uy - hh * 0.45 * ux);
      ctx.lineTo(x1 - hh * ux - hh * 0.45 * uy, y1 - hh * uy + hh * 0.45 * ux);
      ctx.closePath(); ctx.fill();
    }
    function line(ctx, x0, y0, x1, y1, col, lw, dash) {
      ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.setLineDash(dash || []);
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke(); ctx.setLineDash([]);
    }
    function legend(ctx, col, y) {
      ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      line(ctx, 10, y - 4, 34, y - 4, col.ink2, 2);
      ctx.fillStyle = col.ink2; ctx.fillText('before', 40, y);
      line(ctx, 96, y - 4, 120, y - 4, col.sc, 3);
      ctx.fillStyle = col.ink2; ctx.fillText('after', 126, y);
    }
    function drawWall(ctx, w, h, col) {
      const s = S.wall, r = wallRes();
      const wy = Math.round(h * 0.80), px = w / 2;
      const kx = (px - 72) / Math.max(r.par, 1e-9), ky = (wy - 46) / Math.max(r.perp, 1e-9);
      const k = Math.min(kx, ky, 90);
      if (!(k > 0) || !isFinite(k)) return;
      // the wall, hatched
      ctx.strokeStyle = col.ink; ctx.lineWidth = 3;
      line(ctx, 8, wy, w - 8, wy, col.ink, 3);
      ctx.strokeStyle = col.ink3; ctx.lineWidth = 1;
      for (let x = 14; x < w - 8; x += 12) line(ctx, x, wy + 1, x - 8, wy + 9, col.ink3, 1);
      // the normal
      line(ctx, px, wy, px, wy - Math.min(wy - 30, 120), col.ink3, 1, [4, 4]);
      const tx = px - r.par * k, ty = wy - r.perp * k;       // tail of the incoming arrow
      const hx = px + r.par * k, hy = wy - r.perpAfter * k;  // head of the outgoing arrow
      if (comps) {
        const dash = [5, 4];
        line(ctx, tx, ty, tx, wy, col.ink3, 1.4, dash);                // perpendicular component before
        arrow(ctx, tx, wy - 6, px, wy - 6, col.ink3, 1.6, 7, dash);     // parallel component, unchanged
        line(ctx, hx, hy, hx, wy, col.sc2, 1.4, dash);
        arrow(ctx, px, wy - 6, hx, wy - 6, col.sc2, 1.6, 7, dash);
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ctx.fillText('u cos α', (tx + px) / 2, wy + 26);
        ctx.fillText('u cos α', (px + hx) / 2, wy + 26);
        ctx.fillStyle = col.ink2; ctx.textAlign = 'left';
        ctx.fillText('u sin α', tx + 6, (ty + wy) / 2);
        ctx.fillText('e u sin α', hx + 6, (hy + wy) / 2 + 4);
      }
      arrow(ctx, tx, ty, px, wy, col.ink2, 2.2, 10);
      arrow(ctx, px, wy, hx, hy, col.sc, 3.2, 12);
      // angle arcs
      const a = s.alpha * RAD, b = r.beta * RAD;
      ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.arc(px, wy, 32, -Math.PI, -Math.PI + a, false); ctx.stroke();
      ctx.strokeStyle = col.sc; ctx.beginPath(); ctx.arc(px, wy, 42, -b, 0, false); ctx.stroke();
      ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
      ctx.fillText('α', px - 54 * Math.cos(a / 2), Math.min(wy - 16, wy - 54 * Math.sin(a / 2) + 4));
      ctx.fillStyle = col.sc;
      ctx.fillText('β', px + 58 * Math.cos(b / 2), Math.min(wy - 16, wy - 58 * Math.sin(b / 2) + 4));
      ctx.textAlign = 'left';
      ctx.fillStyle = col.ink3; ctx.textAlign = 'left';
      ctx.fillText('normal', px + 6, wy - Math.min(wy - 30, 120) + 12);
      // text
      legend(ctx, col, 16);
      ctx.fillStyle = col.ink2; ctx.textAlign = 'right';
      ctx.fillText(`u = ${n3(s.u)} m/s, α = ${d1(s.alpha)}`, w - 10, 16);
      ctx.fillStyle = col.sc;
      ctx.fillText(`v = ${n3(r.speed)} m/s, β = ${d1(r.beta)}`, w - 10, 32);
    }
    function drawSpheres(ctx, w, h, col) {
      const s = S.sph, r = sphRes();
      const rad1 = 12 + 7 * Math.cbrt(s.m1), rad2 = 12 + 7 * Math.cbrt(s.m2);
      const cx = w / 2, cy = h / 2 + 8;
      const ax = cx - rad1, bx = cx + rad2;
      const speeds = [s.u1, s.u2, r.s1, r.s2];
      const maxS = Math.max(...speeds, 0.5);
      const k = Math.min(60, (ax - 14) / maxS, (w - bx - 14) / maxS, (cy - 40) / maxS, (h - cy - 14) / maxS);
      if (!(k > 0) || !isFinite(k) || rad1 > w / 4 || rad2 > w / 4) return;
      // line of centres and the common tangent
      line(ctx, 8, cy, w - 8, cy, col.ink3, 1, [5, 4]);
      line(ctx, cx, cy - 56, cx, cy + 56, col.ink3, 1, [5, 4]);
      ctx.fillStyle = col.ink3; ctx.textAlign = 'left';
      ctx.fillText('line of centres', 10, cy + 14);
      // the spheres
      ctx.lineWidth = 2;
      ctx.fillStyle = col.card || col.sheet; ctx.strokeStyle = col.ink;
      ctx.beginPath(); ctx.arc(ax, cy, rad1, 0, TAU); ctx.fill(); ctx.stroke();
      ctx.beginPath(); ctx.arc(bx, cy, rad2, 0, TAU); ctx.fill(); ctx.stroke();
      ctx.fillStyle = col.ink; ctx.textAlign = 'center';
      ctx.fillText('A', ax, cy + 4); ctx.fillText('B', bx, cy + 4);
      const vec = (x0, y0, v, c, lw, dash) => arrow(ctx, x0, y0, x0 + v[0] * k, y0 - v[1] * k, c, lw, 10, dash);
      if (comps) {
        const dash = [5, 4];
        [[ax, r.a, r.v1], [bx, r.b, r.v2]].forEach(([x0, bef, aft]) => {
          vec(x0, cy, [bef[0], 0], col.ink3, 1.5, dash); vec(x0, cy, [0, bef[1]], col.ink3, 1.5, dash);
          vec(x0, cy, [aft[0], 0], col.sc2, 1.5, dash); vec(x0, cy, [0, aft[1]], col.sc2, 1.5, dash);
        });
      }
      vec(ax, cy, r.a, col.ink2, 2.2);
      vec(bx, cy, r.b, col.ink2, 2.2);
      if (r.collides) { vec(ax, cy, r.v1, col.sc, 3.2); vec(bx, cy, r.v2, col.sc, 3.2); }
      ctx.textAlign = 'left';
      legend(ctx, col, 16);
      ctx.fillStyle = col.ink2; ctx.textAlign = 'right';
      ctx.fillText(`A: ${n3(r.s1)} m/s at ${d1(r.d1)}`, w - 10, 16);
      ctx.fillText(`B: ${n3(r.s2)} m/s at ${d1(r.d2)}`, w - 10, 32);
      if (!r.collides) { ctx.textAlign = 'center'; ctx.fillStyle = col.red; ctx.fillText('not approaching: no impact', w / 2, h - 10); }
    }
    function draw(ctx, w, h, col) {
      if (!(w > 120 && h > 120)) return;
      ctx.save();
      ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic';
      if (mode === 'wall') drawWall(ctx, w, h, col); else drawSpheres(ctx, w, h, col);
      ctx.restore();
    }

    function setMode(k) {
      mode = k;
      MODES.forEach(([kk]) => tabBtns[kk].setAttribute('aria-pressed', String(kk === mode)));
      wallBox.style.display = mode === 'wall' ? '' : 'none';
      spBox.style.display = mode === 'spheres' ? '' : 'none';
      setNote();
      update();
    }
    setMode(mode);
  });
})();
