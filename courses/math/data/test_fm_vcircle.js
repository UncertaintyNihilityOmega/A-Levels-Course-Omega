// data/test_fm_vcircle.js: the formulas of widgets/fm-vcircle.js against RK4 integration and hand-checked cases.
// Run: node data/test_fm_vcircle.js
const path = require('path');
const core = require(path.join(__dirname, '..', 'widgets', 'fm-vcircle.js'));
let fails = 0, cases = 0;
const near = (a, b, tol, what) => { cases++; if (!(Math.abs(a - b) <= tol * Math.max(1, Math.abs(b)))) { fails++; console.log('FAIL', what, a, b); } };
const G = 10;

// string: leaving angle from analysis against integration
for (const r of [0.5, 1, 1.2, 3]) {
  for (let k = 2.05; k < 5; k += 0.25) {
    const u = Math.sqrt(k * G * r);
    const a = core.analyse('string', u, r);
    if (a.kind !== 'slack') { fails++; console.log('FAIL kind', r, k, a.kind); continue; }
    const ev = core.simulate('string', u, r, 20, 1e-4);
    near(ev.th, a.thetaEnd, 2e-3, `string theta r=${r} k=${k}`);
    near(ev.v, a.vL, 3e-3, `string v r=${r} k=${k}`);
  }
}
// outside
for (const r of [0.5, 2, 5]) {
  for (let k = 0.02; k < 1; k += 0.12) {
    const u = Math.sqrt(k * G * r);
    const a = core.analyse('outside', u, r);
    const ev = core.simulate('outside', u, r, 20, 1e-4);
    near(ev.th, a.thetaEnd, 2e-3, `outside theta r=${r} k=${k}`);
    near(ev.v, a.vL, 3e-3, `outside v r=${r} k=${k}`);
  }
}
// kinds
const A = (m, u, r) => core.analyse(m, u, r).kind;
if (A('string', Math.sqrt(50), 1) !== 'complete') { fails++; console.log('FAIL string 5gr'); }
if (A('string', Math.sqrt(49), 1) !== 'slack') { fails++; console.log('FAIL string 4.9gr'); }
if (A('string', Math.sqrt(20), 1) !== 'swing') { fails++; console.log('FAIL string 2gr'); }
if (A('rod', Math.sqrt(40), 1) !== 'just') { fails++; console.log('FAIL rod 4gr'); }
if (A('rod', Math.sqrt(41), 1) !== 'complete') { fails++; console.log('FAIL rod 4.1gr'); }
if (A('rod', Math.sqrt(39), 1) !== 'swing') { fails++; console.log('FAIL rod 3.9gr'); }
if (A('outside', Math.sqrt(10), 1) !== 'off') { fails++; console.log('FAIL outside gr'); }
// chapter values
near(core.analyse('string', 7, 1.2).thetaEnd * 180 / Math.PI, 133.97, 1e-3, 'ch slack angle');
near(core.analyse('string', 7, 1.2).vL, Math.sqrt(8.3333333), 1e-6, 'ch slack v');
near(core.analyse('outside', 1e-9, 2).thetaEnd * 180 / Math.PI, 48.19, 1e-3, 'outside from rest');
near(core.analyse('outside', 1e-9, 2).vL, Math.sqrt(40 / 3), 1e-6, 'outside leaving speed');
near(core.forceAt('string', 7, 0.8, 0.5, Math.PI / 3), 28.125, 1e-9, 'T at 60');
near(core.forceAt('string', 7, 0.8, 0.5, Math.PI), 5.625, 1e-9, 'T at top');
near(core.forceAt('string', 7, 0.8, 0.5, 0), 35.625, 1e-9, 'T at bottom');
near(core.forceAt('rod', 5, 0.6, 0.2, Math.PI), -1.6667, 1e-3, 'rod thrust at top');
// the tension is positive at every point before the leaving angle
{
  const u = Math.sqrt(3.5 * G * 1), a = core.analyse('string', u, 1);
  for (let t = 0; t < a.thetaEnd - 1e-6; t += 0.01) near(core.forceAt('string', u, 1, 1, t) > 0 ? 1 : 0, 1, 0, 'T positive before leaving');
  near(core.forceAt('string', u, 1, 1, a.thetaEnd), 0, 1e-9, 'T zero at leaving');
}
// leave state: position and velocity
{
  const ls = core.leaveState('string', 7, 1.2);
  near(Math.hypot(ls.x, ls.y), 1.2, 1e-9, 'leave on circle');
  near(ls.vx * ls.x + ls.vy * ls.y, 0, 1e-9, 'leave velocity tangent');
  near(Math.hypot(ls.vx, ls.vy), Math.sqrt(8.3333333), 1e-6, 'leave speed');
}
// through-the-centre case: tan^2 alpha = 1/2, u^2 = (2 + sqrt 3) g r
{
  const r = 1, s3 = Math.sqrt(3), u = Math.sqrt((2 + s3) * G * r);
  const ls = core.leaveState('string', u, r);
  const t = -ls.x / ls.vx;
  near(ls.y + ls.vy * t - 0.5 * G * t * t, 0, 1e-9, 'passes through the centre');
}
console.log(fails ? `${fails} FAILED of ${cases}` : `all ${cases} cases pass`);
process.exit(fails ? 1 : 0);
