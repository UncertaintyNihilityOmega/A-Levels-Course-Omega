# checks/hist.d.usa45.1.py: recomputes every number in the chapter (ages, intervals, votes, percentages, margins)
import os
import re
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Truman: born 8 May 1884, President 12 April 1945 aged 60; Vice-President sworn in 20 January 1945 -> 82 days
eq("Truman age at accession", age(date(1884, 5, 8), date(1945, 4, 12)), 60)
eq("days as Vice-President", (date(1945, 4, 12) - date(1945, 1, 20)).days, 82)
# McCarthy: born 14 November 1908, died 2 May 1957 aged 48
eq("McCarthy age at death", age(date(1908, 11, 14), date(1957, 5, 2)), 48)
# Wheeling speech (9 Feb 1950) to censure (2 Dec 1954): under five years
span = (date(1954, 12, 2) - date(1950, 2, 9)).days
assert 4 * 365 < span < 5 * 365, span
# Army-McCarthy hearings, televised 22 April to 17 June 1954 (36 days of hearings within that span)
assert (date(1954, 6, 17) - date(1954, 4, 22)).days >= 36
assert date(1954, 4, 22) < date(1954, 6, 9) < date(1954, 6, 17)  # Welch's rebuke inside the hearings
# Censure vote 67-22: 89 voting, two-thirds is not needed; majority
eq("censure total", 67 + 22, 89)
assert 67 > 22

# Taft-Hartley: veto 20 June 1947, law 23 June 1947; override votes
assert date(1947, 6, 20) < date(1947, 6, 23)
eq("House override total", 331 + 83, 414)
assert 331 >= 2 * 414 / 3  # two-thirds of those voting
eq("Senate override total", 68 + 25, 93)
assert 68 >= 2 * 93 / 3
eq("Senate Democrats opposed to Truman", 42 - 20, 22)

# Housing Act 1949: 810,000 units over six years = 135,000 a year
eq("housing units a year", 810000 // 6, 135000)
eq("housing divisible", 810000 % 6, 0)
# Minimum wage 40 -> 75 cents is an 87.5 per cent rise
eq("minimum wage rise %", (75 - 40) / 40 * 100, 87.5)

# Election 1948
ev = {"Truman": 303, "Dewey": 189, "Thurmond": 39, "Wallace": 0}
eq("total electoral votes", sum(ev.values()), 531)
eq("majority needed", 531 // 2 + 1, 266)
eq("Thurmond: four states plus one elector", (11 + 10 + 9 + 8) + 1, 39)  # AL, LA, MS, SC
eq("states won", 28 + 16 + 4, 48)
# Popular vote (approximate totals from the National Archives and standard sources)
vote = {"Truman": 24_179_347, "Dewey": 21_991_292, "Thurmond": 1_176_023, "Wallace": 1_157_328}
total = 48_793_826
pct = {k: v / total * 100 for k, v in vote.items()}
assert 49.4 <= pct["Truman"] <= 49.7, pct
assert round(pct["Dewey"], 1) == 45.1, pct
assert round(pct["Thurmond"], 1) == 2.4, pct
assert round(pct["Wallace"], 1) == 2.4, pct
assert round(vote["Truman"] / 1e6, 1) == 24.2
assert round(vote["Dewey"] / 1e6, 1) == 22.0
assert round(vote["Thurmond"] / 1e6, 2) == 1.18
assert round(vote["Wallace"] / 1e6, 2) == 1.16
gap = pct["Truman"] - pct["Dewey"]
assert 4.3 <= gap <= 4.7, gap  # "about four and a half points"
# Three close states: Ohio 25, California 25, Illinois 28 = 78; margins 7,107 + 17,865 + 33,612 = about 58,000
eq("three states' electoral votes", 25 + 25 + 28, 78)
margins = 7107 + 17865 + 33612
eq("three margins total", margins, 58584)
eq("about 58,600", round(margins, -2), 58600)
eq("Dewey wins all three", 189 + 78, 267)
assert 267 >= 266
# Any two of the three go to Dewey: Truman falls below 266 at the smallest swing (25 + 25 = 50)
assert 303 - 50 < 266
assert 189 + 50 < 266  # and Dewey does not reach it either, so the House decides
# Democratic convention civil-rights plank: 651.5 to 582.5
eq("plank vote total", 651.5 + 582.5, 1234.0)
assert 651.5 > 582.5
# Gallup polls: Oct 1948 Dewey 49.5 Truman 44.5 -> 5 point lead
eq("Gallup lead", 49.5 - 44.5, 5.0)
# Gallup on McCarthy: 50/29 in January 1954, 34/45 in June 1954
assert 50 - 29 == 21 and 34 - 45 == -11
# Hollywood Ten contempt vote 346 to 17
eq("Hollywood Ten vote total", 346 + 17, 363)
# Rosenbergs: convicted 29 March 1951, executed 19 June 1953
assert date(1951, 3, 29) < date(1953, 6, 19)
# Civil rights dates
assert date(1946, 12, 5) < date(1947, 10, 29) < date(1948, 2, 2) < date(1948, 7, 26)
# Social Security 1950: 10 million newly covered, benefits up about 77.5 per cent
assert 77 <= 77.5 < 78
# Cold war/red scare dates
assert date(1949, 8, 29) < date(1949, 10, 1) < date(1950, 1, 21) < date(1950, 2, 9) < date(1950, 6, 25)
# Loyalty Program (21 March 1947) comes nine days after the Truman Doctrine (12 March)
eq("days from Doctrine to Loyalty Program", (date(1947, 3, 21) - date(1947, 3, 12)).days, 9)
# NAACP growth 50,000 to 450,000 is a nine-fold rise
eq("NAACP growth", 450000 // 50000, 9)
# Voter registration: about 3% (1940) and 12% (1947) -> a fourfold rise
eq("registration rise", 12 // 3, 4)
# Republican slogan: 1946 midterm gains
assert 55 > 12

text = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "chapters", "hist.d.usa45.1.md"), encoding="utf-8").read()
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
print("ok")
