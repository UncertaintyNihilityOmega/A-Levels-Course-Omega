# checks/hist.eu.germany.1.py: recomputes every number in the chapter (dates, intervals, shares, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Confederation: 35 monarchies + 4 free cities = 39 states
eq("states", 35 + 4, 39)
# 1815 -> 1848: "thirty-three years later"
eq("1815 to 1848", 1848 - 1815, 33)
# Wartburg 18 October 1817 = 4 years after Leipzig (October 1813); 300 years after Luther (1517)
eq("Leipzig anniversary", 1817 - 1813, 4)
eq("Luther anniversary", 1817 - 1517, 300)
# Kotzebue murdered 23 March 1819; Decrees 20 September 1819 (about six months)
d = (date(1819, 9, 20) - date(1819, 3, 23)).days
assert 170 <= d <= 190, d
# Wartburg to Carlsbad: two years
eq("Wartburg to Decrees", 1819 - 1817, 2)
# Press Law first five years, made permanent 1824: five years from 1819 is 1824
eq("press law term", 1819 + 5, 1824)
# Twenty sheets of 16 pages = 320 pages
eq("twenty sheets", 20 * 16, 320)
# Hambach 27 May 1832; Six Articles 28 June; Ten Articles 5 July
assert date(1832, 5, 27) < date(1832, 6, 28) < date(1832, 7, 5)
eq("Ten Articles after Six", (date(1832, 7, 5) - date(1832, 6, 28)).days, 7)
# Zollverein 1 January 1834, customs law 1818: 16 years; Nuremberg-Furth 7 December 1835
eq("1818 to 1834", 1834 - 1818, 16)
# Railways: km totals and growth
rail = {1835: 6, 1840: 500, 1845: 2100, 1850: 6000}
assert rail[1835] < rail[1840] < rail[1845] < rail[1850]
# "about 6,000 km by 1850": 1000 times the 1835 line
eq("rail 1850 / 1835", rail[1850] // rail[1835], 1000)
# Population 25m -> 35m: "about 40 per cent"
growth = Fraction(35, 25) - 1
eq("population growth", growth, Fraction(2, 5))
# Berlin 170,000 -> 420,000: "more than twice"
assert Fraction(420000, 170000) > 2
# Silesian revolt 4-6 June 1844; troops fired 5 June; "crushed within three days"
eq("revolt days", (date(1844, 6, 6) - date(1844, 6, 4)).days + 1, 3)
# Heine's poem 10 July 1844, "a month later" (about 36 days after 4 June)
d = (date(1844, 7, 10) - date(1844, 6, 4)).days
assert 28 <= d <= 40, d
# United Diet 11 April - 26 June 1847; Potato Revolution 21-23 April; Offenburg 12 Sept; Heppenheim 10 Oct
assert date(1847, 4, 11) < date(1847, 4, 21) < date(1847, 6, 26) < date(1847, 9, 12) < date(1847, 10, 10)
eq("Offenburg to Heppenheim: a month", (date(1847, 10, 10) - date(1847, 9, 12)).days, 28)
# Paris 24 February 1848; Metternich 13 March: 18 days
eq("Paris to Vienna", (date(1848, 3, 13) - date(1848, 2, 24)).days, 18)
# Prussian decree 22 May 1815 is 27 days before Waterloo (18 June 1815): "about a month"
eq("decree before Waterloo", (date(1815, 6, 18) - date(1815, 5, 22)).days, 27)
# Frederick William IV accession 7 June 1840; Rhine crisis 1840; Song 26 August 1841
assert date(1840, 6, 7) < date(1841, 8, 26)
# Hoffmann dismissed 1842, a year after the song
eq("song to dismissal", 1842 - 1841, 1)
# Austria: about 8 million Germans of about 36 million is roughly a quarter or less (used in chapter 2)
assert Fraction(8, 36) < Fraction(1, 4)

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25

# Figure layout (viewBox 340 x 322): boxes inside the frame, labels fit with 4 px margin, 7 px a character
frame = (6, 6, 328, 310)
boxes = {
    "austria": (16, 58, 148, 92),
    "prussia": (176, 58, 148, 92),
    "third": (16, 162, 308, 102),
}
for n, (x, y, w, h) in boxes.items():
    assert x >= frame[0] + 4 and x + w <= frame[0] + frame[2] - 4, n
    assert y + h <= frame[1] + frame[3] - 4, n
# Austria and Prussia do not overlap, and Third Germany is below both
assert boxes["austria"][0] + boxes["austria"][2] < boxes["prussia"][0]
assert boxes["austria"][1] + boxes["austria"][3] < boxes["third"][1]
labels = {
    "austria": ["Austria", "German lands only", "Chairs the Diet", "No Zollverein"],
    "prussia": ["Prussia", "Gained the Rhineland", "and Westphalia, 1815", "Zollverein leader"],
    "third": ["The Third Germany", "Bavaria, Saxony, Hanover, Württemberg,", "Baden, Hesse and about 30 smaller", "states and four free cities", "Most in the Zollverein by 1836"],
}
for n, ls in labels.items():
    w = boxes[n][2]
    for s in ls:
        assert len(s) * 7 <= w - 8, (n, s, len(s) * 7, w - 8)
# line spacing 18 px, last label baseline inside box
assert 132 + 4 < 58 + 92 and 254 + 4 < 162 + 102
# title texts inside frame: widths
assert len("German Confederation, 1815") * 7 <= 328 - 8
# legend labels fit beside swatches
assert 46 + len("In the Zollverein") * 7 < 188 and 212 + len("Outside it") * 7 < 334
print("ok")
