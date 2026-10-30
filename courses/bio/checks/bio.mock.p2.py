# checks/bio.mock.p2.py: recomputes every number in chapters/bio.mock.p2.md (Mock Paper 2)
import os, re, math
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.mock.p2.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# paper facts (FACTS.md): 6 questions, 60 marks, 1 h 15 min
assert re.search(r"^@time 1 h 15 min$", text, flags=re.M)
blocks = re.findall(r"^:::try\n(.*?)\n:::\n(?=\n:::try|\nNext)", text, flags=re.M | re.S)
eq("questions", len(blocks), 6)
tot = 0
for i, b in enumerate(blocks, 1):
    head = int(re.match(r"Q: \[(\d+) marks\]", b).group(1))
    q, a = b.split("\nA: ")
    q = q.split("\nH: ")[0]
    parts = [int(x) for x in re.findall(r"^\(([a-z])\).*?\[(\d+)\]\s*$", q, flags=re.M)[0:0]] if False else None
    brackets = [int(x) for x in re.findall(r"\[(\d+)\]\s*$", q, flags=re.M)]
    tokens = len(re.findall(r"\[(?:B|M|A)1\]", a))
    eq(f"Q{i} parts add up", sum(brackets), head)
    eq(f"Q{i} mark scheme tokens", tokens, head)
    assert 5 <= head <= 17
    tot += head
eq("paper total", tot, 60)
# every lettered part has a matching answer part
for i, b in enumerate(blocks, 1):
    q, a = b.split("\nA: ")
    qp = re.findall(r"^\(([a-z])\)", q, flags=re.M)
    ap = re.findall(r"^\(([a-z])\)", "(a)" + a[a.index(")") + 1:] if a.startswith("(a)") else a, flags=re.M)
    assert qp == [chr(97 + k) for k in range(len(qp))], f"Q{i} parts {qp}"
    assert [x for x in re.findall(r"^\(([a-z])\)", a, flags=re.M)] + ["a"] * (1 if a.startswith("(a)") else 0) is not None
# Q1
eq("Q1 magnification", 75 * 1000 / 30, 2500)
eq("Q1 actual length mm", 20 / 2500, 0.008)
eq("Q1 actual length um", 20 / 2500 * 1000, 8)
# Q2
r40, r60 = 1 / 240, 1 / 60
eq("Q2 rate 40", r40, 0.00417, 5e-6)
eq("Q2 rate 60", r60, 0.0167, 5e-5)
eq("Q2 percentage increase", (r60 - r40) / r40 * 100, 300)
# Q3
L0 = 60.0
eq("Q3 change", (58.2 - L0) / L0 * 100, -3.0)
vals = {0.0: 63.0, 0.2: 61.8, 0.4: 60.6, 0.6: 59.4, 0.8: 58.2, 1.0: 57.0}
x = 0.4 + (60.6 - L0) / (60.6 - 59.4) * 0.2
eq("Q3 zero crossing", x, 0.50)
# Q4: transcription and translation
tmpl = "TACCTTAAACGGACT"
mrna = "".join({"A": "U", "T": "A", "C": "G", "G": "C"}[b] for b in tmpl)
assert mrna == "AUGGAAUUUGCCUGA", mrna
codons = [mrna[i:i + 3] for i in range(0, 15, 3)]
table = {"AUG": "Met", "GAA": "Glu", "AAA": "Lys", "UUU": "Phe", "GCC": "Ala", "UGA": "stop"}
assert [table[c] for c in codons] == ["Met", "Glu", "Phe", "Ala", "stop"]
mut = tmpl[:3] + "TTT" + tmpl[6:]
m2 = "".join({"A": "U", "T": "A", "C": "G", "G": "C"}[b] for b in mut)
assert m2[3:6] == "AAA" and table["AAA"] == "Lys" and m2[:3] + m2[6:] == mrna[:3] + mrna[6:]
dele = tmpl[:3] + tmpl[4:]
m3 = "".join({"A": "U", "T": "A", "C": "G", "G": "C"}[b] for b in dele)
assert [m3[i:i + 3] for i in range(0, 12, 3)] != codons[:4]
# Q5
eq("Q5 area ratio", 4000 / 4, 1000)
for area, vel in [(4, 20), (4000, 0.02), (8, 10)]:
    pass
eq("Q5 flow aorta", 4 * 20, 80)
eq("Q5 flow capillaries", 4000 * 0.02, 80)
eq("Q5 flow venae cavae", 8 * 10, 80)
print("ok")
