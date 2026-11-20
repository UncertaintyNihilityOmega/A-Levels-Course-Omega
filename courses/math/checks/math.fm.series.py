# checks/math.fm.series.py: recomputes every number and identity in Summation of series.
# Standard library only: exact arithmetic with Fraction, brute-force sums to confirm every closed form.
from fractions import Fraction as F
from math import isclose, factorial, sqrt, log


def eq(label, got, want, tol=1e-9):
    assert isclose(float(got), float(want), rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def S(u, a, b):
    """Sum of u(r) for r = a..b (exact when u returns Fractions/ints)."""
    return sum(u(r) for r in range(a, b + 1))


NS = range(1, 41)

# ---- warm-up
assert 20 * (2 * 3 + 19 * 4) // 2 == 820 and S(lambda r: 3 + 4 * (r - 1), 1, 20) == 820
for r in range(1, 30):
    assert F(1, r * (r + 1)) == F(1, r) - F(1, r + 1)
assert 2 * 3 ** 3 + 3 * 9 + 3 == 3 * (2 * 3 + 1) * (3 + 1)
for n in NS:
    assert 2 * n ** 3 + 3 * n ** 2 + n == n * (2 * n + 1) * (n + 1)

# ---- sigma notation examples
assert S(lambda r: 2 * r + 1, 1, 4) == 3 + 5 + 7 + 9 == 24
assert S(lambda r: r * r, 3, 6) == 9 + 16 + 25 + 36 == 86 and 6 - 3 + 1 == 4
assert S(lambda r: 3, 1, 5) == 15
assert 1 ** 2 + 2 ** 2 == 5 and (1 + 2) ** 2 == 9

# ---- standard results
s1 = lambda n: F(n * (n + 1), 2)
s2 = lambda n: F(n * (n + 1) * (2 * n + 1), 6)
s3 = lambda n: F(n * n * (n + 1) ** 2, 4)
for n in range(0, 60):
    assert S(lambda r: r, 1, n) == s1(n)
    assert S(lambda r: r * r, 1, n) == s2(n)
    assert S(lambda r: r ** 3, 1, n) == s3(n)
    assert s3(n) == s1(n) ** 2
assert (s1(4), s2(4), s3(4)) == (10, 30, 100)
assert 1 + 2 + 3 + 4 == 10 and 1 + 4 + 9 + 16 == 30 and 1 + 8 + 27 + 64 == 100
assert F(1, 2) * 4 * 5 == 10 and F(1, 6) * 4 * 5 * 9 == 30 and F(1, 4) * 16 * 25 == 100

# proof of sum of squares via (r+1)^3 - r^3
for r in range(1, 30):
    assert (r + 1) ** 3 - r ** 3 == 3 * r * r + 3 * r + 1
for n in range(1, 40):
    assert (n + 1) ** 3 - 1 == 3 * s2(n) + 3 * s1(n) + n
    lhs = (n + 1) ** 3 - 1 - F(3, 2) * n * (n + 1) - n
    assert lhs == n ** 3 + 3 * n ** 2 + 2 * n - F(3, 2) * n ** 2 - F(3, 2) * n
    assert lhs == F(1, 2) * n * (2 * n * n + 3 * n + 1) == F(1, 2) * n * (n + 1) * (2 * n + 1) == 3 * s2(n)

# eg: 20, 12, 6..15
assert F(1, 6) * 20 * 21 * 41 == 2870 == s2(20)
assert F(1, 4) * 12 ** 2 * 13 ** 2 == 36 * 169 == 6084 == s3(12) and s1(12) == 78 and 78 ** 2 == 6084
assert S(lambda r: r ** 3, 6, 15) == s3(15) - s3(5) == 14400 - 225 == 14175
assert F(1, 4) * 15 ** 2 * 16 ** 2 == 14400 and F(1, 4) * 5 ** 2 * 6 ** 2 == 225

# tins
assert s2(12) == 650 and S(lambda r: r * r, 5, 12) == s2(12) - s2(4) == 650 - 30 == 620
assert s2(4) == 30
assert s2(13) == 819 and s2(14) == 1015 and 1000 - 819 == 181
assert F(1, 6) * 13 * 14 * 27 == 819 and F(1, 6) * 14 * 15 * 29 == 1015
assert max(n for n in range(1, 50) if s2(n) <= 1000) == 13

# ---- related sums
for n in NS:
    # r(r+1)
    assert S(lambda r: r * (r + 1), 1, n) == F(n * (n + 1) * (n + 2), 3)
    assert s2(n) + s1(n) == F(1, 6) * n * (n + 1) * ((2 * n + 1) + 3) == F(1, 6) * n * (n + 1) * (2 * n + 4)
    # (2r-1)^2
    assert S(lambda r: (2 * r - 1) ** 2, 1, n) == F(n * (2 * n - 1) * (2 * n + 1), 3)
    assert 4 * s2(n) - 4 * s1(n) + n == F(2, 3) * n * (n + 1) * (2 * n + 1) - 2 * n * (n + 1) + n
    assert F(1, 3) * n * (2 * (n + 1) * (2 * n + 1) - 6 * (n + 1) + 3) == F(1, 3) * n * (4 * n * n - 1)
    assert 4 * n * n + 6 * n + 2 - 6 * n - 6 + 3 == 4 * n * n - 1
    # r(r+1)(r+2)
    assert S(lambda r: r * (r + 1) * (r + 2), 1, n) == F(n * (n + 1) * (n + 2) * (n + 3), 4)
    assert F(1, 4) * n * (n + 1) * (n * (n + 1) + 2 * (2 * n + 1) + 4) == F(1, 4) * n * (n + 1) * (n * n + 5 * n + 6)
    assert n * (n + 1) + 2 * (2 * n + 1) + 4 == n * n + 5 * n + 6 == (n + 2) * (n + 3)
    assert s3(n) + 3 * s2(n) + 2 * s1(n) == F(n * (n + 1) * (n + 2) * (n + 3), 4)
    # r(r+1)(r+2) - (r-1)r(r+1) = 3r(r+1)
    for r in (n,):
        assert r * (r + 1) * (r + 2) - (r - 1) * r * (r + 1) == 3 * r * (r + 1)
assert S(lambda r: r * (r + 1), 1, 3) == 20 and F(1, 3) * 3 * 4 * 5 == 20
assert S(lambda r: (2 * r - 1) ** 2, 1, 3) == 35 == F(1, 3) * 3 * 5 * 7

# sums to 2n
for n in NS:
    assert S(lambda r: r * r, n + 1, 2 * n) == F(n * (2 * n + 1) * (7 * n + 1), 6)
    assert s2(2 * n) - s2(n) == F(1, 6) * n * (2 * n + 1) * (2 * (4 * n + 1) - (n + 1))
    assert 2 * (4 * n + 1) - (n + 1) == 7 * n + 1
    assert S(lambda r: (2 * r) ** 2, 1, n) == F(2, 3) * n * (n + 1) * (2 * n + 1) == 4 * s2(n)
    odd = F(1, 3) * n * (2 * n - 1) * (2 * n + 1)
    even = F(2, 3) * n * (n + 1) * (2 * n + 1)
    assert odd + even == F(1, 3) * n * (2 * n + 1) * (2 * (n + 1) + (2 * n - 1)) == F(1, 3) * n * (2 * n + 1) * (4 * n + 1)
    assert 2 * (n + 1) + (2 * n - 1) == 4 * n + 1
    assert s2(2 * n) == F(1, 6) * 2 * n * (2 * n + 1) * (4 * n + 1) == F(1, 3) * n * (2 * n + 1) * (4 * n + 1)
assert 3 ** 2 + 4 ** 2 == 25 and F(1, 6) * 2 * 5 * 15 == 25

# exam eg: sum (r+2)(2r-1) = n(4n^2+15n-1)/6, then r = 11..30
f = lambda n: F(n * (4 * n * n + 15 * n - 1), 6)
for n in NS:
    assert (n + 2) * (2 * n - 1) == 2 * n * n + 3 * n - 2
    assert S(lambda r: (r + 2) * (2 * r - 1), 1, n) == f(n)
    assert 2 * s2(n) + 3 * s1(n) - 2 * n == F(1, 3) * n * (n + 1) * (2 * n + 1) + F(3, 2) * n * (n + 1) - 2 * n
    assert 2 * (2 * n * n + 3 * n + 1) + 9 * (n + 1) - 12 == 4 * n * n + 15 * n - 1
assert 3 * 1 + 4 * 3 == 15 == f(2) and F(1, 6) * 2 * 45 == 15
assert f(30) == 20245 and 5 * 4049 == 20245 and 4 * 900 + 450 - 1 == 4049
assert f(10) == 915 and 10 * 549 == 5490 and F(5490, 6) == 915 and 400 + 150 - 1 == 549
assert S(lambda r: (r + 2) * (2 * r - 1), 11, 30) == f(30) - f(10) == 19330 == 20245 - 915
assert f(30) - f(11) != 19330

# ---- method of differences
for r in range(1, 40):
    assert F(1, r) - F(1, r + 1) == F(1, r * (r + 1))
    assert F(1, 2) * (F(1, 2 * r - 1) - F(1, 2 * r + 1)) == F(1, (2 * r - 1) * (2 * r + 1))
    assert F(1, 2) * (F(1, r) - F(1, r + 2)) == F(1, r * (r + 2))
    assert F(1, 2) * (F(1, r * (r + 1)) - F(1, (r + 1) * (r + 2))) == F(1, r * (r + 1) * (r + 2))
    assert F(1, 2) * F(1, r) - F(1, r + 1) + F(1, 2) * F(1, r + 2) == F(1, r * (r + 1) * (r + 2))
    assert F(1, r * (r + 1)) - F(1, (r + 1) * (r + 2)) == F(2, r * (r + 1) * (r + 2))
    assert F(1, r) - F(1, r + 3) == F(3, r * (r + 3))
    assert F(1, 2 * r - 1) - F(1, 2 * r + 3) == F(4, (2 * r - 1) * (2 * r + 3))
    assert (r + 1) ** 2 - r ** 2 == 2 * r + 1
    assert F(1, r + 2) - F(1, r + 3) == F(1, (r + 2) * (r + 3))
    assert F(1, 2) * (F(1, 2 * r + 1) - F(1, 2 * r + 3)) == F(1, (2 * r + 1) * (2 * r + 3))
    assert F(1, r + 1) * 0 + F(r, factorial(r + 1)) == F(1, factorial(r)) - F(1, factorial(r + 1))
    assert (r + 1) * factorial(r) == factorial(r + 1) and factorial(r + 1) - factorial(r) == r * factorial(r)
    assert F(1, r * (r + 1) * (r + 2) * (r + 3)) == F(1, 3) * (F(1, r * (r + 1) * (r + 2)) - F(1, (r + 1) * (r + 2) * (r + 3)))
    assert F(1, (r + 1) * (r + 3)) == F(1, 2) * (F(1, r + 1) - F(1, r + 3))
    assert F(1, (3 * r - 1) * (3 * r + 2)) == F(1, 3) * (F(1, 3 * r - 1) - F(1, 3 * r + 2))
    assert F(1, r * r) - F(1, (r + 1) ** 2) == F(2 * r + 1, r * r * (r + 1) ** 2)
    assert F(2, r * (r + 1)) == F(1, F(r * (r + 1), 2))
    eq("sqrt", 1 / (sqrt(r) + sqrt(r + 1)), sqrt(r + 1) - sqrt(r), 1e-12)
    eq("ln", log((r + 1) / r), log(r + 1) - log(r), 1e-12)

for n in NS:
    assert S(lambda r: F(1, r * (r + 1)), 1, n) == 1 - F(1, n + 1) == F(n, n + 1)
    assert S(lambda r: F(1, (2 * r - 1) * (2 * r + 1)), 1, n) == F(1, 2) * (1 - F(1, 2 * n + 1)) == F(n, 2 * n + 1)
    assert S(lambda r: F(1, r * (r + 2)), 1, n) == F(1, 2) * (1 + F(1, 2) - F(1, n + 1) - F(1, n + 2))
    assert F(1, 2) * (1 + F(1, 2) - F(1, n + 1) - F(1, n + 2)) == F(3, 4) - F(2 * n + 3, 2 * (n + 1) * (n + 2))
    assert F(1, n + 1) + F(1, n + 2) == F(2 * n + 3, (n + 1) * (n + 2))
    assert S(lambda r: F(1, r * (r + 1) * (r + 2)), 1, n) == F(1, 4) - F(1, 2 * (n + 1) * (n + 2))
    assert S(lambda r: r * factorial(r), 1, n) == factorial(n + 1) - 1
    eq("sum sqrt", S(lambda r: 1 / (sqrt(r) + sqrt(r + 1)), 1, n), sqrt(n + 1) - 1, 1e-9)
    # exam full question (a), (b)
    assert S(lambda r: r * r + 3 * r + 1, 1, n) == F(n * (n + 2) * (n + 4), 3)
    assert s2(n) + 3 * s1(n) + n == F(1, 6) * n * (2 * n * n + 12 * n + 16)
    assert 2 * n * n + 3 * n + 1 + 9 * n + 9 + 6 == 2 * n * n + 12 * n + 16 == 2 * (n + 2) * (n + 4)
    assert S(lambda r: F(3, r * (r + 3)), 1, n) == F(11, 6) - F(1, n + 1) - F(1, n + 2) - F(1, n + 3) if n >= 3 else True
    assert S(lambda r: F(3, r * (r + 3)), 1, n) == F(11, 6) - F(1, n + 1) - F(1, n + 2) - F(1, n + 3)
assert 1 * (1 + 3) == 4 and F(3, 4) == F(11, 6) - F(1, 2) - F(1, 3) - F(1, 4)
assert F(1, 2) + F(1, 6) + F(1, 12) == F(3, 4) and F(1, 3) + F(1, 15) == F(2, 5)
assert F(1, 3) == F(3, 4) - F(5, 12) and F(1, 6) == F(1, 4) - F(1, 12)
assert 1 + 4 + 18 == 23 == factorial(4) - 1
eq("sqrt n=3", (sqrt(2) - 1) + (sqrt(3) - sqrt(2)) + (2 - sqrt(3)), 1)

# ---- convergence
eq("S inf 1/(2r-1)(2r+1)", float(F(10 ** 8, 2 * 10 ** 8 + 1)), 0.5, 1e-8)
assert F(1, 2) - F(1, 2 * (2 * 5 + 1)) == F(5, 11)
assert S(lambda r: r, 1, 100) == 5050 and S(lambda r: r, 1, 1000) > 500000
# charity
for n in NS:
    assert S(lambda r: F(600, r * (r + 1)), 1, n) == F(600 * n, n + 1) == 600 - F(600, n + 1) < 600
n_first = min(n for n in range(1, 1000) if F(600 * n, n + 1) > 595)
assert n_first == 120 and F(600 * 119, 120) == 595 and F(600 * 120, 121) > 595
eq("charity 120", float(F(72000, 121)), 595.04, 0.005)
assert 600 * 120 == 72000 and 600 * 119 == 71400
# plot S_n = 1 - 1/(n+1)
assert 1 - F(1, 4) == F(3, 4) and 1 - F(1, 10) == F(9, 10)
assert all(0 <= 1 - 1 / (x / 10 + 1) < 1.5 for x in range(0, 106))
# full exam question (c)
eq("11/6", F(11, 6) - F(1, 10 ** 9), 11 / 6, 1e-8)

# ---- spot the error
for n in NS:
    assert S(lambda r: 3 * r * r - 4, 1, n) == F(1, 2) * n * (2 * n * n + 3 * n - 7)
    assert F(1, 2) * n * (n + 1) * (2 * n + 1) - 4 * n == F(1, 2) * n * (2 * n * n + 3 * n + 1 - 8)
    assert 3 * s2(n) == F(1, 2) * n * (n + 1) * (2 * n + 1)
    assert F(1, 2) * n * (n + 1) * (2 * n + 1) - 4 == F(1, 2) * (2 * n ** 3 + 3 * n ** 2 + n - 8)
    assert (n + 1) * (2 * n + 1) == 2 * n * n + 3 * n + 1
assert S(lambda r: 3 * r * r - 4, 1, 2) == 7 == F(1, 2) * 2 * (8 + 6 - 7) and -1 + 8 == 7

# ---- try (easy to standard)
assert s1(14) == 105 and s3(14) == 11025 == 105 ** 2 and F(1, 4) * 14 ** 2 * 15 ** 2 == 11025
assert s2(9) == 285 and s2(10) == 385 and s2(3) == 14 and S(lambda r: r * r, 4, 10) == 371 == 385 - 14
for n in NS:
    assert S(lambda r: 4 * r - 3, 1, n) == n * (2 * n - 1) == 2 * n * (n + 1) - 3 * n
    assert S(lambda r: r * r - 3 * r + 2, 1, n) == F(n * (n - 1) * (n - 2), 3)
    assert F(1, 6) * n * (2 * n * n + 3 * n + 1 - 9 * n - 9 + 12) == F(1, 6) * n * (2 * n * n - 6 * n + 4)
    assert 2 * n * n - 6 * n + 4 == 2 * (n - 1) * (n - 2)
    assert S(lambda r: r * (r + 3), 1, n) == F(n * (n + 1) * (n + 5), 3)
    assert F(1, 6) * n * (n + 1) * (2 * n + 1 + 9) == F(1, 3) * n * (n + 1) * (n + 5)
    assert S(lambda r: 2 * r * (2 * r + 2), 1, n) == F(4, 3) * n * (n + 1) * (n + 2)
    assert S(lambda r: F(1, (r + 2) * (r + 3)), 1, n) == F(n, 3 * (n + 3)) == F(1, 3) - F(1, n + 3)
    assert S(lambda r: F(1, (2 * r + 1) * (2 * r + 3)), 1, n) == F(n, 3 * (2 * n + 3)) == F(1, 2) * (F(1, 3) - F(1, 2 * n + 3))
    assert S(lambda r: 2 * r + 1, 1, n) == (n + 1) ** 2 - 1 == n * n + 2 * n == 2 * s1(n) + n
assert S(lambda r: 4 * r * (r + 1), 1, 3) == 8 + 24 + 48 == 80 and 2 * 4 == 8 and 4 * 6 == 24 and 6 * 8 == 48
assert F(4, 3) * 20 * 21 * 22 == 12320 and S(lambda r: 2 * r * (2 * r + 2), 1, 20) == 12320
assert F(1, 3) * 3 * 2 * 1 == 2 and 1 + 5 + 9 == 15 == 3 * 5
assert F(1, 6) == F(1, 2) * F(1, 3)
# S_n = (3n^2+1)/(n^2+2n) tends to 3
big = 10 ** 7
eq("limit 3", F(3 * big ** 2 + 1, big ** 2 + 2 * big), 3, 1e-6)
# alternating series
alt = [S(lambda r: (-1) ** (r + 1), 1, n) for n in range(1, 9)]
assert alt == [1, 0, 1, 0, 1, 0, 1, 0]

# ---- exam practice
for n in NS:
    assert S(lambda r: 3 * r * r + r, 1, n) == n * (n + 1) ** 2
    assert 3 * s2(n) + s1(n) == F(1, 2) * n * (n + 1) * (2 * n + 1) + F(1, 2) * n * (n + 1) == F(1, 2) * n * (n + 1) * (2 * n + 2)
    assert S(lambda r: r ** 3, n + 1, 2 * n) == F(n * n * (3 * n + 1) * (5 * n + 3), 4)
    assert s3(2 * n) - s3(n) == F(1, 4) * (2 * n) ** 2 * (2 * n + 1) ** 2 - F(1, 4) * n * n * (n + 1) ** 2
    assert F(1, 4) * n * n * (4 * (2 * n + 1) ** 2 - (n + 1) ** 2) == F(1, 4) * n * n * (2 * (2 * n + 1) - (n + 1)) * (2 * (2 * n + 1) + (n + 1))
    assert 2 * (2 * n + 1) - (n + 1) == 3 * n + 1 and 2 * (2 * n + 1) + (n + 1) == 5 * n + 3
    assert S(lambda r: F(1, (r + 1) * (r + 3)), 1, n) == F(5, 12) - F(2 * n + 5, 2 * (n + 2) * (n + 3))
    assert F(1, 2) * (F(1, 2) + F(1, 3) - F(1, n + 2) - F(1, n + 3)) == F(5, 12) - F(2 * n + 5, 2 * (n + 2) * (n + 3))
    assert S(lambda r: F(r, factorial(r + 1)), 1, n) == 1 - F(1, factorial(n + 1))
    eq("ln sum", S(lambda r: log((r + 1) / r), 1, n), log(n + 1), 1e-9)
    # u_r = (2r+1)/(r^2 (r+1)^2)
    assert S(lambda r: F(2 * r + 1, r * r * (r + 1) ** 2), 1, n) == 1 - F(1, (n + 1) ** 2)
    # r(3r-1)
    assert S(lambda r: r * (3 * r - 1), 1, n) == n * n * (n + 1)
    assert 3 * s2(n) - s1(n) == F(1, 2) * n * (n + 1) * (2 * n + 1) - F(1, 2) * n * (n + 1) == F(1, 2) * n * (n + 1) * 2 * n
    assert S(lambda r: F(1, (3 * r - 1) * (3 * r + 2)), 1, n) == F(1, 3) * (F(1, 2) - F(1, 3 * n + 2)) == F(n, 2 * (3 * n + 2))
    assert F(1, 3) * F(3 * n, 2 * (3 * n + 2)) == F(n, 2 * (3 * n + 2))
    # stretch
    T = lambda r: F(r * (r + 1), 2)
    assert S(T, 1, n) == F(n * (n + 1) * (n + 2), 6)
    assert F(1, 2) * (s2(n) + s1(n)) == F(1, 12) * n * (n + 1) * (2 * n + 4)
    assert S(lambda r: 1 / T(r), 1, n) == F(2 * n, n + 1) == 2 * (1 - F(1, n + 1))
    assert S(lambda r: F(1, r * (r + 1) * (r + 2) * (r + 3)), 1, n) == F(1, 18) - F(1, 3 * (n + 1) * (n + 2) * (n + 3))
assert 20 ** 2 * 21 ** 2 // 4 == 44100 and 20 * 21 // 2 == 210 and 2 * 210 == 420 and 44100 - 420 == 43680
assert S(lambda r: r ** 3 - 2 * r, 1, 20) == 43680
assert F(1, 2) * F(1, 2) + 0 == F(1, 4)
# (d) and (e) of the u_r question
assert min(n for n in range(1, 200) if F(1, (n + 1) ** 2) < F(1, 1000)) == 31
assert F(1, 32 ** 2) < F(1, 1000) < F(1, 31 ** 2) and 31 ** 2 == 961 and 32 ** 2 == 1024
eq("sqrt 1000", sqrt(1000), 31.6228, 1e-4)
assert S(lambda r: F(2 * r + 1, r * r * (r + 1) ** 2), 11, 20) == F(320, 53361) == F(1, 121) - F(1, 441)
assert 121 * 441 == 53361 and 441 - 121 == 320 and (1 - F(1, 441)) - (1 - F(1, 121)) == F(320, 53361)
assert 1 * (1 + 1) == 2 and S(lambda r: r * (3 * r - 1), 1, 2) == 12 == 4 * 3
# stretch (c)
assert min(n for n in range(1, 1000) if F(2 * n, n + 1) > F(199, 100)) == 200
assert F(2 * 199, 200) == F(199, 100) and F(400, 201) > F(199, 100)
assert F(1, 1) == 1 and F(1, 6) == F(1, 6)
assert F(1, 3) * (F(1, 6) - F(1, 24)) == F(1, 24)   # n = 1
assert T(1) == 1 and T(2) == 3 and T(3) == 6

# ---- quiz
assert S(lambda r: 5, 1, 7) == 5 * 7
for n in NS:
    assert S(lambda r: 2 * r + 1, 1, n) == n * (n + 2) != n * (n + 1) and n * (n + 2) != (n + 1) ** 2
assert S(lambda r: r * r, 5, 20) == s2(20) - s2(4) != s2(20) - s2(5)
assert s3(10) == 3025 and s2(10) == 385 and s1(10) == 55 and 55 ** 2 == 3025
# six terms left with a gap of 3 (n at least 3)
n = 6
left = [F(1, r) for r in (1, 2, 3)] + [-F(1, r) for r in (n + 1, n + 2, n + 3)]
assert sum(left) == S(lambda r: F(1, r) - F(1, r + 3), 1, n) and len(left) == 6
assert F(1, r := 5) - F(1, 7) == F(2, 35) == 2 * F(1, 5 * 7)

# ---- reciprocals of S_n for the exam-box mention: formula for 1/(r(r+k)) with k = 1, 2, 3
for k in (1, 2, 3, 4):
    for r in range(1, 20):
        assert F(1, r * (r + k)) == F(1, k) * (F(1, r) - F(1, r + k))

print("ok")
