/* phys-orbit: a satellite in a circular orbit round the Earth, the Moon, Mars or Jupiter (phys.gravity).
   data-body="earth|moon|mars|jupiter"   data-r="42200" orbital radius in km, from 1.05 R to 100 R of the body
   data-m="1000" satellite mass in kg, 100–10 000.   data-view="orbit|kepler" the graph shown first.
   Model: GMm/r² = mv²/r, so v = √(GM/r), T = 2πr/v, g = GM/r², φ = −GM/r, E_K = GMm/2r, E_P = −GMm/r.
   The animation is a time-lapse: every period is sped up by the same factor, shown on the canvas.
   For the Earth a marker on the Equator turns once per 24 h in the same time-lapse. */
(function () {
  'use strict';
  W.register('phys-orbit', function (el, opts) {
    const G = 6.67e-11, DAY = 86400, TAU = 2 * Math.PI;
    const BODIES = {
      earth:   { name: 'Earth',   M: 5.97e24, R: 6.37e6 },
      moon:    { name: 'Moon',    M: 7.35e22, R: 1.74e6 },
      mars:    { name: 'Mars',    M: 6.42e23, R: 3.39e6 },
      jupiter: { name: 'Jupiter', M: 1.90e27, R: 6.99e7 }
    };
    const FACTORS = [[1000, '×1 000'], [8640, '×8 640'], [86400, '×86 400']];
    const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
    const sup = (e) => String(e).split('').map((ch) => SUP[ch] || ch).join('');
    const sci = (x, sf) => sci0(x, sf).replace(/^-/, '−');
    function sci0(x, sf) {
      if (!isFinite(x)) return '–';
      if (x === 0) return '0';
      let e = Math.floor(Math.log10(Math.abs(x)));
      let m = x / Math.pow(10, e);
      if (parseFloat(Math.abs(m).toPrecision(sf)) >= 10) { m /= 10; e += 1; }
      if (e >= -2 && e <= 3) return parseFloat(x.toPrecision(sf)).toString();
      return m.toFixed(sf - 1) + ' × 10' + sup(e);
    }
    const spaced = (n) => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    const fmtKm = (km) => (km < 1e7 ? spaced(km) : sci(km, 3)) + ' km';
    function fmtTime(s) {
      if (s < 120) return sci(s, 3) + ' s';
      if (s < 7200) return sci(s / 60, 3) + ' min';
      if (s < 2 * DAY) return sci(s / 3600, 3) + ' h';
      return sci(s / DAY, 3) + ' days';
    }
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };

    const { body } = W.frame(el, 'Satellite in a circular orbit', 'Change the radius and watch the speed, period and energy');
    const notes = [];
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });

    // ---- starting state, validated ----
    let key = 'earth';
    if (opts.body !== undefined && opts.body !== '') {
      const k = String(opts.body).toLowerCase();
      if (BODIES[k]) key = k;
      else notes.push('data-body "' + opts.body + '" is not one of earth, moon, mars, jupiter, so the Earth is used.');
    }
    const B = () => BODIES[key];
    const U_MIN = Math.log10(1.05), U_MAX = 2;          // u = log10(r / R)
    const st = { u: Math.log10(4), m: 1000, f: 1, view: 'orbit', t: 0, playing: false };
    if (opts.r !== undefined && opts.r !== '') {
      const km = parseFloat(opts.r);
      if (!isFinite(km) || km <= 0) notes.push('data-r "' + opts.r + '" is not a positive number of kilometres, so a default radius is used.');
      else {
        const u = Math.log10(km * 1000 / B().R);
        st.u = Math.min(U_MAX, Math.max(U_MIN, u));
        if (st.u !== u) notes.push('data-r = ' + opts.r + ' km is outside the range 1.05 R to 100 R for the ' + B().name + ', so ' + fmtKm(Math.pow(10, st.u) * B().R / 1000) + ' is used.');
      }
    }
    if (opts.view !== undefined && opts.view !== '') {
      if (opts.view === 'kepler' || opts.view === 'orbit') st.view = opts.view;
      else notes.push('data-view "' + opts.view + '" is not orbit or kepler, so the orbit view is shown.');
    }
    if (opts.m !== undefined && opts.m !== '') {
      const m = parseFloat(opts.m);
      if (!isFinite(m)) notes.push('data-m "' + opts.m + '" is not a number, so 1000 kg is used.');
      else {
        st.m = Math.min(10000, Math.max(100, m));
        if (st.m !== m) notes.push('data-m = ' + opts.m + ' is outside 100–10 000 kg, so ' + st.m + ' kg is used.');
      }
    }
    if (notes.length) { err.textContent = notes.join(' '); err.style.display = ''; }

    // ---- physics ----
    function model() {
      const b = B(), r = Math.pow(10, st.u) * b.R, GM = G * b.M;
      const v = Math.sqrt(GM / r), T = TAU * r / v;
      return {
        r, GM, v, T, h: r - b.R, g: GM / (r * r), phi: -GM / r,
        ek: GM * st.m / (2 * r), ep: -GM * st.m / r, et: -GM * st.m / (2 * r),
        k: 4 * Math.PI * Math.PI / GM
      };
    }

    // ---- controls ----
    function tabs(items, get, set, label) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': label });
      const btns = items.map(([v, text]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); } }, text));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    const bodyTabs = tabs(Object.keys(BODIES).map((k) => [k, BODIES[k].name]), () => key, (k) => { key = k; mkRadius(); showEarth(); update(); }, 'Body');
    const viewTabs = tabs([['orbit', 'Orbit'], ['kepler', 'T² against r³']], () => st.view, (v) => { st.view = v; showEarth(); update(); }, 'Graph');
    const speedTabs = tabs(FACTORS.map((f, i) => [i, f[1]]), () => st.f, (i) => { st.f = i; update(); }, 'Time-lapse factor');

    let rs = null;
    const radiusHolder = W.h('div', { class: 'w-ctl-holder' });
    function mkRadius() {
      rs = W.slider({
        label: 'Orbital radius (distance from the centre)', min: U_MIN, max: U_MAX, step: 0.0005, value: st.u,
        fmt: (u) => fmtKm(Math.pow(10, u) * B().R / 1000) + ' = ' + sci(Math.pow(10, u), 3) + ' R',
        oninput: (v) => { st.u = num(v, st.u, U_MIN, U_MAX); update(); }
      });
      radiusHolder.replaceChildren(rs.el);
    }
    mkRadius();
    const sM = W.sliderNum({ label: 'Satellite mass / kg', min: 100, max: 10000, step: 100, value: st.m, oninput: (v) => { st.m = num(v, st.m, 100, 10000); update(); } });

    let simT = 0, last = 0;
    const anim = W.animate(() => {
      const now = performance.now();
      const dt = Math.min(0.1, (now - last) / 1000);
      last = now; simT += dt * FACTORS[st.f][0]; c.redraw();
      return true;
    }, { still: () => {} });
    const reduced = W.reducedMotion();
    function setPlaying(on) {
      if (on && !st.playing) { last = performance.now(); anim.start(); }
      if (!on && st.playing) anim.stop();
      st.playing = on;
      playBtn.textContent = on ? 'Pause' : 'Play';
    }
    const playBtn = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => setPlaying(!st.playing) }, 'Pause');
    const stepBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { setPlaying(false); simT += model().T / 16; c.redraw(); } }, 'Step');
    const snapBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => {
      const m = model(), b = B();
      const r = Math.cbrt(m.GM * DAY * DAY / (TAU * TAU));
      st.u = Math.min(U_MAX, Math.max(U_MIN, Math.log10(r / b.R)));
      mkRadius(); update();
    } }, 'Snap to geostationary');
    function showEarth() {
      snapBtn.style.display = key === 'earth' ? '' : 'none';
      if (typeof legend !== 'undefined') legend.style.display = key === 'earth' && st.view === 'orbit' ? 'flex' : 'none';
    }
    if (reduced) playBtn.style.display = 'none';

    body.append(
      W.h('div', { class: 'w-row' }, bodyTabs, viewTabs),
      W.h('div', { class: 'w-row' }, radiusHolder, sM.el),
      W.h('div', { class: 'w-row' }, speedTabs, playBtn, stepBtn, snapBtn)
    );

    // ---- canvas ----
    function label(ctx, col, txt, x, y, color) {
      ctx.font = '600 12px ' + col.font;
      ctx.fillStyle = color || col.ink2; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText(txt, x, y);
    }
    function niceCeil(v) {
      const e = Math.pow(10, Math.floor(Math.log10(v)));
      const m = v / e;
      return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 5 ? 5 : 10) * e;
    }
    function drawOrbit(ctx, w, h, col) {
      const m = model(), b = B();
      const cx = w / 2, cy = h / 2, rp = Math.max(30, Math.min(w, h) / 2 - 26);
      const pr = Math.max(3, rp * b.R / m.r);
      ctx.save();
      ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([5, 5]);
      ctx.beginPath(); ctx.arc(cx, cy, rp, 0, TAU); ctx.stroke(); ctx.setLineDash([]);
      ctx.globalAlpha = 0.22; ctx.fillStyle = col.sc; ctx.beginPath(); ctx.arc(cx, cy, pr, 0, TAU); ctx.fill(); ctx.globalAlpha = 1;
      ctx.strokeStyle = col.sc; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx, cy, pr, 0, TAU); ctx.stroke();
      const a = TAU * simT / m.T;
      const sx = cx + rp * Math.cos(a), sy = cy - rp * Math.sin(a);
      const geo = key === 'earth' && Math.abs(m.T - DAY) / DAY < 0.01;
      if (key === 'earth') {
        const be = TAU * simT / DAY;
        const mx = cx + pr * Math.cos(be), my = cy - pr * Math.sin(be);
        ctx.strokeStyle = geo ? col.ok : col.rule2; ctx.lineWidth = geo ? 2 : 1; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(sx, sy); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.ok; ctx.beginPath(); ctx.arc(mx, my, 4.5, 0, TAU); ctx.fill();
        ctx.strokeStyle = col.card; ctx.lineWidth = 1.5; ctx.stroke();
      }
      ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(sx, sy, 5.5, 0, TAU); ctx.fill();
      ctx.restore();
      label(ctx, col, 'r = ' + sci(m.r / b.R, 3) + ' R  (planet to scale)', 8, 16);
      const f = FACTORS[st.f][0];
      label(ctx, col, 'Time-lapse ×' + spaced(f) + ': 1 s of animation = ' + fmtTime(f), 8, h - 8);
    }
    function drawKepler(ctx, w, h, col) {
      const m = model();
      const X1 = niceCeil(Math.pow(m.r, 3) * 1.05), Y1 = m.k * X1;
      const ex = Math.floor(Math.log10(X1)), ey = Math.floor(Math.log10(Y1));
      const sx = Math.pow(10, ex), sy = Math.pow(10, ey);
      const view = { x0: 0, x1: X1 / sx, y0: 0, y1: Y1 / sy };
      const ax = W.axes(ctx, w, h, view, col, {
        pad: { l: 46, r: 16, t: 14, b: 34 },
        xlabel: 'r³ / 10' + sup(ex) + ' m³', ylabel: 'T² / 10' + sup(ey) + ' s²'
      });
      const { X, Y } = ax;
      ctx.save();
      ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
      ctx.strokeStyle = col.sc; ctx.lineWidth = 2.5; ctx.beginPath();
      ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(view.x1), Y(view.y1)); ctx.stroke();
      const px = Math.pow(m.r, 3) / sx, py = m.T * m.T / sy;
      ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(X(0), Y(py)); ctx.lineTo(X(px), Y(py)); ctx.lineTo(X(px), Y(0)); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(px), Y(py), 5.5, 0, TAU); ctx.fill();
      ctx.restore();
    }
    const c = W.canvas(body, {
      height: 300,
      draw(ctx, w, h, col) { if (st.view === 'orbit') drawOrbit(ctx, w, h, col); else drawKepler(ctx, w, h, col); }
    });

    const ro = W.readout([
      ['r', 'Orbital radius r (from the centre)'], ['h', 'Height above the surface'], ['v', 'Orbital speed v = √(GM/r)'],
      ['T', 'Period T'], ['g', 'Field strength g at the orbit'], ['phi', 'Potential φ = −GM/r'],
      ['ek', 'Kinetic energy'], ['ep', 'Potential energy'], ['et', 'Total energy'], ['geo', 'Geostationary?']
    ]);
    const dot = (color) => W.h('span', { style: { color: color } }, '●');
    const legend = W.h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '4px 16px', fontSize: '13px', color: 'var(--ink-2)', margin: '6px 0 0' } },
      W.h('span', {}, dot('var(--red)'), ' satellite'), W.h('span', {}, dot('var(--ok)'), ' point on the Equator, turning once in 24 h'));
    const note = W.h('div', { class: 'w-note' });
    body.append(legend, ro.el, note, err);

    function update() {
      const m = model(), b = B();
      if (reduced) simT = m.T / 8;
      ro.set('r', sci(m.r, 3) + ' m = ' + sci(m.r / b.R, 3) + ' R');
      ro.set('h', fmtKm(m.h / 1000));
      ro.set('v', sci(m.v, 3) + ' m s⁻¹');
      ro.set('T', sci(m.T, 3) + ' s = ' + fmtTime(m.T));
      ro.set('g', sci(m.g, 3) + ' N kg⁻¹');
      ro.set('phi', sci(m.phi, 3) + ' J kg⁻¹');
      ro.set('ek', sci(m.ek, 3) + ' J');
      ro.set('ep', sci(m.ep, 3) + ' J');
      ro.set('et', sci(m.et, 3) + ' J');
      if (key === 'earth') {
        const geo = Math.abs(m.T - DAY) / DAY < 0.01;
        ro.set('geo', geo ? 'Yes: T is within 1% of 24 h' : 'No (T is ' + fmtTime(m.T) + ')');
      } else ro.set('geo', 'only defined for the Earth');
      note.textContent = 'For this ' + b.name + ' orbit, T²/r³ = 4π²/GM = ' + sci(m.k, 3) + ' s² m⁻³ at every radius, so the point on the graph of T² against r³ always lies on a straight line through the origin. ' +
        'A bigger orbit means a smaller speed and a longer period, but a larger (less negative) total energy. ' +
        (key === 'earth' ? 'Press “Snap to geostationary” and watch the satellite stay above one point of the Equator.' : 'Change the body to compare the periods: the satellite mass never changes v or T.');
      c.redraw();
    }
    showEarth();
    update();
    if (!reduced) setPlaying(true);
  });
})();
