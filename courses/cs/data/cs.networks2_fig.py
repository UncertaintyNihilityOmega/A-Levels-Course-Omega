# data/cs.networks2_fig.py: builds the two SVG figures of cs.networks2 and checks every label box against every line,
# box and other label (13 px label, about 7 px per character, top at y - 10, bottom at y + 3).
# Run: py data/cs.networks2_fig.py   (writes data/cs.networks2_figs.txt, the text pasted into the chapter)
import pathlib

OUT = pathlib.Path(__file__).resolve().parent / "cs.networks2_figs.txt"
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
# Figure 1: the four layers on two hosts, with a router that has only the two lower layers
# ---------------------------------------------------------------------------------------------
f1 = Fig(600, 250)
layers = ["Application", "Transport", "Internet", "Link"]
ys = [45, 95, 145, 195]
hostx = {"A": 20, "B": 430}
for h, x in hostx.items():
    f1.text(x + 75, 32, f"Host {h}")
    for name, y in zip(layers, ys):
        f1.rect("fm s-acc sw2", x, y, 150, 40)
        f1.text(x + 75, y + 25, name, inside=True)
f1.text(300, 137, "Router")
for name, y in zip(layers[2:], ys[2:]):
    f1.rect("fm2 s-acc sw2", 225, y, 150, 40)
    f1.text(300, y + 25, name, inside=True)
# logical connections (dashed) and the real physical links (solid)
f1.line("ln-m thin dash", [(170, 65), (430, 65)])
f1.text(300, 57, "HTTP request and reply")
f1.line("ln-m thin dash", [(170, 115), (430, 115)])
f1.text(300, 107, "TCP segments")
f1.line("ln-m thin dash", [(170, 165), (225, 165)])
f1.line("ln-m thin dash", [(375, 165), (430, 165)])
f1.text(197, 157, "IP")
f1.text(403, 157, "IP")
f1.line("c1 sw2", [(170, 215), (225, 215)])
f1.line("c1 sw2", [(375, 215), (430, 215)])
f1.text(197, 207, "frames")
f1.text(403, 207, "frames")
f1.line("ln", [(8, 48), (8, 232)], arrow=True)
f1.line("ln", [(592, 232), (592, 48)], arrow=True)
f1.check()
ALT1 = ("The four TCP/IP layers on two hosts and a router. Host A and host B each have four boxes from top to bottom: "
        "Application, Transport, Internet, Link. The router between them has only Internet and Link. Dashed lines join "
        "the Application layers (HTTP request and reply) and the Transport layers (TCP segments) of the two hosts, passing "
        "the router. Dashed lines labelled IP join the Internet layers of host A and the router and of the router and host B. "
        "Solid lines labelled frames join the Link layers. A downward arrow beside host A shows data going down the stack "
        "and an upward arrow beside host B shows data going up.")
CAP1 = ("A message goes down the four layers of host A, crosses the network as frames, and goes up the layers of host B. "
        "The router reads only as far as the Internet layer. The dashed lines are the conversation each layer believes it is having.")

# ---------------------------------------------------------------------------------------------
# Figure 2: four packets cross a network by two different routes
# ---------------------------------------------------------------------------------------------
f2 = Fig(600, 262)
nodes = {  # name: (x, y, w, h)
    "A": (15, 105, 64, 40), "R1": (130, 110, 50, 30), "R2": (270, 35, 50, 30),
    "R3": (270, 185, 50, 30), "R4": (410, 110, 50, 30), "B": (521, 105, 64, 40)}
for name, (x, y, w, h) in nodes.items():
    label = {"A": "Host A", "B": "Host B"}.get(name, name)
    f2.rect("fm s-acc sw2" if name in ("A", "B") else "fm2 s-acc sw2", x, y, w, h)
    f2.text(x + w / 2, y + h / 2 + 5, label, inside=True)
f2.line("c1 sw2", [(79, 125), (130, 125)])
f2.line("c1 sw2", [(180, 118), (270, 52)])
f2.line("c1 sw2", [(320, 52), (410, 118)])
f2.line("c1 sw2 dash", [(180, 132), (270, 198)])
f2.line("c1 sw2 dash", [(320, 198), (410, 132)])
f2.line("c1 sw2", [(460, 125), (521, 125)])
f2.text(104, 118, "5 ms")
f2.text(210, 78, "12 ms", anchor="e")
f2.text(372, 78, "10 ms", anchor="s")
f2.text(210, 172, "20 ms", anchor="e")
f2.text(372, 180, "25 ms", anchor="s")
f2.text(490, 118, "5 ms")
f2.text(295, 25, "Packets 1, 3 and 4")
f2.text(295, 236, "Packet 2 (dashed route)")
f2.check()
ALT2 = ("A network with Host A on the left, then router R1, then two routes to router R4, then Host B on the right. "
        "The upper route goes R1, R2, R4 and is a solid line; its links take 12 ms and 10 ms, and packets 1, 3 and 4 use it. "
        "The lower route goes R1, R3, R4 and is dashed; its links take 20 ms and 25 ms, and packet 2 uses it. "
        "The link from Host A to R1 and the link from R4 to Host B each take 5 ms.")
CAP2 = ("Packet switching: R1 sends packet 2 by the dashed lower route and the other three by the solid upper route. "
        "The upper route takes 5 + 12 + 10 + 5 = 32 ms and the lower route takes 5 + 20 + 25 + 5 = 55 ms.")

assert 5 + 12 + 10 + 5 == 32 and 5 + 20 + 25 + 5 == 55
OUT.write_text("FIG1\n" + f1.out(ALT1, CAP1) + "\nFIG2\n" + f2.out(ALT2, CAP2, "fig") + "\n", encoding="utf-8")
print("figures ok", OUT)
