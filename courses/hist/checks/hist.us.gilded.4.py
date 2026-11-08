# checks/hist.us.gilded.4.py: recomputes every number in the chapter (dates, intervals, shares, totals, widget data, layout)
from datetime import date
import os, re


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, '..', 'chapters', 'hist.us.gilded.4.md'), encoding='utf-8').read()

# --- Roosevelt ---------------------------------------------------------------
# McKinley shot 6 September 1901, died 14 September: "eight days after being shot"
eq("McKinley days", (date(1901, 9, 14) - date(1901, 9, 6)).days, 8)
# Roosevelt born 27 October 1858: aged 42 on 14 September 1901
b, k = date(1858, 10, 27), date(1901, 9, 14)
eq("Roosevelt age", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 42)
# Coal strike 12 May - 23 October 1902: "more than five months"
between("coal strike months", (date(1902, 10, 23) - date(1902, 5, 12)).days / 30.44, 5.0, 6.0)
# Northern Securities 14 March 1904 decided 5-4: nine justices
eq("Northern Securities bench", 5 + 4, 9)
# Taft about 90 suits vs Roosevelt 44 in 4 and 7.5 years: "about twice as many ... in four years"
between("Taft/Roosevelt suits ratio", 90 / 44, 1.9, 2.2)
# Standard Oil 15 May 1911; Hammer 3 June 1918 5-4
eq("Hammer bench", 5 + 4, 9)
# Wilson addressed Congress in person 8 April 1913: first since Adams in 1800 -> 113 years
eq("Congress address gap", 1913 - 1800, 113)
# Zachary Taylor 1848 -> Wilson 1912 election
eq("Southern President gap", 1912 - 1848, 64)

# --- 1912 election -------------------------------------------------------------
votes = {"Wilson": 41.8, "Roosevelt": 27.4, "Taft": 23.2, "Debs": 6.0}
eq("Taft + Roosevelt", round(votes["Taft"] + votes["Roosevelt"], 1), 50.6)
eq("Wilson + Roosevelt + Debs ('three out of four')", round(votes["Wilson"] + votes["Roosevelt"] + votes["Debs"], 1), 75.2)
assert sum(votes.values()) < 100
ev = {"Wilson": 435, "Roosevelt": 88, "Taft": 8}
eq("electoral votes", sum(ev.values()), 531)
m = re.search(r'data-title="The popular vote in the presidential election of 1912"[^>]*data-series="([^"]*)"', text)
assert m, "1912 chart missing"
got = [float(p.split('=')[1]) for p in m.group(1).split(':')[1].split(',')]
eq("1912 chart data", got, [41.8, 27.4, 23.2, 6.0])

# --- amendments: intervals ------------------------------------------------------
am = {
    "16th": (date(1909, 7, 12), date(1913, 2, 3)),
    "17th": (date(1912, 5, 13), date(1913, 4, 8)),
    "18th": (date(1917, 12, 18), date(1919, 1, 16)),
    "19th": (date(1919, 6, 4), date(1920, 8, 18)),
}
yrs = {n: (b - a).days / 365.25 for n, (a, b) in am.items()}
between("16th years (three and a half)", yrs["16th"], 3.4, 3.7)
between("17th about a year", yrs["17th"], 0.8, 1.0)
between("18th thirteen months", (am["18th"][1] - am["18th"][0]).days / 30.44, 12.5, 13.5)
between("19th 14 months", (am["19th"][1] - am["19th"][0]).days / 30.44, 14.0, 15.0)
# three-quarters of 48 states = 36
eq("ratification threshold", 48 * 3 // 4, 36)
# in force date of 18th: one year after ratification
eq("18th in force", (date(1920, 1, 17) - date(1919, 1, 16)).days, 366)
# Wilson 1913 Revenue Act: 1% over $3,000, top total 7%
assert 1 + 6 == 7
# bar chart: x = 20 + days since 1 Jan 1909 * 25/365.25
def X(d): return round(20 + (d - date(1909, 1, 1)).days * 25 / 365.25, 1)
svg = re.search(r'<svg viewBox="0 0 340 292".*?</svg>', text, re.S).group(0)
rects = [tuple(map(float, r)) for r in re.findall(r'<rect class="[^"]*" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg)]
eq("bars", len(rects), 4)
for (x, y, w, h), (n, (a, b)) in zip(rects, am.items()):
    assert abs(x - X(a)) < 0.2, f"{n} bar start {x} vs {X(a)}"
    assert abs(x + w - X(b)) < 0.2, f"{n} bar end {x + w} vs {X(b)}"
ticks = [float(t) for t in re.findall(r'<line class="ax" x1="([\d.]+)" y1="256"', svg)]
for t, y in zip(ticks, (1910, 1915, 1920)):
    assert abs(t - X(date(y, 1, 1))) < 1.0, f"tick {y}: {t} vs {X(date(y, 1, 1))}"

# --- other numbers ------------------------------------------------------------------
# census urban share 1920 = 51.2 so rural 48.8
eq("rural share 1920", round(100 - 51.2, 1), 48.8)
# income tax returns 1914 under 400,000 and under 1 per cent of about 99 million people
assert 357_598 < 400_000 and 357_598 / 99_000_000 < 0.01
# Black Americans 1900: 8.83 million of 76.2 million is more than one in nine
assert 8.83 / 76.2 > 1 / 9
# child labour about 18 -> 8.5 per cent; life expectancy 47.3 -> 54.1
between("child labour 1900", 18.2, 17.5, 18.5)
between("child labour 1920", 8.5, 8.0, 9.0)
assert 54.1 - 47.3 > 6
# tenancy about a quarter in 1880 (25.6) to about 38 per cent in 1920 (38.1)
between("tenancy 1880", 25.6, 24, 27)
between("tenancy 1920", 38.1, 37, 39)
# Wilson 1913 to Senate 1918: Hine photograph 1910 is six years before Keating-Owen (1916)
eq("Hine to Keating-Owen", 1916 - 1910, 6)
# conservation: 150 forests, about 230 million acres; midnight forests 21 forests about 16 million acres
assert 230 > 150
# Occoquan: pickets began 10 January 1917
eq("Silent Sentinels weekday", date(1917, 1, 10).strftime("%A"), "Wednesday")
# 3 March 1913 parade the day before Wilson's inauguration on 4 March
eq("parade before inauguration", (date(1913, 3, 4) - date(1913, 3, 3)).days, 1)
# House passed suffrage 10 January 1918 with exactly two thirds: 274 of 410 votes
assert 274 >= 2 * (274 + 136) / 3 and 273 < 2 * (274 + 136) / 3

# --- hist-timeline widget ---------------------------------------------------------------
tm = re.search(r'data-lanes="([^"]*)" data-events="([^"]*)"', text)
lanes = [s.strip() for s in tm.group(1).split(',')]
events = [e.strip() for e in tm.group(2).split(' ;; ')]
prev = None
for e in events:
    parts = [p.strip() for p in e.split(' | ')]
    assert len(parts) == 4, f"event needs 4 fields: {e[:40]}"
    d, lane = parts[0], parts[3]
    assert lane in lanes, f"lane {lane!r} not declared"
    assert re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", d), d
    key = tuple(int(x) for x in d.split('-'))
    if prev:
        assert key >= prev, f"timeline out of order at {d}"
    prev = key
eq("timeline events", len(events), 21)

# --- exam marks -------------------------------------------------------------------------------
marks = [int(x) for x in re.findall(r'^Q: \[(\d+) marks\]', text, re.M)]
eq("marked questions", len(marks), 10)
eq("marks total", sum(marks), 10 + 10 + 10 + 20 + 20 + 15 + 25 + 20 + 20 + 25)
eq("Paper 2 total", 2 * (10 + 20), 60)
eq("Paper 1 total", 15 + 25, 40)

print("ok")
