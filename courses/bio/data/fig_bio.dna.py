# data/fig_bio.dna.py: builds the hand-drawn SVG figures of chapters/bio.dna.md and checks label clearance.
# Run: py data/fig_bio.dna.py -> prints each <figure> (blank line between) in the order of NAMES below; clearance report on stderr.
# data/place_figs_p6.py bio.dna replaces the @@FIG_<NAME> placeholder lines of the chapter by these figures.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["NUC", "BASES", "ATP", "BOND", "LADDER", "FORK", "MS"]
figs, problems = [], []


def hexagon(cx, cy, r, flat=True):
    a0 = 0 if flat else 30
    return [(round(cx + r * math.cos(math.radians(a0 + 60 * k)), 1), round(cy + r * math.sin(math.radians(a0 + 60 * k)), 1)) for k in range(6)]


def purine(f, cx, cy, r, cls):
    """double ring: a hexagon (pointy top) fused to a pentagon on its right edge."""
    hx = hexagon(cx, cy, r, flat=False)          # vertices at 30, 90, ... deg: right edge is hx[0]-hx[1]? (30 and -30)
    p_top, p_bot = (hx[0], hx[5])                # (cx+.866r, cy+r/2) and (cx+.866r, cy-r/2) in screen coords
    s = r
    R = s / (2 * math.sin(math.radians(36)))
    c5 = (p_top[0] + 0.688 * s, cy)
    pent = [(round(c5[0] + R * math.cos(math.radians(a)), 1), round(c5[1] + R * math.sin(math.radians(a)), 1)) for a in (216, 288, 0, 72, 144)]
    f.poly(hx, cls)
    f.poly(pent, cls)
    return hx, pent


def nuc(f, ox, oy, numbers=False, oh=True, base_label=None):
    """One nucleotide: phosphate - C5' - pentose ring (C1' to the base). Returns key points."""
    O, C1, C2, C3, C4 = (150, 78), (188, 104), (174, 148), (126, 148), (112, 104)
    S = lambda p: (p[0] + ox, p[1] + oy)
    C5 = S((88, 80))
    P = S((62, 56))
    f.poly([S(p) for p in (O, C1, C2, C3, C4)], "fm s-acc sw2")
    f.line([S(C4), C5], "ln")
    f.line([C5, (P[0] + 10, P[1] + 10)], "ln")
    f.circle(P[0], P[1], 14, "f2 s-acc2 sw2")
    f.parts.append(f'<text class="tl tb" x="{P[0]:g}" y="{P[1] + 5:g}" text-anchor="middle">P</text>')
    cx, cy = 262 + ox, 104 + oy
    f.poly(hexagon(cx, cy, 30), "f1 s-acc sw2")
    f.line([S(C1), (cx - 30, cy)], "ln")
    if oh:
        f.line([S(C3), (S(C3)[0], S(C3)[1] + 18)], "ln")
    if base_label:
        f.parts.append(f'<text class="tl tb" x="{cx:g}" y="{cy + 5:g}" text-anchor="middle">{base_label}</text>')
    return dict(P=P, C5=C5, C3=S(C3), C1=S(C1), C4=S(C4), O=S(O), C2=S(C2), hex=(cx, cy))


# ---------- 1. nucleotide ----------
f = Fig("nucleotide")
k = nuc(f, 0, 0, base_label="B")
f.text(96, 36, "phosphate group")
f.leader((92, 38), (76, 49))
f.text(150, 192, "pentose sugar", anchor="middle")
f.leader((150, 178), (150, 150))
f.text(262, 154, "nitrogenous", anchor="middle")
f.text(262, 168, "base", anchor="middle")
f.leader((262, 142), (262, 135))
figs.append(f.svg((330, 206),
    "A nucleotide has three parts: a phosphate group joined to a pentose sugar (a five-carbon ring), and a nitrogenous base joined to the sugar.",
    "A nucleotide (a simplified drawing, not a structural formula). The phosphate group is joined to the pentose sugar, and the "
    "nitrogenous base is joined to the other side of the sugar. In DNA the sugar is deoxyribose; in RNA it is ribose."))
problems.extend(f.check())

# ---------- 2. purines and pyrimidines ----------
f = Fig("bases")
f.text(165, 18, "pyrimidines: one ring", anchor="middle", cls="tl tb")
for cx, letter, name in [(55, "C", "cytosine"), (165, "T", "thymine"), (275, "U", "uracil")]:
    f.poly(hexagon(cx, 56, 22, flat=False), "f1 s-acc sw2")
    f.parts.append(f'<text class="tl tb" x="{cx}" y="61" text-anchor="middle">{letter}</text>')
    f.text(cx, 100, name, anchor="middle")
f.text(165, 132, "purines: two rings", anchor="middle", cls="tl tb")
for cx, letter, name in [(70, "A", "adenine"), (210, "G", "guanine")]:
    hx, pent = purine(f, cx, 172, 22, "f2 s-acc2 sw2")
    f.parts.append(f'<text class="tl tb" x="{cx}" y="177" text-anchor="middle">{letter}</text>')
    f.text(cx + 20, 216, name, anchor="middle")
figs.append(f.svg((330, 232),
    "The five bases drawn as rings. Cytosine, thymine and uracil are pyrimidines with a single ring. Adenine and guanine are purines with a double ring (a six-sided ring joined to a five-sided ring).",
    "The bases (simplified ring shapes, not structural formulae). A pyrimidine has one ring and a purine has two, so a purine is larger. "
    "DNA contains A, G, C and T; RNA contains A, G, C and U."))
problems.extend(f.check())

# ---------- 3. ATP ----------
f = Fig("atp")
hx, pent = purine(f, 44, 54, 20, "f1 s-acc sw2")
f.parts.append('<text class="tl tb" x="44" y="59" text-anchor="middle">A</text>')
f.line([(pent[3][0], 54), (100, 54)], "ln")
f.poly([(122, 36), (141, 50), (134, 72), (110, 72), (103, 50)], "fm s-acc sw2")
f.line([(141, 54), (176, 54)], "ln")
for i, cx in enumerate((190, 232, 274)):
    f.circle(cx, 54, 14, "f2 s-acc2 sw2")
    f.parts.append(f'<text class="tl tb" x="{cx}" y="59" text-anchor="middle">P</text>')
    if i < 2:
        f.line([(cx + 14, 54), (cx + 28, 54)], "ln")
f.text(44, 108, "adenine", anchor="middle")
f.leader((44, 96), (44, 78))
f.text(122, 108, "ribose", anchor="middle")
f.leader((122, 96), (122, 74))
f.text(232, 108, "three phosphate", anchor="middle")
f.text(232, 122, "groups", anchor="middle")
f.leader((232, 96), (232, 70))
figs.append(f.svg((310, 134),
    "ATP is a nucleotide: the base adenine joined to the sugar ribose, which carries a chain of three phosphate groups.",
    "ATP (adenosine triphosphate), a simplified drawing. It is the nucleotide with the base adenine and the sugar ribose, with two extra "
    "phosphate groups added to the first one: a phosphorylated nucleotide."))
problems.extend(f.check())

# ---------- 4. two nucleotides joined (phosphodiester bond) ----------
f = Fig("bond")
k1 = nuc(f, 0, 14, numbers=True, oh=False, base_label="B")
k2 = nuc(f, 0, 144, numbers=True, oh=True, base_label="B")
# phosphodiester bond: C3' of nucleotide 1 to the phosphate of nucleotide 2
f.line([k1["C3"], (k2["P"][0] + 10, k2["P"][1] - 10)], "c2 sw3")
f.text(16, 18, "5′ end: free phosphate group", cls="tl tb")
f.leader((62, 24), (62, 40))
f.text(160, 206, "phosphodiester bond", anchor="start")
f.leader((156, 202), (99, 177))
f.text(160, 336, "3′ end: free OH group", cls="tl tb")
f.leader((152, 332), (130, 322))
# carbon numbers on the upper nucleotide
f.text(84, 126, "5′", anchor="end")
f.text(110, 146, "4′", anchor="end")
f.text(138, 178, "3′", anchor="start")
f.text(196, 102, "1′")
f.text(190, 160, "2′")
figs.append(f.svg((330, 350),
    "Two nucleotides joined. The phosphate group on the 5′ carbon of the lower nucleotide forms a phosphodiester bond with the hydroxyl group on the 3′ carbon of the upper nucleotide. "
    "The upper end has a free phosphate group (the 5′ end) and the lower end has a free OH group (the 3′ end).",
    "A phosphodiester bond joins two nucleotides (simplified). The carbon atoms of the sugar are numbered 1′ to 5′. The bond forms between the "
    "3′ carbon of one nucleotide and the phosphate group on the 5′ carbon of the next, and a molecule of water is lost."))
problems.extend(f.check())

# ---------- 5. DNA ladder ----------
f = Fig("ladder")
XL, XR = 40, 178
YS = [66 + 40 * i for i in range(6)]
pairs = [("A", "T"), ("C", "G"), ("T", "A"), ("G", "C"), ("A", "T"), ("C", "G")]
wide = {"A": 52, "G": 52, "T": 38, "C": 38}
f.line([(XL, 42), (XL, 322)], "c1 sw3", arrow="ahs", check=False)
f.line([(XR, 322), (XR, 42)], "c2 sw3", arrow="ahs", check=False)
for y, (a, b) in zip(YS, pairs):
    wl, wr = wide[a], wide[b]
    f.rect(XL + 5, y - 12, wl, 24, "f2 s-acc2 sw2" if a in "AG" else "f1 s-acc sw2")
    f.rect(XR - 5 - wr, y - 12, wr, 24, "f2 s-acc2 sw2" if b in "AG" else "f1 s-acc sw2")
    f.parts.append(f'<text class="tl tb" x="{XL + 5 + wl / 2:g}" y="{y + 5}" text-anchor="middle">{a}</text>')
    f.parts.append(f'<text class="tl tb" x="{XR - 5 - wr / 2:g}" y="{y + 5}" text-anchor="middle">{b}</text>')
    nb = 2 if {a, b} == {"A", "T"} else 3
    x0, x1 = XL + 5 + wl, XR - 5 - wr
    for j in range(nb):
        yy = y - 6 + (12 * j / (nb - 1) if nb > 1 else 0)
        f.parts.append(f'<path class="ln-m thin dash" d="M{x0 + 3:g} {yy:g}L{x1 - 3:g} {yy:g}"/>')
for y in YS[:-1]:
    for x in (XL, XR):
        f.circle(x, y + 20, 5, "fp ln")
f.text(XL, 30, "5′", anchor="middle", cls="tl tb")
f.text(XR, 30, "3′", anchor="middle", cls="tl tb")
f.text(XL, 344, "3′", anchor="middle", cls="tl tb")
f.text(XR, 344, "5′", anchor="middle", cls="tl tb")
f.text(204, 62, "A–T pair:")
f.text(204, 76, "2 hydrogen bonds")
f.text(204, 102, "C–G pair:")
f.text(204, 116, "3 hydrogen bonds")
f.text(204, 158, "sugar–phosphate")
f.text(204, 172, "backbone")
f.leader((200, 160), (182, 160))
f.text(204, 210, "phosphodiester")
f.text(204, 224, "bond")
f.leader((200, 212), (183, 206))
f.text(109, 372, "bases pair across the helix", anchor="middle")
figs.append(f.svg((340, 384),
    "A DNA double helix drawn as a flat ladder. Two sugar-phosphate backbones run in opposite directions: the left strand from 5′ at the top to 3′ at the bottom, the right strand from 5′ at the bottom to 3′ at the top. "
    "Each rung is a purine joined to a pyrimidine by hydrogen bonds: A with T by two hydrogen bonds, C with G by three.",
    "DNA (simplified, untwisted). The strands are antiparallel: the left strand runs 5′ to 3′ downwards and the right strand 5′ to 3′ upwards. "
    "A purine always pairs with a pyrimidine, so every rung is the same length. A–T has two hydrogen bonds and C–G has three."))
problems.extend(f.check())

# ---------- 6. replication fork (vertical Y: the fork moves down; fig small keeps labels readable on phones) ----------
f = Fig("fork")
XLa, XRa = 100, 250                 # left arm (lagging template) and right arm (leading template)
YTOP, YARM, YJ, YEND = 44, 220, 272, 344
DL, DR = 165, 185                   # the two strands of the parental duplex
left = [(XLa, YTOP), (XLa, YARM), (DL, YJ), (DL, YEND)]
right = [(XRa, YTOP), (XRa, YARM), (DR, YJ), (DR, YEND)]
f.line(left, "c2 sw3", check=False)
f.line(right, "c1 sw3", check=False)
for a, b in zip(left, left[1:]):
    f.segs.append((a, b, "c2"))
for a, b in zip(right, right[1:]):
    f.segs.append((a, b, "c1"))
for y in range(YJ + 6, YEND, 10):                               # parental base pairs
    f.parts.append(f'<path class="ln-m thin" d="M{DL + 3} {y}L{DR - 3} {y}"/>')
LX, GX = XRa - 24, XLa + 24                                      # new leading / lagging strands (dashed = new)
f.line([(LX, YTOP + 2), (LX, 171)], "c1 sw3 dash", check=False)
f.segs.append(((LX, YTOP + 2), (LX, 171), "c1"))
for y in range(YTOP + 8, 168, 10):
    f.parts.append(f'<path class="ln-m thin" d="M{LX + 3} {y}L{XRa - 3} {y}"/>')
frags = [(YTOP + 2, 98), (112, 150), (186, 214)]
for (a, b) in frags:
    f.line([(GX, a), (GX, b)], "c2 sw3 dash", check=False)
    f.segs.append(((GX, a), (GX, b), "c2"))
    for y in range(a + 6, b, 10):
        f.parts.append(f'<path class="ln-m thin" d="M{XLa + 3} {y}L{GX - 3} {y}"/>')
# enzymes
f.circle(LX, 185, 13, "f2 s-acc2 sw2")
f.parts.append(f'<text class="tl tb" x="{LX}" y="190" text-anchor="middle">P</text>')
f.circle(GX, 169, 13, "f2 s-acc2 sw2")
f.parts.append(f'<text class="tl tb" x="{GX}" y="174" text-anchor="middle">P</text>')
f.circle(GX, 105, 10, "fm s-acc sw2")
f.parts.append(f'<text class="tl tb" x="{GX}" y="110" text-anchor="middle">L</text>')
# strand ends
f.text(XLa, 30, "5′", anchor="middle")
f.text(GX, 30, "3′", anchor="middle")
f.text(LX, 30, "5′", anchor="middle")
f.text(XRa, 30, "3′", anchor="middle")
f.text(DL, 360, "3′", anchor="middle")
f.text(DR, 360, "5′", anchor="middle")
# labels
f.text(8, 112, "lagging")
f.text(8, 126, "strand")
f.leader((50, 128), (GX - 3, 134))
f.text(268, 82, "leading")
f.text(268, 96, "strand")
f.leader((264, 88), (LX + 3, 88))
f.text(8, 196, "template")
f.text(8, 210, "strand")
f.leader((64, 202), (XLa - 3, 202))
f.text(206, 316, "parental")
f.text(206, 330, "DNA")
f.leader((202, 322), (DR + 4, 318))
f.text(8, 300, "P = DNA")
f.text(8, 314, "polymerase")
f.text(8, 332, "L = DNA ligase")
# directions
f.text(266, 136, "fork moves")
f.text(266, 150, "this way")
f.line([(300, 162), (300, 226)], "ln", arrow="ah", check=False)
f.line([(190, 100), (190, 150)], "ln", arrow="ah", check=False)
f.line([(148, 236), (148, 190)], "ln", arrow="ah", check=False)
f.text(175, 58, "new DNA", anchor="middle")
f.text(175, 72, "is made", anchor="middle")
f.text(175, 86, "5′ → 3′", anchor="middle")
figs.append(f.svg((350, 372),
    "A replication fork drawn as a Y, with the parental DNA at the bottom and the fork moving down. The right arm is the template for the leading strand, which a DNA polymerase copies continuously. "
    "The left arm is the template for the lagging strand, which is made as short fragments, each away from the fork, joined by DNA ligase. Strand ends are labelled 5′ and 3′, and the two template strands are antiparallel.",
    "A replication fork (schematic, strands drawn straight). DNA polymerase can only add nucleotides to the 3′ end of a new strand, so every new strand grows 5′ to 3′. "
    "The leading strand is made continuously, in the same direction as the fork moves. The lagging strand is made as fragments, each away from the fork, and DNA ligase joins them. Dashed lines are new DNA."))
problems.extend(f.check())

# ---------- 7. Meselson-Stahl bands ----------
f = Fig("ms")
TX = [104, 160, 216, 272]
YT0, YT1 = 44, 192
f.text(190, 18, "generations in light nitrogen", anchor="middle", cls="tl tb")
for i, x in enumerate(TX):
    f.rect(x, YT0, 36, YT1 - YT0, "fp ln", rx=10)
    f.text(x + 18, 36, str(i), anchor="middle")
yh, ym, yl = 168, 118, 76
bands = [[("h", 1.0)], [("m", 1.0)], [("m", 0.5), ("l", 0.5)], [("m", 0.25), ("l", 0.75)]]
ypos = {"h": yh, "m": ym, "l": yl}
cls = {"h": "f1 s-acc sw2", "m": "f2 s-acc2 sw2", "l": "fm s-acc sw2"}
for x, bs in zip(TX, bands):
    for kind, frac in bs:
        h = 16 * frac
        f.parts.append(f'<rect class="{cls[kind]}" x="{x + 3}" y="{ypos[kind] - h / 2:g}" width="30" height="{h:g}"/>')
f.text(94, yl + 4, "light", anchor="end")
f.text(94, ym + 4, "intermediate", anchor="end")
f.text(94, yh + 4, "heavy", anchor="end")
f.text(190, 216, "band position after centrifuging", anchor="middle")
figs.append(f.svg((330, 232),
    "Four centrifuge tubes for generations 0 to 3 after bacteria were moved from heavy nitrogen to light nitrogen. Generation 0 has one heavy band near the bottom. Generation 1 has one intermediate band. "
    "Generation 2 has an intermediate band and a light band of equal thickness. Generation 3 has a thin intermediate band and a thick light band.",
    "Meselson and Stahl's result (a drawing). Heavy DNA settles lower in the tube than light DNA. A thicker band means more DNA. "
    "After one generation all the DNA is intermediate, which fits semi-conservative replication."))
problems.extend(f.check())

assert len(figs) == len(NAMES)
for s in figs:
    print(s)
    print()
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
