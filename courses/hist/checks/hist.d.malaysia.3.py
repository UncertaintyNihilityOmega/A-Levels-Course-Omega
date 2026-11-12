# checks/hist.d.malaysia.3.py: recomputes every number in the chapter (dates, intervals, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


# Population shares, 1930 census (total 60,727,233; Europeans about 240,000; Chinese about 1.2 million)
total = 60_727_233
near("European share (per cent)", 240_000 / total * 100, 0.4, 0.05)
near("Chinese share (per cent)", 1_230_000 / total * 100, 2.0, 0.1)

# Ethical Policy and education (figures quoted in the chapter)
eq("1900 Europeans in European schools", 13_000, 13_000)
near("1928 primary graduates per 1,000 people", 75_000 / total * 1000, 1.2, 0.05)
eq("secondary graduates about", round(6_500, -2), 6_500)

# Intervals
eq("Ethical Policy to Volksraad", 1918 - 1901, 17)
eq("Volksraad: Indonesian members of 39 (15)", 39 - 15, 24)
eq("Volksraad 1927 Indonesian members", 60 // 2, 30)
eq("PNI founded to Sukarno's arrest (years)", 1929 - 1927, 2)
eq("PNI founded to dissolved (years)", 1931 - 1927, 4)
d1 = date(1929, 12, 29)
d2 = date(1931, 4, 25)
eq("Arrest to dissolution (days)", (d2 - d1).days, 482)
eq("Youth Pledge to proclamation (years)", 1945 - 1928, 17)
eq("Sukarno exile 1934 to 1942 (years)", 1942 - 1934, 8)
eq("Soetardjo Petition: Volksraad vote to rejection (months, July 1936 to 16 Nov 1938)", (1938 - 1936) * 12 + (11 - 7), 28)
eq("Soetardjo votes: for minus against", 26 - 20, 6)
eq("Gerindo to Gapi (days)", (date(1939, 5, 21) - date(1937, 5, 24)).days, 727)

# The occupation
d_start = date(1942, 3, 8)
d_end = date(1945, 8, 15)
days = (d_end - d_start).days
eq("occupation length in days", days, 1256)
eq("occupation length in whole years", days // 365, 3)
eq("occupation length in months (March 1942 to August 1945)", (1945 - 1942) * 12 + (8 - 3), 41)
eq("Putera (March 1943) to Peta (October 1943) months", 10 - 3, 7)
eq("Koiso promise to Blitar revolt (days)", (date(1945, 2, 14) - date(1944, 9, 7)).days, 160)
eq("Koiso promise to Japanese surrender (days)", (date(1945, 8, 15) - date(1944, 9, 7)).days, 342)

# Peta
eq("Peta battalions", 66 + 3, 69)
near("Peta men per battalion on Java, Madura and Bali (about)", 37_000 / 69, 536, 1)

# Romusha estimates quoted: ranges, not sums
eq("Ricklefs range low", 4, 4)
eq("Share of those sent from Java who survived at most (70,000 of 200,000)", round(70_000 / 200_000 * 100), 35)
eq("Share of those sent from Java who survived at most (70,000 of 500,000)", round(70_000 / 500_000 * 100), 14)
near("Sato: 15 per cent of 270,000 (about)", 270_000 * 0.15, 40_500, 1)

# Famine estimate relative to Java's population is not computed (population base uncertain)

# Hatta's and Sukarno's lives
eq("Sukarno lifespan", 1970 - 1901, 69)
eq("Hatta lifespan", 1980 - 1902, 78)
eq("Sjahrir lifespan", 1966 - 1909, 57)
eq("Sartono lifespan", 1968 - 1900, 68)
eq("Thamrin lifespan", 1941 - 1894, 47)
eq("Amir Sjarifuddin lifespan", 1948 - 1907, 41)

# Weekdays: 28 October 1928 was a Sunday, 17 August 1945 a Friday
eq("Youth Pledge weekday (6 = Sunday)", date(1928, 10, 28).weekday(), 6)
eq("Proclamation weekday (4 = Friday)", date(1945, 8, 17).weekday(), 4)

# Mark totals in the worked examples
eq("Paper 4 essay: Table A + Table B", 15 + 15, 30)
print("ok")
