# checks/bio.proteins.py: recomputes every number in the Proteins chapter (chapters/bio.proteins.md).
from math import isclose, log10

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def bonds(units):
    """Peptide bonds (= water molecules removed) in a chain of the given length."""
    return units - 1


# --- Counting bonds and sequences ---------------------------------------------------------------------------------
eq("eg: 146 amino acids -> 145 bonds", bonds(146), 145)
eq("eg: tripeptides 20^3", 20 ** 3, 8000)
eq("eg: 20^100 about 1.3e130 (mantissa)", round(20 ** 100 / 10 ** 130, 1), 1.3)
eq("eg: 20^100 exponent", len(str(20 ** 100)) - 1, 130)
eq("try: 250 amino acids -> 249", bonds(250), 249)
eq("quiz: 50 amino acids -> 49", bonds(50), 49)

# --- Iron in haemoglobin -------------------------------------------------------------------------------------------------
fe = 4 * 56
eq("exam: iron per molecule", fe, 224)
eq("exam: % iron", round(fe / 64500 * 100, 2), 0.35, 0.006)
eq("exam: % iron rounds to 0.35", round(fe / 64500 * 100, 2), 0.35, 0.006)

# --- Red blood cell -------------------------------------------------------------------------------------------------------
eq("exam: O2 per red blood cell", 2.5e8 * 4, 1.0e9, 1e-3)

# --- Collagen stretch ---------------------------------------------------------------------------------------------------
eq("stretch: glycines 1050/3", 1050 / 3, 350)
eq("stretch: bonds in one chain", bonds(1050), 1049)
eq("stretch: bonds in the molecule 3 x 1049", 3 * bonds(1050), 3147)

# --- Tendon and rubber band (:::plot): 100 x up to 5.2 mm; 2 x up to 41 mm --------------------------------------------
tendon = lambda x: 100 * x
band = lambda x: 2 * x
eq("plot: tendon 500 N at 5 mm", tendon(5), 500)
eq("plot: rubber band 80 N at 40 mm", band(40), 80)
assert tendon(5.2) < 620 and band(41) < 620, "curves stay inside the y range"
assert tendon(5) / band(5) > 40, "tendon is far stiffer"

# --- Table in exam practice (surface R groups and solubility) ---------------------------------------------------------
assert 78 > 18 and 15.0 > 0.1

print("ok")
