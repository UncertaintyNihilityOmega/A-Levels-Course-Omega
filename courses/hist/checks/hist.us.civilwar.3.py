# checks/hist.us.civilwar.3.py: recomputes every number in the chapter (dates, intervals, ratios, election, marks)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Length of the war: Sumter 12 April 1861 to Appomattox 9 April 1865 is just under four years
war = (date(1865, 4, 9) - date(1861, 4, 12)).days
eq("Sumter to Appomattox", war, 1458)  # 4 x 365 + 1 leap day - 3
assert 4 * 365 - 5 < war < 4 * 365 + 1

# Resources (1860 census, rounded in the chapter)
union, conf, enslaved_conf = 22, 9, 3.5
assert 2.3 < union / conf < 2.6, "about two and a half times"
rail_u, rail_c = 22_000, 9_000
assert 2.3 < rail_u / rail_c < 2.6
eq("whole country 1860 (millions, rounded)", round(union + conf), 31)
assert abs((union + conf) - 31.4) < 0.5
white_conf = conf - enslaved_conf
eq("Confederate white population ~5.5 million", white_conf, 5.5)

# Population of the nation was 31,443,321 in 1860; chapter says 31.4 million
eq("US population 1860", round(31_443_321 / 1e6, 1), 31.4)

# Preliminary proclamation 22 September 1862 -> 1 January 1863: just over 100 days
eq("proclamation interval", (date(1863, 1, 1) - date(1862, 9, 22)).days, 101)
# Antietam 17 Sept, five days before the preliminary proclamation
eq("Antietam to proclamation", (date(1862, 9, 22) - date(1862, 9, 17)).days, 5)
# Greeley letter 22 August 1862, "six months" before the Proclamation (about 4.3 months: 132 days)
d = (date(1863, 1, 1) - date(1862, 8, 22)).days
eq("Greeley to Proclamation (days)", d, 132)
# the chapter must not say six months: check by reading the text below
text = open("chapters/hist.us.civilwar.3.md", encoding="utf-8").read()
assert "Six months later he had issued" not in text, "Greeley letter to Proclamation is about four months"

# Jackson shot 2 May 1863, died 10 May
eq("Jackson died after", (date(1863, 5, 10) - date(1863, 5, 2)).days, 8)
# Gettysburg 1-3 July, Vicksburg 4 July: Vicksburg the day after Gettysburg ended
eq("Gettysburg days", (date(1863, 7, 3) - date(1863, 7, 1)).days + 1, 3)
eq("Vicksburg after Gettysburg", (date(1863, 7, 4) - date(1863, 7, 3)).days, 1)
# Draft riots 13-16 July: four days
eq("riot days", (date(1863, 7, 16) - date(1863, 7, 13)).days + 1, 4)
# Draft started Saturday 11 July 1863
eq("draft start weekday", date(1863, 7, 11).weekday(), 5)
# Grant: commissioned 9 March 1864, took command 12 March
assert date(1864, 3, 9) < date(1864, 3, 12)
# Wilderness 5 May to mid-June is about six weeks
w = (date(1864, 6, 15) - date(1864, 5, 5)).days
eq("Overland weeks", w // 7, 5)  # 41 days: "about six weeks" in the chapter
assert 5 <= w / 7 <= 6.5
# Atlanta 2 Sept 1864 to election 8 Nov 1864: 67 days
eq("Atlanta to election", (date(1864, 11, 8) - date(1864, 9, 2)).days, 67)
# March to the Sea 15 Nov - 21 Dec: 36 days
eq("March to the Sea days", (date(1864, 12, 21) - date(1864, 11, 15)).days, 36)
# Alabama: left July 1862, sunk 19 June 1864; Adams note 5 Sept 1863 (inside)
assert date(1862, 7, 29) < date(1863, 9, 5) < date(1864, 6, 19)
# Trent: seized 8 Nov, released 26 Dec 1861: 48 days
eq("Trent days", (date(1861, 12, 26) - date(1861, 11, 8)).days, 48)
# Lincoln shot 14 April, five days after Appomattox
eq("Appomattox to shooting", (date(1865, 4, 14) - date(1865, 4, 9)).days, 5)
# Richmond bread riot 2 April 1863, Confederate tax-in-kind April 1863
assert date(1863, 4, 2).month == 4
# Chicago Times order: 1 June -> revoked 4 June = three days
eq("Chicago Times", (date(1863, 6, 4) - date(1863, 6, 1)).days, 3)
# Vallandigham arrested 5 May 1863; Corning letter 12 June 1863
assert date(1863, 5, 5) < date(1863, 6, 12)
# Border states are four; West Virginia 35th state (34 states in 1861 + WV)
eq("West Virginia", 34 + 1, 35)

# 1864 election: 212 of 233 electoral votes; popular vote 2,218,388 to 1,812,807
lin, mcc = 2_218_388, 1_812_807
eq("electoral share", round(100 * 212 / 233), 91)
eq("Lincoln popular share", round(100 * lin / (lin + mcc)), 55)
eq("McClellan electoral votes", 233 - 212, 21)  # Kentucky 11, Delaware 3, New Jersey 7
eq("McClellan states", 11 + 3 + 7, 21)

# Union soldiers who were draftees or substitutes: about 46,000 + 118,000 of about 2.1 million
assert (46_000 + 118_000) / 2_100_000 < 0.10, "fewer than one in ten"

# Death estimates: 360,000 + 260,000 = 620,000; Hacker about 750,000 (range 650,000-850,000)
eq("older total", 360_000 + 260_000, 620_000)
assert 650_000 < 750_000 < 850_000

# Black soldiers about 180,000 of about 2.1 million Union troops (under one in ten)
assert 180_000 / 2_100_000 < 0.10

# Inflation: about 9,000% means prices about 91 times higher; Union 80% means 1.8 times
assert abs((1 + 9000 / 100) - 91) < 1e-9
assert abs((1 + 80 / 100) - 1.8) < 1e-9

# Financing the Union (rounded shares quoted as roughly two-thirds, a fifth, an eighth)
shares = {"loans": 65, "taxes": 21, "greenbacks": 13}
assert sum(shares.values()) <= 100
assert 60 <= shares["loans"] <= 70 and 18 <= shares["taxes"] <= 23 and 11 <= shares["greenbacks"] <= 14

# Greenbacks: $150 million authorised in February 1862, about $450 million in all
assert 150 < 450

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
import re
for name in ("Sources for exam practice questions 5 and 6", "Paper 1 (b) [25]"):
    i = text.index(name)
    block = text[i:i + 4000]
    srcs = re.findall(r"\*\*Source [A-D]\*\*\n\n(.+?)\n\n\*", block, flags=re.S)
    n = sum(len(s.split()) for s in srcs)
    assert n <= 600, f"{name}: {n} words in sources"
    assert len(srcs) >= 4, f"{name}: found {len(srcs)} sources"
print("ok")
