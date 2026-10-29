# data/fig_bio.genetech.py: figures of chapters/bio.genetech.md. Run: py data/fig_bio.genetech.py
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit_p18 import Fig, place, report

figs, objs = {}, []

# ---------------------------------------------------------------- 1 EcoRI sticky ends
f = Fig("restrict")
c = lambda i: 104 + 22 * i
top, bot = "GAATTC", "CTTAAG"
f.text(10, 16, "A  EcoRI finds its recognition site", "tl tb")
for i in range(6):
    f.text(c(i), 48, top[i], "tl", "middle")
    f.text(c(i), 82, bot[i], "tl", "middle")
    f.line([(c(i), 55), (c(i), 68)], "ln-m thin dash")
f.text(c(0) - 24, 48, "5′", "tl", "middle")
f.text(c(5) + 24, 48, "3′", "tl", "middle")
f.text(c(0) - 24, 82, "3′", "tl", "middle")
f.text(c(5) + 24, 82, "5′", "tl", "middle")
f.line([(c(0) + 11, 30), (c(0) + 11, 55)], "c2 sw2")
f.line([(c(4) + 11, 68), (c(4) + 11, 94)], "c2 sw2")
f.text(10, 116, "Both strands read GAATTC")
f.text(10, 132, "from 5′ to 3′ (a palindrome)")
f.text(10, 164, "B  Staggered cuts leave sticky ends", "tl tb")
xl = lambda i: c(i) - 22      # left fragment
xr = lambda i: c(i) + 22      # right fragment
f.text(xl(0), 212, "G", "tl", "middle")
for i in range(5):
    f.text(xl(i), 246, bot[i], "tl", "middle")
for i in range(1, 6):
    f.text(xr(i), 212, top[i], "tl", "middle")
f.text(xr(5), 246, "G", "tl", "middle")
f.line([(xl(0), 219), (xl(0), 232)], "ln-m thin dash")
f.line([(xr(5), 219), (xr(5), 232)], "ln-m thin dash")
x0, x1 = xr(1) - 6, xr(4) + 6
f.line([(x0, 195), (x0, 190), (x1, 190), (x1, 195)], "ln-m thin")
f.text((x0 + x1) / 2, 182, "sticky end", "tl", "middle")
x0, x1 = xl(1) - 6, xl(4) + 6
f.line([(x0, 257), (x0, 262), (x1, 262), (x1, 257)], "ln-m thin")
f.text((x0 + x1) / 2, 282, "sticky end", "tl", "middle")
figs["restrict"] = f.svg((300, 296),
    "Two panels. A: the DNA sequence GAATTC on the top strand, 5 prime to 3 prime, paired with CTTAAG on the bottom strand, with a cut between G and A on the top strand and between A and G on the bottom strand. B: after the cut, the left piece keeps G paired with C and has the single-stranded bottom bases TTAA; the right piece keeps the top bases AATT unpaired above a single G; each unpaired stretch is labelled sticky end.",
    "A restriction endonuclease (EcoRI) cuts the two strands at different points. B: each piece is left with a single-stranded stretch, a sticky end, that can pair with a complementary sticky end on another piece cut with the same enzyme.")
objs.append(f)

# ---------------------------------------------------------------- 2 recombinant plasmid
f = Fig("plasmid")
def arc(cx, cy, r, a0, a1, large):
    p = lambda a: (cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    return f"M{x0:.1f} {y0:.1f}A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}"
# row 1
f.raw(f'<path class="ln thick" d="{arc(60, 60, 26, 20, 340, 1)}"/>')
f.rect(130, 52, 100, 16, "f2 s-acc2 sw2")
f.text(60, 102, "plasmid", "tl", "middle")
f.text(180, 92, "gene", "tl", "middle")
f.text(10, 124, "1  The same restriction enzyme cuts")
f.text(10, 140, "the plasmid and the gene.")
f.line([(10, 152), (330, 152)], "ln-m thin")
# row 2
f.circle(250, 206, 26, "ln thick fp")
f.raw(f'<path class="c2 sw3" d="{arc(250, 206, 26, -60, 60, 0)}"/>')
f.text(250, 172, "gene", "tl", "middle")
f.text(250, 250, "recombinant plasmid", "tl", "middle")
f.text(10, 196, "2  DNA ligase seals the")
f.text(10, 212, "sticky-end joins:")
f.text(10, 228, "recombinant plasmid.")
f.line([(10, 268), (330, 268)], "ln-m thin")
# row 3
f.rect(230, 282, 96, 68, "f1 s-acc sw2", rx=24)
f.circle(260, 316, 14, "ln thick fp")
f.text(278, 368, "bacterium", "tl", "middle")
f.text(10, 300, "3  Bacteria are treated")
f.text(10, 316, "(calcium ions, heat")
f.text(10, 332, "shock) so plasmids enter.")
f.line([(10, 388), (330, 388)], "ln-m thin")
f.text(10, 408, "4  Marker gene: cells that glow")
f.text(10, 424, "have the plasmid and express it.")
figs["plasmid"] = f.svg((340, 436),
    "Four steps drawn one under another. 1: a gene shown as a bar and a bacterial plasmid shown as an open ring, cut by the same restriction enzyme. 2: DNA ligase seals the gene into the ring, making a recombinant plasmid. 3: bacteria are treated with calcium ions and heat shock so that the plasmid enters a bacterium. 4: cells with the marker gene glow, showing that they have the plasmid and express it.",
    "Making and selecting bacteria that carry a recombinant plasmid.")
objs.append(f)

# ---------------------------------------------------------------- 3 PCR cycle
f = Fig("pcr")
f.text(10, 18, "1  Denaturation, about 95 °C", "tl tb")
for x in range(34, 141, 12):
    f.line([(x, 38), (x, 50)], "ln-m thin")
f.line([(34, 38), (140, 38)], "ln")
f.line([(34, 50), (140, 50)], "ln")
f.line([(150, 44), (180, 44)], "ln", "ah", check=False)
f.line([(190, 34), (300, 34)], "ln")
f.line([(190, 56), (300, 56)], "ln")
f.text(10, 84, "hydrogen bonds between strands break")
f.line([(10, 94), (330, 94)], "ln-m thin")
f.text(10, 112, "2  Annealing, about 55–65 °C", "tl tb")
f.line([(30, 128), (310, 128)], "ln")
f.line([(30, 178), (310, 178)], "ln")
f.line([(230, 140), (270, 140)], "c2 sw3")
f.line([(70, 166), (110, 166)], "c2 sw3")
f.text(250, 160, "primer", "tl", "middle")
f.text(90, 152, "primer", "tl", "middle")
f.line([(10, 196), (330, 196)], "ln-m thin")
f.text(10, 214, "3  Extension, about 72 °C", "tl tb")
f.line([(30, 232), (310, 232)], "ln")
f.line([(30, 284), (310, 284)], "ln")
f.line([(270, 246), (40, 246)], "c2 sw2", "ah", check=False)
f.line([(70, 270), (300, 270)], "c2 sw2", "ah", check=False)
f.text(170, 262, "new strands", "tl", "middle")
f.text(10, 308, "Taq polymerase adds nucleotides to")
f.text(10, 324, "each primer, making new strands.")
figs["pcr"] = f.svg((340, 336),
    "Three stages of one PCR cycle. 1: denaturation at about 95 degrees Celsius, a double strand of DNA becomes two single strands as hydrogen bonds break. 2: annealing at about 55 to 65 degrees Celsius, one primer binds near the right end of the upper template strand and one near the left end of the lower template strand. 3: extension at about 72 degrees Celsius, Taq polymerase extends each primer to make a new strand, the upper one leftwards and the lower one rightwards.",
    "One cycle of PCR. After extension there are two double-stranded molecules where there was one.")
objs.append(f)

# ---------------------------------------------------------------- 4 gel
f = Fig("gel")
f.rect(50, 30, 250, 192, "f1 s-acc sw2")
lanes = [90, 170, 250]
for x, nm in zip(lanes, ["ladder", "sample 1", "sample 2"]):
    f.rect(x - 22, 30, 44, 10, "fp ln")
    f.text(x, 20, nm, "tl", "middle")
Y = lambda L: 44 + 84 * (math.log10(6000) - math.log10(L))
for L in (5000, 3000, 2000, 1000, 500, 200, 100):
    y = Y(L)
    f.rect(68, y - 2, 44, 4, "f2 s-acc2")
    f.text(44, y + 3, str(L), "ts", "end")
for L, h in ((1900, 9), (1200, 5)):
    f.rect(148, Y(L) - h / 2, 44, h, "fi")
for L, h in ((3800, 5), (1200, 5)):
    f.rect(228, Y(L) - h / 2, 44, h, "fi")
f.text(309, 46, "−", "tl", "middle")
f.text(309, 214, "+", "tl", "middle")
f.text(50, 244, "sizes of the ladder bands in bp", "ts")
figs["gel"] = f.svg((320, 256),
    "A gel with three lanes. Wells at the top, marked minus; the far end is marked plus. The ladder lane has seven bands, 5000, 3000, 2000, 1000, 500, 200 and 100 base pairs from the top down. Sample 1 has a thick band at 1900 base pairs and a band at 1200. Sample 2 has bands at 3800 and 1200. Shorter fragments are nearer the plus end.",
    "A gel after electrophoresis. DNA moves from the wells (−) towards the + end, and shorter fragments travel further. Sample 1 is the 5000 bp DNA cut at 1200 and 3100 bp: two fragments of 1900 bp make one thicker band.")
objs.append(f)

report(objs)
place("bio.genetech", figs)
