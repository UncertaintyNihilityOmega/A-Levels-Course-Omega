# checks/math.s2.sampling.py: recomputes every number in the sampling and estimation chapter.
from math import isclose, sqrt
from statistics import NormalDist

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

Z = NormalDist(); Phi = Z.cdf

def s2(xs):
    n = len(xs); m = sum(xs) / n
    return sum((a - m) ** 2 for a in xs) / (n - 1)

# z table
eq("z90", round(Z.inv_cdf(0.95), 3), 1.645); eq("z95", round(Z.inv_cdf(0.975), 3), 1.96)
eq("z98", round(Z.inv_cdf(0.99), 3), 2.326); eq("z99", round(Z.inv_cdf(0.995), 3), 2.576)

# X ~ N(100, 15^2)
eq("a", sf(1 - Phi(5 / 15)), 0.369); eq("a z", sf(5 / 15), 0.333)
eq("b", sf(1 - Phi(1)), 0.159); eq("sd mean 9", 15 / sqrt(9), 5)
# Train waiting time CLT
eq("var Tbar", (50 / 9) / 50, 1 / 9); eq("T z", (4 - 10 / 3) / (1 / 3), 2); eq("T", sf(1 - Phi(2)), 0.0228)
# Unbiased estimates
x = [12, 15, 11, 18, 14]
eq("mean", sum(x) / 5, 14); eq("ss", sum((a - 14) ** 2 for a in x), 30); eq("s2", s2(x), 7.5); eq("n div", 30 / 5, 6)
eq("sum eg", (3900 - 300 ** 2 / 25) / 24, 12.5); eq("mean eg", 300 / 25, 12); eq("ss eg", 3900 - 3600, 300)
# CI examples
eq("ci1 se", 12 / sqrt(36), 2); eq("ci1 lo", 502 - 1.96 * 2, 498.08); eq("ci1 hi", 502 + 1.96 * 2, 505.92)
se = 5.6 / sqrt(80)
eq("ci2 se", round(se, 4), 0.6261); eq("ci2 margin", round(2.326 * 0.6261, 3), 1.456)
eq("ci2 lo", sf(34.2 - 2.326 * se), 32.7); eq("ci2 hi", sf(34.2 + 2.326 * se), 35.7)
eq("n", (2 * 1.96 * 8 / 2) ** 2, 245.8624); eq("sqrt n", 1.96 * 8 / 1 * 1, 15.68); eq("n up", 246, 246)
eq("mid", (48.2 + 51.8) / 2, 50); eq("margin", 51.8 - 50, 1.8); eq("sigma", sf(1.8 * 5 / 1.96), 4.59)
# Proportion
se = sqrt(0.28 * 0.72 / 200)
eq("p se", round(se, 5), 0.03175); eq("p margin", round(1.96 * se, 4), 0.0622); eq("p lo", sf(0.28 - 1.96 * se), 0.218); eq("p hi", sf(0.28 + 1.96 * se), 0.342)
se = sqrt(0.48 * 0.52 / 500)
eq("p2 se", round(se, 5), 0.02234); eq("p2 margin", round(1.645 * se, 4), 0.0368); eq("p2 lo", sf(0.48 - 1.645 * se), 0.443); eq("p2 hi", sf(0.48 + 1.645 * se), 0.517)
# Exam 1: robot
eq("rob mean", 1830 / 60, 30.5); eq("rob ss", 1830 ** 2 / 60, 55815); eq("rob s2", 1185 / 59, 20.08, 0.005)
se = sqrt((1185 / 59) / 60)
eq("rob se", round(se, 4), 0.5786); eq("rob margin", round(1.96 * se, 2), 1.13); eq("rob lo", sf(30.5 - 1.96 * se), 29.4); eq("rob hi", sf(30.5 + 1.96 * se), 31.6)
# Exam 2: biscuits
eq("bisc var", 8 ** 2 / 64, 1); eq("bisc", sf(1 - Phi(1.5)), 0.0668); eq("Phi1.5", round(Phi(1.5), 4), 0.9332)
# Exam 3: nuts
eq("nuts se", 9 / sqrt(16), 2.25); eq("nuts margin", 1.96 * 2.25, 4.41); eq("nuts lo", 502.5 - 4.41, 498.09); eq("nuts hi", 502.5 + 4.41, 506.91)
eq("nuts sqrt", round(2 * 1.96 * 9 / 4, 2), 8.82); eq("nuts n", round((2 * 1.96 * 9 / 4) ** 2, 1), 77.8); eq("nuts n up", 78, 78)
assert (2 * 1.96 * 9 / sqrt(78)) < 4 and (2 * 1.96 * 9 / sqrt(77)) >= 4
# Try
eq("t3", sf(1 - Phi(1)), 0.159); eq("t3 var", 144 / 9, 16)
eq("t4 var", 36 / 100, 0.36); eq("t4 z", round(-1 / 0.6, 3), -1.667); eq("t4", sf(Phi(-1 / 0.6)), 0.0478)
x5 = [8, 11, 9, 14, 13, 10]
eq("t5 sum", sum(x5), 65); eq("t5 mean", sf(65 / 6, 4), 10.83); eq("t5 sumsq", sum(a * a for a in x5), 731)
eq("t5 num", sf(731 - 65 ** 2 / 6, 4), 26.83); eq("t5 s2", sf(s2(x5)), 5.37)
eq("t6 mean", 620 / 50, 12.4); eq("t6 num", 8100 - 620 ** 2 / 50, 412); eq("t6 s2", sf(412 / 49), 8.41)
eq("t7 lo", sf(48 - 1.645), 46.4); eq("t7 hi", sf(48 + 1.645), 49.6)
eq("t8 margin", 2.576 * 2, 5.152); eq("t8 lo", sf(120 - 5.152, 4), 114.8); eq("t8 hi", sf(120 + 5.152, 4), 125.2)
se = sqrt(0.4 * 0.6 / 250)
eq("t9 se", round(se, 5), 0.03098); eq("t9 margin", round(1.96 * se, 4), 0.0607); eq("t9 lo", sf(0.4 - 1.96 * se), 0.339); eq("t9 hi", sf(0.4 + 1.96 * se), 0.461)
# t11 plants
se = 6.5 / sqrt(40)
eq("t11 se", round(se, 4), 1.0277); eq("t11 margin", round(2.576 * 1.0277, 3), 2.647)
eq("t11 lo", sf(52.4 - 2.576 * se), 49.8); eq("t11 hi", sf(52.4 + 2.576 * se), 55.0); assert 52.4 + 2.576 * se < 56
# quiz
eq("q1", 30 / 4, 7.5); eq("q2", 12 / sqrt(16), 3); eq("q2 wrong", 12 / 16, 0.75)

# ---- P14 additions ----
from math import comb as _comb
from statistics import NormalDist as _ND
_N = _ND()
# warm-up
eq("w1 mean", 85 / 10, 8.5); eq("w1 var", 762 / 10 - 8.5 ** 2, 3.95); eq("w1 sd", sf(sqrt(3.95)), 1.99)
eq("w2a", 3 * 7, 21); eq("w2b", 9 * 7, 63); eq("w3 z", sf(_N.inv_cdf(0.9), 4), 1.282); eq("w3", sf(40 + 1.282 * 6), 47.7)
# proof check: population {0, 2}
import itertools as _it
vals = [0, 2]; tot_n1 = tot_n = 0
for pair in _it.product(vals, repeat=2):
    m = sum(pair) / 2; ss = sum((v - m) ** 2 for v in pair); tot_n1 += ss / 1; tot_n += ss / 2
eq("proof n-1", tot_n1 / 4, 1); eq("proof n", tot_n / 4, 0.5)
# spot the error
eq("sp se", 10 / sqrt(25), 2); eq("sp wrong lo", sf(64 - 19.6), 44.4); eq("sp wrong hi", sf(64 + 19.6), 83.6)
eq("sp lo", sf(64 - 3.92), 60.1); eq("sp hi", sf(64 + 3.92), 67.9)
# exam practice
eq("e1 mean", 465 / 30, 15.5); eq("e1 num", round(7482 - 465 ** 2 / 30, 1), 274.5); eq("e1", sf(274.5 / 29), 9.47)
eq("e2 sd", 30 / 4, 7.5); eq("e2 z", round(-10 / 7.5, 3), -1.333); eq("e2", sf(_N.cdf(-10 / 7.5)), 0.0912)
eq("e3 se", 2.4 / 6, 0.4); eq("e3 m", sf(2.576 * 0.4, 3), 1.03); eq("e3 lo", sf(18.7 - 2.576 * .4), 17.7); eq("e3 hi", sf(18.7 + 2.576 * .4), 19.7)
se = 4.2 / sqrt(70); eq("e4 sd", sf(se), 0.502); eq("e4 z", round(1 / se, 3), 1.992); eq("e4", sf(1 - _N.cdf(1 / se)), 0.0232)
ph = 148 / 400; s5 = sqrt(ph * (1 - ph) / 400)
eq("e5 p", ph, 0.37); eq("e5 se", round(s5, 5), 0.02414); eq("e5 m", round(1.96 * s5, 4), 0.0473)
eq("e5 lo", sf(ph - 1.96 * s5), 0.323); eq("e5 hi", sf(ph + 1.96 * s5), 0.417); assert 0.323 < 0.40 < 0.417
eq("e6 mean", (21.4 + 24.6) / 2, 23); eq("e6 m", 24.6 - 23, 1.6); eq("e6 z", round(_N.inv_cdf(0.99), 3), 2.326)
eq("e6 s", sf(1.6 * sqrt(50) / _N.inv_cdf(0.99)), 4.86)
eq("e7 E", 2 ** 3 / 6, 4 / 3); eq("e7 E2", 2 ** 4 / 8, 2); eq("e7 V", 2 - 16 / 9, 2 / 9)
eq("e7 var", 2 / 9 / 40, 1 / 180); eq("e7 sd", sf(sqrt(1 / 180), 3), 0.0745)
z7 = (1.4 - 4 / 3) / sqrt(1 / 180); eq("e7 z", round(z7, 3), 0.894); eq("e7", sf(1 - _N.cdf(z7)), 0.186)
# stretch
a_ = 10 / 40; eq("s1 a", a_, 0.25)
eq("s1 var", a_ ** 2 * 16 / 10 + (1 - a_) ** 2 * 16 / 30, 0.4); eq("s1 parts", 1 / 16 * 16 / 10, 0.1); eq("s1 parts2", 9 / 16 * 16 / 30, 0.3)
best = min((x / 1000 for x in range(1001)), key=lambda t: t ** 2 * 16 / 10 + (1 - t) ** 2 * 16 / 30); eq("s1 argmin", best, 0.25)
eq("s2 b", sf(0.95 ** 20), 0.358); eq("s2 b4", round(0.95 ** 20, 4), 0.3585); eq("s2 mid", round(20 * 0.05 * 0.95 ** 19, 4), 0.3774)
eq("s2 c", sf(1 - 0.95 ** 20 - 20 * 0.05 * 0.95 ** 19), 0.264)
print("ok")
