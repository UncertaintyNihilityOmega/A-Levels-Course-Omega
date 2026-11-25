# checks/math.fm.inference.py: recomputes every number in "The t-distribution: one-sample tests and intervals".
# Standard library only: t percentage points by Simpson integration of the density and bisection.
from math import isclose, sqrt, lgamma, exp, pi, log
from statistics import NormalDist
from functools import lru_cache


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def t_pdf(x, v):
    return exp(lgamma((v + 1) / 2) - lgamma(v / 2) - 0.5 * log(v * pi) - (v + 1) / 2 * log(1 + x * x / v))


def t_cdf(x, v, n=1000):
    h = x / n
    s = t_pdf(0, v) + t_pdf(x, v) + sum((4 if i % 2 else 2) * t_pdf(i * h, v) for i in range(1, n))
    return 0.5 + s * h / 3


@lru_cache(None)
def t_inv(p, v):
    lo, hi = 0.0, 70.0
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_cdf(mid, v) < p else (lo, mid)
    return lo


def mean(x):
    return sum(x) / len(x)


def s2(x):
    m = mean(x)
    return sum((a - m) ** 2 for a in x) / (len(x) - 1)


def s2_sum(n, sx, sxx):
    return (sxx - sx * sx / n) / (n - 1)


# ---- warm-up
eq("w1 mean", 40 / 5, 8)
eq("w1 s2", s2_sum(5, 40, 340), 5)
eq("w2", 6 / sqrt(9), 2)
eq("w3", sf(NormalDist().inv_cdf(0.975)), 1.96)

# ---- the table in MF19 (quote to the printed 3 d.p.)
table = {
    5: (1.476, 2.015, 2.571, 3.365, 4.032),
    9: (1.383, 1.833, 2.262, 2.821, 3.250),
    14: (1.345, 1.761, 2.145, 2.624, 2.977),
    24: (1.318, 1.711, 2.064, 2.492, 2.797),
}
ps = (0.90, 0.95, 0.975, 0.99, 0.995)
for v, row in table.items():
    for p, want in zip(ps, row):
        eq(f"table nu={v} p={p}", round(t_inv(p, v), 3), want, 1e-9)
inf_row = (1.282, 1.645, 1.960, 2.326, 2.576)
for p, want in zip(ps, inf_row):
    eq(f"table inf p={p}", round(NormalDist().inv_cdf(p), 3), want, 1e-9)
# well-known MF19 rows used by the widget text
eq("nu1 .975", round(t_inv(0.975, 1), 3), 12.706)
eq("nu2 .975", round(t_inv(0.975, 2), 3), 4.303)
eq("nu10 .975", round(t_inv(0.975, 10), 3), 2.228)
eq("nu30 .975", round(t_inv(0.975, 30), 3), 2.042)

# ---- plot: t4 density against the normal
eq("t4 pdf0", t_pdf(0, 4), 0.375, 1e-9)
eq("t4 formula", t_pdf(1.3, 4), 0.375 * (1 + 1.3 ** 2 / 4) ** -2.5, 1e-9)
eq("t4 P(T>2)", sf(1 - t_cdf(2, 4), 3), 0.0581)
eq("Z P(Z>2)", sf(1 - NormalDist().cdf(2), 3), 0.0228)
assert 0.3989 > 0.375

# ---- reading-the-table example
eq("a", round(t_inv(0.975, 9), 3), 2.262)
eq("b", round(t_inv(0.99, 14), 3), 2.624)
eq("c", round(t_inv(0.99, 24), 3), 2.492)
eq("d", round(t_inv(0.95, 5), 3), 2.015)
eq("warn", round(t_inv(0.95, 9), 3), 1.833)

# ---- eg: battery
n, sx, sxx = 10, 477.3, 22818.73
xb = sx / n
v = s2_sum(n, sx, sxx)
eq("A xbar", xb, 47.73)
eq("A num", sxx - sx * sx / n, 37.201, 1e-6)
eq("A s2", sf(v, 4), 4.133)
eq("A s", sf(sqrt(v), 4), 2.033)
se = sqrt(v) / sqrt(n)
eq("A se", sf(se, 4), 0.6429)
t = (xb - 50) / se
eq("A t", sf(t, 4), -3.531)
eq("A crit", round(t_inv(0.95, 9), 3), 1.833)
assert t < -1.833 and t < -t_inv(0.995, 9)
eq("A 3.250", round(t_inv(0.995, 9), 3), 3.250)

# ---- eg: rice packets
B = [248.1, 251.6, 247.3, 249.9, 252.4, 246.8, 250.7, 248.5]
eq("B xbar", sf(mean(B), 5), 249.41)
eq("B s", sf(sqrt(s2(B)), 4), 2.051)
eq("B se", sf(sqrt(s2(B)) / sqrt(8), 4), 0.7252)
tB = (mean(B) - 250) / (sqrt(s2(B)) / sqrt(8))
eq("B t", sf(tB, 4), -0.8102)
eq("B crit", round(t_inv(0.975, 7), 3), 2.365)
assert abs(tB) < 2.365

# ---- exam eg: bus journeys
n, sx, sxx = 12, 104.8, 917.74
v = s2_sum(n, sx, sxx)
eq("C s2", sf(v, 4), 0.2261)
eq("C xbar", sf(sx / n, 4), 8.733)
tC = (sx / n - 8.2) / sqrt(v / n)
eq("C t", sf(tC, 4), 3.886)
eq("C crit", round(t_inv(0.95, 11), 3), 1.796)
assert tC > 1.796

# ---- eg: critical region
eq("D crit", round(t_inv(0.95, 15), 3), 1.753)
eq("D se", 2.4 / 4, 0.6)
eq("D region", sf(30 + 1.753 * 0.6, 4), 31.05)
eq("D normal", sf(30 + 1.645 * 0.6, 4), 30.99)
eq("D exact t", t_inv(0.95, 15) * 0.6 + 30, 31.0518, 1e-3)

# ---- proof: mu0 inside the interval iff |t| < crit
for mu0 in (4.0, 4.7, 5.2, 5.9):
    data = (4.1, 5.3, 4.9, 4.2, 5.0)
    xb2, s_, n2 = mean(data), sqrt(s2(data)), len(data)
    tcrit = t_inv(0.975, n2 - 1)
    inside = xb2 - tcrit * s_ / sqrt(n2) < mu0 < xb2 + tcrit * s_ / sqrt(n2)
    assert inside == (abs((xb2 - mu0) / (s_ / sqrt(n2))) < tcrit), mu0

# ---- CI example: seedlings
Dd = [12.4, 13.1, 11.8, 12.9, 13.6, 12.2, 12.7, 13.3, 12.5]
eq("CI xbar", sf(mean(Dd), 4), 12.72)
eq("CI s", sf(sqrt(s2(Dd)), 4), 0.5652)
eq("CI se", sf(sqrt(s2(Dd)) / 3, 4), 0.1884)
tt = round(t_inv(0.975, 8), 3)
eq("CI t", tt, 2.306)
half = tt * sqrt(s2(Dd)) / 3
eq("CI half", sf(half, 4), 0.4344)
eq("CI lo", sf(mean(Dd) - half, 5), 12.288)
eq("CI hi", sf(mean(Dd) + half, 5), 13.157)
eq("CI 3sf", sf(mean(Dd) - half, 3), 12.3)
eq("CI 3sf hi", sf(mean(Dd) + half, 3), 13.2)

# ---- plates 99%
n, sx, sxx = 12, 42.32, 149.391
v = s2_sum(n, sx, sxx)
eq("E xbar", sf(sx / n, 5), 3.5267)
eq("E s2", sf(v, 5), 0.012952)
eq("E s", sf(sqrt(v), 4), 0.1138)
eq("E se", sf(sqrt(v / n), 4), 0.03285)
tE = round(t_inv(0.995, 11), 3)
eq("E t", tE, 3.106)
hE = tE * sqrt(v / n)
eq("E half", sf(hE, 4), 0.1020)
eq("E lo", sf(sx / n - hE, 5), 3.4246)
eq("E hi", sf(sx / n + hE, 5), 3.6287)
eq("E lo 3sf", sf(sx / n - hE, 3), 3.42)
eq("E hi 3sf", sf(sx / n + hE, 3), 3.63)
tcheck = (sx / n - 3.40) / sqrt(v / n)
eq("E t check", sf(tcheck, 4), 3.856)
assert tcheck > tE and not (sx / n - hE < 3.40 < sx / n + hE)

# ---- exam eg: 98% CI
n, sx, sxx = 15, 612, 25098.4
v = s2_sum(n, sx, sxx)
eq("F xbar", sx / n, 40.8)
eq("F s2", v, 9.2, 1e-9)
tF = round(t_inv(0.99, 14), 3)
eq("F t", tF, 2.624)
hF = tF * sqrt(v / n)
eq("F half", sf(hF, 4), 2.055)
eq("F lo", sf(sx / n - hF, 3), 38.7)
eq("F hi", sf(sx / n + hF, 3), 42.9)
assert sx / n - hF < 42 < sx / n + hF

# ---- spot the error
n, sx, sxx = 9, 558, 34668
eq("S s2", s2_sum(n, sx, sxx), 9)
eq("S xbar", sx / n, 62)
eq("S t", (62 - 60) / (3 / sqrt(9)), 2)
eq("S wrong crit", round(t_inv(0.95, 8), 3), 1.860)
eq("S right crit", round(t_inv(0.975, 8), 3), 2.306)
assert 2 > 1.860 and 2 < 2.306
eq("S score", 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1, 7)

# ---- try block
eq("t1a", round(t_inv(0.975, 12), 3), 2.179)
eq("t1b", round(t_inv(0.95, 12), 3), 1.782)
eq("t1c", round(t_inv(0.99, 12), 3), 2.681)
eq("t2 se", 6 / sqrt(16), 1.5)
eq("t2 t", sf(2.9 / 1.5, 4), 1.933)
eq("t3 one", round(t_inv(0.95, 15), 3), 1.753)
eq("t3 two", round(t_inv(0.975, 15), 3), 2.131)
assert 1.753 < 1.933 < 2.131
n, sx, sxx = 7, 203, 5908
v = s2_sum(n, sx, sxx)
eq("t4 xbar", sx / n, 29)
eq("t4 s2", v, 3.5, 1e-9)
t4 = round(t_inv(0.95, 6), 3)
eq("t4 t", t4, 1.943)
h4 = t4 * sqrt(v / n)
eq("t4 half 4sf", round(h4, 3), 1.374)
eq("t4 lo", sf(29 - h4, 3), 27.6)
eq("t4 hi", sf(29 + h4, 3), 30.4)
eq("t5 mid", (4.1 + 5.3) / 2, 4.7)
assert not (4.1 < 5.5 < 5.3)

# ---- exam practice
Q2 = [24.1, 26.3, 25.8, 27.0, 24.9, 26.1, 25.4, 27.2, 25.9, 26.5]
eq("q2 xbar", mean(Q2), 25.92)
eq("q2 s", sf(sqrt(s2(Q2)), 4), 0.9402)
tq2 = (mean(Q2) - 25.0) / (sqrt(s2(Q2)) / sqrt(10))
eq("q2 t", sf(tq2, 4), 3.094)
eq("q2 crit", round(t_inv(0.975, 9), 3), 2.262)
eq("q2 sums", sum(Q2), 259.2, 1e-9)
# q3 is t4 above
n, sx, sxx = 14, 1645, 193755.5
v = s2_sum(n, sx, sxx)
eq("q4 xbar", sx / n, 117.5)
eq("q4 s2", v, 36, 1e-6)
tq4 = (117.5 - 120) / (6 / sqrt(14))
eq("q4 t", sf(tq4, 4), -1.559)
eq("q4 crit", round(t_inv(0.95, 13), 3), 1.771)
assert tq4 > -1.771
eq("q5 t", round(t_inv(0.975, 19), 3), 2.093)
eq("q5 se", sf(8 / sqrt(20), 4), 1.789)
eq("q5 half", sf(2.093 * 8 / sqrt(20), 4), 3.744)
eq("q5 lo", round(100 - t_inv(0.975, 19) * 8 / sqrt(20), 1), 96.3)
eq("q5 hi", round(100 + t_inv(0.975, 19) * 8 / sqrt(20), 1), 103.7)
# q6
tq6 = (53.6 - 50) / (6 / 4)
eq("q6 t", tq6, 2.4)
eq("q6 c5", round(t_inv(0.95, 15), 3), 1.753)
eq("q6 c1", round(t_inv(0.99, 15), 3), 2.602)
eq("q6 z1", round(NormalDist().inv_cdf(0.99), 3), 2.326)
assert 2.326 < 2.4 < 2.602 and 2.4 > 1.753
# q7 washers
Q7 = [5.12, 4.87, 5.31, 4.95, 5.20, 5.05, 4.78, 5.22]
eq("q7 sx", sum(Q7), 40.5)
eq("q7 sxx", sum(x * x for x in Q7), 205.2692, 1e-9)
eq("q7 xbar", mean(Q7), 5.0625)
eq("q7 s2", sf(s2(Q7), 4), 0.03399)
eq("q7 s", sf(sqrt(s2(Q7)), 4), 0.1844)
eq("q7 t", round(t_inv(0.975, 7), 3), 2.365)
h7 = 2.365 * sqrt(s2(Q7)) / sqrt(8)
eq("q7 lo", sf(mean(Q7) - h7, 3), 4.91)
eq("q7 hi", sf(mean(Q7) + h7, 3), 5.22)
eq("q7 width", sf(2 * h7, 3), 0.308)
zq = NormalDist().inv_cdf(0.975)
hz = 1.960 * 0.15 / sqrt(8)
eq("q7 z lo", sf(mean(Q7) - hz, 3), 4.96)
eq("q7 z hi", sf(mean(Q7) + hz, 3), 5.17)
eq("q7 z width", sf(2 * hz, 3), 0.208)
eq("q7 z", sf(zq, 4), 1.960)

# ---- stretch
eq("st1 mid", (41.2 + 46.8) / 2, 44)
eq("st1 t95", round(t_inv(0.975, 9), 3), 2.262)
eq("st1 t99", round(t_inv(0.995, 9), 3), 3.250)
s_ = 2.8 * sqrt(10) / 2.262
eq("st1 s", sf(s_, 4), 3.914)
h = 3.250 * s_ / sqrt(10)
eq("st1 half", sf(h, 4), 4.023)
eq("st1 lo", sf(44 - h, 3), 40.0)
eq("st1 hi", sf(44 + h, 3), 48.0)
tab = {16: 2.131, 17: 2.120, 18: 2.110}
for n_, tv in tab.items():
    eq(f"st2 t nu={n_ - 1}", round(t_inv(0.975, n_ - 1), 3), tv)
eq("st2 16", sf(2.131 / 4, 3), 0.533)
eq("st2 17", sf(2.120 / sqrt(17), 3), 0.514)
eq("st2 18", sf(2.110 / sqrt(18), 3), 0.497)
first = next(n_ for n_ in range(2, 60) if t_inv(0.975, n_ - 1) / sqrt(n_) <= 0.5)
eq("st2 smallest n", first, 18)

# ---- added: gauges, divisor-n conversion
Gd = [14.2, 15.8, 13.9, 16.1, 15.0, 14.7]
eq("G xbar", mean(Gd), 14.95)
eq("G s", sf(sqrt(s2(Gd)), 4), 0.8689)
eq("G se", sf(sqrt(s2(Gd)) / sqrt(6), 4), 0.3547)
tG = (mean(Gd) - 15.5) / (sqrt(s2(Gd)) / sqrt(6))
eq("G t", sf(tG, 4), -1.550)
eq("G c5", round(t_inv(0.95, 5), 3), 2.015)
eq("G c10", round(t_inv(0.90, 5), 3), 1.476)
assert tG > -2.015 and tG < -1.476
eq("H sum", 12 * 1.8 ** 2, 38.88)
sH2 = 38.88 / 11
eq("H s2", sf(sH2, 4), 3.535)
eq("H s", sf(sqrt(sH2), 4), 1.880)
eq("H se", sf(sqrt(sH2) / sqrt(12), 4), 0.5427)
tH = 0.9 / (sqrt(sH2) / sqrt(12))
eq("H t", sf(tH, 4), 1.658)
eq("H crit", round(t_inv(0.975, 11), 3), 2.201)
eq("H wrong t", sf(0.9 / (1.8 / sqrt(12)), 4), 1.732)
assert tH < 2.201

print("ok")
