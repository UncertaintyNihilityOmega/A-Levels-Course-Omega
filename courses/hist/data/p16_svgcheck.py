# data/p16_svgcheck.py: shared SVG layout check for the P16 chapters (labels inside boxes, clear of each other, inside the viewBox)
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
        boxes = []
        for tm in re.finditer(r"<text\b([^>]*)>(.*?)</text>", body, re.S):
            ta = attrs(tm.group(1))
            s = html.unescape(re.sub(r"<[^>]*>", "", tm.group(2)))
            cls = ta.get("class", "").split()
            w = len(s) * (7.6 if "tb" in cls else 7.0)
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
                if inside and r["width"] >= 60 and r["height"] >= 20:
                    assert x0 >= r["x"] + 3 and x1 <= r["x"] + r["width"] - 3, f"label wider than its box: {s!r} {x0:.0f}-{x1:.0f} vs {r['x']}-{r['x'] + r['width']}"
                    assert y + 3 <= r["y"] + r["height"], f"label below its box: {s!r}"
                    assert y - 10 >= r["y"], f"label above its box: {s!r}"
            boxes.append(box)
        for i, b in enumerate(boxes):
            for c in boxes[i + 1:]:
                ox = min(b[2], c[2]) - max(b[0], c[0])
                oy = min(b[3], c[3]) - max(b[1], c[1])
                assert not (ox > -3 and oy > -2), f"labels overlap: {b[4]!r} and {c[4]!r}"
        # labels must not touch a thin bar
        for b in boxes:
            for r in rects:
                if r["height"] < 20:
                    ox = min(b[2], r["x"] + r["width"]) - max(b[0], r["x"])
                    oy = min(b[3] + 2, r["y"] + r["height"]) - max(b[1], r["y"])
                    assert not (ox > 0 and oy > 0), f"label touches a bar: {b[4]!r}"
        for lm in re.finditer(r"<line\b([^>]*)>", body):
            la = attrs(lm.group(1))
            if "marker-end" in la:
                ln = ((float(la["x2"]) - float(la["x1"])) ** 2 + (float(la["y2"]) - float(la["y1"])) ** 2) ** 0.5
                assert ln >= 20, f"arrow too short: {ln}"
                x2, y2 = float(la["x2"]), float(la["y2"])
                for r in rects:
                    inside = r["x"] - 1 < x2 < r["x"] + r["width"] + 1 and r["y"] < y2 < r["y"] + r["height"]
                    assert not inside, "arrow ends inside a box"
    return n
