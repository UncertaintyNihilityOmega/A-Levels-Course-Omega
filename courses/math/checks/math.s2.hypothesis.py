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
print("ok")
