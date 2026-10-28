/* widgets/bio-sav.js: surface area to volume ratio (data-shape="cube|cuboid|cylinder") with an "Agar block" tab.
   Used in bio.movement. Facts: cube SA = 6L^2, V = L^3, SA:V = 6/L; cylinder SA = 2*pi*r^2 + 2*pi*r*h, V = pi*r^2*h.
   Agar tab is a MODEL: an indicator front moves inwards from every face at a constant 0.1 cm per minute
   (real diffusion slows down as the distance grows, so real times are longer than the model's). */
(function () {
  'use strict';

  const RATE = 0.1;                                   // cm per minute (model)
  const SHAPES = ['cube', 'cuboid', 'cylinder'];
  const NAMES = { cube: 'Cube', cuboid: 'Cuboid', cylinder: 'Cylinder' };

  // ---- pure maths (also used by the test script) ------------------------------------------------------------
  function geom(shape, p) {
    if (shape === 'cylinder') {
      const r = p.r, h = p.len;
      return { sa: 2 * Math.PI * r * r + 2 * Math.PI * r * h, v: Math.PI * r * r * h };
    }
    const a = p.a, b = shape === 'cube' ? p.a : p.b, c = shape === 'cube' ? p.a : p.c;
    return { sa: 2 * (a * b + a * c + b * c), v: a * b * c };
  }
  function centreTime(shape, p) {                      // minutes for the front to reach the middle
    let half;
    if (shape === 'cylinder') half = Math.min(p.r, p.len / 2);
    else half = Math.min(p.a, shape === 'cube' ? p.a : p.b, shape === 'cube' ? p.a : p.c) / 2;
    return half / RATE;
  }
  function uncoloured(shape, p, t) {                   // fraction of the volume the front has not reached
    const d = RATE * t, pos = x => Math.max(0, x);
    const g = geom(shape, p);
    if (!(g.v > 0)) return 0;
    let v;
    if (shape === 'cylinder') v = Math.PI * Math.pow(pos(p.r - d), 2) * pos(p.len - 2 * d);
    else v = pos(p.a - 2 * d) * pos((shape === 'cube' ? p.a : p.b) - 2 * d) * pos((shape === 'cube' ? p.a : p.c) - 2 * d);
    return Math.min(1, v / g.v);
  }
  function sf(x, n) {
    n = n || 3;
    if (!isFinite(x)) return '–';
    if (x === 0) return '0';
    return String(Number(x.toPrecision(n)));
  }
  const num = (v, d, lo, hi) => { const x = Number(v); return isFinite(x) ? Math.min(hi, Math.max(lo, x)) : d; };

  if (typeof module !== 'undefined' && module.exports) module.exports = { geom, centreTime, uncoloured, sf };
  if (typeof W === 'undefined') return;

  function E(tag, props, ...kids) {
    const n = document.createElement(tag);
    for (const k in (props || {})) {
      const v = props[k];
      if (v == null) continue;
      if (k === 'class') n.className = v;
      else if (k === 'style') Object.assign(n.style, v);
      else if (k === 'text') n.textContent = v;
      else if (k.slice(0, 2) === 'on') n[k] = v;
      else n.setAttribute(k, v);
    }
    kids.forEach(c => { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return n;
  }

  W.register('bio-sav', function (el, opts) {
    const { body } = W.frame(el, 'Surface area to volume ratio', 'Change the size of a shape and watch SA:V');
    const S = {
      mode: opts && opts.mode === 'agar' ? 'agar' : 'shape',
      shape: SHAPES.indexOf(opts && opts.shape) >= 0 ? opts.shape : 'cube',
      p: { a: 2, b: 2, c: 1.5, r: 1, len: 3 }, t: 5
    };

    // ---- tabs: mode and shape (outside the area that is rebuilt) ----
    const modeTabs = E('div', { class: 'w-tabs', role: 'group', 'aria-label': 'What to show' });
    const shapeTabs = E('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Shape' });
    const mBtn = {}, sBtn = {};
    [['shape', 'SA:V'], ['agar', 'Agar block']].forEach(([k, label]) => {
      mBtn[k] = E('button', { type: 'button', class: 'w-tab', text: label, 'aria-pressed': S.mode === k ? 'true' : 'false',
        onclick: () => { S.mode = k; sync(); build(); } });
      modeTabs.appendChild(mBtn[k]);
    });
    SHAPES.forEach(k => {
      sBtn[k] = E('button', { type: 'button', class: 'w-tab', text: NAMES[k], 'aria-pressed': S.shape === k ? 'true' : 'false',
        onclick: () => { S.shape = k; sync(); build(); } });
      shapeTabs.appendChild(sBtn[k]);
    });
    body.appendChild(E('div', { class: 'w-row' }, modeTabs, shapeTabs));
    function sync() {
      Object.keys(mBtn).forEach(k => mBtn[k].setAttribute('aria-pressed', S.mode === k ? 'true' : 'false'));
      Object.keys(sBtn).forEach(k => sBtn[k].setAttribute('aria-pressed', S.shape === k ? 'true' : 'false'));
    }

    // ---- canvas ----
    const c = W.canvas(body, {
      height: 420,
      label: 'Drawing of the shape and a bar chart of surface area to volume ratio',
      describe: () => describe(),
      draw: (ctx, w, h, C) => draw(ctx, w, h, C)
    });

    const ctl = E('div', {});
    body.appendChild(ctl);
    const out = E('div', {});
    body.appendChild(out);
    const note = E('div', { class: 'w-note' });
    body.appendChild(note);
    let rd = null;

    function slider(label, key, min, max, step, unit) {
      const s = W.sliderNum({ label: label + ' (' + unit + ')', min, max, step, value: S.p[key],
        oninput: () => { S.p[key] = num(s.get(), S.p[key], min, max); update(); } });
      ctl.appendChild(s.el);
    }

    function build() {
      ctl.innerHTML = '';
      out.innerHTML = '';
      if (S.mode === 'agar') {
        const s = W.sliderNum({ label: 'Time since the block was put in the acid (minutes)', min: 0, max: 25, step: 1, value: S.t,
          oninput: () => { S.t = num(s.get(), S.t, 0, 25); update(); } });
        ctl.appendChild(s.el);
      }
      if (S.shape === 'cube') slider('Side length', 'a', 0.5, 5, 0.1, 'cm');
      else if (S.shape === 'cuboid') {
        slider('Length', 'a', 0.5, 5, 0.1, 'cm'); slider('Width', 'b', 0.5, 5, 0.1, 'cm'); slider('Height', 'c', 0.5, 5, 0.1, 'cm');
      } else { slider('Radius', 'r', 0.5, 2.5, 0.1, 'cm'); slider('Length', 'len', 0.5, 5, 0.1, 'cm'); }
      rd = S.mode === 'agar'
        ? W.readout([['sa', 'Surface area'], ['v', 'Volume'], ['ratio', 'SA:V'], ['tc', 'Time for the colour to reach the centre'], ['unc', 'Volume still uncoloured']])
        : W.readout([['sa', 'Surface area'], ['v', 'Volume'], ['ratio', 'SA:V as a ratio'], ['per', 'SA:V in cm⁻¹']]);
      out.appendChild(rd.el);
      note.textContent = S.mode === 'agar'
        ? 'Model: in this simulation the indicator front moves in from every face at a steady 0.1 cm per minute. Real diffusion slows down as the distance grows, so real times are longer. The bigger block has more volume to reach, so more of it is still uncoloured.'
        : 'Double the side: the volume rises 8 times but the surface only 4 times, so SA:V halves.';
      update();
    }

    function dims() {
      const p = S.p;
      return S.shape === 'cube' ? { a: p.a, b: p.a, c: p.a } : S.shape === 'cuboid' ? { a: p.a, b: p.b, c: p.c } : null;
    }
    function describe() {
      const g = geom(S.shape, S.p);
      let t = NAMES[S.shape] + ': surface area ' + sf(g.sa) + ' square centimetres, volume ' + sf(g.v) + ' cubic centimetres, SA to V ratio ' +
        sf(g.sa / g.v) + ' to 1. ';
      if (S.mode === 'agar') t += 'After ' + S.t + ' minutes ' + sf(uncoloured(S.shape, S.p, S.t) * 100) + ' percent of the volume is still uncoloured; the colour reaches the centre after ' +
        sf(centreTime(S.shape, S.p)) + ' minutes.';
      else t += 'The bar chart shows SA to V for cubes of side 1 to 5 cm: 6, 3, 2, 1.5 and 1.2.';
      return t;
    }

    function update() {
      const g = geom(S.shape, S.p);
      const r = g.sa / g.v;
      rd.set('sa', sf(g.sa) + ' cm²');
      rd.set('v', sf(g.v) + ' cm³');
      if (S.mode === 'agar') {
        rd.set('ratio', sf(r) + ' : 1');
        rd.set('tc', sf(centreTime(S.shape, S.p)) + ' min');
        rd.set('unc', sf(uncoloured(S.shape, S.p, S.t) * 100) + '% after ' + S.t + ' min');
      } else {
        rd.set('ratio', sf(r) + ' : 1');
        rd.set('per', sf(r) + ' cm⁻¹');
      }
      c.redraw();
    }

    // ---- drawing ----
    function poly(ctx, pts, fill, stroke) {
      ctx.beginPath();
      pts.forEach((q, i) => (i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1])));
      ctx.closePath();
      if (fill) { ctx.fillStyle = fill; ctx.fill(); }
      if (stroke) { ctx.strokeStyle = stroke; ctx.stroke(); }
    }
    function dashed(ctx, a, b, col) {
      ctx.save(); ctx.setLineDash([4, 3]); ctx.strokeStyle = col; ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.stroke(); ctx.restore();
    }

    function drawShape(ctx, w, hh, C) {
      const pcm = Math.max(1, Math.min((w - 20) / 7.3, (hh - 14) / 6.7));
      const xs = Math.max(8, (w - 7.1 * pcm) / 2), yb = hh - 6;
      ctx.lineWidth = 1.6;
      const shade = C.sc;
      if (S.shape !== 'cylinder') {
        const d = dims(), A = d.a * pcm, B = d.c * pcm, Cc = d.b * pcm; // front: length x height; depth: width
        const ox = 0.42 * Cc, oy = 0.30 * Cc;
        const fbl = [xs, yb], fbr = [xs + A, yb], ftl = [xs, yb - B], ftr = [xs + A, yb - B];
        const bbl = [xs + ox, yb - oy], bbr = [xs + A + ox, yb - oy], btl = [xs + ox, yb - B - oy], btr = [xs + A + ox, yb - B - oy];
        dashed(ctx, bbl, fbl, C.ink3); dashed(ctx, bbl, bbr, C.ink3); dashed(ctx, bbl, btl, C.ink3);
        ctx.globalAlpha = 0.22;
        poly(ctx, [ftl, ftr, btr, btl], shade, null);
        poly(ctx, [fbr, bbr, btr, ftr], shade, null);
        ctx.globalAlpha = 0.34;
        poly(ctx, [fbl, fbr, ftr, ftl], shade, null);
        ctx.globalAlpha = 1;
        ctx.lineWidth = 2;
        poly(ctx, [fbl, fbr, ftr, ftl], null, C.ink);
        poly(ctx, [ftl, ftr, btr, btl], null, C.ink);
        poly(ctx, [fbr, bbr, btr, ftr], null, C.ink);
      } else {
        const R = S.p.r * pcm, L = S.p.len * pcm;
        const ox = 0.42 * L, oy = 0.30 * L;
        const cx = xs + R, cy = yb - R;
        const phi = Math.atan2(-oy, ox), ln = Math.hypot(ox, oy) || 1;
        const nx = oy / ln, ny = ox / ln;
        // hidden half of the back circle (dashed), then the solid far half
        ctx.save(); ctx.setLineDash([4, 3]); ctx.strokeStyle = C.ink3;
        ctx.beginPath(); ctx.arc(cx + ox, cy - oy, R, phi + Math.PI / 2, phi + 1.5 * Math.PI); ctx.stroke(); ctx.restore();
        ctx.globalAlpha = 0.22;
        poly(ctx, [[cx + nx * R, cy + ny * R], [cx + ox + nx * R, cy - oy + ny * R], [cx + ox - nx * R, cy - oy - ny * R], [cx - nx * R, cy - ny * R]], shade, null);
        ctx.beginPath(); ctx.arc(cx + ox, cy - oy, R, 0, 2 * Math.PI); ctx.fillStyle = shade; ctx.fill();
        ctx.globalAlpha = 1;
        ctx.lineWidth = 2; ctx.strokeStyle = C.ink;
        ctx.beginPath(); ctx.arc(cx + ox, cy - oy, R, phi - Math.PI / 2, phi + Math.PI / 2); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx + nx * R, cy + ny * R); ctx.lineTo(cx + ox + nx * R, cy - oy + ny * R); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - nx * R, cy - ny * R); ctx.lineTo(cx + ox - nx * R, cy - oy - ny * R); ctx.stroke();
        ctx.globalAlpha = 0.34;
        ctx.beginPath(); ctx.arc(cx, cy, R, 0, 2 * Math.PI); ctx.fillStyle = shade; ctx.fill();
        ctx.globalAlpha = 1;
        ctx.beginPath(); ctx.arc(cx, cy, R, 0, 2 * Math.PI); ctx.strokeStyle = C.ink; ctx.stroke();
      }
    }

    function drawBars(ctx, w, hh, C) {
      const padL = 44, padR = 12, padT = 20, padB = 44;
      const pw = w - padL - padR, ph = hh - padT - padB;
      if (pw < 60 || ph < 30) return;
      ctx.font = '12px ' + C.font; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = C.ink2; ctx.textAlign = 'left';
      ctx.fillText('SA:V for cubes (cm⁻¹)', padL, 12);
      const ymax = 7.5, Y = v => padT + ph - (v / ymax) * ph;
      ctx.strokeStyle = C.rule; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(padL, padT); ctx.lineTo(padL, padT + ph); ctx.lineTo(padL + pw, padT + ph); ctx.stroke();
      ctx.textAlign = 'right';
      [0, 2, 4, 6].forEach(v => { ctx.fillStyle = C.ink2; ctx.fillText(String(v), padL - 6, Y(v) + 4); });
      const cubeNow = S.shape === 'cube' ? S.p.a : null;
      let near = 1;
      if (cubeNow != null) for (let k = 1; k <= 5; k++) if (Math.abs(k - cubeNow) < Math.abs(near - cubeNow)) near = k;
      const bw = pw / 5, vals = [];
      const halo = (t, x, y) => { ctx.save(); ctx.lineWidth = 3; ctx.strokeStyle = C.card; ctx.strokeText(t, x, y); ctx.restore(); ctx.fillText(t, x, y); };
      for (let k = 1; k <= 5; k++) {
        const v = 6 / k, x = padL + (k - 0.5) * bw;
        const hi = cubeNow != null && k === near;
        ctx.fillStyle = hi ? C.sc : C.ink3;
        ctx.fillRect(x - bw * 0.3, Y(v), bw * 0.6, padT + ph - Y(v));
        ctx.textAlign = 'center'; ctx.fillStyle = hi ? C.ink : C.ink2;
        vals.push([sf(v, 2), x, Y(v) - 4, hi]);
        ctx.fillText(k + ' cm', x, padT + ph + 16);
        if (hi) { ctx.fillText('▲', x, padT + ph + 29); }
      }
      ctx.textAlign = 'center'; ctx.fillStyle = C.ink2;
      ctx.fillText('side of the cube', padL + pw / 2, hh - 3);
      // the current shape as a dashed line
      const g = geom(S.shape, S.p), r = g.sa / g.v;
      if (isFinite(r) && r <= ymax) {
        ctx.save(); ctx.setLineDash([5, 4]); ctx.strokeStyle = C.red; ctx.lineWidth = 1.6;
        ctx.beginPath(); ctx.moveTo(padL, Y(r)); ctx.lineTo(padL + pw, Y(r)); ctx.stroke(); ctx.restore();
        ctx.fillStyle = C.red; ctx.textAlign = 'right';
        halo('this ' + S.shape + ': ' + sf(r), padL + pw, Y(r) - 4);
      }
      ctx.textAlign = 'center';
      vals.forEach(q => { ctx.fillStyle = q[3] ? C.ink : C.ink2; halo(q[0], q[1], q[2]); });
    }

    function drawAgar(ctx, w, hh, C) {
      const secH = hh * 0.52;
      const pcm = Math.max(1, Math.min((w - 24) / 5.2, (secH - 26) / 5.2));
      const p = S.p, d = RATE * S.t;
      let W0, H0;
      if (S.shape === 'cylinder') { W0 = p.len; H0 = 2 * p.r; }
      else { W0 = p.a; H0 = S.shape === 'cube' ? p.a : p.c; }
      const x0 = (w - W0 * pcm) / 2, y0 = 20 + (secH - 26 - H0 * pcm) / 2 + 6;
      ctx.font = '12px ' + C.font; ctx.textBaseline = 'alphabetic'; ctx.textAlign = 'left';
      ctx.fillStyle = C.ink2;
      ctx.fillText('Cross-section through the middle', 8, 14);
      // outer block: the part the front has reached
      ctx.lineWidth = 2; ctx.strokeStyle = C.ink;
      ctx.fillStyle = C.card; ctx.fillRect(x0, y0, W0 * pcm, H0 * pcm); ctx.strokeRect(x0, y0, W0 * pcm, H0 * pcm);
      const iw = Math.max(0, W0 - 2 * d), ih = Math.max(0, H0 - 2 * d);
      if (iw > 0 && ih > 0) {
        ctx.globalAlpha = 0.45; ctx.fillStyle = C.red;
        ctx.fillRect(x0 + d * pcm, y0 + d * pcm, iw * pcm, ih * pcm); ctx.globalAlpha = 1;
        ctx.save(); ctx.setLineDash([4, 3]); ctx.strokeStyle = C.red; ctx.lineWidth = 1.5;
        ctx.strokeRect(x0 + d * pcm, y0 + d * pcm, iw * pcm, ih * pcm); ctx.restore();
      }
      ctx.fillStyle = C.ink2; ctx.textAlign = 'center';
      ctx.fillText(iw > 0 && ih > 0 ? 'shaded centre: still coloured' : 'all changed: colour has reached the centre', w / 2, y0 + H0 * pcm + 16);
      // curve of % uncoloured against time for this block
      ctx.save();
      ctx.translate(0, secH + 4);
      const ph = hh - secH - 4;
      if (ph > 70) {
        const A = W.axes(ctx, w, ph, { x0: 0, x1: 25, y0: 0, y1: 100 }, C, { pad: { l: 40, r: 12, t: 16, b: 32 }, xlabel: 'time / min', ylabel: '% uncoloured', nx: 5, ny: 4 });
        if (A && A.X && A.Y) {
          ctx.strokeStyle = C.sc; ctx.lineWidth = 2; ctx.beginPath();
          for (let k = 0; k <= 50; k++) {
            const t = k * 0.5, v = uncoloured(S.shape, S.p, t) * 100;
            if (k) ctx.lineTo(A.X(t), A.Y(v)); else ctx.moveTo(A.X(t), A.Y(v));
          }
          ctx.stroke();
          const vn = uncoloured(S.shape, S.p, S.t) * 100;
          ctx.fillStyle = C.red; ctx.beginPath(); ctx.arc(A.X(S.t), A.Y(vn), 4, 0, 2 * Math.PI); ctx.fill();
        }
      }
      ctx.restore();
    }

    function draw(ctx, w, h, C) {
      if (!(w > 0) || !(h > 0)) return;
      if (w < 120 || h < 120) return;
      ctx.clearRect(0, 0, w, h);
      if (S.mode === 'agar') { drawAgar(ctx, w, h, C); return; }
      const ht = h * 0.5;
      drawShape(ctx, w, ht, C);
      ctx.save(); ctx.translate(0, ht + 6); drawBars(ctx, w, h - ht - 6, C); ctx.restore();
    }

    build();
  });
})();
