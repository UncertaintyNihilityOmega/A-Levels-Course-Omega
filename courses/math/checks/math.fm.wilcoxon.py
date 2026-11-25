# checks/math.fm.wilcoxon.py: recomputes every number in "Wilcoxon tests".
# Standard library only: exact distributions by counting all rank subsets; normal from NormalDist.
from math import comb, sqrt, isclose
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from statistics import NormalDist

N = NormalDist()


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def r(x, d):
    return round(float(x), d)


def cdf(n, k):
    return F(sum(comb(n, i) for i in range(0, k + 1)), 2**n)


def ranks(vals):
    s = sorted(vals)
    return [s.index(v) + 1 for v in vals]


def signed(d):
    a = [abs(x) for x in d]
    assert len(set(a)) == len(a), "tied |d|"
    rk = ranks(a)
    P = sum(k for k, x in zip(rk, d) if x > 0)
    Q = sum(k for k, x in zip(rk, d) if x < 0)
    n = len(d)
    assert P + Q == n * (n + 1) // 2
    return rk, P, Q


def sr_dist(n):
    c = [0] * (n * (n + 1) // 2 + 1)
    c[0] = 1
    for k in range(1, n + 1):
        for s in range(len(c) - 1, k - 1, -1):
            c[s] += c[s - k]
    return c


def sr_crit(n, a):
    c = sr_dist(n)
    tot = 2**n
    cum = 0
    best = None
    for t in range(len(c)):
        cum += c[t]
        if F(cum, tot) <= a:
            best = t
        else:
            break
    return best


def rs_crit(m, n, a):
    c = Counter(sum(s) for s in combinations(range(1, m + n + 1), m))
    tot = comb(m + n, m)
    cum = 0
    best = None
    for w in range(m * (m + 1) // 2, m * (2 * n + m + 1) // 2 + 1):
        cum += c.get(w, 0)
        if F(cum, tot) <= a:
            best = w
        else:
            break
    return best


def rsum(A, B):
    allv = sorted(A + B)
    rk = {v: i + 1 for i, v in enumerate(allv)}
    return sum(rk[v] for v in A), sum(rk[v] for v in B)


LV = [F(5, 100), F(25, 1000), F(1, 100), F(5, 1000)]

# warm-up
assert cdf(10, 2) == F(56, 1024)
assert 12 * 13 // 2 == 78
z = (88.5 - 150) / 35
eq("wu z", sf(z, 4), -1.757, 1e-12)
eq("wu p", sf(N.cdf(z), 3), 0.0394, 1e-12)

# ranking example
vals = [14.2, 9.8, 17.5, 11.0, 12.6, 9.1]
assert ranks(vals) == [5, 2, 6, 3, 4, 1] and sum(ranks(vals)) == 21

# sets A and B
for d, pos in (([1, 2, -9, -8, -7], 3), ([9, 8, -1, -2, -7], 9)):
    rk = ranks([abs(x) for x in d])
    assert sum(k for k, x in zip(rk, d) if x > 0) == pos

# signed-rank table
tab = {6: [2, 0, None, None], 7: [3, 2, 0, None], 8: [5, 3, 1, 0], 9: [8, 5, 3, 1], 10: [10, 8, 5, 3],
       11: [13, 10, 7, 5], 12: [17, 13, 9, 7], 13: [21, 17, 12, 9], 14: [25, 21, 15, 12], 15: [30, 25, 19, 15],
       16: [35, 29, 23, 19], 17: [41, 34, 27, 23], 18: [47, 40, 32, 27], 19: [53, 46, 37, 32], 20: [60, 52, 43, 37]}
for n, row in tab.items():
    assert [sr_crit(n, a) for a in LV] == row, n

# n = 4 distribution
assert sr_dist(4) == [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1]
eq("n4 P<=1", float(F(2, 16)), 0.125)
mean4 = sum(s * c for s, c in enumerate(sr_dist(4))) / 16
var4 = sum((s - mean4) ** 2 * c for s, c in enumerate(sr_dist(4))) / 16
eq("mean n=4", mean4, 4 * 5 / 4)
eq("var n=4", var4, 4 * 5 * 9 / 24)
for n in (5, 7, 10):
    c = sr_dist(n)
    tot = 2**n
    mu = sum(s * k for s, k in enumerate(c)) / tot
    va = sum((s - mu) ** 2 * k for s, k in enumerate(c)) / tot
    eq(f"proof mean n={n}", mu, n * (n + 1) / 4)
    eq(f"proof var n={n}", va, n * (n + 1) * (2 * n + 1) / 24)

# battery example
x = [44, 48, 51, 43, 41, 53, 46, 42, 45]
d = [v - 50 for v in x]
rk, P, Q = signed(d)
assert rk == [6, 2, 1, 7, 9, 3, 4, 8, 5] and P == 4 and Q == 41
assert sr_crit(9, F(25, 1000)) == 5 and min(P, Q) <= 5

# egg example
eggs = [56, 61, 52, 62, 57, 50, 55, 53]
d = [v - 60 for v in eggs]
rk, P, Q = signed(d)
assert d == [-4, 1, -8, 2, -3, -10, -5, -7] and rk == [4, 1, 7, 2, 3, 8, 5, 6] and P == 3 and Q == 33
assert sr_crit(8, F(5, 100)) == 5 and P <= 5

# matched pairs, drivers
bef = [312, 295, 340, 301, 288, 325, 310, 297, 333, 318]
aft = [298, 286, 343, 279, 281, 307, 315, 286, 308, 302]
d = [b - a for b, a in zip(bef, aft)]
assert d == [14, 9, -3, 22, 7, 18, -5, 11, 25, 16]
rk, P, Q = signed(d)
assert rk == [6, 4, 1, 9, 3, 8, 2, 5, 10, 7] and Q == 3 and P == 52
assert sr_crit(10, F(5, 100)) == 10
assert cdf(10, 2) == F(56, 1024)
eq("drivers sign", r(cdf(10, 2), 4), 0.0547, 1e-12)

# normal approximation, n = 24
mu = 24 * 25 / 4
var = 24 * 25 * 49 / 24
assert mu == 150 and var == 1225
z = (88.5 - mu) / sqrt(var)
eq("n24 z", sf(z, 4), -1.757, 1e-12)
eq("n24 p", sf(N.cdf(z), 3), 0.0394, 1e-12)
eq("n24 z wrong cc", sf((87.5 - mu) / sqrt(var), 4), -1.786, 1e-12)

# rank-sum tables
t5 = {3: [6, 6, 7, 8, 8, 9], 4: [None, 11, 12, 13, 14, 15], 5: [None, None, 19, 20, 21, 23], 6: [None] * 3 + [28, 29, 31],
      7: [None] * 4 + [39, 41], 8: [None] * 5 + [51]}
t25 = {3: [None, None, 6, 7, 7, 8], 4: [None, 10, 11, 12, 13, 14], 5: [None, None, 17, 18, 20, 21],
       6: [None] * 3 + [26, 27, 29], 7: [None] * 4 + [36, 38], 8: [None] * 5 + [49]}
t1 = {3: [None, None, None, None, 6, 6], 4: [None, None, 10, 11, 11, 12], 5: [None, None, 16, 17, 18, 19],
      6: [None] * 3 + [24, 25, 27], 7: [None] * 4 + [34, 35], 8: [None] * 5 + [45]}
for tbl, lv in ((t5, LV[0]), (t25, LV[1]), (t1, LV[2])):
    for m, row in tbl.items():
        for j, n in enumerate(range(3, 9)):
            if n < m:
                continue
            # a dash in the chapter table means "no rejection possible"
            assert rs_crit(m, n, lv) == row[j], (m, n, lv, rs_crit(m, n, lv), row[j])

# machines X and Y
X = [41, 38, 47, 52, 44, 49, 40, 55]
Y = [36, 43, 39, 35, 46, 37]
Rm, Rn = rsum(Y, X)
assert Rm == 29 and 6 * 15 - Rm == 61 and Rn == 76 and Rm + Rn == 105
assert rs_crit(6, 8, F(25, 1000)) == 29
yr = sorted(range(1, 15))
allv = sorted(X + Y)
assert [allv.index(v) + 1 for v in sorted(Y)] == [1, 2, 3, 5, 8, 10]

# rank-sum normal approximation (12, 15)
m, n = 12, 15
mu = m * (m + n + 1) / 2
var = m * n * (m + n + 1) / 12
assert mu == 168 and var == 420
z = (128.5 - mu) / sqrt(var)
eq("rs z", sf(z, 4), -1.927, 1e-12)
eq("rs p", sf(N.cdf(z), 3), 0.0270, 1e-12)
assert N.cdf(z) > 0.025 and z > -1.959963984540054

# sign test on 11 differences
d11 = [0.4, 0.9, 0.3, 1.1, 0.2, -0.1, 0.6, 7.8, 0.5, -0.3, 0.8]
assert sum(1 for v in d11 if v > 0) == 9
assert cdf(11, 2) == F(67, 2048)
eq("d11 p", r(cdf(11, 2), 4), 0.0327, 1e-12)

# spot the error
d = [2, -9, 4, 1, -3, 6, 5]
rk, P, Q = signed(d)
assert P == 18 and Q == 10 and sr_crit(7, F(5, 100)) == 3
assert sorted(d)[:2] == [-9, -3]  # the student's ranks 1 and 2 give 3

# practice
assert 31 > 17 and ranks([31, 17, 24, 40, 12]) == [4, 2, 3, 5, 1]
rk, P, Q = signed([5, -2, 9, -4, 1, 7])
assert P == 16 and Q == 5
assert sr_crit(12, F(25, 1000)) == 13
assert 5 * 13 == 65 and 65 - 36 == 29
assert 30 * 31 / 4 == 232.5 and 30 * 31 * 61 / 24 == 2363.75

# exam practice
d = [243 - 250, 261 - 250, 238 - 250, 255 - 250, 247 - 250, 236 - 250, 259 - 250, 249 - 250]
assert d == [-7, 11, -12, 5, -3, -14, 9, -1]
rk, P, Q = signed(d)
assert rk == [4, 6, 7, 3, 2, 8, 5, 1] and P == 14 and Q == 22 and sr_crit(8, F(25, 1000)) == 3
A = [9, 12, 10, 8]
B = [14, 15, 17, 22, 18, 11]
Rm, Rn = rsum(A, B)
assert Rm == 11 and 4 * 11 - Rm == 33 and rs_crit(4, 6, F(5, 100)) == 13
t1s = [82, 75, 91, 68, 77, 85, 72, 88, 79]
t2s = [78, 77, 83, 65, 70, 86, 60, 79, 73]
d = [a - b for a, b in zip(t1s, t2s)]
assert d == [4, -2, 8, 3, 7, -1, 12, 9, 6]
rk, P, Q = signed(d)
assert rk == [4, 2, 7, 3, 6, 1, 9, 8, 5] and Q == 3 and P == 42 and sr_crit(9, F(25, 1000)) == 5
A = [31, 25, 26, 29, 34]
B = [27, 36, 42, 33, 40, 45, 39]
Rm, Rn = rsum(A, B)
assert Rm == 19 and 5 * 13 - Rm == 46 and rs_crit(5, 7, F(25, 1000)) == 20
allv = sorted(A + B)
assert allv == [25, 26, 27, 29, 31, 33, 34, 36, 39, 40, 42, 45]
z = (150.5 - 232.5) / sqrt(2363.75)
eq("q5 z", sf(z, 4), -1.687, 1e-12)
assert z < -1.6448536269514722
bef = [61, 48, 70, 55, 62, 77, 53, 66, 74]
aft = [55, 50, 61, 51, 63, 66, 46, 63, 62]
d = [b - a for b, a in zip(bef, aft)]
assert d == [6, -2, 9, 4, -1, 11, 7, 3, 12]
rk, P, Q = signed(d)
assert rk == [5, 2, 7, 4, 1, 8, 6, 3, 9] and Q == 3 and P == 42 and sr_crit(9, F(5, 100)) == 8
assert cdf(9, 2) == F(46, 512)
eq("q6 sign", r(cdf(9, 2), 4), 0.0898, 1e-12)
m, n = 11, 14
mu = m * (m + n + 1) / 2
var = m * n * (m + n + 1) / 12
assert mu == 143
eq("q7 var", sf(var, 5), 333.67, 1e-12)
z = (175.5 - mu) / sqrt(var)
eq("q7 z", sf(z, 4), 1.779, 1e-12)
eq("q7 p", sf(1 - N.cdf(z), 3), 0.0376, 1e-12)
assert 1 - N.cdf(z) < 0.05

# stretch
assert F(1, 32) > F(25, 1000) and F(1, 64) <= F(25, 1000) and F(2, 64) > F(25, 1000)
eq("st 1/32", 1 / 32, 0.03125)
eq("st 1/64", sf(1 / 64, 3), 0.0156, 1e-12)
subs = [s for k in range(0, 4) for s in combinations(range(1, 8), k) if sum(s) <= 2]
assert sorted(subs) == [(), (1,), (2,)]
assert F(3, 128) == F(sum(1 for k in range(0, 4) for s in combinations(range(1, 8), k) if sum(s) <= 2), 128)
eq("st 3/128", sf(3 / 128, 3), 0.0234, 1e-12)
eq("st 5/128", sf(5 / 128, 2), 0.039, 1e-12)
assert sum(1 for k in range(0, 4) for s in combinations(range(1, 8), k) if sum(s) <= 3) == 5
assert sr_crit(7, F(25, 1000)) == 2
assert sum(1 for s in combinations(range(1, 7), 3) if sum(s) <= 6) == 1 and comb(6, 3) == 20
assert rs_crit(3, 3, F(5, 100)) == 6 and rs_crit(3, 3, F(25, 1000)) is None

# quiz
assert 10 * 11 // 2 - 17 == 38
assert 30 * 31 / 4 == 232.5 and 30 * 31 / 2 == 465
print("ok")
