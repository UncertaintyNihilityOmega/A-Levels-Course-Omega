// Node test for the logic of widgets/fm-planes.js (run in the course folder: node data/test_fm_planes.js)
const L = require(process.cwd() + '/widgets/fm-planes.js');
const assert = require('assert');
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, `${a} != ${b}`);
const nearV = (u, v, t = 1e-9) => u.forEach((x, i) => near(x, v[i], t));
const P = (a, b, c, d) => ({ n: [a, b, c], d });

// ---- three-plane classification: the five cases and the degenerate ones ----
let r = L.classify3([P(1, 0, 0, 1), P(0, 1, 0, 2), P(0, 0, 1, 3)]);
assert.equal(r.kind, 'point'); nearV(r.point, [1, 2, 3]);
r = L.classify3([P(1, 1, 1, 3), P(1, -1, 0, 0), P(2, 0, 1, 3)]); assert.equal(r.kind, 'line');
r = L.classify3([P(1, 1, 1, 3), P(1, -1, 0, 0), P(2, 0, 1, 5)]); assert.equal(r.kind, 'prism');
r = L.classify3([P(1, 1, 1, 3), P(1, 1, 1, 5), P(1, -1, 0, 0)]); assert.equal(r.kind, 'parallel'); assert(/two of the planes are parallel/.test(r.text));
r = L.classify3([P(1, 1, 1, 3), P(2, 2, 2, 6), P(3, 3, 3, 9)]); assert.equal(r.kind, 'coincide');
r = L.classify3([P(1, 1, 1, 1), P(1, 1, 1, 2), P(1, 1, 1, 3)]); assert.equal(r.kind, 'parallel'); assert(/three parallel/.test(r.text));
r = L.classify3([P(1, 1, 1, 3), P(2, 2, 2, 6), P(1, -1, 0, 0)]); assert.equal(r.kind, 'line'); assert(/coincide/.test(r.text));
r = L.classify3([P(1, 1, 1, 3), P(2, 2, 2, 6), P(1, 1, 1, 5)]); assert.equal(r.kind, 'parallel'); assert(/coincide and the third/.test(r.text));
// a point example with awkward numbers
r = L.classify3([P(2, -1, 3, 7), P(1, 4, -2, -1), P(3, 1, 1, 6)]);
assert.equal(r.kind, 'point');
[[2, -1, 3, 7], [1, 4, -2, -1], [3, 1, 1, 6]].forEach((q) => near(q[0] * r.point[0] + q[1] * r.point[1] + q[2] * r.point[2], q[3], 1e-9));
// scaled equations do not change the verdict
r = L.classify3([P(0.001, 0.001, 0.001, 0.003), P(1000, -1000, 0, 0), P(2, 0, 1, 3)]); assert.equal(r.kind, 'line');
// the chapter's pairs and the prism from the systems chapter
r = L.classify3([P(1, 2, -1, 4), P(2, 4, -2, 9), P(1, -1, 2, 3)]); assert.equal(r.kind, 'parallel');

// random: the verdict agrees with brute-force solving of random integer planes
const rnd = (() => { let s = 12345; return () => ((s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff); })();
const ri = (k) => Math.round(rnd() * 2 * k - k);
for (let i = 0; i < 4000; i++) {
  const ps = [0, 1, 2].map(() => P(ri(3), ri(3), ri(3), ri(5))).filter((p) => Math.hypot(...p.n) > 0);
  if (ps.length < 3) continue;
  const c = L.classify3(ps);
  const D = L.dot(ps[0].n, L.cross(ps[1].n, ps[2].n));
  if (D !== 0) { assert.equal(c.kind, 'point'); ps.forEach((p) => near(L.dot(p.n, c.point), p.d, 1e-7)); }
  else assert.notEqual(c.kind, 'point');
  assert.equal(L.rank(ps.map((p) => p.n)), D !== 0 ? 3 : L.rank(ps.map((p) => p.n)));
}

// ---- two planes ----
let t = L.twoPlanes(P(1, 2, -2, 5), P(2, -1, 1, 5));
assert.equal(t.kind, 'line'); near(t.angle, 74.2, 0.05); nearV(t.dir, [0, -5, -5]);
nearV(t.point, [3, 0.5, -0.5]);               // the point of the line nearest to O
[P(1, 2, -2, 5), P(2, -1, 1, 5)].forEach((p) => near(L.dot(p.n, t.point), p.d));
t = L.twoPlanes(P(2, 1, -1, 4), P(1, -1, 2, 5)); near(t.angle, 80.4, 0.05); nearV(t.dir, [1, -5, -3]);
t = L.twoPlanes(P(2, 3, -1, -8), P(4, 6, -2, 10)); assert.equal(t.kind, 'parallel'); near(t.gap, 13 / Math.sqrt(14) , 1e-9 * 100);
t = L.twoPlanes(P(1, 1, 1, 3), P(-2, -2, -2, -6)); assert.equal(t.kind, 'coincide');
t = L.twoPlanes(P(1, 0, 0, 0), P(1, 1, 1, 0)); near(t.angle, 54.7, 0.05);
t = L.twoPlanes(P(1, 2, 1, 6), P(2, 4, -1, 9)); assert.equal(t.kind, 'line'); nearV(t.dir, [-6, 3, 0]);
for (let i = 0; i < 2000; i++) {
  const a = P(ri(4), ri(4), ri(4), ri(8)), b = P(ri(4), ri(4), ri(4), ri(8));
  if (Math.hypot(...a.n) === 0 || Math.hypot(...b.n) === 0) continue;
  const q = L.twoPlanes(a, b);
  if (q.kind === 'line') { near(L.dot(a.n, q.point), a.d, 1e-7); near(L.dot(b.n, q.point), b.d, 1e-7); near(L.dot(q.point, q.dir), 0, 1e-7); }
}

// ---- line and plane ----
let lp = L.linePlane({ a: [1, 0, 2], d: [2, 1, -1] }, P(3, 1, -2, 8));
assert.equal(lp.kind, 'meets'); nearV(lp.point, [3, 1, 1]); near(lp.angle, 79.1, 0.05);
lp = L.linePlane({ a: [1, 0, 2], d: [2, 1, -1] }, P(1, 1, 3, 7)); assert.equal(lp.kind, 'in');
lp = L.linePlane({ a: [1, 0, 2], d: [2, 1, -1] }, P(1, 1, 3, 10)); assert.equal(lp.kind, 'parallel'); near(lp.gap, 3 / Math.sqrt(11));
lp = L.linePlane({ a: [2, 0, -1], d: [1, 2, -1] }, P(1, -2, 3, 5)); nearV(lp.point, [1, -2, 0]); near(lp.angle, 40.9, 0.05);

// ---- point and plane ----
let pp = L.pointPlane([3, -1, 4], P(2, 3, -1, -8));
nearV(pp.foot, [2, -2.5, 4.5]); near(pp.dist, 7 / Math.sqrt(14)); assert(!pp.on);
pp = L.pointPlane([-1, 3, -2], P(2, -1, 2, 9)); nearV(pp.foot, [3, 1, 2]); near(pp.dist, 6);
pp = L.pointPlane([2, 1, 3], P(1, -2, 4, 12)); assert(pp.on);

// ---- parsing and bad attributes ----
let ps = L.parsePlanes('1,2,2,6; 3,x,1,2; 0,0,0,5; 1,1,1,1,1', [P(1, 2, 2, 6)]);
assert.equal(ps.planes.length, 1); assert(ps.warn.length >= 3);
ps = L.parsePlanes(undefined, [P(1, 2, 2, 6)]); assert.equal(ps.planes.length, 1); assert.equal(ps.warn.length, 0);
ps = L.parsePlanes('1,0,0,1;0,1,0,1;0,0,1,1;1,1,1,1', []); assert.equal(ps.planes.length, 3); assert(ps.warn.length === 1);
ps = L.parsePlanes('garbage', [P(1, 2, 2, 6)]); assert.equal(ps.planes[0].d, 6); assert(ps.warn.length >= 1);
ps = L.parsePlanes('−1,2,0,3', []); assert.deepEqual(ps.planes[0].n, [-1, 2, 0]);
assert.equal(L.parseLine('1,2,3|0,0,0').line, null);
assert.deepEqual(L.parseLine('1,2,3|4,5,6').line, { a: [1, 2, 3], d: [4, 5, 6] });
assert.equal(L.parseLine('nope').line, null); assert.equal(L.parsePoint('1,2').point, null);
assert.deepEqual(L.parsePoint('1,2,3').point, [1, 2, 3]);
assert.equal(L.planeText(P(1, -2, 0, 3)), 'x − 2y = 3');
assert.equal(L.planeText(P(0, -1, 2, 6)), '−y + 2z = 6');
console.log('ok');
