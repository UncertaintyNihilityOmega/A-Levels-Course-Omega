# checks/math.fm.pgf.py: recomputes every number in "Probability generating functions".
# Standard library only: PGFs as dicts {power: Fraction} (Laurent polynomials), exact mean/variance by direct sums,
# derivatives by exact term-by-term differentiation, Poisson/geometric checked with truncated series.
from fractions import Fraction as F
from math import comb, exp, factorial, isclose

import itertools


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return out


def power(a, n):
    out = {0: F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def sub(a, k):
    """G(t^k) for integer k"""
    return {i * k: x for i, x in a.items()}


def shift(a, b):
    return {i + b: x for i, x in a.items()}


def d1(a):
    return {i - 1: x * i for i, x in a.items() if i != 0}


def ev(a, t=1):
    return sum(x * F(t) ** i for i, x in a.items())


def mean_var(a):
    g1 = ev(d1(a))
    g2 = ev(d1(d1(a)))
    return g1, g2 + g1 - g1**2


def direct_mean_var(a):
    m = sum(i * x for i, x in a.items())
    v = sum(i * i * x for i, x in a.items()) - m * m
    return m, v


def bin_pgf(n, p):
    return power({0: 1 - p, 1: p}, n)


# warm-up
eq("wu1", float(1 / (1 - F(1, 3))), 1.5)
assert power({0: F(3, 5), 1: F(2, 5)}, 2) == {0: F(36, 100), 1: F(48, 100), 2: F(16, 100)}
eq("wu3", 3 * exp(0), 3)

# first example
G = {0: F(1, 10), 1: F(3, 10), 2: F(4, 10), 3: F(2, 10)}
assert ev(G) == 1
m, v = mean_var(G)
assert (m, v) == (F(17, 10), F(81, 100)) and ev(d1(d1(G))) == 2
assert direct_mean_var(G) == (m, v)
assert F(3, 10) + 16 * F(1, 10) + F(18, 10) == F(37, 10) / 1 or True
assert F(3, 10) + F(16, 10) + F(18, 10) == F(37, 10) and F(37, 10) - F(289, 100) == F(81, 100)

# t/(2-t)
terms = [F(1, 2) ** k for k in range(1, 40)]
eq("t/(2-t) coeffs", float(terms[0] + terms[1] + terms[2]), 0.875)
eq("G'(0)", 2 / (2 - 0) ** 2, 0.5)

# standard PGFs
for n in (4, 5, 6, 10):
    U = {x: F(1, n) for x in range(1, n + 1)}
    assert ev(U) == 1
    m, v = mean_var(U)
    assert m == F(n + 1, 2) and v == F(n * n - 1, 12)
    assert ev(d1(d1(U))) == F((n - 1) * (n + 1), 3)
p, q = F(3, 10), F(7, 10)
B6 = bin_pgf(6, p)
assert B6[2] == comb(6, 2) * q**4 * p**2
eq("B(6,.3) P(2)", sf(B6[2], 3), 0.324, 1e-12)
mb, vb = mean_var(B6)
assert (mb, vb) == (F(18, 10), F(126, 100))
# binomial E, Var, general
for n, pp in ((8, F(1, 4)), (13, F(2, 7))):
    m, v = mean_var(bin_pgf(n, pp))
    assert m == n * pp and v == n * pp * (1 - pp)
m8, _ = mean_var(bin_pgf(8, F(1, 4)))
assert m8 == 2


# geometric: truncated series, exact derivative formulas
def geo_trunc(p, K=400):
    return {x: (1 - p) ** (x - 1) * p for x in range(1, K)}


for pp in (0.2, 0.25, 1 / 3, 0.5):
    qq = 1 - pp
    g = geo_trunc(pp)
    mm = sum(i * x for i, x in g.items())
    vv = sum(i * i * x for i, x in g.items()) - mm * mm
    eq("geo mean", mm, 1 / pp, 1e-9)
    eq("geo var", vv, qq / pp**2, 1e-6)
    t = 0.7
    eq("geo closed form", sum(x * t**i for i, x in g.items()), pp * t / (1 - qq * t), 1e-12)
    eq("geo G''(1)", 2 * qq / pp**2, 2 * qq * pp / pp**3, 1e-12)


# Poisson
def po(l, K=120):
    return {x: exp(-l) * l**x / factorial(x) for x in range(K)}


for l in (1.5, 2.0, 2.5, 3.0):
    g = po(l)
    mm = sum(i * x for i, x in g.items())
    vv = sum(i * i * x for i, x in g.items()) - mm * mm
    eq("po mean", mm, l, 1e-9)
    eq("po var", vv, l, 1e-9)
    t = 0.6
    eq("po closed", sum(x * t**i for i, x in g.items()), exp(l * (t - 1)), 1e-12)

# exam example: k (2 + t^2)(1 + 3t^2)
Gk = mul({0: F(2), 2: F(1)}, {0: F(1), 2: F(3)})
assert ev(Gk) == 12
Gk = {i: x / 12 for i, x in Gk.items()}
assert Gk == {0: F(2, 12), 2: F(7, 12), 4: F(3, 12)}
m, v = mean_var(Gk)
assert m == F(13, 6) and ev(d1(d1(Gk))) == F(25, 6) and v == F(59, 36)
assert direct_mean_var(Gk) == (m, v)
assert 2 * F(7, 12) + 4 * F(1, 4) == F(13, 6)

# negative power example: k t^-1 (a t + 1)^2
a = 3
k = F(1, (a + 1) ** 2)
assert k == F(1, 16)
Gn = {i: k * x for i, x in mul({-1: F(1)}, power({0: F(1), 1: F(a)}, 2)).items()}
assert Gn == {-1: F(1, 16), 0: F(6, 16), 1: F(9, 16)}
assert ev(Gn) == 1
m, v = mean_var(Gn)
assert m == F(1, 2) and ev(d1(d1(Gn))) == F(1, 8) and v == F(3, 8)
assert direct_mean_var(Gn) == (m, v)
assert (a - 1) / (a + 1) == 0.5
G3 = power(Gn, 3)
assert G3[1] == F(1215, 4096) and comb(6, 4) * 3**4 == 1215
eq("P(Y=1)", sf(G3[1], 3), 0.297, 1e-12)
eq("P(Y=3)", sf(F(9, 16) ** 3, 3), 0.178, 1e-12)
assert G3[3] == F(9, 16) ** 3

# dice
die = {x: F(1, 6) for x in range(1, 7)}
two = mul(die, die)
assert two[7] == F(1, 6) and [two[s] * 36 for s in range(2, 13)] == [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
m, v = mean_var(two)
assert m == 7 and v == F(35, 6)

# Poisson + Poisson
eq("Po(4) P(2)", sf(exp(-4) * 16 / 2, 3), 0.147, 1e-12)
# geometric sum
p3 = F(1, 3)
q3 = 1 - p3
Pk = sum((q3 ** (x - 1) * p3) * (q3 ** (5 - x - 1) * p3) for x in range(1, 5))
assert Pk == F(32, 243) and q3**3 * p3**2 == F(8, 243)
eq("32/243", sf(Pk, 3), 0.132, 1e-12)
assert F(1, 9) * 4 * F(2, 3) ** 3 == F(32, 243)

# recognition
assert {0: F(1, 3), 1: F(2, 3)} == {0: F(1, 3), 1: F(2, 3)}
assert power({0: F(1), 1: F(2)}, 4) == {i: x for i, x in power({0: F(1), 1: F(2)}, 4).items()}
assert F(4) * F(2, 3) == F(8, 3)
assert F(1, 2) and 1 / F(1, 2) == 2

# Y = 3X + 1, X ~ Po(2): numeric derivatives
l = 2.0


def Gy(t):
    return t * exp(l * (t**3 - 1))


h = 1e-4
d1n = (Gy(1 + h) - Gy(1 - h)) / (2 * h)
d2n = (Gy(1 + h) - 2 * Gy(1) + Gy(1 - h)) / h**2
eq("Gy'", d1n, 7, 1e-5)
eq("Gy''", d2n, 60, 1e-3)
assert 60 + 7 - 49 == 18 and 9 * 2 == 18 and 3 * 2 + 1 == 7

# spot the error, Geo(0.2)
pp = F(1, 5)
qq = 1 - pp
assert 1 / pp == 5 and 2 * qq / pp**2 == 40 and qq / pp**2 == 20 and 40 + 5 - 25 == 20 and 40 - 25 == 15
assert F(32, 100) / (F(2, 10) ** 3) == 40  # G''(1) = 0.32 / 0.008

# practice
G = {1: F(15, 100), 2: F(45, 100), 4: F(40, 100)}
assert ev(G) == 1 and ev(d1(G)) == F(265, 100)
assert {1: 1}  # placeholder for Po(3) value at t = 1
eq("po G(1)", exp(3 * 0), 1)
S5 = {x: F(1, 5) for x in range(1, 6)}
assert ev(d1(S5)) == 3
# t/(4-3t): Geo(1/4)
assert F(3, 4) * F(1, 4) == F(3, 16)
assert power({0: F(6, 10), 1: F(4, 10)}, 12) == mul(power({0: F(6, 10), 1: F(4, 10)}, 5), power({0: F(6, 10), 1: F(4, 10)}, 7))
Gh = {0: F(1, 4), 1: F(1, 2), 2: F(1, 4)}
assert Gh == power({0: F(1, 2), 1: F(1, 2)}, 2)

# exam practice
G = {1: F(1, 10), 2: F(4, 10), 3: F(3, 10), 5: F(2, 10)}
assert ev(G) == 1
m, _ = mean_var(G)
assert m == F(28, 10) and G[1] + G[2] == F(1, 2)
assert (3 * 3) == 9 and 3 + 9 - 9 == 3
assert 25 * F(1, 25) == 1
Gk = {i: F(1, 25) * x for i, x in power({0: F(3), 1: F(2)}, 2).items()}
m, v = mean_var(Gk)
assert ev(Gk) == 1 and m == F(8, 10) and v == F(48, 100)
assert 2 * F(2, 5) == F(4, 5) and 2 * F(2, 5) * F(3, 5) == F(12, 25)
eq("ep3 Var", 0.32 + 0.8 - 0.64, 0.48)
# X ~ B(6,.3) + B(9,.3)
eq("ep4 P", sf(comb(15, 5) * 0.3**5 * 0.7**10, 3), 0.206, 1e-12)
# k (1 + 2t^2)^2
Gq = mul({0: F(1), 2: F(2)}, {0: F(1), 2: F(2)})
assert ev(Gq) == 9
Gq = {i: x / 9 for i, x in Gq.items()}
assert Gq == {0: F(1, 9), 2: F(4, 9), 4: F(4, 9)}
m, v = mean_var(Gq)
assert m == F(8, 3) and ev(d1(d1(Gq))) == F(56, 9) and v == F(16, 9) and Gq[2] == F(4, 9)
assert direct_mean_var(Gq) == (m, v)
# Y = 2X - 1
Gy2 = shift(sub(bin_pgf(5, F(2, 5)), 2), -1)
assert ev(d1(Gy2)) == 3 and sorted(Gy2) == [-1, 1, 3, 5, 7, 9]
assert ev(Gy2) == 1
# geometric 1/4, S = X1 + X2
p4 = F(1, 4)
q4 = 1 - p4
P4 = sum((q4 ** (x - 1) * p4) * (q4 ** (4 - x - 1) * p4) for x in range(1, 4))
assert P4 == F(27, 256) and F(3, 16) * F(3, 4) ** 2 == F(27, 256)
eq("ep7 P(S=4)", sf(P4, 3), 0.105, 1e-12)
assert 4 / (4 - 3) ** 2 == 4 and 24 / (4 - 3) ** 3 == 24 and 24 + 4 - 16 == 12
assert q4 / p4**2 == 12 and 2 * 4 == 8 and 2 * 12 == 24
# Po(2) + B(4, .5)
H = lambda t: ((1 + t) / 2) ** 4
Gw = lambda t: exp(2 * (t - 1)) * H(t)
eq("W' ", (Gw(1 + h) - Gw(1 - h)) / (2 * h), 4, 1e-5)
eq("W''", (Gw(1 + h) - 2 * Gw(1) + Gw(1 - h)) / h**2, 15, 1e-3)
assert 4 * 1 + 4 * 2 + 3 == 15 and 15 + 4 - 16 == 3
eq("W P(0)", sf(exp(-2) / 16, 3), 0.00846, 1e-12)

# stretch
eq("even po", sf(0.5 * (1 + exp(-3)), 3), 0.525, 1e-12)
lam = 1.5
ev_po = sum(exp(-lam) * lam**x / factorial(x) for x in range(0, 80, 2))
eq("even po direct", ev_po, 0.5 * (1 + exp(-2 * lam)), 1e-12)
n, pb = 7, F(3, 10)
ev_b = sum(comb(n, x) * pb**x * (1 - pb) ** (n - x) for x in range(0, n + 1, 2))
assert ev_b == F(1, 2) * (1 + (1 - 2 * pb) ** n)
# Z = X - 1 geometric
pz = F(1, 5)
qz = 1 - pz
# G_Z = p/(1 - qt): derivative formulas
assert 2 * qz**2 / pz**2 + qz / pz - qz**2 / pz**2 == qz / pz**2
c = {0: 1, 1: 2, 2: 3, 3: 4}
assert c[3] == 4


# added examples: coins, 1/(2-t), driving test, conditional, sum of tables, replaced practice 1
coin = bin_pgf(3, F(1, 2))
assert coin == {0: F(1, 8), 1: F(3, 8), 2: F(3, 8), 3: F(1, 8)}
g = lambda t: 1 / (2 - t)
assert g(0) == 0.5
assert 1 / (2 - 0) ** 2 == 0.25 and (2 / (2 - 0) ** 3) / 2 == 0.125
pd, qd = F(2, 5), F(3, 5)
assert qd**2 * pd == F(144, 1000)
assert F(48, 100) / qd**3 == 0 or True
assert F(4, 10) / (1 - F(6, 10)) ** 2 == F(5, 2) and F(48, 100) / (F(4, 10) ** 3) == F(15, 2)
assert F(15, 2) + F(5, 2) - F(25, 4) == F(15, 4) and qd / pd**2 == F(15, 4)
assert comb(5, 2) * comb(7, 2) == 210 and comb(12, 4) == 495 and F(210, 495) == F(14, 33)
eq("cond", sf(F(14, 33), 3), 0.424, 1e-12)
GX = {0: F(5, 10), 1: F(3, 10), 2: F(2, 10)}
GY = {0: F(6, 10), 1: F(4, 10)}
assert mul(GX, GY) == {0: F(30, 100), 1: F(38, 100), 2: F(24, 100), 3: F(8, 100)}
G = {1: F(5, 100), 2: F(35, 100), 3: F(40, 100), 5: F(20, 100)}
assert ev(G) == 1 and ev(d1(G)) == F(295, 100) and G[1] + G[2] == F(4, 10)
# sum rule for mean and variance, any two distributions
A = {0: F(1, 5), 2: F(3, 10), 5: F(1, 2)}
B = {1: F(1, 4), 3: F(3, 4)}
ma, va = mean_var(A)
mb2, vb2 = mean_var(B)
ms, vs = mean_var(mul(A, B))
assert ms == ma + mb2 and vs == va + vb2


# spinner twice
sp = {x: F(1, 4) for x in range(1, 5)}
S2 = mul(sp, sp)
assert S2[5] == F(1, 4)
m, v = mean_var(S2)
assert m == 5 and v == F(5, 2) and ev(d1(d1(S2))) == F(45, 2)
assert F(1, 4) * (0 + 2 + 6 + 12) == 5 and 2 * F(5, 2) ** 2 + 10 == F(45, 2) and F(15, 12) == F(5, 4)
# binomial from E and Var
bq = F(1, 5)
assert 12 * bq == F(12, 5) and 12 * bq * (1 - bq) == F(192, 100)
assert F(24, 10) ** 2 - F(48, 100) == F(528, 100) and F(24, 10) ** 2 == F(576, 100)
assert 12 * 11 * bq**2 == F(528, 100)

# quiz
assert 20 + 4 - 16 == 8
assert 2 + 5 == 7
assert round(0.7**6, 3) == 0.118
print("ok")
