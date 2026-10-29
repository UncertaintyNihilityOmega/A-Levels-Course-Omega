# data/fig_bio.homeostasis.py: builds the hand-drawn SVG figures of chapters/bio.homeostasis.md and checks label clearance.
# Run: py data/fig_bio.homeostasis.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.homeostasis replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, arc_pts, ellipse, bez

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["LOOP", "KIDNEY", "NEPHRON", "FILTER", "PCT", "ADH"]
figs, problems = [], []
BOX = "f1 s-acc sw2"
ARR = "c1 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def tube(f, pts, w, cls="fp ln"):
    """A tube of width w along a polyline: a closed polygon of the two offset sides."""
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]
        b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy)
        nx, ny = -dy / n, dx / n
        left.append((round(x + nx * w / 2, 1), round(y + ny * w / 2, 1)))
        right.append((round(x - nx * w / 2, 1), round(y - ny * w / 2, 1)))
    f.poly(left + right[::-1], cls, True, check=False)


# ---------- 1. control loop ----------
f = Fig("loop")
labels = [("stimulus", "a factor rises or falls"), ("receptor", "detects the change"),
          ("coordination system", "nervous or endocrine"), ("effector", "a muscle or a gland"),
          ("response", "reverses the change")]
for i, (a, b) in enumerate(labels):
    y = 10 + i * 72
    f.rect(50, y, 190, 44, BOX)
    f.text(145, y + 20, a, "tl tb", "middle")
    f.text(145, y + 36, b, "tl", "middle")
    if i < 4:
        f.line([(145, y + 44), (145, y + 72)], ARR, "ah")
f.line([(240, 320), (318, 320), (318, 32), (244, 32)], "c2 sw2", "ah")
f.text(252, 168, "negative", "tl tb")
f.text(252, 184, "feedback", "tl tb")
done(f, (340, 366),
     "A control loop with five boxes joined by downward arrows: stimulus (a factor rises or falls), receptor (detects the change), coordination system (nervous or endocrine), effector (a muscle or a gland) and response (reverses the change). An arrow from the response goes back up to the stimulus and is labelled negative feedback.",
     "The control loop of homeostasis. The response reverses the change that started the loop, so the factor returns to its set point: negative feedback.")

# ---------- 2. kidney in section ----------
f = Fig("kidney")
cx, cy, rx, ry = 170, 172, 92, 135


def outer(deg, scale=1.0, nscale=1.0):
    t = math.radians(deg)
    notch = 55 * nscale * math.exp(-(((deg - 180 + 180) % 360 - 180) / 35) ** 2)
    return (round(cx + rx * scale * math.cos(t) + notch, 1), round(cy + ry * scale * math.sin(t), 1))


pts = [outer(d) for d in range(0, 360, 6)]
f.poly(pts, "f1 ln sw3", True, check=True)
inner = lambda d: outer(d, 0.72, 0.5)
P = (150, 172)
cols = [-52, 0, 52]
for c in cols:
    b0, b1, bc = inner(c - 11), inner(c + 11), inner(c)
    apex = (round(P[0] + 0.3 * (bc[0] - P[0]), 1), round(P[1] + 0.3 * (bc[1] - P[1]), 1))
    f.poly([apex, b0, b1], "f2 s-acc2 sw2", True, check=True)
ellipse(f, 148, 172, 20, 26, "fp ln")
# ureter leaves the pelvis through the hilum and runs down
tube(f, bez((146, 186), (118, 196), (98, 232), (96, 340), 20), 10)
# renal artery and vein enter the hilum, with branches in the sinus
f.line([(14, 112), (148, 112)], "c1 sw3", "ah")
f.line([(148, 146), (14, 146)], "c2 sw3", "ah")
f.line([(148, 112), (172, 94)], "c1 sw2")
f.line([(148, 112), (160, 128)], "c1 sw2")
f.line([(148, 146), (160, 138)], "c2 sw2")
f.text(14, 102, "renal artery", "tl")
f.text(14, 166, "renal vein", "tl")
f.text(14, 290, "ureter", "tl")
f.leader((56, 286), (91, 286))
f.text(282, 34, "fibrous capsule", "tl")
bp = outer(-38)
f.leader((278, 30), (round(bp[0] - 1, 1), round(bp[1] - 1, 1)))
f.text(282, 94, "cortex", "tl")
cpt = outer(-28, 0.88, 0.8)
f.leader((278, 90), cpt)
f.text(282, 178, "medulla", "tl")
mp = inner(0)
f.leader((278, 174), (mp[0] - 14, mp[1]))
f.text(14, 214, "renal pelvis", "tl")
f.leader((98, 210), (131, 180))
done(f, (400, 352),
     "A kidney cut lengthways. The tough fibrous capsule surrounds the outer layer, the cortex. Inside it are the darker medulla, shown as three pyramid shapes pointing towards the renal pelvis, a funnel-shaped space in the middle where urine collects. The ureter leaves the pelvis and runs downwards. The renal artery enters at the middle of the inner edge and divides into branches; the renal vein leaves from the same place.",
     "A kidney in section (a drawing). Blood enters in the renal artery and leaves in the renal vein; urine drains from the renal pelvis into the ureter.")

# ---------- 3. nephron ----------
f = Fig("nephron")
f.rect(108, 16, 190, 214, "fm s-acc sw2")
f.rect(108, 230, 190, 224, "fm2 s-acc sw2")
f.text(114, 34, "cortex", "tl tb")
f.text(208, 340, "medulla", "tl tb")
# Bowman's capsule with glomerulus
f.circle(170, 78, 26, "fp ln")
f.circle(166, 74, 8, "fr ln")
f.circle(176, 80, 8, "fr ln")
f.circle(168, 84, 6, "fr ln")
f.line([(116, 58), (150, 68)], "c1 sw3", "ah")
f.line([(160, 98), (140, 110)], "c1 sw3")
f.line([(140, 110), (134, 150), (138, 210), (150, 270), (150, 340)], "c1 thin dash sw2", "ah")
# tubule
tub = [(170, 104), (150, 116), (190, 128), (150, 140), (190, 152), (170, 164)]
f.line(tub + [(170, 420)], "c3 sw3")
f.line([(170, 420), (176, 436), (194, 436), (200, 420)], "c3 sw3")
f.line([(200, 420), (200, 216)], "c3 sw3")
f.line([(200, 216), (216, 200), (232, 216), (248, 200), (264, 216)], "c3 sw3")
f.line([(264, 216), (264, 442)], "c3 sw3", "ah")
# labels left
f.text(98, 48, "afferent", "tl", "end")
f.text(98, 62, "arteriole", "tl", "end")
f.leader((102, 58), (122, 60))
f.text(98, 112, "efferent", "tl", "end")
f.text(98, 126, "arteriole", "tl", "end")
f.leader((102, 118), (142, 108))
f.text(98, 172, "capillary", "tl", "end")
f.text(98, 186, "network", "tl", "end")
f.leader((102, 176), (134, 168))
f.text(98, 380, "descending", "tl", "end")
f.text(98, 394, "limb", "tl", "end")
f.leader((102, 384), (166, 384))
f.text(98, 440, "loop of Henle", "tl", "end")
f.leader((102, 436), (173, 436))
f.text(98, 330, "to renal", "tl", "end")
f.text(98, 344, "vein", "tl", "end")
# labels right
f.text(308, 50, "glomerulus", "tl")
f.leader((304, 46), (178, 78))
f.text(308, 78, "Bowman's", "tl")
f.text(308, 92, "capsule", "tl")
f.leader((304, 84), (194, 90))
f.text(308, 130, "proximal", "tl")
f.text(308, 144, "convoluted", "tl")
f.text(308, 158, "tubule", "tl")
f.leader((304, 140), (192, 138))
f.text(308, 196, "distal", "tl")
f.text(308, 210, "convoluted", "tl")
f.text(308, 224, "tubule", "tl")
f.leader((304, 200), (246, 202))
f.text(308, 300, "collecting", "tl")
f.text(308, 314, "duct", "tl")
f.leader((304, 304), (268, 304))
f.text(308, 372, "ascending", "tl")
f.text(308, 386, "limb", "tl")
f.leader((304, 376), (203, 376))
f.text(264, 472, "to renal pelvis", "tl", "middle")
done(f, (400, 480),
     "A nephron and its blood supply, drawn in the cortex and medulla of the kidney. An afferent arteriole enters a Bowman's capsule, where it forms the glomerulus, and an efferent arteriole leaves it and forms a capillary network around the tubule that leads to the renal vein. The filtrate leaves the capsule in the proximal convoluted tubule, which is coiled and in the cortex. The tubule then runs down into the medulla as the descending limb of the loop of Henle, turns, and runs up as the ascending limb to the distal convoluted tubule, which is coiled and in the cortex. It joins a collecting duct, which runs down through the medulla to the renal pelvis.",
     "A nephron (a drawing, not to scale). The Bowman's capsule, proximal convoluted tubule and distal convoluted tubule are in the cortex; the loop of Henle and collecting duct run into the medulla.")

# ---------- 4. filter ----------
f = Fig("filter")
f.rect(10, 8, 230, 80, "fm s-acc sw2")
for k in range(6):
    x0 = 26 + 36 * k
    f.rect(x0, 80, 22, 20, BOX)
f.rect(20, 104, 218, 20, "f2 s-acc2 sw2")
for k in range(6):
    x0 = 26 + 36 * k
    f.rect(x0, 128, 24, 18, BOX)
for cxp in (86, 158):
    ellipse(f, cxp, 164, 52, 14, BOX)
f.rect(10, 196, 230, 30, "fp ln")
ellipse(f, 120, 40, 22, 10, "fr ln")
for (px, py) in ((170, 30), (196, 56), (205, 28), (30, 36)):
    f.circle(px, py, 4, "fi")
f.line([(56, 20), (56, 214)], "c3 sw2 dash", "ah")
f.text(252, 28, "red blood cell", "tl")
f.leader((248, 24), (141, 36))
f.text(252, 54, "plasma protein", "tl")
f.leader((248, 50), (200, 54))
f.text(252, 94, "capillary", "tl")
f.text(252, 108, "endothelium", "tl")
f.leader((248, 90), (222, 90))
f.text(252, 134, "basement", "tl")
f.text(252, 148, "membrane", "tl")
f.leader((248, 130), (236, 116))
f.text(252, 172, "podocyte", "tl")
f.text(252, 186, "(slits between", "tl")
f.text(252, 200, "its feet)", "tl")
f.leader((248, 168), (136, 168))
f.text(252, 222, "capsule space", "tl")
f.leader((248, 218), (200, 214))
f.text(252, 236, "(filtrate)", "tl")
done(f, (352, 250),
     "Cross-section of the filter between a glomerular capillary and the Bowman's capsule. At the top is the capillary lumen with a red blood cell and plasma proteins. Below it is the capillary endothelium, a row of cells with gaps (pores) between them, then the basement membrane, a continuous layer. Under that are the podocytes, whose foot-like projections have slits between them, and then the capsule space. A dashed arrow shows water and small molecules passing through a pore, the basement membrane and a slit into the capsule space; the cell and proteins stay in the capillary.",
     "The three layers of the filter. Water and small molecules pass through the pores, the basement membrane and the slits between the podocyte projections; blood cells and plasma proteins stay in the capillary.")

# ---------- 5. PCT cell ----------
f = Fig("pct")
poly = [(112, 272), (112, 106)]
for i in range(8):
    x0 = 112 + 24 * i
    poly += [(x0, 88), (x0 + 12, 88), (x0 + 12, 106)]
    if i < 7:
        poly += [(x0 + 24, 106)]
poly += [(292, 272)]
f.poly(poly, BOX, True)
ellipse(f, 150, 190, 22, 18, "fm s-acc sw2")
for (mx, my) in ((222, 244), (258, 232), (190, 248)):
    ellipse(f, mx, my, 13, 8, "f2 s-acc2 sw2")
# transport proteins
f.rect(152, 100, 14, 16, "fm s-acc sw2")
f.line([(159, 56), (159, 150)], "c3 sw2", "ah")
f.rect(240, 264, 14, 16, "fm s-acc sw2")
f.line([(247, 200), (247, 308)], "c3 sw2", "ah")
f.rect(126, 264, 14, 16, "fm s-acc sw2")
f.line([(133, 224), (133, 308)], "c2 sw2", "ah")
f.rect(118, 316, 174, 40, "fp ln")
# labels left
f.text(104, 40, "lumen of PCT", "tl", "end")
f.text(104, 54, "(filtrate)", "tl", "end")
f.text(104, 98, "microvilli", "tl", "end")
f.leader((108, 94), (118, 96))
f.text(104, 192, "nucleus", "tl", "end")
f.leader((108, 190), (128, 190))
f.text(104, 296, "tissue fluid", "tl", "end")
f.text(104, 340, "blood in", "tl", "end")
f.text(104, 354, "capillary", "tl", "end")
# labels right
f.text(172, 40, "cotransporter protein", "tl")
f.text(172, 54, "carries sodium ions", "tl")
f.text(172, 68, "and glucose in", "tl")
f.text(302, 230, "mitochondria", "tl")
f.leader((298, 226), (272, 232))
f.text(302, 262, "carrier", "tl")
f.text(302, 276, "protein", "tl")
f.text(302, 290, "(glucose out)", "tl")
f.leader((298, 268), (256, 272))
f.text(104, 262, "Na⁺/K⁺ pump", "tl", "end")
f.text(104, 276, "(uses ATP)", "tl", "end")
f.leader((108, 268), (124, 272))
done(f, (400, 372),
     "A cell of the proximal convoluted tubule. The surface facing the lumen of the tubule has microvilli. A cotransporter protein in that membrane carries sodium ions and glucose into the cell together. The cell contains a nucleus and mitochondria. In the membrane facing the blood are a sodium–potassium pump, which moves sodium ions out of the cell and potassium ions in using ATP, and a carrier protein through which glucose leaves by facilitated diffusion. Below the cell is tissue fluid and then a blood capillary.",
     "A PCT cell. Sodium–potassium pumps in the basal membrane keep the sodium ion concentration inside the cell low; sodium ions then enter with glucose by cotransport, and glucose leaves by facilitated diffusion into the blood.")

# ---------- 6. ADH ----------
f = Fig("adh")
steps = [("blood water potential", "falls"), ("osmoreceptors in the", "hypothalamus detect it"),
         ("posterior pituitary", "releases more ADH"), ("ADH binds to receptors on", "collecting duct cells"),
         ("vesicles with aquaporins", "fuse with the membrane"), ("more water reabsorbed", "by osmosis"),
         ("small volume of", "concentrated urine")]
for i, (a, b) in enumerate(steps):
    y = 10 + i * 62
    f.rect(30, y, 210, 40, BOX)
    f.text(135, y + 17, a, "tl", "middle")
    f.text(135, y + 32, b, "tl", "middle")
    if i < len(steps) - 1:
        f.line([(135, y + 40), (135, y + 62)], ARR, "ah")
f.line([(240, 402), (320, 402), (320, 30), (244, 30)], "c2 sw2", "ah")
for k, t in enumerate(["water", "potential", "rises, so", "less ADH"]):
    f.text(250, 190 + 14 * k, t, "tl")
done(f, (340, 434),
     "A flow chart in seven boxes joined by downward arrows: blood water potential falls; osmoreceptors in the hypothalamus detect it; the posterior pituitary releases more ADH; ADH binds to receptors on collecting duct cells; vesicles with aquaporins fuse with the membrane; more water is reabsorbed by osmosis; a small volume of concentrated urine is made. An arrow from the last box back to the first shows that the water potential of the blood rises, so less ADH is released.",
     "The ADH pathway when the water potential of the blood falls. The return arrow is negative feedback: a rise in blood water potential reduces ADH release.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
