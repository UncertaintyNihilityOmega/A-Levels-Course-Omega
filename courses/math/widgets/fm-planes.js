/* fm-planes: one to three planes ax + by + cz = d (and optionally a line and a point) in 3D, with their normals, angles,
   intersections and distances. Further Maths 9231 FP1; the three-plane verdicts are reused by the systems chapter.
   data-planes="a,b,c,d; a,b,c,d; …"   one to three planes; default one plane 1,2,2,6
   data-line="a1,a2,a3|d1,d2,d3"       optional line r = a + t d
   data-point="x,y,z"                  optional point P
   Drag the picture (or use the turn buttons) to rotate it; every number can be edited.
   The logic is plain functions, exported for Node tests (data/test_fm_planes.js). */
(function () {
  'use strict';
  const EPS = 1e-9, LIM = 5, MAXV = 100;
  const W = typeof window !== 'undefined' ? window.W : undefined;

  /* ---- vector helpers ---- */
  const sub = (u, v) => [u[0] - v[0], u[1] - v[1], u[2] - v[2]];
  const add = (u, v) => [u[0] + v[0], u[1] + v[1], u[2] + v[2]];
  const mul = (k, u) => [k * u[0], k * u[1], k * u[2]];
  const dot = (u, v) => u[0] * v[0] + u[1] * v[1] + u[2] * v[2];
  const cross = (u, v) => [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]];
  const mag = (u) => Math.hypot(u[0], u[1], u[2]);
  const DEG = 180 / Math.PI;
  const clean = (x) => (Math.abs(x) < 1e-12 ? 0 : x);

  const fmtN = (x) => {
    if (!isFinite(x)) return '—';
    let v = parseFloat(Number(x).toPrecision(3));
    if (Object.is(v, -0) || v === 0) v = 0;
    return String(v).replace('-', '−');
  };
  // distances: exactly 3 significant figures, trailing zeros kept ("1.60", not "1.6")
  const fmtD = (x) => {
    if (!isFinite(x)) return '—';
    if (Math.abs(x) < 1e-12) return '0';
    const s = Number(x).toPrecision(3);
    return /e/i.test(s) ? fmtN(x) : s.replace('-', '−');
  };
  /* starting turn: the first yaw (nearest 0.7 radians) from which the first normal makes at least about 27° with the screen,
     so the plane is not seen edge-on; the other normals should make at least about 17°. Pure, exported for tests. */
  function chooseYaw(normals, pitch, yaw0) {
    const sp = Math.sin(pitch), cp = Math.cos(pitch);
    const dep = (n, yaw) => {
      const m = Math.hypot(n[0], n[1], n[2]) || 1;
      return Math.abs((n[2] * sp + (n[0] * Math.sin(yaw) + n[1] * Math.cos(yaw)) * cp) / m);
    };
    if (!normals.length) return yaw0;
    const cand = [];
    for (let k = 0; k <= 62; k++) { cand.push(yaw0 + k * 0.05); if (k) cand.push(yaw0 - k * 0.05); }
    const okFirst = (y) => dep(normals[0], y) >= 0.45 && dep(normals[0], y) <= 0.95;
    const okAll = (y) => okFirst(y) && normals.every((n, i) => i === 0 || dep(n, y) >= 0.3);
    for (const y of cand) if (okAll(y)) return y;
    for (const y of cand) if (okFirst(y)) return y;
    let best = yaw0, bd = dep(normals[0], yaw0);
    for (const y of cand) { const d = dep(normals[0], y); if (d > bd + 0.02) { best = y; bd = d; } }
    return best;
  }
  const fmtV = (u) => '(' + u.map(fmtN).join(', ') + ')';
  const planeText = (p) => {
    const parts = [];
    ['x', 'y', 'z'].forEach((nm, i) => {
      const c = p.n[i];
      if (Math.abs(c) < EPS) return;
      const a = Math.abs(c), body = (a === 1 ? '' : fmtN(a)) + nm;
      parts.push((parts.length ? (c < 0 ? ' − ' : ' + ') : (c < 0 ? '−' : '')) + body);
    });
    return parts.join('') + ' = ' + fmtN(p.d);
  };

  /* ---- parsing ---- */
  const nums = (s, k) => {
    const p = String(s == null ? '' : s).replace(/[−–]/g, '-').split(',').map((t) => (t.trim() === '' ? NaN : Number(t)));
    return p.length === k && p.every((x) => isFinite(x) && Math.abs(x) <= MAXV) ? p : null;
  };
  function parsePlanes(str, fallback) {
    const warn = [];
    if (str == null || String(str).trim() === '') return { planes: fallback.slice(), warn };
    const out = [];
    String(str).split(';').forEach((part, i) => {
      if (part.trim() === '') return;
      const v = nums(part, 4);
      if (!v) warn.push(`Plane ${i + 1} should look like "1,2,2,6" (a, b, c, d).`);
      else if (Math.hypot(v[0], v[1], v[2]) < EPS) warn.push(`Plane ${i + 1} needs a, b, c not all zero.`);
      else out.push({ n: v.slice(0, 3), d: v[3] });
    });
    if (out.length > 3) { warn.push('At most three planes are drawn.'); out.length = 3; }
    if (!out.length) return { planes: fallback.slice(), warn: warn.concat('Using the default plane.') };
    return { planes: out, warn };
  }
  function parseLine(str) {
    if (str == null || String(str).trim() === '') return { line: null, warn: [] };
    const parts = String(str).split('|');
    const a = nums(parts[0], 3), d = nums(parts[1], 3);
    if (!a || !d || mag(d) < EPS) return { line: null, warn: ['data-line should look like "1,0,2|2,1,-1" (a point, then a direction that is not zero). It was ignored.'] };
    return { line: { a, d }, warn: [] };
  }
  function parsePoint(str) {
    if (str == null || String(str).trim() === '') return { point: null, warn: [] };
    const p = nums(str, 3);
    return p ? { point: p, warn: [] } : { point: null, warn: ['data-point should look like "2,1,4". It was ignored.'] };
  }

  /* ---- geometry ---- */
  const tolDir = (u, v) => EPS * Math.max(1, mag(u) * mag(v));
  const normalDistance = (p) => Math.abs(p.d) / mag(p.n);

  function pointPlane(P, p) {
    // foot of the perpendicular and distance from P to the plane
    const nn = dot(p.n, p.n), t = (p.d - dot(p.n, P)) / nn;
    const foot = add(P, mul(t, p.n));
    return { foot, dist: Math.abs(t) * Math.sqrt(nn), on: Math.abs(dot(p.n, P) - p.d) < EPS * (1 + Math.abs(p.d) + mag(p.n) * mag(P)) };
  }
  function linePlane(L, p) {
    const bn = dot(L.d, p.n), denom = mag(L.d) * mag(p.n);
    const res = { angle: Math.asin(Math.min(1, Math.abs(bn) / denom)) * DEG };
    if (Math.abs(bn) > EPS * Math.max(1, denom)) {
      const t = (p.d - dot(p.n, L.a)) / bn;
      res.kind = 'meets'; res.t = t; res.point = add(L.a, mul(t, L.d));
    } else {
      const inside = Math.abs(dot(p.n, L.a) - p.d) < EPS * (1 + Math.abs(p.d) + mag(p.n) * mag(L.a));
      res.kind = inside ? 'in' : 'parallel'; res.angle = 0;
      if (!inside) res.gap = Math.abs(dot(p.n, L.a) - p.d) / mag(p.n);
    }
    return res;
  }
  function twoPlanes(p1, p2) {
    const c = cross(p1.n, p2.n), cm = mag(c);
    const cosA = Math.min(1, Math.abs(dot(p1.n, p2.n)) / (mag(p1.n) * mag(p2.n)));
    const angle = Math.acos(cosA) * DEG;
    if (cm < tolDir(p1.n, p2.n)) {
      const k = dot(p1.n, p2.n) / dot(p1.n, p1.n);
      const same = Math.abs(p2.d - k * p1.d) < EPS * (1 + Math.abs(p2.d) + Math.abs(k * p1.d));
      return same ? { kind: 'coincide', angle: 0 } : { kind: 'parallel', angle: 0, gap: Math.abs(p2.d - k * p1.d) / mag(p2.n) };
    }
    const r0 = mul(1 / (cm * cm), cross(sub(mul(p1.d, p2.n), mul(p2.d, p1.n)), c));
    return { kind: 'line', angle, dir: c, point: r0 };
  }

  /* rank of a small matrix by Gaussian elimination with a relative tolerance */
  function rank(M) {
    const A = M.map((r) => r.slice());
    let scale = 0;
    A.forEach((r) => r.forEach((x) => { scale = Math.max(scale, Math.abs(x)); }));
    const tol = 1e-9 * Math.max(1, scale);
    let rk = 0;
    const cols = A[0].length;
    for (let c = 0; c < cols && rk < A.length; c++) {
      let piv = rk;
      for (let r = rk + 1; r < A.length; r++) if (Math.abs(A[r][c]) > Math.abs(A[piv][c])) piv = r;
      if (Math.abs(A[piv][c]) <= tol) continue;
      [A[rk], A[piv]] = [A[piv], A[rk]];
      for (let r = rk + 1; r < A.length; r++) {
        const f = A[r][c] / A[rk][c];
        for (let k = c; k < cols; k++) A[r][k] -= f * A[rk][k];
      }
      rk++;
    }
    return rk;
  }
  const det3 = (a, b, c) => dot(a, cross(b, c));

  /** The five cases for three planes (plus the degenerate ones). Returns {kind, text, point?}. */
  function classify3(planes) {
    const N = planes.map((p) => p.n), aug = planes.map((p) => p.n.concat([p.d]));
    const rN = rank(N), rA = rank(aug);
    const parallelPair = (i, j) => mag(cross(N[i], N[j])) < tolDir(N[i], N[j]);
    const coin = (i, j) => twoPlanes(planes[i], planes[j]).kind === 'coincide';
    if (rN === 3) {
      const D = det3(N[0], N[1], N[2]);
      const pt = mul(1 / D, add(add(mul(planes[0].d, cross(N[1], N[2])), mul(planes[1].d, cross(N[2], N[0]))), mul(planes[2].d, cross(N[0], N[1]))));
      return { kind: 'point', point: pt, text: `meet at a single point ${fmtV(pt.map(clean))}` };
    }
    if (rN === 2) {
      if (rA === 2) {
        const anyCoin = coin(0, 1) || coin(0, 2) || coin(1, 2);
        return { kind: 'line', text: anyCoin ? 'meet in a common line (two of the planes coincide)' : 'meet in a common line (no single point)' };
      }
      const pp = parallelPair(0, 1) || parallelPair(0, 2) || parallelPair(1, 2);
      if (pp) return { kind: 'parallel', text: 'have no common point: two of the planes are parallel and the third cuts them' };
      return { kind: 'prism', text: 'form a triangular prism (no common point; each pair meets in a line, and the three lines are parallel)' };
    }
    // rank 1: all normals parallel
    if (rA === 1) return { kind: 'coincide', text: 'coincide (all three are the same plane)' };
    const c01 = coin(0, 1), c02 = coin(0, 2), c12 = coin(1, 2);
    if (c01 || c02 || c12) return { kind: 'parallel', text: 'have no common point: two of the planes coincide and the third is parallel to them' };
    return { kind: 'parallel', text: 'are three parallel planes with no common point' };
  }

  const core = { sub, add, mul, dot, cross, mag, rank, parsePlanes, parseLine, parsePoint, pointPlane, linePlane, twoPlanes, classify3, planeText, normalDistance, fmtN, fmtD, fmtV, chooseYaw };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- 3D drawing helpers ---- */
  const CUBE = [];
  for (let i = 0; i < 8; i++) CUBE.push([i & 1 ? LIM : -LIM, i & 2 ? LIM : -LIM, i & 4 ? LIM : -LIM]);
  const EDGES = [];
  for (let i = 0; i < 8; i++) for (let b = 0; b < 3; b++) if (!(i & (1 << b))) EDGES.push([i, i | (1 << b)]);

  function planePolygon(p) {
    // intersection of the plane with the cube [-LIM, LIM]^3 as an ordered polygon (possibly empty)
    const pts = [];
    const f = (q) => dot(p.n, q) - p.d;
    const push = (q) => { if (!pts.some((r) => mag(sub(r, q)) < 1e-7)) pts.push(q); };
    EDGES.forEach(([i, j]) => {
      const a = CUBE[i], b = CUBE[j], fa = f(a), fb = f(b);
      if (Math.abs(fa) < 1e-9) push(a);
      if (Math.abs(fb) < 1e-9) push(b);
      if (fa * fb < 0) push(add(a, mul(fa / (fa - fb), sub(b, a))));
    });
    if (pts.length < 3) return [];
    const cen = mul(1 / pts.length, pts.reduce((s, q) => add(s, q), [0, 0, 0]));
    const nh = mul(1 / mag(p.n), p.n);
    const ref = Math.abs(nh[0]) < 0.9 ? [1, 0, 0] : [0, 1, 0];
    const u = cross(nh, ref), uu = mul(1 / mag(u), u), vv = cross(nh, uu);
    pts.sort((a, b) => Math.atan2(dot(sub(a, cen), vv), dot(sub(a, cen), uu)) - Math.atan2(dot(sub(b, cen), vv), dot(sub(b, cen), uu)));
    return pts;
  }
  function clipLine(a, d) {
    // the part of a + t d inside the cube, or null
    let lo = -Infinity, hi = Infinity;
    for (let i = 0; i < 3; i++) {
      if (Math.abs(d[i]) < 1e-12) { if (a[i] < -LIM || a[i] > LIM) return null; continue; }
      let t1 = (-LIM - a[i]) / d[i], t2 = (LIM - a[i]) / d[i];
      if (t1 > t2) [t1, t2] = [t2, t1];
      lo = Math.max(lo, t1); hi = Math.min(hi, t2);
    }
    return lo < hi ? [add(a, mul(lo, d)), add(a, mul(hi, d))] : null;
  }

  W.register('fm-planes', function (el, o) {
    const warn = [];
    const DEFAULT = [{ n: [1, 2, 2], d: 6 }];
    const pp = parsePlanes(o['planes'], DEFAULT); warn.push(...pp.warn);
    const pl = parseLine(o['line']); warn.push(...pl.warn);
    const pt = parsePoint(o['point']); warn.push(...pt.warn);
    const start = { planes: pp.planes.map((p) => p.n.concat([p.d])), line: pl.line ? pl.line.a.concat(pl.line.d) : null, point: pt.point };

    const { body } = W.frame(el, 'Planes, lines and points in 3D', 'Edit any number, then drag the picture or use the turn buttons');
    const err = W.h('div', { class: 'w-err', role: 'status' });
    const showErr = (t) => { err.textContent = t; err.style.display = t ? '' : 'none'; };
    showErr(warn.join(' '));
    body.append(err);

    const fieldRow = (title, names, values, label, colour) => {
      const row = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end', gap: '6px 8px' } });
      row.append(W.h('span', { class: 'w-lab', style: { minWidth: '2.6em', fontWeight: 600, paddingBottom: '10px', color: colour || 'var(--ink-2)' } }, title));
      const fs = names.map((nm, i) => {
        const f = W.field({ label: nm, value: String(values[i]), type: 'number', step: 1, width: '3.4em', oninput: update });
        f.input.setAttribute('aria-label', `${label}: ${nm}`);
        row.append(f.el); return f;
      });
      return { row, fs };
    };
    const SUB = ['₁', '₂', '₃'], PCOL = ['var(--sc)', 'var(--sc2)', 'var(--ok)'];
    const planeFields = start.planes.map((v, k) => fieldRow(`Π${SUB[k]}`, ['a', 'b', 'c', 'd'], v, `Plane ${k + 1}`, PCOL[k]));
    body.append(W.h('div', { class: 'w-note' }, 'Plane Π: a x + b y + c z = d, with normal (a, b, c).'));
    planeFields.forEach((r) => body.append(r.row));
    let lineFields = null, pointFields = null;
    if (start.line) { lineFields = fieldRow('Line l', ['a₁', 'a₂', 'a₃', 'd₁', 'd₂', 'd₃'], start.line, 'Line', 'var(--red)'); body.append(W.h('div', { class: 'w-note' }, 'Line l: r = a + t d, with point a and direction d.'), lineFields.row); }
    if (start.point) { pointFields = fieldRow('Point P', ['x', 'y', 'z'], start.point, 'Point P', 'var(--ink)'); body.append(pointFields.row); }
    const reset = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm' }, 'Reset the numbers');
    reset.addEventListener('click', () => {
      planeFields.forEach((r, k) => r.fs.forEach((f, i) => { f.input.value = String(start.planes[k][i]); }));
      if (lineFields) lineFields.fs.forEach((f, i) => { f.input.value = String(start.line[i]); });
      if (pointFields) pointFields.fs.forEach((f, i) => { f.input.value = String(start.point[i]); });
      update();
    });
    body.append(W.h('div', { class: 'w-row' }, reset));

    const state = { ok: false, model: null };
    const v3 = W.view3d({ yaw: chooseYaw(start.planes.map((p) => p.slice(0, 3)), 0.42, 0.7), pitch: 0.42, scale: 20 });
    const cv = W.canvas(body, { height: 340, draw, label: 'Planes, lines and points in 3D, with turn buttons below', describe: describeScene });
    cv.wrap.style.touchAction = 'none'; cv.wrap.style.cursor = 'grab';
    W.orbit(cv.wrap, v3, cv.redraw);

    const rows = [];
    planeFields.forEach((_, k) => rows.push([`n${k}`, `Π${SUB[k]}: normal and distance from O`]));
    if (start.line) planeFields.forEach((_, k) => rows.push([`l${k}`, `Line l and Π${SUB[k]}`]));
    if (start.point) planeFields.forEach((_, k) => rows.push([`p${k}`, `P and Π${SUB[k]}`]));
    const pairs = [];
    for (let i = 0; i < planeFields.length; i++) for (let j = i + 1; j < planeFields.length; j++) { pairs.push([i, j]); rows.push([`pair${i}${j}`, `Π${SUB[i]} and Π${SUB[j]}`]); }
    if (planeFields.length === 3) rows.push(['triple', 'The three planes']);
    const R = W.readout(rows);
    body.append(R.el, W.h('div', { class: 'w-note' }, 'Planes are drawn only inside the cube from −5 to 5. The line of intersection is given by its point nearest O. Try: change d and the plane slides along its normal.'));

    function read() {
      const planes = [];
      for (let k = 0; k < planeFields.length; k++) {
        const v = planeFields[k].fs.map((f) => parseFloat(f.input.value));
        if (!v.every((x) => isFinite(x) && Math.abs(x) <= MAXV)) return { error: `Enter a number from −${MAXV} to ${MAXV} in every box of Π${SUB[k]}.` };
        if (Math.hypot(v[0], v[1], v[2]) < EPS) return { error: `Π${SUB[k]} needs a, b, c not all zero.` };
        planes.push({ n: v.slice(0, 3), d: v[3] });
      }
      let line = null, point = null;
      if (lineFields) {
        const v = lineFields.fs.map((f) => parseFloat(f.input.value));
        if (!v.every((x) => isFinite(x) && Math.abs(x) <= MAXV)) return { error: `Enter a number from −${MAXV} to ${MAXV} in every box of line l.` };
        if (mag(v.slice(3)) < EPS) return { error: 'The direction of line l cannot be (0, 0, 0).' };
        line = { a: v.slice(0, 3), d: v.slice(3) };
      }
      if (pointFields) {
        const v = pointFields.fs.map((f) => parseFloat(f.input.value));
        if (!v.every((x) => isFinite(x) && Math.abs(x) <= MAXV)) return { error: `Enter a number from −${MAXV} to ${MAXV} in every box of P.` };
        point = v;
      }
      return { planes, line, point };
    }

    function lineText(r) {
      if (r.kind === 'meets') return `meets it at ${fmtV(r.point.map(clean))}; angle between line and plane ${fmtN(r.angle)}°`;
      if (r.kind === 'in') return 'lies in the plane; angle 0°';
      return `is parallel to the plane, ${fmtD(r.gap)} away; angle 0°`;
    }
    function update() {
      const m = read();
      if (m.error) { showErr(m.error); state.ok = false; cv.redraw(); return; }
      showErr(warn.join(' '));
      m.polys = m.planes.map(planePolygon);
      m.pp = m.planes.map((p) => (m.point ? pointPlane(m.point, p) : null));
      m.lp = m.planes.map((p) => (m.line ? linePlane(m.line, p) : null));
      m.two = pairs.map(([i, j]) => twoPlanes(m.planes[i], m.planes[j]));
      m.three = m.planes.length === 3 ? classify3(m.planes) : null;
      state.model = m; state.ok = true;
      m.planes.forEach((p, k) => R.set(`n${k}`, `n = ${fmtV(p.n)}; ${planeText(p)}; distance ${fmtD(normalDistance(p))}`));
      if (m.line) m.lp.forEach((r, k) => R.set(`l${k}`, lineText(r)));
      if (m.point) m.pp.forEach((r, k) => R.set(`p${k}`, r.on ? 'P lies in the plane' : `foot ${fmtV(r.foot.map(clean))}; distance ${fmtD(r.dist)}`));
      pairs.forEach(([i, j], idx) => {
        const r = m.two[idx];
        R.set(`pair${i}${j}`, r.kind === 'line' ? `angle ${fmtN(r.angle)}°; meet in the line through ${fmtV(r.point.map(clean))} with direction ${fmtV(r.dir.map(clean))}`
          : r.kind === 'coincide' ? 'the same plane' : `parallel, ${fmtD(r.gap)} apart`);
      });
      if (m.three) R.set('triple', m.three.text);
      cv.redraw();
    }
    function describeScene() {
      if (!state.ok || !state.model) return 'No picture: a box above needs a valid number.';
      const m = state.model;
      let s = m.planes.map((p, k) => `Plane ${k + 1}: ${planeText(p)}, normal ${fmtV(p.n)}`).join('. ') + '.';
      if (m.line) s += ' ' + m.lp.map((r, k) => `Line and plane ${k + 1}: ${lineText(r)}.`).join(' ');
      if (m.point) s += ' ' + m.pp.map((r, k) => (r.on ? `P lies in plane ${k + 1}.` : `P is ${fmtD(r.dist)} from plane ${k + 1}.`)).join(' ');
      if (m.three) s += ' The three planes ' + m.three.text + '.';
      else if (m.two.length) s += ' ' + (m.two[0].kind === 'line' ? `The planes meet at ${fmtN(m.two[0].angle)} degrees along a line.` : 'The planes are parallel.');
      return s;
    }

    function draw(ctx, w, h, c) {
      if (!(w > 2) || !(h > 2)) return;
      if (!state.ok || !state.model) {
        ctx.fillStyle = c.ink2; ctx.font = `13px ${c.font}`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('Fix the numbers above to see the picture.', w / 2, h / 2); return;
      }
      const m = state.model;
      v3.scale = Math.min(w, h) * 0.05;
      const pr = (p) => v3.project(p[0], p[1], p[2], w, h);
      // which depth direction is "far": larger y is further into the page
      const farSign = Math.sign(pr([0, 1, 0])[2] - pr([0, 0, 0])[2]) || 1;
      const seg = (a, b, col, lw, dash) => { const p = pr(a), q = pr(b); ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(q[0], q[1]); ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.setLineDash(dash || []); ctx.stroke(); ctx.setLineDash([]); };
      const dotAt = (p, r, col) => { const q = pr(p); ctx.beginPath(); ctx.arc(q[0], q[1], r, 0, Math.PI * 2); ctx.fillStyle = col; ctx.fill(); };
      const text = (p, t, col, dx, dy) => { const q = pr(p); ctx.fillStyle = col; ctx.font = `12px ${c.font}`; ctx.textAlign = 'left'; ctx.textBaseline = 'middle'; ctx.fillText(t, q[0] + dx, q[1] + dy); };
      const arrow = (a, b, col) => {
        const p = pr(a), q = pr(b), dx = q[0] - p[0], dy = q[1] - p[1], L = Math.hypot(dx, dy);
        seg(a, b, col, 2);
        if (L < 6) return;
        const ux = dx / L, uy = dy / L;
        ctx.beginPath(); ctx.moveTo(q[0], q[1]); ctx.lineTo(q[0] - 9 * ux + 4 * uy, q[1] - 9 * uy - 4 * ux); ctx.lineTo(q[0] - 9 * ux - 4 * uy, q[1] - 9 * uy + 4 * ux); ctx.closePath(); ctx.fillStyle = col; ctx.fill();
      };
      // cube: far edges dashed and light, near edges solid
      const dep = (p) => pr(p)[2] * farSign;
      EDGES.forEach(([i, j]) => {
        const far = (dep(CUBE[i]) + dep(CUBE[j])) / 2;
        const mid = (dep(CUBE[0]) + dep(CUBE[7])) / 2;
        const isFar = far > mid;
        seg(CUBE[i], CUBE[j], c.ink3, isFar ? 0.8 : 1.4, isFar ? [3, 3] : []);
      });
      // axes
      [[[LIM, 0, 0], 'x'], [[0, LIM, 0], 'y'], [[0, 0, LIM], 'z']].forEach(([end, nm]) => {
        seg([0, 0, 0], end, c.ink2, 1.2, [5, 3]);
        text(mul(1.12, end), nm, c.ink2, -3, 0);
      });
      dotAt([0, 0, 0], 2.5, c.ink2); text([0, 0, 0], 'O', c.ink2, 4, 9);
      // planes
      const cols = [c.sc, c.sc2, c.ok];
      m.planes.forEach((p, k) => {
        const poly = m.polys[k];
        if (!poly.length) return;
        const q = poly.map(pr);
        ctx.beginPath(); q.forEach((a, i) => (i ? ctx.lineTo(a[0], a[1]) : ctx.moveTo(a[0], a[1]))); ctx.closePath();
        ctx.globalAlpha = 0.16; ctx.fillStyle = cols[k]; ctx.fill(); ctx.globalAlpha = 1;
        ctx.strokeStyle = cols[k]; ctx.lineWidth = 1.6; ctx.stroke();
        const cen = mul(1 / poly.length, poly.reduce((s, a) => add(s, a), [0, 0, 0]));
        const nh = mul(1 / mag(p.n), p.n);
        arrow(cen, add(cen, mul(2.4, nh)), cols[k]);
        text(add(cen, mul(2.9, nh)), `n${SUB[k]}`, cols[k], 4, -2);
        text(poly[0], `Π${SUB[k]}`, cols[k], 5, -6);
      });
      // line and its meeting points
      if (m.line) {
        const part = clipLine(m.line.a, m.line.d);
        if (part) { seg(part[0], part[1], c.red, 2.4); text(part[1], 'l', c.red, 6, -4); }
        m.lp.forEach((r) => { if (r.kind === 'meets' && r.point.every((x) => Math.abs(x) <= LIM + 0.5)) dotAt(r.point, 4.5, c.ink); });
      }
      // intersection of the planes
      m.two.forEach((r) => {
        if (r.kind !== 'line') return;
        const part = clipLine(r.point, r.dir);
        if (part) seg(part[0], part[1], c.red, 2.4, [7, 3]);
      });
      if (m.three && m.three.kind === 'point' && m.three.point.every((x) => Math.abs(x) <= LIM + 0.5)) { dotAt(m.three.point, 5, c.red); text(m.three.point, fmtV(m.three.point.map(clean)), c.red, 7, -8); }
      // point and foot
      if (m.point) {
        m.pp.forEach((r, k) => { if (!r.on) { seg(m.point, r.foot, cols[k], 1.4, [4, 3]); dotAt(r.foot, 3.5, cols[k]); } });
        dotAt(m.point, 4.5, c.ink); text(m.point, 'P', c.ink, 6, -6);
      }
    }
    update();
  });
})();
