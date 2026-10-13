# checks/math.exam.p4.py: recomputes every number in the chapter
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

eq("min per mark", 75 / 50, 1.5)
eq("work time", 50 * 1.3, 65)
eq("spare", 75 - 50 * 1.3, 10)
eq("3-mark part", round(3 * 1.3), 4)
eq("6-mark part", round(6 * 1.3), 8)
# the four suvat formulae agree for u=3, a=2, t=4
u, a, t = 3, 2, 4
v = u + a * t
eq("v", v, 11)
eq("s two ways", 0.5 * (u + v) * t, u * t + 0.5 * a * t * t)
eq("v^2", v * v, u * u + 2 * a * (u * t + 0.5 * a * t * t))
print("ok")
