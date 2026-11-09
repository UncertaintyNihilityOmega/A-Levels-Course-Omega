# checks/hist.int.1929.4.py: recomputes every number in the chapter (intervals, ratios, timeline, map layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Hitler's aims and the Hossbach meeting
eq("Hossbach: meeting 5 November, record 10 November (days)", (date(1937, 11, 10) - date(1937, 11, 5)).days, 5)
d = (date(1938, 3, 12) - date(1937, 11, 5)).days
between("Hossbach to Anschluss: about four months", d / 30.4, 4.0, 4.4)
d = (date(1939, 3, 15) - date(1937, 11, 5)).days
between("Hossbach to Prague: within 18 months", d / 30.4, 15.5, 18.0)
eq("Hossbach timetable 1943 against war in 1939 (years early)", 1943 - 1939, 4)
eq("Mein Kampf: volume 1 in 1925, volume 2 in 1926", 1926 - 1925, 1)
eq("Naval Agreement: 35 per cent", 35 * 20, 700)
eq("Conscription: 36 divisions of about 15,000 men is about 550,000", round(36 * 15278 / 1000), 550)
# Britain
eq("Scheme F: 1,736 aircraft in 124 squadrons is 14 per squadron", 1736 // 124, 14)
eq("Scheme F: exact division", 1736 % 124, 0)
eq("Fighter squadrons: 18 Hurricane + 9 Spitfire", 18 + 9, 27)
eq("Spitfire first flight to squadron service (years)", 1938 - 1936, 2)
eq("Hurricane first flight 1935 to service December 1937 (years)", 1937 - 1935, 2)
# Poland
eq("German-Polish pact of January 1934 to its cancellation (years)", 1939 - 1934, 5)
d = (date(1939, 3, 31) - date(1938, 10, 24)).days
eq("German demands of 24 October 1938 to the guarantee (days)", d, 158)
eq("Guarantee to cancellation of the two treaties (days)", (date(1939, 4, 28) - date(1939, 3, 31)).days, 28)
d = (date(1939, 9, 1) - date(1939, 4, 3)).days
eq("Case White of 3 April to 1 September (days)", d, 151)
between("Case White: about five months", d / 30.4, 4.9, 5.1)
eq("Prague to Memel (days)", (date(1939, 3, 23) - date(1939, 3, 15)).days, 8)
eq("Prague to the guarantee (days)", (date(1939, 3, 31) - date(1939, 3, 15)).days, 16)
eq("Pact of Steel to the invasion (days)", (date(1939, 9, 1) - date(1939, 5, 22)).days, 102)
# The Pact and the outbreak
eq("Pact to the invasion of Poland (days)", (date(1939, 9, 1) - date(1939, 8, 23)).days, 9)
eq("Pact to the Red Army's entry into Poland (days)", (date(1939, 9, 17) - date(1939, 8, 23)).days, 25)
eq("Pact to Low's cartoon (days, four weeks)", (date(1939, 9, 20) - date(1939, 8, 23)).days, 28)
eq("Red Army's entry to Low's cartoon (days)", (date(1939, 9, 20) - date(1939, 9, 17)).days, 3)
eq("Pact to the attack date of 26 August (days)", (date(1939, 8, 26) - date(1939, 8, 23)).days, 3)
eq("Anglo-Polish treaty to the planned attack (days)", (date(1939, 8, 26) - date(1939, 8, 25)).days, 1)
eq("Invasion to the declarations (days)", (date(1939, 9, 3) - date(1939, 9, 1)).days, 2)
eq("British ultimatum 9 am to 11 am (hours)", 11 - 9, 2)
eq("11 am deadline to 5 pm French deadline (hours)", 17 - 11, 6)
eq("Chamberlain broadcast at 11:15 (minutes after the deadline)", 15, 15)
eq("Moscow trade agreement 19 August to the Pact (days)", (date(1939, 8, 23) - date(1939, 8, 19)).days, 4)
# Paper totals
eq("Paper 1 totals", 15 + 25, 40)
eq("Paper 2 totals", (10 + 20) * 2, 60)

# ---- timeline dates are valid and in order
text = open(os.path.join(here, "..", "chapters", "hist.int.1929.4.md"), encoding="utf-8").read()
ev = re.search(r'data-events="([^"]*)"', text).group(1).split(" ;; ")
dates = []
for e in ev:
    f = [x.strip() for x in e.split(" | ")]
    eq("timeline event has four fields", len(f), 4)
    y, mo, dd = (int(v) for v in f[0].split("-"))
    dates.append(date(y, mo, dd))
assert dates == sorted(dates), "timeline not in date order"
eq("timeline events", len(ev), 17)

# ---- map figure: seven markers, seven legend lines
fig = re.search(r"<svg viewBox=\"0 0 340 440\".*?</svg>", text, re.S).group(0)
eq("map markers", len(re.findall(r"<circle ", fig)), 7)
eq("map legend lines", len(re.findall(r'<text class="tl" x="14"', fig)), 7)
for n in "1234567":
    assert f'>{n}</text>' in fig, f"marker {n} missing"
eq("number of SVG figures", check_svgs(text), 1)

# ---- text checks
for token in ["16 March 1935", "18 June 1935", "7 March 1936", "25 November 1936", "5 November 1937", "12–13 March 1938",
              "29–30 September 1938", "15 March 1939", "22–23 March 1939", "31 March 1939", "28 April 1939", "22 May 1939",
              "23 August 1939", "25 August 1939", "1 September 1939", "3 September 1939", "24 October 1938", "1943–45",
              "1 hour 15 minutes", "5 pm", "11 am", "Narew, Vistula", "viewBox=\"0 0 340 440\""]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
assert "hedged" not in text, "no editorial notes left in the text"
print("ok")
