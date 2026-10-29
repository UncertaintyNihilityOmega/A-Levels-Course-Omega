// data/test_bio-diversity.js: tests the maths of widgets/bio-diversity.js. Run: node data/test_bio-diversity.js
const assert = require('assert');
const path = require('path');
const m = require(path.join(__dirname, '..', 'widgets', 'bio-diversity.js'));
const near = (a, b, t) => assert(Math.abs(a - b) <= (t || 1e-9), a + ' vs ' + b);
let n = 0;
const ok = (c, msg) => { assert(c, msg); n++; };

// ---- parseCount / parseList
ok(m.parseCount('12').v === 12 && !m.parseCount('12').err, 'count 12');
ok(m.parseCount('').err && m.parseCount('-3').err && m.parseCount('2.5').err && m.parseCount('abc').err, 'bad counts rejected');
ok(m.parseCount('0').v === 0, 'zero ok');
ok(m.parseCount('99999999').err, 'huge rejected');
const pl = m.parseList('1, 2.5  3;4', false);
ok(pl.vals.length === 4 && pl.vals[1] === 2.5, 'list');
ok(m.parseList('1, x', false).err, 'list bad token');
ok(m.parseList('1, 2.5', true).err, 'integer list rejects decimals');
ok(m.parseList('', false).vals.length === 0, 'empty list');

// ---- Simpson (the river data in the chapter, and a few extremes)
let s = m.simpsonOf([24, 18, 21, 20, 17]);
near(s.N, 100); near(s.sumsq, 0.2030); near(s.D, 0.797); ok(s.richness === 5, 'richness'); n += 3;
s = m.simpsonOf([62, 28, 6, 2, 2]);
near(s.D, 0.5328); n++;
s = m.simpsonOf([10, 0, 0]);
near(s.D, 0); ok(s.richness === 1, 'one species'); n++;
s = m.simpsonOf([0, 0, 0]);
ok(s.D === null && s.N === 0, 'N = 0 gives no D');
s = m.simpsonOf([50, 50]); near(s.D, 0.5);
s = m.simpsonOf([97, 1, 1, 1]); near(s.D, 1 - 0.9412, 1e-4);
s = m.simpsonOf([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]); near(s.D, 0.9); n += 3;
// evenness: same richness, different D
const even = m.simpsonOf([20, 20, 20, 20, 20]), uneven = m.simpsonOf([96, 1, 1, 1, 1]);
ok(even.richness === uneven.richness && even.D > uneven.D, 'evenness raises D');
near(even.D, 0.8);
// the sentence
const t1 = m.simpsonText(even, uneven, 'A', 'B');
ok(/A has the higher D/.test(t1) && /same|Both sites have 5 species/.test(t1) && /evenness/.test(t1), 'text equal richness: ' + t1);
const fewer = m.simpsonText(m.simpsonOf([50, 50]), m.simpsonOf([97, 1, 1, 1]), 'B', 'A');
ok(/fewer species/.test(fewer), 'text fewer species higher D: ' + fewer);
ok(/same diversity/.test(m.simpsonText(even, even, 'A', 'B')), 'equal D');
ok(/compare the sites with care/.test(m.simpsonText(m.simpsonOf([100, 100]), m.simpsonOf([5, 3]), 'A', 'B')), 'size note');
ok(/Enter at least one/.test(m.simpsonText(m.simpsonOf([0]), even, 'A', 'B')), 'no individuals text');

// ---- Lincoln
let L = m.lincoln(48, 60, 12);
ok(L.N === 240 && !L.err, 'shrimps 240'); near(L.raw, 240); near(L.share, 0.2); n += 1;
L = m.lincoln(37, 45, 9); ok(L.N === 185, 'default 185');
L = m.lincoln(55, 40, 8); ok(L.N === 275, 'woodlice 275');
L = m.lincoln(10, 10, 3); ok(L.N === 33 && Math.abs(L.raw - 33.333333) < 1e-5, 'rounding to a whole number');
ok(m.lincoln(10, 10, 0).err && /zero/.test(m.lincoln(10, 10, 0).err), 'm2 = 0');
ok(m.lincoln(10, 5, 6).err && /n₂/.test(m.lincoln(10, 5, 6).err), 'm2 > n2');
ok(m.lincoln(5, 10, 6).err && /n₁/.test(m.lincoln(5, 10, 6).err), 'm2 > n1');
ok(m.lincoln(0, 10, 1).err && m.lincoln(10, 0, 1).err, 'zero samples');
ok(m.lincoln(1.5, 10, 1).err && m.lincoln(NaN, 10, 1).err && m.lincoln(-3, 10, 1).err, 'non-integers and negatives');
L = m.lincoln(20, 20, 20); ok(L.N === 20, 'everything recaptured');
ok(m.lincoln(1000000, 1000000, 1).N === 1e12, 'large numbers do not break');

// ---- ranks and Spearman
const eqArr = (a, b) => a.length === b.length && a.every((v, i) => Math.abs(v - b[i]) < 1e-12);
ok(eqArr(m.rankList([3, 5, 5, 8]), [1, 2.5, 2.5, 4]), 'ranks with a tie');
ok(eqArr(m.rankList([4, 6, 6, 9, 11, 13, 15, 15]), [1, 2.5, 2.5, 4, 5, 6, 7.5, 7.5]), 'ranks, two ties');
ok(eqArr(m.rankList([7, 7, 7]), [2, 2, 2]), 'all tied');
ok(eqArr(m.rankList([5, 1, 3]), [3, 1, 2]), 'unsorted input');
let sp = m.spearman([4, 6, 6, 9, 11, 13, 15, 15], [2, 5, 3, 8, 7, 12, 14, 10]);
near(sp.sumD2, 6.0); near(sp.rs, 1 - 36 / 504); ok(sp.denom === 504 && sp.ties, 'rushes example'); n += 2;
sp = m.spearman([12, 18, 25, 25, 31, 40, 47], [34, 29, 30, 22, 25, 14, 9]);
near(sp.sumD2, 104.5); near(sp.rs, -0.8660714285714286); n++;
sp = m.spearman([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]); near(sp.rs, 1);
sp = m.spearman([1, 2, 3, 4, 5], [50, 40, 30, 20, 10]); near(sp.rs, -1); n++;
sp = m.spearman(m.parseList('4.1 4.5 4.9 5.2 5.2 5.8 6.3 6.6 7.0 7.4').vals, m.parseList('6 5 9 8 12 10 15 18 16 20').vals);
ok(sp.rs > 0.648, 'widget default is significant'); console.log('default example rs =', m.f3(sp.rs));
ok(m.spearman([1, 1, 1], [1, 2, 3]).err && m.spearman([1, 2, 3], [4, 4, 4]).err, 'no spread');
ok(m.spearman([1, 2], [1, 2]).err, 'too few pairs');
ok(m.spearman([1, 2, 3], [1, 2]).err, 'unequal lengths');
// sum of D is always 0
sp = m.spearman([3, 1, 4, 1, 5, 9, 2, 6], [2, 7, 1, 8, 2, 8, 1, 8]);
near(sp.D.reduce((a, b) => a + b, 0), 0, 1e-12); n++;
ok(sp.rs >= -1 && sp.rs <= 1, 'rs in range');
// text
let tx = m.spearmanText(m.spearman([1, 2, 3, 4, 5, 6, 7], [2, 1, 4, 3, 6, 5, 7]), 0.786);
ok(/significant positive correlation/.test(tx), tx);
tx = m.spearmanText(m.spearman([1, 2, 3, 4, 5, 6, 7], [3, 1, 6, 2, 7, 4, 5]), 0.786);
ok(/not significant/.test(tx), tx);
tx = m.spearmanText(m.spearman([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]), 0.786);
ok(/significant negative correlation/.test(tx), tx);
ok(/Enter the critical value/.test(m.spearmanText(sp, null)), 'no critical value text');
// formatting
ok(m.f3(-0.0001) === '0.000' && m.f3(0.8) === '0.800' && m.f3(-0.866) === '−0.866' && m.f3(null) === '–', 'f3');
console.log('bio-diversity: all', n, 'checks passed');
