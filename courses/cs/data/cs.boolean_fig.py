# data/cs.boolean_fig.py: generates and checks the SVG figures of cs.boolean (half adder, full adder, ripple
# chain, SR and JK flip-flops, a 4-variable Karnaugh map with its groups).
# Usage: py data/cs.boolean_fig.py          writes data/cs.boolean_figs.txt and checks label positions
#        py data/cs.boolean_fig.py inject   replaces each line "@@FIG name@@" in chapters/cs.boolean.md by its block
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "data"))
from cs_kmap_model import solve, covers, term_text  # noqa: E402

AND = "M0 0 H20 A20 20 0 0 1 20 40 H0 Z"
OR = "M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"
XORARC = "M-6 0 C1 12 1 28 -6 40"
# (path, bubble centre x or None, output x offset, pin x offset)
GATES = {"AND": (AND, None, 40, 0), "OR": (OR, None, 42, 3.9), "XOR": (OR, None, 42, -2.1),
         "NOR": (OR, 46, 50, 3.9)}
PROBLEMS = []


class Fig:
    def __init__(self, name, w, h, cls, aria, caption):
        self.name, self.w, self.h, self.cls, self.aria, self.caption = name, w, h, cls, aria, caption
        self.parts, self.segs, self.texts, self.obst = [], [], [], []

    def line(self, pts, cls="ln", arrow=False):
        d = " ".join(f"{x:g},{y:g}" for x, y in pts)
        m = ' marker-end="url(#ah)"' if arrow else ""
        self.parts.append(f'<polyline class="{cls}" fill="none" points="{d}"{m}/>')
        for a, b in zip(pts, pts[1:]):
            self.segs.append((a, b))

    def dot(self, x, y):
        self.parts.append(f'<circle class="fi" cx="{x:g}" cy="{y:g}" r="3"/>')

    def text(self, x, y, s, anchor="start", extra=""):
        cls = {"start": "tl", "middle": "tl tc", "end": "tl te"}[anchor] + (" " + extra if extra else "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}">{s}</text>')
        wd = 7.2 * len(s)
        x0 = {"start": x, "middle": x - wd / 2, "end": x - wd}[anchor]
        self.texts.append((s, x0, y - 10, x0 + wd, y + 3))

    def gate(self, kind, x, y, n_in=2):
        path, bub, outx, pin = GATES[kind]
        g = f'<g transform="translate({x:g} {y:g})"><path class="fm s-acc sw2" d="{path}"/>'
        if kind == "XOR":
            g += f'<path class="ln" fill="none" d="{XORARC}"/>'
        if bub is not None:
            g += f'<circle class="fm s-acc sw2" cx="{bub}" cy="20" r="4"/>'
        self.parts.append(g + "</g>")
        self.obst.append((x - (6 if kind == "XOR" else 0), y, x + outx, y + 40))
        return {"out": (x + outx, y + 20), "pin": x + pin}

    def rect(self, x, y, w, h, cls="fm s-acc sw2", rx=0):
        r = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{r}/>')

    def raw(self, s):
        self.parts.append(s)

    def block(self):
        body = "".join(self.parts)
        return (f'<figure class="{self.cls}"><svg viewBox="0 0 {self.w:g} {self.h:g}" role="img" aria-label="{self.aria}">'
                f'{body}</svg><figcaption>{self.caption}</figcaption></figure>')

    def check(self):
        # text boxes clear of lines (4 px), gate bodies and each other; everything inside the viewBox
        for i, (s, x0, y0, x1, y1) in enumerate(self.texts):
            if x0 < 0 or y0 < 0 or x1 > self.w or y1 > self.h:
                PROBLEMS.append(f"{self.name}: text {s!r} outside the viewBox")
            bx0, by0, bx1, by1 = x0 - 4, y0 - 4, x1 + 4, y1 + 4
            for (a, b) in self.segs:
                lx0, lx1 = sorted((a[0], b[0]))
                ly0, ly1 = sorted((a[1], b[1]))
                if lx1 >= bx0 and lx0 <= bx1 and ly1 >= by0 and ly0 <= by1:
                    PROBLEMS.append(f"{self.name}: text {s!r} touches a line {a}->{b}")
            for (ox0, oy0, ox1, oy1) in self.obst:
                if ox1 >= bx0 and ox0 <= bx1 and oy1 >= by0 and oy0 <= by1:
                    PROBLEMS.append(f"{self.name}: text {s!r} touches a gate/box")
            for j, (s2, a0, b0, a1, b1) in enumerate(self.texts):
                if j > i and a1 + 4 >= x0 and a0 - 4 <= x1 and b1 + 4 >= y0 and b0 - 4 <= y1:
                    PROBLEMS.append(f"{self.name}: texts {s!r} and {s2!r} overlap")
        for (a, b) in self.segs:
            for p in (a, b):
                if not (0 <= p[0] <= self.w and 0 <= p[1] <= self.h):
                    PROBLEMS.append(f"{self.name}: line point {p} outside")


FIGS = []


def half_adder():
    f = Fig("half", 345, 160, "fig small",
            "A half adder. Inputs A and B each go to two gates. An XOR gate gives the sum S, and an AND gate gives the carry C. S = A XOR B and C = A AND B.",
            "A half adder: one XOR gate and one AND gate share the inputs A and B. The XOR output is the sum S; the AND output is the carry C.")
    x1 = f.gate("XOR", 150, 25)
    x2 = f.gate("AND", 150, 95)
    # inputs
    f.text(14, 39, "A")
    f.line([(30, 35), (148, 35)])
    f.line([(60, 35), (60, 105), (150, 105)])
    f.dot(60, 35)
    f.text(14, 129, "B")
    f.line([(30, 125), (150, 125)])
    f.line([(90, 125), (90, 55), (148, 55)])
    f.dot(90, 125)
    f.line([x1["out"], (240, x1["out"][1])])
    f.text(248, 49, "S = A XOR B")
    f.line([x2["out"], (240, x2["out"][1])])
    f.text(248, 119, "C = A AND B")
    FIGS.append(f)


def full_adder():
    f = Fig("full", 590, 170, "fig",
            "A full adder built from two half adders and an OR gate. Half adder 1 adds A and B, giving a partial sum and a first carry. Half adder 2 adds that partial sum to the carry in Cin, giving the final Sum. The OR gate combines the two carries into Cout.",
            "A full adder: half adder 1 adds A and B; half adder 2 adds its sum to the carry in; an OR gate joins the two carries to give the carry out.")
    f.text(14, 14, "Cin")
    f.line([(40, 10), (270, 10), (270, 40), (290, 40)])
    f.text(14, 44, "A")
    f.line([(30, 40), (90, 40)])
    f.text(14, 74, "B")
    f.line([(30, 70), (90, 70)])
    for x in (90, 290):
        f.rect(x, 25, 100, 60)
    for cx in (140, 340):
        f.text(cx, 49, "Half", "middle")
        f.text(cx, 70, "adder", "middle")
    for x, a, b, s, c in ((90, "A", "B", "S", "C"), (290, "Cin", "S1", "S", "C")):
        pass
    # pin labels inside the boxes
    f.text(96, 44, "A")
    f.text(96, 74, "B")
    f.text(184, 44, "S", "end")
    f.text(184, 74, "C", "end")
    f.text(296, 44, "A", "start")
    f.text(296, 74, "B", "start")
    f.text(384, 44, "S", "end")
    f.text(384, 74, "C", "end")
    # S1 from half adder 1 to the second input of half adder 2
    f.line([(190, 40), (232, 40), (232, 70), (290, 70)])
    # C1 to the OR gate (pin 2)
    f.line([(190, 70), (205, 70), (205, 130), (474, 130)])
    # S of half adder 2 -> Sum
    f.line([(390, 40), (530, 40)])
    f.text(536, 44, "Sum")
    # C2 to the OR gate pin 1
    f.line([(390, 70), (430, 70), (430, 110), (474, 110)])
    o = f.gate("OR", 470, 100)
    f.line([o["out"], (530, o["out"][1])])
    f.text(536, 124, "Cout")
    FIGS.append(f)


def ripple_chain():
    f = Fig("chain", 600, 150, "fig",
            "Four full adders chained to add two 4-bit numbers. Each box adds one bit position. Its carry out goes to the carry in of the box on its left. The carry into the rightmost box is 0, and the leftmost box gives the final carry out.",
            "A ripple-carry adder: four full adders in a row for bits 3 to 0, with the carry passed from each adder to the next on its left.")
    xs = [70, 200, 330, 460]
    for k, x in enumerate(xs):
        bit = 3 - k
        f.rect(x, 45, 90, 50)
        f.text(x + 45, 74, "Full adder", "middle")
        f.text(x + 22, 14, f"A{bit}", "middle")
        f.text(x + 68, 14, f"B{bit}", "middle")
        f.line([(x + 22, 22), (x + 22, 45)], arrow=True)
        f.line([(x + 68, 22), (x + 68, 45)], arrow=True)
        f.line([(x + 45, 95), (x + 45, 118)], arrow=True)
        f.text(x + 45, 136, f"S{bit}", "middle")
    for k in range(3):
        right = xs[k] + 90
        left_of_next = xs[k + 1]
        # carry goes from the left side of the box on the right to the right side of the box on the left: right-to-left
        pass
    # carries (right to left): box k+1 (to the right) passes its carry out to box k (to the left)
    for k in range(3):
        f.line([(xs[k + 1], 70), (xs[k] + 90 + 0, 70)], arrow=True)
    for k in range(3):
        cx = (xs[k] + 90 + xs[k + 1]) / 2
        f.text(cx, 62, f"C{3 - k}", "middle")
    f.line([(xs[0], 70), (45, 70)], arrow=True)
    f.text(8, 74, "Cout")
    f.line([(580, 70), (xs[3] + 90, 70)], arrow=True)
    f.text(588, 74, "0")
    FIGS.append(f)


def sr_latch():
    f = Fig("sr", 355, 205, "fig small",
            "An SR flip-flop made from two NOR gates joined in a loop. Input R goes to the top NOR gate, whose output is Q. Input S goes to the bottom NOR gate, whose output is NOT Q. Each output also feeds the other gate.",
            "An SR flip-flop from two cross-coupled NOR gates. The output of each gate is fed back to an input of the other.")
    n1 = f.gate("NOR", 150, 30)
    n2 = f.gate("NOR", 150, 120)
    # inputs
    f.text(14, 44, "R")
    f.line([(30, 40), (154, 40)])
    f.text(14, 164, "S")
    f.line([(30, 160), (154, 160)])
    # outputs (Q at y=50, NOT Q at y=140)
    f.line([n1["out"], (300, 50)])
    f.text(306, 54, "Q")
    f.line([n2["out"], (300, 140)])
    f.text(306, 144, "NOT Q")
    # feedback: Q down to the bottom gate's upper pin; NOT Q up to the top gate's lower pin
    f.line([(270, 50), (270, 95), (130, 95), (130, 130), (154, 130)])
    f.dot(270, 50)
    f.line([(255, 140), (255, 110), (140, 110), (140, 60), (154, 60)])
    f.dot(255, 140)
    FIGS.append(f)


def jk():
    f = Fig("jk", 355, 215, "fig small",
            "A JK flip-flop built from an SR flip-flop of two NOR gates with two 3-input AND gates in front. The top AND gate takes Q, K and the clock CLK and feeds the top NOR gate, whose output is Q. The bottom AND gate takes CLK, J and NOT Q and feeds the bottom NOR gate, whose output is NOT Q.",
            "A JK flip-flop: two 3-input AND gates, controlled by the clock CLK, in front of an SR flip-flop. Q and NOT Q are fed back to the AND gates.")
    # 3-input AND gates; AND path is 40 wide, pins at y+8, y+20, y+32 (x = gate x)
    a1 = f.gate("AND", 110, 20)
    a2 = f.gate("AND", 110, 140)
    n1 = f.gate("NOR", 200, 30)
    n2 = f.gate("NOR", 200, 130)
    # top AND pins: Q (28), K (40), CLK (52)
    f.text(14, 44, "K")
    f.line([(30, 40), (110, 40)])
    f.text(4, 104, "CLK")
    f.line([(30, 100), (70, 100)])
    f.line([(70, 52), (70, 148), (110, 148)])
    f.line([(70, 52), (110, 52)])
    f.dot(70, 100)
    f.text(14, 164, "J")
    f.line([(30, 160), (110, 160)])
    # AND outputs to the NOR gates
    f.line([(150, 40), (204, 40)])
    f.line([(150, 160), (204, 160)])
    # outputs
    f.line([(250, 50), (300, 50)])
    f.text(306, 54, "Q")
    f.line([(250, 150), (300, 150)])
    f.text(306, 154, "NOT Q")
    # Q feedback: up and round to the top AND gate (pin y=28); and down to the bottom NOR (pin y=140)
    f.line([(270, 50), (270, 8), (95, 8), (95, 28), (110, 28)])
    f.line([(270, 50), (270, 100), (180, 100), (180, 140), (204, 140)])
    f.dot(270, 50)
    # NOT Q feedback: down and round to the bottom AND gate (pin y=172); and up to the top NOR (pin y=60)
    f.line([(260, 150), (260, 200), (95, 200), (95, 172), (110, 172)])
    f.line([(260, 150), (260, 110), (190, 110), (190, 60), (204, 60)])
    f.dot(260, 150)
    FIGS.append(f)


def kmap_fig():
    n = 4
    ones = [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]
    order = ["NOT B AND NOT C", "NOT A AND B AND D", "C AND NOT D"]
    groups = sorted(solve(n, ones), key=lambda g: order.index(term_text(g, n)))
    f = Fig("kmap4", 300, 290, "fig small",
            "A 4-variable Karnaugh map with rows AB and columns CD in Gray code order 00, 01, 11, 10. Ones are in cells 0, 1, 2, 5, 6, 7, 8, 9, 10 and 14. Group 1, solid outline: cells 0, 1, 8 and 9, which wrap from the bottom edge to the top edge, giving NOT B AND NOT C. Group 2, dashed outline: cells 5 and 7, giving NOT A AND B AND D. Group 3, dotted outline: cells 2, 6, 10 and 14, the whole CD = 10 column, giving C AND NOT D.",
            "A 4-variable Karnaugh map for X = (NOT B AND NOT C) OR (NOT A AND B AND D) OR (C AND NOT D). Group 1 has a solid outline, group 2 a dashed outline and group 3 a dotted outline.")
    gx, gy, cw, ch = 66, 52, 50, 36
    gray = [0, 1, 3, 2]
    f.text(166, 22, "CD", "middle")
    f.text(8, 44, "AB")
    for ci, g in enumerate(gray):
        f.text(gx + cw * ci + cw / 2, 44, format(g, "02b"), "middle")
    for ri, g in enumerate(gray):
        f.text(gx - 8, gy + ch * ri + ch / 2 + 4, format(g, "02b"), "end")
    pos = {}
    for ri, rg in enumerate(gray):
        for ci, cg in enumerate(gray):
            m = rg * 4 + cg
            pos[m] = (ri, ci)
            x, y = gx + cw * ci, gy + ch * ri
            f.rect(x, y, cw, ch, "fm s-acc sw1")
            f.text(x + cw / 2, y + ch / 2 + 5, "1" if m in ones else "0", "middle", "tb")
    styles = ["c1 sw2", "c2 sw2 dash", "c3 sw2 dot"]
    for gi, imp in enumerate(groups):
        cells = covers(imp, n)
        rows = sorted({pos[m][0] for m in cells})
        cols = sorted({pos[m][1] for m in cells})

        def runs(idx):
            if idx == [0, 3]:
                return [[0], [3]]
            return [idx]
        inset = 6
        for rr in runs(rows):
            for cc in runs(cols):
                x0 = gx + cw * cc[0] + inset
                y0 = gy + ch * rr[0] + inset
                w = cw * len(cc) - 2 * inset
                h = ch * len(rr) - 2 * inset
                f.raw(f'<rect class="{styles[gi]}" fill="none" rx="8" x="{x0}" y="{y0}" width="{w}" height="{h}"/>')
    f.text(20, 224, "Group 1 (solid): NOT B AND NOT C")
    f.text(20, 244, "Group 2 (dashed): NOT A AND B AND D")
    f.text(20, 264, "Group 3 (dotted): C AND NOT D")
    # check the legend against the grid and the text clear of it
    f.obst.append((gx, gy, gx + 4 * cw, gy + 4 * ch))
    f.texts = [t for t in f.texts if not (t[2] >= gy and t[4] <= gy + 4 * ch)]  # cell numbers sit inside the grid
    FIGS.append(f)


def main():
    half_adder()
    full_adder()
    ripple_chain()
    sr_latch()
    jk()
    kmap_fig()
    for f in FIGS:
        f.check()
    out = []
    for f in FIGS:
        out.append(f"=== {f.name} ===\n:::html\n{f.block()}\n:::\n")
    (ROOT / "data" / "cs.boolean_figs.txt").write_text("\n".join(out), encoding="utf-8")
    print("figures:", len(FIGS), "problems:", len(PROBLEMS))
    for p in PROBLEMS:
        print("  ", p)
    if len(sys.argv) > 1 and sys.argv[1] == "refresh":
        path = ROOT / "chapters" / "cs.boolean.md"
        text = path.read_text(encoding="utf-8")
        for f in FIGS:
            pat = re.compile(r'<figure[^>]*><svg[^>]*aria-label="' + re.escape(f.aria) + r'".*?</figure>', re.S)
            assert pat.search(text), f.name
            text = pat.sub(lambda m: f.block(), text, count=1)
        path.write_text(text, encoding="utf-8")
        print("refreshed")
    if len(sys.argv) > 1 and sys.argv[1] == "inject":
        path = ROOT / "chapters" / "cs.boolean.md"
        text = path.read_text(encoding="utf-8")
        for f in FIGS:
            marker = f"@@FIG {f.name}@@"
            assert marker in text, marker
            text = text.replace(marker, f":::html\n{f.block()}\n:::")
        path.write_text(text, encoding="utf-8")
        print("injected")


if __name__ == "__main__":
    main()
