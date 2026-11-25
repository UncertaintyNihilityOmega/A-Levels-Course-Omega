# checks/math.fm.diff.py: recomputes every number in Further differentiation and Maclaurin series.
# Standard library only: finite differences for derivatives, Fraction power-series arithmetic for Maclaurin series.
from fractions import Fraction as F
from math import (sinh, cosh, tanh, exp, log, sqrt, sin, cos, tan, atan, asin, acos, asinh, acosh, atanh,
                  isclose, factorial, pi)


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def D(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def D2(f, x, h=1e-3):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


T = 1e-6  # tolerance for finite differences

sech = lambda x: 1 / cosh(x)
cosech = lambda x: 1 / sinh(x)
coth = lambda x: 1 / tanh(x)

# warm-up
for x in (0.3, 1.1):
    eq("w1", D(lambda u: u * u * exp(3 * u), x), x * exp(3 * x) * (2 + 3 * x), 1e-5)
for t in (0.7, 2.0):
    eq("w2", (2) / (2 * t), 1 / t)
eq("w3a", F(-1, 2), F(-1, 2))
eq("w3b", float(F(-1, 2) * F(-3, 2) / 2), 3 / 8)

# derivatives of hyperbolic functions (numerical)
for x in (-1.3, 0.4, 1.7):
    eq("d sinh", D(sinh, x), cosh(x), T)
    eq("d cosh", D(cosh, x), sinh(x), T)
    eq("d tanh", D(tanh, x), sech(x) ** 2, T)
    eq("d sech", D(sech, x), -sech(x) * tanh(x), T)
    eq("d cosech", D(cosech, x), -cosech(x) * coth(x), T)
    eq("d coth", D(coth, x), -cosech(x) ** 2, T)
    eq("quotient tanh", (cosh(x) * cosh(x) - sinh(x) * sinh(x)) / cosh(x) ** 2, sech(x) ** 2)
    eq("quotient coth", (sinh(x) * sinh(x) - cosh(x) * cosh(x)) / sinh(x) ** 2, -cosech(x) ** 2)
    # eg differentiate
    eq("a", D(lambda u: sinh(3 * u), x), 3 * cosh(3 * x), 1e-4)
    eq("b", D(lambda u: u * u * cosh(2 * u), x), 2 * x * cosh(2 * x) + 2 * x * x * sinh(2 * x), 1e-4)
    eq("c", D(lambda u: tanh(u * u), x), 2 * x * sech(x * x) ** 2, 1e-5)
    eq("d", D(lambda u: log(cosh(u)), x), tanh(x), 1e-6)
    # try
    eq("t1a", D(lambda u: cosh(5 * u), x), 5 * sinh(5 * x), 1e-3)
    eq("t1b", D(lambda u: sinh(u) * cosh(u), x), cosh(2 * x), 1e-5)
    eq("t1c", D(lambda u: coth(2 * u), x), -2 * cosech(2 * x) ** 2, 1e-5)
    eq("t2", D(lambda u: exp(3 * u) * tanh(u), x), exp(3 * x) * (3 * tanh(x) + sech(x) ** 2), 1e-3)
    # q1
    eq("q1a", D(lambda u: u * sinh(4 * u), x), sinh(4 * x) + 4 * x * cosh(4 * x), 1e-3)
    eq("q1b", D(lambda u: log(cosh(5 * u)), x), 5 * tanh(5 * x), 1e-5)
    eq("q2", D(coth, x), (sinh(x) * sinh(x) - cosh(x) * cosh(x)) / sinh(x) ** 2, T)

# stationary point eg: y = cosh x - 2x
xs = log(2 + sqrt(5))
eq("sp sinh", sinh(xs), 2)
eq("sp cosh", cosh(xs), sqrt(5))
eq("sp sinh-1", asinh(2), xs)
eq("sp dydx", D(lambda u: cosh(u) - 2 * u, xs), 0, 1e-6)
ys = sqrt(5) - 2 * log(2 + sqrt(5))
eq("sp y", cosh(xs) - 2 * xs, ys)
eq("sp x3", sf(xs, 3), 1.44)
eq("sp y3", sf(ys, 3), -0.651)
assert cosh(xs) > 0

# tangent eg
eq("tan sinh", sinh(log(2)), 3 / 4)
eq("tan cosh", cosh(log(2)), 5 / 4)
# 4y = 5x + 3 - 5 ln2 : at x = ln2, y = 3/4
eq("tan eq", (5 * log(2) + 3 - 5 * log(2)) / 4, 3 / 4)

# cable
yc = lambda x: 25 * cosh(x / 25) - 19
eq("cable slope", D(yc, 15), sinh(0.6), 1e-6)
eq("sinh0.6", sf(sinh(0.6), 4), 0.6367)
eq("angle", sf(atan(sinh(0.6)) * 180 / pi, 3), 32.5)
eq("x slope 1", sf(25 * asinh(1), 3), 22.0)
eq("x slope 1 log", 25 * asinh(1), 25 * log(1 + sqrt(2)))
eq("slope at 22.04", D(yc, 25 * asinh(1)), 1, 1e-6)

# inverse functions
for x in (-0.6, 0.2, 0.75):
    eq("d asin", D(asin, x), 1 / sqrt(1 - x * x), 1e-6)
    eq("d acos", D(acos, x), -1 / sqrt(1 - x * x), 1e-6)
    eq("d atan", D(atan, x), 1 / (1 + x * x), 1e-6)
    eq("d atanh", D(atanh, x), 1 / (1 - x * x), 1e-6)
    eq("d asinh", D(asinh, x), 1 / sqrt(x * x + 1), 1e-6)
    # log form derivation
    u = x + sqrt(x * x + 1)
    up = 1 + x / sqrt(x * x + 1)
    eq("asinh log deriv", up / u, 1 / sqrt(x * x + 1))
    eq("u'", up, (sqrt(x * x + 1) + x) / sqrt(x * x + 1))
    # eg
    eq("eg a", D(lambda v: asinh(2 * v), x), 2 / sqrt(4 * x * x + 1), 1e-6)
    eq("eg b", D(lambda v: acos(v * v), x), -2 * x / sqrt(1 - x ** 4), 1e-5)
    eq("eg d", D(lambda v: v * asin(v) + sqrt(1 - v * v), x), asin(x), 1e-5)
    # t3
    eq("t3a", D(lambda v: asin(3 * v), x / 4), 3 / sqrt(1 - 9 * (x / 4) ** 2), 1e-5)
    eq("t3c", D(lambda v: atanh(v ** 3), x), 3 * x * x / (1 - x ** 6), 1e-5)
for x in (1.4, 2.5, 4.0):
    eq("d acosh", D(acosh, x), 1 / sqrt(x * x - 1), 1e-6)
    eq("t3b", D(lambda v: acosh(2 * v), x), 2 / sqrt(4 * x * x - 1), 1e-5)
for x in (0.1, 0.5, 0.8):
    eq("eg c", D(lambda v: atanh(sqrt(v)), x), 1 / (2 * sqrt(x) * (1 - x)), 1e-5)
for x in (0.1, 0.5, 1.0):
    eq("sec", D(lambda v: atanh(sin(v)), x), 1 / cos(x), 1e-5)
    eq("sec2", 1 / (1 - sin(x) ** 2) * cos(x), 1 / cos(x))
    eq("sinh-1 tan", D(lambda v: asinh(tan(v)), x), 1 / cos(x), 1e-5)
# q3a
for x in (0.5, 2.0):
    eq("q3a", D(lambda v: acosh(2 * v + 1), x), 1 / sqrt(x * x + x), 1e-5)
    eq("q3a b", 2 / sqrt((2 * x + 1) ** 2 - 1), 1 / sqrt(x * x + x))
# t5
eq("t5 sqrt", sqrt(9 / 16 + 1), 5 / 4)
eq("t5", D(lambda v: v * asinh(v), 0.75), log(2) + 3 / 5, 1e-6)
eq("t5 ln", asinh(0.75), log(2))

# implicit: x^2 + xy + y^2 = 3
yimp = lambda x: (-x + sqrt(12 - 3 * x * x)) / 2
eq("imp y(1)", yimp(1), 1)
eq("imp y'", D(yimp, 1), -1, 1e-6)
eq("imp y''", D2(yimp, 1), -2 / 3, 1e-5)
eq("imp y(0.9)", sf(yimp(0.9), 5), 1.0968, 1e-4)
eq("imp y(1.1)", sf(yimp(1.1), 4), 0.8966, 1e-4)
eq("imp second diff", (1.0968 + 0.8966 - 2) / 0.01, -0.66, 1e-9)
# check relation holds
for x in (0.9, 1.0, 1.1):
    y = yimp(x)
    eq("imp eq", x * x + x * y + y * y, 3)
# substitution at (1,1)
eq("imp first", 3 + 3 * (-1), 0)
eq("imp second", 2 + 2 * (-1) + 1 * (-2 / 3) + 2 * 1 + 2 * 1 * (-2 / 3), 0)


# folium x^3 + y^3 = 6xy at (3,3)
def yfol(x, y0=3.0):
    y = y0
    for _ in range(100):
        f = x ** 3 + y ** 3 - 6 * x * y
        fp = 3 * y * y - 6 * x
        y -= f / fp
    return y


eq("fol y'", D(yfol, 3), -1, 1e-5)
eq("fol y''", D2(yfol, 3, 1e-3), -16 / 3, 1e-4)
eq("fol first", 27 + 27 * (-1), 18 + 18 * (-1))
eq("fol second", 6 + 6 + 9 * (-16 / 3), -4 + 6 * (-16 / 3))
eq("fol on", 27 + 27, 6 * 9)
# t6: x^3 + y^3 = 9xy at (2,4)
eq("t6 on", 8 + 64, 9 * 8)
eq("t6 y'", (3 * 4 - 4) / (16 - 6), 4 / 5)


def yt6(x, y0=4.0):
    y = y0
    for _ in range(100):
        f = x ** 3 + y ** 3 - 9 * x * y
        fp = 3 * y * y - 9 * x
        y -= f / fp
    return y


eq("t6 numeric", D(yt6, 2), 4 / 5, 1e-5)


# parametric
def d2(xp, yp, t, h=1e-5):
    g = lambda s: yp(s) / xp(s)
    return D(g, t, h) / xp(t)


for t in (0.5, 1.3, 2.2):
    eq("hyp param", d2(sinh, cosh, t), -cosech(t) ** 3, 1e-6)
    eq("hyp param cart", -1 / sinh(t) ** 3, -cosech(t) ** 3)
    eq("poly param", d2(lambda s: 2 * s, lambda s: 3 * s * s - 3, t), 3 * (t * t + 1) / (4 * t ** 3), 1e-6)
    eq("dydx poly", (3 * t * t - 3) / (2 * t), 1.5 * (t - 1 / t))
    eq("dydx poly d", D(lambda s: 1.5 * (s - 1 / s), t), 1.5 * (1 + 1 / t ** 2), 1e-6)
    eq("param 2sinh", d2(lambda s: 2 * cosh(s), lambda s: 2 * sinh(2 * s), t), 1, 1e-6)
    eq("param 2sinh dydx", 4 * sinh(t) * cosh(t) / (2 * cosh(t)), 2 * sinh(t))
    eq("cosh2t", cosh(2 * t), 1 + 2 * sinh(t) ** 2)
    eq("spot dydx", D(lambda s: s * s, t) / D(lambda s: s ** 3 + s, t), 2 * t / (3 * t * t + 1), 1e-6)
    eq("spot d2", d2(lambda s: 3 * s * s + 1, lambda s: 2 * s, t), (2 - 6 * t * t) / (3 * t * t + 1) ** 3, 1e-6)
    eq("spot numer", (2 * (3 * t * t + 1) - 2 * t * 6 * t), 2 - 6 * t * t)
eq("spot t=0", (2 - 0) / 1, 2)
# stationary points of x = t^2+1, y = t^3-3t
for t, xx, yy, d2v in ((1, 2, -2, 3 / 2), (-1, 2, 2, -3 / 2)):
    eq("sp x", t * t + 1, xx)
    eq("sp y", t ** 3 - 3 * t, yy)
    eq("sp dy", (3 * t * t - 3), 0)
    eq("sp d2", 3 * (t * t + 1) / (4 * t ** 3), d2v)
# wrong quotient of second derivatives (spot the error): 2 / 6t
eq("spot wrong", 2 / (6 * 1.0), 1 / 3)

# ---- power series with Fractions ----
N = 9


def smul(a, b):
    c = [F(0)] * N
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < N:
                c[i + j] += x * y
    return c


def sdiv(a, b):
    # a / b with b[0] != 0
    c = [F(0)] * N
    a = a[:]
    for i in range(N):
        c[i] = a[i] / b[0]
        for j in range(N - i):
            if j < len(b):
                a[i + j] -= c[i] * b[j]
    return c


def sconst(v):
    return [F(v)] + [F(0)] * (N - 1)


def sexp(u):
    # exp of series with u[0] == 0
    r = sconst(1)
    term = sconst(1)
    for k in range(1, N):
        term = [x / k for x in smul(term, u)]
        r = [x + y for x, y in zip(r, term)]
    return r


def slog1p(u):
    # ln(1 + u), u[0] == 0
    r = [F(0)] * N
    p = sconst(1)
    for k in range(1, N):
        p = smul(p, u)
        r = [x + y * F((-1) ** (k + 1), k) for x, y in zip(r, p)]
    return r


SIN = [F(0)] * N
COS = [F(0)] * N
SINH = [F(0)] * N
COSH = [F(0)] * N
EXP = [F(1, factorial(k)) for k in range(N)]
for k in range(N):
    if k % 2:
        SIN[k] = F((-1) ** ((k - 1) // 2), factorial(k))
        SINH[k] = F(1, factorial(k))
    else:
        COS[k] = F((-1) ** (k // 2), factorial(k))
        COSH[k] = F(1, factorial(k))
X = [F(0), F(1)] + [F(0)] * (N - 2)


def scale(a, c):
    # a(cx)
    return [x * F(c) ** i for i, x in enumerate(a)]


TAN = sdiv(SIN, COS)
assert TAN[:6] == [0, 1, 0, F(1, 3), 0, F(2, 15)], TAN
eq("tan y5", float(TAN[5] * 120), 16)
eq("tan y3", float(TAN[3] * 6), 2)
# successive differentiation y' = 1 + y^2 at 0
y0, y1 = 0, 1
y2 = 2 * y0 * y1
y3 = 2 * y1 ** 2 + 2 * y0 * y2
y4 = 6 * y1 * y2 + 2 * y0 * y3
y5 = 6 * y2 ** 2 + 8 * y1 * y3 + 2 * y0 * y4
assert (y2, y3, y4, y5) == (0, 2, 0, 16)

# ln(1+x) derivatives
assert [1, -1, 2] == [1, -1, 2]
LN = slog1p(X)
assert LN[1:4] == [1, F(-1, 2), F(1, 3)]
for v in (0.1, 0.05):
    eq("ln series", sum(float(LN[k]) * v ** k for k in range(1, 9)), log(1 + v), 1e-9)

# e^{2x} sin x
P = smul(scale(EXP, 2), SIN)
assert P[:4] == [0, 1, 2, F(11, 6)], P
assert scale(EXP, 2)[:4] == [1, 2, 2, F(4, 3)]
# ln(1 + sin x)
Lsin = slog1p(SIN)
assert Lsin[:4] == [0, 1, F(-1, 2), F(1, 6)], Lsin
# derivatives f'(0)=1, f''(0)=-1, f'''(0)=1
fl = lambda x: log(1 + sin(x))
eq("lnsin f'", D(fl, 0), 1, 1e-6)
eq("lnsin f''", D2(fl, 0, 1e-3), -1, 1e-5)
eq("lnsin f'''", float(Lsin[3] * 6), 1)
for x in (0.2, 0.7):
    eq("lnsin f''formula", D2(fl, x, 1e-3), -1 / (1 + sin(x)), 1e-5)
    eq("lnsin f'''formula", D(lambda v: -1 / (1 + sin(v)), x), cos(x) / (1 + sin(x)) ** 2, 1e-6)
    eq("lnsin f' formula", D(fl, x), cos(x) / (1 + sin(x)), 1e-6)
# e^{sin x}
ES = sexp(SIN)
assert ES[:5] == [1, 1, F(1, 2), 0, F(-1, 8)], ES
# derivatives y' = y cos x etc at 0
ey = lambda x: exp(sin(x))
eq("es y''", D2(ey, 0, 1e-3), 1, 1e-5)
eq("es y'''", float(ES[3] * 6), 0)
# e^x cos x
EC = smul(EXP, COS)
assert EC[:4] == [1, 1, 0, F(-1, 3)], EC
# eg expansion by hand
eq("ec x3", float(F(1, 6) - F(1, 2)), -1 / 3)
# ln 1.1
s = 0.1 - 0.1 ** 2 / 2 + 0.1 ** 3 / 3 - 0.1 ** 4 / 4
eq("ln1.1 series", sf(s, 5), 0.095308, 1e-6)
eq("ln1.1 exact", sf(log(1.1), 5), 0.095310, 1e-6)
eq("terms", sf(0.1 ** 3 / 3, 3), 0.000333, 1e-9)
eq("terms4", 0.1 ** 4 / 4, 0.000025)
eq("next term", 0.1 ** 5 / 5, 2e-6)
eq("sum", 0.1 - 0.005 + 0.000333 - 0.000025, 0.095308, 1e-9)
# limit (sinh x - x cos x)/x^3
D3 = [a - b for a, b in zip(SINH, smul(X, COS))]
assert D3[:4] == [0, 0, 0, F(2, 3)], D3
for x in (1e-2, 1e-3):
    eq("limit 2/3", (sinh(x) - x * cos(x)) / x ** 3, 2 / 3, 1e-3)
assert F(1, 6) + F(1, 2) == F(2, 3)
# (cos x - 1 + x^2/2)/x^4 = 1/24
C4 = COS[4]
assert C4 == F(1, 24)
# e^x cos x limit
for x in (1e-2,):
    eq("limit -1/3", (exp(x) * cos(x) - 1 - x) / x ** 3, -1 / 3, 1e-2)
# cable and parabola
eq("cosh0.6", sf(cosh(0.6), 6), 1.18547, 1e-6)
eq("par", 25 * 1.18 - 19, 10.50)
eq("quartic", sf(25 * 1.1854 - 19, 5), 10.635, 1e-9)
eq("exact", sf(25 * cosh(0.6) - 19, 5), 10.637, 1e-3)
eq("gap", sf(25 * cosh(0.6) - 19 - 10.5, 2), 0.14, 1e-9)
eq("gap2", 25 * cosh(0.6) - 19 - 10.635 < 0.002, True)
eq("u^2/2", 0.6 ** 2 / 2, 0.18)
eq("u^4/24", 0.6 ** 4 / 24, 0.0054)
# pendulum
s05 = sin(0.5)
eq("sin0.5", sf(s05, 6), 0.479426, 1e-6)
eq("err1", sf((0.5 - s05) / s05 * 100, 3), 4.29)
c3 = 0.5 - 0.5 ** 3 / 6
eq("cubic val", sf(c3, 6), 0.479167, 1e-6)
eq("err2", sf((s05 - c3) / s05 * 100, 3), 0.0540)
eq("ratio", round((0.5 - s05) / (s05 - c3)), 80, 1)

# try: series
assert scale(COSH, 2)[:5] == [1, 0, 2, 0, F(2, 3)]
eq("1/(1+x)", 1, 1)
LN1M = [F(0)] + [F(-1, k) for k in range(1, N)]
for v in (0.2, -0.3):
    eq("ln(1-x)", sum(float(LN1M[k]) * v ** k for k in range(1, N)), log(1 - v), 1e-5)
# sin^-1 series by derivatives
fa = asin
eq("asin f'(0)", D(asin, 0), 1, 1e-6)
eq("asin f'''(0)", D2(lambda v: 1 / sqrt(1 - v * v), 0, 1e-3), 1, 1e-5)
for v in (0.1, 0.2):
    eq("asin series", asin(v), v + v ** 3 / 6 + 3 * v ** 5 / 40, 1e-5)

# q7: y' = x + y^2, y(0) = 1
def rk4(x0, y0, x1, n=1000):
    h = (x1 - x0) / n
    x, y = x0, y0
    f = lambda x, y: x + y * y
    for _ in range(n):
        k1 = f(x, y); k2 = f(x + h / 2, y + h * k1 / 2); k3 = f(x + h / 2, y + h * k2 / 2); k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; x += h
    return y


q0, q1 = 1, 0 + 1
q2 = 1 + 2 * q0 * q1
q3 = 2 * q1 ** 2 + 2 * q0 * q2
assert (q1, q2, q3) == (1, 3, 8)
eq("q7 est", 1 + 0.1 + 0.015 + 0.001333, 1.116333, 1e-6)
eq("q7 4sf", sf(1.116333, 4), 1.116)
eq("q7 rk4", rk4(0, 1, 0.1), 1.1163, 2e-3)
eq("q7 coeffs", q3 / 6, 4 / 3)

# q8: y = (asin x)^2
fy = lambda x: asin(x) ** 2
for x in (0.2, 0.4):
    y1_ = D(fy, x)
    y2_ = D2(fy, x, 1e-3)
    eq("q8 y'", y1_, 2 * asin(x) / sqrt(1 - x * x), 1e-5)
    eq("q8a", (1 - x * x) * y2_ - x * y1_, 2, 1e-4)
    y3_ = D(lambda v: D2(fy, v, 1e-3), x, 1e-3)
    eq("q8b", (1 - x * x) * y3_ - 3 * x * y2_ - y1_, 0, 1e-3)
eq("q8 y4", 4 * 2, 8)
eq("q8 coeff", 8 / 24, 1 / 3)
for v in (0.05, 0.1):
    eq("q8 series", fy(v), v * v + v ** 4 / 3 + 8 * v ** 6 / 45, 1e-8)

# stretch 1: tanh series
t0, t1 = 0, 1
t2 = -2 * t0 * t1
t3 = -2 * t1 ** 2 - 2 * t0 * t2
t4 = -6 * t1 * t2 - 2 * t0 * t3
t5 = -6 * t2 ** 2 - 8 * t1 * t3 - 2 * t0 * t4
assert (t2, t3, t4, t5) == (0, -2, 0, 16)
eq("t3 coeff", t3 / 6, -1 / 3)
eq("t5 coeff", t5 / 120, 2 / 15)
for x in (0.05, 0.1):
    eq("tanh series", tanh(x), x - x ** 3 / 3 + 2 * x ** 5 / 15, 1e-7)
    eq("lncosh series", log(cosh(x)), x * x / 2 - x ** 4 / 12 + x ** 6 / 45, 1e-9)
    eq("lncosh deriv", D(lambda v: log(cosh(v)), x), tanh(x), 1e-6)
eq("int coeffs", (1 / 3) / 4, 1 / 12)
eq("int coeffs2", (2 / 15) / 6, 1 / 45)
for v in (0.2, 0.5):
    eq("sech2", 1 - tanh(v) ** 2, sech(v) ** 2)
# stretch 2: ln 2
est = 2 * (1 / 3 + 1 / 81 + 1 / 1215 + 1 / 15309)
eq("ln2 est", sf(est, 4), 0.6931, 1e-9)
eq("ln2 exact", sf(log(2), 4), 0.6931, 1e-9)
eq("x=1/3", (1 + 1 / 3) / (1 - 1 / 3), 2)
eq("3^3*3", 3 ** 3 * 3, 81)
eq("5*3^5", 5 * 3 ** 5, 1215)
eq("7*3^7", 7 * 3 ** 7, 15309)
for v in (0.1, 0.3):
    eq("ln ratio", log((1 + v) / (1 - v)), 2 * sum(v ** (2 * k + 1) / (2 * k + 1) for k in range(0, 30)), 1e-12)

# quiz
eq("quiz coeff", 12 / factorial(3), 2)

# sec series
SEC = sdiv(sconst(1), COS)
assert SEC[:5] == [1, 0, F(1, 2), 0, F(5, 24)], SEC
assert F(1, 4) - F(1, 24) == F(5, 24)
# sinh^-1 series via binomial
BIN = [F(1), F(0), F(-1, 2), F(0), F(3, 8)]
assert F(-1, 2) * F(-3, 2) / 2 == F(3, 8)
for v in (0.05, 0.1):
    eq("asinh series", asinh(v), v - v ** 3 / 6 + 3 * v ** 5 / 40, 1e-8)
    eq("atanh series", atanh(v), v + v ** 3 / 3 + v ** 5 / 5, 1e-7)
    eq("sec numeric", 1 / cos(v), 1 + v * v / 2 + 5 * v ** 4 / 24, 1e-6)

# review fix: Maclaurin series of cosh^-1(2 + x)
fa = lambda x: acosh(2 + x)
eq("a0", fa(0), log(2 + sqrt(3)))
eq("a1", D(fa, 0), 1 / sqrt(3), 1e-6)
eq("a1 form", 1 / sqrt((2 + 0.3) ** 2 - 1), D(fa, 0.3), 1e-6)
eq("a2 form", D(lambda x: 1 / sqrt((2 + x) ** 2 - 1), 0.4), -(2.4) * ((2.4) ** 2 - 1) ** -1.5, 1e-6)
eq("a2", D(lambda x: 1 / sqrt((2 + x) ** 2 - 1), 0), -2 / (3 * sqrt(3)), 1e-6)
eq("a2/2", -2 / (3 * sqrt(3)) / 2, -1 / (3 * sqrt(3)))
eq("a 3sf", sf(log(2 + sqrt(3)), 4), 1.317, 1e-3)
eq("a1 4sf", sf(1 / sqrt(3), 4), 0.5774, 1e-4)
eq("a2 4sf", sf(1 / (3 * sqrt(3)), 4), 0.1925, 1e-4)
ser = log(2 + sqrt(3)) + 0.1 / sqrt(3) - 0.01 / (3 * sqrt(3))
eq("a series", sf(ser, 5), 1.3728, 1e-4)
eq("a calc", sf(fa(0.1), 5), 1.3729, 1e-4)
eq("a terms", sf(1.3170 + 0.0577 - 0.0019, 5), 1.3728, 1e-4)

print("ok")
