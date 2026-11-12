# data/p47_regimes_fig.py: builds and checks the three-regime timeline SVG for hist.d.compare (P47).
# Vertical time axis 1917-1945, three columns (Italy, USSR, Germany). Labels are pushed down where they would overlap.
W = 350
CH = 7.2
LINE = 16           # px between the lines of a two-line label
PX = 20             # px per year
T0 = 1917.0
Y0 = 60


def ty(t):
    return round(Y0 + (t - T0) * PX, 1)


cols = [
    ("Italy", 46, "f1", [
        (1922.82, ["March on", "Rome"]),
        (1924.45, ["Matteotti", "murdered"]),
        (1926.9, ["Parties", "banned"]),
        (1929.12, ["Lateran", "Treaties"]),
        (1935.75, ["Abyssinia", "invaded"]),
        (1938.9, ["Racial", "laws"]),
        (1940.45, ["Enters war"]),
        (1943.57, ["Mussolini", "falls"]),
    ]),
    ("USSR", 148, "f2", [
        (1917.82, ["Bolsheviks", "seize power"]),
        (1924.05, ["Lenin dies"]),
        (1928.8, ["First Five", "Year Plan"]),
        (1929.95, ["Great Turn"]),
        (1932.7, ["Famine"]),
        (1934.92, ["Kirov", "murdered"]),
        (1937.5, ["Great Terror"]),
        (1939.64, ["Nazi–Soviet", "Pact"]),
        (1941.47, ["German", "invasion"]),
    ]),
    ("Germany", 250, "f3", [
        (1923.85, ["Beer Hall", "Putsch"]),
        (1929.82, ["Slump", "begins"]),
        (1933.15, ["Chancellor,", "Enabling Act"]),
        (1934.5, ["Long Knives"]),
        (1935.7, ["Nuremberg", "Laws"]),
        (1936.8, ["Four-Year", "Plan"]),
        (1938.2, ["Anschluss"]),
        (1939.67, ["Invasion of", "Poland"]),
        (1941.47, ["Barbarossa"]),
        (1945.33, ["Hitler dies"]),
    ]),
]

out = []
boxes = []
dots = []
head_y = 24
for name, cx, cls, evs in cols:
    out.append(f'<text class="tl tb" x="{cx - 4}" y="{head_y}">{name}</text>')
    boxes.append((name, cx - 4, head_y - 10, cx - 4 + len(name) * CH, head_y + 3))
end_y = ty(1945.5)
for name, cx, cls, evs in cols:
    out.append(f'<line class="ln-m thin" x1="{cx}" y1="{ty(1917)}" x2="{cx}" y2="{end_y}"/>')
for name, cx, cls, evs in cols:
    last_bottom = -999
    for t, lines in evs:
        yd = ty(t)
        h = (len(lines) - 1) * LINE
        # first baseline so that the label block is centred on the dot
        base = yd - h / 2 + 4
        if base - 10 < last_bottom + 4:
            base = last_bottom + 4 + 10
        last_bottom = base + h + 3
        drift = base - (yd - h / 2 + 4)
        assert drift <= 34, f"{name} {lines}: label pushed {drift:.0f}px"
        lx = cx + 9
        if abs(drift) > 5:
            out.append(f'<line class="ln-m thin" x1="{cx}" y1="{yd}" x2="{lx - 2}" y2="{round(base - 4 - (0 if len(lines) == 1 else 0), 1)}"/>')
        out.append(f'<circle class="{cls} s-acc sw2" cx="{cx}" cy="{yd}" r="3.5"/>')
        dots.append((f"{name} dot {lines}", cx - 4, yd - 4, cx + 4, yd + 4))
        for i, s in enumerate(lines):
            by = round(base + i * LINE, 1)
            out.append(f'<text class="tl halo" x="{lx}" y="{by}">{s}</text>')
            w = len(s) * CH
            boxes.append((f"{name}: {s}", lx, by - 10, lx + w, by + 3))
# left axis
for yr in range(1920, 1946, 5):
    yy = ty(yr)
    out.append(f'<line class="ax" x1="33" y1="{yy}" x2="38" y2="{yy}"/>')
    out.append(f'<text class="ts te" x="30" y="{yy + 4}">{yr}</text>')
    boxes.append((f"axis {yr}", 30 - 4 * 6.2, yy - 6, 30, yy + 4))
out.append(f'<line class="ax" x1="38" y1="{ty(1917)}" x2="38" y2="{end_y}"/>')
H = int(end_y + 22)

for n, a, b, c, d in boxes:
    assert a >= 1 and c <= W - 2, f"{n} leaves the viewBox: {a:.0f}..{c:.0f}"
for i, (n1, a1, b1, c1, d1) in enumerate(boxes):
    for (n2, a2, b2, c2, d2) in boxes[i + 1:]:
        if a1 < c2 + 3 and a2 < c1 + 3 and b1 < d2 + 3 and b2 < d1 + 3:
            raise AssertionError(f"overlap: {n1} / {n2}")
# columns: label boxes must not cross the next column's vertical line or dot
xs = [c[1] for c in cols]
for n, a, b, c, d in boxes:
    for x in xs:
        if a < x < c and not n.startswith(("Italy", "USSR", "Germany")) :
            pass
for name, cx, cls, evs in cols:
    own = [b for b in boxes if b[0].startswith(name + ":")]
    for n, a, b, c, d in own:
        for x in xs:
            if x != cx:
                assert not (a - 3 < x < c + 3), f"{n} touches column line at {x}"

aria = ("Timeline of the three dictatorships from 1917 to 1945, with the years running down the page and one column each for Italy, "
        "the USSR and Germany. Italy: the March on Rome, October 1922; Matteotti murdered, 1924; opposition parties banned, 1926; Lateran Pacts, 1929; "
        "invasion of Abyssinia, 1935; racial laws, 1938; entry into the war, 1940; Mussolini falls, 1943. "
        "USSR: Bolsheviks seize power, October 1917; Lenin dies, 1924; first Five Year Plan, 1928; Great Turn, 1929; famine, 1932 to 1933; Kirov murdered, 1934; "
        "Great Terror, 1937 to 1938; Nazi-Soviet Pact, 1939; German invasion, 1941. "
        "Germany: Beer Hall Putsch, 1923; the slump begins, 1929; Hitler appointed Chancellor, January 1933, and the Enabling Act, March 1933; Night of the Long Knives, 1934; "
        "Nuremberg Laws, 1935; Four Year Plan, 1936; Anschluss, 1938; invasion of Poland, 1939; Barbarossa, 1941; Hitler dies, 1945.")
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">' + "".join(out) + "</svg>"
open("data/p47_regimes.svg.txt", "w", encoding="utf-8").write(svg)
print("height", H, "chars", len(svg), "labels", len(boxes), "ok")
