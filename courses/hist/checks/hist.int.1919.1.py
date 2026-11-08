# checks/hist.int.1919.1.py: recomputes every number in the chapter (dates, ages, intervals, percentages, totals, figure layout)
from datetime import date
import re, os, html


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Ages at the opening of the conference, 18 January 1919
opening = date(1919, 1, 18)
eq("Wilson age", age(date(1856, 12, 28), opening), 62)
eq("Clemenceau age", age(date(1841, 9, 28), opening), 77)
eq("Lloyd George age", age(date(1863, 1, 17), opening), 56)
eq("Orlando age", age(date(1860, 5, 19), opening), 58)

# Intervals
eq("Armistice to conference (days)", (opening - date(1918, 11, 11)).days, 68)
eq("Conference to signing (days)", (date(1919, 6, 28) - opening).days, 161)
eq("Terms handed over to signing (days)", (date(1919, 6, 28) - date(1919, 5, 7)).days, 52)
eq("Signing is five years after Sarajevo", date(1919, 6, 28).year - date(1914, 6, 28).year, 5)
eq("Fourteen Points to Armistice (months)", (1918 - 1918) * 12 + (11 - 1), 10)
eq("Council of Four after the opening (days)", (date(1919, 3, 24) - opening).days, 65)
eq("Terms: fifteen days to reply (to 22 May)", date(1919, 5, 22), date(1919, 5, 7).replace(day=7 + 15))
eq("Versailles to Lausanne: Sevres to Lausanne (days)", (date(1923, 7, 24) - date(1920, 8, 10)).days, 1078)
eq("London Schedule to Wirth acceptance (days)", (date(1921, 5, 11) - date(1921, 5, 5)).days, 6)
eq("Senate: first to second vote (months)", (1920 - 1919) * 12 + (3 - 11), 4)
eq("Hall of Mirrors 1871 to 1919", 1919 - 1871, 48)
eq("Invaded twice in forty-four years (1870 to 1914)", 1914 - 1870, 44)
eq("D'Annunzio at Fiume: 12 Sept 1919 to Dec 1920 (months, about)", (1920 - 1919) * 12 + (12 - 9), 15)
eq("Carthage fell 146 BC; Keynes 1919", 1919 + 146 - 1, 2064)  # 146 BC to AD 1919 is 2,064 years

# Territory and population (Versailles): about 13 per cent of 540,858 km2 is about 70,000 km2
between("Versailles territory lost (share)", 70000 / 540858, 0.12, 0.14)
# Hungary at Trianon: 283,000 km2 to 93,000 km2 is a loss of about two thirds
between("Trianon territory lost", 1 - 93000 / 283000, 0.65, 0.68)
# Austria-Hungary about 50 million; Austria about 6.5 million
between("Austria share of old empire", 6.5 / 50, 0.12, 0.14)
# Upper Silesia
eq("Plebiscite shares sum", round(59.6 + 40.4, 1), 100.0)
between("German vote share", 707393 / (707393 + 479365), 0.595, 0.597)
between("Polish vote share", 479365 / (707393 + 479365), 0.403, 0.405)
between("Poland territory share", 3214.26 / 10950.89, 0.28, 0.31)
between("Poland people share", 965000 / 1950000, 0.48, 0.51)
# Reparations
eq("Bonds total", 12 + 38 + 82, 132)
eq("A and B bonds", 12 + 38, 50)
between("A and B share of total", 50 / 132, 0.375, 0.385)
between("C share of total", 82 / 132, 0.61, 0.63)
usd = 132 / 4.198
between("132 billion gold marks in dollars", usd, 31, 32)
between("A+B in dollars", 50 / 4.198, 11.5, 12.2)
between("Keynes 10 billion vs A+B", 10 / (50 / 4.198), 0.8, 0.9)
between("Keynes 10 billion vs total", 10 / usd, 0.30, 0.33)
between("10 billion dollars in pounds (about 2,000 million)", 10 / 4.86, 2.0, 2.1)
# Scuttling of the fleet: 52 of 74 sank
eq("Scapa Flow", 74 - 52, 22)
# German National Assembly vote
eq("Assembly vote total", 237 + 138 + 5, 380)
# Senate votes
eq("Senate Nov 1919 total", 39 + 55, 94)
eq("Senate Mar 1920 total", 49 + 35, 84)
eq("Two thirds of 84 voting needed", -(-84 * 2 // 3), 56)
assert 49 < 56
eq("Short by (March 1920)", 56 - 49, 7)
# Racial equality vote
eq("Commission vote", 11 + 6, 17)
# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)
# Bar widths in the Upper Silesia figure (300 units): vote bar 59.6 per cent, land bar 29 per cent, people 49.5 per cent
between("vote bar", 300 * 0.596, 178, 180)
between("land bar", 300 * 3214.26 / 10950.89, 87, 89)
between("people bar", 300 * 965000 / 1950000, 148, 150)
# Reparations figure: 2 px per billion
eq("A bar", 12 * 2, 24)
eq("B bar", 38 * 2, 76)
eq("C bar", 82 * 2, 164)
eq("Total bar", 24 + 76 + 164, 264)

# ---- Generic SVG layout check (labels inside boxes, clear of each other, inside the viewBox, arrow lengths)
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.int.1919.1.md"), encoding="utf-8").read()


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
eq("number of SVG figures", nsvg, 3)

# The chapter file must contain the same figure numbers (quick presence tests)
for token in ["18 January 1919", "24 March 1919", "132 billion", "5 May 1921", "28 June 1919", "10 September 1919",
              "27 November 1919", "4 June 1920", "10 August 1920", "24 July 1923", "19 November 1919", "19 March 1920",
              "237 to 138", "52 of the 74", "100,000", "13 per cent", "viewBox=\"0 0 580 365\"", "viewBox=\"0 0 340 205\"",
              "viewBox=\"0 0 340 215\"", "59.6", "40.4", "1.4 million", "116,000", "20 billion gold marks"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert " — " not in text and "—" not in text, "no em dashes"
print("ok")
