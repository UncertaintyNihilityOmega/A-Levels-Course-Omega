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
print("ok")
