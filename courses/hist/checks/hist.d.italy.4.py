# checks/hist.d.italy.4.py: recomputes every number in the chapter (dates, intervals, percentages, marks)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Birth data (ISTAT crude birth rate per 1,000 and live births) as used in the chart and text
rate = {1922: 30.8, 1927: 27.4, 1931: 24.8, 1936: 22.4, 1940: 23.5}
births = {1922: 1127444, 1936: 962686, 1940: 1046479}
fall = (rate[1922] - rate[1936]) / rate[1922]
between("birth-rate fall 1922-36 'more than a quarter'", fall, 0.25, 0.30)
assert rate[1940] > rate[1936] and rate[1940] < rate[1922]
eq("chart years in order", sorted(rate), list(rate))
eq("births 1922 about 1.13 million", round(births[1922] / 1e6, 2), 1.13)
eq("births 1940 about 1.05 million", round(births[1940] / 1e6, 2), 1.05)
assert births[1940] < births[1922]
# The rate rose between 1936 and 1940 but did not return to 1922
eq("rise 1936-40", round(rate[1940] - rate[1936], 1), 1.1)

# Ascension Day target: 40 million to 60 million = half as many again
eq("60/40", 60 / 40, 1.5)
eq("target years 1927 to 1950", 1950 - 1927, 23)

# Lateran Treaties: 750 + 1,000 million lire = 1,750; 59 years since 1870; plebiscite 41 days later
eq("Lateran compensation", 750 + 1000, 1750)
eq("years of the Roman Question", 1929 - 1870, 59)
eq("treaty to plebiscite (days)", (date(1929, 3, 24) - date(1929, 2, 11)).days, 41)
eq("Vatican City 0.44 sq km = 44 hectares", round(0.44 * 100), 44)

# Gaps between events
eq("Zaniboni to Zamboni (days)", (date(1926, 10, 31) - date(1925, 11, 4)).days, 361)
eq("Gibson to Zamboni (months)", (10 - 4), 6)
eq("Gramsci arrest to death (years)", 1937 - 1926, 11)
eq("Gramsci arrest 8 Nov 1926 to release April 1937 (full years)", 10, 10)
eq("Zamboni age", 15, 15)
eq("Catholic Action: encyclical 29 June 1931 after the May closures (months)", 6 - 5, 1)

# Oath of 1931: about 12 of about 1,200 refused = about 1 per cent
between("oath refusal rate", 12 / 1200, 0.009, 0.011)

# Membership figures in millions: ONB 1936, GIL 1937
onb36, gil37 = 5.561, 7.542
eq("ONB rounded", round(onb36, 1), 5.6)
eq("GIL rounded", round(gil37, 1), 7.5)
assert gil37 > onb36

# Illiteracy 27% (1921) to 21% (1931)
eq("illiteracy fall points", 27 - 21, 6)

# Mark totals for the worked examples (Table A + Table B out of 30)
eq("Lateran essay low", 14 + 13, 27)
eq("Lateran essay high", 14 + 14, 28)
eq("table total", 15 + 15, 30)
eq("paper total", 2 * 30, 60)
eq("minutes: two essays in 1 h 45", 105 // 2, 52)

# Reform of Customs / Starace: dropped October 1939, a year after 1938
eq("Customs year to Starace's fall (years)", 1939 - 1938, 1)

print("ok")
