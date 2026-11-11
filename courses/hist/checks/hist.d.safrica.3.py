# checks/hist.d.safrica.3.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# 1994 election table (National Assembly)
votes = {"ANC": 12237655, "NP": 3983690, "IFP": 2058294, "FF": 424555, "DP": 338426, "PAC": 243478, "ACDP": 88104}
seats = {"ANC": 252, "NP": 82, "IFP": 43, "FF": 9, "DP": 7, "PAC": 5, "ACDP": 2}
share = {"ANC": 62.65, "NP": 20.39, "IFP": 10.54, "FF": 2.17, "DP": 1.73, "PAC": 1.25, "ACDP": 0.45}
valid = 19533498  # valid votes in the full count
eq("seats add to 400", sum(seats.values()), 400)
for p in votes:
    near(f"{p} share of valid votes", round(100 * votes[p] / valid, 2), share[p], 0.011)
near("seven parties hold almost every valid vote", sum(votes.values()) / valid, 1.0, 0.01)
near("about 19.5 million valid votes", valid / 1e6, 19.5, 0.05)
eq("ANC seats 63 per cent of 400", round(100 * 252 / 400), 63)
eq("two-thirds of 400 rounds up to 267", -(-2 * 400 // 3), 267)
eq("ANC short of two-thirds", 252 < 267, True)
eq("majority of 400 is 201", 400 // 2 + 1, 201)
eq("ANC + NP + IFP seats", 252 + 82 + 43, 377)
eq("NP polled 20 per cent, over the 5 per cent threshold", share["NP"] > 5, True)

# Referendum of 17 March 1992
yes, no = 1924186, 875619
near("68.7 per cent yes", round(100 * yes / (yes + no), 1), 68.7, 0.05)
near("31.3 per cent no", round(100 * no / (yes + no), 1), 31.3, 0.05)
near("turnout 85 per cent of 3,296,800", round(100 * (yes + no + 5142) / 3296800, 0), 85, 0.5)
eq("3.3 million white voters", round(3296800 / 1e6, 1), 3.3)

# Tricameral
eq("tricameral chambers", 178 + 85 + 45, 308)
eq("1983 referendum: 66.3 yes leaves 33.7", round(100 - 66.3, 1), 33.7)

# Intervals and dates
eq("5 Aug 1962 arrest to 11 Feb 1990 release is 27 full years", (date(1990, 2, 11) - date(1962, 8, 5)).days // 365, 27)
eq("Mandela age on release (born 18 July 1918)", age(date(1918, 7, 18), date(1990, 2, 11)), 71)
eq("de Klerk born 1936, aged 53 in Feb 1989", 1989 - 1936, 53)
eq("Rubicon speech to the US override, days", (date(1986, 10, 2) - date(1985, 8, 15)).days, 413)
eq("Vaal uprising to first emergency, days", (date(1985, 7, 21) - date(1984, 9, 3)).days, 321)
eq("emergency (21 Jul 1985) is 25 days before the Rubicon speech", (date(1985, 8, 15) - date(1985, 7, 21)).days, 25)
eq("UDF launch to Vaal uprising, days", (date(1984, 9, 3) - date(1983, 8, 20)).days, 380)
eq("Tripartite Accord to Namibian independence, days", (date(1990, 3, 21) - date(1988, 12, 22)).days, 454)
eq("De Klerk speech to release, days", (date(1990, 2, 11) - date(1990, 2, 2)).days, 9)
eq("Berlin Wall to de Klerk's speech, days", (date(1990, 2, 2) - date(1989, 11, 9)).days, 85)
eq("Boipatong to ANC withdrawal, days", (date(1992, 6, 24) - date(1992, 6, 17)).days, 7)
eq("Bisho to Record of Understanding, days", (date(1992, 9, 26) - date(1992, 9, 7)).days, 19)
eq("Hani's murder to the election date being fixed, days", (date(1993, 6, 3) - date(1993, 4, 10)).days, 54)
eq("Election date fixed to election, months (June 1993 to April 1994)", (1994 - 1993) * 12 + (4 - 6), 10)
eq("CODESA 1 to CODESA 2, months", (1992 - 1991) * 12 + (5 - 12), 5)
eq("Interim constitution to election, days", (date(1994, 4, 27) - date(1993, 11, 18)).days, 160)
eq("Election to inauguration, days (27 April to 10 May)", (date(1994, 5, 10) - date(1994, 4, 27)).days, 13)
eq("Soweto 1976 to election 1994, years", 1994 - 1976, 18)
eq("Botha as State President 14 Sep 1984 to 14 Aug 1989, years (nearly 5)", (date(1989, 8, 14) - date(1984, 9, 14)).days // 365, 4)
eq("Botha PM 1978 to resignation 1989, about 11 years", 1989 - 1978, 11)
eq("Debt rescheduling last repaid 2001, years after 1985", 2001 - 1985, 16)
eq("IFP joins 19 April, election 27 April: 8 days", (date(1994, 4, 27) - date(1994, 4, 19)).days, 8)
eq("Election days 26-29 April", 29 - 26 + 1, 4)
eq("1984 to 1994 is a decade", 1994 - 1984, 10)
eq("Sixteen years from 1978 to 1994", 1994 - 1978, 16)
eq("Wiehahn 1977 appointed, act 1979: 2 years", 1979 - 1977, 2)
eq("COSATU Dec 1985 to NUM strike Aug 1987, months", (1987 - 1985) * 12 + (8 - 12), 20)
eq("Boipatong 45 + Bisho 28", 45 + 28, 73)
eq("Sebokeng 11 killed 26 March 1990 is 43 days after the release", (date(1990, 3, 26) - date(1990, 2, 11)).days, 43)
eq("Nobel Peace Prize 1993 is within the 1991-94 talks", 1991 <= 1993 <= 1994, True)
eq("Pass laws abolished 1 July 1986 is 12 June + 19 days", (date(1986, 7, 1) - date(1986, 6, 12)).days, 19)
eq("Mandela meets Botha 5 July 1989 to Botha's resignation 14 Aug, days", (date(1989, 8, 14) - date(1989, 7, 5)).days, 40)
eq("Zimbabwe independence 1980 to Botha's PM 1978: 2 years", 1980 - 1978, 2)
print("ok")
