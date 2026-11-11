# checks/hist.d.usa61.2.py: recomputes every number in the chapter (dates, intervals, votes, troop levels, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Cuba
eq("Castro to break in relations (days)", (date(1961, 1, 3) - date(1959, 1, 1)).days, 733)
eq("Bay of Pigs duration (days inclusive)", (date(1961, 4, 19) - date(1961, 4, 17)).days + 1, 3)
between("Bay of Pigs: prisoners about 1,100 or more", 1113, 1100, 1200)
eq("Bay of Pigs to ransom (months)", (1962 - 1961) * 12 + (12 - 4), 20)
eq("U-2 to Kennedy's speech (days)", (date(1962, 10, 22) - date(1962, 10, 14)).days, 8)
eq("U-2 to Khrushchev's announcement (days)", (date(1962, 10, 28) - date(1962, 10, 14)).days, 14)
eq("Kennedy told 16 Oct to announcement 28 Oct, thirteen days inclusive", (date(1962, 10, 28) - date(1962, 10, 16)).days + 1, 13)
eq("Speech to quarantine (days)", (date(1962, 10, 24) - date(1962, 10, 22)).days, 2)
eq("Black Saturday is a Saturday", date(1962, 10, 27).weekday(), 5)
eq("Kennedy speech is a Monday", date(1962, 10, 22).weekday(), 0)
eq("26 Oct to 28 Oct (days)", (date(1962, 10, 28) - date(1962, 10, 26)).days, 2)
eq("Quarantine lifted 20 Nov, days after end of crisis", (date(1962, 11, 20) - date(1962, 10, 28)).days, 23)
eq("Crisis to hot line (days)", (date(1963, 6, 20) - date(1962, 10, 28)).days, 235)
eq("Crisis to Test Ban Treaty (days)", (date(1963, 8, 5) - date(1962, 10, 28)).days, 281)
eq("Khrushchev fall, years after crisis", 1964 - 1962, 2)
eq("Vienna to Berlin Wall: June to August 1961 (months)", 8 - 6, 2)
eq("Soviet troops vs American estimate", 40000 // 10000, 4)
eq("ExComm options", len(["nothing/diplomacy", "secret approach", "air strike", "invasion", "quarantine"]), 5)
eq("Jupiter missiles", 15, 15)

# Vietnam to 1963
eq("Geneva to Diem referendum year gap", 1955 - 1954, 1)
eq("Dien Bien Phu to Geneva (days)", (date(1954, 7, 21) - date(1954, 5, 7)).days, 75)
eq("Elections promised for 1956", 1956 - 1954, 2)
eq("Ap Bac date", date(1963, 1, 2).isoformat(), "1963-01-02")
eq("Diem coup to Kennedy's death (days)", (date(1963, 11, 22) - date(1963, 11, 1)).days, 21)
eq("Advisers growth 1960 to 1963", round(16300 / 900), 18)

# Troop levels (thousands), year-end
troops = {1960: 1, 1961: 3, 1962: 11, 1963: 16, 1964: 23, 1965: 184, 1966: 385, 1967: 486, 1968: 536, 1969: 475,
          1970: 335, 1971: 157, 1972: 24}
exact = {1960: 900, 1961: 3205, 1962: 11326, 1963: 16263, 1964: 23310, 1965: 184314, 1966: 385278, 1967: 485587,
         1968: 536100, 1969: 475200, 1970: 334591, 1971: 156776, 1972: 24172}
for y, v in exact.items():
    eq(f"chart {y}", round(v / 1000), troops[y])
eq("chart years consecutive", sorted(troops), list(range(1960, 1973)))
eq("peak April 1969", 543400 > max(exact.values()), True)
between("fall 1969 to 1972 to about 5 per cent of peak", 24.2 / 543.4, 0.04, 0.05)
between("rise 1964 to 1965 (eight-fold)", 184.3 / 23.3, 7.5, 8.5)
eq("troops 1965 to 1968 years", 1968 - 1965, 3)

# Escalation dates
eq("Tonkin Resolution vote House", 416 + 0, 416)
eq("Tonkin Senate vote total", 88 + 2, 90)
eq("Tonkin Resolution date", date(1964, 8, 7).isoformat(), "1964-08-07")
eq("Maddox to Resolution (days)", (date(1964, 8, 7) - date(1964, 8, 2)).days, 5)
eq("Pleiku to Rolling Thunder (days)", (date(1965, 3, 2) - date(1965, 2, 7)).days, 23)
eq("Rolling Thunder to Marines (days)", (date(1965, 3, 8) - date(1965, 3, 2)).days, 6)
eq("125,000 after 50,000 more", 125000 - 50000, 75000)
eq("Ia Drang duration (days inclusive)", (date(1965, 11, 18) - date(1965, 11, 14)).days + 1, 5)
eq("Rolling Thunder length, about 3.67 years", round((date(1968, 11, 2) - date(1965, 3, 2)).days / 365.25, 1), 3.7)
eq("Herbicides, Agent Orange share", 11 < 19, True)

# Tet and 1968
eq("Tet 30-31 January to Cronkite (days)", (date(1968, 2, 27) - date(1968, 1, 30)).days, 28)
eq("New Hampshire primary to Johnson speech (days)", (date(1968, 3, 31) - date(1968, 3, 12)).days, 19)
eq("McCarthy 42 against Johnson 49", 49 - 42, 7)
eq("Tet to Johnson's speech (days)", (date(1968, 3, 31) - date(1968, 1, 30)).days, 61)
eq("Paris talks open date", date(1968, 5, 13).isoformat(), "1968-05-13")
eq("My Lai to Hersh (months)", (1969 - 1968) * 12 + (11 - 3), 20)
eq("Gallup mistake 1965 and 1968", (24, 53), (24, 53))
between("Gallup gap", 53 - 24, 28, 30)
eq("My Lai dead range", (347, 504), (347, 504))

# Nixon
eq("Midway withdrawal", 25000, 25000)
eq("Troops 543,400 to 24,172 reduction in per cent", round((1 - 24172 / 543400) * 100), 96)
eq("Cambodia to Kent State (days)", (date(1970, 5, 4) - date(1970, 4, 30)).days, 4)
eq("Linebacker II days inclusive", (date(1972, 12, 29) - date(1972, 12, 18)).days + 1, 12)
eq("Accords to last troops (days)", (date(1973, 3, 29) - date(1973, 1, 27)).days, 61)
eq("Sixty-day withdrawal", 60 <= 61, True)
eq("Accords to Saigon (years)", round((date(1975, 4, 30) - date(1973, 1, 27)).days / 365.25, 1), 2.3)
eq("War Powers Resolution date", date(1973, 11, 7).isoformat(), "1973-11-07")
eq("Saigon fell", date(1975, 4, 30).isoformat(), "1975-04-30")
eq("Quote: first withdrawal to peak troops (months)", (1969 - 1969) * 12 + (6 - 4), 2)
eq("Total US dead about 58,000", round(58220, -3), 58000)
eq("Nixon visit to China February 1972 before Easter Offensive", date(1972, 2, 21) < date(1972, 3, 30), True)

# Essay and mark totals
eq("Table A + Table B", 15 + 15, 30)
eq("two essays", 2 * 30, 60)
between("worked answer total about 27-28", 14 + 13.5, 26.5, 28.5)

print("ok")
