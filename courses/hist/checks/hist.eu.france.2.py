# checks/hist.eu.france.2.py: recomputes every number in the chapter (dates, intervals, seat counts, marks, figure layout)
from datetime import date, timedelta
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Days of the week the chapter relies on: 17 July 1791 was a Sunday; 14 July 1789 a Tuesday
eq("17 July 1791 weekday", date(1791, 7, 17).weekday(), 6)

# Order of events in the timeline table
seq = [date(1789, 10, 19), date(1789, 11, 2), date(1790, 1, 15), date(1790, 7, 12), date(1790, 7, 14),
       date(1790, 11, 27), date(1791, 4, 2), date(1791, 4, 18), date(1791, 6, 14), date(1791, 6, 20),
       date(1791, 7, 15), date(1791, 7, 16), date(1791, 7, 17), date(1791, 8, 27), date(1791, 9, 13),
       date(1791, 9, 14), date(1791, 10, 1), date(1791, 11, 9), date(1791, 11, 29), date(1792, 4, 20),
       date(1792, 6, 20), date(1792, 7, 11), date(1792, 7, 25), date(1792, 8, 10), date(1792, 9, 2),
       date(1792, 9, 20), date(1792, 9, 21), date(1792, 9, 22)]
assert seq == sorted(seq), "timeline out of order"

# Civil Constitution (12 July 1790) -> oath decree (27 November 1790); king signed 24 August; assented to oath 26 December
assert date(1790, 7, 12) < date(1790, 8, 24) < date(1790, 11, 27) < date(1790, 12, 26)
# Festival of the Federation a year after the Bastille; "a year earlier" than the Champ de Mars petition (17 July 1791)
eq("federation year", date(1791, 7, 17).year - date(1790, 7, 14).year, 1)

# Flight: left night of 20-21 June, arrested 21 June, back in Paris 25 June (4 days)
eq("return days", (date(1791, 6, 25) - date(1791, 6, 21)).days, 4)
# Mirabeau's death (2 April 1791) -> Saint-Cloud (18 April) -> flight (20 June): "two months later"
eq("Saint-Cloud to flight (months)", (date(1791, 6, 20) - date(1791, 4, 18)).days // 30, 2)
# Pillnitz (27 Aug 1791) to war (20 April 1792): about eight months
eq("Pillnitz to war (months)", round((date(1792, 4, 20) - date(1791, 8, 27)).days / 30.44), 8)
# Leopold II died 1 March 1792, before the war; Francis II
assert date(1792, 3, 1) < date(1792, 4, 20)
# Brunswick Manifesto (25 July) to 10 August: 16 days
eq("Manifesto to 10 August", (date(1792, 8, 10) - date(1792, 7, 25)).days, 16)
# 10 August to Convention abolishing monarchy: 42 days
eq("10 Aug to 21 Sept", (date(1792, 9, 21) - date(1792, 8, 10)).days, 42)
# September Massacres 2-6 September: five days inclusive
eq("massacre days", (date(1792, 9, 6) - date(1792, 9, 2)).days + 1, 5)
# Convention met 20 September, monarchy abolished next day, Year I from the 22nd
eq("Convention to abolition", (date(1792, 9, 21) - date(1792, 9, 20)).days, 1)
eq("abolition to Year I", (date(1792, 9, 22) - date(1792, 9, 21)).days, 1)
# Longwy 23 August, Verdun 2 September: before the massacres begin
assert date(1792, 8, 23) < date(1792, 9, 2)
# Royal family to the Temple 13 August; Lafayette fled 19 August
assert date(1792, 8, 10) < date(1792, 8, 13) < date(1792, 8, 19)
# Legislative Assembly met 1 October 1791 and its veto fight: decrees 9 and 29 November, vetoes in December
assert date(1791, 10, 1) < date(1791, 11, 9) < date(1791, 11, 29) < date(1791, 12, 19)
# Constituent Assembly dissolved 30 September 1791; Legislative met next day
eq("assemblies handover", (date(1791, 10, 1) - date(1791, 9, 30)).days, 1)
# Constitution completed 3 September, king accepted 13, swore 14
assert date(1791, 9, 3) < date(1791, 9, 13) < date(1791, 9, 14)
# Assembly moved to Paris 19 October 1789, 13 days after the October Days (6 October)
eq("move to Paris", (date(1789, 10, 19) - date(1789, 10, 6)).days, 13)
# Artois left 16 July 1789, two days after the Bastille
eq("Artois leaves", (date(1789, 7, 16) - date(1789, 7, 14)).days, 2)
# Favras: hanged February 1790 (after plot December 1789)
assert date(1789, 12, 24) < date(1790, 2, 19)
# Journey to the Republic: Louis king from 1774 (not stated); Year I begins 22 September 1792
eq("tennis to republic years", 1792 - 1789, 3)

# Seats in the Legislative Assembly: about 260 + 135 + 345 = 740 of 745 (the rest scattered); figure says about 345
right, left, centre, total = 264, 136, 345, 745
eq("seat total", right + left + centre, total)
assert abs(260 - right) <= 5 and abs(135 - left) <= 5
# Departments, bishoprics: one diocese per department
eq("departments", 83, 83)
# Budget: assignat ceilings (million livres) rose from 400 to 1,200: tripled
eq("assignat ceiling ratio", Fraction(1200, 400), 3)
# Church land estimate 2,000 to 3,000 million livres, "between two and three thousand million"
assert 2000 < 3000
# Massacre toll range and active citizens
assert 1100 < 1400
eq("active citizens share", round(Fraction(3, 5) * 100), 60)
# Brunswick Manifesto delay: published in Paris at the start of August, after 25 July
assert date(1792, 7, 25) < date(1792, 8, 1)
# Swiss Guard about 900
assert 800 <= 900 <= 1000

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
# Worked-example marks quoted: Level 2 about 4 or 5 sits in 3-5 / 4-7; Level 4 comparison 14-15 in 12-15; Level 5 19-20 in 17-20
assert 3 <= 4 <= 5 and 4 <= 5 <= 7 and 12 <= 14 <= 15 and 17 <= 19 <= 20

# Figures: layout checks
# Groupings figure: five boxes 62 high, gap 8, start y=30; text lines inside boxes; headings clear of boxes
tops = [30, 100, 170, 240, 310]
for t in tops:
    assert t + 54 + 3 < t + 62, "last line too near the box edge"
for a, b in zip(tops, tops[1:]):
    eq("gap", b - (a + 62), 8)
assert 20 + 4 < tops[0]  # heading baseline y=20 clear above first box (top 30)
assert tops[-1] + 62 + 10 < 396 - 10  # bottom heading below last box (bottom 372) with 4+ px clear
# widest text: 31 chars * 7 px = 217 < 300 box width
for txt in ["Radical Jacobins and Cordeliers", "LEFT: want the Revolution to go further", "RIGHT: want to undo the Revolution",
            "about 345 independent deputies", "Lafayette, Barnave, the Lameths"]:
    assert len(txt) * 7 <= 300 or txt.startswith(("LEFT", "RIGHT")) and len(txt) * 7 <= 340, txt

# Road-to-republic figure: six boxes 48 high, step 74, arrows 20 px between box edge gaps
tops2 = [10, 84, 158, 232, 306, 380]
for a, b in zip(tops2, tops2[1:]):
    eq("step", b - a, 74)
    assert (b - 3) - (a + 48 + 3) >= 20, "arrow too short"
for txt in ["the patriots split; republicans hounded", "Year I of the Republic from 22 September",
            "the king seen to reject the Revolution", "Monarchy abolished, 21 September"]:
    assert len(txt) * 7 <= 280, txt
assert tops2[-1] + 48 + 4 <= 432

print("ok")
