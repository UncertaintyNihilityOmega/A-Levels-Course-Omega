# checks/hist.mock.p3.py: recomputes every number in the chapter (paper facts, level ranges, extract lengths, dates, intervals)
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper: 1 h 15 min = 75 min; 40 marks = 20 + 20; plan 15 + 10 + 50 = 75; one question answered of three
eq("minutes", 1 * 60 + 15, 75)
eq("total", 20 + 20, 40)
eq("plan", 15 + 10 + 50, 75)

# Levels: six contiguous bands to 20 in each table; totals at the same level in both tables
A = {6: (18, 20), 5: (15, 17), 4: (12, 14), 3: (9, 11), 2: (5, 8), 1: (1, 4)}
prev = 21
for lvl in (6, 5, 4, 3, 2, 1):
    lo, hi = A[lvl]
    eq(f"level {lvl} contiguous", hi, prev - 1)
    prev = lo
eq("bottom", prev, 1)
want = {6: (36, 40), 5: (30, 34), 4: (24, 28), 3: (18, 22), 2: (10, 16), 1: (2, 8)}
for lvl, (lo, hi) in A.items():
    eq(f"both tables level {lvl}", (2 * lo, 2 * hi), want[lvl])

# Extract lengths: at most 600 words on the real paper; these say "about 450"
text = (Path(__file__).resolve().parent.parent / "chapters" / "hist.mock.p3.md").read_text(encoding="utf-8")
lens = []
for m in re.finditer(r"\*Practice extract ([ABC])\.[^\n]*\n\n(.*?)\n\nWhat can you learn", text, re.S):
    n = len(m.group(2).split())
    lens.append((m.group(1), n))
eq("three extracts found", [x for x, _ in lens], ["A", "B", "C"])
for k, n in lens:
    assert 360 <= n <= 520, f"extract {k} has {n} words (chapter says about 400 to 450; real paper at most 600)"
    assert n <= 600
print("extract words", lens)

# Section A dates
# Extract A (the timetable extract): the order of events and the gaps between them
eq("Sarajevo to blank cheque (days)", (date(1914, 7, 5) - date(1914, 6, 28)).days, 7)
eq("Sarajevo to Austrian ultimatum, 23 July (days)", (date(1914, 7, 23) - date(1914, 6, 28)).days, 25)
eq("ultimatum 23 July, reply 25 July: 48 hours", (date(1914, 7, 25) - date(1914, 7, 23)).days * 24, 48)
eq("Austria's declaration on Serbia, 28 July, is 30 days after Sarajevo", (date(1914, 7, 28) - date(1914, 6, 28)).days, 30)
eq("Russian partial (29 July) to general (30 July) mobilisation (days)", (date(1914, 7, 30) - date(1914, 7, 29)).days, 1)
eq("Russian general mobilisation ordered 30 July, effective 31 July (days)", (date(1914, 7, 31) - date(1914, 7, 30)).days, 1)
eq("German ultimatums 31 July to declaration on Russia 1 August (days)", (date(1914, 8, 1) - date(1914, 7, 31)).days, 1)
eq("German ultimatums 31 July to declaration on France 3 August (days)", (date(1914, 8, 3) - date(1914, 7, 31)).days, 3)
eq("Belgian ultimatum 2 August to Britain's war 4 August (days)", (date(1914, 8, 4) - date(1914, 8, 2)).days, 2)
eq("Sarajevo to Russian general mobilisation (days)", (date(1914, 7, 30) - date(1914, 6, 28)).days, 32)
eq("Schlieffen's memorandum 1905 to 1914 (years)", 1914 - 1905, 9)
eq("about six weeks in days", 6 * 7, 42)
eq("Treaty of London 1839 to 1914 (years)", 1914 - 1839, 75)
eq("War Council 8 December 1912 to the Eastern plan dropped 1913 to war 1914 (years)", (1913 - 1912, 1914 - 1913), (1, 1))
eq("Willy-Nicky telegrams 29 July to 1 August (days)", (date(1914, 8, 1) - date(1914, 7, 29)).days, 3)

# Section B dates and numbers
eq("Vel d'Hiv: 16-17 July 1942 is two days", (date(1942, 7, 17) - date(1942, 7, 16)).days + 1, 2)
eq("Vichy statute Oct 1940 to Vel d'Hiv (years)", 1942 - 1940, 2)
# Hungary: occupied 19 March 1944; deportations 15 May to 9 July 1944 = 55 days = under eight weeks
days = (date(1944, 7, 9) - date(1944, 5, 15)).days
eq("Hungary deportation days", days, 55)
assert days < 8 * 7
eq("occupation to first deportation (days)", (date(1944, 5, 15) - date(1944, 3, 19)).days, 57)
# Slovakia: agreement March 1942; 57,000+ deported 1942 (USHMM figure more than 57,000)
assert 57000 < 57628 < 58000
# Romania commission range 280,000 to 380,000: spread
eq("Romania range spread", 380000 - 280000, 100000)
# Vel d'Hiv: about 13,000, about 4,000 children: roughly 31%
eq("children share (per cent)", round(100 * 4000 / 13000), 31)
# Wannsee 20 January 1942; Denmark roundup October 1943
eq("Wannsee to Denmark (months)", (1943 - 1942) * 12 + (10 - 1), 21)
# Jedwabne 10 July 1941; Jaeger report 1 Dec 1941: 144 days
eq("Jedwabne to Jaeger report (days)", (date(1941, 12, 1) - date(1941, 7, 10)).days, 144)

# Section C dates and numbers
eq("Greece note to Truman Doctrine (days)", (date(1947, 3, 12) - date(1947, 2, 21)).days, 19)
eq("Marshall speech to Paris conference opens (days)", (date(1947, 6, 27) - date(1947, 6, 5)).days, 22)
eq("Paris conference length (days, inclusive)", (date(1947, 7, 2) - date(1947, 6, 27)).days + 1, 6)
eq("Brussels Treaty to NATO (days)", (date(1949, 4, 4) - date(1948, 3, 17)).days, 383)
eq("Blockade length (days, first to last)", (date(1949, 5, 12) - date(1948, 6, 24)).days, 322)
eq("Czech coup 20-25 Feb 1948 is six days", (date(1948, 2, 25) - date(1948, 2, 20)).days + 1, 6)
eq("Brussels Treaty members", len(["Britain", "France", "Belgium", "the Netherlands", "Luxembourg"]), 5)
eq("NATO founders", len(["USA", "Canada", "Britain", "France", "Belgium", "Netherlands", "Luxembourg", "Italy", "Portugal", "Norway", "Denmark", "Iceland"]), 12)
eq("Marshall aid years", 1952 - 1948 + 1, 5)
eq("Federal Republic to GDR (days)", (date(1949, 10, 7) - date(1949, 5, 23)).days, 137)
print("ok")
