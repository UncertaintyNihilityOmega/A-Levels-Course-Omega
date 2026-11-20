# checks/math.fm.roots.py: recomputes every number in Roots of polynomial equations.
# Standard library only: exact relations with Fraction, numeric roots (Durand-Kerner) to confirm them.
from fractions import Fraction as F
from math import isclose, sqrt
from itertools import combinations


def eq(label, got, want, tol=1e-9):
    assert isclose(complex(got).real, complex(want).real, abs_tol=tol) and \
        isclose(complex(got).imag, complex(want).imag, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def roots(c, it=800):
    """All complex roots of the polynomial with coefficients c (highest power first)."""
    n = len(c) - 1
    c = [complex(x) / c[0] for x in c]
    z = [(0.4 + 0.9j) ** k for k in range(n)]
    for _ in range(it):
        new = []
        for i, zi in enumerate(z):
            p = sum(c[k] * zi ** (n - k) for k in range(n + 1))
            q = 1
            for j, zj in enumerate(z):
                if j != i:
                    q *= zi - zj
            new.append(zi - p / q)
        z = new
    return z


def esym(rs, k):
    """Sum of products of the roots taken k at a time."""
    s = 0
    for comb in combinations(rs, k):
        p = 1
        for r in comb:
            p *= r
        s += p
    return s


def rel(c):
    """Exact relations: e_k = (-1)^k c_k / c_0."""
    return [F((-1) ** k) * F(c[k]) / F(c[0]) for k in range(1, len(c))]


def check_rel(label, c):
    rs = roots(c)
    for k, e in enumerate(rel(c), start=1):
        eq(f"{label} e{k}", esym(rs, k), float(e), 1e-7)
    return rs


def S(rs, n):
    return sum(r ** n for r in rs)


def from_roots(rs):
    """Monic polynomial coefficients from roots (numeric)."""
    c = [1]
    for r in rs:
        c = [a - r * b for a, b in zip(c + [0], [0] + c)]
    return c


def same_poly(label, rs, c, tol=1e-6):
    m = from_roots(rs)
    for a, b in zip(m, c):
        eq(label, a * c[0], b, tol)


# Warm-up
assert 2 ** 3 - 3 * 2 ** 2 + 4 == 0
for z in (2 + 3j, 2 - 3j):
    eq("warm-up root", z * z - 4 * z + 13, 0)

# Quadratic 2x^2 - 5x + 7
s, p = rel([2, -5, 7])
assert (s, p) == (F(5, 2), F(7, 2))
assert 25 - 56 == -31
rs = check_rel("2x2-5x+7", [2, -5, 7])
assert s ** 2 - 2 * p == F(-3, 4)
eq("a2+b2", S(rs, 2), -0.75)
assert s / p == F(5, 7)
eq("1/a+1/b", sum(1 / r for r in rs), 5 / 7)
assert s ** 3 - 3 * p * s == F(125, 8) - F(210, 8) == F(-85, 8)
eq("a3+b3", S(rs, 3), -85 / 8)
# new quadratic with roots a^2, b^2: 4x^2 + 3x + 49
assert p ** 2 == F(49, 4)
same_poly("a^2 quadratic", [r * r for r in rs], [4, 3, 49])

# Cubic 2x^3 - 3x^2 + 4x - 5
assert rel([2, -3, 4, -5]) == [F(3, 2), 2, F(5, 2)]
check_rel("2x3", [2, -3, 4, -5])

# Exam eg: x^3 - 2x^2 + 4x + 3
c = [1, -2, 4, 3]
rs = check_rel("x3-2x2+4x+3", c)
e1, e2, e3 = rel(c)
assert (e1, e2, e3) == (2, 4, -3)
S2 = e1 ** 2 - 2 * e2
assert S2 == -4
eq("S2", S(rs, 2), -4)
assert e2 / e3 == F(-4, 3)
eq("sum 1/a", sum(1 / r for r in rs), -4 / 3)
S3 = 2 * S2 - 4 * e1 - 3 * 3
assert S3 == -25 == e1 ** 3 - 3 * e1 * e2 + 3 * e3 == 8 - 24 - 9
eq("S3", S(rs, 3), -25)
assert sum(1 for r in rs if abs(r.imag) < 1e-9) == 1   # one real root, two complex

# S_{-1} from the relation with n = -1 for x^3 - 2x^2 + 4x + 3
assert -(1 * S2 + (-2) * e1 + 4 * 3) / F(3) == F(-4, 3)

# Harder symmetric functions: x^3 + 3x^2 - x + 2
c = [1, 3, -1, 2]
rs = check_rel("harder", c)
s1, s2, s3 = rel(c)
assert (s1, s2, s3) == (-3, -1, -2)
assert s2 ** 2 - 2 * s3 * s1 == -11 == 1 - 12
eq("sum a2b2", sum((rs[i] * rs[j]) ** 2 for i, j in ((0, 1), (1, 2), (0, 2))), -11)
assert F(-11) / s3 ** 2 == F(-11, 4)
eq("sum 1/a^2", sum(1 / r ** 2 for r in rs), -11 / 4)
eq("product of pair sums", (rs[0] + rs[1]) * (rs[1] + rs[2]) * (rs[2] + rs[0]), 5)
assert -27 + 27 + 3 + 2 == 5
same_poly("pair-sum cubic", [rs[1] + rs[2], rs[2] + rs[0], rs[0] + rs[1]], [1, 6, 8, -5])
for y in (0.5, -2.0):
    a = -(y + 3) ** 3 + 3 * (y + 3) ** 2 + (y + 3) + 2
    b = -(y**3 + 9*y**2 + 27*y + 27) + (3*y**2 + 18*y + 27) + y + 3 + 2
    eq("pair-sum expansion", a, b); eq("pair-sum simplified", a, -y**3 - 6*y**2 - 8*y + 5)
rs = roots([1, -4, 2, 5])
eq("try pair sums", (rs[0] + rs[1]) * (rs[1] + rs[2]) * (rs[2] + rs[0]), 13)
assert 64 - 64 + 8 + 5 == 13

# AP: x^3 - 9x^2 + kx - 24, k = 26, roots 2, 3, 4
assert 27 - 81 + 3 * 26 - 24 == 0
same_poly("AP cubic", [2, 3, 4], [1, -9, 26, -24])
assert [1, -6, 8] == [1, -(2 + 4), 2 * 4]

# Complex root 1 + 2i: x^3 + x + 10
assert (1 + 2j) * (1 - 2j) == 5
same_poly("complex cubic", [1 + 2j, 1 - 2j, -2], [1, 0, 1, 10])
assert 5 + (-2) * 2 == 1 and (-2) ** 3 + (-2) + 10 == 0

# Plot y = x^3 + x + 10: only real root -2; range check
assert -27 - 3 + 10 == -20 and -22 < -20
assert 2.5 ** 3 + 2.5 + 10 < 32

# Widget cubic: local extreme values +-0.385, so three real roots only for |k| < 0.385
xm = 2 - 1 / sqrt(3)
eq("widget local max", xm ** 3 - 6 * xm ** 2 + 11 * xm - 6, 0.3849, 1e-4)
for k in (0.3, -1.0):
    eq("widget sum stays 6", sum(roots([1, -6, 11, -6 + k])), 6, 1e-7)

# Container: x^3 - 9x^2 + 23x - 14
c = [1, -9, 23, -14]
rs = check_rel("container", c)
assert all(abs(r.imag) < 1e-9 and r.real > 0 for r in rs)
real = sorted(r.real for r in rs)
assert [sf(r) for r in real] == [0.885, 3.25, 4.86]
assert 4 * 9 == 36 and 2 * 23 == 46 and 81 - 46 == 35
eq("diagonal", sf(sqrt(35)), 5.92)
eq("diagonal from roots", sqrt(sum(r * r for r in real)), sqrt(35))
for t in (1, 2, 7, 14):   # no rational roots
    assert t ** 3 - 9 * t * t + 23 * t - 14 != 0

# Quartic 3x^4 - 2x^3 + 0x^2 + 5x - 6
c = [3, -2, 0, 5, -6]
rs = check_rel("3x4", c)
assert rel(c) == [F(2, 3), 0, F(-5, 3), -2]
eq("quartic S2", S(rs, 2), 4 / 9)

# Exam eg quartic x^4 + 2x^3 + 3x^2 - x + 6
c = [1, 2, 3, -1, 6]
rs = check_rel("quartic exam", c)
assert rel(c) == [-2, 3, 1, 6]
eq("S2 = -2", S(rs, 2), -2)
eq("sum 1/a", sum(1 / r for r in rs), 1 / 6)
assert all(abs(r.imag) > 0.1 for r in rs)        # all four non-real
q = lambda x: x ** 4 + 2 * x ** 3 + 3 * x ** 2 - x + 6
mn = min(q(i / 1000) for i in range(-2500, 1501))
eq("quartic least value", sf(mn), 5.92)
assert q(-1.5) < 65 and q(2) < 65 and abs(q(0.144) - 5.92) < 0.005

# Substitution 2alpha: x^3 - 4x^2 + x + 6 -> y^3 - 8y^2 + 4y + 48
rs = roots([1, -4, 1, 6])
same_poly("2 alpha", [2 * r for r in rs], [1, -8, 4, 48])

# Squares: x^3 + 2x^2 - 3x + 5 -> y^3 - 10y^2 - 11y - 25; sum alpha^4 = 122
rs = roots([1, 2, -3, 5])
same_poly("squares", [r * r for r in rs], [1, -10, -11, -25])
assert 10 ** 2 - 2 * (-11) == 122
eq("S4", S(rs, 4), 122, 1e-6)
assert (-2) ** 2 - 2 * (-3) == 10

# Exam substitution: x^3 - 3x^2 + 5x - 2, y = 2x + 1 -> y^3 - 9y^2 + 35y - 43
rs = roots([1, -3, 5, -2])
ys = [2 * r + 1 for r in rs]
same_poly("2a+1", ys, [1, -9, 35, -43])
assert 81 - 70 == 11
eq("sum y^2", S(ys, 2), 11, 1e-7)
eq("sum 1/y", sum(1 / y for y in ys), 35 / 43, 1e-9)
# expansion line: (y-1)^3 - 6(y-1)^2 + 20(y-1) - 16 at a test value
for y in (0.3, 2.0, -1.7):
    lhs = (y - 1) ** 3 - 6 * (y - 1) ** 2 + 20 * (y - 1) - 16
    eq("expansion", lhs, y ** 3 - 9 * y ** 2 + 35 * y - 43)
    mid = y**3 - 3*y**2 + 3*y - 1 - 6*y**2 + 12*y - 6 + 20*y - 20 - 16
    eq("expanded line", mid, lhs)

# Spot the error: 2x^3 + 3x^2 - 4x + 1
c = [2, 3, -4, 1]
rs = check_rel("spot", c)
assert rel(c) == [F(-3, 2), -2, F(-1, 2)]
assert F(9, 4) + 4 == F(25, 4)
eq("spot S2", S(rs, 2), 6.25)
assert F(-2) / F(-1, 2) == 4 and F(-2) / F(1, 2) == -4
eq("spot 1/a", sum(1 / r for r in rs), 4)
same_poly("reciprocal check", [1 / r for r in rs], [1, -4, 3, 2])

# Try block
c = [1, 6, -2]; rs = check_rel("t1", c); eq("t1 S2", S(rs, 2), 40)
c = [3, -1, 4]; rs = check_rel("t2", c)
eq("t2 1/a", sum(1 / r for r in rs), 0.25)
assert F(1, 9) - F(8, 3) == F(-23, 9) and F(-23, 9) / F(4, 3) == F(-23, 12)
eq("t2 a/b+b/a", rs[0] / rs[1] + rs[1] / rs[0], -23 / 12)
rs = roots([1, -5, 3]); same_poly("t3", [r + 2 for r in rs], [1, -9, 17])
assert 3 + 10 + 4 == 17
c = [4, -8, 1, 3]; rs = check_rel("t4", c)
assert rel(c) == [2, F(1, 4), F(-3, 4)]; eq("t4 S2", S(rs, 2), 3.5)
c = [1, 4, -2, 7]; rs = check_rel("t5", c)
eq("t5 1/a", sum(1 / r for r in rs), 2 / 7); eq("t5 S2", S(rs, 2), 20)
c = [2, 3, -1, 5, -4]; rs = check_rel("t6", c)
assert rel(c) == [F(-3, 2), F(-1, 2), F(-5, 2), -2]; eq("t6 S2", S(rs, 2), 13 / 4)
rs = roots([1, -2, 1, -5]); same_poly("t7", [3 * r for r in rs], [1, -6, 9, -135])
rs = roots([1, 2, -7, 3]); same_poly("t8", [1 / r for r in rs], [1, -F(7, 3), F(2, 3), F(1, 3)])
assert 8 - 28 + 2 * 14 - 8 == 0
same_poly("t9", [1, 2, 4], [1, -7, 14, -8])

# Exam practice
c = [2, 3, -6]; rs = check_rel("E1", c); eq("E1", S(rs, 2), 33 / 4)
c = [1, -5, 2, 4]; rs = check_rel("E2", c); eq("E2 S2", S(rs, 2), 21); eq("E2 1/a", sum(1 / r for r in rs), -0.5)
c = [1, -3, 2, 1, -4]; rs = check_rel("E3", c)
assert rel(c) == [3, 2, -1, -4]
eq("E3 S2", S(rs, 2), 5); eq("E3 1/a", sum(1 / r for r in rs), 0.25)
c = [1, -2, 4, 3, 1]; rs = check_rel("E4", c); eq("E4 S2", S(rs, 2), -4)
same_poly("E5", [1, 2, 3], [1, -6, 11, -6]); assert 27 - 54 + 33 - 6 == 0
rs = roots([1, -1, 3, 2]); same_poly("E6 squares", [r * r for r in rs], [1, 5, 13, -4])
eq("E6 S4", S(rs, 4), -1, 1e-6); assert 25 - 26 == -1
same_poly("E7", [-3 + 2j, -3 - 2j, -2], [1, 8, 25, 26])
assert 13 * -2 == -26 and 13 + (-2) * (-6) == 25 and 64 - 50 == 14
eq("E7 S2", S([-3 + 2j, -3 - 2j, -2], 2), 14)
rs = roots([1, 3, -2, -1]); ys = [1 / (r + 1) for r in rs]
same_poly("E8", ys, [3, -5, 0, 1])
for y in (0.4, -1.3, 2.2):   # expansion line
    a = (1 - y) ** 3 + 3 * y * (1 - y) ** 2 - 2 * y * y * (1 - y) - y ** 3
    b = 1 - 3*y + 3*y**2 - y**3 + 3*y - 6*y**2 + 3*y**3 - 2*y**2 + 2*y**3 - y**3
    eq("E8 expansion", a, b); eq("E8 simplified", a, 3 * y ** 3 - 5 * y ** 2 + 1)
eq("E8 sum", sum(ys), 5 / 3); eq("E8 S2", S(ys, 2), 25 / 9)
assert F(125, 9) - 3 == F(98, 9) and F(98, 9) / 3 == F(98, 27)
eq("E8 S3", S(ys, 3), 98 / 27, 1e-7)

# Stretch: GP roots => b^3 = a^3 c (numeric test), repeated roots k = +-2
for al, r in ((2.0, 3.0), (-1.5, 0.5)):
    rr = [al / r, al, al * r]
    m = from_roots(rr)
    a, b, cc = m[1], m[2], m[3]
    eq("GP b^3 = a^3 c", b ** 3, a ** 3 * cc, 1e-6)
same_poly("k=2", [1, 1, -2], [1, 0, -3, 2])
same_poly("k=-2", [-1, -1, 2], [1, 0, -3, -2])

# Quiz
assert rel([3, -6, 1, -4])[0] == 2
assert rel([2, 5, -1, 8])[2] == -4
assert 9 - 10 == -1
assert rel([1, 0, -3, 0, 7])[3] == 7

# Marks totals of the exam-style answers (also counted by the kit)
assert 3 + 4 + 4 + 3 + 5 + 5 + 8 + 9 == 41
print("ok")
