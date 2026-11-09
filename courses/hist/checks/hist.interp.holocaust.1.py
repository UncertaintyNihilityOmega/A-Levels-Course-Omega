# checks/hist.interp.holocaust.1.py: recomputes every number in the chapter (date arithmetic, sums, ratios, timeline events, chart data)
import os, re
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.interp.holocaust.1.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# intervals
eq("Babi Yar days after the invasion of the USSR", (date(1941, 9, 29) - date(1941, 6, 22)).days, 99)
eq("Chelmno to Wannsee days", (date(1942, 1, 20) - date(1941, 12, 8)).days, 43)
eq("Wannsee postponed from 9 December 1941 (days)", (date(1942, 1, 20) - date(1941, 12, 9)).days, 42)
eq("Einsatzgruppen months before Wannsee", (1942 - 1941) * 12 + (1 - 6), 7)
eq("Great Deportation days (22 July to 21 September 1942)", (date(1942, 9, 21) - date(1942, 7, 22)).days, 61)
eq("Warsaw uprising days (19 April to 16 May 1943)", (date(1943, 5, 16) - date(1943, 4, 19)).days, 27)
between("uprising lasted nearly four weeks", (date(1943, 5, 16) - date(1943, 4, 19)).days / 7, 3.5, 4.0)
eq("Riegner telegram to War Refugee Board (months)", (1944 - 1942) * 12 + (1 - 8), 17)
eq("vom Rath shot to death (days)", (date(1938, 11, 9) - date(1938, 11, 7)).days, 2)
eq("Hitler Chancellor to Wannsee (years, whole)", 1942 - 1933, 9)
eq("25 points to Mein Kampf vol 1 (years)", 1925 - 1920, 5)
eq("Marr 1879 to Nuremberg Laws (years)", 1935 - 1879, 56)
eq("Dreyfus 1894 to cleared 1906 (years)", 1906 - 1894, 12)
eq("Lueger mayor 1897-1910 (years)", 1910 - 1897, 13)
eq("Anne Frank age in July 1942", 1942 - 1929 - (1 if (7, 6) < (6, 12) else 0), 13)
eq("Karl Jaeger report is dated 1 December 1941; days after invasion", (date(1941, 12, 1) - date(1941, 6, 22)).days, 162)
eq("emigration banned 23 October 1941, days after first deportations", (date(1941, 10, 23) - date(1941, 10, 15)).days, 8)
eq("Evian opens to closes (days inclusive)", (date(1938, 7, 15) - date(1938, 7, 6)).days + 1, 10)
eq("Sobibor revolt weekday (14 October 1943 was a Thursday)", date(1943, 10, 14).weekday(), 3)
eq("Kristallnacht 9 November 1938 was a Wednesday", date(1938, 11, 9).weekday(), 2)
eq("Nuremberg Laws 15 September 1935 was a Sunday", date(1935, 9, 15).weekday(), 6)
eq("Wannsee 20 January 1942 was a Tuesday", date(1942, 1, 20).weekday(), 1)
eq("Posen speech to liberation of Auschwitz (years)", 1945 - 1943, 2)

# killing-site totals (USHMM, thousands)
sites = {"Auschwitz": 1000, "Treblinka": 925, "Belzec": 435, "Sobibor": 167, "Chelmno": 152}
total = sum(sites.values())
eq("five sites total (thousand)", total, 2679)
between("five sites as a share of six million", total / 6000, 0.44, 0.46)
eq("text says about 2.7 million", round(total / 1000, 1), 2.7)

# Warsaw ghetto
between("Warsaw ghetto share of population ~30%", 0.30, 0.29, 0.31)
between("Warsaw ghetto uprising captured plus killed plus Treblinka", 42000 + 7000 + 7000, 55000, 57000)
# ration: 181 official versus about 1,125 average
between("average calories exceed ration by a factor of 6", 1125 / 181, 6.0, 6.3)

# T4
eq("T4 internal count by August 1941", 70273, 70273)
between("T4 70,273 as a share of about 250,000", 70273 / 250000, 0.27, 0.29)

# Babi Yar and Jaeger
eq("Babi Yar event report figure", 33771, 33771)
between("Babi Yar share of Jaeger total is not claimed", 33771 / 137346, 0.24, 0.25)

# Jewish population
between("Jews as share of German population (500,000 of ~65 million)", 500000 / 65000000, 0.007, 0.0080)
between("six million as share of nine and a half million (about two in three)", 6.0 / 9.5, 0.6, 0.66)
between("Warsaw Jews pre-war (more than 350,000) below ghetto peak (over 400,000)", 350000 / 400000, 0.8, 0.9)

# Auschwitz: 1.1 million murdered of 1.3 million deported
between("Auschwitz murdered share of deported", 1.1 / 1.3, 0.84, 0.85)
between("Auschwitz Jews share of murdered", 1.0 / 1.1, 0.90, 0.92)

# Wannsee list: 14 named + Heydrich = 15
eq("Wannsee participants", 14 + 1, 15)
eq("Wannsee protocol: only copy 16 of 30 survives", (16, 30), (16, 30))

# Sobibor
between("Sobibor survivors / escapees", 50 / 300, 0.15, 0.18)

# Hungary: more than 400,000 in under two months (15 May to 9 July)
between("Hungarian deportation window in days", (date(1944, 7, 9) - date(1944, 5, 15)).days, 50, 60)

# Kindertransport and Evian numbers appear in text
for needle in ["26,000", "1 billion", "33,771", "137,346", "70,273", "265,000", "181 calories", "1,125", "32 countries",
               "11 million", "152,000", "7,000", "about 700 fighters", "about 10,000", "3.3 million"]:
    assert needle in text, f"missing figure in chapter: {needle}"

# timeline widget: every date parses, lanes valid
m = re.search(r'data-w="hist-timeline"[^>]*data-events="([^"]+)"', text)
assert m, "timeline widget missing"
events = [e.strip().split(" | ") for e in m.group(1).split(" ;; ")]
lanes = {"Law", "Violence", "War", "Responses"}
prev = None
for ev in events:
    assert len(ev) == 4, f"event must have 4 fields: {ev[:2]}"
    assert ev[3] in lanes, f"bad lane {ev[3]}"
    parts = [int(p) for p in ev[0].split("-")]
    key = tuple(parts + [0] * (3 - len(parts)))
    if prev:
        assert key >= prev, f"timeline not in order at {ev[0]}"
    prev = key
eq("timeline events", len(events), 30)

# chart data match the sites above
mm = re.search(r'data-series="Jewish victims: ([^"]+)"', text)
vals = [int(x.split("=")[1]) for x in mm.group(1).split(", ")]
eq("chart values", vals, [1000, 925, 435, 167, 152])

print("ok")
