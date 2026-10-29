# data/fig_bio.dihybrid.py: builds the hand-drawn SVG figure of chapters/bio.dihybrid.md (linked v unlinked genes).
# Run: py data/fig_bio.dihybrid.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.dihybrid replaces the @@FIG_<NAME> placeholder lines of the chapter (later runs refresh them).
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["LINK"]
figs, problems = [], []


def chrom(f, cx, y0, y1, bands, letters_side=None):
    f.rect(cx - 8, y0, 16, y1 - y0, "fm s-acc sw2", rx=8)
    f.parts.append(f'<circle class="fi" cx="{cx}" cy="{(y0 + y1) / 2:g}" r="3"/>')
    for y in bands:
        f.parts.append(f'<rect class="fa s-acc sw2" x="{cx - 8}" y="{y - 4}" width="16" height="8"/>')


f = Fig("link")
f.text(8, 16, "A  Genes on different chromosomes", "tl tb")
# pair 1 (long) and pair 2 (short), bottoms aligned
for cx, letter in ((34, "A"), (62, "a")):
    chrom(f, cx, 36, 128, [66])
    f.text(cx, 146, letter, "tl", "middle")
for cx, letter in ((106, "B"), (134, "b")):
    chrom(f, cx, 68, 128, [80])
    f.text(cx, 146, letter, "tl", "middle")
f.text(170, 62, "AaBb makes four")
f.text(170, 76, "kinds of gamete,")
f.text(170, 90, "in equal numbers:")
f.text(170, 104, "AB, Ab, aB, ab")
f.text(8, 188, "B  Genes on the same chromosome", "tl tb")
for cx, tops in ((48, ("A", "B")), (108, ("a", "b"))):
    chrom(f, cx, 208, 304, [234, 266])
    xl = cx - 16 if cx == 48 else cx + 16
    anchor = "end" if cx == 48 else "start"
    f.text(xl, 238, tops[0], "tl", anchor)
    f.text(xl, 270, tops[1], "tl", anchor)
f.text(78, 324, "AB / ab", "tl tb", "middle")
f.text(170, 252, "AaBb (AB/ab) makes")
f.text(170, 266, "mostly AB and ab,")
f.text(170, 280, "few Ab and aB")
f.text(170, 294, "(crossing over)")
f.vb = (330, 336)
figs.append(f.svg((330, 336),
    "Two arrangements of two genes in a heterozygote AaBb. Panel A: gene A is on one pair of chromosomes and gene B on another "
    "pair, so AaBb makes four kinds of gamete in equal numbers. Panel B: both genes are on the same pair of chromosomes, one "
    "chromosome carrying A and B and its homologue carrying a and b, so the heterozygote makes mostly AB and ab gametes and few "
    "Ab and aB gametes, made by crossing over.",
    "Unlinked and linked genes (drawings, each chromosome before replication). In panel B the slash in AB/ab separates the "
    "two homologous chromosomes, so alleles on the same chromosome are written together."))
problems.extend(f.check())
print("\n\n".join(figs))
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
