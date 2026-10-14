# checks/phys.circular.py: recomputes every number in the Motion in a circle chapter.
from math import isclose, sqrt, pi, sin, cos, tan, asin, radians, degrees

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81
R_E = 6.37e6

# Warm-up
eq("warm a", 3600 / 1200, 3.0)
eq("warm comp", sf(50 * cos(radians(30)), 2), 43)

# Radians
eq("150 deg", sf(150 * pi / 180), 2.62)
eq("0.75 rad", sf(0.75 * 180 / pi), 43.0)
theta = 2.5 * 2 * pi
eq("wheel theta", sf(theta), 15.7)
eq("wheel s", sf(0.34 * theta, 2), 5.3)

# Earth rotation
T = 24 * 3600
eq("T day", T, 8.64e4)
w = 2 * pi / T
eq("w Earth", sf(w), 7.27e-5)
eq("v equator", sf(R_E * w), 463)

# Hard disk
f = 7200 / 60
eq("f disk", f, 120)
wd = 2 * pi * f
eq("w disk", sf(wd), 754)
eq("v disk", sf(0.040 * wd, 2), 30)

# Earth round Sun
Ty = 365.25 * 86400
eq("T year", sf(Ty, 4), 3.156e7)
ws = 2 * pi / Ty
eq("w Sun", sf(ws), 1.99e-7)
eq("a Sun", sf(1.50e11 * ws**2), 5.95e-3)

# Car on bend
eq("F bend", 1200 * 15**2 / 50, 5400)
eq("v max bend", sf(sqrt(7200 * 50 / 1200), 2), 17)
eq("plot k", 1200 / 50, 24)
eq("plot pt", 24 * 15**2, 5400)
eq("plot ymax", 24 * 25**2, 15000)
eq("W car", sf(1200 * g, 3), 11800)
eq("W kN", sf(1200 * g / 1000, 3), 11.8)
eq("F kN", 5400 / 1000, 5.4)

# String on table
w2 = 2 * pi * 1.5
eq("w table", sf(w2, 3), 9.42)
eq("T table", sf(0.25 * 0.80 * w2**2, 2), 18)
eq("T table x2", sf(4 * 0.25 * 0.80 * w2**2, 2), 71)

# Conical pendulum
th = radians(30)
Tn = 0.20 * g / cos(th)
eq("T cone", sf(Tn, 2), 2.3)
r = 0.80 * sin(th)
eq("r cone", r, 0.40)
w3sq = g * tan(th) / r
eq("w^2 cone", sf(w3sq), 14.2)
w3 = sqrt(w3sq)
eq("w cone", sf(w3), 3.76)
eq("v cone", sf(r * w3, 2), 1.5)
eq("period cone", sf(2 * pi / w3, 2), 1.7)

# Vertical circle
m, r = 0.20, 0.60
Tb = m * g + m * 6.0**2 / r
eq("Tb", sf(Tb, 2), 14)
vt2 = 6.0**2 - 4 * g * r
eq("vt2", sf(vt2, 3), 12.5)
eq("vt", sf(sqrt(vt2), 2), 3.5)
Tt = m * vt2 / r - m * g
eq("Tt", sf(Tt, 2), 2.2)
assert 4.0**2 - 4 * g * r < 0
eq("min bottom", sf(sqrt(5 * g * r), 2), 5.4)

# Hump-back bridge
N = 900 * g - 900 * 15**2 / 40
eq("bridge mg", 900 * g, 8829)
eq("bridge mv2/r", 900 * 15**2 / 40, 5062.5)
eq("bridge N", sf(N, 2), 3.8e3)
eq("bridge vmax", sf(sqrt(g * 40), 2), 20)
eq("bridge mg kN", sf(900 * g / 1000, 2), 8.8)
eq("bridge N kN", sf(N / 1000, 2), 3.8)

# Electron in a magnetic field
eq("electron r", sf(9.11e-31 * 2.0e7 / (1.0e-3 * 1.60e-19), 2), 0.11)

# Spot the error
eq("spot wrong", sf(0.15 * 33, 2), 5.0)
w4 = 33 * 2 * pi / 60
eq("spot w", sf(w4, 3), 3.46)
eq("spot v", sf(0.15 * w4, 2), 0.52)

# Start easy
eq("e1 72", sf(72 * pi / 180, 3), 1.26)
eq("e1 3.5", sf(3.5 * 180 / pi, 3), 201)
th5 = 40 * pi / 180
eq("e2 theta", sf(th5, 3), 0.698)
eq("e2 s", sf(0.18 * th5, 2), 0.13)
w6 = 2 * pi / 60
eq("e3 w", sf(w6, 3), 0.105)
eq("e3 v", sf(0.12 * w6, 2), 1.3e-2)
r7 = R_E * cos(radians(52))
eq("e4 r", sf(r7, 3), 3.92e6)
eq("e4 v", sf(r7 * w, 3), 285)
eq("e5 a", 20**2 / 80, 5.0)
eq("e5 F", 1000 * 20**2 / 80, 5.0e3)
w8 = 2 * pi * 2.0
eq("e6 w", sf(w8, 3), 12.6)
eq("e6 T", sf(0.30 * 0.90 * w8**2, 2), 43)
eq("e8 v", (20 / 10)**2, 4)
eq("e8 r", 2, 2)

# Exam practice
w9 = 25 * 2 * pi / 4.0
eq("Q2 w", sf(w9, 2), 39)
eq("Q2 v", sf(0.30 * w9, 2), 12)
v4 = sqrt(7000 * 80 / 1400)
eq("Q4 v2", 7000 * 80 / 1400, 400)
eq("Q4 v", v4, 20)
eq("Q4 wet", sf(20 / sqrt(2), 2), 14)
eq("Q5 sin", 0.30 / 0.50, 0.60)
eq("Q5 theta", sf(degrees(asin(0.6)), 2), 37)
eq("Q5 cos", sqrt(1 - 0.6**2), 0.80)
T5 = 0.15 * g / 0.80
eq("Q5 T", sf(T5, 2), 1.8)
w5sq = T5 * 0.6 / (0.15 * 0.30)
eq("Q5 w2", sf(w5sq, 3), 24.5)
w5 = sqrt(w5sq)
eq("Q5 w", sf(w5, 3), 4.95)
eq("Q5 period", sf(2 * pi / w5, 2), 1.3)
m6, r6 = 0.50, 0.90
eq("Q6 Tt", sf(m6 * 3.5**2 / r6 - m6 * g, 2), 1.9)
vb2 = 3.5**2 + 4 * g * r6
eq("Q6 vb2", sf(vb2, 3), 47.6)
eq("Q6 vb", sf(sqrt(vb2), 2), 6.9)
eq("Q6 Tb", sf(m6 * g + m6 * vb2 / r6, 2), 31)
w7 = 2 * pi * 0.50
eq("Q7 w", w7, pi)
eq("Q7 N", sf(60 * 2.5 * w7**2, 2), 1.5e3)
eq("Q7 F", sf(60 * g, 2), 5.9e2)
eq("Q7 x4", (2.0)**2, 4)

# Stretch
eq("bank v2", sf(120 * g * tan(radians(15)), 3), 315)
eq("bank v", sf(sqrt(120 * g * tan(radians(15))), 2), 18)
eq("loop h", 2.5 * 0.40, 1.0)
eq("loop h energy", 2 * 0.40 + 0.40 / 2, 1.0)
eq("loop v", sf(sqrt(2 * g * 1.0), 2), 4.4)

# Figure labels and quiz
eq("quiz factor", (20 / 10)**2, 4)
eq("rad deg", sf(180 / pi, 3), 57.3)
eq("quiz bridge", sf(900 * g - 900 * 15**2 / 40, 2), 3.8e3)

print("ok")
