# data/fig_bio.nerves.py: builds the hand-drawn SVG figures of chapters/bio.nerves.md and checks label clearance.
# Run: py data/fig_bio.nerves.py -> prints the <figure>s (clearance report on stderr). data/place_figs_p14.py bio.nerves places them.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig, bez

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["REFLEX", "NEURONES", "RESTING", "AP", "SALT"]
figs, problems = [], []

# ---------------------------------------------------------------- 1 reflex arc
f = Fig("reflex")
boxes = [("stimulus", "fm s-acc sw2"), ("sensory receptor", "f1 s-acc sw2"), ("sensory neurone", "f1 s-acc sw2"),
         ("intermediate neurone", "f2 s-acc2 sw2"), ("motor neurone", "f1 s-acc sw2"),
         ("effector (muscle or gland)", "fm2 s-acc sw2"), ("response", "fm s-acc sw2")]
X0, W_, H_, STEP = 20, 230, 28, 46
for i, (t, cls) in enumerate(boxes):
    y = 10 + i * STEP
    f.rect(X0, y, W_, H_, cls, rx=5)
    f.text(X0 + W_ / 2, y + 19, t, "tl", "middle")
    if i < len(boxes) - 1:
        f.line([(X0 + W_ / 2, y + H_ + 2), (X0 + W_ / 2, y + STEP - 3)], "ln", "ah")
# bracket for the CNS around the intermediate neurone
y3 = 10 + 3 * STEP
f.line([(262, y3), (268, y3), (268, y3 + H_), (262, y3 + H_)], "ln-m thin")
f.text(276, y3 + 14, "in the", "tl")
f.text(276, y3 + 28, "CNS", "tl")
# receptor to effector labels
f.text(276, 10 + 2 * STEP + 19, "impulses", "tl")
f.text(276, 10 + 4 * STEP + 19, "impulses", "tl")
figs.append(f.svg((340, 10 + 6 * STEP + H_ + 12),
    "Flow diagram of a reflex arc. A stimulus is detected by a sensory receptor. A sensory neurone carries impulses to an intermediate neurone inside the central nervous system. A motor neurone carries impulses to an effector, a muscle or a gland, which produces the response.",
    "A reflex arc. Impulses pass in one direction: receptor, sensory neurone, intermediate (relay) neurone in the central nervous system, motor neurone, effector."))
problems.extend(f.check())

# ---------------------------------------------------------------- 2 sensory and motor neurones
f = Fig("neurones")
f.text(6, 16, "Sensory neurone", "tl tb")
y = 82
f.line([(42, y), (322, y)], "ln")                       # fibre
f.line([(42, y), (20, 62)], "ln")
f.line([(42, y), (16, y)], "ln")
f.line([(42, y), (20, 102)], "ln")
for sx, ex in ((46, 96), (102, 152), (158, 208), (222, 262), (268, 308)):
    f.rect(sx, y - 7, ex - sx, 14, "fm s-acc sw2", rx=3)
f.line([(214, y), (214, 62)], "ln")                    # stalk to the cell body
f.circle(214, 48, 13, "f1 s-acc sw2")
f.circle(214, 48, 5, "f2 s-acc2 sw2")
f.text(234, 52, "cell body", "tl")
for (ex, ey) in ((336, 68), (338, 82), (336, 96)):
    f.line([(308, y), (ex - 4, ey)], "ln")
    f.circle(ex, ey, 3.5, "f3 s-acc2 sw2")
f.text(6, 40, "dendrite endings", "tl")
f.leader((24, 44), (22, 64))
f.text(100, 60, "myelin sheath", "tl")
f.leader((126, 64), (126, y - 8))
# brackets under the fibre
f.line([(46, 108), (46, 114), (208, 114), (208, 108)], "ln-m thin")
f.text(127, 132, "dendron (long)", "tl", "middle")
f.line([(222, 108), (222, 114), (322, 114), (322, 108)], "ln-m thin")
f.text(272, 132, "axon", "tl", "middle")
f.line([(8, 150), (56, 150)], "ln", "ah")
f.text(64, 154, "direction of impulses", "tl")
oy = 172
f.text(6, oy + 16, "Motor neurone", "tl tb")
y = oy + 84
f.circle(46, y, 17, "f1 s-acc sw2")
f.circle(46, y, 6, "f2 s-acc2 sw2")
for (a, b) in (((36, y - 15), (14, y - 36)), ((46, y - 17), (46, y - 40)), ((56, y - 15), (76, y - 36)), ((32, y + 13), (14, y + 30))):
    f.line([a, b], "ln")
f.line([(63, y), (322, y)], "ln")
for sx, ex in ((90, 150), (156, 216), (222, 282)):
    f.rect(sx, y - 7, ex - sx, 14, "fm s-acc sw2", rx=3)
for (ex, ey) in ((338, y - 14), (340, y), (338, y + 14)):
    f.line([(322, y), (ex - 4, ey)], "ln")
    f.circle(ex, ey, 3.5, "f3 s-acc2 sw2")
f.text(90, oy + 36, "dendrites", "tl")
f.leader((100, oy + 40), (78, y - 38))
f.text(6, oy + 134, "cell body", "tl")
f.leader((36, oy + 122), (42, y + 18))
f.text(100, oy + 60, "node of Ranvier", "tl")
f.leader((153, oy + 64), (153, y - 2))
f.text(248, oy + 36, "axon terminals", "tl")
f.leader((300, oy + 40), (332, y - 17))
f.line([(66, y + 26), (66, y + 32), (322, y + 32), (322, y + 26)], "ln-m thin")
f.text(194, y + 50, "axon (very long)", "tl", "middle")
f.line([(8, oy + 160), (56, oy + 160)], "ln", "ah")
f.text(64, oy + 164, "direction of impulses", "tl")
figs.append(f.svg((350, oy + 176),
    "Two neurones drawn as lines. A sensory neurone: branched dendrite endings at the left, a long dendron wrapped in myelin sheath segments with gaps, a cell body on a short side branch, a short axon and axon terminals at the right; impulses travel left to right. A motor neurone: a cell body at the left end with several dendrites, one very long axon with myelin sheath segments and nodes of Ranvier between them, and axon terminals at the right end.",
    "A sensory neurone (top) has its cell body off to the side of one long fibre; a motor neurone (bottom) has its cell body at one end and a very long axon. Both have a myelin sheath with nodes of Ranvier, and both end in axon terminals."))
problems.extend(f.check())

# ---------------------------------------------------------------- 3 resting membrane
f = Fig("resting")
f.text(6, 16, "outside the axon", "tl tb")
for (x, yy) in ((100, 40), (140, 52), (200, 38), (236, 54), (284, 40), (320, 54), (60, 46), (170, 50)):
    f.circle(x, yy, 4.5, "f3 s-acc2 sw2")
for (x, yy) in ((318, 78), (30, 70)):
    f.circle(x, yy, 4.5, "f1 s-acc sw2")
MY0, MY1 = 150, 190
f.rect(10, MY0, 320, MY1 - MY0, "fm s-acc sw2")
# pump
f.rect(15, MY0 - 10, 90, MY1 - MY0 + 20, "f1 s-acc sw2", rx=6)
f.text(60, MY0 + 15, "Na⁺/K⁺", "tl", "middle")
f.text(60, MY0 + 31, "pump", "tl", "middle")
f.text(60, 100, "3 Na⁺ out", "tl", "middle")
f.line([(60, MY0 - 14), (60, 114)], "c1 sw2", "ah")
f.line([(60, MY1 + 14), (60, MY1 + 38)], "c2 sw2", "ah")
f.text(60, MY1 + 58, "2 K⁺ in", "tl", "middle")
# K+ leak channel
f.rect(150, MY0 - 10, 12, MY1 - MY0 + 20, "f1 s-acc sw2")
f.rect(178, MY0 - 10, 12, MY1 - MY0 + 20, "f1 s-acc sw2")
f.text(170, 100, "K⁺ out", "tl", "middle")
f.line([(170, MY0 - 14), (170, 114)], "c2 sw2 dash", "ah")
f.text(170, MY1 + 34, "K⁺ leak", "tl", "middle")
f.text(170, MY1 + 50, "channel", "tl", "middle")
# voltage-gated Na+ channel, closed
f.rect(250, MY0 - 10, 12, MY1 - MY0 + 20, "f1 s-acc sw2")
f.rect(278, MY0 - 10, 12, MY1 - MY0 + 20, "f1 s-acc sw2")
f.rect(262, MY0 + 8, 16, 24, "f2 s-acc2 sw2")
f.text(270, 100, "no Na⁺ entry", "tl", "middle")
f.text(270, MY1 + 34, "voltage-gated", "tl", "middle")
f.text(270, MY1 + 50, "Na⁺ channel", "tl", "middle")
f.text(270, MY1 + 66, "(closed)", "tl", "middle")
f.text(6, 276, "inside the axon", "tl tb")
for (x, yy) in ((100, 296), (140, 308), (190, 294), (236, 306), (284, 296), (320, 308), (60, 310), (24, 296)):
    f.circle(x, yy, 4.5, "f1 s-acc sw2")
for (x, yy) in ((166, 316), (306, 280)):
    f.circle(x, yy, 4.5, "f3 s-acc2 sw2")
for (x, yy) in ((134, 282), (216, 280), (262, 316), (356, 0)):
    if x < 340:
        f.rect(x - 4, yy - 4, 8, 8, "fa s-acc sw2")
# legend
f.circle(14, 346, 4.5, "f3 s-acc2 sw2")
f.text(24, 350, "Na⁺", "tl")
f.circle(70, 346, 4.5, "f1 s-acc sw2")
f.text(80, 350, "K⁺", "tl")
f.rect(114, 342, 8, 8, "fa s-acc sw2")
f.text(128, 350, "large anion (negative)", "tl")
figs.append(f.svg((340, 362),
    "The membrane of a resting axon. Outside the axon there are many sodium ions and few potassium ions. Inside there are many potassium ions, few sodium ions and large negatively charged anions. The sodium-potassium pump moves 3 sodium ions out and 2 potassium ions in. Potassium ions diffuse out through an open potassium leak channel. The voltage-gated sodium channel is closed, so no sodium ions enter.",
    "The resting axon membrane. The pump keeps sodium ions high outside and potassium ions high inside. Potassium ions leak out through open channels while the voltage-gated sodium channels are shut, so the inside is about 70 mV more negative than the outside."))
problems.extend(f.check())

# ---------------------------------------------------------------- 4 action potential graph
PTS = [(0, -70), (0.5, -70), (0.75, -50), (1.0, 35), (1.5, -20), (2.0, -75), (3.0, -80), (4.0, -72), (5.0, -70)]


def mono(pts):
    """Fritsch-Carlson monotone cubic interpolation: returns a function."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    n = len(xs)
    d = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [d[0]] + [0 if d[i - 1] * d[i] <= 0 else (d[i - 1] + d[i]) / 2 for i in range(1, n - 1)] + [d[-1]]
    for i in range(n - 1):
        if d[i] == 0:
            m[i] = m[i + 1] = 0
        else:
            a, b = m[i] / d[i], m[i + 1] / d[i]
            s = a * a + b * b
            if s > 9:
                t = 3 / s ** 0.5
                m[i], m[i + 1] = t * a * d[i], t * b * d[i]

    def fn(x):
        for i in range(n - 1):
            if x <= xs[i + 1] + 1e-12:
                h = xs[i + 1] - xs[i]
                t = (x - xs[i]) / h
                h00, h10, h01, h11 = 2 * t**3 - 3 * t**2 + 1, t**3 - 2 * t**2 + t, -2 * t**3 + 3 * t**2, t**3 - t**2
                return h00 * ys[i] + h10 * h * m[i] + h01 * ys[i + 1] + h11 * h * m[i + 1]
        return ys[-1]
    return fn


V = mono(PTS)
if __name__ == "__main__":
    pass
f = Fig("ap")
PX0, PX1, PY0, PY1 = 56, 326, 30, 250
ypx = lambda v: PY0 + (50 - v) * (200 / 140)
xpx = lambda t: PX0 + t * (PX1 - PX0) / 5
f.text(6, 14, "membrane potential / mV", "tl")
f.line([(PX0, PY0 - 6), (PX0, PY1 + 8)], "ax")
f.line([(PX0 - 4, PY1 + 4), (PX1 + 4, PY1 + 4)], "ax", "ahm")
f.text(PX1, PY1 + 42, "time / ms", "tl", "end")
for v in (40, 0, -40, -80):
    f.line([(PX0 - 4, ypx(v)), (PX0, ypx(v))], "ax")
    f.text(PX0 - 8, ypx(v) + 3, ("+" if v > 0 else ("−" if v < 0 else "")) + str(abs(v)), "ts", "end")
for t in range(6):
    f.line([(xpx(t), PY1 + 4), (xpx(t), PY1 + 8)], "ax")
    f.text(xpx(t), PY1 + 24, str(t), "ts", "middle")
f.line([(PX0, ypx(-50)), (PX1, ypx(-50))], "ln-m thin dash")
f.line([(PX0, ypx(-70)), (PX1, ypx(-70))], "ln-m thin dash")
f.text(PX1, ypx(-50) - 7, "threshold, about −50 mV", "tl", "end")
f.text(PX1, ypx(-70) - 9, "resting, −70 mV", "tl", "end")
curve = [(round(xpx(t / 40), 1), round(ypx(V(t / 40)), 1)) for t in range(0, 201)]
f.line(curve, "c1 sw2")
for (lab, x, yy) in (("1", 66, 191), ("2", 82, ypx(-20)), ("3", 126, ypx(42)), ("4", 146, ypx(-5)), ("5", 218, 238)):
    f.text(x, yy, lab, "tl tb", "middle")
LEG = ["1  resting potential, channels closed", "2  depolarisation: Na⁺ channels open, Na⁺ in",
       "3  peak: Na⁺ channels close", "4  repolarisation: K⁺ channels open, K⁺ out",
       "5  hyperpolarisation, then back to rest"]
for i, s in enumerate(LEG):
    f.text(8, PY1 + 66 + i * 16, s, "tl")
figs.append(f.svg((340, PY1 + 66 + 4 * 16 + 14),
    "Graph of membrane potential in millivolts against time in milliseconds for one action potential. The potential is at the resting potential of minus 70 millivolts, rises past the threshold of about minus 50 millivolts to a peak of about plus 35 millivolts at 1 millisecond, falls below resting to about minus 80 millivolts at 3 milliseconds and returns to minus 70 millivolts by 5 milliseconds. Numbers 1 to 5 mark the phases: resting, depolarisation, peak, repolarisation and hyperpolarisation.",
    "One action potential (a model trace). Numbers 1 to 5 match the list under the graph."))
problems.extend(f.check())

# ---------------------------------------------------------------- 5 saltatory conduction
f = Fig("salt")
CY0, CY1 = 76, 116
f.rect(10, CY0, 320, CY1 - CY0, "f1 s-acc sw2")
for sx, ex in ((14, 96), (124, 206), (234, 316)):
    f.rect(sx, CY0 - 18, ex - sx, 18, "fm s-acc sw2")
    f.rect(sx, CY1, ex - sx, 18, "fm s-acc sw2")
f.text(20, 100, "axon", "tl")
f.text(170, 108, "local circuit", "tl", "middle")
f.line([(124, 90), (206, 90)], "c4 dash sw2", "ah")
f.text(110, 22, "Na⁺ in", "tl", "middle")
f.line([(110, 38), (110, CY0 - 3)], "c1 sw2", "ah")
f.text(220, 22, "Na⁺ in next", "tl", "middle")
f.line([(220, 38), (220, CY0 - 3)], "c1 sw2 dash", "ah")
f.text(14, 156, "myelin sheath", "tl")
f.leader((50, 145), (50, CY1 + 20))
f.text(120, 156, "node of Ranvier", "tl")
f.leader((152, 145), (112, CY1 + 4))
f.line([(8, 182), (56, 182)], "ln", "ah")
f.text(64, 186, "direction of impulse", "tl")
figs.append(f.svg((340, 198),
    "Longitudinal view of a myelinated axon. Segments of myelin sheath lie above and below the axon with bare gaps, the nodes of Ranvier, between them. Sodium ions enter at one node where the action potential is. A dashed arrow inside the axon shows a local circuit carrying positive charge to the next node, where sodium ions will enter next. The impulse moves from left to right.",
    "Saltatory conduction. Sodium ions enter only at the nodes. The local circuit spreads depolarisation inside the axon to the next node, so the action potential jumps from node to node."))
problems.extend(f.check())

print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
