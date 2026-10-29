# data/fig_bio.genetech2.py: figure of chapters/bio.genetech2.md (ex vivo gene therapy). Run: py data/fig_bio.genetech2.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit_p18 import Fig, place, report

f = Fig("therapy")
steps = [
    ("1  Stem cells or T-lymphocytes", "removed from the patient's blood", "f1 s-acc sw2"),
    ("2  Working ADA gene added to the", "cells, using a virus as the vector", "f1 s-acc sw2"),
    ("3  Cells grown in the laboratory;", "gene expression checked", "f1 s-acc sw2"),
    ("4  Modified cells returned to the", "patient by infusion into the blood", "f1 s-acc sw2"),
    ("5  Cells divide and make the working", "enzyme inside the patient's body", "f2 s-acc2 sw2"),
]
tops = [8 + 68 * k for k in range(5)]
for t, (a, b, cls) in zip(tops, steps):
    f.rect(10, t, 320, 46, cls, rx=6)
    f.text(170, t + 19, a, "tl", "middle")
    f.text(170, t + 35, b, "tl", "middle")
for t in tops[:4]:
    f.line([(170, t + 46), (170, t + 66)], "ln", "ah", check=False)
fig = f.svg((340, 334),
    "Flow diagram in five boxes joined by downward arrows. 1: stem cells or T-lymphocytes are removed from the patient's blood. 2: a working ADA gene is added to the cells using a virus as the vector. 3: the cells are grown in the laboratory and gene expression is checked. 4: the modified cells are returned to the patient by infusion into the blood. 5: the cells divide and make the working enzyme inside the patient's body.",
    "Ex vivo gene therapy for ADA-deficient SCID: the cells are treated outside the body and then returned.")
report([f])
place("bio.genetech2", {"therapy": fig})
