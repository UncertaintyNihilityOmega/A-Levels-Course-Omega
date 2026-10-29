# data/fig_bio.inheritance.py: builds the hand-drawn pedigree SVGs of chapters/bio.inheritance.md and checks label clearance.
# Run: py data/fig_bio.inheritance.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.inheritance replaces the @@FIG_<NAME> placeholder lines of the chapter (later runs refresh them).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["PED1", "PED2"]
figs, problems = [], []
AFF, UNAFF = "fa s-acc sw2", "fp ln"
ROWS = {1: 52, 2: 132, 3: 212}


def sym(f, x, gen, sex, aff, num):
    y = ROWS[gen]
    cls = AFF if aff else UNAFF
    if sex == "m":
        f.rect(x - 12, y - 12, 24, 24, cls)
    else:
        f.circle(x, y, 12, cls)
    f.text(x, y + 28, str(num), "tl", "middle")


def marry(f, x1, x2, gen):
    f.line([(x1 + 12, ROWS[gen]), (x2 - 12, ROWS[gen])], "ln")


def sibs(f, parent_mid, gen_parent, xs):
    ypar = ROWS[gen_parent]
    ybar = ypar + 40
    ychild = ROWS[gen_parent + 1] - 12
    f.line([(parent_mid, ypar), (parent_mid, ybar)], "ln", check=False)
    f.line([(min(xs + [parent_mid]), ybar), (max(xs + [parent_mid]), ybar)], "ln", check=False)
    for x in xs:
        f.line([(x, ybar), (x, ychild)], "ln", check=False)


def pedigree(name, label, caption, people, vb=(330, 292)):
    f = Fig(name)
    for g, r in ((1, "I"), (2, "II"), (3, "III")):
        f.text(8, ROWS[g] + 4, r, "tl tb")
    sibs(f, 140, 1, [50, 110, 170])
    sibs(f, 200, 2, [170, 230])
    marry(f, 110, 170, 1)
    marry(f, 170, 230, 2)
    for (x, gen, sex, aff, num) in people:
        sym(f, x, gen, sex, aff, num)
    # key
    ky = 268
    f.rect(8, ky - 10, 20, 20, UNAFF)
    f.text(34, ky + 4, "male")
    f.circle(106, ky, 10, UNAFF)
    f.text(122, ky + 4, "female")
    f.rect(184, ky - 10, 20, 20, AFF)
    f.text(210, ky + 4, "affected")
    f.vb = vb
    figs.append(f.svg(vb, label, caption))
    problems.extend(f.check())


# generation I: men at x=110, women at x=170; II: siblings 50, 110, 170 and the partner at 230; III: children 170, 230
pedigree("ped1",
         "A pedigree of three generations. Generation I: an unaffected man (1) and an unaffected woman (2). Their children in "
         "generation II are an unaffected daughter (1), an affected son (2) and an unaffected daughter (3). Daughter II-3 has "
         "an unaffected partner (4). Their children in generation III are an unaffected son (1) and an affected daughter (2).",
         "A pedigree: squares are males, circles are females, shaded symbols are affected, a horizontal line joins "
         "partners and the vertical lines lead to their children. Each generation has a roman numeral and each person "
         "a number, so II-3 is the third person in generation II.",
         [(110, 1, "m", False, 1), (170, 1, "f", False, 2),
          (50, 2, "f", False, 1), (110, 2, "m", True, 2), (170, 2, "f", False, 3), (230, 2, "m", False, 4),
          (170, 3, "m", False, 1), (230, 3, "f", True, 2)])

pedigree("ped2",
         "A pedigree of three generations. Generation I: an unaffected man (1) and an unaffected woman (2). Their children in "
         "generation II are an affected son (1), an unaffected son (2) and an unaffected daughter (3). Daughter II-3 has "
         "an unaffected partner (4). Their children in generation III are an affected son (1) and an unaffected daughter (2).",
         "A second pedigree for the exam practice. Squares are males, circles are females and shaded symbols are affected.",
         [(110, 1, "m", False, 1), (170, 1, "f", False, 2),
          (50, 2, "m", True, 1), (110, 2, "m", False, 2), (170, 2, "f", False, 3), (230, 2, "m", False, 4),
          (170, 3, "m", True, 1), (230, 3, "f", False, 2)])

print("\n\n".join(figs))
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
