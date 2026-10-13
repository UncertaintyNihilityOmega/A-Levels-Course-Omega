# checks/math.exam.skills.py: recomputes every number in the chapter
from math import sin, cos, radians, sqrt, pi, isclose
from fractions import Fraction

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

# show that / hence: 2 sin^2 t = 3 cos t  <=>  2cos^2 t + 3 cos t - 2 = 0
for t in (0.3, 1.1, 2.5, 4.0):
    lhs = 2 * sin(t) ** 2 - 3 * cos(t)
    rhs = -(2 * cos(t) ** 2 + 3 * cos(t) - 2)
    eq("identity", lhs, rhs)
c = 0.5
eq("quadratic at 1/2", 2 * c * c + 3 * c - 2, 0)
eq("quadratic at -2", 2 * 4 - 6 - 2, 0)
for th in (60, 300):
    eq(f"solution {th}", 2 * sin(radians(th)) ** 2 - 3 * cos(radians(th)), 0)
eq("360-60", 360 - 60, 300)

# follow-through
eq("true gradient", (8 - 2) / (3 - 1), 3)
eq("true line at x=1", 3 * 1 - 1, 2)
eq("true line at x=3", 3 * 3 - 1, 8)
eq("student x", 10 / 2, 5)
assert Fraction(11, 3) == Fraction(10 + 1, 3)
eq("true x", (10 + 1) / 3, 11 / 3)

# exact integral
eq("integral", 0.5 * sin(pi / 3), sqrt(3) / 4)
eq("decimal", round(sqrt(3) / 4, 3), 0.433)

# verify
eq("verify root", 2**3 - 2 * 2 - 4, 0)
print("ok")
