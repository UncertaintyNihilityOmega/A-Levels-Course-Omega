#!/usr/bin/env python3
"""Widget test harness.

Usage:
  python3 tools/wtest.py src/widgets-math.js 'graph|data-fns="x^2-4" data-x="-5,5" data-y="-5,10"' 'normal|data-mu="0"' ...
Options (env): WT_SUBJ=math (subject colour), WT_OUT=/path/prefix (default scratchpad/wtest)

Builds a test page with the real stylesheet + src/core.js + the given widget file(s), renders each widget,
then takes screenshots: <prefix>-desk-light.png (1000px) , <prefix>-phone-dark.png (390px), and prints any
console errors / exceptions. Look at the PNGs with your image-reading tool.
"""
import os, sys, html
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCR = os.environ.get('SCRATCH', __import__('tempfile').gettempdir())
os.makedirs(SCR, exist_ok=True)
args = sys.argv[1:]
jsfiles = [a for a in args if a.endswith('.js')]
specs = [a for a in args if not a.endswith('.js')]
subj = os.environ.get('WT_SUBJ', 'math')
prefix = os.environ.get('WT_OUT', os.path.join(SCR, 'wtest'))

css = open(os.path.join(ROOT, 'src/style.css')).read()
core = open(os.path.join(ROOT, 'src/core.js')).read()
wjs = '\n;\n'.join(open(os.path.join(ROOT, f) if not os.path.isabs(f) else f).read() for f in jsfiles)
items = []
for s in specs:
    name, _, attrs = s.partition('|')
    items.append(f'<h3>{html.escape(name)}</h3><div class="widget" data-w="{name}" {attrs}></div>')
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>[hidden]{{display:none!important}}body{{margin:0}}{css}</style></head><body>
<div class="app s-{subj}" id="app"><main class="main"><article class="chapter s-{subj}"><div class="prose">{''.join(items)}</div></article></main></div>
<script>{core}</script><script>{wjs}</script>
<script>
for (const el of document.querySelectorAll('.widget[data-w]')) {{
  const fn = W.reg[el.dataset.w];
  if (!fn) {{ console.error('NOT REGISTERED: ' + el.dataset.w); continue; }}
  try {{ fn(el, Object.assign({{}}, el.dataset)); }} catch (e) {{ console.error('INIT FAILED ' + el.dataset.w + ': ' + e.message + '\\n' + e.stack); }}
}}
</script></body></html>'''
path = prefix + '.html'
open(path, 'w').write(page)
with sync_playwright() as p:
    b = p.chromium.launch()
    for tag, w, h, scheme in (('desk-light', 1000, 900, 'light'), ('phone-dark', 390, 844, 'dark')):
        pg = b.new_page(viewport={'width': w, 'height': h}, color_scheme=scheme)
        msgs = []
        pg.on('console', lambda m: msgs.append(f'{m.type}: {m.text}') if m.type in ('error', 'warning') else None)
        pg.on('pageerror', lambda e: msgs.append(f'PAGEERROR: {e}'))
        pg.goto('file://' + path)
        pg.wait_for_timeout(600)
        out = f'{prefix}-{tag}.png'
        pg.screenshot(path=out, full_page=True)
        sw = pg.evaluate('document.documentElement.scrollWidth')
        print(f'{out}  (page width {sw}px for viewport {w}px{" — OVERFLOW!" if sw > w else ""})')
        for m in msgs[:20]: print('   ', m)
        pg.close()
    b.close()
print('test page:', path)
