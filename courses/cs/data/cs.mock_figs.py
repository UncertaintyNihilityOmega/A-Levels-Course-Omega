# data/cs.mock_figs.py: builds and checks the two hand-drawn figures of the P21 mocks
# (the logic circuit of cs.mock.p1 Q5 and the flowchart of cs.mock.p2 Q2).
# Run: py data/cs.mock_figs.py   -> prints "ok" and writes data/cs.mock_figs.txt (one "### name" block per figure)
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent


def load(name, cut=None):
    src = (HERE / name).read_text(encoding="utf-8")
    if cut:
        src = src.split(cut)[0]
    ns = {"__name__": "mod", "__file__": str(HERE / name)}
    exec(compile(src, name, "exec"), ns)
    return ns


logic = load("cs.logic_fig.py", cut='FIGS = {')
flow = load("cs.algorithms_fig.py", cut="figs = {}")
figs = {}

# ---- Paper 1 Q5: X = (A XOR B) OR (B NOR C)
Fig = logic["Fig"]
f = Fig(400, 165, "Logic circuit with inputs A, B and C and output X. A and B feed an XOR gate whose output is labelled P. "
        "B and C feed a NOR gate whose output is labelled Q. B is joined to both gates by a dot. P and Q feed an OR gate whose output is X.",
        "The circuit for Question 5. The dot on B shows that B is joined to both gates. P and Q label the wires between the gates.")
f.gate("xor", "XOR", 110, 30)
f.gate("nor", "NOR", 110, 100)
f.gate("or", "OR", 280, 65)
logic["inputs"](f, [("A", 40), ("B", 85), ("C", 130)], None)
f.wire((30, 40), f.pin("xor", 0))
f.wire((30, 85), (70, 85))
f.wire((70, 85), (70, 60), f.pin("xor", 1))
f.wire((70, 85), (70, 110), f.pin("nor", 0))
f.dot(70, 85)
f.wire((30, 130), f.pin("nor", 1))
f.wire(f.out("xor"), (240, 50), (240, 75), f.pin("or", 0))
f.wire(f.out("nor"), (250, 120), (250, 95), f.pin("or", 1))
o = f.out("or")
f.wire(o, (o[0] + 50, o[1]))
f.text(o[0] + 56, o[1] + 4, "X", bold=True)
f.text(190, 40, "P")
f.text(196, 140, "Q")
bad = f.check()
assert not bad, bad
figs["circuit"] = f.svg()

# ---- Paper 2 Q2: the flowchart with three logic errors
Chart = flow["Chart"]
c = Chart(520, 668)
LX, RX = 140, 405
s = c.term(LX, 28, "Start")
i0 = c.proc(LX, 104, ["Total ← 0", "Taller ← 0", "Count ← 1"])
d1 = c.dec(LX, 200, "Count < 8?")
i1 = c.io(LX, 282, "INPUT Height")
p1 = c.proc(LX, 350, "Total ← Height")
d2 = c.dec(LX, 440, "Height >= 170?")
p2 = c.proc(LX, 535, "Taller ← Taller + 1")
p3 = c.proc(LX, 620, "Count ← Count + 1")
m = c.proc(RX, 200, "Mean ← Total / 8")
o = c.io(RX, 282, "OUTPUT Taller, Mean")
e = c.term(RX, 354, "End")
c.arrow([s["bot"], i0["top"]], src=s, dst=i0)
c.arrow([i0["bot"], d1["top"]], src=i0, dst=d1)
c.arrow([d1["bot"], i1["top"]], src=d1, dst=i1)
c.arrow([i1["bot"], p1["top"]], src=i1, dst=p1)
c.arrow([p1["bot"], d2["top"]], src=p1, dst=d2)
c.arrow([d2["bot"], p2["top"]], src=d2, dst=p2)
c.arrow([p2["bot"], p3["top"]], src=p2, dst=p3)
c.arrow([d1["right"], m["left"]], src=d1, dst=m)
c.arrow([m["bot"], o["top"]], src=m, dst=o)
c.arrow([o["bot"], e["top"]], src=o, dst=e)
BUS = 330
JY = 578
c.arrow([d2["right"], (BUS, 440), (BUS, JY), (LX, JY)], src=d2, dst=None)
c.arrow([p3["left"], (24, 620), (24, 160), (LX, 160)], src=p3, dst=None)
c.label(d1["right"][0] + 8, 192, "No")
c.label(d1["cx"] + 8, d1["cy"] + d1["hh"] + 22, "Yes")
c.label(d2["right"][0] + 8, 432, "No")
c.label(d2["cx"] + 8, d2["cy"] + d2["hh"] + 22, "Yes")
c.check()
figs["flow"] = c.svg(
    "A flowchart. Start, then a process box with Total gets 0, Taller gets 0 and Count gets 1, then a decision Count less than 8. "
    "The exit labelled No leads right to Mean gets Total divided by 8, then OUTPUT Taller and Mean, then End. "
    "The exit labelled Yes leads down to INPUT Height, then Total gets Height, then a decision Height greater than or equal to 170. "
    "Yes leads down to Taller gets Taller plus 1, then Count gets Count plus 1. No leads right, down and back left to join the arrow above Count gets Count plus 1. "
    "An arrow from Count gets Count plus 1 goes left, up and back to the line above the first decision.",
    "A flowchart for a program that reads the heights of 8 athletes and outputs how many are taller than 170 cm and the mean height. It contains three logic errors.")

(HERE / "cs.mock_figs.txt").write_text("\n\n".join(f"### {k}\n{v}" for k, v in figs.items()), encoding="utf-8")
print("ok", list(figs))
