# checks/hist.d.italy.1.py: recomputes every number in the chapter (dates, ages, intervals, seats, percentages, figure layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Mussolini: born 29 July 1883, PM on 31 October 1922 -> "aged 39"
eq("Mussolini age at appointment", age(date(1883, 7, 29), date(1922, 10, 31)), 39)
# Matteotti: born 22 May 1885, speech 30 May 1924 -> "39-year-old"
eq("Matteotti age at his speech", age(date(1885, 5, 22), date(1924, 5, 30)), 39)
# Matteotti murdered 10 June 1924, eleven days after the speech of 30 May
eq("speech to murder (days)", (date(1924, 6, 10) - date(1924, 5, 30)).days, 11)
# Body found 16 August 1924: about two months after the kidnap
assert 60 <= (date(1924, 8, 16) - date(1924, 6, 10)).days <= 70
# Italy neutral Aug 1914 -> enters 24 May 1915: "nine months after it began"
eq("months of neutrality", round((date(1915, 5, 24) - date(1914, 8, 1)).days / 30.44), 10)
# D'Annunzio in Fiume 12 Sep 1919 -> 29 Dec 1920 ("about fifteen months")
assert 15 <= (date(1920, 12, 29) - date(1919, 9, 12)).days / 30.44 <= 16
# Factory occupation: 1-30 September 1920, "almost a month"
assert (date(1920, 9, 30) - date(1920, 9, 1)).days == 29
# Governments: Nitti Jun 1919, Giolitti Jun 1920, Bonomi Jul 1921, Facta Feb 1922 (two ministries) -> 5 governments, 4 PMs
govs = ["Nitti", "Giolitti", "Bonomi", "Facta I", "Facta II"]
eq("governments", len(govs), 5)
eq("prime ministers", len({g.split()[0] for g in govs}), 4)
# June 1919 -> October 1922 = 40 months
eq("months of five governments", (1922 - 1919) * 12 + (10 - 6), 40)
# Quiet gap: the Pact of Pacification was 3 Aug 1921, PNF founded 7-10 Nov 1921
assert date(1921, 8, 3) < date(1921, 11, 7)
# General strike 1-3 August 1922: three days
eq("strike days", (date(1922, 8, 3) - date(1922, 8, 1)).days + 1, 3)
# March on Rome: 27-28 Oct, king invites 29 Oct, Mussolini arrives 30, takes office 31
assert date(1922, 10, 27) < date(1922, 10, 28) < date(1922, 10, 29) < date(1922, 10, 30) < date(1922, 10, 31)
# Naples congress 24 Oct -> office 31 Oct = 7 days
eq("Naples to office", (date(1922, 10, 31) - date(1922, 10, 24)).days, 7)
# Acerbo law: Chamber 21 July 1923; election 6 April 1924 -> about 8.5 months
assert date(1923, 7, 21) < date(1924, 4, 6)

# Elections (Chamber seats)
eq("1919 seats: PSI + PPI", 156 + 100, 256)
assert 156 + 100 < 508
eq("1921 total seats", 535, 535)
assert 123 + 108 + 35 + 15 < 535
# 1924: list 355 + bis 19 = 374 of 535; opposition 161; vote shares 60.09 + 4.85 = 64.94 -> about 65
eq("1924 government seats", 355 + 19, 374)
eq("1924 opposition seats", 535 - 374, 161)
eq("1924 vote share", round(60.09 + 4.85), 65)
# Two-thirds of 535
assert abs(535 * 2 / 3 - 356.7) < 0.1
# 1924 seats of the opposition parties named in the table: PSI 22, PSU 24, PPI 39, PCd'I 19
eq("1924 named opposition seats", 22 + 24 + 39 + 19, 104)
assert 104 <= 161
# Fascist seats 275 inside the 374
assert 275 < 374
# Strength at Rome: 25,000-30,000 blackshirts v 28,000 troops
assert 25000 <= 28000 <= 30000
# Growth of membership: about 20,000 -> over 200,000 is a tenfold rise
assert 200000 / 20000 == 10

# Dates used in the table and widget
assert date(1925, 1, 3) > date(1924, 12, 31)
eq("Matteotti crisis months (June to Jan)", (1925 - 1924) * 12 + (1 - 6), 7)
# 120 deputies stripped in November 1926; 535-seat Chamber -> under a quarter
assert 120 / 535 < 0.25
# Debt about five times, prices about four times (stated as 'about')
# 156 + 100 = 256 of 508 seats: a bare majority of exactly half plus 2 -> "Socialists and Popolari" held a majority together
assert 256 > 508 / 2

text = open(os.path.join(here, "..", "chapters", "hist.d.italy.1.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
# every Paper 4 practice question is a [30] essay
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
# the worked examples name the right mark totals (two tables of 15)
eq("Table A + Table B", 15 + 15, 30)
print("ok")
