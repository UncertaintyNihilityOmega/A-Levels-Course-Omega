# checks/hist.exam.p3.py: recomputes every number in the chapter (paper facts, level ranges, mark totals, timing, dates, word counts)
import re
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 3: 1 h 15 min = 75 min; 40 marks = 20 (Table A, AO4) + 20 (Table B, AO1); AO split 50/50
eq("paper minutes", 1 * 60 + 15, 75)
eq("total marks", 20 + 20, 40)
eq("AO split", 50 + 50, 100)
eq("minutes per mark", round(75 / 40, 3), 1.875)

# Suggested plan: 15 + 10 + 50 = 75
eq("time plan", 15 + 10 + 50, 75)

# Table A and Table B: six levels, top 20, contiguous
A = {6: (18, 20), 5: (15, 17), 4: (12, 14), 3: (9, 11), 2: (5, 8), 1: (1, 4)}
prev = 21
for lvl in (6, 5, 4, 3, 2, 1):
    lo, hi = A[lvl]
    eq(f"Table level {lvl} contiguous", hi, prev - 1)
    prev = lo
eq("Table bottom", prev, 1)

# Both tables at the same level: totals out of 40
want = {6: (36, 40), 5: (30, 34), 4: (24, 28), 3: (18, 22), 2: (10, 16), 1: (2, 8)}
for lvl, (lo, hi) in A.items():
    eq(f"both tables at level {lvl}", (2 * lo, 2 * hi), want[lvl])

# Mixed: Table A level 5 (15-17) + Table B level 3 (9-11)
eq("A5 + B3", (15 + 9, 17 + 11), (24, 28))
# Quiz: Table A level 6 (18-20) + Table B level 4 (12-14)
eq("A6 + B4", (18 + 12, 20 + 14), (30, 34))
# Level 6 worked answer: Table A 19 + Table B 18 = 37 (inside 36-40); level 2 answer 8 + 6 = 14 inside 10-16
eq("worked L6 total", 19 + 18, 37)
assert 36 <= 37 <= 40
eq("worked L2 total", 7 + 7, 14)
assert 10 <= 14 <= 16
eq("worked L3 total", 10 + 10, 20)
assert 18 <= 20 <= 22
eq("worked L4 total", 13 + 13, 26)
assert 24 <= 26 <= 28
eq("worked L5 total", 16 + 16, 32)
assert 30 <= 32 <= 34
# weak paragraph: Table A level 3 (9-11), Table B level 4 (12-14)
assert 9 <= 10 <= 11 and 12 <= 13 <= 14

# Dates in the knowledge lists (day-of-week sanity and intervals)
# the Berlin Blockade lasted 24 June 1948 to 12 May 1949: 322 days from first to last day
eq("Berlin Blockade length (days)", (date(1949, 5, 12) - date(1948, 6, 24)).days, 322)
# Ultimatum 23 July 1914 expired 48 hours later: 25 July
eq("ultimatum deadline", date(1914, 7, 23).toordinal() + 2, date(1914, 7, 25).toordinal())
# Sarajevo to the blank cheque (28 June to 5 July): 7 days
eq("Sarajevo to blank cheque", (date(1914, 7, 5) - date(1914, 6, 28)).days, 7)
# Sarajevo to Britain's entry (28 June to 4 August): 37 days
eq("Sarajevo to Britain's war", (date(1914, 8, 4) - date(1914, 6, 28)).days, 37)
# Potsdam 17 July to 2 August 1945: 16 days
eq("Potsdam length", (date(1945, 8, 2) - date(1945, 7, 17)).days, 16)
# Yalta 4-11 February 1945: 7 days
eq("Yalta length", (date(1945, 2, 11) - date(1945, 2, 4)).days, 7)
# Treaty of Versailles signed 28 June 1919: five years to the day after Sarajevo
eq("Versailles and Sarajevo", date(1919, 6, 28).year - date(1914, 6, 28).year, 5)
# Entente Cordiale 1904, Anglo-Russian Convention 1907, Triple Alliance 1882
eq("Entente to Convention", 1907 - 1904, 3)
eq("Triple Alliance to war", 1914 - 1882, 32)
# Fischer 1961; centenary of the war 2014: 100 years after 1914
eq("centenary", 1914 + 100, 2014)
# the Weekday of 28 June 1914 was a Sunday; 28 July 1914 was a Tuesday
eq("Sarajevo weekday", date(1914, 6, 28).weekday(), 6)
eq("28 July 1914 weekday", date(1914, 7, 28).weekday(), 1)
# Crises settled in 1906, 1909, 1911, 1913 (the extract lists 1905, 1908, 1911, 1913 as crisis years)
eq("Bosnian crisis span", 1909 - 1908, 1)

# Word counts in the worked example (extract about 200; Level 6 answer about 600)
text = open("chapters/hist.exam.p3.md", encoding="utf-8").read()
i = text.index("It has become a habit"); j = text.index("**Plan (ten minutes)")
n_extract = len(text[i:j].split())
assert 190 <= n_extract <= 210, n_extract
a = text.index('"The extract argues one thing in two linked ways'); b = text.index("*Commentary.* The first paragraph states the **whole**")
n_answer = len(text[a:b].split())
assert 580 <= n_answer <= 620, n_answer
# the chapter says so
assert "about 200 words" in text and "About 600 words" in text

# Quiz: three levels of Paper 3 questions are 20 + 20 and 1 + 1 + 1 questions in the specimen
eq("specimen questions", 3 * 1, 3)
print("ok")
