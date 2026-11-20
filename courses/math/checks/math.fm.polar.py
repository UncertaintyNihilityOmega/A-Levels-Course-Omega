# checks/math.fm.polar.py: recomputes every number in Polar coordinates.
# Standard library only: Simpson for areas, finite differences for derivatives, sampling for greatest values.
from math import isclose, sqrt, sin, cos, tan, atan2, atan, pi, exp, acos, asin


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def simpson(g, a, b, n=4000):
    h = (b - a) / n
    s = g(a) + g(b)
    for i in range(1, n):
        s += g(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def area(r, a, b):
    """1/2 integral of r^2 over [a, b], counting only r >= 0 (the convention)."""
    return 0.5 * simpson(lambda t: (r(t) ** 2 if r(t) >= 0 else 0.0), a, b)


def grid(lo, hi, n=200001):
    return [lo + (hi - lo) * i / (n - 1) for i in range(n)]


# ---- warm-up
eq("sector", 0.5 * 36 * 0.5, 9)
for t in grid(0, 2 * pi, 50):
    eq("cos^2", cos(t) ** 2, 0.5 * (1 + cos(2 * t)))
F = lambda t: 0.5 * t * exp(2 * t) - 0.25 * exp(2 * t)
for t in [0.3, 1.0, 2.2]:
    eq("by parts", d(F, t), t * exp(2 * t), 1e-4)

# ---- conversions
x, y = -1, sqrt(3)
eq("r", sqrt(x * x + y * y), 2)
eq("theta", atan2(y, x), 2 * pi / 3)
eq("calc tan^-1", atan(y / x), -pi / 3)
x, y = -2, -2
eq("r2", sqrt(x * x + y * y), 2 * sqrt(2))
eq("theta2", atan2(y, x), -3 * pi / 4)
eq("theta2 alt", atan2(y, x) + 2 * pi, 5 * pi / 4)
eq("x", 4 * cos(pi / 3), 2)
eq("y", 4 * sin(pi / 3), 2 * sqrt(3))

# ---- equations: x^2+y^2 = 4x <-> r = 4cos t
for t in grid(-pi / 2, pi / 2, 21):
    r = 4 * cos(t)
    X, Y = r * cos(t), r * sin(t)
    eq("circle", X * X + Y * Y, 4 * X, 1e-9)
# y = 3 <-> r = 3 csc t
for t in grid(0.2, pi - 0.2, 21):
    r = 3 / sin(t)
    eq("line y=3", r * sin(t), 3)
# y^2 = 4x <-> r = 4cos/sin^2
for t in grid(0.3, 1.4, 11):
    r = 4 * cos(t) / sin(t) ** 2
    eq("parabola", (r * sin(t)) ** 2, 4 * r * cos(t), 1e-9)
# r = 2a cos t circle (a = 3)
for t in grid(-pi / 2, pi / 2, 21):
    r = 6 * cos(t)
    X, Y = r * cos(t), r * sin(t)
    eq("circle a", (X - 3) ** 2 + Y ** 2, 9, 1e-9)
# r = 4/(1+cos t) -> y^2 = 16 - 8x
for t in grid(-2.5, 2.5, 21):
    r = 4 / (1 + cos(t))
    X, Y = r * cos(t), r * sin(t)
    eq("parabola 2", Y * Y, 16 - 8 * X, 1e-9)
    eq("r = 4 - x", r, 4 - X, 1e-9)
# cardioid Cartesian
for t in grid(0, 2 * pi, 21):
    r = 1 + cos(t)
    X, Y = r * cos(t), r * sin(t)
    eq("cardioid cartesian", (X * X + Y * Y - X) ** 2, X * X + Y * Y, 1e-9)

# ---- cardioid sketch table
for t, want in [(0, 2), (pi / 3, 1.5), (pi / 2, 1), (2 * pi / 3, 0.5), (pi, 0)]:
    eq("cardioid table", 1 + cos(t), want, 1e-12)
# microphone: r >= 1 <=> cos >= 0
for t in grid(-pi, pi, 20001):
    assert (1 + cos(t) >= 1 - 1e-12) == (abs(t) <= pi / 2 + 1e-9) or abs(abs(t) - pi / 2) < 1e-3
# limacons
assert min(2 + cos(t) for t in grid(0, 2 * pi, 1001)) >= 1 - 1e-9 and max(2 + cos(t) for t in grid(0, 2 * pi, 1001)) <= 3 + 1e-9
eq("r(pi/2)", 2 + cos(pi / 2), 2)
for t in grid(-pi, pi, 20001):
    assert (1 + 2 * cos(t) >= -1e-12) == (abs(t) <= 2 * pi / 3 + 1e-9) or abs(abs(t) - 2 * pi / 3) < 1e-3
eq("limacon pole", 1 + 2 * cos(2 * pi / 3), 0, 1e-12)
eq("limacon y axis", 1 + 2 * cos(pi / 2), 1)
# rose r = a cos 2t
ok_set = lambda t: cos(2 * t) >= -1e-12
for t in grid(0, 2 * pi, 40001):
    inside = (0 <= t <= pi / 4) or (3 * pi / 4 <= t <= 5 * pi / 4) or (7 * pi / 4 <= t <= 2 * pi)
    assert ok_set(t) == inside or min(abs(t - c) for c in (pi / 4, 3 * pi / 4, 5 * pi / 4, 7 * pi / 4)) < 1e-3, t
for t in (pi / 4, 3 * pi / 4, 5 * pi / 4, 7 * pi / 4):
    eq("rose pole", cos(2 * t), 0, 1e-12)
for t in grid(0, 2 * pi, 51):
    eq("rose symmetry 1", cos(-2 * t), cos(2 * t), 1e-12)
    eq("rose symmetry 2", cos(2 * (pi - t)), cos(2 * t), 1e-12)
# spirals
eq("spiral turn", 2 * pi, 2 * pi)
eq("e^(1)", sf(exp(1)), 2.72)
eq("e^2", sf(exp(2)), 7.39)
eq("e^(theta/pi) at pi", exp(pi / pi), exp(1))

# ---- greatest distance of cardioid (a = 1)
yy = lambda t: (1 + cos(t)) * sin(t)
for t in [0.3, 1.0, 2.0, 2.9]:
    eq("dy/dt", d(yy, t), 2 * cos(t) ** 2 + cos(t) - 1, 1e-5)
    eq("dy/dt factor", d(yy, t), (2 * cos(t) - 1) * (cos(t) + 1), 1e-5)
eq("y at pi/3", yy(pi / 3), 3 * sqrt(3) / 4)
eq("max y", max(yy(t) for t in grid(0, pi, 200001)), 3 * sqrt(3) / 4, 1e-9)
eq("r at pi/3", 1 + cos(pi / 3), 1.5)

# ---- areas
eq("cardioid area", area(lambda t: 1 + cos(t), 0, 2 * pi), 1.5 * pi, 1e-9)
eq("cardioid area a=2", area(lambda t: 2 * (1 + cos(t)), 0, 2 * pi), 6 * pi, 1e-9)
eq("cardioid bounds", sf(1.5 * pi, 3), 4.71)
assert pi < 1.5 * pi < 4 * pi
# integrand algebra
for t in grid(0, 2 * pi, 31):
    eq("expand", (1 + cos(t)) ** 2, 1.5 + 2 * cos(t) + 0.5 * cos(2 * t), 1e-12)
# petal
eq("petal a=1", area(lambda t: cos(2 * t), -pi / 4, pi / 4), pi / 8, 1e-9)
eq("petal half", 2 * area(lambda t: cos(2 * t), 0, pi / 4), pi / 8, 1e-9)
# radar
eq("radar area", area(lambda t: 30 * cos(2 * t), -pi / 4, pi / 4), 112.5 * pi, 1e-6)
eq("radar area 3sf", sf(112.5 * pi), 353)
ry = lambda t: 30 * cos(2 * t) * sin(t)
s = 1 / sqrt(6)
eq("radar max y", max(ry(t) for t in grid(0, pi / 4, 200001)), 20 / sqrt(6), 1e-7)
eq("radar ymax", ry(asin(s)), 20 / sqrt(6), 1e-9)
eq("radar 20/sqrt6", sf(20 / sqrt(6)), 8.16)
eq("radar width", sf(2 * 20 / sqrt(6)), 16.3)
eq("radar dy/ds", 30 - 180 * s * s, 0, 1e-9)
eq("radar y via s", 30 * s * (1 - 2 * s * s), 30 / sqrt(6) * 2 / 3, 1e-9)
# spiral r = a t, 0..pi
eq("spiral area", area(lambda t: t, 0, pi), pi ** 3 / 6, 1e-6)
# circle and cardioid
eq("intersection", 3 * cos(pi / 3), 1 + cos(pi / 3), 1e-12)
eq("r at intersection", 3 * cos(pi / 3), 1.5)
assert 3 * cos(0) > 1 + cos(0)
Ac = 2 * 0.5 * simpson(lambda t: 9 * cos(t) ** 2 - (1 + cos(t)) ** 2, 0, pi / 3)
eq("lune area", Ac, pi, 1e-8)
for t in grid(0, pi / 3, 21):
    eq("8cos^2", 8 * cos(t) ** 2 - 1 - 2 * cos(t), 3 + 4 * cos(2 * t) - 2 * cos(t), 1e-12)
eq("lune antiderivative", (3 * pi / 3 + 2 * sin(2 * pi / 3) - 2 * sin(pi / 3)), pi, 1e-12)
# circle r=2 and line r=sec t
eq("line meets circle", 1 / cos(pi / 3), 2)
Aseg = 0.5 * simpson(lambda t: 4 - 1 / cos(t) ** 2, -pi / 3, pi / 3)
eq("segment", Aseg, 4 * pi / 3 - sqrt(3), 1e-8)
eq("segment geometry", 0.5 * 4 * (2 * pi / 3 - sin(2 * pi / 3)), 4 * pi / 3 - sqrt(3), 1e-12)
assert acos(1 / 2) * 2 == 2 * pi / 3 or abs(acos(0.5) * 2 - 2 * pi / 3) < 1e-12

# ---- exam example 1: r = 3 + 2cos
r1 = lambda t: 3 + 2 * cos(t)
eq("least", min(r1(t) for t in grid(0, 2 * pi, 100001)), 1, 1e-9)
eq("greatest", max(r1(t) for t in grid(0, 2 * pi, 100001)), 5, 1e-9)
eq("area 11pi", area(r1, 0, 2 * pi), 11 * pi, 1e-8)
for t in grid(0, 2 * pi, 31):
    eq("expand ex1", (3 + 2 * cos(t)) ** 2, 11 + 12 * cos(t) + 2 * cos(2 * t), 1e-12)
y1 = lambda t: r1(t) * sin(t)
for t in [0.4, 1.0, 2.0]:
    eq("dy ex1", d(y1, t), 3 * cos(t) + 2 * cos(2 * t), 1e-5)
    eq("dy ex1 quad", 3 * cos(t) + 2 * cos(2 * t), 4 * cos(t) ** 2 + 3 * cos(t) - 2, 1e-12)
c = (-3 + sqrt(41)) / 8
eq("c", sf(c, 4), 0.4254)
eq("quad root", 4 * c * c + 3 * c - 2, 0, 1e-12)
eq("other root", sf((-3 - sqrt(41)) / 8, 4), -1.175)
sn = sqrt(1 - c * c)
eq("sin", sf(sn, 4), 0.9050)
eq("ymax", sf((3 + 2 * c) * sn, 3), 3.48)
eq("ymax 4sf", sf((3 + 2 * c) * sn, 4), 3.485)
eq("ymax numeric", max(y1(t) for t in grid(0, pi, 200001)), (3 + 2 * c) * sn, 1e-9)

# ---- exam example 2: r = sqrt(t) e^t
r2 = lambda t: sqrt(t) * exp(t)
eq("end", sf(r2(1), 3), 2.72)
eq("mid", sf(r2(0.5), 3), 1.17)
eq("0.707 * 1.65", sf(0.707 * 1.65, 3), 1.17)
eq("area exam 2", area(r2, 0, 1), (exp(2) + 1) / 8, 1e-8)
eq("parts", simpson(lambda t: t * exp(2 * t), 0, 1), 0.5 * exp(2) - 0.25 * exp(2) + 0.25, 1e-8)

# ---- exam example 3: circle 4cos t and line 3 sec t
eq("meets", 4 * cos(pi / 6), 3 / cos(pi / 6), 1e-12)
eq("r", 4 * cos(pi / 6), 2 * sqrt(3), 1e-12)
assert abs(cos(pi / 6) ** 2 - 0.75) < 1e-12
A3 = 2 * 0.5 * simpson(lambda t: 16 * cos(t) ** 2 - 9 / cos(t) ** 2, 0, pi / 6)
eq("segment 3", A3, 4 * pi / 3 - sqrt(3), 1e-8)
eq("anti", 8 * (pi / 6) + 4 * sin(pi / 3) - 9 * tan(pi / 6), 4 * pi / 3 + 2 * sqrt(3) - 3 * sqrt(3), 1e-12)
eq("9 tan", 9 * tan(pi / 6), 3 * sqrt(3), 1e-12)
eq("geometry", 0.5 * 4 * (2 * pi / 3 - sqrt(3) / 2), 4 * pi / 3 - sqrt(3), 1e-12)
# circle centre (2,0) radius 2, line x=3 at distance 1
assert abs(2 * acos(1 / 2) - 2 * pi / 3) < 1e-12

# ---- spot the error
eq("true area", area(lambda t: 3 * cos(t), -pi / 2, pi / 2), 9 * pi / 4, 1e-8)
eq("student area", area(lambda t: 3 * cos(t), 0, 2 * pi), 9 * pi / 4, 1e-8)       # convention: r<0 not counted
eq("student wrong", 0.5 * simpson(lambda t: 9 * cos(t) ** 2, 0, 2 * pi), 9 * pi / 2, 1e-8)
eq("circle diameter 3", pi * 1.5 ** 2, 9 * pi / 4)
eq("student line 3", 9 / 4 * (2 * pi + 0.5 * sin(4 * pi)), 9 * pi / 2)

# ---- try
eq("try1 r", sqrt(18), 3 * sqrt(2))
eq("try1 theta", atan2(3, -3), 3 * pi / 4)
eq("try2 x", 6 * cos(5 * pi / 6), -3 * sqrt(3))
eq("try2 y", 6 * sin(5 * pi / 6), 3)
assert 4 + 3 == 7 and 4 - 3 == 1
for t in grid(0, 2 * pi, 31):
    assert 4 + 3 * cos(t) <= 7 + 1e-12 and 4 + 3 * cos(t) >= 1 - 1e-12
ok_set = lambda t: sin(3 * t) >= -1e-12
for t in grid(0, 2 * pi, 40001):
    inside = (0 <= t <= pi / 3) or (2 * pi / 3 <= t <= pi) or (4 * pi / 3 <= t <= 5 * pi / 3)
    assert ok_set(t) == inside or min(abs(t - c0) for c0 in (0, pi / 3, 2 * pi / 3, pi, 4 * pi / 3, 5 * pi / 3, 2 * pi)) < 1e-3
eq("try area circle", 0.5 * 25 * 2 * pi, 25 * pi)
eq("try spiral", area(lambda t: t, 0, 2), 4 / 3, 1e-8)
eq("try circle 2sin", area(lambda t: 2 * sin(t), 0, pi), pi, 1e-8)
eq("try 2+sin2t", max(2 + sin(2 * t) for t in grid(0, 2 * pi, 100001)), 3, 1e-9)

# ---- exam practice
eq("q1", sqrt(9 + 9), 3 * sqrt(2))
eq("q1 theta", atan2(3, -3), 3 * pi / 4)
for t in grid(-2.5, 2.5, 11):
    r = 5 / cos(t)
    eq("q1 x", r * cos(t), 5)
# q3
eq("q3 max", max(4 * sin(2 * t) for t in grid(0, pi / 2, 10001)), 4, 1e-9)
eq("q3 where", 4 * sin(2 * pi / 4), 4)
# q4 3+cos
eq("q4 area", area(lambda t: 3 + cos(t), 0, 2 * pi), 19 * pi / 2, 1e-8)
for t in grid(0, 2 * pi, 31):
    eq("q4 expand", (3 + cos(t)) ** 2, 9.5 + 6 * cos(t) + 0.5 * cos(2 * t), 1e-12)
# q5
eq("q5 area", area(lambda t: t * t, 0, pi / 2), pi ** 5 / 320, 1e-8)
eq("q5 end", (pi / 2) ** 2, pi ** 2 / 4)
# q6 mast
eq("q6 petal", area(lambda t: 8 * sin(3 * t), 0, pi / 3), 16 * pi / 3, 1e-8)
eq("q6 total", sf(16 * pi, 3), 50.3)
eq("q6 three petals", area(lambda t: 8 * sin(3 * t), 0, 2 * pi), 16 * pi, 1e-8)
for t in grid(0, pi / 3, 21):
    eq("q6 identity", 64 * sin(3 * t) ** 2 / 2, 16 * (1 - cos(6 * t)), 1e-12)
# q7: circles r = 2 sin t, r = 1
eq("q7 meet", 2 * sin(pi / 6), 1, 1e-12)
Aq7 = 2 * 0.5 * simpson(lambda t: 4 * sin(t) ** 2 - 1, pi / 6, pi / 2)
eq("q7 area", Aq7, pi / 3 + sqrt(3) / 2, 1e-8)
for t in grid(0, pi, 21):
    eq("q7 identity", 4 * sin(t) ** 2 - 1, 1 - 2 * cos(2 * t), 1e-12)
eq("q7 antiderivative", (pi / 2 - sin(pi)) - (pi / 6 - sin(pi / 3)), pi / 3 + sqrt(3) / 2, 1e-12)
eq("q7 numeric", sf(pi / 3 + sqrt(3) / 2), 1.91)
# also check r < 2 region: inside C1 outside C2 means r1 > r2 between pi/6 and 5pi/6
for t in grid(pi / 6 + 1e-3, 5 * pi / 6 - 1e-3, 101):
    assert 2 * sin(t) > 1

# ---- stretch 1: lemniscate
rl = lambda t: sqrt(cos(2 * t)) if cos(2 * t) >= 0 else -1
eq("lemniscate total", area(rl, 0, 2 * pi), 1, 1e-3)
eq("lemniscate loop", area(rl, -pi / 4, pi / 4), 0.5, 1e-3)
yl = lambda t: rl(t) * sin(t) if rl(t) >= 0 else 0
eq("lemniscate ymax", max(yl(t) for t in grid(0, pi / 4, 200001)), 1 / (2 * sqrt(2)), 1e-8)
eq("a/(2 sqrt2)", sf(1 / (2 * sqrt(2)), 3), 0.354)
for s_ in (0.1, 0.25, 0.3):
    eq("y^2", (1 - 2 * s_) * s_, s_ - 2 * s_ * s_)
eq("y2 at 1/4", (1 - 2 * 0.25) * 0.25, 1 / 8)

# ---- stretch 2: Archimedean spiral
eq("first turn", area(lambda t: t, 0, 2 * pi), 4 * pi ** 3 / 3, 1e-6)
eq("circle", pi * (2 * pi) ** 2, 4 * pi ** 3)
eq("one third", 4 * pi ** 3 / 3 * 3, 4 * pi ** 3)
Aring = 0.5 * simpson(lambda p: (p + 2 * pi) ** 2 - p * p, 0, 2 * pi)
eq("ring", Aring, 8 * pi ** 3, 1e-6)
eq("six times", 6 * 4 * pi ** 3 / 3, 8 * pi ** 3)
for p in grid(0, 2 * pi, 21):
    eq("ring expand", (p + 2 * pi) ** 2 - p * p, 4 * pi * p + 4 * pi ** 2, 1e-9)

# ---- quiz
eq("quiz area", area(lambda t: 2 * cos(t), -pi / 2, pi / 2), pi, 1e-8)
eq("quiz 2pi", 0.5 * 0 + simpson(lambda t: 4 * cos(t) ** 2, -pi / 2, pi / 2), 2 * pi, 1e-8)
eq("quiz 4pi", simpson(lambda t: 4 * cos(t) ** 2, 0, 2 * pi), 4 * pi, 1e-8)
eq("quiz r pole", 3 * sin(2 * (pi / 2)), 0, 1e-12)
eq("quiz line", 6 / 1, 6)

# ---- marks totals
assert 3 + 4 + 5 == 12 and 2 + 6 == 8 and 3 + 5 == 8
assert 4 + 4 + 4 + 5 + 5 + 6 + 11 == 39
assert 2 + 3 + 3 == 8 and 2 + 2 + 4 == 8
assert 3 + 2 == 5

print("ok")
