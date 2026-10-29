# checks/bio.exam.p24.py: recomputes every number in chapters/bio.exam.p24.md (Papers 2 and 4 guide)
import os, re, math
from fractions import Fraction as Fr
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.exam.p24.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# real June 2024 question counts and marks (FACTS.md)
p2 = [14, 12, 6, 17, 5, 6]
p4 = [8, 9, 11, 11, 10, 11, 9, 15, 8, 8]
eq("paper 2 total", sum(p2), 60)
eq("paper 2 questions", len(p2), 6)
eq("paper 4 total", sum(p4), 100)
eq("paper 4 questions", len(p4), 10)
# pacing
eq("min per mark P2", 75 / 60, 1.25)
eq("min per mark P4", 120 / 100, 1.2)
eq("seconds per mark P2", 1.25 * 60, 75)
eq("seconds per mark P4", 1.2 * 60, 72)
for m, a, b in [(1, 1.25, 1.2), (2, 2.5, 2.4), (3, 3.75, 3.6), (4, 5, 4.8), (6, 7.5, 7.2), (8, 10, 9.6)]:
    eq(f"{m} marks P2", m * 1.25, a)
    eq(f"{m} marks P4", m * 1.2, b)
eq("P2 early finish", 70 * 60 / 60, 70)
eq("P4 early finish", 115 * 60 / 100, 69)
eq("weights AS", 46 + 31 + 23, 100)
# command words: seventeen rows
cw = re.findall(r"^\| \*\*(\w+)\*\* \|", text, re.M)
eq("command words", len(cw), 17)
assert sorted(cw) == sorted("define state give identify describe outline compare contrast explain suggest predict determine discuss assess comment calculate sketch".split())
# graph: rate = 0.0004375 x^2 (60 - x)
r = lambda x: 0.0004375 * x * x * (60 - x)
eq("rate at 20", r(20), 7.0)
eq("rate at 40", r(40), 14.0)
eq("rate at 60", r(60), 0.0)
assert max(range(0, 61), key=r) == 40
# assess: vaccine trial
eq("vaccinated %", 2 / 1000 * 100, 0.2)
eq("unvaccinated %", 80 / 1000 * 100, 8)
eq("reduction", (80 - 2) / 80 * 100, 97.5)
# comment: fertiliser
eq("difference", 12.4 - 11.9, 0.5, 1e-9)
eq("difference %", round((12.4 - 11.9) / 11.9 * 100), 4)
# calculate: magnification
eq("30 mm in um", 30 * 1000, 30000)
eq("magnification", 30000 / 7.5, 4000)
# determine: mRNA from template 3'-TAC GGA-5'
comp = {"T": "A", "A": "U", "C": "G", "G": "C"}
assert "".join(comp[b] for b in "TACGGA") == "AUGCCU"
n += 1
# worked example: catalase rate
eq("rate", 24 / 80, 0.30)
eq("time", 60 / (24 / 80), 200)
eq("wrong rate ecf time", 60 / 0.03, 2000)
# Paper 2 style question: nitrate uptake
oxy = [0, 5, 10, 20, 30, 40]
up = [1.0, 5.0, 9.0, 13.0, 13.0, 13.0]
eq("rise", up[3] - up[0], 12.0)
eq("percentage increase 5 to 10", (9.0 - 5.0) / 5.0 * 100, 80)
assert up[3] == up[4] == up[5]
# Paper 4 style question: Hardy-Weinberg
q2 = Fr(4, 40000)
eq("q squared", float(q2), 1.0e-4)
q = math.sqrt(1.0e-4)
eq("q", q, 0.010)
p = 1 - q
eq("p", p, 0.99)
eq("2pq", 2 * p * q, 0.0198)
eq("carriers", round(2 * p * q * 40000), 792)
# marks: the 8- and 10-mark questions, command-word sets
for title, marks in [("Paper 2 style: uptake of nitrate by root cells", 8), ("Paper 4 style: an inherited enzyme deficiency", 10)]:
    blk = text.split(":::try " + title)[1].split("\n:::\n")[0]
    ans = blk.split("\nA: ")[1]
    tok = len(re.findall(r"\[[BMA]1\]", ans))
    eq(title + " marks", tok, marks)
    parts = [int(x) for x in re.findall(r"\[(\d+)\]\s*$", blk.split("\nH: ")[0], re.M)]
    eq(title + " parts add up", sum(parts), marks)
print("ok")
