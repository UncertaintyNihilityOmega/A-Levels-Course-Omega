@chapter cs.testing
@title Testing, errors and maintenance
@level as
@paper CAIE 9618 Paper 2
@time 4–6 hours
@summary How faults get into programs and how to avoid them, how to tell syntax, logic and run-time errors apart and find a logic error with a dry run, the methods of testing (white-box, black-box, integration, stub, alpha, beta, acceptance), how to choose normal, abnormal and extreme/boundary test data and write a test plan, and how and why programs are maintained and amended.

:::why
Every program has mistakes in it when it is first written, and a program that is wrong in even one rare case can lose a customer's money or a patient's safety. Testing is how programmers find the mistakes before users do, and maintenance is how a program is kept correct and useful afterwards. Paper 2 asks you to find errors in given pseudocode, to choose test data, to name testing methods and to say what a change to a program should be called, so these are marks you can win by knowing the vocabulary and practising the method.
:::

**Before you start**, you should know the three kinds of error from [Programming from zero](#cs.f.basics), how to complete a trace table from [Computational thinking and algorithms](#cs.algorithms), and the stages of the life cycle from [The development life cycle and program design](#cs.development).

:::try Warm-up
Q: What is a trace table used for? (from [Programming from zero](#cs.f.basics))
A: It records the value of every variable (and any output) as an algorithm is followed by hand, one row each time a value changes, so you can see what the algorithm does and find mistakes without running it.
Q: What is the difference between validation and verification? (from [Security, privacy and data integrity](#cs.security))
A: Validation checks that data is reasonable and allowed (for example a range check). Verification checks that data entered is the same as the source (for example typing it twice).
Q: Name the stage of the life cycle that comes after coding and the stage that comes after release. (from [The development life cycle and program design](#cs.development))
A: Testing comes after coding, and maintenance comes after release.
:::

## Faults: avoiding them and exposing them

A mistake in a program is called a fault (or a bug), and finding and removing faults is called debugging. There are two ways to deal with faults. You can try not to put them there, and you can find the ones that get in anyway.

### Avoiding faults

Most faults can be avoided by good habits at the design and coding stages.

:::key Ways of avoiding faults
- **Good design first.** Write the algorithm and a structure chart before coding, so the logic is planned and each module has one job (see [The development life cycle and program design](#cs.development)).
- **Modular programs.** Small procedures and functions are easier to understand and test than one long program, and a tested module can be reused.
- **Meaningful identifiers** such as `TotalScore`, not `T`, and **constants** such as `CONSTANT Rate = 0.2` instead of repeating a number, so the program says what it means and a change is made in one place.
- **Comments and indentation** that show the structure, so the programmer (and the next programmer) can read the logic and spot what is wrong.
- **Validation of input** so that bad data is rejected before it reaches the calculation, and checks that guard dangerous operations (test that a divisor is not zero, that an index is inside the array's bounds).
- **Follow the language's rules**, and let the translator and editor help: declare every variable, and use the same style throughout.
- **Review by others.** A second pair of eyes reading the design or the code (a walkthrough) finds mistakes the writer cannot see.
:::

### Exposing faults

The faults that remain are exposed by running the program with test data (the rest of this chapter), by following the algorithm by hand with a trace table, and by the tools in a programming environment. The translator reports syntax errors with a line number. A debugger lets a programmer set a **breakpoint** that stops the program at a chosen line, **step** through one line at a time and **watch** the values of variables change, which is a computer doing the work of a trace table. [System software: operating systems and translators](#cs.software) describes these tools.

## Syntax, logic and run-time errors

You met the three kinds of error in [Programming from zero](#cs.f.basics). Here they are in the exam wording, with what causes them and how each is found.

:::def Syntax error
A mistake in the grammar of the language, such as a missing keyword or bracket or a misspelt command, which breaks the rules of the language so that the translator cannot translate the program and it will not run.
:::

:::def Logic error
A mistake in the logic of the program or algorithm, such as a wrong condition or formula or a statement in the wrong place. The program runs without stopping but gives wrong results.
:::

:::def Run-time error
An error that happens while the program is running, when it tries to do something impossible with the data it has, such as dividing by zero or reading outside the bounds of an array. The program stops (crashes).
:::

| | Syntax error | Logic error | Run-time error |
|---|---|---|---|
| When it appears | before the program runs, when it is translated | no message: the output is simply wrong | while the program is running |
| Does the program run? | no | yes, to the end | it starts, then stops at the error |
| Who finds it | the translator, with a line number | the tester, by comparing results with what is expected, or a dry run | the system, with an error message, or the tester |
| Pseudocode example | `IF Mark >= 50` with no `THEN`; `OUTPUT "Total" Total` with no comma | `IF Age > 18` when 18-year-olds should be included; `Total / 4` for five items | `Average ← Total / Count` when Count is 0; `Marks[6]` in `ARRAY[1:5]` |
| Python example | `for n in range(3)` with no colon | `a + b / 2` for the mean | `marks[3]` in a list of three; `int("abc")` |

The following Python program meets all three kinds, catching each run-time error so the program carries on and prints its name. The syntax error is found by asking Python to translate a program without running it.

```python
try:
    compile("for count in range(1, 4)\n    print(count)", "program", "exec")
except SyntaxError as error:
    print("SyntaxError:", error.msg)
marks = [14, 17, 12]
try:
    print(marks[3])
except IndexError as error:
    print("IndexError:", error)
try:
    print(sum(marks) / (len(marks) - 3))
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)
try:
    print(int("12.5"))
except ValueError as error:
    print("ValueError:", error)
try:
    print("Total: " + 5)
except TypeError as error:
    print("TypeError:", error)
try:
    print(totl)
except NameError as error:
    print("NameError:", error)
print("Mean:", marks[0] + marks[1] + marks[2] / len(marks))
```

Output:

```output
SyntaxError: expected ':'
IndexError: list index out of range
ZeroDivisionError: division by zero
ValueError: invalid literal for int() with base 10: '12.5'
TypeError: can only concatenate str (not "int") to str
NameError: name 'totl' is not defined
Mean: 35.0
```

The first line is a syntax error: the loop header has no colon. The next five are run-time errors, each named by Python. The last line is a logic error: the program ran and printed an answer, but `a + b + c / 3` divides only the last mark, so 35.0 is wrong; the mean of 14, 17 and 12 is \(43 \div 3\). Without the try statements, each run-time error would end the program with a traceback, like this one:

```text
Traceback (most recent call last):
  File "marks.py", line 2, in <module>
    print(marks[3])
IndexError: list index out of range
```

Read a traceback from the bottom: the last line names the error and the line above shows where it happened. (The layout differs a little between Python versions.)

:::warn A crash is not always a syntax error
Students often write "syntax error" for any program that stops. A syntax error stops the program **before it starts**. If the program starts, prints something and then stops with a message, it is a **run-time error**. If it never stops and gives a wrong answer, it is a **logic error**. A run-time error may also appear only for particular data: `Total / Count` works until the first time Count is 0.
:::

:::eg Identifying the type of error (exam style)
State the type of error in each of these statements, and say why. [3 marks]

1. `OUTPUT "Pass mark: " PassMark` (the comma between the items is missing)
2. `Average ← Total / Count`, where the program has just read Count from the user and the user typed 0
3. `IF Mark > 40 THEN OUTPUT "Pass"`, where the rule is that a mark of 40 or more passes

**1.** Syntax error. [B1] The output items must be separated by commas, so the translator cannot understand the statement and the program will not run.

**2.** Run-time error. [B1] The statement is valid, but dividing by zero is impossible, so the program stops when it reaches it with that value.

**3.** Logic error. [B1] The statement is valid and the program runs, but the condition is wrong: a mark of exactly 40 gets no "Pass" although the rule says it should.
:::

## Finding a logic error with a dry run

A syntax error comes with a line number and a run-time error with a message, but a logic error comes with nothing. You find it by comparing what the program does with what it should do. The tool for doing that on paper is the dry run.

:::def Dry run
A method of testing in which a person follows an algorithm or program by hand with chosen test data, writing the value of each variable in a trace table after each step, to see what it does and where it goes wrong without running it on a computer.
:::

:::eg Finding the logic error (exam style)
The array Readings has bounds 1 to 6 and holds the temperature changes 4, −2, 6, 0, 5 and −1. The pseudocode below should output the mean of the readings that are greater than zero.

```pseudocode
DECLARE Readings : ARRAY[1:6] OF INTEGER
DECLARE Index, Total, Count : INTEGER
DECLARE Mean : REAL

Total ← 0
Count ← 0
FOR Index ← 1 TO 6
   IF Readings[Index] > 0 THEN
      Total ← Total + Readings[Index]
   ENDIF
   Count ← Count + 1
NEXT Index
Mean ← Total / Count
OUTPUT "Mean of the positive readings: ", Mean
```

(a) Complete a trace table for this pseudocode. [4 marks]

(b) The program gives the wrong answer. Identify the statement that causes the error and write the corrected statement(s). [2 marks]

**(a)** Give each variable its own column and add a row each time a value changes. Start with the two assignments before the loop, then one row for each pass of the loop.

| Index | Readings[Index] | Total | Count | Mean | OUTPUT |
|---|---|---|---|---|---|
| | | 0 | 0 | | |
| 1 | 4 | 4 | 1 | | |
| 2 | -2 | | 2 | | |
| 3 | 6 | 10 | 3 | | |
| 4 | 0 | | 4 | | |
| 5 | 5 | 15 | 5 | | |
| 6 | -1 | | 6 | | |
| | | | | 2.5 | |
| | | | | | Mean of the positive readings: 2.5 |

- Total starts at 0 and takes the values 4, 10 and 15, only on the passes where the reading is greater than 0 [B1]
- Count takes the values 0, 1, 2, 3, 4, 5, 6 [B1]
- Mean is 2.5 [B1]
- the output line is correct [B1]

**(b)** The three positive readings are 4, 6 and 5, so the correct mean is \(15 \div 3 = 5.0\). The program divides by 6. The statement `Count ← Count + 1` is **inside the loop but outside the IF**, so it counts every reading, not just the positive ones. [B1] It must be moved inside the IF, after the line that adds to Total. [B1]

```pseudocode
FOR Index ← 1 TO 6
   IF Readings[Index] > 0 THEN
      Total ← Total + Readings[Index]
      Count ← Count + 1
   ENDIF
NEXT Index
```

The trace table was the tool that exposed the error: the Count column rose on every row, even the rows where Total did not change. When a column that should follow a condition changes on every row, the statement that changes it is in the wrong place.
:::

The corrected program still has a weakness. If **no** reading is greater than zero, Count stays 0 and `Total / Count` divides by zero, a run-time error. Testing with data that has no positive readings (say −3, 0 and −8) would expose it. A guard fixes it:

```pseudocode
IF Count > 0 THEN
   Mean ← Total / Count
   OUTPUT "Mean of the positive readings: ", Mean
ELSE
   OUTPUT "No positive readings"
ENDIF
```

Here are the faulty program and then the corrected one in Python, using the same six readings.

```python
readings = [4, -2, 6, 0, 5, -1]
total = 0
count = 0
for reading in readings:
    if reading > 0:
        total = total + reading
    count = count + 1
mean = total / count
print("Mean of the positive readings:", mean)
```

Output:

```output
Mean of the positive readings: 2.5
```

The corrected version, as a function, with a second set of data that has no positive readings:

```python
def mean_of_positives(readings):
    total = 0
    count = 0
    for reading in readings:
        if reading > 0:
            total = total + reading
            count = count + 1
    if count > 0:
        return total / count
    return None


print(mean_of_positives([4, -2, 6, 0, 5, -1]))
print(mean_of_positives([-3, 0, -8]))
```

Output:

```output
5.0
None
```

:::tip A method for finding errors in given pseudocode
1. Read the question to see what the code **should** do.
2. Pick small test data and **dry run** it, writing the trace table.
3. Compare each result with what it should be. The first row where they differ is the clue.
4. Check each line for a **syntax** slip (missing THEN, ENDIF, comma), then for a **run-time** risk (index outside the bounds, division by a variable that could be zero, a loop that never ends), then for a **logic** slip (the wrong operator `>` or `>=`, a wrong limit, a statement in the wrong place).
5. Write the line number, the type of error and the corrected line.
:::

## Methods of testing

A program is tested at several levels and by several groups of people. The exam wants you to know each method: what it is, who does it, and when.

:::def Walkthrough
A method of testing in which a programmer, often with colleagues, reads through the design or the code step by step, line by line, explaining what it does, so that errors in the logic are found by discussion without running the program.
:::

Dry runs and walkthroughs are the two methods in which the program is **not** run on a computer. A dry run is usually done by one person with a trace table and chosen data. A walkthrough is done by a group looking at the logic.

### White-box and black-box testing

:::def White-box testing
A method of testing in which the tester can see the code and chooses test data so that every path through the program is executed at least once, that is, every branch of every selection and loop is taken.
:::

:::def Black-box testing
A method of testing in which the tester does not look at the code. Test data is chosen from the specification, and the outputs the program gives are compared with the outputs the specification says it should give.
:::

White-box testing asks "does every part of the code work?" It needs the code, so the programmer or a colleague does it. Black-box testing asks "does the program do what was asked?" It needs only the specification and the program, so the programmer, a separate tester or the user can do it.

Here is a function that turns a mark into a grade.

```pseudocode
FUNCTION Grade(Mark : INTEGER) RETURNS STRING
   IF Mark >= 70 THEN
      RETURN "Distinction"
   ELSE
      IF Mark >= 40 THEN
         RETURN "Pass"
      ELSE
         RETURN "Fail"
      ENDIF
   ENDIF
ENDFUNCTION
```

For **white-box** testing, look at the code. There are three paths, one for each RETURN: the first IF is true; the first IF is false and the second is true; both are false. One test for each path executes every line. The data 85, 55 and 20 do it.

```python
def grade(mark):
    if mark >= 70:
        return "Distinction"
    else:
        if mark >= 40:
            return "Pass"
        else:
            return "Fail"


for mark in [85, 55, 20]:
    print(mark, grade(mark))
```

Output:

```output
85 Distinction
55 Pass
20 Fail
```

For **black-box** testing, ignore the code and use the specification: 70 or more is a distinction, 40 to 69 a pass and below 40 a fail. The values most likely to expose a mistake are the ones at the edges of each band.

| Test data | Expected result |
|---|---|
| 0 | Fail |
| 39 | Fail |
| 40 | Pass |
| 69 | Pass |
| 70 | Distinction |
| 100 | Distinction |

A programmer who wrote `Mark > 70` by mistake would pass all three white-box tests above, yet fail the black-box test for 70. The two methods find different faults, which is why a test strategy uses both.

### Integration, stub, alpha, beta and acceptance testing

:::def Integration testing
Testing of modules that have each already been tested alone, now combined into a larger program, to check that they work together and that the data passed between them is correct.
:::

:::def Stub testing
Testing a module or program before the modules it calls have been written, by replacing each missing module with a stub: a very short module with the same name and parameters that returns a fixed value or a message, so the calling code can be tested.
:::

A stub is useful because the top of a program, which calls the rest, can be tested early. In the parcel program from [The development life cycle and program design](#cs.development), ProcessParcel can be tested before CalculateCharge is finished if a stub stands in for it.

```pseudocode
FUNCTION CalculateCharge(Mass : REAL, Zone : CHAR) RETURNS REAL
   // stub: returns a fixed value so the calling modules can be tested
   RETURN 10.0
ENDFUNCTION
```

The Python version, with the real PrintReceipt module and the stub for the missing function:

```python
def calculate_charge(mass, zone):
    return 10.0


def print_receipt(mass, zone, charge):
    print("Mass:", mass, "kg, zone", zone)
    print("Charge:", charge)


mass = 4.0
zone = "B"
charge = calculate_charge(mass, zone)
print_receipt(mass, zone, charge)
```

Output:

```output
Mass: 4.0 kg, zone B
Charge: 10.0
```

The receipt works with the stub's fixed charge of 10.0, so the programmer knows the receipt code is right. When the real function replaces the stub, **integration testing** checks that the real charge arrives at the receipt correctly.

Three more methods are named after the people who do the testing and the stage of the project.

:::def Alpha testing
Testing of a program by the developers or other staff of the company that is making it, at the development site, before it is released to anyone outside the company.
:::

:::def Beta testing
Testing of a nearly finished program by a selected group of real users outside the company, using it in their own environment, before the program is released to everyone. The users report faults and problems.
:::

:::def Acceptance testing
Testing by the client or customer, usually with their own data in their own environment, to check that the finished program meets the requirements they specified and to decide whether to accept it.
:::

| Method | What is tested | Who tests | When |
|---|---|---|---|
| Dry run | an algorithm, by hand with a trace table | the programmer | during design or after coding |
| Walkthrough | design or code, read through step by step | the programmer and colleagues | during design or coding |
| White-box | every path through the code | the programmer or a colleague who can see the code | after coding each module |
| Black-box | outputs against the specification | a tester, without looking at the code | after coding |
| Stub | a module whose called modules are not yet written | the programmer | while the program is only partly written |
| Integration | modules working together | the programmer or a test team | after the modules are tested alone |
| Alpha | the whole program | the company's own staff | before release outside the company |
| Beta | the nearly finished program | a selected group of real users | after alpha, before general release |
| Acceptance | the finished program against the requirements | the client | at hand-over |

:::exam Alpha, beta and acceptance
Examiners give marks for **who** and **where**. Alpha: by the developer's own staff, at the developer's site. Beta: by a limited group of real users, in their own surroundings. Acceptance: by the client, against the requirements, before they accept (and pay for) the program. Do not say "alpha is the first test". Say who does it.
:::

## Test strategies and test plans

Testing without a plan is guesswork: some parts get tested many times and others never.

:::def Test strategy
An overview of how a whole program will be tested: which methods will be used at which stages, who will do the testing, what environment and tools will be used, and what counts as a pass. It is written near the start of the project.
:::

:::def Test plan
A detailed document, produced in the design stage, that lists every test to be carried out. For each test it gives the purpose, the test data, the type of data and the expected result, with a space for the actual result when the test is run.
:::

The need for both is the same: they make sure every requirement is tested, nothing is forgotten, the tests can be repeated after every change, and the client has evidence that the program works. The expected result is written **before** the test is run, from the specification, so that the tester cannot be tempted to accept whatever the program gives.

A test plan is a table. Here is the start of one for a function that checks that a quantity entered by a user is a whole number from 1 to 100.

| Test | Purpose | Test data | Type | Expected result | Actual result |
|---|---|---|---|---|---|
| 1 | an ordinary value is accepted | 50 | normal | Accepted | |
| 2 | the lowest valid value is accepted | 1 | extreme/boundary | Accepted | |
| 3 | the highest valid value is accepted | 100 | extreme/boundary | Accepted | |

The rest of the plan needs the other kinds of test data.

## Choosing test data

:::def Normal data
Valid data of the kind the program is meant to process, well inside the accepted range. The program should accept it and process it correctly.
:::

:::def Abnormal data
Invalid data that the program should reject, either outside the accepted range or of the wrong data type. A good program gives an error message and does not crash.
:::

:::def Extreme data
Valid data at the very ends of the accepted range: the smallest and largest values the program should accept.
:::

:::def Boundary data
Data on either side of the boundary between acceptable and unacceptable values: the extreme value that should be accepted and the value just beyond it that should be rejected.
:::

The syllabus groups the last two as **extreme/boundary** data, so in a test plan label them that way. For a range of whole numbers from 1 to 100:

| Kind of test data | Values for the range 1 to 100 | Expected result |
|---|---|---|
| Normal | 50 | accepted |
| Extreme/boundary (the ends of the range) | 1 and 100 | accepted |
| Boundary (just outside the range) | 0 and 101 | rejected |
| Abnormal (outside the range, or the wrong type) | −20, 12.5, `ten`, nothing typed | rejected |

Each limit of a range needs a **pair** of tests, one value on each side: 1 is accepted and 0 is rejected; 100 is accepted and 101 is rejected. Programmers make mistakes with limits more than anywhere else, writing `>` where `>=` was meant, and only data on the boundary exposes them.

:::warn Extreme data is valid
The most common mistake is to give 0 or 101 as "extreme" data. Extreme data is **valid**: it is the smallest or largest value that must be accepted. A value just outside the range is abnormal data (and also a boundary test), because the program must reject it. When a question asks for abnormal data, do not give a value that is inside the range.
:::

The complete plan, with the pseudocode of the function under test:

```pseudocode
FUNCTION ValidQuantity(Entry : STRING) RETURNS BOOLEAN
   DECLARE Number : REAL
   IF IS_NUM(Entry) = FALSE THEN
      RETURN FALSE
   ENDIF
   Number ← STR_TO_NUM(Entry)
   IF Number <> INT(Number) THEN
      RETURN FALSE
   ENDIF
   RETURN Number >= 1 AND Number <= 100
ENDFUNCTION
```

| Test | Purpose | Test data | Type | Expected result | Actual result |
|---|---|---|---|---|---|
| 1 | an ordinary value is accepted | 50 | normal | Accepted | |
| 2 | the lowest valid value is accepted | 1 | extreme/boundary | Accepted | |
| 3 | the highest valid value is accepted | 100 | extreme/boundary | Accepted | |
| 4 | the value just below the range is rejected | 0 | abnormal (boundary) | Rejected | |
| 5 | the value just above the range is rejected | 101 | abnormal (boundary) | Rejected | |
| 6 | a negative number is rejected | -20 | abnormal | Rejected | |
| 7 | a number that is not whole is rejected | 12.5 | abnormal | Rejected | |
| 8 | text that is not a number is rejected | ten | abnormal | Rejected | |
| 9 | an empty entry is rejected | (nothing typed) | abnormal | Rejected | |

The Python version of the function, with the plan written as data so the tests run themselves and fill in the "actual result" for us:

```python
def valid_quantity(entry):
    try:
        number = float(entry)
    except ValueError:
        return False
    if number != int(number):
        return False
    return 1 <= number <= 100


plan = [(1, "50", True), (2, "1", True), (3, "100", True), (4, "0", False), (5, "101", False),
        (6, "-20", False), (7, "12.5", False), (8, "ten", False), (9, "", False)]


def run_plan(function):
    passed = 0
    for number, data, expected in plan:
        actual = function(data)
        if actual == expected:
            passed = passed + 1
        else:
            print(f"Test {number}: data {data!r}, expected {expected}, actual {actual}, FAIL")
    print(passed, "of", len(plan), "tests passed")


def valid_quantity_slip(entry):
    try:
        number = float(entry)
    except ValueError:
        return False
    if number != int(number):
        return False
    return 1 < number <= 100


run_plan(valid_quantity)
run_plan(valid_quantity_slip)
```

Output:

```output
9 of 9 tests passed
Test 2: data '1', expected True, actual False, FAIL
8 of 9 tests passed
```

The first run is the correct function: all nine tests pass. The second run is the same function with a slip in the last line, `return 1 < number <= 100`, which wrongly rejects 1 (the first limit should be `>=`, not `>`). Ordinary test data would never notice: 50 is still accepted, and 0, 101 and the others are still rejected. Only the extreme value 1 exposes it. Eight tests pass and one fails, and the failing one is the extreme/boundary test. That is why a test plan always contains them.

:::eg Choosing test data (exam style)
A program for a school in Kigali accepts the age of a pupil as a whole number from 5 to 18 inclusive. Give one value for each type of test data and say what the program should do with it. [5 marks]

Work from the edges of the range outwards.

- Normal: 12 (or any whole number from 6 to 17). The program should accept it. [B1]
- Extreme: 5, the lowest valid age. The program should accept it. [B1]
- Extreme: 18, the highest valid age. The program should accept it. [B1]
- Abnormal (boundary): 4 or 19, just outside the range. The program should reject it with an error message. [B1]
- Abnormal: `twelve` (or 12.5, or −3). The program should reject it, because it is the wrong type or not a whole number or negative. [B1]
:::

## Maintenance

A program is not finished on the day it is released. Faults that testing missed appear, the world around the program changes and users ask for improvements. Updating a program after release is **maintenance**, and for most programs it continues for longer than the original development took. Maintenance is the last stage of the life cycle in [The development life cycle and program design](#cs.development), and it begins the cycle again: a change must be analysed, designed, coded and tested.

There are three types, named by the reason for the change.

:::def Corrective maintenance
Changing a program to find and fix faults, such as logic errors or run-time errors, that appear after the program is in use.
:::

:::def Adaptive maintenance
Changing a program so that it keeps working when its environment or requirements change, for example a new law, a new tax rate, a new operating system, new hardware or a change in how the business works.
:::

:::def Perfective maintenance
Changing a program that works correctly to improve it, for example to make it run faster or use less memory, to make it easier to use, or to add a feature that users have asked for.
:::

| Reason for the change | Type |
|---|---|
| A customer reports that the program crashes whenever a name contains an apostrophe | corrective |
| A government changes the rate of sales tax and the shop's till program must use the new rate | adaptive |
| The program must run on a new model of tablet | adaptive |
| The search of a customer database is rewritten so it takes 2 seconds instead of 20 | perfective |
| Users ask for a button to print the receipt as well as show it on screen | perfective |

:::warn Adaptive or perfective?
Both are changes to a program that works. Ask **why** the change is needed. If something outside the program has changed (a law, a system, a business rule) and the program must keep up, it is adaptive. If nothing outside has changed and the program is simply being made better, it is perfective. If the program was wrong, it is corrective.
:::

## Amending an existing program

Paper 2 often gives you working pseudocode and asks you to change it to do something more: add a new output, a new condition or a new calculation. Writing a new program is not the task. The skill is to understand what is there, find where the change belongs, and make the smallest change that works, in the same style.

:::steps
1. **Read** the code and the comments, and work out what each variable holds. A dry run with small data shows how it works.
2. **Find** the place the new feature belongs: new variables are declared with the others; a new total or count goes in the existing loop if it needs the same values; a new output goes after the loop.
3. **Change as little as possible.** Do not rewrite code that works. Keep the identifier style, the indentation and the data types.
4. **Check** that the new feature works (test data that uses it) and that the old features still give the same answers as before.
:::

:::eg Amending a program (exam style)
A shop's program holds eight prices in the array Prices, with bounds 1 to 8, and outputs their total and how many are over 10.0. It is shown below with the prices 3.5, 12.0, 8.25, 20.0, 4.75, 15.5, 9.0 and 11.0.

```pseudocode
DECLARE Prices : ARRAY[1:8] OF REAL
DECLARE Index, Count : INTEGER
DECLARE Total : REAL

Total ← 0.0
Count ← 0
FOR Index ← 1 TO 8
   Total ← Total + Prices[Index]
   IF Prices[Index] > 10.0 THEN
      Count ← Count + 1
   ENDIF
NEXT Index
OUTPUT "Total: ", Total
OUTPUT "Items over 10.00: ", Count
```

The owner asks for two changes: (a) when the total is over 80.0 a voucher of 5.0 is taken off it before it is output; (b) the program also outputs the position and price of the most expensive item. Write the amended pseudocode. [5 marks]

For (b) the program needs two new variables: the highest price so far and its position, started at the **first** element, and updated inside the existing loop where each price is already being looked at. For (a) the voucher is applied after the loop, once the total is complete, and before the output.

```pseudocode
DECLARE Prices : ARRAY[1:8] OF REAL
DECLARE Index, Count, HighPos : INTEGER
DECLARE Total, Highest : REAL

Total ← 0.0
Count ← 0
Highest ← Prices[1]
HighPos ← 1
FOR Index ← 1 TO 8
   Total ← Total + Prices[Index]
   IF Prices[Index] > 10.0 THEN
      Count ← Count + 1
   ENDIF
   IF Prices[Index] > Highest THEN
      Highest ← Prices[Index]
      HighPos ← Index
   ENDIF
NEXT Index
IF Total > 80.0 THEN
   Total ← Total - 5.0
ENDIF
OUTPUT "Total: ", Total
OUTPUT "Items over 10.00: ", Count
OUTPUT "Most expensive: item ", HighPos, " at ", Highest
```

Mark points:

- new variables for the highest price and its position declared with suitable types [B1]
- Highest initialised to the first element (not 0) and its position to 1 [B1]
- inside the existing loop, compares each price with Highest and stores the price and the index when larger [B1]
- after the loop and before the output, IF Total > 80.0 THEN subtracts 5.0 [B1]
- the original outputs are kept and the new output shows the position and price [B1]

With the data given, the total is 84.0, which is over 80.0, so the output is a total of 79.0, 4 items over 10.0 and the most expensive item is item 4 at 20.0.
:::

The same change in Python, with the original program first and the amended program second.

```python
prices = [3.5, 12.0, 8.25, 20.0, 4.75, 15.5, 9.0, 11.0]
total = 0.0
count = 0
for price in prices:
    total = total + price
    if price > 10.0:
        count = count + 1
print("Total:", total)
print("Items over 10.00:", count)
```

Output:

```output
Total: 84.0
Items over 10.00: 4
```

```python
prices = [3.5, 12.0, 8.25, 20.0, 4.75, 15.5, 9.0, 11.0]
total = 0.0
count = 0
highest = prices[0]
high_pos = 1
for index in range(len(prices)):
    total = total + prices[index]
    if prices[index] > 10.0:
        count = count + 1
    if prices[index] > highest:
        highest = prices[index]
        high_pos = index + 1
if total > 80.0:
    total = total - 5.0
print("Total:", total)
print("Items over 10.00:", count)
print("Most expensive: item", high_pos, "at", highest)
```

Output:

```output
Total: 79.0
Items over 10.00: 4
Most expensive: item 4 at 20.0
```

The old outputs are unchanged apart from the voucher, and the new line is correct: the amendment did not break the existing features. Testing the old features again after a change, as well as the new feature, is always part of maintenance.

## Spot the error, try it yourself and exam practice

:::eg Spot the error: choosing extreme data
Question: A program accepts a score from 0 to 50 inclusive. Give one value of each of these types of test data: normal, extreme and abnormal. [3 marks]

A student wrote:

```text
Normal: 25
Extreme: 51
Abnormal: abc
```

25 is a valid value well inside the range, so it is normal data [B1]. `abc` is the wrong data type and must be rejected, so it is abnormal data [B1]. **51 is outside the range, so it is not extreme data. Extreme data is valid: it is the smallest or largest value the program must accept, which here is 0 or 50. The extreme mark is lost** [B0]. The answer scores 2 out of 3.

The slip is the one the warning above describes. 51 is a good test, but it is an abnormal (boundary) test: it checks that the program rejects the first value above the range. To fix the answer, write `Extreme: 50` (or 0).
:::

:::try Start easy, finish at exam standard
Q: State the type of error: a program has the line `WHILE Count < 10` with no matching ENDWHILE.
A: A syntax error. The translator cannot translate a loop that is never closed, so the program does not run.
Q: A program that adds up 10 numbers uses `FOR Index ← 1 TO 9`. State the type of error.
A: A logic error. The program runs and gives an answer, but it adds only nine numbers.
Q: What is the difference between a dry run and a walkthrough?
A: A dry run follows the algorithm by hand with test data and a trace table to record the variable values. A walkthrough is a group reading through the code or design, step by step, to discuss the logic. Neither runs the program.
Q: Describe white-box testing.
A: The tester can see the code and chooses data so that every path through the program is executed at least once.
Q: A function has three separate paths through its code. What is the least number of tests that executes every statement in white-box testing?
A: Three tests, one for each path.
Q: Which method tests a module before the modules it calls have been written, and what replaces the missing modules?
A: Stub testing. Each missing module is replaced by a stub, a short module with the same name and parameters that returns a fixed value.
Q: A program accepts the number of items ordered, a whole number from 1 to 20. Give one value each of normal data, extreme data and abnormal data.
A: Normal: 10 (any whole number from 2 to 19). Extreme: 1 or 20. Abnormal: 0, 21, −5 or `five`.
Q: A new law requires a payroll program to deduct a new tax. What type of maintenance is this?
A: Adaptive maintenance, because the law, which is outside the program, has changed.
Q: A shop's stock program runs correctly but is slow. The programmer rewrites the sorting section so it runs twice as fast. What type of maintenance is this?
A: Perfective maintenance. The program was correct, and the change improves its performance.
Q: Why is the expected result of a test written in the plan before the test is run?
A: So that the tester compares the program's output with what the specification says it should be, instead of accepting whatever the program gives.
Q: What does a test plan contain for each test?
A: The purpose of the test, the test data, the type of test data (normal, abnormal or extreme/boundary), the expected result and a space for the actual result.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the type of error (syntax, logic or run-time) in each statement. (a) `OUTPUT "Total: ", Total ENDIF` in a program with no IF. (b) A program prints the average of 4 test marks by dividing the total by 5. (c) A program reads a number from a file that does not exist, and stops.
A: One mark for each correct type.

- (a) syntax error, because ENDIF without an IF breaks the grammar of the language [B1]
- (b) logic error, because the program runs but gives wrong results [B1]
- (c) run-time error, because the program stops while it is running [B1]

Q: [6 marks] ★★ (#cs.testing) The pseudocode below should input the five exam marks of a pupil into the array Marks (bounds 1 to 5), then output the mean and output Pass if the mean is at least 50, otherwise Fail. It contains three errors, one of each type: syntax, logic and run-time. For each error, give the line number, the type of the error and a correction.

```pseudocode
01  DECLARE Marks : ARRAY[1:5] OF INTEGER
02  DECLARE Total, Index : INTEGER
03  DECLARE Mean : REAL
04  Total ← 0
05  FOR Index ← 1 TO 5
06     Total ← Total + Marks[Index + 1]
07  NEXT Index
08  Mean ← Total / 4
09  IF Mean >= 50
10     OUTPUT "Pass"
11  ELSE
12     OUTPUT "Fail"
13  ENDIF
```

H: Look for a missing keyword, an index that goes outside the array, and a wrong number in a calculation.
A: Dry run with Marks 20, 30, 40, 50, 60 to see the effect of each error.

- line 06, run-time error: when Index is 5, `Marks[Index + 1]` is `Marks[6]`, outside the bounds of the array [B1]; correct it to `Total ← Total + Marks[Index]` [B1]
- line 08, logic error: the total of five marks is divided by 4, so the mean is too high (for the marks 20, 30, 40, 50, 60 the program would output Pass instead of Fail) [B1]; correct it to `Mean ← Total / 5` [B1]
- line 09, syntax error: the IF has no THEN [B1]; correct it to `IF Mean >= 50 THEN` [B1]

Q: [3 marks] ★ Describe stub testing and state why it is used.
A: One mark for each point.

- a stub is a short module with the same name and parameters as a module that has not been written yet [B1]
- it returns a fixed value or a message instead of doing the real work [B1]
- it lets the modules that call it be tested before the rest of the program is finished [B1]

Q: [5 marks] ★★ A program for a school in Nairobi accepts the number of books a pupil borrows, a whole number from 0 to 8 inclusive. Copy and complete the test plan by giving suitable test data for each row and the expected result.

| Test | Purpose | Type | Test data | Expected result |
|---|---|---|---|---|
| 1 | an ordinary value | normal | | |
| 2 | the lowest valid value | extreme | | |
| 3 | the highest valid value | extreme | | |
| 4 | the value just above the range | abnormal | | |
| 5 | a value of the wrong type | abnormal | | |

H: Extreme data is valid data at the very edge of the range.
A: Any suitable data, with the matching result.

| Test | Purpose | Type | Test data | Expected result |
|---|---|---|---|---|
| 1 | an ordinary value | normal | 4 | accepted |
| 2 | the lowest valid value | extreme | 0 | accepted |
| 3 | the highest valid value | extreme | 8 | accepted |
| 4 | the value just above the range | abnormal | 9 | rejected |
| 5 | a value of the wrong type | abnormal | `five` | rejected |

- normal data inside the range (1 to 7) with the result accepted [B1]
- 0 with the result accepted [B1]
- 8 with the result accepted [B1]
- 9 (or any value above 8) with the result rejected [B1]
- text, or a number with a fractional part, with the result rejected [B1]

Q: [3 marks] ★ State the type of maintenance (corrective, adaptive or perfective) in each case. (a) A hospital's booking program gives two patients the same appointment slot, and a programmer corrects the fault. (b) A country changes its currency, and a shop's program must show prices in the new currency. (c) A programmer rewrites a report routine so that it prints in half the time.
A: One mark for each.

- (a) corrective [B1]
- (b) adaptive [B1]
- (c) perfective [B1]

Q: [6 marks] ★★★ A software company is developing a stock control program for a chain of supermarkets. Describe how alpha testing, beta testing and acceptance testing could each be used for this program.
H: For each, say who tests, where, and what they are checking.
A: Two marks for each method.

- alpha: the company's own programmers or staff test the program [B1] at the company's site before it goes to anyone outside [B1]
- beta: a selected group of real users, such as staff in a few of the supermarkets, use the nearly finished program [B1] in their own stores, with their own stock, and report faults [B1]
- acceptance: the supermarket chain (the client) tests the finished program [B1] with its own data, to check it meets the agreed requirements before it accepts it [B1]

Q: [5 marks] ★★★ The pseudocode below should output the sum of the digits of a whole number, so 472 gives 13. The variable Number is input as 472.

```pseudocode
01  INPUT Number
02  Sum ← 0
03  WHILE Number > 10
04     Sum ← Sum + Number MOD 10
05     Number ← Number DIV 10
06  ENDWHILE
07  OUTPUT Sum
```

(a) Complete a trace table with columns Number, Sum and OUTPUT. [3 marks]

(b) State the line that contains the error and write the corrected line. [2 marks]

H: Do each row by hand. What happens to Number after each pass? When does the loop stop?
A: Follow the algorithm.

| Number | Sum | OUTPUT |
|---|---|---|
| 472 | 0 | |
| 47 | 2 | |
| 4 | 9 | |
| | | 9 |

- Number takes the values 472, 47, 4 [B1]
- Sum takes the values 0, 2, 9 [B1]
- the output is 9 [B1]

(b) Line 03 [B1]. The loop stops when Number is 4, so the last digit is never added. It should be `WHILE Number > 0` [B1]. With this change Sum becomes 2, 9 and 13, which is the sum of the digits.

Q: [6 marks] ★★★ A café in Lima records its sales for the 7 days of a week in the array Sales, with bounds 1 to 7. The pseudocode below outputs the total sales for the week.

```pseudocode
DECLARE Sales : ARRAY[1:7] OF INTEGER
DECLARE Day, Total : INTEGER

Total ← 0
FOR Day ← 1 TO 7
   Total ← Total + Sales[Day]
NEXT Day
OUTPUT "Total sales: ", Total
```

Amend the pseudocode so that it also outputs the number of the day with the highest sales and the number of days on which the sales were more than 100.
H: Add the new variables and put the new statements in the existing loop where you can.
A: One possible answer:

```pseudocode
DECLARE Sales : ARRAY[1:7] OF INTEGER
DECLARE Day, Total, HighDay, DaysOver : INTEGER

Total ← 0
HighDay ← 1
DaysOver ← 0
FOR Day ← 1 TO 7
   Total ← Total + Sales[Day]
   IF Sales[Day] > Sales[HighDay] THEN
      HighDay ← Day
   ENDIF
   IF Sales[Day] > 100 THEN
      DaysOver ← DaysOver + 1
   ENDIF
NEXT Day
OUTPUT "Total sales: ", Total
OUTPUT "Highest sales on day ", HighDay
OUTPUT "Days over 100: ", DaysOver
```

- new variables for the best day and the count declared as INTEGER [B1]
- HighDay initialised to 1 (the first day) and DaysOver to 0 before the loop [B1]
- the new tests are inside the existing loop, not a second copy of it [B1]
- compares each day's sales with the highest so far and stores the day number [B1]
- counts the days with sales above 100 [B1]
- the original total and its output are unchanged, and the new values are output after the loop [B1]

With the sales 120, 80, 150, 95, 110, 60 and 175 the output is a total of 790, highest sales on day 7 and 4 days over 100.
:::

:::try Stretch for A*
Q: A function ValidPassword accepts a password if it has from 8 to 12 characters inclusive and contains at least one digit. Design a test plan of eight tests that checks each of the two conditions on its own and at the limits of the length. Give the test data, the type of each test and the expected result.
H: A test that fails only one condition shows that condition is checked. Which tests are needed at each end of the length range?
H: Remember that the number of characters, not the characters themselves, sets the boundary.
A: Each test is chosen so that the result depends on one thing.

| Test data | Length | Has a digit | Type | Expected result |
|---|---|---|---|---|
| `summer25xy` | 10 | yes | normal | accepted |
| `abcdefg1` | 8 | yes | extreme | accepted |
| `abcdefghij12` | 12 | yes | extreme | accepted |
| `abcdef1` | 7 | yes | abnormal (boundary) | rejected |
| `abcdefghijk12` | 13 | yes | abnormal (boundary) | rejected |
| `abcdefgh` | 8 | no | abnormal | rejected |
| `12345678` | 8 | yes | normal | accepted |
| (nothing typed) | 0 | no | abnormal | rejected |

The tests at 7 and 13 characters fail only the length condition, and `abcdefgh` fails only the digit condition. The test `12345678` shows that a password made only of digits is accepted, because the rule asks for at least one digit and nothing about letters. A test of an empty entry checks that the program does not crash when it is given nothing.

Q: The function below calculates the cost of sending a parcel.

```pseudocode
FUNCTION Shipping(Mass : REAL, Express : BOOLEAN, Remote : BOOLEAN) RETURNS REAL
   DECLARE Cost : REAL
   Cost ← 5.0
   IF Mass > 10.0 THEN
      Cost ← Cost + 4.0
   ENDIF
   IF Express = TRUE THEN
      Cost ← Cost * 2
   ENDIF
   IF Remote = TRUE THEN
      Cost ← Cost + 3.0
   ENDIF
   RETURN Cost
ENDFUNCTION
```

(a) What is the smallest number of tests that executes every statement at least once, and what data would you use? (b) How many different paths are there through the function? (c) What does `Shipping(12.0, TRUE, FALSE)` return?
H: A path is a combination of choices. How many choices does each IF make?
A: (a) One test executes every statement: all three conditions must be true, for example Mass 12.0, Express TRUE and Remote TRUE, which returns \((5.0 + 4.0) \times 2 + 3.0 = 21.0\). (b) Each of the three IFs can be true or false, independently, so there are \(2 \times 2 \times 2 = 8\) paths. (c) The mass is over 10.0, so Cost becomes 9.0; Express doubles it to 18.0; Remote is FALSE so nothing is added: the function returns 18.0.

Testing every statement is a weaker test than testing every path. In the answer to (a), the one test never takes the false branch of any IF, so a fault in the code that runs only when Express is FALSE would not be seen. Testing every path would need all 8 combinations, which is why large programs are tested module by module.
:::

:::quiz
? A program stops while running, with the message "list index out of range". What type of error is this?
- syntax error
- logic error
+ run-time error
- compile error
> The program was valid and started, but it tried to use an element outside the list while running. A syntax error would have stopped it from starting, and a logic error gives wrong results without stopping.
? A program prints "Pass" for a mark of exactly 50, but the specification says 50 should be a fail. The code is `IF Mark >= 50`. Which type of error is this?
- syntax error
+ logic error
- run-time error
- none, because the program ran
> The program runs and gives no message, but the condition is wrong: it should be `Mark > 50`. Only a comparison with what the program should do exposes a logic error.
? What is the main difference between white-box and black-box testing?
- White-box testing is done by users and black-box testing by programmers.
+ White-box testing uses the code to make every path run, and black-box testing uses only the specification and compares outputs with expected outputs.
- Black-box testing needs a trace table.
- White-box testing is done only after the program is released.
> In white-box testing the tester can see the code and chooses data to exercise each path. In black-box testing the code is hidden and the data is chosen from what the program is supposed to do.
? A range check accepts whole numbers from 10 to 99. Which value is extreme data?
- 9
- 50
+ 99
- 100
> Extreme data is valid and at the edge of the range, so 99 (or 10). 9 and 100 are just outside the range, so they are abnormal (boundary) data, and 50 is normal data.
? Why are stubs used?
- To speed up the final program.
- To check that data entered is the same as the source.
+ To stand in for modules that are not yet written, so that the modules that call them can be tested.
- To make the program easier for users to read.
> A stub has the same name and parameters as the missing module and returns a fixed value, so the calling code can be tested before the missing module exists.
? Who carries out alpha testing?
- a selected group of real users outside the company
+ the developers or staff of the company making the program, before release outside the company
- the client, to check the requirements
- nobody, because it is done automatically
> Alpha testing is in-house. Beta testing is by a selected group of real users outside the company, and acceptance testing is by the client against the requirements.
? A bank changes its program so that it follows a new rule about how customer data is stored. Which type of maintenance is this?
- corrective
- perfective
+ adaptive
- preventive
> The change is needed because something outside the program (a rule) has changed, and the program must keep working, so it is adaptive. Corrective fixes faults, and perfective improves a correct program.
? In a test plan, when is the expected result written?
- after the test has been run, using the actual result
+ before the test is run, from the specification
- only if the test fails
- it is not needed, because the program shows the result
> The expected result comes from the specification and is written first, so that the tester judges the program against what it should do and not against what it does.
:::

:::checklist What you can now do
- [ ] I can describe ways of avoiding faults in programs and ways of exposing them.
- [ ] I can identify syntax, logic and run-time errors in pseudocode and in Python.
- [ ] I can find a logic error with a dry run and a trace table and correct it.
- [ ] I can explain dry run, walkthrough, white-box, black-box, integration and stub testing.
- [ ] I can explain alpha, beta and acceptance testing and say who carries out each.
- [ ] I can explain why a test strategy and a test plan are needed and what a test plan contains.
- [ ] I can choose normal, abnormal and extreme/boundary test data for a range and for a data type.
- [ ] I can write a test plan with test data, the type of data and the expected results.
- [ ] I can explain the need for maintenance and state whether a change is corrective, adaptive or perfective.
- [ ] I can analyse an existing program and amend it to add functionality in the same style.
:::

:::recap
- Avoid faults with design before coding, modules, meaningful names, comments, constants and validation. Expose them with testing, dry runs and a debugger's breakpoints, stepping and watches.
- Syntax error: breaks the grammar, found before the program runs. Logic error: runs but gives wrong results, found by testing or a dry run. Run-time error: the program stops while running, such as division by zero or an index outside the bounds.
- A dry run follows the algorithm by hand with a trace table. A column that changes on every row when it should change only sometimes points to a statement in the wrong place.
- White-box testing uses the code and tries every path. Black-box testing uses the specification only. Integration testing combines tested modules. Stub testing replaces unwritten modules with fixed-value stubs.
- Alpha: the company's own staff. Beta: selected real users outside the company. Acceptance: the client, against the requirements.
- A test strategy is the overall approach, and a test plan lists each test: purpose, test data, type, expected result, actual result. Expected results are written first.
- Normal data is valid and typical. Extreme/boundary data is valid at the ends of the range, with the value just outside the limit as the matching boundary test. Abnormal data is invalid and must be rejected.
- Maintenance: corrective fixes faults, adaptive keeps up with changes outside the program, perfective improves a correct program. When amending a program, make the smallest change in the same style and recheck the old features.
:::

:::links
- practise: [Program testing and maintenance: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/12-software-development-/program-testing-and-maintenance/exam-questions/) · Save My Exams · 9618-style questions on testing, test data and maintenance with mark schemes [paid]
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · step through a program line by line and watch every variable, like a computer trace table
- read: [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html) · Python.org · the official tutorial on syntax errors and run-time errors (exceptions)
- read: [Python try and except](https://www.w3schools.com/python/python_try_except.asp) · W3Schools · short lessons on catching run-time errors, with try-it boxes
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations of testing and the software development life cycle

Links checked 13 November 2026.
:::

Next: [User-defined types, file organisation and hashing](#cs.usertypes)
