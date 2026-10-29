# data/fig_bio.respiration.py: builds the hand-drawn SVG figures of chapters/bio.respiration.md and checks label clearance.
# Run: py data/fig_bio.respiration.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.respiration replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, arc_pts, ellipse

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["OVERVIEW", "GLYCO", "KREBS", "CHEMI", "MITO"]
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


# ---------- 1. the four stages ----------
f = Fig("overview")
f.rect(10, 8, 380, 96, "fm s-acc sw2")
f.text(20, 26, "cytoplasm", "tl tb")
f.text(200, 24, "glucose (6C)", "tl", "middle")
f.line([(200, 34), (200, 50)], ARR, "ah")
box(f, 125, 52, 150, 40, ["1  Glycolysis"], BOX, True)
f.rect(10, 140, 380, 272, "fm s-acc sw2")
f.text(380, 158, "mitochondrion", "tl tb", "end")
box(f, 125, 164, 150, 40, ["2  Link reaction"], BOX, True)
box(f, 125, 248, 150, 40, ["3  Krebs cycle"], BOX, True)
box(f, 75, 342, 250, 52, ["4  Oxidative phosphorylation", "(inner membrane)"], "f2 s-acc2 sw2", True)
f.line([(200, 92), (200, 160)], ARR, "ah")
f.text(212, 126, "2 pyruvate (3C)", "tl")
f.line([(200, 204), (200, 244)], ARR, "ah")
f.text(212, 230, "acetyl CoA (2C)", "tl")
f.line([(200, 288), (200, 338)], ARR, "ah")
f.text(212, 312, "reduced NAD,", "tl")
f.text(212, 326, "reduced FAD", "tl")
f.line([(279, 176), (318, 176)], "c2 sw2", "ah")
f.text(326, 181, "CO₂", "tl")
f.line([(279, 260), (318, 260)], "c2 sw2", "ah")
f.text(326, 265, "CO₂", "tl")
f.text(286, 199, "in the matrix", "tl")
f.text(286, 283, "in the matrix", "tl")
f.line([(121, 72), (30, 72), (30, 368), (71, 368)], ARR, "ah")
f.line([(121, 184), (30, 184)], ARR)
f.text(40, 236, "reduced", "tl")
f.text(40, 250, "NAD", "tl")
done(f, (400, 424),
     "Overview of aerobic respiration in four stages. Stage 1, glycolysis, takes place in the cytoplasm: glucose with six carbons is converted to two pyruvate with three carbons each. Pyruvate enters the mitochondrion. Stage 2, the link reaction, and stage 3, the Krebs cycle, take place in the matrix, joined by acetyl coenzyme A, and each releases carbon dioxide. Stage 4, oxidative phosphorylation, is on the inner mitochondrial membrane. Reduced NAD from stages 1 and 2, and reduced NAD and reduced FAD from stage 3, go to stage 4.",
     "The four stages of aerobic respiration and where each takes place in a eukaryotic cell. Reduced NAD and reduced FAD carry hydrogen to stage 4, where most of the ATP is made; oxygen is the final electron acceptor there.")

# ---------- 2. glycolysis ----------
f = Fig("glyco")
box(f, 10, 16, 130, 30, ["glucose (6C)"])
f.line([(75, 46), (75, 86)], ARR, "ah")
f.text(90, 62, "2 ATP used:", "tl")
f.text(90, 78, "phosphorylation", "tl")
box(f, 10, 90, 150, 46, ["fructose 1,6-", "bisphosphate (6C)"])
f.line([(75, 136), (75, 176)], ARR, "ah")
f.text(90, 154, "splitting", "tl")
box(f, 10, 180, 200, 30, ["2 × triose phosphate (3C)"])
f.line([(75, 210), (75, 290)], ARR, "ah")
f.text(90, 232, "oxidation (dehydrogenation):", "tl")
f.text(90, 248, "2 NAD → 2 reduced NAD", "tl")
f.text(90, 264, "4 ADP + 4 Pi → 4 ATP", "tl")
box(f, 10, 294, 150, 30, ["2 × pyruvate (3C)"])
done(f, (340, 336),
     "Glycolysis. Glucose with six carbons is phosphorylated using 2 ATP to give fructose 1,6-bisphosphate with six carbons. It splits into two triose phosphate molecules with three carbons each. These are oxidised by removal of hydrogen, which reduces 2 NAD, and 4 ATP are made, giving two pyruvate molecules with three carbons each.",
     "Glycolysis in the cytoplasm. Two ATP are used and four are made, so the net gain is 2 ATP, with 2 reduced NAD and 2 pyruvate.")

# ---------- 3. Krebs cycle ----------
f = Fig("krebs")
f.text(10, 20, "acetyl CoA (2C)", "tl")
f.line([(124, 26), (150, 42)], ARR, "ah")
box(f, 118, 46, 104, 40, ["citrate", "(6C)"])
box(f, 232, 150, 98, 40, ["5C", "compound"])
box(f, 118, 258, 104, 40, ["4C", "compound"])
box(f, 10, 150, 98, 40, ["oxaloacetate", "(4C)"])
f.line([(214, 90), (262, 146)], ARR, "ah")
f.text(264, 108, "CO₂ out,", "tl")
f.text(264, 122, "reduced NAD", "tl")
f.line([(268, 194), (210, 254)], ARR, "ah")
f.text(260, 222, "CO₂ out,", "tl")
f.text(260, 236, "reduced NAD,", "tl")
f.text(260, 250, "ATP made", "tl")
f.line([(130, 254), (78, 194)], ARR, "ah")
f.text(10, 230, "reduced FAD,", "tl")
f.text(10, 244, "reduced NAD", "tl")
f.line([(68, 146), (122, 90)], ARR, "ah")
f.text(170, 174, "Krebs", "tl tb", "middle")
f.text(170, 190, "cycle", "tl tb", "middle")
done(f, (350, 312),
     "The Krebs cycle with carbon numbers. Acetyl coenzyme A with two carbons joins oxaloacetate with four carbons to form citrate with six carbons. Citrate loses carbon dioxide twice, via a five-carbon compound, giving a four-carbon compound, with reduced NAD formed at each loss and ATP made. Further small steps form reduced FAD and reduced NAD and regenerate oxaloacetate.",
     "The Krebs cycle simplified to carbon numbers. Two carbons enter as acetyl CoA and two leave as carbon dioxide, so oxaloacetate is regenerated and the cycle can turn again. Coenzyme A is released and used again.")

# ---------- 4. chemiosmosis ----------
f = Fig("chemi")
f.text(10, 22, "intermembrane space", "tl tb")
f.text(10, 38, "(high H⁺ concentration)", "tl")
f.rect(20, 170, 360, 30, "f2 s-acc2 sw2")
for cx in (80, 150, 220):
    ellipse(f, cx, 185, 24, 28, "fm s-acc sw2")
    f.line([(cx, 214), (cx, 128)], "c3 sw2", "ah", check=False)
    f.text(cx, 118, "H⁺", "tl", "middle")
f.line([(106, 185), (124, 185)], "c4 sw2 dash", "ah")
f.line([(176, 185), (194, 185)], "c4 sw2 dash", "ah")
f.text(115, 152, "e⁻", "tl", "middle")
f.text(185, 152, "e⁻", "tl", "middle")
f.rect(284, 160, 32, 52, "fm s-acc sw2")
f.circle(300, 238, 22, "f1 s-acc sw2")
f.line([(300, 100), (300, 180)], "c3 sw2", "ah", check=False)
f.text(312, 98, "H⁺ flow back", "tl")
f.text(312, 112, "down the", "tl")
f.text(312, 126, "gradient", "tl")
f.text(324, 144, "ATP", "tl")
f.text(324, 158, "synthase", "tl")
f.leader((322, 150), (317, 166))
f.text(300, 284, "ADP + Pi → ATP", "tl", "middle")
f.leader((300, 270), (300, 262))
f.text(10, 264, "reduced NAD", "tl")
f.text(10, 280, "loses hydrogen", "tl")
f.line([(46, 250), (64, 218)], "c1 sw2", "ah")
f.line([(100, 214), (100, 248)], "c1 sw2", "ah")
f.text(108, 262, "NAD", "tl")
f.line([(220, 214), (220, 248)], "c1 sw2", "ah")
f.text(160, 266, "½O₂ + 2H⁺ + 2e⁻", "tl")
f.text(160, 282, "→ H₂O", "tl")
f.text(150, 330, "electron transport chain", "tl", "middle")
f.leader((140, 318), (140, 210))
f.text(10, 358, "matrix", "tl tb")
f.text(10, 374, "(low H⁺ concentration)", "tl")
f.text(390, 330, "inner mitochondrial", "tl", "end")
f.text(390, 346, "membrane", "tl", "end")
f.leader((376, 316), (376, 201))
done(f, (400, 388),
     "Oxidative phosphorylation on the inner mitochondrial membrane. Reduced NAD gives up hydrogen to the electron transport chain and becomes NAD. Energetic electrons pass along three carriers, releasing energy that pumps protons from the matrix into the intermembrane space. Protons flow back down their gradient into the matrix through ATP synthase, which makes ATP from ADP and phosphate. At the end of the chain, oxygen accepts the electrons and protons to form water.",
     "Chemiosmosis in a mitochondrion. Energy released as electrons pass along the chain pumps protons into the intermembrane space; the protons return through ATP synthase, and the energy released makes ATP. Oxygen is the final electron acceptor.")

# ---------- 5. mitochondrion ----------
f = Fig("mito")
cx, cy = 190, 105
ellipse(f, cx, cy, 80, 50, "f2 s-acc2 sw2")
ellipse(f, cx, cy, 72, 42, "fp ln")


def yb(x):
    return 42 * math.sqrt(1 - ((x - cx) / 72) ** 2)


for dx in (-55, -40, -25, -10):
    x = cx + dx
    f.line([(x, round(cy - yb(x), 1)), (x, round(cy - yb(x) + 20, 1))], "ln", check=False)
    x2 = x + 8
    f.line([(x2, round(cy + yb(x2), 1)), (x2, round(cy + yb(x2) - 20, 1))], "ln", check=False)
ellipse(f, cx + 40, cy - 18, 11, 7, "ln", check=False)
for (dx, dy) in ((32, 14), (46, 22), (52, 6), (26, 28)):
    f.circle(cx + dx, cy + dy, 2.5, "fi")


def on(a, b, deg):
    t = math.radians(deg)
    return (round(cx + a * math.cos(t), 1), round(cy + b * math.sin(t), 1))


f.text(100, 30, "outer membrane", "tl", "end")
f.leader((106, 26), on(80, 50, 225))
f.text(100, 96, "inner membrane", "tl", "end")
f.leader((106, 93), on(72, 42, 185))
f.text(100, 160, "intermembrane", "tl", "end")
f.text(100, 174, "space", "tl", "end")
f.leader((106, 156), on(76, 46, 140))
f.text(282, 30, "cristae", "tl")
f.leader((278, 26), (181, round(cy - yb(180) + 6, 1)))
f.text(282, 68, "circular DNA", "tl")
f.leader((278, 64), (242, 82))
f.text(282, 106, "matrix", "tl")
f.leader((278, 102), (206, 112))
f.text(282, 150, "70S ribosomes", "tl")
f.leader((278, 146), (244, 112))
done(f, (380, 200),
     "Drawing of a mitochondrion cut lengthways. A smooth outer membrane surrounds a gap, the intermembrane space, and then an inner membrane that is folded inwards into cristae. The matrix inside contains a loop of circular DNA and small 70S ribosomes.",
     "A mitochondrion in section, drawn from electron micrographs. The cristae give the inner membrane a large surface area; the matrix holds the enzymes of the link reaction and the Krebs cycle.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
