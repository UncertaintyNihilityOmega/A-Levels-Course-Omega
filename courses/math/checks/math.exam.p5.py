# checks/math.exam.p5.py: recomputes every number in the chapter
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

eq("min per mark", 75 / 50, 1.5)
eq("work time", 50 * 1.3, 65)
eq("spare", 75 - 50 * 1.3, 10)
eq("sigma from variance 64", sqrt(64), 8)
print("ok")
