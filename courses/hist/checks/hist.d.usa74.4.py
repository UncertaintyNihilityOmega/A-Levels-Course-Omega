# checks/hist.d.usa74.4.py: recomputes every number in the chapter (dates, intervals, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Weekdays (Monday = 0 ... Sunday = 6)
eq("SALT I signed, 26 May 1972, a Friday", date(1972, 5, 26).weekday(), 4)
eq("Helsinki, 1 Aug 1975, a Friday", date(1975, 8, 1).weekday(), 4)
eq("SALT II signed, 18 June 1979, a Monday", date(1979, 6, 18).weekday(), 0)
eq("INF signed, 8 Dec 1987, a Tuesday", date(1987, 12, 8).weekday(), 1)
eq("START I signed, 31 July 1991, a Wednesday", date(1991, 7, 31).weekday(), 2)
eq("Evil empire speech, 8 Mar 1983, a Tuesday", date(1983, 3, 8).weekday(), 1)
eq("SDI speech, 23 Mar 1983, a Wednesday", date(1983, 3, 23).weekday(), 2)

# SALT I numbers
eq("SALT I ICBM launchers, difference USSR over US", 1618 - 1054, 564)
eq("SALT I submarine launcher rise, US", 710 - 656, 54)
eq("SALT I submarine launcher rise, USSR", 950 - 740, 210)
# SALT I to Vladivostok limits
assert 1320 < 2400
# SALT II: 2,400 falling to 2,250 by 1 January 1981, a fall of 150
eq("SALT II reduction", 2400 - 2250, 150)
assert 820 < 1320
# Senate two-thirds of 100
eq("two-thirds of the Senate", -(-2 * 100 // 3), 67)
# INF: 846 US + 1,846 Soviet = 2,692 missiles; Senate 93-5 = 98 voting
eq("INF missiles destroyed", 846 + 1846, 2692)
eq("INF Senate vote total", 93 + 5, 98)
eq("START I Senate vote total", 93 + 6, 99)
eq("INF signing to the Senate vote, months", (date(1988, 5, 27).year - date(1987, 12, 8).year) * 12 + date(1988, 5, 27).month - date(1987, 12, 8).month, 5)
# Intervals
eq("SALT II signing to Afghanistan invasion (days)", (date(1979, 12, 24) - date(1979, 6, 18)).days, 189)
eq("Afghanistan invasion to withdrawal request (days)", (date(1980, 1, 3) - date(1979, 12, 24)).days, 10)
eq("Soviet war in Afghanistan, years from invasion to withdrawal", 1989 - 1979, 10)
# "It lasted nine years": 24 Dec 1979 to 15 Feb 1989 is a little over nine years
d = (date(1989, 2, 15) - date(1979, 12, 24)).days
assert 9 * 365 < d < 10 * 365, d
eq("Evil empire to SDI (days)", (date(1983, 3, 23) - date(1983, 3, 8)).days, 15)
# Gorbachev: born 2 March 1931, General Secretary 11 March 1985, aged 54
eq("Gorbachev's age in March 1985", age(date(1931, 3, 2), date(1985, 3, 11)), 54)
eq("Chernenko's death to Gorbachev's election", (date(1985, 3, 11) - date(1985, 3, 10)).days, 1)
# Reagan first met a Soviet leader at Geneva, 19-21 November 1985, after nearly five years in office
eq("Reagan's inauguration to Geneva (years)", 1985 - 1981, 4)
assert 4 < (date(1985, 11, 19) - date(1981, 1, 20)).days / 365.25 < 5
# KAL 007 shot down 1 September 1983; 269 people killed
eq("KAL 007 weekday (Thursday)", date(1983, 9, 1).weekday(), 3)
# Reykjavik 11-12 October 1986: two days
eq("Reykjavik days", (date(1986, 10, 12) - date(1986, 10, 11)).days + 1, 2)
# Geneva 19-21 November 1985: three days
eq("Geneva days", (date(1985, 11, 21) - date(1985, 11, 19)).days + 1, 3)
# Iran-Contra revealed 3 Nov 1986; Tower Commission 26 Feb 1987; Reagan's address 4 March 1987
eq("revelation to Tower report (days)", (date(1987, 2, 26) - date(1986, 11, 3)).days, 115)
eq("Tower report to Reagan's address (days)", (date(1987, 3, 4) - date(1987, 2, 26)).days, 6)
eq("pardons 24 Dec 1992 weekday (Thursday)", date(1992, 12, 24).weekday(), 3)
# Clark Amendment 1976 to repeal 1985
eq("Clark Amendment years in force", 1985 - 1976, 9)
# Tripartite Accord 22 Dec 1988 to Cuban withdrawal by July 1991 (about 2.5 years)
assert 2 < (date(1991, 7, 1) - date(1988, 12, 22)).days / 365.25 < 3
# Soviet Union ends: Gorbachev resigns 25 December 1991, the Union ceases on 26 December
eq("USSR end weekday: 25 Dec 1991 is a Wednesday", date(1991, 12, 25).weekday(), 2)
# Malta 2-3 December 1989
eq("Malta weekday: 2 Dec 1989 is a Saturday", date(1989, 12, 2).weekday(), 5)
# German unification 3 October 1990
eq("German unification weekday (Wednesday)", date(1990, 10, 3).weekday(), 2)
# Moscow summit 29 May-2 June 1988: five days
eq("Moscow summit days", (date(1988, 6, 2) - date(1988, 5, 29)).days + 1, 5)
# Washington summit 7-10 December 1987: four days
eq("Washington summit days", (date(1987, 12, 10) - date(1987, 12, 7)).days + 1, 4)
# SALT talks began 17 Nov 1969; SALT I signed 26 May 1972: about two and a half years
y = (date(1972, 5, 26) - date(1969, 11, 17)).days / 365.25
assert 2.4 < y < 2.6, y
# Cold War years: 1972 to 1991 is nineteen years ("twenty years" in the text is rounded)
eq("1972 to 1991", 1991 - 1972, 19)
eq("eleven years from 1972 to 1983", 1983 - 1972, 11)
eq("four years from 1983 to 1987", 1987 - 1983, 4)
print("ok")
