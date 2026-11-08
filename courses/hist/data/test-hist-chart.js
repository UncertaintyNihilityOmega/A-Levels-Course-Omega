// Logic test for widgets/hist-chart.js: node data/test-hist-chart.js
global.W = { register: function () {} };
const path = require('path');
const m = require(path.join(__dirname, '..', 'widgets', 'hist-chart.js'));
const assert = require('assert');

// parsing
let p = m.parseSeries('Coal: 1900=15.88, 1860=0.3, 1880=3.28');
assert.strictEqual(p.series.length, 1);
assert.deepStrictEqual(p.keys, ['1860', '1880', '1900'], 'years sorted');
assert.ok(p.numeric);
assert.strictEqual(p.series[0].vals['1880'], 3.28);

p = m.parseSeries('A: 1880-4=3.7, 1900-4=17.3 ;; B: 1880-4=1, 1900-4=2 ;; C: 1880-4=9');
assert.strictEqual(p.series.length, 2, 'at most two series');
assert.ok(p.problems.some(function (s) { return /left out/.test(s); }));
assert.ok(!p.numeric, 'period labels are categories');
assert.deepStrictEqual(p.keys, ['1880-4', '1900-4']);

p = m.parseSeries('Bad: 1890=abc, 1900=5, =3, 1910');
assert.strictEqual(p.series.length, 1);
assert.deepStrictEqual(p.keys, ['1900']);
assert.strictEqual(p.problems.length, 3);

p = m.parseSeries('');
assert.strictEqual(p.series.length, 0);
p = m.parseSeries('no colon here');
assert.strictEqual(p.series.length, 0);
assert.strictEqual(p.problems.length, 1);
p = m.parseSeries(undefined);
assert.strictEqual(p.series.length, 0);

// missing values in the second series
p = m.parseSeries('A: 1900=1, 1901=2 ;; B: 1900=5');
assert.deepStrictEqual(p.keys, ['1900', '1901']);
assert.strictEqual(p.series[1].vals['1901'], undefined);

// ticks
let t = m.niceTicks(0, 53.234, 4);
assert.strictEqual(t.lo, 0);
assert.ok(t.hi >= 53.234);
assert.ok(t.ticks.length >= 3 && t.ticks.length <= 8, JSON.stringify(t.ticks));
t = m.niceTicks(0, 2863, 4);
assert.ok(t.hi >= 2863 && t.ticks[1] > 0);
t = m.niceTicks(5, 5, 4);
assert.ok(t.hi > t.lo);
t = m.niceTicks(-3, 8, 4);
assert.ok(t.lo <= -3 && t.hi >= 8);
t = m.niceTicks(NaN, 1, 4);
assert.deepStrictEqual(t.ticks, [0, 1]);
t = m.niceTicks(0, 0.9, 4);
assert.ok(t.ticks.every(function (v) { return Math.abs(v * 10 - Math.round(v * 10)) < 1e-9 || Math.abs(v * 100 - Math.round(v * 100)) < 1e-9; }), JSON.stringify(t.ticks));

// formatting
assert.strictEqual(m.decimals([0.3, 3.28, 15.88]), 2);
assert.strictEqual(m.decimals([1, 2]), 0);
assert.strictEqual(m.fmtNum(15.88, 2), '15.88');
assert.strictEqual(m.fmtNum(2863173, 0), '2,863,173');
assert.strictEqual(m.fmtNum(null, 0), 'no figure');
p = m.parseSeries('Coal: 1860=0.3, 1900=15.88');
assert.ok(/rises from 0\.30 in 1860 to 15\.88 in 1900/.test(m.trendWords(p.series[0], p.keys, 2)), m.trendWords(p.series[0], p.keys, 2));
console.log('hist-chart logic ok');
