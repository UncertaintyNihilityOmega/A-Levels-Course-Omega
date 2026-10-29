# checks/bio.biodiversity.py: recomputes every number in the Biodiversity and sampling chapter.
import os, sys
from math import isclose, sqrt
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
from crit import r_crit

n_checks = 0


def eq(label, got, want, tol=1e-9):
    global n_checks
    n_checks += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def ranks(v):
    """Rank with the smallest = 1; ties get the mean of the ranks they would have had."""
    s = sorted(v)
    return [sum(i + 1 for i, y in enumerate(s) if y == x) / s.count(x) for x in v]


def spearman(x, y):
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    D = [a - b for a, b in zip(rx, ry)]
    assert abs(sum(D)) < 1e-9
    sd2 = sum(d * d for d in D)
    return rx, ry, D, sd2, 1 - 6 * sd2 / (n ** 3 - n)


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sx = sqrt(sum((a - mx) ** 2 for a in x) / (n - 1))
    sy = sqrt(sum((a - my) ** 2 for a in y) / (n - 1))
    sxy = sum(a * b for a, b in zip(x, y))
    return mx, my, sx, sy, sxy, (sxy - n * mx * my) / ((n - 1) * sx * sy)


def simpson(counts):
    N = sum(counts)
    return 1 - sum((c / N) ** 2 for c in counts)


# --- running mean (daisy cover) -------------------------------------------------------------------------
cover = [30, 18, 26, 34, 22, 28, 24, 26, 25, 27]
run = [sum(cover[:i + 1]) / (i + 1) for i in range(len(cover))]
eq("run 1", round(run[0], 1), 30.0)
eq("run 2", round(run[1], 1), 24.0)
eq("run 3", round(run[2], 1), 24.7)
eq("run 4", round(run[3], 1), 27.0)
eq("run 5", round(run[4], 1), 26.0)
eq("run 6", round(run[5], 1), 26.3)
eq("run 7", round(run[6], 1), 26.0)
eq("run 8", round(run[7], 1), 26.0)
eq("run 9", round(run[8], 1), 25.9)
eq("run 10", round(run[9], 1), 26.0)
eq("run max after 5", round(max(run[4:]), 1), 26.3)
eq("run min after 5", round(min(run[4:]), 1), 25.9)
eq("run change first four", round(max(run[:4]) - min(run[:4]), 1), 6.0)

# --- quadrats: daisies -----------------------------------------------------------------------------------
eq("daisy freq", 14 / 20 * 100, 70)
eq("daisy area sampled", 20 * 0.25, 5.0)
eq("daisy density", 84 / 5.0, 16.8)
eq("daisy field", 16.8 * 2400, 40320, 1e-6)
# --- Lincoln: shrimps
eq("shrimp N", 48 * 60 / 12, 240)
eq("shrimp check one fifth", 12 / 60, 0.2)
eq("shrimp check x5", 48 * 5, 240)
eq("beans N", 50 * 60 / 10, 300)

# --- Simpson: river -----------------------------------------------------------------------------------------
up, down = [24, 18, 21, 20, 17], [62, 28, 6, 2, 2]
eq("up N", sum(up), 100)
eq("down N", sum(down), 100)
eq("up sum squares", sum((c / 100) ** 2 for c in up), 0.2030, 1e-9)
eq("up D", round(simpson(up), 3), 0.797)
eq("down sum squares", sum((c / 100) ** 2 for c in down), 0.4672, 1e-9)
eq("down D", round(simpson(down), 3), 0.533)
eq("down sludge worms percent", 62 / 100 * 100, 62)
# spot the error
eq("spot N", 30 + 20 + 10, 60)
sq = (30 / 60) ** 2 + (20 / 60) ** 2 + (10 / 60) ** 2
eq("spot sum squares", round(sq, 4), 0.3889)
eq("spot D", round(1 - sq, 3), 0.611)
eq("spot terms", round((20 / 60) ** 2, 4), 0.1111)
eq("spot term 3", round((10 / 60) ** 2, 4), 0.0278)

# --- Spearman: rushes ---------------------------------------------------------------------------------------------
water = [4, 6, 6, 9, 11, 13, 15, 15]
rush = [2, 5, 3, 8, 7, 12, 14, 10]
rx, ry, D, sd2, rs = spearman(water, rush)
assert rx == [1, 2.5, 2.5, 4, 5, 6, 7.5, 7.5], rx
assert ry == [1, 3, 2, 5, 4, 7, 8, 6], ry
assert D == [0, -0.5, 0.5, -1, 1, -1, -0.5, 1.5], D
n_checks += 3
eq("rushes sum D2", sd2, 6.0)
eq("rushes n3-n", 8 ** 3 - 8, 504)
eq("rushes rs", round(rs, 3), 0.929)
eq("rushes critical 0.738 less than rs", float(rs > 0.738), 1.0)

# --- Pearson: moss ----------------------------------------------------------------------------------------------------
light = [1, 2, 3, 4, 5, 6, 7, 8]
moss = [3, 5, 4, 8, 7, 10, 9, 12]
mx, my, sx, sy, sxy, r = pearson(light, moss)
eq("moss sum x", sum(light), 36)
eq("moss sum y", sum(moss), 58)
eq("moss mean x", mx, 4.5)
eq("moss mean y", my, 7.25)
eq("moss sum xy", sxy, 311)
eq("moss sx", round(sx, 3), 2.449)
eq("moss sy", round(sy, 3), 3.105)
eq("moss numerator", sxy - 8 * mx * my, 50)
eq("moss 8*4.5*7.25", 8 * 4.5 * 7.25, 261)
eq("moss denominator", round(7 * 2.449 * 3.105, 2), 53.23)
eq("moss r", round(r, 3), 0.939)
eq("moss r from rounded", round(50 / 53.23, 3), 0.939)
eq("pearson critical n=8", round(r_crit(8), 3), 0.707)
eq("pearson critical n=10", round(r_crit(10), 3), 0.632)

# --- practice ---------------------------------------------------------------------------------------------------------------
eq("buttercup freq", 18 / 30 * 100, 60)
eq("buttercup density", 66 / (30 * 0.25), 8.8)
eq("buttercup field", 8.8 * 1800, 15840, 1e-6)
eq("snails N", 35 * 28 / 7, 140)
eq("sim 15 15 30", 1 - ((15 / 60) ** 2 * 2 + (30 / 60) ** 2), 0.625)
eq("ranks 3 5 5 8", sum(ranks([3, 5, 5, 8])), 10)
assert ranks([3, 5, 5, 8]) == [1, 2.5, 2.5, 4]
n_checks += 1
# exam practice
eq("clover freq", 20 / 25 * 100, 80)
eq("clover density", 150 / 25, 6.0)
eq("lawn area", 20 * 15, 300)
eq("woodlice N", 55 * 40 / 8, 275)
X = [12, 15, 9, 14, 10]
Y = [40, 8, 6, 4, 2]
eq("beetles X N", sum(X), 60)
eq("beetles Y N", sum(Y), 60)
eq("beetles X sq 1", round((12 / 60) ** 2, 4), 0.04)
eq("beetles X sq 2", round((15 / 60) ** 2, 4), 0.0625)
eq("beetles X sq 3", round((9 / 60) ** 2, 4), 0.0225)
eq("beetles X sq 4", round((14 / 60) ** 2, 4), 0.0544)
eq("beetles X sq 5", round((10 / 60) ** 2, 4), 0.0278)
eq("beetles X sum", round(1 - simpson(X), 4), 0.2072)
eq("beetles X D", round(simpson(X), 3), 0.793)
eq("beetles Y D", round(simpson(Y), 2), 0.52)
eq("beetles Y 40 of 60", 40 / 60, 2 / 3)
# slugs
dist = [12, 18, 25, 25, 31, 40, 47]
slug = [34, 29, 30, 22, 25, 14, 9]
rx, ry, D, sd2, rs = spearman(dist, slug)
assert rx == [1, 2, 3.5, 3.5, 5, 6, 7] and ry == [7, 5, 6, 3, 4, 2, 1] and D == [-6, -3, -2.5, 0.5, 1, 4, 6], (rx, ry, D)
n_checks += 1
eq("slugs sum D2", sd2, 104.5)
eq("slugs n3-n", 7 ** 3 - 7, 336)
eq("slugs rs", round(rs, 3), -0.866)
# limpets (Pearson from sums)
eq("limpets n x mean x mean y", 10 * 11.0 * 45.1, 4961, 1e-6)
eq("limpets numerator", 4374 - 4961, -587)
eq("limpets denominator", round(9 * 6.055 * 11.20, 1), 610.3)
eq("limpets r", round(-587 / 610.3, 3), -0.962)
x2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y2 = [62, 55, 58, 47, 50, 41, 38, 40, 29, 31]
mx, my, sx, sy, sxy, r = pearson(x2, y2)
eq("limpets xbar", mx, 11.0)
eq("limpets ybar", my, 45.1)
eq("limpets sx", round(sx, 3), 6.055)
eq("limpets sy", round(sy, 2), 11.20)
eq("limpets sxy", sxy, 4374)
eq("limpets r exact", round(r, 3), -0.962)
# butterflies
eq("butterfly year 1", 30 * 25 / 5, 150)
eq("butterfly year 5", 24 * 20 / 8, 60)
eq("butterfly decrease percent", (150 - 60) / 150 * 100, 60)
# stretch: altitude and insects
alt = [200, 300, 500, 500, 700, 800, 1000, 1200, 1400, 1600]
sp = [41, 38, 29, 33, 30, 22, 25, 15, 17, 9]
rx, ry, D, sd2, rs = spearman(alt, sp)
assert rx == [1, 2, 3.5, 3.5, 5, 6, 7, 8, 9, 10], rx
assert ry == [10, 9, 6, 8, 7, 4, 5, 2, 3, 1], ry
n_checks += 2
eq("altitude sum D2", sd2, 321.5)
eq("altitude n3-n", 10 ** 3 - 10, 990)
eq("altitude rs", round(rs, 3), -0.948)
# stretch: Simpson A and B
A = [97, 1, 1, 1]
B = [50, 50]
eq("simpson A sum", round(0.97 ** 2 + 3 * 0.01 ** 2, 4), 0.9412)
eq("simpson A D", round(simpson(A), 3), 0.059)
eq("simpson B D", simpson(B), 0.5)
# quiz
eq("quiz lincoln", 40 * 30 / 10, 120)
eq("quiz lincoln wrong", round(40 * 10 / 30), 13)
eq("quiz lincoln 7.5", 30 * 10 / 40, 7.5)
eq("quiz lincoln 1200", 40 * 30, 1200)
eq("quiz simpson", round(simpson([70, 30]), 2), 0.42)
eq("quiz simpson sum of squares", round(0.7 ** 2 + 0.3 ** 2, 2), 0.58)
# random coordinates lie inside the 20 x 20 m area
for x, y in [(3, 16), (11, 7), (17, 13), (6, 4), (14, 18)]:
    assert 0 <= x <= 20 and 0 <= y <= 20
    n_checks += 1
print("ok", n_checks)
