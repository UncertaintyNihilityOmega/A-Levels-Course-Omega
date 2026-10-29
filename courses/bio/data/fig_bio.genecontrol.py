# data/fig_bio.genecontrol.py: builds the hand-drawn SVG figures of chapters/bio.genecontrol.md and checks label clearance.
# Run: py data/fig_bio.genecontrol.py -> prints the <figure>s (clearance report on stderr). data/place_figs_p14.py bio.genecontrol places them.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["LAC", "GA"]
figs, problems = [], []

# ---------------------------------------------------------------- 1 lac operon off and on
f = Fig("lac")
X = dict(I=(10, 60), P=(72, 98), O=(98, 124), Z=(124, 188), Y=(188, 252), A=(252, 316))
H = 26


def strip(y0):
    f.rect(10, y0, 50, H, "fm2 s-acc sw2")
    f.text(35, y0 + 17, "lacI", "tl", "middle")
    f.rect(72, y0, 26, H, "f3 s-acc2 sw2")
    f.text(85, y0 + 17, "P", "tl", "middle")
    f.rect(98, y0, 26, H, "f2 s-acc2 sw2")
    f.text(111, y0 + 17, "O", "tl", "middle")
    for k, nm in (("Z", "lacZ"), ("Y", "lacY"), ("A", "lacA")):
        a, b = X[k]
        f.rect(a, y0, b - a, H, "f1 s-acc sw2")
        f.text((a + b) / 2, y0 + 17, nm, "tl", "middle")
    f.line([(60, y0 + 13), (72, y0 + 13)], "ln thick", check=False)


# panel 1: no lactose
f.text(10, 16, "1  No lactose: operon off", "tl tb")
y0 = 78
strip(y0)
f.rect(60, y0 - 20, 38, 20, "fm s-acc sw2", rx=8)                     # RNA polymerase bound at the promoter
f.circle(116, y0 - 12, 12, "fp s-acc sw2")                            # repressor sitting on the operator
f.text(4, y0 - 36, "RNA polymerase", "tl")
f.leader((60, y0 - 34), (68, y0 - 21))
f.text(136, y0 - 10, "repressor", "tl")
f.line([(104, y0 + 0), (104, y0 + 0)], "ln", check=False)
f.text(206, y0 - 34, "genes not", "tl")
f.text(206, y0 - 20, "transcribed", "tl")
f.text(4, y0 + 48, "regulatory gene", "tl")
f.leader((35, y0 + 28), (35, y0 + 37))
f.text(316, y0 + 48, "structural genes", "tl", "end")
f.leader((220, y0 + 28), (220, y0 + 37))
f.text(60, y0 + 68, "P promoter, O operator", "tl")

# panel 2: lactose present
oy = 168
f.text(10, oy + 16, "2  Lactose present: operon on", "tl tb")
y1 = oy + 100
strip(y1)
f.rect(60, y1 - 20, 38, 20, "fm s-acc sw2", rx=8)
f.line([(102, y1 - 10), (152, y1 - 10)], "c1 sw2", "ah")
f.text(4, y1 - 36, "RNA polymerase", "tl")
f.leader((60, y1 - 34), (68, y1 - 21))
f.circle(230, y1 - 40, 12, "fp s-acc sw2")                           # repressor with lactose, away from the operator
f.circle(245, y1 - 44, 5, "f3 s-acc2 sw2")                           # lactose
f.text(262, y1 - 44, "lactose", "tl")
f.text(176, y1 - 66, "repressor leaves", "tl")
# mRNA: zig-zag below the three structural genes
zig = [(130 + 5 * k, y1 + 38 + (5 if k % 2 else -5)) for k in range(0, 37)]
f.line(zig, "c2 sw2", check=False)
f.parts.append(f'<path class="ln-m thin" d="M156 {y1 + 28}L156 {y1 + 33}"/>')
f.text(4, y1 + 46, "one mRNA from", "tl")
f.text(4, y1 + 62, "lacZ, lacY, lacA", "tl")
f.text(316, y1 + 76, "translated: three proteins made", "tl", "end")
figs.append(f.svg((340, y1 + 88),
    "The lac operon in two panels. Each shows, from left to right, the regulatory gene lacI, the promoter P, the operator O and the structural genes lacZ, lacY and lacA. Panel 1, no lactose: the repressor protein sits on the operator next to RNA polymerase at the promoter, so the structural genes are not transcribed. Panel 2, lactose present: the repressor, with lactose bound, has left the operator, RNA polymerase moves along the structural genes and one mRNA is made from lacZ, lacY and lacA, which is translated into three proteins.",
    "The lac operon. In panel 1 the repressor protein, made from lacI, binds to the operator and blocks RNA polymerase. In panel 2 lactose binds to the repressor and changes its shape, so it leaves the operator and the structural genes are transcribed together."))
problems.extend(f.check())

# ---------------------------------------------------------------- 2 gibberellin, DELLA and transcription factors
g = Fig("ga")
def dna(y0, active):
    g.line([(10, y0 + 13), (330, y0 + 13)], "ln thick", check=False)
    g.rect(170, y0, 40, H, "f3 s-acc2 sw2")
    g.text(190, y0 + 17, "P", "tl", "middle")
    g.rect(210, y0, 120, H, "f1 s-acc sw2")
    g.text(270, y0 + 17, "growth gene", "tl", "middle")

g.text(10, 16, "1  No gibberellin: genes off", "tl tb")
y0 = 96
dna(y0, False)
g.rect(40, y0 - 30, 52, 22, "fm s-acc sw2", rx=8)                      # transcription factor
g.text(66, y0 - 15, "TF", "tl", "middle")
g.circle(108, y0 - 19, 13, "fp s-acc sw2")                             # DELLA protein bound to the TF
g.text(4, y0 - 42, "transcription factor (TF)", "tl")
g.text(160, y0 - 20, "DELLA protein", "tl")
g.leader((158, y0 - 24), (122, y0 - 20))
g.text(4, y0 + 48, "TF cannot bind, so", "tl")
g.text(4, y0 + 64, "genes not transcribed", "tl")

oy = 170
g.text(10, oy + 16, "2  Gibberellin present: genes on", "tl tb")
y1 = oy + 96
dna(y1, True)
g.rect(176, y1 - 24, 52, 22, "fm s-acc sw2", rx=8)                  # TF bound at the promoter
g.text(202, y1 - 9, "TF", "tl", "middle")
g.circle(24, y1 - 50, 5, "f3 s-acc2 sw2")                              # gibberellin
g.text(36, y1 - 46, "gibberellin", "tl")
g.line([(24, y1 - 42), (24, y1 - 22)], "c1 sw2", "ah")
for (x, yy) in ((14, y1 - 12), (30, y1 - 6), (44, y1 - 14)):
    g.circle(x, yy, 4, "fp s-acc sw2")                                 # DELLA fragments
g.text(56, y1 - 6, "DELLA broken", "tl")
g.text(56, y1 + 8, "down", "tl")
zig = [(222 + 5 * k, y1 + 40 + (5 if k % 2 else -5)) for k in range(0, 20)]
g.line(zig, "c2 sw2", check=False)
g.text(4, y1 + 50, "TF free to bind DNA", "tl")
g.text(330, y1 + 70, "growth proteins made", "tl", "end")
figs.append(g.svg((340, y1 + 82),
    "Gibberellin and DELLA proteins in two panels. Panel 1, no gibberellin: a DELLA protein is bound to a transcription factor, so the factor cannot bind to the promoter of the growth gene and the gene is not transcribed. Panel 2, gibberellin present: gibberellin causes the DELLA protein to break down into fragments, the transcription factor is free and binds to the promoter, the growth gene is transcribed into mRNA and growth proteins are made.",
    "How gibberellin switches on genes. DELLA proteins hold transcription factors (TF) back. Gibberellin causes the DELLA proteins to be broken down, which frees the transcription factors to increase transcription of the genes for growth."))
problems.extend(g.check())

print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
