// data/test_fm_pgf.js: the numbers of widgets/fm-pgf.js against the pmf, the standard mean and variance, and the product rule.
// Run from the course folder: node data/test_fm_pgf.js
const path = require('path');
const core = require(path.join(process.cwd(), 'widgets', 'fm-pgf.js'));
let fails = 0, cases = 0;
const near = (a, b, tol, what) => { cases++; if (!(Math.abs(a - b) <= tol)) { fails++; console.log('FAIL', what, a, b); } };
const yes = (cond, what) => { cases++; if (!cond) { fails++; console.log('FAIL', what); } };

const samples = [
  ['binomial', { n: 6, p: 0.3 }], ['binomial', { n: 30, p: 0.95 }], ['binomial', { n: 1, p: 0.05 }], ['binomial', { n: 12, p: 0.5 }],
  ['geometric', { p: 0.25 }], ['geometric', { p: 0.1 }], ['geometric', { p: 0.9 }],
  ['poisson', { lambda: 2 }], ['poisson', { lambda: 0.5 }], ['poisson', { lambda: 8 }],
  ['uniform', { n: 6 }], ['uniform', { n: 2 }], ['uniform', { n: 20 }],
];
for (const [d, pr] of samples) {
  const tag = d + JSON.stringify(pr);
  const a = core.pmf(d, pr, 400);
  const tot = a.reduce((s, v) => s + v, 0);
  near(tot, 1, 2e-3, 'pmf sums to 1 ' + tag);
  near(core.pgf(d, pr, 1), 1, 1e-12, 'G(1) = 1 ' + tag);
  near(core.pgf(d, pr, 0), a[0], 1e-12, 'G(0) = P(X = 0) ' + tag);
  // G(t) equals the power series of the pmf
  const t = d === 'geometric' ? 0.5 : 0.8;
  const series = a.reduce((s, v, x) => s + v * Math.pow(t, x), 0);
  near(core.pgf(d, pr, t), series, 2e-3, 'G(t) = sum p_x t^x ' + tag);
  // G' and G'' by finite differences at t = 1 (use t < 1 side for geometric domain safety: the domain includes 1)
  const h = 1e-4;
  const f = (x) => core.pgf(d, pr, x);
  const num1 = (f(1 + h) - f(1 - h)) / (2 * h);
  const num2 = (f(1 + h) - 2 * f(1) + f(1 - h)) / (h * h);
  const [g1, g2] = core.dG(d, pr);
  near(g1, num1, 1e-3 * Math.max(1, Math.abs(g1)), "G'(1) " + tag);
  near(g2, num2, 2e-2 * Math.max(1, Math.abs(g2)), "G''(1) " + tag);
  // MF19 formulas against the standard formulas and the pmf
  const [mG, vG] = core.meanVarFromG(g1, g2);
  const [mF, vF] = core.meanVarFormula(d, pr);
  near(mG, mF, 1e-9, 'E from G vs formula ' + tag);
  near(vG, vF, 1e-9 * Math.max(1, vF), 'Var from G vs formula ' + tag);
  const [mP, vP] = core.meanVarFromPmf(core.pmf(d, pr, 400));
  near(mP, mF, 0.1, 'E from pmf (the bars stop when the tail is below 0.001) ' + tag);
  near(vP, vF, 6e-2 * Math.max(1, vF), 'Var from pmf ' + tag);
}
// sums of two independent copies
const pairs = [
  ['binomial', { n: 6, p: 0.3 }, { n: 4, p: 0.3 }], ['binomial', { n: 6, p: 0.3 }, { n: 4, p: 0.6 }],
  ['poisson', { lambda: 2 }, { lambda: 1 }], ['uniform', { n: 6 }, { n: 4 }], ['geometric', { p: 0.4 }, { p: 0.55 }],
];
for (const [d, p1, p2] of pairs) {
  const tag = d + JSON.stringify(p1) + JSON.stringify(p2);
  const a = core.convolve(core.pmf(d, p1, 400), core.pmf(d, p2, 400));
  const dd = core.sumD(core.dG(d, p1), core.dG(d, p2));
  const [m, v] = core.meanVarFromG(dd[0], dd[1]);
  const [m1, v1] = core.meanVarFormula(d, p1), [m2, v2] = core.meanVarFormula(d, p2);
  near(m, m1 + m2, 1e-9, 'sum mean ' + tag);
  near(v, v1 + v2, 1e-9 * Math.max(1, v), 'sum variance ' + tag);
  const [mp, vp] = core.meanVarFromPmf(a);
  near(mp, m, 3e-2, 'sum mean from convolution ' + tag);
  near(vp, v, 8e-2 * Math.max(1, v), 'sum variance from convolution ' + tag);
}
// same-p binomials add: the convolution equals B(n1 + n2, p)
const c = core.convolve(core.pmf('binomial', { n: 6, p: 0.3 }), core.pmf('binomial', { n: 4, p: 0.3 }));
const b10 = core.pmf('binomial', { n: 10, p: 0.3 });
c.forEach((v, i) => near(v, b10[i], 1e-12, 'B(6,.3) + B(4,.3) = B(10,.3) at ' + i));
// Poisson sums
const cp = core.convolve(core.pmf('poisson', { lambda: 2 }, 80), core.pmf('poisson', { lambda: 1.5 }, 80));
const p35 = core.pmf('poisson', { lambda: 3.5 }, 80);
for (let i = 0; i < 8; i++) near(cp[i], p35[i], 1e-7, 'Po(2) + Po(1.5) = Po(3.5) at ' + i);
// chapter numbers
near(core.pmf('binomial', { n: 6, p: 0.3 })[2], 0.324135, 1e-6, 'B(6, 0.3) P(2)');
near(core.dG('geometric', { p: 0.4 })[0], 2.5, 1e-12, 'Geo(0.4) mean');
near(core.meanVarFromG(...core.dG('geometric', { p: 0.4 }))[1], 3.75, 1e-12, 'Geo(0.4) variance');
near(core.meanVarFromG(...core.dG('poisson', { lambda: 3 }))[1], 3, 1e-12, 'Po(3) variance');
// geometric domain
yes(isNaN(core.pgf('geometric', { p: 0.1 }, 1.2)), 'geometric G undefined beyond 1/q');
yes(core.upperT('geometric', { p: 0.1 }) < 1.2 && core.upperT('geometric', { p: 0.1 }) > 1, 'geometric upper t');
yes(core.upperT('binomial', { n: 6, p: 0.3 }) === 1.2, 'upper t is 1.2 otherwise');
// parameter parsing
const w = [];
const ok = core.parseParams('binomial', 'n=6,p=0.3', w);
yes(ok.n === 6 && ok.p === 0.3 && w.length === 0, 'parse binomial');
const bad = core.parseParams('binomial', 'n=0,p=2,k=3,zz', w);
yes(bad.n === 6 && bad.p === 0.3 && w.length === 4, 'bad attributes give defaults and warnings: ' + w.length);
const lam = core.parseParams('poisson', 'lambda=2.5', []);
yes(lam.lambda === 2.5, 'parse lambda');
console.log(fails ? fails + ' of ' + cases + ' FAILED' : 'all ' + cases + ' tests passed');
process.exit(fails ? 1 : 0);
