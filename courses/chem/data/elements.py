# data/elements.py: builds data/elements.json from the 9701 syllabus Periodic Table (page 91 of the
# syllabus PDF, extracted to scratch/syl.txt by the LEAD session). Never type element data by hand.
# Each element: z, sym, name (British), ar (1 d.p., None if the table shows "–"), group (1-18, None for f-block),
# period, block, cat, config (full, Z <= 36 only), short (shorthand, Z <= 36 only).
# Run: py data/elements.py   -> prints a summary and writes data/elements.json (needs scratch/syl.txt)
import re, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
txt = open(os.path.join(HERE, '..', 'scratch', 'syl.txt'), encoding='utf-8').read()
page = txt.split('=====PAGE 91')[1].split('=====PAGE 92')[0]
t = [x.strip() for x in page.split('\n')]

els = {}
for i in range(len(t) - 3):
    z, s, n, a = t[i:i + 4]
    if re.fullmatch(r'\d{1,3}', z) and re.fullmatch(r'[A-Z][a-z]{0,2}', s) and re.fullmatch(r'[a-z]+', n) \
            and (re.fullmatch(r'\d+\.\d', a) or a in ('–', '-')):
        els[int(z)] = (s, n, None if a in ('–', '-') else float(a))
# The PDF text puts the lanthanoid/actinoid labels between "Ac" and "actinium"; the table shows 89 Ac actinium "–".
i = t.index('Ac')
assert t[i - 1] == '89' and 'actinium' in t[i:i + 4]
els[89] = ('Ac', 'actinium', None)
assert sorted(els) == list(range(1, 119)), 'missing elements'

def period(z):
    for p, last in enumerate([2, 10, 18, 36, 54, 86, 118], 1):
        if z <= last:
            return p

def group_block(z):
    p = period(z)
    start = [0, 1, 3, 11, 19, 37, 55, 87][p]
    k = z - start            # 0-based position in the period
    if p == 1:
        return (1, 's') if z == 1 else (18, 's')
    if p <= 3:
        return (k + 1, 's') if k < 2 else (k + 11, 'p')
    if p <= 5:
        if k < 2: return (k + 1, 's')
        if k < 12: return (k + 1, 'd')
        return (k + 1, 'p')
    # periods 6 and 7: La/Ac sit in group 3 here (the Cambridge table puts 57-71 and 89-103 in the f rows)
    if k < 2: return (k + 1, 's')
    if k < 17: return (None, 'f')            # 57-71, 89-103 shown in the f-block rows
    j = k - 14                                # 72 -> 4 ...
    if j < 12: return (j + 1, 'd')
    return (j + 1, 'p')

def category(z, g, b):
    if b == 'f': return 'lanthanoid' if z < 89 else 'actinoid'
    if z == 1: return 'non-metal'
    if g == 18: return 'noble gas'
    if g == 1: return 'alkali metal'
    if g == 2: return 'alkaline earth metal'
    if g == 17: return 'halogen'
    if b == 'd': return 'd-block metal' if g in (3, 12) else 'transition metal'   # 9701: Sc and Zn are not transition elements
    metalloids = {5, 14, 32, 33, 51, 52}
    nonmetals = {6, 7, 8, 15, 16, 34}
    if z in metalloids: return 'metalloid'
    if z in nonmetals: return 'non-metal'
    return 'post-transition metal'

ORDER = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p']
CAP = {'s': 2, 'p': 6, 'd': 10}
NOBLE = {2: 'He', 10: 'Ne', 18: 'Ar'}

def config(z):
    occ, left = {}, z
    for sub in ORDER:
        if left == 0: break
        n = min(CAP[sub[1]], left)
        occ[sub] = n
        left -= n
    if z in (24, 29):        # Cr [Ar] 3d5 4s1, Cu [Ar] 3d10 4s1
        occ['4s'] = 1
        occ['3d'] = occ['3d'] + 1
    # written in shell order (3d before 4s), the Cambridge convention
    written = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p']
    full = ' '.join(f'{s}{occ[s]}' for s in written if occ.get(s))
    core = max([k for k in NOBLE if k < z], default=None) if z > 2 else None
    if core:
        skip = {2: ['1s'], 10: ['1s', '2s', '2p'], 18: ['1s', '2s', '2p', '3s', '3p']}[core]
        short = f'[{NOBLE[core]}] ' + ' '.join(f'{s}{occ[s]}' for s in written if occ.get(s) and s not in skip)
    else:
        short = full
    return full, short

out = []
for z in range(1, 119):
    s, n, a = els[z]
    g, b = group_block(z)
    e = dict(z=z, sym=s, name=n, ar=a, group=g, period=period(z), block=b, cat=category(z, g, b))
    if z <= 36:
        e['config'], e['short'] = config(z)
    out.append(e)

# spot checks against facts every chemist knows
by = {e['sym']: e for e in out}
assert by['Cl']['ar'] == 35.5 and by['Cu']['ar'] == 63.5 and by['Na']['group'] == 1 and by['Fe']['period'] == 4
assert by['Fe']['short'] == '[Ar] 3d6 4s2' and by['Cr']['short'] == '[Ar] 3d5 4s1' and by['Cu']['short'] == '[Ar] 3d10 4s1'
assert by['Br']['group'] == 17 and by['Br']['block'] == 'p' and by['Hf']['group'] == 4 and by['La']['block'] == 'f'
assert by['Al']['name'] == 'aluminium' and by['S']['name'] == 'sulfur' and by['Cs']['name'] == 'caesium'
json.dump(out, open(os.path.join(HERE, 'elements.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(out), 'elements;', sum(e['ar'] is None for e in out), 'without Ar;', by['Kr']['config'])
