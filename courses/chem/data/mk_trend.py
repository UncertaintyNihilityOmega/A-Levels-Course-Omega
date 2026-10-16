# data/mk_trend.py: builds widgets/chem-trend.js from data/chem-trend.tpl.js.
# The numbers are parsed from FACTS.md ("First IE", "Successive IE", "Pauling electronegativity"), never typed;
# symbols, names, Z, group, period and block come from data/elements.json.
# Run: py data/mk_trend.py
import json, re

facts = open('FACTS.md', encoding='utf-8').read().splitlines()

def line(prefix):
    for l in facts:
        if l.startswith(prefix):
            return l[len(prefix):]
    raise SystemExit('FACTS.md line not found: ' + prefix)

ie1 = {m.group(1): int(m.group(2)) for m in re.finditer(r'\b([A-Z][a-z]?) (\d+)\b', line('- First IE / kJ mol⁻¹:'))}
succ = {}
for part in line('- Successive IE (1st 2nd 3rd 4th):').split(';'):
    t = part.split()
    if t:
        succ[t[0]] = [int(x.rstrip('.')) for x in t[1:]]
en = {m.group(1): float(m.group(2)) for m in re.finditer(r'\b([A-Z][a-z]?) (\d\.\d)\b', line('- Pauling electronegativity:'))}

els = json.load(open('data/elements.json', encoding='utf-8'))
out = {}
for e in els:
    s = e['sym']
    if e['z'] <= 36 or s in ie1 or s in en or s in succ:
        out[s] = {'z': e['z'], 'name': e['name'], 'period': e['period'], 'group': e['group'], 'block': e['block'],
                  'ie1': ie1.get(s), 'en': en.get(s), 'succ': succ.get(s)}
# sanity: every parsed symbol is a real element, and the first value of each successive list equals the first IE
for d in (ie1, succ, en):
    assert all(s in out for s in d), [s for s in d if s not in out]
for s, v in succ.items():
    assert v[0] == ie1[s], (s, v[0], ie1[s])
assert len(ie1) == 38 and len(succ) == 20, (len(ie1), len(succ))
data = json.dumps({'el': out}, ensure_ascii=False, separators=(',', ':'))
tpl = open('data/chem-trend.tpl.js', encoding='utf-8').read()
open('widgets/chem-trend.js', 'w', encoding='utf-8').write(tpl.replace('/*DATA*/', data))
print('ok', len(ie1), 'first IE,', len(succ), 'successive,', len(en), 'EN,', len(data), 'bytes')
