# checks/phys.mock.p4.py: recomputes every number in the Paper 4 mock and asserts the mark total.
from math import isclose, pi, sqrt, exp, log, sin, cos

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, paper says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# Data-sheet values
G = 6.67e-11; c = 3.00e8; e = 1.60e-19; me = 9.11e-31; h = 6.63e-34
NA = 6.02e23; R = 8.31; k = 1.38e-23; u = 1.66e-27; sigma = 5.67e-8

# ---- Q1 gravity -----------------------------------------------------------
r1 = 4.20e8; T1 = 6.30 * 24 * 3600
eq("Q1 T (s)", sf(T1), 5.44e5)
M = 4 * pi**2 * r1**3 / (G * T1**2)
eq("Q1c M", sf(M), 1.48e26, 1e21)
Trot = 14.0 * 3600
eq("Q1d T rot (s)", sf(Trot), 5.04e4, 1e2)
r_sync = (G * M * Trot**2 / (4 * pi**2)) ** (1 / 3)
eq("Q1d r", sf(r_sync), 8.60e7, 1e5)
assert 8.5e7 <= r_sync <= 8.7e7
m_sat = 640.0; r_hi = 1.20e8
dEp = G * M * m_sat * (1 / r_sync - 1 / r_hi)
eq("Q1e dEp", sf(dEp, 2), 2.1e10, 1e8)
# using the rounded intermediate values the answer agrees to 2 s.f.
eq("Q1e dEp rounded inputs", sf(G * 1.48e26 * m_sat * (1 / 8.60e7 - 1 / r_hi), 2), 2.1e10, 1e8)

# ---- Q2 temperature -------------------------------------------------------
c_w = 60 * 245 / (0.250 * 14.0)
eq("Q2b c", c_w, 4200, 1e-6)
L = (90 - 60) * 300 / ((10.3 - 6.4) * 1e-3)
eq("Q2c L", sf(L, 2), 2.3e6, 1e4)
assert 2.2e6 <= L <= 2.4e6
# model: heat loss h_loss is the same for both powers
hl = 12.0; Lt = 2.26e6
m60 = (60 * 300 - hl * 300) / Lt * 1e3; m90 = (90 * 300 - hl * 300) / Lt * 1e3
eq("Q2 model m60 (g)", round(m60, 1), 6.4, 0.05); eq("Q2 model m90 (g)", round(m90, 1), 10.4, 0.15)

# ---- Q3 gases -------------------------------------------------------------
p3 = 2.5e5; V3 = 3.0e-3; T3 = 290.0; mHe = 6.64e-27
eq("Q3 mHe = 4.0 u", 4.0 * u, mHe, 1e-30)
n3 = p3 * V3 / (R * T3)
eq("Q3b n", sf(n3, 2), 0.31, 1e-9)
c2 = 3 * k * T3 / mHe
eq("Q3c <c^2>", sf(c2), 1.81e6, 1e3)
eq("Q3c c_rms", sf(sqrt(c2)), 1.34e3, 1)
dV = 4.5e-3 - 3.0e-3
Wby = p3 * dV
eq("Q3d(i) work done by gas", Wby, 375, 1e-9)
dU = 900 - Wby
eq("Q3d(ii) dU", dU, 525, 1e-9)

# ---- Q4 oscillations ------------------------------------------------------
x0 = 0.030; T4 = 0.80; m4 = 0.250
w = 2 * pi / T4
eq("Q4 omega", sf(w), 7.85, 5e-3)
eq("Q4b(i) v0", sf(w * x0, 2), 0.24, 1e-9)
eq("Q4b(ii) a0", sf(w**2 * x0, 2), 1.9, 1e-9)
Ek = 0.5 * m4 * w**2 * (x0**2 - 0.020**2)
eq("Q4c Ek", sf(Ek, 2), 3.9e-3, 1e-9)
# the plotted curve 3.0 sin(2 pi t / 0.80): crest at t = 0.20 s, zero at 0.40 s
eq("Q4 plot crest at 0.2 s", 3.0 * sin(2 * pi * 0.20 / 0.80), 3.0, 1e-9)
eq("Q4 plot zero at 0.8 s", 3.0 * sin(2 * pi * 0.80 / 0.80), 0.0, 1e-9)

# ---- Q5 electric fields ---------------------------------------------------
V5 = 600.0; d5 = 0.040; L5 = 0.050; v5 = 2.5e7
E5 = V5 / d5
eq("Q5b E", E5, 1.5e4, 1e-6)
a5 = e * E5 / me
eq("Q5c a", sf(a5, 2), 2.6e15, 1e12)
t5 = L5 / v5
eq("Q5d t", t5, 2.0e-9, 1e-15)
y5 = 0.5 * a5 * t5**2
eq("Q5d y", sf(y5, 2), 5.3e-3, 1e-9)
assert y5 < d5 / 2   # the electron does not hit the plate
# figure: 4.0 cm is 122 px (58 to 180), so 5.0 cm is 152.5 px: plates drawn 152 px long
px_per_cm = 122 / 4.0
eq("Q5 fig plate length (px)", 152, L5 * 100 * px_per_cm, 1.0)
eq("Q5 fig deflection (px)", 119 - 103, y5 * 100 * px_per_cm, 1.0)
slope_exit = 2 * y5 / L5          # dy/dx of the parabola at the exit
eq("Q5 fig exit slope", (119 - 103) / (322 - 246), slope_exit, 0.01)

# ---- Q6 capacitance -------------------------------------------------------
C6 = 330e-6; V6 = 15.0; R6 = 47e3
E6 = 0.5 * C6 * V6**2
eq("Q6b E", sf(E6, 2), 3.7e-2, 1e-9)
tau = R6 * C6
eq("Q6c(i) tau", sf(tau), 15.5, 1e-9)
t6 = tau * log(V6 / 3.0)
eq("Q6c(ii) t", sf(t6, 2), 25, 1e-9)
eq("Q6c(ii) check V at t", V6 * exp(-t6 / tau), 3.0, 1e-9)
Cs = 1 / (1 / 330 + 1 / 220)
eq("Q6d series", sf(Cs), 132, 1e-9)

# ---- Q7 magnetic fields ---------------------------------------------------
v7 = (1.2e3 / 0.030) / 0.050
eq("Q7c v", v7, 8.0e5, 1e-6)
eq("Q7c E", 1.2e3 / 0.030, 4.0e4, 1e-9)
# (d) V_H = BI/(ntq): half the thickness doubles V_H
B7, I7, n7, q7 = 0.05, 1e-3, 1e22, e
eq("Q7d VH ratio", (B7 * I7 / (n7 * 0.5e-4 * q7)) / (B7 * I7 / (n7 * 1.0e-4 * q7)), 2.0, 1e-12)

# ---- Q8 induction, a.c., rectification ------------------------------------
N8 = 400; A8 = 1.5e-3; B8 = 0.060; dt8 = 0.20
emf = N8 * B8 * A8 / dt8
eq("Q8b emf", emf, 0.18, 1e-12)
V0 = 24.0; R8 = 12.0
Vr = V0 / sqrt(2)
eq("Q8c(i) Vrms", sf(Vr, 2), 17, 1e-9)
P8 = Vr**2 / R8
eq("Q8c(ii) P", P8, 24.0, 1e-9)
eq("Q8c P = V0^2/2R", V0**2 / (2 * R8), 24.0, 1e-9)
# figure: full-wave rectified output of a 50 Hz supply, peak 12 V, tau = 40 ms, steady ripple ~2 V
Vp = 12.0; tau8 = 40e-3; dts = 0.25e-3
Vc = 0.0; vmin = Vp
for i in range(int(50e-3 / dts) + 1):
    t = i * dts
    Vc = max(abs(Vp * sin(2 * pi * 50 * t)), Vc * exp(-dts / tau8))
    if t > 12e-3: vmin = min(vmin, Vc)
eq("Q8 fig ripple (V)", sf(Vp - vmin, 2), 2.1, 1e-9)
# figure scale: 12 V = 140 px (y 190 to 50); the lowest point of the solid curve is at y = 75
eq("Q8 fig min y", 190 - vmin * 140 / 12, 75.0, 0.2)
eq("Q8 fig peak x (t = 5 ms -> x = 110)", 70 + 5 * 8.0, 110.0, 1e-9)

# ---- Q9 quantum -----------------------------------------------------------
E9 = h * c / 380e-9
eq("Q9b photon energy", sf(E9), 5.23e-19, 1e-21)
eq("Q9b Ek max", sf(E9 - 3.2e-19, 2), 2.0e-19, 1e-21)
assert E9 > 3.2e-19      # emission happens
p9 = sqrt(2 * me * e * 250)
eq("Q9c lambda", sf(h / p9, 2), 7.8e-11, 1e-13)
dE9 = (-1.2 - (-3.6)) * e
eq("Q9d dE (J)", sf(dE9), 3.84e-19, 1e-21)
eq("Q9d lambda", sf(h * c / dE9, 2), 5.2e-7, 1e-9)
# levels: 25 px per eV below the ionisation line at y = 40
for E_eV, y in [(-1.2, 70), (-2.0, 90), (-3.6, 130), (-8.0, 240)]:
    eq(f"Q9 fig level {E_eV}", 40 - E_eV * 25, y, 1e-9)

# ---- Q10 nuclear ----------------------------------------------------------
mp, mn, mO = 1.00728, 1.00867, 15.99053
dm = 8 * mp + 8 * mn - mO
eq("Q10b mass defect (u)", sf(dm, 5), 0.13707, 1e-9)
EB = dm * u * c**2
eq("Q10b EB (J)", sf(EB), 2.05e-11, 1e-13)
EB_MeV = EB / e / 1e6
eq("Q10b EB (MeV)", sf(EB_MeV), 128, 1e-9)
eq("Q10b per nucleon", sf(EB_MeV / 16), 8.00, 1e-9)
assert 7.9 <= EB_MeV / 16 <= 8.1
N10 = 5.0e-6 / 24 * NA
eq("Q10c N", sf(N10), 1.25e17, 1e14)
lam10 = 0.693 / (15.0 * 3600)
eq("Q10c lambda", sf(lam10), 1.28e-5, 1e-8)
eq("Q10c A", sf(lam10 * N10, 2), 1.6e12, 1e9)

# ---- Q11 medical physics --------------------------------------------------
Z1, Z2 = 1.38e6, 1.70e6
refl = (Z2 - Z1)**2 / (Z2 + Z1)**2
eq("Q11a(i) reflection coefficient", sf(refl, 2), 0.011, 1e-9)
eq("Q11a(ii) air-skin reflection is almost total", sf((1.70e6 - 4.3e2)**2 / (1.70e6 + 4.3e2)**2, 3), 0.999, 1e-9)
mu11 = 65.0
x11 = log(1 / 0.12) / mu11
eq("Q11b x", sf(x11, 2), 3.3e-2, 1e-9)
eq("Q11b check", exp(-mu11 * x11), 0.12, 1e-12)
Eg = me * c**2
eq("Q11c(i) E photon", sf(Eg, 2), 8.2e-14, 1e-16)
eq("Q11c(i) in MeV", sf(Eg / 1.60e-13, 2), 0.51, 1e-9)

# ---- Q12 astrophysics -----------------------------------------------------
T12 = 2.90e-3 / 450e-9
eq("Q12b T", sf(T12), 6.44e3, 1)
L12 = 4.0e27
r12 = sqrt(L12 / (4 * pi * sigma * T12**4))
eq("Q12c r", sf(r12, 2), 1.8e9, 1e6)
r12r = sqrt(L12 / (4 * pi * sigma * 6.44e3**4))
eq("Q12c r with rounded T", sf(r12r, 2), 1.8e9, 1e6)
v12 = c * (398.6 - 393.4) / 393.4
eq("Q12d v", sf(v12, 2), 4.0e6, 1e4)
d12 = v12 / 1e3 / 70.0
eq("Q12d d (Mpc)", sf(d12, 2), 57, 1e-9)
eq("Q12d d (Mpc) from rounded v", sf(4.0e6 / 1e3 / 70.0, 2), 57, 1e-9)
assert 56 <= d12 <= 57.5

marks = {}
marks[1] = {"a": 1, "b": 2, "c": 2, "d": 2, "e": 2}
marks[2] = {"a": 1, "b": 2, "c": 2, "d": 2}
marks[3] = {"a": 2, "b": 2, "c": 2, "d(i)": 2, "d(ii)": 1}
marks[4] = {"a": 2, "b(i)": 2, "b(ii)": 2, "c": 2, "d": 1}
marks[5] = {"a": 1, "b": 2, "c": 2, "d": 2, "e": 2}
marks[6] = {"a": 1, "b": 2, "c(i)": 1, "c(ii)": 2, "d": 2}
marks[7] = {"a": 2, "b": 2, "c": 2, "d": 2}
marks[8] = {"a(i)": 1, "a(ii)": 1, "b": 2, "c(i)": 1, "c(ii)": 2, "d": 2}
marks[9] = {"a": 2, "b": 2, "c": 2, "d": 2}
marks[10] = {"a": 1, "b": 3, "c": 3, "d": 1}
marks[11] = {"a(i)": 3, "a(ii)": 1, "b": 2, "c(i)": 1, "c(ii)": 1}
marks[12] = {"a": 1, "b": 2, "c": 2, "d": 2, "e": 1}

want = {1: 9, 2: 7, 3: 9, 4: 9, 5: 9, 6: 8, 7: 8, 8: 9, 9: 8, 10: 8, 11: 8, 12: 8}
assert len(marks) == 12
for q, parts in marks.items():
    assert sum(parts.values()) == want[q], f"Q{q}: parts sum to {sum(parts.values())}, header says {want[q]}"
total = sum(sum(p.values()) for p in marks.values())
assert total == 100, f"paper total {total}"
syn = {"Q1(b)": 2, "Q4(c)": 2, "Q5(d)": 2, "Q7(b)": 2, "Q8(c)": 3, "Q9(c)": 2, "Q11(c)(ii)": 1}
assert sum(syn.values()) >= 12, sum(syn.values())
print("ok")
