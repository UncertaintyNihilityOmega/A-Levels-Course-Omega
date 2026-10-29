# data/fig_bio.meiosis.py: builds the hand-drawn SVG figures of chapters/bio.meiosis.md and checks label clearance.
# Run: py data/fig_bio.meiosis.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.meiosis replaces the @@FIG_<NAME> placeholder lines of the chapter (later runs refresh them).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, arc_pts, ellipse, xchrom, vchrom

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["HOMOL", "STAGES1", "STAGES2", "STAGES3", "STAGES4", "CROSS", "ORIENT"]
figs, problems = [], []
CELL = "fp ln"


def lead(f, a, b):
    f.leader(a, b)


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


# ---------- 1. a homologous pair with loci and alleles ----------
f = Fig("homol")
MX, PX, W_, Y0, Y1 = 110, 190, 26, 44, 216
f.text(MX, 30, "maternal", "tl", "middle")
f.text(PX, 30, "paternal", "tl", "middle")
f.rect(MX - W_ / 2, Y0, W_, Y1 - Y0, "fm s-acc sw2", rx=13)
f.rect(PX - W_ / 2, Y0, W_, Y1 - Y0, "fm s-acc sw2", rx=13)
for cx in (MX, PX):
    f.parts.append(f'<circle class="fi" cx="{cx}" cy="118" r="5"/>')
loci = [(66, "A", "a", "gene A"), (150, "B", "B", "gene B"), (188, "D", "d", "gene D")]
for (y, am, ap, nm) in loci:
    for cx in (MX, PX):
        f.parts.append(f'<rect class="fa s-acc sw2" x="{cx - W_ / 2:g}" y="{y - 5}" width="{W_}" height="10"/>')
    f.text(133, y + 4, am)
    f.text(162, y + 4, ap)
    f.text(226, y + 4, nm + " locus")
    lead(f, (222, y), (PX + W_ / 2 + 3, y))
f.text(8, 122, "centromere")
lead(f, (80, 118), (MX - 11, 118))
done(f, (330, 236),
     "A homologous pair of chromosomes, one maternal and one paternal, the same length with the centromere in the same place. "
     "Both carry the same genes at the same loci: gene A with alleles A on the maternal and a on the paternal chromosome, gene B "
     "with allele B on both, and gene D with alleles D and d.",
     "A homologous pair (a drawing; each chromosome is drawn before DNA replication, as a single chromatid). The two "
     "chromosomes carry the same genes at the same loci, but the alleles can differ: here gene A has alleles A and a, "
     "gene B has B on both, and gene D has D and d.")

# ---------- 2-5. the stages of meiosis in an animal cell with 2n = 4, two panels per figure ----------
PH = 150


def cell(f, oy, rx=62, ry=62, cxx=72):
    ellipse(f, cxx, oy + 76, rx, ry, CELL)


def centriole(f, x, y):
    f.parts.append(f'<rect class="fi" x="{x - 2:g}" y="{y - 6:g}" width="4" height="12"/>')
    f.parts.append(f'<rect class="fi" x="{x - 6:g}" y="{y - 2:g}" width="12" height="4"/>')


def title(f, oy, s):
    f.text(152, oy + 24, s, "tl tb")


def bivalent(f, bx, by, L, cls, ang=0, gap=None):
    """Two replicated homologues side by side along the direction ang, joined by a chiasma (small X)."""
    d = (gap if gap is not None else L / 2 + 1)
    a = math.radians(ang)
    for s in (-1, 1):
        xchrom(f, bx + s * d * math.cos(a), by + s * d * math.sin(a), L, cls + " sw3", ang + 90, 22)
    f.line([(bx - 3, by - 3), (bx + 3, by + 3)], "ln", check=False)
    f.line([(bx - 3, by + 3), (bx + 3, by - 3)], "ln", check=False)


def fibres(f, cx, cy, targets, poles=(-52, 52), both=True):
    for (tx, ty, side) in targets:
        px = cx + (poles[0] if side < 0 else poles[1])
        f.line([(px, cy), (tx, ty)], "ln-m thin", check=False)


def prophase1(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    ellipse(f, cx, cy, 34, 34, "ln-m thin dash")
    bivalent(f, cx - 2, cy - 12, 20, "c1", 14)
    bivalent(f, cx + 2, cy + 14, 14, "c2", -10)
    centriole(f, cx - 50, cy)
    centriole(f, cx + 50, cy)
    title(f, oy, "1  Prophase I")
    f.text(152, oy + 50, "homologous pairs join")
    f.text(152, oy + 64, "up (bivalents)")
    lead(f, (148, oy + 46), (cx + 18, cy - 16))
    f.text(152, oy + 96, "nuclear envelope")
    f.text(152, oy + 110, "breaking down")
    lead(f, (148, oy + 92), (cx + 30, cy + 22))
    f.text(152, oy + 134, "chiasma")
    lead(f, (148, oy + 130), (cx + 8, cy + 16))


def metaphase1(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    ys = [(-16, 20, "c1"), (16, 14, "c2")]
    tg = []
    for (dy, L, c) in ys:
        bivalent(f, cx, cy + dy, L, c, 0)
        d = L / 2 + 1
        tg += [(cx - d, cy + dy, -1), (cx + d, cy + dy, 1)]
    fibres(f, cx, cy, tg)
    centriole(f, cx - 52, cy)
    centriole(f, cx + 52, cy)
    title(f, oy, "2  Metaphase I")
    f.text(152, oy + 50, "pairs line up on")
    f.text(152, oy + 64, "the equator")
    lead(f, (148, oy + 46), (cx + 14, cy - 18))
    f.text(152, oy + 96, "each chromosome has")
    f.text(152, oy + 110, "fibres from one pole")
    lead(f, (148, oy + 92), (cx + 30, cy + 8))


def anaphase1(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    tg = []
    for side, off in ((-1, -26), (1, 26)):
        for dy, L, c in ((-16, 22, "c1"), (16, 16, "c2")):
            xchrom(f, cx + off, cy + dy, L, c + " sw3", 0, 24)
            tg.append((cx + off - side * 3, cy + dy, side))
    fibres(f, cx, cy, tg)
    centriole(f, cx - 52, cy)
    centriole(f, cx + 52, cy)
    title(f, oy, "3  Anaphase I")
    f.text(152, oy + 50, "homologous pairs")
    f.text(152, oy + 64, "separate")
    lead(f, (148, oy + 46), (cx + 28, cy - 20))
    f.text(152, oy + 96, "chromatids stay")
    f.text(152, oy + 110, "joined")
    lead(f, (148, oy + 92), (cx + 30, cy + 14))
    f.text(152, oy + 134, "fibres shorten")
    lead(f, (148, oy + 130), (cx + 44, cy + 2))


def telophase1(f, oy):
    cx, cy = 72, oy + 76
    pts = []
    for k in range(61):
        t = 2 * math.pi * k / 60
        x = 66 * math.cos(t)
        y = 54 * math.sin(t) * (1 - 0.3 * math.exp(-(x / 14) ** 2))
        pts.append((round(cx + x, 1), round(cy + y, 1)))
    f.poly(pts[:-1], CELL)
    for side in (-1, 1):
        nx = cx + side * 34
        ellipse(f, nx, cy, 19, 19, "ln")
        xchrom(f, nx, cy - 6, 14, "c1 sw3", 0, 24)
        xchrom(f, nx, cy + 7, 10, "c2 sw3", 0, 24)
    title(f, oy, "4  Telophase I")
    f.text(152, oy + 50, "two cells; each has")
    f.text(152, oy + 64, "one of each pair")
    lead(f, (148, oy + 46), (cx + 46, cy - 8))
    f.text(152, oy + 96, "chromosomes still")
    f.text(152, oy + 110, "have 2 chromatids")
    lead(f, (148, oy + 92), (cx + 42, cy + 8))
    f.text(152, oy + 134, "cell starts to divide")
    lead(f, (148, oy + 130), (cx + 2, cy + 30))


def prophase2(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    ellipse(f, cx, cy, 34, 34, "ln-m thin dash")
    xchrom(f, cx - 6, cy - 12, 22, "c1 sw3", 25, 20)
    xchrom(f, cx + 8, cy + 14, 16, "c2 sw3", -35, 20)
    centriole(f, cx - 50, cy)
    centriole(f, cx + 50, cy)
    title(f, oy, "5  Prophase II")
    f.text(152, oy + 50, "one of the two cells")
    f.text(152, oy + 64, "no pairing this time")
    lead(f, (148, oy + 46), (cx + 12, cy - 12))
    f.text(152, oy + 96, "nuclear envelope")
    f.text(152, oy + 110, "breaking down")
    lead(f, (148, oy + 92), (cx + 30, cy + 22))
    f.text(152, oy + 134, "new spindle forms")
    lead(f, (148, oy + 130), (cx + 54, cy + 4))


def metaphase2(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    tg = []
    for dy, L, c in ((-14, 24, "c1"), (14, 16, "c2")):
        xchrom(f, cx, cy + dy, L, c + " sw3", 0, 22)
        tg += [(cx - 3, cy + dy, -1), (cx + 3, cy + dy, 1)]
    fibres(f, cx, cy, tg)
    centriole(f, cx - 52, cy)
    centriole(f, cx + 52, cy)
    title(f, oy, "6  Metaphase II")
    f.text(152, oy + 50, "chromosomes line up")
    f.text(152, oy + 64, "singly on equator")
    lead(f, (148, oy + 46), (cx + 12, cy - 16))
    f.text(152, oy + 96, "fibres from both")
    f.text(152, oy + 110, "poles on each one")
    lead(f, (148, oy + 92), (cx + 30, cy + 9))


def anaphase2(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    for side, off in (("left", -24), ("right", 24)):
        for dy, L, c in ((-14, 20, "c1"), (14, 13, "c2")):
            px = cx + off
            vchrom(f, px, cy + dy, L, c + " sw3", side)
            pole = cx - 52 if side == "left" else cx + 52
            f.line([(pole, cy), (px, cy + dy)], "ln-m thin", check=False)
    centriole(f, cx - 52, cy)
    centriole(f, cx + 52, cy)
    title(f, oy, "7  Anaphase II")
    f.text(152, oy + 50, "centromeres divide")
    lead(f, (148, oy + 46), (cx + 24, cy - 16))
    f.text(152, oy + 82, "chromatids pulled")
    f.text(152, oy + 96, "to opposite poles")
    lead(f, (148, oy + 78), (cx + 30, cy + 12))


def telophase2(f, oy):
    cx, cy = 72, oy + 76
    for dx in (-30, 30):
        for dy in (-28, 28):
            ellipse(f, cx + dx, cy + dy, 26, 24, CELL)
            ellipse(f, cx + dx, cy + dy, 13, 13, "ln")
            f.line([(cx + dx - 6, cy + dy - 3), (cx + dx + 6, cy + dy - 3)], "c1 sw2", check=False)
            f.line([(cx + dx - 4, cy + dy + 4), (cx + dx + 4, cy + dy + 4)], "c2 sw2", check=False)
    title(f, oy, "8  Telophase II")
    f.text(152, oy + 50, "four cells (two from")
    f.text(152, oy + 64, "each cell of meiosis I)")
    lead(f, (148, oy + 46), (cx + 48, cy - 34))
    f.text(152, oy + 96, "each nucleus is")
    f.text(152, oy + 110, "haploid (n = 2)")
    lead(f, (148, oy + 92), (cx + 36, cy + 24))


STG = [
    ("STAGES1", prophase1, metaphase1,
     "Two stages of meiosis I in an animal cell with four chromosomes. Prophase I: homologous chromosomes pair up as bivalents "
     "with chiasmata, and the nuclear envelope breaks down. Metaphase I: the bivalents line up on the equator, each chromosome "
     "attached by its centromere to fibres from one pole.",
     "Prophase I and metaphase I (drawings of an animal cell, 2n = 4). Each chromosome has two chromatids. The two "
     "longer chromosomes are one homologous pair and the two shorter ones another."),
    ("STAGES2", anaphase1, telophase1,
     "Two stages of meiosis I. Anaphase I: whole chromosomes, each still made of two chromatids, are pulled from each pair to "
     "opposite poles. Telophase I: two cells, each with two chromosomes, one from each homologous pair.",
     "Anaphase I and telophase I. The homologues of each pair separate, so each new cell has only two chromosomes: "
     "the number has halved."),
    ("STAGES3", prophase2, metaphase2,
     "Two stages of meiosis II in one of the two cells. Prophase II: a new spindle forms and the nuclear envelope breaks "
     "down. Metaphase II: the two chromosomes line up singly on the equator, attached to fibres from both poles.",
     "Prophase II and metaphase II in one of the two haploid cells (drawings). There is no pairing: this division looks "
     "like mitosis, but the cell has only two chromosomes."),
    ("STAGES4", anaphase2, telophase2,
     "Two stages of meiosis II. Anaphase II: the centromeres divide and the chromatids are pulled to opposite poles. "
     "Telophase II: four cells, each with a nucleus containing two chromosomes.",
     "Anaphase II and telophase II. Each chromatid is now a chromosome. Meiosis I and II together make four haploid "
     "cells from one diploid cell."),
]
for (name, fa, fb, label, caption) in STG:
    f = Fig(name.lower())
    fa(f, 0)
    fb(f, PH)
    done(f, (330, 2 * PH), label, caption)

# ---------- 6. crossing over ----------
f = Fig("cross")
f.text(8, 16, "1  A chiasma forms", "tl tb")
X1 = [40, 64, 146, 170]
T, B = 52, 132
mid = (T + B) / 2
f.line([(X1[0], T), (X1[0], B)], "c1 sw3")
f.line([(X1[3], T), (X1[3], B)], "c2 sw3")
f.line([(X1[1], T), (X1[1], mid - 16), ((X1[1] + X1[2]) / 2, mid)], "c1 sw3", check=False)
f.line([(((X1[1] + X1[2]) / 2), mid), (X1[2], mid + 16), (X1[2], B)], "c2 sw3", check=False)
f.line([(X1[2], T), (X1[2], mid - 16), ((X1[1] + X1[2]) / 2, mid)], "c2 sw3", check=False)
f.line([(((X1[1] + X1[2]) / 2), mid), (X1[1], mid + 16), (X1[1], B)], "c1 sw3", check=False)
f.segs += [((X1[1], T), (X1[1], mid - 16), "c1"), ((X1[2], T), (X1[2], mid - 16), "c2"),
           ((X1[1], mid + 16), (X1[1], B), "c1"), ((X1[2], mid + 16), (X1[2], B), "c2"),
           ((X1[1], mid - 16), (X1[2], mid + 16), "c"), ((X1[2], mid - 16), (X1[1], mid + 16), "c")]
for x, top, bot in ((X1[0], "A", "B"), (X1[1], "A", "B"), (X1[2], "a", "b"), (X1[3], "a", "b")):
    f.text(x, T - 8, top, "tl", "middle")
    f.text(x, B + 16, bot, "tl", "middle")
f.text((X1[1] + X1[2]) / 2, mid + 38, "chiasma", "tl", "middle")
lead(f, ((X1[1] + X1[2]) / 2, mid + 24), ((X1[1] + X1[2]) / 2, mid + 3))
f.text(196, 74, "non-sister")
f.text(196, 88, "chromatids break")
f.text(196, 102, "and rejoin")
f.text(8, 196, "2  After crossing over", "tl tb")
X2 = [46, 110, 174, 238]
T2, B2 = 232, 312
combo = [("A", "B", "c1", "c1"), ("A", "b", "c1", "c2"), ("a", "B", "c2", "c1"), ("a", "b", "c2", "c2")]
for x, (t, b, ct, cb) in zip(X2, combo):
    f.line([(x, T2), (x, (T2 + B2) / 2)], ct + " sw3")
    f.line([(x, (T2 + B2) / 2), (x, B2)], cb + " sw3")
    f.text(x, T2 - 8, t, "tl", "middle")
    f.text(x, B2 + 16, b, "tl", "middle")
    f.text(x, B2 + 38, t + b, "tl tb", "middle")
f.text(8, 372, "AB and ab: parental combinations", "tl")
f.text(8, 388, "Ab and aB: new combinations", "tl")
done(f, (330, 400),
     "Crossing over in two steps. Step 1: two homologous chromosomes, each of two sister chromatids, lie side by side. The "
     "maternal chromosome carries alleles A and B and the paternal carries a and b. Two non-sister chromatids cross at a "
     "chiasma and exchange sections. Step 2: the four chromatids after crossing over carry AB, Ab, aB and ab. AB and ab are "
     "the parental combinations; Ab and aB are new combinations.",
     "Crossing over (a drawing; a line style change marks the exchanged section). Before it, the four chromatids carry only "
     "AB or ab. After it, two of them carry new combinations of alleles, Ab and aB.")

# ---------- 7. random orientation ----------
f = Fig("orient")
for cx, n, up, low, g in ((82, 1, ("A", "a"), ("B", "b"), "gametes AB and ab"), (248, 2, ("A", "a"), ("b", "B"), "gametes Ab and aB")):
    cy = 104
    f.text(cx, 22, "Orientation " + str(n), "tl tb", "middle")
    ellipse(f, cx, cy, 70, 58, CELL)
    for dy, L, c, (l, r) in ((-18, 22, "c1", up), (18, 16, "c2", low)):
        xchrom(f, cx - 12, cy + dy, L, c + " sw3", 0, 22)
        xchrom(f, cx + 12, cy + dy, L, c + " sw3", 0, 22)
        f.text(cx - 32, cy + dy + 4, l, "tl", "end")
        f.text(cx + 32, cy + dy + 4, r, "tl")
    f.line([(cx, 178), (cx, 192)], "ln", "ah")
    f.text(cx, 212, g, "tl", "middle")
f.text(165, 244, "metaphase I, no crossing over:", "tl", "middle")
f.text(165, 260, "four kinds of gamete in all", "tl", "middle")
done(f, (330, 272),
     "Random orientation of two homologous pairs at metaphase I. In orientation 1 the A and B chromosomes face the same pole, "
     "giving gametes AB and ab. In orientation 2 the A and b chromosomes face the same pole, giving gametes Ab and aB.",
     "Two possible orientations of the same two pairs (drawings, no crossing over). Which way round the second pair lies "
     "does not depend on the first, so both orientations are equally likely.")

print("\n\n".join(figs))
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
