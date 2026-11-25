// data/test_fm_topple.js: the geometry of widgets/fm-topple.js against hand values and a brute-force check.
// Run: node data/test_fm_topple.js
const path = require('path');
const core = require(path.join(__dirname, '..', 'widgets', 'fm-topple.js'));
const DEG = 180 / Math.PI, RAD = Math.PI / 180;
let fails = 0, checks = 0;
const near = (a, b, tol, what) => { checks++; if (!(Math.abs(a - b) <= tol)) { fails++; console.log('FAIL', what, a, b); } };
const is = (a, b, what) => { checks++; if (a !== b) { fails++; console.log('FAIL', what, a, b); } };

// critical angles from the chapter: cone r = 6, h = 20, mu 0.8 and 1.5
let c = core.critical('cone', 6, 20, 0.8);
near(c.alphaT, Math.atan(6 / 5) * DEG, 1e-9, 'cone alphaT'); near(c.alphaT, 50.194, 1e-3, 'cone alphaT value');
near(c.alphaS, 38.660, 1e-3, 'slide 0.8'); is(c.first, 'slides', 'cone first, mu 0.8');
c = core.critical('cone', 6, 20, 1.5);
near(c.alphaS, 56.310, 1e-3, 'slide 1.5'); is(c.first, 'topples', 'cone first, mu 1.5');
// cylinder radius 5, height 30: tan = 5/15; cuboid width 6, height 10: tan = 3/5; cube
near(core.critical('cylinder', 5, 30, 0.5).alphaT, 18.435, 1e-3, 'cylinder');
near(core.critical('cuboid', 6, 10, 0.5).alphaT, Math.atan(0.6) * DEG, 1e-9, 'cuboid');
near(core.critical('cuboid', 8, 8, 0.5).alphaT, 45, 1e-9, 'cube topples at 45 degrees');
// geometry
const gc = core.geometry('cone', 6, 20); is(gc.hG, 5, 'cone G at a quarter'); is(gc.a, 6, 'cone half base'); is(gc.base, 12, 'cone base');
const gb = core.geometry('cuboid', 6, 10); is(gb.hG, 5, 'cuboid G'); is(gb.a, 3, 'cuboid half base'); is(gb.base, 6, 'cuboid base');
const gy = core.geometry('cylinder', 5, 30); is(gy.hG, 15, 'cylinder G'); is(gy.a, 5, 'cylinder half base');
// tie
is(core.critical('cuboid', 8, 8, 1).first, 'both', 'tie');
// the foot of the vertical through G is at the lower edge exactly at the toppling angle
['cuboid', 'cylinder', 'cone'].forEach((s) => {
  [[6, 10], [3, 25], [10, 8]].forEach(([w, h]) => {
    const cr = core.critical(s, w, h, 0.7);
    near(core.footU(s, w, h, cr.alphaT), 0, 1e-9, `foot at the edge at alphaT (${s} ${w} ${h})`);
    // brute force over angles: outside iff foot < 0 ; result matches the smaller critical angle
    for (let a = 0; a <= 60; a += 0.25) {
      const st = core.stateAt(s, w, h, 0.7, a);
      const footOutside = core.footU(s, w, h, a) < -1e-9;
      if (Math.abs(a - cr.alphaT) > 1e-6) is(st.outside, footOutside, `outside ${s} ${w} ${h} ${a}`);
      if (Math.abs(a - cr.alphaS) > 1e-6) is(st.slipping, Math.tan(a * RAD) > 0.7, `slipping ${s} ${w} ${h} ${a}`);
      const first = Math.min(cr.alphaT, cr.alphaS);
      if (Math.abs(a - first) > 1e-6) is(st.result === 'stable', a < first, `stable ${s} ${w} ${h} ${a}`);
      if (a > first + 1e-6) is(st.result, cr.first, `result ${s} ${w} ${h} ${a}`);
    }
  });
});
// the chapter's solid: cone with a hemisphere removed has G 61/14 above the base, radius 8: tan = 112/61
near(Math.atan(8 / (61 / 14)) * DEG, 61.425, 1e-3, 'chapter solid');
console.log(fails ? `${fails} FAILED of ${checks}` : `ok: ${checks} checks`);
process.exit(fails ? 1 : 0);
