# checks/chem.electrochem.py: recomputes every number in "Electrochemistry: electrolysis and electrode potentials".
# Ar from data/elements.json; E values are checked against the FACTS.md "E° / V" line; F = 9.65e4, e = 1.60e-19,
# L = 6.022e23, molar gas volume 24.0 dm3 mol-1 (FACTS.md Data section).
import json, re
from math import isclose, log10

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

AR = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
F, e_, L, Vm = 9.65e4, 1.60e-19, 6.022e23, 24.0
eq("Ar Cu", AR['Cu'], 63.5); eq("Ar Ag", AR['Ag'], 107.9); eq("Ar Al", AR['Al'], 27.0)
eq("Ar Zn", AR['Zn'], 65.4); eq("Ar Ni", AR['Ni'], 58.7); eq("Ar C", AR['C'], 12.0)

# --- E values from FACTS.md
facts = open('FACTS.md', encoding='utf-8').read()
line = [l for l in facts.splitlines() if l.startswith('- E° / V:')][0]
E = {}
for item in line[len('- E° / V:'):].strip().rstrip('.').split(';'):
    item = item.strip()
    m = re.match(r'(.+?)\s([+\-−]?\d+\.\d\d)$', item)
    assert m, item
    E[m.group(1).strip()] = float(m.group(2).replace('−', '-'))

def Ev(k): return E[k]
table = [('Li⁺/Li', -3.04), ('K⁺/K', -2.92), ('Ca²⁺/Ca', -2.87), ('Na⁺/Na', -2.71), ('Mg²⁺/Mg', -2.38), ('Al³⁺/Al', -1.66),
         ('Zn²⁺/Zn', -0.76), ('Fe²⁺/Fe', -0.44), ('Pb²⁺/Pb', -0.13), ('2H⁺/H₂', 0.00), ('Cu²⁺/Cu', 0.34), ('I₂/I⁻', 0.54),
         ('Fe³⁺/Fe²⁺', 0.77), ('Ag⁺/Ag', 0.80), ('Br₂/Br⁻', 1.07),
         ('O₂ + 4H⁺ + 4e⁻ ⇌ 2H₂O', 1.23),
         ('Cr₂O₇²⁻ + 14H⁺ + 6e⁻ ⇌ 2Cr³⁺ + 7H₂O', 1.33), ('Cl₂/Cl⁻', 1.36),
         ('MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O', 1.52), ('F₂/F⁻', 2.87),
         ('Cu⁺/Cu', 0.52), ('Cu²⁺/Cu⁺', 0.15), ('Sn⁴⁺/Sn²⁺', 0.15), ('V³⁺/V²⁺', -0.26),
         ('NO₃⁻ + 2H⁺ + e⁻ ⇌ NO₂ + H₂O', 0.81), ('2H₂O + 2e⁻ ⇌ H₂ + 2OH⁻', -0.83),
         ('MnO₂ + 4H⁺ + 2e⁻ ⇌ Mn²⁺ + 2H₂O', 1.23)]
for k, v in table:
    eq("E " + k, Ev(k), v)
# the table in the chapter is in increasing order
vals = [v for k, v in table[:20]]
assert vals == sorted(vals), "table not ordered"

# --- F = Le
eq("F=Le", sf(L * e_), 9.64e4 / 1e4 * 1e4, 1e-6) if False else None
eq("F=Le (3 s.f.)", sf(L * e_ / 1e4) , 9.64)

# --- Cu mass 0.500 A 30.0 min
Q = 0.500 * 30.0 * 60
eq("Q Cu", Q, 900)
ne = Q / F
eq("ne Cu", sf(ne, 4), 9.326e-3, 1e-9)
nCu = ne / 2
eq("nCu", sf(nCu, 4), 4.663e-3, 1e-9)
eq("mass Cu", sf(nCu * AR['Cu']), 0.296)

# --- O2 volume 2.00 A 20.0 min
Q = 2.00 * 20.0 * 60
eq("Q O2", Q, 2400)
ne = Q / F
eq("ne O2", sf(ne, 4), 0.02487)
nO2 = ne / 4
eq("nO2", sf(nO2, 4), 6.218e-3, 1e-9)
eq("V O2 dm3", sf(nO2 * Vm), 0.149)
eq("V O2 cm3", round(nO2 * Vm * 1000), 149)

# --- Ag plating
Q = 1.50 * 20.0 * 60
eq("Q Ag", Q, 1800)
ne = Q / F
eq("ne Ag", sf(ne, 4), 0.01865, 1e-9)
eq("mass Ag", sf(ne * AR['Ag']), 2.01)

# --- aluminium
Q = 1.00e5 * 3600
eq("Q Al", Q, 3.60e8)
ne = Q / F
eq("ne Al", round(ne), 3731)
nAl = ne / 3
eq("nAl", round(nAl), 1244)
eq("mass Al kg", sf(nAl * AR['Al'] / 1000), 33.6)
eq("mass Al g", sf(nAl * AR['Al']), 3.36e4, 1e-6 * 1e4)

# --- Ni charge
Q = 1.50 * 600
ne = Q / F
eq("ne Ni", sf(ne, 4), 9.326e-3, 1e-9)
nNi = 0.274 / AR['Ni']
eq("nNi", sf(nNi, 4), 4.668e-3, 1e-9)
eq("z Ni", round(ne / nNi, 2), 2.00)

# --- L determination
Q = 0.350 * 45.0 * 60
eq("Q L", Q, 945)
nCu = 0.312 / AR['Cu']
eq("nCu L", sf(nCu, 4), 4.913e-3, 1e-9)
ne = 2 * nCu
eq("ne L", sf(ne, 4), 9.827e-3, 1e-9)
Lval = Q / (ne * e_)
eq("L", sf(Lval), 6.01e23, 1e19)
assert abs(Lval - L) / L < 0.01, "L within 1%"
eq("mass uncertainty %", round(0.01 / 0.312 * 100), 3)

# --- cells
eq("Zn/Cu", round(Ev('Cu²⁺/Cu') - Ev('Zn²⁺/Zn'), 2), 1.10)
eq("MnO4/Fe", round(Ev('MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O') - Ev('Fe³⁺/Fe²⁺'), 2), 0.75)
eq("Fe3/I2", round(Ev('Fe³⁺/Fe²⁺') - Ev('I₂/I⁻'), 2), 0.23)
eq("Cl2/Br", round(Ev('Cl₂/Cl⁻') - Ev('Br₂/Br⁻'), 2), 0.29)
eq("Cu + H+", round(Ev('2H⁺/H₂') - Ev('Cu²⁺/Cu'), 2), -0.34)
eq("Cu + NO3", round(Ev('NO₃⁻ + 2H⁺ + e⁻ ⇌ NO₂ + H₂O') - Ev('Cu²⁺/Cu'), 2), 0.47)
eq("H2/O2", round(Ev('O₂ + 4H⁺ + 4e⁻ ⇌ 2H₂O') - Ev('2H⁺/H₂'), 2), 1.23)
eq("MnO2/Cl", round(Ev('MnO₂ + 4H⁺ + 2e⁻ ⇌ Mn²⁺ + 2H₂O') - Ev('Cl₂/Cl⁻'), 2), -0.13)
eq("Cu+ disp", round(Ev('Cu⁺/Cu') - Ev('Cu²⁺/Cu⁺'), 2), 0.37)
eq("Ag/Fe small", round(Ev('Ag⁺/Ag') - Ev('Fe³⁺/Fe²⁺'), 2), 0.03)

# --- Nernst
eq("Cu 0.01", round(0.34 + 0.059 / 2 * log10(0.0100), 3), 0.281)
eq("Cu 0.01 (2 d.p.)", round(0.34 + 0.059 / 2 * log10(0.0100), 2), 0.28)
eq("0.0295 x -2", 0.0295 * -2, -0.059)
eq("Fe 10:1", round(0.77 + 0.059 * log10(10), 3), 0.829)
eq("Fe 10:1 (2 d.p.)", round(0.77 + 0.059, 2), 0.83)
Ezn = -0.76 + 0.059 / 2 * log10(0.100)
eq("Zn 0.1", round(Ezn, 4), -0.7895)
eq("cell Zn 0.1", round(0.34 - Ezn, 2), 1.13)
eq("Ag 0.05", round(0.80 + 0.059 * log10(0.0500), 2), 0.72)
EAg = 0.80 + 0.059 * log10(0.0100)
eq("Ag 0.01", round(EAg, 3), 0.682)
eq("cell Zn/Ag 0.01", round(EAg - Ev('Zn²⁺/Zn'), 2), 1.44)
eq("plot Cu 0.0100", round(0.34 + 0.0295 * -2, 3), 0.281)

# --- exam practice
eq("Q2 Q", 0.800 * 25.0 * 60, 1200)
eq("Q2 ne", sf(1200 / F, 4), 0.01244, 1e-9)
eq("Q2 m", sf(1200 / F * AR['Ag']), 1.34)
Q = 1.50 * 30.0 * 60
ne = Q / F
eq("Q3 ne", sf(ne, 4), 0.02798)
eq("Q3 H2 cm3", round(ne / 2 * Vm * 1000), 336)
eq("Q3 H2 dm3", sf(ne / 2 * Vm), 0.336)
eq("Q3 nO2", sf(ne / 4, 4), 6.995e-3, 1e-9)
eq("Q3 O2 cm3", round(ne / 4 * Vm * 1000), 168)
Q = 0.250 * 3600
eq("Q4 Q", Q, 900)
nCu = 0.294 / AR['Cu']
eq("Q4 nCu", sf(nCu, 4), 4.630e-3, 1e-9)
eq("Q4 ne", sf(2 * nCu, 4), 9.260e-3, 1e-9)
eq("Q4 L", sf(Q / (2 * nCu * e_)), 6.07e23, 1e19)
eq("Q5 E", round(Ev('Sn⁴⁺/Sn²⁺') - Ev('V³⁺/V²⁺'), 2), 0.41)
eq("Q6 Br", round(Ev('MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O') - Ev('Br₂/Br⁻'), 2), 0.45)
eq("Q6 Cl", round(Ev('MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O') - Ev('Cl₂/Cl⁻'), 2), 0.16)
eq("Q8 E", round(Ev('Ag⁺/Ag') - Ev('Zn²⁺/Zn'), 2), 1.56)
dG = -2 * F * 1.56 / 1000
eq("Q8 dG J", sf(-2 * F * 1.56, 3), -3.01e5, 1e2)
eq("Q8 dG kJ", round(dG), -301)

# --- delta G
eq("Daniell dG", sf(-2 * F * 1.10 / 1000), -212)
eq("Daniell dG J", sf(-2 * F * 1.10, 3), -2.12e5, 1e2)
eq("MnO4 dG", round(-5 * F * 0.75 / 1000), -362)
eq("MnO4 dG J", sf(-5 * F * 0.75, 3), -3.62e5, 1e2)
eq("Pb/Cu dG", sf(-2 * F * 0.47 / 1000), -90.7)
eq("Pb/Cu dG J", sf(-2 * F * 0.47, 3), -9.07e4, 1e1)
eq("Cu+ dG", sf(-1 * F * 0.37 / 1000), -35.7)

# --- stretch Al
Q = 1.00e5 * 3600
ne = Q / F
nO2 = ne / 4
eq("Al nO2", sf(nO2, 4), 932.6, 0.05)
eq("Al C kg", sf(nO2 * AR['C'] / 1000), 11.2)

# --- try
eq("try Q", 2.50 * 40.0 * 60, 6000)
Q = 3.00 * 3600
eq("try Zn Q", Q, 10800)
ne = Q / F
eq("try Zn ne", sf(ne, 4), 0.1119)
eq("try Zn n", sf(ne / 2, 4), 0.05596)
eq("try Zn m", sf(ne / 2 * AR['Zn']), 3.66)
eq("try Pb/Cu", round(Ev('Cu²⁺/Cu') - Ev('Pb²⁺/Pb'), 2), 0.47)
eq("try Br/Fe", round(Ev('Br₂/Br⁻') - Ev('Fe³⁺/Fe²⁺'), 2), 0.30)
eq("quiz ne", 2.00 * 965 / F, 0.0200, 1e-9)
eq("quiz Q", 2.00 * 965, 1930)
eq("quiz cell", round(Ev('Ag⁺/Ag') - Ev('Zn²⁺/Zn'), 2), 1.56)
eq("quiz doubled", round(2 * 0.80 + 0.76, 2), 2.36)
eq("quiz add wrong", round(0.80 - 0.76, 2), 0.04)

print("ok")
