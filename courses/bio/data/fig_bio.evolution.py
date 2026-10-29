# data/fig_bio.evolution.py: figures of chapters/bio.evolution.md (a tree from a table of differences; allopatric v sympatric speciation).
# Run: py data/fig_bio.evolution.py -> prints the <figure> lines (clearance report on stderr). py data/place_figs_p14.py bio.evolution places them.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["TREE", "ALLO"]

# ---------------------------------------------------------------- tree
t = Fig("tree")
S = 10                     # px per base difference along one lineage
TX = 250                   # tips
root_x, yz_x, wx_x = TX - 15 * S, TX - 7 * S, TX - 3 * S
ys = {"W": 40, "X": 80, "Y": 130, "Z": 170}
nwx, nyz = (ys["W"] + ys["X"]) / 2, (ys["Y"] + ys["Z"]) / 2
nroot = (nwx + nyz) / 2
t.line([(root_x - 30, nroot), (root_x, nroot)], "ln sw2")
t.line([(root_x, nwx), (root_x, nyz)], "ln sw2")
t.line([(root_x, nwx), (wx_x, nwx)], "ln sw2")
t.line([(root_x, nyz), (yz_x, nyz)], "ln sw2")
t.line([(wx_x, ys["W"]), (wx_x, ys["X"])], "ln sw2")
t.line([(yz_x, ys["Y"]), (yz_x, ys["Z"])], "ln sw2")
for k, x in (("W", wx_x), ("X", wx_x), ("Y", yz_x), ("Z", yz_x)):
    t.line([(x, ys[k]), (TX, ys[k])], "ln sw2")
    t.text(TX + 8, ys[k] + 4, f"species {k}", "tl")
t.text(root_x - 94, nroot - 2, "common", "tl")
t.text(root_x - 94, nroot + 12, "ancestor", "tl")
t.text(wx_x + 8, nwx + 4, "6", "tl tb")
t.text(yz_x + 8, nyz + 4, "14", "tl tb")
t.text(root_x + 8, nroot + 4, "30", "tl tb")
t.line([(root_x, 204), (root_x + 5 * S, 204)], "ln sw2")
t.line([(root_x, 199), (root_x, 209)], "ln sw2")
t.line([(root_x + 5 * S, 199), (root_x + 5 * S, 209)], "ln sw2")
t.text(root_x + 5 * S + 8, 208, "5 differences", "tl")
tree = t.svg((340, 226),
    "A tree of four species. The common ancestor of all four splits into two lineages. One branch point leads to species W and X, which differ by 6 bases. The other leads to species Y and Z, which differ by 14 bases. Species W and X differ from Y and Z by 30 bases, where the root splits. Branch lengths are drawn as half of the number of differences, and a scale bar shows 5 differences along one branch.",
    "The tree for W, X, Y and Z. The number at each branch point is the number of base differences between the two species that split there. Each branch is drawn as half of that number because both lineages gained changes.",
    "fig small")

# ---------------------------------------------------------------- allopatric v sympatric
f = Fig("speciation")
BX, BW, BH, STEP = 10, 150, 50, 66
TXT = 172
A, B = "f1 s-acc", "f2 s-acc2"


def dots(y0, pts):
    for (u, v, kind) in pts:
        f.circle(BX + u, y0 + v, 5, A if kind == "A" else B)


def stage(k, y0, l1, l2):
    f.rect(BX, y0, BW, BH, "fm s-acc sw2")
    f.text(TXT, y0 + 20, l1, "tl")
    f.text(TXT, y0 + 36, l2, "tl")


pos = [(20, 14), (48, 12), (98, 14), (122, 12), (140, 15), (30, 36), (58, 34), (100, 38), (122, 35), (138, 38), (14, 26), (112, 25)]


def mix(pattern):
    return [(u, v, c) for (u, v), c in zip(pos, pattern)]


# panel A: allopatric
f.text(10, 16, "A  Allopatric speciation (barrier)", "tl tb")
y = 26
stage(1, y, "1  One population,", "one gene pool")
dots(y, mix("ABABABABABAB"))
y += STEP
stage(2, y, "2  Barrier: no gene", "flow between them")
left = [(u, v, c) for (u, v), c in zip(pos, "ABABABABABAB") if u < 75]
right = [(u, v, c) for (u, v), c in zip(pos, "ABABABABABAB") if u > 75]
dots(y, left + right)
f.line([(BX + 75, y + 2), (BX + 75, y + BH - 2)], "ln thick", check=False)
y += STEP
stage(3, y, "3  Different selection,", "mutation and drift")
dots(y, [(u, v, "A" if u < 75 else "B") if (i % 5) else (u, v, "B" if u < 75 else "A") for i, (u, v) in enumerate(pos)])
f.line([(BX + 75, y + 2), (BX + 75, y + BH - 2)], "ln thick", check=False)
y += STEP
stage(4, y, "4  Barrier gone: cannot", "interbreed, two species")
dots(y, [(u, v, "A" if u < 75 else "B") for (u, v) in pos])
f.line([(BX + 75, y + 2), (BX + 75, y + BH - 2)], "ln-m thin dash", check=False)
# panel B: sympatric
y += STEP + 8
f.text(10, y + 6, "B  Sympatric speciation (same area)", "tl tb")
y += 16
posB = [(20, 8), (55, 12), (90, 8), (125, 11), (38, 18), (108, 18), (20, 34), (55, 38), (90, 34), (125, 37), (38, 43), (108, 43)]


def stageB(y0, l1, l2, pat):
    f.rect(BX, y0, BW, BH, "fm s-acc sw2")
    f.line([(BX, y0 + BH / 2), (BX + BW, y0 + BH / 2)], "ln-m thin dash", check=False)
    f.text(TXT, y0 + 20, l1, "tl")
    f.text(TXT, y0 + 36, l2, "tl")
    for (u, v), c in zip(posB, pat):
        f.circle(BX + u, y0 + v, 5, A if c == "A" else B)


stageB(y, "1  One population", "uses two habitats", "ABABABABABAB")
y += STEP
stageB(y, "2  Groups mate", "mainly within group", "AAAAABBBBBBA")
y += STEP
stageB(y, "3  Little gene flow:", "two species, one area", "AAAAAABBBBBB")
H = y + BH + 14
fig = f.svg((340, H),
    "Two panels of squares containing dots of two kinds. Panel A, allopatric speciation, has four stages. 1: one square holds a mixed population, one gene pool. 2: a barrier splits it in two, so there is no gene flow. 3: the two halves change differently by selection, mutation and drift. 4: the barrier has gone, but the halves cannot interbreed, so they are two species. Panel B, sympatric speciation, has three stages in one square divided into two habitats by a dashed line. 1: one mixed population uses two habitats. 2: the groups mate mainly within their own group. 3: there is little gene flow and two species live in the same area.",
    "Allopatric and sympatric speciation. The two kinds of dot stand for different alleles. In A a physical barrier (thick line) stops gene flow; in B the dashed line separates two habitats in the same area, and there is no barrier to movement.",
    "fig small")
print(tree)
print()
print(fig)
print("\n".join(t.check() + f.check()) or "clearance ok", file=sys.stderr)
