# checks/bio.planttransport.py: recomputes every number in the Plant tissues and water transport chapter.
from math import pi, exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- Warm-up: water potentials -700 and -400 kPa: water moves to the lower (more negative) value
assert -700 < -400
# --- Plan diagram eg: M = I / A
eq("stem drawing M", 84 / 3.5, 24)
# --- Practice: root drawing
eq("root drawing M", 96 / 1.6, 60)


def vol(r, d):
    return pi * r ** 2 * d


# --- Potometer worked example (privet): 24 mm in 5.0 min, r 0.50 mm
v = vol(0.50, 24)
eq("eg potometer V (unrounded 18.85)", round(v, 2), 18.85)
eq("eg potometer V 2 s.f.", sf(v, 2), 19)
eq("eg potometer rate", sf(v / 5.0, 2), 3.8)
# --- Data example: r 0.60 mm, distances in 10 min
v = vol(0.60, 18)
eq("data eg V", round(v, 1), 20.4)
eq("data eg V (20.36)", round(v, 2), 20.36)
eq("data eg rate", sf(v / 10, 2), 2.0)
eq("moving air more than doubles 18 -> 41", 41 / 18 > 2, True)
# --- Practice: geranium, 36 mm in 8.0 min, r 0.40
v = vol(0.40, 36)
eq("practice V", round(v, 2), 18.10)
eq("practice rate", sf(v / 8.0, 2), 2.3)
# --- Exam practice: draught
eq("draught % increase", round((1.15 - 0.46) / 0.46 * 100, 6), 150)
# --- Exam practice: lilac shoot 45 mm in 6.0 min, r 0.30
v = vol(0.30, 45)
eq("lilac V", round(v, 1), 12.7)
eq("lilac rate", sf(v / 6.0, 2), 2.1)
# --- Plot: 20*exp(-((x-13)/4.5)^2)+1.5
f = lambda x: 20 * exp(0 - ((x - 13) / 4.5) ** 2) + 1.5
eq("peak at 13:00", f(13), 21.5)
eq("rate at 06:00", sf(f(6), 2), 3.3)
assert f(0) < 4 and f(3) < 4 and f(6) < 4
assert max(f(x / 10) for x in range(0, 241)) <= 21.5 + 1e-9
# --- Quiz: r 0.25 mm, 40 mm
v = vol(0.25, 40)
eq("quiz V", sf(v, 2), 7.9)
eq("quiz diameter slip", sf(vol(0.50, 40), 2), 31)
eq("quiz circumference slip", sf(2 * pi * 0.25 * 40, 2), 63)
eq("quiz half distance", sf(vol(0.25, 20), 2), 3.9)
# --- Stretch: trunk 0.20 mm; root water potentials
assert -80 > -500 and -700 < -500
print("ok", n)
