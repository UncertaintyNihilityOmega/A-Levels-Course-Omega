# checks/chem.shapes.py: recomputes every number in "Shapes of molecules and intermolecular forces"
# (electron-pair counts, ideal angles, electron counts, Mr, ice density arithmetic).
import json, os, math
from math import isclose

HERE = os.path.dirname(os.path.abspath(__file__))
EL = {e['sym']: e for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}
AR = {s: e['ar'] for s, e in EL.items()}
Z = {s: e['z'] for s, e in EL.items()}

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3): return float(f"{x:.{n}g}")

def outer(sym):
    g = EL[sym]['group']
    return g if g <= 2 else g - 10

# ---------- pair counting (the chapter's method) ----------
def count(centre, mono=0, charge=0, attached=0):
    """returns (pairs, bonding, lone). mono = H/halogen atoms; charge = ion charge (+1, -2 ...); O atoms add 0"""
    total = outer(centre) + mono - charge
    assert total % 2 == 0, (centre, total)
    pairs = total // 2
    return pairs, attached, pairs - attached

cases = {
    'CO3 2-': (count('C', 0, -2, 3), (3, 3, 0)),
    'SO2':    (count('S', 0, 0, 2), (3, 2, 1)),
    'NH4+':   (count('N', 4, +1, 4), (4, 4, 0)),
    'H3O+':   (count('O', 3, +1, 3), (4, 3, 1)),
    'BeCl2':  (count('Be', 2, 0, 2), (2, 2, 0)),
    'BF3':    (count('B', 3, 0, 3), (3, 3, 0)),
    'NO3-':   (count('N', 0, -1, 3), (3, 3, 0)),
    'SO3':    (count('S', 0, 0, 3), (3, 3, 0)),
    'CH4':    (count('C', 4, 0, 4), (4, 4, 0)),
    'NH3':    (count('N', 3, 0, 3), (4, 3, 1)),
    'H2O':    (count('O', 2, 0, 2), (4, 2, 2)),
    'PF5':    (count('P', 5, 0, 5), (5, 5, 0)),
    'SF6':    (count('S', 6, 0, 6), (6, 6, 0)),
    'PCl3':   (count('P', 3, 0, 3), (4, 3, 1)),
    'SO4 2-': (count('S', 0, -2, 4), (4, 4, 0)),
    'PH3':    (count('P', 3, 0, 3), (4, 3, 1)),
    'SiCl4':  (count('Si', 4, 0, 4), (4, 4, 0)),
    'AlCl4-': (count('Al', 4, -1, 4), (4, 4, 0)),
    'NH2-':   (count('N', 2, -1, 2), (4, 2, 2)),
    'SO3 2-': (count('S', 0, -2, 3), (4, 3, 1)),
    'SF4':    (count('S', 4, 0, 4), (5, 4, 1)),
    'ClF3':   (count('Cl', 3, 0, 3), (5, 3, 2)),
    'BrF5':   (count('Br', 5, 0, 5), (6, 5, 1)),
    'ICl4-':  (count('I', 4, -1, 4), (6, 4, 2)),
}
for name, (got, want) in cases.items():
    assert got == want, f"{name}: computed {got}, chapter says {want}"

# explicit totals quoted in the text
eq("PCl3 total", outer('P') + 3, 8); eq("SO4 total", outer('S') + 2, 8)
eq("CO3 total", outer('C') + 2, 6); eq("SO2 total", outer('S'), 6)
eq("NH4+ total", outer('N') + 4 - 1, 8); eq("H3O+ total", outer('O') + 3 - 1, 8)
eq("NH2- total", outer('N') + 2 + 1, 8); eq("ClF3 total", outer('Cl') + 3, 10)
eq("ICl4- total", outer('I') + 4 + 1, 12); eq("BeCl2 total", outer('Be') + 2, 4)
eq("PF5 total", outer('P') + 5, 10); eq("SF6 total", outer('S') + 6, 12)
eq("SO3 2- total", outer('S') + 2, 8); eq("AlCl4- total", outer('Al') + 4 + 1, 8)
eq("NO3- total", outer('N') + 1, 6)

# ---------- ideal angles ----------
def angle(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    return math.degrees(math.acos(dot / (math.sqrt(sum(a * a for a in u)) * math.sqrt(sum(b * b for b in v)))))
tet = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
eq("tetrahedral angle", round(angle(tet[0], tet[1]), 1), 109.5)
eq("cos theta", (1 * 1 + 1 * -1 + 1 * -1) / 3, -1 / 3)
for i in range(4):
    for j in range(i + 1, 4):
        eq("tetra all equal", angle(tet[i], tet[j]), angle(tet[0], tet[1]), 1e-9)
# trigonal planar
tp = [(math.cos(math.radians(a)), math.sin(math.radians(a)), 0) for a in (90, 210, 330)]
eq("trigonal planar", round(angle(tp[0], tp[1]), 6), 120)
# trigonal bipyramid
tb = [(0, 0, 1), (0, 0, -1)] + [(math.cos(math.radians(a)), math.sin(math.radians(a)), 0) for a in (0, 120, 240)]
eq("TBP axial-axial", angle(tb[0], tb[1]), 180)
eq("TBP axial-equatorial", angle(tb[0], tb[2]), 90)
eq("TBP equatorial", round(angle(tb[2], tb[3]), 6), 120)
# octahedron
oc = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
eq("octa adjacent", angle(oc[0], oc[2]), 90); eq("octa opposite", angle(oc[0], oc[1]), 180)
# lone pair effect: about 2.5 degrees per lone pair
eq("NH3 closes by", 109.5 - 107, 2.5); eq("H2O closes by", 109.5 - 104.5, 5.0)
eq("two lone pairs = 2 x one", 109.5 - 104.5, 2 * (109.5 - 107))

# ---------- electronegativity differences (Pauling, FACTS.md) ----------
X = dict(H=2.1, C=2.5, N=3.0, O=3.5, Cl=3.0)
def d(a, b): return round(abs(X[a] - X[b]), 1)
eq("C=O", d('C', 'O'), 1.0); eq("O-H", d('O', 'H'), 1.4); eq("C-Cl", d('C', 'Cl'), 0.5)
eq("C-H", d('C', 'H'), 0.4); eq("N-H", d('N', 'H'), 0.9); eq("H-Cl", d('H', 'Cl'), 0.9)
assert d('C', 'H') < d('N', 'H') < d('O', 'H')

# ---------- electrons per molecule ----------
def electrons(formula):
    import re
    total = 0
    for sym, n in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
        total += Z[sym] * (int(n) if n else 1)
    return total
for f, n in dict(F2=18, Cl2=34, Br2=70, I2=106, CH4=10, C2H6=18, C3H8=26, C4H10=34,
                 SiH4=18, GeH4=36, SnH4=54, H2O=10, H2S=18, H2Se=36, H2Te=54,
                 C3H6O=32, C3H8O=34, C5H12=42).items():
    eq(f"electrons {f}", electrons(f), n)
eq("alkane step = CH2", electrons('CH2'), 8)
assert electrons('C2H6') - electrons('CH4') == 8 == electrons('C3H8') - electrons('C2H6') == electrons('C4H10') - electrons('C3H8')
eq("I2 vs Cl2 ratio check", electrons('I2') > electrons('Cl2') and True, True)

# ---------- relative molecular masses (Ar to 1 d.p.) ----------
def mr(formula):
    import re
    t = 0.0
    for sym, n in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
        t += AR[sym] * (int(n) if n else 1)
    return t
eq("Mr propanone", round(mr('C3H6O'), 1), 58.0)
eq("Mr butane", round(mr('C4H10'), 1), 58.0)
eq("Mr propan-1-ol", round(mr('C3H8O'), 1), 60.0)

# ---------- boiling points quoted (ordering claims) ----------
# Values checked by the Specialist (REVIEW P3) against standard data (CRC Handbook; Atkins' data tables),
# rounded as quoted: CH4 -161.5, SiH4 -111.9, GeH4 -88.5, SnH4 -52; H2O 100, H2S -60.3, H2Se -41.3, H2Te -2.2;
# C2H6 -88.6, C3H8 -42.1, C4H10 -0.5; pentane 36.1, 2-methylbutane 27.8, 2,2-dimethylpropane 9.5;
# NH3 -33.3; propanone 56.1; propan-1-ol 97.2; ice density at 0 °C 0.9167 g cm-3.
bp14 = [-162, -112, -88, -52]; bp16 = [100, -60, -41, -2]
assert bp14 == sorted(bp14) and bp16[1:] == sorted(bp16[1:])
assert bp16[0] > bp16[-1]                      # water anomalous
eq("water vs methane", bp16[0] - bp14[0], 262)
# ---- boiling point against period plot (REVIEW P3, P4): data/mk_fig_hydrides.py plots exactly these eight values
eq("water above H2S", bp16[0] - bp16[1], 160)
assert -162 < -89 < -42 < -0.5                  # CH4, C2H6, C3H8, C4H10
assert 36 > 28 > 9.5                           # pentane, 2-methylbutane, neopentane
assert -162 < -33 < 100                         # methane, ammonia, water
assert 56 > -0.5 and 97 > 56                    # butane < propanone < propan-1-ol

# ---------- covalent bond versus intermolecular force ----------
oh = 460  # kJ per mol O-H bond (FACTS.md)
eq("2 O-H bonds", 2 * oh, 920)
assert 2 * oh / 41 > 20
eq("ratio", round(2 * oh / 41, 1), 22.4)

# ---------- hydrogen bonds per molecule: limited by the scarcer of H atoms and lone pairs ----------
def hbonds(h, lp): return min(h, lp)
eq("water", hbonds(2, 2), 2); eq("ammonia", hbonds(3, 1), 1)
eq("water bonds each molecule can take part in", 2 + 2, 4)

# ---------- ice and water ----------
rho_w, rho_ice = 1.00, 0.917
m = 330 * rho_w
eq("can mass", m, 330)
eq("can ice volume", sf(m / rho_ice), 360)
eq("percent increase", round((1 / rho_ice - 1) * 100), 9)
eq("percent increase can", round((m / rho_ice - 330) / 330 * 100), 9)
eq("bottle mass", 500 * rho_w, 500)
eq("bottle ice volume", sf(500 * rho_w / rho_ice), 545)
eq("1 kg ice volume", sf(1000 / rho_ice), 1090)
eq("quiz wrong option", sf(1000 * rho_ice), 917)
eq("quiz wrong 83", round(1000 - 1000 * rho_ice), 83)

print("ok")
