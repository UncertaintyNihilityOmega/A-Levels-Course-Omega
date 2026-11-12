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
# Stalin
eq("General Secretary 3 April 1922 to Lenin's death 21 January 1924 (days)", (date(1924, 1, 21) - date(1922, 4, 3)).days, 658)
eq("Lenin's funeral 27 January 1924 is 6 days after death", (date(1924, 1, 27) - date(1924, 1, 21)).days, 6)
eq("Testament postscript 4 Jan 1923 to Thirteenth Congress opens 23 May 1924 (days)", (date(1924, 5, 23) - date(1923, 1, 4)).days, 505)
eq("Lenin Enrolment 240,000 on 446,000", 446000 + 240000, 686000)
eq("expulsions 12-14 November 1927 span three days", (date(1927, 11, 14) - date(1927, 11, 12)).days + 1, 3)
eq("Trotsky exile Jan 1928 to deportation Feb 1929 (months)", (1929 - 1928) * 12 + (2 - 1), 13)
eq("struggle years 1924-29", 1929 - 1924, 5)
# Hitler
eq("Nazi seats Nov 1932 down from July (seats)", 230 - 196, 34)
eq("Nazi vote Sept 1930 to July 1932 (points)", round(37.3 - 18.3, 1), 19.0)
eq("Nazi vote fell Jul to Nov 1932 (points)", round(37.3 - 33.1, 1), 4.2)
eq("Cologne meeting to appointment (days)", (date(1933, 1, 30) - date(1933, 1, 4)).days, 26)
eq("Schleicher fell 28 Jan, Hitler sworn in 30 Jan (days)", (date(1933, 1, 30) - date(1933, 1, 28)).days, 2)
eq("Nazi ministers 3 of 11", (3, 11), (3, 11))
eq("rule by decree 30 March 1930 to appointment (years, months)", (1933 - 1930, 1 - 3), (3, -2))

# Section B: Truman and Eisenhower
eq("NATO to NSC-68 approval (years)", 1950 - 1949, 1)
eq("defence spending rise 14 to over 50 billion dollars: factor about 3.6", round(50 / 14, 1), 3.6)
eq("Geneva Summit 18-23 July 1955 is six days", (date(1955, 7, 23) - date(1955, 7, 18)).days + 1, 6)
eq("U-2 shot down 1 May to Paris summit 16 May 1960 (days)", (date(1960, 5, 16) - date(1960, 5, 1)).days, 15)
eq("Guatemala 18-27 June 1954: 9 days", (date(1954, 6, 27) - date(1954, 6, 18)).days, 9)
eq("Eisenhower Doctrine 5 January 1957 to Hungary 4 November 1956 (days)", (date(1957, 1, 5) - date(1956, 11, 4)).days, 62)
# Civil rights
eq("Mississippi registration rise (factor about 8.9)", round(59.8 / 6.7, 1), 8.9)
eq("Selma 7 March to VRA 6 August 1965 (days)", (date(1965, 8, 6) - date(1965, 3, 7)).days, 152)
eq("Selma to VRA is within five months", (8 - 3), 5)
eq("Birmingham children 2-3 May to Kennedy's address 11 June 1963 (days)", (date(1963, 6, 11) - date(1963, 5, 2)).days, 40)
eq("Black elected officials 1,500 to 3,500 (rise)", 3500 - 1500, 2000)
eq("income share rise 51 to 61 per cent", 61 - 51, 10)
eq("Black unemployment about twice", 2 * 1, 2)
# Reagan
eq("Reagan electoral votes 489 + 49 = 538", 489 + 49, 538)
eq("1980 shares sum", round(50.7 + 41.0 + 6.6, 1), 98.3)
eq("popular votes Reagan 43.9 m to Carter 35.5 m (difference)", round(43.9 - 35.5, 1), 8.4)
eq("hostage days 4 Nov 1979 to 20 Jan 1981", (date(1981, 1, 20) - date(1979, 11, 4)).days, 443)
eq("Carter approval fall 75 to 28 (points)", 75 - 28, 47)
eq("Kennedy challenge 7 Nov 1979 to election 4 Nov 1980 (days)", (date(1980, 11, 4) - date(1979, 11, 7)).days, 363)
eq("Carter's 1976 margin 297 to 240", 297 - 240, 57)

# Section C: Soviet Empire
eq("East German rising 16-17 June 1953: two days", (date(1953, 6, 17) - date(1953, 6, 16)).days + 1, 2)
eq("Hungary: rising 23 Oct to attack 4 Nov (days)", (date(1956, 11, 4) - date(1956, 10, 23)).days, 12)
eq("Nagy hanged 16 June 1958 is 19 months after the attack", (1958 - 1956) * 12 + (6 - 11), 19)
eq("Czech invasion 20-21 August; Moscow Protocol 26 August: 6 days after the 20th", (date(1968, 8, 26) - date(1968, 8, 20)).days, 6)
eq("Warsaw Pact 14 May 1955", date(1955, 5, 14).year, 1955)
eq("Berlin Wall 1961 minus 1949 (years of emigration)", 1961 - 1949, 12)
eq("period 1953-68 is 15 years", 1968 - 1953, 15)
eq("Wyszynski arrested 25 Sep 1953, released 28 Oct 1956 (about three years)", round((date(1956, 10, 28) - date(1953, 9, 25)).days / 365.25), 3)
eq("Kadar slogan year to Prague Spring (years)", 1968 - 1961, 7)
eq("force crises in 1953, 1956, 1968", len([1953, 1956, 1968]), 3)
# South Africa
eq("Sharpeville 21 March to emergency 30 March 1960 (days)", (date(1960, 3, 30) - date(1960, 3, 21)).days, 9)
eq("emergency 30 March to 31 August 1960 (days)", (date(1960, 8, 31) - date(1960, 3, 30)).days, 154)
eq("ANC banned 8 April: 18 days after Sharpeville", (date(1960, 4, 8) - date(1960, 3, 21)).days, 18)
eq("Sharpeville to MK launch (years, months)", (1961 - 1960) * 12 + (12 - 3), 21)
eq("Sharpeville to Soweto (years)", 1976 - 1960, 16)
eq("Resolution 134 on 1 April 1960 is 11 days after the shooting", (date(1960, 4, 1) - date(1960, 3, 21)).days, 11)
eq("Rivonia raid to sentence (days)", (date(1964, 6, 12) - date(1963, 7, 11)).days, 337)
eq("embargo 1963 to mandatory 1977 (years)", 1977 - 1963, 14)
eq("death toll difference 91 - 69", 91 - 69, 22)
# Indonesia
eq("proclamation to sovereignty (years)", 1949 - 1945, 4)
eq("Dutch: proclamation 17 Aug 1945 to sovereignty 27 Dec 1949 (days)", (date(1949, 12, 27) - date(1945, 8, 17)).days, 1593)
eq("Round Table 23 Aug to 2 Nov 1949 (days)", (date(1949, 11, 2) - date(1949, 8, 23)).days, 71)
eq("Roem-Van Roijen to sovereignty (days)", (date(1949, 12, 27) - date(1949, 5, 7)).days, 234)
eq("second police action to Roem-Van Roijen (days)", (date(1949, 5, 7) - date(1948, 12, 19)).days, 139)
eq("Linggadjati initialled to signed (days)", (date(1947, 3, 25) - date(1946, 11, 15)).days, 130)
eq("first police action to Renville (days)", (date(1948, 1, 17) - date(1947, 7, 21)).days, 180)
print("ok")
