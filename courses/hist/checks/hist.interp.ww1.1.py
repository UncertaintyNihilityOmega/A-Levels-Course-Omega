# checks/hist.interp.ww1.1.py: recomputes every number in the chapter (date arithmetic, ratios, timeline events, figure layout)
import os, re, sys
from datetime import date, datetime, timedelta

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs

text = open(os.path.join(here, "..", "chapters", "hist.interp.ww1.1.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# "Thirty-seven days later": Sarajevo 28 June to Britain's declaration 4 August
eq("days Sarajevo to British declaration", (date(1914, 8, 4) - date(1914, 6, 28)).days, 37)
# weekdays: Sarajevo Sunday, ultimatum Thursday, deadline Saturday
eq("28 June 1914 is a Sunday", date(1914, 6, 28).weekday(), 6)
eq("23 July 1914 is a Thursday", date(1914, 7, 23).weekday(), 3)
eq("25 July 1914 is a Saturday", date(1914, 7, 25).weekday(), 5)
# ultimatum delivered 6 pm 23 July, 48 hours -> 6 pm 25 July
eq("ultimatum deadline", datetime(1914, 7, 23, 18) + timedelta(hours=48), datetime(1914, 7, 25, 18))
eq("days from ultimatum to Austria's declaration", (date(1914, 7, 28) - date(1914, 7, 23)).days, 5)
eq("days from blank cheque to ultimatum", (date(1914, 7, 23) - date(1914, 7, 5)).days, 18)
eq("days from blank cheque to war on Britain", (date(1914, 8, 4) - date(1914, 7, 5)).days, 30)
# Princip born 25 July 1894 (New Style): 19 on 28 June 1914
b, d = date(1894, 7, 25), date(1914, 6, 28)
eq("Princip's age", d.year - b.year - ((d.month, d.day) < (b.month, b.day)), 19)
# Old Style: 13 days behind in 1914 -> 17 July OS = 30 July NS
eq("Old Style 17 July", date(1914, 7, 17) + timedelta(days=13), date(1914, 7, 30))
# Franz Joseph reigned 1848-1916
eq("Franz Joseph reign", 1916 - 1848, 68)
# alliance and treaty intervals
eq("Dual Alliance to 1914", 1914 - 1879, 35)
eq("Treaty of Frankfurt to 1914", 1914 - 1871, 43)
eq("Bosnia annexation to Sarajevo", 1914 - 1908, 6)
# Balkan Wars: First War October 1912, Bucharest 10 August 1913 -> about ten months
months = (1913 - 1912) * 12 + (8 - 10)
eq("Balkan Wars months (October 1912 to August 1913)", months, 10)
# Germany: population 41 -> 65 million, steel 17.6 vs 7.7 (more than double)
between("German population growth", 65 / 41, 1.55, 1.6)
between("steel ratio", 17.6 / 7.7, 2.2, 2.4)
between("France/Germany population", 39 / 65, 0.55, 0.65)
# Habsburg: Germans and Magyars together under half (1910 census shares about 24 and 20 per cent)
assert 24 + 20 < 50
# Tirpitz asked for about eighteen months: 1.5 years
eq("eighteen months", 18 / 12, 1.5)
# September Programme 9 September 1914, 36 days after the British declaration
eq("September Programme after British declaration", (date(1914, 9, 9) - date(1914, 8, 4)).days, 36)

# timeline widget: all dates valid, lanes consistent, event count
m = re.search(r'data-lanes="([^"]*)" data-events="([^"]*)"', text)
lanes = [x.strip() for x in m.group(1).split(",")]
events = [e for e in m.group(2).split(" ;; ") if e.strip()]
eq("timeline events", len(events), 21)
last = None
for e in events:
    f = [x.strip() for x in e.split(" | ")]
    assert len(f) == 4, f"bad event: {e[:40]}"
    dt = datetime.strptime(f[0], "%Y-%m-%d")
    assert last is None or dt >= last, f"out of order: {f[0]}"
    last = dt
    assert f[3] in lanes, f"unknown lane {f[3]}"
eq("lanes", len(lanes), 6)

# figure layout
eq("one svg", check_svgs(text), 1)
print("ok")
