# checks/bio.mock.p1.py: recomputes every number in chapters/bio.mock.p1.md (Mock Paper 1)
import os, re, math
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.mock.p1.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# paper facts (FACTS.md): 40 questions, 1 mark each, 40 marks, 1 h 15 min
blocks = re.findall(r"^:::try\n(.*?)\n:::\n(?=\n:::try|\nNext)", text, flags=re.M | re.S)
eq("questions", len(blocks), 40)
marks = [int(re.match(r"Q: \[(\d+) mark", b).group(1)) for b in blocks]
eq("total marks", sum(marks), 40)
assert all(m == 1 for m in marks)
header = re.search(r"^@time (.*)$", text, flags=re.M).group(1)
assert header == "1 h 15 min", header

# answer letters
letters = []
tables = 0
for i, b in enumerate(blocks, 1):
    q, a = b.split("\nA: ")
    m = re.match(r"\*\*([ABCD])\*\* \[B1\]", a)
    assert m, f"Q{i}: answer must start with the letter and [B1]"
    letters.append(m.group(1))
    # nested figures and plots must sit inside the question, and must not name the answer in the aria-label
    for lab in re.findall(r'aria-label="([^"]*)"', q) + re.findall(r'--alt "([^"]*)"', q):
        assert not re.search(r"prokaryot|bacterium|bacterial|metaphase|facilitated|sensitive|resistant", lab, flags=re.I), f"Q{i}: label names the answer"
    if "| **A** |" in q:
        tables += 1
        for L in "ABCD":
            assert f"| **{L}** |" in q, f"Q{i}: table row {L} missing"
        assert "✓" in q and "✗" in q
    else:
        for L in "ABCD":
            assert re.search(rf"^\*\*{L}\*\* ", q, flags=re.M), f"Q{i}: option {L} missing"
        assert not re.search(r"^\*\*E\*\* ", q, flags=re.M)
    assert re.search(r"\(#bio\.[\w.]+\)", q.split("\n")[0]), f"Q{i}: revise link missing"
cnt = Counter(letters)
print("letters", dict(sorted(cnt.items())), "tables", tables)
for L in "ABCD":
    eq("count " + L, cnt[L], 10)
assert tables >= 6
runs = max(len(list(g)) for _, g in __import__("itertools").groupby(letters))
assert runs <= 2, f"run of {runs} equal letters"

# figures and plots inside questions: Q4 cell drawing (SVG), Q16 uptake plot, Q21 mitosis (SVG), Q37 disc plate (SVG)
with_fig = [i for i, b in enumerate(blocks, 1) if ":::html" in b or ":::plot" in b]
assert with_fig == [4, 16, 21, 37], with_fig
assert sum(1 for i in with_fig if ":::html" in blocks[i - 1]) >= 3
# Q4: cell body 120 px long, scale bar 48 px = 1 um (data/fig_bio.mock.p1.py)
eq("Q4 cell length / um", 120 / 48, 2.5)
eq("Q4 wrong C (x10)", 120 / 48 * 10, 25)
eq("Q4 wrong D (/10)", 120 / 48 / 10, 0.25)
# Q11: activation energy 80 -> 50 kJ/mol; energy released 20 kJ/mol unchanged
eq("Q11 fall in Ea", 80 - 50, 30)
# Q14: percentages of each preparation's own maximum
free = {30: 80, 40: 100, 50: 70, 60: 10}
imm = {30: 70, 40: 100, 50: 95, 60: 60}
assert imm[50] > free[50] and imm[60] > free[60]
assert max(free, key=free.get) == max(imm, key=imm.get) == 40
assert imm[60] < 100 and imm[60] > 0
# Q16: P = 0.8x, Q = 12x/(2+x); no ATP; Q levels off
P = lambda x: 0.8 * x
Qf = lambda x: 12 * x / (2 + x)
eq("Q16 P(10)", P(10), 8)
eq("Q16 Q(2)", Qf(2), 6)
eq("Q16 Q(10)", Qf(10), 10)
assert (Qf(10) - Qf(8)) < 0.15 * (Qf(2) - Qf(0)) and math.isclose(P(10) - P(8), P(2) - P(0))
# Q21: 4 chromosomes x 2 chromatids = 8 DNA molecules at metaphase
eq("Q21 DNA molecules", 4 * 2, 8)
# Q37: zone diameters at 2 px per mm (W 60 px, X 36 px, Y 24 px, Z none)
zones = {"W": 60 / 2, "X": 36 / 2, "Y": 24 / 2, "Z": 0}
assert zones["W"] > zones["X"] > zones["Y"] > zones["Z"] == 0
# Q40: clone that binds X strongly and Y hardly at all
clones = {1: (0.85, 0.05), 2: (0.10, 0.90), 3: (0.80, 0.75), 4: (0.04, 0.06)}
specific = [c for c, (x, y) in clones.items() if x >= 0.5 and y <= 0.2]
assert specific == [1], specific
# Q2 drawing size
eq("Q2 drawing", 40 * 250 / 1000, 10)
# Q9 insulin peptide bonds
eq("Q9 bonds", (21 - 1) + (30 - 1), 49)
# Q17 cubes
sa0, v0 = 6 * 3 ** 2, 3 ** 3
sa1, v1 = 27 * 6 * 1 ** 2, 27 * 1 ** 3
eq("Q17 before", sa0 / v0, 2)
eq("Q17 after", sa1 / v1, 6)
eq("Q17 factor", (sa1 / v1) / (sa0 / v0), 3)
# Q22 DNA bases
g = 18
c = g
eq("Q22 thymine", (100 - g - c) / 2, 32)
# Q27 potometer
vol = math.pi * 0.40 ** 2 * 45
eq("Q27 volume", vol, 22.6, 0.05)
eq("Q27 rate", vol / 5.0, 4.5, 0.05)
eq("Q27 wrong B (diameter as radius)", math.pi * 0.80 ** 2 * 45 / 5, 18, 0.2)
eq("Q27 wrong C (no time)", vol, 23, 0.5)
eq("Q27 wrong D (no area)", 45 / 5.0, 9.0)
# Q34 diffusion distance
eq("Q34 rate", 1 / 2, 0.5)
# Q18 water potential order
tissue, P, Q, R = -400, -200, -400, -600
assert P > tissue and Q == tissue and R < tissue
print("ok")
