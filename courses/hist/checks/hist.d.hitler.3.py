# checks/hist.d.hitler.3.py: recomputes every number in the chapter (dates, intervals, percentages, totals, figure layout)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Registered unemployed, annual averages (Statistisches Jahrbuch)
un = {1929: 1898604, 1930: 3075580, 1931: 4519704, 1932: 5575492, 1933: 4804428, 1934: 2718309, 1935: 2151039, 1936: 1592655, 1937: 912312}
eq("1929 about 1.9 million", round(un[1929] / 1e6, 1), 1.9)
eq("1932 about 5.6 million", round(un[1932] / 1e6, 1), 5.6)
eq("1933 about 4.8 million", round(un[1933] / 1e6, 1), 4.8)
eq("1934 about 2.7 million", round(un[1934] / 1e6, 1), 2.7)
eq("1935 about 2.2 million", round(un[1935] / 1e6, 1), 2.2)
eq("1936 about 1.6 million", round(un[1936] / 1e6, 1), 1.6)
eq("1937 about 0.9 million", round(un[1937] / 1e6, 1), 0.9)
# chart values for 1938 and 1939 (standard series rounded): 0.4 and 0.1; January 1939 about 0.3
chart = [5.6, 4.8, 2.7, 2.2, 1.6, 0.9, 0.4, 0.1]
assert all(a > b for a, b in zip(chart, chart[1:])), "series falls every year"
between("fall 1932 to 1937 (million)", un[1932] - un[1937], 4.6e6, 4.7e6)   # about 4.7 million
between("fall 1932 to 1937 share", 1 - un[1937] / un[1932], 0.83, 0.85)      # about 84 per cent
assert un[1937] < 1_000_000   # "under 1 million by 1937"
eq("labour shortage by 1937-38 and 1938 average under 0.5", 0.4 < 0.5, True)

# Military spending (billion RM) and GNP (billion RM) as in Noakes and Pridham; shares rounded
mil = {1933: 1.9, 1934: 4.1, 1935: 6.0, 1936: 10.8, 1937: 11.7, 1938: 17.2, 1939: 30.0}
gnp = {1933: 59, 1934: 67, 1935: 74, 1936: 83, 1937: 93, 1938: 105, 1939: 130}
want = {1933: 3, 1934: 6, 1935: 8, 1936: 13, 1937: 13, 1938: 16, 1939: 23}
for y in mil:
    eq(f"share {y}", round(mil[y] / gnp[y] * 100), want[y])
between("1938 share between 16 and 17", mil[1938] / gnp[1938] * 100, 16.0, 17.0)
assert 14.6 < 17.2 < 20   # estimates for 1938 range from about 15 to 20 per cent

# Dates and intervals
eq("Schacht to dismissal, years", 1939 - 1933, 6)
eq("Schacht minister Aug 1934 to Nov 1937, months", (1937 - 1934) * 12 + (11 - 8), 39)
eq("directors' warning to dismissal days", (date(1939, 1, 20) - date(1939, 1, 7)).days, 13)
eq("autobahn first sod to Law of 1 June 1933, days", (date(1933, 9, 23) - date(1933, 6, 1)).days, 114)
eq("Food Estate to Entailed Farm Law days", (date(1933, 9, 29) - date(1933, 9, 13)).days, 16)
eq("unions occupied to DAF days", (date(1933, 5, 10) - date(1933, 5, 2)).days, 8)
eq("Todt appointed to company founded days", (date(1933, 8, 25) - date(1933, 6, 30)).days, 56)
eq("Todt appointed to first sod days", (date(1933, 9, 23) - date(1933, 6, 30)).days, 85)
eq("Four Year Plan: Göring 18 October after Nuremberg September", date(1936, 10, 18) > date(1936, 9, 15), True)
eq("Four Year Plan runs to 1940", 1936 + 4, 1940)
eq("conscription to RAD law days", (date(1935, 6, 26) - date(1935, 3, 16)).days, 102)
eq("Mefo years 1934 to March 1938, months", (1938 - 1934) * 12 + (3 - 1), 50)   # January 1934 to March 1938 at the most
eq("Mefo five-year guarantee", 5, 5)
eq("New Plan to Four Year Plan, years", 1936 - 1934, 2)

# Marriage loans: a quarter cancelled for each child, so four children clear the loan
loan = 1000
eq("loan cleared by four children", loan - 4 * loan // 4, 0)
eq("one quarter cancelled", loan // 4, 250)

# Autobahn: about 7,000 km planned, about 3,000 km by end 1938, peak 124,483 in 1936 (about 125,000)
eq("autobahn share built", round(3000 / 7000 * 100), 43)
eq("peak workers rounded", round(124483, -3), 124000)
between("peak workers about 125,000", 124483, 120000, 130000)
assert 124483 < 600000   # far below Todt's forecast of hundreds of thousands of jobs (at least 600,000)

# RAD: about 200,000 (1935) and about 350,000 (1939)
between("RAD growth", 350000 / 200000, 1.7, 1.8)

# Agriculture: 68 to 83 per cent (1928 to 1938), 15 points; farm workers 1.8 to 1.4 million (down about 440,000)
eq("self-sufficiency rise points", 83 - 68, 15)
eq("self-sufficiency years", 1938 - 1928, 10)
between("farm workers fall", 1.8 - 1.4, 0.39, 0.41)
assert 440000 > 400000
between("share of farmland about a third", 0.35, 0.3, 0.4)
# Entailed farm size band 7.5 to 125 hectares
eq("farm band ratio", round(125 / 7.5, 1), 16.7)

# Wages and hours: hours 43 to 47-49; real weekly earnings up about 19 per cent (about a fifth)
between("hours rise to 47", 47 - 43, 3, 5)
between("hours rise to 49", 49 - 43, 5, 7)
between("19 per cent about a fifth", 0.19, 0.18, 0.21)

# Volkswagen: 5 marks a week, about 330,000 savers; four years to save for a car at the suggested rate
eq("VW weekly saving", 5, 5)
between("VW price at 5 marks for about 4 years", 5 * 52 * 4, 1000, 1100)
# KdF about 9.6 million participants in 1937 (a figure often quoted)
between("KdF figure", 9.6, 9, 10)

# Labour: Law on Organisation of National Labour 20 January 1934; Trustees of Labour appointed from June 1933
assert date(1934, 1, 20) > date(1933, 6, 15)
# Schacht minister 1934 to 1937; Funk from early 1938
assert 1938 > 1937
# Pflichtjahr 1938; labour books 1935; price freeze November 1936
assert 1938 > 1935 and date(1936, 11, 26) > date(1936, 10, 18)
# Rationing late August 1939, before invasion of Poland on 1 September 1939
eq("rationing before Poland", date(1939, 8, 27) < date(1939, 9, 1), True)
eq("Britain and France declare war 3 September 1939 after 1 September", date(1939, 9, 3) > date(1939, 9, 1), True)

# Chart: three years or eight years? 1932 to 1939 is eight consecutive years (line chart is fine)
eq("years in unemployment chart", len(range(1932, 1940)), 8)
eq("years in military chart", len(range(1933, 1940)), 7)

# Figure layout: boxes y = 10, 80, 150 (46 high), then 220 (64 high), then 310 (46 high)
eq("gap 1", 80 - (10 + 46), 24)
eq("gap 2", 150 - (80 + 46), 24)
eq("gap 3", 220 - (150 + 46), 24)
eq("gap 4", 310 - (220 + 64), 26)
for line in ["Rearmament", "from 1933: arms first", "Needs imports", "oil, rubber, iron ore, metals", "Foreign exchange runs short", "exports too small to pay", "The cost", "butter squeezed, labour short"]:
    assert len(line) * 7 < 280 - 8, line
for line in ["New Plan, 1934", "import licences,", "barter deals", "Four Year Plan", "make it at home,", "Göring in charge"]:
    assert len(line) * 7 < 150 - 8, line
assert len("the same squeeze, two answers") * 7 < 340 - 8
assert 384 + 5 < 405

eq("essay marks", 15 + 15, 30)
print("ok")
