# data/fig_bio.synthesis.py: builds the hand-drawn SVG figures of chapters/bio.synthesis.md and checks label clearance.
# Run: py data/fig_bio.synthesis.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.synthesis replaces the @@FIG_<NAME> placeholder lines (and @@TABLE_CODE) of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["TRANS", "SPLICE", "TRNA", "RIBO"]
figs, problems = [], []


def rungs(f, xs, y0, y1):
    for x in xs:
        f.parts.append(f'<path class="ln-m thin" d="M{x} {y0}L{x} {y1}"/>')


# ---------- 1. transcription ----------
f = Fig("transcription")
XS, XE = 28, 324
ellipse(f, 186, 90, 56, 44, "f2 s-acc2 sw2", check=False)                 # RNA polymerase
f.line([(XS, 92), (XE, 92)], "c1 sw3")                                    # template strand
f.line([(XS, 60), (92, 60), (108, 34), (246, 34), (262, 60), (XE, 60)], "c3 sw3")  # non-transcribed strand
rungs(f, range(34, 92, 12), 63, 89)
rungs(f, range(268, 326, 12), 63, 89)
f.line([(144, 116), (226, 116)], "c2 sw3")                                # mRNA paired to template
rungs(f, range(152, 226, 12), 96, 112)
f.line([(144, 116), (122, 150), (XS, 150)], "c2 sw3")                     # mRNA leaving
f.parts.append('<text class="tl tb" x="186" y="66" text-anchor="middle">RNA</text>')
f.parts.append('<text class="tl tb" x="186" y="81" text-anchor="middle">polymerase</text>')
for (cx, cy) in [(272, 130), (294, 118)]:
    f.circle(cx, cy, 6, "f1 s-acc sw2")
f.text(8, 96, "3′", anchor="start")
f.text(XE + 6, 96, "5′")
f.text(8, 154, "5′", anchor="start")
f.text(248, 121, "3′")
f.text(10, 18, "non-transcribed strand")
f.leader((40, 22), (40, 57))
f.text(8, 126, "template strand")
f.leader((50, 112), (50, 96))
f.text(36, 170, "mRNA")
f.text(236, 166, "free RNA")
f.text(236, 180, "nucleotides")
f.leader((262, 152), (270, 137))
f.line([(110, 214), (290, 214)], "ln", arrow="ah", check=False)
f.text(110, 236, "direction of transcription")
figs.append(f.svg((352, 248),
    "Transcription. RNA polymerase moves along the template strand of DNA, which is paired along the way with a growing strand of mRNA. The non-transcribed strand lies apart. "
    "The two DNA strands separate in front of the enzyme and rejoin behind it. The mRNA grows from its 5′ end and peels away from the template.",
    "Transcription (simplified). RNA polymerase separates the two DNA strands over a short stretch, builds mRNA by pairing free RNA nucleotides with the template strand, "
    "and moves on. The mRNA is made 5′ to 3′ and leaves the template. Only the template strand is copied."))
problems.extend(f.check())

# ---------- 2. splicing ----------
f = Fig("splicing")
f.text(16, 20, "primary transcript (copy of the gene)", cls="tl tb")
ex = [(22, 72), (104, 144), (176, 236), (268, 298)]
f.line([(22, 60), (312, 60)], "ln thick")
for k, (a, b) in enumerate(ex):
    f.rect(a, 48, b - a, 24, "f2 s-acc2 sw2")
    f.parts.append(f'<text class="tl tb" x="{(a + b) / 2:g}" y="65" text-anchor="middle">{k + 1}</text>')
f.text(4, 86, "5′")
f.text(324, 64, "3′")
f.text(40, 112, "exon (kept)")
f.leader((50, 98), (50, 74))
f.text(140, 112, "intron (removed)")
f.leader((160, 98), (160, 62))
f.line([(165, 130), (165, 190)], "ln", arrow="ah", check=False)
f.text(176, 150, "splicing: introns")
f.text(176, 164, "removed, exons joined")
f.text(16, 214, "mRNA", cls="tl tb")
cur = 22
for k, (a, b) in enumerate(ex):
    w = b - a
    f.rect(cur, 224, w, 24, "f2 s-acc2 sw2")
    f.parts.append(f'<text class="tl tb" x="{cur + w / 2:g}" y="241" text-anchor="middle">{k + 1}</text>')
    cur += w
figs.append(f.svg((346, 262),
    "Splicing. The primary transcript has four exons, numbered 1 to 4, separated by three introns drawn as thin lines. The introns are removed and the four exons are joined end to end to make the shorter mRNA.",
    "Splicing in the nucleus (simplified). The primary transcript is a copy of the whole gene. The introns (non-coding) are cut out and the exons (coding) are joined to make the mRNA, which is shorter than the gene."))
problems.extend(f.check())

# ---------- 3. tRNA ----------
f = Fig("trna")
f.rect(140, 40, 20, 130, "fm s-acc sw2")
for (cx, cy, r) in [(116, 112, 27), (184, 112, 27), (150, 188, 32)]:
    f.circle(cx, cy, r, "fm s-acc sw2")
f.parts.append('<rect class="fm" x="141" y="41" width="18" height="122"/>')
f.circle(150, 24, 15, "f1 s-acc sw2")
f.parts.append('<text class="tl tb" x="150" y="29" text-anchor="middle">Met</text>')
for x, ch in zip((128, 150, 172), "UAC"):
    f.parts.append(f'<text class="tl tb" x="{x}" y="193" text-anchor="middle">{ch}</text>')
    f.parts.append(f'<path class="ln-m thin dash" d="M{x} 224L{x} 244"/>')
for x, ch in zip((128, 150, 172), "AUG"):
    f.parts.append(f'<text class="tl tb" x="{x}" y="262" text-anchor="middle">{ch}</text>')
f.line([(100, 270), (200, 270)], "c2 sw3", check=False)
f.text(186, 28, "amino acid (here Met)")
f.leader((182, 26), (166, 26))
f.text(10, 116, "tRNA", cls="tl tb")
f.text(224, 194, "anticodon")
f.leader((220, 190), (186, 190))
f.text(224, 238, "hydrogen bonds")
f.leader((220, 234), (178, 234))
f.text(224, 266, "codon on mRNA")
f.leader((220, 262), (206, 262))
figs.append(f.svg((350, 284),
    "A tRNA molecule, drawn as a clover-leaf with a stem. The amino acid methionine is attached at the top of the stem. At the bottom, the anticodon U A C pairs by hydrogen bonds with the codon A U G on an mRNA strand.",
    "A transfer RNA molecule (simplified). One end carries a specific amino acid. The anticodon at the other end is three bases that are complementary to a codon on mRNA, and it pairs with that codon by hydrogen bonds."))
problems.extend(f.check())

# ---------- 4. translation at the ribosome (fig small: labels stay readable on phones) ----------
f = Fig("translation")
f.line([(22, 210), (330, 210)], "c2 sw3", check=False)
for x, cod in [(54, "CCA"), (122, "GAA"), (190, "UUU")]:
    f.rect(x, 198, 64, 24, "fp ln")
    for dx, ch in zip((-14, 0, 14), cod):
        f.parts.append(f'<text class="tl tb" x="{x + 32 + dx}" y="215" text-anchor="middle">{ch}</text>')
f.rect(40, 44, 160, 120, "fm s-acc sw2", rx=26)                            # large subunit
f.rect(52, 236, 140, 24, "fm2 s-acc sw2", rx=12)                           # small subunit
for cx, anti, aa_ in [(86, "GGU", "Pro"), (154, "CUU", "Glu")]:
    f.rect(cx - 24, 98, 48, 54, "f2 s-acc2 sw2", rx=8)
    for dx, ch in zip((-14, 0, 14), anti):
        f.parts.append(f'<text class="tl tb" x="{cx + dx}" y="144" text-anchor="middle">{ch}</text>')
        f.parts.append(f'<path class="ln-m thin dash" d="M{cx + dx} 172L{cx + dx} 194"/>')
    f.circle(cx, 80, 13, "f1 s-acc sw2")
    f.parts.append(f'<text class="tl tb" x="{cx}" y="85" text-anchor="middle">{aa_}</text>')
f.circle(66, 58, 13, "f1 s-acc sw2")
f.parts.append('<text class="tl tb" x="66" y="63" text-anchor="middle">Met</text>')
f.line([(72, 69), (78, 68)], "ln thick", check=False)
f.line([(100, 80), (140, 80)], "ln dash", check=False)
f.text(4, 214, "5′", anchor="start")
f.text(334, 214, "3′", anchor="start")
f.text(4, 16, "growing")
f.text(4, 30, "polypeptide")
f.leader((62, 33), (60, 47))
f.text(150, 16, "new peptide bond")
f.leader((196, 22), (120, 76))
f.text(212, 70, "large subunit")
f.leader((208, 66), (198, 70))
f.text(212, 100, "amino acid")
f.leader((208, 96), (169, 82))
f.text(212, 130, "tRNA")
f.leader((208, 126), (178, 126))
f.text(212, 158, "anticodon")
f.leader((208, 154), (172, 146))
f.text(260, 186, "codon")
f.leader((256, 188), (238, 200))
f.text(212, 252, "small subunit")
f.leader((208, 248), (194, 248))
f.line([(54, 288), (190, 288)], "ln", arrow="ah", check=False)
f.text(16, 308, "ribosome moves 5′ → 3′")
figs.append(f.svg((350, 320),
    "Translation at a ribosome. The mRNA runs between the large and small subunits. Two tRNA molecules, with anticodons GGU and CUU, are paired by hydrogen bonds with the codons CCA and GAA. "
    "The first tRNA carries the growing polypeptide, Met then Pro, and the second tRNA carries glutamic acid. A new peptide bond forms between them. The ribosome moves one codon to the right.",
    "Translation (simplified). The ribosome holds two tRNA molecules at a time. Each anticodon pairs with a codon on the mRNA. A peptide bond joins the amino acid on the second tRNA to the growing chain, "
    "the first tRNA leaves, and the ribosome moves along by one codon."))
problems.extend(f.check())

assert len(figs) == len(NAMES)
for s in figs:
    print(s)
    print()
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
