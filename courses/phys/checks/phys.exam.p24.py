# checks/phys.exam.p24.py: recomputes every number in the Papers 2 and 4 guide.
from math import isclose, sqrt, pi, exp

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

G = 6.67e-11; e = 1.60e-19; m_e = 9.11e-31
M_E = 5.97e24

# Papers in numbers
eq("p2 min per mark", 75 / 60, 1.25)
eq("p4 min per mark", 120 / 100, 1.2)
eq("4 marks P2", 4 * 1.25, 5)
eq("6 marks P2", 6 * 1.25, 7.5)
eq("2 marks P2", 2 * 1.25, 2.5)

# command word example: kinetic energy of a car
ek = 0.5 * 1200 * 25**2
eq("car EK", ek, 375000)
eq("car EK 2sf", sf(ek, 2), 3.8e5)

# comment: g = 9.4 +- 0.5 includes 9.81
assert 9.4 - 0.5 <= 9.81 <= 9.4 + 0.5
n += 1
# predict: m x4 -> T x2
eq("period ratio", sqrt(4), 2)

# show that: ball dropped 1.8 m
v2 = 2 * 9.81 * 1.8
eq("v2", sf(v2, 3), 35.3)
eq("v", sf(sqrt(v2), 3), 5.94)

# tennis ball
dp = 0.055 * (28 + 4.0)
eq("dp", dp, 1.76)
F = dp / 6.0e-3
eq("F", sf(F, 3), 293)
eq("F 2sf", sf(F, 2), 2.9e2)
eq("F rounded dp", 1.8 / 0.0060, 300)

# unit slips
eq("90 km/h", 90 / 3.6, 25)
eq("1500 rpm", sf(1500 * 2 * pi / 60, 3), 157)
eq("20 C", 20 + 273.15, 293.15)
eq("3.2 eV", sf(3.2 * 1.60e-19, 2), 5.1e-19)
eq("0.35 litre", 0.35e-3, 3.5e-4)
eq("4.5 cm2", 4.5e-4, 4.5 * 1e-4)

# capacitor sketch
V0 = 6.0; RC = 2.2
eq("V at RC", V0 * exp(-1), 2.207, 1e-3)
eq("0.37", sf(exp(-1), 2), 0.37)

# satellite
r = 7.0e6; m = 1200
v2 = G * M_E / r
eq("sat v2", sf(v2, 3), 5.69e7, 1e4)
v = sqrt(v2)
eq("sat v", sf(v, 3), 7.54e3, 1)
eq("sat v 2sf", sf(v, 2), 7.5e3)
T = 2 * pi * r / v
eq("sat T", sf(T, 2), 5.8e3)
eq("sat T min", sf(T / 60, 2), 97)
EK = 0.5 * m * v2
EP = -G * M_E * m / r
eq("sat EK", sf(EK, 3), 3.41e10, 1e7)
eq("sat EP", sf(EP, 3), -6.83e10, 1e7)
eq("sat E", sf(EK + EP, 2), -3.4e10)
assert isclose(EK + EP, -G * M_E * m / (2 * r), rel_tol=1e-9)
n += 1
r2 = 1.0e7
dE = G * M_E * m / 2 * (1 / r - 1 / r2)
eq("sat dE", sf(dE, 2), 1.0e10)
dEP = -G * M_E * m / r2 - EP
dEK = 0.5 * m * G * M_E / r2 - EK
eq("sat dEP", sf(dEP, 3), 2.05e10, 1e7)
eq("sat dEK", sf(dEK, 3), -1.02e10, 1e7)
eq("sat dE = dEP+dEK", dEP + dEK, dE, 1e3)
assert isclose(dEP, -2 * dEK, rel_tol=1e-9)
n += 1

# electron in uniform field
V = 250; d = 0.020; vx = 3.0e7; L = 0.050
E = V / d
eq("E", E, 1.25e4)
a = e * E / m_e
eq("a", sf(a, 4), 2.195e15, 1e12)
t = L / vx
eq("t", sf(t, 3), 1.67e-9, 1e-12)
y = 0.5 * a * t**2
eq("y", sf(y, 3), 3.05e-3, 1e-5)
eq("y 2sf", sf(y, 2), 3.0e-3)
assert y < d / 2
n += 1

# quiz
eq("quiz EK", sf(0.5 * 0.45 * 12**2, 3), 32.4)
eq("quiz EK wrong", 0.5 * 0.45 * 12, 2.7)
eq("quiz v", sf(sqrt(32 / (0.5 * 0.45)), 3), 11.9)
eq("quiz p", sf(0.12 * 2.4, 3), 0.288)
eq("quiz p 2sf", sf(0.12 * 2.4, 2), 0.29)

print("ok")
