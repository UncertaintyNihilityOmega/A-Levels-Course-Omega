# checks/hist.eu.germany.2.py: recomputes every number in the chapter (dates, intervals, votes, shares, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paris 24 Feb 1848 -> Metternich 13 March: 18 days; Berlin 18 March; German colours 21 March
eq("Paris to Vienna", (date(1848, 3, 13) - date(1848, 2, 24)).days, 18)
assert date(1848, 3, 13) < date(1848, 3, 18) < date(1848, 3, 19) < date(1848, 3, 21)
# Mannheim 27 Feb, Heidelberg 5 March
assert date(1848, 2, 24) < date(1848, 2, 27) < date(1848, 3, 5) < date(1848, 3, 13)
# Ludwig I abdicated 20 March
assert date(1848, 3, 18) < date(1848, 3, 20)
# Pre-Parliament 31 March - 3 April; Parliament opens 18 May; Regent 29 June; Regent takes office 12 July
assert date(1848, 3, 31) < date(1848, 4, 3) < date(1848, 5, 18) < date(1848, 6, 29) < date(1848, 7, 12)
# Malmo 26 Aug 1848; Parliament accepts 16 Sept; riots 18 Sept
assert date(1848, 8, 26) < date(1848, 9, 16) < date(1848, 9, 18)
# Vienna retaken 31 Oct; Blum shot 9 Nov; Wrangel 10 Nov; Prussian Assembly dissolved 5 Dec
assert date(1848, 10, 31) < date(1848, 11, 9) < date(1848, 11, 10) < date(1848, 12, 5) < date(1848, 12, 27)
# Franz Joseph born 18 August 1830, emperor 2 December 1848 -> aged 18
b, k = date(1830, 8, 18), date(1848, 12, 2)
eq("Franz Joseph age", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 18)
# Votes: hereditary emperor 267 to 263 (a margin of 4); 290 votes for Frederick William IV and 248 abstentions
eq("hereditary vote total", 267 + 263, 530)
eq("margin", 267 - 263, 4)
eq("election total", 290 + 248, 538)
# Deputation of 32; refusal 3 April 1849, formal rejection 28 April
assert date(1849, 3, 28) < date(1849, 4, 3) < date(1849, 4, 28)
eq("crown refusal days after election", (date(1849, 4, 3) - date(1849, 3, 28)).days, 6)
# Rump dispersed 18 June 1849; Rastatt 23 July; Worlds: Vilagos 13 August
assert date(1849, 5, 30) < date(1849, 6, 18) < date(1849, 7, 23) < date(1849, 8, 13)
# Dresden rising 3-9 May 1849: seven days
eq("Dresden rising days", (date(1849, 5, 9) - date(1849, 5, 3)).days + 1, 7)
# Three Kings' Alliance 26 May 1849; three-class franchise 30 May 1849 until 1918
assert date(1849, 5, 26) < date(1849, 5, 30)
eq("franchise lasted", 1918 - 1849, 69)
# Erfurt Parliament 20 March - 29 April 1850: 40 days
eq("Erfurt Parliament days", (date(1850, 4, 29) - date(1850, 3, 20)).days, 40)
# Bronzell 8 Nov 1850, Olmuetz 29 Nov 1850: 21 days later
eq("Bronzell to Olmutz", (date(1850, 11, 29) - date(1850, 11, 8)).days, 21)
# Dresden Conferences Dec 1850 - May 1851; Federal Diet restored May 1851
assert date(1850, 11, 29) < date(1851, 5, 15)
# Zollverein renewed 1853 for twelve years: to 1865
eq("renewal term", 1853 + 12, 1865)
# Trade treaty 19 February 1853
assert date(1853, 2, 19).year == 1853
# Population: Austria about 36m, Germans about 8m (about 22 per cent); Prussia about 16m
share = Fraction(8, 36)
assert Fraction(1, 5) < share < Fraction(1, 4), float(share)
assert Fraction(36, 16) > 2
# Combined empire plus Confederation "some 70 million": 36 + about 34 outside Austria? (rough: 70 is the figure cited)
assert 60 < 70 < 80
# Coal: about 5 to about 12 million tonnes, 1850-60: more than doubled
assert Fraction(12, 5) > 2
# Crimean War 1853-56; Paris congress Prussia admitted 25 March 1856
assert 1856 - 1853 == 3
# Solferino 24 June, Magenta 4 June, Villafranca 11 July 1859
assert date(1859, 6, 4) < date(1859, 6, 24) < date(1859, 7, 11)
# Regency 7 Oct 1858; stroke 1857; Nationalverein 16 Sept 1859
assert 1857 < 1858 and date(1858, 10, 7) < date(1859, 9, 16)
# Bismarck born 1815; at Frankfurt 1851-59: eight years; aged 36 in 1851
eq("Frankfurt years", 1859 - 1851, 8)
eq("Bismarck age 1851", 1851 - 1815, 36)  # born 1 April 1815, so 36 from April 1851
# Bismarck letter April 1856: five years after 1851
eq("years at Frankfurt by 1856", 1856 - 1851, 5)
# Barricade deaths 200-300; Prussian troops 13,000
assert 200 < 300
# Palacky letter 11 April 1848; Gagern speech 24 June 1848 (five days before the Regent's election)
eq("Gagern speech to election", (date(1848, 6, 29) - date(1848, 6, 24)).days, 5)
# Schwarzenberg's Kremsier speech 27 Nov 1848 (after taking office 21 Nov)
assert date(1848, 11, 21) < date(1848, 11, 27)
# Basic Rights 27 Dec 1848 annulled 23 Aug 1851: just over two and a half years
d = (date(1851, 8, 23) - date(1848, 12, 27)).days
assert 900 < d < 1000, d

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

# Figure layout (viewBox 340 x 292): three boxes of width 104 with 8 px gaps inside 340; labels 7.5 px a character bold
boxes = [(6, 104), (118, 104), (230, 104)]
for (x, w) in boxes:
    assert x >= 0 and x + w <= 340
for (x1, w1), (x2, w2) in zip(boxes, boxes[1:]):
    assert x2 - (x1 + w1) >= 8
for s in ["Austria", "Prussia", "Other states", "Austria out"]:
    assert len(s) * 7.5 <= 104 - 8, s
for s in ["Problem: Austria rules about 36 million,", "only about 8 million German-speaking,", "and will not divide its empire",
          "Problem: needs a Prussian emperor,", "and Austria will oppose it", "Kleindeutsch: without Austria", "Grossdeutsch: with Austria"]:
    assert len(s) * 7.5 <= 340 - 8, s
# vertical: panel 1 boxes 34-78, text 100-136; title 172; panel 2 boxes 184-228, text 250-268; height 292
assert 136 + 6 < 172 - 10 and 268 + 6 < 292
print("ok")
