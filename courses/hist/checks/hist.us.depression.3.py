# checks/hist.us.depression.3.py: recomputes every number in the chapter (dates, intervals, percentages, marks, court ages, figure layout)
import re
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"


# The First Hundred Days (9 March to 16 June 1933)
eq("hundred days length", (date(1933, 6, 16) - date(1933, 3, 9)).days, 99)
eq("Michigan holiday to national holiday", (date(1933, 3, 6) - date(1933, 2, 14)).days, 20)
eq("bank holiday to reopening", (date(1933, 3, 13) - date(1933, 3, 6)).days, 7)
eq("inauguration to bank holiday", (date(1933, 3, 6) - date(1933, 3, 4)).days, 2)
eq("weekday of the 6 March proclamation (Monday=0)", date(1933, 3, 6).weekday(), 0)
eq("weekday of the first fireside chat (Sunday=6)", date(1933, 3, 12).weekday(), 6)
eq("weekday of Schechter (Monday=0)", date(1935, 5, 27).weekday(), 0)
eq("weekday of the 4 March inauguration (Saturday=5)", date(1933, 3, 4).weekday(), 5)
eq("Long shot to death", (date(1935, 9, 10) - date(1935, 9, 8)).days, 2)
eq("Zangara to Cermak death", (date(1933, 3, 6) - date(1933, 2, 15)).days, 19)

# Economy Act: $500 million off a budget of about $3.6 billion
near("Economy Act share of budget", 100 * 500 / 3600, 13.9, 0.05)  # "about 14 per cent"

# Gold: $20.67 to $35 an ounce
near("dollar gold content", 100 * 20.67 / 35, 59.06, 0.01)  # "about 59 per cent"

# CCC pay
eq("CCC pay kept", 30 - 25, 5)

# Unemployment (Margo 1993, Table 1)
leb = {1933: 24.9, 1934: 21.7, 1935: 20.1, 1936: 16.9, 1937: 14.3}
dar = {1933: 20.6, 1934: 16.0, 1935: 14.2, 1936: 9.9}
near("Lebergott fall 1933-35", leb[1933] - leb[1935], 4.8, 1e-9)  # Source D in the Paper 1 (b) example
near("Lebergott fall 1933-36", leb[1933] - leb[1936], 8.0, 1e-9)
near("Darby fall 1933-36", dar[1933] - dar[1936], 10.7, 1e-9)
assert leb[1937] == 14.3 and leb[1935] == 20.1 and dar[1935] == 14.2
assert all(dar[y] < leb[y] for y in dar)

# Long's Share Our Wealth: capital levy schedule (1% on 2nd million, doubling each million)
tax = 0
rate = 0.01
for million in range(2, 6):  # a $5 million fortune pays on millions 2 to 5
    tax += 1_000_000 * rate
    rate *= 2
eq("tax on a $5 million fortune under the 1935 schedule", tax, 150_000)  # 10k + 20k + 40k + 80k
eq("tax on the second million", 1_000_000 * 0.01, 10_000)

# Supreme Court ages in February 1937 (birth dates) and the plan of 5 February 1937
births = {
    "Brandeis": date(1856, 11, 13), "Van Devanter": date(1859, 4, 17), "McReynolds": date(1862, 2, 3),
    "Sutherland": date(1862, 3, 25), "Hughes": date(1862, 4, 11), "Butler": date(1866, 3, 17),
    "Cardozo": date(1870, 5, 24), "Stone": date(1872, 10, 11), "Roberts": date(1875, 5, 2),
}
eq("nine justices", len(births), 9)


def age_on(b, d):
    return d.year - b.year - ((d.month, d.day) < (b.month, b.day))


plan = date(1937, 2, 5)
over70 = [n for n, b in births.items() if age_on(b, plan) >= 70]
eq("justices 70 or older on 5 Feb 1937", len(over70), 6)  # "Six of the nine"
june = date(1937, 6, 1)
over75 = [n for n, b in births.items() if age_on(b, june) >= 75]
eq("justices 75 or older by June 1937", len(over75), 5)  # Roosevelt: "five ... over seventy-five before next June"
eq("seventy to seventy-five", len([n for n in over70 if n not in over75]), 1)
eq("court after plan", 9 + 6, 15)
eq("days from plan to West Coast Hotel", (date(1937, 3, 29) - plan).days, 52)
eq("four horsemen", len(["Van Devanter", "McReynolds", "Sutherland", "Butler"]), 4)
eq("votes needed: horsemen + 1 swing", 4 + 1, 5)
eq("appointments by 1940", len(["Black", "Reed", "Frankfurter", "Douglas", "Murphy"]), 5)

# Congress after 1934: Republicans about a quarter
near("Republican share of the House", 100 * 103 / 435, 23.7, 0.05)
near("Republican share of the Senate", 100 * 25 / 96, 26.0, 0.05)

# Mark totals of the worked examples and level ranges
eq("P2(a) top level span", 10 - 9 + 1, 2)
eq("P2(b) level 5 span", 20 - 17 + 1, 4)
eq("P1(a) level 4 span", 15 - 12 + 1, 4)
eq("P1(b) level 5 span", 25 - 21 + 1, 5)
eq("paper marks", 15 + 25, 40)
eq("paper 2 marks", 2 * (10 + 20), 60)

# Figure layout: every <text> in each SVG sits inside its smallest enclosing <rect>
src = open("chapters/hist.us.depression.3.md", encoding="utf-8").read()
svgs = re.findall(r"<svg.*?</svg>", src, re.S)
eq("number of svgs", len(svgs), 2)
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
        assert 0 <= x - w / 2 and x + w / 2 <= vb[2], f"svg {k}: '{txt}' outside the viewBox"
    for r in rects:
        assert r[0] + r[2] <= vb[2] and r[1] + r[3] <= vb[3], f"svg {k}: box {r} outside viewBox {vb}"
print("ok")
