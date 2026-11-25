# checks/math.fm.contingency.py: recomputes every number in "Chi-squared tests for independence".
# Standard library only: chi-squared percentage points by Simpson integration (substitution x = u^2) and bisection.
from math import isclose, sqrt, lgamma, exp
from functools import lru_cache


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def chi2_cdf(x, v, n=2000):
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


def analyse(T):
    r = [sum(row) for row in T]
    c = [sum(col) for col in zip(*T)]
    N = sum(r)
    E = [[ri * cj / N for cj in c] for ri in r]
    C = [[(T[i][j] - E[i][j]) ** 2 / E[i][j] for j in range(len(c))] for i in range(len(r))]
    return r, c, N, E, C, sum(map(sum, C)), (len(r) - 1) * (len(c) - 1)


def near(label, rows, want, tol):
    for i, (gr, wr) in enumerate(zip(rows, want)):
        for j, (g, w) in enumerate(zip(gr, wr)):
            eq(f"{label}[{i}][{j}]", g, w, tol)


# critical values used
for (v, p), want in {(1, 0.95): 3.841, (1, 0.99): 6.635, (2, 0.95): 5.991, (4, 0.95): 9.488, (4, 0.99): 13.277,
                     (6, 0.95): 12.592, (6, 0.99): 16.812, (8, 0.99): 20.090}.items():
    eq(f"cv {v} {p}", CV(p, v), want, 5e-4)

# ---- warm-up ----
eq("w1", 0.4 * 0.3, 0.12)
eq("w3", (12 - 15) ** 2 / 15 + (18 - 15) ** 2 / 15, 1.2)
assert 6 - 1 - 1 == 4

# ---- travel on time 2x2 ----
T = [[78, 22], [110, 90]]
r, c, N, E, C, X, v = analyse(T)
assert r == [100, 200] and c == [188, 112] and N == 300 and v == 1
eq("78/100", 78 / 100, 0.78)
eq("110/200", 110 / 200, 0.55)
near("e1 E", E, [[62.67, 37.33], [125.3, 74.67]], 5e-2)
eq("e1 E11", E[0][0], 62.67, 5e-3)
eq("e1 E21", E[1][0], 125.33, 5e-3)
near("e1 C", C, [[3.752, 6.298], [1.876, 3.149]], 6e-4)
eq("e1 X2", X, 15.07, 5e-3)
assert X > CV(0.95, 1) and X > CV(0.99, 1)
eq("e1 shortcut", 300 * (78 * 90 - 22 * 110) ** 2 / (100 * 200 * 188 * 112), X, 1e-9)

# ---- revision method 2x3 ----
T = [[28, 45, 17], [22, 60, 18]]
r, c, N, E, C, X, v = analyse(T)
assert r == [90, 100] and c == [50, 105, 35] and N == 190 and v == 2
near("e2 E", E, [[23.68, 49.74, 16.58], [26.32, 55.26, 18.42]], 6e-3)
near("e2 C", C, [[0.786, 0.451, 0.011], [0.708, 0.406, 0.010]], 6e-4)
eq("e2 X2", X, 2.37, 5e-3)
eq("e2 sum of rounded", 0.786 + 0.451 + 0.011 + 0.708 + 0.406 + 0.010, 2.372, 1e-9)
assert X < CV(0.95, 2)

# ---- age and transport, rows combined ----
T = [[28, 24, 28], [40, 32, 38], [20, 12, 36], [2, 2, 8]]
r, c, N, E, C, X, v = analyse(T)
assert r == [80, 110, 68, 12] and c == [90, 70, 110] and N == 270
eq("e3 E41", E[3][0], 4.00, 5e-3)
eq("e3 E42", E[3][1], 3.11, 5e-3)
eq("e3 E43", E[3][2], 4.89, 5e-3)
assert all(e < 5 for e in E[3])
T2 = [[28, 24, 28], [40, 32, 38], [22, 14, 44]]
assert T2[2] == [20 + 2, 12 + 2, 36 + 8]
r, c, N, E, C, X, v = analyse(T2)
assert r == [80, 110, 80] and v == 4
near("e3 E", E, [[26.67, 20.74, 32.59], [36.67, 28.52, 44.81], [26.67, 20.74, 32.59]], 6e-3)
near("e3 C", C, [[0.067, 0.512, 0.647], [0.303, 0.425, 1.036], [0.817, 2.191, 3.993]], 6e-4)
eq("e3 X2", X, 9.99, 5e-3)
assert X > CV(0.95, 4) == 9.488
assert min(map(min, E)) >= 5
# E of merged rows equal sum of the old E
Tf = [[28, 24, 28], [40, 32, 38], [20, 12, 36], [2, 2, 8]]
Ef = analyse(Tf)[3]
for j in range(3):
    eq("merged E additive", Ef[2][j] + Ef[3][j], E[2][j], 1e-9)
eq("e3 E last row", E[2][1], 20.74, 5e-3)
eq("e3 E last row car", E[2][2], 32.59, 5e-3)
# the trap: the uncombined statistic with nu = 6 does not reject
Xf = analyse(Tf)[5]
eq("e3 uncombined X2", Xf, 10.96, 5e-3)
assert CV(0.95, 6) == 12.592 and Xf < 12.592

# ---- Exam style: year group and travel 3x4 ----
T = [[36, 12, 30, 42], [38, 22, 40, 40], [20, 38, 56, 46]]
r, c, N, E, C, X, v = analyse(T)
assert r == [120, 140, 160] and c == [94, 72, 126, 128] and N == 420 and v == 6
eq("a E11", E[0][0], 26.86, 5e-3)
near("a E", E, [[26.86, 20.57, 36.00, 36.57], [31.33, 24.00, 42.00, 42.67], [35.81, 27.43, 48.00, 48.76]], 6e-3)
assert min(map(min, E)) >= 5
near("a C", C, [[3.112, 3.571, 1.000, 0.806], [1.418, 0.167, 0.095, 0.167], [6.980, 4.074, 1.333, 0.156]], 6e-4)
eq("a X2", X, 22.88, 5e-3)
eq("a X2 3sf", sf(X), 22.9)
assert X > CV(0.95, 6) and X > CV(0.99, 6)
mx = max(max(row) for row in C)
eq("a max", mx, 6.980, 6e-4)
assert C[2][0] == mx
eq("a E31", E[2][0], 35.81, 5e-3)
eq("a E32", E[2][1], 27.43, 5e-3)

# ---- Exam style: cars and towns, columns combined ----
T = [[46, 30, 12, 2], [50, 38, 14, 8], [44, 50, 22, 4]]
r, c, N, E, C, X, v = analyse(T)
assert r == [90, 110, 120] and c == [140, 118, 48, 14] and N == 320
eq("b E14", E[0][3], 3.94, 5e-3)
eq("b E24", E[1][3], 4.81, 5e-3)
eq("b E34", E[2][3], 5.25, 5e-3)
assert E[0][3] < 5 and E[1][3] < 5 and E[2][3] > 5
T2 = [[46, 30, 14], [50, 38, 22], [44, 50, 26]]
assert [12 + 2, 14 + 8, 22 + 4] == [14, 22, 26] and 14 + 22 + 26 == 62
r, c, N, E, C, X, v = analyse(T2)
assert c == [140, 118, 62] and v == 4
near("b E", E, [[39.38, 33.19, 17.44], [48.13, 40.56, 21.31], [52.50, 44.25, 23.25]], 6e-3)
assert min(map(min, E)) >= 5
near("b C", C, [[1.115, 0.306, 0.678], [0.073, 0.162, 0.022], [1.376, 0.747, 0.325]], 6e-4)
eq("b X2", X, 4.80, 5e-3)
assert X < CV(0.95, 4)
assert (3 - 1) * (4 - 1) == 6 and (3 - 1) * (3 - 1) == 4

# ---- Spot the error ----
T = [[2, 34, 44], [6, 50, 64], [2, 26, 72]]
r, c, N, E, C, X, v = analyse(T)
assert r == [80, 120, 100] and N == 300 and c == [10, 110, 180]
eq("s E1", E[0][0], 2.67, 5e-3)
eq("s E2", E[1][0], 4.00, 5e-3)
eq("s E3", E[2][0], 3.33, 5e-3)
T2 = [[2 + 34, 44], [6 + 50, 64], [2 + 26, 72]]
assert T2 == [[36, 44], [56, 64], [28, 72]]
r, c, N, E, C, X, v = analyse(T2)
assert v == 2
near("s E", E, [[32, 48], [48, 72], [40, 60]], 1e-9)
near("s C", C, [[0.500, 0.333], [1.333, 0.889], [3.600, 2.400]], 6e-4)
eq("s X2", X, 9.06, 5e-3)
eq("s X2 sum", 0.500 + 0.333 + 1.333 + 0.889 + 3.600 + 2.400, 9.055, 1e-9)
assert CV(0.95, 2) < X < CV(0.95, 4)
assert (3 - 1) * (3 - 1) == 4 and (3 - 1) * (2 - 1) == 2

# ---- Try ----
r, c, N, E, C, X, v = analyse([[24, 16], [36, 24]])
assert r == [40, 60] and c == [60, 40] and E == [[24, 16], [36, 24]] and X == 0
assert [a * b for a, b in [(1, 1), (3, 2), (2, 4), (2, 4)]] == [1, 6, 8, 8]
assert (3 - 1) * (5 - 1) == 8
# combining columns 1 and 2
assert round(3.2 + 12.8, 9) == 16.0 and round(4.8 + 19.2, 9) == 24.0
e = [3.2, 12.8, 14.0, 4.8, 19.2, 21.0]
assert min(e[:3]) < 5 and e[3] < 5 and e[4] > 5
# 2x2 test
r, c, N, E, C, X, v = analyse([[18, 12], [10, 20]])
assert r == [30, 30] and c == [28, 32]
near("t4 E", E, [[14, 16], [14, 16]], 1e-9)
eq("t4 X2", X, 4.29, 5e-3)
eq("t4 X2 sum", 16 / 14 + 1 + 16 / 14 + 1, X, 1e-9)
assert X > CV(0.95, 1)
# 2x3 test
r, c, N, E, C, X, v = analyse([[25, 35, 20], [15, 25, 30]])
assert r == [80, 70] and c == [40, 60, 50] and N == 150
near("t5 E", E, [[21.33, 32.00, 26.67], [18.67, 28.00, 23.33]], 6e-3)
near("t5 C", C, [[0.630, 0.281, 1.667], [0.720, 0.321, 1.905]], 6e-4)
eq("t5 X2", X, 5.52, 5e-3)
assert X < CV(0.95, 2)

# ---- Exam practice ----
# Q1
T = [[30, 25, 15], [20, 30, 30], [10, 25, 45]]
r, c, N, E, C, X, v = analyse(T)
assert r == [70, 80, 80] and c == [60, 80, 90] and N == 230 and v == 4
eq("q1 E", E[0][0], 18.26, 5e-3)
eq("q1 3sf", sf(E[0][0]), 18.3)
# Q2
T = [[45, 55], [30, 70]]
r, c, N, E, C, X, v = analyse(T)
assert c == [75, 125]
near("q2 E", E, [[37.5, 62.5], [37.5, 62.5]], 1e-9)
eq("q2 X2", X, 4.8, 1e-9)
eq("q2 sum", 1.5 + 0.9 + 1.5 + 0.9, 4.8)
eq("q2 shortcut", 200 * (45 * 70 - 55 * 30) ** 2 / (100 * 100 * 75 * 125), 4.8, 1e-9)
assert 45 * 70 - 55 * 30 == 1500 and 10000 * 9375 == 93750000
assert X < CV(0.99, 1) and X > CV(0.95, 1)
# Q3
T = [[3, 25, 52], [9, 38, 63], [8, 27, 65]]
r, c, N, E, C, X, v = analyse(T)
assert r == [80, 110, 100] and c == [20, 90, 180] and N == 290
eq("q3 min E", E[0][0], 5.52, 5e-3)
assert min(map(min, E)) > 5
near("q3 C", C, [[1.148, 0.001, 0.111], [0.264, 0.437, 0.408], [0.177, 0.525, 0.138]], 1e-3)
eq("q3 X2", X, 3.21, 5e-3)
assert X < CV(0.95, 4)
# Q4 missing cells
a = 60 - 18 - 22
b = 50 - 22
cc = 50 - a
assert (a, b, cc) == (20, 28, 30) and 32 + b + cc == 90 and 18 + 32 == 50
T = [[18, 22, 20], [32, 28, 30]]
r, c, N, E, C, X, v = analyse(T)
assert r == [60, 90] and c == [50, 50, 50]
near("q4 E", E, [[20, 20, 20], [30, 30, 30]], 1e-9)
eq("q4 X2", X, 0.667, 5e-4)
eq("q4 sum", 4 / 20 + 4 / 20 + 4 / 30 + 4 / 30, X, 1e-9)
assert X < CV(0.95, 2)
# Q5
T = [[30, 25, 15], [20, 30, 30], [10, 25, 45]]
r, c, N, E, C, X, v = analyse(T)
eq("q5 X2", X, 25.37, 5e-3)
eq("q5 X2 1dp", sf(X, 3), 25.4, 5e-2)
near("q5 C", C, [[7.55, 0.02, 5.61], [0.04, 0.17, 0.05], [5.66, 0.29, 5.99]], 6e-3)
assert X > CV(0.99, 4) == 13.277
eq("q5 E11", E[0][0], 18.3, 5e-2)
eq("q5 E31", E[2][0], 20.9, 5e-2)
eq("q5 E13", E[0][2], 27.4, 5e-2)
eq("q5 E33", E[2][2], 31.3, 5e-2)
assert C[0][0] > 7 and C[2][2] > 5.9
# Q6
T = [[3, 4, 7], [30, 42, 28], [26, 26, 38], [14, 22, 14]]
r, c, N, E, C, X, v = analyse(T)
assert r == [14, 100, 90, 50] and c == [73, 94, 87] and N == 254
eq("q6 E11", E[0][0], 4.02, 5e-3)
eq("q6 E13", E[0][2], 4.80, 5e-3)
assert E[0][0] < 5 and E[0][2] < 5 and E[0][1] > 5
T2 = [[33, 46, 35], [26, 26, 38], [14, 22, 14]]
assert [3 + 30, 4 + 42, 7 + 28] == [33, 46, 35] and sum(T2[0]) == 114
r, c, N, E, C, X, v = analyse(T2)
assert v == 4
near("q6 E", E, [[32.76, 42.19, 39.05], [25.87, 33.31, 30.83], [14.37, 18.50, 17.13]], 6e-3)
assert min(map(min, E)) >= 5
near("q6 C", C, [[0.002, 0.344, 0.420], [0.001, 1.603, 1.669], [0.010, 0.661, 0.571]], 1e-3)
eq("q6 X2", X, 5.28, 5e-3)
assert X < CV(0.95, 4)
# Q7
T = [[56, 24], [64, 56]]
r, c, N, E, C, X, v = analyse(T)
assert r == [80, 120] and c == [120, 80] and N == 200
eq("q7 P car", 80 / 200, 0.4)
eq("q7 P bike", 120 / 200, 0.6)
eq("q7 P both", 0.4 * 0.6, 0.24)
eq("q7 expected both", 200 * 0.24, 48)
near("q7 E", E, [[48, 32], [72, 48]], 1e-9)
near("q7 C", C, [[1.333, 2.000], [0.889, 1.333]], 6e-4)
eq("q7 X2", X, 5.56, 5e-3)
assert X > CV(0.95, 1)
eq("q7 cond1", 56 / 80, 0.7)
eq("q7 cond2", 64 / 120, 0.533, 5e-4)
# Q8
assert (3 - 1) * (5 - 1) == 8 and CV(0.99, 8) == 20.090 and 21.5 > 20.090
eq("q8 cv", chi2_inv(0.99, 8), 20.090, 5e-4)

# ---- Stretch ----
def shortcut(a, b, c_, d):
    R1, R2, C1, C2 = a + b, c_ + d, a + c_, b + d
    return (a + b + c_ + d) * (a * d - b * c_) ** 2 / (R1 * R2 * C1 * C2)


for T in ([[45, 55], [30, 70]], [[78, 22], [110, 90]], [[18, 12], [10, 20]]):
    eq("stretch1 general", shortcut(*T[0], *T[1]), analyse(T)[5], 1e-9)
# a - E11 = (ad - bc)/N symbolic spot-check
a_, b_, c2, d_ = 7, 5, 3, 11
N_ = a_ + b_ + c2 + d_
eq("stretch1 dev", a_ - (a_ + b_) * (a_ + c2) / N_, (a_ * d_ - b_ * c2) / N_, 1e-12)
# part 2
f = lambda a: shortcut(a, 40 - a, 30, 30)
for a in (0, 5, 17, 33):
    eq("stretch2 formula", f(a), 150 * (a - 20) ** 2 / ((a + 30) * (70 - a)), 1e-9)
assert 60 * (30 * 1) == 1800 and 100 * 3600 / (40 * 60) == 150
crit = CV(0.95, 1)
rej = [a for a in range(0, 41) if f(a) > crit]
assert rej == list(range(0, 13)) + list(range(28, 41)), rej
A2, B2, C2 = 150 + 3.841, -6000 - 3.841 * 40, 60000 - 3.841 * 2100
eq("stretch2 a2", A2, 153.841, 1e-9)
eq("stretch2 b", B2, -6153.64, 1e-9)
eq("stretch2 c", C2, 51933.9, 0.1)
disc = B2 * B2 - 4 * A2 * C2
r1, r2 = (-B2 - sqrt(disc)) / (2 * A2), (-B2 + sqrt(disc)) / (2 * A2)
eq("stretch2 r1", r1, 12.10, 5e-3)
eq("stretch2 r2", r2, 27.90, 5e-3)
eq("stretch2 a=20", f(20), 0)
eq("stretch2 recovery", 30 / 60, 0.5)
eq("stretch2 recovery A", 20 / 40, 0.5)

# ---- quiz ----
assert (4 - 1) * (5 - 1) == 12
eq("quiz E", 60 * 45 / 300, 9)
assert 60 * 45 == 2700
assert (3 - 1) * (3 - 1) == 4 and (4 - 1) * (3 - 1) == 6
assert 8.2 < CV(0.95, 4) and 8.2 > CV(0.95, 2)
print("ok")
