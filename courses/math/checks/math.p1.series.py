# checks/math.p1.series.py: recomputes every number in the Series chapter.
from fractions import Fraction as F
from math import isclose, comb, factorial

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

# factorials and coefficients
assert factorial(5) == 120 and factorial(7) // factorial(5) == 42 and comb(7, 3) == 35
assert comb(8, 3) == 56 and factorial(7) // (factorial(5) * factorial(2)) == 21 and comb(10, 10) == 1
assert comb(9, 4) == comb(9, 5)
pascal = {0: [1], 1: [1, 1], 2: [1, 2, 1], 3: [1, 3, 3, 1], 4: [1, 4, 6, 4, 1], 5: [1, 5, 10, 10, 5, 1], 6: [1, 6, 15, 20, 15, 6, 1]}
for n, row in pascal.items(): assert row == [comb(n, r) for r in range(n + 1)]
for n in range(1, 7): assert all(pascal[n][r] == pascal[n-1][r-1] + (pascal[n-1][r] if r < n else 0) for r in range(1, n + 1) if True)

# (2+3x)^4
co = [comb(4, r) * 2**(4 - r) * 3**r for r in range(5)]; assert co == [16, 96, 216, 216, 81]
assert (2 + 3)**4 == 625 == sum(co)
# (3-2x)^5 x^3, (2+x)^6
assert comb(5, 3) * 3**2 * (-2)**3 == -720
assert [comb(6, r) * 2**(6 - r) for r in range(3)] == [64, 192, 240]
# constant term (2x - 1/x)^6: r=3
assert 6 - 2 * 3 == 0 and comb(6, 3) * 2**3 * (-1)**3 == -160
# product (1+2x)(1-x)^6
c = [comb(6, r) * (-1)**r for r in range(7)]; assert c == [1, -6, 15, -20, 15, -6, 1]
assert c[4] + 2 * c[3] == -25
# exam (1+kx)^7
assert comb(7, 2) == 21 and 84 // 21 == 4 and comb(7, 3) * 2**3 == 280

# AP
assert 7 + 19 * 4 == 83 and 20 * (14 + 19 * 4) // 2 == 900 and 20 * (7 + 83) // 2 == 900
assert (399 - 102) // 3 + 1 == 100 and 50 * (102 + 399) == 25050 and sum(range(102, 400, 3)) == 25050
a, d = 5, 3
assert a + 4 * d == 17 and a + 8 * d == 29 and 10 * (2 * a + 9 * d) // 2 == 185
S = lambda n: n * (2 * a + (n - 1) * d) // 2
assert S(10) == 185 and S(11) == 220 and S(10) < 200 < S(11) and 11 * 40 // 2 == 220
assert all(n * (3 * n + 7) // 2 == S(n) for n in range(1, 15) if (n * (3 * n + 7)) % 2 == 0)

# GP
assert 6 * 2**7 == 768 and 6 * (2**8 - 1) == 1530
assert F(486, 18) == 27 and 3**3 == 27 and F(18, 9) == 2 and 2 * (3**6 - 1) // 2 == 728
eq("S inf 40", 40 / (1 + 0.5), 80 / 3)
eq("recurring", 0.27 / (1 - 0.01), 3 / 11); assert F(27, 99) == F(3, 11)
eq("ball", 5 + 2 * 3 / (1 - 0.6), 20); eq("7.5", 3 / (1 - 0.6), 7.5); eq("3 first bounce", 5 * 0.6, 3)

# exam AP/GP
d = 4
assert (4 + d)**2 == 4 * (4 + 3 * d) and (4, 4 + d, 4 + 3 * d) == (4, 8, 16) and 16 / 8 == 8 / 4 == 2
assert 10 * (2 * 4 + 9 * 4) // 2 == 220 and 5 * 44 == 220
assert F(1, 4) * 48 == 12 and F(3, 4) * 16 == 12
for r, a in ((F(1, 4), 48), (F(3, 4), 16)):
    assert a / (1 - r) == 64 and a * r == 12 and 16 * r * r - 16 * r + 3 == 0
assert 64 * 16 // 16 == 64 and (4 * F(1, 4) - 1) == 0 and (4 * F(3, 4) - 3) == 0

# try
assert (1 + 2 * 1)**5 == 243 and [comb(5, r) * 2**r for r in range(4)] == [1, 10, 40, 80]
assert comb(6, 4) * 2**2 == 60
assert 6 - 2 * 3 == 0 and comb(6, 3) * 2**3 == 160
c5 = [comb(5, r) * (-2)**r for r in range(6)]; assert c5[:3] == [1, -10, 40] and 3 * c5[2] + c5[1] == 110
assert 11 - 2 * 4 == 3 and 3 + 7 * 4 == 31 and 12 * (2 * 3 + 11 * 4) // 2 == 300
mult = list(range(7, 100, 7)); assert mult[-1] == 98 and len(mult) == 14 and sum(mult) == 735
assert 3 * 2**9 == 1536 and 3 * (2**10 - 1) == 3069
r = 1 - F(20, 25); assert r == F(1, 5) and 20 * r == 4
# last two exams
a_ = F(4, 5)
assert comb(6, 1) * 2**5 == 192 and comb(6, 2) * 2**4 == 240 and F(192, 240) == a_
eq("x3", comb(6, 3) * 2**3 * float(a_)**3, 81.92); eq("0.512", 0.8**3, 0.512); assert 160 * F(64, 125) == F(10240, 125)
assert F(512, 1000) == F(64, 125)
d = 4; t = [2 + d, 2 + 4 * d, 2 + 13 * d]; assert t == [6, 18, 54] and t[1]**2 == t[0] * t[2] and 18 / 6 == 54 / 18 == 3
assert 4 + 16 * d + 16 * d**2 == 4 + 28 * d + 13 * d**2 and 3 * d**2 == 12 * d
assert 20 * (4 + 19 * 4) // 2 == 800
# general: d = 2a
for a in (1, 2, 5): d = 2 * a; t = [a + d, a + 4 * d, a + 13 * d]; assert t[1]**2 == t[0] * t[2]

# quiz
assert comb(4, 2) * (-2)**2 == 24 and comb(4, 2) == 6 and comb(4, 2) * 2 == 12
assert 5 + 24 * 4 == 101 and (101 - 5) // 4 == 24
assert abs(-F(1, 2)) < 1 and 2 * F(15, 2) == 15 and 6**2 == 3 * 12
# FIX additions
S = lambda a, d, n: n * (2 * a + (n - 1) * d) // 2
assert 24000 + 1500 * 10 == 39000 < 40000 < 24000 + 1500 * 11 == 40500
assert S(24000, 1500, 12) == 387000 and 6 * 64500 == 387000
v = lambda n: 18000 * 0.85**n
eq("v6", round(v(6), 2), 6788.69); eq("v7", round(v(7), 2), 5770.39); assert v(6) > 6000 > v(7)
assert 2 * 18 == 36 and 6**2 == 36 and 18 - 2 == 16 and 18 / 6 == 6 / 2 == 3
print("ok")
