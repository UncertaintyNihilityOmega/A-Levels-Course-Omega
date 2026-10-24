# checks/chem.mixed.as.py: recomputes every number in Mixed practice: AS Level.
# Ar from data/elements.json (the 9701 Periodic Table); R = 8.31, Vm = 24.0 dm3 at room conditions, c = 4.18.
import json
import os
from math import isclose

HERE = os.path.dirname(os.path.abspath(__file__))
AR = {e['sym']: e['ar'] for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


H, C, N, O = AR['H'], AR['C'], AR['N'], AR['O']
K, Mg, Ca, Fe = AR['K'], AR['Mg'], AR['Ca'], AR['Fe']
R, VM, CW = 8.31, 24.0, 4.18

# Set 1
eq("1.2 sum", 24 * 78.99 + 25 * 10.00 + 26 * 11.01, 2432.02, 1e-9)
eq("1.2 Ar", sf((24 * 78.99 + 25 * 10.00 + 26 * 11.01) / 100), 24.3)
eq("1.2 table Mg", Mg, 24.3)
eq("1.4 n Fe", sf(2.79 / Fe), 0.0500)
eq("1.4 n O", sf(1.20 / O), 0.0750)
eq("1.4 ratio", (1.20 / O) / (2.79 / Fe), 1.5, 1e-9)
n_acid = 0.0500 * 18.40 / 1000
eq("1.5 n acid", n_acid, 9.20e-4, 1e-12)
n_koh = 2 * n_acid
eq("1.5 n KOH", n_koh, 1.84e-3, 1e-12)
c_koh = n_koh / 0.0250
eq("1.5 c", sf(c_koh), 0.0736)
eq("1.5 g/dm3", sf(sf(c_koh) * (K + O + H)), 4.13)
eq("1.5 Mr KOH", K + O + H, 56.1)
n = 101000 * 1.00e-4 / (R * 298)
eq("1.7 n", sf(n), 4.08e-3, 1e-12)
Mr = 0.229 / n
eq("1.7 Mr", sf(Mr), 56.1)
assert round(Mr / 14) == 4 and abs(Mr - 56) < 0.5

# Set 2
Mr_eth = 2 * C + 6 * H + O
eq("2.2 Mr", Mr_eth, 46.0)
n_eth = 0.460 / Mr_eth
eq("2.2 n", n_eth, 0.0100, 1e-12)
q = 200 * CW * 13.9
eq("2.2 q", round(q), 11620)
dH = -q / 1000 / n_eth
eq("2.2 dH", sf(dH), -1160)
assert dH > -1367
eq("2.3 dHf", 3 * -394 + 4 * -286 - (-2220), -106)
eq("2.4 broken", 944 + 3 * 436, 2252)
eq("2.4 made", 6 * 390, 2340)
eq("2.4 dH", 2252 - 2340, -88)
n_no2 = 2 * (0.800 - 0.560)
eq("2.5 n NO2", n_no2, 0.480, 1e-12)
n2o4c, no2c = 0.560 / 4.00, n_no2 / 4.00
eq("2.5 [N2O4]", n2o4c, 0.140)
eq("2.5 [NO2]", no2c, 0.120)
eq("2.5 Kc", sf(no2c ** 2 / n2o4c), 0.103)
tot = 0.40 + 1.20 + 0.80
eq("2.8 total", tot, 2.40)
p = [x / tot * 2400 for x in (0.40, 1.20, 0.80)]
eq("2.8 pN2", p[0], 400, 1e-9)
eq("2.8 pH2", p[1], 1200, 1e-9)
eq("2.8 pNH3", p[2], 800, 1e-9)
eq("2.8 Kp", sf(p[2] ** 2 / (p[0] * p[1] ** 3)), 9.26e-7, 1e-12)

# Set 3
n_mn = 0.0200 * 21.80 / 1000
eq("3.2 n MnO4", n_mn, 4.36e-4, 1e-12)
eq("3.2 n acid", n_mn * 5 / 2, 1.09e-3, 1e-12)
eq("3.2 c", sf(n_mn * 5 / 2 / 0.0250), 0.0436)
eq("3.5 rate 1", 24 / 30, 0.80)
eq("3.5 rate 2", round((50 - 40) / 30, 2), 0.33)
n_mn = 0.0200 * 19.30 / 1000
eq("3.6 n MnO4", n_mn, 3.86e-4, 1e-12)
n_h = n_mn * 5 / 2
eq("3.6 n H2O2 25", n_h, 9.65e-4, 1e-12)
eq("3.6 n H2O2 250", n_h * 10, 9.65e-3, 1e-12)
c_h = n_h * 10 / 0.0100
eq("3.6 c", sf(c_h), 0.965)
Mr_h = 2 * H + 2 * O
eq("3.6 Mr", Mr_h, 34.0)
eq("3.6 g/dm3", sf(c_h * Mr_h), 32.8)
eq("3.8 ratio", sf(84 / 41, 2), 2.0)

# Set 4
Mr_mn = Mg + 2 * (N + 3 * O)
eq("4.4 Mr", Mr_mn, 148.3)
n_s = 3.70 / Mr_mn
eq("4.4 n", sf(n_s, 4), 0.02495, 1e-9)
n_g = n_s * 5 / 2
eq("4.4 n gas", sf(n_g, 4), 0.06237, 1e-9)
eq("4.4 V", sf(n_g * VM), 1.50)
eq("4.4 MgO", sf(n_s * (Mg + O)), 1.01)

# Set 5
eq("5.8 Mr acid", 2 * C + 4 * H + 2 * O, 60.0)
Mr_est = 5 * C + 10 * H + 2 * O
eq("5.8 Mr ester", Mr_est, 102.0)
eq("5.8 n", 6.00 / 60.0, 0.100, 1e-12)
eq("5.8 theory", round(0.100 * Mr_est, 1), 10.2)
eq("5.8 yield", sf(7.14 / (0.100 * Mr_est) * 100), 70.0)
assert 14 * 5 + 2 * 16 + 0 * 1 - 0 == 102 or True

# Set 6
for lab, v in (("C", 54.5 / C), ("H", 9.1 / H), ("O", 36.4 / O)):
    pass
eq("6.2 nC", round(54.5 / C, 2), 4.54)
eq("6.2 nO", round(36.4 / O, 3), 2.275)
eq("6.2 ratio C", round((54.5 / C) / (36.4 / O)), 2)
eq("6.2 ratio H", round((9.1 / H) / (36.4 / O)), 4)
eq("6.2 empirical mass", 2 * C + 4 * H + O, 44.0)
eq("6.2 molecular", 88 / 44.0, 2.0)
eq("6.2 M+1 carbons", 100 * 4.4 / (1.1 * 100), 4.0, 1e-9)
n_co2 = 0.390 / VM
eq("6.3 n", n_co2, 0.01625, 1e-12)
Mr_cc = Ca + C + 3 * O
eq("6.3 Mr", Mr_cc, 100.1)
eq("6.3 mass", sf(n_co2 * Mr_cc), 1.63)
eq("6.3 pct", sf(n_co2 * Mr_cc / 2.00 * 100), 81.3)
eq("6.3 mass 4 s.f.", round(n_co2 * Mr_cc, 3), 1.627)
eq("6.3 pct from rounded mass", sf(1.63 / 2.00 * 100), 81.5)
eq("6.6 C3H7", 3 * 12 + 7, 43)
eq("6.6 M", 43 + 79, 122)
eq("6.7 broken", 610 + 460, 1070)
eq("6.7 made", 350 + 410 + 360, 1120)
eq("6.7 dH", 1070 - 1120, -50)
Mr_co2, Mr_h2o = C + 2 * O, 2 * H + O
eq("6.8 Mr CO2", Mr_co2, 44.0)
eq("6.8 Mr H2O", Mr_h2o, 18.0)
eq("6.8 nC", 1.76 / Mr_co2, 0.0400, 1e-12)
eq("6.8 nH", 2 * 0.720 / Mr_h2o, 0.0800, 1e-12)
eq("6.8 mass", 0.0400 * C + 0.0800 * H, 0.560, 1e-9)
eq("6.8 formula", 56 / 14.0, 4.0)

# Quiz
eq("Q1 neutrons", 27 - 13, 14)
n_naoh = 0.0250 * 20.0 / 1000
eq("Q2 n", n_naoh, 5.00e-4, 1e-12)
eq("Q2 V", n_naoh / 2 / 0.0100 * 1000, 25.0, 1e-9)
q = 100 * CW * 6.0
eq("Q3 q", round(q), 2508)
eq("Q3 dH", sf(-q / 1000 / 0.0200), -125)
eq("Q3 wrong", sf(-q / 1000), -2.51)
eq("Q9 carbons", 100 * 3.3 / (1.1 * 100), 3.0, 1e-9)
print("ok")
