@chapter cs.datatypes
@title Data types, records and arrays
@level as
@paper CAIE 9618 Paper 2 (and Paper 4 at A Level)
@time 6–8 hours
@summary Every value a program stores has a data type. You will learn to choose the right type, group related values into a record, store many values in one-dimensional and two-dimensional arrays, and process them with the two algorithms Paper 2 expects you to write from memory: linear search and bubble sort.

:::why
Almost every Paper 2 question stores data somewhere: a list of scores, a table of sales, a set of customer details. If you can choose the right data type, declare a record and an array, and loop through them confidently, you can answer most of the long pseudocode questions. The same skills carry straight into Paper 4, where you write them as real Python code.
:::

**Before you start**, you should be able to write variables, IF statements and the three kinds of loop, from [Programming from zero](#cs.f.basics) and [Programming basics: variables, selection and loops](#cs.programming).

:::try Warm-up
Q: What is output by this pseudocode? `Total ← 0`, then `FOR Count ← 2 TO 8 STEP 2`, `Total ← Total + Count`, `NEXT Count`, then `OUTPUT Total`. (from [Programming basics](#cs.programming))
A: Count takes the values 2, 4, 6 and 8, so Total is \(2 + 4 + 6 + 8 = 20\). The output is 20.
Q: What does the Python statement `print(17 // 5, 17 % 5)` display, and which pseudocode operators do `//` and `%` match? (from [Programming from zero](#cs.f.basics))
A: It displays `3 2`. `//` is integer division, like DIV, and `%` is the remainder, like MOD.
Q: Which loop always runs its body at least once: FOR, WHILE or REPEAT … UNTIL? (from [Programming basics](#cs.programming))
A: REPEAT … UNTIL. It is a post-condition loop: the condition is tested after the body runs.
:::

:::note How code appears in this course
Pseudocode follows the Cambridge Pseudocode Guide for 2027–2029 exactly: keywords in capitals, `←` for assignment, three-space indents. Python blocks are Python 3. The block after a Python program, introduced by "Output:", is exactly what that program prints; every Python example in this chapter has been run to check it.
:::

## Data types

When you store a value, the computer needs to know what kind of value it is. The number 7, the character '7' and the string "7" look alike to you, but they are stored differently and you can do different things with them. You can add 7 to another number. You cannot add the string "7" to a number without converting it first.

:::def Data type
A classification of data that sets which values a variable can hold, how they are stored and which operations can be performed on them.
:::

Cambridge pseudocode uses six basic data types. The syllabus also lists ARRAY (later in this chapter) and FILE (in [Text files, stacks, queues and linked lists](#cs.structures)).

| Type | What it holds | Pseudocode literal | Python type | Typical use |
|---|---|---|---|---|
| INTEGER | a whole number | `42`, `-7` | `int` | a count, an age, a quantity |
| REAL | a number that may have a fractional part | `3.0`, `0.75` | `float` | a price, a mass, an average |
| CHAR | exactly one character | `'Y'`, `'7'` | `str` of length 1 | a grade, a Y/N reply |
| STRING | zero or more characters | `"Lima"`, `""` | `str` | a name, a code, a phone number |
| BOOLEAN | TRUE or FALSE | `TRUE` | `bool` (`True`, `False`) | a yes/no state such as `IsPaid` |
| DATE | a calendar date | `14/03/2027` | `datetime.date` | a date of birth, a due date |

Two details of the literals matter in exam answers. A REAL literal always has at least one digit on each side of the decimal point, so you write `4.0` and `0.5`, never `4.` or `.5`. A CHAR goes in single quotes and a STRING in double quotes, so `'Y'` is a CHAR and `"Y"` is a STRING. The guide writes dates as dd/mm/yyyy and recommends saying so, because date formats differ around the world.

:::def Integer
A data type for whole numbers, positive, negative or zero, with no fractional part.
:::

:::def Real
A data type for numbers that can have a fractional part, such as 2.5 or −0.125.
:::

:::def Boolean
A data type with only two possible values, TRUE and FALSE.
:::

### Choosing the right type

Choosing a type is a decision with reasons, and Paper 2 asks you to give them. The rule that catches most students is about numbers that are not really numbers.

:::key Choosing a data type
- **INTEGER** for counts and whole quantities that you might do arithmetic on: number of tickets, age in years.
- **REAL** when a fractional part is possible: prices, measurements, averages.
- **STRING** for identifiers made of digits, such as telephone numbers, account numbers and codes with leading zeros. They are never used in arithmetic, a leading zero must be kept, and they may contain `+`, spaces or letters.
- **CHAR** for a single character; **BOOLEAN** for anything with exactly two states; **DATE** for dates, so they can be compared and checked as real dates.
:::

:::eg Choosing data types for a bus pass system
A bus company in Nairobi stores these items for each pass: the pass number (for example BP004512), the holder's name, the holder's age, the balance on the pass (for example 12.50), the fare zone (a single letter A to D), whether the holder is a student, and the expiry date. State a suitable data type for each item and give a reason for each choice.

Work through the items one at a time and give a reason tied to the data, not a general definition.

- Pass number: STRING, because it contains letters and leading zeros and is never used in arithmetic. [B1]
- Holder's name: STRING, because it is a sequence of characters. [B1]
- Age: INTEGER, because ages are stored as whole numbers of years. [B1]
- Balance: REAL, because money has a fractional part (cents). [B1]
- Fare zone: CHAR, because it is always exactly one character. [B1]
- Student: BOOLEAN, because there are only two possible values. [B1]
- Expiry date: DATE, so it can be compared with today's date. [B1]

An examiner gives a mark for a correct type with a correct reason. "STRING because it is text" is too weak for the pass number: the reason that earns the mark is the leading zeros or the letters.
:::

### Data types in Python

In Python you do not declare types. Python decides the type from the value you assign, and `type()` tells you what it chose. Notice that Python has no separate CHAR type: a single character is just a string of length 1.

The following Python program prints the type of five values, then shows three conversions.

```python
book_id = "B0193"
copies = 3
price = 18.50
shelf = "C"
on_loan = True
print(type(book_id), type(copies), type(price), type(shelf), type(on_loan))
print("3" + "4", 3 + 4, int("3") + int("4"), str(3) + str(4))
print(7 / 2, 7 // 2, 7 % 2)
```

Output:

```output
<class 'str'> <class 'int'> <class 'float'> <class 'str'> <class 'bool'>
34 7 7 34
3.5 3 1
```

The second line is the one to remember. With strings, `+` joins them, so `"3" + "4"` is `"34"`. With integers, `+` adds. The third line shows that `/` always gives a real number, as it does in pseudocode, while `//` and `%` match DIV and MOD.

This matters every time a program reads from the keyboard, because `input()` always returns a string. You must convert the string before doing arithmetic with it.

```python
quantity = int(input("How many tickets? "))
price = 4.75
total = quantity * price
print("Total to pay:", total)
```

Output, when the user types 3:

```output
How many tickets? 3
Total to pay: 14.25
```

Pseudocode has functions for the same conversions. The Paper 2 insert lists `STR_TO_NUM("23.45")`, which returns the number 23.45, and `NUM_TO_STR(87.5)`, which returns the string "87.5". In an exam, use only the functions the insert gives you.

:::warn The digit '7' is not the number 7
`'7'` (a CHAR) and `"7"` (a STRING) are characters. Their stored codes have nothing to do with the value seven. Comparing `"10" < "9"` as strings gives TRUE, because strings are compared character by character and '1' comes before '9'. Convert to a number first whenever you compare or calculate.
:::

Dates work the same way in both languages: store them as dates, not strings, and you can compare them and find the gap between them. The insert gives `DAY()`, `MONTH()`, `YEAR()` and `TODAY()` for pseudocode. In Python the `datetime` module does the work.

```python
from datetime import date
borrowed = date(2027, 3, 14)
due = date(2027, 4, 2)
print("Loan length in days:", (due - borrowed).days)
print(due > borrowed)
```

Output:

```output
Loan length in days: 19
True
```

## Records: grouping different data under one name

A library book has an ID, a title, an author, a price and a flag saying whether it is on loan. Those values have different types, but they all describe one thing. A **record** lets you keep them together under one identifier, so you can pass "the book" around instead of five separate variables.

:::def Record
A composite data type that groups several data items, which can be of different data types, under one identifier. Each item in a record is called a field.
:::

:::def Field
One named data item inside a record, with its own data type, such as the Title field of a Book record.
:::

You define a record type once, then declare as many variables of that type as you need. In pseudocode:

```pseudocode
TYPE Book
   DECLARE BookID : STRING
   DECLARE Title : STRING
   DECLARE Author : STRING
   DECLARE Price : REAL
   DECLARE OnLoan : BOOLEAN
ENDTYPE

DECLARE ThisBook : Book
DECLARE SpareCopy : Book
```

The TYPE block creates a new data type called Book; it does not create any book. `DECLARE ThisBook : Book` creates a variable that has all five fields. You reach a field with **dot notation**: the variable name, a full stop, then the field name.

```pseudocode
ThisBook.BookID ← "B0193"
ThisBook.Title ← "Rivers of the World"
ThisBook.Price ← 18.50
ThisBook.OnLoan ← FALSE
SpareCopy ← ThisBook
OUTPUT ThisBook.Title, " costs ", ThisBook.Price
```

The line `SpareCopy ← ThisBook` copies every field at once. The guide allows assigning one record variable to another of the same type. It does not allow comparing two whole records with `=`: the insert says comparison operators "cannot be used to compare two records", so compare the fields you care about.

:::key Records in pseudocode
- Define: `TYPE <name>` … `DECLARE <field> : <type>` (one line per field) … `ENDTYPE`.
- Declare a variable: `DECLARE <variable> : <name>`.
- Read or write a field: `<variable>.<field>`, for example `ThisBook.Price ← 18.50`.
- Copy a whole record: `<variable1> ← <variable2>` (same record type).
:::

:::eg Declaring and filling a record (exam style)
A clinic in Lahore stores for each patient: a patient ID (for example "P2207"), the name, the age in years, the mass in kilograms, whether the patient has insurance, and the date of the last visit. Write pseudocode to define a record type Patient, declare a variable NewPatient of that type, and input a value into each field.

```pseudocode
TYPE Patient
   DECLARE PatientID : STRING
   DECLARE Name : STRING
   DECLARE Age : INTEGER
   DECLARE Mass : REAL
   DECLARE Insured : BOOLEAN
   DECLARE LastVisit : DATE
ENDTYPE

DECLARE NewPatient : Patient

INPUT NewPatient.PatientID
INPUT NewPatient.Name
INPUT NewPatient.Age
INPUT NewPatient.Mass
INPUT NewPatient.Insured
INPUT NewPatient.LastVisit
```

Mark points:

- `TYPE Patient` … `ENDTYPE` enclosing the field declarations [B1]
- six fields declared with suitable types (STRING, STRING, INTEGER, REAL, BOOLEAN, DATE) [B1]
- `DECLARE NewPatient : Patient` [B1]
- each field input using dot notation [B1]
:::

### Records in Python

Python has no TYPE statement, so a record is written as a **class** with a constructor, `__init__`, that sets each field. Paper 4 allows exactly this: "A class declaration can be used to declare a record." (The full object-oriented meaning of classes comes at A Level in [Object-oriented programming](#cs.oop); here a class is only a container for fields.)

```python
class Book:
    def __init__(self, book_id, title, author, price, on_loan):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.on_loan = on_loan

library = [Book("B0193", "Rivers of the World", "N. Okafor", 18.50, True),
           Book("B0207", "Starting with Python", "L. Mendes", 24.00, False),
           Book("B0311", "The Night Sky", "R. Iqbal", 12.75, True)]
loaned = 0
for book in library:
    if book.on_loan:
        loaned = loaned + 1
print("Books on loan:", loaned)
print(library[1].title, "costs", f"{library[1].price:.2f}")
```

Output:

```output
Books on loan: 2
Starting with Python costs 24.00
```

`library[1]` is the second book, because Python lists count from 0. The format `f"{…:.2f}"` shows two decimal places; without it, Python would print `24.0`.

## Arrays

Suppose a weather station records the midday temperature every day for a week. Seven separate variables (`Temp1`, `Temp2` …) would work, but you could not loop through them, and a year of readings would need 365 variables. An **array** stores all the values under one identifier and numbers them.

:::def Array
A data structure that holds a fixed number of elements of the same data type under one identifier. Each element is accessed by its index.
:::

:::def Index
The number (subscript) used to identify one element of an array, written in square brackets, as in Temps[4].
:::

:::def Lower bound and upper bound
The lower bound is the index of the first element of an array; the upper bound is the index of the last element. Cambridge pseudocode states both when the array is declared.
:::

:::def Element
One item stored in an array, identified by the array name and its index.
:::

### One-dimensional arrays

A one-dimensional (1D) array is a single row of elements. You declare it with its bounds and the type of every element:

```pseudocode
DECLARE Temps : ARRAY[1:7] OF INTEGER
```

This array has 7 elements, numbered 1 to 7. In general, the number of elements is upper bound − lower bound + 1, so `ARRAY[0:24]` has 25 elements. The guide says it is good practice to state the lower bound explicitly, and that it is usually 1.

:::html
<figure class="fig small"><svg viewBox="-30 0 370 140" role="img" aria-label="A one-dimensional array called Temps with seven boxes holding 31, 33, 30, 28, 29, 32 and 34, numbered with indexes 1 to 7. Index 1 is labelled lower bound, index 7 is labelled upper bound, and the box at index 4 is marked Temps[4] = 28."><text class="tl ti" x="30" y="26">Temps : ARRAY[1:7] OF INTEGER</text><rect class="fm s-acc sw2" x="30" y="40" width="40" height="40"/><text class="tl tc" x="50" y="65">31</text><text class="tl tc" x="50" y="98">1</text><rect class="fm s-acc sw2" x="70" y="40" width="40" height="40"/><text class="tl tc" x="90" y="65">33</text><text class="tl tc" x="90" y="98">2</text><rect class="fm s-acc sw2" x="110" y="40" width="40" height="40"/><text class="tl tc" x="130" y="65">30</text><text class="tl tc" x="130" y="98">3</text><rect class="f1 s-acc sw2" x="150" y="40" width="40" height="40"/><text class="tl tc" x="170" y="65">28</text><text class="tl tc" x="170" y="98">4</text><rect class="fm s-acc sw2" x="190" y="40" width="40" height="40"/><text class="tl tc" x="210" y="65">29</text><text class="tl tc" x="210" y="98">5</text><rect class="fm s-acc sw2" x="230" y="40" width="40" height="40"/><text class="tl tc" x="250" y="65">32</text><text class="tl tc" x="250" y="98">6</text><rect class="fm s-acc sw2" x="270" y="40" width="40" height="40"/><text class="tl tc" x="290" y="65">34</text><text class="tl tc" x="290" y="98">7</text><text class="tl te ti" x="20" y="98">index</text><text class="tl tc" x="50" y="125">lower bound</text><text class="tl tc tb" x="170" y="125">Temps[4] = 28</text><text class="tl tc" x="290" y="125">upper bound</text></svg><figcaption>Seven midday temperatures in °C stored in one array. The index under each box picks out one element: Temps[4] is the fourth reading, 28.</figcaption></figure>
:::

:::analogy
Think of an array as a row of numbered lockers in a school corridor. The row has one name (Temps), every locker is the same size (one type of data), and you open a locker by its number (the index). The number on the door is not the thing inside: locker 4 holds 28.
:::

You use an element exactly like a variable, and the index can be any expression that gives an integer:

```pseudocode
Temps[1] ← 31
Temps[Day + 1] ← Temps[Day]
OUTPUT Temps[4]
```

Asking for an index outside the bounds, such as `Temps[8]`, is a **run-time error**: the program is valid, but it fails while running. In Python the same mistake stops the program with this message:

```text
IndexError: list index out of range
```

### Processing every element: the array loop

Nearly every array algorithm is the same loop with a different body. The loop variable runs from the lower bound to the upper bound and is used as the index.

:::key The array loop
```pseudocode
FOR Index ← 1 TO 7
   // do something with Temps[Index]
NEXT Index
```
Use the array's own bounds. The guide says a statement should never process a group of elements at once, such as `Temps[1 TO 7] ← 0`: set them one at a time inside a loop.
:::

To set every element to zero (initialising the array), the body is one assignment:

```pseudocode
FOR Index ← 1 TO 7
   Temps[Index] ← 0
NEXT Index
```

The three standard jobs are a total (then an average), the largest or smallest value (with its position), and a count of elements that meet a condition. You should be able to write each without thinking.

:::eg Total, average and highest value
The array Temps holds the seven readings in the figure. Write pseudocode to output the total, the mean and the highest temperature with its day number.

Use one loop for all three jobs. Start the highest value at the **first element**, not at zero, so the algorithm works even if every reading is negative.

```pseudocode
DECLARE Index, Total, Highest, HighDay : INTEGER
DECLARE Average : REAL

Total ← 0
Highest ← Temps[1]
HighDay ← 1
FOR Index ← 1 TO 7
   Total ← Total + Temps[Index]
   IF Temps[Index] > Highest THEN
      Highest ← Temps[Index]
      HighDay ← Index
   ENDIF
NEXT Index
Average ← Total / 7
OUTPUT "Total: ", Total
OUTPUT "Average: ", Average
OUTPUT "Highest: ", Highest, " on day ", HighDay
```

With the data 31, 33, 30, 28, 29, 32, 34 the total is 217 and the mean is \(217 \div 7 = 31.0\). Highest starts at 31, changes to 33 on day 2 and to 34 on day 7, so the program outputs 34 on day 7. Average is declared REAL because `/` always gives a REAL result.
:::

The same algorithm in Python. A Python list counts from 0, so element `temps[i]` is day `i + 1`:

```python
temps = [31, 33, 30, 28, 29, 32, 34]
total = 0
highest = temps[0]
day_of_highest = 1
for i in range(len(temps)):
    total = total + temps[i]
    if temps[i] > highest:
        highest = temps[i]
        day_of_highest = i + 1
print("Total:", total)
print("Average:", total / len(temps))
print("Highest:", highest, "on day", day_of_highest)
```

Output:

```output
Total: 217
Average: 31.0
Highest: 34 on day 7
```

:::warn Starting the maximum at zero
`Highest ← 0` looks harmless, but a freezer that logs −18, −17 and −19 would report a highest temperature of 0, which was never measured. Start with the first element (`Highest ← Temps[1]`), or with a value you know is below every possible reading, and say why.
:::

### Arrays and lists: pseudocode to Python

Python has no fixed-size arrays; it has **lists**, which can grow and shrink. Paper 4 says that "if the programming language used does not support arrays, a list can be used instead", so a list is the right tool. Keep these differences in mind.

| Cambridge pseudocode | Python |
|---|---|
| `DECLARE Scores : ARRAY[1:30] OF INTEGER` | `scores = [0] * 30` |
| first element `Scores[1]` | first element `scores[0]` |
| last element `Scores[30]` | `scores[29]` (or `scores[-1]`) |
| size fixed by the declaration | `len(scores)`; a list can grow with `append` |
| `Scores[31]` is an error | `scores[30]` is an error, but `scores[-1]` is not |

Two common ways to map a 1-based pseudocode array onto Python: use index `i - 1` (as in the Temps program), or make the list one longer and never use element 0. Either is fine if you are consistent and say which you chose.

:::warn Negative indexes do not crash in Python
In pseudocode an index below the lower bound is always an error. In Python, `temps[-1]` is the **last** element, so an off-by-one mistake that produces −1 does not stop the program; it silently reads the wrong value. Check loop limits carefully.
:::

### Two-dimensional arrays

Some data is naturally a table. A market in Kumasi has three stalls, and the manager records how many baskets each stall sells in each of four weeks. That is 12 numbers arranged in rows and columns, so it fits a **two-dimensional (2D) array**.

:::def Two-dimensional array
An array whose elements are identified by two indexes, usually a row and a column, so that it represents a table of values of one data type.
:::

```pseudocode
DECLARE Sales : ARRAY[1:3, 1:4] OF INTEGER
```

The first bounds (1:3) are the rows, here the stalls; the second bounds (1:4) are the columns, here the weeks. `Sales[2, 3]` is row 2, column 3: what stall 2 sold in week 3. The array has \(3 \times 4 = 12\) elements.

:::html
<figure class="fig small"><svg viewBox="0 0 330 195" role="img" aria-label="A two-dimensional array Sales with 3 rows and 4 columns. Row 1 holds 12, 15, 9, 14. Row 2 holds 8, 11, 13, 10. Row 3 holds 20, 17, 16, 19. The element in row 2, column 3 is marked: Sales[2, 3] = 13."><text class="tl tc" x="200" y="22">column (week)</text><text class="tl te" x="90" y="42">row (stall)</text><rect class="fm s-acc sw2" x="100" y="50" width="50" height="34"/><text class="tl tc" x="125" y="72">12</text><rect class="fm s-acc sw2" x="150" y="50" width="50" height="34"/><text class="tl tc" x="175" y="72">15</text><rect class="fm s-acc sw2" x="200" y="50" width="50" height="34"/><text class="tl tc" x="225" y="72">9</text><rect class="fm s-acc sw2" x="250" y="50" width="50" height="34"/><text class="tl tc" x="275" y="72">14</text><rect class="fm s-acc sw2" x="100" y="84" width="50" height="34"/><text class="tl tc" x="125" y="106">8</text><rect class="fm s-acc sw2" x="150" y="84" width="50" height="34"/><text class="tl tc" x="175" y="106">11</text><rect class="f1 s-acc sw2" x="200" y="84" width="50" height="34"/><text class="tl tc" x="225" y="106">13</text><rect class="fm s-acc sw2" x="250" y="84" width="50" height="34"/><text class="tl tc" x="275" y="106">10</text><rect class="fm s-acc sw2" x="100" y="118" width="50" height="34"/><text class="tl tc" x="125" y="140">20</text><rect class="fm s-acc sw2" x="150" y="118" width="50" height="34"/><text class="tl tc" x="175" y="140">17</text><rect class="fm s-acc sw2" x="200" y="118" width="50" height="34"/><text class="tl tc" x="225" y="140">16</text><rect class="fm s-acc sw2" x="250" y="118" width="50" height="34"/><text class="tl tc" x="275" y="140">19</text><text class="tl tc tb" x="125" y="42">1</text><text class="tl tc tb" x="175" y="42">2</text><text class="tl tc tb" x="225" y="42">3</text><text class="tl tc tb" x="275" y="42">4</text><text class="tl te tb" x="90" y="72">1</text><text class="tl te tb" x="90" y="106">2</text><text class="tl te tb" x="90" y="140">3</text><text class="tl tc tb" x="200" y="178">Sales[2, 3] = 13: row 2, column 3</text></svg><figcaption>Baskets sold by three stalls (rows) over four weeks (columns). The first index chooses the row and the second chooses the column.</figcaption></figure>
:::

To visit every element you need **nested loops**: an outer loop for the rows and an inner loop for the columns (or the other way round, depending on what you want to total).

:::key Processing a 2D array
```pseudocode
FOR Row ← 1 TO 3
   FOR Column ← 1 TO 4
      // do something with Sales[Row, Column]
   NEXT Column
NEXT Row
```
To total each **row**, reset the total inside the outer loop, before the inner loop starts. To total each **column**, swap the loops so that the column is the outer loop.
:::

:::eg Row totals and the best week (exam style)
The 2D array Sales is declared as `ARRAY[1:3, 1:4] OF INTEGER` and already holds the data in the figure. Write pseudocode to output the total sales for each stall, then output the number of the week with the highest total sales across all three stalls.

```pseudocode
DECLARE Row, Column, StallTotal, WeekTotal, BestTotal, BestWeek : INTEGER

FOR Row ← 1 TO 3
   StallTotal ← 0
   FOR Column ← 1 TO 4
      StallTotal ← StallTotal + Sales[Row, Column]
   NEXT Column
   OUTPUT "Stall ", Row, " total: ", StallTotal
NEXT Row

BestTotal ← -1
BestWeek ← 0
FOR Column ← 1 TO 4
   WeekTotal ← 0
   FOR Row ← 1 TO 3
      WeekTotal ← WeekTotal + Sales[Row, Column]
   NEXT Row
   IF WeekTotal > BestTotal THEN
      BestTotal ← WeekTotal
      BestWeek ← Column
   ENDIF
NEXT Column
OUTPUT "Best week: ", BestWeek
```

Mark points:

- nested loops for stall totals, with rows 1 to 3 and columns 1 to 4 [B1]
- stall total reset to 0 for each stall, before the inner loop [B1]
- adds `Sales[Row, Column]` and outputs each stall's total after the inner loop [B1]
- nested loops for week totals with the week as the outer loop and the total reset for each week [B1]
- compares each week total with the best so far and stores the total and the week number [B1]
- outputs the best week after the loops [B1]

With the data in the figure the stall totals are 50, 42 and 72, and the week totals are 40, 43, 38 and 43. Weeks 2 and 4 tie on 43. Because the test is `>`, a later week only replaces the best when it is strictly greater, so the output is week 2. If a question cares about ties, say how your algorithm treats them.
:::

The same in Python uses a **list of lists**: `sales[1][2]` is the second row, third column, which is `Sales[2, 3]` in pseudocode.

```python
sales = [[12, 15, 9, 14],
         [8, 11, 13, 10],
         [20, 17, 16, 19]]
for stall in range(3):
    stall_total = 0
    for week in range(4):
        stall_total = stall_total + sales[stall][week]
    print("Stall", stall + 1, "total:", stall_total)
best_total = -1
best_week = 0
for week in range(4):
    week_total = 0
    for stall in range(3):
        week_total = week_total + sales[stall][week]
    if week_total > best_total:
        best_total = week_total
        best_week = week + 1
print("Best week:", best_week)
```

Output:

```output
Stall 1 total: 50
Stall 2 total: 42
Stall 3 total: 72
Best week: 2
```

:::warn Creating a 2D list in Python
`[[0] * 4] * 3` looks like a 3 × 4 table of zeros, but it is three references to the **same** row: change one row and all three change. Build each row separately with a loop (a list comprehension) instead.
:::

This program shows the problem and the fix:

```python
grid = [[0] * 4] * 3
grid[0][0] = 5
print(grid)
safe = [[0] * 4 for row in range(3)]
safe[0][0] = 5
print(safe)
```

Output:

```output
[[5, 0, 0, 0], [5, 0, 0, 0], [5, 0, 0, 0]]
[[5, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

### Arrays of records, and choosing a structure

When each item has several fields, combine the two ideas: an **array of records**. The library from earlier becomes:

```pseudocode
DECLARE Library : ARRAY[1:500] OF Book
```

`Library[3].Title` is the title of the third book. The index chooses the record; the dot chooses the field. The loop that counts books on loan is the array loop again:

```pseudocode
OnLoanCount ← 0
FOR Index ← 1 TO 500
   IF Library[Index].OnLoan = TRUE THEN
      OnLoanCount ← OnLoanCount + 1
   ENDIF
NEXT Index
```

Paper 2 often asks you to choose or justify a data structure. Match the structure to the shape of the data.

:::cols
:::col 1D array
A list of values of **one type**, each identified by one number: the 30 marks in a test, 365 daily readings.
:::
:::col 2D array
A **table** of values of one type, identified by two numbers: seats in rows and columns, sales by stall and week.
:::
:::col Array of records
A list of **items with several fields of different types**: books, patients, runners. Keeps each item's data together.
:::
:::

Before records existed in a language, programmers used **parallel arrays**: separate 1D arrays (Names, Ages, Paid) where the same index refers to the same person. They work, but every sort or deletion must move the matching element in every array, which is easy to get wrong. An array of records avoids that, so it is usually the better justification in an exam answer.

:::exam Justifying a structure
"Justify" needs a reason taken from the scenario. "A 2D array, because the data is a table" earns little. "A 2D array, because each value is identified by both the stall number and the week number, and all the values are integers" earns the mark.
:::

## Linear search

A search answers the question "is this value in the array, and where?". The simplest method checks each element in turn.

:::def Linear search
A search that compares each element of an array with the search value in turn, starting from the first, until the value is found or every element has been checked.
:::

A linear search works on any array, sorted or not. Its cost is the number of comparisons: if the item is at position \(k\), the search makes \(k\) comparisons; if the item is not there, it checks all \(n\) elements.

The efficient version stops as soon as it finds the item, so it uses a condition-controlled loop with a Boolean flag. This version searches an array of eight names.

```pseudocode
DECLARE Names : ARRAY[1:8] OF STRING
DECLARE SearchName : STRING
DECLARE Index : INTEGER
DECLARE Found : BOOLEAN

INPUT SearchName
Found ← FALSE
Index ← 1
WHILE Found = FALSE AND Index <= 8
   IF Names[Index] = SearchName THEN
      Found ← TRUE
   ELSE
      Index ← Index + 1
   ENDIF
ENDWHILE
IF Found = TRUE THEN
   OUTPUT SearchName, " found at position ", Index
ELSE
   OUTPUT SearchName, " not found"
ENDIF
```

Two details make it work. Index only increases when the name does not match, so when the loop ends with Found TRUE, Index is still the position of the match. And the condition `Index <= 8` stops the loop after the last element, so the search never reads `Names[9]`.

:::eg Tracing the linear search
Names holds Amara, Bilal, Chen, Dina, Emeka, Farah, Goran and Hana (positions 1 to 8). Complete a trace table when the user inputs Emeka.

A trace table has a column for each variable and for the output, and a new row each time a value changes. Copy the algorithm's order exactly.

| SearchName | Found | Index | Names[Index] compared | OUTPUT |
|---|---|---|---|---|
| Emeka | FALSE | 1 | Amara | |
| | | 2 | Bilal | |
| | | 3 | Chen | |
| | | 4 | Dina | |
| | TRUE | 5 | Emeka | |
| | | | | Emeka found at position 5 |

The search made 5 comparisons. A search for "Zara" would compare all 8 names, finish with Index = 9 and Found = FALSE, and output "Zara not found".
:::

The Python version is a direct translation, with the index starting at 0:

```python
names = ["Amara", "Bilal", "Chen", "Dina", "Emeka", "Farah", "Goran", "Hana"]
search_name = "Emeka"
found = False
index = 0
while not found and index < len(names):
    if names[index] == search_name:
        found = True
    else:
        index = index + 1
if found:
    print(search_name, "found at position", index + 1)
else:
    print(search_name, "not found")
```

Output:

```output
Emeka found at position 5
```

Python can also do this in one line (`search_name in names`), but an exam asks you to write the algorithm, so write the loop.

### When to use a FOR loop instead

If you must look at every element anyway, a FOR loop is simpler and clearer. Counting how many times a value appears is the classic case: you cannot stop at the first match, because there may be more.

```pseudocode
Count ← 0
FOR Index ← 1 TO 8
   IF Names[Index] = SearchName THEN
      Count ← Count + 1
   ENDIF
NEXT Index
OUTPUT SearchName, " appears ", Count, " times"
```

:::exam "Write efficient pseudocode"
When a question says "efficient", an examiner looks for a loop that stops as soon as the job is done. A linear search with a FOR loop that keeps going after a match finds the right answer, but it can lose the efficiency mark. Use WHILE (or REPEAT) with a flag when you can stop early; use FOR when every element must be visited.
:::

## Bubble sort

Sorting puts the elements in order, ascending (smallest first) or descending. Paper 2 expects you to write one sorting algorithm from memory: the bubble sort.

:::def Bubble sort
A sort that repeatedly passes through an array comparing each pair of adjacent elements and swapping them if they are in the wrong order. After each pass, the largest remaining value has moved to its final position.
:::

Watch one pass on the five values 41, 17, 33, 8, 25 (ascending):

1. Compare 41 and 17: wrong order, swap. Now 17, 41, 33, 8, 25.
2. Compare 41 and 33: swap. Now 17, 33, 41, 8, 25.
3. Compare 41 and 8: swap. Now 17, 33, 8, 41, 25.
4. Compare 41 and 25: swap. Now 17, 33, 8, 25, 41.

The largest value, 41, has "bubbled" to the end in one pass, so it never needs to be compared again. Each later pass fixes the next largest value. With \(n\) elements, at most \(n - 1\) passes are needed.

| After pass | Array |
|---|---|
| start | 41, 17, 33, 8, 25 |
| 1 | 17, 33, 8, 25, 41 |
| 2 | 17, 8, 25, 33, 41 |
| 3 | 8, 17, 25, 33, 41 |
| 4 | 8, 17, 25, 33, 41 |

### Swapping two elements

The heart of the sort is the swap, and it needs a third variable. If you write `Values[J] ← Values[J + 1]` first, the old value of `Values[J]` is overwritten and lost. Store it in a temporary variable first.

:::key Swapping two elements
```pseudocode
Temp ← Values[J]
Values[J] ← Values[J + 1]
Values[J + 1] ← Temp
```
Temp must have the same data type as the elements (for an array of records, Temp is a record).
:::

### The basic version

The simplest bubble sort uses two FOR loops: the outer loop counts passes, the inner loop compares each adjacent pair. For an array `Values[1:5]` the inner loop runs J from 1 to 4, comparing `Values[J]` with `Values[J + 1]`.

```pseudocode
FOR Pass ← 1 TO 4
   FOR J ← 1 TO 4
      IF Values[J] > Values[J + 1] THEN
         Temp ← Values[J]
         Values[J] ← Values[J + 1]
         Values[J + 1] ← Temp
      ENDIF
   NEXT J
NEXT Pass
```

The inner loop stops at 4, not 5: when J is 4 it compares elements 4 and 5. Going to 5 would compare `Values[5]` with `Values[6]`, which is outside the array. This version always makes \(4 \times 4 = 16\) comparisons for five elements, even if the data was sorted to begin with.

### The efficient version

Two improvements make the sort much faster on data that is nearly in order, and they are what Cambridge means by an efficient bubble sort.

1. **Shrink the boundary.** After each pass the last unsorted position is fixed, so the next pass can stop one place earlier.
2. **Stop when a pass makes no swaps.** If nothing was swapped, the array is already sorted. A Boolean flag records whether any swap happened.

```pseudocode
DECLARE Values : ARRAY[1:5] OF INTEGER
DECLARE Boundary, J, Temp : INTEGER
DECLARE NoSwaps : BOOLEAN

Boundary ← 4
REPEAT
   NoSwaps ← TRUE
   FOR J ← 1 TO Boundary
      IF Values[J] > Values[J + 1] THEN
         Temp ← Values[J]
         Values[J] ← Values[J + 1]
         Values[J + 1] ← Temp
         NoSwaps ← FALSE
      ENDIF
   NEXT J
   Boundary ← Boundary - 1
UNTIL NoSwaps = TRUE OR Boundary = 0
```

On 41, 17, 33, 8, 25 this makes 4, then 3, then 2 comparisons; pass 3 still swaps (17 and 8), so a fourth pass runs with Boundary 1, makes 1 comparison and no swaps, and the loop stops. That is \(4 + 3 + 2 + 1 = 10\) comparisons instead of 16. On data that is already sorted, the first pass makes 4 comparisons, swaps nothing, and the sort finishes at once.

:::tip Which way round?
For descending order, change `>` to `<` in the comparison. Nothing else changes. For strings, `>` compares character codes from the left, so "Ali" < "Ben" < "Mia"; capital letters have smaller codes than lower-case ones, so "zoe" sorts after "Zoe" and after "Mia".
:::

Here is the efficient sort in Python. It prints the list after each pass and counts the comparisons, so you can check the table above.

```python
values = [41, 17, 33, 8, 25]
boundary = len(values) - 1
comparisons = 0
pass_number = 0
no_swaps = False
while not no_swaps and boundary > 0:
    no_swaps = True
    pass_number = pass_number + 1
    for j in range(boundary):
        comparisons = comparisons + 1
        if values[j] > values[j + 1]:
            temp = values[j]
            values[j] = values[j + 1]
            values[j + 1] = temp
            no_swaps = False
    boundary = boundary - 1
    print(f"After pass {pass_number}: {values}")
print("Comparisons:", comparisons)
```

Output:

```output
After pass 1: [17, 33, 8, 25, 41]
After pass 2: [17, 8, 25, 33, 41]
After pass 3: [8, 17, 25, 33, 41]
After pass 4: [8, 17, 25, 33, 41]
Comparisons: 10
```

Python has no REPEAT … UNTIL, so the program uses a WHILE loop whose condition is the opposite of the UNTIL condition: repeat while "not no swaps and boundary > 0". `range(boundary)` gives j = 0 to boundary − 1, which compares the same pairs as J = 1 to Boundary in pseudocode.

### Sorting records and parallel arrays

To sort an array of records by one field, compare that field but swap **whole records**, so each item's data stays together. For runners sorted by finishing time:

```pseudocode
IF Runners[J].Time > Runners[J + 1].Time THEN
   TempRunner ← Runners[J]
   Runners[J] ← Runners[J + 1]
   Runners[J + 1] ← TempRunner
   NoSwaps ← FALSE
ENDIF
```

TempRunner is declared with the record type. With parallel arrays you would need a separate swap for every array (names, times, clubs), and forgetting one scrambles the data. That is another reason to prefer records.

Python can swap two list elements in one line, `values[j], values[j + 1] = values[j + 1], values[j]`, and it has a built-in `sort()`. Both are fine in your own programs. In an exam that asks for a bubble sort, write the comparisons and the swap yourself.

:::board
Cambridge 9618 tests arrays and sorting on paper, in pseudocode, in Paper 2, and in a real language on a computer in Paper 4. AQA A Level Computer Science (7517) tests programming in an on-screen exam (Paper 1) built around a skeleton program that is released before the exam.
:::

:::eg Spot the error: the inner loop of a bubble sort
Question: Heights is a 1D array of six integers with bounds 1 to 6. Write pseudocode for **one pass** of a bubble sort that puts Heights into ascending order. [4 marks]

A student wrote:

```pseudocode
01  FOR J ← 1 TO 5
02     IF Heights[J] > Heights[J + 1] THEN
03        Heights[J] ← Heights[J + 1]
04        Heights[J + 1] ← Heights[J]
05     ENDIF
06  NEXT J
```

Line 01 loops from 1 to 5, the right limit for comparing pairs in six elements [B1]. Line 02 compares adjacent elements in the right direction [B1]. **Lines 03 and 04 do not swap: line 03 overwrites `Heights[J]`, so line 04 copies the new value straight back. The swap mark is lost** [B0]. Lines 05 and 06 close the IF and the loop correctly [B1]. The answer scores 3 out of 4.

To see the damage, suppose `Heights[1]` is 172 and `Heights[2]` is 165. Line 03 makes `Heights[1]` 165; line 04 copies that 165 into `Heights[2]`. Both elements are now 165, and 172 has vanished. A corrected swap uses a temporary variable:

```pseudocode
03        Temp ← Heights[J]
04        Heights[J] ← Heights[J + 1]
05        Heights[J + 1] ← Temp
```

A two-element dry run, like the one above, catches this slip in seconds.
:::

:::try Start easy, finish at exam standard
Q: State a suitable data type for each of: the number of pupils in a class; the mean mark of the class; a pupil's initial; a pupil's mobile phone number, such as +254 712 000 111.
A: INTEGER (a whole number); REAL (a mean can have a fractional part); CHAR (one character); STRING (it contains `+` and spaces and is never used in arithmetic).
Q: `DECLARE Heights : ARRAY[0:24] OF REAL`. State the lower bound, the upper bound and the number of elements.
A: Lower bound 0, upper bound 24, and \(24 - 0 + 1 = 25\) elements.
Q: Write a pseudocode declaration for a 2D array Board to represent a game board of 6 rows and 7 columns, where each square holds one character.
A: `DECLARE Board : ARRAY[1:6, 1:7] OF CHAR`
Q: The array Nums holds 4, 9, 2, 7, 5 (indexes 1 to 5). What is output by `FOR I ← 1 TO 5`, `IF Nums[I] MOD 2 = 1 THEN OUTPUT Nums[I] ENDIF`, `NEXT I`?
A: It outputs the odd values in order: 9, 7, 5.
Q: What does this Python print? `stock = [5, 0, 12, 3]` then `print(stock[2], len(stock))`.
A: `12 4`. Index 2 is the third item, because Python lists count from 0, and the list has 4 items.
Q: Rain is a 1D array of 30 REAL values, one per day of a month. Write pseudocode to output the number of dry days (days with 0.0 rainfall).
A: Every element must be checked, so use a FOR loop and a counter.

```pseudocode
DryDays ← 0
FOR Day ← 1 TO 30
   IF Rain[Day] = 0.0 THEN
      DryDays ← DryDays + 1
   ENDIF
NEXT Day
OUTPUT "Dry days: ", DryDays
```

Q: Show the array after the first pass of a bubble sort into ascending order on 6, 2, 9, 4, 1.
A: Compare 6 and 2: swap (2, 6, 9, 4, 1). Compare 6 and 9: no swap. Compare 9 and 4: swap (2, 6, 4, 9, 1). Compare 9 and 1: swap. After pass 1: 2, 6, 4, 1, 9.
Q: A linear search looks for a value in an array of 10 elements. How many comparisons does it make if the value is at position 6? How many if the value is not in the array?
A: 6 comparisons if it is at position 6 (it stops when found); 10 comparisons if it is not there (every element is checked).
Q: Write the pseudocode to define a record type Flight with fields FlightCode, Seats (the number of seats), Departure (a date) and Delayed.
A: Choose a type for each field that matches the data.

```pseudocode
TYPE Flight
   DECLARE FlightCode : STRING
   DECLARE Seats : INTEGER
   DECLARE Departure : DATE
   DECLARE Delayed : BOOLEAN
ENDTYPE
```

Q: Marks is a 2D array `ARRAY[1:4, 1:3] OF INTEGER` holding these marks (one row per student, one column per test): row 1: 12, 18, 15; row 2: 9, 14, 11; row 3: 20, 17, 19; row 4: 13, 10, 16. Write pseudocode to output the total of test 2 for all students, and give the value it outputs.
A: Fix the column at 2 and loop through the rows.

```pseudocode
Total ← 0
FOR Student ← 1 TO 4
   Total ← Total + Marks[Student, 2]
NEXT Student
OUTPUT Total
```

The output is \(18 + 14 + 17 + 10 = 59\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A gym stores, for each member, a member code (for example GY0042), the monthly fee (for example 25.50) and whether the member has a locker. State the most suitable data type for each item, with a reason.
A: The mark for each item needs a correct type and a reason.

- Member code: STRING, because it contains letters and a leading zero [B1]
- Monthly fee: REAL, because money has a fractional part [B1]
- Has a locker: BOOLEAN, because there are only two possible values [B1]

Q: [4 marks] ★ A courier company records, for each parcel, a parcel ID (a string), the destination city, the mass in kilograms and whether the parcel has been delivered. Write pseudocode to define a record type Parcel, declare a variable Item of this type, and assign the values "PX-3317", "Quito", 2.4 and FALSE to its fields.
A: One possible answer:

```pseudocode
TYPE Parcel
   DECLARE ParcelID : STRING
   DECLARE Destination : STRING
   DECLARE Mass : REAL
   DECLARE Delivered : BOOLEAN
ENDTYPE

DECLARE Item : Parcel
Item.ParcelID ← "PX-3317"
Item.Destination ← "Quito"
Item.Mass ← 2.4
Item.Delivered ← FALSE
```

- `TYPE Parcel` … `ENDTYPE` [B1]
- four fields with suitable data types [B1]
- `DECLARE Item : Parcel` [B1]
- all four values assigned with dot notation [B1]

Q: [5 marks] ★★ (#cs.datatypes) The 1D array Scores, with bounds 1 to 20, already holds 20 integer test scores. Write pseudocode to calculate the mean of the scores, then output the mean and the number of scores that are greater than the mean.
H: You cannot count the scores above the mean until you know the mean, so you need two loops.
H: Declare the mean as REAL, because `/` gives a REAL.
A: One possible answer:

```pseudocode
DECLARE Index, Total, AboveCount : INTEGER
DECLARE Mean : REAL

Total ← 0
FOR Index ← 1 TO 20
   Total ← Total + Scores[Index]
NEXT Index
Mean ← Total / 20
AboveCount ← 0
FOR Index ← 1 TO 20
   IF Scores[Index] > Mean THEN
      AboveCount ← AboveCount + 1
   ENDIF
NEXT Index
OUTPUT "Mean: ", Mean
OUTPUT "Scores above the mean: ", AboveCount
```

- total initialised to 0 and a loop through all 20 elements adding each score [B1]
- mean calculated after the first loop, as Total / 20 [B1]
- second loop through all 20 elements [B1]
- compares each score with the mean and increments a counter that started at 0 [B1]
- outputs the mean and the count after the loops [B1]

Q: [6 marks] ★★ The pseudocode below sorts the array Data, with bounds 1 to 4. Data holds 15, 3, 11, 7. Complete a trace table with columns Boundary, NoSwaps, J, Temp, Data[1], Data[2], Data[3] and Data[4].

```pseudocode
Boundary ← 3
REPEAT
   NoSwaps ← TRUE
   FOR J ← 1 TO Boundary
      IF Data[J] > Data[J + 1] THEN
         Temp ← Data[J]
         Data[J] ← Data[J + 1]
         Data[J + 1] ← Temp
         NoSwaps ← FALSE
      ENDIF
   NEXT J
   Boundary ← Boundary - 1
UNTIL NoSwaps = TRUE OR Boundary = 0
```

H: Write a new row each time a variable changes, in the order the lines run. Start with the initial values in the first row.
H: In pass 1 the 15 moves all the way to the end, so there are three swaps.
A: One row per change; blank cells mean "unchanged".

| Boundary | NoSwaps | J | Temp | Data[1] | Data[2] | Data[3] | Data[4] |
|---|---|---|---|---|---|---|---|
| 3 | TRUE | | | 15 | 3 | 11 | 7 |
| | FALSE | 1 | 15 | 3 | 15 | | |
| | FALSE | 2 | 15 | | 11 | 15 | |
| | FALSE | 3 | 15 | | | 7 | 15 |
| 2 | TRUE | 1 | | | | | |
| | FALSE | 2 | 11 | | 7 | 11 | |
| 1 | TRUE | 1 | | | | | |
| 0 | | | | | | | |

- initial values: Boundary 3 and the data 15, 3, 11, 7 [B1]
- pass 1: three swaps with Temp = 15 each time, ending 3, 11, 7, 15 [B1]
- NoSwaps set TRUE at the start of each pass and FALSE at each swap [B1]
- Boundary decreases 3, 2, 1, 0, once after each pass [B1]
- pass 2: J = 1 makes no swap; J = 2 swaps (Temp = 11), ending 3, 7, 11, 15 [B1]
- pass 3: one comparison and no swap, so NoSwaps is still TRUE and the loop ends [B1]

(Rows may be split differently, as long as the values in each column appear in the correct order.)

Q: [6 marks] ★★ An array Parcels, with bounds 1 to 200, holds records of the type Parcel from the earlier question. Write efficient pseudocode that inputs a parcel ID, searches Parcels for it, and outputs its destination, or the message "Not found" if no parcel has that ID.
H: "Efficient" means the search must stop as soon as the parcel is found.
H: Compare the ParcelID field, not the whole record.
A: One possible answer:

```pseudocode
DECLARE SearchID : STRING
DECLARE Index : INTEGER
DECLARE Found : BOOLEAN

INPUT SearchID
Found ← FALSE
Index ← 1
WHILE NOT Found AND Index <= 200
   IF Parcels[Index].ParcelID = SearchID THEN
      Found ← TRUE
   ELSE
      Index ← Index + 1
   ENDIF
ENDWHILE
IF Found THEN
   OUTPUT Parcels[Index].Destination
ELSE
   OUTPUT "Not found"
ENDIF
```

- inputs the search ID [B1]
- initialises the flag (or uses the index) and starts at 1 [B1]
- a condition-controlled loop that stops when found **or** after element 200 [B1]
- compares `Parcels[Index].ParcelID` with the search ID [B1]
- increments the index only when not found (or keeps the position of the match) [B1]
- outputs the destination of the matching record, or "Not found", after the loop [B1]

Q: [8 marks] ★★★ A hotel in Mombasa has 5 floors with 20 rooms on each floor. The 2D array Occupied, declared as `ARRAY[1:5, 1:20] OF BOOLEAN`, holds TRUE for an occupied room and FALSE for a free room, where the first index is the floor and the second is the room number.

(a) Justify the use of a 2D array for this data. [2]

(b) Write pseudocode to output, for each floor, the number of free rooms, and then output the floor with the most free rooms. [6]
H: For (b), the count of free rooms must restart for every floor.
H: Keep track of the largest count and the floor where it occurred, as in the "best week" example, but with new data.
A: (a) Each room is identified by two numbers, the floor and the room number [B1], and every value is of the same type, Boolean [B1].

(b) One possible answer:

```pseudocode
DECLARE Floor, Room, FreeCount, MostFree, BestFloor : INTEGER

MostFree ← -1
BestFloor ← 0
FOR Floor ← 1 TO 5
   FreeCount ← 0
   FOR Room ← 1 TO 20
      IF Occupied[Floor, Room] = FALSE THEN
         FreeCount ← FreeCount + 1
      ENDIF
   NEXT Room
   OUTPUT "Floor ", Floor, ": ", FreeCount, " free rooms"
   IF FreeCount > MostFree THEN
      MostFree ← FreeCount
      BestFloor ← Floor
   ENDIF
NEXT Floor
OUTPUT "Most free rooms on floor ", BestFloor
```

- outer loop for floors 1 to 5 and inner loop for rooms 1 to 20 [B1]
- free count reset to 0 for each floor, inside the outer loop [B1]
- tests `Occupied[Floor, Room] = FALSE` (or `NOT Occupied[Floor, Room]`) and increments the count [B1]
- outputs each floor's count after the inner loop [B1]
- compares with the largest so far and records the count and the floor [B1]
- outputs the floor with the most free rooms after both loops [B1]

Q: [7 marks] ★★★ (#cs.datatypes) A running club stores its results in the array Runners, with bounds 1 to 50, of the record type Runner. Each Runner has the fields Name (STRING), Club (STRING) and Time (INTEGER, the finishing time in seconds). Write efficient pseudocode to sort Runners into ascending order of Time.
H: Use the efficient bubble sort: a flag for "no swaps" and a boundary that shrinks.
H: Compare the Time fields, but swap the whole records, using a temporary variable of type Runner.
A: One possible answer:

```pseudocode
DECLARE Boundary, J : INTEGER
DECLARE NoSwaps : BOOLEAN
DECLARE TempRunner : Runner

Boundary ← 49
REPEAT
   NoSwaps ← TRUE
   FOR J ← 1 TO Boundary
      IF Runners[J].Time > Runners[J + 1].Time THEN
         TempRunner ← Runners[J]
         Runners[J] ← Runners[J + 1]
         Runners[J + 1] ← TempRunner
         NoSwaps ← FALSE
      ENDIF
   NEXT J
   Boundary ← Boundary - 1
UNTIL NoSwaps = TRUE OR Boundary = 0
```

- outer post-condition (or pre-condition) loop that repeats passes [B1]
- flag set to TRUE at the start of each pass and FALSE when a swap is made [B1]
- inner loop from 1 to the boundary, which starts at 49 [B1]
- compares the Time fields of adjacent records with `>` [B1]
- swaps whole records using a temporary variable of type Runner [B1]
- boundary decreased by 1 after each pass [B1]
- loop ends when a pass makes no swaps (or the boundary reaches 0) [B1]

(A sort that swaps only the Time fields scores no mark for the swap: it separates names from times.)
:::

:::try Stretch for A*
Q: [5 marks] ★★★ The array Codes, with bounds 1 to 1000, holds integers sorted into **ascending** order. A linear search can be improved for sorted data: once it reaches an element greater than the search value, the value cannot be further along. Write pseudocode for this improved search, outputting the position of the search value or "Not present". Then state the greatest number of comparisons it can make, and explain why a search for a value smaller than `Codes[1]` makes only one.
H: The loop needs to stop for three reasons: found, passed the place where it would be, or reached the end.
H: Keep the comparison and the "gone too far" test in one IF … ELSE structure.
A: One possible answer:

```pseudocode
DECLARE Target, Index : INTEGER
DECLARE Finished : BOOLEAN

INPUT Target
Index ← 1
Finished ← FALSE
WHILE NOT Finished AND Index <= 1000
   IF Codes[Index] >= Target THEN
      Finished ← TRUE
   ELSE
      Index ← Index + 1
   ENDIF
ENDWHILE
IF Finished AND Codes[Index] = Target THEN
   OUTPUT "Found at position ", Index
ELSE
   OUTPUT "Not present"
ENDIF
```

- loop that stops when `Codes[Index] >= Target` or after element 1000 [B1]
- index increased only while the element is smaller than the target [B1]
- after the loop, checks equality to decide between found and not present [B1]
- greatest number of comparisons: 1000, when the target is larger than every element (or equal to the last) [B1]
- a target smaller than `Codes[1]` makes `Codes[1] >= Target` true at once, so the loop ends after one comparison [B1]

(This idea, using the order to stop early, leads to the much faster binary search in [Searching, sorting and Big O](#cs.algorithms2).)
Q: [6 marks] ★★★ The array Grades, with bounds 1 to 120, holds one CHAR grade from 'A' to 'E' for each student. The codes of 'A' to 'E' are consecutive (the code of 'B' is one more than the code of 'A', and so on). Using the insert functions ASC and CHR, write pseudocode that counts each grade in a single pass through Grades, storing the counts in a 1D array, and then outputs each grade with its count.
H: `ASC(Grade) - ASC('A') + 1` turns 'A' into 1, 'B' into 2 and so on: use that as the index of a count array.
H: Initialise all five counts to 0 before counting.
A: One possible answer:

```pseudocode
DECLARE Count : ARRAY[1:5] OF INTEGER
DECLARE Index, Position : INTEGER

FOR Index ← 1 TO 5
   Count[Index] ← 0
NEXT Index
FOR Index ← 1 TO 120
   Position ← ASC(Grades[Index]) - ASC('A') + 1
   Count[Position] ← Count[Position] + 1
NEXT Index
FOR Index ← 1 TO 5
   OUTPUT CHR(ASC('A') + Index - 1), ": ", Count[Index]
NEXT Index
```

- declares a 1D array of five INTEGER counts [B1]
- initialises every count to 0 in a loop [B1]
- one loop through all 120 grades [B1]
- calculates the index from the grade's code using ASC [B1]
- increments the matching count [B1]
- outputs each grade letter (using CHR, or literal letters) with its count [B1]

The same idea in Python, run on seven sample grades:

```python
grades = ["B", "A", "C", "B", "E", "B", "A"]
count = [0] * 5
for grade in grades:
    position = ord(grade) - ord("A")
    count[position] = count[position] + 1
for i in range(5):
    print(chr(ord("A") + i) + ":", count[i])
```

Output:

```output
A: 2
B: 3
C: 1
D: 0
E: 1
```

A real program would first check that each grade is between 'A' and 'E', or an unexpected character would give an index outside the array.
:::

:::quiz
? Which data type is most suitable for a customer's telephone number, such as 0207 946 0018?
- INTEGER
- REAL
+ STRING
- CHAR
> A telephone number is never used in arithmetic, and as an INTEGER the leading zero would be lost and the spaces could not be stored. CHAR holds only one character.
? How many elements are in an array declared as `ARRAY[0:9] OF CHAR`?
- 9
+ 10
- 11
- 0
> The number of elements is upper bound − lower bound + 1 = 9 − 0 + 1 = 10. Answering 9 forgets that index 0 is an element too.
? In Python, `temps = [31, 33, 30]`. What is `temps[1]`?
- 31
+ 33
- 30
- an error, because there is no element 1
> Python lists count from 0, so `temps[0]` is 31 and `temps[1]` is 33. The answer 31 treats the list as if it started at 1, as most pseudocode arrays do.
? What is certain after the first pass of a bubble sort into ascending order?
+ The largest value is in the last position.
- The smallest value is in the first position.
- The array is sorted.
- No element has moved more than one place.
> The largest value is swapped along with every comparison until it reaches the end. The smallest value moves only one place towards the front in each pass, so it may not be first yet.
? Why does an efficient linear search use a WHILE loop rather than a FOR loop?
- A FOR loop cannot use a variable as an array index.
+ It can stop as soon as the item is found.
- WHILE loops make each comparison faster.
- Cambridge pseudocode does not allow FOR loops with arrays.
> A FOR loop always runs to its end value. A condition-controlled loop with a Found flag stops at the first match, which saves comparisons when the item is near the front.
? `DECLARE Sales : ARRAY[1:3, 1:4] OF INTEGER`. Which element is in the second row and the third column?
- `Sales[3, 2]`
+ `Sales[2, 3]`
- `Sales[2][3]`
- `Sales[6]`
> The first index is the row and the second is the column, separated by a comma. `Sales[2][3]` is Python's list-of-lists style, not Cambridge pseudocode.
? What is the purpose of the NoSwaps flag in an efficient bubble sort?
- It counts how many swaps have been made.
- It stops the sort after exactly one pass.
+ It ends the sort when a complete pass makes no swaps, because the array is then sorted.
- It shows the position of the largest value.
> NoSwaps is set TRUE at the start of each pass and FALSE whenever a swap happens. If it is still TRUE at the end of a pass, every adjacent pair is in order, so no more passes are needed.
? A program swaps `Values[J]` and `Values[J + 1]` with `Values[J] ← Values[J + 1]` followed by `Values[J + 1] ← Values[J]`. What happens?
- The two values are swapped correctly.
+ Both elements end up holding the value of `Values[J + 1]`.
- Both elements end up holding the value of `Values[J]`.
- The program stops with a run-time error.
> The first assignment overwrites `Values[J]`, so the second copies that new value back. The original `Values[J]` is lost, which is why a swap needs a temporary variable.
:::

:::checklist What you can now do
- [ ] I can choose a suitable data type (INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE) for a value and justify the choice.
- [ ] I can explain the purpose of a record and define a record type in pseudocode.
- [ ] I can read data from and save data to the fields of a record, including in an array of records.
- [ ] I can use the terms index, element, lower bound and upper bound.
- [ ] I can choose a 1D array, a 2D array or an array of records for a task and justify the choice.
- [ ] I can declare 1D and 2D arrays and process them with loops: totals, means, maximum and minimum, counts.
- [ ] I can write an efficient linear search in pseudocode and say how many comparisons it makes.
- [ ] I can write a bubble sort in pseudocode, including the efficient version with a flag and a shrinking boundary.
- [ ] I can complete a trace table for a search or a sort.
- [ ] I can write the same algorithms in Python using lists, lists of lists and classes as records.
:::

:::recap
- The six basic pseudocode types are INTEGER, REAL, CHAR, STRING, BOOLEAN and DATE. Identifiers made of digits, such as phone numbers, are STRINGs.
- REAL literals have a digit on both sides of the point (`4.0`); CHARs use single quotes, STRINGs double quotes. In Python, `input()` always returns a string.
- A record groups fields of different types: `TYPE Name` … `ENDTYPE`, accessed with dot notation (`Item.Mass`). In Python, a class with `__init__` acts as a record.
- An array holds a fixed number of elements of one type: `DECLARE A : ARRAY[1:n] OF <type>`, and has upper − lower + 1 elements. A 2D array is `ARRAY[1:r, 1:c]`, accessed as `A[row, column]`.
- Process arrays with a FOR loop over the bounds; 2D arrays need nested loops, with any total reset inside the outer loop.
- Python lists start at index 0; build 2D lists with a comprehension, never `[[0] * c] * r`.
- Linear search: compare each element in turn; stop early with a flag in a WHILE loop. Found at position \(k\): \(k\) comparisons; not found: \(n\).
- Bubble sort: compare adjacent pairs and swap with a temporary variable; the efficient version shrinks the boundary and stops when a pass makes no swaps.
:::

:::links
- practise: [Data types and records: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/data-types-and-records/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Arrays: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/arrays/exam-questions/) · Save My Exams · array, search and sort questions by difficulty [paid]
- explore: [Sorting animations](https://visualgo.net/en/sorting) · VisuAlgo · watch bubble sort pass by pass, then try other sorts
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste a program from this chapter and watch the list change line by line
- read: [Python lists](https://www.w3schools.com/python/python_lists.asp) · W3Schools · short lessons on lists with try-it boxes
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · the official rules for arrays and records in pseudocode

Links checked 13 November 2026.
:::

Next: [Procedures, functions and parameters](#cs.procedures)
