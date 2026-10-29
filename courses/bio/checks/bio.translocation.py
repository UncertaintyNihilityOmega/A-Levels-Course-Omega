# checks/bio.translocation.py: recomputes every number in the Translocation in phloem chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- Ringing worked example (bean): width above ring vs control
eq("width difference", round(6.4 - 4.2, 6), 2.2)
eq("percentage increase in width", sf((6.4 - 4.2) / 4.2 * 100, 2), 52)
assert 38 > 21 > 7                        # sucrose: above ring > control > below ring
# --- Tracer speed worked example: 0.84 m in 40 min
t = 40 / 60
eq("t in hours", round(t, 3), 0.667)
eq("speed unrounded", round(0.84 / t, 2), 1.26)
eq("speed 2 s.f.", sf(0.84 / t, 2), 1.3)
# --- Practice: 45 cm in 25 min
eq("practice speed", round(0.45 / (25 / 60), 2), 1.08)
eq("practice speed 2 s.f.", sf(0.45 / (25 / 60), 2), 1.1)
# --- Exam practice: sucrose along the stem
vals = [14.2, 12.9, 11.1, 9.6]
assert all(a > b for a, b in zip(vals, vals[1:]))
eq("percentage decrease 10 to 70 cm", sf((14.2 - 9.6) / 14.2 * 100, 2), 32)
# --- Exam practice: root dry mass
eq("root mass percentage", sf(0.8 / 2.1 * 100, 2), 38)
# --- Exam practice: loading rates
assert 100 > 22 > 18
# --- Quiz: 54 cm in 30 min (REVIEW P4, P5, P7: was 63 cm, which gave the worked example's 1.26 m/h)
eq("quiz speed", 0.54 / 0.5, 1.08)
eq("quiz cm per min", 54 / 30, 1.8)
eq("quiz divides by 2", 0.54 / 2, 0.27)
eq("quiz forgets cm to m", 54 / 0.5, 108)
print("ok", n)
