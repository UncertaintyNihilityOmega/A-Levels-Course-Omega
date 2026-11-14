@chapter cs.programming
@title Programming basics: variables, selection and loops
@level as
@paper CAIE 9618 Paper 2
@time 7–9 hours
@summary The building blocks of every program, at the depth Paper 2 tests. You will declare variables and constants, write arithmetic and Boolean expressions, read input and show output, use the string, number and date functions of the insert, choose between IF and CASE, choose between FOR, WHILE and REPEAT loops, validate input, and write efficient pseudocode, with the Python equivalent of each.

:::why
Paper 2 is a paper of pseudocode written by hand. Every long question, whether it reads a file, searches a list or manages a queue, is made of the same few parts: variables, expressions, input and output, selection and loops. If these are automatic, you can spend the exam thinking about the problem. They are also the first things you type on a computer in Paper 4, in Python.
:::

**Before you start**, you should have worked through [Programming from zero](#cs.f.basics), which introduces each idea gently, and [Computational thinking and algorithms](#cs.algorithms), which gave you structured English, flowcharts and conditions. This chapter goes through the same ground again at exam depth, so every rule is stated precisely and every construct comes with the questions Cambridge asks about it.

:::try Warm-up
Q: What are `17 DIV 5` and `17 MOD 5`? (from [Programming from zero](#cs.f.basics))
A: `17 DIV 5` is 3 and `17 MOD 5` is 2, because \(17 = 3 \times 5 + 2\).
Q: Which loop tests its condition after the body has run once: WHILE or REPEAT … UNTIL? (from [Computational thinking and algorithms](#cs.algorithms))
A: REPEAT … UNTIL. A WHILE loop tests first, so its body can run zero times.
Q: Write the condition "the mark is from 1 to 10 inclusive". (from [Computational thinking and algorithms](#cs.algorithms))
A: `Mark >= 1 AND Mark <= 10`. Two comparisons joined with AND, not a chained comparison.
:::

:::note How code appears in this course
Pseudocode follows the Cambridge Pseudocode Guide for 2027–2029 exactly: keywords in capitals, `←` for assignment, three-space indents. Python blocks are Python 3 and have all been run; the block after a Python program, introduced by "Output:", is exactly what it prints. Where a program reads input, the text says which values were typed.
:::

## Variables, constants and assignment

A program stores values in named places in memory. The name is an identifier (see [Computational thinking and algorithms](#cs.algorithms)). What is stored depends on the data type: INTEGER, REAL, CHAR, STRING, BOOLEAN or DATE.

:::def Variable
A named memory location that stores a value which can change while the program runs.
:::

:::def Constant
A named memory location that stores a value which is set before the program runs and cannot change while it runs.
:::

:::def Declaration
A statement that tells the computer the name and the data type of a variable (or the name and value of a constant) before it is used.
:::

:::def Assignment
A statement that stores a value in a variable. The expression on the right of the `←` is worked out first and its value is stored in the variable on the left.
:::

In pseudocode you declare a variable with `DECLARE` and a constant with `CONSTANT`:

```pseudocode
DECLARE Counter : INTEGER
DECLARE Name : STRING
DECLARE Height, Mass : REAL
CONSTANT HourlyRate = 6.50
CONSTANT SchoolName = "Westfield High"
Counter ← 0
Counter ← Counter + 1
```

Three rules matter in exam answers.

:::key Declarations and assignments
- `DECLARE Identifier : TYPE` gives the name and the type. The guide's own examples declare one name per line, which is always safe; many textbooks and model answers also list several names of one type on one line, separated by commas, as in `DECLARE Height, Mass : REAL`.
- A constant uses `=`, not `←`, and its value must be a **literal** (a plain number, character or string): `CONSTANT Rate = 0.2` is allowed, but `CONSTANT Double = Rate * 2` is not. Apart from type definitions (met in [Data types, records and arrays](#cs.datatypes)), this is the only place `=` is not a comparison.
- An assignment evaluates the right-hand side first. `Counter ← Counter + 1` works out the old value of Counter plus 1, then stores it back. A variable must have been given a value before its value is used.
:::

Python has no declarations. A variable exists as soon as you assign to it, and it takes its type from the value. Python also has no constants, so by convention a name in capitals tells readers not to change it. This is the same Python style as in [Programming from zero](#cs.f.basics).

```python
hourly_rate = 6.50
school_name = "Westfield High"
HOURLY_RATE = 6.50
counter = 0
counter = counter + 1
print(counter, school_name, HOURLY_RATE)
```

Output:

```output
1 Westfield High 6.5
```

Python prints 6.5, not 6.50: it stores a real number and drops trailing zeros. Format a price with an f-string such as `f"{rate:.2f}"` when two decimal places are needed.

### Tracing assignments

Because the right side is evaluated first, the order of statements decides the result. Trace this program by writing one row each time a variable changes.

```pseudocode
X ← 5
Y ← X * 2
X ← X + Y
Y ← X - Y
OUTPUT X, " ", Y
```

| X | Y | OUTPUT |
|---|---|---|
| 5 | | |
| | 10 | |
| 15 | | |
| | 5 | |
| | | 15 5 |

The third statement uses the new Y (10), so X becomes 15. The fourth uses the new X: \(15 - 10 = 5\). Mixing up the old and the new value of a variable is the commonest slip in a trace.

:::eg Declaring a constant and variables
A shop in Kuala Lumpur adds sales tax of 6% to every price. Write pseudocode that declares a suitable constant for the tax rate and variables for the price, the tax and the total, inputs a price, and outputs the total including tax. [4 marks]

The tax rate does not change while the program runs, so it is a constant. The three amounts are money, so they are REAL.

```pseudocode
CONSTANT SalesTax = 0.06
DECLARE Price : REAL
DECLARE Tax : REAL
DECLARE Total : REAL

INPUT Price
Tax ← Price * SalesTax
Total ← Price + Tax
OUTPUT "Total: ", Total
```

- the constant declared with `=` and a literal value [B1]
- the three variables declared with the type REAL [B1]
- the tax calculated as price multiplied by the rate [B1]
- the total calculated and output after it has been calculated [B1]

For a price of 50.00 the tax is \(50.00 \times 0.06 = 3.00\) and the total is 53.00. The same program in Python, run with the typed value 50:

```python
SALES_TAX = 0.06
price = float(input("Price: "))
tax = price * SALES_TAX
total = price + tax
print(f"Total: {total:.2f}")
```

Output, when the user types 50:

```output
Price: 50
Total: 53.00
```
:::

## Expressions and operators

An **expression** combines values, variables and operators and has a value. Pseudocode has three families of operators.

:::def Operator
A symbol or word that carries out an operation on one or two values, such as `+` or `AND`.
:::

| Operation | Pseudocode | Python | Example | Result |
|---|---|---|---|---|
| add, subtract, multiply | `+`  `-`  `*` | `+`  `-`  `*` | `2 + 3 * 4` | 14 |
| divide (always REAL) | `/` | `/` | `17 / 5` | 3.4 |
| whole-number quotient | `DIV` | `//` | `17 DIV 5` | 3 |
| remainder | `MOD` | `%` | `17 MOD 5` | 2 |
| comparison | `=`  `<>`  `<`  `>`  `<=`  `>=` | `==`  `!=`  `<`  `>`  `<=`  `>=` | `Age >= 18` | TRUE or FALSE |
| logic | `AND`  `OR`  `NOT` | `and`  `or`  `not` | `A AND NOT B` | TRUE or FALSE |
| join strings | `&` | `+` | `"Hi " & Name` | a STRING |

The Pseudocode Guide states the normal mathematical order: multiplication and division come before addition and subtraction, and brackets come first of all. It says nothing about `DIV` and `MOD`, and recommends brackets to make the order of a complex expression explicit. So treat `DIV` and `MOD` like division (Python does the same with `//` and `%`), work from left to right at the same level, and add brackets whenever `DIV` or `MOD` meets another operator: brackets never lose a mark.

```python
print(17 / 5, 17 // 5, 17 % 5, 2 + 3 * 4, (2 + 3) * 4)
```

Output:

```output
3.4 3 2 14 20
```

:::warn `=` compares in pseudocode
In an assignment you write `←`; in a condition you write `=`. `IF Total = 10 THEN` asks a question and changes nothing. Python uses `==` for the question and `=` for the assignment, so `if total = 10:` is a syntax error.
:::

### DIV and MOD

`DIV` and `MOD` come from the division you did at primary school: 17 divided by 5 is 3 whole times with 2 left over. They undo each other: \(17 = 3 \times 5 + 2\). Paper 2 questions use them constantly, because they solve a family of problems with one pattern.

:::key What DIV and MOD are used for
- **Last digit and the rest**: `N MOD 10` is the last digit of a whole number; `N DIV 10` is the number without its last digit.
- **Even or odd**: `N MOD 2` is 0 for an even number and 1 for an odd number.
- **Splitting a quantity into units**: `Seconds DIV 60` is the whole minutes and `Seconds MOD 60` the seconds left over.
- **Wrapping round**: `(Hour + 5) MOD 24` is the hour of the clock 5 hours later.
- **Packing**: `Items DIV 12` is the number of full boxes of 12 and `Items MOD 12` the items left over.
:::

:::eg Converting seconds to hours, minutes and seconds
A stopwatch in a school in Port Louis stores a time as a whole number of seconds. Write pseudocode that inputs the number of seconds and outputs the hours, minutes and seconds. Give the output for 7384 seconds.

An hour is 3600 seconds and a minute is 60. Take whole hours first; what is left is less than an hour. Take whole minutes of that; what is left is the seconds.

```pseudocode
INPUT Total
Hours ← Total DIV 3600
Rest ← Total MOD 3600
Minutes ← Rest DIV 60
Seconds ← Rest MOD 60
OUTPUT Hours, " h ", Minutes, " min ", Seconds, " s"
```

For 7384: \(7384 \div 3600\) is 2 remainder 184, so Hours is 2 and Rest is 184. Then \(184 \div 60\) is 3 remainder 4, so Minutes is 3 and Seconds is 4. The output is `2 h 3 min 4 s`.

```python
total = 7384
hours = total // 3600
rest = total % 3600
minutes = rest // 60
seconds = rest % 60
print(hours, "h", minutes, "min", seconds, "s")
```

Output:

```output
2 h 3 min 4 s
```

(In Python, `print` puts a space between the items. In pseudocode, put the spaces you want inside the strings, as the guide's examples do.)
:::

### Boolean expressions

A comparison gives a BOOLEAN value, and a BOOLEAN can be stored like any other. `AND` is true only when both sides are true, `OR` when at least one is, and `NOT` reverses a value.

| A | B | A AND B | A OR B | NOT A |
|---|---|---|---|---|
| TRUE | TRUE | TRUE | TRUE | FALSE |
| TRUE | FALSE | FALSE | TRUE | FALSE |
| FALSE | TRUE | FALSE | TRUE | TRUE |
| FALSE | FALSE | FALSE | FALSE | TRUE |

```pseudocode
IsAdult ← Age >= 18
CanEnter ← IsAdult AND HasTicket
```

A BOOLEAN variable can be used on its own as a condition: write `IF CanEnter THEN`, not `IF CanEnter = TRUE THEN` (though the longer form is also correct). When a condition has both AND and OR, put brackets round each part so that the order is clear: `(Age >= 5 AND Age <= 18) OR HasPass`.

## Input and output

`INPUT` stores a value typed by the user in a variable. `OUTPUT` shows values on the screen. `OUTPUT` takes several values separated by commas. The guide's own examples put any spaces inside the strings (`OUTPUT "You have ", Lives, " lives left"`), so write the spaces you want there.

```pseudocode
INPUT Name
INPUT Hours
Pay ← Hours * 6.50
OUTPUT "Pay for ", Name, " is ", Pay
```

Python's `input()` always returns a string, so a number must be converted with `int()` or `float()` before it is used in a calculation. `print()` takes several values and puts a space between them.

```python
name = input("Name: ")
hours = float(input("Hours worked: "))
rate = 6.50
pay = hours * rate
print("Pay for", name, "is", pay)
```

Output, when the user types Amina and 8:

```output
Name: Amina
Hours worked: 8
Pay for Amina is 52.0
```

To join strings into one longer string, use `&` in pseudocode and `+` in Python. A number must be converted to a string first, with `NUM_TO_STR(Pay)` in pseudocode and `str(pay)` in Python: `"Pay: " & NUM_TO_STR(Pay)`. The comma form of `OUTPUT` does not need that conversion.

## Built-in functions and library routines

A **function** is a named piece of code that you call with some values and that returns a value. Programming languages come with many ready-made ones.

:::def Built-in function
A function that is part of the programming language itself, ready to be used without being written by the programmer.
:::

:::def Library routine
A pre-written, tested routine stored in a library that a program can use, usually after importing the library. In Python, for example, the `random` library holds routines for random numbers.
:::

In Paper 2, an **insert** printed with the paper lists the functions you may use, each with an example. The string functions are always given, so you do not have to memorise their exact names, but you must understand exactly what each one does. A question that needs any other function defines it. These are the ones in the insert:

| Pseudocode | What it returns | Example | Python |
|---|---|---|---|
| `LEFT(S, n)` | the first n characters | `LEFT("computer", 3)` is "com" | `s[:n]` |
| `RIGHT(S, n)` | the last n characters | `RIGHT("computer", 3)` is "ter" | `s[len(s) - n:]` |
| `MID(S, x, n)` | n characters from position x | `MID("computer", 4, 3)` is "put" | `s[x - 1:x - 1 + n]` |
| `LENGTH(S)` | the number of characters | `LENGTH("computer")` is 8 | `len(s)` |
| `TO_UPPER(S)` | capitals | `TO_UPPER("Hi")` is "HI" | `s.upper()` |
| `TO_LOWER(S)` | lower case | `TO_LOWER("Hi")` is "hi" | `s.lower()` |
| `NUM_TO_STR(x)` | a number as text | `NUM_TO_STR(87.5)` is "87.5" | `str(x)` |
| `STR_TO_NUM(S)` | text as a number | `STR_TO_NUM("23.45")` is 23.45 | `float(s)` or `int(s)` |
| `IS_NUM(S)` | TRUE if S is a valid number | `IS_NUM("12")` is TRUE, `IS_NUM("12a")` is FALSE | `s.isdigit()` (whole numbers only) |
| `ASC(C)` | the character code | `ASC('A')` is 65 | `ord(c)` |
| `CHR(n)` | the character with code n | `CHR(65)` is 'A' | `chr(n)` |
| `INT(x)` | the whole-number part | `INT(27.5)` is 27 | `int(x)` |
| `RAND(x)` | a random real from 0 up to but not including x | `RAND(6)` is 0 or more and less than 6 | `random.random() * x` |
| `DAY(d)`, `MONTH(d)`, `YEAR(d)` | parts of a date | `YEAR(14/03/2027)` is 2027 | `d.day`, `d.month`, `d.year` |
| `DAYINDEX(d)` | the day of the week, Sunday is 1 | a Sunday gives 1 | `d.isoweekday() % 7 + 1` |
| `SETDATE(d, m, y)` | a date from three numbers | `SETDATE(14, 3, 2027)` | `datetime.date(y, m, d)` |
| `TODAY()` | today's date | | `datetime.date.today()` |

:::warn Position counts from 1 in pseudocode and from 0 in Python
`MID("computer", 4, 3)` starts at the 4th character, p, and takes three: "put". In Python the first character is at index 0, so the 4th character is `s[3]`, and the slice that matches is `s[3:6]`, not `s[4:7]`. The general translation is `s[x - 1:x - 1 + n]`.
:::

Here are the string functions in Python.

```python
s = "computer"
print(s[:3], s[4 - 1:4 - 1 + 3], s[len(s) - 3:], len(s))
print(s.upper(), "Hi".lower(), str(87.5), float("23.45"), ord("A"), chr(65))
print(int(27.5), int(9.99), int(-2.5), "12".isdigit(), "12a".isdigit(), "-5".isdigit())
```

Output:

```output
com put ter 8
COMPUTER hi 87.5 23.45 65 A
27 9 -2 True False False
```

Three points from the last line. `int()` throws away the fractional part: `int(9.99)` is 9, not 10, and for a negative number it also drops the fraction, so `int(-2.5)` is −2. (Paper 2 keeps to positive numbers.) And `isdigit()` is only a rough match for `IS_NUM`: it is `False` for "-5" and for "3.5", which are valid numbers. When a Python program must accept those, convert with `float()` inside `try` and `except`, which Paper 4 teaches later.

### Random numbers and dates

`RAND(x)` gives a real number from 0 up to, but not including, x. To simulate a dice, scale it and take the whole-number part: `INT(RAND(6)) + 1`. `RAND(6)` is at least 0 and below 6, so `INT` of it is 0 to 5, and adding 1 gives 1 to 6. Python's library routine `random.randint(1, 6)` does the same in one call.

```python
import random
import datetime

roll = int(random.random() * 6) + 1
other = random.randint(1, 6)
print(1 <= roll <= 6, 1 <= other <= 6)

d = datetime.date(2027, 3, 14)
print(d.day, d.month, d.year, d.isoweekday() % 7 + 1)
```

Output:

```output
True True
14 3 2027 1
```

The first line is `True True` whichever numbers are rolled. The date 14/03/2027 is a Sunday, so `DAYINDEX` is 1; Python numbers Monday as 1 and Sunday as 7, so `% 7 + 1` turns Sunday into 1, Monday into 2 and so on.

:::eg Values returned by functions
State the value returned by each of the following. [8 marks]

1. `LEFT("Nairobi", 4)`
2. `MID("Nairobi", 3, 2)`
3. `LENGTH("Nairobi")`
4. `TO_UPPER(RIGHT("Nairobi", 3))`
5. `ASC('C') + 1`
6. `CHR(ASC('C') + 1)`
7. `STR_TO_NUM("12") * 2`
8. `INT(9.99)`

Write the string with its positions: N(1) a(2) i(3) r(4) o(5) b(6) i(7). Work from the inside out when functions are nested.

- 1. "Nair": the first four characters. [B1]
- 2. "ir": two characters starting at position 3. [B1]
- 3. 7. [B1]
- 4. "OBI": `RIGHT` gives "obi" and `TO_UPPER` makes it capitals. [B1]
- 5. 68: `ASC('C')` is 67. [B1]
- 6. 'D': character code 68. [B1]
- 7. 24: the string "12" becomes the number 12. [B1]
- 8. 9: `INT` drops the fraction, it does not round. [B1]
:::

## Selection: IF and CASE

:::def Selection
A programming construct in which a condition decides which statements are executed.
:::

You know `IF … THEN … ELSE … ENDIF` from [Computational thinking and algorithms](#cs.algorithms). A **nested** IF puts one IF inside another.

:::def Nested statement
A statement of one construct (such as an IF or a loop) placed inside the body of another construct.
:::

Take a mark out of 100 and turn it into a grade. A chain of questions, tested from the top, gives Distinction for 70 or more, Pass for 50 to 69, and Fail below 50:

```pseudocode
INPUT Mark
IF Mark >= 70 THEN
   Grade ← "Distinction"
ELSE
   IF Mark >= 50 THEN
      Grade ← "Pass"
   ELSE
      Grade ← "Fail"
   ENDIF
ENDIF
OUTPUT Grade
```

The first condition that is true wins, and the rest of the chain is skipped. In Python, `else` followed by `if` becomes `elif`:

```python
mark = int(input("Mark: "))
if mark >= 70:
    grade = "Distinction"
elif mark >= 50:
    grade = "Pass"
else:
    grade = "Fail"
print(grade)
```

Output, when the user types 63:

```output
Mark: 63
Pass
```

Use the tool below to step through a similar program with different marks. Choose Mark 70 and watch which branch runs: the boundary value belongs with the first condition that includes it.

:::html
<div class="widget" data-w="cs-trace" data-prog="grade"></div>
:::

:::warn Test the most restrictive condition first
In a chain such as `IF Mark >= 50 … ELSE IF Mark >= 70`, a mark of 85 is caught by the first test and the second is never reached, so nobody gets a Distinction. Order a chain so that each test is narrower than the ones after it, or test ranges that cannot overlap.
:::

### The CASE structure

When one variable is compared with several exact values, a `CASE` statement is tidier than a chain of IFs.

:::def CASE structure
A selection construct that compares one expression with a list of values or ranges and runs the statements for the first one that matches, with an OTHERWISE branch for when none match.
:::

```pseudocode
CASE OF Choice
   1 : Price ← 1.50
   2 : Price ← 2.50
   3 : Price ← 4.00
   OTHERWISE : Price ← 0.00
ENDCASE
```

Each line is a value, a colon and the statement to run. A **range** is written with `TO`, as in `70 TO 100 : Grade ← "A"`. Only the first matching line runs. `OTHERWISE` catches everything else and is where you report an invalid value. Python usually writes the same choice as `if … elif … else`, comparing the variable with each value. (Since Python 3.10 there is also a `match` statement, shown in the aside below.)

:::eg A menu with CASE
A parking meter in Sydney sells three lengths of parking: 30 minutes for 1.50, 1 hour for 2.50 and 2 hours for 4.00. Write pseudocode that outputs the menu, inputs the choice and outputs the price. If the choice is not 1, 2 or 3, output "Invalid choice" instead. [5 marks]

The choice is compared with exact values, so CASE fits. Each option calculates one price; the OTHERWISE branch handles anything else.

```pseudocode
OUTPUT "1: 30 minutes  2: 1 hour  3: 2 hours"
INPUT Choice
CASE OF Choice
   1 : OUTPUT 1.50
   2 : OUTPUT 2.50
   3 : OUTPUT 4.00
   OTHERWISE : OUTPUT "Invalid choice"
ENDCASE
```

- the menu output and the choice input before the CASE [B1]
- `CASE OF Choice` with `ENDCASE` [B1]
- the three options 1, 2 and 3 with their prices [B1]
- each price output (or stored and then output) [B1]
- an OTHERWISE branch that outputs "Invalid choice" [B1]

An answer that uses three separate IF statements without ELSE can still score the option marks, but it loses the structure mark, and a choice of 5 would then give no message at all unless the answer added a fourth test.

In Python, with the typed value 2:

```python
print("1: 30 minutes  2: 1 hour  3: 2 hours")
choice = int(input("Choice: "))
if choice == 1:
    print(1.50)
elif choice == 2:
    print(2.50)
elif choice == 3:
    print(4.00)
else:
    print("Invalid choice")
```

Output:

```output
1: 30 minutes  2: 1 hour  3: 2 hours
Choice: 2
2.5
```
:::

Here is the aside promised above. The same choice as a `match` statement, which behaves like CASE:

```python
choice = 3
match choice:
    case 1:
        print(1.50)
    case 2:
        print(2.50)
    case 3:
        print(4.00)
    case _:
        print("Invalid choice")
```

Output:

```output
4.0
```

:::key IF or CASE?
- Use **CASE** when one variable is compared with several exact values or ranges, such as a menu choice, a letter or a mark band.
- Use **IF** when conditions combine several variables or use AND and OR, or when there are only two outcomes.
- In both, put the most restrictive test first and keep an `ELSE` or `OTHERWISE` for the unexpected.
:::

## Iteration: FOR, WHILE and REPEAT

You know the three loops from the last chapters. Here is each precisely, followed by how to choose.

:::def Count-controlled loop
A loop that repeats its body a fixed number of times, decided before the loop starts. In pseudocode this is the FOR loop.
:::

:::def Pre-condition loop
A loop that tests its condition before each repetition of the body, so the body may run zero times. In pseudocode this is the WHILE loop.
:::

:::def Post-condition loop
A loop that tests its condition after each repetition of the body, so the body always runs at least once. In pseudocode this is the REPEAT … UNTIL loop.
:::

```pseudocode
FOR Index ← 1 TO 5
   OUTPUT Index
NEXT Index

WHILE Total < 100
   Total ← Total + 10
ENDWHILE

REPEAT
   INPUT Answer
UNTIL Answer = "yes"
```

:::key The three loops
| | FOR | WHILE | REPEAT … UNTIL |
|---|---|---|---|
| Kind | count-controlled | pre-condition | post-condition |
| Tests | counts from start to end | before each pass | after each pass |
| Runs the body | exactly as many times as counted | zero or more times | at least once |
| Keeps going while | counter has not passed the end | condition is TRUE | condition is FALSE |
| Ends when | counter passes the end value | condition becomes FALSE | condition becomes TRUE |
:::

### The FOR loop and STEP

`FOR Index ← 1 TO 5` counts Index from 1 to 5 in steps of 1. Add `STEP` to count differently, and a negative STEP to count down:

```pseudocode
FOR Count ← 10 TO 2 STEP -2
   OUTPUT Count
NEXT Count
OUTPUT "Go!"
```

This outputs 10, 8, 6, 4, 2, then "Go!". The counter stops when the next value would pass the end value: after 2 comes 0, which is past 2, so the loop ends. Step through it below and watch the FOR line set Count each time round.

:::html
<div class="widget" data-w="cs-trace" data-prog="countdown"></div>
:::

:::key Rules for FOR loops
- The loop variable starts at the first value and changes by STEP each pass (STEP is 1 when it is left out).
- If the start is already past the end (`FOR I ← 5 TO 1` with a positive step), the body runs **zero times**.
- **Never change the loop variable inside the body.** It is controlled by the loop.
- Do not rely on the value of the loop variable after the loop has ended.
- `NEXT` repeats the identifier: `NEXT Count`.
:::

Python's `for` loop uses `range(start, stop, step)`, and **`stop` is not included**. To run a pseudocode loop to its end value, use one past it for a positive step, and one before it for a negative step.

| Pseudocode | Python | Values |
|---|---|---|
| `FOR Index ← 1 TO 5` | `range(1, 6)` | 1, 2, 3, 4, 5 |
| `FOR Index ← 0 TO 20 STEP 5` | `range(0, 21, 5)` | 0, 5, 10, 15, 20 |
| `FOR Count ← 10 TO 2 STEP -2` | `range(10, 1, -2)` | 10, 8, 6, 4, 2 |
| `FOR Index ← 5 TO 1` | `range(5, 0)` | no values: zero times |

```python
for count in range(10, 1, -2):
    print(count)
print("Go!")
```

Output:

```output
10
8
6
4
2
Go!
```

### WHILE and REPEAT

A `WHILE` loop carries on while its condition is true. A `REPEAT … UNTIL` loop carries on until its condition is true. They are opposites: to turn one into the other, negate the condition (see [Computational thinking and algorithms](#cs.algorithms)). The first example writes the squares up to 50 with each loop.

```pseudocode
Count ← 1
WHILE Count <= 5
   OUTPUT Count * Count
   Count ← Count + 1
ENDWHILE
```

```pseudocode
Count ← 1
REPEAT
   OUTPUT Count * Count
   Count ← Count + 1
UNTIL Count > 5
```

Both output 1, 4, 9, 16 and 25. The conditions are opposites: the `WHILE` loop runs while `Count <= 5`, and the `REPEAT` loop runs until `Count > 5`. Python has only `while` and no `REPEAT`. The usual translation is a `while` loop that tests the **opposite** of the `UNTIL` condition, or `while True` with a `break`:

```python
count = 1
while count <= 5:
    print(count * count)
    count = count + 1

count = 1
while True:
    print(count * count)
    count = count + 1
    if count > 5:
        break
```

Output:

```output
1
4
9
16
25
1
4
9
16
25
```

The two rewrites are only equal here because Count starts at 1, so the first test of the WHILE loop would pass anyway. If Count started at 9, the WHILE version would output nothing but the REPEAT version would still output 81 once, because a REPEAT body always runs once before it is tested. Rewriting a WHILE as a REPEAT is safe only when you know the body should run at least once.

### Choosing the loop

:::key Which loop?
- **FOR**: you know, or can calculate, how many times to repeat: the 12 times table, 30 students, every character of a string.
- **REPEAT … UNTIL**: the body must run **at least once**, and what happens next depends on its result: asking for input until it is valid, a menu shown until the user chooses Quit.
- **WHILE**: the body may need to run **zero times**: reading values until a sentinel when there may be none, searching until an item is found or the data runs out.
:::

:::eg Justify the choice of loop
For each task, name the most suitable loop and justify the choice. [4 marks]

(a) Output the 12 times table, from 1 × 12 to 12 × 12.
(b) Keep asking a user for a password until it is correct.

For each one, ask: do I know how many times? Must it run at least once? Could it run zero times?

- (a) A FOR loop [B1], because the number of repetitions (12) is known in advance. [B1]
- (b) A REPEAT … UNTIL loop [B1], because the password must be asked for at least once, and whether to repeat depends on what was typed. [B1]

A mark needs the loop **and** the reason. "A FOR loop because it is the best" earns nothing for the reason. A WHILE loop for (b) is possible if the first input is read before the loop, but the reason in the mark scheme is the one about "at least once".
:::

### Validation loops

A common use of REPEAT is **input validation**: keep asking until the value is acceptable. Here is a program that accepts only an age from 5 to 18.

```pseudocode
REPEAT
   INPUT Age
   IF Age < 5 OR Age > 18 THEN
      OUTPUT "Age must be 5 to 18"
   ENDIF
UNTIL Age >= 5 AND Age <= 18
OUTPUT "Accepted: ", Age
```

Two points. The error message is under the *invalid* condition `Age < 5 OR Age > 18`, while the loop ends on the *valid* condition `Age >= 5 AND Age <= 18`, which is its negation. Run it with the typed values 3, 25 and 12 below: the first two get the message and 12 is accepted.

:::html
<div class="widget" data-w="cs-trace" data-prog="validate"></div>
:::

When the input must be a number, read it as a string, check it with `IS_NUM` and only then convert it. A `WHILE` loop and a `REPEAT` loop both work; this version keeps the pseudocode short.

```pseudocode
REPEAT
   INPUT Entry
UNTIL IS_NUM(Entry)
Age ← STR_TO_NUM(Entry)
```

Here is a Python version that rejects anything that is not a whole number, run with the typed values abc, −4 and 17:

```python
entry = input("Age: ")
while not entry.isdigit():
    print("Please type a whole number")
    entry = input("Age: ")
age = int(entry)
print("Age:", age)
```

Output, when the user types abc, -4 and 17:

```output
Age: abc
Please type a whole number
Age: -4
Please type a whole number
Age: 17
Age: 17
```

:::warn `IS_NUM` accepts more than whole numbers
`IS_NUM("-4")` and `IS_NUM("3.5")` are TRUE, because both are valid numbers. A program that needs a positive whole number must still check the range after converting the string.
:::

:::eg Spot the error: the loop that ends on the wrong condition
Question: Write pseudocode that repeatedly asks for a quantity until the user enters a whole number from 1 to 10, then outputs it. [4 marks]

A student wrote:

```pseudocode
01  REPEAT
02     INPUT Quantity
03  UNTIL Quantity < 1 OR Quantity > 10
04  OUTPUT Quantity
```

The loop is a REPEAT … UNTIL, which is the right structure for validation [B1], and the INPUT is inside the loop [B1]. **Line 03 gives the condition for an invalid number. `UNTIL` stops when its condition is true, so the loop stops as soon as the user types something wrong and carries on while the user types something correct. The condition mark is lost** [B0]. Line 04 outputs after the loop [B1]. The answer scores 3 out of 4.

To see the damage, type 5. It is valid, but the condition `Quantity < 1 OR Quantity > 10` is false, so the loop asks again; it only ends when the user types 12 (an invalid number), and the program then outputs 12. The fix is the negation: `UNTIL Quantity >= 1 AND Quantity <= 10`.
:::

## Totals, counts, maximum and minimum

Four patterns appear in almost every Paper 2 program that reads data. Learn the shape of each one.

:::key Four loop patterns
- **Running total**: set `Total ← 0` *before* the loop; inside, `Total ← Total + Value`.
- **Count**: set `Count ← 0` before the loop; add 1 each time the item you are counting is met.
- **Average**: `Total / Count`, calculated *after* the loop, and only if `Count` is not zero.
- **Highest and lowest**: start `Highest` and `Lowest` with the *first* value, not 0, then replace when a new value is higher or lower.
:::

The next program reads daily rainfall figures in millimetres until the sentinel −1 is typed. It reads the first value before the loop (a **priming read**) so that the WHILE test has something to look at, and it handles the case where there is no data at all.

:::def Sentinel value
A special value, outside the range of valid data, that is entered to show that the data has ended.
:::

```pseudocode
INPUT Rain
IF Rain = -1 THEN
   OUTPUT "No readings"
ELSE
   Total ← 0
   Count ← 0
   Highest ← Rain
   Lowest ← Rain
   WHILE Rain <> -1
      Total ← Total + Rain
      Count ← Count + 1
      IF Rain > Highest THEN
         Highest ← Rain
      ENDIF
      IF Rain < Lowest THEN
         Lowest ← Rain
      ENDIF
      INPUT Rain
   ENDWHILE
   OUTPUT "Readings: ", Count
   OUTPUT "Mean: ", Total / Count
   OUTPUT "Highest: ", Highest
   OUTPUT "Lowest: ", Lowest
ENDIF
```

The first value starts both `Highest` and `Lowest`. If both started at 0, the lowest would wrongly stay 0 for data such as 12, 7, 20 and 3, because no reading is below 0. The sentinel is never added or counted, because the WHILE test fails before the body runs. Here is the program in Python, with the typed values 12, 7, 20, 3 and −1:

```python
rain = int(input("Rainfall in mm (-1 to finish): "))
if rain == -1:
    print("No readings")
else:
    total = 0
    count = 0
    highest = rain
    lowest = rain
    while rain != -1:
        total = total + rain
        count = count + 1
        if rain > highest:
            highest = rain
        if rain < lowest:
            lowest = rain
        rain = int(input("Rainfall in mm (-1 to finish): "))
    print("Readings:", count)
    print("Mean:", total / count)
    print("Highest:", highest)
    print("Lowest:", lowest)
```

Output, when the user types 12, 7, 20, 3 and -1:

```output
Rainfall in mm (-1 to finish): 12
Rainfall in mm (-1 to finish): 7
Rainfall in mm (-1 to finish): 20
Rainfall in mm (-1 to finish): 3
Rainfall in mm (-1 to finish): -1
Readings: 4
Mean: 10.5
Highest: 20
Lowest: 3
```

The total is \(12 + 7 + 20 + 3 = 42\) and the mean is \(42 \div 4 = 10.5\).

## Nested loops

A loop inside a loop is a **nested loop**. For each pass of the outer loop, the inner loop runs completely. A times-table grid needs one: the outer loop picks the row and the inner loop picks the column.

```pseudocode
FOR Row ← 1 TO 3
   Line ← ""
   FOR Column ← 1 TO 4
      Line ← Line & NUM_TO_STR(Row * Column) & " "
   NEXT Column
   OUTPUT Line
NEXT Row
```

The inner loop builds one line of text, and the `OUTPUT` after it prints the finished line, once per row. The inner statement runs \(3 \times 4 = 12\) times. In Python, `end=" "` stops `print` starting a new line, and a bare `print()` ends the row:

```python
for row in range(1, 4):
    for column in range(1, 5):
        print(row * column, end=" ")
    print()
```

Output:

```output
1 2 3 4 
2 4 6 8 
3 6 9 12 
```

:::warn The reset belongs inside the outer loop
Any variable that collects a result for one row (the `Line` above, or a row total) must be set back to its starting value **inside** the outer loop, before the inner loop. Set it before the outer loop and the second row carries on from the first.
:::

## Working with strings

A string is a sequence of characters, and the insert functions let you look at one character at a time. The loop pattern is always the same: a FOR loop from 1 to `LENGTH` of the string, and `MID(Word, Position, 1)` for the character at each position.

The program below counts the vowels in a word, assuming the word is typed in lower case. Step through it with the three words in the tool: "rhythm" has none.

```pseudocode
INPUT Word
Vowels ← 0
FOR Position ← 1 TO LENGTH(Word)
   Letter ← MID(Word, Position, 1)
   IF Letter = 'a' OR Letter = 'e' OR Letter = 'i' OR Letter = 'o' OR Letter = 'u' THEN
      Vowels ← Vowels + 1
   ENDIF
NEXT Position
OUTPUT Word, " has ", Vowels, " vowels"
```

:::html
<div class="widget" data-w="cs-trace" data-prog="vowels"></div>
:::

To count capitals too, change the line that finds the letter to `Letter ← TO_LOWER(MID(Word, Position, 1))`. String comparison is case sensitive: `'A'` and `'a'` are different characters. In Python, a string can be looped over directly, which is shorter than indexing:

```python
word = input("Word: ")
vowels = 0
for letter in word.lower():
    if letter in "aeiou":
        vowels = vowels + 1
print(word, "has", vowels, "vowels")
```

Output, when the user types Education:

```output
Word: Education
Education has 5 vowels
```

### Building a new string

To reverse a word, count the positions **down** from the end and join each character on to a new string, starting with the empty string.

```pseudocode
INPUT Word
Reversed ← ""
FOR Position ← LENGTH(Word) TO 1 STEP -1
   Reversed ← Reversed & MID(Word, Position, 1)
NEXT Position
OUTPUT Reversed
```

For "stressed" the output is "desserts". In Python, `word[position - 1]` is the character at pseudocode position `position`:

```python
word = "stressed"
reversed_word = ""
for position in range(len(word), 0, -1):
    reversed_word = reversed_word + word[position - 1]
print(reversed_word)
```

Output:

```output
desserts
```

(Python can also reverse a string with the slice `word[::-1]`, but in Paper 2 you must show the loop.)

### Validating a code

A student code is two capital letters followed by four digits, such as AB1234. The check has three parts: the length, the first two characters and the last four. A BOOLEAN flag starts as TRUE and is set to FALSE by any test that fails.

```pseudocode
INPUT Code
Valid ← TRUE
IF LENGTH(Code) <> 6 THEN
   Valid ← FALSE
ELSE
   FOR Position ← 1 TO 2
      Letter ← MID(Code, Position, 1)
      IF Letter < 'A' OR Letter > 'Z' THEN
         Valid ← FALSE
      ENDIF
   NEXT Position
   FOR Position ← 3 TO 6
      IF NOT IS_NUM(MID(Code, Position, 1)) THEN
         Valid ← FALSE
      ENDIF
   NEXT Position
ENDIF
IF Valid THEN
   OUTPUT "Valid"
ELSE
   OUTPUT "Invalid"
ENDIF
```

The length test comes first, because asking for the 6th character of a shorter code would be an error. The comparison `Letter < 'A' OR Letter > 'Z'` works because the capital letters have consecutive character codes. Here is the same check in Python, run on four codes:

```python
for code in ["AB1234", "ab1234", "AB123", "A1B234"]:
    valid = True
    if len(code) != 6:
        valid = False
    else:
        for position in range(1, 3):
            letter = code[position - 1]
            if letter < "A" or letter > "Z":
                valid = False
        for position in range(3, 7):
            if not code[position - 1].isdigit():
                valid = False
    print(code, "Valid" if valid else "Invalid")
```

Output:

```output
AB1234 Valid
ab1234 Invalid
AB123 Invalid
A1B234 Invalid
```

:::eg Spot the error: a slice one place out
Question: A Python program must output the three characters of `word = "computer"` that the pseudocode `MID(word, 4, 3)` would return. [2 marks]

A student wrote:

```python
word = "computer"
print(word[4:7])
```

The program prints:

```output
ute
```

The student knows that `MID` takes three characters starting at position 4, so the slice has three characters [B1]. **But Python numbers positions from 0, so position 4 is `word[3]`; `word[4:7]` starts one character too late and prints `ute`, not `put`. The start mark is lost** [B0]. The answer scores 1 out of 2. The correct slice is `word[3:6]`, which prints `put`. The translation to remember is `s[x - 1:x - 1 + n]`.
:::

## Writing efficient pseudocode

Paper 2 often says "write **efficient** pseudocode". An efficient algorithm gives the right answer with as few steps as it reasonably can, and a short, clear program counts as efficient too.

:::key Efficient pseudocode
- **Stop early.** If the answer is known part-way through, leave the loop. Use a `WHILE` or `REPEAT` loop with a Found flag instead of a FOR loop that always runs to the end.
- **Do not repeat work in a loop.** A value that does not change (`MaxMark * 0.4`) is worked out once, before the loop.
- **Do not repeat a test.** Use `ELSE` or a chain of ELSE branches, not a second IF with the opposite condition.
- **Use the right construct.** CASE for several exact values; one loop where a nested pair is not needed; no variables that are set and never used.
:::

:::eg Writing efficient pseudocode
A program reads a word and must output whether it contains the letter 'z'. [4 marks]

An inefficient answer reads every letter, even after a 'z' has been found:

```pseudocode
INPUT Word
Found ← FALSE
FOR Position ← 1 TO LENGTH(Word)
   IF MID(Word, Position, 1) = 'z' THEN
      Found ← TRUE
   ENDIF
NEXT Position
```

For the word "buzz" this makes 4 comparisons, though the answer is known after 3. An efficient answer uses a condition-controlled loop that stops at the first 'z':

```pseudocode
INPUT Word
Found ← FALSE
Position ← 1
WHILE NOT Found AND Position <= LENGTH(Word)
   IF MID(Word, Position, 1) = 'z' THEN
      Found ← TRUE
   ELSE
      Position ← Position + 1
   ENDIF
ENDWHILE
IF Found THEN
   OUTPUT "Contains z"
ELSE
   OUTPUT "No z"
ENDIF
```

- a flag set to FALSE before the loop and a position that starts at 1 [B1]
- a loop that ends when the letter is found **or** the end of the word is reached [B1]
- compares `MID(Word, Position, 1)` with 'z' and increases Position only when it is not found [B1]
- outputs the result after the loop [B1]

For "zebra" the efficient version makes 1 comparison and the first version 5; for "buzz" it makes 3 and the first version 4. For a word with no 'z' both make one comparison per letter, so the improvement is for the cases that finish early.
:::

Hoisting a constant calculation out of a loop is the other common improvement:

```pseudocode
FOR Count ← 1 TO 20
   INPUT Mark
   IF Mark >= MaxMark * 0.4 THEN
      Passes ← Passes + 1
   ENDIF
NEXT Count
```

This works out `MaxMark * 0.4` twenty times for the same answer. Calculate it once, before the loop, with `PassMark ← MaxMark * 0.4`, and compare with `Mark >= PassMark`.

## Python and pseudocode side by side

| Idea | Pseudocode | Python |
|---|---|---|
| assignment | `Total ← Total + 1` | `total = total + 1` |
| constant | `CONSTANT Rate = 0.2` | `RATE = 0.2` (by convention) |
| input | `INPUT Age` | `age = int(input("Age: "))` |
| output | `OUTPUT "Total: ", Total` | `print("Total:", total)` |
| IF | `IF … THEN … ELSE … ENDIF` | `if …:` … `else:` (indentation) |
| nested IF in ELSE | `ELSE` then `IF` … `ENDIF` | `elif …:` |
| CASE | `CASE OF … ENDCASE` | `if … elif … else` |
| count-controlled | `FOR I ← 1 TO 5` | `for i in range(1, 6):` |
| pre-condition | `WHILE cond` … `ENDWHILE` | `while cond:` |
| post-condition | `REPEAT` … `UNTIL cond` | `while True:` … `if cond: break` |
| string character | `MID(S, p, 1)` | `s[p - 1]` |
| length | `LENGTH(S)` | `len(s)` |
| whole division, remainder | `DIV`, `MOD` | `//`, `%` |

:::tip Python is the language of Paper 4, pseudocode of Paper 2
In Paper 2 you write pseudocode on paper, and Python is not accepted. In Paper 4 you write Python on a computer, but the algorithm in your head is the same. Practise writing each exercise in both.
:::

:::try Start easy, finish at exam standard
Q: Declare a variable `Score` that holds a whole number and a constant `MaxScore` with the value 50.
A: `DECLARE Score : INTEGER` and `CONSTANT MaxScore = 50`. The constant uses `=` and a literal.
Q: Work out `29 MOD 6`, `29 DIV 6`, `2 + 3 * 4` and `(2 + 3) * 4`.
A: 5, 4, 14 and 20. Multiplication comes before addition, and brackets change the order.
Q: What does `INT(RAND(10))` return? Give the smallest and largest possible values.
A: A whole number from 0 to 9. `RAND(10)` is at least 0 and below 10, so `INT` of it is 0 up to 9.
Q: What is `MID("Kampala", 2, 3)`? Write the Python slice that gives the same characters.
A: "amp". The Python slice is `"Kampala"[1:4]`, that is `s[x - 1:x - 1 + n]` with x = 2 and n = 3.
Q: How many times does each body run? (a) `FOR I ← 3 TO 9 STEP 2` (b) `FOR I ← 5 TO 1` (c) `WHILE FALSE` (d) `REPEAT … UNTIL TRUE`
A: (a) 4 times (I is 3, 5, 7, 9). (b) 0 times, because the start is past the end for a positive step. (c) 0 times. (d) once.
Q: Write a condition that is TRUE when `Letter` is a capital letter.
A: `Letter >= 'A' AND Letter <= 'Z'`
Q: What is output? `Count ← 0`, then `FOR I ← 1 TO 10 STEP 3`, `Count ← Count + I`, `NEXT I`, then `OUTPUT Count`.
A: I takes the values 1, 4, 7 and 10, so Count is \(1 + 4 + 7 + 10 = 22\).
Q: Which statement is wrong? (a) `Total ← 0` (b) `Total = 0` used to set Total (c) `IF Total = 0 THEN`
A: (b). In pseudocode an assignment uses `←`. The `=` in (c) is a comparison and is correct.
Q: A program must repeat until the user types the word "stop". Which loop, and what is its condition?
A: `REPEAT … UNTIL Command = "stop"`, because the user must be asked at least once. (A WHILE loop would use `Command <> "stop"`.)
Q: Write pseudocode that outputs the digits of a three-digit number `N`, one per line (for example 482 gives 4, 8, 2).
A: Take the digits apart with DIV and MOD.

```pseudocode
OUTPUT N DIV 100
OUTPUT (N DIV 10) MOD 10
OUTPUT N MOD 10
```

For 482: \(482 \div 100 = 4\); \(48 \bmod 10 = 8\); \(482 \bmod 10 = 2\).
Q: Write pseudocode to output the numbers 1 to 20 that are multiples of 3.
A: Test each number with MOD.

```pseudocode
FOR Number ← 1 TO 20
   IF Number MOD 3 = 0 THEN
      OUTPUT Number
   ENDIF
NEXT Number
```

It outputs 3, 6, 9, 12, 15 and 18.
Q: What is wrong with `CONSTANT Tax = Price * 0.2`?
A: A constant must be set to a literal value. `Price * 0.2` is an expression that uses a variable, so it cannot be a constant.
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ Give the value of each expression. (a) `29 MOD 6` (b) `29 DIV 6` (c) `(2 + 3 * 4) MOD 5` (d) `TO_UPPER(LEFT("kampala", 3))` (e) `(5 > 3) AND NOT (2 > 4)`
H: In (c), work out the brackets first, with multiplication before addition, then apply `MOD`.
A: Working each one:

- (a) 5 [B1]
- (b) 4 [B1]
- (c) 4: `3 * 4` is 12, then \(2 + 12 = 14\), then `14 MOD 5` is 4 [B1]
- (d) "KAM" [B1]
- (e) TRUE: `5 > 3` is TRUE, `2 > 4` is FALSE so its NOT is TRUE, and TRUE AND TRUE is TRUE [B1]

Q: [3 marks] ★ This WHILE loop outputs numbers. Rewrite it as a REPEAT … UNTIL loop that produces the same output.

```pseudocode
Number ← 1
WHILE Number <= 50
   OUTPUT Number
   Number ← Number * 2
ENDWHILE
```

H: Negate the condition: `<=` becomes `>`.
A: The loop outputs 1, 2, 4, 8, 16 and 32. The REPEAT version:

```pseudocode
Number ← 1
REPEAT
   OUTPUT Number
   Number ← Number * 2
UNTIL Number > 50
```

- `Number ← 1` before the loop and the loop starts with REPEAT [B1]
- the same two statements in the body [B1]
- `UNTIL Number > 50`, the negation of the WHILE condition [B1]

Q: [4 marks] ★ For each task, name the most suitable loop and justify your choice. (a) Reading marks until the user types -1, when there might be no marks at all. (b) Outputting the squares of the numbers from 1 to 25.
A: Two marks per part:

- (a) WHILE [B1], because the first value might be the sentinel, so the body may need to run zero times [B1]
- (b) FOR [B1], because the number of repetitions (25) is known in advance [B1]

Q: [6 marks] ★★ A train station in Lagos gives each type of ticket a code. Write pseudocode that inputs a code (a single character) and outputs the fare using a CASE statement: 'S' is 600 (single), 'R' is 1000 (return) and 'W' is 3500 (weekly pass). For any other character output "Unknown ticket". Do not use IF.
H: The values are characters, so they go in single quotes.
A: One possible answer:

```pseudocode
INPUT Code
CASE OF Code
   'S' : OUTPUT 600
   'R' : OUTPUT 1000
   'W' : OUTPUT 3500
   OTHERWISE : OUTPUT "Unknown ticket"
ENDCASE
```

- `INPUT Code` before the CASE [B1]
- `CASE OF Code` and `ENDCASE` [B1]
- 'S' with 600 [B1]
- 'R' with 1000 [B1]
- 'W' with 3500 [B1]
- OTHERWISE with the message "Unknown ticket" [B1]

(Characters in single quotes. Accept the fare stored in a variable and output after the ENDCASE.)

Q: [6 marks] ★★ Write pseudocode that inputs a sentence, then outputs the number of spaces in it and the number of words, assuming that words are separated by single spaces and the sentence does not start or end with a space.
H: The number of words is one more than the number of spaces.
A: One possible answer:

```pseudocode
INPUT Sentence
Spaces ← 0
FOR Position ← 1 TO LENGTH(Sentence)
   IF MID(Sentence, Position, 1) = " " THEN
      Spaces ← Spaces + 1
   ENDIF
NEXT Position
OUTPUT "Spaces: ", Spaces
OUTPUT "Words: ", Spaces + 1
```

- `INPUT Sentence` and `Spaces ← 0` before the loop [B1]
- a FOR loop from 1 to `LENGTH(Sentence)` [B1]
- extracts one character each time with `MID(Sentence, Position, 1)` [B1]
- compares it with a space and adds 1 to the count [B1]
- outputs the number of spaces after the loop [B1]
- outputs words as spaces + 1 [B1]

For "the quick brown fox" there are 3 spaces and 4 words.

Q: [6 marks] ★★ Complete the trace table for this pseudocode. Use the columns Outer, Inner, Total and OUTPUT.

```pseudocode
Total ← 0
FOR Outer ← 1 TO 3
   FOR Inner ← 1 TO Outer
      Total ← Total + Inner
   NEXT Inner
NEXT Outer
OUTPUT Total
```

H: The inner loop runs from 1 to the *current* value of Outer, so it runs 1, then 2, then 3 times.
A: One row for each change:

| Outer | Inner | Total | OUTPUT |
|---|---|---|---|
| | | 0 | |
| 1 | 1 | 1 | |
| 2 | 1 | 2 | |
| | 2 | 4 | |
| 3 | 1 | 5 | |
| | 2 | 7 | |
| | 3 | 10 | |
| | | | 10 |

- Total starts at 0 [B1]
- Outer takes the values 1, 2, 3 [B1]
- the inner loop runs once for Outer = 1, twice for Outer = 2 and three times for Outer = 3 [B1]
- Total after each addition: 1, 2, 4, 5, 7, 10 [B1]
- Inner restarts at 1 for each value of Outer [B1]
- the output 10 at the end [B1]

(Rows may be split differently, as long as every value appears in the correct order in its column.)

Q: [6 marks] ★★ A locker code is one letter from A to F followed by exactly three digits, such as C482. Write pseudocode that inputs a code and outputs "Valid" if it follows these rules, or "Invalid" if not.
H: Test the length first. Use a flag that starts TRUE.
A: One possible answer:

```pseudocode
INPUT Code
Valid ← TRUE
IF LENGTH(Code) <> 4 THEN
   Valid ← FALSE
ELSE
   Letter ← LEFT(Code, 1)
   IF Letter < 'A' OR Letter > 'F' THEN
      Valid ← FALSE
   ENDIF
   FOR Position ← 2 TO 4
      IF NOT IS_NUM(MID(Code, Position, 1)) THEN
         Valid ← FALSE
      ENDIF
   NEXT Position
ENDIF
IF Valid THEN
   OUTPUT "Valid"
ELSE
   OUTPUT "Invalid"
ENDIF
```

- `INPUT Code` and a flag set TRUE (or equivalent) [B1]
- a length test `LENGTH(Code) <> 4` that makes the code invalid [B1]
- the first character extracted (`LEFT` or `MID`) [B1]
- the first character tested between 'A' and 'F' [B1]
- the last three characters each tested with `IS_NUM` in a loop [B1]
- "Valid" or "Invalid" output after the tests [B1]

Q: [8 marks] ★★★ A teacher in Accra types in test marks out of 100, ending with the sentinel 999. A mark outside 0 to 100 is ignored with the message "Ignored". Write pseudocode that outputs the number of valid marks, the mean of the valid marks and the highest valid mark. If there are no valid marks, output "No valid marks" instead.
H: Use a priming read before a WHILE loop, and test for validity *inside* the loop.
H: The highest should start at 0, because every valid mark is 0 or more.
A: One possible answer:

```pseudocode
Count ← 0
Total ← 0
Highest ← 0
INPUT Mark
WHILE Mark <> 999
   IF Mark >= 0 AND Mark <= 100 THEN
      Count ← Count + 1
      Total ← Total + Mark
      IF Mark > Highest THEN
         Highest ← Mark
      ENDIF
   ELSE
      OUTPUT "Ignored"
   ENDIF
   INPUT Mark
ENDWHILE
IF Count = 0 THEN
   OUTPUT "No valid marks"
ELSE
   OUTPUT "Valid marks: ", Count
   OUTPUT "Mean: ", Total / Count
   OUTPUT "Highest: ", Highest
ENDIF
```

- Count, Total and Highest initialised before the loop [B1]
- the first mark read before the loop [B1]
- a WHILE loop that ends on the sentinel 999 [B1]
- a validity test `Mark >= 0 AND Mark <= 100` [B1]
- valid marks counted and added to the total [B1]
- the highest updated with a comparison; "Ignored" output for the others; the next mark read at the end of the loop [B1]
- a test for `Count = 0` before the mean is calculated [B1]
- count, mean and highest output [B1]

For the typed values 45, 120, 80, 62, −5, 100 and 999, the marks 120 and −5 are ignored. The count is 4, the total is 287, the mean is 71.75 and the highest is 100.
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A palindromic number reads the same forwards and backwards, such as 1331. Write pseudocode that inputs a positive whole number and outputs "Palindrome" or "Not a palindrome", using only `DIV`, `MOD`, arithmetic and a loop. Do not convert the number to a string.
H: Build the reversed number one digit at a time: take the last digit with `MOD 10`, shift the reversed number left with `* 10`, add the digit, and remove the digit from the original with `DIV 10`.
H: Remember the original number before the loop destroys it.
A:

```pseudocode
INPUT Number
Original ← Number
Reversed ← 0
WHILE Number > 0
   Digit ← Number MOD 10
   Reversed ← Reversed * 10 + Digit
   Number ← Number DIV 10
ENDWHILE
IF Reversed = Original THEN
   OUTPUT "Palindrome"
ELSE
   OUTPUT "Not a palindrome"
ENDIF
```

- the original number saved before the loop [B1]
- Reversed starts at 0 [B1]
- a loop that runs while Number is more than 0 [B1]
- the last digit taken with `MOD 10` and added to `Reversed * 10` [B1]
- the last digit removed with `DIV 10` [B1]
- compares Reversed with the saved original and outputs the correct message [B1]

For 1331: Reversed becomes 1, 13, 133 and 1331, which equals the original. For 1234 it becomes 4, 43, 432 and 4321, which does not.

Q: [8 marks] ★★★ A number greater than 1 is prime if no whole number from 2 up to the number minus 1 divides it. A faster test checks divisors only while `Divisor * Divisor <= Number` and stops at the first divisor found. Write pseudocode that inputs a whole number of at least 2 and outputs "Prime" or "Not prime" using this test. State how many divisors your loop tests for 97 and for 91.
H: If a number has a divisor larger than its square root, it also has one smaller, so the loop can stop when the square of the divisor passes the number.
H: Use a WHILE loop with a flag, as in the efficient search earlier in this chapter.
A:

```pseudocode
INPUT Number
IsPrime ← TRUE
Divisor ← 2
WHILE IsPrime AND Divisor * Divisor <= Number
   IF Number MOD Divisor = 0 THEN
      IsPrime ← FALSE
   ELSE
      Divisor ← Divisor + 1
   ENDIF
ENDWHILE
IF IsPrime THEN
   OUTPUT "Prime"
ELSE
   OUTPUT "Not prime"
ENDIF
```

- a flag `IsPrime` that starts TRUE [B1]
- Divisor starts at 2 [B1]
- a WHILE loop that ends when the flag is FALSE **or** `Divisor * Divisor` exceeds the number [B1]
- tests `Number MOD Divisor = 0` [B1]
- sets the flag FALSE when a divisor is found [B1]
- increases Divisor only when it is not a factor [B1]
- the correct output after the loop [B1]
- 97 tests the divisors 2 to 9, which is 8 divisors, because \(10 \times 10 = 100\) is more than 97; 91 tests 2 to 7, which is 6 divisors, and stops at 7 because \(91 = 7 \times 13\) [B1]

(97 is prime, 91 is not. Testing every number up to 96 would take 95 divisions for 97.)
:::

:::quiz
? What is the value of `17 / 5` in pseudocode?
- 3
- 2
+ 3.4
- 3.0
> `/` always gives a REAL result, so 17 / 5 is 3.4. The whole number 3 is `17 DIV 5`, and 2 is `17 MOD 5`.
? Which statement about `REPEAT … UNTIL Answer = "yes"` is true?
- It repeats while Answer is "yes".
- Its body might not run at all.
+ It repeats until Answer is "yes", and the body always runs at least once.
- It tests the condition before the first pass.
> UNTIL stops the loop when its condition is TRUE, and the test comes after the body. The first two statements describe a WHILE loop.
? What does `MID("computer", 2, 3)` return?
- "com"
- "mpu"
+ "omp"
- "co"
> Position 2 is the letter o, and three characters from there are o, m, p. The answer "mpu" starts one character too late, which is the mistake of using the Python index (1) as a position.
? How many times does the body of `FOR I ← 10 TO 1 STEP -3` run?
- 3
+ 4
- 9
- 0
> I takes the values 10, 7, 4 and 1. The next value, −2, is past the end value 1.
? In a CASE statement, what is the OTHERWISE branch for?
- It runs after every case.
+ It runs when none of the listed values matches.
- It runs when the first case matches.
- It stops the program.
> OTHERWISE is the catch-all, where an invalid value is reported. Only the first matching case runs, and OTHERWISE runs only if none matched.
? A program uses `Highest ← 0` before reading temperatures, then updates Highest from the data. For which data is the answer wrong?
- 12, 18, 25
- 5, 5, 5
+ -8, -3, -15
- 30, 28
> The true highest of −8, −3 and −15 is −3, but nothing is greater than the starting value 0, so the program wrongly reports 0. Start with the first value instead.
? Which is a legal constant declaration in pseudocode?
- `CONSTANT Double = Rate * 2`
- `CONSTANT Pi ← 3.14`
+ `CONSTANT Pi = 3.14`
- `DECLARE Pi = 3.14`
> A constant uses `=` with a literal value. An expression using another identifier is not a literal, and `←` is for assignment.
? What does `INT(9.99)` return?
- 10
+ 9
- 9.9
- 9.99
> INT keeps the whole-number part and drops the rest. It does not round.
? Why is a WHILE loop usually chosen for "read values until the sentinel -1"?
- WHILE loops are always faster.
+ There might be no data, so the body may need to run zero times.
- A FOR loop cannot read input.
- REPEAT loops cannot use a sentinel.
> A WHILE loop tests before the body, so if the first value typed is the sentinel the loop is skipped. REPEAT would run its body once and treat the sentinel as data.
:::

:::checklist What you can now do
- [ ] I can declare variables and constants in pseudocode and use assignment correctly, including the rule that a constant is set to a literal.
- [ ] I can write and evaluate arithmetic expressions with `+ - * / DIV MOD`, with the correct order of operations.
- [ ] I can write Boolean expressions with comparisons, AND, OR and NOT.
- [ ] I can write INPUT and OUTPUT statements, including OUTPUT with several values, and the Python equivalents.
- [ ] I can use the insert functions (LEFT, RIGHT, MID, LENGTH, TO_UPPER, TO_LOWER, NUM_TO_STR, STR_TO_NUM, IS_NUM, ASC, CHR, INT, RAND and the date functions) and give their Python equivalents.
- [ ] I can write IF with ELSE, nested IF and CASE (with values, ranges and OTHERWISE).
- [ ] I can write FOR (with STEP), WHILE and REPEAT loops, and translate each into Python.
- [ ] I can choose the most suitable loop and justify the choice, and rewrite a WHILE loop as a REPEAT loop.
- [ ] I can validate input with a loop, and write running totals, counts, averages, maximum and minimum, and sentinel-controlled loops.
- [ ] I can process strings character by character with MID and LENGTH, and write nested loops.
- [ ] I can write efficient pseudocode: stopping early, not repeating work and not repeating tests.
:::

:::recap
- A **variable** stores a changing value and a **constant** a fixed one. `DECLARE X : TYPE`; `CONSTANT Rate = 0.2` uses `=` and a literal. An assignment evaluates the right side first.
- `/` always gives a REAL. `DIV` is the whole-number quotient and `MOD` the remainder: they split a quantity into units, find digits and test for even or odd.
- Brackets first, then `*` and `/`, then `+ -`; treat `DIV` and `MOD` like division and bracket them. `=` compares in conditions; `←` assigns. Use brackets when mixing AND and OR.
- `MID(S, x, n)` counts positions from 1; Python slices from 0: `s[x - 1:x - 1 + n]`. `INT` drops the fraction. `RAND(x)` is 0 up to but not including x.
- CASE compares one variable with values or ranges, runs the first match and has an OTHERWISE branch. Test the most restrictive condition first in a chain of IFs.
- **FOR** for a known number of repeats (zero times if the start is past the end; never change the loop variable). **WHILE** may run zero times and continues while the condition is TRUE. **REPEAT … UNTIL** runs at least once and stops when the condition is TRUE.
- Validation: REPEAT until the input is valid, with the error message under the *invalid* condition. A sentinel ends data entry and is never counted; read the first value before the WHILE loop.
- Totals start at 0; highest and lowest start with the first value; divide by the count only when it is not zero.
- In a nested loop the inner loop runs fully for each pass of the outer one; reset row totals inside the outer loop.
- Efficient pseudocode stops early, does constant work once before the loop and does not repeat tests.
:::

:::links
- practise: [Programming basics: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/programming-basics/exam-questions/) · Save My Exams · 9618-style questions on variables, operators and functions [paid]
- practise: [Constructs: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/constructs/exam-questions/) · Save My Exams · IF, CASE and loop questions with mark schemes [paid]
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run the Python programs in this chapter line by line and watch every variable
- read: [Python control flow](https://docs.python.org/3/tutorial/controlflow.html) · Python.org · the official tutorial on if, for, while and range
- read: [Python strings](https://www.w3schools.com/python/python_strings.asp) · W3Schools · slicing and string methods with try-it boxes
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · the official rules for the pseudocode you must write

Links checked 13 November 2026.
:::

Next: [Data types, records and arrays](#cs.datatypes)
