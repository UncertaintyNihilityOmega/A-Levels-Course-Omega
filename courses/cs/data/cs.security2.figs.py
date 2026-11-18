# data/cs.security2.figs.py: builds the digital-signature figure of cs.security2 and checks its coordinates.
# Run: py data/cs.security2.figs.py  (prints the SVG to paste into the chapter, then "figure ok")
CH = 7.0   # width of one character of a 13 px label


def tbox(x, y, s, mode="c"):
    w = len(s) * CH
    x0 = x - w / 2 if mode == "c" else x
    return (x0, y - 10, x0 + w, y + 3)


def overlap(a, b, gap=4):
    return not (a[2] + gap <= b[0] or b[2] + gap <= a[0] or a[3] + gap <= b[1] or b[3] + gap <= a[1])


VB = (0, 0, 600, 270)
shapes = []      # (x0, y0, x1, y1, label lines, fill class)
texts = []       # (x, y, text, class, mode)
arrows = []      # (x0, y0, x1, y1)

W, H = 96, 44


def node(x, y, lines, fill):
    shapes.append((x, y, x + W, y + H, lines, fill))


def link(a):
    xa, ya, xb, yb = a
    arrows.append((xa, ya, xb, yb))


# sender row
texts.append((8, 18, "Sender: signs with their own private key", "tl tb", "l"))
row1 = [(8, ["Message"], "fm"), (128, ["Hash", "function"], "f2"), (248, ["Digest"], "fm"),
        (368, ["Encrypt with", "private key"], "f2"), (488, ["Digital", "signature"], "fm")]
for x, lines, fill in row1:
    node(x, 30, lines, fill)
for i in range(len(row1) - 1):
    x1 = row1[i][0] + W
    x2 = row1[i + 1][0]
    link((x1, 52, x2 - 2, 52))
# the network line
texts.append((300, 106, "the message and the signature are sent to the receiver", "tl tc", "c"))
# receiver rows
texts.append((8, 138, "Receiver: checks with the sender's public key", "tl tb", "l"))
row2a = [(8, ["Message", "received"], "fm"), (128, ["Hash", "function"], "f2"), (248, ["Digest 1"], "fm")]
row2b = [(8, ["Digital", "signature"], "fm"), (128, ["Decrypt with", "public key"], "f2"), (248, ["Digest 2"], "fm")]
for x, lines, fill in row2a:
    node(x, 148, lines, fill)
for x, lines, fill in row2b:
    node(x, 210, lines, fill)
for row, y in ((row2a, 170), (row2b, 232)):
    for i in range(len(row) - 1):
        link((row[i][0] + W, y, row[i + 1][0] - 2, y))
# compare
CX0, CY0, CX1, CY1 = 410, 180, 590, 224
shapes.append((CX0, CY0, CX1, CY1, ["Compare Digest 1", "with Digest 2"], "f2"))
link((248 + W, 170, CX0 - 2, 194))
link((248 + W, 232, CX0 - 2, 210))
texts.append((500, 246, "Same: genuine and unchanged", "tl tc", "c"))
texts.append((500, 264, "Different: do not trust it", "tl tc", "c"))

# ------------------------------------------------------------------ checks
boxes = []
for (x0, y0, x1, y1, lines, fill) in shapes:
    n = len(lines)
    for k, s in enumerate(lines):
        w = len(s) * CH
        assert w + 8 <= (x1 - x0), f"label {s!r} too wide for its box"
    boxes.append((x0, y0, x1, y1))
for i, a in enumerate(boxes):
    for b in boxes[i + 1:]:
        assert not overlap(a, b, 10), f"shapes {a} and {b} too close"
    assert a[0] >= 2 and a[1] >= 2 and a[2] <= VB[2] - 2 and a[3] <= VB[3] - 2, f"shape {a} outside the viewBox"
tb = [tbox(x, y, s, m) for (x, y, s, c, m) in texts]
for (x, y, s, c, m), b in zip(texts, tb):
    assert b[0] >= 2 and b[2] <= VB[2] - 2 and b[1] >= 2 and b[3] <= VB[3] - 2, f"text {s!r} outside the viewBox {b}"
    for sb in boxes:
        assert not overlap(b, sb, 4), f"text {s!r} too close to a shape {sb}"
for i in range(len(tb)):
    for j in range(i + 1, len(tb)):
        assert not overlap(tb[i], tb[j], 4), f"texts {texts[i][2]!r} and {texts[j][2]!r} overlap"
for (xa, ya, xb, yb) in arrows:
    assert abs(xb - xa) + abs(yb - ya) >= 20, f"arrow {(xa, ya, xb, yb)} too short"
    for t in tb:
        # the arrow's bounding box (with 4 px) must not cross a text
        ab = (min(xa, xb), min(ya, yb), max(xa, xb), max(ya, yb))
        assert not overlap(ab, t, 3), f"arrow {(xa, ya, xb, yb)} touches text {t}"

out = [f'<figure class="fig"><svg viewBox="0 0 600 270" role="img" aria-label="Producing and checking a digital signature. Sender row: the message goes through a hash function to give a digest, the digest is encrypted with the sender\'s private key, and the result is the digital signature. The message and the signature are sent to the receiver. Receiver rows: the received message goes through the same hash function to give Digest 1; the received signature is decrypted with the sender\'s public key to give Digest 2. The receiver compares the two digests. If they are the same the message is genuine and unchanged; if they are different it must not be trusted.">']
for (x, y, s, c, m) in texts:
    out.append(f'<text class="{c}" x="{x:g}" y="{y:g}">{s}</text>')
out.append(f'<path class="ln-m thin dash" d="M8 114 H592"/>')
for (x0, y0, x1, y1, lines, fill) in shapes:
    rx = ' rx="6"' if False else ''
    out.append(f'<rect class="{fill} s-acc sw2" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    cx = (x0 + x1) / 2
    if len(lines) == 1:
        out.append(f'<text class="tl tc" x="{cx:g}" y="{(y0 + y1) / 2 + 4:g}">{lines[0]}</text>')
    else:
        out.append(f'<text class="tl tc" x="{cx:g}" y="{(y0 + y1) / 2 - 2:g}">{lines[0]}</text>')
        out.append(f'<text class="tl tc" x="{cx:g}" y="{(y0 + y1) / 2 + 13:g}">{lines[1]}</text>')
for (xa, ya, xb, yb) in arrows:
    out.append(f'<path class="ln" d="M{xa} {ya} L{xb} {yb}" marker-end="url(#ah)"/>')
out.append('</svg><figcaption>A digital signature is the digest of a message, encrypted with the sender\'s private key. The receiver decrypts the signature with the sender\'s public key and compares the result with a digest of the message they received. The message itself is not encrypted.</figcaption></figure>')
fig = "".join(out)

if __name__ == "__main__":
    # the dashed divider (y = 114) must be clear of the texts above and below it
    for t in tb:
        assert not (t[1] - 3 <= 114 <= t[3] + 3), f"divider crosses text {t}"
    print(fig)
    print("figure ok")
