# checks/chem.states.py: recomputes every number in the States of matter chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.).
import json
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
R = 8.31

# ---- warm-up
eq("CO2 Mr", A['C'] + 2 * A['O'], 44.0)
eq("CO2 n", 4.40 / 44.0, 0.100)

# ---- worked example: volume of 0.0500 mol at 298 K, 101 kPa
V = 0.0500 * R * 298 / 101000
eq("eg1 m3 (1.226e-3)", sf(V, 4), 1.226e-3, 1e-9)
eq("eg1 dm3", sf(V * 1000), 1.23)

# ---- molar volume checks
eq("Vm 298 K", sf(R * 298 / 101000, 4), 0.02452, 1e-9)
eq("Vm 298 dm3", sf(R * 298 / 101000 * 1000), 24.5)
assert abs(R * 293 / 101000 * 1000 - 24.0) < 0.15      # 24.0 matches about 20 C
eq("Vm stp", sf(R * 273 / 101000 * 1000), 22.5)
assert abs(R * 273 / 101000 * 1000 - 22.4) < 0.15      # data section rounds to 22.4

# ---- worked example: flask, 0.608 g, 250 cm3, 300 K, 152 kPa
n = 152000 * 250e-6 / (R * 300)
eq("eg2 n", sf(n, 4), 0.01524, 1e-9)
eq("eg2 Mr", sf(0.608 / n), 39.9)
eq("Ar Ar", A['Ar'], 39.9)

# ---- ratio shortcut
eq("eg3 p2", 100 * 360 / 300, 120)

# ---- Mr of a volatile liquid
Mr = 0.240 * R * 373 / (101000 * 83.0e-6)
eq("eg4 Mr", sf(Mr), 88.7)
Ef = 2 * A['C'] + 4 * A['H'] + A['O']
eq("eg4 empirical mass", Ef, 44.0)
eq("eg4 multiple", round(sf(Mr) / Ef), 2)
eq("eg4 ratio", sf(sf(Mr) / Ef), 2.02)
eq("C4H8O2 Mr", 4 * A['C'] + 8 * A['H'] + 2 * A['O'], 88.0)

# ---- airbag
MrN = A['Na'] + 3 * A['N']
eq("NaN3 Mr", MrN, 65.0)
nN2 = 65.0 / MrN * 3 / 2
eq("N2 n", nN2, 1.50)
V = nN2 * R * 350 / 101000
eq("airbag m3", sf(V, 4), 0.04320, 1e-9)
eq("airbag dm3", sf(V * 1000), 43.2)

# ---- try questions
eq("try3", sf(0.200 * R * 350 / 100000 * 1000, 3), 5.82)
eq("try3 m3", sf(0.200 * R * 350 / 100000, 4), 5.817e-3, 1e-9)
eq("try4", sf(101000 * 5.00e-4 / (R * 293), 3), 0.0207)
eq("try5", sf(0.350 * R * 300 / (101000 * 2.15e-4)), 40.2)

# ---- exam practice
eq("q2 Mr O2", 2 * A['O'], 32.0)
eq("q2 n", 0.640 / 32.0, 0.0200)
V = 0.0200 * R * 300 / 100000
eq("q2 m3", sf(V, 4), 4.986e-4, 1e-9)
eq("q2 cm3", sf(V * 1e6), 499)
n = 100000 * 6.00e-5 / (R * 373)
eq("q3 n", sf(n, 4), 1.936e-3, 1e-9)
eq("q3 Mr", sf(0.139 / n), 71.8)
Mcc = A['Ca'] + A['C'] + 3 * A['O']
eq("q4 Mr", Mcc, 100.1)
n = 2.50 / Mcc
eq("q4 n", sf(n, 4), 0.02498, 1e-9)
V = n * R * 1000 / 101000
eq("q4 m3", sf(V, 4), 2.055e-3, 1e-9)
eq("q4 dm3", sf(V * 1000), 2.05)
# q8 density
Mr8 = 2350 * R * 300 / 101000
eq("q8 Mr", sf(Mr8), 58.0)
eq("q8 C", sf(82.8 / A['C'], 3), 6.90)
eq("q8 H", sf(17.2 / A['H'], 3), 17.2)
eq("q8 ratio", sf(17.2 / 6.90, 3), 2.49)
eq("q8 ratio x2", round(2 * 17.2 / 6.90), 5)
eq("C2H5 mass", 2 * A['C'] + 5 * A['H'], 29.0)
eq("q8 multiple", 58.0 / 29.0, 2)
eq("C4H10 %C", sf(4 * A['C'] / (4 * A['C'] + 10 * A['H']) * 100, 3), 82.8)
eq("q8 rho from Mr 58.0", sf(58.0 * 101000 / (R * 300) / 1000, 3), 2.35)
# stretch 1
eq("s1 Mr", sf(88.7 / 0.950, 3), 93.4)
# stretch 2
V = R * 298 / 101000
eq("s2 cm3", sf(V * 1e6, 4), 24520, 1)
eq("s2 pct", sf(18.0 / (V * 1e6) * 100, 3), 0.0734)
eq("s2 V/100", sf(V * 1e6 / 100, 4), 245.2, 0.05)
eq("s2 pct2", sf(18.0 / (V * 1e6 / 100) * 100, 3), 7.34)
# quiz
V = R * 300 / 100000
eq("quiz dm3", sf(V * 1000, 3), 24.9)
eq("quiz m3", sf(V, 4), 0.02493, 1e-9)
eq("quiz forgot conversion", sf(V, 3), 0.0249)
print("ok")
