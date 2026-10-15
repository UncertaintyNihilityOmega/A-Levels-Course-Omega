import json
els = json.load(open('data/elements.json', encoding='utf-8'))
data = json.dumps([[e['sym'], e['name'], e['ar']] for e in els], ensure_ascii=False)
tpl = open('data/molar.tpl.js', encoding='utf-8').read()
open('widgets/molar.js', 'w', encoding='utf-8').write(tpl.replace('/*DATA*/', data))
print('ok', len(data))
