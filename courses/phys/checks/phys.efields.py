# checks/phys.efields.py: recomputes every number in the Electric fields chapter.
from math import isclose, sqrt, pi, atan, degrees, tan, sin, cos, radians

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# data sheet values
g = 9.81
e = 1.60e-19
me = 9.11e-31
mp = 1.67e-27
G = 6.67e-11
eps0 = 8.85e-12
k = 1 / (4 * pi * eps0)
eq("k = 8.99e9", sf(k), 8.99e9, 1e6)
K = 8.99e9          # the 3 s.f. value the chapter substitutes

# Warm-up
eq("warm g", sf(9.81 / 4), 2.45)
t = sqrt(2 * 20 / g)
eq("warm t", sf(t), 2.02)
eq("warm x", sf(12 * t, 2), 24)
eq("warm W", 3.0 * 12, 36)

# Section 1: force on charges
eq("eg1 a", 2.0e-6 * 3.0e4, 6.0e-2)
eq("eg1 b", sf(e * 3.0e4, 2), 4.8e-15, 1e-25)

# Uniform field
eq("2 kV / 5 mm", 2.0e3 / 5.0e-3, 4.0e5)
eq("force 6.4e-14", e * 4.0e5, 6.4e-14, 1e-24)

# Oil drop
E = 600 / 1.5e-2
eq("oil E", E, 4.0e4)
W = 3.3e-15 * g
eq("oil W", sf(W, 2), 3.2e-14, 1e-24)
q = W / E
eq("oil q", sf(q, 2), 8.1e-19, 1e-29)
eq("oil q / e", round(q / e), 5)

# Along the field
EK = e * 2.0e3
eq("proton EK", EK, 3.2e-16, 1e-26)
v = sqrt(2 * EK / mp)
eq("proton v", sf(v, 2), 6.2e5, 1)
eq("electron gun v", sf(sqrt(2 * e * 2.0e3 / me), 2), 2.7e7, 1)
eq("c fraction", round(100 * sqrt(2 * e * 2.0e3 / me) / 3.00e8), 9)
eq("speed ratio > 40", sqrt(2 * e * 2.0e3 / me) / v > 40, True)
eq("mass ratio ~ 2000", round(mp / me, -2), 1800)   # 'nearly 2000 times smaller'
assert 1700 < mp / me < 2000

# Electron between plates (worked example)
Ep = 500 / 2.0e-2
eq("E plates", Ep, 2.5e4)
F = e * Ep
eq("F plates", F, 4.0e-15, 1e-25)
a = F / me
eq("a", sf(a, 2), 4.4e15, 1e13)
tt = 5.0e-2 / 3.0e7
eq("t", sf(tt, 2), 1.7e-9, 1e-12)
y = 0.5 * a * tt**2
eq("y", sf(y, 2), 6.1e-3, 1e-5)
eq("y mm for figure", round(y * 1000, 1), 6.1)
assert y < 10e-3
vy = a * tt
eq("vy", sf(vy, 2), 7.3e6, 1e4)
th = degrees(atan(vy / 3.0e7))
eq("theta", sf(th, 2), 14, 0.5)
# check the figure's geometry (60 px per cm): y = 36.6 px, slope at exit 0.244
eq("fig y px", round(y * 100 * 60, 1), 36.6, 0.05)
eq("fig slope", round(2 * 36.6 / 300, 3), 0.244, 0.001)
eq("fig slope = vy/vx", round(vy / 3.0e7, 3), 0.244, 0.001)

# Gravity negligible
w = me * g
eq("weight", sf(w, 2), 8.9e-30, 1e-31)
eq("ratio", sf(F / w, 2), 4.5e14, 1e12)

# Deflection formula check, lab gradient
Va = me * (3.0e7)**2 / (2 * e)
eq("Va", sf(Va, 2), 2600, 50)
grad = 5.0e-2**2 / (4 * 2.0e-2 * Va)
eq("gradient y/V", sf(grad, 3), 1.22e-5, 1e-8)
eq("y from formula", 500 * 5.0e-2**2 / (4 * 2.0e-2 * Va), y, 1e-9)
# with the rounded Va = 2.6 kV
eq("gradient with 2.56 kV", sf(5.0e-2**2 / (4 * 2.0e-2 * 2.56e3), 3), 1.22e-5, 1e-8)
eq("Va 2.56 kV", sf(Va, 3), 2560, 1)
eq("500 V x 1.22e-5", sf(500 * 1.22e-5 * 1000, 2), 6.1, 0.01)

# Coulomb's law
Fc = K * (2.0e-9)**2 / (30e-3)**2
eq("coulomb", sf(Fc, 2), 4.0e-5, 1e-7)
eq("coulomb eps0", sf(1 / (4 * pi * eps0) * (2.0e-9)**2 / (30e-3)**2, 2), 4.0e-5, 1e-7)
eq("2/9 factor", 2 / 3**2, 2 / 9)
ratio = K * e**2 / (G * mp**2)
eq("p-p ratio", sf(ratio, 2), 1.2e36, 1e34)

# Field of a point charge
Q = 5.0e-9
eq("E at 0.10 m", sf(K * Q / 0.10**2, 2), 4.5e3, 10)
# dipole midpoint
E1 = K * 3.0e-9 / 0.10**2
eq("dipole each", sf(E1, 3), 2.70e3, 5)
eq("dipole total", sf(2 * E1, 2), 5.4e3, 10)
# zero field point
Qq = 2.0e-9
d = 0.30
x = 2 * d / 3
eq("zero x", x, 0.20)
eq("zero other", d - x, 0.10, 1e-12)
eq("zero fields equal", K * 4 * Qq / x**2, K * Qq / (d - x)**2, 1e-6)
eq("zero field value", sf(K * Qq / (d - x)**2, 2), 1.8e3, 10)
eq("ratio 2:1", x / (d - x), 2.0, 1e-9)

# Potential
V = K * Q / 0.10
eq("V at 0.10", sf(V, 2), 4.5e2, 1)
eq("V unrounded", sf(V, 4), 449.5, 0.05)
eq("V2 unrounded", sf(K * Q / 0.20, 4), 224.8, 0.05)
eq("work 2 nC", sf(2.0e-9 * V, 2), 9.0e-7, 1e-9)
# Van de Graaff
Vd = K * 1.0e-6 / 0.15
eq("dome V", sf(Vd, 2), 6.0e4, 100)
eq("dome V 3sf", sf(Vd, 3), 5.99e4, 100)
eq("dome E", sf(Vd / 0.15, 2), 4.0e5, 1e3)
eq("dome E = kQ/r^2", sf(K * 1.0e-6 / 0.15**2, 2), 4.0e5, 1e3)
# midpoint potential
eq("midpoint V", K * (3.0e-9 / 0.10 - 3.0e-9 / 0.10), 0.0)
# Work between equipotentials
V1 = K * Q / 0.10
V2 = K * Q / 0.20
eq("V2", sf(V2, 3), 225, 1)
eq("dV", sf(V2 - V1, 3), -225, 1)
eq("dEp", sf(2.0e-9 * (V2 - V1), 2), -4.5e-7, 1e-9)
# equipotential figure labels
eq("fig V 0.40", sf(K * Q / 0.40, 3), 112, 1)
eq("fig V 0.20", sf(K * Q / 0.20, 3), 225, 1)

# Plates graph
eq("plates gradient", (0 - 800) / (2.0 - 0), -400)
eq("plates E", 400 * 100, 4.0e4)
eq("V at 0.5 cm", 800 - 400 * 0.5, 600)
eq("V at 1.5 cm", 800 - 400 * 1.5, 200)
eq("plates E from V/d", 800 / 2.0e-2, 4.0e4)

# Sphere graphs (R = 10 cm, 5.0 nC)
kQ = K * Q
eq("kQ", sf(kQ, 4), 44.95, 0.01)
Vr = lambda r_cm: kQ / (r_cm / 100)
eq("V at 10 cm", sf(Vr(10), 3), 450, 1)
eq("V coefficient", sf(Vr(1), 4), 4495, 1)
Kexact = 1 / (4 * pi * eps0)
eq("V coeff exact k", sf(Kexact * Q / 0.01, 4), 4496, 1)
eq("E at surface kV/m", sf(kQ / 0.10**2 / 1e3, 2), 4.5, 0.01)
slope = -4495 / 20**2           # V per cm at r = 20 cm
eq("slope V/cm", sf(slope, 4), -11.24, 0.005)
eq("slope V/m", sf(slope * 100, 3), -1120, 5)
eq("E at 20 cm", sf(-slope * 100, 2), 1.1e3, 10)
eq("E check kQ/r^2", sf(kQ / 0.20**2, 2), 1.1e3, 10)
eq("E coefficient kV/m", sf(kQ * 1e4 / 1e3, 5), 449.5, 0.1)   # 449.59/r^2 with r in cm

# Potential energy plot and values
eq("e2/(4 pi eps0)", sf(K * e**2, 3), 2.30e-28, 1e-30)
eq("Ep at 1e-10 m", sf(K * e**2 / 1.0e-10, 2), 2.3e-18, 1e-20)
eq("plot coefficient", sf(Kexact * e**2 / 1e-10 / 1e-18, 3), 2.30, 0.005)

# Closest approach (gold)
EKa = 5.5e6 * e
eq("alpha EK", EKa, 8.8e-13, 1e-23)
r = K * (79 * e) * (2 * e) / EKa
eq("alpha r", sf(r, 2), 4.1e-14, 1e-15)

# Hydrogen atom
rH = 5.3e-11
EpH = -K * e**2 / rH
eq("H Ep J", sf(EpH, 2), -4.3e-18, 1e-20)
eq("H Ep eV", sf(EpH / e, 2), -27)
EKH = K * e**2 / (2 * rH)
eq("H EK J", sf(EKH, 2), 2.2e-18, 1e-20)
eq("H EK eV", sf(EKH / e, 3), 13.6, 0.01)
eq("H total", sf((EpH + EKH) / e, 3), -13.6, 0.01)
eq("H total from unrounded", sf((EpH + EKH) / e, 3), -sf(EKH / e, 3), 0.01)

# Gravitational comparison (table): 10^36
eq("10^36", round(ratio / 1e36, 1), 1.2)

# Spot the error
E1 = K * 5.0e-9 / 0.20**2
eq("spot E1", sf(E1, 2), 1.1e3, 10)
eq("spot E", sf(2 * E1, 2), 2.2e3, 20)
eq("spot E 3sf", sf(2 * E1, 3), 2250, 5)

# Start easy
eq("t1", e * 2.0e4, 3.2e-15, 1e-25)
eq("t2", 1500 / 3.0e-2, 5.0e4)
eq("t3", sf(e * 1.2e5 / mp, 2), 1.1e13, 1e11)
eq("t4", sf(K * 3.0e-6 * 5.0e-6 / 0.50**2, 2), 0.54, 0.001)
eq("t5 E", sf(K * 2.0e-9 / 0.30**2, 2), 2.0e2, 1)
eq("t5 V", sf(K * -2.0e-9 / 0.30, 2), -60, 0.5)
eq("t6", sf(sqrt(2 * e * 1.0e3 / mp), 2), 4.4e5, 1e3)
eq("t7", sf(K * 2.0e-9 * -3.0e-9 / 5.0e-2, 2), -1.1e-6, 1e-8)
Ft = e * 2.0e4
eq("t8 F", Ft, 3.2e-15, 1e-25)
eq("t8 d", 8.0e-17 / Ft, 0.025, 1e-9)

# Exam practice
eq("q3 E", sf(450 / 12e-3, 2), 3.8e4, 100)
eq("q3 E 3sf", 450 / 12e-3, 3.75e4, 1e-6)
q3 = 2.4e-15 * g / 3.75e4
eq("q3 q", sf(q3, 2), 6.3e-19, 1e-20)
VP = K * 4.0e-9 / 0.20 + K * -2.0e-9 / 0.30
eq("q4 V parts", sf(K * 4.0e-9 / 0.20, 3), 180, 1)
eq("q4 V parts 2", sf(K * 2.0e-9 / 0.30, 2), 60, 1)
eq("q4 V", sf(VP, 2), 1.2e2, 1)
eq("q4 V 3sf", sf(VP, 4), 119.9, 0.1)
eq("q4 W", sf(0.50e-9 * VP, 2), 6.0e-8, 1e-9)
eq("q6 gradient", (0 - 180) / (0.20 - 0.10), -1.8e3)
# check consistent with a point charge: V = kQ'/r with kQ' = 18 V m  -> tangent hits axis at 2 r
eq("q6 tangent at 2r", 2 * 0.10, 0.20)
eq("q6 E from kQ/r^2", 18 / 0.10**2, 1.8e3, 1e-6)
# q7
E7 = 400 / 2.0e-2
eq("q7 E", E7, 2.0e4)
a7 = e * E7 / me
eq("q7 a", sf(a7, 2), 3.5e15, 1e13)
t7 = 4.0e-2 / 2.5e7
eq("q7 t", t7, 1.6e-9, 1e-15)
y7 = 0.5 * a7 * t7**2
eq("q7 y", sf(y7, 2), 4.5e-3, 1e-5)
assert y7 < 1.0e-2
vy7 = a7 * t7
eq("q7 vy", sf(vy7, 3), 5.62e6, 1e4)
eq("q7 angle", sf(degrees(atan(vy7 / 2.5e7)), 2), 13, 0.5)
# q8
EK8 = 4.8e6 * e
eq("q8 EK", sf(EK8, 2), 7.7e-13, 1e-14)
eq("q8 EK 3sf", EK8, 7.68e-13, 1e-15)
r8 = K * (47 * e) * (2 * e) / EK8
eq("q8 r", sf(r8, 2), 2.8e-14, 1e-15)

# Stretch 1
Ea = K * 2.0e-9 / 0.30**2
Eb = K * 2.0e-9 / 0.40**2
eq("s1 Ea", sf(Ea, 2), 2.0e2, 1)
eq("s1 Eb", sf(Eb, 2), 1.1e2, 1)
Er = sqrt(Ea**2 + Eb**2)
eq("s1 E", sf(Er, 2), 2.3e2, 2)
eq("s1 angle", sf(degrees(atan(Eb / Ea)), 2), 29, 0.5)
eq("s1 angle from rounded", sf(degrees(atan(112 / 200)), 2), 29, 0.5)
V1s = K * 2.0e-9 * (1 / 0.30 + 1 / 0.40)
eq("s1 V", sf(V1s, 2), 1.0e2, 5)
eq("s1 V 4sf", sf(V1s, 4), 104.9, 0.1)
eq("s1 W", sf(1.0e-9 * V1s, 2), 1.0e-7, 1e-9)

# Stretch 2
a2 = e * 2.0e4 / mp
eq("s2 a", sf(a2, 2), 1.9e12, 1e10)
uy = 4.0e5 * sin(radians(30))
eq("s2 uy", uy, 2.0e5, 1)
h = uy**2 / (2 * a2)
eq("s2 h", sf(h, 2), 1.0e-2, 1e-4)
t2 = 2 * uy / a2
eq("s2 t", sf(t2, 2), 2.1e-7, 1e-9)
ux = 4.0e5 * cos(radians(30))
eq("s2 ux", sf(ux, 3), 3.46e5, 1e3)
eq("s2 range", sf(ux * t2, 2), 7.2e-2, 1e-3)

# Quiz
eq("quiz F/2", 2 / 2**2, 0.5)
eq("quiz E doubles", (1 / 0.5), 2.0)

print("ok")
