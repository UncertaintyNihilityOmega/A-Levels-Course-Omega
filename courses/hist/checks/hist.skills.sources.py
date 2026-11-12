# checks/hist.skills.sources.py: recomputes every number in the chapter (dates, votes, marks, time plan, source lengths)
import math
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 1: (a) 15 + (b) 25 = 40 marks; time plan 5 + 25 + 45 = 75 minutes = 1 h 15 min
eq("paper 1 marks", 15 + 25, 40)
eq("time plan", 5 + 25 + 45, 75)
eq("1 h 15 min", 1 * 60 + 15, 75)
# marks per minute are "almost the same" in (a) and (b)
a_rate, b_rate = 15 / 25, 25 / 45
assert abs(a_rate - b_rate) < 0.06, (a_rate, b_rate)

# Level bands are contiguous and top out at the part's total
A = [(1, 3), (4, 7), (8, 11), (12, 15)]
B = [(1, 5), (6, 10), (11, 15), (16, 20), (21, 25)]
for name, bands, top in (("table A", A, 15), ("table B", B, 25)):
    for (lo1, hi1), (lo2, hi2) in zip(bands, bands[1:]):
        eq(f"{name} contiguous", lo2, hi1 + 1)
    eq(f"{name} top", bands[-1][1], top)
# the model answers sit in the level they claim: Level 2 (about 5), Level 3 (about 10), Level 4 (14-15) for (a)
assert 4 <= 5 <= 7 and 8 <= 10 <= 11 and 12 <= 14 <= 15
# (b): Level 3 about 13, Level 5 about 23
assert 11 <= 13 <= 15 and 21 <= 23 <= 25

# AO weights of Paper 1: 75% AO3 + 25% AO1
eq("AO split", 75 + 25, 100)

# Provenance and dates
# Kiautschou occupied 14 November 1897; Bülow speaks 6 December 1897: "a few weeks" (three)
gap = (date(1897, 12, 6) - date(1897, 11, 14)).days
assert 14 <= gap <= 28, gap
# Treaty of Paris signed 10 December 1898; fighting 4 February 1899; Senate vote 6 February 1899, 57-27
assert date(1898, 12, 10) < date(1899, 2, 4) < date(1899, 2, 6)
eq("days between outbreak and vote", (date(1899, 2, 6) - date(1899, 2, 4)).days, 2)
voters = 57 + 27
needed = math.ceil(voters * 2 / 3)
eq("two-thirds of 84", needed, 56)
eq("one more than needed", 57 - needed, 1)
# Sherman Act: Senate 8 April 1890 (51-1), House 20 June 1890 (242-0), signed 2 July 1890
assert date(1890, 4, 8) < date(1890, 6, 20) < date(1890, 7, 2)
eq("Senate vote total", 51 + 1, 52)
# Omaha Platform 4 July 1892; Puck 23 January 1889; Carnegie June 1889: the cartoon is earlier than the essay
assert date(1889, 1, 23) < date(1889, 6, 1) < date(1892, 7, 4)
# Homestead 1892: seven workers and three guards died -> "ten people"
eq("Homestead dead", 7 + 3, 10)
# Senate chosen by state legislatures until 1913; cartoon of 1889 is 24 years earlier
eq("years before direct election", 1913 - 1889, 24)
# Russia: Old Style dates are 13 days behind New Style in 1905-06
eq("Bloody Sunday NS", date(1905, 1, 9).toordinal() + 13, date(1905, 1, 22).toordinal())
eq("Manifesto NS", date(1905, 10, 17).toordinal() + 13, date(1905, 10, 30).toordinal())
eq("Fundamental Laws NS", date(1906, 4, 23).toordinal() + 13, date(1906, 5, 6).toordinal())
# First Duma opened 27 April 1906 (OS): four days after the Fundamental Laws; dissolved 8 July (OS) after 72 days
eq("days between Fundamental Laws and Duma", (date(1906, 4, 27) - date(1906, 4, 23)).days, 4)
eq("Duma lasted", (date(1906, 7, 8) - date(1906, 4, 27)).days, 72)
# Munich: Chamberlain broadcast 27 Sept, agreement 29 Sept, declaration 30 Sept, Churchill 5 Oct 1938
assert date(1938, 9, 27) < date(1938, 9, 29) < date(1938, 9, 30) < date(1938, 10, 5)
eq("Munich to Churchill", (date(1938, 10, 5) - date(1938, 9, 29)).days, 6)
# Bismarck's speech 30 September 1862
assert date(1862, 9, 30).year == 1862
# Khaldei photograph taken 2 May 1945
assert date(1945, 5, 2) < date(1945, 5, 8)
# Rhodes Colossus cartoon 10 December 1892
assert date(1892, 12, 10).weekday() == 5   # a Saturday: Punch's cover date

# Paper 1 source sets: each group of four sources must stay under 600 words (text and provenance together, the cautious count)
text = Path(__file__).resolve().parent.parent.joinpath("chapters", "hist.skills.sources.md").read_text(encoding="utf-8")
lines = text.split("\n")
groups, cur, i = [], None, 0
while i < len(lines):
    m = re.match(r"^\*\*Source ([A-D])\*\*\s*$", lines[i])
    if m:
        if m.group(1) == "A":
            cur = {"words": 0, "letters": []}
            groups.append(cur)
        i += 1
        paras = []
        buf = []
        while i < len(lines) and not re.match(r"^(\*\*Source [A-D]\*\*|\*\*Question|:::|\*\*What the levels)", lines[i]):
            if lines[i].strip():
                buf.append(lines[i].strip())
            elif buf:
                paras.append(" ".join(buf))
                buf = []
            i += 1
        if buf:
            paras.append(" ".join(buf))
        cur["words"] += sum(len(p.split()) for p in paras)
        cur["letters"].append(m.group(1))
        continue
    i += 1
eq("number of source groups", len(groups), 5)   # Bulow/Kipling, Gilded Age, Russia box, US pair, Munich box
for g in groups:
    assert g["words"] <= 600, f"source set {g['letters']} has {g['words']} words"
print("source groups (words incl. provenance):", [(''.join(g['letters']), g['words']) for g in groups])
print("ok")
