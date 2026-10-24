# checks/chem.exam.p1.py: recomputes every number in the Paper 1 survival guide.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0, Ca 40.1.
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

# timing
per_q = 75 / 40
eq("minutes per question", per_q, 1.875)
eq("seconds part", round((per_q - 1) * 60), 52.5, 0.5)

# W1: H2SO4 + 2NaOH
n_naoh = 0.0250 * 0.200
eq("n NaOH", n_naoh, 5.00e-3)
n_h2so4 = n_naoh / 2
V = n_h2so4 / 0.125 * 1000
eq("V acid cm3", V, 20.0)
eq("ignore ratio", n_naoh / 0.125 * 1000, 40.0)
eq("multiply by 2", n_naoh * 2 / 0.125 * 1000, 80.0)
eq("halve twice", n_naoh / 4 / 0.125 * 1000, 10.0)

# W3: CH4 + 2O2 -> CO2 + 2H2O (Data booklet: C-H 410, O=O 496, C=O in CO2 805, O-H 460, C=O 740)
broken = 4 * 410 + 2 * 496
made = 2 * 805 + 4 * 460
eq("broken", broken, 2632)
eq("made", made, 3450)
eq("dH", broken - made, -818)
eq("one O=O only", 4 * 410 + 496 - made, -1314)
eq("average C=O", broken - (2 * 740 + 4 * 460), -688)
eq("wrong sign", made - broken, 818)

# W6: C4H9Br structural isomers: n-butyl (2 positions) + isobutyl skeleton (2 positions)
isomers = ["1-bromobutane", "2-bromobutane", "1-bromo-2-methylpropane", "2-bromo-2-methylpropane"]
eq("isomer count", len(isomers), 4)

# W8: successive IEs Al (Data booklet): large jump after third
ie = [577, 1820, 2740, 11600]
ratios = [ie[i + 1] / ie[i] for i in range(3)]
assert ratios[2] > 4 and ratios[0] < 4 and ratios[1] < 2
eq("jump after 3rd", ratios[2], 11600 / 2740)

# quiz
n = 5.0 / (40.1 + 12.0 + 3 * 16.0)
eq("mol CaCO3", round(n, 4), 0.0500, 5e-5)
eq("n in 25.0 cm3 of 0.100", 0.0250 * 0.100, 2.50e-3)
eq("no unit conversion", 25.0 * 0.100, 2.50)
print("ok")
