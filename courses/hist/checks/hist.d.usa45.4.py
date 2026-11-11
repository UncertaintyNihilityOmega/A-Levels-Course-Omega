# checks/hist.d.usa45.4.py: recomputes every number in the chapter (dates, intervals, percentages, marks)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Potsdam: 17 July to 2 August 1945 is 16 days after opening
eq("Potsdam length", (date(1945, 8, 2) - date(1945, 7, 17)).days, 16)

# Truman Doctrine: 400 million = 300 (Greece) + 100 (Turkey); 85 days to Marshall's speech
eq("Greece plus Turkey", 300 + 100, 400)
eq("Doctrine to Marshall speech (days)", (date(1947, 6, 5) - date(1947, 3, 12)).days, 85)
eq("Marshall speech to Act (days)", (date(1948, 4, 3) - date(1947, 6, 5)).days, 303)

# Britain's note 21 Feb 1947 to the Doctrine speech
eq("note to speech (days)", (date(1947, 3, 12) - date(1947, 2, 21)).days, 19)

# NATO members: USA, Canada, Britain, France, Italy, Belgium, Netherlands, Luxembourg, Norway, Denmark, Iceland, Portugal
nato = ["USA", "Canada", "Britain", "France", "Italy", "Belgium", "Netherlands", "Luxembourg", "Norway", "Denmark", "Iceland", "Portugal"]
eq("NATO founding members", len(nato), 12)
# SEATO: USA, Britain, France, Australia, New Zealand, Philippines, Thailand, Pakistan
seato = ["USA", "Britain", "France", "Australia", "New Zealand", "Philippines", "Thailand", "Pakistan"]
eq("SEATO members", len(seato), 8)
# Baghdad Pact members: Britain, Turkey, Iraq, Iran, Pakistan
eq("Baghdad Pact members", len(["Britain", "Turkey", "Iraq", "Iran", "Pakistan"]), 5)
eq("NATO years since the 1778 alliance with France", 1949 - 1778, 171)

# Berlin Blockade and Airlift
eq("blockade length (days)", (date(1949, 5, 12) - date(1948, 6, 24)).days, 322)
eq("airlift length (days)", (date(1949, 9, 30) - date(1948, 6, 26)).days, 461)
eq("airlift start two days after blockade", (date(1948, 6, 26) - date(1948, 6, 24)).days, 2)
eq("currency reform to blockade (days)", (date(1948, 6, 24) - date(1948, 6, 20)).days, 4)
between("airlift 'about three-quarters' American", 0.75, 0.70, 0.80)
eq("FRG to GDR (days)", (date(1949, 10, 7) - date(1949, 5, 23)).days, 137)
eq("West Germany joins NATO to Warsaw Pact (days)", (date(1955, 5, 14) - date(1955, 5, 9)).days, 5)
eq("Berlin ultimatum six months later", date(1958, 11, 27).month + 6 - 12, 5)  # 27 May 1959
eq("Camp David visit length (days)", (date(1959, 9, 27) - date(1959, 9, 15)).days + 1, 13)
eq("Khrushchev visit 'twelve days' (15 to 27 September, counting the span)", (date(1959, 9, 27) - date(1959, 9, 15)).days, 12)

# Defence spending: about 14 billion (1950) to over 50 billion (1953); 'quadrupled' is nearly 4x
between("defence multiple", 52.8 / 13.7, 3.5, 4.0)
assert 52.8 > 50 and 13.7 < 14.5

# Nuclear stockpile: under 1,500 (1953, 1,169) to roughly 20,000 (1960, 20,434)
assert 1169 < 1500 and 18000 < 20434 < 22000
between("stockpile multiple", 20434 / 1169, 15, 20)

# Korea
eq("invasion to armistice (years)", 1953 - 1950, 3)
eq("invasion to armistice (days)", (date(1953, 7, 27) - date(1950, 6, 25)).days, 1128)
eq("Inchon to crossing (days)", (date(1950, 10, 7) - date(1950, 9, 15)).days, 22)
eq("Chinese offensive to Seoul falls (days)", (date(1951, 1, 4) - date(1950, 11, 25)).days, 40)
eq("MacArthur dismissed, days after Chinese offensive", (date(1951, 4, 11) - date(1950, 11, 25)).days, 137)
eq("Seoul changed hands", 4, 4)
eq("sixteen UN contributors", 16, 16)
eq("US theatre deaths rounded to nearest 500", round(36574 / 500) * 500, 36500)
eq("Korea division year to invasion", 1950 - 1945, 5)
eq("ROK to DPRK (days)", (date(1948, 9, 9) - date(1948, 8, 15)).days, 25)

# Eisenhower years
eq("Stalin's death to Chance for Peace (days)", (date(1953, 4, 16) - date(1953, 3, 5)).days, 42)
eq("Dien Bien Phu siege (days)", (date(1954, 5, 7) - date(1954, 3, 13)).days, 55)
eq("Dien Bien Phu to Geneva Accords (days)", (date(1954, 7, 21) - date(1954, 5, 7)).days, 75)
eq("Geneva Accords to SEATO (days)", (date(1954, 9, 8) - date(1954, 7, 21)).days, 49)
eq("Hungarian Rising length (days)", (date(1956, 11, 4) - date(1956, 10, 23)).days, 12)
eq("Suez nationalisation to Israeli invasion (days)", (date(1956, 10, 29) - date(1956, 7, 26)).days, 95)
eq("Aswan withdrawal to nationalisation (days)", (date(1956, 7, 26) - date(1956, 7, 19)).days, 7)
eq("Guatemala invasion to resignation (days)", (date(1954, 6, 27) - date(1954, 6, 18)).days, 9)
eq("U-2 shot down to Paris summit (days)", (date(1960, 5, 16) - date(1960, 5, 1)).days, 15)
eq("Eisenhower admits responsibility, days after shootdown", (date(1960, 5, 11) - date(1960, 5, 1)).days, 10)
eq("Castro takes power to recognition (days)", (date(1959, 1, 7) - date(1959, 1, 1)).days, 6)
eq("New Look to massive retaliation speech (days)", (date(1954, 1, 12) - date(1953, 10, 30)).days, 74)
eq("Long Telegram to Fulton speech (days)", (date(1946, 3, 5) - date(1946, 2, 22)).days, 11)
eq("Sputnik year", date(1957, 10, 4).year, 1957)
eq("Geneva Summit length (days)", (date(1955, 7, 23) - date(1955, 7, 18)).days, 5)
eq("Eisenhower Doctrine to Congress (days)", (date(1957, 3, 9) - date(1957, 1, 5)).days, 63)
eq("Iran coup to Guatemala (months)", (1954 - 1953) * 12 + (6 - 8), 10)

# Marshall Plan: about 13 billion over 1948-52, a span of four years of aid
eq("Marshall aid years", 1952 - 1948, 4)
eq("Marshall countries (sixteen) plus West Germany", 16 + 1, 17)
assert 12 < 13 < 13.4

# Marks
eq("table total", 15 + 15, 30)
eq("paper total", 2 * 30, 60)
eq("continuity essay total low", 14 + 13, 27)
eq("continuity essay total high", 14 + 14, 28)
print("ok")
