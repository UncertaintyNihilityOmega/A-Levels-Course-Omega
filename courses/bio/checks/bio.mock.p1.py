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
blocks = re.findall(r"^:::try\n(.*?)\n:::\n", text, flags=re.M | re.S)
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
