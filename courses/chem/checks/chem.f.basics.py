# checks/chem.f.basics.py: recomputes every number and balanced equation in "Chemistry from zero".
# Ar values from the 9701 Periodic Table (data/elements.json), read here so nothing is typed from memory.
import json, os, re
from math import isclose
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
EL = {e['sym']: e for e in json.load(open(os.path.join(HERE, '..', 'data', 'elements.json'), encoding='utf-8'))}
AR = {s: e['ar'] for s, e in EL.items()}

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    d = Decimal(repr(x))
    exp = d.adjusted() - n + 1
    return float(d.quantize(Decimal(1).scaleb(exp), rounding=ROUND_HALF_UP))

# ---------- formula parser: atoms in a formula such as Ca3(PO4)2 or (NH4)2SO4 ----------
def atoms(formula):
    def parse(s, i=0):
        counts = {}
        while i < len(s):
            c = s[i]
            if c == '(':
                inner, i = parse(s, i + 1)
                m = re.match(r'\d+', s[i:])
                k = int(m.group()) if m else 1
                i += len(m.group()) if m else 0
                for a, n in inner.items():
                    counts[a] = counts.get(a, 0) + n * k
            elif c == ')':
                return counts, i + 1
            else:
                m = re.match(r'[A-Z][a-z]?', s[i:])
                a = m.group(); i += len(a)
                m2 = re.match(r'\d+', s[i:])
                k = int(m2.group()) if m2 else 1
                i += len(m2.group()) if m2 else 0
                counts[a] = counts.get(a, 0) + k
        return counts, i
    return parse(formula)[0]

def side(text):
    total = {}
    for term in text.split('+'):
        term = term.strip()
        m = re.match(r'(\d*)(.*)', term)
        k = int(m.group(1)) if m.group(1) else 1
        for a, n in atoms(m.group(2)).items():
            total[a] = total.get(a, 0) + n * k
    return total

def balanced(label, lhs, rhs):
    assert side(lhs) == side(rhs), f"{label}: {side(lhs)} != {side(rhs)}"

n_eq = 0
def bal(label, equation):
    global n_eq
    l, r = equation.split('->')
    balanced(label, l, r)
    n_eq += 1

# equations in the chapter (state symbols removed)
bal("Mg + O2", "2Mg + O2 -> 2MgO")
bal("methane", "CH4 + 2O2 -> CO2 + 2H2O")
bal("propane", "C3H8 + 5O2 -> 3CO2 + 4H2O")
bal("aluminium", "4Al + 3O2 -> 2Al2O3")
bal("Mg + H2SO4", "Mg + H2SO4 -> MgSO4 + H2")
bal("CuO + HNO3", "CuO + 2HNO3 -> Cu(NO3)2 + H2O")
bal("CaCO3 + HCl", "CaCO3 + 2HCl -> CaCl2 + H2O + CO2")
bal("Mg(OH)2 + HCl", "Mg(OH)2 + 2HCl -> MgCl2 + 2H2O")
bal("Zn + H2SO4", "Zn + H2SO4 -> ZnSO4 + H2")
bal("try N2+H2", "N2 + 3H2 -> 2NH3")
bal("try Na+H2O", "2Na + 2H2O -> 2NaOH + H2")
bal("try C2H6", "2C2H6 + 7O2 -> 4CO2 + 6H2O")
bal("try Fe", "4Fe + 3O2 -> 2Fe2O3")
bal("try Al+HCl", "2Al + 6HCl -> 2AlCl3 + 3H2")
bal("try Ca(OH)2+HNO3", "Ca(OH)2 + 2HNO3 -> Ca(NO3)2 + 2H2O")
bal("try CaCO3+HNO3", "CaCO3 + 2HNO3 -> Ca(NO3)2 + H2O + CO2")
bal("exam MgCO3", "MgCO3 + 2HCl -> MgCl2 + H2O + CO2")
bal("stretch fertiliser", "Ca3(PO4)2 + 3H2SO4 -> 3CaSO4 + 2H3PO4")
# the spot-the-error equation really is unbalanced (4 H left, 2 H right)
assert side("CH4 + 2O2") != side("CO2 + H2O")
assert side("CH4 + 2O2")['H'] == 4 and side("CO2 + H2O")['H'] == 2
assert side("CH4 + 2O2")['O'] == 4 and side("CO2 + H2O")['O'] == 3

# ---------- ionic formulas: smallest numbers making the charge zero ----------
from math import lcm
def ionic(qc, qa):
    L = lcm(qc, qa)
    return L // qc, L // qa
assert ionic(2, 1) == (1, 2)    # Ca(OH)2, MgCl2, Mg(NO3)2, ZnCl2
assert ionic(1, 2) == (2, 1)    # (NH4)2SO4, Ag2SO4, Na2SO4
assert ionic(3, 2) == (2, 3)    # Al2(SO4)3 and X2Y3
assert ionic(3, 1) == (1, 3)    # Al(OH)3, Al(NO3)3
assert ionic(1, 3) == (3, 1)    # K3PO4
assert ionic(2, 2) == (1, 1)    # CaO
assert ionic(1, 2) == (2, 1)    # (NH4)2CO3
assert 2 * 1 + (-2) == 0 and 2 * 3 + 3 * (-2) == 0 and 2 + 2 * (-1) == 0 + 0

# ---------- the atom ----------
def np_(A, Z, charge=0):
    return Z, A - Z, Z - charge
assert np_(27, 13) == (13, 14, 13)                       # worked example Al
assert np_(23, 11) == (11, 12, 11)                       # try (a) Na
assert np_(35, 17, -1) == (17, 18, 18)                   # try (b) Cl-
assert np_(27, 13, 3) == (13, 14, 10)                    # try (c) Al3+
assert np_(23, 11, 1) == (11, 12, 10)                    # quiz Na+
assert 19 + 20 == 39                                     # exam practice nucleon number

def shells(Z):
    out = []
    for cap in (2, 8, 8, 2):
        if Z <= 0: break
        k = min(cap, Z); out.append(k); Z -= k
    return out
assert shells(11) == [2, 8, 1]       # sodium
assert shells(13) == [2, 8, 3]       # aluminium
assert shells(16) == [2, 8, 6]       # sulfur
assert shells(15) == [2, 8, 5]       # phosphorus
assert shells(19) == [2, 8, 8, 1]    # exam practice
assert shells(17) == [2, 8, 7] and shells(10) == [2, 8]
# element and group/period from data/elements.json
assert EL['S']['group'] == 16 and EL['S']['period'] == 3 and EL['S']['z'] == 16
assert EL['P']['group'] == 15 and EL['P']['period'] == 3 and EL['P']['z'] == 15
assert EL['Na']['group'] == 1 and EL['Na']['period'] == 3
assert 6 + 10 == 16 and 5 + 10 == 15                      # outer electrons + 10 = group
assert EL['K']['z'] == 19 and EL['K']['group'] == 1
for sym in ('Fe', 'Cu'):
    assert EL[sym]['cat'] == 'transition metal'

# ---------- numbers ----------
eq("15% of 60", 0.15 * 60, 9)
eq("45000", 4.5e4, 45000)
eq("rounding eg", sf(0.0042516, 3), 0.00425)
eq("rounding eg std form", 4.25e-3, 0.00425)
eq("250 cm3", 250 / 1000, 0.250)
eq("try 35.0 cm3", 35.0 / 1000, 0.0350)
eq("try 0.0125 dm3", 0.0125 * 1000, 12.5)
eq("try kg", 2.5 * 1000, 2500)
eq("try kJ", 48 * 1000, 48000)
eq("try K", 25 + 273, 298)
eq("try round a", sf(0.0067845, 3), 0.00678)
eq("try round b", sf(1234.5, 3), 1230)
eq("try round c", sf(0.0003059, 2), 0.00031)
eq("try std a", 4.2e-5, 0.000042)
eq("try std b", 3.02e-2, 0.0302)
eq("try std c", 7.5e3, 7500)
eq("exam std form", sf(0.00040720, 3), 4.07e-4)
eq("0.00042 std", 4.2e-4, 0.00042)
eq("56000 std", 5.6e4, 56000)

# ---------- moles preview ----------
M_NaCl = AR['Na'] + AR['Cl']
eq("M NaCl", M_NaCl, 58.5)
eq("n NaCl", 5.85 / M_NaCl, 0.100, 1e-9)
M_H2O = 2 * AR['H'] + AR['O']
eq("M H2O", M_H2O, 18.0)
eq("n H2O", 9.00 / M_H2O, 0.500)
M_CaCO3 = AR['Ca'] + AR['C'] + 3 * AR['O']
eq("M CaCO3", M_CaCO3, 100.1)
eq("n CaCO3", sf(25.0 / M_CaCO3, 3), 0.250)
eq("n Mg", sf(12.0 / AR['Mg'], 3), 0.494)

print("ok")
