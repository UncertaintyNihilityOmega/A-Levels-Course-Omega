# checks/hist.exam.p4.py: recomputes every number in the chapter (paper facts, level ranges, mark totals, timing, dates, figures in the worked examples)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 4: two essays of 30 = 60 marks; each 30 = Table A 15 (AO2) + Table B 15 (AO1); 1 h 45 min = 105 min
eq("marks per essay", 15 + 15, 30)
eq("total marks", 2 * 30, 60)
eq("paper minutes", 1 * 60 + 45, 105)
eq("AO split", 50 + 50, 100)
# Specimen: three sections of three questions each = nine questions; the old paper had four per section = twelve
eq("specimen questions", 3 * 3, 9)
eq("old paper questions", 3 * 4, 12)
# Choice: two of three
eq("questions answered", 2, 2)

# Suggested plan: 6 + 46 + 46 + 7 = 105; each question 4 + 42 = 46
eq("time plan", 6 + 46 + 46 + 7, 105)
eq("per question", 4 + 42, 46)
eq("total writing time", 2 * 42, 84)

# Table A and Table B: five levels, top 15, contiguous
A = {5: (13, 15), 4: (10, 12), 3: (7, 9), 2: (4, 6), 1: (1, 3)}
prev = 16
for lvl in (5, 4, 3, 2, 1):
    lo, hi = A[lvl]
    eq(f"Table level {lvl} contiguous", hi, prev - 1)
    prev = lo
eq("Table bottom", prev, 1)

# Both tables at the same level: totals out of 30
want = {5: (26, 30), 4: (20, 24), 3: (14, 18), 2: (8, 12), 1: (2, 6)}
for lvl, (lo, hi) in A.items():
    eq(f"both tables at level {lvl}", (2 * lo, 2 * hi), want[lvl])
# Mixed: Table A level 2 (4-6) + Table B level 4 (10-12)
eq("A2 + B4", (4 + 10, 6 + 12), (14, 18))
# Quiz: Table A level 4 (10-12) + Table B level 5 (13-15)
eq("A4 + B5", (10 + 13, 12 + 15), (23, 27))

# Worked example 1 (Malaya): marks of each version
eq("L2 total", 5 + 5, 10)
assert 8 <= 10 <= 12
eq("L3 total", 8 + 8, 16)
assert 14 <= 16 <= 18
eq("L4 total", 11 + 11, 22)
assert 20 <= 22 <= 24
eq("L5 total", 14 + 13, 27)
assert 26 <= 27 <= 30
assert 13 <= 14 <= 15 and 13 <= 13 <= 15

# Malaya facts (from the topic chapter)
eq("Alliance seats", 51 + 1, 52)
eq("share of seats", round(51 / 52 * 100, 1), 98.1)
eq("KL municipal election seats won", 9 / 12, 0.75)
eq("London talks length (days)", (date(1956, 2, 6) - date(1956, 1, 18)).days, 19)
eq("election to talks (months)", (1956 - 1955) * 12 + (1 - 7), 6)
eq("Merdeka after the talks (days)", (date(1957, 8, 31) - date(1956, 2, 6)).days, 572)
eq("Emergency ended after independence (days)", (date(1960, 7, 31) - date(1957, 8, 31)).days, 1065)
assert date(1960, 7, 31) > date(1957, 8, 31)
eq("Emergency start to Merdeka (years)", 1957 - 1948, 9)
eq("Briggs plan to Merdeka (years)", 1957 - 1950, 7)
eq("MCA founded to Merdeka (years)", 1957 - 1949, 8)
eq("India 1947 to Merdeka", 1957 - 1947, 10)

# Stalin figures (from the topic chapter): 353,074 + 328,618 = 681,692 shot in 1937-38
eq("shot 1937-38", 353074 + 328618, 681692)
# Order 00447 quotas: 75,950 to be shot, 193,000 to the camps
eq("00447 quotas", 75950 + 193000, 268950)
share = 681692 / 160_000_000
assert 0.004 < share < 0.005, share
# Stalin dates: Stakhanov 30-31 Aug 1935; Order 00447 30 July 1937
eq("Stakhanov to Order 00447 (years)", 1937 - 1935, 2)
eq("1.6 million arrested, about 680,000 shot: share shot", round(681692 / 1_600_000 * 100), 43)

# Words in the Level 5 essay
text = open("chapters/hist.exam.p4.md", encoding="utf-8").read()
a = text.index('"Malaya became independent on 31 August 1957, peacefully'); b = text.index("*Commentary.* The introduction sets **criteria**")
n = len(text[a:b].split())
assert 640 <= n <= 760, n
assert "About 700 words" in text
print("ok")
