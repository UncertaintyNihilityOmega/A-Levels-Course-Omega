# Writes widgets/periodic.js from data/elements.json (never type element data by hand).
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(HERE)
els = json.load(open(os.path.join(root, 'data', 'elements.json'), encoding='utf-8'))
keep = ['z', 'sym', 'name', 'ar', 'group', 'period', 'block', 'cat', 'config', 'short']
rows = [{k: e[k] for k in keep if k in e} for e in els]
data = '[\n' + ',\n'.join('    ' + json.dumps(r, ensure_ascii=False) for r in rows) + '\n  ]'
tpl = open(os.path.join(HERE, 'periodic.template.js'), encoding='utf-8').read()
os.makedirs(os.path.join(root, 'widgets'), exist_ok=True)
open(os.path.join(root, 'widgets', 'periodic.js'), 'w', encoding='utf-8', newline='\n').write(tpl.replace('/*DATA*/', data))
print('wrote', len(rows), 'elements')
