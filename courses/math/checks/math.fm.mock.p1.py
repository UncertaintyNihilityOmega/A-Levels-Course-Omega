# checks/math.fm.mock.p1.py: recomputes every number in Mock Paper 1 (Further Pure Mathematics 1).
# Standard library only: Fraction for exact work, complex arithmetic for the cubic, Simpson for integrals.
import re
import pathlib
from fractions import Fraction as F
from math import isclose, sqrt, pi, sin, cos, acos, degrees


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
        ans = b.split("\nA:", 1)[1]
        got = 0
        for grp in re.findall(r"\[([^\]\n]*)\]", ans):
            if TOKEN.match(grp):
                got += sum(int(d) for d in re.findall(r"(?:DM|M|A|B)(\d)", grp))
        assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
        # the part marks written in the question, e.g. [3] [4] [1], add up too
        qpart = b.split("\nA:", 1)[0]
        parts = [int(x) for x in re.findall(r"(?<!\w)\[(\d+)\](?!\()", qpart)]
        if parts:
            assert sum(parts) == n, f"question {i}: part marks {parts} do not add to {n}"
        grand += n
        spread.append(n)
    assert grand == total, f"paper total {grand}, should be {total}"
    assert len(blocks) == expect_qs, f"{len(blocks)} questions"
    return spread


spread = count_marks("chapters/math.fm.mock.p1.md", 75, 7)
assert spread == [8, 7, 7, 9, 13, 16, 15], spread        # the June 2025 9231/11 spread

# ---- Q1 series ----
for n in (1, 2, 5, 12):
    eq("q1a", sum((2 * r - 1) * (3 * r + 1) for r in range(1, n + 1)), n * (4 * n * n + 5 * n - 1) / 2)
assert (4, 5, -1) == (4, 5, -1) and 6 * F(1, 1) == 6
for n in (1, 2, 7, 30):
    s = sum(F(1, (r + 1) * (r + 3)) for r in range(1, n + 1))
    assert s == F(5, 12) - F(2 * n + 5, 2 * (n + 2) * (n + 3)), n
    assert F(1, (n + 1) * (n + 3)) == F(1, 2) * (F(1, n + 1) - F(1, n + 3))
eq("q1c", float(sum(F(1, (r + 1) * (r + 3)) for r in range(1, 20001))), 5 / 12, 1e-4)

# ---- Q2 roots of x^3 + 2x^2 - 5x + 7 (Durand-Kerner), sums of powers and the new cubic ----
def roots(c):
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


rt = roots([1, 2, -5, 7])
eq("q2 sum", sum(rt).real, -2, 1e-9); eq("q2 sumab", sum(rt[i] * rt[j] for i in range(3) for j in range(i + 1, 3)).real, -5, 1e-9)
eq("q2 prod", (rt[0] * rt[1] * rt[2]).real, -7, 1e-9)
eq("q2b", sum(x * x for x in rt).real, 14, 1e-9); eq("q2c", sum(x ** 3 for x in rt).real, -59, 1e-9)
assert (-2) ** 2 - 2 * (-5) == 14 and -2 * 14 + 5 * (-2) - 3 * 7 == -59
assert (-2) ** 3 - 3 * (-2) * (-5) + 3 * (-7) == -59
for y in [2 * x + 1 for x in rt]:
    eq("q2a root", abs(y ** 3 + y ** 2 - 25 * y + 79), 0, 1e-8)
# expansion of the multiplied-out substitution at several y
for y in (-3, 0, 1.5, 4):
    eq("q2a expand", (y - 1) ** 3 + 4 * (y - 1) ** 2 - 20 * (y - 1) + 56, y ** 3 + y ** 2 - 25 * y + 79)
    eq("q2a sub", 8 * (((y - 1) / 2) ** 3 + 2 * ((y - 1) / 2) ** 2 - 5 * (y - 1) / 2 + 7), (y - 1) ** 3 + 4 * (y - 1) ** 2 - 20 * (y - 1) + 56)

# ---- Q3 induction ----
u = [None, 1]
for n in range(1, 30):
    u.append(3 * u[n] + 2)
for n in range(1, 30):
    assert u[n] == 2 * 3 ** (n - 1) - 1, n
    assert (u[n + 1] - u[n]) == 4 * 3 ** (n - 1) and (u[n + 1] - u[n]) % 4 == 0
assert 3 * (2 * 3 ** 4 - 1) + 2 == 2 * 3 ** 5 - 1

# ---- Q4 matrix ----
M = [[4, -3], [2, -1]]
def mul(A, v): return [A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1]]
for x in (-2, 1, 7):
    assert mul(M, [x, x]) == [x, x]
det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
assert det == 2
Mi = [[F(M[1][1], det), F(-M[0][1], det)], [F(-M[1][0], det), F(M[0][0], det)]]
assert Mi == [[F(-1, 2), F(3, 2)], [F(-1), F(2)]]
P = [Mi[0][0] * 10 + Mi[0][1] * 6, Mi[1][0] * 10 + Mi[1][1] * 6]
assert P == [4, 2] and mul(M, [4, 2]) == [10, 6]
# invariant lines y = mx: 3m^2 - 5m + 2 = 0 has roots 1 and 2/3
for m in (F(1), F(2, 3)):
    assert 3 * m * m - 5 * m + 2 == 0
    x = 5
    img = mul(M, [x, m * x])
    assert img[1] == m * img[0]
assert 2 - F(2, 3) == F(2, 3) * (4 - 3 * F(2, 3))
# eigenvalues 1 and 2 (alternative method): trace 3, det 2; eigenvector (3, 2) for 2
assert mul(M, [3, 2]) == [6, 4]

# ---- Q5 polar ----
r1 = lambda t: 4 * sin(2 * t)
A1 = 0.5 * simpson(lambda t: r1(t) ** 2, 0, pi / 2)
eq("q5b", A1, 2 * pi, 1e-8)
eq("q5b formula", 4 * (pi / 2 - sin(4 * pi / 2) / 4), 2 * pi)
for t in (pi / 12, 5 * pi / 12):
    eq("q5c", r1(t), 2, 1e-12)
eq("q5 sin", sin(2 * pi / 12), 0.5)
A2 = 0.5 * simpson(lambda t: r1(t) ** 2 - 4, pi / 12, 5 * pi / 12)
eq("q5d", A2, 2 * pi / 3 + sqrt(3), 1e-8)
eq("q5d antiderivative", (2 * 5 * pi / 12 - sin(5 * pi / 3)) - (2 * pi / 12 - sin(pi / 3)), 2 * pi / 3 + sqrt(3), 1e-12)
for t in (0.3, 0.7, 1.1):
    eq("q5d identity", 16 * sin(2 * t) ** 2, 8 - 8 * cos(4 * t), 1e-12)
assert r1(pi / 4) == 4 and r1(0) == 0 and abs(r1(pi / 2)) < 1e-12
assert all(r1(t) > 2 for t in (0.3, 0.5, 0.8, 1.2)) and r1(0.2) < 2 and r1(1.4) < 2

# ---- Q6 planes ----
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
A, B, Cc = (1, 2, 0), (3, 0, 1), (-1, 0, 0)
AB, AC = sub(B, A), sub(Cc, A)
assert AB == (2, -2, 1) and AC == (-2, -2, 0)
n = cross(AB, AC)
assert n == (2, -2, -8)
n1 = (1, -1, -4)
assert dot(n1, A) == dot(n1, B) == dot(n1, Cc) == -1
n2 = (2, 1, -1)
assert dot(n1, n2) == 5 and dot(n1, n1) == 18 and dot(n2, n2) == 6
eq("q6b", round(degrees(acos(5 / sqrt(108))), 1), 61.2)
def dist(t):
    D = (t, -2, 2)
    CD = sub(D, Cc)
    nn = cross(AB, CD)
    assert nn == (-2, t - 3, 2 * t - 2)
    assert dot(nn, nn) == 5 * t * t - 14 * t + 17
    assert dot(AC, nn) == 10 - 2 * t
    return abs(dot(AC, nn)) / sqrt(dot(nn, nn))
eq("q6c t=2", dist(2), 2); eq("q6c t=-1", dist(-1), 2)
for t in (-1, 2):
    assert 16 * t * t - 16 * t - 32 == 0 and (t - 2) * (t + 1) == 0
assert 4 * (5 * 9 - 42 + 17) - (10 - 2 * 3) ** 2 == 16 * 9 - 16 * 3 - 32  # RHS - LHS of the equation at t = 3
# the shortest distance is not 2 for other t
assert abs(dist(0) - 2) > 1e-3 and abs(dist(3) - 2) > 1e-3

# ---- Q7 rational function ----
f = lambda x: x * (x + 3) / (x - 1)
for x in (-5, 0.3, 2, 6):
    eq("q7a division", f(x), x + 4 + 4 / (x - 1), 1e-12)
for x in (-1, 3):
    eq("q7b stationary", (f(x + 1e-6) - f(x - 1e-6)) / 2e-6, 0, 1e-6)
    eq("q7b dy/dx", 1 - 4 / (x - 1) ** 2, 0)
eq("q7b y(-1)", f(-1), 1); eq("q7b y(3)", f(3), 9)
for x in (-4, 0.5, 4):
    eq("q7b formula", 1 - 4 / (x - 1) ** 2, (x * x - 2 * x - 3) / (x - 1) ** 2, 1e-12)
# second derivative: maximum at -1, minimum at 3
assert 8 / (-1 - 1) ** 3 < 0 and 8 / (3 - 1) ** 3 > 0
eq("q7c zeros", f(-3), 0); eq("q7c zeros", f(0), 0)
# f takes no value strictly between 1 and 9
assert all(not (1 < f(x) < 9) for x in [i / 100 for i in range(-3000, 3000)] if abs(x - 1) > 1e-9)
# y^2 = f(x): defined where f >= 0
dom = [x for x in [i / 100 for i in range(-500, 800)] if abs(x - 1) > 1e-9 and f(x) >= 0]
assert all((-3 <= x <= 0) or x > 1 for x in dom) and any(-3 <= x <= 0 for x in dom)
eq("q7d (3,3)", sqrt(f(3)), 3); eq("q7d (-1,1)", sqrt(f(-1)), 1)
# inequality f(x) <= 2x
def holds(x): return f(x) <= 2 * x + 1e-12
for x in [i / 50 for i in range(-400, 800)]:
    if abs(x - 1) < 1e-9:
        continue
    assert holds(x) == ((0 <= x < 1) or x >= 5), x
    eq("q7e factorised", x * (x + 3) * (x - 1) - 2 * x * (x - 1) ** 2, x * (x - 1) * (5 - x), 1e-9)
print("ok")
