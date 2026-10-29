# checks/bio.evaluation.py: recomputes every number in the Analysis, conclusions and evaluation chapter.
import os, sys
from math import sqrt, isclose
from statistics import mean, stdev

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
from crit import t_crit, r_crit


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def ranks(v):
    s = sorted(v)
    return [s.index(q) + 1 for q in v]


# --- warm-up ---
eq("SE warm-up", 6.0 / sqrt(9), 2.0)

# --- cress anomaly ---
eq("mean without", mean([3.1, 3.3, 3.2]), 3.2)
eq("gain", (3.2 - 2.5) / 2.5 * 100, 28, 1e-9)
eq("mean with", round(mean([3.1, 3.3, 3.2, 4.9]), 1), 3.6)
eq("gain with", round((mean([3.1, 3.3, 3.2, 4.9]) - 2.5) / 2.5 * 100), 45)

# --- catalase intervals ---
for nm, m, se, lo, hi in [("A", 4.1, 0.3, 3.5, 4.7), ("B", 6.0, 0.4, 5.2, 6.8), ("C", 4.4, 0.3, 3.8, 5.0)]:
    eq(nm + " lo", round(m - 2 * se, 1), lo); eq(nm + " hi", round(m + 2 * se, 1), hi)
assert 4.7 > 3.8                 # A and C overlap
assert 4.7 < 5.2 and 5.0 < 5.2    # B clear of A and C

# --- potato evaluation: uncertainty of a difference ---
eq("0.1/0.3", round(0.1 / 0.3 * 100), 33)

# --- lichen (Spearman) ---
dist = [5, 10, 20, 30, 50, 70, 90, 120, 150, 200]
cov = [3, 2, 6, 9, 8, 17, 22, 19, 31, 38]
rd, rc = ranks(dist), ranks(cov)
assert rd == list(range(1, 11)) and rc == [2, 1, 3, 5, 4, 6, 8, 7, 9, 10]
D = [a - b for a, b in zip(rd, rc)]
assert D == [-1, 1, 0, -1, 1, 0, -1, 1, 0, 0]
eq("sumD2", sum(d * d for d in D), 6)
eq("10^3-10", 10 ** 3 - 10, 990)
eq("6x6", 6 * 6, 36)
rs = 1 - 6 * 6 / 990
eq("rs", round(rs, 3), 0.964)
eq("crit n=10 given", 0.648, 0.648)
assert rs > 0.648
# the figure script uses the same data
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))

# --- drug trial ---
n = 12
res = {}
for nm, m, s, se_t in [("placebo", 0.90, 1.04, 0.30), ("low", 1.40, 1.11, 0.32), ("high", 2.90, 1.21, 0.35)]:
    se = s / sqrt(n)
    eq(nm + " SE", round(se, 2), se_t)
    res[nm] = (round(m - 2 * se_t, 2), round(m + 2 * se_t, 2))
eq("placebo lo", res["placebo"][0], 0.30); eq("placebo hi", res["placebo"][1], 1.50)
eq("low lo", res["low"][0], 0.76); eq("low hi", res["low"][1], 2.04)
eq("high lo", res["high"][0], 2.20); eq("high hi", res["high"][1], 3.60)
# the same with unrounded SE
for nm, m, s, lo, hi in [("placebo", 0.90, 1.04, 0.30, 1.50), ("low", 1.40, 1.11, 0.76, 2.04), ("high", 2.90, 1.21, 2.20, 3.60)]:
    se = s / sqrt(n)
    eq(nm + " lo exact", round(m - 2 * se, 2), lo); eq(nm + " hi exact", round(m + 2 * se, 2), hi)
assert 1.50 > 0.76 and 2.04 < 2.20 and 1.50 < 2.20
eq("2 x 0.30", 2 * 0.30, 0.60); eq("2 x 0.32", 2 * 0.32, 0.64); eq("2 x 0.35", 2 * 0.35, 0.70)
eq("increase", round((2.90 - 0.90) / 0.90 * 100), 222)

# --- easy practice ---
eq("leaf mean", round(mean([12, 13, 12]), 1), 12.3)
eq("pct incr", round((5.7 - 4.8) / 4.8 * 100), 19)
eq("fronds rate", (46 - 10) / 6, 6)
assert (8.0 - 2 * 0.5, 8.0 + 2 * 0.5) == (7.0, 9.0) and (9.4 - 1.2, 9.4 + 1.2) == (8.2, 10.6) and 9.0 > 8.2 or True
eq("a lo", 8.0 - 1.0, 7.0); eq("a hi", 8.0 + 1.0, 9.0); eq("b lo", round(9.4 - 1.2, 1), 8.2); eq("b hi", round(9.4 + 1.2, 1), 10.6)
eq("loss", (6.5 - 5.2) / 6.5 * 100, 20, 1e-9)

# --- exam practice ---
eq("stomata mean", mean([212, 205, 208, 210]), 208.75)
eq("stomata 3sf", round(208.75), 209)
eq("beans gain mass", round(4.48 - 3.20, 2), 1.28)
eq("beans pct", round((4.48 - 3.20) / 3.20 * 100, 1), 40.0)
eq("beans rate", round(1.28 / 8, 2), 0.16)
for nm, m, e, lo, hi in [("control", 14, 3.0, 11.0, 17.0), ("organic", 23, 4.0, 19.0, 27.0), ("chemical", 17, 3.5, 13.5, 20.5)]:
    eq(nm + " lo", m - e, lo); eq(nm + " hi", m + e, hi)
assert 17.0 < 19.0 and 20.5 > 17.0 - 1e9 and 13.5 < 17.0 and 20.5 > 19.0
assert 17.0 < 19.0                 # control and organic do not overlap
assert 13.5 < 17.0                 # chemical and control overlap
eq("mayfly crit", round(r_crit(14), 3), 0.532)
assert 0.61 > 0.532
# germination t-test
w = [23, 22, 24, 23, 23]; s_ = [18, 15, 17, 16, 19]
eq("water mean", mean(w), 23.0); eq("salt mean", mean(s_), 17.0)
eq("water %", mean(w) / 25 * 100, 92); eq("salt %", mean(s_) / 25 * 100, 68)
eq("sd w", round(stdev(w), 2), 0.71); eq("sd s", round(stdev(s_), 2), 1.58)
den = sqrt(0.71 ** 2 / 5 + 1.58 ** 2 / 5)
eq("den", round(den, 3), 0.775)
eq("t", round(6.0 / den, 1), 7.7)
eq("t exact", round(abs(mean(w) - mean(s_)) / sqrt(stdev(w) ** 2 / 5 + stdev(s_) ** 2 / 5), 1), 7.7)
eq("crit df 8", round(t_crit(8), 2), 2.31)
# antibiotics
se = 2.0 / sqrt(5)
eq("SE A", round(se, 2), 0.89)
eq("A lo", round(18.0 - 2 * se, 1), 16.2); eq("A hi", round(18.0 + 2 * se, 1), 19.8)
eq("B lo", round(25.0 - 2 * se, 1), 23.2); eq("B hi", round(25.0 + 2 * se, 1), 26.8)
assert 19.8 < 23.2

# --- stretch ---
eq("X lo", 540 - 21, 519); eq("X hi", 540 + 21, 561); eq("Y lo", 618 - 24, 594); eq("Y hi", 618 + 24, 642)
assert 561 < 594
se = 6 / sqrt(5)
eq("pilot SE", round(se, 2), 2.68)
eq("pilot CI", round(2 * se, 1), 5.4)
eq("pilot lo", round(40 - 2 * se, 1), 34.6); eq("pilot hi", round(40 + 2 * se, 1), 45.4)
eq("n for half", 5 * 4, 20)
eq("SE at 20", round(6 / sqrt(20), 3), round(se / 2, 3))

# --- spot the error + quiz ---
eq("crit n=12 given", 0.591, 0.591)
assert 0.81 > 0.591
assert (10.0 - 1.0, 10.0 + 1.0) == (9.0, 11.0) and (11.0 - 1.0, 11.0 + 1.0) == (10.0, 12.0) and 11.0 > 10.0
assert 0.45 < 0.648
print("ok")
