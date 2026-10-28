/* phys-halflife: random radioactive decay of a grid of nuclei (phys.nuclear).
   data-n0="400"    number of nuclei, 50–400
   data-thalf="5"   half-life in arbitrary time units, 1–20
   Model: nucleus i decays at the random time t_i = −ln(u_i)/λ (u_i uniform, seeded W.rng), the same as a constant
   probability 1 − e^(−λΔt) of decaying in every step Δt. λ = 0.693/t½. The simulated count N(t) is the number with
   t_i > t; the smooth model is N₀ e^(−λt). The time cursor runs from 0 to 5 half-lives. */
(function () {
  'use strict';
  const MAXN = 400;
  const NSTEP = 60;                // simulation steps over the 5 half-lives drawn
  W.register('phys-halflife', function (el, opts) {
    const { body } = W.frame(el, 'Radioactive decay', 'Watch nuclei decay at random and compare with the smooth curve');
    const msgs = [];
    function num(raw, d, lo, hi, name) {
      if (raw === undefined || raw === null || String(raw).trim() === '') return d;
      const x = parseFloat(raw);
      if (!isFinite(x)) { msgs.push(name + ' = "' + raw + '" is not a number, so ' + d + ' is used.'); return d; }
      if (x < lo) { msgs.push(name + ' = ' + x + ' is below the range ' + lo + '–' + hi + ', so ' + lo + ' is used.'); return lo; }
      if (x > hi) { msgs.push(name + ' = ' + x + ' is above the range ' + lo + '–' + hi + ', so ' + hi + ' is used.'); return hi; }
      return x;
    }
    const st = {
      n0: Math.round(num(opts.n0, 400, 50, 400, 'Number of nuclei')),
      th: num(opts.thalf, 5, 1, 20, 'Half-life'),
      k: 0,                         // time cursor in half-lives, 0–5
      seed: 3,
      running: false
    };
    const reduced = W.reducedMotion();
    let base = [];                  // −ln(u) for each nucleus
    function reseed() {
      const r = W.rng(st.seed);
      base = [];
      for (let i = 0; i < MAXN; i++) base.push(-Math.log(Math.max(1e-12, r())));
    }
    reseed();
    const LN2 = 0.693;
    const lam = () => LN2 / st.th;
    const tNow = () => st.k * st.th;
    // number of nuclei undecayed at time t (simulation: decay time = base/λ)
    function simCount(t) {
      const lm = lam(); let c = 0;
      for (let i = 0; i < st.n0; i++) if (base[i] / lm > t) c++;
      return c;
    }
    const model = (t) => st.n0 * Math.exp(-lam() * t);

    // ---- controls -------------------------------------------------------------
    const err = W.h('div', { class: 'w-err', style: { display: msgs.length ? '' : 'none' } });
    err.textContent = msgs.join(' ');
    const sN = W.sliderNum({ label: 'Number of nuclei N₀', min: 50, max: 400, step: 10, value: st.n0, oninput: (v) => {
      const x = parseFloat(v); if (!isFinite(x)) return;
      st.n0 = Math.round(Math.min(400, Math.max(50, x))); update();
    } });
    const sT = W.sliderNum({ label: 'Half-life t½ / time units', min: 1, max: 20, step: 0.5, value: st.th, oninput: (v) => {
      const x = parseFloat(v); if (!isFinite(x)) return;
      st.th = Math.min(20, Math.max(1, x)); update();
    } });
    const sK = W.slider({ label: 'Time cursor', min: 0, max: 5, step: 0.01, value: st.k,
      fmt: (v) => W.fmt(v, 3) + ' half-lives (t = ' + W.fmt(v * st.th, 3) + ')', oninput: (v) => {
        const x = parseFloat(v); if (!isFinite(x)) return;
        st.k = Math.min(5, Math.max(0, x));
        if (st.running) setRunning(false);
        update();
      } });
    let last = 0;
    const anim = W.animate(() => {
      const now = performance.now();
      const dt = Math.min(0.1, (now - last) / 1000);
      last = now;
      st.k = Math.min(5, st.k + dt / 1.6);       // 5 half-lives in about 8 seconds
      sK.set(st.k);
      update();
      if (st.k >= 5) { setRunning(false); return false; }
      return true;
    }, { still: () => { st.k = 5; sK.set(5); update(); } });
    function setRunning(on) {
      if (on) {
        if (st.k >= 5) { st.k = 0; sK.set(0); }
        last = performance.now(); st.running = true; runBtn.textContent = 'Pause'; anim.start();
      } else {
        st.running = false; runBtn.textContent = 'Run'; anim.stop();
        speak();
      }
    }
    const runBtn = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => setRunning(!st.running) }, 'Run');
    const resBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => {
      if (st.running) setRunning(false);
      st.seed += 1; reseed(); st.k = 0; sK.set(0); update();
    } }, 'Reset (new random run)');
    if (reduced) runBtn.style.display = 'none';
    body.append(W.h('div', { class: 'w-row' }, sN.el, sT.el), W.h('div', { class: 'w-row' }, runBtn, resBtn), W.h('div', { class: 'w-row' }, sK.el));

    // ---- grid of nuclei -----------------------------------------------------------
    const grid = W.canvas(body, {
      height: 170,
      label: 'Grid of nuclei, filled where undecayed and outlined where decayed',
      describe: () => simCount(tNow()) + ' of the ' + st.n0 + ' nuclei are undecayed at time ' + W.fmt(tNow(), 3) + ' (' + W.fmt(st.k, 3) + ' half-lives).',
      draw(ctx, w, h, col) {
        const n = st.n0, t = tNow(), lm = lam();
        let s = Math.floor(Math.sqrt((w - 8) * (h - 8) / n));
        for (; s > 4; s--) {
          const cols = Math.floor((w - 8) / s);
          if (cols > 0 && Math.ceil(n / cols) * s <= h - 8) break;
        }
        s = Math.max(4, s);
        const cols = Math.max(1, Math.floor((w - 8) / s));
        const rad = Math.max(1.5, s * 0.36);
        const x0 = (w - cols * s) / 2 + s / 2, y0 = 4 + s / 2;
        for (let i = 0; i < n; i++) {
          const cx = x0 + (i % cols) * s, cy = y0 + Math.floor(i / cols) * s;
          const dead = base[i] / lm <= t;
          ctx.beginPath(); ctx.arc(cx, cy, rad, 0, 2 * Math.PI);
          if (dead) { ctx.strokeStyle = col.rule2; ctx.lineWidth = 1; ctx.stroke(); }
          else { ctx.fillStyle = col.sc; ctx.fill(); }
        }
      }
    });

    // ---- graph ------------------------------------------------------------------------
    const graph = W.canvas(body, {
      height: 250,
      label: 'Graph of the number of undecayed nuclei against time',
      describe: () => 'Number of nuclei N against time t. The smooth curve N₀e^(−λt) falls from ' + st.n0 + ' to ' + W.fmt(model(5 * st.th), 3) + ' at t = ' + W.fmt(5 * st.th, 3) +
        ', halving every ' + W.fmt(st.th, 3) + ' time units. The simulated steps follow it up to the cursor at t = ' + W.fmt(tNow(), 3) + ', where ' + simCount(tNow()) + ' nuclei remain against ' + W.fmt(model(tNow()), 3) + ' from the model.',
      draw(ctx, w, h, col) {
        // the axis runs 15% past the 5 half-lives drawn, so the curve's tail stays clear of the x-axis label
        const th = st.th, n0 = st.n0, lm = lam(), T = 5 * th;
        const ax = W.axes(ctx, w, h, { x0: 0, x1: 5.75 * th, y0: 0, y1: n0 * 1.08 }, col, { pad: { l: 48, r: 14, t: 24, b: 36 }, xlabel: 't / time units', ylabel: 'N' });
        const { X, Y } = ax;
        ctx.save();
        ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
        // half-life markers
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([5, 4]);
        for (let j = 1; j <= 3; j++) {
          const lv = n0 / Math.pow(2, j);
          ctx.beginPath(); ctx.moveTo(X(j * th), Y(0)); ctx.lineTo(X(j * th), Y(n0 * 1.08)); ctx.moveTo(X(0), Y(lv)); ctx.lineTo(X(j * th), Y(lv)); ctx.stroke();
        }
        ctx.setLineDash([]);
        // smooth model
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.8; ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const t = T * i / 200, y = Y(n0 * Math.exp(-lm * t));
          if (i === 0) ctx.moveTo(X(t), y); else ctx.lineTo(X(t), y);
        }
        ctx.stroke();
        // simulated count: steps up to the cursor
        const dtS = T / NSTEP, t = tNow();
        const kmax = Math.floor(t / dtS + 1e-9);
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.6; ctx.beginPath();
        ctx.moveTo(X(0), Y(simCount(0)));
        for (let k = 0; k < kmax; k++) {
          const yk = Y(simCount(k * dtS));
          ctx.lineTo(X((k + 1) * dtS), yk);
          ctx.lineTo(X((k + 1) * dtS), Y(simCount((k + 1) * dtS)));
        }
        ctx.lineTo(X(t), Y(simCount(kmax * dtS)));
        ctx.stroke();
        // cursor
        ctx.strokeStyle = col.red; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(X(t), Y(0)); ctx.lineTo(X(t), Y(n0 * 1.08)); ctx.stroke();
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(t), Y(simCount(t)), 4.5, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
        // labels
        ctx.font = '600 12px ' + col.font; ctx.textBaseline = 'alphabetic';
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
        ['t½', '2t½', '3t½'].forEach((txt, j) => ctx.fillText(txt, X((j + 1) * th), ax.pad.t + 12));
        ctx.textAlign = 'right';
        ['N₀/2', 'N₀/4', 'N₀/8'].forEach((txt, j) => ctx.fillText(txt, w - ax.pad.r - 2, Y(n0 / Math.pow(2, j + 1)) - 4));
        ctx.textAlign = 'right'; ctx.fillStyle = col.sc;
        ctx.fillText('steps: simulated count', w - ax.pad.r - 8, ax.pad.t + 32);
        ctx.fillStyle = col.ink2;
        ctx.fillText('thin line: N₀e^(−λt)', w - ax.pad.r - 8, ax.pad.t + 48);
      }
    });

    // ---- readout -----------------------------------------------------------------------
    const ro = W.readout([
      ['lam', 'Decay constant λ = 0.693 / t½'], ['t', 'Time t'], ['nm', 'N at the cursor (smooth model)'],
      ['ns', 'N at the cursor (simulated)'], ['a', 'Activity λN (model)'], ['fr', 'Fraction remaining (simulated)']
    ]);
    const note = W.h('div', { class: 'w-note' }, 'Each run is different (decay is random), but the larger N₀ is, the closer the steps follow the smooth curve.');
    body.append(ro.el, note, err);
    // the table changes on every frame of a run, so it is not read out; the summary is spoken when the run stops or the reader sets a value
    ro.el.setAttribute('aria-live', 'off');
    function speak() {
      W.say(body, 'At t = ' + W.fmt(tNow(), 3) + ' time units, ' + W.fmt(st.k, 3) + ' half-lives: ' + simCount(tNow()) + ' of ' + st.n0 + ' nuclei remain; the model gives ' + W.fmt(model(tNow()), 3) + '.');
    }

    function update() {
      const t = tNow(), nm = model(t), ns = simCount(t);
      ro.set('lam', W.fmt(lam(), 3) + ' per time unit');
      ro.set('t', W.fmt(t, 3) + ' time units (' + W.fmt(st.k, 3) + ' half-lives)');
      ro.set('nm', W.fmt(nm, 3));
      ro.set('ns', String(ns) + ' of ' + st.n0);
      ro.set('a', W.fmt(lam() * nm, 3) + ' decays per time unit');
      ro.set('fr', W.fmt(ns / st.n0, 3) + '  (model ' + W.fmt(nm / st.n0, 3) + ')');
      grid.redraw(); graph.redraw();
      if (!st.running) speak();
    }
    update();
    if (reduced) { st.k = 5; sK.set(5); update(); } else setRunning(true);
  });
})();
