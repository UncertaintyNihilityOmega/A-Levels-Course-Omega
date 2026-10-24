# checks/chem.org.synthesis2.py: recomputes every number in the Organic synthesis (A Level) chapter.
# Ar from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, N 14.0, O 16.0.
import json, os, re
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

here = os.path.dirname(os.path.abspath(__file__))
ar = {e['sym']: e['ar'] for e in json.load(open(os.path.join(here, '..', 'data', 'elements.json'), encoding='utf-8'))}
for sym, v in (("H", 1.0), ("C", 12.0), ("N", 14.0), ("O", 16.0)):
    eq("Ar " + sym, ar[sym], v)

def Mr(formula):
    tot = 0.0
    for sym, num in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
        tot += ar[sym] * (int(num) if num else 1)
    return tot

# benzene -> nitrobenzene (85.0 %) -> phenylamine (70.0 %), 10.0 g benzene
benz, anil = Mr("C6H6"), Mr("C6H7N")
eq("Mr benzene", benz, 78.0); eq("Mr phenylamine", anil, 93.0)
nb = 10.0 / benz
eq("n benzene", round(nb, 4), 0.1282)
overall = 0.850 * 0.700
eq("overall", round(overall, 3), 0.595)
eq("n phenylamine", round(nb * overall, 5), 0.07628)
eq("m phenylamine", round(nb * overall * anil, 2), 7.09)

# unknown compound A: [M+1] 7.7 % of M, benzamide C7H7NO
carbons = 100 * 7.7 / (1.1 * 100)
eq("carbons from [M+1]", round(carbons, 1), 7.0)
eq("Mr benzamide", Mr("C7H7NO"), 121.0)

# 13C environments from symmetry of the ring substitution pattern (substituent labels matter)
def ring_environments(subs):
    """subs: {ring position (1-6): group label}; number of distinct ring carbons under rotation and reflection symmetry"""
    group = []
    for rot in range(6):
        for flip in (1, -1):
            f = (lambda r, s: (lambda p: ((s * (p - 1) + r) % 6) + 1))(rot, flip)
            if all(subs.get(f(p)) == lab for p, lab in subs.items()) and len({f(p) for p in subs}) == len(subs):
                group.append(f)
    seen, orbits = set(), 0
    for c in range(1, 7):
        if c in seen:
            continue
        orbits += 1
        for f in group:
            seen.add(f(c))
    return orbits
eq("4-nitrobenzoic acid: all carbon peaks", ring_environments({1: "COOH", 4: "NO2"}) + 1, 5)
eq("3-nitrobenzoic acid: all carbon peaks", ring_environments({1: "COOH", 3: "NO2"}) + 1, 7)
eq("4-hydroxybenzoic acid peaks", ring_environments({1: "COOH", 4: "OH"}) + 1, 5)
eq("2-hydroxybenzoic acid peaks", ring_environments({1: "COOH", 2: "OH"}) + 1, 7)
eq("benzamide peaks (one substituent)", ring_environments({1: "CONH2"}) + 1, 5)

# yields
eq("two steps", round(0.800 * 0.600, 3), 0.480)
eq("three steps (quiz)", round(0.900 * 0.800 * 0.700, 3), 0.504)
nY = 12.0 / 120.0
eq("n Y", round(nY, 3), 0.100)
eq("m Z", round(nY * 0.504 * 150.0, 2), 7.56)
r1 = 0.800 * 0.750 * 0.600
r2 = 0.520 * 0.700
eq("route 1", round(r1, 3), 0.360); eq("route 2", round(r2, 3), 0.364)
eq("m Z route 2", round(24.0 / 120.0 * r2 * 150.0, 1), 10.9)

print("ok")
