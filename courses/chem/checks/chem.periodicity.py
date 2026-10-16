# checks/chem.periodicity.py: recomputes every number in the Periodicity: Period 3 chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.).
# First IE, successive IE and electronegativity are the Data booklet values in FACTS.md.
import json
from math import isclose, log10

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

E = {e['sym']: e for e in json.load(open('data/elements.json', encoding='utf-8'))}
A = {s: e['ar'] for s, e in E.items()}

# ---- Period 3 outer electrons and electron counts
outer = {'Na': 1, 'Mg': 2, 'Al': 3, 'Si': 4, 'P': 5, 'S': 6, 'Cl': 7, 'Ar': 8}
for s, n in outer.items():
    assert E[s]['period'] == 3
    eq(f"{s} outer electrons", n, E[s]['group'] if E[s]['group'] <= 2 else E[s]['group'] - 10)
eq("S8 electrons", 8 * E['S']['z'], 128)
eq("P4 electrons", 4 * E['P']['z'], 60)
eq("Cl2 electrons", 2 * E['Cl']['z'], 34)
eq("Ar electrons", E['Ar']['z'], 18)
assert 128 > 60 > 34 > 18
# ion electron counts: Na+, Mg2+, Al3+ have 10; P3-, S2-, Cl- have 18
eq("Na+ e", E['Na']['z'] - 1, 10); eq("Mg2+ e", E['Mg']['z'] - 2, 10); eq("Al3+ e", E['Al']['z'] - 3, 10)
eq("P3- e", E['P']['z'] + 3, 18); eq("S2- e", E['S']['z'] + 2, 18); eq("Cl- e", E['Cl']['z'] + 1, 18)
assert E['Na']['z'] < E['Mg']['z'] < E['Al']['z'] and E['P']['z'] < E['S']['z'] < E['Cl']['z']
eq("Na protons", E['Na']['z'], 11); eq("Cl protons", E['Cl']['z'], 17); eq("Mg protons", E['Mg']['z'], 12)

# ---- Data booklet values quoted (FACTS.md)
ie1 = {'Na': 494, 'Mg': 736, 'Al': 577, 'Si': 786, 'P': 1060, 'S': 1000, 'Cl': 1260, 'Ar': 1520}
en = {'Na': 0.9, 'Mg': 1.3, 'Al': 1.5, 'Si': 1.9, 'P': 2.2, 'S': 2.6, 'Cl': 3.0, 'O': 3.5}
facts = open('FACTS.md', encoding='utf-8').read()
for s, v in ie1.items():
    assert f"{s} {v}" in facts.split('First IE / kJ mol⁻¹:')[1].split('\n')[0], s
for s in ('Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'O'):
    assert f"{s} {en[s]}" in facts.split('Pauling electronegativity:')[1].split('\n')[0], s
# the dips: Mg > Al and P > S
assert ie1['Mg'] > ie1['Al'] and ie1['P'] > ie1['S']
assert all(en[a] < en[b] for a, b in zip(['Na', 'Mg', 'Al', 'Si', 'P', 'S'], ['Mg', 'Al', 'Si', 'P', 'S', 'Cl']))

# ---- electronegativity differences from oxygen (3.5) and chlorine (3.0)
ox = {'Na2O': 'Na', 'MgO': 'Mg', 'Al2O3': 'Al', 'SiO2': 'Si', 'P4O10': 'P', 'SO2': 'S'}
want_ox = {'Na2O': 2.6, 'MgO': 2.2, 'Al2O3': 2.0, 'SiO2': 1.6, 'P4O10': 1.3, 'SO2': 0.9}
for k, s in ox.items():
    eq(f"{k} EN diff", round(en['O'] - en[s], 1), want_ox[k])
cl = {'NaCl': 'Na', 'MgCl2': 'Mg', 'AlCl3': 'Al', 'SiCl4': 'Si', 'PCl5': 'P'}
want_cl = {'NaCl': 2.1, 'MgCl2': 1.7, 'AlCl3': 1.5, 'SiCl4': 1.1, 'PCl5': 0.8}
for k, s in cl.items():
    eq(f"{k} EN diff", round(en['Cl'] - en[s], 1), want_cl[k])
eq("warm-up NaCl diff", round(3.0 - 0.9, 1), 2.1)
eq("AlCl3 diff", round(3.0 - 1.5, 1), 1.5)

# ---- oxidation numbers: balance each formula with O = -2 and Cl = -1
def ox_num(n_el, n_x, x_charge):
    total = -n_x * x_charge
    assert total % n_el == 0
    return total // n_el
eq("Na2O", ox_num(2, 1, -2), 1); eq("MgO", ox_num(1, 1, -2), 2); eq("Al2O3", ox_num(2, 3, -2), 3)
eq("SiO2", ox_num(1, 2, -2), 4); eq("P4O10", ox_num(4, 10, -2), 5); eq("SO2", ox_num(1, 2, -2), 4); eq("SO3", ox_num(1, 3, -2), 6)
eq("NaCl", ox_num(1, 1, -1), 1); eq("MgCl2", ox_num(1, 2, -1), 2); eq("AlCl3", ox_num(1, 3, -1), 3)
eq("SiCl4", ox_num(1, 4, -1), 4); eq("PCl5", ox_num(1, 5, -1), 5)
eq("eg MgCl2 check", 2 + 2 * -1, 0); eq("eg P4O10 check", 4 * 5 + 10 * -2, 0); eq("eg SO3 check", 6 + 3 * -2, 0)

# ---- sketch heights in data/mk_fig_period3.py: only the order is claimed
rad_atom = [186, 160, 143, 118, 110, 104, 99]
assert rad_atom == sorted(rad_atom, reverse=True)
ion = {'Na+': 102, 'Mg2+': 72, 'Al3+': 54, 'P3-': 212, 'S2-': 184, 'Cl-': 181}
assert ion['Na+'] > ion['Mg2+'] > ion['Al3+'] and ion['P3-'] > ion['S2-'] > ion['Cl-']
assert ion['Al3+'] < ion['Cl-'] and ion['Na+'] < rad_atom[0] and ion['Cl-'] > rad_atom[6]
mp = {'Na': 371, 'Mg': 923, 'Al': 933, 'Si': 1683, 'P4': 317, 'S8': 388, 'Cl2': 172, 'Ar': 84}   # K, ordering only
assert mp['Na'] < mp['Mg'] < mp['Al'] < mp['Si'] and mp['S8'] > mp['P4'] > mp['Cl2'] > mp['Ar']

# ---- worked example: 0.310 g Na2O in 250 cm3
Mr_Na2O = 2 * A['Na'] + A['O']
eq("Na2O Mr", Mr_Na2O, 62.0)
n_Na2O = 0.310 / Mr_Na2O
eq("n Na2O", round(n_Na2O, 6), 0.005)
n_OH = 2 * n_Na2O
eq("n OH", round(n_OH, 5), 0.01)
c_OH = n_OH / 0.250
eq("c OH", c_OH, 0.04)
H = 1.00e-14 / c_OH
eq("[H+] x1e-13", round(H * 1e13, 2), 2.50)
eq("pH Na2O", round(-log10(H), 2), 12.60)
assert 12 < -log10(H) < 14            # in the table range 13 to 14 (approx.)

# ---- Al(OH)3 in NaOH
Mr_AlOH3 = A['Al'] + 3 * (A['O'] + A['H'])
eq("Al(OH)3 Mr", Mr_AlOH3, 78.0)
eq("n Al(OH)3", round(0.780 / Mr_AlOH3, 5), 0.01)
eq("V NaOH cm3", round(0.780 / Mr_AlOH3 / 1.00 * 1000, 1), 10.0)

# ---- SiCl4 in water: 0.0100 mol in 1.00 dm3
eq("n HCl", 4 * 0.0100, 0.04)
eq("pH SiCl4", round(-log10(0.0400), 2), 1.40)
# quiz: 0.0200 mol in 2.00 dm3
eq("quiz n HCl", 4 * 0.0200, 0.08)
eq("quiz [H+]", 4 * 0.0200 / 2.00, 0.04)
eq("quiz pH", round(-log10(0.04), 2), 1.40)
eq("quiz wrong 1.70", round(-log10(0.0200), 2), 1.70)
eq("quiz wrong 2.00", round(-log10(0.0200 / 2.00), 2), 2.00)
eq("quiz wrong 1.00", round(-log10(0.1), 2), 1.00)

# ---- Al + O2
eq("Al2O3 Mr", 2 * A['Al'] + 3 * A['O'], 102.0)
n_Al = 2.70 / A['Al']
eq("n Al", round(n_Al, 4), 0.1)
eq("n Al2O3", round(n_Al / 2, 4), 0.05)
eq("mass Al2O3", round(n_Al / 2 * 102.0, 2), 5.10)
eq("n O2", round(n_Al * 3 / 4, 4), 0.075)
eq("V O2", round(n_Al * 3 / 4 * 24.0, 2), 1.80)

# ---- S + O2
n_S = 1.60 / A['S']
eq("n S", round(n_S, 5), 0.04984)
eq("V SO2", sf(n_S * 24.0), 1.20)
eq("V SO2 4sf", round(n_S * 24.0, 3), 1.196)

# ---- P + O2
n_P = 6.20 / A['P']
eq("n P", round(n_P, 3), 0.200)
eq("n P4O10", round(n_P / 4, 4), 0.0500)
Mr_P4O10 = 4 * A['P'] + 10 * A['O']
eq("P4O10 Mr", Mr_P4O10, 284.0)
eq("mass P4O10", round(n_P / 4 * Mr_P4O10, 1), 14.2)
eq("n H3PO4", round(4 * n_P / 4, 3), 0.200)

# ---- PCl5 in water (exam practice)
Mr_PCl5 = A['P'] + 5 * A['Cl']
eq("PCl5 Mr", Mr_PCl5, 208.5)
n_PCl5 = 4.17 / Mr_PCl5
eq("n PCl5", round(n_PCl5, 4), 0.0200)
eq("n HCl", round(5 * n_PCl5, 3), 0.100)
eq("[H+]", round(5 * n_PCl5 / 0.500, 3), 0.200)
eq("pH PCl5", round(-log10(0.200), 2), 0.70)

# ---- successive ionisation energies: Z (577 1820 2740 11600) and W (786 1580 3230 4360)
Z = [577, 1820, 2740, 11600]; W = [786, 1580, 3230, 4360]
rZ = [Z[i + 1] / Z[i] for i in range(3)]; rW = [W[i + 1] / W[i] for i in range(3)]
assert rZ.index(max(rZ)) == 2 and max(rZ) > 3        # big jump after the 3rd: Group 13
assert max(rW) < 3 and round(max(rW), 1) == 2.0      # no jump: "about 2.0"
facts_succ = facts.split('Successive IE (1st 2nd 3rd 4th):')[1].split('\n')[0]
assert 'Al 577 1820 2740 11600' in facts_succ and 'Si 786 1580 3230 4360' in facts_succ

print("ok")
