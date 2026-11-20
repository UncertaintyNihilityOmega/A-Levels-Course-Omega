# checks/math.fm.de.py: recomputes every number in First order differential equations.
# Standard library only. Every solution is checked by substituting it back into its equation
# (central differences), and every condition, limit and mark total is recomputed.
from math import isclose, exp, log, sin, cos, tan, sinh, cosh, tanh, atan, sqrt, pi


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def d(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def sat(label, resid, xs, tol=1e-5):
    """resid(x) should be 0 at every x in xs."""
    for x in xs:
        r = resid(x)
        assert abs(r) < tol * max(1, abs(x)), f"{label}: residual {r} at x = {x}"


def rk4(f, x0, y0, x1, n=4000):
    h = (x1 - x0) / n
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y


# ---- the proof: I = e^{int P}, I' = P I (P = 2/x gives I = x^2; P = tan x gives sec x)
sat("proof I'=PI (x^2)", lambda x: d(lambda t: t ** 2, x) - (2 / x) * x ** 2, [0.5, 1, 3])
sat("proof I'=PI (sec)", lambda x: d(lambda t: 1 / cos(t), x) - tan(x) / cos(x), [0.2, 0.9, -0.7])

# ---- worked example 1: y' - 2y = x, y = -x/2 - 1/4 + c e^{2x}
for c in (0, 0.25, -3, 1.25):
    y = lambda x, c=c: -x / 2 - 0.25 + c * exp(2 * x)
    sat("eg1", lambda x: d(y, x) - 2 * y(x) - x, [-1, 0, 0.7, 2], 1e-4)
eq("eg1 c", 1 + 0.25, 1.25)  # y(0) = 1 gives c = 5/4
eq("eg1 y(0)", -0.25 + 1.25, 1)
# the integral used: int x e^{-2x} = -x e^{-2x}/2 - e^{-2x}/4
sat("eg1 parts", lambda x: d(lambda t: -t * exp(-2 * t) / 2 - exp(-2 * t) / 4, x) - x * exp(-2 * x), [0, 1, 2])

# ---- worked example 2: x y' - 4y = x, y = -x/3 + c x^4
for c in (0, 1, -2.5):
    y = lambda x, c=c: -x / 3 + c * x ** 4
    sat("eg2", lambda x: x * d(y, x) - 4 * y(x) - x, [0.5, 1, 2, 3], 1e-4)

# ---- worked example 3: coth x y' + y = cosh x, y = (sinh^2 x / 2 + c)/cosh x
for c in (0, 1, -2):
    y = lambda x, c=c: (sinh(x) ** 2 / 2 + c) / cosh(x)
    sat("eg3", lambda x: d(y, x) * cosh(x) / sinh(x) + y(x) - cosh(x), [0.3, 1, 2], 1e-5)
    sat("eg3 std", lambda x: d(y, x) + tanh(x) * y(x) - sinh(x), [0.3, 1, 2], 1e-5)
sat("eg3 cosh*tanh", lambda x: cosh(x) * tanh(x) - sinh(x), [0.3, 1])
sat("eg3 int tanh", lambda x: d(lambda t: log(cosh(t)), x) - tanh(x), [0.3, 1, 2])
sat("eg3 int sc", lambda x: d(lambda t: sinh(t) ** 2 / 2, x) - sinh(x) * cosh(x), [0.3, 1, 2])

# ---- sin x y' + 2 y cos x = 1, y(pi/2) = 2: y = (2 - cos x)/sin^2 x
y = lambda x: (2 - cos(x)) / sin(x) ** 2
sat("eg sin", lambda x: sin(x) * d(y, x) + 2 * y(x) * cos(x) - 1, [0.4, 1, pi / 2, 2.5], 1e-4)
eq("eg sin y", y(pi / 2), 2)
for c in (-1, 0.5, 3):
    yy = lambda x, c=c: (c - cos(x)) / sin(x) ** 2
    sat("eg sin GS", lambda x: sin(x) * d(yy, x) + 2 * yy(x) * cos(x) - 1, [0.4, 1, 2.5], 1e-4)
sat("eg sin IF", lambda x: d(lambda t: sin(t) ** 2, x) - 2 * sin(x) * cos(x), [0.4, 1, 2])

# ---- y' + 2xy = 4x: y = 2 + c e^{-x^2}
for c in (0, 1.5, -2):
    y = lambda x, c=c: 2 + c * exp(-x * x)
    sat("eg gauss", lambda x: d(y, x) + 2 * x * y(x) - 4 * x, [-2, -0.5, 0, 1, 2], 1e-5)
sat("eg gauss int", lambda x: d(lambda t: 2 * exp(t * t), x) - 4 * x * exp(x * x), [-1, 0.5, 1])
for u in (0.3, 1.2):
    sat("linear and separable", lambda x: d(lambda t: 3 + u * exp(-2 * t), x) + 2 * (3 + u * exp(-2 * x)) - 6, [0, 1])

# ---- product derivative examples
for c in (0, 2, -1):
    ya = lambda x, c=c: 2 * x ** 2 + c / x
    sat("exact a", lambda x: x * d(ya, x) + ya(x) - 6 * x ** 2, [0.5, 1, 2], 1e-4)
    yb = lambda x, c=c: (x ** 2 + c) / cos(x)
    sat("exact b", lambda x: cos(x) * d(yb, x) - yb(x) * sin(x) - 2 * x, [-1, 0.3, 1], 1e-4)

# ---- exam example 1: x y' + 2y = x e^{-x}, y(1) = 0
y = lambda x: (5 * exp(-1) - exp(-x) * (x * x + 2 * x + 2)) / x ** 2
sat("exam1", lambda x: x * d(y, x) + 2 * y(x) - x * exp(-x), [0.5, 1, 2, 5], 1e-5)
eq("exam1 y(1)", y(1), 0)
sat("exam1 parts", lambda x: d(lambda t: -exp(-t) * (t * t + 2 * t + 2), x) - x * x * exp(-x), [0, 1, 3])
eq("exam1 limit", y(50) * 50 ** 2, 5 * exp(-1), 1e-9)
assert y(80) > 0 and y(80) < 1e-3

# ---- homogeneous example: y' = (x + y)/(x - y); F = atan(y/x) - ln(x^2+y^2)/2 is constant
f = lambda x, y: (x + y) / (x - y)
F = lambda x, y: atan(y / x) - 0.5 * log(x * x + y * y)
y0 = -0.5
for x1 in (1.2, 1.8, 2.4):
    y1 = rk4(f, 1.0, y0, x1)
    eq("homog F", F(x1, y1), F(1.0, y0), 1e-7)
# the check by implicit differentiation: Fx = -(x+y)/(x^2+y^2), Fy = (x-y)/(x^2+y^2)
x, y = 1.3, 0.4
Fx = d(lambda t: F(t, y), x)
Fy = d(lambda t: F(x, t), y)
eq("homog Fx", Fx, -(x + y) / (x * x + y * y), 1e-7)
eq("homog Fy", Fy, (x - y) / (x * x + y * y), 1e-7)
eq("homog slope", -Fx / Fy, f(x, y), 1e-7)
# the algebra of the u equation
for u in (-0.5, 0.2, 0.7):
    eq("homog u", (1 + u) / (1 - u) - u, (1 + u * u) / (1 - u))

# ---- exam example 3: y' = (x^2+y^2)/(xy), y(1) = 2, y = x sqrt(2 ln x + 4)
y = lambda x: x * sqrt(2 * log(x) + 4)
sat("exam3", lambda x: d(y, x) - (x * x + y(x) ** 2) / (x * y(x)), [0.2, 0.5, 1, 2, 4], 1e-5)
eq("exam3 y(1)", y(1), 2)
for u in (0.5, 1.5, 3):
    eq("exam3 u", (1 + u * u) / u - u, 1 / u)
assert 2 * log(exp(-2)) + 4 == 0 or abs(2 * log(exp(-2)) + 4) < 1e-12

# ---- exam example 2: y' + y/x = x y^2, z = 1/y, y = 1/(3x - x^2) on (0, 3)
for c in (3, 5, 2.5):
    y = lambda x, c=c: 1 / (c * x - x * x)
    sat("exam2", lambda x: d(y, x) + y(x) / x - x * y(x) ** 2, [0.4, 1, 1.5, 2], 1e-4)
y = lambda x: 1 / (3 * x - x * x)
eq("exam2 y(1)", y(1), 0.5)
# z' - z/x = -x for z = c x - x^2
for c in (3, 7):
    z = lambda x, c=c: c * x - x * x
    sat("exam2 z", lambda x: d(z, x) - z(x) / x + x, [0.5, 1, 2])

# ---- tank
x_ = lambda t: 0.4 * (50 + t) - 37500 / (50 + t) ** 2
sat("tank", lambda t: d(x_, t) + 2 * x_(t) / (50 + t) - 1.2, [0, 10, 50, 120], 1e-6)
eq("tank x(0)", x_(0), 5)
eq("tank x(50)", x_(50), 36.25)
eq("tank conc", round(x_(50) / 200, 3), 0.181)
eq("tank c", 5 * 2500 - 0.4 * 50 ** 3, -37500)
eq("tank rate in", 6 * 0.2, 1.2)
assert abs(x_(1000) / (100 + 2 * 1000) - 0.2) < 1e-3
# against RK4 of the model itself
eq("tank rk4", rk4(lambda t, x: 1.2 - 4 * x / (100 + 2 * t), 0, 5, 50), 36.25, 1e-6)

# ---- cooling
th = lambda t: 5 + 0.5 * t + 75 * exp(-0.1 * t)
sat("cooling", lambda t: d(th, t) + 0.1 * (th(t) - 10 - 0.5 * t), [0, 5, 20, 60], 1e-6)
eq("cooling th(0)", th(0), 80)
eq("cooling lag", th(200) - (10 + 0.5 * 200), -5, 1e-6)
eq("cooling parts", 0.05 * 10 * 1, 0.5)  # 0.05 * (t/0.1 e^{0.1t} - ...) coefficient of t e^{0.1t}
sat("cooling int", lambda t: d(lambda s: exp(0.1 * s) * (5 + 0.5 * s), t) - (1 + 0.05 * t) * exp(0.1 * t), [0, 3, 10])
eq("cooling plot start", th(0), 80)

# ---- spot the error: x y' + 3y = 8x^2
yc = lambda x, c=2: 8 * x ** 2 / 5 + c / x ** 3
sat("spot correct", lambda x: x * d(yc, x) + 3 * yc(x) - 8 * x ** 2, [0.5, 1, 2], 1e-4)
ys = lambda x, c=2: 4 * x ** 3 / 3 + c / x ** 3
assert abs(2.0 * d(ys, 2.0) + 3 * ys(2.0) - 8 * 4) > 1  # the student's answer does not satisfy the DE
sat("spot student own eq", lambda x: d(ys, x) + 3 * ys(x) / x - 8 * x ** 2, [0.5, 1, 2], 1e-4)  # it does solve what the student wrote
eq("spot marks", 1 + 0 + 1 + 1 + 1 + 1 + 1, 6)
eq("spot max", 1 + 1 + 1 + 1 + 1 + 1 + 1, 7)
sat("spot int", lambda x: d(lambda t: 8 * t ** 5 / 5, x) - 8 * x ** 4, [1, 2])

# ---- try block
y = lambda x, c=1.5: 2 * exp(x) + c * exp(-3 * x)
sat("t1", lambda x: d(y, x) + 3 * y(x) - 8 * exp(x), [0, 1, 2], 1e-4)
y = lambda x, c=0.7: (x + c) * cos(x)
sat("t2", lambda x: d(y, x) + y(x) * tan(x) - cos(x), [-1, 0.2, 1])
y = lambda x, c=1.3: x ** 4 + c * x ** 3
sat("t3", lambda x: x * d(y, x) - 3 * y(x) - x ** 4, [0.5, 1, 2], 1e-4)
y = lambda x, c=2: 2 * x ** 2 + c / x
sat("t4", lambda x: x * d(y, x) + y(x) - 6 * x ** 2, [0.5, 1, 2], 1e-4)
y = lambda x: 2 * x - 1 + 4 * exp(-2 * x)
sat("t5", lambda x: d(y, x) + 2 * y(x) - 4 * x, [0, 1, 2], 1e-5)
eq("t5 y(0)", y(0), 3)
i = lambda t: 2 * (exp(-2 * t) - exp(-8 * t))
sat("t6", lambda t: 0.5 * d(i, t) + 4 * i(t) - 6 * exp(-2 * t), [0, 0.1, 0.5, 1], 1e-5)
eq("t6 i(0)", i(0), 0)
tm = log(4) / 6
eq("t6 di", d(i, tm), 0, 1e-6)
eq("t6 t", round(tm, 3), 0.231)
eq("t6 e6t", exp(6 * tm), 4)
eq("t6 imax", i(tm), 2 * (4 ** (-1 / 3) - 4 ** (-4 / 3)), 1e-12)
y = lambda x, A=1.7: A * x ** 2 - x
sat("t7", lambda x: d(y, x) - (x + 2 * y(x)) / x, [0.5, 1, 2], 1e-4)
P = lambda t: 60 - 10 * exp(0.05 * t)
sat("t8", lambda t: d(P, t) - 0.05 * P(t) + 3, [0, 5, 20], 1e-6)
eq("t8 P0", P(0), 50)
eq("t8 t", round(20 * log(6), 1), 35.8)
eq("t8 zero", P(20 * log(6)), 0, 1e-9)

# ---- exam practice
y = lambda x, c=1.1: 5 * x / 3 + c * x ** -5
sat("ep1", lambda x: x * d(y, x) + 5 * y(x) - 10 * x, [0.5, 1, 2], 1e-4)
y = lambda x, c=0.8: exp(x) / 4 - x * exp(-x) / 2 + c * exp(-x)
sat("ep2", lambda x: d(y, x) + y(x) - sinh(x), [0, 1, 2], 1e-5)
sat("ep2 int", lambda x: d(lambda t: exp(2 * t) / 4 - t / 2, x) - exp(x) * sinh(x), [0, 1, 2])
y = lambda x: (x + 3) * (x + 1)
sat("ep3", lambda x: (x + 1) * d(y, x) - y(x) - (x + 1) ** 2, [-0.5, 0, 1, 2], 1e-5)
eq("ep3 y(0)", y(0), 3)
c_ = lambda t: 50 / 3 * (exp(-0.1 * t) - exp(-0.4 * t))
sat("ep4", lambda t: d(c_, t) + 0.4 * c_(t) - 5 * exp(-0.1 * t), [0, 1, 5, 10], 1e-5)
eq("ep4 c0", c_(0), 0)
t4 = log(4) / 0.3
eq("ep4 dc", d(c_, t4), 0, 1e-6)
eq("ep4 t", round(t4, 2), 4.62)
eq("ep4 cmax", round(c_(t4), 2), 7.87)
eq("ep4 cmax exact", c_(t4), 50 / 3 * (4 ** (-1 / 3) - 4 ** (-4 / 3)), 1e-12)
# a maximum, not a minimum
assert c_(t4) > c_(t4 - 0.5) and c_(t4) > c_(t4 + 0.5)
y = lambda x: -x * log(1 - log(x))
sat("ep5", lambda x: x * d(y, x) - y(x) - x * exp(y(x) / x), [0.3, 1.0001, 1.8, 2.5], 1e-4)
eq("ep5 y(1)", y(1), 0)
for u in (-1, 0.3, 1):
    eq("ep5 u", exp(u) + u - u, exp(u))
# ep6: y' + y = x y^3, y = (x + 1/2 + e^{2x}/2)^(-1/2)
y = lambda x, c=0.5: (x + 0.5 + c * exp(2 * x)) ** -0.5
sat("ep6", lambda x: d(y, x) + y(x) - x * y(x) ** 3, [0, 0.5, 1, 2], 1e-5)
eq("ep6 y(0)", y(0), 1)
z = lambda x, c=0.5: x + 0.5 + c * exp(2 * x)
sat("ep6 z", lambda x: d(z, x) - 2 * z(x) + 2 * x, [0, 1, 2], 1e-4)
sat("ep6 parts", lambda x: d(lambda t: t * exp(-2 * t) + exp(-2 * t) / 2, x) + 2 * x * exp(-2 * x), [0, 1, 2])
# ep7
y = lambda x: 4 / 3 * sinh(x) + 9 / (16 * sinh(x) ** 2)
sat("ep7", lambda x: d(y, x) + 2 * y(x) * cosh(x) / sinh(x) - 4 * cosh(x), [0.4, log(2), 1.5, 3], 1e-4)
eq("ep7 y(ln2)", y(log(2)), 2)
eq("ep7 sinh ln2", sinh(log(2)), 0.75)
eq("ep7 c", 2 * 9 / 16 - 4 / 3 * 27 / 64, 9 / 16)
eq("ep7 limit", y(30) * exp(-30), 2 / 3, 1e-9)
sat("ep7 IF", lambda x: d(lambda t: sinh(t) ** 2, x) - 2 * cosh(x) * sinh(x), [0.3, 1, 2])
sat("ep7 int", lambda x: d(lambda t: 4 / 3 * sinh(t) ** 3, x) - 4 * cosh(x) * sinh(x) ** 2, [0.3, 1, 2])

# ---- stretch
x_of = lambda yy: 2 * exp(yy) - yy * yy - 2 * yy - 2
sat("s1", lambda yy: d(x_of, yy) - (x_of(yy) + yy * yy), [-1, 0, 0.5, 2], 1e-4)
eq("s1 x(0)", x_of(0), 0)
sat("s1 parts", lambda yy: d(lambda t: -exp(-t) * (t * t + 2 * t + 2), yy) - yy * yy * exp(-yy), [0, 1, 2])
# a solution of dy/dx = 1/(x + y^2): y as the inverse function; slope = 1/(dx/dy)
for yy in (0.5, 1, 2):
    eq("s1 slope", 1 / d(x_of, yy), 1 / (x_of(yy) + yy * yy), 1e-6)
# s2: y1 - y2 = C e^{-2x}
Q = lambda x: sin(3 * x) + x
for C in (1, -2):
    w = lambda x, C=C: C * exp(-2 * x)
    sat("s2", lambda x: d(w, x) + 2 * w(x), [0, 1, 3])

# ---- marks
eq("eg exam1 total", 3 + 6 + 1, 10)
eq("eg exam3 total", 4 + 4 + 2, 10)
eq("eg exam2 total", 3 + 4 + 3, 10)
eq("eg tank total", 3 + 6 + 1, 10)
eq("ep1", 4, 1 + 1 + 1 + 1)
eq("ep2", 5, 1 + 1 + 1 + 1 + 1)
eq("ep3", 5, 1 + 1 + 1 + 1 + 1)
eq("ep4", 9, 6 + 3)
eq("ep5", 6, 1 + 1 + 1 + 1 + 1 + 1)
eq("ep6", 9, 3 + 4 + 2)
eq("ep7", 10, 3 + 5 + 2)
eq("s1 m", 6, 1 + 1 + 1 + 1 + 1 + 1)
eq("s2 m", 4, 1 + 1 + 1 + 1)

# ---- quiz
eq("q1 IF", exp(-4 * log(3.0)), 3.0 ** -4)
eq("q5 IF", exp(log(1 / cos(0.4))), 1 / cos(0.4))
eq("q6", 5 + 3 * exp(-2 * 40), 5, 1e-9)
eq("q6 y0", 5 + 3, 8)
print("ok")
