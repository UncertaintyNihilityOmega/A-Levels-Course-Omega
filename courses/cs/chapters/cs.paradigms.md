@chapter cs.paradigms
@title Programming paradigms: low-level, imperative and declarative
@level a2
@paper CAIE 9618 Paper 3
@time 5–7 hours
@summary A programming paradigm is a style of programming. You will compare the imperative, object-oriented, low-level and declarative paradigms, write low-level loops with indexed and indirect addressing, and write facts, rules and goals in the declarative style that Paper 3 tests.

:::why
Every program you have written so far told the computer what to do, step by step. That is only one way to program. A processor runs instructions that each do one tiny job. A class groups data with the code that uses it. A declarative program states facts and rules and lets the computer work out the answers. Paper 3 asks you to recognise these styles, to write in two of them (low-level code and facts and rules) and to say when each one fits.
:::

**Before you start**, you should know the instruction set and the addressing modes from [Processor fundamentals and assembly language](#cs.assembly), and procedures and functions from [Procedures, functions and parameters](#cs.procedures).

:::try Warm-up
Q: IX holds 2. Which memory location does `LDX 150` read? (from [Processor fundamentals and assembly language](#cs.assembly))
A: Indexed addressing adds IX to the operand, so it reads location \(150 + 2 = 152\).
Q: What can a function do that a procedure cannot? (from [Procedures, functions and parameters](#cs.procedures))
A: A function returns a value, so it can be used inside an expression. A procedure is called on its own with `CALL`.
Q: What is a class, and what is an object? (from [Object-oriented programming](#cs.oop))
A: A class is a template that describes the attributes and methods of a kind of thing. An object is one instance made from that template.
:::

:::note How code appears in this course
Pseudocode follows the Cambridge Pseudocode Guide for 2027–2029. Assembly language uses the Cambridge example instruction set in `text` blocks. Declarative code is written in the Prolog style that Cambridge papers print, with the words `IF`, `AND` and `NOT`. A block introduced by "Output:" is exactly what the program prints, and every Python example here has been run to check it.
:::

## What is a programming paradigm?

A **paradigm** is a way of thinking about a program. Two programmers can solve the same problem in different paradigms and get the same answer, but the code looks very different and the programmer's job is different too.

:::def Programming paradigm
A style or approach to programming, with its own concepts and its own way of expressing a solution. A paradigm decides what the programmer writes (steps, objects, machine instructions or facts and rules) and what the computer works out for itself.
:::

:::analogy Giving directions or describing the goal
Imagine you want to eat jollof rice. In the **imperative** way you write the recipe: wash the rice, fry the onions, add the tomato, simmer for 25 minutes. In the **declarative** way you say "I want jollof rice" and the kitchen decides how to make it. In the **low-level** way you tell the cook exactly which hand to move and which pan to lift. In the **object-oriented** way you have a Chef object and a Pot object that each know their own jobs and ask each other for help.
:::

The syllabus names four paradigms. This table is the one to learn.

| Paradigm | How a program is expressed | What the programmer controls | Typical use |
|---|---|---|---|
| Low-level | instructions of the processor (assembly or machine code), one small operation each | registers, memory addresses, the order of every instruction | device drivers, embedded controllers, parts of an operating system where speed and size matter |
| Imperative (procedural) | a sequence of statements that change variables, grouped into procedures and functions | the exact order of steps and the values of variables | most general programs: calculations, data processing, games |
| Object-oriented | classes and objects with attributes and methods; objects work together by calling methods | how data and behaviour are packaged into classes | large programs with many related kinds of thing |
| Declarative | facts and rules that describe what is true, then a goal to satisfy | only the facts and rules: the system chooses how to search | databases of knowledge, expert systems, logic puzzles |

Most real languages mix paradigms. Python lets you write imperative, object-oriented and (a little) declarative code in one file. The paradigm is a way of working, not a language.

## Imperative and procedural programming

:::def Imperative programming
A paradigm in which a program is a sequence of statements that change the state of the program (the values of its variables) step by step. The programmer states **how** to solve the problem, in order.
:::

:::def Procedural programming
Imperative programming in which the program is divided into named procedures and functions, each doing one job and called when needed. It is the structured programming you learnt at AS Level.
:::

You have written imperative programs since the first chapter. The word *state* is the key: a variable holds a value, an assignment changes it, and the program's meaning is the sequence of changes. Here is a classic imperative task. Five students sat a test and a pass mark is 50. The data is in two arrays.

| Index | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Names | Chioma | Dev | Elif | Femi | Gita |
| Marks | 64 | 48 | 91 | 50 | 37 |

In pseudocode, the program visits each element in order, tests it and outputs the names that passed.

```pseudocode
DECLARE Index, PassCount : INTEGER

PassCount ← 0
FOR Index ← 1 TO 5
   IF Marks[Index] >= 50 THEN
      OUTPUT Names[Index]
      PassCount ← PassCount + 1
   ENDIF
NEXT Index
OUTPUT "Passed: ", PassCount
```

The same program in Python (the lists start at index 0, so the loop runs from 0 to 4):

```python
names = ["Chioma", "Dev", "Elif", "Femi", "Gita"]
marks = [64, 48, 91, 50, 37]

pass_count = 0
for index in range(5):
    if marks[index] >= 50:
        print(names[index])
        pass_count = pass_count + 1
print("Passed:", pass_count)
```

Output:

```output
Chioma
Elif
Femi
Passed: 3
```

Everything in this program is a command: set a counter, repeat, test, output, add one. Two variables change as it runs, `Index` and `PassCount`, and the programmer decides every step. That is the imperative paradigm.

:::key Characteristics of imperative (procedural) programs
- A program is a **sequence of instructions** that the computer carries out in order, with selection and iteration to change the order.
- It has **state**: variables whose values change as the program runs.
- The programmer says **how** the result is reached, step by step.
- Code is organised into **procedures and functions** that are called, so each job is written once and reused.
:::

Procedural programming adds one idea: do not write one long block. Split the work into modules, as in [Procedures, functions and parameters](#cs.procedures). The pass-count loop becomes a function `CountPasses(Marks, PassMark)` that returns a number, and the main program just calls it.

## Object-oriented programming

In the object-oriented paradigm the program is a set of **objects**. Each object holds its own data (attributes) and the code that works on that data (methods). Classes describe the objects, inheritance lets one class build on another, and polymorphism lets different classes respond to the same method call in their own way. The paradigm is built on the imperative one, because the body of every method is imperative code. It is the subject of [Object-oriented programming](#cs.oop), so this chapter does not repeat it. In the exam you may be asked to state that it is a paradigm, and to say how it differs from procedural programming: the data and the code that uses it are kept together in one object, and the program is organised around those objects rather than around a list of procedures.

## Low-level programming

:::def Low-level programming
Programming using instructions that map closely to the instruction set of the processor, such as assembly language and machine code. Each instruction does one small operation on a register or a memory location, and the programmer manages the registers and the memory directly.
:::

A high-level statement such as `Total ← Total + Marks[Index]` becomes several processor instructions: load a value, add another, store the result. In a low-level language **you** write those steps. You also decide where each value lives in memory and how to reach it.

Low-level programming is not better or worse than high-level programming. It trades convenience for control.

- **Advantages:** the program can be small and very fast, because there is no translation overhead and the programmer chooses every instruction. It can reach hardware directly, such as a sensor or a memory-mapped device.
- **Disadvantages:** programs are long and hard to read, one small mistake can crash the machine, and the code is written for one type of processor, so it must be rewritten for another.

### The five addressing modes

Every instruction that touches data must say where the data is. The **addressing mode** is the rule for turning the operand into the data. You met all five in [Processor fundamentals and assembly language](#cs.assembly); here they are compared on one memory. (The example instruction set has no relative instruction, as the paragraph after the table explains.) Locations 160 to 165 hold:

| Address | 160 | 161 | 162 | 163 | 164 | 165 |
|---|---|---|---|---|---|---|
| Contents | 165 | 7 | 41 | 12 | 50 | 99 |

IX holds 2.

:::def Immediate addressing
The operand is the value itself. `LDM #160` puts the number 160 in ACC. No memory location is read.
:::

:::def Direct addressing
The operand is the address of the data. `LDD 160` reads location 160, so ACC receives 165.
:::

:::def Indirect addressing
The operand is the address of a location that holds the **address** of the data. `LDI 160` reads location 160, finds 165, then reads location 165, so ACC receives 99.
:::

:::def Indexed addressing
The address used is the operand plus the contents of the index register IX. `LDX 160` with IX holding 2 reads location \(160 + 2 = 162\), so ACC receives 41.
:::

:::def Relative addressing
The address used is given as an offset from the address of the current instruction. An instruction at address 105 with an offset of 3 refers to address \(105 + 3 = 108\).
:::

| Instruction | Mode | Steps | ACC afterwards |
|---|---|---|---|
| `LDM #160` | immediate | use 160 itself | 160 |
| `LDD 160` | direct | read location 160 | 165 |
| `LDI 160` | indirect | read 160, giving 165, then read location 165 | 99 |
| `LDX 160` | indexed | read location \(160 + 2 = 162\) | 41 |

The example instruction set has no relative-addressing instruction, so a question that uses it defines the instruction. In this course the instruction is `JMR #n`: jump to the instruction whose address is the address of the `JMR` plus n, where n may be negative. A `JMR #3` at address 105 makes the next instruction come from address 108. A `JMR #-4` at address 112 sends the processor back to address 108.

:::key Choosing an addressing mode
- **Immediate**: a constant in the program (`LDM #0` to start a total).
- **Direct**: one named variable (`LDD COUNT`).
- **Indirect**: the data is reached through a **pointer** stored in memory. Changing the pointer changes which data is used.
- **Indexed**: an **array**: keep the first address as the operand and change IX to move along it.
- **Relative**: jumps and branches that must still work if the whole program is moved to another place in memory.
:::

The most common slip is mixing up indirect and indexed addressing, because both reach a location that is not named in the instruction. The difference is where the extra number comes from. In **indirect** addressing it comes from **memory** (the contents of the location named). In **indexed** addressing it comes from the **index register** and is added to the operand.

### Indexed addressing: totalling an array

The array is stored in consecutive locations, so one `LDX` instruction can read any element when IX holds the element's offset. A loop that increases IX by one each time visits them all. The instruction set has no instruction that compares IX with a number, so the loop uses a count that is kept in memory and counted down.

:::eg Adding six numbers (exam style)
Six numbers are stored in consecutive memory locations. Write assembly language code, using indexed addressing, to add them and store the total in a location named `TOTAL`. The numbers are 14, 9, 22, 5, 18 and 7. [6 marks]

Plan the program in steps. IX starts at 0 so the first `LDX` reads the first number. TOTAL starts at 0. Each pass loads a number, adds the running total, stores the new total and moves IX on. A location `COUNT`, set to 6, is reduced by one each pass; when it reaches 0 the loop ends.

```text
100  START:  LDR #0
101          LDM #0
102          STO TOTAL
103  LOOP:   LDX NUMS
104          ADD TOTAL
105          STO TOTAL
106          INC IX
107          LDD COUNT
108          SUB #1
109          STO COUNT
110          CMP #0
111          JPN LOOP
112          END
113  NUMS:   14
114          9
115          22
116          5
117          18
118          7
119  TOTAL:  0
120  COUNT:  6
```

After each pass the values are these.

| Pass | Number read | IX | TOTAL | COUNT |
|---|---|---|---|---|
| 1 | 14 | 1 | 14 | 5 |
| 2 | 9 | 2 | 23 | 4 |
| 3 | 22 | 3 | 45 | 3 |
| 4 | 5 | 4 | 50 | 2 |
| 5 | 18 | 5 | 68 | 1 |
| 6 | 7 | 6 | 75 | 0 |

On the sixth pass COUNT becomes 0, `CMP #0` is TRUE and `JPN LOOP` does not jump, so `END` runs with 75 in TOTAL.

- IX set to 0 with `LDR #0` before the loop, and TOTAL set to 0 [B1]
- `LDX NUMS` reads the current number, with NUMS the first address of the array [B1]
- the number is added to the total and the total stored back in TOTAL [B1]
- `INC IX` moves to the next element [B1]
- a count of 6 reduced each pass and compared with 0, with `JPN` back to the start of the loop [B1]
- `END`, and the data locations NUMS, TOTAL and COUNT defined [B1]
:::

Check this against the table: the program in the example stores 75, and \(14 + 9 + 22 + 5 + 18 + 7 = 75\).

:::warn The compare tests ACC, not IX
`CMP #0` compares the **accumulator** with 0. It never looks at IX. A loop that must run a fixed number of times therefore needs a counter that passes through ACC (load it, subtract, store it, compare), or a sentinel value at the end of the data, as in [Processor fundamentals and assembly language](#cs.assembly).
:::

### Indirect addressing: following a pointer

A **pointer** is a location that holds an address. If PTR holds 150, then `LDI PTR` loads the value stored at location 150, and if the program adds one to PTR the same instruction now reads location 151. The program below does the same job as the indexed loop, but it moves a pointer instead of IX. Three numbers, 8, 15 and 6, are stored from location 150.

:::eg Totalling through a pointer
Trace this program. Show the accumulator, PTR, COUNT, TOTAL and the compare result for the first pass, then give the values after each pass. [exam style]

```text
100  START:  LDM #0
101          STO TOTAL
102  LOOP:   LDI PTR
103          ADD TOTAL
104          STO TOTAL
105          LDD PTR
106          INC ACC
107          STO PTR
108          LDD COUNT
109          SUB #1
110          STO COUNT
111          CMP #0
112          JPN LOOP
113          END
114  PTR:    150
115  COUNT:  3
116  TOTAL:  0
150          8
151          15
152          6
```

First pass:

| Address | Instruction | ACC | [PTR] | [COUNT] | [TOTAL] | Compare |
|---|---|---|---|---|---|---|
| start | | | 150 | 3 | 0 | |
| 100 | LDM #0 | 0 | | | | |
| 101 | STO TOTAL | | | | 0 | |
| 102 | LDI PTR | 8 | | | | |
| 103 | ADD TOTAL | 8 | | | | |
| 104 | STO TOTAL | | | | 8 | |
| 105 | LDD PTR | 150 | | | | |
| 106 | INC ACC | 151 | | | | |
| 107 | STO PTR | | 151 | | | |
| 108 | LDD COUNT | 3 | | | | |
| 109 | SUB #1 | 2 | | | | |
| 110 | STO COUNT | | | 2 | | |
| 111 | CMP #0 | | | | | FALSE |
| 112 | JPN LOOP | | | | | |

`LDI PTR` is the instruction to study: PTR holds 150, so it reads location 150 and ACC becomes 8. The program then adds one to PTR, so the second `LDI PTR` reads location 151.

| After pass | Value read | PTR | COUNT | TOTAL |
|---|---|---|---|---|
| 1 | 8 | 151 | 2 | 8 |
| 2 | 15 | 152 | 1 | 23 |
| 3 | 6 | 153 | 0 | 29 |

After pass 3 the compare is TRUE, so `JPN LOOP` does not jump and `END` runs with 29 in TOTAL.

- `LDI PTR` loads 8 from location 150 (the address held in PTR) [B1]
- the first pass ends with TOTAL 8, PTR 151 and COUNT 2 [B1]
- the second pass reads 15, so TOTAL is 23 [B1]
- the third pass reads 6, so TOTAL is 29 and COUNT is 0 [B1]
- the compare is TRUE after the third pass, so the loop ends [B1]
:::

Indirect addressing has one more use that indexed addressing cannot match: a chain of pointers. Each item stores the address of the next one, which is how a linked list lives in memory. You will try that in the Stretch question below.

### Relative addressing

An address written as an **offset** from the current instruction is called relative. It has one big benefit: the program is **relocatable**. Suppose a loop is stored from address 200 and its last instruction is `JMR #-4` at address 208. That jumps to \(208 - 4 = 204\). If the operating system loads the same program starting at 300, the same instruction sits at 308 and jumps to \(308 - 4 = 304\), which is the matching place in the moved program. A `JMP 204` would still jump to 204, and the program would break.

:::warn Offsets are counted from the instruction itself
In this course the offset in `JMR #n` is added to the address of the `JMR` instruction itself, so `JMR #1` at address 105 goes to 106, the next instruction. A question will say how its relative instruction counts; use the rule it gives.
:::

## Declarative programming

In the imperative and low-level paradigms the programmer writes the steps. In the **declarative** paradigm the programmer writes **what is true** and then asks a question. The language system, which contains a general search method, finds the answers.

:::def Declarative programming
A paradigm in which the programmer states facts and rules about a problem, and a goal that the system must satisfy. The system works out how to find the answers, so the programmer does not write the steps.
:::

The declarative language in the syllabus works like Prolog. A program is a **knowledge base** of clauses.

:::def Fact
A clause that states something that is true, such as `parent(kofi, ama).` It is made of a predicate (here `parent`) and arguments in brackets, and it ends with a full stop.
:::

:::def Rule
A clause that states that something is true **if** other things are true. It has a head, the word `IF`, and a body of one or more conditions joined by `AND`. For example `grandparent(X, Z) IF parent(X, Y) AND parent(Y, Z).`
:::

:::def Goal
A question put to the system: a statement that the system tries to **satisfy**, by finding values for its variables (or confirming that it is true) using the facts and rules.
:::

:::def Clause
A fact or a rule: one statement in a declarative program.
:::

### Facts

Here is a small knowledge base about a family in Accra, shown in the figure. Each `parent(X, Y)` fact says that X is a parent of Y.

:::html
<figure class="fig small"><svg viewBox="0 0 350 300" role="img" aria-label="A family tree with arrows from parents to children. Kofi and Abena are the parents of Ama and Yaw. Ama is the parent of Kwame. Yaw is the parent of Esi."><rect class="fm s-acc sw2" x="55" y="12" width="90" height="34" rx="4"/><text class="tl tb tc" x="100" y="34">kofi</text><rect class="fm s-acc sw2" x="205" y="12" width="90" height="34" rx="4"/><text class="tl tb tc" x="250" y="34">abena</text><rect class="fm s-acc sw2" x="55" y="130" width="90" height="34" rx="4"/><text class="tl tb tc" x="100" y="152">ama</text><rect class="fm s-acc sw2" x="205" y="130" width="90" height="34" rx="4"/><text class="tl tb tc" x="250" y="152">yaw</text><rect class="fm s-acc sw2" x="55" y="248" width="90" height="34" rx="4"/><text class="tl tb tc" x="100" y="270">kwame</text><rect class="fm s-acc sw2" x="205" y="248" width="90" height="34" rx="4"/><text class="tl tb tc" x="250" y="270">esi</text><line class="ln" x1="100" y1="46" x2="100" y2="130" marker-end="url(#ah)"/><line class="ln" x1="120" y1="46" x2="230" y2="130" marker-end="url(#ah)"/><line class="ln" x1="230" y1="46" x2="120" y2="130" marker-end="url(#ah)"/><line class="ln" x1="250" y1="46" x2="250" y2="130" marker-end="url(#ah)"/><line class="ln" x1="100" y1="164" x2="100" y2="248" marker-end="url(#ah)"/><line class="ln" x1="250" y1="164" x2="250" y2="248" marker-end="url(#ah)"/><text class="tl halo" x="108" y="94">parent</text><text class="tl halo" x="258" y="94">parent</text><text class="tl halo" x="108" y="212">parent</text><text class="tl halo" x="258" y="212">parent</text></svg><figcaption>Each arrow is a fact parent(X, Y): it points from the parent to the child. Kofi and Abena are the parents of Ama and of Yaw, Ama is the parent of Kwame, and Yaw is the parent of Esi.</figcaption></figure>
:::

The facts are:

```text
parent(kofi, ama).
parent(kofi, yaw).
parent(abena, ama).
parent(abena, yaw).
parent(ama, kwame).
parent(yaw, esi).
male(kofi).
male(yaw).
male(kwame).
female(abena).
female(ama).
female(esi).
```

Four rules of syntax apply to every clause.

:::key Syntax of facts, rules and goals
- A **constant** (a name for a particular thing) starts with a **lower-case** letter: `kofi`, `class_7a`.
- A **variable** starts with a **capital** letter: `X`, `Child`. It stands for "some value". The same variable name in one clause always stands for the same value.
- Every clause ends with a **full stop**.
- In a rule, `IF` separates the head from the body and `AND` joins conditions: every condition must be true. Cambridge questions print the words `IF` and `AND` (and `NOT`, below); a question usually prints the head of the rule and `IF`, and you write the body. A Prolog system such as SWISH writes `:-` for `IF` and a comma for `AND`, and Cambridge mark schemes accept the commas too.
:::

### Goals and results

A goal with no variables asks "is this true?". The system answers true if it can be shown from the clauses, and false if it cannot. A goal with a variable asks "for which values is it true?".

| Goal | Meaning | Result |
|---|---|---|
| `parent(kofi, ama)` | Is Kofi a parent of Ama? | true |
| `parent(esi, kofi)` | Is Esi a parent of Kofi? | false |
| `parent(X, kwame)` | Who is a parent of Kwame? | X = ama |
| `parent(kofi, X)` | Whose parent is Kofi? | X = ama, then X = yaw |

The last goal has two answers. The system finds the **first** fact that matches, reports X = ama and then, if asked for more, **backtracks** to look for another. When a Paper 3 question asks for "the result returned by the goal", it writes several answers on one line, separated by commas: `X = ama, yaw`. Write yours the same way, in the order the system finds them.

:::def Backtracking
The way the system searches for answers. It tries the clauses in order and, when a condition fails or all answers for a choice have been given, it goes back to the most recent choice and tries the next possibility.
:::

Everything not in the knowledge base is taken to be false. The system never says "I don't know": a goal is true if it can be proved, and false otherwise. A question about someone who is not in the facts has the answer false.

### Rules

Facts can only say what you wrote down. A **rule** lets the system work out new facts. A father is a male parent, so:

```text
father(X, Y) IF male(X) AND parent(X, Y).
mother(X, Y) IF female(X) AND parent(X, Y).
grandparent(X, Z) IF parent(X, Y) AND parent(Y, Z).
```

Read the first rule as: X is the father of Y if X is male and X is a parent of Y. The second rule uses a variable `Y` in the body that does not appear in the head. In the grandparent rule, Y is the person in the middle: X is a parent of Y and Y is a parent of Z.

:::eg Satisfying goals with rules (exam style)
Using the facts and rules above, state the result of each goal. [4 marks]

(a) `father(kofi, ama)` (b) `father(yaw, kwame)` (c) `grandparent(kofi, X)` (d) `mother(M, kwame)`

Work through each goal by replacing it with the conditions of the rule and checking each condition against the facts.

- (a) The rule needs `male(kofi)`, which is a fact, and `parent(kofi, ama)`, which is a fact. The result is **true**. [B1]
- (b) The rule needs `male(yaw)` (a fact) and `parent(yaw, kwame)`. There is no such fact: Kwame's parent is Ama. The result is **false**. [B1]
- (c) The rule needs `parent(kofi, Y)` and `parent(Y, X)`. The first match is Y = ama, and `parent(ama, X)` gives X = kwame. Backtracking then tries Y = yaw, and `parent(yaw, X)` gives X = esi. The results are **X = kwame** and **X = esi**. [B1]
- (d) The rule needs `female(M)` and `parent(M, kwame)`. The only parent of Kwame is ama, and `female(ama)` is a fact. The result is **M = ama**. [B1]
:::

### Rules that need a test

Some conditions are comparisons, not facts. Return to the five students and their marks. They become facts, and a rule picks out the ones who passed. This is the declarative version of the loop earlier in the chapter.

```text
mark(chioma, 64).
mark(dev, 48).
mark(elif, 91).
mark(femi, 50).
mark(gita, 37).
passed(Student) IF mark(Student, Score) AND Score >= 50.
```

The goal `passed(S)` gives S = chioma, S = elif and S = femi, in the order of the facts. Notice what is missing: there is no loop, no counter and no order of steps. The rule states what "passed" means. The imperative program said how to find the students; this one says which students count. Comparisons such as `>=`, and the test that two things are different, written `X \= Y` in Prolog, are this course's Prolog notation: none of the recent Paper 3 declarative questions checked for this course needed one, so if a question does, use the symbols it prints.

:::warn A rule that checks only one of several conditions
A university course may have two prerequisites, written as two facts: `requires(mechanics, calculus).` and `requires(mechanics, vectors).` The rule `can_take(S, C) IF requires(C, R) AND completed(S, R).` is true as soon as the student has completed **one** of them, because the system only needs one `R` that works. A student who has completed calculus but not vectors would be allowed on mechanics. To demand both, write a rule that names both conditions: `can_take_mechanics(S) IF completed(S, calculus) AND completed(S, vectors).`
:::

Sometimes the same answer appears twice. A rule for brothers and sisters might be `sibling(X, Y) IF parent(P, X) AND parent(P, Y) AND X \= Y.` In the family above, Ama and Yaw share two parents. The goal `sibling(ama, X)` therefore gives X = yaw **twice**, once through Kofi and once through Abena. The system reports every way of proving the goal.

### Rules with NOT

Recent Paper 3 questions end with a rule that needs the word **NOT**, written from a sentence such as "… may choose … if … and … has not …". `NOT` in front of a condition makes it true when that condition **cannot be proved** from the clauses, which fits the rule that everything not in the knowledge base is false.

A cookery school in Lima records its students, its courses and the courses each student has completed.

```text
student(lina).
student(omar).
course(baking).
course(grilling).
completed(lina, baking).
```

"S may enrol on C if S is a student and C is a course and S has not completed C" becomes one rule:

```text
may_enrol(S, C) IF student(S) AND course(C) AND NOT completed(S, C).
```

| Goal | Result |
|---|---|
| `may_enrol(lina, X)` | X = grilling |
| `may_enrol(S, baking)` | S = omar |
| `may_enrol(omar, X)` | X = baking, grilling |

Lina cannot enrol on baking: `completed(lina, baking)` is a fact, so `NOT completed(lina, baking)` is false. Omar has completed nothing, so `NOT completed(omar, C)` is true for both courses. Mark schemes also accept the comma form and brackets after NOT: `student(S), course(C), NOT(completed(S, C)).`

:::warn Put NOT after the conditions that choose the values
`NOT` can only test values that have already been chosen. The rule `may_enrol(S, C) IF NOT completed(S, C) AND student(S) AND course(C).` gives **no** results for the goal `may_enrol(S, C)`: S and C are still unknown when the NOT is tried, `completed(S, C)` matches the fact about Lina, so the NOT fails before any student or course is picked. Cambridge's model answers write the NOT condition last (9618/31 and 9618/32, June 2024), and so should you.
:::

### Rules that refer to themselves

A rule may use its own name in its body. An **ancestor** is a parent, or the parent of an ancestor.

```text
ancestor(X, Y) IF parent(X, Y).
ancestor(X, Y) IF parent(X, Z) AND ancestor(Z, Y).
```

The first rule is the stopping case, like the base case of a recursive function. The second rule moves one generation up. The goal `ancestor(kofi, X)` gives X = ama, X = yaw, X = kwame, X = esi, in that order: the first rule finds the children, and the second rule goes down through each child in turn. This is recursion again, expressed as a rule instead of a function.

### Writing facts and rules from a description

Exam questions give a description and ask you to write the clauses. A reliable method has four steps.

:::steps
1. List the **things** and the **relationships** the description mentions. Each relationship becomes a predicate (a name in lower case, such as `teaches`).
2. Write one **fact** for every relationship that the description states.
3. For a relationship that is **worked out** from others, write a **rule**: the head is the new predicate and the body lists the facts it depends on.
4. Check that every variable you use in the body is either in the head or links two conditions, that constants are lower case, and that every clause ends with a full stop.
:::

:::eg Writing facts and a rule from a scenario (exam style)
A bus company in Lima records which driver drives which route and which routes pass through which district. Write facts to record that Marta drives route 12 and Pablo drives route 40, and that route 12 serves the district of Miraflores. Then write a rule `serves_driver(District, Driver)` that is true when a driver drives a route that serves the district. [4 marks]

The relationships are *drives* (driver, route) and *serves* (route, district). The facts use lower-case constants.

```text
drives(marta, route_12).
drives(pablo, route_40).
serves(route_12, miraflores).
serves_driver(District, Driver) IF serves(Route, District) AND drives(Driver, Route).
```

- facts with the predicate `drives`, correct for both drivers [B1]
- fact with the predicate `serves` for route 12 and Miraflores [B1]
- rule head `serves_driver(District, Driver)` followed by `IF` [B1]
- body: both conditions joined by `AND`, with the variable `Route` linking them [B1]

(Reject variables written in lower case and clauses with no full stop. Accept any sensible predicate names if they are used consistently.)
:::

:::eg Spot the error: the grandparent rule
A student wrote the rule below. The knowledge base is the family in the figure. The student then asked the goal `grandparent(kofi, Z)` and expected to see kwame and esi.

```text
grandparent(X, Z) IF parent(X, Y) AND parent(X, Z).
```

**Question:** What does the goal give, what is the mistake and what is the fix? [3 marks]

The second condition should link Y to Z. The student wrote X again, so the rule says that X is a parent of both Y and Z. For Kofi, both conditions match the same two children, so the goal gives Z = ama and Z = yaw twice over: Kofi's children, not his grandchildren.

- Mistake: the second condition uses `X` instead of `Y` [B1]
- Result of the faulty rule: the children of Kofi, ama and yaw, not kwame and esi [B1]
- Fix: `parent(Y, Z)`, so the rule is `grandparent(X, Z) IF parent(X, Y) AND parent(Y, Z).` [B1]
:::

## Backtracking, step by step

You rarely need to write out the whole search, but you must be able to explain it. Take the goal `grandparent(kofi, W)`, with the correct rule `grandparent(X, Z) IF parent(X, Y) AND parent(Y, Z).` The system works through the body from left to right.

1. It replaces the goal with `parent(kofi, Y)` then `parent(Y, W)`.
2. It tries the first fact that matches `parent(kofi, Y)`: `parent(kofi, ama)`, so Y = ama.
3. It now needs `parent(ama, W)`. The only matching fact is `parent(ama, kwame)`, so W = kwame. Both conditions are satisfied: the first answer is **W = kwame**.
4. Asked for another answer, it **backtracks** to the most recent choice that had another option. There are no more facts for `parent(ama, W)`, so it goes back one more step to `parent(kofi, Y)` and takes the next fact, `parent(kofi, yaw)`, so Y = yaw.
5. It needs `parent(yaw, W)`: `parent(yaw, esi)` matches, so the second answer is **W = esi**.
6. It backtracks again. `parent(kofi, Y)` has no more facts, so the search ends. There are no more answers.

The answers come in the order of the facts, because the system always takes facts from the top.

## Choosing a paradigm

Declarative programming is ideal when the problem is a set of relationships and the answer is a search: family trees, route networks, medical diagnosis rules, scheduling rules. It is poor at problems that are mainly a sequence of actions: reading input, drawing graphics, controlling a machine, because there the **order** of steps matters and the programmer needs to control it.

:::eg Comparing imperative and declarative programming (exam style)
Compare imperative and declarative programming. [3 marks]

- An imperative program is a sequence of statements that the programmer writes to say **how** to solve the problem step by step [B1]
- A declarative program is facts and rules that state **what** is true, and the system works out how to satisfy a goal [B1]
- Imperative programs change the values of variables (state) as they run, but declarative programs use no assignment: the answers come from searching the facts and rules (or: declarative programs are shorter for relationship problems, but give the programmer less control over the order of the search) [B1]
:::

| | Imperative | Declarative |
|---|---|---|
| The programmer writes | steps to carry out | facts and rules |
| Control of the order | the programmer's | the system's (top to bottom, backtracking) |
| State | variables change by assignment | no assignment: values come from matching |
| Natural for | calculations, input and output, loops | relationships, searches, rule-based knowledge |

:::exam Paradigm questions in Paper 3
- Say which paradigm a snippet belongs to by pointing at its features: `LDX` and `INC IX` are low-level, `IF`/`AND` clauses are declarative, `CLASS` and `NEW` are object-oriented, a loop with assignments is imperative.
- For "write facts and rules", every constant is lower case, every variable is capitalised, every clause ends with a full stop, and a rule head is followed by `IF`. "Has not" or "is not" in the description becomes `NOT`, placed after the conditions that give the variables their values.
- For "state the result of the goal", give **every** answer in order on one line (`X = ama, yaw`), and write "false" (or "no result") when nothing matches.
- For low-level code, state the mode of each instruction you use if the question asks, and remember that `CMP` works on ACC.
:::

:::try Start easy, finish at exam standard
Q: Name the paradigm: a program is written as a list of facts such as `capital(peru, lima).` and rules, and the user types a goal.
A: Declarative programming.
Q: Give one advantage and one disadvantage of low-level programming.
A: Advantage: it can be fast and small, because the programmer controls every instruction and uses the hardware directly. Disadvantage: it is hard to write and read, and it only works on one type of processor.
Q: Memory locations 170 to 173 hold 172, 9, 14 and 30. IX holds 1. State the value loaded into ACC by `LDD 170`, `LDI 170` and `LDX 170`.
A: `LDD 170` loads 172. `LDI 170` reads 170, finds 172 and loads the contents of location 172: 14. `LDX 170` reads location \(170 + 1 = 171\) and loads 9.
Q: A `JMR #5` instruction (jump 5 locations forward of its own address) is stored at address 210. Which address does it jump to?
A: \(210 + 5 = 215\).
Q: Which of these is a variable and which is a constant: `Town`, `lima`?
A: `Town` is a variable (a capital letter), and `lima` is a constant (lower case).
Q: The facts are `stock(rice, 40).`, `stock(beans, 0).`, `stock(maize, 12).` and the rule is `in_stock(Item) IF stock(Item, Amount) AND Amount > 0.` State the results of the goal `in_stock(I)`.
A: Items are tried in the order of the facts. Rice has 40, beans has 0 (fails) and maize has 12. The results are I = rice and I = maize.
Q: Write one fact stating that Aisha is a teacher, and one fact stating that Aisha teaches the class 9c.
A: `teacher(aisha).` and `teaches(aisha, class_9c).`
:::

In the exam practice set below, some questions have a chapter link in brackets after the stars. That link is the chapter to revise: use it after you have tried the question, not before.

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the programming paradigm used by each piece of code. (a) `LDR #0` then `LDX ARRAY` then `INC IX` (b) `route(X, Y) IF flight(X, Y).` (c) A program that declares variables, uses `FOR` loops and `CALL`s procedures that change global variables.
A: One mark for each correct paradigm.

- (a) low-level programming [B1]
- (b) declarative programming [B1]
- (c) imperative (procedural) programming [B1]

Q: [4 marks] ★ (#cs.assembly) Locations 180 to 184 hold 183, 12, 35, 6 and 77. IX holds 1. State the contents of ACC after each instruction is carried out (each one starts from the same memory). (a) `LDM #180` (b) `LDD 180` (c) `LDI 180` (d) `LDX 180`
A: One mark for each correct value.

- (a) 180, because the operand is the value itself (immediate) [B1]
- (b) 183, because the contents of location 180 are loaded (direct) [B1]
- (c) 6: location 180 holds 183, and location 183 holds 6 (indirect) [B1]
- (d) 12: the address is \(180 + 1 = 181\), and location 181 holds 12 (indexed) [B1]

Q: [7 marks] ★★ A school in Lima records which teacher teaches which subject, and which class studies which subject. (a) Write facts to record that Rosa teaches maths, that Luis teaches science and that class 7a studies maths. (b) Write a rule `taught_by(Class, Teacher)` that is true when the class studies a subject that the teacher teaches. (c) The knowledge base also holds `teaches(rosa, physics).`, `studies(class_7a, science).` and `studies(class_8b, physics).` State all the results of the goal `taught_by(class_7a, T)`.
H: In (b), the subject is the link between the two facts: it is a variable in the body that does not appear in the head.
H: In (c), take the facts in the order of the list in (a) and then (c): the subjects class 7a studies are maths, then science.
A: One possible answer for (a) and (b):

```text
teaches(rosa, maths).
teaches(luis, science).
studies(class_7a, maths).
taught_by(Class, Teacher) IF studies(Class, Subject) AND teaches(Teacher, Subject).
```

- `teaches` fact for Rosa, and for Luis, with lower-case constants and a full stop [B1]
- `studies(class_7a, maths).` [B1]
- rule head `taught_by(Class, Teacher)` and `IF` [B1]
- body `studies(Class, Subject)` joined by `AND` to `teaches(Teacher, Subject)`, with the shared variable `Subject` [B1]
- (c) T = rosa (class 7a studies maths, which Rosa teaches) [B1]
- (c) T = luis (class 7a studies science, which Luis teaches) [B1]
- (c) no other answer: Rosa teaches physics, but class 7a does not study it [B1]

Q: [8 marks] ★★ A community garden club keeps these clauses in a knowledge base.

| Clause | Meaning |
|---|---|
| 1 `plant(tomato).` | Tomato is a plant |
| 2 `plant(basil).` | Basil is a plant |
| 3 `plant(mint).` | Mint is a plant |
| 4 `plant(carrot).` | Carrot is a plant |
| 5 `plot(north).` | North is a plot |
| 6 `plot(south).` | South is a plot |
| 7 `plot(east).` | East is a plot |
| 8 `unsuitable(tomato, north).` | Tomato does not grow well in the north plot |
| 9 `unsuitable(basil, north).` | Basil does not grow well in the north plot |
| 10 `unsuitable(basil, east).` | Basil does not grow well in the east plot |
| 11 `unsuitable(mint, south).` | Mint does not grow well in the south plot |
| 12 `unsuitable(carrot, east).` | Carrot does not grow well in the east plot |
| 13 `sown(tomato, south).` | Tomato has been sown in the south plot |
| 14 `sown(mint, east).` | Mint has been sown in the east plot |
| 15 `sown(carrot, north).` | Carrot has been sown in the north plot |

(a) Coriander is a plant, west is a plot, and coriander has been sown in the west plot. Write three clauses to record this. [3]

(b) Using the variable X, the goal `unsuitable(X, east)` returns X = basil, carrot. Write the result returned by the goal `unsuitable(basil, X)`. [1]

(c) A plant may be sown in a plot if it is a plant, the plot is a plot and the plant is not unsuitable for that plot. Complete the rule. [4]

`can_sow(Plant, Plot)`
`IF`
H: In (a), each clause ends with a full stop, uses a lower-case constant, and has its arguments in the same order as the table.
H: In (c), write one condition for each part of the sentence. The condition that tests for something that is not true must come last, after the conditions that choose Plant and Plot.
A: One possible answer for (a) and (c):

```text
plant(coriander).
plot(west).
sown(coriander, west).
can_sow(Plant, Plot) IF plant(Plant) AND plot(Plot) AND NOT unsuitable(Plant, Plot).
```

- (a) `plant(coriander).` [B1]
- (a) `plot(west).` [B1]
- (a) `sown(coriander, west).` with the plant first and the plot second [B1]
- (b) X = north, east (the order of clauses 9 and 10) [B1]
- (c) `plant(Plant)` and `plot(Plot)` as conditions, each joined by `AND` [B1]
- (c) `NOT unsuitable(Plant, Plot)` [B1]
- (c) the `NOT` condition last, using the same variables as the head [B1]
- (c) the head `can_sow(Plant, Plot)` followed by `IF` and the conditions joined by `AND` (the comma form is also accepted) [B1]

(Check with the rule: `can_sow(P, east)` gives P = tomato, mint, because basil and carrot are unsuitable for the east plot.)

Q: [6 marks] ★★ (#cs.assembly) Eight numbers are stored in consecutive locations starting at `LIST`. Write assembly language code, using indexed addressing, to count how many of the numbers equal 7, and store the count in a location named `FOUND`. The numbers are 7, 3, 7, 7, 1, 9, 7 and 2.
H: Use `LDX LIST`, then `CMP #7`. If the compare is FALSE, skip the instructions that add one to FOUND.
H: Loop eight times with a counter in memory, as in the worked example.
A: One possible answer:

```text
100  START:  LDR #0
101          LDM #0
102          STO FOUND
103  LOOP:   LDX LIST
104          CMP #7
105          JPN SKIP
106          LDD FOUND
107          INC ACC
108          STO FOUND
109  SKIP:   INC IX
110          LDD LEFT
111          SUB #1
112          STO LEFT
113          CMP #0
114          JPN LOOP
115          END
116  LIST:   7
117          3
118          7
119          7
120          1
121          9
122          7
123          2
124  FOUND:  0
125  LEFT:   8
```

- IX set to 0 with `LDR #0`, and FOUND set to 0 [B1]
- `LDX LIST` reads the current number inside a loop [B1]
- `CMP #7` and `JPN SKIP`, so the count is changed only when the number is 7 [B1]
- FOUND increased by one (`LDD`, `INC ACC`, `STO`) [B1]
- `INC IX` on every pass, with a counter of 8 reduced and compared with 0 and `JPN LOOP` [B1]
- `END`, and `LIST`, `FOUND` and `LEFT` defined (the program leaves 4 in FOUND) [B1]

Q: [3 marks] ★ Compare imperative programming and declarative programming.
A: One mark for each point, up to three.

- imperative: the programmer writes the steps that say how to solve the problem [B1]
- declarative: the programmer writes facts and rules that say what is true, and the system finds the answers [B1]
- imperative programs change variables as they run (state); declarative programs use no assignment and the order of the search is chosen by the system [B1]

Q: [4 marks] ★★ (#cs.assembly) A program is stored from address 200. The last instruction of a loop, at address 208, is `JMR #-4`, a relative jump that adds the offset to the address of the `JMR` instruction. (a) State the address that the instruction jumps to. (b) The operating system now loads the same program starting at address 300. State where the same instruction is stored and where it jumps to. (c) Explain why a program that uses relative addresses for its jumps can be moved in memory but one that uses `JMP 204` cannot.
A: One mark per point.

- (a) \(208 - 4 = 204\) [B1]
- (b) it is stored at 308 and jumps to \(308 - 4 = 304\) [B1]
- (c) the relative jump is calculated from the address of the instruction, so it always lands on the matching instruction after the move [B1]
- `JMP 204` always jumps to the fixed address 204, which is no longer part of the program after it moves [B1]

Q: [6 marks] ★★★ A travel company records flights between cities with their prices, and hotels in cities with their nightly prices.

```text
flight(lima, quito, 210).
flight(lima, bogota, 260).
flight(quito, bogota, 150).
flight(bogota, miami, 300).
hotel(quito, andes_inn, 60).
hotel(bogota, plaza_sol, 85).
hotel(miami, bay_view, 140).
via(A, C) IF flight(A, B, P1) AND flight(B, C, P2).
```

(a) State all the results of the goal `via(lima, X)`. (b) Write a rule `can_stay(Town)` that is true when a flight arrives in the town and the town has a hotel. (c) State all the results of the goal `can_stay(T)`, using your rule from (b).
H: In (b), a flight fact has three arguments: the city it leaves, the city it reaches and the price. Use one variable for the departure city and one for the price.
H: In (c), the system tries each flight in turn. Count a town once for every flight that reaches it.
A: One possible answer for (b):

```text
can_stay(Town) IF flight(From, Town, Cost) AND hotel(Town, Name, Rate).
```

- (a) X = bogota, from lima to quito to bogota [B1]
- (a) X = miami, from lima to bogota to miami [B1]
- (b) head `can_stay(Town)` and `IF` [B1]
- (b) body: `flight` with `Town` as the arrival city, joined by `AND` to `hotel` with the same `Town` [B1]
- (c) T = quito, then T = bogota, then T = bogota again, then T = miami: four answers in this order [B1]
- (c) bogota appears twice because two flights arrive there (from lima and from quito) [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A company records who reports to whom: `reports_to(dina, sam).`, `reports_to(sam, luca).`, `reports_to(luca, mei).` Write rules for `boss(X, Y)`, true when Y is the manager of X, or the manager of X's manager, and so on up the chain. Then state all the results of the goals `boss(dina, B)` and `boss(X, mei)`.
H: You need two rules: one for a direct manager, and one that goes up a step and then uses `boss` again.
H: For the second goal, the system tries the rules in order, and for each rule it takes the facts in order.
A: One possible answer:

```text
reports_to(dina, sam).
reports_to(sam, luca).
reports_to(luca, mei).
boss(X, Y) IF reports_to(X, Y).
boss(X, Y) IF reports_to(X, Z) AND boss(Z, Y).
```

- first rule for a direct manager: `boss(X, Y) IF reports_to(X, Y).` [B1]
- second rule that goes up one step and uses `boss` again: `reports_to(X, Z) AND boss(Z, Y)` [B1]
- `boss(dina, B)`: B = sam, B = luca, B = mei [B1]
- `boss(X, mei)`: the first rule gives X = luca [B1]
- `boss(X, mei)`: the second rule then gives X = dina and X = sam, so the results are luca, dina and sam in that order [B1]

Q: [5 marks] ★★★ Three numbers are held as a chain in memory. Each item uses two locations: the number, then the address of the next item. The address 0 means "no next item". The location `CUR` holds the address of the first item, 200. The chain is: location 200 holds 5 and 201 holds 210; location 210 holds 9 and 211 holds 230; location 230 holds 4 and 231 holds 0. Write assembly language code that follows the chain with indirect addressing and stores the total of the three numbers in `TOTAL`. State the total.
H: `LDI CUR` loads the number, because CUR holds the address of the current item.
H: The next address is stored one location after the number, so work out `CUR + 1` in the accumulator, store it in a temporary location, then use `LDI` on that location.
A: One possible answer:

```text
100  START:  LDM #0
101          STO TOTAL
102  LOOP:   LDI CUR
103          ADD TOTAL
104          STO TOTAL
105          LDD CUR
106          INC ACC
107          STO TEMP
108          LDI TEMP
109          STO CUR
110          CMP #0
111          JPN LOOP
112          END
113  CUR:    200
114  TEMP:   0
115  TOTAL:  0
200          5
201          210
210          9
211          230
230          4
231          0
```

- `TOTAL` set to 0 before the loop [B1]
- `LDI CUR` loads the number of the current item, which is added to the total [B1]
- the address of the next-item location (`CUR + 1`) is calculated and stored in `TEMP` [B1]
- `LDI TEMP` loads the next address, and it is stored in `CUR` [B1]
- the loop ends when the next address is 0 (`CMP #0` then `JPN LOOP`), and the total is \(5 + 9 + 4 = 18\) [B1]
:::

:::quiz
? Which statement describes a programming paradigm?
- A language's list of reserved words
+ A style of programming with its own way of expressing a solution
- The speed at which a program runs
- The type of processor that runs the code
> A paradigm is an approach such as imperative, object-oriented, low-level or declarative. A single language can support several paradigms.
? What does `LDI 160` do?
- Loads the number 160 into ACC
- Loads the contents of location 160 into ACC
+ Reads location 160, treats its contents as an address and loads the contents of that address
- Loads the contents of location \(160 + \text{IX}\)
> The first option is `LDM` (immediate), the second is `LDD` (direct) and the last is `LDX` (indexed). Indirect addressing follows an address held in memory.
? Which phrase correctly describes relative addressing?
- The operand is the data itself.
- The operand is added to the index register.
+ The address is given as an offset from the address of the current instruction.
- The address is stored in another location.
> Relative addressing lets a program be moved in memory, because jumps are counted from the instruction's own address. The other three describe immediate, indexed and indirect addressing.
? In a declarative program, which of these is a variable?
- `ama`
- `parent`
+ `Child`
- `parent(ama, kwame).`
> Variables start with a capital letter. `ama` is a constant, `parent` is a predicate name, and the last option is a whole fact.
? The facts are `likes(ana, tea).` and `likes(ben, tea).` What does the goal `likes(Who, tea)` give?
- Who = tea
+ Who = ana, then Who = ben
- true
- false
> The variable Who is matched with each fact in order. The first answer is ana, and after backtracking the second is ben. A goal that contains a variable gives values, not just true or false.
? Which is the main difference between imperative and declarative programming?
- Imperative programs cannot use variables.
+ An imperative program says how to solve the problem; a declarative program says what is true and lets the system find the answers.
- Declarative programs always run faster.
- Imperative programs cannot be split into procedures.
> Imperative programs are step-by-step instructions that change state. Declarative programs state facts and rules, and the system searches for answers.
? Why does the goal `sibling(ama, X)` give X = yaw twice when `sibling(X, Y) IF parent(P, X) AND parent(P, Y) AND X \= Y.` and Ama and Yaw have two parents in common?
- The rule is written wrongly.
- Yaw appears twice in the facts.
+ The goal is satisfied once through each shared parent.
- Backtracking repeats the last answer by mistake.
> The system reports every way of proving the goal. With P = kofi it finds yaw, and with P = abena it finds yaw again.
? The rule is `may_enrol(S, C) IF student(S) AND course(C) AND NOT completed(S, C).` and `completed(lina, baking).` is a fact. What does the goal `may_enrol(lina, baking)` give?
- true, because Lina is a student and baking is a course
+ false
- S = lina
- an error, because NOT cannot be used in a rule
> `completed(lina, baking)` can be proved, so `NOT completed(lina, baking)` is false and the rule fails. NOT is true only when its condition cannot be proved.
:::

:::checklist What you can now do
- [ ] I can explain what a programming paradigm is and compare low-level, imperative (procedural), object-oriented and declarative programming.
- [ ] I can describe the characteristics of the imperative paradigm (sequence, state, procedures and functions).
- [ ] I can explain the advantages and disadvantages of low-level programming.
- [ ] I can use immediate, direct, indirect, indexed and relative addressing, and say which location is read.
- [ ] I can write a low-level loop with indexed addressing and a counter, and trace one that uses indirect addressing.
- [ ] I can write facts and rules from a description, using lower-case constants, capitalised variables, full stops and `NOT` for "has not".
- [ ] I can state the results of a goal against a set of facts and rules, including all the answers in order.
- [ ] I can explain backtracking in words and say why a goal can give the same answer more than once.
- [ ] I can compare imperative and declarative programming and say when each is suitable.
:::

:::recap
- A **paradigm** is a style of programming: **low-level** (processor instructions), **imperative/procedural** (statements that change state, grouped in procedures and functions), **object-oriented** (objects with attributes and methods) and **declarative** (facts and rules and a goal).
- Low-level code is fast, small and close to the hardware, but long, hard to read and tied to one processor type.
- Addressing modes: immediate (the value), direct (the address), indirect (the address of the address), indexed (address plus IX), relative (offset from the instruction itself).
- `CMP` compares ACC only; a counted loop needs a count kept in memory, or a sentinel.
- Declarative code: **facts** end with a full stop, **rules** have a head, `IF` and a body joined by `AND`; constants are lower case and variables are capitalised. `NOT` makes a condition true when it cannot be proved; put it after the conditions that choose the values.
- A **goal** is satisfied by matching facts and rules from the top, in order; **backtracking** finds the other answers. Everything not provable is false.
- Imperative says **how**; declarative says **what** is true.
:::

:::links
- practise: [Programming paradigms: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/20-further-programming-/programming-paradigms/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- explore: [SWISH](https://swish.swi-prolog.org/) · SWI-Prolog · type the facts and rules of this chapter (with `:-` and commas) and run the goals
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists on how languages and machines work
- explore: [LMC simulator](https://www.101computing.net/lmc-simulator/) · 101 Computing · step through a small machine-code program
- read: [The 9618 syllabus](https://www.cambridgeinternational.org/Images/721397-2027-2029-syllabus.pdf) · Cambridge · the learning outcomes for programming paradigms

Links checked 13 November 2026.
:::

Next: [File processing and exception handling](#cs.fileproc)
