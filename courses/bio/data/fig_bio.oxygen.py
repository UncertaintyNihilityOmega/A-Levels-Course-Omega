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
f = Fig("redcell")      # REVIEW P6/P8/P9: redrawn 340 wide (the 600-wide version had 5 px labels on phones)
cx, cy, rx, ry = 170, 176, 140, 96
ellipse(f, cx, cy, rx, ry, "fm s-acc sw2")
inside = [(120, "CO₂ + H₂O ⇌ H₂CO₃"), (134, "(carbonic anhydrase)"), (160, "H₂CO₃ ⇌ H⁺ + HCO₃⁻"),
          (186, "H⁺ + Hb → HHb"), (200, "(haemoglobinic acid)"), (224, "CO₂ + Hb → HbCO₂"), (238, "(carbaminohaemoglobin)")]
for y, s in inside:
    f.text(cx, y, s, "tl", "middle")
f.text(cx, 20, "red blood cell", "tl tb", "middle")
f.leader((cx, 28), (cx, cy - ry + 2))
f.text(10, 34, "CO₂ from", "tl"); f.text(10, 48, "the tissue", "tl")
f.line([(34, 58), (64, 104)], "c3 sw2", "ah")
f.text(330, 34, "HCO₃⁻ to", "tl", "end"); f.text(330, 48, "the plasma", "tl", "end")
f.line([(276, 104), (306, 58)], "c3 sw2", "ah")
f.line([(306, 298), (276, 252)], "c4 sw2", "ah")
f.text(330, 314, "Cl⁻ moves in", "tl", "end"); f.text(330, 328, "(chloride shift)", "tl", "end")
f.line([(64, 252), (34, 298)], "c1 sw2", "ah")
f.text(10, 314, "O₂ unloaded from", "tl"); f.text(10, 328, "oxyhaemoglobin", "tl")
f.text(cx, 352, "the plasma carries HCO₃⁻ and some dissolved CO₂", "tl", "middle")
done(f, (340, 362),
     "A red blood cell in a respiring tissue. Carbon dioxide diffuses into the cell. Inside, carbonic anhydrase catalyses carbon dioxide plus water forming carbonic acid, which dissociates into hydrogen ions and hydrogen carbonate ions. Hydrogen ions combine with haemoglobin to form haemoglobinic acid. Some carbon dioxide combines with haemoglobin to form carbaminohaemoglobin. Hydrogen carbonate ions leave the cell into the plasma and chloride ions move in, the chloride shift. Oxygen is unloaded from oxyhaemoglobin.",
     "Carbon dioxide transport in the tissues. In the lungs every step runs in reverse: hydrogen carbonate ions enter the cell, chloride ions leave, and carbon dioxide is released and diffuses into the alveolus.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
