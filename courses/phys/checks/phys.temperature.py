# checks/phys.temperature.py: recomputes every number in the Temperature chapter.
from math import isclose, exp

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

C_W, C_ICE, C_AL, C_CU = 4200, 2100, 900, 390
LF, LV = 3.34e5, 2.26e6
K = 273.15

# Warm-up
eq("warm E", 3000 * 120, 3.6e5)
eq("warm P", 12 * 4.0, 48)
eq("warm m", 450 / 1000, 0.450)

# Thermometer graph: B reading when A reads 50
B = lambda x: 100 * (exp(0.004 * x) - 1) / (exp(0.4) - 1)
eq("B at 0", B(0), 0, 1e-9); eq("B at 100", B(100), 100, 1e-9)
eq("B at 50", sf(B(50), 3), 45.0)

# Conversions
eq("37C", sf(37 + K, 3), 310); eq("37C raw", 37 + K, 310.15)
eq("85K", sf(85 - K, 3), -188); eq("85K raw", 85 - K, -188.15, 1e-9)
eq("N2", sf(-196 + K, 2), 77); eq("N2 raw", -196 + K, 77.15, 1e-9)

# Kettle
E = 0.50 * C_W * 80
eq("kettle E", E, 1.68e5); eq("kettle t", E / 2000, 84)

# Tea and bath
tea = 0.25 * C_W * 60
bath = 150 * C_W * 20
eq("tea", tea, 6.3e4); eq("bath", bath, 1.26e7); eq("bath/tea", bath / tea, 200)
eq("rise ratio", 60 / 20, 3)

# Electrical method: gradient
eq("c elec", 50 / (1.0 * 0.050), 1.0e3)
eq("plot pt", 20 + 0.050 * 300, 35)

# Mixtures: copper into water
th = (0.300 * C_W * 20.0 + 0.200 * C_CU * 100) / (0.300 * C_W + 0.200 * C_CU)
eq("mix theta", sf(th, 2), 25); eq("mix theta raw", sf(th, 3), 24.7)
eq("mix 78", 0.200 * C_CU, 78); eq("mix 1260", 0.300 * C_W, 1260)
eq("mix 7800", 78 * 100, 7800); eq("mix 25200", 1260 * 20.0, 25200)
eq("mix num", 7800 + 25200, 33000); eq("mix den", 78 + 1260, 1338)
c = 0.250 * C_W * 4.0 / (0.150 * (98 - 22.0))
eq("unknown c", sf(c, 2), 3.7e2); eq("unknown c raw", sf(c, 3), 368)
eq("11.4", 0.150 * 76, 11.4); eq("4200", 0.250 * C_W * 4.0, 4200)

# Latent heat
eq("L ratio", sf(LV / LF, 3), 6.77)
q1 = 0.20 * C_ICE * 10; q2 = 0.20 * LF; q3 = 0.20 * C_W * 20
eq("ice q1", q1, 4200); eq("ice q2", q2, 66800); eq("ice q3", q3, 16800)
eq("ice total", q1 + q2 + q3, 87800)
assert q2 / (q1 + q2 + q3) > 0.75

# Steam
qs = 0.050 * LV
eq("steam q", qs, 1.13e5)
th = (qs + 0.050 * C_W * 100 + 0.40 * C_W * 20) / (0.050 * C_W + 0.40 * C_W)
eq("steam theta", sf(th, 2), 89); eq("steam theta raw", sf(th, 3), 88.7)
eq("steam 21000", 0.050 * C_W * 100, 21000); eq("steam 210", 0.050 * C_W, 210)
eq("steam 1680", 0.40 * C_W, 1680); eq("steam 33600", 1680 * 20, 33600)
eq("steam num", 113000 + 21000 + 33600, 167600); eq("steam den", 210 + 1680, 1890)
eq("steam equiv", sf(qs / (0.40 * C_W), 2), 67)

# Funnel experiment
E = 12 * 5.0 * 300
eq("funnel E", E, 1.8e4)
dm = (62.0 - 8.0) * 1e-3
eq("funnel dm", dm, 0.0540)
eq("funnel L", sf(E / dm, 2), 3.3e5)

# Two-power
L = (60 - 40) * 600 / ((14.3 - 9.00) * 1e-3)
eq("2p num", 20 * 600, 1.2e4); eq("2p L", sf(L, 3), 2.26e6)

# Spot the error
eq("spot wrong", sf(2.0 * C_W * 288, 2), 2.4e6)
eq("spot right", sf(2.0 * C_W * 15, 2), 1.3e5); eq("spot raw", 2.0 * C_W * 15, 126000)
assert 15 / 288 < 0.06 and 2.0 * C_W * 288 / (2.0 * C_W * 15) > 19

# Start easy
eq("e1 T", sf(-40 + K, 3), 233); eq("e1 th", sf(500 - K, 3), 227)
eq("e3", 2.0 * C_AL * 50, 9.0e4)
eq("e4 E", 0.30 * LF, 100200); eq("e4 t", sf(0.30 * LF / 1500, 2), 67)
eq("e5", sf(0.40 * LV, 2), 9.0e5)
eq("e6 frac", 19.5 / 38.5 * 100, 50.649350649, 1e-6); eq("e6", sf(19.5 / 38.5 * 100, 2), 51)
eq("e7 E", 100 * 180, 1.8e4); eq("e7 dth", sf(18000 / (0.25 * C_W), 2), 17)

# Exam practice
eq("x1a", sf(37 + K, 3), 310); eq("x1b", sf(85 - K, 3), -188)
th = (0.200 * C_W * 18 + 0.120 * C_AL * 95) / (0.200 * C_W + 0.120 * C_AL)
eq("x4 theta", sf(th, 2), 27)
eq("x4 108", 0.120 * C_AL, 108); eq("x4 840", 0.200 * C_W, 840)
eq("x4 10260", 108 * 95, 10260); eq("x4 15120", 840 * 18, 15120)
eq("x4 num", 10260 + 15120, 25380); eq("x4 den", 108 + 840, 948)
eq("x5 E", 150 * 300, 4.5e4); eq("x5 L", sf(4.5e4 / 0.0188, 3), 2.39e6)
eq("x6 c", sf(500 * 90 / (0.50 * 60), 2), 1.5e3)
eq("x6 E1", 500 * 90, 4.5e4)
eq("x6 L", 500 * 300 / 0.50, 3.0e5); eq("x6 E2", 500 * 300, 1.5e5)
eq("x7 L", sf(20 * 600 / 5.30e-3, 3), 2.26e6)
eq("x7 mL", sf(0.0143 * 2.26e6, 2), 3.2e4); eq("x7 mL raw", 0.0143 * 2.26e6, 32318, 1)
eq("x7 supplied", 60 * 600, 36000)
eq("x7 loss", sf((36000 - 32318) / 600, 1), 6)

# Stretch: shower
mdot = 5.0 / 60
eq("sh mdot", sf(mdot, 3), 0.0833)
P = mdot * C_W * 28
eq("sh P", sf(P, 2), 9.8e3)
eq("sh eff", sf(9.8 / 10.5, 2), 0.93)
eq("sh factor", sf(28 / 38, 2), 0.74); eq("sh flow", sf(5.0 * 28 / 38, 2), 3.7)

# Stretch: ice cube
Em = 0.025 * LF
eq("ice melt", Em, 8350)
th = (0.250 * C_W * 22 - Em) / (0.250 * C_W + 0.025 * C_W)
eq("ice theta", sf(th, 3), 12.8); eq("ice theta 2", sf(th, 2), 13)
eq("ice 1050", 0.250 * C_W, 1050); eq("ice 23100", 1050 * 22, 23100)
eq("ice 105", 0.025 * C_W, 105); eq("ice 1155", 1050 + 105, 1155)
eq("ice num", 23100 - 8350, 14750)
eq("ice q", 0.250 * C_W * 22, 2.31e4)
eq("ice mmax", sf(0.250 * C_W * 22 / LF, 2), 0.069)

print("ok")
