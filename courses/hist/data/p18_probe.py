# Runs the widget probes for P18 (builds no new widget file: it uses hist-timeline in both chapters and hist-chart in chapter 3, with own data).
import re, subprocess, io

jobs = [('hist.int.1929.3', 'hist-timeline'), ('hist.int.1929.3', 'hist-chart'), ('hist.int.1929.4', 'hist-timeline')]
for cid, w in jobs:
    ch = io.open('chapters/%s.md' % cid, encoding='utf-8').read()
    m = re.search(r'<div class="widget" data-w="%s" (.*?)></div>' % w, ch, re.S)
    attrs = m.group(1)
    r = subprocess.run(['node', 'kit/zta.js', 'widget', w, attrs, '--probe'], capture_output=True, text=True, encoding='utf-8')
    out = (r.stdout + r.stderr).strip().splitlines()
    print('==', cid, w, len(re.findall(r' ;; ', attrs)) + 1, 'items')
    print('\n'.join(out[-14:]))
