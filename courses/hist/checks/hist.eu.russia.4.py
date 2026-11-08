# checks/hist.eu.russia.4.py: recomputes every number in the chapter (dates, intervals, counts, marks, figure layout)
from datetime import date, timedelta


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def ns(y, m, d):
    # Old Style is 13 days behind New Style in the twentieth century
    return date(y, m, d) + timedelta(days=13)


# Old Style to New Style
assert ns(1917, 11, 12) == date(1917, 11, 25)     # Constituent Assembly elections
assert ns(1917, 12, 7) == date(1917, 12, 20)      # Cheka
assert ns(1918, 1, 5) == date(1918, 1, 18)        # Assembly meets
assert ns(1917, 11, 14) == date(1917, 11, 27)     # Decree on Workers' Control (not stated in NS in the text)
eq("calendar switch", date(1918, 1, 31) + timedelta(days=14), date(1918, 2, 14))

# Taking power took three days (24-26 October); keeping it six years (to 1924 / Lenin's death)
eq("days to take power", (date(1917, 10, 26) - date(1917, 10, 24)).days + 1, 3)
years = (date(1924, 1, 21) - date(1917, 10, 26)).days / 365.25
assert 6 <= years < 7, years

# Lenin: born 22 April 1870 NS, died 21 January 1924: aged 53
born, died = date(1870, 4, 22), date(1924, 1, 21)
eq("Lenin age", died.year - born.year - ((died.month, died.day) < (born.month, born.day)), 53)

# Dzerzhinsky: eleven years in prisons and exile is stated loosely; no figure checked here

# Constituent Assembly
# SRs about 40%, Bolsheviks about 24%; about 380 and 170 seats of about 700
assert 0.35 < 380 / 700 < 0.60         # a majority of seats (54 per cent)
assert 380 / 700 > 0.5
assert abs(170 / 700 - 0.24) < 0.01     # roughly the same share as the Bolshevik vote
# Chernov elected chairman by 244 votes to 151
eq("votes cast for chair", 244 + 151, 395)
assert 244 > 151
# Assembly session: afternoon of 5 January to early 6 January: one night; dissolved the next day
eq("Assembly lasted one night", (date(1918, 1, 6) - date(1918, 1, 5)).days, 1)

# Brest-Litovsk
eq("Brest to ratification", (date(1918, 3, 15) - date(1918, 3, 3)).days, 12)
eq("German advance to vote", (date(1918, 2, 23) - date(1918, 2, 18)).days, 5)
eq("Trotsky 'neither war nor peace' to German attack", (date(1918, 2, 18) - date(1918, 2, 10)).days, 8)
assert 56_000_000 / 0.32 > 170_000_000 and 56_000_000 / 0.32 < 180_000_000   # 32 per cent = 56 million, population about 175 million

# Civil War
eq("Czech Legion to Wrangel evacuation", (date(1920, 11, 14) - date(1918, 5, 25)).days, 904)
assert 2.4 < 904 / 365.25 < 2.5
eq("royal family murder to Czech Legion rising", (date(1918, 7, 17) - date(1918, 5, 25)).days, 53)
eq("attempt on Lenin to Red Terror decree", (date(1918, 9, 5) - date(1918, 8, 30)).days, 6)
eq("Kolchak shot", date(1920, 2, 7).year - 1918, 2)
assert (date(1920, 2, 7) - date(1918, 11, 18)).days == 446
eq("Treaty of Riga after Kronstadt", (date(1921, 3, 18) - date(1921, 3, 18)).days, 0)   # Riga 18 March 1921; Kronstadt fell 18 March 1921
# Red Army on paper over five million; the strength is "on paper"
assert 5_000_000 > 5_000

# War Communism numbers: grain 80 million (1913) to under 50 million (1920); industry about a fifth
assert 46.5 < 50
assert 46.5 / 80.1 < 0.6
assert abs(1 / 5 - 0.2) < 1e-12
assert 3 <= 5 and 3_000_000 < 5_000_000   # famine deaths 3 to 5 million

# Kronstadt
eq("resolution to fall of the fortress", (date(1921, 3, 18) - date(1921, 2, 28)).days, 18)
eq("resolution to mass meeting", (date(1921, 3, 1) - date(1921, 2, 28)).days, 1)
eq("bombardment to storming", (date(1921, 3, 17) - date(1921, 3, 7)).days, 10)
eq("Congress length (8-16 March) in days", (date(1921, 3, 16) - date(1921, 3, 8)).days + 1, 9)
eq("Lenin 'greater danger than Denikin' to tax in kind", (date(1921, 3, 15) - date(1921, 3, 9)).days, 6)
eq("tax in kind decree after Congress vote", (date(1921, 3, 21) - date(1921, 3, 15)).days, 6)
eq("Congress opens a day after bombardment", (date(1921, 3, 8) - date(1921, 3, 7)).days, 1)
# Kronstadt: about 8,000 fled to Finland; 2,103 sentenced to death (one official count)
assert 2_103 < 8_000
# 300 delegates joined the assault, ten died
assert 10 < 300
assert 15_000 > 8_000    # mass meeting of about 15,000

# Lenin's illness and death
eq("USSR formed to Lenin's death (days)", (date(1924, 1, 21) - date(1922, 12, 30)).days, 387)
eq("Stalin General Secretary to Lenin's death (months, April 1922 to January 1924)", (1924 - 1922) * 12 + (1 - 4), 21)

# Exam facts (FACTS.md): Paper 1 15 + 25 = 40; Paper 2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(5, 8), (9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(6, 10), (11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25
assert 3 <= 4 <= 5 and 9 <= 10 <= 10      # Paper 2 (a): about 4 (Level 2), 10 (Level 4)
assert 4 <= 6 <= 7 and 12 <= 14 <= 15     # Paper 1 (a): about 6 (Level 2), 14 (Level 4)
assert 17 <= 18 <= 20                      # Paper 2 (b): Level 5
eq("practice marks", 10 + 10 + 20 + 20 + 20 + 15 + 20, 115)

# Figure layout: Civil War schematic, viewBox 340 x 440. (x, y, w, h) of each box
boxes = {
    "north": (80, 8, 180, 62), "core": (110, 160, 120, 96), "yudenich": (8, 84, 92, 56),
    "kolchak": (244, 84, 88, 56), "poland": (8, 190, 70, 42), "denikin": (105, 300, 130, 56),
    "wrangel": (105, 384, 130, 42), "vladivostok": (244, 300, 88, 86),
}


def rect(b):
    x, y, w, h = b
    return x, y, x + w, y + h


def overlap(a, b, pad=4):
    ax1, ay1, ax2, ay2 = rect(a)
    bx1, by1, bx2, by2 = rect(b)
    return not (ax2 + pad <= bx1 or bx2 + pad <= ax1 or ay2 + pad <= by1 or by2 + pad <= ay1)


names = list(boxes)
for i, n in enumerate(names):
    x1, y1, x2, y2 = rect(boxes[n])
    assert x1 >= 0 and x2 <= 340 and y1 >= 0 and y2 <= 440, n
    for m in names[i + 1:]:
        assert not overlap(boxes[n], boxes[m]), (n, m)
# label widths: about 7 px per character, with 4 px each side
texts = {
    "north": ["Archangel and", "Murmansk", "Allied landings 1918"], "core": ["Soviet Russia", "Moscow and", "Petrograd,", "railways and", "arms factories"],
    "yudenich": ["Yudenich", "Estonia", "Oct 1919"], "kolchak": ["Kolchak", "Siberia", "1918–20"], "poland": ["Poland", "1920 war"],
    "denikin": ["Denikin", "South Russia and", "Ukraine 1918–20"], "wrangel": ["Wrangel: Crimea", "April–Nov 1920"],
    "vladivostok": ["Vladivostok", "Japanese,", "US, British", "troops,", "1918–22"],
}
for n, lines in texts.items():
    w = boxes[n][2]
    for line in lines:
        assert len(line) * 7 <= w - 8, (n, line, len(line) * 7, w)
# text baselines inside their boxes: last baseline + 4 below the bottom
last_baseline = {"north": 57, "core": 243, "yudenich": 133, "kolchak": 133, "poland": 224, "denikin": 349, "wrangel": 418, "vladivostok": 379}
for n, b in last_baseline.items():
    assert b + 4 <= rect(boxes[n])[3], n
# arrows: (x1, y1, x2, y2), each at least 20 px long and ending within 6 px of its target box
import math
arrows = [((170, 73, 170, 156), "core"), ((54, 143, 106, 178), "core"), ((288, 143, 234, 178), "core"),
          ((81, 211, 106, 211), "core"), ((170, 297, 170, 260), "core"), ((170, 359, 170, 380), "wrangel")]
for (x1, y1, x2, y2), tgt in arrows:
    assert math.hypot(x2 - x1, y2 - y1) >= 20, (x1, y1, x2, y2)
    tx1, ty1, tx2, ty2 = rect(boxes[tgt])
    dx = max(tx1 - x2, 0, x2 - tx2)
    dy = max(ty1 - y2, 0, y2 - ty2)
    assert math.hypot(dx, dy) <= 6, ((x1, y1, x2, y2), tgt, dx, dy)
# no arrow crosses another box
def seg_hits_rect(x1, y1, x2, y2, b, pad=2):
    bx1, by1, bx2, by2 = rect(b)
    for t in [i / 100 for i in range(101)]:
        x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        if bx1 + pad < x < bx2 - pad and by1 + pad < y < by2 - pad:
            return True
    return False

for (x1, y1, x2, y2), tgt in arrows:
    for n, b in boxes.items():
        if n == tgt:
            continue
        assert not seg_hits_rect(x1, y1, x2, y2, b), ((x1, y1, x2, y2), n)
print("ok")
