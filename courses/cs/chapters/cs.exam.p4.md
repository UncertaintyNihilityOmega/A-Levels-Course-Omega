@chapter cs.exam.p4
@title Paper 4 guide: the Practical
@level guide
@paper CAIE 9618 Paper 4
@time 2–3 hours
@summary What Paper 4 prints and allows, how to share 150 minutes across 75 marks, how to prepare and what to do in the exam hall (the evidence document, exact names, building part by part), how its marks are awarded for each feature of a program, two model answers with code and output, a marked slip, the errors that cost marks, and a practice plan that links the Python toolkit.

:::why
Paper 4 is the only paper you take on a computer, and every mark is for a program that works or for evidence that it works. Two students with the same programming skill can score very differently: one reads every instruction, keeps the names exactly, tests after each part and pastes the evidence as they go, and the other loses marks to a misspelt name, a missing screenshot or a part left unsaved. This guide is about the second kind of skill, which is as learnable as the first.
:::

## The paper at a glance

| Feature | Paper 4 |
|---|---|
| Title | Practical |
| Time | 2 hours 30 minutes |
| Marks | 75 |
| Syllabus content | sections 19 and 20, except low-level programming and declarative programming |
| Weighting | 25% of A Level |
| Where you work | on a computer, in Java (console mode), Python (console mode) or Visual Basic (console mode); no internet or email |
| What you hand in | program code and evidence of testing, in the evidence document |
| Assessment | AO3 only: designing, programming and evaluating computer systems |

The front page of the May/June 2025 paper (9618/41) listed what each candidate needs: the candidate source files and the evidence document. It told candidates to carry out every instruction in each task, to save their work using the file names given, not to use the internet or email, and to save their work in the evidence document, **or no marks will be awarded for that task**. It said that a mark of **zero** is given if a language other than the three allowed is used. The second page said to open the evidence document, save it with the name `evidence_` followed by your centre number and candidate number, and noted that a class declaration can be used to declare a record, and that a list can be used if the language has no arrays.

That paper had 12 pages and **3 questions of 20, 25 and 30 marks**: a circular queue held in a global 1D array with head and tail pointers and a counter; reading a text file, splitting the data and writing it to several text files; and a binary tree designed with object-oriented programming, with a recursive in-order output. Each part said to save the program under a given name and to copy and paste the code into the matching part of the evidence document, and the testing parts asked for a screenshot of the output. Treat this as an example of the style, not as a rule: another paper will use different scenarios. Your own paper's front page tells you what to do, so read it first.

This course teaches Python for this paper. Java and Visual Basic are allowed by the paper but are not taught here.

:::exam What AO3 means for you
All 75 marks are AO3: you design, write and test code. There are no marks for describing a topic. Every mark is for a **feature of your program** (a loop that does the right thing, a method that returns the right value, a file that is written correctly) or for **evidence** (the screenshot that shows the output). If a feature is not in the code you pasted, you cannot earn its mark.
:::

## Spending 150 minutes on 75 marks

There are 150 minutes for 75 marks, which is \(150 \div 75 = 2\) minutes per mark. Programming is slower than writing a theory answer, but it is also easy to lose time without noticing, so plan for a small margin: about **1.8 minutes per mark**, which leaves 15 minutes for the evidence document and the final checks.

| Marks in the question | Minutes at 1.8 per mark |
|---|---|
| 20 | 36 |
| 25 | 45 |
| 30 | 54 |
| All three (75) | 135, which leaves 15 minutes |

The three questions of the May/June 2025 paper would be timed at about 36, 45 and 54 minutes. The questions usually build on each other from simpler to more demanding, and the early parts of each question are the cheapest marks.

:::steps
1. **First five minutes:** open the evidence document and save it with the name the paper gives. Read the whole of Question 1 once. Check that the source files are in your folder.
2. **Work in the order of the paper,** one part at a time, as the next part often uses the one before. Do not skip to the end of a question.
3. **After every part:** run the program, save it with the exact file name, paste the code into the evidence document, and take any screenshot that the part asks for. Do this before you read the next part.
4. **At 15 minutes before the end,** stop starting new parts. Check every file name, run every program once more, and save the evidence document again.
:::

:::tip Marks are the clock
A 4-mark part that has taken 15 minutes should be stopped. Save what you have, paste it into the evidence document, and go on. A working program for most of a question scores far more than a perfect program for half of it.
:::

## Before the exam

You cannot prepare by reading alone. Paper 4 is a skill, like playing an instrument, and it needs practice at a keyboard.

:::steps
1. **Practise in the same conditions.** Use a plain editor and a console, with no internet and no help from an assistant. If your school's exam computers have a particular editor, practise in it. Run your programs from the console, in the folder that holds the data files.
2. **Learn the toolkit** in the table below until you can write each item without looking anything up.
3. **Practise whole tasks,** not fragments. Take a task from [Python for Paper 4: the practical toolkit](#cs.python) or the longer tasks in [Mixed practice: A Level (Papers 3 and 4)](#cs.mixed.a2), set a timer, and finish it, including the evidence routine.
4. **Practise the paste.** Copying code and a screenshot into a document takes about a minute each time. Do it for every part in practice, so that it costs no thought in the exam.
:::

| You should be able to write … | Where it is taught |
|---|---|
| a loop that reads a text file line by line, with `strip()` and `split(",")`, and converts with `int()` or `float()` | [File processing and exception handling](#cs.fileproc) |
| a program that writes or appends to a text file, and `try` / `except` for a missing file or a bad number | [File processing and exception handling](#cs.fileproc) |
| a class with `__init__`, attributes and methods, used as a record or as an object | [Object-oriented programming](#cs.oop) |
| a fixed-size global array as a list, with pointers and a counter, and the index rules for 0-based lists | [Python for Paper 4: the practical toolkit](#cs.python) |
| a stack, a queue, a circular queue, a linked list or a binary tree built with lists or classes | [Abstract data types](#cs.adts) |
| a recursive function with a base case, and a recursive method of a class (for example an in-order traversal) | [Recursion](#cs.recursion) |
| a search or a sort written from the algorithm (linear, binary, bubble, insertion) | [Searching, sorting and Big O](#cs.algorithms2) |
| a validation function and a set of normal, boundary and erroneous test data | [Testing, errors and maintenance](#cs.testing) |
| a message that tells the reader what a traceback says | [Python for Paper 4: the practical toolkit](#cs.python) |

## In the exam hall

### Read the task first, then read it again

A Paper 4 task is written to be followed to the letter. Go through each part with a pencil and mark every instruction: each noun that is a name ("a class `Node`", "a function `Enqueue`", "a file `Output.txt`"), each condition ("returns `False` if the array is full") and each output ("output the message `Queue full`"). A mark scheme has about one mark for each of these. The full method is in [Python for Paper 4: the practical toolkit](#cs.python).

:::key Exact names and exact output
- **Identifiers:** use the names in the question, with the same capitals: `HeadPointer` is not `head_pointer`. A later part, or the examiner's own test, may call your function by the name given. In the exam the task's names beat your usual style.
- **File names:** use the names given for source files, data files and the program files you save. Keep the data files in the same folder as the program, and open them by name only.
- **Output:** print what the part says, in the form it shows. If it says "output the message `Queue full`", print exactly that.
- **Return or print:** "returns" means `return`; "outputs" means `print`. A function that prints when it should return loses the marks for the value.
:::

### Build part by part and run it often

Write a small piece, run it, and only then write the next. A long program written without running it produces a long list of errors, and a traceback in the middle of a program is much harder to read than one in a few new lines. Put a test line at the bottom of the file that calls the new function with simple data. You will need the test for the screenshot anyway.

### Evidence: the part that is easy to forget

The evidence document is the examiner's copy of your work. The front page says no marks will be awarded for a task whose work is not saved in it. After **every** part, in this order:

:::steps
1. Save the program with the file name the question gives.
2. Paste the whole program code into the matching part of the evidence document, in plain text (not an image of the code).
3. For a testing part, run the program with the test data the task gives, and take a screenshot of the console that shows **all** of the output. Paste the screenshot into the evidence document under the right part heading.
4. Save the evidence document.
:::

:::warn Pasting at the end is too late
A student who plans to paste everything in the last ten minutes loses the marks for any part they did not reach, and meets the pasting problems (a missing screenshot, the wrong part heading) with no time to fix them. Paste as you go.
:::

### When you are stuck

Mark points are for features, so a program that is half right still earns marks for the half that is right. When a part will not work:

- **Get it to run** with a simpler version: a function that returns a fixed value, or one that handles only the normal case. Paste that.
- **Do not delete working code** to make a new idea fit. Copy the file, and try the idea in the copy.
- **Read the last line of the traceback** first: it names the error and the line. [Python for Paper 4: the practical toolkit](#cs.python) lists the usual causes.
- **Set a limit:** if five minutes pass with no progress, paste what you have, write a comment saying what is missing, and move on. A comment earns nothing, but it will not cost anything either, and the next part may be easy.

## How the marks are awarded

A Paper 4 mark scheme is a list of **features**, one mark each, with extra marks for the evidence. The features follow the order of the question: the declaration, then each function or method, then the test program, then the output. The table shows what the marks are usually for in each kind of part.

| Kind of part | The marks are for … |
|---|---|
| A data structure (array, queue, stack, linked list, tree) | declaring it with the right size and initial values; each operation (add, remove, search, display) with the right checks (full, empty); each return value; the pointers or the counter updated correctly |
| A text-file part | opening the right file in the right mode; a loop that reads every line; splitting or processing each line; converting types; writing the output lines; closing the file (or `with`); handling a missing file if asked |
| A class or an object part | the class with the right name and attributes; the constructor; each method; the object created with the right values; a method that uses another object or a recursive call |
| A recursive part | the base case; the recursive call with a smaller problem; the result used correctly; the first call from outside |
| A validation or calculation | each rule tested separately; the right result for each case; messages as the task says |
| A testing part | the test calls in the program; the data that the task asks for (normal, boundary, erroneous); a screenshot showing the output |

:::eg Paper 4 style: a ten-mark part, with code, output and mark points
A swimming club in Perth records the best 100 m time of up to six swimmers. The data is held in a **global 1D array** named `Swimmers` of 6 elements, in which an empty element holds `None`. Each swimmer is a record with a name (string) and a time in seconds (real).

(a) Write the declaration of a class `Swimmer` with a constructor that sets the name and the time. [2]

(b) Declare the global array `Swimmers` so that every element is empty. [1]

(c) Write a function `AddSwimmer(Name, Seconds)` that stores a new swimmer in the first empty element and returns `True`. If there is no empty element it returns `False`. [3]

(d) Write a function `Fastest()` that returns the name of the swimmer with the lowest time, or an empty string if the array is empty. [2]

(e) Write a program that calls `AddSwimmer` for these seven swimmers in this order: Ana 62.5, Ben 58.2, Chi 71.0, Dev 55.9, Eli 60.4, Fay 59.8, Gus 54.1. For each one it outputs `Added` and the name, or `Full:` and the name if the swimmer was not stored. It then outputs `Fastest:` and the name returned by `Fastest()`. Run the program and take a screenshot of the output. [2]

In Python:

One word in this solution needs explaining first: `None` is Python's value for "nothing here", and `x is None` tests for it (`x is not None` is the opposite). An empty element of the array holds `None`, so the whole logic of "empty element" is these two tests.

```python
class Swimmer:
    def __init__(self, Name, Seconds):
        self.Name = Name
        self.Seconds = Seconds


Swimmers = [None] * 6


def AddSwimmer(Name, Seconds):
    for Index in range(6):
        if Swimmers[Index] is None:
            Swimmers[Index] = Swimmer(Name, Seconds)
            return True
    return False


def Fastest():
    Best = None
    for Item in Swimmers:
        if Item is not None and (Best is None or Item.Seconds < Best.Seconds):
            Best = Item
    if Best is None:
        return ""
    return Best.Name


Data = [("Ana", 62.5), ("Ben", 58.2), ("Chi", 71.0), ("Dev", 55.9),
        ("Eli", 60.4), ("Fay", 59.8), ("Gus", 54.1)]
for Name, Seconds in Data:
    if AddSwimmer(Name, Seconds):
        print("Added", Name)
    else:
        print("Full:", Name)
print("Fastest:", Fastest())
```

Output, which is what the screenshot shows:

```output
Added Ana
Added Ben
Added Chi
Added Dev
Added Eli
Added Fay
Full: Gus
Fastest: Dev
```

The seventh swimmer, Gus, has the lowest time of all (54.1), but he is refused because the array is full, so the fastest swimmer in the array is Dev (55.9). That is why the test data was chosen: it tests the full case and shows that `Fastest` only looks at stored swimmers.

- (a) class `Swimmer` with a constructor `__init__` [B1] that stores both the name and the time in attributes [B1]
- (b) `Swimmers = [None] * 6`, a list of 6 elements that are all empty [B1]
- (c) a loop through the array that looks for an element that is `None` [B1]; a new `Swimmer` with the two values stored in that element [B1]; `True` returned after storing, and `False` returned after the loop if there was no empty element [B1]
- (d) a loop that ignores empty elements and finds the lowest time [B1]; the name returned, and an empty string if no swimmer is stored [B1]
- (e) the program calls `AddSwimmer` for all seven swimmers and outputs `Added` or `Full:` with the name, then the fastest [B1]; the screenshot shows the output above, with `Full: Gus` and `Fastest: Dev` [B1]

(Accept any loop that reaches every element. Accept `if not Swimmers[Index]` for the empty test. Do not accept a program that stores a seventh swimmer, or one that uses a different array name. Code pasted as an image earns no marks.)
:::

:::eg Paper 4 style: a validation part with a testing table
The club must check a time that is typed in. A time is valid if it is a number from 30.0 to 300.0 seconds, including both ends.

(a) Write a function `ValidTime(Text)` that takes a string and returns `True` if it is a valid time and `False` if not. It must not stop the program when the text is not a number. [3]

(b) Write a program that tests the function with seven values chosen to show the normal, boundary and erroneous cases, and outputs each value with its result. [3]

```python
def ValidTime(Text):
    try:
        Seconds = float(Text)
    except ValueError:
        return False
    return 30.0 <= Seconds <= 300.0


Tests = [("62.5", "normal"), ("30", "boundary"), ("300", "boundary"),
         ("29.9", "just outside"), ("300.1", "just outside"),
         ("fast", "erroneous"), ("", "erroneous")]
for Text, Kind in Tests:
    print("Test:", repr(Text), "(" + Kind + ") ->", ValidTime(Text))
```

```output
Test: '62.5' (normal) -> True
Test: '30' (boundary) -> True
Test: '300' (boundary) -> True
Test: '29.9' (just outside) -> False
Test: '300.1' (just outside) -> False
Test: 'fast' (erroneous) -> False
Test: '' (erroneous) -> False
```

- (a) the text converted with `float` [B1]; a `try` / `except ValueError` that returns `False` for text that is not a number [B1]; the range test `30.0 <= Seconds <= 300.0`, which includes both ends, with the result returned [B1]
- (b) test data that includes a normal value, both boundaries (30 and 300) and values just outside them [B1]; erroneous data that is not a number, including an empty string [B1]; every test output with its value and result so that the screenshot is readable [B1]

(The values 30 and 300 test that both ends are included, and 29.9 and 300.1 test that the limits are not too wide. A mark scheme may also accept a negative number or a very large number as erroneous data.)
:::

:::eg Spot the error: a marked answer with working code
Question: A game stores up to four scores in a global 1D array `Stack`, with a global variable `TopPointer` that is \(-1\) when the stack is empty. Write a function `Push(Item)` that adds the item and returns `True`, or outputs the message `Stack full` and returns `False` if the stack is full. Test it by pushing 5, 8, 2, 9 and 4 and outputting the array. [6]

A student wrote this program, which runs without an error:

```python
Stack = [0] * 4
top_pointer = -1


def push(item):
    global top_pointer
    if top_pointer == 3:
        print("stack is full")
        return False
    top_pointer = top_pointer + 1
    Stack[top_pointer] = item
    return True


for number in [5, 8, 2, 9, 4]:
    push(number)
print(Stack)
```

```output
stack is full
[5, 8, 2, 9]
```

The array of four elements is declared correctly and is global [B1]. The full test is correct (`top_pointer == 3`), the pointer is moved on before the item is stored, and `True` and `False` are returned correctly [B1] [B1]. The test loop pushes all five values and outputs the array [B1].

**The names are wrong: the question says `TopPointer` and `Push`, and the student used `top_pointer` and `push`. The mark for the pointer variable is lost** [B0], and a test program written by the examiner that calls `Push(...)` would fail. **The message is `stack is full`, but the question asked for `Stack full`, so the mark for the message is lost** [B0]. The answer scores 4 out of 6. Nothing is wrong with the logic: the lost marks were all in the reading, which is why the habit of underlining each name and message matters.
:::

### Partial credit: what a half-working answer earns

A student runs short of time on a recursive part. The question asked for a method `InOrder` of the class `Node` that outputs the values of a binary tree in ascending order, which needs the base case, a call on the left child, the output of the node's own value and a call on the right child. The student pastes the following code, which does not work because it never stops going left:

```text
def InOrder(self):
    self.Left.InOrder()
    print(self.Value)
    self.Right.InOrder()
```

A mark scheme that lists one mark per feature can give credit for the features that are there: the method has the right name and is a method of the class, the left call comes before the output and the right call after it, and the node's own value is output. It cannot give the mark for the base case (checking that the child exists before the call) or for a program that produces the correct output. The lesson is to paste the code, because only pasted code can earn marks for the features it contains, even when the program as a whole does not run.

## Common ways to lose marks

| The slip | Why it costs marks | The fix |
|---|---|---|
| Work not pasted into the evidence document | the front page says no marks for a task not saved there | paste after every part, and save the document |
| A screenshot that cuts off the output, or does not show the test | the testing mark needs the whole output | run the final version, check that the console shows every line, then take the screenshot |
| A different name for a function, class, array or file | the mark scheme tests the name, and a later part may call it | copy names from the question |
| A different message from the one asked for | the mark is for the exact output | copy the text, including capitals and punctuation |
| `print` where the question says "returns" (or the reverse) | the value is not returned to the calling code | read the verb |
| Index off by one in a 0-based list | the wrong element is read, or an `IndexError` | decide how you will map the question's index range, and use it everywhere |
| A number compared as a string | strings compare character by character: `"10" < "9"` | convert with `int` or `float` straight after reading |
| A file opened in the wrong mode, or in the wrong folder | `FileNotFoundError`, or the old data is overwritten | `"r"` to read, `"w"` to write (it empties the file), `"a"` to add; keep the data next to the program |
| Output file lines with no `\n` | all the data is written on one line | add `"\n"` to each line written with `write` |
| A recursive method with no base case | `RecursionError` | write the case that does not recurse first |
| A language that is not allowed, or a notebook instead of the console | zero marks for the paper | use Python in console mode |
| Saving over a working version with a broken one | a part that worked now scores nothing | save a copy before a big change |

## Technique check

Try these quick items before the longer practice in [Mixed practice: A Level (Papers 3 and 4)](#cs.mixed.a2).

:::try Technique check
Q: A Paper 4 question is worth 30 marks. At 1.8 minutes per mark, how long should it take?
A: \(30 \times 1.8 = 54\) minutes.

Q: The task says "outputs the message `Tail pointer reset`". A student writes `print("tail pointer reset")`. What is wrong?
A: The capital letter is different. The output must match the message in the task exactly, so the mark for the message is likely to be lost.

Q: A task gives a global array `Queue` with indexes 0 to 19, and the student writes `Queue = [-1] * 19`. What happens, and what is the correct line?
A: The list has 19 elements (indexes 0 to 18), so `Queue[19]` raises an `IndexError` and one element is missing. The correct line is `Queue = [-1] * 20`.

Q: A program reads a file with `open("data.txt")` and the traceback ends `FileNotFoundError`. Give two things to check.
A: That the file is in the same folder as the program, and that the name is spelt exactly as in the question, including capital letters and the extension (the file is `Data.txt` on some computers and `data.txt` on others).

Q: A student writes `Total = Total + line` for each line read from a file of numbers and gets a `TypeError`. What is wrong and how is it fixed?
A: The line is a string, not a number. Convert it: `Total = Total + int(line.strip())` (or `float` if the numbers have decimal points).

Q: After finishing Question 1(c), what three things should you do before reading 1(d)?
A: Save the program with the exact file name, paste the code into part 1(c) of the evidence document, and, if the part asks for a screenshot of the output, take it and paste it. Then save the evidence document.
:::

## Practice plan

Do the practice in this order. Each stage takes the pressure up a little.

:::steps
1. **Toolkit:** go through [Python for Paper 4: the practical toolkit](#cs.python), and type every example yourself at the keyboard.
2. **Single parts:** do the Paper 4 style tasks in [Mixed practice: A Level (Papers 3 and 4)](#cs.mixed.a2), one at a time. Write the program, run it and compare your output with the output shown before you read the answer.
3. **Full question:** do a whole 20 to 30 mark question from a past paper or from [Mock Paper 4](#cs.mock.p4) with a timer, including the evidence routine.
4. **Full paper:** do a whole past paper in 2 hours 30 minutes, in an exam-like room and with no internet. Mark it from the mark scheme, one feature at a time.
:::

The tracker below counts the checklist items you have ticked in every Paper 4 chapter.

:::progress P4
:::

## Past papers and self-marking

Real Paper 4 question papers and mark schemes are free to download. A Paper 4 question paper refers to source files such as text files of data. If a site gives you the question paper and the mark scheme but not the source files, create the file yourself from the contents that the question prints, in the same folder as your program, and name it exactly as the question does.

- [PapaCambridge](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) keeps 9618 papers and mark schemes together (an unofficial site).
- [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-4/) lists Paper 4 question papers and mark schemes by series (an unofficial site).
- The [Cambridge 9618 page](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/) has the syllabus and specimen papers.

:::steps
1. **Do the paper first, then open the mark scheme.** Run your programs again as you mark, so that you see whether each feature works.
2. **Mark one feature at a time,** in a different colour. A feature earns its mark only if it is in the code you would have pasted.
3. **Sort every lost mark** into one of three kinds: *knowledge* (you did not know how to write it), *technique* (you knew, but the name, the message or the output was not as asked) or *slip* (an off-by-one, a missing `\n`, a file in the wrong folder).
4. **Fix each kind differently:** revise the chapter, redo the part with the mark scheme in mind, or add a checking step to your routine.
5. **Redo the whole question a week later** with a timer. If you lose the same mark twice, write that point on a revision card.
:::

:::warn Do not learn old answers as scripts
Cambridge writes new tasks every series. A mark scheme is useful because it shows how features are marked, not because the same task returns. Practise the method, and the toolkit that every task uses.
:::

:::recap
- Paper 4: 2 hours 30 minutes, 75 marks, on a computer, sections 19 and 20 except low-level and declarative programming, in Java, Python or Visual Basic in console mode (zero for another language), with no internet or email. The May/June 2025 paper had 3 questions of 20, 25 and 30 marks.
- Pace: 2 minutes per mark in all, so plan about 1.8 minutes per mark and keep 15 minutes for checks.
- Save work with the file names given and paste code and screenshots into the evidence document after every part: no marks for a task that is not saved there.
- Use the exact names, messages and file names of the task; "returns" is `return` and "outputs" is `print`.
- Build part by part and run each part before the next. Test with normal, boundary and erroneous data.
- Marks are for features, so a partly working program still earns marks; pasted code is the only code that can.
- Practise at a keyboard, in plain Python, under a timer, including the evidence routine.
:::

:::links
- papers: [9618 past papers and mark schemes](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · every series in one place [unofficial]
- papers: [Paper 4 past papers by series](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-4/) · Physics & Maths Tutor · Paper 4 only [unofficial]
- practise: [Object-oriented programming: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/20-further-programming-/object-oriented-programming/exam-questions/) · Save My Exams · class and object questions with mark schemes [paid]
- practise: [File processing and exception handling: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/20-further-programming-/file-processing-and-exception-handling/exam-questions/) · Save My Exams · file and exception questions [paid]
- practise: [Exercism: Python track](https://exercism.org/tracks/python) · Exercism · free Python exercises with feedback
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run Python line by line and watch every variable
- read: [The Python tutorial](https://docs.python.org/3/tutorial/) · Python.org · the official guide to the language

Links checked 13 November 2026.
:::

Next: [Mixed practice: A Level (Papers 3 and 4)](#cs.mixed.a2)
