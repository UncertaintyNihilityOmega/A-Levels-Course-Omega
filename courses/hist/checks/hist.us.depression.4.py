# checks/hist.us.depression.4.py: recomputes every number in the chapter (election, unemployment, dates, court votes, marks, figure layout)
import re
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"


# Election of 1936
eq("electoral votes in the college", 523 + 8, 531)
near("Roosevelt share of the college", 100 * 523 / 531, 98.5, 0.05)
eq("states won by Roosevelt", 48 - 2, 46)  # all but Maine and Vermont
near("popular vote shares", 60.8 + 36.5 + 2.0, 99.3, 0.05)  # remaining 0.7 per cent: minor parties
assert 27.7 > 16.7 > 0.89
near("Roosevelt's popular-vote lead in millions", 27.7 - 16.7, 11.0, 1e-9)
eq("Literary Digest replies in millions rounded", round(2.38, 1), 2.4)
near("Literary Digest response rate", 100 * 2.38 / 10, 23.8, 0.05)
eq("1932 electoral votes", 472 + 59, 531)
near("Midterm 1934 Democratic share, house, seats gained", 9 + 9, 18, 0)

# Unemployment (Margo 1993, Table 1; Lebergott and Darby)
leb = {1929: 3.2, 1930: 8.7, 1931: 15.9, 1932: 23.6, 1933: 24.9, 1934: 21.7, 1935: 20.1, 1936: 16.9, 1937: 14.3, 1938: 19.0, 1939: 17.2, 1940: 14.6, 1941: 9.9}
dar = {1929: 3.2, 1930: 8.7, 1931: 15.3, 1932: 22.9, 1933: 20.6, 1934: 16.0, 1935: 14.2, 1936: 9.9, 1937: 9.1, 1938: 12.5, 1939: 11.3, 1940: 9.5}
near("Lebergott fall 1933-36", leb[1933] - leb[1936], 8.0, 1e-9)
near("Lebergott rise 1937-38", leb[1938] - leb[1937], 4.7, 1e-9)
near("Darby rise 1937-38", dar[1938] - dar[1937], 3.4, 1e-9)
near("Lebergott fall 1933-37", leb[1933] - leb[1937], 10.6, 1e-9)  # "about ten percentage points" by 1937
near("Darby fall 1933-37", dar[1933] - dar[1937], 11.5, 1e-9)
assert leb[1940] == 14.6 and dar[1940] == 9.5 and leb[1941] < 10 and leb[1940] > 10
assert max(leb.values()) == leb[1933] and max(dar.values()) == dar[1932]
assert all(dar[y] <= leb[y] for y in dar)
assert leb[1938] > leb[1937] and leb[1939] < leb[1938]
near("Lebergott 1940 against 1933 fall", leb[1933] - leb[1940], 10.3, 1e-9)
assert leb[1935] == 20.1  # "unemployment was still 20.1 per cent in 1935"

# Court plan and appointments
eq("court after the plan", 9 + 6, 15)
eq("days from plan to West Coast Hotel", (date(1937, 3, 29) - date(1937, 2, 5)).days, 52)
near("weeks from plan to Parrish", 52 / 7, 7.4, 0.05)  # "seven weeks", "within eight weeks"
assert 52 / 7 < 8
eq("days from plan to Robinson's death", (date(1937, 7, 14) - date(1937, 2, 5)).days, 159)
eq("Senate recommittal vote", 70 + 20, 90)
near("recommittal majority", 100 * 70 / 90, 77.8, 0.05)
eq("Judiciary report signatories", 7 + 3, 10)
eq("appointments by 1940", len(["Black", "Reed", "Frankfurter", "Douglas", "Murphy"]), 5)
eq("days from plan to Jones & Laughlin", (date(1937, 4, 12) - date(1937, 2, 5)).days, 66)
eq("Parrish vote", 5 + 4, 9)

# Ages of justices on 5 Feb 1937
births = {
    "Brandeis": date(1856, 11, 13), "Van Devanter": date(1859, 4, 17), "McReynolds": date(1862, 2, 3),
    "Sutherland": date(1862, 3, 25), "Hughes": date(1862, 4, 11), "Butler": date(1866, 3, 17),
    "Cardozo": date(1870, 5, 24), "Stone": date(1872, 10, 11), "Roberts": date(1875, 5, 2),
}


def age_on(b, d):
    return d.year - b.year - ((d.month, d.day) < (b.month, b.day))


eq("six justices seventy or older", len([n for n, b in births.items() if age_on(b, date(1937, 2, 5)) >= 70]), 6)

# Dates and intervals
eq("Flint sit-down strike length (days)", (date(1937, 2, 11) - date(1936, 12, 30)).days, 43)
eq("Social Security Act to first payroll tax (months)", (1937 - 1935) * 12 + (1 - 8), 17)
eq("benefits brought forward (years)", 1942 - 1940, 2)
eq("Schechter to Wagner Act (days)", (date(1935, 7, 5) - date(1935, 5, 27)).days, 39)
eq("Wagner Act to Social Security (days)", (date(1935, 8, 14) - date(1935, 7, 5)).days, 40)
eq("Long shot to death", (date(1935, 9, 10) - date(1935, 9, 8)).days, 2)
eq("weekday of 5 July 1935 (Friday=4)", date(1935, 7, 5).weekday(), 4)
eq("weekday of Black Sunday, 14 April 1935 (Sunday=6)", date(1935, 4, 14).weekday(), 6)
eq("weekday of Madison Square Garden speech (Saturday=5)", date(1936, 10, 31).weekday(), 5)
eq("recession length May 1937 to June 1938 (months)", (1938 - 1937) * 12 + (6 - 5), 13)
eq("Parrish to Jones & Laughlin (days)", (date(1937, 4, 12) - date(1937, 3, 29)).days, 14)

# Fair Labor Standards Act and Social Security rates
eq("minimum wage first, cents", 25, 25)
assert 40 > 25 and 44 > 40
near("minimum wage rise to 40c, per cent", 100 * (40 - 25) / 25, 60.0, 1e-9)
eq("payroll tax rate each side 1937 (per cent)", 1, 1)
eq("tax on a worker earning $3,000 (one side)", 3000 * 0.01, 30)

# Houston: sharecroppers
eq("Houston's figure", 490_000, 490000)

# Federal share of output (inputs from Historical Statistics / OMB tables, $ billion)
near("1929 federal outlays share of GDP", 100 * 3.1 / 104.6, 3.0, 0.05)
near("1940 federal outlays share of GDP", 100 * 9.5 / 101.4, 9.4, 0.05)
assert 9.1 < 13.7 < 35.1  # outlays 1939, 1941, 1942: about $9bn, $14bn, over $30bn

# Mark totals and level spans
eq("P2(a) top span", 10 - 9 + 1, 2)
eq("P2(b) level 5 span", 20 - 17 + 1, 4)
eq("P1(a) level 4 span", 15 - 12 + 1, 4)
eq("P1(b) level 5 span", 25 - 21 + 1, 5)
eq("paper 1 marks", 15 + 25, 40)

# Figure layout: every <text> in each SVG sits inside its smallest enclosing <rect>
src = open("chapters/hist.us.depression.4.md", encoding="utf-8").read()
svgs = re.findall(r"<svg.*?</svg>", src, re.S)
eq("number of svgs", len(svgs), 1)
for k, svg in enumerate(svgs):
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    rects = [tuple(float(m) for m in r) for r in re.findall(r'<rect[^>]*x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg)]
    for cls, x, y, txt in re.findall(r'<text class="([^"]+)" x="([\d.]+)" y="([\d.]+)">([^<]*)</text>', svg):
        x, y = float(x), float(y)
        w = len(txt) * (7.6 if "tb" in cls.split() else 7.0)
        inside = [r for r in rects if r[0] <= x <= r[0] + r[2] and r[1] <= y - 10 and y <= r[1] + r[3]]
        assert inside, f"svg {k}: text '{txt}' at ({x},{y}) is in no box"
        r = min(inside, key=lambda t: t[2] * t[3])
        assert x - w / 2 >= r[0] + 4 and x + w / 2 <= r[0] + r[2] - 4, f"svg {k}: text '{txt}' ({w:.0f}px) too wide for its box {r}"
    for r in rects:
        assert r[0] + r[2] <= vb[2] and r[1] + r[3] <= vb[3], f"svg {k}: box {r} outside viewBox {vb}"
print("ok")
