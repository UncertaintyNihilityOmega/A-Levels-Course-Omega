/* phys-photo: the photoelectric effect (phys.quantum).
   data-metal="sodium"  caesium | potassium | sodium | calcium | zinc | copper (approximate work functions)
   data-lambda="400"    wavelength of the light in nm, 100–800
   data-i="60"          intensity in % of the maximum, 0–100
   Model: photon energy hf = hc/λ (h = 6.63e-34 J s, c = 3.00e8 m/s); KEmax = hf − Φ when positive, else no emission;
   vmax = sqrt(2 KEmax/m_e); the photoelectric current is proportional to the intensity above the threshold, zero below. */
(function () {
  'use strict';
  const H = 6.63e-34, C = 3.00e8, E = 1.60e-19, ME = 9.11e-31;
  const METALS = {
    caesium: { name: 'Caesium', phi: 2.1 },
    potassium: { name: 'Potassium', phi: 2.3 },
    sodium: { name: 'Sodium', phi: 2.3 },
    calcium: { name: 'Calcium', phi: 2.9 },
    zinc: { name: 'Zinc', phi: 4.3 },
    copper: { name: 'Copper', phi: 4.7 }
  };
  const KEYS = Object.keys(METALS);
  const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  const sup = (e) => String(e).split('').map((ch) => SUP[ch] || ch).join('');
  function sci(x, sf) {
    if (!isFinite(x) || x === 0) return '0';
    let e = Math.floor(Math.log10(Math.abs(x)));
    let m = x / Math.pow(10, e);
    if (parseFloat(m.toPrecision(sf)) >= 10) { m /= 10; e += 1; }
    return m.toPrecision(sf) + ' × 10' + sup(e);
  }
  function colourName(l) {
    if (l < 380) return 'ultraviolet';
    if (l > 750) return 'infrared';
    if (l < 450) return 'violet';
    if (l < 495) return 'blue';
    if (l < 570) return 'green';
    if (l < 590) return 'yellow';
    if (l < 620) return 'orange';
    return 'red';
  }
  function isDarkBg(c) {
    // luminance of the card colour (hex or rgb()); dark mode needs lighter beam colours
    const s = String(c || '').trim();
    let r = 255, g = 255, b = 255, m;
    if ((m = s.match(/^#([0-9a-f]{6})$/i))) { const n = parseInt(m[1], 16); r = n >> 16; g = (n >> 8) & 255; b = n & 255; }
    else if ((m = s.match(/^#([0-9a-f]{3})$/i))) { r = parseInt(m[1][0] + m[1][0], 16); g = parseInt(m[1][1] + m[1][1], 16); b = parseInt(m[1][2] + m[1][2], 16); }
    else if ((m = s.match(/rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)/))) { r = +m[1]; g = +m[2]; b = +m[3]; }
    return 0.299 * r + 0.587 * g + 0.114 * b < 128;
  }
  function beamColour(l, fallback, dark) {
    if (l < 380 || l > 750) return fallback;
    const hue = l < 400 ? 275 : Math.max(0, 270 - (Math.min(l, 700) - 400) / 300 * 270);
    const light = dark ? (l < 460 || l > 640 ? 70 : 60) : (l > 700 ? 40 : 48);
    return 'hsl(' + Math.round(hue) + ', 85%, ' + light + '%)';
  }

  W.register('phys-photo', function (el, opts) {
    const { body } = W.frame(el, 'The photoelectric effect', 'Choose a metal, then change the wavelength and the intensity');
    const msgs = [];
    function num(raw, d, lo, hi, name, unit) {
      if (raw === undefined || raw === null || String(raw).trim() === '') return d;
      const x = parseFloat(raw);
      if (!isFinite(x)) { msgs.push(name + ' = "' + raw + '" is not a number, so ' + d + unit + ' is used.'); return d; }
      if (x < lo) { msgs.push(name + ' = ' + x + ' is below the range ' + lo + '–' + hi + unit + ', so ' + lo + unit + ' is used.'); return lo; }
      if (x > hi) { msgs.push(name + ' = ' + x + ' is above the range ' + lo + '–' + hi + unit + ', so ' + hi + unit + ' is used.'); return hi; }
      return x;
    }
    const mk = String(opts.metal || 'sodium').toLowerCase();
    if (opts.metal && !METALS[mk]) msgs.push('Metal "' + opts.metal + '" is not known (use ' + KEYS.join(', ') + '), so sodium is used.');
    const st = {
      metal: METALS[mk] ? mk : 'sodium',
      lam: num(opts.lambda, 400, 100, 800, 'Wavelength', ' nm'),
      i: num(opts.i, 60, 0, 100, 'Intensity', ' %')
    };
    const reduced = W.reducedMotion();

    // ---- physics ---------------------------------------------------------------
    function phys(s) {
      const phiJ = METALS[s.metal || st.metal].phi * E;
      const f = C / (s.lam * 1e-9);
      const eph = H * f;
      const ke = Math.max(0, eph - phiJ);
      return { phiJ, f, eph, ke, f0: phiJ / H, lam0: H * C / phiJ * 1e9, v: Math.sqrt(2 * ke / ME) };
    }

    // ---- controls ----------------------------------------------------------------
    const err = W.h('div', { class: 'w-err', style: { display: msgs.length ? '' : 'none' } });
    err.textContent = msgs.join(' ');
    const sel = W.h('select', { 'aria-label': 'Metal' });
    KEYS.forEach((k) => sel.append(W.h('option', { value: k }, METALS[k].name + ' (Φ = ' + METALS[k].phi + ' eV)')));
    sel.value = st.metal;
    sel.addEventListener('change', () => { st.metal = sel.value; update(); });
    const selEl = W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab' }, 'Metal (approximate work function)'), sel);
    const sL = W.sliderNum({ label: 'Wavelength λ / nm', min: 100, max: 800, step: 1, value: st.lam, oninput: (v) => {
      const x = parseFloat(v); if (!isFinite(x)) return;
      st.lam = Math.min(800, Math.max(100, x)); update();
    } });
    const sI = W.slider({ label: 'Intensity', min: 0, max: 100, step: 1, value: st.i, fmt: (v) => v + ' %', oninput: (v) => {
      const x = parseFloat(v); if (!isFinite(x)) return;
      st.i = Math.min(100, Math.max(0, x)); update();
    } });
    // the photons and electrons move all the time, so the reader can pause them (never started under reduced motion)
    const pauseBtn = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', onclick: () => togglePause() }, 'Pause the animation');
    body.append(W.h('div', { class: 'w-row' }, selEl, reduced ? null : pauseBtn), W.h('div', { class: 'w-row' }, sL.el, sI.el));

    // ---- scene canvas -----------------------------------------------------------
    const rng = W.rng(5);
    const geo = { tx: 12, ty: 40, tw: 300, th: 140, px: 80, cx: 260, w: 340 };
    let photons = [], electrons = [], flashes = [];
    let acc = 0;
    const KEREF = 10.5;                      // eV: speed scale for drawing
    function spawnPhoton() {
      if (photons.length > 60) return;
      const yT = geo.ty + 16 + rng() * (geo.th - 32);
      const sx = geo.px + 50 + rng() * Math.max(40, geo.tw * 0.45);
      const sy = geo.ty - 10;
      const tx = geo.px + 6;
      const dx = tx - sx, dy = yT - sy, d = Math.hypot(dx, dy);
      const speed = 210;
      photons.push({ x: sx, y: sy, vx: dx / d * speed, vy: dy / d * speed, left: d / speed, hx: tx, hy: yT });
    }
    function step(dt) {
      const p = phys(st);
      const rate = st.i > 0 ? 0.3 + 14 * st.i / 100 : 0;
      acc += dt * rate;
      while (acc >= 1) { acc -= 1; spawnPhoton(); }
      for (const ph of photons) {
        ph.x += ph.vx * dt; ph.y += ph.vy * dt; ph.left -= dt;
        if (ph.left <= 0) {
          ph.dead = true;
          if (p.ke > 0) {
            if (electrons.length < 90) {
              const keEv = p.ke / E * (0.3 + 0.7 * rng());
              const sp = 70 + 190 * Math.sqrt(keEv / KEREF);
              const ang = (rng() - 0.5) * 0.7;
              electrons.push({ x: ph.hx + 2, y: ph.hy, vx: sp * Math.cos(ang), vy: sp * Math.sin(ang) });
            }
          } else flashes.push({ x: ph.hx, y: ph.hy, life: 1 });
        }
      }
      photons = photons.filter((q) => !q.dead);
      for (const e of electrons) {
        e.x += e.vx * dt; e.y += e.vy * dt;
        if (e.x > geo.cx - 3 || e.y < geo.ty + 3 || e.y > geo.ty + geo.th - 3) e.dead = true;
      }
      electrons = electrons.filter((q) => !q.dead);
      for (const f of flashes) f.life -= dt / 0.4;
      flashes = flashes.filter((f) => f.life > 0);
    }

    function squiggle(ctx, x, y, dx, dy, len) {
      const nx = -dy, ny = dx;
      ctx.beginPath();
      for (let k = 0; k <= 12; k++) {
        const t = k / 12 * len, w = Math.sin(k / 12 * Math.PI * 3) * 2.6;
        const qx = x - dx * t + nx * w, qy = y - dy * t + ny * w;
        if (k === 0) ctx.moveTo(qx, qy); else ctx.lineTo(qx, qy);
      }
      ctx.stroke();
    }
    function arrow(ctx, x0, y0, x1, y1) {
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
      const a = Math.atan2(y1 - y0, x1 - x0);
      ctx.beginPath(); ctx.moveTo(x1, y1);
      ctx.lineTo(x1 - 8 * Math.cos(a - 0.4), y1 - 8 * Math.sin(a - 0.4));
      ctx.lineTo(x1 - 8 * Math.cos(a + 0.4), y1 - 8 * Math.sin(a + 0.4));
      ctx.closePath(); ctx.fill();
    }
    function label(ctx, col, txt, x, y, align, color) {
      ctx.font = '600 12px ' + col.font;
      ctx.fillStyle = color || col.ink2; ctx.textAlign = align || 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText(txt, x, y);
    }

    const scene = W.canvas(body, {
      height: 200,
      label: 'Light shining on a metal emitter in a vacuum tube',
      describe: () => {
        const p = phys(st), name = st.lam < 380 ? 'ultraviolet' : st.lam > 750 ? 'infrared' : colourName(st.lam);
        return 'Photons of ' + name + ' light, ' + Math.round(st.lam) + ' nm, at ' + Math.round(st.i) + ' % intensity hit the ' + METALS[st.metal].name.toLowerCase() + ' emitter. ' +
          (st.i <= 0 ? 'The light is off, so nothing is emitted.' : p.ke > 0 ? 'Each photon has ' + W.fmt(p.eph / E, 3) + ' eV, more than the work function ' + METALS[st.metal].phi + ' eV, so electrons are emitted towards the collector.' : 'Each photon has ' + W.fmt(p.eph / E, 3) + ' eV, less than the work function ' + METALS[st.metal].phi + ' eV, so no electrons are emitted.');
      },
      draw(ctx, w, h, col) {
        const p = phys(st);
        const tx = 12, ty = 38, tw = w - 24, th = h - 62;
        geo.tx = tx; geo.ty = ty; geo.tw = tw; geo.th = th; geo.w = w;
        geo.px = tx + tw * 0.22; geo.cx = tx + tw * 0.82;
        const beam = beamColour(st.lam, col.ink2, isDarkBg(col.card));
        const visible = st.lam >= 380 && st.lam <= 750;
        // light label
        const name = colourName(st.lam);
        label(ctx, col, 'Light: ' + Math.round(st.lam) + ' nm' + (visible ? ' (' + name + ')' : ' (' + (st.lam < 380 ? 'UV' : 'IR') + ')'), tx + 2, 16, 'left', visible ? beam : col.ink2);
        // tube
        ctx.fillStyle = col.card; ctx.strokeStyle = col.rule2; ctx.lineWidth = 2;
        ctx.beginPath();
        const r = 16;
        ctx.moveTo(tx + r, ty); ctx.lineTo(tx + tw - r, ty); ctx.quadraticCurveTo(tx + tw, ty, tx + tw, ty + r);
        ctx.lineTo(tx + tw, ty + th - r); ctx.quadraticCurveTo(tx + tw, ty + th, tx + tw - r, ty + th);
        ctx.lineTo(tx + r, ty + th); ctx.quadraticCurveTo(tx, ty + th, tx, ty + th - r);
        ctx.lineTo(tx, ty + r); ctx.quadraticCurveTo(tx, ty, tx + r, ty); ctx.closePath();
        ctx.fill(); ctx.stroke();
        // plates
        ctx.fillStyle = col.ink2;
        ctx.fillRect(geo.px - 4, ty + 14, 8, th - 28);
        ctx.fillRect(geo.cx - 2, ty + 14, 5, th - 28);
        label(ctx, col, 'emitter', geo.px, h - 8, 'center', col.ink2);
        label(ctx, col, 'collector', geo.cx, h - 8, 'center', col.ink2);
        ctx.save();
        ctx.beginPath(); ctx.rect(tx + 1, ty + 1, tw - 2, th - 2); ctx.clip();
        if (reduced) {
          // static picture: photons arriving and, above threshold, electrons leaving
          ctx.lineWidth = 2.2;
          if (st.i > 0) {
            ctx.strokeStyle = beam; ctx.fillStyle = beam;
            [0.28, 0.5, 0.72].forEach((q) => {
              const yT = ty + th * q;
              arrow(ctx, geo.px + 6 + 90, ty - 2, geo.px + 8, yT);
            });
            if (p.ke > 0) {
              ctx.strokeStyle = col.sc; ctx.fillStyle = col.sc;
              [0.28, 0.5, 0.72].forEach((q) => arrow(ctx, geo.px + 12, ty + th * q, geo.px + 12 + 70 + 110 * Math.sqrt(p.ke / E / KEREF), ty + th * q));
            }
          }
        } else {
          ctx.strokeStyle = beam; ctx.lineWidth = 2;
          for (const ph of photons) {
            const d = Math.hypot(ph.vx, ph.vy);
            squiggle(ctx, ph.x, ph.y, ph.vx / d, ph.vy / d, 18);
          }
          ctx.fillStyle = col.sc;
          for (const e of electrons) { ctx.beginPath(); ctx.arc(e.x, e.y, 3.4, 0, 2 * Math.PI); ctx.fill(); }
          for (const f of flashes) {
            ctx.globalAlpha = Math.max(0, f.life); ctx.strokeStyle = col.red; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.moveTo(f.x + 2, f.y - 5); ctx.lineTo(f.x + 12, f.y + 5); ctx.moveTo(f.x + 12, f.y - 5); ctx.lineTo(f.x + 2, f.y + 5); ctx.stroke();
            ctx.globalAlpha = 1;
          }
        }
        ctx.restore();
        label(ctx, col, p.ke > 0 ? 'electrons are emitted' : (st.i > 0 ? 'no electrons: photon energy < Φ' : 'light is off'), tx + tw / 2, ty + th - 8, 'center', p.ke > 0 ? col.sc : col.red);
      }
    });

    // ---- graph canvas -----------------------------------------------------------
    const gradEv = H * 1e14 / E;             // slope of KEmax against f in eV per 10^14 Hz
    function view(p) {
      const f14 = p.f / 1e14;
      // both threshold points sit in the left two thirds, so neither line runs through the x-axis label
      const other = st.metal === 'zinc' ? 'caesium' : 'zinc';
      const fMax = Math.max(METALS[st.metal].phi, METALS[other].phi) / gradEv;
      const x1 = Math.max(14, Math.ceil(fMax * 1.5), Math.ceil(f14 * 1.12));
      const top = Math.max(1.2, (gradEv * x1 - METALS[st.metal].phi) * 1.06);
      return { x0: 0, x1, y0: 0, y1: top };
    }
    const graph = W.canvas(body, {
      height: 230,
      label: 'Graph of maximum kinetic energy against frequency',
      describe: () => {
        const p = phys(st), phi = METALS[st.metal].phi, keEv = p.ke / E;
        return 'KEmax in electronvolts against frequency in units of 10¹⁴ hertz: a straight line of gradient h starting at the threshold frequency ' + W.fmt(phi / gradEv, 3) + ' × 10¹⁴ Hz for ' + METALS[st.metal].name.toLowerCase() +
          ', with a dashed parallel line for another metal. The marked point is at ' + W.fmt(p.f / 1e14, 3) + ' × 10¹⁴ Hz, ' + (keEv > 0 ? 'where KEmax is ' + W.fmt(keEv, 3) + ' eV.' : 'below the threshold, so there is no emission.');
      },
      draw(ctx, w, h, col) {
        const p = phys(st);
        const vw = view(p);
        const ax = W.axes(ctx, w, h, vw, col, { pad: { l: 46, r: 14, t: 22, b: 36 }, xlabel: 'f / 10¹⁴ Hz', ylabel: 'KEmax / eV' });
        const { X, Y } = ax;
        const phi = METALS[st.metal].phi;
        const other = st.metal === 'zinc' ? 'caesium' : 'zinc';
        const f0 = phi / gradEv, f0o = METALS[other].phi / gradEv;
        ctx.save();
        ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
        // faint comparison line
        ctx.globalAlpha = 0.55; ctx.strokeStyle = col.ink3; ctx.lineWidth = 1.6; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(X(f0o), Y(0)); ctx.lineTo(X(vw.x1), Y(gradEv * vw.x1 - METALS[other].phi)); ctx.stroke();
        ctx.setLineDash([]); ctx.globalAlpha = 1;
        // chosen metal
        ctx.strokeStyle = col.sc; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(X(f0), Y(0)); ctx.lineTo(X(vw.x1), Y(gradEv * vw.x1 - phi)); ctx.stroke();
        // current frequency
        const f14 = p.f / 1e14, keEv = p.ke / E;
        ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(X(f14), Y(0)); ctx.lineTo(X(f14), Y(vw.y1)); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = col.red; ctx.strokeStyle = col.red; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(X(f14), Y(keEv), 5, 0, 2 * Math.PI);
        if (keEv > 0) ctx.fill(); else { ctx.fillStyle = col.card; ctx.fill(); ctx.stroke(); }
        // threshold marker
        ctx.fillStyle = col.sc;
        ctx.beginPath(); ctx.moveTo(X(f0), Y(0) - 7); ctx.lineTo(X(f0) + 5, Y(0)); ctx.lineTo(X(f0) - 5, Y(0)); ctx.closePath(); ctx.fill();
        ctx.restore();
        // legend on rows below the y label
        label(ctx, col, 'solid: ' + METALS[st.metal].name + ', f₀ = ' + W.fmt(f0, 3) + ' × 10¹⁴ Hz', ax.pad.l + 8, ax.pad.t + 30, 'left', col.sc);
        label(ctx, col, 'dashed: ' + METALS[other].name + ' (same gradient)', ax.pad.l + 8, ax.pad.t + 46, 'left', col.ink3);
        if (keEv <= 0) label(ctx, col, 'below threshold: no emission', ax.pad.l + 8, ax.pad.t + 62, 'left', col.red);
      }
    });

    // ---- readout ------------------------------------------------------------------
    const ro = W.readout([
      ['e', 'Photon energy hf'], ['f', 'Frequency f'], ['t', 'Threshold of this metal'],
      ['ke', 'Maximum kinetic energy'], ['v', 'Maximum speed'], ['cur', 'Photoelectric current']
    ]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);

    function update() {
      const p = phys(st);
      ro.set('e', sci(p.eph, 3) + ' J = ' + W.fmt(p.eph / E, 3) + ' eV');
      ro.set('f', sci(p.f, 3) + ' Hz');
      ro.set('t', 'f₀ = ' + sci(p.f0, 3) + ' Hz, λ₀ = ' + W.fmt(p.lam0, 3) + ' nm');
      if (p.ke > 0) {
        ro.set('ke', W.fmt(p.ke / E, 3) + ' eV = ' + sci(p.ke, 3) + ' J');
        ro.set('v', sci(p.v, 3) + ' m s⁻¹');
        ro.set('cur', st.i > 0 ? W.fmt(st.i, 3) + ' % of the maximum (proportional to intensity)' : 'zero: the light is off');
      } else {
        ro.set('ke', 'none: hf < Φ');
        ro.set('v', 'no photoelectrons');
        ro.set('cur', 'zero, however intense the light');
      }
      note.textContent = p.ke > 0
        ? 'Above the threshold, KEmax = hf − Φ depends only on the frequency. Raise the intensity: more photons arrive each second, so the current rises, but the electrons are no faster. Now lengthen the wavelength past λ₀.'
        : 'Below the threshold, each photon has less energy than the work function, so no electron escapes, however many photons arrive. Raise the intensity to check, then shorten the wavelength below λ₀.';
      scene.redraw(); graph.redraw();
    }
    update();

    let last = performance.now();
    const anim = W.animate(() => {
      const now = performance.now();
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      if (dt <= 0) return true;
      step(dt);
      scene.redraw();
      return true;
    }, { still: () => scene.redraw() });
    last = performance.now();
    anim.start();
    function togglePause() {
      if (anim.running) { anim.stop(); pauseBtn.textContent = 'Resume the animation'; }
      else { last = performance.now(); anim.start(); pauseBtn.textContent = 'Pause the animation'; }
    }
  });
})();
