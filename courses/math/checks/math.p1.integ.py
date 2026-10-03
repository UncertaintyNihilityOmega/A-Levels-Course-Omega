# checks/math.p1.integ.py: recomputes every number in the Integration chapter.
from fractions import Fraction as F
from math import isclose, pi, sqrt

def eq(label, got, want, tol=1e-7):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def pint(poly, a, b):
    """exact definite integral of a polynomial {power: coeff} between a and b"""
    tot = F(0)
    for p, c in poly.items():
        tot += F(c) * (F(b)**(p + 1) - F(a)**(p + 1)) / (p + 1)
    return tot

def pmul(p, q):
    r = {}
    for a, x in p.items():
        for b, y in q.items():
            r[a + b] = r.get(a + b, 0) + x * y
    return r

def deriv_check(F_, f, xs=(0.7, 1.3, 2.9), h=1e-6):
    for x in xs:
        eq("deriv", (F_(x + h) - F_(x - h)) / (2 * h), f(x), 1e-5)

# reversing differentiation
deriv_check(lambda x: x**3 - 2*x**2 + 5*x, lambda x: 3*x**2 - 4*x + 5)
deriv_check(lambda x: 2/3 * x**1.5 - 3/x, lambda x: sqrt(x) + 3/x**2)
deriv_check(lambda x: x**3/3 - x**2/2 - 6*x, lambda x: (x + 2) * (x - 3))
# (ax+b)^n
deriv_check(lambda x: (2*x + 3)**5 / 10, lambda x: (2*x + 3)**4)
deriv_check(lambda x: 6 / (3 - x), lambda x: 6 / (3 - x)**2, xs=(0.7, 1.3, 2.1))
deriv_check(lambda x: 0.5 * sqrt(4*x - 1), lambda x: (4*x - 1)**-0.5, xs=(0.9, 1.3, 2.9))
# constants
assert 2 - 4 + 7 == 5
eq("c2", 20 - 2 * 9**1.5, -34); eq("2*27", 2 * 27, 54)
deriv_check(lambda x: 2 * (2*x - 1)**1.5 - 34, lambda x: 6 * (2*x - 1)**0.5, xs=(1.0, 2.0, 5.0))
# tank
V = lambda t: t**2 - 20*t + 150
assert V(0) == 150 and V(5) == 75
deriv_check(V, lambda t: -(20 - 2*t), xs=(1.0, 3.0))

# definite integrals
assert pint({1: 2, 0: 1}, 1, 3) == 10
eq("sqrt x", simpson(lambda x: sqrt(x), 1, 4), 14 / 3)
assert F(2, 3) * 8 - F(2, 3) == F(14, 3)

# area examples
assert pint({2: 1, 0: 1}, 1, 3) == F(32, 3)
assert 9 + 3 - (F(1, 3) + 1) == F(32, 3)
q = {2: 1, 1: -4, 0: 3}
assert pint(q, 0, 1) == F(4, 3) and pint(q, 1, 3) == F(-4, 3) and pint(q, 0, 3) == 0
assert F(4, 3) + F(4, 3) == F(8, 3)
# integration wrt y
eq("16/3", simpson(lambda y: sqrt(y), 0, 4), 16 / 3, 1e-4); assert F(2, 3) * 8 == F(16, 3)
# line and parabola
assert (-1)**2 - 2 * (-1) - 3 == 0 and 3**2 - 2 * 3 - 3 == 0
assert pint({0: 3, 1: 2, 2: -1}, -1, 3) == F(32, 3)
assert 9 + 9 - 9 == 9 and F(1) - 3 + F(1, 3) == F(-5, 3) and 9 - F(-5, 3) == F(32, 3)
eq("sqrt-x2", simpson(lambda x: sqrt(x) - x**2, 0, 1), 1 / 3, 1e-4)
assert 0.25**0.5 == 0.5 and 0.25**2 == 0.0625

# improper
for t in (1e3, 1e6, 1e9): eq("a", -1 / t + 1, 1, 2e-3)
for t in (1e-4, 1e-8): eq("b", 2 - 2 * sqrt(t), 2, 0.03)
for t in (1e4, 1e8): assert 2 * sqrt(t) - 2 > 100 - 3
for t in (1e6, 1e10): eq("exam improper", -8 / sqrt(t) + 8 / 3, 8 / 3, 0.01)

# volumes
eq("32pi/5", pi * simpson(lambda x: x**4, 0, 2), 32 * pi / 5); eq("sf", round(32 * pi / 5, 1), 20.1)
eq("8pi", pi * simpson(lambda y: y, 0, 4), 8 * pi); eq("8pi sf", round(8 * pi, 1), 25.1)
eq("cone", pi * simpson(lambda x: 4 * x**2, 0, 3), 36 * pi); eq("cone formula", pi * 36 * 3 / 3, 36 * pi)
poly = pmul({2: 1, 0: -9}, {2: 1, 0: -9}); poly[0] -= 25
assert poly == {4: 1, 2: -18, 0: 56}
V = pint({4: 1, 2: -18, 0: 56}, -2, 2); assert V == 2 * (112 - 48 + F(32, 5)) == F(704, 5)
eq("vol3sf", round(float(F(704, 5)) * pi), 442)
assert 9 - 2**2 == 5

# exam A
assert 6 * 4 - 16 == 8 and 2 * 4 == 8 and 6*0 - 0 == 0
assert pint({1: 4, 2: -1}, 0, 4) == F(32, 3) and 32 - F(64, 3) == F(32, 3)
poly = pmul({1: 6, 2: -1}, {1: 6, 2: -1}); poly[2] -= 4
assert poly == {2: 32, 3: -12, 4: 1}
Vv = pint(poly, 0, 4); assert Vv == F(1792, 15) and F(2048, 3) - 768 + F(1024, 5) == F(1792, 15)
eq("375", round(float(Vv) * pi), 375)

# exam B
y = lambda x: 2 * x**1.5 + 4 / x - 7
eq("P", y(4), 10); eq("y1", y(1), -1); eq("diff", y(4) - y(1), 11)
deriv_check(y, lambda x: 3 * sqrt(x) - 4 / x**2)

# try questions
deriv_check(lambda x: x**4 - 3*x**2 + x, lambda x: 4*x**3 - 6*x + 1)
deriv_check(lambda x: -1/x**2 + 2/3 * x**1.5, lambda x: 2/x**3 + sqrt(x))
deriv_check(lambda x: (3*x - 1)**6 / 18, lambda x: (3*x - 1)**5)
deriv_check(lambda x: sqrt(2*x + 5), lambda x: (2*x + 5)**-0.5)
assert 8 - 6 + 4 == 6
assert pint({2: 3, 1: -2}, 0, 2) == 4 and F(1) - F(1, 4) == F(3, 4)
assert pint({1: 4, 2: -1}, 0, 4) == F(32, 3)
assert pint({2: 1, 1: -2, 0: -3}, -1, 3) == F(-32, 3)
assert pint({1: 1, 0: 6, 2: -1}, -2, 3) == F(125, 6) and F(27, 2) + F(22, 3) == F(125, 6)
assert 3 + 6 == 9
eq("T8a", 3 * (1 / 3), 1)       # [-x^-3] from 1 to inf
assert 2 * 2 == 4
assert pint({1: 1}, 0, 4) == 8 and pint({2: 1, 4: -1}, 0, 1) == F(2, 15)
Vc = pi * (-F(48, 27) + 48); eq("416pi/9", float(Vc), 416 * pi / 9)
assert -12 / 3 + 12 * 1 == 8
# quiz
assert 4 * 2 == 8 and F(1, 4) - F(1, 4) == 0 and 2 * F(1, 4) == F(1, 2)
assert pint({2: 1, 0: -4}, -2, 2) == F(-32, 3) and pint({2: 1, 0: -4}, 0, 2) == F(-16, 3)
print("ok")
