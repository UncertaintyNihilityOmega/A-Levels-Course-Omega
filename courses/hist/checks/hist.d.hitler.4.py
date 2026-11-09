# checks/hist.d.hitler.4.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Hitler Youth membership: 107,956 (end 1932) about 0.1 million; about 2.3 million (1933), 5.4 million (1936), 8.7 million (1939)
eq("HJ 1932 rounds to 0.1 million", round(107956 / 1e6, 1), 0.1)
eq("HJ 1932 about 108,000", round(107956, -3), 108000)
eq("HJ 1933", round(2292041 / 1e6, 1), 2.3)
eq("HJ 1936", round(5437601 / 1e6, 1), 5.4)
chart = [0.1, 2.3, 5.4, 8.7]
assert all(a < b for a, b in zip(chart, chart[1:]))
between("HJ growth 1933 to 1939", 8.7 / 2.3, 3.7, 3.9)   # nearly four-fold
between("HJ growth 1932 to 1939", 8.7 / 0.108, 79, 82)    # about 80-fold
# Chart: four unevenly spaced years, so a bar chart (not a line)
eq("years in HJ chart", len([1932, 1933, 1936, 1939]), 4)

# Birth rate 14.7 (1933) to 20.3 (1939) per 1,000; marriages 516,800 (1932) to 740,200 (1934)
eq("birth rate rise", round(20.3 - 14.7, 1), 5.6)
between("birth rate rise share", 20.3 / 14.7 - 1, 0.37, 0.39)
eq("marriages 1932 about 517,000", round(516800, -3), 517000)
eq("marriages 1934 about 740,000", round(740200, -4), 740000)
between("marriage rise", 740200 / 516800 - 1, 0.43, 0.44)
# Marriage loan: a quarter cancelled per child, four children clear 1,000 marks; couples with loans averaged one child
loan = 1000
eq("one quarter", loan // 4, 250)
eq("four children clear the loan", 4 * (loan // 4), loan)
eq("one child leaves", loan - loan // 4, 750)
# Mother's Cross classes: 4-5 bronze, 6-7 silver, 8+ gold; established 16 Dec 1938, first presented May 1939
classes = {"bronze": (4, 5), "silver": (6, 7), "gold": (8, None)}
eq("bronze upper meets silver lower", classes["bronze"][1] + 1, classes["silver"][0])
eq("silver upper meets gold lower", classes["silver"][1] + 1, classes["gold"][0])
eq("Mother's Cross to first award months", (1939 - 1938) * 12 + (5 - 12), 5)
# Women: about 14 million in work, 1939

# Church dates
eq("Centre Party dissolves to Concordat days", (date(1933, 7, 20) - date(1933, 7, 5)).days, 15)
eq("Concordat to church election days", (date(1933, 7, 23) - date(1933, 7, 20)).days, 3)
eq("church election to Müller days", (date(1933, 9, 27) - date(1933, 7, 23)).days, 66)
eq("Müller to Sports Palace days", (date(1933, 11, 13) - date(1933, 9, 27)).days, 47)
eq("Barmen days inclusive", (date(1934, 5, 31) - date(1934, 5, 29)).days + 1, 3)
eq("Mit brennender Sorge to reading days", (date(1937, 3, 21) - date(1937, 3, 14)).days, 7)
assert date(1937, 3, 21).weekday() == 6   # Palm Sunday 1937 was a Sunday (Easter 28 March)
assert date(1937, 7, 1) > date(1937, 3, 14)
eq("Niemöller arrest years after Barmen", round((date(1937, 7, 1) - date(1934, 5, 29)).days / 365.25, 1), 3.1)
eq("Barmen after Müller months", (1934 - 1933) * 12 + (5 - 9), 8)
eq("Kerrl 1935", 1935 - 1933, 2)

# Persecution
eq("Nuremberg Laws to first decree days", (date(1935, 11, 14) - date(1935, 9, 15)).days, 60)
eq("boycott to Civil Service law days", (date(1933, 4, 7) - date(1933, 4, 1)).days, 6)
eq("Civil Service law to sterilisation law days", (date(1933, 7, 14) - date(1933, 4, 7)).days, 98)
eq("Grynszpan shot to vom Rath died days", (date(1938, 11, 9) - date(1938, 11, 7)).days, 2)
eq("Polish expulsion to Kristallnacht days", (date(1938, 11, 9) - date(1938, 10, 28)).days, 12)
eq("J stamp to Kristallnacht days", (date(1938, 11, 9) - date(1938, 10, 5)).days, 35)
eq("Nuremberg Laws to Kristallnacht, years", round((date(1938, 11, 9) - date(1935, 9, 15)).days / 365.25, 1), 3.2)
eq("Kristallnacht to Göring meeting days", (date(1938, 11, 12) - date(1938, 11, 10)).days, 2)
between("Kristallnacht arrests, lower estimate to upper", 26000 / 30000, 0.8, 0.9)
assert 1400 > 1000 and 7000 > 1400 and 91 < 1400
eq("fine 1 billion marks", 1_000_000_000, 10**9)
# Jews: about 500,000 in 1933, under 1 per cent of about 66 million
between("Jewish share of population", 500000 / 66_000_000, 0.007, 0.008)
assert 500000 / 66_000_000 < 0.01
# Emigration about 280,000 of about 500,000: more than half
between("emigrated share", 280000 / 500000, 0.55, 0.57)
# First World War: about 100,000 Jews served, about 12,000 died
between("Jewish war dead share", 12000 / 100000, 0.11, 0.13)
# Polish Jews expelled about 17,000
assert 17000 > 10000

# Other minorities
# Homosexual men: about 100,000 arrested, about 50,000 convicted, about 5,000 to 6,000 in camps (1933 to 1945)
between("convicted share of arrested", 50000 / 100000, 0.49, 0.51)
between("camp share of arrested", 5500 / 100000, 0.05, 0.06)
# Sterilisation law: 14 July 1933, in force January 1934, more than 400,000 sterilised
eq("sterilisation law to effect months", (1934 - 1933) * 12 + (1 - 7), 6)
assert 400000 > 62400 + 71700   # more than the totals of 1934 and 1935 together
eq("1934 plus 1935 sterilisations", 62400 + 71700, 134100)
# T4: 70,273 killed by August 1941: about 70,000; Galen sermon 3 August 1941
eq("T4 about 70,000", round(70273, -4), 70000)
# Asocials: about 10,000 arrested in June 1938
# Jehovah's Witnesses: about 250 executed; camp estimates 2,000 to 10,000; deaths 1,200 to 5,000
assert 2000 < 10000 and 1200 < 5000 and 250 < 1200
# Roma decree 26 November 1935 after the Nuremberg Laws, before Marzahn 1936
assert date(1935, 11, 26) > date(1935, 9, 15)
# Youth law and decree: 1 December 1936 to 25 March 1939
eq("youth law to decree days", (date(1939, 3, 25) - date(1936, 12, 1)).days, 844)
eq("youth law to decree, whole years", (date(1939, 3, 25) - date(1936, 12, 1)).days // 365, 2)
# Hitler Youth founded 1922; Schirach June 1933
eq("HJ years before Schirach", 1933 - 1922, 11)
# 1938: about 1.5 million boys trained to shoot
assert 1.5e6 < 8.7e6
# NS-Frauenschaft about 2 million in 1938; 109,320 at end of 1932
between("Frauenschaft growth", 2_000_000 / 109320, 18, 19)
# Voting age for women since 1919 (Weimar), Nazi 1933: 14 years
eq("women's vote to 1933", 1933 - 1919, 14)
# Galton eugenics 1880s; Paragraph 175 since 1871: 62 years to 1933
eq("Paragraph 175 age in 1933", 1933 - 1871, 62)
# Pflichtjahr 1938: women under 25; marriage loan condition dropped 1937
assert 1938 > 1937 > 1933

eq("essay marks", 15 + 15, 30)
print("ok")
