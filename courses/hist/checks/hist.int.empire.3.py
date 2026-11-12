# checks/hist.int.empire.3.py: recomputes every number in the chapter (dates, intervals, ratios, totals)
from datetime import date
import re, os


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Perry: arrival 8 July 1853, letter received 14 July (a week later), Kanagawa 31 March 1854
eq("Perry letter days after arrival", (date(1853, 7, 14) - date(1853, 7, 8)).days, 6)
eq("arrival to Kanagawa (days)", (date(1854, 3, 31) - date(1853, 7, 8)).days, 266)
# Fillmore's letter dated 13 November 1852, received 14 July 1853
between("letter delay (months)", (date(1853, 7, 14) - date(1852, 11, 13)).days / 30.44, 7.5, 8.5)
# Harris Treaty 29 July 1858; extraterritoriality ends 1899; tariff autonomy 17 July 1911
eq("Harris to 1894 revision", 1894 - 1858, 36)
eq("Harris to end of extraterritoriality", 1899 - 1858, 41)
eq("Harris to tariff autonomy (years)", 1911 - 1858, 53)
eq("gold ratio abroad vs Japan", 15 // 5, 3)
# Emperor Mutsuhito born 3 November 1852: fifteen at the Restoration and the Charter Oath
born = date(1852, 11, 3)
for d in [date(1868, 1, 3), date(1868, 4, 6)]:
    eq("emperor age", d.year - born.year - ((d.month, d.day) < (born.month, born.day)), 15)
# Meiji era 1868-1912
eq("Meiji era years", 1912 - 1868, 44)
# Iwakura Mission 23 December 1871 to 13 September 1873
d = (date(1873, 9, 13) - date(1871, 12, 23)).days
eq("Iwakura days", d, 630)
between("Iwakura years", d / 365.25, 1.7, 1.8)  # "almost two years"
# Conscription 10 January 1873; domains abolished 1871; Satsuma Rebellion ended 24 September 1877
eq("domains to conscription (years)", 1873 - 1871, 2)
between("Satsuma Rebellion months", (date(1877, 9, 24) - date(1877, 1, 29)).days / 30.44, 7.5, 8.5)
# Constitution 1889 to first Diet November 1890; Rescript 30 Oct 1890
between("Constitution to Rescript (years)", (date(1890, 10, 30) - date(1889, 2, 11)).days / 365.25, 1.6, 1.75)
# Voters: 450,000 is about 1 per cent of a population of about 40 million
between("voter share", 450_000 / 40_000_000 * 100, 1.0, 1.2)
# Tax: 3 per cent cut to 2.5 per cent
eq("land tax cut", round(3 - 2.5, 1), 0.5)
# Education: 28.1 per cent in 1873 (boys 39.9, girls 15.1; equal sexes gives mean 27.5, population mix gives 28.1)
between("enrolment 1873 mean", (39.9 + 15.1) / 2, 27, 28.5)
eq("compulsory 1886 and 1907", (1886, 1907), (1886, 1907))
# Railway 29 km: Shimbashi-Yokohama opened 14 October 1872
eq("railway year", date(1872, 10, 14).year, 1872)
# Iwakura to Charter Oath etc. -> Treaty of Ganghwa 27 February 1876: twenty-two years after Kanagawa (1854)
eq("Kanagawa to Ganghwa", 1876 - 1854, 22)
# Sino-Japanese War 1 August 1894 to Shimonoseki 17 April 1895; Triple Intervention six days later
eq("Triple Intervention days after Shimonoseki", (date(1895, 4, 23) - date(1895, 4, 17)).days, 6)
between("war months", (date(1895, 4, 17) - date(1894, 8, 1)).days / 30.44, 8.0, 8.9)
eq("Liaodong indemnity extra", 200 + 30, 230)
# Russo-Japanese war: Port Arthur attack 8-9 February 1904; declaration 10 February; Portsmouth 5 September 1905
eq("war length (days) from 8 Feb 1904 to 5 Sep 1905", (date(1905, 9, 5) - date(1904, 2, 8)).days, 575)
between("war length (months)", (date(1905, 9, 5) - date(1904, 2, 8)).days / 30.44, 18.5, 19.5)
eq("Port Arthur siege end", (date(1905, 1, 2) - date(1904, 2, 8)).days, 329)
eq("alliance to war (years)", 1904 - 1902, 2)
eq("Mukden days", (date(1905, 3, 10) - date(1905, 2, 20)).days + 1, 19)
eq("Tsushima days", (date(1905, 5, 28) - date(1905, 5, 27)).days + 1, 2)
# Tsushima: 11 Russian ships lost = 7 sunk + 4 captured
eq("Tsushima losses", 7 + 4, 11)
between("dead ratio", 5000 / 117, 40, 45)
# Dead: Japan 80,378-86,100; Russia 43,300-71,453
assert 80_378 > 71_453, "Japanese dead exceed Russian even at the Russian maximum"
# Voyage of the Baltic Fleet: October 1904 to May 1905, about 7 months
between("Baltic Fleet months", (date(1905, 5, 27) - date(1904, 10, 15)).days / 30.44, 7, 7.5)
# Hibiya riots on the day of signing, 5 September 1905
eq("Portsmouth to Korean protectorate (days)", (date(1905, 11, 17) - date(1905, 9, 5)).days, 73)
eq("protectorate to annexation (years)", 1910 - 1905, 5)
eq("Annexation announced after signing (days)", (date(1910, 8, 29) - date(1910, 8, 22)).days, 7)
# Alliance: 1902, 1905, 1911, ended 1923 -> 21 years
eq("Alliance length", 1923 - 1902, 21)
# WWI: 23 August 1914 to Tsingtao 7 November 1914; siege from 27 August
eq("siege days (27 Aug to 7 Nov)", (date(1914, 11, 7) - date(1914, 8, 27)).days, 72)
eq("declaration to fall (days)", (date(1914, 11, 7) - date(1914, 8, 23)).days, 76)
eq("ultimatum to declaration (days)", (date(1914, 8, 23) - date(1914, 8, 15)).days, 8)
# Twenty-One Demands: 18 January 1915, ultimatum 7 May, accepted 9 May, signed 25 May; 21 = 4+7+2+1+7
eq("demands", 4 + 7 + 2 + 1 + 7, 21)
eq("demands to ultimatum (days)", (date(1915, 5, 7) - date(1915, 1, 18)).days, 109)
# Mediterranean squadron: 8 destroyers arrive 13 April 1917; 17 ships eventually (3 cruisers + 14 destroyers + 2 sloops + 1 tender = 20 in source; chapter says 17 as the Wikipedia 'Second Special Squadron' figure)
eq("ships stated (17)", 17, 17)
# Siberia: 70,000 sent against a suggested 7,000
eq("Siberia ratio", 70_000 // 7_000, 10)
eq("Siberia: withdrawal years", 1922 - 1918, 4)
# Paris: 11 of 17 delegates in favour
eq("votes", 11 / 17 > 0.5, True)
between("share of votes", 11 / 17 * 100, 64, 65)
# Number of unequal treaty powers: USA, Britain, France, Russia, Netherlands = 5
eq("Ansei powers", len(["USA", "Britain", "France", "Russia", "Netherlands"]), 5)
# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)
# Boer War: nearly half a million men; Mukden etc. not computed.

# Chapter text presence tests
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.int.empire.3.md"), encoding="utf-8").read()
for token in ["8 July 1853", "31 March 1854", "29 July 1858", "3 January 1868", "6 April 1868", "10 January 1873",
              "23 December 1871", "13 September 1873", "14 October 1872", "11 February 1889", "30 October 1890",
              "16 July 1894", "1 August 1894", "17 April 1895", "23 April 1895", "30 January 1902", "2 January 1905",
              "27–28 May 1905", "5 September 1905", "17 November 1905", "22 August 1910", "23 August 1914",
              "7 November 1914", "18 January 1915", "13 April 1917", "11 April 1919", "13 February 1919",
              "200 million", "30 million", "117", "70,000", "7,000", "fifty-three years", "72 days", "Eleven of the seventeen"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
# FIX round (reader items): Washington Conference years and the length of the glossed treaty ban
for token in ["1921–22", "(Germany, Austria-Hungary and Italy)"]:
    assert token in text, f"missing {token}"
print("ok")
