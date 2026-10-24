# checks/chem.transition.py: recomputes every number in "Transition elements".
# Ar from data/elements.json (9701 table); E values and ionisation energies are read from FACTS.md.
import json, re
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

AR = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
eq("Ar Fe", AR['Fe'], 55.8); eq("Ar Cu", AR['Cu'], 63.5); eq("Ar Na", AR['Na'], 23.0)
eq("Ar C", AR['C'], 12.0); eq("Ar O", AR['O'], 16.0); eq("Ar H", AR['H'], 1.0)

# --- FACTS.md data
facts = open('FACTS.md', encoding='utf-8').read()
line = [l for l in facts.splitlines() if l.startswith('- E° / V:')][0]
E = {}
for item in line[len('- E° / V:'):].strip().rstrip('.').split(';'):
    item = item.strip()
    m = re.match(r'(.+?)\s([+\-−]?\d+\.\d\d)$', item)
    assert m, item
    E[m.group(1).strip()] = float(m.group(2).replace('−', '-'))
def Ev(k): return E[k]

# --- electron configurations (4s-first filling, ions lose 4s before 3d), Sc to Zn
def config(z, q):
    d = {'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30}
    nd = z - 20             # 3d count if 4s2 (atoms Sc to Zn): Sc is 3d1 4s2
    s4 = 2
    if z == 24: nd, s4 = 5, 1
    if z == 29: nd, s4 = 10, 1
    for _ in range(q):
        if s4 > 0: s4 -= 1
        else: nd -= 1
    return nd, s4
table = [('Sc', 21, 0, 1, 2), ('Sc', 21, 3, 0, 0), ('Ti', 22, 0, 2, 2), ('Ti', 22, 3, 1, 0), ('V', 23, 0, 3, 2), ('V', 23, 3, 2, 0),
         ('V', 23, 2, 3, 0), ('Cr', 24, 0, 5, 1), ('Cr', 24, 3, 3, 0), ('Mn', 25, 0, 5, 2), ('Mn', 25, 2, 5, 0),
         ('Fe', 26, 0, 6, 2), ('Fe', 26, 2, 6, 0), ('Fe', 26, 3, 5, 0), ('Co', 27, 0, 7, 2), ('Co', 27, 2, 7, 0),
         ('Ni', 28, 0, 8, 2), ('Ni', 28, 2, 8, 0), ('Cu', 29, 0, 10, 1), ('Cu', 29, 1, 10, 0), ('Cu', 29, 2, 9, 0),
         ('Zn', 30, 0, 10, 2), ('Zn', 30, 2, 10, 0)]
for sym, z, q, nd, s4 in table:
    got = config(z, q)
    assert got == (nd, s4), f"config {sym} q={q}: {got} vs ({nd},{s4})"
    n += 1

# --- successive ionisation energies (FACTS.md)
ie_line = [l for l in facts.splitlines() if l.startswith('- Successive IE')][0]
def ies(sym):
    m = re.search(sym + r' ([\d ]+?);', ie_line)
    return [int(x) for x in m.group(1).split()]
eq("IE Ca", ies('Ca')[0], 590); eq("IE Ca2", ies('Ca')[1], 1150); eq("IE Ca3", ies('Ca')[2], 4940); eq("IE Ca4", ies('Ca')[3], 6480)
eq("IE Fe", ies('Fe')[0], 762); eq("IE Fe2", ies('Fe')[1], 1560); eq("IE Fe3", ies('Fe')[2], 2960); eq("IE Fe4", ies('Fe')[3], 5400)
assert ies('Ca')[2] / ies('Ca')[1] > 4        # "more than four times"
n += 1

# --- E values used in the chapter (V)
for k, v in [('MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O', 1.52), ('Cr₂O₇²⁻ + 14H⁺ + 6e⁻ ⇌ 2Cr³⁺ + 7H₂O', 1.33),
             ('VO₂⁺ + 2H⁺ + e⁻ ⇌ VO²⁺ + H₂O', 1.00), ('Fe³⁺/Fe²⁺', 0.77), ('I₂/I⁻', 0.54), ('Cu²⁺/Cu⁺', 0.15),
             ('VO²⁺ + 2H⁺ + e⁻ ⇌ V³⁺ + H₂O', 0.34), ('V³⁺/V²⁺', -0.26), ('V²⁺/V', -1.20), ('Zn²⁺/Zn', -0.76),
             ('Cl₂/Cl⁻', 1.36), ('Br₂/Br⁻', 1.07), ('Cu⁺/Cu', 0.52), ('Sn⁴⁺/Sn²⁺', 0.15), ('Cu²⁺/Cu', 0.34),
             ('[Fe(CN)₆]³⁻/[Fe(CN)₆]⁴⁻', 0.36), ('Fe(OH)₃/Fe(OH)₂', -0.56), ('O₂ + 2H₂O + 4e⁻ ⇌ 4OH⁻', 0.40),
             ('NO₃⁻ + 3H⁺ + 2e⁻ ⇌ HNO₂ + H₂O', 0.94), ('Co³⁺/Co²⁺', 1.82), ('O₂ + 4H⁺ + 4e⁻ ⇌ 2H₂O', 1.23)]:
    eq("E " + k, Ev(k), v)

def Ecell(red, ox): return round(red - ox, 2)
eq("warm-up Zn/Cu", Ecell(0.34, -0.76), 1.10)
eq("Fe3+ / I-", Ecell(0.77, 0.54), 0.23)
for lab, red, want in [("VO2+", 1.00, 1.76), ("VO2+ ->V3+", 0.34, 1.10), ("V3+", -0.26, 0.50), ("V2+/V", -1.20, -0.44)]:
    eq("Zn with " + lab, Ecell(red, -0.76), want)
eq("Fe2+ with VO2+", Ecell(1.00, 0.77), 0.23)
eq("Fe2+ with VO2+ -> V3+", Ecell(0.34, 0.77), -0.43)
eq("disproportionation Cu+", Ecell(0.52, 0.15), 0.37)
eq("Fe(OH)2 in air", Ecell(0.40, -0.56), 0.96)
eq("dichromate Fe2+", Ecell(1.33, 0.77), 0.56)
eq("MnO4 Fe2+", Ecell(1.52, 0.77), 0.75)
eq("MnO4 Cl-", Ecell(1.52, 1.36), 0.16)
eq("MnO4 Br-", Ecell(1.52, 1.07), 0.45)
eq("Fe3+ Sn2+", Ecell(0.77, 0.15), 0.62)
eq("Cu2+ I-", Ecell(0.15, 0.54), -0.39)
eq("O2 Co2+", Ecell(1.23, 1.82), -0.59)

# --- titration worked example: tablet
n_mno4 = 0.0100 * 12.40 / 1000
eq("tablet n MnO4", n_mno4, 1.240e-4, 1e-12)
n_fe25 = 5 * n_mno4; eq("tablet n Fe 25", n_fe25, 6.200e-4, 1e-12)
n_fe = 10 * n_fe25; eq("tablet n Fe total", n_fe, 6.200e-3, 1e-12)
m_fe = n_fe * AR['Fe']; eq("tablet mass Fe", round(m_fe, 3), 0.346)
eq("tablet mass Fe 4sf", round(m_fe, 4), 0.3460)
eq("tablet %", round(m_fe / 1.25 * 100, 1), 27.7)

# --- ethanedioate purity
n_mno4 = 0.0200 * 19.05 / 1000; eq("ox n MnO4", n_mno4, 3.810e-4, 1e-12)
n_ox25 = n_mno4 * 5 / 2; eq("ox n 25", n_ox25, 9.525e-4, 1e-12)
n_ox = 10 * n_ox25; eq("ox n total", n_ox, 9.525e-3, 1e-12)
Mr_Na2C2O4 = 2 * AR['Na'] + 2 * AR['C'] + 4 * AR['O']; eq("Mr Na2C2O4", Mr_Na2C2O4, 134.0)
mass = n_ox * Mr_Na2C2O4; eq("ox mass", round(mass, 3), 1.276)
eq("ox purity", round(mass / 1.50 * 100, 1), 85.1)

# --- brass
n_s = 0.100 * 19.65 / 1000; eq("brass n S2O3", n_s, 1.965e-3, 1e-12)
n_cu = 10 * n_s; eq("brass n Cu", n_cu, 1.965e-2, 1e-12)
m_cu = n_cu * AR['Cu']; eq("brass mass Cu", round(m_cu, 3), 1.248)
eq("brass %", round(m_cu / 2.00 * 100, 1), 62.4)

# --- spot the error
n1 = 0.0200 * 0.01840; eq("spot n MnO4", n1, 3.68e-4, 1e-12)
eq("spot wrong conc", sf(n1 / 0.0250), 0.0147)
eq("spot n Fe", 5 * n1, 1.84e-3, 1e-12)
eq("spot conc", sf(5 * n1 / 0.0250), 0.0736)

# --- try questions
eq("try Fe conc", sf(5 * 0.0200 * 0.01680 / 0.0250), 0.0672)
eq("try n MnO4 16.80", 0.0200 * 0.01680, 3.360e-4, 1e-12)
eq("try n Fe 16.80", 5 * 0.0200 * 0.01680, 1.680e-3, 1e-12)
eq("try ethanedioic n MnO4", 0.0200 * 0.02440, 4.880e-4, 1e-12)
eq("try ethanedioic n ox", 0.0200 * 0.02440 * 2.5, 1.220e-3, 1e-12)
eq("try ethanedioic conc", sf(0.0200 * 0.02440 * 2.5 / 0.0200), 0.0610)
eq("try n S2O3 14.30", 0.0500 * 0.01430, 7.15e-4, 1e-12)

# --- exam practice: iron wire
nm = 0.0100 * 0.01425; eq("wire n MnO4", nm, 1.425e-4, 1e-12)
eq("wire n Fe 20", 5 * nm, 7.125e-4, 1e-12)
eq("wire n Fe 100", 25 * nm, 3.5625e-3, 1e-12)
mw = 25 * nm * AR['Fe']; eq("wire mass", round(mw, 4), 0.1988)
eq("wire %", round(mw / 0.215 * 100, 1), 92.5)

# --- hydrated ethanedioic acid
nm = 0.0200 * 0.02510; eq("hyd n MnO4", nm, 5.020e-4, 1e-12)
eq("hyd n ox 25", nm * 2.5, 1.255e-3, 1e-12)
eq("hyd n ox 250", nm * 25, 0.01255, 1e-12)
M = 1.58 / (nm * 25); eq("hyd Mr", round(M, 1), 125.9)
Mr_acid = 2 * AR['H'] + 2 * AR['C'] + 4 * AR['O']; eq("Mr H2C2O4", Mr_acid, 90.0)
x = (M - Mr_acid) / (2 * AR['H'] + AR['O']); eq("hyd x", round(x, 1), 2.0, 0.0)
eq("hyd 18.0x", round(M - Mr_acid, 1), 35.9)

# --- copper sulfate by thiosulfate
n_s = 0.0500 * 0.02160; eq("CuSO4 n S2O3", n_s, 1.080e-3, 1e-12)
eq("CuSO4 conc", sf(n_s / 0.0250), 0.0432)

# --- quiz
eq("quiz n MnO4", 0.0200 * 0.0200, 4.00e-4, 1e-12)
eq("quiz n Fe", 5 * 0.0200 * 0.0200, 2.00e-3, 1e-12)

# --- charges of complexes
eq("charge Fe(CN)6", 3 + 6 * -1, -3)
eq("oxidation state Fe in [Fe(CN)6]4-", -4 - 6 * -1, 2)
eq("Cu in [Cu(EDTA)]2-", -2 - -4, 2)
eq("charge Cr(C2O4)3", 3 + 3 * -2, -3)
eq("Co in CoCl4 2-", -2 - 4 * -1, 2)
eq("cn Ni(en)3", 3 * 2, 6)
eq("cn Co(en)2Cl2", 2 * 2 + 2, 6)
eq("cn Cu(NH3)4(H2O)2", 4 + 2, 6)

print("ok")
