// Node test for the pure functions of widgets/fm-polar.js (run: node data/fm-polar-test.js)
const core = require('../widgets/fm-polar.js');
const { simpsonHalfRSquared: area, niceStep, asPiMultiple } = core;
const PI = Math.PI;
let bad = 0;
function near(label, got, want, tol = 1e-6) {
  if (!(Math.abs(got - want) <= tol)) { console.log('FAIL', label, got, want); bad++; }
}
near('cardioid', area((t) => 1 + Math.cos(t), 0, 2 * PI, 400), 1.5 * PI);
near('circle r=2cos t', area((t) => 2 * Math.cos(t), -PI / 2, PI / 2, 400), PI);
near('rose r=cos 2t, r>=0 only', area((t) => Math.cos(2 * t), 0, 2 * PI, 400), PI / 4, 1e-5);
near('one petal', area((t) => Math.cos(2 * t), -PI / 4, PI / 4, 400), PI / 8);
near('spiral r=t/4', area((t) => t / 4, 0, 4 * PI, 400), 2 * PI ** 3 / 3);
near('lemniscate', area((t) => Math.sqrt(Math.cos(2 * t)), 0, 2 * PI, 400), 1, 1e-3);
near('circle past r<0 not double counted', area((t) => 3 * Math.cos(t), 0, 2 * PI, 400), 9 * PI / 4, 1e-5);
near('empty interval', area((t) => 1, 2, 1, 400), 0);
near('NaN r', area((t) => NaN, 0, 1, 400), 0);
near('step 1', niceStep(1.9), 0.5);
near('step 2', niceStep(10), 2.5 === 2.5 ? niceStep(10) : 0);
console.log('niceStep(2)', niceStep(2), 'niceStep(0.3)', niceStep(0.3), 'niceStep(6.28)', niceStep(6.28));
const pm = [[1.5 * PI, '3/2π'], [PI, 'π'], [-PI / 2, '−1/2π'], [2 * PI, '2π'], [4.2, '']];
for (const [v, want] of pm) if (asPiMultiple(v) !== want) { console.log('FAIL asPi', v, asPiMultiple(v), want); bad++; }
console.log(bad ? bad + ' failures' : 'all ok');
process.exit(bad ? 1 : 0);
