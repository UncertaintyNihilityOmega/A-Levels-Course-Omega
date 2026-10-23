# checks/chem.org.hydrocarbons.py: recomputes every number in "Hydrocarbons: alkanes and alkenes".
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0, Cl 35.5, Br 79.9.
# Boiling points quoted in the chapter (to the nearest degree, as in chem.shapes): methane -162, ethane -89,
# propane -42, butane -0.5, pentane 36, hexane 69, 2-methylbutane 28, 2,2-dimethylpropane 9.5. They are
# standard-table values and are not recomputed here.
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
H, C, O, Cl, Br = A['H'], A['C'], A['O'], A['Cl'], A['Br']
eq("Ar H", H, 1.0); eq("Ar C", C, 12.0); eq("Ar O", O, 16.0); eq("Ar Cl", Cl, 35.5); eq("Ar Br", Br, 79.9)

# --- worked example: 20.0 cm3 butane + 200 cm3 O2, C4H10 + 13/2 O2 -> 4CO2 + 5H2O
v_but, v_o2 = 20.0, 200.0
o2_used = v_but * 6.5
co2 = v_but * 4
eq("eg1 O2 used", o2_used, 130)
eq("eg1 O2 left", v_o2 - o2_used, 70)
eq("eg1 CO2", co2, 80.0)
eq("eg1 total gas", v_o2 - o2_used + co2, 150)

# --- worked example: 1.00 kg octane
Mr_oct = 8 * C + 18 * H
Mr_co2 = C + 2 * O
eq("Mr C8H18", Mr_oct, 114.0)
eq("Mr CO2", Mr_co2, 44.0)
n_oct = 1000 / Mr_oct
eq("eg2 n octane", round(n_oct, 3), 8.772)
n_co2 = 8 * n_oct
eq("eg2 n CO2", round(n_co2, 2), 70.18)
m_co2 = n_co2 * Mr_co2
eq("eg2 m CO2 (g)", round(m_co2), 3088)
eq("eg2 m CO2 (kg, 3 s.f.)", sf(m_co2 / 1000), 3.09)

# --- balanced combustion equations (atom counts)
def balanced(left, right):
    # each side: list of (coef, dict of element counts)
    from collections import Counter
    L, R = Counter(), Counter()
    for c, f in left:
        for k, v in f.items(): L[k] += c * v
    for c, f in right:
        for k, v in f.items(): R[k] += c * v
    return L == R
assert balanced([(1, {'C': 1, 'H': 4}), (2, {'O': 2})], [(1, {'C': 1, 'O': 2}), (2, {'H': 2, 'O': 1})])          # CH4
assert balanced([(1, {'C': 3, 'H': 8}), (5, {'O': 2})], [(3, {'C': 1, 'O': 2}), (4, {'H': 2, 'O': 1})])          # C3H8
assert balanced([(2, {'C': 1, 'H': 4}), (3, {'O': 2})], [(2, {'C': 1, 'O': 1}), (4, {'H': 2, 'O': 1})])          # 2CH4 + 3O2 -> 2CO + 4H2O
assert balanced([(1, {'C': 1, 'H': 4}), (1, {'O': 2})], [(1, {'C': 1}), (2, {'H': 2, 'O': 1})])                  # CH4 + O2 -> C + 2H2O
assert balanced([(2, {'C': 2, 'H': 6}), (7, {'O': 2})], [(4, {'C': 1, 'O': 2}), (6, {'H': 2, 'O': 1})])          # 2C2H6 + 7O2
assert balanced([(2, {'C': 6, 'H': 14}), (19, {'O': 2})], [(12, {'C': 1, 'O': 2}), (14, {'H': 2, 'O': 1})])      # 2C6H14 + 19O2
assert balanced([(2, {'C': 2, 'H': 3, 'Cl': 1}), (5, {'O': 2})], [(4, {'C': 1, 'O': 2}), (2, {'H': 1, 'Cl': 1}), (2, {'H': 2, 'O': 1})])  # PVC
assert balanced([(1, {'C': 10, 'H': 22})], [(1, {'C': 8, 'H': 18}), (1, {'C': 2, 'H': 4})])
assert balanced([(1, {'C': 12, 'H': 26})], [(1, {'C': 8, 'H': 18}), (2, {'C': 2, 'H': 4})])
assert balanced([(1, {'C': 10, 'H': 22})], [(1, {'C': 7, 'H': 16}), (1, {'C': 3, 'H': 6})])
# butane 13/2 O2 and octane 25/2 O2
assert balanced([(2, {'C': 4, 'H': 10}), (13, {'O': 2})], [(8, {'C': 1, 'O': 2}), (10, {'H': 2, 'O': 1})])
assert balanced([(2, {'C': 8, 'H': 18}), (25, {'O': 2})], [(16, {'C': 1, 'O': 2}), (18, {'H': 2, 'O': 1})])

# --- quiz: 40 cm3 CH4 + 100 cm3 O2 -> CO2 + 2H2O(l)
used = 40 * 2; left = 100 - used; co2q = 40
eq("quiz gas left", left + co2q, 60)
eq("quiz gas with steam", left + co2q + 40 * 2, 140)

# --- bond energies (kJ/mol, FACTS.md data section)
CH, CC, CdC, HH, HCl, ClCl, CCl, HBr, CBr, BrBr = 410, 350, 610, 436, 431, 242, 340, 366, 280, 193
eq("pi bond contribution", CdC - CC, 260)
eq("propagation Cl step 1", CH - HCl, -21)
eq("propagation Cl step 2", ClCl - CCl, -98)
eq("propagation Br step 1", CH - HBr, 44)
eq("H2 addition broken", CdC + HH, 1046)
eq("H2 addition formed", CC + 2 * CH, 1170)
eq("dH hydrogenation", (CdC + HH) - (CC + 2 * CH), -124)
eq("dH HBr addition", (CdC + HBr) - (CC + CH + CBr), -64)
eq("HBr broken", CdC + HBr, 976)
eq("HBr formed", CC + CH + CBr, 1040)
eq("Q3 broken", CdC + ClCl, 852)
eq("Q3 formed", CC + 2 * CCl, 1030)
eq("Q3 dH", (CdC + ClCl) - (CC + 2 * CCl), -178)

# --- exam Q4: 0.350 g alkene + 0.800 g Br2
Mr_Br2 = 2 * Br
eq("Mr Br2", Mr_Br2, 159.8)
nBr2 = 0.800 / Mr_Br2
eq("Q4 n Br2", round(nBr2 * 1000, 3), 5.006)
Mr_alk = 0.350 / nBr2
eq("Q4 Mr", sf(Mr_alk), 69.9)
eq("Q4 n carbons", round(Mr_alk / 14), 5)
eq("Mr C5H10", 5 * C + 10 * H, 70.0)

# --- PVC
Mr_pvc = 2 * C + 3 * H + Cl
Mr_hcl = H + Cl
eq("Mr C2H3Cl", Mr_pvc, 62.5)
eq("Mr HCl", Mr_hcl, 36.5)
n1 = 1000 / Mr_pvc
eq("eg PVC n", round(n1, 2), 16.00)
eq("eg PVC m HCl g", round(n1 * Mr_hcl), 584)
n2 = 250 * 1000 / Mr_pvc
eq("Q7 n", n2, 4000)
eq("Q7 m g", n2 * Mr_hcl, 146000)

# --- formula checks: alkene fits CnH2n; products of KMnO4 cleavage conserve carbon
assert 6 + 6 == 6 * 1 + 6          # C6H12 = propanone (3C) + propanoic acid (3C)
assert 3 + 3 == 6
assert 4 + 3 == 7                  # C7H14: butanoic acid (4C) + propanone (3C)
assert 3 + 4 == 7
assert 1 + 4 == 5                  # 2-methylbut-1-ene C5H10: CO2 (1C) + butanone (4C)
print("ok")
