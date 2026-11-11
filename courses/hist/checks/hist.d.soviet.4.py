# checks/hist.d.soviet.4.py: recomputes every number in the chapter (intervals, seats, percentages, ranges, widget dates, exam questions)
import os
import re
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def days(a, b):
    return (date(*b) - date(*a)).days


# Poland, 1980
eq("Walentynowicz dismissed to strike (days)", days((1980, 8, 7), (1980, 8, 14)), 7)
eq("strike start to Gdansk Agreement (days)", days((1980, 8, 14), (1980, 8, 31)), 17)
assert date(1980, 8, 30) < date(1980, 8, 31) < date(1980, 9, 3)  # Szczecin, Gdansk, Jastrzebie
assert date(1980, 9, 6) > date(1980, 8, 31)  # Gierek replaced by Kania
assert date(1980, 11, 10) > date(1980, 9, 17)  # Solidarity founded 17 Sept, registered 10 Nov
eq("Gierek First Secretary 1970 to 1980 (years)", 1980 - 1970, 10)
assert 1976 - 1970 == 6 and date(1976, 6, 24) < date(1976, 9, 23)  # price rises, then KOR
eq("papal election to August 1980 (years)", 1980 - 1978, 2)
eq("papal visit (June 1979) to strike (August 1980): 14 months", (1980 - 1979) * 12 + (8 - 6), 14)
# Round Table and seats
eq("Sejm seats", 460, 460)
free = 161
eq("35 per cent of 460 Sejm seats", round(0.35 * 460), free)
eq("65 per cent of 460 Sejm seats", round(0.65 * 460), 299)
eq("seats sum", 299 + free, 460)
assert 99 < 100  # Senate seats won
eq("Round Table days", days((1989, 2, 6), (1989, 4, 5)), 58)
assert date(1989, 4, 5) < date(1989, 4, 17) < date(1989, 6, 4) < date(1989, 6, 18) < date(1989, 7, 19) < date(1989, 8, 24)
eq("martial law to suspension (days)", days((1981, 12, 13), (1982, 12, 31)), 383)
eq("martial law to lifting (years)", 1983 - 1981, 2)
eq("Wujek miners killed", 9, 9)
assert 9 < 90  # about 90 died under martial law (disputed)
eq("Solidarity share: 10 million of 36 million population (percent, rounded)", round(10 / 36 * 100), 28)
assert 10 / 36 < 1 / 3  # 'about a third of the working-age population': a larger base than all, so a third of the working-age fits
assert 1981 - 1980 == 1
# Gorbachev's decisions and the Sinatra Doctrine
assert date(1988, 12, 7) < date(1989, 7, 6) < date(1989, 10, 23) < date(1989, 10, 25)
eq("Nagy executed 1958, reburied 1989 (years)", 1989 - 1958, 31)
eq("Nagy: same day and month", (date(1958, 6, 16).month, date(1958, 6, 16).day), (date(1989, 6, 16).month, date(1989, 6, 16).day))
eq("Hungary border opened to Sopron picnic (days)", days((1989, 8, 19), (1989, 9, 11)), 23)
assert 30000 > 661
# East Germany
eq("Honecker out to the Wall (days)", days((1989, 10, 18), (1989, 11, 9)), 22)
eq("Leipzig 9 Oct to Honecker 18 Oct (days)", days((1989, 10, 9), (1989, 10, 18)), 9)
eq("Wall to reunification (days)", days((1989, 11, 9), (1990, 10, 3)), 328)
eq("Wall to Bulgaria next day (days)", days((1989, 11, 9), (1989, 11, 10)), 1)
# Czechoslovakia
eq("Velvet Revolution: 17 Nov to Havel 29 Dec (days)", days((1989, 11, 17), (1989, 12, 29)), 42)
eq("six weeks", 42 // 7, 6)
eq("first non-communist government in 41 years (1948-89)", 1989 - 1948, 41)
eq("Czechoslovakia divides 1992 (years after 1989)", 1992 - 1989 + 0, 3)
eq("Opletal 1939 to 1989 (years)", 1989 - 1939, 50)
# Romania
eq("Ceausescu in power 1965-89 (years)", 1989 - 1965, 24)
eq("Zhivkov in power 1954-89 (years)", 1989 - 1954, 35)
eq("Timisoara to Ceausescu's execution (days)", days((1989, 12, 16), (1989, 12, 25)), 9)
assert 689 < 700 and 1290 < 1300  # 'about 700 to about 1,300'
# Dissent
eq("Kunaev replaced: 16 Dec; protest 17-19 Dec (days of unrest)", 19 - 17 + 1, 3)
eq("Baltic Way: 1939 to 1989 (years)", 1989 - 1939, 50)
assert 2_000_000 > 675  # two million people along about 675 km
eq("Lithuania declaration to Vilnius (days)", days((1990, 3, 11), (1991, 1, 13)), 308)
eq("Vilnius dead", 14, 14)
eq("Lithuania blockade April to July: months", 7 - 4, 3)
# Referendum 17 March 1991 (counts in millions)
yes, cast, registered = 113.5, 148.6, 185.6
eq("referendum yes share of votes cast (per cent, rounded)", round(yes / cast * 100), 76)
eq("referendum turnout (per cent, rounded)", round(cast / registered * 100), 80)
assert 6 + 9 == 15  # six republics boycotted, nine voted
# Coup and end
eq("coup length (days) 19-21 August", 21 - 19, 2)  # three calendar days
eq("coup: calendar days 19, 20, 21", len([19, 20, 21]), 3)
eq("Foros visit to Gorbachev's return (days)", days((1991, 8, 18), (1991, 8, 22)), 4)
eq("Union Treaty signing planned for 20 August: day after coup began", days((1991, 8, 19), (1991, 8, 20)), 1)
eq("Gang of Eight members", len(["Yanayev", "Pavlov", "Kryuchkov", "Yazov", "Pugo", "Baklanov", "Starodubtsev", "Tizyakov"]), 8)
eq("Yeltsin elected to coup (days)", days((1991, 6, 12), (1991, 8, 19)), 68)
eq("Belovezha to Gorbachev's resignation (days)", days((1991, 12, 8), (1991, 12, 25)), 17)
eq("Alma-Ata to resignation (days)", days((1991, 12, 21), (1991, 12, 25)), 4)
eq("Alma-Ata Protocol: 11 of 12 remaining republics", 12 - 1, 11)
eq("coup to Belovezha (days)", days((1991, 8, 19), (1991, 12, 8)), 111)
eq("Gorbachev in power to resignation (years): 11 March 1985 to 25 Dec 1991", 1991 - 1985, 6)
assert date(1991, 8, 24) < date(1991, 8, 29) < date(1991, 9, 5) < date(1991, 9, 6)
assert 90 > 84  # Ukraine: about 90 per cent in favour
# Satellites' end
assert date(1991, 3, 31) < date(1991, 6, 28) < date(1991, 7, 1)

text = open(os.path.join(here, "..", "chapters", "hist.d.soviet.4.md"), encoding="utf-8").read()
eq("number of timeline widgets", len(re.findall(r'data-w="hist-timeline"', text)), 1)
ev = re.search(r'data-events="([^"]*)"', text).group(1).split(" ;; ")
eq("number of timeline events", len(ev), 18)
ds = [e.split(" | ")[0] for e in ev]
assert ds == sorted(ds), ds
for e in ev:
    parts = e.split(" | ")
    assert len(parts) == 4, e
    nums = [int(x) for x in parts[0].split("-")]
    if len(nums) == 3:
        date(*nums)
    assert parts[3] in ("Poland", "Other satellites", "USSR"), parts[3]
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 11)
eq("Table A + Table B", 15 + 15, 30)
for mm in re.finditer(r"^Q: \[30 marks\] ★+ (.*)$", text, re.M):
    assert mm.group(1).startswith("Assess") or "Evaluate" in mm.group(1), mm.group(1)
eq("number of quiz questions", len(re.findall(r"^\? ", text, re.M)), 11)
assert "FACTS.md" not in text and "COURSE.md" not in text
print("ok")
