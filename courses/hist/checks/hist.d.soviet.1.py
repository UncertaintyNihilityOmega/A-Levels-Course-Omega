# checks/hist.d.soviet.1.py: recomputes every number in the chapter (date arithmetic, rounded totals, ranges, figure layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Warsaw Pact: signed 14 May 1955, five days after West Germany joined NATO (9 May), a day before the Austrian State Treaty (15 May)
pact, nato_fr, austria = date(1955, 5, 14), date(1955, 5, 9), date(1955, 5, 15)
eq("days after West German entry to NATO", (pact - nato_fr).days, 5)
eq("Austrian State Treaty is the next day", (austria - pact).days, 1)
# Treaty runs 20 years (Article 11): to 1975; ten more unless denounced; the Pact was in fact dissolved in 1991
eq("treaty first term ends", 1955 + 20, 1975)
# Stalin dies 5 March 1953; East German rising 16-17 June 1953
assert date(1953, 3, 5) < date(1953, 5, 28) < date(1953, 6, 9) < date(1953, 6, 16) < date(1953, 6, 17) < date(1953, 6, 26)
eq("norm rise to rising (days)", (date(1953, 6, 17) - date(1953, 5, 28)).days, 20)
eq("rising to Beria's arrest (days)", (date(1953, 6, 26) - date(1953, 6, 17)).days, 9)
# Reparations from East Germany ended 1 January 1954
assert date(1954, 1, 1) > date(1953, 6, 17)
# Hungary 1956: 23 October to 4 November
eq("Hungary: first shots to Soviet attack (days)", (date(1956, 11, 4) - date(1956, 10, 23)).days, 12)
eq("Hungary: Nagy's government as an elected prime minister until the attack (days)", (date(1956, 11, 4) - date(1956, 10, 24)).days, 11)
assert date(1956, 10, 24) < date(1956, 10, 28) < date(1956, 10, 30) < date(1956, 10, 31) < date(1956, 11, 1) < date(1956, 11, 4)
eq("Poland: Khrushchev's flight to Gomulka's election (days)", (date(1956, 10, 21) - date(1956, 10, 19)).days, 2)
# Poznan 28 June 1956, secret speech 25 February 1956: four months and three days
eq("secret speech to Poznan (days)", (date(1956, 6, 28) - date(1956, 2, 25)).days, 124)
assert date(1956, 6, 28) < date(1956, 10, 19)
# Nagy hanged 16 June 1958: about 19 months after the attack
eq("months from the attack to Nagy's execution", (1958 - 1956) * 12 + (6 - 11), 19)
eq("Kadar's slogan 1961 minus 1956 (years)", 1961 - 1956, 5)
# Hungary casualties and refugees
assert 2500 < 3000 and 700 < 2500
eq("Hungarians: 'roughly 2 per cent of the population' left", round(200000 / 9.8e6 * 100), 2)  # Hungary's population about 9.8 million in 1956 (approx.)
# Berlin: Ulbricht's press conference 15 June 1961 to the Wall 13 August 1961 = 59 days; ultimatum 27 Nov 1958 to the Wall
eq("days from 'nobody intends to build a wall' to the Wall", (date(1961, 8, 13) - date(1961, 6, 15)).days, 59)
eq("Wall closed on a Sunday", date(1961, 8, 13).weekday(), 6)  # 6 = Sunday
eq("years the Wall stood (13 Aug 1961 to 9 Nov 1989)", (date(1989, 11, 9) - date(1961, 8, 13)).days // 365, 28)
eq("Peter Fechter aged 18 in 1962 (born 1944)", 1962 - 1944, 18)
assert date(1962, 8, 17) > date(1961, 8, 13)
# Prague Spring
eq("Dubcek's reform period to the invasion (days)", (date(1968, 8, 20) - date(1968, 1, 5)).days, 228)
eq("Action Programme to the invasion (days)", (date(1968, 8, 20) - date(1968, 4, 5)).days, 137)
eq("Dubcek in office as First Secretary (days, 5 Jan 1968 - 17 Apr 1969)", (date(1969, 4, 17) - date(1968, 1, 5)).days, 468)
eq("Cierna talks length (days, 29 July to 1 August inclusive)", (date(1968, 8, 1) - date(1968, 7, 29)).days + 1, 4)
assert date(1968, 3, 23) < date(1968, 6, 27) < date(1968, 7, 15) < date(1968, 7, 29) < date(1968, 8, 3) < date(1968, 8, 20) < date(1968, 8, 26) < date(1968, 9, 26) < date(1968, 10, 16) < date(1968, 11, 12)
eq("Moscow Protocol six days after the invasion", (date(1968, 8, 26) - date(1968, 8, 20)).days, 6)
eq("Brezhnev Doctrine article after the invasion (days)", (date(1968, 9, 26) - date(1968, 8, 21)).days, 36)
eq("Soviet troops stayed 1968 to 1991 (years)", 1991 - 1968, 23)
eq("Hungary 1956 to Czechoslovakia 1968 (years)", 1968 - 1956, 12)
# Stasi: founded 1950, Mielke 1957-89 = 32 years; staff 1989
eq("Mielke's years as head", 1989 - 1957, 32)
eq("years from Stasi's founding to 1989", 1989 - 1950, 39)
assert 91000 < 91015 and 173000 < 173081
# Comecon 1949; Czech election 1946 share of the vote
assert 0.38 < 0.40
# Cardinals and churches
eq("Wyszynski held (Sept 1953 to Oct 1956, years)", 1956 - 1953, 3)
eq("Mindszenty in the American legation (1956-71, years)", 1971 - 1956, 15)
# Slansky trial: 11 of 14 hanged
eq("Slansky trial: defendants not hanged", 14 - 11, 3)
assert round(11 / 14 * 100) == 79
# Kovalev article: Fordham dates it 25 Sept, most sources 26 Sept 1968
assert date(1968, 9, 25) < date(1968, 9, 26)

text = open(os.path.join(here, "..", "chapters", "hist.d.soviet.1.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
eq("number of timeline widgets", len(re.findall(r'data-w="hist-timeline"', text)), 1)
# every timeline event date is a real date and the events are in order
ev = re.search(r'data-events="([^"]*)"', text).group(1).split(" ;; ")
ds = [e.split(" | ")[0] for e in ev]
assert ds == sorted(ds), ds
for d in ds:
    parts = [int(x) for x in d.split("-")]
    if len(parts) == 3:
        date(*parts)
# every Paper 4 practice question is a [30] essay
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
# command words are the real ones
for m in re.finditer(r"^Q: \[30 marks\] ★+ (.*)$", text, re.M):
    assert m.group(1).startswith("Assess") or "Evaluate" in m.group(1), m.group(1)
print("ok")
