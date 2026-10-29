# checks/bio.antibodies.py: recomputes every number in chapters/bio.antibodies.md
from math import isclose, exp

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- :::plot passive (injected antibodies) and active (vaccine) --------------------------------------------------
passive = lambda x: 80 * exp(0 - x / 20)


def active(x):
    u = ((x - 5) + abs(x - 5)) / 2
    return 60 * (1 - exp(0 - u / 8)) ** 3 * exp(0 - u / 90)


xs = [i / 10 for i in range(0, 1201)]
eq("passive 80 at day 0", passive(0), 80)
eq("passive about 4 at day 60", round(passive(60)), 4)
eq("active zero until day 5", active(5), 0)
a_peak = max(xs, key=active)
eq("active peak day 33", round(a_peak), 33)
eq("active peak 40 (point label)", round(active(33)), 40)
eq("active still about 17 at day 120", round(active(120)), 17)
cross = next(x for x in xs if x > 0 and active(x) > passive(x))
eq("curves cross at about day 20", round(cross), 20)
assert all(passive(x) > active(x) for x in xs if 0 <= x < 19), "passive higher before the crossing"
assert all(active(x) > passive(x) for x in xs if x > 20), "active higher after day 20"
assert max(max(passive(x), active(x)) for x in xs) < 100, "below the top of the y axis"

# --- worked example: vaccination coverage ------------------------------------------------------------------------
cov = [55, 65, 75, 85, 92, 96]
cases = [410, 300, 190, 70, 12, 2]
eq("percentage decrease 99.5", sf((410 - 2) / 410 * 100, 4), 99.51)
eq("percentage decrease to 3 s.f.", sf((410 - 2) / 410 * 100, 3), 99.5)
steps = [a - b for a, b in zip(cases, cases[1:])]
eq("cases 410 to 70 between 55% and 85%", cases[0] - cases[3], 340)
assert all(a > b for a, b in zip(cases, cases[1:])), "cases fall as coverage rises"
# slower above 85%: fall per percentage point
per_point = [(a - b) / (y - x) for a, b, x, y in zip(cases, cases[1:], cov, cov[1:])]
assert per_point[3] < per_point[2] and per_point[4] < per_point[3], "fall slows above 85%"
assert per_point[0] > 10 and per_point[1] > 10 and per_point[2] > 10, "steady steep fall below 85%"

# --- exam practice: ring vaccination -----------------------------------------------------------------------------
weekly = [8, 15, 26, 21, 6, 1, 0]
eq("peak 26 in week 3", weekly.index(max(weekly)) + 1, 3)
eq("peak value 26", max(weekly), 26)
eq("percentage decrease week 3 to week 5 is 77", round((26 - 6) / 26 * 100), 77)

# --- stretch: herd immunity ----------------------------------------------------------------------------------------
eq("80% x 85% = 68%", 0.80 * 0.85 * 100, 68.0)
assert 68 < 75, "herd immunity not reached"
eq("coverage needed 88.2%", sf(75 / 85 * 100, 3), 88.2)
assert 0.85 * (75 / 85) > 0.7499, "that coverage gives 75% immune"
print(f"ok ({n} checks)")
