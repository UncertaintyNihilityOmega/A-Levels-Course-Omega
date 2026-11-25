// Node test for widgets/fm-impact.js: node data/test_fm_impact.js
const { wallImpact, spheresImpact, normDeg } = require('../widgets/fm-impact.js');
let fails = 0;
function eq(label, got, want, tol = 1e-9) {
  if (!(Math.abs(got - want) <= tol)) { fails++; console.log('FAIL', label, 'got', got, 'want', want); }
}
// wall, e = 1: speed and angle unchanged
let r = wallImpact(5, 40, 1, 1);
eq('wall e=1 speed', r.speed, 5);
eq('wall e=1 angle', r.beta, 40, 1e-9);
eq('wall e=1 KE lost', r.keLost, 0);
eq('wall e=1 impulse', r.impulse, 2 * 5 * Math.sin(40 * Math.PI / 180));
// wall, e = 0: slides along the wall
r = wallImpact(5, 40, 0, 1);
eq('wall e=0 speed', r.speed, 5 * Math.cos(40 * Math.PI / 180));
eq('wall e=0 angle', r.beta, 0);
// chapter example: u = 20, 30 degrees, e = 0.6, m 0.5
r = wallImpact(20, 30, 0.6, 0.5);
eq('wall speed', r.speed, Math.sqrt(336), 1e-9);
eq('wall beta', r.beta, Math.atan2(6, 20 * Math.cos(Math.PI / 6)) * 180 / Math.PI, 1e-9);
eq('wall beta 1dp', Math.round(r.beta * 10) / 10, 19.1);
eq('wall impulse', r.impulse, 8, 1e-9);
eq('wall KE lost', r.keLost, 16, 1e-9);
// tan beta = e tan alpha
r = wallImpact(7, 55, 0.35, 1);
eq('tan beta', Math.tan(r.beta * Math.PI / 180), 0.35 * Math.tan(55 * Math.PI / 180), 1e-9);
// two spheres, equal masses, e = 1, B at rest: the paths are at 90 degrees
for (const th of [10, 30, 55, 80, -40]) {
  r = spheresImpact(2, 2, 9, th, 0, 0, 1);
  const dot = r.v1[0] * r.v2[0] + r.v1[1] * r.v2[1];
  eq('90 degrees dot, th ' + th, dot, 0, 1e-9);
  eq('KE conserved th ' + th, r.keLost, 0, 1e-9);
  eq('momentum x th ' + th, 2 * r.v1[0] + 2 * r.v2[0], 2 * 9 * Math.cos(th * Math.PI / 180), 1e-9);
}
// e = 0: common velocity along the line
r = spheresImpact(2, 3, 10, 30, 0, 0, 0);
eq('e=0 common', r.v1[0], r.v2[0]);
eq('e=0 perp A unchanged', r.v1[1], 5, 1e-9);
// chapter example: 2 kg, 3 kg, u1 = 10 at 30, e = 0.5
r = spheresImpact(2, 3, 10, 30, 0, 0, 0.5);
eq('v1x', r.v1[0], 0.8660254037844386, 1e-9);
eq('v2x', r.v2[0], 5.196152422706632, 1e-9);
eq('A perp', r.v1[1], 5, 1e-9);
eq('A speed', r.s1, Math.hypot(0.8660254037844386, 5), 1e-9);
eq('A dir 1dp', Math.round(r.d1 * 10) / 10, 80.2);
// KE lost formula along the line of centres
const along = 10 * Math.cos(30 * Math.PI / 180);
eq('KE lost formula', r.keLost, 2 * 3 / (2 * 5) * (1 - 0.25) * along * along, 1e-9);
// the 3m, 2m example: tan alpha = 3/4
const al = Math.atan(3 / 4) * 180 / Math.PI;
r = spheresImpact(3, 2, 1, al, 0, 0, 0.5);
eq('3m 2m vA along', r.v1[0], 0.32, 1e-9);
eq('3m 2m vB', r.v2[0], 0.72, 1e-9);
eq('3m 2m perp', r.v1[1], 0.6, 1e-9);
eq('3m 2m KE lost', r.keLost, 0.288, 1e-9);
// not approaching
r = spheresImpact(1, 1, 3, 30, 5, 0, 0.5);
eq('no collision flag', r.collides ? 1 : 0, 0);
eq('no collision KE', r.keLost, 0);
// B moving towards A
r = spheresImpact(1, 1, 4, 0, 4, 180, 1);
eq('head on swap A', r.v1[0], -4, 1e-9);
eq('head on swap B', r.v2[0], 4, 1e-9);
eq('normDeg', normDeg(190), -170);
eq('normDeg2', normDeg(-180), 180);
// zero speeds
r = spheresImpact(1, 1, 0, 0, 0, 0, 0.5);
eq('zero', r.s1, 0);
console.log(fails ? fails + ' failures' : 'ok');
process.exit(fails ? 1 : 0);
