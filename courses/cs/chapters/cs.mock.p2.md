@chapter cs.mock.p2
@title Mock Paper 2: Problem-solving and Programming
@level mock
@paper CAIE 9618 Paper 2
@time 2 h
@summary A full-length Paper 2 mock: seven questions worth 75 marks on sections 9 to 12, answered in pseudocode with the insert of functions and operators beside you. It has an identifier table and decomposition, a flowchart with logic errors, a trace table, a stack with a pointer, an efficient sort, text-file processing with string functions, and a long final question built from three modules. Every answer has a full mark scheme with one mark point per mark.

:::exam Read these instructions first
- You have **2 hours**. The clock above starts when you open the paper. Stop at the end of the time, then press **Finish** to see the mark schemes.
- Answer **all** questions. Write your answers on paper (or type them), **in pseudocode**. You are not asked to write program code in a programming language.
- **Calculators must not be used** in this paper.
- The marks for each part of a question are shown in brackets, for example [3]. The total for the paper is **75 marks**.
- **No marks will be awarded for using brand names** of software packages or hardware.
- The **insert** is the list below. Refer to the insert for the list of pseudocode functions and operators. Questions never ask you to remember how a function works.
- Plan about 1.6 minutes per mark: a 10-mark question deserves about 16 minutes.
- When the time is up, press Finish, mark each answer honestly (a mark only for a point actually made), enter your mark for each question, and use the chapters listed to revise.

**Insert: pseudocode functions and operators**

- `LEFT(ThisString : STRING, x : INTEGER) RETURNS STRING` returns the leftmost x characters. Example: `LEFT("Tropical", 4)` returns `"Trop"`
- `RIGHT(ThisString : STRING, x : INTEGER) RETURNS STRING` returns the rightmost x characters. Example: `RIGHT("Tropical", 3)` returns `"cal"`
- `MID(ThisString : STRING, x : INTEGER, y : INTEGER) RETURNS STRING` returns y characters, starting at position x (the first character is position 1). Example: `MID("Tropical", 2, 3)` returns `"rop"`
- `LENGTH(ThisString : STRING) RETURNS INTEGER` returns the number of characters. Example: `LENGTH("Tropical")` returns `8`
- `TO_UPPER(x : CHAR or STRING)` returns x in upper case (the same type as x). Example: `TO_UPPER("Tropical")` returns `"TROPICAL"`
- `TO_LOWER(x : CHAR or STRING)` returns x in lower case (the same type as x). Example: `TO_LOWER('Q')` returns `'q'`
- `NUM_TO_STR(x : REAL or INTEGER) RETURNS STRING` returns the number as a string. Example: `NUM_TO_STR(47.5)` returns `"47.5"`
- `STR_TO_NUM(x : STRING) RETURNS REAL or INTEGER` returns the number that the string holds. Example: `STR_TO_NUM("47")` returns `47`
- `IS_NUM(ThisString : STRING) RETURNS BOOLEAN` returns TRUE if the string can be converted to a number. Examples: `IS_NUM("12")` returns `TRUE`; `IS_NUM("1A")` returns `FALSE`
- `ASC(ThisChar : CHAR) RETURNS INTEGER` returns the ASCII value of the character. Example: `ASC('A')` returns `65`
- `CHR(x : INTEGER) RETURNS CHAR` returns the character with ASCII value x. Example: `CHR(66)` returns `'B'`
- `INT(x : REAL) RETURNS INTEGER` returns the integer part of x. Example: `INT(27.9)` returns `27`
- `RAND(x : INTEGER) RETURNS REAL` returns a random real number from 0 up to, but not including, x. Example: `RAND(10)` may return `3.7`
- `DAY(ThisDate)`, `MONTH(ThisDate)` and `YEAR(ThisDate)` return the day, month or year of a date. Example: `YEAR(14/03/2027)` returns `2027`
- `DAYINDEX(ThisDate)` returns the day of the week (Sunday is 1). Example: `DAYINDEX(14/03/2027)` returns `1`
- `SETDATE(Day, Month, Year)` returns a date, and `TODAY()` returns today's date. Example: `SETDATE(14, 3, 2027)`
- `EOF(FileName : STRING) RETURNS BOOLEAN` returns TRUE if there are no more lines to read from the text file (it must be open for reading). Example: `EOF("Data.txt")`
- `&` joins strings (a CHAR may be joined to a STRING). Example: `"Sun" & "day"` gives `"Sunday"`
- `MOD` and `DIV` give the remainder and the whole-number division. Example: `19 MOD 6` is `1`; `19 DIV 6` is `3`
- `=  <>  <  >  <=  >=` compare values, and `AND`, `OR` and `NOT` are the logic operators (a string of length 1 may be used as a CHAR or a STRING)

An error is generated if a function call is badly formed or if an operator is given a value of the wrong type.
:::

:::try
Q: [8 marks] (#cs.algorithms) A school in Accra runs a sports day for six houses. A program inputs the name of each house and the points that the house scored in each of four events. The program then outputs the name of the winning house and its total points.

(a) Complete the identifier table by giving the data type of each identifier. Use the Cambridge pseudocode data types. [4]

| Identifier | Data type | Description |
|---|---|---|
| `HouseName` | | stores the names of the six houses |
| `Points` | | stores the points of every house in every event |
| `BestTotal` | | the highest house total found so far |
| `BestHouse` | | the name of the house with the highest total so far |

(b) The program is written as separate modules. State what is meant by decomposition and give one benefit of it. [2]

(c) The program stores only each house's name and points. It does not store the colour of the house or the names of its members. State the name of this technique and explain why it is used. [2]
A: (a)

| Identifier | Data type |
|---|---|
| `HouseName` | `ARRAY[1:6] OF STRING` |
| `Points` | `ARRAY[1:6, 1:4] OF INTEGER` |
| `BestTotal` | `INTEGER` |
| `BestHouse` | `STRING` |

- `HouseName` is a one-dimensional array of 6 STRING [B1]
- `Points` is a two-dimensional array of INTEGER with 6 rows (houses) and 4 columns (events) [B1]
- `BestTotal` is INTEGER [B1]
- `BestHouse` is STRING [B1]

(b)

- decomposition is breaking a problem down into smaller sub-problems, each of which becomes a module (a procedure or a function) [B1]
- one benefit: each module can be written and tested separately (or by different programmers), and a module can be reused [B1]

(c)

- the technique is abstraction [B1]
- it leaves out the details that are not needed for the problem, so the program is simpler and uses less memory [B1]
:::

:::try
Q: [9 marks] (#cs.algorithms) A program for a school in Manila reads the heights, in centimetres, of 8 athletes. It outputs how many of them are **taller than 170 cm** and the mean height of all 8. The flowchart for the program is shown. It contains three logic errors.

<figure class="fig"><svg viewBox="0 0 426 668" role="img" aria-label="A flowchart. Start, then a process box with Total gets 0, Taller gets 0 and Count gets 1, then a decision Count less than 8. The exit labelled No leads right to Mean gets Total divided by 8, then OUTPUT Taller and Mean, then End. The exit labelled Yes leads down to INPUT Height, then Total gets Height, then a decision Height greater than or equal to 170. Yes leads down to Taller gets Taller plus 1, then Count gets Count plus 1. No leads right, down and back left to join the arrow above Count gets Count plus 1. An arrow from Count gets Count plus 1 goes left, up and back to the line above the first decision."><rect class="fm s-acc sw2" x="98" y="12" width="84" height="32" rx="16"/><text class="tl tc" x="140" y="32">Start</text><rect class="f1 s-acc sw2" x="85" y="69" width="110" height="70" rx="3"/><text class="tl tc" x="140" y="92">Total ← 0</text><text class="tl tc" x="140" y="108">Taller ← 0</text><text class="tl tc" x="140" y="124">Count ← 1</text><polygon class="fp s-acc sw2" points="140,172 194,200 140,228 86,200"/><text class="tl tc" x="140" y="204">Count &lt; 8?</text><polygon class="fm2 s-acc sw2" points="85,265 209,265 195,299 71,299"/><text class="tl tc" x="140" y="286">INPUT Height</text><rect class="f1 s-acc sw2" x="78" y="331" width="124" height="38" rx="3"/><text class="tl tc" x="140" y="354">Total ← Height</text><polygon class="fp s-acc sw2" points="140,412 212,440 140,468 68,440"/><text class="tl tc" x="140" y="444">Height &gt;= 170?</text><rect class="f1 s-acc sw2" x="60.5" y="516" width="159" height="38" rx="3"/><text class="tl tc" x="140" y="539">Taller ← Taller + 1</text><rect class="f1 s-acc sw2" x="67.5" y="601" width="145" height="38" rx="3"/><text class="tl tc" x="140" y="624">Count ← Count + 1</text><rect class="f1 s-acc sw2" x="251" y="181" width="138" height="38" rx="3"/><text class="tl tc" x="320" y="204">Mean ← Total / 8</text><polygon class="fm2 s-acc sw2" points="240.5,265 413.5,265 399.5,299 226.5,299"/><text class="tl tc" x="320" y="286">OUTPUT Taller, Mean</text><rect class="fm s-acc sw2" x="278" y="338" width="84" height="32" rx="16"/><text class="tl tc" x="320" y="358">End</text><path class="ln" fill="none" d="M140 44 L140 69" marker-end="url(#ah)"/><path class="ln" fill="none" d="M140 139 L140 172" marker-end="url(#ah)"/><path class="ln" fill="none" d="M140 228 L140 265" marker-end="url(#ah)"/><path class="ln" fill="none" d="M140 299 L140 331" marker-end="url(#ah)"/><path class="ln" fill="none" d="M140 369 L140 412" marker-end="url(#ah)"/><path class="ln" fill="none" d="M140 468 L140 516" marker-end="url(#ah)"/><path class="ln" fill="none" d="M140 554 L140 601" marker-end="url(#ah)"/><path class="ln" fill="none" d="M194 200 L251 200" marker-end="url(#ah)"/><path class="ln" fill="none" d="M320 219 L320 265" marker-end="url(#ah)"/><path class="ln" fill="none" d="M320 299 L320 338" marker-end="url(#ah)"/><path class="ln" fill="none" d="M212 440 L330 440 L330 578 L140 578" marker-end="url(#ah)"/><path class="ln" fill="none" d="M67.5 620 L24 620 L24 160 L140 160" marker-end="url(#ah)"/><text class="tl" x="202" y="192">No</text><text class="tl" x="148" y="250">Yes</text><text class="tl" x="220" y="432">No</text><text class="tl" x="148" y="490">Yes</text></svg><figcaption>A flowchart for a program that reads the heights of 8 athletes and outputs how many are taller than 170 cm and the mean height. It contains three logic errors.</figcaption></figure>

(a) Identify the three errors and, for each, say how to correct it. [6]

(b) Write corrected pseudocode for the whole program, using a `FOR` loop. [3]
A: (a)

| Error | Correction |
|---|---|
| `Count ← 1` with the test `Count < 8?` makes the loop run only 7 times, so only 7 heights are read | change the test to `Count <= 8?` (or start `Count` at 0) |
| `Total ← Height` replaces the total each time round | change it to `Total ← Total + Height` |
| the test `Height >= 170?` also counts an athlete exactly 170 cm tall | change it to `Height > 170?` |

- error 1 identified: the loop runs 7 times, not 8 [B1]
- correction 1: `Count <= 8` (or `Count < 9`, or `Count` starts at 0) [B1]
- error 2 identified: `Total ← Height` does not add up the heights [B1]
- correction 2: `Total ← Total + Height` [B1]
- error 3 identified: `>=` includes 170, so the athlete who is not taller than 170 is counted [B1]
- correction 3: `Height > 170` [B1]

(b) One possible answer:

```pseudocode
Total ← 0
Taller ← 0
FOR Count ← 1 TO 8
   INPUT Height
   Total ← Total + Height
   IF Height > 170 THEN
      Taller ← Taller + 1
   ENDIF
NEXT Count
Mean ← Total / 8
OUTPUT Taller, Mean
```

- `Total` and `Taller` set to 0 before the loop, and `FOR Count ← 1 TO 8` with `NEXT Count` [B1]
- `INPUT Height` and `Total ← Total + Height` inside the loop [B1]
- `IF Height > 170 THEN Taller ← Taller + 1 ENDIF` inside the loop, then `Mean ← Total / 8` and `OUTPUT Taller, Mean` after it [B1]
:::

:::try
Q: [9 marks] (#cs.testing) A weather program for a farm in Perth stores the highest temperature of each day of one week in the array `Temps`, which has 7 elements. The values are in degrees Celsius.

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| `Temps` | 28 | 31 | 35 | 29 | 36 | 33 | 30 |

The pseudocode below uses the array.

```pseudocode
Highest ← Temps[1]
Day ← 1
Hot ← 0
FOR Index ← 1 TO 7
   IF Temps[Index] > 30 THEN
      Hot ← Hot + 1
   ENDIF
   IF Temps[Index] > Highest THEN
      Highest ← Temps[Index]
      Day ← Index
   ENDIF
NEXT Index
OUTPUT Day, Highest, Hot
```

(a) Complete the trace table for the data above. Write a value in a column only on the row where the variable changes. The first row is for the three assignments before the loop. [6]

| Index | Highest | Day | Hot | OUTPUT |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

(b) State what the pseudocode does. [2]

(c) The value of `Temps[3]` is changed from 35 to 30. State the three values that are now output. [1]
A: (a)

| Index | Highest | Day | Hot | OUTPUT |
|---|---|---|---|---|
| | 28 | 1 | 0 | |
| 1 | | | | |
| 2 | 31 | 2 | 1 | |
| 3 | 35 | 3 | 2 | |
| 4 | | | | |
| 5 | 36 | 5 | 3 | |
| 6 | | | 4 | |
| 7 | | | | |
| | | | | 5 36 4 |

- first row: `Highest` 28, `Day` 1 and `Hot` 0 [B1]
- the `Index` column counts 1 to 7 on the next seven rows [B1]
- the `Hot` column is correct: 1, 2, 3, 4 on the rows for Index 2, 3, 5 and 6 [B1]
- the `Highest` column is correct: 31, 35, 36 on the rows for Index 2, 3 and 5 [B1]
- the `Day` column is correct: 2, 3, 5 on the same rows [B1]
- the last row shows the output 5 36 4 (in that order) [B1]

(b)

- it finds the highest temperature of the week and the day (index) on which it happened [B1]
- it counts the days on which the temperature was above 30 [B1]

(c) The output is 5 36 3 [B1] (the day 3 value 30 is no longer above 30, so `Hot` is one less)
:::

:::try
Q: [10 marks] (#cs.structures) A stack of whole numbers is stored in the global array `Stack[1:6]`. The global variable `TopPointer` holds the index of the item at the top of the stack. It is 0 when the stack is empty. Items are added with a function `Push` and removed with a function `Pop`.

```pseudocode
DECLARE Stack : ARRAY[1:6] OF INTEGER
DECLARE TopPointer : INTEGER
```

At one moment `Stack[1]` is 14, `Stack[2]` is 8 and `Stack[3]` is 21, and `TopPointer` is 3.

(a) These operations are carried out in order: `Push(30)`, `Pop`, `Pop`, `Push(5)`. State the value returned by each `Pop`, and the value of `TopPointer` after each of the four operations. [3]

(b) Write the function `Push(Item)`. It takes an INTEGER, adds it to the top of the stack and returns TRUE. If the stack is full, it changes nothing and returns FALSE. [4]

(c) Write the function `Pop()`. It removes the item at the top of the stack and returns it. If the stack is empty it returns -1. [3]
A: (a)

| Operation | Value returned | TopPointer |
|---|---|---|
| `Push(30)` | TRUE | 4 |
| `Pop` | 30 | 3 |
| `Pop` | 21 | 2 |
| `Push(5)` | TRUE | 3 |

- `TopPointer` is 4 after `Push(30)` [B1]
- the first `Pop` returns 30 and the second returns 21, with `TopPointer` 3 then 2 [B1]
- `TopPointer` is 3 after `Push(5)`, which replaces the value at `Stack[3]` [B1]

(b) One possible answer:

```pseudocode
FUNCTION Push(Item : INTEGER) RETURNS BOOLEAN
   IF TopPointer = 6 THEN
      RETURN FALSE
   ELSE
      TopPointer ← TopPointer + 1
      Stack[TopPointer] ← Item
      RETURN TRUE
   ENDIF
ENDFUNCTION
```

- function header with an INTEGER parameter and `RETURNS BOOLEAN` [B1]
- the test for a full stack (`TopPointer = 6`, or `>= 6`) returning FALSE and changing nothing [B1]
- `TopPointer` increased by 1 before the item is stored [B1]
- the item stored in `Stack[TopPointer]` and TRUE returned [B1]

(c) One possible answer:

```pseudocode
FUNCTION Pop() RETURNS INTEGER
   DECLARE Item : INTEGER

   IF TopPointer = 0 THEN
      RETURN -1
   ELSE
      Item ← Stack[TopPointer]
      TopPointer ← TopPointer - 1
      RETURN Item
   ENDIF
ENDFUNCTION
```

- the test for an empty stack (`TopPointer = 0`) returning -1, with `RETURNS INTEGER` in the header [B1]
- the item at `Stack[TopPointer]` read into a variable before the pointer changes [B1]
- `TopPointer` decreased by 1 and the item returned [B1]
:::

:::try
Q: [11 marks] (#cs.datatypes) A swimming club in Santiago stores the names and the best times, in whole seconds, of its 8 swimmers in two arrays. `SwimmerName[1]` and `SwimTime[1]` belong to the same swimmer, and so on up to index 8.

```pseudocode
DECLARE SwimmerName : ARRAY[1:8] OF STRING
DECLARE SwimTime : ARRAY[1:8] OF INTEGER
```

(a) Write an efficient procedure `SortSwimmers` that uses a bubble sort to sort both arrays so that the swimmer with the **smallest** time is first. Each swimmer's name must stay with his or her time. The sort must stop as soon as a pass makes no swaps, and must not compare items that are already in their final place. [8]

(b) The array `SwimTime` holds 60, 55, 62, 51, 58, 70, 66, 64. The procedure from part (a) is run on this data.

(i) State the contents of `SwimTime` after the first pass. [1]

(ii) State the number of swaps made in the first pass. [1]

(iii) State the total number of passes made, counting the last pass that makes no swaps. [1]
A: (a) One possible answer:

```pseudocode
PROCEDURE SortSwimmers()
   DECLARE Index, Limit, TempTime : INTEGER
   DECLARE TempName : STRING
   DECLARE Swapped : BOOLEAN

   Limit ← 7
   REPEAT
      Swapped ← FALSE
      FOR Index ← 1 TO Limit
         IF SwimTime[Index] > SwimTime[Index + 1] THEN
            TempTime ← SwimTime[Index]
            SwimTime[Index] ← SwimTime[Index + 1]
            SwimTime[Index + 1] ← TempTime
            TempName ← SwimmerName[Index]
            SwimmerName[Index] ← SwimmerName[Index + 1]
            SwimmerName[Index + 1] ← TempName
            Swapped ← TRUE
         ENDIF
      NEXT Index
      Limit ← Limit - 1
   UNTIL Swapped = FALSE OR Limit = 0
ENDPROCEDURE
```

- an outer loop that repeats passes until a pass makes no swaps (or the range has shrunk to nothing) [B1]
- a flag (`Swapped`) set to FALSE at the start of every pass [B1]
- an inner `FOR` loop over the neighbouring pairs of one pass [B1]
- the upper limit of the inner loop reduced after every pass, so that items already in place are not compared [B1]
- the test `SwimTime[Index] > SwimTime[Index + 1]` (smallest first) [B1]
- the two times swapped using a temporary variable [B1]
- the two names swapped in the same way, at the same time [B1]
- the flag set to TRUE when a swap is made [B1]

(b)

- (i) 55, 60, 51, 58, 62, 66, 64, 70 [B1]
- (ii) 5 swaps [B1]
- (iii) 4 passes: the first three make 5, 3 and 1 swaps, and the fourth makes none [B1]
:::

:::try
Q: [12 marks] (#cs.structures) A company in Singapore receives a text file `Branch.txt` of sales figures. Each valid line has three letters (a branch code), a colon, and then a whole number (the quantity sold) with at least one digit. For example, `NAI:105`. Some lines are not valid.

(a) Write a procedure `CleanBranchFile` that processes the file as follows.

- For every valid line, the quantity is added to a running total and the line is written to a new text file `Clean.txt` with the branch code in capital letters.
- A line is **not** valid if it is not longer than 4 characters, if its fourth character is not a colon, or if the part after the colon is not a number. An invalid line is counted but not written.
- When the whole file has been read, the procedure outputs the number of valid lines, the number of invalid lines and the total quantity. [11]

(b) The file `Branch.txt` contains the lines below. State the three values output by the procedure, in the order of part (a). [1]

```text
lim:12
ACC:7
NAI:105
KUL9
SYD:4B
DEL:20
```
A: (a) One possible answer:

```pseudocode
PROCEDURE CleanBranchFile()
   DECLARE Line, Code, Quantity : STRING
   DECLARE Valid, Invalid, Total : INTEGER
   DECLARE IsValid : BOOLEAN

   Valid ← 0
   Invalid ← 0
   Total ← 0
   OPENFILE "Branch.txt" FOR READ
   OPENFILE "Clean.txt" FOR WRITE
   WHILE NOT EOF("Branch.txt")
      READFILE "Branch.txt", Line
      IsValid ← FALSE
      IF LENGTH(Line) > 4 THEN
         IF MID(Line, 4, 1) = ':' THEN
            Quantity ← RIGHT(Line, LENGTH(Line) - 4)
            IF IS_NUM(Quantity) THEN
               IsValid ← TRUE
            ENDIF
         ENDIF
      ENDIF
      IF IsValid = TRUE THEN
         Code ← TO_UPPER(LEFT(Line, 3))
         Total ← Total + STR_TO_NUM(Quantity)
         Valid ← Valid + 1
         WRITEFILE "Clean.txt", Code & ":" & Quantity
      ELSE
         Invalid ← Invalid + 1
      ENDIF
   ENDWHILE
   CLOSEFILE "Branch.txt"
   CLOSEFILE "Clean.txt"
   OUTPUT Valid, Invalid, Total
ENDPROCEDURE
```

- `Branch.txt` opened for reading and `Clean.txt` opened for writing [B1]
- the three counters set to 0 before the loop [B1]
- a loop that continues until `EOF("Branch.txt")` is TRUE, with each line read by `READFILE` inside it [B1]
- the length tested (`LENGTH(Line) > 4`) before the fourth character is examined [B1]
- the fourth character tested with `MID(Line, 4, 1)` against a colon [B1]
- the quantity extracted with `RIGHT` (or `MID`) and `LENGTH` [B1]
- `IS_NUM` used to test the quantity [B1]
- for a valid line, `STR_TO_NUM` of the quantity added to the total, and the valid count increased [B1]
- for a valid line, the code taken with `LEFT(Line, 3)`, converted with `TO_UPPER`, and the line written to `Clean.txt` as code, colon and quantity [B1]
- the invalid count increased for every line that fails any test, and nothing written for it [B1]
- both files closed after the loop, then the three values output after the loop [B1]

(b) The output is 4, 2 and 144 [B1] (the valid lines are `lim:12`, `ACC:7`, `NAI:105` and `DEL:20`: 12 + 7 + 105 + 20 = 144)
:::

:::try
Q: [16 marks] (#cs.procedures) A theatre in Manila sells seats for a school play. The seats are in 5 rows of 8. The global array `Seat` holds `'F'` for a free seat and `'S'` for a sold seat. The program is made of the modules in the table.

```pseudocode
DECLARE Seat : ARRAY[1:5, 1:8] OF CHAR
```

| Module | Kind | Parameters | Returns | Description |
|---|---|---|---|---|
| `Main` | program | none | none | sets every seat free, asks for a row and a number of seats, books them and saves the plan |
| `CountFree` | function | `Row : INTEGER` | INTEGER | the number of free seats in the row |
| `BookSeats` | function | `Row : INTEGER`, `Number : INTEGER` | BOOLEAN | books the first `Number` free seats in the row, or changes nothing |
| `SaveSeats` | procedure | none | none | writes the seating plan to a text file |

(a) Write the function `CountFree`. [3]

(b) Write the function `BookSeats`. If the row has fewer than `Number` free seats, it changes nothing and returns FALSE. Otherwise it changes the first `Number` free seats in the row from `'F'` to `'S'` and returns TRUE. It must use `CountFree`. [6]

(c) Write the procedure `SaveSeats`. It writes the plan to the text file `Seats.txt`, one line for each row, each line made of the 8 seat characters joined together. [4]

(d) Write the `Main` program. It sets every seat to `'F'`, inputs a row and a number of seats, calls `BookSeats`, outputs "Booked" if it returned TRUE and "Not enough seats" if not, and then calls `SaveSeats`. [3]
A: (a) One possible answer:

```pseudocode
FUNCTION CountFree(Row : INTEGER) RETURNS INTEGER
   DECLARE Col, Count : INTEGER

   Count ← 0
   FOR Col ← 1 TO 8
      IF Seat[Row, Col] = 'F' THEN
         Count ← Count + 1
      ENDIF
   NEXT Col
   RETURN Count
ENDFUNCTION
```

- function header with an INTEGER parameter and `RETURNS INTEGER`; `Count` set to 0 [B1]
- a loop over the 8 columns of the given row testing `Seat[Row, Col] = 'F'` [B1]
- `Count` increased for a free seat, and `Count` returned after the loop [B1]

(b) One possible answer:

```pseudocode
FUNCTION BookSeats(Row : INTEGER, Number : INTEGER) RETURNS BOOLEAN
   DECLARE Col, Booked : INTEGER

   IF CountFree(Row) < Number THEN
      RETURN FALSE
   ELSE
      Booked ← 0
      Col ← 1
      WHILE Booked < Number
         IF Seat[Row, Col] = 'F' THEN
            Seat[Row, Col] ← 'S'
            Booked ← Booked + 1
         ENDIF
         Col ← Col + 1
      ENDWHILE
      RETURN TRUE
   ENDIF
ENDFUNCTION
```

- function header with two INTEGER parameters and `RETURNS BOOLEAN` [B1]
- `CountFree(Row)` used in a comparison with `Number`, and FALSE returned with no seat changed when there are too few [B1]
- a loop through the columns that stops once `Number` seats have been booked [B1]
- each seat tested with `Seat[Row, Col] = 'F'` [B1]
- a free seat set to `'S'` and the number booked counted [B1]
- TRUE returned after the booking [B1]

(c) One possible answer:

```pseudocode
PROCEDURE SaveSeats()
   DECLARE Row, Col : INTEGER
   DECLARE Line : STRING

   OPENFILE "Seats.txt" FOR WRITE
   FOR Row ← 1 TO 5
      Line ← ""
      FOR Col ← 1 TO 8
         Line ← Line & Seat[Row, Col]
      NEXT Col
      WRITEFILE "Seats.txt", Line
   NEXT Row
   CLOSEFILE "Seats.txt"
ENDPROCEDURE
```

- `Seats.txt` opened for writing and closed after the loops [B1]
- nested loops over the 5 rows and the 8 columns [B1]
- `Line` set to an empty string at the start of each row and built by joining each seat with `&` [B1]
- `WRITEFILE` of `Line` once for each row, after the column loop [B1]

(d) One possible answer:

```pseudocode
DECLARE Row, Col, Number : INTEGER

FOR Row ← 1 TO 5
   FOR Col ← 1 TO 8
      Seat[Row, Col] ← 'F'
   NEXT Col
NEXT Row
INPUT Row
INPUT Number
IF BookSeats(Row, Number) = TRUE THEN
   OUTPUT "Booked"
ELSE
   OUTPUT "Not enough seats"
ENDIF
CALL SaveSeats()
```

- nested loops setting every seat to `'F'` [B1]
- the row and the number input, and `BookSeats` called inside the condition of an `IF` (not with `CALL`), with the correct message in each case [B1]
- `CALL SaveSeats()` [B1]
:::

Next: [Mock Paper 3: Advanced Theory](#cs.mock.p3)
