# checks/bio.genecontrol.py: recomputes every number in the Genes, phenotype and gene control chapter.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data'))
from math import isclose
from fractions import Fraction
from codon_table import CODE, transcribe

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def is_(label, got, want):
    global n
    n += 1
    assert got == want, f"{label}: computed {got!r}, chapter says {want!r}"


# --- Genetic code facts used in the chapter ---------------------------------------------------------------
is_("GAG is glutamic acid", CODE["GAG"], "Glu")
is_("GUG is valine", CODE["GUG"], "Val")
is_("UAU is tyrosine", CODE["UAU"], "Tyr")
is_("UAA is a stop codon", CODE["UAA"], "STOP")
is_("UAU -> UAA is one base change", sum(a != b for a, b in zip("UAU", "UAA")), 1)
is_("GAG -> GUG is one base change", sum(a != b for a, b in zip("GAG", "GUG")), 1)
is_("CAG is glutamine", CODE["CAG"], "Gln")
is_("GAA is glutamic acid (silent change from GAG)", CODE["GAA"], "Glu")
is_("template CTC -> GAG", transcribe("CTC"), "GAG")
is_("template CAC -> GUG", transcribe("CAC"), "GUG")

# --- Crosses ----------------------------------------------------------------------------------------------
gam = ["Le", "le"]
kids = [(a, b) for a in gam for b in gam]
tall = sum(1 for a, b in kids if "Le" in (a, b))
is_("pea cross 3 tall : 1 dwarf", (tall, len(kids) - tall), (3, 1))
is_("albinism 1 in 4", Fraction(1, 4), Fraction(1, 2) * Fraction(1, 2))
# haemophilia: carrier mother x normal father
mother = ["XH", "Xh"]
father = ["XH", "Y"]
kids = [(a, b) for a in mother for b in father]
sons = [k for k in kids if "Y" in k]
is_("half of sons affected", sum(1 for k in sons if "Xh" in k), 1)
is_("two sons among four children", len(sons), 2)
# man with haemophilia x non-carrier woman: all daughters carriers, no son affected
mother = ["XH", "XH"]
father = ["Xh", "Y"]
kids = [(a, b) for a in mother for b in father]
is_("all daughters carriers", all("Xh" in k for k in kids if "Y" not in k), True)
is_("no son affected", any("Xh" in k for k in kids if "Y" in k), False)
# woman whose brother has haemophilia (mother a carrier, father normal)
is_("woman is a carrier with p 1/2", Fraction(1, 2), Fraction(1, 2))
is_("boy with haemophilia from a carrier mother", Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4))
eq("100 - 41 = 59", 100 - 41, 59)

# --- lac operon data (worked example) ----------------------------------------------------------------------
t = [0, 5, 10, 15, 20, 25, 30, 40]
act = [2, 2, 2, 14, 60, 118, 160, 200]
d = dict(zip(t, act))
eq("fold increase 2 -> 200", d[40] / d[0], 100)
eq("rate 15-25 min", (d[25] - d[15]) / 10, 10.4)
is_("lactose added after the third sample", t[2], 10)

# --- Exam practice tables ----------------------------------------------------------------------------------
lac = {1: (2, 180), 2: (170, 175), 3: (2, 2), 4: (165, 170)}
is_("strain 3 never induced", lac[3][0] == lac[3][1], True)
is_("strains 2 and 4 high without lactose", min(lac[2][0], lac[4][0]) > 100, True)
is_("strain 1 inducible", lac[1][1] > 10 * lac[1][0], True)
rep = [40, 43, 46, 50, 55]
age = [59, 47, 38, 30, 22]
is_("age falls as repeats rise", all(a > b for a, b in zip(age, age[1:])), True)
eq("onset 59 at 40 repeats and 22 at 55", age[0] - age[-1], 37)

print("ok")
