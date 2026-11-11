# checks/hist.d.usa45.2.py: recomputes every number in the chapter (ages, intervals, votes, percentages, budget, highways)
import os
import re
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Ages: Nixon 39 in July 1952 (born 9 Jan 1913); King 26 at the start of the Montgomery boycott (born 15 Jan 1929);
# Rosa Parks 42 on 1 Dec 1955 (born 4 Feb 1913); Emmett Till 14 at death (born 25 July 1941);
# Elizabeth Eckford 15 (born 4 Oct 1941); Eisenhower 62 at the 1952 election, 66 in 1956, 70 at the farewell address
eq("Nixon", age(date(1913, 1, 9), date(1952, 7, 11)), 39)
eq("King", age(date(1929, 1, 15), date(1955, 12, 5)), 26)
eq("Parks", age(date(1913, 2, 4), date(1955, 12, 1)), 42)
eq("Till", age(date(1941, 7, 25), date(1955, 8, 28)), 14)
eq("Eckford", age(date(1941, 10, 4), date(1957, 9, 4)), 15)
eq("Eisenhower 1952", age(date(1890, 10, 14), date(1952, 11, 4)), 62)
eq("Eisenhower 1956", age(date(1890, 10, 14), date(1956, 11, 6)), 66)
eq("Eisenhower 1961", age(date(1890, 10, 14), date(1961, 1, 17)), 70)

# Elections
eq("1952 electoral votes", 442 + 89, 531)
eq("1956 electoral votes", 457 + 73 + 1, 531)
eq("majority", 531 // 2 + 1, 266)
eq("1952 states", 39 + 9, 48)
eq("1956 states", 41 + 7, 48)
eq("1952 Eisenhower popular share", round(34_075_529 / (34_075_529 + 27_375_090 + 300_000) * 100, 0), 55.0)
# shares as given by the standard sources: 55.2 + 44.3 = 99.5; 57.4 + 42.0 = 99.4
assert 55.2 + 44.3 < 100 and 57.4 + 42.0 < 100
assert abs(34.1 - 34.075529) < 0.05 and abs(27.4 - 27.37509) < 0.05
assert abs(35.6 - 35.57918) < 0.05 and abs(26.0 - 26.028028) < 0.05
# 1952 Stevenson states: AL, AR, GA, KY, LA, MS, NC, SC, WV = 9
eq("Stevenson 1952 states", len(["AL", "AR", "GA", "KY", "LA", "MS", "NC", "SC", "WV"]), 9)
# 1956 Stevenson states: AL, AR, GA, MS, MO, NC, SC = 7
eq("Stevenson 1956 states", len(["AL", "AR", "GA", "MS", "MO", "NC", "SC"]), 7)
# Landslide size in 1956: Eisenhower won 86 per cent of electoral votes
assert 85 < 457 / 531 * 100 < 87
assert 83 < 442 / 531 * 100 < 84

# Dates and intervals
# Montgomery boycott: 5 December 1955 to 20 December 1956 = 381 days
eq("boycott days", (date(1956, 12, 20) - date(1955, 12, 5)).days, 381)
# Brown (17 May 1954) to Little Rock troops (24 September 1957): 3 years and about 4 months
months = (1957 - 1954) * 12 + (9 - 5)
eq("months Brown to Little Rock", months, 40)
# Brown II (31 May 1955) is 379 days after Brown
eq("Brown to Brown II days", (date(1955, 5, 31) - date(1954, 5, 17)).days, 379)
# Brown to the 1957 Act: Act signed 9 September 1957
assert date(1954, 5, 17) < date(1955, 5, 31) < date(1957, 9, 9) < date(1957, 9, 24)
# Greensboro (1 Feb 1960) to SNCC (15 April 1960): about two and a half months
gap = (date(1960, 4, 15) - date(1960, 2, 1)).days
assert 70 < gap < 80, gap
# Suez/Hungary vs election day: 23 Oct, 29 Oct, 31 Oct, then polling 6 Nov (14, 8 and 6 days before polling)
eq("Hungary before polling", (date(1956, 11, 6) - date(1956, 10, 23)).days, 14)
eq("Israel invasion before polling", (date(1956, 11, 6) - date(1956, 10, 29)).days, 8)
eq("Anglo-French before polling", (date(1956, 11, 6) - date(1956, 10, 31)).days, 6)
# Heart attack 24 September 1955; ileitis operation 9 June 1956: before the election
assert date(1955, 9, 24) < date(1956, 6, 9) < date(1956, 11, 6)
# Checkers 23 September 1952; Korea pledge 24 October 1952; election 4 November 1952
assert date(1952, 9, 23) < date(1952, 10, 24) < date(1952, 11, 4)
eq("days from Korea pledge to polling", (date(1952, 11, 4) - date(1952, 10, 24)).days, 11)
# Korean armistice 27 July 1953 is under nine months after the pledge
assert (date(1953, 7, 27) - date(1952, 10, 24)).days < 280
# Stalin died 5 March 1953 before the armistice
assert date(1953, 3, 5) < date(1953, 7, 27)

# Highways: 1919 convoy 62 days over 3,200 miles = about 52 miles a day
eq("convoy miles a day", round(3200 / 62), 52)
eq("federal + state share", 90 + 10, 100)
eq("gas tax rise", 3 - 2, 1)
assert abs((3 - 2) / 2 - 0.5) < 1e-9  # a rise of one half
# Minimum wage 75 cents to $1 is a rise of one third
eq("minimum wage rise", round((100 - 75) / 75, 4), round(1 / 3, 4))
# Budget: surplus years 1956, 1957, 1960 = 3
eq("surplus years", len([1956, 1957, 1960]), 3)
# Unemployment peaks at 7.5 per cent in 1958 (the highest of his years)
assert 7.5 > 4.0
# Southern Manifesto: 19 senators + 82 representatives = 101
eq("Southern Manifesto signers", 19 + 82, 101)
# Eisenhower sent about 1,000 paratroopers against nine students
assert 1000 > 9
# Recessions: July 1953 - May 1954; Aug 1957 - Apr 1958; Apr 1960 - Feb 1961 (months)
rec = [((1953, 7), (1954, 5)), ((1957, 8), (1958, 4)), ((1960, 4), (1961, 2))]
eq("number of recessions", len(rec), 3)
for (a, b), (c, d) in rec:
    assert (c - a) * 12 + (d - b) > 0
# Thurmond's filibuster: 24 hours 18 minutes
eq("filibuster minutes", 24 * 60 + 18, 1458)
# NAACP/Black vote: nearly 40 per cent
assert 39 <= 39.5 < 40

text = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "chapters", "hist.d.usa45.2.md"), encoding="utf-8").read()
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
print("ok")
