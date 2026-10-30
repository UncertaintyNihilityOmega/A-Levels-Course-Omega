# data/fig_bio.mock.p4.py: SVG figures of chapters/bio.mock.p4.md (Q4 sarcomere, Q10 gel) with clearance checks.
# Run: py data/fig_bio.mock.p4.py  -> prints each <figure> and a clearance report.
import math, sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "fig_bio.enzymes.py"), encoding="utf-8").read()
# reuse the Fig class and helpers (everything before the figure code)
exec(src.split("figs, problems = [], []")[0])

LEAD = "ln-m thin"
# ---------- Figure Q4: a relaxed sarcomere with parts P, Q, R, S ----------
f = Fig("sarcomere")
for y in (60, 82, 104):
    f.line([(40, y), (144, y)], "c2 sw2")
    f.line([(186, y), (290, y)], "c2 sw2")
for y in (67, 89):
    f.rect(82, y, 167, 8, "f1 s-acc sw2")
f.line([(40, 48), (40, 116)], "ln thick")
f.line([(290, 48), (290, 116)], "ln thick")
f.line([(144, 50), (144, 44), (186, 44), (186, 50)], LEAD)          # bracket over the H zone
f.text(165, 36, "S", "tl tb", "middle")
f.text(91, 28, "P", "tl tb", "middle")
f.line([(91, 36), (91, 57)], LEAD)
f.text(165, 150, "Q", "tl tb", "middle")
f.line([(165, 136), (165, 99)], LEAD)
f.text(290, 150, "R", "tl tb", "middle")
f.line([(290, 136), (290, 120)], LEAD)
svg1 = f.svg((330, 160), "A relaxed sarcomere in longitudinal section. Thin filaments run inwards from a thick vertical line at each end. Two thick filaments lie in the middle. Letter P marks a thin filament, Q marks a thick filament, R marks the vertical line at one end of the sarcomere, and S marks a bracket over the central gap between the ends of the thin filaments.",
             "A relaxed sarcomere (a drawing, not a micrograph). The length of the sarcomere is 2.4 µm; letters P to S are used in the question.")
bad1 = f.check()

# ---------- Figure Q10: an agarose gel ----------
g = Fig("gel")
GX0, GX1, GY0, GY1 = 56, 336, 38, 165
g.rect(GX0, GY0, GX1 - GX0, GY1 - GY0, "f1 s-acc sw2")
lanes = [84, 140, 196, 252, 308]
names = ["M", "WT", "GM1", "GM2", "W"]
ypos = lambda bp: 55 + (3 - math.log10(bp)) * 140
bands = {0: [1000, 750, 500, 250], 1: [250], 2: [250, 500], 3: [250], 4: []}
for cx, nm in zip(lanes, names):
    g.rect(cx - 15, GY0 + 4, 30, 5, "fp s-acc sw2")
    g.text(cx, 30, nm, "tl tb", "middle")
    for bp in bands[lanes.index(cx)]:
        y = ypos(bp)
        g.rect(cx - 15, y - 2.5, 30, 5, "f3 s-acc2 sw2")
for bp, lab in [(1000, "1000"), (750, "750"), (500, "500"), (250, "250 bp")]:
    g.text(50, ypos(bp) + 4, lab, "tl", "end")
g.line([(348, 70), (348, 150)], "c1 sw2", arrow="ah")
g.text(180, 184, "+", "tl tb", "middle")
svg2 = g.svg((360, 192), "An agarose gel with five lanes labelled M, WT, GM1, GM2 and W. Lane M, the size marker, has four bands at 1000, 750, 500 and 250 base pairs. Lane WT has one band at 250. Lane GM1 has two bands, at 250 and 500. Lane GM2 has one band at 250. Lane W has no bands. An arrow at the right shows DNA moving down the gel towards the positive electrode at the bottom.",
             "A gel after PCR and electrophoresis (a drawing). Lane M holds DNA fragments of known size; the wells are at the top and the positive electrode is at the bottom.")
bad2 = g.check()
print(svg1); print(); print(svg2)
print("\nCLEARANCE:", bad1 + bad2 or "none")

# ---------- paste into the chapter: replaces the placeholder lines @@FIG name@@ ----------
if "--paste" in sys.argv:
    assert not (bad1 + bad2), "fix the clearance report first"
    path = os.path.join(os.path.dirname(here), "chapters", "bio.mock.p4.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace("@@FIG sarcomere@@", svg1).replace("@@FIG gel@@", svg2)
    open(path, "w", encoding="utf-8").write(text)
    print("pasted")
