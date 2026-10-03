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

print(f"ok {n} checks")
