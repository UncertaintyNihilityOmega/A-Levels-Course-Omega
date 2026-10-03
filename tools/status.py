#!/usr/bin/env python3
"""Progress report: which work packages are done, and what the next one needs.  python3 tools/status.py"""
import glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = json.load(open(os.path.join(ROOT, 'tools', 'wp.json'), encoding='utf-8'))
have, reg = set(), set()
for p in glob.glob(os.path.join(ROOT, 'content', '**', '*.md'), recursive=True):
    have.update(re.findall(r'^@chapter\s+(\S+)', open(p, encoding='utf-8').read(), re.M))
for p in glob.glob(os.path.join(ROOT, 'src', 'widgets*.js')):
    reg.update(re.findall(r"W\.register\(\s*'([a-z0-9]+)'", open(p, encoding='utf-8').read()))
sp = os.path.join(ROOT, 'STATUS.md')
status = open(sp, encoding='utf-8').read() if os.path.exists(sp) else ''
nxt = missing = None
for wp in W['packages']:
    items = wp.get('chapters') or wp.get('widgets') or []
    pool = have if 'chapters' in wp else reg
    got = [i for i in items if i in pool]
    done = bool(items and len(got) == len(items)) or bool(re.search(r'DONE\s+' + wp['id'] + r'\b', status))
    mark = 'done' if done else (f'{len(got)}/{len(items)}' if items else 'todo')
    print(f"{wp['id']:<5} {mark:<5} {wp['title']}")
    if not done and nxt is None:
        nxt, missing = wp, [i for i in items if i not in pool]
print(f"\n{len(have)} chapters exist; widgets: {', '.join(sorted(reg))}")
if nxt:
    print(f"\nNEXT: {nxt['id']} ({nxt['type']}) - {nxt['title']}")
    if missing: print('  to do:', ', '.join(missing))
    if nxt.get('file'): print('  file:', nxt['file'])
    if nxt.get('syllabus'): print('  syllabus:', W['syllabi'].get(nxt['syllabus'], nxt['syllabus']))
    if nxt.get('topics'): print('  topics:', nxt['topics'])
    if nxt.get('notes'): print('  notes:', nxt['notes'])
    if nxt.get('spec'): print('  spec: read', nxt['spec'])
else:
    print('\nAll packages done.')
