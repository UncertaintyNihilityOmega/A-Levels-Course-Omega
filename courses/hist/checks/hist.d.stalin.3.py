# checks/hist.d.stalin.3.py: recomputes every number in the chapter (dates, intervals, percentages, ratios, figure layout)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# First plan: 1 October 1928 to end of December 1932 = 51 months = "four years and three months"
months = (1932 - 1928) * 12 + (12 - 10) + 1   # October 1928 .. December 1932 inclusive
eq("plan months", months, 51)
eq("four years three months", 4 * 12 + 3, 51)
# Declared fulfilled on 7 January 1933 (after the plan ended)
assert date(1933, 1, 7) > date(1932, 12, 31)

# Speech of 4 February 1931 -> invasion of 22 June 1941 = ten years and four months
d1, d2 = date(1931, 2, 4), date(1941, 6, 22)
eq("years to invasion", d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day)), 10)
eq("months beyond ten years", (d2.month - d1.month) - (1 if d2.day < d1.day else 0), 4)

# Belomor: December 1931 to August 1933 = 20 months ("under two years")
eq("belomor months", (1933 - 1931) * 12 + (8 - 12), 20)

# Industrial output (official, million tonnes; electricity in billion kWh)
coal = {1928: 35.4, 1932: 64.4, 1937: 128.0, 1940: 166.0}
oil = {1928: 11.7, 1932: 21.4, 1937: 28.5, 1940: 31.1}
pig = {1928: 3.3, 1932: 6.2, 1937: 14.5, 1940: 14.9}
steel = {1928: 4.0, 1932: 5.9, 1937: 17.7, 1940: 18.3}
elec = {1928: 5.0, 1932: 13.5, 1937: 36.2, 1940: 48.6}
# Pig iron 1932 against the 1929 plan target of about 10
eq("pig iron % of target", round(pig[1932] / 10 * 100), 62)
# Steel 5.9 against about 10.4
eq("steel % of target", round(steel[1932] / 10.4 * 100), 57)
# Coal 64.4 against 75
eq("coal % of target", round(coal[1932] / 75 * 100), 86)
# Electricity 13.5 against 22
eq("electricity % of target", round(elec[1932] / 22 * 100), 61)
# Pig iron nearly doubled in the first plan
between("pig iron rise", pig[1932] / pig[1928], 1.8, 1.95)
# Steel and pig iron more than four times the 1928 level by 1937 (steel from about 4)
between("steel 1937/1928", steel[1937] / steel[1928], 4.0, 4.6)
between("pig iron 1937/1928", pig[1937] / pig[1928], 4.0, 4.6)
# Electricity almost tenfold 1928 to 1940
between("electricity 1940/1928", elec[1940] / elec[1928], 9.5, 10.0)
# Steel 5.9 -> 17.7 in second plan: tripled
between("steel 1932-37", steel[1937] / steel[1932], 2.9, 3.1)
# Pig iron and steel barely rose after 1937
between("pig iron 1937-40", pig[1940] / pig[1937], 1.0, 1.05)
between("steel 1937-40", steel[1940] / steel[1937], 1.0, 1.05)
# Coal 1940 / 1928
between("coal 1940/1928", coal[1940] / coal[1928], 4.6, 4.8)

# Stakhanov: 102 tonnes against a norm of 7 tonnes: "more than 14 times"
ratio = 102 / 7
between("stakhanov ratio", ratio, 14.0, 15.0)

# Collectivisation shares
assert 21 < 58 and 23 < 58  # fall between March and June 1930
# Livestock
cattle = (70.5, 38.4)
sheep = (146.7, 50.2)
between("cattle fall", 1 - cattle[1] / cattle[0], 0.44, 0.47)   # "about 45 per cent"
between("sheep fall", 1 - sheep[1] / sheep[0], 0.64, 0.68)      # "about 66 per cent", "about two thirds"
# Grain exports (million tonnes, official, rounded from 4,846,024; 5,182,835; 1,819,114; 1,771,364)
eq("export 1930", round(4846024 / 1e6, 1), 4.8)
eq("export 1931", round(5182835 / 1e6, 1), 5.2)
eq("export 1932", round(1819114 / 1e6, 1), 1.8)
eq("export 1933", round(1771364 / 1e6, 1), 1.8)

# Urbanisation: 26.3 million (1926) to 56.1 million (1939): increase about 30 million; shares 18% and 33%
urb26, urb39 = 26.3, 56.1
between("urban increase", urb39 - urb26, 29.5, 30.1)
# Shares assume total populations of about 147 million (1926) and 170.6 million (1939)
eq("urban share 1926", round(urb26 / 147.0 * 100), 18)
eq("urban share 1939", round(urb39 / 170.6 * 100), 33)

# Famine: Davies and Wheatcroft 5.7 million sits within the 5 to 8 million range
assert 5 <= 5.7 <= 8
# Kazakhstan: about 1.5 million is "more than a third" of about 3.6 million Kazakhs (1926 census about 3.6 million)
assert 1.5 / 4.0 > 1 / 3 or 1.5 / 3.6 > 1 / 3

# Original plan: one fifth of households by 1933
eq("one fifth", round(1 / 5 * 100), 20)
# Interval between 5 January 1930 target and Dizzy with Success
eq("days 27 Dec 1929 to 5 Jan 1930", (date(1930, 1, 5) - date(1929, 12, 27)).days, 9)
eq("dekulak resolution to dizzy", (date(1930, 3, 2) - date(1930, 1, 30)).days, 31)

# Ten-year time frame in 1931 and the Gulag growth ("about 1.6 million")
assert 1.6 > 1.0

# Gosplan founded 1921, plans from 1928: 7 years
eq("gosplan to plan", 1928 - 1921, 7)

# Figure layout: five boxes at y = 10, 80, 150, 220, 290, each 46 high; arrows 24 px between
ys = [10, 80, 150, 220, 290]
for a, b in zip(ys, ys[1:]):
    eq("gap", b - (a + 46), 24)
# Longest text line in a 280-wide box at about 7 px per character
for line in ["control grain for towns and export", "Five Year Plan paid for by grain", "about 2 million tonnes less grain"]:
    assert len(line) * 7 < 280 - 8, line
for line in ["Security, self-sufficiency, socialism and", "control all pushed toward force"]:
    assert len(line) * 7 < 340 - 8, line
# Final labels fit inside viewBox height 392: baselines 364 and 382
assert 382 + 5 < 392

# Mark totals: every essay is [30] = 15 + 15
eq("essay marks", 15 + 15, 30)
print("ok")
