# checks/math.fm.overview.py: recomputes every number in the chapter
from math import isclose, exp, factorial, floor
from statistics import NormalDist
from fractions import Fraction

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

# minutes per mark
eq("pure min per mark", 120 / 75, 1.6)
eq("applied min per mark", 90 / 50, 1.8)

# study hours per paper (the @time ranges of the chapters in course.json order)
times = {
    "FP1": [(6, 8), (5, 7), (6, 8), (5, 7), (5, 7), (6, 8), (4, 6), (6, 8), (6, 7), (6, 8)],
    "FP2": [(5, 7), (6, 8), (6, 8), (5, 6), (4, 5), (5, 6), (6, 8), (6, 7), (4, 6), (6, 8), (5, 6), (7, 9)],
    "FM": [(5, 6), (5, 6), (6, 7), (5, 6), (5, 6), (5, 6), (5, 6), (5, 6), (5, 6)],
    "FS": [(5, 6), (5, 6), (6, 8), (5, 7), (4, 6), (4, 5), (6, 7), (5, 6)],
}
want = {"FP1": (10, 55, 74, 9, 12), "FP2": (12, 65, 84, 11, 14), "FM": (9, 46, 55, 8, 9), "FS": (8, 40, 51, 7, 9)}
def rh(x):  # round half up
    return floor(x + 0.5)
tot_lo = tot_hi = 0
for k, v in times.items():
    n, lo, hi, wl, wh = want[k]
    assert len(v) == n, k
    slo = sum(a for a, b in v)
    shi = sum(b for a, b in v)
    eq(k + " lo", slo, lo)
    eq(k + " hi", shi, hi)
    eq(k + " weeks lo", rh(slo / 6), wl)
    eq(k + " weeks hi", rh(shi / 6), wh)
    tot_lo += slo
    tot_hi += shi
eq("all lo", tot_lo, 206)
eq("all hi", tot_hi, 264)
eq("all weeks lo", rh(tot_lo / 6), 34)
eq("all weeks hi", rh(tot_hi / 6), 44)
eq("chapters", sum(len(v) for v in times.values()), 39)
# the chapter says 38 topic chapters? count them
assert sum(len(v) for v in times.values()) == 39

# readiness quiz
import cmath
eq("arg(-1+i)", cmath.phase(complex(-1, 1)), 3 * cmath.pi / 4)
eq("a.b", 1 * 2 + 2 * -1 + 2 * 2, 4)
# integral of x e^{2x}: F = e^{2x}(2x-1)/4, F' = x e^{2x}
F = lambda x: exp(2 * x) * (2 * x - 1) / 4
h = 1e-6
for x in (0.3, 1.1, -0.7):
    eq("by parts", (F(x + h) - F(x - h)) / (2 * h), x * exp(2 * x), 1e-6)
# partial fractions 1/(r(r+2)) = (1/2)(1/r - 1/(r+2))
for r in (1, 2, 5, 7):
    eq("pf", Fraction(1, r * (r + 2)), Fraction(1, 2) * (Fraction(1, r) - Fraction(1, r + 2)))
# dy/dx = 2xy, y(0)=3 -> y = 3 e^{x^2}
y = lambda x: 3 * exp(x * x)
for x in (0.2, 0.9):
    eq("de", (y(x + h) - y(x - h)) / (2 * h), 2 * x * y(x), 1e-5)
eq("y0", y(0), 3)
# Poisson
lam = 3.2
p = lambda k: exp(-lam) * lam ** k / factorial(k)
eq("P(X=2)", round(p(2), 3), 0.209)
eq("P(X<=2)", round(p(0) + p(1) + p(2), 3), 0.380)
eq("P(X=1)", round(p(1), 3), 0.130)
eq("P(X=3)", round(p(3), 3), 0.223)
# momentum
eq("coalesce", 3 * 4 / (3 + 5), 1.5)
eq("wrong 2.4", 3 * 4 / 5, 2.4)
eq("wrong 0.75", 3 * 4 / 16, 0.75)
# normal critical
eq("z 0.975", round(NormalDist().inv_cdf(0.975), 3), 1.960)
eq("z 0.95", round(NormalDist().inv_cdf(0.95), 3), 1.645)
eq("z 0.99", round(NormalDist().inv_cdf(0.99), 3), 2.326)
print("ok")
