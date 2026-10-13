# checks/math.p1.quadratics.py: recomputes every number in the Quadratics chapter.
from fractions import Fraction as F
from math import sqrt, isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    if isinstance(want, (set, tuple, list)) or isinstance(got, (set, tuple, list)):
        g, w = sorted(got), sorted(want)
        same = len(g) == len(w) and all(a == b or (isinstance(a, (int, float, F)) and isclose(a, b, abs_tol=tol)) for a, b in zip(g, w))
        assert same, f"{label}: computed {got}, chapter says {want}"
    else:
        assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def roots(a, b, c):
    """Real roots of ax^2 + bx + c = 0 as exact Fractions when rational, else floats."""
    d = b * b - 4 * a * c
    r = sqrt(d)
    if r == int(r):
        return {F(-b + int(r), 2 * a), F(-b - int(r), 2 * a)}
    return {(-b + r) / (2 * a), (-b - r) / (2 * a)}

def f(a, b, c):
    return lambda x: a * x * x + b * x + c

def complete(a, b, c):
    """a x^2 + b x + c = a (x + p)^2 + q  ->  (p, q)"""
    p = F(b, 2 * a)
    return p, F(c) - a * p * p

# Worked examples
eq("eg solve x^2-5x+6", roots(1, -5, 6), {2, 3})
eq("eg check x=2", f(1, -5, 6)(2), 0)
eq("eg 2x^2+7x-4 ac", 2 * -4, -8)
eq("eg 2x^2+7x-4 split", (8 * -1, 8 + -1), (-8, 7))
eq("eg 2x^2+7x-4", roots(2, 7, -4), {F(1, 2), -4})
eq("eg x^2+6x+11 square", complete(1, 6, 11), (3, 2))
eq("eg 2x^2-12x+7 square", complete(2, -12, 7), (-3, -11))
eq("eg 2x^2-12x+7 check x=0", 2 * (0 - 3) ** 2 - 11, 7)
p, q = complete(1, 4, -1)
eq("eg x^2+4x-1 square", (p, q), (2, -5))
eq("eg x^2+4x-1 exact roots", roots(1, 4, -1), {-2 + sqrt(5), -2 - sqrt(5)})
eq("eg 3x^2-4x-2 discriminant", (-4) ** 2 - 4 * 3 * -2, 40)
eq("eg 3x^2-4x-2 3sf", {sf(x) for x in roots(3, -4, -2)}, {1.72, -0.387})
eq("eg equal roots k", {k for k in range(-20, 21) if k * k - 4 * 9 == 0}, {6, -6})
eq("eg line meets curve: k^2 > 16 boundary", {k for k in range(-20, 21) if k * k - 16 == 0}, {4, -4})
eq("eg 2x^2+5x-3 critical values", roots(2, 5, -3), {F(1, 2), -3})
eq("eg 2x^2+5x-3 <= 0 between roots", f(2, 5, -3)(-1) <= 0 and f(2, 5, -3)(1) > 0 and f(2, 5, -3)(-4) > 0, True)
eq("eg x^2+x-12", roots(1, 1, -12), {-4, 3})
eq("eg circle check (-4,-3)", (-4) ** 2 + (-3) ** 2, 25)
eq("eg circle check (3,4)", 3 ** 2 + 4 ** 2, 25)
eq("eg u^2-5u+4", roots(1, -5, 4), {1, 4})
eq("eg x^4-5x^2+4 solutions", {x for x in range(-5, 6) if x ** 4 - 5 * x ** 2 + 4 == 0}, {-2, -1, 1, 2})
eq("eg 2u^2-7u+3", roots(2, -7, 3), {F(1, 2), 3})
eq("eg 2x-7sqrt(x)+3 at x=1/4", 2 * 0.25 - 7 * sqrt(0.25) + 3, 0)
eq("eg 2x-7sqrt(x)+3 at x=9", 2 * 9 - 7 * 3 + 3, 0)

# Try it yourself
eq("try1", roots(1, 7, 10), {-2, -5})
eq("try2", roots(3, -10, -8), {F(-2, 3), 4})
eq("try3 square", complete(1, -8, 3), (-4, -13))
eq("try4 3sf", {sf(x) for x in roots(5, 2, -1)}, {0.290, -0.690})
eq("try5 boundary k^2 = 4", {k for k in range(-10, 11) if 16 - 4 * k * k == 0}, {2, -2})
eq("try6 critical values", roots(1, 2, -15), {-5, 3})
eq("try7 x values", roots(1, -6, 5), {1, 5})
eq("try7 points", {(x, 2 * x - 1) for x in (1, 5)}, {(1, 1), (5, 9)})
eq("try8a 4-(x-3)^2 at x=0", 4 - (0 - 3) ** 2, f(-1, 6, -5)(0))
eq("try8b max value", max(f(-1, 6, -5)(x / 100) for x in range(0, 601)), 4)
eq("try9 u values", roots(1, -6, 8), {2, 4})
eq("try9 x values", {u * u for u in (2, 4)}, {4, 16})

# Quiz
eq("quiz1 discriminant", 3 ** 2 - 4 * 2 * 5, -31)
eq("quiz2 square", complete(1, -10, 4), (-5, -21))
eq("quiz4 boundaries", roots(1, 0, -9), {-3, 3})

# v2: warm-up
eq("w1 expand", 1, 1);
for x in (-2, 0.5, 3, 7): eq("w1", (x - 3) ** 2 + 4, x * x - 6 * x + 13)
eq("w2 surd", sqrt(50) - sqrt(18), 2 * sqrt(2))
eq("w3 x-int", 2 * 3 - 6, 0)

# v2: proof of the formula, checked on random quadratics: complete-the-square line and the formula roots
import random
random.seed(5)
for _ in range(6):
    a, b, c = random.choice([-3, -2, -1, 1, 2, 3, 5]), random.randint(-9, 9), random.randint(-9, 5)
    D = b * b - 4 * a * c
    for x in (-1.7, 0.3, 2.9):
        eq("proof line1", (x + b / (2 * a)) ** 2 - b * b / (4 * a * a) + c / a, (a * x * x + b * x + c) / a, 1e-9)
        eq("proof line2", (x + b / (2 * a)) ** 2 - D / (4 * a * a), (a * x * x + b * x + c) / a, 1e-9)
    if D >= 0:
        for s in (1, -1):
            x = (-b + s * sqrt(D)) / (2 * a)
            eq("formula root", a * x * x + b * x + c, 0, 1e-9)
        # sum and product of roots
        r1, r2 = (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
        eq("sum", r1 + r2, -b / a, 1e-9); eq("prod", r1 * r2, c / a, 1e-9)
eq("sumprod 2,3", 2 + 3, 5); eq("sumprod prod", 2 * 3, 6)

# v2: spot the error
for x in (0, 1, -2, 3.5):
    eq("spot right", 3 * (x + 2) ** 2 - 7, 3 * x * x + 12 * x + 5, 1e-9)
eq("spot student", 3 * 4 + 1, 13); eq("spot check 0", 3 * 4 - 7, 5)

# v2: exam practice
eq("x1 r1", sf((-3 + sqrt(29)) / 2), 1.19); eq("x1 r2", sf((-3 - sqrt(29)) / 2), -4.19)
for x in (-3, 0, 1.5, 4): eq("x2", 2 * (x + 2) ** 2 + 3, 2 * x * x + 8 * x + 11)
eq("x2 min", 2 * 0 + 3, 3)
for x in (-3, 0, 1.5, 4): eq("x3 fact", (2 * x - 1) * (x - 4), 2 * x * x - 9 * x + 4)
# x3 solution set by scanning
for x in (-1, 0, 0.4, 0.6, 2, 4, 4.5, 10):
    assert (2 * x * x > 9 * x - 4) == (x < 0.5 or x > 4), x
# x4 tangent
k = -0.25
eq("x4 disc", 25 - 4 * (6 - k), 0); eq("x4 x", 5 / 2, 2.5); eq("x4 y", 2 * 2.5 + k, 19 / 4)
eq("x4 on curve", 2.5 ** 2 - 3 * 2.5 + 6, 19 / 4)
# x5
for x, y in ((4, 2), (-2, -4)):
    eq("x5 line", x - 2, y); eq("x5 circle", x * x + y * y, 20)
for x in (-2, 3, 5): eq("x5 quad", x * x + (x - 2) ** 2 - 20, 2 * (x * x - 2 * x - 8), 1e-9)
# x6
for k in (-3, 0, 2, 5): eq("x6 disc", (-2 * k) ** 2 - 4 * (3 * k * k + 1), -8 * k * k - 4)
# x7: rectangle
l, w = 12, 5
eq("x7 perim", 2 * (l + w), 34); eq("x7 diag", sqrt(l * l + w * w), 13)
for x in (0, 3, 9): eq("x7 quad", x * x + (17 - x) ** 2 - 169, 2 * (x * x - 17 * x + 60), 1e-9)
eq("x7 root5", 5 * 5 - 17 * 5 + 60, 0); eq("x7 root12", 12 * 12 - 17 * 12 + 60, 0)
for x in (0, 3, 8.5, 12): eq("x7 area", x * (17 - x), -(x - 8.5) ** 2 + 289 / 4, 1e-9)
eq("x7 max", 289 / 4, 72.25)
# x8
for x in (-1, 0, 3, 5): eq("x8 sq", 2 * (x - 3) ** 2 + 3, 2 * x * x - 12 * x + 21, 1e-9)
eq("x8 disc", 168, 4 * 2 * 21); eq("x8 m", sf(-12 + sqrt(168)), 0.961); eq("x8 m2", sf(-12 - sqrt(168)), -25.0)
eq("x8 exact", sqrt(168), 2 * sqrt(42))
for m in (-12 + sqrt(168), -12 - sqrt(168)):
    eq("x8 tangent disc", (12 + m) ** 2 - 168, 0, 1e-9)
# stretch 1: tangents from (0,-3) to y = x^2 + 1
for kk in (4, -4):
    eq("s1 disc", kk * kk - 16, 0); xt = kk / 2
    eq("s1 touch", xt * xt + 1, kk * xt - 3); eq("s1 y", xt * xt + 1, 5)
# stretch 2: number of real x for x^4 - 6x^2 + k = 0
def nx(k):
    xs = [i / 2000 for i in range(-6000, 6000)]
    v = [x ** 4 - 6 * x * x + k for x in xs]
    return sum(1 for i in range(len(v) - 1) if v[i] * v[i + 1] < 0)
for k, want in ((0.5, 4), (4, 4), (8.5, 4), (-1, 2), (9.5, 0), (10, 0)):
    assert nx(k) == want, (k, nx(k))
eq("s2 roots k=0", 3 - sqrt(9 - 0), 0); eq("s2 k=9", 3 - sqrt(0), 3)
# quiz additions
eq("quiz k", 4 ** 2 - 16, 0); eq("quiz k2", (-4) ** 2 - 16, 0)
for x in (-3, 0, 5): assert (x * x - 2 * x - 8 > 0) == (x < -2 or x > 4)
print(f"ok {n} checks")
