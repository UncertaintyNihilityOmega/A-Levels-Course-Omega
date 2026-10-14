# checks/phys.electricity.py: recomputes every number in the Electricity chapter.
from math import isclose, sqrt, pi, exp

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

e = 1.60e-19
me = 9.11e-31
n_cu = 8.5e28

# Warm-up
eq("warm P", 360e3 / (3.0 * 60), 2000)
eq("warm area", sf(pi * (0.25e-3) ** 2, 3), 1.96e-7, 1e-12)

# Charge example
eq("t", 5.0 * 60, 300)
eq("Q", 3.0 * 300, 900)
eq("N unrounded", 900 / e, 5.625e21, 1e17)
eq("N 2sf", sf(900 / e, 2), 5.6e21, 1e17)

# Lightning
eq("lightning", 15 / 0.20e-3, 7.5e4)

# Quantisation
eq("3e", 4.8 / 1.60, 3)
eq("4e", 6.4 / 1.60, 4)
eq("1.5e", 2.4 / 1.60, 1.5)

# Drift speed in copper
A = pi * (0.50e-3) ** 2
eq("A", sf(A, 3), 7.85e-7, 1e-12)
v = 2.0 / (A * n_cu * e)
eq("v copper", sf(v, 2), 1.9e-4, 1e-9)
# Thin wire
Ath = pi * (0.25e-3) ** 2
vth = 2.0 / (Ath * n_cu * e)
eq("thin wire", sf(vth, 2), 7.5e-4, 1e-8)
eq("ratio", vth / v, 4.0, 1e-9)

# Electron gun
W = e * 2500
eq("W gun", W, 4.0e-16, 1e-20)
vg = sqrt(2 * 4.0e-16 / me)
eq("v gun", sf(vg, 2), 3.0e7, 1e5)
eq("fraction of c", sf(vg / 3.00e8, 1), 0.1)

# Kettle
I = 2000 / 230
eq("kettle I", sf(I, 2), 8.7)
eq("kettle R", sf(230 / I, 2), 26)
eq("kettle R2", 230 ** 2 / 2000, 26.45, 1e-9)
eq("kettle W", 2000 * 180, 3.6e5)

# Lamp 12 V 36 W
eq("lamp I", 36 / 12, 3.0)
eq("lamp R", 12 / 3.0, 4.0)
eq("lamp cold I", 12 / 0.40, 30)
eq("lamp ratio", (12 / 0.40) / 3.0, 10)

# kWh
eq("kWh", 3.0 * 5.0, 15)
eq("cost p", 15 * 30, 450)
eq("kWh J", 15 * 3.6e6, 5.4e7)
eq("kWh in J", 1000 * 3600, 3.6e6)

# Resistance
eq("R 25", 6.0 / 0.24, 25)
eq("I 4.5 V", 4.5 / 25, 0.18)
eq("frac", 4.5 / 6.0 * 0.24, 0.18)

# Lamp characteristic readings (model I = 0.25 (V/6)^0.6)
model = lambda V: 0.25 * (V / 6) ** 0.6
eq("model 2 V", sf(model(2.0), 2), 0.13, 1e-9)
eq("lamp R 2 V", sf(2.0 / 0.13, 2), 15)
eq("lamp R 6 V", 6.0 / 0.25, 24)
eq("rise", sf((24 - 15.4) / 15.4 * 100, 1), 60, 1e-9)
eq("tangent gradient", 0.6 * 0.25 / 6, 0.025, 1e-12)
eq("wrong R", 1 / 0.025, 40)

# Diode
eq("diode f1", 0.60 / 2.0e-3, 300)
eq("diode f2", sf(0.75 / 40e-3, 2), 19)
eq("diode f2 raw", 0.75 / 40e-3, 18.75)
eq("diode rev", 5.0 / 0.10e-6, 5.0e7, 1)
eq("ratio range", 5.0e7 / 18.75, 2.67e6, 1e4)

# Resistivity example
rho = 1.1e-6
A = pi * (0.15e-3) ** 2
eq("A nichrome", sf(A, 3), 7.07e-8, 1e-12)
R = rho * 1.5 / A
eq("R nichrome", sf(R, 2), 23)
eq("R x4", sf(4 * R, 2), 93)

# Resistivity graph
grad = (17.8 - 3.6) / (1.000 - 0.200)
eq("gradient", grad, 17.75, 1e-9)
eq("gradient 3sf", sf(grad, 3), 17.8, 1e-9)
Ad = pi * (0.14e-3) ** 2
eq("A wire", sf(Ad, 3), 6.16e-8, 1e-12)
eq("rho graph", sf(grad * Ad, 2), 1.1e-6, 1e-12)
# line consistency: line 17.75 x + 0.05 passes through both points
eq("line pt1", 17.75 * 0.2 + 0.05, 3.6, 1e-9)
eq("line pt2", 17.75 * 1.0 + 0.05, 17.8, 1e-9)
# Percentage uncertainty from d
eq("d unc", sf(0.01 / 0.28 * 100, 2), 3.6)
eq("rho unc", sf(2 * 0.01 / 0.28 * 100, 1), 7)

# Thermistor
R_th = lambda T: 10 * exp(3950 * (1 / (T + 273.15) - 1 / 298.15))
eq("th 25", R_th(25), 10, 1e-9)
eq("th 50", sf(R_th(50), 3), 3.59, 1e-9)
eq("th 100", sf(R_th(100), 2), 0.70, 1e-9)
eq("I 25", 5.0 / 10e3 * 1e3, 0.50)
eq("I 100", sf(5.0 / 0.70e3 * 1e3, 2), 7.1)
eq("ratio I", sf(7.14 / 0.50, 2), 14)
eq("ratio R", sf(10 / 0.70, 2), 14)

# LDR
R_ldr = lambda x: 100 * (10 / x) ** 0.8
eq("ldr 10", R_ldr(10), 100, 1e-9)
eq("ldr 100", sf(R_ldr(100), 3), 15.8, 1e-9)
eq("ldr 50", sf(R_ldr(50), 3), 27.6, 1e-9)

# Easy questions
eq("easy Q", 4.0e-3 * 5.0, 2.0e-2, 1e-12)
eq("easy N", sf(0.50 / e, 2), 3.1e18, 1e15)
eq("easy I", sf(12 / 330, 2), 0.036, 1e-9)
eq("easy P", sf(12 * 12 / 330, 2), 0.44)
eq("easy Q2", 2.5 * 600, 1500)
eq("easy W", 1500 * 6.0, 9000)
eq("easy R", 4.0 * 3.0 / 2.0, 6.0)
eq("lamp 230 R", sf(230 ** 2 / 60, 2), 880)
eq("lamp 230 I", sf(60 / 230, 2), 0.26)
Ac = pi * (0.30e-3) ** 2
eq("Cu A", sf(Ac, 3), 2.83e-7, 1e-12)
eq("Cu R", sf(1.7e-8 * 2.0 / Ac, 2), 0.12)
eq("MJ", 3.6e6 / 3.6e6, 1.0)

# Exam practice
eq("ex charge", 0.80 * 120, 96)
eq("ex N", sf(96 / e, 2), 6.0e20, 1e17)
eq("ex diode f", sf(0.70 / 12e-3, 2), 58)
eq("ex diode r", 4.0 / 0.20e-6, 2.0e7, 1)
Ay = pi * (0.30e-3) ** 2
eq("ex Y", sf(3.0 / (Ay * n_cu * e), 2), 7.8e-4, 1e-8)
eq("ex Y area ratio", (1.2 / 0.60) ** 2, 4)
# heater
eq("heater I", sf(1500 / 230, 2), 6.5)
Rh = 230 ** 2 / 1500
eq("heater R", sf(Rh, 2), 35)
Ah = pi * (0.20e-3) ** 2
eq("heater A", sf(Ah, 3), 1.26e-7, 1e-12)
eq("heater L", sf(Rh * Ah / 1.1e-6, 2), 4.0)
eq("heater L from rounded R", sf(35.3 * Ah / 1.1e-6, 2), 4.0)

# Stretch
eq("stretch", 1.1 ** 2, 1.21, 1e-12)
vcu = 1.0e-3 / (2.0e-6 * n_cu * e)
vsm = 1.0e-3 / (2.0e-6 * 2.0e22 * e)
eq("v cu", sf(vcu, 2), 3.7e-8, 1e-12)
eq("v semi", sf(vsm, 2), 0.16, 1e-9)
eq("v semi 3sf", sf(vsm, 3), 0.156, 1e-9)
eq("ratio", 8.5e28 / 2.0e22, 4.25e6, 1)
eq("ratio 2sf (4.25 rounds half up)", 8.5e28 / 2.0e22, 4.3e6, 0.05e6 + 1)
eq("ratio unrounded speeds", vsm / vcu, 4.25e6, 1e3)

# Area under the I-t graph (REVIEW P5-P6)
eq("I-t area", 0.5 * 10 * 4.0 + 5.0 * 4.0, 40)
eq("I-t average", sf(40 / 15, 2), 2.7)
eq("I-t plot at 10 s", (0.4 * 10 + 4 - abs(0.4 * 10 - 4)) / 2, 4.0)
eq("I-t plot at 5 s", (0.4 * 5 + 4 - abs(0.4 * 5 - 4)) / 2, 2.0)
eq("I-t area triangle", 0.5 * 30 * 6.0e-3, 0.090, 1e-12)

print("ok")
