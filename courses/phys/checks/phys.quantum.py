# checks/phys.quantum.py: recomputes every number in the Quantum physics chapter.
from math import isclose, sqrt

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def near(label, got, want, unit):
    """got rounds to want when quoted to the nearest `unit` (half up allowed)."""
    global n
    n += 1
    assert abs(got - want) <= unit / 2 + 1e-9, f"{label}: computed {got}, chapter says {want}"

h = 6.63e-34; c = 3.00e8; e = 1.60e-19; me = 9.11e-31; g = 9.81
def E_l(lam): return h * c / lam

# Warm-up
eq("warm f", c / 500e-9, 6.00e14, 1e6)
eq("warm eV", e * 100, 1.60e-17, 1e-25)

# Radio and X-ray photons
eq("radio", h * 100e6, 6.63e-26, 1e-28)
eq("xray", sf(E_l(0.10e-9)), 1.99e-15, 1e-18)
eq("xray ratio", sf(E_l(0.10e-9) / (h * 100e6), 2), 3.0e10, 1e8)

# Laser pointer
E = E_l(650e-9)
eq("laser E", sf(E), 3.06e-19, 1e-22)
eq("laser N", sf(5.0e-3 / E, 2), 1.6e16, 1e13)

# eV
eq("450 J", sf(E_l(450e-9)), 4.42e-19, 1e-22)
eq("450 eV", sf(E_l(450e-9) / e), 2.76, 1e-9)
eq("700 J", sf(E_l(700e-9)), 2.84e-19, 1e-22)
eq("700 eV", sf(E_l(700e-9) / e), 1.78, 1e-9)
eq("400 J", sf(E_l(400e-9)), 4.97e-19, 1e-22)
eq("400 eV", sf(E_l(400e-9) / e), 3.11, 1e-9)
eq("hc/e", sf(h * c / e, 4), 1.243e-6, 1e-9)
eq("tip 450", sf(1240 / 450), 2.76, 1e-9)

# Momentum
eq("p 650", sf(h / 650e-9), 1.02e-27, 1e-30)
eq("force absorbed", sf(5.0e-3 / c, 2), 1.7e-11, 1e-13)
N = 5.0e-3 / E_l(650e-9)
eq("N p", N * h / 650e-9, 5.0e-3 / c, 1e-15)
P = 1400 * 200
eq("sail P", P, 2.8e5)
eq("sail absorbed", sf(P / c, 2), 9.3e-4, 1e-6)
F = 2 * P / c
eq("sail F", sf(F, 2), 1.9e-3, 1e-5)
eq("sail a", sf(F / 5.0, 2), 3.7e-4, 1e-6)
eq("sail v", sf(F / 5.0 * 86400, 2), 32, 1e-9)

# Sodium example
phi = 2.3 * e
eq("Na phi", phi, 3.68e-19, 1e-25)
Eph = E_l(400e-9)
ke = Eph - phi
eq("Na KE", sf(ke), 1.29e-19, 1e-22)
eq("Na KE eV", sf(ke / e, 2), 0.81, 1e-9)
v = sqrt(2 * ke / me)
eq("Na v", sf(v, 2), 5.3e5, 1)
eq("Na lam0", sf(h * c / phi, 2), 5.4e-7, 1e-9)
near("Na lam0 nm", h * c / phi * 1e9, 540, 10)
eq("Na vs", sf(ke / e, 2), 0.81, 1e-9)
eq("600 nm below", float(E_l(600e-9) < phi), 1.0)

# Graph figure (units 10^14 Hz, eV)
grad = h * 1e14 / e
eq("gradient eV", sf(grad, 4), 0.4144, 1e-9)
f0_na = 2.3 / grad; f0_zn = 4.3 / grad
eq("f0 Na", sf(f0_na, 3), 5.55, 1e-9)
eq("f0 Zn", sf(f0_zn, 3), 10.4, 1e-9)
eq("zinc Phi J", sf(h * 10.4e14, 2), 6.9e-19, 1e-22)
eq("zinc Phi eV", sf(h * 10.4e14 / e, 2), 4.3, 1e-9)
eq("Na at 8.0", sf(grad * 8.0 - 2.3, 2), 1.0, 1e-9)

# Intensity warn
eq("N 400", sf(2.0e-3 / E_l(400e-9), 2), 4.0e15, 1e12)
eq("N 300", sf(2.0e-3 / E_l(300e-9), 2), 3.0e15, 1e12)
eq("N ratio", (2.0e-3 / E_l(300e-9)) / (2.0e-3 / E_l(400e-9)), 0.75, 1e-9)

# Stopping potential and h
eq("Vs", sf(ke / e, 2), 0.81, 1e-9)
eq("h photocell", sf(e * 4.1e-15, 2), 6.6e-34, 1e-36)

# Electron 150 V
p150 = sqrt(2 * me * e * 150)
eq("p 150", sf(p150), 6.61e-24, 1e-27)
eq("lam 150", sf(h / p150, 2), 1.0e-10, 1e-13)
# cricket ball
eq("cricket", sf(h / (0.16 * 30), 2), 1.4e-34, 1e-37)
eq("cricket vs nucleus", float(1e-15 / (h / (0.16 * 30)) > 1e18), 1.0)

# Spot the error
Ek = e * 150
eq("spot Ek", sf(Ek, 2), 2.4e-17, 1e-20)
eq("spot wrong lam", sf(h / 2.4e-17, 2), 2.8e-17, 1e-19)
eq("spot p", sf(sqrt(2 * me * 2.4e-17)), 6.61e-24, 1e-27)
eq("spot lam", sf(h / sqrt(2 * me * 2.4e-17), 2), 1.0e-10, 1e-13)

# Hydrogen levels
levels = {1: -13.6, 2: -3.40, 3: -1.51, 4: -0.85}
eq("3->2 gap", round(levels[3] - levels[2], 2), 1.89)
eq("3->2 J", sf(1.89 * e), 3.02e-19, 1e-22)
eq("3->2 lam", sf(h * c / (1.89 * e)), 6.58e-7, 1e-10)
table = [((4, 3), 0.66, 1880, 10), ((4, 2), 2.55, 488, 1), ((3, 2), 1.89, 658, 1),
         ((4, 1), 12.75, 97.5, 0.1), ((3, 1), 12.09, 103, 1), ((2, 1), 10.20, 122, 1)]
for (hi, lo), dE, lam, unit in table:
    eq(f"gap {hi}->{lo}", round(levels[hi] - levels[lo], 2), dE)
    near(f"lam {hi}->{lo}", h * c / (dE * e) * 1e9, lam, unit)
eq("lines n=4", 4 * 3 // 2, 6)
eq("lines n=5", 5 * 4 // 2, 10)
# 2->1 start-easy
eq("2->1 J", sf(10.2 * e), 1.63e-18, 1e-21)
eq("2->1 lam", sf(h * c / (10.2 * e)), 1.22e-7, 1e-10)
# visible-line strip positions: Balmer lines from E_n = -13.6/n^2
def xw(l): return 90 + (l - 400) * 1.4
for nn, x in ((3, 451.4), (4, 212.5), (5, 139.4), (6, 105.9)):
    dE = 13.6 * (1 / 4 - 1 / nn**2)
    lam = h * c / (dE * e) * 1e9
    eq(f"balmer x {nn}", round(xw(lam), 1), x, 0.1)
for nn, lam in ((3, 658), (4, 487.5), (5, 435), (6, 411)):
    dE = 13.6 * (1 / 4 - 1 / nn**2)
    near(f"balmer lam {nn}", h * c / (dE * e) * 1e9, lam, 1.0)
# collision
eq("1->2 gap", round(13.6 - 3.40, 2), 10.2)
eq("1->3 gap", round(13.6 - 1.51, 2), 12.09)
eq("1->3 gap 12.1", sf(13.6 - 1.51, 3), 12.1, 1e-9)
eq("electron left", round(11 - 10.2, 2), 0.8)
# ionisation
Ei = 13.6 * e
eq("ion J", sf(Ei, 3), 2.18e-18, 1e-21)
eq("ion lam", sf(h * c / Ei, 3), 9.14e-8, 1e-10)
eq("20 eV photon", round(20 - 13.6, 1), 6.4)

# Start easy
eq("se1 J", sf(h * 4.5e14), 2.98e-19, 1e-22)
eq("se1 eV", sf(h * 4.5e14 / e, 2), 1.9, 1e-9)
eq("se2 J", sf(2.4 * e), 3.84e-19, 1e-22)
eq("se2 eV", sf(3.2e-19 / e, 2), 2.0, 1e-9)
phi_cs = 2.1 * e
eq("Cs phi", phi_cs, 3.36e-19, 1e-25)
eq("Cs lam0", sf(h * c / phi_cs, 2), 5.9e-7, 1e-9)
near("Cs nm", h * c / phi_cs * 1e9, 590, 10)
eq("300 J", sf(E_l(300e-9)), 6.63e-19, 1e-22)
eq("300 eV", sf(E_l(300e-9) / e, 3), 4.14, 1e-9)
eq("300 below zinc", float(E_l(300e-9) / e < 4.3), 1.0)
eq("se5 p", sf(h / 500e-9, 2), 1.3e-27, 1e-30)
eq("se6 lam", sf(h / (me * 2.0e6), 2), 3.6e-10, 1e-12)
eq("se8 power", 0.050 * 60, 3.0)
eq("se8 E", sf(E_l(550e-9)), 3.62e-19, 1e-22)
eq("se8 N", sf(3.0 / E_l(550e-9), 2), 8.3e18, 1e16)

# Exam practice
eq("ex2 J", sf(E_l(590e-9)), 3.37e-19, 1e-22)
eq("ex2 eV", sf(E_l(590e-9) / e, 2), 2.1, 1e-9)
eq("ex4 hf", sf(E_l(254e-9)), 7.83e-19, 1e-22)
ke4 = E_l(254e-9) - 2.9 * e
eq("ex4 KE", sf(ke4), 3.19e-19, 1e-22)
eq("ex4 v", sf(sqrt(2 * ke4 / me), 2), 8.4e5, 1)
p600 = sqrt(2 * me * e * 600)
eq("ex6 p", sf(p600, 3), 1.32e-23, 1e-26)
eq("ex6 lam", sf(h / p600, 2), 5.0e-11, 1e-13)
eq("ex6 lam2400", sf(h / sqrt(2 * me * e * 2400), 2), 2.5e-11, 1e-13)
# atom X
X = [-9.0, -5.0, -3.0, -2.0]
gaps = sorted(round(X[j] - X[i], 1) for i in range(4) for j in range(i + 1, 4))
eq("X lines", len(gaps), 6)
eq("X gaps", sum(gaps), 1.0 + 2.0 + 3.0 + 4.0 + 6.0 + 7.0)
assert gaps == [1.0, 2.0, 3.0, 4.0, 6.0, 7.0], gaps
eq("X longest", sf(h * c / (1.0 * e), 2), 1.2e-6, 1e-9)
eq("X shortest", sf(h * c / (7.0 * e), 2), 1.8e-7, 1e-10)
near("X 2.0 eV nm", h * c / (2.0 * e) * 1e9, 622, 1)
near("X 3.0 eV nm", h * c / (3.0 * e) * 1e9, 414, 1)
eq("X visible lo", float(1.77 < 1.78), 1.0)
eq("visible limits eV", sf(E_l(700e-9) / e, 2), 1.8, 1e-9)
eq("visible limits eV hi", sf(E_l(400e-9) / e, 2), 3.1, 1e-9)
# KE-f data question: KE = 0.4144 f - 2.3 (eV, f in 1e14 Hz)
data = [(6.0, 0.19), (7.0, 0.60), (8.0, 1.01), (9.0, 1.43), (10.0, 1.84)]
for f, k in data:
    near(f"data {f}", grad * f - 2.3, k, 0.011)
gr = (1.84 - 0.19) / (10.0 - 6.0)
eq("data gradient eV", sf(gr, 4), 0.4125, 1e-9)
eq("data h", sf((1.84 - 0.19) * e / (4.0 * 1e14), 2), 6.6e-34, 1e-36)
eq("data intercept", sf(0.19 - gr * 6.0, 2), -2.3, 1e-9)

# Stretch
p01 = h / 0.10e-9
eq("s1 p", sf(p01, 2), 6.6e-24, 1e-26)
eq("s1 Eph J", sf(p01 * c), 1.99e-15, 1e-18)
eq("s1 Eph keV", sf(p01 * c / e / 1e3, 3), 12.4, 1e-9)
Ee = p01**2 / (2 * me)
eq("s1 Ee J", sf(Ee), 2.41e-17, 1e-20)
eq("s1 Ee eV", sf(Ee / e), 151, 1e-9)
eq("s1 ratio", sf(p01 * c / Ee, 2), 82, 1e-9)
Elas = E_l(532e-9)
eq("s2 E", sf(Elas), 3.74e-19, 1e-22)
eq("s2 N", sf(20 / Elas, 2), 5.3e19, 1e17)
F2 = 2 * 20 / c
eq("s2 F", sf(F2, 2), 1.3e-7, 1e-9)
eq("s2 F3", sf(F2, 3), 1.33e-7, 1e-10)
eq("s2 m", sf(F2 / g, 2), 1.4e-8, 1e-10)

print("ok")
