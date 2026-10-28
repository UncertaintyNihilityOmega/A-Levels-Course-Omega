# REVIEW helper: numbers in a worked-example title that reappear in a practice question or quiz stem
import sys,re
for cid in sys.argv[1:]:
    t=open(f'chapters/{cid}.md',encoding='utf-8').read()
    egs=re.findall(r'^:::eg (.*)$',t,re.M)
    prac=t[t.find('## Practice'):] if '## Practice' in t else ''
    stems=[l for l in prac.split('\n') if l.startswith('Q:') or l.startswith('? ')]
    for e in egs:
        nums=set(re.findall(r'\d+(?:\.\d+)?',e))-{'1','2','3','4','5','6','10','100','1000'}
        for s in stems:
            hit=[n for n in nums if re.search(r'(?<![\d.])'+re.escape(n)+r'(?![\d.])',s)]
            if len(hit)>=2 or any('.' in h for h in hit): print(cid,'|',e[:70],'|',hit,'|',s[:90])
