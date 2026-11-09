# data/p17_svg.py: shared layout check for the hand SVG figures of P17 (labels inside boxes and the viewBox, no label
# overlaps, arrows long enough and not ending inside a box). Imported by checks/hist.int.1929.*.py
import re, html


def attrs(tag):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', tag))


def check_svgs(text):
    n = 0
    for m in re.finditer(r"<svg\b([^>]*)>(.*?)</svg>", text, re.S):
        n += 1
        a = attrs(m.group(1))
        vb = [float(v) for v in a["viewBox"].split()]
        W, H = vb[2], vb[3]
        body = m.group(2)
        rects = [attrs(t) for t in re.findall(r"<rect\b[^>]*>", body)]
        rects = [{k: (float(v) if k in "x y width height".split() else v) for k, v in r.items()} for r in rects]
        for r in rects:
            assert r["x"] >= 0 and r["x"] + r["width"] <= W and r["y"] >= 0 and r["y"] + r["height"] <= H, f"rect outside viewBox: {r}"
        boxes = []
        for tm in re.finditer(r"<text\b([^>]*)>(.*?)</text>", body, re.S):
            ta = attrs(tm.group(1))
            s = html.unescape(re.sub(r"<[^>]*>", "", tm.group(2)))
            cls = ta.get("class", "").split()
            w = len(s) * (7.6 if "tb" in cls else 7.0)
            if "ts" in cls:
                w = len(s) * 6.0
            x, y = float(ta["x"]), float(ta["y"])
            if "tc" in cls:
                x0, x1 = x - w / 2, x + w / 2
            else:
                x0, x1 = x, x + w
            box = (x0, y - 10, x1, y + 3, s)
            assert x0 >= 0 and x1 <= W, f"label outside viewBox width: {s!r} {x0:.0f}-{x1:.0f} of {W}"
            assert y + 3 <= H, f"label below viewBox: {s!r}"
            for r in rects:
                inside = r["x"] <= x <= r["x"] + r["width"] and r["y"] <= y - 4 <= r["y"] + r["height"]
                if inside and r["width"] >= 40:
                    assert x0 >= r["x"] + 3 and x1 <= r["x"] + r["width"] - 3, f"label wider than its box: {s!r} {x0:.0f}-{x1:.0f} vs {r['x']}-{r['x'] + r['width']}"
                    assert y + 3 <= r["y"] + r["height"], f"label below its box: {s!r}"
                    assert y - 10 >= r["y"], f"label above its box: {s!r}"
            boxes.append(box)
        for i, b in enumerate(boxes):
            for c in boxes[i + 1:]:
                ox = min(b[2], c[2]) - max(b[0], c[0])
                oy = min(b[3], c[3]) - max(b[1], c[1])
                assert not (ox > -3 and oy > -2), f"labels overlap: {b[4]!r} and {c[4]!r}"
        # labels must keep 4 px clear of horizontal and vertical lines they do not belong to
        lines = [attrs(t) for t in re.findall(r"<line\b[^>]*>", body)]
        for lm in lines:
            x1, y1, x2, y2 = (float(lm[k]) for k in ("x1", "y1", "x2", "y2"))
            if "marker-end" in lm:
                ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                assert ln >= 20, f"arrow too short: {ln:.0f}"
                for r in rects:
                    inside = r["x"] - 1 < x2 < r["x"] + r["width"] + 1 and r["y"] - 1 < y2 < r["y"] + r["height"] + 1
                    assert not inside, "arrow ends inside or touching a box"
            for b in boxes:
                if y1 == y2 and min(x1, x2) - 2 <= b[2] and max(x1, x2) + 2 >= b[0]:
                    assert not (b[1] - 4 < y1 < b[3] + 4), f"label too close to a horizontal line: {b[4]!r}"
                if x1 == x2 and min(y1, y2) - 2 <= b[3] and max(y1, y2) + 2 >= b[1]:
                    assert not (b[0] - 4 < x1 < b[2] + 4), f"label too close to a vertical line: {b[4]!r}"
    return n
