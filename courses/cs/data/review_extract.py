# Review helper: print the why, key, warn, exam and quiz blocks of a chapter (and eg titles)
import sys, re
for cid in sys.argv[1:]:
    lines = open(f'chapters/{cid}.md', encoding='utf-8').read().split('\n')
    print(f'##### {cid}')
    keep = False
    for i, l in enumerate(lines, 1):
        m = re.match(r'^:::(\w+)(.*)', l)
        if m:
            kind = m.group(1)
            keep = kind in ('why', 'key', 'warn', 'exam', 'quiz')
            if kind in ('eg', 'try', 'def', 'note', 'tip', 'analogy'):
                print(f'{i}: [{kind}]{m.group(2)}')
            if keep:
                print(f'{i}: {l}')
            continue
        if l.strip() == ':::':
            keep = False
            continue
        if keep:
            print(l)
