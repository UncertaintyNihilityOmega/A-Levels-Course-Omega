# data/p47_axis_fig.py: builds and checks the "one axis" SVG for hist.f.eras (P47).
# Run: py data/p47_axis_fig.py  -> prints the SVG and writes data/p47_axis.svg.txt
W = 350
X0, X1 = 10, 318            # x for 1770 and 2000
Y0, Y1 = 1770, 2000
S = (X1 - X0) / (Y1 - Y0)
CH = 7.2                    # px per character of a 13 px label (safe)


def x(y):
    return round(X0 + (y - Y0) * S, 1)


eras = [(1774, 1850, "1", "1774–1849", "Age of revolutions"),
        (1850, 1914, "2", "1850–1914", "Nations, industry and empire"),
        (1914, 1929, "3", "1914–29", "World war and its aftermath"),
        (1929, 1945, "4", "1929–41", "Depression, dictatorship, war"),
        (1945, 1991, "5", "1945–91", "Cold War and decolonisation")]

groups = [
    ("AS European", "f1", [("France 1774–1814", 1774, 1814), ("Germany 1815–71", 1815, 1871), ("Russia 1881–1924", 1881, 1924)]),
    ("AS American", "f2", [("Civil War, Reconstruction 1820–77", 1820, 1877), ("Gilded Age 1870–1920", 1870, 1920), ("Crash, Depression 1920–41", 1920, 1941)]),
    ("AS International", "f3", [("Imperialism 1870–1918", 1870, 1918), ("International 1919–29", 1919, 1929), ("International 1929–39", 1929, 1939)]),
    ("Paper 3", "f1", [("Origins of WW1 1890–1914", 1890, 1914), ("Holocaust 1933–45", 1933, 1945), ("Cold War origins 1941–49", 1941, 1949)]),
    ("Paper 4 European", "f2", [("Italy 1919–41", 1919, 1941), ("Stalin's USSR 1924–41", 1924, 1941), ("Hitler's Germany 1929–41", 1929, 1941)]),
    ("Paper 4 American", "f3", [("USA 1945–61", 1945, 1961), ("USA 1961–74", 1961, 1974), ("USA 1974–93", 1974, 1993)]),
    ("Paper 4 International", "f1", [("Soviet Empire 1953–91", 1953, 1991), ("South Africa, Zimbabwe 1948–94", 1948, 1994), ("Malaysia, Indonesia 1909–67", 1909, 1967)]),
]

out = []
boxes = []   # (name, x0, y0, x1, y1) label boxes to test


def text(cls, xx, yy, s, anchor="s", name=None):
    n = len(s)
    w = n * CH
    if anchor == "m":
        bx0, bx1 = xx - w / 2, xx + w / 2
    elif anchor == "e":
        bx0, bx1 = xx - w, xx
    else:
        bx0, bx1 = xx, xx + w
    boxes.append((name or s, bx0, yy - 10, bx1, yy + 3))
    out.append(f'<text class="{cls}" x="{xx}" y="{yy}">{s}</text>')


# key
y = 16
for a, b, num, rng, name in eras:
    text("tl tb", 8, y, num, "s", "key" + num)
    text("tl", 24, y, f"{rng}  {name}", "s", "keytext" + num)
    y += 17
key_bottom = y
axis_y = key_bottom + 14
# tick labels (top)
ticks = [1800, 1850, 1900, 1950, 2000]
for t in ticks:
    text("ts tc", x(t), axis_y, str(t), "m", "tick" + str(t))
band_y = axis_y + 18
top = band_y + 6

# rows
rows = []
y = band_y + 20
for gname, cls, items in groups:
    rows.append(("h", gname, y))
    y += 20
    for lab, a, b in items:
        rows.append(("b", lab, y, a, b, cls))
        y += 30
chart_bottom = y - 10
bottom_tick_y = chart_bottom + 16
H = bottom_tick_y + 10

# era dividers (full height) and era numbers
for a, b, num, rng, name in eras:
    if a != 1774:
        out.append(f'<line class="ln-m thin dash" x1="{x(a)}" y1="{top}" x2="{x(a)}" y2="{chart_bottom}"/>')
last = eras[-1]
out.append(f'<line class="ln-m thin dash" x1="{x(1991)}" y1="{top}" x2="{x(1991)}" y2="{chart_bottom}"/>')
for a, b, num, rng, name in eras:
    mid = (x(a) + x(b)) / 2
    text("tl tb tc", round(mid, 1), band_y, num, "m", "era" + num)

# axis lines
out.append(f'<line class="ax" x1="{X0}" y1="{top}" x2="{X1}" y2="{top}"/>')
out.append(f'<line class="ax" x1="{X0}" y1="{chart_bottom}" x2="{X1}" y2="{chart_bottom}"/>')
for t in ticks:
    out.append(f'<line class="ax" x1="{x(t)}" y1="{top}" x2="{x(t)}" y2="{top + 5}"/>')
    out.append(f'<line class="ax" x1="{x(t)}" y1="{chart_bottom - 5}" x2="{x(t)}" y2="{chart_bottom}"/>')
for t in ticks:
    text("ts tc", x(t), bottom_tick_y, str(t), "m", "btick" + str(t))

bars = []
for r in rows:
    if r[0] == "h":
        text("tl tb", 8, r[2], r[1], "s", "hdr " + r[1])
    else:
        _, lab, yy, a, b, cls = r
        bx0, bx1 = x(a), x(b)
        w = len(lab) * CH
        if bx0 + w <= 338:
            text("tl halo", max(bx0, 4), yy, lab, "s", lab)
        else:
            text("tl te halo", bx1, yy, lab, "e", lab)
        out.append(f'<rect class="{cls} s-acc sw2" x="{bx0}" y="{yy + 7}" width="{round(bx1 - bx0, 1)}" height="8" rx="2"/>')
        bars.append((lab, bx0, yy + 7, bx1, yy + 15))

# checks
for n, a, b, c, d in boxes:
    assert a >= 2 and c <= W - 2, f"label '{n}' leaves the viewBox: {a:.0f}..{c:.0f}"
for i, (n1, a1, b1, c1, d1) in enumerate(boxes):
    for (n2, a2, b2, c2, d2) in boxes[i + 1:]:
        if n1.startswith("key") and n2.startswith("key"):
            continue
        if a1 < c2 + 4 and a2 < c1 + 4 and b1 < d2 + 4 and b2 < d1 + 4:
            raise AssertionError(f"labels overlap: {n1} / {n2}")
for (n, a, b, c, d) in boxes:
    for (bn, ba, bb, bc, bd) in bars:
        if a < bc + 3 and ba < c + 3 and b < bd + 3 and bb < d + 3:
            raise AssertionError(f"label {n} too close to bar {bn}")
# every bar inside the axis
for lab, a, b, c, d in bars:
    assert a >= X0 and c <= X1, lab

aria = ("Chart of the course's topics on one time axis from 1770 to 2000, in five eras: 1, 1774 to 1849, the age of revolutions; "
        "2, 1850 to 1914, nations, industry and empire; 3, 1914 to 1929, world war and its aftermath; 4, 1929 to 1945, depression, dictatorship "
        "and the road to war; 5, 1945 to 1991, the Cold War and decolonisation. One bar per topic, grouped by paper and option. "
        "AS European: France 1774 to 1814, Germany 1815 to 1871, Russia 1881 to 1924. AS American: Civil War and Reconstruction 1820 to 1877, "
        "Gilded Age 1870 to 1920, Crash and Depression 1920 to 1941. AS International: imperialism 1870 to 1918, international relations 1919 to 1929 "
        "and 1929 to 1939. Paper 3: origins of the First World War 1890 to 1914, the Holocaust 1933 to 1945, origins of the Cold War 1941 to 1949. "
        "Paper 4 European: Italy 1919 to 1941, Stalin's USSR 1924 to 1941, Hitler's Germany 1929 to 1941. Paper 4 American: the USA 1945 to 1961, 1961 to 1974, "
        "1974 to 1993. Paper 4 International: the Soviet empire 1953 to 1991, South Africa and Zimbabwe 1948 to 1994, Malaysia and Indonesia 1909 to 1967.")
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">' + "".join(out) + "</svg>"
open("data/p47_axis.svg.txt", "w", encoding="utf-8").write(svg)
print("height", H, "chars", len(svg), "labels", len(boxes), "ok")
