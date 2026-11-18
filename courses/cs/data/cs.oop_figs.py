# data/cs.oop_figs.py: builds the two class-diagram SVGs of chapters/cs.oop.md (vertical, phone-friendly) and checks them.
# Run: py -X utf8 data/cs.oop_figs.py > scratch/oop_figs.txt   (prints the SVG blocks to paste into the chapter)
from itertools import combinations

CHAR = 7.0  # px per character of a 13 px label
LH = 18     # line height inside a compartment


def overlap(a, b, gap=4):
    return not (a[2] + gap <= b[0] or b[2] + gap <= a[0] or a[3] + gap <= b[1] or b[3] + gap <= a[1])


def class_box(out, boxes, x, y, w, name, attrs, methods):
    h_name, h_attr, h_meth = 28, len(attrs) * LH + 10, len(methods) * LH + 10
    h = h_name + h_attr + h_meth
    out.append(f'<rect class="fm s-acc sw2" x="{x}" y="{y}" width="{w}" height="{h}"/>')
    out.append(f'<line class="ln" x1="{x}" y1="{y + h_name}" x2="{x + w}" y2="{y + h_name}"/>')
    out.append(f'<line class="ln" x1="{x}" y1="{y + h_name + h_attr}" x2="{x + w}" y2="{y + h_name + h_attr}"/>')
    out.append(f'<text class="tl tb tc" x="{x + w / 2:g}" y="{y + 19}">{name}</text>')
    for i, a in enumerate(attrs):
        ty = y + h_name + 16 + i * LH
        out.append(f'<text class="tl" x="{x + 10}" y="{ty}">{a}</text>')
        assert len(a) * CHAR + 20 <= w, (a, w)
    for i, m in enumerate(methods):
        ty = y + h_name + h_attr + 16 + i * LH
        out.append(f'<text class="tl" x="{x + 10}" y="{ty}">{m}</text>')
        assert len(m) * CHAR + 20 <= w, (m, w)
    boxes.append((x, y, x + w, y + h))
    return (x, y, w, h)


# ------------------- Figure 1: Pet, Cat and Dog (vertical) -------------------
W1 = 350
out1, boxes1 = [], []
BX, BW = 36, 300
pet = class_box(out1, boxes1, BX, 12, BW, "Pet",
                ["− Name : STRING", "− Age : INTEGER"],
                ["+ NEW(GivenName, GivenAge)", "+ GetName() : STRING", "+ GetAge() : INTEGER", "+ SetAge(NewAge : INTEGER)", "+ Speak() : STRING"])
pet_bottom = pet[1] + pet[3]
cat = class_box(out1, boxes1, BX, pet_bottom + 56, BW, "Cat",
                ["− Breed : STRING"],
                ["+ NEW(GivenName, GivenAge, GivenBreed)", "+ GetBreed() : STRING", "+ Speak() : STRING"])
cat_bottom = cat[1] + cat[3]
dog = class_box(out1, boxes1, BX, cat_bottom + 32, BW, "Dog",
                ["− Trained : BOOLEAN"],
                ["+ NEW(GivenName, GivenAge, TrainedFlag)", "+ IsTrained() : BOOLEAN", "+ Speak() : STRING"])
H1 = dog[1] + dog[3] + 12
spine = 12
pet_mid = pet[1] + 20      # inside the name compartment
cat_mid = cat[1] + 14
dog_mid = dog[1] + 14
arrow_cat = f'<path class="ln" d="M{BX},{cat_mid} L{spine},{cat_mid} L{spine},{pet_mid} L{BX},{pet_mid}" fill="none" marker-end="url(#ah)"/>'
arrow_dog = f'<path class="ln" d="M{BX},{dog_mid} L{spine},{dog_mid} L{spine},{cat_mid}" fill="none"/>'
label_y = pet_bottom + 34
label1 = f'<text class="tl" x="{BX + 10}" y="{label_y}">Cat and Dog inherit from Pet</text>'
lab = (BX + 10, label_y - 10, BX + 10 + 28 * CHAR, label_y + 3)
for b in boxes1:
    assert not overlap(lab, b, 4), (lab, b)
assert lab[0] - 4 > spine
for a, b in combinations(boxes1, 2):
    assert not overlap(a, b, 4)
assert spine >= 8 and BX - spine >= 20  # the arrow's last segment is long enough for its head
svg1 = (f'<svg viewBox="0 0 {W1} {H1:g}" role="img" aria-label="A class diagram. The class Pet has private attributes Name (STRING) and Age (INTEGER) and public methods NEW, GetName, GetAge, SetAge and Speak. '
        f'Below it, the class Cat has the private attribute Breed (STRING) and the public methods NEW, GetBreed and Speak, and the class Dog has the private attribute Trained (BOOLEAN) and the public methods NEW, IsTrained and Speak. '
        f'A line down the left side joins Cat and Dog to an arrow that points at Pet, labelled Cat and Dog inherit from Pet.">'
        + "".join(out1) + arrow_cat + arrow_dog + label1 + "</svg>")

# ------------------- Figure 2: Library contains Book (vertical) -------------------
W2 = 300
out2, boxes2 = [], []
lib = class_box(out2, boxes2, 25, 12, 250, "Library",
                ["− Name : STRING", "− Books : ARRAY OF Book"],
                ["+ NEW(GivenName)", "+ AddBook(NewBook : Book)", "+ CountOnLoan() : INTEGER"])
lib_bottom = lib[1] + lib[3]
dx = 150
diamond = f'<polygon class="fp s-acc sw2" points="{dx},{lib_bottom} {dx + 8},{lib_bottom + 12} {dx},{lib_bottom + 24} {dx - 8},{lib_bottom + 12}"/>'
book_top = lib_bottom + 24 + 42
book = class_box(out2, boxes2, 25, book_top, 250, "Book",
                 ["− Title : STRING", "− Author : STRING", "− OnLoan : BOOLEAN"],
                 ["+ NEW(GivenTitle, GivenAuthor)", "+ GetTitle() : STRING", "+ IsOnLoan() : BOOLEAN", "+ Borrow() : BOOLEAN"])
line = f'<line class="ln" x1="{dx}" y1="{lib_bottom + 24}" x2="{dx}" y2="{book_top}"/>'
ly = lib_bottom + 24 + 26
lab2 = f'<text class="tl halo" x="{dx + 12}" y="{ly}">contains many</text>'
lb = (dx + 12, ly - 10, dx + 12 + 13 * CHAR, ly + 3)
assert lb[0] - 4 > dx and lb[2] < W2 - 4 and lb[1] > lib_bottom + 24 and lb[3] < book_top
H2 = book[1] + book[3] + 12
for a, b in combinations(boxes2, 2):
    assert not overlap(a, b, 4)
svg2 = (f'<svg viewBox="0 0 {W2} {H2:g}" role="img" aria-label="A class diagram showing containment. The class Library has private attributes Name (STRING) and Books (an array of Book) and public methods NEW, AddBook and CountOnLoan. '
        f'Below it, the class Book has private attributes Title, Author and OnLoan and public methods NEW, GetTitle, IsOnLoan and Borrow. A line with a diamond at the Library end, labelled contains many, joins Library to Book: a Library contains many Books.">'
        + "".join(out2) + line + diamond + lab2 + "</svg>")
print("FIGURE 1\n" + svg1 + "\n\nFIGURE 2\n" + svg2 + "\n\ngeometry ok")
