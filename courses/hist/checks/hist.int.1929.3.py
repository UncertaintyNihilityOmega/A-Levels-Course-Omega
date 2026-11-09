# checks/hist.int.1929.3.py: recomputes every number in the chapter (intervals, votes, percentages, chart data, layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Britain
d = (date(1932, 3, 23) - date(1919, 8, 1)).days / 365.25
between("Ten-Year Rule lasted almost thirteen years (12.5 to 13)", d, 12.5, 13.0)
eq("Oxford Union: votes cast", 275 + 153, 428)
eq("Oxford Union: majority", 275 - 153, 122)
between("Peace Ballot: military measures yes share (about 59 per cent)", 6.8 / 11.5, 0.58, 0.60)
between("Peace Ballot: economic sanctions share (about 87 per cent)", 10.0 / 11.5, 0.86, 0.88)
d = (date(1936, 3, 7) - date(1935, 6, 27)).days
between("Peace Ballot result to Rhineland: eight months", d / 30.4, 8.0, 8.6)
eq("Rhineland to first round of the French election (days)", (date(1936, 4, 26) - date(1936, 3, 7)).days, 50)
between("Rhineland to election: about seven weeks", (date(1936, 4, 26) - date(1936, 3, 7)).days / 7, 7.0, 7.3)
# Spending chart
sp = {"1934–35": 113.9, "1936–37": 186.1, "1937–38": 262.1, "1938–39": 382.5}
between("spending more than tripled", sp["1938–39"] / sp["1934–35"], 3.0, 3.5)
text = open(os.path.join(here, "..", "chapters", "hist.int.1929.3.md"), encoding="utf-8").read()
m = re.search(r'data-series="Defence spending: ([^"]*)"', text)
got = dict(p.strip().split("=") for p in m.group(1).split(","))
eq("chart data", {k: float(v) for k, v in got.items()}, sp)
eq("Defence Requirements Committee: asked 71, cut to 50", 71 - 50, 21)
eq("Fighter squadrons: 18 Hurricane + 9 Spitfire", 18 + 9, 27)
# Czechoslovakia
between("Germans in Czechoslovakia: 3.2 of 14.7 million is 22 per cent", 3.2 / 14.7, 0.217, 0.220)
eq("Chamberlain's age on 15 September 1938", 1938 - 1869 - (1 if (9, 15) < (3, 18) else 0), 69)
eq("Berchtesgaden to Munich (days)", (date(1938, 9, 29) - date(1938, 9, 15)).days, 14)
eq("Godesberg talks to Munich (days)", (date(1938, 9, 29) - date(1938, 9, 22)).days, 7)
eq("Munich evacuation 1 to 10 October (days)", (date(1938, 10, 10) - date(1938, 10, 1)).days, 9)
d = (date(1939, 3, 15) - date(1938, 9, 30)).days
eq("Munich to Prague (days)", d, 166)
between("Munich to Prague: less than six months, about 5.5", d / 30.4, 5.3, 5.7)
eq("Prague to the guarantee to Poland (days)", (date(1939, 3, 31) - date(1939, 3, 15)).days, 16)
eq("Commons vote on Munich: majority", 366 - 144, 222)
between("Naval Agreement: 35 per cent", 35 / 100, 0.35, 0.35)
eq("Anschluss: troops 12 March, law 13 March (days)", (date(1938, 3, 13) - date(1938, 3, 12)).days, 1)
eq("Austrian plebiscite after the Anschluss (days)", (date(1938, 4, 10) - date(1938, 3, 13)).days, 28)
eq("Eden resigns to the Anschluss (days)", (date(1938, 3, 12) - date(1938, 2, 20)).days, 20)
eq("Conscription 16 March 1935 to Naval Agreement (days)", (date(1935, 6, 18) - date(1935, 3, 16)).days, 94)
eq("Hitler's divisions 36 and about 550,000 men: about 15,000 per division", round(550000 / 36 / 1000), 15)
eq("Dominions declaring war: Australia and NZ 3 Sept, Canada 10 Sept (days)", (date(1939, 9, 10) - date(1939, 9, 3)).days, 7)
# Paper totals
eq("Paper 1 totals", 15 + 25, 40)
eq("Paper 2 totals", (10 + 20) * 2, 60)

# ---- timeline dates are valid and in order
ev = re.search(r'data-events="([^"]*)"', text).group(1).split(" ;; ")
dates = []
for e in ev:
    f = [x.strip() for x in e.split(" | ")]
    eq("timeline event has four fields", len(f), 4)
    y, mo, dd = (int(v) for v in f[0].split("-"))
    dates.append(date(y, mo, dd))
assert dates == sorted(dates), "timeline not in date order"
eq("timeline events", len(ev), 16)

# ---- figures and text
eq("number of SVG figures", check_svgs(text), 1)
for token in ["23 March 1932", "9 February 1933", "275 votes to 153", "16 March 1935", "18 June 1935", "7 March 1936", "28 May 1937",
              "20 February 1938", "12–13 March 1938", "15 September", "22–23 September", "29–30 September", "5 October 1938",
              "15 March 1939", "31 March 1939", "366 votes to 144", "11.5 million", "6.8 million", "27 September 1938",
              "1 hour 15 minutes", "peace for our time", "a total and unmitigated defeat", "viewBox=\"0 0 340 352\""]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
assert "hedged" not in text, "no editorial notes left in the text"
print("ok")
