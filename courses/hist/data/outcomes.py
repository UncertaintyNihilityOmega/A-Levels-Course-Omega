import re, json, sys
L = open('scratch/syl.txt', encoding='utf-8').read().split('\n')
def section(a, b):
    out = []  # list of (topic, kq, [bullets])
    topic = None; kq = None; items = []
    for raw in L[a-1:b-1]:
        s = raw.strip().replace('\t', ' ')
        if not s or s == 'continued' or s.endswith(' continued') and re.match(r'^\d\.\d', s): continue
        if re.match(r'^(European|American|International) (o|O)ption', s): continue
        if s.startswith('Within each') or s.startswith('question is') or s.startswith('question.'): continue
        m = re.match(r'^(\d)\s+([A-Z].*)$', s)
        if m and not re.match(r'^\d\.\d', s):
            topic = s; continue
        m = re.match(r'^(\d\.\d)\s+(.*)$', s)
        if m:
            if out and out[-1][1].startswith(m.group(1)): kq = out[-1]; continue
            kq = [topic, s, []]; out.append(kq); continue
        if kq is None: continue
        if s.startswith('•'): kq[2].append(['• ' + s[1:].strip()]); continue
        if s.startswith('–') or s.startswith('○'):
            if not kq[2]: kq[2].append(['•'])
            kq[2][-1].append(s); continue
        # continuation line
        if kq[2] and len(kq[2][-1]) > 0:
            kq[2][-1][-1] += ' ' + s
        else:
            kq[1] += ' ' + s
    return out
AS = section(366, 1137); P4 = section(1281, 2091)
def fmt(sec):
    res = []; last = None
    for t, k, bl in sec:
        if t != last: res.append(f'\n### {t}'); last = t
        res.append(f'**{k}**')
        for b in bl:
            head = b[0]; subs = b[1:]
            line = head
            if subs:
                parts = []; cur = None
                for x in subs:
                    if x.startswith('–'): parts.append(x[1:].strip())
                    elif parts:
                        sep = ': ' if parts[-1].endswith('including') or parts[-1].endswith('nationalism in the Empire') else ', '
                        parts[-1] = parts[-1] + sep + x[1:].strip()
                    else: parts.append(x[1:].strip())
                line += ': ' + '; '.join(parts)
            res.append('- ' + line[2:])
    return '\n'.join(res)
json.dump({'AS': AS, 'P4': P4}, open('scratch/outcomes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
open('scratch/as.md', 'w', encoding='utf-8').write(fmt(AS))
open('scratch/p4.md', 'w', encoding='utf-8').write(fmt(P4))
print(len(AS), len(P4))
