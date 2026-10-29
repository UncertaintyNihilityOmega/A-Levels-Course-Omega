// data/test_bio-ttest.js: node data/test_bio-ttest.js tests the maths of widgets/bio-ttest.js against the chapter's worked examples.
const assert = require('assert');
const T = require('../widgets/bio-ttest.js');
const near = (a, b, tol, m) => assert(Math.abs(a - b) <= tol, m + ': ' + a + ' vs ' + b);

// parsing
assert.deepStrictEqual(T.parseList('1, 2.5  3;4').vals, [1, 2.5, 3, 4]);
assert(T.parseList('1, x').err.includes('not a number'));
assert(T.parseList('5').err.includes('at least 2'));
assert(T.parseList('').err.includes('at least 2'));
assert(T.parseList(null).err.includes('at least 2'));
assert.deepStrictEqual(T.parseList('−2, 3').vals, [-2, 3]);
assert(T.parseList(Array(150).fill('1').join(',')).err.includes('at most'));
assert(T.parseList('1e400, 2').err !== '');

// chapter example: sun and shade leaves
const sun = [42, 45, 38, 44, 47, 41, 43, 46], shade = [52, 49, 55, 51, 48, 54, 50, 53, 56, 47];
let r = T.ttest(sun, shade);
near(r.A.mean, 43.25, 1e-9, 'mean sun'); near(r.B.mean, 51.5, 1e-9, 'mean shade');
near(r.A.ss, 59.5, 1e-9, 'ss sun'); near(r.B.ss, 82.5, 1e-9, 'ss shade');
near(r.A.s, 2.9155, 1e-3, 's sun'); near(r.B.s, 3.0277, 1e-3, 's shade');
near(r.t, 5.864, 2e-3, 't'); assert.strictEqual(r.df, 16); assert.strictEqual(r.crit, 2.12); assert.strictEqual(r.sig, true);
assert(T.conclusion(r).includes('reject the null hypothesis'));
// a close pair: no significant difference
r = T.ttest([34, 38, 31, 36, 40, 35, 33, 37], [36, 39, 33, 38, 41, 34, 35, 40, 37]);
near(r.t, 1.097, 2e-3, 't close'); assert.strictEqual(r.df, 15); assert.strictEqual(r.crit, 2.13); assert.strictEqual(r.sig, false);
assert(T.conclusion(r).includes('accept the null hypothesis'));
// identical samples: t = 0
r = T.ttest([5, 6, 7], [5, 6, 7]); assert.strictEqual(r.t, 0); assert.strictEqual(r.sig, false);
// no spread
r = T.ttest([5, 5, 5], [6, 6, 6]); assert.strictEqual(r.nospread, true); assert(T.conclusion(r).includes('no spread'));
r = T.ttest([5, 5, 5], [5, 5]); assert.strictEqual(r.t, 0); assert(T.conclusion(r).includes('t = 0'));
// df beyond the table
const big = Array.from({ length: 20 }, (_, i) => i), big2 = Array.from({ length: 20 }, (_, i) => i + 3);
r = T.ttest(big, big2); assert.strictEqual(r.df, 38); assert.strictEqual(r.crit, null); assert(T.conclusion(r).includes('table given'));
// the table agrees with FACTS.md
const facts = [12.71, 4.30, 3.18, 2.78, 2.57, 2.45, 2.36, 2.31, 2.26, 2.23, 2.20, 2.18, 2.16, 2.14, 2.13, 2.12, 2.11, 2.10, 2.09, 2.09, 2.08, 2.07, 2.07, 2.06, 2.06, 2.06, 2.05, 2.05, 2.05, 2.04];
facts.forEach((v, i) => assert.strictEqual(T.CRIT[i + 1], v));
// default samples give a significant result
r = T.ttest(T.parseList(T.DEF_A).vals, T.parseList(T.DEF_B).vals); assert.strictEqual(r.sig, true);
// formatting
assert.strictEqual(T.fmt(0), '0'); assert.strictEqual(T.fmt(Infinity), 'infinity'); assert.strictEqual(T.fmt(5.8642), '5.86');
console.log('ok bio-ttest');
