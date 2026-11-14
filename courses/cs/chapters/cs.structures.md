@chapter cs.structures
@title Text files, stacks, queues and linked lists
@level as
@paper CAIE 9618 Paper 2 (and Paper 4 at A Level)
@time 6–8 hours
@summary Programs lose their variables when they stop, so data that must last is saved in text files. You will learn to read, write and append text files in pseudocode and Python, and to build three standard abstract data types, the stack, the queue and the linked list, in arrays.
:::why
Variables disappear when a program ends, so any program that must remember something, such as a list of customers, needs a file. Paper 2 asks you to write the file-handling code in pseudocode and to show what a stack, a queue or a linked list looks like inside an array after some operations. Both are routine marks once you know the patterns, and Paper 4 asks for the same code in Python, including a circular queue.
:::

**Before you start**, you should be comfortable with arrays and loops from [Data types, records and arrays](#cs.datatypes), and with procedures, functions and parameters from [Procedures, functions and parameters](#cs.procedures).

:::try Warm-up
Q: `DECLARE Scores : ARRAY[1:6] OF INTEGER`. What is the index of the first element and of the last, and which loop visits them all? (from [Data types, records and arrays](#cs.datatypes))
A: The first is 1 and the last is 6. `FOR Index ← 1 TO 6` … `NEXT Index` visits every element.
Q: What does `RIGHT("ABCDEFGH", 3)` return, and what does `NUM_TO_STR(42)` return? (from [Programming from zero](#cs.f.basics))
A: `RIGHT` gives the last 3 characters, `"FGH"`. `NUM_TO_STR(42)` gives the string `"42"`.
Q: A function returns a value; a procedure does not. Which one is called with CALL? (from [Procedures, functions and parameters](#cs.procedures))
A: A procedure is called with CALL. A function is called inside an expression, and CALL is never used with it.
:::

## Why we need files

A variable lives in the computer's main memory, and main memory is cleared when the program ends or the power goes off. A teacher in Nairobi who types in 30 pupils' marks would have to type them again each morning. A **file** is a named block of data kept on backing storage, such as a hard disk or flash memory, so it is still there tomorrow.

:::def Text file
A file that stores data as lines of text, which are read or written one line after another.
:::

Files are needed for three reasons, and Paper 2 expects you to give them.

- **Data persists.** A file keeps its data after the program stops and the computer is switched off.
- **Data can be shared.** One program can write a file that another program, or the same program on another day, reads.
- **Large amounts of data.** A file can hold far more data than the program's variables and arrays can sensibly keep in memory at once, and the program can read only the part it needs.

## Reading and writing text files

A text file is a sequence of lines. Cambridge pseudocode reads and writes **one line at a time, as a STRING**. Before you use a file you must **open** it, saying which job you want to do with it, and when you finish you must **close** it.

:::def File mode
The way a file is opened, which decides what the program may do with it. READ is for reading existing lines, WRITE is for writing new lines (any data already in the file is lost) and APPEND is for adding lines after the existing ones. A file is opened in only one mode at a time.
:::

:::def EOF
The end-of-file test. `EOF(<file>)` returns TRUE when there are no more lines to read, and FALSE otherwise. It is used only on a file opened in READ mode.
:::

:::key Text file commands in pseudocode
- `OPENFILE <file> FOR READ`, `FOR WRITE` or `FOR APPEND`. The file can be a string literal such as `"Visitors.txt"` or a STRING variable that holds the name.
- `READFILE <file>, <variable>` reads the next line into a STRING variable.
- `WRITEFILE <file>, <data>` writes one line.
- `EOF(<file>)` is TRUE when no lines are left to read.
- `CLOSEFILE <file>` when you have finished.
:::

Three details cause most of the errors.

- **WRITE erases.** Opening an existing file FOR WRITE creates a new, empty file: all the old lines are lost. To add to the end of a file, use APPEND.
- **READFILE gives a string.** A line holding `85` is the string `"85"`. Convert it with STR_TO_NUM before you calculate with it.
- **Always close the file.** Unclosed files can lose data that has not yet been saved, and a file open in one mode cannot be reopened in another.

Here is a complete round trip. The program writes three names, then reads them back and outputs them.

```pseudocode
DECLARE Line : STRING

OPENFILE "Visitors.txt" FOR WRITE
WRITEFILE "Visitors.txt", "Amara"
WRITEFILE "Visitors.txt", "Bilal"
WRITEFILE "Visitors.txt", "Chen"
CLOSEFILE "Visitors.txt"

OPENFILE "Visitors.txt" FOR READ
WHILE NOT EOF("Visitors.txt")
   READFILE "Visitors.txt", Line
   OUTPUT Line
ENDWHILE
CLOSEFILE "Visitors.txt"
```

Output:

```output
Amara
Bilal
Chen
```

The loop tests EOF **before** each READFILE, so it also works correctly for an empty file: the body never runs. If the loop read first and tested afterwards, an empty file would make READFILE try to read a line that is not there, which is an error.

### Text files in Python

In Python you open a file with `open(name, mode)`, where the mode is `"r"` (read), `"w"` (write) or `"a"` (append). The `with` statement closes the file for you at the end of its indented block, so you cannot forget CLOSEFILE. Two differences from pseudocode matter:

- `file.write(text)` writes exactly the text you give it. To end a line you must include `"\n"`.
- Reading a line gives the text **with its `"\n"`** at the end. `strip()` removes it (and any spaces at the ends).

```python
with open("visitors.txt", "w") as file:
    file.write("Amara\n")
    file.write("Bilal\n")
    file.write("Chen\n")

with open("visitors.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("visitors.txt", "a") as file:
    file.write("Dina\n")
with open("visitors.txt", "r") as file:
    print(len(file.readlines()), "lines after appending")

with open("visitors.txt", "w") as file:
    file.write("Emeka\n")
with open("visitors.txt", "r") as file:
    print(len(file.readlines()), "line after writing again")
```

Output:

```output
Amara
Bilal
Chen
4 lines after appending
1 line after writing again
```

The last two lines show why the mode matters. Appending Dina made four lines. Opening the file again with `"w"` threw all four away and left one.

A `for line in file` loop reads every line. Paper 4 programs often use the pattern that matches the pseudocode more closely: `readline()` returns the next line, and returns an empty string `""` at the end of the file.

```python
file = open("visitors.txt", "r")
line = file.readline()
while line != "":
    print(line.strip())
    line = file.readline()
file.close()
```

Output:

```output
Emeka
```

### Common file tasks

Most file questions are one of a few patterns: copy or transform every line, count the lines that meet a condition, search for a line, or save and load records. Each one is a loop that runs until EOF.

:::eg Copying a file and numbering the lines
A pupil keeps a to-do list in `Notes.txt`. Write pseudocode to copy every line into a new file `Numbered.txt`, putting the line number and a colon before each line. For example, the line `Buy rice` becomes `1: Buy rice`.

A new file is needed for the output, so it is opened FOR WRITE. The counter starts at 0 and is increased inside the loop, and `NUM_TO_STR` turns it into a string so that `&` can join it to the text.

```pseudocode
DECLARE LineOfText : STRING
DECLARE LineNumber : INTEGER

LineNumber ← 0
OPENFILE "Notes.txt" FOR READ
OPENFILE "Numbered.txt" FOR WRITE
WHILE NOT EOF("Notes.txt")
   READFILE "Notes.txt", LineOfText
   LineNumber ← LineNumber + 1
   WRITEFILE "Numbered.txt", NUM_TO_STR(LineNumber) & ": " & LineOfText
ENDWHILE
CLOSEFILE "Notes.txt"
CLOSEFILE "Numbered.txt"
```

If `Notes.txt` holds `Buy rice`, `Call the clinic` and `Pay the bus fare`, then `Numbered.txt` holds `1: Buy rice`, `2: Call the clinic` and `3: Pay the bus fare`. Both files are closed at the end.
:::

```python
with open("notes.txt", "w") as file:
    file.write("Buy rice\nCall the clinic\nPay the bus fare\n")

line_number = 0
with open("notes.txt", "r") as source, open("numbered.txt", "w") as target:
    for line_of_text in source:
        line_number = line_number + 1
        target.write(str(line_number) + ": " + line_of_text.strip() + "\n")

with open("numbered.txt", "r") as file:
    print(file.read(), end="")
```

Output:

```output
1: Buy rice
2: Call the clinic
3: Pay the bus fare
```

:::eg Counting lines that meet a condition (exam style)
The text file `Visitors.txt` holds the number of visitors to a museum in Lima on each day of a week, one whole number per line. Write pseudocode to read the file and output how many days had more than 100 visitors, and how many days the file holds. [6 marks]

```pseudocode
DECLARE LineOfText : STRING
DECLARE Visitors, BusyDays, Days : INTEGER

BusyDays ← 0
Days ← 0
OPENFILE "Visitors.txt" FOR READ
WHILE NOT EOF("Visitors.txt")
   READFILE "Visitors.txt", LineOfText
   Visitors ← STR_TO_NUM(LineOfText)
   Days ← Days + 1
   IF Visitors > 100 THEN
      BusyDays ← BusyDays + 1
   ENDIF
ENDWHILE
CLOSEFILE "Visitors.txt"
OUTPUT BusyDays, " busy days out of ", Days
```

- file opened in READ mode [B1]
- loop that continues until EOF [B1]
- READFILE inside the loop into a STRING variable [B1]
- converts the line with STR_TO_NUM and compares it with 100 [B1]
- both counters initialised to 0 and incremented correctly [B1]
- file closed, then both counts output after the loop [B1]

If the file holds 85, 120, 100, 143, 99, 101 and 90, three lines exceed 100 (120, 143 and 101) and the file has 7 lines, so the output is `3 busy days out of 7`. The value 100 itself is not more than 100.
:::

```python
with open("visitors.txt", "w") as file:
    for count in [85, 120, 100, 143, 99, 101, 90]:
        file.write(str(count) + "\n")

busy_days = 0
days = 0
with open("visitors.txt", "r") as file:
    for line_of_text in file:
        visitors = int(line_of_text)
        days = days + 1
        if visitors > 100:
            busy_days = busy_days + 1
print(busy_days, "busy days out of", days)
```

Output:

```output
3 busy days out of 7
```

(`int(line_of_text)` accepts the trailing newline, so no `strip()` is needed here. Use `strip()` whenever you compare a line with text.)

**Searching a file.** To find out whether a name is in a file, stop as soon as it is found. The loop therefore has two reasons to end: the name was found, or the file has run out. A function suits it, because the answer is one Boolean.

```pseudocode
FUNCTION NameInFile(SearchName : STRING) RETURNS BOOLEAN
   DECLARE Found : BOOLEAN
   DECLARE LineOfText : STRING
   Found ← FALSE
   OPENFILE "Visitors.txt" FOR READ
   WHILE NOT EOF("Visitors.txt") AND NOT Found
      READFILE "Visitors.txt", LineOfText
      IF LineOfText = SearchName THEN
         Found ← TRUE
      ENDIF
   ENDWHILE
   CLOSEFILE "Visitors.txt"
   RETURN Found
ENDFUNCTION
```

Notice that the file is closed **before** the RETURN. A RETURN ends the function at once, so a CLOSEFILE placed after it would never run. That is why this function uses a flag and a single RETURN at the end, rather than returning from inside the loop.

```python
with open("visitors.txt", "w") as file:
    file.write("Amara\nBilal\nChen\n")


def name_in_file(search_name):
    found = False
    file = open("visitors.txt", "r")
    line = file.readline()
    while line != "" and not found:
        if line.strip() == search_name:
            found = True
        line = file.readline()
    file.close()
    return found


print(name_in_file("Bilal"), name_in_file("Zara"))
```

Output:

```output
True False
```

**Saving records.** A file stores strings, so to save a record you join its fields into one line with a separator such as a comma, and to load it you split the line at the comma. A pupil's name and mark become `Amina,78`. The procedure below adds one record to the end of `Results.txt`; APPEND creates the file if it does not exist yet and never disturbs the lines already there.

```pseudocode
PROCEDURE SaveResult(PupilName : STRING, Mark : INTEGER)
   OPENFILE "Results.txt" FOR APPEND
   WRITEFILE "Results.txt", PupilName & "," & NUM_TO_STR(Mark)
   CLOSEFILE "Results.txt"
ENDPROCEDURE
```

To read a record back, find the comma, take the text before it as the name and the text after it as the mark. The string functions from the Paper 2 insert do this.

```pseudocode
PROCEDURE ShowResults()
   DECLARE LineOfText, PupilName : STRING
   DECLARE Mark, Position : INTEGER
   OPENFILE "Results.txt" FOR READ
   WHILE NOT EOF("Results.txt")
      READFILE "Results.txt", LineOfText
      Position ← 1
      WHILE MID(LineOfText, Position, 1) <> ","
         Position ← Position + 1
      ENDWHILE
      PupilName ← LEFT(LineOfText, Position - 1)
      Mark ← STR_TO_NUM(RIGHT(LineOfText, LENGTH(LineOfText) - Position))
      OUTPUT PupilName, " scored ", Mark
   ENDWHILE
   CLOSEFILE "Results.txt"
ENDPROCEDURE
```

For the line `Amina,78` the comma is at position 6, the name is `LEFT(LineOfText, 5)` which is `"Amina"`, and the mark is the last \(8 - 6 = 2\) characters, `"78"`. If the three calls `CALL SaveResult("Amina", 78)`, `CALL SaveResult("Tomas", 64)` and `CALL SaveResult("Ngozi", 91)` are followed by `CALL ShowResults()`, the output is:

```output
Amina scored 78
Tomas scored 64
Ngozi scored 91
```

In Python, `split(",")` does the splitting in one step and returns a list of strings:

```python
def save_result(pupil_name, mark):
    with open("results.txt", "a") as file:
        file.write(pupil_name + "," + str(mark) + "\n")


def show_results():
    with open("results.txt", "r") as file:
        for line in file:
            pupil_name, mark = line.strip().split(",")
            print(pupil_name, "scored", int(mark))


save_result("Amina", 78)
save_result("Tomas", 64)
save_result("Ngozi", 91)
show_results()
```

Output:

```output
Amina scored 78
Tomas scored 64
Ngozi scored 91
```

:::warn File mistakes that lose marks
1. Opening an existing data file FOR WRITE when you meant to add to it. All the old lines are lost; use APPEND.
2. Reading with READFILE after EOF is TRUE, or testing EOF on a file that is not open in READ mode. Both are errors.
3. Calculating with a line without converting it: `"85" + 1` is not a number. Use STR_TO_NUM first.
4. Forgetting CLOSEFILE, or placing it after a RETURN where it can never run.
5. Opening the same file in READ and WRITE at the same time. Close it first, then open it in the other mode.
:::

:::eg Spot the error: adding a name to a file
Question: A file `Pupils.txt` already holds the names of pupils, one per line. Write a procedure `AddPupil` that takes a name as a parameter and adds it to the end of the file. [4 marks]

A student wrote:

```pseudocode
01  PROCEDURE AddPupil(NewName : STRING)
02     OPENFILE "Pupils.txt" FOR WRITE
03     WRITEFILE "Pupils.txt", NewName
04     CLOSEFILE "Pupils.txt"
05  ENDPROCEDURE
```

Lines 01 and 05 form a correct procedure with the name as a parameter [B1]. **Line 02 opens the file in WRITE mode, which creates a new empty file and loses every name already stored. It must be `FOR APPEND`** [B0]. Line 03 writes the new name as one line [B1]. Line 04 closes the file [B1]. The answer scores 3 out of 4.

With the file holding Amara, Bilal and Chen, calling `CALL AddPupil("Dina")` as written leaves a file holding only Dina. The corrected line 02 is `OPENFILE "Pupils.txt" FOR APPEND`, and the file then holds all four names.
:::

## Abstract data types

An array holds values. But many problems need a collection with **rules** about how items go in and out: a pile of plates where only the top one can be taken, a queue at a bus stop where the person who arrived first is served first. Programmers describe such a collection by the operations it offers, not by how it is built.

:::def Abstract data type (ADT)
A collection of data together with a set of operations that can be performed on that data. The description says what the operations do, not how the data is stored.
:::

"Abstract" means the user of an ADT does not need to know how it is stored inside. The same stack can be built from an array, from a linked list or from a ready-made library. This chapter builds three ADTs from arrays, the way Paper 2 asks: the **stack**, the **queue** and the **linked list**. At AS you do not have to write their code from memory, but you must understand it well enough to show the contents of an array after a series of operations, and to describe how an item is added or removed.

## Stacks

:::def Stack
An ADT in which items are added to and removed from the same end, called the top, so the item removed is always the one most recently added. It is a last in, first out (LIFO) structure.
:::

:::def LIFO
Last in, first out: the last item added is the first one to be removed.
:::

:::analogy
A stack is a pile of plates. You put a clean plate on the top and take the next plate from the top. You cannot take the bottom plate without first lifting off all the others.
:::

A stack has three operations.

- **Push** adds an item to the top.
- **Pop** removes the top item and returns it.
- **Peek** returns the top item **without removing it**.

Stacks are used wherever the latest thing must be dealt with first: the **undo** command in an editor (the last change is undone first), the **back button** in a web browser (the page you came from most recently), and the **call stack**, where a computer remembers where to return to when procedures call other procedures. Pushing the letters of a word and then popping them all returns the letters in **reverse** order.

### A stack in an array

To store a stack in an array you need the array and one extra variable, the **top pointer**, which holds the index of the item at the top. When the stack is empty there is no top item, so the pointer is 0 (arrays here start at 1).

:::def Top pointer
A variable that holds the index of the item at the top of a stack. It is 0 when the stack is empty (for an array that starts at index 1).
:::

:::def Stack overflow
The error that happens when an item is pushed onto a stack that is already full.
:::

:::def Stack underflow
The error that happens when an item is popped from (or peeked at) a stack that is empty.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 212" role="img" aria-label="A stack stored in an array of five elements, drawn with index 5 at the top. Index 1 holds 12, index 2 holds 7 and index 3 holds 5; indexes 4 and 5 are empty. An arrow points at index 3 and is labelled Top = 3."><text class="tl tb" x="20" y="18">Stack : ARRAY[1:5] OF INTEGER</text><rect class="fp s-acc sw2" x="110" y="28" width="80" height="30"/><rect class="fp s-acc sw2" x="110" y="58" width="80" height="30"/><rect class="f1 s-acc sw2" x="110" y="88" width="80" height="30"/><rect class="fm s-acc sw2" x="110" y="118" width="80" height="30"/><rect class="fm s-acc sw2" x="110" y="148" width="80" height="30"/><text class="tl tc" x="150" y="108">5</text><text class="tl tc" x="150" y="138">7</text><text class="tl tc" x="150" y="168">12</text><text class="tl te" x="100" y="48">5</text><text class="tl te" x="100" y="78">4</text><text class="tl te" x="100" y="108">3</text><text class="tl te" x="100" y="138">2</text><text class="tl te" x="100" y="168">1</text><line class="c2 sw2" x1="238" y1="103" x2="196" y2="103" marker-end="url(#ah)"/><text class="tl" x="244" y="108">Top = 3</text><text class="tl" x="20" y="202">Push 12, Push 7, Push 30, Pop, Push 5</text></svg><figcaption>The stack after the operations written under it. The top pointer is 3, so the stack holds 12, 7 and 5 with 5 on top, and positions 4 and 5 are free.</figcaption></figure>
:::

Here are the stack operations in pseudocode for an array of five integers. The array and the pointer are global.

```pseudocode
DECLARE Stack : ARRAY[1:5] OF INTEGER
DECLARE TopPointer : INTEGER

TopPointer ← 0

PROCEDURE Push(NewItem : INTEGER)
   IF TopPointer = 5 THEN
      OUTPUT "Stack overflow"
   ELSE
      TopPointer ← TopPointer + 1
      Stack[TopPointer] ← NewItem
   ENDIF
ENDPROCEDURE

FUNCTION Pop() RETURNS INTEGER
   DECLARE Item : INTEGER
   IF TopPointer = 0 THEN
      OUTPUT "Stack underflow"
      RETURN -1
   ELSE
      Item ← Stack[TopPointer]
      TopPointer ← TopPointer - 1
      RETURN Item
   ENDIF
ENDFUNCTION
```

`Push` first checks whether the stack is full, because writing to `Stack[6]` would be an error. It then moves the pointer **up** and stores the item. `Pop` checks the stack is not empty, reads the item at the pointer and moves the pointer **down**. It returns -1 when the stack is empty, which is safe here only because the stack holds non-negative numbers; a question states what an empty pop should return. Peek is just `RETURN Stack[TopPointer]` with the same empty test and no change to the pointer.

:::key Stack operations and the pointer
- Push: check not full (`TopPointer = size` means full), then **add 1 to the pointer**, then store the item.
- Pop: check not empty (`TopPointer = 0` means empty), then read the item, then **subtract 1 from the pointer**.
- The pointer moves **after** a pop and **before** a push.
- Popping does not erase the old value from the array: it stays there, ignored, until another push writes over it.
:::

:::eg Tracing stack operations
A stack of five integers is empty. These operations are carried out in order: Push 12, Push 7, Push 30, Pop, Push 5, Pop, Pop, Pop, Pop. Complete the trace table. Show the value returned by each Pop and any error message.

Write the TopPointer column from the pointer rules, and write an array element only when a push stores a value in it. A pop changes the pointer but not the array.

| Operation | TopPointer | Stack[1] | Stack[2] | Stack[3] | Result |
|---|---|---|---|---|---|
| start | 0 | | | | |
| Push 12 | 1 | 12 | | | |
| Push 7 | 2 | | 7 | | |
| Push 30 | 3 | | | 30 | |
| Pop | 2 | | | | 30 |
| Push 5 | 3 | | | 5 | |
| Pop | 2 | | | | 5 |
| Pop | 1 | | | | 7 |
| Pop | 0 | | | | 12 |
| Pop | | | | | Stack underflow |

Stack[1] to Stack[3] are the only elements used (Stack[4] and Stack[5] are never written). The first Pop returns 30, the last pushed. The push of 5 then overwrites the stale 30 in `Stack[3]`. The last Pop finds TopPointer 0, outputs "Stack underflow" and leaves the pointer at 0.
:::

The same operations in Python, with the array as a list of five items. Python lists count from 0, so the item at pseudocode position `p` is `stack[p - 1]`, and the top pointer still holds the pseudocode position 0 to 5.

```python
stack = [0] * 5
top_pointer = 0


def push(new_item):
    global top_pointer
    if top_pointer == 5:
        print("Stack overflow")
    else:
        top_pointer = top_pointer + 1
        stack[top_pointer - 1] = new_item


def pop():
    global top_pointer
    if top_pointer == 0:
        print("Stack underflow")
        return -1
    item = stack[top_pointer - 1]
    top_pointer = top_pointer - 1
    return item


push(12)
push(7)
push(30)
print(pop())
push(5)
print(pop(), pop(), pop())
print(pop())
print(stack, top_pointer)
```

Output:

```output
30
5 7 12
Stack underflow
-1
[12, 7, 5, 0, 0] 0
```

The last line shows that the stack is empty (the pointer is 0) although the list still holds the old values 12, 7 and 5. Python lists can also be used as ready-made stacks: `append(x)` pushes, `pop()` removes and returns the last item, and `stack[-1]` is a peek. The version above is the one to write when a question says "using an array".

```python
word = "LIMA"
letters = []
for letter in word:
    letters.append(letter)
reversed_word = ""
while len(letters) > 0:
    reversed_word = reversed_word + letters.pop()
print(reversed_word)
```

Output:

```output
AMIL
```

The widget below is the same stack. Push values, pop them, and watch the pointer. A value in brackets is still in the array but is no longer part of the stack. Try pushing until you see the overflow message, and popping an empty stack.

:::html
<div class="widget" data-w="cs-stack" data-type="stack" data-size="5" data-items="12,7,30"></div>
:::

:::eg Describing a stack after operations (exam style)
A stack that can hold six items is stored in the array `Stack`, with a top pointer, and is empty. The operations Push "red", Push "blue", Pop, Push "green", Push "pink" are carried out in that order. State the value of the top pointer and the contents of `Stack[1]` to `Stack[3]`. [4 marks]

Track the pointer and what each operation writes. Pop returns "blue" and moves the pointer down, but "blue" stays in `Stack[2]` until something overwrites it.

- the top pointer is 3 [B1]
- `Stack[1]` holds "red" [B1]
- `Stack[2]` holds "green", which replaced "blue" [B1]
- `Stack[3]` holds "pink" [B1]
:::

## Queues

:::def Queue
An ADT in which items are added at one end, the rear, and removed from the other end, the front, so the item removed is always the one that has waited longest. It is a first in, first out (FIFO) structure.
:::

:::def FIFO
First in, first out: the first item added is the first one to be removed.
:::

A queue has two main operations: **enqueue** adds an item at the rear, and **dequeue** removes and returns the item at the front. It is used where things must be dealt with in the order they arrive: the print jobs waiting for a shared printer, characters typed on a keyboard waiting for the processor to read them (a buffer), and processes waiting for the processor in a scheduling system.

A queue in an array needs the array and **two pointers**.

:::def Front pointer and rear pointer
The front pointer holds the index of the first item in a queue, the next to be removed. The rear pointer holds the index of the last item added.
:::

This chapter uses these conventions (a question tells you its own). The array starts at 1. At the start the front pointer is 1 and the rear pointer is 0, which means "empty". Enqueue moves the rear pointer **up** before storing. Dequeue reads the item at the front pointer and moves the front pointer **up**.

```pseudocode
DECLARE Queue : ARRAY[1:6] OF STRING
DECLARE FrontPointer, RearPointer : INTEGER

FrontPointer ← 1
RearPointer ← 0

PROCEDURE Enqueue(NewItem : STRING)
   IF RearPointer = 6 THEN
      OUTPUT "Queue full"
   ELSE
      RearPointer ← RearPointer + 1
      Queue[RearPointer] ← NewItem
   ENDIF
ENDPROCEDURE

FUNCTION Dequeue() RETURNS STRING
   DECLARE Item : STRING
   IF FrontPointer > RearPointer THEN
      OUTPUT "Queue empty"
      RETURN ""
   ELSE
      Item ← Queue[FrontPointer]
      FrontPointer ← FrontPointer + 1
      RETURN Item
   ENDIF
ENDFUNCTION
```

The queue is empty when the front pointer has passed the rear pointer (`FrontPointer > RearPointer`), which is true at the start (1 > 0).

### The problem with a linear queue

In this **linear queue** the pointers only ever move forward. Watch what happens to a print queue of six places. The jobs are called J1 to J7.

:::eg Tracing a linear queue
Six print jobs J1 to J6 are enqueued, then three jobs are dequeued, then J7 is enqueued. The array has six elements. Complete the trace table, writing the Queue column as the six elements in order with `_` for an empty element.

Dequeue never changes the array: it only moves the front pointer. So the Queue column changes only on an enqueue.

| Operation | FrontPointer | RearPointer | Queue | Result |
|---|---|---|---|---|
| start | 1 | 0 | _ _ _ _ _ _ | |
| Enqueue J1 | | 1 | J1 _ _ _ _ _ | |
| Enqueue J2 | | 2 | J1 J2 _ _ _ _ | |
| Enqueue J3 | | 3 | J1 J2 J3 _ _ _ | |
| Enqueue J4 | | 4 | J1 J2 J3 J4 _ _ | |
| Enqueue J5 | | 5 | J1 J2 J3 J4 J5 _ | |
| Enqueue J6 | | 6 | J1 J2 J3 J4 J5 J6 | |
| Dequeue | 2 | | | J1 |
| Dequeue | 3 | | | J2 |
| Dequeue | 4 | | | J3 |
| Enqueue J7 | | | | Queue full |

The queue holds only three jobs (J4, J5 and J6), yet J7 is refused: the rear pointer has reached 6, and nothing in this design can reuse the three places at the front that the dequeued jobs freed.
:::

This is the weakness of the linear queue: the space at the front is wasted. Two fixes exist. One is to shift every item forward after each dequeue, which is slow. The better one is the **circular queue**.

### The circular queue

:::def Circular queue
A queue stored in an array in which the pointers wrap round from the last element to the first, so that places freed at the front are reused. It is full only when every element is in use.
:::

When a pointer would move past the end of the array, it goes back to the first element instead. The wrap uses the remainder operator MOD. For an array of 6 elements numbered 1 to 6, the next position after position \(p\) is `p MOD 6 + 1`:

| Current position \(p\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `p MOD 6 + 1` | 2 | 3 | 4 | 5 | 6 | 1 |

At position 6, \(6 \bmod 6 = 0\) and \(0 + 1 = 1\), so the pointer wraps to the start. A circular queue also needs a way to tell "full" from "empty", because in both cases the front pointer can sit just after the rear pointer. The simplest way is a **count** of the items held.

:::html
<figure class="fig small"><svg viewBox="0 0 340 185" role="img" aria-label="A circular queue of six elements, indexes 1 to 6. Index 1 holds J7 and is labelled Rear. Indexes 2 and 3 hold J2 and J3 in brackets, meaning old values no longer in the queue. Index 4 holds J4 and is labelled Front. Indexes 5 and 6 hold J5 and J6. A curved arrow from index 6 back to index 1 is labelled: wraps round, 6 MOD 6 + 1 = 1."><text class="tl tc" x="45" y="30">Rear</text><line class="c2 sw2" x1="45" y1="40" x2="45" y2="56" marker-end="url(#ah)"/><text class="tl tc" x="195" y="30">Front</text><line class="c2 sw2" x1="195" y1="40" x2="195" y2="56" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="20" y="60" width="50" height="36"/><text class="tl tc" x="45" y="83">J7</text><rect class="fp s-acc sw2" x="70" y="60" width="50" height="36"/><text class="tl tc" x="95" y="83">(J2)</text><rect class="fp s-acc sw2" x="120" y="60" width="50" height="36"/><text class="tl tc" x="145" y="83">(J3)</text><rect class="fm s-acc sw2" x="170" y="60" width="50" height="36"/><text class="tl tc" x="195" y="83">J4</text><rect class="fm s-acc sw2" x="220" y="60" width="50" height="36"/><text class="tl tc" x="245" y="83">J5</text><rect class="fm s-acc sw2" x="270" y="60" width="50" height="36"/><text class="tl tc" x="295" y="83">J6</text><text class="tl tc" x="45" y="114">1</text><text class="tl tc" x="95" y="114">2</text><text class="tl tc" x="145" y="114">3</text><text class="tl tc" x="195" y="114">4</text><text class="tl tc" x="245" y="114">5</text><text class="tl tc" x="295" y="114">6</text><path class="c1 sw2" d="M 295 124 C 295 158 45 158 45 124" marker-end="url(#ah)"/><text class="tl tc" x="170" y="176">wraps round: 6 MOD 6 + 1 = 1</text></svg><figcaption>A circular queue of six places after J1 to J6 were enqueued, J1 to J3 dequeued and J7 enqueued. J7 went into place 1, which J1 had freed. The queue holds J4, J5, J6 and J7, in that order; the bracketed values are stale.</figcaption></figure>
:::

```pseudocode
DECLARE Queue : ARRAY[1:6] OF STRING
DECLARE FrontPointer, RearPointer, Count : INTEGER

FrontPointer ← 1
RearPointer ← 0
Count ← 0

PROCEDURE Enqueue(NewItem : STRING)
   IF Count = 6 THEN
      OUTPUT "Queue full"
   ELSE
      RearPointer ← RearPointer MOD 6 + 1
      Queue[RearPointer] ← NewItem
      Count ← Count + 1
   ENDIF
ENDPROCEDURE

FUNCTION Dequeue() RETURNS STRING
   DECLARE Item : STRING
   IF Count = 0 THEN
      OUTPUT "Queue empty"
      RETURN ""
   ELSE
      Item ← Queue[FrontPointer]
      FrontPointer ← FrontPointer MOD 6 + 1
      Count ← Count - 1
      RETURN Item
   ENDIF
ENDFUNCTION
```

The queue is **full** when `Count = 6` and **empty** when `Count = 0`. The wrap is the only change from the linear version.

:::eg Tracing a circular queue
The same operations as before happen to a circular queue of six elements: Enqueue J1 to J6, three Dequeues, Enqueue J7. Show the pointers and the count.

After the six enqueues, the front pointer is 1, the rear pointer is 6 and the count is 6. Each dequeue moves the front pointer on by one place and reduces the count. The final enqueue finds the count is only 3, so it is allowed, and it wraps the rear pointer.

| Operation | FrontPointer | RearPointer | Count | Queue | Result |
|---|---|---|---|---|---|
| after six Enqueues | 1 | 6 | 6 | J1 J2 J3 J4 J5 J6 | |
| Dequeue | 2 | | 5 | | J1 |
| Dequeue | 3 | | 4 | | J2 |
| Dequeue | 4 | | 3 | | J3 |
| Enqueue J7 | | 1 | 4 | J7 J2 J3 J4 J5 J6 | |

The rear pointer becomes \(6 \bmod 6 + 1 = 1\) and J7 goes into `Queue[1]`, the place J1 left. The queue now holds J4, J5, J6 and J7 in that order, from the front pointer 4 onwards and wrapping round to place 1. J2 and J3 are still in the array but are stale.
:::

This is exactly the structure of the Paper 4 circular-queue task, which stores the queue in a global one-dimensional array with pointers and a counter. In Python:

```python
queue = [""] * 6
front_pointer = 1
rear_pointer = 0
count = 0


def enqueue(new_item):
    global rear_pointer, count
    if count == 6:
        print("Queue full")
    else:
        rear_pointer = rear_pointer % 6 + 1
        queue[rear_pointer - 1] = new_item
        count = count + 1


def dequeue():
    global front_pointer, count
    if count == 0:
        print("Queue empty")
        return ""
    item = queue[front_pointer - 1]
    front_pointer = front_pointer % 6 + 1
    count = count - 1
    return item


for job in ["J1", "J2", "J3", "J4", "J5", "J6"]:
    enqueue(job)
print(dequeue(), dequeue(), dequeue())
enqueue("J7")
print(queue, front_pointer, rear_pointer, count)
```

Output:

```output
J1 J2 J3
['J7', 'J2', 'J3', 'J4', 'J5', 'J6'] 4 1 4
```

Use the widget to compare the two designs. Enqueue six jobs and dequeue three on the **Queue** tab and then try one more enqueue; do the same on the **Circular queue** tab.

:::html
<div class="widget" data-w="cs-stack" data-type="circular" data-size="6" data-items="J1,J2,J3,J4,J5,J6"></div>
:::

:::exam Justifying a stack or a queue
Match the structure to the order in which items must be dealt with, and say so. "A queue, because the print jobs must be printed in the order they were sent [B1], so the first job to arrive is the first one printed [B1]" scores. "A stack, because the most recent change must be undone first, so the last item added is the first one removed" is the answer for an undo feature.
:::

## Linked lists

Inserting a new value into the middle of a sorted array is slow, because every later element has to move along one place to make room. A **linked list** avoids this. Its items are stored in **nodes** that do not have to be next to each other in memory, and each node says where the next one is.

:::def Linked list
An ADT in which each item is stored in a node that holds the data and a pointer to the next node in the list, so that the order of the items is given by the pointers and not by where the nodes are stored.
:::

:::def Node
One item of a linked list: the data value, and a pointer to the next node.
:::

:::def Pointer
A value that identifies where another item is stored. In a linked list stored in arrays, a pointer is the index of the next node.
:::

:::def Null pointer
A pointer value that points to nothing. The last node of a list holds it, which marks the end of the list. This chapter uses 0 as the null pointer, because array indexes start at 1; a question may use −1.
:::

A list needs a **start pointer**, the index of the first node. To follow the list, start there, read the data, then jump to the node the pointer names, and repeat until you reach the null pointer.

### A linked list in arrays

In a Paper 2 question a linked list is stored in two parallel arrays of the same size. `Data` holds the values, and `Pointer` holds, at the same index, the index of the **next** node. Two variables hold the ends: `StartPointer` for the first node of the list and `FreePointer` for the first of the unused nodes.

:::def Free list
A linked list of the unused nodes of the array. Every node is either in the list holding data or in the free list waiting to be used, and a variable (the free pointer) points to the first free node.
:::

Here is a list of four names in alphabetical order, stored in arrays of seven nodes. The nodes are not in alphabetical order in the array, but the pointers put them in order.

:::html
<figure class="fig small"><svg viewBox="0 0 340 275" role="img" aria-label="A linked list of four nodes drawn from top to bottom, each a data box and a pointer box. StartPointer = 3 points to the node at index 3, holding Bilal with pointer 4. That points to the node at index 4, holding Chen with pointer 1. That points to the node at index 1, holding Dina with pointer 2. That points to the node at index 2, holding Farah with pointer 0, which means the null pointer."><text class="tl" x="100" y="18">StartPointer = 3</text><line class="c2 sw2" x1="137" y1="28" x2="137" y2="37" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="100" y="40" width="74" height="34"/><rect class="f1 s-acc sw2" x="174" y="40" width="34" height="34"/><text class="tl tc" x="137" y="62">Bilal</text><text class="tl tc" x="191" y="62">4</text><text class="tl te" x="92" y="62">index 3</text><path class="c1 sw2" d="M 191 74 L 191 86 L 137 86 L 137 97" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="100" y="100" width="74" height="34"/><rect class="f1 s-acc sw2" x="174" y="100" width="34" height="34"/><text class="tl tc" x="137" y="122">Chen</text><text class="tl tc" x="191" y="122">1</text><text class="tl te" x="92" y="122">index 4</text><path class="c1 sw2" d="M 191 134 L 191 146 L 137 146 L 137 157" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="100" y="160" width="74" height="34"/><rect class="f1 s-acc sw2" x="174" y="160" width="34" height="34"/><text class="tl tc" x="137" y="182">Dina</text><text class="tl tc" x="191" y="182">2</text><text class="tl te" x="92" y="182">index 1</text><path class="c1 sw2" d="M 191 194 L 191 206 L 137 206 L 137 217" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="100" y="220" width="74" height="34"/><rect class="f1 s-acc sw2" x="174" y="220" width="34" height="34"/><text class="tl tc" x="137" y="242">Farah</text><text class="tl tc" x="191" y="242">0</text><text class="tl te" x="92" y="242">index 2</text><text class="tl" x="218" y="242">0 = null pointer</text></svg><figcaption>Each node is a data box and a pointer box. The pointer holds the index of the next node, so the list reads Bilal, Chen, Dina, Farah even though they are stored at indexes 3, 4, 1 and 2. The pointer 0 in the last node marks the end.</figcaption></figure>
:::

Traversing (outputting) the list follows the pointers:

```pseudocode
PROCEDURE ShowList()
   DECLARE Current : INTEGER
   Current ← StartPointer
   WHILE Current <> 0
      OUTPUT Data[Current]
      Current ← Pointer[Current]
   ENDWHILE
ENDPROCEDURE
```

An empty list has `StartPointer` 0, and every node is in the free list: node 1 points to node 2, node 2 to node 3, and so on, with the last node holding 0.

```pseudocode
DECLARE Data : ARRAY[1:7] OF STRING
DECLARE Pointer : ARRAY[1:7] OF INTEGER
DECLARE StartPointer, FreePointer : INTEGER

PROCEDURE StartEmpty()
   DECLARE Index : INTEGER
   StartPointer ← 0
   FreePointer ← 1
   FOR Index ← 1 TO 6
      Pointer[Index] ← Index + 1
   NEXT Index
   Pointer[7] ← 0
ENDPROCEDURE
```

### Adding a node in order

To insert a value in alphabetical order, you take a node from the free list, store the value in it, find where it belongs, and change the pointers so it joins the list. Nothing is moved: only two pointers change.

:::steps
1. If `FreePointer` is 0, there are no free nodes and the list is full.
2. Take the first free node: `NewNode ← FreePointer`, then move the free pointer on with `FreePointer ← Pointer[NewNode]`.
3. Store the value: `Data[NewNode] ← NewItem`.
4. Walk along the list from the start, keeping the previous node, until the current node holds a value that is not smaller than the new one, or you reach the null pointer.
5. Make the new node point to the current node: `Pointer[NewNode] ← Current`.
6. Make the previous node (or the start pointer, if the new node is first) point to the new node.
:::

```pseudocode
PROCEDURE InsertInOrder(NewItem : STRING)
   DECLARE NewNode, Previous, Current : INTEGER
   IF FreePointer = 0 THEN
      OUTPUT "List full"
   ELSE
      NewNode ← FreePointer
      FreePointer ← Pointer[NewNode]
      Data[NewNode] ← NewItem
      Previous ← 0
      Current ← StartPointer
      WHILE Current <> 0 AND Data[Current] < NewItem
         Previous ← Current
         Current ← Pointer[Current]
      ENDWHILE
      Pointer[NewNode] ← Current
      IF Previous = 0 THEN
         StartPointer ← NewNode
      ELSE
         Pointer[Previous] ← NewNode
      ENDIF
   ENDIF
ENDPROCEDURE
```

The loop condition tests `Current <> 0` first, so `Data[0]`, which does not exist, is never read. (In Python the same test works because `and` stops as soon as its left side is false.)

:::eg Inserting Chen into a list
The list holds Bilal, Dina and Farah in the arrays below (`StartPointer` is 3 and `FreePointer` is 4). Show the arrays after `CALL InsertInOrder("Chen")`.

The free node is 4, so `FreePointer` becomes `Pointer[4]` = 5. Walking from the start: node 3 holds Bilal, which is smaller than Chen, so Previous is 3 and Current is 1. Node 1 holds Dina, which is not smaller than Chen, so the walk stops. Chen's node points to Dina's node (`Pointer[4] ← 1`) and Bilal's node points to Chen's (`Pointer[3] ← 4`).

| Index | Data before | Pointer before | Data after | Pointer after |
|---|---|---|---|---|
| 1 | Dina | 2 | Dina | 2 |
| 2 | Farah | 0 | Farah | 0 |
| 3 | Bilal | 1 | Bilal | 4 |
| 4 | | 5 | Chen | 1 |
| 5 | | 6 | | 6 |
| 6 | | 7 | | 7 |
| 7 | | 0 | | 0 |

`StartPointer` stays 3 and `FreePointer` changes from 4 to 5. Only three array cells changed: `Data[4]`, `Pointer[4]` and `Pointer[3]`. The list now reads Bilal (3), Chen (4), Dina (1), Farah (2).
:::

:::warn Change the pointers in the right order
Join the **new** node to the rest of the list **before** you join the old node to the new one. In the example, `Pointer[4] ← Pointer[3]` (Chen points to Dina) must happen before `Pointer[3] ← 4`. Reverse them and `Pointer[3]` is already 4, so Chen's pointer becomes 4, pointing to itself; Dina and Farah are cut off and the traversal repeats Chen for ever.
:::

Inserting at the front works by the same rule. To insert "Amara" next, the free node is 5. The walk stops at once because Bilal is not smaller than Amara, so Previous stays 0, `Pointer[5]` becomes 3 and `StartPointer` becomes 5.

### Deleting a node

To delete a value, find the node, make the previous node (or the start pointer) skip it, and **return the node to the free list** so its space can be reused.

```pseudocode
PROCEDURE DeleteItem(OldItem : STRING)
   DECLARE Previous, Current : INTEGER
   Previous ← 0
   Current ← StartPointer
   WHILE Current <> 0 AND Data[Current] <> OldItem
      Previous ← Current
      Current ← Pointer[Current]
   ENDWHILE
   IF Current = 0 THEN
      OUTPUT OldItem, " not found"
   ELSE
      IF Previous = 0 THEN
         StartPointer ← Pointer[Current]
      ELSE
         Pointer[Previous] ← Pointer[Current]
      ENDIF
      Pointer[Current] ← FreePointer
      FreePointer ← Current
   ENDIF
ENDPROCEDURE
```

:::eg Deleting Dina from a list
After Chen and Amara have been inserted, the list holds Amara (5), Bilal (3), Chen (4), Dina (1) and Farah (2), with `StartPointer` 5 and `FreePointer` 6. Show the pointer array after `CALL DeleteItem("Dina")`.

Dina is at node 1 and its previous node is 4 (Chen). Chen's pointer skips Dina and takes Dina's pointer, 2 (`Pointer[4] ← 2`). Node 1 then joins the front of the free list: it points to the old free pointer (`Pointer[1] ← 6`) and becomes the new free pointer (`FreePointer ← 1`).

| Index | Data | Pointer before | Pointer after |
|---|---|---|---|
| 1 | Dina | 2 | 6 |
| 2 | Farah | 0 | 0 |
| 3 | Bilal | 4 | 4 |
| 4 | Chen | 1 | 2 |
| 5 | Amara | 3 | 3 |
| 6 | | 7 | 7 |
| 7 | | 0 | 0 |

`StartPointer` is still 5 and `FreePointer` is now 1. The list reads Amara, Bilal, Chen, Farah. `Data[1]` still holds "Dina", but no pointer leads to it from the list, so it is ignored until a later insert takes node 1 from the free list and overwrites it.
:::

To **edit** a value in a list kept in order, delete the old value and insert the new one, so that it ends up in the right place. Changing `Data` in place is safe only when the new value would not change the order.

In Python the arrays are lists of 8 items, with item 0 unused, so that the pointer values 1 to 7 are the list indexes and the null pointer 0 points at the unused slot.

```python
data = [None] * 8
pointer = [0] * 8
start_pointer = 0
free_pointer = 1
for index in range(1, 7):
    pointer[index] = index + 1
pointer[7] = 0


def insert_in_order(new_item):
    global start_pointer, free_pointer
    if free_pointer == 0:
        print("List full")
        return
    new_node = free_pointer
    free_pointer = pointer[new_node]
    data[new_node] = new_item
    previous = 0
    current = start_pointer
    while current != 0 and data[current] < new_item:
        previous = current
        current = pointer[current]
    pointer[new_node] = current
    if previous == 0:
        start_pointer = new_node
    else:
        pointer[previous] = new_node


def delete_item(old_item):
    global start_pointer, free_pointer
    previous = 0
    current = start_pointer
    while current != 0 and data[current] != old_item:
        previous = current
        current = pointer[current]
    if current == 0:
        print(old_item, "not found")
    else:
        if previous == 0:
            start_pointer = pointer[current]
        else:
            pointer[previous] = pointer[current]
        pointer[current] = free_pointer
        free_pointer = current


def list_items():
    items = []
    current = start_pointer
    while current != 0:
        items.append(data[current])
        current = pointer[current]
    return items


for name in ["Dina", "Farah", "Bilal"]:
    insert_in_order(name)
print(list_items(), start_pointer, free_pointer)
insert_in_order("Chen")
insert_in_order("Amara")
print(list_items(), start_pointer, free_pointer)
delete_item("Dina")
print(list_items(), start_pointer, free_pointer)
delete_item("Zara")
print(data[1:], pointer[1:])
```

Output:

```output
['Bilal', 'Dina', 'Farah'] 3 4
['Amara', 'Bilal', 'Chen', 'Dina', 'Farah'] 5 6
['Amara', 'Bilal', 'Chen', 'Farah'] 5 1
Zara not found
['Dina', 'Farah', 'Bilal', 'Chen', 'Amara', None, None] [6, 0, 4, 2, 3, 7, 0]
```

The first line is the example before Chen: inserting Dina, Farah and Bilal into the empty list puts them at nodes 1, 2 and 3. The widget below starts from the same three names. Try Insert with a new name and watch the **Pointer** column; use Delete, then Insert again, to see a freed node reused. Find follows the pointers one node at a time and says how many nodes it visited.

:::html
<div class="widget" data-w="cs-stack" data-type="list" data-size="7" data-items="Dina,Farah,Bilal"></div>
:::

### Choosing the right structure

:::cols
:::col Stack
Last in, first out, one open end. Use it when the **most recent** item must be handled first: undo, the back button, the call stack, reversing.
:::
:::col Queue
First in, first out, two ends. Use it when items must be handled **in the order they arrive**: print jobs, keyboard buffer, process scheduling.
:::
:::col Linked list
Items in order set by pointers. Use it when items are **often inserted or deleted in the middle** of an ordered collection, since only pointers change and nothing is moved.
:::
:::

A linked list also has costs. Each node needs room for a pointer as well as the data, and to reach the 10th item you must follow nine pointers, whereas an array jumps straight to element 10. So a list is a good choice for an ordered collection that changes often, and an array is better when you need quick access to any element and the data rarely changes.

:::exam "Describe how an item is added"
Examiners mark the steps in order: take the node at the free pointer (and move the free pointer on) [B1]; store the data in it [B1]; find where it belongs by following the pointers from the start [B1]; set the new node's pointer to the following node and the previous node's pointer (or the start pointer) to the new node [B1]. Name the pointers: "the pointer of the previous node" is a mark; "change some pointers" is not.
:::

:::try Start easy, finish at exam standard
Q: Give two reasons why a program stores data in a file instead of in variables.
A: Any two of: the data is still there after the program ends; the data can be shared with other programs; a file can hold more data than the program's memory should.
Q: A program must read the existing lines of `Log.txt`, then add new lines to the end, then replace the whole file with a new list. State the file mode for each of the three jobs.
A: READ for reading the existing lines, APPEND for adding to the end, WRITE for replacing the contents.
Q: A stack is empty. Push 4, Push 9, Push 2, Pop. What is the value returned by the Pop and the value of the top pointer?
A: The Pop returns 2, the last item pushed. The pointer was 3 after three pushes and is now 2.
Q: A queue is empty. Enqueue A, Enqueue B, Enqueue C, Dequeue. Which item is returned, and which items are left?
A: A is returned, because it arrived first. B and C are left, with B at the front.
Q: A circular queue has 8 elements numbered 1 to 8. The rear pointer is 8. What is its value after another item is enqueued?
A: \(8 \bmod 8 + 1 = 0 + 1 = 1\). The pointer wraps to the first element (if the queue is not full).
Q: A stack holds five items (top pointer 5) and the array has five elements. What happens on the next Push?
A: The stack is full, so the push causes a stack overflow, and the item is not stored.
Q: In a linked list the pointer in the last node holds 0. What does this mean?
A: 0 is the null pointer: there is no next node, so this is the end of the list.
Q: Write pseudocode that reads the file `Names.txt` and outputs every line.
A: Open for reading, loop until EOF, close.

```pseudocode
DECLARE Line : STRING
OPENFILE "Names.txt" FOR READ
WHILE NOT EOF("Names.txt")
   READFILE "Names.txt", Line
   OUTPUT Line
ENDWHILE
CLOSEFILE "Names.txt"
```

Q: Which structure would you choose to store the pages you have visited so that the back button works: a stack, a queue or a linked list? Give a reason.
A: A stack. The back button returns to the most recently visited page, so the last item added must be the first removed (last in, first out).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Give two reasons why a program stores its data in a text file.
A: Any two of:

- the data is kept after the program has finished or the computer is switched off
- the data can be used by another program, or by the same program on another day
- a file can hold more data than variables in main memory can sensibly keep (accept: data can be read in as it is needed)

Two different reasons [B1] [B1].

Q: [3 marks] ★ A program uses a text file `Stock.txt`. State the file mode that must be used to (a) read the lines already in the file, (b) add a new line after the existing lines, and (c) replace everything in the file with new lines.
A: (a) READ [B1] (b) APPEND [B1] (c) WRITE [B1]

Q: [6 marks] ★★ The text file `Sales.txt` holds the number of items sold on each day of a month, one whole number per line. Write pseudocode to output the total of all the numbers in the file, or the message "No data" if the file is empty.
H: Read each line as a STRING and convert it before adding it.
H: To know whether the file was empty, count the lines read, or compare the total's counter with 0 after the loop.
A: One possible answer:

```pseudocode
DECLARE LineOfText : STRING
DECLARE Total, Lines : INTEGER

Total ← 0
Lines ← 0
OPENFILE "Sales.txt" FOR READ
WHILE NOT EOF("Sales.txt")
   READFILE "Sales.txt", LineOfText
   Total ← Total + STR_TO_NUM(LineOfText)
   Lines ← Lines + 1
ENDWHILE
CLOSEFILE "Sales.txt"
IF Lines = 0 THEN
   OUTPUT "No data"
ELSE
   OUTPUT "Total: ", Total
ENDIF
```

- file opened in READ mode [B1]
- loop until EOF [B1]
- READFILE inside the loop into a STRING variable [B1]
- converts with STR_TO_NUM and adds to a total that started at 0 [B1]
- file closed [B1]
- outputs the total, or "No data" when no lines were read [B1]

Q: [4 marks] ★★ A stack that can hold five integers is stored in the array `Stack`, with a top pointer, and is empty. These operations are carried out in order: Push 8, Push 3, Push 9, Pop, Pop, Push 4, Push 6.

(a) State the two values returned by the Pops. [2]

(b) State the value of the top pointer and the values of `Stack[1]` to `Stack[3]` at the end. [2]
H: A Pop does not erase the array: the old value stays until a Push overwrites it.
A: (a) The first Pop returns 9 [B1] and the second returns 3 [B1].

(b) After three pushes the pointer is 3, the two pops make it 1, and the two pushes make it 3, so the top pointer is 3 [B1]. `Stack[1]` is 8, `Stack[2]` is 4 (it replaced the 3) and `Stack[3]` is 6 (it replaced the 9) [B1].

Q: [4 marks] ★★ A circular queue is stored in an array `Queue` with 5 elements numbered 1 to 5, with a front pointer, a rear pointer and a count. At the start the front pointer is 1, the rear pointer is 0 and the count is 0. These operations happen: Enqueue A, Enqueue B, Enqueue C, Enqueue D, Dequeue, Dequeue, Enqueue E, Enqueue F. State the front pointer, the rear pointer and the count at the end, and the items in the queue in order, front first.
H: The rear pointer goes to \(\text{Rear} \bmod 5 + 1\) after each enqueue; it wraps after position 5.
A: After the four enqueues the front is 1, the rear is 4 and the count is 4. The two dequeues remove A and B, so the front becomes 3 and the count 2. E goes into position 5 (rear 5, count 3). F goes to position \(5 \bmod 5 + 1 = 1\) (rear 1, count 4).

- front pointer 3 [B1]
- rear pointer 1 [B1]
- count 4 [B1]
- the queue holds C, D, E, F in that order, front first [B1]

Q: [7 marks] ★★★ A linked list stores names in alphabetical order in two arrays. `StartPointer` is 2 and `FreePointer` is 5.

| Index | Data | Pointer |
|---|---|---|
| 1 | Joy | 3 |
| 2 | Alba | 4 |
| 3 | Marta | 0 |
| 4 | Ela | 1 |
| 5 | | 6 |
| 6 | | 0 |

(a) Describe how a new name is added to this list so that it stays in alphabetical order. [3]

(b) The name "Hana" is added. State the new value of `Data[5]`, `Pointer[5]`, `Pointer[4]` and `FreePointer`. [4]
H: Find the two nodes that "Hana" must go between by following the pointers from the start.
A: (a) Take the node at the free pointer for the new name, store the name in it and move the free pointer on to the next free node [B1]. Follow the pointers from the start pointer until the next node holds a name that comes after the new name [B1]. Set the new node's pointer to that next node, and set the previous node's pointer (or the start pointer, if it comes first) to the new node [B1].

(b) The list is Alba (2), Ela (4), Joy (1), Marta (3), and "Hana" comes after Ela and before Joy. `Data[5]` is "Hana" [B1]. `Pointer[5]` is 1, the index of Joy [B1]. `Pointer[4]` is 5 [B1]. `FreePointer` is 6, the old `Pointer[5]` [B1].

Q: [6 marks] ★★★ A school computer room has one printer shared by 30 computers. Print jobs are stored in an array.

(a) Justify the use of a queue for the print jobs. [2]

(b) The queue is stored in an array of 20 elements, with a front pointer and a rear pointer that only ever move forward. After many jobs, the queue is reported full although it holds only three jobs. Explain why this happens, and how a circular queue avoids it. [4]
H: Think about what happens to the places freed when jobs are dequeued.
A: (a) Jobs must be printed in the order they arrive, which is first in, first out [B1]. New jobs join at the rear and the printer takes jobs from the front, so a queue makes it fair [B1].

(b) The rear pointer has reached the last element [B1], and the places before the front pointer, freed by jobs that were dequeued, cannot be reused because the pointers never go back [B1]. In a circular queue the pointer wraps round to the first element when it passes the last, using MOD [B1], so freed places are reused and the queue is full only when the count of jobs equals the number of elements [B1].
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A web browser keeps two stacks, Back and Forward. The page being shown is the current page. Visiting a new page pushes the current page onto Back, empties Forward, and shows the new page. Pressing the Back button pushes the current page onto Forward and pops the top of Back to become the current page. The browser starts on page A with both stacks empty. The user visits B, C and D, presses Back twice, then visits E. State the current page and the contents of Back and Forward (top item last) (a) after the two Back presses, and (b) after visiting E. Explain why Forward must be emptied when a new page is visited.
H: Do the visits first: Back holds A, B, C with D current.
H: Each Back press moves one page from the top of Back to current, and the old current page to Forward.
A: Visiting B, C and D leaves Back holding A, B, C (C on top) and D as the current page.

(a) The first Back press pushes D onto Forward and pops C from Back, so C is current. The second pushes C onto Forward and pops B. The current page is B [B1], Back holds A only [B1] and Forward holds D then C, with C on top [B1].

(b) Visiting E pushes B onto Back and empties Forward. The current page is E [B1], Back holds A then B, with B on top [B1], and Forward is empty [B1].

Forward must be emptied because the pages D and C were reached from the old route; once the user goes somewhere new, pressing Forward could not sensibly lead back to them (accept any reason that the forward history is no longer valid).

Q: [6 marks] ★★★ A linked list in arrays holds names in alphabetical order. `StartPointer` is 3 and `FreePointer` is 0.

| Index | Data | Pointer |
|---|---|---|
| 1 | Rao | 2 |
| 2 | Sia | 0 |
| 3 | Ana | 4 |
| 4 | Ken | 5 |
| 5 | Lee | 1 |

(a) Explain why an attempt to add a name fails at the moment. [1]

(b) "Lee" is deleted. State the new values of `Pointer[4]`, `Pointer[5]` and `FreePointer`. [3]

(c) "Mia" is then added. State which index is used for it and the new values of `Pointer[5]` and `Pointer[4]`. [2]
H: A free pointer of 0 is the null pointer.
H: In (b), the node that was Lee's joins the free list. In (c), the free list has exactly one node.
A: (a) `FreePointer` is 0, the null pointer, so there are no free nodes and the list is full [B1].

(b) `Pointer[4]` becomes 1, because Ken's pointer takes Lee's pointer [B1]. `Pointer[5]` becomes 0, the old free pointer, so node 5 is the only node in the free list [B1]. `FreePointer` becomes 5 [B1].

(c) "Mia" is stored in index 5, the node Lee freed [B1]. It goes between Ken and Rao, so `Pointer[5]` is 1 (Rao) and `Pointer[4]` is 5 [B1].
:::

:::quiz
? A stack is empty. The items 4, 8 and 2 are pushed in that order, then one Pop is carried out. What does the Pop return?
- 4
- 8
+ 2
- 14
> A stack is last in, first out, so the Pop returns the item pushed last, 2. The answer 4 is what a queue would return.
? A queue is empty. The items A, B and C are enqueued in that order, then one Dequeue is carried out. What does it return?
+ A
- B
- C
- nothing, because the queue is full
> A queue is first in, first out, so the Dequeue returns A, the item that has waited longest.
? What is a stack overflow?
- Popping from an empty stack.
+ Pushing an item onto a stack that is already full.
- Peeking at the top item of a stack.
- Having more pushes than pops in a program.
> Overflow happens when there is no room to push. Popping from an empty stack is underflow.
? A circular queue is stored in an array of 6 elements numbered 1 to 6, and the rear pointer is 6. The queue is not full. What is the rear pointer after an Enqueue?
- 7
- 0
+ 1
- 6
> The next position is `Rear MOD 6 + 1`, and \(6 \bmod 6 = 0\), so the rear pointer wraps to \(0 + 1 = 1\). The answer 7 would be outside the array.
? A linear queue in an array of 20 elements reports "full" when it holds only 3 items. What is the cause?
- The front pointer is at element 1.
- The array is too small for any queue.
+ The rear pointer has reached the last element, and the places freed at the front cannot be reused.
- The count has become negative.
> In a linear queue the pointers only move forward, so the space before the front pointer is wasted. A circular queue wraps the pointers round and reuses it.
? Why is a linked list a good choice for an ordered list that has many items inserted in the middle?
- Any item can be reached directly by its index.
- It uses less memory than an array.
+ Only pointers change when an item is inserted, so no items have to be moved along.
- The data is stored in alphabetical order in the array.
> In an array that is kept in order, every later item moves along one place to make room. In a linked list the new node is linked in by changing two pointers. The nodes need extra memory for the pointers, and reaching item \(n\) means following \(n - 1\) pointers.
? A file holds 5 lines. A program opens it FOR WRITE, writes one line and closes it. How many lines does the file now hold?
- 6
- 5
+ 1
- 0
> WRITE mode creates a new empty file, so the 5 old lines are lost and only the new line remains. APPEND would give 6.
? What does `EOF("Data.txt")` return?
- The last line of the file.
+ TRUE when there are no more lines to read, and FALSE otherwise.
- The number of lines in the file.
- TRUE when the file has been closed.
> EOF is a test, not a read: it says whether any lines remain. It is used on a file opened in READ mode, normally as the condition of a loop that contains READFILE.
? What is the purpose of the free list in a linked list stored in arrays?
- It holds the items that have been deleted so they can be undone.
+ It links the unused nodes, so a new item can take a free node and a deleted node can be reused.
- It holds the pointers to the start of the list.
- It stores the data in alphabetical order.
> Every node is either in the list or in the free list. Insert takes the node at the free pointer; delete puts the node back at the front of the free list.
:::

:::checklist What you can now do
- [ ] I can explain why files are needed: data persists, can be shared and can be large.
- [ ] I can write pseudocode that opens, reads, writes, appends and closes a text file of one or more lines, using EOF.
- [ ] I can write the same file handling in Python with `open`, `with`, `strip()` and `"\n"`.
- [ ] I can explain what an abstract data type is.
- [ ] I can describe a stack, with push, pop, peek, the top pointer, overflow and underflow, and give uses.
- [ ] I can describe a queue and a circular queue, with enqueue, dequeue, the front and rear pointers and MOD, and give uses.
- [ ] I can describe a linked list, with nodes, the start pointer, the null pointer and the free list.
- [ ] I can show the contents of an array and the pointers after a series of stack, queue or linked-list operations.
- [ ] I can describe how an item is added to and deleted from each structure, stored in arrays.
- [ ] I can justify the use of a stack, a queue or a linked list for a given problem.
:::

:::recap
- A file keeps data after the program ends, lets programs share data and can hold large amounts. A text file is read and written one line (a STRING) at a time.
- `OPENFILE <file> FOR READ | WRITE | APPEND`, `READFILE`, `WRITEFILE`, `EOF` and `CLOSEFILE`. WRITE erases existing data; APPEND adds after it. Test EOF before each READFILE.
- In Python use `open(name, "r" | "w" | "a")` with `with`; `write` needs `"\n"`; `strip()` removes it; `split(",")` splits a record.
- An abstract data type is a collection of data with a set of operations on it.
- A stack is LIFO, with push, pop and peek at one end and a top pointer (0 when empty). Pushing onto a full stack is overflow; popping an empty stack is underflow.
- A queue is FIFO, with enqueue at the rear and dequeue at the front. A linear queue wastes the places freed at the front; a circular queue wraps the pointers with MOD and uses a count to tell full from empty.
- A linked list stores each item in a node with a pointer to the next node, so the order is set by the pointers. It has a start pointer, a null pointer at the end and a free list of unused nodes.
- To insert, take a free node, store the data, and change two pointers (new node to the next, previous to the new node, in that order); to delete, make the previous node skip the node and return it to the free list.
:::

:::links
- practise: [Files: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/files/exam-questions/) · Save My Exams · 9618-style file-handling questions with mark schemes [paid]
- practise: [Introduction to abstract data types: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/exam-questions/) · Save My Exams · stack, queue and linked-list questions [paid]
- explore: [VisuAlgo: stacks, queues and linked lists](https://visualgo.net/en/list) · VisuAlgo · animated insert and delete on each structure
- explore: [Data structure visualisations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) · USF · step through stacks, queues and linked lists
- read: [Python file handling](https://www.w3schools.com/python/python_file_handling.asp) · W3Schools · short lessons on open, read, write and append, with try-it boxes
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · section 9, the official rules for text files

Links checked 13 November 2026.
:::

Next: [The development life cycle and program design](#cs.development)
