/* phys-stretch: stretching a wire, loading and unloading (phys.solids).
   data-material="steel|copper|rubber" (default copper)  data-l="2.0" (original length, m, 0.5–5)
   data-d="0.50" (diameter, mm, 0.1–2).
   Typical values: steel E 2.0e11 Pa, limit of proportionality 2.5e8, elastic limit 2.7e8, breaking 4.0e8;
   copper E 1.2e11, 7e7, 8e7, 2.2e8. The plastic strain range is shortened so the whole curve fits on one graph.
   Rubber is a qualitative non-linear curve (steep, flatter, then stiffening) with no plastic region. */
(function () {
  'use strict';
  W.register('phys-stretch', function (el, opts) {
    const { body } = W.frame(el, 'Stretching a wire', 'Load the wire, pass its limits, then remove the load');
    const msgs = [];
    const numOpt = (v, d, lo, hi, label) => {
      if (v === undefined || v === null || v === '') return d;
      const x = parseFloat(v);
      if (!isFinite(x)) { msgs.push(label + ' must be a number, so ' + d + ' is used.'); return d; }
      const c = Math.min(hi, Math.max(lo, x));
      if (c !== x) msgs.push(label + ' must be between ' + lo + ' and ' + hi + ', so ' + c + ' is used.');
      return c;
    };

    const rub = (e) => 1e7 * e / (1 + 3 * e) + 9.26e3 * Math.pow(e, 4);   // rubber stress (Pa) at strain e
    const RUB_EB = 5;
    const MAT = {
      steel: { label: 'Steel', E: 2.0e11, sp: 2.5e8, se: 2.7e8, sb: 4.0e8, eb: 0.010 },
      copper: { label: 'Copper', E: 1.2e11, sp: 7e7, se: 8e7, sb: 2.2e8, eb: 0.012 },
      rubber: { label: 'Rubber', rubber: true, E: 1e7, sp: 0, se: Infinity, sb: rub(RUB_EB), eb: RUB_EB }
    };
    let matKey = 'copper';
    if (opts.material !== undefined && opts.material !== '') {
      const k = String(opts.material).toLowerCase();
      if (MAT[k]) matKey = k; else msgs.push('Material "' + W.esc(String(opts.material)) + '" is not available, so copper is used.');
    }
    const st = {
      mat: matKey,
      L: numOpt(opts.l, 2.0, 0.5, 5, 'Length'),
      d: numOpt(opts.d, 0.5, 0.1, 2, 'Diameter'),
      p: 0.3,          // load as a fraction of the breaking load
      unl: false       // load removed
    };

    // strain at a given stress (monotonic in stress, so the load can be the controlled variable)
    function epsOf(m, s) {
      if (s <= 0) return 0;
      if (m.rubber) {
        let lo = 0, hi = RUB_EB;
        for (let i = 0; i < 60; i++) { const mid = (lo + hi) / 2; if (rub(mid) < s) lo = mid; else hi = mid; }
        return (lo + hi) / 2;
      }
      if (s <= m.sp) return s / m.E;
      if (s <= m.se) return s / m.E + 0.5 * (s - m.sp) * (s - m.sp) / ((m.se - m.sp) * m.E);
      const ee = m.se / m.E + 0.5 * (m.se - m.sp) / m.E;
      const u = Math.min(1, (s - m.se) / (m.sb - m.se));
      return ee + (m.eb - ee) * (1 - Math.sqrt(1 - u));
    }

    // number formatting
    const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
    function sci(x, sf) {
      if (!isFinite(x)) return '–';
      if (x === 0) return '0';
      let e = Math.floor(Math.log10(Math.abs(x)));
      let m = x / Math.pow(10, e);
      if (parseFloat(Math.abs(m).toPrecision(sf)) >= 10) { m /= 10; e += 1; }
      if (e >= -2 && e <= 2) return parseFloat(x.toPrecision(sf)).toString();
      return m.toFixed(sf - 1) + ' × 10' + String(e).split('').map((ch) => SUP[ch] || ch).join('');
    }
    const fmtLen = (x) => (x === 0 ? '0 mm' : x < 1 ? sci(x * 1e3, 3) + ' mm' : sci(x, 3) + ' m');

    // derived quantities for the current wire
    function model() {
      const m = MAT[st.mat];
      const A = Math.PI * Math.pow(st.d * 1e-3, 2) / 4;
      const Fb = m.sb * A;
      const k0 = (m.rubber ? 1e7 : m.E) * A / st.L;
      const xOf = (F) => epsOf(m, F / A) * st.L;
      return { m, A, Fb, k0, xOf, xb: m.eb * st.L };
    }
    function permExt(M, Fmax) {
      if (M.m.rubber) return 0;
      if (Fmax / M.A <= M.m.se) return 0;
      return Math.max(0, M.xOf(Fmax) - Fmax / M.k0);
    }
    function energyArea(M, Fmax) {            // area under the loading curve, J
      const smax = Fmax / M.A, n = 400;
      let sum = 0, e0 = 0, s0 = 0;
      for (let i = 1; i <= n; i++) {
        const s = smax * i / n, e = epsOf(M.m, s);
        sum += 0.5 * (s + s0) * (e - e0);
        s0 = s; e0 = e;
      }
      return sum * M.A * st.L;
    }

    // controls
    const err = W.h('div', { class: 'w-err', style: { display: msgs.length ? '' : 'none' } });
    err.textContent = msgs.join(' ');
    function tabs(items, get, set) {
      const row = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Material' });
      const btns = items.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { set(v); sync(); update(); } }, label));
      const sync = () => btns.forEach((b, i) => b.setAttribute('aria-selected', String(items[i][0] === get())));
      btns.forEach((b) => row.append(b));
      sync();
      return row;
    }
    const matTabs = tabs([['steel', 'Steel'], ['copper', 'Copper'], ['rubber', 'Rubber']], () => st.mat, (v) => { st.mat = v; st.unl = false; });
    const sL = W.sliderNum({ label: 'Original length / m', min: 0.5, max: 5, step: 0.1, value: st.L, oninput: (v) => { st.L = numOpt(v, 2.0, 0.5, 5, 'Length'); st.unl = false; update(); } });
    const sD = W.sliderNum({ label: 'Diameter / mm', min: 0.1, max: 2, step: 0.05, value: st.d, oninput: (v) => { st.d = numOpt(v, 0.5, 0.1, 2, 'Diameter'); st.unl = false; update(); } });
    const sP = W.slider({ label: 'Load', min: 0, max: 1, step: 0.001, value: st.p, fmt: (v) => Math.round(v * 100) + '% of the breaking load', oninput: (v) => { st.p = Math.min(1, Math.max(0, v)); st.unl = false; update(); } });
    const rmBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { if (st.p > 0 && st.p < 0.995) { st.unl = true; update(); } } }, 'Remove load');

    body.append(
      W.h('div', { class: 'w-row' }, matTabs),
      W.h('div', { class: 'w-row' }, sL.el, sD.el),
      W.h('div', { class: 'w-row' }, sP.el, rmBtn)
    );

    const c = W.canvas(body, {
      height: 280,
      draw(ctx, w, h, col) {
        const M = model();
        const mm = M.xb < 1;
        const xu = mm ? 1e3 : 1;
        const view = { x0: 0, x1: M.xb * xu * 1.08, y0: 0, y1: M.Fb * 1.12 };
        const ax = W.axes(ctx, w, h, view, col, {
          pad: { l: 52, r: 14, t: 16, b: 34 },
          xlabel: 'extension / ' + (mm ? 'mm' : 'm'),
          ylabel: 'force / N'
        });
        const { X, Y } = ax;
        const Fmax = st.p * M.Fb;
        const snapped = st.p >= 0.995;
        ctx.save();
        ctx.beginPath(); ctx.rect(ax.pad.l, ax.pad.t, w - ax.pad.l - ax.pad.r, h - ax.pad.t - ax.pad.b); ctx.clip();
        // loading curve points (dense near the top, where the plastic region is flat)
        const pts = [];
        const n = 400;
        for (let i = 0; i <= n; i++) {
          const u = i / n, F = Fmax * (1 - (1 - u) * (1 - u));
          pts.push([M.xOf(F) * xu, F]);
        }
        if (Fmax > 0) {
          // work done: area under the loading curve
          ctx.globalAlpha = 0.18; ctx.fillStyle = col.sc;
          ctx.beginPath(); ctx.moveTo(X(0), Y(0));
          pts.forEach((p) => ctx.lineTo(X(p[0]), Y(p[1])));
          ctx.lineTo(X(pts[n][0]), Y(0)); ctx.closePath(); ctx.fill();
          ctx.globalAlpha = 1;
          if (st.unl) {                                   // energy recovered on unloading
            const xp = permExt(M, Fmax) * xu;
            ctx.globalAlpha = 0.35; ctx.fillStyle = col.sc2;
            ctx.beginPath(); ctx.moveTo(X(xp), Y(0)); ctx.lineTo(X(pts[n][0]), Y(Fmax)); ctx.lineTo(X(pts[n][0]), Y(0)); ctx.closePath(); ctx.fill();
            ctx.globalAlpha = 1;
          }
        }
        // full curve, faint, so the reader sees what lies ahead
        ctx.strokeStyle = col.rule2; ctx.lineWidth = 1.5; ctx.beginPath();
        for (let i = 0; i <= 200; i++) {
          const u = i / 200, F = M.Fb * (1 - (1 - u) * (1 - u));
          if (i === 0) ctx.moveTo(X(0), Y(0)); else ctx.lineTo(X(M.xOf(F) * xu), Y(F));
        }
        ctx.stroke();
        ctx.strokeStyle = col.sc; ctx.lineWidth = 2.5; ctx.beginPath();
        pts.forEach((p, i) => { if (i === 0) ctx.moveTo(X(p[0]), Y(p[1])); else ctx.lineTo(X(p[0]), Y(p[1])); });
        ctx.stroke();
        // unloading line
        let dotX = pts[n][0], dotY = Fmax;
        if (st.unl) {
          const xp = permExt(M, Fmax) * xu;
          ctx.strokeStyle = col.red; ctx.lineWidth = 2; ctx.setLineDash([6, 4]);
          ctx.beginPath(); ctx.moveTo(X(pts[n][0]), Y(Fmax)); ctx.lineTo(X(xp), Y(0)); ctx.stroke();
          ctx.setLineDash([]);
          dotX = xp; dotY = 0;
        }
        // markers: limit of proportionality (P) and elastic limit (E)
        if (!M.m.rubber) {
          const mk = (s, lab, side) => {
            const F = s * M.A, px = X(M.xOf(F) * xu), py = Y(F);
            ctx.strokeStyle = col.ink2; ctx.fillStyle = col.card; ctx.lineWidth = 1.5;
            ctx.beginPath(); ctx.arc(px, py, 4, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
            ctx.fillStyle = col.ink2; ctx.font = '600 12px ' + col.font; ctx.textBaseline = 'middle';
            ctx.textAlign = side > 0 ? 'left' : 'right';
            ctx.fillText(lab, px + side * 8, py + (side > 0 ? -6 : 6));
          };
          mk(M.m.sp, 'P', -1);
          mk(M.m.se, 'E', 1);
        }
        // current point
        ctx.fillStyle = col.red; ctx.beginPath(); ctx.arc(X(dotX), Y(dotY), 5, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
        ctx.fillStyle = col.ink2; ctx.font = '12px ' + col.font; ctx.textBaseline = 'alphabetic'; ctx.textAlign = 'right';
        const lx = w - ax.pad.r - 8, ly = h - ax.pad.b - 10;
        if (!M.m.rubber) { ctx.fillText('P: limit of proportionality', lx, ly - 16); ctx.fillText('E: elastic limit', lx, ly); }
        else ctx.fillText('qualitative curve only', lx, ly);
        ctx.textAlign = 'left';
        if (snapped) {
          ctx.fillStyle = col.red; ctx.font = '700 20px ' + col.font; ctx.textAlign = 'center';
          ctx.fillText('The wire has snapped!', ax.pad.l + (w - ax.pad.l - ax.pad.r) / 2, ax.pad.t + 52);
        }
      }
    });

    const ro = W.readout([
      ['F', 'Load F'], ['x', 'Extension x'], ['s', 'Stress σ = F/A'], ['e', 'Strain ε = x/L'],
      ['E', 'Young modulus σ/ε'], ['en', 'Energy stored'], ['perm', 'Permanent extension']
    ]);
    const note = W.h('div', { class: 'w-note' });
    body.append(ro.el, note, err);

    function update() {
      const M = model();
      const m = M.m;
      const Fmax = st.p * M.Fb;
      const snapped = st.p >= 0.995;
      const F = st.unl ? 0 : Fmax;
      const xperm = st.unl ? permExt(M, Fmax) : 0;
      const x = st.unl ? xperm : M.xOf(F);
      const s = F / M.A;
      const eps = x / st.L;
      ro.set('F', F === 0 ? '0 N' : sci(F, 3) + ' N');
      ro.set('x', fmtLen(x));
      ro.set('s', s === 0 ? '0 Pa' : sci(s, 3) + ' Pa');
      ro.set('e', eps === 0 ? '0 (no unit)' : sci(eps, 3) + ' (no unit)');
      if (st.unl) ro.set('E', 'load removed');
      else if (m.rubber) ro.set('E', F === 0 ? '–' : 'not constant (rubber is not proportional)');
      else if (F === 0) ro.set('E', '–');
      else if (s <= m.sp) ro.set('E', sci(s / eps, 3) + ' Pa');
      else ro.set('E', 'beyond the limit of proportionality');
      if (st.unl) {
        const W0 = energyArea(M, Fmax), Wr = 0.5 * Fmax * (M.xOf(Fmax) - xperm);
        ro.set('en', 'work done ' + sci(W0, 3) + ' J, recovered ' + sci(m.rubber ? W0 : Wr, 3) + ' J');
      } else if (F === 0) ro.set('en', '0 J');
      else if (!m.rubber && s <= m.sp) ro.set('en', '½Fx = ' + sci(0.5 * F * x, 3) + ' J');
      else ro.set('en', 'area under the curve = ' + sci(energyArea(M, F), 3) + ' J');
      const px = permExt(M, Fmax);
      if (st.unl) ro.set('perm', px === 0 ? 'none: back to its original length' : fmtLen(px));
      else ro.set('perm', Fmax === 0 ? '–' : (px === 0 ? 'none if unloaded now' : fmtLen(px) + ' if unloaded now'));
      rmBtn.style.display = snapped ? 'none' : '';
      rmBtn.disabled = st.p === 0;
      if (snapped) note.textContent = 'The wire broke at the breaking stress. Slide the load back to fit a fresh wire.';
      else if (st.unl) note.textContent = m.rubber
        ? 'Rubber returns to its original length: the red line retraces the loading curve. Move the load slider to load it again.'
        : (px === 0
          ? 'You stayed within the elastic limit, so the wire went back to its original length. Move the load slider to load it again.'
          : 'The red line is parallel to the straight part of the graph and leaves a permanent extension. The area between the two lines is the energy dissipated as thermal energy.');
      else note.textContent = m.rubber
        ? 'Typical values; rubber is a qualitative curve. Slide the load up: the extension is not proportional to the force, but there is no permanent extension.'
        : 'Typical values; the plastic region is shortened to fit. Slide the load past P and E, then press Remove load and see what is left over.';
      c.redraw();
    }
    update();
  });
})();
