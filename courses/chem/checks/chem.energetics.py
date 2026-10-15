# checks/chem.energetics.py: recomputes every number in the Chemical energetics chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.).
import json
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
c = 4.18
R = 8.31

# ---- warm-up
eq("NaOH Mr", A['Na'] + A['O'] + A['H'], 40.0)
eq("NaOH n", 2.00 / 40.0, 0.0500)
eq("HCl n", 1.00 * 50.0 / 1000, 0.0500)

# ---- worked example: neutralisation, 50.0 g, 6.8 K
q = 50.0 * c * 6.8
eq("neut q", sf(q, 4), 1421, 1)
eq("neut n", 1.00 * 25.0 / 1000, 0.0250)
dH = -q / 0.0250
eq("neut dH kJ", sf(dH / 1000, 3), -56.8)
eq("neut dH J (-56 848)", round(dH), -56848)

# ---- displacement Zn + CuSO4
n = 0.200 * 25.0 / 1000
eq("disp n", n, 0.00500)
q = 25.0 * c * 10.4
eq("disp q", sf(q, 4), 1087, 1)
eq("disp dH", sf(-q / n / 1000, 3), -217)

# ---- dissolving NH4NO3
Mr = 2 * A['N'] + 4 * A['H'] + 3 * A['O']
eq("NH4NO3 Mr", Mr, 80.0)
n = 4.00 / Mr
eq("NH4NO3 n", n, 0.0500)
q = 50.0 * c * (-6.1)
eq("dissolve q", sf(q, 4), -1275, 1)
eq("dissolve dH", sf(-q / n / 1000, 3), 25.5)

# ---- ethanol burner
Mr = 2 * A['C'] + 6 * A['H'] + A['O']
eq("EtOH Mr", Mr, 46.0)
n = 0.78 / Mr
eq("EtOH n", sf(n, 4), 0.01696, 1e-9)
q = 200 * c * 20.0
eq("EtOH q", q, 16720)
dH = -q / n / 1000
eq("EtOH dHc", sf(dH, 3), -986)
eq("EtOH 986000 J", sf(-q / n, 3), -986000, 1)
eq("EtOH percent of data book", sf(986 / 1367 * 100, 2), 72)

# ---- bond energies: methane
broken = 4 * 410 + 2 * 496
formed = 2 * 805 + 4 * 460
eq("CH4 broken parts", 1640 + 992, 2632)
eq("CH4 broken", broken, 2632)
eq("CH4 formed parts", 1610 + 1840, 3450)
eq("CH4 formed", formed, 3450)
eq("CH4 dH", broken - formed, -818)
# ethene + H2
eq("hydrogenation", (610 + 436) - (350 + 2 * 410), -124)
eq("hydrogenation parts", 610 + 436, 1046)
eq("hydrogenation formed", 350 + 2 * 410, 1170)
# Haber
eq("Haber broken", 944 + 3 * 436, 2252)
eq("Haber formed", 6 * 390, 2340)
eq("Haber dH", 2252 - 2340, -88)
# unknown O-H
b = 2 * 436 + 496
eq("OH broken", b, 1368)
E = (b + 484) / 4
eq("OH 4E", b + 484, 1852)
eq("OH E", E, 463)

# ---- Hess: blast furnace
eq("furnace products", 3 * -394, -1182)
eq("furnace reactants", -824 + 3 * -111, -1157)
eq("furnace dH", -1182 - (-1157), -25)
# hand warmer
eq("handwarmer total", 2 * -824, -1648)
eq("handwarmer per mol Fe", 1648 / 4, 412)
nFe = 10.0 / A['Fe']
eq("handwarmer n", sf(nFe, 4), 0.1792, 1e-9)
eq("handwarmer kJ", sf(nFe * 412, 3), 73.8)
# ethanol formation from combustion
eq("EtOH Hc react parts", 2 * -394 + 3 * -286, -1646)
eq("EtOH 788", 2 * 394, 788)
eq("EtOH 858", 3 * 286, 858)
eq("EtOH dHf", (2 * -394 + 3 * -286) - (-1367), -279)
# propane
eq("propane CO2 H2O", 3 * -394 + 4 * -286, -2326)
eq("propane 1182", 3 * 394, 1182)
eq("propane 1144", 4 * 286, 1144)
eq("propane dHc", (3 * -394 + 4 * -286) - (-105), -2221)
# CaCO3 cycle
eq("CaCO3 dH", -15 - (-194), 179)
# CO
eq("CO dHf", -394 - (-283), -111)
# fuels per gram
eq("H2 per g", 286 / (2 * A['H']), 143)
Moct = 8 * A['C'] + 18 * A['H']
eq("octane Mr", Moct, 114.0)
eq("octane per g", sf(5470 / Moct, 3), 48.0)

# ---- try questions
eq("try3 q", 75.0 * c * 8.0, 2508)
q = 40.0 * c * (-3.5)
eq("try4 q", sf(q, 3), -585, 1)
eq("try4 dH", sf(-q / 0.0200 / 1000, 3), 29.3)
eq("try4 J", sf(-q / 0.0200, 4), 29260, 1)
eq("try5", (410 + 242) - (340 + 431), -119)
eq("try5 broken", 410 + 242, 652)
eq("try5 formed", 340 + 431, 771)
eq("try6 products", 2 * -286, -572)
eq("try6 reactants", 2 * -188, -376)
eq("try6 dH", -572 - (-376), -196)
eq("try7", 2 * 40, 80)

# ---- exam practice
q = 100.0 * c * 13.5
eq("q3 q", q, 5643)
eq("q3 n", 2.00 * 50.0 / 1000, 0.100)
eq("q3 dH J", sf(-q / 0.100, 4), -56430, 1)
eq("q3 dH", sf(-q / 0.100 / 1000, 3), -56.4)
eq("q4 broken", 610 + 366, 976)
eq("q4 formed", 350 + 410 + 280, 1040)
eq("q4 dH", 976 - 1040, -64)
Mm = A['C'] + 4 * A['H'] + A['O']
eq("methanol Mr", Mm, 32.0)
n = 0.64 / Mm
eq("methanol n", n, 0.0200)
q = 150 * c * 18.0
eq("methanol q", q, 11286)
eq("methanol dH", sf(-q / n / 1000, 3), -564)
eq("q7 broken", 944 + 3 * 436, 2252)
eq("q7 formed", 6 * 390, 2340)
eq("q7 dH", 2252 - 2340, -88)
eq("q7 formation dH", 2 * -46 - 0, -92)
eq("q8 H2 n", 1000 / (2 * A['H']), 500)
eq("q8 H2 kJ", 500 * 286, 143000)
nO = 1000 / Moct
eq("q8 octane n", sf(nO, 4), 8.772, 1e-9)
eq("q8 octane kJ", sf(nO * 5470, 4), 47980, 10)
V = 500 * R * 298 / 101000
eq("q8 V m3", sf(V, 3), 12.3)
# stretch
eq("s1 dH", -66.1 - 11.7, -77.8)
eq("s2 condense", 2 * 44.0, 88.0)
eq("s2 dH", -818 - 88.0, -906)
eq("s2 gap", abs(-906 - (-890)), 16)

# ---- quiz
q = 100 * c * 5.0
eq("quiz q", q, 2090)
eq("quiz dH", sf(q / 1000 / 0.0500, 3), 41.8)
eq("quiz forgot n", sf(q / 1000, 3), 2.09)
print("ok")
