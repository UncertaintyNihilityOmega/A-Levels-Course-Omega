# data/cs.media_fig.py: generates the two hand SVG figures of cs.media (waveform sampling, RLE pixel grid)
# and checks label boxes against lines. Run: py data/cs.media_fig.py
import math

# ---- Figure 1: sampling a wave ----------------------------------------------------------------
X0, X1 = 36, 316                  # plot x range for t = 0 .. 12
YTOP, YBOT = 30, 150              # y of level 7 and level 0
N = 12
levels = []
for t in range(N):
    value = math.sin(2 * math.pi * t / N)
    levels.append(round((value + 1) / 2 * 7))
print("levels", levels)


def x(t):
    return X0 + (X1 - X0) * t / N


def y(level):
    return YBOT - (YBOT - YTOP) * level / 7


def ya(v):
    return y((v + 1) / 2 * 7)


pts = " ".join(f"{x(t / 4):.1f},{ya(math.sin(2 * math.pi * t / 4 / N)):.1f}" for t in range(4 * N + 1))
svg = ['<figure class="fig small"><svg viewBox="0 0 340 222" role="img" aria-label="PLACEHOLDER">']
svg.append(f'<line class="ax" x1="{X0}" y1="22" x2="{X0}" y2="160"/>')
svg.append(f'<line class="ax" x1="{X0}" y1="160" x2="{X1 + 8}" y2="160"/>')
svg.append(f'<text class="tl tc" x="{X0}" y="14">level</text>')
svg.append(f'<text class="ts te" x="{X0 - 6}" y="{YTOP + 4}">7</text>')
svg.append(f'<text class="ts te" x="{X0 - 6}" y="{YBOT + 4}">0</text>')
svg.append(f'<text class="ts" x="{X1 - 22}" y="174">time</text>')
svg.append(f'<polyline class="c1" fill="none" points="{pts}"/>')
# stepped digital line: each sample's level held until the next sample
d = f"M{x(0):.1f},{y(levels[0]):.1f}"
for t in range(N):
    d += f" H{x(t + 1):.1f}"
    if t + 1 < N:
        d += f" V{y(levels[t + 1]):.1f}"
svg.append(f'<path class="c2 sw2" fill="none" d="{d}"/>')
for t in range(N):
    svg.append(f'<circle class="f1" cx="{x(t):.1f}" cy="{ya(math.sin(2 * math.pi * t / N)):.1f}" r="3.5"/>')
# legend, three rows, below the axis
svg.append(f'<line class="c1" x1="{X0}" y1="188" x2="{X0 + 24}" y2="188"/><text class="tl" x="{X0 + 32}" y="192">analogue wave</text>')
svg.append(f'<circle class="f1" cx="{X0 + 12}" cy="204" r="3.5"/><text class="tl" x="{X0 + 32}" y="208">sample point</text>')
svg.append(f'<line class="c2 sw2" x1="{X0 + 150}" y1="188" x2="{X0 + 174}" y2="188"/><text class="tl" x="{X0 + 182}" y="192">stored level</text>')
svg.append('</svg><figcaption>CAPTION</figcaption></figure>')
print("\n".join(svg))
print()

# ---- Figure 2: pixel grid for RLE ----------------------------------------------------------------
rows = ["LLLLLLLLLLLL", "LLLLDDDDLLLL", "LLDDDDDDDDLL", "LLLLDDDDLLLL", "LLLLLLLLLLLL"]
CELL, GX, GY = 18, 14, 30


def rle(row):
    out, i = [], 0
    while i < len(row):
        j = i
        while j < len(row) and row[j] == row[i]:
            j += 1
        out.append(f"{j - i}{row[i]}")
        i = j
    return out


g = ['<figure class="fig small"><svg viewBox="0 0 330 160" role="img" aria-label="PLACEHOLDER">']
g.append(f'<text class="tl ti" x="{GX}" y="16">12 × 5 pixel image</text><text class="tl ti" x="246" y="16">RLE of each row</text>')
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        cls = "f1" if ch == "D" else "fm"
        g.append(f'<rect class="{cls} s-acc" x="{GX + c * CELL}" y="{GY + r * CELL}" width="{CELL}" height="{CELL}"/>')
    g.append(f'<text class="tl" x="{GX + 12 * CELL + 12}" y="{GY + r * CELL + 13}">{" ".join(rle(row))}</text>')
g.append(f'<text class="tl" x="{GX}" y="{GY + 5 * CELL + 22}">L = light pixel (pale square), D = dark pixel (solid square)</text>')
g.append('</svg><figcaption>CAPTION</figcaption></figure>')
print("\n".join(g))
for row in rows:
    print(rle(row))
print("runs", sum(len(rle(r)) for r in rows))
# label box check: the widest RLE label starts at GX + 12*CELL + 12 and is at most 8 chars of 7 px
print("rle label right edge", GX + 12 * CELL + 12 + 8 * 7, "viewBox width 330")
print("legend right edge", GX + 52 * 7)
