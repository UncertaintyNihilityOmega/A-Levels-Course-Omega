# checks/hist.mock.p2.py: recomputes every number in Mock Paper 2 (marks, time, level ranges, dates, figures)
import re
from datetime import date
from pathlib import Path


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 2: 60 marks = two questions of 30 = (a) 10 + (b) 20; 1 h 45 min = 105 min
eq("question marks", 10 + 20, 30)
eq("paper marks", 2 * 30, 60)
eq("paper minutes", 1 * 60 + 45, 105)
eq("time plan total", sum([6, 14, 32, 14, 32, 7]), 105)
eq("part (b) plan + write", 4 + 28, 32)
eq("minutes per mark", round(105 / 60, 2), 1.75)
eq("part (a) is a third of a question", 10 * 3, 30)

# Table A (part (a), 10 marks) and Table B (part (b), 20 marks): contiguous ranges
A = {4: (9, 10), 3: (6, 8), 2: (3, 5), 1: (1, 2)}
B = {5: (17, 20), 4: (13, 16), 3: (9, 12), 2: (5, 8), 1: (1, 4)}
for name, table, top in (("A", A, 10), ("B", B, 20)):
    hi = top
    for lvl in sorted(table, reverse=True):
        lo, h = table[lvl]
        eq(f"Table {name} level {lvl} top", h, hi)
        hi = lo - 1
    eq(f"Table {name} bottom", hi, 0)

# The chapter file: six questions of 30, each with (a) [10] and (b) [20]
text = (Path(__file__).resolve().parent.parent / "chapters" / "hist.mock.p2.md").read_text(encoding="utf-8")
qs = re.findall(r"^Q: \[(\d+) marks\](.*?)(?=^A: )", text, flags=re.S | re.M)
eq("number of questions", len(qs), 6)
for i, (m, body) in enumerate(qs, 1):
    eq(f"Q{i} marks", int(m), 30)
    eq(f"Q{i} part (a)", int(re.search(r"\(a\).*?\[(\d+)\]", body).group(1)), 10)
    eq(f"Q{i} part (b)", int(re.search(r"\(b\).*?\[(\d+)\]", body, flags=re.S).group(1)), 20)

# Q1 Germany
eq("Bismarck at the Diet 1851-59 (years)", 1859 - 1851, 8)
eq("Zollverein 1834 to the war of 1866", 1866 - 1834, 32)
eq("Carlsbad 1819 to the Hambach Festival 1832", 1832 - 1819, 13)
eq("Carlsbad decrees 1819 to the revolution 1848", 1848 - 1819, 29)
eq("Italy treaty 8 April to the end of its 3-month window (8 July) vs Konigratz 3 July",
   (date(1866, 7, 8) - date(1866, 7, 3)).days, 5)
eq("Austria to the Diet 1 June, Diet vote 14 June (days)", (date(1866, 6, 14) - date(1866, 6, 1)).days, 13)
eq("Gastein 14 Aug 1865 to 1 June 1866 (days)", (date(1866, 6, 1) - date(1865, 8, 14)).days, 291)
eq("Kotzebue 23 March 1819 to Carlsbad Decrees 20 Sept 1819 (days)", (date(1819, 9, 20) - date(1819, 3, 23)).days, 181)
# Q2 Russia
eq("harvest fall 1913 to 1920 at least (80 to 50 million tonnes)", round((80 - 50) / 80 * 100), 38)
eq("Kronstadt rising 28 Feb to 18 March 1921 (days)", (date(1921, 3, 18) - date(1921, 2, 28)).days, 18)
eq("Tenth Congress 8-16 March: 9 days", 16 - 8 + 1, 9)
eq("Tsar takes command 23 Aug 1915 to abdication 2 March 1917 (days, Old Style both)", (date(1917, 3, 2) - date(1915, 8, 23)).days, 557)
eq("Tsar's command, whole months", 18, 18)
eq("Women's Day strike 23 Feb to abdication 2 March (days)", (date(1917, 3, 2) - date(1917, 2, 23)).days, 7)
# Q3 Civil War
eq("preliminary proclamation to 1 January 1863 (days)", (date(1863, 1, 1) - date(1862, 9, 22)).days, 101)
eq("Black soldiers and sailors", 180000 + 20000, 200000)
eq("electoral votes in 1876", 184 + 165 + 20, 369)
eq("votes needed", 369 // 2 + 1, 185)
eq("Tilden short by one", 185 - 184, 1)
eq("Hayes with the disputed votes", 165 + 20, 185)
eq("Electoral Commission 5+5+5", 5 + 5 + 5, 15)
eq("Commission 8-7", 8 + 7, 15)
eq("Reconstruction Redeemers 1869 to 1877 (years)", 1877 - 1869, 8)
# Q4 Great Crash
eq("top rate fall 1921 to 1925 (points)", 73 - 25, 48)
eq("years for the tax cuts", 1925 - 1921, 4)
eq("unemployment fall 1933 to 1940 (points)", round(24.9 - 14.6, 1), 10.3)
eq("unemployment 1941", 9.9, 9.9)
eq("WPA period (years)", 1943 - 1935, 8)
eq("Social Security Act to the Wagner Act (days)", (date(1935, 8, 14) - date(1935, 7, 5)).days, 40)
eq("farm prices fell by about 53% between 1920 and 1921", round((1 - 0.47) * 100), 53)
# Q5 1919-29
eq("Geneva Protocol 2 Oct 1924 to British rejection 12 March 1925 (days)", (date(1925, 3, 12) - date(1924, 10, 2)).days, 161)
eq("Dawes standard annuity multiple", 2.5 / 1, 2.5)
eq("loans against reparations (billion marks)", 25 - 10, 15)
eq("Dawes loan on the American market (about half of 800 million)", 800 // 2, 400)
eq("Locarno conference 5-16 October: 12 days", 16 - 5 + 1, 12)
eq("Rhineland evacuation 1930 five years early", 1935 - 1930, 5)
# Q6 1929-39
eq("Mukden 18 Sept 1931 to Manchukuo 1 March 1932 (days)", (date(1932, 3, 1) - date(1931, 9, 18)).days, 165)
eq("Rhineland 7 March 1936 to the Spanish rising 17 July 1936 (days)", (date(1936, 7, 17) - date(1936, 3, 7)).days, 132)
eq("Spanish war to Anti-Comintern Pact (days)", (date(1936, 11, 25) - date(1936, 7, 17)).days, 131)
eq("Anti-Comintern Pact to Italy joining (days)", (date(1937, 11, 6) - date(1936, 11, 25)).days, 346)
eq("Guernica 26 April 1937 after the war began (days)", (date(1937, 4, 26) - date(1936, 7, 17)).days, 283)
eq("Non-Intervention Agreement 15 Aug to committee 9 Sept (days)", (date(1936, 9, 9) - date(1936, 8, 15)).days, 25)
eq("Spanish war end 1 April 1939, length in months (July 1936 to April 1939)", (1939 - 1936) * 12 + (4 - 7), 33)
print("ok")
