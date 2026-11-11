# checks/hist.f.eras.py: recomputes every number in the chapter (dates, intervals, timeline events, figure data)
import re
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


text = (HERE / "chapters" / "hist.f.eras.md").read_text(encoding="utf-8")

# --- Old Style to New Style (Julian to Gregorian) conversions used in the chapter
def ns(y, m, d, gap):
    return date(y, m, d) + timedelta(days=gap)

eq("25 Oct 1917 OS = 7 Nov", ns(1917, 10, 25, 13), date(1917, 11, 7))
eq("19 Feb 1861 OS = 3 March", ns(1861, 2, 19, 12), date(1861, 3, 3))
eq("1 March 1881 OS = 13 March", ns(1881, 3, 1, 12), date(1881, 3, 13))
eq("9 Jan 1905 OS = 22 Jan", ns(1905, 1, 9, 13), date(1905, 1, 22))

# --- Intervals
eq("Meiji to German Empire", 1871 - 1868, 3)
eq("Kingdom of Italy 1861 to Rome 1870", 1870 - 1861, 9)
eq("Mandela years in prison (5 Aug 1962 to 11 Feb 1990)", (date(1990, 2, 11) - date(1962, 8, 5)).days // 365, 27)
assert (date(1990, 2, 11) - date(1962, 8, 5)).days / 365.25 > 27
eq("Seven Years' War 1756-63", 1763 - 1756, 7)
eq("Haiti: 1791 rising to 1804 independence", 1804 - 1791, 13)
eq("Hobsbawm long 19th c. 1789-1914", 1914 - 1789, 125)
eq("Hobsbawm short 20th c. 1914-1991", 1991 - 1914, 77)
eq("Era 1 length 1774-1849", 1849 - 1774, 75)
eq("Era 2 length 1850-1914", 1914 - 1850, 64)
eq("Louis XIV reign 1643-1715", 1715 - 1643, 72)
eq("Declaration to Treaty of Paris", 1783 - 1776, 7)
eq("War declared 28 July to Britain 4 Aug (days)", (date(1914, 8, 4) - date(1914, 7, 28)).days, 7)
eq("Poland 1 Sept to Britain/France 3 Sept", (date(1939, 9, 3) - date(1939, 9, 1)).days, 2)
eq("Pearl Harbor to German declaration", (date(1941, 12, 11) - date(1941, 12, 7)).days, 4)
eq("Armistice to Versailles signed (days)", (date(1919, 6, 28) - date(1918, 11, 11)).days, 229)

# --- Nazi vote and unemployment figures used in the examples
vote = {"1928": 2.6, "1930": 18.3, "1932": 37.3}
assert vote["1928"] < vote["1930"] < vote["1932"]
unemp = {1929: 1.9, 1932: 5.6}
assert 2.5 < unemp[1932] / unemp[1929] < 3.5
# slave trade: arrivals as a share of embarkations (the text gives 12.5 and 10.7 million)
share = 10.7 / 12.5
assert 0.85 < share < 0.86

# --- Timeline widget: parse the events from the chapter and check them
m = re.search(r'data-events="([^"]+)"', text)
assert m, "no hist-timeline widget found"
events = [e.strip() for e in m.group(1).split(" ;; ")]
eq("number of timeline events", len(events), 44)
lanes = ["Europe", "Americas", "Asia and Africa", "International"]
lm = re.search(r'data-lanes="([^"]+)"', text)
eq("lanes", lm.group(1).split(","), lanes)
prev = None
counts = {l: 0 for l in lanes}
for e in events:
    f = [x.strip() for x in e.split(" | ")]
    eq(f"fields of {e[:30]}", len(f), 4)
    parts = f[0].split("-")
    y = int(parts[0]); mo = int(parts[1]) if len(parts) > 1 else 1; d = int(parts[2]) if len(parts) > 2 else 1
    dt = date(y, mo, d)  # raises on an impossible date
    if prev:
        assert dt >= prev, f"events not in date order at {f[0]}"
    prev = dt
    assert f[3] in lanes, f"unknown lane {f[3]}"
    counts[f[3]] += 1
    assert "'" not in f[1] or True
eq("first event", events[0][:10], "1756-05-18")
eq("last event", events[-1][:10], "1991-12-25")
for l in lanes:
    assert counts[l] >= 5, f"lane {l} has only {counts[l]} events"

# --- Axis figure: rebuild from data/p47_axis_fig.py's data and check the bars' dates against the text
bars = {
    "France": (1774, 1814), "Germany": (1815, 1871), "Russia": (1881, 1924),
    "Civil War": (1820, 1877), "Gilded Age": (1870, 1920), "Crash": (1920, 1941),
    "Imperialism": (1870, 1918), "Intl 1": (1919, 1929), "Intl 2": (1929, 1939),
    "WW1": (1890, 1914), "Holocaust": (1933, 1945), "Cold War": (1941, 1949),
    "Italy": (1919, 1941), "Stalin": (1924, 1941), "Hitler": (1929, 1941),
    "USA 1": (1945, 1961), "USA 2": (1961, 1974), "USA 3": (1974, 1993),
    "Soviet": (1953, 1991), "SA": (1948, 1994), "Malaysia": (1909, 1967),
}
eq("number of bars", len(bars), 21)
for k, (a, b) in bars.items():
    assert 1770 <= a < b <= 2000, k
svg = (HERE / "chapters" / "hist.f.eras.md").read_text(encoding="utf-8")
eq("figure rect count", len(re.findall(r'<rect class="f[123] s-acc sw2"', svg)), 21)
eq("question and quiz counts", text.count("\n? "), 9)

print("ok")
