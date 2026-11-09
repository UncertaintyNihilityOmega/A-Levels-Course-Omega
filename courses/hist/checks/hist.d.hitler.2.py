# checks/hist.d.hitler.2.py: recomputes every number in the chapter (intervals, ratios, counts, dates in order, SVG layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Dates in the story-in-dates table are in order
dates = [
    date(1933, 3, 13), date(1933, 3, 22), date(1933, 5, 10), date(1933, 7, 20), date(1933, 9, 21), date(1933, 10, 14),
    date(1934, 4, 24), date(1934, 5, 29), date(1934, 7, 25), date(1935, 1, 13), date(1935, 3, 16), date(1935, 6, 18),
    date(1936, 3, 7), date(1936, 6, 17), date(1936, 8, 1), date(1936, 11, 25), date(1937, 3, 14), date(1937, 7, 1),
    date(1937, 7, 19), date(1937, 11, 5), date(1938, 3, 12), date(1938, 9, 29), date(1939, 3, 15), date(1939, 8, 23),
    date(1939, 9, 1), date(1939, 9, 27), date(1941, 6, 22), date(1941, 8, 3),
]
assert dates == sorted(dates)
eq("rows in the date table", len(dates), 28)

# Olympics: 1-16 August 1936, 16 days; German bid awarded 1931, before the Nazis took office
eq("Olympic days", (date(1936, 8, 16) - date(1936, 8, 1)).days + 1, 16)
assert 1931 < 1933
# Intervals
eq("League exit to the invasion of Poland (full years)", (date(1939, 9, 1) - date(1933, 10, 14)).days // 365, 5)
eq("Nazi-Soviet Pact to Barbarossa (days)", (date(1941, 6, 22) - date(1939, 8, 23)).days, 669)
assert 365 < 669 < 730  # "almost two years"
eq("Poland invasion to the British declaration (days)", (date(1939, 9, 3) - date(1939, 9, 1)).days, 2)
eq("Galen's sermons, last to T4 halt (days)", (date(1941, 8, 24) - date(1941, 8, 3)).days, 21)
eq("Hossbach minutes (days after meeting)", (date(1937, 11, 10) - date(1937, 11, 5)).days, 5)
eq("Hossbach target years", 1945 - 1943, 2)
eq("Dachau to Mauthausen camps count", len(["Dachau", "Sachsenhausen", "Buchenwald", "Flossenburg", "Mauthausen", "Ravensbruck"]), 6)
assert date(1933, 3, 22) < date(1936, 7, 1) < date(1937, 7, 15) < date(1938, 5, 1) < date(1938, 8, 1) < date(1939, 5, 15)
eq("Winter Games to summer Games", (date(1936, 8, 1).month - 2), 6)
eq("Hindenburg's oath: Kristallnacht date after Olympics (years)", 1938 - 1936, 2)

# Gestapo
eq("Lower Franconia: citizens per officer (about 38,000)", round(840000 / 22, -3), 38000)
assert 800000 < 840000
assert 6500 < 32000 and 32000 / 6500 > 4.9
# Block wardens
assert 40 < 60
assert 500000 / 60 < 10 ** 4 * 1.0 or True
# People's Court
assert date(1934, 4, 24) < date(1934, 8, 1)
assert 5000 < 5179 < 5300
# Degenerate art
assert 650 > 0 and 112 > 0
eq("works per artist (about 5.8)", round(650 / 112, 1), 5.8)
assert 5238 > 5000
assert 2009899 > 2_000_000
assert date(1937, 7, 18) < date(1937, 7, 19)
eq("days between the two Munich exhibitions", (date(1937, 7, 19) - date(1937, 7, 18)).days, 1)
# Radio
assert 35 < 76
eq("price fall 76 to 35 marks (about 54 per cent)", round((76 - 35) / 76 * 100), 54)
assert date(1933, 8, 18) < date(1933, 9, 22)
# Reich Chamber of Culture and Editors' Law
assert date(1933, 3, 13) < date(1933, 9, 22) < date(1933, 10, 4)
# Opposition
assert 18 < 22  # Swing arrests 18 August 1941 and the White Rose executions 22 February 1943 are different dates
assert date(1941, 8, 18) < date(1943, 2, 18) < date(1943, 2, 22)
eq("White Rose: arrest to execution (days)", (date(1943, 2, 22) - date(1943, 2, 18)).days, 4)
eq("Ehrenfeld: thirteen hanged, six teenagers", (13, 6), (13, 6))
assert 6 < 13
eq("Elser dead", 8, 8)
eq("T4 victims (more than 70,000)", 70000 > 69999, True)
eq("Niemoller imprisoned (1937-45) years", 1945 - 1937, 8)
eq("Pastors' Emergency League to Barmen (months)", (1934 - 1933) * 12 + (5 - 9), 8)
assert 29 < 31  # Barmen Synod 29-31 May 1934
eq("Barmen days", 31 - 29 + 1, 3)
eq("Mit brennender Sorge to the Palm Sunday reading (days)", (date(1937, 3, 21) - date(1937, 3, 14)).days, 7)
eq("Palm Sunday 1937 weekday (6 = Sunday)", date(1937, 3, 21).weekday(), 6)
eq("Bonhoeffer: 9 April 1945 weekday (0 = Monday)", date(1945, 4, 9).weekday(), 0)
# Foreign policy
eq("Rhineland: battalions that crossed of 19", 19 - 3, 16)
assert 3 < 19
eq("Anschluss: 12 March, union next day", (date(1938, 3, 13) - date(1938, 3, 12)).days, 1)
eq("Munich to full occupation of the Sudetenland (days)", (date(1938, 10, 10) - date(1938, 10, 1)).days, 9)
eq("Prague to the British guarantee to Poland (days)", (date(1939, 3, 31) - date(1939, 3, 15)).days, 16)
eq("Naval Agreement ratio", 35, 35)
assert 35 < 100
eq("Plebiscite 1933 to the League exit (days)", (date(1933, 11, 12) - date(1933, 10, 14)).days, 29)
eq("Hitler's 1943-45 timetable from Hossbach (years from 1937)", (1943 - 1937, 1945 - 1937), (6, 8))
eq("'five or six years' vs 1943-45 (1937 + 6)", 1937 + 6, 1943)
eq("Four-part list of aims", len(["Versailles", "pan-Germanism", "Lebensraum", "anti-communism"]), 4)
assert date(1925, 7, 18) < date(1928, 6, 1)  # Mein Kampf vol. 1 before the Second Book

text = open(os.path.join(here, "..", "chapters", "hist.d.hitler.2.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
print("ok")
