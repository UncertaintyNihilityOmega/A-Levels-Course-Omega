# builds widgets/chem-cell.js from data/chem-cell.tpl.js and the FACTS.md E° / V line (no E value is typed here). Run: py data/mk_cell.py
import re, json
facts = open('FACTS.md', encoding='utf-8').read()
line = [l for l in facts.splitlines() if l.startswith('- E° / V:')][0]
E = {}
for item in line[len('- E° / V:'):].strip().rstrip('.').split(';'):
    m = re.match(r'(.+?)\s([+\-−]?\d+\.\d\d)$', item.strip())
    E[m.group(1).strip()] = float(m.group(2).replace('−', '-'))
# id, FACTS key, label, lhs species (no electrons), rhs species, z, kind, electrode text, solution text, nernst
S = [
 ('Li','Li⁺/Li','Li⁺/Li',[(1,'Li⁺(aq)')],[(1,'Li(s)')],1,'metal','Li(s)','Li⁺(aq)'),
 ('K','K⁺/K','K⁺/K',[(1,'K⁺(aq)')],[(1,'K(s)')],1,'metal','K(s)','K⁺(aq)'),
 ('Ca','Ca²⁺/Ca','Ca²⁺/Ca',[(1,'Ca²⁺(aq)')],[(1,'Ca(s)')],2,'metal','Ca(s)','Ca²⁺(aq)'),
 ('Na','Na⁺/Na','Na⁺/Na',[(1,'Na⁺(aq)')],[(1,'Na(s)')],1,'metal','Na(s)','Na⁺(aq)'),
 ('Mg','Mg²⁺/Mg','Mg²⁺/Mg',[(1,'Mg²⁺(aq)')],[(1,'Mg(s)')],2,'metal','Mg(s)','Mg²⁺(aq)'),
 ('Al','Al³⁺/Al','Al³⁺/Al',[(1,'Al³⁺(aq)')],[(1,'Al(s)')],3,'metal','Al(s)','Al³⁺(aq)'),
 ('Zn','Zn²⁺/Zn','Zn²⁺/Zn',[(1,'Zn²⁺(aq)')],[(1,'Zn(s)')],2,'metal','Zn(s)','Zn²⁺(aq)'),
 ('Fe','Fe²⁺/Fe','Fe²⁺/Fe',[(1,'Fe²⁺(aq)')],[(1,'Fe(s)')],2,'metal','Fe(s)','Fe²⁺(aq)'),
 ('Ni','Ni²⁺/Ni','Ni²⁺/Ni',[(1,'Ni²⁺(aq)')],[(1,'Ni(s)')],2,'metal','Ni(s)','Ni²⁺(aq)'),
 ('Sn','Sn²⁺/Sn','Sn²⁺/Sn',[(1,'Sn²⁺(aq)')],[(1,'Sn(s)')],2,'metal','Sn(s)','Sn²⁺(aq)'),
 ('Pb','Pb²⁺/Pb','Pb²⁺/Pb',[(1,'Pb²⁺(aq)')],[(1,'Pb(s)')],2,'metal','Pb(s)','Pb²⁺(aq)'),
 ('H','2H⁺/H₂','H⁺/H₂ (SHE)',[(2,'H⁺(aq)')],[(1,'H₂(g)')],2,'gas','Pt, H₂(g) 101 kPa','H⁺(aq)'),
 ('Cu','Cu²⁺/Cu','Cu²⁺/Cu',[(1,'Cu²⁺(aq)')],[(1,'Cu(s)')],2,'metal','Cu(s)','Cu²⁺(aq)'),
 ('Cu+','Cu⁺/Cu','Cu⁺/Cu',[(1,'Cu⁺(aq)')],[(1,'Cu(s)')],1,'metal','Cu(s)','Cu⁺(aq)'),
 ('Ag','Ag⁺/Ag','Ag⁺/Ag',[(1,'Ag⁺(aq)')],[(1,'Ag(s)')],1,'metal','Ag(s)','Ag⁺(aq)'),
 ('I2','I₂/I⁻','I₂/I⁻',[(1,'I₂(aq)')],[(2,'I⁻(aq)')],2,'nonmetal','Pt','I₂(aq), I⁻(aq)'),
 ('Br2','Br₂/Br⁻','Br₂/Br⁻',[(1,'Br₂(aq)')],[(2,'Br⁻(aq)')],2,'nonmetal','Pt','Br₂(aq), Br⁻(aq)'),
 ('Cl2','Cl₂/Cl⁻','Cl₂/Cl⁻',[(1,'Cl₂(g)')],[(2,'Cl⁻(aq)')],2,'gas','Pt, Cl₂(g) 101 kPa','Cl⁻(aq)'),
 ('F2','F₂/F⁻','F₂/F⁻',[(1,'F₂(g)')],[(2,'F⁻(aq)')],2,'gas','Pt, F₂(g) 101 kPa','F⁻(aq)'),
 ('Fe3','Fe³⁺/Fe²⁺','Fe³⁺/Fe²⁺',[(1,'Fe³⁺(aq)')],[(1,'Fe²⁺(aq)')],1,'ions','Pt','Fe³⁺(aq), Fe²⁺(aq)'),
 ('Cu2','Cu²⁺/Cu⁺','Cu²⁺/Cu⁺',[(1,'Cu²⁺(aq)')],[(1,'Cu⁺(aq)')],1,'ions','Pt','Cu²⁺(aq), Cu⁺(aq)'),
 ('Sn4','Sn⁴⁺/Sn²⁺','Sn⁴⁺/Sn²⁺',[(1,'Sn⁴⁺(aq)')],[(1,'Sn²⁺(aq)')],2,'ions','Pt','Sn⁴⁺(aq), Sn²⁺(aq)'),
 ('V3','V³⁺/V²⁺','V³⁺/V²⁺',[(1,'V³⁺(aq)')],[(1,'V²⁺(aq)')],1,'ions','Pt','V³⁺(aq), V²⁺(aq)'),
 ('O2','O₂ + 4H⁺ + 4e⁻ ⇌ 2H₂O','O₂/H₂O (acid)',[(1,'O₂(g)'),(4,'H⁺(aq)')],[(2,'H₂O(l)')],4,'gas','Pt, O₂(g) 101 kPa','H⁺(aq)'),
 ('Cr2O7','Cr₂O₇²⁻ + 14H⁺ + 6e⁻ ⇌ 2Cr³⁺ + 7H₂O','Cr₂O₇²⁻/Cr³⁺',[(1,'Cr₂O₇²⁻(aq)'),(14,'H⁺(aq)')],[(2,'Cr³⁺(aq)'),(7,'H₂O(l)')],6,'other','Pt','Cr₂O₇²⁻, Cr³⁺, H⁺'),
 ('MnO4','MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O','MnO₄⁻/Mn²⁺',[(1,'MnO₄⁻(aq)'),(8,'H⁺(aq)')],[(1,'Mn²⁺(aq)'),(4,'H₂O(l)')],5,'other','Pt','MnO₄⁻, Mn²⁺, H⁺'),
]
out = []
for (i, key, label, lhs, rhs, z, kind, elec, sol) in S:
    out.append({'id': i, 'label': label, 'E': E[key], 'z': z, 'kind': kind, 'lhs': lhs, 'rhs': rhs, 'elec': elec, 'sol': sol,
                'nernst': kind in ('metal', 'ions')})
out.sort(key=lambda d: d['E'])  # most negative first, as in the chapter's table
js = 'const HC = ' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';'
t = open('data/chem-cell.tpl.js', encoding='utf-8').read()
assert '/*HC*/' in t
open('widgets/chem-cell.js', 'w', encoding='utf-8').write(t.replace('/*HC*/', js))
print(len(out), len(js))
