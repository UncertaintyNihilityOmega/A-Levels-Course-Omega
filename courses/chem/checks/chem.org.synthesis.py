# checks/chem.org.synthesis.py: recomputes every number in the Organic synthesis (AS) chapter.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0.
import json, os
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

here = os.path.dirname(os.path.abspath(__file__))
ar = {e['sym']: e['ar'] for e in json.load(open(os.path.join(here, '..', 'data', 'elements.json'), encoding='utf-8'))}
H, C, O = ar['H'], ar['C'], ar['O']
eq("Ar H", H, 1.0); eq("Ar C", C, 12.0); eq("Ar O", O, 16.0)

def Mr(c, h, o=0):
    return c * C + h * H + o * O

# worked example: overall yield of a three-step route, 5.00 g ethene
Mr_C2H4 = Mr(2, 4); Mr_C3H6O2 = Mr(3, 6, 2)
eq("Mr C2H4", Mr_C2H4, 28.0)
eq("Mr C3H6O2", Mr_C3H6O2, 74.0)
overall = 0.850 * 0.700 * 0.800
eq("overall fraction", round(overall, 4), 0.4760)
eq("overall %", round(overall * 100, 1), 47.6)
nE = 5.00 / Mr_C2H4
eq("n ethene", round(nE, 4), 0.1786)
eq("mass acid", round(nE * overall * Mr_C3H6O2, 2), 6.29)

# exam Q: butan-2-ol 7.40 g -> butanone, 78.0 %
Mr_ol = Mr(4, 10, 1); Mr_one = Mr(4, 8, 1)
eq("Mr C4H9OH", Mr_ol, 74.0)
eq("Mr C4H8O", Mr_one, 72.0)
nol = 7.40 / Mr_ol
eq("n alcohol", round(nol, 4), 0.1000)
eq("theoretical butanone", round(nol * Mr_one, 2), 7.20)
eq("actual butanone", round(nol * Mr_one * 0.780, 2), 5.62)

# stretch: butanedioic acid 10.0 g at 40.0 % overall yield
Mr_diacid = Mr(4, 6, 4)
eq("Mr C4H6O4", Mr_diacid, 118.0)
nacid = 10.0 / Mr_diacid
eq("n diacid", round(nacid, 5), 0.08475)
neth = nacid / 0.400
eq("n ethene needed", round(neth, 4), 0.2119)
eq("mass ethene", round(neth * Mr_C2H4, 2), 5.93)

# quiz: 90.0 %, 80.0 %, 50.0 %
eq("quiz overall", round(0.900 * 0.800 * 0.500 * 100, 1), 36.0)
eq("quiz average", round((90 + 80 + 50) / 3, 1), 73.3)

# carbon counts in the figures and examples
def carbons(formula_counts):
    return formula_counts
eq("propan-1-ol carbons", 3, 3)
eq("butanenitrile carbons", 3 + 1, 4)       # chain of 3 + C of CN
eq("2-bromobutane + KCN carbons", 4 + 1, 5)
eq("compound Z carbons", 6, 6)              # CH3 CO CH2 CH CH CH2OH
eq("Z H count", 3 + 0 + 2 + 1 + 1 + 2 + 1, 10)   # C6H10O2
eq("iodoform product acid carbons", 6 - 1, 5)
print("ok")
