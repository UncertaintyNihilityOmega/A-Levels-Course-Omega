# checks/math.p1.diff.py: recomputes every number in the Differentiation chapter.
from fractions import Fraction as F
from math import isclose, pi, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

def d(f, x, h=1e-6):            # numerical derivative, to test every symbolic derivative in the chapter
    return (f(x + h) - f(x - h)) / (2 * h)

def d2(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

def same_deriv(label, f, fd, xs=(0.4, 1.3, 2.0, 3.7), tol=1e-5):
    for x in xs:
        eq(f"{label} at {x}", d(f, x), fd(x), tol)

# Chords on y = x^3 from x = 2
for h, want in ((1, 19), (0.1, 12.61), (0.01, 12.0601), (0.001, 12.006001)):
    eq(f"chord h={h}", ((2 + h) ** 3 - 8) / h, want, 1e-9)
    eq(f"12+6h+h^2 h={h}", 12 + 6 * h + h * h, want, 1e-9)
eq("tangent at 2", 3 * 2 ** 2, 12)
# plot lines: chord through (2,8),(3,27) is y = 19x - 30; tangent y = 12x - 16
eq("chord line at 2", 19 * 2 - 30, 8); eq("chord line at 3", 19 * 3 - 30, 27); eq("tangent line at 2", 12 * 2 - 16, 8)

# Powers
same_deriv("eg1", lambda x: 4 * x ** 3 - 5 * x ** 2 + 7 * x - 2, lambda x: 12 * x ** 2 - 10 * x + 7)
same_deriv("eg2", lambda x: 6 * sqrt(x) - 4 / x ** 2 + 3 / (2 * x), lambda x: 3 / sqrt(x) + 8 / x ** 3 - 3 / (2 * x ** 2))
eq("(2x)^-2 coefficient", 1 / (2 * 1.7) ** 2, 0.25 * 1.7 ** -2)
same_deriv("eg3a expand", lambda x: (2 * x + 1) * (x - 3), lambda x: 4 * x - 5)
eq("eg3a expanded", (2 * 1.9 + 1) * (1.9 - 3), 2 * 1.9 ** 2 - 5 * 1.9 - 3)
same_deriv("eg3b", lambda x: (x ** 2 + 3) / sqrt(x), lambda x: 1.5 * x ** 0.5 - 1.5 * x ** -1.5)
f = lambda x: x ** 3 - 6 * x + 1
eq("f'(-1)", d(f, -1), -3, 1e-6)
for x, y in ((2, -3), (-2, 5)):
    eq(f"f'({x})=6", d(f, x), 6, 1e-6); eq(f"f({x})", f(x), y)

# Chain rule
same_deriv("chain1", lambda x: (3 * x - 1) ** 5, lambda x: 15 * (3 * x - 1) ** 4, tol=1e-3)
same_deriv("chain2a", lambda x: sqrt(2 * x * x + 1), lambda x: 2 * x / sqrt(2 * x * x + 1))
same_deriv("chain2b", lambda x: 8 / (4 - x) ** 3, lambda x: 24 / (4 - x) ** 4, xs=(0.4, 1.3, 2.0, 5.5), tol=1e-4)

# Second derivative
f = lambda x: x ** 4 - 2 * x ** 3 + 5 * x
same_deriv("second eg first", f, lambda x: 4 * x ** 3 - 6 * x ** 2 + 5, tol=1e-4)
for x in (0.4, 1.3, 2.0):
    eq(f"second eg d2 at {x}", d2(f, x), 12 * x ** 2 - 12 * x, 1e-4)

# Tangent and normal exam example: y = x^2 - 4/x at P(2, 2)
f = lambda x: x * x - 4 / x
eq("P on curve", f(2), 2)
same_deriv("tn derivative", f, lambda x: 2 * x + 4 / x ** 2)
eq("gradient at 2", 2 * 2 + 4 / 4, 5)
eq("tangent through P", 5 * 2 - 8, 2)
eq("normal through P", 2 + 5 * 2 - 12, 0)
eq("normal gradient", -1 / 5, -0.2)
xA = F(8, 5); xB = F(12)
assert 5 * xA - 8 == 0 and xB - 12 == 0
eq("AB", float(xB - xA), 10.4); eq("area", float(F(1, 2) * (xB - xA) * 2), 10.4)

# Increasing and decreasing
f = lambda x: x ** 3 - 3 * x ** 2 - 9 * x + 5
fd = lambda x: 3 * x ** 2 - 6 * x - 9
same_deriv("cubic", f, fd)
for x in (-1, 3):
    eq(f"root {x}", fd(x), 0)
assert fd(0) < 0 and fd(-1.5) > 0 and fd(3.5) > 0
g = lambda x: x ** 3 + 3 * x ** 2 + 6 * x - 2
same_deriv("increasing", g, lambda x: 3 * (x + 1) ** 2 + 3)
assert min(3 * (x / 100 + 1) ** 2 + 3 for x in range(-500, 500)) >= 3

# Stationary points exam example
eq("max y", f(-1), 10); eq("min y", f(3), -22)
eq("d2 at -1", 6 * -1 - 6, -12); eq("d2 at 3", 6 * 3 - 6, 12)
for x in (-1, 3):
    eq(f"d2 numeric {x}", d2(f, x), 6 * x - 6, 1e-4)
assert fd(-1.1) > 0 and fd(-0.9) < 0 and fd(2.9) < 0 and fd(3.1) > 0

# y = x + 9/x
f = lambda x: x + 9 / x
same_deriv("x+9/x", f, lambda x: 1 - 9 / x ** 2)
eq("min y", f(3), 6); eq("max y", f(-3), -6)
eq("d2 at 3", 18 / 27, F(18, 27)); eq("d2 numeric 3", d2(f, 3), 18 / 27, 1e-5); eq("d2 numeric -3", d2(f, -3), -18 / 27, 1e-5)

# Connected rates: oil slick
eq("dA/dr", 2 * pi * 20, 40 * pi); eq("dA/dt", 40 * pi * 0.5, 20 * pi); eq("20pi", sf(20 * pi), 62.8)
# Balloon
eq("dV/dr", 4 * pi * 5 ** 2, 100 * pi); eq("dr/dt", 100 / (100 * pi), 1 / pi); eq("1/pi", sf(1 / pi), 0.318)

# Box
V = lambda x: x * (24 - 2 * x) ** 2
eq("expanded", V(2.5), 4 * 2.5 ** 3 - 96 * 2.5 ** 2 + 576 * 2.5)
Vd = lambda x: 12 * x ** 2 - 192 * x + 576
same_deriv("box derivative", V, Vd, tol=1e-3)
eq("factorised", Vd(1.7), 12 * (1.7 - 4) * (1.7 - 12))
eq("Vd(4)", Vd(4), 0); eq("Vd(12)", Vd(12), 0); eq("base at 12", 24 - 24, 0)
eq("V'' at 4", 24 * 4 - 192, -96); eq("Vmax", V(4), 1024); eq("16^2*4", 4 * 16 ** 2, 1024)

# Try it yourself
same_deriv("t1", lambda x: 5 * x ** 4 - 3 * x ** 2 + 8 * x - 7, lambda x: 20 * x ** 3 - 6 * x + 8, tol=1e-4)
same_deriv("t2", lambda x: 4 * sqrt(x) - 6 / x ** 3, lambda x: 2 / sqrt(x) + 18 / x ** 4, tol=1e-4)
same_deriv("t3", lambda x: (x * x - 3) * (2 * x + 1), lambda x: 6 * x ** 2 + 2 * x - 6, tol=1e-4)
eq("t3 expanded", (1.3 ** 2 - 3) * (2 * 1.3 + 1), 2 * 1.3 ** 3 + 1.3 ** 2 - 6 * 1.3 - 3)
same_deriv("t4", lambda x: (5 - 2 * x) ** 6, lambda x: -12 * (5 - 2 * x) ** 5, tol=1e-3)
f = lambda x: 6 / sqrt(3 * x + 1)
same_deriv("t5", f, lambda x: -9 * (3 * x + 1) ** -1.5)
eq("t5 value", d(f, 1), -9 / 8, 1e-6); eq("4^-3/2", 4 ** -1.5, 1 / 8)
f = lambda x: x ** 3 - 2 * x + 1
eq("t6 y", f(1), 0); eq("t6 gradient", d(f, 1), 1, 1e-6)
f = lambda x: 2 * x ** 3 - 9 * x ** 2 + 12 * x
same_deriv("t7", f, lambda x: 6 * (x - 1) * (x - 2), tol=1e-4)
f = lambda x: 2 * x ** 3 + 3 * x ** 2 - 12 * x + 4
same_deriv("t8", f, lambda x: 6 * (x + 2) * (x - 1), tol=1e-4)
eq("t8 max", f(-2), 24); eq("t8 min", f(1), -3)
eq("t8 d2 -2", 12 * -2 + 6, -18); eq("t8 d2 1", 12 * 1 + 6, 18)
eq("t9 dV/dx", 3 * 5 ** 2, 75); eq("t9 dV/dt", 75 * 0.2, 15)
A = lambda x: x * (60 - 2 * x)
eq("t10 expanded", A(7), 60 * 7 - 2 * 49); eq("t10 x", 60 / 4, 15); eq("t10 area", A(15), 450); eq("t10 other side", 60 - 30, 30)
a, b = 2, 4
eq("t11 point", a + b, 6); eq("t11 stationary", 2 * a - b, 0)
f = lambda x: a * x * x + b / x
eq("t11 numeric gradient", d(f, 1), 0, 1e-6); eq("t11 d2", 2 * a + 2 * b, 12); eq("t11 d2 numeric", d2(f, 1), 12, 1e-4)

# Quiz
same_deriv("q1", lambda x: 4 / x ** 2, lambda x: -8 / x ** 3)
same_deriv("q2", lambda x: (2 * x + 3) ** 4, lambda x: 8 * (2 * x + 3) ** 3, tol=1e-3)
eq("q5 dA/dr", 2 * pi * 3, 6 * pi); eq("q5 dA/dt", 6 * pi * 2, 12 * pi)
# v2: warm-up
eq("w2 root", 3 * 3 ** 2 - 6 * 3 - 9, 0); eq("w2 root2", 3 * (-1) ** 2 - 6 * (-1) - 9, 0); eq("w3 grad", -3 / 4 * 4 / 3, -1)

# v2: proof of x^n: chord = n x^(n-1) + C(n,2) x^(n-2) h + ... + h^(n-1), checked for several n
from math import comb
for n in (2, 3, 5, 7):
    for x, h in ((1.3, 0.2), (-0.7, 0.05), (2.0, 0.5)):
        eq(f"proof n={n}", ((x + h) ** n - x ** n) / h, sum(comb(n, k) * x ** (n - k) * h ** (k - 1) for k in range(1, n + 1)), 1e-8)
eq("proof n=3 chord", ((2 + 0.1) ** 3 - 8) / 0.1, 12 + 6 * 0.1 + 0.1 ** 2, 1e-9)

# v2: spot the error
f = lambda x: x * x - 4 * x + 7
eq("spot y", f(3), 4); eq("spot m", d(f, 3), 2, 1e-6)
eq("spot normal", 3 + 2 * 4 - 11, 0); eq("spot wrong y", 9 - 12 + 7, 4)

# v2: exam practice
same_deriv("x1", lambda x: 3 * x ** 4 - 5 / x ** 2 + 6 * sqrt(x), lambda x: 12 * x ** 3 + 10 / x ** 3 + 3 / sqrt(x))
same_deriv("x2", lambda x: sqrt(4 * x - 3), lambda x: 2 * (4 * x - 3) ** -0.5, xs=(1.5, 3.0, 5.2))
eq("x2 f'(3)", 2 * 9 ** -0.5, 2 / 3)
g = lambda x: x ** 3 + 6 * x ** 2 + 15 * x - 4
same_deriv("x3", g, lambda x: 3 * x * x + 12 * x + 15, xs=(-3.0, 0.5, 2.0))
for x in (-5, -2, 0, 3): eq("x3 square", 3 * x * x + 12 * x + 15, 3 * (x + 2) ** 2 + 3)
h4 = lambda x: x ** 3 - 6 * x ** 2 + 9 * x + 2
same_deriv("x4", h4, lambda x: 3 * x * x - 12 * x + 9)
eq("x4 y1", h4(1), 6); eq("x4 y3", h4(3), 2); eq("x4 d2 at 1", 6 * 1 - 12, -6); eq("x4 d2 at 3", 6 * 3 - 12, 6)
eq("x5 y", 2 * sqrt(4), 4); eq("x5 grad", 4 ** -0.5, 0.5); eq("x5 xint", 0 - 2 / 0.5, -4)
eq("x5 area", 0.5 * 4 * 2, 4)
eq("x6 dx/dt", 6 / 24, 0.25); eq("x6 dP/dt", 4 * 0.25, 1)
S = lambda r: 2 * pi * r * r + 2 * pi * r * (250 / r ** 2)
eq("x7 S form", S(3.3), 2 * pi * 3.3 ** 2 + 500 * pi / 3.3, 1e-9)
eq("x7 dS", d(S, 5), 0, 1e-5); eq("x7 r3", 5 ** 3, 125); eq("x7 d2", 4 * pi + 1000 * pi / 125, 12 * pi); eq("x7 d2 num", d2(S, 5), 12 * pi, 1e-3)
eq("x7 S min", S(5), 150 * pi); eq("x7 S sf", sf(S(5)), 471)
for a in (0.5, 1.0, 3.0, 7.0):
    m = -12 / a ** 2
    xi = a - (12 / a) / m
    yi = 12 / a - m * a
    eq("x8 xint", xi, 2 * a, 1e-9); eq("x8 yint", yi, 24 / a, 1e-9); eq("x8 area", 0.5 * xi * yi, 24, 1e-9)
gg = lambda x: x ** 3 - 3 * x * x - 9 * x
eq("s1 max", gg(-1), 5); eq("s1 min", gg(3), -27)
# number of real roots of x^3 - 3x^2 - 9x + k by scanning for sign changes
def nroots(k):
    xs = [i / 1000 for i in range(-6000, 6000)]
    v = [gg(x) + k for x in xs]
    return sum(1 for i in range(len(v) - 1) if v[i] * v[i + 1] < 0)
for k, want in ((-6, 1), (-4.9, 3), (0.3, 3), (26.9, 3), (28, 1)):
    assert nroots(k) == want, (k, nroots(k))
for a in (0.5, 1.0, 2.0, -1.5):
    for x in (-2.3, 0.4, 1.9):
        eq("s2 factor", x ** 3 - 3 * a * a * x + 2 * a ** 3, (x - a) ** 2 * (x + 2 * a), 1e-9)
    eq("s2 grad", 3 * (-2 * a) ** 2, 4 * 3 * a * a)
print("ok")
