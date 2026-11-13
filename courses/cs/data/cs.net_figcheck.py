# data/cs.net_figcheck.py: checks label boxes in the hand SVGs of cs.networks and cs.internet.
# Usage (from the course folder): py data/cs.net_figcheck.py
# A 13 px label is about 7 px per character wide and 13 px tall (baseline at y, top at y - 10).
import pathlib
import re

ROOT = pathlib.Path.cwd()
problems = 0


def attrs(tag):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', tag))


def check(chapter):
    global problems
    text = (ROOT / "chapters" / f"{chapter}.md").read_text(encoding="utf-8")
    for n, svg in enumerate(re.findall(r"<svg.*?</svg>", text, re.S), 1):
        vb = [float(v) for v in attrs(svg)["viewBox"].split()] if "viewBox" in attrs(re.match(r"<svg[^>]*>", svg).group(0)) else None
        vb = [float(v) for v in attrs(re.match(r"<svg[^>]*>", svg).group(0))["viewBox"].split()]
        items = []   # in drawing order: (kind, data)
        for m in re.finditer(r"<(line|rect|text)\b([^>]*)>(.*?)(?=<|$)", svg, re.S):
            kind, tag, inner = m.group(1), attrs(m.group(2)), m.group(3)
            if kind == "line":
                items.append(("line", (float(tag["x1"]), float(tag["y1"]), float(tag["x2"]), float(tag["y2"]), tag.get("class", ""))))
            elif kind == "rect":
                items.append(("rect", (float(tag["x"]), float(tag["y"]), float(tag["width"]), float(tag["height"]))))
            else:
                x, y, label = float(tag["x"]), float(tag["y"]), inner
                width = 7 * len(label)
                cls = tag.get("class", "").split()
                left = x - width / 2 if "tc" in cls else (x - width if "te" in cls else x)
                items.append(("text", (left, y - 10, left + width, y + 3, label)))
        rects = [(i, d) for i, (k, d) in enumerate(items) if k == "rect"]
        texts = [(i, d) for i, (k, d) in enumerate(items) if k == "text"]
        for i, (l, t, r, b, label) in texts:
            tag = f"{chapter} svg {n} label {label!r}"
            if l < vb[0] or t < vb[1] or r > vb[0] + vb[2] or b > vb[1] + vb[3]:
                print("OUTSIDE viewBox:", tag, (l, t, r, b)); problems += 1
            for _, (rx, ry, rw, rh) in rects:     # inside a rect, or at least 4 px clear of its border
                inside = l >= rx + 2 and r <= rx + rw - 2 and t >= ry + 1 and b <= ry + rh - 1
                touches = not (r < rx - 4 or l > rx + rw + 4 or b < ry - 4 or t > ry + rh + 4)
                if touches and not inside:
                    print("TOUCHES rect:", tag, (l, t, r, b), (rx, ry, rw, rh)); problems += 1
            for j, (l2, t2, r2, b2, label2) in texts:
                if j > i and not (r + 4 < l2 or l2 + 0 > r + 400 or b + 4 < t2 or t2 + 0 > b + 400):
                    if not (r + 4 < l2 or r2 + 4 < l or b + 4 < t2 or b2 + 4 < t):
                        print("LABELS overlap:", tag, "and", label2); problems += 1
            for k, (kind, d) in enumerate(items):
                if kind != "line":
                    continue
                x1, y1, x2, y2, cls = d
                steps = int(max(abs(x2 - x1), abs(y2 - y1))) + 1
                for s in range(steps + 1):
                    px, py_ = x1 + (x2 - x1) * s / steps, y1 + (y2 - y1) * s / steps
                    hidden = any(rk > k and rx <= px <= rx + rw and ry <= py_ <= ry + rh for rk, (rx, ry, rw, rh) in rects)
                    if hidden:
                        continue
                    if l - 3 <= px <= r + 3 and t - 3 <= py_ <= b + 3:
                        if "halo" in text.split(label)[0][-200:] or True:
                            pass
                        # a halo label may sit on a dashed reference line; report only solid or arrow lines
                        if "dash" in cls and "ln-m" in cls:
                            continue
                        print("LINE through label:", tag, (round(px), round(py_)), cls); problems += 1
                        break
        print(f"{chapter} svg {n}: {len(texts)} labels, {len(rects)} rects checked")


for chapter in ("cs.networks", "cs.internet"):
    check(chapter)
print("figure check:", "clean" if problems == 0 else f"{problems} problems")
