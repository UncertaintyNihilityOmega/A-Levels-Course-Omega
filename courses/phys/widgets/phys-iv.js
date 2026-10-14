/* phys-iv: I–V characteristics of a resistor, a filament lamp, a diode and a thermistor (phys.electricity).
   data-c="resistor|lamp|diode|thermistor"  (anything else falls back to resistor)
   Models: resistor 100 Ω; lamp I = 0.25 sign(V) (|V|/6)^0.6 A; diode I = 1e-9 (e^(V/0.05) - 1) A capped at 0.5 A;
   thermistor R = 10 kΩ exp(3950 (1/T - 1/298.15)). The diode slider covers ±2 V so the 0.6 V knee is visible. */
(function () {
  'use strict';
  W.register('phys-iv', function (el, opts) {
    const { body } = W.frame(el, 'I–V characteristics', 'Slide the p.d. and compare R = V/I with the gradient');
    const names = ['resistor', 'lamp', 'diode', 'thermistor'];
    const M = {
      resistor:   { tab: 'Resistor',       vmax: 6, imax: 0.065, def: 3,   h: 0.05,  I: (v) => v / 100 },
      lamp:       { tab: 'Filament lamp',  vmax: 6, imax: 0.30,  def: 3,   h: 0.05,  I: (v) => 0.25 * Math.sign(v) * Math.pow(Math.abs(v) / 6, 0.6) },
      diode:      { tab: 'Diode',          vmax: 2, imax: 0.55,  def: 0.7, h: 0.002, I: (v) => Math.min(0.5, 1e-9 * (Math.exp(v / 0.05) - 1)) },
      thermistor: { tab: 'Thermistor',     vmax: 6, imax: 0.010, def: 3,   h: 0.05,  I: (v, s) => v / rTherm(s.temp) }
    };
    const rTherm = (t) => 1e4 * Math.exp(3950 * (1 / (t + 273.15) - 1 / 298.15));   // ohms
    const bad = opts.c && names.indexOf(opts.c) < 0;
    const st = { c: names.indexOf(opts.c) >= 0 ? opts.c : 'resistor', v: 0, temp: 25, chord: true, tang: false };
    st.v = M[st.c].def;

    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    if (bad) { err.textContent = 'Unknown component "' + String(opts.c).slice(0, 30) + '", so the resistor is shown.'; err.style.display = ''; }

    const fmtI = (a) => {
      const x = Math.abs(a);
      if (x >= 1) return W.fmt(a, 3) + ' A';
      if (x >= 1e-3) return W.fmt(a * 1e3, 3) + ' mA';
      if (x >= 1e-6) return W.fmt(a * 1e6, 3) + ' µA';
      return W.fmt(a * 1e9, 3) + ' nA';
    };
    const fmtR = (r) => {
      const x = Math.abs(r);
      if (!isFinite(x)) return '—';
      if (x >= 1e9) return W.fmt(r / 1e9, 3) + ' GΩ';
      if (x >= 1e6) return W.fmt(r / 1e6, 3) + ' MΩ';
      if (x >= 1e3) return W.fmt(r / 1e3, 3) + ' kΩ';
      return W.fmt(r, 3) + ' Ω';
    };
    const cur = (v) => M[st.c].I(v, st);
    const slope = (v) => { const h = M[st.c].h; return (cur(v + h) - cur(v - h)) / (2 * h); };   // A per V

    const tabRow = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Component' });
    const btns = names.map((n) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => pick(n) }, M[n].tab));
    btns.forEach((b) => tabRow.append(b));
    const syncTabs = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(names[i] === st.c)));

    const vHold = W.h('div', { class: 'w-ctl', style: { flex: '1 1 220px' } });
    let vSlider = null;
    const buildV = () => {
      const m = M[st.c];
      vSlider = W.sliderNum({
        label: 'p.d. V / V', min: -m.vmax, max: m.vmax, step: 0.05, value: st.v,
        oninput: (x) => { const n = parseFloat(x); st.v = isFinite(n) ? Math.max(-m.vmax, Math.min(m.vmax, n)) : 0; update(); }
      });
      vHold.replaceChildren(vSlider.el);
    };
    const sT = W.slider({ label: 'Temperature', min: 0, max: 100, step: 1, value: st.temp, fmt: (x) => x + ' °C', oninput: (x) => { st.temp = parseFloat(x) || 0; update(); } });

    const mkCheck = (label, key) => {
      const inp = W.h('input', { type: 'checkbox' });
      inp.checked = !!st[key];
      inp.addEventListener('change', () => { st[key] = inp.checked; update(); });
      return W.h('label', { class: 'w-ctl', style: { display: 'flex', gap: '6px', alignItems: 'center' } }, inp, W.h('span', {}, label));
    };
    const chkChord = mkCheck('Line from the origin (gradient 1/R)', 'chord');
    const chkTang = mkCheck('Tangent at the point', 'tang');

    body.append(tabRow, W.h('div', { class: 'w-row' }, vHold, sT.el), W.h('div', { class: 'w-row' }, chkChord, chkTang));

    const c = W.canvas(body, {
      height: 290,
      draw(ctx, w, h, col) {
        const m = M[st.c];
        const pad = { l: 56, r: 14, t: 16, b: 34 };
        const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
        const vmax = m.vmax, imax = m.imax;
        const X = (v) => pad.l + (v + vmax) / (2 * vmax) * pw;
        const Y = (i) => pad.t + (imax - i) / (2 * imax) * ph;
        const niceStep = (span, n) => {
          const raw = span / n, p = Math.pow(10, Math.floor(Math.log10(raw))), f = raw / p;
          return (f < 1.5 ? 1 : f < 3.5 ? 2 : f < 7.5 ? 5 : 10) * p;
        };
        const sx = niceStep(2 * vmax, 6), sy = niceStep(2 * imax * 1000, 6);
        ctx.font = '11px system-ui, sans-serif';
        ctx.lineWidth = 1;
        ctx.strokeStyle = col.rule; ctx.fillStyle = col.ink3;
        ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        for (let v = Math.ceil(-vmax / sx) * sx; v <= vmax + 1e-9; v += sx) {
          ctx.beginPath(); ctx.moveTo(X(v), pad.t); ctx.lineTo(X(v), pad.t + ph); ctx.stroke();
          ctx.fillText(W.fmt(v, 2).replace(/^-/, '−'), X(v), pad.t + ph + 4);
        }
        ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
        for (let i = Math.ceil(-imax * 1000 / sy) * sy; i <= imax * 1000 + 1e-9; i += sy) {
          ctx.beginPath(); ctx.moveTo(pad.l, Y(i / 1000)); ctx.lineTo(pad.l + pw, Y(i / 1000)); ctx.stroke();
          ctx.fillText(W.fmt(i, 3).replace(/^-/, '−'), pad.l - 6, Y(i / 1000));
        }
        ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(pad.l, Y(0)); ctx.lineTo(pad.l + pw, Y(0)); ctx.moveTo(X(0), pad.t); ctx.lineTo(X(0), pad.t + ph); ctx.stroke();
        ctx.fillStyle = col.ink2; ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
        ctx.fillText('V / V', pad.l + pw / 2, h - 2);
        ctx.save();
        ctx.translate(12, pad.t + ph / 2); ctx.rotate(-Math.PI / 2);
        ctx.textBaseline = 'top'; ctx.fillText('I / mA', 0, 0);
        ctx.restore();

        ctx.save();
        ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
        // the characteristic
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.5; ctx.beginPath();
        const n = 400;
        for (let k = 0; k <= n; k++) {
          const v = -vmax + 2 * vmax * k / n, i = cur(v);
          if (k === 0) ctx.moveTo(X(v), Y(i)); else ctx.lineTo(X(v), Y(i));
        }
        ctx.stroke();
        const v0 = st.v, i0 = cur(v0);
        ctx.lineWidth = 1.5; ctx.setLineDash([6, 4]);
        if (st.chord && Math.abs(v0) > 1e-9) {
          ctx.strokeStyle = col.ink2;
          ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(v0), Y(i0)); ctx.stroke();
        }
        if (st.tang) {
          const g = slope(v0);
          ctx.strokeStyle = col.sc2;
          ctx.beginPath(); ctx.moveTo(X(-vmax), Y(i0 + g * (-vmax - v0))); ctx.lineTo(X(vmax), Y(i0 + g * (vmax - v0))); ctx.stroke();
        }
        ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(v0), Y(i0), 5.5, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
      }
    });

    const ro = W.readout([['v', 'p.d. V'], ['i', 'Current I'], ['r', 'Resistance R = V/I'], ['rt', '1 / gradient of the tangent']]);
    const note = W.h('div', { class: 'w-note' });
    const hint = W.h('div', { class: 'w-note' }, 'Try this: choose the filament lamp and compare R = V/I at 1 V and at 6 V. Then switch on the tangent. For a curve, 1/(tangent gradient) is not the resistance.');
    body.append(ro.el, note, hint, err);

    function describe(v, i) {
      if (st.c === 'resistor') return 'Model resistor of 100 Ω: R = V/I is the same at every point, so the graph is a straight line through the origin and the tangent lies on the line from the origin.';
      if (st.c === 'lamp') {
        const a = Math.abs(v);
        return 'Model lamp, 6 V 0.25 A. ' + (a < 1 ? 'The filament is cool and its resistance is low.' : a < 4 ? 'The filament is getting hot, so the ions vibrate more, collide with more electrons and R rises.' : 'The filament is white hot and its resistance is several times its cold value.') + ' The graph is symmetrical because the filament heats the same way in either direction.';
      }
      if (st.c === 'diode') {
        if (v < 0) return 'Model diode in reverse bias: almost no current flows, so the resistance is enormous.';
        if (v < 0.6) return 'Model diode in forward bias, but below about 0.6 V: the current is still tiny and R is large.';
        return 'Model diode above about 0.6 V: the current rises very steeply, so the resistance falls to a few ohms.';
      }
      return 'Thermistor (NTC) at ' + st.temp + ' °C: R = ' + fmtR(rTherm(st.temp)) + '. Raise the temperature and R falls, so the line gets steeper. It stays straight at each fixed temperature.';
    }

    function update() {
      const v = st.v, i = cur(v), g = slope(v);
      ro.set('v', W.fix(v, 2).replace(/^-/, '−') + ' V');
      ro.set('i', fmtI(i).replace(/^-/, '−'));
      ro.set('r', Math.abs(v) < 1e-9 ? '—' : fmtR(v / i));
      ro.set('rt', st.tang ? (Math.abs(g) < 1e-14 ? '—' : fmtR(1 / g)) : 'tangent off');
      note.textContent = describe(v, i);
      sT.el.style.display = st.c === 'thermistor' ? '' : 'none';
      c.redraw();
    }
    function pick(n) {
      st.c = n; st.v = M[n].def;
      syncTabs(); buildV(); update();
    }
    syncTabs(); buildV(); update();
  });
})();
