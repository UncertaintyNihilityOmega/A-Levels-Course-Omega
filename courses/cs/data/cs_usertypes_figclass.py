import sys
CH = 7.0  # px per character at 13 px


class Fig:
    def __init__(self, name, w, h):
        self.name, self.w, self.h = name, w, h
        self.parts, self.boxes = [], []   # boxes: (kind, x0, y0, x1, y1, label)

    def rect(self, cls, x, y, w, h):
        self.parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}"/>')
        self.boxes.append(("rect", x, y, x + w, y + h, cls))

    def text(self, cls, x, y, s):
        n = sum(4.5 if c in "⁻¹²³⁴⁵⁶⁷" else CH for c in s)
        if "tc" in cls.split():
            x0 = x - n / 2
        elif "te" in cls.split():
            x0 = x - n
        else:
            x0 = x
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}">{s}</text>')
        self.boxes.append(("text", x0, y - 10, x0 + n, y + 3, s))

    def line(self, cls, d, marker=False):
        m = ' marker-end="url(#ah)"' if marker else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{m}/>')

    def check(self):
        texts = [b for b in self.boxes if b[0] == "text"]
        rects = [b for b in self.boxes if b[0] == "rect"]
        for b in texts:
            assert b[1] >= 0 and b[3] <= self.w and b[2] >= 0 and b[4] <= self.h, (self.name, "outside", b)
        for i, a in enumerate(texts):
            for b in texts[i + 1:]:
                gap_x = max(b[1] - a[3], a[1] - b[3])
                gap_y = max(b[2] - a[4], a[2] - b[4])
                assert max(gap_x, gap_y) >= 4, (self.name, "labels too close", a[5], b[5])
        # a label may sit inside a rect, but must not straddle a rect edge
        for t in texts:
            for r in rects:
                inter_x = min(t[3], r[3]) > max(t[1], r[1])
                inter_y = min(t[4], r[4]) > max(t[2], r[2])
                if inter_x and inter_y:
                    inside = t[1] >= r[1] + 2 and t[3] <= r[3] - 2 and t[2] >= r[2] + 1 and t[4] <= r[4] + 1
                    assert inside, (self.name, "label straddles a box edge", t[5], r[5])

    def svg(self, label, caption):
        self.check()
        return (f'<figure class="fig small"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{label}">'
                + "".join(self.parts) + f'</svg><figcaption>{caption}</figcaption></figure>')


