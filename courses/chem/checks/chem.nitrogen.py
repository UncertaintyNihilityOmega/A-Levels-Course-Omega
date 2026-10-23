# checks/chem.nitrogen.py: recomputes every number in the Nitrogen and sulfur chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table); bond energies from FACTS.md.
# Not from the syllabus Data section (standard data tables, rounded): N2 boils at -196 degrees C; unpolluted rain has pH
# about 5.6 (CO2 dissolved); air is about 78% nitrogen by volume.
import json
from math import isclose
from collections import Counter
import re

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

E = {e['sym']: e for e in json.load(open('data/elements.json', encoding='utf-8'))}
A = {s: e['ar'] for s, e in E.items()}
facts = open('FACTS.md', encoding='utf-8').read()

for s, v in dict(H=1.0, C=12.0, N=14.0, O=16.0, S=32.1).items():
    eq("Ar " + s, A[s], v)

# ---- bond energies (FACTS.md Data booklet values)
exact = [l for l in facts.split('\n') if l.startswith('- Bond energies, exact')][0]
avg = [l for l in facts.split('\n') if l.startswith('- Bond energies, average')][0]
for k in ("N≡N 944", "O=O 496", "H–H 436"):
    assert k in exact, k
for k in ("N–N 160", "N=N 410", "N–H 390"):
    assert k in avg, k
assert 944 > 3 * 160                      # triple bond far more than three single bonds
eq("N2 vs O2 ratio", round(944 / 496, 1), 1.9)

# ---- worked example: delta H for N2 + 3H2 -> 2NH3
broken = 944 + 3 * 436
made = 6 * 390
eq("broken", broken, 2252)
eq("made", made, 2340)
eq("dH Haber", broken - made, -88)
# exam: 1/2 N2 + 3/2 H2 -> NH3
b2 = 0.5 * 944 + 1.5 * 436
eq("half N2", 0.5 * 944, 472)
eq("3/2 H2", 1.5 * 436, 654)
eq("broken per NH3", b2, 1126)
eq("made per NH3", 3 * 390, 1170)
eq("dH per NH3", b2 - 3 * 390, -44)

# ---- percentage of N in the fertilisers
Mr_AN = 2 * A['N'] + 4 * A['H'] + 3 * A['O']
Mr_AS = 2 * (A['N'] + 4 * A['H']) + A['S'] + 4 * A['O']
eq("Mr NH4NO3", Mr_AN, 80.0)
eq("Mr (NH4)2SO4", Mr_AS, 132.1)
eq("%N NH4NO3", sf(2 * A['N'] / Mr_AN * 100), 35.0)
eq("%N (NH4)2SO4", sf(2 * A['N'] / Mr_AS * 100), 21.2)
eq("quiz wrong 17.5", sf(A['N'] / Mr_AN * 100), 17.5)
eq("quiz wrong 70.0", sf(Mr_AN * 0 + 2 * 2 * A['N'] / Mr_AN * 100), 70.0)
assert 2 * A['N'] / Mr_AN > 2 * A['N'] / Mr_AS

# ---- sulfur to sulfuric acid
Mr_H2SO4 = 2 * A['H'] + A['S'] + 4 * A['O']
eq("Mr H2SO4", Mr_H2SO4, 98.1)
nS = 100 / A['S']
eq("n S", round(nS, 3), 3.115)
eq("m H2SO4", sf(nS * Mr_H2SO4), 306)
eq("64.2 g S", 64.2 / A['S'], 2.00)
eq("m 2.00 mol H2SO4", sf(2.00 * Mr_H2SO4), 196)

# ---- stretch: yield of ammonium sulfate
Mr_NH3 = A['N'] + 3 * A['H']
eq("Mr NH3", Mr_NH3, 17.0)
nN = 1700 / Mr_NH3
eq("n NH3", nN, 100)
nAS = nN / 2
eq("n AS", nAS, 50.0)
mAS = nAS * Mr_AS
eq("max mass", round(mAS), 6605)
eq("yield", round(5800 / mAS * 100, 1), 87.8)

# ---- oxidation numbers
eq("N in NO2", 4, 0 - 2 * (-2))
eq("N in NO", 2, 0 - (-2))
eq("N in HNO3", 5, -(1 + 3 * (-2)))
eq("N in HNO2", 3, -(1 + 2 * (-2)))
eq("C in CO", 2, 0 - (-2))
eq("C in CO2", 4, 0 - 2 * (-2))
eq("S in SO2", 4, 0 - 2 * (-2))
eq("S in SO3", 6, 0 - 3 * (-2))

# ---- atom balance of the equations (parse simple formulae)
def parse(f):
    # formula like (NH4)2SO4, CO2, C3H8, H2S2O7 -> Counter
    def grp(s):
        cnt = Counter()
        i = 0
        stack = [Counter()]
        while i < len(s):
            c = s[i]
            if c == '(':
                stack.append(Counter()); i += 1
            elif c == ')':
                i += 1
                m = re.match(r'\d+', s[i:])
                k = int(m.group()) if m else 1
                i += len(m.group()) if m else 0
                top = stack.pop()
                for e, n in top.items():
                    stack[-1][e] += n * k
            else:
                m = re.match(r'([A-Z][a-z]?)(\d*)', s[i:])
                e, n = m.group(1), int(m.group(2) or 1)
                stack[-1][e] += n
                i += len(m.group())
        return stack[0]
    return grp(f)

def side(terms):
    tot = Counter()
    for coef, f in terms:
        for e, n in parse(f).items():
            tot[e] += coef * n
    return tot

def balanced(label, left, right):
    l, r = side(left), side(right)
    assert l == r, f"{label}: left {dict(l)} right {dict(r)}"

balanced("NH3+HCl", [(1, 'NH3'), (1, 'HCl')], [(1, 'NH4Cl')])
balanced("NH3+HNO3", [(1, 'NH3'), (1, 'HNO3')], [(1, 'NH4NO3')])
balanced("NH3+H2SO4", [(2, 'NH3'), (1, 'H2SO4')], [(1, '(NH4)2SO4')])
balanced("NH4Cl+NaOH", [(1, 'NH4Cl'), (1, 'NaOH')], [(1, 'NaCl'), (1, 'NH3'), (1, 'H2O')])
balanced("NH4+ + OH-", [(1, 'NH4'), (1, 'OH')], [(1, 'NH3'), (1, 'H2O')])   # charges cancel (+1, -1)
balanced("N2+O2", [(1, 'N2'), (1, 'O2')], [(2, 'NO')])
balanced("NO+O2", [(2, 'NO'), (1, 'O2')], [(2, 'NO2')])
balanced("CO+NO", [(2, 'CO'), (2, 'NO')], [(2, 'CO2'), (1, 'N2')])
balanced("CO+NO2", [(4, 'CO'), (2, 'NO2')], [(4, 'CO2'), (1, 'N2')])
balanced("C3H8+NO", [(1, 'C3H8'), (10, 'NO')], [(3, 'CO2'), (4, 'H2O'), (5, 'N2')])
balanced("NO2+H2O", [(2, 'NO2'), (1, 'H2O')], [(1, 'HNO3'), (1, 'HNO2')])
balanced("4NO2", [(4, 'NO2'), (1, 'O2'), (2, 'H2O')], [(4, 'HNO3')])
balanced("SO2+NO2", [(1, 'SO2'), (1, 'NO2')], [(1, 'SO3'), (1, 'NO')])
balanced("SO3+H2O", [(1, 'SO3'), (1, 'H2O')], [(1, 'H2SO4')])
balanced("SO3+H2SO4", [(1, 'SO3'), (1, 'H2SO4')], [(1, 'H2S2O7')])
balanced("H2S2O7+H2O", [(1, 'H2S2O7'), (1, 'H2O')], [(2, 'H2SO4')])
balanced("CaCO3+H2SO4", [(1, 'CaCO3'), (1, 'H2SO4')], [(1, 'CaSO4'), (1, 'H2O'), (1, 'CO2')])
# half-oxygen equations: SO2 + 1/2 O2 -> SO3 and NO + 1/2 O2 -> NO2 (doubled)
balanced("SO2+O2", [(2, 'SO2'), (1, 'O2')], [(2, 'SO3')])
balanced("NO+1/2O2", [(2, 'NO'), (1, 'O2')], [(2, 'NO2')])
# adding the two catalytic steps: SO2 + NO2 + NO + 1/2 O2 -> SO3 + NO + NO2 ; NO2 and NO cancel
# electrons for the displacement: charges balance
eq("charge NH4+ + OH-", +1 - 1, 0)

# ---- electrons: N from +2 to 0 and C from +2 to +4 in 2CO + 2NO
eq("N electrons gained per N", 2 - 0, 2)
eq("C electrons lost per C", 4 - 2, 2)
eq("2CO+2NO electrons", 2 * 2, 2 * 2)

print("ok")
