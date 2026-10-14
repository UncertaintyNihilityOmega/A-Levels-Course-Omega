# checks/phys.forces.py: recomputes every number in the Forces, density and pressure chapter.
from math import isclose, sqrt, sin, cos, tan, radians, atan2, degrees

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81
s = lambda d: sin(radians(d))
c = lambda d: cos(radians(d))

# Warm-up
eq("warm W", sf(2.5 * g), 24.5)
eq("warm hor", sf(50 * c(30)), 43.3)
eq("warm vert", sf(50 * s(30)), 25.0)
eq("warm a", 12 / 3.0, 4.0)

# Stability figure: centre of gravity positions relative to pivot (block 60 x 100)
for ang, want_x, want_y in [(15, 294.0, 143.9), (40, 519.2, 142.4)]:
    px = 310 if ang == 15 else 510
    cx = px + (-30 * c(ang) + 50 * s(ang))
    cy = 200 + (-30 * s(ang) - 50 * c(ang))
    eq(f"cg x {ang}", round(cx, 1), want_x, 0.11)
    eq(f"cg y {ang}", round(cy, 1), want_y, 0.11)
eq("tilt 15 inside", float(294.0 < 310), 1.0)
eq("tilt 40 outside", float(519.2 > 510), 1.0)

# Moment of a force
eq("moment perp", 80 * 0.25, 20)
eq("moment 60", sf(80 * 0.25 * s(60)), 17.3)
eq("component", sf(80 * s(60), 3), 69.3)

# Spanner figure geometry: pivot (70,190), A (270,190), force at 60 deg
d_perp = 200 * s(60)
eq("spanner dperp", round(d_perp, 1), 173.2, 0.05)
eq("foot x", 270 - 100 * c(60), 220)
eq("foot y", round(190 - 100 * s(60), 1), 103.4, 0.05)

# Couple
eq("steering", 12 * 0.36, 4.32, 1e-9)
eq("steering 2sf", round(12 * 0.36, 1), 4.3, 1e-9)
eq("steering centre", 12 * 0.18 + 12 * 0.18, 4.32)

# Beam on two supports
RB = (200 * 2.0 + 500 * 1.0) / 4.0
eq("RB", RB, 225)
eq("RA", 700 - RB, 475)
eq("RA check", (200 * 2.0 + 500 * 3.0) / 4.0, 475)
eq("RB moment rhs", 200 * 2.0 + 500 * 1.0, 900)
eq("RA moment rhs", 200 * 2.0 + 500 * 3.0, 1900)

# Hinged beam
T = (100 * 1.0 + 60 * 2.0) / (2.0 * s(30))
eq("hinged rhs", 100 * 1.0 + 60 * 2.0, 220)
eq("hinged T", T, 220, 1e-9)
H = T * c(30)
V = 160 - T * s(30)
eq("hinged H", round(H, 1), 190.5, 0.05)
eq("hinged H 3sf", sf(H, 3), 191)
eq("hinged Tvert", T * s(30), 110)
eq("hinged V", V, 50)
eq("hinged mag", sf(sqrt(H**2 + V**2), 3), 197)
eq("hinged angle", sf(degrees(atan2(V, H)), 3), 14.7)
# figure arrows at 0.5 px per N
eq("figure T arrow", round(110 * c(30), 1), 95.3, 0.05)
eq("figure T arrow y", round(110 * s(30), 1), 55.0, 0.05)
eq("figure H arrow", round(0.5 * H, 1), 95.3, 0.05)
eq("figure V arrow", 0.5 * V, 25)

# Forearm
eq("forearm load", 5.0 * g, 49.05)
eq("forearm F", sf(5.0 * g * 0.35 / 0.040, 3), 429)
eq("forearm ratio", round(5.0 * g * 0.35 / 0.040 / (5.0 * g), 1), 8.8, 0.06)

# Picture on strings
Tp = 12 / (2 * s(40))
eq("picture T", sf(Tp, 3), 9.33)
eq("triangle t px", round(Tp * 10, 1), 93.3, 0.05)
eq("triangle dx", round(Tp * 10 * c(40), 1), 71.5, 0.05)
eq("triangle dy", round(Tp * 10 * s(40), 1), 60.0, 0.05)
eq("string pic x", round(80 / tan(radians(40)), 1), 95.3, 0.05)
eq("string tension arrow", round(Tp * 5 * c(40), 1), 35.8, 0.05)

# Ball on slope
eq("ball T", 8.0 * s(30), 4.0)
eq("ball N", sf(8.0 * c(30), 2), 6.9)

# Stiletto
eq("stiletto W", 60 * g, 588.6)
eq("stiletto heel", sf(588.6 / 1.0e-4, 2), 5.9e6)
eq("stiletto flat", sf(588.6 / 0.015, 2), 3.9e4)
eq("stiletto ratio", 150 / 1.0, 150)

# Hydrostatic: sea
dp = 1030 * g * 30
eq("sea dp", sf(dp, 3), 3.03e5)
eq("sea total", sf(sf(dp, 3) + 1.01e5, 3), 4.04e5)
eq("sea F", sf(4.04e5 * 0.20, 3), 8.08e4)
eq("sea net F", sf(3.03e5 * 0.20, 3), 6.06e4)

# Floating cube
Wc = 700 * 0.10**3 * g
eq("cube W", sf(Wc, 3), 6.87)
Vs = Wc / (1000 * g)
eq("cube Vs", sf(Vs, 2), 7.0e-4)
eq("cube depth", sf(Vs / 0.10**2, 2), 0.070)
eq("cube fraction", 700 / 1000 * 0.10, 0.070)

# Steel in water
V = 2.0 / 7800
eq("steel V", sf(V, 3), 2.56e-4)
F = 1000 * g * V
eq("steel upthrust", sf(F, 3), 2.52)
eq("steel weight", sf(2.0 * g, 3), 19.6)
eq("steel reading", sf(2.0 * g - F, 3), 17.1)

# Spot the error
eq("sote wrong", 50 * 0.30, 15)
eq("sote correct", sf(50 * 0.30 * s(40), 2), 9.6)

# Start easy
eq("e1", 20 * 0.35, 7.0)
eq("e2", 30 * 1.8 / 45, 1.2)
eq("e3", 15 * 0.30, 4.5)
eq("e4", sf(1.0 * 0.20 / 0.30, 2), 0.67)
eq("e5", 468 / 60, 7.8)
eq("e5 V", 5.0 * 4.0 * 3.0, 60)
eq("e6 W", 80 * g, 784.8)
eq("e6 boots", sf(784.8 / 0.040, 2), 2.0e4)
eq("e6 snowshoes", sf(784.8 / 0.50, 2), 1.6e3)
eq("e7 rho g h", sf(1000 * g * 12, 3), 1.18e5)
eq("e7 total", sf(sf(1000 * g * 12, 3) + 1.01e5, 3), 2.19e5)
eq("e8", sf(13600 * g * 0.12, 3), 1.60e4)
eq("e9", sf(1000 * g * 0.0030, 3), 29.4)
eq("e10", 8.0 * s(30), 4.0)

# Exam practice
RL = (300 * 3.0 + 750 * 4.0) / 6.0
eq("deck RL", RL, 650)
eq("deck RR", 1050 - RL, 400)
Wt = 80
k = Wt / s(75)
eq("traffic T1", sf(k * s(45), 3), 58.6)
eq("traffic T2", sf(k * s(60), 3), 71.7)
eq("traffic horizontal", round(k * s(45) * c(30), 3), round(k * s(60) * c(45), 3), 1e-3)
eq("traffic angles", 75 + 45 + 60, 180)
eq("cylinder", 0.60 * 1000, 600)
eq("cylinder frac", 600 / 800, 0.75)
# hinged beam exam
rhs = 90 * 1.5 + 120 * 2.0
eq("beam rhs", rhs, 375)
T = rhs / (3.0 * s(35))
eq("beam T", sf(T, 3), 218)
eq("beam H", sf(T * c(35), 3), 179)
eq("beam Tvert", sf(T * s(35), 3), 125)
eq("beam V", sf(210 - T * s(35), 3), 85.0)
# cube in water
dp = 1000 * g * 0.050
eq("cube dp", sf(dp, 2), 4.9e2)
A = 0.050**2
eq("cube area", A, 2.5e-3)
F = dp * A
eq("cube F", sf(F, 3), 1.23)
Wcube = 7800 * 0.050**3 * g
eq("cube weight", sf(Wcube, 3), 9.56)
eq("cube reading", sf(Wcube - F, 3), 8.34)

# Stretch
S = 200 / (2 * tan(radians(60)))
eq("ladder a", sf(S, 3), 57.7)
S2 = (200 * 0.5 + 700 * 0.75) / tan(radians(60))
eq("ladder b rhs", 200 * 0.5 + 700 * 0.75, 625)
eq("ladder b", sf(S2, 3), 361)
eq("u-tube", 1000 * 18.0 / 22.5, 800)

# Quiz
eq("quiz torque", 10 * 0.40, 4.0)
eq("quiz density", 2.7 * 1000, 2700)

print("ok")
