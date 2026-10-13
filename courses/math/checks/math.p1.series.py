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
# v2: warm-up
eq("w1", F(4 + 12 + 9), 25); eq("w2", 2 ** -3 * 16 ** 0.5, 0.5); eq("w3", 7 * 7 + 7 - 56, 0)

# v2: proofs. Pascal's rule, AP and GP sums against direct summation, S_infinity as a limit
for n in range(1, 12):
    for r in range(0, n):
        eq("pascal", comb(n, r) + comb(n, r + 1), comb(n + 1, r + 1))
        eq("pascal fact", factorial(n) // (factorial(r) * factorial(n - r)) + F(factorial(n), factorial(r + 1) * factorial(n - r - 1)), comb(n + 1, r + 1))
for a, d, n in ((7, 3, 15), (-2, 5, 11), (1.5, 0.25, 40)):
    terms = [a + k * d for k in range(n)]
    eq("ap sum direct", sum(terms), n / 2 * (2 * a + (n - 1) * d), 1e-9); eq("ap sum l", sum(terms), n / 2 * (terms[0] + terms[-1]), 1e-9)
    eq("ap pairs", terms[1] + terms[-2], a + terms[-1], 1e-9)
for a, r, n in ((6, 2, 8), (3, 0.5, 12), (5, -0.6, 9), (1, 3, 5)):
    terms = [a * r ** k for k in range(n)]
    eq("gp sum direct", sum(terms), a * (1 - r ** n) / (1 - r), 1e-9)
    eq("gp rS", sum(terms) - r * sum(terms), a - a * r ** n, 1e-9)
eq("sinf 0.5", sum(0.5 ** k for k in range(1, 40)), 1.0, 1e-9)
eq("sinf limit", sum(10 * 0.6 ** k for k in range(200)), 25, 1e-9)

# v2: spot the error
eq("spot ok u15", 7 + 14 * 3, 49); eq("spot ok S15", 15 / 2 * (7 + 49), 420); eq("spot bad u15", 7 + 15 * 3, 52); eq("spot bad S15", 15 / 2 * (7 + 52), 442.5)
eq("spot n=1", 7 + 1 * 3, 10)
assert sum(7 + 3 * k for k in range(15)) == 420

# v2: exam practice
eq("x1 c1", comb(5, 1) * 2, 10); eq("x1 c2", comb(5, 2) * 4, 40); eq("x1 c3", comb(5, 3) * 8, 80)
eq("x2 u30", 5 + 29 * 4, 121); eq("x2 S30", 15 * (5 + 121), 1890); assert sum(5 + 4 * k for k in range(30)) == 1890
eq("x3 r", 96 / 12, 8); eq("x3 a", 12 / 4, 3); eq("x3 S8", 3 * (2 ** 8 - 1) / (2 - 1), 765); eq("x3 direct", sum(3 * 2 ** k for k in range(8)), 765); eq("x3 u6", 3 * 2 ** 5, 96)
eq("x4 c1", comb(4, 1) * -3, -12); eq("x4 c2", comb(4, 2) * 9, 54); eq("x4 coef", 2 * 54 + 1 * -12, 96); eq("x4 sub", 108 - 12, 96)
# check x4 by full expansion
poly = [1]
for _ in range(4):
    poly = [(poly[i] if i < len(poly) else 0) + (-3 * poly[i - 1] if i > 0 else 0) for i in range(len(poly) + 1)]
assert poly == [1, -12, 54, -108, 81], poly
prod = [2 * poly[i] + (poly[i - 1] if i > 0 else 0) for i in range(len(poly))]
eq("x4 full", prod[2], 96)
eq("x5 S15", 15 * 31, 465); eq("x5 S16", 16 * 33, 528); assert sum(3 + 4 * k for k in range(15)) == 465 and sum(3 + 4 * k for k in range(16)) == 528
eq("x5 formula", 15 / 2 * (6 + 4 * 14), 465); eq("x5 leastn", min(n for n in range(1, 100) if n * (2 * n + 1) > 500), 16)
eq("x6 1-r", 10 / 25, 0.4); eq("x6 r2", 1 - 0.4, 0.6); eq("x6 S3", 10 * (1 - 0.6 ** 3) / 0.4, 19.6); eq("x6 direct", 10 + 6 + 3.6, 19.6)
# x7: AP 3, 3+d, 3+4d in GP with d = 6
d_ = 6
eq("x7 sq", (3 + d_) ** 2, 3 * (3 + 4 * d_)); eq("x7 quad", d_ ** 2 - 6 * d_, 0)
eq("x7 S10 AP", 5 * (6 + 9 * 6), 300); assert sum(3 + 6 * k for k in range(10)) == 300
eq("x7 GP terms", 3 * 3 ** 1, 9); eq("x7 GP 3rd", 3 + 4 * d_, 27); eq("x7 S10", 3 * (3 ** 10 - 1) / 2, 88572); assert sum(3 * 3 ** k for k in range(10)) == 88572
eq("x7 S12", 3 * (3 ** 12 - 1) / 2, 797160); eq("x7 S13", 3 * (3 ** 13 - 1) / 2, 2391483)
eq("x7 least", min(n for n in range(1, 40) if 3 * (3 ** n - 1) / 2 > 1e6), 13)
# stretch 1
from math import sqrt
for r in ((3 + sqrt(3)) / 6, (3 - sqrt(3)) / 6):
    eq("s1 eq", 6 * r * r - 6 * r + 1, 0, 1e-9); eq("s1 S", 1 / (1 - r), 6 * r, 1e-9); assert abs(r) < 1
eq("s1 r1", round((3 + sqrt(3)) / 6, 3), 0.789); eq("s1 r2", round((3 - sqrt(3)) / 6, 3), 0.211)
# stretch 2
eq("s2 c3", comb(6, 3), 20); eq("s2 c2", comb(6, 2), 15); eq("s2 a", 60 / 20, 3); eq("s2 rel", comb(6, 3) * 3 ** 3, 4 * comb(6, 2) * 3 ** 2); eq("s2 x4", comb(6, 4) * 3 ** 4, 1215)
print("ok")
