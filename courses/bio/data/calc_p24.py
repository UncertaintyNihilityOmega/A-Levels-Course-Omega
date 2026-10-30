# data/calc_p24.py: the data of Mock Papers 3 and 5 (P24) in one place. Imported by the figure scripts and the checks.
import math

# ---- Mock Paper 3, Question 1: carrot cylinders in sodium chloride solution --------------------------------
CONC = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50]          # mol dm-3
INI = [3.12, 3.28, 3.15, 3.25, 3.20, 3.22]           # g, mass of three cylinders before
FIN = [3.55, 3.54, 3.21, 3.04, 3.12, 2.60]           # g, after 40 minutes
ANOM = 4                                              # index of the anomalous result (0.40)
PC = [(f - i) / i * 100 for i, f in zip(INI, FIN)]    # percentage change


def fit():
    xs = [c for k, c in enumerate(CONC) if k != ANOM]
    ys = [p for k, p in enumerate(PC) if k != ANOM]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


if __name__ == "__main__":
    print([round(x, 2) for x in PC], [round(f - i, 2) for i, f in zip(INI, FIN)])
    a, b = fit()
    print("fit", a, b, "intercept", -a / b)
    print(5.8 ** 2 / 12, 6.5 ** 2 / 12, (47.9 - 41.2) / 41.2 * 100)
    s = 5.8 ** 2 / 12 + 6.5 ** 2 / 12
    print(s, math.sqrt(s), 6.7 / math.sqrt(s))
    print([round(v / math.sqrt(12), 3) for v in (5.8, 6.4, 6.5)])
    print((0.88 - 0.31) / 0.88 * 100)
