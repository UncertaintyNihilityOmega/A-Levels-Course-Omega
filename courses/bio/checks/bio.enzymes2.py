# checks/bio.enzymes2.py: recomputes every number in the Enzyme kinetics, inhibitors and immobilised enzymes chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def mm(V, K):
    return lambda s: V * s / (K + s)


def r1(x):
    return round(x + 1e-12, 1)


# --- Vmax / Km :::plot and worked example 1 (Vmax 80, Km 5) -----------------------------------------------
f1 = mm(80, 5)
eq("rate at Km is half Vmax", f1(5), 40)
eq("rate at 50 about 73", round(f1(50)), 73)
assert f1(50) < 80

# --- Worked example 2: table (Vmax 50, Km 4) ------------------------------------------------------------
f2 = mm(50, 4)
S = [1, 2, 4, 8, 16, 32, 64]
want = [10.0, 16.7, 25.0, 33.3, 40.0, 44.4, 47.1]
for s, w in zip(S, want):
    eq(f"table rate at {s}", r1(f2(s)), w)
eq("half of 50", 50 / 2, 25)
eq("Km read at 25.0 is 4", f2(4), 25.0)

# --- Compare two enzymes (Vmax 90, Km 2 and 10) ---------------------------------------------------------
X, Y = mm(90, 2), mm(90, 10)
eq("X at Km", X(2), 45)
eq("Y at its Km", Y(10), 45)
eq("Y at 2 is 15", Y(2), 15)
eq("X is three times faster at 2", X(2) / Y(2), 3)

# --- Competitive plot (Vmax 80, Km 4 -> 12) ---------------------------------------------------------------
c0, c1 = mm(80, 4), mm(80, 12)
eq("no inhibitor at 4", c0(4), 40)
eq("with inhibitor at 4", c1(4), 20)
eq("no inhibitor at 12", c0(12), 60)
eq("with inhibitor at 12", c1(12), 40)
eq("with inhibitor reaches 40 at 12", c1(12), 40)
eq("Km x3", 12 / 4, 3)

# --- Non-competitive plot (Vmax 80 -> 40, Km 4) ----------------------------------------------------------
n1 = mm(40, 4)
eq("half of 40 at Km 4", n1(4), 20)
eq("half of 80 at Km 4", c0(4), 40)

# --- Table with inhibitors X and Y ----------------------------------------------------------------------
ctl, xx, yy = mm(100, 5), mm(100, 15), mm(60, 5)
S = [5, 10, 20, 40, 80, 160]
for s, a, b, c in zip(S, [50.0, 66.7, 80.0, 88.9, 94.1, 97.0], [25.0, 40.0, 57.1, 72.7, 84.2, 91.4],
                      [30.0, 40.0, 48.0, 53.3, 56.5, 58.2]):
    eq(f"none at {s}", r1(ctl(s)), a)
    eq(f"X at {s}", r1(xx(s)), b)
    eq(f"Y at {s}", r1(yy(s)), c)
eq("X reaches 50 at 15", xx(15), 50)
assert xx(10) < 50 < xx(20)
eq("Y half-max 30 at 5", yy(5), 30)
eq("Y at 5 is exactly half its Vmax", yy(5), 60 / 2)

# --- Immobilised enzyme temperature example (no calculation, just the comparisons stated) ----------------
free = {30: 70, 40: 100, 50: 40, 60: 5, 70: 0}
imm = {30: 55, 40: 80, 50: 85, 60: 52, 70: 15}
eq("free optimum 40", max(free, key=free.get), 40)
eq("immobilised optimum 50", max(imm, key=imm.get), 50)
assert imm[40] < free[40] and imm[50] > free[50] and imm[60] > free[60]

# --- Practice ---------------------------------------------------------------------------------------------
eq("try: half of 36", 36 / 2, 18)
eq("try: 60 -> 36 is 40 %", (60 - 36) / 60 * 100, 40)
P, Q = mm(60, 2), mm(60, 8)
for s, p, q in zip([2, 4, 8, 16, 32, 64], [30.0, 40.0, 48.0, 53.3, 56.5, 58.2], [12.0, 20.0, 30.0, 40.0, 48.0, 53.3]):
    eq(f"P at {s}", r1(P(s)), p)
    eq(f"Q at {s}", r1(Q(s)), q)
eq("P half-max at 2", P(2), 30)
eq("Q half-max at 8", Q(8), 30)
a0, a1 = mm(64, 4), mm(32, 4)
for s, u, w in zip([1, 2, 4, 8, 16, 32], [12.8, 21.3, 32.0, 42.7, 51.2, 56.9], [6.4, 10.7, 16.0, 21.3, 25.6, 28.4]):
    eq(f"insecticide none at {s}", r1(a0(s)), u)
    eq(f"insecticide with Z at {s}", r1(a1(s)), w)
eq("insecticide half of 64 at 4", a0(4), 32)
eq("insecticide half of 32 at 4", a1(4), 16)
eq("beads: 100 -> 88 is 12 %", (100 - 88) / 100 * 100, 12)

# --- Stretch: drugs A (competitive, Km 3 -> 12) and B (non-competitive, Vmax 100 -> 40) ---------------------
none, A, B = mm(100, 3), mm(100, 12), mm(40, 3)
for s, a, b, c in zip([2, 10, 30, 100], [40.0, 76.9, 90.9, 97.1], [14.3, 45.5, 71.4, 89.3], [16.0, 30.8, 36.4, 38.8]):
    eq(f"drug table none at {s}", r1(none(s)), a)
    eq(f"drug table A at {s}", r1(A(s)), b)
    eq(f"drug table B at {s}", r1(B(s)), c)
eq("A % decrease at 2", round((40.0 - 14.3) / 40.0 * 100), 64)
eq("A % decrease at 100", round((97.1 - 89.3) / 97.1 * 100), 8)
eq("B % decrease at 2", round((40.0 - 16.0) / 40.0 * 100), 60)
eq("B % decrease at 100", round((97.1 - 38.8) / 97.1 * 100), 60)
eq("column 5 cm3/min", 5 * 0.96, 4.8)
eq("column 10 cm3/min", 10 * 0.90, 9.0)
eq("column 20 cm3/min", 20 * 0.71, 14.2)

print("ok")
