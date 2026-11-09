# checks/hist.interp.coldwar.1.py: recomputes every number in the chapter (date arithmetic, percentages, totals, timeline widget, map layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs

text = open(os.path.join(here, "..", "chapters", "hist.interp.coldwar.1.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# intervals
eq("Truman Vice-President days (20 Jan to 12 Apr 1945)", (date(1945, 4, 12) - date(1945, 1, 20)).days, 82)
eq("Yalta length in days (4-11 Feb inclusive)", (date(1945, 2, 11) - date(1945, 2, 4)).days + 1, 8)
eq("Blockade length (24 Jun 1948 to 12 May 1949)", (date(1949, 5, 12) - date(1948, 6, 24)).days, 322)
between("Blockade almost eleven months", 322 / 30.44, 10.4, 10.7)
eq("Airlift ends 30 Sep 1949: months after start", (1949 - 1948) * 12 + 9 - 6, 15)
eq("Fulton to Truman Doctrine (days)", (date(1947, 3, 12) - date(1946, 3, 5)).days, 372)
eq("US atomic monopoly: Hiroshima to Soviet test (years)", 1949 - 1945, 4)
between("monopoly just over four years", (date(1949, 8, 29) - date(1945, 8, 6)).days / 365.25, 4.0, 4.1)
eq("Percentages to Yalta (days)", (date(1945, 2, 4) - date(1944, 10, 9)).days, 118)
eq("NATO signed to first Soviet test (days)", (date(1949, 8, 29) - date(1949, 4, 4)).days, 147)
eq("Trinity to Hiroshima (days)", (date(1945, 8, 6) - date(1945, 7, 16)).days, 21)
between("bomb events within a month", (date(1945, 8, 9) - date(1945, 7, 16)).days, 0, 31)
eq("Brussels Treaty to NATO (days)", (date(1949, 4, 4) - date(1948, 3, 17)).days, 383)
eq("Katyn to Soviet admission (years)", 1990 - 1940, 50)
eq("Djilas memoir years after the conversation", 1962 - 1945, 17)
eq("Churchill account years after Percentages", 1953 - 1944, 9)
eq("Czech crisis days", (date(1948, 2, 25) - date(1948, 2, 20)).days, 5)
# Marshall Plan: about 13 billion over four years (1948-52)
eq("Marshall Plan span", 1952 - 1948, 4)
between("per year", 13 / 4, 3.2, 3.3)
# Airlift tonnage
us, uk = 1783573, 541937
between("airlift total tons", us + uk, 2.3e6, 2.4e6)
between("US share (about three-quarters)", us / (us + uk), 0.74, 0.79)
# Soviet demobilisation: 11.3 to 2.8 million
between("Soviet armed forces cut (about three-quarters)", 1 - 2.8 / 11.3, 0.74, 0.76)
# NATO founding members
members = "USA, Canada, Britain, France, Belgium, the Netherlands, Luxembourg, Italy, Portugal, Norway, Denmark and Iceland".replace(" and ", ", ").split(", ")
eq("NATO founders", len(members), 12)
eq("Brussels Treaty states", len("Britain, France, Belgium, the Netherlands and Luxembourg".replace(" and ", ", ").split(", ")), 5)
eq("Cominform parties", len("the USSR, Bulgaria, Czechoslovakia, Hungary, Poland, Romania, Yugoslavia, French, Italian".split(", ")), 9)
eq("Hungary 1945 Smallholders + Communists below 100", 57 + 17 < 100, True)
between("Soviet to US losses ratio", 27e6 / 4e5, 60, 70)

# timeline widget
m = re.search(r'data-lanes="([^"]*)" data-events="([^"]*)"', text)
lanes = [x.strip() for x in m.group(1).split(",")]
events = [e.strip() for e in m.group(2).split(" ;; ") if e.strip()]
eq("timeline events", len(events), 26)
prev = None
for e in events:
    f = [x.strip() for x in e.split(" | ")]
    eq("fields in " + f[0], len(f), 4)
    assert f[3] in lanes, f"unknown lane {f[3]}"
    y, mo, d = (int(v) for v in f[0].split("-"))
    dt = date(y, mo, d)
    assert prev is None or dt >= prev, f"timeline out of order at {f[0]}"
    prev = dt
eq("lanes", len(lanes), 4)

# story table: dates in order where a single date is given
rows = re.findall(r"^\| (\d{1,2}) (\w+) (\d{4}) \|", text, re.M)
months = {m: i for i, m in enumerate("January February March April May June July August September October November December".split(), 1)}
ds = [date(int(y), months[mo], int(d)) for d, mo, y in rows]
assert ds == sorted(ds), "story table dates are not in order"

# figures
svgs = re.findall(r"<svg\b.*?</svg>", text, re.S)
eq("two figures", len(svgs), 2)
eq("svg layout checks", check_svgs(text), 2)
s = svgs[0]
paths = re.findall(r'<path class="([^"]*)" d="([^"]*)"', s)


def poly(d):
    return [tuple(float(v) for v in p.split(",")) for p in re.findall(r"[\d.]+,[\d.]+", d)]


zones = {}
for cls, d in paths:
    if "dash" in cls:
        continue
    zones[cls.split()[0]] = poly(d)


def inside(pt, pg):
    x, y = pt
    c = False
    for i in range(len(pg)):
        (x1, y1), (x2, y2) = pg[i], pg[(i + 1) % len(pg)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


want = {"British zone": "f1", "Soviet zone": "f3", "US zone": "f2", "French": "fm2", "zone": "fm2"}
for tm in re.finditer(r'<text class="([^"]*)" x="([\d.]+)" y="([\d.]+)">([^<]*)</text>', s):
    cls, x, y, t = tm.group(1), float(tm.group(2)), float(tm.group(3)), tm.group(4)
    if t in want:
        w = len(t) * (7.6 if "tb" in cls else 7.0)
        for corner in [(x + 2, y - 9), (x + w - 2, y - 9), (x + 2, y + 2), (x + w - 2, y + 2)]:
            assert inside(corner, zones[want[t]]), f"label {t!r} corner {corner} outside its zone"
cm = re.search(r'<circle class="[^"]*" cx="([\d.]+)" cy="([\d.]+)"', s)
assert inside((float(cm.group(1)), float(cm.group(2))), zones["f3"]), "Berlin outside Soviet zone"
dash = [poly(d) for cls, d in paths if "dash" in cls][0]
for p in dash:
    assert p in zones["f3"], f"dashed point {p} is not on the Soviet zone edge"
for gx in range(0, 340, 3):
    for gy in range(0, 410, 3):
        n = sum(inside((gx, gy), pg) for pg in zones.values())
        assert n <= 1, f"zones overlap at {gx},{gy}"
print("ok")
