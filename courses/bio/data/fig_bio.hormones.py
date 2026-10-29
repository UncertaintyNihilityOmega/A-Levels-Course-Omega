# data/fig_bio.hormones.py: builds the hand-drawn SVG figures of chapters/bio.hormones.md and checks label clearance.
# Run: py data/fig_bio.hormones.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.hormones replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["GUARD", "ABA", "AUXIN", "BARLEY"]
figs, problems = [], []
BOX = "f1 s-acc sw2"
ARR = "c1 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def box(f, x, y, w, h, lines, cls=BOX):
    f.rect(x, y, w, h, cls)
    n = len(lines)
    for i, s in enumerate(lines):
        yy = y + h / 2 + 5 + (i - (n - 1) / 2) * 15
        f.text(x + w / 2, round(yy, 1), s, "tl", "middle")


def flow(f, x, w, lines_list, y0, h=42, gap=22, last_cls=None):
    for i, lines in enumerate(lines_list):
        y = y0 + i * (h + gap)
        box(f, x, y, w, h, lines, last_cls if (last_cls and i == len(lines_list) - 1) else BOX)
        if i < len(lines_list) - 1:
            f.line([(x + w / 2, y + h), (x + w / 2, y + h + gap)], ARR, "ah")


# ---------- 1. guard cell pair, open and closed ----------
f = Fig("guard")


def bean(xm, cy, side, gap_half, wmax=27, L=54, n=18):
    pin, pout = [], []
    for k in range(n + 1):
        u = -1 + 2 * k / n
        x_in = gap_half * (1 - u * u) + 1.5
        w = wmax * math.sqrt(max(1 - u * u, 0)) + 2
        pin.append((round(xm + side * x_in, 1), round(cy + u * L, 1)))
        pout.append((round(xm + side * (x_in + w), 1), round(cy + u * L, 1)))
    return pin, pout


def panel(cy, gap_half, title):
    f.text(170, cy - 70, title, "tl tb", "middle")
    res = {}
    for side in (-1, 1):
        pin, pout = bean(170, cy, side, gap_half)
        f.poly(pout + pin[::-1], BOX, True)
        f.line(pin, "ln sw3", check=False)
        for u in (-0.55, -0.15, 0.25, 0.65):
            k = int(round((u + 1) / 2 * 18))
            f.line([pin[k], pout[k]], "ln-m thin", check=False)
        k = 9
        mx = (pin[k][0] + pout[k][0]) / 2
        # chloroplasts between the microfibril lines
        for u in (-0.35, 0.05, 0.45):
            kk = int(round((u + 1) / 2 * 18))
            cxp = (pin[kk][0] + pout[kk][0]) / 2
            ellipse(f, round(cxp, 1), round(cy + u * 54, 1), 5, 3.2, "fp ln", check=False)
        res[side] = (pin, pout)
    return res


A = panel(92, 13, "stoma open: guard cells turgid")
B = panel(262, 0, "stoma closed: guard cells flaccid")
# labels on panel A
pin, pout = A[-1]
f.text(112, 70, "thin outer wall", "tl", "end")
f.leader((116, 66), (pout[5][0] - 0.5, pout[5][1]))
f.text(112, 124, "chloroplast", "tl", "end")
cxl = (pin[int(round((0.45 + 1) / 2 * 18))][0] + pout[int(round((0.45 + 1) / 2 * 18))][0]) / 2
f.leader((116, 120), (round(cxl - 3, 1), round(92 + 0.45 * 54, 1)))
pin, pout = A[1]
k = 4
f.text(236, 66, "thick inner", "tl")
f.text(236, 80, "wall", "tl")
f.leader((232, 72), (pin[k][0] + 1, pin[k][1]))
kk = int(round((0.65 + 1) / 2 * 18))
f.text(236, 120, "cellulose", "tl")
f.text(236, 134, "microfibrils", "tl")
f.leader((232, 126), (round((pin[kk][0] + pout[kk][0]) / 2, 1), pin[kk][1]))
done(f, (340, 326),
     "Top view of a pair of guard cells in two states. Top: stoma open. The two bean-shaped guard cells are turgid and curve apart, leaving a pore between them. Bottom: stoma closed. The guard cells are flaccid and straight, touching along the middle. Each guard cell has a thick inner wall next to the pore, a thin outer wall, cellulose microfibrils arranged across the cell like hoops, and chloroplasts.",
     "Guard cells in a drawing. Because the inner wall is thick and the microfibrils run across the cell, a turgid guard cell lengthens and curves, so the pair move apart and open the stoma; flaccid guard cells straighten and close it.")

# ---------- 2. ABA pathway ----------
f = Fig("aba")
flow(f, 40, 260, [["water stress: the plant", "makes more abscisic acid"], ["ABA binds to receptors on", "the guard cell membrane"],
                  ["calcium ions enter the", "cytoplasm (second messenger)"], ["ion channels open:", "K⁺ ions leave the guard cells"],
                  ["water potential rises:", "water leaves by osmosis"], ["guard cells flaccid:", "stoma closes"],
                  ["less water lost by", "transpiration"]], 10, 42, 22, "f2 s-acc2 sw2")
done(f, (340, 460),
     "A flow chart of seven boxes with downward arrows. Water stress: the plant makes more abscisic acid. ABA binds to receptors on the guard cell membrane. Calcium ions enter the cytoplasm as a second messenger. Ion channels open and potassium ions leave the guard cells. The water potential of the guard cells rises and water leaves by osmosis. The guard cells become flaccid and the stoma closes. Less water is lost by transpiration.",
     "How abscisic acid closes a stoma. Calcium ions are the second messenger between the receptor at the surface and the ion channels.")

# ---------- 3. auxin acid growth ----------
f = Fig("auxin")
flow(f, 40, 260, [["auxin made in the shoot tip", "moves to cells behind it"], ["auxin binds to receptors", "on the cell surface membrane"],
                  ["proton pumps (ATP) pump", "H⁺ ions into the cell wall"], ["wall pH falls:", "expansins are activated"],
                  ["expansins loosen bonds between", "cellulose microfibrils"], ["water enters by osmosis: turgor", "stretches the loosened wall"],
                  ["the cell elongates"]], 10, 42, 22, "f2 s-acc2 sw2")
done(f, (340, 460),
     "A flow chart of seven boxes with downward arrows. Auxin made in the shoot tip moves to the cells behind it. Auxin binds to receptors on the cell surface membrane. Proton pumps, using ATP, pump hydrogen ions into the cell wall. The wall pH falls and expansins are activated. Expansins loosen the bonds between cellulose microfibrils. Water enters by osmosis and turgor stretches the loosened wall. The cell elongates.",
     "The acid growth hypothesis. Elongation is permanent: the loosened wall is stretched by the turgor pressure and then re-formed.")

# ---------- 4. barley grain ----------
f = Fig("barley")


def rrect(x, y, w, h, r, cls):
    pts = []
    for (cx_, cy_, a0) in ((x + w - r, y + r, -90), (x + w - r, y + h - r, 0), (x + r, y + h - r, 90), (x + r, y + r, 180)):
        for k in range(9):
            a = math.radians(a0 + 90 * k / 8)
            pts.append((round(cx_ + r * math.cos(a), 1), round(cy_ + r * math.sin(a), 1)))
    f.poly(pts, cls, True)


rrect(10, 10, 240, 200, 44, "fm s-acc sw2")
rrect(24, 24, 212, 172, 32, "f1 s-acc sw2")
ellipse(f, 204, 180, 28, 17, "fr ln")
f.line([(200, 164), (200, 17)], "c3 sw2 dash", "ah")
f.line([(76, 17), (76, 112)], "c1 sw2", "ah")
f.text(84, 52, "amylase", "tl")
f.text(112, 94, "gibberellin", "tl")
f.text(34, 142, "starch hydrolysed to", "tl")
f.text(34, 156, "maltose, then glucose", "tl")
f.line([(116, 168), (172, 182)], "c2 sw2", "ah")
f.text(262, 26, "aleurone", "tl")
f.text(262, 40, "layer", "tl")
f.leader((258, 30), (243, 48))
f.text(262, 110, "starchy", "tl")
f.text(262, 124, "endosperm", "tl")
f.leader((258, 116), (230, 116))
f.text(262, 196, "embryo", "tl")
f.leader((258, 192), (230, 186))
done(f, (352, 224),
     "Section through a barley grain. The outer layer is the aleurone layer. Inside it is the large starchy endosperm. A small embryo sits at the bottom right. A dashed arrow shows gibberellin passing from the embryo to the aleurone layer. A solid arrow shows amylase passing from the aleurone layer into the endosperm. Starch in the endosperm is hydrolysed to maltose and then glucose, and an arrow carries the glucose to the embryo.",
     "Gibberellin from the embryo switches on amylase production in the aleurone layer. Amylase hydrolyses the starch of the endosperm, and the sugars feed the embryo.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
