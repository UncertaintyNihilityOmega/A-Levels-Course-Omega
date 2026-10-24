# checks/chem.org.phenol.py: recomputes every number in the Phenol chapter.
# Ar values from the 9701 Periodic Table: H 1.0, C 12.0, O 16.0, Br 79.9.
# pKa values (ethanoic 4.76, chloroethanoic 2.86, as in chem.acids2) are standard table values quoted in the text and given as data in the question.
from math import isclose, sqrt, log10

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

H, C, O, Br = 1.0, 12.0, 16.0, 79.9
Mr_phenol = 6 * C + 6 * H + O
Mr_tbp = 6 * C + 3 * H + 3 * Br + O          # C6H2Br3OH
eq("Mr phenol", Mr_phenol, 94.0)
eq("Mr tribromophenol", round(Mr_tbp, 1), 330.7)

# warm-up: Ka from pKa 4.76
eq("Ka ethanoic", round(10 ** -4.76 * 1e5, 2), 1.74)

# worked example: 4.70 g phenol
nph = 4.70 / Mr_phenol
eq("eg moles", round(nph, 4), 0.0500)
eq("eg mass", round(nph * Mr_tbp, 1), 16.5)

# chloroethanoic vs ethanoic: ratio of Ka
ratio = 10 ** (4.76 - 2.86)          # 2.86 = -lg(1.38e-3), the chem.acids2 table value
eq("pKa chloroethanoic", round(-log10(1.38e-3), 2), 2.86)
eq("exponent", round(4.76 - 2.86, 2), 1.90)
eq("ratio", round(ratio), 79)

# try: pH of 0.100 mol dm-3 phenol, Ka 1.0e-10
h = sqrt(1.0e-10 * 0.100)
eq("[H+]", round(h * 1e6, 2), 3.16)
eq("pH", round(-log10(h), 2), 5.50)

# exam: 2.35 g phenol, 7.31 g obtained
n2 = 2.35 / Mr_phenol
eq("Q moles", round(n2, 4), 0.0250)
m2 = n2 * Mr_tbp
eq("Q max", round(m2, 2), 8.27)
eq("Q yield", round(7.31 / m2 * 100, 1), 88.4)

# exam: volume of 0.0500 mol/dm3 bromine water for 0.235 g phenol
n3 = 0.235 / Mr_phenol
eq("Q3 phenol moles", round(n3, 5), 0.00250)
nbr = 3 * n3
eq("Q3 Br2 moles", round(nbr, 5), 0.00750)
eq("Q3 volume dm3", nbr / 0.0500, 0.150)
eq("Q3 volume cm3", nbr / 0.0500 * 1000, 150)

# quiz: 0.188 g phenol
n4 = 0.188 / Mr_phenol
eq("quiz moles", round(n4, 5), 0.00200)
eq("quiz mass", round(n4 * Mr_tbp, 3), 0.661)
eq("quiz x3 option", round(n4 * Mr_tbp * 3, 2), 1.98)
eq("quiz /10 option", round(n4 * Mr_tbp / 10, 4), 0.0661 )
print("ok", n)
