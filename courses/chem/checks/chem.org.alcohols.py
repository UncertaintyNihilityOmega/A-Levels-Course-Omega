# checks/chem.org.alcohols.py: recomputes every number in "Alcohols".
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0.
# Boiling points quoted (to the nearest degree, standard-table values, not recomputed):
# ethane -89, methanol 65, propane -42, ethanol 78, propan-1-ol 97, butan-1-ol 118, propanal 49, propanoic acid 141.
# Electronegativities O 3.5, H 2.1 are from FACTS.md (Data section).
import json
from math import isclose
from collections import Counter

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
H, C, O = A['H'], A['C'], A['O']
eq("Ar H", H, 1.0); eq("Ar C", C, 12.0); eq("Ar O", O, 16.0)

def Mr(c, h, o=0): return c * C + h * H + o * O

# --- boiling point table Mr values
eq("Mr ethane", Mr(2, 6), 30.0)
eq("Mr methanol", Mr(1, 4, 1), 32.0)
eq("Mr propane", Mr(3, 8), 44.0)
eq("Mr ethanol", Mr(2, 6, 1), 46.0)
eq("Mr propan-1-ol", Mr(3, 8, 1), 60.0)
eq("Mr butan-1-ol", Mr(4, 10, 1), 74.0)
eq("ethanol vs propane b.p. gap", 78 - (-42), 120)

# --- fermentation example: 1.00 kg glucose
Mr_glu = Mr(6, 12, 6)
eq("Mr glucose", Mr_glu, 180.0)
n_glu = 1000 / Mr_glu
eq("n glucose", round(n_glu, 3), 5.556)
n_eth = 2 * n_glu
eq("n ethanol", round(n_eth, 2), 11.11)
eq("m ethanol g", round(n_eth * Mr(2, 6, 1)), 511)
assert 0.5 < (n_eth * 46.0) / 1000 < 0.52     # "just over half the mass of glucose"

# --- ester yield example: 7.20 g propan-1-ol -> 9.10 g propyl ethanoate
Mr_ester3 = Mr(5, 10, 2)
eq("Mr propyl ethanoate", Mr_ester3, 102.0)
n1 = 7.20 / Mr(3, 8, 1)
eq("eg n propanol", round(n1, 4), 0.1200)
eq("eg max ester", round(n1 * Mr_ester3, 2), 12.24)
eq("eg % yield", round(9.10 / (n1 * Mr_ester3) * 100, 1), 74.3)

# --- exam Q3: 9.20 g ethanol -> 14.3 g ethyl propanoate
n2 = 9.20 / Mr(2, 6, 1)
eq("Q3 n", round(n2, 4), 0.2000)
eq("Q3 max", round(n2 * Mr(5, 10, 2), 2), 20.40)
eq("Q3 %", round(14.3 / (n2 * Mr(5, 10, 2)) * 100, 1), 70.1)

# --- exam Q: dichromate titration
n_cr = 0.0200 * 0.0500
eq("Q n dichromate", n_cr, 1.000e-3, 1e-12)
n_et = n_cr * 3 / 2
eq("Q n ethanol", n_et, 1.500e-3, 1e-12)
eq("Q mass ethanol", round(n_et * 46.0, 4), 0.0690)

# --- quiz: 4.60 g ethanol -> ethyl ethanoate (Mr 88.0)
Mr_ee = Mr(4, 8, 2)
eq("Mr ethyl ethanoate", Mr_ee, 88.0)
nq = 4.60 / 46.0
eq("quiz n", round(nq, 3), 0.100)
eq("quiz max ester", round(nq * Mr_ee, 2), 8.80)
eq("quiz distractor x2", 17.6, 2 * 8.80)
eq("quiz distractor half", 4.40, 8.80 / 2)

# --- balanced equations (atoms and charge)
def side(items):
    t = Counter(); q = 0
    for coef, f, ch in items:
        for k, v in f.items(): t[k] += coef * v
        q += coef * ch
    return t, q
def bal(left, right, label):
    assert side(left) == side(right), f"unbalanced: {label}: {side(left)} vs {side(right)}"

# 3 propan-1-ol + Cr2O7 2- + 8H+ -> 3 propanal + 2Cr3+ + 7H2O
bal([(3, {'C': 3, 'H': 8, 'O': 1}, 0), (1, {'Cr': 2, 'O': 7}, -2), (8, {'H': 1}, 1)],
    [(3, {'C': 3, 'H': 6, 'O': 1}, 0), (2, {'Cr': 1}, 3), (7, {'H': 2, 'O': 1}, 0)], "propanol dichromate")
# 2MnO4- + 6H+ + 5 ethanol -> 2Mn2+ + 8H2O + 5 ethanal
bal([(2, {'Mn': 1, 'O': 4}, -1), (6, {'H': 1}, 1), (5, {'C': 2, 'H': 6, 'O': 1}, 0)],
    [(2, {'Mn': 1}, 2), (8, {'H': 2, 'O': 1}, 0), (5, {'C': 2, 'H': 4, 'O': 1}, 0)], "ethanol permanganate")
# 16 H+ on the left less 10 H+ on the right = 6 H+
eq("H+ cancel", 16 - 10, 6)
# propan-1-ol + PCl5 -> 1-chloropropane + POCl3 + HCl
bal([(1, {'C': 3, 'H': 8, 'O': 1}, 0), (1, {'P': 1, 'Cl': 5}, 0)], [(1, {'C': 3, 'H': 7, 'Cl': 1}, 0), (1, {'P': 1, 'O': 1, 'Cl': 3}, 0), (1, {'H': 1, 'Cl': 1}, 0)], "PCl5 propanol")
# 3 ethanol + 2 Cr2O7 2- + 16H+ -> 3 ethanoic acid + 4Cr3+ + 11 H2O
bal([(3, {'C': 2, 'H': 6, 'O': 1}, 0), (2, {'Cr': 2, 'O': 7}, -2), (16, {'H': 1}, 1)],
    [(3, {'C': 2, 'H': 4, 'O': 2}, 0), (4, {'Cr': 1}, 3), (11, {'H': 2, 'O': 1}, 0)], "ethanol to acid")
# CH3CH2OH + 4I2 + 6OH- -> CHI3 + HCOO- + 5I- + 5H2O
bal([(1, {'C': 2, 'H': 6, 'O': 1}, 0), (4, {'I': 2}, 0), (6, {'O': 1, 'H': 1}, -1)],
    [(1, {'C': 1, 'H': 1, 'I': 3}, 0), (1, {'C': 1, 'H': 1, 'O': 2}, -1), (5, {'I': 1}, -1), (5, {'H': 2, 'O': 1}, 0)], "iodoform ethanol")
# butan-2-ol + 4I2 + 6OH- -> CHI3 + CH3CH2COO- + 5I- + 5H2O
bal([(1, {'C': 4, 'H': 10, 'O': 1}, 0), (4, {'I': 2}, 0), (6, {'O': 1, 'H': 1}, -1)],
    [(1, {'C': 1, 'H': 1, 'I': 3}, 0), (1, {'C': 3, 'H': 5, 'O': 2}, -1), (5, {'I': 1}, -1), (5, {'H': 2, 'O': 1}, 0)], "iodoform butan-2-ol")
# general: CH3CH(OH)R, shown with R = CH3 (propan-2-ol -> ethanoate)
bal([(1, {'C': 3, 'H': 8, 'O': 1}, 0), (4, {'I': 2}, 0), (6, {'O': 1, 'H': 1}, -1)],
    [(1, {'C': 1, 'H': 1, 'I': 3}, 0), (1, {'C': 2, 'H': 3, 'O': 2}, -1), (5, {'I': 1}, -1), (5, {'H': 2, 'O': 1}, 0)], "iodoform propan-2-ol")
# 2C2H5OH + 2Na -> 2C2H5ONa + H2; methanol analogue
bal([(2, {'C': 2, 'H': 6, 'O': 1}, 0), (2, {'Na': 1}, 0)], [(2, {'C': 2, 'H': 5, 'O': 1, 'Na': 1}, 0), (1, {'H': 2}, 0)], "Na ethanol")
bal([(2, {'C': 1, 'H': 4, 'O': 1}, 0), (2, {'Na': 1}, 0)], [(2, {'C': 1, 'H': 3, 'O': 1, 'Na': 1}, 0), (1, {'H': 2}, 0)], "Na methanol")
# combustion of ethanol
bal([(1, {'C': 2, 'H': 6, 'O': 1}, 0), (3, {'O': 2}, 0)], [(2, {'C': 1, 'O': 2}, 0), (3, {'H': 2, 'O': 1}, 0)], "ethanol burns")
# fermentation
bal([(1, {'C': 6, 'H': 12, 'O': 6}, 0)], [(2, {'C': 2, 'H': 6, 'O': 1}, 0), (2, {'C': 1, 'O': 2}, 0)], "fermentation")
# reductions: CH3CHO + 2[H]; CH3COOH + 4[H] -> CH3CH2OH + H2O (count H as atoms)
bal([(1, {'C': 2, 'H': 4, 'O': 1}, 0), (2, {'H': 1}, 0)], [(1, {'C': 2, 'H': 6, 'O': 1}, 0)], "reduce aldehyde")
bal([(1, {'C': 2, 'H': 4, 'O': 2}, 0), (4, {'H': 1}, 0)], [(1, {'C': 2, 'H': 6, 'O': 1}, 0), (1, {'H': 2, 'O': 1}, 0)], "reduce acid")
# oxidations with [O]
bal([(1, {'C': 2, 'H': 6, 'O': 1}, 0), (1, {'O': 1}, 0)], [(1, {'C': 2, 'H': 4, 'O': 1}, 0), (1, {'H': 2, 'O': 1}, 0)], "ethanol to ethanal")
bal([(1, {'C': 2, 'H': 6, 'O': 1}, 0), (2, {'O': 1}, 0)], [(1, {'C': 2, 'H': 4, 'O': 2}, 0), (1, {'H': 2, 'O': 1}, 0)], "ethanol to acid [O]")
bal([(1, {'C': 3, 'H': 8, 'O': 1}, 0), (2, {'O': 1}, 0)], [(1, {'C': 3, 'H': 6, 'O': 2}, 0), (1, {'H': 2, 'O': 1}, 0)], "propanol to acid [O]")
bal([(1, {'C': 3, 'H': 8, 'O': 1}, 0), (1, {'O': 1}, 0)], [(1, {'C': 3, 'H': 6, 'O': 1}, 0), (1, {'H': 2, 'O': 1}, 0)], "propan-2-ol to ketone")
# esterification
bal([(1, {'C': 2, 'H': 4, 'O': 2}, 0), (1, {'C': 2, 'H': 6, 'O': 1}, 0)], [(1, {'C': 4, 'H': 8, 'O': 2}, 0), (1, {'H': 2, 'O': 1}, 0)], "ethyl ethanoate")
bal([(1, {'C': 2, 'H': 4, 'O': 2}, 0), (1, {'C': 3, 'H': 8, 'O': 1}, 0)], [(1, {'C': 5, 'H': 10, 'O': 2}, 0), (1, {'H': 2, 'O': 1}, 0)], "propyl ethanoate")
# diol and glycerol formulas
bal([(1, {'C': 2, 'H': 4}, 0), (1, {'O': 1}, 0), (1, {'H': 2, 'O': 1}, 0)], [(1, {'C': 2, 'H': 6, 'O': 2}, 0)], "ethane-1,2-diol from ethene")

# electronegativity difference O-H (FACTS.md: O 3.5, H 2.1)
eq("O-H delta chi", round(3.5 - 2.1, 1), 1.4)

# isomer counts quoted: four C4H9OH isomers (2 primary, 1 secondary, 1 tertiary); 3 alkenes from butan-2-ol
assert 2 + 1 + 1 == 4 and 1 + 2 == 3
# iodoform: 5 I- from 4 I2 and CHI3: iodine atoms 8 = 3 + 5
eq("iodine atoms", 4 * 2, 3 + 5)
print("ok")
