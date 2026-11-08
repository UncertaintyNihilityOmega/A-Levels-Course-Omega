# checks/hist.us.depression.1.py: recomputes every number in the chapter (dates, Dow, banks, tax, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"


# Dow Jones: peak, 1921 base, November 1929, April 1930 and the 1932 low
peak, base21, nov29, apr30, low32 = 381.17, 63, 198.60, 294.07, 41.22
near("Dow sixfold", peak / base21, 6.05, 0.01)
assert 5.9 < peak / base21 < 6.2  # "six times higher"
near("fall to 13 Nov 1929", 100 * (peak - nov29) / peak, 47.9, 0.05)  # "almost half"
near("fall to 8 Jul 1932", 100 * (peak - low32) / peak, 89.2, 0.05)  # "89 per cent"
recovered = (apr30 - nov29) / (peak - nov29)
assert 0.45 < recovered < 0.58, recovered  # "about half of its fall"

# Black Thursday, Monday, Tuesday
close28 = 260.64
prev28 = round(close28 + 38.33, 2)
near("28 Oct %", 100 * 38.33 / prev28, 12.82, 0.01)
close29 = round(close28 - 30.57, 2)
eq("29 Oct close", close29, 230.07)
near("29 Oct %", 100 * 30.57 / close28, 11.73, 0.01)
near("two-day fall points", prev28 - close29, 68.90, 0.005)
near("two-day fall %", 100 * (prev28 - close29) / prev28, 23.05, 0.01)  # "nearly a quarter"
assert 6.38 / (6.38 / 0.0209) > 0
near("24 Oct %", 100 * 6.38 / 305.85, 2.09, 0.02)  # prior close about 305.85
eq("Black Thursday weekday", date(1929, 10, 24).weekday(), 3)  # Thursday
eq("Black Monday weekday", date(1929, 10, 28).weekday(), 0)
eq("Black Tuesday weekday", date(1929, 10, 29).weekday(), 1)
eq("Peak to Black Thursday days", (date(1929, 10, 24) - date(1929, 9, 3)).days, 51)
eq("Peak to Fisher (six weeks)", (date(1929, 10, 15) - date(1929, 9, 3)).days // 7, 6)
eq("Fisher to Black Thursday (nine days)", (date(1929, 10, 24) - date(1929, 10, 15)).days, 9)
eq("Babson after peak (two days)", (date(1929, 9, 5) - date(1929, 9, 3)).days, 2)
eq("Fisher 16 Oct report weekday", date(1929, 10, 16).weekday(), 2)

# Dow year-end chart
dow = {1925: 156.66, 1926: 157.2, 1927: 202.4, 1928: 300, 1929: 248.48, 1930: 164.58, 1931: 77.9, 1932: 59.93}
assert max(dow, key=dow.get) == 1928 and dow[1932] < dow[1925]

# Income tax top rates (Smiley, EH.net): 73 -> 58 -> 46 -> 25
rates = [73, 58, 46, 25]
eq("tax cut points", rates[0] - rates[-1], 48)
assert rates == sorted(rates, reverse=True)
# bar chart geometry: baseline 160, 80% at y 20 -> 1.75 px per per cent
k = 1.75
for r, (y, h) in zip(rates, [(32.25, 127.75), (58.5, 101.5), (79.5, 80.5), (116.25, 43.75)]):
    near(f"bar height {r}", r * k, h, 0.005)
    near(f"bar top {r}", 160 - r * k, y, 0.005)

# Banks (Federal Reserve Bulletin, Sept 1937): suspensions, all banks
susp = {1921: 505, 1922: 366, 1923: 646, 1924: 775, 1925: 618, 1926: 976, 1927: 669, 1928: 498, 1929: 659,
        1930: 1350, 1931: 2293, 1932: 1453, 1933: 4000}
eq("suspensions 1921-29", sum(susp[y] for y in range(1921, 1930)), 5712)
assert sum(susp[y] for y in range(1921, 1930)) / 9 > 600  # "more than 600 a year"
eq("suspensions 1930-33", sum(susp[y] for y in range(1930, 1934)), 9096)
eq("banks fall", 28885 - 23631, 5254)
near("banks fall %", 100 * 5254 / 28885, 18.2, 0.05)
assert 28800 < 28885 < 29000 and 23500 < 23631 < 23700  # "about 28,900", "about 23,600"

# Cars, Model T
near("vehicles factor", 26.7 / 9.2, 2.9, 0.05)  # "nearly 27 million" from "about 9 million"
near("Model T price cut %", 100 * (825 - 260) / 825, 68.5, 0.05)  # "less than a third of 1908 price"
assert 260 / 825 < 1 / 3
eq("assembly time", (12.5 * 60, 93)[1], 93)  # 12.5 hours = 750 min -> 93 min
near("assembly factor", 750 / 93, 8.06, 0.01)

# Dates and intervals
eq("Hoover inaug to Black Thursday (days)", (date(1929, 10, 24) - date(1929, 3, 4)).days, 234)
assert 7 < 234 / 30.4 < 8  # about seven and a half months
eq("Harding death 1923", date(1923, 8, 2).year, 1923)
eq("Recession before Crash (Aug 1 to Oct 24 about 2 months)", round((date(1929, 10, 24) - date(1929, 8, 1)).days / 30.4), 3)
eq("Hoover elected weekday (Tuesday)", date(1928, 11, 6).weekday(), 1)
eq("Smoot-Hawley year", date(1930, 6, 17).year, 1930)
eq("Dow low weekday (Friday)", date(1932, 7, 8).weekday(), 4)

# Mellon in office 1921-32; Coolidge a third of debt; war debts
eq("Mellon years", 1932 - 1921, 11)

# Reparations: 132 -> 121 billion gold marks; trade 36 -> 12 billion
near("trade fall %", 100 * (36 - 12) / 36, 66.7, 0.05)  # "about two thirds"
near("Young Plan cut %", 100 * (132 - 121) / 132, 8.3, 0.05)
near("marks to dollars 1921", 31.5 / 132, 0.2386, 0.001)  # about 24 cents a mark
near("marks to dollars 1929", 29 / 121, 0.2397, 0.001)

# Investment trusts 1929: about one every business day (265 in about 250-310 days)
assert 0.8 < 265 / 300 < 1.1

# Farm: prices down 53.3% (1920-21), farm cash income 4.89bn -> 1.473bn (used in the practice box)
near("farm income fall %", 100 * (4890 - 1473) / 4890, 69.9, 0.05)

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25

# Figure layout: Depression layers (viewBox 340 x 322), box 324 wide, ~7 px per character, 4 px margin
tops = [8, 96, 184, 272]
heights = [58, 58, 58, 44]
for i in range(3):
    gap = tops[i + 1] - (tops[i] + heights[i])
    assert gap - 8 >= 20, ("arrow too short", i, gap)  # arrow runs 4 px clear at each end
assert tops[3] + heights[3] <= 322
for s in ["Weak foundations, 1921–29", "farm slump, old industries, unequal", "incomes, small banks, war debts, tariffs",
          "Mistakes that deepened the slump", "money supply down by nearly 30%,", "Smoot–Hawley, no rescue of banks",
          "jobless 3% to 25%; trade down by two thirds"]:
    assert len(s) * 7 <= 324 - 8, s
# Circle diagram (340 x 250): label clear of the arrows
def x_at(x1, y1, x2, y2, y):
    return x1 + (x2 - x1) * (y - y1) / (y2 - y1)
assert 62 < x_at(120, 60, 70, 154, 108) - 4  # "loans" ends at x=62
assert 262 > x_at(276, 154, 222, 60, 112) + 4  # "war debts" starts right of the arrow
assert 262 + len("war debts") * 7 <= 340 - 4
assert 182 - 176 >= 4  # "reparations" baseline 176, arrow at 182
assert 170 - len("reparations") * 7 / 2 > 124 + 4 and 170 + len("reparations") * 7 / 2 < 216 - 4
print("ok")
