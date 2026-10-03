# checks/math.m.momentum.py: recomputes every number in the momentum chapter.
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

eq("car", 1200 * 15, 18000); eq("bullet", 0.02 * -400, -8)
eq("coal", 12 / 5, 2.4)
eq("rebound", (12 + 3) / 5, 3)
eq("opp mom", 4 * 5 + 2 * -8, 4); eq("opp V", sf(4 / 6, 3), 0.667); eq("opp v", (4 - 4) / 2, 0)
eq("gun", -(0.02 * 400) / 4, -2)
eq("unknown", (12 - 2) / 4, 2.5)
eq("trucks V", 12000 * 3 / 20000, 1.8); eq("KE b", 0.5 * 12000 * 9, 54000); eq("KE a", 0.5 * 20000 * 1.8 ** 2, 32400); eq("loss", 54000 - 32400, 21600)
# exam 1
m = 18 / 5; eq("m", m, 3.6); eq("eq", 15 - 2 * m, -3 + 3 * m, 1e-9); eq("V", -3 / 5, -0.6)
# exam 2
eq("sand", 20 / 8, 2.5)
# try
eq("t1", 0.5 * -12, -6); eq("t2", 1.5 * 4 / 4, 1.5); eq("t3", sf(14 / 3), 4.67); eq("t4", 15 - 15, 0)
eq("t5 V", (18 + 12) / 6, 5); eq("KE b", 81 + 18, 99); eq("KE a", 0.5 * 6 * 25, 75); eq("loss", 99 - 75, 24)
eq("t6", -(40 * 1.2) / 8, -6)
v = (0.4 * 5 + 0.6 * -3 - 0.4 * 2) / 0.6; eq("t7", v, -1)
eq("t7 mom", 0.4 * 5 + 0.6 * -3, 0.2, 1e-12)
eq("t9 mom", 0.5 * 4 + 0.3 * 2, 2.6); v = (2.6 - 0.75) / 0.3; eq("t9a", sf(v), 6.17); eq("t9b", 2.6 / 0.8, 3.25)
eq("t10 v", -(2 * 6) / 3, -4); eq("t10 KE", 0.5 * 2 * 36 + 0.5 * 3 * 16, 60)
eq("q1", 3 * 4, 12); eq("q2", 6 / 6, 1); eq("q2w", 6 / 4, 1.5)
print("ok")
