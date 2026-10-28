# data/fig_bio.disease.py: builds the hand-drawn SVG figures of chapters/bio.disease.md and checks label clearance.
# Run: py data/fig_bio.disease.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.disease replaces the @@FIG_<NAME> placeholder lines of the chapter (and refreshes them later).
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["FAECAL", "VECTOR"]
figs, problems = [], []
BOX = "f1 s-acc sw2"
BOX2 = "f2 s-acc2 sw2"
FL = "c2 sw2"          # path of the pathogen (arrow class)


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def box(f, x, y, w, h, l1, l2, cls=BOX):
    f.rect(x, y, w, h, cls, 6)
    f.text(x + w / 2, y + h / 2 - 2, l1, "tl", "middle")
    f.text(x + w / 2, y + h / 2 + 13, l2, "tl", "middle")


# ---------- 1. the faecal-oral route of cholera ----------
f = Fig("faecal")
box(f, 10, 20, 110, 46, "person with", "cholera")
box(f, 220, 20, 110, 46, "faeces with", "bacteria", BOX2)
box(f, 220, 196, 110, 46, "water and food", "contaminated", BOX2)
box(f, 10, 196, 110, 46, "healthy person", "swallows them")
f.line([(122, 43), (216, 43)], FL, "ah")
f.text(169, 34, "diarrhoea", "tl", "middle")
f.line([(275, 70), (275, 192)], FL, "ah")
f.text(266, 124, "sewage, flood,", "tl", "end")
f.text(266, 138, "poor hygiene", "tl", "end")
f.line([(216, 219), (124, 219)], FL, "ah")
f.text(169, 210, "drinking", "tl", "middle")
f.line([(65, 192), (65, 70)], FL, "ah")
f.text(74, 126, "becomes"); f.text(74, 140, "infected")
done(f, (340, 256),
     "The faecal–oral route of cholera as a cycle. A person with cholera passes out faeces containing the bacteria; sewage, flood "
     "or poor hygiene lets the faeces contaminate water and food; a healthy person drinks or eats it and becomes infected.",
     "Cholera spreads in a cycle from faeces to mouth. Breaking the cycle at any point, with clean water, sewage treatment and "
     "hygiene, stops the disease spreading.")

# ---------- 2. malaria: the mosquito as a vector ----------
f = Fig("vector")
box(f, 20, 14, 150, 40, "person with", "malaria")
box(f, 20, 104, 150, 46, "female Anopheles", "mosquito (vector)", BOX2)
box(f, 20, 200, 150, 40, "healthy person", "now infected")
f.line([(95, 58), (95, 100)], FL, "ah")
f.line([(95, 154), (95, 196)], FL, "ah")
f.text(106, 72, "1  bite: the mosquito")
f.text(106, 86, "takes up the parasite")
f.text(106, 172, "2  bite: the parasite")
f.text(106, 186, "is injected")
done(f, (330, 254),
     "How malaria is passed on. A female Anopheles mosquito bites a person with malaria and takes up the parasite Plasmodium; "
     "when it bites a healthy person it injects the parasite, and that person becomes infected.",
     "The mosquito is the vector: it carries the pathogen from one person to the next. The pathogen is the protoctist Plasmodium, "
     "not the mosquito.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
