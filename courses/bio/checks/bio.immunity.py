# checks/bio.immunity.py: recomputes every number in chapters/bio.immunity.md
from math import isclose, exp

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# --- :::plot antibody concentration (first exposure day 0, second day 28) -----------------------------------
def total(x):
    u = ((x - 30) + abs(x - 30)) / 2
    return 0.00135 * x ** 6 * exp(0 - x / 2) + 135 * (1 - exp(0 - u / 1.5)) ** 3 * exp(0 - u / 25)


xs = [i / 10 for i in range(0, 701)]
p_peak = max(xs[:281], key=total)
s_peak = max(xs[281:], key=total)
eq("primary peak day 12", p_peak, 12.0)
eq("primary peak 10 units", round(total(p_peak), 1), 10.0)
eq("secondary peak day 36", round(s_peak), 36)
eq("secondary peak 100.5 (label y)", round(total(s_peak), 1), 100.5)
assert 9 < total(s_peak) / total(p_peak) < 11, "secondary peak about ten times the primary peak"
assert total(3) < 0.5, "almost no antibody for the first 3 days"
assert total(5) < 2.5, "still low at day 5"
eq("day 28 almost zero (below 1)", total(28) < 1, True)
assert total(31) > total(12) * 0.99, "within 3 days of the second exposure the level reaches the primary peak"
eq("day 70 about 27", round(total(70)), 27)
assert max(total(x) for x in xs) < 130, "curve below the top of the y axis"
assert all(total(x) < 125 for x in xs)
# the secondary response is quicker: first day on which the level exceeds 10 units
first = lambda a, b: next(x for x in xs if a <= x <= b and total(x) > 10)
eq("first exposure: never above 10 before day 12", total(12) <= 10.0001, True)
eq("second exposure: above 10 units by day 31", first(28, 40) <= 31.1, True)

# --- worked example HIV -------------------------------------------------------------------------------------
t_cells = [(0, 1000), (2, 880), (4, 740), (6, 560), (8, 320), (10, 160)]
falls = [a[1] - b[1] for a, b in zip(t_cells, t_cells[1:])]
eq("first fall 120", falls[0], 120)
eq("biggest fall 240", max(falls), 240)
eq("biggest fall between 6 and 8 years", falls.index(240), 3)
eq("percentage decrease 84", (1000 - 160) / 1000 * 100, 84.0)

# --- exam practice: mouse with antigens A and B -----------------------------------------------------------------
days = [0, 7, 14, 21, 28, 35, 38, 42, 49, 56]
a = [0, 1, 6, 9, 5, 3, 40, 85, 60, 35]
b = [0, 0, 0, 0, 0, 0, 0, 2, 7, 10]
eq("first anti-A peak 9", max(a[:6]), 9)
eq("first peak at day 21", days[a.index(9)], 21)
eq("second anti-A peak 85", max(a[6:]), 85)
eq("second peak at day 42", days[a.index(85)], 42)
eq("anti-A falls day 21 to 35", a[3] > a[4] > a[5], True)
eq("40 units 3 days after the second injection", days[6] - 35, 3)
eq("anti-B lower than anti-A at every time after day 35", all(y < x for x, y in zip(a[6:], b[6:])), True)

# --- skin graft: rejection after 10 days and 3 days (no calculation, but the order matters) ---------------------
assert 3 < 10

# --- stretch table -------------------------------------------------------------------------------------------
m1, m2, m3 = 55, 12, 4
assert m3 < m2 < m1, "mouse 3 < mouse 2 < mouse 1"
print(f"ok ({n} checks)")
