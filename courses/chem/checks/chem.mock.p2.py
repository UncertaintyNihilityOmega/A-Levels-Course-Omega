# checks/chem.mock.p2.py: recomputes every number in Mock paper 2 (AS structured).
# Ar from data/elements.json (the 9701 Periodic Table); Vm = 24.0 dm3 at room conditions; c = 4.18 J g-1 K-1.
import json
import os
from math import isclose

HERE = os.path.dirname(os.path.abspath(__file__))
AR = {e['sym']: e['ar'] for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


C, O, Mg, Cu, Si = AR['C'], AR['O'], AR['Mg'], AR['Cu'], AR['Si']

# Q1
eq("1b sum", 28 * 92.2 + 29 * 4.7 + 30 * 3.1, 2810.9, 1e-9)
eq("1b abundances", 92.2 + 4.7 + 3.1, 100.0, 1e-9)
eq("1b Ar", sf((28 * 92.2 + 29 * 4.7 + 30 * 3.1) / 100), 28.1)
eq("1b table Si", Si, 28.1)
eq("1c Cl-", 2 + 2 + 6 + 2 + 6, 18)
eq("1c Fe2+", 26 - 2, 24)
eq("1c Fe2+ shells", 2 + 2 + 6 + 2 + 6 + 6, 24)
ie = [590, 1150, 4940, 6480]  # Ca values from FACTS.md
assert ie[2] / ie[1] > 4 and ie[1] / ie[0] < 2.5
eq("1e Cu", round(3.17 / Cu, 4), 0.0499)
eq("1e O", round(0.400 / O, 4), 0.0250)
eq("1e ratio", round((3.17 / Cu) / (0.400 / O)), 2)

# Q2
dT = 27.3 - 20.5
eq("2a dT", round(dT, 1), 6.8)
q = 100 * 4.18 * dT
eq("2a q", round(q), 2842)
n = 1.00 * 50.0 / 1000
eq("2a n", n, 0.0500, 1e-12)
eq("2a dH", sf(-q / n / 1000), -56.8)
eq("2b dHf", -394 + 2 * -286 - (-726), -240)
n_h2 = 0.500 - 0.790 / 2
eq("2c n H2", n_h2, 0.105, 1e-12)
hi, h2 = 0.790 / 2.00, n_h2 / 2.00
eq("2c [HI]", hi, 0.395, 1e-12)
eq("2c [H2]", h2, 0.0525, 1e-12)
eq("2c Kc", sf(hi ** 2 / (h2 * h2)), 56.6)

# Q3
Mr = Mg + C + 3 * O
eq("3c Mr", Mr, 84.3)
n = 4.21 / Mr
eq("3c n", sf(n), 0.0499)
eq("3c V", sf(n * 24.0), 1.20)

# Q5
eq("5a carbons", 100 * 4.4 / (1.1 * 100), 4.0, 1e-9)
eq("5b H", 72 - 4 * C - O, 8.0)
eq("5d 57", 2 * C * 1 + 5 * 1.0 + C + O - 0, 57.0, 1e-9)  # C2H5CO+: 3C + 5H + O
eq("5d 43", 2 * C + 3 * 1.0 + O, 43.0, 1e-9)  # CH3CO+: 2C + 3H + O
print("ok")
