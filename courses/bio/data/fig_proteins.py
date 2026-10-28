# data/fig_proteins.py: hand-drawn SVG figures of chapters/bio.proteins.md with label-clearance checks.
# Run: PYTHONUTF8=1 py data/fig_proteins.py > scratch/proteins_figs.txt   (figures on stdout, report on stderr)
import math, sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p3 import ChemFig, trim, finish, LEAD

figs = []
problems = []


def inlet(f, x, y, s, cls="tl"):
    f.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="middle">{s}</text>')


# ---------------- Figure 1: general structure of an amino acid ----------------
f = ChemFig("aminoacid")
cx, cy = 165, 84
f.text(cx, cy + 4, "C", "tl tb", "middle")
f.sub(cx - 12, cy, "l", "H₂N", 12)
f.sub(cx + 12, cy, "r", "COOH", 12)
f.sub(cx, cy - 11, "u", "H", 10)
f.sub(cx, cy + 11, "d", "R", 10)
f.text(10, 30, "amine group", "tl")
f.line([(40, 36), (112, 72)], LEAD, check=False)
f.text(224, 30, "carboxyl group", "tl")
f.line([(262, 36), (228, 72)], LEAD, check=False)
f.text(10, 150, "central carbon atom", "tl")
f.line([(100, 140), (156, 92)], LEAD, check=False)
f.text(180, 150, "R group (side chain)", "tl")
f.line([(200, 141), (172, 120)], LEAD, check=False)
f.text(10, 190, "The 20 amino acids all have this structure", "tl")
f.text(10, 206, "and differ only in the R group.", "tl")
figs.append(f.svg((330, 218),
    "General structure of an amino acid: a central carbon atom bonded to a hydrogen atom above, an amine group H2N on the left, a "
    "carboxyl group COOH on the right and an R group below. The groups are labelled amine group, carboxyl group, central carbon atom "
    "and R group (side chain).",
    "Every amino acid has an amine group, a carboxyl group, a hydrogen atom and an R group on one central carbon. Only the R group differs "
    "between the 20 amino acids."))
problems.extend(f.check())

# ---------------- Figure 2: dipeptide formation ----------------
f = ChemFig("dipeptide")
f.text(10, 16, "Two amino acids", "tl tb")
for y, r in ((58, "R₁"), (138, "R₂")):
    f.text(30, y + 4, "H₂N", "tl", "middle")
    f.line([(45.5, y), (60, y)], "ln")
    f.text(72, y + 4, "CH", "tl", "middle")
    f.line([(84, y), (98, y)], "ln")
    f.text(122, y + 4, "COOH", "tl", "middle")
    f.sub(72, y + 12, "d", r, 8)
f.text(165, 102, "+", "tl tb", "middle")
f.line([(165, 180), (165, 214)], "ln", "ah")
f.text(177, 194, "condensation", "tl")
f.text(10, 242, "Dipeptide and water", "tl tb")
y = 296
f.text(30, y + 4, "H₂N", "tl", "middle")
f.line([(45.5, y), (60, y)], "ln")
f.text(72, y + 4, "CH", "tl", "middle")
f.line([(84, y), (98, y)], "ln")
f.text(106, y + 4, "C", "tl", "middle")
f.line([(104, y - 10), (104, y - 20)], "ln")
f.line([(108, y - 10), (108, y - 20)], "ln")
f.text(106, y - 28, "O", "tl", "middle")
f.line([(114.5, y), (128, y)], "ln")
f.text(140, y + 4, "NH", "tl", "middle")
f.line([(152, y), (166, y)], "ln")
f.text(178, y + 4, "CH", "tl", "middle")
f.line([(190, y), (204, y)], "ln")
f.text(222, y + 4, "COOH", "tl", "middle")
f.sub(72, y + 12, "d", "R₁", 8)
f.sub(178, y + 12, "d", "R₂", 8)
f.rect(94, y - 9, 61, 20, "ln-m thin dash", 4, check=False)
f.text(124, y + 60, "peptide bond", "tl", "middle")
f.line([(124, y + 49), (124, y + 15)], LEAD, check=False)
f.text(258, y + 4, "+ H₂O", "tl tb")
figs.append(f.svg((330, 372),
    "Formation of a dipeptide. Top: two amino acids, each drawn as H2N, CH with an R group below, and COOH. An arrow labelled "
    "condensation leads to the dipeptide below: the COOH of the first amino acid has joined to the NH of the second, forming a "
    "C double-bonded to O joined to NH, labelled peptide bond, plus a molecule of water.",
    "The COOH group of one amino acid and the H₂N group of the next join in a condensation reaction. The OH of the carboxyl group and an H of the "
    "amine group leave as water, and the new C–N covalent bond is the peptide bond. Breaking it needs water: hydrolysis."))
problems.extend(f.check())

# ---------------- Figure 3: four levels of structure ----------------
f = ChemFig("levels")
# 1 primary
f.text(10, 16, "1  Primary: the sequence", "tl tb")
bx = [24 + 30 * i for i in range(9)]
f.line([(x, 46) for x in bx], "ln", check=False)
for i, x in enumerate(bx):
    f.circle(x, 46, 8, "f1 s-acc sw2" if i % 3 else "f2 s-acc2 sw2", check=False)
f.text(10, 80, "amino acids joined by peptide bonds", "tl")
# 2 secondary
f.text(10, 112, "2  Secondary: helix or sheet", "tl tb")
helix = [(round(24 + 4.4 * t + 11 * math.cos(t), 1), round(158 + 15 * math.sin(t), 1)) for t in [k * 0.25 for k in range(0, 85)]]
f.line(helix, "c1 sw2", check=False)
f.text(24, 194, "α-helix", "tl")
sx0 = 178
for r in range(3):
    yb = 140 + 17 * r
    f.line(zig_pts := [(sx0 + 13 * k, yb - (7 if k % 2 else 0)) for k in range(11)], "c2 sw2", check=False)
for r in range(2):
    yb = 140 + 17 * r
    f.multi([[(sx0 + 13 * k, yb + 3), (sx0 + 13 * k, yb + 14)] for k in range(0, 11, 2)], "ln-m thin dash", check=False)
f.text(178, 194, "β-pleated sheet", "tl")
f.text(10, 220, "held by hydrogen bonds (dashed lines)", "tl")
# 3 tertiary: a chain folded back on itself, with bonds between neighbouring runs
f.text(10, 252, "3  Tertiary: folded 3D shape", "tl tb")
x0, x1, ys0, dy, R = 118, 210, 276, 20, 10
runs = []
chain = []
for k in range(5):
    y = ys0 + dy * k
    xs = [x0 + 6 + (x1 - x0 - 12) * i / 24 for i in range(25)]
    seg = [(round(x, 1), round(y + 2.5 * math.sin(i * 0.9 + k), 1)) for i, x in enumerate(xs)]
    if k % 2:
        seg = seg[::-1]
    runs.append(seg)
for k in range(5):
    chain += runs[k]
    if k < 4:
        # turn at the end where run k finishes (right end for even k, left end for odd k)
        xe = chain[-1][0]
        ya, yb = ys0 + dy * k, ys0 + dy * (k + 1)
        sign = 1 if k % 2 == 0 else -1
        for a in [m / 8 * math.pi for m in range(1, 8)]:
            chain.append((round(xe + sign * (dy / 2) * math.sin(a), 1), round((ya + yb) / 2 - (dy / 2) * math.cos(a), 1)))
f.line(chain, "c1 sw2", check=False)
f.line([(150, ys0 + 2.5), (150, ys0 + dy - 2)], "ln thick", check=False)
f.line([(190, ys0 + dy + 2), (190, ys0 + 2 * dy - 2)], "ln-m thin dash", check=False)
f.line([(190, ys0 + 3 * dy + 2), (190, ys0 + 4 * dy - 2)], "ln-m thin dot", check=False)
f.text(10, ys0 + 14, "disulfide bond", "tl")
f.line([(110, ys0 + 10), (146, ys0 + 10)], LEAD, check=False)
f.text(232, ys0 + 34, "hydrogen bond", "tl")
f.line([(228, ys0 + 30), (193, ys0 + 30)], LEAD, check=False)
f.text(232, ys0 + 74, "ionic bond", "tl")
f.line([(228, ys0 + 70), (193, ys0 + 70)], LEAD, check=False)
# 4 quaternary
f.text(10, 390, "4  Quaternary: several chains", "tl tb")
for k, x in enumerate((46, 106, 166, 226)):
    f.circle(x, 432, 22, "f1 s-acc sw2" if k < 2 else "f2 s-acc2 sw2", check=False)
    inlet(f, x, 437, "α" if k < 2 else "β")
f.text(10, 478, "four polypeptides, as in haemoglobin", "tl")
figs.append(f.svg((330, 492),
    "Four levels of protein structure. 1 Primary: a row of circles joined by lines, the amino acid sequence. 2 Secondary: an "
    "alpha helix, a coil, and a beta-pleated sheet, parallel zigzag strands, both held by hydrogen bonds. 3 Tertiary: a chain folded "
    "into a compact shape held by a disulfide bond, hydrogen bonds and ionic bonds. 4 Quaternary: four polypeptide chains, two alpha "
    "and two beta, together as one molecule.",
    "Primary structure is the order of amino acids. Secondary structure is the helix or sheet made by hydrogen bonds in the backbone. Tertiary "
    "structure is the folding of the whole chain, held by bonds between R groups. Quaternary structure is two or more polypeptides together."))
problems.extend(f.check())

# ---------------- Figure 4: haemoglobin ----------------
f = ChemFig("haemoglobin")
f.text(10, 16, "Haemoglobin: four polypeptides", "tl tb")
cen = [(92, 82, "α-globin"), (184, 82, "β-globin"), (92, 174, "β-globin"), (184, 174, "α-globin")]
for (x, y, s) in cen:
    cls = "f1 s-acc sw2" if s.startswith("α") else "f2 s-acc2 sw2"
    f.circle(x, y, 44, cls, check=False)
    inlet(f, x, y - 12, s)
    f.rect(x - 13, y + 2, 26, 22, "fp ln", 3, check=False)
    inlet(f, x, y + 18, "Fe")
f.text(236, 52, "haem group", "tl")
f.text(236, 68, "with one Fe²⁺", "tl")
f.line([(232, 60), (195, 90)], LEAD, check=False)
f.text(10, 250, "2 α-globin + 2 β-globin + 4 haem groups.", "tl")
f.text(10, 266, "Each Fe²⁺ binds one O₂, so one haemoglobin", "tl")
f.text(10, 282, "carries up to four O₂ molecules.", "tl")
figs.append(f.svg((330, 294),
    "Haemoglobin as four rounded polypeptide chains in a square: two alpha-globin and two beta-globin. Each chain holds a small "
    "square haem group containing an iron ion, Fe2+. A label points to one haem group with one Fe2+.",
    "Haemoglobin is a globular protein with quaternary structure: two α-globin and two β-globin polypeptides, each with a haem group that "
    "contains one Fe²⁺ ion, so one molecule can carry four O₂ molecules."))
problems.extend(f.check())

# ---------------- Figure 5: collagen ----------------
f = ChemFig("collagen")
f.text(10, 16, "A collagen molecule: a triple helix", "tl tb")
for k, cls in enumerate(("c1 sw2", "c2 sw2", "c3 sw2")):
    ph = k * 2 * math.pi / 3
    f.line([(round(18 + 8 * t, 1), round(66 + 15 * math.sin(t + ph), 1)) for t in [i * 0.3 for i in range(0, 41)]], cls, check=False)
f.text(196, 52, "three polypeptide", "tl")
f.text(196, 68, "chains wound", "tl")
f.text(196, 84, "together", "tl")
f.text(10, 112, "Glycine, the smallest amino acid, is every", "tl")
f.text(10, 128, "third one, so the chains pack tightly.", "tl")
f.text(10, 150, "Molecules in a fibril", "tl tb")
L, g, pitch = 88, 8, 96
rows = [178, 194, 210]
for r, y in enumerate(rows):
    off = (r * 32) % pitch
    xs = [off - pitch + k * pitch for k in range(5)]
    rects = []
    for x in xs:
        a, b = max(x + 8, 10), min(x + 8 + L, 320)
        if b - a > 10:
            rects.append([(a, y - 4), (b, y - 4), (b, y + 4), (a, y + 4)])
    f.multi(rects, "f1 s-acc sw2", closed=True, check=False)
links = []
for r in range(2):
    for k in range(4):
        x = 30 + 70 * k + 24 * r
        links.append([(x, rows[r] + 4), (x, rows[r + 1] - 4)])
f.multi(links, "ln thick", check=False)
f.text(10, 242, "Molecules lie side by side, staggered, with", "tl")
f.text(10, 258, "covalent cross-links (short thick lines).", "tl")
f.text(10, 288, "Fibrils make a fibre", "tl tb")
f.rect(16, 300, 190, 44, "f1 s-acc sw2", 4)
f.multi([[(22, 308 + 8 * k), (200, 308 + 8 * k)] for k in range(5)], "ln thick", check=False)
f.text(218, 324, "collagen fibre", "tl")
figs.append(f.svg((330, 358),
    "Collagen. Top: three polypeptide chains, drawn as three intertwined wavy lines, wound together into a triple helix. Middle: rows of "
    "collagen molecules lie end to end and side by side, with the ends staggered between rows and short thick lines marking "
    "covalent cross-links between neighbouring molecules. Bottom: many fibrils bundled into a collagen fibre.",
    "Three polypeptides form a collagen molecule (triple helix). Molecules lie side by side, staggered, joined by covalent cross-links, "
    "to form fibrils, and fibrils form fibres."))
problems.extend(f.check())
finish(figs, problems)
