import sys, math, json
sys.path.insert(0, 'data')
from fig import Fig

out = {}

# ---------- G1: chain isomers C4H10 ----------
f = Fig()
pts = [(30, 60), (65, 40), (100, 60), (135, 40)]
for i, (x, y) in enumerate(pts):
    f.atom('b%d' % i, x, y)
for i in range(3):
    f.bond('b%d' % i, 'b%d' % (i + 1))
f.atom('m0', 200, 60); f.atom('m1', 235, 40); f.atom('m2', 270, 60); f.atom('m3', 235, 6)
f.bond('m0', 'm1'); f.bond('m1', 'm2'); f.bond('m1', 'm3')
f.free_text(82, 95, 'butane', 'tl tc'); f.free_text(235, 95, '2-methylpropane', 'tl tc')
vb = (0, 0, 300, 105)
print('G1', f.check(vb=vb))
out['G1'] = f.svg(vb, 'Skeletal formulas of butane, a four-carbon chain, and 2-methylpropane, a three-carbon chain with a methyl branch; both are C4H10',
                  'Two chain isomers of C₄H₁₀. Both have four carbon atoms, but one has a branch.')

# ---------- G2: cis / trans but-2-ene ----------
f = Fig()
def butene(f, tag, x0, cis):
    c2 = (x0, 70); c3 = (x0 + 40, 70)
    f.atom(tag + 'c2', *c2); f.atom(tag + 'c3', *c3)
    f.bond(tag + 'c2', tag + 'c3', 2)
    dx, dy = 17.5, 30.3
    # on C2: methyl up-left, H down-left
    f.atom(tag + 'm1', c2[0] - dx, c2[1] - dy)
    f.atom(tag + 'h1', c2[0] - dx, c2[1] + dy, 'H'); f.label(c2[0] - dx, c2[1] + dy, 'H')
    f.bond(tag + 'c2', tag + 'm1'); f.bond(tag + 'c2', tag + 'h1')
    if cis:
        f.atom(tag + 'm2', c3[0] + dx, c3[1] - dy)
        f.atom(tag + 'h2', c3[0] + dx, c3[1] + dy, 'H'); f.label(c3[0] + dx, c3[1] + dy, 'H')
    else:
        f.atom(tag + 'm2', c3[0] + dx, c3[1] + dy)
        f.atom(tag + 'h2', c3[0] + dx, c3[1] - dy, 'H'); f.label(c3[0] + dx, c3[1] - dy, 'H')
    f.bond(tag + 'c3', tag + 'm2'); f.bond(tag + 'c3', tag + 'h2')
butene(f, 'c', 70, True); butene(f, 't', 220, False)
f.free_text(90, 140, 'cis-but-2-ene', 'tl tc'); f.free_text(240, 140, 'trans-but-2-ene', 'tl tc')
vb = (0, 25, 330, 130)
print('G2', f.check(vb=vb))
out['G2'] = f.svg(vb, 'Skeletal formulas of cis-but-2-ene, with both methyl groups on the same side of the double bond, and trans-but-2-ene, with the methyl groups on opposite sides',
                  'In cis-but-2-ene the two CH₃ groups are on the same side of the C=C; in trans-but-2-ene they are on opposite sides. The H atoms on the double-bond carbons are drawn so you can see the groups.')

# ---------- G3: cis / trans 1,2-dimethylcyclohexane ----------
f = Fig()
def ring(f, tag, cx, cy, R, hashed2):
    P = []
    for k in range(6):
        a = math.radians(-90 + 60 * k)
        P.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    for i, (x, y) in enumerate(P):
        f.atom(tag + str(i), x, y)
    for i in range(6):
        f.bond(tag + str(i), tag + str((i + 1) % 6))
    # methyls on vertex 0 (top) and vertex 1 (upper right)
    for i, hashed in ((0, False), (1, hashed2)):
        x, y = P[i]
        ux, uy = (x - cx) / R, (y - cy) / R
        L = 30
        f.atom(tag + 'm%d' % i, x + ux * L, y + uy * L)
        f.wedge(tag + str(i), tag + 'm%d' % i, w=8, hashed=hashed)
ring(f, 'a', 80, 90, 36, False)
ring(f, 'b', 250, 90, 36, True)
f.free_text(80, 148, 'cis', 'tl tc'); f.free_text(250, 148, 'trans', 'tl tc')
vb = (0, 8, 330, 150)
print('G3', f.check(vb=vb))
out['G3'] = f.svg(vb, 'Skeletal formulas of cis-1,2-dimethylcyclohexane, with both methyl groups drawn on wedge bonds, and trans-1,2-dimethylcyclohexane, with one wedge and one hashed bond',
                  'A wedge bond points towards you and a hashed bond points away. In the cis isomer both methyl groups are on the same face of the ring; in the trans isomer they are on opposite faces. The ring stops them swapping places.')

# ---------- G4: enantiomers of butan-2-ol ----------
f = Fig()
def enant(f, tag, cx, cy, mirror):
    s = -1 if mirror else 1
    f.atom(tag + 'C', cx, cy, 'C*'); f.label(cx, cy, 'C*')
    ul = (cx - s * 24, cy - 30); ur = (cx + s * 24, cy - 30)
    wd = (cx + s * 34, cy + 24); hs = (cx - s * 34, cy + 24)
    # in-plane: CH3 at up-left (unmirrored), C2H5 at up-right
    f.atom(tag + 'a', *ul, 'CH₃'); f.label(*ul, 'CH₃')
    f.atom(tag + 'b', *ur, 'C₂H₅'); f.label(*ur, 'C₂H₅')
    f.atom(tag + 'w', *wd, 'OH'); f.label(*wd, 'OH')
    f.atom(tag + 'h', *hs, 'H'); f.label(*hs, 'H')
    f.bond(tag + 'C', tag + 'a', cls='ln thick'); f.bond(tag + 'C', tag + 'b', cls='ln thick')
    f.wedge(tag + 'C', tag + 'w', w=8); f.wedge(tag + 'C', tag + 'h', w=8, hashed=True)
enant(f, 'p', 80, 78, False); enant(f, 'q', 250, 78, True)
f.raw('<path class="ln-m thin dash" d="M165 24V128"/>')
f.free_text(165, 16, 'mirror', 'tl tc ta')
f.free_text(80, 150, 'enantiomer 1', 'tl tc'); f.free_text(250, 150, 'enantiomer 2', 'tl tc')
vb = (0, 0, 330, 160)
print('G4', f.check(vb=vb))
out['G4'] = f.svg(vb, 'The two enantiomers of butan-2-ol drawn as mirror images across a dashed mirror line, each with a chiral carbon bonded to CH3, C2H5, OH and H, using a wedge and a hashed bond',
                  'The two enantiomers of butan-2-ol. The carbon marked * is the chiral centre. The wedge comes out of the page and the hashed bond goes behind it. The right-hand molecule is the mirror image of the left, and no rotation can make it match.')

# ---------- G5: polarimeter ----------
f = Fig()
y = 60
f.raw('<circle class="fa s-acc sw2" cx="20" cy="60" r="9"/>')
f.raw('<rect class="fm ln" x="68" y="34" width="8" height="52" rx="2"/>')
f.raw('<rect class="fa ln" x="118" y="40" width="80" height="40" rx="3"/>')
f.raw('<rect class="fm ln" x="240" y="34" width="8" height="52" rx="2"/>')
f.raw('<circle class="fm2 ln" cx="312" cy="60" r="9"/>')
f.raw('<path class="ln-m thin dash" d="M29 60H64"/><path class="ln-m thin dash" d="M80 60H114"/><path class="ln-m thin dash" d="M202 60H236"/><path class="ln-m thin dash" d="M252 60H300"/>')
f.raw('<path class="c1 sw2" d="M97 60V42" marker-end="url(#ahs-red)"/><path class="c1 sw2" d="M97 60V78" marker-end="url(#ahs-red)"/>')
t = math.radians(30)
ex, ey = 18 * math.sin(t), 18 * math.cos(t)
f.raw('<path class="c1 sw2" d="M220 60L%s %s" marker-end="url(#ahs-red)"/><path class="c1 sw2" d="M220 60L%s %s" marker-end="url(#ahs-red)"/>' % (f.f(220 + ex), f.f(60 - ey), f.f(220 - ex), f.f(60 + ey)))
for x, s_ in ((20, 'lamp'), (72, 'polariser'), (158, 'sample'), (244, 'analyser'), (312, 'detector')):
    f.free_text(x, 104, s_, 'tl tc')
f.free_text(97, 24, 'plane', 'tl tc ta'); f.free_text(220, 24, 'turned by α', 'tl tc ta')
vb = (0, 10, 355, 105)
print('G5', f.check(vb=vb))
out['G5'] = f.svg(vb, 'Polarimeter: a lamp, a polariser, a tube containing the sample, an analyser and a detector; the plane of the polarised light is turned by an angle alpha in the sample tube',
                  'A polarimeter. The polariser lets through light that vibrates in one plane only. An optically active sample turns that plane by an angle α, and the analyser is rotated to find the new plane.')
json.dump(out, open('scratch/iso_figs.json', 'w', encoding='utf-8'), ensure_ascii=False)
for k, v in out.items():
    print('=====', k); print(v)
