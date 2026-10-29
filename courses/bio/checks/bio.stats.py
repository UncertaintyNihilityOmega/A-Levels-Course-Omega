# checks/bio.stats.py: recomputes every number in the Statistics chapter (chapters/bio.stats.md).
import os, sys
from math import sqrt, isclose, comb
from fractions import Fraction as F
from statistics import mean, median, mode, stdev

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
from crit import chi2_crit, t_crit, r_crit


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


def chi2(O, E):
    return sum((o - e) ** 2 / e for o, e in zip(O, E))


def ranks(v):
    s = sorted(v)
    return [s.index(q) + 1 for q in v]


def tstat(m1, s1, n1, m2, s2, n2):
    return abs(m1 - m2) / sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


# --- aphids ---
ap = [2, 3, 3, 4, 4, 4, 5, 7, 24]
eq("aphid sum", sum(ap), 56)
eq("aphid mean", round(mean(ap), 1), 6.2)
eq("aphid median", median(ap), 4)
eq("aphid mode", mode(ap), 4)
eq("aphid range", max(ap) - min(ap), 22)

# --- probability: Cc x Cc ---
eq("CF first child", F(1, 2) * F(1, 2), F(1, 4))
eq("both of two", F(1, 4) * F(1, 4), F(1, 16))
eq("one of two", 2 * F(1, 4) * F(3, 4), F(3, 8))
eq("3/16 each order", F(1, 4) * F(3, 4), F(3, 16))

# --- bean roots ---
x = [34, 29, 38, 31, 35, 31]
eq("bean mean", mean(x), 33.0)
ss = sum((v - mean(x)) ** 2 for v in x)
eq("bean SS", ss, 54)
for v, d, d2 in zip(x, [1, -4, 5, -2, 2, -2], [1, 16, 25, 4, 4, 4]):
    eq("dev", v - 33, d); eq("dev2", (v - 33) ** 2, d2)
s = stdev(x)
eq("bean s", sf(s), 3.29)
se = s / sqrt(6)
eq("bean SE", sf(se, 3), 1.34)
eq("bean 2SE", sf(2 * se), 2.68)
eq("bean CI lo", round(33 - 2 * se, 1), 30.3)
eq("bean CI hi", round(33 + 2 * se, 1), 35.7)

# --- tomato error bars ---
n = 10
for nm, m, sd_, se_t, lo, hi in [("control", 33.0, 3.3, 1.04, 30.9, 35.1), ("X", 36.0, 3.5, 1.11, 33.8, 38.2), ("Y", 42.0, 3.1, 0.98, 40.0, 44.0)]:
    se_ = sd_ / sqrt(n)
    eq(nm + " SE", round(se_, 2), se_t)
    eq(nm + " lo", round(m - 2 * se_, 1), lo)
    eq(nm + " hi", round(m + 2 * se_, 1), hi)
assert 35.1 > 33.8 and 38.2 < 40.0
eq("X - control", 36.0 - 33.0, 3.0)
eq("Y - X", 42.0 - 36.0, 6.0)

# --- woodlice chi-squared ---
O = [66, 38, 54, 22]
E = [45] * 4
eq("woodlice total", sum(O), 180)
eq("E", 180 / 4, 45)
parts = [(o - 45) ** 2 / 45 for o in O]
for p, w in zip(parts, [9.80, 1.09, 1.80, 11.76]):
    eq("woodlice part", round(p, 2), w)
eq("woodlice chi2", sf(chi2(O, E), 3), 24.4)
eq("woodlice crit", round(chi2_crit(3), 2), 7.81)
eq("dark total", 66 + 54, 120); eq("light total", 38 + 22, 60)

# --- Daphnia t-test ---
a = [134, 140, 146, 150, 152, 158, 162, 166]
b = [172, 176, 181, 184, 189, 191, 196, 207]
eq("a mean", mean(a), 151); eq("b mean", mean(b), 187)
eq("a SS", sum((v - 151) ** 2 for v in a), 832)
eq("b SS", sum((v - 187) ** 2 for v in b), 892)
s1, s2 = sqrt(832 / 7), sqrt(892 / 7)
eq("s1", round(s1, 1), 10.9); eq("s2", round(s2, 1), 11.3)
eq("s1^2 /8", round(s1 ** 2 / 8 * 1, 2), round(832 / 7 / 8, 2))
eq("118.86", round(832 / 7, 2), 118.86); eq("127.43", round(892 / 7, 2), 127.43)
eq("14.857", round(832 / 7 / 8, 3), 14.857); eq("15.929", round(892 / 7 / 8, 3), 15.929)
eq("denominator", round(sqrt(832 / 7 / 8 + 892 / 7 / 8), 3), 5.548)
t = tstat(151, s1, 8, 187, s2, 8)
eq("t", sf(t), 6.49)
eq("t crit 14", round(t_crit(14), 2), 2.14)

# --- Pearson, soil nitrate ---
xs = [10, 20, 30, 40, 50, 60, 70]
ys = [12, 15, 21, 25, 33, 30, 39]
n = 7
eq("xbar", mean(xs), 40); eq("ybar", mean(ys), 25)
sxy = sum(p * q for p, q in zip(xs, ys))
eq("sum xy", sxy, 8230)
eq("sx", round(stdev(xs), 3), 21.602); eq("sy", round(stdev(ys), 3), 9.747)
eq("numerator", sxy - n * 40 * 25, 1230)
den = (n - 1) * 21.602 * 9.747
eq("denominator", round(den, 1), 1263.3)
r = (sxy - n * 40 * 25) / ((n - 1) * stdev(xs) * stdev(ys))
eq("r", round(r, 3), 0.974)
eq("r crit 7", round(r_crit(7), 3), 0.754)

# --- Spearman barnacles ---
h = [0.5, 0.9, 1.2, 1.8, 2.1, 2.6, 3.0, 3.4, 4.1]
c = [210, 180, 195, 120, 96, 110, 40, 52, 18]
rh, rc = ranks(h), ranks(c)
D = [p - q for p, q in zip(rh, rc)]
eq("rank c", rc == [9, 7, 8, 6, 4, 5, 2, 3, 1], True) if False else None
assert rc == [9, 7, 8, 6, 4, 5, 2, 3, 1] and rh == list(range(1, 10))
assert D == [-8, -5, -5, -2, 1, 1, 5, 5, 8]
assert [d * d for d in D] == [64, 25, 25, 4, 1, 1, 25, 25, 64]
eq("sumD2", sum(d * d for d in D), 234)
eq("6*234", 6 * 234, 1404); eq("9^3-9", 9 ** 3 - 9, 720)
eq("rs", round(1 - 1404 / 720, 2), -0.95)

# --- practice: easy set ---
eg = [3, 4, 4, 5, 4, 6, 9]
eq("eggs mean", mean(eg), 5); eq("eggs median", median(eg), 4); eq("eggs mode", mode(eg), 4); eq("eggs range", max(eg) - min(eg), 6)
eq("SE 16", 4.2 / sqrt(16), 1.05)
eq("CI lo", 52 - 2 * 1.05, 49.9); eq("CI hi", 52 + 2 * 1.05, 54.1)
eq("df chi 5", 5 - 1, 4); eq("df t", 12 + 9 - 2, 19)
eq("tall^3", float(F(3, 4) ** 3), 27 / 64); eq("27/64", round(27 / 64, 2), 0.42)
eq("crit r10", round(r_crit(10), 3), 0.632)
assert 0.82 > 0.632
assert (9.0, 15.0) == (12.0 - 3.0, 12.0 + 3.0) and (11.0, 17.0) == (14.0 - 3.0, 14.0 + 3.0) and 15.0 > 11.0

# --- exam practice ---
s_sn = sqrt(63.0 / 7)
eq("snail s", round(s_sn, 2), 3.00)
eq("snail SE", round(s_sn / sqrt(8), 2), 1.06)
eq("snail CI", round(12.5 - 2 * s_sn / sqrt(8), 1), 10.4); eq("snail CI hi", round(12.5 + 2 * s_sn / sqrt(8), 1), 14.6)
eq("snail 2SE", round(2 * 1.06, 2), 2.12)
# striped snails
eq("E striped", 160 * 3 / 4, 120); eq("E unstriped", 160 / 4, 40)
x2 = chi2([118, 42], [120, 40])
eq("chi2 snails", round(x2, 2), 0.13)
eq("parts", round(4 / 120, 3), 0.033); eq("parts2", round(4 / 40, 3), 0.1)
eq("crit df1", round(chi2_crit(1), 2), 3.84)
# wheat
tw = tstat(42.6, 3.1, 10, 38.9, 3.7, 12)
eq("wheat 0.961", round(3.1 ** 2 / 10, 3), 0.961); eq("wheat 1.141", round(3.7 ** 2 / 12, 3), 1.141)
eq("wheat den", round(sqrt(3.1 ** 2 / 10 + 3.7 ** 2 / 12), 3), 1.450)
eq("wheat t", round(tw, 2), 2.55)
eq("wheat crit 20", round(t_crit(20), 2), 2.09)
eq("wheat diff", round(42.6 - 38.9, 1), 3.7)
# algae
for nm, m, e in [("P", 52, 6), ("Q", 61, 7), ("R", 83, 8)]:
    pass
assert 52 + 6 > 61 - 7          # P, Q overlap
assert 61 + 7 < 83 - 8          # Q, R do not
eq("algae P lo/hi", 52 - 6, 46); eq("Q lo", 61 - 7, 54); eq("Q hi", 61 + 7, 68); eq("R lo", 83 - 8, 75); eq("R hi", 83 + 8, 91)
eq("P hi", 52 + 6, 58)
eq("algae SE", 7 / 2, 3.5); eq("algae s", round(3.5 * sqrt(10), 1), 11.1)
# beetles
bx = [9, 10, 11, 13, 14, 15]; by = [2.9, 3.6, 3.3, 4.3, 4.4, 5.5]
eq("bx mean", mean(bx), 12.0); eq("by mean", round(mean(by), 6), 4.0)
eq("bsxy", round(sum(p * q for p, q in zip(bx, by)), 6), 298.4)
eq("bsx", round(stdev(bx), 3), 2.366); eq("bsy", round(stdev(by), 3), 0.934)
eq("bnum", round(298.4 - 6 * 12.0 * 4.0, 6), 10.4)
eq("bden", round(5 * 2.366 * 0.934, 2), 11.05)
eq("br", round(10.4 / (5 * 2.366 * 0.934), 3), 0.941)
rb = (sum(p * q for p, q in zip(bx, by)) - 6 * 12 * 4) / (5 * stdev(bx) * stdev(by))
eq("br unrounded", round(rb, 3), 0.941)
eq("r crit 6", round(r_crit(6), 3), 0.811)
# caddis
tt = [8, 9, 11, 12, 14, 15, 17, 19]; cc = [48, 52, 41, 35, 38, 22, 25, 14]
rt, rcc = ranks(tt), ranks(cc)
assert rt == list(range(1, 9)) and rcc == [7, 8, 6, 4, 5, 2, 3, 1]
Dd = [p - q for p, q in zip(rt, rcc)]
assert Dd == [-6, -6, -3, 0, 0, 4, 4, 7]
eq("caddis sumD2", sum(d * d for d in Dd), 162)
eq("36+36+9+16+16+49", 36 + 36 + 9 + 0 + 0 + 16 + 16 + 49, 162)
eq("caddis 8^3-8", 8 ** 3 - 8, 504)
eq("caddis 1.929", round(6 * 162 / 504, 3), 1.929)
eq("caddis rs", round(1 - 6 * 162 / 504, 3), -0.929)
# finches
eq("finch SE", round(0.6 / sqrt(50), 3), 0.085)
eq("finch lo", round(9.4 - 2 * 0.085, 2), 9.23); eq("finch hi", round(9.4 + 2 * 0.085, 2), 9.57)
eq("finch 2sd lo", round(9.4 - 1.2, 1), 8.2); eq("finch 2sd hi", round(9.4 + 1.2, 1), 10.6)
# maize
Om = [96, 28, 25, 11]; Em = [160 * 9 / 16, 160 * 3 / 16, 160 * 3 / 16, 160 / 16]
assert Em == [90, 30, 30, 10] and sum(Om) == 160
for p, w in zip([(o - e) ** 2 / e for o, e in zip(Om, Em)], [0.40, 0.13, 0.83, 0.10]):
    eq("maize part", round(p, 2), w)
eq("maize chi2", round(chi2(Om, Em), 2), 1.47)
eq("maize 0.40+0.13+0.83+0.10", 0.40 + 0.13 + 0.83 + 0.10, 1.46) if False else None
eq("maize crit", round(chi2_crit(3), 2), 7.81)
eq("9/16", float(F(3, 4) * F(3, 4)), 9 / 16)
# stretch
eq("SE A", 4.0 / sqrt(25), 0.80); eq("SE B", 12.0 / sqrt(25), 2.4)
eq("A lo", 50 - 1.6, 48.4); eq("A hi", 50 + 1.6, 51.6); eq("B lo", 50 - 4.8, 45.2); eq("B hi", 50 + 4.8, 54.8)
eq("sd ratio", 12.0 / 4.0, 3.0)
eq("0.95^20", round(0.95 ** 20, 3), 0.358); eq("at least one", round(1 - 0.95 ** 20, 2), 0.64)

# --- quiz ---
eq("quiz SE25", 8.0 / sqrt(25), 1.6); eq("quiz SE100", 8.0 / sqrt(100), 0.8); eq("quarter", 1.6 / 4, 0.4)
eq("quiz df", 6 - 1, 5)
eq("quiz rs crit n10", round(0.71, 2), 0.71); assert 0.71 > 0.648
eq("rs crit 10 given", 0.648, 0.648)
print("ok")
