# checks/chem.redox.py: recomputes every number in the Redox and oxidation numbers chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.).
import json
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def same(label, got, want):
    global n
    n += 1
    assert got == want, f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}

# ---- species as (element counts, charge); an equation side is a list of (coefficient, species)
def sp(charge=0, **atoms):
    return (atoms, charge)

def side_total(side):
    atoms, ch = {}, 0
    for c, (a, q) in side:
        for k, v in a.items():
            atoms[k] = atoms.get(k, 0) + c * v
        ch += c * q
    return atoms, ch

def balanced(label, left, right):
    la, lc = side_total(left); ra, rc = side_total(right)
    same(label + " atoms", la, ra)
    same(label + " charge", lc, rc)

e_ = sp(-1)
MnO4 = sp(-1, Mn=1, O=4); Mn2 = sp(2, Mn=1); H = sp(1, H=1); H2O = sp(0, H=2, O=1)
Cr2O7 = sp(-2, Cr=2, O=7); Cr3 = sp(3, Cr=1); Fe2 = sp(2, Fe=1); Fe3 = sp(3, Fe=1)
C2O4 = sp(-2, C=2, O=4); CO2 = sp(0, C=1, O=2); I = sp(-1, I=1); I2 = sp(0, I=2)
SO3 = sp(-2, S=1, O=3); SO4 = sp(-2, S=1, O=4); H2O2 = sp(0, H=2, O=2); O2 = sp(0, O=2)
Cl2 = sp(0, Cl=2); Cl = sp(-1, Cl=1); Zn = sp(0, Zn=1); Zn2 = sp(2, Zn=1); Cu = sp(0, Cu=1); Cu2 = sp(2, Cu=1)
Cup = sp(1, Cu=1)
S2O3 = sp(-2, S=2, O=3); S4O6 = sp(-2, S=4, O=6)

# ---- oxidation numbers (sum of the oxidation numbers equals the charge)
def ox(label, x, others, charge):
    same(label, x + sum(others), charge)
ox("Mn in MnO4-", 7, [4 * -2], -1)
ox("Cr in Cr2O7 2-", 6 * 2, [7 * -2], -2); eq("Cr each", (-2 + 14) / 2, 6)
ox("S in SO4 2-", 6, [4 * -2], -2)
eq("S in S2O3 2- average", (-2 + 6) / 2, 2)
eq("N in NH4+", 1 - 4, -3)
eq("O in H2O2", (0 - 2) / 2, -1)
eq("C in CH4", 0 - 4, -4); eq("C in CH3OH", 0 - 4 + 2, -2); eq("C in HCHO", 0 - 2 + 2, 0)
eq("C in HCOOH", -(2 * 1 + 2 * -2), 2)
eq("C in CO2", -(2 * -2), 4)
eq("Fe in Fe2O3", 6 / 2, 3); eq("Mn in KMnO4", 8 - 1, 7)
eq("S in H2S", -2, -2); eq("N in NO3-", -1 + 6, 5); eq("Cl in ClO4-", -1 + 8, 7); eq("Mn in MnO2", 4, 4)
eq("Mn in MnO4 2-", -2 + 8, 6); eq("Cl in ClO3-", -1 + 6, 5); eq("S in S4O6 2-", (-2 + 12) / 4, 2.5)
eq("Cl in KClO3", -(1 - 6), 5)
eq("S in SO3 2-", -2 + 6, 4)

# ---- half-equations and ionic equations (atoms and charge)
balanced("MnO4- half", [(1, MnO4), (8, H), (5, e_)], [(1, Mn2), (4, H2O)])
balanced("Cr2O7 half", [(1, Cr2O7), (14, H), (6, e_)], [(2, Cr3), (7, H2O)])
balanced("Zn half", [(1, Zn)], [(1, Zn2), (2, e_)]); balanced("Cu half", [(1, Cu2), (2, e_)], [(1, Cu)])
balanced("Zn + Cu2+", [(1, Zn), (1, Cu2)], [(1, Zn2), (1, Cu)])
balanced("Fe half", [(1, Fe2)], [(1, Fe3), (1, e_)])
balanced("C2O4 half", [(1, C2O4)], [(2, CO2), (2, e_)]); balanced("I half", [(2, I)], [(1, I2), (2, e_)])
balanced("SO3 half", [(1, SO3), (1, H2O)], [(1, SO4), (2, H), (2, e_)])
balanced("H2O2 ox half", [(1, H2O2)], [(1, O2), (2, H), (2, e_)])
balanced("H2O2 red half", [(1, H2O2), (2, H), (2, e_)], [(2, H2O)])
balanced("Cl2 half", [(1, Cl2), (2, e_)], [(2, Cl)])
balanced("Cr + Fe", [(1, Cr2O7), (14, H), (6, Fe2)], [(2, Cr3), (7, H2O), (6, Fe3)])
balanced("MnO4 + H2O2", [(2, MnO4), (6, H), (5, H2O2)], [(2, Mn2), (8, H2O), (5, O2)])
balanced("MnO4 + Fe", [(1, MnO4), (5, Fe2), (8, H)], [(1, Mn2), (5, Fe3), (4, H2O)])
balanced("MnO4 + C2O4", [(2, MnO4), (5, C2O4), (16, H)], [(2, Mn2), (10, CO2), (8, H2O)])
balanced("H2O2 + Fe2+", [(1, H2O2), (2, Fe2), (2, H)], [(2, H2O), (2, Fe3)])
balanced("Cl2 + 2Fe2+", [(1, Cl2), (2, Fe2)], [(2, Cl), (2, Fe3)])
balanced("2Cl- half", [(2, Cl)], [(1, Cl2), (2, e_)])
balanced("S2O3 + I2", [(2, S2O3), (1, I2)], [(1, S4O6), (2, I)])
balanced("2Cu+", [(2, Cup)], [(1, Cu), (1, Cu2)])
# electron counts used in the text
eq("MnO4 e", 7 - 2, 5); eq("Cr2O7 e", 2 * (6 - 3), 6); eq("LCM 5,2", 10, 10)
eq("MnO4 H+ cancel", 16 - 10, 6); eq("Cr charge left", -2 + 14 + 12, 24); eq("Cr charge right", 6 + 18, 24)
eq("MnO4 charge left", -1 + 10 + 8, 17); eq("MnO4 charge right", 2 + 15, 17)
eq("H2O2 charge", -2 + 6, 4)
eq("Cl2 + Fe charge left", 2 * 2, 4); eq("Cl2 + Fe charge right", -2 + 6, 4)
eq("SO3 charge right", -2 + 2 - 2, -2)

# ---- whole-formula equations (atom counts)
def bal_f(label, left, right):
    la = {}; ra = {}
    for c, a in left:
        for k, v in a.items(): la[k] = la.get(k, 0) + c * v
    for c, a in right:
        for k, v in a.items(): ra[k] = ra.get(k, 0) + c * v
    same(label, la, ra)
bal_f("Cu + HNO3", [(1, dict(Cu=1)), (4, dict(H=1, N=1, O=3))], [(1, dict(Cu=1, N=2, O=6)), (2, dict(N=1, O=2)), (2, dict(H=2, O=1))])
bal_f("hot NaOH", [(3, dict(Cl=2)), (6, dict(Na=1, O=1, H=1))], [(5, dict(Na=1, Cl=1)), (1, dict(Na=1, Cl=1, O=3)), (3, dict(H=2, O=1))])
bal_f("cold NaOH", [(1, dict(Cl=2)), (2, dict(Na=1, O=1, H=1))], [(1, dict(Na=1, Cl=1)), (1, dict(Na=1, Cl=1, O=1)), (1, dict(H=2, O=1))])
bal_f("H2O2 decomposition", [(2, dict(H=2, O=2))], [(2, dict(H=2, O=1)), (1, dict(O=2))])
eq("Cu ox change", 2 - 0, 2); eq("N red change", 5 - 4, 1); eq("N total", 2 + 2, 4)
eq("hot: gain", 5 * 1, 5); eq("hot: loss", 1 * 5, 5)
eq("Cu HNO3 H", 4, 2 * 2); eq("Cu HNO3 O", 12, 6 + 4 + 2)

# ---- titrations
eq("eg1 n MnO4", 0.0200 * 22.40 / 1000, 4.48e-4, 1e-12)
eq("eg1 n Fe", 5 * 4.48e-4, 2.24e-3, 1e-12)
eq("eg1 c Fe", sf(2.24e-3 / 0.0250), 0.0896, 1e-12)
eq("tablet n MnO4", 0.0100 * 14.40 / 1000, 1.440e-4, 1e-12)
eq("tablet n Fe25", 5 * 1.440e-4, 7.20e-4, 1e-12); eq("tablet n Fe250", 7.20e-4 * 10, 7.20e-3, 1e-12)
MrFeSO4 = A['Fe'] + A['S'] + 4 * A['O']
eq("Mr FeSO4", round(MrFeSO4, 1), 151.9)
eq("tablet mass", round(7.20e-3 * MrFeSO4, 3), 1.094)
eq("tablet %", round(7.20e-3 * MrFeSO4 / 1.50 * 100, 1), 72.9)
eq("ethanedioate n", 0.0500 * 0.0250, 1.25e-3, 1e-12); eq("ethanedioate n MnO4", 1.25e-3 * 2 / 5, 5.00e-4, 1e-12)
eq("ethanedioate V", 5.00e-4 / 0.0200 * 1000, 25.0, 1e-9)
eq("try Fe n", 0.0500 * 0.0250, 1.25e-3, 1e-12); eq("try Fe n MnO4", 1.25e-3 / 5, 2.50e-4, 1e-12)
eq("try Fe V", 0.0500 * 0.0250 / 5 / 0.0200 * 1000, 12.5, 1e-9)
eq("quiz wrong 1:1", 0.0500 * 0.0250 / 0.0200 * 1000, 62.5, 1e-9)
# exam practice
eq("H2O2 n MnO4", 0.0200 * 0.02000, 4.00e-4, 1e-12); eq("H2O2 n", 4.00e-4 * 5 / 2, 1.00e-3, 1e-12)
eq("H2O2 c", 1.00e-3 / 0.0250, 0.0400, 1e-12)
MrH2O2 = 2 * A['H'] + 2 * A['O']
eq("H2O2 Mr", MrH2O2, 34.0); eq("H2O2 g/dm3", sf(0.0400 * MrH2O2), 1.36)
eq("Cu n", sf(0.635 / A['Cu']), 0.0100); eq("NO2 n", 2 * 0.0100, 0.0200); eq("NO2 V", sf(0.0200 * 24.0), 0.480)
eq("dichromate n", 0.0200 * 0.02000, 4.00e-4, 1e-12); eq("dichromate n Fe", 6 * 4.00e-4, 2.40e-3, 1e-12)
eq("dichromate c Fe", 2.40e-3 / 0.0250, 0.0960, 1e-12)
eq("thiosulfate n", 0.100 * 0.0200, 2.00e-3, 1e-12); eq("iodine n", 2.00e-3 / 2, 1.00e-3, 1e-12)
eq("iodine c", 1.00e-3 / 0.0250, 0.0400, 1e-12)
eq("S electrons", 4 * 0.5, 2)
eq("CH4 -> CO2 C change", 4 - (-4), 8); eq("Fe2O3 Fe decrease", 2 * (3 - 0), 6); eq("CO increase", 3 * (4 - 2), 6)
bal_f("Fe2O3 + CO", [(1, dict(Fe=2, O=3)), (3, dict(C=1, O=1))], [(2, dict(Fe=1)), (3, dict(C=1, O=2))])
bal_f("CH4 combustion", [(1, dict(C=1, H=4)), (2, dict(O=2))], [(1, dict(C=1, O=2)), (2, dict(H=2, O=1))])
eq("Fe in Fe2O3", 6 / 2, 3)
print("ok")
