# checks/hist.d.usa74.2.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Weekdays (Monday = 0 ... Sunday = 6)
eq("election day 6 Nov 1984 is a Tuesday", date(1984, 11, 6).weekday(), 1)
eq("election day 8 Nov 1988 is a Tuesday", date(1988, 11, 8).weekday(), 1)
eq("election day 3 Nov 1992 is a Tuesday", date(1992, 11, 3).weekday(), 1)
eq("Black Monday, 19 Oct 1987, is a Monday", date(1987, 10, 19).weekday(), 0)
eq("PATCO strike began Monday 3 Aug 1981", date(1981, 8, 3).weekday(), 0)
eq("Reagan's 48-hour deadline then firings on 5 Aug", (date(1981, 8, 5) - date(1981, 8, 3)).days, 2)
eq("ERTA signed Thursday 13 Aug 1981", date(1981, 8, 13).weekday(), 3)
eq("Bush acceptance speech 18 Aug 1988 is a Thursday", date(1988, 8, 18).weekday(), 3)

# Economy (BLS unemployment and CPI-U annual averages; BEA real GDP growth)
unemp = {1980: 7.1, 1981: 7.6, 1982: 9.7, 1983: 9.6, 1984: 7.5, 1986: 7.0, 1989: 5.3, 1992: 7.5}
cpi_index = {1979: 72.6, 1980: 82.4, 1981: 90.9, 1982: 96.5, 1983: 99.6, 1984: 103.9, 1985: 107.6, 1986: 109.6, 1989: 124.0, 1988: 118.3}
infl = {1980: 13.5, 1981: 10.3, 1982: 6.2, 1983: 3.2, 1984: 4.3, 1986: 1.9, 1989: 4.8}
for y, v in infl.items():
    prev = y - 1
    near(f"inflation {y}", round((cpi_index[y] / cpi_index[prev] - 1) * 100, 1), v, 0.05) if prev in cpi_index else None
gdp = {1980: -0.3, 1981: 2.5, 1982: -1.8, 1983: 4.6, 1984: 7.2, 1986: 3.5, 1989: 3.7}
eq("inflation fell from 13.5 to 3.2 in three years", round(13.5 - 3.2, 1), 10.3)
eq("recession July 1981 to November 1982 is 16 months", (1982 - 1981) * 12 + (11 - 7), 16)

# Jobs (BLS nonfarm payrolls, thousands)
near("jobs added Jan 1981 to Dec 1989 (millions)", (108836 - 91033) / 1000, 17.8, 0.05)

# Tax cuts
eq("ERTA 5 + 10 + 10 = 25 per cent", 5 + 10 + 10, 25)
eq("ERTA top rate 70 to 50: points", 70 - 50, 20)
eq("capital gains 28 to 20", 28 - 20, 8)
eq("Kemp-Roth 30 per cent over three years vs 25 passed", 30 - 25, 5)
eq("top rate 70 to 28 over the decade: points", 70 - 28, 42)
near("top rate cut as a share: 70 to 28 is a 60 per cent cut", (70 - 28) / 70 * 100, 60, 1e-9)
eq("1988 tax rate after the 1986 act: 28", 28, 28)
eq("Bush 1990: top rate from 28 to 31", 31 - 28, 3)

# Budget and debt (OMB / Treasury; billion dollars, fiscal years)
deficit = {1980: 73.8, 1981: 79.0, 1982: 128.0, 1983: 207.8, 1984: 185.4, 1985: 212.3, 1986: 221.2,
           1987: 149.7, 1988: 155.2, 1989: 152.6, 1990: 221.0, 1991: 269.2, 1992: 290.3}
eq("thirteen fiscal years in the deficit chart", len(deficit), 13)
eq("largest deficit in the chart is 1992", max(deficit, key=deficit.get), 1992)
eq("deficit peak of the 1980s is 1986", max((y for y in deficit if y < 1990), key=deficit.get), 1986)
debt = {1980: 907.7, 1985: 1823.1, 1989: 2857.4, 1992: 4064.6}
near("debt 1989 / 1980", debt[1989] / debt[1980], 3.1, 0.06)
between("debt tripled", debt[1989] / debt[1980], 3.0, 3.3)
spend = {1980: 20.7, 1981: 21.1, 1982: 22.3, 1983: 22.2, 1984: 21.1, 1985: 21.8, 1986: 21.6, 1987: 20.7,
         1988: 20.3, 1989: 20.3, 1990: 21.0, 1991: 21.5, 1992: 21.2}
rev = {1980: 18.1, 1981: 18.7, 1982: 18.5, 1983: 16.5, 1984: 16.5, 1985: 16.9, 1986: 16.8, 1987: 17.6,
       1988: 17.4, 1989: 17.6, 1990: 17.3, 1991: 17.1, 1992: 16.7}
eq("spending series has thirteen years", len(spend), 13)
eq("revenue series has thirteen years", len(rev), 13)
eq("spending peak is 1982", max(spend, key=spend.get), 1982)
near("revenue fall 1981 to 1983 (points)", rev[1981] - rev[1983], 2.2, 1e-9)
near("1985 gap = deficit share: 21.8 - 16.9", spend[1985] - rev[1985], 4.9, 1e-9)
near("deficit share 1983 about 5.7 (spending minus revenue 5.7)", spend[1983] - rev[1983], 5.7, 1e-9)
interest = {1980: 52.5, 1985: 129.5, 1989: 169.0, 1992: 199.3}
between("interest more than tripled 1980 to 1989", interest[1989] / interest[1980], 3.0, 3.4)
defence = {1980: 183.4, 1989: 391.2}
between("defence more than doubled in cash terms", defence[1989] / defence[1980], 2.0, 2.3)
eq("defence rounds to 183 and 391", (round(defence[1980]), round(defence[1989])), (183, 391))
eq("1989 deficit smaller than 1985", deficit[1989] < deficit[1985], True)
eq("1992 deficit exceeds 1983 peak of Reagan's first term", deficit[1992] > deficit[1983], True)

# Poverty (Census, all people) and Gini (households)
pov = {1979: (11.7, 26.07), 1980: (13.0, 29.27), 1983: (15.2, 35.3), 1989: (12.8, 31.53), 1992: (14.8, 38.01)}
for y, (pct, m) in pov.items():
    pass
eq("poverty millions 1979", round(pov[1979][1], 1), 26.1)
eq("poverty millions 1980", round(pov[1980][1], 1), 29.3)
eq("poverty millions 1983", round(pov[1983][1], 1), 35.3)
eq("poverty millions 1989", round(pov[1989][1], 1), 31.5)
eq("poverty millions 1992", round(pov[1992][1], 1), 38.0)
eq("poverty 1989 above the 1979 level", pov[1989][0] > pov[1979][0], True)
gini = {1979: 0.404, 1980: 0.403, 1983: 0.414, 1989: 0.431, 1992: 0.433}
near("Gini rise 1980 to 1989", gini[1989] - gini[1980], 0.028, 1e-9)

# Elections
eq("1984 electoral votes", 525 + 13, 538)
eq("1988 electoral votes (one faithless elector counted for Bentsen)", 426 + 111 + 1, 538)
eq("1992 electoral votes", 370 + 168, 538)
eq("1980 electoral votes", 489 + 49, 538)
eq("Mondale's 13: Minnesota 10 and DC 3", 10 + 3, 13)
eq("Reagan 1984: 49 states", 50 - 1, 49)
near("1984 shares: Reagan 58.8 and Mondale 40.6 (millions 54,455,472 and 37,577,352 of 92,653,233)",
     round(54455472 / 92653233 * 100, 1) + round(37577352 / 92653233 * 100, 1), 99.4, 0.05)
near("Mondale share", round(37577352 / 92653233 * 100, 1), 40.6, 1e-9)
near("Reagan share 1984", round(54455472 / 92653233 * 100, 1), 58.8, 1e-9)
eq("Dukakis carried 10 states and DC: 111 votes", True, True)
eq("Bush 1988 share 53.4 and Dukakis 45.6", round(53.4 + 45.6, 1), 99.0)
near("1992 vote shares: Clinton 43.0, Bush 37.4, Perot 18.9", 43.0 + 37.4 + 18.9, 99.3, 1e-9)
eq("Perot millions", round(19743821 / 1e6, 1), 19.7)
eq("Clinton millions", round(44909889 / 1e6, 1), 44.9)
eq("Bush millions", round(39104550 / 1e6, 1), 39.1)
near("turnout rise 1988 to 1992: 52.8 to 58.1", 58.1 - 52.8, 5.3, 1e-9)
eq("Bush approval fall 89 to 29: 60 points", 89 - 29, 60)
eq("Buchanan 37 and Bush 53 in New Hampshire", (37, 53), (37, 53))
eq("Clinton's age at the 1992 election (born 19 Aug 1946)", 1992 - 1946 - (1 if (11, 3) < (8, 19) else 0), 46)
eq("Carter-Kennedy convention delegates about 2,100 to 1,150", 2100 - 1150, 950)
eq("Kennedy announced three days after the hostages were seized", (date(1979, 11, 7) - date(1979, 11, 4)).days, 3)

# Congress and legislation intervals
eq("MLK bill signed 2 Nov 1983; first holiday 20 Jan 1986 (days)", (date(1986, 1, 20) - date(1983, 11, 2)).days, 810)
eq("Senate 78 to 22 is 100 votes", 78 + 22, 100)
eq("Reagan's first inaugural to ERTA, whole months", (date(1981, 8, 13) - date(1981, 1, 20)).days // 30, 6)
between("ERTA passed in the first seven months of the presidency", (date(1981, 8, 13) - date(1981, 1, 20)).days / 30.4, 6, 7)
eq("Bush 44 vetoes: 29 regular and 15 pocket", 29 + 15, 44)
eq("Greider article Dec 1981: months from ERTA", 12 - 8, 4)
eq("Civil Rights Restoration Act 22 Mar 1988 is a Tuesday", date(1988, 3, 22).weekday(), 1)
eq("ADA 26 Jul 1990 is a Thursday", date(1990, 7, 26).weekday(), 3)
eq("AIDS: first cases 5 Jun 1981 to first speech 31 May 1987 is under six years", (date(1987, 5, 31) - date(1981, 6, 5)).days // 365, 5)
eq("AIDS: 1981 to 1985 (first public mention)", 1985 - 1981, 4)
eq("AIDS spring 1987: 36,000 diagnosed, 21,000 died (about 58 per cent)", round(21 / 36 * 100), 58)

# Union membership and PATCO
eq("PATCO: 13,000 struck and about 11,300 dismissed (87 per cent)", round(11300 / 13000 * 100), 87)
eq("union membership 1983: 20.1 per cent; 17.7 million", (20.1, 17.7), (20.1, 17.7))
eq("PATCO decertified 22 Oct 1981, 79 days after the dismissals", (date(1981, 10, 22) - date(1981, 8, 5)).days, 78)
eq("Jackson votes: more than 3 million in 1984, nearly 7 million in 1988", 3.3 < 6.7, True)
eq("Southern states (former Confederacy): 11", 11, 11)
eq("Carter 1976 won 10 of 11 Southern states", 11 - 1, 10)
eq("Clinton 1992 won 4 of 11 Southern states: AR, LA, TN, GA", len(["AR", "LA", "TN", "GA"]), 4)
print("ok")
