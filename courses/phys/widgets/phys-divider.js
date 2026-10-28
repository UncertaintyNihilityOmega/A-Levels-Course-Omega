/* phys-divider: a potential divider with a thermistor or an LDR (phys.dc).
   data-mode="thermistor|ldr"  data-pos="top|bottom" (where the sensor sits)
   data-vin="6" (supply p.d., V, 1–12)  data-r="2" (fixed resistor, kΩ, 0.5–50)
   Models: NTC thermistor R = 10 kΩ · exp(3950 (1/T − 1/298.15)); LDR R = 100 kΩ · (10 / lux)^0.8. */
(function () {
  'use strict';
  W.register('phys-divider', function (el, opts) {
    const { body } = W.frame(el, 'Potential divider with a sensor', 'Change the temperature or light and watch Vout');
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const st = {
      mode: opts.mode === 'ldr' ? 'ldr' : 'thermistor',
      pos: opts.pos === 'bottom' ? 'bottom' : 'top',
      vin: num(opts.vin, 6, 1, 12),
      r: num(opts.r, 2, 0.5, 50),
      temp: 20,
      lg: 2            // log10 of light intensity in lux
    };
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    if ((opts.vin && !isFinite(parseFloat(opts.vin))) || (opts.r && !isFinite(parseFloat(opts.r)))) {
      err.textContent = 'Some starting values were not numbers, so defaults are used.';
      err.style.display = '';
    }

    const rSensor = (s) => s.mode === 'thermistor'
      ? 10 * Math.exp(3950 * (1 / (s.temp + 273.15) - 1 / 298.15))   // kΩ
      : 100 * Math.pow(10 / Math.pow(10, s.lg), 0.8);                // kΩ
    const vout = (s, rs) => {
      const rb = s.pos === 'top' ? s.r : rs;    // bottom component carries Vout
      return s.vin * rb / (s.r + rs);
    };
    const fmtR = (k) => k >= 1000 ? W.fmt(k / 1000, 3) + ' MΩ' : k >= 1 ? W.fmt(k, 3) + ' kΩ' : W.fmt(k * 1000, 3) + ' Ω';

    function tabs(items, get, set, name) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': name });
      const btns = items.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); update(); } }, label));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-pressed', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    const modeTabs = tabs([['thermistor', 'Thermistor'], ['ldr', 'LDR']], () => st.mode, (v) => { st.mode = v; showCond(); }, 'Sensor type');
    const posTabs = tabs([['top', 'Sensor on top'], ['bottom', 'Sensor at bottom']], () => st.pos, (v) => { st.pos = v; }, 'Sensor position');

    const sVin = W.sliderNum({ label: 'Supply p.d. / V', min: 1, max: 12, step: 0.5, value: st.vin, oninput: (v) => { st.vin = num(v, 6, 1, 12); update(); } });
    const sR = W.sliderNum({ label: 'Fixed resistor / kΩ', min: 0.5, max: 50, step: 0.1, value: st.r, oninput: (v) => { st.r = num(v, 2, 0.5, 50); update(); } });
    const sT = W.slider({ label: 'Temperature', min: -10, max: 100, step: 1, value: st.temp, fmt: (v) => v + ' °C', oninput: (v) => { st.temp = v; update(); } });
    const sL = W.slider({ label: 'Light intensity', min: 0, max: 4, step: 0.05, value: st.lg, fmt: (v) => W.fmt(Math.pow(10, v), 2) + ' lux', oninput: (v) => { st.lg = v; update(); } });
    function showCond() { sT.el.style.display = st.mode === 'thermistor' ? '' : 'none'; sL.el.style.display = st.mode === 'ldr' ? '' : 'none'; }
    showCond();

    body.append(
      W.h('div', { class: 'w-row' }, modeTabs, posTabs),
      W.h('div', { class: 'w-row' }, sVin.el, sR.el),
      W.h('div', { class: 'w-row' }, sT.el, sL.el)
    );

    const c = W.canvas(body, {
      height: 250,
      label: 'Graph of Vout against temperature or light intensity',
      describe() {
        const th = st.mode === 'thermistor';
        const y0 = vout(st, rSensor(st));
        const lo = vout(Object.assign({}, st, th ? { temp: -10 } : { lg: 0 }), rSensor(Object.assign({}, st, th ? { temp: -10 } : { lg: 0 })));
        const hiS = Object.assign({}, st, th ? { temp: 100 } : { lg: 4 });
        const hi = vout(hiS, rSensor(hiS));
        return 'Vout in volts against ' + (th ? 'temperature from −10 to 100 °C' : 'light intensity from 1 to 10 000 lux (log scale)') + ', for supply ' + W.fmt(st.vin, 3) + ' V. The curve ' + (hi > lo ? 'rises' : 'falls') +
          ' from ' + W.fmt(lo, 3) + ' V to ' + W.fmt(hi, 3) + ' V. The marked point is at ' + (th ? W.fmt(st.temp, 3) + ' °C' : W.fmt(Math.pow(10, st.lg), 3) + ' lux') + ', where Vout is ' + W.fmt(y0, 3) + ' V.';
      },
      draw(ctx, w, h, col) {
        const th = st.mode === 'thermistor';
        const view = th ? { x0: -10, x1: 100, y0: 0, y1: Math.max(1, st.vin) * 1.08 } : { x0: 0, x1: 4, y0: 0, y1: Math.max(1, st.vin) * 1.08 };
        const ax = W.axes(ctx, w, h, view, col, {
          pad: { l: 40, r: 14, t: 14, b: 30 },
          xlabel: th ? 'θ / °C' : 'light / lux',
          ylabel: 'Vout / V',
          fx: th ? null : (v) => (Number.isInteger(v) ? W.fmt(Math.pow(10, v), 2) : ''),
          zeroX: true
        });
        const { X, Y } = ax;
        ctx.save();
        ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.5; ctx.beginPath();
        const n = 160;
        for (let i = 0; i <= n; i++) {
          const x = view.x0 + (view.x1 - view.x0) * i / n;
          const s = Object.assign({}, st, th ? { temp: x } : { lg: x });
          const y = vout(s, rSensor(s));
          if (i === 0) ctx.moveTo(X(x), Y(y)); else ctx.lineTo(X(x), Y(y));
        }
        ctx.stroke();
        const x0 = th ? st.temp : st.lg;
        const y0 = vout(st, rSensor(st));
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(X(view.x0), Y(y0)); ctx.lineTo(X(x0), Y(y0)); ctx.lineTo(X(x0), Y(0)); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(x0), Y(y0), 5, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
      }
    });

    const ro = W.readout([['rs', 'Sensor resistance'], ['i', 'Current'], ['vs', 'p.d. across sensor'], ['vf', 'p.d. across fixed resistor'], ['vo', 'Vout (across the bottom component)']]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);

    function update() {
      const rs = rSensor(st);
      const i = st.vin / (st.r + rs);            // mA, since kΩ
      const vs = i * rs, vf = i * st.r;
      ro.set('rs', fmtR(rs));
      ro.set('i', W.fmt(i, 3) + ' mA');
      ro.set('vs', W.fmt(vs, 3) + ' V');
      ro.set('vf', W.fmt(vf, 3) + ' V');
      ro.set('vo', W.fmt(st.pos === 'top' ? vf : vs, 3) + ' V');
      const cond = st.mode === 'thermistor' ? 'temperature' : 'light intensity';
      const rises = st.pos === 'top';
      note.textContent = 'Vout is taken across the bottom component. With the sensor ' + (rises ? 'on top' : 'at the bottom') +
        ', Vout ' + (rises ? 'rises' : 'falls') + ' as the ' + cond + ' rises, because the sensor’s resistance falls and it takes a smaller share of the supply p.d.';
      c.redraw();
    }
    update();
  });
})();
