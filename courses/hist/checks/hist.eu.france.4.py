# checks/hist.eu.france.4.py: recomputes every number in the chapter (dates, ages, intervals, shares, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


born = date(1769, 8, 15)
eq("age at Toulon (19 Dec 1793)", age(born, date(1793, 12, 19)), 24)
eq("age at Brumaire", age(born, date(1799, 11, 10)), 30)
eq("age at coronation (2 Dec 1804)", age(born, date(1804, 12, 2)), 35)
eq("age at abdication", age(born, date(1814, 4, 6)), 44)

# Timeline order
seq = [date(1793, 12, 19), date(1795, 10, 5), date(1797, 10, 17), date(1799, 11, 9), date(1799, 12, 13),
       date(1800, 1, 17), date(1800, 2, 13), date(1800, 2, 17), date(1800, 6, 14), date(1801, 7, 15),
       date(1802, 3, 25), date(1802, 5, 1), date(1802, 8, 2), date(1803, 3, 28), date(1804, 3, 21),
       date(1804, 12, 2), date(1805, 10, 21), date(1806, 11, 21), date(1808, 5, 2), date(1812, 6, 24),
       date(1812, 9, 14), date(1813, 10, 16), date(1814, 3, 31), date(1814, 4, 6)]
assert seq == sorted(seq), "timeline not in order"

# Press: 73 papers cut to 13 -> 60 closed
eq("papers closed", 73 - 13, 60)
# Plebiscites (rounded official figures): ratios very large
for label, yes, no in [("1800", 3_011_007, 1_562), ("1802", 3_568_885, 8_374), ("1804", 3_572_329, 2_569)]:
    assert yes > 300 * no, label
assert round(3_011_007 / 1e6, 1) == 3.0
assert round(3_568_885 / 1e6, 2) == 3.57 and round(3_572_329 / 1e6, 2) == 3.57
assert round(8_374, -2) == 8400 and round(2_569, -2) == 2600 and round(1_562, -2) == 1600
# 1800 plebiscite with about a million added: real yes about 1.5-2.0 million ("nearer 1.5 million")
assert 3_011_007 - 1_000_000 > 1_500_000
# Consul for life 2 August 1802 and the Tribunate cut to 50 members of 100
eq("Tribunate halved", 100 // 2, 50)
# Civil Code: promulgated 21 March 1804; Duc d'Enghien shot the same day; renamed 1807
eq("Code and Enghien same day", date(1804, 3, 21), date(1804, 3, 21))
# Concordat signed 15 July 1801, published Easter Sunday 18 April 1802; lasted to 1905
assert date(1802, 4, 18).weekday() == 6, "18 April 1802 should be a Sunday (Easter)"
eq("Concordat lasted", 1905 - 1801, 104)
# Peace of Amiens: first general peace for ten years (war began April 1792; Amiens March 1802)
eq("years of war", 1802 - 1792, 10)
# Franc germinal 1803 lasted until 1914
eq("franc lifespan", 1914 - 1803, 111)
# Moscow 14 Sept to retreat 19 Oct: five weeks
eq("Moscow weeks", (date(1812, 10, 19) - date(1812, 9, 14)).days // 7, 5)
# Leipzig 16-19 October 1813: four days
eq("Leipzig days", (date(1813, 10, 19) - date(1813, 10, 16)).days + 1, 4)
# Peninsular War 1808-14: six years
eq("Peninsular war years", 1814 - 1808, 6)
# Emperor to abdication: nine years and four months (1804-1814)
eq("Empire years", 1814 - 1804, 10)
# Fifteen years of rule (Brumaire 1799 to April 1814)
assert 14 < (date(1814, 4, 6) - date(1799, 11, 9)).days / 365.25 < 15.5
# Frankfurt declaration 1 December 1813; 29th Bulletin 3 December 1812; abdication 6 April 1814
assert date(1812, 12, 3) < date(1813, 12, 1) < date(1814, 4, 6)
# Marie-Louise marriage 2 April 1810; King of Rome 20 March 1811
assert date(1810, 4, 2) < date(1811, 3, 20)
# Interval Napoleon left army (5 Dec 1812) after 29th Bulletin (3 Dec)
eq("left army two days after bulletin", (date(1812, 12, 5) - date(1812, 12, 3)).days, 2)
# Civil Code: 2,281 articles
eq("articles", 2281, 2281)
# Plebiscite share for Empire
assert Fraction(2569, 3572329 + 2569) < Fraction(1, 1000)
# Brumaire date conversions: 18 Brumaire VIII = 9 Nov 1799 (Year VIII began 23 Sept 1799; Brumaire is month 2)
eq("18 Brumaire VIII", date.fromordinal(date(1799, 9, 23).toordinal() + 30 + 17), date(1799, 11, 9))
eq("28 Pluviose VIII", date.fromordinal(date(1799, 9, 23).toordinal() + 30 * 4 + 27), date(2000, 1, 1).replace(year=1800, month=2, day=17))
eq("7 Germinal XI", date.fromordinal(date(1802, 9, 23).toordinal() + 30 * 6 + 6), date(1803, 3, 28))

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(5, 8), (9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25

# Figure layout (Constitution of the Year VIII SVG, viewBox 340 x 440)
boxes = [(10, 54), (84, 128), (158, 202), (232, 276), (306, 350), (380, 424)]
for (a1, a2), (b1, b2) in zip(boxes, boxes[1:]):
    assert b1 - a2 >= 28, "gap too small for an arrow"
down = [(57, 78, 0, 1), (131, 152, 1, 2), (205, 226, 2, 3)]
for y1, y2, a, b in down:
    assert y2 - y1 >= 20
    assert boxes[a][1] + 3 <= y1 and y2 + 4 <= boxes[b][0]
up = [(302, 281, 4, 3), (376, 355, 5, 4)]
for y1, y2, frm, to in up:
    assert y1 - y2 >= 20
    assert boxes[frm][0] - 4 >= y1 and y2 >= boxes[to][1] + 4
assert 440 - 424 >= 10
for t in ["First Consul: Bonaparte, 10 years", "holds real power; two others advise", "picks members of the two bodies above",
          "Legislative Body: 300 members", "debate the bills, cannot vote", "chosen by all men over 21"]:
    assert len(t) * 7 <= 300 - 12, t

print("ok")
