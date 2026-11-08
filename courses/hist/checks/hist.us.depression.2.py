# checks/hist.us.depression.2.py: recomputes every number in the chapter (dates, rates, banks, votes, marks, figure layout)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"


# Crash losses against the federal budget (about $3 billion a year)
eq("weeks losses vs budget", 30 // 3, 10)  # "many times"
near("Dow fall to 1932 low", 100 * (381.17 - 41.22) / 381.17, 89.2, 0.05)

# Unemployment (Margo 1993, Table 1): Lebergott and Darby
leb = {1929: 3.2, 1930: 8.7, 1931: 15.9, 1932: 23.6, 1933: 24.9}
dar = {1929: 3.2, 1930: 8.7, 1931: 15.3, 1932: 22.9, 1933: 20.6}
near("Lebergott rise", leb[1933] - leb[1929], 21.7, 1e-9)  # "over 20 percentage points"
near("Darby rise", dar[1933] - dar[1929], 17.4, 1e-9)
assert dar[1933] < leb[1933] and leb[1929] == dar[1929]
assert 20 < dar[1933] < 25 and 24 < leb[1933] < 25  # "between about 21 and 25 per cent"
assert max(dar.values()) == dar[1932]

# Banks (Federal Reserve Bulletin, Sept 1937): suspensions and deposits ($ thousand)
susp = {1930: 1350, 1931: 2293, 1932: 1453, 1933: 4000}
eq("suspensions 1930-33", sum(susp.values()), 9096)
dep = {1929: 230643, 1930: 837036, 1931: 1680232, 1932: 706188, 1933: 3596698}
near("deposits 1929 $m", dep[1929] / 1000, 230.6, 0.05)
near("deposits 1930 $m", dep[1930] / 1000, 837.0, 0.05)
near("deposits 1931 $m", dep[1931] / 1000, 1680.2, 0.05)
near("deposits 1932 $m", dep[1932] / 1000, 706.2, 0.05)
near("deposits 1933 $m", dep[1933] / 1000, 3596.7, 0.05)
assert 3.55 < dep[1933] / 1000 / 1000 < 3.65  # "$3.6 billion"
assert 1.6 < dep[1931] / 1e6 < 1.7  # "$1.68 billion"

# Farm income after expenses ($ million): 4,890 (1929) -> 1,473 (1932)
near("farm income fall %", 100 * (4890 - 1473) / 4890, 69.9, 0.05)  # "about 70 per cent"
near("farm income $bn 1929", 4890 / 1000, 4.9, 0.05)
near("farm income $bn 1932", 1473 / 1000, 1.5, 0.05)

# Mexican-born population in AZ, CA, NM, TX (Yawp, census): 1930 -> 1940
near("Mexican-born fall %", 100 * (616998 - 377433) / 616998, 38.8, 0.05)

# Relief: Garner-Wagner about $2.1 billion vs $300 million of loans
assert 6 < 2100 / 300 < 8

# Tax: top rate 25 -> 63 in 1932
eq("Revenue Act rise (points)", 63 - 25, 38)

# Bonus Army: dates, votes, weekdays
eq("House vote total", 211 + 176, 387)
eq("Senate vote total", 62 + 18, 80)
eq("Patman bill House weekday", date(1932, 6, 15).weekday(), 2)  # Wednesday
eq("Patman bill Senate weekday", date(1932, 6, 17).weekday(), 4)  # Friday
eq("Clearance weekday", date(1932, 7, 28).weekday(), 3)  # Thursday
eq("Senate vote to clearance (days)", (date(1932, 7, 28) - date(1932, 6, 17)).days, 41)
eq("Clearance to election (days)", (date(1932, 11, 8) - date(1932, 7, 28)).days, 103)
assert date(1932, 7, 28) < date(1932, 7, 29)  # Hoover's statement the next day

# Election of 1932
roosevelt, hoover, total = 22818740, 15760425, 39747783
near("Roosevelt %", 100 * roosevelt / total, 57.4, 0.05)
near("Hoover %", 100 * hoover / total, 39.65, 0.05)
assert 39.5 < 100 * hoover / total < 40.5  # "about 40 per cent"
rest = total - roosevelt - hoover
assert 880000 + 100000 < rest  # Thomas and Foster fit inside the remainder
eq("electoral votes", 472 + 59, 531)
assert 472 > 531 // 2 + 1
eq("states", 42 + 6, 48)
eq("Hoover's six states", 36 + 8 + 3 + 3 + 4 + 5, 59)  # PA, CT, DE, VT, NH, ME
eq("Election weekday (Tuesday)", date(1932, 11, 8).weekday(), 1)
eq("Acceptance speech weekday (Saturday)", date(1932, 7, 2).weekday(), 5)
eq("Madison Square Garden weekday (Monday)", date(1932, 10, 31).weekday(), 0)
eq("Hoover speech 1928 weekday (Monday)", date(1928, 10, 22).weekday(), 0)
eq("Relief statement weekday (Tuesday)", date(1931, 2, 3).weekday(), 1)
eq("Bank of US failure weekday (Thursday)", date(1930, 12, 11).weekday(), 3)
eq("RFC weekday (Friday)", date(1932, 1, 22).weekday(), 4)
eq("Relief Act weekday (Thursday)", date(1932, 7, 21).weekday(), 3)
eq("Inauguration weekday (Saturday)", date(1933, 3, 4).weekday(), 5)
# 1936: 46 of 48 states, 523 electoral votes to 8
eq("1936 electoral", 523 + 8, 531)
eq("1936 states", 46 + 2, 48)

# Sizes: RFC $500 million + $1.5 billion; Farm Board $500 million
eq("RFC total backing ($m)", 500 + 1500, 2000)

# Years: Mellon-era and welfare comparisons
eq("Britain insurance 1911 to 1932", 1932 - 1911, 21)
eq("Germany insurance 1927 to 1932", 1932 - 1927, 5)
eq("Section 213 repeal years", 1937 - 1932, 5)

# Paper structure (FACTS.md)
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

# Figure layout: spiral (viewBox 340 x 354). Boxes 250 wide at x=8, height 40, step 72; arrows 24 px, 4 px clear at each end
tops = [10 + 72 * i for i in range(5)]
for a, b in zip(tops, tops[1:]):
    gap = b - (a + 40)
    assert gap - 8 >= 20, ("arrow too short", gap)
assert tops[-1] + 40 <= 354
for s in ["Spending and prices fall", "spend less, cannot pay debts", "Farms, firms and banks fail",
          "prices fall, debts stay the same", "Banks lend less", "money supply shrinks", "Unemployed families"]:
    assert len(s) * 7 <= 250 - 8, s
# return path at x=300 clear of box edge (258) by more than 4 px; label at x=318..331 inside 340
assert 300 - 258 > 4 and 318 + 13 <= 340 - 4
assert 174 - 20 * 7 / 2 > tops[0] and 174 + 20 * 7 / 2 < tops[-1] + 40  # label sits between the first and last box
# coalition diagram (340 x 304): frame 8..332, boxes at x=14 and 174, width 152; 7 px per character, 4 px margin
for s in ["Southern whites", "the Solid South", "Catholics, Jews,", "ethnic groups", "Midwest and West", "strong after 1935",
          "African Americans", "mainly from", "1934 to 1936", "Reformers", "women and", "intellectuals", "Trade unionists", "Urban workers"]:
    assert len(s) * 7 <= 152 - 8, s
rows = [(88, 60), (154, 60), (220, 68)]
for (y, h), (y2, _) in zip(rows, rows[1:]):
    assert y2 - (y + h) >= 4
assert rows[-1][0] + rows[-1][1] <= 80 + 216 - 4  # inside the frame (80..296)
assert 14 + 152 < 174 and 174 + 152 < 332
print("ok")
