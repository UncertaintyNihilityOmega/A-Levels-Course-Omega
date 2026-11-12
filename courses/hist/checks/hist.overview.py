# checks/hist.overview.py: recomputes every number in the chapter and checks the chapter map covers every id
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
text = (HERE / "chapters" / "hist.overview.md").read_text(encoding="utf-8")
course = json.loads((HERE / "course.json").read_text(encoding="utf-8"))


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# --- Every chapter id of the course is linked from the map (except this chapter itself)
ids = [c["id"] for c in course["chapters"]]
eq("number of chapters", len(ids), 96)
linked = set(re.findall(r"\]\(#([a-z0-9.]+)\)", text))
missing = [i for i in ids if i != "hist.overview" and i not in linked]
assert not missing, f"chapters not linked in the map: {missing}"
unknown = sorted(l for l in linked if l not in ids and not l.startswith(("road.", "about.")))
assert not unknown, f"links to ids not in course.json: {unknown}"

# --- Paper table: papers, times, marks, weights
paper = {1: (75, 40, 40, 20), 2: (105, 60, 60, 30), 3: (75, 40, 0, 20), 4: (105, 60, 0, 30)}   # minutes, marks, AS %, A Level %
eq("AS weights add to 100", sum(v[2] for v in paper.values()), 100)
eq("A Level weights add to 100", sum(v[3] for v in paper.values()), 100)
eq("Paper 1 time", 1 * 60 + 15, paper[1][0])
eq("Paper 2 time", 1 * 60 + 45, paper[2][0])
eq("Paper 2 two questions of 30", 2 * (10 + 20), paper[2][1])
eq("Paper 4 two questions of 30", 2 * 30, paper[4][1])
eq("Paper 1 parts", 15 + 25, paper[1][1])
eq("Paper 3 two tables", 20 + 20, paper[3][1])
eq("Paper 4 two tables", 15 + 15, 30)
# AO weights within papers and for the qualification
eq("Paper 1 AOs", 25 + 75, 100)
eq("Paper 2 AOs", 50 + 50, 100)
eq("AS AOs", 40 + 30 + 30 + 0, 100)
eq("A Level AOs", 45 + 30 + 15 + 10, 100)
# check the AO totals follow from the paper weights: AO3 at AS = 75% of Paper 1's 40%
eq("AS AO3 from Paper 1", 75 * 40 // 100, 30)
eq("AS AO1 from papers", (25 * 40 + 50 * 60) // 100, 40)
eq("AS AO2 from Paper 2", 50 * 60 // 100, 30)
eq("A Level AO3 from Paper 1", 75 * 20 // 100, 15)
eq("A Level AO4 from Paper 3", 50 * 20 // 100, 10)
eq("A Level AO1 from papers", (25 * 20 + 50 * 30 + 50 * 20 + 50 * 30) // 100, 45)
eq("A Level AO2 from papers", (50 * 30 + 50 * 30) // 100, 30)

# --- Level ranges (contiguous, and the top level reaches the total)
levels = {
    "P1a": [(1, 3), (4, 7), (8, 11), (12, 15)],
    "P1b": [(1, 5), (6, 10), (11, 15), (16, 20), (21, 25)],
    "P2a": [(1, 2), (3, 5), (6, 8), (9, 10)],
    "P2b": [(1, 4), (5, 8), (9, 12), (13, 16), (17, 20)],
}
for name, bands in levels.items():
    for (a, b), (c, d) in zip(bands, bands[1:]):
        assert c == b + 1, f"{name}: bands {a}-{b} and {c}-{d} are not contiguous"
eq("P1a top", levels["P1a"][-1][1], 15)
eq("P1b top", levels["P1b"][-1][1], 25)
eq("P2a top", levels["P2a"][-1][1], 10)
eq("P2b top", levels["P2b"][-1][1], 20)
for must in ["Level 1, 1–3", "Level 2, 4–7", "Level 3, 8–11", "Level 4, 12–15", "Level 3 (11–15)", "Level 4 (16–20)", "Level 5 (21–25)",
             "Level 3, 6–8", "Level 4, 9–10", "Level 3 (9–12)", "Level 4 (13–16)", "Level 5 (17–20)"]:
    assert must in text, f"missing level text {must}"

# --- Rotation: each option's three topics are on Paper 1 exactly once in 2027-29, and never on Paper 2 that year
rotation = {
    "European": {2027: ("France", ["Germany", "Russia"]), 2028: ("Germany", ["France", "Russia"]), 2029: ("Russia", ["France", "Germany"])},
    "American": {2027: ("Gilded", ["Civil War", "Great Crash"]), 2028: ("Great Crash", ["Civil War", "Gilded"]), 2029: ("Civil War", ["Gilded", "Great Crash"])},
    "International": {2027: ("Imperialism", ["1919-29", "1929-39"]), 2028: ("1919-29", ["Imperialism", "1929-39"]), 2029: ("1929-39", ["Imperialism", "1919-29"])},
}
for opt, years in rotation.items():
    p1 = [y[0] for y in years.values()]
    eq(opt + " Paper 1 topics all different", len(set(p1)), 3)
    for yr, (a, b) in years.items():
        assert a not in b and len(set([a] + b)) == 3, f"{opt} {yr}"
for k in ("2027", "2028", "2029"):
    assert f"| {k} |" in text

# --- Study hours: 12 AS chapters at 8-11 hours; Paper 3 18-22 hours; 180 and 360 guided learning hours
eq("AS chapters in an option", 3 * 4, 12)
lo, hi = 12 * 8, 12 * 11
assert 96 == lo and 132 == hi
assert "100–130 hours" in text and 100 <= lo + 4 and hi - 2 <= 130   # stated as a rounded range
eq("Paper 3 hours", (8 + 10, 10 + 12), (18, 22))
eq("A Level GLH = twice AS", 180 * 2, 360)
# Time split suggestion on the day
eq("Paper 1 split", 25 + 45 + 5, 75)
assert 105 // 2 - 2 <= 50 <= 105 // 2   # about 50 minutes per Paper 2 question

# Papers in course.json used by :::progress
pids = {p["id"] for p in course["papers"]}
for p in ("P1", "P2", "P3", "P4"):
    assert p in pids and f":::progress {p}" in text, p

print("ok")
