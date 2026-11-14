# data/cs.usertypes_fig.py: builds the three SVG figures of cs.usertypes and checks label boxes
import sys
sys.stdout.reconfigure(encoding="utf-8")
CH = 7.0  # px per character at 13 px


class Fig:
    def __init__(self, name, w, h):
        self.name, self.w, self.h = name, w, h
        self.parts, self.boxes = [], []   # boxes: (kind, x0, y0, x1, y1, label)

    def rect(self, cls, x, y, w, h):
        self.parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}"/>')
        self.boxes.append(("rect", x, y, x + w, y + h, cls))

    def text(self, cls, x, y, s):
        n = len(s) * CH
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


# ---- Figure 1: serial, sequential and random organisation of the same six records -------------
ARRIVAL = [6045, 2171, 9308, 4417, 1052, 7734]
SLOTS = 8
table = [None] * SLOTS
home = {}
for k in ARRIVAL:
    a = k % SLOTS
    home[k] = a
    while table[a] is not None:
        a = (a + 1) % SLOTS
    table[a] = k
f1 = Fig("organisations", 360, 222)
f1.text("tl ti", 20, 16, "Serial: in order of arrival")
for i, k in enumerate(ARRIVAL):
    f1.rect("fm s-acc sw2", 20 + 52 * i, 24, 52, 28)
    f1.text("tl tc", 46 + 52 * i, 43, str(k))
f1.text("tl ti", 20, 82, "Sequential: in order of the key")
for i, k in enumerate(sorted(ARRIVAL)):
    f1.rect("fm s-acc sw2", 20 + 52 * i, 90, 52, 28)
    f1.text("tl tc", 46 + 52 * i, 109, str(k))
f1.text("tl ti", 20, 148, "Random: at the address the hash gives")
for i in range(SLOTS):
    k = table[i]
    cls = "fp s-acc sw2" if k is None else ("f1 s-acc sw2" if home[k] != i else "fm s-acc sw2")
    f1.rect(cls, 20 + 40 * i, 156, 40, 28)
    if k is not None:
        f1.text("tl tc", 40 + 40 * i, 175, str(k))
    f1.text("tl tc", 40 + 40 * i, 202, str(i + 1))
print(f1.svg("Three rows of boxes show the same six records. Serial file: 6045, 2171, 9308, 4417, 1052, 7734 in the order they arrived. Sequential file: 1052, 2171, 4417, 6045, 7734, 9308 in key order. Random file with eight slots: slot 1 empty, slot 2 holds 4417, slot 3 empty, slot 4 holds 2171, slot 5 holds 9308, slot 6 holds 6045, slot 7 holds 1052 and slot 8 holds 7734.",
             "The same six account numbers in three organisations. In the random file each key goes to its key MOD 8, plus 1; 1052 and 7734 found their slots taken and moved on to the next free one (the two darker boxes). Slots 1 and 3 stay empty."))
print(table, {k: v + 1 for k, v in home.items()})

# ---- Figure 2: the 11-slot file after the worked example --------------------------------------
KEYS = [4023, 5117, 2064, 8830, 1479, 3306, 7712, 4045]
N = 11
tab = [None] * N
hm = {}
for k in KEYS:
    a = k % N
    hm[k] = a
    while tab[a] is not None:
        a = (a + 1) % N
    tab[a] = k
f2 = Fig("hashtable", 330, 300)
f2.text("tl ti", 20, 16, "Random file of 11 slots")
for i in range(N):
    y = 26 + 24 * i
    k = tab[i]
    cls = "fp s-acc sw2" if k is None else ("f1 s-acc sw2" if hm[k] != i else "fm s-acc sw2")
    f2.rect(cls, 50, y, 90, 24)
    f2.text("tl te", 40, y + 17, str(i + 1))
    f2.text("tl tc", 95, y + 17, "empty" if k is None else str(k))
    if k is not None and hm[k] != i:
        f2.text("tl", 152, y + 17, f"home slot {hm[k] + 1}")
print(f2.svg("A column of eleven slots numbered 1 to 11 holding account numbers: slot 2 holds 7712, slot 3 holds 5117, slot 6 holds 1479, slot 7 holds 3306, slot 8 holds 2064, slot 9 holds 4023, slot 10 holds 8830 and slot 11 holds 4045. Slots 1, 4 and 5 are empty. 8830 and 4045 are marked as having home slot 9.",
             "The file after eight keys are stored with the address Key MOD 11 + 1 and linear probing. 8830 and 4045 both hash to slot 9, which 4023 already holds, so they were placed in the next free slots, 10 and 11 (the two darker boxes)."))
print(tab, {k: v + 1 for k, v in hm.items()})

# ---- Figure 3: a pointer --------------------------------------------------------------------
f3 = Fig("pointer", 340, 140)
f3.text("tl ti", 20, 16, "Memory")
f3.rect("fm s-acc sw2", 20, 40, 100, 36)
f3.text("tl tc tb", 70, 63, "3012")
f3.text("tl tc", 70, 98, "Ptr")
f3.rect("fm s-acc sw2", 220, 40, 100, 36)
f3.text("tl tc tb", 270, 63, "40")
f3.text("tl tc", 270, 98, "Score")
f3.text("tl tc", 270, 30, "address 3012")
f3.line("c1 sw2", "M 120 58 L 212 58", marker=True)
f3.text("tl tc", 166, 48, "points to")
f3.text("tl tc", 70, 126, "Ptr holds an address")
f3.text("tl tc", 270, 126, "Ptr^ is 40")
print(f3.svg("A box called Ptr holds the number 3012. An arrow labelled points to runs from it to a box called Score at address 3012, which holds the value 40. Under the pointer box: Ptr holds an address. Under the Score box: Ptr^ is 40.",
             "A pointer holds an address, not a value. Following the pointer (Ptr^) gives the value stored at that address, here 40."))
