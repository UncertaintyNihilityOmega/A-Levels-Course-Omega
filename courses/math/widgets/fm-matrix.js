/* fm-matrix: a 2x2 matrix acting on the plane (Further Maths 9231 FP1, reused for eigenvectors in FP2).
   data-m="a,b,c,d"      the matrix (a b; c d); default 1,1,0,1
   data-shape="square|triangle|L"   the shape that is transformed; default square
   data-show="grid,det,invariant,eigen"   extras (comma list); default grid,det,invariant
   data-presets="rotation,reflection,shear,stretch,enlargement"   buttons that load an example; default all five
   The logic (determinant, inverse, invariant lines, eigenvalues) is plain functions, exported for Node tests. */
(function () {
  'use strict';
  const EPS = 1e-9, FIX = 1e-3, LIM = 10;
  const SHAPES = {
    square: [[0, 0], [1, 0], [1, 1], [0, 1]],
    triangle: [[0, 0], [2, 0], [0, 1]],
    L: [[0, 0], [2, 0], [2, 1], [1, 1], [1, 2], [0, 2]],
  };
  const PRESETS = {
    rotation: { m: [0.5, -0.866, 0.866, 0.5], note: 'rotation through 60° anticlockwise' },
    reflection: { m: [0.5, 0.866, 0.866, -0.5], note: 'reflection in y = x tan 30°' },
    shear: { m: [1, 1, 0, 1], note: 'shear, x-axis fixed' },
    stretch: { m: [2, 0, 0, 1], note: 'stretch parallel to the x-axis, scale factor 2' },
    enlargement: { m: [2, 0, 0, 2], note: 'enlargement, scale factor 2, centre O' },
  };
  const PRESET_LABEL = { rotation: 'Rotation 60°', reflection: 'Reflection', shear: 'Shear', stretch: 'Stretch', enlargement: 'Enlargement' };

  const fmtN = (x) => {
    if (!isFinite(x)) return '—';
    let v = parseFloat(Number(x).toPrecision(3));
    if (Object.is(v, -0) || v === 0) v = 0;
    return String(v).replace('-', '−');
  };
  const det = (m) => m[0] * m[3] - m[1] * m[2];
  const apply = (m, p) => [m[0] * p[0] + m[1] * p[1], m[2] * p[0] + m[3] * p[1]];
  const inverse = (m) => {
    const d = det(m);
    if (!isFinite(d) || Math.abs(d) < EPS) return null;
    return [m[3] / d, -m[1] / d, -m[2] / d, m[0] / d];
  };

  /** Invariant lines through the origin of (a b; c d): y = mx with b m^2 + (a - d) m - c = 0, and x = 0 when b = 0.
      lam is the factor by which points on the line are scaled (a + b m); lam = 1 means a line of invariant points. */
  function invariantLines(m) {
    const [a, b, c, d] = m;
    const out = { all: false, identity: false, lines: [], vertical: null };
    if (Math.abs(b) < EPS && Math.abs(c) < EPS && Math.abs(a - d) < EPS) {
      out.all = true; out.identity = Math.abs(a - 1) < FIX; return out;
    }
    if (Math.abs(b) < EPS) {
      out.vertical = { lam: d, fixed: Math.abs(d - 1) < FIX };
      if (Math.abs(a - d) > EPS) out.lines.push({ m: c / (a - d), lam: a, fixed: Math.abs(a - 1) < FIX });
    } else {
      const disc = (a - d) * (a - d) + 4 * b * c;
      const tol = EPS * Math.max(1, (a - d) * (a - d));
      const add = (mm) => { const lam = a + b * mm; out.lines.push({ m: mm, lam, fixed: Math.abs(lam - 1) < FIX }); };
      if (Math.abs(disc) < tol) add((d - a) / (2 * b));
      else if (disc > 0) { const s = Math.sqrt(disc); add((d - a + s) / (2 * b)); add((d - a - s) / (2 * b)); }
    }
    out.lines.sort((p, q) => p.m - q.m);
    return out;
  }

  /** Real eigenvalues with a direction vector each, or complex = true when there are none. */
  function eigen(m) {
    const [a, b, c, d] = m;
    const t = a + d, disc = (a - d) * (a - d) + 4 * b * c;
    if (disc < -EPS * Math.max(1, t * t)) return { complex: true, values: [], scalar: false };
    const s = Math.sqrt(Math.max(0, disc));
    const scalar = Math.abs(b) < EPS && Math.abs(c) < EPS && Math.abs(a - d) < EPS;
    const lams = s < EPS ? [t / 2] : [(t + s) / 2, (t - s) / 2];
    const values = lams.map((lam) => {
      let v;
      if (Math.abs(b) > EPS) v = [b, lam - a];
      else if (Math.abs(c) > EPS) v = [lam - d, c];
      else v = Math.abs(lam - a) < Math.abs(lam - d) ? [1, 0] : [0, 1];
      return { lam, dir: v };
    });
    return { complex: false, values, scalar };
  }

  const lineText = (mm) => {
    if (Math.abs(mm) < 1e-9) return 'y = 0';
    const k = fmtN(mm);
    return k === '1' ? 'y = x' : k === '−1' ? 'y = −x' : `y = ${k}x`;
  };
  const dirText = (v) => (Math.abs(v[0]) < EPS ? 'x = 0' : lineText(v[1] / v[0]));

  function describeMatrix(m) {
    const d = det(m);
    const out = { det: d, area: Math.abs(d), singular: Math.abs(d) < EPS };
    out.orient = out.singular ? 'singular: the plane collapses onto a line' : d < 0 ? 'orientation reversed (a reflection is involved)' : 'orientation kept';
    const il = invariantLines(m);
    let lines;
    if (il.all) lines = il.identity ? 'every line through O' : 'every line through O (scalar matrix)';
    else {
      const parts = il.lines.map((l) => lineText(l.m) + (l.fixed ? ' (every point fixed)' : Math.abs(l.lam) < FIX ? ' (points go to O)' : ''));
      if (il.vertical) parts.push('x = 0' + (il.vertical.fixed ? ' (every point fixed)' : Math.abs(il.vertical.lam) < FIX ? ' (points go to O)' : ''));
      lines = parts.length ? parts.join(', ') : 'none (no real invariant line through O)';
    }
    out.lines = lines;
    let fixed;
    if (il.identity) fixed = 'every point (the identity)';
    else {
      const f = il.lines.filter((l) => l.fixed).map((l) => lineText(l.m));
      if (il.vertical && il.vertical.fixed) f.push('x = 0');
      fixed = il.all ? 'only the origin' : f.length ? 'line of invariant points: ' + f.join(' and ') : 'only the origin';
    }
    out.fixed = fixed;
    const eg = eigen(m);
    out.eigenvalues = eg.complex ? 'complex: no real eigenvalues' : eg.values.map((v) => 'λ = ' + fmtN(v.lam)).join(', ');
    out.eigenvectors = eg.complex ? 'no real eigenvectors' : eg.scalar ? 'every direction' : eg.values.map((v) => 'λ = ' + fmtN(v.lam) + ': ' + dirText(v.dir)).join('; ');
    return out;
  }

  /** Parse "a,b,c,d": returns {m, err}. Falls back to the identity on any problem. */
  function parseMatrix(str, dflt) {
    if (str == null || String(str).trim() === '') return { m: dflt.slice(), err: '' };
    const parts = String(str).split(',').map((s) => s.trim());
    const nums = parts.map((s) => (s === '' ? NaN : Number(s)));
    if (parts.length !== 4 || nums.some((x) => !isFinite(x))) return { m: [1, 0, 0, 1], err: 'data-m needs four numbers "a,b,c,d", so the identity matrix is used.' };
    if (nums.some((x) => Math.abs(x) > LIM)) return { m: nums.map((x) => Math.max(-LIM, Math.min(LIM, x))), err: `Matrix entries are limited to −${LIM} to ${LIM}.` };
    return { m: nums, err: '' };
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { det, inverse, apply, invariantLines, eigen, describeMatrix, parseMatrix, lineText, SHAPES, PRESETS };
  }
  const W = typeof window !== 'undefined' ? window.W : undefined;
  if (!W) return;

  W.register('fm-matrix', function (el, o) {
    const warn = [];
    const pm = parseMatrix(o.m, [1, 1, 0, 1]);
    if (pm.err) warn.push(pm.err);
    let M = pm.m;
    let shape = String(o.shape || 'square').trim();
    if (!SHAPES[shape]) { warn.push('data-shape should be square, triangle or L, so square is used.'); shape = 'square'; }
    const knownShow = ['grid', 'det', 'invariant', 'eigen'];
    let show = o.show == null || String(o.show).trim() === '' ? ['grid', 'det', 'invariant'] : String(o.show).split(',').map((s) => s.trim()).filter(Boolean);
    const badShow = show.filter((s) => knownShow.indexOf(s) < 0);
    if (badShow.length) { warn.push('data-show does not know: ' + badShow.join(', ') + '.'); show = show.filter((s) => knownShow.indexOf(s) >= 0); }
    let presets = o.presets == null || String(o.presets).trim() === '' ? Object.keys(PRESETS) : String(o.presets).split(',').map((s) => s.trim()).filter(Boolean);
    const badPre = presets.filter((s) => !PRESETS[s]);
    if (badPre.length) { warn.push('data-presets does not know: ' + badPre.join(', ') + '.'); presets = presets.filter((s) => PRESETS[s]); }
    const has = (k) => show.indexOf(k) >= 0;

    const { body } = W.frame(el, 'Matrix transformation', 'Set the four entries a, b, c, d and watch the shape and its image');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const fields = {};
    const keys = ['a', 'b', 'c', 'd'];
    // the four entries laid out like the matrix: a b / c d
    const row = W.h('div', { class: 'w-row', style: { display: 'grid', gridTemplateColumns: 'repeat(2, 5.5rem)', gap: '10px 16px', alignItems: 'end' } });
    keys.forEach((k, i) => {
      fields[k] = W.field({
        label: k, value: String(Math.round(M[i] * 10000) / 10000), type: 'number', step: '0.1', width: '5.5rem',
        oninput: (v) => {
          const x = parseFloat(v);
          if (isFinite(x) && Math.abs(x) <= LIM) { M[i] = x; setErr(''); resetAnim(); update(); }
          else setErr(`Type a number from −${LIM} to ${LIM} for ${k}.`);
        },
      });
      row.append(fields[k].el);
    });
    body.append(row);
    function setErr(t) { errBox.textContent = t; errBox.style.display = t ? '' : 'none'; }

    let s = 0;               // 0: image under M, 1: back at the shape (identity)
    let target = 0, raf = 0;
    const brow = W.h('div', { class: 'w-row' });
    const loadMatrix = (arr) => {
      M = arr.slice();
      keys.forEach((k, i) => { fields[k].input.value = String(Math.round(M[i] * 10000) / 10000); });
      setErr(''); resetAnim(); update();
    };
    presets.forEach((p) => {
      brow.append(W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', onclick: () => { loadMatrix(PRESETS[p].m); W.say(body, 'Loaded: ' + PRESETS[p].note + '.'); } }, PRESET_LABEL[p]));
    });
    const invBtn = W.h('button', { class: 'btn btn-sm', type: 'button', 'aria-pressed': 'false', onclick: () => toggleInverse() }, 'Show A⁻¹');
    brow.append(invBtn);
    body.append(brow);
    const status = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    body.append(status);

    const cv = W.canvas(body, { height: 340, draw, label: 'A shape and its image under the matrix', describe: describeScene });
    const rows = [];
    if (has('det')) rows.push(['det', 'det M'], ['area', 'Area scale factor |det M|'], ['orient', 'Orientation']);
    if (has('invariant')) rows.push(['lines', 'Invariant lines through O'], ['fixed', 'Invariant points']);
    if (has('eigen')) rows.push(['eig', 'Eigenvalues'], ['vec', 'Eigenvector directions']);
    const R = rows.length ? W.readout(rows) : null;
    if (R) body.append(R.el);
    body.append(W.h('div', { class: 'w-note' },
      has('invariant') || has('eigen')
        ? 'Try it: choose Shear, then Reflection, then Rotation and compare the dashed invariant lines. For the matrix 3, 1, 2, 2 one line is stretched by 4 and one is fixed point by point. "Show A⁻¹" undoes the transformation (it needs det M ≠ 0).'
        : 'Try it: the arrows Mi and Mj are the columns of the matrix. Change b and watch the top of the shape slide; set a, b, c, d to 0, −1, 1, 0 for a quarter turn. "Show A⁻¹" undoes the transformation.'));

    function resetAnim() {
      cancelAnimationFrame(raf); raf = 0; s = 0; target = 0;
      invBtn.setAttribute('aria-pressed', 'false'); invBtn.textContent = 'Show A⁻¹';
      status.textContent = '';
    }
    function toggleInverse() {
      if (!inverse(M)) { status.textContent = 'This matrix is singular (det M = 0), so A⁻¹ does not exist: the plane has been flattened and cannot be restored.'; return; }
      target = target === 0 ? 1 : 0;
      const pressed = target === 1;
      invBtn.setAttribute('aria-pressed', pressed ? 'true' : 'false');
      invBtn.textContent = pressed ? 'Show A again' : 'Show A⁻¹';
      status.textContent = pressed ? 'Showing the image being moved back by A⁻¹: it returns to the original shape.' : 'Showing the image under A.';
      cancelAnimationFrame(raf);
      if (W.reducedMotion()) { s = target; cv.redraw(); return; }
      const from = s, t0 = performance.now(), dur = 1000;
      const step = (now) => {
        const p = Math.max(0, Math.min(1, (now - t0) / dur));
        const e = p * p * (3 - 2 * p);
        s = from + (target - from) * e;
        cv.redraw();
        if (p < 1) raf = requestAnimationFrame(step); else raf = 0;
      };
      raf = requestAnimationFrame(step);
    }

    function shown() {   // matrix drawn: (1 - s) M + s I
      return [(1 - s) * M[0] + s, (1 - s) * M[1], (1 - s) * M[2], (1 - s) * M[3] + s];
    }

    function draw(ctx, w, h, c) {
      if (!(w > 40 && h > 40)) return;
      const P = SHAPES[shape];
      const pad = { l: 30, r: 12, t: 14, b: 24 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      if (!(pw > 10 && ph > 10)) return;
      // View fitted to the shape, its image under M and the columns Mi, Mj (so it stays fixed while a preset or A⁻¹ animates):
      // at least ±3, the same scale on both axes, the origin at the centre.
      let ex = 0, ey = 0;
      P.concat([[1, 0], [0, 1]]).forEach((p) => {
        const q = apply(M, p);
        ex = Math.max(ex, Math.abs(p[0]), Math.abs(q[0])); ey = Math.max(ey, Math.abs(p[1]), Math.abs(q[1]));
      });
      let hy = Math.max(3, 1.2 * ey, 1.2 * ex * ph / pw);
      hy = Math.min(60, Math.ceil(hy * 2) / 2);
      const Rr = hy, hx = hy * pw / ph;
      const A = W.axes(ctx, w, h, { x0: -hx, x1: hx, y0: -hy, y1: hy }, c, { pad, xlabel: 'x', ylabel: 'y' });
      const X = A.X, Y = A.Y;
      const D = shown();
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
      // transformed grid
      if (has('grid')) {
        const N = Math.min(30, Math.ceil(Math.max(hx, hy)));
        ctx.lineWidth = 1; ctx.strokeStyle = c.rule2 || c.rule; ctx.globalAlpha = 0.9;
        const L = Math.max(hx, hy) * 3;
        for (let j = -N; j <= N; j++) {
          let p = apply(D, [j, -L]), q = apply(D, [j, L]);
          ctx.beginPath(); ctx.moveTo(X(p[0]), Y(p[1])); ctx.lineTo(X(q[0]), Y(q[1])); ctx.stroke();
          p = apply(D, [-L, j]); q = apply(D, [L, j]);
          ctx.beginPath(); ctx.moveTo(X(p[0]), Y(p[1])); ctx.lineTo(X(q[0]), Y(q[1])); ctx.stroke();
        }
        ctx.globalAlpha = 1;
      }
      // invariant lines (dashed)
      if (has('invariant')) {
        const il = invariantLines(M);
        const far = Math.max(hx, hy) * 4;
        ctx.setLineDash([7, 5]); ctx.lineWidth = 1.6; ctx.strokeStyle = c.red;
        const seg = (p, q) => { ctx.beginPath(); ctx.moveTo(X(p[0]), Y(p[1])); ctx.lineTo(X(q[0]), Y(q[1])); ctx.stroke(); };
        if (!il.all) {
          il.lines.forEach((l) => seg([-far, -far * l.m], [far, far * l.m]));
          if (il.vertical) seg([0, -far], [0, far]);
        }
        ctx.setLineDash([]);
      }
      // original shape (outline) and image (filled)
      const path = (pts) => { ctx.beginPath(); pts.forEach((p, i) => { const x = X(p[0]), y = Y(p[1]); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }); ctx.closePath(); };
      path(P);
      ctx.setLineDash([5, 4]); ctx.lineWidth = 1.8; ctx.strokeStyle = c.ink2; ctx.stroke(); ctx.setLineDash([]);
      const img = P.map((p) => apply(D, p));
      path(img);
      ctx.globalAlpha = 0.28; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1;
      ctx.lineWidth = 2.2; ctx.strokeStyle = c.sc; ctx.stroke();
      // arrows i -> Mi, j -> Mj
      const arrow = (x1, y1, x2, y2, col, wd) => {
        const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy);
        if (len < 3) return;
        const ux = dx / len, uy = dy / len, hl = Math.min(10, len * 0.5);
        ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = wd;
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2 - ux * hl * 0.6, y2 - uy * hl * 0.6); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x2, y2); ctx.lineTo(x2 - ux * hl + uy * hl * 0.42, y2 - uy * hl - ux * hl * 0.42);
        ctx.lineTo(x2 - ux * hl - uy * hl * 0.42, y2 - uy * hl + ux * hl * 0.42); ctx.closePath(); ctx.fill();
      };
      const Mi0 = apply(D, [1, 0]), Mj0 = apply(D, [0, 1]);
      arrow(X(0), Y(0), X(Mi0[0]), Y(Mi0[1]), c.sc, 2.6);
      arrow(X(0), Y(0), X(Mj0[0]), Y(Mj0[1]), c.sc2, 2.6);
      ctx.fillStyle = c.ink; ctx.beginPath(); ctx.arc(X(0), Y(0), 3, 0, Math.PI * 2); ctx.fill();
      ctx.restore();
      // labels (outside the clip, kept inside the canvas)
      const label = (txt, x, y, col, align) => {
        ctx.font = `600 12px ${c.font}`; ctx.textBaseline = 'middle'; ctx.textAlign = 'left';
        const wd = ctx.measureText(txt).width;
        let lx = align === 'right' ? x - wd : align === 'center' ? x - wd / 2 : x;
        lx = Math.max(4, Math.min(w - 4 - wd, lx));
        const ly = Math.max(pad.t + 8, Math.min(h - pad.b - 8, y));
        ctx.lineWidth = 3; ctx.strokeStyle = c.card; ctx.lineJoin = 'round'; ctx.strokeText(txt, lx, ly);
        ctx.fillStyle = col; ctx.fillText(txt, lx, ly);
      };
      const tipLabel = (txt, p, col) => {
        const px = X(p[0]), py = Y(p[1]), ox = px - X(0), oy = py - Y(0), len = Math.hypot(ox, oy);
        if (len < 16) { label(txt, px + 8, py - 12, col, 'left'); return; }
        const ux = ox / len, uy = oy / len;
        label(txt, px + ux * 9, py + uy * 9, col, ux > 0.35 ? 'left' : ux < -0.35 ? 'right' : 'center');
      };
      const Mi = apply(D, [1, 0]), Mj = apply(D, [0, 1]);
      tipLabel('Mi', Mi, c.sc);
      tipLabel('Mj', Mj, c.sc2);
      let far = img[0];
      img.forEach((p) => { if (Math.hypot(p[0], p[1]) > Math.hypot(far[0], far[1])) far = p; });
      tipLabel('image', far, c.ink);
      if (has('invariant')) {
        const il = invariantLines(M);
        if (!il.all) {
          il.lines.forEach((l) => {
            const xr = Math.min(hx * 0.88, hy * 0.88 / Math.max(Math.abs(l.m), 1e-6));
            label(lineText(l.m), X(xr), Y(l.m * xr) + (l.m >= 0 ? -9 : 10), c.red, 'right');
          });
          if (il.vertical) label('x = 0', X(0) + 6, Y(hy * 0.85), c.red, 'left');
        }
      }
      return null;
    }

    function describeScene() {
      const P = SHAPES[shape];
      const img = P.map((p) => apply(M, p));
      const d = describeMatrix(M);
      const pt = (p) => `(${fmtN(p[0])}, ${fmtN(p[1])})`;
      return `Matrix ${fmtN(M[0])}, ${fmtN(M[1])}; ${fmtN(M[2])}, ${fmtN(M[3])}. The ${shape} with corners ${P.map(pt).join(' ')} maps to the image with corners ${img.map(pt).join(' ')}. Determinant ${fmtN(d.det)}, ${d.orient}. Invariant lines through the origin: ${d.lines}.`;
    }

    function update() {
      const d = describeMatrix(M);
      if (R) {
        if (has('det')) {
          R.set('det', fmtN(d.det));
          R.set('area', d.singular ? '0' : fmtN(d.area));
          R.set('orient', d.orient);
        }
        if (has('invariant')) { R.set('lines', d.lines); R.set('fixed', d.fixed); }
        if (has('eigen')) { R.set('eig', d.eigenvalues); R.set('vec', d.eigenvectors); }
      }
      cv.redraw();
    }
    update();
  });
})();
