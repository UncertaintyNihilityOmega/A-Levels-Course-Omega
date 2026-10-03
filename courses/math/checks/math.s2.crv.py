# checks/math.s2.crv.py: recomputes every number in the continuous random variables chapter.
from math import isclose, sqrt, sin, pi, comb
from fractions import Fraction as F

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

def integ(f, a, b, n=20000):
    # Simpson's rule
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n))
    return s * h / 3

def solve(g, lo, hi):
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(lo) * g(mid) <= 0: hi = mid
        else: lo = mid
    return (lo + hi) / 2

# Waiting time f = (10 - t)/50
f = lambda t: (10 - t) / 50
eq("area", integ(f, 0, 10), 1); eq("P>5", integ(f, 5, 10), 0.25)
ET = integ(lambda t: t * f(t), 0, 10); ET2 = integ(lambda t: t * t * f(t), 0, 10)
eq("E T", ET, 10 / 3); eq("E T2", ET2, 50 / 3); eq("Var T", ET2 - ET ** 2, 50 / 9); eq("Var T dec", sf(50 / 9, 4), 5.556)
eq("sd T", sf(sqrt(50 / 9)), 2.36); eq("E T 3 s.f.", sf(ET, 3), 3.33)
eq("median T", solve(lambda m: integ(f, 0, m) - 0.5, 0, 10), 10 - 5 * sqrt(2)); eq("median T 3sf", sf(10 - 5 * sqrt(2)), 2.93)

# kx^2 on 0..3
k = 1 / 9; eq("k", 1 / integ(lambda x: x * x, 0, 3), 1 / 9)
eq("P 1<X<2", integ(lambda x: k * x * x, 1, 2), 7 / 27); eq("P 3sf", sf(7 / 27), 0.259)

# kx(4-x)
kk = 1 / integ(lambda x: x * (4 - x), 0, 4); eq("k 3/32", kk, 3 / 32)
eq("P>3", integ(lambda x: kk * x * (4 - x), 3, 4), 5 / 32); eq("P>3 3sf", sf(5 / 32), 0.156)
g = lambda x: 3 / 32 * x * (4 - x)
eq("E", integ(lambda x: x * g(x), 0, 4), 2); eq("E2", integ(lambda x: x * x * g(x), 0, 4), 4.8)
eq("Var", 4.8 - 4, 0.8)

# 1/(2 sqrt x), 1..4
h = lambda x: 0.5 / sqrt(x)
eq("area", integ(h, 1, 4), 1); eq("E", integ(lambda x: x * h(x), 1, 4), 7 / 3); eq("E 3sf", sf(7 / 3), 2.33)
eq("median", solve(lambda m: integ(h, 1, m) - 0.5, 1, 4), 2.25)
eq("sqrt m", sqrt(2.25), 1.5)

# 3/8 x^2 on 0..2
c = lambda x: 3 / 8 * x * x
eq("area", integ(c, 0, 2), 1); eq("90th", solve(lambda q: integ(c, 0, q) - 0.9, 0, 2), 7.2 ** (1 / 3)); eq("90th 3sf", sf(7.2 ** (1 / 3)), 1.93)
eq("q3", 7.2, 0.9 * 8)
eq("E", integ(lambda x: x * c(x), 0, 2), 1.5); eq("E2", integ(lambda x: x * x * c(x), 0, 2), 12 / 5)
eq("Var", 12 / 5 - 1.5 ** 2, 0.15); eq("median", solve(lambda m: integ(c, 0, m) - 0.5, 0, 2), 4 ** (1 / 3)); eq("median 3sf", sf(4 ** (1 / 3)), 1.59)

# 3/x^4, x>=1 : closed forms with large upper limit
big = 1e4
p = lambda x: 3 / x ** 4
eq("area", 3 * (1 / 3 - big ** -3 / 3), 1, 1e-9)
eq("P>2", 3 * (2 ** -3 / 3), 1 / 8); eq("E", 3 * (1 / 2), 3 / 2); eq("E2", 3.0, 3.0); eq("Var", 3 - 9 / 4, 3 / 4)
eq("median", 2 ** (1 / 3), 1.26, 5e-3); eq("median check", 1 - (2 ** (1 / 3)) ** -3, 0.5); eq("median 3sf", sf(2 ** (1 / 3)), 1.26)
eq("E1/X", 3 / 4, 0.75)
eq("numeric E", integ(lambda x: x * p(x), 1, 2000, 200000), 1.5, 1e-3)
eq("numeric E1/X", integ(lambda x: 3 * x ** -5, 1, 500), 0.75, 1e-4)

# k/x^5
eq("area5", 4 * (1 / 4), 1); eq("E5", 4 / 3, 4 * (1 / 3)); eq("E25", 2.0, 4 * (1 / 2)); eq("Var5", 2 - 16 / 9, 2 / 9); eq("Var5 3sf", sf(2 / 9), 0.222)
eq("median5", sf(2 ** 0.25), 1.19); eq("m5 check", 1 - (2 ** .25) ** -4, 0.5)

# try
eq("t1 k", 8 * (1 / 8), 1); eq("t1 P", 4 / 16, 0.25); eq("t1 E", 64 / 24, 8 / 3); eq("t1 q", sqrt(0.25 * 16), 2); eq("t1 uq", sf(sqrt(12)), 3.46)
eq("t2 k", 4 * 0.25, 1); eq("t2 E", 0.25 * (8 / 3 + 2), 7 / 6); eq("t2 num", integ(lambda x: x * 0.25 * (x + 1), 0, 2), 7 / 6)
t3 = lambda x: 3 / 16 * (4 - x * x)
eq("t3 area", integ(t3, 0, 2), 1); eq("t3 P", integ(t3, 1, 2), 5 / 16); eq("t3 E", integ(lambda x: x * t3(x), 0, 2), 3 / 4)
t4 = lambda x: 0.5 * sin(x)
eq("t4 area", integ(t4, 0, pi), 1); eq("t4 P", integ(t4, 0, pi / 3), 0.25); eq("t4 median", solve(lambda m: integ(t4, 0, m) - 0.5, 0, pi), pi / 2); eq("t4 m 3sf", sf(pi / 2), 1.57)
eq("t5 area", 8 * 2 ** -3, 1); eq("t5 E", 12 * 2 ** -2, 3); eq("t5 E2", 24 / 2, 12); eq("t5 Var", 12 - 9, 3)
eq("t5 median", sf(16 ** (1 / 3)), 2.52); eq("t5 mcheck", 1 - 8 / 16, 0.5); eq("t5 P", 8 * 5 ** -3, 0.064)
eq("t6 E2", 3.2 + 36, 39.2)
eq("t7 k", 4 * 0.25, 1); eq("t7 P", 0.25 * (2 * 2 - 2), 0.5)
t8 = lambda x: x - 1; eq("t8 area", integ(t8, 0, 3), 1.5)
t9 = lambda x: 3 / 16 * sqrt(x)
eq("t9 area", integ(t9, 0, 4), 1, 1e-6); eq("t9 E", integ(lambda x: x * t9(x), 0, 4), 2.4, 1e-6); eq("t9 E2", integ(lambda x: x * x * t9(x), 0, 4), 48 / 7, 1e-6)
eq("t9 Var", 48 / 7 - 2.4 ** 2, 192 / 175); eq("t9 Var 3sf", sf(192 / 175), 1.10); eq("t9 med", solve(lambda m: integ(t9, 0, m) - 0.5, 0, 4), 4 ** (2 / 3), 1e-5); eq("t9 med 3sf", sf(4 ** (2 / 3)), 2.52)
eq("t9 coef", 3 / 16 * 64 / 5, 2.4); eq("t9 coef2", 3 / 16 * 256 / 7, 48 / 7)
eq("t10 E", 50 / 8, 6.25); eq("t10 P", sf(comb(50, 5) * (1 / 8) ** 5 * (7 / 8) ** 45), 0.159)
print("ok")
