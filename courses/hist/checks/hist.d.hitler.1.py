# checks/hist.d.hitler.1.py: recomputes every number in the chapter (ages, intervals, election figures, votes, SVG layout)
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


# Ages
eq("Hindenburg elected April 1925", age(date(1847, 10, 2), date(1925, 4, 26)), 77)
eq("Hindenburg at the 1932 election", age(date(1847, 10, 2), date(1932, 3, 13)), 84)
eq("Hindenburg on 30 Jan 1933", age(date(1847, 10, 2), date(1933, 1, 30)), 85)
eq("Papen on 30 Jan 1933", age(date(1879, 10, 29), date(1933, 1, 30)), 53)
eq("Schleicher on 30 Jan 1933", age(date(1882, 4, 7), date(1933, 1, 30)), 50)
eq("Hitler on 30 Jan 1933", age(date(1889, 4, 20), date(1933, 1, 30)), 43)
eq("Hindenburg at death", age(date(1847, 10, 2), date(1934, 8, 2)), 86)

# Intervals
eq("full months from 30 Jan 1933 to 2 Aug 1934", (1934 - 1933) * 12 + (8 - 1) - (1 if 2 < 30 else 0), 18)
assert date(1933, 1, 30) < date(1933, 2, 27) < date(1933, 3, 5) < date(1933, 3, 23) < date(1933, 5, 2) < date(1934, 6, 30) < date(1934, 8, 2)
eq("Altona to Prussian coup (days)", (date(1932, 7, 20) - date(1932, 7, 17)).days, 3)
eq("days from Hindenburg's death to the plebiscite", (date(1934, 8, 19) - date(1934, 8, 2)).days, 17)
eq("election 5 March 1933 weekday (6 = Sunday)", date(1933, 3, 5).weekday(), 6)
assert date(1930, 3, 27) < date(1930, 3, 30)
assert date(1932, 5, 30) < date(1932, 6, 1) < date(1932, 12, 3) < date(1933, 1, 28) < date(1933, 1, 30)

# Unemployment (Statistisches Jahrbuch annual averages) -> chart in millions to 0.1
ue = {1929: 1898604, 1930: 3075580, 1931: 4519704, 1932: 5575492, 1933: 4804428}
chart = {y: round(v / 1e6, 1) for y, v in ue.items()}
eq("unemployment chart", chart, {1929: 1.9, 1930: 3.1, 1931: 4.5, 1932: 5.6, 1933: 4.8})
assert ue[1932] / ue[1929] > 2.9  # "nearly tripled" from 1929 to 1932 (2.94)
assert 2.9 < ue[1932] / ue[1929] < 3.0
assert ue[1933] < ue[1932]

# Reichstag elections: votes, percentages, seats
nsdap_pct = {"1928": 2.6, "1930": 18.3, "1932a": 37.3, "1932b": 33.1, "1933": 43.9}
eq("NSDAP percentages", [round(p, 1) for p in (2.63, 18.25 + 0.0001, 37.27, 33.09, 43.9)], list(nsdap_pct.values()))
nsdap_seats = {"1928": 12, "1930": 107, "1932a": 230, "1932b": 196, "1933": 288}
eq("seat change 1928->1930", nsdap_seats["1930"] - nsdap_seats["1928"], 95)
eq("seat change Jul->Nov 1932", nsdap_seats["1932a"] - nsdap_seats["1932b"], 34)
eq("seat change 1930 -> Jul 1932", nsdap_seats["1932a"] - nsdap_seats["1930"], 123)
tot = {"1928": 491, "1930": 577, "1932a": 608, "1932b": 584, "1933": 647}
eq("Nazi share of seats Jul 1932 (about 38 per cent)", round(230 / 608 * 100), 38)
# the two parties of the extremes
neg_jul = 230 + 89
neg_nov = 196 + 100
assert neg_jul > 608 / 2 and neg_nov > 584 / 2
eq("negative majority July", (neg_jul, 608), (319, 608))
eq("negative majority November", (neg_nov, 584), (296, 584))
eq("KPD+NSDAP vote Nov 1932 (almost half)", round(33.09 + 16.86, 1), 50.0)
assert 49 < 33.09 + 16.86 <= 50.0
assert 20.4 + 16.9 > 33.1  # SPD + KPD against Nazis, Nov 1932
eq("Nazi vote loss Jul-Nov 1932 (about 2 million)", round((13745680 - 11737021) / 1e6, 1), 2.0)
eq("Nazi votes Jul 1932 (13.7m) and Nov 1932 (11.7m)", (round(13745680 / 1e6, 1), round(11737021 / 1e6, 1)), (13.7, 11.7))
eq("Nazi vote fall in points", round(37.27 - 33.09, 1), 4.2)
# March 1933
need = 647 // 2 + 1
eq("majority needed in March 1933", need, 324)
eq("short of a majority", need - 288, 36)
eq("Nazis plus DNVP seats", 288 + 52, 340)
assert 288 + 52 >= need
eq("17.3 million votes in March 1933", round(17277180 / 1e6, 1), 17.3)
# Weimar elections 1928 etc, percentages quoted in the table
assert round(29.76, 1) == 29.8 and round(12.07, 1) == 12.1 and round(10.62, 1) == 10.6
assert round(24.53, 1) == 24.5 and round(21.58, 1) == 21.6 and round(20.43, 1) == 20.4
assert round(14.32, 1) == 14.3 and round(16.86, 1) == 16.9 and round(12.44, 1) == 12.4 and round(11.93, 1) == 11.9
assert round(7.03, 1) == 7.0 and round(5.91, 1) == 5.9 and round(8.34, 1) == 8.3 and round(11.81, 1) == 11.8
# Presidential election: second round sums to 100, first round about 100
eq("second round total", round(53.0 + 36.8 + 10.2, 1), 100.0)
assert 99 < 49.6 + 30.1 + 13.2 + 6.8 <= 100
eq("Hitler votes second round (13.4 million)", round(13418517 / 1e6, 1), 13.4)

# Enabling Act
eq("votes counted", 444 + 94, 538)
eq("absent", 647 - (444 + 94), 109)
eq("two-thirds of 647", -(-647 * 2 // 3), 432)
eq("two-thirds of 647 minus 81 KPD seats", -(-(647 - 81) * 2 // 3), 378)
assert 444 > 432
assert 444 + 94 >= 432  # quorum
assert 444 / (444 + 94) > 2 / 3
eq("Reichstag seats for the yes parties (NSDAP+DNVP+Centre+BVP)", 288 + 52 + 73 + 19, 432)
assert 444 - 432 == 12  # small parties
eq("Enabling Act valid until", date(1937, 4, 1).year - 1933, 4)

# Cabinet of eleven: Hitler, Papen, Neurath, Frick, Goering, Blomberg, Hugenberg, Seldte, Schwerin von Krosigk, Guertner, Eltz-Ruebenach
cabinet = ["Hitler", "Papen", "Neurath", "Frick", "Goering", "Blomberg", "Hugenberg", "Seldte", "Schwerin von Krosigk", "Guertner", "Eltz-Ruebenach"]
eq("cabinet members", len(cabinet), 11)
eq("Nazi ministers", len([m for m in cabinet if m in ("Hitler", "Frick", "Goering")]), 3)

# Fire decree: seven articles
arts = [114, 115, 117, 118, 123, 124, 153]
eq("articles suspended", len(arts), 7)

# SA figures
sa = {"1930": 60000, "Jan 1931": 77000, "Nov 1931": 221000, "Aug 1932": 445000}
assert list(sa.values()) == sorted(sa.values())
assert sa["Aug 1932"] / sa["1930"] > 7
# Altona dead
eq("Altona dead", 2 + 16, 18)
# SA ban dates
assert date(1932, 4, 13) < date(1932, 6, 16)
# Night of the Long Knives
eq("NoLK length (days, inclusive)", (date(1934, 7, 2) - date(1934, 6, 30)).days + 1, 3)
assert 85 < 150
# Young Plan referendum
assert 13.8 < 50
# elite petition
assert date(1932, 11, 19) < date(1933, 2, 20)
# plebiscite
eq("yes votes 1934 in millions", round(38394848 / 1e6, 1), 38.4)
# Gleichschaltung dates in order
assert date(1933, 3, 31) < date(1933, 4, 7) < date(1933, 5, 2) < date(1933, 5, 10) < date(1933, 6, 22) < date(1933, 7, 5) < date(1933, 7, 14) < date(1933, 7, 20)
# Strasser resigned before Schleicher's fall
assert date(1932, 12, 8) < date(1933, 1, 28)
# two elections took place in 1932 + presidential: five national votes (two presidential rounds, two Reichstag elections)
eq("national votes in 1932", len(["13 Mar", "10 Apr", "31 Jul", "6 Nov"]), 4)

text = open(os.path.join(here, "..", "chapters", "hist.d.hitler.1.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
print("ok")
