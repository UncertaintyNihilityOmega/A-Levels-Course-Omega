# data/fig_bio.photosynthesis.py: builds the hand-drawn SVG figures of chapters/bio.photosynthesis.md and checks label clearance.
# Run: py data/fig_bio.photosynthesis.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.photosynthesis replaces the @@FIG_<NAME> placeholder lines of the chapter (later runs refresh them).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, arc_pts, ellipse, seg_box

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["CHLORO", "SPECTRA", "CHROM", "NONCYC", "CYCLIC", "CALVIN"]
figs, problems = [], []
BOX = "f1 s-acc sw2"
ARR = "c1 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def box(f, x, y, w, h, lines, cls=BOX, bold=False):
    f.rect(x, y, w, h, cls)
    n = len(lines)
    for i, s in enumerate(lines):
        yy = y + h / 2 + 5 + (i - (n - 1) / 2) * 15
        f.text(x + w / 2, round(yy, 1), s, "tl tb" if bold else "tl", "middle")


def lead_clear(f, a, b, name, skip=()):
    """A leader may not cross a label box other than its own (checked by Fig) nor any drawn edge except at its end."""
    return


# ---------- 1. chloroplast ----------
f = Fig("chloro")
cx, cy = 190, 150
ellipse(f, cx, cy, 94, 64, "fm s-acc sw2")
ellipse(f, cx, cy, 87, 57, "f1 s-acc sw2")


def granum(f, gx, y0, n=4):
    for i in range(n):
        f.rect(gx - 17, y0 + i * 9, 34, 6, "f2 s-acc2 sw2", rx=3)


granum(f, 148, 112)
granum(f, 192, 124)
granum(f, 236, 100)
f.line([(165, 128), (175, 136)], "ln")
f.line([(209, 134), (219, 120)], "ln")
f.circle(118, 160, 8, "fp ln")                       # circular DNA
f.parts.append('<ellipse class="fp s-acc sw2" cx="224" cy="188" rx="14" ry="9"/>')   # starch grain
for (x, y) in [(140, 182), (150, 190)]:               # lipid droplets
    f.circle(x, y, 4.5, "fa s-acc sw2")
for (x, y) in [(262, 150), (267, 159), (259, 165)]:   # 70S ribosomes
    f.parts.append(f'<circle class="fi" cx="{x}" cy="{y}" r="2.4"/>')
# left labels
f.text(6, 36, "envelope", "tl")
f.text(6, 50, "(2 membranes)", "tl")
f.leader((60, 56), (116, 115))
f.text(6, 116, "stroma", "tl")
f.leader((52, 118), (118, 140))
f.text(6, 212, "circular DNA", "tl")
f.leader((70, 198), (113, 164))
f.text(6, 262, "lipid droplet", "tl")
f.leader((60, 248), (137, 184))
# top label
f.text(190, 16, "single thylakoid", "tl", "middle")
f.leader((188, 20), (171, 131))
# right labels
f.text(294, 36, "thylakoid", "tl")
f.leader((290, 40), (250, 103))
f.text(294, 82, "granum", "tl")
f.leader((290, 86), (252, 128))
f.text(294, 170, "70S", "tl")
f.text(294, 184, "ribosomes", "tl")
f.leader((290, 174), (270, 162))
f.text(294, 226, "starch", "tl")
f.text(294, 240, "grain", "tl")
f.leader((290, 230), (237, 193))
done(f, (360, 274),
     "Labelled drawing of a chloroplast. Two membranes form the envelope. Inside, stacks of flattened thylakoids called grana are joined by single thylakoids, in a fluid stroma that also holds a circular DNA molecule, 70S ribosomes, a starch grain and lipid droplets.",
     "A chloroplast in section (a drawing, not a photograph). The grana hold the light-dependent stage; the stroma holds the enzymes of the light-independent stage.")

# ---------- 2. absorption and action spectra ----------
f = Fig("spectra")


def G(x, mu, sd):
    return math.exp(-((x - mu) / sd) ** 2 / 2)


def chl_a(l): return 0.95 * G(l, 432, 17) + 0.72 * G(l, 664, 13) + 0.05 * G(l, 540, 60)
def chl_b(l): return 0.82 * G(l, 457, 17) + 0.46 * G(l, 642, 13) + 0.04 * G(l, 540, 60)
def caro(l): return 0.72 * G(l, 452, 17) + 0.62 * G(l, 482, 14) + 0.03 * G(l, 540, 60)
def act(l):
    return 0.55 * chl_a(l) + 0.4 * chl_b(l) + 0.3 * caro(l)


amax = max(act(l) for l in range(400, 701))
X = lambda l: 56 + (l - 400) / 300 * 260
panels = [(190, 130, "A  Absorption spectra", "absorbance"), (410, 110, "B  An action spectrum", "rate of photosynthesis")]
for (base, hgt, ttl, ylab) in panels:
    f.text(10, base - hgt - 38, ttl, "tl tb")
    f.text(10, base - hgt - 18, ylab, "tl")
    f.line([(56, base), (56, base - hgt - 8)], "ax", "ahm")
    f.line([(52, base), (322, base)], "ax", "ahm")
    for l in (400, 500, 600, 700):
        f.line([(X(l), base), (X(l), base + 4)], "ax", check=False)
        f.text(X(l), base + 17, str(l), "ts", "middle")
    f.text(190, base + 36, "wavelength / nm", "tl", "middle")


def curve(fn, base, hgt, cls, norm=1.0):
    pts = [(round(X(l), 1), round(base - hgt * fn(l) / norm, 1)) for l in range(400, 701, 4)]
    f.line(pts, cls)
    return pts


def pt(fn, base, hgt, l, norm=1.0):
    return (round(X(l), 1), round(base - hgt * fn(l) / norm, 1))


pa = curve(chl_a, 190, 130, "c1 sw2")
pb = curve(chl_b, 190, 130, "c2 sw2")
pc = curve(caro, 190, 130, "c3 sw2 dash")
pd = curve(act, 410, 110, "c1 sw2", amax)
f.text(150, 62, "chlorophyll a", "tl")
f.leader((146, 60), pt(chl_a, 190, 130, 432))
f.text(158, 116, "chlorophyll b", "tl")
f.leader((266, 120), pt(chl_b, 190, 130, 642))
f.text(150, 152, "carotene", "tl")
f.leader((148, 148), pt(caro, 190, 130, 490))
f.text(150, 358, "action", "tl")
f.text(150, 372, "spectrum", "tl")
f.leader((166, 376), pt(act, 410, 110, 540, amax))
done(f, (340, 458),
     "Two graphs against wavelength in nanometres from 400 to 700. Graph A, absorption spectra of chlorophyll a, chlorophyll b and carotene: chlorophyll a absorbs most in the blue-violet near 430 nanometres and the red near 660, chlorophyll b near 450 and 640, and carotene broadly from 420 to 500; all three absorb very little between 500 and 600. Graph B, an action spectrum: the rate of photosynthesis has two peaks, in the blue-violet and in the red, and a low point in the green, matching the combined absorption.",
     "Schematic spectra (idealised curves, not measured data). The action spectrum follows the combined absorption of all the pigments, with a low point where little light is absorbed.")

# ---------- 3. chromatogram ----------
f = Fig("chrom")
f.rect(104, 24, 120, 252, "fp ln")
f.line([(104, 252), (224, 252)], "ln-m thin dash")
f.line([(104, 44), (224, 44)], "ln-m thin dash")
spots = [("carotene", 0.95), ("xanthophyll", 0.71), ("chlorophyll a", 0.65), ("chlorophyll b", 0.45)]
y_or, y_fr = 252, 44
for name, rf in spots:
    y = y_or - rf * (y_or - y_fr)
    f.parts.append(f'<ellipse class="fa s-acc sw2" cx="164" cy="{y:.1f}" rx="20" ry="5"/>')
    f.segs += []
lab_y = {"carotene": 66, "xanthophyll": 84, "chlorophyll a": 118, "chlorophyll b": 164}
for name, rf in spots:
    y = y_or - rf * (y_or - y_fr)
    f.text(236, lab_y[name], name, "tl")
    f.leader((232, lab_y[name] - 4), (186, y))
f.text(236, 40, "solvent front", "tl")
f.text(236, 268, "origin (pencil)", "tl")
f.text(236, 284, "spots start here", "tl")
f.line([(90, y_or), (90, y_fr + 2)], ARR, "ah")
f.text(78, 150, "b", "tl tb", "end")
yb = y_or - 0.45 * (y_or - y_fr)
f.line([(124, y_or), (124, yb)], "c2 sw2", "ah")
f.line([(124, yb), (140, yb)], "ln-m thin dash")
f.text(132, 230, "a", "tl tb")
f.text(164, 308, "solvent level below the origin", "tl", "middle")
f.line([(104, 276), (224, 276)], "ln-m thin")
done(f, (360, 322),
     "A paper chromatogram of a leaf extract. The origin line is at the bottom and the solvent front at the top. From the top the four spots are carotene, xanthophyll, chlorophyll a and chlorophyll b. Arrow b is the distance moved by the solvent, from the origin to the solvent front. Arrow a is the distance moved by the pigment, from the origin to the centre of the chlorophyll b spot.",
     "A chromatogram (a drawing; real spots are smeared and fade). Rf = a ÷ b, with both distances measured from the origin; here a is for chlorophyll b.")

# ---------- 4. non-cyclic photophosphorylation ----------
f = Fig("noncyc")
f.text(10, 20, "thylakoid space", "tl tb")
f.text(10, 36, "(high H⁺ concentration)", "tl")
MT, MB = 190, 218
f.rect(15, MT, 380, MB - MT, "f2 s-acc2 sw2")
f.rect(40, 170, 56, 68, "fm s-acc sw2", rx=6)
f.text(68, 209, "PSII", "tl tb", "middle")
f.rect(272, 170, 56, 68, "fm s-acc sw2", rx=6)
f.text(300, 209, "PSI", "tl tb", "middle")
for gx in (152, 214):
    f.parts.append(f'<ellipse class="fm s-acc sw2" cx="{gx}" cy="204" rx="17" ry="21"/>')
    f.segs += [((gx - 17, 204), (gx + 17, 204), "e")]
f.line([(98, 204), (132, 204)], "c4 sw2 dash", "ah")
f.line([(172, 204), (192, 204)], "c4 sw2 dash", "ah")
f.line([(234, 204), (268, 204)], "c4 sw2 dash", "ah")
f.text(112, 181, "e⁻", "tl", "middle")
f.text(250, 181, "e⁻", "tl", "middle")
for gx in (152, 214):
    f.line([(gx, 180), (gx, 148)], "c3 sw2", "ah")
    f.text(gx, 140, "H⁺", "tl", "middle")
f.text(10, 64, "light", "tl")
f.line([(30, 74), (50, 166)], "c2 sw2", "ah")
f.text(262, 80, "light", "tl")
f.line([(292, 90), (296, 166)], "c2 sw2", "ah")
f.text(76, 96, "photolysis:", "tl")
f.text(76, 112, "2H₂O → 4H⁺ + 4e⁻ + O₂", "tl")
f.leader((80, 118), (72, 168))
f.rect(352, 186, 24, 34, "fm s-acc sw2")
f.circle(364, 240, 17, "f1 s-acc sw2")
f.line([(364, 128), (364, 182)], "c3 sw2", "ah")
f.text(302, 108, "H⁺ flow back", "tl")
f.text(306, 312, "ATP synthase", "tl")
f.leader((364, 298), (364, 258))
f.text(296, 328, "ADP + Pi → ATP", "tl")
f.line([(300, 240), (300, 286)], "c4 sw2 dash", "ah")
f.text(292, 264, "NADP + 2H⁺ + 2e⁻", "tl", "end")
f.text(292, 280, "→ reduced NADP", "tl", "end")
f.line([(152, 228), (152, 330)], "ln-m thin")
f.text(152, 346, "electron transport chain", "tl", "middle")
f.text(10, 392, "thylakoid membrane", "tl")
f.leader((24, 380), (24, 215))
f.text(10, 432, "stroma", "tl tb")
f.text(10, 448, "(low H⁺ concentration)", "tl")
done(f, (400, 462),
     "Non-cyclic photophosphorylation on the thylakoid membrane. Light is absorbed by photosystem II. Water is split in the thylakoid space (photolysis) into protons, electrons and oxygen, and the electrons replace those lost from photosystem II. Energetic electrons pass along the electron transport chain to photosystem I, releasing energy that pumps protons from the stroma into the thylakoid space. Light is also absorbed by photosystem I, and its electrons pass to NADP in the stroma, forming reduced NADP. Protons flow back into the stroma through ATP synthase, which makes ATP from ADP and phosphate.",
     "Non-cyclic photophosphorylation. Both photosystems absorb light; electrons flow from water through PSII, the chain and PSI to NADP. ATP, reduced NADP and oxygen are the products.")

# ---------- 5. cyclic photophosphorylation ----------
f = Fig("cyclic")
f.text(10, 20, "thylakoid space", "tl tb")
f.text(10, 36, "(high H⁺ concentration)", "tl")
MT, MB = 120, 148
f.rect(15, MT, 330, MB - MT, "f2 s-acc2 sw2")
f.rect(36, 100, 56, 68, "fm s-acc sw2", rx=6)
f.text(64, 139, "PSI", "tl tb", "middle")
for gx in (150, 214):
    f.parts.append(f'<ellipse class="fm s-acc sw2" cx="{gx}" cy="134" rx="17" ry="21"/>')
    f.segs += [((gx - 17, 134), (gx + 17, 134), "e")]
f.line([(94, 134), (130, 134)], "c4 sw2 dash", "ah")
f.line([(170, 134), (192, 134)], "c4 sw2 dash", "ah")
f.line([(214, 158), (214, 196), (64, 196), (64, 172)], "c4 sw2 dash", "ah")
f.text(139, 216, "electrons return to PSI", "tl", "middle")
f.text(112, 111, "e⁻", "tl", "middle")
for gx in (150, 214):
    f.line([(gx, 110), (gx, 78)], "c3 sw2", "ah")
    f.text(gx, 70, "H⁺", "tl", "middle")
f.text(10, 60, "light", "tl")
f.line([(30, 74), (48, 96)], "c2 sw2", "ah")
f.rect(290, 116, 24, 34, "fm s-acc sw2")
f.circle(302, 170, 17, "f1 s-acc sw2")
f.line([(302, 60), (302, 112)], "c3 sw2", "ah")
f.text(250, 50, "H⁺ flow back", "tl")
f.text(240, 220, "ATP synthase", "tl")
f.leader((300, 204), (302, 189))
f.text(232, 236, "ADP + Pi → ATP", "tl")
f.text(10, 262, "stroma", "tl tb")
f.text(10, 278, "(low H⁺ concentration)", "tl")
done(f, (350, 292),
     "Cyclic photophosphorylation. Light is absorbed by photosystem I only. Its electrons pass along the electron transport chain, which pumps protons from the stroma into the thylakoid space, and then return to photosystem I. Protons flow back into the stroma through ATP synthase, which makes ATP. No water is split, no oxygen is released and no reduced NADP is made.",
     "Cyclic photophosphorylation. The electrons go round a loop and come back to PSI, so the only product is ATP.")

# ---------- 6. Calvin cycle ----------
f = Fig("calvin")
bx = 160
box(f, bx, 20, 120, 40, ["3 × RuBP (5C)"])
box(f, bx, 124, 120, 40, ["6 × GP (3C)"])
box(f, bx, 232, 120, 40, ["6 × TP (3C)"])
f.line([(220, 60), (220, 120)], ARR, "ah")
f.text(230, 84, "3 CO₂ added by", "tl")
f.text(230, 100, "rubisco (fixation)", "tl")
f.line([(220, 164), (220, 228)], ARR, "ah")
f.text(230, 184, "reduction, using", "tl")
f.text(230, 200, "6 ATP and", "tl")
f.text(230, 216, "6 reduced NADP", "tl")
f.line([(160, 252), (40, 252), (40, 40), (156, 40)], ARR, "ah")
f.text(48, 150, "5 × TP are used", "tl")
f.text(48, 166, "to regenerate", "tl")
f.text(48, 182, "3 × RuBP,", "tl")
f.text(48, 198, "using 3 ATP", "tl")
f.line([(220, 272), (220, 318)], "c2 sw2", "ah")
f.text(230, 296, "1 × TP leaves", "tl")
f.text(220, 336, "carbohydrates,", "tl", "middle")
f.text(220, 352, "lipids, amino acids", "tl", "middle")
done(f, (360, 366),
     "The Calvin cycle with carbon numbers, for three carbon dioxide molecules. Three RuBP (5C) combine with three carbon dioxide molecules, catalysed by rubisco, to give six GP (3C). Six GP are reduced to six TP (3C) using 6 ATP and 6 reduced NADP. One TP leaves the cycle to make carbohydrates, lipids and amino acids. The other five TP are used to regenerate three RuBP, using 3 ATP.",
     "The Calvin cycle for 3 CO₂: 15 carbon atoms in RuBP plus 3 in CO₂ make 18 in six GP; five of the six TP (15 carbon atoms) regenerate RuBP and one TP (3 carbon atoms) is the net gain.")

print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
