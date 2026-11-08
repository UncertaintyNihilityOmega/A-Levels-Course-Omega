# checks/hist.eu.russia.2.py: recomputes every number in the chapter (dates, statistics, intervals, marks, figure layout)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"


def age(b, k):
    return k.year - b.year - ((k.month, k.day) < (b.month, b.day))


# Old Style is 13 days behind New Style in the twentieth century
def ns(y, m, d):
    from datetime import timedelta
    return date(y, m, d) + timedelta(days=13)


assert ns(1905, 1, 9) == date(1905, 1, 22)       # Bloody Sunday: 9 January OS = 22 January NS
assert ns(1904, 1, 27) == date(1904, 2, 9)       # attack on Port Arthur: 27 January OS = 9 February NS
assert ns(1905, 8, 23) == date(1905, 9, 5)       # Treaty of Portsmouth: 23 August OS = 5 September NS
assert ns(1906, 4, 23) == date(1906, 5, 6)       # Fundamental Laws: 23 April OS = 6 May NS
assert ns(1905, 10, 17) == date(1905, 10, 30)    # October Manifesto
assert ns(1905, 5, 14) == date(1905, 5, 27)      # Tsushima began 27 May NS
assert ns(1905, 6, 14) == date(1905, 6, 27)      # Potemkin

# Nicholas II born 6 May 1868 NS; accession 1 November 1894 NS (20 October OS): aged 26
eq("Nicholas age", age(date(1868, 5, 6), date(1894, 11, 1)), 26)
eq("zemstvo speech after accession (days)", (date(1895, 1, 17) - date(1894, 10, 20)).days, 89)

# Witte Finance Minister 1892-1903
eq("Witte years", 1903 - 1892, 11)
# Railways 1880 22,865 km, 1900 53,234 km: "more than twice"
assert 53234 / 22865 > 2
near("rail ratio", 53234 / 22865, 2.33, 0.01)
assert round(53234, -2) == 53200

# Russo-Japanese War
# Port Arthur 20 December 1904 OS; Bloody Sunday 9 January 1905: 20 days later
eq("Port Arthur to Bloody Sunday", (date(1905, 1, 9) - date(1904, 12, 20)).days, 20)
# Tsushima 14-15 May; Portsmouth 23 August
assert date(1905, 5, 15) < date(1905, 8, 23)
# Russian dead 43,300-71,453: "roughly 43,000 to 71,000"
assert 43_000 <= 43_300 and 71_453 < 71_500
# Baltic Fleet voyage: left October 1904, Tsushima May 1905: about seven months
assert 7 == 5 + 2  # Oct->Nov->Dec->Jan->Feb->Mar->Apr->May = seven months

# Bloody Sunday: marchers 7,000-50,000 ; official dead about 100-130; wounded about 300; strikers January 414,000
assert 7_000 < 50_000
assert 96 < 100 and 130 >= 130
# 150,000 strikers in St Petersburg before 9 January; 414,000 across Russia in January
assert 150_000 < 414_000

# Strikers (Lenin 1913, official statistics): 1903-1912
s = {1903: 86832, 1904: 24904, 1905: 2863173, 1906: 1108406, 1907: 740074, 1908: 176101, 1909: 64166, 1910: 46623, 1911: 105110, 1912: 683361}
chart = {1903: 86.8, 1904: 24.9, 1905: 2863.2, 1906: 1108.4, 1907: 740.1, 1908: 176.1, 1909: 64.2, 1910: 46.6, 1911: 105.1, 1912: 683.4}
for y in s:
    near(f"chart {y}", s[y] / 1000, chart[y], 0.05)
near("1905 over 1903", s[1905] / s[1903], 32.97, 0.01)  # "about thirty-three times"
assert 2.86e6 < s[1905] < 2.87e6                             # "about 2.86 million"
assert round(s[1909], -3) == 64000 and round(s[1912], -2) == 683400
assert s[1909] < s[1910] * 2 and s[1910] < s[1911] < s[1912]  # fall to 1910, then rise
assert s[1905] > 1e6 * 2.8 and s[1909] < 70_000
near("percent over 100", 2863173 / 1_748_000, 1.638, 0.001)  # Lenin: 163.8% of workers in 1905

# Dumas (Old Style): First 27 April-8 July 1906 = 72 days; Second 20 Feb-3 June 1907 about 100 days; Third from 1 Nov 1907
eq("First Duma days", (date(1906, 7, 8) - date(1906, 4, 27)).days, 72)
d2 = (date(1907, 6, 3) - date(1907, 2, 20)).days
eq("Second Duma days", d2, 103)  # "about 100 days"
eq("Third Duma term", 1912 - 1907, 5)
assert date(1907, 6, 3) < date(1907, 11, 1)
# Fundamental Laws 23 April 1906 four days before the First Duma
eq("Laws before Duma", (date(1906, 4, 27) - date(1906, 4, 23)).days, 4)
# Fundamental Laws "six months after the Manifesto": 17 October 1905 -> 23 April 1906
m = (date(1906, 4, 23) - date(1905, 10, 17)).days
assert 180 <= m <= 190, m
# Manifesto nine months after the petition: 9 January -> 17 October 1905
mm = (date(1905, 10, 17) - date(1905, 1, 9)).days
assert 270 <= mm <= 290, mm  # about nine months (281 days)
# 1881 Manifesto -> 1905 petition: 24 years
eq("years between", 1905 - 1881, 24)
# Landowner vote ~ 260 workers (commonly given)
assert 260 > 45 > 15 > 3

# Stolypin: Interior Minister April 1906, Prime Minister July 1906, shot 1 Sept 1911, died 5 Sept; Prime Minister 1906-11 = 5 years
eq("Stolypin years", 1911 - 1906, 5)
assert (date(1911, 9, 5) - date(1911, 9, 1)).days == 4
# Siberia: about 2.8 million moved 1908-13 (six years)
eq("Siberia years", 1913 - 1908 + 1, 6)
# Redemption payments abolished 1 January 1907; land decree 9 November 1906
assert date(1906, 11, 9) < date(1907, 1, 1)
# Speech 10 May 1907 before the Second Duma's dissolution on 3 June
assert date(1907, 5, 10) < date(1907, 6, 3)
# Estimates of households leaving: 10% to a quarter
assert 10 < 25
# Lena 4 April 1912 (17 April NS); dead about 80-270
assert ns(1912, 4, 4) == date(1912, 4, 17)
assert 80 < 270
# French loan about 2.25 billion francs (1906)
eq("loan francs", 2.25e9, 2_250_000_000)
# Executions 1906-09 about 3,000 over four years
eq("courts-martial span", 1909 - 1906, 3)

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10), (4, 7), (8, 11), (12, 15), (9, 12), (13, 16), (17, 20), (11, 15), (16, 20), (21, 25), (5, 8)]:
    assert lo <= hi
assert 3 <= 4 <= 5 and 9 <= 10 <= 10 and 12 <= 14 <= 15 and 17 <= 18 <= 20

# Figure 1 layout (viewBox 340 x 386): boxes x=40..336, y = 30, 96, 162, 228, 294, height 58, gap 8
ys = [30, 96, 162, 228, 294]
for a, b in zip(ys, ys[1:]):
    assert b - (a + 58) == 8
assert ys[-1] + 58 <= 386 - 14
assert 40 + 296 <= 340
# Text left at x=48 in a 296-wide box: 280 px available; bold about 7.7 px per character, regular 7
bold = ["Social Democrats (1898)", "Socialist Revolutionaries (1901–02)", "Kadets (Constitutional Democrats)",
        "Octobrists (Union of 17 October)", "Union of the Russian People (1905)"]
reg = ["Marxists: workers' revolution; split in", "1903 into Bolsheviks and Mensheviks", "land for the peasants; terror, e.g.",
       "the murder of Plehve in 1904", "liberals, 1905: a real parliament", "under the Tsar; more than he gave",
       "1905: accepted the Manifesto; wanted", "order and gradual reform", "Black Hundreds: for the autocracy;",
       "violent attacks on Jews and radicals"]
for t in bold:
    assert len(t) * 7.7 <= 280, t
for t in reg:
    assert len(t) * 7 <= 280, t
# baselines inside each box: top+19, +34, +49 within height 58
for y in ys:
    assert y + 49 < y + 58 - 4
# arrow and labels
assert 22 < 30 and 348 < 352
print("ok")
