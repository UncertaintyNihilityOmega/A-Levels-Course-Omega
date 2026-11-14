# data/p9_combine.py: builds checks/<id>.py from the gold helper (lines 1-113 of checks/cs.datatypes.py) and a body file.
import sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
chapter_id, body = sys.argv[1], sys.argv[2]
gold = (root / "checks" / "cs.datatypes.py").read_text(encoding="utf-8").split("\n")
head = "\n".join(gold[:113]).replace('CHAPTER_ID = "cs.datatypes"', f'CHAPTER_ID = "{chapter_id}"')
head = head.replace("# checks/cs.datatypes.py:", f"# checks/{chapter_id}.py:")
(root / "checks" / f"{chapter_id}.py").write_text(head + "\n" + (root / body).read_text(encoding="utf-8"), encoding="utf-8")
