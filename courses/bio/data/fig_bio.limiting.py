# data/fig_bio.limiting.py: builds the hand-drawn SVG figure of chapters/bio.limiting.md (Elodea apparatus) and checks label clearance.
# Run: py data/fig_bio.limiting.py -> prints the <figure>; clearance report on stderr.
# data/place_figs_p6.py bio.limiting replaces the @@FIG_<NAME> placeholder line of the chapter (later runs refresh it).
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["ELODEA"]
figs, problems = [], []

f = Fig("elodea")
# lamp on a stand
f.circle(44, 120, 16, "fh s-mute sw2")
f.line([(44, 136), (44, 200)], "ln")
f.line([(28, 200), (60, 200)], "ln")
f.text(44, 92, "lamp", "tl", "middle")
for y in (108, 120, 132):
    f.line([(64, y), (92, y)], "c4 sw2 dash", "ah")
    f.line([(118, y), (146, y)], "c4 sw2 dash", "ah")
# heat shield: a tank of water between lamp and beaker
f.rect(96, 76, 16, 130, "f2 s-acc2 sw2")
f.text(104, 226, "heat shield", "tl", "middle")
f.text(104, 242, "(water tank)", "tl", "middle")
# beaker with solution
f.line([(150, 66), (150, 96)], "ln")
f.line([(260, 66), (260, 96)], "ln")
f.rect(150, 96, 110, 110, "f2 s-acc2 sw2")
# thermometer
f.rect(156, 74, 8, 112, "fp ln")
f.circle(160, 190, 6, "fa s-acc sw2")
f.text(186, 54, "thermometer", "tl", "end")
f.leader((166, 58), (160, 76))
# inverted funnel with test tube over its stem
f.poly([(172, 196), (238, 196), (215, 140), (215, 120), (195, 120), (195, 140)], "fp ln")
f.line([(190, 138), (190, 66), (194, 62), (216, 62), (220, 66), (220, 138)], "ln")
f.rect(192, 64, 26, 22, "fp s-acc sw2")
# pondweed and bubbles
for pts in ([(190, 194), (186, 172), (192, 160)], [(205, 194), (208, 174), (202, 160)], [(221, 194), (226, 174), (219, 162)]):
    f.line(pts, "c2 sw2", check=False)
for (x, y) in ((205, 150), (209, 140), (204, 130)):
    f.parts.append(f'<circle class="fp s-acc sw2" cx="{x}" cy="{y}" r="2.5"/>')
# right-hand labels
f.text(272, 46, "gas collects", "tl")
f.leader((268, 50), (218, 72))
f.text(272, 112, "inverted funnel", "tl")
f.leader((268, 118), (228, 168))
f.text(272, 196, "pondweed", "tl")
f.leader((268, 192), (224, 184))
f.text(160, 262, "sodium hydrogencarbonate", "tl")
f.text(160, 278, "solution in a beaker", "tl")
# distance from lamp to beaker
f.line([(86, 262), (44, 262)], "c1 sw2", "ah")
f.line([(110, 262), (150, 262)], "c1 sw2", "ah")
f.text(98, 267, "d", "tl tb", "middle")
f.line([(44, 254), (44, 270)], "ln-m thin")
f.line([(150, 254), (150, 270)], "ln-m thin")
figs.append(f.svg((380, 292),
    "Apparatus for investigating photosynthesis in pondweed. A lamp on a stand shines through a tank of water that acts as a heat shield onto a beaker of sodium hydrogencarbonate solution. In the beaker, pondweed lies under an inverted funnel whose stem leads into a test tube, where the gas given off collects. A thermometer is in the beaker. The distance d from the lamp to the beaker is the measured light variable.",
    "Pondweed (Elodea) apparatus. The gas collected is mostly oxygen. The lamp distance d sets the light intensity, the sodium hydrogencarbonate sets the carbon dioxide available, and a water bath or the water tank keeps the temperature steady."))
problems.extend(f.check())
print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
