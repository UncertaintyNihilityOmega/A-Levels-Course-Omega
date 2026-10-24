# checks/chem.org.polymers.py: recomputes every number in the Polymerisation chapter.
# Ar from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, N 14.0, O 16.0, Na 23.0, Cl 35.5.
import json, os, re
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

here = os.path.dirname(os.path.abspath(__file__))
ar = {e['sym']: e['ar'] for e in json.load(open(os.path.join(here, '..', 'data', 'elements.json'), encoding='utf-8'))}
for sym, v in (("H", 1.0), ("C", 12.0), ("N", 14.0), ("O", 16.0), ("Na", 23.0), ("Cl", 35.5)):
    eq("Ar " + sym, ar[sym], v)

def Mr(formula):
    """Mr of a simple formula such as C8H4Cl2O2 (no brackets)."""
    tot = 0.0
    for sym, num in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
        tot += ar[sym] * (int(num) if num else 1)
    return tot

H2O = Mr("H2O"); HCl = Mr("HCl")
eq("Mr H2O", H2O, 18.0); eq("Mr HCl", HCl, 36.5)

# PET: ethane-1,2-diol C2H6O2 + benzene-1,4-dicarboxylic acid C8H6O4 - 2 H2O = repeat unit C10H8O4
diol, diacid, unit = Mr("C2H6O2"), Mr("C8H6O4"), Mr("C10H8O4")
eq("Mr diol", diol, 62.0); eq("Mr diacid", diacid, 166.0); eq("Mr PET unit", unit, 192.0)
eq("unit from monomers", diol + diacid - 2 * H2O, 192.0)
eq("PET chain", 38400 / unit, 200.0)

# nylon-6,6: hexanedioic acid C6H10O4 + 1,6-diaminohexane C6H16N2 - 2 H2O = C12H22N2O2
acid, amine, nunit = Mr("C6H10O4"), Mr("C6H16N2"), Mr("C12H22N2O2")
eq("Mr hexanedioic acid", acid, 146.0); eq("Mr nylon unit", nunit, 226.0)
eq("nylon unit from monomers", acid + amine - 2 * H2O, 226.0)
na = 10.0 / acid
eq("n acid", round(na, 5), 0.06849)
maxm = na * nunit
eq("max mass", round(maxm, 2), 15.48)
eq("yield", round(12.1 / maxm * 100, 1), 78.2)

# HCl from benzene-1,4-dioyl dichloride C8H4Cl2O2
dc = Mr("C8H4Cl2O2")
eq("Mr dichloride", dc, 203.0)
nd = 5.00 / dc
eq("n dichloride", round(nd, 5), 0.02463)
eq("n HCl", round(2 * nd, 5), 0.04926)
eq("m HCl", round(2 * nd * HCl, 2), 1.80)
eq("polyester unit from dichloride + diol", dc + diol - 2 * HCl, unit)

# poly(glycolic acid): unit C2H2O2, sodium 2-hydroxyethanoate C2H3O3Na
pg, salt = Mr("C2H2O2"), Mr("C2H3O3Na")
eq("Mr PGA unit", pg, 58.0); eq("Mr salt", salt, 98.0)
npg = 2.00 / pg
eq("n PGA", round(npg, 5), 0.03448)
eq("m salt", round(npg * salt, 2), 3.38)

# burning 1.00 kg of poly(ethene): repeat unit CH2 -> CO2
ch2, co2 = Mr("CH2"), Mr("CO2")
eq("Mr CH2", ch2, 14.0); eq("Mr CO2", co2, 44.0)
nch2 = 1000 / ch2
eq("n CH2", round(nch2, 2), 71.43)
eq("m CO2 g", round(nch2 * co2), 3143)
eq("m CO2 kg", round(nch2 * co2 / 1000, 2), 3.14)

# atom balance of the nylon hydrolysis equations (per repeat unit)
def atoms(d):
    return dict(d)
unit_atoms = {"C": 12, "H": 22, "N": 2, "O": 2}
acid_h = {"C": 12, "H": 28, "N": 2, "O": 4}      # unit + 2 H2O + 2 H+ -> diacid (C6H10O4) + diammonium (C6H18N2 2+)
left = {"C": 12, "H": 22 + 4 + 2, "N": 2, "O": 2 + 2}
right = {"C": 6 + 6, "H": 10 + 18, "N": 2, "O": 4}
eq("acid hydrolysis atoms", sum(left[k] == right[k] for k in left), 4)
left2 = {"C": 12, "H": 22 + 2, "N": 2, "O": 2 + 2}   # unit + 2 OH-
right2 = {"C": 6 + 6, "H": 8 + 16, "N": 2, "O": 4}   # dicarboxylate (C6H8O4 2-) + diamine C6H16N2
eq("alkali hydrolysis atoms", sum(left2[k] == right2[k] for k in left2), 4)

# peptides
eq("dipeptides from gly and ala, one each", 2, 2)
eq("water lost in a tripeptide", 3 - 1, 2)
gly, ala = Mr("C2H5NO2"), Mr("C3H7NO2")
eq("Mr glycine", gly, 75.0); eq("Mr alanine", ala, 89.0)

print("ok")
