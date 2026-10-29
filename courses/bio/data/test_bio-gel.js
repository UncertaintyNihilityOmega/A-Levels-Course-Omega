// data/test_bio-gel.js: node data/test_bio-gel.js  -> tests the pure functions of widgets/bio-gel.js
const assert = require('assert');
const g = require('../widgets/bio-gel.js');
assert.deepStrictEqual(g.fragments(5000, [1200, 3100]), [1200, 1900, 1900]);
assert.deepStrictEqual(g.groups([1200, 1900, 1900]), [[1900, 2], [1200, 1]]);
assert.deepStrictEqual(g.parseCuts('1200, 3100', 5000).cuts, [1200, 3100]);
assert.deepStrictEqual(g.parseCuts('3100;1200 1200', 5000).cuts, [1200, 3100]);
assert.deepStrictEqual(g.parseCuts('0, 5000, abc, 12.5, -3, 400', 5000).bad, ['0', '5000', 'abc', '12.5', '-3']);
assert.deepStrictEqual(g.parseCuts('', 5000).cuts, []);
assert.deepStrictEqual(g.parseCuts(undefined, 5000).cuts, []);
assert.deepStrictEqual(g.presetCuts('A', 5000), [1200, 3100]);
assert.deepStrictEqual(g.presetCuts('B', 5000), [2000]);
assert.deepStrictEqual(g.presetCuts('AB', 5000), [1200, 2000, 3100]);
assert.deepStrictEqual(g.presetCuts('A', 200), [48, 124]);
assert.deepStrictEqual(g.fragments(200, []), [200]);
const M = 5750;
assert(g.travel(100, M) > g.travel(1000, M) && g.travel(1000, M) > g.travel(5000, M));
assert.strictEqual(g.travel(1, M), 1);
assert.strictEqual(g.travel(1e9, M), 0);
assert.strictEqual(g.travel(100, NaN), 0);
assert(isFinite(g.travel(NaN, M)));
// fragments always add up to the DNA length
for (const L of [200, 777, 5000, 20000]) for (const k of ['A', 'B', 'AB']) {
  const fr = g.fragments(L, g.presetCuts(k, L));
  assert.strictEqual(fr.reduce((a, b) => a + b, 0), L);
}
assert.strictEqual(g.numOr('abc', 5000, 200, 20000), 5000);
assert.strictEqual(g.numOr('1e9', 5000, 200, 20000), 20000);
console.log('ok');
