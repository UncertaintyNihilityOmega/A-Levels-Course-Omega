# checks/math.fm.nonpar.py: recomputes every number in "Non-parametric tests: the sign test".
# Standard library only: exact binomial B(n, 1/2) probabilities with Fractions, normal from NormalDist.
from math import comb, sqrt, isclose
from fractions import Fraction as F
from statistics import NormalDist

N = NormalDist()


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def cdf(n, k, p=F(1, 2)):
    return sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(0, k + 1))


def up(n, k, p=F(1, 2)):
    return 1 - cdf(n, k - 1, p)


def r(x, d):
    return round(float(x), d)


# warm-up
eq("wu1", r(cdf(10, 2), 4), 0.0547, 1e-12)
assert cdf(10, 2) == F(56, 1024)
eq("wu2 B(20,.3) P<=2", r(cdf(20, 2, F(3, 10)), 4), 0.0355, 1e-12)
z = 4.5 / sqrt(12.5)
eq("wu3 z", sf(z, 4), 1.273, 1e-12)
eq("wu3 p", sf(1 - N.cdf(4.5 / sqrt(12.5)), 3), 0.102, 1e-12)

# eg1 bus
bus = [22, 19, 27, 21, 18, 24, 23, 20, 26, 17]
assert sum(1 for x in bus if x > 25) == 2 and len(bus) == 10 and 25 not in bus
eq("bus p", r(cdf(10, 2), 4), 0.0547, 1e-12)
assert cdf(10, 2) > F(5, 100)
eq("bus p1", r(cdf(10, 1), 4), 0.0107, 1e-12)
assert cdf(10, 1) == F(11, 1024)

# eg2 shopkeeper
shop = [52, 47, 61, 45, 38, 55, 49, 58, 43, 66, 51, 36]
assert sum(1 for x in shop if x > 40) == 10 and sum(1 for x in shop if x < 40) == 2 and 40 not in shop
assert cdf(12, 2) == F(79, 4096)
eq("shop p", r(cdf(12, 2), 4), 0.0193, 1e-12)
assert cdf(12, 2) < F(25, 1000) and 2 * cdf(12, 2) < F(5, 100)
eq("shop double", r(2 * cdf(12, 2), 4), 0.0386, 1e-12)
assert cdf(12, 2) > F(5, 1000)

# critical-value table
def crit(n, a):
    best = None
    for k in range(0, n + 1):
        if cdf(n, k) <= a:
            best = k
        else:
            break
    return best


table = {6: (0, 0, None), 7: (0, 0, 0), 8: (1, 0, 0), 9: (1, 1, 0), 10: (1, 1, 0), 11: (2, 1, 1), 12: (2, 2, 1),
         13: (3, 2, 1), 14: (3, 2, 2), 15: (3, 3, 2), 16: (4, 3, 2), 17: (4, 4, 3), 18: (5, 4, 3), 19: (5, 4, 4),
         20: (5, 5, 4)}
for n, row in table.items():
    got = (crit(n, F(5, 100)), crit(n, F(25, 1000)), crit(n, F(1, 100)))
    assert got == row, (n, got, row)

# eg3 n = 15
assert cdf(15, 3) == F(576, 32768) and cdf(15, 4) == F(1941, 32768)
eq("n15 tail", r(cdf(15, 3), 4), 0.0176, 1e-12)
eq("n15 next", r(cdf(15, 4), 4), 0.0592, 1e-12)
eq("n15 alpha", r(2 * cdf(15, 3), 4), 0.0352, 1e-12)
assert 15 - 3 == 12

# eg4 athletes
before = [24.1, 26.3, 23.8, 27.5, 25.2, 28.0, 24.9, 26.7]
after = [23.4, 25.1, 24.0, 26.2, 24.6, 26.9, 24.4, 25.7]
d = [round(b - a, 1) for b, a in zip(before, after)]
assert d == [0.7, 1.2, -0.2, 1.3, 0.6, 1.1, 0.5, 1.0], d
assert sum(1 for x in d if x > 0) == 7
assert up(8, 7) == F(9, 256)
eq("athletes p", r(up(8, 7), 4), 0.0352, 1e-12)

# eg5 reaction times, normal approximation
z = (26.5 - 20) / sqrt(10)
eq("rt z", sf(z, 4), 2.055, 1e-12)
eq("rt p", sf(1 - N.cdf(z), 3), 0.0199, 1e-12)
eq("rt exact", r(up(40, 27), 4), 0.0192, 1e-12)

# eg6 puzzle with music
assert up(12, 9) == F(299, 4096) and 220 + 66 + 12 + 1 == 299
eq("music p", r(up(12, 9), 4), 0.0730, 1e-12)


# eg coffee shop (stem-and-leaf)
cs = [4, 5, 7, 10, 12, 12, 15, 18, 19, 21, 23, 34, 40, 86]
assert len(cs) == 14 and 8 not in cs and sum(1 for x in cs if x > 8) == 11
assert up(14, 11) == F(470, 16384) and 364 + 91 + 14 + 1 == 470
eq("coffee p", r(up(14, 11), 4), 0.0287, 1e-12)

# spot the error, n = 14
assert cdf(14, 3) == F(470, 16384) and 1 + 14 + 91 + 364 == 470
eq("spot tail", r(cdf(14, 3), 4), 0.0287, 1e-12)
eq("spot double", r(2 * cdf(14, 3), 4), 0.0574, 1e-12)
assert cdf(14, 3) > F(25, 1000)

# practice
assert cdf(9, 3) == F(130, 512)
eq("pr1", sf(cdf(9, 3), 3), 0.254, 1e-12)
assert up(11, 9) == F(67, 2048)
eq("pr2", r(up(11, 9), 4), 0.0327, 1e-12)
assert up(10, 8) == F(56, 1024)
eq("pr3", r(up(10, 8), 4), 0.0547, 1e-12)
assert cdf(12, 2) == F(79, 4096) and cdf(12, 3) == F(299, 4096)
eq("pr4", r(cdf(12, 3), 4), 0.0730, 1e-12)
z = -7.5 / sqrt(15)
eq("pr7 z", sf(z, 4), -1.936, 1e-12)
eq("pr7 p", sf(N.cdf(z), 3), 0.0264, 1e-12)

# exam practice
assert up(9, 7) == F(46, 512)
eq("ep1", r(up(9, 7), 4), 0.0898, 1e-12)
assert cdf(11, 1) == F(12, 2048) and cdf(11, 2) == F(67, 2048)
eq("ep2 a", sf(cdf(11, 1), 3), 0.00586, 1e-12)
eq("ep2 b", sf(cdf(11, 2), 3), 0.0327, 1e-12)
assert crit(11, F(25, 1000)) == 1
eq("ep2 level", sf(2 * cdf(11, 1), 3), 0.0117, 1e-12)
b4 = [148, 152, 139, 160, 145, 157, 151, 143]
a4 = [141, 150, 142, 151, 138, 149, 153, 136]
dd = [x - y for x, y in zip(b4, a4)]
assert dd == [7, 2, -3, 9, 7, 8, -2, 7]
assert sum(1 for x in dd if x > 0) == 6
assert up(8, 6) == F(37, 256)
eq("ep3", sf(up(8, 6), 3), 0.145, 1e-12)
z = 7.5 / sqrt(15)
eq("ep4 z", sf(z, 4), 1.936, 1e-12)
eq("ep4 p", sf(1 - N.cdf(z), 3), 0.0264, 1e-12)
assert 1 - N.cdf(z) > 0.025
assert 1 + 18 + 153 + 816 + 3060 == 4048
eq("ep5 a", sf(cdf(18, 4), 3), 0.0154, 1e-12)
eq("ep5 alpha", sf(2 * cdf(18, 4), 3), 0.0309, 1e-12)
p3 = F(3, 10)
beta = cdf(18, 13, p3) - cdf(18, 4, p3)
eq("ep5 beta", sf(beta, 3), 0.667, 1e-12)
eq("ep5 P(S<=4)", sf(cdf(18, 4, p3), 4), 0.3327, 1e-12)
assert 3.9e-5 < float(up(18, 14, p3)) < 4.0e-5
cafe = [3.2, 4.1, 2.8, 9.5, 5.0, 3.7, 6.8, 4.4, 2.9, 3.5]
assert sum(1 for x in cafe if x > 6) == 2 and 6 not in cafe
eq("ep6", r(cdf(10, 2), 4), 0.0547, 1e-12)
eq("ep7 P<=7", sf(cdf(25, 7), 3), 0.0216, 1e-12)
eq("ep7 P<=8", sf(cdf(25, 8), 3), 0.0539, 1e-12)
s = 12.5 - 0.5 - 1.6448536269514722 * 2.5
eq("ep7 s", sf(s, 3), 7.89, 1e-12)
assert int(s) == 7

# stretch
eq("st a", sf(up(10, 9), 3), 0.0107, 1e-12)
pw = up(10, 9, F(4, 5))
eq("st b", sf(pw, 3), 0.376, 1e-12)
eq("st b1", sf(10 * 0.8**9 * 0.2, 4), 0.2684, 1e-12)
eq("st b2", sf(0.8**10, 4), 0.1074, 1e-12)
eq("st2 6", sf(0.5**6, 3), 0.0156, 1e-12)
eq("st2 7", sf(0.5**7, 3), 0.00781, 1e-12)
assert 0.5**6 > 0.01 > 0.5**7

# quiz
assert (40 / 2, 40 / 4) == (20, 10)
print("ok")
