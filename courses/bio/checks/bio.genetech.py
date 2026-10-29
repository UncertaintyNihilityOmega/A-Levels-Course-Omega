# checks/bio.genetech.py: recomputes every number in the Tools of genetic technology chapter.
from math import isclose, log10

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


def frags_linear(length, cuts):
    pts = [0] + sorted(cuts) + [length]
    return [b - a for a, b in zip(pts, pts[1:])]


def frags_circular(length, cuts):
    c = sorted(cuts)
    out = [b - a for a, b in zip(c, c[1:])]
    out.append(length - c[-1] + c[0])
    return out


# --- gene v cDNA
gene = 150 + 210 + 90 + 800 + 1200
eq("gene length", gene, 2450)
eq("cDNA length", 150 + 210 + 90, 450)
eq("cDNA % of gene", sf(450 / gene * 100), 18.4)
eq("amino acids", (450 - 3) / 3, 149)

# --- PCR
eq("2^10", 2**10, 1024)
eq("250 x 2^8", 250 * 2**8, 64000)
eq("2^19", 2**19, 524288)
eq("2^20", 2**20, 1048576)
eq("2^30", 2**30, 1073741824)
eq("2^30 sf", sf(2**30 / 1e9, 3), 1.07)
eq("table 2^5", 2**5, 32)
eq("30 x 2^6", 30 * 2**6, 1920)
eq("2^7", 2**7, 128)
eq("2n mistake", 2 * 7, 14)
eq("n squared", 7**2, 49)
eq("2^6", 2**6, 64)
eq("2^13", 2**13, 8192)
eq("2^14", 2**14, 16384)
cyc = min(k for k in range(1, 40) if 2**k > 10000)
eq("cycles for >10000", cyc, 14)
cyc = min(k for k in range(1, 40) if 2**k > 1e6)
eq("cycles for >1e6", cyc, 20)

# --- restriction maps
f = frags_linear(5000, [1200, 3100])
eq("eg fragments", sorted(f), sorted([1200, 1900, 1900])) if False else None
assert sorted(f) == [1200, 1900, 1900], f
n += 1
assert sum(f) == 5000
f = frags_circular(4500, [500, 1500, 3200])
assert sorted(f) == [1000, 1700, 1800], f
n += 1
f1 = frags_linear(8000, [2500, 6000])
assert f1 == [2500, 3500, 2000], f1
f2 = frags_linear(8000, [5000])
assert f2 == [5000, 3000], f2
n += 2

# --- ladder example: distance to length
lad = {5000: 13, 3000: 20, 2000: 26, 1000: 36, 500: 46, 200: 59, 100: 69}
for L, d in lad.items():
    eq(f"ladder {L}", round(135 - 33 * log10(L)), d)
mid = (log10(2000) + log10(1000)) / 2
eq("log mid", sf(mid, 5), 3.1505)
eq("L mid", round(10**mid, -2), 1400)
eq("linear mid is 1500", (2000 + 1000) / 2, 1500)
eq("31 mm is halfway", (26 + 36) / 2, 31)
eq("log 2000", sf(log10(2000), 4), 3.301)

# --- practice ladder (each halving adds 10 mm)
eq("P", round(2000 * 2 ** (-0.4), -2), 1500)
eq("P exact", round(2000 * 2 ** (-0.4)), 1516)
eq("Q", round(500 * 2 ** (-0.5), -1), 350)
eq("Q exact", round(500 * 2 ** (-0.5)), 354)
eq("P fraction", (24 - 20) / 10, 0.4)
eq("Q fraction", (45 - 40) / 10, 0.5)

# --- stretch: plasmid
eq("recombinant length", 3600 + 1000, 4600)
eq("X to Y", 1900 - 400, 1500)
eq("rest", 4600 - 1000 - 1500, 2100)
eq("no insert second fragment", 3600 - 1500, 2100)
assert sorted(frags_circular(4600, [400, 1400, 2900])) == [1000, 1500, 2100]
n += 1

# --- figure gel positions use the model of bio-gel
for L in (5000, 3000, 2000, 1000, 500, 200, 100):
    y = 44 + 84 * (log10(6000) - log10(L))
    assert 40 < y < 222
n += 1

print("ok")
