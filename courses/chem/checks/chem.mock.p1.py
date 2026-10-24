# checks/chem.mock.p1.py: recomputes every number in Mock paper 1 (Paper 1 multiple choice).
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, N 14.0, O 16.0, Mg 24.3, Cl 35.5, Ca 40.1.
# Data booklet / FACTS.md: R = 8.31, c = 4.18, Vm = 24.0 (room), 22.4 (s.t.p.); bond energies N#N 944, H-H 436, N-H 390,
# C-Cl 340, C-Br 280, C-I 240; IE Ca 590 1150 4940 6480.
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

H, C, N, O, Mg, Cl, Ca = 1.0, 12.0, 14.0, 16.0, 24.3, 35.5, 40.1

# Q2 Ar from isotopes
ar = (24 * 79.0 + 25 * 10.0 + 26 * 11.0) / 100
eq("Q2 Ar", round(ar, 1), 24.3)
eq("Q2 abundances", 79.0 + 10.0 + 11.0, 100.0)
eq("Q2 Ar vs table", round(ar, 1), Mg)
eq("Q2 unweighted mean", (24 + 25 + 26) / 3, 25.0)

# Q3 successive IE jump
ie = [590, 1150, 4940, 6480]
r = [ie[i + 1] / ie[i] for i in range(3)]
assert r[1] > 4 and r[0] < 2.5 and r[2] < 1.5

# Q4 empirical formula
nc, nh = 85.7 / C, 14.3 / H
eq("Q4 ratio H:C", round(nh / nc, 2), 2.00, 0.01)
eq("Q4 Mr/14", 84.0 / (C + 2 * H), 6.0)
eq("Q4 C3H6 Mr", 3 * C + 6 * H, 42.0)

# Q5 Na2CO3 + 2HCl
n = 0.0250 * 0.100
V = 2 * n / 0.150 * 1000
eq("Q5 V", round(V, 1), 33.3)
eq("Q5 1:1", round(n / 0.150 * 1000, 1), 16.7)
eq("Q5 0.100", round(2 * n / 0.100 * 1000, 1), 50.0)
eq("Q5 inverted", round(25.0 * 2 * 0.150 / 0.100, 1), 75.0)

# Q6 sigma and pi in CH2=CH-C#N
sigma = 3 + 1 + 1 + 1
pi = 1 + 2
eq("Q6 sigma", sigma, 6)
eq("Q6 pi", pi, 3)

# Q8 pV = nRT
p, Vm3, T, m, R = 1.00e5, 1.25e-4, 300.0, 0.320, 8.31
nn = p * Vm3 / (R * T)
Mr = m / nn
eq("Q8 n", sf(nn), 5.01e-3, 1e-12)
eq("Q8 Mr", sf(Mr), 63.8)
eq("Q8 kPa+cm3", sf(m / (100 * 125 / (R * T))), 0.0638, 1e-9)
eq("Q8 kPa+m3", sf(m / (100 * 1.25e-4 / (R * T))), 6.38e4, 1)
eq("Q8 Pa+cm3", sf(m / (1.00e5 * 125 / (R * T))), 6.38e-5, 1e-9)

# Q10 N2 + 3H2 -> 2NH3
broken = 944 + 3 * 436
made = 6 * 390
eq("Q10 broken", broken, 2252)
eq("Q10 made", made, 2340)
eq("Q10 dH", broken - made, -88)
eq("Q10 per mol", (broken - made) / 2, -44)
eq("Q10 three N-H", broken - 3 * 390, 1082)

# Q11 neutralisation
q = 100 * 4.18 * 6.80
eq("Q11 q", round(q, 1), 2842.4)
dH = -q / 0.0500
eq("Q11 dH J", round(dH), -56848)
eq("Q11 dH kJ", sf(dH / 1000), -56.8)
eq("Q11 n=0.100", sf(-q / 0.100 / 1000), -28.4)

# Q12 MnO4- / Fe2+
nFe = 0.0250 * 0.100
nMn = nFe / 5
eq("Q12 V", round(nMn / 0.0250 * 1000, 2), 20.0)
eq("Q12 1:1", nFe / 0.0250 * 1000, 100.0)
eq("Q12 x5", nFe * 5 / 0.0250 * 1000, 500.0)
eq("Q12 /25", round(nFe / 25 / 0.0250 * 1000, 2), 4.00)

# Q13 Kc N2O4 <=> 2NO2
no2 = 0.0400
n2o4 = 0.100 - no2 / 2
eq("Q13 [N2O4]", n2o4, 0.0800)
eq("Q13 Kc", no2 ** 2 / n2o4, 0.0200, 1e-12)
eq("Q13 initial", no2 ** 2 / 0.100, 0.0160, 1e-12)
eq("Q13 multiply", 2 * no2 ** 2 / n2o4, 0.0400, 1e-12)
eq("Q13 inverted", sf(n2o4 / no2 ** 2), 50.0)

# Q18 CaCO3
Mcc = Ca + C + 3 * O
eq("Q18 Mr", Mcc, 100.1)
eq("Q18 mass", sf(1.00 / 24.0 * Mcc), 4.17)
eq("Q18 22.4", sf(1.00 / 22.4 * Mcc), 4.47)
eq("Q18 double", sf(2 * 1.00 / 24.0 * Mcc), 8.34)
eq("Q18 half", sf(0.5 * 1.00 / 24.0 * Mcc), 2.09)

# Q23 NH4Cl
Mnh = N + 4 * H + Cl
eq("Q23 Mr", Mnh, 53.5)
nn = 2.14 / Mnh
eq("Q23 n", round(nn, 4), 0.0400)
eq("Q23 V", round(nn * 24.0 * 1000), 960)
eq("Q23 22.4", round(nn * 22.4 * 1000), 896)
eq("Q23 double", round(2 * nn * 24.0 * 1000), 1920)
eq("Q23 half", round(0.5 * nn * 24.0 * 1000), 480)

# Q26 C5H10 alkenes
alkenes = ["pent-1-ene", "pent-2-ene (E)", "pent-2-ene (Z)", "2-methylbut-1-ene", "3-methylbut-1-ene", "2-methylbut-2-ene"]
eq("Q26 count", len(alkenes), 6)

# Q31 bond energies order
assert 240 < 280 < 340

# Q36 percentage yield
Macid = 2 * C + 4 * H + 2 * O
Mester = 4 * C + 8 * H + 2 * O
eq("Q36 Mr acid", Macid, 60.0)
eq("Q36 Mr ester", Mester, 88.0)
nacid = 3.00 / Macid
eq("Q36 n", nacid, 0.0500)
theo = nacid * Mester
eq("Q36 theoretical", theo, 4.40, 1e-9)
eq("Q36 yield", sf(3.30 / theo * 100), 75.0)
eq("Q36 no Mr", sf(3.30 / 3.00 * 100), 110.0)
eq("Q36 doubled", sf(3.30 / (2 * theo) * 100), 37.5)
eq("Q36 inverted", sf(theo / 3.30 * 100), 133.0)

# Q40 [M+1]
nC = 100 * 1.76 / (1.1 * 32.0)
eq("Q40 n", round(nC, 2), 5.00)
eq("Q40 no 1.1", 100 * 1.76 / 32.0, 5.5)
eq("Q40 inverted", round(32.0 / 1.76, 1), 18.2)

# answer key and balance (read the chapter and compare)
key = "CBDACAACDDBCBDBBACADABCDBCADABDACDCBDACB"
assert len(key) == 40
counts = {k: key.count(k) for k in "ABCD"}
assert counts == {"A": 10, "B": 10, "C": 10, "D": 10}, counts
import re, pathlib
text = pathlib.Path(__file__).resolve().parent.parent.joinpath("chapters", "chem.mock.p1.md").read_text(encoding="utf-8")
got = "".join(re.findall(r"^A: \*\*([ABCD])\*\*", text, flags=re.M))
assert got == key, (got, key)
assert len(re.findall(r"^Q: \[1 mark\]", text, flags=re.M)) == 40
print("ok")
