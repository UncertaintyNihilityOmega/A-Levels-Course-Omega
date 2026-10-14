/* phys-collide: a one-dimensional collision lab (phys.dynamics).
   data-m1, data-m2 (kg, 0.1–10)  data-u1, data-u2 (m/s, -10–10, positive = to the right)
   data-type="elastic|stick|explode" (default elastic)
   Elastic: v1 = ((m1-m2)u1 + 2 m2 u2)/(m1+m2), v2 = ((m2-m1)u2 + 2 m1 u1)/(m1+m2).
   Stick: v = (m1 u1 + m2 u2)/(m1+m2).  Explosion (both at rest, energy E released): equal and opposite momenta. */
(function () {
  'use strict';
  W.register('phys-collide', function (el, opts) {
    const { body } = W.frame(el, 'Collision lab', 'Set the masses and speeds, then press Play');
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const TYPES = ['elastic', 'stick', 'explode'];
    const st = {
      type: TYPES.indexOf(opts.type) >= 0 ? opts.type : 'elastic',
      m1: num(opts.m1, 2, 0.1, 10),
      m2: num(opts.m2, 1, 0.1, 10),
      u1: num(opts.u1, 3, -10, 10),
      u2: num(opts.u2, 0, -10, 10),
      E: 20
    };
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    const bad = ['m1', 'm2', 'u1', 'u2'].some((k) => opts[k] !== undefined && opts[k] !== '' && !isFinite(parseFloat(opts[k])));
    const badType = opts.type !== undefined && opts.type !== '' && TYPES.indexOf(opts.type) < 0;
    if (bad || badType) {
      err.textContent = 'Some starting values were not valid, so defaults are used.';
      err.style.display = '';
    }

    const clean = (x) => (Math.abs(x) < 1e-9 ? 0 : x);
    const WIN = 7;                                   // world window is -WIN..WIN metres
    const width = (m) => 0.7 + 0.12 * m;             // trolley width in world units

    // ---- physics -----------------------------------------------------------
    function model(s) {
      const w1 = width(s.m1), w2 = width(s.m2);
      const r = { w1, w2, collides: false, tc: 0 };
      if (s.type === 'explode') {
        r.u1 = 0; r.u2 = 0;
        r.v1 = -Math.sqrt(2 * s.E * s.m2 / (s.m1 * (s.m1 + s.m2)));
        r.v2 = Math.sqrt(2 * s.E * s.m1 / (s.m2 * (s.m1 + s.m2)));
        r.x1 = -w1 / 2; r.x2 = w2 / 2;
        r.collides = true; r.tc = 0;
        return r;
      }
      r.u1 = s.u1; r.u2 = s.u2;
      const gap = 4;                                  // clear space between the trolleys at the start
      r.x1 = -5; r.x2 = r.x1 + (w1 + w2) / 2 + gap;
      if (s.u1 > s.u2) {
        r.collides = true;
        r.tc = gap / (s.u1 - s.u2);
        if (s.type === 'stick') {
          r.v1 = r.v2 = (s.m1 * s.u1 + s.m2 * s.u2) / (s.m1 + s.m2);
        } else {
          r.v1 = ((s.m1 - s.m2) * s.u1 + 2 * s.m2 * s.u2) / (s.m1 + s.m2);
          r.v2 = ((s.m2 - s.m1) * s.u2 + 2 * s.m1 * s.u1) / (s.m1 + s.m2);
        }
      } else {
        r.v1 = s.u1; r.v2 = s.u2;                     // never meet
      }
      return r;
    }
    // positions and velocities at simulated time t
    function at(r, t) {
      if (!r.collides || t < r.tc) return { x1: r.x1 + r.u1 * t, x2: r.x2 + r.u2 * t, v1: r.u1, v2: r.u2 };
      const xc1 = r.x1 + r.u1 * r.tc, xc2 = r.x2 + r.u2 * r.tc, d = t - r.tc;
      return { x1: xc1 + r.v1 * d, x2: xc2 + r.v2 * d, v1: r.v1, v2: r.v2 };
    }
    // total simulated time so the animation stays on the track
    function span(r) {
      const away = (x, v, lim) => (Math.abs(v) < 1e-6 ? Infinity : Math.max(0, ((v > 0 ? lim : -lim) - x) / v));
      let after;
      if (r.collides) {
        const c = at(r, r.tc);
        after = Math.min(away(c.x1, r.v1, WIN - 0.8), away(c.x2, r.v2, WIN - 0.8));
        after = Math.min(after, Math.max(r.tc, 1.2), 4);
        if (!isFinite(after)) after = 1;
        if (r.tc === 0) after = Math.min(after, 3);
        return r.tc + after;
      }
      after = Math.min(away(r.x1, r.u1, WIN - 0.8), away(r.x2, r.u2, WIN - 0.8), 4);
      return isFinite(after) ? after : 2;
    }

    // ---- controls ----------------------------------------------------------
    let R = model(st), T = span(R);
    let prog = 0;                                     // 0..1 through the animation
    const DUR = 4;                                    // real seconds for a full run

    function tabs(items, get, set) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Type of interaction' });
      const btns = items.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); } }, label));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    const typeTabs = tabs([['elastic', 'Elastic'], ['stick', 'Stick together'], ['explode', 'Explosion']],
      () => st.type, (v) => { st.type = v; showCtl(); changed(); });

    const sM1 = W.sliderNum({ label: 'Mass m1 / kg', min: 0.1, max: 10, step: 0.1, value: st.m1, oninput: (v) => { st.m1 = num(v, 2, 0.1, 10); changed(); } });
    const sM2 = W.sliderNum({ label: 'Mass m2 / kg', min: 0.1, max: 10, step: 0.1, value: st.m2, oninput: (v) => { st.m2 = num(v, 1, 0.1, 10); changed(); } });
    const sU1 = W.sliderNum({ label: 'Velocity u1 / m s⁻¹', min: -10, max: 10, step: 0.1, value: st.u1, oninput: (v) => { st.u1 = num(v, 3, -10, 10); changed(); } });
    const sU2 = W.sliderNum({ label: 'Velocity u2 / m s⁻¹', min: -10, max: 10, step: 0.1, value: st.u2, oninput: (v) => { st.u2 = num(v, 0, -10, 10); changed(); } });
    const sE = W.sliderNum({ label: 'Energy released E / J', min: 0, max: 50, step: 1, value: st.E, oninput: (v) => { st.E = num(v, 20, 0, 50); changed(); } });
    function showCtl() {
      const ex = st.type === 'explode';
      sU1.el.style.display = ex ? 'none' : '';
      sU2.el.style.display = ex ? 'none' : '';
      sE.el.style.display = ex ? '' : 'none';
    }
    showCtl();

    const playBtn = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => play() }, 'Play');
    const resetBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { anim.stop(); prog = 0; c.redraw(); } }, 'Reset');

    body.append(
      W.h('div', { class: 'w-row' }, typeTabs),
      W.h('div', { class: 'w-row' }, sM1.el, sM2.el),
      W.h('div', { class: 'w-row' }, sU1.el, sU2.el, sE.el),
      W.h('div', { class: 'w-row' }, playBtn, resetBtn)
    );

    // ---- drawing -----------------------------------------------------------
    function row(ctx, w, y, p, col, label) {
      const px = (x) => w / 2 + x * (w / (2 * WIN));          // world metres to pixels
      const sc = w / (2 * WIN);
      const th = 30;
      ctx.strokeStyle = col.ink3; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(8, y); ctx.lineTo(w - 8, y); ctx.stroke();
      const items = [
        { x: p.x1, v: p.v1, m: st.m1, wd: R.w1, fill: col.sc, name: '1' },
        { x: p.x2, v: p.v2, m: st.m2, wd: R.w2, fill: col.sc2, name: '2' }
      ];
      items.forEach((it) => {
        const pw = Math.max(26, it.wd * sc), x0 = px(it.x) - pw / 2;
        ctx.fillStyle = it.fill; ctx.globalAlpha = 0.85;
        ctx.fillRect(x0, y - th - 5, pw, th); ctx.globalAlpha = 1;
        ctx.strokeStyle = col.ink; ctx.lineWidth = 1.5; ctx.strokeRect(x0, y - th - 5, pw, th);
        ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(x0 + 6, y - 2, 3, 0, 2 * Math.PI); ctx.arc(x0 + pw - 6, y - 2, 3, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = col.ink; ctx.font = '600 12px ' + col.font; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(W.fmt(it.m, 2) + ' kg', px(it.x), y - th / 2 - 5);
        // velocity arrow above the trolley
        const len = Math.max(-90, Math.min(90, it.v * 9));
        const ay = y - th - 22, ax = px(it.x);
        if (Math.abs(it.v) > 0.04) {
          ctx.strokeStyle = it.fill; ctx.fillStyle = it.fill; ctx.lineWidth = 2.5;
          const dir = len > 0 ? 1 : -1, tip = ax + len;
          ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(tip, ay); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(tip, ay); ctx.lineTo(tip - dir * 8, ay - 5); ctx.lineTo(tip - dir * 8, ay + 5); ctx.closePath(); ctx.fill();
        }
        ctx.fillStyle = col.ink2; ctx.font = '12px ' + col.font; ctx.textAlign = 'center';
        ctx.fillText('v' + it.name + ' = ' + W.fmt(clean(it.v), 3) + ' m s⁻¹', ax, ay - 12);
      });
      if (label) {
        ctx.fillStyle = col.ink2; ctx.font = '600 11px ' + col.font; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
        ctx.fillText(label, 10, y + 18);
      }
    }
    const c = W.canvas(body, {
      height: 200,
      draw(ctx, w, h, col) {
        ctx.textBaseline = 'alphabetic';
        if (W.reducedMotion()) {
          row(ctx, w, 88, at(R, 0), col, 'before');
          row(ctx, w, 180, at(R, T), col, 'after');
          return;
        }
        row(ctx, w, 140, at(R, prog * T), col, '');
      }
    });

    const ro = W.readout([
      ['p0', 'Total momentum before'], ['p1', 'Total momentum after'],
      ['k0', 'Total kinetic energy before'], ['k1', 'Total kinetic energy after'],
      ['dk', 'Change of kinetic energy'],
      ['ap', 'Relative speed of approach'], ['sp', 'Relative speed of separation']
    ]);
    const msg = W.h('div', { class: 'w-note' });
    const note = W.h('div', { class: 'w-note' }, 'Momentum is always the same before and after. Kinetic energy is only conserved in the elastic case: then the relative speeds match too.');
    body.append(ro.el, msg, note, err);

    function readouts() {
      const b1 = R.u1, b2 = R.u2;
      const p0 = st.m1 * b1 + st.m2 * b2, p1 = st.m1 * R.v1 + st.m2 * R.v2;
      const k0 = 0.5 * st.m1 * b1 * b1 + 0.5 * st.m2 * b2 * b2;
      const k1 = 0.5 * st.m1 * R.v1 * R.v1 + 0.5 * st.m2 * R.v2 * R.v2;
      const dk = k1 - k0;
      ro.set('p0', W.fmt(clean(p0), 3) + ' kg m s⁻¹');
      ro.set('p1', W.fmt(clean(p1), 3) + ' kg m s⁻¹');
      ro.set('k0', W.fmt(clean(k0), 3) + ' J');
      ro.set('k1', W.fmt(clean(k1), 3) + ' J');
      if (st.type === 'explode') {
        ro.set('dk', '+' + W.fmt(clean(dk), 3) + ' J (energy released)');
        ro.set('ap', '0 m s⁻¹');
        ro.set('sp', W.fmt(clean(R.v2 - R.v1), 3) + ' m s⁻¹');
        msg.textContent = 'Both trolleys start at rest, so the total momentum is zero: they leave with equal and opposite momenta. The lighter trolley gets the greater speed and most of the kinetic energy.';
      } else if (!R.collides) {
        ro.set('dk', '0 J (no collision)');
        ro.set('ap', W.fmt(clean(st.u1 - st.u2), 3) + ' m s⁻¹');
        ro.set('sp', 'no collision');
        msg.textContent = 'Trolley 1 never catches trolley 2 (u1 is not greater than u2), so they do not collide. Give trolley 1 a greater velocity than trolley 2.';
      } else {
        const pc = k0 > 1e-9 ? ' (' + W.fmt(100 * dk / k0, 3) + '%)' : '';
        ro.set('dk', W.fmt(clean(dk), 3) + ' J' + pc);
        ro.set('ap', W.fmt(clean(st.u1 - st.u2), 3) + ' m s⁻¹');
        ro.set('sp', W.fmt(clean(R.v2 - R.v1), 3) + ' m s⁻¹');
        msg.textContent = st.type === 'stick'
          ? 'The trolleys stick together and move with one velocity, so the speed of separation is zero. This loses the most kinetic energy.'
          : 'Elastic: the kinetic energy is unchanged and the relative speed of separation equals the relative speed of approach.';
      }
    }

    function changed() {
      anim.stop(); R = model(st); T = span(R); prog = 0;
      readouts(); c.redraw();
    }

    // ---- animation ---------------------------------------------------------
    let t0 = 0;
    const anim = W.animate(() => {
      prog = Math.min(1, (performance.now() - t0) / (DUR * 1000));
      c.redraw();
      return prog < 1;
    }, { still: () => { prog = 1; c.redraw(); } });
    function play() {
      anim.stop();
      prog = 0; t0 = performance.now();
      if (W.reducedMotion()) { prog = 1; c.redraw(); return; }
      anim.start();
    }

    readouts();
  });
})();
