# checks/hist.int.1919.3.py: recomputes every number in the chapter (dates, intervals, ratios, shares, figure layout)
from datetime import date
from math import log10
import os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
sys.path.insert(0, os.path.join(root, "data"))
from p16_svgcheck import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


def easter(y):  # anonymous Gregorian algorithm
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(y, month, day)


# Dates and intervals
eq("Rapallo 1922 was on Easter Sunday", easter(1922), date(1922, 4, 16))
eq("Fiume seized to Bloody Christmas (about 15 months)", round((date(1920, 12, 24) - date(1919, 9, 12)).days / 30.44), 15)
eq("Tellini murder to ultimatum (days)", (date(1923, 8, 29) - date(1923, 8, 27)).days, 2)
eq("Tellini murder to bombardment (days; timeline says four days)", (date(1923, 8, 31) - date(1923, 8, 27)).days, 4)
eq("Ultimatum to bombardment (days)", (date(1923, 8, 31) - date(1923, 8, 29)).days, 2)
eq("Tellini murder to Italian withdrawal (days)", (date(1923, 9, 27) - date(1923, 8, 27)).days, 31)
eq("Mussolini in office at the ultimatum (about ten months)", round((date(1923, 8, 29) - date(1922, 10, 31)).days / 30.44), 10)
eq("Occupation of the Ruhr to end of passive resistance (days)", (date(1923, 9, 26) - date(1923, 1, 11)).days, 258)
eq("Little Entente: first treaty to third (days)", (date(1921, 6, 7) - date(1920, 8, 14)).days, 297)
eq("Washington Conference length (days)", (date(1922, 2, 6) - date(1921, 11, 12)).days, 86)
eq("Genoa Conference length (days)", (date(1922, 5, 19) - date(1922, 4, 10)).days, 39)
eq("London Schedule ultimatum: six days to 11 May", (date(1921, 5, 11) - date(1921, 5, 5)).days, 6)
eq("Treaty of Rome 1924 after Rapallo 1920 (years)", 1924 - 1920, 4)
eq("Lausanne to Republic (days)", (date(1923, 10, 29) - date(1923, 7, 24)).days, 97)
eq("Lausanne after Mudanya (months, about nine)", round((date(1923, 7, 24) - date(1922, 10, 11)).days / 30.44), 9)
eq("Passive resistance vote: for and against", 283 + 12, 295)

# Reparations
eq("London Schedule: A and B bonds plus C bonds", 50 + 82, 132)
between("A and B share of the 132 billion", 50 / 132, 0.37, 0.39)

# Washington Naval Treaty
ships = {"USA": 525, "Britain": 525, "Japan": 315, "France": 175, "Italy": 175}
eq("Total capital ship tonnage allowed (thousand tons)", sum(ships.values()), 1715)
eq("Ratio USA", ships["USA"] / 105, 5.0)
eq("Ratio Britain", ships["Britain"] / 105, 5.0)
eq("Ratio Japan", ships["Japan"] / 105, 3.0)
eq("Ratio France", round(ships["France"] / 105, 2), 1.67)
eq("Ratio Italy", round(ships["Italy"] / 105, 2), 1.67)
eq("Japan's share of the American figure", ships["Japan"] / ships["USA"], 0.6)
between("France's share of the American figure (about a third)", ships["France"] / ships["USA"], 0.33, 0.34)
eq("Treaty runs to the end of 1936: years from 1922", 1936 - 1922, 14)

# Hyperinflation bars: 22 px per factor of ten
for label, value, width in [("1914", 4, 13), ("late 1919", 48, 37), ("1921", 90, 43), ("1922", 320, 55), ("Jan 1923", 17000, 93), ("Nov 1923", 4.2e12, 278)]:
    eq(f"log bar width {label}", round(22 * log10(value)), width)
between("Nov 1923 against 1914 (orders of magnitude)", log10(4.2e12 / 4.2), 11.9, 12.1)

# Washington bars: 299 px = 525 thousand tons
for label, v, w in [("USA", 525, 299), ("Britain", 525, 299), ("Japan", 315, 179), ("France", 175, 100), ("Italy", 175, 100)]:
    eq(f"Washington bar {label}", round(v * 299 / 525), w)

# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)

# Chapter text
text = open(os.path.join(root, "chapters", "hist.int.1919.3.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 3)
for token in ["12 September 1919", "12 November 1920", "27 January 1924", "14 August 1920", "23 April 1921", "7 June 1921", "5 May 1921",
              "132 billion", "11 January 1923", "26 September 1923", "27 August 1923", "29 August", "31 August", "27 September",
              "525,000", "315,000", "175,000", "1.67", "4.2 trillion", "16 April 1922", "24 July 1923", "10 April – 19 May 1922",
              "12 November 1921", "6 February 1922", "13 December 1921", "1 hour 15 minutes", "283 to 12", "24 June 1922", "26 December 1922"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
assert "<!--END-->" not in text, "leftover marker"
print("ok")
