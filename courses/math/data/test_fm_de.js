// data/test_fm_de.js: the exact solutions of widgets/fm-de.js against a fine RK4 integration of a y'' + b y' + c y = 0.
// Run: node data/test_fm_de.js
const path = require('path');
const core = require(path.join(__dirname, '..', 'widgets', 'fm-de.js'));
let fails = 0, cases = 0;
const near = (a, b, tol, what) => { cases++; if (!(Math.abs(a - b) <= tol * Math.max(1, Math.abs(b)))) { fails++; console.log('FAIL', what, a, b); } };

function rk4(a, b, c, y0, v0, x1, n) {
  // y'' = -(b y' + c y)/a as a first order system (y, v)
  const f = (y, v) => [v, -(b * v + c * y) / a];
  let y = y0, v = v0;
  const h = x1 / n;
  for (let i = 0; i < n; i++) {
    const k1 = f(y, v);
    const k2 = f(y + h * k1[0] / 2, v + h * k1[1] / 2);
    const k3 = f(y + h * k2[0] / 2, v + h * k2[1] / 2);
    const k4 = f(y + h * k3[0], v + h * k3[1]);
    y += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6;
    v += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6;
  }
  return y;
}

const kinds = {};
const as = [0.5, 1, 2], bs = [-4, -1, 0, 0.5, 2, 4, 6, 10], cs = [-6, -1, 0, 1, 2.5, 4, 5, 9, 30];
const ics = [[1, 0], [0, 1], [2, -3], [-5, 7], [0, 0]];
as.forEach((a) => bs.forEach((b) => cs.forEach((c) => ics.forEach(([y0, v0]) => {
  const s = core.solve(a, b, c, y0, v0);
  kinds[s.kind] = (kinds[s.kind] || 0) + 1;
  near(s.f(0), y0, 1e-9, `y(0) a=${a} b=${b} c=${c}`);
  const h = 1e-6;
  near((s.f(h) - s.f(-h)) / (2 * h), v0, 1e-5, `y'(0) a=${a} b=${b} c=${c}`);
  [0.5, 2, 5, 9].forEach((x) => {
    const ref = rk4(a, b, c, y0, v0, x, 4000);
    if (Math.abs(ref) < 1e8) near(s.f(x), ref, 1e-5, `y(${x}) a=${a} b=${b} c=${c} y0=${y0} v0=${v0} kind=${s.kind}`);
  });
}))));
console.log('kinds covered:', JSON.stringify(kinds));
['real', 'repeated', 'complex'].forEach((k) => { if (!kinds[k]) { fails++; console.log('FAIL no case of', k); } });

// the exact repeated and near-repeated cases
const rep = core.solve(1, 4, 4, 2, 0);
near(rep.m, -2, 1e-12, 'repeated root'); near(rep.A, 2, 1e-12, 'A'); near(rep.B, 4, 1e-12, 'B');
const rep2 = core.solve(4, 12, 9, 2, 0);
near(rep2.m, -1.5, 1e-12, 'repeated root 2'); near(rep2.B, 3, 1e-12, 'B2');
// floating point: 0.1 steps that should be repeated (b = 2.2, c = 1.21)
near(core.solve(1, 2.2, 1.21, 1, 0).kind === 'repeated' ? 1 : 0, 1, 0, 'b=2.2 c=1.21 repeated');
// the chapter's example: roots -1 +- 2i, y = e^-x (cos 2x + 0.5 sin 2x)
const ex = core.solve(1, 2, 5, 1, 0);
near(ex.p, -1, 1e-12, 'p'); near(ex.q, 2, 1e-12, 'q'); near(ex.A, 1, 1e-12, 'A'); near(ex.B, 0.5, 1e-12, 'B');

// growth flags and view ranges
const flags = [
  [1, -1, 5, 1, 0, true], [1, 2, 5, 1, 0, false], [1, 0, 4, 1, 0, false], [1, -2, 1, 1, 0, true], [1, 0, 0, 1, 1, true],
  [1, 0, 0, 1, 0, false], [1, -1, -6, 1, 1, true], [1, 5, 6, 1, 0, false], [1, -3, 2, 1, -1, true], [1, 3, 2, 1, -1, false],
];
flags.forEach(([a, b, c, y0, v0, want]) => {
  const s = core.solve(a, b, c, y0, v0);
  cases++;
  if (core.grows(s) !== want) { fails++; console.log('FAIL grows', a, b, c, y0, v0, core.grows(s), want); }
});
const v1 = core.viewRange(core.solve(1, -4, 2, 1, 0), 1);
if (!(v1.capped && v1.y1 < 1000)) { fails++; console.log('FAIL view cap', v1); }
const v2 = core.viewRange(core.solve(1, 2, 5, 1, 0), 1);
if (v2.capped || !(v2.y0 < 0 && v2.y1 > 1)) { fails++; console.log('FAIL view decay', v2); }
const v3 = core.viewRange(core.solve(1, 0, 0, 0, 0), 0);
if (!(isFinite(v3.y0) && isFinite(v3.y1) && v3.y1 > v3.y0)) { fails++; console.log('FAIL view zero', v3); }
// extreme sliders must stay finite
const ext = core.solve(0.1, -4, 30, 100, 100);
const vv = core.viewRange(ext, 100);
if (!(isFinite(vv.y0) && isFinite(vv.y1))) { fails++; console.log('FAIL extreme view', vv); }
const ext2 = core.solve(0.1, -4, -6, 100, 100);
const vv2 = core.viewRange(ext2, 100);
if (!(isFinite(vv2.y0) && isFinite(vv2.y1))) { fails++; console.log('FAIL extreme view 2', vv2, ext2.f(10)); }
console.log(fails ? `${fails} FAILED of ${cases}` : `all ${cases} checks passed`);
process.exit(fails ? 1 : 0);
