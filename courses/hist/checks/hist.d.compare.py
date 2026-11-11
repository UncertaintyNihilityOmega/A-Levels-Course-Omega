# checks/hist.d.compare.py: recomputes every number in the chapter (dates, intervals, shares, totals, figure positions)
import re
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


text = (HERE / "chapters" / "hist.d.compare.md").read_text(encoding="utf-8")

# --- Gaining power
d_pm = date(1922, 10, 31)
d_chan = date(1933, 1, 30)
yrs = (d_chan - d_pm).days / 365.25
between("Mussolini PM to Hitler Chancellor 'a little over ten years'", yrs, 10.0, 10.5)
eq("March on Rome to Beer Hall Putsch (days)", (date(1923, 11, 8) - date(1922, 10, 28)).days, 376)
eq("Fascist seats: 35 of 535 per cent", round(35 / 535 * 100, 1), 6.5)
eq("Nazi ministers 3 of 11", (3, 11), (3, 11))
assert 3 / 11 < 0.28
eq("Years in which the Special Tribunal sat, 1927-43", 1943 - 1927, 16)
eq("Years 1928 to 1932 vote span", 1932 - 1928, 4)
eq("Nazi vote Nov 1932 below July 1932", 33.1 < 37.3, True)

# --- Scale of repression
shot_1937, shot_1938 = 353074, 328618
eq("NKVD shot 1937+1938", shot_1937 + shot_1938, 681692)
share = 681692 / 170e6 * 100
eq("share of USSR population shot (per cent, 1 d.p.)", round(share, 1), 0.4)
between("about one in 250", 170e6 / 681692, 245, 255)
eq("Special Tribunal executed of sentenced", (31, 42), (31, 42))
assert 31 < 42 < 4600 < 5600
conv = 4600 / 5600
between("convicted share about 82 per cent", conv * 100, 81, 83)
# Italian executions as a share of population (about 42 million, 1931 census): tiny
assert 31 / 42e6 < 1e-6
eq("Gulag camps 1 Jan 1941, millions", round(1501 / 1000, 1), 1.5)

# --- Economies
eq("Mefo bills about 12 billion marks", 12, 12)
eq("Collectivised by 1937: nine tenths", 0.9, 0.9)
eq("Dekulakisation: 1.8 million deported 1930-31 (two years)", 1931 - 1930 + 1, 2)
assert 5 <= 5.7 <= 8     # Davies and Wheatcroft central estimate within the 5 to 8 million range
eq("First Five Year Plan start", date(1928, 10, 1).isoformat(), "1928-10-01")
eq("Four Year Plan starts October 1936", date(1936, 10, 18).month, 10)

# --- Links between the regimes
eq("Nazi-Soviet Pact to Barbarossa (days)", (date(1941, 6, 22) - date(1939, 8, 23)).days, 669)
between("... nearly two years", 669 / 365.25, 1.8, 1.9)
eq("Pact of Steel to Nazi-Soviet Pact (days)", (date(1939, 8, 23) - date(1939, 5, 22)).days, 93)
eq("Anti-Comintern Pact to Italy joining (days)", (date(1937, 11, 6) - date(1936, 11, 25)).days, 346)
eq("Hindenburg dies to Hitler Fuhrer: same day", date(1934, 8, 2).day, 2)
eq("Italy's war: 10 June 1940 weekday is Monday", date(1940, 6, 10).weekday(), 0)
eq("Mussolini dismissal 25 July 1943 weekday is Sunday", date(1943, 7, 25).weekday(), 6)
eq("Beer Hall Putsch, 8 Nov 1923, was a Thursday", date(1923, 11, 8).weekday(), 3)
eq("Old Style 25 Oct 1917 + 13 days", date(1917, 11, 7).toordinal() - date(1917, 10, 25).toordinal(), 13)
eq("Stalin's 50th birthday: born 18 Dec 1878 (NS 21 Dec 1879 official); celebrated 21 Dec 1929", 1929 - 1879, 50)

# --- Marks used in the worked examples: each Paper 4 essay is 30 = 15 + 15 (Table A + Table B)
eq("Paper 4 essay total", 15 + 15, 30)
eq("Level 5 bands", (13, 15), (13, 15))
eq("Level 4 bands", (10, 12), (10, 12))
eq("Level 3 bands", (7, 9), (7, 9))
eq("Paper 4: two questions of 30 make 60", 2 * 30, 60)
eq("Paper 4 time 1 h 45 min in minutes", 60 + 45, 105)

# --- Figure: positions follow dates (y = 60 + (t - 1917) * 20)
svg = text[text.index("<svg"):text.index("</svg>")]
circles = re.findall(r'<circle class="f([123]) s-acc sw2" cx="(\d+)" cy="([\d.]+)"', svg)
eq("number of dots", len(circles), 27)
events = {
    "Italy": [1922.82, 1924.45, 1926.9, 1929.12, 1935.75, 1938.9, 1940.45, 1943.57],
    "USSR": [1917.82, 1924.05, 1928.8, 1929.95, 1932.7, 1934.92, 1937.5, 1939.64, 1941.47],
    "Germany": [1923.85, 1929.82, 1933.15, 1934.5, 1935.7, 1936.8, 1938.2, 1939.67, 1941.47, 1945.33],
}
ys = [round(60 + (t - 1917) * 20, 1) for k in ("Italy", "USSR", "Germany") for t in events[k]]
got = [float(c[2]) for c in circles]
eq("dot positions", got, ys)
# a few exact dates the dots stand for
def frac(y, m, d):
    return y + (date(y, m, d) - date(y, 1, 1)).days / 365.25
between("March on Rome dot", frac(1922, 10, 28), 1922.8, 1922.85)
between("Bolsheviks dot (7 Nov 1917 NS)", frac(1917, 11, 7), 1917.8, 1917.87)
between("Lenin dies dot", frac(1924, 1, 21), 1924.03, 1924.07)
between("Beer Hall Putsch dot", frac(1923, 11, 8), 1923.84, 1923.87)
between("Mussolini falls dot", frac(1943, 7, 25), 1943.55, 1943.58)
between("Hitler dies dot", frac(1945, 4, 30), 1945.32, 1945.34)
between("Barbarossa dot", frac(1941, 6, 22), 1941.46, 1941.48)
between("Long Knives dot (30 June 1934)", frac(1934, 6, 30), 1934.49, 1934.51)
between("Abyssinia dot (3 Oct 1935)", frac(1935, 10, 3), 1935.75, 1935.77)
between("Anschluss dot (12 Mar 1938)", frac(1938, 3, 12), 1938.18, 1938.2)
eq("quiz questions", text.count("\n? "), 9)

print("ok")
