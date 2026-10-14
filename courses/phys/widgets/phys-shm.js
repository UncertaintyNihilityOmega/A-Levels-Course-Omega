/* phys-shm: simple harmonic motion and resonance (phys.oscillations).
   data-mode="shm|resonance" (default shm).
   shm:       data-x0="0.05" amplitude in m (0.01–0.10)   data-f="0.5" frequency in Hz (0.2–2)
              data-m="0.5" mass in kg (0.1–2)             data-damp="none|light|critical|heavy"
              data-start="eq|max" (start at equilibrium, x = x0 sin ωt, or at maximum displacement, x = x0 cos ωt)
   resonance: data-ratio="0.8" driving frequency ÷ natural frequency (0.1–3)   data-b="0.3" damping b/ω0 (0.05–2)
   Model: x'' + 2ζω0 x' + ω0² x = 0 with ζ = 0 / 0.08 / 1 / 3 (none / light / critical / heavy), solved by RK4;
   spring-type energies KE = ½mv², PE = ½mω0²x². Resonance: A/A0 = 1 / √((1 − r²)² + (b̂ r)²) with r = f/f0, b̂ = b/ω0,
   A0 = F0/(mω0²), the amplitude of a very slow drive. Reduced motion: no animation, a time slider instead. */
(function () {
  'use strict';
  W.register('phys-shm', function (el, opts) {
    const TAU = 2 * Math.PI;
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const has = (v) => v !== undefined && v !== null && String(v).trim() !== '';
    const notes = [];
    function read(name, d, lo, hi, what) {
      if (!has(opts[name])) return d;
      const x = parseFloat(opts[name]);
      if (!isFinite(x)) { notes.push('data-' + name + ' "' + opts[name] + '" is not a number, so ' + d + ' is used for the ' + what + '.'); return d; }
      const y = Math.min(hi, Math.max(lo, x));
      if (y !== x) notes.push('data-' + name + ' = ' + opts[name] + ' is outside ' + lo + '–' + hi + ', so ' + y + ' is used for the ' + what + '.');
      return y;
    }
    function nice(v) {
      if (!(v > 0) || !isFinite(v)) return 1;
      const e = Math.pow(10, Math.floor(Math.log10(v))), m = v / e;
      const steps = [1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10];
      for (let i = 0; i < steps.length; i++) if (m <= steps[i] + 1e-9) return steps[i] * e;
      return 10 * e;
    }
    function label(ctx, col, txt, x, y, align, color, size) {
      ctx.font = '600 ' + (size || 12) + 'px ' + col.font;
      ctx.fillStyle = color || col.ink2; ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText(txt, x, y);
    }
    function tabs(items, get, set, aria) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': aria });
      const btns = items.map(([v, text]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); } }, text));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }

    let mode = 'shm';
    if (has(opts.mode)) {
      const m = String(opts.mode).toLowerCase();
      if (m === 'shm' || m === 'resonance') mode = m;
      else notes.push('data-mode "' + opts.mode + '" is not shm or resonance, so the SHM view is shown.');
    }
    const { body } = W.frame(el, mode === 'shm' ? 'Simple harmonic motion' : 'Forced oscillations and resonance',
      mode === 'shm' ? 'Watch x, v and a, and the energy of a mass on a spring' : 'Sweep the driving frequency through the natural frequency');
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    const reduced = W.reducedMotion();

    if (mode === 'shm') buildShm(); else buildResonance();
    if (notes.length) { err.textContent = notes.join(' '); err.style.display = ''; }
    body.append(err);

    /* ============================ SHM ============================ */
    function buildShm() {
      const ZETA = { none: 0, light: 0.08, critical: 1, heavy: 3 };
      const st = { x0: 0.05, f: 0.5, m: 0.5, damp: 'none', start: 'eq', t: 0, playing: false };
      st.x0 = read('x0', st.x0, 0.01, 0.1, 'amplitude');
      st.f = read('f', st.f, 0.2, 2, 'frequency');
      st.m = read('m', st.m, 0.1, 2, 'mass');
      if (has(opts.damp)) {
        const d = String(opts.damp).toLowerCase();
        if (ZETA[d] !== undefined) st.damp = d; else notes.push('data-damp "' + opts.damp + '" is not none, light, critical or heavy, so no damping is used.');
      }
      if (has(opts.start)) {
        const s = String(opts.start).toLowerCase();
        if (s === 'eq' || s === 'max') st.start = s; else notes.push('data-start "' + opts.start + '" is not eq or max, so the motion starts at equilibrium.');
      }

      // ---- the model ----
      const N = 800;
      let sim = null;
      function simulate() {
        const w0 = TAU * st.f, z = ZETA[st.damp], T = 1 / st.f, Tw = 4 * T, dt = Tw / N;
        const x = new Float64Array(N + 1), v = new Float64Array(N + 1), a = new Float64Array(N + 1);
        let xx = st.start === 'max' ? st.x0 : 0, vv = st.start === 'max' ? 0 : w0 * st.x0;
        const acc = (p, q) => -w0 * w0 * p - 2 * z * w0 * q;
        for (let i = 0; i <= N; i++) {
          x[i] = xx; v[i] = vv; a[i] = acc(xx, vv);
          const k1x = vv, k1v = acc(xx, vv);
          const k2x = vv + 0.5 * dt * k1v, k2v = acc(xx + 0.5 * dt * k1x, vv + 0.5 * dt * k1v);
          const k3x = vv + 0.5 * dt * k2v, k3v = acc(xx + 0.5 * dt * k2x, vv + 0.5 * dt * k2v);
          const k4x = vv + dt * k3v, k4v = acc(xx + dt * k3x, vv + dt * k3v);
          xx += dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6;
          vv += dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6;
        }
        const peak = (arr) => { let m = 0; for (let i = 0; i <= N; i++) m = Math.max(m, Math.abs(arr[i])); return m; };
        // envelope of light damping: x = e^(−ζω0 t)(c1 cos ωd t + c2 sin ωd t)
        let env = 0;
        if (z > 0 && z < 1) {
          const wd = w0 * Math.sqrt(1 - z * z);
          const c1 = st.start === 'max' ? st.x0 : 0;
          const c2 = ((st.start === 'max' ? 0 : w0 * st.x0) + z * w0 * c1) / wd;
          env = Math.sqrt(c1 * c1 + c2 * c2);
        }
        sim = { w0, z, T, Tw, dt, x, v, a, env, xm: peak(x), vm: peak(v), am: peak(a), E0: 0.5 * st.m * w0 * w0 * st.x0 * st.x0 };
      }
      const at = (arr, t) => {
        const u = Math.max(0, Math.min(N, t / sim.dt)), i = Math.min(N - 1, Math.floor(u)), f = u - i;
        return arr[i] * (1 - f) + arr[i + 1] * f;
      };
      const now = () => {
        const x = at(sim.x, st.t), v = at(sim.v, st.t), a = at(sim.a, st.t);
        return { x, v, a, ke: 0.5 * st.m * v * v, pe: 0.5 * st.m * sim.w0 * sim.w0 * x * x };
      };

      simulate();

      // ---- controls ----
      const dampTabs = tabs([['none', 'No damping'], ['light', 'Light'], ['critical', 'Critical'], ['heavy', 'Heavy']],
        () => st.damp, (v) => { st.damp = v; changed(); }, 'Damping');
      const startTabs = tabs([['eq', 'Start at equilibrium'], ['max', 'Start at maximum']],
        () => st.start, (v) => { st.start = v; changed(); }, 'Starting point');
      const sX = W.sliderNum({ label: 'Amplitude x₀ / m', min: 0.01, max: 0.1, step: 0.005, value: st.x0, oninput: (v) => { st.x0 = num(v, st.x0, 0.01, 0.1); changed(); } });
      const sF = W.sliderNum({ label: 'Frequency f / Hz', min: 0.2, max: 2, step: 0.05, value: st.f, oninput: (v) => { st.f = num(v, st.f, 0.2, 2); changed(); } });
      const sM = W.sliderNum({ label: 'Mass m / kg', min: 0.1, max: 2, step: 0.05, value: st.m, oninput: (v) => { st.m = num(v, st.m, 0.1, 2); changed(); } });
      const sT = W.slider({ label: 'Time', min: 0, max: 1, step: 0.0025, value: 0, fmt: (u) => W.fmt(u * (sim ? sim.Tw : 1), 3) + ' s',
        oninput: (u) => { setPlaying(false); st.t = num(u, 0, 0, 1) * sim.Tw; update(); } });
      let last = 0;
      const anim = W.animate(() => {
        const nowMs = performance.now(), dt = Math.min(0.1, (nowMs - last) / 1000);
        last = nowMs; st.t += dt;
        if (st.t >= sim.Tw) st.t -= sim.Tw;
        sT.set(st.t / sim.Tw); update(); return true;
      }, { still: () => {} });
      function setPlaying(on) {
        if (on && !st.playing) { last = performance.now(); anim.start(); }
        if (!on && st.playing) anim.stop();
        st.playing = on;
        playBtn.textContent = on ? 'Pause' : 'Play';
      }
      const playBtn = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => setPlaying(!st.playing) }, 'Pause');
      const restartBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { st.t = 0; sT.set(0); update(); } }, 'Restart');
      if (reduced) { playBtn.style.display = 'none'; restartBtn.style.display = 'none'; }

      body.append(
        W.h('div', { class: 'w-row' }, dampTabs, startTabs),
        W.h('div', { class: 'w-row' }, sX.el, sF.el, sM.el),
        W.h('div', { class: 'w-row' }, playBtn, restartBtn, sT.el)
      );

      // ---- the spring, the mass and the energy bars ----
      const H1 = 120, H2 = 110, H3 = 130, HT = H1 + H2 + H3;
      const left = W.h('div', { style: { flex: '0 0 120px', width: '120px' } });
      const right = W.h('div', { style: { flex: '1 1 0', minWidth: '0' } });
      const row = W.h('div', { style: { display: 'flex', gap: '8px', alignItems: 'flex-start', margin: '8px 0' } }, left, right);
      body.append(row);
      const cs = W.canvas(left, { height: HT, draw: drawSpring });
      function graph(arrKey, name, colorKey, h, showX, unit) {
        return W.canvas(right, {
          height: h,
          draw(ctx, w, hh, col) {
            const arr = sim[arrKey], amax = nice(Math.max(sim[arrKey === 'x' ? 'xm' : arrKey === 'v' ? 'vm' : 'am'], 1e-12) * 1.12);
            const color = col[colorKey];
            const axo = { pad: { l: 50, r: 8, t: 16, b: showX ? 32 : 6 }, xlabel: showX ? 't / s' : '', ylabel: name + ' / ' + unit, nx: 4, ny: W.ticks(-amax, amax, 3).length >= 3 ? 3 : 4 };   // always label ±a value, not just 0
            if (!showX) axo.fx = () => '';
            const ax = W.axes(ctx, w, hh, { x0: 0, x1: sim.Tw, y0: -amax, y1: amax }, col, axo);
            const { X, Y } = ax;
            ctx.save();
            ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t - 2, w - ax.pad.l - ax.pad.r, hh - ax.pad.t - ax.pad.b + 4); ctx.clip();
            const trace = (to, alpha, lw) => {
              ctx.globalAlpha = alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath();
              const n = Math.max(1, Math.round(to / sim.dt));
              for (let i = 0; i <= n; i++) { const t = Math.min(to, i * sim.dt), y = Y(arr[Math.min(N, i)]); if (i === 0) ctx.moveTo(X(t), y); else ctx.lineTo(X(t), y); }
              ctx.stroke(); ctx.globalAlpha = 1;
            };
            trace(sim.Tw, 0.2, 2);
            if (arrKey === 'x' && sim.env > 0) {                       // envelope of the light damping
              ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 3]);
              [1, -1].forEach((sg) => {
                ctx.beginPath();
                for (let i = 0; i <= 120; i++) { const t = sim.Tw * i / 120, y = Y(sg * sim.env * Math.exp(-sim.z * sim.w0 * t)); if (i === 0) ctx.moveTo(X(t), y); else ctx.lineTo(X(t), y); }
                ctx.stroke();
              });
              ctx.setLineDash([]);
            }
            trace(Math.min(st.t, sim.Tw), 1, 2.6);
            ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
            ctx.beginPath(); ctx.moveTo(X(st.t), ax.pad.t - 2); ctx.lineTo(X(st.t), hh - ax.pad.b); ctx.stroke(); ctx.setLineDash([]);
            ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(st.t), Y(at(arr, st.t)), 4.5, 0, TAU); ctx.fill();
            ctx.restore();
          }
        });
      }
      const gX = graph('x', 'x', 'sc', H1, false, 'm');
      const gV = graph('v', 'v', 'sc2', H2, false, 'm s⁻¹');
      const gA = graph('a', 'a', 'ok', H3, true, 'm s⁻²');
      function drawSpring(ctx, w, h, col) {
        const n = now(), cx = 40, yTop = 14, yEq = Math.round(h / 2), scale = 650, mw = 36, mh = 26;
        const ym = yEq - n.x * scale;
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 3; ctx.lineCap = 'round';
        ctx.beginPath(); ctx.moveTo(cx - 20, yTop); ctx.lineTo(cx + 20, yTop); ctx.stroke();
        ctx.lineWidth = 1.2;
        for (let i = -16; i <= 16; i += 8) { ctx.beginPath(); ctx.moveTo(cx + i, yTop - 2); ctx.lineTo(cx + i - 5, yTop - 8); ctx.stroke(); }
        ctx.setLineDash([4, 4]); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(2, yEq); ctx.lineTo(60, yEq); ctx.stroke(); ctx.setLineDash([]);
        label(ctx, col, 'x = 0', 2, yEq - 5, 'left', col.ink2, 11);
        const y0 = yTop, y1 = ym - mh / 2, nC = 10;
        ctx.strokeStyle = col.ink; ctx.lineWidth = 1.8; ctx.lineJoin = 'round'; ctx.beginPath(); ctx.moveTo(cx, y0);
        for (let i = 0; i < nC; i++) ctx.lineTo(cx + (i % 2 ? 11 : -11), y0 + 5 + (y1 - y0 - 10) * (i + 0.5) / nC);
        ctx.lineTo(cx, y1 - 5); ctx.lineTo(cx, y1); ctx.stroke();
        ctx.globalAlpha = 0.25; ctx.fillStyle = col.sc; ctx.fillRect(cx - mw / 2, ym - mh / 2, mw, mh); ctx.globalAlpha = 1;
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2; ctx.strokeRect(cx - mw / 2, ym - mh / 2, mw, mh);
        // energy bars: full height = the energy at t = 0 with no damping
        const yb = h - 24, yt = 24, hh = yb - yt, E = Math.max(sim.E0, 1e-30);
        const bars = [[68, n.ke, col.sc2, 'KE', true], [86, n.pe, col.sc, 'PE', true], [104, n.ke + n.pe, col.ink2, 'E', false]];
        bars.forEach(([bx, val, color, nm, fill]) => {
          const bh = Math.max(0, Math.min(1.05, val / E)) * hh;
          if (fill) { ctx.fillStyle = color; ctx.fillRect(bx, yb - bh, 12, bh); }
          else { ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.strokeRect(bx + 1, yb - bh, 10, bh); }
          label(ctx, col, nm, bx + 6, h - 8, 'center', col.ink2, 12);
        });
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(64, yt); ctx.lineTo(118, yt); ctx.stroke(); ctx.setLineDash([]);
        ctx.strokeStyle = col.ink2; ctx.beginPath(); ctx.moveTo(64, yb); ctx.lineTo(118, yb); ctx.stroke();
        label(ctx, col, 'energy', 91, yt - 6, 'center', col.ink2, 11);
      }

      const ro = W.readout([
        ['w', 'Angular frequency ω = 2πf'], ['T', 'Period T = 1/f'], ['k', 'Force constant k = mω²'],
        ['vm', 'Maximum speed v₀ = ωx₀ (undamped)'], ['am', 'Maximum acceleration ω²x₀ (undamped)'], ['E', 'Energy ½mω²x₀² (undamped)'],
        ['xva', 'Now: x, v, a'], ['en', 'Now: KE, PE, total']
      ]);
      const note = W.h('div', { class: 'w-note' });
      body.append(ro.el, note);

      const sci = (x, sf) => {
        const ax = Math.abs(x);
        if (ax < 1e-9) return '0';
        if (ax >= 0.01 && ax < 1000) return W.fmt(x, sf);
        const e = Math.floor(Math.log10(ax)), m = x / Math.pow(10, e);
        const sup = String(e).split('').map((ch) => ({ '-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' }[ch] || ch)).join('');
        return m.toFixed(sf - 1) + ' × 10' + sup;
      };
      function statics() {
        ro.set('w', W.fmt(sim.w0, 3) + ' rad s⁻¹');
        ro.set('T', W.fmt(sim.T, 3) + ' s');
        ro.set('k', W.fmt(st.m * sim.w0 * sim.w0, 3) + ' N m⁻¹');
        ro.set('vm', W.fmt(sim.w0 * st.x0, 3) + ' m s⁻¹');
        ro.set('am', W.fmt(sim.w0 * sim.w0 * st.x0, 3) + ' m s⁻²');
        ro.set('E', sci(sim.E0, 3) + ' J');
        const z = st.damp;
        note.textContent = z === 'none'
          ? 'No damping: the amplitude stays at x₀ = ' + st.x0 + ' m. v leads x by a quarter of a period, a is the mirror image of x (a = −ω²x), KE and PE swap but the total never changes. Changing the mass changes the energy, not the graphs.'
          : z === 'light'
            ? 'Light damping: the amplitude shrinks roughly exponentially (dashed envelope) while the period hardly changes, and the total energy falls steadily.'
            : z === 'critical'
              ? 'Critical damping: the mass returns to x = 0 in the shortest time and does not oscillate.'
              : 'Heavy damping: no oscillation, and the return to x = 0 is slower than for critical damping.';
      }
      function dynamics() {
        const n = now();
        ro.set('xva', sci(n.x, 3) + ' m, ' + sci(n.v, 3) + ' m s⁻¹, ' + sci(n.a, 3) + ' m s⁻²');
        ro.set('en', sci(n.ke, 3) + ' J, ' + sci(n.pe, 3) + ' J, ' + sci(n.ke + n.pe, 3) + ' J');
      }
      function update() { dynamics(); cs.redraw(); gX.redraw(); gV.redraw(); gA.redraw(); }
      function changed() {
        const frac = sim ? st.t / sim.Tw : 0;
        simulate();
        st.t = Math.min(frac, 1) * sim.Tw;
        sT.set(frac);
        statics(); update();
      }
      if (reduced) st.t = sim.Tw / 8;
      sT.set(st.t / sim.Tw);
      statics(); update();
      if (!reduced) setPlaying(true);
    }

    /* ========================== Resonance ========================== */
    function buildResonance() {
      const REFS = [0.1, 0.3, 0.8];
      const F0 = 1;                                     // natural frequency of the animated oscillator, Hz
      const st = { r: 0.8, b: 0.3, t: 0, playing: false };
      st.r = read('ratio', st.r, 0.1, 3, 'frequency ratio');
      st.b = read('b', st.b, 0.05, 2, 'damping');
      const amp = (r, b) => 1 / Math.sqrt(Math.pow(1 - r * r, 2) + b * b * r * r);
      const phase = (r, b) => Math.atan2(b * r, 1 - r * r);               // lag of the mass behind the driver, 0 to π
      const peakOf = (b) => { const r = b * b < 2 ? Math.sqrt(1 - b * b / 2) : 0; return { a: amp(r, b), r }; };   // exact peak of amp(r, b)
      const ymaxNow = () => nice(1.12 * Math.max(peakOf(REFS[0]).a, peakOf(st.b).a));
      const word = (b) => (b < 0.15 ? 'light' : b < 0.5 ? 'moderate' : b < 1.2 ? 'heavy' : 'very heavy');

      const sR = W.sliderNum({ label: 'Driving frequency ÷ natural frequency', min: 0.1, max: 3, step: 0.01, value: st.r, oninput: (v) => { st.r = num(v, st.r, 0.1, 3); update(); } });
      const sB = W.slider({ label: 'Damping b / ω₀', min: 0.05, max: 2, step: 0.01, value: st.b,
        fmt: (v) => W.fmt(v, 2) + ' (' + word(v) + ')', oninput: (v) => { st.b = num(v, st.b, 0.05, 2); update(); } });
      let last = 0;
      const anim = W.animate(() => {
        const nowMs = performance.now(), dt = Math.min(0.1, (nowMs - last) / 1000);
        last = nowMs; st.t += dt; cAn.redraw(); return true;
      }, { still: () => {} });
      function setPlaying(on) {
        if (on && !st.playing) { last = performance.now(); anim.start(); }
        if (!on && st.playing) anim.stop();
        st.playing = on;
        playBtn.textContent = on ? 'Pause' : 'Play';
      }
      const playBtn = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => setPlaying(!st.playing) }, 'Pause');
      const resBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { st.r = 1; sR.set(1); update(); } }, 'Go to f = f₀');
      if (reduced) playBtn.style.display = 'none';
      body.append(W.h('div', { class: 'w-row' }, sR.el, sB.el), W.h('div', { class: 'w-row' }, playBtn, resBtn));

      const wrapL = W.h('div', { style: { flex: '1 1 260px', minWidth: '0' } });
      const wrapR = W.h('div', { style: { flex: '0 0 130px', width: '130px' } });
      body.append(W.h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '8px', alignItems: 'flex-start', margin: '8px 0' } }, wrapL, wrapR));

      const cCurve = W.canvas(wrapL, {
        height: 260,
        draw(ctx, w, h, col) {
          const ym = ymaxNow();
          const ax = W.axes(ctx, w, h, { x0: 0, x1: 3, y0: 0, y1: ym }, col, {
            pad: { l: 44, r: 12, t: 20, b: 38 }, xlabel: 'f / f₀', ylabel: 'A / A₀', nx: 6
          });
          const { X, Y } = ax;
          ctx.save();
          ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
          const curve = (b, color, lw, alpha) => {
            ctx.globalAlpha = alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath();
            for (let i = 0; i <= 300; i++) { const r = 3 * i / 300, y = Y(amp(r, b)); if (i === 0) ctx.moveTo(X(r), y); else ctx.lineTo(X(r), y); }
            ctx.stroke(); ctx.globalAlpha = 1;
          };
          REFS.forEach((b) => curve(b, col.ink2, 1.6, 0.4));
          curve(st.b, col.sc, 3, 1);
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
          ctx.beginPath(); ctx.moveTo(X(1), Y(0)); ctx.lineTo(X(1), ax.pad.t); ctx.stroke();
          const a = amp(st.r, st.b);
          ctx.beginPath(); ctx.moveTo(X(0), Y(a)); ctx.lineTo(X(st.r), Y(a)); ctx.lineTo(X(st.r), Y(0)); ctx.stroke(); ctx.setLineDash([]);
          ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(st.r), Y(a), 5.5, 0, TAU); ctx.fill();
          ctx.restore();
          label(ctx, col, 'bold: your damping', w - ax.pad.r - 4, ax.pad.t + 14, 'right', col.sc, 12);
          label(ctx, col, 'faint: 0.1, 0.3, 0.8', w - ax.pad.r - 4, ax.pad.t + 30, 'right', col.ink2, 12);
        }
      });
      const cAn = W.canvas(wrapR, {
        height: 260,
        draw(ctx, w, h, col) {
          const a = amp(st.r, st.b), d = phase(st.r, st.b), ym = ymaxNow();
          const wt = TAU * st.r * F0 * st.t;
          const cx = 62, yEq = 150, yd = 40, amplPx = Math.min(60, 60 * a / ym);
          const drv = yd - 5 * Math.cos(wt);
          const ymass = yEq - amplPx * Math.cos(wt - d);
          ctx.strokeStyle = col.ink2; ctx.lineWidth = 4; ctx.lineCap = 'round';
          ctx.beginPath(); ctx.moveTo(cx - 24, drv); ctx.lineTo(cx + 24, drv); ctx.stroke();
          ctx.setLineDash([4, 4]); ctx.strokeStyle = col.ink3; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(4, yEq); ctx.lineTo(w - 4, yEq); ctx.stroke(); ctx.setLineDash([]);
          const y0 = drv + 2, y1 = ymass - 13, nC = 10;
          ctx.strokeStyle = col.ink; ctx.lineWidth = 1.8; ctx.lineJoin = 'round'; ctx.beginPath(); ctx.moveTo(cx, y0);
          for (let i = 0; i < nC; i++) ctx.lineTo(cx + (i % 2 ? 11 : -11), y0 + 5 + (y1 - y0 - 10) * (i + 0.5) / nC);
          ctx.lineTo(cx, y1 - 5); ctx.lineTo(cx, y1); ctx.stroke();
          ctx.globalAlpha = 0.25; ctx.fillStyle = col.sc; ctx.fillRect(cx - 18, ymass - 13, 36, 26); ctx.globalAlpha = 1;
          ctx.strokeStyle = col.sc; ctx.lineWidth = 2; ctx.strokeRect(cx - 18, ymass - 13, 36, 26);
          label(ctx, col, 'driver', cx, yd - 22, 'center', col.ink2, 12);
          label(ctx, col, 'f = ' + W.fmt(st.r * F0, 2) + ' f₀', cx, h - 28, 'center', col.ink2, 12);
          label(ctx, col, 'A = ' + W.fmt(a, 3) + ' A₀', cx, h - 12, 'center', col.sc, 12);
        }
      });
      const ro = W.readout([
        ['r', 'Driving frequency ÷ natural frequency'], ['a', 'Amplitude A / A₀ at this frequency'], ['d', 'Phase lag of the mass behind the driver'],
        ['pk', 'Peak of this curve'], ['pos', 'Frequency of the peak']
      ]);
      const note = W.h('div', { class: 'w-note' });
      body.append(ro.el, note);
      function update() {
        const a = amp(st.r, st.b), pk = peakOf(st.b);
        ro.set('r', W.fmt(st.r, 3));
        ro.set('a', W.fmt(a, 3));
        ro.set('d', W.fmt(phase(st.r, st.b), 3) + ' rad = ' + W.fmt(phase(st.r, st.b) * 180 / Math.PI, 3) + '°');
        ro.set('pk', W.fmt(pk.a, 3) + ' A₀');
        ro.set('pos', pk.r < 0.02 ? 'no peak (heavily damped)' : W.fmt(pk.r, 3) + ' f₀');
        note.textContent = 'A₀ is the amplitude for a very slow drive. With ' + word(st.b) + ' damping the curve peaks at ' + W.fmt(pk.a, 2) +
          ' A₀, ' + (pk.r > 0.98 ? 'almost exactly at' : 'a little below') + ' the natural frequency. More damping lowers and broadens the peak and moves it to a lower frequency; ' +
          'the faint curves show b/ω₀ = 0.1, 0.3 and 0.8. Far above f₀ the mass hardly moves, and well below f₀ it follows the driver.';
        cCurve.redraw(); cAn.redraw();
      }
      update();
      if (!reduced) setPlaying(true);
    }
  });
})();
