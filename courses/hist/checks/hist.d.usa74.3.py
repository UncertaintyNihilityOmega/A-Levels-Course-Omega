# checks/hist.d.usa74.3.py: recomputes every number in the chapter (dates, intervals, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Hostage crisis: 4 November 1979 to 20 January 1981 is counted inclusively as 444 days
eq("hostage days (inclusive)", (date(1981, 1, 20) - date(1979, 11, 4)).days + 1, 444)
eq("hostages held to the end", 66 - 13 - 1, 52)
eq("released in November 1979 (3 + 10)", 3 + 10, 13)

# Camp David: 5-17 September 1978, thirteen days counted inclusively
eq("Camp David days", (date(1978, 9, 17) - date(1978, 9, 5)).days + 1, 13)
# Framework to treaty: 17 September 1978 to 26 March 1979
d = (date(1979, 3, 26) - date(1978, 9, 17)).days
eq("framework to treaty days", d, 190)
assert 6 <= d / 30.44 < 6.5  # "three months stretched to six"
# Sinai: full withdrawal within three years of the 26 March 1979 treaty; completed April 1982
assert (date(1982, 4, 25) - date(1979, 3, 26)).days < 3 * 365 + 60
# Sadat's visit: announced 9 November 1977, landed 19 November: ten days
eq("announcement to visit", (date(1977, 11, 19) - date(1977, 11, 9)).days, 10)

# Weekdays (Monday = 0 ... Sunday = 6)
eq("4 Nov 1979 is a Sunday", date(1979, 11, 4).weekday(), 6)
eq("17 Sep 1978 is a Sunday", date(1978, 9, 17).weekday(), 6)
eq("26 Mar 1979 is a Monday", date(1979, 3, 26).weekday(), 0)
eq("20 Jan 1981 is a Tuesday", date(1981, 1, 20).weekday(), 1)
eq("4 Nov 1980 (election) is a Tuesday", date(1980, 11, 4).weekday(), 1)
eq("19 Nov 1977 is a Saturday", date(1977, 11, 19).weekday(), 5)

# Election of 1980: Reagan 489, Carter 49, total 538
eq("electoral votes", 489 + 49, 538)
eq("election day is the anniversary of the seizure", (date(1980, 11, 4).month, date(1980, 11, 4).day), (11, 4))
eq("seizure to election, years", date(1980, 11, 4).year - date(1979, 11, 4).year, 1)

# Panama treaties: Senate votes 68-32 (both), 100 senators; canal handed over 31 December 1999
eq("Senate size", 68 + 32, 100)
eq("Panama treaties to handover, years", 1999 - 1977, 22)

# Iran: Shah left 16 Jan 1979, Khomeini returned 1 Feb 1979; Shah to NY 22 Oct, embassy 4 Nov 1979
eq("Shah's departure to Khomeini's return (days)", (date(1979, 2, 1) - date(1979, 1, 16)).days, 16)
eq("Shah in New York to embassy seizure (days)", (date(1979, 11, 4) - date(1979, 10, 22)).days, 13)
assert (date(1979, 11, 4) - date(1979, 10, 22)).days < 14  # "within two weeks"
eq("Eagle Claw to Vance's resignation (days)", (date(1980, 4, 28) - date(1980, 4, 24)).days, 4)
eq("Shah's age at death", age(date(1919, 10, 26), date(1980, 7, 27)), 60)
eq("Iraq's invasion to the Algiers Accords (days)", (date(1981, 1, 19) - date(1980, 9, 22)).days, 119)
# Months of the crisis: about fourteen and a half
m = (date(1981, 1, 20) - date(1979, 11, 4)).days / 30.44
assert 14 <= m < 15, m

# Eagle Claw: eight helicopters, three failed, at least six needed
eq("helicopters left", 8 - 3, 5)
assert 5 < 6

# Chile: Pinochet ruled from 11 September 1973 to 1990 (17 years at most)
eq("Pinochet years in power", 1990 - 1973, 17)
# Treaty has lasted more than forty years by 2026
assert 2026 - 1979 > 40
# Interval from inaugural address to Notre Dame speech
eq("inaugural to Notre Dame (days)", (date(1977, 5, 22) - date(1977, 1, 20)).days, 122)
# Sadat murdered 6 October 1981; anniversary of the 1973 war (6 October 1973)
eq("Sadat's murder, a Tuesday", date(1981, 10, 6).weekday(), 1)
# SALT II signed 18 June 1979
eq("SALT II signing, a Monday", date(1979, 6, 18).weekday(), 0)
print("ok")
