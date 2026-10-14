/* phys-gas: molecules in a box with a movable wall (phys.gases).
   data-n="60"   number of drawn particles, 10–200 (each stands for 1e20 molecules)
   data-t="300"  temperature in K, 50–1000
   data-gas="n2" he | n2 | o2
   Model: 2D box 10 cm high, 10 cm deep, width 5–20 cm (the volume). Elastic walls, no particle–particle collisions.
   The r.m.s. speed drawn is the real sqrt(3kT/m) slowed by a fixed factor (1 cm/s on screen = 50 m/s), so it scales as sqrt(T).
   Readouts use pV = NkT, c_rms = sqrt(3kT/m), mean KE = 3kT/2 with m = M/N_A. */
(function () {
  'use strict';
  const NA = 6.02e23, KB = 1.38e-23;
  const GASES = {
    he: { sym: 'He', name: 'Helium', M: 0.004 },
    n2: { sym: 'N₂', name: 'Nitrogen', M: 0.028 },
    o2: { sym: 'O₂', name: 'Oxygen', M: 0.032 }
  };
  const SCALE = 50;          // m/s of real speed per cm/s drawn
  const PER = 1e20;          // molecules each drawn particle stands for
  const HEIGHT = 10;         // cm, box height (and depth)
  const RAD = 0.25;          // cm, drawn radius of a particle
  const NB = 14;             // histogram bins
  const XMAXES = [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000];
  const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  const sup = (e) => String(e).split('').map((ch) => SUP[ch] || ch).join('');
  function sci(x, sf) {
    if (!isFinite(x) || x === 0) return '0';
    let e = Math.floor(Math.log10(Math.abs(x)));
    let m = x / Math.pow(10, e);
    if (parseFloat(m.toPrecision(sf)) >= 10) { m /= 10; e += 1; }
    return m.toPrecision(sf) + ' × 10' + sup(e);
  }

  W.register('phys-gas', function (el, opts) {
    const { body } = W.frame(el, 'Molecules in a box', 'Change the temperature, the volume, the number of molecules and the gas');
    const msgs = [];
    function num(raw, d, lo, hi, name, unit) {
      if (raw === undefined || raw === null || String(raw).trim() === '') return d;
      const x = parseFloat(raw);
      if (!isFinite(x)) { msgs.push(name + ' = "' + raw + '" is not a number, so ' + d + unit + ' is used.'); return d; }
      if (x < lo) { msgs.push(name + ' = ' + x + ' is below the range ' + lo + '–' + hi + unit + ', so ' + lo + unit + ' is used.'); return lo; }
      if (x > hi) { msgs.push(name + ' = ' + x + ' is above the range ' + lo + '–' + hi + unit + ', so ' + hi + unit + ' is used.'); return hi; }
      return x;
    }
    const gasKey = String(opts.gas || 'n2').toLowerCase();
    if (opts.gas && !GASES[gasKey]) msgs.push('Gas "' + opts.gas + '" is not known (use he, n2 or o2), so nitrogen is used.');
    const st = {
      gas: GASES[gasKey] ? gasKey : 'n2',
      n: Math.round(num(opts.n, 60, 10, 200, 'Number of particles', '')),
      T: num(opts.t, 300, 50, 1000, 'Temperature', ' K'),
      w: 10                // box width, cm
    };

    // ---- particles (positions in cm, velocities in cm/s drawn) --------------
    const rng = W.rng(11);
    const MAXN = 200;
    const px = [], py = [], vx = [], vy = [];
    for (let i = 0; i < MAXN; i++) {
      px.push(RAD + rng() * (20 - 2 * RAD)); py.push(RAD + rng() * (HEIGHT - 2 * RAD));
      vx.push(rng.normal(0, 1)); vy.push(rng.normal(0, 1));
    }
    for (let i = 0; i < MAXN; i++) px[i] = RAD + (px[i] - RAD) / (20 - 2 * RAD) * (st.w - 2 * RAD);

    const mOf = () => GASES[st.gas].M / NA;
    const cReal = () => Math.sqrt(3 * KB * st.T / mOf());
    function rmsNow() {
      let s = 0;
      for (let i = 0; i < st.n; i++) s += vx[i] * vx[i] + vy[i] * vy[i];
      return Math.sqrt(s / Math.max(1, st.n));
    }
    function retune() {           // rescale every velocity so the drawn r.m.s. speed matches the model
      const cur = rmsNow();
      const f = cur > 1e-9 ? (cReal() / SCALE) / cur : 1;
      for (let i = 0; i < MAXN; i++) { vx[i] *= f; vy[i] *= f; }
    }
    retune();

    // ---- controls ------------------------------------------------------------
    const err = W.h('div', { class: 'w-err', style: { display: msgs.length ? '' : 'none' } });
    err.textContent = msgs.join(' ');

    function tabs(items, get, set) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose the gas' });
      const btns = items.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); } }, label));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    const gasTabs = tabs(Object.keys(GASES).map((k) => [k, GASES[k].name + ' (' + GASES[k].sym + ')']), () => st.gas, (v) => { st.gas = v; retune(); changed(); });
    const sT = W.sliderNum({ label: 'Temperature T / K', min: 50, max: 1000, step: 10, value: st.T, oninput: (v) => {
      const x = parseFloat(v); if (!isFinite(x)) return;
      st.T = Math.min(1000, Math.max(50, x)); retune(); changed();
    } });
    const sN = W.sliderNum({ label: 'Drawn particles', min: 10, max: 200, step: 1, value: st.n, oninput: (v) => {
      const x = parseFloat(v); if (!isFinite(x)) return;
      st.n = Math.round(Math.min(200, Math.max(10, x))); retune(); changed();
    } });
    const sV = W.slider({ label: 'Box width (volume)', min: 5, max: 20, step: 0.5, value: st.w, fmt: (v) => W.fmt(v, 3) + ' cm', oninput: (v) => setWidth(parseFloat(v)) });

    body.append(
      W.h('div', { class: 'w-row' }, gasTabs),
      W.h('div', { class: 'w-row' }, sT.el, sN.el),
      W.h('div', { class: 'w-row' }, sV.el)
    );

    function setWidth(wv) {
      if (!isFinite(wv)) return;
      const nw = Math.min(20, Math.max(5, wv));
      if (nw < st.w) for (let i = 0; i < MAXN; i++) px[i] = RAD + (px[i] - RAD) * (nw - 2 * RAD) / (st.w - 2 * RAD);
      st.w = nw;
      changed();
    }

    // ---- box canvas ------------------------------------------------------------
    const geo = { s: 14, left: 16, top: 25 };
    let flashes = [];
    let dragging = false;
    const reduced = W.reducedMotion();
    const box = W.canvas(body, {
      height: 190,
      draw(ctx, w, h, col) {
        const s = Math.max(6, Math.min(14, (w - 36) / 20));
        const Hb = HEIGHT * s;
        const left = Math.max(14, (w - 20 * s) / 2), top = (h - Hb) / 2 - 4;
        geo.s = s; geo.left = left; geo.top = top;
        const bw = st.w * s;
        ctx.save();
        ctx.setLineDash([4, 4]); ctx.lineWidth = 1; ctx.strokeStyle = col.rule2;
        ctx.strokeRect(left + 0.5, top + 0.5, 20 * s, Hb);
        ctx.setLineDash([]);
        ctx.fillStyle = col.card; ctx.fillRect(left, top, bw, Hb);
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 3; ctx.lineCap = 'square';
        ctx.beginPath(); ctx.moveTo(left + bw, top); ctx.lineTo(left, top); ctx.lineTo(left, top + Hb); ctx.lineTo(left + bw, top + Hb); ctx.stroke();
        // moving wall
        ctx.fillStyle = dragging ? col.sc : col.ink2;
        ctx.fillRect(left + bw, top - 4, 8, Hb + 8);
        ctx.strokeStyle = col.card; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(left + bw + 2.5, top + Hb / 2 - 9); ctx.lineTo(left + bw + 2.5, top + Hb / 2 + 9);
        ctx.moveTo(left + bw + 5.5, top + Hb / 2 - 9); ctx.lineTo(left + bw + 5.5, top + Hb / 2 + 9); ctx.stroke();
        // flashes where particles hit a wall
        for (const f of flashes) {
          ctx.globalAlpha = Math.max(0, f.life) * 0.9;
          ctx.fillStyle = col.red;
          ctx.beginPath(); ctx.arc(left + f.x * s, top + f.y * s, 6, 0, 2 * Math.PI); ctx.fill();
        }
        ctx.globalAlpha = 1;
        // particles
        const r = Math.max(2, Math.min(4, RAD * s));
        ctx.save();
        ctx.beginPath(); ctx.rect(left, top, bw, Hb); ctx.clip();
        for (let i = st.n - 1; i >= 0; i--) {
          const X = left + px[i] * s, Y = top + py[i] * s;
          if (reduced) {
            ctx.strokeStyle = col.ink3; ctx.lineWidth = 1;
            const ex = X + vx[i] * s * 0.3, ey = Y + vy[i] * s * 0.3;
            const len = Math.hypot(ex - X, ey - Y);
            if (len > 3) {
              const ux = (ex - X) / len, uy = (ey - Y) / len;
              ctx.beginPath(); ctx.moveTo(X, Y); ctx.lineTo(ex, ey);
              ctx.moveTo(ex, ey); ctx.lineTo(ex - 5 * ux + 3 * uy, ey - 5 * uy - 3 * ux);
              ctx.moveTo(ex, ey); ctx.lineTo(ex - 5 * ux - 3 * uy, ey - 5 * uy + 3 * ux);
              ctx.stroke();
            }
          }
          ctx.fillStyle = i === 0 ? col.red : col.sc;
          ctx.beginPath(); ctx.arc(X, Y, i === 0 ? r + 1 : r, 0, 2 * Math.PI); ctx.fill();
        }
        ctx.restore();
        ctx.fillStyle = col.ink3; ctx.font = '12px ' + col.font; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
        ctx.fillText('width ' + W.fmt(st.w, 3) + ' cm · height and depth 10 cm' + (reduced ? ' · frozen snapshot, arrows show the velocities' : ''), left, top + Hb + 20);
        ctx.restore();
      }
    });
    box.wrap.style.touchAction = 'pan-y';
    W.drag(box.wrap, {
      hit(x, y) {
        const wx = geo.left + st.w * geo.s + 4;
        if (Math.abs(x - wx) < 16 && y > geo.top - 12 && y < geo.top + HEIGHT * geo.s + 12) { dragging = true; return 'wall'; }
        return null;
      },
      move(thing, x) {
        const v = Math.round(Math.min(20, Math.max(5, (x - geo.left) / geo.s)) * 2) / 2;
        sV.set(v);
        setWidth(v);
      },
      end() { dragging = false; box.redraw(); }
    });

    // ---- histogram -------------------------------------------------------------
    let xmax = 1500;
    const hist = W.canvas(body, {
      height: 170,
      draw(ctx, w, h, col) {
        const crms = cReal();
        xmax = XMAXES.find((v) => v >= 2.5 * crms) || XMAXES[XMAXES.length - 1];
        const counts = new Array(NB).fill(0);
        let sum = 0;
        for (let i = 0; i < st.n; i++) {
          const sp = Math.hypot(vx[i], vy[i]) * SCALE;
          sum += sp;
          counts[Math.min(NB - 1, Math.floor(sp / xmax * NB))]++;
        }
        const mean = sum / Math.max(1, st.n);
        const ymax = Math.max(4, Math.ceil(Math.max.apply(null, counts) * 1.45));
        const ax = W.axes(ctx, w, h, { x0: 0, x1: xmax, y0: 0, y1: ymax }, col, {
          pad: { l: 40, r: 14, t: 14, b: 40 },
          xlabel: 'speed / m s⁻¹', ylabel: 'particles',
          fy: (v) => (Number.isInteger(v) ? String(v) : ''),
          nx: 5, ny: 4
        });
        const { X, Y } = ax;
        ctx.save();
        ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
        const bwid = xmax / NB;
        ctx.fillStyle = col.sc; ctx.globalAlpha = 0.8;
        for (let b = 0; b < NB; b++) {
          if (!counts[b]) continue;
          const x0 = X(b * bwid) + 1, x1 = X((b + 1) * bwid) - 1;
          ctx.fillRect(x0, Y(counts[b]), Math.max(1, x1 - x0), Y(0) - Y(counts[b]));
        }
        ctx.globalAlpha = 1;
        // mean speed (dashed) and r.m.s. speed (solid)
        ctx.lineWidth = 1.5; ctx.strokeStyle = col.ink2; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(X(mean), Y(0)); ctx.lineTo(X(mean), ax.pad.t); ctx.stroke();
        ctx.setLineDash([]);
        ctx.lineWidth = 2.5; ctx.strokeStyle = col.red;
        ctx.beginPath(); ctx.moveTo(X(crms), Y(0)); ctx.lineTo(X(crms), ax.pad.t); ctx.stroke();
        ctx.fillStyle = col.ink; ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic';
        ctx.textAlign = 'right'; ctx.fillText('mean', X(mean) - 5, ax.pad.t + 12);
        ctx.fillStyle = col.red; ctx.textAlign = 'left'; ctx.fillText('r.m.s.', X(crms) + 5, ax.pad.t + 12);
        ctx.restore();
      }
    });

    // ---- readout -----------------------------------------------------------------
    const ro = W.readout([
      ['N', 'Number of molecules N'], ['V', 'Volume V'], ['T', 'Temperature T'], ['p', 'Pressure p = NkT / V'],
      ['m', 'Mass of one molecule m = M / N_A'], ['c', 'r.m.s. speed √(3kT/m)'], ['ek', 'Mean kinetic energy 3kT/2'], ['hits', 'Wall hits per second (drawn particles)']
    ]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);
    note.textContent = 'Each drawn particle stands for 10²⁰ molecules, and the box is 10 cm high and 10 cm deep, so its width sets the volume. ' +
      'Speeds on the screen are slowed (1 cm/s stands for 50 m s⁻¹) but keep the true scaling: the r.m.s. speed goes as √T and as 1/√m. ' +
      'The highlighted particle can be followed. Try: raise T and watch the speeds and the hit rate rise; narrow the box (drag the wall) and watch the hit rate and the pressure rise; ' +
      'switch to helium and see the same temperature give faster molecules.';

    let rate = 0, lastShown = 0;
    function analyticRate() {
      let s = 0;
      for (let i = 0; i < st.n; i++) s += Math.abs(vx[i]) / st.w + Math.abs(vy[i]) / HEIGHT;
      return s;
    }
    function readouts() {
      const g = GASES[st.gas];
      const N = st.n * PER, V = st.w * HEIGHT * HEIGHT * 1e-6;     // m³
      const p = N * KB * st.T / V;
      const c = cReal();
      ro.set('N', sci(N, 2));
      ro.set('V', sci(V, 3) + ' m³ (' + W.fmt(V * 1e3, 3) + ' L)');
      ro.set('T', W.fmt(st.T, 3) + ' K (' + W.fmt(st.T - 273.15, 3) + ' °C)');
      ro.set('p', sci(p, 3) + ' Pa');
      ro.set('m', sci(mOf(), 3) + ' kg (' + g.name + ', M = ' + g.M + ' kg mol⁻¹)');
      ro.set('c', W.fmt(c, 3) + ' m s⁻¹');
      ro.set('ek', sci(1.5 * KB * st.T, 3) + ' J');
      ro.set('hits', W.fmt(rate, 3) + ' s⁻¹');
    }
    function changed() {
      rate = analyticRate();
      flashes = [];
      readouts(); box.redraw(); hist.redraw();
    }

    // ---- motion --------------------------------------------------------------------
    function addFlash(x, y) { if (flashes.length < 80) flashes.push({ x, y, life: 1 }); }
    function step(dt) {
      const w = st.w, n = st.n;
      let hits = 0;
      const sub = Math.max(1, Math.ceil(dt / 0.01));
      const h = dt / sub;
      for (let k = 0; k < sub; k++) {
        for (let i = 0; i < n; i++) {
          let x = px[i] + vx[i] * h, y = py[i] + vy[i] * h;
          if (x < RAD) { x = 2 * RAD - x; vx[i] = Math.abs(vx[i]); hits++; addFlash(0, y); }
          else if (x > w - RAD) { x = 2 * (w - RAD) - x; vx[i] = -Math.abs(vx[i]); hits++; addFlash(w, y); }
          if (y < RAD) { y = 2 * RAD - y; vy[i] = Math.abs(vy[i]); hits++; addFlash(x, 0); }
          else if (y > HEIGHT - RAD) { y = 2 * (HEIGHT - RAD) - y; vy[i] = -Math.abs(vy[i]); hits++; addFlash(x, HEIGHT); }
          px[i] = Math.min(w - RAD, Math.max(RAD, x)); py[i] = Math.min(HEIGHT - RAD, Math.max(RAD, y));
        }
      }
      for (const f of flashes) f.life -= dt / 0.25;
      flashes = flashes.filter((f) => f.life > 0);
      return hits;
    }
    let last = performance.now();
    const anim = W.animate(() => {
      const now = performance.now();
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      if (dt <= 0) return true;
      const hits = step(dt);
      rate += (hits / dt - rate) * (1 - Math.exp(-dt / 1.0));
      box.redraw();
      if (now - lastShown > 250) { lastShown = now; ro.set('hits', W.fmt(rate, 3) + ' s⁻¹'); }
      return true;
    }, { still: () => { rate = analyticRate(); readouts(); box.redraw(); } });

    rate = analyticRate();
    readouts();
    if (reduced) { anim.start(); } else { last = performance.now(); anim.start(); }
  });
})();
