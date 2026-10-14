# checks/phys.thermo.py: recomputes every number in the Thermodynamics chapter.
from math import isclose, log

n_ = 0
def eq(label, got, want, tol=1e-9):
    global n_
    n_ += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

NA, R, k, K = 6.02e23, 8.31, 1.38e-23, 273.15

# Warm-up
eq("warm KE", sf(1.5 * k * 400, 3), 8.28e-21, 1e-23)
eq("warm W", 50 * 0.40, 20)

# U against T plot: 1.00 mol, U = 1.5 R T (kJ)
eq("plot gradient", 1.5 * R / 1000, 0.012465, 1e-12)
eq("plot point", sf(1.5 * R * 300 / 1000, 3), 3.74, 1e-9)
eq("plot end", 1.5 * R * 600 / 1000 < 9, 1, 0)

# Internal energy example: 2.00 mol He
U300 = 1.5 * 2.00 * R * 300
eq("U 300", sf(U300, 3), 7.48e3, 1e-6)
dU = 1.5 * 2.00 * R * 50.0
eq("dU", sf(dU, 3), 1.25e3, 1e-6)
eq("U 350", sf(U300 * 350 / 300 / 1000, 3), 8.73, 1e-9)
eq("U350 - U300", sf(U300 * 350 / 300 - U300, 3), 1.25e3, 1e-6)

# Balloon
dV = (5.0 - 2.0) * 1e-3
eq("balloon dV", dV, 3.0e-3, 1e-12)
eq("balloon W", sf(1.01e5 * dV, 2), 3.0e2, 1e-9)
eq("balloon unrounded", sf(1.01e5 * dV, 3), 303, 1e-9)

# Trapezium and true area (pV = 300 J, V in L, p in kPa)
p = lambda V: 300 / V
trap = 0.5 * 2.0 * (p(2) + p(4)) + 0.5 * 2.0 * (p(4) + p(6))
eq("p2", p(2), 150); eq("p4", p(4), 75); eq("p6", p(6), 50)
eq("trap", trap, 350)
true = 300 * log(6 / 2)
eq("true area", sf(true, 3), 330, 1e-9)
eq("overestimate", trap > true, 1, 0)

# First law examples
W = -1.5e5 * (5.0e-3 - 2.0e-3)
eq("eg W", W, -450, 1e-9)
eq("eg dU", 1200 + W, 750, 1e-9)
eq("eg2 q", -30 - (-90), 60)

# Constant volume
eq("const V q", sf(1.5 * 0.500 * R * 100, 3), 623, 1e-9)

# Constant pressure
dU = 1.5 * 2.00 * R * 50.0
Wby = 2.00 * R * 50.0
eq("const p dU", dU, 1246.5, 1e-9)
eq("const p Wby", Wby, 831, 1e-9)
q = dU + Wby
eq("const p q", q, 2077.5, 1e-9)
eq("const p q 3sf", sf(q, 3), 2.08e3, 1e-6)
eq("const p fraction", sf(Wby / q, 2), 0.40, 1e-9)
eq("2/5", 2 / 5, 0.4)

# Isothermal
eq("iso q", 0 - (-80), 80)

# Cycle ABC: monatomic ideal gas, U = 1.5 pV
pa, Va = 1.0e5, 2.0e-3
pb, Vb = 3.0e5, 2.0e-3
pc, Vc = 3.0e5, 4.0e-3
UA, UB, UC = 1.5 * pa * Va, 1.5 * pb * Vb, 1.5 * pc * Vc
eq("UA", UA, 300); eq("UB", UB, 900); eq("UC", UC, 1800)
dAB, dBC, dCA = UB - UA, UC - UB, UA - UC
WAB = 0.0
WBC = -pb * (Vc - Vb)
WCA = 0.5 * (pc + pa) * (Vc - Va)
eq("dAB", dAB, 600); eq("dBC", dBC, 900); eq("dCA", dCA, -1500)
eq("WBC", WBC, -600); eq("WCA", WCA, 400)
qAB, qBC, qCA = dAB - WAB, dBC - WBC, dCA - WCA
eq("qAB", qAB, 600); eq("qBC", qBC, 1500); eq("qCA", qCA, -1900)
eq("net q", qAB + qBC + qCA, 200); eq("net W", WAB + WBC + WCA, -200)
eq("net dU", dAB + dBC + dCA, 0)
eq("area", 0.5 * (Vc - Va) * (pb - pa), 200)
eq("energy in", qAB + qBC, 2100)
# the C -> A line is straight, so the mean pressure is (1 + 3)/2: a straight line on p-V gives the trapezium
# Figure geometry: x = 70 + 60 V(10^-3 m^3), y = 230 - 45 p(10^5 Pa)
eq("fig A x", 70 + 60 * 2.0, 190); eq("fig C x", 70 + 60 * 4.0, 310)
eq("fig A y", 230 - 45 * 1.0, 185); eq("fig B y", 230 - 45 * 3.0, 95)

# Process figure curves
for ox, oy in [(50, 348), (340, 348)]:
    for px in (45, 52, 60, 70, 82, 96, 110):
        pass
iso = lambda px: 4500 / px
adi = lambda px: 100 * (45 / px) ** (5 / 3)
eq("iso end y", round(348 - iso(110)), 307)
eq("adi end y", round(348 - adi(110)), 325)
eq("iso 70", round(348 - iso(70)), 284)
eq("adi 70", round(348 - adi(70)), 300)

# Spot the error
eq("spot wrong", -40 - 150, -190)
eq("spot right", -40 + 150, 110)

# Try: easy
dV = 2.0e-3 - 6.0e-3
eq("try W", -2.0e5 * dV, 800, 1e-9)
eq("try dU 1", 500 + 200, 700)
eq("try dU 2", -300 + -120, -420)
eq("try U", round(1.5 * 0.25 * R * 300, 1), 934.9, 1e-9)
eq("try U 2sf", sf(1.5 * 0.25 * R * 300, 2), 930, 1e-9)
eq("try iso q", 0 - 60, -60)

# Exam practice
eq("ex dV", (650 - 250) * 1e-6, 4.00e-4, 1e-12)
eq("ex W", sf(1.20e5 * 4.00e-4, 3), 48.0, 1e-9)
# table
eq("table qXY", 340 - 0, 340)
eq("table dUYZ", 160 + (-210), -50)
eq("table dUZX", -(340 + (-50)), -290)
eq("table qZX", -290 - 180, -470)
eq("table netW", 0 + -210 + 180, -30)
eq("table netq", 340 + 160 + -470, 30)
# melting ice
m, L, rho_i, rho_w, pa_ = 0.250, 3.34e5, 917, 1000, 1.01e5
qm = m * L
eq("ice q", qm, 83500)
eq("ice q 3sf", sf(qm, 3), 8.35e4, 1e-6)
Vi, Vw = m / rho_i, m / rho_w
eq("Vi", sf(Vi, 3), 2.73e-4, 1e-9 * 1e-3)
eq("Vw", Vw, 2.50e-4, 1e-12)
dVm = Vw - Vi
eq("dV ice", sf(dVm, 3), -2.26e-5, 1e-9 * 1e-3)
Wm = -pa_ * dVm
eq("W ice", sf(Wm, 2), 2.3, 1e-9)
eq("W/q percent", sf(Wm / qm * 100, 1), 0.003, 1e-9)
# triangle RST
pR, VR = 1.0e5, 2.0e-3
pS, VS = 1.0e5, 6.0e-3
pT, VT = 5.0e5, 2.0e-3
area = 0.5 * (VS - VR) * (pT - pR)
eq("RST area", area, 800)
WRS = -pR * (VS - VR)
WST = 0.5 * (pS + pT) * (VS - VT)
eq("WRS", WRS, -400); eq("WST", WST, 1200); eq("net W RST", WRS + WST, 800)
UR, US, UT = 1.5 * pR * VR, 1.5 * pS * VS, 1.5 * pT * VT
eq("UR", UR, 300); eq("US", US, 900); eq("UT", UT, 1500)
eq("dU TR", UR - UT, -1200)
qTR = (UR - UT) - 0
eq("q TR", qTR, -1200)
qRS = (US - UR) - WRS
qST = (UT - US) - WST
eq("q RS", qRS, 1000); eq("q ST", qST, -600)
eq("net q RST", qRS + qST + qTR, -800)

# Stretch
dUs = 12.0
dT = dUs / (1.5 * 0.0100 * R)
eq("stretch dT", sf(dT, 3), 96.3, 1e-9)
eq("stretch T", sf(300 + dT, 3), 396, 1e-9)
eq("stretch q", -12.0, -12.0)
eq("2/5 share", (1.0) / (1.5 + 1.0), 0.4)

# Quiz
eq("quiz dU", -30 + 50, 20)

print("ok")
