import json
els = json.load(open('data/elements.json', encoding='utf-8'))
data = json.dumps([[e['sym'], e['name']] for e in els if e['z'] <= 36], ensure_ascii=False)
tpl = open('data/chem-config.tpl.js', encoding='utf-8').read()
open('widgets/chem-config.js', 'w', encoding='utf-8').write(tpl.replace('/*DATA*/', data))
print('ok', len(data))
