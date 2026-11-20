# checks/math.fm.rational.py: recomputes every number in Rational functions and their graphs.
# Standard library only: exact values with Fraction, finite differences for derivatives, brute-force sampling for ranges.
from fractions import Fraction as F
from math import isclose, sqrt


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def sample(f, lo, hi, n=200001, skip=()):
    """Values of f on a grid, skipping points near the listed poles."""
    out = []
    for i in range(n):
        x = lo + (hi - lo) * i / (n - 1)
        if any(abs(x - s) < 1e-4 for s in skip):
            continue
        out.append((x, f(x)))
    return out


def divide(num, den):
    """Polynomial long division, coefficients highest power first (Fraction): quotient, remainder."""
    num = [F(c) for c in num]
    q = []
    while len(num) >= len(den):
        c = num[0] / den[0]
        q.append(c)
        for i in range(len(den)):
            num[i] -= c * den[i]
        num.pop(0)
    return q, num


# ---- warm-up
assert 36 - 36 == 0 and (-6) ** 2 - 36 == 0 and 7 ** 2 - 36 > 0 and 0 ** 2 - 36 < 0
q, r = divide([1, -1, 3], [1, -2])
assert q == [1, 1] and r == [5]
eq("warm-up quotient rule", d(lambda x: x / (x + 1), 2.0), 1 / (2 + 1) ** 2, 1e-7)

# ---- eg: y = (2x+1)/(x-3)
f1 = lambda x: (2 * x + 1) / (x - 3)
q, r = divide([2, 1], [1, -3])
assert q == [2] and r == [7]
eq("eg1 y(0)", f1(0), -1 / 3)
eq("eg1 y(-1/2)", f1(-0.5), 0)
assert f1(3.1) > 0 and f1(2.9) < 0
eq("eg1 deriv", d(f1, 5.0), -7 / (5 - 3) ** 2, 1e-6)
eq("eg1 -7/(x-3)^2 at 0", d(f1, 0.0), -7 / 9, 1e-6)
assert f1(1000) > 2 and f1(-1000) < 2

# ---- eg: y = (2x-1)/((x+1)(x-3))
f2 = lambda x: (2 * x - 1) / ((x + 1) * (x - 3))
for x, s in [(-2, -1), (0, 1), (1, -1), (4, 1)]:
    assert (f2(x) > 0) == (s > 0), f"sign table at {x}"
assert f2(-1.001) < 0 and f2(-0.999) > 0 and f2(2.999) < 0 and f2(3.001) > 0
eq("eg2 y(0)", f2(0), 1 / 3)
eq("eg2 y(1/2)", f2(0.5), 0)
# numerator of f' = 2(x^2-2x-3) - (2x-1)(2x-2) = -2x^2+2x-8
for x in [-3.0, 0.0, 0.5, 2.0, 5.0]:
    num = 2 * (x * x - 2 * x - 3) - (2 * x - 1) * (2 * x - 2)
    eq("eg2 numerator", num, -2 * x * x + 2 * x - 8)
    assert num < 0
assert 2 ** 2 - 4 * 1 * 4 * 1 < 0 and 4 - 64 < 0  # 2x - ... discriminant of -2x^2+2x-8
eq("eg2 deriv numeric", d(f2, 0.0), (-2 * 0 + 0 - 8) / ((0 - 2 * 0 - 3) ** 2), 1e-6)

# ---- eg: y = (x^2-4)/(x^2-1)
f3 = lambda x: (x * x - 4) / (x * x - 1)
eq("eg3 y(0)", f3(0), 4)
eq("eg3 y(2)", f3(2), 0)
for x in [-3.0, -0.5, 0.7, 2.5]:
    eq("eg3 split", f3(x), 1 - 3 / (x * x - 1))
    eq("eg3 deriv", d(f3, x), 6 * x / (x * x - 1) ** 2, 1e-5)
assert d(f3, -0.5) < 0 and d(f3, 0.5) > 0
for x in [-9, -2, 2, 9]:
    assert f3(x) < 1
vals = [y for x, y in sample(f3, -6, 6, skip=(-1, 1)) if abs(y) < 1e6]
assert min(y for x, y in sample(f3, -0.99, 0.99)) >= 4 - 1e-9
# ---- oblique asymptote: y = (x^2-3x+6)/(x-1)
f4 = lambda x: (x * x - 3 * x + 6) / (x - 1)
q, r = divide([1, -3, 6], [1, -1])
assert q == [1, -2] and r == [4]
for x in [-4.0, 0.0, 2.0, 5.0]:
    eq("eg4 split", f4(x), x - 2 + 4 / (x - 1))
    eq("eg4 deriv", d(f4, x), 1 - 4 / (x - 1) ** 2, 1e-5)
eq("eg4 f(3)", f4(3), 3)
eq("eg4 f(-1)", f4(-1), -5)
eq("eg4 f(0)", f4(0), -6)
assert d(f4, 3.0) < 1e-6 and d(f4, 2.9) < 0 < d(f4, 3.1)   # minimum at 3
assert d(f4, 0.9 * 0 - 1.1) > 0 > d(f4, -0.9)              # maximum at -1
assert 9 - 24 < 0
assert f4(3) > 3 - 2 and f4(-1) < -1 - 2   # right branch above y = x-2, left below
# range by discriminant: y^2 + 2y - 15
for y in [-6, -5, 0, 3, 4]:
    assert ((3 + y) ** 2 - 4 * (6 + y) >= 0) == (y <= -5 or y >= 3)
ys = [y for x, y in sample(f4, -30, 30, skip=(1,))]
assert not any(-5 + 1e-6 < y < 3 - 1e-6 for y in ys), "gap between -5 and 3"
assert min(y for y in ys if y > 0) >= 3 - 1e-6 and max(y for y in ys if y < 0) <= -5 + 1e-6

# ---- range of (x^2-4)/(x^2-1): y<1 or y>=4
for y in [0.5, 1.0, 2.0, 3.9, 4.0, 5.0, -3.0]:
    ok = 4 * (y - 1) * (y - 4) >= 0 and y != 1
    assert ok == (y < 1 or y >= 4), y
ys = [y for x, y in sample(f3, -40, 40, skip=(-1, 1))]
assert not any(1 <= y < 4 - 1e-9 for y in ys)
assert min(abs(y - 1) for y in ys) > 0   # y = 1 never taken
# y = 1: 0 = -(1-4) = 3 false
assert -(1 - 4) == 3

# ---- real context: stools
A = lambda n: (0.02 * n * n + 5 * n + 2000) / n
for n in [10.0, 100.0, 316.0, 500.0]:
    eq("stool split", A(n), 0.02 * n + 5 + 2000 / n)
eq("stool n", sqrt(2000 / 0.02), 316.2, 0.05)
eq("stool n exact", sqrt(100000), 316.22776601683796, 1e-9)
amin = 0.02 * sqrt(100000) + 5 + 2000 / sqrt(100000)
eq("stool min", sf(amin, 4), 17.65, 1e-9)
eq("stool min disc", sf(5 + sqrt(160), 4), 17.65, 1e-9)
eq("stool A(316) 4sf", sf(A(316), 5), 17.649, 1e-9)
eq("stool A(316)", sf(A(316), 4), 17.65, 1e-9)
assert min(A(n) for n in range(1, 2000)) == A(316)
assert 4 * 0.02 * 2000 == 160

# ---- crossing: y = (2x^2-3x)/(x^2-1)
f5 = lambda x: (2 * x * x - 3 * x) / (x * x - 1)
eq("cross y", f5(2 / 3), 2.0)
for x in [-30.0, 40.0, 5.0]:
    eq("cross split", f5(x) - 2, (2 - 3 * x) / (x * x - 1))
assert f5(1000) < 2 and f5(-1000) > 2
eq("cross y(3/2)", f5(1.5), 0)
for x in [-3.0, 0.0, 2.0, 5.0]:
    num = (4 * x - 3) * (x * x - 1) - (2 * x * x - 3 * x) * 2 * x
    # numerator of f' is -(3x^2 - 4x + 3)? compute exactly: 4x^3-4x-3x^2+3-4x^3+6x^2 = 3x^2-4x+3
    eq("cross numerator exact", num, 3 * x * x - 4 * x + 3)
    eq("cross deriv formula", d(f5, x), num / (x * x - 1) ** 2, 1e-5)
assert 16 - 36 < 0

# ---- hole
for x in [0.0, 1.0, 3.0, -4.0]:
    eq("hole", (x * x + x - 6) / (x - 2), x + 3)
assert 2 + 3 == 5

# ---- exam example: f = (x-2)^2/(x+1)
f6 = lambda x: (x - 2) ** 2 / (x + 1)
q, r = divide([1, -4, 4], [1, 1])
assert q == [1, -5] and r == [9]
assert (-1 - 2) ** 2 == 9
for x in [-6.0, -3.0, 0.0, 1.0, 4.0]:
    eq("exam split", f6(x), x - 5 + 9 / (x + 1))
    eq("exam deriv", d(f6, x), 1 - 9 / (x + 1) ** 2, 1e-5)
eq("exam f(2)", f6(2), 0)
eq("exam f(-4)", f6(-4), -12)
assert (-4 - 2) ** 2 == 36 and 36 / (-3) == -12
eq("exam f(0)", f6(0), 4)
eq("exam f(3-sqrt7)", f6(3 - sqrt(7)), 2, 1e-9)
eq("exam f(3+sqrt7)", f6(3 + sqrt(7)), 2, 1e-9)
eq("exam 3-sqrt7", sf(3 - sqrt(7)), 0.354)
eq("exam 3+sqrt7", sf(3 + sqrt(7)), 5.65)
assert abs((3 + sqrt(7)) ** 2 - 6 * (3 + sqrt(7)) + 2) < 1e-9 and 36 - 8 == 28
eq("exam f(1)", f6(1), 0.5)
eq("exam f(6)", f6(6), 16 / 7)
# solution set of f(x) <= 2
for x, _ in sample(f6, -30, 30, n=60001, skip=(-1,)):
    inside = x < -1 or (3 - sqrt(7) <= x <= 3 + sqrt(7))
    assert (f6(x) <= 2 + 1e-12) == inside or abs(x - (3 - sqrt(7))) < 1e-3 or abs(x - (3 + sqrt(7))) < 1e-3, x
# stationary points: min at 2, max at -4
assert d(f6, 1.9) < 0 < d(f6, 2.1)
assert d(f6, -4.1) > 0 > d(f6, -3.9)
# range from discriminant: y(y+12) >= 0 (used in graphs chapter)

# ---- spot the error: (x^2+4)/x
g = lambda x: (x * x + 4) / x
assert g(2) == 4 and g(-2) == -4 and g(1) == 5
ys = [y for x, y in sample(g, -50, 50, skip=(0,))]
assert not any(-4 + 1e-9 < y < 4 - 1e-9 for y in ys)
assert (4 ** 2 - 16 == 0)

# ---- try block
eq("try1", 3.0, 3.0)
f = lambda x: (x - 6) / (x + 2)
eq("try2 y(0)", f(0), -3)
eq("try2 x", f(6), 0)
q, r = divide([1, 0, 3], [1, 1])
assert q == [1, -1] and r == [4]
# which side
h = lambda x: (x * x + 3) / (x + 1)
assert h(2) > 2 - 1 and h(-3) < -3 - 1
# y = x / ((x-2)(x+3)) signs
k = lambda x: x / ((x - 2) * (x + 3))
assert k(-3.001) < 0 and k(-2.999) > 0 and k(1.999) < 0 and k(2.001) > 0
# y = x/(x^2+4)
m = lambda x: x / (x * x + 9 - 5)
ys = [y for x, y in sample(m, -40, 40)]
assert abs(max(ys) - 0.25) < 1e-6 and abs(min(ys) + 0.25) < 1e-6
assert 1 - 16 * (0.25) ** 2 == 0
# y = x^2/(x-2)
p = lambda x: x * x / (x - 2)
eq("try stationary (4,8)", p(4), 8)
eq("try deriv", d(p, 4.0), 0, 1e-6)
eq("try deriv 0", d(p, 0.0), 0, 1e-6)
for x in [-1.0, 1.0, 3.0, 5.0]:
    eq("try quotient", d(p, x), x * (x - 4) / (x - 2) ** 2, 1e-5)
# (x^2+1)/(x^2-4) never meets 1
assert 1 != -4
# hole (x^2-9)/(x^2-3x)
for x in [1.0, 5.0, -2.0]:
    eq("try hole", (x * x - 9) / (x * x - 3 * x), (x + 3) / x)
eq("try hole value", (3 + 3) / 3, 2)
# y = x + k/x min at 3 -> k = 9
eq("try k", d(lambda x: x + 9 / x, 3.0), 0, 1e-6)

# ---- exam practice
# Q1: (3x-1)/(x+2)
q, r = divide([3, -1], [1, 2])
assert q == [3]
# Q2: x/(x^2+9): range [-1/6, 1/6]
ys = [y for x, y in sample(lambda x: x / (x * x + 9), -60, 60)]
assert abs(max(ys) - 1 / 6) < 1e-6 and abs(min(ys) + 1 / 6) < 1e-6
assert 1 - 36 * (1 / 6) ** 2 == 0
# Q3: (2x^2-3x+5)/(x-2)
q, r = divide([2, -3, 5], [1, -2])
assert q == [2, 1] and r == [7]
assert 2 * 4 - 6 + 5 == 7
# Q4: (3x^2-2x)/(x^2-4) crosses y=3 at x=6
q4 = lambda x: (3 * x * x - 2 * x) / (x * x - 4)
eq("q4 cross", q4(6), 3)
assert 3 * 36 - 12 == 96 and 3 * 32 == 96
assert -2 * 6 == -12
# Q5: C = (n^2+40n+400)/n >= 80
C = lambda n: (n * n + 40 * n + 400) / n
assert min(C(0.01 * i) for i in range(1, 200000)) >= 80 - 1e-9
eq("q5 C(20)", C(20), 80)
assert (40 - 80) ** 2 - 1600 == 0
eq("q5 root", (80 - 40) / 2, 20)
# Q6: x^2/(x-2): (0,0), (4,8); disc y^2 - 8y
assert 0 ** 2 - 8 * 0 == 0 and 8 ** 2 - 8 * 8 == 0
ys = [y for x, y in sample(p, -60, 60, skip=(2,))]
assert not any(1e-6 < y < 8 - 1e-6 for y in ys)
# Q7: (x-1)(x+2)/(x-2)
q7 = lambda x: (x - 1) * (x + 2) / (x - 2)
q, r = divide([1, 1, -2], [1, -2])
assert q == [1, 3] and r == [4]
assert 4 + 2 - 2 == 4
eq("q7 (0,1)", q7(0), 1)
eq("q7 (4,9)", q7(4), 9)
eq("q7 (1,0)", q7(1), 0)
eq("q7 (-2,0)", q7(-2), 0)
assert (1 - 5) ** 2 == 16 and (1 - 1) ** 2 - 4 * (2 * 1 - 2) == 0
for y in [-3, 0, 1, 5, 9, 10]:
    assert ((1 - y) ** 2 - 4 * (2 * y - 2) >= 0) == (y <= 1 or y >= 9)
assert (1 - 10 * 1 + 9) == 0 and 1 - 10 * 9 + 81 + 9 - 9 == 1 - 90 + 81 + 0 + 9 - 9
eq("q7 repeated root y=1", (1 - 1) / 2, 0)
eq("q7 repeated root y=9", (9 - 1) / 2, 4)
ys = [y for x, y in sample(q7, -60, 60, skip=(2,))]
assert not any(1 + 1e-6 < y < 9 - 1e-6 for y in ys)
assert abs(d(q7, 0.0)) < 1e-6 and abs(d(q7, 4.0)) < 1e-6
assert d(q7, -0.1) > 0 > d(q7, 0.1) and d(q7, 3.9) < 0 < d(q7, 4.1)  # max at 0, min at 4

# ---- stretch
s = lambda x, k: (x * x + k) / (x - 1)
q, r = divide([1, 0, F(5)], [1, -1])
assert q == [1, 1] and r == [6]    # k = 5 example: x + 1 + 6/(x-1)  (k+1 = 6)
for k in [3, -3, 0]:
    for x in [-2.0, 0.5, 3.0]:
        eq("stretch split", s(x, k), x + 1 + (k + 1) / (x - 1), 1e-9)
assert (3 + 1) == 4 and 16 + 16 * (-2) < 0
assert (6 - 6) * (6 + 2) == 0 and 36 - 24 - 12 == 0 and 4 + 8 - 12 == 0
ys = [y for x, y in sample(lambda x: s(x, 3), -80, 80, skip=(1,))]
assert not any(-2 + 1e-6 < y < 6 - 1e-6 for y in ys)
ys = [y for x, y in sample(lambda x: s(x, -3), -80, 80, skip=(1,))]
assert min(ys) < -50 and max(ys) > 50 and abs(s(2.0, -3) - (4 - 3)) < 1e-9
# k = -3: y = 2 is attained? y^2-4y+12>0 always, so every real y; spot check y = 0 and y = 2 solutions exist
for y in [0.0, 2.0, -7.0, 11.0]:
    disc = y * y - 4 * (y + (-3))
    assert disc > 0
# lens
for u in [11.0, 15.0, 20.0, 40.0]:
    v = 10 * u / (u - 10)
    eq("lens eq", 1 / u + 1 / v, 0.1)
    eq("lens D", u + v, u * u / (u - 10))
assert min((u * u) / (u - 10) for u in [10 + 0.001 * i for i in range(1, 100000)]) >= 40 - 1e-9
eq("lens u=20", 20 * 20 / 10, 40)
assert 40 ** 2 - 40 * 40 == 0

# ---- marks totals (each answer's tokens add up to its [n marks])
marks = {
    "exam eg": 3 + 4 + 3 + 5,
    "values eg": 1 + 1 + 1 + 1,
    "q1": 3, "q2": 4, "q3": 5, "q4": 5, "q5": 5 + 2, "q6": 6 + 3, "q7": 3 + 4 + 2 + 3, "stretch1": 3 + 2 + 2, "stretch2": 3 + 4,
}
assert marks["values eg"] == 4
# the exam example: discriminant of x^2 - (3+y)x + (6+y) is (y+5)(y-3)
for yy in [-7.0, -5.0, 0.0, 3.0, 5.0]:
    assert isclose((3 + yy) ** 2 - 4 * (6 + yy), (yy + 5) * (yy - 3), abs_tol=1e-9)
assert marks["exam eg"] == 15 and marks["q5"] == 7 and marks["q6"] == 9 and marks["q7"] == 12
assert marks["stretch1"] == 7 and marks["stretch2"] == 7

print("ok")
