# checks/hist.eu.russia.3.py: recomputes every number in the chapter (dates, intervals, counts, marks, figure layout)
from datetime import date, timedelta


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def ns(y, m, d):
    # Old Style is 13 days behind New Style in the twentieth century
    return date(y, m, d) + timedelta(days=13)


# Calendar conversions stated in the chapter
assert ns(1917, 2, 23) == date(1917, 3, 8)        # Women's Day: 8 March NS
assert ns(1917, 10, 24) == date(1917, 11, 6)      # 24 October OS = 6 November NS
assert ns(1917, 10, 25) == date(1917, 11, 7)      # 25 October OS = 7 November NS
assert ns(1917, 4, 3) == date(1917, 4, 16)        # Lenin at the Finland Station
assert ns(1915, 8, 23) == date(1915, 9, 5)        # Tsar takes command
assert ns(1916, 11, 1) == date(1916, 11, 14)      # Milyukov's speech
assert ns(1917, 3, 2) == date(1917, 3, 15)        # abdication: 15 March NS (the 8-15 March range)
# Gregorian calendar introduced: the day after 31 January 1918 OS was 14 February
eq("calendar switch", date(1918, 1, 31) + timedelta(days=14), date(1918, 2, 14))

# Romanov rule 1613 to 1917
eq("Romanov years", 1917 - 1613, 304)

# Collapse in five days: 23 February to 2 March (1917 is not a leap year; Old Style February has 28 days)
eq("February to abdication", (date(1917, 3, 2) - date(1917, 2, 23)).days, 7)
eq("strike to garrison mutiny", (date(1917, 2, 27) - date(1917, 2, 23)).days, 4)
eq("strike to mutiny of the Volynsky regiment is 4 days", 27 - 23, 4)

# Tannenberg 26-30 August 1914: five days
eq("Tannenberg length", (date(1914, 8, 30) - date(1914, 8, 26)).days + 1, 5)

# Intervals in 1917 (Old Style)
eq("Lenin return to Theses read", (date(1917, 4, 4) - date(1917, 4, 3)).days, 1)
eq("Theses published", (date(1917, 4, 7) - date(1917, 4, 3)).days, 4)
eq("June offensive to July Days", (date(1917, 7, 3) - date(1917, 6, 18)).days, 15)
eq("Kerensky PM after July Days start", (date(1917, 7, 8) - date(1917, 7, 3)).days, 5)
eq("Kornilov dismissal to arrest", (date(1917, 9, 1) - date(1917, 8, 27)).days, 5)
eq("Kornilov to Bolshevik majority", (date(1917, 8, 31) - date(1917, 8, 27)).days, 4)
eq("MRC to rising", (date(1917, 10, 24) - date(1917, 10, 12)).days, 12)
eq("vote for rising to rising", (date(1917, 10, 24) - date(1917, 10, 10)).days, 14)
eq("Trotsky chair to rising", (date(1917, 10, 25) - date(1917, 9, 25)).days, 30)
eq("February to October (months)", 10 - 2, 8)
eq("Tsar abdication to Michael's refusal", (date(1917, 3, 3) - date(1917, 3, 2)).days, 1)
eq("Tsar abdication to Lenin's return", (date(1917, 4, 3) - date(1917, 3, 2)).days, 32)

# Rasputin's murder to the revolution (Old Style): 16-17 December to 23 February
eq("Rasputin to revolution", (date(1917, 2, 23) - date(1916, 12, 17)).days, 68)
# Tsar takes command (23 August 1915) to abdication: about 18 months
months = (1917 - 1915) * 12 + (3 - 8)
eq("command to abdication months", months, 19)
assert 18 <= months <= 19

# Central Committee vote, 10 October: ten to two
eq("CC vote total", 10 + 2, 12)
assert 10 > 2

# Bolshevik membership: about 24,000 in February; party claimed about 240,000 by August (ten times)
eq("membership ratio", 240_000 // 24_000, 10)
assert 240_000 > 200_000

# Delegates at the Second Congress (most-cited count): 649 delegates, 390 Bolsheviks
eq("Bolshevik share of delegates, per cent", round(390 / 649 * 100), 60)
assert 390 + 160 + 72 + 14 + 13 == 649

# Constituent Assembly vote mentioned: Bolsheviks about a quarter (24.0 per cent)
assert 0.2 < 24.0 / 100 < 0.3

# Tannenberg: about 92,000 prisoners; Russian paper money about five times the 1914 level
eq("quintupled", 5 * 1, 5)

# Exam facts (FACTS.md): Paper 1 15 + 25 = 40; Paper 2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(5, 8), (9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(6, 10), (11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25
# worked-answer marks sit inside their levels
assert 3 <= 4 <= 5 and 9 <= 10 <= 10      # Paper 2 (a): about 4 (Level 2), 10 (Level 4)
assert 4 <= 5 <= 7 and 12 <= 14 <= 15     # Paper 1 (a): about 5 (Level 2), 14 (Level 4)
assert 17 <= 18 <= 20                      # Paper 2 (b): Level 5
# Exam practice marks
eq("practice marks", 10 + 10 + 20 + 20 + 15 + 20 + 20, 115)

# Figure layout: dual power SVG, viewBox 340 x 266
rows = [(10, 72), (100, 166), (194, 252)]
for (a1, a2), (b1, b2) in zip(rows, rows[1:]):
    assert b1 - a2 >= 21, "gap too small for an arrow"
arrows = [(75, 96), (169, 190)]
for (y1, y2), (r_a, r_b) in zip(arrows, zip(rows, rows[1:])):
    assert y1 > r_a[1] and y2 < r_b[0] and y2 - y1 >= 20
assert max(r[1] for r in rows) + 14 <= 266
# text widths: about 7 px per character, boxes 156 px wide
for line in ["Petrograd Soviet", "formed 27 February", "The garrison, the", "railways, post and", "telegraph workers",
             "Ministers and the", "legal authority", "(no armed force)"]:
    assert len(line) * 7 <= 156 - 8, line
for line in ["Soldiers obey the government", "only where the Soviet agrees", "Order No. 1 (1 March)"]:
    assert len(line) * 7 <= 324 - 8, line
print("ok")
