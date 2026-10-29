// data/test_bio-rq.js: run `node data/test_bio-rq.js` in the course folder; checks the maths of widgets/bio-rq.js
// against the numbers in chapters/bio.energy.md and checks/bio.energy.py.
const assert = require('assert');
const path = require('path');
const { balance, verdict, respiro, formulaText, numOr } = require(path.join(process.cwd(), 'widgets', 'bio-rq.js'));
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
// glucose, oleic acid, tripalmitin, malic acid, palmitic acid, sucrose
let b = balance(6, 12, 6); near(b.o2, 6); near(b.rq, 1); assert.strictEqual(b.eq, 'C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O');
b = balance(18, 34, 2); near(b.o2, 25.5); assert.strictEqual(b.rq.toFixed(2), '0.71'); assert(b.eq.includes('25.5 O₂') && b.eq.includes('17 H₂O'), b.eq);
b = balance(51, 98, 6); near(b.o2, 72.5); assert.strictEqual(b.rq.toFixed(2), '0.70');
b = balance(4, 6, 5); near(b.o2, 3); assert.strictEqual(b.rq.toFixed(2), '1.33');
b = balance(16, 32, 2); near(b.o2, 23); assert.strictEqual(b.rq.toFixed(2), '0.70');
b = balance(12, 22, 11); near(b.rq, 1);
b = balance(3, 8, 3); near(b.o2, 3.5); assert.strictEqual(b.rq.toFixed(2), '0.86');
// atom balance for many formulas
for (let x = 1; x <= 20; x += 3) for (let y = 0; y <= 40; y += 5) for (let z = 0; z <= 8; z += 2) {
  const r = balance(x, y, z);
  if (r.ok) near(z + 2 * r.o2, 2 * x + r.h2o, 1e-9);
}
// impossible and bad input never throw
assert.strictEqual(balance(1, 0, 2).ok, false);           // CO2 itself: needs no O2
assert.strictEqual(balance(0, 4, 0).ok, false);
assert.strictEqual(balance(NaN, 4, 0).ok, false);
assert.strictEqual(balance(2.5, 4, 0).ok, false);
assert.strictEqual(balance(6, -1, 0).ok, false);
assert.strictEqual(balance(500, 1, 1).ok, false);
assert(balance(2, 6, 1).ok);                               // ethanol
assert.strictEqual(formulaText(1, 4, 0), 'CH₄'); assert.strictEqual(formulaText(2, 0, 4), 'C₂O₄');
// verdicts
assert(verdict(1.0).includes('carbohydrate')); assert(verdict(0.7).includes('lipid')); assert(verdict(1.33).includes('> 1'));
assert(verdict(0.85).includes('mixture')); assert.strictEqual(verdict(NaN), ''); assert.strictEqual(verdict(-1), '');
// respirometer: chapter worked example and start values
let r = respiro(0.5, 42, 12); assert(r.ok); assert.strictEqual(Math.round(r.vo2), 33); assert.strictEqual(Math.round(r.vco2), 24); assert.strictEqual(r.rq.toFixed(2), '0.71');
near(r.vnet, Math.PI * 0.25 * 12); near(r.vo2 - r.vnet, r.vco2);
r = respiro(0.5, 40, 12); near(r.rq, 0.7);
r = respiro(0.35, 30, 6); assert.strictEqual(Math.round(r.vo2), 12); near(r.rq, 0.8);
r = respiro(0.5, 30, -6); assert(r.ok); near(r.rq, 1.2);               // drop moved away: more CO2 than O2
assert.strictEqual(respiro(0.5, 0, 0).ok, false); assert.strictEqual(respiro(0.5, 10, 20).ok, false);
assert.strictEqual(respiro(0, 10, 5).ok, false); assert.strictEqual(respiro(NaN, 10, 5).ok, false);
near(respiro(0.2, 40, 12).rq, respiro(1, 40, 12).rq);                   // radius cancels
assert.strictEqual(numOr('abc', 6, 1, 100), 6); assert.strictEqual(numOr('-5', 6, 1, 100), 1); assert.strictEqual(numOr('900', 6, 1, 100), 100);
console.log('bio-rq maths ok');
