# checks/phys.kinematics.py: recomputes every number in the Kinematics chapter.
from math import isclose, sqrt, pi, cos, sin, atan, radians, degrees

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("w1 x", sf(20 * cos(radians(30))), 17.3)
eq("w1 y", sf(20 * sin(radians(30))), 10.0)
eq("w2", 72e3 / 3600, 20)

# Describing motion
eq("lap speed", 400 / 50, 8.0)
v100 = 100e3 / 3600
eq("100 km/h", sf(v100, 3), 27.8)
eq("a car", sf(v100 / 8.0, 3), 3.47)
eq("a car 2sf", sf(v100 / 8.0, 2), 3.5)
eq("wall a", (-6.0 - 8.0) / 0.020, -700)
eq("wall about 70g", round(700 / g), 71)

# s-t example: s = 5t^2
eq("s(2)", 5 * 2**2, 20)
eq("tangent through (1,0)", 20 * 1 - 20, 0)
eq("tangent through (3,40)", 20 * 3 - 20, 40)
eq("tangent grad", (40 - 0) / (3.0 - 1.0), 20)
eq("ds/dt at 2", 10 * 2, 20)

# Trolley v-t
A1 = 0.5 * 2 * 4
A2 = (5 - 2) * 4
A3 = 0.5 * (7 - 5) * 4
A4 = -0.5 * (8 - 7) * 2
A5 = -(10 - 8) * 2
eq("A1", A1, 4); eq("A2", A2, 12); eq("A3", A3, 4); eq("A4", A4, -1); eq("A5", A5, -4)
eq("a 5-8", (-2 - 4) / (8 - 5), -2.0)
eq("zero crossing", 4 - 2 * (7 - 5), 0)
eq("v at 8", 4 - 2 * (8 - 5), -2)
eq("displacement", A1 + A2 + A3 + A4 + A5, 15)
eq("distance", abs(A1) + abs(A2) + abs(A3) + abs(A4) + abs(A5), 25)
eq("avg v", 15 / 10, 1.5)
eq("avg speed", 25 / 10, 2.5)
eq("a-t area", 2 * 2, 4)
# figure geometry: 40 px per s, 25 px per m/s, origin (70,130)
eq("fig t=2", 70 + 40 * 2, 150)
eq("fig t=5", 70 + 40 * 5, 270)
eq("fig t=7", 70 + 40 * 7, 350)
eq("fig t=8", 70 + 40 * 8, 390)
eq("fig t=10", 70 + 40 * 10, 470)
eq("fig v=4", 130 - 25 * 4, 30)
eq("fig v=-2", 130 + 25 * 2, 180)

# Equations
a, t = 2.5, 8.0
eq("v", a * t, 20)
eq("s", 0.5 * a * t**2, 80)
a2 = -(20**2) / (2 * 40)
eq("brake a", a2, -5.0)
eq("brake t", 2 * 40 / 20, 4.0)

# Stopping distance
eq("think 15", 15 * 0.70, 10.5)
eq("brake 15", 15**2 / (2 * 5.0), 22.5)
eq("stop 15", 15 * 0.70 + 15**2 / (2 * 5.0), 33)
eq("think 30", 30 * 0.70, 21)
eq("brake 30", 30**2 / (2 * 5.0), 90)
eq("stop 30", 21 + 90, 111)
eq("brake ratio", (30**2) / (15**2), 4)

# Cliff
h = 15**2 / (2 * g)
eq("max h", sf(h, 3), 11.5)
disc = sqrt(15**2 + 4 * (g / 2) * 20)
eq("sqrt disc", sf(disc, 4), 24.85)
t_ = (15 + disc) / g
eq("cliff t", sf(t_, 3), 4.06)
eq("neg root", sf((15 - disc) / g, 3), -1.00)
eq("v impact", sf(sqrt(15**2 + 2 * g * 20), 3), 24.8)
eq("v check", sf(15 - g * t_, 3), -24.8)
eq("v^2", sf(15**2 + 2 * g * 20, 4), 617.4)
eq("2g", 2 * g, 19.62)
eq("g/2", g / 2, 4.905)

# Free fall figure
eq("top time", sf(15 / g, 3), 1.53)

# g experiment
sh = [0.447, 0.632, 0.775, 0.894, 1.000, 1.095]
import math
for hh, s_, tm in zip([0.20, 0.40, 0.60, 0.80, 1.00, 1.20], sh, [214, 298, 362, 416, 464, 507]):
    eq(f"sqrt h {hh}", round(math.sqrt(hh), 3), s_, 1e-9)
    # data come from t = sqrt(2h/g) + 12 ms, rounded to the nearest ms
    eq(f"t {hh}", round((math.sqrt(2 * hh / g) + 0.012) * 1000), tm, 1e-9)
grad = (0.507 - 0.214) / (1.095 - 0.447)
eq("grad", sf(grad, 3), 0.452)
eq("g exp", sf(2 / grad**2, 3), 9.78)
eq("intercept", sf(0.214 - 0.452 * 0.447, 2), 0.012)

# Parcel
tp = sqrt(2 * 500 / g)
eq("parcel t", sf(tp, 3), 10.1)
eq("parcel x", sf(60 * tp, 3), 606)
vy = g * tp
eq("parcel vy", sf(vy, 3), 99.0)
eq("parcel v", sf(sqrt(60**2 + vy**2), 3), 116)
eq("parcel angle", sf(degrees(atan(vy / 60)), 3), 58.8)

# Kick
ux, uy = 25 * cos(radians(35)), 25 * sin(radians(35))
eq("ux", sf(ux, 3), 20.5)
eq("uy", sf(uy, 3), 14.3)
T = 2 * uy / g
eq("T", sf(T, 3), 2.92)
eq("H", sf(uy**2 / (2 * g), 3), 10.5)
eq("R", sf(ux * T, 3), 59.9)
eq("half T", sf(T / 2, 3), 1.46)
eq("top 14.34", sf(14.34 / 4.905, 3), 2.92)

# Spot the error
eq("rise time", sf(12 / g, 2), 1.2)
tw = (12 + sqrt(144 + 4 * 4.905 * 30)) / (2 * 4.905)
eq("wrong t", sf((-12 + sqrt(144 + 4 * 4.905 * 30)) / (2 * 4.905), 3), 1.54)
eq("right t", sf(tw, 3), 3.98)
eq("disc", sf(144 + 4 * 4.905 * 30, 4), 732.6)
eq("588.6", 4 * 4.905 * 30, 588.6, 1e-9)

# Try easy
eq("t1", 90 / 15, 6.0)
eq("t2", (20 - 8.0) / 6.0, 2.0)
eq("t3 a", (0 - 30) / 20, -1.5)
eq("t3 s", 0.5 * 30 * 20, 300)
eq("t4", sf(0.5 * g * 2.4**2, 2), 28)
eq("t5", 12 * 5.0, 60)
eq("t6", sf(400 / (2 * g), 3), 20.4)
eq("t7 x", 1.5 * 0.40, 0.60)
eq("t7 vy", sf(g * 0.40, 2), 3.9)
eq("t8", 100 / 20, 5.0)
eq("t10", sf(40 * cos(radians(30)), 3), 34.6)

# Exam practice
eq("train tri", 0.5 * 60 * 30, 900)
eq("train rect", 30 * 120, 3600)
eq("train total", 900 + 3600, 4500)
eq("brake 25", sf(625 / 12, 2), 52)
eq("ball 18 h", sf(18**2 / (2 * g), 3), 16.5)
eq("ball 18 t", sf(18 / 4.905, 3), 3.67)
tt = sqrt(2 * 0.95 / g)
eq("table t", sf(tt, 3), 0.440)
eq("table x", sf(1.8 * 0.440, 2), 0.79)
eq("table vy", sf(g * 0.440, 3), 4.32)
eq("table v", sf(sqrt(1.8**2 + 4.32**2), 2), 4.7)
# Platform
uy2 = 20 * sin(radians(40))
eq("platform uy", sf(uy2, 3), 12.9)
eq("platform uy 4", sf(uy2, 4), 12.86)
d2 = sqrt(12.86**2 - 4 * 4.905 * 3.0)
tl, tu = (12.86 - d2) / 9.81, (12.86 + d2) / 9.81
eq("t early", sf(tl, 2), 0.26)
eq("t late", sf(tu, 3), 2.36)
eq("x plat", sf(20 * cos(radians(40)) * 2.362, 2), 36)
eq("ux plat", sf(20 * cos(radians(40)), 3), 15.3)
eq("vy at top", sf(12.86 / g, 3), 1.31)
eq("vy end", sf(12.856 - g * 2.362, 3), -10.3)
# Stretch 1
eq("meet t", 80 / 25, 3.2)
fallen = 0.5 * g * 3.2**2
eq("fallen", sf(fallen, 3), 50.2)
eq("meet h", sf(80 - fallen, 3), 29.8)
eq("B h", sf(25 * 3.2 - 4.905 * 3.2**2, 3), 29.8)
# Stretch 2
eq("Rmax", sf(25**2 / g, 3), 63.7)

# Quiz
eq("quiz horiz", sf(20 * cos(radians(30)), 3), 17.3)
eq("quiz vertical", 20 * sin(radians(30)), 10.0, 1e-9)
eq("quiz 4d", (20 / 10)**2, 4)

print("ok")
