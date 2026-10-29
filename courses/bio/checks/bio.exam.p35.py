# checks/bio.exam.p35.py: recomputes every number in chapters/bio.exam.p35.md (Papers 3 and 5 guide)
import os, re, math
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.exam.p35.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# paper facts (FACTS.md)
eq("paper 3 min per mark", 120 / 40, 3)
eq("paper 3 June 2024 total", 21 + 19, 40)
eq("paper 3 q1 minutes", 21 * 3, 63)
eq("paper 3 q2 minutes", 19 * 3, 57)
assert 15 + 11 + 11 <= 40 <= 17 + 13 + 13
eq("presentation + analysis min", 11 + 11, 22)
eq("presentation + analysis max", 13 + 13, 26)
eq("microscope total low", 10 * 10, 100)
eq("microscope total high", 10 * 40, 400)
eq("paper 5 min per mark", 75 / 30, 2.5)
eq("paper 5 June 2024 total", 19 + 11, 30)
eq("paper 5 q1 minutes", 19 * 2.5, 47.5)
eq("paper 5 q2 minutes", 11 * 2.5, 27.5)
assert 14 + 14 <= 30 <= 16 + 16
eq("AS weights", 31 + 46 + 23, 100)
# Paper 5 plan: six temperatures at 10 C intervals; eight marking points
temps = [20, 30, 40, 50, 60, 70]
eq("six temperatures", len(temps), 6)
assert all(b - a == 10 for a, b in zip(temps, temps[1:]))
plan = text.split(":::eg Plan an investigation of the effect of temperature")[1].split("\n:::\n")[0]
eq("plan marks", len(re.findall(r"\[B1\]", plan)), 8)
# Paper 3 example: volumes, rates, marks
conc = [2, 4, 6, 8, 10]
vol = [8, 12, 14, 16, 17]
rate = [v / 60 for v in vol]
want = [0.13, 0.20, 0.23, 0.27, 0.28]
for c, r, w in zip(conc, rate, want):
    eq(f"rate at {c}%", round(r, 2), w)
f = lambda x: 0.4 * x / (4 + x)
for c, r in zip(conc, rate):
    eq(f"curve near point {c}", f(c), r, 0.01)
eq("0.13 to 0.20 rise", round(rate[1], 2) - round(rate[0], 2), 0.07)
eq("0.27 to 0.28 rise", round(rate[4], 2) - round(rate[3], 2), 0.01)
assert all(b > a for a, b in zip(rate, rate[1:])) and (rate[1] - rate[0]) > (rate[4] - rate[3])
eg = text.split(":::eg A student added different concentrations")[1].split("\n:::\n")[0]
eq("paper 3 example marks", len(re.findall(r"\[[BMA]1\]", eg)), 11)
# quick checks: marks per question match tokens
blk = text.split(":::try Fix the slip")[1].split("\n:::\n")[0]
qs = re.findall(r"^Q: \[(\d+) marks?\]", blk, re.M)
ans = blk.split("\nQ: ")
tot = 0
for a in ans[1:]:
    m = int(re.match(r"\[(\d+) mark", a).group(1))
    eq("fix-the-slip tokens", len(re.findall(r"\[[BMA]1\]", a)), m)
    tot += m
eq("fix-the-slip total", tot, 10)
print("ok")
