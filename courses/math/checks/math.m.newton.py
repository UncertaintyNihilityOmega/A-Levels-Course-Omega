# checks/math.m.newton.py: recomputes every number in the Newton's laws chapter.
from math import isclose, sqrt, sin, cos, radians

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

g = 10
# block pulled
eq("a1", (20 - 8) / 4, 3); eq("v1", 3 * 5, 15)
# lift
eq("R", 70 * (g + 1.5), 805); eq("700+105", 700 + 105, 805)
eq("T", 480 * 10.5, 5040); eq("T form", 4800 + 480 * 0.5, 5040); eq("R2", 80 * 10.5, 840)
# smooth slope
eq("a slope", 2 * 10 * sin(radians(30)) / 2, 5); eq("v2", 2 * 5 * 4, 40); eq("v", sf(sqrt(40)), 6.32)
# rough slope 3-4-5
eq("R", 5 * 10 * 0.8, 40); eq("F", 0.5 * 40, 20); eq("W//", 5 * 10 * 0.6, 30)
eq("a down", (30 - 20) / 5, 2); eq("a up", (30 + 20) / 5, 10); eq("s", 64 / 20, 3.2)
# pulled block
eq("R pull", 40 - 20 * 0.6, 28); eq("F pull", 0.3 * 28, 8.4); eq("a pull", (16 - 8.4) / 4, 1.9)
# 5 kg 3 kg
a = (50 - 30) / 8; eq("a", a, 2.5); eq("T", 30 + 3 * a, 37.5); eq("chk", 50 - 37.5, 5 * a)
# table
a = (20 - 10) / 6; eq("a tab", sf(a), 1.67); eq("T tab", sf(20 - 2 * a), 16.7); eq("T exact", 50 / 3, 20 - 2 * a)
# landing
eq("v land", sf(sqrt(2 * 2.5 * 2)), 3.16); eq("v2", 2 * 2.5 * 2, 10); eq("s up", 10 / 20, 0.5); eq("rise", 2 + 0.5, 2.5)
# exam 1
a = (25 - 20) / 6.5; eq("a ex", sf(a), 0.769); eq("a frac", 10 / 13, a); eq("T ex", sf(20 + 4 * a), 23.1)
v2 = 2 * a * 1.2; eq("v2", sf(v2, 4), 1.846); eq("v", sf(sqrt(v2)), 1.36); eq("s", sf(v2 / 10, 3), 0.185)
eq("W//", 4 * 10 * sin(radians(30)), 20)
# car trailer
a = (2200 - 400) / 1200; eq("a car", a, 1.5); eq("T", 150 + 400 * a, 750); eq("chk", 2200 - 250 - 750, 800 * a)
# try
eq("t1", 3000 / 1200, 2.5); eq("t2a", (30 - 10) / 5, 4); eq("t2v", 24, 4 * 6); eq("t3", 600 - 120, 480)
R = 40 * cos(radians(30)); eq("t4 R", sf(R, 4), 34.64); eq("t4 F", sf(0.2 * R, 3), 6.93); eq("t4 a", sf((20 - 0.2 * R) / 4), 3.27)
a = (60 - 40) / 10; eq("t5 a", a, 2); eq("t5 T", 40 + 4 * a, 48)
a = 30 / 8; eq("t6 a", a, 3.75); eq("t6 T", 5 * a, 18.75)
a = (3000 - 800) / 1200; eq("t7 a", sf(a), 1.83); eq("t7 T", 200 + 300 * a, 750)
a = (60 - 20) / 8; eq("t9 a", a, 5); eq("t9 T", 20 + 2 * a, 30); eq("t9 v2", 2 * 5 * 1.6, 16); eq("t9 s", 16 / 20, 0.8); eq("t9 h", 1.6 + 0.8, 2.4)
T = 12 / 0.98; eq("t10 T", sf(T), 12.2); eq("t10 eq", 0.8 * T, 0.3 * (40 - 0.6 * T), 1e-9); eq("t10 coef", 0.8 + 0.18, 0.98)
# quiz
eq("q1", 50 + 5 * 2, 60); eq("q2", g * sin(radians(30)), 5)
a = (30 - 20) / 5; eq("q3 T", 2 * (10 + a), 24)
print("ok")
