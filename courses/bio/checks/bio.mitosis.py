# checks/bio.mitosis.py: recomputes every number in the mitosis chapter (chapters/bio.mitosis.md).
from math import exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- Counting rule: human body cell (46) and the fruit fly example (8) -----------------------------------
def counts(c):
    """chromosomes, chromatids and DNA molecules at each stage for a cell with c chromosomes in G1."""
    return {
        "G1": (c, 0, c),
        "G2": (c, 2 * c, 2 * c),
        "metaphase": (c, 2 * c, 2 * c),
        "anaphase": (2 * c, 0, 2 * c),
        "daughter": (c, 0, c),
    }


h = counts(46)
eq("human G2 chromatids", h["G2"][1], 92)
eq("human anaphase chromosomes", h["anaphase"][0], 92)
eq("human daughter chromosomes", h["daughter"][0], 46)
fly = counts(8)
eq("fly G2 chromatids", fly["G2"][1], 16)
eq("fly anaphase chromosomes", fly["anaphase"][0], 16)
eq("fly daughter chromosomes", fly["daughter"][2], 8)
eq("try: 12 chromosomes G2 chromatids", counts(12)["G2"][1], 24)
eq("try: 12 chromosomes anaphase chromosomes", counts(12)["anaphase"][0], 24)
eq("exam: pea 14 chromosomes metaphase", counts(14)["metaphase"][0], 14)
eq("exam: pea 14 chromosomes chromatids", counts(14)["metaphase"][1], 28)

# --- Warm-up and practice magnifications --------------------------------------------------------------------
eq("warm-up magnification", 80 * 1000 / 40, 2000)
eq("try magnification", 60 * 1000 / 24, 2500)

# --- DNA content plot (the formula in the :::plot) and the worked example -------------------------------------------
def dna(x):
    s = (abs((x - 8) / 6) - abs((x - 8) / 6 - 1) + 1) / 2
    return 2 + 2 * s - 2 / (1 + exp(0 - (x - 19.5) * 8))


for x in (0, 4, 8):
    eq(f"DNA content {x} h (G1)", dna(x), 2, 1e-6)
eq("DNA content at 11 h (halfway through S)", dna(11), 3, 1e-6)
for x in (14, 16, 18.5):
    eq(f"DNA content {x} h (after S, before division)", dna(x), 4, 1e-2)
eq("DNA content after division", dna(22), 2, 1e-3)
eq("S phase doubles the DNA", dna(14) / dna(8), 2, 1e-6)

# --- Mitotic index worked example -----------------------------------------------------------------------------
cnt = {"prophase": 52, "metaphase": 12, "anaphase": 7, "telophase": 19, "interphase": 410}
total = sum(cnt.values())
eq("cells counted", total, 500)
mito = total - cnt["interphase"]
eq("cells in mitosis", mito, 90)
eq("mitotic index", mito / total, 0.18)
cycle = 20
tm = {k: cnt[k] / total * cycle for k in ("prophase", "metaphase", "anaphase", "telophase")}
eq("prophase h", tm["prophase"], 2.08)
eq("metaphase h", tm["metaphase"], 0.48)
eq("anaphase h", tm["anaphase"], 0.28)
eq("telophase h", tm["telophase"], 0.76)
eq("anaphase about 17 min", round(tm["anaphase"] * 60), 17)
eq("prophase about 2 h", round(tm["prophase"]), 2)
eq("all of mitosis h", 0.18 * cycle, 3.6)
eq("interphase h", cycle - 0.18 * cycle, 16.4)
eq("sum of stage times = mitosis", sum(tm.values()), 3.6)

# --- Practice -----------------------------------------------------------------------------------------------------
eq("try: 20 in 250 cells", 20 / 250, 0.08)
eq("try: metaphase 5% of 18 h in min", 0.05 * 18 * 60, 54)
root = {"interphase": 78, "prophase": 11, "metaphase": 4, "anaphase": 3, "telophase": 4}
eq("exam: root percentages add to 100", sum(root.values()), 100)
eq("exam: mitotic index of root", (100 - root["interphase"]) / 100, 0.22)
eq("exam: 11 + 4 + 3 + 4", 11 + 4 + 3 + 4, 22)
eq("exam: prophase time", sf(0.11 * 24, 2), 2.6)
eq("exam: prophase time unrounded", 0.11 * 24, 2.64)
eq("exam: normal tissue mitotic index", 24 / 800, 0.03)
eq("exam: tumour mitotic index", sf(143 / 650, 2), 0.22)

tel = [(0, 10.0), (10, 9.2), (20, 8.4), (30, 7.6), (40, 6.8), (50, 6.0)]
per10 = [round(a[1] - b[1], 9) for a, b in zip(tel, tel[1:])]
eq("telomere loss per 10 divisions is constant", len(set(per10)), 1)
loss = (tel[0][1] - tel[1][1]) / 10
eq("telomere loss per division, kb", loss, 0.08)
eq("telomere loss per division, bases", loss * 1000, 80)
eq("telomere divisions to 4.8 kb", (10.0 - 4.8) / loss, 65, 1e-6)

dnat = [(0, 3.0), (6, 3.0), (10, 3.0), (12, 4.0), (14, 5.0), (16, 6.0), (22, 6.0), (24, 3.0)]
eq("exam: S phase starts at 10 h", dnat[2][0], 10)
eq("exam: S phase ends at 16 h", dnat[5][0], 16)
eq("exam: S phase length", dnat[5][0] - dnat[2][0], 6)
eq("exam: DNA rises 1 unit per 2 h in S", (dnat[5][1] - dnat[2][1]) / (dnat[5][0] - dnat[2][0]), 0.5)
eq("exam: DNA doubles", dnat[5][1] / dnat[2][1], 2)
eq("exam: DNA halves", dnat[7][1] / dnat[6][1], 0.5)

ctrl = {"interphase": 86, "prophase": 7, "metaphase": 3, "anaphase": 2, "telophase": 2}
treat = {"interphase": 96, "prophase": 1, "metaphase": 1, "anaphase": 1, "telophase": 1}   # X-ray question (REVIEW P6/P8/P9)
eq("exam: control percentages add to 100", sum(ctrl.values()), 100)
eq("exam: treated percentages add to 100", sum(treat.values()), 100)
eq("exam: control mitotic index", (100 - ctrl["interphase"]) / 100, 0.14)
eq("exam: treated mitotic index", (100 - treat["interphase"]) / 100, 0.04)
eq("exam: 7 + 3 + 2 + 2", 7 + 3 + 2 + 2, 14)
eq("exam: 1 + 1 + 1 + 1", 1 + 1 + 1 + 1, 4)

yeast = {"normal": (56, 21, 23), "P": (91, 4, 5), "Q": (6, 5, 89)}
for k, v in yeast.items():
    eq(f"stretch: yeast {k} adds to 100", sum(v), 100)

# stretch: drug stops cytokinesis; 46 chromosomes, G1 DNA = 1 unit
eq("stretch: DNA after one S phase, no cytokinesis", 1 * 2, 2)
eq("stretch: DNA after second S phase", 2 * 2, 4)
eq("stretch: chromatids in G2 of second cycle", 2 * 46 * 2, 184)

# --- Quiz ---------------------------------------------------------------------------------------------------------
eq("quiz: mitotic index 27/180", 27 / 180, 0.15)
eq("quiz: wrong option divides by interphase cells", sf(27 / (180 - 27), 2), 0.18)
eq("quiz: wrong option 180/27", sf(180 / 27, 2), 6.7)
eq("quiz: wrong option 1 - 0.15", 1 - 27 / 180, 0.85)
eq("quiz: interphase cells", 180 - 27, 153)
eq("quiz: 27 / 153", sf(27 / 153, 3), 0.176)

print("ok")
