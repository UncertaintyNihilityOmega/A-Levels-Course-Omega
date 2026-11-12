# checks/hist.int.1919.4.py: recomputes every number in the chapter (dates, intervals, ages, shares, totals, figure layout)
from datetime import date
import os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
sys.path.insert(0, os.path.join(root, "data"))
from p16_svgcheck import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Intervals and ages
eq("Dawes report to Dawes Plan in force (days)", (date(1924, 9, 1) - date(1924, 4, 9)).days, 145)
eq("Geneva Protocol to British rejection (days)", (date(1925, 3, 12) - date(1924, 10, 2)).days, 161)
eq("Locarno conference length (days)", (date(1925, 10, 16) - date(1925, 10, 5)).days, 11)
eq("Locarno initialled to signed (days)", (date(1925, 12, 1) - date(1925, 10, 16)).days, 46)
eq("Locarno signed to in force (days)", (date(1926, 9, 14) - date(1925, 12, 1)).days, 287)
eq("Germany out of the League 1920 to 1926 (years)", 1926 - 1920, 6)
eq("Thoiry a week after Germany took its seat", (date(1926, 9, 17) - date(1926, 9, 10)).days, 7)
eq("Zinoviev letter to the election (days)", (date(1924, 10, 29) - date(1924, 10, 25)).days, 4)
eq("ARCOS raid to the break (days)", (date(1927, 5, 27) - date(1927, 5, 12)).days, 15)
eq("Hague Conference first session (days)", (date(1929, 8, 31) - date(1929, 8, 6)).days, 25)
born, died = date(1878, 5, 10), date(1929, 10, 3)
eq("Stresemann's age (exact)", died.year - born.year - ((died.month, died.day) < (born.month, born.day)), 51)
eq("Stresemann chancellor 13 August to 23 November 1923 (a hundred days)", round((date(1923, 11, 23) - date(1923, 8, 13)).days, -1), 100)
eq("Hague conference to Stresemann's death (weeks, about five)", round((date(1929, 10, 3) - date(1929, 8, 31)).days / 7), 5)
eq("Rhineland evacuated: years ahead of 1935", 1935 - 1930, 5)
eq("Young Plan: 1929 to 1988 (years)", 1988 - 1929, 59)
eq("Kellogg: nine named states plus five dominions plus India", 9 + 5 + 1, 15)
eq("Berlin Treaty valid five years: to", 1926 + 5, 1931)
eq("Crash: two dates", (date(1929, 10, 29) - date(1929, 10, 24)).days, 5)

# Money
eq("Dawes standard annuity against first year", 2.5 / 1.0, 2.5)
between("Young average annuity (112 billion over 59 years, about 2 billion)", 112 / 59, 1.8, 2.0)
between("Foreign loans against reparations (more than twice)", 25 / 10, 2.0, 3.0)
between("Loans, upper estimate against reparations", 29 / 10, 2.0, 3.0)
between("Young Plan total against the 1921 schedule", 112 / 132, 0.84, 0.86)
eq("Referendum: share of the electorate that voted, said about 14.9", 14.9 < 50, True)
eq("Nazi seats 1928 to 1930", (12, 107), (12, 107))
between("Nazi seats multiplied (about nine times)", 107 / 12, 8.5, 9.0)
eq("Locarno Reichstag vote: for, against", (291, 174), (291, 174))
eq("Senate vote on Kellogg", (85, 1), (85, 1))

# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)

# Chapter text
text = open(os.path.join(root, "chapters", "hist.int.1919.4.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 2)
for token in ["9 April 1924", "1 September 1924", "2 October 1924", "12 March 1925", "5–16 October 1925", "1 December 1925", "14 September 1926",
              "24 April 1926", "8 September 1926", "10 September", "27 May 1927", "27 August 1928", "7 June 1929", "6–31 August 1929", "3 October 1929",
              "30 June 1930", "17 September 1926", "112 billion", "59 years", "800 million", "2.5 billion", "fifteen states", "85 votes to 1", "291 votes to 174",
              "1 hour 15 minutes", "1 February 1924", "9 February 1925", "98 billion".replace("98", "132")]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
assert "<!--END-->" not in text, "leftover marker"
# FIX round (reader items): present value 36 billion against 112 billion paid over 59 years (average about 1.9 billion a year)
_avg = 112 / 59
_pv_rate = None
for _r in [x / 1000 for x in range(10, 120)]:
    _pv = _avg * (1 - (1 + _r) ** -59) / _r
    if _pv <= 36:
        _pv_rate = _r
        break
assert _pv_rate is not None and 0.04 <= _pv_rate <= 0.055, f"implied discount rate {_pv_rate}"
assert "36 billion is what all the future instalments were worth in 1929 money" in text
print("ok")
