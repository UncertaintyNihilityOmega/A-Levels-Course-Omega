# data/fig_bio.glucose.py: builds the hand-drawn SVG figures of chapters/bio.glucose.md and checks label clearance.
# Run: py data/fig_bio.glucose.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.glucose replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["FEEDBACK", "CASCADE", "STRIP", "SENSOR"]
figs, problems = [], []
BOX = "f1 s-acc sw2"
ARR = "c1 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def box(f, x, y, w, h, lines, cls=BOX, bold_first=False):
    f.rect(x, y, w, h, cls)
    n = len(lines)
    for i, s in enumerate(lines):
        yy = y + h / 2 + 5 + (i - (n - 1) / 2) * 15
        f.text(x + w / 2, round(yy, 1), s, "tl tb" if (bold_first and i == 0) else "tl", "middle")


# ---------- 1. blood glucose feedback ----------
f = Fig("feedback")
cols = [(5, "glucose too high",
         [["blood glucose", "rises after a meal"], ["β cells secrete", "insulin"],
          ["liver and muscle", "cells take up glucose", "and make glycogen"], ["blood glucose falls", "to the set point"]]),
        (175, "glucose too low",
         [["blood glucose", "falls between meals"], ["α cells secrete", "glucagon"],
          ["liver cells break", "down glycogen and", "release glucose"], ["blood glucose rises", "to the set point"]])]
for (x0, head, boxes) in cols:
    f.text(x0 + 80, 20, head, "tl tb", "middle")
    for i, lines in enumerate(boxes):
        y = 34 + i * 80
        box(f, x0, y, 160, 56, lines)
        if i < len(boxes) - 1:
            f.line([(x0 + 80, y + 56), (x0 + 80, y + 80)], ARR, "ah")
f.text(170, 352, "negative feedback: each change is reversed", "tl", "middle")
done(f, (340, 364),
     "Two columns of four boxes with downward arrows. Left column, glucose too high: blood glucose rises after a meal; beta cells secrete insulin; liver and muscle cells take up glucose and make glycogen; blood glucose falls to the set point. Right column, glucose too low: blood glucose falls between meals; alpha cells secrete glucagon; liver cells break down glycogen and release glucose; blood glucose rises to the set point.",
     "Negative feedback control of blood glucose. Insulin lowers a high concentration; glucagon raises a low one. Each response reverses the change that caused it.")

# ---------- 2. glucagon cascade ----------
f = Fig("cascade")
f.circle(30, 22, 8, "fr ln")
f.text(46, 27, "glucagon (outside the cell)", "tl")
f.line([(30, 30), (30, 46)], ARR, "ah")
f.rect(82, 58, 168, 32, "f2 s-acc2 sw2")
f.text(166, 79, "cell surface membrane", "tl", "middle")
f.rect(10, 46, 72, 56, "fm s-acc sw2")
f.text(46, 79, "receptor", "tl", "middle")
f.rect(250, 46, 80, 56, "fm s-acc sw2")
f.text(290, 70, "adenylyl", "tl", "middle")
f.text(290, 85, "cyclase", "tl", "middle")
ellipse(f, 150, 126, 50, 20, "fm s-acc sw2")
f.text(150, 131, "G-protein", "tl", "middle")
f.line([(50, 104), (104, 120)], ARR, "ah")
f.line([(194, 118), (268, 103)], ARR, "ah")
f.text(150, 162, "receptor activates G-protein,", "tl", "middle")
f.text(150, 176, "which stimulates the enzyme", "tl", "middle")
# cytoplasm cascade
names = [["cAMP", "second messenger"], ["protein kinase A", "activated by cAMP"], ["enzyme 1", "phosphorylated: active"],
         ["enzyme 2", "phosphorylated: active"], ["glycogen phosphorylase", "final enzyme: active"],
         ["glycogen → glucose", "released into the blood"]]
y0 = 214
for i, lines in enumerate(names):
    y = y0 + i * 62
    box(f, 100, y, 230, 40, lines, "f2 s-acc2 sw2" if i == 4 else BOX, bold_first=True)
    if i < len(names) - 1:
        f.line([(215, y + 40), (215, y + 62)], ARR, "ah")
f.line([(290, 102), (290, 212)], ARR, "ah")
f.text(282, 200, "ATP → cAMP", "tl", "end")
f.line([(90, 236), (90, 500)], "c2 sw2", "ah")
for k, t in enumerate(["signal", "amplified", "at each", "step"]):
    f.text(6, 362 + 14 * k, t, "tl")
done(f, (340, 578),
     "How glucagon acts on a liver cell. Glucagon outside the cell binds to a receptor in the cell surface membrane. The receptor activates a G-protein, which stimulates the enzyme adenylyl cyclase in the membrane. Adenylyl cyclase converts ATP to cyclic AMP, the second messenger. Below, in the cytoplasm, boxes joined by arrows show the enzyme cascade: cyclic AMP activates protein kinase A, which phosphorylates enzyme 1, which phosphorylates enzyme 2, which activates the final enzyme, glycogen phosphorylase, which breaks down glycogen to glucose that is released into the blood. A downward arrow beside the cascade is labelled signal amplified at each step.",
     "The glucagon signalling pathway in a liver cell. The hormone stays outside the cell; the second messenger, cAMP, carries the message to the enzyme cascade, which amplifies it.")

# ---------- 3. test strip ----------
f = Fig("strip")
box(f, 20, 10, 200, 36, ["glucose + oxygen"])
f.line([(120, 46), (120, 100)], ARR, "ah")
f.text(132, 78, "glucose oxidase", "tl")
box(f, 20, 104, 200, 44, ["gluconic acid +", "hydrogen peroxide"])
f.line([(120, 148), (120, 208)], ARR, "ah")
f.text(132, 170, "peroxidase", "tl")
f.text(132, 184, "+ chromogen", "tl")
f.text(132, 198, "(colourless)", "tl")
box(f, 20, 212, 200, 44, ["coloured product", "+ water"])
f.line([(120, 256), (120, 286)], ARR, "ah")
box(f, 20, 290, 200, 44, ["compare the colour", "with the chart"], "f2 s-acc2 sw2")
done(f, (340, 346),
     "Reactions on a glucose test strip. Glucose and oxygen react, catalysed by glucose oxidase, to give gluconic acid and hydrogen peroxide. The hydrogen peroxide reacts with a colourless chromogen, catalysed by peroxidase, to give a coloured product and water. The user compares the colour with a chart.",
     "The two enzymes of a test strip. The amount of coloured product depends on the amount of hydrogen peroxide, and so on the amount of glucose.")

# ---------- 4. biosensor ----------
f = Fig("sensor")
box(f, 20, 10, 210, 36, ["drop of blood on the strip"])
f.line([(125, 46), (125, 88)], ARR, "ah")
f.text(137, 72, "glucose is oxidised", "tl")
box(f, 20, 92, 210, 50, ["glucose oxidase,", "immobilised on an electrode"])
f.line([(125, 142), (125, 184)], ARR, "ah")
f.text(137, 168, "electrons pass", "tl")
box(f, 20, 188, 210, 50, ["electric current:", "more glucose, more current"])
f.line([(125, 238), (125, 280)], ARR, "ah")
f.text(137, 264, "transducer and meter", "tl")
box(f, 20, 284, 210, 50, ["number on the display:", "glucose concentration"], "f2 s-acc2 sw2")
done(f, (340, 346),
     "How a glucose biosensor works. A drop of blood is placed on the strip. Glucose is oxidised by glucose oxidase that is immobilised on an electrode. Electrons pass to the electrode and produce an electric current, which is greater when there is more glucose. A transducer and meter convert the current to a number on the display, the glucose concentration.",
     "A glucose biosensor. The current is proportional to the glucose concentration, so the meter can display a number.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
