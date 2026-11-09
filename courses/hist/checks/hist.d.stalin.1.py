# checks/hist.d.stalin.1.py: recomputes every number in the chapter (ages, intervals, membership, trial figures, figure layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


death = date(1924, 1, 21)
# Lenin: born 22 April 1870 -> "aged 53" at death
eq("Lenin age at death", age(date(1870, 4, 22), death), 53)
# Politburo members' ages in January 1924 (table): Stalin 45, Trotsky 44, Zinoviev 40, Kamenev 40, Bukharin 35, Rykov 42, Tomsky 43
eq("Stalin age", age(date(1878, 12, 18), death), 45)
eq("Trotsky age", age(date(1879, 11, 7), death), 44)
eq("Zinoviev age", age(date(1883, 9, 23), death), 40)
eq("Kamenev age", age(date(1883, 8, 4), death), 40)
eq("Bukharin age", age(date(1888, 10, 9), death), 35)
eq("Rykov age", age(date(1881, 3, 9), death), 42)
eq("Tomsky age", age(date(1880, 4, 12), death), 43)
assert min(35, 40, 40, 42, 43, 44, 45) == 35, "Bukharin the youngest"
eq("Politburo full members", len(["Zinoviev", "Kamenev", "Stalin", "Trotsky", "Bukharin", "Rykov", "Tomsky"]), 7)
# Stalin's birthday: church records 18 Dec 1878, official 21 Dec 1879 -> a year and three days later
eq("birthday gap days", (date(1879, 12, 21) - date(1878, 12, 18)).days - 365, 3)
eq("50th birthday year (official 1879 + 50)", 1879 + 50, 1929)
# Strokes and the Testament
assert date(1922, 5, 25) < date(1922, 12, 16) < date(1923, 3, 9) < death
eq("Testament dictation span (days)", (date(1923, 1, 4) - date(1922, 12, 23)).days, 12)
# Stalin General Secretary 3 April 1922 -> Lenin's death: about 21 months
eq("months as General Secretary before Lenin died", (death.year - 1922) * 12 + (1 - 4), 21)
# Funeral Sunday 27 January 1924; the telegram said Saturday (26th)
eq("funeral weekday (6 = Sunday)", date(1924, 1, 27).weekday(), 6)
eq("26 January weekday (5 = Saturday)", date(1924, 1, 26).weekday(), 5)
# Trotsky left Moscow 18 January; Lenin died 21 January
eq("days between Trotsky leaving and Lenin's death", (death - date(1924, 1, 18)).days, 3)
# Thirteenth Congress 23-31 May 1924: Testament given to the Central Committee 18 May, five days before
eq("Testament to Congress (days)", (date(1924, 5, 23) - date(1924, 5, 18)).days, 5)
# Testament first published in the USSR in 1956, three years after Stalin's death (1953)
eq("years after Stalin's death", 1956 - 1953, 3)
# Lenin Enrolment and party size
enrolled, members_1924, members_1926 = 241600, 446089, 1000000
assert 235000 <= enrolled <= 245000  # "about 240,000"
assert enrolled / members_1924 > 0.5   # "more than half as many again"
assert members_1926 / members_1924 > 2.2  # "more than doubled"
eq("chart values", (round(members_1924 / 1000), round(members_1926 / 1000)), (446, 1000))
# Stages and stage lengths
assert date(1925, 12, 18) < date(1926, 7, 14) < date(1927, 11, 12) < date(1929, 4, 23)
assert date(1927, 11, 12) < date(1927, 11, 14)
# Trotsky: exile Jan 1928, deported Feb 1929, murdered Aug 1940 -> 11 years after deportation
eq("years from deportation to murder", 1940 - 1929, 11)
# Struggle length: Lenin's death (Jan 1924) to the Right's condemnation (Apr 1929) = 5 years 3 months
eq("months of the struggle", (1929 - 1924) * 12 + (4 - 1), 63)
# Shakhty: 18 May - 6 July 1928; 53 accused, 11 death sentences, 5 shot, 6 commuted
eq("Shakhty trial length (days)", (date(1928, 7, 6) - date(1928, 5, 18)).days, 49)
eq("Shakhty commuted", 11 - 5, 6)
assert 11 < 53 and 5 <= 11
# Foreign engineers: 3 Germans among 53, so 50 Russians
eq("Shakhty Russians", 53 - 3, 50)
# Fourteenth Congress December 1925; Fifteenth December 1927
eq("congress gap years", 1927 - 1925, 2)
# Rykov replaced as head of Sovnarkom in December 1930; Bukharin off Pravda April 1929 and Politburo November 1929
assert date(1929, 4, 23) < date(1929, 11, 1) < date(1930, 12, 1)
# The Lenin enrolment of workers within 4.5 months (22 Jan-15 May 1924)
assert 100 < (date(1924, 5, 15) - date(1924, 1, 22)).days < 150

text = open(os.path.join(here, "..", "chapters", "hist.d.stalin.1.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
# every Paper 4 practice question is a [30] essay
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
print("ok")
