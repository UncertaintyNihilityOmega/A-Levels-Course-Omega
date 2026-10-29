// data/test_bio-actionpot.js: run `node data/test_bio-actionpot.js` in the course folder; checks the maths of widgets/bio-actionpot.js
// against the values in chapters/bio.nerves.md (the table of the recorded trace, 500 per second at a 2 ms refractory period).
const assert = require('assert');
const path = require('path');
const m = require(path.join(process.cwd(), 'widgets', 'bio-actionpot.js'));
const near = (a, b, t = 1e-6) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
const table = { 0: -70, 0.5: -70, 0.75: -50, 1.0: 35, 1.5: -20, 2.0: -75, 3.0: -80, 4.0: -72, 5.0: -70 };
for (const t in table) near(m.apV(+t), table[t]);
let max = -1e9, min = 1e9;
for (let t = 0; t <= 5; t += 0.01) { const v = m.apV(t); max = Math.max(max, v); min = Math.min(min, v); assert(isFinite(v)); }
assert(max <= 35.0001 && max > 34.9, 'peak ' + max); assert(min >= -80.0001 && min < -79.9, 'min ' + min);
// supra threshold: identical trace for any stimulus >= 20 mV (all-or-nothing)
for (let t = 0; t <= 5; t += 0.05) near(m.singleV(t, 20), m.singleV(t, 30));
// sub threshold: never reaches -50, decays to rest
for (let d = 0; d < 20; d++) { let hi = -1e9; for (let t = 0; t <= 5; t += 0.01) hi = Math.max(hi, m.singleV(t, d)); assert(hi <= -50 && hi >= -70 - 1e-9, 'sub ' + d + ' ' + hi); near(m.singleV(5, d), -70, 0.01); }
assert(m.singleV(0.5, 25) === -70);
// train: frequency capped at 500 per second = 1 / 2 ms; none below strength 10
near(m.freq(0), 0); near(m.freq(9), 0); assert(m.freq(10) > 0); near(m.freq(100), 500); near(m.freq(71), 500);
for (let s = 10; s <= 100; s++) assert(m.freq(s) <= 500 && m.freq(s) >= m.freq(s - 1));
near(1000 / m.freq(100), m.REFRACTORY);
// spikes: separated by at least the refractory period, inside the window
for (const f of [16, 100, 250, 500]) { const ts = m.spikeTimes(f, 50); for (let i = 1; i < ts.length; i++) assert(ts[i] - ts[i - 1] >= 2 - 1e-9); assert(ts.length >= 1 && ts[ts.length - 1] < 50); }
assert.strictEqual(m.spikeTimes(0, 50).length, 0); assert.strictEqual(m.spikeTimes(NaN, 50).length, 0);
near(m.spikeV(0), -70); near(m.spikeV(0.5), 35); near(m.spikeV(2), -70);
// bad numbers
assert.strictEqual(m.numOr('abc', 5, 0, 10), 5); assert.strictEqual(m.numOr('99', 5, 0, 10), 10);
assert(isFinite(m.apV(NaN)) && isFinite(m.singleV(Infinity, 5)));
console.log('ok');
