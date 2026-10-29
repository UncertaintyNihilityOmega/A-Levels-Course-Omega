# checks/bio.photosynthesis.py: recomputes every number in the Photosynthesis chapter (chapters/bio.photosynthesis.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


def dp(x, k):
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-k), ROUND_HALF_UP))


# --- Calvin cycle bookkeeping for 3 CO2 (figure, text, glucose example, practice) --------------------------------
RUBP_C, GP_C, TP_C = 5, 3, 3
co2 = 3
c_in = co2 * RUBP_C + co2 * 1
eq("carbon atoms after fixation of 3 CO2", c_in, 18)
gp = c_in // GP_C
eq("GP from 3 CO2", gp, 6)
eq("GP per CO2 fixed", gp / co2, 2)
tp = gp                                   # one TP per GP
eq("TP made", tp, 6)
eq("TP carbon atoms", tp * TP_C, 18)
tp_regen = 5
eq("TP used to regenerate RuBP (carbon atoms)", tp_regen * TP_C, 15)
rubp_regen = tp_regen * TP_C // RUBP_C
eq("RuBP regenerated", rubp_regen, 3)
tp_out = tp - tp_regen
eq("TP leaving per 3 CO2", tp_out, 1)
atp_reduction, nadp_reduction, atp_regen = gp * 1, gp * 1, rubp_regen * 1     # 1 ATP + 1 reduced NADP per GP; 1 ATP per RuBP
eq("ATP for reduction", atp_reduction, 6)
eq("reduced NADP for reduction", nadp_reduction, 6)
eq("ATP for regeneration", atp_regen, 3)
atp_total, nadp_total = atp_reduction + atp_regen, nadp_reduction
eq("ATP per 3 CO2", atp_total, 9)
eq("reduced NADP per 3 CO2", nadp_total, 6)
atp_per, nadp_per = atp_total / co2, nadp_total / co2
eq("ATP per CO2", atp_per, 3)
eq("reduced NADP per CO2", nadp_per, 2)
# glucose example: 6 CO2
eq("CO2 for glucose", 6, 6)
eq("glucose ATP", 6 * atp_per, 18)
eq("glucose reduced NADP", 6 * nadp_per, 12)
eq("TP leaving per glucose carbon atoms", 2 * TP_C, 6)
eq("TP leaving per glucose (6 CO2)", 6 / co2 * tp_out, 2)
# practice: 12 CO2 and 15 CO2
eq("12 CO2 ATP", 12 * atp_per, 36)
eq("12 CO2 reduced NADP", 12 * nadp_per, 24)
eq("15 CO2 GP", 15 * 2, 30)
eq("15 CO2 ATP", 15 * atp_per, 45)
eq("15 CO2 reduced NADP", 15 * nadp_per, 30)
eq("15 CO2 TP leaving", 15 / co2 * tp_out, 5)

# --- Rf worked example ------------------------------------------------------------------------------------------
front = 8.0
ref = {"carotene": 0.95, "xanthophyll": 0.71, "chlorophyll a": 0.65, "chlorophyll b": 0.45}
dist = [7.6, 5.7, 5.2, 3.6]
for d, (name, r) in zip(dist, ref.items()):
    eq(f"Rf {name}", dp(d / front, 2), r)
eq("Rf 5.2 / 8.0", dp(5.2 / 8.0, 2), 0.65)
eq("wrong-way division gives above 1", sf(8.0 / 5.2, 2), 1.5)
# figure: spot positions come from the reference Rf values (origin y=252, front y=44)
for r in ref.values():
    y = 252 - r * (252 - 44)
    assert 44 < y < 252

# --- Rf practice ----------------------------------------------------------------------------------------------------
eq("Rf 5.4 / 9.0", 5.4 / 9.0, 0.60, 1e-12)
ref_b = {"carotene": 0.88, "xanthophyll": 0.52, "chlorophyll a": 0.30, "chlorophyll b": 0.18}
eq("yellow leaf spot 1", dp(6.6 / 7.5, 2), ref_b["carotene"])
eq("yellow leaf spot 2", dp(3.9 / 7.5, 2), ref_b["xanthophyll"])
eq("quiz Rf 4.0 / 8.0", 4.0 / 8.0, 0.50)
eq("quiz wrong way", 8.0 / 4.0, 2.0)

# --- magnification practice -----------------------------------------------------------------------------------
A_mm = 48 / 8000
eq("chloroplast length mm", A_mm, 0.0060, 1e-12)
eq("chloroplast length um", A_mm * 1000, 6.0, 1e-9)

# --- spectra worked example table ----------------------------------------------------------------------------
wl = [400, 450, 500, 550, 600, 650, 700]
absorb = [68, 80, 12, 5, 20, 74, 10]
rate = [60, 80, 40, 22, 38, 68, 8]
eq("highest rate wavelength", wl[rate.index(max(rate))], 450)
eq("highest rate value", max(rate), 80)
eq("lowest rate in green is at 550", wl[rate.index(min(rate[:6]))], 550)
eq("rate at 550", rate[3], 22)
eq("rate at 650", rate[5], 68)
eq("rate at 700", rate[6], 8)
eq("chlorophyll a absorbs at 500", absorb[2], 12)
assert rate[2] > absorb[2]                           # rate at 500 higher than absorption suggests
# local maxima of rate: 450 and 650 only
peaks = [wl[i] for i in range(1, 6) if rate[i] > rate[i - 1] and rate[i] > rate[i + 1]]
assert peaks == [450, 650], peaks

# --- barley mutant table ---------------------------------------------------------------------------------------
w2 = [430, 460, 500, 550, 600, 640, 680]
normal = [80, 85, 30, 20, 36, 66, 90]
mutant = [72, 58, 25, 18, 32, 43, 88]
assert all(m < nn for m, nn in zip(mutant, normal))
diffs = [nn - m for nn, m in zip(normal, mutant)]
eq("largest difference at 460", w2[diffs.index(max(diffs))], 460)
eq("difference at 460", diffs[1], 27)
eq("difference at 640", diffs[5], 23)
assert sorted(diffs)[-2] == 23                       # 640 is the second largest
eq("680 nm normal", normal[6], 90)
eq("680 nm mutant", mutant[6], 88)
assert diffs[6] == min(diffs)                        # 680 nm: smallest difference... (2) ties with 550
assert diffs[3] == diffs[6]

# --- GP / RuBP after light off ----------------------------------------------------------------------------------
t = [0, 15, 30, 45, 60]
GP = [40, 62, 77, 85, 88]
RuBP = [20, 13, 8, 5, 3]
assert all(b > a for a, b in zip(GP, GP[1:]))
assert all(b < a for a, b in zip(RuBP, RuBP[1:]))
eq("GP at 0", GP[0], 40)
eq("GP at 60", GP[-1], 88)
eq("RuBP at 0", RuBP[0], 20)
eq("RuBP at 60", RuBP[-1], 3)

# --- figure geometry sanity: absorption/action spectra peaks sit where the text says -------------------------------
from math import exp


def G(x, mu, sd):
    return exp(-((x - mu) / sd) ** 2 / 2)


def chl_a(l): return 0.95 * G(l, 432, 17) + 0.72 * G(l, 664, 13) + 0.05 * G(l, 540, 60)
def chl_b(l): return 0.82 * G(l, 457, 17) + 0.46 * G(l, 642, 13) + 0.04 * G(l, 540, 60)
def caro(l): return 0.72 * G(l, 452, 17) + 0.62 * G(l, 482, 14) + 0.03 * G(l, 540, 60)
def act(l): return 0.55 * chl_a(l) + 0.4 * chl_b(l) + 0.3 * caro(l)


ls = range(400, 701)
a_peak = max(ls, key=chl_a)
assert 428 <= a_peak <= 436
red_a = max(range(600, 701), key=chl_a)
assert 655 <= red_a <= 675
blue_act = max(range(400, 520), key=act)
red_act = max(range(600, 701), key=act)
assert 425 <= blue_act <= 460 and 650 <= red_act <= 680, (blue_act, red_act)
green_low = min(range(500, 600), key=act)
assert act(green_low) < 0.2 * act(blue_act)

print("ok")
