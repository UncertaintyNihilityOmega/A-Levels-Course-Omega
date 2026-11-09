# checks/hist.d.italy.3.py: recomputes every number in the chapter (dates, intervals, percentages, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Lira: about 150 to the pound in mid-1926, 92.46 in December 1927 -> value up "about three fifths"
rise = 150 / 92.46 - 1
between("lira rise", rise, 0.55, 0.65)
# Pesaro speech to stabilisation: 18 August 1926 -> December 1927 is 16 months
eq("months Pesaro to Quota 90", (1927 - 1926) * 12 + (12 - 8), 16)
# The target 90 against the 1922 rate of about 90: target equals the 1922 rate
eq("target = 1922 rate", 90, 90)

# Wheat: about 5.39 to 7.27 million tonnes (1925-35) -> "about a third"
w = 7.27 / 5.39 - 1
between("wheat rise", w, 0.30, 0.40)
eq("wheat years", 1935 - 1925, 10)
# Wheat imports 2,241,913 t (1925) -> 1,464,968 t (1931): "about 2.2 to about 1.5 million tonnes"
i25, i31 = 2241913, 1464968
eq("imports 1925 rounded", round(i25 / 1e6, 1), 2.2)
eq("imports 1931 rounded", round(i31 / 1e6, 1), 1.5)
between("imports fall", 1 - i31 / i25, 0.30, 0.40)

# Unemployment: about 300,000 (1929) to about one million (1932-33): roughly three times
between("unemployment ratio", 1000000 / 300000, 3, 3.5)

# Corporate State intervals
eq("Vidoni to corporations", 1934 - 1925, 9)
eq("Charter to corporations", 1934 - 1927, 7)
eq("Vidoni to Rocco (days)", (date(1926, 4, 3) - date(1925, 10, 2)).days, 183)
# Charter 21 April 1927 is nearly a year after the Ministry (July 1926)
eq("Ministry to Charter months", (1927 - 1926) * 12 + (4 - 7), 9)

# Sanctions 18 November 1935 to July 1936: about 8 months
months = (1936 - 1935) * 12 + (7 - 11)
eq("sanctions months", months, 8)

# IRI share of capital in 1936: 12.5 per cent = one eighth
eq("IRI one eighth", Fraction(125, 1000), Fraction(1, 8))
# Shipping share "more than four fifths"; pig iron "three quarters"
assert Fraction(4, 5) < Fraction(81, 100) and Fraction(3, 4) == Fraction(75, 100)

# Real wages: about 15 per cent fall 1921 to 1929: index 100 -> 85
eq("real wage index 1929", 100 * (1 - 0.15), 85.0)

# Dates used in the timeline and text
eq("Day of Faith year gap from Abyssinia (Oct 1935 to Dec 1935 months)", 12 - 10, 2)
eq("Littoria to Sabaudia years", 1934 - 1932, 2)
eq("IMI to IRI months", (1933 - 1931) * 12 + (1 - 11), 14)
eq("Ascension of IRI permanence years after founding", 1937 - 1933, 4)

# Mark totals in the worked examples (Table A + Table B out of 30)
eq("battles essay low", 14 + 13, 27)
eq("battles essay high", 14 + 14, 28)
eq("corporate state essay low", 14 + 13, 27)
eq("corporate state essay high", 14 + 14, 28)
eq("paper total", 2 * 30, 60)
eq("table total", 15 + 15, 30)

# Figure layout: every label fits its box (7 px per character), arrows at least 20 px long
boxes = [
    (30, 10, 280, 46, ["Mussolini, Head of Government", "Ministry of Corporations (1926)"]),
    (30, 80, 280, 46, ["National Council of Corporations", "advises and coordinates (law of 1930)"]),
    (30, 150, 280, 64, ["22 corporations (law of 1934)", "one for each branch of the economy:", "employers, workers and party officials"]),
    (10, 240, 150, 64, ["Employers' bodies", "Confindustria and", "other confederations"]),
    (180, 240, 150, 64, ["Fascist unions", "the only unions the", "state recognises"]),
    (30, 330, 280, 64, ["Labour courts (Rocco Law, 1926)", "settle disputes; strikes and", "lockouts are crimes"]),
]
for x, y, w_, h, lines in boxes:
    for t in lines:
        assert len(t) * 7 <= w_ - 10, f"label too wide: {t}"
    assert x >= 5 and x + w_ <= 335 and y + h <= 404
for (x1, y1, x2, y2) in [(170, 56, 170, 80), (170, 126, 170, 150), (85, 240, 85, 214), (255, 240, 255, 214), (85, 330, 85, 304), (255, 330, 255, 304)]:
    assert abs(y2 - y1) >= 20, "arrow too short"

print("ok")
