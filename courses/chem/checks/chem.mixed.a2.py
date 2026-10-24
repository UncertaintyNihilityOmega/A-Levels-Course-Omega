# checks/chem.mixed.a2.py: recomputes every number in Mixed practice: A Level.
# Ar from data/elements.json (the 9701 Periodic Table); constants from the Data booklet (FACTS.md).
import json, os
from math import isclose, log10, sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
AR = {e['sym']: e['ar'] for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

R, F = 8.31, 9.65e4
H, C, O, Ca, Br, Fe, S, Cu = (AR[s] for s in ('H', 'C', 'O', 'Ca', 'Br', 'Fe', 'S', 'Cu'))

# ---- Set 1
# Q1 CaF2 Born-Haber
fat = 158 / 2
eq("S1Q1 2 Hat F", 2 * fat, 158)
latt = -1220 - (178 + 590 + 1150 + 2 * fat + 2 * (-328))
eq("S1Q1 sum", 178 + 590 + 1150 + 158 - 656, 1420)
eq("S1Q1 latt", latt, -2640)
# Q2 phenol bromination
mphenol = 6 * C + 6 * H + O
eq("S1Q2 Mr phenol", mphenol, 94.0)
mtbp = 6 * C + 3 * H + 3 * Br + O
eq("S1Q2 Mr TBP", round(mtbp, 1), 330.7)
n = 1.88 / mphenol
eq("S1Q2 n", round(n, 4), 0.0200)
theo = n * mtbp
eq("S1Q2 theo", round(theo, 3), 6.614)
eq("S1Q2 yield", sf(5.00 / theo * 100), 75.6)
# Q3 MgCl2 solution
eq("S1Q3 dHsol", 2526 - 1920 + 2 * (-364), -122)
# Q5 CaCO3 dG
eq("S1Q5 dG", sf(178 - 298 * 0.161), 130.0)
eq("S1Q5 T", sf(178000 / 161), 1110.0)
# Q6 purity
mcc = Ca + C + 3 * O
eq("S1Q6 Mr", round(mcc, 1), 100.1)
nco2 = 0.232 / 24.0
eq("S1Q6 n", round(nco2, 6), 9.667e-3, 1e-6)
mass = nco2 * mcc
eq("S1Q6 mass", round(mass, 4), 0.9677, 1e-4)
eq("S1Q6 pct", sf(mass / 1.25 * 100), 77.4)
# Q7 Haber
dS = 2 * 193 - (192 + 3 * 131)
eq("S1Q7 dS", dS, -199)
dG = -92 - 298 * (dS / 1000)
eq("S1Q7 dG", sf(dG), -32.7)
eq("S1Q7 T", sf(-92 / (dS / 1000)), 462)
# Q8 bond energies
broken = 4 * 410 + 2 * 496
formed = 2 * 805 + 4 * 460
eq("S1Q8 broken", broken, 2632)
eq("S1Q8 formed", formed, 3450)
eq("S1Q8 dH", broken - formed, -818)

# ---- Set 2
Q = 0.750 * 40.0 * 60
eq("S2Q1 Q", Q, 1800)
ncu = Q / (2 * F)
eq("S2Q1 n", round(ncu, 6), 9.326e-3, 1e-6)
eq("S2Q1 mass", sf(ncu * Cu), 0.592)
# Q2 cell
ecell = 0.77 - 0.15
eq("S2Q2 E", round(ecell, 2), 0.62)
eq("S2Q2 dG", sf(-2 * F * ecell / 1000), -120)
eq("S2Q2 dG J", sf(-2 * F * ecell), -1.20e5, 1)
# Q3 Nernst
e1 = 0.34 + 0.059 / 2 * log10(0.0100)
eq("S2Q3 E", round(e1, 3), 0.281)
eq("S2Q3 Ecell", sf(e1 + 0.76), 1.04)
# Q4 FeSO4 tablet
nmn = 0.0200 * 14.20 / 1000
eq("S2Q4 nMn", nmn, 2.84e-4, 1e-12)
nfe25 = 5 * nmn
eq("S2Q4 nFe25", nfe25, 1.42e-3, 1e-12)
nfe = nfe25 * 10
eq("S2Q4 nFe", nfe, 1.42e-2, 1e-12)
mrfeso4 = Fe + S + 4 * O
eq("S2Q4 Mr", round(mrfeso4, 1), 151.9)
m = nfe * mrfeso4
eq("S2Q4 mass", round(m, 3), 2.157, 1e-3)
eq("S2Q4 pct", sf(m / 2.50 * 100), 86.3)
# Q5 brass
ns = 0.100 * 24.60 / 1000
eq("S2Q5 nS", ns, 2.46e-3, 1e-12)
mcu = ns * Cu
eq("S2Q5 mass", round(mcu, 4), 0.1562, 1e-4)
eq("S2Q5 pct", sf(mcu / 0.500 * 100), 31.2)
# Q7 disproportionation
e = 0.52 - 0.15
eq("S2Q7 E", round(e, 2), 0.37)
eq("S2Q7 dG", sf(-1 * F * e / 1000), -35.7)
eq("S2Q7 dG J", sf(-1 * F * e), -3.57e4, 10)
# Q8 Kp
tot = 1.50 + 1.00
x1, x2 = 1.50 / tot, 1.00 / tot
eq("S2Q8 x1", x1, 0.600)
eq("S2Q8 x2", x2, 0.400)
p1, p2 = x1 * 2.00e5, x2 * 2.00e5
eq("S2Q8 p1", p1, 1.20e5, 1e-3)
eq("S2Q8 p2", p2, 0.800e5, 1e-3)
eq("S2Q8 Kp", sf(p2 ** 2 / p1), 5.33e4, 1)

# ---- Set 3
# Q2 gas Mr
nn = 1.01e5 * 6.25e-5 / (R * 373)
eq("S3Q2 n", round(nn, 6), 2.037e-3, 1e-6)
eq("S3Q2 Mr", sf(0.150 / nn), 73.7)
# Q3 buffer
Ka = 1.74e-5
h = Ka * 0.250 / 0.100
eq("S3Q3 H", sf(h), 4.35e-5, 1e-9)
eq("S3Q3 pH", round(-log10(h), 2), 4.36)
na, ns_ = 0.250 * 0.5, 0.100 * 0.5
eq("S3Q3 na", na, 0.125)
eq("S3Q3 ns", ns_, 0.0500)
na2, ns2 = na + 0.0100, ns_ - 0.0100
eq("S3Q3 na2", na2, 0.135)
eq("S3Q3 ns2", ns2, 0.0400)
h2 = Ka * na2 / ns2
eq("S3Q3 H2", sf(h2), 5.87e-5, 1e-8)
eq("S3Q3 pH2", round(-log10(h2), 2), 4.23)
# Q4 Ksp Mg(OH)2
ksp = 4 * (1.20e-4) ** 3
eq("S3Q4 ksp", sf(ksp), 6.91e-12, 1e-14)
oh = sqrt(ksp / 0.0100)
eq("S3Q4 OH", sf(oh), 2.63e-5, 1e-7)
eq("S3Q4 s", sf(oh / 2), 1.31e-5, 1e-7)
# Q5 partition
m1 = 6.0 / 14
eq("S3Q5 a", sf(m1), 0.429, 1e-9)
assert isclose((m1 / 50.0) / ((0.500 - m1) / 100), 12.0)
x = 6.0 / 16
eq("S3Q5 x", x, 0.375)
assert isclose((x / 25.0) / ((0.500 - x) / 100), 12.0)
y = 12.0 * (0.500 - x) / (4 + 12.0)  # y/25 / ((0.125-y)/100) = 12 -> 4y = 12(0.125-y)
eq("S3Q5 rem", 0.500 - x, 0.125)
eq("S3Q5 y", y, 0.09375, 1e-12)
eq("S3Q5 total", sf(x + y), 0.469, 1e-9)
assert x + y > m1
# Q7 weak acid
nn = 0.100 * 20.0 / 1000
eq("S3Q7 n", nn, 2.00e-3, 1e-12)
ha = nn / 0.0250
eq("S3Q7 HA", ha, 0.0800)
hh = 10 ** -2.95
eq("S3Q7 H", sf(hh), 1.12e-3, 1e-6)
ka = hh ** 2 / ha
eq("S3Q7 Ka", sf(ka), 1.57e-5, 1e-8)
eq("S3Q7 pKa", round(-log10(ka), 2), 4.80)
# Q8 AgX
agcl = sqrt(2.0e-10)
agi = sqrt(8.0e-17)
eq("S3Q8 AgCl", sf(agcl, 2), 1.4e-5, 1e-8)
eq("S3Q8 AgI", sf(agi, 2), 8.9e-9, 1e-11)
assert agcl / agi > 1000

# ---- Set 4
# Q2 initial rates
r1, r2, r3 = 3.2e-6, 6.4e-6, 2.88e-5
eq("S4Q2 A order", r2 / r1, 2)
eq("S4Q2 B", r3 / r1, 9)
k = r1 / (0.020 * 0.010 ** 2)
eq("S4Q2 k", k, 1.6, 1e-9)
eq("S4Q2 rate3 check", k * 0.040 * 0.010 ** 2, r2, 1e-12)
eq("S4Q2 rate3", k * 0.020 * 0.030 ** 2, r3, 1e-12)
eq("S4Q2 d", k * 0.050 * 0.020 ** 2, 3.2e-5, 1e-12)
# Q3 half-life
kk = 0.693 / 8.50
eq("S4Q3 k", sf(kk), 0.0815, 1e-9)
eq("S4Q3 n half-lives", 25.5 / 8.50, 3)
eq("S4Q3 conc", 0.640 / 2 ** 3, 0.0800)
eq("S4Q3 rate", sf(kk * 0.640), 5.22e-2, 1e-9)
# Q5 ester
k5 = 3.0e-5 / (0.20 * 0.10)
eq("S4Q5 k", k5, 1.5e-3, 1e-12)
eq("S4Q5 rate", k5 * 0.10 * 0.30, 4.5e-5, 1e-12)
# Q6 catalysis
eq("S4Q6 E1", round(2.01 - 0.54, 2), 1.47)
eq("S4Q6 E2", round(0.77 - 0.54, 2), 0.23)
eq("S4Q6 E3", round(2.01 - 0.77, 2), 1.24)

# ---- Set 5
# Q6 Kstab
ks = 1.1e13
cu = 0.0200 / (ks * 0.500 ** 4)
eq("S5Q6 Cu", sf(cu), 2.91e-14, 1e-16)
# Q7 ethanedioic acid
nmn = 0.0200 * 25.00 / 1000
eq("S5Q7 nMn", nmn, 5.00e-4, 1e-12)
nox = nmn * 5 / 2
eq("S5Q7 nox25", nox, 1.25e-3, 1e-12)
eq("S5Q7 nox", nox * 10, 1.25e-2, 1e-12)
mr = 1.575 / (nox * 10)
eq("S5Q7 Mr", round(mr, 1), 126.0)
mracid = 2 * H + 2 * C + 4 * O
eq("S5Q7 Mr acid", round(mracid, 1), 90.0)
eq("S5Q7 x", round((mr - mracid) / (2 * H + O)), 2)
# balance 2MnO4- + 5H2C2O4 + 6H+ -> 2Mn2+ + 10CO2 + 8H2O
assert (2 * -1 + 6) == (2 * 2)            # charge
assert (2 * 4 + 5 * 4) == (10 * 2 + 8)    # O
assert (5 * 2 + 6) == (8 * 2)             # H
assert 5 * 2 == 10                         # C

# ---- Set 6
# Q8 chromatography
eq("S6Q8 Rf", round(3.9 / 7.5, 2), 0.52)
tot = 14.0 + 22.5 + 33.5
eq("S6Q8 total", tot, 70.0)
eq("S6Q8 pct", sf(22.5 / tot * 100), 32.1)
# Q6 ester C4H8O2: H count 3+2+3 = 8, relative area 3:2:3
assert 3 + 2 + 3 == 8

# ---- Quiz
eq("Q3 T", 40.0 * 1000 / 100, 400)
eq("Q4 E", round(0.77 + 0.059 * log10(0.100 / 0.0100), 2), 0.83)
eq("Q4 wrong inverted", round(0.77 + 0.059 * log10(0.0100 / 0.100), 2), 0.71)
eq("Q4 wrong double", round(0.77 + 2 * 0.059, 2), 0.89)
eq("Q6 s", sf((4.0e-12 / 4) ** (1 / 3)), 1.0e-4, 1e-10)
eq("Q6 sqrt wrong", sf(sqrt(4.0e-12)), 2.0e-6, 1e-9)
eq("Q6 cuberoot wrong", sf((4.0e-12) ** (1 / 3), 2), 1.6e-4, 1e-8)
eq("Q5 pH", 4.20, 4.20)
eq("Q5 wrong", 14 - 4.20, 9.80)
eq("Q3 wrong K", 400 - 273, 127)
eq("Q3 wrong K2", 400 + 273, 673)

print("ok")
