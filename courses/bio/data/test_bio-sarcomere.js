// data/test_bio-sarcomere.js: run `node data/test_bio-sarcomere.js` in the course folder; checks widgets/bio-sarcomere.js against chapters/bio.synapses.md.
const assert = require('assert');
const path = require('path');
const m = require(path.join(process.cwd(), 'widgets', 'bio-sarcomere.js'));
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
// chapter values (x20 000 micrograph: 50 mm = 2.5 um relaxed, 40 mm = 2.0 um contracted)
let b = m.bands(2.5); near(b.A, 1.6); near(b.I, 0.9); near(b.H, 0.5); near(b.overlap, 3.6 - 2.5);
b = m.bands(2.0); near(b.I, 0.4); near(b.H, 0); near(b.overlap, 1.6);
b = m.bands(3.0); near(b.H, 1.0); near(b.I, 1.4);
b = m.bands(2.4); near(b.I, 0.8); near(b.H, 0.4);
for (let L = 1.8; L <= 3.4001; L += 0.05) { const x = m.bands(L); near(x.A, 1.6); assert(x.I >= 0 && x.H >= 0 && x.overlap >= 0); near(x.I + 1.6, L); near(x.overlap, 3.6 - L, 1e-9); }
// rules
assert.deepStrictEqual(m.effLen(2.0, 2.5, false, true, NaN), { len: 2.5, mode: 'relaxed' });   // no calcium: cannot shorten
assert.strictEqual(m.effLen(3.2, 2.5, false, true, NaN).len, 3.2);                              // stretching allowed
assert.deepStrictEqual(m.effLen(2.0, 2.5, true, true, NaN), { len: 2.0, mode: 'active' });
assert.deepStrictEqual(m.effLen(1.8, 2.5, true, false, 2.2), { len: 2.2, mode: 'rigor' });      // frozen
assert.strictEqual(m.effLen(NaN, 2.5, true, true, NaN).len, 2.5);
assert.strictEqual(m.effLen(99, 2.5, true, true, NaN).len, 3.4); assert.strictEqual(m.effLen(-5, 2.5, true, true, NaN).len, 1.8);
assert.strictEqual(m.numOr('x', 2.5, 2.2, 3.0), 2.5); assert.strictEqual(m.numOr('9', 2.5, 2.2, 3.0), 3.0);
console.log('ok');
