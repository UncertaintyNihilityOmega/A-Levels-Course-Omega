@chapter cs.f.basics
@title Programming from zero: Python and pseudocode
@level pre
@time 6–8 hours
@summary You have never programmed? Start here. You will learn what a program is, then write and run your first programs in two languages side by side: Python, which Paper 4 uses, and Cambridge pseudocode, which Paper 2 uses. You will cover output, variables, data types, arithmetic, input, conditions, selection, loops, strings, errors and trace tables.

:::why
Every programming question in Cambridge Computer Science, in Paper 2 on paper and in Paper 4 on a computer, is built from the same few ideas: store values, calculate with them, make decisions and repeat steps. If you can do those five things in both pseudocode and Python, you can learn the rest of the course. This chapter teaches them slowly, from nothing, and every program in it was run to check its output.
:::

**Before you start**, you need nothing except the arithmetic you learned at school. This chapter is the first programming chapter of the course. The next programming chapters, [Computational thinking and algorithms](#cs.algorithms) and [Programming basics: variables, selection and loops](#cs.programming), take the same ideas to full exam depth.

:::try Warm-up
Q: What is the remainder when 29 is divided by 6? (GCSE)
A: \(29 = 4 \times 6 + 5\), so the remainder is 5.
Q: Follow these steps. Start with 5. Double it. Subtract 3. Then repeat the last two steps once more. What number do you finish with? (GCSE)
A: \(5 \to 10 \to 7\), then \(7 \to 14 \to 11\). You finish with 11.
Q: True or false: "A number qualifies if it is greater than 10 AND less than 20." The number 25 qualifies. (GCSE)
A: False. 25 is greater than 10 but not less than 20, and AND needs both parts to be true.
:::

:::note How code appears in this course
Two languages appear side by side. **Cambridge pseudocode** follows the Pseudocode Guide for 2027–2029: keywords in capitals, `←` for assignment, three-space indents. **Python** is Python 3. The sentence before every code block says which language it is. A block called "Output:" is exactly what the program prints. Where a program asks the user to type, the output shows the typed answer after the question, as a real console does.
:::

## What a program is

A computer does only what it is told, one tiny step at a time. The instructions you give it are a **program**. The steps behind the instructions, described exactly, are an **algorithm**.

:::def Program
A set of instructions, written in a programming language, that a computer carries out to complete a task.
:::

:::def Algorithm
A sequence of defined steps that solves a problem or completes a task.
:::

A recipe is a good picture. The recipe (the algorithm) says what to do, in order, with exact amounts. The cook who follows it (the computer) does not think: if the recipe says add a cup of salt, a cup of salt goes in. The program is the recipe written in a language the cook understands.

Almost every program does the same three jobs in the same order: it takes **input**, does some **processing**, and gives **output**. While it works, it keeps values in named boxes called variables, which you meet below.

:::html
<figure class="fig small"><svg viewBox="0 0 330 300" role="img" aria-label="Three stages from top to bottom joined by arrows. INPUT: the user types 15. PROCESS: decide the fare, with two named variable boxes, Age holding 15 and Fare holding 3.00, and an arrow from Age to Fare. OUTPUT: the screen shows Fare: 3.00."><rect class="fm s-acc sw2" x="20" y="10" width="290" height="50"/><text class="tl tc tb" x="165" y="32">INPUT</text><text class="tl tc" x="165" y="50">the user types 15</text><line class="ln" x1="165" y1="60" x2="165" y2="90" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="20" y="90" width="290" height="120"/><text class="tl tc tb" x="165" y="110">PROCESS: decide the fare</text><text class="tl tc" x="90" y="134">Age</text><rect class="f1 s-acc sw2" x="40" y="142" width="100" height="36"/><text class="tl tc" x="90" y="166">15</text><text class="tl tc" x="240" y="134">Fare</text><rect class="f1 s-acc sw2" x="190" y="142" width="100" height="36"/><text class="tl tc" x="240" y="166">3.00</text><line class="ln" x1="144" y1="160" x2="186" y2="160" marker-end="url(#ah)"/><text class="tl tc" x="165" y="198">a variable: a named box for one value</text><line class="ln" x1="165" y1="210" x2="165" y2="240" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="20" y="240" width="290" height="50"/><text class="tl tc tb" x="165" y="262">OUTPUT</text><text class="tl tc" x="165" y="280">the screen shows: Fare: 3.00</text></svg><figcaption>Input, process, output. Between input and output the program keeps values in variables, here Age and Fare.</figcaption></figure>
:::

### Source code, and running it

The text of a program is its **source code**. A program called an **interpreter** reads Python source code and carries out its lines one at a time, from the top, in order. Doing the lines in order is called **sequence**, and it is the simplest of the three building blocks you learn in this chapter. The other two are selection (choosing) and iteration (repeating).

To run Python on your own computer, download Python 3 free from python.org. It comes with IDLE, a simple editor: choose File, New File, type your program, save it with a name ending in `.py`, and press F5 to run it. If you cannot install anything, paste a program into the free Python Tutor page in the links at the end of the chapter and it runs in your browser, one line at a time.

### Why Cambridge uses two languages

**Paper 2** is on paper. You cannot run a program on paper and the examiners do not want you to learn one language only, so Paper 2 asks you to write **pseudocode**.

:::def Pseudocode
A way of writing an algorithm in structured, language-independent statements. It looks like a program but follows no one programming language's strict rules, so that people can read it and later turn it into code.
:::

Cambridge publishes exact rules for its pseudocode in a Pseudocode Guide, and the exam expects you to follow them. **Paper 4** is on a computer and asks for real code: this course teaches Python for it. A good habit that this chapter builds: write the idea in pseudocode first, then translate it into Python.

## Output: showing something on the screen

The first thing to learn is how to make the computer show a result. In pseudocode the statement is `OUTPUT`; in Python it is `print()`.

In pseudocode:

```pseudocode
OUTPUT "Hello, world"
OUTPUT "Total: ", 42
```

The same in Python:

```python
print("Hello, world")
print("Total:", 42)
print("Total: " + "42")
```

Output:

```output
Hello, world
Total: 42
Total: 42
```

Three things to notice. Text goes inside double quotes, and the quotes are not shown. In pseudocode a comma separates the items to output, and OUTPUT joins them exactly as given, so the space in `"Total: "` is part of the text. In Python a comma also separates items, but `print` puts one space between them, so `print("Total:", 42)` shows `Total: 42` without the space inside the quotes. The third line shows `+`, which joins two pieces of text with nothing added between them.

A piece of text in quotes is a **string**. Python accepts single or double quotes; Cambridge pseudocode uses double quotes for a string, and single quotes only for a single character, which you meet in [Data types, records and arrays](#cs.datatypes). Use double quotes in both languages in this course. If the text contains an apostrophe, double quotes cope: `print("It's here")` shows `It's here`.

A **comment** is a note for human readers that the computer ignores. In Python it starts with `#`; in pseudocode it starts with `//`.

```python
city = "Lima"  # a comment starts at the # sign and runs to the end of the line
print(city)  # Python ignores every comment
```

Output:

```output
Lima
```

A comment can also fill a whole line, starting with `#` at the left. In pseudocode the same comment is `// a note for the reader`. Use comments to say why you do something, not to repeat what the code says.

## Variables and assignment

A program usually needs to remember values: a score, a name, a price. It stores each one in a **variable**.

:::def Variable
A named memory location that stores a value which can change while the program runs.
:::

:::def Assignment
A statement that stores a value in a variable, replacing the value the variable held before.
:::

Think of a variable as a labelled box. The label is the name, and the box holds one value at a time. Putting a new value in throws the old one away. In pseudocode you write an assignment with an arrow, `←`; in Python with an equals sign. In both languages, **the right-hand side is worked out first, then stored in the variable on the left**.

In pseudocode:

```pseudocode
DECLARE Score : INTEGER
DECLARE Name : STRING

Score ← 0
Score ← Score + 10
Score ← Score + 10
Name ← "Amina"
OUTPUT Name, " has ", Score, " points"
```

The same in Python:

```python
score = 0
score = score + 10
score = score + 10
name = "Amina"
print(name, "has", score, "points")
```

Output:

```output
Amina has 20 points
```

The line `Score ← Score + 10` is not an equation. Read it as "take the current value of Score, add 10, and store the result back in Score". The first time it runs, Score changes from 0 to 10; the second time, from 10 to 20.

Pseudocode has a `DECLARE` line that says the name and the data type of each variable before it is used: `DECLARE Score : INTEGER`. Python has no declaration: a variable exists from the moment you assign to it.

:::key Names for variables
- A name is made of letters, digits and underscores, and starts with a letter (Python also allows starting with an underscore). No spaces.
- Choose a name that says what the variable holds: `TotalPrice` or `total_price`, never `x`. Examiners award marks for meaningful names, and you read your own code more easily.
- Cambridge pseudocode style, used in this course: each word starts with a capital (`TotalScore`, `NumberOfPlayers`). Pseudocode names are not case sensitive.
- Python style: lower case with underscores (`total_score`). Python **is** case sensitive: `Score`, `score` and `SCORE` are three different variables, and a wrongly capitalised name is a run-time error.
- A word the language already uses (`IF`, `FOR`, `while`, `print` …) cannot be a variable name.
:::

A **constant** is like a variable that never changes while the program runs, such as a tax rate or the number of days in a week.

:::def Constant
A named value that is set once and cannot change while the program runs.
:::

In pseudocode you write `CONSTANT TaxRate = 0.2`. This is the only place pseudocode uses `=` to give a value, and the value must be a literal such as `0.2` or `"Lima"`, not a calculation. Python has no constants. The usual habit is to write the name in capitals, `TAX_RATE = 0.2`, and promise yourself not to change it.

:::warn Three different equals signs
`←` stores a value in pseudocode. `=` stores a value in Python. But `=` in a pseudocode condition (`IF Score = 10`) **compares** two values, and the Python comparison is written `==`. You meet comparisons below. Writing `←` as `=`, or the other way round, is the most common slip in this chapter.
:::

:::eg Storing and using values (a shop total)
A shop in Accra sells notebooks at 12.50 each. Write a Python program that stores the price, stores the number bought as 3, calculates the total and shows both the price and the total.

Store the two given values, calculate the total from them in a third variable, then show them.

```python
price = 12.50
items = 3
total = price * items
print("Price:", price)
print("Total:", total)
```

Output:

```output
Price: 12.5
Total: 37.5
```

Python shows 12.5, not 12.50: a number stores its value, not the way you typed it. The total is \(12.5 \times 3 = 37.5\). The calculation uses the variables, not the numbers 12.5 and 3, so changing `items` changes the total without changing the line that calculates it.
:::

## Data types at first sight

Every value has a **data type**. The number 7 and the text "7" look alike, but you can multiply the number by 2 and get 14, while "7" repeated twice is "77".

:::def Data type
A classification of data that sets which values a variable can hold, how they are stored and which operations can be performed on them.
:::

Four types are enough for now.

| Pseudocode type | Python type | What it holds | Example values |
|---|---|---|---|
| INTEGER | `int` | a whole number | `42`, `-7`, `0` |
| REAL | `float` | a number that may have a fractional part | `3.0`, `0.75`, `-2.5` |
| STRING | `str` | text: zero or more characters | `"Lima"`, `"7"`, `""` |
| BOOLEAN | `bool` | only TRUE or FALSE | `TRUE` and `FALSE`; in Python `True` and `False` |

Two more types, CHAR (one character) and DATE, are in [Data types, records and arrays](#cs.datatypes). In pseudocode a REAL literal always has at least one digit on both sides of the point, so you write `4.0` and `0.5`, never `4.` or `.5`. Python's `type()` tells you which type a value has.

```python
age = 15
height = 1.72
name = "Lucia"
is_student = True
print(type(age), type(height), type(name), type(is_student))
```

Output:

```output
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>
```

You can convert between types with `int()`, `float()` and `str()`. In pseudocode the matching functions are `INT(x)`, which gives the whole-number part, and `NUM_TO_STR(x)` and `STR_TO_NUM(s)`, which the Paper 2 insert lists.

```python
print(int(3.9), float(4), str(25) + "%", int("17") + 1)
```

Output:

```output
3 4.0 25% 18
```

`int(3.9)` is 3, because `int` cuts off the fractional part; it does not round. `float(4)` is `4.0`. `str(25) + "%"` makes the text `25%`, and `int("17") + 1` turns the text `"17"` into a number before adding.

:::key Choosing a type
Use INTEGER for counts, REAL for measurements and prices, STRING for text, and BOOLEAN for yes/no facts such as `IsStudent`. A telephone number is a STRING, not an INTEGER: you never do arithmetic with it and a leading 0 must be kept.
:::

## Arithmetic

Both languages calculate with the usual operators. Division needs care, because there are two kinds: one that gives the exact quotient as a real number, and one that gives the whole number of times it goes in, with the remainder kept apart.

| Operation | Pseudocode | Python | Example | Result |
|---|---|---|---|---|
| add | `+` | `+` | 17 + 5 | 22 |
| subtract | `-` | `-` | 17 - 5 | 12 |
| multiply | `*` | `*` | 17 * 5 | 85 |
| divide (real result) | `/` | `/` | 17 / 5 | 3.4 |
| whole-number quotient | `DIV` | `//` | 17 DIV 5 | 3 |
| remainder | `MOD` | `%` | 17 MOD 5 | 2 |

```python
print(17 + 5, 17 - 5, 17 * 5)
print(17 / 5, 17 // 5, 17 % 5)
print(20 / 4, 20 // 4)
```

Output:

```output
22 12 85
3.4 3 2
5.0 5
```

The last line shows the rule to remember: `/` **always gives a real number**, even when the answer is whole (`20 / 4` is `5.0`), in pseudocode and in Python. Use DIV or `//` when you want a whole number.

DIV and MOD are not exotic: they undo each other. 17 divided by 5 is 3 whole times with 2 left over, so \(17 = 3 \times 5 + 2\). The remainder tells you a lot:

- `Number MOD 2 = 0` is TRUE when Number is even.
- `Number MOD 10` is the last digit of a whole number, and `Number DIV 10` removes it.
- `Total DIV 60` and `Total MOD 60` turn a number of seconds into whole minutes and seconds left over.

:::eg Seconds to minutes and seconds (exam style)
A swimming club in Nairobi records each swim time in seconds. Write pseudocode that inputs a time in seconds as a whole number, then outputs the whole minutes and the seconds left over. For example, 200 seconds is 3 minutes and 20 seconds. [4 marks]

One minute is 60 seconds, so the whole minutes are the whole-number quotient of the time by 60, and the seconds left over are the remainder.

```pseudocode
DECLARE Seconds, Minutes, Left : INTEGER

INPUT Seconds
Minutes ← Seconds DIV 60
Left ← Seconds MOD 60
OUTPUT Minutes, " minutes ", Left, " seconds"
```

Mark points:

- inputs the time into an integer variable [B1]
- calculates the minutes with `DIV 60` [B1]
- calculates the seconds left over with `MOD 60` [B1]
- outputs both values [B1]

Check with 200: \(200 \div 60\) is 3 with remainder 20, so the output is `3 minutes 20 seconds`.

The same in Python, with 200 typed:

```python
seconds = int(input("Time in seconds: "))
minutes = seconds // 60
left = seconds % 60
print(minutes, "minutes", left, "seconds")
```

Output:

```output
Time in seconds: 200
3 minutes 20 seconds
```
:::

### Which calculation happens first

Both languages follow the order you know from school: brackets first, then `*`, `/`, `DIV` and `MOD`, then `+` and `-`. Operators of the same level work from left to right.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(8 + 6 / 2)
print((8 + 6) / 2)
```

Output:

```output
14
20
11.0
7.0
```

The same numbers give two different answers depending on the brackets. When you mean "add, then divide", the brackets are not optional.

:::warn The mean of two numbers
`A + B / 2` divides only B by 2, then adds A. The mean of A and B is `(A + B) / 2`. This slip appears in real exam scripts every year. If a calculation adds before it multiplies or divides, put brackets round the addition.
:::

## Input: asking the user

A program is more useful when it can ask the user for values. In pseudocode the statement is `INPUT`; in Python it is `input()`, which can show a question first.

```python
name = input("Your name: ")
print("Hello", name)
```

Output, when the user types Amina:

```output
Your name: Amina
Hello Amina
```

**`input()` always gives back a string**, even when the user types digits. That causes the best-known beginner error, because `+` joins strings.

```python
first = input("First number: ")
second = input("Second number: ")
print(first + second)
print(int(first) + int(second))
```

Output, when the user types 3 and then 4:

```output
First number: 3
Second number: 4
34
7
```

The line `print(first + second)` joined the text "3" and the text "4" into "34". The next line turned both into whole numbers with `int()` before adding, and got 7. For a number with a fractional part, use `float(input(…))`.

In pseudocode you write only `INPUT Quantity`, because `DECLARE Quantity : INTEGER` has already told the computer what type to expect. Python has no declaration, so you convert yourself.

In pseudocode:

```pseudocode
DECLARE Price : REAL
DECLARE Quantity : INTEGER

INPUT Price
INPUT Quantity
OUTPUT "Total: ", Price * Quantity
```

The same in Python:

```python
price = float(input("Price of one item: "))
quantity = int(input("How many? "))
print("Total:", price * quantity)
```

Output, when the user types 2.5 and then 4:

```output
Price of one item: 2.5
How many? 4
Total: 10.0
```

:::warn Text that looks like a number
`"3" + "4"` is `"34"`, and `"10" < "9"` is true, because text is compared one character at a time and "1" comes before "9". Convert with `int()` or `float()` before you calculate or compare numbers that came from `input()`.
:::

## Comparisons and Boolean logic

To make a decision, a program first asks a question whose answer is true or false. The answer is a **Boolean** value, the fourth data type above. You make it with a comparison.

| Question | Pseudocode | Python |
|---|---|---|
| equal to | `=` | `==` |
| not equal to | `<>` | `!=` |
| less than, greater than | `<`  `>` | `<`  `>` |
| less than or equal, greater than or equal | `<=`  `>=` | `<=`  `>=` |

You combine questions with three Boolean operators. `A AND B` is true only when both are true. `A OR B` is true when at least one is true. `NOT A` reverses the answer. Python writes them in lower case: `and`, `or`, `not`.

| A | B | A AND B | A OR B | NOT A |
|---|---|---|---|---|
| TRUE | TRUE | TRUE | TRUE | FALSE |
| TRUE | FALSE | FALSE | TRUE | FALSE |
| FALSE | TRUE | FALSE | TRUE | TRUE |
| FALSE | FALSE | FALSE | FALSE | TRUE |

```python
age = 15
print(age > 12, age == 15, age != 15, age <= 14)
print(age > 12 and age < 18)
print(age < 12 or age > 64)
print(not age > 12)
```

Output:

```output
True True False False
True
False
False
```

When you mix operators, NOT is applied first, then AND, then OR. Put brackets round the part you mean, as in `(Age >= 12) AND (Age < 18)`, to make the order clear to the reader and to the examiner. A condition like `12 <= Age < 18` is not pseudocode: write two comparisons joined by AND.

:::key Equals, in four lines
- Pseudocode: `Score ← 5` stores 5; `IF Score = 5` asks whether Score is 5.
- Python: `score = 5` stores 5; `if score == 5:` asks whether score is 5.
:::

## Selection: choosing what to do

**Selection** lets a program choose between actions depending on a condition.

:::def Selection
A construct that chooses which statements to run, depending on whether a condition is true.
:::

In pseudocode an IF statement has THEN, an optional ELSE, and ends with ENDIF. In Python the line ends with a colon and the lines that belong to the IF are **indented**.

In pseudocode:

```pseudocode
IF Age >= 18 THEN
   OUTPUT "Adult"
ELSE
   OUTPUT "Under 18"
ENDIF
```

The same in Python, with `age` set to 15:

```python
age = 15
if age >= 18:
    print("Adult")
else:
    print("Under 18")
```

Output:

```output
Under 18
```

When there are more than two choices, nest one IF inside the ELSE of another. Python has a shorter form for exactly this, `elif` (else if). The program works down the tests and runs the **first** one that is true, then skips the rest.

In pseudocode:

```pseudocode
IF Mark >= 70 THEN
   Result ← "High"
ELSE
   IF Mark >= 40 THEN
      Result ← "Pass"
   ELSE
      Result ← "Retake"
   ENDIF
ENDIF
OUTPUT Mark, " is ", Result
```

The same in Python, with `mark` set to 58:

```python
mark = 58
if mark >= 70:
    result = "High"
elif mark >= 40:
    result = "Pass"
else:
    result = "Retake"
print(mark, "is", result)
```

Output:

```output
58 is Pass
```

The order of the tests matters. 58 is not at least 70, so the first test fails; it is at least 40, so the second succeeds and the rest is skipped. If you tested `Mark >= 40` first, a mark of 85 would be called "Pass", because that test would succeed before the test for "High" was ever reached. Test the narrowest condition first.

:::key Indentation
In Python the indentation is part of the language: it shows which lines belong inside the IF. Use four spaces, the same on every line of one block. In pseudocode ENDIF closes the IF, and the three-space indent is for the reader (the exam expects it). Forgetting the colon or the indent is a syntax error in Python.
:::

Pseudocode also has a CASE statement for choosing between many exact values; it is in [Programming basics: variables, selection and loops](#cs.programming).

:::eg Marking a quiz answer (exam style)
A quiz asks the player "What is 7 times 8?". Write pseudocode that inputs the player's answer, then outputs "Correct" and adds 1 to Score if the answer is 56, otherwise outputs "Wrong". Score already holds the player's score so far. [4 marks]

Input the answer, compare it with 56 using `=` (a comparison, not a store), and choose between the two actions.

```pseudocode
DECLARE Answer : INTEGER

INPUT Answer
IF Answer = 56 THEN
   OUTPUT "Correct"
   Score ← Score + 1
ELSE
   OUTPUT "Wrong"
ENDIF
```

Mark points:

- inputs the answer into a variable [B1]
- IF with the correct comparison `Answer = 56` [B1]
- correct branch outputs "Correct" and adds 1 to Score [B1]
- ELSE branch outputs "Wrong" [B1]

The same in Python, with the player typing 56 and Score starting at 4:

```python
score = 4
answer = int(input("What is 7 times 8? "))
if answer == 56:
    print("Correct")
    score = score + 1
else:
    print("Wrong")
print("Score:", score)
```

Output:

```output
What is 7 times 8? 56
Correct
Score: 5
```
:::

## Iteration: repeating steps

Computers are good at repeating. A group of statements that repeats is a **loop**, and using loops is called **iteration**.

:::def Iteration
A construct that repeats a group of statements, either a set number of times or until a condition changes.
:::

### The FOR loop: a known number of times

When you know how many times to repeat, use a FOR loop. It is a **count-controlled** loop: it counts for you.

In pseudocode:

```pseudocode
FOR Count ← 1 TO 5
   OUTPUT Count
NEXT Count
```

The same in Python:

```python
for count in range(1, 6):
    print(count)
```

Output:

```output
1
2
3
4
5
```

Look closely at `range(1, 6)`. Python's range **stops before** its second number, so `range(1, 6)` gives 1, 2, 3, 4, 5, while the pseudocode `1 TO 5` includes 5. To count 1 to N in Python you write `range(1, N + 1)`. Forgetting the `+ 1` is the most common loop mistake in Python.

You can see what a range makes by turning it into a list, shown in square brackets (lists are in the next programming chapters):

```python
print(list(range(1, 6)))
print(list(range(5)))
print(list(range(2, 11, 2)))
print(list(range(5, 0, -1)))
```

Output:

```output
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4]
[2, 4, 6, 8, 10]
[5, 4, 3, 2, 1]
```

| Pseudocode | Python | Values of the counter |
|---|---|---|
| `FOR C ← 1 TO 5` | `range(1, 6)` | 1, 2, 3, 4, 5 |
| `FOR C ← 2 TO 10 STEP 2` | `range(2, 11, 2)` | 2, 4, 6, 8, 10 |
| `FOR C ← 5 TO 1 STEP -1` | `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

`STEP` is how much the counter goes up each time (the third number in `range`). With only one number, `range(5)` starts at 0. A pseudocode FOR loop whose start is already past its end, such as `FOR C ← 5 TO 1`, runs zero times.

A loop is often used to build a **running total**: a variable that starts at 0 and gets something added each time round.

```python
total = 0
for number in range(1, 6):
    total = total + number
print("Total:", total)
```

Output:

```output
Total: 15
```

### The WHILE loop: while a condition is true

Sometimes you do not know how many repeats there will be: you repeat until something happens. A **condition-controlled** loop tests a condition. The WHILE loop tests it **before** each repeat, so its body can run zero times, and it repeats **while the condition is true**.

In pseudocode:

```pseudocode
Savings ← 100
Years ← 0
WHILE Savings < 1000
   Savings ← Savings * 2
   Years ← Years + 1
ENDWHILE
OUTPUT Years, " ", Savings
```

The same in Python:

```python
savings = 100
years = 0
while savings < 1000:
    savings = savings * 2
    years = years + 1
print(years, savings)
```

Output:

```output
4 1600
```

Savings doubles from 100 until it is no longer below 1000: 200, 400, 800, 1600. That is 4 doublings. A WHILE loop must change something that its condition depends on. If the body never changed `savings`, the condition would stay true forever and the program would never stop. That is an **infinite loop**; press Ctrl+C in Python to stop it.

### The REPEAT … UNTIL loop: at least once

The third loop tests its condition **after** the body, so the body always runs at least once. It repeats **until the condition becomes true**, which is the opposite way round from WHILE. It is the natural loop for "ask until the answer is valid".

In pseudocode:

```pseudocode
REPEAT
   INPUT Number
UNTIL Number > 0
```

Python has no REPEAT keyword. The standard translation is a loop that runs forever, with a `break` that leaves it when the stop condition is true:

```python
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break
print("You entered", number)
```

Output, when the user types -3, then 0, then 7:

```output
Enter a positive number: -3
Enter a positive number: 0
Enter a positive number: 7
You entered 7
```

:::key Choosing a loop
- **FOR**: the number of repeats is known before the loop starts. It counts for you.
- **WHILE**: repeat while a condition is true. The test comes first, so the body may run zero times.
- **REPEAT … UNTIL**: repeat until a condition is true. The test comes last, so the body runs at least once.
- WHILE continues while its condition is TRUE. REPEAT … UNTIL stops when its condition is TRUE. Turning one into the other means reversing the condition.
:::

## Strings: working with text

A string is a sequence of characters, and both languages have tools for it. You will need these four.

| Job | Pseudocode (Paper 2 insert) | Python |
|---|---|---|
| number of characters | `LENGTH(Word)` | `len(word)` |
| join two strings | `First & Last` | `first + last` |
| some characters from the middle | `MID(Word, 2, 3)` | `word[1:4]` |
| convert to capitals | `TO_UPPER(Word)` | `word.upper()` |

`MID(S, x, y)` gives y characters starting at position x, where the first character is position 1. Python counts positions from 0, so the character at pseudocode position 1 is `word[0]`. The slice `word[1:4]` means "from index 1 up to, but not including, index 4": three characters, the same as `MID(Word, 2, 3)`. In general, `MID(S, x, y)` is `s[x - 1 : x - 1 + y]`. The same functions in full, with `LEFT` and `RIGHT`, are in [Programming basics: variables, selection and loops](#cs.programming).

```python
word = "computer"
print(len(word))
print(word[0], word[3])
print(word[1:4])
print(word.upper())
print("Hello, " + "Ana" + "!")
```

Output:

```output
8
c p
omp
COMPUTER
Hello, Ana!
```

The word `computer` has 8 characters. `word[0]` is `c` and `word[3]` is `p` (the fourth character). `word[1:4]` is `omp`, the characters at indexes 1, 2 and 3.

The string joining operator needs strings on both sides. To put a number in a message, convert it with `str()` in Python (`NUM_TO_STR` in pseudocode), or use a comma in `print` and `OUTPUT`, which accepts any types.

```python
age = 15
message = "Age: " + str(age)
print(message)
print(len(message))
```

Output:

```output
Age: 15
7
```

## When programs go wrong: three kinds of error

Programs have mistakes. An error is not a failure: finding and fixing them is most of what a programmer does. There are three kinds, and the exam asks you to name them.

:::def Syntax error
A mistake in the rules of the language, such as a missing colon or bracket, that stops the program being translated, so it does not run at all.
:::

:::def Run-time error
An error that happens while the program is running and makes it stop, such as dividing by zero.
:::

:::def Logic error
A mistake in the design of the program that lets it run but gives wrong results.
:::

| Kind | When it shows | Does the program run? | Example |
|---|---|---|---|
| syntax error | before the program starts | no, Python reports it and runs nothing | a missing colon after `for` |
| run-time error | in the middle of running | it stops at that line | `total / 0`, or `int("abc")` |
| logic error | never reported: you notice the wrong answer | yes, all the way | `A + B / 2` for the mean |

Python tells you about the first two. The message names the type of error and the line number. This program has a syntax error:

```text
for count in range(1, 4)
    print(count)
```

and Python's report is:

```text
  File "loop.py", line 1
    for count in range(1, 4)
                            ^
SyntaxError: expected ':'
```

Here is a run-time error. The program divides by a count that is 0:

```text
total = 120
count = 0
average = total / count
print(average)
```

```text
Traceback (most recent call last):
  File "shop.py", line 3, in <module>
    average = total / count
              ~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

The layout of these reports varies a little between Python versions, but you read them the same way, **from the bottom up**. The last line names the error (`ZeroDivisionError`) and says what is wrong in plain words. The line above shows the code that failed and the line before it says which line number of your file it is (line 3 here). Common run-time errors in this chapter are `ZeroDivisionError`, `ValueError` (for example `int("abc")`, which is not a whole number), `TypeError` (for example `"Total: " + 5`, which adds text and a number) and `NameError` (a variable name that was never given a value, often a spelling mistake).

A logic error gives no message at all, which makes it the hardest to find. This program runs perfectly and prints the wrong answer:

```python
first = 10
second = 20
mean = first + second / 2
print("Mean:", mean)
```

Output:

```output
Mean: 20.0
```

The mean of 10 and 20 is 15. The program divided only `second` by 2 (see the precedence rule above). The tool for finding errors like this is the trace table.

## Trace tables: running a program by hand

In Paper 2 you cannot run a program, so the exam asks you to run one **by hand**: a dry run.

:::def Trace table
A table used to dry-run an algorithm by hand. It has a column for each variable (and one for the output), and a new row each time a value changes.
:::

:::steps
1. Make a column for every variable and one for OUTPUT, in the order the variables first appear.
2. Work through the statements in order, as the computer does, one at a time.
3. Every time a variable gets a new value, write it in that variable's column on a new row. Leave the other cells empty: an empty cell means "no change".
4. When something is output, write it in the OUTPUT column.
5. For a loop, go round it as many times as the condition or the counter says, writing the new values on each repeat.
:::

:::eg Tracing the savings loop
Complete a trace table for the pseudocode in the WHILE section above, the savings loop that starts at 100.

Follow the four statements in order. The condition `Savings < 1000` is tested before each repeat, so the loop runs while Savings is 100, 200, 400 and 800.

| Savings | Years | OUTPUT |
|---|---|---|
| 100 | 0 | |
| 200 | 1 | |
| 400 | 2 | |
| 800 | 3 | |
| 1600 | 4 | |
| | | 4 1600 |

After the fourth repeat Savings is 1600, which is not less than 1000, so the loop ends and the last line outputs `4 1600`. This matches the output that the Python program printed.
:::

Real exam tables often have one more column or a column for the condition. The method does not change: one row per change, in the order the code runs. A trace table that you can fill in correctly shows that you understand the algorithm.

## Putting it together: two complete programs

You now have every tool for two real programs.

### A times-table printer

The program asks which times table the user wants and prints it from 1 to 12.

In pseudocode:

```pseudocode
DECLARE Number, Multiplier : INTEGER

INPUT Number
FOR Multiplier ← 1 TO 12
   OUTPUT Number, " x ", Multiplier, " = ", Number * Multiplier
NEXT Multiplier
```

The same in Python:

```python
number = int(input("Which times table? "))
for multiplier in range(1, 13):
    print(number, "x", multiplier, "=", number * multiplier)
```

Output, when the user types 7:

```output
Which times table? 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84
```

The loop uses `range(1, 13)` because the last value, 12, must be included. The calculation `number * multiplier` is made inside the output statement, which is allowed in both languages.

### A guessing game

The computer holds a secret number and the player keeps guessing until right. It says "Too low" or "Too high" after each guess and counts the guesses. The secret is fixed at 17 for now, so the program is easy to test.

In pseudocode:

```pseudocode
CONSTANT Secret = 17
DECLARE Guess, Guesses : INTEGER

Guesses ← 0
REPEAT
   INPUT Guess
   Guesses ← Guesses + 1
   IF Guess < Secret THEN
      OUTPUT "Too low"
   ELSE
      IF Guess > Secret THEN
         OUTPUT "Too high"
      ENDIF
   ENDIF
UNTIL Guess = Secret
OUTPUT "Correct! You took ", Guesses, " guesses"
```

The same in Python:

```python
secret = 17
guesses = 0
guess = 0
while guess != secret:
    guess = int(input("Guess the number: "))
    guesses = guesses + 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
print("Correct! You took", guesses, "guesses")
```

Output, when the player types 10, then 20, then 17:

```output
Guess the number: 10
Too low
Guess the number: 20
Too high
Guess the number: 17
Correct! You took 3 guesses
```

The Python version uses a WHILE loop whose condition is the opposite of the pseudocode UNTIL: repeat while the guess is not the secret. It gives `guess` a starting value of 0 so that the condition can be tested the first time. The program uses all three building blocks: a sequence of statements, a selection (the IF) and an iteration (the loop).

To make the game different every time, let the computer choose the secret. In Python, `random.randint(1, 100)` gives a random whole number from 1 to 100, including both ends. The pseudocode way is the insert function `RAND`, where `RAND(x)` gives a real number from 0 up to but not including x, so `INT(RAND(100)) + 1` is a whole number from 1 to 100.

```python
import random
secret = random.randint(1, 100)
print("The secret is between 1 and 100:", secret >= 1 and secret <= 100)
```

Output:

```output
The secret is between 1 and 100: True
```

Replace the line `secret = 17` of the guessing game with the first two lines here and the game changes on every run. The line `import random` makes the random library available; a Python program names every library it uses at the top.

:::key Pseudocode and Python side by side
| Idea | Pseudocode | Python |
|---|---|---|
| show | `OUTPUT "Total: ", Total` | `print("Total:", total)` |
| store | `Total ← 0` | `total = 0` |
| ask | `INPUT Age` | `age = int(input())` |
| comment | `// note` | `# note` |
| compare | `=`  `<>` | `==`  `!=` |
| combine | `AND`  `OR`  `NOT` | `and`  `or`  `not` |
| whole division | `DIV`  `MOD` | `//`  `%` |
| choose | `IF … THEN … ELSE … ENDIF` | `if …:` `elif …:` `else:` |
| repeat a known number of times | `FOR I ← 1 TO N … NEXT I` | `for i in range(1, N + 1):` |
| repeat while true | `WHILE … ENDWHILE` | `while …:` |
| repeat until true | `REPEAT … UNTIL` | `while True:` with `break` |
:::

:::eg Spot the error: the mean of two numbers
Question: Write pseudocode to input two numbers and output their mean. [4 marks]

A student wrote:

```pseudocode
01  INPUT A
02  INPUT B
03  Mean ← A + B / 2
04  OUTPUT Mean
```

Line 01 inputs the first number [B1]. Line 02 inputs the second number [B1]. **Line 03 divides only B by 2 and then adds A, because division is done before addition. The calculation mark is lost** [B0]. Line 04 outputs the result [B1]. The answer scores 3 out of 4.

To see the damage, let A be 10 and B be 20. The line calculates \(10 + 20 \div 2 = 10 + 10 = 20\), but the mean is 15. The fix is brackets:

```pseudocode
03  Mean ← (A + B) / 2
```

A quick dry run with two easy numbers catches this slip in seconds.
:::

:::try Start easy, finish at exam standard
Q: What does this pseudocode output? `X ← 6`, then `Y ← X * 2 + 1`, then `OUTPUT Y`.
A: X is 6, so Y is \(6 \times 2 + 1 = 13\). It outputs 13.
Q: State a suitable data type for each of: a person's age in years; the price of a ticket; a person's name; whether a seat is free.
A: INTEGER; REAL (a price has a fractional part); STRING; BOOLEAN (two possible values).
Q: Work out `23 DIV 5` and `23 MOD 5`.
A: 5 goes into 23 four times (20) with 3 left over, so `23 DIV 5` is 4 and `23 MOD 5` is 3.
Q: What does this Python print? `print(7 // 2, 7 % 2, 7 / 2)`
A: `3 1 3.5`. The whole-number quotient is 3, the remainder is 1, and `/` gives the real result 3.5.
Q: What numbers does `for i in range(2, 9, 3):` give to `i`?
A: It starts at 2 and adds 3 each time, stopping before 9: 2, 5, 8.
Q: Write pseudocode that outputs the even numbers from 2 to 20, one per line.
A: Count in steps of 2.

```pseudocode
FOR Number ← 2 TO 20 STEP 2
   OUTPUT Number
NEXT Number
```

Q: A Python program has the line `print("Total: " + 5)`. When it is run, it stops with a `TypeError`. State the kind of error and explain it.
A: A run-time error. The program is written in valid Python, so it starts, but it fails at that line because `+` cannot join a string and an integer. The fix is `print("Total:", 5)` or `str(5)`.
Q: Complete a trace table (columns Count, Total) for `Total ← 0`, then `FOR Count ← 1 TO 4`, `Total ← Total + Count`, `NEXT Count`, then `OUTPUT Total`.
A: Total starts at 0 and gains Count each time.

| Count | Total | OUTPUT |
|---|---|---|
| | 0 | |
| 1 | 1 | |
| 2 | 3 | |
| 3 | 6 | |
| 4 | 10 | |
| | | 10 |

Q: `MID("computer", 4, 3)` is called with the first character at position 1. What does it return?
A: The characters at positions 4, 5 and 6 of c-o-m-p-u-t-e-r are `p`, `u`, `t`, so it returns `"put"`.
Q: What does this Python print? `print(len("Lagos") * 2)`
A: `"Lagos"` has 5 characters, so the output is 10.
Q: A student wants to count from 1 to 10 in Python and writes `for n in range(1, 10):`. What is output, and how is it fixed?
A: It outputs 1 to 9 only, because range stops before its second number. The fix is `range(1, 11)`.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ The following pseudocode is run. The variables have been declared. Write down the three lines that are output.

```pseudocode
A ← 47
Tens ← A DIV 10
Units ← A MOD 10
OUTPUT "Tens: ", Tens
OUTPUT "Units: ", Units
OUTPUT "Quarter: ", A / 4
```

A: `A DIV 10` is 4 and `A MOD 10` is 7. A quarter of 47 is 11.75.

- `Tens: 4` [B1]
- `Units: 7` [B1]
- `Quarter: 11.75` [B1]

Q: [3 marks] ★ Name the kind of error in each of these cases, and say why.

(a) A Python program has the line `print("Hello"` with the closing bracket missing.

(b) A program reads the number of pupils into Count and then runs `Average ← Total / Count`. The user types 0.

(c) A program should add 5% tax to a price, but the line is `Cost ← Price * 0.05`. It runs and shows a value that is much too small.

A: (a) Syntax error, because it breaks the rules of the language and the program cannot start [B1]. (b) Run-time error, because it divides by zero while the program is running and the program stops [B1]. (c) Logic error, because the program runs but gives the wrong result [B1].

Q: [4 marks] ★★ A shop in Accra sells notebooks at 2.50 each. Write pseudocode that inputs the number of notebooks bought, calculates the cost, and outputs it. If the cost is more than 50.0, a 10% discount is taken off before the cost is output.
H: Work out the cost first, then decide whether to reduce it, then output once.
H: A 10% discount means the customer pays 90% of the cost.
A: One possible answer:

```pseudocode
DECLARE Quantity : INTEGER
DECLARE Cost : REAL

INPUT Quantity
Cost ← Quantity * 2.5
IF Cost > 50.0 THEN
   Cost ← Cost * 0.9
ENDIF
OUTPUT Cost
```

- inputs the quantity [B1]
- calculates the cost as the quantity times 2.5 [B1]
- IF with the condition cost greater than 50.0, reducing the cost by 10% (for example `Cost * 0.9`) [B1]
- outputs the final cost after the IF, so that it is output in both cases [B1]

Q: [5 marks] ★★ Complete a trace table, with columns Number, Steps and OUTPUT, for this pseudocode.

```pseudocode
Number ← 5
Steps ← 0
WHILE Number > 1
   IF Number MOD 2 = 0 THEN
      Number ← Number DIV 2
   ELSE
      Number ← Number * 3 + 1
   ENDIF
   Steps ← Steps + 1
ENDWHILE
OUTPUT Steps
```

H: Number 5 is odd, so the ELSE branch runs on the first repeat.
H: Test `Number > 1` before every repeat. Stop when Number reaches 1.
A: One row per repeat, with Number and Steps changed on it.

| Number | Steps | OUTPUT |
|---|---|---|
| 5 | 0 | |
| 16 | 1 | |
| 8 | 2 | |
| 4 | 3 | |
| 2 | 4 | |
| 1 | 5 | |
| | | 5 |

- initial values 5 and 0 [B1]
- Number becomes 16 then 8 [B1]
- Number becomes 4, 2 and then 1 [B1]
- Steps counts 1, 2, 3, 4, 5 [B1]
- 5 is output once, after the loop ends [B1]

Q: [5 marks] ★★ A market trader in Kumasi types in each day's sales as a whole number. The typing ends when the trader types 0. Write pseudocode that outputs the total of the numbers typed (not counting the 0) and how many numbers were typed.
H: You do not know how many numbers there will be, so which loop?
H: The final 0 must not be added to the total or counted.
A: One possible answer:

```pseudocode
DECLARE Number, Total, Count : INTEGER

Total ← 0
Count ← 0
INPUT Number
WHILE Number <> 0
   Total ← Total + Number
   Count ← Count + 1
   INPUT Number
ENDWHILE
OUTPUT "Total: ", Total
OUTPUT "Count: ", Count
```

- initialises Total and Count to 0 [B1]
- a loop that repeats until 0 is entered (for example `WHILE Number <> 0`) [B1]
- inputs a number inside the loop, and before it when the loop is a WHILE [B1]
- adds Number to Total and 1 to Count, only for numbers that are not 0 [B1]
- outputs the total and the count after the loop [B1]

(A REPEAT … UNTIL loop is also correct if the 0 is not added or counted.)

Q: [4 marks] ★★ A school in Dar es Salaam makes each pupil a username from the first three letters of the pupil's first name followed by the last name, all in lower case. The question gives these functions: `LEFT(S, N)` returns the first N characters of the string S, and `TO_LOWER(S)` returns S in lower case. Write pseudocode that inputs FirstName and LastName and outputs the username. For example, "Amina" and "Mwangi" give "amimwangi".
H: Build the username in one assignment, using `&` to join.
A: One possible answer:

```pseudocode
DECLARE FirstName, LastName, Username : STRING

INPUT FirstName
INPUT LastName
Username ← TO_LOWER(LEFT(FirstName, 3) & LastName)
OUTPUT Username
```

- inputs both names [B1]
- takes the first three characters with `LEFT(FirstName, 3)` [B1]
- joins them to the last name with `&` [B1]
- converts to lower case with TO_LOWER and outputs the result [B1]

Q: [8 marks] ★★★ A bus company in Lima charges fares by age: a passenger under 12 pays 1.50, a passenger from 12 to 64 pays 3.00, and a passenger aged 65 or over pays 1.00. A program inputs the ages of 10 passengers and outputs the total of their fares.

(a) Complete the identifier table with a suitable data type for each variable. [3]

| Identifier | Data type | Purpose |
|---|---|---|
| Passenger | | counts the passengers from 1 to 10 |
| Age | | the age of one passenger |
| TotalFare | | the sum of the fares |

(b) Write the pseudocode for the program. [5]
H: For (b), which loop is right when you know there are exactly 10 passengers?
H: Use one IF inside the ELSE of another to choose between three fares.
A: (a) Passenger: INTEGER [B1]. Age: INTEGER [B1]. TotalFare: REAL, because fares have a fractional part [B1].

(b) One possible answer:

```pseudocode
DECLARE Passenger, Age : INTEGER
DECLARE TotalFare : REAL

TotalFare ← 0.0
FOR Passenger ← 1 TO 10
   INPUT Age
   IF Age < 12 THEN
      TotalFare ← TotalFare + 1.5
   ELSE
      IF Age < 65 THEN
         TotalFare ← TotalFare + 3.0
      ELSE
         TotalFare ← TotalFare + 1.0
      ENDIF
   ENDIF
NEXT Passenger
OUTPUT "Total fare: ", TotalFare
```

- TotalFare initialised to 0 before the loop [B1]
- FOR loop from 1 to 10 that inputs an age on every repeat [B1]
- a passenger under 12 adds 1.50 [B1]
- a passenger from 12 to 64 adds 3.00, using a second test inside the first ELSE [B1]
- a passenger of 65 or over adds 1.00, and the total is output after the loop [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A children's game counts from 1 to 15. For a multiple of 3 it says "Tick", for a multiple of 5 it says "Tock", and for a multiple of both 3 and 5 it says "TickTock". Every other number is shown as itself. Write pseudocode that outputs the 15 lines.
H: The test for "both" must come first. Why does a multiple of 15 fail if you test for 3 first?
H: A number can be a multiple of 3 and of 5 only if `Number MOD 15 = 0`.
A: One possible answer:

```pseudocode
DECLARE Number : INTEGER

FOR Number ← 1 TO 15
   IF Number MOD 15 = 0 THEN
      OUTPUT "TickTock"
   ELSE
      IF Number MOD 3 = 0 THEN
         OUTPUT "Tick"
      ELSE
         IF Number MOD 5 = 0 THEN
            OUTPUT "Tock"
         ELSE
            OUTPUT Number
         ENDIF
      ENDIF
   ENDIF
NEXT Number
```

- FOR loop from 1 to 15 [B1]
- tests for a multiple of both 3 and 5 first (`MOD 15`, or both `MOD 3` and `MOD 5`) [B1]
- tests `Number MOD 3 = 0` and outputs "Tick" [B1]
- tests `Number MOD 5 = 0` and outputs "Tock" [B1]
- outputs the number itself otherwise [B1]
- nested IF (or ELSE) so that each number gives exactly one line [B1]

The same in Python:

```python
for number in range(1, 16):
    if number % 15 == 0:
        print("TickTock")
    elif number % 3 == 0:
        print("Tick")
    elif number % 5 == 0:
        print("Tock")
    else:
        print(number)
```

Output:

```output
1
2
Tick
4
Tock
Tick
7
8
Tick
Tock
11
Tick
13
14
TickTock
```

Q: [6 marks] ★★★ Write pseudocode that inputs a positive whole number and outputs the sum of its digits, using only DIV, MOD, a loop and a total. For example 4096 gives \(4 + 0 + 9 + 6 = 19\). Then complete a trace table for the input 4096.
H: `Number MOD 10` is the last digit. `Number DIV 10` is the number without its last digit.
H: Repeat until no digits are left, that is while Number is greater than 0.
A: One possible answer:

```pseudocode
DECLARE Number, Total : INTEGER

INPUT Number
Total ← 0
WHILE Number > 0
   Total ← Total + Number MOD 10
   Number ← Number DIV 10
ENDWHILE
OUTPUT Total
```

- inputs the number [B1]
- Total initialised to 0 [B1]
- loop that continues while Number is greater than 0 [B1]
- adds the last digit (`Number MOD 10`) to Total [B1]
- removes the last digit (`Number DIV 10`) in the loop [B1]
- outputs Total after the loop [B1]

The trace table for 4096:

| Number | Total | OUTPUT |
|---|---|---|
| 4096 | 0 | |
| 409 | 6 | |
| 40 | 15 | |
| 4 | 15 | |
| 0 | 19 | |
| | | 19 |

The Python version, with 4096 typed:

```python
number = int(input("Enter a number: "))
total = 0
while number > 0:
    total = total + number % 10
    number = number // 10
print("Digit sum:", total)
```

Output:

```output
Enter a number: 4096
Digit sum: 19
```
:::

:::quiz
? A Python program reads two numbers with `a = input()` and `b = input()`. The user types 3 and then 4. What does `print(a + b)` show?
- 7
- 7.0
+ 34
- an error, because you cannot add the two names
> `input()` returns strings, and `+` joins strings, so "3" and "4" make "34". Use `int(a) + int(b)` to get 7.
? What does `for n in range(1, 5):` followed by `print(n)` output?
- 1 2 3 4 5, one per line
+ 1 2 3 4, one per line
- 2 3 4 5, one per line
- 0 1 2 3 4, one per line
> The range stops before its second number, so it includes 1 and stops after 4. The pseudocode `FOR N ← 1 TO 5` would include 5, but Python's range does not.
? What is the value of `17 MOD 5` in pseudocode?
- 3
- 3.4
+ 2
- 12
> MOD gives the remainder: 17 is 3 fives (15) with 2 left over. The answer 3 is the whole-number quotient, `17 DIV 5`.
? A program runs without any error message but shows the wrong answer. Which kind of error is it?
- syntax error
- run-time error
+ logic error
- compile error
> A logic error is a mistake in the design that lets the program run to the end and gives wrong results. Syntax errors stop the program starting; run-time errors stop it while it runs.
? Which line of Python checks whether `score` is equal to 10?
- `if score = 10:`
+ `if score == 10:`
- `if score ← 10:`
- `if score <> 10:`
> In Python `=` stores a value and `==` compares. `←` and `<>` are pseudocode symbols (and `<>` means "not equal" there).
? What does `5 + 6 * 2` equal?
- 22
+ 17
- 16
- 13
> Multiplication happens before addition: \(6 \times 2 = 12\), then \(5 + 12 = 17\). The answer 22 adds first, which only brackets can make happen: `(5 + 6) * 2`.
? Which loop always runs its body at least once?
- FOR
- WHILE
+ REPEAT … UNTIL
- none of them
> REPEAT … UNTIL tests its condition after the body. A WHILE loop tests first and can run zero times, and a FOR loop whose start is past its end also runs zero times.
? In Python, what does `print(8 / 2)` show?
- 4
+ 4.0
- 4.5
- an error
> `/` always gives a real number, so `8 / 2` is `4.0`. Use `8 // 2` when you want the whole number 4.
? A program has `A ← 5`, then `B ← A`, then `A ← 9`. What does B hold at the end?
+ 5
- 9
- 14
- B and A are now the same variable
> `B ← A` copies the value 5 into B at that moment. Changing A afterwards does not change B.
:::

:::checklist What you can now do
- [ ] I can explain what a program, an algorithm and pseudocode are, and why Cambridge uses pseudocode in Paper 2 and Python in Paper 4.
- [ ] I can show output with `OUTPUT` and `print()`, and write comments with `//` and `#`.
- [ ] I can declare and assign variables and constants, choose meaningful names, and choose INTEGER, REAL, STRING or BOOLEAN.
- [ ] I can use `+ - * /` and DIV and MOD (`//` and `%`) and write calculations with the correct order and brackets.
- [ ] I can read values with `INPUT` and `input()`, and convert text to numbers with `int()` and `float()`.
- [ ] I can write comparisons and combine them with AND, OR and NOT, without mixing up `←`, `=` and `==`.
- [ ] I can write IF statements, including nested IF and `elif`, with the correct indentation.
- [ ] I can write FOR, WHILE and REPEAT … UNTIL loops in pseudocode, translate them to Python, and choose between them.
- [ ] I can find the length of a string, join strings, take part of a string and convert to capitals.
- [ ] I can tell syntax, run-time and logic errors apart and read a Python error message.
- [ ] I can complete a trace table for an algorithm with a loop.
- [ ] I can write a short input–process–output program in both pseudocode and Python.
:::

:::recap
- A program is a set of instructions; an algorithm is the sequence of defined steps behind it. Pseudocode is the Cambridge way to write an algorithm on paper (Paper 2); Python is the language of Paper 4.
- A variable is a named box for a value that can change. `Score ← Score + 10` (pseudocode) and `score = score + 10` (Python) store the value of the right-hand side in the variable.
- Data types: INTEGER (`int`), REAL (`float`), STRING (`str`), BOOLEAN (`bool`). `/` always gives a REAL; DIV and MOD (`//` and `%`) give the whole-number quotient and the remainder.
- Order of calculation: brackets, then `*` `/` DIV MOD, then `+` `-`. The mean of A and B is `(A + B) / 2`.
- `input()` always returns a string; convert with `int()` or `float()` before you calculate.
- Comparisons give TRUE or FALSE: `=` `<>` in pseudocode, `==` `!=` in Python. Combine with AND, OR, NOT.
- Selection: IF … THEN … ELSE … ENDIF; Python uses a colon, indentation and `elif`. Test the narrowest condition first.
- Iteration: FOR (known number of repeats; Python's `range` stops before its end value), WHILE (test first, may run zero times), REPEAT … UNTIL (test last, runs at least once, stops when the condition is true; Python uses `while True` with `break`).
- Syntax errors stop the program starting; run-time errors stop it while it runs; logic errors give wrong results. Read a Python error from the bottom line up.
- A trace table has a column for each variable and the output, with a new row each time a value changes.
:::

:::links
- read: [The Python tutorial](https://docs.python.org/3/tutorial/) · Python.org · the official tutorial, clear and free
- read: [W3Schools Python](https://www.w3schools.com/python/) · W3Schools · short Python lessons with try-it boxes
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste any program from this chapter and watch each variable change line by line
- practise: [Exercism Python track](https://exercism.org/tracks/python) · Exercism · free Python exercises with feedback
- practise: [Programming basics: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/programming-basics/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [CS50](https://cs50.harvard.edu/x/) · Harvard CS50 · a free introductory course with problem sets

Links checked 13 November 2026.
:::

Next: [Number systems and binary arithmetic](#cs.data)
