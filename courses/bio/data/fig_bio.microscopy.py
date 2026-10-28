# data/fig_bio.microscopy.py: SVG figures of chapters/bio.microscopy.md. Run: py data/fig_bio.microscopy.py
# Prints each <figure> (paste into the chapter) and a clearance report on stderr.
import math, sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p2 import Fig, finish, ell_pts

figs, problems = [], []

# ---------- Figure 1: light microscope ----------
f = Fig("microscope")
D = 26
def X(x): return x + D
# arm (with the bridge to the body tube) and base
f.poly([(X(212), 64), (X(262), 64), (X(262), 282), (X(238), 282), (X(238), 98), (X(212), 98)], "f1 s-acc sw2")
f.rect(X(150), 282, 130, 16, "fm s-acc sw2", 4)                  # base
f.rect(X(192), 44, 20, 86, "f1 s-acc sw2")                       # body tube
f.rect(X(188), 22, 28, 22, "f2 s-acc2 sw2")                      # eyepiece
f.rect(X(184), 130, 36, 12, "fm s-acc sw2")                      # revolving nosepiece
f.poly([(X(188), 142), (X(200), 142), (X(198), 164), (X(190), 164)], "f2 s-acc2 sw2")   # x10 objective
f.poly([(X(204), 142), (X(216), 142), (X(214), 176), (X(206), 176)], "f2 s-acc2 sw2")   # x40 objective
f.rect(X(176), 184, 56, 6, "fp ln")                              # slide
f.rect(X(158), 190, 90, 8, "fm s-acc sw2")                       # stage
f.poly([(X(194), 198), (X(210), 198), (X(206), 212), (X(198), 212)], "f2 s-acc2 sw2")   # condenser lens
f.rect(X(190), 216, 24, 6, "fm s-acc sw2")                       # iris diaphragm
f.circle(X(202), 252, 12, "fh s-mute sw2")                       # lamp
f.circle(X(250), 176, 13, "fm s-acc sw2")                        # coarse focus
f.circle(X(250), 212, 8, "fm s-acc sw2")                         # fine focus
L = 150
f.label(L, 36, "eyepiece lens", (L + 4, 33), (X(188), 33), "end")
f.label(L, 84, "body tube", (L + 4, 81), (X(192), 81), "end")
f.label(L, 138, "revolving nosepiece", (L + 4, 135), (X(184), 135), "end")
f.label(L, 160, "objective lenses", (L + 4, 157), (X(188), 157), "end")
f.label(L, 182, "slide + coverslip", (L + 4, 179), (X(176), 187), "end")
f.label(L, 210, "stage", (L + 4, 207), (X(160), 195), "end")
f.label(L, 232, "condenser + diaphragm", (L + 4, 229), (X(190), 220), "end")
f.label(L, 256, "light source", (L + 4, 253), (X(190), 253), "end")
f.label(L, 295, "base", (L + 4, 292), (X(150), 291), "end")
R = X(270)
f.label(R + 4, 112, "arm", (R + 2, 109), (X(262), 109))
f.text(R + 8, 172, "coarse")
f.text(R + 8, 186, "focus")
f.line([(R + 4, 179), (X(263), 179)], "ln-m thin", check=False)
f.leads.append(((R + 4, 179), (X(263), 179), "coarse"))
f.text(R + 8, 212, "fine")
f.text(R + 8, 226, "focus")
f.line([(R + 4, 215), (X(258), 215)], "ln-m thin", check=False)
f.leads.append(((R + 4, 215), (X(258), 215), "fine"))
figs.append(f.svg((360, 312),
    "Side view of a light microscope. From the top: eyepiece lens, body tube, revolving nosepiece with two objective "
    "lenses, a stage that holds the slide and coverslip, a condenser lens and iris diaphragm below the stage, and a "
    "light source above the base. The arm joins the body tube to the base and carries the coarse focus and fine focus wheels.",
    "A light microscope. Light from the source passes up through the condenser and the thin specimen, then through "
    "an objective lens and the eyepiece lens to your eye."))
problems.extend(f.check())

# ---------- Figure 2: graticule over stage micrometer ----------
f = Fig("graticule")
x0, ppu = 20, 10.0                      # 10 px per eyepiece unit; 25 units = 6 stage divisions
div = 25 * ppu / 6                      # px per stage division
f.text(20, 14, "eyepiece graticule: 30 units", "tl tb")
f.line([(x0, 56), (x0 + 300, 56)], "ln")
for u in range(0, 31):
    h = 10 if u % 5 == 0 else 5
    f.line([(x0 + u * ppu, 56), (x0 + u * ppu, 56 - h)], "ln", check=False)
    if u % 5 == 0:
        f.text(x0 + u * ppu, 34, str(u), "ts", "middle")
f.line([(x0, 108), (x0 + 7 * div + 4, 108)], "ln")
for d in range(0, 8):
    f.line([(x0 + d * div, 108), (x0 + d * div, 122)], "ln", check=False)
    f.text(x0 + d * div, 138, str(d), "ts", "middle")
f.line([(x0, 56), (x0, 108)], "ln-m thin dash", check=False)
f.line([(x0 + 250, 56), (x0 + 250, 108)], "ln-m thin dash", check=False)
f.text(x0 + 250 - 8, 86, "25 units = 6 divisions", "tl", "end")
f.text(20, 160, "stage micrometer: 1 division = 10 µm", "tl tb")
figs.append(f.svg((340, 172),
    "Eyepiece graticule laid over a stage micrometer. The zero marks of both scales line up at the left. The graticule "
    "has 30 units drawn; the stage micrometer has divisions numbered 0 to 7, each 10 micrometres. At the right, the 25 "
    "mark of the graticule lines up with the 6 mark of the stage micrometer.",
    "Calibrating an eyepiece graticule at one objective: line up the zeros, then find a mark on the graticule that lines "
    "up exactly with a mark on the stage micrometer. Here 25 eyepiece units match 6 divisions of 10 µm."))
problems.extend(f.check())

# ---------- Figure 3: scale bar on an electron micrograph (drawing) ----------
f = Fig("scalebar")
f.rect(10, 10, 320, 200, "fm s-acc sw2", 4, check=False)           # the micrograph frame
f.ellipse(190, 84, 60, 28, "f2 s-acc2 sw2")                        # outer membrane of a mitochondrion
f.ellipse(190, 84, 53, 21, "fp ln")                                # inner membrane
for k in range(-3, 4):                                             # cristae: folds of the inner membrane
    cx = 190 + k * 14
    f.line([(cx, 63 if k % 2 == 0 else 105), (cx, 84 + (10 if k % 2 == 0 else -10))], "ln", check=False)
f.line([(30, 176), (70, 176)], "ln thick")                         # scale bar, 40 units long
f.line([(30, 170), (30, 182)], "ln", check=False)
f.line([(70, 170), (70, 182)], "ln", check=False)
f.text(50, 198, "0.5 µm", "tl", "middle")
f.label(210, 146, "mitochondrion", (216, 135), (200, 112), "start")
f.label(110, 40, "membranes", (114, 41), (176, 58), "end")
f.label(150, 166, "scale bar", (146, 163), (74, 174), "start")
figs.append(f.svg((340, 222),
    "Drawing of an electron micrograph of one mitochondrion, with a scale bar at the bottom left labelled 0.5 micrometres. "
    "The mitochondrion is about three times as long as the scale bar.",
    "A drawing of an electron micrograph with its scale bar. The mitochondrion is 3 bar lengths long, so it is 3 × 0.5 µm = "
    "1.5 µm long. In a real micrograph you would measure both lengths with a ruler.", "fig small"))
problems.extend(f.check())

# ---------- Figure 4: lowering a coverslip ----------
f = Fig("coverslip")
f.rect(30, 140, 270, 10, "fp ln")                                   # slide (top edge at y = 140)
f.ellipse(112, 135, 32, 6, "f2 s-acc2 sw2")                         # drop of water or stain
ang = math.radians(28)
L = 150
p0 = (80, 138)                                                       # left edge rests on the slide at the drop
p1 = (p0[0] + L * math.cos(ang), p0[1] - L * math.sin(ang))
th = 3
f.poly([p0, p1, (p1[0] + th * math.sin(ang), p1[1] + th * math.cos(ang)), (p0[0] + th * math.sin(ang), p0[1] + th * math.cos(ang))], "f1 s-acc sw2")
f.line([(270, 24), (p1[0] + 4, p1[1] + 6)], "ln thick", check=False)    # mounted needle
f.line([(296, 50), (296, 84)], "ln", "ah", check=False)             # lower slowly
f.text(250, 112, "lower slowly", "tl")
f.label(250, 172, "slide", (252, 169), (240, 151), "start")
f.label(14, 190, "specimen in a drop of water or stain", (66, 180), (96, 142), "start")
mid = (p0[0] + 0.45 * L * math.cos(ang), p0[1] - 0.45 * L * math.sin(ang))
f.label(14, 60, "coverslip", (60, 64), (mid[0] - 2, mid[1] - 3), "start")
f.label(232, 28, "mounted needle", (236, 26), (258, 34), "end")
figs.append(f.svg((340, 204),
    "Side view of lowering a coverslip. A drop of water or stain with the specimen lies on a slide. One edge of the "
    "coverslip rests on the slide beside the drop, and the other edge is held up by a mounted needle and lowered slowly.",
    "Lower the coverslip at an angle. The liquid spreads along the edge and pushes the air out in front of it, so no "
    "bubbles are trapped under the glass.", "fig small"))
problems.extend(f.check())

# ---------- Figure 5: the magnification triangle ----------
f = Fig("triangle")
f.poly([(100, 10), (190, 130), (10, 130)], "f1 s-acc sw2")
f.line([(55, 70), (145, 70)], "ln", check=False)
f.line([(100, 70), (100, 130)], "ln", check=False)
f.text(100, 56, "I", "tl tb", "middle")
f.text(66, 112, "A", "tl tb", "middle")
f.text(134, 112, "M", "tl tb", "middle")
figs.append(f.svg((200, 142),
    "The magnification triangle. I is at the top; A and M sit side by side below it, separated by a vertical line. "
    "Cover the quantity you want: covering I leaves A times M, covering A leaves I over M, covering M leaves I over A.",
    "The magnification triangle: I = image size, A = actual size, M = magnification. Cover the one you want to find.", "fig small"))
problems.extend(f.check())

finish(figs, problems)
