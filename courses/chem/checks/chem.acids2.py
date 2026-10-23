# checks/chem.acids2.py: recomputes every number in "pH, buffers, solubility product and partition".
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0, Na 23.0, S 32.1, Cl 35.5, Ag 107.9, Ba 137.3.
# Ka, Ksp and Kpc values are data stated in the chapter (not derived). Kw = 1.00e-14 at 298 K.
from math import isclose, log10, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def pH(h):
    return -log10(h)

def r2(x):
    return round(x + 1e-12, 2)

Kw = 1.00e-14
Ka_eth = 1.74e-5
H, C, O, Na, S, Cl, Ag, Ba = 1.0, 12.0, 16.0, 23.0, 32.1, 35.5, 107.9, 137.3

# ---- warm-up
eq("warm moles", 0.100 * 25.0 / 1000, 0.00250)

# ---- pKa table
for name, ka, pka in [("chloroethanoic", 1.38e-3, 2.86), ("methanoic", 1.78e-4, 3.75), ("ethanoic", 1.74e-5, 4.76), ("propanoic", 1.35e-5, 4.87)]:
    eq("pKa " + name, r2(-log10(ka)), pka)

# ---- strong acids and alkalis
eq("HCl 0.0500", r2(pH(0.0500)), 1.30)
n = 0.100 * 10.0 / 1000
eq("dilution n", n, 1.00e-3)
eq("dilution pH", r2(pH(n / 1.00)), 3.00)
eq("H2SO4", r2(pH(2 * 0.0500)), 1.00)
h = Kw / 0.0200
eq("NaOH 0.0200 H+", sf(h), 5.00e-13)
eq("NaOH 0.0200 pH", r2(pH(h)), 12.30)
eq("NaOH shortcut", r2(14 + log10(0.0200)), 12.30)
eq("NaOH wrong 1.70", r2(-log10(0.0200)), 1.70)
eq("Ba(OH)2 OH", 2 * 0.0250, 0.0500)

# ---- mixing HCl and NaOH
nH = 0.100 * 25.0 / 1000
nOH = 0.100 * 15.0 / 1000
eq("mix nH", nH, 2.50e-3)
eq("mix nOH", nOH, 1.50e-3)
excess = nH - nOH
eq("mix excess", excess, 1.00e-3)
c = excess / (40.0 / 1000)
eq("mix conc", c, 0.0250)
eq("mix pH", r2(pH(c)), 1.60)

# ---- weak acids
h = sqrt(Ka_eth * 0.100)
eq("ethanoic 0.100 H+", sf(h, 4), 1.319e-3)
eq("ethanoic 0.100 pH", r2(pH(h)), 2.88)
eq("ethanoic % dissociated", round(h / 0.100 * 100, 1), 1.3)
eq("HCl same conc pH", r2(pH(0.100)), 1.00)
eq("ratio H+ weak/strong", round(h / 0.100 * 100, 1), 1.3)

h = 10 ** -2.60
eq("HX H+", sf(h, 4), 2.512e-3)
Ka = h ** 2 / 0.250
eq("HX Ka", sf(Ka), 2.52e-5)
eq("HX Ka 4sf", sf(Ka, 4), 2.524e-5)
eq("HX pKa", r2(-log10(Ka)), 4.60)

h2 = sqrt(Ka_eth * 0.0100)
eq("ethanoic 0.0100 H+", sf(h2, 4), 4.171e-4)
eq("ethanoic 0.0100 pH", r2(pH(h2)), 3.38)
eq("rise 0.50", round(pH(h2) - pH(h), 1) if False else round(pH(h2) - pH(sqrt(Ka_eth * 0.100)), 2), 0.50)
eq("HCl rise", r2(pH(0.0100)) - r2(pH(0.100)), 1.00)
eq("spot error wrong pH", r2(pH(0.0100)), 2.00)

# ---- buffers
h = Ka_eth * 0.100 / 0.0500
eq("buf1 H+", sf(h), 3.48e-5)
eq("buf1 pH", r2(pH(h)), 4.46)
eq("buf1 conc A", 0.100 * 50.0 / 100.0, 0.0500) if False else None
eq("buf1 amounts HA", 0.200 * 50.0 / 1000, 0.0100)
eq("buf1 amounts A", 0.100 * 50.0 / 1000, 0.00500)

nHA = 0.500 * 100 / 1000
nNaOH = 0.500 * 40.0 / 1000
eq("buf2 nHA", nHA, 0.0500)
eq("buf2 nNaOH", nNaOH, 0.0200)
eq("buf2 left", nHA - nNaOH, 0.0300)
h = Ka_eth * (nHA - nNaOH) / nNaOH
eq("buf2 H+", sf(h), 2.61e-5)
eq("buf2 pH", r2(pH(h)), 4.58)

h = 1.00e-5
ratio = Ka_eth / h
eq("buf3 ratio", sf(ratio), 1.74)
nHA = 0.200 * 250 / 1000
eq("buf3 nHA", nHA, 0.0500)
nA = ratio * nHA
eq("buf3 nA", sf(nA), 0.0870)
Mr_NaOAc = 2 * C + 3 * H + 2 * O + Na
eq("Mr sodium ethanoate", Mr_NaOAc, 82.0)
eq("buf3 mass", sf(nA * Mr_NaOAc), 7.13)

# buffer + acid / alkali
eq("buf4 pH a", r2(-log10(Ka_eth)), 4.76)
h = Ka_eth * 0.510 / 0.490
eq("buf4 H+", sf(h, 4), 1.811e-5)
eq("buf4 pH", r2(pH(h)), 4.74)
eq("buf4 change", round(-log10(Ka_eth) - pH(h), 2), 0.02)
eq("water + HCl", r2(pH(0.0100)), 2.00)
h = Ka_eth * 0.490 / 0.510
eq("buf4 NaOH H+", sf(h, 4), 1.672e-5)
eq("buf4 NaOH pH", r2(pH(h)), 4.78)
eq("buf4 NaOH change", round(pH(h) - (-log10(Ka_eth)), 2), 0.02)
eq("blood ratio", round(10 ** (7.4 - 6.1)), 20)

# ---- titration table: 25.0 cm3 0.100 mol dm-3 ethanoic acid with 0.100 NaOH
nA0 = 0.100 * 25.0 / 1000
eq("tit nHA", nA0, 2.50e-3)
eq("tit v0 pH", r2(pH(sqrt(Ka_eth * 0.100))), 2.88)
nb = 0.100 * 10.0 / 1000
eq("tit 10 ratio HA", nA0 - nb, 0.00150)
eq("tit 10 pH", r2(pH(Ka_eth * (nA0 - nb) / nb)), 4.58)
eq("tit 12.5 pH", r2(-log10(Ka_eth)), 4.76)
nb = 0.100 * 20.0 / 1000
eq("tit 20 ratio HA", nA0 - nb, 0.000500)
eq("tit 20 pH", r2(pH(Ka_eth * (nA0 - nb) / nb)), 5.36)
nb = 0.100 * 30.0 / 1000
exc = nb - nA0
eq("tit 30 excess", exc, 5.00e-4)
oh = exc / (55.0 / 1000)
eq("tit 30 pH", r2(pH(Kw / oh)), 11.96)
# equivalence pH "about 8.7": ethanoate 0.0500 mol dm-3, Kb route (check only the approximate figure)
cA = nA0 / (50.0 / 1000)
oh = sqrt(Kw / Ka_eth * cA)
assert 8.6 < 14 + log10(oh) < 8.8, 14 + log10(oh)

# titration with unknown acid
nOH = 0.100 * 20.0 / 1000
eq("unk n", nOH, 2.00e-3)
eq("unk c", nOH / (25.0 / 1000), 0.0800)
eq("unk Ka", sf(10 ** -4.20), 6.31e-5)

# ---- Ksp
s = 1.34e-5
eq("AgCl Ksp", sf(s ** 2), 1.80e-10)
Mr_AgCl = Ag + Cl
eq("Mr AgCl", Mr_AgCl, 143.4)
eq("AgCl mass", sf(s * Mr_AgCl), 1.92e-3)

eq("Ca(OH)2 OH", 2 * 1.10e-2, 2.20e-2)
eq("Ca(OH)2 Ksp", sf(1.10e-2 * (2.20e-2) ** 2), 5.32e-6)

s = sqrt(1.1e-10)
eq("BaSO4 s", sf(s), 1.05e-5)
Mr_BaSO4 = Ba + S + 4 * O
eq("Mr BaSO4", Mr_BaSO4, 233.4)
eq("BaSO4 mass", sf(s * Mr_BaSO4), 2.45e-3)

s = (5.6e-12 / 4) ** (1 / 3)
eq("Mg(OH)2 s", sf(s), 1.12e-4)
oh = 2 * s
eq("Mg(OH)2 OH", sf(oh), 2.24e-4) if False else eq("Mg(OH)2 OH 4sf", sf(oh, 4), 2.237e-4)
h = Kw / oh
eq("Mg(OH)2 H+", sf(h), 4.47e-11)
eq("Mg(OH)2 pH", r2(pH(h)), 10.35)

# precipitation
eq("ppt Q1", sf((5.0e-5) ** 2), 2.5e-9)
assert (5.0e-5) ** 2 > 1.8e-10
eq("ppt Q2", sf((5.0e-6) ** 2), 2.5e-11)
assert (5.0e-6) ** 2 < 1.8e-10

# common ion
Ksp = 1.80e-10
eq("common ion Ag", sf(Ksp / 0.100), 1.80e-9)
eq("pure water s", sf(sqrt(Ksp)), 1.34e-5)
eq("ratio", round(sqrt(Ksp) / (Ksp / 0.100), -1) if False else round(sqrt(Ksp) / (Ksp / 0.100), -1), 7450)
eq("Mg(OH)2 in NaOH", sf(5.6e-12 / 0.0100 ** 2), 5.6e-8)
assert 1990 < ((5.6e-12 / 4) ** (1 / 3)) / 5.6e-8 < 2010

# ---- partition
eq("Kpc iodine", 0.0850 / 1.00e-3, 85.0, 1e-9)
# one extraction 100 cm3 ether, Kpc 4.00: m/100 / ((1-m)/100) = 4
m = 4.00 / 5.00
eq("ether a", m, 0.800)
frac = 100 / (100 + 4.00 * 100)
eq("frac a", frac, 0.200)
m1 = 2.00 / 3.00
eq("ether b m1", round(m1, 3), 0.667)
eq("ether b left", round(1 - m1, 3), 0.333)
m2 = (1 - m1) * 2.00 / 3.00
eq("ether b m2", round(m2, 3), 0.222)
eq("ether b total", round(m1 + m2, 3), 0.889)
frac2 = 100 / (100 + 4.00 * 50.0)
eq("frac b", round(frac2, 3), 0.333)
eq("frac b2", round(frac2 ** 2, 3), 0.111)

# ---- try questions
eq("try2a", r2(pH(0.0250)), 1.60)
eq("try2b H+", sf(Kw / 0.00400), 2.50e-12)
eq("try2b pH", r2(pH(Kw / 0.00400)), 11.60)
eq("try3", sf(10 ** -3.40), 3.98e-4)
h = sqrt(1.35e-5 * 0.250)
eq("try4 H+", sf(h, 4), 1.837e-3)
eq("try4 pH", r2(pH(h)), 2.74)
eq("try5 Ka", sf(10 ** -3.75), 1.78e-4)
h = 10 ** -3.10
eq("try6 H+", sf(h, 4), 7.943e-4)
eq("try6 Ka", sf(h ** 2 / 0.0800), 7.89e-6)
h = 1.35e-5 * 0.200 / 0.150
eq("try7 H+", sf(h), 1.80e-5)
eq("try7 pH", r2(pH(h)), 4.74)
s = 2.14e-4
eq("try9 Ksp", sf(4 * s ** 3), 3.92e-11)
a = 2.0e-4 * 20.0 / 50.0
cl = 1.0e-3 * 30.0 / 50.0
eq("try10 Ag", a, 8.0e-5)
eq("try10 Cl", cl, 6.0e-4)
eq("try10 Q", sf(a * cl), 4.8e-8)
assert a * cl > 1.8e-10
eq("try11", 7.5 * 0.020, 0.15)

# ---- exam practice
eq("ep1 OH", 2 * 0.0250, 0.0500)
eq("ep1 H+", sf(Kw / 0.0500), 2.00e-13)
eq("ep1 pH", r2(pH(Kw / 0.0500)), 12.70)
h = sqrt(1.78e-4 * 0.0500)
eq("ep2 H+", sf(h, 4), 2.983e-3)
eq("ep2 pH", r2(pH(h)), 2.53)
h = 10 ** -2.85
eq("ep3 H+", sf(h, 4), 1.413e-3)
Ka = h ** 2 / 0.150
eq("ep3 Ka", sf(Ka), 1.33e-5)
eq("ep3 pKa", r2(-log10(Ka)), 4.88)
h = 10 ** -4.30
eq("ep4 H+", sf(h, 4), 5.012e-5)
ratio = Ka_eth / h
eq("ep4 ratio", sf(ratio, 4), 0.3472)
nHA = 0.400 * 250 / 1000
eq("ep4 nHA", nHA, 0.100)
eq("ep4 nA", sf(ratio * nHA, 4), 0.03472)
eq("ep4 mass", sf(ratio * nHA * Mr_NaOAc), 2.85)
s = 1.35e-3
eq("ep6 I", 2 * s, 2.70e-3)
Ksp = s * (2 * s) ** 2
eq("ep6 Ksp", sf(Ksp), 9.84e-9)
i = sqrt(Ksp / 0.0100)
eq("ep6 I common", sf(i), 9.92e-4)
eq("ep6 s common", sf(i / 2), 4.96e-4)
oh = sqrt(5.6e-12 / 0.0200)
eq("ep7 OH2", sf(5.6e-12 / 0.0200), 2.8e-10)
eq("ep7 OH", sf(oh), 1.67e-5)
h = Kw / oh
eq("ep7 H+", sf(h), 5.98e-10)
eq("ep7 pH", r2(pH(h)), 9.22)
# ep8
m = 2 * 0.600 / (2 + 6.00) * 1 if False else None
# 6.00 = (m/50)/((0.600-m)/100) -> 2m = 6(0.600-m) -> m = 3.6/8
m = 6.00 * 0.600 / (2 + 6.00)
eq("ep8 a", m, 0.450)
f = 100 / (100 + 6.00 * 25.0)
eq("ep8 frac", f, 0.400)
eq("ep8 left", sf(0.600 * f ** 2), 0.0960)
eq("ep8 extracted", sf(0.600 - 0.600 * f ** 2), 0.504)

# ---- stretch 1
nHA = 0.200 * 25.0 / 1000
eq("s1 nHA", nHA, 5.00e-3)
eq("s1 veq", nHA / 0.100 * 1000, 50.0)
h = sqrt(Ka_eth * 0.200)
eq("s1 H+", sf(h, 4), 1.865e-3)
eq("s1 pH0", r2(pH(h)), 2.73)
eq("s1 pH25", r2(-log10(Ka_eth)), 4.76)
nb = 0.100 * 40.0 / 1000
eq("s1 nOH40", nb, 4.00e-3)
eq("s1 HA left", nHA - nb, 1.00e-3)
h = Ka_eth * (nHA - nb) / nb
eq("s1 H+40", sf(h), 4.35e-6)
eq("s1 pH40", r2(pH(h)), 5.36)
nb = 0.100 * 60.0 / 1000
eq("s1 nOH60", nb, 6.00e-3)
eq("s1 excess", nb - nHA, 1.00e-3)
oh = (nb - nHA) / (85.0 / 1000)
eq("s1 OH", sf(oh, 4), 0.01176)
eq("s1 H+60", sf(Kw / oh), 8.50e-13)
eq("s1 pH60", r2(pH(Kw / oh)), 12.07)

# ---- stretch 2
agi = 8.5e-17 / 0.0100
agcl = 1.8e-10 / 0.0100
eq("s2 AgI", sf(agi), 8.5e-15)
eq("s2 AgCl", sf(agcl), 1.8e-8)
i = 8.5e-17 / agcl
eq("s2 I", sf(i, 2), 4.7e-9)
eq("s2 fraction", sf(i / 0.0100, 2), 4.7e-7)
eq("s2 percent", sf(i / 0.0100 * 100, 2), 4.7e-5)

# ---- quiz
eq("q2", r2(pH(Kw / 0.0100)), 12.00)
eq("q3", r2(pH(sqrt(Ka_eth * 0.0100))), 3.38)
eq("q8 Ksp", sf(1.0e-4 * (2.0e-4) ** 2), 4.0e-12)

print("ok")
