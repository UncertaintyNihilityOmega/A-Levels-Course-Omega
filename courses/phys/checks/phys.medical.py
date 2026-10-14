# checks/phys.medical.py: recomputes every number in the Medical physics chapter.
from math import isclose, exp, log

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# Data sheet values
h, c, e, me = 6.63e-34, 3.00e8, 1.60e-19, 9.11e-31
v_t = 1540.0                      # speed of sound in soft tissue (typical)
Z_air = 1.3 * 330
Z_t = 1060 * 1540
Z_b = 1900 * 4000
R = lambda a, b: (a - b) ** 2 / (a + b) ** 2
LN2 = 0.693                       # the syllabus form t1/2 = 0.693/lambda

# Warm-up
eq("warm wavelength", sf(1540 / 3.0e6, 2), 5.1e-4, 1e-12)
Ephot = h * c / 1.0e-10
eq("warm E J", sf(Ephot, 3), 1.99e-15, 1e-18)
eq("warm E keV", sf(Ephot / e / 1e3, 2), 12)
eq("warm quarter", 0.5 * 0.5, 0.25)

# 5.0 MHz wavelength
lam5 = v_t / 5.0e6
eq("lam 5 MHz", sf(lam5, 2), 3.1e-4, 1e-12)
eq("lam 5 MHz mm", sf(lam5 * 1e3, 2), 0.31)

# Echo depth
eq("depth 65us", sf(v_t * 65e-6 / 2, 2), 5.0e-2, 1e-12)
eq("depth cm", sf(v_t * 65e-6 / 2 * 100, 2), 5.0)

# Pulse rate
t_deep = 2 * 0.15 / v_t
eq("t deep", sf(t_deep, 2), 1.9e-4, 1e-12)
eq("t deep 4sf", sf(t_deep, 4), 1.948e-4, 1e-10)
eq("prf", sf(1 / t_deep, 2), 5.1e3, 1e-6)

# Resolution
dt = 2 * 2.0e-3 / v_t
eq("dt 2mm us", sf(dt * 1e6, 2), 2.6)
eq("pulse duration", 3 / 5.0e6, 0.60e-6, 1e-12)
assert 3 / 5.0e6 < dt

# Lab: gradient
eq("lab v", sf(2 / 5.88e-3, 3), 340, 1e-6)

# Impedances
eq("Z air", sf(Z_air, 2), 4.3e2, 1e-9)
eq("Z tissue", sf(Z_t, 3), 1.63e6, 1)
eq("Z bone", Z_b, 7.6e6)
eq("Z tissue 1.6324", Z_t / 1e6, 1.6324, 1e-9)
r_tb = R(Z_t, Z_b)
eq("R tissue-bone", sf(r_tb, 3), 0.418, 1e-9)
eq("R pieces num", sf((1.6324 - 7.6) ** 2, 3) ** 0.5, 5.97, 0.01)
eq("R 5.9676", Z_b / 1e6 - Z_t / 1e6, 5.9676, 1e-9)
eq("R 9.2324", Z_b / 1e6 + Z_t / 1e6, 9.2324, 1e-9)
eq("tissue-bone pct", sf(r_tb * 100, 2), 42)
eq("tissue-bone T pct", sf((1 - r_tb) * 100, 2), 58)
r_at = R(Z_air, Z_t)
eq("R air-tissue", sf(r_at, 3), 0.999, 1e-9)
eq("air tissue enter pct", sf((1 - r_at) * 100, 1), 0.1, 1e-9)
r_gel = R(1.50e6, Z_t)
eq("R gel", sf(r_gel, 2), 1.8e-3, 1e-12)
assert 1 - r_gel > 0.998

# Attenuation
mu = 35.0
eq("mu cm", mu / 100, 0.35)
xh = LN2 / mu
eq("x half m", sf(xh, 2), 0.020, 1e-12)
eq("x half cm", sf(xh * 100, 2), 2.0)
eq("plot 1.98 halves", exp(-0.35 * 1.98), 0.5, 1e-3)
eq("plot 3.96 quarter", exp(-0.35 * 3.96), 0.25, 1e-3)
eq("plot x half 1.98", sf(xh * 100, 3), 1.98)
eq("plot 4.0 label", sf(2 * xh * 100, 2), 4.0)
# lab aluminium
mu_al = log(820 / 165) / 16e-3
eq("mu Al", sf(mu_al, 2), 1.0e2, 1e-9)
# 4.0 cm echo
f40 = exp(-mu * 0.080)
eq("echo 4cm fraction", sf(f40, 2), 0.061, 1e-12)
eq("echo 4cm pct", sf(f40 * 100, 2), 6.1)
# combined, 3.0 cm
a30 = exp(-mu * 0.060)
eq("att 6cm", sf(a30, 4), 0.1225, 1e-9)
tot = a30 * r_tb
eq("combined fraction", sf(tot, 2), 0.051, 1e-12)
eq("combined 3sf", sf(tot, 3), 0.0512, 1e-9)

# X-ray production
lam80 = h * c / (e * 80e3)
eq("lmin 80 kV", sf(lam80, 3), 1.55e-11, 1e-14)
eq("Emax 80 keV", 80e3 * e, 1.28e-14, 1e-17)
lam120 = h * c / (e * 120e3)
eq("lmin 120 kV", sf(lam120, 3), 1.04e-11, 1e-14)
eq("fig px 80", sf(lam80 * 1e11, 3), 1.55)
eq("fig px 120", sf(lam120 * 1e11, 3), 1.04)
ne = 15e-3 / e
eq("electrons per s", sf(ne, 2), 9.4e16, 1e12)
P = 15e-3 * 80e3
eq("tube power", P, 1.2e3, 1e-6)
eq("xray 1pct", 0.01 * P, 12, 1e-9)
eq("heat 99pct", sf(0.99 * P, 2), 1.2e3, 1e-6)

# Contrast
tA = exp(-30 * 0.100)
eq("path A", sf(tA, 2), 0.050, 1e-12)
ex = 150 * 0.030 + 30 * 0.070
eq("exponent B", ex, 6.6, 1e-9)
tB = exp(-ex)
eq("path B", sf(tB, 2), 1.4e-3, 1e-9)
eq("ratio", sf(tA / tB, 2), 37)
eq("ratio e^3.6", exp(3.6), tA / tB, 1e-9)

# Annihilation
E_ann = me * c ** 2
eq("E ann J", sf(E_ann, 3), 8.20e-14, 1e-17)
eq("E ann eV", sf(E_ann / e, 3), 5.12e5, 1)
eq("E ann MeV", sf(E_ann / e / 1e6, 3), 0.512, 1e-9)
eq("wavelength ann", sf(h * c / E_ann, 3), 2.43e-12, 1e-15)
eq("photon momentum", sf(E_ann / c, 3), 2.73e-22, 1e-25)
eq("2 m c^2", sf(2 * E_ann, 3), 1.64e-13, 1e-16)
eq("2 x 8.20e-14", 2 * 8.20e-14, 1.64e-13, 1e-16)

# PET timing and F-18
eq("tof 0.30 ns", c * 0.30e-9 / 2, 4.5e-2, 1e-12)
lam_f = LN2 / (110 * 60)
eq("lambda F18", sf(lam_f, 3), 1.05e-4, 1e-9)
A = 370 * exp(-LN2 * 240 / 110)
eq("A F18 4h", sf(A, 2), 82)
eq("fraction F18 4h", sf(exp(-LN2 * 240 / 110) * 100, 2), 22)

# Start easy
eq("e1 wavelength", sf(1540 / 2.5e6, 2), 6.2e-4, 1e-12)
eq("e2 depth", sf(1540 * 80e-6 / 2, 2), 0.062, 1e-12)
eq("e3 Z water", 1000 * 1480, 1.48e6)
eq("e4 R", sf(R(1.60e6, 1.70e6), 2), 9.2e-4, 1e-12)
eq("e4 num", (1.60 - 1.70) ** 2, 0.0100, 1e-9)
eq("e4 den", (1.60 + 1.70) ** 2, 10.89, 1e-9)
eq("e5 attenuation", sf(exp(-30 * 0.050), 2), 0.22, 1e-12)
eq("e6 lmin 50 kV", sf(h * c / (e * 50e3), 2), 2.5e-11, 1e-14)
eq("e7 three half lives", 0.5 ** 3, 0.125)

# Exam practice
eq("x2 lmin 65 kV", sf(h * c / (e * 65e3), 2), 1.9e-11, 1e-14)
eq("x2 Emax eV", 65e3, 6.5e4)
Z_air2, Z_sk = 4.3e2, 1.7e6
eq("x4 R", sf(R(Z_air2, Z_sk), 3), 0.999, 1e-9)
# Q8
Zt8, Zb8 = 1.63e6, 7.60e6
R8 = R(Zt8, Zb8)
eq("x8 R", sf(R8, 3), 0.418, 1e-9)
I1 = 5.0e2 * exp(-35 * 0.050)
eq("x8 I at boundary", sf(I1, 2), 87)
I2 = I1 * R8
eq("x8 reflected", sf(I2, 2), 36)
I3 = I2 * exp(-35 * 0.050)
eq("x8 back at surface", sf(I3, 2), 6.3, 1e-9)
# rounded chain also agrees
eq("x8 rounded chain", sf(0.418 * 87 * exp(-35 * 0.050), 2), 6.3, 1e-9)
eq("x8 e^-1.75 sensible", sf(exp(-1.75), 3), 0.174, 1e-9)

# Stretch 1
eq("s1 tissue xhalf", sf(LN2 / 30, 2), 2.3e-2, 1e-12)
eq("s1 lead xhalf", sf(LN2 / 2700, 2), 2.6e-4, 1e-12)
eq("s1 ratio 90", 2700 / 30, 90)
eq("s1 lead 1mm", sf(exp(-2700 * 1.0e-3), 2), 0.067, 1e-12)
eq("s1 1pct", sf(log(100) / 2700, 2), 1.7e-3, 1e-12)
# Stretch 2
eq("s2 x", c * 1.2e-9 / 2, 0.18, 1e-9)
eq("s2 dx", c * 0.20e-9 / 2, 0.030, 1e-9)

# Quiz
eq("q echo", sf(1540 * 40e-6 / 2 * 100, 2), 3.1)
eq("q echo d=vt", sf(1540 * 40e-6 * 100, 2), 6.2)
eq("q echo 1.5", sf(1540 * 40e-6 / 4 * 100, 2), 1.5)
eq("q echo 12", sf(1540 * 40e-6 * 2 * 100, 2), 12)
eq("q lmin halves", (h * c / (e * 2 * 80e3)) / (h * c / (e * 80e3)), 0.5)
eq("q total ann MeV", sf(2 * E_ann / e / 1e6, 3), 1.02, 1e-9)
eq("q half ann MeV", sf(E_ann / e / 1e6 / 2, 2), 0.26, 1e-9)

# Exam: X-ray contrast question (arm 6.0 cm)
eq("xq IA", sf(exp(-30 * 0.060), 2), 0.17, 1e-9)
eq("xq exponent B", 150 * 0.020 + 30 * 0.040, 4.2, 1e-9)
eq("xq IB", sf(exp(-4.2), 2), 0.015, 1e-9)
eq("xq ratio", sf(exp(4.2 - 1.8), 2), 11, 1e-9)

print("ok")
