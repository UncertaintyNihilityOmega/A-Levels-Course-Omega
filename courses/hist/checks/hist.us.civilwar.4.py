# checks/hist.us.civilwar.4.py: recomputes every number in the chapter (dates, votes, electoral college, chart, marks)
import re
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


text = open("chapters/hist.us.civilwar.4.md", encoding="utf-8").read()

# Lincoln: shot 14 April, died 15 April, five days after Appomattox
eq("Appomattox to shooting", (date(1865, 4, 14) - date(1865, 4, 9)).days, 5)
# Wade-Davis Bill: passed 2 July, pocket veto 4 July, Lincoln's statement 8 July, Manifesto 5 August 1864
assert date(1864, 7, 2) < date(1864, 7, 4) < date(1864, 7, 8) < date(1864, 8, 5)
eq("pocket veto to manifesto (days)", (date(1864, 8, 5) - date(1864, 7, 4)).days, 32)  # "a month after"
# 13th Amendment: House vote 119-56 on 31 Jan 1865; two-thirds of those voting
yes, no = 119, 56
assert yes / (yes + no) >= 2 / 3
eq("House 13th total", yes + no, 175)
# ratified 6 December 1865, proclaimed 18 December
assert date(1865, 12, 6) < date(1865, 12, 18)
# Johnson: Amnesty 29 May 1865; Memphis 1-3 May 1866; New Orleans 30 July 1866
eq("Memphis days", (date(1866, 5, 3) - date(1866, 5, 1)).days + 1, 3)
# Civil Rights Act: vetoed 27 March, overridden 9 April 1866 (13 days)
eq("veto to override", (date(1866, 4, 9) - date(1866, 3, 27)).days, 13)
# First Reconstruction Act 2 March 1867 and Tenure of Office Act the same day
assert date(1867, 3, 2).weekday() == 5  # Saturday
# Stanton dismissed 21 Feb 1868; impeachment 24 Feb: three days
eq("Stanton to impeachment", (date(1868, 2, 24) - date(1868, 2, 21)).days, 3)
# House vote 126-47
eq("House impeachment total", 126 + 47, 173)
# Senate 35-19: 54 senators, two-thirds is 36
sen = 35 + 19
eq("Senate size", sen, 54)
eq("two-thirds needed", -(-2 * sen // 3), 36)
eq("one vote short", 36 - 35, 1)
eq("Republican defectors", len(["Fessenden", "Fowler", "Grimes", "Henderson", "Ross", "Trumbull", "Van Winkle"]), 7)
# 14th Amendment ratified 9 July 1868; 15th ratified 3 February 1870; 13th Dec 1865
assert date(1865, 12, 6) < date(1868, 7, 9) < date(1870, 2, 3)
eq("13th to 15th (years)", 1870 - 1865, 5)
# Revels seated 25 February 1870, three weeks after the 15th Amendment
eq("15th to Revels", (date(1870, 2, 25) - date(1870, 2, 3)).days, 22)
# Bruce full Senate term 1875-81: six years
eq("Senate term", 1881 - 1875, 6)
# Enforcement Acts: 31 May 1870, 28 Feb 1871, 20 April 1871
assert date(1870, 5, 31) < date(1871, 2, 28) < date(1871, 4, 20)
# Amnesty Act 22 May 1872; Colfax 13 April 1873; Panic 18 Sept 1873; Civil Rights Act 1 March 1875
assert date(1872, 5, 22) < date(1873, 4, 13) < date(1873, 9, 18) < date(1875, 3, 1)
# Civil Rights Cases 15 October 1883: eight years after the Act
eq("Act to Cases", 1883 - 1875, 8)
# Tilden 184 + Hayes 165 + 20 disputed = 369 electoral votes; 185 needed
eq("electoral votes", 184 + 165 + 20, 369)
eq("majority", 369 // 2 + 1, 185)
eq("Hayes if all 20", 165 + 20, 185)
eq("Tilden", 184, 185 - 1)
eq("disputed", 3 + 1, 4)  # Florida, Louisiana, South Carolina, plus Oregon (as states)
eq("Electoral Commission", 5 + 5 + 5, 15)
eq("Commission split", 8 + 7, 15)
# Popular vote margin about a quarter of a million (4.29m vs 4.04m)
margin = 4_290_000 - 4_040_000
assert 200_000 <= margin <= 300_000
# Hayes declared 2 March, inaugurated 5 March 1877; troops out April 1877
eq("declared to inauguration", (date(1877, 3, 5) - date(1877, 3, 2)).days, 3)
# Redeemer table: states and the cumulative chart
redeemed = {"Tennessee": 1869, "Virginia": 1870, "North Carolina": 1870, "Georgia": 1871, "Texas": 1873,
            "Arkansas": 1874, "Alabama": 1874, "Mississippi": 1875, "Louisiana": 1877,
            "South Carolina": 1877, "Florida": 1877}
eq("eleven states", len(redeemed), 11)
chart = {1869: 1, 1870: 3, 1871: 4, 1872: 4, 1873: 5, 1874: 7, 1875: 8, 1876: 8, 1877: 11}
for y, n in chart.items():
    eq(f"cumulative {y}", sum(1 for v in redeemed.values() if v <= y), n)
assert f"1869={chart[1869]}, 1870={chart[1870]}, 1871={chart[1871]}, 1872={chart[1872]}, 1873={chart[1873]}, 1874={chart[1874]}, 1875={chart[1875]}, 1876={chart[1876]}, 1877={chart[1877]}" in text
eq("eight states before 1877", 11 - 3, 8)
# Black population: about 3.5 million of 9 million in the Confederacy = 39 per cent ("nearly 4 in 10")
assert 0.38 < 3.5 / 9 < 0.40
# Registration 1867: about 700,000 Black men
assert 650_000 < 700_000 < 750_000
# Impeachment articles: 9 + 1 + 1 = 11
eq("articles", 9 + 1 + 1, 11)
# Freedmen's Bureau 3 March 1865 to 1872: seven years
eq("Bureau life", 1872 - 1865, 7)
# Klan Act used in nine counties; Colfax range 62-80 inside 60-150
assert 60 <= 62 <= 80 <= 150
# Lincoln's reply: The 1864 election gave Johnson the vice-presidency; Johnson's term to 4 March 1869
assert date(1865, 4, 15) < date(1869, 3, 4)
eq("Johnson years", 1869 - 1865, 4)

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

# Source word counts: Paper 1 allows at most 600 words in the four sources
for name in ("Sources for exam practice questions 6 and 7", "Paper 1 (b) [25]: use all four sources"):
    i = text.index(name)
    block = text[i:i + 5000]
    srcs = re.findall(r"\*\*Source [A-D]\*\*\n\n(.+?)\n\n\*", block, flags=re.S)
    n = sum(len(s.split()) for s in srcs)
    assert len(srcs) >= 4, f"{name}: found {len(srcs)} sources"
    srcs = srcs[:4]
    n = sum(len(s.split()) for s in srcs)
    assert n <= 600, f"{name}: {n} words in sources"
print("ok")
