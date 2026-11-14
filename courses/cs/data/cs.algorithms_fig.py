# data/cs.algorithms_fig.py: builds and checks the hand-drawn SVG figures of chapters/cs.algorithms.md.
# Run: py data/cs.algorithms_fig.py    (prints "ok" when every shape, label and arrow passes the checks;
# writes data/cs.algorithms_figs.txt, one figure per "### name" block, ready to paste inside :::html)
import pathlib

CW = 7.0     # width of one 13 px label character
LH = 16      # line height of a two-line label


class Chart:
    def __init__(self, w, h, cls="fig"):
        self.w, self.h, self.cls = w, h, cls
        self.parts, self.nodes, self.texts, self.paths = [], [], [], []

    # ---- nodes: each returns a dict with the shape's box and connection points ----
    def _node(self, kind, cx, cy, lines, w, h, extra=None):
        n = {"kind": kind, "cx": cx, "cy": cy, "w": w, "h": h, "lines": lines,
             "x0": cx - w / 2, "x1": cx + w / 2, "y0": cy - h / 2, "y1": cy + h / 2,
             "top": (cx, cy - h / 2), "bot": (cx, cy + h / 2), "left": (cx - w / 2, cy), "right": (cx + w / 2, cy)}
        self.nodes.append(n)
        # text lines, centred
        k = len(lines)
        for i, s in enumerate(lines):
            ty = cy + 4 - (k - 1) * LH / 2 + i * LH
            self._text(cx, ty, s, "tl tc", node=n)
        return n

    def _text(self, x, y, s, cls, node=None, anchor="middle"):
        n = len(s)
        s = s.replace("<", "&lt;").replace(">", "&gt;")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}">{s}</text>')
        tw = n * CW
        if anchor == "middle":
            x0, x1 = x - tw / 2, x + tw / 2
        else:
            x0, x1 = x, x + tw
        self.texts.append({"x0": x0, "x1": x1, "y0": y - 10, "y1": y + 3, "s": s, "node": node})

    def term(self, cx, cy, text, fill="fm"):
        w, h = max(len(text) * CW + 34, 84), 32
        n = self._node("term", cx, cy, [text], w, h)
        self.parts.insert(len(self.parts) - 1, f'<rect class="{fill} s-acc sw2" x="{n["x0"]:g}" y="{n["y0"]:g}" width="{w:g}" height="{h}" rx="{h / 2:g}"/>')
        return n

    def proc(self, cx, cy, lines, fill="f1", minw=110):
        lines = [lines] if isinstance(lines, str) else lines
        w, h = max(max(len(s) for s in lines) * CW + 26, minw), 22 + LH * len(lines)
        n = self._node("proc", cx, cy, lines, w, h)
        self.parts.insert(len(self.parts) - len(lines), f'<rect class="{fill} s-acc sw2" x="{n["x0"]:g}" y="{n["y0"]:g}" width="{w:g}" height="{h}" rx="3"/>')
        return n

    def predefined(self, cx, cy, text, fill="f1"):
        w, h = len(text) * CW + 50, 34
        n = self._node("pre", cx, cy, [text], w, h)
        i = len(self.parts) - 1
        self.parts.insert(i, f'<rect class="{fill} s-acc sw2" x="{n["x0"]:g}" y="{n["y0"]:g}" width="{w:g}" height="{h}" rx="3"/>'
                             f'<line class="ln" x1="{n["x0"] + 12:g}" y1="{n["y0"]:g}" x2="{n["x0"] + 12:g}" y2="{n["y1"]:g}"/>'
                             f'<line class="ln" x1="{n["x1"] - 12:g}" y1="{n["y0"]:g}" x2="{n["x1"] - 12:g}" y2="{n["y1"]:g}"/>')
        return n

    def io(self, cx, cy, text, fill="fm2"):
        slant = 14
        w, h = max(len(text) * CW + 26 + 2 * slant, 120), 34
        n = self._node("io", cx, cy, [text], w, h)
        x0, x1, y0, y1 = n["x0"], n["x1"], n["y0"], n["y1"]
        pts = f"{x0 + slant:g},{y0:g} {x1:g},{y0:g} {x1 - slant:g},{y1:g} {x0:g},{y1:g}"
        self.parts.insert(len(self.parts) - 1, f'<polygon class="{fill} s-acc sw2" points="{pts}"/>')
        n["slant"] = slant
        return n

    def dec(self, cx, cy, lines, fill="fp"):
        lines = [lines] if isinstance(lines, str) else lines
        k = len(lines)
        tw = max(len(s) for s in lines) * CW
        hh = 28 + 8 * (k - 1)
        hw = (tw / 2 + 6) / (1 - (k * 13 / 2) / hh)
        hw = round(hw + 0.5)
        n = self._node("dec", cx, cy, lines, 2 * hw, 2 * hh)
        pts = f"{cx:g},{cy - hh:g} {cx + hw:g},{cy:g} {cx:g},{cy + hh:g} {cx - hw:g},{cy:g}"
        self.parts.insert(len(self.parts) - len(lines), f'<polygon class="{fill} s-acc sw2" points="{pts}"/>')
        n["hw"], n["hh"] = hw, hh
        return n

    # ---- arrows (orthogonal polylines), labels ----
    def arrow(self, pts, head=True, src=None, dst=None):
        for (a, b) in zip(pts, pts[1:]):
            assert a[0] == b[0] or a[1] == b[1], f"diagonal segment {a}->{b}"
        d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts)
        mk = ' marker-end="url(#ah)"' if head else ""
        self.parts.append(f'<path class="ln" fill="none" d="{d}"{mk}/>')
        self.paths.append({"pts": pts, "src": src, "dst": dst, "head": head})

    def label(self, x, y, s, anchor="start"):
        cls = "tl" if anchor == "start" else "tl tc"
        self._text(x, y, s, cls, node=None, anchor=anchor)
        self.texts[-1]["free"] = True

    def plain(self, x, y, s, cls="tl tc"):
        """a caption-like text outside the flowchart"""
        self._text(x, y, s, cls, node=None, anchor="middle" if "tc" in cls else "start")
        self.texts[-1]["free"] = True

    def raw(self, svg):
        self.parts.append(svg)

    # ---- checks ----
    def check(self):
        N = self.nodes
        # 1. every shape inside the figure, shapes apart
        for n in N:
            assert 4 <= n["x0"] and n["x1"] <= self.w - 4 and 4 <= n["y0"] and n["y1"] <= self.h - 4, f"shape outside figure: {n['lines']}"
        for i, a in enumerate(N):
            for b in N[i + 1:]:
                apart = a["x1"] + 8 <= b["x0"] or b["x1"] + 8 <= a["x0"] or a["y1"] + 8 <= b["y0"] or b["y1"] + 8 <= a["y0"]
                assert apart, f"shapes too close: {a['lines']} / {b['lines']}"
        # 2. text inside its own shape (diamond: inside the rhombus), free labels clear of shapes
        for t in self.texts:
            assert 0 <= t["x0"] and t["x1"] <= self.w and 0 <= t["y0"] and t["y1"] <= self.h, f"text outside figure: {t['s']}"
            n = t["node"]
            if n is None:
                continue
            if n["kind"] == "dec":
                for (px, py) in ((t["x0"], t["y0"]), (t["x1"], t["y0"]), (t["x0"], t["y1"]), (t["x1"], t["y1"])):
                    inside = abs(px - n["cx"]) / n["hw"] + abs(py - n["cy"]) / n["hh"] <= 1 - 0.02
                    assert inside, f"text pokes out of the diamond: {t['s']}"
            else:
                m = 4 + (n.get("slant", 0) if n["kind"] == "io" else 0)
                assert n["x0"] + m <= t["x0"] and t["x1"] <= n["x1"] - m, f"text too wide for its shape: {t['s']}"
                assert n["y0"] <= t["y0"] and t["y1"] <= n["y1"], f"text outside its shape vertically: {t['s']}"
        # 3. every arrow: no crossing of unrelated shapes, last segment long enough
        for p in self.paths:
            pts = p["pts"]
            for (a, b) in zip(pts, pts[1:]):
                for n in N:
                    if n is p["src"] or n is p["dst"]:
                        continue
                    assert not seg_hits_rect(a, b, n["x0"] - 2, n["y0"] - 2, n["x1"] + 2, n["y1"] + 2), f"arrow {a}->{b} crosses {n['lines']}"
            if p["head"]:
                a, b = pts[-2], pts[-1]
                assert abs(a[0] - b[0]) + abs(a[1] - b[1]) >= 18, f"last arrow segment too short {pts}"
        # 4. free labels keep 4 px from every shape and every arrow segment, and from other text
        for t in self.texts:
            if not t.get("free"):
                continue
            for n in N:
                clear = t["x1"] + 4 <= n["x0"] or n["x1"] + 4 <= t["x0"] or t["y1"] + 4 <= n["y0"] or n["y1"] + 4 <= t["y0"]
                assert clear, f"label {t['s']} touches {n['lines']}"
            for p in self.paths:
                for (a, b) in zip(p["pts"], p["pts"][1:]):
                    assert not seg_hits_rect(a, b, t["x0"] - 4, t["y0"] - 4, t["x1"] + 4, t["y1"] + 4), f"label {t['s']} touches an arrow"
        T = self.texts
        for i, a in enumerate(T):
            for b in T[i + 1:]:
                if a["node"] is not None and a["node"] is b["node"]:
                    continue
                gap = 4
                over = not (a["x1"] + gap <= b["x0"] or b["x1"] + gap <= a["x0"] or a["y1"] + gap <= b["y0"] or b["y1"] + gap <= a["y0"])
                assert not over, f"texts collide: {a['s']} / {b['s']}"

    def svg(self, label, caption):
        return (f'<figure class="{self.cls}"><svg viewBox="0 0 {self.w:g} {self.h:g}" role="img" aria-label="{label}">'
                + "".join(self.parts) + f'</svg><figcaption>{caption}</figcaption></figure>')


def seg_hits_rect(a, b, x0, y0, x1, y1):
    (ax, ay), (bx, by) = a, b
    sx0, sx1, sy0, sy1 = min(ax, bx), max(ax, bx), min(ay, by), max(ay, by)
    return not (sx1 < x0 or sx0 > x1 or sy1 < y0 or sy0 > y1)


def down(a, b, dst=None, src=None, head=True, ch=None):
    ch.arrow([a, b], head=head, src=src, dst=dst)


figs = {}

# ---------------------------------------------------------------------------------------------------
# Figure 1: the flowchart symbols
# ---------------------------------------------------------------------------------------------------
c = Chart(520, 372)
rows = [
    ("term", "Start", "Terminator: the one start and one end"),
    ("proc", "Total ← 0", "Process: a calculation or assignment"),
    ("io", "INPUT Age", "Input or output: INPUT and OUTPUT"),
    ("dec", "Age >= 18?", "Decision: a yes/no question, two exits"),
    ("pre", "SortList", "Predefined process: a module defined elsewhere"),
]
y = 36
SYM_X = 90
text_x = 175
for kind, label, desc in rows:
    if kind == "term":
        c.term(SYM_X, y, label)
    elif kind == "proc":
        c.proc(SYM_X, y, label)
    elif kind == "io":
        c.io(SYM_X, y, label)
    elif kind == "dec":
        c.dec(SYM_X, y + 12, label)
    else:
        c.predefined(SYM_X, y + 26, label)
    if kind == "dec":
        c.plain(text_x, y + 16, desc, "tl")
        y += 76
    elif kind == "pre":
        c.plain(text_x, y + 30, desc, "tl")
        y += 62
    else:
        c.plain(text_x, y + 4, desc, "tl")
        y += 56
# arrow row
ay = y + 18
c.arrow([(30, ay), (170, ay)], src=None, dst=None)
c.plain(text_x, ay + 4, "Arrow: the order the steps run in", "tl")
# the "text" in the free labels above are left-aligned; they must stay inside the figure
c.check()
figs["symbols"] = c.svg(
    "The six flowchart symbols, each with its meaning. A rounded terminator labelled Start: the one start and the one end of the flowchart. A rectangle labelled Total gets 0: a process, a calculation or an assignment. A parallelogram labelled INPUT Age: input or output. A diamond labelled Age at least 18: a decision, a question with exactly two exits, Yes and No. A rectangle with double side lines labelled SortList: a predefined process, a module defined somewhere else. A plain arrow: the order in which the steps run.",
    "The flowchart symbols used in Cambridge questions, with what each means. A flowchart has one start terminator and one end terminator.")

# ---------------------------------------------------------------------------------------------------
# Figure 2: decomposition of the canteen ordering system
# ---------------------------------------------------------------------------------------------------
c = Chart(620, 330)
top = c.proc(310, 30, "Canteen ordering system", fill="f1", minw=200)
cols = [
    ("Take the order", ["Show the menu", "Read choices", "Check stock"]),
    (("Work out", "the bill"), ["Add prices", "Apply discount"]),
    ("Take payment", ["Read amount", "Give change"]),
    (("Report", "the day"), ["Count orders", "Add up takings"]),
]
xs = [72, 222, 372, 522]
# a hierarchy (tree) drawn with plain lines: each sub-problem's parts hang side by side from one spine,
# so they read as siblings, not as a chain of steps
for (head, subs), x in zip(cols, xs):
    h = c.proc(x, 124, list(head) if isinstance(head, tuple) else head, fill="fm", minw=124)
    c.arrow([(310, top["y1"]), (310, 72), (x, 72), (x, h["y0"])], head=False, src=top, dst=h)
    spine = x - 56
    yy = 190
    kids = []
    for s in subs:
        kids.append(c.proc(x + 20, yy, s, fill="fm2", minw=124))
        yy += 50
    c.arrow([(spine, h["y1"]), (spine, kids[-1]["cy"])], head=False, src=h, dst=None)
    for b in kids:
        c.arrow([(spine, b["cy"]), (b["x0"], b["cy"])], head=False, src=None, dst=b)
c.check()
figs["tree"] = c.svg(
    "A tree diagram. At the top, Canteen ordering system. Below it four sub-problems: Take the order, Work out the bill, Take payment, and Report the day. Under Take the order: Show the menu, Read choices, Check stock. Under Work out the bill: Add prices, Apply discount. Under Take payment: Read amount, Give change. Under Report the day: Count orders, Add up takings.",
    "The canteen ordering system split into four sub-problems, each split again into the parts listed under it. Each of the smallest boxes is small enough to become one module (a procedure or a function).")

# ---------------------------------------------------------------------------------------------------
# Figure 3: Example 1 flowchart (loop): pages read until 0
# ---------------------------------------------------------------------------------------------------
c = Chart(520, 552)
LX, RX = 120, 370
s = c.term(LX, 28, "Start")
a1 = c.proc(LX, 88, "Total ← 0")
a2 = c.proc(LX, 148, "Days ← 0")
a3 = c.io(LX, 208, "INPUT Pages")
d = c.dec(LX, 300, "Pages <> 0?")
o1 = c.io(LX, 400, "OUTPUT Days")
o2 = c.io(LX, 458, "OUTPUT Total")
e = c.term(LX, 516, "End")
b1 = c.proc(RX, 300, "Total ← Total + Pages")
b2 = c.proc(RX, 362, "Days ← Days + 1")
b3 = c.io(RX, 424, "INPUT Pages")
c.arrow([s["bot"], a1["top"]], src=s, dst=a1)
c.arrow([a1["bot"], a2["top"]], src=a1, dst=a2)
c.arrow([a2["bot"], a3["top"]], src=a2, dst=a3)
c.arrow([a3["bot"], d["top"]], src=a3, dst=d)
c.arrow([d["bot"], o1["top"]], src=d, dst=o1)
c.arrow([o1["bot"], o2["top"]], src=o1, dst=o2)
c.arrow([o2["bot"], e["top"]], src=o2, dst=e)
c.arrow([d["right"], b1["left"]], src=d, dst=b1)
c.arrow([b1["bot"], b2["top"]], src=b1, dst=b2)
c.arrow([b2["bot"], b3["top"]], src=b2, dst=b3)
# return arrow: out of the last INPUT on the right, up, back to the decision's entry
c.arrow([b3["right"], (500, 424), (500, 250), (LX, 250)], src=b3, dst=None)
c.label(d["right"][0] + 8, 292, "Yes")
c.label(d["bot"][0] + 8, 352, "No")
c.check()
figs["loop"] = c.svg(
    "A flowchart. Start, then Total gets 0, then Days gets 0, then INPUT Pages, then a decision Pages not equal to 0. The Yes exit leads right to Total gets Total plus Pages, then Days gets Days plus 1, then INPUT Pages, then an arrow goes back up to the decision. The No exit leads down to OUTPUT Days, OUTPUT Total and End.",
    "The reading-club program as a flowchart. The decision sits before the loop body, and the arrow from the last INPUT returns to it: this is a WHILE loop.")


# ---------------------------------------------------------------------------------------------------
# Figure 4: Example 2 flowchart (nested selection): museum price
# ---------------------------------------------------------------------------------------------------
c = Chart(520, 680)
LX, RX = 130, 385
s = c.term(LX, 28, "Start")
i1 = c.io(LX, 88, "INPUT Age")
i2 = c.io(LX, 148, "INPUT Student")
d1 = c.dec(LX, 230, "Age < 5?")
d2 = c.dec(LX, 330, "Age < 18?")
d3 = c.dec(LX, 430, "Student = 'Y'?")
n3 = c.proc(LX, 520, "Price ← 10.00")
o = c.io(LX, 590, "OUTPUT Price")
e = c.term(LX, 646, "End")
p1 = c.proc(RX, 230, "Price ← 0.00")
p2 = c.proc(RX, 330, "Price ← 4.00")
p3 = c.proc(RX, 430, "Price ← 6.00")
c.arrow([s["bot"], i1["top"]], src=s, dst=i1)
c.arrow([i1["bot"], i2["top"]], src=i1, dst=i2)
c.arrow([i2["bot"], d1["top"]], src=i2, dst=d1)
c.arrow([d1["bot"], d2["top"]], src=d1, dst=d2)
c.arrow([d2["bot"], d3["top"]], src=d2, dst=d3)
c.arrow([d3["bot"], n3["top"]], src=d3, dst=n3)
c.arrow([n3["bot"], o["top"]], src=n3, dst=o)
c.arrow([o["bot"], e["top"]], src=o, dst=e)
for d_, p_ in ((d1, p1), (d2, p2), (d3, p3)):
    c.arrow([d_["right"], p_["left"]], src=d_, dst=p_)
    c.label(d_["right"][0] + 8, d_["cy"] - 8, "Yes")
    c.label(d_["cx"] + 8, d_["cy"] + d_["hh"] + 24, "No")
BUS = 495
c.arrow([p1["right"], (BUS, 230), (BUS, 590), o["right"]], src=p1, dst=o)
c.arrow([p2["right"], (BUS, 330)], head=False, src=p2)
c.arrow([p3["right"], (BUS, 430)], head=False, src=p3)
c.check()
figs["nested"] = c.svg(
    "A flowchart. Start, INPUT Age, INPUT Student, then three decisions one below the other. Decision Age less than 5: Yes leads right to Price gets 0.00, No leads down. Decision Age less than 18: Yes leads right to Price gets 4.00, No leads down. Decision Student equals Y: Yes leads right to Price gets 6.00, No leads down to Price gets 10.00. All four assignments then lead to OUTPUT Price, then End.",
    "The museum price as a flowchart. Each No exit leads to the next question, so the decisions are nested. Only one of the four assignments runs, and every route then reaches OUTPUT Price.")

# ---------------------------------------------------------------------------------------------------
# Figure 5: exam question flowchart (score validation)
# ---------------------------------------------------------------------------------------------------
c = Chart(520, 490)
LX, RX = 130, 385
s = c.term(LX, 28, "Start")
i1 = c.io(LX, 94, "INPUT Score")
d1 = c.dec(LX, 190, ["Score < 0 OR", "Score > 100?"])
d2 = c.dec(LX, 310, "Score >= 40?")
f = c.io(LX, 400, 'OUTPUT "Fail"')
e = c.term(LX, 462, "End")
inv = c.io(RX, 190, 'OUTPUT "Invalid"')
ps = c.io(RX, 310, 'OUTPUT "Pass"')
c.arrow([s["bot"], i1["top"]], src=s, dst=i1)
c.arrow([i1["bot"], d1["top"]], src=i1, dst=d1)
c.arrow([d1["bot"], d2["top"]], src=d1, dst=d2)
c.arrow([d2["bot"], f["top"]], src=d2, dst=f)
c.arrow([f["bot"], e["top"]], src=f, dst=e)
c.arrow([d1["right"], inv["left"]], src=d1, dst=inv)
c.arrow([d2["right"], ps["left"]], src=d2, dst=ps)
c.arrow([inv["top"], (RX, 94), i1["right"]], src=inv, dst=i1)
c.arrow([ps["bot"], (RX, 462), e["right"]], src=ps, dst=e)
c.label(d1["right"][0] + 8, 182, "Yes")
c.label(d1["cx"] + 8, d1["cy"] + d1["hh"] + 22, "No")
c.label(d2["right"][0] + 8, 302, "Yes")
c.label(d2["cx"] + 8, d2["cy"] + d2["hh"] + 22, "No")
c.check()
figs["validate"] = c.svg(
    "A flowchart. Start, INPUT Score, then a decision Score less than 0 OR Score greater than 100. Yes leads right to OUTPUT Invalid, and an arrow goes back up to INPUT Score. No leads down to a decision Score at least 40. Yes leads right to OUTPUT Pass, which leads to End. No leads down to OUTPUT Fail, which leads to End.",
    "A score-checking flowchart. An invalid score sends the flow back to INPUT Score; a valid score is then compared with 40.")

# ---------------------------------------------------------------------------------------------------
# Figure 6: a flowchart with errors (mean of five marks)
# ---------------------------------------------------------------------------------------------------
c = Chart(520, 474)
LX, RX = 130, 385
s = c.term(LX, 28, "Start")
a1 = c.proc(LX, 92, "Count ← 1")
d = c.dec(LX, 190, "Count <= 5?")
m = c.proc(LX, 300, "Mean ← Total / 4")
o = c.io(LX, 372, "OUTPUT Mean")
e = c.term(LX, 440, "End")
b1 = c.io(RX, 190, "INPUT Mark")
b2 = c.proc(RX, 252, "Total ← Total + Mark")
b3 = c.proc(RX, 314, "Count ← Count + 1")
c.arrow([s["bot"], a1["top"]], src=s, dst=a1)
c.arrow([a1["bot"], d["top"]], src=a1, dst=d)
c.arrow([d["bot"], m["top"]], src=d, dst=m)
c.arrow([m["bot"], o["top"]], src=m, dst=o)
c.arrow([o["bot"], e["top"]], src=o, dst=e)
c.arrow([d["right"], b1["left"]], src=d, dst=b1)
c.arrow([b1["bot"], b2["top"]], src=b1, dst=b2)
c.arrow([b2["bot"], b3["top"]], src=b2, dst=b3)
c.arrow([b3["right"], (505, 314), (505, 140), (LX, 140)], src=b3, dst=None)
c.label(d["right"][0] + 8, 182, "No")
c.label(d["cx"] + 8, d["cy"] + d["hh"] + 24, "Yes")
c.check()
figs["errors"] = c.svg(
    "A flowchart. Start, then Count gets 1, then a decision Count less than or equal to 5. The exit labelled No leads right to INPUT Mark, then Total gets Total plus Mark, then Count gets Count plus 1, then an arrow goes back up to the line above the decision. The exit labelled Yes leads down to Mean gets Total divided by 4, then OUTPUT Mean, then End.",
    "A flowchart that is meant to output the mean of five marks. It contains logic errors.")

(pathlib.Path(__file__).resolve().parent / "cs.algorithms_figs.txt").write_text(
    "\n\n".join(f"### {k}\n{v}" for k, v in figs.items() if not k.startswith("_")), encoding="utf-8")
print("ok", list(k for k in figs if not k.startswith("_")))
