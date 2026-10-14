# checks/phys.capacitance.py: recomputes every number in the Capacitance chapter.
from math import isclose, exp, log, sqrt

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

k = 8.99e9          # 1/(4 pi eps0)
RE = 6.37e6
uF = 1e-6

# Warm-up
eq("warm V sphere", sf(k * 2.0e-9 / 0.10, 2), 1.8e2, 1e-9)
eq("warm R parallel", 6.0 * 3.0 / 9.0 + 4.0, 6.0)
eq("warm x", log(4), 1.39, 0.005)

# Q = CV
Q = 470 * uF * 12
eq("Q 470uF", Q, 5.64e-3, 1e-12)

# Isolated sphere
C = 0.050 * 1 / k
eq("sphere C pF", sf(C * 1e12), 5.56)
eq("sphere Q nC", sf(C * 1000 * 1e9, 2), 5.6)
eq("Earth C", sf(RE / k), 7.09e-4, 1e-9)
eq("Earth mF", sf(RE / k * 1e3, 2), 0.71)
eq("Earth vs flash", round(RE / k / (120 * uF)), 6)      # about six times

# Series and parallel
eq("par 2+3", 2.0 + 3.0, 5.0)
eq("series 2,3", 1 / (1 / 2.0 + 1 / 3.0), 1.2)
eq("1/C", 1 / 2.0 + 1 / 3.0, 0.833, 0.001)
Qs = 1.2 * 10
eq("Q series", Qs, 12)
eq("V 2.0", Qs / 2.0, 6.0)
eq("V 3.0", Qs / 3.0, 4.0)
eq("V sum", Qs / 2.0 + Qs / 3.0, 10)

# Network: 6.0 in series with (2.0 || 4.0), 12 V
pair = 2.0 + 4.0
Ct = 6.0 * pair / (6.0 + pair)
eq("net pair", pair, 6.0)
eq("net total", Ct, 3.0)
Qt = Ct * 12
eq("net Q", Qt, 36)
Vp = Qt / pair
eq("net Vpair", Vp, 6.0)
eq("net Q 2.0", 2.0 * Vp, 12)
eq("net Q 4.0", 4.0 * Vp, 24)
eq("net sum", 2.0 * Vp + 4.0 * Vp, 36)

# Energy
W = 0.5 * 470 * uF * 12**2
eq("W 470uF", sf(W), 3.38e-2, 1e-9)
eq("W via QV", sf(0.5 * Q * 12), 3.38e-2, 1e-9)
eq("W via Q2/2C", sf(Q**2 / (2 * 470 * uF)), 3.38e-2, 1e-9)

# Flash
Wf = 0.5 * 120 * uF * 300**2
eq("flash W", Wf, 5.4)
eq("flash P", Wf / 1.0e-3, 5.4e3, 1e-6)

# Sharing: 2.0 uF at 6.0 V onto 4.0 uF
Qsh = 2.0 * 6.0
Vsh = Qsh / (2.0 + 4.0)
eq("share Q", Qsh, 12)
eq("share V", Vsh, 2.0)
Eb = 0.5 * 2.0 * 6.0**2
Ea = 0.5 * 6.0 * Vsh**2
eq("share Ebefore uJ", Eb, 36)
eq("share Eafter uJ", Ea, 12)
eq("share lost uJ", Eb - Ea, 24)
eq("share frac", (Eb - Ea) / Eb, 2 / 3, 1e-12)

# Charging through R
eq("supply energy", sf(470 * uF * 144, 3), 6.77e-2, 1e-9)

# V-Q plot: 0.50 mF, 6.0 mC at 12 V
eq("plot V", 6.0 / 0.50, 12)
eq("plot gradient", 12 / 6.0, 2.0)

# Discharge table
eq("e-1", sf(exp(-1)), 0.368)
eq("e-2", sf(exp(-2)), 0.135)
eq("e-3", sf(exp(-3), 3), 0.0498)
eq("e-5", sf(exp(-5), 3), 0.00674)
eq("e-3 pct", sf(exp(-3) * 100, 2), 5.0)
eq("e-2 pct", sf(exp(-2) * 100, 2), 14)
eq("area I0 tau", (9.0 / 50e3) * (50e3 * 100 * uF), 100 * uF * 9.0, 1e-12)

# 100 uF, 50 kOhm, 9.0 V
tau = 50e3 * 100 * uF
eq("tau", tau, 5.0)
eq("I0", 9.0 / 50e3, 1.8e-4, 1e-12)
eq("e-0.6", sf(exp(-0.6)), 0.549)
eq("V at 3 s", sf(9.0 * exp(-3.0 / tau), 2), 4.9)
eq("V at 3 s full", sf(9.0 * exp(-3.0 / tau)), 4.94)
eq("I at 3 s uA", sf(1.8e-4 * exp(-0.6) * 1e6, 3), 98.8)
eq("I via V/R", sf(4.94 / 50e3 * 1e6, 3), 98.8)
eq("t to 2.0 V", sf(tau * log(9.0 / 2.0), 2), 7.5)
eq("ln 4.5", sf(log(4.5), 4), 1.504)
eq("t half", sf(tau * log(2), 2), 3.5)
eq("0.693", sf(log(2), 3), 0.693)

# Graph reading: V0 = 6.0, tau = 10 s, R = 100 kOhm
eq("graph 6/e", sf(6.0 / exp(1), 2), 2.2)
eq("graph 6/e plot", sf(6 * exp(-1), 4), 2.207)
eq("graph thalf", sf(10 * log(2), 2), 6.9)
eq("graph tau from half", sf(6.9 / log(2), 2), 10)
eq("graph C", 10 / 100e3, 1.0e-4, 1e-12)

# ln V plot: 9.0 V, tau 5.0 s
eq("ln 9", sf(log(9), 4), 2.197)
eq("ln V at 5 s", sf(log(9) - 0.2 * 5, 4), 1.197)
eq("gradient", -1 / 5.0, -0.20)
eq("ln 9 plot", sf(log(9), 3), 2.20)
eq("ln V 5 s plot", sf(log(9) - 1.0, 3), 1.20)

# Spot the error
eq("spot RC", 20e3 * 100 * uF, 2.0)
eq("spot wrong", sf(12 * exp(-3.0 / 2.0), 3), 2.68, 0.005)
eq("spot wrong 2sf", sf(12 * exp(-3.0 / 2.0), 2), 2.7)
eq("spot wrong factor", sf(exp(-1.5), 3), 0.223)
eq("spot correct factor", sf(exp(-0.0030 / 2.0), 4), 0.9985)
eq("spot correct V", sf(12 * exp(-0.0030 / 2.0), 2), 12)

# Start easy
eq("se1", sf(220 * uF * 9.0, 3), 1.98e-3, 1e-12)
eq("se1 2sf", sf(220 * uF * 9.0, 2), 2.0e-3, 1e-12)
eq("se2", 94 / 4.7, 20, 1e-9)
eq("se3 series", 6.0 * 3.0 / 9.0, 2.0)
eq("se3 par", 6.0 + 3.0, 9.0)
eq("se4", sf(0.5 * 2200 * uF * 16**2, 2), 0.28)
eq("se5", 100e3 * 4.7 * uF, 0.47, 1e-12)
eq("se6", sf(exp(-2), 3), 0.135)
tau7 = 10e3 * 220 * uF
eq("se7 tau", tau7, 2.2, 1e-12)
eq("se7 V", sf(6.0 / exp(1), 2), 2.2)
eq("se9 Q", 10 * 20, 200)
eq("se9 V", 200 / 20.0, 10)
eq("se9 E before", 0.5 * 10 * uF * 400, 2.0e-3, 1e-12)
eq("se9 E after", 0.5 * 20 * uF * 100, 1.0e-3, 1e-12)

# Exam practice
eq("ep4 pair", 4.0 + 8.0, 12)
eq("ep4 C", 12 * 12 / 24, 6.0)
eq("ep4 Q", 6.0 * 24, 144)
eq("ep4 Vpair", 144 / 12, 12)
eq("ep4 Q4", 4.0 * 12, 48)
eq("ep5 8/e", sf(8.0 / exp(1), 2), 2.9)
eq("ep5 R", 4.0 / (2000 * uF), 2.0e3, 1e-6)
tau6 = 47e3 * 470 * uF
eq("ep6 tau 2sf", sf(tau6, 2), 22)
eq("ep6 tau", sf(tau6, 4), 22.09)
eq("ep6 V", sf(12 * exp(-30 / tau6), 2), 3.1)
# defibrillator
Wd = 0.5 * 40 * uF * (4.0e3) ** 2
eq("defib W", Wd, 320, 1e-6)
taud = 50 * 40 * uF
eq("defib tau", taud, 2.0e-3, 1e-12)
# energy halves when exp(-2t/tau) = 1/2
th = 0.5 * taud * log(2)
eq("defib t", sf(th, 2), 6.9e-4, 1e-12)
eq("defib check", exp(-2 * th / taud), 0.5, 1e-12)
eq("defib P", sf((Wd / 2) / th, 2), 2.3e5, 1)
# ln V data
data = [(0, 10.0), (20, 6.7), (40, 4.5), (60, 3.0), (80, 2.0), (100, 1.35)]
eq("ln 10", sf(log(10.0), 4), 2.303)
eq("ln 1.35", sf(log(1.35), 3), 0.300)
grad = (log(1.35) - log(10.0)) / 100
eq("grad", sf(grad, 3), -2.00e-2, 1e-9)
Cdat = 1 / (100e3 * abs(grad))
eq("C data", sf(Cdat, 2), 5.0e-4, 1e-9)
eq("C unc", 5.0e-4 * 0.05, 0.25e-4, 1e-9)
# data consistent with tau = 50 s
for t, v in data:
    eq(f"data t={t}", sf(10.0 * exp(-t / 50.0), 3 if v == 1.35 else 2), v, 0.051)

# Stretch
eq("st Q1", 4.0 * 10, 40)
eq("st Q2", 6.0 * 5.0, 30)
eq("st Qtot", 70, 70)
eq("st V", 70 / 10.0, 7.0)
Eb2 = 0.5 * 4.0 * 10**2 + 0.5 * 6.0 * 5.0**2
eq("st E before", Eb2, 275)
Ea2 = 0.5 * 10.0 * 7.0**2
eq("st E after", Ea2, 245)
eq("st lost", Eb2 - Ea2, 30)
eq("st half time ratio", (0.5 * log(2)) / log(2), 0.5)

print("ok")
