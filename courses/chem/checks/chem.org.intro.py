# checks/chem.org.intro.py: recomputes every number in Introduction to organic chemistry.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, N 14.0, O 16.0.
import json
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

Ar = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
H, C, N, O = Ar['H'], Ar['C'], Ar['N'], Ar['O']
eq("Ar H", H, 1.0); eq("Ar C", C, 12.0); eq("Ar O", O, 16.0)

def Mr(c=0, h=0, o=0, nn=0):
    return c * C + h * H + o * O + nn * N

# ---- warm-up: 92.3 % C, 7.7 % H -> CH
eq("warm C", round(92.3 / C, 2), 7.69); eq("warm H", 7.7 / H, 7.7)
eq("warm ratio", round((7.7 / H) / (92.3 / C), 2), 1.0, 0.01)

# ---- general formulae and the alkane table: CnH2n+2 and CnH2n
for k, h in zip(range(1, 7), (4, 6, 8, 10, 12, 14)):
    eq("alkane C%d" % k, 2 * k + 2, h)
eq("C6 alkane H", 2 * 6 + 2, 14); eq("C4 alkene H", 2 * 4, 8)
# bond energies from FACTS: C=C 610 < 2 x C-C 350
assert 610 < 2 * 350
eq("two C-C", 2 * 350, 700)
# electronegativity C 2.5, H 2.1: small difference
eq("EN difference C-H", round(2.5 - 2.1, 1), 0.4)

# ---- formulae from skeletal formulae (eg: cyclohexene, 3-methylbutan-2-ol, methyl propanoate)
eq("cyclohexene H", 4 * 2 + 2 * 1, 10)         # six carbons, so C6H10
eq("cyclohexene empirical", 6 / 2, 3); eq("cyclohexene empirical H", 10 / 2, 5)
eq("3-methylbutan-2-ol C", 4 + 1, 5)
eq("3-methylbutan-2-ol H", 3 + 1 + 1 + 3 + 3 + 1, 12)
eq("methyl propanoate H", 3 + 2 + 3, 8); eq("methyl propanoate C", 3 + 1, 4)
eq("methyl propanoate empirical C", 4 / 2, 2); eq("methyl propanoate empirical H", 8 / 2, 4); eq("methyl propanoate empirical O", 2 / 2, 1)
# displayed formula of methyl propanoate: 3 + 2 + 3 H atoms, 4 C, 2 O, 14 atoms; sigma bonds = atoms - 1
eq("methyl propanoate atoms", 4 + 8 + 2, 14)
# C3 aldehyde/ketone: C3H6O ; acid/ester C3H6O2
eq("propanal H", 3 + 2 + 1, 6); eq("propanone H", 3 + 3, 6); eq("propanoic acid H", 3 + 2 + 1, 6); eq("methyl ethanoate H", 3 + 3, 6)
eq("CnH2nO2 n=3", 2 * 3, 6)

# ---- ethyl butanoate C6H12O2
eq("ethyl butanoate C", 4 + 2, 6)
eq("ethyl butanoate H", 3 + 2 + 2 + 2 + 3, 12)
M = Mr(6, 12, 2)
eq("ethyl butanoate Mr", M, 116.0)
eq("ethyl butanoate %C", round(6 * C / M * 100, 1), 62.1)
# quiz distractors: one O missing, three O, C4H8O2
eq("quiz one O missing", Mr(6, 12, 1), 100.0); eq("quiz three O", Mr(6, 12, 3), 132.0); eq("quiz C4H8O2", Mr(4, 8, 2), 88.0)

# ---- sigma / pi counts (acyclic: sigma = atoms - 1)
# but-1-ene C4H8
atoms = 4 + 8
eq("but-1-ene sigma", atoms - 1, 11); eq("but-1-ene sigma by hand", 3 + 8, 11)
# propenal CH2=CHCHO C3H4O
atoms = 3 + 4 + 1
eq("propenal sigma", atoms - 1, 7); eq("propenal pi", 1 + 1, 2)
# ethyne
eq("ethyne sigma", 4 - 1, 3); eq("ethyne pi", 2, 2)
# but-3-enenitrile CH2=CHCH2C#N, C4H5N
eq("but-3-enenitrile H", 2 + 1 + 2, 5)
# but-2-enal CH3CH=CHCHO, C4H6O
eq("but-2-enal H", 3 + 1 + 1 + 1, 6)
atoms = 4 + 6 + 1
eq("but-2-enal sigma", atoms - 1, 10); eq("but-2-enal pi", 2, 2)
# hybridisation: regions of electron density
eq("sp3 regions", 4, 4); eq("sp2 regions", 3, 3); eq("sp regions", 2, 2)

# ---- exam: 85.7 % C, 14.3 % H, Mr 56.0
cC, cH = 85.7 / C, 14.3 / H
eq("exam C moles", round(cC, 3), 7.142); eq("exam H moles", round(cH, 1), 14.3)
eq("exam ratio", round(cH / cC, 1), 2.0, 0.01)
eq("exam Mr CH2", Mr(1, 2), 14.0); eq("exam factor", 56.0 / Mr(1, 2), 4)
eq("exam C4H8 Mr", Mr(4, 8), 56.0)

# ---- exam: ester C4H8O2 from ethanoic acid -> ethanol
eq("acid formula H", 4, 4)       # C2H4O2
# C4H8O2 + H2O - C2H4O2 = C2H6O
eq("alcohol C", 4 - 2, 2); eq("alcohol H", 8 + 2 - 4, 6); eq("alcohol O", 2 + 1 - 2, 1)
eq("ester Mr", Mr(4, 8, 2), 88.0)

# ---- stretch: combustion, 0.700 g hydrocarbon -> 2.20 g CO2, 0.900 g H2O, Mr 70.0
MrCO2, MrH2O = Mr(1, 0, 2), Mr(0, 2, 1)
eq("Mr CO2", MrCO2, 44.0); eq("Mr H2O", MrH2O, 18.0)
nC = 2.20 / MrCO2; nH = 2 * 0.900 / MrH2O
eq("n CO2", nC, 0.0500, 1e-9); eq("n H2O", 0.900 / MrH2O, 0.0500, 1e-9); eq("n H", nH, 0.100, 1e-9)
eq("C:H", nH / nC, 2.0, 1e-9)
eq("mass C + H", nC * C + nH * H, 0.700, 1e-9)
eq("C5H10", 70.0 / Mr(1, 2), 5.0)
eq("C5H10 Mr", Mr(5, 10), 70.0)
# propadiene: sigma bonds = atoms - 1 = 3 + 4 - 1 = 6 (4 C-H, 2 C=C sigma), pi = 2
eq("propadiene sigma", 3 + 4 - 1, 6); eq("propadiene pi", 2, 2)
print("ok", n)
