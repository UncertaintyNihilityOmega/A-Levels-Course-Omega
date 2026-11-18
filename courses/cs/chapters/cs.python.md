@chapter cs.python
@title Python for Paper 4: the practical toolkit
@level a2
@paper CAIE 9618 Paper 4
@time 5–7 hours
@summary Paper 4 is a practical exam: you write Python on a computer and save evidence of it working. You will learn how to read a task, set up global lists and records, handle strings and files, translate any pseudocode construct into Python, read a traceback quickly, test your code, and manage 2 hours 30 minutes.
:::why
Papers 1 to 3 are written on paper. Paper 4 is different: you sit at a computer, write programs that run, and copy the code and a picture of the output into an evidence document. A program that almost works earns few marks, and one that has the right names and the exact output earns many. This chapter collects the Python skills and the exam habits that turn a task into marks. It teaches no new syllabus topic: it uses what you learned in the programming chapters, and shows how it is examined.
:::

**Before you start**, you should have worked through the Python in [Data types, records and arrays](#cs.datatypes), [Procedures, functions and parameters](#cs.procedures), [Object-oriented programming](#cs.oop) and [File processing and exception handling](#cs.fileproc).

:::try Warm-up
Q: How do you create a Python list `Marks` of 5 items, all 0? And why is `[[0] * 5] * 3` a poor way to make a list of three rows? (from [Data types, records and arrays](#cs.datatypes))
A: `Marks = [0] * 5`. In `[[0] * 5] * 3` the three rows are the **same** list, so changing one element changes it in every row. Use `[[0] * 5 for _ in range(3)]`.
Q: What do `17 // 5` and `17 % 5` give, and which pseudocode operators do they match? (from [Programming from zero](#cs.f.basics))
A: 3 and 2. `//` is DIV (the quotient) and `%` is MOD (the remainder).
Q: How does Paper 4 let you store a record? (from [Data types, records and arrays](#cs.datatypes))
A: With a class that has an `__init__` method: the paper says "a class declaration can be used to declare a record".
:::

## What Paper 4 asks of you

The front page of the May/June 2025 paper sets out the rules of the exam. The details that shape how you work are these.

| Fact | What it means for you |
|---|---|
| 2 hours 30 minutes, 75 marks | an average of 2 minutes per mark, since \(150 \div 75 = 2\) |
| you need the candidate source files and `evidence.doc` | files such as text files of data are supplied; do not look for them elsewhere |
| carry out every instruction in each task | every sentence of a question is worth marks or tells you how to get them |
| save work using the file names given | a program saved under another name may earn no marks |
| no internet or email | you cannot look things up, so learn the toolkit in this chapter |
| save your work in the evidence document, or no marks for that task | the evidence document is the examiner's copy of your work |
| Python (console mode), Java or Visual Basic; a mark of zero if another language is used | this course teaches Python: make sure that you run it in console mode, not in a notebook or app |

That 2025 paper had 3 questions worth 20, 25 and 30 marks. Each part says to save the program under a given name and to copy and paste the program code into the matching part of the evidence document, and the testing parts ask for a screenshot of the output. Your own paper's front page tells you what to do; read it before you start.

:::def Evidence document
A word-processed file supplied with Paper 4, in which you paste your program code and screenshots of its output, part by part, so that the examiner can see your work. It is saved with a name that includes your centre number and candidate number.
:::

:::steps
1. Open the evidence document first and save it with the name the paper gives (with your centre and candidate numbers).
2. For each part: write the code, run it, fix it, save the program **with the exact file name the question gives**, then paste the code into the evidence document.
3. For a testing part: run the program with the test data the task gives, take a screenshot of the console showing the output, and paste it.
4. Save the evidence document often, and again at the end. Check the file names last.
:::

## Reading a task

A Paper 4 task is written to be followed to the letter. Read the whole question once, then go through it part by part.

- **Use the names exactly.** If the task says the array is `Queue`, the pointer is `HeadPointer` and the function is `Enqueue`, then use those names, capitals and all. A test program that the examiner has written, or a later part of the question, may rely on them. (In this chapter the examples use the task's names, not `snake_case`, for that reason.)
- **Note the array sizes and the index range.** "A global 1D array of 20 elements, indexes 0 to 19" is a Python list `[...] * 20`. If the task says "indexes 1 to 20", you must take care: see below.
- **"Global" means defined outside every function**, so that every function can reach it.
- **Return or output?** If a part says the function "returns" a value, use `return`. If it says "outputs", use `print`. Do not mix them up.
- **Match the output.** If the question shows an expected output, such as `Added Aisha`, your program's output should say the same thing in the same form.

:::exam Every instruction is a mark
Underline each instruction in the question as you read it ("define a class", "return FALSE if the array is full", "output a message"). The mark scheme gives about one mark per instruction. After you finish a part, check each underlined instruction against your code, one by one.
:::

## Lists, 2D lists and records

### One-dimensional global lists

A Cambridge array of `n` items is a Python **list**. A task that gives indexes from 0, such as `ARRAY[0:5]`, matches a Python list directly: index 0 is the first item. A task that gives indexes from 1 needs a decision, and you should say which you chose. Two methods work.

- **Subtract 1** at every use: pseudocode `Marks[Index]` becomes `marks[index - 1]`.
- **Leave index 0 unused** by creating the list one item longer: `marks = [0] * 7` for 6 items, then `marks[1]` to `marks[6]` as in the pseudocode.

```python
Queue = [""] * 6                       # 1D list: indexes 0 to 5
Grid = [[0] * 5 for _ in range(4)]     # 2D list: 4 rows, 5 columns
Grid[1][3] = 9                         # row 1, column 3 (counting from 0)
print(Queue)
print(Grid)

Bad = [[0] * 5] * 4                    # WRONG: four names for ONE row
Bad[1][3] = 9
print(Bad)
```

Output:

```output
['', '', '', '', '', '']
[[0, 0, 0, 0, 0], [0, 0, 0, 9, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[0, 0, 0, 9, 0], [0, 0, 0, 9, 0], [0, 0, 0, 9, 0], [0, 0, 0, 9, 0]]
```

The last line is the mistake from [Data types, records and arrays](#cs.datatypes): `[[0] * 5] * 4` repeats one row four times, so a change to one row shows in all of them.

:::def List comprehension
A short way to build a list from a loop, in the form `[expression for name in sequence]`. This course uses only the simple form, such as `[[0] * 5 for _ in range(4)]` (a new row for each of 4 passes; `_` is a name for a variable you do not use) or `[p.strip() for p in parts]`.
:::

### Global variables inside functions

:::def Global variable
A variable that is created outside every function, so that all of the program can read it. A function that **assigns** to a global variable must say so with the word `global`; a function that only reads one does not need to.
:::

```python
Count = 0

def add_one():
    global Count
    Count = Count + 1

def show_double():
    print(Count * 2)

add_one()
add_one()
print(Count)
show_double()
```

Output:

```output
2
4
```

Without the line `global Count`, the assignment `Count = Count + 1` would make `Count` a **new local variable** inside `add_one`, and Python would stop with an `UnboundLocalError` when it tried to read it before giving it a value. This is one of the commonest slips in Paper 4 programs that use global pointers.

### Records and arrays of records

A record is a class with an `__init__` method. Default values let you create a list of empty records and fill them in later, which is how a task that says "an array of 3 `Item` records" is usually met.

```python
class Item:
    def __init__(self, code="", quantity=0):
        self.code = code
        self.quantity = quantity

Stock = [Item() for _ in range(3)]
Stock[0].code = "A100"
Stock[0].quantity = 12
Stock[2] = Item("C300", 4)
for item in Stock:
    print(repr(item.code), item.quantity)
```

Output:

```output
'A100' 12
'' 0
'C300' 4
```

`Item()` with no arguments uses the defaults, so slot 1 stays empty. `repr` shows the quotes, which makes the empty string visible. The comprehension calls `Item()` three times, so there are three separate objects: writing `[Item()] * 3` would give one object three times, the same mistake as for 2D lists.

## Strings, numbers and output

Paper 4 tasks handle text all the time: validating a code, splitting a line, building a message. This program shows every string tool that you need.

```python
word = "Computer"
print(word[0], word[-1], word[:3], word[3:])
print(word[2:2 + 4])
print(len(word), word.upper(), word.lower())

sentence = "  red, green ,blue "
parts = sentence.split(",")
print(parts)
print([p.strip() for p in parts])

print("2024".isdigit(), "20.5".isdigit(), "-3".isdigit())
print(ord("A"), chr(66), chr(ord("a") + 2))
print(str(42) + "!", int("17") + 1, float("2.5") * 2)

price = 3.456
print(round(price, 2), f"{price:.2f}", f"{4:>3}|")
```

Output:

```output
C r Com puter
mput
8 COMPUTER computer
['  red', ' green ', 'blue ']
['red', 'green', 'blue']
True False False
65 B c
42! 18 5.0
3.46 3.46   4|
```

How to read it:

- `word[0]` is the first character and `word[-1]` the last. `word[:3]` is the first three characters, and `word[3:]` is everything from index 3.
- `word[2:2 + 4]` takes 4 characters starting at index 2: this is the pseudocode `MID(Word, 3, 4)`, because pseudocode counts from 1.
- `split(",")` cuts a string at every comma and gives a list of strings. `strip()` removes spaces and `"\n"` from both ends.
- `isdigit()` is True only for a string made entirely of the digits 0 to 9, so it is False for `"20.5"` and `"-3"`. To accept those, use `float()` inside a `try`, as in [File processing and exception handling](#cs.fileproc).
- `ord` gives the character code, `chr` turns a code into a character.
- `round(price, 2)` rounds a number, and `f"{price:.2f}"` builds a string with exactly two decimal places. `:>3` right-aligns in a width of 3.

:::def f-string
A string literal that starts with `f` and contains names or expressions in curly brackets, which are replaced by their values: `f"Total: {total}"`. A format such as `:.2f` after the name sets the layout of the value.
:::

:::warn input() returns a string
`age = input("Age: ")` stores text. `age + 1` raises a `TypeError`, and `age > 17` compares text with a number. Convert first: `age = int(input("Age: "))`. Put the conversion inside a `try` when the user might type something else.
:::

## From pseudocode to Python

Papers 2 and 3 use Cambridge pseudocode, and Paper 4 uses Python, so you must be able to move between them in both directions. This table has every construct.

| Pseudocode | Python |
|---|---|
| `X ← 5` | `x = 5` |
| `DECLARE X : INTEGER` | nothing: a variable exists when it is first assigned |
| `CONSTANT Rate = 0.2` | `RATE = 0.2` (capitals by convention) |
| `INPUT X` | `x = int(input())` (convert to the right type) |
| `OUTPUT "Total: ", Total` | `print("Total:", total)` |
| `IF … THEN … ELSE … ENDIF` | `if …:` and `else:` |
| an `IF` inside an `ELSE` | `elif …:` |
| `CASE OF … ENDCASE` | `if` / `elif` / `else` |
| `FOR I ← 1 TO N` | `for i in range(1, n + 1):` |
| `FOR I ← N TO 1 STEP -1` | `for i in range(n, 0, -1):` |
| `WHILE c … ENDWHILE` | `while c:` |
| `REPEAT … UNTIL c` | `while True:` with `if c: break` at the end |
| `PROCEDURE P(A)` and `CALL P(5)` | `def p(a):` and `p(5)` |
| `FUNCTION F(A) RETURNS INTEGER` | `def f(a):` with `return` |
| `BYREF` parameter | return the new value(s), or change a list or object that was passed in |
| `DECLARE A : ARRAY[1:n] OF INTEGER` | `a = [0] * (n + 1)` (index 0 unused) or `[0] * n` and subtract 1 |
| `Board[2, 3]` | `board[1][2]` (counting from 0) |
| `TYPE … ENDTYPE` (record) | a `class` with `__init__`; `Item.Price` becomes `item.price` |
| `CLASS B INHERITS A` | `class B(A):`; `SUPER.NEW(X)` becomes `super().__init__(x)` |
| `NEW Cat("Kit")` | `Cat("Kit")` |
| `OPENFILE F FOR READ` | `open(f, "r")` or `with open(f, "r") as file:` |
| `READFILE F, Line` | `line = file.readline()` |
| `WRITEFILE F, Data` | `file.write(data + "\n")` |
| `EOF(F)` | `line == ""` after `readline()`, or the end of a `for line in file` loop |
| `&` (join strings) | `+` |
| `DIV`, `MOD` | `//`, `%` (for positive numbers) |
| `<>`, `=` (comparison) | `!=`, `==` |
| `AND`, `OR`, `NOT`, `TRUE`, `FALSE` | `and`, `or`, `not`, `True`, `False` |
| `// comment` | `# comment` |

The string and number functions of the Paper 2 insert have these matches.

| Insert function | Python |
|---|---|
| `LENGTH(S)` | `len(s)` |
| `LEFT(S, N)` | `s[:n]` |
| `RIGHT(S, N)` | `s[-n:]` (for n greater than 0) |
| `MID(S, X, Y)` | `s[x - 1:x - 1 + y]` |
| `TO_UPPER(S)`, `TO_LOWER(S)` | `s.upper()`, `s.lower()` |
| `NUM_TO_STR(X)`, `STR_TO_NUM(S)` | `str(x)`, `int(s)` or `float(s)` |
| `IS_NUM(S)` | `s.isdigit()` for whole numbers, or `float(s)` in a `try` for any number |
| `ASC(C)`, `CHR(N)` | `ord(c)`, `chr(n)` |
| `INT(X)` | `int(x)` |
| `RAND(X)` | `random.random() * x`, after `import random` |

`random.random()` gives a number from 0 up to but not including 1, so `random.random() * x` is from 0 up to but not including x. Because the result changes every run, you cannot print it and expect fixed output; test it by checking its range.

```python
import random

values = [random.random() * 10 for _ in range(1000)]
print(min(values) >= 0, max(values) < 10)
```

Output:

```output
True True
```

:::eg Translating pseudocode into Python (exam style)
Translate each pseudocode program into Python and give the output. [6 marks]

**Program 1**

```pseudocode
CONSTANT PassMark = 50
DECLARE Marks : ARRAY[1:6] OF INTEGER
DECLARE Index, Passes, Total : INTEGER
DECLARE Average : REAL

Marks[1] ← 71
Marks[2] ← 45
Marks[3] ← 88
Marks[4] ← 50
Marks[5] ← 62
Marks[6] ← 38
Passes ← 0
Total ← 0
FOR Index ← 1 TO 6
   Total ← Total + Marks[Index]
   IF Marks[Index] >= PassMark THEN
      Passes ← Passes + 1
   ENDIF
NEXT Index
Average ← Total / 6
OUTPUT "Passes: ", Passes
OUTPUT "Average: ", Average
OUTPUT "Last digit of total: ", Total MOD 10
OUTPUT "Tens in total: ", Total DIV 10
```

The array runs from 1, so the Python list gets an unused item at index 0, and the loop runs to 6 inclusive, which is `range(1, 7)`.

```python
PASS_MARK = 50
marks = [None, 71, 45, 88, 50, 62, 38]
passes = 0
total = 0
for index in range(1, 7):
    total = total + marks[index]
    if marks[index] >= PASS_MARK:
        passes = passes + 1
average = total / 6
print("Passes:", passes)
print("Average:", average)
print("Last digit of total:", total % 10)
print("Tens in total:", total // 10)
```

Output:

```output
Passes: 4
Average: 59.0
Last digit of total: 4
Tens in total: 35
```

The total is \(71 + 45 + 88 + 50 + 62 + 38 = 354\), so the average is \(354 \div 6 = 59.0\), the last digit is \(354 \bmod 10 = 4\) and the tens are \(354 \operatorname{div} 10 = 35\).

**Program 2**

```pseudocode
DECLARE Value, Count : INTEGER
Value ← 3
Count ← 0
REPEAT
   Value ← Value * 2
   Count ← Count + 1
UNTIL Value > 100
OUTPUT Count, " doublings give ", Value
```

`REPEAT … UNTIL` runs the body at least once and stops when the condition becomes true. Python has no such loop, so `while True` with a `break` at the end of the body does the same.

```python
value = 3
count = 0
while True:
    value = value * 2
    count = count + 1
    if value > 100:
        break
print(count, "doublings give", value)
```

Output:

```output
6 doublings give 192
```

The value goes 6, 12, 24, 48, 96, 192, so there are 6 doublings, and the loop stops at the first value above 100.

**Program 3**

```pseudocode
FUNCTION Grade(Mark : INTEGER) RETURNS CHAR
   IF Mark >= 80 THEN
      RETURN 'A'
   ELSE
      IF Mark >= 50 THEN
         RETURN 'B'
      ELSE
         RETURN 'C'
      ENDIF
   ENDIF
ENDFUNCTION

PROCEDURE Swap(BYREF First : INTEGER, BYREF Second : INTEGER)
   DECLARE Temp : INTEGER
   Temp ← First
   First ← Second
   Second ← Temp
ENDPROCEDURE

DECLARE Low, High : INTEGER
Low ← 90
High ← 40
CALL Swap(Low, High)
OUTPUT "Low is ", Low, " grade ", Grade(Low)
OUTPUT "High is ", High, " grade ", Grade(High)
```

A Python function cannot change a number that the caller holds, so the `BYREF` procedure becomes a function that **returns** the two values in the new order.

```python
def grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 50:
        return "B"
    else:
        return "C"

def swap(first, second):
    return second, first

low = 90
high = 40
low, high = swap(low, high)
print("Low is", low, "grade", grade(low))
print("High is", high, "grade", grade(high))
```

Output:

```output
Low is 40 grade C
High is 90 grade A
```

- Program 1: list with an unused index 0 (or index − 1 used), and `range(1, 7)` [B1]
- Program 1: `%` and `//` for MOD and DIV, and the correct output (4, 59.0, 4, 35) [B1]
- Program 2: `while True` with a `break` when the value exceeds 100, with the body before the test [B1]
- Program 2: the correct output `6 doublings give 192` [B1]
- Program 3: nested IF as `if` / `elif` / `else`, with `return` in each branch [B1]
- Program 3: the BYREF swap written as a function that returns both values, used as `low, high = swap(low, high)`, with the correct output [B1]
:::

## Input validation

Many tasks say "the user must be asked again until a valid value is entered". The pattern is a loop that only ends when the value passes every test. For a whole number in a range, the conversion goes in a `try` (see [File processing and exception handling](#cs.fileproc)) and the range test follows.

```python
def read_choice(low, high):
    while True:
        text = input("Choose " + str(low) + " to " + str(high) + ": ")
        try:
            choice = int(text)
        except ValueError:
            print("Not a whole number")
            continue
        if choice < low or choice > high:
            print("Out of range")
        else:
            return choice

picked = read_choice(1, 5)
print("You chose", picked)
```

Output, when the user types `x`, then 9, then 4:

```output
Choose 1 to 5: x
Not a whole number
Choose 1 to 5: 9
Out of range
Choose 1 to 5: 4
You chose 4
```

The `continue` sends control straight back to the top of the loop, so a word that cannot be converted skips the range test, which would fail on a missing value.

## Testing and evidence

A Paper 4 task often ends with "test your program" and a screenshot. A test shows that the program does what the task asks, so choose data that shows each requirement, and make the output easy to read.

:::key Habits that protect your marks
- **Run after every part**, not only at the end. A small error found at once costs seconds; found at the end, it costs minutes.
- **Run the saved file** from the same folder as the data files, in console mode, just as the examiner will. A program that works only in the editor's shell may not work when run on its own.
- **Keep data files in the same folder as the program.** A `FileNotFoundError` in Paper 4 is usually a wrong folder or a wrong name. Copy file names exactly, including capital letters and the extension.
- **Print what the task asks** and label it (`print("Total:", total)`), so the examiner can find each answer in the screenshot.
- **Test the three kinds of data**: normal, boundary (the edge of the valid range) and erroneous, as in [Testing, errors and maintenance](#cs.testing). For a seat number from 1 to 5: 3 is normal, 1 and 5 are boundary, and 0 and 6 are erroneous.
- **Take the screenshot after the final run** and make sure the whole output is visible in it.
:::

## Reading a traceback

When a Python program stops with an error, it prints a **traceback**. It looks long, but it takes ten seconds to read if you start at the bottom.

:::def Traceback
The message that Python prints when a program stops with an unhandled exception. It lists the lines being run, ending with the line that failed, then the type of error and a message.
:::

```text
Traceback (most recent call last):
  File "Question1.py", line 14, in <module>
    print(scores[5])
IndexError: list index out of range
```

1. **Last line first**: the error type (`IndexError`) and its message say what went wrong: an index outside the list.
2. **The line above it**: the line of code that failed (`print(scores[5])`), and just above it the file and line number (line 14).
3. **Think about why**: the list `scores` must have fewer than 6 items, so item 5 does not exist. Remember that a list of 5 items has indexes 0 to 4.

The error types you will meet most are in the table.

| Error | Usual cause |
|---|---|
| `SyntaxError`, `IndentationError` | a missing colon or bracket, or lines indented by different amounts; Python reports it before the program runs |
| `NameError` | a name that has not been defined: a typing mistake, or used before it is assigned |
| `TypeError` | the wrong kind of value, such as `"Score: " + 5`, or calling something that is not a function |
| `ValueError` | the right type but an unusable value, such as `int("4.5")` |
| `IndexError` | a list index outside the list: often an off-by-one |
| `UnboundLocalError` | assigning to a global variable inside a function without `global` |
| `AttributeError` | an attribute or method that does not exist, often a spelling mistake |
| `FileNotFoundError` | a wrong file name or the file is in another folder |

The program below runs seven small functions, each with one of these mistakes, and prints the type of error each one causes. It catches the general `Exception` only here, to list them: in your own programs you should name the exception that you expect.

```python
total = 0

def off_by_one():
    scores = [10, 20, 30]
    return scores[3]

def missing_global():
    global_total = total
    total = total + 5
    return global_total

def typo_name():
    return totl

def wrong_type():
    return "Score: " + 5

def shadowed():
    list = [1, 2]
    return list("ab")

def bad_conversion():
    return int("4.5")

def no_attribute():
    return "abc".push("d")

for function in [off_by_one, missing_global, typo_name, wrong_type, shadowed, bad_conversion, no_attribute]:
    try:
        function()
    except Exception as error:
        print(function.__name__, "->", type(error).__name__)
```

Output:

```output
off_by_one -> IndexError
missing_global -> UnboundLocalError
typo_name -> NameError
wrong_type -> TypeError
shadowed -> TypeError
bad_conversion -> ValueError
no_attribute -> AttributeError
```

Two of these deserve a second look. In `shadowed`, the name `list` was used for a variable, so it no longer means the built-in function `list`, and calling it fails. Never use the names of built-in functions (`list`, `max`, `min`, `sum`, `input`, `str`) for your own variables. In `missing_global`, the assignment `total = total + 5` makes `total` local to the whole function, so reading it on the line before fails.

:::eg Spot the error: a pointer that does not change
A student wrote this part of a program. The global variable `Tail` should move on by one each time an item is added, but when it ran, Python stopped with an error.

```text
Tail = 0
Names = [""] * 4

def Add(Name):
    Names[Tail] = Name
    Tail = Tail + 1

Add("Aisha")
```

```text
Traceback (most recent call last):
  File "Question2.py", line 8, in <module>
    Add("Aisha")
  File "Question2.py", line 5, in Add
    Names[Tail] = Name
UnboundLocalError: cannot access local variable 'Tail' where it is not associated with a value
```

**Question:** State the error type, the cause and the correction. [3 marks]

The line `Tail = Tail + 1` assigns to `Tail`, so Python treats `Tail` as a local variable in the whole function, including the earlier line that reads it. The list `Names` is only changed by an item assignment, so it needs no declaration, but `Tail` does.

- Error: `UnboundLocalError`, raised on the line `Names[Tail] = Name` [B1]
- Cause: `Tail` is assigned inside the function without `global`, so it is a new local variable with no value at that point [B1]
- Fix: add the line `global Tail` at the start of `Add` [B1]
:::

## Common errors under pressure

:::warn Off-by-one with range and with 0-based lists
`range(1, 6)` gives 1, 2, 3, 4, 5, so to count 1 to N you write `range(1, N + 1)`. A list of 6 items has indexes 0 to 5, so `items[6]` is an `IndexError`. When the task says indexes 1 to 6, check which of the two methods (subtract 1, or leave index 0 unused) you are using and apply it **everywhere**.
:::

:::warn / and // are different
`7 / 2` is 3.5 (always a float) and `7 // 2` is 3. Use `//` where the pseudocode says DIV. Both operands should be positive: for negative numbers `//` rounds down (`-7 // 2` is -4), and a task that needs DIV on negative numbers will say how to treat them.
:::

:::warn Comparing strings with numbers
`"10" < "9"` is True, because strings are compared character by character. If a value comes from a file or from `input()`, convert it to `int` or `float` before comparing or adding.
:::

:::warn Wrong file names and folders
A file `Data.txt` is not `data.txt` on every computer. Copy the names from the question. If the task gives a data file, keep it in the same folder as your program, and open it with just its name, not a full path.
:::

## A complete task: a circular queue

Paper 4 often asks for a data structure in a global array with pointers. This task is built the way those tasks are: parts that add up, a test program and an output that shows what happens.

:::eg A clinic queue (exam style)
A clinic in Lahore gives each arriving patient a place in a waiting queue that holds at most 6 names. The queue is a **circular queue** in the global 1D array `WaitQueue` of 6 strings, indexes 0 to 5, which starts with every item `""`. The global integers `Head` (the index of the first name), `Tail` (the index of the next free place) and `Count` (the number of names in the queue) all start at 0. [14 marks]

(a) Write code to declare and initialise these four global variables. [3]

(b) Write a function `Enqueue(Name)` that adds the name at the tail and returns `True`, or returns `False` if the queue is full. [4]

(c) Write a function `Dequeue()` that removes the name at the head and returns it, or returns `""` if the queue is empty. [4]

(d) Write a test program that adds Aisha, Bilal, Chen, Dina, Emeka, Farah and Gul in that order, outputting `Added` and the name, or `Queue full:` and the name followed by `not added`. It then removes two names, adds Hana, and outputs the array and the values of `Head`, `Tail` and `Count`. [3]

Both pointers move forward and **wrap round** to 0 after index 5, which is what `% 6` does: after index 5, \((5 + 1) \bmod 6 = 0\). A dequeued place is set back to `""` so that the array shows what the queue holds.

```python
WaitQueue = [""] * 6
Head = 0
Tail = 0
Count = 0

def Enqueue(Name):
    global Tail, Count
    if Count == 6:
        return False
    WaitQueue[Tail] = Name
    Tail = (Tail + 1) % 6
    Count = Count + 1
    return True

def Dequeue():
    global Head, Count
    if Count == 0:
        return ""
    Name = WaitQueue[Head]
    WaitQueue[Head] = ""
    Head = (Head + 1) % 6
    Count = Count - 1
    return Name

for patient in ["Aisha", "Bilal", "Chen", "Dina", "Emeka", "Farah", "Gul"]:
    if Enqueue(patient):
        print("Added", patient)
    else:
        print("Queue full:", patient, "not added")
print("Served:", Dequeue())
print("Served:", Dequeue())
print("Added Hana:", Enqueue("Hana"))
print(WaitQueue)
print("Head", Head, "Tail", Tail, "Count", Count)
```

Output (this is the text to screenshot for the evidence document):

```output
Added Aisha
Added Bilal
Added Chen
Added Dina
Added Emeka
Added Farah
Queue full: Gul not added
Served: Aisha
Served: Bilal
Added Hana: True
['Hana', '', 'Chen', 'Dina', 'Emeka', 'Farah']
Head 2 Tail 1 Count 5
```

After six names, `Tail` has wrapped to 0 and `Count` is 6, so Gul is refused. Two `Dequeue` calls move `Head` to 2 and leave places 0 and 1 empty. Hana goes into place 0, the first free place, and `Tail` becomes 1. The queue now holds five names, from index 2 round to index 0.

- (a) the list of 6 empty strings and the three pointers all set to 0, outside any function [B1] [B1] [B1]
- (b) `global` declared for `Tail` and `Count` [B1]
- (b) `False` returned when `Count` is 6 (queue full) [B1]
- (b) name stored at `WaitQueue[Tail]`, then `Tail` moved on with wrap-round and `Count` increased [B1]
- (b) `True` returned [B1]
- (c) `Head` and `Count` declared global, and `""` returned when `Count` is 0 [B1]
- (c) name read from `WaitQueue[Head]` and the place cleared [B1]
- (c) `Head` moved on with wrap-round, and `Count` decreased [B1]
- (c) the name returned [B1]
- (d) loop adding the seven names with the correct messages, including the refusal of Gul [B1]
- (d) two names removed, Hana added and the results output [B1]
- (d) the array, `Head`, `Tail` and `Count` output with the correct values [B1]
:::

## Practising whole tasks

The practice below is in the Paper 4 style: a short scenario, named functions, test code and an expected output. Do it at a computer. Write the program, run it, and compare your output with the one shown before you look at the answer.

:::try Start easy, finish at exam standard
Q: Write the Python for the pseudocode `FOR Index ← 10 TO 2 STEP -2` and `OUTPUT Index`, and state the values output.
A: `for index in range(10, 1, -2):` then `print(index)`. The end value of `range` is not included, so it must be 1, not 2. The values are 10, 8, 6, 4, 2.
Q: Write Python for `LEFT(Name, 3)` and `RIGHT(Name, 2)`.
A: `name[:3]` and `name[-2:]`.
Q: A task says the array `Stock` has indexes 1 to 8. Give two ways to store it in Python.
A: Either a list of 8 items with the index reduced by 1 (`stock[index - 1]`), or a list of 9 items with index 0 unused (`stock = [0] * 9`) so `stock[index]` matches.
Q: What is wrong with `Names = [""] * 3` followed by `Names[3] = "Ana"`?
A: The list has indexes 0, 1 and 2, so index 3 raises an `IndexError`.
Q: Write Python to ask for a whole number and convert it, using the name `Quantity`.
A: `Quantity = int(input("Quantity: "))`.
Q: A program prints `"5" + "3"` and `5 + 3`. What are the two outputs?
A: `53` (joining strings) and `8` (adding numbers).
Q: Which line makes a function able to change the global `Count`?
A: `global Count` at the start of the function.
Q: A traceback ends `NameError: name 'totl' is not defined`. What is the likely cause?
A: A typing mistake: the variable was spelled `total` elsewhere, or `totl` was never assigned.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State three things that you must do in Paper 4 so that your work earns marks.
A: Any three of these.

- save each program with the file name the question gives [B1]
- copy and paste the program code into the matching part of the evidence document [B1]
- take a screenshot of the output for a testing part and paste it into the evidence document [B1]
- (accept: write the program in a language the paper allows, because another language scores zero; save the evidence document with the file name the paper gives, because a task not saved there earns no marks)

Q: [4 marks] ★ Write a Python expression for each pseudocode expression. (a) `MID(Code, 2, 3)` (b) `Total DIV 7` (c) `NUM_TO_STR(Count) & " items"` (d) `Words <> "stop"`
A: One mark each.

- (a) `code[1:4]` [B1]
- (b) `total // 7` [B1]
- (c) `str(count) + " items"` [B1]
- (d) `words != "stop"` [B1]

Q: [10 marks] ★★ A cinema hall has 4 rows of 5 seats. Write a Python program that uses a global 2D list `Seats` of 4 rows and 5 columns, in which `"."` means a free seat and `"X"` a booked seat, all free at the start. Write a function `BookSeat(Row, Col)` (row 1 to 4, column 1 to 5, counted from 1) that returns `True` and books the seat if it exists and is free, and returns `False` otherwise; a function `CountFree()` that returns the number of free seats; and a procedure `Display()` that outputs each row on its own line with a space between seats. Test the program by booking row 2 column 3 twice, then row 5 column 1, row 1 column 1 and row 4 column 5, output each result as `Booked:` and the value, then output the number of free seats and the display.
H: Row 1 is index 0, so subtract 1 from both numbers before you use them.
H: Check that the row and column are in range before you look at the list.
A: One possible answer:

```python
Seats = [["."] * 5 for _ in range(4)]

def BookSeat(Row, Col):
    if Row < 1 or Row > 4 or Col < 1 or Col > 5:
        return False
    if Seats[Row - 1][Col - 1] != ".":
        return False
    Seats[Row - 1][Col - 1] = "X"
    return True

def CountFree():
    free = 0
    for row in range(4):
        for col in range(5):
            if Seats[row][col] == ".":
                free = free + 1
    return free

def Display():
    for row in range(4):
        print(" ".join(Seats[row]))

print("Booked:", BookSeat(2, 3))
print("Booked:", BookSeat(2, 3))
print("Booked:", BookSeat(5, 1))
print("Booked:", BookSeat(1, 1))
print("Booked:", BookSeat(4, 5))
print("Free seats:", CountFree())
Display()
```

```output
Booked: True
Booked: False
Booked: False
Booked: True
Booked: True
Free seats: 17
X . . . .
. . X . .
. . . . .
. . . . X
```

- global 2D list created with a comprehension so each row is separate, 4 rows of 5 `"."` [B1]
- `BookSeat` returns `False` when the row or column is outside the range [B1]
- `BookSeat` tests whether the seat is free [B1]
- `BookSeat` converts the row and column to indexes (subtract 1) [B1]
- `BookSeat` sets the seat to `"X"` and returns `True` [B1]
- `CountFree` uses nested loops over all 20 seats [B1]
- `CountFree` counts the free seats and returns the count [B1]
- `Display` outputs one row per line with spaces between the seats (for example with `join`) [B1]
- the five test calls are made, with the results output [B1]
- the output is correct: 17 free seats and the display shown [B1]

Q: [8 marks] ★★ A warehouse in Mombasa uses product codes made of two capital letters, a hyphen and three digits, such as `KE-482`. Write a function `IsValidCode(Code)` that returns `True` only if the code has this form. Then test it with the codes `KE-482`, `ke-482`, `K-4821`, `NG-12A` and `UG-007`, outputting each code and the word `valid` or `invalid`, and finally the number of valid codes.
H: Check the length first, so that the slices cannot go wrong.
H: `isalpha()` and `isupper()` work on the first two characters, and `isdigit()` on the last three.
A: One possible answer:

```python
def IsValidCode(Code):
    if len(Code) != 6:
        return False
    if not (Code[0:2].isalpha() and Code[0:2].isupper()):
        return False
    if Code[2] != "-":
        return False
    return Code[3:].isdigit()

valid = 0
for code in ["KE-482", "ke-482", "K-4821", "NG-12A", "UG-007"]:
    if IsValidCode(code):
        print(code, "valid")
        valid = valid + 1
    else:
        print(code, "invalid")
print("Valid codes:", valid)
```

```output
KE-482 valid
ke-482 invalid
K-4821 invalid
NG-12A invalid
UG-007 valid
Valid codes: 2
```

- length of 6 checked and `False` returned if it is wrong [B1]
- first two characters tested as letters (`isalpha`) [B1]
- and as capitals (`isupper`) [B1]
- third character tested for the hyphen [B1]
- last three characters tested as digits, and the result returned [B1]
- loop over the five codes, calling the function [B1]
- `valid` or `invalid` output for each code, correctly [B1]
- the count of valid codes output, 2 [B1]

Q: [12 marks] ★★★ A company pays its staff by the hour. Write a class `Employee` with attributes `name`, `hours` and `rate` (a whole number), set by `__init__`, and a method `Pay()` that returns `hours * rate`. Write a class `Manager` that inherits from `Employee`, has an extra attribute `bonus`, and overrides `Pay()` to return the usual pay plus the bonus, using the method of the parent class. Create a list holding `Employee("Ana", 40, 20)`, `Employee("Bo", 35, 22)` and `Manager("Cy", 40, 30, 150)`. Output each person's name, hours and pay as `Ana 40 hours: 800`, then the total pay of all three.
H: A `Manager` is also an `Employee`, so one list can hold both; `Pay()` runs the method of the object's own class.
H: In the child class, `super().__init__(...)` sets the attributes of the parent, and `super().Pay()` calls the parent's method.
A: One possible answer:

```python
class Employee:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def Pay(self):
        return self.hours * self.rate

class Manager(Employee):
    def __init__(self, name, hours, rate, bonus):
        super().__init__(name, hours, rate)
        self.bonus = bonus

    def Pay(self):
        return super().Pay() + self.bonus

staff = [Employee("Ana", 40, 20), Employee("Bo", 35, 22), Manager("Cy", 40, 30, 150)]
total = 0
for person in staff:
    print(person.name, person.hours, "hours:", person.Pay())
    total = total + person.Pay()
print("Total pay:", total)
```

```output
Ana 40 hours: 800
Bo 35 hours: 770
Cy 40 hours: 1350
Total pay: 2920
```

- class `Employee` with `__init__` that sets `name`, `hours` and `rate` [B1] [B1]
- `Employee.Pay` returns `hours * rate` [B1]
- `class Manager(Employee)` shows inheritance [B1]
- `Manager.__init__` calls `super().__init__` with the three parent values [B1]
- `Manager.__init__` stores the extra attribute `bonus` [B1]
- `Manager.Pay` overrides the method [B1]
- `Manager.Pay` uses `super().Pay()` and adds the bonus [B1]
- the three objects are created and put in one list [B1]
- a loop calls `Pay()` for each object, so the right method runs for each class [B1]
- each line is output in the format required, with pay 800, 770 and 1350 [B1]
- the total pay is accumulated and output, 2920 [B1]

Q: [4 marks] ★★ State the output of this program.

```python
values = [4, 7, 1, 9]
total = 0
for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        total = total + values[i]
print(total)
print(values[len(values) - 1], values[-2])
```

H: The loop starts at index 1, so the first value, 4, is only ever compared and never added.
A: The output is:

```output
16
9 1
```

- i = 1: 7 > 4, so total becomes 7 [B1]
- i = 2: 1 is not greater than 7, so the total stays 7; i = 3: 9 > 1, so the total becomes 16 [B1]
- the first line is 16 [B1]
- `values[len(values) - 1]` is the last item, 9, and `values[-2]` is the second last, 1 [B1]

Q: [3 marks] ★ A Paper 4 has 75 marks and lasts 150 minutes. (a) Calculate the average time per mark. (b) For a question worth 25 marks, how long is that on average? (c) Give one reason why you should not spend all of your time on the question you find hardest.
A: One mark each.

- (a) \(150 \div 75 = 2\) minutes per mark [B1]
- (b) \(25 \times 2 = 50\) minutes [B1]
- (c) any one: the other questions would be left unfinished and each part is worth marks, so a hard part can cost the marks of easier parts; moving on and returning later earns more [B1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ The text file `Orders.txt` holds one order per line: the order number, the city and the amount, separated by commas. It holds these lines.

```text
101,Quito,40
102,Lima,15
103,Quito,25
104,Bogota,60
105,Lima,35
```

Write a Python program that reads the file and writes each order to a text file named after its city (`Quito.txt`, `Lima.txt`, `Bogota.txt`), then outputs the name and total amount of each city. Handle a missing `Orders.txt` with a message.
H: Open the city's file in append mode (`"a"`) each time an order is read, with `city + ".txt"` as the name.
H: Keep the city names and their totals in two lists, adding a city the first time you see it.
A: One possible answer:

```python
with open("Orders.txt", "w") as file:
    file.write("101,Quito,40\n102,Lima,15\n103,Quito,25\n104,Bogota,60\n105,Lima,35\n")

cities = []
totals = []
try:
    with open("Orders.txt", "r") as file:
        for line in file:
            number, city, amount = line.strip().split(",")
            with open(city + ".txt", "a") as target:
                target.write(line.strip() + "\n")
            if city not in cities:
                cities.append(city)
                totals.append(0)
            position = cities.index(city)
            totals[position] = totals[position] + int(amount)
except FileNotFoundError:
    print("Orders.txt was not found")

for i in range(len(cities)):
    print(cities[i], totals[i])
with open("Quito.txt", "r") as file:
    print(file.read(), end="")
```

```output
Quito 65
Lima 50
Bogota 60
101,Quito,40
103,Quito,25
```

- file opened for reading inside a `try` with `except FileNotFoundError` and a message [B1]
- each line stripped and split into three fields [B1]
- the city file opened in append mode, with the name built as `city + ".txt"` [B1]
- the order written to the city's file with a newline [B1]
- a new city added to the list of cities (with a total of 0) the first time it is seen [B1]
- the amount converted with `int()` and added to that city's total [B1]
- every city and its total output [B1]
- the totals are correct: Quito 65, Lima 50, Bogota 60 [B1]

Q: [6 marks] ★★★ This program should output the average of the marks in the list, ignoring marks below 0, but it has three errors. Find them and write the corrected program.

```text
marks = [72, -1, 58, 90, 64]
total = 0
count = 0
for i in range(1, len(marks)):
    if marks[i] >= 0:
        total = total + marks[i]
        count = count + 1
sum = total / count
print("Average: " + sum)
```

H: Compare the loop's range with the indexes of the list.
H: One error is a built-in name, and one is joining a string and a number.
A: The program has three faults.

- the loop starts at index 1, so `marks[0]` (72) is never used; it should be `range(len(marks))` [B1]
- the variable name `sum` replaces the built-in function `sum`; use a name such as `average` [B1]
- `"Average: " + sum` joins a string and a number, which raises a `TypeError`; use `print("Average:", average)` [B1]

A corrected program is:

```python
marks = [72, -1, 58, 90, 64]
total = 0
count = 0
for i in range(len(marks)):
    if marks[i] >= 0:
        total = total + marks[i]
        count = count + 1
average = total / count
print("Average:", average)
```

```output
Average: 71.0
```

- loop over all indexes, so the first mark is included [B1]
- the average is stored in a name that does not shadow a built-in [B1]
- the average output without joining a string to a number, giving 71.0 [B1]
:::

:::quiz
? A Paper 4 task says the array is called `Queue` and the pointer is `HeadPointer`. What should you use in your program?
- `queue` and `head_pointer`, because Python style uses lower case
+ `Queue` and `HeadPointer`, exactly as in the task
- any names, as long as the program works
- `Q` and `H`, to save typing
> The task's names may be relied on by later parts or by the examiner's checks, so keep them exactly, including capital letters.
? What does `"Computer"[2:6]` give?
- `"ompu"`
+ `"mput"`
- `"mpute"`
- `"Comp"`
> A slice `[2:6]` starts at index 2 and stops before index 6, so it takes the characters at indexes 2, 3, 4 and 5: m, p, u, t.
? Which Python statement is the match for the pseudocode `FOR I ← 1 TO 5`?
- `for i in range(1, 5):`
+ `for i in range(1, 6):`
- `for i in range(5):`
- `for i in range(0, 5):`
> `range` stops before its end value, so 1 to 5 inclusive needs 6. `range(5)` runs 0 to 4, and `range(1, 5)` stops at 4.
? A function contains `Count = Count + 1`, where `Count` was created outside the function. What happens without `global Count`?
- The global value goes up by one.
+ Python raises an `UnboundLocalError`.
- Python creates a second copy of the function.
- Nothing: Python ignores the line.
> Assigning inside a function makes `Count` a local variable for the whole function, so reading it before it has a value fails.
? Which error does the last line of a traceback `IndexError: list index out of range` point to?
- a wrong file name
- a missing colon
+ an index larger than the last index of the list
- a wrong type
> An `IndexError` means the index does not exist. The list may be shorter than you expect, or the code may be off by one.
? What is the Python equivalent of the pseudocode `REPEAT … UNTIL Value > 100`?
- `while value > 100:`
- `while value <= 100:` with the test before the body
+ `while True:` with `if value > 100: break` at the end of the body
- `for value in range(100):`
> `REPEAT` always runs the body at least once and tests at the end. The `while True` with a `break` copies that. The other `while` forms test first, so they could skip the body.
? A teacher says that Paper 4 has 75 marks in 150 minutes. How long, on average, should a 30-mark question take?
- 30 minutes
- 45 minutes
+ 60 minutes
- 75 minutes
> The average is \(150 \div 75 = 2\) minutes per mark, so \(30 \times 2 = 60\) minutes.
:::

:::checklist What you can now do
- [ ] I can read a Paper 4 task, use its names and sizes exactly, and match its output.
- [ ] I can follow the Paper 4 procedure: save files with the given names, paste code into the evidence document and screenshot the output.
- [ ] I can create global 1D and 2D lists, records as classes, and arrays of records in Python.
- [ ] I can use `global` correctly when a function changes a global variable.
- [ ] I can handle strings with slices, `split`, `strip`, `upper`, `isdigit`, `ord`, `chr`, f-strings and `round`.
- [ ] I can translate every pseudocode construct and insert function into Python, and back.
- [ ] I can write an input validation loop and read, split and write text files.
- [ ] I can read a traceback from the bottom up and name the likely cause of the common errors.
- [ ] I can test a program with normal, boundary and erroneous data and plan my time for 2 hours 30 minutes.
:::

:::recap
- **Paper 4**: 2 hours 30 minutes, 75 marks, about 2 minutes per mark; Python in console mode; save programs with the given names; paste code and screenshots into the evidence document; carry out every instruction.
- Use the task's identifiers and array sizes exactly. A 1-based array is a list with index 0 unused, or an index reduced by 1: say which and be consistent.
- Lists: `[0] * n`, and `[[0] * c for _ in range(r)]` for 2D (never `[[0] * c] * r`). A record is a class with `__init__`. A function that assigns a global variable needs `global`.
- Strings: `s[a:b]`, `split`, `strip`, `upper`, `isdigit`, `ord`, `chr`, `str`, `int`, `float`, f-strings, `round`. `input()` returns a string.
- Translation: `DIV` is `//`, `MOD` is `%`, `MID(S, X, Y)` is `s[x - 1:x - 1 + y]`, `REPEAT … UNTIL` is `while True` with `break`, `BYREF` is a returned value, `INHERITS` is `class B(A):`.
- Read a traceback from the last line up. Do not name variables after built-ins (`list`, `max`, `sum`, `input`).
- Test normal, boundary and erroneous data, run the saved program, and screenshot the final run.
:::

:::links
- practise: [Programming basics: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/programming-basics/exam-questions/) · Save My Exams · 9618-style programming questions with mark schemes [paid]
- papers: [9618 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-4/) · Physics & Maths Tutor · real Paper 4 tasks to practise against the clock [unofficial]
- read: [The Python tutorial](https://docs.python.org/3/tutorial/) · Python.org · the official guide to lists, strings, functions and classes
- read: [Python lessons](https://www.w3schools.com/python/) · W3Schools · short lessons with try-it boxes on every topic here
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · step through a program from this chapter and watch the variables change
- practise: [Exercism Python](https://exercism.org/tracks/python) · Exercism · free exercises with feedback

Links checked 13 November 2026.
:::

Next: [Paper 1 guide: Theory Fundamentals](#cs.exam.p1)
