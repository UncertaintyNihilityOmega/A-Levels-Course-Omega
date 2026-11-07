# checks/hist.eu.france.3.py: recomputes every number in the chapter (dates, ages, intervals, shares, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Robespierre born 6 May 1758; joined the Committee 27 July 1793 -> "at 35"
eq("Robespierre age at Committee", age(date(1758, 5, 6), date(1793, 7, 27)), 35)
# Bonaparte born 15 August 1769; 13 Vendemiaire (5 October 1795) -> "aged 26"
eq("Bonaparte at Vendemiaire", age(date(1769, 8, 15), date(1795, 10, 5)), 26)

# Dates in order (story in dates)
seq = [date(1793, 1, 21), date(1793, 2, 24), date(1793, 3, 10), date(1793, 4, 6), date(1793, 6, 2),
       date(1793, 6, 24), date(1793, 7, 13), date(1793, 7, 27), date(1793, 8, 23), date(1793, 9, 5),
       date(1793, 9, 17), date(1793, 9, 29), date(1793, 10, 10), date(1793, 10, 16), date(1793, 12, 4),
       date(1794, 3, 24), date(1794, 4, 5), date(1794, 6, 8), date(1794, 6, 10), date(1794, 6, 26),
       date(1794, 7, 27), date(1794, 12, 24), date(1795, 4, 1), date(1795, 5, 20), date(1795, 8, 22),
       date(1795, 10, 5), date(1795, 11, 2), date(1796, 5, 10), date(1797, 9, 4), date(1797, 9, 30),
       date(1797, 10, 17), date(1798, 5, 11), date(1799, 6, 18), date(1799, 11, 9)]
assert seq == sorted(seq), "timeline not in order"

# Great Terror: 10 June to 27 July 1794 = 47 days (inclusive count of days from 10 June to 27 July)
eq("Great Terror days", (date(1794, 7, 27) - date(1794, 6, 10)).days, 47)
# Marat killed 13 July 1793; painting presented in the autumn of 1793
assert date(1793, 7, 13) < date(1793, 9, 22)
# Roux petition 25 June 1793 is the day after the Constitution of 1793 (24 June)
eq("Roux day after constitution", (date(1793, 6, 25) - date(1793, 6, 24)).days, 1)
# Roux petition three weeks after the purge of 2 June
eq("Roux weeks after purge", (date(1793, 6, 25) - date(1793, 6, 2)).days // 7, 3)
# Robespierre's speech 5 February 1794 is eight months after Roux (25 June 1793)
eq("Roux to Robespierre months", (1794 - 1793) * 12 + (2 - 6), 8)
# Robespierre executed the day after 9 Thermidor
eq("execution day", (date(1794, 7, 28) - date(1794, 7, 27)).days, 1)
# Directory ran 2 November 1795 to 9 November 1799: four years
eq("Directory years", date(1799, 11, 9).year - date(1795, 11, 2).year, 4)
# Revolutionary government dated "from the king's execution": Terror September 1793 to July 1794
assert date(1793, 9, 5) < date(1794, 7, 27)
# Governments: five different governments in seven years (1792-99, listed in the table)
eq("years 1792-99", 1799 - 1792, 7)
# Dumouriez went over on 5 April, the Committee formed 6 April
eq("Dumouriez to Committee", (date(1793, 4, 6) - date(1793, 4, 5)).days, 1)
# Savenay 23 December 1793 is after Toulon retaken in December and before 1794
assert date(1793, 8, 28) < date(1793, 10, 9) < date(1793, 12, 23)
# Fructidor 18 = 4 September 1797; Floreal 22 = 11 May 1798; Prairial 30 = 18 June 1799;
# Vendemiaire 13 = 5 October 1795; Germinal 12 = 1 April 1795; Prairial 1 = 20 May 1795
# (Year III Vendemiaire 1 = 22 Sept 1794 ; Year IV Vendemiaire 1 = 23 Sept 1795 ; year V 22 Sept 1796; VI 22 Sept 1797;
#  VII 23 Sept 1798; VIII 23 Sept 1799)
def rep(day_year_start, month_index, day):
    return day_year_start.toordinal() + 30 * (month_index - 1) + (day - 1)
y3 = date(1794, 9, 22); y4 = date(1795, 9, 23); y5 = date(1796, 9, 22); y6 = date(1797, 9, 22); y7 = date(1798, 9, 22); y8 = date(1799, 9, 23)
# Months: 1 Vend,2 Brum,3 Frim,4 Nivose,5 Pluviose,6 Ventose,7 Germinal,8 Floreal,9 Prairial,10 Messidor,11 Thermidor,12 Fructidor
eq("13 Vendemiaire IV", date.fromordinal(rep(y4, 1, 13)), date(1795, 10, 5))
eq("12 Germinal III", date.fromordinal(rep(y3, 7, 12)), date(1795, 4, 1))
eq("1 Prairial III", date.fromordinal(rep(y3, 9, 1)), date(1795, 5, 20))
eq("18 Fructidor V", date.fromordinal(rep(y5, 12, 18)), date(1797, 9, 4))
eq("22 Floreal VI", date.fromordinal(rep(y6, 8, 22)), date(1798, 5, 11))
eq("30 Prairial VII", date.fromordinal(rep(y7, 9, 30)), date(1799, 6, 18))
eq("18 Brumaire VIII", date.fromordinal(rep(y8, 2, 18)), date(1799, 11, 9))
eq("9 Thermidor II", date.fromordinal(rep(date(1793, 9, 22), 11, 9)), date(1794, 7, 27))
eq("22 Prairial II", date.fromordinal(rep(date(1793, 9, 22), 9, 22)), date(1794, 6, 10))
eq("14 Frimaire II", date.fromordinal(rep(date(1793, 9, 22), 3, 14)), date(1793, 12, 4))
eq("9 Vendemiaire VI", date.fromordinal(rep(y6, 1, 9)), date(1797, 9, 30))

# Terror statistics (Greer): 16,594 death sentences, Paris 2,639 -> "about 17,000", "roughly one in six", "five in six outside Paris"
total, paris = 16594, 2639
assert 16500 < total < 17000
share = Fraction(paris, total)
assert Fraction(15, 100) < share < Fraction(17, 100), f"Paris share {float(share):.3f}"
assert Fraction(1, 7) < share < Fraction(1, 5)
assert Fraction(5, 6) - Fraction(2, 100) < 1 - share < Fraction(5, 6) + Fraction(2, 100)
# Great Terror rate: about 1,400 in 47 days -> about 30 a day; more than ~1,250 before
assert 1250 < 1400
assert 28 < 1400 / 47 < 32
# Referendum 1793: about 1.8 million yes, about 12,000 no
yes, no = 1_800_000, 12_000
assert yes > 100 * no
# Maximum: prices 1790 + one third, wages 1790 + one half
eq("price cap", Fraction(4, 3), 1 + Fraction(1, 3))
eq("wage cap", Fraction(3, 2), 1 + Fraction(1, 2))
# Two-thirds debt: one third kept
eq("debt kept", 1 - Fraction(2, 3), Fraction(1, 3))
# Councils: 500 + 250 members; five Directors, one retires each year (cycle of five years)
eq("councils", 500 + 250, 750)
eq("Director term cycle", 5 * 1, 5)

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
# Practice mark totals: Paper 2 pairs of 10 + 20
eq("practice marks", 10 + 10 + 10 + 20 + 20 + 15 + 25 + 20, 130)

# Figure layout (Directory SVG, viewBox 340 x 436): boxes, arrows at least 20 px long and clear of boxes
boxes = {"citizens": (10, 54), "electors": (84, 128), "councils": (158, 234), "directory": (276, 352), "ministers": (382, 426)}
arrows = [(57, 78, "citizens", "electors"), (131, 152, "electors", "councils"), (238, 270, "councils", "directory"), (355, 376, "directory", "ministers")]
for y1, y2, a, b in arrows:
    assert y2 - y1 >= 20, "arrow too short"
    assert boxes[a][1] + 3 <= y1 and y2 + 4 <= boxes[b][0], f"arrow {a}->{b} touches a box"
assert 436 - 426 == 10
# horizontal arrow between councils: 158 -> 180 (22 px), boxes end 155 and start 185
assert 180 - 158 >= 20 and 155 + 3 <= 158 and 180 + 4 <= 185
# text widths (7 px per character) inside 260 px boxes
for t in ["Active citizens: men aged 21+", "chosen under a property test", "Executive Directory: five Directors", "list drawn up by the Five Hundred", "Ministers and commissioners"]:
    assert len(t) * 7 <= 260 - 12, t
for t in ["250 members, 40+", "accept or reject", "proposes laws", "Five Hundred"]:
    assert len(t) * 7 <= 145 - 12, t

print("ok")
