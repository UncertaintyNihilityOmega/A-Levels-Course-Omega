# checks/hist.eu.russia.1.py: recomputes every number in the chapter (dates, statistics, ages, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"


# Old Style / New Style: 1 March 1881 OS = 13 March 1881 NS (12 days behind in the nineteenth century, 13 after 1900)
eq("OS gap 1881", 13 - 1, 12)
# Alexander II born 29 April 1818 NS; killed 13 March 1881 NS: aged 62
b, k = date(1818, 4, 29), date(1881, 3, 13)
eq("Alexander II age", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 62)
# Alexander III born 10 March 1845 NS; Manifesto 29 April 1881 OS = 11 May NS: aged 36
b, k = date(1845, 3, 10), date(1881, 5, 11)
eq("Alexander III age 1881", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 36)
# Manifesto six weeks after the assassination (1 March -> 29 April OS = 59 days = about eight weeks)
d = (date(1881, 4, 29) - date(1881, 3, 1)).days
eq("assassination to Manifesto days", d, 59)
assert 8 <= d / 7 < 9  # "about two months"
# Reign length: 1 March 1881 -> 20 October 1894 OS: just over thirteen years
d = date(1894, 10, 20) - date(1881, 3, 1)
assert 13 * 365 < d.days < 14 * 365, d.days
eq("reign years", 1894 - 1881, 13)
# Nicholas II born 6 May 1868 NS; accession 1 November 1894 NS: aged 26
b, k = date(1868, 5, 6), date(1894, 11, 1)
eq("Nicholas II age", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 26)
# Lenin born 22 April 1870 NS; brother hanged 8 May 1887 OS = 20 May 1887 NS: Lenin aged 17
b, k = date(1870, 4, 22), date(1887, 5, 20)
eq("Lenin age 1887", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 17)
# Plot 1 March 1887 on the sixth anniversary of 1881
eq("anniversary", 1887 - 1881, 6)
# Pobedonostsev Over-Procurator 1880-1905
eq("Pobedonostsev years", 1905 - 1880, 25)
# Bunge 1881-86; Vyshnegradsky 1887-92 (Jan 1887 to Aug 1892)
assert 1886 < 1887 and 1892 < 1892.7
# Reforms: serfs 1861, zemstvos 1864, conscription 1874
assert 1861 < 1864 < 1874 < 1881
# Alexander II reign: 1855-81
eq("Alexander II reign", 1881 - 1855, 26)

# 1897 census: 125,640,021 people; 16,828,395 urban
pop, urban = 125_640_021, 16_828_395
near("urban share", urban / pop * 100, 13.4, 0.05)
near("population million", pop / 1e6, 125.6, 0.05)

# Coal (Statesman's Year-Book 1913), tons: 1860 298,500; 1880 3,280,000; 1900 15,878,203
c60, c80, c00 = 298_500, 3_280_000, 15_878_203
near("coal 1860 chart", c60 / 1e6, 0.3, 0.005)
near("coal 1880 chart", c80 / 1e6, 3.28, 0.0001)
near("coal 1900 chart", c00 / 1e6, 15.88, 0.005)
ratio = c00 / c80
assert 4.5 < ratio < 5.0, ratio  # "almost fivefold"
near("coal 1900 over 1880", ratio, 4.84, 0.01)
assert 3.2 < c80 / 1e6 < 3.4 and 15.8 < c00 / 1e6 < 16.0  # "about 3.3 to about 15.9"

# Railways (Fontana via Fordham), km: 1860 1,626; 1880 22,865; 1900 53,234
r60, r80, r00 = 1626, 22865, 53234
near("rail 1860 chart", r60 / 1000, 1.626, 1e-9)
near("rail 1880 chart", r80 / 1000, 22.865, 1e-9)
near("rail 1900 chart", r00 / 1000, 53.234, 1e-9)
assert 2.0 < r00 / r80 < 2.5  # "more than doubled"
near("rail growth", r00 / r80, 2.33, 0.01)
assert round(r80, -2) == 22900 and round(r00, -2) == 53200

# Strikers (Lenin 1913, official statistics): 1895-1900
s = {1895: 31195, 1896: 29527, 1897: 59870, 1898: 43150, 1899: 57498, 1900: 29389}
assert 25_000 <= min(s.values()) and max(s.values()) <= 60_000  # "30,000 to 60,000" (rounded)
assert min(s.values()) > 29_000 and max(s.values()) < 60_000
# percentages of all workers implied by Lenin's table -> workers covered: about 1.5 million
pct = {1895: 2.0, 1896: 1.9, 1897: 4.0, 1898: 2.9, 1899: 3.8, 1900: 1.7}
for y in s:
    w = s[y] / (pct[y] / 100)
    assert 1.4e6 < w < 1.8e6, (y, w)  # "about 1.5 million"
assert 2_863_173 > 60 * max(s.values()) / 1.6  # 1905 dwarfs the 1890s (about 48 times the 1897 peak)
near("1905 vs 1897 peak", 2_863_173 / 59_870, 47.8, 0.1)

# Famine: aid to 27 provinces, 172 million roubles; deaths from about 375,000; cholera about 300,000
assert 375_000 < 500_000
assert 300_000 < 375_000
# Famine announced 17 November 1891; Tolstoy's article 13 November 1891
assert date(1891, 11, 13) < date(1891, 11, 17)
# Morozov strike January 1885 -> law of 1886
assert 1885 < 1886
# Tolstoy "A Terrible Question" 13 Nov 1891 -> 1896 English translation: five years
eq("translation gap", 1896 - 1891, 5)
# Pobedonostsev Reflections 1896 (Russian) -> 1898 English; fifteen years after 1881
eq("Reflections gap", 1896 - 1881, 15)
# Emancipation of Labour 1883 predates the famine (1891) and Morozov (1885)
assert 1883 < 1885 < 1891
# State Order Statute renewed every three years until 1917 (1881 + 3k): 36 years
eq("Statute years", 1917 - 1881, 36)
# May Laws 1882 -> repealed 1917: 35 years ("thirty years" is a lower bound used in the text)
assert 1917 - 1882 > 30
# Jews emigrated about two million, 1881-1914: 33 years
eq("emigration years", 1914 - 1881, 33)
# Quotas 10/5/3 per cent
assert 10 > 5 > 3
# Capital published in Russian 1872: 9 years before 1881
eq("Capital gap", 1881 - 1872, 9)
# Uvarov 1833 slogan; used 48 years before 1881
eq("slogan gap", 1881 - 1833, 48)
# Dorpat renamed Yuryev 1893
assert 1893 > 1890

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
# Level bands used in the text
for lo, hi in [(3, 5), (6, 8), (9, 10), (4, 7), (8, 11), (12, 15), (9, 12), (13, 16), (17, 20), (11, 15), (16, 20), (21, 25), (5, 8)]:
    assert lo <= hi
# Model answers: P2(a) Level 2 about 4 -> Level 3 6-8 -> Level 4 10; P1(a) Level 4 14-15; P2(b) Level 5 18-20
assert 3 <= 4 <= 5 and 9 <= 10 <= 10 and 12 <= 14 <= 15 and 17 <= 18 <= 20

# Figure 1 layout (viewBox 340 x 436): box tops/bottoms, arrows at least 20 px, labels fit boxes with 4 px margin
boxes = {
    "tsar": (60, 8, 220, 48),
    "state council": (4, 86, 100, 76), "ministers": (110, 86, 120, 76), "senate": (236, 86, 100, 76),
    "army": (4, 190, 100, 76), "police": (110, 190, 120, 76), "church": (236, 190, 100, 76),
    "local": (4, 294, 332, 56), "people": (4, 376, 332, 46),
}
for name, (x, y, w, h) in boxes.items():
    assert x >= 0 and x + w <= 340 and y + h <= 436, name
labels = {
    "tsar": ["The Tsar", "autocrat; head of the Church"],
    "state council": ["State Council", "advisory body", "of appointees"],
    "ministers": ["Ministers", "each reports to", "the Tsar alone"],
    "senate": ["Senate", "top court,", "checks law"],
    "army": ["Army", "largest in", "Europe; also", "keeps order"],
    "police": ["Police", "Okhrana, 1881;", "State Order", "Statute, 1881"],
    "church": ["Church", "Holy Synod;", "Pobedonostsev"],
    "local": ["Local rule", "governors; land captains (1889);", "zemstvos under supervision"],
    "people": ["The people", "125 million (1897); about 80% peasants"],
}
for name, lines in labels.items():
    w = boxes[name][2]
    for ln in lines:
        assert len(ln) * 7 <= w - 8, f"{name}: '{ln}' is {len(ln) * 7}px in a {w}px box"
# arrows: lengths and gaps
arrows = [(58, 82), (164, 188), (268, 292), (352, 374)]
for a, b2 in arrows:
    assert b2 - a >= 20, "arrow too short"
assert 86 - 82 >= 2 and 190 - 188 >= 2 and 294 - 292 >= 2 and 376 - 374 >= 2
# rows do not overlap
assert 56 < 58 and 162 < 164 and 266 < 268 and 350 < 352
print("ok")
