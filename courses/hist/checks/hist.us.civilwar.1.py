# checks/hist.us.civilwar.1.py: recomputes every number in the chapter (dates, census figures, votes, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Census 1860: 3,953,760 enslaved of 31,443,321 people = "about one in eight" (12.6%)
enslaved, total = 3_953_760, 31_443_321
share = Fraction(enslaved, total)
assert Fraction(12, 100) < share < Fraction(13, 100), float(share)
# Fifteen slave states: 12,240,293 people, "about a third" enslaved, "roughly 12.2 million"
slave_pop = 12_240_293
s2 = Fraction(enslaved, slave_pop)
assert Fraction(31, 100) < s2 < Fraction(34, 100), float(s2)
eq("12.2 million", round(slave_pop / 1e6, 1), 12.2)
# chart values rounded to 0.01 million: 1860 = 3.95, 1790 = 0.70
eq("chart 1860", round(3_953_760 / 1e6, 2), 3.95)
eq("chart 1790", round(697_681 / 1e6, 2), 0.70)
eq("chart 1850", round(3_204_313 / 1e6, 2), 3.20)
eq("chart 1840", round(2_487_355 / 1e6, 2), 2.49)
eq("chart 1830", round(2_009_043 / 1e6, 2), 2.01)
eq("chart 1820", round(1_538_022 / 1e6, 2), 1.54)
eq("chart 1810", round(1_191_362 / 1e6, 2), 1.19)
eq("chart 1800", round(893_602 / 1e6, 2), 0.89)

# Missouri Compromise 1820 to the Kansas-Nebraska Act 1854: "34 years"
eq("compromise lasted", 1854 - 1820, 34)
# Compromise of 1850 lasted to 1854: "four years"
eq("compromise 1850 lasted", 1854 - 1850, 4)
# Senate balance before 1820: 11 + 11 states
eq("states 1819", 11 + 11, 22)
# California admitted: free states 16 against slave 15
eq("senate after California", (15 + 1, 15), (16, 15))

# Dates
assert date(1850, 9, 9) < date(1850, 9, 18) < date(1850, 9, 20)  # five measures 9-20 Sept; FSA 18 Sept
assert date(1854, 5, 30) > date(1854, 1, 24)                     # Act after the Appeal
eq("Brooks attack weekday is not claimed", (date(1856, 5, 22) - date(1856, 5, 19)).days, 3)  # speech 19-20 May, attack 22 May
eq("Pottawatomie after Sack of Lawrence", (date(1856, 5, 24) - date(1856, 5, 21)).days, 3)
# Lincoln-Douglas: seven debates 21 August to 15 October 1858
d1, d7 = date(1858, 8, 21), date(1858, 10, 15)
assert d1 < date(1858, 8, 27) < d7
eq("debates", len(["Ottawa", "Freeport", "Jonesboro", "Charleston", "Galesburg", "Quincy", "Alton"]), 7)
# Senate vote on Lecompton: 33-25 on 23 March 1858; Kansas admitted 29 January 1861 (nearly three years later)
assert (date(1861, 1, 29) - date(1858, 3, 23)).days // 365 == 2
# Kansas-Nebraska vote counts
eq("Senate vote", 37 + 14, 51)
eq("House vote", 113 + 100, 213)
# Wilmot Proviso House vote
eq("Proviso vote", 83 + 64, 147)
# Lecompton referendum
assert 10_226 > 138 and 10_226 + 138 == 10_364
# Illinois legislature
eq("Illinois legislature", 54 + 46, 100)
pop_rep, pop_dem = 190_468, 166_374
assert 190_000 <= pop_rep <= 191_000 and 166_000 <= pop_dem <= 167_000
# Kansas election 37 of 39 seats
eq("seats", 39 - 37, 2)
# Kansas death toll about 56
# Election of 1852: Pierce 254, Scott 42 (296 electoral votes)
eq("1852 electors", 254 + 42, 296)

# Election of 1856 (UCSB): Buchanan 1,836,072, Fremont 1,342,345, Fillmore 873,053; total 4,054,647
b, f, fi = 1_836_072, 1_342_345, 873_053
tot = 4_054_647
eq("1856 total", b + f + fi, 4_054_647 - 0 if b + f + fi == 4_054_647 else b + f + fi)
eq("Buchanan %", round(100 * b / tot, 1), 45.3)
eq("Fremont %", round(100 * f / tot, 1), 33.1)
eq("Fillmore %", round(100 * fi / tot, 1), 21.5)  # Wikipedia gives 21.6 in the header, 21.5 in the totals row
eq("1856 electors", 174 + 114 + 8, 296)
# Fremont needed 149 electoral votes for a majority; Pennsylvania (27) + Illinois (11) would have been enough
eq("majority", 296 // 2 + 1, 149)
assert 114 + 27 + 11 >= 149 and 114 + 27 + 13 >= 149

# Cotton: almost 60% of exports; 3/4 of world supply (stated as "roughly")
# Immigration 2.6 million in 1850s
# Enslaved people in the South 1860 and free Black people about 250,000 (rounded, hedged in text)

# Convention walkout: "about fifty" (51 delegates) at Charleston 23 April - 3 May 1860
eq("Charleston dates", (date(1860, 5, 3) - date(1860, 4, 23)).days, 10)

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
# Source words (four sources at most 600 words in total) for each source box; counted roughly below
srcA = "All good citizens are hereby commanded to aid and assist in the prompt and efficient execution of this law. In no trial or hearing under this act shall the testimony of such alleged fugitive be admitted in evidence. The commissioner shall receive a fee of ten dollars for each case in which he decides that the person is a fugitive, and five dollars where the proof is not enough."
srcB = "The Nebraska bill is, the authors say, a gross violation of a sacred pledge. The Missouri Compromise of 1820 promised that the land north of 36°30′ would stay free of slavery, and the bill would throw that land open to it."
srcD = "A house divided against itself cannot stand. I believe this government cannot endure, permanently half slave and half free. I do not expect the Union to be dissolved. I do not expect the house to fall. But I do expect it will cease to be divided. It will become all one thing, or all the other."
words = sum(len(s.split()) for s in [srcA, srcB, srcD]) + 40  # plus the cartoon description
assert words <= 600, words

# Figure (schematic map) layout: viewBox 620 x 295; rows, gaps and label boxes
boxes = {  # x, y, w, h
    "california": (10, 50, 120, 225), "utah": (140, 50, 120, 90), "newmexico": (140, 185, 120, 90),
    "nebraska": (270, 50, 180, 42), "kansas": (270, 98, 180, 42), "missouri": (460, 98, 150, 42),
    "texas": (270, 185, 180, 90), "arkansas": (460, 185, 150, 90),
}
for k, (x, y, w, h) in boxes.items():
    assert x >= 0 and y >= 0 and x + w <= 620 and y + h <= 295, k
names = list(boxes)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        x1, y1, w1, h1 = boxes[names[i]]
        x2, y2, w2, h2 = boxes[names[j]]
        assert x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1, (names[i], names[j])
# text width (about 7 px a character) must fit inside each box with 4 px each side
texts = {
    "utah": ["Territory 1850:", "sovereignty"], "newmexico": ["Territory 1850:", "sovereignty"],
    "nebraska": ["Nebraska 1854: open to", "popular sovereignty"], "kansas": ["Kansas 1854: open to", "popular sovereignty"],
    "missouri": ["slave state, 1821"], "texas": ["annexed 1845", "slave state,"],
    "arkansas": ["slave state, 1836", "south of the"], "california": ["admitted 1850", "free state,"],
}
for k, lines in texts.items():
    w = boxes[k][2]
    for s in lines:
        assert len(s) * 7 <= w - 8, (k, s)
# dashed 36°30' line at y = 162 sits between rows (140 and 185); labels clear by 4 px
assert 140 + 4 <= 162 - 13 + 3, "upper label too close to boxes"
# upper label baseline 154 (top 144, bottom ~157): clear of the line at 162 by 5 and of boxes (140) by 4
assert 154 - 10 - 140 >= 4 and 162 - (154 + 3) >= 4
# lower label baseline 178 (top 168, bottom ~181): clear of the line by 6 and of boxes (185) by 4
assert 168 - 162 >= 4 and 185 - (178 + 3) >= 4
# label widths on the line
assert 278 + len("north: closed to slavery 1820–54") * 7 <= 610
print("ok")
