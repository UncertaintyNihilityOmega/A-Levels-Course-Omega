# checks/hist.mixed.as.py: recomputes every number in the chapter (dates, intervals, timing, word limits)
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 1: 75 minutes, plan 8 + 20 + 4 + 38 + 5; part (b) 42 = 4 plan + 38 write
eq("paper 1 plan", 8 + 20 + 4 + 38 + 5, 75)
eq("part (b) time", 4 + 38, 42)
# Paper 2: 14 + 32 per question; a pair takes 46 minutes
eq("paper 2 pair", 14 + 32, 46)
eq("paper 2 plan", 6 + 14 + 32 + 14 + 32 + 7, 105)
eq("paper 1 marks", 15 + 25, 40)
eq("paper 2 marks", 2 * (10 + 20), 60)
# Levels (Paper 1 Table A, Table B; Paper 2 Table A, Table B)
eq("P1(a) top level span", 15 - 12 + 1, 4)
eq("P1(b) top level span", 25 - 21 + 1, 5)
eq("P2(a) top level span", 10 - 9 + 1, 2)
eq("P2(b) top level span", 20 - 17 + 1, 4)

# Dates and intervals
eq("Missouri line closed 1820-1854", 1854 - 1820, 34)
eq("Brunswick Manifesto to 10 August", (date(1792, 8, 10) - date(1792, 7, 25)).days, 16)
eq("Hoare speech to invasion of Abyssinia", (date(1935, 10, 3) - date(1935, 9, 11)).days, 22)
eq("Litvinov speech to Munich", (date(1938, 9, 29) - date(1938, 9, 21)).days, 8)
eq("Anschluss (12 March) to Litvinov, months", (9 - 3), 6)
eq("Haile Selassie speech to sanctions lifted", (date(1936, 7, 15) - date(1936, 6, 30)).days, 15)
eq("Kronstadt resolution to NEP report", (date(1921, 3, 15) - date(1921, 2, 28)).days, 15)
eq("Cheka decree OS to NS (1917)", (date(1917, 12, 20) - date(1917, 12, 7)).days, 13)
eq("Cheka decree six weeks after 25 Oct OS", round((date(1917, 12, 7) - date(1917, 10, 25)).days / 7), 6)
eq("Johnson veto to override", (date(1866, 4, 9) - date(1866, 3, 27)).days, 13)
eq("Lincoln's call to Sumter", (date(1861, 4, 15) - date(1861, 4, 13)).days, 2)
eq("Ruhr occupation after default year", 1923 - 1921, 2)
eq("Port Arthur (January) to Tsushima (May) 1905, months", 5 - 1, 4)
eq("Stevens speech, Congress had met 4 Dec", (date(1865, 12, 18) - date(1865, 12, 4)).days, 14)
eq("Emancipation preliminary to effect days", (date(1863, 1, 1) - date(1862, 9, 22)).days, 101)
eq("Vote margin Frankfurt", 267 - 263, 4)
eq("Roosevelt 1932 electoral votes", 472 + 59, 531)
eq("Third of voters who did not vote Bolshevik approx", 100 - 24, 76)

# Source word limit: at most 600 words in the four sources of each Paper 1 set
text = Path(__file__).resolve().parent.parent.joinpath("chapters", "hist.mixed.as.md").read_text(encoding="utf-8")
notes = re.findall(r"^:::note Sources A to D[^\n]*\n(.*?)^:::", text, re.S | re.M)
eq("number of Paper 1 sets", len(notes), 3)
for i, body in enumerate(notes, 1):
    words = 0
    for para in body.split("\n\n"):
        p = para.strip()
        if not p or p.startswith("**Source") or p.startswith("*"):
            continue
        words += len(p.split())
    assert words <= 600, f"set {i}: {words} words of sources (limit 600)"
    print(f"set {i}: {words} words of source text")

# Counts used in the text
eq("recall round questions", len(re.findall(r"^Q: \(#", text, re.M)), 12)
quiz = re.search(r"^:::quiz Check the facts\n(.*?)^:::", text, re.S | re.M).group(1)
assert len(re.findall(r"^\? ", quiz, re.M)) >= 8
print("ok")
