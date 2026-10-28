/* widgets/chem-boltzmann.js: the Boltzmann (Maxwell–Boltzmann) distribution of molecular energies at one or two temperatures,
   with the activation energy marked, the fraction of molecules with E >= Ea shaded, and an optional catalyst (lower Ea).
   Attributes: data-t1="300" (K, 250 to 600), data-t2="310" (K, 250 to 600), data-ea="50" (kJ per mol, 10 to 100),
   data-cat="0" or "1" (start with a catalyst).
   Model: f(E) = 2/sqrt(pi) * (RT)^(-3/2) * sqrt(E) * exp(-E/RT), the same area (1) at every temperature, R = 8.31 J K-1 mol-1.
   The fractions are found by Simpson integration of f from Ea upwards. The upper panel is drawn to scale; the lower panel
   enlarges the tail beyond Ea, because at real activation energies the shaded area is far too thin to see. */
(function () {
  'use strict';

  const R = 8.31e-3;                      // kJ K-1 mol-1
  const MINUS = '−';
  const SUPD = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  const sup = n => String(n).replace(/[0-9-]/g, c => SUPD[c]);

  const dens = (E, T) => {
    const rt = R * T;
    return E <= 0 ? 0 : 2 / Math.sqrt(Math.PI) * Math.pow(rt, -1.5) * Math.sqrt(E) * Math.exp(-E / rt);
  };
  // fraction of molecules with energy >= ea (kJ per mol) at T: Simpson's rule from ea to ea + 45 RT
  function tail(ea, T) {
    const rt = R * T, a = ea, b = ea + 45 * rt, n = 2000, h = (b - a) / n;
    let s = dens(a, T) + dens(b, T);
    for (let i = 1; i < n; i++) s += dens(a + i * h, T) * (i % 2 ? 4 : 2);
    return s * h / 3;
  }
  function pct(f) {
    const v = f * 100;
    if (!isFinite(v) || v <= 0) return '0 %';
    if (v >= 0.01) return W.fmt(v, 3) + ' %';
    const e = Math.floor(Math.log10(v));
    const m = v / Math.pow(10, e);
    return m.toFixed(2) + ' × 10' + sup(e) + ' %';
  }
  function times(x) {
    if (!isFinite(x)) return '—';
    if (x >= 1000) { const e = Math.floor(Math.log10(x)); return (x / Math.pow(10, e)).toFixed(2) + ' × 10' + sup(e); }
    return W.fmt(x, 3);
  }

  W.register('chem-boltzmann', function (el, opts) {
    const { body } = W.frame(el, 'Boltzmann distribution', 'Compare two temperatures and a catalyst');
    const msgs = [];
    function num(key, lo, hi, fb, what) {
      const raw = opts[key];
      if (raw === undefined || raw === '') return fb;
      const v = Number(String(raw).replace(MINUS, '-'));
      if (!isFinite(v)) { msgs.push('data-' + key + ' must be a number (' + what + '). Showing ' + fb + ' instead.'); return fb; }
      if (v < lo || v > hi) { msgs.push('data-' + key + ' = ' + raw + ' is outside ' + lo + ' to ' + hi + ' (' + what + '), so it was moved to the nearest allowed value.'); return Math.min(hi, Math.max(lo, v)); }
      return v;
    }
    const state = {
      t1: Math.round(num('t1', 250, 600, 300, 'temperature in K, from 250 to 600')),
      t2: Math.round(num('t2', 250, 600, 310, 'temperature in K, from 250 to 600')),
      ea: Math.round(num('ea', 10, 100, 50, 'activation energy in kJ mol⁻¹, from 10 to 100')),
      two: true, cat: false, eaCat: 30, catTouched: false
    };
    if (opts.cat !== undefined && opts.cat !== '') {
      const c = String(opts.cat).toLowerCase();
      if (c === '1' || c === 'true' || c === 'yes') state.cat = true;
      else if (c !== '0' && c !== 'false' && c !== 'no') msgs.push('data-cat must be 0 or 1. Showing the reaction without a catalyst.');
    }
    const defaultCat = () => Math.max(5, Math.round(state.ea * 0.6));
    state.eaCat = defaultCat();

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const sT1 = W.sliderNum({ label: 'Temperature T₁ (K)', min: 250, max: 600, step: 5, value: state.t1, oninput: v => { state.t1 = v; update(); } });
    const sT2 = W.sliderNum({ label: 'Temperature T₂ (K)', min: 250, max: 600, step: 5, value: state.t2, oninput: v => { state.t2 = v; update(); } });
    const sEa = W.sliderNum({ label: 'Activation energy Eₐ (kJ mol⁻¹)', min: 10, max: 100, step: 1, value: state.ea, oninput: v => { state.ea = v; update(); } });
    const sCat = W.sliderNum({ label: 'Eₐ with the catalyst (kJ mol⁻¹)', min: 5, max: 95, step: 1, value: state.eaCat, oninput: v => { state.eaCat = v; state.catTouched = true; update(); } });

    function check(label, key, onchange, checked) {
      const c = W.h('input', { type: 'checkbox', 'aria-label': label });
      c.checked = checked;
      c.onchange = () => onchange(c.checked);
      return W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, c, W.h('span', { class: 'w-lab', text: label }));
    }
    const rowChecks = W.h('div', { class: 'w-row' },
      check('show a second temperature T₂', 'two', v => { state.two = v; update(); }, state.two),
      check('add a catalyst', 'cat', v => { state.cat = v; if (v && !state.catTouched) state.eaCat = defaultCat(); update(); }, state.cat));

    body.appendChild(sT1.el);
    const t2Wrap = W.h('div', {}, sT2.el);
    body.appendChild(t2Wrap);
    body.appendChild(sEa.el);
    body.appendChild(rowChecks);
    const catWrap = W.h('div', {}, sCat.el);
    body.appendChild(catWrap);
    body.appendChild(err);

    function halo(ctx, col, s, x, y, align, color) {
      ctx.textAlign = align || 'left';
      ctx.lineWidth = 4; ctx.strokeStyle = col.card; ctx.lineJoin = 'round';
      ctx.strokeText(s, x, y);
      ctx.fillStyle = color || col.ink; ctx.fillText(s, x, y);
    }

    const legend = W.h('div', { class: 'w-note', style: { display: 'flex', flexWrap: 'wrap', gap: '4px 18px', alignItems: 'center' } });
    body.appendChild(legend);
    function swatch(color, dash) {
      return W.h('span', { 'aria-hidden': 'true', style: { display: 'inline-block', width: '22px', height: '0', borderTop: '3px ' + (dash ? 'dashed' : 'solid') + ' ' + color, marginRight: '6px', verticalAlign: 'middle' } });
    }
    function drawLegend() {
      legend.textContent = '';
      legend.appendChild(W.h('span', {}, swatch('var(--sc)'), 'T₁ = ' + state.t1 + ' K'));
      if (state.two) legend.appendChild(W.h('span', {}, swatch('var(--sc2)'), 'T₂ = ' + state.t2 + ' K'));
      legend.appendChild(W.h('span', {}, swatch('var(--ink-2)'), 'Eₐ' + (state.cat ? ' (solid) and Eₐ with the catalyst (dashed)' : '')));
    }

    const cvs = W.canvas(body, {
      height: 400,
      draw(ctx, w, h, col) {
        const left = 30, right = w - 12;
        const Tmax = Math.max(state.t1, state.two ? state.t2 : 0);
        const ea = state.ea, ec = state.cat ? state.eaCat : null;
        const xmax = Math.max(1.35 * ea, 10 * R * Tmax);
        const temps = [{ T: state.t1, c: col.sc, name: 'T₁ = ' + state.t1 + ' K' }];
        if (state.two) temps.push({ T: state.t2, c: col.sc2, name: 'T₂ = ' + state.t2 + ' K' });
        ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic'; ctx.lineCap = 'round'; ctx.lineJoin = 'round';

        function panel(top, bot, x0, x1, ymax, label, zoom) {
          const X = e => left + (right - left) * (e - x0) / (x1 - x0);
          const Y = v => bot - (bot - top) * v / ymax;
          // axes
          ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.6;
          ctx.beginPath(); ctx.moveTo(left, bot); ctx.lineTo(left, top - 2); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(left, bot); ctx.lineTo(right + 4, bot); ctx.stroke();
          // x ticks
          let tk = W.ticks(x0, x1, 5); if (!Array.isArray(tk) || !tk.length) tk = [x0, x1];
          ctx.fillStyle = col.ink2; ctx.textAlign = 'center';
          tk.forEach(v => { if (v < x0 - 1e-9 || v > x1 + 1e-9) return; ctx.strokeStyle = col.ink2; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(X(v), bot); ctx.lineTo(X(v), bot + 4); ctx.stroke(); ctx.fillText(W.fmt(v, 3), X(v), bot + 16); });
          ctx.textAlign = 'right'; ctx.fillStyle = col.ink2; ctx.fillText('energy / kJ mol⁻¹', right, bot + 31);
          ctx.save(); ctx.translate(10, (top + bot) / 2); ctx.rotate(-Math.PI / 2); ctx.textAlign = 'center'; ctx.fillText('number of molecules', 0, 0); ctx.restore();
          if (zoom) halo(ctx, col, label, left + 8, top - 10, 'left', col.ink2);
          else halo(ctx, col, label, left + 8, top + 8, 'left', col.ink2);

          // shaded tails
          const shade = (from, T, alpha, c) => {
            ctx.save(); ctx.beginPath(); ctx.rect(left, top - 2, right - left + 2, bot - top + 4); ctx.clip();
            ctx.globalAlpha = alpha; ctx.fillStyle = c; ctx.beginPath(); ctx.moveTo(X(from), bot);
            const n = 160;
            for (let i = 0; i <= n; i++) { const e = from + (x1 - from) * i / n; ctx.lineTo(X(e), Y(dens(e, T))); }
            ctx.lineTo(X(x1), bot); ctx.closePath(); ctx.fill(); ctx.restore();
          };
          temps.forEach(t => {
            if (ec !== null) shade(ec, t.T, 0.14, t.c);
            shade(ea, t.T, 0.34, t.c);
          });
          // curves
          ctx.save(); ctx.beginPath(); ctx.rect(left, top - 2, right - left + 2, bot - top + 4); ctx.clip();
          temps.forEach(t => {
            ctx.strokeStyle = t.c; ctx.lineWidth = 2.6; ctx.beginPath();
            const n = 300;
            for (let i = 0; i <= n; i++) { const e = x0 + (x1 - x0) * i / n; const y = Y(dens(e, t.T)); if (i) ctx.lineTo(X(e), y); else ctx.moveTo(X(e), y); }
            ctx.stroke();
          });
          ctx.restore();
          // Ea lines
          // neutral ink: in dark mode red and the course colour of the T1 curve look alike
          ctx.strokeStyle = col.ink2; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(X(ea), bot); ctx.lineTo(X(ea), top); ctx.stroke();
          halo(ctx, col, 'Eₐ', zoom ? X(ea) + 5 : X(ea) - 5, top + (zoom && ec !== null ? 30 : 12), zoom ? 'left' : 'right', col.ink2);
          if (ec !== null) {
            ctx.setLineDash([6, 4]); ctx.beginPath(); ctx.moveTo(X(ec), bot); ctx.lineTo(X(ec), top); ctx.stroke(); ctx.setLineDash([]);
            halo(ctx, col, 'Eₐ (catalyst)', zoom ? X(ec) + 5 : X(ec) - 5, top + 12, zoom ? 'left' : 'right', col.ink2);
          }
          return { X, Y };
        }

        // upper panel: to scale
        const ymax1 = Math.max.apply(null, temps.map(t => dens(R * t.T / 2, t.T))) * 1.12;
        const top1 = 14, bot1 = Math.round(h * 0.47);
        panel(top1, bot1, 0, xmax, ymax1, 'drawn to scale', false);
        // lower panel: the tail enlarged
        const e0 = ec !== null ? ec : ea;
        const ymax2 = Math.max.apply(null, temps.map(t => dens(e0, t.T))) * 1.2;
        const x1b = Math.min(xmax, Math.max(e0 + Math.max(0.6 * e0, 10 * R * Tmax), ec !== null ? 1.12 * ea : 0));
        const top2 = Math.round(h * 0.47) + 62, bot2 = h - 40;
        panel(top2, bot2, e0, Math.max(x1b, e0 + 1), ymax2, 'the tail beyond Eₐ, enlarged', true);
      }
    });
    cvs.cv.setAttribute('role', 'img');
    cvs.describe = () => {
      const f1 = tail(state.ea, state.t1), f2 = tail(state.ea, state.t2);
      let s = 'Upper graph, drawn to scale: number of molecules against energy in kJ per mole, one hump for ' + state.t1 + ' K' + (state.two ? ' and a lower, broader hump for ' + state.t2 + ' K' : '') + ', both with the same area. A vertical line marks Eₐ = ' + state.ea + ' kJ per mole'
        + (state.cat ? ' and a dashed line marks the catalysed Eₐ = ' + state.eaCat : '') + '. Lower graph: the tail beyond ' + (state.cat ? state.eaCat : state.ea) + ' kJ per mole enlarged. ';
      s += 'Molecules with at least Eₐ: ' + pct(f1) + ' at ' + state.t1 + ' K' + (state.two ? ', ' + pct(f2) + ' at ' + state.t2 + ' K' : '') + '.';
      return s.replace(/\s+/g, ' ');
    };

    const read = W.readout([['f1', 'Molecules with E ≥ Eₐ at T₁'], ['f2', 'Molecules with E ≥ Eₐ at T₂'], ['ratio', 'Ratio T₂ : T₁'], ['c1', 'With the catalyst at T₁'], ['cr', 'Catalyst: increase in that fraction']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Raise T₂ by 10 K and compare the shaded areas. The upper graph is drawn to scale: at a realistic Eₐ the shaded area is far too thin to see, so the lower graph enlarges it. The area under each whole curve is the same.' }));

    function update() {
      err.textContent = msgs.join(' ');
      drawLegend();
      t2Wrap.style.display = state.two ? '' : 'none';
      catWrap.style.display = state.cat ? '' : 'none';
      if (state.eaCat > state.ea - 5) { state.eaCat = Math.max(5, state.ea - 5); }
      sCat.set(state.eaCat);
      const f1 = tail(state.ea, state.t1);
      const f2 = state.two ? tail(state.ea, state.t2) : NaN;
      read.set('f1', pct(f1));
      read.set('f2', state.two ? pct(f2) : '(T₂ is switched off)');
      read.set('ratio', state.two ? '× ' + times(f2 / f1) + ' for a change from ' + state.t1 + ' K to ' + state.t2 + ' K' : '—');
      if (state.cat) {
        const fc = tail(state.eaCat, state.t1);
        read.set('c1', pct(fc) + ' (Eₐ = ' + state.eaCat + ' kJ mol⁻¹)');
        read.set('cr', '× ' + times(fc / f1) + ' at ' + state.t1 + ' K');
      } else { read.set('c1', 'no catalyst'); read.set('cr', '—'); }
      cvs.setLabel('Boltzmann distribution at ' + state.t1 + ' K' + (state.two ? ' and ' + state.t2 + ' K' : '') + (state.cat ? ', with and without a catalyst' : ''));
      cvs.redraw();
    }
    update();
  });
})();
