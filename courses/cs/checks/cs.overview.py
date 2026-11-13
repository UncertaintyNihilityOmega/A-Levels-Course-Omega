# checks/cs.overview.py: every chapter in course.json is linked from the map, and the paper table matches FACTS.md.
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = (ROOT / "chapters" / "cs.overview.md").read_text(encoding="utf-8")
course = json.loads((ROOT / "course.json").read_text(encoding="utf-8"))

linked = set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT))
ids = [c["id"] for c in course["chapters"]]
missing = [i for i in ids if i not in linked]
assert not missing, f"chapters not linked from the course map: {missing}"
unknown = sorted(linked - set(ids))
assert not unknown, f"links to ids not in course.json: {unknown}"
assert len(ids) == 49, len(ids)

# the paper table (FACTS.md: The papers)
papers = {
    "| 1 | Theory Fundamentals | 1 h 30 min | 75 | 1–8 | 50% | 25% |",
    "| 2 | Fundamental Problem-solving and Programming Skills | 2 h | 75 | 9–12 | 50% | 25% |",
    "| 3 | Advanced Theory | 1 h 30 min | 75 | 13–20 | none | 25% |",
    "| 4 | Practical | 2 h 30 min | 75 | 19–20, except low-level and declarative programming | none | 25% |",
}
for row in papers:
    assert row in TEXT, row

# weightings add up: AS 50 + 50, A Level 4 x 25, AO rows 100
assert 50 + 50 == 100 and 25 * 4 == 100
for row in ("| AS Level overall | 30% | 40% | 30% |", "| A Level overall | 30% | 30% | 40% |",
            "| Paper 1 | 60% | 40% | none |", "| Paper 2 | none | 40% | 60% |",
            "| Paper 3 | 60% | 40% | none |", "| Paper 4 | none | none | 100% |"):
    assert row in TEXT, row
assert 30 + 40 + 30 == 100 and 60 + 40 == 100 and 40 + 60 == 100
# pace: 180 and 360 hours at 6 hours a week
assert 180 // 6 == 30 and 360 // 6 == 60
assert "about 30 weeks" in TEXT and "60 for the A Level" in TEXT
print("ok")
