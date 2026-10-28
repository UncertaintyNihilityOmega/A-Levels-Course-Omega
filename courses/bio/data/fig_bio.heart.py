# data/fig_bio.heart.py: builds the hand-drawn SVG figures of chapters/bio.heart.md and checks label clearance.
# Run: py data/fig_bio.heart.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.heart replaces the @@FIG_<NAME> placeholder lines of the chapter.
# The pressure graph (PRESS) is drawn from the same model as the widget (data/fig_cardiac.py).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts, bez
from fig_cardiac import LA, LV, AO, events

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["HEARTEXT", "HEARTLS", "PRESS", "CONDUCT"]
figs, problems = [], []

WALL = "fm s-acc sw2"     # cardiac muscle
MID = "f1 s-acc sw2"
LUM = "fp ln"
VALVE = "f2 s-acc2 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def tube(f, centre, w, lum="fp", line="ln", check=False):
    """A vessel: a lumen polygon (fill only) plus the two side lines, along a centre line with half-width w/2."""
    left, right = [], []
    n = len(centre)
    for i, (x, y) in enumerate(centre):
        if i == 0:
            dx, dy = centre[1][0] - x, centre[1][1] - y
        elif i == n - 1:
            dx, dy = x - centre[i - 1][0], y - centre[i - 1][1]
        else:
            a = math.atan2(y - centre[i - 1][1], x - centre[i - 1][0])
            b = math.atan2(centre[i + 1][1] - y, centre[i + 1][0] - x)
            m = (a + b) / 2
            dx, dy = math.cos(m), math.sin(m)
            k = 1 / max(math.cos((b - a) / 2), 0.4)
        L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        k = 1 / max(math.cos((b - a) / 2), 0.4) if 0 < i < n - 1 else 1
        left.append((round(x + nx * w / 2 * k, 1), round(y + ny * w / 2 * k, 1)))
        right.append((round(x - nx * w / 2 * k, 1), round(y - ny * w / 2 * k, 1)))
    f.poly(left + right[::-1], lum, True, False)
    f.line(left, line, check=check)
    f.line(right, line, check=check)


def sc(pts, s, ox, oy, x0=208, y0=104):
    return [(round(ox + (x - x0) * s, 1), round(oy + (y - y0) * s, 1)) for x, y in pts]


# ---- shared longitudinal-section geometry (heart LS, viewBox coordinates before scaling) ----
OUTER = [(208, 150), (222, 118), (262, 104), (302, 116), (325, 126), (352, 116), (392, 104), (438, 118), (452, 152), (456, 225),
         (432, 300), (385, 355), (332, 378), (290, 356), (248, 305), (216, 235)]
RIGHT = [(220, 148), (230, 126), (262, 114), (308, 124), (312, 330), (296, 346), (276, 328), (245, 285), (226, 232), (224, 190)]
LEFT = [(338, 126), (366, 126), (366, 208), (378, 208), (378, 128), (414, 126), (432, 152), (428, 200), (418, 224), (406, 290),
        (368, 338), (338, 348)]

# ---------- 1. external view ----------
f = Fig("heartext")
dx = 30
P = lambda pts: [(x + dx, y) for x, y in pts]
outer = P([(100, 170), (112, 134), (150, 116), (190, 124), (214, 118), (250, 112), (290, 130), (300, 172), (290, 235), (256, 300),
           (205, 340), (172, 310), (134, 250), (108, 205)])
tube(f, P([(126, 138), (126, 60)]), 20)
tube(f, P([(172, 130), (172, 88), (158, 62)]), 22)
tube(f, P([(224, 130), (224, 72), (250, 44), (292, 40)]), 24)
f.poly(outer, WALL, True, False)
f.line(P([(100, 174), (158, 196), (240, 190), (296, 168)]), "ln-m thin", check=False)         # atrio-ventricular groove
f.line(P([(194, 192), (190, 262), (205, 338)]), "ln-m thin", check=False)                        # interventricular groove
f.poly(P([(102, 170), (110, 138), (148, 120), (186, 126), (196, 150), (190, 190), (150, 196)]), MID, True, False)   # right atrium
f.poly(P([(236, 114), (270, 114), (296, 134), (298, 172), (262, 186), (236, 178), (226, 140)]), MID, True, False)    # left atrium
tube(f, P([(172, 134), (172, 88), (158, 62)]), 22)
tube(f, P([(224, 134), (224, 72), (250, 44), (292, 40)]), 24)
tube(f, P([(126, 142), (126, 62)]), 20)
f.line(P(bez((236, 128), (284, 150), (290, 222), (258, 286), 20)), "c3 sw2", check=False)
f.line(P(bez((212, 128), (160, 150), (120, 170), (118, 214), 20)), "c3 sw2", check=False)
f.line(P(bez((276, 160), (292, 176), (296, 210), (284, 236), 10)), "c3 sw2", check=False)
f.text(120, 30, "pulmonary artery", "tl", "end")
f.text(114, 74, "vena cava", "tl", "end")
f.text(96, 160, "right atrium", "tl", "end"); f.leader((100, 156), (150, 152))
f.text(104, 262, "right ventricle", "tl", "end"); f.leader((108, 258), (168, 250))
f.text(358, 40, "aorta", "tl")
f.text(342, 160, "left", "tl"); f.text(342, 174, "atrium", "tl"); f.leader((338, 160), (318, 152))
f.text(342, 250, "left", "tl"); f.text(342, 264, "ventricle", "tl"); f.leader((338, 252), (298, 240))
f.text(342, 206, "coronary", "tl"); f.text(342, 220, "artery", "tl"); f.leader((338, 208), (306, 210))
f.text(235, 366, "apex", "tl", "middle"); f.leader((235, 352), (235, 344))
done(f, (400, 378),
     "External view of the heart from the front. Two thin-walled atria sit above two thicker ventricles. The vena cava enters the right atrium, the pulmonary artery leaves the right ventricle and the aorta leaves the left ventricle. Coronary arteries run over the surface of the ventricles from the base of the aorta. The apex is the pointed bottom end.",
     "The outside of the heart, seen from the front, with the right side of the body on the left. The pulmonary veins enter the back of the left atrium, so they are not seen here. The coronary arteries supply the heart muscle itself.")

# ---------- 2. internal structure (longitudinal section) ----------
f = Fig("heartls")
f.poly(OUTER, WALL, True, False)
f.poly(RIGHT, LUM, True, False)
f.poly(LEFT, LUM, True, False)
tube(f, [(150, 167), (232, 167)], 22) if False else None
tube(f, [(184, 167), (230, 167)], 22)                      # vena cava into the right atrium
tube(f, [(292, 134), (292, 92), (270, 68), (236, 58)], 22)  # pulmonary artery
tube(f, [(353, 134), (353, 84), (372, 62), (410, 56)], 26)  # aorta
tube(f, [(426, 147), (488, 147)], 22)                       # pulmonary vein into the left atrium
# semilunar valve cusps (pocket-shaped) at the base of the pulmonary artery and aorta
f.poly([(281, 128), (287, 144), (292, 128)], VALVE, True, False); f.poly([(292, 128), (297, 144), (303, 128)], VALVE, True, False)
f.poly([(340, 130), (346, 146), (353, 130)], VALVE, True, False); f.poly([(353, 130), (360, 146), (366, 130)], VALVE, True, False)
# atrioventricular valves with tendinous cords
f.line([(226, 208), (252, 246)], "ln thick", check=False); f.line([(312, 208), (286, 246)], "ln thick", check=False)
f.line([(338, 208), (364, 246)], "ln thick", check=False); f.line([(418, 210), (392, 248)], "ln thick", check=False)
f.poly([(250, 322), (262, 294), (276, 322)], MID, True, False)
f.poly([(340, 346), (352, 318), (366, 340)], MID, True, False)
f.line([(252, 246), (258, 296)], "ln-m thin", check=False); f.line([(286, 246), (272, 296)], "ln-m thin", check=False)
f.line([(364, 246), (352, 316)], "ln-m thin", check=False); f.line([(392, 248), (358, 316)], "ln-m thin", check=False)
# labels, left column
f.text(172, 54, "pulmonary", "tl", "end"); f.text(172, 68, "artery", "tl", "end"); f.leader((176, 62), (240, 62))
f.text(172, 100, "semilunar valve", "tl", "end"); f.text(172, 114, "(pulmonary)", "tl", "end"); f.leader((176, 108), (284, 130))
f.text(172, 171, "vena cava", "tl", "end")
f.text(172, 216, "right atrium", "tl", "end"); f.leader((176, 212), (246, 188))
f.text(172, 262, "tricuspid valve", "tl", "end"); f.text(172, 276, "(right AV valve)", "tl", "end"); f.leader((176, 258), (244, 238))
f.text(172, 316, "tendinous cords", "tl", "end"); f.leader((176, 312), (255, 274))
f.text(172, 362, "right ventricle", "tl", "end"); f.leader((176, 358), (282, 322))
# labels, right column
f.text(500, 54, "aorta", "tl"); f.leader((496, 50), (404, 58))
f.text(500, 98, "semilunar valve", "tl"); f.text(500, 112, "(aortic)", "tl"); f.leader((496, 104), (364, 134))
f.text(500, 151, "pulmonary vein", "tl")
f.text(500, 196, "left atrium", "tl"); f.leader((496, 192), (412, 176))
f.text(500, 250, "bicuspid valve", "tl"); f.text(500, 264, "(left AV valve)", "tl"); f.leader((496, 246), (396, 238))
f.text(500, 300, "thick muscular wall", "tl"); f.text(500, 314, "of left ventricle", "tl"); f.leader((496, 296), (448, 280))
f.text(500, 362, "left ventricle", "tl"); f.leader((496, 358), (388, 296))
f.text(326, 404, "septum", "tl", "middle"); f.leader((326, 392), (326, 330))
done(f, (640, 416),
     "The heart in longitudinal section, seen from the front, with the right side of the body on the left. The right atrium and right ventricle are on the left of the figure and the left atrium and left ventricle on the right. A muscular septum separates the two sides. The tricuspid valve lies between the right chambers and the bicuspid valve between the left chambers, each with tendinous cords attached to the ventricle wall. Semilunar valves are at the start of the pulmonary artery and the aorta. The wall of the left ventricle is much thicker than the wall of the right ventricle, and the atria have thin walls.",
     "Internal structure of the heart. The wall of the left ventricle is about three times as thick as the wall of the right ventricle, and the atria are thin-walled. The cords stop the atrioventricular valve flaps turning inside out when the ventricles contract.",
     "fig")

# ---------- 3. pressure graph (model) ----------
f = Fig("press")
x0, x1, ytop, ybot = 60, 500, 40, 270
X = lambda t: x0 + (x1 - x0) * t / 0.8
Y = lambda p: ybot - (ybot - ytop) * p / 18
f.line([(x0, ytop - 6), (x0, ybot), (x1 + 6, ybot)], "ax", check=False)
for t in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
    f.line([(X(t), ybot), (X(t), ybot + 5)], "ln-m thin", check=False)
    f.text(X(t), ybot + 18, f"{t:g}", "ts", "middle")
for p in [0, 5, 10, 15]:
    f.line([(x0 - 5, Y(p)), (x0, Y(p))], "ln-m thin", check=False)
    f.text(x0 - 9, Y(p) + 4, f"{p}", "ts", "end")
f.text(8, 14, "pressure / kPa", "tl")
f.text(580, ybot + 18, "time / s", "tl", "end")
ts = [k * 0.004 for k in range(201)]
for fn, cls in ((AO, "c1 sw2"), (LV, "c2 sw2"), (LA, "c3 sw2")):
    f.line([(round(X(t), 1), round(Y(fn(t)), 1)) for t in ts], cls, check=False)
ev = events()
for k, (t, s) in enumerate(ev, 1):
    f.line([(round(X(t), 1), ybot), (round(X(t), 1), ytop + 6)], "ln-m thin dash", check=False)
    f.text(X(t), ytop - 6, str(k), "tl tb", "middle")
f.text(X(0.25), Y(16.2) - 8, "left ventricle", "tl", "middle")
f.text(504, Y(AO(0.8)) + 4, "aorta", "tl")
f.text(X(0.06) + 18, Y(1.55) - 24, "left atrium", "tl")
# phases under the axis
for (a, b, name) in [(0, 0.1, None), (0.1, 0.4, "ventricular systole"), (0.4, 0.8, "diastole")]:
    f.line([(X(a) + 2, 296), (X(b) - 2, 296)], "ln thick", check=False)
f.text(X(0.05), 312, "atrial", "tl", "middle"); f.text(X(0.05), 326, "systole", "tl", "middle")
f.text(X(0.25), 312, "ventricular systole", "tl", "middle")
f.text(X(0.6), 312, "diastole", "tl", "middle")
done(f, (600, 336),
     "Model graph of pressure in kilopascals against time in seconds for one cardiac cycle of 0.8 seconds, for the left atrium, the left ventricle and the aorta. The left atrium pressure stays below 1.6 kilopascals. The left ventricle pressure is near 0.5 kilopascals, rises steeply to about 16 kilopascals at 0.25 seconds and falls again by 0.45 seconds. The aorta pressure stays between 10.5 and 16 kilopascals. Four numbered dashed lines mark valve events: 1, the atrioventricular valve closes at about 0.10 seconds; 2, the semilunar valve opens at about 0.17 seconds; 3, the semilunar valve closes at about 0.38 seconds; 4, the atrioventricular valve opens at about 0.45 seconds. Atrial systole lasts 0.1 seconds, ventricular systole 0.3 seconds and diastole 0.4 seconds.",
     "Pressures in the left side of the heart in one cycle (a model, 75 beats per minute). Dashed lines: 1 AV valve closes (ventricular pressure rises above atrial pressure), 2 semilunar valve opens (ventricular pressure rises above aortic pressure), 3 semilunar valve closes (ventricular pressure falls below aortic pressure), 4 AV valve opens (ventricular pressure falls below atrial pressure).",
     "fig")

# ---------- 4. conducting system ----------
f = Fig("conduct")
s, ox, oy = 0.72, 116, 56
f.poly(sc(OUTER, s, ox, oy), WALL, True, False)
f.poly(sc(RIGHT, s, ox, oy), LUM, True, False)
f.poly(sc(LEFT, s, ox, oy), LUM, True, False)
S = lambda x, y: (round(ox + (x - 208) * s, 1), round(oy + (y - 104) * s, 1))
# fibrous tissue between atria and ventricles (gap at the AVN)
f.line([S(226, 210), S(296, 210)], "ln thick", check=False)
f.line([S(310, 210), S(428, 210)], "ln thick", check=False)
# excitation across the atria
f.line([S(244, 138), S(296, 186)], "c3 sw2 dash", "ah", check=False)
f.line([S(250, 134), S(330, 130), S(396, 150), S(410, 176)], "c3 sw2 dash", "ah", check=False)
# SAN, AVN
e = S(240, 134); ellipse(f, e[0], e[1], 7, 5, VALVE, check=False)
e2 = S(304, 205); ellipse(f, e2[0], e2[1], 7, 5, VALVE, check=False)
# bundle of His and Purkyne tissue
f.line([S(304, 210), S(326, 232), S(326, 336)], "c1 sw3", check=False)
f.line([S(326, 336), S(296, 336), S(262, 300), S(236, 244)], "c1 sw2", "ah", check=False)
f.line([S(326, 336), S(368, 330), S(404, 290), S(420, 232)], "c1 sw2", "ah", check=False)
# labels
f.text(108, 62, "sinoatrial", "tl", "end"); f.text(108, 76, "node (SAN)", "tl", "end"); f.leader((112, 70), (e[0] - 6, e[1] - 2))
f.text(108, 112, "wave spreads", "tl", "end"); f.text(108, 126, "across atria", "tl", "end"); f.leader((112, 118), S(262, 160))
f.text(108, 170, "fibrous tissue", "tl", "end"); f.text(108, 184, "(no conduction)", "tl", "end"); f.leader((112, 176), S(240, 210))
f.text(108, 250, "Purkyne", "tl", "end"); f.text(108, 264, "tissue", "tl", "end"); f.leader((112, 256), S(246, 270))
f.text(304, 150, "atrio-", "tl"); f.text(304, 164, "ventricular", "tl"); f.text(304, 178, "node (AVN)", "tl"); f.leader((300, 160), (e2[0] + 8, e2[1] - 1))
f.text(304, 216, "bundle of His", "tl"); f.leader((300, 212), S(328, 250))
f.text(304, 268, "ventricles contract", "tl"); f.text(304, 282, "from the apex up", "tl")
done(f, (400, 330),
     "The conducting system of the heart in longitudinal section. The sinoatrial node, SAN, is in the wall of the right atrium. Dashed arrows show the wave of excitation spreading across both atria. A layer of fibrous tissue between the atria and the ventricles blocks the wave except at the atrioventricular node, AVN, at the base of the right atrium near the septum. From the AVN the bundle of His runs down the septum, then Purkyne tissue carries the wave to the apex and up the walls of both ventricles.",
     "How a heartbeat spreads: SAN, then across the atria, then the delay at the AVN (the only way through the fibrous tissue), then the bundle of His and Purkyne tissue to the apex, so the ventricles contract from the bottom upwards.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
