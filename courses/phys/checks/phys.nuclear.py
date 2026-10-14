# checks/phys.nuclear.py: recomputes every number in the Nuclear physics chapter.
from math import isclose, sqrt, exp, log

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

c = 3.00e8; u = 1.66e-27; e = 1.60e-19; NA = 6.02e23; me = 9.11e-31
MEV = 1.60e-13
YEAR = 3.15e7
LN2 = 0.693

# Warm-up
eq("warm Q", sf(exp(-2.0), 2), 0.14, 1e-9)
eq("warm MeV", 2.5e6 * e, 4.0e-13, 1e-25)

# Coal
eq("coal dm", sf(3.0e7 / c**2, 2), 3.3e-10, 1e-12)

# 1 u
Eu = u * c**2
eq("u in J", sf(Eu, 4), 1.494e-10, 1e-13)
eq("u in MeV", sf(Eu / MEV, 3), 934, 1e-9)
u_mev = 934

# 1 g and the Sun
eq("1 g", 1.0e-3 * c**2, 9.0e13, 1e6)
eq("lamp s", 9.0e13 / 100, 9e11, 1e3)
eq("lamp years", sf(9.0e13 / 100 / YEAR, 1), 3e4, 1)
eq("sun dm", sf(3.8e26 / c**2, 2), 4.2e9, 1e7)

# Equations
eq("rutherford A", 14 + 4, 17 + 1); eq("rutherford Z", 7 + 2, 8 + 1)
eq("fission x", 235 + 1 - 141 - 92, 3); eq("fission Z", 92, 56 + 36)
eq("U decay A", 238 - 234, 4); eq("U decay Z", 92 - 90, 2)
eq("Ra decay A", 226 - 222, 4); eq("Ra decay Z", 88 - 86, 2)
eq("C14 A", 14, 14); eq("C14 Z", 6, 7 - 1)

# He-4
mp, mn, mHe = 1.007276, 1.008665, 4.001506
sep = 2 * mp + 2 * mn
eq("sep", round(sep, 6), 4.031882)
dm = sep - mHe
eq("dm u", round(dm, 6), 0.030376)
eq("dm kg", sf(dm * u), 5.04e-29, 1e-32)
EB = dm * u * c**2
eq("EB J", sf(EB), 4.54e-12, 1e-15)
eq("EB MeV", sf(EB / MEV), 28.4, 1e-9)
eq("EB/A", sf(EB / MEV / 4, 2), 7.1, 1e-9)
eq("EB via 934", sf(dm * u_mev, 3), 28.4, 1e-9)
# electrons warn
eq("electron u", sf(me / u, 3), 5.49e-4, 1e-7)
eq("two electrons u", sf(2 * me / u, 2), 1.1e-3, 1e-6)
eq("two electrons MeV", sf(2 * me / u * u_mev, 2), 1.0, 0.06)

# Fission estimate
eq("fission dBE", round(8.5 - 7.6, 1), 0.9)
eq("fission total", sf(235 * 0.9, 1), 2e2, 1)

# D-T
md, mt, mn_ = 2.013553, 3.015501, 1.008665
react = md + mt; prod = mHe + mn_
eq("DT react", round(react, 6), 5.029054); eq("DT prod", round(prod, 6), 5.010171)
dmDT = react - prod
eq("DT dm", round(dmDT, 6), 0.018883)
eq("DT E J", sf(dmDT * u * c**2, 2), 2.8e-12, 1e-14)
eq("DT E MeV", sf(dmDT * u_mev, 3), 17.6, 1e-9)

# U fission per kg
Nu = 1.0 / 0.235 * NA
eq("U nuclei", sf(Nu), 2.56e24, 1e21)
eq("fission J", 200 * e * 1e6, 3.2e-11, 1e-20)
Ef = Nu * 200 * MEV
eq("U per kg", sf(Ef, 2), 8.2e13, 1e11)
eq("ratio coal", sf(Ef / 3.0e7, 2), 2.7e6, 1e4)

# Fluctuations
eq("sqrtN 400", sqrt(400), 20)
eq("sqrtN %", sqrt(400) / 400 * 100, 5.0)
eq("10000 counts", 1 / sqrt(10000) * 100, 1.0)

# Background
eq("bg rate", 75 / 5.0, 15)
eq("corrected", 180 - 15, 165)

# Iodine-131
lam = LN2 / 8.0
eq("I lam", sf(lam, 3), 0.0866, 1e-9)
eq("I 20 d", sf(exp(-lam * 20)), 0.177, 1e-9)
eq("I 5%", sf(log(1 / 0.050), 3), 3.00, 1e-9)
eq("I t", sf(log(1 / 0.050) / lam, 2), 35, 1e-9)
eq("I half-lives", sf(log(1 / 0.050) / lam / 8.0, 2), 4.3, 1e-9)
eq("I check", sf(0.5 ** 4.3, 1), 0.05, 1e-9)
# decay plot points
for t, a in ((8, 20), (16, 10), (24, 5)):
    assert abs(40 * exp(-0.0866 * t) - a) < 0.1 * a, (t, a)
    n += 1
eq("ln 40", sf(log(40), 4), 3.689, 1e-9)
eq("ln plot", sf(log(40), 3), 3.69, 1e-9)

# Am-241
Nam = 1.0e-9 / 0.241 * NA
eq("Am N", sf(Nam, 2), 2.5e15, 1e12)
lam_am = LN2 / (432 * YEAR)
eq("Am lam", sf(lam_am, 2), 5.1e-11, 1e-13)
eq("Am A", sf(lam_am * Nam, 2), 1.3e5, 1e3)

# Carbon dating
t = 5730 / LN2 * log(0.23 / 0.12)
eq("C14 ln", sf(log(0.23 / 0.12), 3), 0.651, 1e-9)
eq("C14 age", sf(t, 2), 5.4e3, 1)
eq("C14 factor", round(5730 / LN2), 8268)

# Spot the error
eq("spot wrong", sf(0.693 * 12, 2), 8.3, 1e-9)
eq("spot right", sf(0.693 / 12, 2), 0.058, 1e-9)

# Start easy
eq("se1", 2.0e-6 * c**2, 1.8e11, 1e5)
eq("se2", sf(0.0100 * u_mev, 3), 9.34, 1e-9)
eq("se4", sf(492 / 56, 2), 8.8, 1e-9)
eq("se6", 150 - 30, 120)
eq("se7", sf(LN2 / 2.0e-4, 2), 3.5e3, 1)
eq("se7 min", round(LN2 / 2.0e-4 / 60), 58)
eq("se8", 20 / 4, 5.0)
assert 640 / 2**4 == 40
eq("se9", 4.0e-6 * 3.0e12, 1.2e7, 1)

# Exam practice
dm2 = 2 * md - (3.014932 + mn_)
eq("dd dm", round(dm2, 6), 0.003509)
eq("dd dm kg", sf(0.003509 * u, 2), 5.8e-30, 1e-32)
eq("dd E", sf(sf(0.003509 * u, 2) * c**2, 2), 5.2e-13, 1e-15)
eq("fission mass", float(7.6 < 8.5), 1.0)
# Co-60
Nco = 1.0e-9 / 0.060 * NA
eq("Co N", sf(Nco, 2), 1.0e16, 1e13)
lam_co = LN2 / (5.3 * YEAR)
eq("Co lam", sf(lam_co, 2), 4.2e-9, 1e-11)
eq("Co A", sf(lam_co * Nco, 2), 4.2e7, 1e5)
# G-M data: corrected = total - 24, C = 520 exp(-0.28 t)
data = [(0, 544), (1.0, 417), (2.0, 321), (3.0, 248), (4.0, 194), (5.0, 152)]
for tt, tot in data:
    assert abs(520 * exp(-0.28 * tt) + 24 - tot) < 1.0, (tt, tot)
    n += 1
eq("gm corr0", 544 - 24, 520); eq("gm corr5", 152 - 24, 128)
lam_gm = log(520 / 128) / 5.0
eq("gm lam", sf(lam_gm, 2), 0.28, 1e-9)
eq("gm half", sf(LN2 / lam_gm, 2), 2.5, 1e-9)
eq("gm half using 0.28", sf(0.693 / 0.28, 2), 2.5, 1e-9)
# Tc-99m
lam_tc = LN2 / 6.0
eq("Tc lam", sf(lam_tc, 4), 0.1155, 1e-9)
eq("Tc A", sf(350 * exp(-lam_tc * 9.0), 2), 1.2e2, 1e-9)

# Stretch: two isotopes
eq("X 10h", 800 * 0.5**5, 25); eq("Y 10h", 800 * 0.5, 400); eq("tot 10h", 25 + 400, 425)
eq("X 30h", sf(800 * 0.5**15, 1), 0.02, 1e-9); eq("Y 30h", 800 * 0.5**3, 100)
eq("tot 30h", sf(800 * 0.5**15 + 800 * 0.5**3, 2), 100, 1e-9)
# BE per nucleon
eq("He BE", round(4 * 7.07, 2), 28.28)
eq("react BE", round(2 * 1.11 + 3 * 2.83, 2), 10.71)
eq("DT BE", round(28.28 - 10.71, 2), 17.57)
eq("DT BE sf", sf(28.28 - 10.71, 3), 17.6, 1e-9)
eq("DT per nucleon", sf(17.57 / 5, 2), 3.5, 1e-9)
eq("fission per nucleon", sf(235 * (8.5 - 7.6) / 235, 2), 0.90, 1e-9)
eq("ratio", sf(17.57 / 5 / 0.9, 1), 4, 1e-9)

# Figure: curve points x = 80 + 2.2 A, y = 250 - 22 BE
for A, be, x, y in ((2, 1.11, 84.4, 225.6), (4, 7.07, 88.8, 94.5), (12, 7.68, 106.4, 81.0),
                    (56, 8.79, 203.2, 56.6), (235, 7.59, 597.0, 83.0)):
    eq(f"fig x {A}", round(80 + 2.2 * A, 1), x, 0.05)
    eq(f"fig y {A}", round(250 - 22 * be, 1), y, 0.06)

print("ok")
