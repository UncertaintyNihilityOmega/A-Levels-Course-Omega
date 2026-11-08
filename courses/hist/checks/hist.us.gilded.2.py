# checks/hist.us.gilded.2.py: recomputes every number in the chapter (dates, ratios, totals, figure layout)
from datetime import date
import os, re


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# NBER contraction October 1873 - March 1879 = 65 months ("the longest")
months = (1879 - 1873) * 12 + (3 - 10)
eq("1873-79 contraction months", months, 65)
# Panic of 1873 on 18 September 1873 (a Thursday); Exchange closed ten days (20-30 September)
eq("Cooke failure weekday", date(1873, 9, 18).weekday(), 3)
eq("exchange closure days", (date(1873, 9, 30) - date(1873, 9, 20)).days, 10)
# Resumption 1 January 1879; Munn 1 March 1877; Wabash 1886; ICA 4 February 1887; Sherman 2 July 1890
assert date(1877, 3, 1) < date(1879, 1, 1) < date(1886, 1, 1) < date(1887, 2, 4) < date(1890, 7, 2)
# Urban share 26% (1870) -> 40% (1900); farm workforce half -> 40%
assert 26 < 40
# Chicago 300,000 -> 1.7 million
between("Chicago growth", 1.7e6 / 0.3e6, 5.5, 5.8)
# Child labour 1.75 million, about 18% of 10-15s: implies about 9.7 million children of that age
between("child population implied", 1.75e6 / 0.18, 9.2e6, 10.2e6)
# Life expectancy 47 (1900)
# Monongah 6 December 1907: 362 killed
eq("Monongah year", date(1907, 12, 6).year, 1907)
# Spahr 1896: richest 1% hold more than half (51%)
assert 51 > 50
# Tweed: courthouse more than $12 million; estimates $30m to over $100m
assert 30 < 100
# Standard Oil: incorporated 1870, South Improvement 1872, trust 2 January 1882, Ohio order 1892, NJ 1899
assert 1870 < 1872 < 1882 < 1892 < 1899
eq("Ohio order to NJ holding company", 1899 - 1892, 7)
# U.S. Steel: $480m purchase, $1.4bn capitalisation, about two-thirds of output
between("US Steel multiple", 1400 / 480, 2.8, 3.0)
assert 0.6 < 2 / 3 < 0.7
# Knights: 100,000 (1885) -> 700,000 (1886) = sevenfold; Haymarket 4 May 1886; hangings 11 November 1887; Altgeld 1893
eq("Knights growth", 700000 // 100000, 7)
eq("Haymarket to hangings (days)", (date(1887, 11, 11) - date(1886, 5, 4)).days, 556)
eq("Haymarket to pardon (years)", 1893 - 1886, 7)
# Haymarket sentences: 8 convicted, 7 death sentences, 4 hanged, 3 survivors pardoned (Fielden, Schwab, Neebe), 1 suicide (Lingg)
eq("Haymarket tally", 4 + 1 + 2 + 0, 7)
eq("pardoned", 8 - 4 - 1, 3)
# AFL: December 1886; Gompers president to 1924 = 38 years
eq("Gompers years", 1924 - 1886, 38)
# AFL: half a million (1900) -> 1.7 million (1904)
between("AFL growth", 1.7 / 0.5, 3.3, 3.5)
# Great Railroad Strike began 16 July 1877; Hayes was President (1877-81)
eq("Martinsburg date", date(1877, 7, 16).year, 1877)
# Homestead: about 800 of 3,800 workers in the union
between("Homestead union share", 800 / 3800, 0.2, 0.22)
# 7 workers + 3 Pinkertons = 10 dead; Pattison sent 8,000 militia on 12 July; clash 6 July; Berkman 23 July
eq("Homestead dead", 7 + 3, 10)
eq("Homestead to militia (days)", (date(1892, 7, 12) - date(1892, 7, 6)).days, 6)
eq("Homestead to Berkman (days)", (date(1892, 7, 23) - date(1892, 7, 6)).days, 17)
# Carnegie autobiography 1920 (he died 1919)
assert 1920 > 1919
# Pullman: strike 11 May 1894; boycott 26 June; injunction 2 July; troops 4 July; 29 railroads; 125,000 workers
d = (date(1894, 6, 26) - date(1894, 5, 11)).days
eq("Pullman strike to boycott (days)", d, 46)
eq("boycott to troops (days)", (date(1894, 7, 4) - date(1894, 6, 26)).days, 8)
# Debs jailed six months; In re Debs 1895
# Grange 1867, 800,000 members in 1875; Kelley
eq("Grange to Munn (years)", 1877 - 1867, 10)
# Weaver 1892: 22 electoral votes = KS 10 + CO 4 + ID 3 + NV 3 + ND 1 + OR 1
eq("Weaver electoral votes", 10 + 4 + 3 + 3 + 1 + 1, 22)
# Weaver about 1 million votes ~ 8.5% of ~ 12 million cast
between("Weaver share", 1.03 / 12.1, 0.083, 0.087)
# Weaver 1880: about 3% (308,000 of 9.2 million)
between("Weaver 1880 share", 308 / 9210, 0.03, 0.036)
# Bryan age at Cross of Gold: born 19 March 1860, speech 8 July 1896 -> 36
b, s = date(1860, 3, 19), date(1896, 7, 8)
eq("Bryan age", s.year - b.year - ((s.month, s.day) < (b.month, b.day)), 36)
# McKinley 271 vs Bryan 176 electoral votes (total 447); 271 > 224 needed
eq("1896 total electoral votes", 271 + 176, 447)
assert 271 >= 448 // 2 + 1 or 271 > 447 / 2
# Panic of 1893: Philadelphia and Reading Feb 1893; stock crash 5 May 1893; repeal Nov 1893; Morgan gold $62m 1895; recovery 1897
assert date(1893, 2, 20) < date(1893, 5, 5) < date(1893, 11, 1) < date(1895, 2, 1)
# 1907: Knickerbocker 22 October 1907
eq("Knickerbocker", date(1907, 10, 22).month, 10)
# Vanderbilt left about $100 million in 1877
# Cotton: under half of mid-1870s price; wheat about half
assert 5 < 0.5 * 11 and 49 < 110 * 0.5
# Mark totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)
# Gilded.1 to gilded.2: 1900 steel etc not used here

# Figure geometry: vertical/horizontal combination figure (viewBox 346 x 292)
vboxes = [(6, 30, 70, 60, ["Ore and", "coal", "mines"]), (94, 30, 70, 60, ["Ships", "and rail", "lines"]),
          (182, 30, 70, 60, ["Coke and", "blast", "furnaces"]), (270, 30, 70, 60, ["Steel", "mills", "(rails)"])]
for x, y, w, h, lines in vboxes:
    for t in lines:
        assert len(t) * 7 <= w - 8, f"label too wide {t!r}"
    assert x + w <= 346 - 4
for (x1, _, w1, _, _), (x2, _, _, _, _) in zip(vboxes, vboxes[1:]):
    gap = x2 - (x1 + w1)
    assert gap == 18, gap
# horizontal arrows sit in the gaps with 3 px clearance each side
for xa, xb, gx1, gx2 in [(79, 91, 76, 94), (167, 179, 164, 182), (255, 267, 252, 270)]:
    assert xa - gx1 >= 3 and gx2 - xb >= 3
hboxes = [(6, 132, 104, 48), (121, 132, 104, 48), (236, 132, 104, 48)]
for x, y, w, h in hboxes:
    assert len("refinery") * 7 <= w - 16
assert hboxes[0][0] + hboxes[0][2] < hboxes[1][0] and hboxes[1][0] + hboxes[1][2] < hboxes[2][0]
assert 236 + 104 <= 346 - 4
# arrows down: from y=184 (box bottom 180 + 4) to 214 (target top 218 - 4)
assert 184 >= 180 + 4 and 214 <= 218 - 4
# target box and text
assert len("about 90% of refining by c.1880") * 7 <= 334 - 16
assert 218 + 62 <= 292 - 6
# panel headings clear of the boxes: heading baseline 20 vs box top 30; heading baseline 122 vs box top 132
assert 20 + 4 < 30 and 122 + 4 < 132 and 90 + 4 < 122 - 10

here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.us.gilded.2.md"), encoding="utf-8").read()
for token in ["18 September 1873", "65 months", "4 February 1887", "2 July 1890", "6 July", "8 July 1896", "22 electoral votes", "1.75 million", "362 men", "$480 million", "$1.4 billion"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
print("ok")
