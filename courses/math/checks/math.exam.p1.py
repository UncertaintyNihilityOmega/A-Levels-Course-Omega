# checks/math.exam.p1.py: recomputes every number in the chapter
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

eq("minutes per mark", round(110 / 75, 2), 1.47)
eq("4 marks", round(4 * 1.3), 5)
eq("6 marks", round(6 * 1.3), 8)
eq("10 marks", round(10 * 1.3), 13)
eq("whole paper", round(75 * 1.3), 98)
eq("spare", round(110 - 75 * 1.3), 12)
print("ok")
