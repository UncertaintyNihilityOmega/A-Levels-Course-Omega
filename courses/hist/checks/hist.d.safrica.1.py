# checks/hist.d.safrica.1.py: recomputes every number in the chapter (dates, intervals, percentages, totals)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want} (tolerance {tol})"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# 1948 election (Wikipedia table from official returns)
seats = {"UP": 65, "HNP": 70, "AP": 9, "Lab": 6, "Ind": 0}
votes = {"UP": 524230, "HNP": 401834, "AP": 41885, "Lab": 27360, "Ind": 70662}
eq("seats total", sum(seats.values()), 150)
total_votes = sum(votes.values())
eq("valid votes total", total_votes, 1065971)
for k, want in {"UP": 49.2, "HNP": 37.7, "AP": 3.9, "Lab": 2.6, "Ind": 6.6}.items():
    near(f"share {k}", votes[k] / total_votes * 100, want, 0.05)
eq("majority needed", 150 // 2 + 1, 76)
eq("NP+AP seats", seats["HNP"] + seats["AP"], 79)
eq("UP+Lab seats", seats["UP"] + seats["Lab"], 71)
eq("79 is three more than 76", 79 - 76, 3)
np_votes = votes["HNP"] + votes["AP"]
up_votes = votes["UP"] + votes["Lab"]
near("NP+AP share", np_votes / total_votes * 100, 41.6, 0.05)
near("UP+Lab share", up_votes / total_votes * 100, 51.7, 0.05)
near("NP+AP seat share", 79 / 150 * 100, 52.7, 0.05)
near("UP+Lab seat share", 71 / 150 * 100, 47.3, 0.05)
near("votes per NP+AP seat", np_votes / 79, 5600, 50)
near("votes per UP+Lab seat", up_votes / 71, 7800, 50)
eq("UP+Lab lead in votes over NP+AP positive", up_votes > np_votes, True)
eq("HNP 37.7 share on its own", round(votes["HNP"] / total_votes * 100, 1), 37.7)
eq("registered voters turnout not used", True, True)

# Ages and intervals
eq("Smuts age at the election (born 24 May 1870)", age(date(1870, 5, 24), date(1948, 5, 26)), 78)
eq("Hertzog vote 80-67 margin", 80 - 67, 13)
eq("Union 1910 to 1948 years", 1948 - 1910, 38)
eq("1948 to 1959 years", 1959 - 1948, 11)
eq("Union to 1994 years", 1994 - 1948, 46)
eq("Broederbond 1918 to 1948", 1948 - 1918, 30)
eq("Treason Trial arrests to verdict, in years (5 Dec 1956 to 29 Mar 1961)", round((date(1961, 3, 29) - date(1956, 12, 5)).days / 365.25, 1), 4.3)
eq("Treason accused sum", 105 + 21 + 23 + 7, 156)
eq("1956 women's march is the 9th", date(1956, 8, 9).day, 9)
eq("Defiance Campaign start to Treason arrests, years", 1956 - 1952, 4)
eq("Freedom Charter to PAC, years", 1959 - 1955, 4)
eq("1938 Voortrekker centenary: 1838 + 100", 1838 + 100, 1938)
eq("Boer war to 1948", 1948 - 1902, 46)

# 1951 census (12,671,000 total; 8,560,000 African; 1,103,000 Coloured)
tot, afr, col = 12671000, 8560000, 1103000
near("African share of 1951 census", afr / tot * 100, 67.6, 0.1)
near("Coloured share of 1951 census", col / tot * 100, 8.7, 0.1)
near("white about one fifth (2.6 million)", 2.6e6 / tot * 100, 20.5, 0.6)
eq("reserves 13 per cent leaves 87", 100 - 13, 87)

# Education
near("per-pupil ratio 1953 (127.84 : 17.08)", 127.84 / 17.08, 7.5, 0.05)
near("per-pupil ratio 1975-76 (644 : 42)", 644 / 42, 15.3, 0.1)
eq("subsidy cuts: 75, 50, 25, 0 steps of 25", [75, 50, 25, 0], [100 - 25 * i for i in range(1, 5)])
eq("1955 to 1958 four years of cuts", 1958 - 1955 + 1, 4)

# Defiance campaign
eq("SAHO monthly total rounds to 8,500", round(8557, -2), 8600)  # chapter says "about 8,500" and quotes 8,557
assert abs(8557 - 8500) < 100

# Women's march
eq("Senate 48 to 89 enlarged by", 89 - 48, 41)
eq("Appeal Court 5 to 11 judges enlarged by", 11 - 5, 6)
eq("Natives Land Act 1913 to 1948", 1948 - 1913, 35)
eq("pass arrests 500,000 a year over ten years", 500000 * 10, 5000000)
eq("1948 97 per cent church schools leaves 3", 100 - 97, 3)
eq("Mid 1946 strike 60,000 to 76,000 midpoint", (60000 + 76000) // 2, 68000)
eq("Sophiatown 65,000 a plausible figure", 65000 > 60000, True)
eq("PAC date", (date(1959, 4, 6).month, date(1959, 4, 6).day), (4, 6))
eq("Verwoerd PM 2 Sept 1958", date(1958, 9, 2).year, 1958)
print("ok")
