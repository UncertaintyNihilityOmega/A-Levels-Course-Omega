# data/fig_bio.prokaryotes.py: SVG figures of chapters/bio.prokaryotes.md. Run: py data/fig_bio.prokaryotes.py
import math, sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p2 import Fig, finish, ell_pts

figs, problems = [], []


def stadium(cx, y0, y1, w):
    """Vertical rod with half-circle ends: points of the outline."""
    r = w / 2
    pts = []
    for k in range(0, 19):                                  # top cap, from left to right
        t = math.pi + math.pi * k / 18
        pts.append((cx + r * math.cos(t), y0 + r + r * math.sin(t)))
    for k in range(0, 19):                                  # bottom cap, right to left
        t = math.pi * k / 18
        pts.append((cx + r * math.cos(t), y1 - r + r * math.sin(t)))
    return pts


# ---------- bacterium ----------
f = Fig("bacterium")
cx = 90
f.smooth(stadium(cx, 20, 180, 84), "fm s-acc sw2")                 # capsule
f.smooth(stadium(cx, 26, 174, 72), "f3 s-acc2 sw2")                # cell wall
f.smooth(stadium(cx, 31, 169, 62), "f1 ln")                        # cell surface membrane (cytoplasm inside)
loop = []
for k in range(0, 61):                                             # circular DNA, folded in the cytoplasm
    t = 2 * math.pi * k / 60
    loop.append((cx - 2 + (13 + 5 * math.sin(5 * t)) * math.cos(t), 92 + 34 * math.sin(t)))
f.smooth(loop, "c3 sw2", True, check=False)
f.circle(cx + 12, 146, 7, "c1 sw2", check=False)                   # plasmid
f.dots([(cx - 20, 60), (cx + 18, 56), (cx - 18, 128), (cx + 20, 108), (cx - 8, 150), (cx + 6, 160), (cx - 22, 82),
        (cx + 22, 76), (cx - 14, 162), (cx + 0, 44)], 2.4, "fi")   # 70S ribosomes
for (x0, y0, x1, y1) in ((118, 36, 130, 22), (126, 46, 140, 36), (132, 58, 148, 52)):   # pili at the top end
    f.line([(x0, y0), (x1, y1)], "ln", check=False)
flag = [(cx + 9 * math.sin(k * 0.55), 180 + k * 4) for k in range(0, 24)]
f.smooth(flag, "ln thick", False, check=False)                     # flagellum
X0 = 176
f.label(X0, 26, "pili*", (X0 - 4, 23), (134, 30), "start")
f.label(X0, 64, "capsule*", (X0 - 4, 61), (cx + 42, 66), "start")
f.label(X0, 86, "cell wall", (X0 - 4, 83), (cx + 36, 86), "start")
f.text(X0, 106, "cell surface", "tl"); f.text(X0, 120, "membrane", "tl")
f.line([(X0 - 4, 110), (cx + 31, 110)], "ln-m thin", check=False); f.leads.append(((X0 - 4, 110), (cx + 31, 110), "cell surface"))
f.label(X0, 144, "circular DNA", (X0 - 4, 141), (cx + 8, 116), "start")
f.label(X0, 168, "plasmid*", (X0 - 4, 165), (cx + 19, 147), "start")
f.label(X0, 192, "70S ribosomes", (X0 - 4, 189), (cx + 17, 160), "start")
f.label(X0, 238, "flagellum*", (X0 - 4, 235), (cx + 5, 235), "start")
figs.append(f.svg((350, 288),
    "A rod-shaped bacterium. From the outside: a slime capsule, a cell wall of peptidoglycan, and the cell surface "
    "membrane. Inside, the cytoplasm contains a folded loop of circular DNA that is not enclosed by a membrane, a small "
    "ring-shaped plasmid and many small 70S ribosomes. Pili project from the top end and a flagellum extends from the "
    "bottom end.",
    "A typical bacterium. Labels marked * (pili, capsule, plasmid, flagellum) are found in some bacteria only; every "
    "bacterium has a cell wall, a cell surface membrane, circular DNA and 70S ribosomes, and no nucleus.", "fig small"))
problems.extend(f.check())

# ---------- viruses ----------
f = Fig("viruses")
f.text(10, 16, "Non-enveloped virus", "tl tb")
hexa = [(95 + 40 * math.cos(math.pi / 6 + k * math.pi / 3), 80 + 40 * math.sin(math.pi / 6 + k * math.pi / 3)) for k in range(6)]
f.poly(hexa, "f1 s-acc sw2")
hexa2 = [(95 + 30 * math.cos(math.pi / 6 + k * math.pi / 3), 80 + 30 * math.sin(math.pi / 6 + k * math.pi / 3)) for k in range(6)]
f.poly(hexa2, "fp ln", check=False)
core = [(95 + (14 + 3 * math.sin(4 * t)) * math.cos(t), 80 + (14 + 3 * math.sin(4 * t)) * math.sin(t)) for t in [2 * math.pi * k / 40 for k in range(41)]]
f.smooth(core, "c3 sw2", True, check=False)
X0 = 160
f.label(X0, 66, "capsid (protein)", (X0 - 4, 63), (130, 70), "start")
f.text(X0, 94, "nucleic acid core", "tl"); f.text(X0, 108, "(DNA or RNA)", "tl")
f.line([(X0 - 4, 98), (109, 83)], "ln-m thin", check=False); f.leads.append(((X0 - 4, 98), (109, 83), "nucleic acid core"))
# enveloped virus
f.text(10, 150, "Enveloped virus", "tl tb")
ox, oy = 95, 235
f.ellipse(ox, oy, 56, 56, "f2 s-acc2 sw2")                          # envelope: phospholipid layer
f.ellipse(ox, oy, 48, 48, "fp ln", check=False)
for k in range(12):                                                  # attachment proteins in the envelope
    a = 2 * math.pi * k / 12
    f.line([(ox + 56 * math.cos(a), oy + 56 * math.sin(a)), (ox + 70 * math.cos(a), oy + 70 * math.sin(a))], "ln thick", check=False)
hexb = [(ox + 32 * math.cos(math.pi / 6 + k * math.pi / 3), oy + 32 * math.sin(math.pi / 6 + k * math.pi / 3)) for k in range(6)]
f.poly(hexb, "f1 s-acc sw2", check=False)
coreb = [(ox + (13 + 3 * math.sin(4 * t)) * math.cos(t), oy + (13 + 3 * math.sin(4 * t)) * math.sin(t)) for t in [2 * math.pi * k / 40 for k in range(41)]]
f.smooth(coreb, "c3 sw2", True, check=False)
f.label(X0 + 16, 190, "envelope", (X0 + 12, 187), (ox + 52 * math.cos(-0.5), oy + 52 * math.sin(-0.5)), "start")
f.label(X0 + 16, 218, "capsid (protein)", (X0 + 12, 215), (ox + 28 * math.cos(-0.2), oy + 28 * math.sin(-0.2)), "start")
f.label(X0 + 16, 246, "nucleic acid core", (X0 + 12, 243), (ox + 12, oy + 3), "start")
f.label(X0 + 16, 274, "attachment proteins", (X0 + 12, 271), (ox + 66 * math.cos(0.7), oy + 66 * math.sin(0.7)), "start")
figs.append(f.svg((350, 306),
    "Two virus particles. Top: a non-enveloped virus, a hexagonal protein capsid enclosing a core of nucleic acid, DNA or "
    "RNA. Bottom: an enveloped virus, with the same capsid and nucleic acid core inside an outer envelope made of "
    "phospholipid that carries attachment proteins.",
    "All viruses have a nucleic acid core (DNA or RNA) inside a protein capsid. Some also have an outer envelope of "
    "phospholipid. None is a cell.", "fig small"))
problems.extend(f.check())

finish(figs, problems)
