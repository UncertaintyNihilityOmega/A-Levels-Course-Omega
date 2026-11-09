# Runs the hist-timeline probe on the two P16 timelines (P16 builds no new widget; it uses the P1 timeline with its own data).
import re, subprocess, io

for cid in ['hist.int.1919.3', 'hist.int.1919.4']:
    ch = io.open('chapters/%s.md' % cid, encoding='utf-8').read()
    m = re.search(r'<div class="widget" data-w="hist-timeline" (.*?)></div>', ch, re.S)
    attrs = m.group(1)
    r = subprocess.run(['node', 'kit/zta.js', 'widget', 'hist-timeline', attrs, '--probe'], capture_output=True, text=True, encoding='utf-8')
    out = (r.stdout + r.stderr).strip().splitlines()
    print('==', cid, len(re.findall(r' ;; ', attrs)) + 1, 'events')
    print('\n'.join(out[-14:]))
