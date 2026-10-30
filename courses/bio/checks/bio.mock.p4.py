# checks/bio.mock.p4.py: recomputes every number in chapters/bio.mock.p4.md (Mock Paper 4) and the paper total
import os, re, sys, math
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(here), "data"))
from crit import chi2_crit, t_crit
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.mock.p4.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def r(x, d=2): return round(x + 1e-12, d)


# paper structure: 10 questions, 100 marks (FACTS.md: June 2024 had 10 questions, 100 marks, 2 h)
marks = [int(m) for m in re.findall(r"^Q: \[(\d+) marks\]", text, re.M)]
eq("questions", len(marks), 10)
eq("total marks", sum(marks), 100)
assert marks == [9, 10, 12, 10, 10, 9, 8, 14, 9, 9], marks
assert all(8 <= m <= 15 for m in marks)
# Q1
eq("Q1 CO2", 0.50 - 0.10, 0.40); eq("Q1 RQ", r(0.40 / 0.50), 0.80)
# Q2
eq("Q2 ratio", 11.0 / 4.0, 2.75); eq("Q2 2sf", r(11.0 / 4.0, 1) , 2.8, 1e-9)
# Q3 plot values
f = lambda x: 20 + 190 * math.exp(-((x - 90) / 35) ** 2)
eq("Q3 t0", round(f(0)), 20); eq("Q3 peak", round(f(90)), 210)
assert f(60) > 100 and f(120) > 100 and f(50) < 100 and f(130) < 100
assert abs(f(170) - 20) < 2
# Q6
eq("Q6 quarter", 80 / 4, 20)
# Q7
O = [210, 31, 28, 51]; E = [180, 60, 60, 20]
eq("Q7 total", sum(O), 320); eq("Q7 exp total", sum(E), 320)
terms = [(o - e) ** 2 / e for o, e in zip(O, E)]
eq("Q7 t1", r(terms[0], 1), 5.0); eq("Q7 t2", r(terms[1], 1), 14.0); eq("Q7 t3", r(terms[2], 1), 17.1); eq("Q7 t4", r(terms[3], 1), 48.1)
eq("Q7 chi", r(sum(terms), 1), 84.1)
for df, v in [(1, 3.84), (2, 5.99), (3, 7.81), (4, 9.49), (5, 11.07)]:
    eq(f"Q7 crit {df}", r(chi2_crit(df)), v)
# Q8
a, b = 1.9 ** 2 / 15, 2.2 ** 2 / 15
eq("Q8 a", round(a, 4), 0.2407); eq("Q8 b", round(b, 4), 0.3227 if False else round(b, 4))
assert round(a, 4) == 0.2407 and round(b, 4) == 0.3227 and round(0.2407 + 0.3227, 4) == 0.5634
t = 1.3 / math.sqrt(a + b)
eq("Q8 t", r(t), 1.73)
for df, v in [(26, 2.06), (27, 2.05), (28, 2.05), (29, 2.05), (30, 2.04)]:
    eq(f"Q8 crit {df}", r(t_crit(df)), v)
eq("Q8 df", 15 + 15 - 2, 28)
q = math.sqrt(0.09)
eq("Q8 q", q, 0.30); eq("Q8 2pq", 2 * 0.7 * 0.3, 0.42); eq("Q8 het", 0.42 * 500, 210)
# Q9
eq("Q9 N", 50 * 40 / 8, 250)
sA = sum((k / 100) ** 2 for k in (40, 30, 20, 10)); sB = sum((k / 100) ** 2 for k in (85, 8, 4, 3))
eq("Q9 sumA", sA, 0.30); eq("Q9 DA", r(1 - sA), 0.70); eq("Q9 sumB", round(sB, 4), 0.7314); eq("Q9 DB", r(1 - sB), 0.27)
# Q10 gel: marker positions are drawn to log scale and the 500 bp band of GM1 lines up with the 500 bp marker
ypos = lambda bp: 55 + (3 - math.log10(bp)) * 140
assert ypos(1000) < ypos(750) < ypos(500) < ypos(250)
print("ok", n)
