/* phys-fringes: two-slit fringes and the diffraction grating (phys.superposition).
   data-mode="double|grating"
   double:  data-a="0.5" slit separation, mm, 0.1–1.0 · data-d="2.0" slit-to-screen distance D, m, 0.5–4
            data-lambda="600" wavelength, nm, 400–700
   grating: data-n="300" lines per mm, 100–1000 · data-lambda="589" · data-white="1" starts with white light
   Double slit: I = I0 cos²(π a y / λD) (idealised, very narrow slits, small angles); fringe separation x = λD/a.
   Grating: d sin θ = nλ with d = 1/N; the highest order is the largest n with nλ < d. */
(function () {
  'use strict';
  W.register('phys-fringes', function (el, opts) {
    const TAU = 2 * Math.PI;
    const notes = [];
    const get = (key, d, lo, hi, unit, whole) => {
      const raw = opts[key];
      if (raw === undefined || raw === '') return d;
      let x = parseFloat(raw);
      if (!isFinite(x)) { notes.push('data-' + key + ' "' + raw + '" is not a number, so ' + d + ' is used.'); return d; }
      if (whole) x = Math.round(x);
      const y = Math.min(hi, Math.max(lo, x));
      if (y !== x) {
        notes.push('data-' + key + ' = ' + raw + ' is outside the range ' + lo + '–' + hi + ' ' + unit + ', so ' + y + ' is used.' +
          (key === 'lambda' ? ' Visible light is 400–700 nm.' : ''));
      }
      return y;
    };
    let mode = 'double';
    if (opts.mode === 'grating') mode = 'grating';
    else if (opts.mode !== undefined && opts.mode !== '' && opts.mode !== 'double') notes.push('data-mode "' + opts.mode + '" is not recognised, so the double slit is shown.');
    const st = {
      a: get('a', 0.5, 0.1, 1.0, 'mm'),
      D: get('d', 2.0, 0.5, 4, 'm'),
      lam: get('lambda', mode === 'grating' ? 589 : 600, 400, 700, 'nm'),
      N: get('n', 300, 100, 1000, 'lines per mm', true),
      white: opts.white === '1' || opts.white === 'true'
    };
    const num = (v, d, lo, hi) => { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    if (notes.length) { err.textContent = notes.join(' '); err.style.display = ''; }

    // wavelength (nm) to an approximate screen colour
    function rgb(w) {
      let r = 0, g = 0, b = 0;
      if (w < 440) { r = -(w - 440) / 60; b = 1; }
      else if (w < 490) { g = (w - 440) / 50; b = 1; }
      else if (w < 510) { g = 1; b = -(w - 510) / 20; }
      else if (w < 580) { r = (w - 510) / 70; g = 1; }
      else if (w < 645) { r = 1; g = -(w - 645) / 65; }
      else { r = 1; }
      let f = 1;
      if (w < 420) f = 0.35 + 0.65 * (w - 380) / 40;
      else if (w > 700) f = 0.35 + 0.65 * (780 - w) / 80;
      const c = (v) => Math.round(255 * Math.pow(Math.max(0, v * f), 0.8));
      return [c(r), c(g), c(b)];
    }
    const css = (w, k) => { const c = rgb(w); return k === undefined ? 'rgb(' + c.join(',') + ')' : 'rgb(' + c.map((v) => Math.round(v * k)).join(',') + ')'; };
    const colourName = (w) => w < 450 ? 'violet' : w < 495 ? 'blue' : w < 570 ? 'green' : w < 590 ? 'yellow' : w < 620 ? 'orange' : 'red';

    const { body } = W.frame(el, mode === 'grating' ? 'Diffraction grating' : 'Young’s double slit',
      mode === 'grating' ? 'Change the lines per millimetre and the wavelength' : 'Change a, D and the wavelength and watch the fringes');

    if (mode === 'grating') buildGrating(); else buildDouble();

    // ======================================================================
    function buildDouble() {
      const WIN = 15;                                   // the screen window is -15 mm to +15 mm
      const xsep = () => st.lam * 1e-9 * st.D / (st.a * 1e-3) * 1e3;   // mm
      const sA = W.sliderNum({ label: 'Slit separation a / mm', min: 0.1, max: 1.0, step: 0.01, value: st.a, oninput: (v) => { st.a = num(v, 0.5, 0.1, 1); update(); } });
      const sD = W.sliderNum({ label: 'Slit-to-screen distance D / m', min: 0.5, max: 4, step: 0.1, value: st.D, oninput: (v) => { st.D = num(v, 2, 0.5, 4); update(); } });
      const sL = W.sliderNum({ label: 'Wavelength λ / nm', min: 400, max: 700, step: 1, value: st.lam, oninput: (v) => { st.lam = num(v, 600, 400, 700); update(); } });
      body.append(mk('div', { class: 'w-row' }, sA.el, sD.el, sL.el));

      const fine = (w, x) => (x / (2 * WIN)) * w < 5;     // fringe period under 5 px: cannot be drawn
      const cG = W.canvas(body, {
        height: 190,
        draw(ctx, w, h, col) {
          const x = xsep();
          const ax = W.axes(ctx, w, h, { x0: -WIN, x1: WIN, y0: 0, y1: 1.4 }, col,
            { pad: { l: 46, r: 14, t: 14, b: 34 }, xlabel: 'distance from the centre of the screen / mm', ylabel: 'I / I₀' });
          const { X, Y } = ax;
          ctx.save();
          ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
          ctx.strokeStyle = col.sc; ctx.lineWidth = 2.2; ctx.beginPath();
          if (fine(w - ax.pad.l - ax.pad.r, x)) {
            ctx.moveTo(X(-WIN), Y(0.5)); ctx.lineTo(X(WIN), Y(0.5));
          } else {
            const n = 3 * Math.round(w - ax.pad.l - ax.pad.r);
            for (let i = 0; i <= n; i++) {
              const y = -WIN + 2 * WIN * i / n, I = Math.pow(Math.cos(Math.PI * y / x), 2);
              if (i === 0) ctx.moveTo(X(y), Y(I)); else ctx.lineTo(X(y), Y(I));
            }
          }
          ctx.stroke();
          // fringe separation x between the central maximum and the next one
          if (x <= WIN) {
            const yy = Y(1.22);
            ctx.strokeStyle = col.ink; ctx.fillStyle = col.ink; ctx.lineWidth = 1.5;
            ctx.setLineDash([3, 3]); ctx.beginPath(); ctx.moveTo(X(0), Y(1)); ctx.lineTo(X(0), yy - 2); ctx.moveTo(X(x), Y(1)); ctx.lineTo(X(x), yy - 2); ctx.stroke(); ctx.setLineDash([]);
            const m = (X(0) + X(x)) / 2;
            arrow(ctx, m - 1, X(0), yy); arrow(ctx, m + 1, X(x), yy);
            if (X(x) - X(0) > 36) { ctx.font = '600 13px ' + col.font; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic'; ctx.fillText('x', m, yy - 5); }
          }
          ctx.restore();
        }
      });

      const cS = W.canvas(body, {
        height: 54,
        draw(ctx, w, h, col) {
          const pl = 46, pr = 14, pw = w - pl - pr, x = xsep();
          ctx.fillStyle = '#000'; ctx.fillRect(pl, 4, pw, h - 22);
          const flat = fine(pw, x);
          for (let i = 0; i < pw; i++) {
            const y = -WIN + 2 * WIN * (i + 0.5) / pw, I = flat ? 0.5 : Math.pow(Math.cos(Math.PI * y / x), 2);
            ctx.fillStyle = css(st.lam, I); ctx.fillRect(pl + i, 4, 1, h - 22);
          }
          ctx.fillStyle = col.ink2; ctx.font = '12px ' + col.font; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
          ctx.fillText('the pattern on the screen (' + colourName(st.lam) + ', ' + Math.round(st.lam) + ' nm)', pl, h - 3);
        }
      });

      const ro = W.readout([
        ['x', 'Fringe separation x = λD/a'], ['col', 'Colour of the light'], ['ten', 'Ten fringe spacings'], ['n', 'Bright fringes in the window']
      ]);
      const msg = mk('div', { class: 'w-note' });
      const note = mk('div', { class: 'w-note' }, 'Try: halve a and see x double; double D and see x double; change λ from red (700 nm) to violet (400 nm) and see the fringes close up. The graph is the idealised pattern for very narrow slits. In a real experiment you measure across ten spacings and divide.');
      body.append(ro.el, msg, note, err);

      function update() {
        const x = xsep();
        ro.set('x', W.fmt(x, 3) + ' mm  (= ' + W.fmt(st.lam, 3) + ' nm × ' + W.fmt(st.D, 3) + ' m ÷ ' + W.fmt(st.a, 3) + ' mm)');
        ro.set('col', colourName(st.lam) + ', ' + Math.round(st.lam) + ' nm');
        ro.set('ten', W.fmt(10 * x, 3) + ' mm');
        const nb = Math.floor(WIN / x) * 2 + 1;
        ro.set('n', x > 2 * WIN ? '1 (only the central fringe)' : String(nb));
        msg.textContent = x < 0.4 ? 'These fringes are less than 0.4 mm apart and are too close to draw on this scale (the graph shows the average level). Increase λ or D, or reduce a.' :
          x > WIN ? 'The fringe separation is bigger than the window shown (15 mm each side), so only the central fringe is in view.' :
            'Bright fringes are at 0, ±x, ±2x, … where the path difference a sin θ is a whole number of wavelengths; dark fringes are halfway between.';
        cG.redraw(); cS.redraw();
      }
      update();
    }

    // ======================================================================
    function buildGrating() {
      const sN = W.sliderNum({ label: 'Lines per millimetre N', min: 100, max: 1000, step: 10, value: st.N, oninput: (v) => { st.N = Math.round(num(v, 300, 100, 1000)); update(); } });
      const sL = W.sliderNum({ label: 'Wavelength λ / nm', min: 400, max: 700, step: 1, value: st.lam, oninput: (v) => { st.lam = num(v, 589, 400, 700); update(); } });
      const cb = mk('input', { type: 'checkbox', 'aria-label': 'White light (400 to 700 nm)' });
      cb.checked = st.white;
      cb.onchange = () => { st.white = cb.checked; update(); };
      const cbLab = mk('label', { class: 'w-ctl', style: { flexDirection: 'row', alignItems: 'center', gap: '8px' } }, cb, mk('span', { class: 'w-lab' }, 'White light (400–700 nm)'));
      body.append(mk('div', { class: 'w-row' }, sN.el, sL.el, cbLab));

      const dnm = () => 1e6 / st.N;                        // slit spacing in nm
      const nmax = (lam) => { const r = dnm() / lam; const n = Math.floor(r); return Math.abs(r - n) < 1e-9 ? n - 1 : n; };
      const thetaOf = (n, lam) => Math.asin(Math.min(1, n * lam / dnm()));

      const c = W.canvas(body, {
        height: 300,
        draw(ctx, w, h, col) {
          const cx = 56, cy = h / 2;
          const R = Math.max(60, Math.min(w - cx - 66, h / 2 - 28));
          ctx.textBaseline = 'alphabetic';
          // screen (a semicircle round the grating)
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]);
          ctx.beginPath(); ctx.arc(cx, cy, R, -Math.PI / 2, Math.PI / 2); ctx.stroke(); ctx.setLineDash([]);
          // incoming beam, grating
          ctx.strokeStyle = col.ink2; ctx.fillStyle = col.ink2; ctx.lineWidth = 2;
          arrow(ctx, 8, cx - 5, cy);
          ctx.strokeStyle = col.ink; ctx.lineWidth = 5;
          ctx.beginPath(); ctx.moveTo(cx, cy - 34); ctx.lineTo(cx, cy + 34); ctx.stroke();
          ctx.fillStyle = col.ink2; ctx.font = '12px ' + col.font; ctx.textAlign = 'center';
          ctx.fillText('grating', cx, cy - 40);
          ctx.fillText('screen', cx + R * 0.7, cy - R * 0.72 - 6);
          const at = (th, r) => [cx + r * Math.cos(th), cy - r * Math.sin(th)];
          const lbl = (txt, th, r) => {
            const p = at(th, r + 8);
            ctx.font = '600 12px ' + col.font; ctx.fillStyle = col.ink; ctx.textAlign = 'left';
            ctx.fillText(txt, Math.min(w - 40, p[0]), p[1] + (th > 0.02 ? -2 : th < -0.02 ? 12 : 4));
          };
          if (st.white) {
            // zero order is white
            ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + R, cy); ctx.stroke();
            ctx.fillStyle = col.card; ctx.strokeStyle = col.ink; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.arc(cx + R, cy, 6, 0, TAU); ctx.fill(); ctx.stroke();
            lbl('n = 0', 0, R + 4);
            const top = Math.min(6, nmax(400));
            for (let k = 1; k <= top; k++) {
              const rr = R - 11 * ((k - 1) % 3) ;
              for (const sgn of [1, -1]) {
                ctx.lineWidth = 9; ctx.lineCap = 'butt';
                for (let wl = 400; wl < 700; wl += 5) {
                  if (k * wl >= dnm()) break;
                  const t1 = thetaOf(k, wl), t2 = thetaOf(k, Math.min(700, wl + 5));
                  ctx.strokeStyle = css(wl);
                  ctx.beginPath(); ctx.arc(cx, cy, rr, -sgn * t2, -sgn * t1, sgn < 0); ctx.stroke();
                }
              }
              if (k <= 3 && k * 400 < dnm()) lbl('n = ' + k, thetaOf(k, 700) * 0.5 + thetaOf(k, 400) * 0.5, R);
            }
          } else {
            const nm = nmax(st.lam);
            ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.2;
            ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + R, cy); ctx.stroke();
            for (let n = 1; n <= nm; n++) {
              const th = thetaOf(n, st.lam);
              for (const sgn of [1, -1]) {
                const p = at(sgn * th, R);
                ctx.strokeStyle = col.ink2; ctx.lineWidth = 1.2;
                ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(p[0], p[1]); ctx.stroke();
              }
            }
            for (let n = 0; n <= nm; n++) {
              const th = thetaOf(n, st.lam);
              for (const sgn of (n === 0 ? [1] : [1, -1])) {
                const p = at(sgn * th, R);
                ctx.fillStyle = css(st.lam); ctx.strokeStyle = col.ink; ctx.lineWidth = 1.5;
                ctx.beginPath(); ctx.arc(p[0], p[1], 6, 0, TAU); ctx.fill(); ctx.stroke();
              }
              if (n === 0) lbl('n = 0', 0, R + 4);
              else if (nm <= 6 || n <= 3 || n === nm) { lbl('n = ' + n, thetaOf(n, st.lam), R); lbl('n = −' + n, -thetaOf(n, st.lam), R); }
            }
          }
        }
      });

      const ro = W.readout([
        ['d', 'Slit spacing d = 1/N'], ['nm', 'Highest order n (nλ < d)'], ['tot', 'Number of maxima, 2n + 1'], ['ang', 'Angles θ of the orders']
      ]);
      const msg = mk('div', { class: 'w-note' });
      const note = mk('div', { class: 'w-note' }, 'Try: increase the lines per millimetre and watch the orders spread out and the highest order fall. Then switch on white light: the first spectrum is separate from the second, but the second and third overlap.');
      body.append(ro.el, msg, note, err);

      function update() {
        const d = dnm();
        ro.set('d', W.fmt(d / 1000, 3) + ' µm = 1 / (' + st.N + ' × 10³ m⁻¹)');
        if (st.white) {
          ro.set('nm', 'orders appear while nλ < d, so up to n = ' + nmax(400) + ' for violet (400 nm) and ' + nmax(700) + ' for red (700 nm)');
          ro.set('tot', 'depends on the colour (white light has all 400–700 nm)');
          const parts = [];
          for (let k = 1; k <= Math.min(3, nmax(400)); k++) parts.push(k + ': ' + W.fmt(thetaOf(k, 400) * 180 / Math.PI, 3) + '° to ' + W.fmt(thetaOf(k, 700) * 180 / Math.PI, 3) + '°');
          ro.set('ang', parts.join(' · ') + ' (violet to red)');
          let s = '';
          for (let k = 1; k < 5; k++) {
            if ((k + 1) * 400 < d && (k + 1) * 400 < k * 700) {
              const lo = W.fmt(thetaOf(k + 1, 400) * 180 / Math.PI, 3), hi = W.fmt(thetaOf(k, 700) * 180 / Math.PI, 3);
              s = 'Orders ' + k + ' and ' + (k + 1) + ' overlap between ' + lo + '° and ' + hi + '°: the violet end of order ' + (k + 1) + ' comes before the red end of order ' + k + '.';
              break;
            }
          }
          if (!s) s = d < 800 ? 'This grating is so fine that only the first spectrum (and maybe part of the second) appears, so no orders overlap.' : 'No two orders overlap for this grating.';
          msg.textContent = s;
        } else {
          const nm = nmax(st.lam);
          ro.set('d', W.fmt(d / 1000, 3) + ' µm = 1 / (' + st.N + ' × 10³ m⁻¹)');
          ro.set('nm', nm + '  (d/λ = ' + W.fmt(d / st.lam, 3) + ', rounded down)');
          ro.set('tot', String(2 * nm + 1) + ' (' + nm + ' each side and the central maximum)');
          const parts = [];
          for (let k = 1; k <= Math.min(5, nm); k++) parts.push(k + ': ' + W.fmt(thetaOf(k, st.lam) * 180 / Math.PI, 3) + '°');
          ro.set('ang', nm ? parts.join(' · ') + (nm > 5 ? ' …' : '') : 'only the central maximum');
          msg.textContent = 'd sin θ = nλ: for order ' + (nm || 1) + ', sin θ = ' + W.fmt((nm || 1) * st.lam / d, 3) + '. The next order would need sin θ = ' + W.fmt((nm + 1) * st.lam / d, 3) + ', which is more than 1, so it cannot exist.';
        }
        c.redraw();
      }
      update();
    }

    // ----- helpers -----
    function mk(tag, props, ...kids) { return W.h(tag, props, ...kids); }
    function arrow(ctx, x1, x2, y) {
      const dir = x2 > x1 ? 1 : -1;
      ctx.beginPath(); ctx.moveTo(x1, y); ctx.lineTo(x2, y); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x2, y); ctx.lineTo(x2 - dir * 7, y - 4); ctx.lineTo(x2 - dir * 7, y + 4); ctx.closePath(); ctx.fill();
    }
  });
})();
