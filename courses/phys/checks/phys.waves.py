# checks/phys.waves.py: recomputes every number in the Waves chapter.
from math import isclose, sqrt, pi, cos, sin, radians

c = 3.00e8

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# Warm-up
eq("warm v", 45 / 3.0, 15)
eq("warm nm", 650e-9, 6.50e-7, 1e-15)
eq("warm E", 60 * 2.0 * 60, 7200)

# Period and frequency
eq("T 50 Hz", 1 / 50, 0.020)
eq("T 5 ms", 1 / 5.0e-3, 200)

# Rope wave: A 4.0 cm, lambda 2.0 m, f 0.50 Hz. y = 4 sin(pi x); particle at 0.5 m: y = 4 cos(pi t)
lam, f = 2.0, 0.50
eq("rope T", 1 / f, 2.0)
eq("rope v", lam / (1 / f), 1.0)
eq("rope v = f lambda", f * lam, 1.0)
eq("graph crest x", 0.5 + lam, 2.5)
eq("graph1 y(0.5)", 4 * sin(pi * 0.5), 4.0)
eq("graph1 y(2.5)", 4 * sin(pi * 2.5), 4.0)
eq("graph1 y(1.5)", 4 * sin(pi * 1.5), -4.0)
eq("graph2 y(0)", 4 * cos(0), 4.0)
eq("graph2 y(2)", 4 * cos(pi * 2), 4.0)
eq("graph2 y(1)", 4 * cos(pi), -4.0)
eq("graph2 is the particle at 0.5 m", 4 * sin(pi * 0.5 - pi * 1.0), -4.0)   # y(x=0.5, t=1) trough
eq("peak to peak", 2 * 4.0, 8.0)
eq("1.5 m vs 0.5 m", 1.5 - 0.5, 1.0)
eq("phase rope", 1.0 / lam * 360, 180)

# Phase difference example
eq("phase frac", 0.30 / 1.2, 0.25)
eq("phase deg", 0.30 / 1.2 * 360, 90)
eq("phase rad", sf(2 * pi * 0.30 / 1.2), 1.57)
eq("phase rad = pi/2", 2 * pi * 0.30 / 1.2, pi / 2)

# Wave equation examples
eq("radio", sf(c / 98.5e6), 3.05)
eq("sound 256", sf(340 / 256), 1.33)
eq("helium", sf(1000 / 256, 2), 3.9)

# Oscilloscope
T = 2.5 * 2.0e-3
eq("cro T", T, 5.0e-3)
eq("cro f", 1 / T, 200)
eq("cro ptp", 3.0 * 0.50, 1.5)
eq("cro amp", 3.0 * 0.50 / 2, 0.75)
eq("cro 1.0 ms/cm", T / 1.0e-3, 5.0)
eq("cro cycles", 10 / 5.0, 2)

# Intensity
A = pi * (1.0e-3) ** 2
eq("laser area", sf(A), 3.14e-6, 1e-8)
eq("laser I", sf(5.0e-3 / A, 2), 1.6e3)
eq("I 2 m", sf(60 / (4 * pi * 2.0**2)), 1.19)
eq("I 4 m", sf(60 / (4 * pi * 4.0**2)), 0.298)
eq("I ratio", (60 / (4 * pi * 16)) / (60 / (4 * pi * 4)), 0.25)
eq("A ratio", sqrt(0.25), 0.50)
eq("amp x3", 3**2, 9)

# Longitudinal example
eq("spring v", 15 * 0.40, 6.0)
eq("spring sep", 0.60 / 0.40, 1.5)
eq("spring phase", 1.5 * 360, 540)
eq("spring phase mod", 540 % 360, 180)

# Doppler
eq("amb app", sf(700 * 340 / (340 - 25), 3), 756)
eq("amb rec", sf(700 * 340 / (340 + 25), 3), 652)
eq("train", 340 - 480 * 340 / 510, 20, 1e-9)
eq("spot wrong", sf(700 * 340 / (340 + 25), 3), 652)
eq("spot right", sf(700 * 340 / (340 - 25), 3), 756)
# Doppler figure: source speed 0.4 v, wavefront gaps
eq("fig gap ahead", 22 - 0.4 * 22, 13.2, 1e-9)
eq("fig gap behind", 22 + 0.4 * 22, 30.8, 1e-9)

# EM spectrum
eq("f 400", c / 400e-9, 7.50e14, 1e6)
eq("f 700", sf(c / 700e-9), 4.29e14, 1e9)
eq("oven", sf(c / 2.45e9), 0.122)
eq("fig visible x", 20 + (4 + 6.155) * 30 - 20 - 0, 304.65, 0.01)   # log10(7e-7) = -6.155
from math import log10
eq("log 7e-7", round(log10(7e-7), 3), -6.155)
eq("log 4e-7", round(log10(4e-7), 3), -6.398)
x_ir = 20 + (4 - log10(7e-7)) * 30
x_vis = 20 + (4 - log10(4e-7)) * 30
eq("fig IR end", x_ir, 324.6, 0.1)
eq("fig vis end", x_vis, 331.9, 0.1)
eq("fig UV end", 20 + (4 + 8) * 30, 380)
eq("fig X end", 20 + (4 + 13) * 30, 530)
eq("fig gamma start", 20 + (4 + 11) * 30, 470)

# Malus
eq("malus 30", 8.0 * cos(radians(30)) ** 2, 6.0, 1e-9)
eq("cos2 30", sf(cos(radians(30)) ** 2), 0.75)
eq("three filters 45", cos(radians(45)) ** 2, 0.5)
eq("three filters", cos(radians(45)) ** 4, 0.25)
eq("crossed", cos(radians(90)) ** 2, 0.0, 1e-30)
i1 = 12 * cos(radians(20)) ** 2
eq("malus2 I1", sf(i1), 10.6)
eq("malus2 I2", sf(i1 * cos(radians(50)) ** 2, 2), 4.4)
eq("cos2 50", sf(cos(radians(50)) ** 2), 0.413)

# Try: start easy
eq("t1", 5.0 * 0.30, 1.5)
eq("t2", 1 / 50 * 1000, 20)
eq("t3 frac", 0.40 / 0.60, 2 / 3)
eq("t3 deg", 0.40 / 0.60 * 360, 240)
eq("t3 rad", sf(0.40 / 0.60 * 2 * pi), 4.19)
eq("t4 T", 4.0 * 5.0, 20)
eq("t4 f", 1 / 20e-3, 50)
eq("t5", 500 * 0.40, 200)
eq("t7", sf(1000 * 340 / (340 + 30)), 919)
eq("t8", sf(c / 450e-9), 6.67e14, 1e10)
eq("t9", 10 * cos(radians(60)) ** 2, 2.5)

# Exam practice
eq("Q3 I", 0.40 / 4, 0.10)
eq("Q3 ratio", sqrt(0.10 / 0.40), 0.50)
Tq = 4.0 * 0.50e-3
eq("Q4 T", Tq, 2.0e-3)
eq("Q4 f", 1 / Tq, 500)
eq("Q4 lambda", 340 / 500, 0.68)
j1 = 6.0 * cos(radians(40)) ** 2
eq("Q5 I1", sf(j1), 3.52)
eq("Q5 I2", sf(j1 * cos(radians(50)) ** 2, 2), 1.5)
eq("Q6 lambda", sf(c / 94.6e6), 3.17)
# Q7 racing car
r = 1380 / 1020
eq("Q7 ratio", r, 23 / 17)
us = 340 * (r - 1) / (r + 1)
eq("Q7 vs", us, 51, 1e-9)
eq("Q7 40 vs", 40 * us, 6 * 340)
fs = 1380 * (340 - us) / 340
eq("Q7 fs", fs, 1173, 1e-9)
eq("Q7 fs check", 1020 * (340 + us) / 340, 1173, 1e-9)
# Q8
eq("Q8 lambda", 0.75 - 0.15, 0.60)
eq("Q8 f", 1 / 0.020, 50)
eq("Q8 v", 50 * 0.60, 30)
eq("Q8 sep", 0.45 - 0.30, 0.15)
eq("Q8 quarter", 0.60 / 4, 0.15)
eq("Q8 crest", sin(2 * pi * 0.15 / 0.60), 1.0)
eq("Q8 trough", sin(2 * pi * 0.45 / 0.60), -1.0)
eq("Q8 M zero", sin(2 * pi * 0.30 / 0.60), 0.0, 1e-12)

# Stretch 1
eq("S1 fo", sf(50 * 340 / (340 - 6.0), 3), 50.9)
shift = 50 * 340 / (340 - 6.0) - 50
eq("S1 shift", sf(shift, 3), 0.898)
eq("S1 frac", sf(shift / 50 * 100, 3), 1.80)
eq("S1 vs/v", sf(6.0 / 340 * 100, 3), 1.76)
# Stretch 2
eq("S2 ratio", sqrt(4.0 / 9.0), 2 / 3)
eq("S2 amp", 2 / 3 * 1.2, 0.80, 1e-12)

# Quiz
eq("quiz quarter", 0.25 * 360, 90)
eq("quiz amp x2", 2**2, 4)
eq("quiz 45", cos(radians(45)) ** 2, 0.5)

print("ok")
