/* widgets/bio-cardiac.js: the cardiac cycle (data-bpm="75"). Used in bio.heart.
   MODEL pressure traces (kPa) of the left atrium, left ventricle and aorta for one cycle of 0.8 s at 75 beats per minute.
   KEY points and the monotone cubic (PCHIP) interpolation are copied from data/fig_cardiac.py, which draws the static graph
   of the chapter; data/test_bio-cardiac.js checks this file against data/cardiac_samples.json.
   Valves follow the pressures alone: the AV (mitral) valve is open when left atrial pressure > left ventricular pressure;
   the semilunar (aortic) valve is open when left ventricular pressure > aortic pressure.
   Heart rate rescales time: cycle T = 60 / bpm; systole S = min(0.4, 0.2 + 0.25 T) s (atrial S/4, ventricular 3S/4) and
   diastole T - S, so diastole shortens most (60 bpm: systole 0.4 s, diastole 0.6 s; 150 bpm: 0.3 s and 0.1 s).
   Pure functions are exported for data/test_bio-cardiac.js. */
(function () {
  'use strict';

  const KEY = {
    la: [[0.00, 0.90], [0.03, 1.30], [0.06, 1.55], [0.09, 1.30], [0.11, 0.95], [0.14, 0.80], [0.20, 0.85], [0.30, 1.05],
      [0.40, 1.25], [0.44, 1.18], [0.50, 0.80], [0.60, 0.60], [0.70, 0.70], [0.80, 0.90]],
    lv: [[0.00, 0.55], [0.04, 0.70], [0.08, 0.85], [0.10, 0.95], [0.12, 2.20], [0.14, 5.20], [0.16, 9.00], [0.18, 12.00],
      [0.21, 14.90], [0.25, 16.20], [0.30, 16.00], [0.34, 15.70], [0.37, 15.10], [0.385, 13.80], [0.40, 9.00],
      [0.42, 3.50], [0.44, 1.40], [0.46, 0.80], [0.50, 0.45], [0.60, 0.40], [0.70, 0.45], [0.80, 0.55]],
    ao: [[0.00, 10.80], [0.08, 10.62], [0.17, 10.50], [0.20, 11.80], [0.25, 15.30], [0.28, 15.80], [0.32, 15.45],
      [0.35, 15.05], [0.375, 14.65], [0.395, 14.25], [0.42, 14.60], [0.45, 14.20], [0.55, 12.70], [0.65, 11.60],
      [0.75, 10.95], [0.80, 10.80]]
  };
  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? clamp(Math.round(x), lo, hi) : d; };

  function pchip(pts) {
    const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]), n = xs.length;
    const d = [], m = new Array(n).fill(0);
    for (let i = 0; i < n - 1; i++) d.push((ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]));
    for (let i = 1; i < n - 1; i++) {
      if (d[i - 1] * d[i] > 0) {
        const h0 = xs[i] - xs[i - 1], h1 = xs[i + 1] - xs[i];
        const w1 = 2 * h1 + h0, w2 = h1 + 2 * h0;
        m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i]);
      }
    }
    return function (t) {
      t = clamp(t, xs[0], xs[n - 1]);
      let lo = 0, hi = n - 2;
      while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (xs[mid] <= t) lo = mid; else hi = mid - 1; }
      const i = lo, h = xs[i + 1] - xs[i], s = (t - xs[i]) / h;
      const h00 = 2 * s ** 3 - 3 * s ** 2 + 1, h10 = s ** 3 - 2 * s ** 2 + s, h01 = -2 * s ** 3 + 3 * s ** 2, h11 = s ** 3 - s ** 2;
      return h00 * ys[i] + h10 * h * m[i] + h01 * ys[i + 1] + h11 * h * m[i + 1];
    };
  }
  const LA = pchip(KEY.la), LV = pchip(KEY.lv), AO = pchip(KEY.ao);

  function phases(bpm) {
    const T = 60 / bpm, S = Math.min(0.4, 0.2 + 0.25 * T);
    return { T: T, S: S, a: S / 4, v: 0.75 * S, d: T - S };
  }
  function tau(t, bpm) {                       // real time in the cycle -> time in the 0.8 s model cycle
    const P = phases(bpm);
    if (t <= P.a) return 0.1 * t / P.a;
    if (t <= P.S) return 0.1 + 0.3 * (t - P.a) / (P.S - P.a);
    return 0.4 + 0.4 * (t - P.S) / (P.T - P.S);
  }
  function state(t, bpm) {
    const P = phases(bpm);
    t = clamp(isFinite(t) ? t : 0, 0, P.T);
    const k = tau(t, bpm), la = LA(k), lv = LV(k), ao = AO(k);
    return { t: t, la: la, lv: lv, ao: ao, avOpen: la > lv, slOpen: lv > ao,
      phase: t < P.a ? 'atrial systole' : t < P.S ? 'ventricular systole' : 'diastole' };
  }
  const EV_NAMES = ['AV valve closes', 'semilunar valve opens', 'semilunar valve closes', 'AV valve opens'];
  function events(bpm) {                       // valve events found from the pressures alone
    const P = phases(bpm), n = 1600, step = P.T / n, out = [];
    let s = state(0, bpm), pav = s.avOpen, psl = s.slOpen;
    for (let k = 1; k <= n; k++) {
      const t = k * step;
      s = state(t, bpm);
      if (s.avOpen !== pav) out.push({ t: Math.round(t * 1e4) / 1e4, name: s.avOpen ? 'AV valve opens' : 'AV valve closes' });
      if (s.slOpen !== psl) out.push({ t: Math.round(t * 1e4) / 1e4, name: s.slOpen ? 'semilunar valve opens' : 'semilunar valve closes' });
      pav = s.avOpen; psl = s.slOpen;
    }
    return out;
  }
  const f2 = x => x.toFixed(2);
  function reasons(s) {
    return {
      av: s.avOpen ? 'The pressure in the left atrium is higher than in the left ventricle, so the AV valve is open.'
        : 'The pressure in the left ventricle is higher than in the left atrium, so the AV valve is closed.',
      sl: s.slOpen ? 'The pressure in the left ventricle is higher than in the aorta, so the semilunar valve is open.'
        : 'The pressure in the aorta is higher than in the left ventricle, so the semilunar valve is closed.'
    };
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { KEY, LA, LV, AO, phases, tau, state, events, reasons, num, clamp };
  if (typeof W === 'undefined') return;

  W.register('bio-cardiac', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'The cardiac cycle', 'Move through one heartbeat and watch the pressures and the valves');
    const S = { bpm: num(opts.bpm, 75, 50, 150), t: 0, playing: false, busy: false, ev: [], P: null };

    // ---- controls ----
    const tInput = W.h('input', { type: 'range', min: '0', max: '0.8', step: '0.01', value: '0' });
    const tOut = W.h('span', { class: 'w-lab' });
    const tLab = W.h('label', { class: 'w-ctl', style: { flex: '1 1 220px' } }, W.h('span', { class: 'w-lab', text: 'Time in the cycle / s' }), tInput);
    const playBtn = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Play' });
    const nextBtn = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Next valve event' });
    const bpmSl = W.sliderNum({ label: 'Heart rate / beats per minute', min: 50, max: 150, step: 1, value: S.bpm,
      oninput: function () { if (S.busy) return; setBpm(num(bpmSl.get(), 75, 50, 150)); } });
    body.appendChild(W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } }, tLab, playBtn, nextBtn));
    body.appendChild(W.h('div', { class: 'w-row' }, bpmSl.el));

    // ---- drawing ----
    function tag(ctx, c, txt, x, y, align, size) {
      ctx.save();
      ctx.font = (size || 12) + 'px ' + (c.font || 'sans-serif');
      ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic'; ctx.lineJoin = 'round';
      ctx.lineWidth = 4; ctx.strokeStyle = c.card; ctx.strokeText(txt, x, y);
      ctx.fillStyle = c.ink; ctx.fillText(txt, x, y);
      ctx.restore();
    }
    function draw(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 200 || h < 140) return;
      const P = S.P, T = P.T, small = w < 420;
      const L = small ? 34 : 42, R = w - (small ? 84 : 96), Tp = 36, B = h - 36;
      const Wd = R - L, Hd = B - Tp;
      if (!(Wd > 20) || !(Hd > 20)) return;
      const X = t => L + Wd * t / T, Y = p => B - Hd * p / 18;
      const pal = (W.palette && W.palette(el)) || {};
      const ser = (pal.series && pal.series.length >= 3) ? pal.series : [c.sc, c.sc2, c.red];
      const cLV = ser[0], cAO = ser[1], cLA = ser[2];
      const st = state(S.t, S.bpm);
      ctx.save();
      // current phase shaded
      const span = st.phase === 'atrial systole' ? [0, P.a] : st.phase === 'ventricular systole' ? [P.a, P.S] : [P.S, T];
      ctx.globalAlpha = 0.12; ctx.fillStyle = c.sc; ctx.fillRect(X(span[0]), Tp, X(span[1]) - X(span[0]), Hd); ctx.globalAlpha = 1;
      // grid, axes, ticks
      ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
      [0, 5, 10, 15].forEach(p => { ctx.beginPath(); ctx.moveTo(L, Y(p)); ctx.lineTo(R, Y(p)); ctx.stroke(); });
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(L, Tp - 4); ctx.lineTo(L, B); ctx.lineTo(R + 4, B); ctx.stroke();
      ctx.font = '11px ' + (c.font || 'sans-serif'); ctx.fillStyle = c.ink2; ctx.textBaseline = 'alphabetic';
      ctx.textAlign = 'right';
      [0, 5, 10, 15].forEach(p => ctx.fillText(String(p), L - 6, Y(p) + 4));
      ctx.textAlign = 'center';
      const dt = (T <= 1.01 && Wd >= 260) ? 0.1 : 0.2;
      for (let k = 0; k * dt <= T + 1e-9; k++) { const t = k * dt; ctx.beginPath(); ctx.moveTo(X(t), B); ctx.lineTo(X(t), B + 4); ctx.stroke(); ctx.fillText(String(Math.round(t * 10) / 10), X(t), B + 16); }
      ctx.textAlign = 'right'; ctx.fillText('time / s', R + 4, B + 31);
      ctx.textAlign = 'left'; ctx.fillText('pressure / kPa', 4, 11);
      // valve events: dashed lines with numbers
      ctx.setLineDash([4, 4]); ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
      S.ev.forEach(e => { ctx.beginPath(); ctx.moveTo(X(e.t), B); ctx.lineTo(X(e.t), Tp); ctx.stroke(); });
      ctx.setLineDash([]);
      // traces
      const trace = (fn, col, wd, dash) => {
        ctx.save(); ctx.strokeStyle = col; ctx.lineWidth = wd; ctx.lineJoin = 'round'; if (dash) ctx.setLineDash(dash);
        ctx.beginPath();
        const n = Math.max(40, Math.round(Wd / 2));
        for (let i = 0; i <= n; i++) { const t = T * i / n, s = state(t, S.bpm); const px = X(t), py = Y(s[fn]); if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py); }
        ctx.stroke(); ctx.restore();
      };
      trace('ao', cAO, 2.5, [8, 4]); trace('la', cLA, 2.5, [2, 3]); trace('lv', cLV, 3);
      // cursor and dots
      ctx.strokeStyle = c.ink; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(X(st.t), Tp - 2); ctx.lineTo(X(st.t), B); ctx.stroke();
      ctx.fillStyle = c.ink; ctx.beginPath(); ctx.moveTo(X(st.t) - 5, Tp - 8); ctx.lineTo(X(st.t) + 5, Tp - 8); ctx.lineTo(X(st.t), Tp - 1); ctx.closePath(); ctx.fill();
      [['ao', cAO], ['la', cLA], ['lv', cLV]].forEach(k => {
        ctx.beginPath(); ctx.arc(X(st.t), Y(st[k[0]]), 4.5, 0, 2 * Math.PI); ctx.fillStyle = k[1]; ctx.fill();
        ctx.lineWidth = 1.5; ctx.strokeStyle = c.card; ctx.stroke();
      });
      ctx.restore();
      // event numbers (on top of everything), trace names at the right ends (stacked so they never touch)
      S.ev.forEach((e, i) => tag(ctx, c, String(i + 1), X(e.t), Tp - 12, 'center'));
      const aoEnd = state(T, S.bpm).ao;
      tag(ctx, c, 'aorta', R + 8, Y(aoEnd) + 4, 'left');
      tag(ctx, c, 'left atrium', R + 8, B - 17, 'left');
      tag(ctx, c, 'left ventricle', R + 8, B - 3, 'left');
    }

    const cv = W.canvas(body, {
      height: (el.clientWidth || 600) < 480 ? 290 : 320,
      label: 'Model pressure traces of the left atrium, left ventricle and aorta over one cardiac cycle',
      describe: function () {
        const s = state(S.t, S.bpm), ev = S.ev.map((e, i) => (i + 1) + ', ' + e.name + ' at ' + f2(e.t) + ' seconds').join('; ');
        return 'Model graph of pressure in kilopascals against time over one cycle of ' + f2(S.P.T) + ' seconds. The left ventricle pressure rises to about 16 kPa in ventricular systole; the aorta pressure stays between about 10.5 and 16 kPa; the left atrium pressure stays below about 1.6 kPa. Dashed lines mark valve events: ' + ev +
          '. The cursor is at ' + f2(s.t) + ' seconds, ' + s.phase + ': left atrium ' + s.la.toFixed(1) + ' kPa, left ventricle ' + s.lv.toFixed(1) + ' kPa, aorta ' + s.ao.toFixed(1) + ' kPa.';
      },
      draw: draw
    });

    const info = W.h('div', { class: 'w-note' });
    body.appendChild(info);
    const ro = W.readout([['ph', 'Phase'], ['av', 'AV (mitral) valve'], ['sl', 'Semilunar (aortic) valve'], ['hr', 'Heart rate'], ['du', 'Atrial systole, ventricular systole, diastole']]);
    body.appendChild(ro.el);
    const why = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.appendChild(why);
    const evLine = W.h('div', { class: 'w-note' });
    body.appendChild(evLine);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Model pressures for the left side of the heart (the right side follows the same pattern at lower pressures). Heart rate = 60 ÷ cycle time. Up to 75 beats per minute systole lasts 0.4 s; above that it shortens a little and diastole shortens most. Play runs at a quarter of real speed. The dashed lines 1 to 4 are the valve events, and Next valve event moves the cursor to each in turn.' }));

    const last = {};
    function setRow(k, v) { if (last[k] !== v) { last[k] = v; ro.set(k, v); } }
    let lastWhy = '';
    function update(redraw) {
      const s = state(S.t, S.bpm), r = reasons(s), P = S.P;
      tInput.setAttribute('aria-valuetext', f2(s.t) + ' seconds, ' + s.phase);
      info.textContent = 'Time ' + f2(s.t) + ' s of ' + f2(P.T) + ' s · left atrium ' + s.la.toFixed(1) + ' kPa · left ventricle ' + s.lv.toFixed(1) + ' kPa · aorta ' + s.ao.toFixed(1) + ' kPa';
      setRow('ph', s.phase);
      setRow('av', s.avOpen ? 'open' : 'closed');
      setRow('sl', s.slOpen ? 'open' : 'closed');
      setRow('hr', S.bpm + ' beats per minute (60 ÷ ' + f2(P.T) + ' s)');
      setRow('du', f2(P.a) + ' s, ' + f2(P.v) + ' s, ' + f2(P.d) + ' s');
      const wtxt = r.av + ' ' + r.sl;
      if (wtxt !== lastWhy) { lastWhy = wtxt; why.textContent = wtxt; }
      if (redraw !== false) cv.redraw();
    }
    function refreshModel() {
      S.P = phases(S.bpm);
      S.ev = events(S.bpm);
      const mx = Math.floor(S.P.T * 100) / 100;
      tInput.max = String(mx);
      evLine.textContent = 'Valve events: ' + S.ev.map((e, i) => (i + 1) + ' ' + e.name + ' at ' + f2(e.t) + ' s').join('; ') + '.';
    }
    function setBpm(b) {
      const frac = S.P ? S.t / S.P.T : 0;
      S.bpm = b; refreshModel();
      S.t = clamp(frac * S.P.T, 0, parseFloat(tInput.max));
      tInput.value = String(S.t);
      update();
    }
    function setPlaying(p) {
      S.playing = p; playBtn.textContent = p ? 'Pause' : 'Play';
      why.setAttribute('aria-live', p ? 'off' : 'polite');
    }
    function nextEvent() {
      const nxt = S.ev.find(e => e.t > S.t + 0.004);
      S.t = nxt ? Math.min(nxt.t + 0.002, S.P.T) : 0;       // just after the event, so the new valve state shows
      tInput.value = String(S.t);
      update();
    }

    tInput.addEventListener('input', function () {
      if (S.playing) { anim.stop(); setPlaying(false); }
      S.t = clamp(parseFloat(tInput.value) || 0, 0, S.P.T);
      update();
    });
    nextBtn.onclick = function () { if (S.playing) { anim.stop(); setPlaying(false); } nextEvent(); };

    let lastNow = 0;
    const anim = W.animate(function () {
      const now = Date.now(), dt = Math.min(0.1, (now - lastNow) / 1000);
      lastNow = now;
      S.t += dt * 0.25;                       // quarter speed
      if (S.t >= S.P.T) S.t -= S.P.T;
      tInput.value = String(Math.round(S.t * 100) / 100);
      update();
      return true;
    }, { still: nextEvent });
    playBtn.onclick = function () {
      if (S.playing) { anim.stop(); setPlaying(false); return; }
      if (W.reducedMotion && W.reducedMotion()) { anim.start(); return; }
      lastNow = Date.now(); setPlaying(true); anim.start();
    };

    refreshModel();
    update();
  });
})();
