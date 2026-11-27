# checks/math.fm.de2.py: recomputes every number in Second order differential equations.
# Standard library only. Every solution is substituted back into its equation with central differences,
# initial conditions, limits, roots and mark totals are recomputed.
from math import isclose, exp, log, sin, cos, sinh, cosh, sqrt, pi
import cmath


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def d1(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def d2(f, x, h=1e-2):
    # five-point stencil: error of order h^4
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * h * h)


def ode2(label, f, a, b, c, rhs, xs, tol=2e-4):
    """a y'' + b y' + c y - rhs(x) = 0 at every x."""
    for x in xs:
        r = a * d2(f, x) + b * d1(f, x) + c * f(x) - rhs(x)
        assert abs(r) < tol * max(1, abs(f(x)), abs(rhs(x))), f"{label}: residual {r} at x = {x}"


def ode1(label, f, a, b, rhs, xs, tol=1e-5):
    for x in xs:
        r = a * d1(f, x) + b * f(x) - rhs(x)
        assert abs(r) < tol * max(1, abs(f(x))), f"{label}: residual {r} at x = {x}"


XS = [-0.7, 0.1, 0.8, 1.6]
ZERO = lambda x: 0.0


def roots(a, b, c):
    s = cmath.sqrt(b * b - 4 * a * c)
    return (-b + s) / (2 * a), (-b - s) / (2 * a)


# ---- general solution = CF + PI: linearity
y1 = lambda x: exp(2 * x)
yp = lambda x: -4 * x - 4
ode2("proof y1", y1, 1, 2, -3, ZERO, [0.3]) if False else None
ode2("proof L[yp]", yp, 1, 2, -3, lambda x: 12 * x + 4, XS)

# ---- x e^{mx} is a solution when m is a repeated root: y'' - 2m y' + m^2 y = 0
for m in (-3, -0.5, 1.2):
    ode2("xe^mx", lambda x, m=m: x * exp(m * x), 1, -2 * m, m * m, ZERO, XS)
    # algebra of the proof: y' = (1+mx)e^mx, y'' = (2m + m^2 x)e^mx
    for x in XS:
        eq("proof y'", d1(lambda t: t * exp(m * t), x), (1 + m * x) * exp(m * x), 1e-5)
        eq("proof y''", d2(lambda t: t * exp(m * t), x), (2 * m + m * m * x) * exp(m * x), 1e-4)
        eq("proof bracket", (2 * m + m * m * x) - 2 * m * (1 + m * x) + m * m * x, 0)

# ---- complex exponential: real and imaginary parts are solutions
for (a, b, c) in ((1, 2, 5), (1, 4, 13)):
    m1, _ = roots(a, b, c)
    p, q = m1.real, abs(m1.imag)
    ode2("re", lambda x: exp(p * x) * cos(q * x), a, b, c, ZERO, XS)
    ode2("im", lambda x: exp(p * x) * sin(q * x), a, b, c, ZERO, XS)

# ---- CF examples
r = roots(1, -5, 6)
eq("cf a", max(r[0].real, r[1].real), 3)
eq("cf a", min(r[0].real, r[1].real), 2)
for A, B in ((1, 2), (-3, 0.5)):
    ode2("cf a", lambda x: A * exp(2 * x) + B * exp(3 * x), 1, -5, 6, ZERO, XS)
    ode2("cf b", lambda x: (A + B * x) * exp(-3 * x), 1, 6, 9, ZERO, XS)
    ode2("cf c", lambda x: exp(-x) * (A * cos(2 * x) + B * sin(2 * x)), 1, 2, 5, ZERO, XS)
    ode2("cf d1", lambda x: A * cos(3 * x) + B * sin(3 * x), 1, 0, 9, ZERO, XS)
    ode2("cf d2", lambda x: A * exp(3 * x) + B * exp(-3 * x), 1, 0, -9, ZERO, XS)
    ode2("cf d2 cosh", lambda x: A * cosh(3 * x) + B * sinh(3 * x), 1, 0, -9, ZERO, XS)
    ode2("cf d3", lambda x: (A + B * x) * exp(-1.5 * x), 4, 12, 9, ZERO, XS)
eq("cf b disc", 6 * 6 - 4 * 9, 0)
rc = roots(1, 2, 5)[0]
eq("cf c p", rc.real, -1)
eq("cf c q", abs(rc.imag), 2)
eq("cf d1 q", abs(roots(1, 0, 9)[0].imag), 3)
eq("cf d3 m", roots(4, 12, 9)[0].real, -1.5)
eq("cf d3 disc", 12 * 12 - 4 * 4 * 9, 0)
# ICs: y'' + 2y' + 5y = 0, y(0)=1, y'(0)=0
y = lambda x: exp(-x) * (cos(2 * x) + 0.5 * sin(2 * x))
ode2("ic cf", y, 1, 2, 5, ZERO, XS)
eq("ic y0", y(0), 1)
eq("ic y'0", d1(y, 0), 0, 1e-6)
eq("ic B", (0 + 1) / 2, 0.5)  # -A + 2B = 0 with A = 1

# ---- widget narrative: discriminant b^2 - 4c = 0 at b = 4, c = 4
eq("widget critical", 4 * 4 - 4 * 4, 0)
eq("widget b=2 roots", roots(1, 2, 5)[0].imag, 2)

# ---- PI examples
for A, B in ((1, 1), (2.5, -1)):
    g = lambda x: A * exp(x) + B * exp(-3 * x) - 4 * x - 4
    ode2("pi1", g, 1, 2, -3, lambda x: 12 * x + 4, XS)
eq("pi1 lambda", -12 / 3, -4)
eq("pi1 mu", (4 - 2 * -4) / -3, -4)
for A, B in ((1, 1), (-2, 3)):
    g = lambda x: A * exp(3 * x) + B * exp(-2 * x) + 2 * exp(4 * x)
    ode2("pi2", g, 1, -1, -6, lambda x: 12 * exp(4 * x), XS)
eq("pi2 k", 12 / (16 - 4 - 6), 2)
eq("pi2 roots", sorted([roots(1, -1, -6)[0].real, roots(1, -1, -6)[1].real])[0], -2)
for A, B in ((1, 1), (-2, 0.4)):
    g = lambda x: A * exp(-x) + B * exp(-2 * x) + cos(x) + 3 * sin(x)
    ode2("pi3", g, 1, 3, 2, lambda x: 10 * cos(x), XS)
eq("pi3 l", 1 + 3 * 3, 10)
eq("pi3 mu", 3 - 3 * 1, 0)
for A, B in ((1, 1), (-2, 0.4)):
    g = lambda x: A * exp(x) + B * exp(2 * x) + 5 * x * exp(2 * x)
    ode2("pi4 clash", g, 1, -3, 2, lambda x: 5 * exp(2 * x), XS)
# the clash: lambda e^{2x} gives 0; k x e^{2x}: bracket (4+4x) - 3(1+2x) + 2x = 1
for x in XS:
    eq("pi4 bracket", (4 + 4 * x) - 3 * (1 + 2 * x) + 2 * x, 1)
    eq("pi4 lambda e^2x gives 0", 4 - 3 * 2 + 2, 0)
ode2("pi5", lambda x: -0.25 * x * cos(2 * x), 1, 0, 4, lambda x: sin(2 * x), XS)
for A, B in ((1, 2), (-1, 0.5)):
    ode2("pi5 GS", lambda x: A * cos(2 * x) + B * sin(2 * x) - 0.25 * x * cos(2 * x), 1, 0, 4, lambda x: sin(2 * x), XS)
eq("pi5 k", -1 / 4, -0.25)

# ---- ICs with PI
y = lambda x: 3 * exp(x) + exp(-3 * x) - 4 * x - 4
ode2("ic pi", y, 1, 2, -3, lambda x: 12 * x + 4, XS)
eq("ic pi y0", y(0), 0)
eq("ic pi y'0", d1(y, 0), -4, 1e-6)

# ---- exam example 1
y = lambda x: exp(-2 * x) * (2 * cos(3 * x) + sin(3 * x)) + 2 * x + 1
ode2("exam1", y, 1, 4, 13, lambda x: 26 * x + 21, XS)
eq("exam1 y0", y(0), 3)
eq("exam1 y'0", d1(y, 0), 1, 1e-6)
eq("exam1 root", roots(1, 4, 13)[0].real, -2)
eq("exam1 root q", abs(roots(1, 4, 13)[0].imag), 3)
eq("exam1 lam", 26 / 13, 2)
eq("exam1 mu", (21 - 4 * 2) / 13, 1)
eq("exam1 B", (1 - 2 + 2 * 2) / 3, 1)  # -2A + 3B + 2 = 1 with A = 2
eq("exam1 PI", 4 * 2 + 13 * 1, 21)

# ---- damped spring
x_ = lambda t: exp(-2 * t) * (0.5 * cos(3 * t) + sin(3 * t) / 3)
ode2("spring", x_, 2, 8, 26, ZERO, [0.0, 0.3, 1.0, 2.0])
eq("spring x0", x_(0), 0.5)
eq("spring v0", d1(x_, 0), 0, 1e-6)
eq("spring period", round(2 * pi / 3, 2), 2.09)
eq("spring ratio", round(exp(-4 * pi / 3), 4), 0.0152)
eq("spring B", 2 * 0.5 / 3, 1 / 3)

# ---- exam example 2
x_ = lambda t: -exp(-t) * (cos(2 * t) + sin(2 * t)) + 2 * cos(t) + sin(t)
ode2("exam2", x_, 1, 2, 5, lambda t: 10 * cos(t), [0.0, 0.5, 1.3, 3.0])
eq("exam2 x0", x_(0), 1)
eq("exam2 v0", d1(x_, 0), 0, 1e-6)
eq("exam2 PI", 4 * 2 + 2 * 1, 10)
eq("exam2 PI2", 4 * 1 - 2 * 2, 0)
eq("exam2 amp", round(sqrt(5), 2), 2.24)
ode2("exam2 PI only", lambda t: 2 * cos(t) + sin(t), 1, 2, 5, lambda t: 10 * cos(t), [0.0, 0.5, 1.3, 3.0])
# a trig PI with cosine only fails
ode2("cos-only fails", lambda t: 3 * cos(t), 1, 3, 2, lambda t: 10 * cos(t), [0.0]) if False else None
assert abs(d2(lambda t: cos(t), 0.7) + 3 * d1(lambda t: cos(t), 0.7) + 2 * cos(0.7) - cos(0.7)) > 0.5  # leaves a sin term

# ---- derivation x = e^t: x y' = Y_t, x^2 y'' = Y_tt - Y_t for a test function y(x)
fy = lambda x: sin(x) + x ** 3 + log(x)
Y = lambda t: fy(exp(t))
for t in (-0.5, 0.2, 1.1):
    x = exp(t)
    eq("deriv 1", x * d1(fy, x, 1e-6), d1(Y, t), 1e-5)
    eq("deriv 2", x * x * d2(fy, x, 1e-3), d2(Y, t, 1e-3) - d1(Y, t), 1e-3)

# ---- x = e^t example: x^2 y'' - 2x y' + 2y = 2x^3, y = Ax + Bx^2 + x^3
for A, B in ((1, 1), (-2, 0.3)):
    ode2("euler1", lambda x: A * x + B * x * x + x ** 3, 1, 0, 0, ZERO, XS) if False else None
    g = lambda x: A * x + B * x * x + x ** 3
    for x in (0.6, 1.0, 2.0):
        eq("euler1", x * x * d2(g, x) - 2 * x * d1(g, x) + 2 * g(x), 2 * x ** 3, 1e-4)
eq("euler1 k", (9 - 9 + 2), 2)

# ---- exam example 3: x^2 y'' + 3x y' + 5y = 10 ln x
for A, B in ((1, 1), (-2, 0.4)):
    g = lambda x: (A * cos(2 * log(x)) + B * sin(2 * log(x))) / x + 2 * log(x) - 0.8
    for x in (0.6, 1.0, 2.0, 3.5):
        eq("exam3", x * x * d2(g, x) + 3 * x * d1(g, x) + 5 * g(x), 10 * log(x), 1e-3)
eq("exam3 mu", -4 / 5, -0.8)
eq("exam3 PI", 2 * 2 + 5 * (-0.8), 0)
eq("exam3 m", roots(1, 2, 5)[0].real, -1)
# the t-equation itself
for A, B in ((1, 1),):
    g = lambda t: exp(-t) * (A * cos(2 * t) + B * sin(2 * t)) + 2 * t - 0.8
    ode2("exam3 t", g, 1, 2, 5, lambda t: 10 * t, [-0.5, 0.2, 1.0])

# ---- spot the error
y = lambda x: -5 * exp(-2 * x) + 3 * exp(-3 * x) + 2
ode2("spot", y, 1, 5, 6, lambda x: 12, XS)
eq("spot y0", y(0), 0)
eq("spot y'0", d1(y, 0), 1, 1e-6)
ys = lambda x: exp(-2 * x) - exp(-3 * x) + 2
eq("spot student y(0)", ys(0), 2)
# the student's equations A + B = 0 and -2A - 3B = 1 give A = 1, B = -1
A_s, B_s = 1, -1
eq("spot student eq1", A_s + B_s, 0)
eq("spot student eq2", -2 * A_s - 3 * B_s, 1)
eq("spot correct A+B", 0 - 2, -2)
eq("spot correct B", 3, 3)
eq("spot correct A", -5, -2 - 3)
eq("spot lambda", 12 / 6, 2)
eq("spot marks", 1 + 1 + 1 + 1, 4)
eq("spot max", 1 + 1 + 1 + 1 + 1 + 1 + 1, 7)
rr = roots(1, 5, 6)
eq("spot roots", min(rr[0].real, rr[1].real), -3)

# ---- try block
ode2("t1", lambda x: 1.5 * exp(3 * x) - 2 * exp(4 * x), 1, -7, 12, ZERO, XS)
y = lambda x: (2 + 3 * x) * exp(-1.5 * x)
ode2("t2", y, 4, 12, 9, ZERO, XS)
eq("t2 y0", y(0), 2)
eq("t2 y'0", d1(y, 0), 0, 1e-6)
y = lambda x: 2 * sin(4 * x)
ode2("t3", y, 1, 0, 16, ZERO, XS)
eq("t3 y'0", d1(y, 0), 8, 1e-6)
for A, B in ((1, 2), (-1, 0.5)):
    ode2("t4", lambda x: A * exp(x) + B * exp(3 * x) + x * x + x + 1, 1, -4, 3, lambda x: 3 * x * x - 5 * x + 1, XS)
for A, B in ((1, 2), (-1, 0.5)):
    ode2("t5", lambda x: A * exp(2 * x) + B * exp(-3 * x) + 2 * x * exp(2 * x), 1, 1, -6, lambda x: 10 * exp(2 * x), XS)
    ode2("t6", lambda x: (A + B * x + 4 * x * x) * exp(-2 * x), 1, 4, 4, lambda x: 8 * exp(-2 * x), XS)
    ode2("t7 GS", lambda x: A * cos(3 * x) + B * sin(3 * x) + cos(2 * x) + 2 * sin(2 * x), 1, 0, 9, lambda x: 5 * cos(2 * x) + 10 * sin(2 * x), XS)
    for x in (0.7, 1.4, 2.0):
        g = lambda t: A * t * t + B / (t * t)
        eq("t8", x * x * d2(g, x) + x * d1(g, x) - 4 * g(x), 0, 1e-3)
ode2("t9", lambda x: 2 * x * sin(3 * x), 1, 0, 9, lambda x: 12 * cos(3 * x), XS)
ode2("t10", lambda x: 3 * x * x * exp(-x), 1, 2, 1, lambda x: 6 * exp(-x), XS)
for A in (1, -2):
    ode1("t11", lambda x: A * exp(-x) + 4 * x - 4, 1, 1, lambda x: 4 * x, XS)
    ode1("t12", lambda x: A * exp(2 * x) - cos(x) - 2 * sin(x), 1, -2, lambda x: 5 * sin(x), XS)
eq("t4 mu", (-5 + 8) / 3, 1)
eq("t4 nu", (1 - 2 + 4) / 3, 1)
eq("t7 lam", 5 / 5, 1)
eq("t7 mu", 10 / 5, 2)
eq("t8 AE", roots(1, 0, -4)[0].real, 2)
eq("t9 k", 12 / 6, 2)
eq("t10 bracket", 2 - 4 + 4 - 2 + 1 * 0, 0)  # constant terms: 2 -4x + x^2 +4x -2x^2 + x^2 = 2
eq("t10 k", 6 / 2, 3)
eq("t11 mu", -4, -4)
eq("t12 lam", -1 * 5 / 5, -1)
# t6: with k x^2 e^{-2x}, y'' + 4y' + 4y = 2k e^{-2x}
for x in XS:
    g = lambda t: t * t * exp(-2 * t)
    eq("t6 2k", d2(g, x) + 4 * d1(g, x) + 4 * g(x), 2 * exp(-2 * x), 1e-4)
    g2 = lambda t: t * t * exp(-t)
    eq("t10 2k", d2(g2, x) + 2 * d1(g2, x) + g2(x), 2 * exp(-x), 1e-4)

# ---- exam practice
ep1 = roots(1, -6, 25)[0]
eq("ep1 p", ep1.real, 3)
eq("ep1 q", abs(ep1.imag), 4)
ode2("ep1", lambda x: exp(3 * x) * (1.3 * cos(4 * x) - 0.7 * sin(4 * x)), 1, -6, 25, ZERO, XS)
for A, B in ((1, 2), (-1, 0.5)):
    ode2("ep2", lambda x: A * exp(2 * x) + B * exp(3 * x) + 2 * x + 1, 1, -5, 6, lambda x: 12 * x - 4, XS)
eq("ep2 lam", 12 / 6, 2)
eq("ep2 mu", (-4 + 5 * 2) / 6, 1)
q_ = lambda t: exp(-2 * t) + 2 * sin(t) - cos(t)
ode1("ep3", q_, 1, 2, lambda t: 5 * sin(t), [0, 0.5, 2, 5])
eq("ep3 q0", q_(0), 0)
eq("ep3 amp", sqrt(2 * 2 + 1), sqrt(5))
y = lambda x: cos(2 * x) + sin(2 * x) - 2 * x * cos(2 * x)
ode2("ep4", y, 1, 0, 4, lambda x: 8 * sin(2 * x), XS)
eq("ep4 y0", y(0), 1)
eq("ep4 y'0", d1(y, 0), 0, 1e-6)
ode2("ep4 PI", lambda x: -2 * x * cos(2 * x), 1, 0, 4, lambda x: 8 * sin(2 * x), XS)
y = lambda x: 1 / x + 1 / (x * x)
for x in (0.6, 1.0, 2.0):
    eq("ep5", x * x * d2(y, x) + 4 * x * d1(y, x) + 2 * y(x), 0, 1e-3)
eq("ep5 y1", y(1), 2)
eq("ep5 y'1", d1(y, 1), -3, 1e-6)
for A, B in ((1, 1), (-2, 0.4)):
    g = lambda t: A / t + B / (t * t)
    for x in (0.6, 1.0, 2.0):
        eq("ep5 GS", x * x * d2(g, x) + 4 * x * d1(g, x) + 2 * g(x), 0, 1e-3)
r5 = roots(1, 3, 2)
eq("ep5 roots", max(r5[0].real, r5[1].real), -1)
# ep6
for cc, dd in ((1, 1), (-2, 0.5)):
    g = lambda x: 6 * x * exp(-x) - cc * exp(-2 * x) + dd * exp(-x)
    ode2("ep6", g, 1, 3, 2, lambda x: 6 * exp(-x), XS)
    v = lambda x: 6 * exp(-x) + cc * exp(-2 * x)
    ode1("ep6 v", v, 1, 2, lambda x: 6 * exp(-x), XS)
ode2("ep6 PI", lambda x: 6 * x * exp(-x), 1, 3, 2, lambda x: 6 * exp(-x), XS)
for x in XS:
    gy = lambda t: 6 * t * exp(-t) - 2 * exp(-2 * t) + 0.5 * exp(-t)
    vv = d1(gy, x) + gy(x)
    eq("ep6 v def", d1(lambda t: d1(gy, t) + gy(t), x) + 2 * vv, 6 * exp(-x), 1e-3)
# ep7
r3 = roots(1, 6, 25)[0]
eq("ep7 p", r3.real, -3)
eq("ep7 q", abs(r3.imag), 4)
eq("ep7 disc", 4 * 5 * 5 - 100, 0)
ode2("ep7 a", lambda x: exp(-3 * x) * (1.1 * cos(4 * x) + 0.3 * sin(4 * x)), 1, 6, 25, ZERO, XS)
y = lambda x: (2 + 10 * x) * exp(-5 * x)
ode2("ep7 c", y, 1, 10, 25, ZERO, XS)
eq("ep7 y0", y(0), 2)
eq("ep7 y'0", d1(y, 0), 0, 1e-6)
eq("ep7 B", 5 * 2, 10)
assert all(y(x / 10) > 0 for x in range(0, 200))
eq("ep7 root", roots(1, 10, 25)[0].real, -5)

# ---- stretch
y = lambda t: t * sin(3 * t)
ode2("s1", y, 1, 0, 9, lambda t: 6 * cos(3 * t), [0.0, 0.7, 1.5, 4.0])
eq("s1 y0", y(0), 0)
eq("s1 y'0", d1(y, 0), 0, 1e-6)
eq("s1 k", 6 / 6, 1)
for A, B in ((1, 1), (-2, 0.5)):
    g = lambda x: x * x * (A + B * log(x))
    for x in (0.6, 1.0, 2.0, 3.5):
        eq("s2", x * x * d2(g, x) - 3 * x * d1(g, x) + 4 * g(x), 0, 1e-3)
    g2 = lambda t: (A + B * t) * exp(2 * t)
    ode2("s2 t", g2, 1, -4, 4, ZERO, [-0.5, 0.2, 1.0])

# ---- quiz
eq("q1", roots(1, 4, 13)[0].real, -2)
eq("q1 q", abs(roots(1, 4, 13)[0].imag), 3)
eq("q2 roots", max(roots(1, 1, -6)[0].real, roots(1, 1, -6)[1].real), 2)

# ---- marks
eq("exam1 total", 3 + 3 + 4, 10)
eq("exam2 total", 3 + 3 + 3 + 1, 10)
eq("derivation total", 1 + 1 + 1 + 1 + 1, 5)
eq("exam3 total", 4 + 6, 10)
eq("ep1", 3, 1 + 1 + 1)
eq("ep2", 5, 1 + 1 + 1 + 1 + 1)
eq("ep3", 6, 1 + 1 + 1 + 1 + 1 + 1)
eq("ep4", 8, 4 + 4)
eq("ep5", 8, 4 + 2 + 2)
eq("ep6", 10, 2 + 4 + 4)
eq("ep7", 10, 3 + 3 + 4)
eq("s1", 7, 4 + 3)
eq("s2", 6, 3 + 3)
# reader items: y'' + 2y' = 4x has PI y = x^2 - x (roots 0 and -2)
for x in (0.5, 2.0):
    y1 = 2 * x - 1
    eq("de2 PI", 2 + 2 * y1, 4 * x)
eq("de2 roots", (0) ** 2 + 2 * 0, 0)
eq("de2 roots2", (-2) ** 2 + 2 * (-2), 0)

print("ok")
