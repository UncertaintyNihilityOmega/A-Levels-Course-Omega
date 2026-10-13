# checks/math.s2.hypothesis.py: recomputes every number in the hypothesis testing chapter.
from math import isclose, comb, exp, factorial, sqrt
from statistics import NormalDist

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

Z = NormalDist(); Phi = Z.cdf

def bcdf(n, p, r):
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(r + 1))

def pcdf(l, r):
    return sum(exp(-l) * l ** k / factorial(k) for k in range(r + 1))

# Binomial one-tailed
eq("P<=2", sf(bcdf(20, .3, 2), 3), 0.0355)
eq("P<=3", sf(bcdf(20, .3, 3), 3), 0.107)
eq("P>=10", sf(1 - bcdf(20, .3, 9), 3), 0.0480); eq("P>=9", sf(1 - bcdf(20, .3, 8), 3), 0.113)
eq("sig a", sf(bcdf(20, .3, 2) * 100, 3), 3.55); eq("sig b", sf((1 - bcdf(20, .3, 9)) * 100, 3), 4.80)
# Coin 15 of 20
eq("P>=15", sf(1 - bcdf(20, .5, 14), 3), 0.0207); eq("P<=5", sf(bcdf(20, .5, 5), 3), 0.0207); eq("P<=6", sf(bcdf(20, .5, 6), 3), 0.0577)
eq("sig 2t", sf(2 * bcdf(20, .5, 5) * 100, 3), 4.14)
# Poisson
eq("po12", sf(1 - pcdf(6, 11), 3), 0.0201)
eq("po web", sf(1 - pcdf(4, 6), 3), 0.111); eq("po web 4", round(1 - pcdf(4, 6), 4), 0.1107); eq("rate", 0.8 * 5, 4)
# Normal approx
eq("bin var", 100 * .4 * .6, 24); eq("z bin", sf(9.5 / sqrt(24), 4), 1.939); eq("bin", sf(1 - Phi(9.5 / sqrt(24)), 3), 0.0262)
eq("po z", 9.5 / 5, 1.9); eq("po", sf(1 - Phi(1.9), 3), 0.0287)
# Mean tests
eq("flour se", 12 / sqrt(36), 2); eq("flour z", (496.5 - 500) / 2, -1.75); eq("flour", sf(Phi(-1.75), 3), 0.0401)
eq("tin se", 6 / 5, 1.2); eq("tin z", sf(2.8 / 1.2, 4), 2.333); eq("tin p", sf(1 - Phi(2.8 / 1.2), 3), 0.00982)
eq("tin cv", 1.96 * 1.2, 2.352); eq("tin lo", round(100 - 2.352, 2), 97.65); eq("tin hi", round(100 + 2.352, 2), 102.35)
se = 5.6 / sqrt(80)
eq("item se", round(se, 4), 0.6261); eq("item z", sf(1.2 / se, 4), 1.917); eq("item", sf(1 - Phi(1.2 / se), 3), 0.0276)
assert 1 - Phi(1.2 / se) > 0.01
assert 1 - pcdf(6, 11) > 0.01   # 12 calls: not significant at 1%
# Type I and II
eq("t2 p.1", sf(1 - bcdf(20, .1, 2), 3), 0.323); eq("B20,.1 P<=2", sf(bcdf(20, .1, 2), 4), 0.6769)
eq("flour cv", 500 - 1.645 * 2, 496.71); eq("flour z2", sf((496.71 - 495) / 2, 3), 0.855)
eq("flour Phi", round(Phi(0.855), 4), 0.8037); eq("flour II", sf(1 - Phi(0.855), 3), 0.196)
# Exam 1 parcels
eq("par P", sf(1 - bcdf(25, .15, 6), 3), 0.0695); eq("par P8", sf(1 - bcdf(25, .15, 7), 3), 0.0255)
# Exam 2 cloth
eq("cloth rate", 3.5 * 2, 7); eq("cloth P", sf(pcdf(7, 2), 3), 0.0296); eq("cloth form", 32.5 * exp(-7), pcdf(7, 2)); eq("cloth P3", sf(pcdf(7, 3), 3), 0.0818)
eq("cloth II", sf(1 - pcdf(4, 2), 3), 0.762); eq("cloth P2 4", sf(pcdf(4, 2), 4), 0.2381)
# Exam 3 tins
eq("tin3 se", 5 / 4, 1.25); eq("tin3 z", 2.6 / 1.25, 2.08); eq("tin3 p", sf(1 - Phi(2.08), 3), 0.0188)
eq("tin3 cv", round(1.96 * 1.25, 2), 2.45); eq("tin3 lo", 400 - 1.96 * 1.25, 397.55); eq("tin3 hi", 400 + 1.96 * 1.25, 402.45)
eq("tin3 II", sf(Phi((402.45 - 403) / 1.25) - Phi((397.55 - 403) / 1.25), 3), 0.330); eq("tin3 z1", (402.45 - 403) / 1.25, -0.44); eq("tin3 z2", (397.55 - 403) / 1.25, -4.36)
# Try
eq("t2", sf(1 - bcdf(12, .5, 9), 3), 0.0193)
eq("t3", sf(1 - bcdf(30, 1 / 6, 8), 3), 0.0506)
eq("t4a", sf(bcdf(25, .4, 5), 3), 0.0294); eq("t4b", sf(bcdf(25, .4, 6), 3), 0.0736)
eq("t5", sf(1 - bcdf(30, .08, 4), 3), 0.0874)
eq("t6", sf(1 - pcdf(3, 7), 3), 0.0119)
eq("t7 z", sf(9.5 / sqrt(20), 4), 2.124); eq("t7", sf(1 - Phi(9.5 / sqrt(20)), 3), 0.0168); eq("t7 var", 80 * .25, 20)
eq("t8 se", 2.4 / 3, 0.8); eq("t8 z", -1.1 / 0.8, -1.375); eq("t8", sf(Phi(-1.375), 3), 0.0846)
eq("t10 P4", sf(bcdf(10, .7, 4), 3), 0.0473); eq("t10 P3", sf(bcdf(10, .7, 3), 3), 0.0106); eq("t10 II", sf(1 - bcdf(10, .5, 4), 3), 0.623); eq("t10 cdf5", sf(bcdf(10, .5, 4), 3), 0.377)
eq("t11 se", 15 / 10, 1.5); eq("t11 z", sf(3.5 / 1.5, 4), 2.333); eq("t11", sf(1 - Phi(3.5 / 1.5), 3), 0.00982)

# ---- P14 additions ----
from math import comb as _cb, exp as _ex, factorial as _fa, sqrt as _sq
from statistics import NormalDist as _ND
_N = _ND()
def _b(n, p, r): return _cb(n, r) * p ** r * (1 - p) ** (n - r)
def _bc(n, p, r): return sum(_b(n, p, k) for k in range(r + 1))
def _po(l, r): return _ex(-l) * l ** r / _fa(r)
def _pc(l, r): return sum(_po(l, k) for k in range(r + 1))
def sf4(x): return float(f"{x:.4g}")
# warm-up
eq("w1", sf(_bc(15, .4, 4)), 0.217); eq("w2 cdf", sf4(_pc(2.5, 3)), 0.7576); eq("w2", sf(1 - _pc(2.5, 3)), 0.242)
eq("w3", sf(1 - _N.cdf(1)), 0.159)
# spot the error
eq("sp tail", sf(1 - _bc(30, .5, 19)), 0.0494); eq("sp both", sf(2 * (1 - _bc(30, .5, 19))), 0.0987)
# exam practice
eq("e1", sf4(_bc(12, .25, 1)), 0.1584)
eq("e2 cdf", sf4(_pc(3.5, 7)), 0.9733); eq("e2", sf(1 - _pc(3.5, 7)), 0.0267)
eq("e3 l4", round(_bc(25, .4, 4), 4), 0.0095); eq("e3 l5", round(_bc(25, .4, 5), 4), 0.0294)
eq("e3 u16", round(1 - _bc(25, .4, 15), 4), 0.0132); eq("e3 u15", round(1 - _bc(25, .4, 14), 4), 0.0344)
assert _bc(25, .4, 4) <= .025 < _bc(25, .4, 5) and 1 - _bc(25, .4, 15) <= .025 < 1 - _bc(25, .4, 14)
eq("e3 act", round(_bc(25, .4, 4) + 1 - _bc(25, .4, 15), 4), 0.0226)
eq("e4 var", 120 * .2 * .8, 19.2); eq("e4 z", round((32.5 - 24) / _sq(19.2), 3), 1.940); eq("e4", sf(1 - _N.cdf((32.5 - 24) / _sq(19.2))), 0.0262)
se5 = 3.2 / _sq(40); z5 = 1.1 / se5
eq("e5 se", round(se5, 3), 0.506); eq("e5 z", round(z5, 3), 2.174); eq("e5 p", sf(1 - _N.cdf(z5)), 0.0149)
eq("e6 a", sf(1 - _pc(2, 5)), 0.0166); eq("e6 b", sf(_pc(4, 5)), 0.785)
se = 4 / 5; c = 250 - 1.645 * se; c0 = 250 - _N.inv_cdf(.95) * se
eq("e7 c", round(c0, 2), 248.68); eq("e7 c3", sf(c0, 4), 248.7); eq("e7 z", round((c0 - 248) / se, 3), 0.855); eq("e7 b", sf(1 - _N.cdf((c0 - 248) / se)), 0.196)
eq("e7 zinv", round(_N.inv_cdf(.9), 3), 1.282); eq("e7 root", round((1.282 + 1.645) / .5, 3), 5.854); eq("e7 n", round(((1.282 + 1.645) / .5) ** 2, 1), 34.3)
def _t2(n):
    s = 4 / _sq(n); cc = 250 - _N.inv_cdf(.95) * s; return 1 - _N.cdf((cc - 248) / s)
eq("e7 n35", round(_t2(35), 4), 0.0946); eq("e7 n34", round(_t2(34), 4), 0.1019)
assert _t2(35) < .1 < _t2(34)
# stretch
eq("s1 a4", .5 ** 4, 0.0625); eq("s1 a5", .5 ** 5, 0.03125)
eq("s1 b9", round(1 - _bc(10, .5, 8), 4), 0.0107); eq("s1 b8", round(1 - _bc(10, .5, 7), 4), 0.0547)
eq("s1 c", sf(_bc(10, .8, 8)), 0.624); eq("s1 c9", sf(_b(10, .8, 9) + _b(10, .8, 10)), 0.376); eq("s1 c9b", round(_b(10, .8, 9) + _b(10, .8, 10), 4), 0.3758)
eq("s2", sf(1 - .95 ** 20), 0.642); eq("s2 pct", round(.95 ** 20, 4), 0.3585)
print("ok")
