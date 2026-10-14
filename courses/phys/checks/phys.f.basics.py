# checks/phys.f.basics.py: recomputes every number in the Physics from zero chapter.
from math import isclose, sqrt, sin, cos, tan, atan, asin, radians, degrees, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("warm std", 4.2e-4, 0.00042)
eq("warm 12%", 0.12 * 250, 30)
eq("warm x", (20 - 5) / 3, 5)

# Standard form examples
eq("45.6e6", 4.56e7, 45_600_000)
eq("7.2e-6", 7.2e-6, 0.0000072)
eq("multiply SF", (3.00e8) * (2.0e-3), 6.0e5, tol=1e-6)

# s.f. example
eq("v 250/12", 250 / 12, 20.8333333333, tol=1e-9 + 1e-6)
eq("v 2sf", sf(250 / 12, 2), 21)
eq("25340 3sf", sf(25340, 3), 25300)

# prefixes
eq("2.4 GHz", 2.4e9, 2.4 * 10**9)
eq("350 mA", 350e-3, 0.350)
eq("25 um", 25e-6, 2.5e-5)
eq("650 nm", 650e-9, 6.50e-7, tol=1e-15)
eq("12 pF", 12e-12, 1.2e-11, tol=1e-20)
eq("cm2", (1e-2) ** 2, 1e-4, tol=1e-15)
eq("cm3", (1e-2) ** 3, 1e-6, tol=1e-18)
eq("25 cm2", 25e-4, 2.5e-3, tol=1e-12)

# Rearranging examples
eq("t = s/v", 540 / 6.0, 90)
I = 2400 / 230
eq("I kettle", I, 10.4347826, tol=1e-6)
eq("I 2sf", sf(I, 2), 10)
eq("V = m/rho", 0.54 / 2700, 2.0e-4, tol=1e-12)
v = sqrt(2 * 1800 / 80)
eq("v from E", v ** 2, 45)
eq("v 2sf", sf(v, 2), 6.7)
eq("a suvat", (20**2 - 8.0**2) / (2 * 120), 1.4)
eq("336", 20**2 - 8.0**2, 336)
eq("240", 2 * 120, 240)

# Graphs: s = 4t + 10
f = lambda t: 4 * t + 10
eq("pt1", f(2), 18)
eq("pt2", f(8), 42)
eq("gradient", (42 - 18) / (8 - 2), 4.0)
eq("intercept", f(0), 10)
# V = 5.0 I
eq("V pt", 5.0 * 0.8, 4.0)
eq("R grad", 4.0 / 0.80, 5.0)
# inverse
eq("t = 12/v 2", 12 / 2, 6)
eq("t = 12/v 4", 12 / 4, 3)
# area under v-t
eq("accel", 12 / 6.0, 2.0)
eq("plot pt", 2 * 6, 12)
eq("area tri", 0.5 * 6.0 * 12, 36)
eq("area rect", 12 * 10, 120)
eq("total", 36 + 120, 156)
eq("total 2sf", sf(156, 2), 160)

# Trigonometry
eq("ramp sin", 0.60 / 3.0, 0.20)
th = degrees(asin(0.20))
eq("ramp angle", th, 11.5369, tol=1e-3)
eq("ramp 1 d.p.", round(th, 1), 11.5)
eq("ramp 2sf", sf(th, 2), 12)
Fx = 40 * cos(radians(30))
Fy = 40 * sin(radians(30))
eq("Fx", Fx, 34.641016, tol=1e-5)
eq("Fx 3sf", sf(Fx, 3), 34.6)
eq("Fx 2sf", sf(Fx, 2), 35)
eq("Fy", Fy, 20.0, tol=1e-9)
eq("slope", 50 * sin(radians(20)), 17.101, tol=1e-3)
eq("slope 2sf", sf(50 * sin(radians(20)), 2), 17)
eq("pythag", sqrt(3.0**2 + 4.0**2), 5.0)
eq("angle 3-4", degrees(atan(4.0 / 3.0)), 53.13, tol=1e-2)
eq("angle 2sf", sf(degrees(atan(4.0 / 3.0)), 2), 53)

# figure geometry: 40 N drawn 200 px long at 30 degrees
eq("fig tip x", 80 + 200 * cos(radians(30)), 253.2, tol=0.05)
eq("fig tip y", 230 - 200 * sin(radians(30)), 130, tol=1e-9)
eq("fig arc x", 80 + 40 * cos(radians(30)), 114.6, tol=0.05)
eq("fig arc y", 230 - 40 * sin(radians(30)), 210, tol=1e-9)
eq("tri arc x", 60 + 35 * cos(atan(120 / 180)), 89.1, tol=0.05)
eq("tri arc y", 200 - 35 * sin(atan(120 / 180)), 180.6, tol=0.05)

# Areas and volumes
r = 0.25e-3
A = pi * r**2
eq("wire A", A, 1.9635e-7, tol=1e-10)
eq("wire A 3sf", sf(A, 3), 1.96e-7, tol=1e-12)
eq("wire A 2sf", sf(A, 2), 2.0e-7, tol=1e-12)
eq("wire V", A * 2.0, 3.927e-7, tol=1e-10)
eq("wire V 2sf", sf(A * 2.0, 2), 3.9e-7, tol=1e-12)
eq("ball area", 4 * pi * 0.11**2, 0.1521, tol=1e-4)
eq("ball area 2sf", sf(4 * pi * 0.11**2, 2), 0.15)
eq("ball vol", 4 / 3 * pi * 0.11**3, 5.5752e-3, tol=1e-6)
eq("ball vol 2sf", sf(4 / 3 * pi * 0.11**3, 2), 5.6e-3, tol=1e-9)

# School physics
eq("a car", (27 - 0) / 9.0, 3.0)
eq("W earth", 70 * g, 686.7, tol=1e-9 + 0.01)
eq("W earth 2sf", sf(70 * g, 2), 690)
eq("W moon", 70 * 1.6, 112, tol=1e-9)
eq("W moon 2sf", sf(70 * 1.6, 2), 110)
eq("resultant", 3000 - 800, 2200)
eq("a car F=ma", 2200 / 1200, 1.8333, tol=1e-3)
eq("a 2sf", sf(2200 / 1200, 2), 1.8)
Ep = 20 * g * 1.5
eq("Ep", Ep, 294.3, tol=1e-9 + 1e-6)
eq("Ep 2sf", sf(Ep, 2), 290)
eq("P lift", Ep / 3.0, 98.1, tol=1e-6)
eq("P lift 2sf", sf(Ep / 3.0, 2), 98)
eq("eff", (Ep / 3.0) / 150, 0.654, tol=1e-6)
eq("eff %", sf((Ep / 3.0) / 150 * 100, 2), 65)
eq("pressure", 600 / 0.040, 15000)
eq("cube V", 0.020**3, 8.0e-6, tol=1e-15)
rho = 0.0630 / 0.020**3
eq("rho", rho, 7875, tol=1e-6)
eq("rho 2sf", sf(rho, 2), 7900)
# circuit
eq("I circuit", 6.0 / 20, 0.30)
eq("P circuit", 6.0 * 0.30, 1.8)
eq("Q circuit", 0.30 * 2.0 * 60, 36)
# waves
eq("lambda sound", 340 / 440, 0.7727, tol=1e-3)
eq("lambda sound 2sf", sf(340 / 440, 2), 0.77)
eq("lambda radio", 3.00e8 / 1.00e8, 3.00)
# radioactivity
eq("Ra A", 226 - 4, 222)
eq("Ra Z", 88 - 2, 86)
eq("half-lives", 12 / 4.0, 3)
eq("activity", 960 / 2**3, 120)
eq("960/480/240/120", 960 / 2 / 2 / 2, 120)
eq("C-14 neutrons", 14 - 6, 8)

# Spot the error
eq("cube V cm", (2.0e-2) ** 3, 8.0e-6, tol=1e-15)
eq("wrong rho", 21.6 / 8.0e-6, 2.7e6, tol=1)
eq("rho right", 0.0216 / 8.0e-6, 2700, tol=1e-6)
eq("rho / water", 2700 / 1000, 2.7)

# Start easy
eq("e1", 3.5e-4 / 1e-6, 350, tol=1e-9 + 1e-6)
eq("e2a", 72000 / 3600, 20)
eq("e2b", 15 * 3600 / 1000, 54)
eq("e3", (15 - 3.0) / 2.0, 6.0)
eq("e4", 2.0 / 0.40, 5.0)
eq("e5a", 60 * cos(radians(40)), 45.96, tol=0.01)
eq("e5a 2sf", sf(60 * cos(radians(40)), 2), 46)
eq("e5b", 60 * sin(radians(40)), 38.567, tol=0.01)
eq("e5b 2sf", sf(60 * sin(radians(40)), 2), 39)
eq("e6 r", 0.60e-2, 6.0e-3, tol=1e-12)
eq("e6 A", pi * (6.0e-3) ** 2, 1.131e-4, tol=1e-7)
eq("e6 A 2sf", sf(pi * (6.0e-3) ** 2, 2), 1.1e-4, tol=1e-12)
eq("e7", 2.5 * g, 24.525, tol=1e-9 + 1e-6)
eq("e7 2sf", sf(2.5 * g, 2), 25)
eq("e8", 2000 * 3.0 * 60, 360000)
eq("e9", 2.0 * 0.75, 1.5)
eq("e10", 800 / 0.40, 2000)

# Ready for AS?
eq("as1 a", (25 - 5.0) / 8.0, 2.5)
eq("as1 s", 0.5 * (5.0 + 25) * 8.0, 120)
eq("as1 s check", 5.0 * 8.0 + 0.5 * 2.5 * 8.0**2, 120)
eq("as2 x", 80 * cos(radians(60)), 40, tol=1e-9)
eq("as2 y", 80 * sin(radians(60)), 69.282, tol=1e-3)
eq("as2 y 2sf", sf(80 * sin(radians(60)), 2), 69)
V = pi * 0.40**2 * 1.2
eq("as3 V", V, 0.6032, tol=1e-4)
eq("as3 V 2sf", sf(V, 2), 0.60)
eq("as3 m", 1000 * V, 603.2, tol=0.1)
eq("as3 m 2sf", sf(1000 * V, 2), 600)
eq("as4 R", 6.0 / 0.50, 12)
eq("as4 E", 6.0 * 0.50 * 120, 360)
eq("as5 lambda", 340 / 512, 0.6641, tol=1e-3)
eq("as5 lambda 2sf", sf(340 / 512, 2), 0.66)

# Quiz
eq("quiz std", 7.2e-5, 0.000072, tol=1e-12)
eq("quiz Fy", 40 * sin(radians(30)), 20, tol=1e-9)
eq("quiz Fx", sf(40 * cos(radians(30)), 2), 35)
eq("quiz 69", sf(80 * sin(radians(60)), 2), 69)

print("ok")
