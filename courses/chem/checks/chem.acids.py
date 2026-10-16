# checks/chem.acids.py: recomputes every number in the Acids and bases chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.); pH values from data/titration_model.py
# (the same charge-balance model the chem-titration widget uses).
import json, sys
from math import isclose, sqrt, log10
sys.path.insert(0, 'data')
from titration_model import ph_at, veq

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}

# ---- warm-up
eq("HCl n", 0.100 * 25.0 / 1000, 0.00250)

# ---- pH facts: water, 0.100 mol dm-3 solutions, degree of dissociation of ethanoic acid
Kw = 1.00e-14
eq("water [H+]", sqrt(Kw), 1.00e-7, 1e-12)
eq("0.100 HCl pH", ph_at(0.0, True, True), 1.00, 0.005)
eq("0.100 NaOH pH", 14 + log10(0.100), 13.0)
eq("0.100 CH3COOH pH (about 2.9)", ph_at(0.0, False, True), 2.9, 0.05)
Ka = 10 ** (-4.76)
c = 0.100
x = (-Ka + sqrt(Ka ** 2 + 4 * Ka * c)) / 2
eq("fraction dissociated about 1 in 100", x / c, 0.013, 0.001)
eq("NH3 start pH about 11", 14 - (-log10(sqrt(10 ** -4.75 * 0.100))), 11.1, 0.1)

# ---- worked example: Mg with equal amounts of acid
n_acid = 0.100 * 25.0 / 1000
eq("acid n", n_acid, 0.00250)
eq("H2 volume cm3", sf(0.5 * n_acid * 24.0 * 1000, 3), 30.0)

# ---- worked example: Mg(OH)2 antacid
Mr = A['Mg'] + 2 * (A['O'] + A['H'])
eq("Mg(OH)2 Mr", Mr, 58.3)
n = 0.500 / Mr
eq("Mg(OH)2 n", sf(n, 4), 0.008576, 1e-9)
nH = 2 * n
eq("HCl n", sf(nH, 4), 0.01715, 1e-9)
eq("HCl V cm3", sf(nH / 0.100 * 1000, 3), 172)
eq("HCl V dm3", sf(nH / 0.100, 4), 0.1715, 1e-9)

# ---- titration curves, 25.0 cm3 of 0.100 mol dm-3 acid and 0.100 mol dm-3 base
ve = veq()
eq("equivalence volume", ve, 25.0)
d = 0.02 * ve  # 0.5 cm3 either side
cases = {
    'ss': (True, True),
    'ws': (False, True),
    'sw': (True, False),
    'ww': (False, False),
}
eq("ss start", ph_at(0, True, True), 1.0, 0.005)
eq("ws start about 3", ph_at(0, False, True), 2.9, 0.05)
eq("sw start about 1", ph_at(0, True, False), 1.0, 0.005)
eq("ss eq", ph_at(ve, True, True), 7.0, 0.005)
eq("ws eq about 8.7", ph_at(ve, False, True), 8.7, 0.05)
eq("sw eq about 5.3", ph_at(ve, True, False), 5.3, 0.05)
eq("ww eq about 7", ph_at(ve, False, False), 7.0, 0.05)
# steep part = pH at 24.5 and 25.5 cm3
lo, hi = ph_at(ve - d, True, True), ph_at(ve + d, True, True)
eq("ss steep low", lo, 3.0, 0.05); eq("ss steep high", hi, 11.0, 0.05)
lo, hi = ph_at(ve - d, False, True), ph_at(ve + d, False, True)
eq("ws steep low (6.5)", lo, 6.5, 0.06); eq("ws steep high", hi, 11.0, 0.05)
lo, hi = ph_at(ve - d, True, False), ph_at(ve + d, True, False)
eq("sw steep low", lo, 3.0, 0.05); eq("sw steep high (7.5)", hi, 7.5, 0.06)
lo, hi = ph_at(ve - d, False, False), ph_at(ve + d, False, False)
eq("ww low (6.4)", lo, 6.4, 0.05); eq("ww high (7.6)", hi, 7.6, 0.05)
assert hi - lo < 2.0, "weak/weak should have no steep part"
# ends of the curves
eq("ss end ~12.5", ph_at(2 * ve, True, True), 12.5, 0.05)
eq("sw end below ss end", ph_at(2 * ve, True, False), 9.25, 0.01)
# a single drop (0.05 cm3) either side of the equivalence point, strong/strong: pH 4 and 10
eq("drop low", ph_at(ve - 0.05, True, True), 4.0, 0.01)
eq("drop high", ph_at(ve + 0.05, True, True), 10.0, 0.01)
# indicator ranges against steep parts, as drawn in the figure
ind = {'mo': (2.9, 4.6), 'bpb': (3.0, 4.5), 'tb': (8.0, 9.6), 'tp': (9.3, 10.5)}
steep = {'ss': (3.0, 11.0), 'ws': (6.5, 11.0), 'sw': (3.0, 7.5)}
def inside(i, s): return steep[s][0] - 0.11 <= ind[i][0] and ind[i][1] <= steep[s][1] + 0.01
assert all(inside(i, 'ss') for i in ind)
assert [i for i in ind if inside(i, 'ws')] == ['tb', 'tp']
assert [i for i in ind if inside(i, 'sw')] == ['mo', 'bpb']
# the stated pH at the figure axes
assert abs(7 - ph_at(ve, True, True)) < 0.01

# ---- worked example: vinegar
n_naoh = 0.100 * 21.30 / 1000
eq("vinegar n NaOH", sf(n_naoh, 4), 0.002130, 1e-9)
c_dil = n_naoh / (25.0 / 1000)
eq("vinegar c diluted", sf(c_dil, 3), 0.0852)
c_v = c_dil * 10
eq("vinegar c", sf(c_v, 3), 0.852)
Mr_a = 2 * A['C'] + 4 * A['H'] + 2 * A['O']
eq("CH3COOH Mr", Mr_a, 60.0)
eq("vinegar g/dm3", sf(c_v * Mr_a, 3), 51.1)

# ---- worked example: sulfuric acid with concordant titres
t = [22.45, 22.40, 22.40]
assert max(t) - min(t) <= 0.10
mean = sum(t) / 3
eq("mean titre", sf(mean, 4), 22.42, 1e-9)
n_naoh = 0.200 * mean / 1000
eq("H2SO4 NaOH n", sf(n_naoh, 4), 0.004483, 1e-9)
n_a = n_naoh / 2
eq("H2SO4 n", sf(n_a, 4), 0.002242, 1e-9)
eq("H2SO4 c", sf(n_a / 0.0250, 3), 0.0897)
# same answer using the rounded mean in the chapter
eq("H2SO4 c from 22.42", sf(0.200 * 22.42 / 1000 / 2 / 0.0250, 3), 0.0897)

# ---- try questions
eq("try H2SO4 NaOH volume", 2 * 0.100 * 20.0 / 1000 / 0.100 * 1000, 40.0)
eq("try n H2SO4", 0.100 * 20.0 / 1000, 0.00200)

# ---- exam practice: CaCO3 antacid
Mr = A['Ca'] + A['C'] + 3 * A['O']
eq("CaCO3 Mr", Mr, 100.1)
n = 0.500 / Mr
eq("CaCO3 n", sf(n, 4), 0.004995, 1e-9)
eq("HCl n", sf(2 * n, 4), 0.009990, 1e-9)
eq("HCl V dm3", sf(2 * n / 0.100, 3), 0.0999)
eq("HCl V cm3", sf(2 * n / 0.100 * 1000, 3), 99.9)

# ---- exam practice: NaOH with H2SO4
n = 0.150 * 25.0 / 1000
eq("NaOH n", n, 0.003750)
eq("H2SO4 n", n / 2, 0.001875)
cc = n / 2 / (18.60 / 1000)
eq("H2SO4 c 4 sf", sf(cc, 4), 0.1008)
eq("H2SO4 c 3 sf", sf(cc, 3), 0.101)

# ---- stretch: sulfuric acid equivalence point
n = 0.100 * 25.0 / 1000
eq("H2SO4 n", n, 0.00250)
eq("NaOH needed", 2 * n, 0.00500)
eq("NaOH V cm3", 2 * n / 0.100 * 1000, 50.0)

# ---- stretch: hydrated ethanedioic acid
n_naoh = 0.100 * 20.00 / 1000
eq("NaOH n", n_naoh, 0.002000)
n_acid = n_naoh / 2
eq("acid n 25 cm3", n_acid, 0.001000)
eq("acid n 250 cm3", n_acid * 10, 0.01000)
eq("Mr", sf(1.26 / (n_acid * 10), 4), 126.0)
Mr0 = 2 * A['H'] + 2 * A['C'] + 4 * A['O']
eq("H2C2O4 Mr", Mr0, 90.0)
eq("water Mr", 2 * A['H'] + A['O'], 18.0)
eq("x", (1.26 / (n_acid * 10) - Mr0) / 18.0, 2.0, 1e-9)

print("ok")
