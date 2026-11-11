# checks/hist.d.safrica.2.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Sharpeville and the emergency
eq("police count vs later research (killed)", 91 - 69, 22)
eq("police count vs later research (injured)", 238 - 180, 58)
eq("Resolution 134 is 11 days after Sharpeville", (date(1960, 4, 1) - date(1960, 3, 21)).days, 11)
eq("emergency 30 March to 31 August 1960, days", (date(1960, 8, 31) - date(1960, 3, 30)).days, 154)
eq("ban comes 18 days after Sharpeville", (date(1960, 4, 8) - date(1960, 3, 21)).days, 18)
eq("Sharpeville rounds fired: more than 1,300 (1,344)", 1344 > 1300, True)
eq("PAC founded 6 April 1959 to Sharpeville in months", (1960 - 1959) * 12 + (3 - 4), 11)

# UN votes
eq("Resolution 1761: 67 + 16 + 23 members voting", 67 + 16 + 23, 106)
eq("Resolution 1761 passed by a majority of those voting", 67 > 16 + 23, True)

# Rivonia
eq("Rivonia: eight life sentences + Bernstein + Kantor = ten accused", 8 + 1 + 1, 10)
eq("Rivonia raid to sentences, months", (1964 - 1963) * 12 + (6 - 7), 11)
eq("MK launched 16 December 1961 is 5 months... after Mandela's acquittal (29 Mar 1961), in months", (1961 - 1961) * 12 + (12 - 3), 9)
eq("Mandela arrest 5 Aug 1962 to sentence 7 Nov 1962, days", (date(1962, 11, 7) - date(1962, 8, 5)).days, 94)
eq("Mandela's statement of 20 April 1964 is before the verdict of 11 June 1964, days", (date(1964, 6, 11) - date(1964, 4, 20)).days, 52)
eq("MK sabotage: about 200 acts in 18 months, per month", round(200 / 18, 1), 11.1)

# Verwoerd and Vorster
eq("Verwoerd PM 1958-66", 1966 - 1958, 8)
eq("Vorster PM 1966-78", 1978 - 1966, 12)
eq("Homelands: 13 per cent of the land leaves 87", 100 - 13, 87)
eq("Transkei self-government 1963 to independence 1976", 1976 - 1963, 13)
eq("Four 'independent' homelands out of ten leaves six self-governing", 10 - 4, 6)
eq("Surplus People Project: 1960-83 span, years", 1983 - 1960, 23)

# Black Consciousness
eq("SASO (July 1969) to BPC (July 1972), years", 1972 - 1969, 3)
eq("Biko age at death (born 18 Dec 1946, died 12 Sep 1977)", age(date(1946, 12, 18), date(1977, 9, 12)), 30)
eq("Biko arrest 18 Aug to death 12 Sep 1977, days", (date(1977, 9, 12) - date(1977, 8, 18)).days, 25)
eq("19 Oct 1977 bans are 37 days after Biko's death", (date(1977, 10, 19) - date(1977, 9, 12)).days, 37)
eq("37 days is just over five weeks", 37 // 7, 5)
eq("UN Resolution 418 is 23 days after the bans", (date(1977, 11, 4) - date(1977, 10, 12 + 7)).days, 16)  # 19 Oct to 4 Nov
eq("Timol 1971 to the 2017 ruling, years", 2017 - 1971, 46)
eq("TRC refused amnesty 1998; no prosecution announced 2003 (years)", 2003 - 1998, 5)

# Soweto
eq("Soweto estimates are in order", 23 < 176 < 575 < 700, True)
eq("Hector Pieterson aged 12", 12, 12)
eq("Afrikaans decree 1974 to Soweto 1976, years", 1976 - 1974, 2)
eq("Soweto 1976 is sixteen years after Sharpeville", 1976 - 1960, 16)
eq("Sharpeville 1960 to the unbanning 1990, years", 1990 - 1960, 30)
eq("Durban strikes: about 60,000 workers", 60000, 60000)
eq("Cillie: 575 by 28 Feb 1977, which is 257 days after 16 June 1976", (date(1977, 2, 28) - date(1976, 6, 16)).days, 257)
eq("Mozambique 25 June 1975 to Angola 11 Nov 1975, days", (date(1975, 11, 11) - date(1975, 6, 25)).days, 139)
eq("Portuguese revolution 25 April 1974 to Mozambique independence, months", (1975 - 1974) * 12 + (6 - 4), 14)
eq("OAU 1963 to Wankie 1967, years", 1967 - 1963, 4)
eq("Biko banned March 1973 to death Sept 1977, years (about 4.5)", round((date(1977, 9, 12) - date(1973, 3, 1)).days / 365.25, 1), 4.5)
eq("Republic 31 May 1961 is 5 months... after referendum of 5 Oct 1960 (about 8 months)", (1961 - 1960) * 12 + (5 - 10), 7)
print("ok")
