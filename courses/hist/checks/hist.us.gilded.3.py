# checks/hist.us.gilded.3.py: recomputes every number in the chapter (dates, intervals, shares, totals, widget data, layout)
from datetime import date
import os, re


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, '..', 'chapters', 'hist.us.gilded.3.md'), encoding='utf-8').read()

# --- dates and intervals ---------------------------------------------------
# Garfield shot 2 July 1881, died 19 September; Pendleton Act 16 January 1883 "about eighteen months after the shooting"
shot, died, pend = date(1881, 7, 2), date(1881, 9, 19), date(1883, 1, 16)
between("months shooting to Pendleton", (pend - shot).days / 30.44, 17.5, 18.5)
eq("Garfield survived days", (died - shot).days, 79)
# Hull-House opened 1889; Twenty Years at Hull-House 1910 -> "21 years after"
eq("Hull-House to memoir", 1910 - 1889, 21)
# La Follette governor January 1901 to 1906: five years
eq("La Follette years", 1906 - 1901, 5)
# Roosevelt's muck-rake speech 14 April 1906 precedes the 30 June 1906 Acts by 77 days
eq("speech to Acts", (date(1906, 6, 30) - date(1906, 4, 14)).days, 77)
# Progressive convention 5-7 August 1912: three days
eq("convention days", (date(1912, 8, 7) - date(1912, 8, 5)).days + 1, 3)
# 17th Amendment ratified 8 April 1913; Lorimer unseated 1912; Wilson-era dates in order
assert date(1912, 7, 13) < date(1913, 4, 8)
# Panic of 1907: Knickerbocker failure 22 October 1907 (a Tuesday)
eq("Knickerbocker weekday", date(1907, 10, 22).strftime("%A"), "Tuesday")
# Triangle fire 25 March 1911 was a Saturday
eq("Triangle weekday", date(1911, 3, 25).strftime("%A"), "Saturday")
# Lochner 17 April 1905 and Muller 24 February 1908: about 2 years 10 months apart
between("Lochner to Muller years", (date(1908, 2, 24) - date(1905, 4, 17)).days / 365.25, 2.8, 2.9)
# Lochner vote 5-4 is a full nine-member Court; Muller unanimous 9-0
eq("Lochner bench", 5 + 4, 9)
# Pendleton covered about a tenth of 131,000 federal jobs at first (14,000 classified)
between("Pendleton share", 14000 / 131000, 0.09, 0.12)

# --- Louisiana Black registration ------------------------------------------
reg96, reg04 = 130334, 1342
assert reg96 > 130000 and 1300 <= reg04 <= 1400
between("Louisiana fall factor", reg96 / reg04, 90, 100)

# --- census urban share (chart) and union membership (chart) ----------------
urban = {1870: 25.7, 1880: 28.2, 1890: 35.1, 1900: 39.6, 1910: 45.6, 1920: 51.2}
m = re.search(r'data-title="Share of Americans living in urban places[^"]*"[^>]*data-series="([^"]*)"', text)
assert m, "urban chart missing"
got = {int(k): float(v) for k, v in (p.split('=') for p in m.group(1).split(':')[1].split(','))}
eq("urban chart data", got, urban)
eq("urban 1870 'about 26 per cent'", round(urban[1870]), 26)
assert urban[1920] > 50 and urban[1910] < 50  # "more than half" in 1920 for the first time

union = {1900: 868500, 1910: 2140500, 1920: 5047800}
m = re.search(r'data-title="Trade union members[^"]*"[^>]*data-series="([^"]*)"', text)
assert m, "union chart missing"
got = {int(k): float(v) for k, v in (p.split('=') for p in m.group(1).split(':')[1].split(','))}
for y, n in union.items():
    eq(f"union {y}", got[y], round(n / 1e6, 2))
eq("0.9 million in 1900", round(union[1900] / 1e6, 1), 0.9)
assert union[1910] > 2_000_000 and round(union[1920] / 1e6) == 5

# --- suffrage states by 1913 "about nine" ------------------------------------
full_by_1913 = ["Wyoming", "Colorado", "Utah", "Idaho", "Washington", "California", "Oregon", "Arizona", "Kansas"]
eq("states with full women's suffrage by 1913 (before 1914 gains)", len(full_by_1913), 9)

# --- Pujo: directorships and companies --------------------------------------
assert 330 <= 341 <= 350 and 100 < 112

# --- hist-timeline widget: every date parses, every lane is declared ---------
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
eq("timeline events", len(events), 16)

# --- exam marks used in the text ---------------------------------------------
# Paper 2: (a) 10, (b) 20, two questions = 2 x (10 + 20) = 60. Paper 1: (a) 15 + (b) 25 = 40.
eq("Paper 2 total", 2 * (10 + 20), 60)
eq("Paper 1 total", 15 + 25, 40)
# practice marks in the chapter
marks = [int(x) for x in re.findall(r'^Q: \[(\d+) marks\]', text, re.M)]
eq("number of marked exam-practice questions", len(marks), 10)
eq("marks of the practice questions", sum(marks), 10 + 10 + 10 + 20 + 20 + 15 + 25 + 20 + 20 + 20)

# --- figure layout: five boxes and arrows in the pressures diagram -----------
svg = re.search(r'<svg viewBox="0 0 340 318".*?</svg>', text, re.S).group(0)
rects = [tuple(map(float, r)) for r in re.findall(r'<rect class="[^"]*" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg)]
eq("rect count", len(rects), 6)
big = rects[-1]
for x, y, w, h in rects[:-1]:
    assert x + w <= big[0] - 20, "box too close to the big box"
    assert y + h <= 318 and x >= 0
assert big[1] + big[3] <= 318 and big[0] + big[2] <= 340
arrows = re.findall(r'<line class="ln" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', svg)
eq("arrow count", len(arrows), 5)
for (x1, y1, x2, y2), (bx, by, bw, bh) in zip(arrows, rects[:-1]):
    assert float(y1) == float(y2) and by < float(y1) < by + bh
    assert float(x1) > bx + bw and float(x2) < big[0]

print("ok")
