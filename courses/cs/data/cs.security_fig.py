# data/cs.security_fig.py: builds and checks the two SVG figures of chapters/cs.security.md
# (the firewall and the received parity block). Run: py data/cs.security_fig.py
import pathlib

CW = 7.0


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts, self.boxes, self.texts, self.arrows = [], [], [], []

    def rect(self, x, y, w, h, cls):
        self.parts.append(f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="{w}" height="{h}"/>')
        self.boxes.append((x, y, w, h))

    def text(self, x, y, s, cls="tl tc"):
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}">{s}</text>')
        n = len(s)
        if " te" in " " + cls:
            x0, x1 = x - n * CW, x
        elif cls.split()[-1] == "tl" and "tc" not in cls:
            x0, x1 = x, x + n * CW
        else:
            x0, x1 = x - n * CW / 2, x + n * CW / 2
        self.texts.append((x0, y - 10, x1, y + 3, s, cls))

    def arrow(self, x1, y1, x2, y2, cls="ln"):
        self.parts.append(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#ah)"/>')
        self.arrows.append((x1, y1, x2, y2))

    def check(self, allow_in_box=True):
        for (x0, y0, x1, y1, s, cls) in self.texts:
            assert 0 <= x0 and x1 <= self.w and 0 <= y0 and y1 <= self.h, f"text outside figure: {s}"
        for i, a in enumerate(self.texts):
            for b in self.texts[i + 1:]:
                overlap = not (a[2] + 4 <= b[0] or b[2] + 4 <= a[0] or a[3] + 4 <= b[1] or b[3] + 4 <= a[1])
                assert not overlap, f"labels collide: {a[4]} / {b[4]}"
        for (x0, y0, x1, y1, s, cls) in self.texts:
            inside = any(bx + 2 <= x0 and x1 <= bx + bw - 2 and by <= y0 + 1 and y1 <= by + bh for bx, by, bw, bh in self.boxes)
            if inside:
                continue
            for bx, by, bw, bh in self.boxes:
                clear = x1 + 4 <= bx or bx + bw + 4 <= x0 or y1 + 4 <= by or by + bh + 4 <= y0
                assert clear, f"label {s} touches a box"
        for (x1, y1, x2, y2) in self.arrows:
            assert abs(y2 - y1) >= 20 or abs(x2 - x1) >= 20, "arrow too short"
            for (tx0, ty0, tx1, ty1, s, cls) in self.texts:
                lo_y, hi_y = min(y1, y2), max(y1, y2)
                crosses = tx0 - 4 <= x1 <= tx1 + 4 and not (hi_y < ty0 or lo_y > ty1)
                assert not crosses, f"arrow runs through label {s}"

    def svg(self, label, caption, cls="fig small"):
        return (f'<figure class="{cls}"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{label}">'
                f'{"".join(self.parts)}</svg><figcaption>{caption}</figcaption></figure>')


# ---- Figure 1: a firewall between the internet and a private network ---------------------------
f1 = Fig(340, 262)
f1.rect(30, 10, 280, 34, "fm"); f1.text(170, 32, "The internet")
f1.arrow(100, 48, 100, 96); f1.text(108, 76, "allowed", "tl")
f1.arrow(240, 48, 240, 96, "ln dash"); f1.text(248, 76, "blocked", "tl")
f1.rect(30, 100, 280, 58, "f1"); f1.text(170, 122, "Firewall", "tl tc tb"); f1.text(170, 142, "checks each packet")
f1.arrow(100, 162, 100, 210); f1.text(108, 190, "allowed", "tl")
f1.rect(30, 214, 280, 34, "fm"); f1.text(170, 236, "Private network")
f1.check()

# ---- Figure 2: the received block with one flipped bit ------------------------------------------
WORD = "SECURED"
sent = []
for ch in WORD:
    bits = format(ord(ch), "07b")
    parity = str(bits.count("1") % 2)          # even parity, parity bit on the left
    sent.append(parity + bits)
cols = [sum(int(row[c]) for row in sent) % 2 for c in range(8)]
sent.append("".join(map(str, cols)))
assert all(r.count("1") % 2 == 0 for r in sent) and all(sum(int(r[c]) for r in sent) % 2 == 0 for c in range(8))
ROW, COL = 3, 3                                  # byte 4, data bit 3 (column 3 counting the parity bit as column 0)
recv = [list(r) for r in sent]
recv[ROW][COL] = "0" if recv[ROW][COL] == "1" else "1"
bad_rows = [r for r in range(8) if "".join(recv[r]).count("1") % 2 == 1]
bad_cols = [c for c in range(8) if sum(int(recv[r][c]) for r in range(8)) % 2 == 1]
assert bad_rows == [ROW] and bad_cols == [COL]

x0, y0, cell = 92, 40, 26
f2 = Fig(350, 312)
f2.text(x0 + cell / 2, 28, "P", "tl tc tb")
for k in range(1, 8):
    f2.text(x0 + k * cell + cell / 2, 28, str(k), "tl tc tb")
f2.text(x0 + 8 * cell + 24, 28, "row", "tl tc tb")
for r in range(8):
    f2.text(x0 - 8, y0 + r * cell + 18, f"byte {r + 1}" if r < 7 else "parity byte", "tl te")
    for c in range(8):
        flipped = (r == ROW and c == COL)
        f2.rect(x0 + c * cell, y0 + r * cell, cell, cell, "f1" if flipped else "fm")
        f2.text(x0 + c * cell + cell / 2, y0 + r * cell + 18, recv[r][c])
    if r in bad_rows:
        f2.text(x0 + 8 * cell + 24, y0 + r * cell + 18, "✗", "tl tc tb")
f2.text(x0 - 8, y0 + 8 * cell + 20, "column", "tl te tb")
for c in bad_cols:
    f2.text(x0 + c * cell + cell / 2, y0 + 8 * cell + 20, "✗", "tl tc tb")
f2.text(x0 + 4 * cell, y0 + 8 * cell + 48, "error: byte 4, data bit 3", "tl tc tb")
f2.check()

out = pathlib.Path(__file__).resolve().parent / "cs.security_figs.txt"
out.write_text("\n\n".join([
    f1.svg("A firewall between the internet at the top and a private network at the bottom. Allowed traffic passes down through the firewall to the private network. Blocked traffic, drawn dashed, stops at the firewall.",
           "A firewall checks each packet against its rules. Packets the rules allow pass through; the rest are stopped."),
    f2.svg("An eight by eight grid of bits: seven data bytes for the word SECURED and a parity byte, with the parity bit on the left of each byte. One bit has been flipped. Byte 4 fails its row check and data bit 3 fails its column check, so the error is at byte 4, data bit 3.",
           "A received block with even parity. The row check fails for byte 4 and the column check fails for data bit 3. The shaded bit where they meet is the error."),
]), encoding="utf-8")
print("ok")
print("\n".join(sent))
print("received:", ["".join(r) for r in recv])
