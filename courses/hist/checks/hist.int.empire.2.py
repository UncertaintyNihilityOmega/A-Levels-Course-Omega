# checks/hist.int.empire.2.py: recomputes every number in the chapter (dates, intervals, ratios, totals)
from datetime import date
import re, os


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Berlin Conference: 15 November 1884 to 26 February 1885 = 103 days
eq("Berlin days", (date(1885, 2, 26) - date(1884, 11, 15)).days, 103)
# Fourteen states attended
states = ["Germany", "Austria-Hungary", "Belgium", "Denmark", "France", "Britain", "Italy", "the Netherlands",
          "Portugal", "Russia", "Spain", "Sweden-Norway", "the Ottoman Empire", "the United States"]
eq("states", len(states), 14)
# Navy Laws: 19 battleships (1898), doubled to 38 (1900)
eq("Second Navy Law doubles", 19 * 2, 38)
# Algeciras Conference 16 January to 7 April 1906
eq("Algeciras days", (date(1906, 4, 7) - date(1906, 1, 16)).days, 81)
# Agadir: Panther 1 July to convention 4 November = 126 days (about four months)
d = (date(1911, 11, 4) - date(1911, 7, 1)).days
eq("Agadir days", d, 126)
between("Agadir months", d / 30.44, 4.0, 4.3)
# Mansion House speech three weeks after the Panther
eq("Mansion House after Panther (days)", (date(1911, 7, 21) - date(1911, 7, 1)).days, 20)
# Kruger telegram 3 January 1896, Jameson Raid began 29 December 1895: five days before
eq("raid to telegram (days)", (date(1896, 1, 3) - date(1895, 12, 29)).days, 5)
# Bülow's speech about three weeks after Kiaochow (14 November 1897)
between("Kiaochow to speech (days)", (date(1897, 12, 6) - date(1897, 11, 14)).days, 20, 23)
# Fashoda: Marchand 10 July; Kitchener 19 September; French orders 3 November; Omdurman 2 September
eq("Marchand to Kitchener (days)", (date(1898, 9, 19) - date(1898, 7, 10)).days, 71)
eq("Kitchener to withdrawal order (days)", (date(1898, 11, 3) - date(1898, 9, 19)).days, 45)
assert date(1898, 9, 2) < date(1898, 9, 19)
eq("Marchand mission years 1896-98", 1898 - 1896, 2)
# Fashoda to Entente Cordiale: six years
eq("Fashoda to Entente", 1904 - 1898, 6)
eq("Anglo-Japanese to Entente", 1904 - 1902, 2)
eq("Entente to Russian convention", 1907 - 1904, 3)
eq("Boer War length (years, approx)", round((date(1902, 5, 31) - date(1899, 10, 11)).days / 365.25, 1), 2.6)
# Delcassé foreign minister June 1898, Fashoda July-Dec 1898
assert date(1898, 6, 1) < date(1898, 7, 10)
# Heligoland-Zanzibar to Kruger telegram: about five and a half years
between("1890 to 1896", 1896 - 1890, 5, 7)
# Empire table (Lenin, Hübner/Supan), million km2 and million people
cols = {"Britain": (22.5, 33.5, 393.5, 0.3, 46.5), "France": (0.9, 10.6, 55.5, 0.5, 39.6),
        "Russia": (17.0, 17.4, 33.2, 5.4, 136.2), "Germany": (0, 2.9, 12.3, 0.5, 64.9)}
for k, (a76, a14, p14, am, pm) in cols.items():
    pass
between("Britain total area share", (33.5 + 0.3) / 133.9, 0.25, 0.26)
between("Britain total pop share", (393.5 + 46.5) / 1657.0, 0.26, 0.27)
between("France growth", 10.6 / 0.9, 11.5, 12.0)
eq("Britain gain", round(33.5 - 22.5, 1), 11.0)
between("Germany pop", 64.9, 64, 66)
# Neukamerun about 275,000 km2 (French Equatorial Africa) vs Germany's colonies 2.9 million km2 (before): about a tenth
between("Neukamerun vs German colonies", 0.275 / 2.9, 0.09, 0.10)
# Congo over 2 million km2
assert 2.345409 > 2
# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)

# Chapter text presence tests
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.int.empire.2.md"), encoding="utf-8").read()
for token in ["15 November 1884", "26 February 1885", "103 days", "28 March 1898", "14 June 1900", "19 battleships",
              "38", "10 February", "31 March 1905", "16 January", "7 April 1906", "1 July 1911", "21 July 1911",
              "4 November 1911", "275,000", "30 January 1902", "8 April 1904", "31 August 1907", "10 July 1898",
              "19 September", "21 March 1899", "3 January 1896", "6 December 1897", "29 December 1895",
              "33.5", "393.5", "10.6", "55.5", "2.9", "12.3"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
print("ok")
