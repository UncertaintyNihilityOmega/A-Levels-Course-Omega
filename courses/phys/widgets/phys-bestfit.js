/* phys-bestfit: best-fit line, worst acceptable line and the uncertainty in the gradient (phys.planning).
   data-preset="pendulum|discharge|power|blank" (default discharge). Presets give the table and the graph shown first:
     pendulum  l / m and T / s, graph T² against l, readout g = 4π² / gradient
     discharge t / s and V / V, graph ln V against t, readout RC = −1 / gradient and V₀
     power     x and y with y = a xⁿ, graph lg y against lg x, readout n and a
     blank     x and y with a straight-line relationship, graph y against x
   data-x, data-y, data-dy: comma lists (3–10 values) that replace the preset table; data-dy may be one number for all rows.
   data-xlabel, data-ylabel: names such as "t / s" (quantity / unit). data-tab="y|lg|ln|sq" chooses the graph shown first.
   Bars are drawn as ± (value transformed − value), the "max minus value" rule, so they are symmetric on the graph.
   The best-fit line is least squares. The worst acceptable line is the steepest or shallowest straight line that still
   passes through every error bar (an exact search over the bounding lines), whichever differs more from the best fit. */
(function () {
  'use strict';

  // <math>
  function lsq(X, Y) {
    const n = X.length;
    let sx = 0, sy = 0;
    for (let i = 0; i < n; i++) { sx += X[i]; sy += Y[i]; }
    const mx = sx / n, my = sy / n;
    let sxx = 0, sxy = 0;
    for (let i = 0; i < n; i++) { sxx += (X[i] - mx) * (X[i] - mx); sxy += (X[i] - mx) * (Y[i] - my); }
    if (!(sxx > 0)) return null;
    const m = sxy / sxx;
    return { m: m, c: my - m * mx };
  }
  // The straight lines that pass through every bar form a convex set in (gradient, intercept); its extreme gradients
  // are lines through two bar ends. Try every pair, keep those that cross every bar.
  function extremeLines(X, lo, hi) {
    const pts = [];
    let scale = 1;
    for (let i = 0; i < X.length; i++) {
      pts.push([X[i], lo[i]]); pts.push([X[i], hi[i]]);
      scale = Math.max(scale, Math.abs(lo[i]), Math.abs(hi[i]));
    }
    const tol = 1e-9 * scale;
    let mn = null, mx = null;
    for (let a = 0; a < pts.length; a++) {
      for (let b = a + 1; b < pts.length; b++) {
        if (pts[a][0] === pts[b][0]) continue;
        const m = (pts[b][1] - pts[a][1]) / (pts[b][0] - pts[a][0]);
        const c = pts[a][1] - m * pts[a][0];
        let ok = true;
        for (let i = 0; i < X.length; i++) {
          const v = c + m * X[i];
          if (v < lo[i] - tol || v > hi[i] + tol) { ok = false; break; }
        }
        if (!ok) continue;
        if (!mn || m < mn.m) mn = { m: m, c: c };
        if (!mx || m > mx.m) mx = { m: m, c: c };
      }
    }
    return mn ? { min: mn, max: mx } : null;
  }
  // tab: y | lg | ln | sq. Returns X, Y and the half-length dY of each error bar, or an error message.
  function transform(tab, x, y, dy) {
    const X = [], Y = [], dY = [];
    for (let i = 0; i < x.length; i++) {
      const up = y[i] + Math.abs(dy[i]);
      let Yi, Yu;
      if (tab === 'lg') {
        if (!(x[i] > 0) || !(y[i] > 0)) return { error: 'A logarithm needs positive numbers: check row ' + (i + 1) + '.' };
        X.push(Math.log10(x[i])); Yi = Math.log10(y[i]); Yu = Math.log10(up);
      } else if (tab === 'ln') {
        if (!(y[i] > 0)) return { error: 'A logarithm needs positive numbers: check y in row ' + (i + 1) + '.' };
        X.push(x[i]); Yi = Math.log(y[i]); Yu = Math.log(up);
      } else if (tab === 'sq') {
        X.push(x[i]); Yi = y[i] * y[i]; Yu = up * up;
      } else {
        X.push(x[i]); Yi = y[i]; Yu = up;
      }
      Y.push(Yi); dY.push(Math.abs(Yu - Yi));
    }
    return { X: X, Y: Y, dY: dY };
  }
  function analyse(tab, x, y, dy) {
    const t = transform(tab, x, y, dy);
    if (t.error) return { error: t.error };
    const best = lsq(t.X, t.Y);
    if (!best) return { error: 'All the x values are the same, so no line can be drawn.' };
    const lo = t.Y.map((v, i) => v - t.dY[i]), hi = t.Y.map((v, i) => v + t.dY[i]);
    const ex = extremeLines(t.X, lo, hi);
    let worst = null;
    if (ex) worst = Math.abs(ex.min.m - best.m) >= Math.abs(ex.max.m - best.m) ? ex.min : ex.max;
    return { X: t.X, Y: t.Y, dY: t.dY, lo: lo, hi: hi, best: best, worst: worst };
  }
  // </math>

  const PRESETS = {
    pendulum: { x: [0.300, 0.400, 0.500, 0.600, 0.700, 0.800], y: [1.100, 1.269, 1.418, 1.556, 1.679, 1.797], dy: [0.005, 0.005, 0.005, 0.005, 0.005, 0.005], xl: 'l / m', yl: 'T / s', tab: 'sq' },
    discharge: { x: [10, 20, 30, 40, 50, 60], y: [8.0, 5.4, 3.6, 2.4, 1.6, 1.1], dy: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1], xl: 't / s', yl: 'V / V', tab: 'ln' },
    power: { x: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], y: [105, 158, 198, 238, 268, 297], dy: [3, 3, 3, 3, 3, 3], xl: 'x', yl: 'y', tab: 'lg' },
    blank: { x: [1, 2, 3, 4, 5, 6], y: [3.1, 4.9, 7.2, 8.8, 11.1, 13.0], dy: [0.4, 0.4, 0.4, 0.4, 0.4, 0.4], xl: 'x', yl: 'y', tab: 'y' }
  };

  W.register('phys-bestfit', function (el, opts) {
    const { body } = W.frame(el, 'Best-fit line and worst acceptable line', 'Edit the table to see how the gradient and its uncertainty change');
    const notes = [];
    const presetName = PRESETS[opts.preset] ? opts.preset : (opts.preset ? (notes.push('The preset must be pendulum, discharge, power or blank, so discharge is used.'), 'discharge') : 'discharge');
    const P = PRESETS[presetName];

    // Starting data: the preset, or comma lists from the attributes
    const list = (s) => String(s).split(',').map((t) => t.trim()).filter((t) => t !== '');
    let rows = P.x.map((v, i) => [String(v), String(P.y[i]), String(P.dy[i])]);
    if (opts.x !== undefined || opts.y !== undefined) {
      const xs = list(opts.x || ''), ys = list(opts.y || '');
      let ds = list(opts.dy || '');
      const nn = Math.min(xs.length, ys.length, 10);
      const bad = xs.concat(ys, ds).some((t) => !isFinite(parseFloat(t)));
      if (bad || nn < 3) {
        notes.push('The data attributes need at least three numbers each (x and y), so the preset table is used.');
      } else {
        if (ds.length === 1) ds = Array(nn).fill(ds[0]);
        if (ds.length < nn) { notes.push('The uncertainties were missing or too few, so ±5% of each y is used.'); ds = ys.map((t) => String(+(Math.abs(parseFloat(t)) * 0.05).toPrecision(2))); }
        rows = [];
        for (let i = 0; i < nn; i++) rows.push([xs[i], ys[i], ds[i]]);
      }
    }
    const names = (s, d) => {
      const t = String(s || d);
      const k = t.indexOf(' / ');
      return k > 0 ? { q: t.slice(0, k).trim(), u: t.slice(k + 3).trim() } : { q: t.trim(), u: '' };
    };
    const xn = names(opts.xlabel, P.xl), yn = names(opts.ylabel, P.yl);
    const tabList = [['y', 'y against x'], ['lg', 'lg y against lg x'], ['ln', 'ln y against x']];
    if (presetName === 'pendulum' || opts.tab === 'sq') tabList.push(['sq', 'y² against x']);
    const st = { tab: tabList.some((t) => t[0] === opts.tab) ? opts.tab : (tabList.some((t) => t[0] === P.tab) ? P.tab : 'y') };

    const err = W.h('div', { class: 'w-err', style: { display: notes.length ? '' : 'none' } }, notes.join(' '));

    // Tabs
    const tabRow = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Which graph to plot' });
    const btns = tabList.map(([v, label]) => W.h('button', { class: 'w-tab', type: 'button', onclick: () => { st.tab = v; syncTabs(); update(); } }, label));
    const syncTabs = () => btns.forEach((b, i) => b.setAttribute('aria-pressed', String(tabList[i][0] === st.tab)));
    btns.forEach((b) => tabRow.append(b));
    syncTabs();

    // Table of x, y and Δy
    const head = (txt) => W.h('th', { scope: 'col' }, txt);
    const xh = xn.u ? xn.q + ' / ' + xn.u : xn.q, yh = yn.u ? yn.q + ' / ' + yn.u : yn.q;
    const tbody = W.h('tbody', {});
    const inputs = [];
    function addRow(vals) {
      const i = inputs.length;
      const mk = (col, v, label) => {
        const inp = W.h('input', { type: 'text', inputmode: 'decimal', value: v, 'aria-label': label + ', row ' + (i + 1), style: { width: '100%', minWidth: '3.5em' } });
        inp.addEventListener('input', update);
        return inp;
      };
      const r = [mk(0, vals[0], 'x'), mk(1, vals[1], 'y'), mk(2, vals[2], 'uncertainty in y')];
      inputs.push(r);
      tbody.append(W.h('tr', {}, W.h('td', {}, r[0]), W.h('td', {}, r[1]), W.h('td', {}, r[2])));
    }
    rows.forEach(addRow);
    const table = W.h('table', { style: { width: '100%', tableLayout: 'fixed' } }, W.h('thead', {}, W.h('tr', {}, head(xh), head(yh), head('Δ' + (yn.q.length <= 2 ? yn.q : 'y') + (yn.u ? ' / ' + yn.u : '')))), tbody);
    const addBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { if (inputs.length < 10) { const last = inputs[inputs.length - 1]; addRow(['', '', last ? last[2].value : '']); update(); } } }, 'Add row');
    const delBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { if (inputs.length > 3) { inputs.pop(); tbody.lastChild.remove(); update(); } } }, 'Remove row');
    const resetBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { while (inputs.length) { inputs.pop(); tbody.lastChild.remove(); } rows.forEach(addRow); update(); } }, 'Reset');

    body.append(tabRow, table, W.h('div', { class: 'w-row' }, addBtn, delBtn, resetBtn));

    // Graph
    let model = null;
    const c = W.canvas(body, {
      height: 300,
      label: 'Graph of the data with the best-fit line and the worst acceptable line',
      describe() {
        if (!model) return 'No graph yet: the table needs at least three complete rows of numbers.';
        const m = model, nm = labels();
        let t = 'Graph of ' + nm.y + ' against ' + nm.x + ' with ' + m.X.length + ' points, each with an error bar. Best-fit line: gradient ' + W.fmt(m.best.m, 3) + ', intercept ' + W.fmt(m.best.c, 3) + '.';
        t += m.worst ? ' Worst acceptable line (dashed): gradient ' + W.fmt(m.worst.m, 3) + ', intercept ' + W.fmt(m.worst.c, 3) + '.' : ' No straight line passes through every error bar, so there is no worst acceptable line.';
        return t;
      },
      draw(ctx, w, h, col) {
        if (!model) {
          ctx.fillStyle = col.ink3; ctx.font = '13px ' + (col.font || 'sans-serif');
          ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
          ctx.fillText('Fix the table to see the graph.', w / 2, h / 2);
          return;
        }
        const m = model;
        const nX = m.X.length;
        let xmin = Infinity, xmax = -Infinity;
        for (let i = 0; i < nX; i++) { xmin = Math.min(xmin, m.X[i]); xmax = Math.max(xmax, m.X[i]); }
        const span = (xmax - xmin) || 1;
        let x0 = xmin - 0.08 * span, x1 = xmax + 0.08 * span;
        if (x0 > 0 && x0 <= 1.2 * span + 0.0) x0 = 0;                            // show the vertical axis at the left edge when it is near the data (its tick labels then sit outside the plot, clear of the lines)
        if (x1 < 0 && -x1 <= 1.2 * span) x1 = 0.04 * span;
        let ylo = Infinity, yhi = -Infinity;
        const see = (v) => { ylo = Math.min(ylo, v); yhi = Math.max(yhi, v); };
        for (let i = 0; i < nX; i++) { see(m.lo[i]); see(m.hi[i]); }
        const xe = xmax + 0.02 * span;                                             // lines stop just past the last point, so they do not run through the x-axis tick labels
        [m.best, m.worst].forEach((L) => { if (L) { see(L.c + L.m * x0); see(L.c + L.m * xe); } });
        const ys = (yhi - ylo) || 1;
        const view = { x0: x0, x1: x1, y0: ylo - 0.08 * ys, y1: yhi + 0.10 * ys };
        const names2 = labels();
        const ax = W.axes(ctx, w, h, view, col, { pad: { l: 52, r: 14, t: 24, b: 40 }, zeroX: false });
        const { X, Y, pad } = ax;
        ctx.save();
        ctx.fillStyle = col.ink2; ctx.font = 'italic 12px ' + (col.font || 'sans-serif');
        ctx.textAlign = 'left'; ctx.textBaseline = 'top'; ctx.fillText(names2.y, pad.l + 4, 4);
        ctx.textAlign = 'center'; ctx.textBaseline = 'bottom'; ctx.fillText(names2.x, pad.l + (w - pad.l - pad.r) / 2, h - 4);
        ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
        // best fit and worst acceptable lines
        const line = (L, colr, dash, wd) => {
          ctx.strokeStyle = colr; ctx.lineWidth = wd; ctx.setLineDash(dash);
          ctx.beginPath(); ctx.moveTo(X(x0), Y(L.c + L.m * x0)); ctx.lineTo(X(xe), Y(L.c + L.m * xe)); ctx.stroke();
          ctx.setLineDash([]);
        };
        if (m.worst) line(m.worst, col.sc2, [6, 4], 2);
        line(m.best, col.sc, [], 2.5);
        // error bars and points
        ctx.strokeStyle = col.ink; ctx.lineWidth = 1.3;
        for (let i = 0; i < nX; i++) {
          const px = X(m.X[i]);
          ctx.beginPath();
          ctx.moveTo(px, Y(m.lo[i])); ctx.lineTo(px, Y(m.hi[i]));
          ctx.moveTo(px - 4, Y(m.lo[i])); ctx.lineTo(px + 4, Y(m.lo[i]));
          ctx.moveTo(px - 4, Y(m.hi[i])); ctx.lineTo(px + 4, Y(m.hi[i]));
          ctx.stroke();
          ctx.beginPath();
          ctx.moveTo(px - 4, Y(m.Y[i])); ctx.lineTo(px + 4, Y(m.Y[i]));
          ctx.moveTo(px, Y(m.Y[i]) - 4); ctx.lineTo(px, Y(m.Y[i]) + 4);
          ctx.stroke();
        }
        ctx.restore();
      }
    });

    // Legend (below the graph, off the curves)
    const sw = (colour, dashed) => W.h('span', { 'aria-hidden': 'true', style: { display: 'inline-block', width: '22px', height: '0', verticalAlign: 'middle', marginRight: '6px', borderTop: '3px ' + (dashed ? 'dashed' : 'solid') + ' ' + colour } });
    const legend = W.h('div', { class: 'w-note', style: { display: 'flex', flexWrap: 'wrap', gap: '4px 16px' } },
      W.h('span', {}, sw('var(--sc)', false), 'best-fit line (least squares)'),
      W.h('span', {}, sw('var(--sc2)', true), 'worst acceptable line'),
      W.h('span', {}, '+ with bars: value ± uncertainty'));

    const ro = W.readout([['m', 'Gradient (best fit)'], ['mw', 'Gradient (worst acceptable)'], ['dm', 'Uncertainty in gradient'], ['c', 'Intercept (best fit)'], ['dc', 'Uncertainty in intercept'], ['k1', 'Constant'], ['k2', 'Second constant']]);
    const note = W.h('div', { class: 'w-note' });
    body.append(legend, ro.el, note, err);

    function labels() {
      const q = (n) => n.q, u = (n) => n.u;
      const pair = (qq, uu) => (uu ? qq + ' / ' + uu : qq);
      if (st.tab === 'lg') return { x: 'lg (' + pair(q(xn), u(xn)) + ')', y: 'lg (' + pair(q(yn), u(yn)) + ')' };
      if (st.tab === 'ln') return { x: pair(q(xn), u(xn)), y: 'ln (' + pair(q(yn), u(yn)) + ')' };
      if (st.tab === 'sq') return { x: pair(q(xn), u(xn)), y: pair(q(yn) + '²', u(yn) ? u(yn) + '²' : '') };
      return { x: pair(q(xn), u(xn)), y: pair(q(yn), u(yn)) };
    }
    const fmtU = (v, d) => (isFinite(v) ? W.fmt(v, d) : '—');
    // value ± uncertainty: the uncertainty to 2 s.f., the value to the same decimal place (25.0 ± 1.1, not 25 ± 1.1)
    const pm = (v, dv) => {
      if (!isFinite(v) || !isFinite(dv) || dv <= 0) return W.fmt(v, 3);
      const e = Math.floor(Math.log10(dv)) - 1;
      const sgn = (s) => s.replace('-', '−');
      if (e < 0) return sgn(v.toFixed(-e)) + ' ± ' + dv.toFixed(-e);
      const r = Math.pow(10, e);
      return sgn(String(Math.round(v / r) * r)) + ' ± ' + String(Math.round(dv / r) * r);
    };

    function readRows() {
      const out = [], bad = [];
      inputs.forEach((r, i) => {
        const v = r.map((inp) => parseFloat(String(inp.value).replace(/[−–]/g, '-')));
        if (!v.every((t) => isFinite(t))) { if (r.some((inp) => String(inp.value).trim() !== '')) bad.push(i + 1); return; }
        out.push(v);
      });
      return { out: out, bad: bad };
    }

    function update() {
      const { out, bad } = readRows();
      const msgs = notes.slice();
      if (bad.length) msgs.push('Row ' + bad.join(', ') + ' contains something that is not a number, so it is left out.');
      let res = null;
      if (out.length < 3) {
        msgs.push('At least three complete rows are needed to draw a line.');
      } else {
        res = analyse(st.tab, out.map((r) => r[0]), out.map((r) => r[1]), out.map((r) => r[2]));
        if (res.error) { msgs.push(res.error); }
      }
      model = res && !res.error ? res : null;
      err.textContent = msgs.join(' ');
      err.style.display = msgs.length ? '' : 'none';
      ['m', 'mw', 'dm', 'c', 'dc', 'k1', 'k2'].forEach((k) => ro.set(k, '—'));
      note.textContent = 'Fix the table to see the graph.';
      if (model) {
        const b = model.best, w = model.worst;
        ro.set('m', W.fmt(b.m, 4));
        ro.set('c', W.fmt(b.c, 4));
        if (w) {
          const dm = Math.abs(b.m - w.m), dc = Math.abs(b.c - w.c);
          ro.set('mw', W.fmt(w.m, 4));
          ro.set('dm', '± ' + fmtU(dm, 2) + ' (' + fmtU(dm / Math.abs(b.m) * 100, 2) + '%)');
          ro.set('dc', '± ' + fmtU(dc, 2));
          derived(b, w, dm, dc);
          note.textContent = 'The uncertainty in the gradient is the difference between the best-fit gradient and the worst acceptable gradient. Edit a value or an uncertainty and watch both lines. The widget uses a least-squares line, so its numbers differ a little from a line drawn by eye.';
        } else {
          ro.set('mw', 'none');
          derived(b, null, NaN, NaN);
          note.textContent = 'No straight line passes through every error bar, so there is no worst acceptable line. Either the error bars are too small for the scatter of the points, or the graph is not a straight line. Try a different graph, or larger uncertainties.';
        }
      }
      c.redraw();
    }

    function derived(b, w, dm, dc) {
      const have = isFinite(dm);
      const hint = (name) => 'show the “' + name + '” graph';
      if (presetName === 'pendulum') {
        if (st.tab === 'sq') {
          const g = 4 * Math.PI * Math.PI / b.m;
          ro.set('k1', 'g = 4π² / gradient = ' + (have ? pm(g, g * dm / Math.abs(b.m)) : W.fmt(g, 3)) + ' m s⁻²');
          ro.set('k2', 'T² = (4π²/g) l: the line should pass through the origin');
        } else ro.set('k1', hint('y² against x'));
      } else if (presetName === 'discharge') {
        if (st.tab === 'ln') {
          const rc = -1 / b.m, v0 = Math.exp(b.c);
          ro.set('k1', 'RC = −1 / gradient = ' + (have ? pm(rc, rc * dm / Math.abs(b.m)) : W.fmt(rc, 3)) + ' s');
          ro.set('k2', 'V₀ = e^intercept = ' + (have ? pm(v0, v0 * dc) : W.fmt(v0, 3)) + ' V');
        } else ro.set('k1', hint('ln y against x'));
      } else if (presetName === 'power') {
        if (st.tab === 'lg') {
          const a = Math.pow(10, b.c);
          ro.set('k1', 'n = gradient = ' + (have ? pm(b.m, dm) : W.fmt(b.m, 3)));
          ro.set('k2', 'a = 10^intercept = ' + (have && w ? pm(a, Math.abs(a - Math.pow(10, w.c))) : W.fmt(a, 3)));
        } else ro.set('k1', hint('lg y against lg x'));
      } else {
        ro.set('k1', 'Gradient and intercept above');
      }
    }
    update();
  });
})();
