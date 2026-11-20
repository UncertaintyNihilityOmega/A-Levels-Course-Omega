// Node test for widgets/fm-maclaurin.js: coefficients against MF19 and against the functions themselves.
// Run from the course folder: node data/fm-maclaurin-test.js
const c = require(process.cwd() + '/widgets/fm-maclaurin.js');
const assert = require('assert');
// MF19 series
assert.deepStrictEqual(c.coef('exp', 4), [1, 24]);
assert.deepStrictEqual(c.coef('sin', 3), [-1, 6]);
assert.deepStrictEqual(c.coef('sin', 5), [1, 120]);
assert.deepStrictEqual(c.coef('sin', 4), [0, 1]);
assert.deepStrictEqual(c.coef('cos', 2), [-1, 2]);
assert.deepStrictEqual(c.coef('cos', 4), [1, 24]);
assert.deepStrictEqual(c.coef('cos', 0), [1, 1]);
assert.deepStrictEqual(c.coef('ln1p', 1), [1, 1]);
assert.deepStrictEqual(c.coef('ln1p', 2), [-1, 2]);
assert.deepStrictEqual(c.coef('ln1p', 3), [1, 3]);
assert.deepStrictEqual(c.coef('ln1p', 0), [0, 1]);
assert.deepStrictEqual(c.coef('atan', 3), [-1, 3]);
assert.deepStrictEqual(c.coef('atan', 5), [1, 5]);
assert.deepStrictEqual(c.coef('sinh', 3), [1, 6]);
assert.deepStrictEqual(c.coef('cosh', 4), [1, 24]);
assert.deepStrictEqual(c.coef('tan', 3), [1, 3]);
assert.deepStrictEqual(c.coef('tan', 5), [2, 15]);
assert.deepStrictEqual(c.coef('tan', 7), [17, 315]);
// every polynomial of degree 15 matches the function at a small x
const f = { exp: Math.exp, sin: Math.sin, cos: Math.cos, ln1p: (x) => Math.log(1 + x), atan: Math.atan, sinh: Math.sinh, cosh: Math.cosh, tan: Math.tan };
for (const fn of Object.keys(f)) {
  for (const x of [0.2, -0.2, 0.5]) {
    const err = Math.abs(f[fn](x) - c.evalPoly(fn, 15, x));
    assert(err < 1e-5, `${fn} at ${x}: error ${err}`);
  }
}
// tan: the table equals the coefficients from y' = 1 + y^2 (floating point recurrence)
const N = 16, a = new Array(N).fill(0);   // a[k] = coefficient of x^k in tan x
a[1] = 1;
for (let k = 2; k < N; k++) {              // k a[k] = coefficient of x^(k-1) in 1 + y^2
  let s = 0; for (let i = 1; i < k - 1; i++) s += a[i] * a[k - 1 - i];
  a[k] = s / k;
}
for (let k = 1; k <= 15; k += 2) {
  const [n, d] = c.coef('tan', k);
  assert(Math.abs(n / d - a[k]) < 1e-12 * Math.max(1, a[k]), `tan x^${k}: table ${n}/${d}, recurrence ${a[k]}`);
}
// text
assert.strictEqual(c.polyText('sin', 7, 4), 'x − x³/6 + x⁵/120 − x⁷/5040');
assert.strictEqual(c.polyText('sin', 9, 4), 'x − x³/6 + x⁵/120 − x⁷/5040 + …');
assert.strictEqual(c.polyText('sin', 2, 4), 'x');
assert.strictEqual(c.polyText('sin', 0, 4), '0');
assert.strictEqual(c.polyText('cos', 4, 4), '1 − x²/2 + x⁴/24');
assert.strictEqual(c.polyText('ln1p', 4, 4), 'x − x²/2 + x³/3 − x⁴/4');
assert.strictEqual(c.polyText('tan', 5, 4), 'x + x³/3 + 2x⁵/15');
assert.strictEqual(c.polyText('exp', 3, 4), '1 + x + x²/2 + x³/6');
console.log('fm-maclaurin core ok');
