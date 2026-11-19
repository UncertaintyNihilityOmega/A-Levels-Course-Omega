@chapter cs.exam.p2
@title Paper 2 guide: Problem-solving and Programming
@level guide
@paper CAIE 9618 Paper 2
@time 2–3 hours
@summary What Paper 2 prints and allows, what the insert contains, how to share 120 minutes across 75 marks, how to write pseudocode that earns a mark for every feature, the question types the paper uses, three model answers (a trace table, a function and a file-processing procedure) and a marked student answer, the slips that lose marks, and a revision plan that links every Paper 2 chapter.

:::why
Paper 2 is the programming paper for AS Level, and you answer it on paper, in pseudocode. There is no computer to run your code and no compiler to catch a mistake, so the marks go to students who write clear, correct pseudocode in the Cambridge style and check it by hand. This guide shows what the paper contains, how pseudocode is marked, and how to avoid the slips that cost the most.
:::

## The paper at a glance

| Feature | Paper 2 |
|---|---|
| Title | Fundamental Problem-solving and Programming Skills |
| Time | 2 hours |
| Marks | 75 |
| Syllabus content | sections 9 to 12 (computational thinking and algorithms, programming, data types and structures, software development) |
| Weighting | 50% of AS Level, 25% of A Level |
| Where you answer | on the question paper, in **pseudocode** (you are not asked to write programming code) |
| Supplied with the paper | the **insert**, which lists the pseudocode functions and operators |

The front page of the May/June 2025 paper (9618/21) said "You will need: Insert (enclosed)" and that the insert contains all the resources referred to in the questions. It also said that **calculators must not be used** and that no marks are awarded for brand names of software packages or hardware. That paper had 20 pages and 7 questions, 75 marks in all. Every question started with "Refer to the insert for the list of pseudocode functions and operators" and was built on a scenario, ending with a long question that joined several modules together. Treat that as an example of the style, not a rule for every series.

The assessment objectives for Paper 2 are 40% AO2 (applying knowledge to analyse a problem) and 60% AO3 (designing, programming and evaluating). Most of the marks are for **doing** something: writing, completing, tracing or correcting an algorithm. Facts to recall matter less than in Paper 1.

## The insert

The insert is part of the paper: you may use everything on it, and you never need to remember how a function works. In the May/June 2025 paper it listed, with examples:

| Group | What it contained |
|---|---|
| String and character functions | `LEFT`, `RIGHT`, `MID(ThisString, x, y)` (y characters starting at position x), `LENGTH`, `TO_UPPER` and `TO_LOWER` (for a CHAR or a STRING), `NUM_TO_STR`, `STR_TO_NUM`, `IS_NUM`, `ASC` (the ASCII value of a character), `CHR` (the character with an ASCII value) |
| Numeric functions | `INT(x)` (the integer part of x), `RAND(x)` (a random real number from 0 up to but not including x) |
| Date functions (dates are DD/MM/YYYY) | `DAY`, `MONTH`, `YEAR`, `DAYINDEX` (Sunday is 1), `SETDATE(Day, Month, Year)`, `TODAY()` |
| Text file function | `EOF(FileName)`, which is TRUE if there are no more lines to read (an error if the file is not open for reading) |
| Operators | `&` (joins strings), `AND`, `OR`, `NOT`, `MOD` (10 MOD 3 is 1), `DIV` (10 DIV 3 is 3), and the comparisons `=`, `>`, `<`, `>=`, `<=`, `<>` |

The insert also states some rules that examiners test. A string of length 1 may be used as a CHAR or as a STRING. A CHAR may be assigned to or joined to a STRING, but a STRING longer than one character cannot be assigned to a CHAR. Comparisons of CHARs and STRINGs are case sensitive. REAL and INTEGER values may be compared, but records cannot. An error is generated if a function call is badly formed or an operator receives a value of the wrong type.

:::exam Read the insert once, early
Spend the first two minutes of the exam looking at the insert so you know which functions exist and what they are called. The names in this course follow the insert: `TO_UPPER`, not `UCASE`. A question that needs any other function defines it in the question. Use only the functions printed.
:::

## Spending 120 minutes on 75 marks

There are 120 minutes for 75 marks, so each mark is worth \(120 \div 75 = 1.6\) minutes. Programming takes longer than recall, and the pace is slower than in Paper 1.

| Marks | Minutes at 1.6 per mark | Round to |
|---|---|---|
| 4 | 6.4 | 6 |
| 6 | 9.6 | 10 |
| 8 | 12.8 | 13 |
| 10 | 16.0 | 16 |
| 12 | 19.2 | 19 |

Plan to finish with about **ten minutes** in hand. Use them to walk through each algorithm you wrote with one test value: the dry run of your own answer finds more mistakes than reading it again.

:::steps
1. **Read the whole question** and its scenario. The identifiers it names (`Names`, `HeadPointer`, `Total`) are the ones to use.
2. **Plan first** for a long answer: write a short outline in the margin ("loop 1 to 30; test; count") before the pseudocode.
3. **Write neatly with space.** Leave room between lines; examiners must read indentation.
4. **Do not rewrite.** Cross out a wrong line with one line, and write the corrected line next to it. A tidy answer with a crossed-out slip scores the same as a perfect one.
5. **Dry run** the algorithm with one value at the end.
:::

## How to write pseudocode for marks

A mark scheme for a "write pseudocode" question lists the **features** an algorithm needs, one mark each. A partly correct answer therefore still scores: each feature present earns a mark, even if another is missing. The skill is to make every feature easy to see.

:::key Pseudocode conventions that the papers expect
- **Keywords in capitals**: `IF`, `THEN`, `ELSE`, `ENDIF`, `FOR`, `TO`, `NEXT`, `WHILE`, `ENDWHILE`, `REPEAT`, `UNTIL`, `CASE OF`, `ENDCASE`, `FUNCTION`, `ENDFUNCTION`, `PROCEDURE`, `ENDPROCEDURE`, `RETURN`, `CALL`.
- **Assignment with `←`**: `Total ← Total + Price`. Write `=` only to compare, and in `CONSTANT Rate = 0.2`.
- **Declare** variables with their type: `DECLARE Count : INTEGER`. Arrays: `DECLARE Scores : ARRAY[1:30] OF INTEGER`. Declarations are good practice, and some questions ask for them.
- **Indent** by about three spaces inside every `IF`, loop and module; close each structure with its closing keyword, and repeat the identifier in `NEXT Index`.
- **Identifiers**: meaningful, letters, digits and underscore only, starting with a letter (`NumberOfPlayers`, `TotalScore`), never a single letter that tells the reader nothing.
- **Comments** begin `//` and explain a step that is not obvious. They never earn marks by themselves.
- **Input and output**: `INPUT Answer`; `OUTPUT "Total: ", Total`.
- **Modules**: a procedure is run with `CALL Name(...)`; a function is used inside an expression and is **never** called with `CALL`. A function ends with `RETURN` a value. Parameters are by value unless marked `BYREF`.
- **Text files**: `OPENFILE`, `READFILE`, `WRITEFILE`, `EOF` and `CLOSEFILE`, as in [Text files, stacks, queues and linked lists](#cs.structures).
:::

Three habits make the marks easy to award.

1. **Use the insert's functions exactly.** `MID(Name, 1, 1)` takes the first character. Do not invent `Name[1]`, `Name.length` or `substring`.
2. **Write efficient algorithms.** A question that asks for "efficient" pseudocode wants the loop to stop when its job is done (a `WHILE` or `REPEAT` that ends when the item is found), not a `FOR` that always runs to the end. See [Data types, records and arrays](#cs.datatypes).
3. **Use the scenario's names and types.** If the question declares `Names` as an array, use `Names`, not your own list.

:::tip Mark schemes accept alternatives
Cambridge mark schemes award marks for any correct way of doing the job. A `REPEAT … UNTIL` loop for a task where the mark scheme shows a `WHILE` loop is fine if it works. Write the version you are most sure of.
:::

## What the paper asks

| Question type | What to do | Chapter |
|---|---|---|
| **Identifier table** | name each variable, constant or array, its data type and a description | [Computational thinking and algorithms](#cs.algorithms) |
| **Flowchart to pseudocode, or the reverse** | turn each symbol into a statement; a diamond is a decision (an `IF` or a loop condition); find a logic error | [Computational thinking and algorithms](#cs.algorithms) |
| **Trace table (a dry run)** | one column per variable plus OUTPUT, one row per change, blank when unchanged | [Computational thinking and algorithms](#cs.algorithms), [Testing, errors and maintenance](#cs.testing) |
| **Write or complete a function or procedure** | header with parameters and RETURNS, the algorithm, RETURN | [Procedures, functions and parameters](#cs.procedures) |
| **Arrays and records** | totals, counts, highest, search, bubble sort, 2D tables | [Data types, records and arrays](#cs.datatypes) |
| **Stacks, queues and linked lists** | trace pushes and pops with pointers; show the structure after operations | [Text files, stacks, queues and linked lists](#cs.structures) |
| **Text-file processing** | read each line, convert, calculate, write to another file, close both | [Text files, stacks, queues and linked lists](#cs.structures) |
| **Structure charts and module descriptions** | which module calls which, what passes between them; write the modules | [The development life cycle and program design](#cs.development) |
| **Testing and test data** | normal, abnormal and extreme or boundary data with expected results; types of error | [Testing, errors and maintenance](#cs.testing) |
| **Amend a given program** | read the code, find the line, change only what is asked | [Testing, errors and maintenance](#cs.testing) |

## Three model answers

After each answer is the mark scheme, one `[B1]` for each feature. Notice how the answers use the scenario's names, declare their variables and close every structure.

:::eg Trace table: the even digits
A program totals the even digits of a number. Complete the trace table for this pseudocode. Write a value in a row only when the variable changes. [5 marks]

```pseudocode
DECLARE Number, Digit, Total : INTEGER

Number ← 4683
Total ← 0
WHILE Number > 0
   Digit ← Number MOD 10
   IF (Digit MOD 2) = 0 THEN
      Total ← Total + Digit
   ENDIF
   Number ← Number DIV 10
ENDWHILE
OUTPUT "Even total: ", Total
```

`Number MOD 10` is the last digit, and `Number DIV 10` removes it. Follow the program one statement at a time. When the digit is odd, the `IF` is false and Total does not change, so that row stays blank.

| Number | Digit | Total | OUTPUT |
|---|---|---|---|
| 4683 | | | |
| | | 0 | |
| | 3 | | |
| 468 | | | |
| | 8 | | |
| | | 8 | |
| 46 | | | |
| | 6 | | |
| | | 14 | |
| 4 | | | |
| | 4 | | |
| | | 18 | |
| 0 | | | |
| | | | Even total: 18 |

- Digit takes the values 3, 8, 6 and 4 in order [B1]
- Total starts at 0 and then takes 8, 14 and 18; it is unchanged for the digit 3 [B1]
- Number takes 4683, 468, 46, 4 and 0 [B1]
- the loop stops when Number is 0, so there is no further row after 0 [B1]
- the output is Even total: 18 [B1]
:::

:::eg Write a function (6 marks)
A ticket code has six characters: two capital letters followed by four digits, for example `KT4021`. Write a function `ValidCode` that takes a STRING and returns TRUE if it is a valid ticket code and FALSE otherwise. Refer to the insert for the functions you may use. [6 marks]

Break the rule into three tests: the length, the first two characters and the last four. Each one can return FALSE as soon as it fails.

```pseudocode
FUNCTION ValidCode(Code : STRING) RETURNS BOOLEAN
   DECLARE Index : INTEGER

   IF LENGTH(Code) <> 6 THEN
      RETURN FALSE
   ENDIF
   FOR Index ← 1 TO 2
      IF ASC(MID(Code, Index, 1)) < 65 OR ASC(MID(Code, Index, 1)) > 90 THEN
         RETURN FALSE
      ENDIF
   NEXT Index
   FOR Index ← 3 TO 6
      IF NOT IS_NUM(MID(Code, Index, 1)) THEN
         RETURN FALSE
      ENDIF
   NEXT Index
   RETURN TRUE
ENDFUNCTION
```

- function header with the STRING parameter and `RETURNS BOOLEAN`, closed with `ENDFUNCTION` [B1]
- the length is tested and FALSE returned when it is not 6 [B1]
- a loop through the first two characters, each extracted with `MID` [B1]
- each of those characters tested as a capital letter (ASCII 65 to 90) with FALSE returned if not [B1]
- a loop through characters 3 to 6, each tested with `IS_NUM` (or an ASCII range of 48 to 57) [B1]
- `RETURN TRUE` after all tests have passed [B1]

(Accept a Boolean flag set to FALSE in the loops and returned at the end. Accept a letter test written as a comparison with the characters `'A'` and `'Z'`, which needs no ASCII codes.)
:::

:::eg Process a text file (8 marks)
A weather station in Santiago saves one temperature per line of the text file `Readings.txt`, for example `24.5`. The file holds at least one line. Write a procedure `ProcessReadings` that reads every line, outputs how many readings there are and the highest reading, and writes every reading above 30.0 to a second text file `Alerts.txt`. [8 marks]

Each line is read as a STRING, so it must be converted with `STR_TO_NUM` before it is compared. Two files are open at once, so both need closing. The first reading is a good starting value for the highest. `Highest` has no value until then, so the comparison `Value > Highest` sits inside the `ELSE` of `IF Count = 1`: writing `Count = 1 OR Value > Highest` would compare an empty variable on the first pass, because pseudocode may test both halves of an `OR`, even when the first half is true (the Cambridge pseudocode guide does not promise that it stops early).

```pseudocode
PROCEDURE ProcessReadings()
   DECLARE Line : STRING
   DECLARE Value, Highest : REAL
   DECLARE Count : INTEGER

   Count ← 0
   OPENFILE "Readings.txt" FOR READ
   OPENFILE "Alerts.txt" FOR WRITE
   WHILE NOT EOF("Readings.txt")
      READFILE "Readings.txt", Line
      Value ← STR_TO_NUM(Line)
      Count ← Count + 1
      IF Count = 1 THEN
         Highest ← Value
      ELSE
         IF Value > Highest THEN
            Highest ← Value
         ENDIF
      ENDIF
      IF Value > 30.0 THEN
         WRITEFILE "Alerts.txt", Line
      ENDIF
   ENDWHILE
   CLOSEFILE "Readings.txt"
   CLOSEFILE "Alerts.txt"
   OUTPUT "Readings: ", Count
   OUTPUT "Highest: ", Highest
ENDPROCEDURE
```

- `Readings.txt` opened for reading [B1]
- `Alerts.txt` opened for writing [B1]
- loop that continues until the end of the file, using `EOF` [B1]
- `READFILE` inside the loop and the line converted to a number with `STR_TO_NUM` [B1]
- the number of readings counted [B1]
- the highest reading found, initialised from the first reading or a suitable low value [B1]
- readings above 30.0 written to `Alerts.txt` [B1]
- both files closed, with the count and the highest output after the loop [B1]

(Do not give the `WRITEFILE` mark if the file was opened for reading. Opening `Alerts.txt` for writing erases anything already in it: use `APPEND` only if the question says to keep the old alerts.)
:::

:::eg Spot the error: a missing NEXT
A student answers: "Write pseudocode to input 10 whole numbers and output how many of them are negative. [4 marks]"

```pseudocode
Count ← 0
FOR Index ← 1 TO 10
   INPUT Number
   IF Number < 0 THEN
      Count ← Count + 1
   ENDIF
OUTPUT Count
```

The student scores 3 out of 4. The line `OUTPUT Count` follows the `ENDIF` with no `NEXT Index`, so the `FOR` loop is never closed. Without `NEXT Index` the examiner cannot tell whether the output is inside the loop (ten outputs) or after it.

- `Count` initialised to 0 [B1]
- a loop that repeats 10 times, with the input inside it and closed with `NEXT Index` [B0] (the loop is never closed)
- negative numbers tested and counted [B1]
- the count output after the loop [B1]

The fix: add `NEXT Index` on the line after `ENDIF`, aligned with `FOR`. A paper-based exam gives no warning, so build the habit: whenever you write `FOR`, write `NEXT` straight away and fill in the body between them.
:::

## Common slips

| The slip | Why it loses the mark | The fix |
|---|---|---|
| Python syntax: `for i in range(10)`, `if x == 5:`, `print(x)` | not Cambridge pseudocode | `FOR Index ← 1 TO 10`, `IF X = 5 THEN`, `OUTPUT X` |
| `=` used for assignment | in pseudocode `=` compares | `Total ← 0` |
| missing `ENDIF`, `ENDWHILE`, `NEXT`, `ENDFUNCTION`, `ENDPROCEDURE` | the structure is not closed | write the closing keyword as soon as you write the opening one |
| `CALL` used on a function | a function is used in an expression | `Total ← Sum(A, B)`, not `Total ← CALL Sum(A, B)` |
| function with no `RETURN`, or `RETURN` before it is ready | a function must give a value back | end with `RETURN` of the answer |
| string positions off by one | positions in `MID` start at 1 | `MID(Word, 1, 1)` is the first character |
| `WRITEFILE` after `OPENFILE … FOR WRITE` on a file you meant to extend | WRITE erases the old content | `FOR APPEND` to add to the end |
| a file never closed | data may be lost and the file cannot be reopened in another mode | `CLOSEFILE` for every file you open |
| a line from a file used as a number | `READFILE` gives a STRING | `STR_TO_NUM(Line)` before any arithmetic |
| the maximum started at 0 | a list of negative numbers gives a wrong answer | start from the first element |
| array indexed from 0 when the question says 1 | the lower bound is 1 unless stated | use the bounds in the declaration |

## Technique check

:::try Technique check
Q: A question is worth 12 marks. At the pace of this guide, about how many minutes does it deserve?
A: \(12 \times 1.6 = 19.2\), so about 19 minutes.

Q: Write one line of pseudocode that stores the third character of the STRING `Name` in the variable `Letter`.
A: `Letter ← MID(Name, 3, 1)`. MID takes the string, the start position (counting from 1) and the number of characters.

Q: State the value of `17 DIV 5` and of `17 MOD 5`.
A: `17 DIV 5` is 3 (whole number of times 5 goes into 17) and `17 MOD 5` is 2 (the remainder).

Q: Correct this line: `Total ← CALL Sum(A, B)`, where `Sum` is a function.
A: `Total ← Sum(A, B)`. A function is called inside an expression, so it is never used with `CALL`.

Q: A student opens `Scores.txt` FOR WRITE to add one more line to the end of the existing file. What goes wrong, and what should be used?
A: Opening for WRITE erases the existing lines, so only the new line remains. `OPENFILE "Scores.txt" FOR APPEND` adds to the end instead.

Q: Why is `IF Age >= 11 AND <= 19 THEN` wrong?
A: Each side of `AND` must be a complete condition. It should be `IF Age >= 11 AND Age <= 19 THEN`.
:::

## Revision plan

:::steps
1. **Learn the pseudocode** conventions above until you write them without thinking.
2. **Study the chapters** below in order. For every algorithm in them (linear search, bubble sort, totals and maximum, stack and queue operations, file reading), write it from a blank page, then compare.
3. **Practise every question type** with the exam practice in each chapter, then the "Paper 2 style" set in [Mixed practice: AS (Papers 1 and 2)](#cs.mixed.as).
4. **Time yourself:** do [Mock Paper 2](#cs.mock.p2) in 2 hours with the insert beside you, then past papers (below).
:::

The tracker below counts the checklist items you have ticked in every Paper 2 chapter.

:::progress P2
:::

## Past papers and self-marking

Paper 2 question papers come with an insert, and the insert is a separate file: download both, together with the mark scheme.

- [PapaCambridge](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) keeps 9618 papers, inserts and mark schemes together (an unofficial site).
- [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-2/) sorts Paper 2 papers by series (an unofficial site).

:::steps
1. **Write each answer by hand,** as you would in the exam. Typing it into an editor hides the slips the paper will not forgive.
2. **Mark each feature separately** against the mark scheme, in a different colour.
3. **Dry run your own answer** with the test values from the question. If it fails, find the line and fix it: this is the habit that finds errors in the exam.
4. **Compare with the mark scheme's algorithm,** not to copy it, but to see how else the job can be done and how neatly.
5. **Keep a list of your slips** (missing `NEXT`, off-by-one, no `CLOSEFILE`) and read it before each practice session.
:::

:::warn Pseudocode is not Python
This course teaches Python for Paper 4, so Python habits creep into pseudocode. Before you hand in a Paper 2 script, scan it once for `==`, `print`, `range`, `:` at the end of a line, `[i]` string indexes and `len`. None of them belongs in Cambridge pseudocode.
:::

:::recap
- Paper 2: 2 hours, 75 marks, sections 9 to 12, answers written in pseudocode on the paper, an insert supplied, no calculator. The May/June 2025 paper had 7 scenario questions ending with a long multi-module question.
- The insert lists the string, numeric, date and file functions and the operators; use only those, with the names printed.
- Pace: \(120 \div 75 = 1.6\) minutes per mark. Keep ten minutes to dry-run your own answers.
- Marks are given for each **feature** of an algorithm, so a partly correct answer still scores.
- Cambridge pseudocode: keywords in capitals, `←` for assignment, `DECLARE` with types, three-space indents, every structure closed, `CALL` for procedures only, `RETURN` in functions.
- Question types: identifier tables, flowcharts, trace tables, functions and procedures, arrays and records, stacks and queues, text files, structure charts, testing, amending code.
- Common slips: Python syntax, `=` for assignment, missing closing keywords, `CALL` on a function, off-by-one string positions, WRITE instead of APPEND, unclosed files, a line used as a number.
- Practise by hand, mark each feature, and dry run your own answer.
:::

:::links
- papers: [9618 past papers, inserts and mark schemes](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · every series in one place [unofficial]
- papers: [Paper 2 past papers by series](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-2/) · Physics & Maths Tutor · Paper 2 only [unofficial]
- practise: [Programming basics: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/programming-basics/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Arrays: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/arrays/exam-questions/) · Save My Exams · array, search and sort questions [paid]
- practise: [Files: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/files/exam-questions/) · Save My Exams · text-file questions [paid]
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · the official rules for every pseudocode construct
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run a translation of your algorithm line by line to check your dry run

Links checked 13 November 2026.
:::

Next: [Mixed practice: AS (Papers 1 and 2)](#cs.mixed.as)
