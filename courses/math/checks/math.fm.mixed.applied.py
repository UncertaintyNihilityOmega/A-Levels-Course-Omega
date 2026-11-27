# checks/math.fm.mixed.applied.py: recomputes every number in "Mixed practice: Further Mechanics and Statistics".
# Standard library only: Fraction for exact work, Simpson for integrals, t and chi-squared percentage points by
# integrating the density and bisecting, Wilcoxon rank-sum values by counting every rank subset.
import re
import pathlib
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import isclose, sqrt, pi, sin, cos, tan, atan, acos, degrees, radians, exp, log, lgamma, comb, factorial
from statistics import NormalDist

N01 = NormalDist()


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    return sum((f(a + i * h) + 4 * f(a + (i + .5) * h) + f(a + (i + 1) * h)) * h / 6 for i in range(n))


# ---- mark counting and structure ----
TOKEN = re.compile(r"^(?:(?:DM|M|A|B)\d(?: FT)?\s*)+$")
text = pathlib.Path("chapters/math.fm.mixed.applied.md").read_text(encoding="utf8")
blocks = re.split(r"(?m)^Q: ", text)[1:]
assert len(blocks) == 32, len(blocks)
chap, stars, marks = [], [], []
for i, b in enumerate(blocks, 1):
    b = b.split("\n:::")[0]
    m = re.match(r"\[(\d+) marks?\] \(#(math\.fm\.[a-z0-9]+)\) (★+)", b)
    assert m, f"question {i}: header"
    n = int(m.group(1))
    chap.append(m.group(2)); stars.append(len(m.group(3))); marks.append(n)
    qpart, ans = b.split("\nA:", 1)
    got = sum(int(d) for grp in re.findall(r"\[([^\]\n]*)\]", ans) if TOKEN.match(grp) for d in re.findall(r"(?:DM|M|A|B)(\d)", grp))
    assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
    parts = [int(x) for x in re.findall(r"(?<!\w)\[(\d+)\](?!\()", qpart)]
    if parts:
        assert sum(parts) == n, f"question {i}: part marks {parts} do not add to {n}"
assert all(chap[i] != chap[i + 1] for i in range(31)), "two neighbours share a chapter"
fm = {"projectiles", "com", "rigid", "elastic", "circular", "vertical", "variable", "impulse", "oblique"}
fs = {"crv", "inference", "twosample", "chisq", "contingency", "nonpar", "wilcoxon", "pgf"}
assert all(c.split(".")[-1] in fm for c in chap[:14]), "questions 1 to 14 are Further Mechanics"
assert all(c.split(".")[-1] in fs for c in chap[14:28]), "questions 15 to 28 are Further Statistics"
assert stars[:14] == sorted(stars[:14]) and stars[14:28] == sorted(stars[14:28])
assert all(s == 3 for s in stars[28:])
assert [c.split(".")[-1] in fm for c in chap[28:]] == [True, False, True, False], "mixed set alternates"
assert set(c.split(".")[-1] for c in chap) == fm | fs, "every chapter of the two papers appears"
assert stars[:14] == [1] * 5 + [2] * 5 + [3] * 4 and stars[14:28] == [1] * 5 + [2] * 5 + [3] * 4
# the table at the end lists every question under its chapter
table = text.split("## Where the questions come from")[1].split(":::recap")[0]
labels = [f"{nm} {j}" for nm, cnt in (("Mechanics warm-up", 5), ("Mechanics exam standard", 5), ("Mechanics stretch", 4), ("Statistics warm-up", 5), ("Statistics exam standard", 5), ("Statistics stretch", 4), ("mixed set", 4)) for j in range(1, cnt + 1)]
assert len(labels) == len(chap) == 32
for i, c in enumerate(chap, 1):
    row = [ln for ln in table.splitlines() if f"(#{c})" in ln]
    assert row, c
    assert labels[i - 1] in [x.strip() for x in row[0].split("|")[2].split(",")], f"question {labels[i - 1]} missing from the table row for {c}"
g = 10

# ---- 1 projectile ----
eq("q1a", (20 * sin(radians(30))) ** 2 / (2 * g), 5)
eq("q1b", 20 * cos(radians(30)) * 2, 34.64, 0.01)
# ---- 2 L-shaped lamina ----
A1, A2 = 12, 10
xb = F(A1 * 3 + A2 * 1, A1 + A2); yb = F(A1 * 1 + A2 * F(9, 2), A1 + A2)
assert xb == F(23, 11) and yb == F(57, 22)
eq("q2", float(xb), 2.09, 0.005); eq("q2", float(yb), 2.59, 0.005)
# ---- 3 dv/dt = -2v ----
h = 1e-5; v = 10.0
for k in range(int(0.7 / h)):
    v += -2 * v * h
eq("q3 v(0.7)", v, 10 * exp(-1.4), 1e-3)
# ---- 4 elastic string ----
eq("q4 T", 18 * 0.3 / 0.6, 9); eq("q4 E", 18 * 0.09 / 1.2, 1.35)
# ---- 5 horizontal circle on a table ----
eq("q5 w", 3 / 0.5, 6); eq("q5 T", 0.4 * 9 / 0.5, 7.2); eq("q5 T w", 0.4 * 0.5 * 36, 7.2)
# ---- 6 ladder ----
S = 200 * 1.5 / 4
eq("q6 S", S, 75); eq("q6 mu", S / 200, 0.375)
assert 3 ** 2 + 4 ** 2 == 5 ** 2
# ---- 7 string released from horizontal ----
v2 = 2 * g * 0.8
eq("q7 v", sqrt(v2), 4); eq("q7 T", 0.5 * g + 0.5 * v2 / 0.8, 15)
# ---- 8 direct impact ----
vA = F(12 - 9, 5); vB = vA + 3
assert vA == F(3, 5) and vB == F(18, 5) and 2 * 6 == 2 * vA + 3 * vB
ke0 = F(1, 2) * 2 * 36; ke1 = F(1, 2) * 2 * vA ** 2 + F(1, 2) * 3 * vB ** 2
eq("q8 KE after", float(ke1), 19.8); eq("q8 loss", float(ke0 - ke1), 16.2)
# ---- 9 oblique impact with a wall ----
tn, nm = 10 * cos(radians(30)), 10 * sin(radians(30))
eq("q9 comps", tn, 8.66, 0.005); eq("q9 normal", nm, 5)
sp = sqrt(tn ** 2 + (0.6 * nm) ** 2)
eq("q9 speed2", sp ** 2, 84); eq("q9 speed", sp, 9.17, 0.005)
eq("q9 angle", degrees(atan(3 / tn)), 19.1, 0.05)
# ---- 10 horizontal elastic string on a table ----
epe = 15 * 0.2 ** 2 / (2 * 0.5)
eq("q10 epe", epe, 0.6); eq("q10 v2", 2 * epe / 0.6, 2); eq("q10 v", sqrt(2), 1.41, 0.005)
# ---- 11 cliff projectile ----
ux, uy = 25 * 0.8, 25 * 0.6
assert (ux, uy) == (20, 15) and F(3, 4) == F(15, 20)
for t in (4, -1):
    assert -(15 * t - 5 * t * t) - 20 == 5 * (t * t - 3 * t - 4)    # the equation -20 = 15t - 5t^2 rearranged
assert 15 * 4 - 5 * 16 == -20 and 4 * 4 - 3 * 4 - 4 == 0 and (4 - 4) * (4 + 1) == 0
eq("q11b", ux * 4, 80)
vy = uy - g * 4
eq("q11c vy", vy, -25); eq("q11c speed", sqrt(ux ** 2 + vy ** 2), 32.0, 0.05); eq("q11c speed2", ux ** 2 + vy ** 2, 1025)
eq("q11c angle", degrees(atan(25 / 20)), 51.3, 0.05)
# ---- 12 hemisphere and cone ----
def xbar(h, r=1.0):
    vh, vc = 2 / 3 * r ** 3, r * r * h / 3
    return (vc * h / 4 - vh * 3 * r / 8) / (vh + vc)
for h in (0.5, 1, 2.2, 3):
    eq("q12a formula", xbar(h), (h * h - 3) / (4 * (2 + h)), 1e-12)
eq("q12b", xbar(sqrt(3)), 0, 1e-12)
assert xbar(1.7) < 0 < xbar(1.8)
eq("q12c", xbar(1), -1 / 6, 1e-12); eq("q12c vertex", 1 - xbar(1), 7 / 6, 1e-12)
# ---- 13 bowl ----
a, m, w = 0.8, 0.3, 5
Rr = m * a * w * w
eq("q13 R", Rr, 6); c = m * g / Rr
eq("q13b cos", c, 0.5); eq("q13b theta", degrees(acos(c)), 60.0, 1e-9)
r = a * sin(acos(c))
eq("q13c r", r, 0.693, 0.0005); eq("q13c v", r * w, 3.46, 0.005)
eq("q13d", g / a, 12.5); eq("q13d w", sqrt(12.5), 3.54, 0.005)
# the circle satisfies both equations
th = acos(c)
eq("q13 vertical", Rr * cos(th), m * g, 1e-9); eq("q13 horizontal", Rr * sin(th), m * r * w * w, 1e-9)
# ---- 14 boat ----
dt = 1e-4; vb = 0.0; dist = 0.0; t = 0.0
while t < 10 - 1e-12:
    k1 = 0.1 * (20 - vb)
    vm = vb + k1 * dt / 2
    k2 = 0.1 * (20 - vm)
    vb += k2 * dt; t += dt
    dist += vb * dt
eq("q14a v(10)", vb, 20 * (1 - exp(-1)), 1e-4)
eq("q14c dist", 200 / exp(1), 73.6, 0.05)
eq("q14c integral", simpson(lambda t: 20 * (1 - exp(-0.1 * t)), 0, 10), 200 / exp(1), 1e-6)
eq("q14c sim", dist, 200 / exp(1), 5e-3)
eq("q14a eq", 400 / 200, 2.0); eq("q14a k", 20 / 200, 0.1)

# ---- statistics helpers ----
def t_pdf(x, v):
    return exp(lgamma((v + 1) / 2) - lgamma(v / 2) - 0.5 * log(v * pi) - (v + 1) / 2 * log(1 + x * x / v))


def t_cdf(x, v, n=1000):
    hh = x / n
    return 0.5 + (t_pdf(0, v) + t_pdf(x, v) + sum((4 if i % 2 else 2) * t_pdf(i * hh, v) for i in range(1, n))) * hh / 3


def t_inv(p, v):
    lo, hi = 0.0, 70.0
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_cdf(mid, v) < p else (lo, mid)
    return lo


def chi2_cdf(x, v, n=2000):
    top = sqrt(x)
    cc = 2 / (2 ** (v / 2) * exp(lgamma(v / 2)))
    gg = lambda u: cc * u ** (v - 1) * exp(-u * u / 2)
    hh = top / n
    return (gg(0) + gg(top) + sum((4 if i % 2 else 2) * gg(i * hh) for i in range(1, n))) * hh / 3


def chi2_inv(p, v):
    lo, hi = 0.0, 300.0
    for _ in range(70):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if chi2_cdf(mid, v) < p else (lo, mid)
    return (lo + hi) / 2


def rs_crit(mm, nn, al):
    cnt = Counter(sum(s) for s in combinations(range(1, mm + nn + 1), mm))
    tot = comb(mm + nn, mm); cum = 0; best = None
    for ww in range(mm * (mm + 1) // 2, mm * (2 * nn + mm + 1) // 2 + 1):
        cum += cnt.get(ww, 0)
        if F(cum, tot) <= al:
            best = ww
        else:
            break
    return best


# ---- 15 f = k x^2 ----
eq("q15 k", 1 / simpson(lambda x: x * x, 0, 3), 1 / 9, 1e-9)
eq("q15 E", simpson(lambda x: x * x * x / 9, 0, 3), 9 / 4, 1e-9)
# ---- 16 one-sample t ----
x16 = [12.1, 11.8, 12.6, 12.3, 11.9, 12.5]
mean16 = sum(x16) / 6; S16 = sum((v - mean16) ** 2 for v in x16)
eq("q16 mean", mean16, 12.2, 1e-9); eq("q16 S", S16, 0.52, 1e-9)
s16 = sqrt(S16 / 5); eq("q16 s2", S16 / 5, 0.104, 1e-9); eq("q16 s", s16, 0.3225, 5e-5)
t16 = (mean16 - 12) / (s16 / sqrt(6)); eq("q16 t", t16, 1.52, 0.005)
eq("q16 crit", t_inv(0.95, 5), 2.015, 1e-3); assert t16 < 2.015
# ---- 17 die ----
o17 = [15, 22, 18, 25, 17, 23]; assert sum(o17) == 120
X17 = sum((v - 20) ** 2 / 20 for v in o17)
assert sum((v - 20) ** 2 for v in o17) == 76
eq("q17 X2", X17, 3.8, 1e-9); eq("q17 crit", chi2_inv(0.95, 5), 11.070, 1e-3); assert X17 < 11.07
# ---- 18 sign test ----
p18 = sum(comb(10, k) for k in (8, 9, 10)) / 1024
assert comb(10, 8) + comb(10, 9) + comb(10, 10) == 45 + 10 + 1
eq("q18 p", p18, 0.0547, 5e-5); assert p18 > 0.05
# ---- 19 PGFs of Poisson ----
eq("q19", exp(-5) * 25 / 2, 0.0842, 5e-5)
# ---- 20 paired t ----
d20 = [2.1, 3.4, -0.5, 1.8, 2.9, 0.7, 3.3, 1.5]
sd, sdd = sum(d20), sum(v * v for v in d20)
eq("q20 sum", sd, 15.2, 1e-9); eq("q20 sumsq", sdd, 41.5, 1e-9)
dbar = sd / 8; s2_20 = (sdd - sd ** 2 / 8) / 7
eq("q20 dbar", dbar, 1.9, 1e-9); eq("q20 s2", s2_20, 1.803, 5e-4); eq("q20 s", sqrt(s2_20), 1.3427, 5e-5)
t20 = dbar / (sqrt(s2_20) / sqrt(8)); eq("q20 t", t20, 4.00, 0.005)
eq("q20 crit", t_inv(0.95, 7), 1.895, 1e-3); assert t20 > 1.895
# ---- 21 contingency 2 x 3 ----
O21 = [[30, 45, 25], [50, 30, 20]]
rt = [sum(r_) for r_ in O21]; ct = [sum(O21[i][j] for i in range(2)) for j in range(3)]
assert rt == [100, 100] and ct == [80, 75, 45]
E21 = [[rt[i] * ct[j] / 200 for j in range(3)] for i in range(2)]
assert E21 == [[40.0, 37.5, 22.5]] * 2
X21 = sum((O21[i][j] - E21[i][j]) ** 2 / E21[i][j] for i in range(2) for j in range(3))
eq("q21 X2", X21, 8.56, 0.005); eq("q21 inner", 2.5 + 1.5 + 2.5 ** 2 / 22.5, 4.2778, 1e-4)
eq("q21 crit", chi2_inv(0.95, 2), 5.991, 1e-3); assert X21 > 5.991
# ---- 22 rank-sum ----
Xs = [12, 15, 9, 18, 11]; Ys = [20, 17, 22, 14, 25, 19]
allv = sorted(Xs + Ys); rk = {v: i + 1 for i, v in enumerate(allv)}
assert len(set(allv)) == 11
rX = sorted(rk[v] for v in Xs)
assert rX == [1, 2, 3, 5, 7] and sum(rX) == 18 and 5 * 12 - 18 == 42
assert rs_crit(5, 6, F(25, 1000)) == 18 and 18 <= 18
# ---- 23 CDF (x^3 + x)/10 ----
Fc = lambda x: (x ** 3 + x) / 10
eq("q23 F(0)", Fc(0), 0); eq("q23 F(2)", Fc(2), 1)
eq("q23 f", (Fc(1.2 + 1e-6) - Fc(1.2 - 1e-6)) / 2e-6, (3 * 1.44 + 1) / 10, 1e-6)
eq("q23 P", 1 - Fc(1.5), 0.5125, 1e-12); eq("q23 pdf area", simpson(lambda x: (3 * x * x + 1) / 10, 0, 2), 1, 1e-9)
assert all((3 * x * x + 1) / 10 > 0 for x in (0, 1, 2))
# ---- 24 t interval ----
tc = t_inv(0.975, 8); eq("q24 t", tc, 2.306, 1e-3)
eq("q24 half", 2.306 * 1.2, 2.767, 5e-4); eq("q24 lo", 52.4 - 2.767, 49.6, 0.05); eq("q24 hi", 52.4 + 2.767, 55.2, 0.05)
# ---- 25 PGF (1+t)/(4-2t) ----
G = lambda t: (1 + t) / (4 - 2 * t)
eq("q25 G(1)", G(1), 1)
hh = 1e-5
g1 = (G(1 + hh) - G(1 - hh)) / (2 * hh); g2 = (G(1 + hh) - 2 * G(1) + G(1 - hh)) / hh ** 2
eq("q25 E", g1, 1.5, 1e-6); eq("q25 G''", g2, 3, 1e-3)
eq("q25 var", g2 + g1 - g1 ** 2, 2.25, 1e-3)
for t in (0.3, 1.0, 1.7):
    eq("q25 G'", ((4 - 2 * t) + 2 * (1 + t)) / (4 - 2 * t) ** 2, 6 / (4 - 2 * t) ** 2, 1e-12)
    eq("q25 G''", 24 / (4 - 2 * t) ** 3, (G(t + 1e-4) - 2 * G(t) + G(t - 1e-4)) / 1e-8, 1e-4)
p25 = [F(1, 4)] + [F(3, 8) * F(1, 2) ** (r - 1) for r in range(1, 80)]
assert p25[:3] == [F(1, 4), F(3, 8), F(3, 16)]
eq("q25 mean from pmf", float(sum(r * q for r, q in enumerate(p25))), 1.5, 1e-9)
eq("q25 var from pmf", float(sum(r * r * q for r, q in enumerate(p25)) - sum(r * q for r, q in enumerate(p25)) ** 2), 2.25, 1e-9)
# ---- 26 Poisson fit ----
obs = [12, 26, 24, 12, 6]; assert sum(obs) == 80
lam = 1.7
P = [exp(-lam) * lam ** r / factorial(r) for r in range(4)]; P.append(1 - sum(P))
E26 = [80 * q for q in P]
for got, want in zip(E26, (14.61, 24.84, 21.12, 11.97, 7.46)):
    eq("q26 E", got, want, 0.006)
assert all(e >= 5 for e in E26)
X26 = sum((o - e) ** 2 / e for o, e in zip(obs, E26))
eq("q26 X2", X26, 1.20, 0.005)
parts = [(o - e) ** 2 / e for o, e in zip(obs, E26)]
for got, want in zip(parts, (0.468, 0.054, 0.393, 0.000, 0.284)):
    eq("q26 parts", got, want, 0.0006)
Er = [14.61, 24.84, 21.12, 11.97, 7.46]
eq("q26 X2 from rounded E", sum((o - e) ** 2 / e for o, e in zip(obs, Er)), 1.20, 0.005)
eq("q26 remainder", 80 - 14.61 - 24.84 - 21.12 - 11.97, 7.46, 1e-9)
eq("q26 mean", sum(i * o for i, o in enumerate([12, 26, 24, 12])) / 80 + 0, (26 + 48 + 36) / 80, 1e-12)   # the 4-or-more group is not used for the mean here
eq("q26 crit", chi2_inv(0.95, 3), 7.815, 1e-3); assert X26 < 7.815
# ---- 27 one-sample t with sums ----
S27 = 27148 - 520 ** 2 / 10
eq("q27 S", S27, 108); eq("q27 s2", S27 / 9, 12)
t27 = (52 - 50) / (sqrt(12) / sqrt(10)); eq("q27 t", t27, 1.83, 0.005)
t9 = t_inv(0.975, 9); eq("q27 crit", t9, 2.262, 1e-3); assert abs(t27) < 2.262
half = 2.262 * sqrt(12) / sqrt(10)
eq("q27 half", half, 2.478, 0.001); eq("q27 lo", 52 - half, 49.5, 0.03); eq("q27 hi", 52 + half, 54.5, 0.03)
assert 52 - half < 50 < 52 + half
# ---- 28 signed-rank normal approximation ----
n = 30
mu28 = n * (n + 1) / 4; var28 = n * (n + 1) * (2 * n + 1) / 24
eq("q28 mean", mu28, 232.5); eq("q28 var", var28, 2363.75)
assert 140 + 325 == n * (n + 1) // 2
z28 = (140.5 - mu28) / sqrt(var28)
eq("q28 sd", sqrt(var28), 48.62, 0.005); eq("q28 z", z28, -1.89, 0.005)
eq("q28 crit", N01.inv_cdf(0.975), 1.960, 5e-4); assert z28 > -1.96
# ---- 29 elastic string on a smooth incline ----
m29, lam29, l29 = 0.8, 24, 1.0
wd = m29 * g * sin(radians(30)); eq("q29 comp", wd, 4)
v2 = 2 * wd * 1 / m29; eq("q29a v2", v2, 10); eq("q29a v", sqrt(v2), 3.16, 0.005)
xe = (1 + sqrt(13)) / 6
eq("q29b eq", wd * (1 + xe) - lam29 * xe ** 2 / (2 * l29), 0, 1e-12)
eq("q29b x", xe, 0.768, 0.0005); assert 3 * xe ** 2 - xe - 1 < 1e-12
e = wd * l29 / lam29; eq("q29c e", e, 1 / 6, 1e-12)
v2c = (wd * (1 + e) - lam29 * e ** 2 / (2 * l29)) * 2 / m29
eq("q29c v2", v2c, 10.833, 0.001); eq("q29c v", sqrt(v2c), 3.29, 0.005)
eq("q29c 4(1+e)", 4 * (1 + e), 4.667, 0.001); eq("q29c EPE", 12 * e ** 2, 0.333, 0.001)
# numeric simulation of the motion confirms the greatest extension and speed
y, vv, dtt = 1.0, sqrt(v2), 1e-6        # distance down the slope from O; taut at y = 1
ymax, vmax = 1.0, vv
while vv > 0:
    ext = y - 1
    acc = wd / m29 - lam29 * ext / l29 / m29
    vv += acc * dtt; y += vv * dtt
    ymax = max(ymax, y); vmax = max(vmax, vv)
eq("q29 sim max ext", ymax - 1, xe, 2e-3); eq("q29 sim vmax", vmax, sqrt(v2c), 2e-3)
# ---- 30 contingency, combining columns ----
O30 = [[50, 24, 4], [20, 28, 2]]
r30 = [78, 50]; c30 = [70, 52, 6]
assert [sum(r) for r in O30] == r30 and [sum(O30[i][j] for i in range(2)) for j in range(3)] == c30 and sum(r30) == 128
E30 = [[r30[i] * c30[j] / 128 for j in range(3)] for i in range(2)]
eq("q30 E cycle town", E30[0][2], 3.66, 0.005); eq("q30 E cycle village", E30[1][2], 2.34, 0.005)
assert E30[0][2] < 5 and E30[1][2] < 5 and all(E30[i][j] >= 5 for i in range(2) for j in range(2))
O2 = [[50, 28], [20, 30]]; c2 = [70, 58]
E2 = [[r30[i] * c2[j] / 128 for j in range(2)] for i in range(2)]
for got, want in zip(E2[0] + E2[1], (42.66, 35.34, 27.34, 22.66)):
    eq("q30 E2", got, want, 0.006)
cont = [(O2[i][j] - E2[i][j]) ** 2 / E2[i][j] for i in range(2) for j in range(2)]
for got, want in zip(cont, (1.264, 1.526, 1.972, 2.380)):
    eq("q30 contributions", got, want, 0.0006)
X30 = sum(cont); eq("q30 X2", X30, 7.14, 0.005)
assert max(cont) == cont[3]
eq("q30 crit", chi2_inv(0.95, 1), 3.841, 1e-3); assert X30 > 3.841
# ---- 31 inside of a sphere ----
for th in (0.0, 0.5, 1.3, 2.0):
    v2 = 3 * g - 2 * g * (1 - cos(th))          # a = 1
    eq("q31a v2", v2, g * (1 + 2 * cos(th)), 1e-12)
    R = g * cos(th) + v2
    eq("q31a R", R, g * (1 + 3 * cos(th)), 1e-12)
thl = acos(-1 / 3)
eq("q31b v2", g * (1 + 2 * cos(thl)), g / 3, 1e-12)
vl2 = g / 3
# leaving velocity: perpendicular to OP, upward component v * sin(angle of OP with the vertical)
sx, sy = sin(thl), -cos(thl)                    # position of P relative to O (a = 1)
tx, ty = cos(thl), sin(thl)                     # tangent direction for increasing theta
eq("q31c unit", sx * tx + sy * ty, 0, 1e-12)
eq("q31c vy2", vl2 * ty ** 2, 8 * g / 27, 1e-12)
eq("q31c sin", sin(thl), 2 * sqrt(2) / 3, 1e-12)
top = (1 - cos(thl)) + vl2 * ty ** 2 / (2 * g)
eq("q31c top", top, 40 / 27, 1e-12); eq("q31c leaving height", 1 - cos(thl), 4 / 3, 1e-12)
assert 0 < top < 2     # below the top of the sphere
# ---- 32 f = k / x^2 on [1, 4] ----
eq("q32a", simpson(lambda x: 4 / 3 / (x * x), 1, 4), 1, 1e-9)
Fx = lambda x: 4 / 3 * (1 - 1 / x)
eq("q32b F(4)", Fx(4), 1); eq("q32b F", Fx(2.5), simpson(lambda t: 4 / 3 / (t * t), 1, 2.5), 1e-9)
eq("q32c", Fx(1.6), 0.5, 1e-12)
Gy = lambda y: Fx(exp(y))
eq("q32d G", Gy(0.7), 4 / 3 * (1 - exp(-0.7)), 1e-12)
eq("q32d g", (Gy(0.7 + 1e-6) - Gy(0.7 - 1e-6)) / 2e-6, 4 / 3 * exp(-0.7), 1e-6)
eq("q32d top", Gy(log(4)), 1, 1e-12); eq("q32d g area", simpson(lambda y: 4 / 3 * exp(-y), 0, log(4)), 1, 1e-9)
# travel table: combining rail and bus would leave the cycle column below 5
_rows = (78, 50); _cols = (70, 52, 6)
eq("cycle expected town", 78 * 6 / 128, 3.65625, 1e-9)
assert all(r * c / 128 < 5 for r in (78, 50) for c in (6,)) and 50 * 6 / 128 < 5
assert all(r * c / 128 >= 5 for r in _rows for c in (52 + 6, 70))
# L-shaped lamina: base 6 wide, 2 high; upright 2 wide, 5 high on top at the left end
eq("L xbar", (12 * 3 + 10 * 1) / 22, 23 / 11); eq("L ybar", (12 * 1 + 10 * 4.5) / 22, 57 / 22)
print("ok")
