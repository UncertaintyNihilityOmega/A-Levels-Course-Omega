/* slopefield: the direction field of dy/dx = f(x, y) with solution curves drawn by RK4 through any clicked or dragged point.
   data-f "x/y" (use x and y)  data-x "-4,4"  data-y "-4,4"  data-start "0,2" (first point, optional) */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const pair = (s, dflt) => {
    if (s == null || String(s).trim() === '') return dflt;
    const p = String(s).replace(/[−–]/g, '-').split(',').map((t) => parseFloat(t));
    return p.length >= 2 && isFinite(p[0]) && isFinite(p[1]) && p[1] > p[0] ? [p[0], p[1]] : null;
  };
  const MAXKEEP = 6;

  W.register('slopefield', function (el, o) {
    const { body } = W.frame(el, 'Slope field', 'click or drag to draw a solution through a point');
    const warn = [];
    let xr = pair(o.x, [-4, 4]); if (!xr) { warn.push('data-x should look like "-4,4". Using -4 to 4.'); xr = [-4, 4]; }
    let yr = pair(o.y, [-4, 4]); if (!yr) { warn.push('data-y should look like "-4,4". Using -4 to 4.'); yr = [-4, 4]; }
    let src = String(o.f || o.fn || 'x - y').trim();
    let fn = null;
    function compile(text) {
      const p = W.parse(text);
      const vs = p.vars instanceof Set ? [...p.vars] : Array.isArray(p.vars) ? p.vars : Object.keys(p.vars || {});
      const extra = vs.filter((v) => v !== 'x' && v !== 'y');
      if (extra.length) throw new Error(`only x and y can be used, not ${extra.join(', ')}`);
      return (x, y) => { const v = p.f({ x, y }); return typeof v === 'number' ? v : NaN; };
    }
    try { fn = compile(src); } catch (e) { warn.push(`Can't read dy/dx = ${src}: ${e.message}. Using x − y.`); src = 'x - y'; fn = compile(src); }

    const startP = pair(o.start, null) || [xr[0] + (xr[1] - xr[0]) * 0.5, yr[0] + (yr[1] - yr[0]) * 0.5];
    let curves = [{ x: clamp(startP[0], xr[0], xr[1]), y: clamp(startP[1], yr[0], yr[1]) }];

    /* controls */
    const err = W.h('div', { class: 'w-err', role: 'status' });
    const showErr = (t) => { err.textContent = t; err.style.display = t ? '' : 'none'; };
    showErr(warn.join(' '));
    const fld = W.field({ label: 'dy/dx =', value: src, type: 'text', width: '12em', oninput: () => {
      const t = fld.input.value.trim();
      try { fn = compile(t); src = t; showErr(''); redraw(); } catch (e) { showErr(`Can't read that: ${e.message}. Use x and y, for example x*y or 0.05y(10-y).`); }
    } });
    const clear = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm' }, 'Clear curves');
    clear.addEventListener('click', () => { curves = curves.slice(-1); redraw(); });
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } }, fld.el, clear), err);

    const pad = { l: 40, r: 14, t: 12, b: 28 };
    const geom = { w: 300, h: 300 };
    const toData = (px, py) => [xr[0] + (px - pad.l) / (geom.w - pad.l - pad.r) * (xr[1] - xr[0]), yr[1] - (py - pad.t) / (geom.h - pad.t - pad.b) * (yr[1] - yr[0])];

    // RK4 solution through (x0, y0), forward then backward; stops at the edge of the window or where f is not defined
    function solve(x0, y0) {
      const span = xr[1] - xr[0], ymax = (yr[1] - yr[0]) * 20;
      const pts = [];
      for (const dir of [1, -1]) {
        const h = dir * span / 500; let x = x0, y = y0; const side = [];
        for (let i = 0; i < 700; i++) {
          const k1 = fn(x, y), k2 = fn(x + h / 2, y + h * k1 / 2), k3 = fn(x + h / 2, y + h * k2 / 2), k4 = fn(x + h, y + h * k3);
          const yn = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6;
          if (!isFinite(yn) || Math.abs(yn) > ymax) break;
          x += h; y = yn;
          if (x < xr[0] - span * 0.02 || x > xr[1] + span * 0.02) break;
          side.push([x, y]);
        }
        if (dir < 0) side.reverse();
        if (dir > 0) pts.push([x0, y0], ...side); else pts.unshift(...side);
      }
      return pts;
    }

    const cv = W.canvas(body, { height: 310, draw });
    cv.wrap.setAttribute('role', 'img');
    cv.wrap.style.touchAction = 'none';
    cv.wrap.style.cursor = 'crosshair';
    const R = W.readout([['pt', 'Solution through'], ['slope', 'Gradient there, dy/dx']]);
    body.append(R.el, W.h('div', { class: 'w-note' }, 'Each short line shows the gradient of a solution at its point. Click to start a new curve; drag to move the latest one. A curve stops where dy/dx is not defined.'));

    function readout() {
      const c = curves[curves.length - 1], s = fn(c.x, c.y);
      R.set('pt', `(${W.fmt(c.x, 3)}, ${W.fmt(c.y, 3)})`);
      R.set('slope', isFinite(s) ? W.fmt(s, 3) : 'not defined here');
      cv.wrap.setAttribute('aria-label', `Slope field of dy/dx = ${src}. The latest solution curve passes through (${W.fmt(c.x, 3)}, ${W.fmt(c.y, 3)}).`);
    }
    function redraw() { readout(); cv.redraw(); }

    W.drag(cv.wrap, {
      hit(px, py) {
        if (px < pad.l || px > geom.w - pad.r || py < pad.t || py > geom.h - pad.b) return null;
        const [x, y] = toData(px, py);
        curves.push({ x, y }); if (curves.length > MAXKEEP) curves.shift();
        redraw(); return { i: curves.length - 1 };
      },
      move(t, px, py) {
        const [x, y] = toData(clamp(px, pad.l, geom.w - pad.r), clamp(py, pad.t, geom.h - pad.b));
        const c = curves[t.i]; if (c) { c.x = x; c.y = y; redraw(); }
      },
      end() {},
    });

    function draw(ctx, w, h, c) {
      geom.w = w; geom.h = h;
      const A = W.axes(ctx, w, h, { x0: xr[0], x1: xr[1], y0: yr[0], y1: yr[1] }, c, { pad, xlabel: 'x', ylabel: 'y' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      // the field
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      const nx = clamp(Math.round(pw / 26), 8, 30), ny = clamp(Math.round(ph / 26), 8, 24);
      const L = 0.42 * Math.min(pw / nx, ph / ny), kx = pw / (xr[1] - xr[0]), ky = ph / (yr[1] - yr[0]);
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.4; ctx.globalAlpha = 0.85;
      for (let i = 0; i < nx; i++) for (let j = 0; j < ny; j++) {
        const x = xr[0] + (i + 0.5) / nx * (xr[1] - xr[0]), y = yr[0] + (j + 0.5) / ny * (yr[1] - yr[0]);
        const m = fn(x, y);
        if (!isFinite(m)) continue;
        const dxp = kx, dyp = -m * ky, n = Math.hypot(dxp, dyp), ux = dxp / n * L, uy = dyp / n * L;
        ctx.beginPath(); ctx.moveTo(X(x) - ux, Y(y) - uy); ctx.lineTo(X(x) + ux, Y(y) + uy); ctx.stroke();
      }
      ctx.globalAlpha = 1;
      // solution curves: older ones fainter, the latest in the course colour
      curves.forEach((cu, k) => {
        const last = k === curves.length - 1, pts = solve(cu.x, cu.y);
        ctx.beginPath();
        pts.forEach(([x, y], q) => (q ? ctx.lineTo(X(x), Y(y)) : ctx.moveTo(X(x), Y(y))));
        ctx.strokeStyle = last ? c.sc : c.sc2; ctx.globalAlpha = last ? 1 : 0.55; ctx.lineWidth = last ? 2.8 : 2; ctx.stroke(); ctx.globalAlpha = 1;
        ctx.beginPath(); ctx.arc(X(cu.x), Y(cu.y), last ? 5 : 3.5, 0, Math.PI * 2); ctx.fillStyle = last ? c.red : c.sc2; ctx.fill();
      });
      ctx.restore();
    }
    redraw();
  });
})();
