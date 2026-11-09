# checks/hist.int.1929.1.py: recomputes every number in the chapter (percentages, tonnage ratios, vote counts, totals, figure layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# German industrial production (1928 = 100): 102 in 1929, 58 in 1932: "more than 40 per cent"
fall = (102 - 58) / 102
between("production fall", fall, 0.40, 0.45)
# Nazi vote shares: chart and text
nazi = {"May 1928": 2.6, "Sep 1930": 18.3, "Jul 1932": 37.3, "Nov 1932": 33.1, "Mar 1933": 43.9}
eq("five elections", len(nazi), 5)
eq("elections span under five years", (date(1933, 3, 5) - date(1928, 5, 20)).days < 5 * 365, True)
eq("Nazi vote fell between Jul and Nov 1932", nazi["Nov 1932"] < nazi["Jul 1932"], True)
# Reichstag seats: 230 of 608 in July 1932 is 37.8 per cent of the seats, close to but not the vote share
between("seat share July 1932", 230 / 608, 0.37, 0.38)
# votes lost between July and November 1932: 13,745,680 to about 11.74 million: about two million
between("votes lost", 13745680 - 11737000, 1_900_000, 2_100_000)
# Hamaguchi shot 14 November 1930, died August 1931 (months)
eq("Hamaguchi survived about nine months", (date(1931, 8, 26) - date(1930, 11, 14)).days // 30, 9)
# Naval tonnages (thousands of tons): Japan against the USA
between("heavy cruisers: 108,400 of 180,000 is about 60 per cent", 108400 / 180000, 0.59, 0.61)
between("light cruisers: 100,450 of 143,500 is about 70 per cent", 100450 / 143500, 0.69, 0.71)
between("destroyers: 105,500 of 150,000 is about 70 per cent", 105500 / 150000, 0.69, 0.71)
# Senate vote on the World Court, 1935: 52 to 36; two thirds of 88 is 58.67, so the vote fell short
eq("World Court vote short of two thirds", 52 < 2 * (52 + 36) / 3, True)
eq("votes short", int(-(-(2 * (52 + 36)) // 3)) - 52, 7)
# Admission of the USSR: 39 for, 3 against, 7 abstentions
eq("USSR admission votes", 39 + 3 + 7, 49)
# Stresa 11-14 April 1935
eq("Stresa days", 14 - 11 + 1, 4)
# Disarmament Conference: MacDonald plan 200,000 men doubles the German army of 100,000
eq("German army doubles", 200000 // 100000, 2)
# Barthou, Hitler's conscription: a year between the end of the Conference's life and the announcement
eq("Years from Conference to conscription", 1935 - 1934, 1)
# Dates and intervals mentioned
eq("Naval Agreement to Italian invasion (days)", (date(1935, 10, 3) - date(1935, 6, 18)).days, 107)
eq("Stresa to Rhineland (days, 14 April 1935 to 7 March 1936)", (date(1936, 3, 7) - date(1935, 4, 14)).days, 328)
eq("Anti-Comintern Pact to Italy joining (days)", (date(1937, 11, 6) - date(1936, 11, 25)).days, 346)
eq("Hitler Chancellor to Germany leaves Geneva (days)", (date(1933, 10, 14) - date(1933, 1, 30)).days, 257)
# Paper totals
eq("Paper 1 totals", 15 + 25, 40)
eq("Paper 2 totals", (10 + 20) * 2, 60)
eq("Population of Japan (millions, about)", 64 > 60, True)

# ---- text checks
text = open(os.path.join(here, "..", "chapters", "hist.int.1929.1.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
m = re.search(r'data-series="Nazi vote: ([^"]*)"', text)
series = {k.strip(): float(v) for k, v in (p.split("=") for p in m.group(1).split(","))}
eq("chart series matches the checks", series, nazi)
for token in ["24 October 1929", "17 June 1930", "14 September 1930", "14 November 1930", "15 May 1932", "31 July 1932",
              "11 December 1932", "30 January 1933", "17 May 1933", "14 October 1933", "18 September 1934", "16 March 1935",
              "11 to 14 April 1935", "18 June 1935", "3 October 1935", "7 March 1936", "25 November 1936", "6 November 1937",
              "108,400", "180,000", "52 votes to 36", "39 votes to 3", "1 hour 15 minutes", "37.3 per cent", "18.3 per cent",
              "43.9 per cent", "2.6 per cent"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
print("ok")
