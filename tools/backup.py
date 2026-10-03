#!/usr/bin/env python3
"""Bundle all sources into dist/backup.json (published next to the page so work survives a container reset).
Restore with: python3 tools/backup.py --restore backup.json"""
import json, os, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) > 2 and sys.argv[1] == '--restore':
    data = json.load(open(sys.argv[2]))
    for rel, txt in data['files'].items():
        p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w').write(txt)
    print('restored', len(data['files']), 'files'); sys.exit()
pats = ['content/**/*.md', 'src/*', 'tools/*.py', 'tools/*.js', 'tools/*.json', '*.md', 'build.js', 'lib.js', 'package.json', 'package-lock.json']
files = {}
for pat in pats:
    for p in glob.glob(os.path.join(ROOT, pat), recursive=True):
        if os.path.isfile(p):
            files[os.path.relpath(p, ROOT)] = open(p, encoding='utf-8').read()
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
json.dump({'files': files}, open(os.path.join(ROOT, 'dist/backup.json'), 'w'))
print('backup:', len(files), 'files', round(os.path.getsize(os.path.join(ROOT, 'dist/backup.json')) / 1024), 'KB')
