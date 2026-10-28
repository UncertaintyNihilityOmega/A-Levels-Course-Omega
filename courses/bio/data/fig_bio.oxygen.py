# data/fig_bio.oxygen.py: builds the hand-drawn SVG figures of chapters/bio.oxygen.md and checks label clearance.
# Run: py data/fig_bio.oxygen.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.oxygen replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["COOP", "REDCELL"]
figs, problems = [], []
EMPTY = "fm s-acc sw2"
FULL = "f2 s-acc2 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


# ---------- 1. cooperative binding: four stages of loading ----------
f = Fig("coop")
rows = [("1  First O₂ binds slowly", 0, 0, 23),
        ("2  Shape changes: 2nd, 3rd bind easily", 1, 0, 26),
        ("3  Fourth O₂ binds slowly", 3, 0, 26),
        ("4  Fully saturated: 4 O₂ bound", 4, 0, 26)]
for k, (title, nbound, _, r) in enumerate(rows):
    oy = k * 108
    f.text(10, oy + 16, title, "tl tb")
    cy = oy + 78
    xs = [38, 96, 154, 212]
    for i, x in enumerate(xs):
        full = i < nbound
        ellipse(f, x, cy, r, r, FULL if full else EMPTY)
        f.text(x, cy + 4, "O₂" if full else "haem", "tl", "middle")
    # incoming O2 arrows on the subunits that are about to bind (one in row 1, two in row 2, one in row 3)
    inc = {0: [0], 1: [1, 2], 2: [3]}.get(k, [])
    for i in inc:
        f.line([(xs[i], cy - r - 20), (xs[i], cy - r - 6)], "c1 sw2", "ah", check=False)
        f.text(xs[i] + 8, cy - r - 8, "O₂", "tl")
done(f, (300, 440),
     "Four stages of oxygen loading onto haemoglobin, shown as four subunits each with a haem group. Stage 1: all four haem groups are empty and the first oxygen molecule binds slowly. Stage 2: one oxygen is bound, the subunits have changed shape and the second and third oxygen molecules bind easily. Stage 3: three oxygen molecules are bound and the fourth binds slowly because few sites are left. Stage 4: all four haem groups carry oxygen.",
     "Cooperative binding. The first oxygen to bind changes the shape of haemoglobin (the circles widen), so the second and third bind easily; the fourth binds slowly because there is only one vacant haem group to find.")

# ---------- 2. red blood cell: carbon dioxide transport in the tissues ----------
f = Fig("redcell")
cx, cy, rx, ry = 300, 150, 140, 95
ellipse(f, cx, cy, rx, ry, "fm s-acc sw2")
inside = [(100, "CO₂ + H₂O ⇌ H₂CO₃"), (114, "(carbonic anhydrase)"), (140, "H₂CO₃ ⇌ H⁺ + HCO₃⁻"),
          (166, "H⁺ + Hb → HHb"), (180, "(haemoglobinic acid)"), (204, "CO₂ + Hb → HbCO₂"), (218, "(carbaminohaemoglobin)")]
for y, s in inside:
    f.text(cx, y, s, "tl", "middle")
f.text(20, 24, "red blood cell", "tl tb")
f.leader((72, 32), (186, 94))
f.text(590, 24, "plasma carries HCO₃⁻ and some dissolved CO₂", "tl", "end")
f.line([(20, 132), (146, 132)], "c3 sw2", "ah")
f.text(20, 120, "CO₂ from the tissue", "tl")
f.line([(452, 124), (570, 124)], "c3 sw2", "ah")
f.text(452, 112, "HCO₃⁻ to plasma", "tl")
f.line([(570, 176), (452, 176)], "c4 sw2", "ah")
f.text(580, 198, "Cl⁻ moves in", "tl", "end"); f.text(580, 212, "(chloride shift)", "tl", "end")
f.line([(212, 228), (160, 268)], "c1 sw2", "ah")
f.text(10, 284, "O₂ unloaded from oxyhaemoglobin", "tl")
done(f, (600, 296),
     "A red blood cell in a respiring tissue. Carbon dioxide diffuses into the cell. Inside, carbonic anhydrase catalyses carbon dioxide plus water forming carbonic acid, which dissociates into hydrogen ions and hydrogen carbonate ions. Hydrogen ions combine with haemoglobin to form haemoglobinic acid. Some carbon dioxide combines with haemoglobin to form carbaminohaemoglobin. Hydrogen carbonate ions leave the cell into the plasma and chloride ions move in, the chloride shift. Oxygen is unloaded from oxyhaemoglobin.",
     "Carbon dioxide transport in the tissues. In the lungs every step runs in reverse: hydrogen carbonate ions enter the cell, chloride ions leave, and carbon dioxide is released and diffuses into the alveolus.",
     "fig")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
