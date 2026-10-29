/* widgets/bio-actionpot.js: the action potential of a neurone. Used in bio.nerves.
   Model (a textbook-style trace, stated on screen): resting -70 mV, threshold about -50 mV, peak +35 mV, undershoot to -80 mV.
   The trace passes through these control points (the same as the table in the chapter), joined by a monotone cubic:
     (0,-70) (0.5,-70) (0.75,-50) (1.0,35) (1.5,-20) (2.0,-75) (3.0,-80) (4.0,-72) (5.0,-70)   [ms, mV]
   Stimulus applied at 0.5 ms. Single mode: a stimulus below 20 mV of depolarisation (threshold) gives only a local change that dies away.
   Train mode: frequency f(s) = 0 for strength s < 10, else min(500, 8 (s - 8)) per second; refractory period 2 ms (max 500 per second).
   Attributes: data-mode = single | train (default single); data-stage 0-4, data-dep 0-30 (mV), data-str 0-100 set the starting state. Pure functions are exported for data/test_bio-actionpot.js. */
(function () {
  'use strict';

  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const numOr = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? clamp(x, lo, hi) : d; };

  const REST = -70, THRESH = -50, PEAK = 35, T_STIM = 0.5, REFRACTORY = 2, MAXF = 500;
  const PTS = [[0, -70], [0.5, -70], [0.75, -50], [1.0, 35], [1.5, -20], [2.0, -75], [3.0, -80], [4.0, -72], [5.0, -70]];

  // monotone cubic (Fritsch-Carlson) through PTS
  const XS = PTS.map(p => p[0]), YS = PTS.map(p => p[1]);
  const N = XS.length, D = [], M = [];
  for (let i = 0; i < N - 1; i++) D.push((YS[i + 1] - YS[i]) / (XS[i + 1] - XS[i]));
  M.push(D[0]);
  for (let i = 1; i < N - 1; i++) M.push(D[i - 1] * D[i] <= 0 ? 0 : (D[i - 1] + D[i]) / 2);
  M.push(D[N - 2]);
  for (let i = 0; i < N - 1; i++) {
    if (D[i] === 0) { M[i] = 0; M[i + 1] = 0; continue; }
    const a = M[i] / D[i], b = M[i + 1] / D[i], s = a * a + b * b;
    if (s > 9) { const t = 3 / Math.sqrt(s); M[i] = t * a * D[i]; M[i + 1] = t * b * D[i]; }
  }
  function apV(t) {
    if (!isFinite(t) || t <= 0) return REST;
    if (t >= 5) return REST;
    for (let i = 0; i < N - 1; i++) {
      if (t <= XS[i + 1]) {
        const h = XS[i + 1] - XS[i], u = (t - XS[i]) / h;
        const h00 = 2 * u * u * u - 3 * u * u + 1, h10 = u * u * u - 2 * u * u + u, h01 = -2 * u * u * u + 3 * u * u, h11 = u * u * u - u * u;
        return h00 * YS[i] + h10 * h * M[i] + h01 * YS[i + 1] + h11 * h * M[i + 1];
      }
    }
    return REST;
  }
  // stimulus: depolarisation in mV applied at T_STIM; at or above 20 mV (threshold) the full action potential follows
  const THRESH_DEP = THRESH - REST;
  function singleV(t, dep) {
    if (dep >= THRESH_DEP) return apV(t);
    if (t <= T_STIM) return REST;
    const ramp = Math.min(1, (t - T_STIM) / 0.05);
    return REST + dep * ramp * Math.exp(-(t - T_STIM) / 0.35);
  }
  const STAGE_END = [0.5, 1.0, 2.0, 3.4, 5.0];
  const STAGES = ['Resting potential', 'Depolarisation', 'Repolarisation', 'Hyperpolarisation', 'Return to resting'];
  // channel states per stage for a full action potential
  const STATES = [
    { na: false, k: false, pump: true },
    { na: true, k: false, pump: true },
    { na: false, k: true, pump: true },
    { na: false, k: true, pump: true },
    { na: false, k: false, pump: true }
  ];
  function freq(s) { return s < 10 ? 0 : Math.min(MAXF, 8 * (s - 8)); }
  // start times (ms) of the impulses within a window
  function spikeTimes(f, window) {
    const out = [];
    if (!(f > 0) || !(window > 0)) return out;
    const period = 1000 / f;
    for (let t = 10; t < window && out.length < 400; t += period) out.push(t);
    return out;
  }
  function spikeV(tau) {            // shape of one impulse in the train, tau ms after it starts
    if (tau < 0) return REST;
    if (tau <= 1.5) return apV(T_STIM + tau);
    if (tau <= 2) return apV(2.0) + (REST - apV(2.0)) * (tau - 1.5) / 0.5;
    return REST;
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { apV, singleV, freq, spikeTimes, spikeV, numOr, clamp, STAGE_END, STATES, REST, THRESH, PEAK, THRESH_DEP, REFRACTORY, MAXF };
  if (typeof W === 'undefined') return;

  W.register('bio-actionpot', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'The action potential', 'A model trace, not data: values are textbook approximations');
    const S = { mode: opts.mode === 'train' ? 'train' : 'single', stage: Math.round(numOr(opts.stage, 0, 0, 4)), dep: Math.round(numOr(opts.dep, 25, 0, 30)), str: Math.round(numOr(opts.str, 40, 0, 100)) };

    function tag(ctx, c, txt, x, y, align, color) {
      ctx.save();
      ctx.font = '12px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round'; ctx.lineWidth = 4; ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }

    // own axes: x axis at the bottom (V = -100), y ticks at +40, 0, -40, -80
    function myAxes(ctx, w, h, xmax, xstep, c) {
      const L = 40, R = 10, T = 16, B = 30;
      if (w - L - R < 60 || h - T - B < 40) return null;
      const X = t => L + (t / xmax) * (w - L - R), Y = v => T + (50 - v) / 150 * (h - T - B);
      ctx.save();
      ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2;
      ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      [40, 0, -40, -80].forEach(function (v) {
        ctx.beginPath(); ctx.moveTo(L, Y(v)); ctx.lineTo(w - R, Y(v)); ctx.stroke();
        ctx.fillText((v > 0 ? '+' : (v < 0 ? '−' : '')) + Math.abs(v), L - 5, Y(v));
      });
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (let t = 0; t <= xmax + 1e-9; t += xstep) {
        ctx.beginPath(); ctx.moveTo(X(t), T); ctx.lineTo(X(t), h - B); ctx.stroke();
        ctx.fillText(String(t), X(t), h - B + 5);
      }
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(L, T - 4); ctx.lineTo(L, h - B); ctx.lineTo(w - R, h - B); ctx.stroke();
      ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText('membrane potential / mV', L + 6, T + 8);
      ctx.textAlign = 'right';
      ctx.fillText('time / ms', w - R, h - 4);
      ctx.restore();
      return { X: X, Y: Y };
    }

    // ---- tabs
    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'View' });
    const bSingle = W.h('button', { type: 'button', class: 'w-tab', text: 'One action potential' });
    const bTrain = W.h('button', { type: 'button', class: 'w-tab', text: 'A train of impulses' });
    tabs.appendChild(bSingle); tabs.appendChild(bTrain);
    body.appendChild(tabs);

    const boxSingle = W.h('div'), boxTrain = W.h('div');
    body.appendChild(boxSingle); body.appendChild(boxTrain);

    // ---- single mode
    let gInfo = null;
    function singleDescribe() {
      const sub = S.dep < THRESH_DEP;
      const end = STAGE_END[S.stage];
      const v = singleV(end, S.dep);
      return 'Model graph of membrane potential in millivolts against time from 0 to 5 milliseconds, drawn up to the stage "' + STAGES[S.stage] +
        '", where the potential is ' + Math.round(v) + ' millivolts. ' + (sub ? 'The stimulus is below the threshold, so only a small local change that dies away appears.' : 'The stimulus reaches the threshold of about minus 50 millivolts, so a full action potential follows.') +
        ' Below the graph a membrane diagram shows which channels are open.';
    }
    function drawChannel(ctx, c, cx, yTop, yBot, open, label, state, inward, arrowDir) {
      const my = (yTop + yBot) / 2, bw = 11, gap = open ? 16 : 6;
      ctx.save();
      ctx.lineWidth = 1.5; ctx.strokeStyle = c.sc; ctx.fillStyle = c.card;
      const l = cx - gap / 2 - bw, r = cx + gap / 2;
      ctx.beginPath(); ctx.rect(l, yTop - 6, bw, yBot - yTop + 12); ctx.fill(); ctx.stroke();
      ctx.beginPath(); ctx.rect(r, yTop - 6, bw, yBot - yTop + 12); ctx.fill(); ctx.stroke();
      if (!open) {
        ctx.fillStyle = c.sc2; ctx.beginPath(); ctx.rect(cx - gap / 2, my - 6, gap, 12); ctx.fill();
      }
      ctx.restore();
      return my;
    }
    function arrow(ctx, c, x, y0, y1, color, width) {
      const dir = y1 > y0 ? 1 : -1;
      ctx.save(); ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = width || 2.5;
      ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y1 - dir * 6); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x, y1); ctx.lineTo(x - 5, y1 - dir * 9); ctx.lineTo(x + 5, y1 - dir * 9); ctx.closePath(); ctx.fill();
      ctx.restore();
    }
    function drawSingle(ctx, w, h, c) {
      gInfo = null;
      if (!(w > 0) || !(h > 0) || w < 200 || h < 220) return;
      const hg = Math.round(h * 0.52);
      const A = myAxes(ctx, w, hg, 5, 1, c);
      if (!A) return;
      const px0 = A.X(0), px1 = A.X(5);
      ctx.save();
      ctx.beginPath(); ctx.rect(px0, A.Y(50), px1 - px0, A.Y(-100) - A.Y(50)); ctx.clip();
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      [REST, THRESH].forEach(function (v) { ctx.beginPath(); ctx.moveTo(px0, A.Y(v)); ctx.lineTo(px1, A.Y(v)); ctx.stroke(); });
      ctx.setLineDash([]);
      const end = STAGE_END[S.stage];
      ctx.strokeStyle = c.sc; ctx.lineWidth = 3; ctx.lineJoin = 'round';
      ctx.beginPath();
      for (let i = 0; i <= 500; i++) {
        const t = i * 0.01;
        if (t > end + 1e-9) break;
        const x = A.X(t), y = A.Y(singleV(t, S.dep));
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
      // stimulus marker
      ctx.fillStyle = c.red; ctx.beginPath();
      const sx = A.X(T_STIM), sy = A.Y(-100) - 3;
      ctx.moveTo(sx, sy); ctx.lineTo(sx - 5, sy + 0); ctx.lineTo(sx, sy - 9); ctx.lineTo(sx + 5, sy); ctx.closePath(); ctx.fill();
      // current point
      const ex = A.X(end), ey = A.Y(singleV(end, S.dep));
      ctx.beginPath(); ctx.arc(ex, ey, 5.5, 0, 2 * Math.PI); ctx.fillStyle = c.red; ctx.fill();
      ctx.lineWidth = 2; ctx.strokeStyle = c.card; ctx.stroke();
      ctx.restore();
      tag(ctx, c, 'threshold, about −50 mV', px1 - 4, A.Y(THRESH) - 5, 'right', c.ink2);
      tag(ctx, c, 'resting, −70 mV', px1 - 4, A.Y(REST) + 13, 'right', c.ink2);
      tag(ctx, c, 'stimulus', sx + 8, A.Y(-100) - 6, 'left', c.red);
      gInfo = { px0: px0, px1: px1 };

      // ---- membrane diagram
      const y0 = hg + 8, mH = h - y0 - 4;
      if (mH < 90) return;
      const mTop = y0 + Math.round(mH * 0.36), mBot = mTop + Math.round(mH * 0.26);
      const st = S.dep < THRESH_DEP ? { na: S.stage === 1, k: false, pump: true, few: true } : STATES[S.stage];
      ctx.save();
      ctx.fillStyle = c.card; ctx.strokeStyle = c.sc; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.rect(8, mTop, w - 16, mBot - mTop); ctx.fill(); ctx.stroke();
      ctx.restore();
      tag(ctx, c, 'outside the axon', 10, mTop - 16, 'left', c.ink2);
      tag(ctx, c, 'inside the axon', 10, mBot + 22, 'left', c.ink2);
      const cols = [w * 0.17, w * 0.50, w * 0.83];
      // voltage-gated Na+ channel
      drawChannel(ctx, c, cols[0], mTop, mBot, st.na, '', '', true);
      drawChannel(ctx, c, cols[1], mTop, mBot, st.k, '', '', false);
      // pump: a block with a label inside
      ctx.save(); ctx.fillStyle = c.card; ctx.strokeStyle = c.sc; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.rect(cols[2] - 26, mTop - 6, 52, mBot - mTop + 12); ctx.fill(); ctx.stroke();
      ctx.restore();
      tag(ctx, c, 'pump', cols[2], (mTop + mBot) / 2 + 4, 'center', c.ink);
      // arrows
      if (st.na) arrow(ctx, c, cols[0], mTop - 22, mBot + 22, c.sc, st.few ? 1.5 : 3.5);
      if (st.k) arrow(ctx, c, cols[1], mBot + 22, mTop - 22, c.sc2, 3.5);
      arrow(ctx, c, cols[2] - 20, mBot + 20, mTop - 16, c.ink2, 1.5);
      arrow(ctx, c, cols[2] + 20, mTop - 16, mBot + 20, c.ink2, 1.5);
      // text labels under each protein (state in words, not colour)
      const nal = st.na ? (st.few ? 'Na⁺ channels: few open' : 'Na⁺ channels: OPEN') : 'Na⁺ channels: closed';
      const kl = st.k ? 'K⁺ channels: OPEN' : 'K⁺ channels: closed';
      ctx.save(); ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink; ctx.textAlign = 'center';
      const ly = mBot + 40;
      if (w >= 300) {
        ctx.fillText(nal, cols[0], ly); ctx.fillText(kl, cols[1], ly); ctx.fillText('Na⁺/K⁺ pump', cols[2], ly);
        ctx.fillText('(Na⁺ in)', cols[0], ly + 13); ctx.fillText('(K⁺ out)', cols[1], ly + 13);
        ctx.fillText('3 Na⁺ out, 2 K⁺ in', cols[2], ly + 13);
      } else {
        ctx.fillText(nal.replace(' channels', ''), cols[0], ly); ctx.fillText(kl.replace(' channels', ''), cols[1], ly); ctx.fillText('pump', cols[2], ly);
      }
      ctx.restore();
    }
    let updateSingle = null, updateTrain = null;
    function buildSingle() {
    const cvS = W.canvas(boxSingle, {
      height: 400,
      label: 'Model graph of the membrane potential during one action potential, with a membrane diagram showing which channels are open at the chosen stage',
      describe: singleDescribe,
      draw: drawSingle
    });

    const CAPS = [
      'Resting potential, about −70 mV. The voltage-gated Na⁺ and K⁺ channels are closed. The pump keeps Na⁺ high outside and K⁺ high inside, and K⁺ leak out through other channels that are open at rest.',
      'Depolarisation. Once the threshold (about −50 mV) is reached, voltage-gated Na⁺ channels open. Na⁺ diffuse in down their electrochemical gradient and the inside becomes positive, up to about +35 mV.',
      'Repolarisation. The Na⁺ channels close and voltage-gated K⁺ channels open. K⁺ diffuse out through the channels and the inside becomes negative again.',
      'Hyperpolarisation. The K⁺ channels are slow to close, so too many K⁺ leave and the potential falls below the resting potential, to about −80 mV.',
      'Return to resting. The K⁺ channels close. The pump and the K⁺ leak channels restore the resting potential, −70 mV, and the ion gradients.'
    ];
    const CAPS_SUB = [
      'Resting potential, −70 mV, before the stimulus.',
      'The stimulus depolarises the membrane a little. A few Na⁺ channels open but the potential does not reach the threshold (about −50 mV), so the Na⁺ channels do not open in large numbers.',
      'No action potential. K⁺ leaving and the pump push the potential back towards −70 mV. The response is all-or-nothing: a stimulus below the threshold gives no impulse at all.',
      'The membrane has returned to the resting potential. Nothing was transmitted.',
      'Still at the resting potential, −70 mV. Raise the stimulus to the threshold (20 mV of depolarisation) or above to start an action potential.'
    ];
    const stepper = W.stepper(boxSingle, { steps: STAGES.length, labels: STAGES, onstep: function (i) { S.stage = i; updateSingle(); } });
    if (stepper.el && !stepper.el.parentNode) boxSingle.appendChild(stepper.el);
    const sDep = W.sliderNum({ label: 'Stimulus: depolarisation applied / mV (threshold is 20 mV)', min: 0, max: 30, step: 1, value: S.dep,
      oninput: function () { S.dep = Math.round(numOr(sDep.get(), 25, 0, 30)); updateSingle(); } });
    boxSingle.appendChild(W.h('div', { class: 'w-row' }, sDep.el));
    const roS = W.readout([['st', 'Stage'], ['v', 'Membrane potential'], ['ch', 'Channels']]);
    boxSingle.appendChild(roS.el);
    const capS = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    boxSingle.appendChild(capS);
    updateSingle = function () {
      const sub = S.dep < THRESH_DEP;
      const v = singleV(STAGE_END[S.stage], S.dep);
      roS.set('st', (S.stage + 1) + ' of 5: ' + (sub ? ['Resting potential', 'Small local depolarisation', 'Decaying back', 'Back at rest', 'At rest'][S.stage] : STAGES[S.stage]));
      roS.set('v', Math.round(v) + ' mV');
      const st = sub ? { na: S.stage === 1, k: false } : STATES[S.stage];
      roS.set('ch', 'Na⁺ ' + (st.na ? (sub ? 'few open' : 'open') : 'closed') + '; K⁺ ' + (st.k ? 'open' : 'closed') + '; pump working');
      capS.textContent = sub ? CAPS_SUB[S.stage] : CAPS[S.stage];
      cvS.redraw();
    };
    stepper.go(S.stage);
    }

    // ---- train mode
    function buildTrain() {
    function trainDescribe() {
      const f = freq(S.str);
      return 'Model graph of membrane potential against time for 50 milliseconds. ' + (f > 0 ? 'There are action potentials of the same height at ' + Math.round(f) + ' impulses per second' + (f >= MAXF ? ', the maximum set by the refractory period of 2 milliseconds.' : '.') : 'The stimulus is below the threshold, so there are no impulses.');
    }
    function drawTrain(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 200 || h < 130) return;
      const A = myAxes(ctx, w, h, 50, 10, c);
      if (!A) return;
      const px0 = A.X(0), px1 = A.X(50);
      const f = freq(S.str), times = spikeTimes(f, 50);
      ctx.save();
      ctx.beginPath(); ctx.rect(px0, A.Y(50), px1 - px0, A.Y(-100) - A.Y(50)); ctx.clip();
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(px0, A.Y(THRESH)); ctx.lineTo(px1, A.Y(THRESH)); ctx.stroke(); ctx.setLineDash([]);
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2.5; ctx.lineJoin = 'round';
      ctx.beginPath();
      const step = 0.1;
      for (let t = 0; t <= 50 + 1e-9; t += step) {
        let v = REST;
        for (let k = times.length - 1; k >= 0; k--) { if (t >= times[k]) { v = spikeV(t - times[k]); break; } }
        const x = A.X(t), y = A.Y(v);
        if (t === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();
      ctx.restore();
      tag(ctx, c, 'threshold', px0 + 4, A.Y(THRESH) - 5, 'left', c.ink2);
      if (!times.length) tag(ctx, c, 'no impulses: stimulus below threshold', (px0 + px1) / 2, A.Y(0), 'center', c.ink);
    }
    const cvT = W.canvas(boxTrain, {
      height: 250,
      label: 'Model graph of membrane potential over 50 milliseconds showing a train of identical action potentials',
      describe: trainDescribe,
      draw: drawTrain
    });
    const sStr = W.sliderNum({ label: 'Stimulus strength (weak to strong) / arbitrary units', min: 0, max: 100, step: 1, value: S.str,
      oninput: function () { S.str = Math.round(numOr(sStr.get(), 40, 0, 100)); updateTrain(); } });
    boxTrain.appendChild(W.h('div', { class: 'w-row' }, sStr.el));
    const roT = W.readout([['f', 'Impulses per second'], ['n', 'Impulses shown (50 ms)'], ['h', 'Height of each impulse'], ['g', 'Gap between impulses']]);
    boxTrain.appendChild(roT.el);
    const capT = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    boxTrain.appendChild(capT);
    updateTrain = function () {
      const f = freq(S.str), n = spikeTimes(f, 50).length;
      roT.set('f', f > 0 ? Math.round(f) + ' per second' : '0 (below threshold)');
      roT.set('n', String(n));
      roT.set('h', f > 0 ? 'about +' + PEAK + ' mV, always' : 'none');
      roT.set('g', f > 0 ? (1000 / f).toFixed(1) + ' ms' : 'none');
      capT.textContent = f <= 0 ? 'Below the threshold there is no impulse at all.' :
        (f >= MAXF ? 'The frequency has reached its maximum, 1 ÷ 0.002 s = 500 per second. A new impulse cannot start until the 2 ms refractory period is over, so a stronger stimulus cannot make the neurone fire faster.' :
          'A stronger stimulus makes the impulses more frequent, not bigger. Every impulse reaches the same height: the action potential is all-or-nothing.');
      cvT.redraw();
    };
    }

    body.appendChild(W.h('div', { class: 'w-note', text: 'A model, not data. One action potential: step through the five stages and look at the channels in the membrane diagram, then lower the stimulus below 20 mV to see all-or-nothing. A train of impulses: raise the stimulus and watch the frequency, not the height, change until the refractory period (modelled as 2 ms) sets the limit.' }));

    function setMode(m) {
      S.mode = m;
      boxSingle.style.display = m === 'single' ? '' : 'none';
      boxTrain.style.display = m === 'train' ? '' : 'none';
      bSingle.setAttribute('aria-pressed', m === 'single' ? 'true' : 'false');
      bTrain.setAttribute('aria-pressed', m === 'train' ? 'true' : 'false');
      if (m === 'single') { if (!updateSingle) buildSingle(); updateSingle(); }
      else { if (!updateTrain) buildTrain(); updateTrain(); }
    }
    bSingle.onclick = function () { setMode('single'); };
    bTrain.onclick = function () { setMode('train'); };
    setMode(S.mode);
  });
})();
