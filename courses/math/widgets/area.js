/* area: strips under a curve (rectangles or trapezia) and discs for a volume of revolution.
   data-f "x^2"  data-x "1,3"  data-n 4  data-mode riemann | trapezium | volume  data-y "ymin,ymax" (optional) */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const num = (v, d) => { const n = parseFloat(v); return isFinite(n) ? n : d; };
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const pair = (s) => {
    if (s == null || String(s).trim() === '') return null;
    const p = String(s).replace(/[−–]/g, '-').split(',').map((t) => parseFloat(t));
    return p.length >= 2 && isFinite(p[0]) && isFinite(p[1]) && p[1] > p[0] ? [p[0], p[1]] : 'bad';
  };

  W.register('area', function (el, o) {
    const modes = ['riemann', 'trapezium', 'volume'];
    const mode = modes.includes(String(o.mode)) ? String(o.mode) : 'riemann';
    const warn = [];
    const src = String(o.f || o.fn || 'x^2').trim();
    let fn = null;
    try { fn = W.parse(src).f; } catch (e) { warn.push(`Can't read f(x) = ${src}: ${e.message}. Using x².`); fn = W.parse('x^2').f; }
    const f = (x) => { try { const v = fn({ x }); return typeof v === 'number' ? v : NaN; } catch (e) { return NaN; } };
    let xr = pair(o.x);
    if (xr === 'bad' || !xr) { if (xr === 'bad') warn.push('data-x should look like "1,3". Using 0 to 2.'); xr = [0, 2]; }
    const [a, b] = xr;
    const MAXN = mode === 'volume' ? 40 : 60;
    let n = Math.round(clamp(num(o.n, mode === 'volume' ? 6 : 4), 1, MAXN));
    let rule = 'left';

    const titles = {
      riemann: ['Area under a curve', 'more strips, better estimate'],
      trapezium: ['Trapezium rule', 'more strips, better estimate'],
      volume: ['Volume of revolution', 'a stack of discs about the x-axis'],
    };
    const { body } = W.frame(el, titles[mode][0], titles[mode][1]);

    // exact value (Simpson with many intervals: far below the 4 s.f. we display)
    const simpson = (g, lo, hi, m = 2000) => {
      const h = (hi - lo) / m; let s = g(lo) + g(hi);
      for (let i = 1; i < m; i++) s += g(lo + i * h) * (i % 2 ? 4 : 2);
      return s * h / 3;
    };
    const exact = mode === 'volume' ? Math.PI * simpson((x) => f(x) ** 2, a, b) : simpson(f, a, b);

    // y range from samples
    let ys = [];
    for (let i = 0; i <= 200; i++) { const y = f(a + (b - a) * i / 200); if (isFinite(y)) ys.push(y); }
    let yr = pair(o.y);
    if (!isFinite(exact) || !ys.length) warn.push('f(x) is not defined everywhere between the limits, so the figures below may be missing.');
    if (yr === 'bad' || !yr) {
      let lo = ys.length ? Math.min(...ys) : -1, hi = ys.length ? Math.max(...ys) : 1;
      if (mode === 'volume') { const m = Math.max(Math.abs(lo), Math.abs(hi), 1e-9); lo = -m; hi = m; } else { lo = Math.min(lo, 0); hi = Math.max(hi, 0); }
      if (!(hi - lo > 1e-9)) { lo -= 1; hi += 1; }
      const pad = (hi - lo) * 0.1;
      yr = [mode === 'volume' || lo < 0 ? lo - pad : lo, hi + pad];
    }

    /* controls */
    const ctl = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } });
    const nSl = W.sliderNum({ label: mode === 'volume' ? 'Number of discs' : 'Number of strips', min: 1, max: MAXN, step: 1, value: n,
      oninput: (v) => { n = Math.round(clamp(v, 1, MAXN)); update(); } });
    ctl.append(nSl.el);
    let ruleBtns = [];
    if (mode === 'riemann') {
      const seg = W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Height of each rectangle' });
      for (const [k, t] of [['left', 'Left edge'], ['right', 'Right edge'], ['mid', 'Midpoint']]) {
        const bt = W.h('button', { type: 'button', class: 'w-tab', role: 'tab', 'aria-selected': String(k === rule) }, t);
        bt.addEventListener('click', () => { rule = k; ruleBtns.forEach(([kk, bb]) => bb.setAttribute('aria-selected', String(kk === rule))); update(); });
        ruleBtns.push([k, bt]); seg.append(bt);
      }
      ctl.append(seg);
    }
    body.append(ctl);
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const cv = W.canvas(body, { height: 270, draw });
    cv.wrap.setAttribute('role', 'img');
    const R = W.readout(mode === 'volume'
      ? [['est', 'Volume of the discs'], ['exact', 'Exact volume'], ['err', 'Difference']]
      : [['est', 'Estimate'], ['exact', 'Exact area'], ['err', 'Error']]);
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, mode === 'volume'
      ? `Raise the number of discs: the stack's volume closes in on π∫y² dx = ${W.fmt(exact, 4)}.`
      : mode === 'trapezium'
        ? 'Raise the number of strips and watch the error shrink. For a curve that bends upwards the trapezia lie above it: an overestimate.'
        : 'Switch between left edge, right edge and midpoint. For an increasing curve the left edges give an underestimate and the right edges an overestimate.'));

    const dx = () => (b - a) / n;
    function estimate() {
      const d = dx(); let s = 0;
      for (let i = 0; i < n; i++) {
        const x0 = a + i * d, x1 = x0 + d;
        if (mode === 'riemann') s += f(rule === 'left' ? x0 : rule === 'right' ? x1 : (x0 + x1) / 2) * d;
        else if (mode === 'trapezium') s += (f(x0) + f(x1)) / 2 * d;
        else s += Math.PI * f(x0 + d / 2) ** 2 * d;
      }
      return s;
    }
    function update() {
      const est = estimate(), err = est - exact;
      const unit = mode === 'volume' ? ' cubic units' : ' square units';
      R.set('est', isFinite(est) ? W.fmt(est, 4) + unit : 'not defined');
      R.set('exact', isFinite(exact) ? W.fmt(exact, 4) + unit : 'not defined');
      const tiny = Math.abs(exact) * 1e-6 + 1e-12;
      R.set('err', !isFinite(err) ? '—' : Math.abs(err) < tiny ? 'none' : `${W.fmt(Math.abs(err), 3)} (${err > 0 ? 'over' : 'under'}estimate)`);
      cv.wrap.setAttribute('aria-label', `${titles[mode][0]} of ${src} from x = ${a} to ${b} with ${n} ${mode === 'volume' ? 'discs' : 'strips'}: estimate ${isFinite(est) ? W.fmt(est, 4) : 'undefined'}, exact ${isFinite(exact) ? W.fmt(exact, 4) : 'undefined'}.`);
      cv.redraw();
    }

    function draw(ctx, w, h, c) {
      const pad = { l: 42, r: 16, t: 12, b: 26 };
      const A = W.axes(ctx, w, h, { x0: a - (b - a) * 0.08, x1: b + (b - a) * 0.08, y0: yr[0], y1: yr[1] }, c, { pad, xlabel: 'x', ylabel: mode === 'volume' ? 'radius' : 'y' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      const d = dx();
      ctx.lineWidth = 1.4;
      for (let i = 0; i < n; i++) {
        const x0 = a + i * d, x1 = x0 + d;
        if (mode === 'volume') {
          const r = f(x0 + d / 2);
          if (!isFinite(r)) continue;
          const px0 = X(x0), px1 = X(x1), top = Y(Math.abs(r)), bot = Y(-Math.abs(r));
          const ex = Math.min(9, (px1 - px0) * 0.35);
          ctx.globalAlpha = 0.28; ctx.fillStyle = c.sc2;
          ctx.fillRect(px0, top, px1 - px0, bot - top);
          ctx.globalAlpha = 0.55; ctx.beginPath(); ctx.ellipse(px1, (top + bot) / 2, ex, (bot - top) / 2, 0, 0, Math.PI * 2); ctx.fill();
          ctx.globalAlpha = 1; ctx.strokeStyle = c.sc2;
          ctx.strokeRect(px0 + 0.5, top, px1 - px0, bot - top);
          ctx.beginPath(); ctx.ellipse(px1, (top + bot) / 2, ex, (bot - top) / 2, 0, 0, Math.PI * 2); ctx.stroke();
        } else {
          const y0 = f(x0), y1 = f(x1);
          let pts;
          if (mode === 'riemann') {
            const hgt = f(rule === 'left' ? x0 : rule === 'right' ? x1 : (x0 + x1) / 2);
            if (!isFinite(hgt)) continue;
            pts = [[x0, 0], [x0, hgt], [x1, hgt], [x1, 0]];
          } else {
            if (!isFinite(y0) || !isFinite(y1)) continue;
            pts = [[x0, 0], [x0, y0], [x1, y1], [x1, 0]];
          }
          ctx.beginPath(); pts.forEach(([x, y], k) => (k ? ctx.lineTo(X(x), Y(y)) : ctx.moveTo(X(x), Y(y)))); ctx.closePath();
          ctx.globalAlpha = 0.26; ctx.fillStyle = c.sc2; ctx.fill(); ctx.globalAlpha = 1;
          ctx.strokeStyle = c.sc2; ctx.stroke();
        }
      }
      // the curve (and its reflection for a solid)
      const N = Math.max(80, Math.round(w - pad.l - pad.r));
      for (const sgn of mode === 'volume' ? [1, -1] : [1]) {
        ctx.beginPath(); let pen = false;
        for (let i = 0; i <= N; i++) {
          const x = a + (b - a) * i / N, y = f(x);
          if (!isFinite(y)) { pen = false; continue; }
          const px = X(x), py = Y(sgn * y);
          if (pen) ctx.lineTo(px, py); else { ctx.moveTo(px, py); pen = true; }
        }
        ctx.strokeStyle = c.sc; ctx.lineWidth = 2.4; ctx.setLineDash(sgn < 0 ? [5, 4] : []); ctx.stroke(); ctx.setLineDash([]);
      }
      // limits
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 4]);
      for (const x of [a, b]) { ctx.beginPath(); ctx.moveTo(Math.round(X(x)) + 0.5, pad.t); ctx.lineTo(Math.round(X(x)) + 0.5, h - pad.b); ctx.stroke(); }
      ctx.setLineDash([]);
      ctx.restore();
    }
    update();
  });
})();
