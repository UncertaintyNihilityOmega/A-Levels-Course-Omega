# checks/chem.org.carbonyl.py: recomputes every number in "Aldehydes and ketones".
# Ar from the 9701 Periodic Table (data/elements.json). Boiling points (standard-table values, not recomputed):
# propane -42, propanal 49, propanone 56, propan-1-ol 97 (deg C). Bond energies C=O 740, C-O 360 and
# electronegativities C 2.5, O 3.5 are from FACTS.md (Data section).
import json
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
H, C, O, Cu, Ag = A['H'], A['C'], A['O'], A['Cu'], A['Ag']
eq("Ar H", H, 1.0); eq("Ar C", C, 12.0); eq("Ar O", O, 16.0); eq("Ar Cu", Cu, 63.5); eq("Ar Ag", Ag, 107.9)

def Mr(c, h, o=0): return c * C + h * H + o * O

# physical properties table
eq("Mr propane", Mr(3, 8), 44.0)
eq("Mr propanal", Mr(3, 6, 1), 58.0)
eq("Mr propanone", Mr(3, 6, 1), 58.0)
eq("Mr propan-1-ol", Mr(3, 8, 1), 60.0)
assert -42 < 49 < 56 < 97
assert 2.5 < 3.5

# pi bond estimate
eq("pi bond", 740 - 360, 380)

# yield example: 2.90 g butanone -> 2.05 g butan-2-ol
Mk, Ma = Mr(4, 8, 1), Mr(4, 10, 1)
eq("Mr butanone", Mk, 72.0); eq("Mr butan-2-ol", Ma, 74.0)
nk = 2.90 / Mk
eq("n butanone", round(nk, 5), 0.04028)
mx = nk * Ma
eq("max mass", round(mx, 3), 2.981)
eq("yield", round(2.05 / mx * 100, 1), 68.8)

# Fehling's: 0.725 g propanal -> Cu2O
Mcu2o = 2 * Cu + O
eq("Mr Cu2O", Mcu2o, 143.0)
npr = 0.725 / Mr(3, 6, 1)
eq("n propanal", round(npr, 5), 0.01250)
eq("mass Cu2O", sf(npr * Mcu2o), 1.79)

# Tollens': 0.360 g butanal -> Ag
nb = 0.360 / Mr(4, 8, 1)
eq("n butanal", round(nb, 5), 0.00500)
eq("n Ag", 2 * nb, 0.0100)
eq("mass Ag", sf(2 * nb * Ag), 1.08)

# quiz: 0.0300 mol ethanal
eq("quiz Ag", sf(2 * 0.0300 * Ag), 6.47)
eq("quiz wrong 3.24", sf(0.0300 * Ag), 3.24)
eq("quiz wrong 12.9", sf(4 * 0.0300 * Ag), 12.9)

# balance checks (atoms, charge)
# explicit per-element tally: [H, O, charge] with R ignored
tol_l = [1 + 3, 1 + 3, +2 - 3]            # CHO + 3OH-: H 1+3, O 1+3 ; charge +2-3
tol_r = [2 * 2, 2 + 2, -1]                # COO- + 2H2O: H 4, O 2+2 ; charge -1
assert tol_l == tol_r
fl = [1 + 5, 1 + 5, 4 - 5]                # CHO + 5OH- (+ 2Cu2+)
fr = [3 * 2, 2 + 1 + 3, -1]               # COO- + Cu2O + 3H2O
assert fl == fr
# iodoform propanone: CH3COCH3 + 3I2 + 4OH- -> CHI3 + CH3COO- + 3I- + 3H2O
assert (6 + 4, 1 + 4, -4) == (1 + 3 + 6, 2 + 3, -1 - 3)
# ethanal: CH3CHO + 3I2 + 4OH- -> CHI3 + HCOO- + 3I- + 3H2O
assert (4 + 4, 1 + 4, -4) == (1 + 1 + 6, 2 + 3, -1 - 3)
# MnO4-/propan-2-ol: 2MnO4- + 6H+ + 5C3H8O -> 2Mn2+ + 8H2O + 5C3H6O
assert (6 + 5 * 8, 8 + 5, -2 + 6) == (16 + 5 * 6, 8 + 5, +4)
n += 5
print("ok", n)
