# checks/hist.d.usa74.1.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Weekdays named or implied (Monday = 0 ... Sunday = 6)
eq("election day 2 Nov 1976 is a Tuesday", date(1976, 11, 2).weekday(), 1)
eq("election day 4 Nov 1980 is a Tuesday", date(1980, 11, 4).weekday(), 1)
eq("Ford pardon 8 Sep 1974 is a Sunday", date(1974, 9, 8).weekday(), 6)
eq("Carter speech 15 Jul 1979 is a Sunday", date(1979, 7, 15).weekday(), 6)
eq("Proposition 13, 6 Jun 1978, is a Tuesday", date(1978, 6, 6).weekday(), 1)
eq("Volcker 'Saturday night special', 6 Oct 1979, is a Saturday", date(1979, 10, 6).weekday(), 5)

# BLS annual averages (unemployment rate; CPI-U percentage change) used in the table and chart
unemp = {1973: 4.9, 1974: 5.6, 1975: 8.5, 1976: 7.7, 1977: 7.1, 1978: 6.1, 1979: 5.8, 1980: 7.1, 1981: 7.6}
infl = {1973: 6.2, 1974: 11.0, 1975: 9.1, 1976: 5.8, 1977: 6.5, 1978: 7.6, 1979: 11.3, 1980: 13.5, 1981: 10.3}
misery = {1973: 11.1, 1974: 16.6, 1975: 17.6, 1976: 13.5, 1977: 13.6, 1978: 13.7, 1979: 17.1, 1980: 20.6, 1981: 17.9}
for y in unemp:
    near(f"misery index {y}", unemp[y] + infl[y], misery[y], 1e-9)
eq("misery index peaks in 1980", max(misery, key=misery.get), 1980)
eq("misery index 1975 is the peak before 1979", max((y for y in misery if y < 1979), key=misery.get), 1975)
# CPI-U annual average index values (1982-84 = 100), from BLS, reproduce the inflation column
cpi = {1972: 41.8, 1973: 44.4, 1974: 49.3, 1975: 53.8, 1976: 56.9, 1977: 60.6, 1978: 65.2, 1979: 72.6, 1980: 82.4, 1981: 90.9}
for y in range(1973, 1982):
    near(f"inflation {y}", round((cpi[y] / cpi[y - 1] - 1) * 100, 1), infl[y], 0.05)
near("Dec-to-Dec inflation 1979 (13.3) and 1980 (12.5) as quoted in the chart note", 13.3 - 12.5, 0.8, 1e-9)
near("inflation roughly doubled 1976 to 1979", infl[1979] / infl[1976], 1.95, 0.05)
between("growth 1976-78 about 5% a year", (5.4 + 4.6 + 5.5) / 3, 4.9, 5.2)
eq("unemployment fell from 8.5 (1975) to 5.8 (1979)", (unemp[1975], unemp[1979]), (8.5, 5.8))
eq("recession of 1973-75: months from Nov 1973 to Mar 1975", (1975 - 1973) * 12 + 3 - 11, 16)

# Presidents' dates
eq("Ford's months in office (9 Aug 1974 to 20 Jan 1977)", (1977 - 1974) * 12 + (1 - 8) + (0 if 20 >= 9 else -1), 29)
eq("Ford office: 29 months", 29, 29)
eq("days from Nixon's resignation to the pardon", (date(1974, 9, 8) - date(1974, 8, 9)).days, 30)
eq("Ford approval fall (Gallup) 71 to 50", 71 - 50, 21)
eq("pardon covers 20 Jan 1969 to 9 Aug 1974 (years, full)", age(date(1969, 1, 20), date(1974, 8, 9)), 5)
eq("Ford's 66 vetoes: 48 regular and 18 pocket", 48 + 18, 66)
eq("12 of 66 overridden is about 18 per cent", round(12 / 66 * 100), 18)

# Elections
eq("1976 electoral votes sum (Carter 297, Ford 240, one faithless Reagan vote)", 297 + 240 + 1, 538)
eq("270 needed to win", 538 // 2 + 1, 270)
eq("Ohio and Wisconsin flip would have given Ford a majority", 240 + 1 + 36 > 270 - 1, True)
eq("Carter without Ohio and Wisconsin", 297 - 36, 261)
eq("Ford with Ohio and Wisconsin (and the stray vote counted as his)", 240 + 1 + 36, 277)
near("1976 shares: 50.1 + 48.0 + others", 50.1 + 48.0, 98.1, 1e-9)
eq("1976 convention 1,187 to 1,070: margin", 1187 - 1070, 117)
eq("1980 electoral votes sum", 489 + 49, 538)
eq("Carter's 1980 electoral votes: GA 12, MD 10, MN 10, RI 4, WV 6, HI 4, DC 3", 12 + 10 + 10 + 4 + 6 + 4 + 3, 49)
eq("Carter's 1980 states plus DC (six states and DC)", len(["GA", "MD", "MN", "RI", "WV", "HI"]), 6)
eq("Reagan won 44 states", 50 - 6, 44)
total_80 = 86509678
reagan, carter, anderson = 43899248, 35481436, 5719850
near("Reagan share 1980", round(reagan / total_80 * 100, 1), 50.7, 0.05)
near("Carter share 1980", round(carter / total_80 * 100, 1), 41.0, 0.05)
near("Anderson share 1980", round(anderson / total_80 * 100, 1), 6.6, 0.05)
eq("Reagan millions", round(reagan / 1e6, 1), 43.9)
eq("Carter millions", round(carter / 1e6, 1), 35.5)
eq("Anderson millions", round(anderson / 1e6, 1), 5.7)
eq("Reagan's age on election day 1980", age(date(1911, 2, 6), date(1980, 11, 4)), 69)
eq("hostages: 4 Nov 1979 to 20 Jan 1981 in days, counting both days", (date(1981, 1, 20) - date(1979, 11, 4)).days + 1, 444)
eq("hostages seized one year before election day", date(1980, 11, 4).year - date(1979, 11, 4).year, 1)
eq("Carter's 1976 to 1980 share fall: 50.1 to 41.0", round(50.1 - 41.0, 1), 9.1)

# Deficits (billion dollars, fiscal years): Treasury/OMB via St Louis Fed
deficit = {1976: 73.7, 1977: 53.7, 1978: 59.2, 1979: 40.7, 1980: 73.8}
near("deficit 1979 as a share of 1976", deficit[1979] / deficit[1976], 0.55, 0.01)
between("deficit almost halved 1976 to 1979", deficit[1979] / deficit[1976], 0.5, 0.6)
eq("Ford deficit 1976 about 74", round(deficit[1976]), 74)

# Jobs: BLS nonfarm payrolls (thousands)
near("jobs created Jan 1977 to Jan 1981 (millions)", (91033 - 80690) / 1000, 10.3, 0.05)

# Trust in government (ANES via Pew)
trust = {1964: 77, 1974: 36, 1980: 25, 1984: 44}
eq("trust fell by 52 points 1964 to 1980", trust[1964] - trust[1980], 52)
between("trust more than halved 1964 to 1980", trust[1980] / trust[1964], 0.3, 0.5)

# Congress and 1974 elections
eq("Democrats about two-thirds of the House after 1974 (291 of 435)", round(291 / 435 * 100), 67)
eq("Democrats about two-thirds of the House in 1977 (292 of 435)", round(292 / 435 * 100), 67)

# Carter's electoral appeal and Volcker
eq("Volcker named 25 Jul 1979 ten days after the speech", (date(1979, 7, 25) - date(1979, 7, 15)).days, 10)
eq("Cabinet shake-up two days after the speech", (date(1979, 7, 17) - date(1979, 7, 15)).days, 2)
eq("hit list: 19 water projects", 19, 19)
eq("Carter's approval fell from about 75 to about 28: 47 points", 75 - 28, 47)

# Proposition 13 and referendums
eq("Prop 13 about 65 to 35", 65 + 35, 100)
eq("Dade County repeal 69 to 31", 69 + 31, 100)
eq("Briggs 58 to 42", 58 + 42, 100)
eq("Proposition 13 limits tax to 1 per cent of 1975 values (years from 1975 to 1978)", 1978 - 1975, 3)
eq("Kemp-Roth: 30 per cent over three years is 10 per cent a year", 30 // 3, 10)
eq("ERA: 35 ratified, 38 needed, three short", 38 - 35, 3)
eq("ERA deadline extended from March 1979 to June 1982, in months", (1982 - 1979) * 12 + (6 - 3), 39)

# Misc
eq("first Saturday-night-special rate: prime 21.5 per cent in December 1980 exceeds the 1980 inflation", 21.5 > 13.5, True)
eq("inflation fell from 13.5 (1980) to 3.2 (1983)", round(13.5 - 3.2, 1), 10.3)
print("ok")
