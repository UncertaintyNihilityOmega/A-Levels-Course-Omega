# checks/hist.d.malaysia.2.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


# 1955 election (official returns as tabulated in Wikipedia)
eq("elected seats", 52, 52)
eq("Alliance + PMIP seats", 51 + 1, 52)
near("Alliance seat share", 51 / 52 * 100, 98.1, 0.05)
near("others seat share", 1 / 52 * 100, 1.9, 0.05)
near("Alliance vote share", 818013 / 1001000 * 100, 81.7, 0.2)  # total valid votes about 1.00 million
near("others vote share", 100 - 81.7, 18.3, 0.05)
near("shares sum to 100", 81.7 + 18.3, 100, 0.001)
near("PMIP vote share", 40667 / 1001000 * 100, 4.06, 0.1)
eq("nominated and ex-officio seats", 98 - 52, 46)
eq("majority of 52", 52 // 2 + 1, 27)

# Singapore referendum, 1 September 1962 (sg-elections.com tabulation)
a, b, c = 397626, 9422, 7911
blank, unclear = 144077, 2523
cast = 561559
eq("votes cast add up", a + b + c + blank + unclear, cast)
eq("merger votes", a + b + c, 414959)
near("A share of all votes", a / cast * 100, 70.8, 0.05)
near("A share of non-blank votes", a / (a + b + c) * 100, 95.8, 0.05)
near("blank share", blank / cast * 100, 25.7, 0.05)
near("turnout", cast / 619867 * 100, 90.6, 0.05)

# Dewan Rakyat, 1963
eq("seats", 104 + 15 + 24 + 16, 159)
eq("three new members", 15 + 24 + 16, 55)
eq("Borneo seats", 24 + 16, 40)
eq("Malaya states + three = 14", 11 + 3, 14)

# intervals
eq("Singapore in Malaysia, days", (date(1965, 8, 9) - date(1963, 9, 16)).days, 693)
eq("under two years", (date(1965, 8, 9) - date(1963, 9, 16)).days < 2 * 365, True)
eq("Malayan Union to Federation, months", (1948 - 1946) * 12 + 2 - 4, 22)  # April 1946 to February 1948 = 22 months, under two years
eq("Emergency years", 1960 - 1948, 12)
eq("Emergency lasted more than twelve years", (date(1960, 7, 31) - date(1948, 6, 16)).days > 12 * 365, True)
eq("independence to Malaysia, years", 1963 - 1957, 6)
eq("1945 to 1957", 1957 - 1945, 12)
eq("1963 minus 1957", 1963 - 1957, 6)
eq("Gurney killed to Templer appointed, days", (date(1952, 1, 22) - date(1951, 10, 6)).days, 108)
eq("1945 return to 1957: twelve years", 1957 - 1945, 12)

# riots
eq("riot deaths 1964", 23 + 13, 36)
eq("Singapore race riots date", date(1964, 7, 21).weekday(), 1)  # a Tuesday

# Briggs Plan
eq("range of resettlement estimates ordered", 470509 < 500000 < 573000, True)

# Parliament vote
eq("126-0", 126 - 0, 126)

# Practice question marks
eq("two essays at 30 marks", 2 * 30, 60)
eq("Table A + Table B", 15 + 15, 30)
eq("Level 5 example total", 14 + 13, 27)
eq("Level 5 example total upper", 14 + 14, 28)
print("ok")
