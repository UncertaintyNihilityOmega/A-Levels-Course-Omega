# checks/bio.mock.p5.py: recomputes every number in chapters/bio.mock.p5.md (Mock Paper 5) and the paper total
import importlib.util, math, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
sys.path.insert(0, os.path.join(root, "data"))
from crit import t_crit
text = open(os.path.join(root, "chapters", "bio.mock.p5.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def r(x, d=2): return round(x + 1e-12, d)


spec = importlib.util.spec_from_file_location("figp5", os.path.join(root, "data", "fig_bio.mock.p5.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# --- paper structure: FACTS.md says 9700/52 (June 2024) had 2 questions, 19 + 11 = 30 marks, 1 h 15 min
assert re.search(r"^@time 1 h 15 min$", text, flags=re.M)
blocks = re.findall(r"^:::try\n(.*?)\n:::\n(?=\n:::)", text, flags=re.M | re.S)
eq("questions", len(blocks), 2)
SKILL = {  # P = planning, A = analysis, conclusions and evaluation
    1: {"a": ("P", 3), "b": ("P", 3), "c": ("P", 1), "d": ("P", 2), "e": ("P", 4), "f": ("P", 2), "g": ("A", 2), "h": ("A", 1)},
    2: {"a": ("A", 2), "b": ("A", 2), "c": ("A", 1), "d": ("A", 3), "e": ("A", 2), "f": ("A", 2)},
}
tot, sk = 0, {"P": 0, "A": 0}
for i, b in enumerate(blocks, 1):
    head = int(re.match(r"Q: \[(\d+) marks\]", b).group(1))
    q, a = b.split("\nA: ")
    got = {p: int(k) for p, k in re.findall(r"^\(([a-z])\) .*?\[(\d+)\]\s*$", q, flags=re.M)}
    assert got == {p: v[1] for p, v in SKILL[i].items()}, (i, got)
    eq(f"Q{i} parts add up", sum(got.values()), head)
    eq(f"Q{i} mark scheme tokens", len(re.findall(r"\[(?:B|M|A)1\]", a)), head)
    for s, k in SKILL[i].values():
        sk[s] += k
    tot += head
eq("paper total", tot, 30)
assert 17 <= 18 <= 19 and 11 <= 12 <= 13
assert 14 <= sk["P"] <= 16 and 14 <= sk["A"] <= 16, sk
eq("planning", sk["P"], 15); eq("analysis", sk["A"], 15)
assert "Marks by skill in Question 1: planning 15" in text and "analysis, conclusions and evaluation 3" in text
assert "Marks by skill in Question 2: analysis, conclusions and evaluation 12" in text
# command words not on the syllabus list (REVIEW notes)
assert not re.search(r"\b(Evaluate|Estimate)\b", text)

# --- Question 1
eq("mass of F", 4.0 * 200 / 100, 8.0)
eq("serial 0.25", 4.0 / 2 ** 4, 0.25); eq("serial 2.0", 4.0 / 2, 2.0)
eq("pilot decrease", r(0.88 - 0.31), 0.57)
eq("pilot percent", r((0.88 - 0.31) / 0.88 * 100, 2), 64.77, 0.005)
eq("pilot percent 2sf", float(f"{(0.88 - 0.31) / 0.88 * 100:.2g}"), 65)
assert 0.57 > 0.04 + 0.06

# --- Question 2
MEAN, SD, N = m.MEANS, m.SDS, m.N
eq("n per group", N, 12); eq("seedlings", 3 * N, 36)
for sd, se in zip(SD, [1.7, 1.8, 1.9]):
    eq("SE", r(sd / math.sqrt(N), 1), se)
assert "| control (water) | 41.2 | 5.8 | 1.7 |" in text and "| 1.0% extract | 43.0 | 6.4 | 1.8 |" in text
assert "| 2.0% extract | 47.9 | 6.5 | 1.9 |" in text
eq("percentage increase", r((47.9 - 41.2) / 41.2 * 100, 2), 16.26, 0.005)
eq("percentage 3sf", float(f"{(47.9 - 41.2) / 41.2 * 100:.3g}"), 16.3)
eq("difference", r(47.9 - 41.2, 1), 6.7)
eq("s1^2/n1", r(5.8 ** 2 / 12, 3), 2.803)
eq("s2^2/n2", r(6.5 ** 2 / 12, 3), 3.521)
eq("sum", r(5.8 ** 2 / 12 + 6.5 ** 2 / 12, 3), 6.324)
eq("sqrt", r(math.sqrt(5.8 ** 2 / 12 + 6.5 ** 2 / 12), 3), 2.515, 0.0006)
t = 6.7 / math.sqrt(5.8 ** 2 / 12 + 6.5 ** 2 / 12)
eq("t", r(t, 2), 2.66)
eq("df", 12 + 12 - 2, 22)
# critical values printed in the question (df 18 to 26), from data/crit.py
for df, v in zip(range(18, 27), [2.10, 2.09, 2.09, 2.08, 2.07, 2.07, 2.06, 2.06, 2.06]):
    eq(f"crit {df}", r(t_crit(df), 2), v)
    assert f"| {df} | {v:.2f} |" in text
assert t > t_crit(22)
# error bars (SE): control and 1.0% overlap, control and 2.0% do not
lo = [mn - se for mn, se in zip(MEAN, m.SES)]
hi = [mn + se for mn, se in zip(MEAN, m.SES)]
assert lo[1] < hi[0] and lo[2] > hi[0]
eq("control bar low", r(lo[0], 1), 39.5); eq("control bar high", r(hi[0], 1), 42.9)
eq("1.0% bar low", r(lo[1], 1), 41.2, 0.06); eq("1.0% bar high", r(hi[1], 1), 44.8, 0.06)
print("ok")
