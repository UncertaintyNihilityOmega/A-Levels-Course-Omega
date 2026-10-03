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
print("ok")
