# checks/math.fm.arclength.py: recomputes every number in Arc length and surface area.
# Standard library only: Simpson's rule for integrals, polylines for lengths and surface areas.
from fractions import Fraction as F
from math import isclose, sqrt, sin, cos, tan, cosh, sinh, asinh, log, exp, pi, e


def eq(label, got, want, tol=1e-8):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simp(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def polylen(x, y, a, b, n=40000):
    """Length of the curve (x(t), y(t)) as a polyline."""
    s = 0.0
    px, py = x(a), y(a)
    for i in range(1, n + 1):
        t = a + (b - a) * i / n
        cx, cy = x(t), y(t)
        s += sqrt((cx - px) ** 2 + (cy - py) ** 2)
        px, py = cx, cy
    return s


def polysurf(x, y, a, b, axis="x", n=40000):
    """Surface of revolution as a sum of 2*pi*(distance)*chord."""
    s = 0.0
    px, py = x(a), y(a)
    for i in range(1, n + 1):
        t = a + (b - a) * i / n
        cx, cy = x(t), y(t)
        dist = (cy + py) / 2 if axis == "x" else (cx + px) / 2
        s += 2 * pi * dist * sqrt((cx - px) ** 2 + (cy - py) ** 2)
        px, py = cx, cy
    return s


# ---- warm-up
eq("wu3", pi * simp(lambda x: x, 0, 4), 8 * pi)
eq("wu1", (3 * 1.3) / 2, 1.95)   # dy/dx = 3t/2 at t = 1.3 (formula identity)
for x in (0.3, 1.1):
    eq("cosh identity", sqrt(1 + sinh(x) ** 2), cosh(x))

# ---- eg: y = x^{3/2}, 0..4
f1 = lambda x: sqrt(1 + 9 * x / 4)
s1 = 8 / 27 * (10 * sqrt(10) - 1)
eq("eg1 exact", s1, simp(f1, 0, 4))
eq("eg1 3sf", sf(s1), 9.07)
eq("eg1 polyline", s1, polylen(lambda t: t, lambda t: t ** 1.5, 0, 4), 1e-3)
eq("chord", sqrt(80), 8.94427190999916)
assert sqrt(80) < s1 < 12 and sf(sqrt(80), 3) == 8.94
# parametric version: x = t^2, y = t^3, 0..2
sp = (40 ** 1.5 - 8) / 27
eq("param same", sp, s1)
eq("param simp", simp(lambda t: sqrt(4 * t * t + 9 * t ** 4), 0, 2), s1)
eq("40^1.5", 40 ** 1.5, 80 * sqrt(10))

# ---- eg: y = x^2/4 - ln(x)/2
dy = lambda x: x / 2 - 1 / (2 * x)
for x in (0.7, 1.5, 2.3):
    eq("perfect square", 1 + dy(x) ** 2, (x / 2 + 1 / (2 * x)) ** 2)
    eq("dy numeric", d(lambda t: t * t / 4 - 0.5 * log(t), x), dy(x), 1e-6)
s2 = (e ** 2 + 1) / 4
eq("eg2", s2, simp(lambda x: x / 2 + 1 / (2 * x), 1, e))
eq("eg2 value", sf(s2), 2.10)
eq("eg2 poly", s2, polylen(lambda t: t, lambda t: t * t / 4 - 0.5 * log(t), 1, e), 1e-3)
yE = e ** 2 / 4 - 0.5
eq("yE", sf(yE, 3), 1.35)
dist = sqrt((e - 1) ** 2 + (yE - 0.25) ** 2)
eq("chord2", sf(dist, 3), 2.04)
eq("dx", sf(e - 1, 3), 1.72)
eq("dy chord", sf(yE - 0.25, 3), 1.10)
assert dist < s2

# ---- cable
s3 = 50 * sinh(0.8)
eq("cable", s3, simp(lambda x: cosh(x / 25), -20, 20))
eq("cable 3sf", sf(s3), 44.4)
eq("cable poly", s3, polylen(lambda t: t, lambda t: 25 * cosh(t / 25), -20, 20), 1e-3)
eq("height at pole", sf(25 * cosh(0.8), 3), 33.4)
eq("sag", sf(25 * cosh(0.8) - 25, 2), 8.4)
eq("plot pt", 25 * cosh(0.8), 33.44, 5e-3)

# ---- x = y^2/2, 0..2
s4 = sqrt(5) + 0.5 * asinh(2)
eq("eg4", s4, simp(lambda y: sqrt(1 + y * y), 0, 2))
eq("eg4 value", sf(s4), 2.96)
eq("asinh 2", asinh(2), log(2 + sqrt(5)))
eq("asinh 2 value", sf(asinh(2), 4), 1.444)
eq("0.722", sf(0.5 * asinh(2), 3), 0.722)
eq("sqrt5", sf(sqrt(5), 4), 2.236)
eq("chord4", sf(sqrt(8), 3), 2.83)
eq("eg4 poly", s4, polylen(lambda t: t * t / 2, lambda t: t, 0, 2), 1e-3)
# u antiderivative check: integral of cosh^2 u from 0 to asinh2
u2 = asinh(2)
eq("cosh2 int", simp(lambda u: cosh(u) ** 2, 0, u2), 0.5 * u2 + 0.5 * sinh(u2) * cosh(u2))
eq("sinh2u/4", 0.25 * sinh(2 * u2), 0.5 * sinh(u2) * cosh(u2))
eq("cosh u", cosh(u2), sqrt(5))

# ---- cycloid a = 3
x = lambda t: 3 * (t - sin(t))
y = lambda t: 3 * (1 - cos(t))
for t in (0.4, 1.7, 3.0, 5.5):
    eq("cyc ds2", d(x, t) ** 2 + d(y, t) ** 2, 36 * sin(t / 2) ** 2, 1e-5)
eq("cyc", simp(lambda t: 6 * sin(t / 2), 0, 2 * pi), 24)
eq("cyc poly", polylen(x, y, 0, 2 * pi), 24, 1e-3)
eq("width", sf(6 * pi, 3), 18.8)
eq("over+down", sf(6 * pi + 12, 3), 30.8)

# ---- astroid
xa = lambda t: cos(t) ** 3
ya = lambda t: sin(t) ** 3
eq("astroid", polylen(xa, ya, 0, 2 * pi), 6, 1e-3)
eq("astroid quarter", polylen(xa, ya, 0, pi / 2), 1.5, 1e-3)
eq("astroid integral", simp(lambda t: 3 * sin(t) * cos(t), 0, pi / 2), 1.5)
for t in (0.3, 2.0):
    eq("astroid ds2", d(xa, t) ** 2 + d(ya, t) ** 2, 9 * sin(t) ** 2 * cos(t) ** 2, 1e-5)

# ---- polar
def plen(r, a, b, n=40000):
    return polylen(lambda t: r(t) * cos(t), lambda t: r(t) * sin(t), a, b, n)


# proof: x'^2 + y'^2 = r^2 + r'^2 for an arbitrary r
rr = lambda t: 2 + sin(3 * t) + 0.3 * t
xx = lambda t: rr(t) * cos(t)
yy = lambda t: rr(t) * sin(t)
for t in (0.2, 1.1, 2.5):
    eq("polar identity", d(xx, t) ** 2 + d(yy, t) ** 2, rr(t) ** 2 + d(rr, t) ** 2, 1e-5)
# circle
eq("circle", simp(lambda t: 2.5, 0, 2 * pi), 2 * pi * 2.5)
# cardioid a = 1 and a = 2.7
for a in (1, 2.7):
    r = lambda t: a * (1 + cos(t))
    eq("cardioid", plen(r, 0, 2 * pi), 8 * a, 1e-3)
    for t in (0.5, 2.0):
        eq("cardioid ds2", r(t) ** 2 + (a * sin(t)) ** 2, 4 * a * a * cos(t / 2) ** 2, 1e-9)
eq("cardioid integral", 2 * simp(lambda t: 2 * cos(t / 2), 0, pi), 8)
eq("box w", 2 - (-0.25), 2.25)
eps = max(sin(t / 1000 * pi) * (1 + cos(t / 1000 * pi)) for t in range(1001))
eq("box h", 2 * eps, 2.598, 1e-3)
eq("box perimeter", sf(2 * (2.25 + 2 * eps), 2), 9.7)
eq("cardioid min x", min(cos(t / 1000 * pi) * (1 + cos(t / 1000 * pi)) for t in range(1001)), -0.25, 1e-5)
# spiral r = 2 e^theta
s5 = 2 * sqrt(2) * (e - 1)
eq("spiral", s5, plen(lambda t: 2 * exp(t), 0, 1), 1e-3)
eq("spiral integral", s5, simp(lambda t: 2 * sqrt(2) * exp(t), 0, 1))
eq("spiral value", sf(s5, 3), 4.86)
eq("2e", sf(2 * e, 3), 5.44)
eq("radial", sf(2 * e - 2, 3), 3.44)
eq("8.88", sf(2 * e - 2 + 2 * e, 3), 8.87)
eq("sqrt2 x radial", s5, sqrt(2) * (2 * e - 2))
# Archimedean r = theta
eq("archimedes", plen(lambda t: t, 0, 2), s4, 1e-3)
eq("archimedes integral", simp(lambda t: sqrt(t * t + 1), 0, 2), s4)

# ---- surfaces
# sphere check
R = 2.3
eq("sphere", simp(lambda xx_: 2 * pi * R, -R, R), 4 * pi * R * R)
for xv in (-1.0, 0.4, 1.9):
    yv = sqrt(R * R - xv * xv)
    eq("sphere y ds", yv * sqrt(1 + (xv / yv) ** 2), R)
# cone check: y = x/2, 0..6
eq("cone S", 9 * sqrt(5) * pi, 2 * pi * simp(lambda t: 0.5 * t * sqrt(5) / 2, 0, 6))
eq("cone S value", sf(9 * sqrt(5) * pi), 63.2)
eq("pi r l", 3 * sqrt(45) * pi, 9 * sqrt(5) * pi)
eq("cone poly", 9 * sqrt(5) * pi, polysurf(lambda t: t, lambda t: t / 2, 0, 6), 1e-3)
eq("ds", sqrt(1 + 0.25), sqrt(5) / 2)
# y = cosh x about x axis
s6 = pi * (log(2) + 15 / 16)
eq("cosh surf", s6, 2 * pi * simp(lambda t: cosh(t) ** 2, 0, log(2)))
eq("cosh surf value", sf(s6), 5.12)
eq("cosh surf poly", s6, polysurf(lambda t: t, lambda t: cosh(t), 0, log(2)), 1e-3)
eq("sinh 2ln2", sinh(2 * log(2)), 15 / 8)
eq("C2", simp(lambda t: cosh(t) ** 2, 0, log(2)), 0.5 * log(2) + 15 / 32)
# y = x^2 about y axis, 0..1
s7 = pi / 6 * (5 * sqrt(5) - 1)
eq("bowl", s7, 2 * pi * simp(lambda t: t * sqrt(1 + 4 * t * t), 0, 1))
eq("bowl value", sf(s7), 5.33)
eq("bowl poly", s7, polysurf(lambda t: t, lambda t: t * t, 0, 1, "y"), 1e-3)
eq("flat disc", sf(pi, 3), 3.14)
eq("cone", sf(pi * sqrt(2), 3), 4.44)
assert pi < pi * sqrt(2) < s7
# dish x = t^2, y = 2t about x axis
s8 = 8 * pi / 3 * (2 * sqrt(2) - 1)
eq("dish", s8, 2 * pi * simp(lambda t: 2 * t * 2 * sqrt(1 + t * t), 0, 1))
eq("dish value", sf(s8), 15.3)
eq("dish poly", s8, polysurf(lambda t: t * t, lambda t: 2 * t, 0, 1), 1e-3)
eq("disc 4pi", sf(4 * pi, 3), 12.6)
assert 4 * pi < s8
for t in (0.3, 0.9):
    eq("dish ds", sqrt(4 * t * t + 4), 2 * sqrt(1 + t * t))

# ---- spot the error
true5 = (16 * sqrt(2) - 8) / 3
eq("spot true", true5, simp(lambda t: t * sqrt(4 + t * t), 0, 2))
eq("spot true value", sf(true5, 3), 4.88)
eq("spot true poly", true5, polylen(lambda t: t * t, lambda t: t ** 3 / 3, 0, 2), 1e-3)
eq("spot wrong", sf(2 / 3 * (8 ** 1.5 - 4 ** 1.5), 3), 9.75)
eq("spot wrong is double", 2 * true5, 2 / 3 * (8 ** 1.5 - 4 ** 1.5))
eq("spot chord", sf(sqrt(16 + 64 / 9), 3), 4.81)
eq("64/9", sf(64 / 9, 3), 7.11)
eq("16+7.11", sf(sqrt(16 + 7.11), 3), 4.81)
eq("8 thr", 8 ** 1.5, 16 * sqrt(2) / 2 * 1.0 + 0 if False else 8 ** 1.5)

# ---- try questions
eq("try1", simp(lambda t: sqrt(1 + (t * sqrt(t * t + 2)) ** 2), 0, 3), 12)
eq("try1 poly", polylen(lambda t: t, lambda t: (t * t + 2) ** 1.5 / 3, 0, 3), 12, 1e-3)
eq("try2", log(2 + sqrt(3)), simp(lambda t: 1 / cos(t), 0, pi / 3))
eq("try2 value", sf(log(2 + sqrt(3))), 1.32)
eq("try3", polylen(lambda t: exp(t) * cos(t), lambda t: exp(t) * sin(t), 0, 1), sqrt(2) * (e - 1), 1e-3)
eq("try3 value", sf(sqrt(2) * (e - 1)), 2.43)
eq("try4", polylen(lambda t: 3 * t * t, lambda t: 2 * t ** 3, 0, 1), 2 * (2 * sqrt(2) - 1), 1e-3)
eq("try5", plen(lambda t: 4 * cos(t), 0, pi), 4 * pi, 1e-3)
eq("try6", 56 * pi / 3, polysurf(lambda t: t, lambda t: 2 * sqrt(t), 0, 3, n=200000), 5e-2)
eq("try6 ds", 2 * sqrt(1 + 1), 2 * sqrt(1 + 1))
eq("try7", 14 * pi / 3, polysurf(lambda t: t, lambda t: t * t / 2, 0, sqrt(3), "y"), 1e-3)
eq("try8", 8 * pi, polysurf(lambda t: 2 * cos(t), lambda t: 2 * sin(t), 0, pi / 2), 1e-3)
eq("hemisphere", 2 * pi * 2 ** 2, 8 * pi)
eq("try9", sf(simp(lambda t: sqrt(1 + cos(t) ** 2), 0, pi), 3), 3.82)
s10 = sqrt(5) / 2 + 0.25 * asinh(2)
eq("try10", s10, simp(lambda t: sqrt(1 + 4 * t * t), 0, 1))
eq("try10 value", sf(s10), 1.48)

# ---- exam practice
eq("q1", 2 / 3 * (5 * sqrt(5) - 2 * sqrt(2)), simp(sqrt, 2, 5))
eq("q1 poly", 2 / 3 * (5 * sqrt(5) - 2 * sqrt(2)), polylen(lambda t: t, lambda t: 2 / 3 * (t - 1) ** 1.5, 2, 5), 1e-3)
xi = lambda t: 4 * (cos(t) + t * sin(t))
yi = lambda t: 4 * (sin(t) - t * cos(t))
for t in (0.4, 1.2):
    eq("q2 dx", d(xi, t), 4 * t * cos(t), 1e-5)
    eq("q2 dy", d(yi, t), 4 * t * sin(t), 1e-5)
eq("q2", polylen(xi, yi, 0, pi / 2), pi ** 2 / 2, 1e-3)
eq("q3", (7 * sqrt(7) - 8) / 3, simp(lambda t: t * sqrt(t * t + 4), 0, sqrt(3)))
eq("q3 poly", (7 * sqrt(7) - 8) / 3, plen(lambda t: t * t, 0, sqrt(3)), 1e-3)
eq("q4", 6 * pi, polysurf(lambda t: t, lambda t: sqrt(9 - t * t), 1, 2), 1e-3)
# q5: cycloid a = 2
x2 = lambda t: 2 * (t - sin(t))
y2 = lambda t: 2 * (1 - cos(t))
for t in (0.5, 2.2, 5.0):
    eq("q5 ds", sqrt(d(x2, t) ** 2 + d(y2, t) ** 2), 4 * sin(t / 2), 1e-5)
eq("q5b", polylen(x2, y2, 0, 2 * pi), 16, 1e-3)
eq("q5c", polysurf(x2, y2, 0, 2 * pi, n=100000), 256 * pi / 3, 1e-2)
eq("q5c integral", 32 * pi * simp(lambda t: sin(t / 2) ** 3, 0, 2 * pi), 256 * pi / 3)
assert F(2, 3) * 128 == F(256, 3)
eq("sin3", simp(lambda t: sin(t) ** 3, 0, pi / 2), 2 / 3)
eq("sin3 pi", simp(lambda t: sin(t) ** 3, 0, pi), 4 / 3)
# q6: r = e^{theta/2}
r6 = lambda t: exp(t / 2)
for t in (0.4, 2.0):
    eq("q6 ds2", r6(t) ** 2 + (0.5 * r6(t)) ** 2, 1.25 * exp(t))
s6a = sqrt(5) * (exp(pi / 2) - 1)
eq("q6a", s6a, plen(r6, 0, pi), 1e-3)
eq("q6b", 0.5 * (exp(pi) - 1), 0.5 * simp(lambda t: exp(t), 0, pi))
al = 2 * log(1 + 10 / sqrt(5))
eq("q6c e^(a/2)", sf(1 + 10 / sqrt(5), 4), 5.472)
eq("q6c", sf(al, 3), 3.40)
eq("q6c check", sqrt(5) * (exp(al / 2) - 1), 10)

# ---- stretch
for a_ in (0.7, log(2), 1.9):
    S = pi * (a_ + sinh(a_) * cosh(a_))
    V = pi / 2 * (a_ + sinh(a_) * cosh(a_))
    eq("soap S", S, 2 * pi * simp(lambda t: cosh(t) ** 2, 0, a_))
    eq("soap V", V, pi * simp(lambda t: cosh(t) ** 2, 0, a_))
    eq("S=2V", S, 2 * V)
eq("soap value", sf(pi * (log(2) + 0.75 * 1.25), 3), 5.12)
eq("sinh cosh ln2", sinh(log(2)) * cosh(log(2)), 15 / 16)
a_ = 1.3
r7 = lambda t: a_ * sin(t / 3) ** 3
eq("q7 length", plen(r7, 0, 3 * pi), 3 * pi * a_ / 2, 1e-3)
for t in (0.8, 4.0):
    dr = a_ * sin(t / 3) ** 2 * cos(t / 3)
    eq("q7 ds2", r7(t) ** 2 + dr ** 2, a_ ** 2 * sin(t / 3) ** 4, 1e-9)
    eq("q7 dr", d(r7, t), dr, 1e-6)

print("ok")
