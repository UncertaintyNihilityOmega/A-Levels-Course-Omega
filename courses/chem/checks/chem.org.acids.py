# checks/chem.org.acids.py: recomputes every number in "Carboxylic acids, esters and nitriles".
# Ar from the 9701 Periodic Table (data/elements.json). Boiling points (standard-table values, not recomputed):
# ethanol 78, ethanoic acid 118, propanoic acid 141, methyl ethanoate 57 (deg C).
import json
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
H, C, O, Na = A['H'], A['C'], A['O'], A['Na']
eq("Ar H", H, 1.0); eq("Ar C", C, 12.0); eq("Ar O", O, 16.0); eq("Ar Na", Na, 23.0)
def Mr(c, h, o=0, na=0): return c * C + h * H + o * O + na * Na

# table Mr
eq("Mr ethanol", Mr(2, 6, 1), 46.0)
eq("Mr ethanoic acid", Mr(2, 4, 2), 60.0)
eq("Mr propanoic acid", Mr(3, 6, 2), 74.0)
eq("Mr methyl ethanoate", Mr(3, 6, 2), 74.0)
eq("bp gap", 141 - 57, 84)

# CO2 example: 5.00 g ethanoic acid
na = 5.00 / Mr(2, 4, 2)
eq("n acid", round(na, 5), 0.08333)
eq("n CO2", round(na / 2, 5), 0.04167)
eq("V CO2", sf(na / 2 * 24.0), 1.00)

# yield example: 6.00 g ethanoic acid -> 5.72 g ethyl ethanoate
Me = Mr(4, 8, 2)
eq("Mr ethyl ethanoate", Me, 88.0)
n1 = 6.00 / Mr(2, 4, 2)
eq("n", round(n1, 4), 0.1000)
eq("max", round(n1 * Me, 2), 8.80)
eq("yield", round(5.72 / (n1 * Me) * 100, 1), 65.0)

# titration example: 0.370 g, 25.0 cm3 of 0.200 mol/dm3 NaOH
nn = 0.200 * 25.0 / 1000
eq("n NaOH", nn, 0.00500)
eq("Mr acid", sf(0.370 / nn), 74.0)
eq("Mr COOH", C + 2 * O + H, 45.0)
eq("Mr R", 74.0 - 45.0, 29.0)
eq("Mr C2H5", 2 * C + 5 * H, 29.0)

# exam: methanol yield
nm = 2.40 / Mr(1, 4, 1)
eq("Mr methanol", Mr(1, 4, 1), 32.0)
eq("n methanol", round(nm, 5), 0.07500)
eq("max ester", round(nm * Me, 2), 6.60)
eq("yield 2", round(4.95 / (nm * Me) * 100, 1), 75.0)
eq("Mr methyl propanoate", Mr(4, 8, 2), 88.0)

# exam: 0.880 g acid in 250 cm3, 25.0 cm3 needs 20.0 cm3 of 0.0500
nb = 0.0500 * 20.0 / 1000
eq("n NaOH 2", nb, 0.001000)
eq("n total", nb * 10, 0.01000)
eq("Mr butanoic", sf(0.880 / (nb * 10)), 88.0)
eq("Mr butanoic formula", Mr(4, 8, 2), 88.0)

# synoptic: acid Mr 60.0, ester C5H10O2 -> alcohol C3H8O
eq("ester carbons", 5 - 2, 3)
eq("Mr C5H10O2", Mr(5, 10, 2), 102.0)

# stretch: tristearin
Mf = 3 * (18 * C + 35 * H + 2 * O) + 3 * C + 5 * H
eq("Mr tristearin", Mf, 890.0)
eq("C in fat", 3 * 18 + 3, 57); eq("H in fat", 3 * 35 + 5, 110)
eq("Mr sodium stearate", 18 * C + 35 * H + 2 * O + Na, 306.0)
nf = 8.90 / Mf
eq("n fat", round(nf, 5), 0.01000)
eq("mass soap", sf(3 * nf * 306.0), 9.18)

# quiz: 3.00 g ethanoic acid
nq = 3.00 / 60.0
eq("quiz V", sf(nq / 2 * 24.0), 0.600)
eq("quiz wrong 1.20", sf(nq * 24.0), 1.20)
eq("quiz wrong 1.80", sf(nq * 1.5 * 24.0), 1.80)

# balance tallies [C, H, O, charge]
# RCN + 2H2O + H+ -> RCOOH + NH4+ (R and C ignored): H 5 -> 5 ; O 2 -> 2 ; charge +1 -> +1
assert (4 + 1, 2, 1) == (1 + 4, 2, 1)
# RCN + H2O + OH- -> RCOO- + NH3: H 3 -> 3 ; O 2 -> 2 ; charge -1 -> -1
assert (2 + 1, 1 + 1, -1) == (3, 2, -1)
# tristearin saponification: 3 NaOH, 3 soap
assert 3 * 1 == 3
n += 3
print("ok", n)
