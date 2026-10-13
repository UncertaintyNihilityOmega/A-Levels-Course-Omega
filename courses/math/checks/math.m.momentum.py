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
# ---- v2 additions ----
from math import sqrt
# warm-up
eq("w1 a", (8 - 2) / 3, 2); eq("w1 F", 3 * 2, 6); eq("w2", (15 - 8 - 4) / 3, 1); eq("w2 chk", 15 - 8, 3 * 1 + 4)
# proof
eq("pr dA", 2 * (2.4 - 6), -7.2); eq("pr dB", 3 * (2.4 - 0), 7.2); eq("pr V", 2 * 6 / 5, 2.4)
# spot the error
eq("se V", (18 - 10) / 8, 1); eq("se wrong", (18 + 10) / 8, 3.5)
# exam practice
V = 0.4 * 5 / 1.0; eq("q1 V", V, 2); eq("q1 ke0", 0.5 * 0.4 * 25, 5); eq("q1 ke1", 0.5 * 1.0 * 4, 2); eq("q1 loss", 5 - 2, 3)
eq("q2", sf(0.015 * 600 / 3.5), 2.57)
eq("q3", (2 * 7 - 5 * 3) / 2, -0.5)
m = 6; eq("q4", 3 * 4 + m * 1, (3 + m) * 2)
v = (0 + 2 * 2) / 3; eq("q5 v", sf(v), 1.33); eq("q5 mom", 2 * 6 - 3 * 4, 2 * -2 + 3 * v)
ke0 = 0.5 * 2 * 36 + 0.5 * 3 * 16; ke1 = 0.5 * 2 * 4 + 0.5 * 3 * (4 / 3) ** 2
eq("q5 ke0", ke0, 60); eq("q5 ke1", sf(ke1), 6.67); eq("q5 loss", sf(ke0 - ke1, 3), 53.3)
eq("q6 V1", 6000 * 4 / 10000, 2.4); eq("q6 V2", 10000 * 2.4 / 20000, 1.2); eq("q6 one", 24000 / 20000, 1.2)
a = 0.3 * 30 / 3; eq("q7 F", 0.3 * 30, 9); eq("q7 a", a, 3); v = sqrt(64 - 2 * 3 * 5); eq("q7 v2", 64 - 30, 34); eq("q7 v", sf(v), 5.83)
V = 3 * v / 5; eq("q7 V", sf(V), 3.50); eq("q7 F2", 0.3 * 50, 15); eq("q7 a2", 15 / 5, 3); eq("q7 V2", round(V ** 2, 2), 12.24); eq("q7 s", V ** 2 / 6, 2.04, 1e-9)
# stretch
vt = -120 / 200; eq("s1 v", vt, -0.6); eq("s1 man", vt + 1.5, 0.9); eq("s1 eq", 80 * (vt + 1.5) + 120 * vt, 0, 1e-9); eq("s1 chk", 80 * 0.9, 72); eq("s1 chk2", 120 * 0.6, 72)
eq("s2 F", 0.5 * 20, 10); eq("s2 a", 10 / 2, 5); V = sqrt(2 * 5 * 2); eq("s2 V", sf(V), 4.47); u = 2 * V / 0.02; eq("s2 u", sf(u), 447); eq("s2 chk", round(0.02 * u, 2), 8.94); eq("s2 chk2", round(2 * V, 2), 8.94)

print("ok")
