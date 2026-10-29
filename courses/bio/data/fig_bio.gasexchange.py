# data/fig_bio.gasexchange.py: builds the hand-drawn SVG figures of chapters/bio.gasexchange.md and checks label clearance.
# Run: py data/fig_bio.gasexchange.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.gasexchange replaces the @@FIG_<NAME> placeholder lines of the chapter (and refreshes them later).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts, bez

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["AIRWAYS", "WALLS", "EPITH", "ALVEOLUS"]
figs, problems = [], []

EPI = "f2 s-acc2 sw2"
WALL = "fm s-acc sw2"
CART = "f1 s-acc sw2"
MUSC = "fa s-acc2 sw2"
LUM = "fp ln"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def ring(f, cx, cy, r0, r1, a0, a1, cls):
    outer = arc_pts(cx, cy, r1, r1, a0, a1, 36)
    inner = arc_pts(cx, cy, r0, r0, a1, a0, 36)
    f.poly(outer + inner, cls, True)


def pol(cx, cy, r, a):
    return (round(cx + r * math.cos(math.radians(a)), 1), round(cy + r * math.sin(math.radians(a)), 1))


# ---------- 1. the airway tree ----------
f = Fig("airways")
SX, SY, OXF, OYF = 0.75, 0.93, 212, 12
tf = lambda x, y: (round(OXF + (x - 170) * SX, 1), round(OYF + y * SY, 1))
T = lambda pts: [tf(x, y) for x, y in pts]
lungL = [(154, 80), (124, 64), (78, 84), (50, 150), (46, 250), (66, 298), (122, 304), (150, 292), (156, 170)]
lungR = [(340 - x, y) for x, y in lungL]
f.poly(T(lungL), WALL)
f.poly(T(lungR), WALL)
# trachea (hollow tube)
f.rect(tf(163, 24)[0], tf(163, 24)[1], 14 * SX, 80 * SY, LUM)
brL = [[(170, 104), (126, 140)], [(126, 140), (92, 186)], [(126, 140), (134, 196)], [(92, 186), (68, 232)],
       [(92, 186), (106, 234)], [(134, 196), (124, 238)], [(134, 196), (146, 236)]]
ends = [(68, 232), (106, 234), (124, 238), (146, 236)]
for seg in brL:
    cls = "ln thick" if seg[0] == (170, 104) or seg[0] == (126, 140) else "ln"
    for mirror in (False, True):
        pts = [((340 - x) if mirror else x, y) for x, y in seg]
        f.line(T(pts), cls)
clusters = []
for mirror in (False, True):
    for (x, y) in ends:
        xx = (340 - x) if mirror else x
        for dx, dy in [(-6, 5), (6, 5), (0, 13)]:
            cx, cy = tf(xx + dx, y + dy)
            f.circle(cx, cy, 5, "f2 s-acc2 sw2")
        clusters.append(tf(xx, y + 8))
LX, RX = 96, 322
def lab_left(y, s, target):
    f.text(LX, y, s, "tl", "end"); f.leader((LX + 4, y - 3), target)
def lab_right(y, s, target):
    f.text(RX, y, s, "tl"); f.leader((RX - 4, y - 3), target)
tx, ty = tf(163, 50)
lab_left(40, "trachea", (tx - 1, ty))
bx, by = tf(148, 122)
lab_left(120, "bronchus", (bx, by))
bx2, by2 = tf(80, 210)
lab_left(205, "bronchiole", (bx2, by2))
ax, ay = clusters[0]
lab_left(262, "alveoli", (ax - 3, ay + 1))
lx, ly = tf(300, 110)
lab_right(96, "lung", (lx, ly))
lab_right(150, "bronchus", tf(340 - 148, 122))
lab_right(226, "bronchiole", tf(340 - 80, 210))
lab_right(280, "alveoli", (clusters[4][0] + 3, clusters[4][1] + 1))
done(f, (400, 316),
     "The airway tree of the lungs. The trachea divides into two bronchi, one to each lung. Each bronchus divides into smaller "
     "bronchi and then into many bronchioles, and each bronchiole ends in a cluster of alveoli.",
     "The airways divide again and again, from the trachea to the alveoli. Each lung holds a very large number of alveoli, "
     "drawn here as only a few clusters. The airways are drawn thinner as they get narrower.")

# ---------- 2. plan diagrams of trachea and bronchus walls ----------
f = Fig("walls")
f.text(10, 16, "A  Trachea (TS)", "tl tb")
cx, cy = 92, 98
f.circle(cx, cy, 31, LUM)
ring(f, cx, cy, 31, 36, 0, 360, EPI)
ring(f, cx, cy, 36, 46, 0, 360, WALL)
ring(f, cx, cy, 46, 58, 118, 422, CART)          # C-shaped cartilage, open toward the bottom
ring(f, cx, cy, 46, 58, 62, 118, MUSC)           # smooth muscle bridges the gap
def lt(y, s, target, x=176):
    f.text(x, y, s)
    f.leader((x - 4, y - 3), target)
lt(44, "ciliated epithelium", pol(cx, cy, 33.5, -52))
f.text(176, 58, "with goblet cells")
lt(88, "submucosa with", pol(cx, cy, 41, -8))
f.text(176, 102, "mucous glands")
lt(132, "C-shaped cartilage", pol(cx, cy, 52, 28))
lt(162, "smooth muscle", pol(cx, cy, 52, 84))
lt(190, "lumen", pol(cx, cy, 10, 40)) if False else None
f.text(176, 24, "lumen"); f.leader((172, 21), pol(cx, cy, 8, -30))

f.text(10, 216, "B  Bronchus (TS)", "tl tb")
bx, by = 92, 302
f.circle(bx, by, 22, LUM)
ring(f, bx, by, 22, 26, 0, 360, EPI)
ring(f, bx, by, 26, 32, 0, 360, MUSC)
ring(f, bx, by, 32, 38, 0, 360, WALL)
for a0, a1 in [(8, 66), (100, 152), (184, 252), (282, 346)]:
    ring(f, bx, by, 38, 47, a0, a1, CART)
f.text(176, 246, "lumen"); f.leader((172, 243), pol(bx, by, 8, -20))
f.text(176, 276, "epithelium"); f.leader((172, 273), pol(bx, by, 24, -35))
f.text(176, 296, "smooth muscle")
f.leader((172, 293), pol(bx, by, 29, 5))
f.text(176, 326, "mucous glands")
f.leader((172, 323), pol(bx, by, 35, 35))
f.text(176, 352, "plates of cartilage"); f.text(176, 366, "(irregular)")
f.leader((172, 349), pol(bx, by, 42.5, 126))
done(f, (340, 386),
     "Plan diagrams of transverse sections. A, the trachea: a lumen lined by an epithelium of ciliated cells and goblet cells, a "
     "submucosa with mucous glands, a C-shaped ring of cartilage and smooth muscle across the gap in the C. B, a bronchus: a "
     "smaller lumen, the epithelium, a ring of smooth muscle, submucosa with mucous glands and separate irregular plates of "
     "cartilage outside them.",
     "Plan diagrams in transverse section (TS) show tissue layers only, with no cells. In the trachea the cartilage is a C-shape; in "
     "a bronchus it is irregular plates, and a ring of smooth muscle lies inside them. A bronchiole would have no cartilage at all.")

# ---------- 3. ciliated epithelium and goblet cells ----------
f = Fig("epith")
x0, W = 30, 36
base, top = 204, 152
f.rect(x0, 98, 5 * W, 26, WALL)                       # mucus layer
for i in range(5):
    xx = x0 + i * W
    f.rect(xx, top, W, base - top, "f1 s-acc sw2")
    if i != 2:
        for k in range(4):
            f.line([(xx + 6 + k * 8, top), (xx + 6 + k * 8, 118)], "ln-m thin", check=False)
        ellipse(f, xx + W / 2, 184, 9, 7, "f2 s-acc2 sw2")
    else:
        ellipse(f, xx + W / 2, 192, 9, 5, "f2 s-acc2 sw2")
        for (dx, dy) in [(-7, 163), (7, 163), (0, 174)]:
            f.circle(xx + W / 2 + dx, dy, 4, "fm2 s-acc sw2")
f.line([(x0, base + 6), (x0 + 5 * W, base + 6)], "ln thick")
for (px, py) in [(50, 108), (118, 112), (172, 106)]:
    f.circle(px, py, 3, "fi")
f.line([(x0 + 10, 80), (x0 + 5 * W - 10, 80)], "c3 sw2", "ah")
f.text(x0 + 2.5 * W, 68, "mucus moved towards the throat", "tl", "middle")
RXX = 226
def le(y, s, target, s2=None):
    f.text(RXX, y, s)
    if s2:
        f.text(RXX, y + 14, s2)
    f.leader((RXX - 4, y - 3), target)
le(112, "mucus", (x0 + 5 * W - 4, 112))
le(142, "cilia", (x0 + 5 * W - 28, 140))
le(168, "ciliated epithelial", (x0 + 5 * W - 3, 168), "cell")
le(206, "goblet cell", (x0 + 2 * W + 28, 176))
le(240, "basement membrane", (x0 + 5 * W - 6, base + 6))
f.text(x0 + 2, 244, "trapped dust and bacteria", "tl")
f.leader((x0 + 34, 233), (50, 111))
done(f, (400, 262),
     "Ciliated epithelium and goblet cells of the airway lining. Rows of ciliated columnar cells with hair-like cilia lie on a basement "
     "membrane, with a goblet cell among them. A layer of mucus above the cilia holds trapped dust and bacteria and is moved "
     "towards the throat.",
     "A drawing of the lining of the trachea. Goblet cells secrete mucus, which traps dust and bacteria; the cilia of the ciliated cells "
     "beat to sweep the mucus towards the throat. The drawing is not to scale.")

# ---------- 4. gas exchange across the alveolus wall ----------
f = Fig("alveolus")
ax0, ax1 = 20, 200
f.rect(ax0, 22, ax1 - ax0, 78, LUM)                    # air in the alveolus
f.rect(ax0, 100, ax1 - ax0, 7, CART)                   # squamous epithelium of the alveolus
f.line([(ax0, 109.5), (ax1, 109.5)], "ln thick")       # fused basement membranes
f.rect(ax0, 112, ax1 - ax0, 7, CART)                   # endothelium of the capillary
f.rect(ax0, 119, ax1 - ax0, 100, WALL)                 # blood plasma
ellipse(f, 100, 137, 40, 15, "fr ln")                  # red blood cell, squeezed against the wall as the caption says (REVIEW)
f.line([(116, 40), (116, 142)], "c1 sw2", "ah")        # O2 in
f.line([(158, 140), (158, 40)], "c2 sw2", "ah")        # CO2 out
f.text(124, 62, "O₂")
f.text(164, 62, "CO₂")
RXX = 214
def la(y, s, target, s2=None):
    f.text(RXX, y, s)
    if s2:
        f.text(RXX, y + 14, s2)
    f.leader((RXX - 4, y - 3), target)
la(44, "air in the", (ax1 - 8, 36), "alveolus")
la(84, "squamous epithelium", (ax1 - 10, 103.5))
f.text(RXX, 98, "of the alveolus")
la(124, "basement membrane", (ax1 - 24, 109.5))
la(152, "endothelium of the", (ax1 - 6, 115.5), "capillary wall")
la(196, "plasma", (ax1 - 12, 204))
la(226, "red blood cell", (128, 145))
done(f, (380, 246),
     "Gas exchange between an alveolus and a capillary. From the air in the alveolus to the blood, oxygen crosses a squamous epithelium "
     "of the alveolus, the basement membranes and the squamous endothelium of the capillary, then enters the plasma and a red blood "
     "cell. Carbon dioxide travels the other way.",
     "Oxygen (arrow down) and carbon dioxide (arrow up) diffuse across two very thin layers of squamous cells. The red blood cell is "
     "squeezed close to the wall, so the diffusion distance is very short. Not to scale: the layers are thinner than drawn.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
