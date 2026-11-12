# checks/hist.mixed.a2.py: recomputes every number in the chapter (marks, intervals, word counts, vote totals)
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 3: 40 marks = 20 + 20; Paper 4: 60 marks = 2 x 30; each 30 = 15 + 15
eq("paper 3 marks", 20 + 20, 40)
eq("paper 4 question marks", 15 + 15, 30)
eq("paper 4 total", 2 * 30, 60)
eq("Paper 3 top level span", 20 - 18 + 1, 3)
eq("Paper 4 top level span", 15 - 13 + 1, 3)
eq("Paper 4 timing", 2 * 50 + 5, 105)
eq("Paper 3 timing", 10 + 60 + 5, 75)
eq("timed pair of Paper 4 answers (2 x 50)", 2 * 50, 100)

# Intervals used in the text
eq("hostage days, counted inclusively as 444", (date(1981, 1, 20) - date(1979, 11, 4)).days + 1, 444)
eq("Yalta to Czech coup (years)", 1948 - 1945, 3)
eq("Gorbachev chosen aged", 1985 - 1931, 54)

# Electoral votes and seats (each pair adds to the totals the text implies)
eq("Enabling Act vote total", 444 + 94, 538)
eq("Reagan 1980", 489 + 49, 538)
eq("Truman 1948", 303 + 189 + 39, 531)
eq("Eisenhower 1952", 442 + 89, 531)
eq("Johnson 1964", 486 + 52, 538)
eq("Kennedy 1960 with 15 for Byrd", 303 + 219 + 15, 537)
eq("Rhodesia 1980 seats", 57 + 20 + 3, 80)
eq("Rhodesia Lancaster House seats", 80 + 20, 100)
eq("Rhodesia internal settlement seats", 72 + 28, 100)
eq("Malaya census shares leave 1.3 per cent", round(100 - (49.5 + 38.4 + 10.8), 1), 1.3)

# Differences quoted in the text
eq("military share rose by (points)", 23 - 3, 20)
eq("birth rate rise per thousand", round(20.3 - 14.7, 1), 5.6)
eq("US poverty fall 1964-73 (points)", round(19.0 - 11.1, 1), 7.9)
eq("deficit rise 1980-85 (billion dollars)", round(212.3 - 73.8, 1), 138.5)
eq("debt multiple 1980-89", round(2857.4 / 907.7, 1), 3.1)
eq("Gini rise", round(0.431 - 0.403, 3), 0.028)
eq("Order 00447 quotas total", 75950 + 193000, 268950)

# Practice extracts: stated lengths are 'about' the true word counts (within 8 words), all under 600
text = Path(__file__).resolve().parent.parent.joinpath("chapters", "hist.mixed.a2.md").read_text(encoding="utf-8")
found = re.findall(r"^:::note Practice extract (\w) \(about (\d+) words\)\n(.*?)^\*A summary", text, re.S | re.M)
eq("number of practice extracts", len(found), 6)
for letter, said, body in found:
    n = len(body.split())
    assert abs(n - int(said)) <= 8, f"extract {letter}: says about {said} words, has {n}"
    assert n <= 600, f"extract {letter} over 600 words"

# Counts
eq("Paper 4 questions", len(re.findall(r"^Q: \[30 marks\]", text, re.M)), 27)
eq("Paper 3 questions", len(re.findall(r"^Q: \[40 marks\]", text, re.M)), 6)
eq("recall round questions", len(re.findall(r"^Q: \(#", text, re.M)), 12)
quiz = re.search(r"^:::quiz Check the facts\n(.*?)^:::", text, re.S | re.M).group(1)
assert len(re.findall(r"^\? ", quiz, re.M)) >= 8
print("ok")
