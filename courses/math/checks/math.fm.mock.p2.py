# checks/math.fm.mock.p2.py: recomputes every number in Mock Paper 2 (Further Pure Mathematics 2).
# Standard library only: Fraction for exact matrices, complex numbers, Simpson for integrals, finite differences.
import re
import pathlib
from fractions import Fraction as F
from math import isclose, sqrt, pi, sin, cos, tan, tanh, cosh, sinh, acosh, asinh, log, exp, e


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    return sum((f(a + i * h) + 4 * f(a + (i + .5) * h) + f(a + (i + 1) * h)) * h / 6 for i in range(n))


# ---- mark counting: the tokens in every answer must add up to the question's [n marks] ----
TOKEN = re.compile(r"^(?:(?:DM|M|A|B)\d(?: FT)?\s*)+$")


def count_marks(path, total, expect_qs):
    text = pathlib.Path(path).read_text(encoding="utf8")
    blocks = re.split(r"(?m)^Q: ", text)[1:]
    grand, spread = 0, []
    for i, b in enumerate(blocks, 1):
        b = b.split("\n:::")[0]
        m = re.match(r"\[(\d+) marks?\]", b)
        assert m, f"question {i}: no [n marks]"
        n = int(m.group(1))
        qpart, ans = b.split("\nA:", 1)
        got = 0
        for grp in re.findall(r"\[([^\]\n]*)\]", ans):
            if TOKEN.match(grp):
                got += sum(int(d) for d in re.findall(r"(?:DM|M|A|B)(\d)", grp))
        assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
        parts = [int(x) for x in re.findall(r"(?<!\w)\[(\d+)\](?!\()", qpart)]
        if parts:
            assert sum(parts) == n, f"question {i}: part marks {parts} do not add to {n}"
        grand += n
        spread.append(n)
    assert grand == total, f"paper total {grand}, should be {total}"
    assert len(blocks) == expect_qs, f"{len(blocks)} questions"
    return spread


spread = count_marks("chapters/math.fm.mock.p2.md", 75, 8)
assert spread == [5, 7, 11, 8, 10, 10, 10, 14], spread     # the June 2026 9231/21 spread

# ---- Q1 Maclaurin of cosh^-1(3 + x) ----
f = lambda x: acosh(3 + x)
h = 1e-4
eq("q1 f0", f(0), log(3 + 2 * sqrt(2)), 1e-12)
eq("q1 b", (f(h) - f(-h)) / (2 * h), sqrt(2) / 4, 1e-7)
eq("q1 c", (f(h) - 2 * f(0) + f(-h)) / h ** 2 / 2, -3 * sqrt(2) / 64, 1e-6)
eq("q1 f'0", 1 / sqrt(8), sqrt(2) / 4); eq("q1 f''0", -3 / (8 * sqrt(8)), -3 * sqrt(2) / 32)
for x in (0.01, -0.02):
    eq("q1 series", f(x), log(3 + 2 * sqrt(2)) + sqrt(2) / 4 * x - 3 * sqrt(2) / 64 * x * x, 1e-6)
eq("q1 a", 3 + sqrt(8), (1 + sqrt(2)) ** 2)

# ---- Q2 reduction formula for I_n = int_0^{pi/4} sec^n ----
def I(n): return simpson(lambda x: 1 / cos(x) ** n, 0, pi / 4)
for n in range(2, 9):
    eq(f"q2a n={n}", (n - 1) * I(n), sqrt(2) ** (n - 2) + (n - 2) * I(n - 2), 1e-8)
# the derivative identity
for x in (0.2, 0.5, 0.7):
    for n in (2, 3, 5):
        g = lambda t: tan(t) / cos(t) ** (n - 2)
        eq("q2a d/dx", (g(x + 1e-6) - g(x - 1e-6)) / 2e-6, (n - 1) / cos(x) ** n - (n - 2) / cos(x) ** (n - 2), 1e-5)
eq("q2b I2", I(2), 1, 1e-9); eq("q2b I4", I(4), 4 / 3, 1e-9); eq("q2b I6", I(6), 28 / 15, 1e-8)
assert F(4) + F(4) * F(4, 3) == F(28, 3) and F(28, 3) / 5 == F(28, 15) and F(1) + F(2, 3) + F(1, 5) == F(28, 15)

# ---- Q3 (a) integral, (b) first order DE with tanh ----
eq("q3a", simpson(lambda x: 1 / sqrt(x * x + 2 * x + 5), 0, 1), log(2 * (1 + sqrt(2)) / (1 + sqrt(5))), 1e-10)
eq("q3a sinh", asinh(1) - asinh(0.5), log(2 * (1 + sqrt(2)) / (1 + sqrt(5))), 1e-12)
eq("q3a ln forms", asinh(1), log(1 + sqrt(2))); eq("q3a ln half", asinh(0.5), log((1 + sqrt(5)) / 2))
y = lambda x: (x / 2 + sinh(2 * x) / 4 + 1) / cosh(x)
eq("q3b y(0)", y(0), 1)
for x in (0.0, 0.4, 1.3, -0.8):
    dy = (y(x + 1e-6) - y(x - 1e-6)) / 2e-6
    eq("q3b ode", dy + y(x) * tanh(x), cosh(x), 1e-6)
    eq("q3b cosh^2", cosh(x) ** 2, 0.5 * (1 + cosh(2 * x)), 1e-12)
eq("q3b IF", exp(log(cosh(0.7))), cosh(0.7))

# ---- Q4 parametric curve (tractrix) and its arc length ----
X = lambda t: t - tanh(t)
Y = lambda t: 1 / cosh(t)
for t in (0.3, 1.0, 2.2):
    dx = (X(t + 1e-6) - X(t - 1e-6)) / 2e-6
    dy = (Y(t + 1e-6) - Y(t - 1e-6)) / 2e-6
    eq("q4 dx/dt", dx, tanh(t) ** 2, 1e-6); eq("q4 dy/dt", dy, -tanh(t) / cosh(t), 1e-6)
    eq("q4a", dy / dx, -1 / sinh(t), 1e-5)
    eq("q4b speed", sqrt(dx * dx + dy * dy), tanh(t), 1e-6)
    eq("q4b identity", tanh(t) ** 4 + tanh(t) ** 2 / cosh(t) ** 2, tanh(t) ** 2, 1e-12)
L = simpson(lambda t: sqrt(((X(t + 1e-6) - X(t - 1e-6)) / 2e-6) ** 2 + ((Y(t + 1e-6) - Y(t - 1e-6)) / 2e-6) ** 2), 0, log(2), 2000)
eq("q4b length", L, log(5 / 4), 1e-6)
eq("q4b cosh ln2", cosh(log(2)), 5 / 4)

# ---- Q5 rectangles: bounds for sum 1/sqrt(r) ----
for n in (1, 2, 5, 40, 1000):
    s = sum(1 / sqrt(r) for r in range(1, n + 1))
    assert 2 * sqrt(n + 1) - 2 < s < 2 * sqrt(n) - 1 + 1e-12 or n == 1, n
assert 2 * sqrt(2) - 2 < 1 <= 2 * 1 - 1        # n = 1: lower bound below, upper bound attained (a strict inequality needs n >= 2)
eq("q5a int", simpson(lambda x: x ** -0.5, 1, 50), 2 * sqrt(50) - 2, 1e-8)
eq("q5b int", simpson(lambda x: x ** -0.5, 1, 51), 2 * sqrt(51) - 2, 1e-8)
S = sum(1 / sqrt(r) for r in range(1, 10001))
lo, hi = 2 * sqrt(10001) - 2, 2 * sqrt(10000) - 1
eq("q5c lo", round(lo, 2), 198.01); eq("q5c hi", hi, 199)
assert lo < S < hi and 198 < lo and hi < 199 + 1e-9 and 198 < S < 199

# ---- Q6 second order DE: x'' + 4x' + 13x = 30 e^{-t}, x(0) = x'(0) = 0 ----
x = lambda t: 3 * exp(-t) - exp(-2 * t) * (3 * cos(3 * t) + sin(3 * t))
eq("q6 x0", x(0), 0)
eq("q6 x'0", (x(1e-6) - x(-1e-6)) / 2e-6, 0, 1e-5)
for t in (0.0, 0.5, 1.7, 3.0):
    d1 = (x(t + 1e-5) - x(t - 1e-5)) / 2e-5
    d2 = (x(t + 1e-4) - 2 * x(t) + x(t - 1e-4)) / 1e-8
    eq("q6 ode", d2 + 4 * d1 + 13 * x(t), 30 * exp(-t), 1e-4)
assert 16 - 52 == -36 and (-4) / 2 == -2 and sqrt(36) / 2 == 3
assert 1 - 4 + 13 == 10 and 30 // 10 == 3
A_, B_ = -3, -1
assert A_ + 3 == 0 and -2 * A_ + 3 * B_ - 3 == 0

# ---- Q7 fifth roots of unity ----
rts = [complex(cos(2 * k * pi / 5), sin(2 * k * pi / 5)) for k in (0, 1, -1, 2, -2)]
for z in rts:
    eq("q7a root", abs(z ** 5 - 1), 0, 1e-12)
eq("q7b sum", abs(sum(rts)), 0, 1e-12)
eq("q7b", cos(2 * pi / 5) + cos(4 * pi / 5), -0.5, 1e-12)
c = cos(2 * pi / 5)
eq("q7c double", cos(4 * pi / 5), 2 * c * c - 1, 1e-12)
eq("q7c quad", 4 * c * c + 2 * c - 1, 0, 1e-12)
eq("q7c", c, (sqrt(5) - 1) / 4, 1e-12)
assert (-1 - sqrt(5)) / 4 < 0 < (-1 + sqrt(5)) / 4 and 2 * pi / 5 < pi / 2
assert 4 + 16 == 20 and sqrt(20) == 2 * sqrt(5)

# ---- Q8 matrices ----
A = [[1, 1, 1], [2, 0, 1], [-2, 2, 1]]
def mm(X_, Y_): return [[sum(X_[i][k] * Y_[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def mv(X_, v): return [sum(X_[i][k] * v[k] for k in range(3)) for i in range(3)]
def det3(M):
    a, b, c_ = M[0]; d, e_, f_ = M[1]; g, h_, i = M[2]
    return a * (e_ * i - f_ * h_) - b * (d * i - f_ * g) + c_ * (d * h_ - e_ * g)
def inv3(M):
    d = det3(M)
    cof = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[M[r][c_] for c_ in range(3) if c_ != j] for r in range(3) if r != i]
            cof[i][j] = (-1) ** (i + j) * (m[0][0] * m[1][1] - m[0][1] * m[1][0])
    return [[F(cof[j][i], d) for j in range(3)] for i in range(3)]
I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# (b) characteristic polynomial at several lambda
for lam in (-2, -1, 0, 0.5, 1, 2, 3):
    M = [[A[i][j] - (lam if i == j else 0) for j in range(3)] for i in range(3)]
    eq("q8b det", det3(M), (1 - lam) * (lam - 2) * (lam + 1), 1e-9)
    eq("q8b poly", -(lam ** 3 - 2 * lam ** 2 - lam + 2), (1 - lam) * (lam - 2) * (lam + 1), 1e-9)
    eq("q8b minor", (1 - lam) * (lam * lam - lam - 2) - (4 - 2 * lam) + (4 - 2 * lam), det3(M), 1e-9)
# (c) eigenvectors, P, D
vecs = {-1: [0, 1, -1], 1: [1, 1, -1], 2: [1, 1, 0]}
for lam, v in vecs.items():
    assert mv(A, v) == [lam * x_ for x_ in v], lam
P = [[0, 1, 1], [1, 1, 1], [-1, -1, 0]]
assert [[P[i][j] for i in range(3)] for j in range(3)] == [vecs[-1], vecs[1], vecs[2]]
A2 = mm(A, A)
B = [[A2[i][j] - 2 * A[i][j] for j in range(3)] for i in range(3)]
D = [[3, 0, 0], [0, -1, 0], [0, 0, 0]]
Pi = inv3(P)
PD = [[sum(P[i][k] * D[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
PDPi = [[sum(PD[i][k] * Pi[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert PDPi == [[F(x_) for x_ in r] for r in B], (PDPi, B)
for lam in (-1, 1, 2):
    assert lam * lam - 2 * lam == {-1: 3, 1: -1, 2: 0}[lam]
assert 4 - 4 == 0 and 1 + 2 == 3 and 1 - 2 == -1
# (d) Cayley-Hamilton and the inverse
A3 = mm(A2, A)
CH = [[A3[i][j] - 2 * A2[i][j] - A[i][j] + 2 * I3[i][j] for j in range(3)] for i in range(3)]
assert CH == [[0] * 3] * 3
Ainv = inv3(A)
rhs = [[F(-1, 2) * A2[i][j] + A[i][j] + F(1, 2) * I3[i][j] for j in range(3)] for i in range(3)]
assert Ainv == rhs, (Ainv, rhs)
assert det3(A) == -2 == (-1) * 1 * 2
print("ok")
