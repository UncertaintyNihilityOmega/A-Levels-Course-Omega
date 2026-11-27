# checks/math.fm.twosample.py: recomputes every number in "Comparing two means".
# Standard library only: t percentage points by Simpson integration of the density and bisection.
from math import isclose, sqrt, lgamma, exp, pi, log
from statistics import NormalDist
from functools import lru_cache
from itertools import product


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


def T(p, v):
    return round(t_inv(p, v), 3)


N = NormalDist()


def mean(x):
    return sum(x) / len(x)


def sxx(x):
    m = mean(x)
    return sum((a - m) ** 2 for a in x)


def s2(x):
    return sxx(x) / (len(x) - 1)


def sxx_sum(n, sx, sxx_):
    return sxx_ - sx * sx / n


def pooled(a, b):
    return (sxx(a) + sxx(b)) / (len(a) + len(b) - 2)


# ---- warm-up
eq("w1 mean", 10 - 8, 2)
eq("w1 var", 4 / 5 + 9 / 10, 1.7)
eq("w2", T(0.975, 11), 2.201)
eq("w3", sf((300 - 50 ** 2 / 10) / 9, 3), 5.56)
eq("w3 frac", 50 / 9, (300 - 50 ** 2 / 10) / 9)

# ---- paired figure: points and means (y = 200 - (v - 35) * 7)
bef = [45, 52, 38, 60, 49, 55, 41, 57]
aft = [42, 50, 37, 56, 47, 51, 40, 53]
yb = [200 - (v - 35) * 7 for v in bef]
ya = [200 - (v - 35) * 7 for v in aft]
assert yb == [130, 81, 179, 25, 102, 60, 158, 46], yb
assert ya == [151, 95, 186, 53, 116, 88, 165, 74], ya
eq("fig mean before", sf(mean(bef), 3), 49.6)
eq("fig mean after", mean(aft), 47.0)
eq("fig y before", 200 - (mean(bef) - 35) * 7, 97.6, 0.05)
eq("fig y after", 200 - (mean(aft) - 35) * 7, 116, 1e-9)

# ---- proof: pooled variance unbiased, enumerate a tiny population {0, 1, 4}
pop = [0, 1, 4]
mu = mean(pop)
sig2 = sum((x - mu) ** 2 for x in pop) / len(pop)
n1_, n2_ = 2, 3
tot, cnt = 0.0, 0
for s1 in product(pop, repeat=n1_):
    for s2_ in product(pop, repeat=n2_):
        tot += (sxx(list(s1)) + sxx(list(s2_))) / (n1_ + n2_ - 2)
        cnt += 1
eq("pooled unbiased", tot / cnt, sig2, 1e-9)

# ---- wheat data
A = [5.8, 6.4, 6.1, 5.9, 6.6, 6.2]
B = [5.4, 5.9, 5.6, 6.0, 5.2, 5.7, 5.5]
eq("A sx", sum(A), 37.0)
eq("A sxx2", sum(x * x for x in A), 228.62, 1e-9)
eq("B sx", sum(B), 39.3, 1e-9)
eq("B sxx2", sum(x * x for x in B), 221.11, 1e-9)
eq("A Sxx", sf(sxx(A), 4), 0.4533)
eq("B Sxx", sf(sxx(B), 4), 0.4686)
eq("A Sxx formula", sf(228.62 - 37.0 ** 2 / 6, 4), 0.4533)
eq("B Sxx formula", sf(221.11 - 39.3 ** 2 / 7, 4), 0.4686)
sp2 = pooled(A, B)
eq("sp2 sum", sf(0.4533 + 0.4686, 4), 0.9219)
eq("sp2", sf(sp2, 4), 0.08381)
eq("sp", sf(sqrt(sp2), 4), 0.2895)
eq("s1^2", sf(s2(A), 3), 0.0907)
eq("s2^2", sf(s2(B), 3), 0.0781)
se = sqrt(sp2 * (1 / 6 + 1 / 7))
eq("wheat se", sf(se, 4), 0.1611)
eq("xbarA", sf(mean(A), 5), 6.1667)
eq("xbarB", sf(mean(B), 5), 5.6143)
t1 = (mean(A) - mean(B)) / se
eq("wheat t", sf(t1, 4), 3.430)
eq("wheat crit", T(0.95, 11), 1.796)
t2 = (mean(A) - mean(B) - 0.2) / se
eq("wheat t2", sf(t2, 4), 2.188)
assert t1 > 1.796 and t2 > 1.796

# ---- exam eg: soils
n1, sx1, sxx1 = 8, 195.2, 4771.96
n2, sx2, sxx2 = 9, 204.9, 4669.81
S1, S2 = sxx_sum(n1, sx1, sxx1), sxx_sum(n2, sx2, sxx2)
eq("soil S1", S1, 9.08, 1e-9)
eq("soil S2", S2, 4.92, 1e-9)
sps = (S1 + S2) / (n1 + n2 - 2)
eq("soil sp2", sf(sps, 4), 0.9333)
eq("soil xbar", sx1 / n1, 24.4)
eq("soil ybar", sf(sx2 / n2, 5), 22.767)
tS = (sx1 / n1 - sx2 / n2) / sqrt(sps * (1 / n1 + 1 / n2))
eq("soil t", sf(tS, 4), 3.479)
eq("soil crit", T(0.975, 15), 2.131)
assert tS > 2.131

# ---- paired practice
d = [x - y for x, y in zip(bef, aft)]
assert d == [3, 2, 1, 4, 2, 4, 1, 4]
eq("p sum d", sum(d), 21)
eq("p sum d2", sum(x * x for x in d), 67)
eq("p dbar", mean(d), 2.625)
eq("p sd2", sf(s2(d), 4), 1.696)
eq("p sd", sf(sqrt(s2(d)), 4), 1.302)
eq("p sd2 formula", (67 - 21 ** 2 / 8) / 7, s2(d), 1e-12)
tp = mean(d) / (sqrt(s2(d)) / sqrt(8))
eq("p t", sf(tp, 4), 5.700)
eq("p crit", T(0.95, 7), 1.895)
tcp = T(0.975, 7)
eq("p ci t", tcp, 2.365)
hp = tcp * sqrt(s2(d)) / sqrt(8)
eq("p ci half", sf(hp, 4), 1.089)
eq("p ci lo", sf(mean(d) - hp, 3), 1.54)
eq("p ci hi", sf(mean(d) + hp, 3), 3.71)
# treated as independent
sp_i = pooled(bef, aft)
eq("ind means", mean(bef), 49.625)
eq("ind sum before", sum(bef), 397)
eq("ind sumsq before", sum(v * v for v in bef), 20129)
eq("ind sxx before", sxx(bef), 427.875)
eq("ind sum after", sum(aft), 376)
eq("ind sumsq after", sum(v * v for v in aft), 17988)
eq("ind sxx after", sxx(aft), 316)
eq("ind sp2 working", sf((sxx(bef) + sxx(aft)) / 14, 5), 53.134)
eq("ind sp2", sf(sp_i, 4), 53.13)
eq("ind se", sf(sqrt(sp_i * (1 / 8 + 1 / 8)), 4), 3.645)
tI = (mean(bef) - mean(aft)) / sqrt(sp_i * (1 / 8 + 1 / 8))
eq("ind t", sf(tI, 3), 0.720)
eq("ind crit", T(0.95, 14), 1.761)
assert tI < 1.761

# ---- exam eg: fuel
n, sd, sdd = 9, 25.2, 142.56
vd = (sdd - sd * sd / n) / (n - 1)
eq("fuel dbar", sd / n, 2.8)
eq("fuel sd2", vd, 9.0, 1e-9)
eq("fuel t", (sd / n) / sqrt(vd / n), 2.8, 1e-9)
# paired exam-style example: H0 mu_d = 3.5
bef = [52, 38, 61, 45, 70, 33, 58, 47]; aft = [57, 44, 64, 52, 75, 35, 66, 51]
dd = [y - x for x, y in zip(bef, aft)]
eq("tr d", sum(dd), 40); eq("tr dd", sum(x * x for x in dd), 228)
eq("tr dbar", sum(dd) / 8, 5); eq("tr sd2", (228 - 40 ** 2 / 8) / 7, 4)
tr = (5 - 3.5) / (2 / sqrt(8)); eq("tr t", sf(tr, 4), 2.121)
eq("tr crit", T(0.90, 7), 1.415); assert tr > 1.415
assert 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 == 8   # trainer example
eq("fuel crit", T(0.975, 8), 2.306)
assert 2.8 > 2.306

# ---- exam eg: schools (large samples)
n1, sx1, sxx1 = 50, 4120, 341252
n2, sx2, sxx2 = 60, 4800, 386891
v1 = (sxx1 - sx1 ** 2 / n1) / (n1 - 1)
v2 = (sxx2 - sx2 ** 2 / n2) / (n2 - 1)
eq("school xbar", sx1 / n1, 82.4)
eq("school ybar", sx2 / n2, 80)
eq("school s1", v1, 36, 1e-9)
eq("school s2", v2, 49, 1e-9)
sev = sqrt(v1 / n1 + v2 / n2)
eq("school se", sf(sev, 4), 1.240)
zs = 2.4 / sev
eq("school z", sf(zs, 4), 1.936)
eq("school crit", sf(N.inv_cdf(0.975), 4), 1.960)
eq("school p", sf(2 * (1 - N.cdf(zs)), 3), 0.0529)
assert zs < 1.96 and zs > 1.645
eq("school crit1", sf(N.inv_cdf(0.95), 4), 1.645)
# CI
eq("school ci z", sf(N.inv_cdf(0.975), 4), 1.960)
eq("school ci half", sf(1.960 * sev, 3), 2.43)
eq("school ci lo", sf(2.4 - 1.96 * sev, 2), -0.03)
eq("school ci hi", sf(2.4 + 1.96 * sev, 3), 4.83)
eq("school 90 half", sf(1.645 * sev, 3), 2.04)
eq("school 90 lo", round(2.4 - 1.645 * sev, 2), 0.36)
eq("school 90 hi", sf(2.4 + 1.645 * sev, 3), 4.44)

# ---- known variances
sek = sqrt(16 / 9 + 25 / 12)
eq("kv se", sf(sek, 4), 1.965)
eq("kv z", sf(3.2 / sek, 4), 1.629)
assert 3.2 / sek < 1.645

# ---- exam eg: blood pressure CI
n1, sx1, sxx1 = 10, 1496, 224224
n2, sx2, sxx2 = 11, 1563, 222329
S1, S2 = sxx_sum(n1, sx1, sxx1), sxx_sum(n2, sx2, sxx2)
eq("bp S1", S1, 422.4, 1e-6)
eq("bp S2", sf(S2, 4), 240.9)
spb = (S1 + S2) / 19
eq("bp sp2", sf(spb, 4), 34.91)
eq("bp xbar1", sx1 / n1, 149.6)
eq("bp xbar2", sf(sx2 / n2, 5), 142.09)
db = sx1 / n1 - sx2 / n2
eq("bp diff", sf(db, 3), 7.51)
eq("bp t", T(0.975, 19), 2.093)
hb = 2.093 * sqrt(spb * (1 / n1 + 1 / n2))
eq("bp half", sf(hb, 3), 5.40)
eq("bp lo", sf(db - hb, 3), 2.11)
eq("bp hi", sf(db + hb, 3), 12.9)
assert db - hb > 0

# ---- spot the error
n1, sx1, sxx1 = 5, 100, 2032
n2, sx2, sxx2 = 10, 175, 3080.5
S1, S2 = sxx_sum(n1, sx1, sxx1), sxx_sum(n2, sx2, sxx2)
eq("spot S1", S1, 32)
eq("spot S2", S2, 18)
eq("spot s1^2", S1 / 4, 8)
eq("spot s2^2", S2 / 9, 2)
eq("spot wrong", (8 + 2) / 2, 5)
eq("spot sp2", sf((S1 + S2) / 13, 4), 3.846)
eq("spot xbar1", sx1 / n1, 20)
eq("spot xbar2", sx2 / n2, 17.5)
eq("spot wrong t", sf(2.5 / sqrt(5 * (1 / 5 + 1 / 10)), 4), 2.041)
eq("spot right t", sf(2.5 / sqrt((S1 + S2) / 13 * 0.3), 4), 2.327)
eq("spot crit", T(0.975, 13), 2.160)
assert 2.041 < 2.160 < 2.327
eq("spot score", 1 + 0 + 0 + 1 + 1 + 1 + 1 + 1, 6)

# ---- try block
eq("t2 S1", sxx_sum(7, 84, 1050), 42)
eq("t2 S2", sxx_sum(9, 99, 1100), 11)
eq("t2 sp2", sf(53 / 14, 4), 3.786)
eq("t3 se", sf(2.4 * sqrt(1 / 6 + 1 / 10), 4), 1.239)
eq("t3 factor", sf(sqrt(1 / 6 + 1 / 10), 4), 0.5164)
eq("t4 t", sf(1.2 / (2.0 / sqrt(10)), 4), 1.897)
eq("t4 crit", T(0.975, 9), 2.262)
eq("t5 se", sf(sqrt(6 / 40 + 8 / 50), 4), 0.5568)
eq("t5 z", sf(1.1 / sqrt(6 / 40 + 8 / 50), 4), 1.976)
eq("t6 mid", (-1.2 + 4.6) / 2, 1.7)

# ---- exam practice
Xa = [31, 35, 29, 33, 36, 30]
Ya = [27, 30, 26, 29, 31, 28, 25]
eq("q2 sx", sum(Xa), 194)
eq("q2 sxx", sum(x * x for x in Xa), 6312)
eq("q2 sy", sum(Ya), 196)
eq("q2 syy", sum(x * x for x in Ya), 5516)
eq("q2 S1", sf(sxx(Xa), 4), 39.33)
eq("q2 S2", sxx(Ya), 28)
spq = pooled(Xa, Ya)
eq("q2 sp2", sf(spq, 4), 6.121)
eq("q2 diff", sf(mean(Xa) - mean(Ya), 4), 4.333)
tq2 = (mean(Xa) - mean(Ya) - 2) / sqrt(spq * (1 / 6 + 1 / 7))
eq("q2 t", sf(tq2, 4), 1.695)
assert tq2 < T(0.95, 11)
dq = [2, 3, 1, 4, 0, 4]
eq("q3 sum", sum(dq), 14)
eq("q3 sumsq", sum(x * x for x in dq), 46)
eq("q3 dbar", sf(mean(dq), 4), 2.333)
eq("q3 sd2", sf(s2(dq), 4), 2.667)
tq3 = mean(dq) / sqrt(s2(dq) / 6)
eq("q3 t", sf(tq3, 4), 3.500)
eq("q3 crit", T(0.975, 5), 2.571)
sq4 = sqrt(3.1 ** 2 / 45 + 2.8 ** 2 / 55)
eq("q4 se", sf(sq4, 4), 0.5967)
eq("q4 z", sf(0.9 / sq4, 4), 1.508)
assert 0.9 / sq4 < 1.645
# q5: pooled CI
n1, sx1, sxx1 = 12, 300, 7750
n2, sx2, sxx2 = 10, 203, 4260.9
S1, S2 = sxx_sum(n1, sx1, sxx1), sxx_sum(n2, sx2, sxx2)
eq("q5 S1", S1, 250)
eq("q5 S2", S2, 140, 1e-9)
sp5 = (S1 + S2) / 20
eq("q5 sp2", sp5, 19.5, 1e-9)
se5 = sqrt(sp5 * (1 / 12 + 1 / 10))
eq("q5 se", sf(se5, 4), 1.891)
d5 = sx1 / n1 - sx2 / n2
eq("q5 diff", d5, 4.7)
eq("q5 t95", T(0.975, 20), 2.086)
eq("q5 t99", T(0.995, 20), 2.845)
eq("q5 half95", sf(2.086 * se5, 4), 3.944)
eq("q5 lo95", sf(d5 - 2.086 * se5, 3), 0.756)
eq("q5 hi95", sf(d5 + 2.086 * se5, 3), 8.64)
eq("q5 half99", sf(2.845 * se5, 3), 5.38)
eq("q5 lo99", sf(d5 - 2.845 * se5, 2), -0.68)
eq("q5 hi99", sf(d5 + 2.845 * se5, 3), 10.1)
assert d5 - 2.086 * se5 > 0 and d5 - 2.845 * se5 < 0
# q6: athletes
b6 = [21.4, 20.8, 22.9, 21.1, 23.5, 22.2, 20.6, 22.7]
a6 = [20.9, 20.5, 22.1, 20.8, 22.6, 21.6, 20.4, 21.8]
d6 = [round(x - y, 1) for x, y in zip(b6, a6)]
assert d6 == [0.5, 0.3, 0.8, 0.3, 0.9, 0.6, 0.2, 0.9], d6
eq("q6 sd", sum(d6), 4.5, 1e-9)
eq("q6 sdd", sum(x * x for x in d6), 3.09, 1e-9)
eq("q6 dbar", mean(d6), 0.5625)
eq("q6 s2", sf(s2(d6), 4), 0.07982)
tq6 = mean(d6) / sqrt(s2(d6) / 8)
eq("q6 t", sf(tq6, 4), 5.631)
eq("q6 crit", T(0.95, 7), 1.895)
eq("q6 sx", sum(b6), 175.2, 1e-9)
eq("q6 sxx", sum(x * x for x in b6), 3844.96, 1e-9)
eq("q6 sy", sum(a6), 170.7, 1e-9)
eq("q6 syy", sum(x * x for x in a6), 3646.83, 1e-9)
eq("q6 Sb", sf(sxx(b6), 4), 8.08)
eq("q6 Sa", sf(sxx(a6), 4), 4.519)
sp6 = pooled(b6, a6)
eq("q6 sp2", sf(sp6, 4), 0.8999)
t6i = (mean(b6) - mean(a6)) / sqrt(sp6 * (2 / 8))
eq("q6 ind t", sf(t6i, 4), 1.186)
eq("q6 ind crit", T(0.95, 14), 1.761)
assert t6i < 1.761 < 5
# q7: P and Q
Sp = 1583.28 - 118.8 ** 2 / 9
Sq = 1447.26 - 131.4 ** 2 / 12
eq("q7 Sp", Sp, 15.12, 1e-9)
eq("q7 Sq", sf(Sq, 3), 8.43)
sp7 = (Sp + Sq) / 19
eq("q7 sp2", sf(sp7, 4), 1.239)
eq("q7 xp", 118.8 / 9, 13.2)
eq("q7 xq", 131.4 / 12, 10.95)
t7 = ((13.2 - 10.95) - 2) / sqrt(sp7 * (1 / 9 + 1 / 12))
eq("q7 se", sf(sqrt(sp7 * (1 / 9 + 1 / 12)), 4), 0.4909)
eq("q7 t", sf(t7, 4), 0.5092)
eq("q7 crit", T(0.95, 19), 1.729)
assert abs(t7) < 1.729

# ---- stretch
eq("st1 pooled", sf((4 * 8 + 9 * 2) / 13, 4), 3.846)
eq("st1 frac", 50 / 13, (4 * 8 + 9 * 2) / 13)
eq("st2 t26", T(0.975, 26), 2.056)
eq("st2 t28", T(0.975, 28), 2.048)
eq("st2 n14", sf(2.056 * 4 * sqrt(2 / 14), 4), 3.108)
eq("st2 n15", sf(2.048 * 4 * sqrt(2 / 15), 4), 2.991)
first = next(n for n in range(2, 80) if t_inv(0.975, 2 * n - 2) * 4 * sqrt(2 / n) <= 3)
eq("st2 smallest", first, 15)

# ---- quiz
eq("quiz df", 8 + 11 - 2, 17)
eq("quiz weights", sf((4 * 8 + 9 * 2) / 13, 3), 3.85)
eq("quiz wrong", (5 * 8 + 10 * 2) / 15, 4)

print("ok")
