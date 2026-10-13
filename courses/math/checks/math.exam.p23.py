# checks/math.exam.p23.py: recomputes every number in the chapter
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

eq("P2 min/mark", 75 / 50, 1.5)
eq("P3 min/mark", round(110 / 75, 2), 1.47)
eq("P2 at 1.3", 50 * 1.3, 65)
eq("P2 spare", 75 - 50 * 1.3, 10)
eq("P3 at 1.3", round(75 * 1.3), 98)
eq("P3 spare", round(110 - 75 * 1.3), 12)
# sqrt(4 + x) = 2 sqrt(1 + x/4) at sample values
for x in (0.5, 1.0, 3.0):
    eq("factor out", (4 + x) ** 0.5, 2 * (1 + x / 4) ** 0.5)
# sin^2 x = (1 - cos 2x)/2
from math import sin, cos
for x in (0.3, 1.2, 2.2):
    eq("identity", sin(x) ** 2, (1 - cos(2 * x)) / 2)
eq("|3+(-5)|", abs(3 + -5), 2)
print("ok")
