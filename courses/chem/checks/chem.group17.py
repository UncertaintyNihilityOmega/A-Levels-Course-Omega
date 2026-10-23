# checks/chem.group17.py: recomputes every number in the Group 17 chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table); bond energies and E values from FACTS.md.
# Boiling points (F2 -188, Cl2 -34, Br2 59, I2 184 degrees C) are standard data-table values rounded to whole
# degrees (CRC Handbook: -188.1, -34.0, 58.8, 184.3); they are not in the syllabus Data section.
import json
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

E = {e['sym']: e for e in json.load(open('data/elements.json', encoding='utf-8'))}
A = {s: e['ar'] for s, e in E.items()}
facts = open('FACTS.md', encoding='utf-8').read()

# ---- Ar values used (1 d.p.)
for s, v in dict(H=1.0, O=16.0, Na=23.0, S=32.1, Cl=35.5, K=39.1, Br=79.9, Ag=107.9, I=126.9).items():
    eq("Ar " + s, A[s], v)
for s in ('F', 'Cl', 'Br', 'I'):
    assert E[s]['group'] == 17

# ---- table: electrons per molecule
eq("F2 electrons", 2 * E['F']['z'], 18)
eq("Cl2 electrons", 2 * E['Cl']['z'], 34)
eq("Br2 electrons", 2 * E['Br']['z'], 70)
eq("I2 electrons", 2 * E['I']['z'], 106)
bp = dict(F=-188, Cl=-34, Br=59, I=184)
assert bp['F'] < bp['Cl'] < bp['Br'] < bp['I']

# ---- bond energies (FACTS.md Data booklet values)
line = [l for l in facts.split('\n') if l.startswith('- Bond energies, exact')][0]
be = dict(HH=436, FF=158, ClCl=242, BrBr=193, II=151, HF=562, HCl=431, HBr=366, HI=299, NN=944)
for k, v in [("H–H", 436), ("F–F", 158), ("Cl–Cl", 242), ("Br–Br", 193), ("I–I", 151),
             ("H–F", 562), ("H–Cl", 431), ("H–Br", 366), ("H–I", 299)]:
    assert f"{k} {v}" in line, k
assert be['ClCl'] > be['BrBr'] > be['II']
assert be['FF'] < be['ClCl']
assert be['HCl'] > be['HBr'] > be['HI']

# ---- delta H of H2 + X2 -> 2HX and the reverse (per mole of equation)
dH = {}
for x, xx, hx in [('F', 158, 562), ('Cl', 242, 431), ('Br', 193, 366), ('I', 151, 299)]:
    dH[x] = (436 + xx) - 2 * hx
eq("dH F", dH['F'], -530)
eq("dH Cl", dH['Cl'], -184)
eq("dH Br", dH['Br'], -103)
eq("dH I", dH['I'], -11)
# worked example: decomposition of HCl and HI
eq("HCl broken", 2 * 431, 862)
eq("HCl made", 436 + 242, 678)
eq("dH 2HCl", 862 - 678, 184)
eq("HI broken", 2 * 299, 598)
eq("HI made", 436 + 151, 587)
eq("dH 2HI", 598 - 587, 11)
eq("dH decomposition HBr", -dH['Br'], 103)

# ---- standard electrode potentials in the note (FACTS.md)
eps = {}
for k, v in [("F₂/F⁻", 2.87), ("Cl₂/Cl⁻", 1.36), ("Br₂/Br⁻", 1.07), ("I₂/I⁻", 0.54)]:
    assert f"{k} +{v:.2f}" in facts, k
    eps[k[0:2]] = v
assert eps['F₂'] > eps['Cl'] > eps['Br'] > eps['I₂']

# ---- oxidation numbers of chlorine
eq("Cl in ClO3-", -1 - 3 * (-2), 5)
eq("Cl in HOCl", 0 - 1 - (-2), 1)
eq("Cl in ClO-", -1 - (-2), 1)
eq("Cl in NaClO3", 0 - 1 - 3 * (-2), 5)
eq("S in H2SO4", -(2 * 1 + 4 * (-2)), 6)
# electrons: five Cl- gained (5 x 1) balances one ClO3- lost (5)
eq("hot NaOH electrons", 5 * 1, 1 * 5)
# atom balance of 3Cl2 + 6NaOH -> 5NaCl + NaClO3 + 3H2O
eq("Cl balance hot", 3 * 2, 5 + 1)
eq("Na balance hot", 6, 5 + 1)
eq("O balance hot", 6, 3 + 3)
eq("H balance hot", 6, 3 * 2)
# cold: Cl2 + 2NaOH -> NaCl + NaClO + H2O
eq("O balance cold", 2, 1 + 1)
eq("H balance cold", 2, 2)

# ---- sulfur electrons per H2SO4 in the iodide reactions: 2HI/6HI/8HI
eq("e- to SO2", 6 - 4, 2)
eq("e- to S", 6 - 0, 6)
eq("e- to H2S", 6 - (-2), 8)
# atom balance of the three iodide equations
# 2HI + H2SO4 -> I2 + SO2 + 2H2O ; H: 2+2 = 4 ; O: 4 = 2 + 2
eq("H 2HI", 2 + 2, 2 * 2); eq("O 2HI", 4, 2 + 2)
# 6HI + H2SO4 -> 3I2 + S + 4H2O ; H: 6+2 = 8 ; O: 4
eq("H 6HI", 6 + 2, 4 * 2); eq("O 6HI", 4, 4)
# 8HI + H2SO4 -> 4I2 + H2S + 4H2O ; H: 8+2 = 10 = 2 + 8 ; O: 4
eq("H 8HI", 8 + 2, 2 + 4 * 2); eq("O 8HI", 4, 4)
# 2HBr + H2SO4 -> Br2 + SO2 + 2H2O
eq("H 2HBr", 2 + 2, 2 * 2); eq("O 2HBr", 4, 2 + 2)

# ---- worked example: mass of AgCl from 25.0 cm3 of 0.0800 mol/dm3 NaCl
Mr_AgCl = A['Ag'] + A['Cl']
eq("Mr AgCl", Mr_AgCl, 143.4, 1e-9)
n = 0.0800 * 25.0 / 1000
eq("n NaCl", n, 2.00e-3)
eq("m AgCl", sf(n * Mr_AgCl), 0.287)

# ---- worked example: 4.80 dm3 Cl2 -> NaClO
Mr_NaClO = A['Na'] + A['Cl'] + A['O']
eq("Mr NaClO", Mr_NaClO, 74.5, 1e-9)
nCl2 = 4.80 / 24.0
eq("n Cl2", nCl2, 0.200)
eq("m NaClO", sf(nCl2 * Mr_NaClO), 14.9)

# ---- worked example (real context): 2.0e6 dm3 at 0.50 mg/dm3
Mr_Cl2 = 2 * A['Cl']
eq("Mr Cl2", Mr_Cl2, 71.0)
m_mg = 0.50 * 2.0e6
eq("dose mass mg", m_mg, 1.0e6)
eq("dose mass g", m_mg / 1000, 1.0e3)
nd = (m_mg / 1000) / Mr_Cl2
eq("dose n", round(nd, 2), 14.08)
eq("dose V", sf(nd * 24.0), 338)

# ---- exam: pool 5.0e4 dm3 at 2.0 mg/dm3
m2 = 2.0 * 5.0e4 / 1000
eq("pool mass g", m2, 100)
n2 = m2 / Mr_Cl2
eq("pool n", round(n2, 3), 1.408)
eq("pool V", sf(n2 * 24.0), 33.8)

# ---- exam: moles quiz 0.250 mol Cl2
eq("quiz V", 0.250 * 24.0, 6.00)
eq("quiz wrong stp", round(0.250 * 22.4, 2), 5.60)
eq("quiz wrong ratio", 0.500 * 24.0, 12.0)

# ---- stretch 1: bleach titration
nS = 0.100 * 21.40 / 1000
eq("n S2O3", nS, 2.140e-3)
nI2 = nS / 2
eq("n I2", nI2, 1.070e-3)
nClO_25 = nI2
nClO_250 = nClO_25 * 10
eq("n ClO 250", nClO_250, 1.070e-2)
c = nClO_250 / (10.0 / 1000)
eq("c bleach", sf(c), 1.07)
eq("g per dm3", sf(c * Mr_NaClO), 79.7)

# ---- stretch 2: KX / AgX
mKX, mAgX = 1.190, 1.878
# mKX (107.9 + Ar) = mAgX (39.1 + Ar)
Ar = (mAgX * A['K'] - mKX * A['Ag']) / (mKX - mAgX)
eq("Ar X", sf(Ar, 3), 79.9)
eq("lhs const", round(mKX * A['Ag'], 1), 128.4)
eq("rhs const", round(mAgX * A['K'], 2), 73.43)
eq("coefficient", round(mAgX - mKX, 3), 0.688)
eq("difference", round(mKX * A['Ag'] - mAgX * A['K'], 2), 54.97)
eq("Ar bromine", A['Br'], 79.9)
# check that AgBr from 1.190 g KBr would give 1.878 g
Mr_KBr = A['K'] + A['Br']
eq("AgBr from KBr", sf((mKX / Mr_KBr) * (A['Ag'] + A['Br']), 4), 1.878)

# ---- pH not used; first ionisation energies shown by the widget are from FACTS.md
for s, v in dict(F=1680, Cl=1260, Br=1140, I=1010).items():
    assert f"{s} {v}" in facts, s

print("ok")
