// data/test_fm_demoivre.js: the arithmetic of widgets/fm-demoivre.js against Python's cmath.
// Run: node data/test_fm_demoivre.js
const { spawnSync } = require('child_process');
const path = require('path');
const core = require(path.join(__dirname, '..', 'widgets', 'fm-demoivre.js'));
const PI = Math.PI;

function py(code) {
  const res = spawnSync('py', ['-c', code], { encoding: 'utf8' });
  if (res.status !== 0) throw new Error('python failed: ' + res.stderr);
  return JSON.parse(res.stdout);
}
let fails = 0;
const near = (a, b, tol, what) => { if (!(Math.abs(a - b) <= tol)) { fails++; console.log('FAIL', what, a, b); } };

// reduceArg
[[0, 0], [PI, PI], [-PI, PI], [3 * PI, PI], [-3 * PI, PI], [PI + 1e-15, PI], [2 * PI, 0], [7, 7 - 2 * PI], [-7, -7 + 2 * PI], [PI / 2, PI / 2]].forEach(([t, want]) => near(core.reduceArg(t), want, 1e-9, 'reduceArg ' + t));

// roots against cmath: many (r, theta, n)
const cases = [];
[0.05, 0.5, 1, 2.5, 16, 100].forEach((r) => [-3.1, -1, 0, 0.5, PI, 2.4, 7].forEach((t) => [2, 3, 4, 5, 6, 7, 11, 12].forEach((n) => cases.push([r, t, n]))));
const expectedRoots = py(`
import cmath, json
out = []
for r, t, n in ${JSON.stringify(cases)}:
    w = cmath.rect(r, t)
    roots = []
    for k in range(n):
        z = cmath.rect(r ** (1 / n), (t + 2 * cmath.pi * k) / n)
        roots.append([z.real, z.imag, abs(z), cmath.phase(z)])
    out.append(roots)
print(json.dumps(out))
`);
cases.forEach(([r, t, n], i) => {
  const got = core.rootList(r, t, n);
  if (got.length !== n) { fails++; console.log('FAIL length', r, t, n); return; }
  let sr = 0, si = 0;
  got.forEach((p, k) => {
    const e = expectedRoots[i][k];
    near(p.re, e[0], 1e-9 * Math.max(1, Math.abs(e[0])), `root re r=${r} t=${t} n=${n} k=${k}`);
    near(p.im, e[1], 1e-9 * Math.max(1, Math.abs(e[1])), `root im r=${r} t=${t} n=${n} k=${k}`);
    near(p.mod, e[2], 1e-9 * Math.max(1, e[2]), `root mod r=${r} t=${t} n=${n} k=${k}`);
    // the reduced argument equals cmath.phase(z) of the same root (compare as points on the circle: cos and sin)
    near(Math.cos(p.arg), Math.cos(e[3]), 1e-9, 'arg cos');
    near(Math.sin(p.arg), Math.sin(e[3]), 1e-9, 'arg sin');
    if (!(p.arg > -PI + 1e-12 || Math.abs(p.arg - PI) < 1e-9) || p.arg > PI + 1e-12) { fails++; console.log('FAIL arg range', p.arg); }
    sr += p.re; si += p.im;
    // each root raised to the power n gives w
    const wr = Math.pow(p.mod, n) * Math.cos(n * p.arg), wi = Math.pow(p.mod, n) * Math.sin(n * p.arg);
    near(wr, r * Math.cos(t), 1e-7 * Math.max(1, r), 'z^n re');
    near(wi, r * Math.sin(t), 1e-7 * Math.max(1, r), 'z^n im');
  });
  near(sr, 0, 1e-9 * Math.max(1, got[0].mod * n), 'sum of roots re');
  near(si, 0, 1e-9 * Math.max(1, got[0].mod * n), 'sum of roots im');
});

// powers against cmath, positive and negative n
const pcases = [];
[0.2, 0.7, 1, 1.1, 2, 3].forEach((r) => [-2.9, -0.4, 0, 0.5, 1.3, PI].forEach((t) => [-6, -3, -1, 0, 1, 2, 5, 12].forEach((n) => pcases.push([r, t, n]))));
const expectedPow = py(`
import cmath, json
out = []
for r, t, n in ${JSON.stringify(pcases)}:
    z = cmath.rect(r, t)
    step = 1 if n >= 0 else -1
    pts = []
    for k in range(0, n + step, step):
        v = z ** k
        pts.append([k, v.real, v.imag, abs(v)])
    out.append(pts)
print(json.dumps(out))
`);
pcases.forEach(([r, t, n], i) => {
  const got = core.powerPoints(r, t, n);
  const want = expectedPow[i];
  if (got.length !== want.length) { fails++; console.log('FAIL power length', r, t, n, got.length, want.length); return; }
  got.forEach((p, j) => {
    const e = want[j];
    if (p.k !== e[0]) { fails++; console.log('FAIL k', p.k, e[0]); }
    near(p.re, e[1], 1e-9 * Math.max(1, Math.abs(e[1])), `pow re r=${r} t=${t} n=${n} k=${p.k}`);
    near(p.im, e[2], 1e-9 * Math.max(1, Math.abs(e[2])), `pow im r=${r} t=${t} n=${n} k=${p.k}`);
    near(p.mod, e[3], 1e-9 * Math.max(1, e[3]), 'pow mod');
    near(p.mod, Math.pow(r, p.k), 1e-9 * Math.max(1, p.mod), 'mod = r^k');
    if (!(p.arg > -PI - 1e-12 && p.arg <= PI + 1e-12)) { fails++; console.log('FAIL pow arg range', p.arg); }
  });
});
console.log(fails ? `${fails} failure(s)` : `fm-demoivre logic ok (${cases.length} root cases, ${pcases.length} power cases)`);
process.exit(fails ? 1 : 0);
