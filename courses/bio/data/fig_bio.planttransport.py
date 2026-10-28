# data/fig_bio.planttransport.py: builds the hand-drawn SVG figures of chapters/bio.planttransport.md and checks label clearance.
# Run: py data/fig_bio.planttransport.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.planttransport replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["STEM", "ROOT", "LEAF", "XYLEM", "PHLOEM", "PATHWAYS", "TRANSP", "POTOM", "MARRAM"]
figs, problems = [], []


def pol(cx, cy, r, a):
    return (round(cx + r * math.cos(math.radians(a)), 1), round(cy + r * math.sin(math.radians(a)), 1))


def sector(cx, cy, r0, r1, a0, a1, n=8):
    return arc_pts(cx, cy, r1, r1, a0, a1, n) + arc_pts(cx, cy, r0, r0, a1, a0, n)


def rot(pts, cx, cy, ang):
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    return [(round(cx + (x - cx) * c - (y - cy) * s, 1), round(cy + (x - cx) * s + (y - cy) * c, 1)) for x, y in pts]


XY = "f2 s-acc2 sw2"     # xylem
PH = "f1 s-acc sw2"      # phloem
TISS = "fm s-acc sw2"    # ground tissue
PALE = "fp ln"

# ---------- 1. stem TS plan ----------
f = Fig("stem")
cx, cy, R = 200, 125, 88
ellipse(f, cx, cy, R, R, "fm s-acc sw3", check=False)                       # epidermis (thick outline) and cortex
ellipse(f, cx, cy, 30, 30, PALE, check=False)                                # pith
for k in range(8):
    a = 22.5 + 45 * k
    f.poly(sector(cx, cy, 36, 56, a - 9, a + 9), XY, check=False)             # xylem
    f.line(arc_pts(cx, cy, 57, 57, a - 11, a + 11, 8), "c3 sw2", check=False)  # cambium
    f.poly(sector(cx, cy, 58, 70, a - 11, a + 11), PH, check=False)           # phloem
LX, RX = 100, 300
f.text(LX, 52, "epidermis", anchor="end"); f.leader((LX + 4, 49), pol(cx, cy, R, 215))
f.text(LX, 129, "cortex", anchor="end"); f.leader((LX + 4, 126), (cx - 80, 126))
f.text(LX, 188, "pith", anchor="end"); f.leader((LX + 4, 185), pol(cx, cy, 14, 160))
f.text(RX, 60, "phloem"); f.leader((RX - 4, 57), pol(cx, cy, 65, -67.5))
f.text(RX, 112, "cambium"); f.leader((RX - 4, 109), pol(cx, cy, 57, -22.5))
f.text(RX, 152, "xylem"); f.leader((RX - 4, 149), pol(cx, cy, 46, 22.5))
f.text(RX, 200, "vascular", ); f.text(RX, 214, "bundle"); f.leader((RX - 4, 197), pol(cx, cy, 52, 67.5))
figs.append(f.svg((400, 232),
    "Plan diagram of a transverse section of a herbaceous dicotyledonous stem. An outer epidermis surrounds a wide cortex. "
    "Eight vascular bundles lie in a ring. In each bundle xylem is on the inside, phloem on the outside and a layer of cambium between them. "
    "The centre of the stem is pith.",
    "Plan diagram of a stem TS: tissue outlines only, no cells. The vascular bundles form a ring, with xylem towards the pith and phloem towards the epidermis."))
problems += f.check()

# ---------- 2. root TS plan ----------
f = Fig("root")
cx, cy, R = 200, 125, 80
ellipse(f, cx, cy, R, R, "fm s-acc sw3", check=False)                        # epidermis and cortex
for a in list(range(40, 141, 20)) + list(range(220, 321, 20)):                # root hairs
    f.line([pol(cx, cy, R, a), pol(cx, cy, R + 13, a)], "ln", check=False)
ellipse(f, cx, cy, 36, 36, "fp c3 sw3", check=False)                          # endodermis ring (pericycle inside)
ellipse(f, cx, cy, 31, 31, PALE, check=False)                                 # pericycle
cross = [(-6, -24), (6, -24), (6, -6), (24, -6), (24, 6), (6, 6), (6, 24), (-6, 24), (-6, 6), (-24, 6), (-24, -6), (-6, -6)]
f.poly(rot([(cx + x, cy + y) for x, y in cross], cx, cy, 45), XY, check=False)   # xylem: X shape
for a in (0, 90, 180, 270):
    ellipse(f, *pol(cx, cy, 19, a), 6, 6, PH, check=False)                    # phloem between the arms
LX, RX = 100, 296
f.text(LX, 44, "root hair", anchor="end"); f.leader((LX + 4, 41), pol(cx, cy, R + 10, 232))
f.text(LX, 100, "epidermis", anchor="end"); f.leader((LX + 4, 97), pol(cx, cy, R - 2, 200))
f.text(LX, 160, "cortex", anchor="end"); f.leader((LX + 4, 157), pol(cx, cy, 58, 170))
f.text(RX, 44, "endodermis"); f.leader((RX - 4, 41), pol(cx, cy, 36, -50))
f.text(RX, 92, "pericycle"); f.leader((RX - 4, 89), pol(cx, cy, 33, -20))
f.text(RX, 148, "xylem"); f.leader((RX - 4, 145), pol(cx, cy, 14, 45))
f.text(RX, 190, "phloem"); f.leader((RX - 4, 187), pol(cx, cy, 19, 0))
figs.append(f.svg((400, 232),
    "Plan diagram of a transverse section of a herbaceous dicotyledonous root. Root hairs project from the epidermis. A wide cortex surrounds a central ring of endodermis and pericycle. "
    "In the centre the xylem forms a cross shape, and there is a patch of phloem between each pair of arms.",
    "Plan diagram of a root TS. The xylem is in the centre as a star or cross, with phloem between its arms, all inside the endodermis. A stem has its xylem and phloem in a ring of bundles instead."))
problems += f.check()

# ---------- 3. leaf TS plan ----------
f = Fig("leaf")
x0, x1, ytop, ybot = 20, 262, 50, 118
f.rect(x0, ytop, x1 - x0, 5, "f2 s-acc2 sw2")                              # upper epidermis
f.rect(x0, 55, x1 - x0, 24, "f1 s-acc sw2")                                # palisade mesophyll
f.rect(x0, 79, 70, 34, TISS)                                              # spongy mesophyll left of midrib
f.rect(190, 79, x1 - 190, 34, TISS)                                       # spongy mesophyll right of midrib
hump = [(90, 79), (190, 79), (190, 113), (178, 160), (145, 186), (112, 160), (90, 113)]
f.poly(hump, TISS, check=False)
f.poly(arc_pts(140, 128, 24, 20, 180, 360, 10), XY, check=False)           # xylem on the upper side
f.poly(arc_pts(140, 128, 24, 20, 0, 180, 10), PH, check=False)             # phloem below
f.circle(226, 98, 7, "f2 s-acc2 sw2")                                     # small vein
low = [(x0, ybot), (90, ybot), (90, 113), (112, 160), (145, 186), (178, 160), (190, 113), (190, ybot), (x1, ybot)]
f.line([(90, 113), (112, 160), (145, 186), (178, 160), (190, 113)], "ln sw3", check=False)
f.rect(x0, 113, 70, 4, "f2 s-acc2 sw2")
f.rect(190, 113, 36, 4, "f2 s-acc2 sw2")
f.rect(236, 113, x1 - 236, 4, "f2 s-acc2 sw2")
RX = 272
f.text(RX, 52, "upper epidermis"); f.leader((RX - 4, 49), (250, 52))
f.text(RX, 67, "palisade mesophyll"); f.leader((RX - 4, 64), (250, 67))
f.text(RX, 84, "spongy mesophyll"); f.leader((RX - 4, 81), (250, 90))
f.text(RX, 102, "small vein"); f.leader((RX - 4, 99), (234, 99))
f.text(RX, 120, "lower epidermis"); f.leader((RX - 4, 117), (252, 116))
f.text(RX, 138, "stoma"); f.leader((RX - 4, 135), (232, 118))
f.text(206, 158, "xylem (upper side)"); f.leader((202, 155), (158, 120))
f.text(206, 176, "phloem (lower side)"); f.leader((202, 173), (158, 138))
f.text(206, 194, "midrib"); f.leader((202, 191), (170, 168))
figs.append(f.svg((400, 222),
    "Plan diagram of a transverse section of a dicotyledonous leaf. A thin upper epidermis lies above a layer of palisade mesophyll and a layer of spongy mesophyll, "
    "with a lower epidermis that has stomata. The midrib bulges downwards and holds a vascular bundle with xylem on the upper side and phloem below. A small vein lies in the spongy mesophyll.",
    "Plan diagram of a leaf TS through the midrib. The xylem is on the upper side of each vein and the phloem on the lower side. Stomata are mostly in the lower epidermis."))
problems += f.check()

# ---------- 4. xylem vessel elements (LS) ----------
f = Fig("xylem")
L0, L1, R0, R1 = 140, 148, 200, 208
top, mid, bot = 28, 128, 228
wall = "f1 s-acc sw2"
f.rect(L1, top, R0 - L1, bot - top, "f2 ln")
for (a, b) in [(top, 70), (82, mid - 4), (mid + 4, 172), (184, bot)]:
    f.rect(L0, a, 8, b - a, wall)
for (a, b) in [(top, 96), (108, mid - 4), (mid + 4, 190), (202, bot)]:
    f.rect(R0, a, 8, b - a, wall)
for yy in (top, mid - 4, bot - 8):                                        # remnants of the end walls
    pass
f.rect(L1, mid - 4, 6, 8, wall); f.rect(R0 - 6, mid - 4, 6, 8, wall)      # ledge: end wall broken down
f.line([(174, 218), (174, 40)], "c1 sw2", arrow="ah")
LX, RX = 128, 222
f.text(LX, 56, "lumen: no", anchor="end"); f.text(LX, 70, "cytoplasm", anchor="end"); f.leader((LX + 4, 52), (160, 56))
f.text(LX, 124, "end wall", anchor="end"); f.text(LX, 138, "broken down", anchor="end"); f.leader((LX + 4, 131), (L1 + 2, mid))
f.text(LX, 180, "pit", anchor="end"); f.leader((LX + 4, 177), (L0 + 2, 179))
f.text(RX, 52, "thick wall"); f.text(RX, 66, "with lignin"); f.leader((RX - 4, 56), (R1 - 2, 56))
f.text(RX, 102, "pit: no lignin,"); f.text(RX, 116, "water passes"); f.text(RX, 130, "sideways"); f.leader((RX - 4, 99), (R0 + 6, 102))
f.text(RX, 210, "water flows up"); f.leader((RX - 4, 207), (178, 206))
figs.append(f.svg((340, 248),
    "Longitudinal section of two xylem vessel elements joined end to end. The side walls are thick and contain lignin, with gaps called pits. "
    "The end wall between the two elements has broken down, leaving a continuous empty tube with no cytoplasm, through which water flows upwards.",
    "Xylem vessel elements in longitudinal section. Each element is a dead cell: lignified side walls, pits, no end walls and an empty lumen, so the elements form one continuous tube."))
problems += f.check()

# ---------- 5. phloem sieve tube element and companion cell (LS) ----------
f = Fig("phloem")
sx0, sx1 = 120, 170
f.rect(sx0, 24, 50, 100, "fm s-acc sw2")                                  # sieve tube element 1
f.rect(sx0, 132, 50, 100, "fm s-acc sw2")                                 # sieve tube element 2
f.rect(sx0, 124, 50, 8, "f1 s-acc sw2")                                   # sieve plate
for x in (128, 141, 154):
    f.rect(x, 125, 6, 6, "fp ln")                                         # pores in the plate
f.rect(sx1, 40, 46, 72, "f1 s-acc sw2")                                   # companion cell
ellipse(f, 193, 62, 11, 11, "f2 s-acc2 sw2", check=False)                 # nucleus
ellipse(f, 190, 98, 8, 5, "fok s-acc sw2", check=False)                   # mitochondria
ellipse(f, 204, 90, 6, 4, "fok s-acc sw2", check=False)
for y in (52, 76, 100):
    f.line([(sx1 - 4, y), (sx1 + 4, y)], "c3 sw2", check=False)           # plasmodesmata
LX, RX = 112, 228
f.text(LX, 60, "sieve tube", anchor="end"); f.text(LX, 74, "element", anchor="end"); f.leader((LX + 4, 66), (sx0 + 8, 66))
f.text(LX, 130, "sieve plate", anchor="end"); f.leader((LX + 4, 127), (sx0 + 6, 128))
f.text(LX, 184, "no nucleus,", anchor="end"); f.text(LX, 198, "few organelles", anchor="end"); f.leader((LX + 4, 191), (sx0 + 10, 191))
f.text(RX, 44, "companion cell"); f.leader((RX - 4, 41), (sx1 + 44, 46))
f.text(RX, 70, "nucleus"); f.leader((RX - 4, 67), (205, 65))
f.text(RX, 98, "mitochondria"); f.leader((RX - 4, 95), (210, 93))
f.text(176, 146, "plasmodesmata"); f.leader((186, 132), (sx1 + 2, 104))
figs.append(f.svg((340, 250),
    "Longitudinal section of two sieve tube elements joined end to end by a sieve plate with pores, and a companion cell beside the upper element. "
    "The sieve tube element has no nucleus and few organelles. The companion cell has a nucleus and many mitochondria and is joined to the sieve tube element by plasmodesmata.",
    "A sieve tube element and its companion cell in longitudinal section. The sieve tube element is a living cell with almost empty cytoplasm; the companion cell runs its metabolism."))
problems += f.check()

# ---------- 6. apoplast and symplast pathways across the root ----------
f = Fig("pathways")
f.rect(36, 14, 112, 30, "f2 s-acc2 sw2")                                  # soil water
f.rect(36, 60, 112, 204, "fm ln sw3")                                     # cell wall material
f.rect(66, 40, 40, 24, "f1 s-acc sw2")                                    # root hair
for (a, b) in [(64, 110), (118, 158), (166, 206), (214, 256)]:
    f.rect(44, a, 88, b - a, "f1 s-acc sw2")                              # cells
f.rect(36, 268, 112, 50, "f2 s-acc2 sw3")                                 # xylem vessel
f.rect(52, 278, 80, 30, "fp ln")
f.rect(132, 212, 16, 46, "fi")                                            # Casparian strip
f.line([(140, 70), (140, 198)], "c2 dash sw2", arrow="ah")                # apoplast
f.line([(88, 50), (88, 300)], "c1 sw2", arrow="ah")                       # symplast
f.line([(136, 202), (120, 226)], "c2 sw2", arrow="ah")                    # apoplast water forced into the cytoplasm
for yy in (112, 160, 208, 258):
    for xx in (62, 114):
        f.line([(xx, yy - 3), (xx, yy + 5)], "ln sw3", check=False)       # plasmodesmata
RX = 164
f.text(RX, 32, "soil water"); f.leader((RX - 4, 29), (150, 29))
f.text(RX, 78, "root hair cell"); f.leader((RX - 4, 75), (128, 78))
f.line([(RX, 108), (192, 108)], "c2 dash sw2", arrow="ah"); f.text(198, 112, "apoplast: walls")
f.line([(RX, 130), (192, 130)], "c1 sw2", arrow="ah"); f.text(198, 134, "symplast: cytoplasm")
f.text(RX, 176, "cortex cells"); f.leader((RX - 4, 173), (128, 180))
f.text(RX, 226, "Casparian strip"); f.text(RX, 240, "(suberin) blocks"); f.text(RX, 254, "the apoplast"); f.leader((RX - 4, 223), (150, 230))
f.text(RX, 286, "endodermis cell"); f.leader((RX - 4, 283), (128, 244))
f.text(RX, 312, "xylem vessel"); f.leader((RX - 4, 309), (150, 300))
figs.append(f.svg((340, 328),
    "Pathways of water across a root from the soil water to a xylem vessel. A dashed arrow runs down the cell walls of root hair and cortex cells (apoplast pathway) and stops at the Casparian strip in the endodermis, "
    "which is waterproof. A solid arrow runs through the cytoplasm of the cells, passing through plasmodesmata (symplast pathway) to the xylem. "
    "Where the apoplast pathway is blocked, a solid arrow shows water entering the cytoplasm of the endodermis cell.",
    "Water crosses the root by two pathways. The apoplast pathway (dashed) runs through cell walls without crossing a membrane, until the Casparian strip blocks it; the symplast pathway (solid) runs through cytoplasm. "
    "All water must cross the cell surface membrane of an endodermis cell to reach the xylem."))
problems += f.check()

# ---------- 7. transpiration in the leaf ----------
f = Fig("transp")
f.rect(18, 14, 24, 150, "f2 s-acc2 sw2")                                  # xylem in a vein
for (ex, ey, rx, ry) in [(104, 56, 36, 26), (184, 66, 34, 26), (134, 122, 36, 26)]:
    ellipse(f, ex, ey, rx, ry, "f1 s-acc sw2", check=False)               # mesophyll cells
f.rect(30, 196, 98, 30, "f1 s-acc sw2")                                   # lower epidermis cells
f.rect(212, 196, 98, 30, "f1 s-acc sw2")
ellipse(f, 146, 211, 14, 16, "f2 s-acc2 sw2", check=False)                # guard cells
ellipse(f, 194, 211, 14, 16, "f2 s-acc2 sw2", check=False)
f.line([(30, 228), (160, 228)], "ln sw3", check=False)
f.line([(180, 228), (310, 228)], "ln sw3", check=False)
f.line([(44, 90), (68, 74)], "c1 sw2", arrow="ah")                          # water from xylem to cell walls
f.line([(162, 108), (178, 114)], "c3 sw2", arrow="ah")                    # evaporation from the wall into the air space
f.line([(176, 130), (170, 186), (170, 250)], "c3 dash sw2", arrow="ah")   # vapour diffuses out
RX = 238
f.text(RX, 38, "mesophyll cell"); f.leader((RX - 4, 35), (216, 54))
f.text(RX, 98, "air space"); f.leader((RX - 4, 95), (210, 118))
f.text(RX, 150, "stoma"); f.leader((RX - 4, 147), (176, 206))
f.text(RX, 172, "guard cell"); f.leader((RX - 4, 169), (206, 207))
f.text(60, 12, "xylem", "tl")
f.text(186, 246, "air outside has"); f.text(186, 260, "lower water potential")
f.text(10, 284, "1 water leaves the xylem", "ts")
f.text(10, 298, "2 evaporates from wet cell wall", "ts")
f.text(10, 312, "3 vapour diffuses through air spaces and stoma", "ts")
figs.append(f.svg((340, 322),
    "Part of a leaf in section. A xylem vessel in a vein supplies water to mesophyll cells. Water evaporates from the wet cell walls of the mesophyll cells into the air spaces. "
    "The water vapour diffuses through the air spaces and out through a stoma between two guard cells into the air outside.",
    "Transpiration: water evaporates from the surfaces of the mesophyll cell walls into the air spaces, then water vapour diffuses out through the stomata down a water potential gradient."))
problems += f.check()

# ---------- 8. potometer ----------
f = Fig("potometer")
f.rect(34, 130, 32, 60, "fp ln")                                          # tube holding the shoot
f.rect(36, 160, 28, 28, "f2 s-acc2 sw2")                                  # water at the base of the shoot tube
f.line([(50, 126), (50, 44)], "c1 sw3", check=False)                      # stem
ellipse(f, 33, 66, 16, 7, "f1 s-acc sw2", check=False)
ellipse(f, 67, 52, 16, 7, "f1 s-acc sw2", check=False)
ellipse(f, 36, 96, 14, 6, "f1 s-acc sw2", check=False)
f.rect(40, 122, 20, 10, "fi")                                             # bung
f.rect(66, 170, 210, 18, "fp ln")                                         # capillary tube
f.rect(68, 172, 90, 14, "f2 s-acc2 sw2")
f.rect(190, 172, 84, 14, "f2 s-acc2 sw2")
ellipse(f, 174, 179, 14, 5, "fp ln", check=False)                         # air bubble
f.rect(250, 140, 60, 56, "fp ln")                                         # beaker of water
f.rect(252, 160, 56, 34, "f2 s-acc2 sw2")
f.rect(110, 196, 130, 12, "fm s-acc sw2")                                 # scale
for xx in range(116, 240, 10):
    f.line([(xx, 196), (xx, 202)], "ln thin", check=False)
f.text(90, 28, "leafy shoot"); f.leader((86, 25), (72, 47))
f.text(76, 118, "bung (airtight)")
f.leader((74, 126), (62, 128)) if False else None
f.text(190, 156, "air bubble", anchor="end"); f.leader((194, 159), (180, 174))
f.text(110, 226, "capillary tube with scale")
f.text(256, 108, "beaker"); f.text(256, 122, "of water")
figs.append(f.svg((340, 238),
    "Potometer. A leafy shoot is held by an airtight bung in a tube of water. The tube joins a horizontal capillary tube with a scale, which has an air bubble in it and dips into a beaker of water. "
    "As the shoot takes up water, the bubble moves along the scale.",
    "A potometer. The distance the air bubble moves along the scale in a measured time is the volume of water taken up by the shoot divided by the cross-sectional area of the capillary."))
problems += f.check()

# ---------- 9. marram grass leaf TS ----------
f = Fig("marram")
cx, cy, Ro = 200, 128, 86
a0, a1 = -65, 245                                                         # leaf rolled: gap at the top
outer = arc_pts(cx, cy, Ro, Ro, a0, a1, 40)
inner = []
n = 10
for k in range(2 * n + 1):
    a = a1 - (a1 - a0) * k / (2 * n)
    r = 28 if k % 2 == 0 else 44                                          # ridges (small r) and grooves (large r)
    inner.append(pol(cx, cy, r, a))
f.poly(outer + inner, "f1 s-acc sw2", check=False)                        # leaf tissue as a C-shaped ring
f.line(outer, "ln sw3", check=False)                                      # thick waxy cuticle on the outside
for k in range(0, 2 * n + 1, 2):                                          # hairs on the ridge tips, and bundles below
    a = a1 - (a1 - a0) * k / (2 * n)
    if 0 < k < 2 * n:
        f.line([pol(cx, cy, 28, a), pol(cx, cy, 15, a)], "ln thin", check=False)
        f.circle(*pol(cx, cy, 58, a), 6, "f2 s-acc2 sw2")
for k in range(1, 2 * n, 2):                                              # stomata at the groove bottoms
    a = a1 - (a1 - a0) * k / (2 * n)
    f.circle(*pol(cx, cy, 44, a), 3, "fp ln")
LX, RX = 106, 294
f.text(LX, 70, "thick waxy", anchor="end"); f.text(LX, 84, "cuticle on the", anchor="end"); f.text(LX, 98, "outer surface", anchor="end")
f.leader((LX + 4, 81), pol(cx, cy, Ro, 218))
f.text(LX, 140, "vascular", anchor="end"); f.text(LX, 154, "bundle", anchor="end"); f.leader((LX + 4, 137), pol(cx, cy, 58, 183))
f.text(LX, 190, "mesophyll", anchor="end"); f.leader((LX + 4, 187), pol(cx, cy, 72, 140))
f.text(RX, 56, "hairs"); f.leader((RX - 4, 53), pol(cx, cy, 21, -34))
f.text(RX, 108, "sunken stomata"); f.text(RX, 122, "in grooves"); f.leader((RX - 4, 105), pol(cx, cy, 44, -18.5))
f.text(RX, 184, "rolled leaf"); f.text(RX, 198, "traps humid"); f.text(RX, 212, "air"); f.leader((RX - 4, 181), pol(cx, cy, 6, 40))
figs.append(f.svg((400, 232),
    "Transverse section of a rolled marram grass leaf. A thick waxy cuticle covers the outer surface. The leaf is rolled so that the inner surface, which has grooves containing sunken stomata and hairs, faces a central space of trapped humid air that opens to the outside only through a narrow slit. "
    "Vascular bundles lie in the mesophyll beneath the ridges.",
    "Annotated drawing of a marram grass leaf TS: the rolled shape, hairs and sunken stomata trap moist air next to the stomata, which reduces the water potential gradient and so the loss of water vapour."))
problems += f.check()

print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
