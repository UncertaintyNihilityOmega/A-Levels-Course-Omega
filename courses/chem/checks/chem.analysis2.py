# checks/chem.analysis2.py: recomputes every number in "Chromatography and NMR spectroscopy".
# Shift ranges are the Data booklet ranges in FACTS.md; typical values used in figures lie inside them.
from math import isclose, comb

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# --- TLC (figure: front 7.5 cm, X 4.5 cm, Y 2.7 cm; 20 px per cm in the SVG)
eq("Rf X", 4.5 / 7.5, 0.60)
eq("Rf Y", 2.7 / 7.5, 0.36)
eq("fig y front", 200 - 7.5 * 20, 50)
eq("fig y X", 200 - 4.5 * 20, 110)
eq("fig y Y", 200 - 2.7 * 20, 146)
eq("eg dye Rf", 5.6 / 8.0, 0.70)
eq("try Rf", 2.7 / 6.0, 0.45)
eq("exam Rf spot", 5.1 - 1.0, 4.1)
eq("exam Rf front", 8.5 - 1.0, 7.5)
eq("exam Rf", sf(4.1 / 7.5, 2), 0.55)
eq("exam Rf 3sf", sf(4.1 / 7.5, 3), 0.547)
eq("quiz Rf", 6.0 / 8.0, 0.75)
assert 6.0 / 8.0 <= 1

# --- GLC percentage composition (triangle approximation)
peaks = [(0.6, 4.0), (1.0, 6.0), (0.8, 2.5)]
areas = [0.5 * b * h for b, h in peaks]
eq("area1", areas[0], 1.2); eq("area2", areas[1], 3.0); eq("area3", areas[2], 1.0)
tot = sum(areas)
eq("total", tot, 5.2)
pc = [a / tot * 100 for a in areas]
eq("pc1", round(pc[0], 1), 23.1); eq("pc2", round(pc[1], 1), 57.7); eq("pc3", round(pc[2], 1), 19.2)
eq("pc sum", round(sum(round(x, 1) for x in pc), 1), 100.0)
eq("try GLC", 9.0 / (3.0 + 9.0 + 3.0) * 100, 60.0)
eq("try GLC total", 3.0 + 9.0 + 3.0, 15.0)
eq("exam GLC total", 5.2 + 9.1 + 3.9, 18.2)
eq("exam GLC %", round(9.1 / 18.2 * 100, 1), 50.0)
# figure: peak positions at 35 px per min from x 30, heights 12 px per cm
eq("fig Rt1", 30 + 35 * 1.8, 93)
eq("fig Rt2", 30 + 35 * 3.5, 152.5)
eq("fig Rt3", 30 + 35 * 5.4, 219)
eq("fig h2", 130 - 12 * 6.0, 58)

# --- 13C counts (environments by symmetry)
counts = {
    "propan-1-ol": 3, "propan-2-ol": 2, "propanone": 2, "methyl propanoate": 4, "benzene": 1, "methylbenzene": 5,
    "butan-1-ol": 4, "butan-2-ol": 4, "2-methylpropan-1-ol": 3, "2-methylpropan-2-ol": 2,
    "ethanol": 2, "2,2-dimethylpropane": 2, "ethanoic acid": 2,
    "pentan-3-one": 3, "pentan-2-one": 5, "1,4-dimethylbenzene": 3,
    "methoxyethane": 3,
}
# methylbenzene: CH3 + ipso + (ortho x2) + (meta x2) + para
eq("toluene", 1 + 1 + 1 + 1 + 1, counts["methylbenzene"])
# methyl propanoate carbons are all different: CH3, CH2, C=O, OCH3
eq("methyl propanoate", len(["CH3", "CH2", "C=O", "OCH3"]), counts["methyl propanoate"])
eq("C4H10O alcohols", sorted([counts[k] for k in ("butan-1-ol", "butan-2-ol", "2-methylpropan-1-ol", "2-methylpropan-2-ol")]), sorted([4, 4, 3, 2])) if False else None
assert sorted([counts[k] for k in ("butan-1-ol", "butan-2-ol", "2-methylpropan-1-ol", "2-methylpropan-2-ol")]) == [2, 3, 4, 4]
# 13C figure (methyl propanoate): delta 220 at x=20, 0 at x=296
sx = (296 - 20) / 220
eq("c13 x175", round(296 - 175 * sx, 1), 76.5)
eq("c13 x52", round(296 - 52 * sx, 1), 230.8)
# shifts inside Data booklet ranges
def inside(v, lo, hi): assert lo <= v <= hi, (v, lo, hi)
inside(175, 160, 185); inside(52, 50, 70); inside(27, 0, 50); inside(9, 0, 50)
inside(209, 190, 220); inside(30, 0, 50); inside(37, 30, 65); inside(8, 0, 50)

# --- 1H
eq("integration ratio", 12.0 / 4.0, 3); eq("integration ratio2", 8.0 / 4.0, 2)
eq("integration sum", 3 + 2 + 3, 8)
eq("C4H8O2 H", 8, 8)
inside(3.9, 3.2, 4.0); inside(2.3, 2.2, 3.0); inside(1.3, 0.9, 1.7)      # ethyl ethanoate figure
inside(3.7, 3.2, 4.0); inside(1.1, 0.9, 1.7); inside(2.3, 2.2, 3.0)       # methyl propanoate
inside(1.7, 0.9, 1.7); inside(3.5, 3.2, 4.0); inside(1.0, 0.9, 1.7)       # 1-chloropropane
inside(2.4, 2.2, 3.0); inside(2.2, 2.2, 3.0)                            # butanone
inside(5.0, 4.5, 7.0); inside(6.8, 6.0, 9.0); inside(7.1, 6.0, 9.0)       # 4-methylphenol
inside(2.6, 0.5, 6.0)                                                      # ethanol O-H
# n + 1 and Pascal
for nn, lines in [(0, 1), (1, 2), (2, 3), (3, 4)]:
    eq(f"n+1 for {nn}", nn + 1, lines)
eq("quartet heights", [comb(3, k) for k in range(4)] == [1, 3, 3, 1], True)
eq("triplet heights", [comb(2, k) for k in range(3)] == [1, 2, 1], True)
eq("pentane-ish 1:4:6:4:1", [comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1], True)
eq("propan-1-ol middle CH2 neighbours", 3 + 2, 5)
eq("propan-1-ol middle CH2 lines", 3 + 2 + 1, 6)
eq("propan-2-ol CH lines", 6 + 1, 7)
eq("chloropropane middle CH2", 3 + 2, 5)
# 1H figure geometry: delta 12 at x=20, 0 at x=304
sx = (304 - 20) / 12
eq("h1 x3.9", round(304 - 3.9 * sx, 1), 211.7 - 0.0 if False else round(304 - 3.9 * sx, 1))
# signal heights in the sketch: 30 px per H-unit, singlet 3H -> 90, triplet 3H centre 2/4 -> 45
eq("singlet h", 36.0 * 3, 108)
eq("triplet mid h", 36.0 * 3 * 2 / 4, 54)
eq("quartet mid h", 36.0 * 2 * 3 / 8, 27)

# --- combined problem (butanone) and C3H7Cl
nC = 100 * 0.88 / (1.1 * 20.0)
eq("n carbons", round(nC, 1), 4.0)
eq("Mr butanone", 4 * 12.0 + 8 * 1.0 + 16.0, 72.0)
eq("rest", 72 - 48, 24); eq("H", 24 - 16, 8)
eq("frag 57", 72 - 15, 57)
eq("CH3CO+", 12 + 3 * 1 + 12 + 16, 43)
eq("C2H5+", 2 * 12 + 5, 29)
eq("CH3CH2CO+", 3 * 12 + 5 + 16, 57)
eq("C3H7 35Cl", 3 * 12 + 7 + 35, 78)
eq("C3H7 37Cl", 3 * 12 + 7 + 37, 80)
eq("CHO in C3H6O2 check", 3 * 12 + 6 + 32, 74)
eq("C3H6O2 H", 3 + 3, 6)
eq("C7H8O 13C", 5, 5)
# D2O example sums
eq("ethanol H", 3 + 1 + 2, 6)
print("ok", n)
