// data/test_fm_chisq.js: the numbers of widgets/fm-chisq.js against the MF19 chi-squared table and numerical integration.
// Run from the course folder: node data/test_fm_chisq.js
const path = require('path');
const core = require(path.join(process.cwd(), 'widgets', 'fm-chisq.js'));
let fails = 0, cases = 0;
const near = (a, b, tol, what) => { cases++; if (!(Math.abs(a - b) <= tol)) { fails++; console.log('FAIL', what, a, b); } };
const yes = (cond, what) => { cases++; if (!cond) { fails++; console.log('FAIL', what); } };
const r3 = (x) => Math.round(x * 1000) / 1000;

// MF19 rows (3 d.p.): P(X <= x) = p
const table = {
  1:  { 0.9: 2.706, 0.95: 3.841, 0.975: 5.024, 0.99: 6.635, 0.995: 7.879, 0.999: 10.828 },
  2:  { 0.9: 4.605, 0.95: 5.991, 0.975: 7.378, 0.99: 9.210, 0.995: 10.597, 0.999: 13.816 },
  3:  { 0.9: 6.251, 0.95: 7.815, 0.99: 11.345 },
  4:  { 0.9: 7.779, 0.95: 9.488, 0.975: 11.143, 0.99: 13.277, 0.995: 14.860, 0.999: 18.467 },
  5:  { 0.95: 11.070, 0.99: 15.086 },
  6:  { 0.95: 12.592, 0.99: 16.812 },
  8:  { 0.95: 15.507, 0.99: 20.090 },
  10: { 0.9: 15.987, 0.95: 18.307, 0.975: 20.483, 0.99: 23.209, 0.995: 25.188, 0.999: 29.588 },
  25: { 0.9: 34.382, 0.95: 37.652, 0.975: 40.646, 0.99: 44.314, 0.995: 46.928, 0.999: 52.620 },
};
for (const [v, row] of Object.entries(table)) {
  for (const [p, want] of Object.entries(row)) {
    near(r3(core.chiInv(Number(p), Number(v))), want, 1e-9, `chiInv nu=${v} p=${p}`);
  }
}
// alpha -> critical value
near(r3(core.critical(0.05, 4)), 9.488, 1e-9, 'critical 5% nu=4');
near(r3(core.critical(0.005, 10)), 25.188, 1e-9, 'critical 0.5% nu=10');

// the density integrates to the cdf (Simpson in u = sqrt(x) removes the singularity at 0)
function simpson(f, a, b, n) { const h = (b - a) / n; let s = f(a) + f(b); for (let i = 1; i < n; i++) s += (i % 2 ? 4 : 2) * f(a + i * h); return s * h / 3; }
for (const v of [1, 2, 3, 4, 7, 10, 20, 25, 30]) {
  for (const x of [0.5, 2, 5, 12.3, 40]) {
    const num = simpson((u) => (u === 0 ? (v === 1 ? 2 / Math.sqrt(2 * Math.PI) : 0) : core.chiPdf(u * u, v) * 2 * u), 0, Math.sqrt(x), 20000);
    near(core.chiCdf(x, v), num, 1e-7, `chiCdf nu=${v} x=${x}`);
    near(core.chiCdf(x, v) + core.upperTail(x, v), 1, 1e-12, `cdf + tail nu=${v} x=${x}`);
  }
}
near(core.chiCdf(0, 5), 0, 0, 'cdf at 0');
near(core.upperTail(0, 5), 1, 0, 'tail at 0');
near(core.chiCdf(2 * Math.log(2), 2), 0.5, 1e-12, 'nu=2 median');
near(core.chiCdf(3.841458820694124, 1), 0.95, 1e-9, 'nu=1 5% point');
yes(core.upperTail(150, 3) > 0 && core.upperTail(150, 3) < 1e-25, 'extreme tail is tiny but positive');

// the chapter's numbers
near(core.upperTail(4.5, 5), 0.4799, 5e-4, 'P(X > 4.5), nu = 5 (die)');
yes(core.decide(4.5, 11.070) === false, 'die: do not reject');
yes(core.decide(12, 11.070) === true, 'reject above the critical value');
yes(core.decide(null, 5) === null, 'decide null');
yes(core.decide(NaN, 5) === null, 'decide NaN');
near(core.upperTail(22.88, 6), 0.00082, 5e-5, 'P(X > 22.88), nu = 6');
near(core.upperTail(13.689, 3), 0.0034, 5e-4, 'ratio example P-value');
yes(core.inTable(25) && core.inTable(30) && !core.inTable(26) && !core.inTable(29) && core.inTable(1), 'MF19 rows');

// ranges
for (let v = 1; v <= 30; v++) {
  for (const a of [0.1, 0.05, 0.025, 0.01, 0.005]) {
    const c = core.critical(a, v);
    yes(isFinite(c) && c > v * 0.5, `critical finite nu=${v} a=${a}`);
    const xm = core.xMax(v, c, null);
    yes(xm > c && isFinite(xm), `xMax holds the critical value nu=${v} a=${a}`);
    const ym = core.yMax(v);
    yes(ym > 0 && isFinite(ym), `yMax nu=${v}`);
    if (v >= 3) yes(ym >= core.chiPdf(v - 2, v), `yMax above the mode nu=${v}`);
  }
  let prev = 0;
  for (const a of [0.1, 0.05, 0.025, 0.01, 0.005]) { const c = core.critical(a, v); yes(c > prev, `monotone nu=${v} a=${a}`); prev = c; }
}
yes(core.xMax(4, 9.488, 500) <= 2.5 * core.xMax(4, 9.488, null) + 1e-9, 'xMax with a huge statistic is capped');
near(core.xMax(4, 9.488, 14) >= 14 ? 1 : 0, 1, 0, 'xMax shows a statistic of 14');
console.log(fails ? `${fails} FAILED of ${cases}` : `ok: ${cases} cases`);
process.exit(fails ? 1 : 0);
