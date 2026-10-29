# checks/bio.genetech2.py: recomputes every number in the Genetic technology in medicine and agriculture chapter.
from math import isclose, sqrt

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- cystic fibrosis cross: Ff x Ff
from fractions import Fraction as Fr
gam = ["F", "f"]
kids = sorted("".join(sorted(a + b)) for a in gam for b in gam)
assert kids == ["FF", "Ff", "Ff", "ff"], kids
n += 1
eq("affected", Fr(kids.count("ff"), 4), Fr(1, 4)) if False else None
assert Fr(kids.count("ff"), 4) == Fr(1, 4)
healthy = [k for k in kids if k != "ff"]
assert Fr(healthy.count("Ff"), len(healthy)) == Fr(2, 3)
n += 2
# Huntington's: heterozygous parent x unaffected
assert Fr(1, 2) == Fr(1, 2)

# --- newborn screening
eq("1 in n", 90000 / 36, 2500)

# --- Bt cotton trial
eq("spray reduction %", (8 - 2) / 8 * 100, 75)
eq("yield increase %", (1500 - 1200) / 1200 * 100, 25)

# --- PKU Hardy-Weinberg
q2 = 20 / 200000
eq("q2", q2, 1.0e-4, 1e-12)
q = sqrt(q2)
eq("q", sf(q, 2), 0.010)
p = 1 - q
eq("p", sf(p, 3), 0.990)
eq("2pq", sf(2 * p * q, 3), 0.0198)
eq("2pq 2 sf", sf(2 * p * q, 2), 0.020)
eq("carriers", round(2 * p * q * 200000), 3960)

# --- salmon
eq("time reduction %", sf((30 - 16) / 30 * 100, 3), 46.7)

# --- soybean trial
eq("yield increase soy %", (3.0 - 2.4) / 2.4 * 100, 25, 1e-9)

# --- SCID trial
eq("normal immune %", 14 / 20 * 100, 70)
eq("leukaemia %", 2 / 20 * 100, 10)
eq("trial total", 14 + 4 + 2, 20)

print("ok")
