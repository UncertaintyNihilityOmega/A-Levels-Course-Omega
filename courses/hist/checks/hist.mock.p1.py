# checks/hist.mock.p1.py: recomputes every number in Mock Paper 1 (marks, time, source word counts, level ranges, dates)
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 1: 40 marks = (a) 15 + (b) 25; 1 h 15 min = 75 min; the time plan sums to 75
eq("total marks", 15 + 25, 40)
eq("paper minutes", 1 * 60 + 15, 75)
eq("time plan total", sum([8, 20, 4, 38, 5]), 75)
eq("part (a) plan + write", 2 + 18, 20)

# Table A (part (a)) and Table B (part (b)) levels: contiguous, top marks 15 and 25
A = {4: (12, 15), 3: (8, 11), 2: (4, 7), 1: (1, 3)}
B = {5: (21, 25), 4: (16, 20), 3: (11, 15), 2: (6, 10), 1: (1, 5)}
for name, table, top in (("A", A, 15), ("B", B, 25)):
    hi = top
    for lvl in sorted(table, reverse=True):
        lo, h = table[lvl]
        eq(f"Table {name} level {lvl} top", h, hi)
        hi = lo - 1
    eq(f"Table {name} bottom", hi, 0)

# The chapter file: every question is 40 marks, its sources total at most 600 words, at least 3 written
text = (Path(__file__).resolve().parent.parent / "chapters" / "hist.mock.p1.md").read_text(encoding="utf-8")
qs = re.findall(r"^Q: \[(\d+) marks\].*?(?=^A: )", text, flags=re.S | re.M)
eq("number of questions", len(qs), 3)
blocks = re.split(r"^Q: \[\d+ marks\]", text, flags=re.M)[1:]
for i, b in enumerate(blocks, 1):
    b = b.split("\nA: ")[0]
    parts = re.split(r"\*\*Source ([A-D])\*\*\n\n", b)[1:]
    srcs = []
    for k in range(0, len(parts), 2):
        body = parts[k + 1].split("\n\n")[0]
        srcs.append((parts[k], body))
    eq(f"Q{i} sources", [s[0] for s in srcs], ["A", "B", "C", "D"])
    words = [len(s[1].split()) for s in srcs]
    assert sum(words) <= 600, f"Q{i}: sources total {sum(words)} words, more than 600"
    print(f"Q{i} source words {words} total {sum(words)}")
    eq(f"Q{i} part (a) marks", int(re.search(r"\(a\).*?\[(\d+)\]", b).group(1)), 15)
    eq(f"Q{i} part (b) marks", int(re.search(r"\(b\).*?\[(\d+)\]", b, flags=re.S).group(1)), 25)

# Dates used in the mark scheme
# Section A: flight to Varennes 20-21 June 1791; Champ de Mars 17 July 1791; Legislative Assembly met 1 October 1791
eq("flight to Varennes lasts one night", (date(1791, 6, 21) - date(1791, 6, 20)).days, 1)
eq("Varennes to Champ de Mars (days)", (date(1791, 7, 17) - date(1791, 6, 21)).days, 26)
eq("address to the King was 29 Nov 1791, 59 days after the Assembly met", (date(1791, 11, 29) - date(1791, 10, 1)).days, 59)
eq("Roland letter to 10 August 1792 (roughly two months)", (date(1792, 8, 10) - date(1792, 6, 13)).days, 58)
eq("Brunswick Manifesto to 10 August", (date(1792, 8, 10) - date(1792, 7, 25)).days, 16)
# Section B: Pullman strike
eq("troops sent 4 July, proclamation 8 July (days)", (date(1894, 7, 8) - date(1894, 7, 4)).days, 4)
eq("proclamation to Altgeld letter (about six weeks)", (date(1894, 8, 19) - date(1894, 7, 8)).days, 42)
eq("six weeks", 6 * 7, 42)
eq("strike began 11 May, boycott 26 June (days)", (date(1894, 6, 26) - date(1894, 5, 11)).days, 46)
eq("workers' appeal 17 Aug, Altgeld letter 19 Aug", (date(1894, 8, 19) - date(1894, 8, 17)).days, 2)
# Section C: Fashoda, 10 July and 19 September 1898; Blunt's entry 17 October
eq("Marchand at Fashoda before Kitchener (days)", (date(1898, 9, 19) - date(1898, 7, 10)).days, 71)
eq("Kitchener at Fashoda to the diary entry (days)", (date(1898, 10, 17) - date(1898, 9, 19)).days, 28)
eq("Paton letter 1883 to the 1887 commission", 1887 - 1883, 4)
eq("Paton letter 1883 to the 1906 condominium", 1906 - 1883, 23)
eq("Livingstone's Cambridge lecture 1857 to Ferry 1885", 1885 - 1857, 28)
print("ok")
