/* phys-star: black-body spectrum, luminosity and size of a star (phys.astro).
   data-t="5800" (surface temperature, K, 2500–40000)  data-r="1" (radius in solar radii, 0.01–1000)
   data-d="" (optional distance, light-years, 1–1e9: switches on the radiant flux intensity readout)
   Planck: B(λ,T) ∝ λ⁻⁵ / (exp(hc/λkT) − 1). Wien b = 2.9×10⁻³ m K. L = 4πσr²T⁴ with σ = 5.67×10⁻⁸. */
(function () {
  'use strict';
  W.register('phys-star', function (el, opts) {
    const { body } = W.frame(el, 'Stars: temperature, colour, luminosity', 'Change T and r, or pick a star');
    const SIG = 5.67e-8, WIEN = 2.9e-3, C2 = 1.4388e-2;           // C2 = hc/k in m K
    const L_SUN = 3.83e26, R_SUN = 6.96e8, LY = 9.46e15;
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const bad = (v) => v !== undefined && v !== '' && !isFinite(parseFloat(v));
    const hasD = opts.d !== undefined && opts.d !== '' && isFinite(parseFloat(opts.d));

    const st = {
      T: num(opts.t, 5800, 2500, 40000),
      r: num(opts.r, 1, 0.01, 1000),
      dly: num(opts.d, 100, 1, 1e9),
      useD: hasD,
      same: false,
      preset: null
    };
    const PRESETS = [
      ['sun', 'Sun', 5800, 1],
      ['red', 'Red supergiant (approx.)', 3500, 1000],
      ['sirius', 'Sirius A-like (approx.)', 9900, 1.7],
      ['wd', 'White dwarf (approx.)', 25000, 0.01]
    ];
    PRESETS.forEach((p) => { if (p[2] === st.T && p[3] === st.r) st.preset = p[0]; });

    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    if (bad(opts.t) || bad(opts.r) || bad(opts.d)) {
      err.textContent = 'Some starting values were not numbers, so defaults are used.';
      err.style.display = '';
    }

    // ---------- physics helpers ----------
    const planck = (nm, T) => {                                    // relative spectral intensity, λ in nm
      const lam = nm * 1e-9;
      const x = C2 / (lam * T);
      if (x > 700) return 0;
      return 1 / (Math.pow(nm, 5) * (Math.exp(x) - 1));
    };
    const peakOf = (T) => planck(WIEN / T * 1e9, T);
    const SUN_T = 5800;
    const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
    const sup = (n) => String(n).split('').map((c) => SUP[c] || c).join('');
    const sci = (x, unit) => {
      if (!isFinite(x) || x <= 0) return '0 ' + unit;
      if (x >= 0.01 && x < 1e4) return W.fmt(x, 3) + ' ' + unit;
      let e = Math.floor(Math.log10(x));
      let m = x / Math.pow(10, e);
      if (Number(m.toFixed(2)) >= 10) { m /= 10; e += 1; }
      return m.toFixed(2) + ' × 10' + sup(e) + ' ' + unit;
    };
    const lum = (s) => 4 * Math.PI * SIG * Math.pow(s.r * R_SUN, 2) * Math.pow(s.T, 4);
    // approximate colour of a black body (Tanner Helland fit), returns [r, g, b]
    const bbColour = (T) => {
      const t = T / 100;
      const cl = (v) => Math.max(0, Math.min(255, Math.round(v)));
      const r = t <= 66 ? 255 : 329.698727446 * Math.pow(t - 60, -0.1332047592);
      const g = t <= 66 ? 99.4708025861 * Math.log(t) - 161.1195681661 : 288.1221695283 * Math.pow(t - 60, -0.0755148492);
      const b = t >= 66 ? 255 : t <= 19 ? 0 : 138.5177312231 * Math.log(t - 10) - 305.0447927307;
      return [cl(r), cl(g), cl(b)];
    };

    // ---------- controls ----------
    const tabRow = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose a star' });
    const btns = PRESETS.map((p) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => pick(p) }, p[1]));
    btns.forEach((b) => tabRow.append(b));
    const syncTabs = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(PRESETS[i][0] === st.preset)));

    const sT = W.sliderNum({ label: 'Surface temperature T / K', min: 2500, max: 40000, step: 100, value: st.T,
      oninput: (v) => { st.T = num(v, st.T, 2500, 40000); st.preset = null; syncTabs(); update(); } });
    const sR = W.slider({ label: 'Radius', min: -2, max: 3, step: 0.01, value: Math.log10(st.r),
      fmt: (v) => W.fmt(Math.pow(10, v), 3) + ' R☉',
      oninput: (v) => { st.r = num(Math.pow(10, v), st.r, 0.01, 1000); st.preset = null; syncTabs(); update(); } });
    const sD = W.slider({ label: 'Distance', min: 0, max: 9, step: 0.05, value: Math.log10(st.dly),
      fmt: (v) => sci(Math.pow(10, v), 'light-years'),
      oninput: (v) => { st.dly = num(Math.pow(10, v), st.dly, 1, 1e9); update(); } });

    const cbD = W.h('input', { type: 'checkbox' });
    cbD.checked = st.useD;
    cbD.addEventListener('change', () => { st.useD = cbD.checked; showD(); update(); });
    const cbS = W.h('input', { type: 'checkbox' });
    cbS.checked = st.same;
    cbS.addEventListener('change', () => { st.same = cbS.checked; update(); });
    const labD = W.h('label', { class: 'w-ctl' }, cbD, ' Set a distance (shows the flux F)');
    const labS = W.h('label', { class: 'w-ctl' }, cbS, ' Same scale as the Sun (hotter stars are higher)');
    function showD() { sD.el.style.display = st.useD ? '' : 'none'; }
    showD();

    body.append(
      tabRow,
      W.h('div', { class: 'w-row' }, sT.el, sR.el),
      W.h('div', { class: 'w-row' }, labS, labD),
      W.h('div', { class: 'w-row' }, sD.el)
    );

    function pick(p) {
      sT.set(p[2]); sR.set(Math.log10(p[3]));
      st.T = p[2]; st.r = p[3]; st.preset = p[0];   // set after the sliders, in case set() fires oninput
      syncTabs(); update();
    }

    // ---------- spectrum canvas ----------
    const c = W.canvas(body, {
      height: 250,
      draw(ctx, w, h, col) {
        const pkSelf = peakOf(st.T), pkSun = peakOf(SUN_T);
        const rel = pkSelf / pkSun;                                 // peak height relative to the Sun's peak
        const ymax = st.same ? 1.12 * Math.max(rel, 1) : 1.12;
        const scale = st.same ? 1 / pkSun : 1 / pkSelf;             // curve value → plot units
        const view = { x0: 0, x1: 3000, y0: 0, y1: ymax };
        const ax = W.axes(ctx, w, h, view, col, {
          pad: { l: 46, r: 14, t: 18, b: 32 },
          xlabel: 'λ / nm',
          ylabel: st.same ? 'intensity / (Sun’s peak)' : 'relative intensity',
          nx: 6, ny: 3,
          fy: (v) => W.fmt(v, 2)
        });
        const { X, Y } = ax;
        const x0p = ax.pad.l, y0p = ax.pad.t, wp = w - ax.pad.l - ax.pad.r, hp = h - ax.pad.t - ax.pad.b;
        ctx.save();
        ctx.beginPath(); ctx.rect(x0p, y0p, wp, hp); ctx.clip();
        // visible band 400–700 nm with a faint rainbow wash and a strong strip at the bottom
        const gx0 = X(400), gx1 = X(700);
        const grad = ctx.createLinearGradient(gx0, 0, gx1, 0);
        const stops = [[0, 275], [0.2, 235], [0.4, 150], [0.6, 60], [0.8, 30], [1, 0]];
        stops.forEach(([p, hue]) => grad.addColorStop(p, 'hsla(' + hue + ',85%,55%,0.18)'));
        ctx.fillStyle = grad; ctx.fillRect(gx0, y0p, gx1 - gx0, hp);
        const grad2 = ctx.createLinearGradient(gx0, 0, gx1, 0);
        stops.forEach(([p, hue]) => grad2.addColorStop(p, 'hsl(' + hue + ',85%,55%)'));
        ctx.fillStyle = grad2; ctx.fillRect(gx0, y0p + hp - 7, gx1 - gx0, 7);
        // the Sun for comparison when on the same scale
        if (st.same && st.T !== SUN_T) {
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]); ctx.beginPath();
          for (let i = 0; i <= 200; i++) {
            const nm = 20 + (3000 - 20) * i / 200;
            const y = planck(nm, SUN_T) / pkSun;
            if (i === 0) ctx.moveTo(X(nm), Y(y)); else ctx.lineTo(X(nm), Y(y));
          }
          ctx.stroke(); ctx.setLineDash([]);
        }
        // the star's curve
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.5; ctx.beginPath();
        for (let i = 0; i <= 300; i++) {
          const nm = 10 + (3000 - 10) * i / 300;
          const y = planck(nm, st.T) * scale;
          if (i === 0) ctx.moveTo(X(nm), Y(y)); else ctx.lineTo(X(nm), Y(y));
        }
        ctx.stroke();
        // λmax marker
        const lmax = WIEN / st.T * 1e9;
        const ym = planck(lmax, st.T) * scale;
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(X(lmax), Y(ym)); ctx.lineTo(X(lmax), Y(0)); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(lmax), Y(ym), 4.5, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
        // labels on a second row, inside the plot, away from the curve
        ctx.font = '12px ' + col.font; ctx.fillStyle = col.ink2; ctx.textBaseline = 'alphabetic';
        const tx = X(3000) - 8;
        ctx.textAlign = 'right';
        ctx.fillText('λmax = ' + W.fmt(lmax, 3) + ' nm', tx, y0p + 30);
        if (st.same && st.T !== SUN_T) ctx.fillText('dashed: the Sun', tx, y0p + 46);
        ctx.textAlign = 'left';
      }
    });

    // ---------- star disc ----------
    const disc = W.canvas(body, {
      height: 130,
      draw(ctx, w, h, col) {
        const cx = Math.min(100, w * 0.3), cy = h / 2;
        const rad = (s) => (14 + 78 * (Math.log10(s) + 2) / 5) / 2;     // radius in px from log radius
        const R = rad(st.r), Rs = rad(1);
        const [r, g, b] = bbColour(st.T);
        const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, R * 1.35);
        grad.addColorStop(0, 'rgb(' + r + ',' + g + ',' + b + ')');
        grad.addColorStop(0.74, 'rgb(' + r + ',' + g + ',' + b + ')');
        grad.addColorStop(1, 'rgba(' + r + ',' + g + ',' + b + ',0)');
        ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(cx, cy, R * 1.35, 0, 2 * Math.PI); ctx.fill();
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([4, 3]);
        ctx.beginPath(); ctx.arc(cx, cy, Rs, 0, 2 * Math.PI); ctx.stroke(); ctx.setLineDash([]);
        ctx.font = '12px ' + col.font; ctx.fillStyle = col.ink2; ctx.textBaseline = 'alphabetic';
        const tx = cx + Math.max(R, Rs) * 1.35 + 12;
        ctx.textAlign = 'left';
        const lines = ['Approximate colour', 'Dashed: size of the Sun', 'Size follows log r'];
        lines.forEach((t, i) => ctx.fillText(t, tx, cy - 14 + i * 18));
      }
    });

    // ---------- readout ----------
    const ro = W.readout([
      ['lmax', 'Peak wavelength λmax = b/T'],
      ['area', 'Power per unit area σT⁴'],
      ['L', 'Luminosity L = 4πσr²T⁴'],
      ['Ls', 'Luminosity in solar luminosities'],
      ['F', 'Radiant flux intensity F = L/(4πd²)']
    ]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);

    function update() {
      const L = lum(st);
      ro.set('lmax', W.fmt(WIEN / st.T * 1e9, 3) + ' nm');
      ro.set('area', sci(SIG * Math.pow(st.T, 4), 'W m⁻²'));
      ro.set('L', sci(L, 'W'));
      ro.set('Ls', sci(L / L_SUN, 'L☉'));
      if (st.useD) {
        const d = st.dly * LY;
        ro.set('F', sci(L / (4 * Math.PI * d * d), 'W m⁻²'));
      } else {
        ro.set('F', 'tick “Set a distance”');
      }
      note.textContent = 'Double the temperature: the peak moves to half the wavelength and the luminosity rises 16 times. ' +
        'Double the radius: the luminosity rises 4 times. Presets are approximate.';
      c.redraw(); disc.redraw();
    }
    syncTabs();
    update();
  });
})();
