# checks/phys.ac.py: recomputes every number in the Alternating currents chapter.
from math import isclose, sqrt, exp, sin, asin, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# Warm-up
eq("warm tau", 2.0e3 * 470e-6, 0.94, 1e-12)
eq("warm P", 12**2 / 6.0, 24)
eq("warm omega", sf(2 * pi * 50), 314)

# Mains: V = 325 sin(100 pi t)
eq("f", 100 * pi / (2 * pi), 50)
eq("T", 1 / 50, 0.020)
eq("rms", sf(325 / sqrt(2), 3), 230)
eq("V at 2.5 ms", sf(325 * sin(100 * pi * 0.0025), 3), 230)
eq("pi/4", 100 * pi * 0.0025, pi / 4, 1e-12)
wt = asin(200 / 325)
eq("wt", sf(wt, 4), 0.6629)
eq("t200 ms", sf(wt / (100 * pi) * 1000, 2), 2.1)
eq("230 peak", sf(230 * sqrt(2), 3), 325)

# Oscilloscope example
eq("pp", 6.0 * 2.0, 12); eq("V0", 6.0 * 2.0 / 2, 6.0)
eq("T cro", 4.0 * 5.0, 20); eq("f cro", 1 / 0.020, 50)

# Heater 25 ohm, 325 V peak
P0 = 325**2 / 25
eq("P0", P0, 4225); eq("P0 2sf", sf(P0, 2), 4200); eq("mean", P0 / 2, 2112.5); eq("mean 2sf", sf(P0 / 2, 2), 2100)

# Lamp 60 W, 230 V
Irms = 60 / 230
eq("lamp I", sf(Irms, 3), 0.261)
eq("lamp I0", sf(Irms * sqrt(2), 2), 0.37)
eq("lamp I0 raw", sf(Irms * sqrt(2), 4), 0.3689)
eq("lamp peak P", 2 * 60, 120)
eq("lamp R", sf(230**2 / 60, 2), 880)
eq("lamp check", sf(Irms * sqrt(2) * 325, 3), 120)   # 230*sqrt(2) = 325.27 -> 120.0

# 9.0 V peak
Vr = 9.0 / sqrt(2)
eq("9 V rms", sf(Vr, 2), 6.4)
eq("ratio", sf((9.0 / 6.36)**2, 2), 2.0)
eq("6.36", sf(Vr, 3), 6.36)

# Bridge rectifier
eq("pulses", 2 * 50, 100)
eq("peak out", 12.0 - 2 * 0.70, 10.6)

# Smoothing example 470 uF, 2.0 kOhm, 12 V peak, full wave
RC = 2.0e3 * 470e-6
eq("RC", RC, 0.94, 1e-12)
dV = 12 * 0.010 / RC
eq("dV", sf(dV, 2), 0.13)
eq("dV pct", sf(dV / 12 * 100, 2), 1.1)
dVh = 12 * 0.020 / RC
eq("dV half", sf(dVh, 2), 0.26)
eq("dV half pct", sf(dVh / 12 * 100, 2), 2.1)
eq("exact full", sf(12 * (1 - exp(-0.010 / RC)), 2), 0.13)

# Radio: 0.040 A, half-wave, ripple 0.30 V
dQ = 0.040 * 0.020
eq("radio dQ", dQ, 8.0e-4, 1e-12)
C = dQ / 0.30
eq("radio C", sf(C, 2), 2.7e-3, 1e-9)
eq("radio C full", sf(0.040 * 0.010 / 0.30, 2), 1.3e-3, 1e-9)

# Spot the error
eq("spot wrong", sf(80 / sqrt(2), 2), 57)
eq("spot right", 80 / 2, 40)

# Start easy
eq("e1", 1 / 0.025, 40)
eq("e2 f", 200 * pi / (2 * pi), 100); eq("e2 T", 1 / 100, 0.010)
eq("e3", sf(170 / sqrt(2), 3), 120)
eq("e4", 0.5 * 3.0**2 * 10, 45)
eq("e5 I", sf(2000 / 230, 2), 8.7); eq("e5 R", sf(230**2 / 2000, 2), 26)
eq("e7 pulses", 2 * 50, 100)
eq("e8 RC", 500 * 1000e-6, 0.50, 1e-12); eq("e8 dV", 10 * 0.010 / 0.50, 0.20, 1e-12)
eq("e9", 15.0 - 2 * 0.70, 13.6)

# Exam practice
eq("Q2 pp", 5.6 * 5.0, 28); eq("Q2 V0", 5.6 * 5.0 / 2, 14)
eq("Q2 T", 5.0 * 2.0, 10); eq("Q2 f", 1 / 0.010, 100)
eq("Q2 rms", sf(14 / sqrt(2), 2), 9.9)
eq("Q3 P0", 2.0**2 * 15, 60); eq("Q3 mean", 60 / 2, 30)
I = 9.0 / 150
eq("Q7 I", I, 0.060, 1e-12)
eq("Q7 dQ", I * 0.010, 6.0e-4, 1e-12)
eq("Q7 C", 6.0e-4 / 0.50, 1.2e-3, 1e-12)
eq("Q7 1000uF", 6.0e-4 / 1.0e-3, 0.60, 1e-12)
eq("Q8 P", 12**2 / 8.0, 18)
eq("Q8 V0", sf(sqrt(2) * 12, 2), 17)
eq("Q8 P0", 2 * 18, 36)
eq("Q8 P0 check", sf((sqrt(2) * 12)**2 / 8.0, 3), 36.0)

# Stretch 1: half-wave rms
eq("S1 V rms", 325 / 2, 162.5)
eq("S1 P", sf(162.5**2 / 100, 3), 264)
eq("S1 full", sf(230**2 / 100, 3), 529)
eq("S1 half of full", 162.5**2 / 100 / (230**2 / 100), 0.5, 2e-3)   # 325 vs 230*sqrt2 = 325.27
# numeric mean-square check for the half-wave rectified sine
N = 100000
ms = sum(max(sin(2 * pi * k / N), 0)**2 for k in range(N)) / N
eq("S1 mean square", ms, 0.25, 1e-6)
ms_full = sum(sin(2 * pi * k / N)**2 for k in range(N)) / N
eq("sin2 mean", ms_full, 0.5, 1e-6)
# Stretch 2
eq("S2 P", 20**2 / (2 * 40), 5.0)

print("ok")
