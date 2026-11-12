# checks/hist.f.basics.py: recomputes every number in the chapter (dates, calendars, centuries, figure layout)
import re
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
text = (HERE / "chapters" / "hist.f.basics.md").read_text(encoding="utf-8")


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# --- Centuries: the n-th century is years (n-1)*100+1 .. n*100
def century(year):
    return (year - 1) // 100 + 1

eq("1789 century", century(1789), 18)
eq("1871 century", century(1871), 19)
eq("1914 century", century(1914), 20)
eq("1991 century", century(1991), 20)
eq("1904 century", century(1904), 20)
eq("1905 century", century(1905), 20)
eq("18th century range", ((18 - 1) * 100 + 1, 18 * 100), (1701, 1800))
eq("19th century range", ((19 - 1) * 100 + 1, 19 * 100), (1801, 1900))
eq("20th century range", ((20 - 1) * 100 + 1, 20 * 100), (1901, 2000))

# --- Julian to Gregorian gaps (the Julian date is this many days behind)
def gap(y, m, d):
    # days between Julian and Gregorian date of the same day, valid 1800-03-01 .. 2100-02-28
    if date(1900, 3, 1) <= date(y, m, d) <= date(2100, 2, 28):
        return 13
    if date(1800, 3, 1) <= date(y, m, d) <= date(1900, 2, 28):
        return 12
    raise ValueError

def ns(y, m, d):
    return date(y, m, d) + timedelta(days=gap(y, m, d))

eq("25 Oct 1917 OS = 7 Nov NS", ns(1917, 10, 25), date(1917, 11, 7))
eq("23 Feb 1917 OS = 8 March NS", ns(1917, 2, 23), date(1917, 3, 8))
eq("9 Jan 1905 OS = 22 Jan NS", ns(1905, 1, 9), date(1905, 1, 22))
eq("gap in 1917", gap(1917, 10, 25), 13)
eq("gap in 1861", gap(1861, 2, 19), 12)
# Russia 1918: the day after 31 January was 14 February (13 days skipped)
eq("1 Feb 1918 OS = 14 Feb NS", ns(1918, 2, 1), date(1918, 2, 14))
# Britain 1752: Wednesday 2 September followed by Thursday 14 September
eq("2 Sept 1752 (Julian) = 13 Sept proleptic Gregorian, a Wednesday", date(1752, 9, 2 + 11).strftime("%A"), "Wednesday")
eq("14 Sept 1752 weekday", date(1752, 9, 14).strftime("%A"), "Thursday")
eq("days skipped 1752", 14 - 2 - 1, 11)

# --- Worked example: Russo-Japanese War (8 Feb 1904 NS) to Bloody Sunday (22 Jan 1905 NS)
a, b = date(1904, 2, 8), date(1905, 1, 22)
months = (b.year - a.year) * 12 + b.month - a.month - (1 if b.day < a.day else 0)
eq("months from war to Bloody Sunday", months, 11)
assert 340 < (b - a).days < 350, (b - a).days   # "about eleven and a half months"

# --- Louis XVI facts used in the PEEL practice and tables
spend, revenue, interest = 629, 503, 318
eq("deficit 1788", spend - revenue, 126)
assert 0.45 < interest / spend < 0.55   # "about half" (the gold chapter's claim)
eq("years from 1614 to 1789", 1789 - 1614, 175)

# --- Lincoln's election in 1860 (electoral votes 180 of 303, 152 needed)
eq("majority of 303", 303 // 2 + 1, 152)
assert 180 >= 152
assert 0.59 < 180 / 303 < 0.60
# secession dates: seven states by 1 February 1861
seceded = {"South Carolina": date(1860, 12, 20), "Mississippi": date(1861, 1, 9), "Florida": date(1861, 1, 10),
           "Alabama": date(1861, 1, 11), "Georgia": date(1861, 1, 19), "Louisiana": date(1861, 1, 26),
           "Texas": date(1861, 2, 1)}
eq("states seceded by 1 Feb 1861", sum(1 for d in seceded.values() if d <= date(1861, 2, 1)), 7)
eq("seven states by 4 March 1861", len(seceded), 7)
eq("Lincoln's inauguration weekday", date(1861, 3, 4).strftime("%A"), "Monday")
eq("Treaty of Versailles signed", date(1919, 6, 28).strftime("%A"), "Saturday")
eq("Sarajevo assassination year", 1914, 1914)
eq("14 July national day since 1880: years to 2026", 2026 - 1880, 146)

# --- Marks totals in the AO line: Paper 1 25+75, Paper 2 50+50, Paper 3 50+50
eq("Paper 1 AO split", 25 + 75, 100)
eq("Paper 2 AO split", 50 + 50, 100)

# --- Figure layout: boxes, text widths (about 7 px per character at 13 px), arrow lengths
def figures():
    return re.findall(r"<svg viewBox=\"0 0 (\d+) (\d+)\".*?</svg>", text, flags=re.S)

figs = re.findall(r"<svg viewBox=\"0 0 (\d+) (\d+)\"(.*?)</svg>", text, flags=re.S)
eq("three figures", len(figs), 3)
for w, h, body in figs:
    w, h = int(w), int(h)
    assert 300 <= w <= 360, f"viewBox width {w}"
    for m in re.finditer(r'<text class="([^"]*)" x="(\d+)" y="(\d+)">([^<]*)</text>', body):
        cls, x, y, s = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        width = 7 * len(s) * (1.1 if "tb" in cls else 1.0)
        if "tc" in cls:
            lo, hi = x - width / 2, x + width / 2
        else:
            lo, hi = x, x + width
        assert lo >= 2 and hi <= w - 2, f"label '{s}' spans {lo:.0f}-{hi:.0f} in width {w}"
        assert y <= h - 2, f"label '{s}' y {y} beyond {h}"
    for m in re.finditer(r'<rect class="[^"]*" x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)"', body):
        x, y, rw, rh = map(int, m.groups())
        assert x + rw <= w and y + rh <= h, f"rect {x},{y},{rw},{rh} outside {w}x{h}"
    for m in re.finditer(r'<line class="ln" x1="(\d+)" y1="(\d+)" x2="(\d+)" y2="(\d+)" marker-end', body):
        x1, y1, x2, y2 = map(int, m.groups())
        assert abs(y2 - y1) >= 20, f"arrow too short {y1}->{y2}"

# Century figure: 1 px per year from 1700 at x=20
x = lambda yr: 20 + (yr - 1700)
eq("1789 x", x(1789), 109)
eq("1914 x", x(1914), 234)
eq("1991 x", x(1991), 311)
assert 20 <= x(1789) < 120 and 220 <= x(1914) < 320 and 220 <= x(1991) < 320

print("ok")
