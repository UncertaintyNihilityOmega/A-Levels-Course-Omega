# checks/phys.dc.py: recomputes every number in the D.C. circuits chapter.
from math import isclose, sqrt, exp

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def par(*rs):
    return 1 / sum(1 / r for r in rs)

# Warm-up
eq("warm Q", 0.25 * 2.0 * 60, 30)
eq("warm R", 12 / 0.40, 30)
eq("warm P", 12 * 0.40, 4.8)

# e.m.f. example
eq("W = QE", 15 * 9.0, 135)
eq("W 2sf", sf(135, 2), 140)

# Internal resistance example 1
I = 1.50 / (2.5 + 0.50)
eq("I", I, 0.50)
eq("V = IR", I * 2.5, 1.25)
eq("V = E - Ir", 1.50 - I * 0.50, 1.25)
eq("I^2 r", I**2 * 0.50, 0.125)
eq("I^2 R", I**2 * 2.5, 0.625)
eq("fraction wasted", 0.125 / (0.125 + 0.625), 1 / 6)

# Car battery example (150 A)
eq("lost volts", 150 * 0.020, 3.0)
eq("terminal", 12.0 - 150 * 0.020, 9.0)

# Graph example: V = 1.55 - 0.80 I
eq("graph point", 1.55 - 0.8 * 1.00, 0.75)
eq("gradient", (0.75 - 1.55) / (1.00 - 0), -0.80)

# Two readings example
I1, I2 = 2.4 / 4.0, 2.7 / 9.0
eq("I1", I1, 0.60); eq("I2", I2, 0.30)
r = (2.7 - 2.4) / (I1 - I2)
eq("r", r, 1.0)
eq("E", 2.4 + I1 * r, 3.0)

# Kirchhoff two-loop example: 4I1 + 2I2 = 12, 2I1 + 4I2 = 9
det = 4 * 4 - 2 * 2
i1 = (12 * 4 - 2 * 9) / det
i2 = (4 * 9 - 2 * 12) / det
eq("I1", i1, 2.5); eq("I2", i2, 1.0); eq("I3", i1 + i2, 3.5)
eq("left loop", 2.0 * i1 + 2.0 * (i1 + i2), 12)
eq("right loop", 2.0 * i2 + 2.0 * (i1 + i2), 9.0)
eq("outer loop", 2.0 * i1 - 2.0 * i2, 12 - 9.0)

# Series/parallel example
rp = par(3.0, 6.0)
eq("parallel pair", rp, 2.0)
eq("total", 6.0 + rp, 8.0)
Is = 12 / (6.0 + rp)
eq("supply I", Is, 1.5)
eq("V pair", Is * rp, 3.0)
eq("I in 3", 3.0 / 3.0, 1.0); eq("I in 6", 3.0 / 6.0, 0.50)

# Potential dividers
eq("divider 9 V", 5.0 / (10 + 5.0) * 9.0, 3.0)
eq("thermistor 20C", 2.0 / (4.0 + 2.0) * 6.0, 2.0)
eq("thermistor 60C", 2.0 / (1.0 + 2.0) * 6.0, 4.0)
eq("LDR dark", sf(100 / (10 + 100) * 5.0, 2), 4.5)
eq("LDR light", sf(1.0 / (10 + 1.0) * 5.0, 2), 0.45)

# Widget model sanity (thermistor 10 kOhm at 25 C, LDR 100 kOhm at 10 lux)
eq("widget thermistor 25C", 10 * exp(3950 * (1 / 298.15 - 1 / 298.15)), 10)

# Potentiometer
eq("E2", sf(1.02 * 74.0 / 51.0), 1.48)

# Spot the error
I = 6.0 / (2.5 + 0.50)
eq("spot I", I, 2.0); eq("spot lost", I * 0.50, 1.0)
eq("spot wrong", 6.0 + 1.0, 7.0); eq("spot right", 6.0 - I * 0.50, 5.0); eq("spot IR", I * 2.5, 5.0)

# Try questions
eq("try junction", 2.5 - 0.8, 1.7)
eq("try series", 47 + 33 + 20, 100)
eq("try parallel", par(12, 12, 12), 4.0)
eq("try terminal", 1.5 - 0.50 * 0.30, 1.35)
eq("try divider", 2.0 / (1.0 + 2.0) * 12, 8.0)
eq("try divider other", 12 - 8.0, 4.0)
eq("try pair", par(6.0, 6.0), 3.0)
eq("try I", 12 / (3.0 + 3.0), 2.0)
eq("try Vpair", 2.0 * 3.0, 6.0)
eq("try r", (3.0 - 2.6) / 0.40, 1.0)
eq("try short", 3.0 / 1.0, 3.0)

# Exam practice
eq("Q2 pair", par(20, 30), 12)
eq("Q2 I", 6.0 / (12 + 8.0), 0.30)
eq("Q3 r", (12 - 10.8) / 3.0, 0.40)
eq("Q3 P", 3.0**2 * 0.40, 3.6)
eq("Q4 Vout", 1.5 / (3.5 + 1.5) * 5.0, 1.5)
eq("Q5 I", (9.0 - 3.0) / (2.0 + 4.0), 1.0)
eq("Q6 E", 2.0 / 1.00 * 0.725, 1.45)
eq("Q7 V", 12.0 - 160 * 0.025, 8.0)
eq("Q7 P", 8.0 * 160, 1280)
eq("Q7 W", 160**2 * 0.025 * 2.5, 1600)
VAB = 1.5 * 1.00 / 0.750
eq("Q8 VAB", VAB, 2.0)
Iw = VAB / 5.0
eq("Q8 I", Iw, 0.40)
eq("Q8 R", (4.0 - VAB) / Iw, 5.0)
eq("Q8 balance without R", 1.5 / 4.0 * 100, 37.5)

# Stretch 1: maximum power
E, r = 6.0, 2.0
P = lambda R: E**2 * R / (R + r)**2
eq("Pmax", E**2 / (4 * r), 4.5)
eq("Pmax at R=r", P(r), 4.5)
assert P(r) > P(1.9) and P(r) > P(2.1)
eq("EI at max", E * E / (2 * r), 9.0)
eq("efficiency", 4.5 / 9.0, 0.50)

# Stretch 2: voltmeter loading
rp = par(100, 100)
eq("loaded pair", rp, 50)
eq("loaded reading", rp / (100 + rp) * 12.0, 4.0)
eq("target", 0.99 * 6.0, 5.94)
Rp = 5.94 * 100 / (12.0 - 5.94)
eq("Rp", sf(Rp), 98.0)
RV = 1 / (1 / Rp - 1 / 100)
eq("RV", sf(RV), 4950)

# Quiz
eq("quiz terminal", 3.0 * 2.0 / (3.0 + 1.0), 1.5)
eq("quiz lost", 1.0 * 2.0 / (3.0 + 1.0), 0.50)
eq("quiz 1.5R", 0.5 + 1, 1.5)
eq("quiz 2R/3", par(1, 2), 2 / 3)

print("ok")
