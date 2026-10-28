// data/test_bio-cardiac.js: run `node data/test_bio-cardiac.js` in the course folder; checks widgets/bio-cardiac.js against
// data/cardiac_samples.json (written by data/fig_cardiac.py) and the numbers in chapters/bio.heart.md.
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const C = require(path.join(process.cwd(), 'widgets', 'bio-cardiac.js'));
const ref = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'data', 'cardiac_samples.json'), 'utf8'));
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
ref.samples.forEach(s => { near(C.LA(s.t), s.la); near(C.LV(s.t), s.lv); near(C.AO(s.t), s.ao); });
// 75 bpm: same valve events as the Python model, identity time map
const ev = C.events(75);
assert.strictEqual(ev.length, 4);
ev.forEach((e, i) => { near(e.t, ref.events[i][0], 1e-9); assert.strictEqual(e.name, ref.events[i][1]); });
const P = C.phases(75); near(P.T, 0.8); near(P.S, 0.4); near(P.a, 0.1); near(P.v, 0.3); near(P.d, 0.4);
[0, 0.05, 0.3, 0.6, 0.8].forEach(t => near(C.tau(t, 75), t));
// chapter statements
const order = ['AV valve closes', 'semilunar valve opens', 'semilunar valve closes', 'AV valve opens'];
for (let b = 50; b <= 150; b++) {
  const e = C.events(b); assert.deepStrictEqual(e.map(x => x.name), order, 'events at ' + b);
  const p = C.phases(b); near(p.a + p.v + p.d, 60 / b, 1e-12);
  assert(p.d > 0 && p.v > p.a);
  for (let i = 1; i < 4; i++) assert(e[i].t > e[i - 1].t);
  // heart rate rescales time and diastole shortens most
  if (b > 75) assert((C.phases(b - 1).d - p.d) > (C.phases(b - 1).S - p.S) - 1e-9);
}
near(C.phases(60).S, 0.4); near(C.phases(60).d, 0.6); near(C.phases(150).S, 0.3, 1e-12); near(C.phases(150).d, 0.1, 1e-12); near(C.phases(150).T, 0.4);
// states at the cycle ends are the same (a cycle repeats)
const s0 = C.state(0, 100), s1 = C.state(C.phases(100).T, 100); near(s0.lv, s1.lv); near(s0.ao, s1.ao); near(s0.la, s1.la);
assert.strictEqual(C.state(0, 75).phase, 'atrial systole'); assert.strictEqual(C.state(0.2, 75).phase, 'ventricular systole'); assert.strictEqual(C.state(0.5, 75).phase, 'diastole');
// valves
let s = C.state(0.05, 75); assert(s.avOpen && !s.slOpen);
s = C.state(0.12, 75); assert(!s.avOpen && !s.slOpen);
s = C.state(0.25, 75); assert(!s.avOpen && s.slOpen);
s = C.state(0.39, 75); assert(!s.avOpen && !s.slOpen);
s = C.state(0.6, 75); assert(s.avOpen && !s.slOpen);
assert(/left ventricle is higher than in the left atrium, so the AV valve is closed/.test(C.reasons(C.state(0.12, 75)).av));
// peaks
let mx = 0, mxa = 0; for (let k = 0; k <= 800; k++) { mx = Math.max(mx, C.LV(k / 1000)); mxa = Math.max(mxa, C.LA(k / 1000)); }
near(mx, 16.2, 0.05); assert(mxa < 1.6);
// bad input
[NaN, -1, 99, undefined].forEach(t => { const x = C.state(t, 75); assert(isFinite(x.lv) && isFinite(x.t)); });
assert.strictEqual(C.num('abc', 75, 50, 150), 75); assert.strictEqual(C.num('999', 75, 50, 150), 150); assert.strictEqual(C.num('10', 75, 50, 150), 50);
console.log('bio-cardiac maths ok');
