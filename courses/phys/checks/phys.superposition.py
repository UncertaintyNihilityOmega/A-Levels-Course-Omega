# checks/phys.superposition.py: recomputes every number in the Superposition chapter.
from math import isclose, sqrt, pi, sin, cos, tan, asin, atan, degrees, radians, floor, ceil

c = 3.00e8   # m s^-1, data sheet

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def nmax(d, lam):
    """Highest order with n*lam < d (sin theta < 1)."""
    n = floor(d / lam)
    return n - 1 if isclose(n * lam, d) else n

# Warm-up
eq("warm lambda", sf(340 / 440), 0.773)
eq("warm phase frac", 0.20 / 0.80, 0.25)
eq("warm phase deg", 0.20 / 0.80 * 360, 90)
eq("warm intensity", 3 ** 2, 9)
eq("warm theta", sf(degrees(atan(0.020 / 2.0))), 0.573)

# Principle of superposition
eq("pulses", 3.0 - 5.0, -2.0)
eq("plot in phase", 1.0 + 0.6, 1.6)
eq("plot antiphase", 1.0 - 0.6, 0.4)

# String, 1.20 m, third harmonic 150 Hz
L = 1.20
lam = 2 * L / 3
eq("string lambda", lam, 0.80)
eq("string v", 150 * lam, 120)
eq("string f1", 150 / 3, 50)
eq("string f1 check", 120 / (2 * L), 50)
eq("string f4", 4 * 50, 200)

# Microwaves
lam = 5.6e-2 / 4 * 2
eq("microwave lambda", lam, 2.8e-2)
eq("microwave f", sf(c / lam), 1.07e10, 1e6)
eq("spot student f", sf(c / 0.014), 2.14e10, 1e7)
eq("spot student ratio", (c / 0.014) / (c / 0.028), 2)

# Pipes
v = 340
lam = 4 * 0.30
eq("closed pipe lambda", lam, 1.20)
eq("closed f1", round(v / lam), 283)
eq("closed f3", round(3 * v / lam, -1), 850)
eq("closed f3 exact", 3 * v / lam, 850)
lam = 2 * 0.30
eq("open lambda", lam, 0.60)
eq("open f1", round(v / lam), 567)
eq("open/closed factor", (v / 0.60) / (v / 1.20), 2)

# Resonance tube
half = 0.493 - 0.163
eq("tube half lambda", half, 0.330, 1e-9)
eq("tube lambda", 2 * half, 0.660, 1e-9)
eq("tube v", round(512 * 0.660), 338)
eq("tube lambda/4", 0.660 / 4, 0.165)

# Radio diffraction
eq("long wave", c / 2.00e5, 1500)
eq("FM", c / 1.00e8, 3.00)

# Loudspeakers
lam = 340 / 850
eq("speaker lambda", lam, 0.40)
eq("speaker pd1", 3.6 - 3.0, 0.60, 1e-9)
eq("speaker pd1 in lambda", 0.60 / lam, 1.5)
eq("speaker pd2", 3.4 - 3.0, 0.40, 1e-9)
eq("speaker pd2 in lambda", 0.40 / lam, 1.0)

# Double slit
eq("ds x", 24 / 10, 2.4)
eq("ds lambda", 0.50e-3 * 2.4e-3 / 2.0, 6.0e-7, 1e-12)
eq("plot x", 600e-9 * 2.0 / 0.50e-3 * 1e3, 2.4, 1e-9)       # mm
eq("laser x", sf(633e-9 * 1.5 / 0.25e-3 * 1e3, 2), 3.8)
eq("halve a", (1 / 0.5), 2)

# Grating, 300 lines/mm, 589 nm
d = 1 / 3.00e5
eq("d 300", sf(d * 1e6), 3.33)
s1 = 589e-9 / d
eq("sin1", sf(s1, 4), 0.1767, 1e-9)
eq("theta1", round(degrees(asin(s1)), 1), 10.2)
eq("sin2", sf(2 * s1, 4), 0.3534, 1e-9)
eq("theta2", round(degrees(asin(2 * s1)), 1), 20.7)
eq("d/lambda", round(d / 589e-9, 2), 5.66)
eq("nmax 589", nmax(d, 589e-9), 5)
eq("total maxima", 2 * 5 + 1, 11)

# Laser + 600 lines/mm
y = 1.24 / 2
th = atan(y / 1.50)
eq("laser y", y, 0.62)
eq("laser theta", round(degrees(th), 1), 22.5)
d6 = 1 / 6.00e5
eq("d 600", sf(d6 * 1e6), 1.67)
eq("laser lambda m", sf(d6 * sin(th)), 6.37e-7, 1e-10)
eq("laser lambda nm", round(d6 * sin(th) * 1e9), 637)

# White light overlap, 300 lines/mm
eq("overlap 1200/d", round(1200e-9 / d, 3), 0.360)
eq("overlap 1400/d", round(1400e-9 / d, 3), 0.420)
eq("overlap violet 3", round(degrees(asin(1200e-9 / d)), 1), 21.1)
eq("overlap red 2", round(degrees(asin(1400e-9 / d)), 1), 24.8)
assert 700 < 800 and 1200 < 1400
eq("d um", sf(d * 1e6), 3.33)
eq("d in nm", round(d * 1e9), 3333)

# Try: start easy
eq("t1 in phase", 3.0 + 2.0, 5.0)
eq("t1 antiphase", 3.0 - 2.0, 1.0)
eq("t2 lambda", 2 * 0.35, 0.70)
eq("t2 f", 140 / 0.70, 200)
eq("t3 first", 2 * 0.60, 1.2)
eq("t4 f", 340 / (4 * 0.25), 340)
eq("t5 a", 0.90 / 0.30, 3)
eq("t5 b", 0.75 / 0.30, 2.5)
eq("t6 x", sf(550e-9 * 1.5 / 0.40e-3 * 1e3, 2), 2.1)
eq("t7 d", 1 / 2.00e5 * 1e6, 5.0)
d4 = 1 / 4.00e5
eq("t8 d", d4 * 1e6, 2.50)
eq("t8 sin", 500e-9 / d4, 0.20)
eq("t8 theta", round(degrees(asin(0.20)), 1), 11.5)

# Exam practice
lam = 4 * 0.34
eq("e3 lambda", lam, 1.36)
eq("e3 f1", 340 / lam, 250)
eq("e3 f3", 3 * 340 / lam, 750)
eq("e4 x factor", 2 * 2, 4)
eq("e5 lambda", 340 / 850, 0.40)
eq("e5 pd", 3.6 - 3.0, 0.60, 1e-9)
d5 = 1 / 5.00e5
eq("e6 d", d5 * 1e6, 2.00)
eq("e6 d/lambda", round(d5 / 650e-9, 2), 3.08)
eq("e6 nmax", nmax(d5, 650e-9), 3)
eq("e6 sin", round(3 * 650e-9 / d5, 3), 0.975)
eq("e6 theta", round(degrees(asin(3 * 650e-9 / d5)), 1), 77.2)
y = 0.730 / 2
th = atan(y / 2.00)
eq("e7 y", y, 0.365)
eq("e7 theta", round(degrees(th), 1), 10.3)
eq("e7 lambda", sf(d * sin(th)), 5.98e-7, 1e-10)
eq("e7 nm", round(d * sin(th) * 1e9), 598)
# two wavelengths
eq("e8 ratio", 640 / 480, 4 / 3)
eq("e8 sin", round(4 * 480e-9 / d4, 3), 0.768)
eq("e8 theta", round(degrees(asin(4 * 480e-9 / d4)), 1), 50.2)
eq("e8 same", 4 * 480, 3 * 640)
eq("e8 d/l1", round(d4 / 480e-9, 1), 5.2)
eq("e8 d/l2", round(d4 / 640e-9, 1), 3.9)

# Stretch: loudspeakers 1.5 m apart, 4.0 m away, 1700 Hz
lam = 340 / 1700
eq("s1 lambda", lam, 0.200)
def pd(yy):
    return sqrt(4.0 ** 2 + (yy + 0.75) ** 2) - sqrt(4.0 ** 2 + (yy - 0.75) ** 2)
lo, hi = 0.0, 1.0
for _ in range(80):
    mid = (lo + hi) / 2
    if pd(mid) < lam / 2:
        lo = mid
    else:
        hi = mid
yx = lo
eq("s1 exact y", round(yx, 3), 0.272)
eq("s1 pd at 0.272", round(pd(0.272), 3), 0.100)
eq("s1 dist far", round(sqrt(16 + (0.272 + 0.75) ** 2), 4), 4.1285, 1e-9)
eq("s1 dist near", round(sqrt(16 + (0.272 - 0.75) ** 2), 4), 4.0285, 1e-9)
eq("s1 1.022", 0.272 + 0.75, 1.022, 1e-9)
eq("s1 0.478", 0.272 - 0.75, -0.478, 1e-9)
xs = lam * 4.0 / 1.5
eq("s1 formula x", round(xs, 3), 0.533)
eq("s1 half x", round(xs / 2, 3), 0.267)
eq("s1 percent", round((yx - xs / 2) / yx * 100), 2)

# Stretch: white light, 300 lines/mm (same numbers as the worked example)
eq("s2 begin", round(degrees(asin(1200e-9 / d)), 1), 21.1)
eq("s2 end", round(degrees(asin(1400e-9 / d)), 1), 24.8)

# Quiz
eq("q gap", 0.020 / 0.020, 1)
eq("q d/lambda", round(2000 / 630, 2), 3.17)
eq("q maxima", 2 * 3 + 1, 7)

print("ok")
