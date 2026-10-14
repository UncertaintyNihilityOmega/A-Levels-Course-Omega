/* phys-ac: rectifying and smoothing an a.c. supply (phys.ac).
   data-v0="10" (peak p.d., V, 1–20)  data-f="50" (Hz, 10–100)  data-mode="none|half|full"
   data-c="0" (smoothing capacitor, µF, 0 = none, up to 2200)  data-r="1" (load, kΩ, 0.1–10)
   Model: ideal diode(s), optionally 0.7 V each. The capacitor follows the rectified p.d. while that is higher,
   otherwise it decays as V·exp(−Δt/RC) through the load. */
(function () {
  'use strict';
  W.register('phys-ac', function (el, opts) {
    const { body } = W.frame(el, 'Rectifying and smoothing an a.c. supply', 'Pick a rectifier, then add a smoothing capacitor and watch the ripple');
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const bad = (v) => v !== undefined && v !== '' && !isFinite(parseFloat(v));
    const MODES = ['none', 'half', 'full'];
    const problems = [];
    let mode = 'full';
    if (opts.mode !== undefined && opts.mode !== '') {
      if (MODES.indexOf(opts.mode) >= 0) mode = opts.mode;
      else { mode = 'none'; problems.push('Unknown rectifier "' + opts.mode + '": showing the unrectified supply.'); }
    }
    ['v0', 'f', 'c', 'r'].forEach((k) => { if (bad(opts[k])) problems.push('data-' + k + ' is not a number, so a default is used.'); });
    const st = {
      mode,
      v0: num(opts.v0, 10, 1, 20),
      f: num(opts.f, 50, 10, 100),
      c: num(opts.c, 0, 0, 2200),
      r: num(opts.r, 1, 0.1, 10),
      drop: false
    };
    const err = W.h('div', { class: 'w-err', style: { display: problems.length ? '' : 'none' } });
    err.textContent = problems.join(' ');

    function tabs(items, get, set) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Rectifier' });
      const btns = items.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); update(); } }, label));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    const modeTabs = tabs([['none', 'No rectifier'], ['half', 'Half-wave'], ['full', 'Full-wave']], () => st.mode, (v) => { st.mode = v; });

    const sV = W.sliderNum({ label: 'Peak p.d. V₀ / V', min: 1, max: 20, step: 0.5, value: st.v0, oninput: (v) => { st.v0 = num(v, 10, 1, 20); update(); } });
    const sF = W.slider({ label: 'Frequency', min: 10, max: 100, step: 1, value: st.f, fmt: (v) => v + ' Hz', oninput: (v) => { st.f = num(v, 50, 10, 100); update(); } });
    const sC = W.slider({ label: 'Smoothing capacitor C', min: 0, max: 2200, step: 10, value: st.c, fmt: (v) => (+v === 0 ? 'none' : v + ' μF'), oninput: (v) => { st.c = num(v, 0, 0, 2200); update(); } });
    const sR = W.sliderNum({ label: 'Load R / kΩ', min: 0.1, max: 10, step: 0.1, value: st.r, oninput: (v) => { st.r = num(v, 1, 0.1, 10); update(); } });
    const dropBox = W.h('input', { type: 'checkbox' });
    dropBox.addEventListener('change', () => { st.drop = dropBox.checked; update(); });
    const dropLab = W.h('label', { class: 'w-ctl', style: { display: 'flex', gap: '8px', alignItems: 'center' } }, dropBox, 'Include 0.7 V across each conducting diode');

    body.append(
      W.h('div', { class: 'w-row' }, modeTabs),
      W.h('div', { class: 'w-row' }, sV.el, sF.el),
      W.h('div', { class: 'w-row' }, sC.el, sR.el),
      W.h('div', { class: 'w-row' }, dropLab)
    );

    let cur = null;
    function simulate(s) {
      const T = 1 / s.f;
      const spc = 400, pre = 2, win = 4;
      const dt = T / spc;
      const nd = s.mode === 'half' ? 1 : s.mode === 'full' ? 2 : 0;
      const dropV = s.drop ? 0.7 * nd : 0;
      const RC = s.r * s.c * 1e-3;                    // kΩ × µF = ms, so ×1e-3 for seconds
      const smooth = s.mode !== 'none' && s.c > 0;
      let vc = 0;
      const tt = [], vin = [], vout = [];
      const total = (pre + win) * spc;
      for (let i = 0; i <= total; i++) {
        const t = i * dt;
        const v = s.v0 * Math.sin(2 * Math.PI * s.f * t);
        let o = s.mode === 'none' ? v : s.mode === 'half' ? Math.max(v - dropV, 0) : Math.max(Math.abs(v) - dropV, 0);
        if (smooth) { vc = Math.max(o, vc * Math.exp(-dt / RC)); o = vc; }
        if (i >= pre * spc) { tt.push((t - pre * T) * 1000); vin.push(v); vout.push(o); }
      }
      const last = vout.slice((win - 1) * spc);
      const hi = Math.max.apply(null, last), lo = Math.min.apply(null, last);
      return { T, tt, vin, vout, smooth, RC, hi, lo, ripple: hi - lo, peak: Math.max.apply(null, vout) };
    }

    const c = W.canvas(body, {
      height: 270,
      draw(ctx, w, h, col) {
        const s = cur;
        if (!s) return;
        const v0 = st.v0;
        const none = st.mode === 'none';
        const view = { x0: 0, x1: 4 * s.T * 1000, y0: none ? -1.15 * v0 : 0, y1: (none ? 1.7 : 1.45) * v0 };
        const pad = { l: 44, r: 14, t: 14, b: 44 };
        const ax = W.axes(ctx, w, h, view, col, { pad, ylabel: 'V / V', fx: () => '', ny: 5, nx: 4 });
        const { X, Y } = ax;
        ctx.save();
        ctx.fillStyle = col.ink3; ctx.font = '11px ' + (col.mono || 'monospace'); ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        ax.xt.forEach((v) => ctx.fillText(W.fmt(v, 4), X(v), h - pad.b + 5));
        ctx.textAlign = 'right'; ctx.textBaseline = 'bottom'; ctx.font = 'italic 12px ' + (col.font || 'sans-serif');
        ctx.fillText('t / ms', w - pad.r - 2, h - 2);
        ctx.restore();

        ctx.save();
        ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
        const trace = (ys, color, lw) => {
          ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineJoin = 'round'; ctx.beginPath();
          for (let i = 0; i < s.tt.length; i++) { const x = X(s.tt[i]), y = Y(ys[i]); if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y); }
          ctx.stroke();
        };
        if (!none) trace(s.vin, col.ink3, 1.5);
        trace(s.vout, col.sc, 2.5);
        if (s.smooth) {
          const x0 = X(3 * s.T * 1000), x1 = X(4 * s.T * 1000);
          ctx.strokeStyle = col.red; ctx.lineWidth = 1.3; ctx.setLineDash([5, 4]);
          ctx.beginPath(); ctx.moveTo(x0, Y(s.hi)); ctx.lineTo(x1, Y(s.hi)); ctx.moveTo(x0, Y(s.lo)); ctx.lineTo(x1, Y(s.lo)); ctx.stroke();
          ctx.setLineDash([]); ctx.lineWidth = 2;
          const xm = x1 - 8;
          ctx.beginPath(); ctx.moveTo(xm, Y(s.hi)); ctx.lineTo(xm, Y(s.lo)); ctx.stroke();
        }
        ctx.restore();

        ctx.save();
        ctx.fillStyle = col.ink2; ctx.font = '11px ' + (col.font || 'sans-serif'); ctx.textAlign = 'left'; ctx.textBaseline = 'top';
        ctx.fillText(none ? 'bold line: p.d. across the load (the supply itself)' : 'faint line: supply · bold line: across the load', pad.l + 8, pad.t + 22);
        if (s.smooth) ctx.fillText('dashed lines: ripple ΔV', pad.l + 8, pad.t + 36);
        ctx.restore();
      }
    });

    const ro = W.readout([
      ['v0', 'Peak value V₀ of the supply'],
      ['vr', 'V r.m.s. = V₀/√2'],
      ['t', 'Period T (frequency f)'],
      ['p', 'Mean power in R, unrectified: V r.m.s.² / R'],
      ['tau', 'Time constant RC'],
      ['rip', 'Ripple ΔV (from the simulation)'],
      ['est', 'Ripple from V₀t/RC (t = time between peaks)'],
      ['pct', 'Ripple as a percentage of the output peak']
    ]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);

    const fmtT = (s) => s >= 1 ? W.fmt(s, 3) + ' s' : W.fmt(s * 1000, 3) + ' ms';

    function update() {
      st.v0 = num(st.v0, 10, 1, 20); st.f = num(st.f, 50, 10, 100); st.c = num(st.c, 0, 0, 2200); st.r = num(st.r, 1, 0.1, 10);
      cur = simulate(st);
      const none = st.mode === 'none';
      sC.input.disabled = none;
      sC.el.style.opacity = none ? '0.5' : '';
      const vr = st.v0 / Math.SQRT2;
      ro.set('v0', W.fmt(st.v0, 3) + ' V');
      ro.set('vr', W.fmt(vr, 3) + ' V');
      ro.set('t', W.fmt(cur.T * 1000, 3) + ' ms (' + W.fmt(st.f, 3) + ' Hz)');
      ro.set('p', W.fmt(vr * vr / st.r, 3) + ' mW');
      let msg;
      if (cur.peak <= 0) {
        ro.set('tau', '–'); ro.set('rip', '–'); ro.set('est', '–'); ro.set('pct', '–');
        msg = 'The supply peak is below the diode drop, so no current flows. Raise V₀ or untick the diode drop.';
      } else if (cur.smooth) {
        const gap = st.mode === 'half' ? cur.T : cur.T / 2;
        const est = cur.peak * gap / cur.RC;
        ro.set('tau', fmtT(cur.RC));
        ro.set('rip', W.fmt(cur.ripple, 3) + ' V');
        ro.set('est', gap < cur.RC ? W.fmt(est, 3) + ' V' : 'RC is not much longer than t: the formula fails');
        ro.set('pct', W.fmt(100 * cur.ripple / cur.peak, 3) + ' %');
        msg = 'The capacitor charges to the peak, then discharges through R with time constant RC until the next peak tops it up. A larger C or R, or full-wave instead of half-wave, gives a smaller ripple.';
      } else {
        ro.set('tau', st.mode === 'none' ? '–' : 'no capacitor');
        ro.set('rip', '–'); ro.set('est', '–'); ro.set('pct', '–');
        msg = st.mode === 'none'
          ? 'Without a rectifier the load sees the alternating supply. Its mean value is zero, but the mean power in R is not: it is V r.m.s.² / R.'
          : st.mode === 'half'
            ? 'Half-wave: one diode passes the positive half-cycles only, so there is one pulse per cycle. Raise C above zero to smooth it.'
            : 'Full-wave: a bridge of four diodes passes every half-cycle the same way, so there are two pulses per cycle. Raise C above zero to smooth it.';
      }
      note.textContent = msg;
      c.redraw();
    }
    update();
  });
})();
