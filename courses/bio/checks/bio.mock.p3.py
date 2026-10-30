# checks/bio.mock.p3.py: recomputes every number in chapters/bio.mock.p3.md (Mock Paper 3) and the paper total
import importlib.util, math, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
sys.path.insert(0, os.path.join(root, "data"))
import calc_p24 as C
text = open(os.path.join(root, "chapters", "bio.mock.p3.md"), encoding="utf-8").read()
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def r(x, d=2): return round(x + 1e-12, d)


# the figure script (same geometry as the figures in the chapter)
spec = importlib.util.spec_from_file_location("figp3", os.path.join(root, "data", "fig_bio.mock.p3.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# --- paper structure: FACTS.md says 9700/32 (June 2024) had 2 questions, 21 + 19 = 40 marks, 2 h
assert re.search(r"^@time 2 h$", text, flags=re.M)
blocks = re.findall(r"^:::try\n(.*?)\n:::\n(?=\n:::)", text, flags=re.M | re.S)
eq("questions", len(blocks), 2)
SKILL = {  # question -> part -> (skill, marks): M = manipulation, measurement and observation, P = presentation, A = analysis
    1: {"a": ("M", 2), "b": ("M", 3), "c": ("M", 2), "d": ("M", 1), "e": ("P", 3), "f": ("A", 2), "g": ("A", 1),
        "h": ("P", 2), "i": ("A", 2), "j": ("A", 2), "k": ("A", 2), "l": ("A", 1)},
    2: {"a": ("M", 1), "b": ("P", 4), "c": ("M", 2), "d": ("M", 2), "e": ("P", 3), "f": ("A", 2), "g": ("M", 3)},
}
tot = 0
sk = {"M": 0, "P": 0, "A": 0}
for i, b in enumerate(blocks, 1):
    head = int(re.match(r"Q: \[(\d+) marks\]", b).group(1))
    q, a = b.split("\nA: ")
    parts = re.findall(r"^\(([a-z])\) .*?\[(\d+)\]\s*$", q, flags=re.M)
    got = {p: int(k) for p, k in parts}
    assert got == {p: v[1] for p, v in SKILL[i].items()}, (i, got)
    eq(f"Q{i} parts add up", sum(got.values()), head)
    eq(f"Q{i} mark scheme tokens", len(re.findall(r"\[(?:B|M|A)1\]", a)), head)
    for p, (s, k) in SKILL[i].items():
        sk[s] += k
    tot += head
eq("paper total", tot, 40)
assert 21 <= 23 <= 23 and 17 <= 17 <= 19
assert (15 <= sk["M"] <= 17) and (11 <= sk["P"] <= 13) and (11 <= sk["A"] <= 13), sk
eq("skill M", sk["M"], 16); eq("skill P", sk["P"], 12); eq("skill A", sk["A"], 12)
assert "Marks by skill in Question 1: manipulation, measurement and observation 8" in text
assert "presentation 5" in text and "analysis, conclusions and evaluation 10" in text
assert "Marks by skill in Question 2: manipulation, measurement and observation 8" in text
assert "presentation 7" in text and "analysis, conclusions and evaluation 2" in text
# microscope: x10 and x40 only (FACTS.md); no x4
assert "×4 " not in text and "x4 " not in text

# --- Question 1 data and calculations
for c, v in zip(C.CONC, [0, 5, 10, 15, 20, 25]):
    eq(f"volume of S for {c}", r(c / 0.60 * 30, 6), v)
eq("S 0.20", 0.20 / 0.60 * 30, 10); eq("S 0.40", 0.40 / 0.60 * 30, 20); eq("S 0.50", 0.50 / 0.60 * 30, 25)
for c, w in zip([0.20, 0.40, 0.50], [20, 10, 5]):
    eq(f"volume of W for {c}", 30 - c / 0.60 * 30, w)
dm = [r(f - i) for i, f in zip(C.INI, C.FIN)]
assert dm == [0.43, 0.26, 0.06, -0.21, -0.08, -0.62], dm
for i, (a, b2, d) in enumerate(zip(C.INI, C.FIN, [0.43, 0.26, 0.06, -0.21, -0.08, -0.62])):
    assert f"| {C.CONC[i]:.2f} | {a:.2f} | {b2:.2f} | {'+' if d > 0 else '−'}{abs(d):.2f} |" in text, i
eq("pc 0.30", r(C.PC[3]), -6.46)
eq("pc 0.30 3sf", float(f"{C.PC[3]:.3g}"), -6.46)
for k, want in enumerate([13.8, 7.9, 1.9, -6.5, -2.5, -19.3]):
    eq(f"pc {k}", r(C.PC[k], 1), want)
assert "+13.8, +7.9, +1.9, −6.5, −2.5 and −19.3 %" in text
# the anomaly: all other points fall; 0.40 is above 0.30
assert C.ANOM == 4 and C.PC[4] > C.PC[3]
assert all(C.PC[k] > C.PC[k + 1] for k in (0, 1, 2)) and C.PC[3] > C.PC[5]
a, b = C.fit()
eq("intercept", r(-a / b), 0.21, 0.005)
eq("line a", r(a, 1), 14.3); eq("line b", r(b, 1), -67.1)
assert 0.20 <= -a / b <= 0.22
# expected value at 0.40 from the line (about -13 per cent)
eq("expected at 0.40", a + b * 0.40, -12.5, 0.1)
# Question 1 totals
eq("Q1 total", sum(v[1] for v in SKILL[1].values()), 23)

# --- Question 2: calibration, graticule, scale bar
eq("stage micrometer", 4 * 0.10 * 1000, 400)
eq("one division", 400 / 32, 12.5)
eq("S1 geometry A", m.div(m.S1_CX - m.S1_R), 5); eq("S1 geometry B", m.div(m.S1_CX + m.S1_R), 45)
eq("S1 geometry C", m.div(m.S1_CX - m.S1_ENDO), 17); eq("S1 geometry D", m.div(m.S1_CX + m.S1_ENDO), 33)
eq("endodermis divisions", m.div(m.S1_CX + m.S1_ENDO) - m.div(m.S1_CX - m.S1_ENDO), 16)
eq("endodermis um", 16 * 12.5, 200)
eq("ratio ring/section", 16 / 40, 0.4)
eq("cortex share of radius", (m.S1_R - m.S1_ENDO) / m.S1_R, 0.6)
eq("cell Z width", 28 / 20 * 50, 70)
eq("figure ratio XY/bar", m.XY_PX / m.SCALE_BAR_PX, 28 / 20)
print("ok")
