# data/mk_fig_p18.py: builds the hand SVG figures of P18 (chem.org.polymers, chem.org.synthesis2) and checks clearances.
# Run: py data/mk_fig_p18.py   (writes scratch/p18_<name>.html and prints any clash; the figures are pasted into the chapters).
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mk_fig_p16 import Fig, ring, f, R, verts

DX, DY = 35, 20        # zigzag step (bond about 40 px at 30 degrees)
DO = 36                # length of a vertical C=O or branch bond
GAP = 4.8              # clear gap between a bond end and a label box


class Mol:
    def __init__(self, F):
        self.F = F
        self.A = {}

    def atom(self, k, x, y, lab=None):
        self.A[k] = (x, y, lab)
        if lab:
            self.F.text(x, y + 4, lab, "middle")
        return (x, y)

    def _cut(self, a, b):
        x, y, lab = self.A[a]
        if not lab:
            return 0.0
        bx, by, _ = self.A[b]
        dx, dy = bx - x, by - y
        L = math.hypot(dx, dy)
        hw, hh = 3.5 * len(lab), 6.5
        tx = hw / abs(dx / L) if abs(dx) > 1e-9 else 1e9
        ty = hh / abs(dy / L) if abs(dy) > 1e-9 else 1e9
        return min(tx, ty) + GAP

    def bond(self, a, b, order=1, cls="ln thick"):
        x1, y1, _ = self.A[a]
        x2, y2, _ = self.A[b]
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        ca, cb = self._cut(a, b), self._cut(b, a)
        if order == 2:
            ca = ca + 1.5 if ca else 0
            cb = cb + 1.5 if cb else 0
        p = (x1 + ux * ca, y1 + uy * ca)
        q = (x2 - ux * cb, y2 - uy * cb)
        nx, ny = -uy, ux
        for o in ([0] if order == 1 else [-2.5, 2.5]):
            self.F.line([(p[0] + nx * o, p[1] + ny * o), (q[0] + nx * o, q[1] + ny * o)], cls)

    def stub(self, a, dx, dy, cls="ln thick"):
        """A short bond from atom a to a free end (a chain that continues)."""
        x, y, _ = self.A[a]
        self.A["_s%d" % len(self.A)] = (x + dx, y + dy, None)
        k = "_s%d" % (len(self.A) - 1)
        self.bond(a, k, 1, cls)
        return (x + dx, y + dy)


def bracket(F, x, y0, y1, side):
    s = 7 if side == "l" else -7
    F.raw('<path class="ln" d="M%s %sH%sV%sH%s"/>' % (f(x + s), f(y0), f(x), f(y1), f(x + s)))
    F.pts += [(x, y0), (x, y1), (x + s, y0), (x + s, y1)]


def put(F, M, k, x, y, lab=None):
    M.atom(k, x, y, lab)
    F.pts.append((x, y))


def finish(F, vb, cls, aria, cap, name):
    F.check()
    x0, y0, w, h = vb
    # crop check: everything inside the viewBox with a margin
    for (a, b, c, d, s) in F.texts:
        if a < x0 + 2 or c > x0 + w - 2 or b < y0 + 1 or d > y0 + h - 1:
            print("  OUTSIDE %s: text %r (%d,%d,%d,%d)" % (name, s, a, b, c, d))
    for p in F.pts:
        if p[0] < x0 or p[0] > x0 + w or p[1] < y0 or p[1] > y0 + h:
            print("  OUTSIDE %s: point %s" % (name, tuple(round(v) for v in p)))
    print("  %s: viewBox %s" % (name, vb))
    svg = ('<figure class="%s"><svg viewBox="%s %s %s %s" role="img" aria-label="%s">%s</svg><figcaption>%s</figcaption></figure>'
           % (cls, f(x0), f(y0), f(w), f(h), aria, "".join(F.el), cap))
    os.makedirs("scratch", exist_ok=True)
    with open("scratch/p18_%s.html" % name, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return svg


def diol(F, M, x0, y):
    put(F, M, "o1", x0, y + DY, "HO")
    put(F, M, "c1", x0 + DX, y)
    put(F, M, "c2", x0 + 2 * DX, y + DY)
    put(F, M, "o2", x0 + 3 * DX, y, "OH")
    for a, b in [("o1", "c1"), ("c1", "c2"), ("c2", "o2")]:
        M.bond(a, b)


def terephthalic(F, cx, y, prefix="t"):
    """benzene-1,4-dicarboxylic acid, flat ring centred (cx, y); COOH groups up and outwards."""
    v = ring(F, cx, y, flat=True)
    M = Mol(F)
    M.A["ringL"] = (v[3][0], v[3][1], None)
    M.A["ringR"] = (v[0][0], v[0][1], None)
    for side, sgn, ri in (("l", -1, "ringL"), ("r", 1, "ringR")):
        vx, vy = M.A[ri][0], M.A[ri][1]
        cx_, cy_ = vx + sgn * DX, vy - DY
        put(F, M, "C" + side, cx_, cy_)
        put(F, M, "O" + side, cx_, cy_ - DO, "O")
        put(F, M, "H" + side, cx_ + sgn * DX, cy_ + DY, "OH" if sgn > 0 else "HO")
        M.bond(ri, "C" + side)
        M.bond("C" + side, "O" + side, 2)
        M.bond("C" + side, "H" + side)
    return M


# ------------------------------------------------------------------ PET (fig small, stacked)
def fig_pet():
    F = Fig("pet")
    M = Mol(F)
    diol(F, M, 133, 75)
    F.text(185, 130, "ethane-1,2-diol", "middle")
    F.text(185, 160, "+", "middle")
    terephthalic(F, 185, 235)
    F.text(185, 292, "benzene-1,4-dicarboxylic acid", "middle")
    F.line([(185, 308), (185, 346)], "ln", marker="ah", ok=True)
    F.text(197, 331, "loses H₂O at each link", "start")
    yl = 440
    x0 = 42
    N = Mol(F)
    put(F, N, "O1", x0, yl, "O")
    put(F, N, "C2", x0 + DX, yl - DY)
    put(F, N, "C3", x0 + 2 * DX, yl)
    put(F, N, "O4", x0 + 3 * DX, yl - DY, "O")
    put(F, N, "C5", x0 + 4 * DX, yl)
    put(F, N, "OA", x0 + 4 * DX, yl + DO, "O")
    cxr = x0 + 4 * DX + DX + 28
    v = ring(F, cxr, yl - DY, flat=True)
    N.A["L"] = (v[3][0], v[3][1], None)
    N.A["R"] = (v[0][0], v[0][1], None)
    put(F, N, "C7", v[0][0] + DX, yl)
    put(F, N, "OB", v[0][0] + DX, yl + DO, "O")
    N.stub("O1", -24, -13.7)
    N.stub("C7", 24, -13.7)
    for a, b, o in [("O1", "C2", 1), ("C2", "C3", 1), ("C3", "O4", 1), ("O4", "C5", 1), ("C5", "OA", 2),
                    ("C5", "L", 1), ("R", "C7", 1), ("C7", "OB", 2)]:
        N.bond(a, b, o)
    xl = x0 - 17
    xr = N.A["C7"][0] + 17
    bracket(F, xl, yl - 58, yl + 54, "l")
    bracket(F, xr, yl - 58, yl + 54, "r")
    F.text(xr + 6, yl + 66, "n", "start")
    mx = (N.A["O4"][0] + N.A["C5"][0]) / 2
    F.line([(mx, yl + 58), (mx, yl)], "ln-m thin", ok=True)
    F.text(mx, yl + 74, "ester link", "middle")
    vb = (0, 40, 370, 480)
    cap = ("Making PET (Terylene). The repeat unit is in square brackets with a bond through each bracket. It holds one ester link, O–C=O, "
           "and the next link forms across the bracket. The ring is a hexagon with a circle, and its two groups are opposite each other.")
    aria = ("Ethane-1,2-diol and benzene-1,4-dicarboxylic acid join with loss of water to give PET, whose repeat unit "
            "contains an oxygen, two CH2 groups, an ester link, a benzene ring and a carbonyl group, in square brackets with n at the bottom right; the ester link is labelled")
    return finish(F, vb, "fig small", aria, cap, "pet")


# ------------------------------------------------------------------ nylon-6,6
def zig(F, M, prefix, x0, ylow, labs, dxs=DX):
    """Zigzag chain; atom i at x0 + i*DX, low if i even else up. labs: {index: label}. Returns list of keys."""
    keys = []
    for i in range(len(labs)):
        k = "%s%d" % (prefix, i)
        put(F, M, k, x0 + i * dxs, ylow - (DY if i % 2 else 0), labs[i])
        keys.append(k)
    for a, b in zip(keys, keys[1:]):
        M.bond(a, b)
    return keys


def fig_nylon():
    # REVIEW P18 (24 Oct 2026): chem.org.polymers now holds a hand-edited 360-wide `fig small` version of this
    # figure (names under the monomers, the polymer section drawn with (CH2)6 / (CH2)4). Do not paste this
    # 640-wide output back into the chapter.
    F = Fig("nylon")
    M = Mol(F)
    # row 1: 1,6-diaminohexane
    k = zig(F, M, "a", 60, 95, ["H₂N", None, None, None, None, None, None, "NH₂"])
    F.text(350, 93, "1,6-diaminohexane", "start")
    F.text(335, 142, "+", "middle") if False else None
    # row 2: hexanedioic acid, carbonyl C at idx1 (up) and idx6 (low)
    labs = ["HO", None, None, None, None, None, None, "OH"]
    k2 = zig(F, M, "b", 60, 225, labs)
    put(F, M, "b1O", M.A["b1"][0], M.A["b1"][1] - DO, "O")
    put(F, M, "b6O", M.A["b6"][0], M.A["b6"][1] + DO, "O")
    M.bond("b1", "b1O", 2)
    M.bond("b6", "b6O", 2)
    F.text(350, 223, "hexanedioic acid", "start")
    F.text(60 + 3.5 * DX, 168, "+", "middle")
    # arrow
    F.line([(330, 278), (330, 318)], "ln", marker="ah", ok=True)
    F.text(342, 303, "H₂O is lost at each amide link", "start")
    # row 3: section of polymer with cuts
    x0, yl = 60, 400
    labs3 = [None, "NH"] + [None] * 6 + ["NH", None] + [None] * 4 + [None, "NH"]
    k3 = zig(F, M, "p", x0, yl, labs3)
    # carbonyl oxygens: idx0 (even,low) down; idx9 (odd,up) up; idx14 (even, low) down
    for idx, sgn in ((0, 1), (9, -1), (14, 1)):
        a = "p%d" % idx
        ax, ay = M.A[a][0], M.A[a][1]
        put(F, M, a + "O", ax, ay + sgn * DO, "O")
        M.bond(a, a + "O", 2)
    M.stub("p0", -20, -11.4)
    M.stub("p15", 20, 11.4)
    # cuts at the three amide links (C-N bonds): between idx 0-1, 8-9, 14-15
    cuts = []
    for i, j in ((0, 1), (8, 9), (14, 15)):
        mx = (M.A["p%d" % i][0] + M.A["p%d" % j][0]) / 2
        cuts.append(mx)
        F.line([(mx, yl - 48), (mx, yl + 46)], "ln-m thin dash", ok=True)
        F.text(mx, yl + 66, "amide link", "middle")
    F.text((cuts[0] + cuts[1]) / 2, yl + 100, "from 1,6-diaminohexane", "middle")
    F.text((cuts[1] + cuts[2]) / 2, yl + 100, "from hexanedioic acid", "middle")
    vb = (10, 36, 640, 490)
    cap = ("Nylon-6,6. The two monomers lose one water molecule for every amide link. In the section of polymer the dashed lines cut the three amide links "
           "(C–N bonds); putting H back on each N and OH on each C=O gives the monomers again. One repeat unit is a diamine piece plus a diacid piece.")
    aria = ("1,6-diaminohexane and hexanedioic acid join by amide links with loss of water; below, a section of nylon-6,6 with dashed lines cutting each amide link, "
            "the piece between two cuts labelled as coming from the diamine or from the diacid")
    return finish(F, vb, "fig", aria, cap, "nylon")


# ------------------------------------------------------------------ Kevlar (fig small, stacked)
def fig_kevlar():
    F = Fig("kevlar")
    M = Mol(F)
    cx, y = 185, 95
    v = ring(F, cx, y, flat=True)
    M.A["L"] = (v[3][0], v[3][1], None)
    M.A["R"] = (v[0][0], v[0][1], None)
    put(F, M, "NL", v[3][0] - DX, y - DY, "H₂N")
    put(F, M, "NR", v[0][0] + DX, y - DY, "NH₂")
    M.bond("L", "NL")
    M.bond("R", "NR")
    F.text(cx, 150, "benzene-1,4-diamine", "middle")
    F.text(185, 180, "+", "middle")
    terephthalic(F, 185, 265)
    F.text(185, 322, "benzene-1,4-dicarboxylic acid", "middle")
    F.line([(185, 338), (185, 376)], "ln", marker="ah", ok=True)
    F.text(197, 361, "loses H₂O at each link", "start")
    yl, x0 = 470, 38
    N = Mol(F)
    put(F, N, "N1", x0, yl, "NH")
    v1 = ring(F, x0 + DX + 28, yl - DY, flat=True)
    N.A["L1"] = (v1[3][0], v1[3][1], None)
    N.A["R1"] = (v1[0][0], v1[0][1], None)
    put(F, N, "N2", v1[0][0] + DX, yl, "NH")
    put(F, N, "C3", v1[0][0] + 2 * DX, yl - DY)
    put(F, N, "O3", v1[0][0] + 2 * DX, yl - DY - DO, "O")
    v2 = ring(F, v1[0][0] + 3 * DX + 28, yl, flat=True)
    N.A["L2"] = (v2[3][0], v2[3][1], None)
    N.A["R2"] = (v2[0][0], v2[0][1], None)
    put(F, N, "C4", v2[0][0] + DX, yl - DY)
    put(F, N, "O4", v2[0][0] + DX, yl - DY - DO, "O")
    N.stub("N1", -24, -13.7)
    N.stub("C4", 24, 13.7)
    for a, b, o in [("N1", "L1", 1), ("R1", "N2", 1), ("N2", "C3", 1), ("C3", "O3", 2), ("C3", "L2", 1), ("R2", "C4", 1), ("C4", "O4", 2)]:
        N.bond(a, b, o)
    xl = x0 - 17
    xr = N.A["C4"][0] + 17
    bracket(F, xl, yl - 80, yl + 44, "l")
    bracket(F, xr, yl - 80, yl + 44, "r")
    F.text(xr + 6, yl + 56, "n", "start")
    mx = (N.A["N2"][0] + N.A["C3"][0]) / 2
    F.line([(mx, yl + 38), (mx, yl + 6)], "ln-m thin", ok=True)
    F.text(mx, yl + 54, "amide link", "middle")
    vb = (0, 48, 370, 495)
    cap = ("Kevlar is a polyamide made from benzene-1,4-diamine and benzene-1,4-dicarboxylic acid (or its dioyl chloride, losing HCl). "
           "The two groups on each ring are opposite each other, so the chain is straight and stiff.")
    aria = ("Benzene-1,4-diamine and benzene-1,4-dicarboxylic acid give Kevlar, whose repeat unit has a benzene ring, an NH group, a carbonyl group "
            "and a second benzene ring, in square brackets; the amide link is labelled")
    return finish(F, vb, "fig small", aria, cap, "kevlar")


# ------------------------------------------------------------------ PLA (small)
def fig_pla():
    F = Fig("pla")
    M = Mol(F)
    put(F, M, "o", 40, 105, "HO")
    put(F, M, "c2", 75, 85)
    put(F, M, "me", 75, 85 - DO + 6, "CH₃")
    put(F, M, "c1", 110, 105)
    put(F, M, "od", 110, 105 + DO, "O")
    put(F, M, "oh", 145, 85, "OH")
    for a, b, o in [("o", "c2", 1), ("c2", "me", 1), ("c2", "c1", 1), ("c1", "od", 2), ("c1", "oh", 1)]:
        M.bond(a, b, o)
    F.text(92, 170, "2-hydroxypropanoic acid", "middle")
    F.line([(250, 70), (250, 108)], "ln", marker="ah", ok=True) if False else None
    F.text(250, 108, "n", "middle") if False else None
    # row 2: section of two residues
    N = Mol(F)
    x0, yl = 45, 270
    put(F, N, "o1", x0, yl, "O")
    put(F, N, "c1", x0 + DX, yl - DY)
    put(F, N, "m1", x0 + DX, yl - DY - DO + 6, "CH₃")
    put(F, N, "k1", x0 + 2 * DX, yl)
    put(F, N, "d1", x0 + 2 * DX, yl + DO, "O")
    put(F, N, "o2", x0 + 3 * DX, yl - DY, "O")
    put(F, N, "c2", x0 + 4 * DX, yl)
    put(F, N, "m2", x0 + 4 * DX, yl + DO - 6, "CH₃")
    put(F, N, "k2", x0 + 5 * DX, yl - DY)
    put(F, N, "d2", x0 + 5 * DX, yl - DY - DO, "O")
    N.stub("o1", -DX / 1.6, -DY / 1.6)
    N.stub("k2", DX / 1.6, DY / 1.6)
    for a, b, o in [("o1", "c1", 1), ("c1", "m1", 1), ("c1", "k1", 1), ("k1", "d1", 2), ("k1", "o2", 1), ("o2", "c2", 1),
                    ("c2", "m2", 1), ("c2", "k2", 1), ("k2", "d2", 2)]:
        N.bond(a, b, o)
    mx = (N.A["k1"][0] + N.A["o2"][0]) / 2
    F.line([(mx + 5, yl + 52), (mx + 2, yl + 2)], "ln-m thin", ok=True)
    F.text(mx + 7, yl + 68, "ester link", "middle")
    F.text(x0 + 2.5 * DX, 372, "section of poly(lactic acid)", "middle")
    vb = (0, 25, 330, 365)
    cap = ("Lactic acid (2-hydroxypropanoic acid) has an OH group at one end and a COOH group at the other, so it can join to itself. "
           "In the section of poly(lactic acid) each residue carries a CH₃ side group, and the groups on the carbon next to C=O face alternate ways only because of the zigzag drawing.")
    aria = ("2-hydroxypropanoic acid with an OH, a CH3 on the middle carbon and a COOH; below it a section of poly(lactic acid) with two residues joined by an ester link, which is labelled")
    return finish(F, vb, "fig small", aria, cap, "pla")


# ------------------------------------------------------------------ methylbenzene routes (synthesis2)
def fig_routes():
    F = Fig("routes")

    def subst(cx, cy, subs):
        v = ring(F, cx, cy)
        for idx, lab in subs:
            x, y = v[idx]
            dx, dy = x - cx, y - cy
            L = math.hypot(dx, dy)
            dx, dy = dx / L, dy / L
            ex, ey = x + dx * 17, y + dy * 17
            F.line([(x, y), (ex, ey)], "ln thick")
            if abs(dy) > 0.75:
                F.text(ex, ey - 7 if dy < 0 else ey + 17, lab, "middle")
            elif dx > 0:
                F.text(ex + 4, ey + 4, lab, "start")
            else:
                F.text(ex - 4, ey + 4, lab, "end")
        return v

    xa, xb = 85, 255
    subst(170, 75, [(0, "CH₃")])
    F.text(170, 121, "methylbenzene", "middle")
    F.line([(150, 134), (115, 172)], "ln", marker="ah", ok=True)
    F.line([(190, 134), (225, 172)], "ln", marker="ah", ok=True)
    F.text(100, 158, "nitration", "end")
    F.text(232, 158, "oxidation", "start")
    y2 = 250
    subst(xa, y2, [(0, "CH₃"), (3, "NO₂")])
    F.text(xa, 336, "4-nitromethylbenzene", "middle")
    subst(xb, y2, [(0, "COOH")])
    F.text(xb, 296, "benzoic acid", "middle")
    F.line([(xa, 349), (xa, 393)], "ln", marker="ah", ok=True)
    F.text(xa + 12, 375, "oxidation", "start")
    F.line([(xb, 309), (xb, 393)], "ln", marker="ah", ok=True)
    F.text(xb + 12, 355, "nitration", "start")
    y3 = 470
    subst(xa, y3, [(0, "COOH"), (3, "NO₂")])
    F.text(xa, 556, "4-nitrobenzoic acid", "middle")
    subst(xb, y3, [(0, "COOH"), (2, "NO₂")])
    F.text(xb, 556, "3-nitrobenzoic acid", "middle")
    vb = (5, 5, 330, 570)
    cap = ("Two routes from methylbenzene. Left: nitrate first (CH₃ directs to the 2- and 4-positions, and the 4-isomer is separated), then oxidise the side chain. "
           "Right: oxidise first (COOH directs to the 3-position), then nitrate.")
    aria = ("Methylbenzene is nitrated and then oxidised to give 4-nitrobenzoic acid on the left, or oxidised to benzoic acid and then nitrated to give 3-nitrobenzoic acid on the right")
    return finish(F, vb, "fig small", aria, cap, "routes")


if __name__ == "__main__":
    for fn in (fig_pet, fig_nylon, fig_kevlar, fig_pla, fig_routes):
        print(fn.__name__)
        fn()
