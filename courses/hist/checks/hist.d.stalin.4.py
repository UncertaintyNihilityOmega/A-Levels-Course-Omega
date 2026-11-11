# checks/hist.d.stalin.4.py: recomputes every number in the chapter (dates, intervals, percentages, totals, figure layout)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Zhenotdel: 1919 to January 1930
eq("zhenotdel years", 1930 - 1919, 11)
# Abortion legal from November 1920 to the ban of 27 June 1936: 15 years 7 months
eq("abortion legal months", (1936 - 1920) * 12 + (6 - 11), 15 * 12 + 7)
# Draft law published 26 May 1936 -> decree 27 June 1936: 32 days
eq("draft to decree", (date(1936, 6, 27) - date(1936, 5, 26)).days, 32)
# Decree 27 June to Constitution 5 December 1936
assert date(1936, 12, 5) > date(1936, 6, 27)
# Divorce fees 50, 150, 300
fees = [50, 150, 300]
eq("fee ratio", fees[2] / fees[0], 6)
# Allowance: 2,000 roubles a year for five years = 10,000 per child
eq("allowance per child", 2000 * 5, 10000)
# Maintenance shares: one quarter, one third, one half
assert 0.25 < 1 / 3 < 0.5

# Recorded abortions 1,900 thousand (1935) to 570 thousand (1937) to 755 thousand (1939)
a35, a37, a39 = 1900, 570, 755
between("abortion fall 1935-37", 1 - a37 / a35, 0.69, 0.71)   # about 70 per cent
assert a39 > a37
# Infant mortality 146 to 162 per thousand (1935 to 1938)
between("infant mortality rise", 162 / 146 - 1, 0.10, 0.12)
eq("infant mortality rise points", 162 - 146, 16)

# Women's share of the workforce: 24 per cent (1928) to 39 per cent (1940): up 15 points
eq("women share rise", 39 - 24, 15)
assert 39 / 24 > 1.6

# Literacy, population aged 9 and over: 51.1 (1926 census) to 81.2 (1939 census), "about 51" and "about 81"
# (56.6 is the 1926 figure for ages 9-49 only, so it must not be paired with 81.2)
eq("literacy 1926", round(51.1), 51)
eq("literacy 1939", round(81.2), 81)
between("literacy rise", 81.2 - 51.1, 30.0, 30.2)

# Koreans: about 172,000 (171,781 in 36,442 families); decree 21 August 1937, deportation September-October
between("koreans", 171781, 170000, 173000)
between("persons per family", 171781 / 36442, 4.6, 4.8)
assert date(1937, 8, 21) < date(1937, 9, 30)
# Polish operation: more than 100,000 shot (111,091 in NKVD records)
assert 111091 > 100000
# Russian made compulsory 13 March 1938
assert date(1938, 3, 13) > date(1937, 12, 31)

# Writers' Congress: 17 August to 1 September 1934 = 16 days inclusive
eq("congress days", (date(1934, 9, 1) - date(1934, 8, 17)).days + 1, 16)
# Stalin attends Lady Macbeth on 26 January 1936, Pravda attack on 28 January: two days
eq("pravda after visit", (date(1936, 1, 28) - date(1936, 1, 26)).days, 2)
# RAPP dissolved 23 April 1932; congress two years and four months later
eq("rapp to congress months", (1934 - 1932) * 12 + (8 - 4), 28)
# Census 6 January 1937: 55.3 million believers and 42.2 million non-believers among those aged 16+ who answered,
# i.e. 56.7 per cent of respondents, "about 57 per cent"
between("believers share", 55.3 / (55.3 + 42.2) * 100, 56.5, 57.0)
eq("believers rounded", round(55.3 / (55.3 + 42.2) * 100), 57)
# Census years
eq("1937 to 1939 census", 1939 - 1937, 2)
# Cathedral destroyed 5 December 1931; Law on Religious Associations 8 April 1929: 2 years 8 months
eq("law to cathedral months", (1931 - 1929) * 12 + (12 - 4), 32)
# League of the Militant Godless 1925; Sergii declaration 29 July 1927
assert date(1927, 7, 29) > date(1925, 12, 31)
# Komsomol about 2 million to about 10 million: five-fold
eq("komsomol growth", round(10 / 2), 5)
# Pioneers founded 1922, Komsomol 1918: 4 years
eq("pioneers after komsomol", 1922 - 1918, 4)
# Constitution: eleven republics
republics = ["RSFSR", "Ukraine", "Belorussia", "Armenia", "Azerbaijan", "Georgia", "Kazakhstan", "Kirghizia", "Uzbekistan", "Turkmenistan", "Tajikistan"]
eq("republics", len(republics), 11)

# Figure layout: boxes y = 10, 80, 150 (46 high), then 220 (64 high), then 310 (46 high)
eq("gap 1", 80 - (10 + 46), 24)
eq("gap 2", 150 - (80 + 46), 24)
eq("gap 3", 220 - (150 + 46), 24)
eq("gap 4", 310 - (220 + 64), 26)
# Text widths at about 7 px per character: wide boxes 280 wide, small boxes 150 wide
for line in ["Stalin, Zhdanov, Central Committee", "Creative unions (from 1932)", "Glavlit; Pravda sets the line", "works must serve the party"]:
    assert len(line) * 7 < 280 - 8, line
for line in ["publication, prizes,", "attack, silence,", "arrest, execution", "flats and dachas"]:
    assert len(line) * 7 < 150 - 8, line
assert len("control from above, by carrot and stick") * 7 < 340 - 8
assert 384 + 5 < 405

eq("essay marks", 15 + 15, 30)
print("ok")
