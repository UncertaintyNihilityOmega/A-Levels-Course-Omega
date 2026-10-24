# checks/chem.mock.p4.py: recomputes every number in Mock paper 4 (100 marks).
# Ar from data/elements.json (the 9701 Periodic Table); constants from the Data booklet (FACTS.md).
import json, os
from math import isclose, log10, sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
AR = {e['sym']: e['ar'] for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

F = 9.65e4
Cu, Fe = AR['Cu'], AR['Fe']

# Marks: 8 + 8 + 9 + 11 + 8 + 12 + 8 + 13 + 13 + 10 = 100
assert 8 + 8 + 9 + 11 + 8 + 12 + 8 + 13 + 13 + 10 == 100
# Q10 13C: methyl 4-hydroxybenzoate, ring 4 environments + C=O + OCH3
assert 4 + 1 + 1 == 6

# Q1 Na2O Born-Haber
steps = 2 * 107 + 2 * 494 + 249 + (-141) + 798
eq("Q1 sum", steps, 2108)
eq("Q1 2Na", 2 * 107, 214)
eq("Q1 2IE", 2 * 494, 988)
eq("Q1 latt", -414 - steps, -2522)

# Q2 NaHCO3
dS = (135 + 189 + 214) - 2 * 102
eq("Q2 dS", dS, 334)
dG = 130 - 298 * dS / 1000
eq("Q2 dG", sf(dG), 30.5)
assert dG > 0
eq("Q2 T", sf(130000 / dS), 389)

# Q3
Q = 0.400 * 50.0 * 60
eq("Q3 Q", Q, 1200)
elec = Q / 1.60e-19
eq("Q3 electrons", sf(elec), 7.50e21, 1e17)
atoms = elec / 2
eq("Q3 atoms", sf(atoms), 3.75e21, 1e17)
ncu = 0.395 / Cu
eq("Q3 n", sf(ncu), 6.22e-3, 1e-5)
L = atoms / ncu
eq("Q3 L", sf(L), 6.03e23, 1e19)
e_ag = 0.80 + 0.059 * log10(0.0500)
eq("Q3 E Ag", round(e_ag, 3), 0.723)
eq("Q3 E Ag 2dp", round(e_ag, 2), 0.72)
eq("Q3 Ecell", round(e_ag + 0.76, 2), 1.48)
e0 = 0.80 + 0.76
eq("Q3 E0", round(e0, 2), 1.56)
eq("Q3 dG", sf(-2 * F * e0 / 1000), -301)

# Q4
Ka = 1.78e-4
h = sqrt(Ka * 0.0500)
eq("Q4a H", sf(h), 2.98e-3, 1e-6)
eq("Q4a pH", round(-log10(h), 2), 2.53)
nha = 0.200 * 0.0400
noh = 0.150 * 0.0200
eq("Q4b nHA", nha, 8.00e-3, 1e-12)
eq("Q4b nOH", noh, 3.00e-3, 1e-12)
ha, a = nha - noh, noh
eq("Q4b HA", ha, 5.00e-3, 1e-12)
h2 = Ka * ha / a
eq("Q4b H", sf(h2), 2.97e-4, 1e-7)
eq("Q4b pH", round(-log10(h2), 2), 3.53)
s = (8.0e-12 / 4) ** (1 / 3)
eq("Q4c s", sf(s), 1.26e-4, 1e-7)
ag = sqrt(8.0e-12 / 0.0100)
eq("Q4d Ag", sf(ag), 2.83e-5, 1e-7)
eq("Q4d s", sf(ag / 2), 1.41e-5, 1e-7)
assert ag / 2 < s

# Q5
r1, r2, r3 = 4.0e-6, 8.0e-6, 4.0e-6
eq("Q5 order RBr", r2 / r1, 2.0)   # [RBr] x2 -> rate x2: first order
eq("Q5 order OH", r3 / r1, 1.0)    # [OH] x3 -> rate x1: zero order
k = r1 / 0.0100
eq("Q5 k", k, 4.0e-4, 1e-12)
eq("Q5 check exp2", k * 0.0200, r2, 1e-12)
eq("Q5 check exp3", k * 0.0100, r3, 1e-12)

# Q6
nmn = 0.0200 * 19.60 / 1000
eq("Q6 nMn", nmn, 3.92e-4, 1e-12)
n25 = 5 * nmn
eq("Q6 n25", n25, 1.96e-3, 1e-12)
n250 = n25 * 10
eq("Q6 n250", n250, 1.96e-2, 1e-12)
m = n250 * Fe
eq("Q6 mass", round(m, 3), 1.094, 1e-3)
eq("Q6 pct", sf(m / 1.45 * 100), 75.4)
eq("Q6 E", round(1.52 - 1.36, 2), 0.16)

print("ok")
