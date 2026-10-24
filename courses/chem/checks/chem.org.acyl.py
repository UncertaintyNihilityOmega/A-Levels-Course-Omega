# checks/chem.org.acyl.py: recomputes every number in the Acyl chlorides chapter.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, N 14.0, O 16.0, Cl 35.5.
# Electronegativities (O 3.5, Cl 3.0, C 2.5) are the Pauling values in FACTS.md.
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

H, C, N, O, Cl = 1.0, 12.0, 14.0, 16.0, 35.5

def sp(charge=0, **atoms):
    return (atoms, charge)

def balanced(label, lhs, rhs):
    """lhs, rhs: lists of (coefficient, species) with species = (dict of atoms, charge)"""
    global n
    n += 1
    def tot(side):
        atoms, q = {}, 0
        for c, (a, ch) in side:
            for k, v in a.items():
                atoms[k] = atoms.get(k, 0) + c * v
            q += c * ch
        return atoms, q
    la, lq = tot(lhs); ra, rq = tot(rhs)
    assert la == ra and lq == rq, f"{label}: not balanced: {la} {lq} vs {ra} {rq}"

# toluene (C7H8) -> benzoate: C6H5CH3 + 2 MnO4- -> C6H5COO- + 2 MnO2 + OH- + H2O
balanced("toluene alkaline MnO4", [(1, sp(C=7, H=8)), (2, sp(-1, Mn=1, O=4))],
         [(1, sp(-1, C=7, H=5, O=2)), (2, sp(0, Mn=1, O=2)), (1, sp(-1, O=1, H=1)), (1, sp(0, H=2, O=1))])
# C6H5CH3 + 3[O] -> C6H5COOH + H2O
balanced("toluene [O]", [(1, sp(C=7, H=8)), (3, sp(O=1))], [(1, sp(C=7, H=6, O=2)), (1, sp(H=2, O=1))])
# 5 HCOOH + 2 MnO4- + 6 H+ -> 5 CO2 + 2 Mn2+ + 8 H2O
balanced("HCOOH MnO4", [(5, sp(C=1, H=2, O=2)), (2, sp(-1, Mn=1, O=4)), (6, sp(1, H=1))],
         [(5, sp(C=1, O=2)), (2, sp(2, Mn=1)), (8, sp(H=2, O=1))])
# 3 HCOOH + Cr2O7 2- + 8 H+ -> 3 CO2 + 2 Cr3+ + 7 H2O
balanced("HCOOH dichromate", [(3, sp(C=1, H=2, O=2)), (1, sp(-2, Cr=2, O=7)), (8, sp(1, H=1))],
         [(3, sp(C=1, O=2)), (2, sp(3, Cr=1)), (7, sp(H=2, O=1))])
# HCOOH + 2 Ag+ -> CO2 + 2 Ag + 2 H+
balanced("HCOOH Tollens", [(1, sp(C=1, H=2, O=2)), (2, sp(1, Ag=1))], [(1, sp(C=1, O=2)), (2, sp(Ag=1)), (2, sp(1, H=1))])
# 2 MnO4- + 5 H2C2O4 + 6 H+ -> 2 Mn2+ + 10 CO2 + 8 H2O
balanced("ethanedioic MnO4", [(2, sp(-1, Mn=1, O=4)), (5, sp(C=2, H=2, O=4)), (6, sp(1, H=1))],
         [(2, sp(2, Mn=1)), (10, sp(C=1, O=2)), (8, sp(H=2, O=1))])
# acyl chloride equations
balanced("CH3COCl + 2NH3", [(1, sp(C=2, H=3, O=1, Cl=1)), (2, sp(N=1, H=3))], [(1, sp(C=2, H=5, N=1, O=1)), (1, sp(N=1, H=4, Cl=1))])
balanced("CH3COCl + 2CH3NH2", [(1, sp(C=2, H=3, O=1, Cl=1)), (2, sp(C=1, H=5, N=1))],
         [(1, sp(C=3, H=7, N=1, O=1)), (1, sp(1, C=1, H=6, N=1)), (1, sp(-1, Cl=1))])
balanced("C6H5COCl + C6H5OH", [(1, sp(C=7, H=5, O=1, Cl=1)), (1, sp(C=6, H=6, O=1))], [(1, sp(C=13, H=10, O=2)), (1, sp(H=1, Cl=1))])
balanced("acid + PCl5", [(1, sp(C=2, H=4, O=2)), (1, sp(P=1, Cl=5))], [(1, sp(C=2, H=3, O=1, Cl=1)), (1, sp(P=1, O=1, Cl=3)), (1, sp(H=1, Cl=1))])
balanced("3 acid + PCl3", [(3, sp(C=2, H=4, O=2)), (1, sp(P=1, Cl=3))], [(3, sp(C=2, H=3, O=1, Cl=1)), (1, sp(H=3, P=1, O=3))])
balanced("acid + SOCl2", [(1, sp(C=2, H=4, O=2)), (1, sp(S=1, O=1, Cl=2))], [(1, sp(C=2, H=3, O=1, Cl=1)), (1, sp(S=1, O=2)), (1, sp(H=1, Cl=1))])

# electronegativity story
eq("EN O-C", 3.5 - 2.5, 1.0)
eq("EN Cl-C", 3.0 - 2.5, 0.5)

# worked example: yield of ethyl ethanoate
Mr_acyl = 2 * C + 3 * H + O + Cl
Mr_ester = 4 * C + 8 * H + 2 * O
eq("Mr CH3COCl", Mr_acyl, 78.5)
eq("Mr ethyl ethanoate", Mr_ester, 88.0)
nA = 7.85 / Mr_acyl
eq("eg moles", round(nA, 3), 0.100)
mmax = nA * Mr_ester
eq("eg max", round(mmax, 2), 8.80)
eq("eg yield", round(6.16 / mmax * 100, 1), 70.0)
eq("quiz moles", round(7.85 / 78.5, 3), 0.100)

# worked example: titration of ethanedioic acid
Mr_ox = 2 * H + 2 * C + 4 * O + 2 * (2 * H + O)
eq("Mr hydrated acid", Mr_ox, 126.0)
n250 = 0.9450 / Mr_ox
eq("n 250", round(n250, 5), 0.00750)
n25 = n250 / 10
eq("n 25", round(n25, 6), 0.000750)
nMn = n25 * 2 / 5
eq("n MnO4", round(nMn, 6), 3.00e-4, 1e-12)
V = nMn / 0.0200 * 1000
eq("titre cm3", round(V, 2), 15.0)

# exam practice Q3: benzoyl chloride -> phenyl benzoate
Mr_bc = 7 * C + 5 * H + Cl + O
Mr_pb = 13 * C + 10 * H + 2 * O
eq("Mr benzoyl chloride", Mr_bc, 140.5)
eq("Mr phenyl benzoate", Mr_pb, 198.0)
nb = 7.03 / Mr_bc
eq("Q3 moles", round(nb, 5), 0.05004)
mb = nb * Mr_pb
eq("Q3 max", round(mb, 3), 9.907)
eq("Q3 yield", round(7.45 / mb * 100, 1), 75.2)

# W: C4H7ClO is butanoyl chloride
eq("W formula H count", 3 + 2 + 2, 7)

print("ok")
