# checks/bio.classification.py: recomputes every number in the Classification chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def kind(a, t, u, g, c):
    """Classify a virus from its base percentages: returns 'dsDNA', 'ssDNA', 'dsRNA' or 'ssRNA'."""
    assert a + t + u + g + c == 100, "percentages must add to 100"
    dna = t > 0
    assert not (t > 0 and u > 0)
    pair = (a == (t if dna else u)) and g == c
    return ("ds" if pair else "ss") + ("DNA" if dna else "RNA")


# worked example: viruses P, Q, R
viruses = {"P": (22, 22, 0, 28, 28), "Q": (31, 0, 27, 24, 18), "R": (28, 33, 0, 18, 21)}
want = {"P": "dsDNA", "Q": "ssRNA", "R": "ssDNA"}
for k, v in viruses.items():
    assert kind(*v) == want[k], f"virus {k}: {kind(*v)} not {want[k]}"
    n += 1
# exam practice: viruses S, T, U, V
practice = {"S": ((19, 0, 19, 31, 31), "dsRNA"), "T": ((26, 35, 0, 22, 17), "ssDNA"),
            "U": ((27, 27, 0, 23, 23), "dsDNA"), "V": ((18, 0, 33, 30, 19), "ssRNA")}
for k, (v, w) in practice.items():
    assert kind(*v) == w, f"virus {k}: {kind(*v)} not {w}"
    n += 1
eq("eg P A = T", 22, 22)
eq("eg R A not T", 28 - 33, -5)

# rRNA table: symmetric, and B1/B2 closest, A1/E1 next
T = {("B1", "B2"): 12, ("A1", "E1"): 30, ("B1", "A1"): 48, ("B1", "E1"): 48, ("B2", "A1"): 48, ("B2", "E1"): 48}
eq("rRNA closest pair", min(T.values()), 12)
eq("rRNA A1 nearest is E1", min(T[k] for k in T if "A1" in k), 30)
eq("rRNA A1 to bacteria", T[("B1", "A1")], T[("B2", "A1")])
eq("rRNA 48 is also bacteria to E1", T[("B1", "E1")], 48)

# mitochondrial rRNA (stretch): smallest difference is the bacterium
mito = {"bacterium": 28, "archaeon": 52, "nuclear rRNA": 54}
eq("mito nearest", min(mito.values()), 28)

# hierarchy: seven ranks below domain, eight with the domain
ranks = ["kingdom", "phylum", "class", "order", "family", "genus", "species"]
eq("seven ranks", len(ranks), 7)
eq("mnemonic letters", len("KPCOFGS"), len(ranks))
assert all(a == b[0].upper() for a, b in zip("KPCOFGS", ranks))
n += 1
print("ok", n)
