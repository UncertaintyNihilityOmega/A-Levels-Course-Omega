/* phys-rc: a capacitor discharging (or, for comparison, charging) through a resistor (phys.capacitance).
   data-c="100" capacitance in µF (1–2200)   data-r="50" resistance in kΩ (1–1000)   data-v="9" initial p.d. in V (1–20)
   data-mode="discharge|charge" (default discharge)   data-show="v|q|i|ln" (which quantity to plot first, default v)
   Shows V, Q, I or ln V against time, with τ, 2τ, 3τ marked, the 1/e level and the half-life, and a time cursor. */
(function () {
  'use strict';
  W.register('phys-rc', function (el, opts) {
    const { body } = W.frame(el, 'Capacitor discharging through a resistor', 'Change R, C and V₀, then move the time cursor');
    const notes = [];
    const get = (name, label, d, lo, hi) => {
      const raw = opts[name];
      if (raw === undefined || raw === null || raw === '') return d;
      const x = parseFloat(raw);
      if (!isFinite(x)) { notes.push(label + ' was not a number, so ' + d + ' is used.'); return d; }
      if (x < lo || x > hi) { notes.push(label + ' was outside ' + lo + '–' + hi + ', so it was limited to that range.'); return Math.min(hi, Math.max(lo, x)); }
      return x;
    };
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const st = {
      c: get('c', 'The capacitance', 100, 1, 2200),     // µF
      r: get('r', 'The resistance', 50, 1, 1000),       // kΩ
      v: get('v', 'The initial p.d.', 9, 1, 20),        // V
      mode: opts.mode === 'charge' ? 'charge' : 'discharge',
      tab: ['v', 'q', 'i', 'ln'].indexOf(opts.show) >= 0 ? opts.show : 'v',
      x: 1                                              // cursor time in units of τ
    };
    if (opts.mode && opts.mode !== 'charge' && opts.mode !== 'discharge') notes.push('The mode must be discharge or charge, so discharge is used.');
    const err = W.h('div', { class: 'w-err', style: { display: notes.length ? '' : 'none' } }, notes.join(' '));

    const E1 = Math.exp(-1), LN2 = Math.LN2;
    const tau = () => st.r * st.c * 1e-3;                     // s  (kΩ × µF = ms)
    const isCh = () => st.mode === 'charge';
    // fraction of the final (charge) or initial (discharge) value of V or Q at time x·τ
    const fracV = (x) => (isCh() ? 1 - Math.exp(-x) : Math.exp(-x));
    const fracI = (x) => Math.exp(-x);

    const fmtTime = (t) => (t >= 1 ? W.fmt(t, 3) + ' s' : t >= 1e-3 ? W.fmt(t * 1e3, 3) + ' ms' : W.fmt(t * 1e6, 3) + ' µs');
    const fmtQ = (uC) => (uC >= 1e6 ? W.fmt(uC / 1e6, 3) + ' C' : uC >= 1000 ? W.fmt(uC / 1000, 3) + ' mC' : W.fmt(uC, 3) + ' µC');
    const fmtI = (mA) => (mA >= 1 ? W.fmt(mA, 3) + ' mA' : W.fmt(mA * 1000, 3) + ' µA');
    const fmtE = (uJ) => (uJ >= 1e6 ? W.fmt(uJ / 1e6, 3) + ' J' : uJ >= 1000 ? W.fmt(uJ / 1000, 3) + ' mJ' : W.fmt(uJ, 3) + ' µJ');
    const fmtTick = (v) => String(parseFloat(v.toPrecision(3)));

    function tabs(items, get1, set1, aria) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': aria });
      const btns = items.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set1(v); sync(); update(); } }, label));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-pressed', String(items[i][0] === get1())));
      btns.forEach((b) => row.append(b));
      sync();
      row.sync = sync;
      row.btns = btns;
      return row;
    }
    const modeTabs = tabs([['discharge', 'Discharge'], ['charge', 'Charge (comparison)']], () => st.mode, (v) => { st.mode = v; }, 'Discharging or charging');
    const qtyTabs = tabs([['v', 'V'], ['q', 'Q'], ['i', 'I'], ['ln', 'ln V']], () => st.tab, (v) => { st.tab = v; }, 'Quantity to plot');

    const sC = W.sliderNum({ label: 'Capacitance C / µF', min: 1, max: 2200, step: 1, value: st.c, oninput: (v) => { st.c = num(v, st.c, 1, 2200); update(); } });
    const sR = W.sliderNum({ label: 'Resistance R / kΩ', min: 1, max: 1000, step: 1, value: st.r, oninput: (v) => { st.r = num(v, st.r, 1, 1000); update(); } });
    const sV = W.sliderNum({ label: 'Initial p.d. V₀ / V', min: 1, max: 20, step: 0.5, value: st.v, oninput: (v) => { st.v = num(v, st.v, 1, 20); update(); } });
    const sT = W.slider({ label: 'Time cursor', min: 0, max: 6, step: 0.01, value: st.x,
      fmt: (v) => W.fmt(v, 3) + ' τ = ' + fmtTime(v * tau()), oninput: (v) => { st.x = num(v, st.x, 0, 6); update(); } });

    body.append(
      W.h('div', { class: 'w-row' }, modeTabs, qtyTabs),
      W.h('div', { class: 'w-row' }, sC.el, sR.el, sV.el),
      W.h('div', { class: 'w-row' }, sT.el)
    );

    // the quantity currently plotted: returns {y(x), y0 (scale value), label, unit}
    function series() {
      const V0 = st.v, Q0 = st.c * st.v, I0 = st.v / st.r;     // V, µC, mA
      if (st.tab === 'v') return { f: (x) => V0 * fracV(x), top: V0, ylabel: 'V / V', kind: isCh() ? 'rise' : 'fall' };
      if (st.tab === 'q') {
        const big = Q0 >= 1000, k = big ? 1e-3 : 1;
        return { f: (x) => Q0 * k * fracV(x), top: Q0 * k, ylabel: 'Q / ' + (big ? 'mC' : 'µC'), kind: isCh() ? 'rise' : 'fall' };
      }
      if (st.tab === 'i') {
        const small = I0 < 1, k = small ? 1000 : 1;
        return { f: (x) => I0 * k * fracI(x), top: I0 * k, ylabel: 'I / ' + (small ? 'µA' : 'mA'), kind: 'fall' };
      }
      return { f: (x) => Math.log(V0) - x, top: Math.log(V0), ylabel: isCh() ? 'ln (V₀ − V)' : 'ln (V / V)', kind: 'line' };
    }

    function text(ctx, col, s, x, y, align, color, px, weight) {
      ctx.font = (weight || '500') + ' ' + (px || 12) + 'px ' + col.font;
      ctx.fillStyle = color || col.ink2; ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText(s, x, y);
    }

    const c = W.canvas(body, {
      height: 290,
      label: 'Graph of the capacitor against time in units of the time constant',
      describe: () => {
        const s = series(), t = tau(), cy = s.f(st.x);
        const what = st.tab === 'ln' ? 'ln V falls in a straight line of gradient −1/RC = ' + W.fmt(-1 / t, 3) + ' s⁻¹'
          : s.kind === 'rise' ? s.ylabel + ' rises exponentially to its final value ' + W.fmt(s.top, 3) + ', reaching 63% at one time constant'
            : s.ylabel + ' falls exponentially from ' + W.fmt(s.top, 3) + ', reaching 37% at one time constant and half at 0.693 τ';
        return 'Time from 0 to 6τ, with τ = RC = ' + fmtTime(t) + '. ' + what + '. The cursor is at ' + W.fmt(st.x, 3) + ' τ = ' + fmtTime(st.x * t) + ', where the value is ' + W.fmt(cy, 3) + ' on the scale shown.';
      },
      draw(ctx, w, h, col) {
        const s = series();
        const pad = { l: 52, r: 14, t: 24, b: 54 };
        const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
        const line = s.kind === 'line';
        const ymax = line ? s.top + 0.6 : s.top * 1.12;
        const ymin = line ? s.top - 6.4 : 0;
        const X = (x) => pad.l + pw * x / 6;
        const Y = (v) => pad.t + ph * (1 - (v - ymin) / (ymax - ymin));
        // grid and y ticks
        const yt = W.ticks(ymin, ymax, line ? 6 : 5) || [];
        ctx.lineWidth = 1;
        yt.forEach((v) => {
          ctx.strokeStyle = col.rule2 || col.rule; ctx.beginPath(); ctx.moveTo(pad.l, Y(v)); ctx.lineTo(w - pad.r, Y(v)); ctx.stroke();
          text(ctx, col, fmtTick(v), pad.l - 6, Y(v) + 4, 'right', col.ink2, 11);
        });
        for (let k = 1; k <= 6; k++) {
          ctx.strokeStyle = col.rule; ctx.setLineDash(k <= 3 ? [2, 3] : []); ctx.beginPath(); ctx.moveTo(X(k), pad.t); ctx.lineTo(X(k), pad.t + ph); ctx.stroke();
        }
        ctx.setLineDash([]);
        // axes
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.4;
        ctx.beginPath(); ctx.moveTo(pad.l, pad.t); ctx.lineTo(pad.l, pad.t + ph); ctx.lineTo(w - pad.r, pad.t + ph); ctx.stroke();
        text(ctx, col, s.ylabel, 4, 13, 'left', col.ink2, 12, '600');
        // x labels: multiples of τ, then the same times in seconds
        const sparse = pw / 6 < 52;
        for (let k = 0; k <= 6; k++) {
          const lab = k === 0 ? '0' : k === 1 ? 'τ' : k + 'τ';
          ctx.strokeStyle = col.ink3; ctx.beginPath(); ctx.moveTo(X(k), pad.t + ph); ctx.lineTo(X(k), pad.t + ph + 4); ctx.stroke();
          text(ctx, col, lab, X(k), pad.t + ph + 18, 'center', k >= 1 && k <= 3 ? col.ink : col.ink2, 12, k >= 1 && k <= 3 ? '700' : '500');
          if (!sparse || k % 2 === 0) text(ctx, col, k === 0 ? '0 s' : fmtTime(k * tau()), X(k), pad.t + ph + 34, k === 0 ? 'left' : k === 6 ? 'right' : 'center', col.ink3, 11);
        }
        // everything below is clipped to the plot area
        ctx.save();
        ctx.beginPath(); ctx.rect(pad.l, pad.t - 2, pw + 2, ph + 4); ctx.clip();
        if (line) {
          if (ymin < 0 && ymax > 0) {
            ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
            ctx.beginPath(); ctx.moveTo(pad.l, Y(0)); ctx.lineTo(w - pad.r, Y(0)); ctx.stroke(); ctx.setLineDash([]);
            text(ctx, col, 'ln V = 0', w - pad.r - 4, Y(0) - 5, 'right', col.ink3, 11);
          }
        } else {
          // 1/e (discharge) or 63% (charge) level and the half-value time
          const rise = s.kind === 'rise';
          const lev = (rise ? 1 - E1 : E1) * s.top;
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([5, 4]);
          ctx.beginPath(); ctx.moveTo(pad.l, Y(lev)); ctx.lineTo(w - pad.r, Y(lev)); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(X(LN2), Y(0)); ctx.lineTo(X(LN2), Y(0.5 * s.top)); ctx.stroke();
          ctx.setLineDash([]);
          text(ctx, col, rise ? '63% of final value' : '37% = 1/e of start', w - pad.r - 4, Y(lev) - 5, 'right', col.ink2, 11);
        }
        // the curve
        ctx.strokeStyle = col.sc; ctx.lineWidth = 3; ctx.beginPath();
        for (let i = 0; i <= 240; i++) {
          const x = 6 * i / 240, y = s.f(x);
          if (i === 0) ctx.moveTo(X(x), Y(y)); else ctx.lineTo(X(x), Y(y));
        }
        ctx.stroke();
        if (!line) {
          const rise = s.kind === 'rise';
          const px = X(LN2), py = Y(0.5 * s.top);
          ctx.fillStyle = col.card || col.sheet; ctx.strokeStyle = col.sc; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.arc(px, py, 4, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
          text(ctx, col, 't½ = 0.693 τ', px + 8, rise ? py + 16 : py - 7, 'left', col.ink, 11, '600');
        } else {
          const gr = -1 / tau();
          text(ctx, col, 'gradient = −1/RC', X(0.25), Y(s.top - 4.3), 'left', col.ink, 12, '600');
          text(ctx, col, '= ' + W.fmt(gr, 3) + ' s⁻¹', X(0.25), Y(s.top - 4.3) + 15, 'left', col.ink, 12, '600');
        }
        // cursor
        const cy = s.f(st.x);
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(pad.l, Y(cy)); ctx.lineTo(X(st.x), Y(cy)); ctx.lineTo(X(st.x), Y(ymin)); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(st.x), Y(cy), 5.5, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
      }
    });

    const ro = W.readout([
      ['tau', 'Time constant τ = RC'], ['th', 'Half-life 0.693 RC'], ['v', 'p.d. across the capacitor V'], ['q', 'Charge on the capacitor Q'],
      ['i', 'Current I'], ['e', 'Energy stored ½CV²'], ['f', 'Fraction of initial (final) energy'], ['g', 'Gradient of ln V against t']
    ]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);

    let busy = false;
    function update() {
      const t = tau();
      const x = st.x;
      const V = st.v * fracV(x), Q = st.c * V, I = st.v / st.r * fracI(x);
      const Ewin = 0.5 * st.c * V * V;            // µC × V / 2 = µJ
      ro.set('tau', fmtTime(t));
      ro.set('th', fmtTime(LN2 * t));
      ro.set('v', W.fmt(V, 3) + ' V');
      ro.set('q', fmtQ(Q));
      ro.set('i', fmtI(I));
      ro.set('e', fmtE(Ewin));
      ro.set('f', W.fmt(Math.pow(fracV(x), 2) * 100, 3) + ' %');
      ro.set('g', W.fmt(-1 / t, 3) + ' s⁻¹');
      if (!busy) { busy = true; sT.set(st.x); busy = false; }
      let extra;
      if (st.tab === 'ln') extra = isCh() ? 'Plotting ln (V₀ − V) against t gives a straight line of gradient −1/RC.' : 'ln V against t is a straight line of gradient −1/RC, so RC = −1/gradient.';
      else if (isCh()) extra = 'Charging: the p.d. rises to 63% of the final value in one time constant, the mirror image of the discharge curve (compare the current I, which falls).';
      else extra = 'After one time constant the value has fallen to 37% (1/e) of its start, and it halves every 0.693 RC.';
      note.textContent = 'Double R or C and the time constant doubles; the curve has the same shape, stretched in time. ' + extra;
      modeTabs.sync();
      qtyTabs.sync();
      c.redraw();
    }
    update();
  });
})();
