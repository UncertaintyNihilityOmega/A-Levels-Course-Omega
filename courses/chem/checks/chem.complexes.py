# checks/chem.complexes.py: recomputes every number in "Complexes: colour, isomerism and stability".
# Kstab values are rounded textbook values quoted in the chapter as data (exam questions give them).
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=2):
    return float(f"{x:.{k}g}")

# d-electron counts (4s lost first): Z, charge
def dcount(z, q):
    nd, s4 = z - 20, 2
    if z == 24: nd, s4 = 5, 1
    if z == 29: nd, s4 = 10, 1
    for _ in range(q):
        if s4: s4 -= 1
        else: nd -= 1
    return nd
for name, z, q, d in [('Sc3+', 21, 3, 0), ('Ti3+', 22, 3, 1), ('Cr3+', 24, 3, 3), ('Fe3+', 26, 3, 5), ('Cu2+', 29, 2, 9),
                      ('Cu+', 29, 1, 10), ('Zn2+', 30, 2, 10), ('Mn2+', 25, 2, 5), ('Ni2+', 28, 2, 8)]:
    eq("d count " + name, dcount(z, q), d)

# cn
eq("cn Ni(en)3", 3 * 2, 6)

# particles for the chelate effect: Cu(H2O)6 + 4NH3 -> ... + 4H2O (5 -> 5); Cu(H2O)6 + EDTA -> Cu(EDTA) + 6H2O (2 -> 7)
eq("particles ammine left", 1 + 4, 5); eq("particles ammine right", 1 + 4, 5)
eq("particles EDTA left", 1 + 1, 2); eq("particles EDTA right", 1 + 6, 7)
eq("particles Cu(NH3)4 + EDTA left", 1 + 1, 2); eq("particles right", 1 + 4 + 2, 7)

# worked example: free Cu2+ aq
K = 1.1e13
eq("free Cu eg", sf(0.0100 / (K * 0.960 ** 4), 3), 1.07e-15, 1e-18)
# Kstab from concentrations
eq("Kstab Cu from data", sf(2.50e-3 / (1.4e-13 * 0.200 ** 4), 2), 1.1e13, 1e10)
# exchange constant, silver
eq("Ag exchange K", sf(2.9e13 / 1.6e7, 2), 1.8e6, 1e3)
# EDTA vs ammine
eq("EDTA/ammine ratio", sf(6.3e18 / 1.1e13, 2), 5.7e5, 1e3)
# try questions
eq("try Ag+ free", sf(0.00500 / (1.6e7 * 0.490 ** 2), 3), 1.30e-9, 1e-12)
# exam practice
eq("exam Cu free", sf(0.0200 / (K * 0.500 ** 4), 2), 2.9e-14, 1e-16)
eq("0.5^4 K", K * 0.500 ** 4, 6.875e11, 1e8)
eq("exam Kstab Ag", sf(0.0400 / (2.5e-8 * 0.300 ** 2), 2), 1.8e7, 1e4)
eq("exam exchange", sf(6.3e18 / 1.1e13, 2), 5.7e5, 1e3)
# quiz
eq("quiz Kstab", sf(0.100 / (1.0e-6 * 0.500 ** 2), 2), 4.0e5, 1e2)
# oxidation state of Pt in cisplatin
eq("Pt ox state", 0 - 2 * -1, 2)
# stereoisomer count for [Co(en)2Cl2]+: cis (2 enantiomers) + trans (1)
eq("isomers Co(en)2Cl2", 2 + 1, 3)
# fix: Planck constant quoted in the colour section
eq("Planck constant mantissa", 6.626e-34 / 1e-34, 6.63, 0.005)

print("ok")
