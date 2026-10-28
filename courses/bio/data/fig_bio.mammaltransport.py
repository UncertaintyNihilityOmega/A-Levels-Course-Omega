# data/fig_bio.mammaltransport.py: builds the hand-drawn SVG figures of chapters/bio.mammaltransport.md and checks label clearance.
# Run: py data/fig_bio.mammaltransport.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.mammaltransport replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts, bez

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["DOUBLE", "VESSELS", "VESSELS_LS", "CELLS", "CAPBED"]
figs, problems = [], []

OX = "c1 sw2"            # oxygenated blood (arrow class)
DE = "c2 sw2"            # deoxygenated blood (arrow class)
WALL = "fm s-acc sw2"
MID = "f1 s-acc sw2"
LUM = "fp ln"
NUC = "f2 s-acc2 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


# ---------- 1. double circulation (flow diagram) ----------
f = Fig("double")
f.rect(105, 12, 130, 34, WALL, 6); f.text(170, 34, "lungs", "tl tb", "middle")
f.rect(105, 284, 130, 34, WALL, 6); f.text(170, 306, "body tissues", "tl tb", "middle")
cx_l, cx_r = 68, 272
for (cx, y0, nm1, nm2, cls) in [(cx_l, 100, "right", "ventricle", MID), (cx_l, 200, "right", "atrium", MID),
                                (cx_r, 100, "left", "atrium", MID), (cx_r, 200, "left", "ventricle", MID)]:
    f.rect(cx - 40, y0, 80, 50, cls, 6)
    f.text(cx, y0 + 21, nm1, "tl", "middle"); f.text(cx, y0 + 36, nm2, "tl", "middle")
# deoxygenated: body -> RA -> RV -> lungs
f.line([(105, 301), (cx_l, 301), (cx_l, 254)], DE, "ah")
f.line([(cx_l, 198), (cx_l, 154)], DE, "ah")
f.line([(cx_l, 98), (cx_l, 29), (103, 29)], DE, "ah")
# oxygenated: lungs -> LA -> LV -> body
f.line([(237, 29), (cx_r, 29), (cx_r, 96)], OX, "ah")
f.line([(cx_r, 154), (cx_r, 198)], OX, "ah")
f.line([(cx_r, 254), (cx_r, 301), (237, 301)], OX, "ah")
# vessel names
f.text(cx_l + 10, 276, "vena cava", "tl tb")
f.text(cx_l + 10, 64, "pulmonary", "tl tb"); f.text(cx_l + 10, 78, "artery", "tl tb")
f.text(cx_r - 10, 64, "pulmonary", "tl tb", "end"); f.text(cx_r - 10, 78, "vein", "tl tb", "end")
f.text(cx_r - 10, 276, "aorta", "tl tb", "end")
# legend
f.line([(125, 160), (150, 160)], DE, "ah"); f.text(158, 164, "deoxygenated", "tl")
f.line([(125, 186), (150, 186)], OX, "ah"); f.text(158, 190, "oxygenated", "tl")
done(f, (340, 330),
     "Flow diagram of the double circulation. Deoxygenated blood flows from the body tissues along the vena cava to the right atrium, then the right ventricle, then along the pulmonary artery to the lungs. Oxygenated blood flows from the lungs along the pulmonary vein to the left atrium, then the left ventricle, then along the aorta to the body tissues. The blood passes through the heart twice in each circuit of the body.",
     "The double circulation drawn as a flow diagram: the chambers are in the order the blood meets them, not in their real positions. Follow the arrows: body, right atrium, right ventricle, lungs, left atrium, left ventricle, body. The blood passes through the heart twice per circuit.")

# ---------- 2. TS plan diagrams: artery, vein, capillary ----------
f = Fig("vessels")
LX = 196                      # label column
# A artery
f.text(10, 16, "A  Artery (TS)", "tl tb")
cx, cy = 92, 92
ellipse(f, cx, cy, 58, 58, WALL, check=False)
ellipse(f, cx, cy, 42, 42, MID, check=False)
ellipse(f, cx, cy, 21, 21, LUM, check=False)
f.text(LX, 42, "tunica externa", "tl"); f.text(LX, 56, "(collagen)", "tl")
f.leader((LX - 4, 45), (cx + 50, cy - 29))
f.text(LX, 88, "tunica media", "tl"); f.text(LX, 102, "(smooth muscle,", "tl"); f.text(LX, 116, "elastic fibres)", "tl")
f.leader((LX - 4, 90), (cx + 32, cy - 6))
f.text(LX, 148, "lumen", "tl"); f.leader((LX - 4, 145), (cx + 6, cy + 8))
f.text(LX, 164, "endothelium: single", "tl"); f.text(LX, 178, "layer of flat cells", "tl")
f.leader((LX - 4, 161), (cx + 15, cy + 15))
# B vein
f.text(10, 214, "B  Vein (TS)", "tl tb")
cx, cy = 92, 292
ellipse(f, cx, cy, 62, 50, WALL, check=False)
ellipse(f, cx, cy, 54, 42, MID, check=False)
ellipse(f, cx, cy, 48, 36, LUM, check=False)
f.text(LX, 262, "thin tunica externa", "tl"); f.leader((LX - 4, 265), (cx + 46, cy - 29))
f.text(LX, 286, "thin tunica media", "tl"); f.leader((LX - 4, 289), (cx + 53, cy - 4))
f.text(LX, 314, "wide lumen", "tl"); f.leader((LX - 4, 311), (cx + 18, cy + 8))
# C capillary
f.text(10, 372, "C  Capillary (TS)", "tl tb")
cx, cy = 92, 414
ellipse(f, cx, cy, 24, 24, WALL, check=False)
ellipse(f, cx, cy, 17, 17, LUM, check=False)
f.parts.append(f'<ellipse class="fr ln" cx="{cx}" cy="{cy}" rx="11" ry="6"/>')
f.text(LX, 394, "wall: one cell", "tl"); f.text(LX, 408, "thick (endothelium)", "tl")
f.leader((LX - 4, 397), (cx + 20, cy - 12))
f.text(LX, 434, "red blood cell", "tl"); f.leader((LX - 4, 431), (cx + 8, cy + 3))
f.text(LX, 450, "lumen about 7 µm", "tl"); f.leader((LX - 4, 447), (cx + 12, cy + 12))
done(f, (340, 470),
     "Three plan diagrams of blood vessels in transverse section. A, artery: a thick wall made of tunica externa with collagen, a thick tunica media of smooth muscle and elastic fibres, and a narrow round lumen lined by endothelium. B, vein: a thin wall with thin tunica externa and tunica media, and a wide lumen. C, capillary: a wall one endothelium cell thick and a lumen about 7 micrometres across holding one red blood cell.",
     "Plan diagrams in transverse section (TS). They show the tissue layers only, with no individual cells. The capillary is drawn far bigger than its true size compared with the artery and vein, so that its wall can be seen.")

# ---------- 3. LS: artery and vein with a pocket valve ----------
f = Fig("vessels_ls")
LX = 214
f.text(10, 16, "A  Artery (LS)", "tl tb")
x0, x1 = 20, 200
top = 30
f.rect(x0, top, x1 - x0, 12, WALL)                    # externa
f.rect(x0, top + 12, x1 - x0, 24, MID)                # media
f.rect(x0, top + 36, x1 - x0, 40, LUM)                # lumen
f.rect(x0, top + 76, x1 - x0, 24, MID)
f.rect(x0, top + 100, x1 - x0, 12, WALL)
f.text(LX, 44, "tunica externa", "tl"); f.leader((LX - 4, 41), (150, top + 6))
f.text(LX, 70, "tunica media", "tl"); f.text(LX, 84, "(thick)", "tl"); f.leader((LX - 4, 67), (150, top + 24))
f.text(LX, 110, "lumen", "tl"); f.leader((LX - 4, 107), (150, top + 56))
f.line([(40, top + 66), (110, top + 66)], "c1 sw2", "ah")
f.text(40, top + 54, "blood flow", "tl")
# B vein with valve
f.text(10, 176, "B  Vein (LS)", "tl tb")
vt = 194
f.rect(x0, vt, x1 - x0, 5, WALL)
f.rect(x0, vt + 5, x1 - x0, 4, MID)
f.rect(x0, vt + 9, x1 - x0, 62, LUM)
f.rect(x0, vt + 71, x1 - x0, 4, MID)
f.rect(x0, vt + 75, x1 - x0, 5, WALL)
# pocket valve: two flaps pointing along the flow (to the right)
f.poly([(96, vt + 9), (126, vt + 9), (136, vt + 34), (128, vt + 36)], MID)
f.poly([(96, vt + 71), (126, vt + 71), (136, vt + 46), (128, vt + 44)], MID)
f.text(LX, vt + 14, "thin wall", "tl"); f.leader((LX - 4, vt + 11), (160, vt + 3))
f.text(LX, vt + 44, "pocket valve", "tl"); f.leader((LX - 4, vt + 41), (138, vt + 40))
f.text(LX, vt + 76, "wide lumen", "tl"); f.leader((LX - 4, vt + 73), (170, vt + 56))
f.line([(28, vt + 40), (80, vt + 40)], "c2 sw2", "ah")
f.text(24, vt + 28, "blood flow", "tl")
done(f, (330, 300),
     "Two longitudinal sections. A, an artery: two parallel thick walls, each with a tunica externa and a thick tunica media, with the lumen between them. B, a vein: two parallel thin walls and a wide lumen containing a pocket valve, a pair of flaps pointing in the direction of blood flow towards the heart.",
     "Longitudinal sections (LS), cut along the vessel. The artery wall is thick and the lumen narrow. The vein wall is thin, the lumen wide, and a pocket valve lets blood pass towards the heart but fills and closes if the blood starts to flow backwards.")


# ---------- 4. blood cells (same scale: 1 µm = 5 px) ----------
def bean(cx, cy, R, ang, dent=0.38, n=48):
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / n
        d = (t - ang + math.pi) % (2 * math.pi) - math.pi
        r = R * (1 - dent * math.exp(-(d / 0.7) ** 2))
        pts.append((round(cx + r * math.cos(t), 1), round(cy + r * math.sin(t), 1)))
    return pts


f = Fig("cells")
PX = 5
cells = [(85, 62, "red blood cell", ["no nucleus;", "biconcave disc"]),
         (250, 62, "neutrophil", ["lobed nucleus,", "granular cytoplasm"]),
         (85, 208, "monocyte", ["kidney-shaped", "nucleus; largest cell"]),
         (250, 208, "lymphocyte", ["round nucleus fills", "most of the cell"])]
for cx, cy, nm, lines in cells:
    ty = cy + 54
    f.text(cx, ty, nm, "tl tb", "middle")
    for i, s in enumerate(lines):
        f.text(cx, ty + 15 * (i + 1), s, "tl", "middle")
# red cell 7 µm
r = 3.5 * PX
ellipse(f, 85, 62, r, r, WALL)
ellipse(f, 85, 62, r * 0.45, r * 0.45, LUM, check=False)
# neutrophil 11 µm, three-lobed nucleus
ellipse(f, 250, 62, 5.5 * PX, 5.5 * PX, WALL)
for dx, dy in [(-13, 5), (0, -7), (13, 5)]:
    ellipse(f, 250 + dx, 62 + dy, 8, 8, NUC, check=False)
f.line([(237, 67), (250, 55), (263, 67)], "c2 sw3", check=False)
# monocyte 16 µm, kidney-shaped nucleus
ellipse(f, 85, 208, 8 * PX, 8 * PX, WALL)
f.poly(bean(88, 208, 22, math.radians(200)), NUC, check=False)
# lymphocyte 9 µm, round nucleus filling most of the cell
ellipse(f, 250, 208, 4.5 * PX, 4.5 * PX, WALL)
ellipse(f, 250, 208, 18, 18, NUC, check=False)
# scale bar
f.line([(20, 320), (70, 320)], "ln thick")
f.line([(20, 315), (20, 325)], "ln"); f.line([(70, 315), (70, 325)], "ln")
f.text(80, 324, "10 µm", "tl")
done(f, (340, 336),
     "Drawings of four blood cells at the same scale. Red blood cell: about 7 micrometres across, no nucleus, a pale centre because it is a biconcave disc. Neutrophil: about 11 micrometres, nucleus with three connected lobes, granular cytoplasm. Monocyte: the largest, about 16 micrometres, with a large kidney-shaped nucleus. Lymphocyte: about 9 micrometres, with a round nucleus filling most of the cell.",
     "Blood cells drawn as they look in a stained film, at one scale. These are drawings: in a real photomicrograph the nuclei stain darkest and the red blood cells are pink or red. Look at the nucleus first.")

# ---------- 5. capillary bed with pressure arrows ----------
f = Fig("capbed")
cy = 128
top_y, bot_y = cy - 22, cy + 22
# arteriole (left) tapering into the capillary, venule (right)
f.poly([(20, cy - 42), (120, top_y), (120, bot_y), (20, cy + 42)], MID, closed=False, check=True)
f.poly([(540, cy - 42), (440, top_y), (440, bot_y), (540, cy + 42)], MID, closed=False, check=True)
# capillary walls with gaps
gaps = [150, 200, 250, 350, 400]
def wall(y):
    xs = [120] + [g for g in gaps for g in (g - 5, g + 5)] + [440]
    for a, b in zip(xs[::2], xs[1::2]):
        f.line([(a, y), (b, y)], "c1 sw3", check=True)
wall(top_y); wall(bot_y)
# tissue cells above and below
f.rect(215, 28, 150, 44, WALL, 10)
f.rect(215, cy + 56, 150, 44, WALL, 10)
f.text(290, 55, "tissue cell", "tl", "middle")
f.text(290, cy + 83, "tissue cell", "tl", "middle")
# red cells and proteins in the lumen
for x in (140, 215, 330, 410):
    f.parts.append(f'<ellipse class="fr ln" cx="{x}" cy="{cy}" rx="10" ry="6"/>')
for x, y in [(160, cy - 8), (180, cy + 9), (240, cy - 10), (262, cy + 8), (290, cy - 4), (310, cy + 10), (365, cy - 8), (385, cy + 8), (430, cy - 8)]:
    f.parts.append(f'<circle class="fi" cx="{x}" cy="{y}" r="2.5"/>')
# fluid out at the arterial end (arrow out through gaps)
f.line([(150, top_y - 4), (150, 52)], "c3 sw2", "ah")
f.line([(200, top_y - 4), (200, 52)], "c3 sw2", "ah")
f.line([(150, bot_y + 4), (150, cy + 76)], "c3 sw2", "ah")
f.line([(200, bot_y + 4), (200, cy + 76)], "c3 sw2", "ah")
# water back in at the venous end
f.line([(350, 52), (350, top_y - 4)], "c4 sw2", "ah")
f.line([(400, 52), (400, top_y - 4)], "c4 sw2", "ah")
f.line([(350, cy + 76), (350, bot_y + 4)], "c4 sw2", "ah")
f.line([(400, cy + 76), (400, bot_y + 4)], "c4 sw2", "ah")
# along the top: pressure falls
f.line([(130, 22), (430, 22)], "ln-m thin dash", "ah")
f.text(280, 12, "hydrostatic pressure falls along the capillary", "tl", "middle")
# labels
f.text(20, 52, "arteriole", "tl"); f.text(540, 52, "venule", "tl", "end")
f.text(20, cy + 62, "high pressure:", "tl"); f.text(20, cy + 76, "fluid forced out", "tl")
f.text(540, cy + 62, "lower pressure;", "tl", "end"); f.text(540, cy + 76, "water in by osmosis", "tl", "end")
f.text(20, 228, "blood flow →", "tl")
f.text(20, 250, "red blood cell", "tl"); f.parts.append(f'<ellipse class="fr ln" cx="125" cy="246" rx="10" ry="6"/>')
f.text(160, 250, "plasma protein", "tl"); f.parts.append('<circle class="fi" cx="267" cy="246" r="2.5"/>')
f.text(283, 250, "gap between endothelium cells", "tl")
done(f, (560, 262),
     "A capillary bed. Blood flows from an arteriole on the left, through a capillary with gaps in its wall, to a venule on the right. At the arterial end, arrows show fluid forced out through the gaps into the tissue fluid around two tissue cells by high hydrostatic pressure. At the venous end, arrows show water returning into the capillary by osmosis. Red blood cells and plasma proteins stay inside the capillary.",
     "Tissue fluid. Outward arrows: fluid is forced out at the arterial end by hydrostatic pressure. Inward arrows: water returns by osmosis at the venous end because the plasma proteins lower the water potential of the plasma. Red blood cells and proteins stay in the capillary. Excess tissue fluid drains into lymph vessels.",
     "fig")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
