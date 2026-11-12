# checks/hist.mock.p4.py: recomputes every number in the chapter (paper facts, level ranges, mark totals, dates, intervals, sums)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper: 1 h 45 min = 105 min; 60 marks = 2 x 30; each essay 30 = 15 (AO2) + 15 (AO1); nine questions, three per section
eq("minutes", 1 * 60 + 45, 105)
eq("total", 30 + 30, 60)
eq("essay marks", 15 + 15, 30)
eq("questions", 3 * 3, 9)
eq("plan 6 + 46 + 46 + 7", 6 + 46 + 46 + 7, 105)
eq("each essay 4 + 42", 4 + 42, 46)

# Levels: five contiguous bands to 15 in each table; totals at the same level in both tables
T = {5: (13, 15), 4: (10, 12), 3: (7, 9), 2: (4, 6), 1: (1, 3)}
prev = 16
for lvl in (5, 4, 3, 2, 1):
    lo, hi = T[lvl]
    eq(f"level {lvl} contiguous", hi, prev - 1)
    prev = lo
eq("bottom", prev, 1)
want = {5: (26, 30), 4: (20, 24), 3: (14, 18), 2: (8, 12), 1: (2, 6)}
for lvl, (lo, hi) in T.items():
    eq(f"both tables level {lvl}", (2 * lo, 2 * hi), want[lvl])

# Section A: Italy
eq("Lateran compensation 750 + 1,000 million lire", 750 + 1000, 1750)
eq("Roman Question 1870 to 1929 (years)", 1929 - 1870, 59)
eq("plebiscite 24 March 1929 is 41 days after 11 February", (date(1929, 3, 24) - date(1929, 2, 11)).days, 41)
eq("Non abbiamo bisogno 29 June 1931", date(1931, 6, 29).year - date(1929, 2, 11).year, 2)
# Stalin: collective security
eq("years 1933-39", 1939 - 1933, 6)
eq("Franco-Soviet (2 May) to Czech treaty (16 May 1935) (days)", (date(1935, 5, 16) - date(1935, 5, 2)).days, 14)
eq("Seventh Congress 25 July to 20 August 1935 (days, inclusive)", (date(1935, 8, 20) - date(1935, 7, 25)).days + 1, 27)
eq("Litvinov's proposal 17 March to Munich 29 September 1938 (days)", (date(1938, 9, 29) - date(1938, 3, 17)).days, 196)
eq("Munich 29-30 September is two days", (date(1938, 9, 30) - date(1938, 9, 29)).days + 1, 2)
eq("Polish guarantee 31 March to the mission's arrival 11 August 1939 (days)", (date(1939, 8, 11) - date(1939, 3, 31)).days, 133)
eq("Litvinov dismissed 3 May to Pact 23 August 1939 (days)", (date(1939, 8, 23) - date(1939, 5, 3)).days, 112)
eq("mission arrives 11 August, Pact 23 August (days)", (date(1939, 8, 23) - date(1939, 8, 11)).days, 12)
eq("Pact 23 August to Soviet invasion of Poland 17 September 1939 (days)", (date(1939, 9, 17) - date(1939, 8, 23)).days, 25)
eq("Tukhachevsky tried 11 June, shot 12 June 1937 (days)", (date(1937, 6, 12) - date(1937, 6, 11)).days, 1)
eq("commanders killed 13 of 15 and marshals 3 of 5 (survivors)", (15 - 13, 5 - 3), (2, 2))
# Hitler
eq("Nazi seats Nov 1932 down from July (seats)", 230 - 196, 34)
eq("Nazi vote Sept 1930 to July 1932 (points)", round(37.3 - 18.3, 1), 19.0)
eq("Nazi vote fell Jul to Nov 1932 (points)", round(37.3 - 33.1, 1), 4.2)
eq("Cologne meeting to appointment (days)", (date(1933, 1, 30) - date(1933, 1, 4)).days, 26)
eq("Schleicher fell 28 Jan, Hitler sworn in 30 Jan (days)", (date(1933, 1, 30) - date(1933, 1, 28)).days, 2)
eq("Nazi ministers 3 of 11", (3, 11), (3, 11))
eq("rule by decree 30 March 1930 to appointment (years, months)", (1933 - 1930, 1 - 3), (3, -2))

# Section B: Truman and the 1948 election
eq("electoral votes 303 + 189 + 39 + 0", 303 + 189 + 39 + 0, 531)
eq("needed to win (majority of 531)", 531 // 2 + 1, 266)
eq("Thurmond: four states' 38 votes plus one faithless elector", 38 + 1, 39)
eq("Ohio + California + Illinois electoral votes", 25 + 25 + 28, 78)
eq("their margins together (about 58,600)", round((7107 + 17865 + 33612) / 100) * 100, 58600)
eq("Truman without the three states", 303 - 78, 225)
eq("Dewey with all three has 267", 189 + 78, 267)
eq("Truman if he lost the two smallest-value pairs (Ohio and California)", 303 - 50, 253)
eq("Truman if he lost California and Illinois (the largest pair)", 303 - 53, 250)
assert 253 < 266 and 250 < 266
eq("popular shares sum", round(49.5 + 45.1 + 2.4 + 2.4, 1), 99.4)
eq("Gallup lead 49.5 - 44.5", round(49.5 - 44.5, 1), 5.0)
eq("Gallup 15-25 October (days)", (date(1948, 10, 25) - date(1948, 10, 15)).days, 10)
eq("convention plank 651.5 to 582.5 (margin)", 651.5 - 582.5, 69.0)
eq("convention speech 15 July to Turnip Day 26 July (days)", (date(1948, 7, 26) - date(1948, 7, 15)).days, 11)
eq("civil rights message 2 Feb to election 2 Nov 1948 (days)", (date(1948, 11, 2) - date(1948, 2, 2)).days, 274)
# Women's movement
eq("years 1963-74", 1974 - 1963, 11)
eq("labour-force rise 1960 to 1970 (points)", round(43.3 - 37.7, 1), 5.6)
eq("labour-force rise 1960 to 1974 (points)", round(45.7 - 37.7, 1), 8.0)
eq("pay ratio fell 60.7 to 59.4 (points)", round(60.7 - 59.4, 1), 1.3)
eq("three-quarters of 50 states, rounded up", -(-3 * 50 // 4), 38)
eq("ERA short by 3 states in 1977", 38 - 35, 3)
eq("ERA passed 22 March 1972 to Title IX 23 June 1972 (days)", (date(1972, 6, 23) - date(1972, 3, 22)).days, 93)
eq("ERA passed 22 March 1972 to Roe 22 January 1973 (days)", (date(1973, 1, 22) - date(1972, 3, 22)).days, 306)
eq("Roe 7 to 2", 7 + 2, 9)
# Carter's foreign policy
eq("Carter's term 1977-81 (years)", 1981 - 1977, 4)
eq("inaugural 20 Jan to Notre Dame 22 May 1977 (days)", (date(1977, 5, 22) - date(1977, 1, 20)).days, 122)
eq("Senate vote 68-32 is 100 senators", 68 + 32, 100)
eq("two-thirds of 100 is 67, so 68 is one over", 68 - 67, 1)
eq("Shah toast 31 Dec 1977 to Shah leaves 16 Jan 1979 (days)", (date(1979, 1, 16) - date(1977, 12, 31)).days, 381)
eq("Camp David 5-17 September 1978 (days, inclusive)", (date(1978, 9, 17) - date(1978, 9, 5)).days + 1, 13)
eq("Camp David to treaty 26 March 1979 (days)", (date(1979, 3, 26) - date(1978, 9, 17)).days, 190)
eq("Pinochet in power to 1990 after Carter's term (years)", 1990 - 1977, 13)

# Section C: Gorbachev
eq("years 1985-91", 1991 - 1985, 6)
eq("growth slowed 4.9 to 1.8 (points)", round(4.9 - 1.8, 1), 3.1)
eq("oil price 30 to 10 dollars: fall by more than half", 10 < 30 / 2, True)
eq("hard-currency debt: low and high multiples of 26 billion", (round(55 / 26, 1), round(80 / 26, 1)), (2.1, 3.1))
eq("note withdrawal 22 January to price rises 2 April 1991 (days)", (date(1991, 4, 2) - date(1991, 1, 22)).days, 70)
eq("INF Treaty 8 December 1987 to the UN speech 7 December 1988 (days)", (date(1988, 12, 7) - date(1987, 12, 8)).days, 365)
eq("Law on Cooperatives 26 May 1988 to Russia's sovereignty 12 June 1990 (days)", (date(1990, 6, 12) - date(1988, 5, 26)).days, 747)
eq("alcohol decree 7 May 1985 to Chernobyl 26 April 1986 (days)", (date(1986, 4, 26) - date(1985, 5, 7)).days, 354)
# South Africa: the 1948 election
eq("HNP + Afrikaner Party seats", 70 + 9, 79)
eq("total seats 79 + 71", 79 + 71, 150)
eq("majority of 150", 150 // 2 + 1, 76)
eq("HNP + AP share 37.7 + 3.9", round(37.7 + 3.9, 1), 41.6)
eq("HNP + AP votes", 401834 + 41885, 443719)
eq("votes per seat, NP and AP (about 5,600)", round(443719 / 79, -2), 5600)
eq("votes per seat, UP and Labour (about 7,800) from 51.7 per cent of 1,065,971", round(0.517 * 1065971 / 71, -2), 7800)
eq("1939 war vote 80 to 67 (margin)", 80 - 67, 13)
eq("Broederbond 1918 to the election (years)", 1948 - 1918, 30)
eq("Voortrekker Centenary 1938 to the election (years)", 1948 - 1938, 10)
eq("election 26 May 1948 is three months after the Fagan Report (February)", 5 - 2, 3)
# Indonesia
eq("proclamation to sovereignty (years)", 1949 - 1945, 4)
eq("Dutch: proclamation 17 Aug 1945 to sovereignty 27 Dec 1949 (days)", (date(1949, 12, 27) - date(1945, 8, 17)).days, 1593)
eq("Round Table 23 Aug to 2 Nov 1949 (days)", (date(1949, 11, 2) - date(1949, 8, 23)).days, 71)
eq("Roem-Van Roijen to sovereignty (days)", (date(1949, 12, 27) - date(1949, 5, 7)).days, 234)
eq("second police action to Roem-Van Roijen (days)", (date(1949, 5, 7) - date(1948, 12, 19)).days, 139)
eq("Linggadjati initialled to signed (days)", (date(1947, 3, 25) - date(1946, 11, 15)).days, 130)
eq("first police action to Renville (days)", (date(1948, 1, 17) - date(1947, 7, 21)).days, 180)
print("ok")
