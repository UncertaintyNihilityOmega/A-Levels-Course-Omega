# checks/math.p3.diff.py: recomputes every number in the Further differentiation chapter.
from math import isclose, sqrt, sin, cos, tan, exp, log, atan, e, pi, radians

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def d(f, x, h=1e-6): return (f(x + h) - f(x - h)) / (2 * h)
def chk(label, f, g, xs=(0.4, 0.9, 1.7, 2.6)):
    for x in xs: eq(label, d(f, x), g(x), 1e-5)

eq("e tangent", e * 1, exp(1)); eq("gradient e at 1", d(exp, 1), e, 1e-6)
sec = lambda x: 1 / cos(x)
# standard
chk("a", lambda x: 3 * exp(2 * x) - 4 * log(x), lambda x: 6 * exp(2 * x) - 4 / x)
chk("b", lambda x: 5 * sin(3 * x) + cos(x / 2), lambda x: 15 * cos(3 * x) - 0.5 * sin(x / 2))
chk("c", lambda x: tan(4 * x), lambda x: 4 * sec(4 * x)**2, xs=(0.1, 0.3, 0.5))
chk("d", lambda x: log(5 * x - 2), lambda x: 5 / (5 * x - 2), xs=(0.9, 1.7))
eq("deg", d(lambda x: sin(radians(x)), 30), pi / 180 * cos(radians(30)), 1e-6)
# chain
chk("e^x2", lambda x: exp(x * x), lambda x: 2 * x * exp(x * x), xs=(0.3, 0.8))
chk("sin2", lambda x: sin(x)**2, lambda x: 2 * sin(x) * cos(x))
chk("(3+2e^x)^4", lambda x: (3 + 2 * exp(x))**4, lambda x: 8 * exp(x) * (3 + 2 * exp(x))**3, xs=(0.2, 0.7))
chk("ln cos", lambda x: log(cos(x)), lambda x: -tan(x), xs=(0.2, 0.7, 1.1))
# product
chk("x2e3x", lambda x: x * x * exp(3 * x), lambda x: x * exp(3 * x) * (3 * x + 2), xs=(0.3, 0.8))
chk("xlnx", lambda x: x * log(x), lambda x: 1 + log(x))
chk("e sin2x", lambda x: exp(x) * sin(2 * x), lambda x: exp(x) * (2 * cos(2 * x) + sin(2 * x)))
# quotient
chk("sin/x", lambda x: sin(x) / x, lambda x: (x * cos(x) - sin(x)) / x**2)
chk("e2x/(x+1)", lambda x: exp(2 * x) / (x + 1), lambda x: exp(2 * x) * (2 * x + 1) / (x + 1)**2, xs=(0.3, 0.8, 1.5))
chk("tan", tan, lambda x: sec(x)**2, xs=(0.3, 0.8, 1.2))
# stationary xe^-x
chk("xe-x", lambda x: x * exp(-x), lambda x: exp(-x) * (1 - x))
eq("x=1 y", 1 * exp(-1), 1 / e); chk("xe-x2", lambda x: exp(-x) * (1 - x), lambda x: exp(-x) * (x - 2))
eq("d2 at 1", exp(-1) * (1 - 2), -exp(-1))
# ln x / x
chk("lnx/x", lambda x: log(x) / x, lambda x: (1 - log(x)) / x**2, xs=(0.5, 1.5, 3.0))
eq("y at e", log(e) / e, 1 / e); chk("d2", lambda x: (1 - log(x)) / x**2, lambda x: (2 * log(x) - 3) / x**3, xs=(0.5, 1.5, 3.0))
eq("d2 at e", (2 - 3) / e**3, -1 / e**3)
# x^2 ln x
chk("x2lnx", lambda x: x * x * log(x), lambda x: x + 2 * x * log(x))
xs_ = exp(-0.5); eq("x", sf(xs_, 4), 0.6065); eq("y", sf(xs_**2 * log(xs_), 3), -0.184); eq("y exact", -1 / (2 * e), xs_**2 * log(xs_))
chk("d2 x2lnx", lambda x: x + 2 * x * log(x), lambda x: 2 * log(x) + 3); eq("d2", 2 * log(xs_) + 3, 2)
eq("tangent grad", 2 * exp(0) + 3, 5); eq("y0", exp(0) + 0, 1)
# parametric
assert 6 * 2 / (3 * 2**2) == 1 and (2**3, 3 * 2**2) == (8, 12) and 12 - 8 == 4
x_, y_ = 2**2, 2**3 - 3 * 2; assert (x_, y_) == (4, 2); assert (3 * 4 - 3) / (2 * 2) == 9 / 4
assert (1, 1**3 - 3) == (1, -2) and (1, (-1)**3 + 3) == (1, 2)
# implicit
assert 3**2 + 4**2 == 25 and -3 / 4 * (4 / 3) == -1
assert 2**2 + 2 * 1 + 1**2 == 7; assert -(2 * 2 + 1) / (2 + 2 * 1) == -5 / 4
assert 5 * 2 + 4 * 1 - 14 == 0 and 4 * (1 - 1) == -5 * (2 - 2) * 1
for x, y in ((2, 1),): assert x * x + x * y + y * y == 7
assert 3 * exp(0) + 0 == 3 and -exp(0) / (3 * exp(0) + 1) == -0.25 and 1 / 0.25 == 4
# tan-inverse
chk("atan2x", lambda x: atan(2 * x), lambda x: 2 / (1 + 4 * x * x))
chk("x atan x", lambda x: x * atan(x), lambda x: x / (1 + x * x) + atan(x))
chk("atan", atan, lambda x: 1 / (1 + x * x))
# context
eq("P'", sf(6 * exp(0.3)), 8.10); eq("P' = .03P", 6 * exp(0.3), 0.03 * 200 * exp(0.3)); eq("T'", sf(-8 * exp(-0.5), 3), -4.85)

# try
chk("T1a", lambda x: 4 * exp(-3 * x), lambda x: -12 * exp(-3 * x)); chk("T1b", lambda x: 2 * log(3 * x + 1), lambda x: 6 / (3 * x + 1))
chk("T1c", lambda x: sin(2 * x - 1), lambda x: 2 * cos(2 * x - 1)); chk("T1d", lambda x: tan(3 * x), lambda x: 3 * sec(3 * x)**2, xs=(0.1, 0.3, 0.4))
chk("T2a", lambda x: exp(sin(x)), lambda x: cos(x) * exp(sin(x))); chk("T2b", lambda x: cos(x)**3, lambda x: -3 * sin(x) * cos(x)**2)
chk("T2c", lambda x: log(x * x + 1), lambda x: 2 * x / (x * x + 1))
chk("T3a", lambda x: x**3 * sin(x), lambda x: x**3 * cos(x) + 3 * x * x * sin(x))
chk("T3b", lambda x: exp(2 * x) * cos(x), lambda x: exp(2 * x) * (2 * cos(x) - sin(x)))
chk("T3c", lambda x: sqrt(x) * log(x), lambda x: (2 + log(x)) / (2 * sqrt(x)))
chk("T4a", lambda x: x / exp(x), lambda x: (1 - x) / exp(x))
chk("T4b", lambda x: (1 + sin(x)) / cos(x), lambda x: (1 + sin(x)) / cos(x)**2, xs=(0.2, 0.6, 1.0))
eq("T5", 2 * sec(pi / 4)**2, 4)
eq("T6", 2 * 1 - 3, -1);
chk("T7", lambda x: exp(2 * x) - 6 * x, lambda x: 2 * exp(2 * x) - 6); x7 = 0.5 * log(3); eq("T7 x", sf(x7), 0.549); eq("T7 y", sf(3 - 3 * log(3)), -0.296); eq("d2", 4 * exp(2 * x7), 12)
t = 1; assert (3 * t - 1, t * t + 2 * t) == (2, 3) and (2 * t + 2) / 3 == 4 / 3 and -3 / 4 * 4 / 3 == -1 and 3 * 2 + 4 * 3 - 18 == 0
assert 4 + 4 - 1 == 7 and (2 + 1) / (1 - 2) == -3
# last
chk("T10 a", lambda x: x * x * exp(-x), lambda x: x * exp(-x) * (2 - x))
chk("T10 d2", lambda x: exp(-x) * (2 * x - x * x), lambda x: exp(-x) * (x * x - 4 * x + 2))
eq("T10 max", 4 * exp(-2), 0.5413, 1e-4); eq("T10 d2 at 2", exp(-2) * (4 - 8 + 2), -2 * exp(-2))
# quiz
chk("Q1", lambda x: exp(5 * x), lambda x: 5 * exp(5 * x), xs=(0.2, 0.5)); chk("Q2", lambda x: log(3 * x), lambda x: 1 / x)
chk("Q3", lambda x: x * sin(x), lambda x: sin(x) + x * cos(x)); assert 2 / (2 * 3) == 1 / 3

# ---- v2 additions: warm-up, proofs, spot the error, exam practice, stretch ----
chk("warm-up chain", lambda x: (3 * x + 1) ** 5, lambda x: 15 * (3 * x + 1) ** 4, xs=(0.1, -0.2, 0.3))
eq("warm-up x", 0.5 * log(5), log(5) / 2); eq("warm-up e^2x", exp(2 * 0.5 * log(5)), 5)
for x in (0.3, 1.1): eq("warm-up sin2x", sin(x) * cos(x), 0.5 * sin(2 * x))
eq("proof k(2)", log(2), 0.693, 5e-4); eq("proof k(3)", log(3), 1.099, 5e-4)       # proof of e^x
for a in (2, 3, e): eq("proof limit (a^h-1)/h", (a ** 1e-7 - 1) / 1e-7, log(a), 1e-6)
chk("proof ln x", log, lambda x: 1 / x)
for h in (1e-4, 1e-6):                                                              # proof of sin x
    eq("sin limit", sin(h) / h, 1, 1e-7); eq("1 - cos limit", (cos(h) - 1) / h, 0, 1e-3)
    eq("identity cos h - 1", cos(h) - 1, -sin(h) ** 2 / (1 + cos(h)), 1e-12)
for h in (0.2, 0.7, 1.2): assert sin(h) < h < tan(h) and cos(h) < sin(h) / h < 1
chk("proof sin", sin, cos)
u = lambda x: x * x + 1; v = lambda x: x + 1                                       # product rule widget numbers
assert u(1) == 2 and v(1) == 2 and 2 * 2 + 2 * 1 == 6 and 3 * 1 + 2 * 1 + 1 == 6
for h in (0.05, 0.5, 1.0):
    eq("widget dy/h", (u(1 + h) * v(1 + h) - u(1) * v(1)) / h, 6 + 4 * h + h * h)
    du = u(1 + h) - u(1); dv = v(1 + h) - v(1)
    eq("widget split", u(1 + h) * v(1 + h) - 4, v(1) * du + u(1) * dv + du * dv)
chk("proof product", lambda x: u(x) * v(x), lambda x: 2 * x * v(x) + u(x) * 1)
chk("proof quotient", lambda x: sin(x) / (x + 2), lambda x: ((x + 2) * cos(x) - sin(x)) / (x + 2) ** 2)
chk("spot", lambda x: x * x * sin(3 * x), lambda x: 3 * x * x * cos(3 * x) + 2 * x * sin(3 * x))
eq("spot correct", d(lambda x: x * x * sin(3 * x), 0.7), 0.4664, 5e-5)
eq("spot wrong", 0.7 ** 2 * cos(2.1) + 2 * 0.7 * sin(2.1), 0.9611, 5e-5)
chk("Q1", lambda x: 3 * exp(-2 * x) + 5 * log(4 * x), lambda x: -6 * exp(-2 * x) + 5 / x)  # exam practice
chk("Q2", lambda x: x ** 3 * log(x), lambda x: x * x + 3 * x * x * log(x))
chk("Q3", lambda x: sin(x) / (1 + cos(x)), lambda x: 1 / (1 + cos(x)), xs=(0.4, 1.3, 2.2))
for t in (0.3, 1.4, -2.0):                                                          # Q4 parametric
    dydx = (6 * t * t - 6) / (6 * t); eq("Q4 dy/dx", dydx, (t * t - 1) / t)
    eq("Q4 numeric", ((2 * (t + 1e-6) ** 3 - 6 * (t + 1e-6)) - (2 * (t - 1e-6) ** 3 - 6 * (t - 1e-6))) / ((3 * (t + 1e-6) ** 2) - (3 * (t - 1e-6) ** 2)), dydx, 1e-4)
assert (3 * 1, 2 - 6) == (3, -4) and (3 * 1, -2 + 6) == (3, 4)
assert 1 + 2 + 4 == 7                                                               # Q5 implicit
Fx = lambda x, y: 2 * x + y; Fy = lambda x, y: x + 2 * y
eq("Q5 gradient", -Fx(1, 2) / Fy(1, 2), -0.8); assert 4 * 1 + 5 * 2 == 14
chk("Q6", lambda x: log(x) / x ** 2, lambda x: (1 - 2 * log(x)) / x ** 3)
eq("Q6 x", sqrt(e), e ** 0.5); eq("Q6 y", log(sqrt(e)) / e, 1 / (2 * e)); eq("Q6 zero", (1 - 2 * log(sqrt(e))), 0)
chk("Q7a", lambda x: exp(2 * x) * sin(x), lambda x: exp(2 * x) * (2 * sin(x) + cos(x)))   # Q7
R = sqrt(5); al = atan(1 / 2); eq("Q7 R", R, sqrt(2 ** 2 + 1)); eq("Q7 alpha", al, 0.464, 5e-4)
for x in (0.2, 1.5, 3.0): eq("Q7 form", 2 * sin(x) + cos(x), R * sin(x + al))
eq("Q7 x", pi - al, 2.68, 5e-3); eq("Q7 stat", 2 * sin(pi - al) + cos(pi - al), 0, 1e-12)
assert 2 ** 3 + 4 ** 3 == 9 * 2 * 4 == 72                                          # Q8 folium
Fx = lambda x, y: 3 * x * x - 9 * y; Fy = lambda x, y: 3 * y * y - 9 * x
eq("Q8 gradient", -Fx(2, 4) / Fy(2, 4), 0.8); eq("Q8 formula", (3 * 4 - 2 ** 2) / (4 ** 2 - 3 * 2), 0.8)
assert 4 * 2 - 5 * 4 + 12 == 0
x = 54 ** (1 / 3); y = x * x / 3; eq("Q8 x", x, 3.78, 5e-3); eq("Q8 on curve", x ** 3 + y ** 3, 9 * x * y, 1e-9); eq("Q8 numerator", 3 * y - x * x, 0)
for x in (0.5, 1.7, 3.0): eq("S1 identity", x ** x, exp(x * log(x)))                     # stretch
chk("S1", lambda x: x ** x, lambda x: x ** x * (log(x) + 1), xs=(0.5, 1.2, 2.5))
eq("S1 min", exp(-1 / e), 0.692, 5e-4); eq("S1 min check", (1 / e) ** (1 / e), exp(-1 / e))
assert all((1 / e) ** (1 / e) <= x ** x for x in [i / 100 for i in range(1, 400)])
eq("S2 tangent", log(e) - (1 / e) * e, 0)
print("ok")
