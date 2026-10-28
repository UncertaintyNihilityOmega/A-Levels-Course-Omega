/* widgets/bio-enzyme.js: enzyme rate explorer (package P4). data-mode = temperature | ph | kinetics (default kinetics).
   Models (all simplified, arbitrary units, stated on screen):
   - temperature: rate = 7 * 2^(T/10) / (1 + exp((T - 45) / 2.5)), the curve plotted in the Enzymes chapter (peak near 41 C);
   - pH: bell curves 100 * exp(-((pH - opt)/1.3)^2) for pepsin (opt about 2) and salivary amylase (opt about 7);
   - kinetics: Michaelis-Menten rate = Vmax * S / (Km + S); competitive inhibitor Km x 3; non-competitive Vmax x 0.5.
   Optional attributes: data-vmax (20-100), data-km (0.5-10), data-s (0-50). */
(function () {
  'use strict';

  const MODES = ['temperature', 'ph', 'kinetics'];
  const TITLES = { temperature: 'Temperature', ph: 'pH', kinetics: 'Substrate and inhibitors' };
  const ENZ = [
    { name: 'stomach protease (pepsin)', opt: 2 },
    { name: 'salivary amylase', opt: 7 }
  ];

  function rateT(T) { return 7 * Math.pow(2, T / 10) / (1 + Math.exp((T - 45) / 2.5)); }
  function ratePH(p, opt) { return 100 * Math.exp(-Math.pow((p - opt) / 1.3, 2)); }
  function rateMM(s, v, k) { return v * s / (k + s); }

  // the optimum of the temperature model, found once
  let T0 = 0, R0 = 0;
  for (let t = 0; t <= 80; t += 0.1) { const r = rateT(t); if (r > R0) { R0 = r; T0 = t; } }

  function num(v, lo, hi, dflt) {
    const x = parseFloat(v);
    return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : dflt;
  }
  function fix(x, d) { return isFinite(x) ? (Math.round(x * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d) : '–'; }
  function clean(x, d) { return String(Number(fix(x, d))); }

  W.register('bio-enzyme', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Enzyme rate explorer', 'Simplified model curves in arbitrary units');
    const st = {
      mode: MODES.indexOf(opts.mode) >= 0 ? opts.mode : 'kinetics',
      T: 25, pH: 5, enz: 0,
      vmax: num(opts.vmax, 20, 100, 80), km: num(opts.km, 0.5, 10, 4), s: num(opts.s, 0, 50, 10),
      comp: true, nonc: false
    };

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Factor to explore' });
    const tabBtns = {};
    MODES.forEach(function (m) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': m === st.mode ? 'true' : 'false', text: TITLES[m] });
      b.onclick = function () { setMode(m); };
      tabBtns[m] = b;
      tabs.appendChild(b);
    });
    body.appendChild(W.h('div', { class: 'w-row' }, tabs));
    const panel = W.h('div');
    body.appendChild(panel);

    // ----- helpers shared by the three modes -----
    function setupCanvas(label, describe, draw) {
      return W.canvas(panel, { height: 270, label: label, describe: describe, draw: draw });
    }
    function clipPlot(ctx, A, v) {
      ctx.save();
      ctx.beginPath();
      ctx.rect(A.X(v.x0), A.Y(v.y1), A.X(v.x1) - A.X(v.x0), A.Y(v.y0) - A.Y(v.y1));
      ctx.clip();
    }
    function curve(ctx, A, v, f, color, width, alpha) {
      ctx.save();
      ctx.globalAlpha = alpha == null ? 1 : alpha;
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.lineJoin = 'round';
      ctx.beginPath();
      const n = 160;
      for (let i = 0; i <= n; i++) {
        const x = v.x0 + (v.x1 - v.x0) * i / n;
        const px = A.X(x), py = A.Y(f(x));
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.restore();
    }
    function dashed(ctx, c, x0, y0, x1, y1, color) {
      ctx.save();
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      ctx.setLineDash([6, 4]);
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();
      ctx.restore();
    }
    function tag(ctx, c, txt, x, y, align, color) {
      ctx.save();
      ctx.font = '12px ' + c.font;
      ctx.textAlign = align || 'left';
      ctx.textBaseline = 'alphabetic';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 4;
      ctx.strokeStyle = c.card;
      ctx.strokeText(txt, x, y);
      ctx.fillStyle = color || c.ink;
      ctx.fillText(txt, x, y);
      ctx.restore();
    }
    function marker(ctx, c, A, x, y) {
      ctx.save();
      ctx.strokeStyle = c.red;
      ctx.lineWidth = 1.5;
      ctx.setLineDash([2, 3]);
      ctx.beginPath();
      ctx.moveTo(A.X(x), A.Y(y));
      ctx.lineTo(A.X(x), A.Y(0));
      ctx.stroke();
      ctx.restore();
      ctx.beginPath();
      ctx.arc(A.X(x), A.Y(y), 6, 0, 2 * Math.PI);
      ctx.fillStyle = c.red;
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = c.card;
      ctx.stroke();
    }
    function note(txt) { return W.h('div', { class: 'w-note', text: txt }); }
    function explain() { return W.h('div', { class: 'w-note', 'aria-live': 'polite' }); }

    // ----- mode: temperature -----
    function buildTemperature() {
      const v = { x0: 0, x1: 80, y0: 0, y1: 120 };
      function draw(ctx, w, h, c) {
        if (w <= 0 || h <= 0) return;
        const A = W.axes(ctx, w, h, v, c, { xlabel: 'temperature / °C', ylabel: 'rate / arbitrary units', nx: 8, ny: 4 });
        if (!A) return;
        clipPlot(ctx, A, v);
        curve(ctx, A, v, rateT, c.sc, 3);
        ctx.restore();
        tag(ctx, c, 'optimum region', A.X(T0), A.Y(R0) - 10, 'center', c.ink2);
        marker(ctx, c, A, st.T, rateT(st.T));
      }
      const cv = setupCanvas('Rate of an enzyme reaction against temperature, model curve',
        function () { return 'Model curve of rate against temperature from 0 to 80 °C. The rate rises from ' + clean(rateT(0), 0) + ' units at 0 °C to a peak of about ' + clean(R0, 0) + ' near ' + clean(T0, 0) + ' °C, then falls steeply to almost zero by 60 °C. The marker is at ' + st.T + ' °C, rate ' + clean(rateT(st.T), 0) + ' units.'; },
        draw);
      const sl = W.sliderNum({ label: 'Temperature / °C', min: 0, max: 80, step: 1, value: st.T, oninput: function () { st.T = sl.get(); update(); } });
      panel.appendChild(W.h('div', { class: 'w-row' }, sl.el));
      const ro = W.readout([['t', 'Temperature'], ['r', 'Rate'], ['s', 'Stage']]);
      panel.appendChild(ro.el);
      const ex = explain();
      panel.appendChild(ex);
      panel.appendChild(note('Move the slider from 0 to 80 °C. This is a model curve only: the values are arbitrary, and the optimum is different for every enzyme.'));
      function update() {
        const T = st.T, r = rateT(T);
        let stage, msg;
        if (T < T0 - 4) {
          stage = 'rising';
          msg = 'Rate rising: more kinetic energy, so more frequent collisions and more successful collisions between enzyme and substrate.';
          if (T <= 8) msg += ' The enzyme is slow here, not damaged: warming it would restore the rate.';
        } else if (T <= T0 + 4) {
          stage = 'near the optimum';
          msg = 'Near the optimum: the rate is at or close to its maximum for this enzyme.';
        } else {
          stage = 'falling';
          msg = 'Rate falling: bonds holding the tertiary structure break, so the active site changes shape and fewer enzyme–substrate complexes form.';
          if (r < 2) msg += ' The enzyme is denatured and almost no reaction takes place.';
        }
        ro.set('t', T + ' °C');
        ro.set('r', clean(r, 0) + ' arbitrary units');
        ro.set('s', stage);
        ex.textContent = msg;
        cv.redraw();
      }
      update();
    }

    // ----- mode: pH -----
    function buildPH() {
      const v = { x0: 1, x1: 13, y0: 0, y1: 120 };
      function draw(ctx, w, h, c) {
        if (w <= 0 || h <= 0) return;
        const A = W.axes(ctx, w, h, v, c, { xlabel: 'pH', ylabel: 'rate / % of maximum', nx: 6, ny: 4 });
        if (!A) return;
        const e = ENZ[st.enz], o = ENZ[1 - st.enz];
        clipPlot(ctx, A, v);
        curve(ctx, A, v, function (p) { return ratePH(p, o.opt); }, c.ink3, 2, 0.5);
        curve(ctx, A, v, function (p) { return ratePH(p, e.opt); }, c.sc, 3);
        ctx.restore();
        tag(ctx, c, 'optimum about pH ' + e.opt, A.X(e.opt) + (e.opt < 5 ? 8 : -8), A.Y(100) - 8, e.opt < 5 ? 'left' : 'right', c.ink2);
        marker(ctx, c, A, st.pH, ratePH(st.pH, e.opt));
      }
      const cv = setupCanvas('Rate of an enzyme reaction against pH, model curve',
        function () {
          const e = ENZ[st.enz];
          return 'Model curve of rate against pH for ' + e.name + ', a bell shape with its peak of 100 per cent near pH ' + e.opt + ' and almost no activity more than 3 pH units away. The second enzyme is drawn faint. The marker is at pH ' + clean(st.pH, 1) + ', rate ' + clean(ratePH(st.pH, e.opt), 0) + ' per cent.';
        }, draw);
      const sel = W.h('select', { 'aria-label': 'Enzyme' });
      ENZ.forEach(function (e, i) { sel.appendChild(W.h('option', { value: String(i), text: e.name })); });
      sel.value = String(st.enz);
      sel.onchange = function () { st.enz = parseInt(sel.value, 10) || 0; update(); };
      const sl = W.sliderNum({ label: 'pH', min: 1, max: 13, step: 0.1, value: st.pH, oninput: function () { st.pH = sl.get(); update(); } });
      panel.appendChild(W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } },
        W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Enzyme' }), sel), sl.el));
      const ro = W.readout([['p', 'pH'], ['r', 'Rate'], ['s', 'Stage']]);
      panel.appendChild(ro.el);
      const ex = explain();
      panel.appendChild(ex);
      panel.appendChild(note('Choose an enzyme, then move the pH away from its optimum. The faint curve is the other enzyme. Model curves only: each optimum is approximate.'));
      function update() {
        const e = ENZ[st.enz], p = st.pH, r = ratePH(p, e.opt), d = p - e.opt;
        let stage, msg;
        if (Math.abs(d) <= 0.6) {
          stage = 'near the optimum';
          msg = 'Near the optimum: the charges on the R groups and the shape of the active site suit the substrate, so many enzyme–substrate complexes form.';
        } else if (d < 0) {
          stage = 'too acidic';
          msg = 'Extra H⁺ ions change the charges on R groups. Ionic bonds and hydrogen bonds between R groups break, so the tertiary structure and the active site change shape and the substrate binds less well.';
        } else {
          stage = 'too alkaline';
          msg = 'Extra OH⁻ ions change the charges on R groups. Ionic bonds and hydrogen bonds between R groups break, so the tertiary structure and the active site change shape and the substrate binds less well.';
        }
        if (Math.abs(d) > 0.6 && r < 5) msg += ' The enzyme is denatured: almost no activity.';
        ro.set('p', clean(p, 1));
        ro.set('r', clean(r, 0) + ' % of maximum');
        ro.set('s', stage);
        ex.textContent = msg;
        cv.redraw();
      }
      update();
    }

    // ----- mode: kinetics -----
    function eff() { return { V: st.vmax * (st.nonc ? 0.5 : 1), K: st.km * (st.comp ? 3 : 1) }; }
    function buildKinetics() {
      function yMax() { return Math.ceil(st.vmax * 1.25 / 10) * 10; }
      function draw(ctx, w, h, c) {
        if (w <= 0 || h <= 0) return;
        const v = { x0: 0, x1: 50, y0: 0, y1: yMax() };
        const A = W.axes(ctx, w, h, v, c, { xlabel: 'substrate concentration / mmol dm⁻³', ylabel: 'rate / arbitrary units', nx: 5, ny: 4 });
        if (!A) return;
        const e = eff(), any = st.comp || st.nonc, half = e.V / 2;
        clipPlot(ctx, A, v);
        if (any) curve(ctx, A, v, function (s) { return rateMM(s, st.vmax, st.km); }, c.ink3, 2, 0.55);
        curve(ctx, A, v, function (s) { return rateMM(s, e.V, e.K); }, c.sc, 3);
        dashed(ctx, c, A.X(0), A.Y(e.V), A.X(50), A.Y(e.V), c.ink2);
        dashed(ctx, c, A.X(0), A.Y(half), A.X(e.K), A.Y(half), c.ink2);
        dashed(ctx, c, A.X(e.K), A.Y(half), A.X(e.K), A.Y(0), c.ink2);
        ctx.restore();
        tag(ctx, c, 'Vmax = ' + clean(e.V, 1), A.X(50) - 4, A.Y(e.V) - 6, 'right', c.ink);
        tag(ctx, c, 'Km = ' + clean(e.K, 1), A.X(e.K) + 5, A.Y(0) - 8, 'left', c.ink);
        if (A.X(e.K) - A.X(0) > 60) tag(ctx, c, 'half of Vmax', A.X(0) + 6, A.Y(half) - 5, 'left', c.ink2);
        marker(ctx, c, A, st.s, rateMM(st.s, e.V, e.K));
      }
      const cv = setupCanvas('Rate of an enzyme reaction against substrate concentration, Michaelis–Menten model',
        function () {
          const e = eff();
          return 'Model curve of rate against substrate concentration. It rises and levels off towards Vmax = ' + clean(e.V, 1) + ' units. Half of Vmax, ' + clean(e.V / 2, 1) + ', is reached at a substrate concentration Km = ' + clean(e.K, 1) + ' mmol per dm cubed. '
            + (st.comp ? 'A competitive inhibitor is on. ' : '') + (st.nonc ? 'A non-competitive inhibitor is on. ' : '')
            + 'The marker is at a substrate concentration of ' + clean(st.s, 1) + ', rate ' + clean(rateMM(st.s, e.V, e.K), 1) + ' units.';
        }, draw);
      const sV = W.sliderNum({ label: 'Vmax (no inhibitor)', min: 20, max: 100, step: 1, value: st.vmax, oninput: function () { st.vmax = sV.get(); update(); } });
      const sK = W.sliderNum({ label: 'Km (mmol dm⁻³, no inhibitor)', min: 0.5, max: 10, step: 0.5, value: st.km, oninput: function () { st.km = sK.get(); update(); } });
      const sS = W.sliderNum({ label: 'Substrate concentration [S] (mmol dm⁻³)', min: 0, max: 50, step: 0.5, value: st.s, oninput: function () { st.s = sS.get(); update(); } });
      panel.appendChild(W.h('div', { class: 'w-row' }, sV.el));
      panel.appendChild(W.h('div', { class: 'w-row' }, sK.el));
      panel.appendChild(W.h('div', { class: 'w-row' }, sS.el));
      function check(txt, key) {
        const cb = W.h('input', { type: 'checkbox' });
        cb.checked = !!st[key];
        cb.onchange = function () { st[key] = cb.checked; update(); };
        return W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, cb, W.h('span', { class: 'w-lab', text: txt }));
      }
      panel.appendChild(W.h('div', { class: 'w-row' }, check('Competitive inhibitor (Km × 3)', 'comp')));
      panel.appendChild(W.h('div', { class: 'w-row' }, check('Non-competitive inhibitor (Vmax × 0.5)', 'nonc')));
      const ro = W.readout([['v', 'Vmax'], ['k', 'Km'], ['r', 'Rate at the chosen [S]']]);
      panel.appendChild(ro.el);
      const ex = explain();
      panel.appendChild(ex);
      panel.appendChild(W.h('div', { class: 'w-note' },
        'Key to the graph: the solid curve is the rate with the current settings; the faint curve is the rate with no inhibitor; dashed lines mark Vmax, half of Vmax and the drop line to Km; the dot is the chosen [S]. Model only, arbitrary units.'));
      panel.appendChild(note('Switch the competitive inhibitor off and on: Vmax stays, Km rises. Then try the non-competitive inhibitor: Vmax falls, Km stays.'));
      function update() {
        const e = eff();
        ro.set('v', clean(e.V, 1) + ' arbitrary units');
        ro.set('k', clean(e.K, 1) + ' mmol dm⁻³');
        ro.set('r', clean(rateMM(st.s, e.V, e.K), 1) + ' arbitrary units');
        let msg;
        if (st.comp && st.nonc) msg = 'Both inhibitors: Vmax is halved and Km is tripled. The competitive one binds the active site; the non-competitive one binds elsewhere and changes the active site.';
        else if (st.comp) msg = 'Competitive inhibitor: it binds the active site, so more substrate is needed to reach half of Vmax (Km × 3). Vmax is unchanged, because plenty of substrate beats the inhibitor.';
        else if (st.nonc) msg = 'Non-competitive inhibitor: it binds elsewhere and changes the shape of the active site, so some enzyme molecules cannot work. Vmax is halved and Km is unchanged.';
        else msg = 'No inhibitor: the rate reaches half of Vmax at the substrate concentration Km. A low Km means a high affinity.';
        ex.textContent = msg;
        cv.redraw();
      }
      update();
    }

    function setMode(m) {
      st.mode = m;
      MODES.forEach(function (k) { tabBtns[k].setAttribute('aria-pressed', k === m ? 'true' : 'false'); });
      build();
    }
    function build() {
      panel.textContent = '';
      if (st.mode === 'temperature') buildTemperature();
      else if (st.mode === 'ph') buildPH();
      else buildKinetics();
    }
    build();
  });
})();
