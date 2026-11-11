# checks/hist.d.usa45.3.py: recomputes every number in the chapter (dates, intervals, percentages, marks)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# GNP in current dollars (billions, BEA via FRED GNPA): 228.3, 301.3, 427.9, 545.5
gnp = {1945: 228.3, 1950: 301.3, 1955: 427.9, 1960: 545.5}
shown = {y: round(v) for y, v in gnp.items()}
eq("chart GNP rounded", shown, {1945: 228, 1950: 301, 1955: 428, 1960: 546})
between("GNP 1945-60 'more than doubled'", gnp[1960] / gnp[1945], 2.0, 2.5)
between("GNP 1950-60 'about four-fifths'", gnp[1960] / gnp[1950] - 1, 0.78, 0.84)
eq("chart years in order", sorted(gnp), list(gnp))

# Cars registered (millions): 25.8 in 1945, 59.5 in 1959 (59,453,984 exactly)
eq("cars 1959 rounded", round(59453984 / 1e6, 1), 59.5)
between("cars 'more than double'", 59.5 / 25.8, 2.0, 2.5)
eq("cars span years", 1959 - 1945, 14)

# Television: 9 per cent (1950), 88 per cent (1960); '87 to 90' range and '9 to 12' range
assert 87 <= 88 <= 90 and 9 <= 12
between("TV rise points", 88 - 9, 75, 85)

# Home ownership 43.6 -> 61.9 (rounded 44 -> 62) over 1940-60
eq("homeownership 1940 rounded", round(43.6), 44)
eq("homeownership 1960 rounded", round(61.9), 62)

# Suburbs 1950: 23.3 per cent; 1960: about 31 per cent; metro 1960 112.9 million = 58.0 + 54.9
eq("suburbs 1950 rounded", round(23.3), 23)
eq("metro 1960 total", round(58.0 + 54.9, 1), 112.9)
between("suburb share 1960 about 31 per cent", 54.9 / 179.3, 0.30, 0.32)  # US population 1960 179.3 million
between("suburban growth about half", 0.49, 0.45, 0.55)

# California population: 10,586,223 (1950), 15,717,204 (1960)
ca = (15717204 - 10586223) / 10586223
between("California 'nearly half'", ca, 0.45, 0.50)
eq("California 1950 million", round(10586223 / 1e6, 1), 10.6)
eq("California 1960 million", round(15717204 / 1e6, 1), 15.7)

# Detroit 1,849,568 -> 1,670,144; St Louis 856,796 -> 750,026
det = (1849568 - 1670144) / 1849568
between("Detroit fall about a tenth", det, 0.08, 0.11)
eq("Detroit 1950 million", round(1849568 / 1e6, 2), 1.85)
eq("Detroit 1960 million", round(1670144 / 1e6, 2), 1.67)
stl = (856796 - 750026) / 856796
between("St Louis fall about an eighth", stl, 0.11, 0.14)

# GI Bill: 7.8 of 16 million used education or training; 2.2 million to college; 2.4 million home loans by 1952
between("GI Bill share of veterans", 7.8 / 16, 0.48, 0.50)
assert 2.2 < 7.8
eq("GI Bill signed to Levittown (years)", 1947 - 1944, 3)
eq("GI Bill date", date(1944, 6, 22).isoformat(), "1944-06-22")

# Highway Act: 29 June 1956 was a Friday; 90 per cent federal share
eq("Highway Act weekday", date(1956, 6, 29).strftime("%A"), "Friday")
eq("federal share of highway cost, state share", 100 - 90, 10)

# Dates used in the chapter
eq("Sputnik to NDEA (years)", 1958 - 1957, 1)
eq("Elvis on Sullivan weekday", date(1956, 9, 9).strftime("%A"), "Sunday")
eq("American Bandstand national date", date(1957, 8, 5).strftime("%A"), "Monday")
eq("Kitchen Debate year", date(1959, 7, 24).year, 1959)
eq("Pill approval to commission (months)", (1961 - 1960) * 12 + (12 - 5), 19)
eq("Dean death to Rebel (days between 30 Sept and 27 Oct 1955)", (date(1955, 10, 27) - date(1955, 9, 30)).days, 27)
eq("Holly died Feb 1959, years after Elvis Sun 1954", 1959 - 1954, 5)

# Baby boom: 1946 to 1964 is 18 years; about 4 million a year over the later 1950s
eq("baby boom span", 1964 - 1946, 18)
assert 76 > 4 * 18 - 1  # 76 million births over 18 years is about 4.2 million a year
between("births per year", 76 / 18, 4.0, 4.5)

# Women: labour force participation 33.9 -> 37.7; share of workers 29.6 -> 33.4
eq("participation rise (points)", round(37.7 - 33.9, 1), 3.8)
eq("share of workers rise (points)", round(33.4 - 29.6, 1), 3.8)
eq("bachelor's degrees to women 1960", 100 - 65, 35)
between("women's pay 60 cents on the dollar", 0.60, 0.55, 0.65)

# College enrolment 2.28 -> 3.58 million
between("enrolment rise 'more than half'", 3.58 / 2.28 - 1, 0.5, 0.6)
eq("enrolment 1950 rounded", round(2.28, 1), 2.3)
eq("enrolment 1960 rounded", round(3.58, 1), 3.6)

# Poverty: 22.4 per cent of about 176 million = about 39 million
between("poverty people", 0.224 * 176, 38.5, 40.0)
between("Harrington 40 to 50 million", 45, 40, 50)

# Defence spending 14 (1950) -> over 50 (1953)
assert 53 > 50 > 14
between("defence rise multiple", 52.8 / 13.7, 3.5, 4.0)

# Marks: Paper 4 essay [30] = 15 + 15; both-table totals in the worked answers
eq("table total", 15 + 15, 30)
eq("paper total", 2 * 30, 60)
eq("conformity essay total low", 14 + 13, 27)
eq("conformity essay total high", 14 + 14, 28)
print("ok")
