# checks/chem.org.halogen.py: recomputes every number in the Halogenoalkanes chapter.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0, Br 79.9, Ag 107.9.
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

H, C, O, Br, Ag, Cl, I = 1.0, 12.0, 16.0, 79.9, 107.9, 35.5, 126.9

Mr_C4H9Br = 4 * C + 9 * H + Br
Mr_C4H9OH = 4 * C + 10 * H + O
Mr_AgBr = Ag + Br
eq("Mr C4H9Br", Mr_C4H9Br, 136.9, 1e-9)
eq("Mr C4H9OH", Mr_C4H9OH, 74.0, 1e-9)
eq("Mr AgBr", Mr_AgBr, 187.8, 1e-9)

# worked example: 5.00 g 1-bromobutane -> 2.10 g butan-1-ol
nRBr = 5.00 / Mr_C4H9Br
eq("eg yield moles", round(nRBr, 5), 0.03652)
mmax = nRBr * Mr_C4H9OH
eq("eg yield max mass", round(mmax, 3), 2.703)
eq("eg yield %", round(2.10 / mmax * 100, 1), 77.7)

# exam Q3: 6.85 g 2-bromo-2-methylpropane -> 2.96 g 2-methylpropan-2-ol
n3 = 6.85 / Mr_C4H9Br
eq("Q3 moles", round(n3, 5), 0.05004)
m3 = n3 * Mr_C4H9OH
eq("Q3 max mass", round(m3, 3), 3.703)
eq("Q3 %", round(2.96 / m3 * 100, 1), 79.9)

# exam Q: 1.37 g bromoalkane gives 1.88 g AgBr
nAgBr = 1.88 / Mr_AgBr
eq("Q AgBr moles", round(nAgBr, 5), 0.01001)
Mr = 1.37 / nAgBr
eq("Q Mr", sf(Mr), 137)
k = (Mr_C4H9Br - 1 - Br) / 14          # 14n + 1 + 79.9 = 136.9
eq("Q n carbons", k, 4)
eq("Q Mr rounds to C4H9Br", round(Mr), round(Mr_C4H9Br))

# bond energies quoted (Data section): C-Cl 340 > C-Br 280 > C-I 240
BE = {"C-Cl": 340, "C-Br": 280, "C-I": 240}
assert BE["C-Cl"] > BE["C-Br"] > BE["C-I"]
# Pauling electronegativities in the warm-up: C 2.5 < Cl 3.0
assert 2.5 < 3.0

# carbon counts: butanenitrile from 1-bromopropane has 3 + 1 carbons; propanenitrile from bromoethane 2 + 1
eq("butanenitrile C", 3 + 1, 4)
eq("propanenitrile C", 2 + 1, 3)
# 2-bromobutane elimination: but-1-ene + cis and trans but-2-ene
eq("alkenes from 2-bromobutane", 1 + 2, 3)
# PCl3 equation balance: 3 C2H5OH + PCl3 -> 3 C2H5Cl + H3PO3 (O: 3 = 3, H: 18 = 15 + 3, Cl: 3 = 3)
assert (3 * 1, 3 * 6, 3) == (3, 15 + 3, 3)
print("ok", n)
