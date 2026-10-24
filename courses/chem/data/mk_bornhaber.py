# builds widgets/chem-bornhaber.js from data/chem-bornhaber.tpl.js with the FACTS.md ionisation energies. Run: py data/mk_bornhaber.py
import re, json
facts = open('FACTS.md', encoding='utf-8').read()
first = [l for l in facts.splitlines() if l.startswith('- First IE')][0]
succ = [l for l in facts.splitlines() if l.startswith('- Successive IE')][0]
f1 = {m.group(1): float(m.group(2)) for m in re.finditer(r'\b([A-Z][a-z]?) (\d+)(?=[,.])', first.split(':', 1)[1])}
sc = {}
for part in succ.split(':', 1)[1].split(';'):
    t = part.strip().rstrip('.').split()
    sc[t[0]] = [int(x) for x in t[1:]]
IE = {}
for el in ['Na', 'K', 'Mg', 'Ca']:
    a = [int(f1[el])]
    if el in sc: a = sc[el][:2]
    else: a.append(0)
    IE[el] = a
js = 'const IE = ' + json.dumps(IE) + ';'
t = open('data/chem-bornhaber.tpl.js', encoding='utf-8').read()
assert '/*IE*/' in t
open('widgets/chem-bornhaber.js', 'w', encoding='utf-8').write(t.replace('/*IE*/', js))
print(js)
