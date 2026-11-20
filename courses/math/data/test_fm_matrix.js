// Node test for the logic of widgets/fm-matrix.js (run in the course folder: node data/test_fm_matrix.js)
const L = require(process.cwd() + '/widgets/fm-matrix.js');
const assert = require('assert');
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, `${a} != ${b}`);
const lines = (m) => L.invariantLines(m);
let r = lines([1, 1, 0, 1]);
assert.equal(r.lines.length, 1); near(r.lines[0].m, 0); assert(r.lines[0].fixed); assert.equal(r.vertical, null);
r = lines([0.5, -0.866, 0.866, 0.5]); assert.equal(r.lines.length, 0); assert.equal(r.vertical, null);
r = lines([0, -1, 1, 0]); assert.equal(r.lines.length, 0);
r = lines([-1, 0, 0, -1]); assert(r.all && !r.identity);
r = lines([0.5, 0.8660254037844386, 0.8660254037844386, -0.5]);
assert.equal(r.lines.length, 2); near(r.lines[0].m, -1 / Math.tan(Math.PI / 6), 1e-9); near(r.lines[1].m, Math.tan(Math.PI / 6), 1e-9);
assert(r.lines[1].fixed && !r.lines[0].fixed); near(r.lines[0].lam, -1, 1e-9);
r = lines([0, 1, 1, 0]); near(r.lines[0].m, -1); near(r.lines[1].m, 1); assert(r.lines[1].fixed && !r.lines[0].fixed);
r = lines([1, 0, 0, -1]); assert.equal(r.lines.length, 1); near(r.lines[0].m, 0); assert(r.lines[0].fixed); assert(r.vertical && !r.vertical.fixed);
r = lines([2, 0, 0, 1]); near(r.lines[0].m, 0); near(r.lines[0].lam, 2); assert(!r.lines[0].fixed); assert(r.vertical.fixed);
r = lines([2, 0, 0, 2]); assert(r.all && !r.identity); r = lines([1, 0, 0, 1]); assert(r.all && r.identity);
r = lines([3, 1, 2, 2]); assert.equal(r.lines.length, 2); near(r.lines[0].m, -2); near(r.lines[1].m, 1);
near(r.lines[0].lam, 1); assert(r.lines[0].fixed); near(r.lines[1].lam, 4); assert.equal(r.vertical, null);
r = lines([1, 2, 3, 2]); near(r.lines[0].m, -1); near(r.lines[1].m, 1.5);
r = lines([2, -1, 1, 0]); assert.equal(r.lines.length, 1); near(r.lines[0].m, 1); assert(r.lines[0].fixed);
r = lines([3, -2, 1, 0]); near(r.lines[0].m, 0.5); near(r.lines[1].m, 1); assert(r.lines[1].fixed);
r = lines([1, 0, 2, 1]); assert.equal(r.lines.length, 0); assert(r.vertical.fixed);
r = lines([1, 2, 2, 4]); assert.equal(r.lines.length, 2);
near(L.det([3, -2, 4, 5]), 23); assert.deepEqual(L.inverse([1, 2, 2, 4]), null);
const inv = L.inverse([3, -2, 4, 5]); near(inv[0], 5 / 23); near(inv[1], 2 / 23); near(inv[2], -4 / 23); near(inv[3], 3 / 23);
r = lines([0, 0, 0, 0]); assert(r.all);
for (let i = 0; i < 3000; i++) {
  const m = [0, 0, 0, 0].map(() => Math.round((Math.random() * 8 - 4) * 2) / 2);
  const il = lines(m);
  const test = (p) => { const q = L.apply(m, p); return Math.abs(q[0] * p[1] - q[1] * p[0]) < 1e-9; };
  if (il.all) continue;
  il.lines.forEach((l) => assert(test([1, l.m]), `line ${l.m} of ${m}`));
  if (il.vertical) assert(test([0, 1]));
  for (let k = -8; k <= 8; k++) {
    const mm = k / 2;
    if (test([1, mm])) assert(il.lines.some((l) => Math.abs(l.m - mm) < 1e-9), `missing ${mm} for ${m}`);
  }
  if (test([0, 1])) assert(il.vertical, `missing vertical for ${m}`);
}
let e = L.eigen([3, 1, 2, 2]); near(e.values[0].lam, 4); near(e.values[1].lam, 1);
e = L.eigen([0, -1, 1, 0]); assert(e.complex);
e = L.eigen([2, 0, 0, 2]); assert(e.scalar && e.values.length === 1);
e = L.eigen([1, 1, 0, 1]); assert.equal(e.values.length, 1); near(e.values[0].lam, 1);
assert.equal(L.parseMatrix('1,2,3', [1, 1, 0, 1]).m.join(), '1,0,0,1'); assert(L.parseMatrix('1,2,3', [1, 1, 0, 1]).err);
assert(L.parseMatrix('a,b,c,d', [1, 1, 0, 1]).err); assert.equal(L.parseMatrix('', [1, 1, 0, 1]).m.join(), '1,1,0,1');
assert.equal(L.parseMatrix('99,0,0,1', [1, 1, 0, 1]).m[0], 10);
const d = L.describeMatrix([3, 1, 2, 2]); console.log(d.lines, '|', d.fixed, '|', d.eigenvectors);
console.log(L.describeMatrix([0, -1, 1, 0]).lines, '|', L.describeMatrix([1, 2, 2, 4]).orient, '|', L.describeMatrix([0.5, 0.866, 0.866, -0.5]).orient);
console.log('fm-matrix logic ok');
