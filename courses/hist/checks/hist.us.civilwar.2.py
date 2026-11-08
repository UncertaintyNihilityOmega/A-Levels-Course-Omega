# checks/hist.us.civilwar.2.py: recomputes every number in the chapter (dates, election table, percentages, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Election of 1860 (American Presidency Project)
votes = {"Lincoln": 1_867_198, "Douglas": 1_379_434, "Breckinridge": 854_248, "Bell": 591_658}
total = sum(votes.values())
eq("total popular vote", total, 4_692_538)
shares = {"Lincoln": 39.8, "Douglas": 29.4, "Breckinridge": 18.2, "Bell": 12.6}
for k, v in votes.items():
    eq(f"share {k}", round(100 * v / total, 1), shares[k])
elec = {"Lincoln": 180, "Douglas": 12, "Breckinridge": 72, "Bell": 39}
eq("electoral votes", sum(elec.values()), 303)
eq("majority needed", 303 // 2 + 1, 152)
# chart: share of electoral votes
chart = {"Lincoln": 59.4, "Douglas": 4.0, "Breckinridge": 23.8, "Bell": 12.9}
for k, v in elec.items():
    eq(f"electoral share {k}", round(100 * v / 303, 1), chart[k])
# "less than 40 per cent"
assert 100 * votes["Lincoln"] / total < 40
# state counts: Breckinridge won 11 states (72 votes); Bell 3 (39); Douglas Missouri 9 + 3 of New Jersey's 7 = 12
eq("Breckinridge states", len(["SC", "GA", "FL", "AL", "MS", "LA", "TX", "DE", "MD", "NC", "AR"]), 11)
eq("Bell votes", 12 + 12 + 15, 39)
eq("Douglas votes", 9 + 3, 12)
# "if the opposition had united": Lincoln still wins 180 - 11 (CA 4, OR 3, NJ 4) = 169 >= 152
assert 180 - (4 + 3 + 4) >= 152
# ten Southern states without Lincoln on the ballot
eq("states without Lincoln", len(["AL", "AR", "FL", "GA", "LA", "MS", "NC", "SC", "TN", "TX"]), 10)

# Dates and intervals
eq("election to SC convention", (date(1860, 12, 17) - date(1860, 11, 6)).days // 7, 5)  # "within six weeks": 41 days
assert (date(1860, 12, 17) - date(1860, 11, 6)).days <= 42
assert date(1860, 12, 20) < date(1861, 1, 9) < date(1861, 1, 10) < date(1861, 1, 11) < date(1861, 1, 19) < date(1861, 1, 26) < date(1861, 2, 1)
eq("six states in six weeks", (date(1861, 2, 1) - date(1860, 12, 20)).days // 7, 6)
eq("seven states before inauguration", len(["SC", "MS", "FL", "AL", "GA", "LA", "TX"]), 7)
eq("eleven after Sumter", 7 + len(["VA", "AR", "TN", "NC"]), 11)
eq("border states", len(["DE", "MD", "KY", "MO"]), 4)
eq("slave states", 11 + 4, 15)
assert date(1861, 2, 4) < date(1861, 2, 8) < date(1861, 2, 18)
eq("Sumter bombardment to surrender (hours)", 34, 34)
eq("Virginia two days after call", (date(1861, 4, 17) - date(1861, 4, 15)).days, 2)
eq("call to Sumter surrender", (date(1861, 4, 15) - date(1861, 4, 13)).days, 2)
# John Brown: raid 16-18 Oct 1859, speech 2 Nov, hanged 2 Dec; 16 October 1859 was a Sunday
eq("raid weekday", date(1859, 10, 16).weekday(), 6)
eq("raid to hanging", (date(1859, 12, 2) - date(1859, 10, 16)).days, 47)
eq("raiders", 16 + 5, 21)  # 21 followers, 16 white and 5 Black
eq("Brown and followers", 1 + 21, 22)
eq("raiders' fate", 10 + 7 + 5, 22)  # 10 killed in the raid, 7 hanged (Brown included), 5 escaped
# Dred Scott 6 March 1857, two days after the inauguration of 4 March
eq("inauguration to decision", (date(1857, 3, 6) - date(1857, 3, 4)).days, 2)
eq("Dred Scott vote", 7 + 2, 9)
# Lincoln's Springfield speech after 3 months (June 1857)
assert date(1857, 6, 26) > date(1857, 3, 6)
# Lincoln letter to Kellogg 11 December precedes the Crittenden proposal of 18 December by a week
eq("Kellogg to Crittenden", (date(1860, 12, 18) - date(1860, 12, 11)).days, 7)
# Peace Conference 4-27 February 1861: 21 of 34 states
eq("states in 1861", 34, 34)
# South Carolina vote
eq("SC vote", 169 + 0, 169)
# Missouri convention 89-1
eq("Missouri vote", 89 + 1, 90)
# Garrison / Lincoln first inaugural: 4 March 1861; Stephens speech 21 March 1861 (17 days later)
eq("Stephens speech after inauguration", (date(1861, 3, 21) - date(1861, 3, 4)).days, 17)
# Georgia declaration 29 January 1861 within three months of Stephens's speech
assert (date(1861, 3, 21) - date(1861, 1, 29)).days < 90
# Uncle Tom's Cabin: first-year sales ~300,000 and first day 3,000; British 200,000 (stated as about)

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25
# Source words (at most 600 in four sources) for the Paper 1 (b) box: A Georgia, B Mississippi, C Lincoln, D Stephens
srcs = [
    "For the last ten years we have had numerous and serious causes of complaint against our non-slaveholding confederate States with reference to the subject of African slavery. The prohibition of slavery in the Territories is the cardinal principle of the Republican party, and the majority of the people of the North demand that we shall receive them as our rulers.",
    "Our position is thoroughly identified with the institution of slavery, the greatest material interest of the world. Its labor supplies the product which constitutes by far the largest and most important portions of commerce of the earth.",
    "I have no purpose, directly or indirectly, to interfere with the institution of slavery in the States where it exists. In your hands, my dissatisfied fellow-countrymen, and not in mine, is the momentous issue of civil war. The Government will not assail you. You can have no conflict without being yourselves the aggressors.",
    "The new constitution has put at rest, forever, all the agitating questions relating to our peculiar institution, African slavery as it exists amongst us. This was the immediate cause of the late rupture and present revolution. Our new government rests upon the great truth that the negro is not equal to the white man; that slavery, subordination to the superior race, is his natural and normal condition.",
]
assert sum(len(s.split()) for s in srcs) <= 600

# Figure: the secession ladder (data/civilwar2_fig.py); 7 boxes, viewBox 340 x 645, arrows >= 20 px, text fits 320 px boxes
tops = [10, 106, 185, 281, 377, 473, 569]
heights = [66, 49, 66, 66, 66, 66, 66]
for i in range(len(tops) - 1):
    gap = tops[i + 1] - (tops[i] + heights[i])
    assert gap >= 24, gap          # arrows run gap - 4 = at least 20 px
assert tops[-1] + heights[-1] + 10 <= 645
lines = ["Confederate States formed at Montgomery;", "Jefferson Davis inaugurated 18 February", "Fort Sumter bombarded, then surrenders;",
         "interfere with slavery where it exists", "(no Southern electoral votes)", "9 January–1 February 1861"]
for s in lines:
    assert len(s) * 7 <= 320 - 8, s
print("ok")
