# checks/math.fm.chisq.py: recomputes every number in "Chi-squared goodness of fit".
# Standard library only: chi-squared percentage points by Simpson integration of the density (substitution x = u^2
# removes the singularity at 0) and bisection.
from math import isclose, sqrt, lgamma, exp, comb, factorial
from statistics import NormalDist
from functools import lru_cache

N01 = NormalDist()


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def rd(x, d):
    return round(x + 0.0, d)


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def chi2_cdf(x, v, n=2000):
    # P(X <= x) for chi-squared with v degrees of freedom: integrate in u = sqrt(t), g(u) = 2 u^(v-1) e^(-u^2/2) / (2^(v/2) Gamma(v/2))
    if x <= 0:
        return 0.0
    top = sqrt(x)
    c = 2 / (2 ** (v / 2) * exp(lgamma(v / 2)))
    g = lambda u: c * u ** (v - 1) * exp(-u * u / 2)
    h = top / n
    s = g(0) + g(top) + sum((4 if i % 2 else 2) * g(i * h) for i in range(1, n))
    return s * h / 3


@lru_cache(None)
def chi2_inv(p, v):
    lo, hi = 0.0, 300.0
    for _ in range(70):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if chi2_cdf(mid, v) < p else (lo, mid)
    return (lo + hi) / 2


def CV(p, v):
    return round(chi2_inv(p, v), 3)


def X2(o, e):
    return sum((a - b) ** 2 / b for a, b in zip(o, e))


def contrib(o, e):
    return [(a - b) ** 2 / b for a, b in zip(o, e)]


# ---- the MF19 table (printed values) and the table in the chapter ----
mf19 = {1: {0.95: 3.841, 0.99: 6.635}, 2: {0.95: 5.991, 0.99: 9.210}, 3: {0.95: 7.815, 0.99: 11.345, 0.9: 6.251},
        4: {0.95: 9.488, 0.99: 13.277}, 5: {0.95: 11.070, 0.99: 15.086}, 6: {0.95: 12.592, 0.99: 16.812},
        7: {0.95: 14.067, 0.99: 18.475}, 8: {0.95: 15.507, 0.99: 20.090}}
for v, row in mf19.items():
    for p, want in row.items():
        eq(f"table nu={v} p={p}", CV(p, v), want, 5e-4)
for (v, p), want in {(1, 0.9): 2.706, (2, 0.9): 4.605, (10, 0.95): 18.307, (25, 0.95): 37.652}.items():
    eq(f"extra table nu={v} p={p}", CV(p, v), want, 5e-4)
eq("crit 0.9 nu 3", CV(0.9, 3), 6.251, 5e-4)
eq("1.96^2", 1.96 ** 2, 3.8416, 1e-4)
eq("z crit squared", N01.inv_cdf(0.975) ** 2, CV(0.95, 1), 2e-3)
eq("E(0.3) contribution", (1 - 0.3) ** 2 / 0.3, 1.63, 5e-3)

# ---- warm-up ----
eq("w1", comb(5, 2) * 0.2 ** 2 * 0.8 ** 3, 0.2048)
eq("w2", exp(-2.2) * 2.2 ** 3 / 6, 0.1966, 5e-5)
eq("w3", N01.cdf(-1.5), 0.0668, 5e-5)

# ---- the die ----
o = [15, 25, 22, 18, 24, 16]
assert sum(o) == 120
e = [20] * 6
eq("die x2", X2(o, e), 4.5)
eq("die sumO2/E - N", sum(a * a for a in o) / 20 - 120, 4.5)
assert sum(a * a for a in o) == 2490 and sum(a * a for a in o) / 20 == 124.5
assert [(a - 20) ** 2 for a in o] == [25, 25, 4, 4, 16, 16]
assert 4.5 < CV(0.95, 5)

# ---- ratio 9:3:3:1 ----
o = [160, 84, 52, 24]
assert sum(o) == 320
e = [320 * w / 16 for w in (9, 3, 3, 1)]
assert e == [180, 60, 60, 20]
for got, want in zip(contrib(o, e), [2.222, 9.600, 1.067, 0.800]):
    eq("ratio contrib", got, want, 5e-4)
eq("ratio x2", X2(o, e), 13.69, 5e-3)
assert 13.69 > CV(0.95, 3) and 13.69 > CV(0.99, 3)
assert 9.6 / X2(o, e) > 2 / 3

# ---- binomial, p given ----
pm = [comb(5, k) * 0.2 ** k * 0.8 ** (5 - k) for k in range(6)]
e = [200 * p for p in pm]
for got, want in zip(e, [65.536, 81.92, 40.96, 10.24, 1.28, 0.064]):
    eq("binG E", got, want, 1e-9)
eq("binG 3+", sum(e[3:]), 11.584)
oc = [60, 88, 40, 12]
assert sum(oc) == 200 and 10 + 2 + 0 == 12 and 60 + 88 + 40 + 10 + 2 == 200
ec = e[:3] + [sum(e[3:])]
for got, want in zip(contrib(oc, ec), [0.4676, 0.4512, 0.0225, 0.0149]):
    eq("binG contrib", got, want, 5e-5)
eq("binG x2", X2(oc, ec), 0.956, 5e-4)

# ---- Exam style: binomial, p estimated ----
o = [55, 62, 41, 26, 10, 5, 1]
n = sum(o)
assert n == 200
sxf = sum(i * f for i, f in enumerate(o))
assert sxf == 293
mean = sxf / n
eq("binA mean", mean, 1.465)
ph = mean / 6
eq("binA p", ph, 0.2442, 5e-5)
eq("binA p 3sf", sf(ph), 0.244)
e = [n * comb(6, k) * ph ** k * (1 - ph) ** (6 - k) for k in range(7)]
for got, want in zip(e, [37.29, 72.28, 58.37, 25.14, 6.09, 0.79, 0.04]):
    eq("binA E", got, want, 5e-3)
eq("binA sum 2dp", 37.29 + 72.28 + 58.37 + 25.14 + 6.09 + 0.79 + 0.04, 200.00, 1e-9)
eq("binA E2 workings", 200 * 15 * (1.465 / 6) ** 2 * (1 - 1.465 / 6) ** 4, 58.37, 6e-3)
eq("binA E2 with rounded p", 200 * 15 * 0.2442 ** 2 * 0.7558 ** 4, 58.38, 6e-3)
oc = o[:4] + [sum(o[4:])]
ec = e[:4] + [sum(e[4:])]
assert oc[-1] == 16
eq("binA comb E", ec[-1], 6.92, 5e-3)
assert e[4] > 5 and e[5] < 5 and e[6] < 5 and e[5] + e[6] + e[4] > 5
eq("binA comb E (rounded)", 6.09 + 0.79 + 0.04, 6.92, 1e-9)
for got, want in zip(contrib(oc, ec), [8.41, 1.46, 5.17, 0.03, 11.91]):
    eq("binA contrib", got, want, 6e-3)
eq("binA x2", sf(X2(oc, ec)), 27.0)
assert 8.41 + 1.46 + 5.17 + 0.03 + 11.91 == 26.98
assert X2(oc, ec) > CV(0.95, 3) == 7.815
assert o[0] > e[0] and sum(o[4:]) > sum(e[4:])
eq("binA x2 from rounded", X2(oc, [37.29, 72.28, 58.37, 25.14, 6.92]), 27.0, 0.05)

# ---- Exam style: Poisson ----
o = [20, 22, 20, 14, 10, 8, 6]
n = sum(o)
assert n == 100
assert [i * f for i, f in enumerate(o)] == [0, 22, 40, 42, 40, 40, 36] and sum(i * f for i, f in enumerate(o)) == 220
lam = 2.2
eq("po mean", sum(i * f for i, f in enumerate(o)) / n, lam)
pp = [exp(-lam) * lam ** k / factorial(k) for k in range(6)]
e = [n * p for p in pp] + [n * (1 - sum(pp))]
for got, want in zip(e, [11.08, 24.38, 26.81, 19.66, 10.82, 4.76, 2.49]):
    eq("po E", got, want, 6e-3)
oc = o[:5] + [o[5] + o[6]]
ec = e[:5] + [e[5] + e[6]]
assert oc[-1] == 14
eq("po comb E", ec[-1], 7.25, 5e-3)
eq("po comb E rounded", 4.76 + 2.49, 7.25, 1e-9)
for got, want in zip(contrib(oc, ec), [7.18, 0.23, 1.73, 1.63, 0.06, 6.29]):
    eq("po contrib", got, want, 6e-3)
eq("po x2", sf(X2(oc, ec)), 17.1)
eq("po x2 sum", 7.18 + 0.23 + 1.73 + 1.63 + 0.06 + 6.29, 17.12, 1e-9)
assert X2(oc, ec) > CV(0.95, 4) == 9.488
eq("po var", sum(i * i * f for i, f in enumerate(o)) / n - lam ** 2, 3.2)
assert sum(i * i * f for i, f in enumerate(o)) == 804 and 0 + 22 + 80 + 126 + 160 + 200 + 216 == 804
eq("po 8.04-4.84", 8.04 - 4.84, 3.2)
assert 7.18 / 17.12 > 0.4 and 6.29 / 17.12 > 0.3

# ---- geometric, p estimated ----
o = [41, 22, 14, 11, 5, 7]
assert sum(o) == 100
mean = 260 / 100
p = 1 / mean
eq("geo p", p, 5 / 13, 1e-12)
eq("geo p 4dp", p, 0.3846, 5e-5)
q = 1 - p
e = [100 * q ** (r - 1) * p for r in range(1, 6)] + [100 * q ** 5]
eq("geo sumE", sum(e), 100, 1e-9)
for got, want in zip(e, [38.46, 23.67, 14.57, 8.96, 5.52, 8.83]):
    eq("geo E", got, want, 6e-3)
assert min(e) >= 5
for got, want in zip(contrib(o, e), [0.168, 0.118, 0.022, 0.463, 0.048, 0.378]):
    eq("geo contrib", got, want, 6e-4)
eq("geo x2", X2(o, e), 1.196, 5e-4)
eq("geo x2 3sf", sf(X2(o, e)), 1.20)
assert X2(o, e) < CV(0.95, 4)

# ---- normal, parameters given ----
bounds = [244, 248, 252, 256]
z = [(b - 250) / 4 for b in bounds]
assert z == [-1.5, -0.5, 0.5, 1.5]
cdf = [N01.cdf(a) for a in z]
for got, want in zip(cdf, [0.0668, 0.3085, 0.6915, 0.9332]):
    eq("norm cdf", got, want, 5e-5)
pr = [cdf[0], cdf[1] - cdf[0], cdf[2] - cdf[1], cdf[3] - cdf[2], 1 - cdf[3]]
for got, want in zip(pr, [0.0668, 0.2417, 0.3829, 0.2417, 0.0668]):
    eq("norm P", got, want, 6e-5)
eq("norm P rounded", 0.3085 - 0.0668, 0.2417, 1e-9)
e = [200 * a for a in pr]
for got, want in zip(e, [13.36, 48.35, 76.58, 48.35, 13.36]):
    eq("norm E", got, want, 6e-3)
o = [18, 45, 70, 52, 15]
assert sum(o) == 200
for got, want in zip(contrib(o, e), [1.610, 0.232, 0.566, 0.276, 0.201]):
    eq("norm contrib", got, want, 6e-4)
eq("norm x2", X2(o, e), 2.885, 5e-4)
eq("norm x2 3sf", sf(X2(o, e)), 2.89)
assert X2(o, e) < CV(0.95, 4)

# ---- continuous PDF x/8 ----
def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n))
    return s * h / 3


eq("pdf total", simpson(lambda x: x / 8, 0, 4), 1, 1e-12)
pr = [(b * b - a * a) / 16 for a, b in [(0, 1), (1, 2), (2, 3), (3, 4)]]
eq("pdf P1", pr[0], 1 / 16)
eq("pdf P3", simpson(lambda x: x / 8, 2, 3), 5 / 16, 1e-12)
e = [160 * a for a in pr]
assert [round(a, 9) for a in e] == [10, 30, 50, 70]
o = [14, 26, 55, 65]
assert sum(o) == 160
for got, want in zip(contrib(o, e), [1.600, 0.533, 0.500, 0.357]):
    eq("pdf contrib", got, want, 6e-4)
eq("pdf x2", X2(o, e), 2.99, 5e-3)
assert X2(o, e) < CV(0.95, 3)

# ---- Exam style: PMF kr ----
k = 1 / (1 + 2 + 3 + 4)
eq("pmf k", k, 0.1)
o = [22, 27, 41, 60]
assert sum(o) == 150
e = [150 * k * r for r in range(1, 5)]
assert [round(a, 9) for a in e] == [15, 30, 45, 60]
for got, want in zip(contrib(o, e), [3.267, 0.300, 0.356, 0.0]):
    eq("pmf contrib", got, want, 6e-4)
eq("pmf x2", X2(o, e), 3.92, 5e-3)
eq("pmf cv", CV(0.9, 3), 6.251, 5e-4)
assert X2(o, e) < CV(0.9, 3)

# ---- Spot the error ----
o = [29, 43, 28, 17, 3]
n = sum(o)
assert n == 120
sxf = sum(i * f for i, f in enumerate(o))
assert sxf == 43 + 56 + 51 + 12 == 162
mean = sxf / n
eq("spot mean", mean, 1.35)
ph = mean / 4
eq("spot p", ph, 0.3375)
e = [n * comb(4, k) * ph ** k * (1 - ph) ** (4 - k) for k in range(5)]
for got, want in zip(e, [23.12, 47.11, 36.00, 12.23, 1.56]):
    eq("spot E", got, want, 6e-3)
oc = o[:3] + [o[3] + o[4]]
ec = e[:3] + [e[3] + e[4]]
assert oc[-1] == 20
eq("spot comb E", ec[-1], 13.78, 5e-3)
for got, want in zip(contrib(oc, ec), [1.497, 0.358, 1.776, 2.805]):
    eq("spot contrib", got, want, 6e-4)
eq("spot x2", X2(oc, ec), 6.44, 5e-3)
assert CV(0.95, 3) == 7.815 and CV(0.95, 2) == 5.991
assert CV(0.95, 2) < 6.44 < CV(0.95, 3)
assert e[3] > 5 and e[4] < 5

# ---- Try (easy to exam) ----
eq("try1", X2([24, 18, 22, 15, 21], [20] * 5), 2.5)
assert 16 + 4 + 4 + 25 + 1 == 50
eq("try3", X2([14, 27, 29, 10], [10, 30, 30, 10]), 1.933, 5e-4)
assert [80 * c / 8 for c in (1, 3, 3, 1)] == [10, 30, 30, 10]
assert round(1.8 + 6.2, 9) == 8.0 and round(12.1 + 4.4, 9) == 16.5
eq("try5", X2([78, 70, 32], [90, 60, 30]), 3.4, 1e-9)
for got, want in zip(contrib([78, 70, 32], [90, 60, 30]), [1.6, 1.667, 0.133]):
    eq("try5 c", got, want, 6e-4)
assert 3.4 < CV(0.95, 2)
p0 = exp(-1.5)
p1 = 1.5 * p0
eq("try6 P0", p0, 0.2231, 5e-5)
eq("try6 P1", p1, 0.3347, 5e-5)
eq("try6 P2+", 1 - p0 - p1, 0.4422, 5e-5)
e = [60 * p0, 60 * p1, 60 * (1 - p0 - p1)]
for got, want in zip(e, [13.39, 20.08, 26.53]):
    eq("try6 E", got, want, 6e-3)
for got, want in zip(contrib([10, 24, 26], e), [0.857, 0.765, 0.011]):
    eq("try6 c", got, want, 6e-4)
eq("try6 x2", X2([10, 24, 26], e), 1.63, 5e-3)
assert 10 + 24 + 26 == 60
assert 576 + 324 + 484 + 225 + 441 == 2050 and 2050 / 20 - 100 == 2.5
assert 7 - 1 == 6 and 6 - 1 - 1 == 4 and 5 - 1 - 1 == 3 and 6 - 1 - 2 == 3

# ---- Exam practice ----
# Q1
eq("ep1", X2([27, 15, 22, 18, 18], [20] * 5), 4.3)
assert 49 + 25 + 4 + 4 + 4 == 86 and 86 / 20 == 4.3 and 27 + 15 + 22 + 18 + 18 == 100
# Q2
e = [3.9, 14.6, 25.8, 27.4, 17.6, 7.4, 3.3]
eq("ep2 sum", sum(e), 100, 1e-9)
assert round(3.9 + 14.6, 9) == 18.5 and round(7.4 + 3.3, 9) == 10.7
assert 5 - 1 - 1 == 3 and CV(0.95, 3) == 7.815
# Q3 geometric 0.3
p, q = 0.3, 0.7
e = [100 * q ** (r - 1) * p for r in range(1, 8)] + [100 * q ** 7]
for got, want in zip(e, [30, 21, 14.7, 10.29, 7.203, 5.042, 3.529, 8.235]):
    eq("ep3 E", got, want, 6e-4)
o = [34, 20, 13, 12, 7, 5, 3, 6]
assert sum(o) == 100
oc = o[:6] + [o[6] + o[7]]
ec = e[:6] + [e[6] + e[7]]
eq("ep3 comb E", ec[-1], 11.76, 6e-3)
eq("ep3 tail check", 100 * q ** 6, ec[-1], 1e-9)
for got, want in zip(contrib(oc, ec), [0.533, 0.048, 0.197, 0.284, 0.006, 0.000, 0.650]):
    eq("ep3 c", got, want, 6e-4)
eq("ep3 x2", X2(oc, ec), 1.72, 5e-3)
assert CV(0.95, 6) == 12.592 and X2(oc, ec) < 12.592
assert min(ec) >= 5 and e[6] < 5
# Q4 PDF 3x^2/8
pr = [(b ** 3 - a ** 3) / 8 for a, b in [(0, 0.5), (0.5, 1), (1, 1.5), (1.5, 2)]]
eq("ep4 total", simpson(lambda x: 3 * x * x / 8, 0, 2), 1, 1e-12)
eq("ep4 P2", simpson(lambda x: 3 * x * x / 8, 0.5, 1), 7 / 64, 1e-12)
assert [round(a * 64, 9) for a in pr] == [1, 7, 19, 37]
e = [160 * a for a in pr]
assert [round(a, 9) for a in e] == [2.5, 17.5, 47.5, 92.5]
oc = [3 + 19, 44, 94]
assert 3 + 19 + 44 + 94 == 160
ec = [e[0] + e[1], e[2], e[3]]
assert ec == [20, 47.5, 92.5]
for got, want in zip(contrib(oc, ec), [0.200, 0.258, 0.024]):
    eq("ep4 c", got, want, 6e-4)
eq("ep4 x2", X2(oc, ec), 0.482, 5e-4)
assert CV(0.95, 2) == 5.991
# Q5 normal, both estimated
pb = [N01.cdf(-1), N01.cdf(0) - N01.cdf(-1), N01.cdf(1) - N01.cdf(0), 1 - N01.cdf(1)]
for got, want in zip(pb, [0.1587, 0.3413, 0.3413, 0.1587]):
    eq("ep5 P", got, want, 5e-5)
e = [120 * a for a in pb]
for got, want in zip(e, [19.04, 40.96, 40.96, 19.04]):
    eq("ep5 E", got, want, 6e-3)
o = [25, 36, 42, 17]
assert sum(o) == 120
for got, want in zip(contrib(o, e), [1.867, 0.601, 0.026, 0.218]):
    eq("ep5 c", got, want, 1e-3)
eq("ep5 x2", X2(o, e), 2.71, 5e-3)
assert 4 - 1 - 2 == 1 and CV(0.95, 1) == 3.841 and X2(o, e) < 3.841
# Q7 typing errors, Poisson
o = [40, 55, 31, 15, 7, 2]
n = sum(o)
assert n == 150
assert [i * f for i, f in enumerate(o)] == [0, 55, 62, 45, 28, 10] and 0 + 55 + 62 + 45 + 28 + 10 == 200
lam = 200 / 150
eq("ep7 lam", lam, 4 / 3)
pp = [exp(-lam) * lam ** k / factorial(k) for k in range(5)]
e = [n * a for a in pp] + [n * (1 - sum(pp))]
for got, want in zip(e, [39.54, 52.72, 35.15, 15.62, 5.21, 1.77]):
    eq("ep7 E", got, want, 6e-3)
oc = o[:4] + [o[4] + o[5]]
ec = e[:4] + [e[4] + e[5]]
assert oc[-1] == 9
eq("ep7 comb E", ec[-1], 6.97, 6e-3)
for got, want in zip(contrib(oc, ec), [0.005, 0.099, 0.489, 0.025, 0.589]):
    eq("ep7 c", got, want, 6e-4)
eq("ep7 x2", X2(oc, ec), 1.21, 5e-3)
assert 5 - 1 - 1 == 3 and X2(oc, ec) < CV(0.95, 3)
assert e[3] > 5 and e[4] > 5 and e[5] < 5
# Q8 seeds B(5, p)
o = [4, 20, 46, 32, 14, 4]
n = sum(o)
assert n == 120 and 0 + 20 + 92 + 96 + 56 + 20 == 284
mean = 284 / 120
eq("ep8 mean", mean, 2.3667, 5e-5)
ph = mean / 5
eq("ep8 p", ph, 0.4733, 5e-5)
e = [n * comb(5, k) * ph ** k * (1 - ph) ** (5 - k) for k in range(6)]
eq("ep8 E0", e[0], 4.86, 5e-3)
eq("ep8 E0 3sf", sf(e[0]), 4.86)
eq("ep8 E0 workings", 120 * 0.5267 ** 5, 4.86, 1e-2)
for got, want in zip(e, [4.86, 21.85, 39.28, 35.30, 15.86, 2.85]):
    eq("ep8 E", got, want, 6e-3)
oc = [o[0] + o[1], o[2], o[3], o[4] + o[5]]
ec = [e[0] + e[1], e[2], e[3], e[4] + e[5]]
assert oc == [24, 46, 32, 18]
eq("ep8 E01", ec[0], 26.71, 6e-3)
eq("ep8 E45", ec[3], 18.71, 6e-3)
for got, want in zip(contrib(oc, ec), [0.276, 1.151, 0.308, 0.027]):
    eq("ep8 c", got, want, 1e-3)
eq("ep8 x2", X2(oc, ec), 1.76, 5e-3)
assert 4 - 1 - 1 == 2 and X2(oc, ec) < CV(0.95, 2)
assert e[0] < 5 and e[5] < 5 and e[1] > 5

# ---- Stretch ----
n, p, x = 100, 0.3, 40
two = (x - n * p) ** 2 / (n * p) + ((n - x) - n * (1 - p)) ** 2 / (n * (1 - p))
eq("stretch a", two, (x - n * p) ** 2 / (n * p * (1 - p)), 1e-9)
eq("stretch b", N01.inv_cdf(0.975) ** 2, 3.8415, 1e-3)
eq("stretch b chi", CV(0.95, 1), 3.841, 5e-4)
eq("stretch 2 scaling", X2([3 * a for a in [15, 25, 22, 18, 24, 16]], [60] * 6), 13.5, 1e-9)
eq("stretch 2 k", 11.070 / 4.5, 2.46, 5e-3)
assert 4.5 * 2 < CV(0.95, 5) < 4.5 * 3

# ---- marks of the examples are counted by the kit; the remaining statements ----
assert CV(0.99, 3) == 11.345
assert abs(CV(0.975, 4) - 11.143) < 5e-4 and abs(CV(0.9, 5) - 9.236) < 5e-4
print("ok")
