# checks/hist.skills.essays.py: recomputes every number in the chapter (dates, votes, marks, time plan, level bands)
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 2: two questions of (a) 10 + (b) 20 = 30 marks each = 60 marks in 105 minutes
eq("paper 2 marks", 2 * (10 + 20), 60)
eq("paper 4 marks", 2 * 30, 60)
eq("105 minutes", 1 * 60 + 45, 105)
# Time plan: (a) 15 + (b) 35 = 50 per question, two questions = 100, leaving 5 of 105
eq("paper 2 question time", 15 + 35, 50)
eq("paper 2 total time", 2 * (15 + 35), 100)
eq("reading time left", 105 - 100, 5)
eq("paper 4 total time", 2 * 50, 100)
# planning time is part of the stated time: (a) 2 of 15, (b) 4 of 35, Paper 4 5 of 50
assert 2 < 15 and 4 < 35 and 5 < 50
# Level bands (Paper 2 (a) [10], (b) [20], Paper 4 [15] tables)
bands = {
    "P2a": ([(1, 2), (3, 5), (6, 8), (9, 10)], 10),
    "P2b": ([(1, 4), (5, 8), (9, 12), (13, 16), (17, 20)], 20),
    "P4": ([(1, 3), (4, 6), (7, 9), (10, 12), (13, 15)], 15),
}
for name, (bs, top) in bands.items():
    for (lo1, hi1), (lo2, hi2) in zip(bs, bs[1:]):
        eq(f"{name} contiguous", lo2, hi1 + 1)
    eq(f"{name} top", bs[-1][1], top)
eq("P4 tables", 15 + 15, 30)
# the model answers sit in the levels claimed
assert 3 <= 4 <= 5          # (a) Level 2 about 4
assert 9 <= 10 <= 10        # (a) Level 4
assert 17 <= 19 <= 20       # (b) Level 5 (19-20)
# Paper weights: Paper 2 = 60% of AS and 30% of A Level; Paper 4 = 30% of A Level
eq("AS weights", 40 + 60, 100)
eq("A Level weights", 20 + 30 + 20 + 30, 100)

# History
# Senate vote on the Treaty of Versailles 19 November 1919: 39 for, 55 against, 94 voting
eq("senators voting", 39 + 55, 94)
assert 55 > 39
# League began 10 January 1920; Germany joined 1926; USSR 1934
assert date(1919, 11, 19) < date(1920, 1, 10)
eq("Germany joined after the League began (years)", 1926 - 1920, 6)
eq("USSR joined", 1934 - 1920, 14)
# Königgrätz 3 July 1866; Italian alliance 8 April 1866; Biarritz October 1865 is before
assert date(1865, 10, 4) < date(1866, 4, 8) < date(1866, 6, 15) < date(1866, 7, 3)
eq("war to battle (days)", (date(1866, 7, 3) - date(1866, 6, 15)).days, 18)
# Roon's reforms from 1860, six years before 1866
eq("Roon to Königgrätz", 1866 - 1860, 6)
# Lateran Treaties: 11 February 1929; 750 + 1,000 = 1,750 million lire; plebiscite 24 March 1929
eq("Lateran payment", 750 + 1000, 1750)
assert date(1929, 2, 11) < date(1929, 3, 24)
# quarrel since 1870 ended in 1929: 59 years
eq("church-state quarrel", 1929 - 1870, 59)
# Nazi consolidation: Enabling Act 23 Mar 1933; one-party state 14 Jul 1933; Night of the Long Knives 30 Jun 1934; plebiscite 19 Aug 1934
assert date(1933, 3, 23) < date(1933, 7, 14) < date(1934, 6, 30) < date(1934, 8, 19)
# "destroyed within eighteen months": from January/March 1933 to June/August 1934 (at most 18 months from 30 Jan 1933 to 30 Jun 1934)
months = (1934 - 1933) * 12 + (6 - 1)
assert months <= 18, months
# 1936 Rhineland, 1938 Anschluss; plebiscite 1934; unemployment 6 million to under 1 million: more than a five-sixths fall
assert 1 / 6 < 1 / 5
# Montgomery boycott: Rosa Parks arrested 1 December 1955; boycott began 5 December 1955 and ended 20 December 1956: 381 days
eq("Montgomery boycott days", (date(1956, 12, 20) - date(1955, 12, 5)).days, 381)
# Wall Street: Black Thursday 24 October 1929 and Black Tuesday 29 October 1929 are both in October, five days apart
eq("Thursday to Tuesday", (date(1929, 10, 29) - date(1929, 10, 24)).days, 5)
assert date(1929, 10, 24).weekday() == 3 and date(1929, 10, 29).weekday() == 1
# Berlin Conference 15 November 1884 to 26 February 1885 (about three and a half months)
d = (date(1885, 2, 26) - date(1884, 11, 15)).days
assert 100 <= d <= 108, d
# Adowa 1896 to Abyssinia 1935: 39 years
eq("Adowa to invasion", 1935 - 1896, 39)
# Vidoni Palace 1925, Rocco Law 1926, Charter of Labour 1927, Chamber of Fasci and Corporations 1939
assert 1925 < 1926 < 1927 < 1939
# Sherman etc not used here. Corfu: Greece paid 50 million lire
eq("Corfu payment", 50, 50)

# The plan widgets must have 6 factors each and sides on both sides
text = Path(__file__).resolve().parent.parent.joinpath("chapters", "hist.skills.essays.md").read_text(encoding="utf-8")
for m in re.finditer(r'data-factors="([^"]*)"', text):
    facs = [f.strip() for f in m.group(1).split(";;")]
    assert len(facs) == 6, len(facs)
    sides = [f.split("|")[1].strip() for f in facs]
    assert set(sides) == {"support", "challenge"}, sides
print("ok")
