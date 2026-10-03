# checks/math.m.projectiles.py: recomputes every number in the projectiles and moments chapter.
from math import isclose, sqrt, sin, cos, tan, atan, asin, degrees, radians

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

g = 10
# plot: u=20, 45 deg
a = radians(45); u = 20
eq("range", u * u * sin(2 * a) / g, 40); eq("H", u * u * sin(a) ** 2 / (2 * g), 10)
eq("traj", tan(a) - g / (2 * u * u * cos(a) ** 2) * 1, 1 - 1 / 40, 1e-12)
# e1
vx, vy = 20 * cos(radians(30)), 20 * sin(radians(30)); eq("vx", sf(vx, 4), 17.32); eq("vy", vy, 10); eq("T", 2 * vy / g, 2); eq("H", vy ** 2 / (2 * g), 5); eq("R", sf(vx * 2), 34.6)
# cliff
eq("t", sqrt(45 / 5), 3); eq("x", 12 * 3, 36); eq("speed", sf(sqrt(1044)), 32.3); eq("th", sf(degrees(atan(30 / 12)), 3), 68.2)
# tower
t = 1 + sqrt(7); eq("t", sf(t), 3.65); eq("x", sf(vx * t), 63.1); vyl = 10 - 10 * t; eq("vy", sf(vyl, 4), -26.46); eq("v", sf(sqrt(vx ** 2 + vyl ** 2)), 31.6)
eq("v energy", sf(sqrt(400 + 2 * 10 * 30)), 31.6); eq("quad", t * t - 2 * t - 6, 0, 1e-9)
# wall
eq("y", 15 * 1 - 5, 10); eq("traj", 20 * 0.75 - 10 * 400 / (2 * 25 ** 2 * 0.64), 10); eq("cos2", 0.8 ** 2, 0.64)
# moments
eq("see", 300 * 2 / 400, 1.5)
Rc = (200 * 3 + 50 * 6) / 4; eq("Rc", Rc, 225); eq("Ra", 250 - Rc, 25); eq("chk", (250 - Rc) * 4 + 50 * 2, 200)
T = 60 / (sin(radians(30)) * 2); eq("T", T, 60); eq("X", sf(T * cos(radians(30)), 3), 52.0); eq("Y", 60 - T * sin(radians(30)), 30)
eq("hinge", sf(sqrt((T * cos(radians(30))) ** 2 + 30 ** 2)), 60.0, 1e-9)
eq("tip", 200 * 1.5 / 400, 0.75); eq("near B", 1 - 0.75, 0.25)
# exam 1
eq("vx", 26 * 12 / 13, 24); eq("vy", 26 * 5 / 13, 10); eq("H", 100 / 20, 5); eq("R", 24 * 2, 48)
eq("speed", sf(sqrt(24 ** 2 + 5 ** 2)), 24.5); eq("ang", sf(degrees(atan(5 / 24)), 3), 11.8)
# exam 2
Rc = (120 * 2 + 80 * 4) / 3; eq("Rc", sf(Rc, 4), 186.7); eq("Ra", sf(200 - Rc, 3), 13.3); eq("W", 120 * 1 / 1, 120)
# try
eq("t1a", 40 * cos(radians(60)), 20); eq("t1b", sf(40 * sin(radians(60))), 34.6)
vx, vy = 30 * cos(radians(30)), 15; eq("t2 vx", sf(vx, 4), 25.98); eq("T", 2 * 15 / 10, 3); eq("H", 225 / 20, 11.25); eq("R", sf(vx * 3), 77.9)
eq("t3", sqrt(20 / 5), 2); eq("t3 x", 30, 15 * 2)
eq("t4", 400 / 10, 40); eq("t5", 30 - 900 / 40, 7.5)
s = asin(0.75); eq("t6 a", sf(degrees(s) / 2 * 1, 3), 24.3); eq("t6 b", sf(90 - degrees(s) / 2), 65.7); eq("2a", sf(degrees(s), 3), 48.6); eq("2a2", sf(180 - degrees(s), 4), 131.4)
eq("t7", 250 * 1.8 / 300, 1.5)
eq("t8 T", 40 * 1.5 / 2, 30); eq("t8 Y", 40 - 30, 10)
t = (12 + sqrt(544)) / 10; eq("t9 t", sf(t), 3.53); eq("t9 x", sf(9 * t), 31.8); eq("t9 v", sqrt(15 ** 2 + 2 * 10 * 20), 25); eq("disc", 144 + 400, 544); eq("quad", 5 * t * t - 12 * t - 20, 0, 1e-9)
eq("t10", sf(560 / 3, 3), 187)
eq("q4", 20 * 0.5, 10); eq("q5", 3 * 2 / 4, 1.5)
print("ok")
