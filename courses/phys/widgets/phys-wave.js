/* phys-wave: a progressive wave (phys.waves) or a stationary wave on a string (phys.superposition).
   data-mode="progressive|stationary"  data-view="transverse|longitudinal" (progressive only)
   data-a="2" amplitude, cm, 0.5–5   data-lambda="4" wavelength, m, 0.5–10   data-f="0.5" frequency, Hz, 0.1–2
   data-n="3" harmonic of the stationary wave, 1–6 (the string is 2.00 m long).
   Progressive: y = A sin(2π(x/λ − f t)), moving right; P and Q are points on the wave (drag them or use the sliders).
   Stationary: sum of two travelling waves of amplitude A/2: y = A sin(kx) cos(ωt), drawn in slow motion. */
(function () {
  'use strict';
  W.register('phys-wave', function (el, opts) {
    const notes = [];
    const clampNote = (key, d, lo, hi, whole) => {
      const raw = opts[key];
      if (raw === undefined || raw === '') return d;
      let x = parseFloat(raw);
      if (!isFinite(x)) { notes.push('data-' + key + ' "' + raw + '" is not a number, so ' + d + ' is used.'); return d; }
      if (whole) x = Math.round(x);
      const y = Math.min(hi, Math.max(lo, x));
      if (y !== x) notes.push('data-' + key + ' = ' + raw + ' is outside ' + lo + '–' + hi + ', so ' + y + ' is used.');
      return y;
    };
    let mode = 'progressive';
    if (opts.mode === 'stationary') mode = 'stationary';
    else if (opts.mode !== undefined && opts.mode !== '' && opts.mode !== 'progressive') notes.push('data-mode "' + opts.mode + '" is not recognised, so the progressive wave is shown.');
    const stationary = mode === 'stationary';
    const st = {
      a: clampNote('a', 2, 0.5, 5),
      lam: clampNote('lambda', 4, 0.5, 10),
      f: clampNote('f', 0.5, 0.1, 2),
      n: clampNote('n', 3, 1, 6, true),
      view: opts.view === 'longitudinal' ? 'longitudinal' : 'transverse',
      xp: 1.0, xq: 2.5,
      comps: true
    };
    const TAU = 2 * Math.PI;
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    if (notes.length) { err.textContent = notes.join(' '); err.style.display = ''; }

    const { body } = W.frame(el, stationary ? 'Stationary wave on a string' : 'A progressive wave',
      stationary ? 'Two travelling waves add to give nodes and antinodes' : 'Watch the wave move and compare two points on it');

    const mk = (tag, props, ...kids) => W.h(tag, props, ...kids);
    function tabs(items, get, set, label) {
      const row = mk('div', { class: 'w-tabs', role: 'group', 'aria-label': label });
      const btns = items.map(([v, text]) => mk('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); } }, text));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    // text with a card-coloured backing so labels stay readable over lines
    function label(ctx, col, txt, x, y, align, color) {
      ctx.font = '600 13px ' + col.font;
      const w = ctx.measureText(txt).width;
      const x0 = align === 'center' ? x - w / 2 : align === 'right' ? x - w : x;
      ctx.fillStyle = col.card; ctx.globalAlpha = 0.85;
      ctx.fillRect(x0 - 3, y - 12, w + 6, 16); ctx.globalAlpha = 1;
      ctx.fillStyle = color || col.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText(txt, x0, y);
    }
    function arrowH(ctx, x1, x2, y) {
      const dir = x2 > x1 ? 1 : -1;
      ctx.beginPath(); ctx.moveTo(x1, y); ctx.lineTo(x2, y); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x2, y); ctx.lineTo(x2 - dir * 7, y - 4); ctx.lineTo(x2 - dir * 7, y + 4); ctx.closePath(); ctx.fill();
    }

    // clock shared by both modes: t in seconds, advanced by the animation or by the Step button
    let t = 0, last = 0, playing = false;
    let redrawAll = () => {};
    let stepSize = () => 0.25;
    const anim = W.animate(() => {
      const now = performance.now();
      const dt = Math.min(0.1, (now - last) / 1000);
      last = now; t += dt; redrawAll();
      return true;
    }, { still: () => {} });
    const playBtn = mk('button', { class: 'btn btn-sm', type: 'button', onclick: () => toggle() }, 'Pause');
    const stepBtn = mk('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => step() }, 'Step (T/8)');
    function setPlaying(on) {
      if (on && !playing) { last = performance.now(); anim.start(); }
      if (!on && playing) anim.stop();
      playing = on;
      playBtn.textContent = on ? 'Pause' : 'Play';
    }
    function toggle() { if (W.reducedMotion()) { step(); return; } setPlaying(!playing); }
    function step() { setPlaying(false); t += stepSize(); redrawAll(); }
    const reduced = W.reducedMotion();
    if (reduced) playBtn.style.display = 'none';

    if (stationary) buildStationary(); else buildProgressive();

    // ======================================================================
    function buildProgressive() {
      const XMAX = 10, YM = 6.5;
      stepSize = () => 1 / (8 * st.f);
      const yAt = (x, tt) => st.a * Math.sin(TAU * (x / st.lam - st.f * tt));
      const geo = { pl: 46, pr: 14, w: 300, X: null, Y: null };

      const viewTabs = tabs([['transverse', 'Transverse'], ['longitudinal', 'Longitudinal']], () => st.view,
        (v) => { st.view = v; showView(); redrawAll(); }, 'Type of wave');
      const sA = W.sliderNum({ label: 'Amplitude A / cm', min: 0.5, max: 5, step: 0.1, value: st.a, oninput: (v) => { st.a = clampv(v, 2, 0.5, 5); redrawAll(); } });
      const sL = W.sliderNum({ label: 'Wavelength λ / m', min: 0.5, max: 10, step: 0.1, value: st.lam, oninput: (v) => { st.lam = clampv(v, 4, 0.5, 10); redrawAll(); } });
      const sF = W.sliderNum({ label: 'Frequency f / Hz', min: 0.1, max: 2, step: 0.05, value: st.f, oninput: (v) => { st.f = clampv(v, 0.5, 0.1, 2); redrawAll(); } });
      const sP = W.sliderNum({ label: 'Point P at x / m', min: 0, max: XMAX, step: 0.05, value: st.xp, oninput: (v) => { st.xp = clampv(v, 1, 0, XMAX); redrawAll(); } });
      const sQ = W.sliderNum({ label: 'Point Q at x / m', min: 0, max: XMAX, step: 0.05, value: st.xq, oninput: (v) => { st.xq = clampv(v, 2.5, 0, XMAX); redrawAll(); } });
      body.append(
        mk('div', { class: 'w-row' }, viewTabs, playBtn, stepBtn),
        mk('div', { class: 'w-row' }, sA.el, sL.el, sF.el),
        mk('div', { class: 'w-row' }, sP.el, sQ.el)
      );

      // ---- displacement against distance ----
      const cA = W.canvas(body, {
        height: 210,
        draw(ctx, w, h, col) {
          const long = st.view === 'longitudinal';
          const ax = W.axes(ctx, w, h, { x0: 0, x1: XMAX, y0: -YM, y1: YM }, col,
            { pad: { l: geo.pl, r: geo.pr, t: 16, b: 34 }, xlabel: 'x / m', ylabel: long ? 's / cm' : 'y / cm' });
          const { X, Y } = ax;
          geo.w = w; geo.X = X; geo.Y = Y; geo.top = ax.pad.t;
          ctx.save();
          ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
          ctx.strokeStyle = col.sc; ctx.lineWidth = 2.5; ctx.beginPath();
          const n = 500;
          for (let i = 0; i <= n; i++) {
            const x = XMAX * i / n, yy = Y(yAt(x, t));
            if (i === 0) ctx.moveTo(X(x), yy); else ctx.lineTo(X(x), yy);
          }
          ctx.stroke();
          if (!long) {                                   // particles of the rope, moving up and down
            ctx.fillStyle = col.ink2;
            const dxp = Math.min(0.25, st.lam / 8);
            for (let x = 0; x <= XMAX + 1e-9; x += dxp) { ctx.beginPath(); ctx.arc(X(x), Y(yAt(x, t)), 2.3, 0, TAU); ctx.fill(); }
          }
          // one wavelength, crest to crest
          const u = ((0.25 + st.f * t) % 1 + 1) % 1, x1 = st.lam * u;
          if (x1 + st.lam <= XMAX) {
            const yy = Y(st.a + 0.8);
            ctx.strokeStyle = col.ink2; ctx.fillStyle = col.ink2; ctx.lineWidth = 1.5;
            ctx.setLineDash([]);
            arrowH(ctx, (X(x1) + X(x1 + st.lam)) / 2 - 1, X(x1), yy);
            arrowH(ctx, (X(x1) + X(x1 + st.lam)) / 2 + 1, X(x1 + st.lam), yy);
            label(ctx, col, 'λ', (X(x1) + X(x1 + st.lam)) / 2, yy - 5, 'center', col.ink2);
          }
          // P and Q
          const marks = [['P', st.xp, col.red], ['Q', st.xq, col.sc2]];
          marks.forEach(([nm, x, color], k) => {
            const px = X(x), py = Y(yAt(x, t));
            ctx.strokeStyle = color; ctx.lineWidth = 1.2; ctx.setLineDash([4, 3]);
            ctx.beginPath(); ctx.moveTo(px, Y(0)); ctx.lineTo(px, py); ctx.stroke(); ctx.setLineDash([]);
            ctx.fillStyle = color; ctx.beginPath(); ctx.arc(px, py, 6, 0, TAU); ctx.fill();
            ctx.strokeStyle = col.card; ctx.lineWidth = 1.5; ctx.stroke();
            let lx = px;
            if (k === 1 && Math.abs(X(st.xq) - X(st.xp)) < 20) lx = px + 20;
            label(ctx, col, nm, lx, ax.pad.t + 14, 'center', color);
          });
          ctx.restore();
          // direction of travel
          ctx.strokeStyle = col.ink2; ctx.fillStyle = col.ink2; ctx.lineWidth = 1.5;
          arrowH(ctx, w - 120, w - 70, h - 8);
          ctx.font = '12px ' + col.font; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
          ctx.fillText('wave travels', w - 66, h - 4);
        }
      });
      cA.wrap.style.touchAction = 'pan-y';

      // ---- the same wave as a row of particles (longitudinal) ----
      let cB = null;                                      // built the first time the longitudinal view is shown
      const makeB = () => W.canvas(body, {
        height: 84,
        draw(ctx, w, h, col) {
          const pl = geo.pl, pr = geo.pr, sc = (w - pl - pr) / XMAX;
          const px = (x) => pl + x * sc;
          const dx = Math.max(0.05, Math.min(0.2, st.lam / 10));
          const ad = Math.max(0.03, 0.12 * st.lam * st.a / 5);   // exaggerated displacement amplitude, m
          const sAt = (x) => ad * Math.sin(TAU * (x / st.lam - st.f * t));
          const yy = 34;
          ctx.strokeStyle = col.rule2; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(pl, yy); ctx.lineTo(w - pr, yy); ctx.stroke();
          const r = Math.max(1.3, Math.min(3.4, dx * sc * 0.38));
          ctx.fillStyle = col.ink2;
          for (let x = 0; x <= XMAX + 1e-9; x += dx) { ctx.beginPath(); ctx.arc(px(x + sAt(x)), yy, r, 0, TAU); ctx.fill(); }
          [['P', st.xp, col.red], ['Q', st.xq, col.sc2]].forEach(([nm, x, color]) => {
            ctx.fillStyle = color; ctx.beginPath(); ctx.arc(px(x + sAt(x)), yy, 5, 0, TAU); ctx.fill();
            ctx.strokeStyle = col.card; ctx.lineWidth = 1.5; ctx.stroke();
            label(ctx, col, nm, px(x + sAt(x)), yy - 12, 'center', color);
          });
          // compressions (C) and rarefactions (R): s = 0 with s decreasing along x is a compression
          if (dx * sc > 0 && st.lam * sc > 60) {
            for (let m = -1; m <= XMAX / st.lam + 1; m++) {
              const xc = st.lam * (0.5 + st.f * t + m), xr = st.lam * (st.f * t + m);
              if (xc >= 0 && xc <= XMAX) label(ctx, col, 'C', px(xc), yy + 28, 'center', col.ink);
              if (xr >= 0 && xr <= XMAX) label(ctx, col, 'R', px(xr), yy + 28, 'center', col.ink2);
            }
          }
          ctx.fillStyle = col.ink2; ctx.font = '12px ' + col.font; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
          ctx.fillText('particles (C = compression, R = rarefaction)', pl, h - 3);
        }
      });

      // ---- displacement against time for P and Q ----
      const cC = W.canvas(body, {
        height: 150,
        draw(ctx, w, h, col) {
          const long = st.view === 'longitudinal';
          const Tp = 1 / st.f, tw = 2 * Tp;
          const ax = W.axes(ctx, w, h, { x0: 0, x1: tw, y0: -YM, y1: YM }, col,
            { pad: { l: geo.pl, r: geo.pr, t: 12, b: 34 }, xlabel: 't / s', ylabel: long ? 's / cm' : 'y / cm' });
          const { X, Y } = ax;
          ctx.save();
          ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
          const curve = (x, color, dash) => {
            ctx.strokeStyle = color; ctx.lineWidth = 2.2; ctx.setLineDash(dash);
            ctx.beginPath();
            for (let i = 0; i <= 240; i++) { const tt = tw * i / 240, yy = Y(yAt(x, tt)); if (i === 0) ctx.moveTo(X(tt), yy); else ctx.lineTo(X(tt), yy); }
            ctx.stroke(); ctx.setLineDash([]);
          };
          curve(st.xq, col.sc2, [6, 4]);
          curve(st.xp, col.red, []);
          const tm = ((t % tw) + tw) % tw;
          ctx.strokeStyle = col.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(X(tm), ax.pad.t); ctx.lineTo(X(tm), h - ax.pad.b); ctx.stroke(); ctx.setLineDash([]);
          [[st.xp, col.red], [st.xq, col.sc2]].forEach(([x, color]) => {
            ctx.fillStyle = color; ctx.beginPath(); ctx.arc(X(tm), Y(yAt(x, tm)), 5, 0, TAU); ctx.fill();
          });
          ctx.restore();
          label(ctx, col, 'P (solid)', geo.pl, h - 2, 'left', col.red);
          label(ctx, col, 'Q (dashed)', geo.pl + 84, h - 2, 'left', col.sc2);
        }
      });

      const ro = W.readout([
        ['v', 'Wave speed v = fλ'], ['T', 'Period T = 1/f'],
        ['dx', 'Distance from P to Q'], ['ph', 'Phase difference between P and Q']
      ]);
      const msg = mk('div', { class: 'w-note' });
      const note = mk('div', { class: 'w-note' }, 'Try: put Q one whole wavelength from P (in phase), then half a wavelength (antiphase). Switch to Longitudinal and find the compressions. Lower f to watch one particle: it only moves up and down about its own position.');
      body.append(ro.el, msg, note, err);

      function showView() {
        if (st.view === 'longitudinal') {
          if (!cB) cB = makeB();
          body.insertBefore(cB.wrap, cC.wrap);
          cB.redraw();
        } else if (cB && cB.wrap.parentNode) {
          cB.wrap.parentNode.removeChild(cB.wrap);
        }
      }
      function readouts() {
        const v = st.f * st.lam, d = Math.abs(st.xq - st.xp), frac = d / st.lam;
        const phi = (frac % 1) * 360, rad = (frac % 1) * TAU;
        ro.set('v', W.fmt(st.f, 3) + ' Hz × ' + W.fmt(st.lam, 3) + ' m = ' + W.fmt(v, 3) + ' m s⁻¹');
        ro.set('T', W.fmt(1 / st.f, 3) + ' s');
        ro.set('dx', W.fmt(d, 3) + ' m = ' + W.fmt(frac, 3) + ' λ');
        ro.set('ph', W.fmt(phi, 3) + '° = ' + W.fmt(rad, 3) + ' rad (' + W.fmt(rad / Math.PI, 3) + 'π)');
        const eps = 0.004;
        const near = (x, y) => Math.abs(x - y) < eps;
        const fr = frac % 1;
        let s;
        if (d < 1e-9) s = 'P and Q are at the same place: no phase difference.';
        else if (near(fr, 0) || near(fr, 1)) s = 'A whole number of wavelengths apart: P and Q are in phase, so they move together.';
        else if (near(fr, 0.5)) s = 'An odd number of half wavelengths apart: P and Q are in antiphase (180°), so one is up when the other is down.';
        else s = (st.xq > st.xp ? 'Q is further along the direction of travel, so Q lags behind P' : 'Q is behind P in the direction of travel, so Q leads P') +
          ' by ' + W.fmt(phi, 3) + '° (reduced to between 0° and 360°).';
        msg.textContent = s;
      }
      function clampv(v, d, lo, hi) { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; }

      redrawAll = () => {
        cA.redraw();
        if (st.view === 'longitudinal') cB.redraw();
        cC.redraw();
        readouts();
      };

      W.drag(cA.wrap, {
        hit(x, y) {
          if (!geo.X) return null;
          const cand = [['P', st.xp], ['Q', st.xq]].map(([nm, xv]) => ({ nm, dx: Math.abs(geo.X(xv) - x), dy: Math.abs(geo.Y(yAt(xv, t)) - y) }))
            .filter((c) => c.dx < 22 && c.dy < 70).sort((a, b) => a.dx - b.dx);
          return cand.length ? cand[0].nm : null;
        },
        move(which, x) {
          const xv = Math.round(Math.min(XMAX, Math.max(0, (x - geo.pl) / (geo.w - geo.pl - geo.pr) * XMAX)) * 20) / 20;
          if (which === 'P') { st.xp = xv; sP.set(xv); } else { st.xq = xv; sQ.set(xv); }
          redrawAll();
        },
        end() {}
      });

      showView();
      readouts();
      if (!reduced) setPlaying(true);
    }

    // ======================================================================
    function buildStationary() {
      const L = 2.0, YM = 6.5, TD = 4;                  // string length (m), display period (s)
      stepSize = () => TD / 8;
      const sN = W.slider({ label: 'Harmonic n (number of loops)', min: 1, max: 6, step: 1, value: st.n, fmt: (v) => String(v), oninput: (v) => { st.n = Math.round(clampv(v, 3, 1, 6)); redrawAll(); } });
      const sA = W.sliderNum({ label: 'Amplitude A / cm', min: 0.5, max: 5, step: 0.1, value: st.a, oninput: (v) => { st.a = clampv(v, 2, 0.5, 5); redrawAll(); } });
      const cb = mk('input', { type: 'checkbox', 'aria-label': 'Show the two travelling waves' });
      cb.checked = st.comps;
      cb.onchange = () => { st.comps = cb.checked; redrawAll(); };
      const cbLab = mk('label', { class: 'w-ctl', style: { flexDirection: 'row', alignItems: 'center', gap: '8px' } }, cb, mk('span', { class: 'w-lab' }, 'Show the two travelling waves'));
      body.append(
        mk('div', { class: 'w-row' }, sN.el, sA.el),
        mk('div', { class: 'w-row' }, playBtn, stepBtn, cbLab)
      );

      const c = W.canvas(body, {
        height: 260,
        draw(ctx, w, h, col) {
          const k = st.n * Math.PI / L, om = TAU / TD;
          const ax = W.axes(ctx, w, h, { x0: 0, x1: L, y0: -YM, y1: YM }, col,
            { pad: { l: 46, r: 14, t: 18, b: 34 }, xlabel: 'x / m', ylabel: 'y / cm' });
          const { X, Y } = ax;
          ctx.save();
          ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
          const draw = (fn, color, lw, dash) => {
            ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.setLineDash(dash || []); ctx.beginPath();
            for (let i = 0; i <= 300; i++) { const x = L * i / 300, yy = Y(fn(x)); if (i === 0) ctx.moveTo(X(x), yy); else ctx.lineTo(X(x), yy); }
            ctx.stroke(); ctx.setLineDash([]);
          };
          draw((x) => st.a * Math.sin(k * x), col.ink3, 1, [5, 4]);
          draw((x) => -st.a * Math.sin(k * x), col.ink3, 1, [5, 4]);
          if (st.comps) {
            draw((x) => (st.a / 2) * Math.sin(k * x - om * t), col.sc, 1.6);
            draw((x) => (st.a / 2) * Math.sin(k * x + om * t), col.sc2, 1.6);
          }
          draw((x) => st.a * Math.sin(k * x) * Math.cos(om * t), col.red, 3);
          ctx.restore();
          // nodes and antinodes
          for (let m = 0; m <= st.n; m++) {
            const x = m * L / st.n;
            ctx.fillStyle = col.ink; ctx.beginPath(); ctx.arc(X(x), Y(0), 4, 0, TAU); ctx.fill();
            label(ctx, col, 'N', Math.min(w - 20, Math.max(ax.pad.l + 10, X(x))), h - ax.pad.b - 6, 'center', col.ink);
          }
          for (let m = 0; m < st.n; m++) {
            const x = (m + 0.5) * L / st.n;
            label(ctx, col, 'A', X(x), Y(st.a) - 8, 'center', col.ink);
          }
          ctx.fillStyle = col.ink2; ctx.font = '12px ' + col.font; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
          ctx.fillText(st.comps ? 'thick = sum · thin = the two travelling waves · dashed = envelope' : 'thick = the stationary wave · dashed = envelope', ax.pad.l + 6, h - 4);
        }
      });

      const ro = W.readout([
        ['L', 'String length L'], ['lam', 'Wavelength λ = 2L/n'], ['f', 'Frequency'],
        ['nn', 'Nodes (with both ends)'], ['aa', 'Antinodes']
      ]);
      const note = mk('div', { class: 'w-note' }, 'Try: switch the travelling waves on, press Pause, and use Step to see how the thin waves add to the thick one. Count the nodes for n = 1 to 6: there are always n + 1, with the two ends fixed. The animation is slowed down so you can follow it; a real string vibrates much faster.');
      body.append(ro.el, note, err);

      function readouts() {
        ro.set('L', W.fmt(L, 3) + ' m = ' + st.n + ' × λ/2 (L = nλ/2)');
        ro.set('lam', W.fmt(2 * L / st.n, 3) + ' m');
        ro.set('f', st.n + ' × f₁ (the speed v = fλ stays the same)');
        ro.set('nn', String(st.n + 1) + ' (' + (st.n - 1) + ' between the ends, λ/2 apart)');
        ro.set('aa', String(st.n));
      }
      function clampv(v, d, lo, hi) { const x = parseFloat(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; }
      redrawAll = () => { c.redraw(); readouts(); };
      readouts();
      if (!reduced) setPlaying(true);
    }
  });
})();
