# checks/bio.exam.p1.py: recomputes every number in chapters/bio.exam.p1.md (Paper 1 guide)
import os, re, math
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.exam.p1.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# paper facts (FACTS.md): 40 questions, 75 min, 40 marks, weights
eq("seconds per question", 75 * 60 / 40, 112.5)
eq("first pass seconds per question", 55 * 60 / 40, 82.5)
eq("passes + check", 55 + 15 + 5, 75)
eq("ten questions in minutes", 10 * 112.5 / 60, 18.75)
eq("AS weights", 31 + 46 + 23, 100)
# eg 3: zero crossing of the potato change in mass
conc = [0.0, 0.2, 0.4, 0.6, 0.8]
chg = [14, 6, -4, -11, -16]
i = max(k for k in range(4) if chg[k] > 0 and chg[k + 1] < 0)
frac = chg[i] / (chg[i] - chg[i + 1])
eq("fraction of the way", frac, 0.6)
zero = conc[i] + frac * (conc[i + 1] - conc[i])
eq("zero crossing", zero, 0.32)
assert min([0.2, 0.3, 0.4, 0.6], key=lambda c: abs(c - zero)) == 0.3
# eg 4: magnification
eq("image in um", 45 * 1000, 45000)
eq("magnification", 45000 / 1.5, 30000)
eq("wrong: no conversion", 45 / 1.5, 30)
# practice 3: cuboid 2 x 4 x 5
a, b, c = 2, 4, 5
sa = 2 * (a * b + a * c + b * c)
v = a * b * c
eq("SA", sa, 76)
eq("V", v, 40)
eq("SA:V", sa / v, 1.9)
eq("V:SA", v / sa, 0.53, 0.005)
eq("SA counted twice", 2 * sa / v, 3.8)
# practice 4: percentage change
eq("change", 44 - 50, -6)
eq("percentage change", (44 - 50) / 50 * 100, -12)
eq("wrong: divide by final", (44 - 50) / 44 * 100, -13.6, 0.05)
# practice 8: inhibitor data
free = [12, 20, 28, 33, 35]
inh = [6, 10, 14, 16.5, 17.5]
for f_, i_ in zip(free, inh):
    eq("half", i_ / f_, 0.5, 0.02)
eq("plateau ratio", 17.5 / 35, 0.5)
# every practice question is 1 mark and has one token; options are lettered
qs = re.findall(r"^Q: \[1 mark\]", text, re.M)
eq("ten practice questions", len(qs), 10)
block = text.split(":::try Practice set: ten questions")[1].split("\n:::\n")[0]
eq("ten answers", len(re.findall(r"^A: \*\*[ABCD]\*\*", block, re.M)), 10)
eq("ten tokens", len(re.findall(r"\[B1\]", block)), 10)
print("ok")
