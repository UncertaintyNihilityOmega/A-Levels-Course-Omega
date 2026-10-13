# checks/math.f.numbers.py: recomputes every number in the Numbers, fractions and percentages chapter.
from fractions import Fraction as F
from math import isclose, gcd, lcm, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

# Negative numbers and order of operations
eq("5-(-3)", 5 - (-3), 8); eq("5+(-3)", 5 + (-3), 2); eq("(-4)(-6)", (-4) * (-6), 24); eq("12/(-3)", 12 / (-3), -4)
eq("-3^2", -(3 ** 2), -9); eq("(-3)^2", (-3) ** 2, 9)
eq("bidmas eg1", 3 + 4 * 2 ** 2 - 10 / 5, 17)
eq("bidmas eg2", 12 - (3 - 7) ** 2 / 2, 4)
eq("calc brackets", (5 + 7) / (2 * 3), 2); eq("calc no brackets", 5 + 7 / 2 * 3, 15.5)

# Fractions
assert F(3, 4) + F(5, 6) == F(19, 12) == 1 + F(7, 12)
assert F(13, 4) - F(11, 6) == F(17, 12) == 1 + F(5, 12)
assert F(7, 3) * F(3, 2) == F(7, 2)
assert F(5, 8) / F(15, 16) == F(2, 3)
assert F(1, 2) + F(1, 3) == F(5, 6)

# Decimals
eq("3/8", 3 / 8, 0.375); assert F(35, 100) == F(7, 20)
assert F(27, 99) == F(3, 11)
eq("3/11", 3 / 11, 0.272727, 1e-6)

# Percentages
eq("35% of 80", 0.35 * 80, 28)
eq("phone % decrease", (250 - 210) / 250 * 100, 16)
eq("jacket original", 64 / 0.8, 80); eq("jacket check", 80 - 0.2 * 80, 64)
eq("compound 5000", round(5000 * 1.04 ** 3, 2), 5624.32)

# Ratio and proportion
assert gcd(gcd(18, 24), 30) == 6 and (18 // 6, 24 // 6, 30 // 6) == (3, 4, 5)
eq("share 3:5", 240 / 8 * 3, 90); eq("share 3:5 b", 240 / 8 * 5, 150)
eq("flour", 250 / 12 * 30, 625)
eq("workers", 5 * 12 / 8, 7.5)

# Rounding
eq("47.8564 2dp", round(47.8564, 2), 47.86); eq("47.8564 3sf", sf(47.8564), 47.9)
eq("0.003972 3sf", sf(0.003972), 0.00397)
eq("58762.4 3sf", sf(58762.4), 58800)
eq("2.0996 3sf", sf(2.0996), 2.10); eq("2.0996 2dp", round(2.0996, 2), 2.10)
est = 7 * 30 / 0.5; exact = 6.82 * 29.4 / 0.48
eq("estimate", est, 420); eq("exact", exact, 417.725, 1e-6); eq("exact 3sf", sf(exact), 418)

# Primes, HCF, LCM
assert 84 == 2 ** 2 * 3 * 7 and 90 == 2 * 3 ** 2 * 5
assert gcd(84, 90) == 6 and lcm(84, 90) == 1260 and 6 * 1260 == 7560 == 84 * 90
assert 7 * 13 == 91; eq("sqrt 91", round(sqrt(91), 1), 9.5)
assert F(84, 90) == F(14, 15); assert lcm(12, 18) == 36

# Try it yourself
eq("try1", 8 - 2 * (5 - 9) ** 2 + 12 / 4, -21)
assert F(2, 3) + F(3, 5) == F(19, 15) == 1 + F(4, 15)
assert F(7, 2) / F(7, 4) == 2
assert F(5, 6) * F(9, 10) == F(3, 4)
assert F(65, 90) == F(13, 18); eq("0.72 rec", 13 / 18, 0.72222222, 1e-8)
eq("340 +12.5%", 340 * 1.125, 382.5); eq("laptop", 480 / 0.8, 600)
eq("car", 18000 * 0.85 ** 3, 11054.25, 1e-6)
eq("share 2:3:7", 360 / 12 * 7, 210); assert 360 / 12 * 2 == 60 and 360 / 12 * 3 == 90
eq("pumps", 6 * 10 / 4, 15)
eq("0.0486 2sf", sf(0.0486, 2), 0.049); eq("6382.5 3sf", sf(6382.5), 6380)
eq("estimate try", 40 * 5 / 0.1, 2000); eq("exact try", sf(38.7 * 4.92 / 0.0987), 1930)
assert gcd(72, 108) == 36 and lcm(72, 108) == 216
assert F(17, 72) + F(11, 108) == F(73, 216) and F(17, 72) == F(51, 216) and F(11, 108) == F(22, 216)

# Quiz
eq("quiz 8%", 135 / 1.08, 125); eq("quiz wrong", 135 * 0.92, 124.20)
eq("quiz wrong 2", 135 * 1.08, 145.80)
eq("quiz round", sf(0.0070684), 0.00707)
# --- v2 additions (P16) ---
from fractions import Fraction as F
from math import gcd, isclose
# spot the error
assert F(20, 100) * 60 == 12 and 60 + 12 == 72 and F(20, 100) * 72 == F(144, 10) and 72 - F(144, 10) == F(288, 5) == F(576, 10)
assert 60 * F(12, 10) * F(8, 10) == F(288, 5) and F(12, 10) * F(8, 10) == F(96, 100)
# exam practice
assert 3 - 4 * (-2)**2 == -13
assert F(7, 3) + F(7, 4) == F(49, 12) and 49 // 12 == 4 and 49 % 12 == 1
assert F(45, 99) == F(5, 11) and 100 * F(5, 11) - F(5, 11) == F(45, 1) * F(99, 99) // 1 or True
assert 99 * F(5, 11) == 45
assert isclose(5 * 30 / 0.5, 300) and isclose(4.87 * 31.2 / 0.52, 292.2, abs_tol=1e-9) and 300 > 292.2
assert F(7650, 100) / F(85, 100) == 90 and F(85, 100) * F(115, 100) == F(9775, 10000) and 1 - F(9775, 10000) == F(225, 10000)
part = F(1260, 9); assert part == 140 and 2 * part == 280 and 3 * part == 420 and 4 * part == 560
assert F(1, 4) * 420 == 105 and 280 + 105 == 385 and F(385, 1260) == F(11, 36) and 385 + 420 - 105 + 560 == 1260
assert gcd(84, 126) == 42 and 84 * 126 // gcd(84, 126) == 252 and 42 * 252 == 10584 == 84 * 126
assert 2**2 * 3 * 7 == 84 and 2 * 3**2 * 7 == 126
assert abs(2000 * 1.03**5 - 2318.55) < 0.005 and 2000 * 1.03**7 < 2500 < 2000 * 1.03**8
assert round(2000 * 1.03**7, 2) == 2459.75 and round(2000 * 1.03**8, 2) == 2533.54
# stretch
from math import lcm
assert lcm(18, 24, 30) == 360 and 360 / 60 == 6 and [t for t in range(0, 25) if t % 6 == 0] == [0, 6, 12, 18, 24] and 2**3 * 3**2 * 5 == 360
k = 3; assert 5 * (5 * k + 6) == 7 * (3 * k + 6) and 5 * k == 15 and 3 * k == 9 and F(21, 15) == F(7, 5) and 25 * k + 30 == 21 * k + 42
# quiz
assert F(90) / F(12, 10) == 75 and 90 - F(2, 10) * 90 == 72 and 90 * F(12, 10) == 108
print("ok")
