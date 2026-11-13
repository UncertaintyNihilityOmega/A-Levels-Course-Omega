# data/cs.databases_fig.py: draws the E-R figures of cs.databases (crow's foot notation) and checks label boxes.
# Run: py data/cs.databases_fig.py > scratch/db_figs.txt   (prints each figure's <svg> and any problems found)
import sys

CH = 7.0   # px per character of a 13 px label
problems = []


class Fig:
    def __init__(self, name, w, h, label):
        self.name, self.w, self.h, self.label = name, w, h, label
        self.parts, self.lines, self.texts, self.rects = [], [], [], []

    def line(self, x1, y1, x2, y2, cls="ln"):
        self.parts.append(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
        self.lines.append((x1, y1, x2, y2))

    def rect(self, x, y, w, h, cls="fm s-acc sw2"):
        self.parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}"/>')
        self.rects.append((x, y, w, h))

    def text(self, x, y, s, cls="tl", anchor="middle"):
        c = {"middle": "tc", "start": "", "end": "te"}[anchor]
        full = (cls + " " + c).strip()
        self.parts.append(f'<text class="{full}" x="{x}" y="{y}">{s}</text>')
        wd = len(s.replace("&amp;", "&")) * CH
        x0 = x - wd / 2 if anchor == "middle" else (x if anchor == "start" else x - wd)
        self.texts.append((x0, y - 10, x0 + wd, y + 3, s))

    def entity(self, x, y, w, title, attrs):
        """A table box: title row then one row per attribute (name, tag). Returns the box (x, y, w, h)."""
        rowh = 20
        h = 26 + rowh * len(attrs)
        self.rect(x, y, w, h)
        self.text(x + w / 2, y + 18, title, "tl tb")
        self.line(x, y + 26, x + w, y + 26)
        for i, (name, tag) in enumerate(attrs):
            ty = y + 26 + 15 + rowh * i
            self.text(x + 8, ty, name, "tl", "start")
            if tag:
                self.text(x + w - 8, ty, tag, "tl te", "end")
        return (x, y, w, h)

    def box(self, x, y, w, h, title):
        self.rect(x, y, w, h)
        self.text(x + w / 2, y + h / 2 + 5, title, "tl tb")
        return (x, y, w, h)

    # cardinality ends: (px, py) is the point on the box edge, d = (dx, dy) the unit direction away from the box
    def one(self, px, py, d):
        dx, dy = d
        bx, by = px + dx * 12, py + dy * 12
        if dx:
            self.line(bx, by - 8, bx, by + 8)
        else:
            self.line(bx - 8, by, bx + 8, by)

    def many(self, px, py, d):
        dx, dy = d
        tx, ty = px + dx * 16, py + dy * 16     # the point where the three prongs meet
        if dx:
            for off in (-9, 0, 9):
                self.line(px, py + off, tx, ty)
        else:
            for off in (-9, 0, 9):
                self.line(px + off, py, tx, ty)

    def svg(self, cls="fig small"):
        body = "".join(self.parts)
        return (f'<figure class="{cls}"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.label}">'
                f'{body}</svg><figcaption>@@CAPTION@@</figcaption></figure>')

    def verify(self):
        # every text box inside the viewBox, clear of rect edges' lines by 4 px, and not overlapping another text
        for i, (a0, b0, a1, b1, s) in enumerate(self.texts):
            if a0 < 0 or b0 < 0 or a1 > self.w or b1 > self.h:
                problems.append(f"{self.name}: text {s!r} outside the viewBox ({a0:.0f},{b0:.0f},{a1:.0f},{b1:.0f})")
            for j, (c0, d0, c1, d1, t) in enumerate(self.texts[i + 1:], i + 1):
                if a0 < c1 + 4 and c0 < a1 + 4 and b0 < d1 + 4 and d0 < b1 + 4:
                    problems.append(f"{self.name}: texts overlap {s!r} / {t!r}")
            for (x1, y1, x2, y2) in self.lines:
                lx0, lx1 = min(x1, x2) - 4, max(x1, x2) + 4
                ly0, ly1 = min(y1, y2) - 4, max(y1, y2) + 4
                if a0 < lx1 and lx0 < a1 and b0 < ly1 and ly0 < b1:
                    problems.append(f"{self.name}: text {s!r} within 4 px of line {(x1, y1, x2, y2)}")
            for (rx, ry, rw, rh) in self.rects:
                # text that straddles a box edge (partly inside) is a problem; wholly inside or outside is fine
                inside = a0 >= rx - 1 and a1 <= rx + rw + 1 and b0 >= ry - 1 and b1 <= ry + rh + 1
                outside = a1 < rx - 4 or a0 > rx + rw + 4 or b1 < ry - 4 or b0 > ry + rh + 4
                if not inside and not outside:
                    problems.append(f"{self.name}: text {s!r} straddles a box edge {(rx, ry, rw, rh)}")
        for (x, y, w, h) in self.rects:
            if x < 0 or y < 0 or x + w > self.w or y + h > self.h:
                problems.append(f"{self.name}: rect outside viewBox {(x, y, w, h)}")


def fig_types():
    f = Fig("types", 340, 244, "Three small entity-relationship diagrams in crow's foot notation. One-to-one: STUDENT and LOCKER joined by a line with a single bar at each end. One-to-many: FORM and STUDENT, a bar at the FORM end and a crow's foot at the STUDENT end. Many-to-many: STUDENT and CLUB, a crow's foot at both ends.")
    rows = [("STUDENT", "LOCKER", "one", "one", "one-to-one", "one student has one locker"),
            ("FORM", "STUDENT", "one", "many", "one-to-many", "one form has many students"),
            ("STUDENT", "CLUB", "many", "many", "many-to-many", "each side has many of the other")]
    for i, (a, b, ea, eb, name, sentence) in enumerate(rows):
        y0 = 12 + 78 * i
        ym = y0 + 18
        f.box(20, y0, 80, 36, a)
        f.box(240, y0, 80, 36, b)
        f.line(100, ym, 240, ym)
        (f.one if ea == "one" else f.many)(100, ym, (1, 0))
        (f.one if eb == "one" else f.many)(240, ym, (-1, 0))
        f.text(170, y0 + 12 - 2, name, "tl")
        f.text(170, y0 + 58, sentence if len(sentence) < 44 else sentence, "tl")
    f.verify()
    return f


def fig_manymany():
    f = Fig("manymany", 580, 188, "Two diagrams. Top: STUDENT and CLUB joined directly with a crow's foot at both ends, labelled many-to-many and marked as not allowed in a relational database. Bottom: the same data with a link table MEMBERSHIP between them: STUDENT has a bar and MEMBERSHIP a crow's foot on one side, CLUB has a bar and MEMBERSHIP a crow's foot on the other.")
    f.box(20, 12, 120, 36, "STUDENT")
    f.box(440, 12, 120, 36, "CLUB")
    f.line(140, 30, 440, 30)
    f.many(140, 30, (1, 0))
    f.many(440, 30, (-1, 0))
    f.text(290, 20, "many-to-many", "tl")
    f.text(290, 50, "cannot be stored directly", "tl")
    f.text(290, 78, "so split it with a link table", "tl")
    y = 116
    f.box(20, y, 120, 36, "STUDENT")
    f.box(220, y, 140, 36, "MEMBERSHIP")
    f.box(440, y, 120, 36, "CLUB")
    f.line(140, y + 18, 220, y + 18)
    f.one(140, y + 18, (1, 0))
    f.many(220, y + 18, (-1, 0))
    f.line(360, y + 18, 440, y + 18)
    f.many(360, y + 18, (1, 0))
    f.one(440, y + 18, (-1, 0))
    f.text(290, y + 62, "two one-to-many relationships", "tl")
    f.verify()
    return f


def fig_orders():
    f = Fig("orders", 560, 262, "Entity-relationship diagram of four tables in crow's foot notation. CUSTOMER (CustomerID primary key, CustomerName, City) has a one-to-many relationship with ORDERS (OrderID primary key, OrderDate, CustomerID foreign key). ORDERS has a one-to-many relationship with ORDERLINE (OrderID and ProductID, both primary key and foreign key, and Quantity). PRODUCT (ProductID primary key, ProductName, UnitPrice) has a one-to-many relationship with ORDERLINE.")
    c = f.entity(20, 14, 190, "CUSTOMER", [("CustomerID", "PK"), ("CustomerName", ""), ("City", "")])
    o = f.entity(340, 14, 200, "ORDERS", [("OrderID", "PK"), ("OrderDate", ""), ("CustomerID", "FK")])
    p = f.entity(20, 160, 190, "PRODUCT", [("ProductID", "PK"), ("ProductName", ""), ("UnitPrice", "")])
    ol = f.entity(340, 160, 200, "ORDERLINE", [("OrderID", "PK, FK"), ("ProductID", "PK, FK"), ("Quantity", "")])
    ym = 14 + 40
    f.line(210, ym, 340, ym)
    f.one(210, ym, (1, 0))
    f.many(340, ym, (-1, 0))
    f.text(275, ym - 8, "places", "tl")
    xm = 440
    f.line(xm, o[1] + o[3], xm, ol[1])
    f.one(xm, o[1] + o[3], (0, 1))
    f.many(xm, ol[1], (0, -1))
    f.text(xm + 10, 132, "contains", "tl", "start")
    yb = 160 + 40
    f.line(210, yb, 340, yb)
    f.one(210, yb, (1, 0))
    f.many(340, yb, (-1, 0))
    f.text(275, yb - 8, "is sold on", "tl")
    f.verify()
    return f


def fig_library():
    f = Fig("library", 370, 78, "Entity-relationship diagram: MEMBER has a one-to-many relationship with LOAN (bar at MEMBER, crow's foot at LOAN), and BOOK has a one-to-many relationship with LOAN (bar at BOOK, crow's foot at LOAN).")
    f.box(10, 20, 90, 36, "MEMBER")
    f.box(140, 20, 90, 36, "LOAN")
    f.box(270, 20, 90, 36, "BOOK")
    f.line(100, 38, 140, 38)
    f.one(100, 38, (1, 0))
    f.many(140, 38, (-1, 0))
    f.line(230, 38, 270, 38)
    f.many(230, 38, (1, 0))
    f.one(270, 38, (-1, 0))
    f.verify()
    return f


if __name__ == "__main__":
    caps = {"types": "The three kinds of relationship. The bar means one; the crow's foot (three prongs) means many.",
            "manymany": "A many-to-many relationship is resolved by a link table that holds a foreign key to each side.",
            "orders": "The finished design from the order example: four tables, linked by foreign keys.",
            "library": "One member makes many loans, and one book appears in many loans."}
    for fn in (fig_types, fig_manymany, fig_orders, fig_library):
        f = fn()
        print(f"=== {f.name}")
        print(f.svg("fig small" if f.w < 420 else "fig").replace("@@CAPTION@@", caps[f.name]))
    print("PROBLEMS:" if problems else "no problems")
    for p in problems:
        print(" ", p)
