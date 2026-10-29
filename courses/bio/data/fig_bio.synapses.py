# data/fig_bio.synapses.py: builds the hand-drawn SVG figures of chapters/bio.synapses.md and checks label clearance.
# Run: py data/fig_bio.synapses.py -> prints the <figure>s (clearance report on stderr). data/place_figs_p14.py bio.synapses places them.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["SYNAPSE", "FIBRE", "SARCO", "CYCLE"]
figs, problems = [], []

# ---------------------------------------------------------------- 1 cholinergic synapse
f = Fig("synapse")
# axon and presynaptic knob
f.rect(150, 4, 40, 30, "f1 s-acc sw2")
f.rect(110, 30, 120, 100, "f1 s-acc sw2", rx=14)
f.rect(124, 52, 26, 14, "f2 s-acc2 sw2", rx=6)               # mitochondrion
f.circle(196, 56, 8, "fp s-acc sw2")                          # vesicles
f.circle(214, 84, 8, "fp s-acc sw2")
f.circle(170, 96, 8, "fp s-acc sw2")
for (x, y) in ((196, 56), (214, 84), (170, 96)):
    f.parts.append(f'<circle class="f3" cx="{x - 2}" cy="{y}" r="2"/>')
    f.parts.append(f'<circle class="f3" cx="{x + 2}" cy="{y + 2}" r="2"/>')
f.circle(186, 126, 9, "fp s-acc sw2")                         # vesicle fusing with the membrane
f.parts.append('<circle class="f3" cx="184" cy="124" r="2"/><circle class="f3" cx="189" cy="128" r="2"/>')
# voltage-gated calcium channel in the presynaptic membrane
f.rect(116, 122, 8, 16, "f1 s-acc sw2")
f.rect(138, 122, 8, 16, "f1 s-acc sw2")
f.circle(126, 158, 4, "f3 s-acc2 sw2")                        # Ca2+ ions
f.circle(138, 168, 4, "f3 s-acc2 sw2")
f.line([(131, 176), (131, 144)], "c2 sw2", "ah")
# ACh crossing the cleft
for (x, y) in ((198, 148), (206, 158), (196, 168), (212, 178)):
    f.parts.append(f'<circle class="f2 s-acc sw2" cx="{x}" cy="{y}" r="2.5"/>')
f.line([(204, 134), (204, 190)], "c1 sw2 dash", "ah")
f.poly([(218, 168), (226, 164), (232, 170), (228, 178), (220, 178)], "f2 s-acc2 sw2")   # acetylcholinesterase
# postsynaptic neurone
f.rect(110, 206, 120, 130, "f1 s-acc sw2", rx=14)
f.rect(196, 200, 8, 16, "f1 s-acc sw2")
f.rect(214, 200, 8, 16, "f1 s-acc sw2")
f.line([(209, 224), (209, 262)], "c3 sw2", "ah")
# left labels
f.text(4, 40, "presynaptic", "tl")
f.text(4, 54, "knob", "tl")
f.leader((48, 58), (112, 60))
f.text(4, 88, "mitochondrion", "tl")
f.leader((96, 86), (126, 62))
f.text(4, 124, "voltage-gated", "tl")
f.text(4, 138, "Ca²⁺ channel", "tl")
f.leader((92, 132), (116, 130))
f.text(4, 180, "synaptic cleft", "tl")
f.text(4, 252, "postsynaptic", "tl")
f.text(4, 266, "neurone", "tl")
f.leader((60, 258), (112, 258))
f.text(140, 196, "Ca²⁺ in", "tl")
# right labels
f.text(244, 86, "ACh vesicle", "tl")
f.leader((242, 82), (224, 82))
f.text(244, 120, "exocytosis", "tl")
f.leader((242, 116), (196, 124))
f.text(244, 148, "ACh diffuses", "tl")
f.text(238, 184, "acetyl-", "tl")
f.text(238, 198, "cholinesterase", "tl")
f.leader((236, 176), (230, 174))
f.text(244, 220, "receptor", "tl")
f.text(244, 234, "(Na⁺ channel)", "tl")
f.leader((242, 218), (224, 210))
f.text(203, 262, "Na⁺ in", "tl", "end")
figs.append(f.svg((340, 346),
    "A cholinergic synapse. Above, the presynaptic knob, with a mitochondrion, vesicles of acetylcholine (ACh), one vesicle fusing with the presynaptic membrane, and a voltage-gated calcium ion channel with calcium ions entering. Below it, the synaptic cleft: ACh diffuses across and acetylcholinesterase breaks it down. At the bottom the postsynaptic neurone has receptor proteins that are sodium ion channels; sodium ions enter when ACh binds.",
    "A cholinergic synapse (not to scale: the real cleft is about 20 nm wide). Calcium ions enter the knob, vesicles release acetylcholine (ACh) by exocytosis, ACh diffuses across the cleft and opens sodium ion channels, and acetylcholinesterase breaks it down."))
problems.extend(f.check())

# ---------------------------------------------------------------- 2 muscle fibre
f = Fig("fibre")
# motor neurone ending above the fibre
f.rect(158, 4, 24, 22, "f1 s-acc sw2")
f.rect(132, 26, 76, 24, "f1 s-acc sw2", rx=8)
f.text(4, 24, "neuromuscular", "tl")
f.text(4, 38, "junction", "tl")
f.leader((66, 42), (130, 42))
f.text(192, 16, "motor neurone", "tl")
f.leader((190, 12), (178, 12))
# fibre
FX0, FX1, FY0, FY1 = 14, 244, 56, 310
f.rect(FX0, FY0, FX1 - FX0, FY1 - FY0, "fm s-acc sw2", rx=8)
for y0 in (80, 152, 224):
    f.rect(30, y0, 198, 40, "fm2 s-acc sw2", rx=3)
    for x in range(52, 228, 22):
        f.line([(x, y0 + 6), (x, y0 + 34)], "ln-m thin", check=False)
# T-tubule from the surface, between the myofibrils; sacs of sarcoplasmic reticulum beside it
f.rect(122, FY0, 10, 236, "f2 s-acc2 sw2")
for y0 in (124, 196):
    f.rect(106, y0, 8, 24, "f3 s-acc2 sw2")
    f.rect(140, y0, 8, 24, "f3 s-acc2 sw2")
# mitochondrion and nucleus
f.rect(172, 203, 30, 10, "f1 s-acc sw2", rx=5)
f.rect(190, 62, 40, 12, "f2 s-acc2 sw2", rx=5)
# labels (right column), in the order of the parts from top to bottom
f.text(252, 66, "nucleus", "tl")
f.leader((250, 62), (231, 66))
f.text(252, 92, "sarcolemma", "tl")
f.leader((250, 88), (244, 84))
f.text(252, 116, "myofibril", "tl")
f.leader((250, 112), (226, 106))
f.text(252, 140, "sarcoplasmic", "tl")
f.text(252, 154, "reticulum", "tl")
f.leader((250, 136), (149, 136))
f.text(248, 212, "mitochondrion", "tl")
f.leader((246, 208), (203, 208))
f.text(252, 284, "T-tubule", "tl")
f.leader((250, 280), (133, 280))
figs.append(f.svg((344, 322),
    "A muscle fibre in longitudinal section with the end of a motor neurone at the top forming a neuromuscular junction. The surface membrane is the sarcolemma. A T-tubule passes in from the surface between the myofibrils, with sacs of sarcoplasmic reticulum on each side of it. A mitochondrion lies between the myofibrils and a nucleus lies near the surface.",
    "A muscle fibre (simplified). The T-tubule is a fold of the sarcolemma that passes into the fibre next to the sarcoplasmic reticulum, which stores calcium ions. The fibre is a single cell with many nuclei."))
problems.extend(f.check())

# ---------------------------------------------------------------- 3 sarcomere, relaxed and contracted (to scale, 100 px = 1 um)
f = Fig("sarco")
M = 165


def panel(oy, L, title, hzone):
    Zl, Zr = M - L * 50, M + L * 50
    A0, A1 = M - 80, M + 80
    f.text(6, oy + 16, title, "tl tb")
    if hzone:
        f.line([(M - 25, oy + 24), (M - 25, oy + 20), (M + 25, oy + 20), (M + 25, oy + 24)], "ln-m thin")
        f.text(M, oy + 11, "H", "tl tb", "middle")
    for (a, b, lab) in ((Zl, A0, "I"), (A0, A1, "A"), (A1, Zr, "I")):
        f.line([(a, oy + 52), (a, oy + 48), (b, oy + 48), (b, oy + 52)], "ln-m thin")
        f.text((a + b) / 2, oy + 41, lab, "tl tb", "middle")
    for ry in (64, 86, 108):
        f.line([(Zl, oy + ry), (Zl + 100, oy + ry)], "c2 sw2")
        f.line([(Zr - 100, oy + ry), (Zr, oy + ry)], "c2 sw2")
    for ry in (71, 93):
        f.rect(A0, oy + ry, 160, 8, "f1 s-acc sw2")
    f.line([(M, oy + 56), (M, oy + 122)], "ln-m thin dash")
    f.line([(Zl, oy + 56), (Zl, oy + 122)], "ln thick")
    f.line([(Zr, oy + 56), (Zr, oy + 122)], "ln thick")
    f.text(Zl, oy + 138, "Z", "tl tb", "middle")
    f.text(Zr, oy + 138, "Z", "tl tb", "middle")
    f.text(M, oy + 138, "M", "tl tb", "middle")


panel(4, 2.5, "Relaxed", True)
panel(164, 2.0, "Contracted", False)
f.text(M, 164 + 14, "no H zone", "tl", "middle")
LEG = ["I  light band: thin (actin) filaments only", "A  dark band: the thick (myosin) filaments", "H  zone: myosin only; gone when contracted",
       "M  line: middle of the thick filaments", "Z  line: ends of the sarcomere, actin attached"]
for i, s in enumerate(LEG):
    f.text(6, 334 + i * 16, s, "tl")
figs.append(f.svg((340, 334 + 4 * 16 + 14),
    "Two sarcomeres drawn to the same scale. Relaxed, 2.5 micrometres long: Z lines at each end with thin actin filaments attached, two thick myosin filaments in the middle, an M line at the centre, light I bands at each end, a dark A band of 1.6 micrometres and a short H zone in the middle of it. Contracted, 2.0 micrometres: the Z lines are closer, the A band is the same length, the I bands are shorter and the H zone has disappeared.",
    "A sarcomere relaxed (above) and contracted (below), drawn to scale. The thin filaments slide inwards; the A band does not change length. Letters are explained under the drawing."))
problems.extend(f.check())

# ---------------------------------------------------------------- 4 cross-bridge cycle (four panels)
f = Fig("cycle")
OYS = [4, 158, 284, 410]
XL, XR = 10, 240


def cpanel(i, title, dx, head, tip, label_atp=None, sites_open=True, detached=False, extra=None):
    oy = OYS[i]
    f.text(6, oy + 14, title, "tl tb")
    f.rect(XL, oy + 26, XR - XL, 10, "f1 s-acc sw2")              # thick filament
    f.rect(XL, oy + 86, XR - XL, 10, "f2 s-acc2 sw2")             # thin filament
    # myosin head: base on the thick filament at x=170, tip at (tip, oy + 86 or lifted)
    ty = oy + (74 if detached else 84)
    f.poly([(164, oy + 36), (176, oy + 36), (tip + 3, ty), (tip - 3, ty)], "f1 s-acc sw2")
    # binding sites on the thin filament and tropomyosin
    for k in range(-2, 3):
        sx = 190 + dx + 30 * k
        if XL + 6 < sx < XR - 6:
            f.parts.append(f'<path class="ln" d="M{sx - 3} {oy + 86}L{sx} {oy + 82}L{sx + 3} {oy + 86}"/>')
    ty2 = oy + 102 if sites_open else oy + 84
    return oy


# panel 1: calcium bound, tropomyosin moved, head binds
oy = cpanel(0, "1  Ca²⁺ binds troponin; head binds actin", 0, True, 190)
f.circle(100, oy + 109, 5, "f3 s-acc2 sw2")                      # troponin
f.circle(113, oy + 109, 3, "fp s-acc sw2")                       # Ca2+
f.line([(XL + 4, oy + 100), (XR - 4, oy + 100)], "c4 sw2")        # tropomyosin moved to the side
f.text(246, oy + 66, "myosin head", "tl")
f.leader((244, oy + 62), (184, oy + 70))
f.text(246, oy + 36, "thick", "tl")
f.text(246, oy + 50, "(myosin)", "tl")
f.leader((244, oy + 32), (XR, oy + 31))
f.text(246, oy + 92, "thin (actin)", "tl")
f.leader((244, oy + 88), (XR, oy + 91))
f.text(246, oy + 108, "tropomyosin", "tl")
f.leader((244, oy + 104), (XR - 6, oy + 100))
f.text(246, oy + 126, "troponin with", "tl")
f.text(246, oy + 140, "Ca²⁺ bound", "tl")
f.leader((244, oy + 122), (106, oy + 112))
# panel 2: power stroke
oy = cpanel(1, "2  Power stroke: actin slides", -30, True, 160)
f.text(246, oy + 66, "ADP + Pi", "tl")
f.text(246, oy + 80, "released", "tl")
f.line([(100, oy + 114), (50, oy + 114)], "c1 sw2", "ah")
f.text(108, oy + 118, "to M line", "tl")
# panel 3: ATP binds, head detaches
oy = cpanel(2, "3  ATP binds; head detaches", -30, True, 160, detached=True)
f.text(246, oy + 60, "ATP", "tl tb")
# panel 4: ATP hydrolysed, head recocked
oy = cpanel(3, "4  ATP hydrolysed; head recocked", -30, True, 190, detached=True)
f.text(246, oy + 52, "ATP →", "tl")
f.text(246, oy + 66, "ADP + Pi", "tl")
figs.append(f.svg((340, OYS[3] + 126),
    "Four stages of the cross-bridge cycle. 1: calcium ions are bound to troponin, tropomyosin has moved aside and a myosin head carrying ADP and phosphate binds to actin. 2: the head tilts in the power stroke and the thin filament slides towards the M line, releasing ADP and phosphate. 3: ATP binds to the head, which detaches from actin. 4: ATP is hydrolysed and the head returns to its original position, ready to bind further along the actin.",
    "The cross-bridge cycle. The actin binding sites are shown as small marks on the thin filament; in stage 1 tropomyosin has been moved off them by calcium ions bound to troponin."))
problems.extend(f.check())

print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
