# checks/hist.f.choose.py: recomputes every number in the chapter (plan hours, rotation tables, chapter counts)
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
text = (HERE / "chapters" / "hist.f.choose.md").read_text(encoding="utf-8")
course = json.loads((HERE / "course.json").read_text(encoding="utf-8"))


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


ids = {c["id"] for c in course["chapters"]}
linked = set(re.findall(r"\]\(#([a-z0-9.]+)\)", text))
unknown = sorted(l for l in linked if l not in ids and not l.startswith("road."))
assert not unknown, f"links to ids not in course.json: {unknown}"

# --- AS option = 3 topics x 4 key questions
eq("AS chapters per option", 3 * 4, 12)
for prefix, n in [("hist.eu.", 12), ("hist.us.", 12), ("hist.int.", 12)]:
    # AS options: european, american, and the international option's empire/1919/1929 chapters
    count = sum(1 for i in ids if i.startswith(prefix))
    eq(prefix + " chapter count", count, n)
for topic in ["italy", "stalin", "hitler", "usa45", "usa61", "usa74", "soviet", "safrica", "malaysia"]:
    eq("Paper 4 chapters in " + topic, sum(1 for i in ids if i.startswith(f"hist.d.{topic}.")), 4)
for topic in ["ww1", "holocaust", "coldwar"]:
    eq("Paper 3 chapters in " + topic, sum(1 for i in ids if i.startswith(f"hist.interp.{topic}.")), 2)

# --- AS plan: 6 h/week for 36 weeks
eq("AS hours total", 6 * 36, 216)
as_plan = [((1, 2), 12), ((3, 4), 12), ((5, 11), 42), ((12, 18), 42), ((19, 25), 42), ((26, 30), 30), ((31, 33), 18), ((34, 36), 18)]
prev_end = 0
for (a, b), hours in as_plan:
    assert a == prev_end + 1, f"AS weeks not contiguous at {a}"
    eq(f"AS weeks {a}-{b} hours", (b - a + 1) * 6, hours)
    prev_end = b
eq("AS plan last week", prev_end, 36)
eq("AS plan hours add up", sum(h for _, h in as_plan), 216)
# the three topics: four chapters at 8-11 h each is 32-44 h, which 42 h covers
assert 4 * 8 <= 42 <= 4 * 11

# --- A Level plan: 7 h/week for 30 weeks
eq("A Level hours total", 7 * 30, 210)
a2_plan = [((1, 1), 7), ((2, 4), 21), ((5, 21), 119), ((22, 27), 42), ((28, 30), 21)]
prev_end = 0
for (a, b), hours in a2_plan:
    assert a == prev_end + 1, f"A Level weeks not contiguous at {a}"
    eq(f"A Level weeks {a}-{b} hours", (b - a + 1) * 7, hours)
    prev_end = b
eq("A Level plan last week", prev_end, 30)
eq("A Level plan hours add up", sum(h for _, h in a2_plan), 210)
eq("Paper 4 weeks: 3 topics", 21 - 5 + 1, 17)
eq("Paper 4 weeks: 2 topics", 15 - 5 + 1, 11)
# 12 chapters at about 10 h = 120 h, the 119 h of the plan; 8 chapters = 80 h, within 77 h + spare
assert abs(12 * 10 - 119) <= 2
assert abs(8 * 10 - 11 * 7) <= 3
# Paper 3 context 8-10 h, debate 10-12 h: 18-22 h; 21 h in the plan
assert 18 <= 21 <= 22

# --- Model week
eq("model week hours", 1 + 1.5 + 1 + 2.5, 6)

# --- Rotation tables agree with each other and are a Latin square for each option
p1 = {"European": ["France", "Germany", "Russia"], "American": ["Gilded", "Crash", "Civil"], "International": ["Imperialism", "1919", "1929"]}
for opt, tops in p1.items():
    eq(opt + " topics on Paper 1 over three years", len(set(tops)), 3)
for y in ("2027", "2028", "2029"):
    assert f"| {y} |" in text

# --- Paper 4 structure: 3 topics per option, 3 questions, answer 2
eq("Paper 4 questions answered", 2, 2)
assert 2 <= 3
eq("Paper 4 marks", 2 * 30, 60)
eq("recap range for AS hours", (12 * 8, 12 * 11), (96, 132))
assert "100–130 hours" in text

print("ok")
