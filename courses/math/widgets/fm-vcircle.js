/* fm-vcircle: a particle moving in a vertical circle without loss of energy (9231 Paper 3, Further Mechanics).
   data-mode="string|rod|outside"  string: light string; rod: light rod, tube or bead on a ring; outside: on the outside of a smooth sphere. Default string.
   data-u="7"   speed in m/s: at the lowest point (string, rod) or at the highest point (outside). Default 7 (string), 5 (rod), 0.5 (outside).
   data-r="1"   radius in m, 0.2 to 5. Default 1.
   data-m="0.5" mass in kg, 0.05 to 20. Default 0.5.
   g = 10 m/s^2 (stated on screen). The angle theta is measured from the lowest point (string, rod) or from the highest point (outside).
   Shows the path (the full circle, the swing, or the arc then the parabola after the string slackens or the particle leaves the sphere),
   the speed v and the tension, thrust or reaction at the chosen angle from energy and the radial equation, and what happens.
   Play runs the motion (RK4 integration of the angle). data/test_fm_vcircle.js tests the formulas against that integration.
   Try: <div class="widget" data-w="fm-vcircle" data-mode="string" data-u="7" data-r="1" data-m="0.5"></div> */
(function () {
  'use strict';
  const W = typeof window !== 'undefined' ? window.W : undefined;
  const G = 10, TAU = 2 * Math.PI;
  const MINUS = '−';

  /* ---- pure helpers (tested in Node) ---- */
  function analyse(mode, u, r) {
    // what happens, from the speed u (bottom for string and rod, top for outside)
    const k = u * u / (G * r);
    if (mode === 'string') {
      if (k >= 5 - 1e-9) return { kind: 'complete', k, crit: Math.sqrt(5 * G * r), thetaEnd: TAU };
      if (k <= 2 + 1e-9) return { kind: 'swing', k, crit: Math.sqrt(5 * G * r), thetaEnd: Math.acos(1 - k / 2) };
      const c = (2 - k) / 3, th = Math.acos(c);
      return { kind: 'slack', k, crit: Math.sqrt(5 * G * r), thetaEnd: th, cosL: c, vL: Math.sqrt(-G * r * c) };
    }
    if (mode === 'rod') {
      if (k >= 4 - 1e-9) return { kind: Math.abs(k - 4) < 1e-9 ? 'just' : 'complete', k, crit: Math.sqrt(4 * G * r), thetaEnd: Math.abs(k - 4) < 1e-9 ? Math.PI : TAU };
      return { kind: 'swing', k, crit: Math.sqrt(4 * G * r), thetaEnd: Math.acos(1 - k / 2) };
    }
    // outside: from the top
    if (k >= 1 - 1e-9) return { kind: 'off', k, crit: Math.sqrt(G * r), thetaEnd: 0, cosL: 1, vL: u };
    const c = (k + 2) / 3;
    return { kind: 'leave', k, crit: Math.sqrt(G * r), thetaEnd: Math.acos(c), cosL: c, vL: Math.sqrt(G * r * c) };
  }
  function v2At(mode, u, r, th) {
    return mode === 'outside' ? u * u + 2 * G * r * (1 - Math.cos(th)) : u * u - 2 * G * r * (1 - Math.cos(th));
  }
  function forceAt(mode, u, r, m, th) {
    // string, rod: tension T (negative = thrust in a rod); outside: normal reaction R
    const v2 = v2At(mode, u, r, th);
    return mode === 'outside' ? m * (G * Math.cos(th) - v2 / r) : m * (v2 / r + G * Math.cos(th));
  }
  function pos(mode, r, th) {
    return mode === 'outside' ? [r * Math.sin(th), r * Math.cos(th)] : [r * Math.sin(th), -r * Math.cos(th)];
  }
  function leaveState(mode, u, r) {
    // position and velocity at the moment the string slackens or the particle leaves the sphere
    const a = analyse(mode, u, r);
    if (a.kind !== 'slack' && a.kind !== 'leave' && a.kind !== 'off') return null;
    const th = a.thetaEnd, p = pos(mode, r, th), v = a.vL;
    const dir = mode === 'outside' ? [Math.cos(th), -Math.sin(th)] : [Math.cos(th), Math.sin(th)];
    return { x: p[0], y: p[1], vx: v * dir[0], vy: v * dir[1], th };
  }
  function simulate(mode, u, r, tmax, dt) {
    // RK4 on th'' = -+(g/r) sin th; returns the first event (slack or leaves) or null
    const s = mode === 'outside' ? 1 : -1;
    let th = 0, om = u / r, t = 0;
    const f = (a, b) => [b, s * (G / r) * Math.sin(a)];
    while (t < tmax) {
      const k1 = f(th, om), k2 = f(th + dt * k1[0] / 2, om + dt * k1[1] / 2);
      const k3 = f(th + dt * k2[0] / 2, om + dt * k2[1] / 2), k4 = f(th + dt * k3[0], om + dt * k3[1]);
      th += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6;
      om += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6;
      t += dt;
      const radial = mode === 'outside' ? G * Math.cos(th) - r * om * om : r * om * om + G * Math.cos(th);
      if (mode !== 'rod' && radial <= 0) return { th, v: Math.abs(r * om), t };
    }
    return null;
  }
  const core = { analyse, v2At, forceAt, pos, leaveState, simulate };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting and input ---- */
  function n3(x) {
    if (!isFinite(x)) return '—';
    let v = parseFloat(Number(x).toPrecision(3));
    if (Object.is(v, -0)) v = 0;
    return String(v).replace('-', MINUS);
  }
  const deg = (t) => n3(t * 180 / Math.PI) + '°';
  function parseNum(v, dflt, lo, hi, name, warn) {
    if (v == null || String(v).trim() === '') return dflt;
    const n = Number(String(v).replace(MINUS, '-'));
    if (!isFinite(n) || n < lo || n > hi) { warn.push(`${name} should be a number from ${lo} to ${hi}, so ${dflt} is used.`); return dflt; }
    return n;
  }
  const MODES = [['string', 'String'], ['rod', 'Rod or tube'], ['outside', 'Outside of a sphere']];
  const DEFAULT_U = { string: 7, rod: 5, outside: 0.5 };

  W.register('fm-vcircle', function (el, o) {
    const warn = [];
    let mode = MODES.some((x) => x[0] === o.mode) ? o.mode : 'string';
    if (o.mode != null && String(o.mode).trim() !== '' && mode !== o.mode) warn.push('data-mode should be string, rod or outside, so string is used.');
    const r = parseNum(o.r, 1, 0.2, 5, 'data-r', warn);
    const m = parseNum(o.m, 0.5, 0.05, 20, 'data-m', warn);
    const uMax = { string: Math.ceil(2 * Math.sqrt(5 * G * r)), rod: Math.ceil(2 * Math.sqrt(4 * G * r)), outside: Math.max(2, Math.ceil(2 * Math.sqrt(G * r))) };
    const uMin = { string: 0.5, rod: 0.5, outside: 0.1 };
    const u = {};
    MODES.forEach(([k]) => {
      let d = k === 'string' ? DEFAULT_U.string * Math.sqrt(r) : DEFAULT_U[k] * Math.sqrt(r);
      d = Math.min(uMax[k], Math.max(uMin[k], Math.round(d * 20) / 20));
      u[k] = d;
    });
    if (o.u != null && String(o.u).trim() !== '') {
      const x = parseNum(o.u, u[mode], uMin[mode], uMax[mode], 'data-u', warn);
      u[mode] = x;
    }
    let theta = 0;
    let sim = null;           // the running motion
    let playing = false;

    const { body } = W.frame(el, 'Motion in a vertical circle', 'Choose the situation, set the speed, drag the angle or press Play');
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

    const labelU = { string: 'Speed u at the lowest point (m/s)', rod: 'Speed u at the lowest point (m/s)', outside: 'Speed u at the top (m/s)' };
    const uS = {};
    MODES.forEach(([k]) => {
      uS[k] = W.slider({ label: labelU[k], min: uMin[k], max: uMax[k], step: 0.05, value: u[k], fmt: (v) => n3(v), oninput: (v) => { u[k] = Number(v); stopAll(); sim = null; update(true); } });
      uS[k].el.style.display = k === mode ? '' : 'none';
      body.append(uS[k].el);
    });
    const thS = W.slider({ label: 'Angle θ of the particle (degrees from the lowest point; from the top for the sphere)', min: 0, max: 360, step: 0.5, value: 0, fmt: (v) => n3(v) + '°', oninput: (v) => { stopAll(); sim = null; theta = Number(v) * Math.PI / 180; update(false); } });
    body.append(thS.el);
    const play = W.h('button', { type: 'button', class: 'btn btn-sm' }, 'Play');
    const reset = W.h('button', { type: 'button', class: 'btn btn-sm btn-sec' }, 'Reset');
    body.append(W.h('div', { class: 'w-row' }, play, reset));

    const cv = W.canvas(body, { height: 300, draw, label: 'Vertical circle diagram', describe });
    const R = W.readout([['v', 'Speed v at this angle'], ['f', 'Force'], ['crit', 'Critical speed'], ['out', 'What happens']]);
    body.append(R.el);
    const live = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.append(live);
    const TRY = {
      string: 'Try: slide u from 5 up to 8 and watch where the string goes slack (the dashed curve is the free flight afterwards). At u² = 5gr the tension at the top just reaches zero and the circle closes.',
      rod: 'Try: a rod can push, so u² = 4gr is enough to reach the top. Drag the angle to the top and see the force in the rod become a thrust. Below that speed the rod swings back.',
      outside: 'Try: start almost at rest and drag the angle until the reaction R falls to zero (cos θ = 2/3 from rest). Raise u towards √(gr) and the particle leaves earlier; at √(gr) or more it leaves at once.'
    };
    const noteEl = W.h('div', { class: 'w-note' });
    const setNote = () => { noteEl.textContent = 'Take g = 10 m s⁻²; radius ' + n3(r) + ' m and mass ' + n3(m) + ' kg, no energy lost. ' + TRY[mode]; };
    setNote();
    body.append(noteEl);

    /* ---- the geometry of the picture ---- */
    function viewBox() {
      return mode === 'outside' ? { x0: -2.3 * r, x1: 2.3 * r, y0: -0.3 * r, y1: 1.6 * r } : { x0: -2.3 * r, x1: 2.3 * r, y0: -1.4 * r, y1: 1.9 * r };
    }
    function mapper(w, h) {
      const v = viewBox();
      const s = Math.min(w / (v.x1 - v.x0), h / (v.y1 - v.y0));
      const cx = (v.x0 + v.x1) / 2, cy = (v.y0 + v.y1) / 2;
      return { s, v, X: (x) => w / 2 + (x - cx) * s, Y: (y) => h / 2 - (y - cy) * s };
    }
    function freeFlight(ls, step, tMax) {
      const pts = [], v = viewBox();
      for (let t = 0; t <= tMax; t += step) {
        const x = ls.x + ls.vx * t, y = ls.y + ls.vy * t - 0.5 * G * t * t;
        pts.push([x, y]);
        if (y < (mode === 'outside' ? 0 : v.y0) || x < v.x0 || x > v.x1) break;
      }
      return pts;
    }
    function maxTheta() {
      const a = analyse(mode, u[mode], r);
      return a.thetaEnd;
    }
    function syncAngleSlider() {
      const top = Math.max(0.5, Math.min(360, maxTheta() * 180 / Math.PI));
      thS.input.max = String(Math.ceil(top * 2) / 2);
      if (theta * 180 / Math.PI > top) theta = top * Math.PI / 180;
      thS.set(theta * 180 / Math.PI);
    }

    /* ---- text ---- */
    function whatHappens() {
      const a = analyse(mode, u[mode], r);
      if (mode === 'string') {
        if (a.kind === 'complete') return 'Completes the circle: the tension stays positive at the top (u² ≥ 5gr).';
        if (a.kind === 'swing') return `Swings back: rises to θ = ${deg(a.thetaEnd)} and returns, string always taut (u² ≤ 2gr).`;
        return `String slack at θ = ${deg(a.thetaEnd)} (v = ${n3(a.vL)} m s⁻¹), then free flight as a projectile.`;
      }
      if (mode === 'rod') {
        if (a.kind === 'just') return 'Just reaches the top, with speed zero there (u² = 4gr).';
        if (a.kind === 'complete') return 'Completes the circle: the rod can push, so speed at the top need only be above zero (u² ≥ 4gr).';
        return `Comes to rest at θ = ${deg(a.thetaEnd)} and swings back.`;
      }
      if (a.kind === 'off') return 'Leaves the sphere at once (u² ≥ gr), then follows a parabola.';
      return `Leaves the sphere at θ = ${deg(a.thetaEnd)} from the top, speed ${n3(a.vL)} m s⁻¹ (R = 0), then follows a parabola.`;
    }
    function fLabel(th) {
      const f = forceAt(mode, u[mode], r, m, th);
      if (mode === 'outside') return `Reaction R = ${n3(f)} N`;
      if (mode === 'rod') return f >= 0 ? `Tension in the rod = ${n3(f)} N` : `Thrust in the rod = ${n3(-f)} N`;
      return `Tension T = ${n3(Math.max(0, f))} N`;
    }
    function critText() {
      const a = analyse(mode, u[mode], r);
      const nm = mode === 'string' ? `√(5gr) = ${n3(a.crit)} m s⁻¹ at the bottom to complete the circle`
        : mode === 'rod' ? `√(4gr) = ${n3(a.crit)} m s⁻¹ at the bottom to reach the top`
          : `√(gr) = ${n3(a.crit)} m s⁻¹ at the top: faster than this and it leaves at once`;
      return nm;
    }
    function angleNow() {
      return sim && sim.phase === 'arc' ? sim.th : theta;
    }
    function update(redrawAll) {
      if (redrawAll) syncAngleSlider();
      const th = Math.min(angleNow(), maxTheta() + 1e-9);
      const v2 = v2At(mode, u[mode], r, th);
      R.set('v', v2 > 0 ? `${n3(Math.sqrt(v2))} m s⁻¹ (v² = ${n3(v2)})` : '0 m s⁻¹ (momentarily at rest)');
      R.set('f', fLabel(th));
      R.set('crit', critText());
      R.set('out', whatHappens());
      cv.redraw();
    }
    function describe() {
      const th = Math.min(angleNow(), maxTheta());
      return `Vertical circle of radius ${n3(r)} metres, ${MODES.find((x) => x[0] === mode)[1].toLowerCase()} case, speed ${n3(u[mode])} metres per second ${mode === 'outside' ? 'at the top' : 'at the lowest point'}. The particle is at angle ${deg(th)}. ${whatHappens()} ${fLabel(th)}.`;
    }

    /* ---- drawing ---- */
    function arrow(ctx, x0, y0, x1, y1, col, head) {
      const dx = x1 - x0, dy = y1 - y0, len = Math.hypot(dx, dy);
      if (!(len > 1)) return;
      ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
      const ux = dx / len, uy = dy / len, hh = Math.min(head, len * 0.6);
      ctx.beginPath(); ctx.moveTo(x1, y1);
      ctx.lineTo(x1 - hh * ux + hh * 0.45 * uy, y1 - hh * uy - hh * 0.45 * ux);
      ctx.lineTo(x1 - hh * ux - hh * 0.45 * uy, y1 - hh * uy + hh * 0.45 * ux);
      ctx.closePath(); ctx.fill();
    }
    function draw(ctx, w, h, col) {
      if (!(w > 80 && h > 80)) return;
      const M = mapper(w, h);
      if (!(M.s > 0) || !isFinite(M.s)) return;
      const { X, Y, s } = M;
      const a = analyse(mode, u[mode], r);
      const ox = X(0), oy = Y(0), pr = r * s;
      ctx.save();
      ctx.lineJoin = 'round'; ctx.lineCap = 'round';
      ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic';
      if (mode === 'outside') {
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(0, oy); ctx.lineTo(w, oy); ctx.stroke();
        ctx.beginPath(); ctx.arc(ox, oy, pr, Math.PI, TAU); ctx.closePath();
        ctx.globalAlpha = 0.35; ctx.fillStyle = col.rule2; ctx.fill(); ctx.globalAlpha = 1;
        ctx.strokeStyle = col.ink; ctx.lineWidth = 2; ctx.stroke();
      } else {
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.arc(ox, oy, pr, 0, TAU); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(ox, oy, 3, 0, TAU); ctx.fill();
      }
      // the path
      const endTh = a.thetaEnd;
      const nArc = 120;
      ctx.strokeStyle = col.sc; ctx.lineWidth = 3;
      const arcSpan = a.kind === 'swing' ? [-endTh, endTh] : [0, endTh];
      if (endTh > 0.001) {
        ctx.beginPath();
        for (let i = 0; i <= nArc; i++) {
          const t = arcSpan[0] + (arcSpan[1] - arcSpan[0]) * i / nArc, p = pos(mode, r, t);
          i ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1]));
        }
        ctx.stroke();
      }
      const ls = leaveState(mode, u[mode], r);
      if (ls) {
        const fl = freeFlight(ls, 0.01, 8);
        ctx.strokeStyle = col.sc2; ctx.lineWidth = 2.2; ctx.setLineDash([6, 5]);
        ctx.beginPath();
        fl.forEach((p, i) => { i ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1])); });
        ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(ls.x), Y(ls.y), 4.5, 0, TAU); ctx.fill();
        ctx.fillStyle = col.ink;
        const lx = X(ls.x), ly = Y(ls.y), txt = 'leaves here';
        const right = lx >= ox;
        ctx.textAlign = right ? 'left' : 'right';
        ctx.fillText(txt, lx + (right ? 10 : -10), ly - 6);
        ctx.textAlign = 'left';
      }
      // the particle
      let px, py, thP = null, inFlight = false;
      if (sim && (sim.phase === 'flight' || (sim.phase === 'done' && sim.t > 0))) { px = sim.x; py = sim.y; inFlight = true; }
      else { thP = Math.min(angleNow(), endTh); const p = pos(mode, r, thP); px = p[0]; py = p[1]; }
      const PX = X(px), PY = Y(py);
      if (sim && sim.trail && sim.trail.length > 1) {
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.4;
        ctx.beginPath(); sim.trail.forEach((p, i) => { i ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1])); }); ctx.stroke();
      }
      if (mode !== 'outside' && !inFlight) {
        ctx.strokeStyle = col.ink; ctx.lineWidth = mode === 'rod' ? 4 : 1.6;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(PX, PY); ctx.stroke();
      }
      const rad = Math.max(5, Math.min(10, pr * 0.08));
      ctx.fillStyle = col.sc; ctx.strokeStyle = col.ink; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(PX, PY, rad, 0, TAU); ctx.fill(); ctx.stroke();
      if (!inFlight) {
        // weight (down) and the contact force (toward the centre for T, away for R)
        const wl = 26;
        arrow(ctx, PX, PY + rad, PX, PY + rad + wl, col.ink2, 8);
        ctx.fillStyle = col.ink2; ctx.textAlign = 'left';
        ctx.fillText('mg', PX + 6, PY + rad + wl);
        const f = forceAt(mode, u[mode], r, m, thP);
        const len = Math.max(0, Math.min(64, 22 * Math.abs(f) / (m * G)));
        if (len > 3) {
          let dx = ox - PX, dy = oy - PY; const d = Math.hypot(dx, dy) || 1; dx /= d; dy /= d;
          let sgn = mode === 'outside' ? -1 : 1;
          if (mode === 'rod' && f < 0) sgn = -1;
          const sx = PX + dx * rad * sgn, sy = PY + dy * rad * sgn;
          arrow(ctx, sx, sy, sx + dx * len * sgn, sy + dy * len * sgn, col.red, 8);
          ctx.fillStyle = col.red;
          ctx.fillText(mode === 'outside' ? 'R' : (mode === 'rod' && f < 0 ? 'thrust' : 'T'), sx + dx * len * sgn + 6, sy + dy * len * sgn - 4);
        }
      }
      // the lowest or highest point label
      ctx.fillStyle = col.ink3;
      ctx.textAlign = 'right';
      if (mode === 'outside') ctx.fillText('top', ox - 16, Y(r) + 4);
      else ctx.fillText('lowest point', ox - 16, Y(-r) + 4);
      ctx.restore();
    }

    /* ---- animation ---- */
    function startSim() {
      const a = analyse(mode, u[mode], r);
      sim = { phase: 'arc', th: 0, om: u[mode] / r, t: 0, a, trail: [], x: 0, y: 0, vx: 0, vy: 0, ls: leaveState(mode, u[mode], r) };
      theta = 0; thS.set(0);
    }
    function stepSim(dt) {
      // RK4 of the angle; dt is real seconds, the motion runs at about 0.7 of real time
      const sgn = mode === 'outside' ? 1 : -1;
      const f = (aa, bb) => [bb, sgn * (G / r) * Math.sin(aa)];
      let left = dt * 0.7;
      while (left > 1e-9 && sim.phase === 'arc') {
        const hh = Math.min(left, 1 / 240); left -= hh;
        const k1 = f(sim.th, sim.om), k2 = f(sim.th + hh * k1[0] / 2, sim.om + hh * k1[1] / 2);
        const k3 = f(sim.th + hh * k2[0] / 2, sim.om + hh * k2[1] / 2), k4 = f(sim.th + hh * k3[0], sim.om + hh * k3[1]);
        sim.th += hh * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6;
        sim.om += hh * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6;
        const radial = mode === 'outside' ? G * Math.cos(sim.th) - r * sim.om * sim.om : r * sim.om * sim.om + G * Math.cos(sim.th);
        if (mode !== 'rod' && radial <= 0 && sim.ls) {
          sim.phase = 'flight'; sim.t = 0;
          sim.x = sim.ls.x; sim.y = sim.ls.y;
          // continue with the true state at the moment of leaving
          const p = pos(mode, r, sim.th), v = Math.abs(r * sim.om);
          const dir = mode === 'outside' ? [Math.cos(sim.th), -Math.sin(sim.th)] : [Math.cos(sim.th), Math.sin(sim.th)];
          sim.x0 = p[0]; sim.y0 = p[1]; sim.vx = v * dir[0] * Math.sign(sim.om || 1); sim.vy = v * dir[1] * Math.sign(sim.om || 1);
          sim.x = p[0]; sim.y = p[1];
        }
        if (sim.phase === 'arc') {
          const p = pos(mode, r, sim.th);
          if (!sim.trail.length || Math.hypot(p[0] - sim.trail[sim.trail.length - 1][0], p[1] - sim.trail[sim.trail.length - 1][1]) > 0.02 * r) sim.trail.push(p);
          if (sim.trail.length > 400) sim.trail.shift();
        }
      }
      if (sim.phase === 'flight') {
        sim.t += dt * 0.7;
        sim.x = sim.x0 + sim.vx * sim.t; sim.y = sim.y0 + sim.vy * sim.t - 0.5 * G * sim.t * sim.t;
        sim.trail.push([sim.x, sim.y]); if (sim.trail.length > 400) sim.trail.shift();
        const v = viewBox();
        if (sim.y < (mode === 'outside' ? 0 : v.y0) || sim.x < v.x0 || sim.x > v.x1 || sim.t > 8) { sim.phase = 'done'; return false; }
      }
      if (sim.phase === 'arc') {
        const kind = sim.a.kind;
        theta = (kind === 'complete') ? (((sim.th % TAU) + TAU) % TAU) : Math.abs(sim.th);
        thS.set(Math.min(theta, maxTheta()) * 180 / Math.PI);
      }
      return true;
    }
    let lastTs = null;
    const anim = W.animate(() => {
      if (!sim) return false;
      const now = typeof performance !== 'undefined' ? performance.now() : Date.now();
      if (lastTs == null) lastTs = now;
      const dt = Math.min(0.05, Math.max(0, (now - lastTs) / 1000));
      lastTs = now;
      const go = stepSim(dt);
      update(false);
      if (!go) { playing = false; play.textContent = 'Play'; }
      return go;
    }, { still: () => { sim = null; theta = Math.min(maxTheta(), Math.PI * 2) ; thS.set(theta * 180 / Math.PI); update(false); } });
    function stopAll() { anim.stop(); playing = false; play.textContent = 'Play'; lastTs = null; }
    play.addEventListener('click', () => {
      if (playing) { stopAll(); return; }
      if (W.reducedMotion && W.reducedMotion()) { anim.start(); return; }
      if (!sim || sim.phase === 'done') startSim();
      playing = true; play.textContent = 'Pause'; lastTs = null;
      anim.start();
    });
    reset.addEventListener('click', () => { stopAll(); sim = null; theta = 0; thS.set(0); update(false); });
    function setMode(k) {
      stopAll(); sim = null; mode = k; theta = 0;
      MODES.forEach(([kk]) => { tabBtns[kk].setAttribute('aria-pressed', String(kk === mode)); uS[kk].el.style.display = kk === mode ? '' : 'none'; });
      setNote();
      update(true);
    }
    syncAngleSlider();
    update(true);
  });
})();
