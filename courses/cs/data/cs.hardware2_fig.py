# data/cs.hardware2_fig.py: builds the virtual machine figure of cs.hardware2 and checks its label boxes
# (same checker as data/cs.networks2_fig.py). Run: py data/cs.hardware2_fig.py (writes data/cs.hardware2_figs.txt)
import pathlib

OUT = pathlib.Path(__file__).resolve().parent / "cs.hardware2_figs.txt"
CW, LH = 7.0, 13.0


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.svg, self.texts, self.lines, self.rects = [], [], [], []

    def rect(self, cls, x, y, w, h):
        self.svg.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}"/>')
        self.rects.append((x, y, x + w, y + h))

    def text(self, x, y, s, anchor="c", inside=False):
        w = len(s) * CW
        x0 = x - w / 2 if anchor == "c" else (x if anchor == "s" else x - w)
        cls = {"c": "tl tc", "s": "tl", "e": "tl te"}[anchor]
        self.svg.append(f'<text class="{cls}" x="{x}" y="{y}">{s}</text>')
        self.texts.append((x0, y - 10, x0 + w, y + 3, s, inside))

    def line(self, cls, pts, arrow=False):
        d = "M" + " L".join(f"{x} {y}" for x, y in pts)
        self.svg.append(f'<path class="{cls}" d="{d}"' + (' marker-end="url(#ah)"' if arrow else "") + "/>")
        self.lines.append(pts)

    def check(self):
        def seg_box_dist(p, q, b):
            # smallest distance between segment p-q and box b (sampled)
            best = 1e9
            for i in range(0, 201):
                t = i / 200
                x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
                dx = max(b[0] - x, 0, x - b[2])
                dy = max(b[1] - y, 0, y - b[3])
                best = min(best, (dx * dx + dy * dy) ** 0.5)
            return best

        for i, t in enumerate(self.texts):
            assert t[0] >= 0 and t[2] <= self.w and t[1] >= 0 and t[3] <= self.h, ("outside", t)
            for pts in self.lines:
                for p, q in zip(pts, pts[1:]):
                    d = seg_box_dist(p, q, t[:4])
                    assert d >= 4, ("label too close to a line", t[4], round(d, 1), p, q)
            for u in self.texts[i + 1:]:
                gap_x = max(t[0] - u[2], u[0] - t[2])
                gap_y = max(t[1] - u[3], u[1] - t[3])
                assert max(gap_x, gap_y) >= 4, ("labels overlap", t[4], u[4])
            if not t[5]:
                for r in self.rects:
                    gap_x = max(t[0] - r[2], r[0] - t[2])
                    gap_y = max(t[1] - r[3], r[1] - t[3])
                    assert max(gap_x, gap_y) >= 4, ("label touches a box", t[4], r)
            else:  # a label inside a box must be inside it with room
                assert any(r[0] + 4 <= t[0] and t[2] <= r[2] - 4 and r[1] + 2 <= t[1] and t[3] <= r[3] - 2 for r in self.rects), ("label not inside its box", t[4])

    def out(self, alt, cap, cls="fig"):
        body = "".join(self.svg)
        return (f'<figure class="{cls}"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{alt}">{body}</svg>'
                f"<figcaption>{cap}</figcaption></figure>")



# ---------------------------------------------------------------------------------------------
# Figure: one physical computer running three virtual machines under a hypervisor
# ---------------------------------------------------------------------------------------------
f = Fig(600, 262)
f.rect("fm s-acc sw2", 20, 210, 560, 40)
f.text(300, 235, "Physical hardware: processor, memory, storage", inside=True)
f.rect("fm2 s-acc sw2", 20, 160, 560, 40)
f.text(300, 185, "Hypervisor (manages the virtual machines)", inside=True)
for i, x in enumerate((20, 213, 407)):
    f.text(x + 86.5, 36, f"Virtual machine {i + 1}")
    f.rect("f1 s-acc sw2", x, 50, 173, 45)
    f.text(x + 86.5, 77, "Applications", inside=True)
    f.rect("f1 s-acc sw2", x, 105, 173, 45)
    f.text(x + 86.5, 132, "Guest operating system", inside=True)
f.check()
ALT = ("A physical computer running three virtual machines. From the bottom: a wide box for the physical hardware "
       "(processor, memory, storage); above it a wide box for the hypervisor, which manages the virtual machines; above that "
       "three separate columns, each labelled Virtual machine 1, 2 or 3, each with a guest operating system box and an "
       "applications box on top of it.")
CAP = ("The hypervisor shares the one set of hardware among three virtual machines. Each guest operating system believes it has a whole computer "
       "to itself, and the three cannot see each other.")
OUT.write_text(f.out(ALT, CAP) + chr(10), encoding="utf-8")
print("figure ok", OUT)
