# checks/chem.org.arenes.py: recomputes every number in the Arenes chapter.
# Ar values from the 9701 Periodic Table: H 1.0, C 12.0, N 14.0, O 16.0.
# Bond lengths (nm) and hydrogenation enthalpies (kJ mol-1) are standard textbook values quoted in the text and given as data in the questions.
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

H, C, N, O = 1.0, 12.0, 14.0, 16.0
Mr_C6H6 = 6 * C + 6 * H
Mr_PhNO2 = 6 * C + 5 * H + N + 2 * O
eq("Mr benzene", Mr_C6H6, 78.0)
eq("Mr nitrobenzene", Mr_PhNO2, 123.0)

# hydrogenation enthalpy worked example
h_ene, h_benz, h_diene = -120, -208, -232
eq("predicted benzene", 3 * h_ene, -360)
eq("stabilisation", h_benz - 3 * h_ene, 152)
# stretch: diene
eq("predicted diene", 2 * h_ene, -240)
eq("diene difference", h_diene - 2 * h_ene, 8)

# yield worked example: 15.6 g benzene -> 19.1 g nitrobenzene
nb = 15.6 / Mr_C6H6
eq("eg moles", round(nb, 3), 0.200)
mmax = nb * Mr_PhNO2
eq("eg max mass", round(mmax, 1), 24.6)
eq("eg yield", round(19.1 / mmax * 100, 1), 77.6)

# exam Q: 7.80 g -> 8.90 g
nb2 = 7.80 / Mr_C6H6
eq("Q moles", round(nb2, 3), 0.100)
m2 = nb2 * Mr_PhNO2
eq("Q max", round(m2, 1), 12.3)
eq("Q yield", round(8.90 / m2 * 100, 1), 72.4)

# quiz: 11.7 g benzene, 80.0 % yield
nq = 11.7 / Mr_C6H6
eq("quiz moles", round(nq, 3), 0.150)
eq("quiz max", round(nq * Mr_PhNO2, 2), 18.45)
eq("quiz actual", round(nq * Mr_PhNO2 * 0.800, 1), 14.8)
# distractors: 18.5 g is the theoretical mass (18.45); 23.1 g divides by 0.800 instead of multiplying
eq("quiz theoretical option", nq * Mr_PhNO2, 18.45, 1e-9)
eq("quiz divide option", round(nq * Mr_PhNO2 / 0.800, 1), 23.1)

# bond lengths and energies quoted: C-C 0.154 > benzene 0.140 > C=C 0.134 nm; 350 < 520 < 610 kJ/mol
assert 0.154 > 0.140 > 0.134
assert 350 < 520 < 610
print("ok", n)
