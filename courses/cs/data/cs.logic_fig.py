# data/cs.logic_fig.py: draws the logic-gate figures of chapters/cs.logic.md and checks their geometry
# (every label box clear of every wire, gate and other label). Run: py data/cs.logic_fig.py [name]
# Prints one <figure> per name; the chapter holds the printed SVG.
import sys

H = 40  # gate height


def or_back_x(y):
    """x of the back curve of the OR body at height y (0..40), by bisection on the Bezier."""
    P = [(0, 40), (7, 28), (7, 12), (0, 0)]

    def pt(t):
        u = 1 - t
        return (u**3 * P[0][0] + 3 * u * u * t * P[1][0] + 3 * u * t * t * P[2][0] + t**3 * P[3][0],
                u**3 * P[0][1] + 3 * u * u * t * P[1][1] + 3 * u * t * t * P[2][1] + t**3 * P[3][1])
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if pt(mid)[1] > y:
            lo = mid
        else:
            hi = mid
    return pt(lo)[0]


ORX = {10: or_back_x(10), 30: or_back_x(30)}
SHAPES = {
    "AND": ('M0 0 H20 A20 20 0 0 1 20 40 H0 Z', [], 0, 40),
    "OR": ('M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z', [], 0, 42),
    "NOT": ('M0 0 L28 20 L0 40 Z', [(32, 20)], 0, 36),
    "NAND": ('M0 0 H20 A20 20 0 0 1 20 40 H0 Z', [(44, 20)], 0, 48),
    "NOR": ('M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z', [(46, 20)], 0, 50),
    "XOR": ('M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z', [], -6, 42),
}


def pins(kind):
    """(input pins, output pin) relative to the gate's top-left corner."""
    if kind in ("AND", "NAND"):
        ins = [(0, 10), (0, 30)]
    elif kind in ("OR", "NOR"):
        ins = [(ORX[10], 10), (ORX[30], 30)]
    elif kind == "XOR":
        ins = [(ORX[10] - 6, 10), (ORX[30] - 6, 30)]
    else:
        ins = [(0, 20)]
    return ins, (SHAPES[kind][3], 20)


def r(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Fig:
    def __init__(self, w, h, label, caption, small=False):
        self.w, self.h, self.label, self.caption, self.small = w, h, label, caption, small
        self.parts, self.segs, self.boxes, self.labels, self.gates = [], [], [], [], {}

    def gate(self, name, kind, x, y):
        d, bubbles, x0, x1 = SHAPES[kind]
        g = [f'<g transform="translate({r(x)} {r(y)})"><path class="fm s-acc sw2" d="{d}"/>']
        for cx, cy in bubbles:
            g.append(f'<circle class="fm s-acc sw2" cx="{cx}" cy="{cy}" r="4"/>')
        if kind == "XOR":
            g.append('<path class="ln" fill="none" d="M-6 0 C1 12 1 28 -6 40"/>')
        g.append("</g>")
        self.parts.append("".join(g))
        self.boxes.append((x + x0 - 1, y - 1, x + x1 + 1, y + H + 1))
        ins, out = pins(kind)
        self.gates[name] = ([(x + a, y + b) for a, b in ins], (x + out[0], y + out[1]))

    def pin(self, name, k):
        return self.gates[name][0][k]

    def out(self, name):
        return self.gates[name][1]

    def wire(self, *pts):
        pts = [(float(a), float(b)) for a, b in pts]
        s = " ".join(f"{r(a)},{r(b)}" for a, b in pts)
        self.parts.append(f'<polyline class="ln" fill="none" points="{s}"/>')
        for p, q in zip(pts, pts[1:]):
            self.segs.append((p, q))

    def dot(self, x, y):
        self.parts.append(f'<circle class="fi" cx="{r(x)}" cy="{r(y)}" r="3.5"/>')

    def text(self, x, y, s, cls="tl", anchor="s", bold=False):
        c = cls + (" tb" if bold else "")
        if anchor == "m":
            c += " tc"
        elif anchor == "e":
            c += " te"
        self.parts.append(f'<text class="{c}" x="{r(x)}" y="{r(y)}">{s}</text>')
        n = len(s.replace("&amp;", "&"))
        wd = 7.2 * n + (n * 0.4 if bold else 0)
        x0 = x if anchor == "s" else (x - wd / 2 if anchor == "m" else x - wd)
        self.labels.append((s, (x0, y - 10, x0 + wd, y + 3)))

    def check(self):
        bad = []
        W, Hh = self.w, self.h
        for s, (a, b, c, d) in self.labels:
            if a < 0 or b < 0 or c > W or d > Hh:
                bad.append(f"label {s!r} outside the viewBox: {a:.0f},{b:.0f},{c:.0f},{d:.0f}")
            for (p, q) in self.segs:
                x0, x1 = sorted((p[0], q[0]))
                y0, y1 = sorted((p[1], q[1]))
                if x0 - 4 < c and x1 + 4 > a and y0 - 4 < d and y1 + 4 > b:
                    bad.append(f"label {s!r} too close to wire {p}-{q}")
            for (a2, b2, c2, d2) in self.boxes:
                if a2 - 4 < c and c2 + 4 > a and b2 - 4 < d and d2 + 4 > b:
                    bad.append(f"label {s!r} too close to a gate")
        for i, (s, (a, b, c, d)) in enumerate(self.labels):
            for s2, (a2, b2, c2, d2) in self.labels[i + 1:]:
                if a2 - 4 < c and c2 + 4 > a and b2 - 4 < d and d2 + 4 > b:
                    bad.append(f"labels {s!r} and {s2!r} overlap")
        return bad

    def svg(self):
        cls = "fig small" if self.small else "fig"
        inner = "".join(self.parts)
        return (f'<figure class="{cls}"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.label}">{inner}</svg>'
                f"<figcaption>{self.caption}</figcaption></figure>")


def inputs(f, spec, x_end):
    """spec: list of (label, y). Draws a label and a wire from x=30 to x_end per input (None: no wire)."""
    for lab, y in spec:
        f.text(12, y + 4, lab, bold=True)
        if x_end is not None:
            f.wire((30, y), (x_end, y))


# ------------------------------------------------------------------------------------------------
def six_gates():
    f = Fig(600, 250, "The six logic gate symbols: NOT, AND and OR in the top row; NAND, NOR and XOR in the bottom row. "
            "Each has input wires labelled A and B (NOT has only A), an output wire labelled X, and its expression under it. "
            "NOT is a triangle with a small circle on its output. AND has a flat back and a rounded front. OR has a curved back and a pointed front. "
            "NAND is AND with the small circle, NOR is OR with the small circle, and XOR is OR with an extra curved line behind it.",
            "The six gates with their expressions. A small circle on the output means NOT. Every gate except NOT has two inputs.")
    kinds = [["NOT", "AND", "OR"], ["NAND", "NOR", "XOR"]]
    for row, ks in enumerate(kinds):
        oy = row * 130
        for col, k in enumerate(ks):
            ox = col * 200
            f.text(ox + 100, oy + 24, k, anchor="m", bold=True)
            gx, gy = ox + 70, oy + 40
            f.gate(f"{k}", k, gx, gy)
            ins, out = f.gates[k]
            names = ["A"] if k == "NOT" else ["A", "B"]
            for (px, py), lab in zip(ins, names):
                f.wire((ox + 34, py), (px, py))
                f.text(ox + 20, py + 4, lab, anchor="m")
            f.wire(out, (out[0] + 22, out[1]))
            f.text(out[0] + 28, out[1] + 4, "X")
            expr = "X = NOT A" if k == "NOT" else f"X = A {k} B"
            f.text(ox + 100, oy + 108, expr, anchor="m")
    return f


def circuit1():
    f = Fig(430, 175, "Logic circuit with inputs A, B and C and output X. A and B feed an AND gate whose output, labelled P, goes to an OR gate. "
            "C feeds a NOT gate whose output, labelled Q, goes to the other input of the OR gate. The OR gate output is X.",
            "The circuit for X = (A AND B) OR NOT C. P and Q label the wires between the gates.")
    f.gate("and", "AND", 110, 35)
    f.gate("not", "NOT", 110, 115)
    f.gate("or", "OR", 270, 75)
    inputs(f, [("A", 45), ("B", 65), ("C", 135)], None)
    f.wire((30, 45), f.pin("and", 0))
    f.wire((30, 65), f.pin("and", 1))
    f.wire((30, 135), f.pin("not", 0))
    f.wire(f.out("and"), (210, 55), (210, 85), f.pin("or", 0))
    f.wire(f.out("not"), (230, 135), (230, 105), f.pin("or", 1))
    o = f.out("or")
    f.wire(o, (o[0] + 50, o[1]))
    f.text(o[0] + 56, o[1] + 4, "X", bold=True)
    f.text(172, 47, "P")
    f.text(172, 152, "Q")
    return f


def circuit_xor():
    f = Fig(420, 175, "Logic circuit with inputs A and B and output X, built from four gates. A and B each go to an OR gate and to an AND gate. "
            "The OR output is labelled P. The AND output Q goes through a NOT gate, whose output is labelled R. "
            "P and R feed a second AND gate whose output is X. The wires from A and B cross without a dot where they are not joined.",
            "X = (A OR B) AND NOT (A AND B). Wires that cross without a dot are not joined.")
    f.gate("or", "OR", 150, 25)
    f.gate("and1", "AND", 150, 105)
    f.gate("not", "NOT", 220, 105)
    f.gate("and2", "AND", 310, 65)
    inputs(f, [("A", 35), ("B", 135)], None)
    f.wire((30, 35), f.pin("or", 0))
    f.wire((30, 135), f.pin("and1", 1))
    f.wire((60, 35), (60, 115), f.pin("and1", 0))
    f.wire((80, 135), (80, 55), f.pin("or", 1))
    f.dot(60, 35)
    f.dot(80, 135)
    o = f.out("or")
    f.wire(o, (282, o[1]), (282, 75), f.pin("and2", 0))
    a = f.out("and1")
    f.wire(a, f.pin("not", 0))
    n = f.out("not")
    f.wire(n, (292, n[1]), (292, 95), f.pin("and2", 1))
    q = f.out("and2")
    f.wire(q, (q[0] + 50, q[1]))
    f.text(q[0] + 56, q[1] + 4, "X", bold=True)
    f.text(212, 38, "P")
    f.text(200, 142, "Q")
    f.text(268, 142, "R")
    return f


def alarm():
    f = Fig(380, 125, "Logic circuit for a burglar alarm with inputs A, B and C and output X. A and B feed an AND gate. "
            "Its output and C feed an OR gate, whose output is X.",
            "The alarm circuit X = (A AND B) OR C. A is the door sensor, B the arming switch and C the panic button.", small=False)
    f.gate("and", "AND", 100, 35)
    f.gate("or", "OR", 230, 45)
    inputs(f, [("A", 45), ("B", 65), ("C", 100)], None)
    f.wire((30, 45), f.pin("and", 0))
    f.wire((30, 65), f.pin("and", 1))
    f.wire((30, 100), (200, 100), (200, 75), f.pin("or", 1))
    f.wire(f.out("and"), f.pin("or", 0))
    o = f.out("or")
    f.wire(o, (o[0] + 50, o[1]))
    f.text(o[0] + 56, o[1] + 4, "X", bold=True)
    return f


def exam_circuit():
    f = Fig(390, 160, "Logic circuit with inputs A, B and C and output X. A and B feed a NAND gate. B and C feed a NOR gate. "
            "B is joined to both gates by a dot. The outputs of the NAND and the NOR gates feed an XOR gate whose output is X.",
            "The circuit for the exam practice question. The dot on B shows that B is joined to both gates.")
    f.gate("nand", "NAND", 110, 30)
    f.gate("nor", "NOR", 110, 100)
    f.gate("xor", "XOR", 270, 65)
    inputs(f, [("A", 40), ("B", 85), ("C", 130)], None)
    f.wire((30, 40), f.pin("nand", 0))
    f.wire((30, 85), (70, 85))
    f.wire((70, 85), (70, 60), f.pin("nand", 1))
    f.wire((70, 85), (70, 110), f.pin("nor", 0))
    f.dot(70, 85)
    f.wire((30, 130), f.pin("nor", 1))
    f.wire(f.out("nand"), (226, 50), (226, 75), f.pin("xor", 0))
    f.wire(f.out("nor"), (246, 120), (246, 95), f.pin("xor", 1))
    o = f.out("xor")
    f.wire(o, (o[0] + 50, o[1]))
    f.text(o[0] + 56, o[1] + 4, "X", bold=True)
    return f


FIGS = {"six": six_gates, "c1": circuit1, "xor": circuit_xor, "alarm": alarm, "exam": exam_circuit}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        fig = FIGS[n]()
        problems = fig.check()
        print(f"--- {n}: {'OK' if not problems else problems}")
        if len(sys.argv) > 1:
            print(fig.svg())
