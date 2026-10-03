# checks/math.f.powers.py: recomputes every number in the Indices, surds and standard form chapter.
from fractions import Fraction as F
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

# index laws and evaluation
assert 2**5 == 32 and 2**3 * 2**4 == 2**7
eq("2^-3", 2**-3, 1/8)
eq("25^1/2", 25**0.5, 5); eq("8^2/3", 8**(2/3), 4); eq("16^-3/4", 16**(-3/4), 1/8)
eq("(4/9)^-1/2", (4/9)**-0.5, 1.5)
eq("4^1/2", 4**0.5, 2)
for x in (F(2), F(3), F(5, 2), F(-7)):
    assert (2*x**3)**2 * 3*x**-1 / (6*x**4) == 2*x
    assert 1/(2*x**-1) == x/2
eq("9^1.5", 9**1.5, 27); eq("(3^2)^1.5", (3**2)**1.5, 3**3)

# surds
eq("sqrt(9+16)", sqrt(9 + 16), 5); eq("sqrt9+sqrt16", sqrt(9) + sqrt(16), 7)
eq("sqrt72", sqrt(72), 6*sqrt(2)); eq("surd sum", sqrt(50) + sqrt(18) - sqrt(8), 6*sqrt(2))
eq("sqrt6*sqrt15", sqrt(6)*sqrt(15), 3*sqrt(10))
eq("expand1", (3 + sqrt(5))*(2 - sqrt(5)), 1 - sqrt(5))
eq("expand2", (2 + sqrt(3))**2, 7 + 4*sqrt(3))
eq("rationalise 6/sqrt3", 6/sqrt(3), 2*sqrt(3))
eq("4/(3-sqrt5)", 4/(3 - sqrt(5)), 3 + sqrt(5)); eq("4/(3-sqrt5) decimal", round(4/(3 - sqrt(5)), 3), 5.236)
eq("(sqrt3+1)/(sqrt3-1)", (sqrt(3) + 1)/(sqrt(3) - 1), 2 + sqrt(3))
assert 3 + 2*sqrt(3) + 1 > 0
eq("show numerator", (sqrt(3) + 1)**2, 4 + 2*sqrt(3))

# standard form
eq("45000", 4.5e4, 45000); eq("0.00032", 3.2e-4, 0.00032)
eq("sf a", 3e5 * 4e7, 1.2e13); eq("sf b", 6e-3 / 1.5e5, 4e-8); eq("sf c", 2.4e6 + 3e5, 2.7e6, 1e-3)

# try questions
eq("T1a", 3**-2, 1/9); eq("T1b", 81**0.75, 27); eq("T1c", (27/8)**(-2/3), 4/9)
for x, y in ((F(2), F(3)), (F(5), F(-2))):
    assert (3*x**2*y)**3 / (9*x**4*y) == 3*x**2*y**2
eq("T4a", 4**3, 64); eq("T4b", 8**(2/3), 4)
eq("T5a", sqrt(108), 6*sqrt(3)); eq("T5b", sqrt(45) + sqrt(80), 7*sqrt(5)); eq("T5c", sqrt(12)*sqrt(27), 18)
eq("T6", (4 - sqrt(3))*(1 + 2*sqrt(3)), -2 + 7*sqrt(3))
eq("T7a", 10/sqrt(5), 2*sqrt(5)); eq("T7b", 6/(4 + sqrt(7)), (8 - 2*sqrt(7))/3)
eq("T8", (sqrt(5) + 2)/(sqrt(5) - 2), 9 + 4*sqrt(5)); eq("T8 num", (sqrt(5) + 2)**2, 9 + 4*sqrt(5))
eq("T9", 3e-3 / 1.2e-7, 2.5e4, 1e-6)

# quiz
eq("Q3", sqrt(75), 5*sqrt(3)); eq("Q4", 1/(2 + sqrt(3)), 2 - sqrt(3))
print("ok")
