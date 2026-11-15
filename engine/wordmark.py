# wordmark.py: designs for a top-bar wordmark "Zero to A* Ω" (white wood for "Zero to A", crimson wood for "* Ω").
# Writes a page of options to choose from; the header itself is not changed (shell.html still has the name as text).
# Letters are outlines from the fonts in engine/fonts (SIL Open Font License), so the page needs no font files.
# Run: py engine/wordmark.py <out.html>   (needs fonttools and brotli; the build does not run it)
#      py engine/wordmark.py <out.html> <folder>   options A–F instead, in the storybook fonts found in <folder>
#      (MysteryQuest-Regular.ttf, Griffy-Regular.ttf, HennyPenny-Regular.ttf: SIL Open Font License, from
#      github.com/google/fonts; they have no Ω, so Ω is the logo's Caudex Ω from logo-glyphs.json)
import json, math, os, sys
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, wght):
    f = instantiateVariableFont(TTFont(os.path.join(HERE, 'fonts', name + '.woff2')), {'wght': wght})
    return f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm
FONTS = {'i': load('literata-italic', 700), 'u': load('literata', 700), 's': load('atkinson-next', 800)}
GL = json.load(open(os.path.join(HERE, 'logo-glyphs.json'), encoding='utf-8'))
EXTRA = {'m': ('MysteryQuest-Regular', 'Mystery Quest'), 'g': ('Griffy-Regular', 'Griffy'), 'h': ('HennyPenny-Regular', 'Henny Penny')}
def load_extra(folder):
    for k, (name, _) in EXTRA.items():
        f = TTFont(os.path.join(folder, name + '.ttf'))
        FONTS[k] = (f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm)
def cap_height(fk):
    """height of a capital Z as a part of the font size"""
    gs, cmap, upm = FONTS[fk]
    bp = BoundsPen(gs); gs[cmap[ord('Z')]].draw(bp)
    return bp.bounds[3] / upm
OMEGA_H = max(y for poly in GL['O']['polys'] for x, y in poly) / GL['upm']
BASE, H = 31.0, 42

def lay(letters, x=3.0):
    """letters: (char, font, size, tilt°, lift, gap after, group 'a' | 'b') -> paths [(group, d)], width, spans"""
    paths, spans = [], {'a': [1e9, -1e9], 'b': [1e9, -1e9]}
    for ch, fk, size, tilt, lift, gap, grp in letters:
        gs, cmap, upm = FONTS[fk]
        logo = ord(ch) not in cmap     # Ω in a font without Greek: the logo's Ω
        if logo: upm = GL['upm']
        g = None if logo else gs[cmap[ord(ch)]]
        s = size / upm
        adv = (GL['O']['adv'] if logo else g.width) * s
        # the letter's place, tilt and size go into its coordinates, so outlines keep one width
        t = Transform().translate(x, BASE - lift).translate(adv / 2, -size * 0.3).rotate(math.radians(tilt)).translate(-adv / 2, size * 0.3).scale(s, -s)
        if logo:
            d = ''.join('M' + 'L'.join('%.2f %.2f' % t.transformPoint(pt) for pt in poly) + 'Z' for poly in GL['O']['polys'])
        else:
            pen = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
            g.draw(TransformPen(pen, t))
            d = pen.getCommands()
        paths.append((grp, d))
        spans[grp][0] = min(spans[grp][0], x); spans[grp][1] = max(spans[grp][1], x + adv)
        x += adv + gap
    return paths, math.ceil(x + 3), spans

def spiral(cx, cy, r0, r1, a0, turns, n=60):
    pts = []
    for j in range(n + 1):
        t = j / n
        a, r = a0 + turns * 2 * math.pi * t, r0 + (r1 - r0) * t
        pts.append('%.1f %.1f' % (cx + r * math.cos(a), cy + r * math.sin(a)))
    return 'M' + 'L'.join(pts)

def wood(pid, seed, fx, fy):
    """a filter that lays wood grain (stretched noise in the colour --g) over whatever it is applied to"""
    return ('<filter id="%s" x="-5%%" y="-20%%" width="110%%" height="140%%" color-interpolation-filters="sRGB">'
            '<feTurbulence type="fractalNoise" baseFrequency="%g %g" numOctaves="3" seed="%d"/>'
            '<feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.5 0 0 0 -0.62" result="n"/>'
            '<feFlood style="flood-color:var(--g)"/><feComposite in2="n" operator="in"/><feComposite in2="SourceAlpha" operator="in" result="gr"/>'
            '<feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="gr"/></feMerge></filter>') % (pid, fx, fy, seed)

def letters_svg(k, letters, extra=lambda spans, w: ('', ''), grain=(0.035, 0.55), cls='wm'):
    paths, w, spans = lay(letters)
    ids = ['w%dp%d' % (k, i) for i in range(len(paths))]
    defs = ''.join('<path id="%s" d="%s"/>' % (ids[i], d) for i, (grp, d) in enumerate(paths))
    use = lambda g: ''.join('<use href="#%s"/>' % ids[i] for i, p in enumerate(paths) if p[0] == g)
    under, over = extra(spans, w)
    return ('<svg class="%s" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" aria-hidden="true">'
            '<defs>%s%s%s</defs>%s'
            '<g class="wa"><g class="ol">%s</g><g class="fl" filter="url(#w%dfa)">%s</g></g>'
            '<g class="wb"><g class="ol">%s</g><g class="fl" filter="url(#w%dfb)">%s</g></g>%s</svg>') % (
        cls, w, H, defs, wood('w%dfa' % k, 3 + k, *grain), wood('w%dfb' % k, 11 + k, *grain), under,
        use('a'), k, use('a'), use('b'), k, use('b'), over)

def curls(spans, w):
    a0, a1 = spans['a']; b1 = spans['b'][1]
    d = spiral(a0 + 1.5, 5.5, 0.4, 3.6, 0.5, 1.6) + ' ' + spiral(b1 + 2.2, 33, 3.8, 0.4, math.pi, 1.7)
    d += ' M%.1f 36.5C%.1f 40.5 %.1f 33.5 %.1f 37.5S%.1f 40 %.1f 36.8' % (a0 + 2, a0 + (a1 - a0) * .3, a0 + (a1 - a0) * .55, a1 - 8, b1 - 6, b1 + 2.2 - 3.8)
    return '', '<path class="curl" d="%s"/>' % d

def plank(k):
    """two sawn boards: the name is cut into them"""
    la = [('Z', 'u', 27, 0, 0, .3, 'a'), ('e', 'u', 24, 0, 0, .2, 'a'), ('r', 'u', 24, 0, 0, .2, 'a'), ('o', 'u', 24, 0, 0, 5, 'a'),
          ('t', 'i', 20, 0, 1, .2, 'a'), ('o', 'i', 20, 0, 1, 5, 'a'), ('A', 'u', 29, 0, 0, 11, 'a'),
          ('*', 'u', 30, 0, -5, 2, 'b'), ('Ω', 'u', 28, 0, 0, 0, 'b')]
    paths, w, spans = lay(la, 7.0)
    w += 4
    t = lambda g: ''.join('<path d="%s"/>' % d for grp, d in paths if grp == g)
    (a0, a1), (b0, b1) = spans['a'], spans['b']
    return ('<svg class="wm" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" aria-hidden="true"><defs>%s%s</defs>'
            '<g transform="rotate(-2 %.1f 21)"><rect class="pa" filter="url(#w%dfa)" x="%.1f" y="6" width="%.1f" height="31" rx="3.5"/><g class="ia">%s</g></g>'
            '<g transform="rotate(3 %.1f 21)"><rect class="pb" filter="url(#w%dfb)" x="%.1f" y="6" width="%.1f" height="31" rx="3.5"/><g class="ib">%s</g></g></svg>') % (
        w, H, wood('w%dfa' % k, 5, 0.03, 0.5), wood('w%dfb' % k, 9, 0.03, 0.5),
        (a0 + a1) / 2, k, a0 - 5, a1 - a0 + 10, t('a'), (b0 + b1) / 2, k, b0 - 5, b1 - b0 + 10, t('b'))

O = 'Ω'
OPTIONS = [
    ('1', 'Tumbling', 'Slanted storybook letters that bounce along the line, each a little tilted.',
     lambda k: letters_svg(k, [('Z', 'i', 33, -7, 0, .2, 'a'), ('e', 'i', 26, 5, .6, 0, 'a'), ('r', 'i', 26, -4, -.6, -.3, 'a'), ('o', 'i', 26, 6, 1, 6, 'a'),
                               ('t', 'i', 21, -6, 5, 0, 'a'), ('o', 'i', 21, 5, 6, 5.5, 'a'), ('A', 'i', 35, 4, 0, 2.2, 'a'),
                               ('*', 'i', 34, 0, -5.5, 2.4, 'b'), (O, 'i', 33, -5, 0, 0, 'b')])),
    ('2', 'Storybook', 'Upright book letters with a large Z and A, like the first line of a chapter. The calmest of the playful ones.',
     lambda k: letters_svg(k, [('Z', 'u', 36, 0, 0, .4, 'a'), ('e', 'u', 25, 2, .4, .2, 'a'), ('r', 'u', 25, -2, -.3, .1, 'a'), ('o', 'u', 25, 2, .5, 6, 'a'),
                               ('t', 'i', 19, -3, 7, .2, 'a'), ('o', 'i', 19, 3, 7.5, 5.5, 'a'), ('A', 'u', 36, 0, 0, 3, 'a'),
                               ('*', 'u', 34, 0, -6, 2.6, 'b'), (O, 'u', 34, 0, 0, 0, 'b')])),
    ('3', 'Topsy-turvy', 'The most "Wonderland": slanted and upright letters mixed, big jumps in size and tilt. The least calm.',
     lambda k: letters_svg(k, [('Z', 'i', 36, -12, 0, .6, 'a'), ('e', 'u', 23, 9, 2, .3, 'a'), ('r', 'i', 28, -7, -1, .2, 'a'), ('o', 'u', 21, 11, 3.5, 6, 'a'),
                               ('t', 'i', 21, -11, 7, .4, 'a'), ('o', 'u', 17, 13, 10, 5.5, 'a'), ('A', 'i', 38, 8, 0, 3, 'a'),
                               ('*', 'u', 37, 14, -6.5, 3, 'b'), (O, 'u', 33, -9, 0, 0, 'b')])),
    ('4', 'Curls', 'Slanted letters, nearly level, with a curl at each end and a ribbon under the name.',
     lambda k: letters_svg(k, [('Z', 'i', 32, -3, 1.5, .3, 'a'), ('e', 'i', 25, 2, 1.8, .1, 'a'), ('r', 'i', 25, -2, 1.5, -.2, 'a'), ('o', 'i', 25, 2, 1.8, 5.5, 'a'),
                               ('t', 'i', 20, -3, 5.5, .1, 'a'), ('o', 'i', 20, 3, 6, 5, 'a'), ('A', 'i', 33, 2, 1.5, 2.4, 'a'),
                               ('*', 'i', 33, 0, -4, 2.4, 'b'), (O, 'i', 31, -3, 1.5, 0, 'b')], curls)),
    ('5', 'Two boards', 'A white board and a crimson board, a little crooked, with the name cut into them. Shows the wood most clearly.', plank),
    ('6', 'Plain and clear', 'The same letters as the rest of the site, level, with only the wood colours and grain. The easiest to read.',
     lambda k: letters_svg(k, [('Z', 's', 29, 0, 0, .3, 'a'), ('e', 's', 29, 0, 0, .3, 'a'), ('r', 's', 29, 0, 0, .3, 'a'), ('o', 's', 29, 0, 0, 7, 'a'),
                               ('t', 's', 29, 0, 0, .3, 'a'), ('o', 's', 29, 0, 0, 7, 'a'), ('A', 's', 29, 0, 0, 2.5, 'a'),
                               ('*', 's', 33, 0, -3, 2.5, 'b'), (O, 's', 29, 0, 0, 0, 'b')])),
]

def storybook(fk, small_caps):
    """big capitals 25 units high; small capitals (or the font's own small letters) after them, a little uneven"""
    ch = cap_height(fk)
    B, S, T, OM = 25 / ch, 18.5 / ch, 15.5 / ch, 25 / OMEGA_H
    if small_caps:
        L = [('Z', fk, B, -3, 0, .5, 'a'), ('E', fk, S, 3, .5, .4, 'a'), ('R', fk, S, -2, -.3, .4, 'a'), ('O', fk, S, 3, .6, 8, 'a'),
             ('T', fk, T, -4, .2, .6, 'a'), ('O', fk, T, 4, .8, 8.5, 'a'), ('A', fk, B, 2, 0, 4.5, 'a')]
    else:
        L = [('Z', fk, B, -3, 0, .3, 'a'), ('e', fk, B, 3, .4, .2, 'a'), ('r', fk, B, -2, -.3, .2, 'a'), ('o', fk, B, 3, .5, 8, 'a'),
             ('t', fk, B * .86, -4, .3, .4, 'a'), ('o', fk, B * .86, 4, .8, 8.5, 'a'), ('A', fk, B, 2, 0, 4.5, 'a')]
    L += [('*', fk, B * 1.15, 8, -4, 3, 'b'), ('Ω', fk, OM, -3, 0, 0, 'b')]
    return lambda k: letters_svg(k, L, cls='wm fat')   # these fonts are thin: the letters get a little weight
def extra_options():
    out = []
    for n, (fk, sc) in enumerate([('m', True), ('m', False), ('g', True), ('g', False), ('h', True), ('h', False)]):
        name = EXTRA[fk][1]
        out.append(('ABCDEF'[n], name + (', small capitals' if sc else ', capitals and small letters'),
                    ('Large Z and A with smaller capitals between them, as in your sample.' if sc else 'The same font with its own small letters.')
                    + ' The Ω is the one from the logo: this font has none.', storybook(fk, sc)))
    return out

LOGO = '<svg viewBox="0 0 100 100" width="34" height="34"><circle cx="50" cy="50" r="50" fill="#123220"/><circle cx="50" cy="50" r="43.5" fill="#fff"/><text x="50" y="66" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="42" fill="#1E4D2B">AΩ</text></svg>'
CSS = '''
body{margin:0;font:16px/1.5 "Segoe UI",system-ui,sans-serif;background:#EEF1F3;color:#1B2430}
main{max-width:900px;margin:0 auto;padding:20px 16px 60px}
h1{font-size:1.5rem;margin:.2em 0}h2{font-size:1.15rem;margin:0}p{margin:.3em 0 .8em;color:#485363}
.opt{background:#fff;border:1px solid #D8DDE3;border-radius:12px;padding:16px;margin:18px 0}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:10px}@media(max-width:640px){.pair{grid-template-columns:1fr}}
.bar{display:flex;align-items:center;gap:10px;height:60px;padding:0 18px;border:1px solid #D8DDE3;border-radius:8px;margin-bottom:10px}
.bar .wm{height:38px}.big{padding:14px 18px;border-radius:8px;border:1px solid #D8DDE3}.big .wm{height:auto;width:100%;max-height:150px}
.wm{display:block;overflow:visible}
.light{background:#fff;--af:#FFFDF6;--ao:#123220;--g:#7FA08A;--bf:#C8102E;--bo:#5E0A18;--ia:#1E4D2B;--ib:#FFF4E6}
.dark{background:#19231F;border-color:#2F3E39;--af:#FFFDF6;--ao:#0A120F;--g:#7FA08A;--bf:#D8243F;--bo:#FF9A9A;--ia:#1E4D2B;--ib:#FFF4E6}
.pair>div{min-width:0}
.wa .ol{fill:var(--ao);stroke:var(--ao);stroke-width:1.5;stroke-linejoin:round}.wa .fl{fill:var(--af)}
.wb .ol{fill:var(--bo);stroke:var(--bo);stroke-width:1.5;stroke-linejoin:round}.wb .fl{fill:var(--bf);--g:#7A0D20}

.fat .wa .fl{stroke:var(--af);stroke-width:.75;stroke-linejoin:round}.fat .wb .fl{stroke:var(--bf);stroke-width:.75;stroke-linejoin:round}.fat .ol{stroke-width:2.5}
.curl{fill:none;stroke:var(--bf);stroke-width:1.1;stroke-linecap:round}
.pa{fill:var(--af);stroke:var(--ao);stroke-width:1.1}.pb{fill:var(--bf);stroke:var(--bo);stroke-width:1.1;--g:#7A0D20}
.ia{fill:var(--ia)}.ib{fill:var(--ib)}
'''
def page():
    out = ['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Wordmark options</title><style>%s</style><main>' % CSS,
           '<h1>Wordmark options for "Zero to A* Ω"</h1><p>Each option is shown at its real size in the top bar (paper and chalkboard mode), then enlarged. Tell the Organizer the number you like; say also what to change (more or less tilt, stronger or softer grain, other colours).</p>']
    k = 0
    for num, name, note, make in OPTIONS:
        a = []
        for cls in ('light', 'dark'):
            k += 1
            a.append('<div><div class="bar %s">%s%s</div><div class="big %s">%s</div></div>' % (cls, LOGO, make(k), cls, make(k + 50)))
        out.append('<section class="opt"><h2>%s. %s</h2><p>%s</p><div class="pair">%s</div></section>' % (num, name, note, ''.join(a)))
    return ''.join(out) + '</main></html>'

if __name__ == '__main__':
    dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '.run', 'wordmark-options.html')
    if len(sys.argv) > 2:
        load_extra(sys.argv[2])
        OPTIONS = extra_options()
    html = page()
    open(dest, 'w', encoding='utf-8', newline='').write(html)
    print('%d options, %d KB -> %s' % (len(OPTIONS), len(html) // 1024, os.path.normpath(dest)))
