# checks/hist.d.malaysia.1.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


# 1947 census shares (Census of Malaya 1947, as tabulated by the EHM website)
shares = {"Malay": 49.5, "Chinese": 38.4, "Indian": 10.8, "Others": 1.3}
near("shares sum to 100", sum(shares.values()), 100.0, 0.05)
near("non-Malay share", shares["Chinese"] + shares["Indian"] + shares["Others"], 50.5, 0.05)
eq("non-Malays outnumber Malays", 50.5 > 49.5, True)

# intervals
eq("Kota Bharu to Singapore surrender, days", (date(1942, 2, 15) - date(1941, 12, 8)).days, 69)
near("69 days is about ten weeks", 69 / 7, 10, 0.5)
eq("1941 to 1957 is sixteen years", 1957 - 1941, 16)
eq("1941 to 1963 is twenty-two years", 1963 - 1941, 22)
eq("1909 to 1941 years", 1941 - 1909, 32)
clementi = (date(1934, 2, 17) - date(1930, 2, 5)).days / 365.25
near("Clementi term about four years", clementi, 4.0, 0.05)
eq("Pangkor 1874 to FMS 1895 is 21 years", 1895 - 1874, 21)
eq("Singapore 1819 to Straits Settlements 1826", 1826 - 1819, 7)
eq("Crown colony 1867 after 1826", 1867 - 1826, 41)
near("occupation length from 15 Feb 1942 to 15 Aug 1945 in years", (date(1945, 8, 15) - date(1942, 2, 15)).days / 365.25, 3.5, 0.05)
eq("al-Imam ran two years", 1908 - 1906, 2)

# Clementi's opponents
near("85 of 111 is about 77 per cent", 85 / 111 * 100, 77, 0.5)

# Sook Ching levy
near("28 of 50 million is 56 per cent", 28 / 50 * 100, 56, 0.05)

# railway
near("25,000 of 73,000 is about a third", 25000 / 73000, 1 / 3, 0.02)

# MPAJA disarmament
eq("6,800 guerrillas, 5,497 weapons: fewer weapons than men", 5497 < 6800, True)
eq("1,303 men without a handed-in weapon", 6800 - 5497, 1303)

# Chinese share of population
eq("Chinese share rose from 29 to 38", 38 - 29, 9)

# Practice question marks
eq("two essays at 30 marks", 2 * 30, 60)
eq("Table A + Table B", 15 + 15, 30)
eq("Level 5 example total 27-28", 14 + 13, 27)
eq("Level 5 example total upper", 14 + 14, 28)
print("ok")
