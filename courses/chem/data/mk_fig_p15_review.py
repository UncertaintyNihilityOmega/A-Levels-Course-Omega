# Specialist REVIEW (P15): redrawn optical-isomer figure (chem.complexes #6) and chelate figure (chem.transition #3).
# Run: py data/mk_fig_p15_review.py  -> writes scratch/p15_optical.svg.txt and scratch/p15_chelate.svg.txt
import math, os

def f(v):
    s = ('%.1f' % v).rstrip('0').rstrip('.')
    return '0' if s == '-0' else s

# ---------------------------------------------------------------- optical isomers
POS = {'U': (0, -56), 'D': (0, 56), 'L': (-56, 0), 'R': (56, 0), 'F': (-30, 32), 'B': (30, -32)}

def label_half(s):
    return 4.5 if s == 'N' else 13.0          # half width of the label text

def bond(out, cx, cy, key, lab, mir):
    dx, dy = POS[key]
    if mir: dx = -dx
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    s0 = 11 if abs(ux) < 0.2 else (14 if abs(uy) < 0.2 else 12)          # clear of the Ni label
    hw = label_half(lab)
    e = L - (9 if abs(ux) < 0.5 else hw + 5)                               # stop short of the ligand label
    x0, y0, x1, y1 = cx + ux * s0, cy + uy * s0, cx + ux * e, cy + uy * e
    if key == 'F':                                                         # wedge towards the reader
        px, py = -uy, ux
        out.append('<path class="fi" d="M%s %sL%s %sL%s %sZ"/>' % (f(x0), f(y0), f(x1 + px * 3.5), f(y1 + py * 3.5), f(x1 - px * 3.5), f(y1 - py * 3.5)))
    elif key == 'B':                                                       # hashed bond away from the reader
        px, py = -uy, ux; d = []
        for i in range(6):
            t = i / 5.0; x = x0 + (x1 - x0) * t; y = y0 + (y1 - y0) * t; h = 1.0 + 2.6 * t
            d.append('M%s %sL%s %s' % (f(x + px * h), f(y + py * h), f(x - px * h), f(y - py * h)))
        out.append('<path class="ln" d="%s"/>' % ''.join(d))
    else:
        out.append('<path class="ln" d="M%s %sL%s %s"/>' % (f(x0), f(y0), f(x1), f(y1)))
    out.append('<text class="tl tc" x="%s" y="%s">%s</text>' % (f(cx + dx), f(cy + dy + 4.5), lab))

def en_arc(out, cx, cy, a, b, mir):
    ax, ay = POS[a]; bx, by = POS[b]
    if mir: ax, bx = -ax, -bx
    mx, my = (ax + bx) / 2, (ay + by) / 2
    m = math.hypot(mx, my); ux, uy = mx / m, my / m
    chord = math.hypot(bx - ax, by - ay)
    k = 0.42 * chord + 6
    qx, qy = mx + ux * k, my + uy * k
    def start(px, py):                       # leave the N label towards the control point
        vx, vy = qx - px, qy - py; v = math.hypot(vx, vy)
        return px + vx / v * 10, py + vy / v * 10
    sx, sy = start(ax, ay); ex, ey = start(bx, by)
    out.append('<path class="ln thick" d="M%s %sQ%s %s %s %s"/>' % (f(cx + sx), f(cy + sy), f(cx + qx), f(cy + qy), f(cx + ex), f(cy + ey)))

def panel(out, cx, cy, pairs, waters, mir):
    out.append('<text class="tl tc" x="%s" y="%s">Ni</text>' % (f(cx), f(cy + 4.5)))
    for a, b in pairs:
        bond(out, cx, cy, a, 'N', mir); bond(out, cx, cy, b, 'N', mir); en_arc(out, cx, cy, a, b, mir)
    for w in waters:
        bond(out, cx, cy, w, 'H₂O', mir)

def fig_optical():
    out = []
    TRIS = [('U', 'B'), ('L', 'F'), ('R', 'D')]
    rows = [(92, TRIS, [], '[Ni(en)₃]²⁺'), (302, [('L', 'F'), ('R', 'D')], ['U', 'B'], 'cis-[Ni(en)₂(H₂O)₂]²⁺')]
    for cy, pairs, waters, name in rows:
        panel(out, 82, cy, pairs, waters, False)
        panel(out, 258, cy, pairs, waters, True)
        out.append('<path class="ln-m thin dash" d="M170 %sV%s"/>' % (f(cy - 78), f(cy + 70)))
        out.append('<text class="tl tc" x="170" y="%s">mirror</text>' % f(cy + 88))
        out.append('<text class="tl tc" x="82" y="%s">%s</text>' % (f(cy + 112), name))
        out.append('<text class="tl tc" x="258" y="%s">%s</text>' % (f(cy + 112), name))
    return ('<svg viewBox="0 0 340 430" role="img" aria-label="Two pairs of mirror-image complexes either side of a dashed mirror line. '
            'Top: the two optical isomers of the nickel complex with three 1,2-diaminoethane ligands; each ligand is a curved line joining two '
            'nitrogen atoms bonded to nickel. Bottom: the two optical isomers of the cis nickel complex with two 1,2-diaminoethane ligands and '
            'two water ligands">' + ''.join(out) + '</svg>')

# ---------------------------------------------------------------- chelate figure (en and ethanedioate)
def fig_chelate():
    o = []
    # en
    o.append('<text class="tl tc" x="85" y="39.5">M</text><text class="tl tc" x="50" y="93.5">H₂N</text><text class="tl tc" x="120" y="93.5">NH₂</text>')
    o.append('<path class="ln thick" d="M77.5 47.5L57.5 78.5"/><path class="ln thick" d="M92.5 47.5L112.5 78.5"/>')
    o.append('<path class="ln thick" d="M54.4 102.1L66 134"/><path class="ln thick" d="M115.6 102.1L104 134"/><path class="ln thick" d="M66 134L104 134"/>')
    o.append('<text class="tl tc" x="85" y="196">en</text><text class="tl tc" x="85" y="213">H₂NCH₂CH₂NH₂</text>')
    # ethanedioate: ring O-C-C-O, each C carries a C=O drawn straight down (two parallel lines 5 px apart)
    o.append('<text class="tl tc" x="255" y="39.5">M</text><text class="tl tc" x="222" y="93.5">O</text><text class="tl tc" x="288" y="93.5">O</text>')
    o.append('<path class="ln thick" d="M247.9 47.6L229.1 78.4"/><path class="ln thick" d="M262.1 47.6L280.9 78.4"/>')
    o.append('<path class="ln thick" d="M225.9 102.2L236 134"/><path class="ln thick" d="M284.1 102.2L274 134"/><path class="ln thick" d="M236 134L274 134"/>')
    for x in (236, 274):
        o.append('<path class="ln thick" d="M%s 134V161M%s 136V161"/>' % (f(x - 2.5), f(x + 2.5)))
        o.append('<text class="tl tc" x="%s" y="178">O</text>' % f(x))
    o.append('<text class="tl tc" x="255" y="200">ethanedioate</text><text class="tl tc" x="255" y="217">C₂O₄²⁻</text>')
    return ('<svg viewBox="0 15 340 212" role="img" aria-label="Two bidentate ligands on a metal ion M: 1,2-diaminoethane bonded through two '
            'nitrogen atoms, and the ethanedioate ion bonded through two oxygen atoms, each forming a five-membered ring with the metal; each '
            'carbon of the ethanedioate ion also carries a doubly bonded oxygen">' + ''.join(o) + '</svg>')

os.makedirs('scratch', exist_ok=True)
open('scratch/p15_optical.svg.txt', 'w', encoding='utf-8').write(fig_optical())
open('scratch/p15_chelate.svg.txt', 'w', encoding='utf-8').write(fig_chelate())
print('ok')
