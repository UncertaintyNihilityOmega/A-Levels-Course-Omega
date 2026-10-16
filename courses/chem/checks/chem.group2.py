# checks/chem.group2.py: recomputes every number in the Group 2 chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.); ionisation energies from FACTS.md.
import json
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

E = {e['sym']: e for e in json.load(open('data/elements.json', encoding='utf-8'))}
A = {s: e['ar'] for s, e in E.items()}

# ---- outer electrons: Group 2 elements all in group 2
for s in ('Mg', 'Ca', 'Sr', 'Ba'):
    assert E[s]['group'] == 2

# ---- successive ionisation energies (FACTS.md Data booklet values)
facts = open('FACTS.md', encoding='utf-8').read()
succ_line = facts.split('Successive IE (1st 2nd 3rd 4th):')[1].split('\n')[0]
ie = {'Mg': (736, 1450, 7740), 'Ca': (590, 1150, 4940), 'Sr': (548, 1060, 4120), 'Ba': (502, 966, 3390)}
fourth = {'Mg': 10500, 'Ca': 6480, 'Sr': 5440, 'Ba': 4700}
for s, v in ie.items():
    assert f"{s} {v[0]} {v[1]} {v[2]} {fourth[s]}" in succ_line, s
sums = {s: v[0] + v[1] for s, v in ie.items()}
eq("Mg 1st+2nd", sums['Mg'], 2186); eq("Ca 1st+2nd", sums['Ca'], 1740)
eq("Sr 1st+2nd", sums['Sr'], 1608); eq("Ba 1st+2nd", sums['Ba'], 1468)
assert sums['Mg'] > sums['Ca'] > sums['Sr'] > sums['Ba']
assert all(ie[s][2] > 3 * ie[s][1] for s in ie)             # third IE much bigger than the second
eq("Mg 3rd vs 2nd", ie['Mg'][2], 7740); eq("Mg 2nd", ie['Mg'][1], 1450)

# ---- warm-up: moles of Mg
eq("warm-up n Mg", round(0.486 / A['Mg'], 4), 0.0200)

# ---- nitrate decomposition: 2M(NO3)2 -> 2MO + 4NO2 + O2; atoms balance
eq("N atoms", 2 * 2, 4)
eq("O atoms left", 2 * 6, 12)
eq("O atoms right", 2 * 1 + 4 * 2 + 2, 12)
eq("gas mol per mol nitrate", (4 + 1) / 2, 2.5)

# ---- lime kiln: 20.0 g CaCO3
Mr_CaCO3 = A['Ca'] + A['C'] + 3 * A['O']; Mr_CaO = A['Ca'] + A['O']
eq("CaCO3 Mr", Mr_CaCO3, 100.1); eq("CaO Mr", Mr_CaO, 56.1)
n = 20.0 / Mr_CaCO3
eq("n CaCO3", round(n, 4), 0.1998)
eq("mass CaO", sf(n * Mr_CaO), 11.2)
eq("V CO2", sf(n * 24.0), 4.80)

# ---- barium nitrate 5.23 g
Mr_BaN = A['Ba'] + 2 * (A['N'] + 3 * A['O'])
eq("Ba(NO3)2 Mr", Mr_BaN, 261.3)
n = 5.23 / Mr_BaN
eq("n Ba(NO3)2", round(n, 5), 0.02002)
eq("n gas (from 0.02002)", round(2.5 * 0.02002, 5), 0.05005)
eq("V gas", sf(2.5 * n * 24.0), 1.20)

# ---- Ca(OH)2 titration
n_HCl = 0.0500 * 19.5 / 1000
eq("n HCl", n_HCl, 9.75e-4)
n_CaOH2 = n_HCl / 2
eq("n Ca(OH)2", n_CaOH2, 4.875e-4)
c = n_CaOH2 / 0.0250
eq("solubility mol", c, 0.0195)
Mr_CaOH2 = A['Ca'] + 2 * (A['O'] + A['H'])
eq("Ca(OH)2 Mr", Mr_CaOH2, 74.1)
eq("solubility g/dm3", sf(c * Mr_CaOH2), 1.44)

# ---- BaSO4 gravimetric
Mr_BaSO4 = A['Ba'] + A['S'] + 4 * A['O']
eq("BaSO4 Mr", Mr_BaSO4, 233.4)
n = 0.467 / Mr_BaSO4
eq("n BaSO4 (x1e-3)", round(n * 1000, 3), 2.001)
eq("c sulfate", sf(n / 0.0250), 0.0800)

# ---- Mg + HCl (warm-up quiz and try)
n = 0.243 / A['Mg']
eq("n Mg", round(n, 4), 0.0100)
eq("V H2 dm3", n * 24.0, 0.240)
eq("V H2 cm3", round(n * 24.0 * 1000), 240)
eq("quiz half", 0.240 / 2, 0.120); eq("quiz double", 0.240 * 2, 0.480)

# ---- Sr(NO3)2 4.23 g
Mr_SrN = A['Sr'] + 2 * (A['N'] + 3 * A['O'])
eq("Sr(NO3)2 Mr", Mr_SrN, 211.6)
n = 4.23 / Mr_SrN
eq("n Sr(NO3)2", round(n, 5), 0.01999)
Mr_SrO = A['Sr'] + A['O']
eq("SrO Mr", Mr_SrO, 103.6)
eq("mass SrO", sf(n * Mr_SrO), 2.07)

# ---- Sr(OH)2 titration
n_HCl = 0.0500 * 0.0330
eq("n HCl", n_HCl, 1.65e-3)
n_SrOH2 = n_HCl / 2
eq("n Sr(OH)2", n_SrOH2, 8.25e-4)
c = n_SrOH2 / 0.0250
eq("c Sr(OH)2", c, 0.0330)
Mr_SrOH2 = A['Sr'] + 2 * (A['O'] + A['H'])
eq("Sr(OH)2 Mr", Mr_SrOH2, 121.6)
eq("solubility g/dm3", sf(c * Mr_SrOH2), 4.01)

# ---- delta H solution (data for this question)
dHlatt, hydM, hydX = -2480, -1650, -950
eq("dHsol", -dHlatt + hydM + hydX, -120)

# ---- unknown carbonate, worked example: 2.50 g -> 1.40 g
Mr_CO2 = A['C'] + 2 * A['O']
eq("CO2 Mr", Mr_CO2, 44.0)
eq("mass CO2", round(2.50 - 1.40, 2), 1.10)
n = 1.10 / Mr_CO2
eq("n CO2", round(n, 4), 0.0250)
eq("Mr MCO3", 2.50 / 0.0250, 100.0)
eq("Ar M", 100.0 - (A['C'] + 3 * A['O']), 40.0)
assert abs(A['Ca'] - 40.0) < 0.2

# ---- unknown carbonate, practice: 3.95 g -> 3.07 g
eq("mass CO2", round(3.95 - 3.07, 2), 0.88)
n = 0.88 / Mr_CO2
eq("n CO2", round(n, 4), 0.0200)
eq("Mr MCO3", 3.95 / 0.0200, 197.5)
eq("Ar M", 197.5 - (A['C'] + 3 * A['O']), 137.5)
assert abs(A['Ba'] - 137.5) < 0.3 and A['Ba'] == 137.3

# ---- IE: third vs second for Mg
assert 7740 / 1450 > 5

print("ok")
