# checks/math.fm.crv.py: recomputes every number in Continuous random variables.
# Standard library only: exact values with Fraction, Simpson integration and bisection to confirm them.
from fractions import Fraction as F
from math import isclose, sqrt, e, log


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n))
    return s * h / 3


def bisect(g, lo, hi, it=200):
    for _ in range(it):
        mid = (lo + hi) / 2
        if (g(lo) < 0) == (g(mid) < 0):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ---- warm-up
eq("w1 k", float(F(9, 2) * F(2, 9)), 1)
eq("w2", (8 - 4) - (1 - 2), 5)
eq("w3", float(1 - F(4, 16)), 0.75)

# ---- key box: piecewise PDF 1/10, 1/5
eq("key area", 2 * 0.1 + 4 * 0.2, 1)

# ---- eg: kx on [0,2), 2k on [2,5]
k = F(1, 8)
eq("eg1 area", float(2 * k + 6 * k), 1)
p = simpson(lambda x: float(k) * x, 1, 2) + simpson(lambda x: 2 * float(k), 2, 3)
eq("eg1 P", p, 7 / 16)
eq("eg1 parts", 3 / 16 + 4 / 16, 7 / 16)

# ---- exam eg: ax, b, c(7-x), continuous
a = 1 / 10
b = 2 * a
c = b / 2
eq("ex1 a", 10 * a, 1)
eq("ex1 area", simpson(lambda x: a * x, 0, 2) + simpson(lambda x: b, 2, 5) + simpson(lambda x: c * (7 - x), 5, 7), 1)
eq("ex1 b", b, 1 / 5)
eq("ex1 c", c, 1 / 10)
eq("ex1 P", simpson(lambda x: b, 3, 5) + simpson(lambda x: c * (7 - x), 5, 6), 11 / 20)
eq("ex1 bracket", 24 - 22.5, 1.5)

# ---- running example
f1 = lambda x: x / 2
f2 = lambda x: (4 - x) / 6
eq("run area", simpson(f1, 0, 1) + simpson(f2, 1, 4), 1)
eq("run join", f1(1), f2(1))
Fr = lambda x: 0 if x < 0 else (x * x / 4 if x <= 1 else ((8 * x - x * x - 4) / 12 if x <= 4 else 1))
for x in (0.3, 0.9, 1.0, 1.7, 2.5, 3.9):
    num = simpson(f1, 0, min(x, 1)) + (simpson(f2, 1, x) if x > 1 else 0)
    eq(f"run F({x})", Fr(x), num)
eq("run F(1)", Fr(1), 0.25)
eq("run F(4)", Fr(4), 1)
eq("run join F", 1 / 4, 3 / 12)
# percentiles
m = 4 - sqrt(6)
eq("run median", Fr(m), 0.5)
eq("run median val", sf(m), 1.55)
eq("run other root", 4 + sqrt(6), 6.449489742783178, 1e-9)
eq("run Q1", Fr(1), 0.25)
q3 = 4 - sqrt(3)
eq("run Q3", Fr(q3), 0.75)
eq("run Q3 val", sf(q3), 2.27)
eq("run IQR", sf(q3 - 1), 1.27)
eq("run IQR exact", 3 - sqrt(3), q3 - 1)
p90 = 4 - sqrt(1.2)
eq("run P90", Fr(p90), 0.9)
eq("run P90 val", sf(p90), 2.90)
# moments
EX = simpson(lambda x: x * f1(x), 0, 1) + simpson(lambda x: x * f2(x), 1, 4)
EX2 = simpson(lambda x: x * x * f1(x), 0, 1) + simpson(lambda x: x * x * f2(x), 1, 4)
eq("run EX", EX, 5 / 3)
eq("run EX2", EX2, 7 / 2)
eq("run Var", EX2 - EX ** 2, 13 / 18)
eq("run EX parts", 1 / 6 + (1 / 6) * (32 / 3 - 5 / 3), 5 / 3)
eq("run EX parts2", 32 / 3 - 5 / 3, 9)
eq("run EX2 parts", 1 / 8 + (1 / 6) * (64 / 3 - 13 / 12), 7 / 2)
eq("run EX2 bracket", (4 * 64 / 3 - 64) - (4 / 3 - 1 / 4), 64 / 3 - 13 / 12)
eq("run EX2 27/8", (1 / 6) * (64 / 3 - 13 / 12), 27 / 8)
# mode: maximum of f at x = 1
xs = [i / 1000 * 4 for i in range(1001)]
fv = lambda x: f1(x) if x <= 1 else f2(x)
eq("run mode", max(xs, key=fv), 1.0, 0.004)
assert 1.55 < 5 / 3  # median < mean

# ---- CDF from F eg: (x^2-4)/12 on [2,4]
eq("F4", (16 - 4) / 12, 1)
eq("F3", (9 - 4) / 12, 5 / 12)
eq("P(X>3)", 1 - 5 / 12, 7 / 12)
eq("P(X>3) int", simpson(lambda x: x / 6, 3, 4), 7 / 12)
# F with constant c = 9
eq("c", 3 ** 2 / 9, 1)
eq("P(2<X<3)", 4 / 9 - 1 / 9, 1 / 3)
eq("P int", simpson(lambda x: 2 * (x - 1) / 9, 2, 3), 1 / 3)

# ---- exam eg: F = x(12-x)/36 on [0,6]
G = lambda x: x * (12 - x) / 36
eq("ee F(6)", G(6), 1)
for x in (0.5, 2, 5.9):
    assert (12 - 2 * x) / 36 >= 0
m2 = 6 - sqrt(18)
eq("ee median", G(m2), 0.5)
eq("ee median val", sf(m2), 1.76)
assert 6 + sqrt(18) > 6
a90 = 6 - sqrt(3.6)
eq("ee a", G(a90), 0.9)
eq("ee a val", sf(a90), 4.10)
eq("ee eq", 12 ** 2 - 4 * 32.4, 14.4)

# ---- E(X) and Var for f = 3/x^4
eq("pareto area", simpson(lambda x: 3 * x ** -4, 1, 2000, 200000), 1 - 2000 ** -3, 1e-7)
EX_p = 3 / 2
eq("pareto EX", simpson(lambda x: 3 * x ** -3, 1, 2000, 200000), 1.5 * (1 - 2000 ** -2), 1e-7)
eq("pareto EX2", 3.0, 3.0)
eq("pareto Var", 3 - 1.5 ** 2, 0.75)
eq("pareto E1/X", simpson(lambda x: 3 * x ** -5, 1, 2000, 200000), 0.75 * (1 - 2000 ** -4), 1e-7)
eq("1/EX", 1 / 1.5, 2 / 3)
# E(X^3) integrand 3/x grows like log
assert simpson(lambda x: 3 / x, 1, 1e6, 400000) > 40

# ---- real context
ft = lambda t: 3 * t * (4 - t) / 32
eq("ctx area", simpson(ft, 0, 4), 1)
Ft = lambda t: (6 * t * t - t ** 3) / 32
eq("ctx F3", Ft(3), 27 / 32)
eq("ctx P", 1 - Ft(3), 5 / 32)
eq("ctx F4", Ft(4), 1)
eq("ctx F int", simpson(ft, 0, 3), Ft(3))
eq("ctx ET", simpson(lambda t: t * ft(t), 0, 4), 2)
eq("ctx ET2", simpson(lambda t: t * t * ft(t), 0, 4), 4.8)
eq("ctx ET2 exact", 3 / 32 * (256 - 1024 / 5), 4.8)
eq("ctx Var", 4.8 - 4, 0.8)
eq("ctx E1/T", simpson(lambda t: ft(t) / t, 1e-9, 4), 0.75, 1e-6)
eq("ctx EC", 10 + 24 * 0.75, 28)
eq("ctx naive", 10 + 24 / 2, 22)
eq("ctx 3/32*32/3", 3 / 32 * 32 / 3, 1)

# ---- CDF method: Y = X^3, f = x/2 on [0,2]
Fx = lambda x: x * x / 4
Gy = lambda y: Fx(y ** (1 / 3))
eq("Y3 G(8)", Gy(8), 1)
eq("Y3 form", Gy(5), 5 ** (2 / 3) / 4)
gy = lambda y: y ** (-1 / 3) / 6
eq("Y3 g area", 1 / 6 * 1.5 * 8 ** (2 / 3), 1)
h = 1e-6
eq("Y3 deriv", (Gy(3 + h) - Gy(3 - h)) / (2 * h), gy(3), 1e-6)

# ---- Y = 1/X
Fp = lambda x: 1 - x ** -3
Gi = lambda y: 1 - Fp(1 / y)
eq("inv G", Gi(0.4), 0.4 ** 3)
eq("inv area", simpson(lambda y: 3 * y * y, 0, 1), 1)
eq("inv EY", simpson(lambda y: 3 * y ** 3, 0, 1), 0.75)

# ---- exam eg: kx, k on [0,3]
k = F(2, 5)
eq("xe area", float(k / 2 + 2 * k), 1)
fe = lambda x: float(k) * x if x <= 1 else float(k)
eq("xe EX", simpson(lambda x: x * fe(x), 0, 1) + simpson(lambda x: x * fe(x), 1, 3), 26 / 15)
eq("xe EX parts", 2 / 15 + 8 / 5, 26 / 15)
Fe = lambda x: x * x / 5 if x <= 1 else (2 * x - 1) / 5
eq("xe F1", Fe(1), 0.2)
eq("xe F3", Fe(3), 1)
eq("xe F1 form", 1 / 5 + 2 / 5 * (1.7 - 1), Fe(1.7))
eq("xe median", Fe(1.75), 0.5)
Gye = lambda y: Fe(sqrt(y))
eq("xe G(1)", Gye(1), 0.2)
eq("xe G(9)", Gye(9), 1)
eq("xe G form", Gye(4), (2 * 2 - 1) / 5)
ge = lambda y: 0.2 if y <= 1 else 1 / (5 * sqrt(y))
eq("xe g area", simpson(ge, 0, 1) + simpson(ge, 1, 9), 1)
eq("xe g area2", 1 / 5 + 2 / 5 * (3 - 1), 1)
eq("xe deriv", (Gye(5 + h) - Gye(5 - h)) / (2 * h), ge(5), 1e-6)
# EX^2 via Y
eq("xe EY", simpson(lambda x: x * x * fe(x), 0, 1) + simpson(lambda x: x * x * fe(x), 1, 3), simpson(lambda y: y * ge(y), 0, 1) + simpson(lambda y: y * ge(y), 1, 9))

# ---- spot the error
fs = lambda x: x / 6 if x <= 2 else 1 / 3
eq("spot area", simpson(fs, 0, 2) + simpson(fs, 2, 4), 1)
eq("spot F2", 4 / 12, 1 / 3)
eq("spot wrong F4", (4 - 2) / 3, 2 / 3)
eq("spot right F", 1 / 3 + (4 - 2) / 3, 1)
eq("spot (x-1)/3", (4 - 1) / 3, 1)
eq("spot wrong median", 0.5 * 3 + 2, 3.5)
eq("spot median", 0.5 * 3 + 1, 2.5)
eq("spot score", 1 + 1 + 1 + 1, 4)

# ---- try block
eq("t1", 27 / 26 - 1 / 26, 1)
eq("t1 P", simpson(lambda x: 3 / 26 * x * x, 2, 3), 19 / 26)
eq("t2 area", 0.25 * 1 + 1.5 * 0.5, 1)
eq("t2 F2", 0.25 + 0.5 * 1, 0.75)
eq("t3 median", sf(3 * 0.5 ** (1 / 3)), 2.38)
eq("t4 EX", simpson(lambda x: x * x / 8, 0, 4), 8 / 3)
eq("t4 EX2", simpson(lambda x: x ** 3 / 8, 0, 4), 8)
eq("t4 Var", 8 - 64 / 9, 8 / 9)
eq("t4 Esqrt", simpson(lambda x: x ** 1.5 / 8, 0, 4), 8 / 5)
eq("t4 form", 1 / 8 * 2 / 5 * 32, 8 / 5)
# Y = 2X + 1, F = x^2/16
Gt5 = lambda y: ((y - 1) / 2) ** 2 / 16
eq("t5 G", Gt5(9), 1)
eq("t5 G form", Gt5(5), (5 - 1) ** 2 / 64)
eq("t5 g", (Gt5(4 + h) - Gt5(4 - h)) / (2 * h), (4 - 1) / 32, 1e-6)
# Y = X^2, uniform on 0..2
Gt6 = lambda y: sqrt(y) / 2
eq("t6 G", Gt6(4), 1)
eq("t6 g", (Gt6(1 + h) - Gt6(1 - h)) / (2 * h), 1 / (4 * 1), 1e-6)
# Y = 4 - X, f = x/2
Gt7 = lambda y: 1 - (4 - y) ** 2 / 4
eq("t7 G(2)", Gt7(2), 0)
eq("t7 G(4)", Gt7(4), 1)
eq("t7 g", (Gt7(3 + h) - Gt7(3 - h)) / (2 * h), (4 - 3) / 2, 1e-6)
eq("t7 P", 1 - ((4 - 3) ** 2) / 4, Gt7(3))

# ---- exam practice
Fq1 = lambda x: (x - 1) ** 2 / 9
eq("q1 F4", Fq1(4), 1)
eq("q1 P", Fq1(3) - Fq1(2), 1 / 3)
eq("q1 median", Fq1(1 + 3 / sqrt(2)), 0.5)
eq("q1 median val", sf(1 + 3 / sqrt(2)), 3.12)
eq("q2 EX", simpson(lambda x: x * x / 8, 0, 4), 8 / 3)
eq("q2 EX2", 8, simpson(lambda x: x ** 3 / 8, 0, 4))
eq("q2 Esqrt", 1 / 8 * 2 / 5 * 32, 8 / 5)
eq("q3 area", simpson(lambda x: 3 * x * x / 8, 0, 2), 1)
Gq3 = lambda y: ((y - 1) / 2) ** 3 / 8
eq("q3 G", Gq3(5), 1)
eq("q3 G form", Gq3(3), (3 - 1) ** 3 / 64)
eq("q3 g", (Gq3(2.5 + h) - Gq3(2.5 - h)) / (2 * h), 3 * (2.5 - 1) ** 2 / 64, 1e-6)
eq("q4 area", simpson(lambda x: 2 * x / 9, 0, 3), 1)
Gq4 = lambda y: y ** 4 / 9
eq("q4 G", Gq4(sqrt(3)), 1)
eq("q4 g", (Gq4(1.2 + h) - Gq4(1.2 - h)) / (2 * h), 4 * 1.2 ** 3 / 9, 1e-6)
eq("q4 EY", simpson(lambda y: y * 4 * y ** 3 / 9, 0, sqrt(3)), 4 * sqrt(3) / 5)
eq("q4 EY2", simpson(lambda x: sqrt(x) * 2 * x / 9, 0, 3), 4 * sqrt(3) / 5)
eq("q4 EY val", sf(4 * sqrt(3) / 5), 1.39)
eq("q4 form", 4 / 45 * sqrt(3) ** 5, 4 * sqrt(3) / 5)
eq("q4 form2", 4 / 45 * 3 ** 2.5, 4 * sqrt(3) / 5)
# Q5: triangle peak at 2 on [0,6]
fq5 = lambda x: x / 6 if x <= 2 else (6 - x) / 12
eq("q5 area", simpson(fq5, 0, 2) + simpson(fq5, 2, 6), 1)
eq("q5 areas", 2 / 6 * 1 + 4 / 6, 1)
Fq5 = lambda x: x * x / 12 if x <= 2 else 1 - (6 - x) ** 2 / 24
eq("q5 join", Fq5(2), 1 / 3)
eq("q5 join2", 1 - 16 / 24, 1 / 3)
eq("q5 F6", Fq5(6), 1)
for x in (3, 4.5):
    eq(f"q5 F({x})", Fq5(x), simpson(fq5, 0, 2) + simpson(fq5, 2, x))
mq5 = 6 - 2 * sqrt(3)
eq("q5 median", Fq5(mq5), 0.5)
eq("q5 median val", sf(mq5), 2.54)
# Q6: 1/x on [1,e]
eq("q6 area", simpson(lambda x: 1 / x, 1, e), 1)
eq("q6 median", log(sqrt(e)), 0.5)
eq("q6 median val", sf(sqrt(e)), 1.65)
EXq6 = e - 1
EX2q6 = (e * e - 1) / 2
eq("q6 EX", simpson(lambda x: x / x, 1, e), EXq6)
eq("q6 EX val", sf(EXq6), 1.72)
eq("q6 EX2", simpson(lambda x: x * x / x, 1, e), EX2q6)
eq("q6 Var", sf(EX2q6 - EXq6 ** 2), 0.242)

# ---- stretch
Fs1 = lambda x: (x ** 3 + 1) / 2
eq("s1 area", simpson(lambda x: 1.5 * x * x, -1, 1), 1)
Gs1 = lambda y: Fs1(sqrt(y)) - Fs1(-sqrt(y))
eq("s1 G", Gs1(0.36), 0.36 ** 1.5)
eq("s1 G(1)", Gs1(1), 1)
eq("s1 g", (Gs1(0.5 + h) - Gs1(0.5 - h)) / (2 * h), 1.5 * sqrt(0.5), 1e-6)
fs2 = lambda x: 2 / (x + 1) ** 3
eq("s2 area", simpson(fs2, 0, 4000, 200000), 1 - 1 / 4001 ** 2, 1e-6)
# exact tail check of E(X): antiderivative -2/(x+1) + 1/(x+1)^2 from 0 to T
T = 4000.0
eq("s2 EX exact", (-2 / (T + 1) + 1 / (T + 1) ** 2) - (-2 + 1), 1 - 2 / (T + 1) + 1 / (T + 1) ** 2, 1e-12)
eq("s2 EX num", simpson(lambda x: x * fs2(x), 0, T, 400000), (-2 / (T + 1) + 1 / (T + 1) ** 2) - (-2 + 1), 1e-6)
eq("s2 int 1-F", simpson(lambda x: 1 / (x + 1) ** 2, 0, T, 400000), 1 - 1 / (T + 1), 1e-6)
assert simpson(lambda x: 2 * x * x / (x + 1) ** 3, 0, 1e4, 400000) > 15  # grows like 2 ln x
for x in (1, 10, 100):
    assert 2 * x * x / (x + 1) ** 3 >= 1 / (4 * x)

# ---- added examples: f = a + bx with E(X) = 10/9
b_, a_ = F(1, 6), F(1, 3)
eq("ab area", float(2 * a_ + 2 * b_), 1)
eq("ab mean", float(2 * a_ + F(8, 3) * b_), 10 / 9)
eq("ab int", simpson(lambda x: x * (float(a_) + float(b_) * x), 0, 2), 10 / 9)
eq("ab diff", 8 / 3 - 2, 2 / 3)
eq("ab b", (10 / 9 - 1) / (2 / 3), 1 / 6)
eq("ab a", (1 - 2 / 6) / 2, 1 / 3)
assert a_ > 0 and b_ > 0
# warranty refund
eq("wr F1", Ft(1), 5 / 32)
eq("wr F2", Ft(2), 16 / 32)
eq("wr P12", Ft(2) - Ft(1), 11 / 32)
eq("wr E", 60 * Ft(1) + 20 * (Ft(2) - Ft(1)), 16.25)
eq("wr E frac", (300 + 220) / 32, 16.25)
eq("wr int", 60 * simpson(ft, 0, 1) + 20 * simpson(ft, 1, 2), 16.25)

# ---- smooth peak: 12x^2(1-x)
fm_ = lambda x: 12 * x * x * (1 - x)
eq("sm area", simpson(fm_, 0, 1), 1)
eq("sm mode", max([i / 10000 for i in range(10001)], key=fm_), 2 / 3, 1e-4)
eq("sm f'", 24 * (2 / 3) - 36 * (2 / 3) ** 2, 0, 1e-12)
eq("sm EX", simpson(lambda x: x * fm_(x), 0, 1), 3 / 5)
eq("sm EX frac", 12 * (1 / 4 - 1 / 5), 3 / 5)
eq("sm EX2", simpson(lambda x: x * x * fm_(x), 0, 1), 2 / 5)
eq("sm EX2 frac", 12 * (1 / 5 - 1 / 6), 2 / 5)
eq("sm Var", 2 / 5 - 9 / 25, 1 / 25)
Fm_ = lambda x: 4 * x ** 3 - 3 * x ** 4
eq("sm F", Fm_(0.6), simpson(fm_, 0, 0.6))
eq("sm F(.6)", sf(Fm_(0.6), 4), 0.4752)
eq("sm F(.65)", sf(Fm_(0.65), 4), 0.5630)
eq("sm cubes", 4 * 0.274625 - 3 * 0.17850625, Fm_(0.65), 1e-12)
med = bisect(lambda x: Fm_(x) - 0.5, 0.5, 0.9)
eq("sm median", sf(med, 3), 0.614)
assert 0.6 < med < 0.65 and med > 3 / 5 and 2 / 3 > med

print("ok")
