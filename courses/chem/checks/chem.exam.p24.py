# checks/chem.exam.p24.py: recomputes every number in the Papers 2 and 4 survival guide.
# Data booklet first IE (FACTS.md): P 1060, S 1000 kJ mol-1.
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

eq("P2 minutes per mark", 75 / 60, 1.25)
eq("P4 minutes per mark", 120 / 100, 1.2)
IE = {"P": 1060, "S": 1000}
assert IE["S"] < IE["P"]
# model answer marks and weak answer marks
assert 1 + 1 + 1 == 3
assert 1 + 1 + 0 == 2
# practice try block: marks of the four questions and the ecf mole example
assert 2 + 3 + 3 + 4 == 12
assert [1 + 1, 1 + 1 + 1, 1 + 1 + 1, 1 + 1 + 1 + 1] == [2, 3, 3, 4]
n_naoh = 25.0 / 1000 * 0.200
eq("n NaOH", round(n_naoh, 5), 5.00e-3, 1e-12)
n_acid = n_naoh / 2
eq("n H2SO4", round(n_acid, 5), 2.50e-3, 1e-12)
eq("V acid dm3", round(n_acid / 0.125, 4), 0.0200, 1e-12)
eq("V acid cm3", round(n_acid / 0.125 * 1000, 1), 20.0)
# student's slip: volume not converted to dm3
s_a = 25.0 * 0.200
eq("student (a)", s_a, 5.00)
s_b = s_a / 2
eq("student n acid", s_b, 2.50)
eq("student V dm3", s_b / 0.125, 20.0)
eq("student V cm3", s_b / 0.125 * 1000, 20000.0)
assert 0 + 1 + 1 == 2     # ecf marks earned out of 3
print("ok")
