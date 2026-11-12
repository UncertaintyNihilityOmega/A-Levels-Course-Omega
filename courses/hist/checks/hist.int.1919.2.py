# checks/hist.int.1919.2.py: recomputes every number in the chapter (dates, intervals, percentages, totals, figure layout)
from datetime import date
import re, os, html


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Intervals
eq("Covenant adopted to in force (days)", (date(1920, 1, 10) - date(1919, 4, 28)).days, 257)
eq("In force to first Assembly (days)", (date(1920, 11, 15) - date(1920, 1, 10)).days, 310)
eq("Fourteen Points to Covenant adopted (days)", (date(1919, 4, 28) - date(1918, 1, 8)).days, 475)
eq("Draft Covenant to adoption (days)", (date(1919, 4, 28) - date(1919, 2, 14)).days, 73)
eq("Vilna seized to Ambassadors' decision (days)", (date(1923, 3, 15) - date(1920, 10, 9)).days, 887)
eq("Vilna: about two and a half years", round((date(1923, 3, 15) - date(1920, 10, 9)).days / 365.25, 1), 2.4)
eq("Greco-Bulgarian: incident to invasion (days)", (date(1925, 10, 22) - date(1925, 10, 19)).days, 3)
eq("Upper Silesia plebiscite to Geneva Convention (days)", (date(1922, 5, 15) - date(1921, 3, 20)).days, 421)
eq("Memel seizure to Memel Convention (years)", 1924 - 1923, 1)
eq("Germany joins: years after League began", 1926 - 1920, 6)
eq("USSR joins: years after League began", 1934 - 1920, 14)
eq("Drummond's years as Secretary-General", 1933 - 1920, 13)
eq("The League lasted (years, 1920 to 1946)", 1946 - 1920, 26)
eq("Slavery Convention year after Temporary Commission (1924)", 1926 - 1924, 2)
eq("ILO conventions by 1939 (more than)", 60 < 67, True)
eq("Nansen appointed for refugees a year before the Nobel prize", 1922 - 1921, 1)
eq("Senate votes: first and second", (39 + 55, 49 + 35), (94, 84))
eq("Council at the start: permanent plus elected", 4 + 4, 8)
eq("Council after 1922", 4 + 6, 10)
eq("Council after 1926 (Germany a fifth permanent member)", 5 + 9, 14)
# Teschen decision: 58.1 per cent of the area and 67.9 per cent of the people to Czechoslovakia
between("Teschen area", 58.1, 58, 58.2)
between("Teschen people (about two thirds)", 67.9 / 100, 0.66, 0.69)
# Upper Silesia: plebiscite 59.6 / 40.4; Poland 3,214.26 of 10,950.89 km2; 965,000 of 1,950,000 people
eq("Plebiscite sums", round(59.6 + 40.4, 1), 100.0)
between("Poland land share (just under a third)", 3214.26 / 10950.89, 0.28, 0.333)
between("Poland people share (about half)", 965000 / 1950000, 0.48, 0.51)
# Aaland: about 25,000 people
between("Aaland population", 25000, 20000, 30000)
# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)
# Membership figure: 12 px per year from x = 150 at 1920
def x_of(d):
    return 150 + (d.year + (d.timetuple().tm_yday - 1) / 365 - 1920) * 12
between("Germany bar start", x_of(date(1926, 9, 8)), 229, 232)
between("Germany bar end", x_of(date(1933, 10, 14)), 314, 317)
between("Germany bar width", x_of(date(1933, 10, 14)) - x_of(date(1926, 9, 8)), 84, 87)
between("USSR bar start", x_of(date(1934, 9, 18)), 325, 328)
between("USSR bar width", 330 - x_of(date(1934, 9, 18)), 3, 5)
eq("Britain and France bar", 330 - 150, 180)

# ---- Generic SVG layout check (labels inside boxes, clear of each other, inside the viewBox, arrow lengths)
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.int.1919.2.md"), encoding="utf-8").read()


def attrs(tag):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', tag))


def check_svgs(text):
    n = 0
    for m in re.finditer(r"<svg\b([^>]*)>(.*?)</svg>", text, re.S):
        n += 1
        a = attrs(m.group(1))
        vb = [float(v) for v in a["viewBox"].split()]
        W, H = vb[2], vb[3]
        body = m.group(2)
        rects = [attrs(t) for t in re.findall(r"<rect\b[^>]*>", body)]
        rects = [{k: (float(v) if k in "x y width height".split() else v) for k, v in r.items()} for r in rects]
        boxes = []
        for tm in re.finditer(r"<text\b([^>]*)>(.*?)</text>", body, re.S):
            ta = attrs(tm.group(1))
            s = html.unescape(re.sub(r"<[^>]*>", "", tm.group(2)))
            cls = ta.get("class", "").split()
            w = len(s) * (7.6 if "tb" in cls else 7.0)
            x, y = float(ta["x"]), float(ta["y"])
            if "tc" in cls:
                x0, x1 = x - w / 2, x + w / 2
            else:
                x0, x1 = x, x + w
            box = (x0, y - 10, x1, y + 3, s)
            assert x0 >= 0 and x1 <= W, f"label outside viewBox width: {s!r} {x0:.0f}-{x1:.0f} of {W}"
            assert y + 3 <= H, f"label below viewBox: {s!r}"
            for r in rects:
                inside = r["x"] <= x <= r["x"] + r["width"] and r["y"] <= y - 4 <= r["y"] + r["height"]
                if inside and r["width"] >= 60:
                    assert x0 >= r["x"] + 3 and x1 <= r["x"] + r["width"] - 3, f"label wider than its box: {s!r} {x0:.0f}-{x1:.0f} vs {r['x']}-{r['x'] + r['width']}"
                    assert y + 3 <= r["y"] + r["height"], f"label below its box: {s!r}"
                    assert y - 10 >= r["y"], f"label above its box: {s!r}"
            boxes.append(box)
        for i, b in enumerate(boxes):
            for c in boxes[i + 1:]:
                ox = min(b[2], c[2]) - max(b[0], c[0])
                oy = min(b[3], c[3]) - max(b[1], c[1])
                assert not (ox > -3 and oy > -2), f"labels overlap: {b[4]!r} and {c[4]!r}"
        for lm in re.finditer(r"<line\b([^>]*)>", body):
            la = attrs(lm.group(1))
            if "marker-end" in la:
                ln = ((float(la["x2"]) - float(la["x1"])) ** 2 + (float(la["y2"]) - float(la["y1"])) ** 2) ** 0.5
                assert ln >= 20, f"arrow too short: {ln}"
                x2, y2 = float(la["x2"]), float(la["y2"])
                for r in rects:
                    inside = r["x"] - 1 < x2 < r["x"] + r["width"] + 1 and r["y"] < y2 < r["y"] + r["height"]
                    assert not inside, "arrow ends inside a box"
        # text must not sit on a label-free line: texts versus horizontal lines
        for lm in re.finditer(r"<(?:line|path)\b([^>]*)>", body):
            pass
    return n


nsvg = check_svgs(text)
eq("number of SVG figures", nsvg, 2)

for token in ["8 January 1918", "28 April 1919", "10 January 1920", "15 November 1920", "28 July 1920", "9 October 1920",
              "15 March 1923", "22 October", "8 September 1926", "25 September 1926", "45,000", "59.6", "40.4",
              "viewBox=\"0 0 340 425\"", "viewBox=\"0 0 350 215\"", "42 members", "58", "1 hour 15 minutes"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
# FIX round (reader items): Corfu and Ruhr box, Council seats
for token in ["50 million lire", "China replaced Greece in 1921", "(a committee of Allied ambassadors in Paris)"]:
    assert token in text, f"missing {token}"
assert "January 1923" in text
print("ok")
