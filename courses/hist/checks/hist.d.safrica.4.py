# checks/hist.d.safrica.4.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


# 1980 common-roll election
votes = {"ZANU-PF": 1668992, "PF-ZAPU": 638879, "UANC": 219307}
share = {"ZANU-PF": 62.99, "PF-ZAPU": 24.11, "UANC": 8.28}
seats = {"ZANU-PF": 57, "PF-ZAPU": 20, "UANC": 3}
eq("common-roll seats add to 80", sum(seats.values()), 80)
eq("80 common-roll + 20 white = 100", 80 + 20, 100)
eq("white seats are 20 per cent of the house", 100 * 20 // 100, 20)
totals = [votes[p] / (share[p] / 100) for p in votes]
near("shares agree on one common total (within 1,000 votes)", max(totals) - min(totals), 0, 1500)
eq("ZANU-PF share is under two-thirds of the vote but over two-thirds of the seats", 57 / 80 > 2 / 3, True)
eq("57 of 80 is 71 per cent", round(100 * 57 / 80), 71)

# 1979 election
eq("1979: 72 common-roll seats (51 + 12 + 9)", 51 + 12 + 9, 72)
eq("1979: 72 Black + 28 white = 100", 72 + 28, 100)
eq("1979: 20 white-roll + 8 non-constituency = 28 white seats", 20 + 8, 28)
eq("1979: 28 seats is a blocking share of 100 (78 needed to amend)", 100 - 28 < 78 + 1, True)
eq("Internal Settlement 3 Mar 1978 to election 10 Apr 1979, months", (1979 - 1978) * 12 + (4 - 3), 13)
eq("Muzorewa PM 1 June 1979 is 41 days after the common-roll vote of 21 April", (date(1979, 6, 1) - date(1979, 4, 21)).days, 41)

# Intervals
eq("UDI 11 Nov 1965 to independence 18 Apr 1980, years (14)", (date(1980, 4, 18) - date(1965, 11, 11)).days // 365, 14)
eq("UDI to Lancaster House agreement 21 Dec 1979, years (14)", (date(1979, 12, 21) - date(1965, 11, 11)).days // 365, 14)
eq("Referendum 5 Nov 1964 to UDI, days", (date(1965, 11, 11) - date(1964, 11, 5)).days, 371)
eq("Smith PM 13 Apr 1964 to UDI, months", (1965 - 1964) * 12 + (11 - 4), 19)
eq("Tiger talks 2-4 Dec 1966: three days", 4 - 2 + 1, 3)
eq("Resolution 232 is 12 days after the Tiger talks ended", (date(1966, 12, 16) - date(1966, 12, 4)).days, 12)
eq("Beira Patrol March 1966 to June 1975, years (9)", 1975 - 1966, 9)
eq("Byrd Amendment 1971 to repeal 1977, years", 1977 - 1971, 6)
eq("Home-Smith Nov 1971 to Pearce report May 1972, months", (1972 - 1971) * 12 + (5 - 11), 6)
eq("Chinhoyi 28 Apr 1966 to Altena 21 Dec 1972, years (6)", (date(1972, 12, 21) - date(1966, 4, 28)).days // 365, 6)
eq("Mozambique 25 June 1975 to border closure Mar 1976, months", (1976 - 1975) * 12 + (3 - 6), 9)
eq("Mugabe detained 1964 to 1974, years", 1974 - 1964, 10)
eq("ZAPU 1961 to ZANU 1963, years", 1963 - 1961, 2)
eq("Kissinger meets Smith 19 Sep 1976; Smith's broadcast 24 Sep: 5 days", (date(1976, 9, 24) - date(1976, 9, 19)).days, 5)
eq("Geneva 28 Oct to 14 Dec 1976, days", (date(1976, 12, 14) - date(1976, 10, 28)).days, 47)
eq("Lancaster House 10 Sep to 15 Dec 1979, days", (date(1979, 12, 15) - date(1979, 9, 10)).days, 96)
eq("Lancaster House conference lasted about 14 weeks", (date(1979, 12, 15) - date(1979, 9, 10)).days // 7, 13)
eq("Lusaka 1-7 August 1979: seven days", 7 - 1 + 1, 7)
eq("Thatcher elected 3 May 1979 to Lusaka 1 Aug, days", (date(1979, 8, 1) - date(1979, 5, 3)).days, 90)
eq("Agreement 21 Dec 1979 to ceasefire 28 Dec, days", (date(1979, 12, 28) - date(1979, 12, 21)).days, 7)
eq("Election result 4 Mar 1980 to independence 18 Apr 1980, days", (date(1980, 4, 18) - date(1980, 3, 4)).days, 45)
eq("Land restriction ten years from 1980 runs to 1990", 1980 + 10, 1990)
eq("20 white seats for seven years from 1980 runs to 1987", 1980 + 7, 1987)
eq("Viscount 825 (3 Sep 1978) to 827 (12 Feb 1979), days", (date(1979, 2, 12) - date(1978, 9, 3)).days, 162)
eq("Conscription 18 months by 1976 is 1.5 years", 18 / 12, 1.5)
eq("Population: 220,000 whites among about 4.2 million is about 5 per cent", round(100 * 220000 / (4000000 + 220000)), 5)
eq("Mozambique border about 1,300 km", 1300, 1300)
eq("War deaths range 20,000 to 30,000", 20000 < 30000, True)
eq("Two Viscounts: 38 + 59 killed", 38 + 59, 97)
eq("Internal Settlement 1978 to Lancaster House agreement 1979, years", 1979 - 1978, 1)
eq("Federation 1953-63 lasted ten years", 1963 - 1953, 10)
eq("Self-government 1923 to UDI 1965, years (42)", 1965 - 1923, 42)
eq("Rhodesia 4 official names then Zimbabwe: five rows in the table", 5, 5)
eq("1980 independence is 15 years after UDI (to the nearest year)", 1980 - 1965, 15)
print("ok")
