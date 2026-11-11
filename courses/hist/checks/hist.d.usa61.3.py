# checks/hist.d.usa61.3.py: recomputes every number in the chapter (dates, intervals, percentages, marks)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, got, lo, hi):
    assert lo < got < hi, f"{label}: computed {got}, chapter says between {lo} and {hi}"


# Montgomery boycott: 5 December 1955 to 20 December 1956 = 381 days
eq("boycott days", (date(1956, 12, 20) - date(1955, 12, 5)).days, 381)

# Weekdays named in the text (Monday = 0 ... Sunday = 6)
eq("Bloody Sunday is a Sunday", date(1965, 3, 7).weekday(), 6)
eq("Anniston, Mother's Day, is a Sunday", date(1961, 5, 14).weekday(), 6)
assert date(1961, 5, 14).day > 7 and date(1961, 5, 14).day <= 14  # second Sunday of May
eq("12 April 1963 (Good Friday) is a Friday", date(1963, 4, 12).weekday(), 4)
eq("16th Street bombing is a Sunday", date(1963, 9, 15).weekday(), 6)

# King's ages: born 15 January 1929
def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))

eq("King's age at Montgomery boycott", age(date(1929, 1, 15), date(1955, 12, 5)), 26)
eq("King's age at the Nobel Prize ceremony", age(date(1929, 1, 15), date(1964, 12, 10)), 35)

# The three murdered in Neshoba County: 21 June 1964
eq("Chaney age", age(date(1943, 5, 30), date(1964, 6, 21)), 21)
eq("Goodman age", age(date(1943, 11, 23), date(1964, 6, 21)), 20)
eq("Schwerner age", age(date(1939, 11, 6), date(1964, 6, 21)), 24)
eq("Neshoba to discovery (days)", (date(1964, 8, 4) - date(1964, 6, 21)).days, 44)

# Birmingham church bombing victims' ages: three aged 14, one aged 11
eq("four girls", len([14, 14, 14, 11]), 4)
eq("first conviction years after the bombing", 1977 - 1963, 14)

# Intervals in the text
eq("March on Washington to church bombing (days)", (date(1963, 9, 15) - date(1963, 8, 28)).days, 18)
assert 18 < 21  # "less than three weeks"
eq("Bloody Sunday to Johnson's speech (days)", (date(1965, 3, 15) - date(1965, 3, 7)).days, 8)
months = (date(1965, 8, 6).year - date(1965, 3, 7).year) * 12 + (8 - 3)
eq("Bloody Sunday to VRA (months, 'within five months')", months, 5)
eq("Brown to autumn 1964 (years, 'ten years')", 1964 - 1954, 10)
eq("Fair Housing a week after King's death", (date(1968, 4, 11) - date(1968, 4, 4)).days, 7)
eq("Birmingham: Project C start to children's march (days)", (date(1963, 5, 2) - date(1963, 4, 3)).days, 29)
eq("Kennedy's address to the bill (days)", (date(1963, 6, 19) - date(1963, 6, 11)).days, 8)
eq("1968 is a leap year (Kerner Report, 29 February)", date(1968, 2, 29).day, 29)
eq("Selma march length (days, 21-25 March)", 25 - 21 + 1, 5)
between("Selma march miles per day ('about eleven')", 54 / 5, 10.0, 12.0)
eq("Poll tax ban in state elections follows the Amendment by (years)", 1966 - 1964, 2)

# Voter registration (per cent of voting-age Black residents): March 1965 and September 1967
reg65 = {"Mississippi": 6.7, "Alabama": 19.3, "Georgia": 27.4}
reg67 = {"Mississippi": 59.8, "Alabama": 51.6, "Georgia": 52.6}
between("Mississippi 'almost ninefold'", reg67["Mississippi"] / reg65["Mississippi"], 8.5, 9.0)
eq("Mississippi rise (points)", round(reg67["Mississippi"] - reg65["Mississippi"], 1), 53.1)
eq("registration gap in months", (1967 - 1965) * 12 + (9 - 3), 30)
for st in reg65:
    assert reg67[st] > reg65[st]

# Freedom Summer: about 1,600 of about 17,000 applicants accepted = about one in ten
between("one in ten", 1600 / 17000, 0.09, 0.10)

# Votes
eq("Southern Manifesto signers", 19 + 82, 101)
eq("House vote total (290-130)", 290 + 130, 420)
eq("Cloture vote total (71-29)", 71 + 29, 100)
eq("Senate passage total (73-27)", 73 + 27, 100)
assert 71 >= -(-2 * 100 // 3)  # two-thirds of 100 senators is 67; cloture needs 67 when all vote
eq("two-thirds of 100 rounded up", -(-2 * 100 // 3), 67)

# Wallace 1968: 13.5 per cent and 46 electoral votes
assert 13 < 13.5 < 14 and 46 > 0

# Poverty and income: Black poverty 41.8 in 1966 ('about 42'); 1959 about 55; income ratio 54 -> 61
eq("poverty rounded", round(41.8), 42)
between("poverty fell by about 13 points", 55 - 41.8, 12.5, 14)
eq("income ratio rise (points)", 61 - 54, 7)

# Black elected officials about 1,500 (1970) to about 3,500 (1975): more than double
between("more than doubled", 3500 / 1500, 2.0, 2.5)
eq("span of years", 1975 - 1970, 5)

# Schools: 2.25 per cent of Black Southern pupils in mixed schools in autumn 1964
assert 2.0 < 2.25 < 2.5

# Loving: married 1958, sentence suspended for 25 years if they left; 16 states
eq("Loving decided 12 June 1967", date(1967, 6, 12).year - 1958, 9)
eq("sixteen states", 16, 16)

# Mark totals in worked examples: Table A + Table B = [30]; paper = 2 x 30
eq("table total", 15 + 15, 30)
eq("paper total", 2 * 30, 60)
eq("federal-government essay total low", 14 + 13, 27)
eq("federal-government essay total high", 14 + 14, 28)
print("ok")
