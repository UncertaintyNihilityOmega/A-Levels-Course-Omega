# checks/bio.variation.py: recomputes every number in the Variation and the t-test chapter.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data'))
from math import isclose, sqrt, comb
from statistics import mean, stdev
from crit import t_crit

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


def tstat(m1, s1, n1, m2, s2, n2):
    return abs(m1 - m2) / sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def crit(df):
    return round(t_crit(df), 2)


# --- Warm-up and the standard deviation example -----------------------------------------------------------
eq("warm-up mean 8 11 9 12 10", mean([8, 11, 9, 12, 10]), 10)
pods = [5, 7, 8, 6, 9, 7]
eq("pods mean", mean(pods), 7)
eq("pods sum of squares", sum((x - 7) ** 2 for x in pods), 10)
eq("pods s", sf(stdev(pods)), 1.41)
eq("pods 7 - 2s", round(7 - 2 * sqrt(2), 1), 4.2)
eq("pods 7 + 2s", round(7 + 2 * sqrt(2), 1), 9.8)
eq("try s of 10 12 14 16", sf(stdev([10, 12, 14, 16])), 2.58)

# --- Three-gene additive model ---------------------------------------------------------------------------
fr = [comb(6, k) for k in range(7)]
assert fr == [1, 6, 15, 20, 15, 6, 1] and sum(fr) == 64
eq("seven phenotypes", len(fr), 7)
eq("extra height with 6 contributing alleles", 6 * 2, 12)
# two-gene exam question: AaBb x AaBb, 5 g per capital letter
fr2 = [comb(4, k) for k in range(5)]
eq("exam: five masses", len(fr2), 5)
eq("exam: most common class has 6 of 16", max(fr2), 6)
eq("exam: 10 g for two capitals", 2 * 5, 10)
eq("exam: AABB 1/16", (1 / 4) * (1 / 4), 1 / 16)

# --- Leaves in sun and shade -------------------------------------------------------------------------------
sun = [42, 45, 38, 44, 47, 41, 43, 46]
shade = [52, 49, 55, 51, 48, 54, 50, 53, 56, 47]
eq("sun sum", sum(sun), 346)
eq("shade sum", sum(shade), 515)
eq("sun mean", mean(sun), 43.25)
eq("shade mean", mean(shade), 51.5)
eq("sun SS", sum((x - mean(sun)) ** 2 for x in sun), 59.5)
eq("shade SS", sum((x - mean(shade)) ** 2 for x in shade), 82.5)
eq("sun s", sf(stdev(sun)), 2.92)
eq("shade s", sf(stdev(shade)), 3.03)
eq("sun s^2", stdev(sun) ** 2, 8.5)
eq("shade s^2 to 4 s.f.", sf(stdev(shade) ** 2, 4), 9.167)
t = tstat(mean(sun), stdev(sun), 8, mean(shade), stdev(shade), 10)
eq("leaf t", sf(t), 5.86)
eq("denominator sum 1.0625 + 0.9167", round(8.5 / 8 + stdev(shade) ** 2 / 10, 4), 1.9792)
eq("denominator 1.407", sf(sqrt(8.5 / 8 + stdev(shade) ** 2 / 10), 4), 1.407)
eq("leaf df", 8 + 10 - 2, 16)
eq("leaf critical value", crit(16), 2.12)
eq("difference of means", 51.5 - 43.25, 8.25)
assert t > crit(16)

# --- Earthworms (not significant) -------------------------------------------------------------------------
tw = tstat(12.4, 1.6, 9, 10.9, 1.4, 8)
eq("worm 0.2844", round(1.6 ** 2 / 9, 4), 0.2844)
eq("worm 0.2450", round(1.4 ** 2 / 8, 4), 0.2450)
eq("worm denominator", sf(sqrt(1.6 ** 2 / 9 + 1.4 ** 2 / 8), 4), 0.7276)
eq("worm t", sf(tw), 2.06)
eq("worm df", 9 + 8 - 2, 15)
eq("worm critical value", crit(15), 2.13)
assert tw < crit(15)

# --- Drug and placebo ---------------------------------------------------------------------------------------
td = tstat(12.6, 2.22, 10, 9.0, 1.83, 10)
eq("drug 0.4928", round(2.22 ** 2 / 10, 4), 0.4928)
eq("placebo 0.3349", round(1.83 ** 2 / 10, 4), 0.3349)
eq("drug denominator", sf(sqrt(2.22 ** 2 / 10 + 1.83 ** 2 / 10), 4), 0.9098)
eq("drug t", sf(td), 3.96)
eq("drug df", 10 + 10 - 2, 18)
eq("drug critical value", crit(18), 2.10)
assert td > crit(18)

# --- Spot the error ---------------------------------------------------------------------------------------
eq("beech df", 8 + 8 - 2, 14)
eq("beech critical value", crit(14), 2.14)

# --- Practice -----------------------------------------------------------------------------------------------
eq("try df 12 and 9", 12 + 9 - 2, 19)
eq("quiz df 7 and 11", 7 + 11 - 2, 16)
eq("try t-crit 10 df", crit(10), 2.23)
eq("try t-crit 16 df (pain relief)", crit(16), 2.12)
beans = [4, 14, 33, 30, 15, 4]
eq("beans total 100", sum(beans), 100)
eq("beans peak 33", max(beans), 33)
fert = [27, 30, 26, 29, 24, 31, 28]
nofert = [23, 26, 21, 25, 24, 27, 22, 25]
eq("fert mean", sf(mean(fert), 4), 27.86)
eq("fert s", sf(stdev(fert)), 2.41)
eq("nofert mean 24.125 (24.13 rounded half up)", mean(nofert), 24.125)
eq("nofert s", sf(stdev(nofert)), 2.03)
eq("fert 0.8297", round(2.41 ** 2 / 7, 4), 0.8297)
eq("nofert 0.5151", round(2.03 ** 2 / 8, 4), 0.5151)
eq("fert denominator", sf(sqrt(2.41 ** 2 / 7 + 2.03 ** 2 / 8), 4), 1.160)
eq("fert difference 3.73", round(27.86 - 24.13, 2), 3.73)
eq("fert t from the raw data", sf(tstat(mean(fert), stdev(fert), 7, mean(nofert), stdev(nofert), 8)), 3.22)
eq("fert df", 7 + 8 - 2, 13)
eq("fert critical value", crit(13), 2.16)
tbl = {11: 2.20, 12: 2.18, 13: 2.16, 14: 2.14, 15: 2.13}
for df, c in tbl.items():
    eq(f"printed table df {df}", crit(df), c)

# --- Stretch: SE, CI and the overlap --------------------------------------------------------------------------
se = 4.0 / sqrt(12)
eq("SE 1.15", sf(se, 3), 1.15)
eq("CI 1 low", round(48 - 2 * se, 1), 45.7)
eq("CI 1 high", round(48 + 2 * se, 1), 50.3)
eq("CI 2 low", round(52 - 2 * se, 1), 49.7)
eq("CI 2 high", round(52 + 2 * se, 1), 54.3)
t2 = tstat(52, 4.0, 12, 48, 4.0, 12)
eq("stretch t", sf(t2), 2.45)
eq("stretch denominator", sf(sqrt(16 / 12 + 16 / 12), 4), 1.633)
eq("stretch df", 12 + 12 - 2, 22)
eq("stretch critical value", crit(22), 2.07)
assert t2 > crit(22) and (52 - 2 * se) < (48 + 2 * se)
P = [61, 63, 60, 62, 64, 62]
Q = [58, 66, 52, 71, 49, 76]
eq("antlers P mean", mean(P), 62)
eq("antlers Q mean", mean(Q), 62)
eq("antlers P s about 1.4", sf(stdev(P), 2), 1.4)
eq("antlers Q s about 11", round(stdev(Q)), 11)

# --- Figure data ------------------------------------------------------------------------------------------------
eq("blood groups total", sum([84, 76, 28, 12]), 200)
eq("heights total", sum([2, 6, 14, 24, 26, 16, 8, 4]), 100)

print("ok")
