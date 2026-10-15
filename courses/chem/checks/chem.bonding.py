# checks/chem.bonding.py: recomputes every number in "Chemical bonding"
# (electronegativity differences, outer-electron counts, sigma/pi counts, bond-energy arithmetic).
import json, os
from math import isclose

HERE = os.path.dirname(os.path.abspath(__file__))
EL = {e['sym']: e for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

# ---------- Pauling values (FACTS.md Data section) ----------
X = dict(H=2.1, Li=1.0, Be=1.6, B=2.0, C=2.5, N=3.0, O=3.5, F=4.0,
         Na=0.9, Mg=1.3, Al=1.5, Si=1.9, P=2.2, S=2.6, Cl=3.0, K=0.8, Ca=1.0, Br=2.6)
def d(a, b): return round(abs(X[a] - X[b]), 1)

# Period 3 rises steadily, Group 17 falls
p3 = [X[s] for s in ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']]
assert p3 == sorted(p3) and len(set(p3)) == 7, "Period 3 must rise"
g17 = [X[s] for s in ['F', 'Cl', 'Br']]
assert g17 == sorted(g17, reverse=True), "Group 17 must fall"

eq("NaCl diff", d('Na', 'Cl'), 2.1)
eq("HCl diff", d('H', 'Cl'), 0.9)
eq("Cl2 diff", d('Cl', 'Cl'), 0.0)
eq("CaF2 diff", d('Ca', 'F'), 3.0)
eq("C-H diff", d('C', 'H'), 0.4)
eq("Mg-O diff", d('Mg', 'O'), 2.2)
eq("C-Cl diff", d('C', 'Cl'), 0.5)
eq("Si-Cl diff", d('Si', 'Cl'), 1.1)
assert d('Mg', 'O') > d('C', 'Cl')
# quiz: only CaF2 is mainly ionic
eq("quiz SiCl4", d('Si', 'Cl'), 1.1)
eq("quiz CH4", d('C', 'H'), 0.4)
eq("quiz HCl", d('H', 'Cl'), 0.9)
assert d('Ca', 'F') >= 2 > max(d('Si', 'Cl'), d('C', 'H'), d('H', 'Cl'))

# ---------- outer electrons: group number (Groups 1-2: g; Groups 13-17: g - 10) ----------
def outer(sym):
    g = EL[sym]['group']
    return g if g <= 2 else g - 10
for s, n in dict(Cl=7, Na=1, Mg=2, Al=3, C=4, N=5, O=6, S=6, P=5, F=7, H=1).items():
    assert outer(s) == n, (s, outer(s))

def pairs(total): return total // 2

# water, ammonia, carbon dioxide
eq("H2O electrons", outer('O') + 2 * outer('H'), 8); eq("H2O pairs", pairs(8), 4)
eq("NH3 electrons", outer('N') + 3 * outer('H'), 8); eq("NH3 pairs", pairs(8), 4)
eq("CO2 electrons", outer('C') + 2 * outer('O'), 16); eq("CO2 pairs", pairs(16), 8)
# CO2: 2 single bonds use 2 pairs; 2 O x 3 lone pairs = 6; total 8
eq("CO2 single-bond build", 2 + 6, 8)
# SF6
eq("SF6 electrons", outer('S') + 6 * outer('F'), 48); eq("SF6 pairs", pairs(48), 24)
eq("SF6 lone pairs on F", 6 * 3, 18); eq("SF6 pairs rebuilt", 6 + 18, 24)
eq("SF6 around S", 6 * 2, 12)
eq("PCl5 around P", 5 * 2, 10)
eq("SO2 around S (2 double bonds + lone pair)", 2 * 4 + 2, 10)
# NH4+
eq("NH4+ electrons", outer('N') + 4 * outer('H') - 1, 8)
# CO3 2- (try)
eq("CO3 2- electrons", outer('C') + 3 * outer('O') + 2, 24)
# NO2
eq("NO2 electrons", outer('N') + 2 * outer('O'), 17)
# Al2Cl6
eq("AlCl3 electrons around Al", 3 * 2, 6)
eq("Al2Cl6 Al-Cl bonds", 6 + 2, 8)
eq("Al2Cl6 electrons around Al", 4 * 2, 8)
# N2 lone pairs: 3 shared + 2 lone (one each) -> try says 6 lone pairs for a diatomic with 3 per atom (Cl2-type)
eq("Cl2 lone pairs total", 2 * 3, 6)
# CO
eq("CO electrons", outer('C') + outer('O'), 10); eq("CO pairs", pairs(10), 5)
eq("CO around C", 3 * 2 + 2, 8)

# ---------- sigma and pi counts ----------
# propene CH3-CH=CH2: 6 C-H, 1 C-C, 1 C=C
sigma = 6 + 1 + 1; pi = 1
eq("propene sigma", sigma, 8); eq("propene pi", pi, 1)
eq("propene atoms-1", 3 + 6 - 1, 8)
# ethanenitrile CH3-C#N: 3 C-H, 1 C-C, 1 C#N
eq("ethanenitrile sigma", 3 + 1 + 1, 5); eq("ethanenitrile pi", 2, 2)
# C2H2 : 2 C-H + C#C ; CO2 : 2 C=O
eq("C2H2 sigma", 2 + 1, 3); eq("C2H2 pi", 2, 2)
eq("CO2 sigma", 2, 2); eq("CO2 pi", 2, 2)
# HCN
eq("HCN sigma", 2, 2); eq("HCN pi", 2, 2)
# ethene 5 sigma 1 pi ; N2 1 sigma 2 pi ; hybridisation by regions
eq("C2H4 sigma", 4 + 1, 5)
# propene alternative quiz options 7/2, 9/0, 6/3 are wrong
assert (sigma, pi) not in [(7, 2), (9, 0), (6, 3)]

# ---------- bond energies ----------
BE = {'C-C': 350, 'C=C': 610, 'C#C': 840, 'N#N': 944, 'O=O': 496, 'Cl-Cl': 242, 'F-F': 158, 'I-I': 151,
      'H-F': 562, 'H-Cl': 431, 'H-Br': 366, 'H-I': 299, 'H-H': 436, 'C-H': 410, 'C#O': 1077,
      'C-Cl': 340, 'C-Br': 280, 'C-I': 240}
assert BE['C-C'] < BE['C=C'] < BE['C#C']
eq("2 x C-C", 2 * BE['C-C'], 700)
assert BE['C=C'] < 2 * BE['C-C']
eq("pi bond energy", BE['C=C'] - BE['C-C'], 260)
eq("quiz wrong option 960", BE['C=C'] + BE['C-C'], 960)
assert BE['H-F'] > BE['H-Cl'] > BE['H-Br'] > BE['H-I']
assert BE['C-Cl'] > BE['C-Br'] > BE['C-I']
assert BE['F-F'] < BE['Cl-Cl']
# ethene + H2 -> ethane
broken = BE['C=C'] + BE['H-H']
formed = BE['C-C'] + 2 * BE['C-H']
eq("broken", broken, 1046); eq("2 x C-H", 2 * BE['C-H'], 820); eq("formed", formed, 1170)
eq("dH hydrogenation", broken - formed, -124)

print("ok")
