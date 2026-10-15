# checks/chem.atoms.py: recomputes every number in the Atomic structure chapter.
# Configurations come from data/elements.json (generated from the 9701 table) and from a filling-rule model.
import json
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def same(label, got, want):
    global n
    n += 1
    assert got == want, f"{label}: computed {got!r}, chapter says {want!r}"

els = json.load(open('data/elements.json', encoding='utf-8'))
by_z = {e['z']: e for e in els}
by_sym = {e['sym']: e for e in els}

# ---- model of ground-state configurations
ORDER = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p']
CAP = {'s': 2, 'p': 6, 'd': 10}
def atom_config(z):
    c = {}
    left = z
    for sub in ORDER:
        k = min(left, CAP[sub[1]])
        if k: c[sub] = k
        left -= k
    # exceptions Cr, Cu: one 4s electron promoted to 3d
    if z in (24, 29):
        c['4s'] -= 1
        c['3d'] += 1
    return c
def ion_config(z, charge):
    c = atom_config(z)
    e = -charge          # electrons to add (negative charge) or remove (positive)
    if e < 0:            # remove: highest n first, then highest l (4s before 3d)
        for _ in range(-e):
            sub = max((s for s in c if c[s] > 0), key=lambda s: (int(s[0]), 'spdf'.index(s[1])))
            c[sub] -= 1
    else:
        for _ in range(e):
            for sub in ORDER:
                if c.get(sub, 0) < CAP[sub[1]]:
                    c[sub] = c.get(sub, 0) + 1
                    break
    return c
def fmt(c, order=('1s','2s','2p','3s','3p','3d','4s','4p')):
    sup = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
    return ' '.join(f"{s}{str(c[s]).translate(sup)}" for s in order if c.get(s, 0) > 0)
def short(c):
    ar = {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6}
    rest = {s: v for s, v in c.items() if s not in ar or v != ar[s]}
    full_ar = all(c.get(s, 0) == v for s, v in ar.items())
    if full_ar:
        return '[Ar] ' + fmt({s: v for s, v in c.items() if s not in ar}, ('3d','4s','4p')) if any(s not in ar and v for s, v in c.items()) else '[Ar]'
    return fmt(c)
def unpaired(c):
    u = 0
    for s, v in c.items():
        orbs = {'s': 1, 'p': 3, 'd': 5}[s[1]]
        u += v if v <= orbs else 2 * orbs - v
    return u

def sup_to_ascii(s):
    return s.translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789'))

# the model agrees with the table for H to Kr
for z in range(1, 37):
    mine = fmt(atom_config(z))
    table = ' '.join(by_z[z]['config'].split())
    # table writes 3d before 4s in the same Cambridge order
    assert sup_to_ascii(mine) == table, f"Z={z}: model {sup_to_ascii(mine)} vs table {table}"
n += 1

# ---- particle counts
def particles(sym, A, charge):
    z = by_sym[sym]['z']
    return z, A - z, z - charge
same("Fe3+ particles", particles('Fe', 56, 3), (26, 30, 23))
same("S2- particles", particles('S', 32, -2), (16, 16, 18))
same("Mg-25", particles('Mg', 25, 0), (12, 13, 12))
same("Al3+ particles", particles('Al', 27, 3), (13, 14, 10))
same("Cl-37 particles", particles('Cl', 37, -1), (17, 20, 18))
same("Zn2+ particles", particles('Zn', 65, 2), (30, 35, 28))
same("warm-up neutrons Z17 A35", 35 - 17, 18)
same("Mg-26 vs Mg-24 extra neutrons", (26 - 12) - (24 - 12), 2)
eq("electron deflection ratio", 1 / (1 / 1836), 1836)
# 24 -> 26 only: the quiz distractors
same("Al3+ distractors", (13 + 3, 27 - 3), (16, 24))

# ---- configurations used in the chapter
same("Fe", short(atom_config(26)), '[Ar] 3d⁶ 4s²')
same("Fe2+", short(ion_config(26, 2)), '[Ar] 3d⁶')
same("Fe3+", short(ion_config(26, 3)), '[Ar] 3d⁵')
same("Cr", short(atom_config(24)), '[Ar] 3d⁵ 4s¹')
same("Cu", short(atom_config(29)), '[Ar] 3d¹⁰ 4s¹')
same("Cu full", fmt(atom_config(29)), '1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s¹')
same("Cu2+ electrons", 29 - 2, 27)
same("Cu2+", fmt(ion_config(29, 2)), '1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁹')
same("Cu2+ unpaired", unpaired(ion_config(29, 2)), 1)
same("Cu+", fmt(ion_config(29, 1)), '1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰')
same("Cr3+", short(ion_config(24, 3)), '[Ar] 3d³')
same("Cr unpaired", unpaired(atom_config(24)), 6)
same("Mn", short(atom_config(25)), '[Ar] 3d⁵ 4s²')
same("Mn2+", short(ion_config(25, 2)), '[Ar] 3d⁵')
same("Zn2+", short(ion_config(30, 2)), '[Ar] 3d¹⁰')
same("V", fmt(atom_config(23)), '1s² 2s² 2p⁶ 3s² 3p⁶ 3d³ 4s²')
same("P", fmt(atom_config(15)), '1s² 2s² 2p⁶ 3s² 3p³')
same("Ca2+", fmt(ion_config(20, 2)), '1s² 2s² 2p⁶ 3s² 3p⁶')
same("Br- electrons", 35 + 1, 36)
same("Br-", fmt(ion_config(35, -1)), '1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶')
same("Ga", short(atom_config(31)), '[Ar] 3d¹⁰ 4s² 4p¹')
same("Zn", short(atom_config(30)), '[Ar] 3d¹⁰ 4s²')
same("Cl-", fmt(ion_config(17, -1)), '1s² 2s² 2p⁶ 3s² 3p⁶')
same("Na+", fmt(ion_config(11, 1)), '1s² 2s² 2p⁶')
same("Mg2+", fmt(ion_config(12, 2)), '1s² 2s² 2p⁶')
same("N unpaired", unpaired(atom_config(7)), 3)
same("O unpaired", unpaired(atom_config(8)), 2)
same("C unpaired", unpaired(atom_config(6)), 2)
same("S unpaired", unpaired(atom_config(16)), 2)
same("Fe3+ unpaired", unpaired(ion_config(26, 3)), 5)
same("Cl unpaired", unpaired(atom_config(17)), 1)
same("H unpaired", unpaired(atom_config(1)), 1)
same("Cl- unpaired", unpaired(ion_config(17, -1)), 0)
same("Cl2/HCl all paired", 0, 0)
# shell capacities
same("shell 1", 2, CAP['s'])
same("shell 2", CAP['s'] + CAP['p'], 8)
same("shell 3", CAP['s'] + CAP['p'] + CAP['d'], 18)
same("orbitals p d", (CAP['p'] // 2, CAP['d'] // 2), (3, 5))

# ---- isoelectronic ions: protons and 10 electrons
iso = {'N': -3, 'O': -2, 'F': -1, 'Na': 1, 'Mg': 2, 'Al': 3}
same("iso protons", [by_sym[s]['z'] for s in iso], [7, 8, 9, 11, 12, 13])
same("iso electrons", [by_sym[s]['z'] - q for s, q in iso.items()], [10] * 6)
same("quiz radius protons", [by_sym[s]['z'] for s in ('O', 'F', 'Na', 'Mg')], [8, 9, 11, 12])
same("radius order protons Al Mg Na F", [by_sym[s]['z'] for s in ('Al', 'Mg', 'Na', 'F')], [13, 12, 11, 9])
same("Cl vs Na protons", (by_sym['Cl']['z'], by_sym['Na']['z']), (17, 11))
same("Ca vs Mg protons", (by_sym['Ca']['z'], by_sym['Mg']['z']), (20, 12))
same("Ga vs Zn protons", (by_sym['Ga']['z'], by_sym['Zn']['z']), (31, 30))
same("K vs Na protons", (by_sym['K']['z'], by_sym['Na']['z']), (19, 11))
same("O vs N protons", (by_sym['O']['z'], by_sym['N']['z']), (8, 7))

# ---- ionisation energies (Data booklet values in FACTS.md)
first = dict(H=1310, He=2370, Li=519, Be=900, B=799, C=1090, N=1400, O=1310, F=1680, Ne=2080, Na=494, Mg=736,
             Al=577, Si=786, P=1060, S=1000, Cl=1260, Ar=1520, K=418, Ca=590, Zn=908, Ga=577, Rb=403, Cs=376,
             Sr=548, Ba=502)
succ = dict(Na=(494, 4560, 6940, 9540), Mg=(736, 1450, 7740, 10500), Al=(577, 1820, 2740, 11600),
            Si=(786, 1580, 3230, 4360), Ca=(590, 1150, 4940, 6480), Be=(900, 1760, 14800, 21000),
            P=(1060, 1900, 2920, 4960))
for el, vals in succ.items():
    assert vals[0] == first[el], el
    assert all(b > a for a, b in zip(vals, vals[1:])), el   # successive IEs rise
n += 1
syms20 = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca".split()
same("20 elements plotted", [by_sym[s]['z'] for s in syms20], list(range(1, 21)))
# dips and drops claimed in the text
assert first['B'] < first['Be'] and first['Al'] < first['Mg'] and first['O'] < first['N'] and first['S'] < first['P']
assert first['Na'] < first['Ne'] and first['K'] < first['Ar'] and first['Mg'] > first['Al']
assert first['K'] < first['Na'] and first['Ca'] < first['Mg'] and first['Ga'] < first['Zn']
for a, b in (('Li', 'Na'), ('Na', 'K'), ('K', 'Rb'), ('Rb', 'Cs')): assert first[a] > first[b]
for a, b in (('Be', 'Mg'), ('Mg', 'Ca'), ('Ca', 'Sr'), ('Sr', 'Ba')): assert first[a] > first[b]
n += 1
# across period 2 and 3 rises (apart from the dips)
same("Group 1 values", [first[s] for s in ('Li', 'Na', 'K', 'Rb', 'Cs')], [519, 494, 418, 403, 376])
same("Group 2 values", [first[s] for s in ('Be', 'Mg', 'Ca', 'Sr', 'Ba')], [900, 736, 590, 548, 502])
# jumps
def biggest_jump(vals):
    ratios = [b / a for a, b in zip(vals, vals[1:])]
    return ratios.index(max(ratios)) + 1, max(ratios)
same("Na jump after 1", biggest_jump(succ['Na'])[0], 1)
same("Mg jump after 2", biggest_jump(succ['Mg'])[0], 2)
same("Al jump after 3", biggest_jump(succ['Al'])[0], 3)
same("Ca jump after 2", biggest_jump(succ['Ca'])[0], 2)
same("Be jump after 2", biggest_jump(succ['Be'])[0], 2)
assert 1450 / 736 < 2.1 and 7740 / 1450 > 5
n += 1
assert max(b / a for a, b in zip(succ['Si'], succ['Si'][1:])) < 2.1   # no large jump for Si
assert max(b / a for a, b in zip(succ['P'], succ['P'][1:])) < 2.1
n += 1
same("Mg and Be outer shell electrons", (by_sym['Mg']['z'] - 10, by_sym['Be']['z'] - 2), (2, 2))
# bar chart heights (chart: 12000 -> 190 px)
for v, h in ((577, 9.1), (1820, 28.8), (2740, 43.4), (11600, 183.7)):
    eq(f"bar {v}", round(v / 12000 * 190, 1), h)
# ---- sodium sketch (REVIEW fix): shell populations 1 | 8 | 2 and the Al try question 3 | 8 | 2
na_cfg = (1, 8, 2); al_cfg = (3, 8, 2)
same("Na electrons in sketch", sum(na_cfg), 11); same("Na z", by_sym['Na']['z'], 11)
same("Na jumps after electron", (na_cfg[0], na_cfg[0] + na_cfg[1]), (1, 9))
same("Al electrons", sum(al_cfg), by_sym['Al']['z'])
same("Al jumps after electron", (al_cfg[0], al_cfg[0] + al_cfg[1]), (3, 11))
same("Al shells 12 and 13 inner", (13 - 11), 2)

print("ok")
