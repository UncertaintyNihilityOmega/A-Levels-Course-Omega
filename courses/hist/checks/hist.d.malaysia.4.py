# checks/hist.d.malaysia.4.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


# Independence and the revolution
proclamation = date(1945, 8, 17)
eq("Koiso promise to proclamation (days)", (proclamation - date(1944, 9, 7)).days, 344)
eq("Japanese surrender to proclamation (days)", (proclamation - date(1945, 8, 15)).days, 2)
eq("Pancasila speech to proclamation (days)", (proclamation - date(1945, 6, 1)).days, 77)
eq("Proclamation to sovereignty (days)", (date(1949, 12, 27) - proclamation).days, 1593)
eq("Proclamation to sovereignty (whole years)", 1949 - 1945, 4)
eq("Proclamation to unitary republic (years)", 1950 - 1945, 5)
eq("Linggadjati initialled to signed (days)", (date(1947, 3, 25) - date(1946, 11, 15)).days, 130)
eq("Linggadjati signed to first police action (days)", (date(1947, 7, 21) - date(1947, 3, 25)).days, 118)
eq("Renville to second police action (days)", (date(1948, 12, 19) - date(1948, 1, 17)).days, 337)
eq("Second police action to Roem-Van Roijen (days)", (date(1949, 5, 7) - date(1948, 12, 19)).days, 139)
near("... in months (about 4.6, 'within five months')", 139 / 30.44, 4.6, 0.1)
eq("Round Table length (days, 23 August to 2 November 1949)", (date(1949, 11, 2) - date(1949, 8, 23)).days, 71)
eq("Surabaya fighting from 10 November, about three weeks: to 30 November (days)", (date(1945, 11, 30) - date(1945, 11, 10)).days, 20)
eq("Madiun to second police action (days)", (date(1948, 12, 19) - date(1948, 9, 18)).days, 92)
eq("Dalat to return (days, 12 to 14 August)", 14 - 12, 2)

# Weekdays: 17 August 1945 Friday; 1 October 1965 Friday; 11 March 1966 Friday; 27 December 1949 Tuesday
eq("17 August 1945 weekday (4 = Friday)", proclamation.weekday(), 4)
eq("1 October 1965 weekday", date(1965, 10, 1).weekday(), 4)
eq("11 March 1966 weekday", date(1966, 3, 11).weekday(), 4)
eq("27 December 1949 weekday (1 = Tuesday)", date(1949, 12, 27).weekday(), 1)

# Debt at the Round Table Conference (about 4.5 billion guilders)
eq("debt in millions", 4.5 * 1000, 4500)

# 1955 election: vote shares and seats (official results as tabulated on Wikipedia)
shares = {"PNI": 22.32, "Masyumi": 20.92, "NU": 18.41, "PKI": 16.35}
near("four parties' share", sum(shares.values()), 78.00, 0.005)
near("all others", 100 - 78.00, 22.0, 0.005)
near("rounded chart values sum to 100", 22.3 + 20.9 + 18.4 + 16.4 + 22.0, 100.0, 0.001)
seats = {"PNI": 57, "Masyumi": 57, "NU": 45, "PKI": 39}
eq("four parties' seats", sum(seats.values()), 198)
eq("majority of 257", 257 // 2 + 1, 129)
near("PNI seat share", 57 / 257 * 100, 22.2, 0.05)
near("PKI seat share", 39 / 257 * 100, 15.2, 0.05)
near("four parties' seat share", 198 / 257 * 100, 77.0, 0.05)
near("PKI votes in millions (6,176,914)", 6_176_914 / 1e6, 6.2, 0.05)
near("PKI vote share of votes counted", 6_176_914 / 37_785_299 * 100, 16.35, 0.01)
near("PNI vote share of votes counted", 8_434_653 / 37_785_299 * 100, 22.32, 0.01)
near("Masyumi vote share of votes counted", 7_903_886 / 37_785_299 * 100, 20.92, 0.01)
near("NU vote share of votes counted", 6_955_141 / 37_785_299 * 100, 18.41, 0.01)

# Cabinets, 1950-57
months = (1957 - 1950) * 12 + (3 - 9)
eq("September 1950 to March 1957 in months", months, 78)
assert months < 7 * 12, "chapter says under seven years"
eq("six cabinets", len(["Natsir", "Sukiman", "Wilopo", "Ali I", "Burhanuddin", "Ali II"]), 6)

# PRRI/Permesta (Nasution's figures as reported: 7,146 military deaths, 6,115 of them on the PRRI side)
eq("government side deaths", 7146 - 6115, 1031)
near("rebel share of military deaths (per cent)", 6115 / 7146 * 100, 85.6, 0.05)

# Konfrontasi
eq("Brunei revolt to Subandrio's announcement (days)", (date(1963, 1, 20) - date(1962, 12, 8)).days, 43)
eq("Malaysia formed to Indonesia's UN exit (days)", (date(1965, 1, 7) - date(1963, 9, 16)).days, 479)
eq("Subandrio's announcement to Bangkok agreement (days)", (date(1966, 8, 11) - date(1963, 1, 20)).days, 1299)
near("... in years", 1299 / 365.25, 3.6, 0.05)
eq("Malaysia formed to Manila: embassy burned two days later (16 to 18 September)", 18 - 16, 2)

# The fall of Sukarno
eq("30 September Movement to Supersemar (days)", (date(1966, 3, 11) - date(1965, 10, 1)).days, 161)
eq("Supersemar to PKI ban (days)", (date(1966, 3, 12) - date(1966, 3, 11)).days, 1)
eq("Supersemar to Suharto acting president (days)", (date(1967, 3, 12) - date(1966, 3, 11)).days, 366)
eq("Movement to acting president (months, about 17)", (1967 - 1965) * 12 + (3 - 10), 17)
eq("Tritura to Supersemar (days)", (date(1966, 3, 11) - date(1966, 1, 10)).days, 60)
eq("Arief Rachman Hakim killed to Supersemar (days)", (date(1966, 3, 11) - date(1966, 2, 24)).days, 15)
eq("Sukarno's lifespan (years, 6 June 1901 to 21 June 1970)", 1970 - 1901, 69)
eq("Seven officers buried (six generals and Tendean)", 6 + 1, 7)
eq("Generals killed at homes and at Lubang Buaya", 3 + 3, 6)

# Estimates of the dead (given as ranges in the chapter)
low, high = 500_000, 1_000_000
eq("range ratio", high // low, 2)
assert 78_500 < low and 3_000_000 > high
eq("Kopkamtib 1976 range midpoint", (450_000 + 500_000) // 2, 475_000)
eq("Cribb range width", 800_000 - 200_000, 600_000)

# Guided Democracy
eq("Constitution of 1945 restored to 1959 (years)", 1959 - 1945, 14)
eq("Sukarno president for life 1963; Guided Democracy years", 1963 - 1959, 4)
eq("Devaluation of 75 per cent: Rp 1,000 note worth", 1000 * 0.10, 100.0)  # notes declared worth one-tenth

# Economy 1965
eq("debt 2.4 billion in millions", 2.4 * 1000, 2400)
eq("debt service 1966 (530 million) as share of debt (per cent, rounded)", round(530 / 2400 * 100), 22)

# Mark totals
eq("Paper 4 essay: Table A + Table B", 15 + 15, 30)
print("ok")
