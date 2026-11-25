// data/test_fm_tdist.js: the numbers of widgets/fm-tdist.js against the MF19 t table and numerical integration.
// Run from the course folder: node data/test_fm_tdist.js
const path = require('path');
const core = require(path.join(process.cwd(), 'widgets', 'fm-tdist.js'));
let fails = 0, cases = 0;
const near = (a, b, tol, what) => { cases++; if (!(Math.abs(a - b) <= tol)) { fails++; console.log('FAIL', what, a, b); } };
const yes = (cond, what) => { cases++; if (!cond) { fails++; console.log('FAIL', what); } };

// MF19 rows (3 d.p.)
const table = {
  1:  { 0.9: 3.078, 0.95: 6.314, 0.975: 12.706, 0.99: 31.821, 0.995: 63.657 },
  5:  { 0.9: 1.476, 0.95: 2.015, 0.975: 2.571, 0.99: 3.365, 0.995: 4.032 },
  10: { 0.9: 1.372, 0.95: 1.812, 0.975: 2.228, 0.99: 2.764, 0.995: 3.169 },
  30: { 0.9: 1.310, 0.95: 1.697, 0.975: 2.042, 0.99: 2.457, 0.995: 2.750 },
  9:  { 0.95: 1.833, 0.975: 2.262, 0.99: 2.821, 0.995: 3.250 },
  15: { 0.95: 1.753, 0.99: 2.602, 0.975: 2.131, 0.995: 2.947 },
};
for (const [v, row] of Object.entries(table)) {
  for (const [p, want] of Object.entries(row)) {
    near(Math.round(core.tInv(Number(p), Number(v)) * 1000) / 1000, want, 1e-9, `tInv nu=${v} p=${p}`);
  }
}
// normal row (nu = infinity)
const inf = { 0.9: 1.282, 0.95: 1.645, 0.975: 1.960, 0.99: 2.326, 0.995: 2.576 };
for (const [p, want] of Object.entries(inf)) near(Math.round(core.tInv(Number(p), Infinity) * 1000) / 1000, want, 1e-9, `tInv inf p=${p}`);

// the density integrates to the cdf (Simpson) for several nu
function simpson(f, a, b, n) { const h = (b - a) / n; let s = f(a) + f(b); for (let i = 1; i < n; i++) s += (i % 2 ? 4 : 2) * f(a + i * h); return s * h / 3; }
for (const v of [1, 2, 3, 7, 20, 60]) {
  for (const x of [0.5, 1.3, 2.4, 4]) {
    near(core.tCdf(x, v), 0.5 + simpson((t) => core.tPdf(t, v), 0, x, 4000), 1e-8, `tCdf nu=${v} x=${x}`);
    near(core.tCdf(-x, v), 1 - core.tCdf(x, v), 1e-12, `symmetry nu=${v} x=${x}`);
  }
}
near(core.tCdf(0, 4), 0.5, 1e-15, 'cdf at 0');
near(core.normCdf(1.96), 0.9750021048517795, 1e-9, 'normCdf 1.96');
near(core.normCdf(-1), 0.15865525393145707, 1e-9, 'normCdf -1');
// the chapter's numbers
near(1 - core.tCdf(2, 4), 0.0581, 5e-5, 'P(T>2), nu=4');
yes(core.pValue(2.0, 2, 9) > 0.05, 'p-value of t = 2.0, nu = 9, two-tailed, is above 5%');
near(core.critical(0.05, 2, 9), 2.262, 5e-4, 'critical 5% two-tailed nu=9');
near(core.critical(0.05, 1, 9), 1.833, 5e-4, 'critical 5% one-tailed nu=9');
near(core.critical(0.01, 2, 2), 9.925, 5e-4, 'critical 1% two-tailed nu=2');
near(core.critical(0.05, 2, 2), 4.303, 5e-4, 'critical 5% two-tailed nu=2');
// decisions and ranges
yes(core.decide(2.0, 2, 2.262) === false, 'decide no');
yes(core.decide(-2.5, 2, 2.262) === true, 'decide two-tailed negative');
yes(core.decide(-2.5, 1, 2.262) === false, 'decide one-tailed negative');
yes(core.decide(null, 1, 2) === null, 'decide null');
near(core.halfWidth(2.262, null), 4.5, 1e-12, 'halfWidth default');
near(core.halfWidth(63.7, null), 16, 1e-12, 'halfWidth capped');
near(core.halfWidth(2, 30), 16, 1e-12, 'halfWidth t capped');
// every nu 1..60 and every alpha/tails gives a finite increasing critical value
for (let v = 1; v <= 60; v++) for (const t of [1, 2]) {
  let prev = 0;
  for (const a of [0.1, 0.05, 0.02, 0.01]) { const c = core.critical(a, t, v); yes(isFinite(c) && c > prev, `monotone nu=${v} tails=${t} alpha=${a}`); prev = c; }
}
console.log(fails ? `${fails} FAILED of ${cases}` : `ok: ${cases} cases`);
process.exit(fails ? 1 : 0);
