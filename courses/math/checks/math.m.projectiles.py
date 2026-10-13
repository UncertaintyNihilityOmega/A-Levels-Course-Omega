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
# ---- v2 additions ----
d = radians
# warm-up
eq("w1", 15 ** 2 / 20, 11.25); a = degrees(asin(0.6)); eq("w2 a", round(a / 2, 1), 18.4); eq("w2 b", round((180 - a) / 2, 1), 71.6); eq("w2 2a", round(a, 2), 36.87)
eq("w3 max", 4 * 20 - 20 ** 2 / 10, 40); eq("w3 sq", -(1 / 10) * (20 - 20) ** 2 + 40, 40)
for x in (3, 11, 27): eq("w3 form", 4 * x - x ** 2 / 10, -(x - 20) ** 2 / 10 + 40)
# proof
for al in (20, 33, 57):
    u = 20; t = 7 / (u * cos(d(al))); x = u * t * cos(d(al)); y = u * t * sin(d(al)) - 5 * t * t
    eq("pr traj", y, x * tan(d(al)) - 10 * x ** 2 / (2 * u ** 2 * cos(d(al)) ** 2), 1e-9)
    eq("pr range", 2 * u ** 2 * cos(d(al)) ** 2 * tan(d(al)) / 10, u ** 2 * sin(d(2 * al)) / 10, 1e-9)
eq("pr 30", sf(400 * sin(d(60)) / 10), 34.6); eq("pr 60", sf(400 * sin(d(120)) / 10), 34.6); eq("pr 45", 400 * sin(d(90)) / 10, 40)
# spot the error
eq("se sin", 25 * 0.6, 15); eq("se cos", 25 * 0.8, 20); assert abs(0.6 ** 2 + 0.8 ** 2 - 1) < 1e-12
eq("se wrong H", 20 ** 2 / 20, 20); eq("se wrong T", 2 * 20 / 10, 4); eq("se H", 15 ** 2 / 20, 11.25); eq("se T", 2 * 15 / 10, 3)
# exam practice
eq("q1 t", sqrt(2 * 20 / 10), 2); eq("q1 x", 8 * 2, 16); eq("q1 vy", 10 * 2, 20); eq("q1 v", sf(sqrt(8 ** 2 + 20 ** 2)), 21.5)
x = 2 * 3 / (2 + 4) * 0 + 2; eq("q2", 2 * x, 4 * (3 - x))
eq("q3 vy", 26 * 5 / 13, 10); eq("q3 H", 10 ** 2 / 20, 5)
t = 30 / (20 * cos(d(40))); y = 20 * sin(d(40)) * t - 5 * t * t
eq("q4 vx", round(20 * cos(d(40)), 2), 15.32); eq("q4 t", round(t, 3), 1.958); eq("q4 a", round(20 * sin(d(40)) * t, 2), 25.17); eq("q4 b", round(5 * t * t, 2), 19.17); eq("q4 y", round(y, 2), 6.00)
assert y > 2
RC = (160 * 2.5 + 640 * 5) / 4; eq("q5 RC", RC, 900); eq("q5 RA", 800 - RC, -100); eq("q5 x", 4 + 160 * 1.5 / 640, 4.375); eq("q5 mom", 640 * (4.375 - 4), 160 * 1.5)
T = 120 / (3 * sin(d(40))); eq("q6 T", sf(T), 62.2); X = T * cos(d(40)); Y = 80 - T * sin(d(40)); eq("q6 X", sf(X), 47.7); eq("q6 Y", Y, 40); eq("q6 R", sf(sqrt(X ** 2 + Y ** 2)), 62.2)
eq("q6 mom", T * sin(d(40)) * 3, 120)
# q7: 9t^2 - 24t + 13 = 0
eq("q7 mult", 11.25 * 0.8, 9); eq("q7 mult2", 30 * 0.8, 24); eq("q7 mult3", 16.25 * 0.8, 13); eq("q7 disc", 24 ** 2 - 4 * 9 * 13, 108)
eq("q7 coeff", 10 * 30 ** 2 / (2 * 20 ** 2), 11.25); eq("q7 const", 11.25 - 5, 6.25 * 1); eq("q7 const2", 11.25 + 5, 16.25)
t1 = (24 + sqrt(108)) / 18; t2 = (24 - sqrt(108)) / 18
eq("q7 t1", round(t1, 3), 1.911); eq("q7 t2", round(t2, 3), 0.756); eq("q7 a1", round(degrees(atan(t1)), 1), 62.4); eq("q7 a2", round(degrees(atan(t2)), 1), 37.1)
for tt in (t1, t2): eq("q7 check", 30 * tt - 11.25 * (1 + tt ** 2), 5, 1e-9)
eq("q7 check1911", round(30 * 1.911 - 11.25 * (1 + 1.911 ** 2), 2), 5.00, 0.01)
# stretch
for al in (25, 40, 55):
    u = 17; H = u ** 2 * sin(d(al)) ** 2 / 20; R = u ** 2 * sin(d(2 * al)) / 10; eq("s1 ratio", tan(d(al)), 4 * H / R, 1e-9)
eq("s1 a", round(degrees(atan(4 / 3)), 1), 53.1); eq("s1 u2", 20 * 20 / 0.64, 625); eq("s1 R", 625 * 0.96 / 10, 60); eq("s1 sin2a", 2 * 0.8 * 0.6, 0.96)
eq("s2 vx", 25 * 0.8, 20); eq("s2 vy", 25 * 0.6, 15); eq("s2 t", 40 / 20, 2); eq("s2 dart", 15 * 2 - 5 * 4, 10); eq("s2 target", 30 - 5 * 4, 10)

print("ok")
