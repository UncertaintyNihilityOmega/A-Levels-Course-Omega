# data/fig_bio.mock.p5.py: bar chart with standard-error bars for chapters/bio.mock.p5.md (Mock Paper 5, Question 2).
# Run: py data/fig_bio.mock.p5.py -> clearance report. data/place_figs_p24.py pastes it into the chapter.
import math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib_p19 import Fig

sys.stdout.reconfigure(encoding="utf-8")
N = 12
MEANS = [41.2, 43.0, 47.9]
SDS = [5.8, 6.4, 6.5]
NAMES = ["control", "1.0% extract", "2.0% extract"]
SES = [s / math.sqrt(N) for s in SDS]


def figure(problems):
    f = Fig("bars")
    X0, X1, Y0, Y1 = 58, 322, 28, 220
    fy = lambda v: Y1 - v / 60 * (Y1 - Y0)
    for v in range(0, 61, 10):
        f.line([(X0, round(fy(v), 1)), (X1, round(fy(v), 1))], "gr", check=False)
        f.text(X0 - 6, round(fy(v), 1) + 3, str(v), "ts", "end")
    f.line([(X0, Y0), (X0, Y1)], "ax", check=False)
    f.line([(X0, Y1), (X1, Y1)], "ax", check=False)
    for k, (m, se, nm) in enumerate(zip(MEANS, SES, NAMES)):
        cx = X0 + 44 + k * 88
        f.parts.append(f'<rect class="f1 s-acc sw2" x="{cx - 26}" y="{fy(m):.1f}" width="52" height="{Y1 - fy(m):.1f}"/>')
        top, bot = round(fy(m + se), 1), round(fy(m - se), 1)
        f.line([(cx, top), (cx, bot)], "ln sw2", check=False)
        f.line([(cx - 7, top), (cx + 7, top)], "ln sw2", check=False)
        f.line([(cx - 7, bot), (cx + 7, bot)], "ln sw2", check=False)
        f.text(cx, Y1 + 16, nm, "tl", "middle")
    f.text(10, 16, "mean dry mass / mg", "tl")
    f.vb = (340, 252)
    label = ("Bar chart of the mean dry mass in milligrams of lettuce seedlings after 21 days. Control about 41, "
             "1.0 per cent extract about 43, 2.0 per cent extract about 48. Each bar has an error bar showing plus and "
             "minus one standard error; the bars of the control and the 1.0 per cent extract overlap, and the bar of "
             "the 2.0 per cent extract does not overlap the control.")
    cap = "Fig. 2.1 Mean dry mass of lettuce seedlings (n = 12 in each group). Error bars show ±1 standard error."
    problems += f.check()
    return f.svg((340, 252), label, cap)


def figures():
    problems = []
    return {"bars": figure(problems)}, problems


if __name__ == "__main__":
    figs, problems = figures()
    print("\n".join(problems) or "clearance ok")
    for m, se in zip(MEANS, SES):
        print(round(m - se, 2), round(m + se, 2))
