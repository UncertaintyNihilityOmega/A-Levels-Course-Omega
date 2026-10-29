// data/test_bio-hardy.js: node data/test_bio-hardy.js tests the maths of widgets/bio-hardy.js against the chapter's worked examples.
const assert = require('assert');
const H = require('../widgets/bio-hardy.js');
const near = (a, b, tol, m) => assert(Math.abs(a - b) <= tol, m + ': ' + a + ' vs ' + b);

// parsing
near(H.parseFreq('0.04').f, 0.04, 1e-12, '0.04'); near(H.parseFreq('4%').f, 0.04, 1e-12, '4%'); near(H.parseFreq(' 4 % ').f, 0.04, 1e-12, '4 %');
near(H.parseFreq('1 in 2500').f, 0.0004, 1e-12, '1 in 2500'); near(H.parseFreq('1/2500').f, 0.0004, 1e-12, '1/2500'); near(H.parseFreq('1:10').f, 0.1, 1e-12, '1:10');
near(H.parseFreq('1 in 1').f, 1, 1e-12, '1 in 1'); near(H.parseFreq('0,25').f, 0.25, 1e-12, 'comma decimal');
['', '   ', 'abc', '4', '1.2', '120%', '1 in 0', '-0.1', '1 in', null, undefined, '1 in 0.5'].forEach(function (s) {
  const r = H.parseFreq(s);
  if (s === '4') { assert(r.err && isNaN(r.f), 'plain 4 is outside 0-1'); return; }
  assert(r.err && isNaN(r.f), 'should reject ' + JSON.stringify(s));
});

// 1 in 2500
let r = H.solve('q2', 1 / 2500);
near(r.q, 0.02, 1e-12, 'q'); near(r.p, 0.98, 1e-12, 'p'); near(r.h, 0.0392, 1e-12, '2pq'); near(r.p2, 0.9604, 1e-12, 'p2'); near(r.q2, 0.0004, 1e-12, 'q2');
near(r.p2 + r.h + r.q2, 1, 1e-12, 'sum');
// 9 % recessive
r = H.solve('q2', 0.09); near(r.q, 0.3, 1e-12, 'q'); near(r.h, 0.42, 1e-12, '2pq'); near(r.p2, 0.49, 1e-12, 'p2');
// p2 given
r = H.solve('p2', 0.49); near(r.p, 0.7, 1e-12, 'p'); near(r.q, 0.3, 1e-12, 'q'); near(r.h, 0.42, 1e-12, '2pq');
// 2pq given: 0.42 -> q = 0.3 (smaller)
r = H.solve('h', 0.42); near(r.q, 0.3, 1e-9, 'q from 2pq'); near(r.p, 0.7, 1e-9, 'p from 2pq'); assert(r.note.includes('swapped'));
near(H.solve('h', 0.5).q, 0.5, 1e-9, '2pq = 0.5'); assert(H.solve('h', 0.51).err);
// extremes
r = H.solve('q2', 0); assert.strictEqual(r.q, 0); assert.strictEqual(r.p, 1);
r = H.solve('q2', 1); assert.strictEqual(r.q, 1); assert.strictEqual(r.h, 0);
assert(H.solve('q2', 1.5).err); assert(H.solve('q2', NaN).err); assert(H.solve('q2', -0.1).err);
// fmt never prints NaN/undefined
['NaN', 'undefined', 'Infinity'].forEach(function (bad) {
  [0, 1e-9, 0.0004, 0.0392, 1, NaN, Infinity].forEach(function (x) { assert(!H.fmt(x).includes(bad) || bad === 'NaN' && false, 'fmt ' + x); });
});

// drift: a seeded generator
function lcg(seed) { let s = seed >>> 0; return function () { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; }; }
const run = H.drift(100, 0.5, 50, 5, lcg(1));
assert.strictEqual(run.length, 5); run.forEach(function (l) { assert.strictEqual(l.length, 51); assert.strictEqual(l[0], 0.5); l.forEach(function (v) { assert(v >= 0 && v <= 1); }); });
// same seed, same lines
assert.deepStrictEqual(H.drift(10, 0.5, 50, 5, lcg(3)), H.drift(10, 0.5, 50, 5, lcg(3)));
// once fixed or lost, stays so
H.drift(10, 0.5, 50, 20, lcg(9)).forEach(function (l) { for (let g = 1; g < l.length; g++) if (l[g - 1] === 0 || l[g - 1] === 1) assert.strictEqual(l[g], l[g - 1]); });
// small populations drift further and fix more often than large ones; the mean frequency stays near the start
function stat(n, reps) { const ls = H.drift(n, 0.5, 50, reps, lcg(42 + n)); let fixed = 0, dev = 0, mean = 0; ls.forEach(function (l) { const v = l[50]; if (v === 0 || v === 1) fixed++; dev += Math.abs(v - 0.5); mean += v; }); return { fixed: fixed / reps, dev: dev / reps, mean: mean / reps }; }
const s10 = stat(10, 400), s100 = stat(100, 400), s1000 = stat(1000, 100);
assert(s10.fixed > s100.fixed && s100.fixed >= s1000.fixed, 'fixation: ' + [s10.fixed, s100.fixed, s1000.fixed]);
assert(s10.dev > s100.dev && s100.dev > s1000.dev, 'deviation: ' + [s10.dev, s100.dev, s1000.dev]);
near(s10.mean, 0.5, 0.05, 'mean frequency stays near the start for N = 10');
assert(s10.fixed > 0.5 && s1000.fixed === 0, 'N = 10 mostly fixes; N = 1000 does not in 50 generations: ' + [s10.fixed, s1000.fixed]);
console.log('ok bio-hardy', JSON.stringify({ s10: s10, s100: s100, s1000: s1000 }));
