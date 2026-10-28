/* vectors3d: two lines r = a + t d in 3D. Drag to rotate; says parallel / intersecting (at …) / skew, the acute angle between
   the lines and, if a point P is given, the foot of the perpendicular from P to line 1.
   data-lines "a1,a2,a3|d1,d2,d3; a1,a2,a3|d1,d2,d3"   data-point "p1,p2,p3" (optional)   data-skew "a1,a2,a3|d1,d2,d3" (optional second line for a button) */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const num3 = (s) => {
    const p = String(s == null ? '' : s).replace(/[−–]/g, '-').split(',').map((t) => parseFloat(t));
    return p.length === 3 && p.every(isFinite) ? p : null;
  };
  const line = (s) => {
    const parts = String(s == null ? '' : s).split('|');
    const a = num3(parts[0]), d = num3(parts[1]);
    return a && d ? { a, d } : null;
  };
  const sub = (u, v) => [u[0] - v[0], u[1] - v[1], u[2] - v[2]];
  const add = (u, v) => [u[0] + v[0], u[1] + v[1], u[2] + v[2]];
  const mul = (k, u) => [k * u[0], k * u[1], k * u[2]];
  const dot = (u, v) => u[0] * v[0] + u[1] * v[1] + u[2] * v[2];
  const cross = (u, v) => [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]];
  const mag = (u) => Math.hypot(u[0], u[1], u[2]);
  const fmtV = (u) => `(${u.map((x) => W.fmt(x, 3)).join(', ')})`;
  const LIM = 1e4;

  W.register('vectors3d', function (el, o) {
    const { body } = W.frame(el, 'Two lines in 3D', 'drag the picture to rotate it; edit any number');
    const warn = [];
    const raw = String(o.lines || '1,2,3|1,-1,2; 1,-1,8|2,1,-1').split(';');
    let L1 = line(raw[0]), L2 = line(raw[1]);
    if (!L1 || !L2) { warn.push('data-lines should look like "1,2,3|1,-1,2; 1,-1,8|2,1,-1". Using that example.'); L1 = { a: [1, 2, 3], d: [1, -1, 2] }; L2 = { a: [1, -1, 8], d: [2, 1, -1] }; }
    const P0 = o.point ? num3(o.point) : null;
    if (o.point && !P0) warn.push('data-point should look like "4,0,5". It was ignored.');
    const skew = o.skew ? line(o.skew) : null;
    const start = [L1.a.concat(L1.d), L2.a.concat(L2.d)];
    const flds = [[], []];
    const rows = [];
    const names = ['a₁', 'a₂', 'a₃', 'd₁', 'd₂', 'd₃'];
    const err = W.h('div', { class: 'w-err', role: 'status' });
    const showErr = (t) => { err.textContent = t; err.style.display = t ? '' : 'none'; };
    showErr(warn.join(' '));
    for (let k = 0; k < 2; k++) {
      const row = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end', gap: '6px 8px' } });
      row.append(W.h('span', { class: 'w-lab', style: { minWidth: '5.5em', color: k ? 'var(--sc2)' : 'var(--sc)', fontWeight: 600 } }, `Line ${k + 1}`));
      names.forEach((nm, i) => {
        const f = W.field({ label: nm, value: start[k][i], type: 'number', step: 1, width: '4em', oninput: update });
        f.input.setAttribute('aria-label', `Line ${k + 1}: ${nm}`);
        flds[k].push(f); row.append(f.el);
        if (i === 2) row.append(W.h('span', { class: 'w-lab' }, '  '));
      });
      rows.push(row);
    }
    body.append(W.h('div', { class: 'w-note' }, 'Line k is r = a + t·d, with point a = (a₁, a₂, a₃) and direction d = (d₁, d₂, d₃).'), ...rows);
    let pf = null;
    if (P0) {
      const row = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end', gap: '6px 8px' } });
      row.append(W.h('span', { class: 'w-lab', style: { minWidth: '5.5em', fontWeight: 600 } }, 'Point P'));
      pf = ['x', 'y', 'z'].map((nm, i) => { const f = W.field({ label: nm, value: P0[i], type: 'number', step: 1, width: '4em', oninput: update }); f.input.setAttribute('aria-label', `Point P: ${nm}`); row.append(f.el); return f; });
      body.append(row);
    }
    const btns = W.h('div', { class: 'w-row' });
    const reset = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm' }, 'Reset');
    reset.addEventListener('click', () => { start.forEach((vals, k) => vals.forEach((v, i) => flds[k][i].input.value = String(v))); if (pf) pf.forEach((f, i) => f.input.value = String(P0[i])); update(); });
    btns.append(reset);
    if (skew) {
      const bt = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm' }, 'Load the skew example for line 2');
      bt.addEventListener('click', () => { skew.a.concat(skew.d).forEach((v, i) => flds[1][i].input.value = String(v)); update(); });
      btns.append(bt);
    }
    body.append(btns, err);

    const v3 = W.view3d({ yaw: 0.7, pitch: 0.42, scale: 40 });
    const state = { ok: false };
    const cv = W.canvas(body, { height: 330, draw, label: 'Two lines in 3D, with turn buttons below', describe: describeLines });
    cv.wrap.style.touchAction = 'none'; cv.wrap.style.cursor = 'grab';
    W.orbit(cv.wrap, v3, cv.redraw);
    const R = W.readout([['verdict', 'The lines are'], ['detail', 'Common point'], ['angle', 'Acute angle between the lines']].concat(P0 ? [['foot', 'Foot of the perpendicular from P to line 1'], ['dist', 'Perpendicular distance']] : []));
    body.append(R.el, W.h('div', { class: 'w-note' }, 'Intersecting lines share one point; parallel lines have direction vectors that are multiples of each other; skew lines are not parallel and never meet.'));

    function read() {
      const out = { lines: [], P: null };
      for (let k = 0; k < 2; k++) {
        const v = flds[k].map((f) => parseFloat(f.input.value));
        if (!v.every((x) => isFinite(x) && Math.abs(x) <= LIM)) return { error: 'Enter a number in every box (between −10000 and 10000).' };
        out.lines.push({ a: v.slice(0, 3), d: v.slice(3) });
        if (mag(out.lines[k].d) < 1e-9) return { error: `The direction vector of line ${k + 1} cannot be (0, 0, 0).` };
      }
      if (pf) { const p = pf.map((f) => parseFloat(f.input.value)); if (!p.every((x) => isFinite(x) && Math.abs(x) <= LIM)) return { error: 'Enter a number in every box for P.' }; out.P = p; }
      return out;
    }

    let model = null;
    function analyse(m) {
      const [l1, l2] = m.lines, n = cross(l1.d, l2.d), nn = dot(n, n), w0 = sub(l2.a, l1.a);
      const cosA = Math.abs(dot(l1.d, l2.d)) / (mag(l1.d) * mag(l2.d));
      const angle = Math.acos(Math.min(1, cosA)) * 180 / Math.PI;
      const tol = 1e-9 * (1 + mag(l1.d) * mag(l2.d));
      const r = { angle };
      if (Math.sqrt(nn) < tol) {
        const same = mag(cross(w0, l1.d)) < 1e-9 * (1 + mag(w0) * mag(l1.d));
        r.kind = 'parallel'; r.same = same;
        const s0 = dot(sub([0, 0, 0], l1.a), l1.d) / dot(l1.d, l1.d); r.c1 = s0; r.c2 = dot(sub(add(l1.a, mul(s0, l1.d)), l2.a), l2.d) / dot(l2.d, l2.d);
      } else {
        const s = dot(cross(w0, l2.d), n) / nn, t = dot(cross(w0, l1.d), n) / nn;
        const p1 = add(l1.a, mul(s, l1.d)), p2 = add(l2.a, mul(t, l2.d));
        const gap = mag(sub(p1, p2));
        r.s = s; r.t = t; r.p1 = p1; r.p2 = p2;
        r.kind = gap < 1e-7 * (1 + mag(p1)) ? 'intersecting' : 'skew';
      }
      if (m.P) { const tt = dot(sub(m.P, l1.a), l1.d) / dot(l1.d, l1.d); r.foot = add(l1.a, mul(tt, l1.d)); r.fd = mag(sub(m.P, r.foot)); }
      return r;
    }

    function update() {
      const m = read();
      if (m.error) { showErr(m.error); state.ok = false; cv.redraw(); return; }
      showErr(warn.join(' '));
      model = m; model.r = analyse(m); state.ok = true;
      const r = model.r;
      R.set('verdict', r.kind === 'parallel' ? (r.same ? 'parallel (the same line)' : 'parallel') : r.kind);
      R.set('detail', r.kind === 'intersecting' ? `${fmtV(r.p1)} at s = ${W.fmt(r.s, 3)}, t = ${W.fmt(r.t, 3)}` : r.kind === 'parallel' ? (r.same ? 'every point' : 'none') : 'none: no values of s and t fit all three equations');
      R.set('angle', r.kind === 'parallel' ? '0°' : `${W.fix(r.angle, 1)}°`);
      if (m.P) { R.set('foot', fmtV(r.foot)); R.set('dist', W.fmt(r.fd, 3)); }
      cv.redraw();
    }
    function describeLines() {
      if (!state.ok || !model) return 'No picture: a box above needs a valid number.';
      const { lines, P, r } = model;
      const ln = lines.map((l, k) => `Line ${k + 1} through ${fmtV(l.a)} with direction ${fmtV(l.d)}`).join('; ');
      let s = `${ln}. The lines are ${r.kind === 'parallel' && r.same ? 'parallel (the same line)' : r.kind}`;
      if (r.kind === 'intersecting') s += `, meeting at ${fmtV(r.p1)}`;
      s += r.kind === 'parallel' ? '.' : `, with an acute angle of ${W.fix(r.angle, 1)} degrees.`;
      if (P) s += ` The foot of the perpendicular from P to line 1 is ${fmtV(r.foot)}, at distance ${W.fmt(r.fd, 3)}.`;
      return s;
    }

    function draw(ctx, w, h, c) {
      if (!state.ok || !model) {
        ctx.fillStyle = c.ink2; ctx.font = `13px ${c.font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('Fix the numbers above to see the lines.', w / 2, h / 2); return;
      }
      const { lines, P, r } = model;
      // parameter windows around the closest points so the interesting part is always on screen
      const centre = [r.kind === 'parallel' ? r.c1 : r.s, r.kind === 'parallel' ? r.c2 : r.t];
      const pts = [];
      const segs = lines.map((ln, k) => {
        const t0 = centre[k], ext = 4 / Math.max(0.5, mag(ln.d)) * 1.6;
        const A = add(ln.a, mul(t0 - ext, ln.d)), B = add(ln.a, mul(t0 + ext, ln.d));
        pts.push(A, B); return [A, B];
      });
      if (P) { pts.push(P, r.foot); }
      const box = (list) => {
        const lo = [Infinity, Infinity, Infinity], hi = [-Infinity, -Infinity, -Infinity];
        list.forEach((p) => p.forEach((x, i) => { lo[i] = Math.min(lo[i], x); hi[i] = Math.max(hi[i], x); }));
        return { cen: lo.map((x, i) => (x + hi[i]) / 2), rad: Math.max(1e-6, Math.hypot(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2]) / 2) };
      };
      let { cen, rad } = box(pts);
      // show the axes only when the origin is not far from the lines, or the lines shrink to a speck
      const showAxes = Math.hypot(cen[0], cen[1], cen[2]) <= 3 * rad;
      if (showAxes) ({ cen, rad } = box(pts.concat([[0, 0, 0]])));
      v3.scale = Math.min(w, h) * 0.4 / rad;
      const pr = (p) => v3.project(p[0] - cen[0], p[1] - cen[1], p[2] - cen[2], w, h);
      const drawSeg = (A, B, col, lw, dash) => { const a = pr(A), b = pr(B); ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.setLineDash(dash || []); ctx.stroke(); ctx.setLineDash([]); };
      const label = (p, t, col, dx = 8, dy = -8) => { const q = pr(p); ctx.fillStyle = col; ctx.font = `12px ${c.font}`; ctx.textAlign = 'left'; ctx.textBaseline = 'middle'; ctx.fillText(t, q[0] + dx, q[1] + dy); };
      const dotAt = (p, rr, col) => { const q = pr(p); ctx.beginPath(); ctx.arc(q[0], q[1], rr, 0, Math.PI * 2); ctx.fillStyle = col; ctx.fill(); };
      // axes from the origin
      if (showAxes) {
        const al = rad * 0.9;
        for (const [vec, nm] of [[[al, 0, 0], 'x'], [[0, al, 0], 'y'], [[0, 0, al], 'z']]) { drawSeg([0, 0, 0], vec, c.ink3, 1.2, [4, 3]); label(vec, nm, c.ink3, 4, 0); }
        dotAt([0, 0, 0], 3, c.ink3); label([0, 0, 0], 'O', c.ink3, 5, 9);
      }
      drawSeg(segs[0][0], segs[0][1], c.sc, 3); drawSeg(segs[1][0], segs[1][1], c.sc2, 3);
      label(segs[0][1], 'line 1', c.sc, 6, -2); label(segs[1][1], 'line 2', c.sc2, 6, -2);
      if (r.kind === 'intersecting') { dotAt(r.p1, 5.5, c.red); label(r.p1, `(${r.p1.map((x) => W.fmt(x, 3)).join(', ')})`, c.red, 8, -10); }
      else if (r.kind === 'skew') { drawSeg(r.p1, r.p2, c.red, 1.6, [3, 3]); dotAt(r.p1, 3.5, c.sc); dotAt(r.p2, 3.5, c.sc2); }
      if (P) { drawSeg(P, r.foot, c.ok, 2, [5, 3]); dotAt(P, 4.5, c.ink); label(P, 'P', c.ink, 7, -6); dotAt(r.foot, 4, c.ok); label(r.foot, 'foot', c.ok, 7, 8); }
    }
    update();
  });
})();
