# checks/bio.mixed.as.py: recomputes every number in chapters/bio.mixed.as.md (AS mixed practice)
import os, re, math
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(os.path.dirname(here), "chapters", "bio.mixed.as.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# Section 1
eq("magnification", 63 * 1000 / 18, 3500)
comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
strand = "TACGGCAT"
other = "".join(comp[b] for b in strand)
assert other == "ATGCCGTA", other
hb = sum(2 if b in "AT" else 3 for b in strand)
eq("hydrogen bonds", hb, 20)
eq("cube SA", 6 * 0.6 ** 2, 2.16)
eq("cube V", 0.6 ** 3, 0.216)
eq("cube SA:V", 6 * 0.6 ** 2 / 0.6 ** 3, 10)
eq("chromatids at prophase", 12 * 2, 24)
tmpl = "TACCGATTG"
mrna = "".join({"A": "U", "T": "A", "C": "G", "G": "C"}[b] for b in tmpl)
assert mrna == "AUGGCUAAC", mrna
assert comp["G"] == "C" and "".join({"G": "C", "C": "G", "U": "A"}[b] for b in "GCU") == "CGA"
eq("zone area", math.pi * 9 ** 2, 254, 0.5)
# Section 2
eq("heart rate", 60 / 0.8, 75)
assert 12.5 > 12.3 and 3.5 > 1 and 3.5 < 10.7 and 3.0 < 4  # valve logic at 0.1 s and 0.2 s
eq("maternal fall", (100 - 25) / 100 * 100, 75)
eq("culture rise", (4.1 - 2.0) / 2.0 * 100, 105)
eq("net fall", (210 - 70) / 210 * 100, 66.7, 0.05)
f = lambda p, k: 100 * p ** 2.7 / (k ** 2.7 + p ** 2.7)
for p, k, want in [(4, 3.4, 61), (4, 2.2, 83), (8, 3.4, 91), (8, 2.2, 97)]:
    eq(f"ODC {p} {k}", f(p, k), want, 0.5)
eq("human unloads", 91 - 61, 30)
eq("X unloads", 97 - 83, 14)

# structure: marks, interleaving
topic = {}
for ids, t in [("microscopy cells prokaryotes", 1), ("foodtests carbs lipids proteins", 2), ("enzymes enzymes2", 3),
               ("membranes movement", 4), ("mitosis", 5), ("dna synthesis", 6), ("planttransport translocation", 7),
               ("mammaltransport oxygen heart", 8), ("gasexchange", 9), ("disease antibiotics", 10),
               ("immunity antibodies", 11)]:
    for i in ids.split():
        topic["bio." + i] = t
# carbs/proteins/foodtests are all topic 2 in the syllabus but neighbours must also differ by chapter
sections = re.split(r"^## ", text, flags=re.M)
totals = {}
for sec in sections:
    title = sec.split("\n")[0]
    if not title.startswith("Section 1") and not title.startswith("Section 2"):
        continue
    qs = re.findall(r"^Q: \[(\d+) marks\] (★+) \(#([\w.]+)\)", sec, flags=re.M)
    ids = [q[2] for q in qs]
    for a, b in zip(ids, ids[1:]):
        assert topic[a] != topic[b], f"neighbours from the same topic: {a}, {b}"
    totals[title[:9]] = sum(int(q[0]) for q in qs)
    stars = [len(q[1]) for q in qs]
    assert stars == sorted(stars), f"stars not in order in {title}"
eq("section 1 marks", totals["Section 1"], 38)
eq("section 2 marks", totals["Section 2"], 59)
s3 = re.findall(r"^:::try Extended.*\nQ: \[(\d+) marks\]", text, flags=re.M)
eq("section 3 questions", len(s3), 6)
eq("section 3 marks", sum(int(x) for x in s3), 48)
eq("section 4 questions", len(re.findall(r"^\? ", text, flags=re.M)), 10)
for blk in text.split(":::quiz")[1:]:
    for q in re.split(r"^\? ", blk, flags=re.M)[1:]:
        eq("one correct", len(re.findall(r"^\+ ", q, flags=re.M)), 1)
print("ok")
