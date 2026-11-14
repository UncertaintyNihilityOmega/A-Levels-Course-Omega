# data/cs.float_fig.py: the two SVG figures of cs.float, with label-box checks
import os
import sys
from fractions import Fraction as F
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cs_usertypes_figclass import Fig  # noqa: E402

# ---- Figure 1: the layout of a 12-bit number --------------------------------------------------
PATTERN = "010110000011"
SUP = {"1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷"}
f1 = Fig("layout", 342, 168)
f1.text("tl ti", 20, 16, "A 12-bit floating-point number")
f1.text("tl tc", 116, 40, "mantissa (8 bits)")
f1.text("tl tc", 274, 40, "exponent (4 bits)")
xs = [20 + 24 * i for i in range(8)] + [226 + 24 * i for i in range(4)]
mant_pv = ["−1"] + ["2⁻" + SUP[str(i)] for i in range(1, 8)]
exp_pv = ["−8", "4", "2", "1"]
for i, x in enumerate(xs):
    cls = "f1 s-acc sw2" if i in (0, 8) else "fm s-acc sw2"
    f1.rect(cls, x, 46, 24, 28)
    f1.text("tl tc tb", x + 12, 65, PATTERN[i])
    f1.text("tl tc", x + 12, 100, (mant_pv + exp_pv)[i])
f1.parts.append('<circle class="fi" cx="44" cy="82" r="2.5"/>')
f1.text("tl tc", 32, 122, "sign bit")
f1.text("tl tc", 238, 122, "sign bit")
f1.text("tl", 20, 144, "dot = binary point (after the sign bit)")
f1.text("tl", 20, 162, "0.1011000 × 2³ = 5.5")
print(f1.svg("A row of twelve bit boxes holding 0 1 0 1 1 0 0 0, then 0 0 1 1. The first eight are the mantissa with place values minus 1, then 2 to the minus 1 down to 2 to the minus 7; a dot after the first box marks the binary point. The last four are the exponent with place values minus 8, 4, 2 and 1. The first box of each part is the sign bit. The value is 0.1011000 times 2 cubed, which is 5.5.",
             "The pattern 01011000 0011 split into an 8-bit mantissa and a 4-bit exponent. Both are two's complement numbers: the sign bit has a negative place value. The mantissa is a fraction with the binary point after its sign bit."))

# ---- Figure 2: every positive normalised value of a 4-bit mantissa, 2-bit exponent format ----
vals = []
for E in range(-2, 2):
    for n in range(4, 8):          # mantissa 0.100 to 0.111 = n/8
        vals.append((F(n, 8) * F(2) ** E, E))
assert len(vals) == 16
f2 = Fig("numberline", 340, 128)
f2.text("tl ti", 20, 16, "All 16 positive normalised values")
f2.parts.append('<path class="ln-m thin" d="M 20 52 L 330 52"/>')
SC = 170
for v, E in vals:
    x = 20 + float(v) * SC
    f2.parts.append(f'<path class="c1 sw2" d="M {x:g} 38 L {x:g} 52"/>')
f2.parts.append('<path class="ln" d="M 20 34 L 20 52"/>')
for v, label in [(F(0), "0"), (F(1, 4), "0.25"), (F(1, 2), "0.5"), (F(1), "1"), (F(7, 4), "1.75")]:
    f2.text("tl tc", 20 + float(v) * SC, 72, label)
groups = {}
for v, E in vals:
    groups.setdefault(E, []).append(float(v))
for E, vs in groups.items():
    cx = 20 + (min(vs) + max(vs)) / 2 * SC
    f2.text("tl tc", round(cx), 96, "−" + str(-E) if E < 0 else str(E))
f2.text("tl tc", 170, 118, "exponent of each group of four ticks")
print(f2.svg("A number line from 0 to 1.75 with sixteen tick marks, the representable positive values. They fall in four groups of four, for exponents minus 2, minus 1, 0 and 1. The ticks are very close together near 0.125 and spread further apart in each group: the gaps are 0.03125, 0.0625, 0.125 and 0.25.",
             "Every positive normalised value of a format with a 4-bit mantissa and a 2-bit exponent. The gap between neighbours doubles whenever the exponent goes up by one, so large numbers are stored less precisely than small ones."))
print([(str(v), E) for v, E in vals])
