# checks/bio.overview.py: recomputes the numbers in the course map (chapters/bio.overview.md).
import json, re, math, os

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# Paper table (FACTS.md "Exam structure")
marks = {1: 40, 2: 60, 3: 40, 4: 100, 5: 30}
as_w = {1: 31, 2: 46, 3: 23}
a_w = {1: 15.5, 2: 23, 3: 11.5, 4: 38.5, 5: 11.5}
eq("AS weights add to 100", sum(as_w.values()), 100)
eq("A Level weights add to 100", sum(a_w.values()), 100)
for p in (1, 2, 3):
    eq(f"paper {p}: A Level weight is half the AS weight", a_w[p], as_w[p] / 2)
eq("AO weights", 40 + 40 + 20, 100)
eq("Paper 1 questions = marks", 40, marks[1])

# Chapter lists from course.json
cj = json.load(open(os.path.join(root, "course.json"), encoding="utf-8"))
ch = cj["chapters"]
ids = [c["id"] for c in ch]
text = open(os.path.join(root, "chapters", "bio.overview.md"), encoding="utf-8").read()
linked = set(re.findall(r"\(#(bio\.[A-Za-z0-9_.]+)\)", text))
for i in ids:
    if i != "bio.overview":
        assert i in linked, f"{i} is not linked in the course map"
eq("every chapter linked", len([i for i in ids if i != "bio.overview" and i in linked]), len(ids) - 1)

skills = {"bio.f.basics", "bio.maths", "bio.practical", "bio.practical2", "bio.stats", "bio.planning", "bio.evaluation"}
as_topic = [c["id"] for c in ch if c["level"] == "as" and c["id"] not in skills]
a2_topic = [c["id"] for c in ch if c["level"] == "a2" and c["id"] not in skills]
as_skills = [c for c in ("bio.maths", "bio.practical", "bio.practical2")]
a2_skills = [c for c in ("bio.stats", "bio.planning", "bio.evaluation")]
eq("AS topic chapters", len(as_topic), 24)
eq("A Level topic chapters", len(a2_topic), 22)
eq("AS chapters incl. skills", len(as_topic) + len(as_skills), 27)
eq("A Level extra chapters incl. skills", len(a2_topic) + len(a2_skills), 25)

# Pace table: weeks = chapters / (chapters per week), rounded up
for per, as_wk, a_wk in ((2, 14, 13), (3, 9, 9), (4, 7, 7)):
    eq(f"AS weeks at {per}/week", math.ceil(27 / per), as_wk)
    eq(f"A Level weeks at {per}/week", math.ceil(25 / per), a_wk)
print("ok")
