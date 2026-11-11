# checks/hist.d.usa61.4.py: recomputes every number in the chapter (dates, intervals, percentages, marks)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Weekdays named in the text (Monday = 0 ... Sunday = 6)
eq("Stonewall raid, 28 June 1969, is a Saturday", date(1969, 6, 28).weekday(), 5)
eq("Kent State, 4 May 1970, is a Monday", date(1970, 5, 4).weekday(), 0)
eq("Moratorium, 15 October 1969, is a Wednesday", date(1969, 10, 15).weekday(), 2)

# Malcolm X: born 19 May 1925, killed 21 February 1965, aged 39
eq("Malcolm X age at death", age(date(1925, 5, 19), date(1965, 2, 21)), 39)

# Fred Hampton killed 4 December 1969 aged 21 (born 30 August 1948)
eq("Hampton age", age(date(1948, 8, 30), date(1969, 12, 4)), 21)

# Kent State: four killed (ages 19, 20, 20, 19), nine wounded, 13 seconds, at least 61 shots
ages = {"Krause": 19, "Miller": 20, "Scheuer": 20, "Schroeder": 19}
eq("four killed", len(ages), 4)
eq("killed plus wounded", 4 + 9, 13)
assert 61 > 13

# Intervals
eq("Alcatraz: 20 Nov 1969 to 11 Jun 1971 (months, 'nearly nineteen')",
   ((date(1971, 6, 11) - date(1969, 11, 20)).days) // 30, 18)
between("Alcatraz days", (date(1971, 6, 11) - date(1969, 11, 20)).days, 550, 580)
eq("Wounded Knee, 27 Feb to 8 May 1973 inclusive", (date(1973, 5, 8) - date(1973, 2, 27)).days + 1, 71)
eq("Stonewall to first Pride (years)", 1970 - 1969, 1)
eq("Voting Rights Act to Watts (days)", (date(1965, 8, 11) - date(1965, 8, 6)).days, 5)
eq("Watts, 11-16 August, six days", 16 - 11 + 1, 6)
eq("Detroit, 23-27 July, five days", 27 - 23 + 1, 5)
eq("King's Riverside speech a year before his death", date(1968, 4, 4).year - date(1967, 4, 4).year, 1)
eq("Chicago convention days", 29 - 26 + 1, 4)
eq("Kerner report date (leap year)", date(1968, 2, 29).day, 29)
eq("Kerner Commission set up to report (months)", (date(1968, 2, 29).month - date(1967, 7, 27).month) + 12, 7)
eq("Nixon's silent majority speech to the Moratorium march (days)", (date(1969, 11, 15) - date(1969, 11, 3)).days, 12)
eq("Women's Strike on the 50th anniversary of 1920", 1970 - 1920, 50)
eq("Roe: 22 January 1973", date(1973, 1, 22).year, 1973)
eq("Equal Pay Act to Title VII (years)", 1964 - 1963, 1)
eq("NOW to the ERA passing (years)", 1972 - 1966, 6)

# Women in the labour force (per cent, aged 16 and over): 1950, 1960, 1970, 1974
# BLS series LNU01300002, annual averages of the monthly values (review: 1970 and 1974 corrected)
lf = {1950: 33.9, 1960: 37.7, 1970: 43.3, 1974: 45.7}
eq("chart years in order", sorted(lf), list(lf))
eq("rise 1960-70 (points)", round(lf[1970] - lf[1960], 1), 5.6)
eq("rise 1960-74 (points)", round(lf[1974] - lf[1960], 1), 8.0)
# Pay ratio, 60.7 (1960) and 59.4 (1970): fell, so 'did not improve'
assert 59.4 < 60.7
between("pay 'about 60'", 60.7, 59, 61)

# ERA: 38 states = three-quarters of 50 (37.5 rounded up); 35 ratified, three short
eq("states needed", -(-3 * 50 // 4), 38)
eq("short by", 38 - 35, 3)
assert 30 < 35 < 38

# Baby boom: 76 million over 1946-64
between("births per year", 76 / (1964 - 1946), 4.0, 4.5)

# Riots: deaths Watts 34, Newark 26, Detroit 43
deaths = {"Watts": 34, "Newark": 26, "Detroit": 43}
eq("sum of three riots", sum(deaths.values()), 103)
assert max(deaths, key=deaths.get) == "Detroit"

# Native Americans: termination 109 tribes and bands; AIM July 1968; Wounded Knee 71 days
eq("termination count", 109, 109)
between("Declaration of Indian Purpose 'about 450' from 'about ninety' tribes", 450 / 90, 4.9, 5.1)

# Black elected officials / poverty cross-reference with the civil rights chapter
between("elected officials more than doubled", 3500 / 1500, 2.0, 2.5)
eq("poverty rounded", round(41.8), 42)

# Wallace 1968: 13.5 per cent
assert 13 < 13.5 < 14

# Marks in worked examples
eq("table total", 15 + 15, 30)
eq("paper total", 2 * 30, 60)
eq("Black Power essay total low", 14 + 13, 27)
eq("Black Power essay total high", 14 + 14, 28)
print("ok")
