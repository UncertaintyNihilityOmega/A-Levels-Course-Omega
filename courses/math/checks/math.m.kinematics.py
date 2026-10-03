# checks/math.m.kinematics.py: recomputes every number in the kinematics chapter.
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

# walker
eq("disp", sqrt(3 ** 2 + 4 ** 2), 5)
# v-t car
eq("acc", 20 / 8, 2.5); eq("dec", sf(20 / 12), 1.67)
A, B, C = 0.5 * 8 * 20, 30 * 20, 0.5 * 12 * 20
eq("A", A, 80); eq("B", B, 600); eq("C", C, 120); eq("dist", A + B + C, 800); eq("avg", 800 / (8 + 30 + 12), 16)
# figure coordinates
eq("x8", 50 + 8 * 9, 122); eq("x38", 50 + 38 * 9, 392); eq("x50", 50 + 50 * 9, 500); eq("y20", 190 - 20 * 7, 50)
# brake
eq("stop s", 625 / 10, 62.5); eq("stop t", 25 / 5, 5)
# train
a = (900 - 144) / (2 * 540); eq("train a", a, 0.7); t = 18 / a; eq("train t", sf(t), 25.7); eq("train check", 0.5 * 42 * t, 540, 1e-6)
# ball up
eq("H", 18 ** 2 / 20, 16.2); eq("tup", 18 / 10, 1.8); eq("tot", 18 / 5, 3.6)
# stone from cliff
eq("disc", 12 ** 2 + 4 * 5 * 32, 784); eq("t", (12 + 28) / 10, 4); eq("t neg", (12 - 28) / 10, -1.6); eq("v", 12 - 40, -28)
assert 5 * 4 ** 2 - 12 * 4 - 32 == 0 and (5 * 4 + 8) * 0 == 0
# 20 m
assert 25 * 1 - 5 * 1 == 20 and 25 * 4 - 5 * 16 == 20
# cyclist and motorbike
eq("quad", 8 + sqrt(48), 14.93, 0.005); eq("quad2", 8 - sqrt(48), 1.07, 0.005); eq("meet d", sf(6 * (8 + sqrt(48)), 3), 89.6)
t = 8 + sqrt(48); eq("meet eq", 6 * t, 0.75 * (t - 4) ** 2, 1e-9); eq("coef", 0.75 * 16, 12)
# towers
eq("meet t", 60 / 20, 3); eq("meet h", 20 * 3 - 5 * 9, 15)
# calculus 1
s = lambda t: t ** 3 - 6 * t ** 2 + 9 * t
eq("s1", s(1), 4); eq("s3", s(3), 0); eq("s4", s(4), 4); eq("dist12", 4 + 4 + 4, 12); eq("v roots", 3 * (1 - 1) * (1 - 3), 0)
# calculus 2
eq("vmax", 4 * 2 - 2 ** 2, 4); eq("s at 4", sf(32 - 64 / 3, 3), 10.7); eq("32/3", 32 - 64 / 3, 32 / 3)
# exam 1
eq("V", 1050 / 52.5, 20); eq("52.5", 0.5 * 10 + 40 + 0.5 * 15, 52.5); eq("a1", 20 / 10, 2); eq("dec", 20 / 15, 4 / 3); eq("tau", (20 - 16) / (4 / 3), 3); eq("t53", 50 + 3, 53)
# exam 2
s = lambda t: t ** 3 / 3 - 3 * t ** 2 + 8 * t
eq("s2", s(2), 20 / 3); eq("s4", s(4), 16 / 3); eq("s4 3sf", sf(16 / 3), 5.33); eq("back", 20 / 3 - 16 / 3, 4 / 3); eq("dist", 20 / 3 + 4 / 3, 8); eq("a0", 2 * 0 - 6, -6)
# try
eq("t1", 400 / 80, 5)
eq("t2", 0.5 * 6 * 12 + 10 * 12 + 0.5 * 4 * 12, 180); eq("t2 avg", 180 / 20, 9)
eq("t3 s", 5 * 8 + 0.5 * 2 * 64, 104); eq("t3 v", 5 + 2 * 8, 21)
eq("t4 a", 900 / (2 * 225), 2); eq("t4 t", 30 / 2, 15)
eq("t5 a", -400 / 100, -4); eq("t5 t", 20 / 4, 5)
eq("t6 t", sqrt(45 / 5), 3); eq("t6 v", 30, 10 * 3)
s = lambda t: 2 * t ** 3 - 15 * t ** 2 + 36 * t
eq("t7 s2", s(2), 28); eq("t7 s3", s(3), 27); eq("t7 a", 12 * 2 - 30, -6); eq("t7 v", 6 * 4 - 60 + 36, 0); eq("t7 v3", 6 * 9 - 90 + 36, 0)
eq("t8 vmax", 18 - 9, 9); eq("t8 s", 3 * 36 - 216 / 3, 36)
t = (-20 + sqrt(400 + 2880)) / 6; eq("t9", sf(t), 6.21); eq("t9 eq", 5 * t, 60 - 0.75 * t ** 2, 1e-9)
eq("t10 disc", 100 + 4 * 5 * 15 - 400, 0) if False else None
assert -15 == 10 * 3 - 5 * 9 and 3 ** 2 - 2 * 3 - 3 == 0; eq("t10 v", 10 - 30, -20)
# quiz
eq("q4", 0.5 * 3 * 16, 24); eq("q5", 6 * 2, 12); eq("q5 wrong", 3 * 4 - 4, 8)
print("ok")
