# data/fig_bio.antibiotics.py: builds the hand-drawn SVG figures of chapters/bio.antibiotics.md and checks label clearance.
# Run: py data/fig_bio.antibiotics.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.antibiotics replaces the @@FIG_<NAME> placeholder lines of the chapter (and refreshes them later).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["PENICILLIN", "RESIST", "DISC"]
figs, problems = [], []
ENZ = "f1 s-acc sw2"
PEN = "f2 s-acc2 sw2"
CELL = "fm s-acc sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


# ---------- 1. how penicillin works (four stacked stages) ----------
f = Fig("penicillin")
ROW = 124
titles = ["1  Cross-links form in the growing wall", "2  Penicillin blocks the enzyme",
          "3  Weak wall: water enters by osmosis", "4  The cell bursts"]
for r in range(4):
    f.text(10, r * ROW + 16, titles[r], "tl tb")
# rows 1 and 2: two peptidoglycan chains with cross-links and the enzyme at the growing edge
for r, rungs in [(0, [34, 64, 94, 124]), (1, [34, 64])]:
    oy = r * ROW
    f.line([(20, oy + 46), (150, oy + 46)], "ln thick")
    f.line([(20, oy + 78), (150, oy + 78)], "ln thick")
    for x in rungs:
        f.line([(x, oy + 46), (x, oy + 78)], "ln-m thin", check=False)
    f.circle(190 if r else 172, oy + 62, 14, ENZ)
f.parts.append("")  # (no-op: keeps part order explicit)
# row 1: penicillin binds the enzyme
oy = 1 * ROW
f.poly([(154, oy + 52), (168, oy + 62), (154, oy + 72)], PEN)
# labels, row 0
def lab(x, y, s, target, ax=None):
    f.text(x, y, s)
    f.leader((x - 4, y - 3), target)
lab(214, 36, "peptidoglycan chains", (150, 46))
lab(214, 62, "cross-links", (124, 62))
lab(214, 102, "enzyme joining the", (181, 74))
f.text(214, 116, "chains with a link")
# labels, row 1
oy = ROW
lab(222, oy + 44, "penicillin", (169, oy + 58))
f.text(20, oy + 104, "no cross-links form here", "tl")
f.leader((70, oy + 91), (94, oy + 70))
# row 2: bacterium with water entering
oy = 2 * ROW
f.rect(20, oy + 34, 120, 62, CELL, 22)
for y in (oy + 48, oy + 64, oy + 80):
    f.line([(204, y), (152, y)], "c4 sw2", "ah")
f.text(212, oy + 60, "water enters")
f.text(212, oy + 74, "by osmosis")
f.text(20, oy + 114, "wall too weak to hold it", "tl")
# row 3: burst cell
oy = 3 * ROW
pieces = [[(24, oy + 40), (70, oy + 34), (84, oy + 56), (52, oy + 66), (30, oy + 60)],
          [(98, oy + 38), (136, oy + 44), (130, oy + 70), (104, oy + 62)],
          [(60, oy + 84), (96, oy + 80), (110, oy + 96), (70, oy + 100)]]
for p in pieces:
    f.poly(p, CELL)
for (x, y) in [(86, oy + 60), (92, oy + 72), (46, oy + 78), (118, oy + 88), (74, oy + 70)]:
    f.circle(x, y, 3.5, "fp ln")
f.text(160, oy + 56, "cell contents leak out")
f.text(160, oy + 72, "the cell dies")
done(f, (370, 4 * ROW - 6),
     "How penicillin kills a growing bacterium in four stages. 1: enzymes join chains of peptidoglycan with cross-links as the wall grows. "
     "2: penicillin binds to the enzyme and no new cross-links form. 3: the weak new wall cannot resist water entering by osmosis. "
     "4: the cell bursts and its contents leak out.",
     "Penicillin does not dissolve the wall. It stops the enzymes that make cross-links in new peptidoglycan, so a growing cell "
     "builds a weak wall, water enters by osmosis and the cell bursts.")

# ---------- 2. how resistance spreads (three stages) ----------
f = Fig("resist")
ROW = 108
titles = ["1  A mutation makes one cell resistant", "2  The antibiotic kills the others", "3  The survivor divides: all are resistant"]
for r in range(3):
    f.text(10, r * ROW + 16, titles[r], "tl tb")
NOR, RES, DEAD = "f2 s-acc2 sw2", "fa s-acc sw2", "fp ln dash"
grid = [(30 + k * 34, 46 + j * 30) for j in range(2) for k in range(5)]
mut = 7   # index of the resistant cell in stage 1
for i, (x, y) in enumerate(grid):
    f.circle(x, y, 10, RES if i == mut else NOR)
for i, (x, y) in enumerate(grid):
    f.circle(x, y + ROW, 10, RES if i == mut else DEAD)
for i, (x, y) in enumerate(grid):
    f.circle(x, y + 2 * ROW, 10, RES)
def lab2(x, y, s, target):
    f.text(x, y, s)
    f.leader((x - 4, y - 3), target)
lab2(214, 40, "bacteria that are", grid[4])
f.text(214, 54, "not resistant")
lab2(214, 92, "one resistant cell", (grid[mut][0] + 10, grid[mut][1] + 1))
f.text(214, 106, "(by random mutation)")
lab2(214, ROW + 40, "killed by the", (grid[4][0] + 10, grid[4][1] + ROW))
f.text(214, ROW + 54, "antibiotic")
lab2(214, ROW + 92, "survives and divides", (grid[mut][0] + 10, grid[mut][1] + ROW + 1))
lab2(214, 2 * ROW + 60, "every offspring has", (grid[9][0] + 10, grid[9][1] + 2 * ROW - 6))
f.text(214, 2 * ROW + 74, "the resistance allele")
done(f, (370, 3 * ROW - 8),
     "How antibiotic resistance spreads in three stages. 1: among many bacteria that are not resistant, one cell has a mutation that makes it "
     "resistant. 2: the antibiotic kills the non-resistant cells and the resistant cell survives. 3: the survivor divides, and all of its "
     "offspring are resistant.",
     "Resistance starts as a random mutation before the antibiotic is used. The antibiotic is the selection pressure: it kills the "
     "other bacteria, so the resistant ones survive and reproduce and the resistance allele becomes common.")

# ---------- 3. a disc diffusion plate ----------
f = Fig("disc")
cx, cy, R = 120, 124, 110
S = 2 * R / 90.0                       # px per mm for a 90 mm plate
f.circle(cx, cy, R, CELL)
zones = {"A": (225, 22.0), "B": (315, 12.0), "C": (45, 6.0), "D": (135, 18.0)}   # angle, zone diameter / mm
pos = {}
for k, (ang, d) in zones.items():
    ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    dx, dy = cx + 58 * ux, cy + 58 * uy
    pos[k] = (dx, dy, d * S / 2)
    if d > 6:
        f.circle(dx, dy, d * S / 2, "fp ln")
    f.circle(dx, dy, 3 * S, ENZ)
    rz = max(d * S / 2, 3 * S)
    f.text(dx + ux * (rz + 14), dy + uy * (rz + 14) + 4, k, "tl tb", "middle")
RXX = 252
def lab3(y, s, target, s2=None):
    f.text(RXX, y, s)
    if s2:
        f.text(RXX, y + 14, s2)
    f.leader((RXX - 4, y - 3), target)
bx, by, bz = pos["B"]
lab3(30, "paper disc with", (bx + 6, by - 4), "antibiotic")
lab3(86, "zone of inhibition", (bx + bz, by + 2))
f.text(RXX, 100, "(no bacteria grow)")
dx_, dy_, dz_ = pos["C"]
lab3(166, "bacteria grow up to", (dx_ + 8, dy_ + 2), "the edge of disc C")
lab3(212, "lawn of bacteria", (cx + 82, cy + 58), "on agar")
done(f, (380, 252),
     "An agar plate seen from above, with a lawn of bacteria and four paper discs, A to D, each holding a different antibiotic. "
     "Around discs A, B and D there is a clear circle, the zone of inhibition, where no bacteria grew; A has the largest zone and "
     "D the next largest. Around disc C there is no clear zone.",
     "Disc diffusion. The antibiotic spreads out of each disc into the agar. Where it is strong enough to stop the bacteria growing, "
     "there is a clear zone. A larger zone usually means the bacteria are more sensitive to that antibiotic.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
