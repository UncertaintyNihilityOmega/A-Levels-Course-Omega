# checks/phys.gases.py: recomputes every number in the Ideal gases chapter.
from math import isclose, sqrt

n_ = 0
def eq(label, got, want, tol=1e-9):
    global n_
    n_ += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

NA, R, k, K = 6.02e23, 8.31, 1.38e-23, 273.15
eq("k = R/NA", sf(R / NA, 3), 1.38e-23, 1e-26)

# Warm-up
eq("warm T", sf(27 + K, 3), 300); eq("warm dp", 2 * 0.20 * 5.0, 2.0); eq("warm p", 240 / 0.0040, 6.0e4)

# Helium sample
n = 2.0e-3 / 0.0040
eq("He n", n, 0.50); eq("He N", sf(n * NA, 2), 3.0e23, 1e21)
m = 0.0040 / NA
eq("He m", sf(m, 2), 6.6e-27, 1e-29); eq("He m u", sf(4 * 1.66e-27, 2), 6.6e-27, 1e-29)

# Pressure law graph geometry: p = 100 (1 + theta/273.15) kPa
eq("p(100)", sf(100 * (1 + 100 / K), 3), 137, 1)
eq("p(-273.15)", 100 * (1 + (-K) / K), 0, 1e-9)

# Boyle plot
eq("200/4", 200 / 4, 50); eq("300/4", 300 / 4, 75); eq("ratio T", 450 / 300, 300 / 200)

# Molecules in 1 m3 of air
N = 1.01e5 * 1.0 / (k * (20 + K))
eq("air N", sf(N, 2), 2.5e25, 1e23)
eq("per mm3", sf(N / 1e9, 2), 2.5e16, 1e15)

# Helium cylinder
T1, T2 = 15 + K, 40 + K
nHe = 1.5e7 * 0.020 / (R * T1)
eq("cyl n", sf(nHe, 3), 125, 0.5); eq("cyl n raw", sf(nHe, 4), 125.3, 0.05)
eq("cyl m", sf(nHe * 0.0040, 2), 0.50, 0.005)
eq("cyl p2", sf(1.5e7 * T2 / T1, 2), 1.6e7, 1e5)

# Bubble
V2 = 4.0 * (3.0e5 / 1.0e5) * (290 / 280)
eq("bubble V", sf(V2, 2), 12); eq("bubble V raw", sf(V2, 3), 12.4)

# Tyre
p2 = 2.0e5 * (35 + K) / (10 + K)
eq("tyre", sf(p2, 2), 2.2e5, 1e3)

# Oxygen used
dn = (3.2e5 - 2.0e5) * 0.040 / (R * 290)
eq("O2 dn", sf(dn, 3), 1.99); eq("O2 m", sf(dn * 0.032, 2), 0.064, 1e-4)
eq("O2 m g", sf(dn * 0.032 * 1000, 2), 64, 1)

# Density of nitrogen
rho = 1.01e5 * 0.028 / (R * 300)
eq("rho N2", sf(rho, 2), 1.1, 0.01); eq("rho N2 raw", sf(rho, 3), 1.13, 0.005)

# Five molecules
v = [200, 300, 400, 500, 600]
eq("mean v", sum(v) / 5, 400)
msq = sum(x * x for x in v) / 5
eq("msq", msq, 1.8e5); eq("sum sq", sum(x * x for x in v), 9.0e5)
eq("rms 5", sf(sqrt(msq), 3), 424, 0.5); eq("rms 5 2sf", sf(sqrt(msq), 2), 4.2e2, 1)
assert sqrt(msq) > 400

# Density to speed
c2 = 3 * 1.01e5 / 1.20
eq("c2", sf(c2, 3), 2.53e5, 1e3); eq("crms", sf(sqrt(c2), 2), 5.0e2, 1); eq("crms raw", sf(sqrt(c2), 3), 502, 0.5)

# Mean KE at 27 C
EK = 1.5 * k * (27 + K)
eq("EK", sf(EK, 2), 6.2e-21, 1e-23); eq("EK raw", sf(EK, 3), 6.21e-21, 1e-23)

# rms N2, He
mN = 0.028 / NA
crN = sqrt(3 * k * 300 / mN)
eq("mN", sf(mN, 3), 4.65e-26, 1e-28)
eq("rms N2", sf(crN, 2), 5.2e2, 1); eq("rms N2 raw", sf(crN, 3), 517, 1)
mHe = 0.0040 / NA
crHe = sqrt(3 * k * 300 / mHe)
eq("mHe", sf(mHe, 3), 6.64e-27, 1e-29)
eq("rms He", sf(crHe, 2), 1.4e3, 1); eq("rms He raw", sf(crHe, 3), 1370, 5)
eq("ratio He/N2", sf(sqrt(28 / 4.0), 2), 2.6, 0.01); eq("sqrt7", sf(sqrt(7), 2), 2.6, 0.01)

# Temperature factor
eq("T factor", sf(sqrt((327 + K) / (27 + K)), 3), 1.41, 0.005)
eq("sqrt12", sf(sqrt(327 / 27), 2), 3.5, 0.05); eq("327/27", 327 / 27, 12, 0.2)

# Spot the error
eq("spot wrong", sf(0.20 * R * 27 / 5.0e-3, 2), 9.0e3, 50)
pc = 0.20 * R * (27 + K) / 5.0e-3
eq("spot right", sf(pc, 2), 1.0e5, 1e3)
assert 8.97e3 * 11 > 9.5e4 and pc / (0.20 * R * 27 / 5.0e-3) > 11 and pc / (0.20 * R * 27 / 5.0e-3) < 12

# Start easy
eq("e1 n", 0.016 / 0.032, 0.50); eq("e1 N", sf(0.50 * NA, 2), 3.0e23, 1e21)
eq("e2", sf(0.0040 / NA, 2), 6.6e-27, 1e-29)
eq("e3", 2.0e5 * 0.010 / 0.0050, 4.0e5)
eq("e4", sf(1.00e5 * (80 + K) / (20 + K), 2), 1.2e5, 1e3)
eq("e5", sf(R * K / 1.01e5, 3), 0.0225, 1e-5); eq("e5 L", sf(R * K / 1.01e5 * 1e3, 3), 22.5, 0.05)
eq("e6a", sf(1.5 * k * 300, 2), 6.2e-21, 1e-23); eq("e6b", sf(1.5 * k * 600, 2), 1.2e-20, 1e-22)
v5 = [100, 200, 300, 400, 500]
eq("e7 mean", sum(v5) / 5, 300); eq("e7 msq", sum(x * x for x in v5) / 5, 1.1e5)
eq("e7 rms", sf(sqrt(1.1e5), 3), 332, 0.5)
eq("e8", sf(sqrt(32 / 28), 3), 1.07, 0.005)

# Exam practice
nn = 1.2e5 * 2.5e-3 / (R * (27 + K))
eq("x2 n", sf(nn, 2), 0.12, 0.005); eq("x2 N", sf(nn * NA, 2), 7.2e22, 1e21)
mO = 0.032 / NA
eq("x5 m", sf(mO, 3), 5.32e-26, 1e-28)
c = sqrt(3 * k * (20 + K) / mO)
eq("x5 c", sf(c, 2), 4.8e2, 1); eq("x5 c raw", sf(c, 3), 478, 1)
nAR = 1.5e5 * 2.0e-3 / 300; nBR = 1.0e5 * 3.0e-3 / 400
eq("x7 nA", nAR, 1.00); eq("x7 nB", nBR, 0.75)
p = (nAR + nBR) / (2.0e-3 / 300 + 3.0e-3 / 400)
eq("x7 p", sf(p, 2), 1.2e5, 1e3); eq("x7 p raw", sf(p, 3), 1.24e5, 500)
mH = 0.0020 / NA
eq("x8 m", sf(mH, 3), 3.32e-27, 1e-29)
cH = sqrt(3 * k * 300 / mH)
eq("x8 c", sf(cH, 2), 1.9e3, 10)

# Stretch 1
eq("s1 ratio", sf(sqrt(0.040 / 0.0040), 2), 3.2, 0.05)
eq("s1 p", sf(2.0 * R * 300 / 0.050, 2), 1.0e5, 1e3)
# Stretch 2 (Venus)
c2v = 3 * 9.2e6 / 65
eq("s2 c2", sf(c2v, 3), 4.25e5, 500); eq("s2 c", sf(sqrt(c2v), 2), 6.5e2, 1)
Tv = 7.3e-26 * c2v / (3 * k)
eq("s2 T", sf(Tv, 2), 7.5e2, 5); eq("s2 C", sf(Tv - K, 2), 480, 5)
assert Tv - K > 327

print("ok")
