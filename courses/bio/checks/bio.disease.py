# checks/bio.disease.py: recomputes every number in chapters/bio.disease.md
from math import isclose, exp

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- :::plot and worked example: malaria cases before and after a programme (invented data) --------------------
cases = lambda x: 40 + 80 / (1 + exp((x - 6) / 0.6))
eq("plot point (2, 119.9)", round(cases(2), 1), 119.9)
eq("plot point (9, 40.5)", round(cases(9), 1), 40.5)
assert abs(cases(2) - 120) < 1, "about 120 before the programme"
assert abs(cases(0) - 120) < 1 and abs(cases(4) - 120) < 4, "flat until year 5"
assert abs(cases(9) - 40) < 1 and abs(cases(8) - 40) < 3 and abs(cases(11) - 40) < 1, "about 40 from year 8"
assert cases(5) > 100 and cases(8) < 45, "fall is steep between years 5 and 8"
assert max(cases(x / 10) for x in range(0, 111)) < 160, "curve below the top of the axis (y max 160)"
eq("eg percentage fall about 120 -> about 40", sf((120 - 40) / 120 * 100, 2), 67)

# --- practice --------------------------------------------------------------------------------------------------
eq("try: 18 of 400", 18 / 400 * 100, 4.5)
eq("exam: district A decrease", sf((480 - 90) / 480 * 100, 2), 81)
eq("exam: district B decrease (for the contrast)", round((460 - 440) / 460 * 100, 1), 4.3)
eq("exam: ART group %", 3 / 120 * 100, 2.5)
eq("exam: no-drug group %", 24 / 80 * 100, 30)
eq("exam: women in the study", 120 + 80, 200)

print("ok")
