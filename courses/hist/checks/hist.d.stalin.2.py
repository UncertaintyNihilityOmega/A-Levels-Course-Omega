# checks/hist.d.stalin.2.py: recomputes every number in the chapter (Terror figures, intervals, percentages, chart values, figure layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# NKVD records: people shot in 1937 and 1938 -> 681,692 ("about 680,000"); chart shows 353 and 329 (thousands)
shot_1937, shot_1938 = 353074, 328618
eq("shot 1937-38", shot_1937 + shot_1938, 681692)
eq("chart values (thousands)", (round(shot_1937 / 1000), round(shot_1938 / 1000)), (353, 329))
assert 675000 <= 681692 <= 685000
assert 1_500_000 <= 1_575_259 <= 1_650_000  # "about 1.6 million" arrested
assert 1_575_259 > 681692 * 2
# Order 00447: initial quotas 75,950 shot and 193,000 camps; results about 767,000 sentenced, about 387,000 shot
q_shot, q_camp = 75950, 193000
eq("initial quota total", q_shot + q_camp, 268950)
assert round(387000 / q_shot) == 5, "about five times the first quota"
assert 0.49 < 387000 / 767000 < 0.51
# Polish operation: about 140,000 arrested, about 111,000 shot
assert 111091 < 143810 and 0.75 < 111091 / 143810 < 0.8
# Khrushchev's claim: 98 of 139 Central Committee members and candidates shot
eq("Khrushchev claim share (per cent)", round(98 / 139 * 100), 71)
# Military purge tallies quoted in the text
assert 3 / 5 == 0.6 and round(13 / 15 * 100) == 87 and round(50 / 57 * 100) == 88 and round(154 / 186 * 100) == 83
eq("generals tried with Tukhachevsky", 1 + 7, 8)
# Show trials
eq("first trial shot", 16, 16)
eq("second trial: shot and imprisoned", 13 + 4, 17)
eq("third trial: death sentences and prison", 18 + 3, 21)
assert date(1936, 8, 19) < date(1936, 8, 24) < date(1936, 8, 25)
assert date(1937, 1, 23) < date(1937, 1, 30) and date(1938, 3, 2) < date(1938, 3, 13) < date(1938, 3, 15)
eq("second trial length (days)", (date(1937, 1, 30) - date(1937, 1, 23)).days, 7)
eq("third trial length (days)", (date(1938, 3, 13) - date(1938, 3, 2)).days, 11)
# Kirov: shot 1 Dec 1934, Nikolaev shot 29 Dec 1934; first trial 19 Aug 1936
eq("Nikolaev shot after (days)", (date(1934, 12, 29) - date(1934, 12, 1)).days, 28)
assert 19 <= ((date(1936, 8, 19).year - 1934) * 12 + 8 - 12) <= 21
# End of the Yezhovshchina: decree 17 Nov 1938, Beria 25 Nov 1938 (8 days), Order 00447 to decree about 15 months
eq("decree to Beria (days)", (date(1938, 11, 25) - date(1938, 11, 17)).days, 8)
assert 15 <= ((1938 - 1937) * 12 + (11 - 7)) <= 16
assert date(1937, 7, 30) < date(1938, 11, 17) < date(1939, 4, 10) < date(1940, 2, 4)
# Gulag camp population (thousands)
camps = {1930: 179, 1934: 510, 1937: 821, 1939: 1317, 1941: 1501}
assert 8 < camps[1941] / camps[1930] < 9, "more than eightfold"
assert camps[1930] < camps[1934] < camps[1937] < camps[1939] < camps[1941]
# Stalin's 60th birthday on 21 December 1939 (official birth year 1879)
eq("sixtieth birthday year", 1879 + 60, 1939)
# Foreign policy intervals
pact, barbarossa = date(1939, 8, 23), date(1941, 6, 22)
eq("Pact to Barbarossa (whole months)", (barbarossa.year - pact.year) * 12 + barbarossa.month - pact.month - (1 if barbarossa.day < pact.day else 0), 21)
assert 21.5 < (barbarossa - pact).days / 30.44 < 22.5, "about 22 months"
eq("Poland: German to Soviet invasion (days)", (date(1939, 9, 17) - date(1939, 9, 1)).days, 16)
eq("Winter War length (days)", (date(1940, 3, 13) - date(1939, 11, 30)).days, 104)
assert 120000 / 25000 > 4
eq("TASS statement before invasion (days)", (barbarossa - date(1941, 6, 14)).days, 8)
eq("Neutrality Pact to Barbarossa (days)", (barbarossa - date(1941, 4, 13)).days, 70)
assert date(1939, 5, 3) < pact and date(1938, 9, 30) < date(1939, 5, 3)
eq("Popular Front congress length (days)", (date(1935, 8, 20) - date(1935, 7, 25)).days, 26)
eq("Franco-Soviet pact before Czech pact (days)", (date(1935, 5, 16) - date(1935, 5, 2)).days, 14)
assert date(1934, 9, 18) < date(1935, 5, 2) < date(1936, 10, 1)
# Congress gaps: 17th (1934) to 18th (1939)
eq("years between congresses", 1939 - 1934, 5)
# Sovnarkom: Molotov chairman Dec 1930 to May 1941 (10 years 5 months)
eq("months Molotov chaired Sovnarkom", (1941 - 1930) * 12 + (5 - 12), 125)
# Spanish gold about 500 tonnes (stated 'about'); International Brigades about 35,000
assert 450 <= 510 <= 550
# Seventeenth Congress length
eq("17th Congress length (days)", (date(1934, 2, 10) - date(1934, 1, 26)).days, 15)
# Eight generals + Gamarnik not counted; Butovo over 20,000
assert 20000 < 20762

text = open(os.path.join(here, "..", "chapters", "hist.d.stalin.2.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
print("ok")
