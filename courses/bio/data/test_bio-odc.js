// data/test_bio-odc.js: run `node data/test_bio-odc.js` in the course folder; checks the maths of widgets/bio-odc.js
// against the numbers quoted in chapters/bio.oxygen.md and checks/bio.oxygen.py.
const assert = require('assert');
const path = require('path');
const { p50, sat, unloaded, num, clamp } = require(path.join(process.cwd(), 'widgets', 'bio-odc.js'));
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
near(p50(5.3), 3.4); near(p50(10), 4.575); near(p50(4), 3.4 + 0.25 * (4 - 5.3)); near(p50(99), 4.575); near(p50(-5), p50(4));
assert.strictEqual(Math.round(sat(13, 5.3)), 97); assert.strictEqual(Math.round(sat(4, 5.3)), 61);
assert.strictEqual(Math.round(sat(5, 5.3)), 74); assert.strictEqual(Math.round(sat(8, 5.3)), 91);
assert.strictEqual(Math.round(sat(4, 10)), 41); near(sat(4, 10), 41.0, 0.05); near(sat(4, 5.3), 60.8, 0.05); near(sat(13, 5.3), 97.4, 0.05);
near(sat(0, 5.3), 0); near(sat(-1, 5.3), 0); assert(sat(14, 5.3) < 100 && sat(14, 5.3) > 97);
assert.strictEqual(unloaded(13, 4, 5.3), 36);
assert(unloaded(13, 4, 10) > unloaded(13, 4, 5.3));
for (let p = 0.1; p < 14; p += 0.1) assert(sat(p + 0.1, 7) > sat(p, 7), 'increasing');
for (let p = 0.5; p < 14; p += 0.5) assert(sat(p, 8) < sat(p, 5.3), 'curve shifts right with pCO2');
assert.strictEqual(num('abc', 5.3, 4, 10), 5.3); assert.strictEqual(num('99', 5.3, 4, 10), 10); assert.strictEqual(num(undefined, 5.3, 4, 10), 5.3);
assert.strictEqual(clamp(3, 4, 10), 4);
console.log('bio-odc maths ok');
