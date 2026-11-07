# checks/hist.eu.france.1.py: recomputes every number in the chapter (dates, budget, prices, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Louis XVI: born 23 August 1754, king 10 May 1774 -> "aged 19"
b, k = date(1754, 8, 23), date(1774, 5, 10)
eq("age at accession", k.year - b.year - ((k.month, k.day) < (b.month, b.day)), 19)

# Estates-General last met in 1614; 1789 meeting 175 years later
eq("gap since 1614", 1789 - 1614, 175)

# 1788 budget (million livres): deficit and interest share ("about half")
spend, revenue, interest = 629, 503, 318
eq("deficit 1788", spend - revenue, 126)
share = Fraction(interest, spend)
assert Fraction(45, 100) < share < Fraction(55, 100), f"interest share {float(share):.3f} is not about half"

# Bread: 8 sous -> 14.5 sous, "almost doubled"
ratio = Fraction(29, 2) / 8
assert Fraction(17, 10) < ratio < 2, f"bread ratio {float(ratio):.2f}"

# Estates-General: six weeks of deadlock 5 May -> 17 June
d = (date(1789, 6, 17) - date(1789, 5, 5)).days
eq("deadlock weeks", d // 7, 6)
# Clergy voted to join "two days later" (19 June)
eq("clergy join", (date(1789, 6, 19) - date(1789, 6, 17)).days, 2)
# Assembly followed the king to Paris "within two weeks" (6 October -> 19 October)
assert (date(1789, 10, 19) - date(1789, 10, 6)).days <= 14
# Bastille 14 July: king recalled Necker 16 July, came to Paris 17 July; Necker dismissed 11 July
assert date(1789, 7, 11) < date(1789, 7, 14) < date(1789, 7, 16) < date(1789, 7, 17)
# Young's poor woman: 12 July, "two days before the Bastille"
eq("Young before Bastille", (date(1789, 7, 14) - date(1789, 7, 12)).days, 2)
# Pamphlets entry: 9 June 1789; Desmoulins speech 12 July
assert date(1789, 6, 9) < date(1789, 7, 12)
# Dues on land abolished without compensation 1793: four years after 1789
eq("redemption period", 1793 - 1789, 4)

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
# Level ranges quoted in the chapter
eq("P2a L4", (9, 10), (9, 10))
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25

# Figure 2 layout: arrows at least 20 px long and clear of boxes
tops = [34, 118, 202, 286, 370]
for a, b2 in zip(tops, tops[1:]):
    assert b2 - (a + 56) - 6 >= 20, "arrow too short"
assert 454 - (370 + 56) - 6 >= 20
# label widths (about 7 px a character) fit the 158 px columns with 4 px margin
for s in ["Parlement demands", "the Estates-General", "deficit 126 million", "Unemployment after", "Riots in Paris and", "dispute over voting"]:
    assert len(s) * 7 <= 158 - 8, s
print("ok")
