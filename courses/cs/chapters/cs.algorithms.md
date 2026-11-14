@chapter cs.algorithms
@title Computational thinking and algorithms
@level as
@paper CAIE 9618 Paper 2
@time 5–7 hours
@summary Before you write a program you must decide what to include, what to leave out and what the steps are. You will learn abstraction and decomposition, how to write an algorithm as structured English, a flowchart or pseudocode and convert between the three, how to refine an algorithm in stages, and how to state conditions as logic statements.

:::why
Paper 2 does not start with code. Its questions start with a scenario, and the first marks are for thinking: which details matter, how the problem splits into parts, what the steps are and how to show them clearly. Examiners also give whole questions to identifier tables, flowcharts and trace tables. If you can plan an algorithm and move it between three forms, the programming that follows in [Programming basics](#cs.programming) becomes translation rather than invention.
:::

**Before you start**, you should know what an algorithm is and how variables, IF statements and loops work, from [Programming from zero](#cs.f.basics).

:::try Warm-up
Q: What is an algorithm? (from [Programming from zero](#cs.f.basics))
A: A sequence of defined steps that solves a problem or completes a task.
Q: What does the statement `Count ← Count + 1` do? (from [Programming from zero](#cs.f.basics))
A: It works out the old value of Count plus 1 and stores the result back in Count, so Count goes up by one.
Q: A discount applies when `Age >= 60 AND Member = TRUE`. Does a 65-year-old who is not a member get it? (from [Programming from zero](#cs.f.basics))
A: No. AND needs both parts to be true, and `Member = TRUE` is false.
:::

:::note How code appears in this course
Pseudocode follows the Cambridge Pseudocode Guide for 2027–2029: keywords in capitals, `←` for assignment, three-space indents. Python blocks are Python 3 and have all been run; the block after a Python program, introduced by "Output:", is exactly what it prints. Structured English is shown in plain `text` blocks.
:::

## Computational thinking and abstraction

Computational thinking means preparing a problem so that a computer can help to solve it. Two skills do most of the work: **abstraction**, which decides what to ignore, and **decomposition**, which splits a big problem into small ones. This section deals with abstraction.

A real situation always contains more detail than a program can use, or needs. A bus has a colour, a driver, a route number, 52 seats, a fuel gauge, a registration plate and a smell of old sandwiches. A timetable program needs the route number and the times. Everything else only gets in the way.

:::def Abstraction
The process of removing unnecessary detail from a problem so that only the essential features remain, in order to produce a simpler model that can be programmed.
:::

You meet abstraction every day. A railway map shows stations and the lines between them, but not the true distances or the curves in the track. That map is an **abstract model** of the railway: it is wrong about distances on purpose, because distances are not what a traveller needs to plan a journey.

:::key The need, purpose and benefits of abstraction
- **Need**: the real world has too much detail to represent completely, and most of it is irrelevant to the task.
- **Purpose**: to produce a model that includes only the essential details, and so hides the complexity that does not matter.
- **Benefits**: the problem is easier to understand and to program; less data is stored and processed, so the program runs faster and uses less memory; the same model can often be reused for similar problems.
:::

Notice that abstraction depends on the purpose. A lending library needs a book's number and its due date. A bookshop that sorts books by size needs the height and width. The same book gives different essential details for different programs.

:::eg Which details to keep
A school library wants a program that records which pupil has borrowed which book and when the book is due back. For each detail below, say whether the abstract model should keep it or remove it, with a reason.

1. the pupil's ID number
2. the book's copy number
3. the due date
4. the colour of the book's cover
5. the pupil's favourite sport
6. the number of pages in the book

Ask of each detail: does the program need it to do its job (record the loan and detect late returns)?

- Pupil's ID number: keep, because it identifies who has the book. [B1]
- Copy number: keep, because it identifies which copy has been lent. [B1]
- Due date: keep, because the program needs it to find late returns. [B1]
- Cover colour: remove, because it plays no part in lending. [B1]
- Favourite sport: remove, because it is unrelated to the loan. [B1]
- Number of pages: remove, because the loan does not depend on it. [B1]

The reason is the mark. "Keep, because it is important" says nothing; "keep, because it identifies who has the book" ties the detail to the job.
:::

:::warn Abstraction is not decomposition
Abstraction removes detail: the problem gets simpler because there is less in it. Decomposition splits the problem into parts: the problem gets simpler because each part is smaller. Exam questions use the two words precisely, so do not swap them.
:::

## Decomposition and modules

Large programs are written by breaking the problem into smaller sub-problems, then breaking those into even smaller ones, until each piece is small enough to solve directly.

:::def Decomposition
Breaking a complex problem down into smaller sub-problems, which can be solved separately and then combined, until each is simple enough to be solved directly.
:::

Each small piece becomes a **module**: a named, self-contained part of a program that does one job.

:::def Module
A self-contained part of a program that performs one task. In pseudocode a module is a procedure (which carries out a task) or a function (which carries out a task and returns a value).
:::

Take a canteen in a school in Accra. Pupils order from a menu, the system works out the bill, takes payment and prints a report at the end of the day. The whole system is too big to design in one go, so split it.

:::html
<figure class="fig"><svg viewBox="0 0 620 330" role="img" aria-label="A tree diagram. At the top, Canteen ordering system. Below it four sub-problems: Take the order, Work out the bill, Take payment, and Report the day. Under Take the order: Show the menu, Read choices, Check stock. Under Work out the bill: Add prices, Apply discount. Under Take payment: Read amount, Give change. Under Report the day: Count orders, Add up takings."><rect class="f1 s-acc sw2" x="210" y="11" width="200" height="38" rx="3"/><text class="tl tc" x="310" y="34">Canteen ordering system</text><rect class="fm s-acc sw2" x="10" y="105" width="124" height="38" rx="3"/><text class="tl tc" x="72" y="128">Take the order</text><path class="ln" fill="none" d="M310 49 L310 72 L72 72 L72 105"/><rect class="fm2 s-acc sw2" x="30" y="171" width="124" height="38" rx="3"/><text class="tl tc" x="92" y="194">Show the menu</text><rect class="fm2 s-acc sw2" x="30" y="221" width="124" height="38" rx="3"/><text class="tl tc" x="92" y="244">Read choices</text><rect class="fm2 s-acc sw2" x="30" y="271" width="124" height="38" rx="3"/><text class="tl tc" x="92" y="294">Check stock</text><path class="ln" fill="none" d="M16 143 L16 290"/><path class="ln" fill="none" d="M16 190 L30 190"/><path class="ln" fill="none" d="M16 240 L30 240"/><path class="ln" fill="none" d="M16 290 L30 290"/><rect class="fm s-acc sw2" x="160" y="97" width="124" height="54" rx="3"/><text class="tl tc" x="222" y="120">Work out</text><text class="tl tc" x="222" y="136">the bill</text><path class="ln" fill="none" d="M310 49 L310 72 L222 72 L222 97"/><rect class="fm2 s-acc sw2" x="180" y="171" width="124" height="38" rx="3"/><text class="tl tc" x="242" y="194">Add prices</text><rect class="fm2 s-acc sw2" x="180" y="221" width="124" height="38" rx="3"/><text class="tl tc" x="242" y="244">Apply discount</text><path class="ln" fill="none" d="M166 151 L166 240"/><path class="ln" fill="none" d="M166 190 L180 190"/><path class="ln" fill="none" d="M166 240 L180 240"/><rect class="fm s-acc sw2" x="310" y="105" width="124" height="38" rx="3"/><text class="tl tc" x="372" y="128">Take payment</text><path class="ln" fill="none" d="M310 49 L310 72 L372 72 L372 105"/><rect class="fm2 s-acc sw2" x="330" y="171" width="124" height="38" rx="3"/><text class="tl tc" x="392" y="194">Read amount</text><rect class="fm2 s-acc sw2" x="330" y="221" width="124" height="38" rx="3"/><text class="tl tc" x="392" y="244">Give change</text><path class="ln" fill="none" d="M316 143 L316 240"/><path class="ln" fill="none" d="M316 190 L330 190"/><path class="ln" fill="none" d="M316 240 L330 240"/><rect class="fm s-acc sw2" x="460" y="97" width="124" height="54" rx="3"/><text class="tl tc" x="522" y="120">Report</text><text class="tl tc" x="522" y="136">the day</text><path class="ln" fill="none" d="M310 49 L310 72 L522 72 L522 97"/><rect class="fm2 s-acc sw2" x="480" y="171" width="124" height="38" rx="3"/><text class="tl tc" x="542" y="194">Count orders</text><rect class="fm2 s-acc sw2" x="480" y="221" width="124" height="38" rx="3"/><text class="tl tc" x="542" y="244">Add up takings</text><path class="ln" fill="none" d="M466 151 L466 240"/><path class="ln" fill="none" d="M466 190 L480 190"/><path class="ln" fill="none" d="M466 240 L480 240"/></svg><figcaption>The canteen ordering system split into four sub-problems, each split again into the parts listed under it. Each of the smallest boxes is small enough to become one module (a procedure or a function).</figcaption></figure>
:::

Each of the smallest boxes, the parts listed under a sub-problem, is small enough to program as one module. A module that works out and hands back a value, such as "Add prices", is a **function**. A module that carries out a job without handing back a value, such as "Show the menu", is a **procedure**. The main program then becomes a short list of calls, one per module:

```pseudocode
CALL ShowMenu()
CALL ReadChoices()
Bill ← CalculateBill()
CALL TakePayment(Bill)
CALL ReportDay()
```

The first, second, fourth and fifth lines call procedures with `CALL`. The third line calls a function inside an assignment, because it returns a value that is stored in `Bill`. How to write procedures and functions is the subject of [Procedures, functions and parameters](#cs.procedures); for now you only need to see that decomposition leads straight to them.

:::key Why decompose?
- Each module is small enough to understand, write and test on its own.
- Different programmers can write different modules at the same time.
- A module can be reused: "Read amount" might serve the canteen and the school shop.
- A fault is easier to find, because you know which module to look in.
- A module can be replaced or improved without rewriting the rest.
:::

Structure charts, a diagram that records which modules call which, come in [Software development](#cs.development).

## Algorithms

:::def Algorithm
A sequence of defined steps that solves a problem or completes a task.
:::

Two words in the definition carry weight. **Sequence** means the order matters: "crack the egg, then fry it" is not the same as "fry the egg, then crack it". **Defined** means each step is exact enough that whoever follows it, person or computer, has no choice to make. "Add a bit of salt" is not defined; "add 5 g of salt" is.

An algorithm takes **input**, carries out a **process** and gives **output**. In pseudocode these are visible: `INPUT` statements bring the data in, assignments and decisions process it, and `OUTPUT` statements give the result.

Every algorithm is built from just three constructs.

:::key The three constructs
- **Sequence**: steps run one after another, in the order written.
- **Selection**: a condition decides which steps run (`IF`, `CASE`).
- **Iteration**: steps are repeated (`FOR`, `WHILE`, `REPEAT`), a fixed number of times or until a condition changes.
:::

Making a cup of tea contains all three. Boil the water, put the tea bag in the cup and pour the water in: that is a **sequence**. If the drinker takes sugar, add a spoonful: that is **selection**. Stir until the sugar has dissolved: that is **iteration**. Programs differ from recipes in size, not in kind.

## Identifiers and identifier tables

Every variable, constant, array, procedure or function needs a name. That name is an **identifier**.

:::def Identifier
The name given to a variable, constant, array, procedure, function or other item in a program.
:::

The Pseudocode Guide sets the rules for pseudocode identifiers.

:::key Rules for identifiers
- Use only letters, digits and the underscore, and start with a letter. No spaces, hyphens or other symbols: `DaysLate` and `Days_Late` are legal, `Days Late` and `2ndTry` are not.
- Identifiers are not case sensitive, so `Total` and `TOTAL` are the same item. Never use two names that differ only in capitals.
- Choose names that say what the item holds, in mixed case: `NumberOfPlayers`, not `x` or `n1`.
- A name must not be a keyword such as `IF`, `FOR` or `OUTPUT`.
:::

When you plan a program on paper you list its identifiers in a table. Paper 2 often asks you to complete one, or to build one for a given scenario.

:::def Identifier table
A table that lists every identifier used in a program or algorithm with its data type and a description of what it is used for.
:::

The columns are always the same: **Identifier**, **Data type**, **Description**. A constant's description gives its value. The data types are the six you know (INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE), plus ARRAY and others that come in later chapters. [Data types, records and arrays](#cs.datatypes) says how to choose between them; for now the rule that catches most students is that a number you never calculate with (a code, a phone number) is a STRING.

:::eg Completing an identifier table
A library program works out the fine for a late book. Here is the pseudocode:

```pseudocode
CONSTANT DailyFine = 0.25
INPUT BookCode
INPUT DaysLate
Fine ← DaysLate * DailyFine
IF Fine > 5.00 THEN
   Fine ← 5.00
ENDIF
OUTPUT BookCode, " fine: ", Fine
```

Complete the identifier table. [4 marks]

Go through the code and find each identifier. For each one decide what it holds, then choose the type.

| Identifier | Data type | Description |
|---|---|---|
| DailyFine | REAL | constant, the fine for each day late, 0.25 |
| BookCode | STRING | the code that identifies the book |
| DaysLate | INTEGER | the number of whole days the book is late |
| Fine | REAL | the fine to be paid, never more than 5.00 |

- DailyFine: REAL, because 0.25 has a fractional part, and a description that says it is a constant. [B1]
- BookCode: STRING, because a code is not used in calculations. [B1]
- DaysLate: INTEGER, because whole days are counted. [B1]
- Fine: REAL, because it is a money amount that has a fractional part. [B1]

With DaysLate typed as 12, the fine is \(12 \times 0.25 = 3.0\), below the 5.00 limit. With DaysLate 30 the product is 7.5, so the IF statement reduces it to 5.00.
:::

:::warn Names examiners reject
`x`, `temp2` or `Variable1` say nothing about the data. A name copied from the question (`Fine`, `DaysLate`) is always safe. A name with a space (`Days Late`) is not an identifier at all, so you lose the mark even though the meaning is clear.
:::

## Three ways to write an algorithm

An algorithm exists independently of any language. You can document it in three forms, and the syllabus expects you to move between them in both directions.

:::def Structured English
A way of writing an algorithm as numbered, plain-English steps in a fixed style, with indentation for the steps inside a selection or a loop. It has no single official form.
:::

:::def Flowchart
A diagram that shows the steps of an algorithm in symbols joined by arrows, with a decision symbol where the flow can go two ways.
:::

:::def Pseudocode
A language-independent way of writing an algorithm in a structured form that looks like program code but follows no real language's strict rules. In this course it follows the Cambridge Pseudocode Guide.
:::

**Structured English** is the friendliest: numbered steps, one action per step, and words such as "If", "Otherwise", "While" and "Repeat" with the steps they control indented underneath. **Flowcharts** show the shape of the logic at a glance, which makes loops and branches easy to see. **Pseudocode** is closest to a program, so it is the form you must write for most Paper 2 answers.

### The flowchart symbols

:::html
<figure class="fig"><svg viewBox="0 0 520 372" role="img" aria-label="The six flowchart symbols, each with its meaning. A rounded terminator labelled Start: the one start and the one end of the flowchart. A rectangle labelled Total gets 0: a process, a calculation or an assignment. A parallelogram labelled INPUT Age: input or output. A diamond labelled Age at least 18: a decision, a question with exactly two exits, Yes and No. A rectangle with double side lines labelled SortList: a predefined process, a module defined somewhere else. A plain arrow: the order in which the steps run."><rect class="fm s-acc sw2" x="48" y="20" width="84" height="32" rx="16"/><text class="tl tc" x="90" y="40">Start</text><text class="tl" x="175" y="40">Terminator: the one start and one end</text><rect class="f1 s-acc sw2" x="35" y="73" width="110" height="38" rx="3"/><text class="tl tc" x="90" y="96">Total ← 0</text><text class="tl" x="175" y="96">Process: a calculation or assignment</text><polygon class="fm2 s-acc sw2" points="44,131 150,131 136,165 30,165"/><text class="tl tc" x="90" y="152">INPUT Age</text><text class="tl" x="175" y="152">Input or output: INPUT and OUTPUT</text><polygon class="fp s-acc sw2" points="90,188 144,216 90,244 36,216"/><text class="tl tc" x="90" y="220">Age &gt;= 18?</text><text class="tl" x="175" y="220">Decision: a yes/no question, two exits</text><rect class="f1 s-acc sw2" x="37" y="289" width="106" height="34" rx="3"/><line class="ln" x1="49" y1="289" x2="49" y2="323"/><line class="ln" x1="131" y1="289" x2="131" y2="323"/><text class="tl tc" x="90" y="310">SortList</text><text class="tl" x="175" y="310">Predefined process: a module defined elsewhere</text><path class="ln" fill="none" d="M30 360 L170 360" marker-end="url(#ah)"/><text class="tl" x="175" y="364">Arrow: the order the steps run in</text></svg><figcaption>The flowchart symbols used in Cambridge questions, with what each means. A flowchart has one start terminator and one end terminator.</figcaption></figure>
:::

:::key Flowchart rules
- One **Start** and one **End** terminator.
- A **decision** diamond has exactly one way in and exactly **two** ways out, labelled **Yes** and **No** (or True and False). Write the question inside as a condition: `Age >= 18?`.
- Every box has an arrow in and an arrow out (except Start, which has none in, and End, which has none out).
- Write inside a box the same statements you would write in pseudocode: `Total ← Total + Pages`, `INPUT Age`.
- A loop is an arrow that goes back to an earlier point. Where the decision sits tells you the kind of loop.
:::

### Worked example 1: a loop

A reading club in Kampala logs the pages each member read each day. The user types the pages for one day at a time and types 0 when there is no more data. The program then outputs the number of days and the total number of pages.

Start with the algorithm in structured English.

```text
1. Set Total to 0
2. Set Days to 0
3. Input Pages
4. While Pages is not 0
5.    Add Pages to Total
6.    Add 1 to Days
7.    Input Pages
8. Output Days
9. Output Total
```

The first `Input Pages` (line 3) happens before the loop so that the test in line 4 has a value to look at. The last step of the loop (line 7) reads the next value. The value 0 ends the loop and is never added: it is a **sentinel**, a special value that signals the end of the data.

Converting to pseudocode is nearly word for word: "Set" becomes `←`, "While … " becomes `WHILE … ENDWHILE`, and "Add Pages to Total" becomes `Total ← Total + Pages`.

```pseudocode
Total ← 0
Days ← 0
INPUT Pages
WHILE Pages <> 0
   Total ← Total + Pages
   Days ← Days + 1
   INPUT Pages
ENDWHILE
OUTPUT "Days: ", Days
OUTPUT "Total pages: ", Total
```

Here is the flowchart for the same algorithm. Compare it with the other two forms line by line.

:::html
<figure class="fig"><svg viewBox="0 0 520 552" role="img" aria-label="A flowchart. Start, then Total gets 0, then Days gets 0, then INPUT Pages, then a decision Pages not equal to 0. The Yes exit leads right to Total gets Total plus Pages, then Days gets Days plus 1, then INPUT Pages, then an arrow goes back up to the decision. The No exit leads down to OUTPUT Days, OUTPUT Total and End."><rect class="fm s-acc sw2" x="78" y="12" width="84" height="32" rx="16"/><text class="tl tc" x="120" y="32">Start</text><rect class="f1 s-acc sw2" x="65" y="69" width="110" height="38" rx="3"/><text class="tl tc" x="120" y="92">Total ← 0</text><rect class="f1 s-acc sw2" x="65" y="129" width="110" height="38" rx="3"/><text class="tl tc" x="120" y="152">Days ← 0</text><polygon class="fm2 s-acc sw2" points="68.5,191 185.5,191 171.5,225 54.5,225"/><text class="tl tc" x="120" y="212">INPUT Pages</text><polygon class="fp s-acc sw2" points="120,272 178,300 120,328 62,300"/><text class="tl tc" x="120" y="304">Pages &lt;&gt; 0?</text><polygon class="fm2 s-acc sw2" points="68.5,383 185.5,383 171.5,417 54.5,417"/><text class="tl tc" x="120" y="404">OUTPUT Days</text><polygon class="fm2 s-acc sw2" points="65,441 189,441 175,475 51,475"/><text class="tl tc" x="120" y="462">OUTPUT Total</text><rect class="fm s-acc sw2" x="78" y="500" width="84" height="32" rx="16"/><text class="tl tc" x="120" y="520">End</text><rect class="f1 s-acc sw2" x="283.5" y="281" width="173" height="38" rx="3"/><text class="tl tc" x="370" y="304">Total ← Total + Pages</text><rect class="f1 s-acc sw2" x="304.5" y="343" width="131" height="38" rx="3"/><text class="tl tc" x="370" y="366">Days ← Days + 1</text><polygon class="fm2 s-acc sw2" points="318.5,407 435.5,407 421.5,441 304.5,441"/><text class="tl tc" x="370" y="428">INPUT Pages</text><path class="ln" fill="none" d="M120 44 L120 69" marker-end="url(#ah)"/><path class="ln" fill="none" d="M120 107 L120 129" marker-end="url(#ah)"/><path class="ln" fill="none" d="M120 167 L120 191" marker-end="url(#ah)"/><path class="ln" fill="none" d="M120 225 L120 272" marker-end="url(#ah)"/><path class="ln" fill="none" d="M120 328 L120 383" marker-end="url(#ah)"/><path class="ln" fill="none" d="M120 417 L120 441" marker-end="url(#ah)"/><path class="ln" fill="none" d="M120 475 L120 500" marker-end="url(#ah)"/><path class="ln" fill="none" d="M178 300 L283.5 300" marker-end="url(#ah)"/><path class="ln" fill="none" d="M370 319 L370 343" marker-end="url(#ah)"/><path class="ln" fill="none" d="M370 381 L370 407" marker-end="url(#ah)"/><path class="ln" fill="none" d="M435.5 424 L500 424 L500 250 L120 250" marker-end="url(#ah)"/><text class="tl" x="186" y="292">Yes</text><text class="tl" x="128" y="352">No</text></svg><figcaption>The reading-club program as a flowchart. The decision sits before the loop body, and the arrow from the last INPUT returns to it: this is a WHILE loop.</figcaption></figure>
:::

The decision `Pages <> 0?` is tested **before** the loop body, and the arrow from the last `INPUT Pages` goes back to it. That shape is a `WHILE` loop. Because the test comes first, the loop body can run zero times: if the first value typed is 0, the program goes straight to the outputs and prints 0 days and 0 pages.

Here is the same program in Python, run with the values 12, 30, 25 and 0.

```python
total = 0
days = 0
pages = int(input("Pages read (0 to finish): "))
while pages != 0:
    total = total + pages
    days = days + 1
    pages = int(input("Pages read (0 to finish): "))
print("Days:", days)
print("Total pages:", total)
```

Output, when the user types 12, 30, 25 and 0:

```output
Pages read (0 to finish): 12
Pages read (0 to finish): 30
Pages read (0 to finish): 25
Pages read (0 to finish): 0
Days: 3
Total pages: 67
```

:::key From flowchart to pseudocode
1. Follow the arrows from Start. Straight runs of boxes are a **sequence**: write the statements in order.
2. A diamond whose two exits lead to different boxes that rejoin later is a **selection**: write `IF … THEN … ELSE … ENDIF`, with the Yes branch under `THEN`.
3. A diamond with an arrow that leads back to an earlier point is a **loop**. If the diamond comes **before** the boxes it controls, write `WHILE`. If it comes **after** them, write `REPEAT … UNTIL`, and remember that `UNTIL` stops when its condition is **true**, so the condition is the one on the exit that leaves the loop.
4. A box that holds `INPUT` or `OUTPUT` becomes that statement, and a process box becomes an assignment.
5. Put a closing keyword (`ENDIF`, `ENDWHILE`, `UNTIL`) wherever the branches or the loop come together again.
:::

### Worked example 2: nested selection

A museum in Cape Town charges by age. Children under 5 enter free. Anyone aged 5 to 17 pays 4.00. Adults pay 10.00, but an adult who is a student pays 6.00. The program inputs the age and whether the visitor is a student (typed as the letter Y or N), then outputs the price.

The structure is a chain of questions where each "No" leads to the next question: first "under 5?", then "under 18?", and only for adults "a student?". The question about students is **nested** inside the answers to the two before it.

```text
1. Input Age
2. Input Student
3. If Age is less than 5 then
4.    Set Price to 0.00
5. Otherwise, if Age is less than 18 then
6.    Set Price to 4.00
7. Otherwise (the visitor is an adult)
8.    If Student is 'Y' then
9.       Set Price to 6.00
10.   Otherwise
11.      Set Price to 10.00
12. Output Price
```

In pseudocode, the guide's `IF` has `THEN`, `ELSE` and `ENDIF`. To ask a further question, put a new `IF` inside the `ELSE`, and **every `IF` needs its own `ENDIF`**:

```pseudocode
INPUT Age
INPUT Student
IF Age < 5 THEN
   Price ← 0.00
ELSE
   IF Age < 18 THEN
      Price ← 4.00
   ELSE
      IF Student = 'Y' THEN
         Price ← 6.00
      ELSE
         Price ← 10.00
      ENDIF
   ENDIF
ENDIF
OUTPUT Price
```

And the flowchart. Every assignment leads on to the same `OUTPUT Price`, which is where the three `ENDIF`s come together.

:::html
<figure class="fig"><svg viewBox="0 0 520 680" role="img" aria-label="A flowchart. Start, INPUT Age, INPUT Student, then three decisions one below the other. Decision Age less than 5: Yes leads right to Price gets 0.00, No leads down. Decision Age less than 18: Yes leads right to Price gets 4.00, No leads down. Decision Student equals Y: Yes leads right to Price gets 6.00, No leads down to Price gets 10.00. All four assignments then lead to OUTPUT Price, then End."><rect class="fm s-acc sw2" x="88" y="12" width="84" height="32" rx="16"/><text class="tl tc" x="130" y="32">Start</text><polygon class="fm2 s-acc sw2" points="84,71 190,71 176,105 70,105"/><text class="tl tc" x="130" y="92">INPUT Age</text><polygon class="fm2 s-acc sw2" points="71.5,131 202.5,131 188.5,165 57.5,165"/><text class="tl tc" x="130" y="152">INPUT Student</text><polygon class="fp s-acc sw2" points="130,202 175,230 130,258 85,230"/><text class="tl tc" x="130" y="234">Age &lt; 5?</text><polygon class="fp s-acc sw2" points="130,302 179,330 130,358 81,330"/><text class="tl tc" x="130" y="334">Age &lt; 18?</text><polygon class="fp s-acc sw2" points="130,402 202,430 130,458 58,430"/><text class="tl tc" x="130" y="434">Student = 'Y'?</text><rect class="f1 s-acc sw2" x="71.5" y="501" width="117" height="38" rx="3"/><text class="tl tc" x="130" y="524">Price ← 10.00</text><polygon class="fm2 s-acc sw2" points="75,573 199,573 185,607 61,607"/><text class="tl tc" x="130" y="594">OUTPUT Price</text><rect class="fm s-acc sw2" x="88" y="630" width="84" height="32" rx="16"/><text class="tl tc" x="130" y="650">End</text><rect class="f1 s-acc sw2" x="330" y="211" width="110" height="38" rx="3"/><text class="tl tc" x="385" y="234">Price ← 0.00</text><rect class="f1 s-acc sw2" x="330" y="311" width="110" height="38" rx="3"/><text class="tl tc" x="385" y="334">Price ← 4.00</text><rect class="f1 s-acc sw2" x="330" y="411" width="110" height="38" rx="3"/><text class="tl tc" x="385" y="434">Price ← 6.00</text><path class="ln" fill="none" d="M130 44 L130 71" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 105 L130 131" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 165 L130 202" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 258 L130 302" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 358 L130 402" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 458 L130 501" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 539 L130 573" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 607 L130 630" marker-end="url(#ah)"/><path class="ln" fill="none" d="M175 230 L330 230" marker-end="url(#ah)"/><text class="tl" x="183" y="222">Yes</text><text class="tl" x="138" y="282">No</text><path class="ln" fill="none" d="M179 330 L330 330" marker-end="url(#ah)"/><text class="tl" x="187" y="322">Yes</text><text class="tl" x="138" y="382">No</text><path class="ln" fill="none" d="M202 430 L330 430" marker-end="url(#ah)"/><text class="tl" x="210" y="422">Yes</text><text class="tl" x="138" y="482">No</text><path class="ln" fill="none" d="M440 230 L495 230 L495 590 L199 590" marker-end="url(#ah)"/><path class="ln" fill="none" d="M440 330 L495 330"/><path class="ln" fill="none" d="M440 430 L495 430"/></svg><figcaption>The museum price as a flowchart. Each No exit leads to the next question, so the decisions are nested. Only one of the four assignments runs, and every route then reaches OUTPUT Price.</figcaption></figure>
:::

In Python, `elif` plays the part of "ELSE, then another IF", so the nesting becomes a flat chain. The program below is run with the typed values 30 and Y, an adult student.

```python
age = int(input("Age: "))
student = input("Student (Y or N): ")
if age < 5:
    price = 0.00
elif age < 18:
    price = 4.00
elif student == "Y":
    price = 6.00
else:
    price = 10.00
print(f"Price: {price:.2f}")
```

Output, when the user types 30 and Y:

```output
Age: 30
Student (Y or N): Y
Price: 6.00
```

Check the boundaries with test values, as you would in an exam trace. An age of 4 gives 0.00 and an age of 5 gives 4.00; 17 gives 4.00 and 18 gives 10.00 for a non-student. The two comparisons use `<`, not `<=`, so the boundary values 5 and 18 fall in the next group up.

:::tip Converting in the other direction
To go from pseudocode to a flowchart, take the statements in order: each `INPUT` or `OUTPUT` is a parallelogram and each assignment a rectangle. Each `IF` becomes a diamond with two arrows that rejoin after the `ENDIF`. Each `WHILE` becomes a diamond **above** its body, with an arrow from the end of the body back to it. Each `REPEAT … UNTIL` becomes a diamond **below** its body, with the arrow back to the top on the exit where the condition is false.
:::

## Stepwise refinement

Writing a whole algorithm in one go is hard. **Stepwise refinement** starts with a rough outline and rewrites each step in more detail, level by level, until every step is a statement you can write in pseudocode.

:::def Stepwise refinement
A method of designing an algorithm by starting with a general description of the solution and repeatedly breaking each step into more detailed steps, until each can be written directly in code.
:::

Take a taxi in Nairobi. The fare is a basic 3.00 which covers the first 2 km, plus 1.50 for each further whole kilometre. A night journey has 2.00 added. A program inputs the distance and whether it is night, and outputs the fare.

**Level 1** is the outline:

```text
1. Get the journey details
2. Work out the fare
3. Show the fare
```

**Level 2** refines each step:

```text
1. Get the journey details
   1.1 Input the distance in whole kilometres
   1.2 Input whether the journey is at night
2. Work out the fare
   2.1 Start with the basic fare
   2.2 Add the charge for each kilometre after the first 2
   2.3 Add the night charge if the journey is at night
3. Show the fare
```

**Level 3** turns each refined step into a pseudocode statement. Notice that steps 2.2 and 2.3 are *selections* hidden inside the words, and that the three numbers (3.00, 2, 1.50, 2.00) become named constants so that a change in price needs only one edit.

```pseudocode
CONSTANT BaseFare = 3.00
CONSTANT FreeKm = 2
CONSTANT RatePerKm = 1.50
CONSTANT NightCharge = 2.00
DECLARE Distance : INTEGER
DECLARE AtNight : CHAR
DECLARE Fare : REAL

INPUT Distance
INPUT AtNight
Fare ← BaseFare
IF Distance > FreeKm THEN
   Fare ← Fare + (Distance - FreeKm) * RatePerKm
ENDIF
IF AtNight = 'Y' THEN
   Fare ← Fare + NightCharge
ENDIF
OUTPUT "Fare: ", Fare
```

For a 7 km night journey, the distance after the first 2 km is \(7 - 2 = 5\), so the charge is \(5 \times 1.50 = 7.50\). The fare is \(3.00 + 7.50 + 2.00 = 12.50\). The same algorithm in Python:

```python
BASE_FARE = 3.00
FREE_KM = 2
RATE_PER_KM = 1.50
NIGHT_CHARGE = 2.00

distance = int(input("Distance in whole kilometres: "))
at_night = input("At night (Y or N): ")
fare = BASE_FARE
if distance > FREE_KM:
    fare = fare + (distance - FREE_KM) * RATE_PER_KM
if at_night == "Y":
    fare = fare + NIGHT_CHARGE
print(f"Fare: {fare:.2f}")
```

Output, when the user types 7 and Y:

```output
Distance in whole kilometres: 7
At night (Y or N): Y
Fare: 12.50
```

Python has no constants, so by convention a name written in capitals tells readers not to change it.

:::tip Refinement in the exam
When a Paper 2 question asks you to write an algorithm for a long scenario, write the Level 1 steps as comments or a quick list first. It takes thirty seconds, stops you forgetting a requirement, and the steps become the lines of your answer.
:::

## Logic statements in an algorithm

Selection and iteration both depend on a **condition**: a statement that is either true or false. Writing the condition correctly is where many marks are lost.

:::def Logic statement
A statement that is either true or false, built from comparisons (`=`, `<>`, `<`, `>`, `<=`, `>=`) combined with AND, OR and NOT. It is used as the condition of a selection or a loop.
:::

The skill is turning a sentence into a condition. Say each part of the sentence as a comparison, then join the parts with the right word.

| In words | As a condition |
|---|---|
| the age is at least 13 | `Age >= 13` |
| the mark is more than 49 | `Mark > 49` |
| the number is between 10 and 20 (including both) | `Number >= 10 AND Number <= 20` |
| the number is outside 10 to 20 | `Number < 10 OR Number > 20` |
| the grade is not 'A' | `Grade <> 'A'` |
| the user is at least 13 and has given consent | `Age >= 13 AND Consent = TRUE` |
| the answer is Y or y | `Answer = 'Y' OR Answer = 'y'` |

:::warn Three slips with conditions
- **Chained comparisons.** `10 <= Number <= 20` is not valid pseudocode. Write two comparisons joined by AND.
- **Incomplete comparisons.** `Answer = 'Y' OR 'y'` is wrong, because `'y'` on its own is not a condition. Repeat the variable: `Answer = 'Y' OR Answer = 'y'`.
- **AND for "outside".** "Outside 10 to 20" is *less than 10 OR more than 20*. Nothing is both, so `Number < 10 AND Number > 20` is never true.
:::

A lift in a hospital may start moving when its doors are closed, the load is at most 800 kg and the alarm is not sounding. As a logic statement: `DoorsClosed = TRUE AND Load <= 800 AND AlarmOn = FALSE`, or, using NOT, `DoorsClosed AND Load <= 800 AND NOT AlarmOn`. A BOOLEAN variable is already true or false, so it may be used on its own as a condition.

### Turning a condition round

A `REPEAT … UNTIL` loop stops when its condition is true; a `WHILE` loop carries on while its condition is true. So when you change one into the other you must **negate** the condition. Negating a condition changes each comparison to its opposite and swaps AND with OR (De Morgan's rule):

\[
\text{NOT}(A \text{ AND } B) = (\text{NOT } A) \text{ OR } (\text{NOT } B)
\qquad
\text{NOT}(A \text{ OR } B) = (\text{NOT } A) \text{ AND } (\text{NOT } B)
\]

For example, a validation loop that repeats until the age is from 5 to 18 has the exit condition `Age >= 5 AND Age <= 18`. Written as a `WHILE` loop, the condition becomes `Age < 5 OR Age > 18`: each comparison reversed and AND changed to OR. You will use this in the next chapter whenever a question asks you to rewrite one loop as the other.

## Dry running an algorithm

You can check an algorithm without a computer by working through it by hand, with a **trace table**: one column for each variable and for the output, and a row for each change. Take the reading-club program with the typed values 12, 30, 25 and 0.

| Total | Days | Pages | OUTPUT |
|---|---|---|---|
| 0 | | | |
| | 0 | | |
| | | 12 | |
| 12 | | | |
| | 1 | | |
| | | 30 | |
| 42 | | | |
| | 2 | | |
| | | 25 | |
| 67 | | | |
| | 3 | | |
| | | 0 | |
| | | | Days: 3 |
| | | | Total pages: 67 |

Each row shows one change. The 0 is read into Pages, the test `Pages <> 0` fails and the loop ends without adding it, so the last two rows are the outputs. The tool below shows the same trace one line at a time: press Next, watch the arrow move to the line that has just run and see the row appear. Choose the second set of typed values to see the loop run zero times.

:::html
<div class="widget" data-w="cs-trace" data-prog="total"></div>
:::

A trace table is how you find logic errors in Paper 2. Do not skip lines in your head: the whole point is to follow the algorithm as the computer would, not as you hope it behaves.

:::eg Spot the error: the wrong loop for the flowchart
Question: Write pseudocode for the reading-club flowchart earlier in this chapter. [6 marks]

A student wrote:

```pseudocode
01  Total ← 0
02  Days ← 0
03  REPEAT
04     INPUT Pages
05     Total ← Total + Pages
06     Days ← Days + 1
07  UNTIL Pages = 0
08  OUTPUT "Days: ", Days
09  OUTPUT "Total pages: ", Total
```

Lines 01 and 02 initialise both variables [B1] [B1]. The flowchart reads a value **before** the decision, so the first `INPUT Pages` must come before the loop; here there is none [B0]. The decision comes before the loop body, so the loop must be a pre-condition `WHILE Pages <> 0`; here `REPEAT … UNTIL` tests afterwards [B0]. Lines 05 and 06 do add Pages to Total and count a day inside the loop [B1] and lines 08 and 09 output both results [B1]. **The answer scores 4 out of 6.**

The slip is more than lost marks: the answer gives wrong results. With the typed values 12, 30, 25 and 0, the loop body runs for the 0 as well, so `Days` becomes 4, not 3. A `REPEAT` loop always runs its body once before testing, so it cannot leave a sentinel out. The corrected version is the `WHILE` loop in the worked example, with the first `INPUT Pages` before it and a second `INPUT Pages` as the last line inside it.
:::

:::try Start easy, finish at exam standard
Q: A phone game shows a character with a name, a health bar and a level, but the program ignores the character's clothes. Which skill is this, and what is the benefit?
A: Abstraction: it keeps only the essential details. The model is simpler, so it uses less memory and runs faster.
Q: State which of `Total 1`, `total_1`, `1stTotal` and `FOR` are legal pseudocode identifiers.
A: Only `total_1`. `Total 1` has a space, `1stTotal` starts with a digit and `FOR` is a keyword.
Q: Write conditions for: (a) the mark is at least 40 and at most 100; (b) the code is neither 'X' nor 'Z'.
A: (a) `Mark >= 40 AND Mark <= 100`. (b) `Code <> 'X' AND Code <> 'Z'`. Not X and not Z needs AND; `OR` would be true for every code.
Q: Which of sequence, selection and iteration does each describe? (a) "Keep adding water until the glass is full." (b) "If it is raining, take an umbrella." (c) "Wash, then dry."
A: (a) iteration; (b) selection; (c) sequence.
Q: In a flowchart, how many exits must a decision symbol have, and how are they labelled?
A: Exactly two, labelled Yes and No.
Q: A flowchart has a diamond with the question `Count < 10?`, followed by boxes, and an arrow from the last box back to the diamond. Which pseudocode loop is this?
A: `WHILE Count < 10 … ENDWHILE`, because the test comes before the body and the arrow returns to it.
Q: Write structured English for: input two numbers and output the larger.
A: There are several correct versions. One is:

```text
1. Input First
2. Input Second
3. If First is greater than Second then
4.    Output First
5. Otherwise
6.    Output Second
```

Q: Write the pseudocode for the structured English in the previous answer.
A: A direct translation:

```pseudocode
INPUT First
INPUT Second
IF First > Second THEN
   OUTPUT First
ELSE
   OUTPUT Second
ENDIF
```

Q: A condition `Age < 5 OR Age > 18` controls a WHILE loop. Write the UNTIL condition for an equivalent REPEAT loop.
A: Negate it: `Age >= 5 AND Age <= 18`. Each comparison is reversed and OR becomes AND.
Q: Give two benefits of splitting a program into modules.
A: Any two: each module is easier to write and test on its own; programmers can work on different modules at the same time; a module can be reused; faults are easier to locate.
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ A program for a school sports day contains this pseudocode.

```pseudocode
CONSTANT PassMark = 40
INPUT StudentName
INPUT TestMark
IF TestMark >= PassMark THEN
   Result ← "Pass"
ELSE
   Result ← "Fail"
ENDIF
IsDistinction ← TestMark >= 80
OUTPUT StudentName, ": ", Result
```

Complete an identifier table with a column for the identifier, a column for the data type and a column for a description, with one row for each identifier.
H: Count the names that appear: one is a constant, one is declared by an assignment to a comparison.
A: Five identifiers:

| Identifier | Data type | Description |
|---|---|---|
| PassMark | INTEGER | constant, the lowest mark that is a pass, 40 |
| StudentName | STRING | the name of the student |
| TestMark | INTEGER | the student's mark in the test |
| Result | STRING | "Pass" or "Fail" |
| IsDistinction | BOOLEAN | TRUE if the mark is at least 80 |

- PassMark: INTEGER and described as a constant [B1]
- StudentName: STRING [B1]
- TestMark: INTEGER [B1]
- Result: STRING [B1]
- IsDistinction: BOOLEAN, because it stores the result of a comparison [B1]

(Accept REAL for PassMark and TestMark only if the description says marks can have a fractional part. Accept CHAR never for names.)

Q: [2 marks] ★ A navigation app shows a map with only the roads and junctions: it leaves out the colour of the buildings and the names of the shops. Describe one benefit to the app of using abstraction like this.
A: One benefit with its reason:

- the map data is smaller, because unnecessary detail is not stored, so the app uses less memory and loads faster [B1]
- the route calculation only has to process roads and junctions, so it is quicker [B1]

(Accept: the display is easier for the user to read, because only essential information is shown.)

Q: [4 marks] ★★ A bus company in Lima wants a program to manage seat bookings. Decompose the problem into at least four sub-problems, and say which of them you would write as a function.
H: Think about what happens when a passenger books: what must be asked, checked, calculated and printed?
A: One possible decomposition:

- input the passenger's journey details (route, date, number of seats) [B1]
- check whether enough seats are free on that journey [B1]
- calculate the fare for the booking [B1]
- print the ticket, or output a message when there are no seats [B1]

(Accept other sensible sub-problems such as "cancel a booking" or "update the number of free seats". Calculate the fare, which gives back a value, is the natural function; the others can be procedures. Marks are for four distinct sub-problems, each a smaller part of the problem.)

Q: [6 marks] ★★ The flowchart below checks a score. Write pseudocode that does the same.

:::html
<figure class="fig"><svg viewBox="0 0 520 490" role="img" aria-label="A flowchart. Start, INPUT Score, then a decision Score less than 0 OR Score greater than 100. Yes leads right to OUTPUT Invalid, and an arrow goes back up to INPUT Score. No leads down to a decision Score at least 40. Yes leads right to OUTPUT Pass, which leads to End. No leads down to OUTPUT Fail, which leads to End."><rect class="fm s-acc sw2" x="88" y="12" width="84" height="32" rx="16"/><text class="tl tc" x="130" y="32">Start</text><polygon class="fm2 s-acc sw2" points="78.5,77 195.5,77 181.5,111 64.5,111"/><text class="tl tc" x="130" y="98">INPUT Score</text><polygon class="fp s-acc sw2" points="130,154 206,190 130,226 54,190"/><text class="tl tc" x="130" y="186">Score &lt; 0 OR</text><text class="tl tc" x="130" y="202">Score &gt; 100?</text><polygon class="fp s-acc sw2" points="130,282 193,310 130,338 67,310"/><text class="tl tc" x="130" y="314">Score &gt;= 40?</text><polygon class="fm2 s-acc sw2" points="71.5,383 202.5,383 188.5,417 57.5,417"/><text class="tl tc" x="130" y="404">OUTPUT "Fail"</text><rect class="fm s-acc sw2" x="88" y="446" width="84" height="32" rx="16"/><text class="tl tc" x="130" y="466">End</text><polygon class="fm2 s-acc sw2" points="316,173 468,173 454,207 302,207"/><text class="tl tc" x="385" y="194">OUTPUT "Invalid"</text><polygon class="fm2 s-acc sw2" points="326.5,293 457.5,293 443.5,327 312.5,327"/><text class="tl tc" x="385" y="314">OUTPUT "Pass"</text><path class="ln" fill="none" d="M130 44 L130 77" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 111 L130 154" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 226 L130 282" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 338 L130 383" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 417 L130 446" marker-end="url(#ah)"/><path class="ln" fill="none" d="M206 190 L302 190" marker-end="url(#ah)"/><path class="ln" fill="none" d="M193 310 L312.5 310" marker-end="url(#ah)"/><path class="ln" fill="none" d="M385 173 L385 94 L195.5 94" marker-end="url(#ah)"/><path class="ln" fill="none" d="M385 327 L385 462 L172 462" marker-end="url(#ah)"/><text class="tl" x="214" y="182">Yes</text><text class="tl" x="138" y="248">No</text><text class="tl" x="201" y="302">Yes</text><text class="tl" x="138" y="360">No</text></svg><figcaption>A score-checking flowchart.</figcaption></figure>
:::

H: The arrow from `OUTPUT "Invalid"` returns to `INPUT Score`: that is a loop, and its test comes before its body.
H: After the loop, the second diamond is an ordinary IF with a Yes and a No branch.
A: One possible answer:

```pseudocode
INPUT Score
WHILE Score < 0 OR Score > 100
   OUTPUT "Invalid"
   INPUT Score
ENDWHILE
IF Score >= 40 THEN
   OUTPUT "Pass"
ELSE
   OUTPUT "Fail"
ENDIF
```

- `INPUT Score` before the loop [B1]
- a loop whose condition is `Score < 0 OR Score > 100` [B1]
- `OUTPUT "Invalid"` and `INPUT Score` again inside the loop [B1]
- `IF Score >= 40` after the loop [B1]
- `OUTPUT "Pass"` in the THEN branch [B1]
- `OUTPUT "Fail"` in the ELSE branch, with ENDWHILE and ENDIF correctly placed [B1]

(A `REPEAT … UNTIL Score >= 0 AND Score <= 100` loop with `INPUT Score` first and an IF that outputs "Invalid" is also correct.)

Q: [6 marks] ★★ Describe, in order, the flowchart symbols you would draw for this pseudocode, including the labels on the decisions.

```pseudocode
Count ← 0
REPEAT
   INPUT Number
   IF Number MOD 2 = 1 THEN
      Count ← Count + 1
   ENDIF
UNTIL Number = 0
OUTPUT Count
```

H: There are two decisions. The second, after the IF, is the loop test of the REPEAT, so the arrow back to `INPUT Number` leaves it on the answer that does **not** stop the loop.
A: A full flowchart, in order:

1. a Start terminator, then a process `Count ← 0` [B1]
2. a parallelogram `INPUT Number` [B1]
3. a decision `Number MOD 2 = 1?` with the Yes exit to a process `Count ← Count + 1` and the No exit going on [B1]
4. both routes join before the second decision, so the process box and the No exit lead to it [B1]
5. a decision `Number = 0?` with its No exit going back to `INPUT Number` and its Yes exit going on [B1]
6. a parallelogram `OUTPUT Count`, then an End terminator [B1]

(Accept the loop decision written as `Number <> 0?` with Yes returning to the INPUT. Both decisions need Yes and No labels.) For the typed values 3, 8, 5, 0 the program outputs 2, because 3 and 5 are odd.

Q: [5 marks] ★★ Write pseudocode for this structured English. Use a variable called Price.

```text
1. Set Total to 0
2. Repeat 5 times
3.    Input Price
4.    If Price is more than 50 then
5.       Add Price minus 5 to Total
6.    Otherwise
7.       Add Price to Total
8. Output Total
```

H: "Repeat 5 times" is a count-controlled loop: it needs a loop variable.
A: One possible answer:

```pseudocode
Total ← 0
FOR Count ← 1 TO 5
   INPUT Price
   IF Price > 50 THEN
      Total ← Total + Price - 5
   ELSE
      Total ← Total + Price
   ENDIF
NEXT Count
OUTPUT Total
```

- `Total ← 0` before the loop [B1]
- a loop that runs five times with `INPUT Price` inside it [B1]
- the correct condition `Price > 50` [B1]
- the discount (Price − 5) added in the THEN branch and the full price in the ELSE branch [B1]
- `OUTPUT Total` after the loop (not inside it) [B1]

For the prices 60, 20, 50, 80 and 10, the total is \(55 + 20 + 50 + 75 + 10 = 210\). A price of exactly 50 is **not** more than 50, so it is added in full.

Q: [3 marks] ★★★ The flowchart below should output the mean of five marks. It contains errors.

:::html
<figure class="fig"><svg viewBox="0 0 520 474" role="img" aria-label="A flowchart. Start, then Count gets 1, then a decision Count less than or equal to 5. The exit labelled No leads right to INPUT Mark, then Total gets Total plus Mark, then Count gets Count plus 1, then an arrow goes back up to the line above the decision. The exit labelled Yes leads down to Mean gets Total divided by 4, then OUTPUT Mean, then End."><rect class="fm s-acc sw2" x="88" y="12" width="84" height="32" rx="16"/><text class="tl tc" x="130" y="32">Start</text><rect class="f1 s-acc sw2" x="75" y="73" width="110" height="38" rx="3"/><text class="tl tc" x="130" y="96">Count ← 1</text><polygon class="fp s-acc sw2" points="130,162 188,190 130,218 72,190"/><text class="tl tc" x="130" y="194">Count &lt;= 5?</text><rect class="f1 s-acc sw2" x="61" y="281" width="138" height="38" rx="3"/><text class="tl tc" x="130" y="304">Mean ← Total / 4</text><polygon class="fm2 s-acc sw2" points="78.5,355 195.5,355 181.5,389 64.5,389"/><text class="tl tc" x="130" y="376">OUTPUT Mean</text><rect class="fm s-acc sw2" x="88" y="424" width="84" height="32" rx="16"/><text class="tl tc" x="130" y="444">End</text><polygon class="fm2 s-acc sw2" points="337,173 447,173 433,207 323,207"/><text class="tl tc" x="385" y="194">INPUT Mark</text><rect class="f1 s-acc sw2" x="302" y="233" width="166" height="38" rx="3"/><text class="tl tc" x="385" y="256">Total ← Total + Mark</text><rect class="f1 s-acc sw2" x="312.5" y="295" width="145" height="38" rx="3"/><text class="tl tc" x="385" y="318">Count ← Count + 1</text><path class="ln" fill="none" d="M130 44 L130 73" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 111 L130 162" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 218 L130 281" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 319 L130 355" marker-end="url(#ah)"/><path class="ln" fill="none" d="M130 389 L130 424" marker-end="url(#ah)"/><path class="ln" fill="none" d="M188 190 L323 190" marker-end="url(#ah)"/><path class="ln" fill="none" d="M385 207 L385 233" marker-end="url(#ah)"/><path class="ln" fill="none" d="M385 271 L385 295" marker-end="url(#ah)"/><path class="ln" fill="none" d="M457.5 314 L505 314 L505 140 L130 140" marker-end="url(#ah)"/><text class="tl" x="196" y="182">No</text><text class="tl" x="138" y="242">Yes</text></svg><figcaption>A flowchart meant to output the mean of five marks.</figcaption></figure>
:::

Identify three errors and say how each should be corrected.
H: Dry run it with the marks 10, 20, 30, 40, 50. Does the loop body ever run? Is Total ever set?
A: Three of these errors earn one mark each:

- the **Yes and No labels on the decision are the wrong way round**: the loop body should be on the Yes exit and the output on the No exit [B1]
- **Total is never set to 0** before the loop, so the sum starts with an undefined value; add `Total ← 0` after Start [B1]
- the mean divides by **4**, but five marks are added, so it should be `Total / 5` [B1]

(Accept dividing by `Count - 1`, because Count is 6 when the loop ends.) With marks 10, 20, 30, 40 and 50 the correct total is 150 and the mean \(150 \div 5 = 30\).

Q: [4 marks] ★★★ A shop's till program must accept a card payment only when the card has not expired, the amount is more than 0.00 and at most 500.00, and the customer has entered the PIN correctly. (a) Write this as one condition, using the BOOLEAN variables NotExpired and PinCorrect and the REAL variable Amount. [3] (b) A WHILE loop should keep asking for a PIN while the condition in (a) is **false**. Write that loop's condition using NOT. [1]
H: "More than 0.00 and at most 500.00" needs two comparisons joined by AND.
A: (a) `NotExpired AND Amount > 0.00 AND Amount <= 500.00 AND PinCorrect`

- `Amount > 0.00` [B1]
- `Amount <= 500.00` [B1]
- all four parts joined with AND, using NotExpired and PinCorrect on their own [B1]

(b) `WHILE NOT (NotExpired AND Amount > 0.00 AND Amount <= 500.00 AND PinCorrect)` [B1]. (Accept the expanded form `NOT NotExpired OR Amount <= 0.00 OR Amount > 500.00 OR NOT PinCorrect`.)
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A cash machine holds only notes of 50, 20 and 10. A user asks for an amount that is a multiple of 10, such as 180. Using stepwise refinement, design an algorithm that outputs the **smallest** number of notes that makes up the amount, and the number of notes of each value. (a) Write Level 1 and Level 2 in structured English. [3] (b) Write the Level 3 pseudocode, using DIV and MOD. [5] (c) Give the output for 180.
H: Use as many 50s as possible first, then as many 20s as possible from what is left, then 10s.
H: `Amount DIV 50` is how many 50s fit; `Amount MOD 50` is what remains.
A: (a)

```text
Level 1:
1. Get the amount
2. Work out the notes
3. Show the notes

Level 2:
1. Get the amount
   1.1 Input the amount
2. Work out the notes
   2.1 Fifties: the whole number of 50s in the amount, and the amount left over
   2.2 Twenties: the whole number of 20s in the amount left, and the amount left over
   2.3 Tens: the amount left, divided by 10
3. Show the notes
   3.1 Output the three counts
```

(b)

```pseudocode
INPUT Amount
Fifties ← Amount DIV 50
Amount ← Amount MOD 50
Twenties ← Amount DIV 20
Amount ← Amount MOD 20
Tens ← Amount DIV 10
OUTPUT "50s: ", Fifties
OUTPUT "20s: ", Twenties
OUTPUT "10s: ", Tens
```

- Level 1 has three sensible steps in order (input, calculate, output) [B1]
- Level 2 breaks the calculation into the three note values, largest first [B1]
- Level 2 shows the amount left over being passed on [B1]
- `Amount DIV 50` for the number of fifties [B1]
- `Amount MOD 50` to keep what is left [B1]
- the same DIV and MOD pattern for 20 [B1]
- the number of tens from what remains (`Amount DIV 10`) [B1]
- the three counts output [B1]

(c) For 180: \(180 \div 50\) is 3 remainder 30; \(30 \div 20\) is 1 remainder 10; \(10 \div 10\) is 1. The output is 3 fifties, 1 twenty and 1 ten, 5 notes. Using the largest notes first gives the fewest notes here because each note value divides evenly into the next larger one.

Q: [4 marks] ★★★ Two students rewrite the same loop. Version A uses `REPEAT … UNTIL Number = 0` and version B uses `WHILE Number <> 0`. Both read Number with `INPUT Number` and add it to Total. (a) For the typed values 4, 6, 0, say what each version leaves in Total and how many times each loop body runs. (b) For the typed value 0 only, say what happens in each version. (c) State one situation where each loop type is the better choice.
A: Version A (REPEAT) with `INPUT Number` as the first line inside the loop and `Total ← Total + Number` after it; version B (WHILE) with `INPUT Number` once before the loop and again as the last line inside it, adding Number first.

- (a) Both give Total = 10. Version A runs its body 3 times (4, 6 and 0: the 0 is added, which does no harm). Version B runs its body 2 times [B1] [B1]
- (b) Version A runs its body once and adds 0, then stops. Version B runs its body zero times [B1]
- (c) REPEAT when the body must run at least once, for example asking for a password. WHILE when the data may be empty, for example reading values until a sentinel when there may be none [B1]
:::

:::quiz
? Which of these is the best description of abstraction?
- Splitting a problem into smaller sub-problems.
+ Removing unnecessary detail so that only the essential features remain.
- Writing an algorithm as a flowchart.
- Testing a program with many sets of data.
> Abstraction is about leaving detail out. Splitting a problem into parts is decomposition, and the other options are about documenting and testing.
? A program is split into modules called ShowMenu, CalculateBill and PrintReceipt. This is an example of:
- abstraction
+ decomposition
- iteration
- validation
> The problem has been broken into smaller parts that each become a module. Abstraction would instead remove detail from the problem.
? Which is a valid pseudocode identifier?
- `Final Score`
- `3rdAttempt`
+ `Final_Score`
- `WHILE`
> Identifiers use letters, digits and underscores only, start with a letter and cannot be keywords. A space, a leading digit and a keyword each break a rule.
? What does a flowchart decision symbol have?
- one exit, labelled with the answer
+ two exits, labelled Yes and No
- three exits, one for each possible value
- no exits, because it only shows a test
> A decision asks a question that has two answers, so it has exactly two exits.
? A flowchart has a diamond **before** the boxes it controls, with an arrow from the last box back to the diamond. This is:
- a REPEAT … UNTIL loop
+ a WHILE loop
- a nested IF
- a FOR loop with STEP
> The test comes first and the loop returns to it, so the body may run zero times. That is a pre-condition WHILE loop.
? Which condition is true for a number between 10 and 20, inclusive?
- `10 <= Number <= 20`
- `Number >= 10 OR Number <= 20`
+ `Number >= 10 AND Number <= 20`
- `Number > 10 AND Number < 20`
> Two comparisons joined by AND is correct. A chained comparison is not valid pseudocode, OR is true for every number, and the last option leaves out 10 and 20.
? The condition of a REPEAT loop is `Age >= 5 AND Age <= 18`. What is the equivalent WHILE condition?
- `Age >= 5 AND Age <= 18`
- `Age < 5 AND Age > 18`
+ `Age < 5 OR Age > 18`
- `Age <= 5 OR Age >= 18`
> NOT(A AND B) is (NOT A) OR (NOT B). Each comparison is reversed and AND changes to OR. The last option reverses to `<=` and `>=`, which wrongly includes 5 and 18.
? In stepwise refinement, what is true of the final level?
- It is written as a flowchart.
- It contains the test data.
+ Each step can be written directly as a pseudocode statement.
- It is the same as Level 1.
> Refinement stops when every step is small and exact enough to become a statement of code.
:::

:::checklist What you can now do
- [ ] I can describe the need for abstraction, its purpose and its benefits, and decide which details a model needs.
- [ ] I can decompose a problem into sub-problems that become modules (procedures and functions).
- [ ] I can define an algorithm and recognise sequence, selection and iteration in it.
- [ ] I can choose suitable identifier names and complete an identifier table.
- [ ] I can write an algorithm as structured English, as a flowchart and as pseudocode.
- [ ] I can convert pseudocode from structured English or from a flowchart, and a flowchart from structured English or pseudocode.
- [ ] I can recognise a WHILE or REPEAT loop and a nested selection in a flowchart.
- [ ] I can refine an algorithm in stages until each step is a statement of code.
- [ ] I can write conditions as logic statements with AND, OR and NOT, and turn a condition round for the other loop type.
- [ ] I can find an error in an algorithm by completing a trace table.
:::

:::recap
- **Abstraction** removes detail so only essential features remain; **decomposition** splits a problem into modules. They are different skills.
- An **algorithm** is a sequence of defined steps. It uses sequence, selection and iteration, and takes input, processes it and gives output.
- Identifiers use letters, digits and underscores, start with a letter, have no spaces and are not case sensitive. An **identifier table** lists identifier, data type and description.
- Structured English, a flowchart and pseudocode are three forms of the same algorithm. A flowchart has one Start, one End, and decisions with exactly two exits labelled Yes and No.
- A diamond before the body with a return arrow is a WHILE loop; a diamond after the body is REPEAT … UNTIL. For a chain of questions, nest a new `IF` in the `ELSE`, each with its own `ENDIF`.
- **Stepwise refinement** rewrites each step in more detail until every step is one statement.
- Write conditions as comparisons joined with AND, OR and NOT; never chain comparisons. Negating a condition reverses each comparison and swaps AND and OR.
- A **trace table** has a column for each variable and the output and a row for each change; use it to check an algorithm by hand.
:::

:::links
- practise: [Algorithms: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/19-computational-thinking-and-problem-solving-/algorithms/exam-questions/) · Save My Exams · 9618 algorithm questions with mark schemes [paid]
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations of abstraction, decomposition and algorithms, with questions
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run the Python programs in this chapter line by line and watch every variable
- read: [Khan Academy: algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) · Khan Academy · what an algorithm is and how to compare algorithms
- practise: [CS50](https://cs50.harvard.edu/x/) · Harvard CS50 · a free introductory course with problem sets
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · the official rules for the pseudocode you must write

Links checked 13 November 2026.
:::

Next: [Programming basics: variables, selection and loops](#cs.programming)
