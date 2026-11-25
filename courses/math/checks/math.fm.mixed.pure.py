# checks/math.fm.mixed.pure.py: recomputes every number in "Mixed practice: Further Pure".
# Standard library only: Fraction for exact work, complex numbers, Simpson for integrals, finite differences.
import re
import pathlib
from fractions import Fraction as F
from math import isclose, sqrt, pi, sin, cos, tan, asin, degrees, sinh, cosh, acosh, log, exp, e


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    return sum((f(a + i * h) + 4 * f(a + (i + .5) * h) + f(a + (i + 1) * h)) * h / 6 for i in range(n))


# ---- mark counting: the tokens in every answer add up to the question's [n marks] ----
TOKEN = re.compile(r"^(?:(?:DM|M|A|B)\d(?: FT)?\s*)+$")
text = pathlib.Path("chapters/math.fm.mixed.pure.md").read_text(encoding="utf8")
blocks = re.split(r"(?m)^Q: ", text)[1:]
assert len(blocks) == 31, len(blocks)
chap = []
stars = []
for i, b in enumerate(blocks, 1):
    b = b.split("\n:::")[0]
    m = re.match(r"\[(\d+) marks?\] \(#(math\.fm\.[a-z0-9]+)\) (★+)", b)
    assert m, f"question {i}: header"
    n = int(m.group(1))
    chap.append(m.group(2)); stars.append(len(m.group(3)))
    qpart, ans = b.split("\nA:", 1)
    got = sum(int(d) for grp in re.findall(r"\[([^\]\n]*)\]", ans) if TOKEN.match(grp) for d in re.findall(r"(?:DM|M|A|B)(\d)", grp))
    assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
    parts = [int(x) for x in re.findall(r"(?<!\w)\[(\d+)\](?!\()", qpart)]
    if parts:
        assert sum(parts) == n, f"question {i}: part marks {parts} do not add to {n}"
# no two neighbouring questions from the same chapter; stars never go down within the paper's blocks
assert all(chap[i] != chap[i + 1] for i in range(len(chap) - 1)), "two neighbours share a chapter"
assert stars == sorted(stars), "stars must rise from one to three"
fp1 = {"roots", "series", "matrices", "transform", "induction", "rational", "graphs", "polar", "vectors", "vectors2"}
assert all(c.split(".")[-1] in fp1 for c in chap[:15]), "questions 1 to 15 must be Further Pure 1"
assert any(c.split(".")[-1] not in fp1 for c in chap[15:])
# the table at the end lists every question under its chapter
table = text.split("## Where the questions come from")[1].split(":::recap")[0]
for i, c in enumerate(chap, 1):
    row = [ln for ln in table.splitlines() if f"(#{c})" in ln]
    assert row, c
    assert str(i) in re.split(r"[,\s]+", row[0].split("|")[2].strip()), f"question {i} missing from the table row for {c}"

# ---- 1 series ----
eq("q1", sum(r * r + 3 * r for r in range(1, 13)), 884)
assert 12 * 13 * 25 // 6 == 650 and 3 * (12 * 13 // 2) == 234
# ---- 2 matrices ----
A = [[1, 2, 0], [3, -1, 2]]; B = [[2, 1], [0, 3], [1, -1]]
AB = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(2)] for i in range(2)]
assert AB == [[2, 7], [8, -2]]
BA = [[sum(B[i][k] * A[k][j] for k in range(2)) for j in range(3)] for i in range(3)]
assert len(BA) == 3 and len(BA[0]) == 3
# ---- 3 roots of 2x^2 - 6x + 3 ----
d = sqrt(36 - 24); a_, b_ = (6 + d) / 4, (6 - d) / 4
eq("q3", a_ * a_ + b_ * b_, 6); eq("q3 sums", a_ + b_, 3); eq("q3 prod", a_ * b_, 1.5)
# ---- 4 polar ----
eq("q4a x", 4 * cos(pi / 3), 2); eq("q4a y", 4 * sin(pi / 3), 2 * sqrt(3))
for t in (0.3, 1.0, 2.5):
    r = 6 * cos(t); x, y = r * cos(t), r * sin(t)
    eq("q4b", x * x + y * y, 6 * x, 1e-12)
# ---- 5 vectors ----
def cross(u, v): return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
def dot(u, v): return sum(x * y for x, y in zip(u, v))
assert cross((1, 2, -1), (3, 0, 2)) == (4, -5, -6)
eq("q5", 0.5 * sqrt(16 + 25 + 36), 4.387482193696061, 1e-12); eq("q5 3sf", round(0.5 * sqrt(77), 2), 4.39)
# ---- 6 rational asymptotes ----
g = lambda x: (x * x + 1) / (x - 1)
for x in (-7, 0.2, 3, 50):
    eq("q6", g(x), x + 1 + 2 / (x - 1), 1e-9)
# ---- 7 induction step ----
for k in range(1, 12):
    assert 7 ** (k + 1) - 1 == 7 * (7 ** k - 1) + 6 and (7 ** k - 1) % 6 == 0
# ---- 8 transformations ----
def mm2(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
R = [[0, -1], [1, 0]]; S = [[0, 1], [1, 0]]
assert mm2(R, S) == [[-1, 0], [0, 1]]
# S then R on a point (x, y): S gives (y, x), then R gives (-x, y)
for (x, y) in ((3, 5), (-2, 7)):
    assert (R[0][0] * y + R[0][1] * x, R[1][0] * y + R[1][1] * x) == (-x, y)
# ---- 9 graphs ----
f9 = lambda x: x * x - 4 * x
assert f9(2) == -4 and 1 / f9(2) == -0.25
vals = [f9(x / 10) for x in range(1, 40)]
assert all(-4 <= v < 0 for v in vals)
assert all(f9(x) > 0 for x in (-3, -0.1, 4.1, 9))
# ---- 10 line and plane ----
lam = 3
assert (1 + 2 * lam) + 2 * lam + 3 * (2 - lam) == 10 and (1 + 2 * lam, lam, 2 - lam) == (7, 3, -1)
dd, nn = (2, 1, -1), (1, 2, 3)
assert dot(dd, nn) == 1 and dot(dd, dd) == 6 and dot(nn, nn) == 14
eq("q10b", round(degrees(asin(1 / sqrt(84))), 1), 6.3)
# ---- 11 method of differences ----
for n in (1, 2, 6, 25):
    s = sum(F(1, r * (r + 2)) for r in range(1, n + 1))
    assert s == F(3, 4) - F(2 * n + 3, 2 * (n + 1) * (n + 2)), n
    assert s == F(1, 2) * (1 + F(1, 2) - F(1, n + 1) - F(1, n + 2)), n
for r in range(1, 9):
    assert F(1, r * (r + 2)) == F(1, 2) * (F(1, r) - F(1, r + 2))
# ---- 12 roots: x^3 - 4x^2 + 5x - 7 ----
def durand(c):
    n = len(c) - 1
    r = [(0.4 + 0.9j) ** k for k in range(n)]
    for _ in range(500):
        for i in range(n):
            p = sum(c[k] * r[i] ** (n - k) for k in range(n + 1))
            q = 1
            for j in range(n):
                if j != i:
                    q *= (r[i] - r[j])
            r[i] -= p / c[0] / q
    return r
rt = durand([1, -4, 5, -7])
eq("q12a", sum(x * x for x in rt).real, 6, 1e-9); assert 16 - 10 == 6
for x in rt:
    y = 1 / x
    eq("q12b", abs(7 * y ** 3 - 5 * y ** 2 + 4 * y - 1), 0, 1e-8)
for y in (-2, 0.5, 3):
    eq("q12b expand", 1 / y ** 3 - 4 / y ** 2 + 5 / y - 7, (1 - 4 * y + 5 * y * y - 7 * y ** 3) / y ** 3, 1e-9)
# ---- 13 cardioid ----
eq("q13", 0.5 * simpson(lambda t: (2 + 2 * cos(t)) ** 2, 0, 2 * pi), 6 * pi, 1e-8)
eq("q13 antiderivative", 2 * (1.5 * 2 * pi + 0 + 0), 6 * pi)
for t in (0.4, 1.3):
    eq("q13 expand", (2 + 2 * cos(t)) ** 2 / 2, 2 * (1.5 + 2 * cos(t) + 0.5 * cos(2 * t)), 1e-12)
# ---- 14 3x3 inverse ----
M = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
def minor(Mx, i, j):
    m = [[Mx[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
cof = [[(-1) ** (i + j) * minor(M, i, j) for j in range(3)] for i in range(3)]
assert cof == [[-24, 20, -5], [18, -15, 4], [5, -4, 1]]
det = sum(M[0][j] * cof[0][j] for j in range(3))
assert det == 1 and 1 * (0 - 24) - 2 * (0 - 20) + 3 * (0 - 5) == 1
Minv = [[cof[j][i] for j in range(3)] for i in range(3)]
assert Minv == [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]
prod = [[sum(M[i][k] * Minv[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert prod == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# ---- 15 induction: sum r(r+1) ----
for n in range(1, 30):
    assert sum(r * (r + 1) for r in range(1, n + 1)) == n * (n + 1) * (n + 2) // 3
for k in range(1, 20):
    assert F(k * (k + 1) * (k + 2), 3) + (k + 1) * (k + 2) == F((k + 1) * (k + 2) * (k + 3), 3)
# ---- 16 hyperbolic ----
for x in (-1.2, 0.3, 2.0):
    eq("q16a", sinh(2 * x), 2 * sinh(x) * cosh(x), 1e-12)
    eq("q16a exp", 2 * 0.5 * (exp(x) - exp(-x)) * 0.5 * (exp(x) + exp(-x)), 0.5 * (exp(2 * x) - exp(-2 * x)), 1e-12)
for x in (0, acosh(1.5), -acosh(1.5)):
    eq("q16b", sinh(2 * x), 3 * sinh(x), 1e-12)
eq("q16b value", round(acosh(1.5), 3), 0.962)
# ---- 17 sum from n+1 to 2n ----
for n in range(1, 25):
    assert sum(r * r for r in range(n + 1, 2 * n + 1)) * 6 == n * (2 * n + 1) * (7 * n + 1)
    assert F(2 * n * (2 * n + 1) * (4 * n + 1), 6) - F(n * (n + 1) * (2 * n + 1), 6) == F(n * (2 * n + 1) * (7 * n + 1), 6)
# ---- 18 integral of sinh^2 ----
F18 = lambda x: sinh(2 * x) / 4 - x / 2
eq("q18", F18(1.3) - F18(0.2), simpson(lambda x: sinh(x) ** 2, 0.2, 1.3), 1e-9)
eq("q18 id", cosh(2 * 0.7), 1 + 2 * sinh(0.7) ** 2, 1e-12)
# ---- 19 area scale factor ----
assert 3 * 4 - 1 * 2 == 10 and 10 * 6 == 60
# ---- 20 de Moivre ----
z = complex(sqrt(3), -1)
eq("q20 mod", abs(z), 2); eq("q20 arg", __import__("cmath").phase(z), -pi / 6)
w = z ** 5
eq("q20 re", w.real, -16 * sqrt(3), 1e-9); eq("q20 im", w.imag, -16, 1e-9)
eq("q20 polar", 32 * cos(-5 * pi / 6), -16 * sqrt(3), 1e-9)
# ---- 21 first order DE ----
y21 = lambda x: exp(3 * x) + exp(2 * x)
eq("q21 y0", y21(0), 2)
for x in (0.0, 0.5, -0.7):
    eq("q21", (y21(x + 1e-6) - y21(x - 1e-6)) / 2e-6 - 2 * y21(x), exp(3 * x), 1e-4)
# ---- 22 system with k ----
def det3(Mx):
    a, b, c, d_, e_, f_, g_, h_, i_ = [v for r in Mx for v in r]
    return a * (e_ * i_ - f_ * h_) - b * (d_ * i_ - f_ * g_) + c * (d_ * h_ - e_ * g_)
for k in (-3, 0, 4, 7):
    assert det3([[1, 1, 1], [1, 2, 3], [2, 3, k]]) == k - 4 == 1 * (2 * k - 9) - 1 * (k - 6) + 1 * (3 - 4)
# the third equation (k = 4) is the sum of the first two: coefficients (2, 3, 4), constant 5
assert (1 + 1, 1 + 2, 1 + 3, 1 + 4) == (2, 3, 4, 5)
for lm in (-2, 0, 3.5):
    x, y_, zz = lm - 2, 3 - 2 * lm, lm
    assert (x + y_ + zz, x + 2 * y_ + 3 * zz, 2 * x + 3 * y_ + 4 * zz) == (1, 4, 5)
# ---- 23 Maclaurin of e^(sin x) ----
y23 = lambda x: exp(sin(x))
h = 1e-3
eq("q23 y'(0)", (y23(h) - y23(-h)) / (2 * h), 1, 1e-5)
eq("q23 y''(0)", (y23(h) - 2 * y23(0) + y23(-h)) / h ** 2, 1, 1e-5)
h = 2e-2
y3 = (y23(2 * h) - 2 * y23(h) + 2 * y23(-h) - y23(-2 * h)) / (2 * h ** 3)
eq("q23 y'''(0)", y3, 0, 1e-2)
for x in (0.01, -0.02):
    eq("q23 series", y23(x), 1 + x + x * x / 2, 1e-6)
for x in (0.3, 0.9, 2.0):
    d2 = (y23(x + 1e-4) - 2 * y23(x) + y23(x - 1e-4)) / 1e-8
    eq("q23 y''", d2, y23(x) * (cos(x) ** 2 - sin(x)), 1e-3)
    d1 = (y23(x + 1e-6) - y23(x - 1e-6)) / 2e-6
    eq("q23 y'", d1, y23(x) * cos(x), 1e-5)
# ---- 24 eigenvalues ----
A24 = [[3, 1], [2, 2]]
for lam, v in ((1, (1, -2)), (4, (1, 1))):
    assert (A24[0][0] * v[0] + A24[0][1] * v[1], A24[1][0] * v[0] + A24[1][1] * v[1]) == (lam * v[0], lam * v[1])
    assert (3 - lam) * (2 - lam) - 2 == 0 and lam * lam - 5 * lam + 4 == 0
# ---- 25 foot of perpendicular ----
Pt = (1, 2, 0); n25 = (2, -1, 2)
t = F(9 - dot(n25, Pt), dot(n25, n25))
assert t == 1
Fp = tuple(p + t * c for p, c in zip(Pt, n25))
assert Fp == (3, 1, 2) and dot(n25, Fp) == 9
eq("q25b", sqrt(sum((a - b) ** 2 for a, b in zip(Fp, Pt))), 3)
Pr = tuple(p + 2 * (f - p) for p, f in zip(Pt, Fp))
assert Pr == (5, 0, 4)
assert dot(n25, Pr) - 9 == 9 - dot(n25, Pt)       # P and its reflection are equally far from the plane, on opposite sides
# ---- 26 reduction formula I_n = n I_{n-1} - 1/e ----
def I(n): return simpson(lambda x: x ** n * exp(-x), 0, 1)
for n in range(1, 7):
    eq(f"q26a {n}", I(n), n * I(n - 1) - exp(-1), 1e-9)
eq("q26b I0", I(0), 1 - exp(-1)); eq("q26b I1", I(1), 1 - 2 / e); eq("q26b I2", I(2), 2 - 5 / e); eq("q26b I3", I(3), 6 - 16 / e)
# ---- 27 second order DE ----
y27 = lambda x: 2 * x - 0.8
eq("q27 PI", 0 + 2 * 2 + 5 * y27(1.7), 10 * 1.7, 1e-12)
eq("q27 PI2", 0 + 2 * 2 + 5 * y27(-0.4), 10 * -0.4, 1e-12)
cf = lambda x: exp(-x) * (0.7 * cos(2 * x) - 1.3 * sin(2 * x))
for x in (0.0, 0.8, 2.0):
    d1 = (cf(x + 1e-5) - cf(x - 1e-5)) / 2e-5
    d2 = (cf(x + 1e-4) - 2 * cf(x) + cf(x - 1e-4)) / 1e-8
    eq("q27 CF", d2 + 2 * d1 + 5 * cf(x), 0, 1e-3)
assert 4 - 20 == -16 and sqrt(16) / 2 == 2
# ---- 28 set of values ----
for yv in (2 - 2 * sqrt(2), 2 + 2 * sqrt(2)):
    eq("q28 disc", yv ** 2 - 4 * (yv + 1), 0, 1e-12)
    xv = yv / 2
    eq("q28 x", xv, 1 + (1 if yv > 0 else -1) * sqrt(2), 1e-12)
    eq("q28 y", g(xv), yv, 1e-9)
    eq("q28 stationary", (g(xv + 1e-6) - g(xv - 1e-6)) / 2e-6, 0, 1e-5)
for x in [i / 20 for i in range(-200, 200)]:
    if abs(x - 1) > 1e-9:
        v = g(x)
        assert v <= 2 - 2 * sqrt(2) + 1e-9 or v >= 2 + 2 * sqrt(2) - 1e-9
# ---- 29 cube roots of 8i ----
rts = [2 * complex(cos(pi / 6 + 2 * k * pi / 3), sin(pi / 6 + 2 * k * pi / 3)) for k in range(3)]
for zz in rts:
    eq("q29a", abs(zz ** 3 - 8j), 0, 1e-12)
args = [__import__("cmath").phase(zz) for zz in rts]
eq("q29 args", sum(abs(a - b) for a, b in zip(sorted(args), [-pi / 2, pi / 6, 5 * pi / 6])), 0, 1e-12)
area = 0.5 * abs((rts[1] - rts[0]).real * (rts[2] - rts[0]).imag - (rts[1] - rts[0]).imag * (rts[2] - rts[0]).real)
eq("q29b", area, 3 * sqrt(3), 1e-12); eq("q29b parts", 3 * 0.5 * 2 * 2 * sin(2 * pi / 3), 3 * sqrt(3), 1e-12)
# ---- 30 arc length and surface area of y = cosh x on [0, ln 3] ----
eq("q30a", simpson(lambda x: sqrt(1 + sinh(x) ** 2), 0, log(3)), 4 / 3, 1e-9)
eq("q30a sinh", sinh(log(3)), 4 / 3)
eq("q30b", 2 * pi * simpson(lambda x: cosh(x) * sqrt(1 + sinh(x) ** 2), 0, log(3)), pi * (log(3) + 20 / 9), 1e-8)
eq("q30b sinh", sinh(2 * log(3)), 40 / 9)
# ---- 31 matrix powers ----
Mm = [[3, -2], [2, -1]]
P = [[1, 0], [0, 1]]
for n in range(1, 15):
    P = mm2(P, Mm)
    assert P == [[1 + 2 * n, -2 * n], [2 * n, 1 - 2 * n]], n
for k in range(1, 15):
    Mk = [[1 + 2 * k, -2 * k], [2 * k, 1 - 2 * k]]
    assert mm2(Mk, Mm) == [[3 + 2 * k, -2 - 2 * k], [2 + 2 * k, -1 - 2 * k]]
print("ok")
