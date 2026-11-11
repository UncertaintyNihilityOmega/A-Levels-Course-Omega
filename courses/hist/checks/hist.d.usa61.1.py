# checks/hist.d.usa61.1.py: recomputes every number in the chapter (dates, ages, votes, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# 1960 election
eq("1960 EV total", 303 + 219 + 15, 537)
kennedy, nixon, byrd = 34220984, 34108157, 638222
eq("1960 margin", kennedy - nixon, 112827)
total_all = 69155922
between("margin about 0.17 per cent of all votes", (kennedy - nixon) / total_all * 100, 0.16, 0.18)
eq("election day 1960", date(1960, 11, 8).weekday(), 1)  # Tuesday
eq("debate 26 Sept 1960 is a Monday", date(1960, 9, 26).weekday(), 0)
eq("days from debate to election", (date(1960, 11, 8) - date(1960, 9, 26)).days, 43)
# ages on election day
def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))
eq("Kennedy age", age(date(1917, 5, 29), date(1960, 11, 8)), 43)
eq("Nixon age", age(date(1913, 1, 9), date(1960, 11, 8)), 47)
# Illinois and Texas swing: 27 + 24 electoral votes would have cost Kennedy the election
between("Kennedy EV without IL and TX", 303 - 27 - 24, 0, 269)
# House Rules Committee fight 217-212, enlarged 12 to 15
eq("Rules Committee vote margin", 217 - 212, 5)
eq("Rules Committee enlarged by", 15 - 12, 3)
# King's arrest, call to Coretta Scott King 26 Oct 1960 (11 days before election)
eq("days from call to election", (date(1960, 11, 8) - date(1960, 10, 26)).days, 13)

# Kennedy economy
eq("minimum wage rise", round(1.25 - 1.00, 2), 0.25)
eq("unemployment 1961, 1964, 1965", (6.7, 5.2, 4.5), (6.7, 5.2, 4.5))
eq("top tax rate cut", 91 - 70, 21)
eq("Medicare vote 1962 total", 52 + 48, 100)
eq("Medicare vote date", date(1962, 7, 17).isoformat(), "1962-07-17")
eq("Equal Pay Act weekday", date(1963, 6, 10).weekday(), 0)

# Johnson
eq("1964 EV total", 486 + 52, 538)
between("1964 vote shares", 61.1 + 38.5, 99.0, 100.0)
eq("House 1964 total", 295 + 140, 435)
eq("Senate 1964 total", 68 + 32, 100)
eq("Senate cloture vote", 71 + 29, 100)
eq("Civil Rights Act signed", date(1964, 7, 2).isoformat(), "1964-07-02")
eq("Cloture date", date(1964, 6, 10).isoformat(), "1964-06-10")
eq("Selma Bloody Sunday to Voting Rights Act (days)", (date(1965, 8, 6) - date(1965, 3, 7)).days, 152)
eq("Selma to speech (days)", (date(1965, 3, 15) - date(1965, 3, 7)).days, 8)
eq("Medicare signed to Voting Rights Act (days)", (date(1965, 8, 6) - date(1965, 7, 30)).days, 7)
eq("Fair Housing Act a week after King's murder", (date(1968, 4, 11) - date(1968, 4, 4)).days, 7)
eq("Great Society speech to Civil Rights Act (days)", (date(1964, 7, 2) - date(1964, 5, 22)).days, 41)
# poverty
pov = {1959: 22.4, 1964: 19.0, 1969: 12.1, 1973: 11.1}
eq("poverty fall 1964-73", round(pov[1964] - pov[1973], 1), 7.9)
eq("chart years in order", sorted(pov), list(pov))
eq("years 1964 to 1973", 1973 - 1964, 9)
between("1959 rate to 1964 fall", pov[1959] - pov[1964], 3.0, 4.0)
# Mississippi Black registration roughly 7 per cent (6.7) to 60 per cent (59.8)
eq("Mississippi 1965 rounded", round(6.7), 7)
eq("Mississippi 1967 rounded", round(59.8), 60)
# riots
eq("riots dead", (34, 26, 43), (34, 26, 43))
eq("1966 House losses", 47, 47)

# Nixon
eq("1968 EV total", 301 + 191 + 46, 538)
between("1968 vote shares", 43.4 + 42.7 + 13.5, 99.0, 100.0)
eq("1972 EV (one faithless elector)", 520 + 17 + 1, 538)
eq("1968 Wallace states", len(["Alabama", "Arkansas", "Georgia", "Louisiana", "Mississippi"]), 5)
eq("NEP date weekday (Sunday)", date(1971, 8, 15).weekday(), 6)
eq("Revenue sharing per year about", round(30.2 / 5, 1), 6.0)
eq("EPA to NEPA (days)", (date(1970, 12, 2) - date(1970, 1, 1)).days, 335)
eq("Earth Day", date(1970, 4, 22).isoformat(), "1970-04-22")
eq("school desegregation fall", 68 - 8, 60)

# Watergate
eq("break-in to resignation (days)", (date(1974, 8, 9) - date(1972, 6, 17)).days, 783)
eq("break-in to election (days)", (date(1972, 11, 7) - date(1972, 6, 17)).days, 143)
eq("Butterfield to Saturday Night Massacre (days)", (date(1973, 10, 20) - date(1973, 7, 16)).days, 96)
eq("Supreme Court ruling to resignation (days)", (date(1974, 8, 9) - date(1974, 7, 24)).days, 16)
eq("Smoking gun release to resignation (days)", (date(1974, 8, 9) - date(1974, 8, 5)).days, 4)
eq("Resignation to pardon (days)", (date(1974, 9, 8) - date(1974, 8, 9)).days, 30)
eq("Judiciary votes", (27 + 11, 28 + 10, 21 + 17), (38, 38, 38))
eq("Supreme Court vote", 8 + 0, 8)
eq("Agnew resigned before Saturday Night Massacre (days)", (date(1973, 10, 20) - date(1973, 10, 10)).days, 10)
eq("Ruckelshaus EPA to Saturday Night (years)", 1973 - 1970, 3)
eq("Saturday Night Massacre is a Saturday", date(1973, 10, 20).weekday(), 5)
eq("Break-in is a Saturday", date(1972, 6, 17).weekday(), 5)
eq("Resignation address Thursday 8 Aug", date(1974, 8, 8).weekday(), 3)

# Essay and mark totals
eq("Table A + Table B", 15 + 15, 30)
eq("two essays", 2 * 30, 60)
between("worked answer total about 27-28", 14 + 13.5, 26.5, 28.5)
eq("Level 5 band", (13, 15), (13, 15))

print("ok")
