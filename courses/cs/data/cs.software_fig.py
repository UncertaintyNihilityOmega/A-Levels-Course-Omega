# data/cs.software_fig.py: builds and checks the three SVG figures of chapters/cs.software.md.
# Run: py data/cs.software_fig.py   (prints nothing but "ok" when every label fits; writes data/cs.software_figs.txt)
import pathlib

CW = 7.0  # width of one 13 px label character


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts, self.boxes, self.texts, self.arrows = [], [], [], []

    def rect(self, x, y, w, h, cls):
        self.parts.append(f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="{w}" height="{h}"/>')
        self.boxes.append((x, y, w, h))

    def text(self, x, y, s, cls="tl tc"):
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}">{s}</text>')
        n = len(s.replace("&amp;", "&"))
        half = n * CW / 2
        self.texts.append((x - half, y - 10, x + half, y + 3, s, cls))

    def arrow(self, x1, y1, x2, y2):
        self.parts.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#ah)"/>')
        self.arrows.append((x1, y1, x2, y2))

    def check(self):
        for (x0, y0, x1, y1, s, cls) in self.texts:
            assert 0 <= x0 and x1 <= self.w and 0 <= y0 and y1 <= self.h, f"text outside figure: {s}"
        for i, a in enumerate(self.texts):
            for b in self.texts[i + 1:]:
                gap = 4
                overlap = not (a[2] + gap <= b[0] or b[2] + gap <= a[0] or a[3] + gap <= b[1] or b[3] + gap <= a[1])
                assert not overlap, f"labels collide: {a[4]} / {b[4]}"
        for (x0, y0, x1, y1, s, cls) in self.texts:
            inside = any(bx + 4 <= x0 and x1 <= bx + bw - 4 and by <= y0 + 1 and y1 <= by + bh for bx, by, bw, bh in self.boxes)
            free = any(cls.endswith(c) for c in ("te",)) or not inside
            if inside:
                continue
            # a label outside every box must keep clear of every box
            for bx, by, bw, bh in self.boxes:
                clear = x1 + 4 <= bx or bx + bw + 4 <= x0 or y1 + 4 <= by or by + bh + 4 <= y0
                assert clear, f"label {s} touches a box"
        for (x1, y1, x2, y2) in self.arrows:
            assert abs(y2 - y1) >= 20 or abs(x2 - x1) >= 20, "arrow too short"
            for (tx0, ty0, tx1, ty1, s, cls) in self.texts:
                lo_y, hi_y = min(y1, y2), max(y1, y2)
                crosses = tx0 - 4 <= x1 <= tx1 + 4 and not (hi_y < ty0 or lo_y > ty1)
                assert not crosses, f"arrow runs through label {s}"

    def svg(self, label, cls="fig small", caption=""):
        body = "".join(self.parts)
        return (f'<figure class="{cls}"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{label}">'
                f'{body}</svg><figcaption>{caption}</figcaption></figure>')


# ---- Figure 1: the operating system between applications and hardware -------------------------
f1 = Fig(340, 300)
f1.rect(30, 10, 280, 34, "fm"); f1.text(170, 32, "User")
f1.rect(30, 78, 280, 34, "fm"); f1.text(170, 100, "Application software")
f1.rect(30, 146, 280, 76, "f1"); f1.text(170, 168, "Operating system", "tl tc tb")
f1.text(170, 188, "memory · files · security"); f1.text(170, 206, "hardware · processes")
f1.rect(30, 256, 280, 34, "fm"); f1.text(170, 278, "Hardware")
for top, bottom in ((44, 78), (112, 146), (222, 256)):
    f1.arrow(150, top + 4, 150, bottom - 4)
    f1.arrow(190, bottom - 4, 190, top + 4)
f1.check()

# ---- Figure 2: a magnetic disk before and after defragmentation -------------------------------
f2 = Fig(340, 180)
before = "ABACBFACFBFC"   # F = free
after = "AAABBBCCCFFF"
fills = {"A": "f1", "B": "f2", "C": "f3", "F": "fm"}
x0, bw = 26, 24
f2.text(26, 20, "Before", "tl")
for i, ch in enumerate(before):
    f2.rect(x0 + i * bw, 28, bw, 28, fills[ch])
    if ch != "F":
        f2.text(x0 + i * bw + bw / 2, 47, ch)
f2.text(26, 84, "After", "tl")
for i, ch in enumerate(after):
    f2.rect(x0 + i * bw, 92, bw, 28, fills[ch])
    if ch != "F":
        f2.text(x0 + i * bw + bw / 2, 111, ch)
for i in range(12):
    f2.text(x0 + i * bw + bw / 2, 140, str(i + 1))
f2.text(170, 164, "sector number")
f2.check()
assert before.count("A") == after.count("A") == 3 and before.count("B") == 3 and before.count("C") == 3
assert before.count("F") == after.count("F") == 3


def fragments(layout, name):
    runs, prev = 0, False
    for ch in layout:
        here = ch == name
        if here and not prev:
            runs += 1
        prev = here
    return runs


FRAG_BEFORE = {n: fragments(before, n) for n in "ABC"}
FRAG_AFTER = {n: fragments(after, n) for n in "ABC"}
assert FRAG_BEFORE == {"A": 3, "B": 3, "C": 3} and FRAG_AFTER == {"A": 1, "B": 1, "C": 1}

# ---- Figure 3: compiler against interpreter ---------------------------------------------------
f3 = Fig(340, 320)
f3.text(80, 20, "Compiler", "tl tc tb"); f3.text(260, 20, "Interpreter", "tl tc tb")
f3.rect(10, 34, 140, 34, "fm"); f3.text(80, 56, "Source code")
f3.rect(190, 34, 140, 34, "fm"); f3.text(260, 56, "Source code")
f3.rect(10, 102, 140, 34, "f1"); f3.text(80, 124, "Compiler")
f3.rect(190, 102, 140, 44, "f1"); f3.text(260, 119, "Interpreter"); f3.text(260, 138, "one line at a time")
f3.rect(10, 170, 140, 34, "fm"); f3.text(80, 192, "Object code")
f3.rect(10, 238, 140, 34, "fm"); f3.text(80, 260, "Runs on the CPU")
f3.rect(190, 176, 140, 34, "fm"); f3.text(260, 198, "Runs on the CPU")
f3.text(260, 230, "no object code kept")
f3.text(80, 292, "the compiler is not"); f3.text(80, 310, "needed to run it")
for ya, yb in ((68, 102), (136, 170), (204, 238)):
    f3.arrow(80, ya + 4, 80, yb - 4)
f3.arrow(260, 72, 260, 98)
f3.arrow(260, 150, 260, 172)
f3.check()

out = pathlib.Path(__file__).resolve().parent / "cs.software_figs.txt"
out.write_text("\n\n".join([
    f1.svg("The operating system sits between the user and application software above and the hardware below. Arrows run down for requests and up for results. The operating system box lists memory, files, security, hardware and processes.",
           caption="The operating system is the layer between the programs a user runs and the hardware. Requests go down and results come back up."),
    f2.svg("Two rows of twelve disk sectors. Before defragmentation, file A is in sectors 1, 3 and 7, file B in sectors 2, 5 and 10, file C in sectors 4, 8 and 12, and sectors 6, 9 and 11 are free. After defragmentation, A fills sectors 1 to 3, B sectors 4 to 6, C sectors 7 to 9, and sectors 10 to 12 are free.",
           caption="Three files on a magnetic disk. Before, each file is in three fragments; after defragmentation, each is in one run of neighbouring sectors."),
    f3.svg("Two columns. The compiler column: source code goes to the compiler, which produces object code, which runs on the CPU, and the compiler is not needed to run it. The interpreter column: source code goes to the interpreter, which translates one line at a time and runs on the CPU, with no object code kept.",
           caption="A compiler translates the whole program once and produces object code. An interpreter translates and runs one line at a time."),
]), encoding="utf-8")
print("ok", FRAG_BEFORE, FRAG_AFTER)
