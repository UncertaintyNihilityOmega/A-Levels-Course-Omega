# checks/math.fm.mock.p3.py: recomputes every number in Mock Paper 3 (Further Mechanics).
# Standard library only: Fraction for exact work, small-step integration to confirm the closed forms.
import re
import pathlib
from fractions import Fraction as F
from math import isclose, sqrt, pi, sin, cos, tan, atan, acos, atan2, degrees, radians


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# ---- mark counting: the tokens in every answer must add up to the question's [n marks] ----
TOKEN = re.compile(r"^(?:(?:DM|M|A|B)\d(?: FT)?\s*)+$")


def count_marks(path, total, expect_qs):
    text = pathlib.Path(path).read_text(encoding="utf8")
    blocks = re.split(r"(?m)^Q: ", text)[1:]
    grand, spread = 0, []
    for i, b in enumerate(blocks, 1):
        b = b.split("\n:::")[0]
        m = re.match(r"\[(\d+) marks?\]", b)
        assert m, f"question {i}: no [n marks]"
        n = int(m.group(1))
        ans = b.split("\nA:", 1)[1]
        got = 0
        for grp in re.findall(r"\[([^\]\n]*)\]", ans):
            if TOKEN.match(grp):
                got += sum(int(d) for d in re.findall(r"(?:DM|M|A|B)(\d)", grp))
        assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
        qpart = b.split("\nA:", 1)[0]
        parts = [int(x) for x in re.findall(r"(?<!\w)\[(\d+)\](?!\()", qpart)]
        if parts:
            assert sum(parts) == n, f"question {i}: part marks {parts} do not add to {n}"
        grand += n
        spread.append(n)
    assert grand == total, f"paper total {grand}, should be {total}"
    assert len(blocks) == expect_qs, f"{len(blocks)} questions"
    return spread


spread = count_marks("chapters/math.fm.mock.p3.md", 50, 7)
assert spread == [5, 7, 6, 7, 7, 9, 9], spread
g = 10

# ---- Q1: 0.5 v dv/dx = -3/(x+1)^2, v(0)=4  ->  v^2 = 4 + 12/(x+1) ----
# integrate numerically with a small step in x (v dv = -6/(x+1)^2 dx, i.e. d(v^2/2) = -6/(x+1)^2 dx)
h = 1e-4
half_v2 = 8.0
x = 0.0
for _ in range(int(20 / h)):
    half_v2 += -6 / ((x + h / 2 + 1) ** 2) * h
    x += h
eq("q1 numeric at x=20", 2 * half_v2, 4 + 12 / 21, 1e-6)
eq("q1 v(0)^2", 4 + 12 / 1, 16)
for xx in (0, 1, 3, 11):
    # derivative check of the closed form: 0.5 * d(v^2/2)/dx = -3/(x+1)^2
    d = ((4 + 12 / (xx + 1e-6 + 1)) - (4 + 12 / (xx - 1e-6 + 1))) / 2e-6 / 2
    eq("q1 force", 0.5 * d, -3 / (xx + 1) ** 2, 1e-5)
assert all(4 + 12 / (xx + 1) > 4 for xx in range(0, 1000))

# ---- Q2: trajectory, two angles, speed at P ----
u, X, Y = 25, 30, 20
for t in (F(4, 3), F(17, 6)):
    assert 18 * t * t - 75 * t + 68 == 0, t
    assert (3 * t - 4) * (6 * t - 17) == 18 * t * t - 75 * t + 68
    # the trajectory really passes through (30, 20)
    eq("q2 traj", float(X * t - g * X * X * (1 + t * t) / (2 * u * u)), Y, 1e-9)
eq("q2 const", 10 * 900 / (2 * 625), 7.2)
th1, th2 = degrees(atan(4 / 3)), degrees(atan(17 / 6))
eq("q2 th1", round(th1, 1), 53.1, 1e-9); eq("q2 th2", round(th2, 1), 70.6, 1e-9)
for th in (atan(4 / 3), atan(17 / 6)):
    ux, uy = u * cos(th), u * sin(th)
    t = X / ux
    eq("q2 y at t", uy * t - 5 * t * t, Y, 1e-9)
    vx, vy = ux, uy - g * t
    eq("q2 speed", sqrt(vx * vx + vy * vy), 15, 1e-9)
# for 53.1 the point P is the highest point; for 70.6 the vertical component is -12.5
eq("q2 vy lower", 25 * sin(atan(4 / 3)) - 10 * (30 / (25 * cos(atan(4 / 3)))), 0, 1e-9)
eq("q2 vy upper", round(25 * sin(atan(17 / 6)) - 10 * (30 / (25 * cos(atan(17 / 6)))), 1), -12.5, 1e-9)
eq("q2 vx upper", round(25 * cos(atan(17 / 6)), 2), 8.32, 1e-9)

# ---- Q3: cone on cylinder, toppling ----
a = F(1)
Vcyl = 18 * a ** 3; Vcone = F(1, 3) * 9 * 4 * a ** 3 * 3  # in units of pi: (1/3)(9)(4) = 12 ... computed below
Vcyl = 9 * 2   # pi (3a)^2 (2a) / (pi a^3)
Vcone = F(1, 3) * 9 * 4
assert Vcyl == 18 and Vcone == 12
xbar = (Vcyl * 1 + Vcone * (2 + F(4, 4) * 1)) / (Vcyl + Vcone)
assert 2 + F(4, 4) == 3 and xbar == F(9, 5)
# numeric confirmation by slicing the solid into discs
n = 200000
dz = 6.0 / n
mom = vol = 0.0
for i in range(n):
    z = (i + 0.5) * dz
    r = 3.0 if z < 2 else 3.0 * (6 - z) / 4
    dvol = pi * r * r * dz
    vol += dvol; mom += dvol * z
eq("q3 xbar numeric", mom / vol, 1.8, 1e-6)
tan_a = F(3) / xbar
assert tan_a == F(5, 3)
eq("q3 alpha", round(degrees(atan(5 / 3)), 1), 59.0, 1e-9)

# ---- Q4: elastic conical pendulum ----
lam, l0, L, m = 15, 0.5, 0.75, 0.5
T = lam * (L - l0) / l0
eq("q4a T", T, 7.5)
c = m * g / T
eq("q4b cos", c, 2 / 3)
s = sqrt(1 - c * c)
omega2 = T / (m * L)       # T sin(theta) = m (L sin(theta)) omega^2
eq("q4c omega^2", omega2, 20)
eq("q4c omega", round(sqrt(omega2), 2), 4.47, 1e-9)
r = L * s
eq("q4c horizontal", T * s, m * r * omega2, 1e-9)
eq("q4d v", r * sqrt(omega2), 2.5, 1e-9)
eq("q4d r", round(r, 3), 0.559, 1e-9)

# ---- Q5: oblique impact of A (m) and B (2m), e = 1/2 ----
ca = F(4, 5)
along, perp = 10 * ca, 10 * F(3, 5)
assert along == 8 and perp == 6
# solve m*8 = m*vA + 2m*vB, vB - vA = e*8
vB = (8 + F(1, 2) * 8) / 3
vA = vB - F(1, 2) * 8
assert vB == 4 and vA == 0
assert 1 * 8 == 1 * vA + 2 * vB and vB - vA == F(1, 2) * 8
eq("q5 A speed after", sqrt(float(vA) ** 2 + 6 ** 2), 6)
# wall: B moves at 30 degrees to the wall
nb = 4 * sin(radians(30)); tb = 4 * cos(radians(30))
eq("q5b normal", nb, 2); eq("q5b tangent", tb, 2 * sqrt(3))
sp = sqrt(tb ** 2 + (0.5 * nb) ** 2)
eq("q5b speed", sp, sqrt(13)); eq("q5b speed 3sf", round(sp, 2), 3.61, 1e-9)

# ---- Q6: particle on the outside of a sphere ----
a6, m6, u6 = 0.9, 0.2, 1.5
def R(th):
    v2 = u6 ** 2 + 2 * g * a6 * (1 - cos(th))
    return m6 * g * cos(th) - m6 * v2 / a6
for th in (0.0, 0.3, 0.6, 0.7):
    eq("q6a R", R(th), 6 * cos(th) - 4.5, 1e-9)
    eq("q6a v2", u6 ** 2 + 2 * g * a6 * (1 - cos(th)), 20.25 - 18 * cos(th), 1e-9)
assert isclose(m6 * 0.9, 0.18) and 0.2 * 20.25 / 0.9 == 4.5 and 0.2 * 18 / 0.9 == 4.0
thl = acos(4.5 / 6)
eq("q6b theta", round(degrees(thl), 1), 41.4, 1e-9)
v2l = 20.25 - 18 * 0.75
eq("q6c v2", v2l, 6.75); eq("q6c v2 = g a cos", g * a6 * 0.75, 6.75)
eq("q6c v", round(sqrt(v2l), 2), 2.60, 1e-9)
# free flight from the leaving point: energy conserved down to the ground, 2a below the top
v_ground2 = u6 ** 2 + 2 * g * (2 * a6)
eq("q6d v2", v_ground2, 38.25); eq("q6d v", round(sqrt(v_ground2), 2), 6.18, 1e-9)
# the same by projecting from the leaving point
hx = a6 * sin(thl); hy = a6 + a6 * cos(thl)   # height above ground of leaving point
vl = sqrt(v2l); vx = vl * cos(thl); vy = -vl * sin(thl)   # tangent direction pointing down and outwards
eq("q6d via free flight", sqrt(vx ** 2 + (vy ** 2 + 2 * g * hy)), sqrt(v_ground2), 1e-9)

# ---- Q7: elastic string, hanging particle ----
m7, lam7, l7 = 0.5, 20, 0.8
eq("q7a e", m7 * g * l7 / lam7, 0.2)
x0 = 0.6
epe = lam7 * x0 ** 2 / (2 * l7)
eq("q7b EPE", epe, 4.5)
ke = epe - m7 * g * x0
eq("q7b KE", ke, 1.5)
v2 = 2 * ke / m7
eq("q7b v2", v2, 6); eq("q7b v", round(sqrt(v2), 2), 2.45, 1e-9)
hup = v2 / (2 * g)
eq("q7c h", hup, 0.3); eq("q7c total", x0 + hup, 0.9)
# the same by simulating the whole motion from B (down positive from the natural-length point)
y, vv, dt = x0, 0.0, 1e-6          # y = extension (positive down); velocity down positive
top = y
while True:
    acc = g - (lam7 * y / l7 / m7 if y > 0 else 0.0)
    vv += acc * dt; y += vv * dt
    top = min(top, y)
    if vv > 0 and y > x0 + 1e-4: break
    if y < -1: break
    if vv > 0 and y > 0 and top < 0: break
eq("q7c simulated top above natural length", -top, 0.3, 2e-3)
print("ok")
