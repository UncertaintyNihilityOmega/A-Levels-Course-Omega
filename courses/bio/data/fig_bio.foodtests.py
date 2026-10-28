# data/fig_bio.foodtests.py: hand-drawn SVG figures of chapters/bio.foodtests.md with a label-clearance check.
# Run: py data/fig_bio.foodtests.py > scratch/foodtests_figs.txt (figures on stdout, clearance report on stderr).
import sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p4 import Fig

figs = []

# ---------- Figure 1: Benedict's colour ladder (bar length grows with the amount of reducing sugar) ----------
f = Fig("benedict")
f.text(10, 18, "After heating with Benedict's solution", "tl tb")
rows = [("blue", "none: negative result", 30),
        ("green", "very low concentration", 80),
        ("yellow", "low concentration", 130),
        ("orange", "medium concentration", 190),
        ("brick-red", "high concentration", 270)]
y = 52
for name, amount, w in rows:
    f.text(10, y, name, "tl tb")
    f.text(100, y, amount, "tl")
    f.rect(10, y + 8, w, 12, "f1 s-acc sw2")
    y += 44
f.text(10, y - 8, "longer bar = more reducing sugar", "tl")
figs.append(f.svg((330, y + 8),
    "Colour ladder for Benedict's test. From top to bottom: blue means no reducing sugar, green a very low concentration, "
    "yellow a low concentration, orange a medium concentration and brick-red a high concentration. The bar under each "
    "name gets longer as the amount of reducing sugar rises.",
    "The colour after heating Benedict's solution with a sample. Each step is named, because a figure must not rely on "
    "colour alone. The longer the bar, the more reducing sugar was in the sample."))
f.problems = f.check()

# ---------- Figure 2: decision flow for sugars ----------
g = Fig("sugarflow")
g.rect(10, 8, 170, 36, "f1 s-acc sw2", 6)
g.text(95, 30, "Benedict's test", "tl", "middle")
g.line([(180, 26), (246, 26)], "ln", "ah")
g.text(188, 18, "positive", "tl")
g.rect(248, 6, 110, 40, "f2 s-acc2 sw2", 6)
g.text(303, 22, "reducing", "tl", "middle")
g.text(303, 36, "sugar present", "tl", "middle")
g.line([(95, 44), (95, 86)], "ln", "ah")
g.text(104, 70, "negative", "tl")
g.rect(10, 88, 170, 62, "f1 s-acc sw2", 6)
g.text(95, 106, "Fresh sample: boil", "tl", "middle")
g.text(95, 120, "with dilute acid,", "tl", "middle")
g.text(95, 134, "neutralise, retest", "tl", "middle")
g.line([(180, 119), (246, 119)], "ln", "ah")
g.text(188, 111, "positive", "tl")
g.rect(248, 99, 110, 40, "f2 s-acc2 sw2", 6)
g.text(303, 115, "non-reducing", "tl", "middle")
g.text(303, 129, "sugar present", "tl", "middle")
g.line([(95, 150), (95, 192)], "ln", "ah")
g.text(104, 176, "negative", "tl")
g.rect(10, 194, 170, 32, "f3 s-acc sw2", 6)
g.text(95, 214, "no sugar detected", "tl", "middle")
figs.append(g.svg((368, 236),
    "Flow chart for testing a sample for sugars. Heat the sample with Benedict's solution: a positive result means a "
    "reducing sugar is present. If it is negative, boil a fresh sample with dilute acid, neutralise it and test again: a "
    "positive result now means a non-reducing sugar is present, and a negative result means no sugar was detected.",
    "The order of the sugar tests. The acid step is only done after a negative first Benedict's test, using a fresh "
    "sample of the same solution."))
g.problems = g.check()

for s in figs:
    print(s)
    print()
bad = f.problems + g.problems
print("\n".join(bad) if bad else "clearance ok", file=sys.stderr)
