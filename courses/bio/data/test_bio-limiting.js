// data/test_bio-limiting.js: run `node data/test_bio-limiting.js` in the course folder; checks the maths of widgets/bio-limiting.js
// against the plateau values used in chapters/bio.limiting.md (40 and 70 at 25 degrees C; 36 at 15 degrees C).
const assert = require('assert');
const path = require('path');
const { pmax, rate, limiting, tfac, cfac, numOr, niceTop, TOPT } = require(path.join(process.cwd(), 'widgets', 'bio-limiting.js'));
const near = (a, b, t = 1e-6) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
near(pmax(0.04, 25), 40); near(pmax(0.12, 25), 70); near(tfac(25), 1);
assert(Math.abs(pmax(0.12, 15) - 35.6) < 0.2, String(pmax(0.12, 15)));
assert(TOPT > 29 && TOPT < 33, String(TOPT));
// rate rises with light, never exceeds min(aI, Pmax), and tends to Pmax
for (const [C, T] of [[0.04, 25], [0.12, 15], [0.01, 5], [0.15, 45], [0.1, 31]]) {
  let prev = -1;
  for (let I = 0; I <= 100; I += 5) {
    const r = rate(I, C, T);
    assert(r >= prev - 1e-9 && r <= Math.min(1.6 * I, pmax(C, T)) + 1e-9 && isFinite(r), `rate ${I} ${C} ${T}`);
    prev = r;
  }
  assert(rate(100, C, T) > 0.8 * pmax(C, T) || pmax(C, T) > 100);
}
near(rate(0, 0.04, 25), 0);
// initial slope is the same whatever CO2 and temperature are
near(rate(1, 0.04, 25) / 1, rate(1, 0.12, 25) / 1, 0.01);
// limiting factor logic
assert.strictEqual(limiting(0, 0.04, 25).kind, 'dark');
assert.strictEqual(limiting(10, 0.04, 25).kind, 'light');
let L = limiting(90, 0.04, 25); assert.strictEqual(L.kind, 'other'); assert.strictEqual(L.other, 'co2');
L = limiting(90, 0.15, 8); assert.strictEqual(L.kind, 'other'); assert.strictEqual(L.other, 'cold');
L = limiting(90, 0.15, 44); assert.strictEqual(L.kind, 'other'); assert.strictEqual(L.other, 'hot');
// high CO2 raises the plateau; temperature has little effect at low light
assert(pmax(0.15, 25) > pmax(0.04, 25));
assert(Math.abs(rate(8, 0.12, 15) - rate(8, 0.12, 25)) < 1.5);
// bad input never throws
assert.strictEqual(numOr('abc', 0.04, 0.01, 0.15), 0.04); assert.strictEqual(numOr('9', 0.04, 0.01, 0.15), 0.15);
assert(isFinite(rate(NaN || 0, 0.04, 25))); assert(niceTop(1000) >= 1000);
console.log('bio-limiting: ok');
