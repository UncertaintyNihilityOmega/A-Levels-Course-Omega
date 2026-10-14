# checks/phys.magnetic.py: recomputes every number in the Magnetic fields chapter.
from math import isclose, sqrt, sin, radians, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

e = 1.60e-19
me = 9.11e-31
mp = 1.67e-27
u = 1.66e-27
g = 9.81

# Warm-up
eq("warm v", sf(sqrt(2 * e * 500 / me), 2), 1.3e7, 1)
eq("warm T", 0.50 * 4.0**2 / 0.80, 10)
eq("warm drift", sf(2.0 / (1.0e-6 * 8.5e28 * e), 2), 1.5e-4, 1e-12)

# F = BIL
eq("BIL 90", 0.20 * 3.0 * 0.050, 0.030, 1e-12)
eq("BIL 30", 0.20 * 3.0 * 0.050 * sin(radians(30)), 0.015, 1e-12)

# Current balance example
grad = 0.40e-3 / 2.0
eq("balance gradient", grad, 2.0e-4, 1e-12)
Bbal = g * grad / 0.040
eq("balance B", sf(Bbal, 2), 4.9e-2, 1e-9)
eq("balance B mT", sf(Bbal * 1e3, 2), 49)

# Moving charge: electron 2.0e7 m/s in 5.0 mT
v = 2.0e7
B = 5.0e-3
F = B * e * v
eq("F electron", F, 1.6e-14, 1e-26)
eq("a electron", sf(F / me, 2), 1.8e16, 1e13)
# proton at 30 deg
Fp = 0.40 * e * 4.0e6 * sin(radians(30))
eq("F proton 30", sf(Fp, 2), 1.3e-13, 1e-25)

# radius and period for the electron
r = me * v / (B * e)
eq("r electron", sf(r, 2), 2.3e-2, 1e-9)
eq("r electron 4sf", sf(r, 4), 0.02278, 1e-9)
T = 2 * pi * r / v
eq("T electron", sf(T, 2), 7.2e-9, 1e-12)
eq("T via m", sf(2 * pi * me / (B * e), 2), 7.2e-9, 1e-12)

# Proton through 2.0 kV in 0.10 T
vp = sqrt(2 * e * 2000 / mp)
eq("proton v", sf(vp, 2), 6.2e5, 1)
eq("proton v 3sf", sf(vp, 3), 6.19e5, 10)
rp = mp * vp / (0.10 * e)
eq("proton r", sf(rp, 2), 6.5e-2, 1e-9)
eq("proton r cm", sf(rp * 100, 3), 6.46)

# Velocity selector
Esel = 600 / 0.020
eq("E plates", Esel, 3.0e4, 1e-6)
eq("v select", Esel / 0.15, 2.0e5, 1e-4)

# Hall voltage example
VH = 0.10 * 20e-3 / (1.0e22 * 0.50e-3 * e)
eq("VH semi", VH, 2.5e-3, 1e-12)
eq("n ratio", 8.5e28 / 1.0e22, 8.5e6, 1)
VHcu = VH / (8.5e28 / 1.0e22)
eq("VH copper", sf(VHcu, 2), 2.9e-10, 1e-13)
eq("VH copper direct", sf(0.10 * 20e-3 / (8.5e28 * 0.50e-3 * e), 2), 2.9e-10, 1e-13)

# Start easy
eq("se1", 0.080 * 6.0 * 0.25, 0.12, 1e-12)
eq("se4", sf(0.040 * e * 3.0e6, 2), 1.9e-14, 1e-26)
eq("se5", sf(mp * 5.0e5 / (0.20 * e), 2), 2.6e-2, 1e-9)
eq("se6", 5.0e3 / 0.025, 2.0e5, 1e-4)

# Exam practice
eq("ep2", sf(0.30 * 4.0 * 0.15 * sin(radians(40)), 2), 0.12, 1e-12)
r5 = mp * 3.0e6 / (0.50 * e)
eq("ep5 r", sf(r5, 2), 6.3e-2, 1e-9)
eq("ep5 r 3sf", sf(r5, 3), 6.26e-2, 1e-9)
eq("ep5 T", sf(2 * pi * r5 / 3.0e6, 2), 1.3e-7, 1e-12)
B6 = 3.0e-3 * 5.0e21 * 0.20e-3 * e / 15e-3
eq("ep6 B", sf(B6, 2), 3.2e-2, 1e-9)
# neon selector
v7 = 2.0e4 / 0.20
eq("ep7 v", v7, 1.0e5, 1e-6)
r20 = 20 * u * v7 / (0.20 * e)
r22 = 22 * u * v7 / (0.20 * e)
eq("ep7 r20", sf(r20, 3), 0.104, 1e-9)
eq("ep7 r20 4sf", sf(r20, 4), 0.1038, 1e-9)
eq("ep7 r22 from ratio", sf(r20 * 22 / 20, 3), 0.114, 1e-9)
eq("ep7 r22", sf(r22, 3), 0.114, 1e-9)
eq("ep7 r22 4sf", sf(r22, 4), 0.1141, 1e-9)
eq("ep7 sep", sf(2 * (r22 - r20), 2), 2.1e-2, 1e-9)

# Stretch 1: cyclotron idea
B = 1.2
t_half = pi * mp / (B * e)
eq("st1 t", sf(t_half, 2), 2.7e-8, 1e-12)
eq("st1 r1", sf(mp * 1.0e6 / (B * e), 2), 8.7e-3, 1e-9)
eq("st1 r2", sf(mp * 2.0e6 / (B * e), 2), 1.7e-2, 1e-9)
eq("st1 r ratio", (mp * 2.0e6 / (B * e)) / (mp * 1.0e6 / (B * e)), 2.0)
# Stretch 2: balance
gr = (1.80e-3 - 0.37e-3) / (5.0 - 1.0)
eq("st2 grad", sf(gr, 4), 3.575e-4, 1e-9)
eq("st2 grad 2sf", sf(gr, 2), 3.6e-4, 1e-9)
eq("st2 B", sf(g * gr / 0.060, 2), 5.8e-2, 1e-9)

print("ok")
