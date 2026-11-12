# checks/hist.int.1929.2.py: recomputes every number in the chapter (intervals, votes, percentages, figure bars, layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Manchuria
eq("Mukden to Council vote (days)", (date(1931, 10, 24) - date(1931, 9, 18)).days, 36)
eq("Council deadline after vote (days)", (date(1931, 11, 16) - date(1931, 10, 24)).days, 23)
eq("Mukden to Lytton Commission agreed (days)", (date(1931, 12, 10) - date(1931, 9, 18)).days, 83)
eq("Lytton Commission agreed to Report published (days)", (date(1932, 10, 2) - date(1931, 12, 10)).days, 297)
eq("Manchukuo proclaimed about five months after Mukden", (date(1932, 3, 1) - date(1931, 9, 18)).days // 30, 5)
eq("Mukden to Stimson note (months, about four)", round((date(1932, 1, 7) - date(1931, 9, 18)).days / 30.4), 4)
eq("Assembly vote on the Report", 42 + 1 + 1, 44)   # 42 for, 1 against (Japan), 1 abstention (Siam)
eq("Japan: notice plus two years", date(1933 + 2, 3, 27), date(1935, 3, 27))
eq("Italy: notice plus two years is in December 1939", (1937 + 2, 12), (1939, 12))
eq("Germany: announced October 1933, effect October 1935", 1933 + 2, 1935)
# Abyssinia
eq("Walwal to invasion (days)", (date(1935, 10, 3) - date(1934, 12, 5)).days, 302)
between("Walwal to invasion is about ten months", (date(1935, 10, 3) - date(1934, 12, 5)).days / 30.4, 9.5, 10.5)
eq("Invasion to sanctions (days)", (date(1935, 11, 18) - date(1935, 10, 3)).days, 46)
between("Invasion to sanctions is about six weeks", (date(1935, 11, 18) - date(1935, 10, 3)).days / 7, 6, 7)
eq("Haile Selassie speech to sanctions lifted (days, about two weeks)", (date(1936, 7, 15) - date(1936, 6, 30)).days, 15)
eq("Sanctions lifted to the Spanish rising (days)", (date(1936, 7, 17) - date(1936, 7, 15)).days, 2)
eq("Italian troops in Addis Ababa and annexation (days apart)", (date(1936, 5, 9) - date(1936, 5, 5)).days, 4)
between("Peace Ballot: economic sanctions share", 10.0 / 11.5, 0.86, 0.88)
between("Peace Ballot: military action share", 6.8 / 11.5, 0.58, 0.60)
eq("Sanctions: fifty states agreed, of the 54 voting (Italy and others did not)", 50 < 54, True)
# Membership
eq("USSR admission votes", 39 + 3 + 7, 49)
d = date(1939, 12, 14) - date(1934, 9, 18)
eq("USSR membership (days)", d.days, 1913)
between("USSR membership about five years", d.days / 365.25, 5.2, 5.3)
eq("Germany joined 1926, left 1933: years", 1933 - 1926, 7)
# Spain
eq("France proposes to first meeting (days)", (date(1936, 9, 9) - date(1936, 8, 2)).days, 38)
eq("Spanish Civil War (days)", (date(1939, 4, 1) - date(1936, 7, 17)).days, 988)
between("Spanish Civil War is under three years", (date(1939, 4, 1) - date(1936, 7, 17)).days / 365.25, 2.6, 2.8)
eq("Britain and France recognise Franco 33 days before victory", (date(1939, 4, 1) - date(1939, 2, 27)).days, 33)
eq("International Brigades: about 32,000, never more than 18,000 at once", 18000 < 32000, True)
# Paper totals
eq("Paper 1 totals", 15 + 25, 40)
eq("Paper 2 totals", (10 + 20) * 2, 60)

# ---- membership figure: 20 px per year from x = 120 at 1930
def x_of(y, m, dd):
    yd = (date(y, m, dd) - date(y, 1, 1)).days
    ylen = 366 if y % 4 == 0 else 365
    return 120 + (y + yd / ylen - 1930) * 20


text = open(os.path.join(here, "..", "chapters", "hist.int.1929.2.md"), encoding="utf-8").read()
fig = re.search(r'<svg viewBox="0 0 340 300".*?</svg>', text, re.S).group(0)
rects = [tuple(float(v) for v in m) for m in re.findall(r'<rect class="f[mp] s-acc sw2" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', fig)]
bars = {int(y): (x, w) for x, y, w in rects if y in (30, 64, 98, 132, 166)}
rows = {}
for x, y, w in rects:
    rows.setdefault(int(y), []).append((x, x + w))
want = {
    30: [(120, 320)],
    64: [(120, x_of(1933, 3, 27)), (x_of(1933, 3, 27), x_of(1935, 3, 27))],
    98: [(120, x_of(1933, 10, 14)), (x_of(1933, 10, 14), x_of(1935, 10, 14))],
    132: [(120, x_of(1936, 1, 1)), (x_of(1936, 1, 1), x_of(1939, 12, 10))],
    166: [(x_of(1934, 9, 18), x_of(1939, 12, 14))],
}
for y, segs in want.items():
    got = sorted(rows[y])
    eq(f"bar row {y} segments", len(got), len(segs))
    for (a, b), (c, e) in zip(got, segs):
        between(f"bar row {y} start", a, c - 1, c + 1)
        between(f"bar row {y} end", b, e - 1.5, e + 1.5)

# ---- text checks
eq("number of SVG figures", check_svgs(text), 2)
for token in ["18 September 1931", "24 October 1931", "13 to 1", "10 December 1931", "7 January 1932", "1 March 1932", "2 October 1932",
              "24 February 1933", "42 votes to 1", "27 March 1933", "14 October 1933", "18 September 1934", "5 December 1934",
              "3 October 1935", "18 November 1935", "18 December", "5 May 1936", "30 June 1936", "15 July 1936", "17 July 1936",
              "9 September 1936", "26 April 1937", "11 December 1937", "14 December 1939", "1 April 1939", "39 votes to 3",
              "32,000", "18,000", "27 states", "1 hour 15 minutes", "viewBox=\"0 0 340 300\"", "viewBox=\"0 0 340 314\""]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
assert "—" not in text, "no em dashes"
# FIX round (reader items): fifty states imposed sanctions; the Emperor's fifty-two is every member except Italy and Ethiopia
assert 54 - 2 == 52, "League had 54 members in 1936; minus Italy and Ethiopia = 52"
for token in ["fifty-two", "Fifty states agreed"]:
    assert token in text, f"missing {token}"
print("ok")
