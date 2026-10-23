# checks/chem.equilibria.py: recomputes every number in the Chemical equilibria chapter.
from math import isclose, sqrt, exp

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def same(label, got, want):
    global n
    n += 1
    assert got == want, f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# ---- warm-up
eq("warm c", 0.200 / 0.500, 0.400)

# ---- plots: the levels the text quotes (A falls to 0.4, B rises to 0.6, rates meet at 0.4)
A = lambda t: 1 - 0.6 * (1 - exp(-t)); B = lambda t: 0.6 * (1 - exp(-t)); R = lambda t: 0.4 * (1 - exp(-t))
eq("A end", A(30), 0.4, 1e-9); eq("B end", B(30), 0.6, 1e-9); eq("rates meet", A(30), R(30), 1e-9)
eq("A+B conserved", A(2.3) + B(2.3), 1.0)
eq("kf/kr = K", 0.6 / 0.4, 1.0 / (2 / 3))  # kf = 1, kr = 2/3: rate_r = (2/3)(0.6)(...) = 0.4(...)
eq("reverse rate coefficient", (2 / 3) * 0.6, 0.4)

# ---- units of Kc: power of mol dm-3 is (moles of products) - (moles of reactants)
same("Haber dn", 2 - (1 + 3), -2); same("N2O4 dn", 2 - 1, 1); same("SO3 dn", 2 - (2 + 1), -1); same("HI dn", 2 - 2, 0)
same("NO + O2 dn", 2 - 3, -1)
same("Haber gas moles", (1 + 3, 2), (4, 2)); same("Contact gas moles", (2 + 1, 2), (3, 2))

# ---- Kc from equilibrium moles
eq("ester initial acid", 0.200 + 0.400, 0.600)
eq("ester Kc", (0.400 * 0.400) / (0.200 * 0.200), 4.00)
eq("HI used", 1.50 / 2, 0.75); eq("H2 left", 1.00 - 0.75, 0.25)
eq("HI Kc", 1.50 ** 2 / (0.25 * 0.25), 36.0)
eq("N2O4 used", 1.00 - 0.600, 0.400); eq("NO2 formed", 2 * 0.400, 0.800)
eq("N2O4 conc", 0.600 / 2.00, 0.300); eq("NO2 conc", 0.800 / 2.00, 0.400)
eq("N2O4 Kc", sf(0.400 ** 2 / 0.300), 0.533)
eq("SO2 left", 2.00 - 1.60, 0.40); eq("O2 left", 1.00 - 0.80, 0.20)
eq("SO2 c", 0.40 / 5.00, 0.0800); eq("O2 c", 0.20 / 5.00, 0.0400); eq("SO3 c", 1.60 / 5.00, 0.320)
eq("SO3 Kc", sf(0.320 ** 2 / (0.0800 ** 2 * 0.0400)), 400, 1e-6)
# equilibrium amount from Kc = 4.00 (perfect square)
x = 2.00 / 3.00
eq("ester x", round(x, 3), 0.667); eq("K check", x ** 2 / (1 - x) ** 2, 4.00, 1e-9)
eq("x/(1-x)", sqrt(4.00), 2.00); eq("3x=2", 2.00 / 3.00, x)
eq("reverse Kc", 1 / 4.00, 0.250)
# Haber from initial amounts
eq("NH3 N2 used", 0.600 / 2, 0.300); eq("NH3 H2 used", 0.600 * 3 / 2, 0.900)
eq("N2 eq", 1.00 - 0.300, 0.700); eq("H2 eq", 3.00 - 0.900, 2.10)
eq("N2 c", 0.700 / 2.00, 0.350); eq("H2 c", 2.10 / 2.00, 1.05); eq("NH3 c", 0.600 / 2.00, 0.300)
eq("Haber Kc", sf(0.300 ** 2 / (0.350 * 1.05 ** 3)), 0.222)
# spot the error
eq("err N2 c", 0.400 / 2.00, 0.200); eq("err H2 c", 1.20 / 2.00, 0.600); eq("err NH3 c", 0.400 / 2.00, 0.200)
eq("err wrong Kc", sf(0.200 / (0.200 * 0.600)), 1.67)
eq("err correct num", 0.200 ** 2, 0.0400); eq("err correct den", 0.200 * 0.600 ** 3, 0.0432, 1e-12)
eq("err correct Kc", sf(0.0400 / 0.0432), 0.926)

# ---- mole fraction and partial pressure
tot = 1.00 + 3.00 + 1.00
eq("tot", tot, 5.00); eq("x N2", 1.00 / tot, 0.200); eq("x H2", 3.00 / tot, 0.600); eq("x NH3", 1.00 / tot, 0.200)
eq("x sum", 0.200 + 0.600 + 0.200, 1.00)
eq("p N2", 0.200 * 200, 40.0); eq("p H2", 0.600 * 200, 120); eq("p NH3", 0.200 * 200, 40.0); eq("p sum", 40.0 + 120 + 40.0, 200)
eq("Haber Kp denominator", 40.0 * 120 ** 3, 6.912e7, 1)
eq("Haber Kp", sf(40.0 ** 2 / (40.0 * 120 ** 3)), 2.31e-5, 1e-9)
# N2O4 Kp in Pa
t2 = 0.600 + 0.800
eq("x N2O4", round(0.600 / t2, 4), 0.4286); eq("x NO2", round(0.800 / t2, 4), 0.5714)
pN = 0.600 / t2 * 2.00e5; pO = 0.800 / t2 * 2.00e5
eq("p N2O4", sf(pN, 4), 8.571e4, 1); eq("p NO2", sf(pO, 4), 1.143e5, 10)
eq("N2O4 Kp", sf(pO ** 2 / pN), 1.52e5, 1e2)
# PCl5
eq("PCl5 dec", 0.250 * 2.00, 0.500); eq("PCl5 eq", 2.00 - 0.500, 1.50); eq("PCl5 total", 1.50 + 0.500 + 0.500, 2.50)
eq("x PCl5", 1.50 / 2.50, 0.600); eq("x PCl3", 0.500 / 2.50, 0.200)
eq("p PCl5", 0.600 * 3.00, 1.80); eq("p PCl3", 0.200 * 3.00, 0.600)
eq("PCl5 Kp", 0.600 * 0.600 / 1.80, 0.200)

# ---- practice
eq("try x A", 0.50 / 4.00, 0.125); eq("try x B", 1.50 / 4.00, 0.375); eq("try x C", 2.00 / 4.00, 0.500)
eq("try pC", 0.500 * 5.00, 2.50)
eq("try reverse K", 1 / 0.250, 4.00)
eq("try HI Kc", 0.500 ** 2 / (0.100 * 0.100), 25.0)
eq("try Kp", 4.0 ** 2 / (2.0 * 2.0), 4.0)
# exam practice
eq("exam HI Kc", 1.20 ** 2 / (0.200 * 0.300), 24.0)
eq("exam PCl5 Kc n", 2.00 - 0.500, 1.50)
eq("exam PCl5 c1", 1.50 / 4.00, 0.375); eq("exam PCl5 c2", 0.500 / 4.00, 0.125)
eq("exam PCl5 Kc", sf(0.125 * 0.125 / 0.375), 0.0417, 1e-6)
tot3 = 2.00 + 5.00 + 3.00
eq("exam tot", tot3, 10.0)
eq("exam x", 2.00 / tot3, 0.200); eq("exam x2", 5.00 / tot3, 0.500); eq("exam x3", 3.00 / tot3, 0.300)
eq("exam p", 0.200 * 100, 20.0); eq("exam p2", 0.500 * 100, 50.0); eq("exam p3", 0.300 * 100, 30.0)
eq("exam Kp den", 20.0 * 50.0 ** 3, 2.50e6, 1)
eq("exam Kp", sf(30.0 ** 2 / (20.0 * 50.0 ** 3)), 3.60e-4, 1e-9)
# esterification, mass of ester: Mr(CH3COOC2H5) = C4H8O2
import json
Ar = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
Mr = 4 * Ar['C'] + 8 * Ar['H'] + 2 * Ar['O']
eq("ester Mr", Mr, 88.0); eq("ester mass", sf(2.00 / 3.00 * Mr), 58.7)
# exam practice: Kc = 9.00, 1.50 mol each
x2 = 1.50 * 3.00 / 4.00
eq("ester2 x", x2, 1.125, 1e-12); eq("ester2 x 3sf", round(x2 + 1e-9, 2), 1.13); eq("ester2 K", x2 ** 2 / (1.50 - x2) ** 2, 9.00, 1e-9)
eq("ester2 sqrt", sqrt(9.00), 3.00); eq("ester2 mass", sf(x2 * Mr), 99.0)
# try: H2 + I2 <=> 2HI, Kc = 49.0
eq("HI sq", 49.0 * 0.0200 * 0.0200, 0.0196, 1e-12); eq("HI", sqrt(0.0196), 0.140, 1e-9)

# ---- stretch: N2O4 dissociation, alpha = 0.200 at 2.00 atm, then 4.00 atm
a = 0.200
tn = 1 + a
eq("S1 N2O4 mol", 1 - a, 0.800); eq("S1 NO2 mol", 2 * a, 0.400); eq("S1 total", tn, 1.200)
eq("S1 x N2O4", round((1 - a) / tn, 4), 0.6667, 1e-4); eq("S1 x NO2", round(2 * a / tn, 4), 0.3333, 1e-4)
p1 = (1 - a) / tn * 2.00; p2 = 2 * a / tn * 2.00
eq("S1 p N2O4", round(p1, 3), 1.333); eq("S1 p NO2", round(p2, 4), 0.6667, 1e-4)
Kp = p2 ** 2 / p1
eq("S1 Kp", sf(Kp), 0.333)
eq("S1 Kp formula", 4 * a ** 2 * 2.00 / (1 - a ** 2), Kp)
a2sq = Kp / (16 + Kp)
eq("S1 alpha^2", round(a2sq, 5), 0.02041, 1e-5); eq("S1 alpha", sf(sqrt(a2sq)), 0.143)
eq("S1 exact 1/7", sqrt(a2sq), 1 / 7)
eq("S1 16.333", 16 + Kp, 16.333, 1e-3)
# methanol
eq("S2 Kc", 0.0150 / (0.0500 * 0.100 ** 2), 30.0)
same("S2 gas moles", (1 + 2, 1), (3, 1))

# ---- quiz
eq("quiz N2O4 wrong moles", sf(0.800 ** 2 / 0.600), 1.07)
eq("quiz N2O4 Kc", sf(0.400 ** 2 / 0.300), 0.533)
eq("quiz 2.13", sf(4 * 0.400 ** 2 / 0.300), 2.13); eq("quiz 0.267", sf(0.400 ** 2 / 0.300 / 2), 0.267)
print("ok")
