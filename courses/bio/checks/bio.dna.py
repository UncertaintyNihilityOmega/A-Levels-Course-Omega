# checks/bio.dna.py: recomputes every number and sequence in the DNA chapter (chapters/bio.dna.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def same(label, got, want):
    global n
    n += 1
    assert got == want, f"{label}: computed {got!r}, chapter says {want!r}"


PAIR = {"A": "T", "T": "A", "C": "G", "G": "C"}


def comp(s):
    """complementary strand written under s (ends reversed): returns the bases left to right under s."""
    return "".join(PAIR[b] for b in s)


def hbonds(strand):
    """hydrogen bonds between a strand and its complement."""
    return sum(2 if b in "AT" else 3 for b in strand)


# --- polynucleotides ---------------------------------------------------------------------------------------------
eq("25 nucleotides -> 24 bonds", 25 - 1, 24)
eq("3 nucleotides -> 2 bonds", 3 - 1, 2)
eq("try: 40 nucleotides -> 39", 40 - 1, 39)

# --- complementary strands and the 5'/3' labels -------------------------------------------------------------------
same("GATTACA complement", comp("GATTACA"), "CTAATGT")
same("GATTACA complement read 5' to 3'", comp("GATTACA")[::-1], "TGTAATC")
same("try: TACGGT complement", comp("TACGGT"), "ATGCCA")
same("exam: ATGCGATTCGCA complement", comp("ATGCGATTCGCA"), "TACGCTAAGCGT")
s = "ATGCGATTCGCA"
eq("exam: A or T in the strand", sum(b in "AT" for b in s), 6)
eq("exam: C or G in the strand", sum(b in "CG" for b in s), 6)
eq("exam: hydrogen bonds", hbonds(s), 30)
eq("exam: 6 x 2 + 6 x 3", 6 * 2 + 6 * 3, 30)

# --- base ratios -------------------------------------------------------------------------------------------------
for sp, (a, t, g, c) in {"X": (31, 31, 19, 19), "Y": (22, 22, 28, 28)}.items():
    eq(f"species {sp} adds to 100", a + t + g + c, 100)
    eq(f"species {sp} A = T", a, t)
    eq(f"species {sp} G = C", g, c)
    eq(f"species {sp} purines = 50", a + g, 50)
eq("X: A + T", 31 + 31, 62)
eq("X: G + C", 19 + 19, 38)
eq("Y: A + T", 22 + 22, 44)
eq("Y: G + C", 28 + 28, 56)

total = 4000
A = 0.28 * total
eq("eg: A", A, 1120)
eq("eg: G + C", total - 2 * A, 1760)
eq("eg: G = C", (total - 2 * A) / 2, 880)
eq("eg: base pairs", total / 2, 2000)
eq("eg: A-T pairs + C-G pairs = pairs", A + 880, 2000)
eq("eg: 1120 x 2", 1120 * 2, 2240)
eq("eg: 880 x 3", 880 * 3, 2640)
eq("eg: hydrogen bonds", 2240 + 2640, 4880)

eq("try: 12 A-T and 7 C-G pairs", 12 * 2 + 7 * 3, 45)
eq("try: 30% G -> A", (100 - 2 * 30) / 2, 20)
eq("quiz: 18% T -> G", (100 - 2 * 18) / 2, 32)
eq("quiz: C + G", 100 - 2 * 18, 64)

# --- exam: bacterium and virus table --------------------------------------------------------------------------------
eq("bacterium adds to 100", 20 + 20 + 30 + 30, 100)
eq("virus adds to 100", 26 + 33 + 22 + 19, 100)
eq("virus purines", 26 + 22, 48)
eq("virus pyrimidines", 33 + 19, 52)

# --- lagging strand fragments -------------------------------------------------------------------------------------
eq("try: fragments", 1200 / 150, 8)
eq("try: joins", 1200 / 150 - 1, 7)

# --- Meselson-Stahl ----------------------------------------------------------------------------------------------
def band_intermediate(gens):
    """% of DNA molecules that still hold one original strand (intermediate density) after gens generations."""
    return 100 * 2 / 2 ** gens if gens >= 1 else 0.0


tbl = {0: (100, 0, 0), 1: (0, 100, 0), 2: (0, 50, 50), 3: (0, 25, 75)}
for g, row in tbl.items():
    eq(f"eg table row {g} adds to 100", sum(row), 100)
    if g >= 1:
        eq(f"eg table row {g} intermediate", row[1], band_intermediate(g))
        eq(f"eg table row {g} light", row[2], 100 - band_intermediate(g))
eq("eg: gen 4 intermediate", band_intermediate(4), 12.5)
eq("eg: gen 4 light", 100 - band_intermediate(4), 87.5)
eq("eg: 2^4", 2 ** 4, 16)
eq("eg: 2/16", 2 / 16, 0.125)
eq("try: 2^3 molecules", 2 ** 3, 8)
eq("try: molecules with an original strand after any replication", 2, 2)
eq("exam: conservative after one generation, heavy %", 100 * 1 / 2, 50)
eq("exam: conservative after four generations, molecules", 2 ** 4, 16)
eq("exam: conservative after four generations, heavy %", 100 * 1 / 16, 6.25)
eq("exam: conservative after four generations, light %", 100 - 100 * 1 / 16, 93.75)

# --- stretch: hot spring and soil bacteria -------------------------------------------------------------------------
eq("hot spring A", (100 - 68) / 2, 16)
eq("soil A", (100 - 38) / 2, 31)
eq("hot spring: 68 CG pairs and 32 AT pairs", 68 + 32, 100)
eq("hot spring: 68 x 3", 68 * 3, 204)
eq("hot spring: 32 x 2", 32 * 2, 64)
eq("hot spring hydrogen bonds per 100 bp", 68 * 3 + 32 * 2, 268)

print("ok")
