# data/p9_figcheck.py: checks hand-drawn SVG figures of P9 chapters: label boxes (7 px per character, 13 px tall)
# against each other, against lines/rect edges (4 px clear) and against the viewBox.
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
def seg_rect_hit(seg, box):
    (x1, y1), (x2, y2) = seg
    bx0, by0, bx1, by1 = box
    n = 40
    for i in range(n + 1):
        x = x1 + (x2 - x1) * i / n; y = y1 + (y2 - y1) * i / n
        if bx0 <= x <= bx1 and by0 <= y <= by1: return True
    return False
for cid in sys.argv[1:]:
    text = (root / "chapters" / f"{cid}.md").read_text(encoding="utf-8")
    for fi, m in enumerate(re.finditer(r"<svg viewBox=\"([^\"]+)\".*?</svg>", text, re.S)):
        vb = [float(v) for v in m.group(1).split()]
        svg = m.group(0)
        texts, segs, rects = [], [], []
        for t in re.finditer(r"<text class=\"([^\"]*)\" x=\"([\d.-]+)\" y=\"([\d.-]+)\">(.*?)</text>", svg):
            cls, x, y, s = t.group(1).split(), float(t.group(2)), float(t.group(3)), t.group(4)
            w = 7 * len(s)
            x0 = x - w / 2 if "tc" in cls else (x - w if "te" in cls else x)
            texts.append((s, (x0, y - 10, x0 + w, y + 3)))
        for r in re.finditer(r"<rect class=\"([^\"]*)\" x=\"([\d.-]+)\" y=\"([\d.-]+)\" width=\"([\d.-]+)\" height=\"([\d.-]+)\"", svg):
            x, y, w, h = (float(r.group(i)) for i in (2, 3, 4, 5))
            rects.append((x, y, x + w, y + h))
            outline = "s-acc" in r.group(1) or "ln" in r.group(1)
            if outline:
                segs += [((x, y), (x + w, y)), ((x + w, y), (x + w, y + h)), ((x + w, y + h), (x, y + h)), ((x, y + h), (x, y))]
        for l in re.finditer(r"<line class=\"[^\"]*\" x1=\"([\d.-]+)\" y1=\"([\d.-]+)\" x2=\"([\d.-]+)\" y2=\"([\d.-]+)\"", svg):
            a, b, c, d = (float(l.group(i)) for i in (1, 2, 3, 4))
            segs.append(((a, b), (c, d)))
        for p in re.finditer(r"<path class=\"[^\"]*\" d=\"M ([\d.-]+) ([\d.-]+) C ([\d.-]+) ([\d.-]+) ([\d.-]+) ([\d.-]+) ([\d.-]+) ([\d.-]+)\"", svg):
            x0, y0, x1, y1, x2, y2, x3, y3 = (float(p.group(i)) for i in range(1, 9))
            pts = []
            for i in range(41):
                t = i / 40
                pts.append(((1-t)**3*x0 + 3*(1-t)**2*t*x1 + 3*(1-t)*t*t*x2 + t**3*x3, (1-t)**3*y0 + 3*(1-t)**2*t*y1 + 3*(1-t)*t*t*y2 + t**3*y3))
            segs += list(zip(pts[:-1], pts[1:]))
        problems = []
        for i, (s, b) in enumerate(texts):
            if b[0] < 0 or b[1] < 0 or b[2] > vb[2] or b[3] > vb[3]:
                problems.append(f"'{s}' outside viewBox {b}")
            big = (b[0] - 4, b[1] - 4, b[2] + 4, b[3] + 4)
            for sg in segs:
                if seg_rect_hit(sg, big): problems.append(f"'{s}' within 4 px of a line/edge {sg}"); break
            for s2, b2 in texts[i + 1:]:
                if not (b[2] + 4 < b2[0] or b2[2] + 4 < b[0] or b[3] + 4 < b2[1] or b2[3] + 4 < b[1]):
                    problems.append(f"'{s}' close to '{s2}'")
        print(f"{cid} figure {fi + 1} viewBox {vb}: {'ok' if not problems else ''}")
        for p in problems: print("   ", p)
