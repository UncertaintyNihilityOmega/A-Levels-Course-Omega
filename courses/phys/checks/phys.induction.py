# checks/phys.induction.py: recomputes every number in the Electromagnetic induction chapter.
from math import isclose, sqrt, exp, cos, sin, radians, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("warm P", 12 * 0.50, 6.0)

# Flux eg: square coil 2.0 cm, 0.25 T
A = 0.020**2
eq("A", A, 4.0e-4, 1e-12)
phi = 0.25 * A
eq("phi", phi, 1.0e-4, 1e-12)
eq("phi 60", phi * cos(radians(60)), 5.0e-5, 1e-12)

# Flux linkage eg: 200 turns
eq("NPhi 200", 200 * phi, 2.0e-2, 1e-12)

# Tilted coil: 50 turns, 6.0 x 4.0 cm, 0.12 T, field 30 degrees from the plane -> 60 from the normal
A2 = 0.060 * 0.040
eq("A2", A2, 2.4e-3, 1e-12)
phi2 = 0.12 * A2 * cos(radians(90 - 30))
eq("phi2", phi2, 1.44e-4, 1e-12)
eq("NPhi2", 50 * phi2, 7.2e-3, 1e-12)

# Faraday eg: 200 turns, B rises 0 -> 0.25 T in 0.050 s
NPhi = 200 * 0.25 * 4.0e-4
eq("NPhi", NPhi, 2.0e-2, 1e-12)
eq("E", NPhi / 0.050, 0.40, 1e-12)

# 100 turns, flux 5.0e-3 -> 1.0e-3 in 0.20 s
eq("start", 100 * 5.0e-3, 0.50); eq("end", 100 * 1.0e-3, 0.10)
eq("dNPhi", 100 * (5.0e-3 - 1.0e-3), 0.40, 1e-12)
eq("E2", 100 * (5.0e-3 - 1.0e-3) / 0.20, 2.0, 1e-12)
# spot the error
eq("spot dPhi", 5.0e-3 - 1.0e-3, 4.0e-3, 1e-12)
eq("spot wrong", (5.0e-3 - 1.0e-3) / 0.20, 0.020, 1e-12)

# Rod eg: L 0.40, v 3.0, B 0.50, R 2.0
E = 0.50 * 0.40 * 3.0
eq("E rod", E, 0.60)
I = E / 2.0
eq("I rod", I, 0.30)
F = 0.50 * I * 0.40
eq("F rod", F, 0.060, 1e-12)
eq("P rod", F * 3.0, 0.18, 1e-12)
eq("EI", E * I, 0.18, 1e-12)
eq("I2R", I**2 * 2.0, 0.18, 1e-12)

# Aircraft
eq("aircraft", 4.0e-5 * 30 * 250, 0.30, 1e-12)

# Coil through field: 50 turns, 4.0 cm x 5.0 cm, 0.30 T, 12 cm region, v 0.20 m/s
N, w, h, B, v, d = 50, 0.040, 0.050, 0.30, 0.20, 0.12
eq("flux linkage max", N * B * w * h, 0.030, 1e-12)
eq("t enter", w / v, 0.20); eq("t inside", (d - w) / v, 0.40); eq("t leave", w / v, 0.20)
eq("E enter", N * B * w * h / (w / v), 0.15, 1e-12)
eq("NBhv", N * B * h * v, 0.15, 1e-12)
eq("area pulse", 0.15 * 0.20, 0.030, 1e-12)
# timings used in the graph figure: 0.2, 0.6, 0.8
eq("t 0.6", (w + (d - w)) / v, 0.60); eq("t 0.8", (d + w) / v - 0.0 - 0.0 + (0.8 - (d + w) / v), 0.8)
eq("t leave end", (w / v) + (d - w) / v + (w / v), 0.80)

# Magnet through coil plot: equal areas of the two Gaussians (50 mV x 0.08 s, 80 mV x 0.05 s)
eq("areas", 50 * 0.08, 80 * 0.05, 1e-12)

# Generator eg: 200 turns, 0.020 m2, 50 Hz, 0.15 T
w50 = 2 * pi * 50
eq("omega", sf(w50), 314)
E0 = 0.15 * 0.020 * 200 * w50
eq("E0 raw", sf(E0, 4), 188.5)
eq("E0 2sf", sf(E0, 2), 190)

# Start easy
eq("e1 A", 0.050**2, 2.5e-3, 1e-12); eq("e1 phi", 0.40 * 2.5e-3, 1.0e-3, 1e-12)
eq("e2", 120 * 3.5e-4, 4.2e-2, 1e-12)
eq("e3", 0.060 / 0.40, 0.15, 1e-12)
eq("e4", sf(0.20 * 3.0e-3 * cos(radians(30)), 2), 5.2e-4, 1e-12)
eq("e6", 0.30 * 0.15 * 4.0, 0.18, 1e-12)

# Exam practice
eq("Q4", (0.048 - 0.012) / 0.15, 0.24, 1e-12)
E5 = 0.40 * 0.25 * 2.4
eq("Q5 E", E5, 0.24, 1e-12)
I5 = E5 / 1.5
eq("Q5 I", I5, 0.16, 1e-12)
F5 = 0.40 * I5 * 0.25
eq("Q5 F", F5, 0.016, 1e-12)
eq("Q5 P", sf(F5 * 2.4, 2), 0.038, 1e-12)
eq("Q5 I2R", I5**2 * 1.5, F5 * 2.4, 1e-12)
w7 = 2 * pi * 25
eq("Q7 omega", sf(w7), 157)
A7 = 0.050 * 0.080
eq("Q7 A", A7, 4.0e-3, 1e-12)
E07 = 0.20 * A7 * 120 * w7
eq("Q7 E0", sf(E07, 2), 15)
eq("Q7 E0 rounded", sf(0.20 * 4.0e-3 * 120 * 157, 2), 15)

# Stretch 1: loop 0.10 m, 0.50 ohm, 0.40 T, 2.0 m/s, 0.30 m region
L, R, B, v = 0.10, 0.50, 0.40, 2.0
Es = B * L * v
eq("S1 E", Es, 0.080, 1e-12)
Is = Es / R
eq("S1 I", Is, 0.16, 1e-12)
Fs = B * Is * L
eq("S1 F", Fs, 6.4e-3, 1e-12)
t = L / v
eq("S1 t", t, 0.050, 1e-12)
W = Is**2 * R * t
eq("S1 W", W, 6.4e-4, 1e-12)
eq("S1 Fd", Fs * L, 6.4e-4, 1e-12)
eq("S1 t leading edge leaves", 0.30 / v, 0.15, 1e-12)
eq("S1 t trailing edge leaves", (0.30 + L) / v, 0.20, 1e-12)
eq("S1 total", sf(2 * W, 2), 1.3e-3, 1e-12)

# Stretch 2: m 0.020 kg, L 0.30 m, B 0.50 T, R 0.10 ohm
m, L, B, R = 0.020, 0.30, 0.50, 0.10
I2 = m * g / (B * L)
eq("S2 I", sf(I2, 2), 1.3)
E2 = I2 * R
eq("S2 E", sf(E2, 3), 0.131)
v2 = E2 / (B * L)
eq("S2 v", sf(v2, 2), 0.87)
eq("S2 v formula", v2, m * g * R / (B**2 * L**2), 1e-12)
eq("S2 mgv", sf(m * g * v2, 3), 0.171)
eq("S2 I2R", sf(I2**2 * R, 3), 0.171)
eq("S2 mgv = I2R", m * g * v2, I2**2 * R, 1e-12)

print("ok")
