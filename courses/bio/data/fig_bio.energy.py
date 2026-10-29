# data/fig_bio.energy.py: builds the hand-drawn SVG figures of chapters/bio.energy.md and checks label clearance.
# Run: py data/fig_bio.energy.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.energy replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, arc_pts

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["ATP", "RESP"]
figs, problems = [], []


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def hexagon(f, cx, cy, r, cls):
    pts = [(cx + r * math.cos(math.radians(60 * k)), cy + r * math.sin(math.radians(60 * k))) for k in range(6)]
    f.poly([(round(x, 1), round(y, 1)) for x, y in pts], cls)


def pentagon(f, cx, cy, r, cls):
    pts = [(cx + r * math.cos(math.radians(-90 + 72 * k)), cy + r * math.sin(math.radians(-90 + 72 * k))) for k in range(5)]
    f.poly([(round(x, 1), round(y, 1)) for x, y in pts], cls)


def nucleotide_row(f, y, phosphates, free_pi=None):
    """adenine hexagon, ribose pentagon and a chain of phosphate circles at height y."""
    hexagon(f, 36, y, 19, "f1 s-acc sw2")
    f.text(36, y + 5, "A", "tl tb", "middle")
    f.line([(55, y), (70, y)], "ln")
    pentagon(f, 92, y, 22, "fm s-acc sw2")
    f.line([(112, y + 2), (134, y)], "ln")
    x = 150
    for k in range(phosphates):
        f.circle(x, y, 15, "f2 s-acc2 sw2")
        f.text(x, y + 5, "P", "tl tb", "middle")
        if k < phosphates - 1:
            f.line([(x + 15, y), (x + 25, y)], "ln")
        x += 40
    if free_pi:
        f.circle(free_pi, y, 15, "f2 s-acc2 sw2")
        f.text(free_pi, y + 5, "P", "tl tb", "middle")


# ---------- 1. ATP hydrolysis and synthesis ----------
f = Fig("atp")
f.text(10, 16, "ATP", "tl tb")
nucleotide_row(f, 52, 3)
f.line([(120, 90), (120, 160)], "c1 sw2", "ah")
f.text(106, 104, "hydrolysis", "tl", "end")
f.text(106, 120, "(+ H₂O)", "tl", "end")
f.text(106, 140, "energy", "tl", "end")
f.text(106, 156, "released", "tl", "end")
f.line([(300, 160), (300, 90)], "c3 sw2", "ah")
f.text(290, 104, "ATP rebuilt", "tl", "end")
f.text(290, 120, "using energy", "tl", "end")
f.text(290, 136, "from respiration", "tl", "end")
f.text(10, 184, "ADP + Pi", "tl tb")
nucleotide_row(f, 218, 2, free_pi=290)
f.text(36, 266, "adenine", "tl", "middle")
f.leader((36, 252), (36, 230))
f.text(100, 266, "ribose", "tl", "middle")
f.leader((100, 252), (96, 230))
f.text(190, 266, "2 phosphate", "tl", "middle")
f.text(190, 280, "groups", "tl", "middle")
f.leader((190, 252), (190, 234))
f.text(290, 266, "Pi", "tl", "middle")
f.leader((290, 252), (290, 234))
done(f, (340, 292),
     "ATP is adenine, ribose and three phosphate groups. Hydrolysis of ATP with water removes the end phosphate group to give ADP and an inorganic phosphate ion, Pi, and releases energy. A downward arrow from ATP to ADP plus Pi is labelled hydrolysis, plus water, energy released. An upward arrow back to ATP is labelled ATP rebuilt using energy from respiration.",
     "ATP is hydrolysed to ADP and inorganic phosphate (Pi), releasing about 30.5 kJ per mole. Respiration supplies the energy to join Pi back on to ADP, so the same molecules are recycled all the time.")

# ---------- 2. respirometer ----------
f = Fig("resp")
# water bath and tube
f.rect(140, 135, 150, 130, "fp ln")
f.rect(141, 160, 148, 104, "fm s-acc sw2")
f.line([(141, 160), (289, 160)], "ln-m thin dash")
f.poly([(170, 74), (170, 205), (180, 225), (250, 225), (260, 205), (260, 74)], "fp ln", closed=False)
f.poly([(171, 200), (259, 200), (259, 205), (250, 224), (180, 224), (171, 205)], "f2 s-acc2 sw2", check=False)
f.line([(172, 170), (258, 170)], "ln thick")
for sx in (187, 202, 217, 232, 247):
    f.circle(sx, 163, 6, "fa s-acc sw2")
f.rect(165, 58, 100, 16, "fi")
# capillary, ruler and drop
f.line([(215, 58), (215, 40), (395, 40)], "ln thick", check=False)
f.line([(332, 40), (348, 40)], "c1 sw3", check=False)
f.rect(235, 52, 160, 12, "fp ln")
for tx in range(240, 395, 10):
    f.line([(tx, 52), (tx, 57 if (tx - 240) % 50 else 60)], "ln-m thin", check=False)
# labels
f.text(125, 68, "bung", "tl", "end")
f.leader((129, 64), (164, 66))
f.text(125, 104, "boiling tube", "tl", "end")
f.leader((129, 100), (170, 100))
f.text(125, 150, "germinating seeds", "tl", "end")
f.leader((129, 146), (182, 160))
f.text(125, 190, "gauze platform", "tl", "end")
f.leader((129, 186), (178, 171))
f.text(125, 232, "KOH solution", "tl", "end")
f.text(125, 246, "(absorbs CO₂)", "tl", "end")
f.leader((129, 228), (190, 214))
f.text(305, 255, "water bath", "tl")
f.leader((301, 251), (282, 251))
f.text(170, 22, "capillary tube", "tl")
f.leader((205, 27), (214, 42))
f.text(340, 22, "fluid drop", "tl", "middle")
f.leader((340, 27), (340, 38))
f.text(395, 86, "millimetre scale", "tl", "end")
f.leader((350, 74), (350, 65))
f.line([(390, 104), (300, 104)], "c3 sw2", "ah")
f.text(395, 124, "drop moves", "tl", "end")
f.text(395, 138, "towards tube", "tl", "end")
done(f, (410, 280),
     "A simple respirometer. A boiling tube stands in a water bath. Germinating seeds rest on a gauze platform above potassium hydroxide solution, which absorbs carbon dioxide. A bung closes the tube and a capillary tube leaves it, with a drop of coloured fluid in the capillary and a millimetre scale beneath. An arrow shows the drop moving towards the tube as oxygen is taken up.",
     "A simple respirometer. The seeds take in oxygen, the potassium hydroxide absorbs the carbon dioxide, so the gas volume falls and the drop moves towards the tube. Replace the potassium hydroxide with water and the drop shows only the net change in volume. A second tube with glass beads, or boiled seeds, acts as a control.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
