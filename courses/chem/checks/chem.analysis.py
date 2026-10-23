# checks/chem.analysis.py: recomputes every number in the IR and mass spectrometry chapter.
# Ar values from the 9701 Periodic Table (data/elements.json). Isotope abundances are the chapter's data.
import json, os
from math import isclose, comb

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

here = os.path.dirname(os.path.abspath(__file__))
ar = {e['sym']: e['ar'] for e in json.load(open(os.path.join(here, '..', 'data', 'elements.json'), encoding='utf-8'))}
eq("Ar Mg", ar['Mg'], 24.3); eq("Ar Cl", ar['Cl'], 35.5); eq("Ar B", ar['B'], 10.8)
eq("Ar Ne", ar['Ne'], 20.2); eq("Ar Si", ar['Si'], 28.1); eq("Ar Br", ar['Br'], 79.9)

# wavenumber example
lam = 1 / 3000
eq("lambda cm", sf(lam), 3.33e-4, 1e-9)
eq("lambda micrometres", sf(lam * 1e4), 3.33, 1e-9)

def Ar(pairs):
    return sum(m * a for m, a in pairs) / sum(a for _, a in pairs)

# Mg
eq("Mg sum", 24 * 79 + 25 * 10 + 26 * 11, 2432)
eq("Mg Ar", Ar([(24, 79), (25, 10), (26, 11)]), 24.32, 1e-9)
eq("Mg Ar 3sf", sf(Ar([(24, 79), (25, 10), (26, 11)])), 24.3)
# Cl
eq("Cl 35x", 35 * 75.8, 2653, 1e-9)
eq("Cl 37x", 37 * 24.2, 895.4, 1e-9)
eq("Cl Ar", round(Ar([(35, 75.8), (37, 24.2)]), 2), 35.48)
eq("Cl Ar 3sf", sf(Ar([(35, 75.8), (37, 24.2)])), 35.5)
# B: 10x + 11(100-x) = 1080
x = 1100 - 1080
eq("B x", x, 20)
eq("B Ar check", Ar([(10, 20), (11, 80)]), 10.8, 1e-9)
# Br from mass numbers
eq("Br Ar from mass numbers", round(Ar([(79, 50.7), (81, 49.3)]), 2), 79.99)
# Si
eq("Si sum", round(28 * 92.2 + 29 * 4.7 + 30 * 3.1, 1), 2810.9)
eq("Si Ar", sf(Ar([(28, 92.2), (29, 4.7), (30, 3.1)])), 28.1)
# Ne
eq("Ne sum", round(20 * 90.5 + 21 * 0.3 + 22 * 9.2, 1), 2018.7)
eq("Ne abundance total", round(90.5 + 0.3 + 9.2, 1), 100.0)
eq("Ne Ar", round(Ar([(20, 90.5), (21, 0.3), (22, 9.2)]), 3), 20.187)
eq("Ne Ar 3sf", sf(Ar([(20, 90.5), (21, 0.3), (22, 9.2)])), 20.2)
# quiz: 10 % mass 20, 90 % mass 22
eq("quiz Ar", Ar([(20, 10), (22, 90)]), 21.8, 1e-9)
eq("quiz simple mean", (20 + 22) / 2, 21.0)
# element E (stretch): 69x + 71(100-x) = 6970
xE = (7100 - 6970) / 2
eq("E x", xE, 65)
eq("E Ar", Ar([(69, 65), (71, 35)]), 69.7, 1e-9)
h = [0.65 ** 2, 2 * 0.65 * 0.35, 0.35 ** 2]
eq("E 138 height", round(h[0], 4), 0.4225)
eq("E 140 height", round(h[1], 4), 0.455)
eq("E 142 height", round(h[2], 4), 0.1225)
eq("E ratio a", round(h[0] / h[2], 1), 3.4)
eq("E ratio b", round(h[1] / h[2], 1), 3.7)

# [M+1] carbon counting
def nC(m, m1):
    return 100 * m1 / (1.1 * m)
eq("eg butane-like", nC(25.0, 1.10), 4.0, 1e-9)
eq("try 18.0/0.99", nC(18.0, 0.99), 5.0, 1e-9)
eq("quiz 50.0/3.30", nC(50.0, 3.30), 6.0, 1e-9)
eq("quiz no 1.1 factor", round(100 * 3.30 / 50.0, 1), 6.6)
eq("P carbons", nC(20.0, 0.66), 3.0, 1e-9)
eq("exam hydrocarbon carbons", nC(40.0, 2.64), 6.0, 1e-9)
eq("R carbons", nC(12.5, 0.55), 4.0, 1e-9)

# masses (H 1, C 12, N 14, O 16, Cl 35, Br 79 integer masses)
H, C, O, Cl, Br = 1, 12, 16, 35, 79
eq("CH3+", C + 3 * H, 15)
eq("C2H5+", 2 * C + 5 * H, 29)
eq("CHO+", C + H + O, 29)
eq("CH2OH+", C + 2 * H + O + H, 31)
eq("CH3CO+", C + 3 * H + C + O, 43)
eq("C3H7+", 3 * C + 7 * H, 43)
eq("COOH+", C + O + O + H, 45)
eq("CH3CH2CO+", 3 * C + 5 * H + O, 57)
eq("propanone Mr", 3 * C + 6 * H + O, 58)
eq("C4H10 Mr", 4 * C + 10 * H, 58)
eq("C4 H count from Mr 58", 58 - 48, 10)
eq("C3H6O2 Mr", 3 * C + 6 * H + 2 * O, 74)
eq("M - COOH", 74 - 45, 29)
eq("P: remaining after C3 and O2", 74 - 36 - 32, 6)
eq("C6H14 Mr", 6 * C + 14 * H, 86)
eq("hexane H", 86 - 72, 14)
eq("C4H8O2 Mr", 4 * C + 8 * H + 2 * O, 88)
eq("R hydrogens", 88 - 48 - 32, 8)
eq("C2H5Cl M", 2 * C + 5 * H + Cl, 64)
eq("C2H5Br M", 2 * C + 5 * H + Br, 108)
eq("CH2Cl2 M", C + 2 * H + 2 * Cl, 84)
eq("C3H7Cl M", 3 * C + 7 * H + Cl, 78)
eq("78 - Cl", 78 - Cl, 43)
eq("C3H7Br M", 3 * C + 7 * H + Br, 122)
eq("122 - Br", 122 - Br, 43)
eq("C4H9Cl M", 4 * C + 9 * H + Cl, 92)
eq("92 - Cl", 92 - Cl, 57)
eq("C4H9+", 4 * C + 9 * H, 57)
eq("CH2BrCl M", C + 2 * H + Br + Cl, 128)
eq("CH2Cl+", C + 2 * H + Cl, 49)
eq("CH2Br+", C + 2 * H + Br, 93)
eq("E2 masses", 69 + 69, 138)
eq("E2 masses b", 69 + 71, 140)
eq("E2 masses c", 71 + 71, 142)

# halogen patterns
eq("Cl2 pattern a", 3 * 3, 9)
eq("Cl2 pattern b", 2 * 3 * 1, 6)
eq("Cl2 pattern c", 1 * 1, 1)
eq("9/16", 3 / 4 * 3 / 4, 9 / 16)
eq("6/16", 2 * 3 / 4 * 1 / 4, 6 / 16)
eq("1/16", 1 / 4 * 1 / 4, 1 / 16)
eq("ClBr pattern", (3 * 1), 3)
eq("ClBr pattern mid", 3 * 1 + 1 * 1, 4)
eq("ClBr pattern end", 1 * 1, 1)
eq("3:1 heights 75/25", 75 / 25, 3.0)
print("ok")
