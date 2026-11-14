# data/cs.development_fig.py: builds and checks the hand-drawn SVG figures of chapters/cs.development.md.
# Run: py data/cs.development_fig.py   (prints "ok" when every label, arrow and shape passes the checks;
# writes data/cs.development_figs.txt, one figure per "### name" block, ready to paste inside :::html)
import math
import pathlib

CW = 7.0  # width of one 13 px label character


class Fig:
    def __init__(self, name, w, h, cls, aria, caption):
        self.name, self.w, self.h, self.cls, self.aria, self.caption = name, w, h, cls, aria, caption
        self.parts, self.texts, self.shapes, self.paths, self.ends = [], [], [], [], []
        self.problems = []

    # ---- primitives -------------------------------------------------------------------------
    def text(self, x, y, s, cls="tl tc", owner=None, own=None):
        tw = len(s) * CW
        if "tc" in cls:
            x0 = x - tw / 2
        elif "te" in cls:
            x0 = x - tw
        else:
            x0 = x
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}">{s}</text>')
        self.texts.append({"x0": x0, "x1": x0 + tw, "y0": y - 10, "y1": y + 3, "s": s, "owner": owner, "own": own})

    def rect(self, x, y, w, h, lines, cls="fm s-acc sw2", name=None):
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"/>')
        pts = []
        for t in range(0, int(w) + 1):
            pts += [(x + t, y), (x + t, y + h)]
        for t in range(0, int(h) + 1):
            pts += [(x, y + t), (x + w, y + t)]
        shape = {"kind": "rect", "x0": x, "y0": y, "x1": x + w, "y1": y + h, "pts": pts, "name": name or lines[0]}
        self.shapes.append(shape)
        k = len(lines)
        for i, s in enumerate(lines):
            ty = y + h / 2 + 4 - (k - 1) * 8 + i * 16
            self.text(x + w / 2, ty, s, "tl tc", owner=shape)
            if len(s) * CW > w - 8:
                self.problems.append(f"label '{s}' too wide for its box")
        return shape

    def circle(self, cx, cy, r, lines, double=False, cls="fm s-acc sw2"):
        self.parts.append(f'<circle class="{cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        if double:
            self.parts.append(f'<circle class="ln" fill="none" cx="{cx:g}" cy="{cy:g}" r="{r - 6:g}"/>')
        pts = [(cx + r * math.cos(a / 180 * math.pi), cy + r * math.sin(a / 180 * math.pi)) for a in range(0, 360, 2)]
        shape = {"kind": "circle", "cx": cx, "cy": cy, "r": r, "pts": pts, "name": lines[0]}
        self.shapes.append(shape)
        k = len(lines)
        for i, s in enumerate(lines):
            ty = cy + 4 - (k - 1) * 8 + i * 16
            self.text(cx, ty, s, "tl tc", owner=shape)
            half = (r - (6 if double else 0)) * 2 - 8
            if len(s) * CW > half:
                self.problems.append(f"label '{s}' too wide for circle")
        return shape

    def dot(self, cx, cy, filled):
        if filled:
            self.parts.append(f'<circle class="fi" cx="{cx:g}" cy="{cy:g}" r="3.5"/>')
        else:
            self.parts.append(f'<circle class="fp s-acc sw2" cx="{cx:g}" cy="{cy:g}" r="3.5"/>')
        self.paths.append(("dot", [(cx + 3.5 * math.cos(a / 180 * math.pi), cy + 3.5 * math.sin(a / 180 * math.pi)) for a in range(0, 360, 30)]))

    def line(self, pts, cls="ln", arrow=False, name=""):
        d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts)
        mk = ' marker-end="url(#ah)"' if arrow else ""
        self.parts.append(f'<path class="{cls}" fill="none" d="{d}"{mk}/>')
        sample = []
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(1, int(math.hypot(x1 - x0, y1 - y0)))
            sample += [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n) for i in range(n + 1)]
        self.paths.append((name, sample))
        if arrow:
            self.ends.append((name, pts[-1]))

    def curve(self, p0, c, p1, cls="c1 sw2", arrow=True, name=""):
        d = f"M{p0[0]:g} {p0[1]:g} Q{c[0]:g} {c[1]:g} {p1[0]:g} {p1[1]:g}"
        mk = ' marker-end="url(#ah)"' if arrow else ""
        self.parts.append(f'<path class="{cls}" fill="none" d="{d}"{mk}/>')
        sample = []
        for i in range(0, 201):
            t = i / 200
            sample.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0],
                           (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1]))
        self.paths.append((name, sample))
        if arrow:
            self.ends.append((name, p1))

    def cubic(self, p0, c1, c2, p1, cls="c1 sw2", name=""):
        d = f"M{p0[0]:g} {p0[1]:g} C{c1[0]:g} {c1[1]:g} {c2[0]:g} {c2[1]:g} {p1[0]:g} {p1[1]:g}"
        self.parts.append(f'<path class="{cls}" fill="none" d="{d}" marker-end="url(#ah)"/>')
        sample = []
        for i in range(0, 201):
            t = i / 200
            u = 1 - t
            sample.append((u ** 3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t ** 3 * p1[0],
                           u ** 3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t ** 3 * p1[1]))
        self.paths.append((name, sample))
        self.ends.append((name, p1))

    def polygon(self, pts, cls="fp s-acc sw2"):
        self.parts.append('<polygon class="' + cls + '" points="' + " ".join(f"{x:g},{y:g}" for x, y in pts) + '"/>')
        sample = []
        for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]):
            n = max(1, int(math.hypot(x1 - x0, y1 - y0)))
            sample += [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n) for i in range(n + 1)]
        self.paths.append(("polygon", sample))

    # ---- checks -----------------------------------------------------------------------------
    def check(self):
        m = 4  # clear space around a label
        for i, t in enumerate(self.texts):
            x0, y0, x1, y1 = t["x0"] - m, t["y0"] - m, t["x1"] + m, t["y1"] + m
            if t["x0"] < 0 or t["x1"] > self.w or t["y0"] < 0 or t["y1"] > self.h:
                self.problems.append(f"label '{t['s']}' leaves the viewBox")
            for u in self.texts[i + 1:]:
                if not (x1 < u["x0"] or u["x1"] < x0 or y1 < u["y0"] or u["y1"] < y0):
                    self.problems.append(f"labels '{t['s']}' and '{u['s']}' overlap")
            for name, pts in self.paths:
                if t["own"] == name:
                    continue
                if any(x0 <= px <= x1 and y0 <= py <= y1 for px, py in pts):
                    self.problems.append(f"label '{t['s']}' touches line '{name}'")
            for sh in self.shapes:
                if t["owner"] is sh:
                    continue
                if any(x0 <= px <= x1 and y0 <= py <= y1 for px, py in sh["pts"]):
                    self.problems.append(f"label '{t['s']}' touches shape '{sh['name']}'")
        for name, (ex, ey) in self.ends:
            for t in self.texts:
                if t["owner"] is not None or name.startswith(t["s"]):
                    continue
                dx = max(t["x0"] - ex, 0, ex - t["x1"])
                dy = max(t["y0"] - ey, 0, ey - t["y1"])
                if math.hypot(dx, dy) < 10:
                    self.problems.append(f"arrow '{name}' ends within 10 px of label '{t['s']}'")
        return self.problems

    def html(self):
        body = "".join(self.parts)
        aria = self.aria.replace('"', "'")
        return (f'<figure class="{self.cls}"><svg viewBox="0 0 {self.w:g} {self.h:g}" role="img" aria-label="{aria}">'
                f'{body}</svg><figcaption>{self.caption}</figcaption></figure>')


def edge(c0, c1, r0, r1, gap=1):
    """Points on the circles' outlines along the line between their centres."""
    (x0, y0), (x1, y1) = c0, c1
    d = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / d, (y1 - y0) / d
    return (x0 + ux * (r0 + gap), y0 + uy * (r0 + gap)), (x1 - ux * (r1 + gap), y1 - uy * (r1 + gap))


figs = []

# ---------------------------------------------------------------------------------------------
# Figure 1: waterfall
# ---------------------------------------------------------------------------------------------
f = Fig("waterfall", 540, 290, "fig",
        "The waterfall model drawn as five boxes stepping down from top left to bottom right: Analysis, Design, Coding, Testing, Maintenance. A downward arrow leads from each stage to the next. A note says each stage is finished and signed off before the next starts.",
        "The waterfall model. Work flows one way, down the steps, and each stage is signed off before the next begins.")
names = ["Analysis", "Design", "Coding", "Testing", "Maintenance"]
for i, nm in enumerate(names):
    f.rect(10 + 95 * i, 14 + 56 * i, 120, 34, [nm])
for i in range(4):
    x = 120 + 95 * i
    f.line([(x, 14 + 56 * i + 34), (x, 14 + 56 * (i + 1))], "c1 sw2", True, f"w{i}")
f.text(14, 200, "Each stage is finished and signed off", "tl")
f.text(14, 218, "before the next stage starts", "tl")
figs.append(f)

# ---------------------------------------------------------------------------------------------
# Figure 2: iterative
# ---------------------------------------------------------------------------------------------
f = Fig("iterative", 340, 220, "fig small",
        "The iterative model drawn as a loop of four boxes: Analyse, Design, Code, Test and review, with arrows going round and back to Analyse. The centre says each lap makes a working version.",
        "The iterative model. Each lap round the loop produces a working version that users can try, and feedback starts the next lap.")
f.rect(10, 30, 120, 34, ["Analyse"])
f.rect(210, 30, 120, 34, ["Design"])
f.rect(210, 150, 120, 34, ["Code"])
f.rect(10, 150, 120, 34, ["Test and review"])
f.line([(130, 47), (210, 47)], "c1 sw2", True, "a-d")
f.line([(270, 64), (270, 150)], "c1 sw2", True, "d-c")
f.line([(210, 167), (130, 167)], "c1 sw2", True, "c-t")
f.line([(70, 150), (70, 64)], "c1 sw2", True, "t-a")
f.text(170, 100, "each lap makes")
f.text(170, 122, "a working version")
figs.append(f)

# ---------------------------------------------------------------------------------------------
# Figure 3: structure chart
# ---------------------------------------------------------------------------------------------
f = Fig("structure", 600, 430, "fig",
        "A structure chart. The top module ProcessParcel calls three modules: GetParcel, CalculateCharge and PrintReceipt. GetParcel passes up Mass and Zone as data and Valid as a flag. CalculateCharge receives Mass and Zone and passes up Charge. PrintReceipt receives Mass, Zone and Charge. CalculateCharge calls BaseRate, which receives Zone and passes up Rate, and Surcharge, which receives Mass and passes up Extra. An open circle at the tail of an arrow marks data and a filled circle marks a flag.",
        "Structure chart for the parcel program. Arrows show data passed between modules, not the order of execution: open circle for data, filled circle for a flag.")
f.text(10, 26, "open circle: data couple", "tl")
f.text(10, 44, "filled circle: flag", "tl")
f.rect(230, 20, 140, 34, ["ProcessParcel"])
level2 = [(95, 110, "GetParcel"), (300, 140, "CalculateCharge"), (505, 120, "PrintReceipt")]
for cx, w, nm in level2:
    f.rect(cx - w / 2, 200, w, 34, [nm])
f.line([(300, 54), (300, 84)], "ln", False, "root")
f.line([(95, 84), (505, 84)], "ln", False, "bus")
for cx, w, nm in level2:
    if cx != 300:
        f.line([(cx, 84), (cx, 200)], "ln", False, nm)
f.line([(300, 84), (300, 200)], "ln", False, "calc")


def couples(f, xl, seg_top, seg_bot, downs, ups):
    """Draw arrows beside a vertical connector: downs on the left, ups on the right. Items are (name, is_flag)."""
    for side, items, direction in (("l", downs, "down"), ("r", ups, "up")):
        n = len(items)
        if n == 0:
            continue
        total = n * 24 + (n - 1) * 10
        y = (seg_top + seg_bot) / 2 - total / 2
        x = xl - 14 if side == "l" else xl + 14
        for nm, flag in items:
            ya, yb = y, y + 24
            if direction == "down":
                f.line([(x, ya), (x, yb)], "c1", True, nm + "-d")
                f.dot(x, ya, flag)
            else:
                f.line([(x, yb), (x, ya)], "c1", True, nm + "-u")
                f.dot(x, yb, flag)
            if side == "l":
                f.text(x - 8, (ya + yb) / 2 + 4, nm, "tl te")
            else:
                f.text(x + 8, (ya + yb) / 2 + 4, nm, "tl")
            y += 34


couples(f, 95, 84, 200, [], [("Mass", False), ("Zone", False), ("Valid", True)])
couples(f, 300, 84, 200, [("Mass", False), ("Zone", False)], [("Charge", False)])
couples(f, 505, 84, 200, [("Mass", False), ("Zone", False), ("Charge", False)], [])
f.rect(165, 380, 110, 34, ["BaseRate"])
f.rect(320, 380, 120, 34, ["Surcharge"])
f.line([(300, 234), (300, 264)], "ln", False, "stub")
f.line([(220, 264), (380, 264)], "ln", False, "bus2")
f.line([(220, 264), (220, 380)], "ln", False, "base")
f.line([(380, 264), (380, 380)], "ln", False, "sur")
couples(f, 220, 264, 380, [("Zone", False)], [("Rate", False)])
couples(f, 380, 264, 380, [("Mass", False)], [("Extra", False)])
figs.append(f)

# ---------------------------------------------------------------------------------------------
# Figure 4: selection and iteration symbols
# ---------------------------------------------------------------------------------------------
f = Fig("symbols", 600, 200, "fig",
        "Two small structure charts side by side. Left, iteration: module Main calls Read and Show, and a curved arrow across the two lines means they repeat. Right, selection: module Menu has a diamond under it and calls Add or Delete, meaning one of them is chosen.",
        "The two control symbols. A curved arrow across the lines means the modules below repeat; a diamond means one of them is chosen.")
f.text(150, 16, "Iteration: repeat", "tl tc")
f.text(450, 16, "Selection: choose one", "tl tc")
f.rect(100, 30, 100, 34, ["Main"])
f.line([(150, 64), (150, 90)], "ln", False, "m-stub")
f.line([(60, 90), (240, 90)], "ln", False, "m-bus")
f.rect(15, 140, 90, 34, ["Read"])
f.rect(195, 140, 90, 34, ["Show"])
f.line([(60, 90), (60, 140)], "ln", False, "m-l")
f.line([(240, 90), (240, 140)], "ln", False, "m-r")
f.curve((46, 112), (150, 142), (254, 112), "c1 sw2", True, "loop")
f.rect(400, 30, 100, 34, ["Menu"])
f.polygon([(450, 64), (460, 74), (450, 84), (440, 74)])
f.line([(450, 84), (450, 100)], "ln", False, "s-stub")
f.line([(360, 100), (540, 100)], "ln", False, "s-bus")
f.rect(315, 140, 90, 34, ["Add"])
f.rect(495, 140, 90, 34, ["Delete"])
f.line([(360, 100), (360, 140)], "ln", False, "s-l")
f.line([(540, 100), (540, 140)], "ln", False, "s-r")
f.line([(300, 24), (300, 190)], "ln-m thin dash", False, "divider")
figs.append(f)

# ---------------------------------------------------------------------------------------------
# Figure 5: turnstile state-transition diagram
# ---------------------------------------------------------------------------------------------
f = Fig("turnstile", 440, 198, "fig small",
        "A state-transition diagram of a turnstile with two states, Locked and Unlocked. A start arrow points at Locked. The arrow from Locked to Unlocked is labelled coin slash unlock. The arrow from Unlocked back to Locked is labelled push slash lock. Locked has a loop labelled push slash nothing and Unlocked has a loop labelled coin slash nothing.",
        "A turnstile has two states. Each arrow is labelled event / action, and an arrow that returns to its own state is a loop.")
R = 36
L, U = (120, 120), (330, 120)
f.circle(L[0], L[1], R, ["Locked"])
f.circle(U[0], U[1], R, ["Unlocked"])
f.line([(20, 120), (L[0] - R - 1, 120)], "c1 sw2", True, "start")
f.text(14, 104, "start", "tl")
f.curve((L[0] + 28, L[1] - 24), (225, 62), (U[0] - 28, U[1] - 24), "c1 sw2", True, "lock-unlock")
f.text(225, 70, "coin / unlock", "tl tc")
f.curve((U[0] - 28, U[1] + 24), (225, 176), (L[0] + 28, L[1] + 24), "c1 sw2", True, "unlock-lock")
f.text(225, 187, "push / lock", "tl tc")
f.cubic((L[0] - 22, L[1] - 30), (L[0] - 70, L[1] - 100), (L[0] + 10, L[1] - 100), (L[0] + 2, L[1] - 37), "c1 sw2", "loopL")
f.cubic((U[0] - 2, U[1] - 37), (U[0] - 10, U[1] - 100), (U[0] + 70, U[1] - 100), (U[0] + 22, U[1] - 30), "c1 sw2", "loopU")
f.text(L[0] - 40, 20, "push / nothing", "tl tc")
f.text(U[0] + 40, 20, "coin / nothing", "tl tc")
figs.append(f)

# ---------------------------------------------------------------------------------------------
# Figure 6: PIN check state-transition diagram
# ---------------------------------------------------------------------------------------------
f = Fig("pin", 520, 445, "fig",
        "A state-transition diagram for a PIN check at a cash machine. States: Try 1, Try 2, Try 3, Accepted and Blocked. Accepted and Blocked are drawn as double circles because they are stop states. From each Try state, a correct PIN leads to Accepted with the action menu. A wrong PIN leads from Try 1 to Try 2 and from Try 2 to Try 3, with the action try again, and from Try 3 to Blocked with the action keep card.",
        "The PIN check. Double circles are stop states. Every Try state has one arrow for each event: correct PIN and wrong PIN.")
R, RD = 32, 40
t1, t2, t3, bl, ac = (80, 50), (80, 160), (80, 270), (80, 390), (430, 160)
f.circle(*t1, R, ["Try 1"])
f.circle(*t2, R, ["Try 2"])
f.circle(*t3, R, ["Try 3"])
f.circle(*bl, RD, ["Blocked"], double=True)
f.circle(*ac, RD, ["Accepted"], double=True)
f.line([(10, 50), (t1[0] - R - 1, 50)], "c1 sw2", True, "start")
f.text(10, 34, "start", "tl")
for a, b, ra, rb, nm, lab in ((t1, t2, R, R, "w1", ["wrong PIN", "try again"]), (t2, t3, R, R, "w2", ["wrong PIN", "try again"]), (t3, bl, R, RD, "w3", ["wrong PIN", "keep card"])):
    p, q = edge(a, b, ra, rb)
    f.line([p, q], "c1 sw2", True, nm)
    my = (p[1] + q[1]) / 2
    f.text(a[0] + 12, my - 6, lab[0], "tl")
    f.text(a[0] + 12, my + 16, lab[1], "tl")
for a, nm in ((t1, "c1"), (t2, "c2"), (t3, "c3")):
    p, q = edge(a, ac, R, RD)
    f.line([p, q], "c1 sw2", True, nm)
f.text(330, 100, "correct PIN / menu", "tl tc")
f.text(255, 150, "correct PIN / menu", "tl tc")
f.text(330, 232, "correct PIN / menu", "tl tc")
figs.append(f)

# ---------------------------------------------------------------------------------------------
# Figures 7 and 8: three-module structure charts (bill, login)
# ---------------------------------------------------------------------------------------------
def three(name, aria, caption, root, kids, legend=True):
    g = Fig(name, 520, 250, "fig", aria, caption)
    if legend:
        g.text(10, 26, "open circle: data couple", "tl")
        g.text(10, 44, "filled circle: flag", "tl")
    g.rect(200, 20, 120, 34, [root])
    g.line([(260, 54), (260, 80)], "ln", False, "root")
    g.line([(90, 80), (430, 80)], "ln", False, "bus")
    for (cx, w, nm, downs, ups) in kids:
        g.rect(cx - w / 2, 170, w, 34, [nm])
        g.line([(cx, 80), (cx, 170)], "ln", False, nm)
        couples(g, cx, 80, 170, downs, ups)
    return g


figs.append(three("bill",
    "A structure chart. The top module SplitBill calls three modules. GetBill passes up Total and People. CalculateShare receives Total and People and passes up Share. ShowShare receives Share. All are data couples, drawn with an open circle at the tail of each arrow.",
    "Structure chart for the bill-sharing program: every couple is data, so every arrow has an open circle.",
    "SplitBill",
    [(90, 110, "GetBill", [], [("Total", False), ("People", False)]),
     (260, 150, "CalculateShare", [("Total", False), ("People", False)], [("Share", False)]),
     (430, 110, "ShowShare", [("Share", False)], [])]))
figs.append(three("login",
    "A structure chart. The top module Login calls three modules. ReadEntry passes up Entry as data and Attempts as data. CheckEntry receives Entry and passes up Correct as a flag, drawn with a filled circle. ShowResult receives Correct as a flag and Attempts as data.",
    "Structure chart for a login program, used in Exam practice question 4.",
    "Login",
    [(90, 110, "ReadEntry", [], [("Entry", False), ("Attempts", False)]),
     (260, 150, "CheckEntry", [("Entry", False)], [("Correct", True)]),
     (430, 120, "ShowResult", [("Correct", True), ("Attempts", False)], [])]))

# ---------------------------------------------------------------------------------------------
out = []
bad = 0
for fg in figs:
    probs = fg.check()
    if probs:
        bad += 1
        print(f"[{fg.name}]")
        for p in sorted(set(probs)):
            print("  ", p)
    out.append(f"### {fg.name}\n{fg.html()}\n")
pathlib.Path(__file__).with_name("cs.development_figs.txt").write_text("\n".join(out), encoding="utf-8")
print("ok" if not bad else f"{bad} figure(s) with problems")
