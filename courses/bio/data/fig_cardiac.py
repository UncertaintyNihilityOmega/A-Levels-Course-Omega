# data/fig_cardiac.py: the MODEL pressure traces (kPa) of one cardiac cycle at 75 beats per minute (0.8 s) behind
# chapters/bio.heart.md, widgets/bio-cardiac.js and the static pressure graph in fig_bio.heart.py.
# The widget holds the same key points (KEY) and the same monotone cubic (PCHIP) interpolation; data/test_bio-cardiac.js
# checks the JavaScript against data/cardiac_samples.json, which this script writes.
# Run: py data/fig_cardiac.py  -> prints the valve events and writes data/cardiac_samples.json
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")

T0 = 0.8                                   # cycle length in s at 75 beats per minute
# time (s) -> pressure (kPa); time 0 is the start of atrial systole
KEY = {
    "la": [(0.00, 0.90), (0.03, 1.30), (0.06, 1.55), (0.09, 1.30), (0.11, 0.95), (0.14, 0.80), (0.20, 0.85), (0.30, 1.05),
           (0.40, 1.25), (0.44, 1.18), (0.50, 0.80), (0.60, 0.60), (0.70, 0.70), (0.80, 0.90)],
    "lv": [(0.00, 0.55), (0.04, 0.70), (0.08, 0.85), (0.10, 0.95), (0.12, 2.20), (0.14, 5.20), (0.16, 9.00), (0.18, 12.00),
           (0.21, 14.90), (0.25, 16.20), (0.30, 16.00), (0.34, 15.70), (0.37, 15.10), (0.385, 13.80), (0.40, 9.00),
           (0.42, 3.50), (0.44, 1.40), (0.46, 0.80), (0.50, 0.45), (0.60, 0.40), (0.70, 0.45), (0.80, 0.55)],
    "ao": [(0.00, 10.80), (0.08, 10.62), (0.17, 10.50), (0.20, 11.80), (0.25, 15.30), (0.28, 15.80), (0.32, 15.45),
           (0.35, 15.05), (0.375, 14.65), (0.395, 14.25), (0.42, 14.60), (0.45, 14.20), (0.55, 12.70), (0.65, 11.60),
           (0.75, 10.95), (0.80, 10.80)],
}


def pchip(pts):
    """Monotone cubic Hermite interpolation (Fritsch-Carlson), end slopes 0. Returns a function of t."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    n = len(xs)
    d = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [0.0] * n
    for i in range(1, n - 1):
        if d[i - 1] * d[i] > 0:
            h0, h1 = xs[i] - xs[i - 1], xs[i + 1] - xs[i]
            w1, w2 = 2 * h1 + h0, h1 + 2 * h0
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    def f(t):
        t = min(max(t, xs[0]), xs[-1])
        lo, hi = 0, n - 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if xs[mid] <= t:
                lo = mid
            else:
                hi = mid - 1
        i = lo
        h = xs[i + 1] - xs[i]
        s = (t - xs[i]) / h
        h00, h10 = 2 * s**3 - 3 * s**2 + 1, s**3 - 2 * s**2 + s
        h01, h11 = -2 * s**3 + 3 * s**2, s**3 - s**2
        return h00 * ys[i] + h10 * h * m[i] + h01 * ys[i + 1] + h11 * h * m[i + 1]
    return f


LA, LV, AO = (pchip(KEY[k]) for k in ("la", "lv", "ao"))


def events(step=0.0005):
    """Valve events from the pressures alone: AV open iff LA > LV; semilunar open iff LV > AO."""
    ev = []
    n = int(round(T0 / step))
    prev_av, prev_sl = LA(0) > LV(0), LV(0) > AO(0)
    for k in range(1, n + 1):
        t = k * step
        av, sl = LA(t) > LV(t), LV(t) > AO(t)
        if av != prev_av:
            ev.append((round(t, 4), "AV valve opens" if av else "AV valve closes"))
        if sl != prev_sl:
            ev.append((round(t, 4), "semilunar valve opens" if sl else "semilunar valve closes"))
        prev_av, prev_sl = av, sl
    return ev


if __name__ == "__main__":
    ev = events()
    for t, s in ev:
        print(f"{t:.3f} s  {s}")
    assert [s for _, s in ev] == ["AV valve closes", "semilunar valve opens", "semilunar valve closes", "AV valve opens"], ev
    print("peaks: LV %.2f kPa, aorta %.2f kPa (min %.2f), LA %.2f kPa" % (
        max(LV(k / 1000) for k in range(801)), max(AO(k / 1000) for k in range(801)), min(AO(k / 1000) for k in range(801)),
        max(LA(k / 1000) for k in range(801))))
    samples = [{"t": round(k * 0.01, 2), "la": LA(k * 0.01), "lv": LV(k * 0.01), "ao": AO(k * 0.01)} for k in range(0, 81)]
    json.dump({"events": ev, "samples": samples}, open(os.path.join(os.path.dirname(__file__), "cardiac_samples.json"), "w"))
    print("wrote cardiac_samples.json")
