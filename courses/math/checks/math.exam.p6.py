# checks/math.exam.p6.py: recomputes every number in the chapter
from math import isclose, exp

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

eq("min per mark", 75 / 50, 1.5)
eq("work time", 50 * 1.3, 65)
eq("spare", 75 - 50 * 1.3, 10)
# Poisson scaling: P(none in 10 m) = 0.449 means lambda = 0.8
eq("p10", round(exp(-0.8), 3), 0.449)
eq("doubled wrongly", round(2 * round(exp(-0.8), 3), 3), 0.898)
eq("p20 right", round(exp(-1.6), 3), 0.202)
# variance rules: Var(3X-2) = 9 Var X; X1+X2 gives 2 sigma^2, 2X gives 4 sigma^2
v = 5.0
eq("var 3X-2", 3**2 * v, 45.0)
eq("X1+X2", v + v, 2 * v)
eq("2X", 2**2 * v, 4 * v)
print("ok")
