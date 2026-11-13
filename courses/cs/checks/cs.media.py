# checks/cs.media.py: runs every Python block in the chapter, and recomputes every number the chapter
# states (bitmap and sound sizes, colour counts, RLE codes and sizes, the sampled waveform of the figure).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.media"

# ---------------------------------------------------------------------------------------------
# Helper (copy unchanged into every checks file of this course; only CHAPTER_ID and INPUTS change)
# ---------------------------------------------------------------------------------------------
CHAPTER = pathlib.Path(__file__).resolve().parent.parent / "chapters" / f"{CHAPTER_ID}.md"
TEXT = CHAPTER.read_text(encoding="utf-8")
FENCES = list(re.finditer(r"^```(\w+)\n(.*?)^```", TEXT, re.S | re.M))


def run_python_blocks(inputs):
    """Run each ```python block in a fresh namespace inside a temporary folder.
    inputs: list of (text found in the block, [values the user types]). Typed values are echoed after
    the prompt, as a console shows them. If the next fence after a python block is ```output, the
    printed text must match it exactly (trailing spaces ignored)."""
    ran = 0
    with tempfile.TemporaryDirectory() as tmp:
        old = os.getcwd()
        os.chdir(tmp)
        try:
            for i, f in enumerate(FENCES):
                if f.group(1) != "python":
                    continue
                code = f.group(2)
                ran += 1
                typed = list(next((v for key, v in inputs if key in code), []))
                out = io.StringIO()

                def fake_input(prompt=""):
                    assert typed, f"python block {ran}: input() called but no typed value left"
                    value = typed.pop(0)
                    out.write(str(prompt) + value + "\n")
                    return value

                namespace = {"__name__": "__main__", "input": fake_input}
                with contextlib.redirect_stdout(out):
                    exec(compile(code, f"{CHAPTER_ID} python block {ran}", "exec"), namespace)
                assert not typed, f"python block {ran}: typed values not used: {typed}"
                nxt = FENCES[i + 1] if i + 1 < len(FENCES) else None
                if nxt is not None and nxt.group(1) == "output":
                    got = [line.rstrip() for line in out.getvalue().rstrip("\n").split("\n")]
                    want = [line.rstrip() for line in nxt.group(2).rstrip("\n").split("\n")]
                    assert got == want, f"python block {ran}: printed {got}, chapter shows {want}"
        finally:
            os.chdir(old)
    return ran


PAIRS = [("IF", "ENDIF"), ("WHILE", "ENDWHILE"), ("FOR", "NEXT"), ("REPEAT", "UNTIL"),
         ("CASE OF", "ENDCASE"), ("PROCEDURE", "ENDPROCEDURE"), ("FUNCTION", "ENDFUNCTION"),
         ("CLASS", "ENDCLASS")]


def lint_pseudocode_blocks():
    """Light checks on ```pseudocode blocks: Cambridge symbols, no Python syntax, balanced
    structures (blocks that are deliberate fragments contain a line '...' and skip the balance test)."""
    n = 0
    for f in FENCES:
        if f.group(1) != "pseudocode":
            continue
        n += 1
        code = f.group(2)
        lines = [re.sub(r"^\s*\d+\s{2,}", "", ln).split("//")[0] for ln in code.split("\n")]
        body = "\n".join(lines)
        for bad in ("<-", "==", "!=", "print(", "elif", "range(", "True", "False", "\t"):
            assert bad not in body, f"pseudocode block {n}: contains {bad!r}"
        if any(ln.strip() == "..." for ln in lines):
            continue
        words = [ln.strip() for ln in lines]
        for start, end in PAIRS:
            if start == "FOR":
                opened = sum(1 for w in words if re.match(r"FOR \w+ ←", w))
            elif start == "CASE OF":
                opened = sum(1 for w in words if w.startswith("CASE OF"))
            elif start in ("PROCEDURE", "FUNCTION"):
                opened = sum(1 for w in words if re.match(rf"(PUBLIC |PRIVATE )?{start} ", w))
            else:
                opened = sum(1 for w in words if re.match(rf"{start}\b", w))
            closed = sum(1 for w in words if re.match(rf"{end}\b", w))
            # a block of four lines or fewer may be a fragment (for example a corrected swap)
            assert opened == closed or len(words) <= 4, f"pseudocode block {n}: {start}/{end} {opened}/{closed}"
        types = sum(1 for w in words if re.match(r"TYPE \w+\s*$", w))
        assert types == sum(1 for w in words if w.startswith("ENDTYPE")), f"pseudocode block {n}: TYPE/ENDTYPE"
    return n


def table_after(marker):
    """Rows of the first Markdown table after the text marker, as lists of cell strings."""
    start = TEXT.index(marker)
    rows = []
    for line in TEXT[start:].split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
        elif rows:
            break
    return rows[0], rows[1:]


def column_values(header, rows, name):
    k = header.index(name)
    return [r[k] for r in rows if r[k] != ""]




import math


def bitmap_bits(w, h, depth):
    return w * h * depth


def sound_bits(rate, res, secs, channels=1):
    return rate * res * secs * channels


def rle(data):
    runs = []
    for item in data:
        if runs and runs[-1][1] == item:
            runs[-1][0] += 1
        else:
            runs.append([1, item])
    return runs


def rle_text(data):
    return "".join(str(c) + i for c, i in rle(data))


def unrle(runs):
    return "".join(i * c for c, i in runs)


blocks = run_python_blocks([])
assert blocks == 4, f"expected 4 python blocks, found {blocks}"

# --- Warm-up -------------------------------------------------------------------------------
assert 4 * 1024 == 4096 and 2 ** 3 == 8 and int("1011", 2) == 11 and format(11, "X") == "B"

# --- Colour depth --------------------------------------------------------------------------------
header, rows = table_after("| Colour depth (bits) |")
assert [int(x) for x in header[1:]] == [1, 2, 4, 8, 16, 24]
assert [int(x.replace(" ", "")) for x in rows[0][1:]] == [2 ** d for d in [1, 2, 4, 8, 16, 24]]
assert (2 ** 7, 2 ** 8) == (128, 256) and 2 ** 7 < 200 <= 2 ** 8
assert 2 ** 24 == 16777216 and 24 // 8 == 3

# --- The 4 x 4 image -----------------------------------------------------------------------------------
grid = [["00", "00", "01", "01"], ["00", "10", "10", "01"], ["11", "10", "10", "00"], ["11", "11", "00", "00"]]
header, rows = table_after("| | Column 1 | Column 2 |")
assert [r[1:] for r in rows] == grid
assert ["".join(r) for r in grid] == ["00000101", "00101001", "11101000", "11110000"]
assert [f"{r[0]} {r[1]}" for r in [("0000", "0101"), ("0010", "1001"), ("1110", "1000"), ("1111", "0000")]] == \
    [f"{''.join(r)[:4]} {''.join(r)[4:]}" for r in grid]
assert 4 * 4 == 16 and bitmap_bits(4, 4, 2) == 32 and 32 // 8 == 4

# --- Bitmap sizes ----------------------------------------------------------------------------------------
bits = bitmap_bits(1024, 768, 24)
assert 1024 * 768 == 786432 and 786432 * 3 == 2359296 == bits // 8
assert bits // 8 / 1024 == 2304 and 2304 / 1024 == 2.25
assert 1024 == 2 ** 10 and 768 == 3 * 2 ** 8 and 2 ** 10 * 3 * 2 ** 8 * 3 == 9 * 2 ** 18 and 9 * 2 ** 8 == 2304
# changing the settings
b640 = bitmap_bits(640, 480, 16)
assert b640 == 4915200 and b640 // 8 == 614400 and 614400 / 1024 == 600
assert bitmap_bits(320, 240, 16) // 8 / 1024 == 150 == 600 / 4
assert bitmap_bits(640, 480, 8) // 8 / 1024 == 300 == 600 / 2
# spot the error
assert 800 * 600 * 24 == 11520000 and 11520000 / 1024 == 11250.0
assert 11520000 // 8 == 1440000 and 1440000 / 1024 == 1406.25 and 11250 / 1406.25 == 8

# --- Sound ----------------------------------------------------------------------------------------------------
levels = [round((math.sin(2 * math.pi * t / 12) + 1) / 2 * 7) for t in range(12)]
assert levels == [4, 5, 7, 7, 7, 5, 4, 2, 0, 0, 0, 2]
# the figure's stepped path and sample points come from the same numbers (data/cs.media_fig.py)
x0, x1, ytop, ybot = 36, 316, 30, 150
assert [round(ybot - (ybot - ytop) * lv / 7, 1) for lv in levels[:4]] == [81.4, 64.3, 30.0, 30.0]
assert 'M36.0,81.4 H59.3 V64.3 H82.7 V30.0' in TEXT and round(x0 + (x1 - x0) * 1 / 12, 1) == 59.3
assert sound_bits(8000, 16, 60) == 7680000 and 7680000 // 8 == 960000 and 960000 / 1024 == 937.5
assert sound_bits(8000, 16, 60, 2) // 8 == 1920000
assert sound_bits(44100, 16, 180, 2) // 8 == 31752000

# --- Compression ------------------------------------------------------------------------------------------------
assert rle_text("WWWWWWWBBBBBWWWW") == "7W5B4W" and len("WWWWWWWBBBBBWWWW") == 16 == 7 + 5 + 4
assert rle("WWWWWWWBBBBBWWWW") == [[7, "W"], [5, "B"], [4, "W"]]
assert unrle(rle("WWWWWWWBBBBBWWWW")) == "WWWWWWWBBBBBWWWW"
assert rle("ABCD") == [[1, "A"], [1, "B"], [1, "C"], [1, "D"]]
# the 12 x 5 figure
img = ["LLLLLLLLLLLL", "LLLLDDDDLLLL", "LLDDDDDDDDLL", "LLLLDDDDLLLL", "LLLLLLLLLLLL"]
assert [rle_text(r) for r in img] == ["12L", "4L4D4L", "2L8D2L", "4L4D4L", "12L"]
runs_total = sum(len(rle(r)) for r in img)
assert runs_total == 11 and 12 * 5 == 60 and 60 * 8 == 480 and 11 * (8 + 8) == 176
assert round(176 / 480 * 100) == 37
alt = "WBWBWBWBWBWBWBWB"
assert len(rle(alt)) == 16 and 16 * 8 == 128 and 16 * 16 == 256 == 2 * 128
for row_text in ["4L 4D 4L", "2L 8D 2L", "12L"]:
    assert row_text in TEXT
# RLE on text
assert rle_text("AAAABBBCCD") == "4A3B2C1D" and len("4A3B2C1D") == 8 and len("AAAABBBCCD") == 10
assert unrle([[3, "X"], [1, "Y"], [4, "Z"]]) == "XXXYZZZZ" and rle_text("ABCD") == "1A1B1C1D"
assert rle_text("AAABBBBCCA") == "3A4B2C1A" and unrle([[3, "A"], [4, "B"], [2, "C"]]) == "AAABBBBCC"
# dictionary example
d = {"to": "1", "be": "2"}
assert " ".join(d.get(w, w) for w in "to be or not to be".split()) == "1 2 or not 1 2"

# --- Try yourself -----------------------------------------------------------------------------------------------
assert 2 ** 5 == 32 and 2 ** 6 < 100 <= 2 ** 7
assert bitmap_bits(100, 50, 1) == 5000 and 5000 / 8 == 625
assert bitmap_bits(4, 4, 3) == 48 and 48 // 8 == 6
assert 1920 * 1080 == 2073600 and 1920 * 1000 + 1920 * 80 == 2073600
assert sound_bits(10000, 8, 5) == 400000 and 400000 // 8 == 50000
assert rle_text("AAAAABBC") == "5A2B1C" and unrle([[2, "X"], [3, "Y"], [1, "Z"]]) == "XXYYYZ"
assert (20 * 3, 30 * 3, 10 * 3) == (60, 90, 30)

# --- Exam practice ----------------------------------------------------------------------------------------------
assert bitmap_bits(1280, 720, 8) == 7372800 and 7372800 // 8 == 921600 and 921600 / 1024 == 900 and 900 * 2 == 1800
assert sound_bits(16000, 8, 20) == 2560000 and 2560000 // 8 == 320000 and 320000 / 1024 == 312.5
assert rle_text("WWWWBBWWWWWWWWBB") == "4W2B8W2B" and len("WWWWBBWWWWWWWWBB") == 16 and unrle([[3, "R"], [5, "G"], [4, "R"]]) == "RRRGGGGGRRRR"
assert 2048 == 2 ** 11 and 1024 == 2 ** 10 and bitmap_bits(2048, 1024, 4) == 8388608 == 2 ** 23
assert 8388608 // 8 == 1048576 == 2 ** 20 and 1048576 / 1024 / 1024 == 1 and 2 ** 4 == 16
assert bitmap_bits(1024, 512, 4) // 8 / 1024 == 256 == 1024 / 4
# Stretch
assert 40 + 24 == 64 and 2 * 9 == 18 and 64 * 9 == 576 and 576 / 64 == 9
assert (2 * 1) * (1 / 2) == 1 and sound_bits(16000, 8, 10) == sound_bits(8000, 16, 10)
# quiz
assert 2 ** 8 == 256 and bitmap_bits(100, 50, 2) == 10000 and 10000 // 8 == 1250
assert 8000 * 16 == 128000

print("ok")
