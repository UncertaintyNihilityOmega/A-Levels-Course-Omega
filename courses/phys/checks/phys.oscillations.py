# checks/phys.oscillations.py: recomputes every number in the Oscillations chapter.
from math import isclose, sqrt, pi, sin, cos, asin, exp, atan, radians

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("warm omega", sf(2 * pi / 0.50), 12.6)
eq("warm dphi", 2 * pi / 4, pi / 2)
eq("warm energy", 0.5 * 50 * 0.10**2, 0.25)

# Guitar string
eq("guitar T", sf(1 / 440), 2.27e-3, 1e-12)
eq("guitar omega", sf(2 * pi * 440), 2760, 1e-6)

# Phase difference example
eq("phase", 2 * pi * 0.10 / 0.80, pi / 4)
eq("phase rad", sf(pi / 4), 0.785)

# Spring example (0.50 kg, 80 N/m)
w = sqrt(80 / 0.50)
eq("spring w", sf(w), 12.6)
eq("spring w unrounded", sf(w, 4), 12.65)
eq("spring T", sf(2 * pi / w), 0.497)
eq("spring f", sf(w / (2 * pi)), 2.01)

# Pendulum
eq("pendulum Earth", sf(2 * pi * sqrt(1.00 / 9.81)), 2.01)
eq("pendulum Moon", sf(2 * pi * sqrt(1.00 / 1.62)), 4.94)

# Worked example: x0 = 4.0 cm, T = 0.40 s
w = 2 * pi / 0.40
eq("w", sf(w), 15.7)
eq("w 4sf", sf(w, 4), 15.71)
eq("v0", sf(w * 0.040), 0.628)
eq("amax", sf(w**2 * 0.040), 9.87)
eq("v at 2cm", sf(w * sqrt(0.040**2 - 0.020**2)), 0.544)
t = asin(0.020 / 0.040) / w
eq("t", sf(t), 0.0333)
eq("t = T/12", t, 0.40 / 12)
eq("first half amplitude T/12 + T/6 = T/4", 0.40 / 12 + 0.40 / 6, 0.40 / 4)

# x = 3.0 sin(8.0 t)
eq("f", sf(8.0 / (2 * pi)), 1.27)
eq("T", sf(2 * pi / 8.0), 0.785)
eq("x(0.5)", sf(3.0 * sin(4.0), 3), -2.27)
eq("sin 4", sf(sin(4.0)), -0.757)
eq("t first", sf(asin(2.0 / 3.0) / 8.0), 0.0912)
eq("8t", sf(asin(2.0 / 3.0)), 0.730)

# Cosine start example
w = 2 * pi * 1.5
eq("w cos", sf(w), 9.42)
eq("wt", sf(w * 0.10), 0.942)
x = 6.0 * cos(w * 0.10)
eq("x cos", sf(x), 3.53)
v = w * sqrt(0.060**2 - (x / 100)**2)
eq("v cos", sf(v), 0.457)
eq("v from derivative", w * 0.060 * sin(w * 0.10), v)

# Graph: a-x
w = 2 * pi / 0.40
eq("a-x gradient", w**2 * 0.040, 9.87, 0.005)
eq("a-x slope per cm", sf(w**2 / 100, 5), 2.4674)
grad = 9.87 / 0.040
eq("gradient", sf(grad), 247)
eq("omega from graph", sf(sqrt(grad)), 15.7)
eq("T from graph", sf(2 * pi / sqrt(grad)), 0.400)
eq("v-t amplitude", sf(w * 0.040), 0.628)
eq("v-t coefficient", sf(w * 0.040, 4), 0.6283)

# Warm plot function values
eq("x-t crest", 4 * sin(5 * pi * 0.1), 4.0)
eq("x-t trough", 4 * sin(5 * pi * 0.3), -4.0)
eq("v-t at 0.2", 0.6283 * cos(5 * pi * 0.2), -0.6283)
eq("a-t at 0.3", -9.870 * sin(5 * pi * 0.3), 9.870)
eq("a-t at 0.1", -9.870 * sin(5 * pi * 0.1), -9.870)

# Energy example
m, w, x0 = 0.20, 10.0, 0.050
E = 0.5 * m * w**2 * x0**2
eq("E", E, 0.025)
Ek = 0.5 * m * w**2 * (x0**2 - 0.030**2)
eq("EK", Ek, 0.016)
eq("EP", E - Ek, 0.009)
eq("EP check", 0.5 * m * w**2 * 0.030**2, 0.009)
eq("v from EK", sqrt(2 * Ek / m), 0.40)
eq("v formula", w * sqrt(x0**2 - 0.030**2), 0.40)
eq("k", m * w**2, 20.0)
# plot constants: E in mJ with x in cm
eq("PE coefficient", 0.5 * m * w**2 * 1e-4 * 1e3, 1.0)
eq("E mJ", E * 1e3, 25.0)
eq("equal at", sf(x0 / sqrt(2) * 100, 2), 3.5)
eq("v at equal ratio", 1 / sqrt(2), 0.7071, 1e-4)

# Lab
k = 4 * pi**2 / 1.58
eq("k lab", sf(k), 25.0)

# Damping
eq("energy ratio", (4.5 / 5.0)**2, 0.81)
eq("lost fraction", 1 - 0.81, 0.19)
eq("amp after 10", sf(5.0 * 0.90**10, 2), 1.7)
eq("energy after 10", sf(0.81**10, 2), 0.12)

# Car resonance
f0 = sqrt(4.0e4 / 1000) / (2 * pi)
eq("f0", sf(f0), 1.01)
eq("v res", sf(f0 * 4.0, 2), 4.0)
eq("v km/h", sf(f0 * 4.0 * 3.6, 2), 14)

# Resonance plot sanity: peak heights and peak positions
A = lambda r, b: 1 / sqrt((1 - r**2)**2 + (b * r)**2)
eq("peak light", A(0.99, 0.2), 5.0, 0.03)
assert max(A(i / 1000, 0.2) for i in range(1, 2500)) < 6.5
assert max(A(i / 1000, 0.6) for i in range(1, 2500)) < max(A(i / 1000, 0.2) for i in range(1, 2500))
r_light = max(range(1, 2500), key=lambda i: A(i / 1000, 0.2)) / 1000
r_heavy = max(range(1, 2500), key=lambda i: A(i / 1000, 0.6)) / 1000
assert r_heavy < r_light < 1.0

# Spot the error 1
w = 2 * pi * 2.0
eq("spot w", sf(w, 4), 12.57)
eq("spot wt", sf(w * 0.30, 4), 3.770)
eq("spot wrong sin", sf(sin(radians(w * 0.30)), 3), 0.0657)
eq("spot wrong x", sf(5.0 * sin(radians(w * 0.30)), 2), 0.33)
eq("spot sin", sf(sin(w * 0.30), 4), -0.5878)
eq("spot right x", sf(5.0 * sin(w * 0.30), 3), -2.94)
eq("quick check sin(3.77)", sf(sin(3.77), 2), -0.59)

# Spot the error 2
eq("spot2 wrong v", 10 * 0.030, 0.30)
eq("spot2 wrong EK", 0.5 * 0.20 * 0.30**2, 0.0090)
eq("spot2 right v", 10 * sqrt(0.050**2 - 0.030**2), 0.40)
eq("spot2 right EK", 0.5 * 0.20 * 0.40**2, 0.016)

# Try questions
eq("try T", 1 / 5.0, 0.20)
eq("try w", sf(2 * pi * 5.0), 31.4)
eq("try spring w", sf(sqrt(200 / 0.80)), 15.8)
eq("try spring T", sf(2 * pi / sqrt(200 / 0.80)), 0.397)
eq("try vmax", 5.0 * 0.020, 0.10)
eq("try amax", 5.0**2 * 0.020, 0.50)
eq("try v", sf(3.0 * sqrt(0.12**2 - 0.060**2), 2), 0.31)
eq("try E", 0.5 * 0.50 * 4.0**2 * 0.10**2, 0.040)
eq("try phase", 2 * pi * 0.125 / (1 / 2.0), pi / 2)

# Exam practice
grad = 2.4 / 0.040
eq("Q2 grad", grad, 60)
eq("Q2 w", sf(sqrt(grad), 2), 7.7)
eq("Q2 T", sf(2 * pi / sqrt(grad), 2), 0.81)
eq("Q2 vmax", sf(sqrt(grad) * 0.060, 2), 0.46)
w = 2 * pi * 2.5
eq("Q3 w", sf(w), 15.7)
eq("Q3 v", sf(w * sqrt(0.060**2 - 0.040**2), 2), 0.70)
w = 2 * pi / 0.40
eq("Q4 vmax", sf(w * 0.030, 2), 0.47)
eq("Q4 zero crossing", 0.40 / 4, 0.10)
w2 = 25 / 0.40
eq("Q5 w2", w2, 62.5)
eq("Q5 E", 0.5 * 0.40 * w2 * 0.080**2, 0.080)
eq("Q5 EK", sf(0.5 * 0.40 * w2 * (0.080**2 - 0.050**2), 2), 0.049)
w2 = 1000 * g * 3.1e-4 / 0.045
eq("Q8 w2", sf(w2), 67.6)
eq("Q8 T", sf(2 * pi / sqrt(w2), 2), 0.76)

# Stretch 1
th = radians(20)
eq("theta", sf(th), 0.349)
eq("sin20", sf(sin(th)), 0.342)
eq("ratio", sf(sin(th) / th), 0.980)
eq("percent", sf((1 - sin(th) / th) * 100, 2), 2.0)
eq("period increase", sf(th**2 / 16 * 100, 2), 0.76)   # about 0.8 %
# Stretch 2
eq("parallel k", 2 * 40, 80)
eq("parallel T", sf(2 * pi * sqrt(0.50 / 80), 2), 0.50)
eq("series k", 40 / 2, 20)
eq("series T", sf(2 * pi * sqrt(0.50 / 20), 2), 0.99)
eq("ratio of periods", (2 * pi * sqrt(0.50 / 20)) / (2 * pi * sqrt(0.50 / 80)), 2.0)

print("ok")
