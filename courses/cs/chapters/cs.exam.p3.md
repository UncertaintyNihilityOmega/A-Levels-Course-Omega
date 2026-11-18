@chapter cs.exam.p3
@title Paper 3 guide: Advanced Theory
@level guide
@paper CAIE 9618 Paper 3
@time 2–3 hours
@summary What Paper 3 prints and allows, how to share 90 minutes across 75 marks, the technique for each kind of A Level question (floating point, Boolean algebra, grammars, scheduling, graph searches, encryption, ADT pseudocode, recursion, OOP, declarative and low-level code), eight model answers with mark points, the slips that cost marks, and a revision plan that links every Paper 3 chapter.

:::why
Paper 3 is the A Level theory paper: sections 13 to 20, written for students who already know the AS course. The questions are short, but they are dense: a floating-point conversion, a Boolean simplification or a pseudocode algorithm each needs a method that you have practised until it is automatic. This guide shows what the paper looks like, how to spend the 90 minutes, and the method that earns each mark.
:::

## The paper at a glance

| Feature | Paper 3 |
|---|---|
| Title | Advanced Theory |
| Time | 1 hour 30 minutes |
| Marks | 75 |
| Syllabus content | sections 13 to 20 (data representation, communication and internet technologies, hardware and virtual machines, system software, security, artificial intelligence, computational thinking and problem-solving, further programming) |
| Weighting | 25% of A Level |
| Where you answer | on the question paper itself; no additional materials |
| Questions | answer all of them: some short, some longer |

The front page of the May/June 2025 paper (9618/31) told candidates that **calculators must not be used**, and said under "Information" that the total is 75 marks, that the marks for each part are in brackets `[ ]`, and that **no marks will be awarded for using brand names of software packages or hardware**.

That paper had 16 pages and 12 questions of 4 to 9 marks. Its topics were floating point, the TCP/IP layers, a linked list, a truth table to simplify, interpreters, syntax diagrams, multi-tasking, SSL/TLS, graphs in artificial intelligence, a class to design and a pseudocode algorithm to complete. Treat that list as an example of the style, not as a rule: other papers have different questions, and the topics change from series to series. What stays the same is the style: a short scenario or a diagram, then parts (a), (b), (c) with the marks in brackets.

:::exam What the assessment objectives mean for you
Paper 3 is 60% AO1 (knowledge and understanding) and 40% AO2 (applying knowledge to a problem). The AO1 marks are the definitions, descriptions and conversions you have learned. The AO2 marks are the answers that need the scenario or the data in the question: "complete this trace", "justify a choice for this system". A student who learns only the facts keeps the 60% and loses most of the other 40%.
:::

There is no programming on a computer in this paper, but there is **writing code on paper**: pseudocode for linked lists, trees, recursion and classes. The pseudocode must follow the Cambridge guide, which is why [Programming from zero](#cs.f.basics) and [Paper 2 guide](#cs.exam.p2) matter for Paper 3 as well.

## Spending 90 minutes on 75 marks

Paper 3 has the same pace as Paper 1: \(90 \div 75 = 1.2\) minutes per mark. The questions are short, so the pace is easy to keep and easy to lose: one slow Boolean simplification can eat the time of two other questions.

| Marks | Minutes at 1.2 per mark | Round to |
|---|---|---|
| 4 | 4.8 | 5 |
| 6 | 7.2 | 7 |
| 7 | 8.4 | 8 |
| 9 | 10.8 | 11 |

On average a question of the May/June 2025 paper (75 marks over 12 questions) gets \(90 \div 12 = 7.5\) minutes. Plan to **finish with about ten minutes left**, and spend them on the parts of the paper that are easy to get wrong without noticing: arithmetic in a floating-point conversion, a missing row in a truth table, a pointer that is changed in the wrong order, a trace table row that is skipped.

:::steps
1. **First two minutes:** read the first line of every question and mark the ones that look quick. Start with the topic you know best.
2. **Write the method, not just the answer.** For every conversion, simplification and trace, show the working: a mark scheme gives a method mark for each step.
3. **Pseudocode last, within a time box.** A 6-mark algorithm can take 10 minutes if you start with a blank page. Plan it first (what must be initialised, what repeats, what is returned) and write it once.
4. **At ten minutes before the end,** stop starting new work. Check every calculation, every table and every pointer assignment.
:::

:::tip Marks are the clock
If a 4-mark question has taken eight minutes, stop. Write what you have, star the question and move on. A half-answer scores some marks; a blank scores none, and the questions you have not yet reached are worth more per minute.
:::

## What each section tends to ask

Cambridge sets original questions every series, so no one can say what will appear. What can be said is what **kinds of question** each section produces. Practise each kind until the method is automatic.

| Syllabus section | Chapter | Question types to practise |
|---|---|---|
| 13 Data representation | [User-defined types, file organisation and hashing](#cs.usertypes), [Floating-point numbers](#cs.float) | write the declaration of an enumerated type, a pointer, a record or a set; serial, sequential and random files; a hashing calculation with a collision; floating point to denary and back, normalising, range against precision, rounding, overflow and underflow |
| 14 Communication | [Protocols, TCP/IP and packet switching](#cs.networks2) | what each of the four TCP/IP layers does as a message is sent; which protocol does which job; how packets cross a network; benefits and drawbacks of circuit and packet switching |
| 15 Hardware | [Processors, parallel processing and virtual machines](#cs.hardware2), [Boolean algebra, Karnaugh maps, adders and flip-flops](#cs.boolean) | RISC against CISC; a pipeline timing diagram; SISD, SIMD, MISD, MIMD; virtual machines; a truth table to an expression; simplifying with laws or with a Karnaugh map; half and full adders; SR and JK flip-flops |
| 16 System software | [Operating systems: processes, scheduling and memory](#cs.os), [Compilers, BNF and Reverse Polish notation](#cs.translators) | process states and the transitions between them; round robin, SJF, FCFS and SRT traces; paging, segmentation and virtual memory; how an interpreter and a compiler work; BNF and syntax diagrams; infix to RPN and RPN with a stack |
| 17 Security | [Encryption, SSL/TLS and digital certificates](#cs.security2) | symmetric and asymmetric encryption with the right key at each step; digital signatures; certificates; SSL/TLS; quantum cryptography |
| 18 Artificial intelligence | [Graphs and pathfinding: Dijkstra and A*](#cs.ai), [Machine learning and neural networks](#cs.ml) | a Dijkstra or A* table; why a graph is used; supervised, unsupervised and reinforcement learning; back propagation; regression |
| 19 Computational thinking | [Searching, sorting and Big O](#cs.algorithms2), [Abstract data types](#cs.adts), [Recursion](#cs.recursion) | binary search and insertion sort traces; Big O; stacks, queues, linked lists, trees and graphs as ADTs; pseudocode to find, insert or delete; a recursive function traced and written |
| 20 Further programming | [Object-oriented programming](#cs.oop), [Programming paradigms](#cs.paradigms), [File processing and exception handling](#cs.fileproc) | design a class with `INHERITS` and `SUPER`; facts, rules and goals in a declarative language; addressing modes in a low-level trace; random file operations; exception handling |

Notice how many of these ask you to **do** something: convert, simplify, trace, complete, write. The next sections give the method for each.

## Command words at A Level

The command words are the same as in Paper 1 and are listed in [Paper 1 guide: Theory Fundamentals](#cs.exam.p1): *state*, *describe*, *explain*, *justify*, *complete*, *calculate*, *define*. Three more matter a great deal in Paper 3.

| Command word | Cambridge meaning | What the answer contains |
|---|---|---|
| **Complete** | add to a diagram or table | every blank filled, in the layout given: a trace table, a K-map, a Dijkstra table, a missing line of pseudocode |
| **Write** | write an answer in a specific way | the answer in the form named: pseudocode, a BNF rule, a logic expression, a declarative rule. The form is part of the mark |
| **Identify** | name, select or recognise | the one name asked for, with no explanation |

:::warn "Write" means the form matters
"Write a Boolean expression" is not answered by a sentence, and "write pseudocode" is not answered by Python. A correct idea in the wrong form scores little or nothing. For code, use the Cambridge pseudocode keywords exactly as the question and the Pseudocode Guide show them.
:::

## The method for each kind of question

Each method below is short on purpose: it is the checklist to run in your head, so that you do not work out the method again in the exam.

### Floating point

Always begin by reading how many bits the mantissa and the exponent have. The mantissa is a two's complement fraction with the binary point **after the sign bit**; the exponent is a two's complement integer. For the other direction the steps are the same, reversed.

:::steps
1. **To denary:** read the exponent first (negative sign bit!); move the point of the mantissa that many places (right for a positive exponent, left for a negative one); then read the place values. Check with mantissa × \(2^{\text{exponent}}\).
2. **From denary, positive number:** write the number in binary, write it as \(0.1\ldots\) times a power of 2 (count how far the point moves), put the mantissa digits in the bits, put the count in the exponent.
3. **From denary, negative number:** do the positive number first, then take the two's complement of the mantissa (invert, add 1). Then check that the mantissa starts with 10.
4. **Normalised** means the first two bits of the mantissa differ. If they are the same, shift the mantissa left and subtract 1 from the exponent for each shift.
:::

### Boolean algebra and Karnaugh maps

:::steps
1. **From a truth table:** a K-map is quicker than algebra for three or four variables. Draw the grid with the headings in Gray code order (00, 01, 11, 10), put a 1 in every cell where the output is 1, and group the 1s in rectangles of 1, 2, 4 or 8, as large as possible, wrapping round the edges.
2. **From an expression:** use laws, and **name the law on every line** (De Morgan, distributive, absorption, identity, complement). Every line should be one law applied to one place, so that the examiner can follow it.
3. **Check** by testing one row of the truth table in the original and the simplified expressions.
:::

### Grammar: BNF, syntax diagrams and Reverse Polish notation

:::steps
1. **BNF:** one rule per `<name>`, written `<name> ::= …`; alternatives separated by `|`; **repetition is recursion**, so a rule that allows one or more digits refers to itself: `<number> ::= <digit> | <digit><number>`.
2. **Syntax diagram:** a rectangle for something defined elsewhere, a rounded box for a literal symbol, and a loop-back line for repetition. Follow the arrows to test a string.
3. **Infix to RPN:** bracket each operator and its two operands in order of precedence, move each operator to its closing bracket, delete the brackets.
4. **Evaluating RPN:** read left to right; a number is **pushed**; an operator **pops two** values (the first popped is the right-hand operand), applies the operator and **pushes the result**. At the end one value is left.
:::

### Processes and scheduling

Draw the three states, **ready**, **running** and **blocked**, and learn the transitions with their causes: ready to running (the scheduler chooses it), running to ready (its time slice ends, or a higher-priority process arrives), running to blocked (it waits for an input or output event), blocked to ready (the event happens). A blocked process never goes straight to running.

For a scheduling trace, draw a **Gantt chart** first (a row of boxes with the time at each edge), then work out completion, turnaround (completion − arrival) and waiting (turnaround − burst) from it. Write the tie rule the question gives next to the chart.

### Graph searches

A Dijkstra table has one column per vertex and one row per step; each cell holds a distance and the previous vertex, and a vertex is visited in order of smallest distance. For A*, add the heuristic: the vertex chosen each time is the one with the smallest \(f = g + h\), where \(g\) is the cost from the start so far and \(h\) is the estimated cost to the goal. In both, the path is read **backwards** along the previous vertices, and the algorithm stops when the **destination is chosen**, not when it first gets a value.

### Encryption in sequence

Write the steps in the order they happen, and **name the key at every step**: "encrypts with the receiver's **public** key", "decrypts with her **private** key", "signs the digest with the sender's **private** key", "checks with the sender's **public** key". Say "digest" or "hash" where a signature is involved. A certificate holds a **public** key and is signed by the **certificate authority**.

### ADT pseudocode

For a linked list in arrays (`Data`, `Pointer`, `StartPointer`, `FreePointer`) the marks are almost always for the **same few things**: a check for the special case (empty list, full list, first node), a loop that follows the pointers and stops at 0, the pointer changes **in the right order**, the free list updated, and the return value. Draw the arrays on the question paper, run your pseudocode on them by hand, and only then trust it.

### Recursion

Say what the **base case** is (the call that does not call itself), show that each call moves **towards** it, and trace by writing each call on its own line as you go down, then the returned values as you come back up. A trace table for recursion has a column for the call, one for the parameter and one for the value returned.

### Object-oriented pseudocode

Learn the shape: `CLASS Name` … `ENDCLASS`; `PRIVATE` attributes; `PUBLIC PROCEDURE NEW(…)` as the constructor; getters and setters as `PUBLIC FUNCTION` and `PUBLIC PROCEDURE`; `CLASS Child INHERITS Parent`; `SUPER.NEW(…)` inside the child's constructor; and `Object ← NEW Child(…)` to create an instance. Every mark is a feature of this shape.

### Declarative and low-level code

A declarative **fact** is `predicate(constant, constant).`; a **rule** has a head, the word `IF` and a body joined by `AND`; constants start with a lower-case letter and variables with a capital letter; every clause ends with a full stop. A goal with a variable has several answers, **in the order of the facts**. For low-level code, the paper prints the instruction set it uses, so trace the program row by row, and for indexed addressing remember that the address used is the operand **plus the contents of IX**.

## Model answers

The answers below show what a full-mark answer looks like for eight styles of question that carry many marks in Paper 3. Each one explains its method before the mark points. The questions are original, in the style of the paper.

:::eg Floating point: from denary, with an explanation
A weather station in Nairobi stores each temperature as a normalised floating-point number. The mantissa has 8 bits and the exponent has 4 bits, both in two's complement.

(a) Show how \(-3.75\) is stored. [4]

(b) The station also stores the value 0.3. Explain why the value stored is not exactly 0.3. [2]

(c) State how you can tell from the bits of the mantissa, without converting, that your answer to (a) is normalised. [1]

Method: do the positive number first, then make it negative.

(a) \(3.75\) is \(11.11_2\), because \(2 + 1 + \tfrac12 + \tfrac14 = 3.75\). [B1]

Written as \(0.1111 \times 2^{2}\): the point moves two places, so the exponent is \(2 = 0010\) and the positive mantissa is 0.1111000, that is 01111000. [B1]

To make the mantissa negative, invert 01111000 to give 10000111 and add 1 to give 10001000. [B1]

The stored number is mantissa 10001000, exponent 0010. [B1]

Check: \(1.0001000_2 = -1 + \tfrac1{16} = -0.9375\), and \(-0.9375 \times 4 = -3.75\).

(b) 0.3 is \(0.0100110011\ldots_2\), a binary fraction that never ends (it repeats). [B1]

The mantissa has only 7 digits after the binary point, so the later digits are dropped (or rounded) and the stored value is slightly different, for example 0.296875 when the extra digits are dropped. [B1]

(c) The first two bits of the mantissa are different (1 then 0). [B1]
:::

:::eg Karnaugh map: four variables, with wrap-around
A security light has four sensors A, B, C and D. The light output Z is 1 when the inputs ABCD are 0000, 0001, 0010, 0101, 1000, 1001 and 1010, and 0 for every other combination.

Complete the Karnaugh map, loop the groups, and write the simplified expression for Z. [5]

Method: the headings are in Gray code order (00, 01, 11, 10), so that neighbouring cells differ in one input. Write a 1 in each cell whose input pattern gives Z = 1.

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 1 | 1 | 0 | 1 |
| 01 | 0 | 1 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 |
| 10 | 1 | 1 | 0 | 1 |

The map is filled correctly (seven 1s and nine 0s). [B1]

Group 1: the **four corners** (0000, 0010, 1000, 1010). The left and right edges touch and the top and bottom edges touch, so these four cells are neighbours. B and D are 0 in all four, giving \(\text{NOT } B \cdot \text{NOT } D\). [B1]

Group 2: the **first two columns of the top row and of the bottom row** (0000, 0001, 1000, 1001), joined by wrapping from the top edge to the bottom edge. B and C are 0 in all four, giving \(\text{NOT } B \cdot \text{NOT } C\). [B1]

Group 3: the pair 0001 and 0101 (A, C and D unchanged, B changes). A is 0, C is 0 and D is 1, giving \(\text{NOT } A \cdot \text{NOT } C \cdot D\). [B1]

\[ Z = \text{NOT } B \cdot \text{NOT } D + \text{NOT } B \cdot \text{NOT } C + \text{NOT } A \cdot \text{NOT } C \cdot D \]

The three terms are joined with OR. [B1]

Each group is needed: 0010 and 1010 are only in group 1, 1001 is only in group 2, and 0101 is only in group 3.
:::

:::eg Dijkstra's algorithm on a delivery network
A courier company has six depots, S, A, B, C, D and T. The roads between them and their lengths in kilometres are: S–A 4, S–B 2, A–B 1, A–C 5, B–C 8, B–D 10, C–D 2, C–T 6, D–T 3.

Use Dijkstra's algorithm to find the shortest route from S to T and its length. If two vertices have the same distance, take the one earlier in the alphabet. [6]

Method: one row for each vertex visited, in order of smallest distance. A cell such as `3 B` means distance 3 with previous vertex B. A blank cell means no change.

| Step | Visit | S | A | B | C | D | T |
|---|---|---|---|---|---|---|---|
| 0 |  | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | S |  | 4 S | 2 S |  |  |  |
| 2 | B |  | 3 B |  | 10 B | 12 B |  |
| 3 | A |  |  |  | 8 A |  |  |
| 4 | C |  |  |  |  | 10 C | 14 C |
| 5 | D |  |  |  |  |  | 13 D |
| 6 | T |  |  |  |  |  |  |

- Step 1: S is visited. A becomes 4 and B becomes 2, both with previous vertex S. [B1]
- Step 2: B (2) is the smallest, so B is visited. A would be \(2 + 1 = 3\), smaller than 4, so A changes to 3 with previous vertex B. C becomes 10 and D becomes 12. [B1]
- Step 3: A (3) is visited. C would be \(3 + 5 = 8\), smaller than 10, so C changes to 8 via A. [B1]
- Step 4: C (8) is visited. D would be \(8 + 2 = 10\), smaller than 12, so D changes to 10 via C. T becomes \(8 + 6 = 14\). [B1]
- Step 5: D (10) is visited. T would be \(10 + 3 = 13\), smaller than 14, so T changes to 13 via D. [B1]
- Step 6: T (13) is now the smallest unvisited vertex, so the algorithm stops. Reading the previous vertices backwards, T ← D ← C ← A ← B ← S, so the shortest route is S, B, A, C, D, T and its length is \(2 + 1 + 5 + 2 + 3 = 13\) km. [B1]

A common slip is to stop at step 4, when T first gets a value (14): it is not final until T is chosen.
:::

:::eg ADT pseudocode: delete from a linked list
A linked list is stored in two arrays. `Data[1:6]` holds integers and `Pointer[1:6]` holds the number of the next node, with 0 meaning no node. `StartPointer` is the first node of the list and `FreePointer` is the first node of the free list. The list is in ascending order. The current contents are:

| Node | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Data | 30 | 10 | 50 | 20 | 40 | |
| Pointer | 5 | 4 | 0 | 1 | 3 | 0 |

`StartPointer` is 2 and `FreePointer` is 6.

Write pseudocode for a function `DeleteItem(Target : INTEGER) RETURNS BOOLEAN` that removes the node holding `Target` from the list, returns the node to the free list and returns TRUE, or returns FALSE if `Target` is not in the list. [6]

Method: follow the pointers from the start, keeping the **previous** node as well as the current one, so that the previous node can be made to skip the deleted node. Then put the deleted node at the front of the free list.

```pseudocode
FUNCTION DeleteItem(Target : INTEGER) RETURNS BOOLEAN
   DECLARE Previous, Current : INTEGER
   Previous ← 0
   Current ← StartPointer
   WHILE Current <> 0 AND Data[Current] <> Target
      Previous ← Current
      Current ← Pointer[Current]
   ENDWHILE
   IF Current = 0 THEN
      RETURN FALSE
   ENDIF
   IF Previous = 0 THEN
      StartPointer ← Pointer[Current]
   ELSE
      Pointer[Previous] ← Pointer[Current]
   ENDIF
   Pointer[Current] ← FreePointer
   FreePointer ← Current
   RETURN TRUE
ENDFUNCTION
```

- variables `Previous` and `Current` set to 0 and `StartPointer` before the loop [B1]
- loop that follows the pointers and stops at the end of the list (0) or when the item is found, keeping `Previous` one node behind [B1]
- returns FALSE if the item is not found (`Current = 0`) [B1]
- first node deleted: `StartPointer` set to the next node [B1]
- other node deleted: the previous node's pointer set to `Pointer[Current]` [B1]
- deleted node added to the front of the free list (`Pointer[Current] ← FreePointer`, then `FreePointer ← Current`, in that order) and TRUE returned [B1]

(The guard `Current <> 0` comes first in the loop condition so that `Data[0]` is never read. Accept a version using a `REPEAT` loop if it gives the same result.)

After `DeleteItem(30)`: node 1 is the current node and node 4 the previous node. `Pointer[4]` becomes 5, `Pointer[1]` becomes 6 and `FreePointer` becomes 1. The list is now 10, 20, 40, 50 and node 1 is the first free node, followed by node 6.
:::

:::eg Reverse Polish notation: convert and evaluate
(a) Write the expression `(P + Q) * R - S / T` in Reverse Polish notation. [2]

(b) The Reverse Polish expression `9 3 / 4 2 + * 5 -` is evaluated using a stack. Show the contents of the stack after each token is processed, and state the result. [4]

(a) Multiplication and division come before subtraction, so bracket: `(((P + Q) * R) - (S / T))`. Move each operator to its closing bracket and delete the brackets: `P Q + R * S T / -`.

- `P Q + R *` (the sum, then the multiplication) [B1]
- `S T /` and the final `-` after both parts [B1]

(b) A number is pushed. An operator pops the top two values: the first one popped is the **right-hand** operand, the second the left-hand one. The result is pushed.

| Token | Action | Stack, bottom to top |
|---|---|---|
| 9 | push | 9 |
| 3 | push | 9, 3 |
| / | \(9 \div 3 = 3\) | 3 |
| 4 | push | 3, 4 |
| 2 | push | 3, 4, 2 |
| + | \(4 + 2 = 6\) | 3, 6 |
| * | \(3 \times 6 = 18\) | 18 |
| 5 | push | 18, 5 |
| - | \(18 - 5 = 13\) | 13 |

- 9 and 3 divided to give 3 [B1]
- 4 and 2 added to give 6, with 3 still on the stack [B1]
- 3 and 6 multiplied to give 18 [B1]
- 5 subtracted from 18, giving the result 13 [B1]
:::

:::eg Encryption in sequence: a private, verified message
Anil in Chennai sends a contract to Beth in Cardiff. Only Beth must be able to read it, and Beth must be able to check that it came from Anil and was not changed on the way. Describe how this is done, using public and private keys. [6]

Method: there are two jobs, and each uses a different pair of keys. **Privacy** uses the receiver's keys. **Proof of the sender** uses the sender's keys. Put the steps in time order.

- Anil applies a hash function to the contract to produce a digest. [B1]
- Anil encrypts the digest with his **private** key, giving the digital signature. [B1]
- Anil encrypts the contract (and the signature) with Beth's **public** key, so that only Beth can read it. [B1]
- The cipher text is sent; anyone who intercepts it cannot read it because they do not have Beth's private key. [B1]
- Beth decrypts the cipher text with her own **private** key, to get the contract and the signature. [B1]
- Beth decrypts the signature with Anil's **public** key to get the digest, hashes the contract herself, and compares the two digests: if they are the same, the contract came from Anil and is unchanged. [B1]

(Accept a version in which a symmetric session key is encrypted with Beth's public key and the contract is encrypted with that key. Reject "encrypted with a key" with no key named.)
:::

:::eg Object-oriented pseudocode: a class and a subclass
A bus company in Lima records each vehicle's registration (a string) and its number of seats (an integer). A minibus is a kind of vehicle and also records whether it has a wheelchair ramp (a Boolean).

Write pseudocode to define a class `Vehicle` with a constructor and a getter for the number of seats, a class `Minibus` that inherits from `Vehicle`, and a statement that creates a minibus with registration "LMA-452", 16 seats and a ramp. [7]

```pseudocode
CLASS Vehicle
   PRIVATE Registration : STRING
   PRIVATE Seats : INTEGER

   PUBLIC PROCEDURE NEW(GivenRegistration : STRING, GivenSeats : INTEGER)
      Registration ← GivenRegistration
      Seats ← GivenSeats
   ENDPROCEDURE

   PUBLIC FUNCTION GetSeats() RETURNS INTEGER
      RETURN Seats
   ENDFUNCTION
ENDCLASS

CLASS Minibus INHERITS Vehicle
   PRIVATE HasRamp : BOOLEAN

   PUBLIC PROCEDURE NEW(GivenRegistration : STRING, GivenSeats : INTEGER, GivenRamp : BOOLEAN)
      SUPER.NEW(GivenRegistration, GivenSeats)
      HasRamp ← GivenRamp
   ENDPROCEDURE
ENDCLASS

Bus1 ← NEW Minibus("LMA-452", 16, TRUE)
```

- `CLASS Vehicle` … `ENDCLASS` with the two attributes declared `PRIVATE` with the correct types [B1]
- constructor `NEW` with parameters that sets both attributes [B1]
- `GetSeats` declared as a `FUNCTION` that returns an `INTEGER` and returns `Seats` [B1]
- `CLASS Minibus INHERITS Vehicle` with `ENDCLASS` [B1]
- the extra attribute `HasRamp` declared as a `PRIVATE BOOLEAN` [B1]
- the subclass constructor calls `SUPER.NEW` with the registration and seats, then sets `HasRamp` [B1]
- the object created with `NEW Minibus(…)` and the three values in the right order, assigned to a variable [B1]

(Accept any identifier names that are meaningful. The attributes are private, so `Minibus` cannot use `Seats` directly: that is why it must call `SUPER.NEW`.)
:::

:::eg Declarative programming: a rule and its goal
A school stores facts about which teacher teaches which subject and where each subject is taught.

```text
teaches(ortiz, maths).
teaches(khan, physics).
teaches(ortiz, computing).
room(maths, r12).
room(physics, r5).
room(computing, r7).
```

(a) Write a rule `works_in(Teacher, Room)` that is true when the teacher teaches a subject that is taught in that room. [3]

(b) State every result of the goal `works_in(ortiz, R)`, in the order the system gives them. [2]

(a)

```text
works_in(Teacher, Room) IF teaches(Teacher, Subject) AND room(Subject, Room).
```

- head `works_in(Teacher, Room)` followed by `IF` [B1]
- both conditions `teaches(Teacher, Subject)` and `room(Subject, Room)` joined with `AND` [B1]
- the same variable `Subject` in both conditions, so they refer to the same subject (and a full stop at the end) [B1]

(b) The system looks for a subject taught by `ortiz`, in the order of the facts, and then for the room of that subject. The first subject is `maths`, in `r12`; the second is `computing`, in `r7`.

- `R = r12` [B1]
- `R = r7` [B1]
:::

## Writing pseudocode for Paper 3

A Paper 3 algorithm is worth 4 to 9 marks, and the marks are for **features**, as the linked-list answer above shows. The same features appear in most algorithms.

:::key What the marks are for in a pseudocode answer
- **The header:** the name, parameters and `RETURNS` type exactly as the question gives them.
- **Initialisation:** every variable that the loop reads is set before it, including pointers, counters and totals.
- **The loop:** the right kind (`WHILE` when it may run zero times, `FOR` when the count is known), and a condition that stops it. If the condition tests an array element and an index, test the index first.
- **The special cases:** an empty structure, a full structure, the first node, the item that is not there.
- **The update:** every pointer or index changes in the right order. Draw it on the paper if you are unsure.
- **The result:** a `RETURN` of the right type, or an `OUTPUT`.
:::

Use the identifiers that the question gives, even if you would have chosen better ones, and add a `//` comment only where it helps you check your own work. Indent by three spaces and close every structure (`ENDIF`, `ENDWHILE`, `ENDFUNCTION`). Do not write Python: `elif`, `==` and `print` score no marks.

## Common ways to lose marks

| Topic | The slip | The fix |
|---|---|---|
| Floating point | reading the mantissa as a whole number, or forgetting the sign bit is negative | the point is after the sign bit; the first place value is \(-1\) |
| Floating point | a negative number whose mantissa starts 11 or 00 is called normalised | normalised means the first two bits **differ** |
| Floating point | rounding error said to be "a mistake in the program" | it happens because the mantissa has a fixed number of bits |
| Hashing | forgetting to wrap round to the first slot when probing | the file is a circle: after the last address comes the first |
| Protocols | naming the layer that sends, not the layer that does the job | learn one job per layer: application, transport (TCP, ports), internet (IP addresses), link (frames) |
| Packet switching | saying packets "take the same route" | each packet may take a different route and is reassembled at the destination |
| Boolean algebra | a line with two laws applied at once | one law per line, and name it |
| K-map | a group of 3 or a group with a 0 in it | groups are 1, 2, 4, 8 or 16 cells, all 1s |
| K-map | headings in binary order (00, 01, 10, 11) | Gray code: 00, 01, 11, 10 |
| Scheduling | a blocked process shown going straight to running | blocked goes to ready, and the scheduler chooses from ready |
| Scheduling | waiting time = completion time | waiting = turnaround − burst, turnaround = completion − arrival |
| RPN | the left and right operands of `-` and `/` swapped | the first value popped is the **right** operand |
| BNF | repetition drawn with dots or a loop | write a recursive rule that refers to itself |
| Encryption | "encrypt with a key" or the keys the wrong way round | name the key and say whose it is |
| Certificates | a private key inside the certificate | a certificate holds the owner's **public** key and the CA's signature |
| Dijkstra | stopping when the destination first gets a distance | stop when it is **chosen** as the smallest unvisited vertex |
| Linked list | changing the pointers in the wrong order, so the rest of the list is lost | point the new or deleted node's neighbours **before** you overwrite the pointer |
| Linked list | forgetting the free list | a deleted node goes back to the free list; an inserted node comes from it |
| Recursion | no base case, or a call that does not move towards it | write the base case first and check that the parameter changes |
| OOP | a subclass that uses a private attribute of its parent directly | call the parent's constructor with `SUPER.NEW` and use its methods |
| Declarative | a capital letter on a constant or a lower-case letter on a variable | variables start with a capital letter; constants with a lower-case letter |
| Any | a brand name or a non-Cambridge pseudocode style | say "a router", "a compiler"; use `←`, `ENDIF`, `OUTPUT` |

## Technique check

Try these quick items before the longer practice in [Mixed practice: A Level (Papers 3 and 4)](#cs.mixed.a2).

:::try Technique check
Q: A Paper 3 question is worth 7 marks. About how long should it take, at the pace of this guide?
A: \(7 \times 1.2 = 8.4\) minutes, so about 8 minutes.

Q: A floating-point number has an 8-bit mantissa and a 4-bit exponent. Convert mantissa 10100000, exponent 0010 to denary.
A: The exponent 0010 is 2. The mantissa is \(1.0100000_2 = -1 + \tfrac14 = -0.75\). Moving the point two places right gives \(101.00000_2 = -4 + 1 = -3\). Check: \(-0.75 \times 4 = -3\).

Q: The pattern 00110100 0100 has an 8-bit mantissa and a 4-bit exponent. Is it normalised? If not, normalise it.
A: The first two bits of the mantissa are 00, so it is not normalised. Shift the mantissa left once, 01101000, and subtract 1 from the exponent, 0011. Both patterns have the value 6.5.

Q: Write the infix expression for the Reverse Polish expression `A B + C *`.
A: `(A + B) * C`. The addition is done first because its operator comes first, so it needs brackets in infix.

Q: A process is running and it asks to read a file. Which state does it enter, and which state does it enter when the read finishes?
A: Blocked, because it is waiting for an event. When the read finishes it goes to ready, not to running: the scheduler chooses it later.

Q: Improve this answer to "Explain why a certificate is used with a public key. [2]": "It makes it secure."
A: "Secure" is vague and gives no reason. A full answer: the certificate is signed by a certificate authority, which confirms that the public key belongs to the named owner; so the sender knows that the key really belongs to the receiver and not to someone pretending to be them.
:::

## Revision plan

Work through the paper in four stages. Spend the most time where you lose most marks, not where you feel comfortable.

:::steps
1. **Learn:** work through each chapter in the table above and tick its checklist. Every `:::def` card is exam wording: learn it.
2. **Practise by topic:** do the exam practice at the end of each chapter, then the topic questions linked there.
3. **Mix topics:** the real paper mixes sections 13 to 20. Do the "Paper 3 style" set in [Mixed practice: A Level (Papers 3 and 4)](#cs.mixed.a2) in a random order.
4. **Time yourself:** do [Mock Paper 3](#cs.mock.p3) in 90 minutes, then past papers (below), then mark them against the mark scheme.
:::

The tracker below counts the checklist items you have ticked in every Paper 3 chapter.

:::progress P3
:::

## Past papers and self-marking

Real Paper 3 question papers and mark schemes are free to download. Do them under timed conditions, with a pen, and without a calculator.

- [PapaCambridge](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) keeps 9618 papers, mark schemes and inserts together (an unofficial site).
- [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-3/) sorts Paper 3 papers by series (an unofficial site).
- The [Cambridge 9618 page](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/) has the syllabus and specimen papers.

:::steps
1. **Mark with a different colour pen,** using the mark scheme, one mark point at a time. Do not mark generously.
2. **Copy the wording.** A mark scheme shows the accepted answer and often words to reject. Write down the precise term it uses, and use it in your next answer.
3. **Sort every lost mark** into one of three kinds: *knowledge* (you did not know it), *technique* (you knew it but wrote it vaguely, or used the wrong form) or *slip* (arithmetic, a missing row, a pointer in the wrong order).
4. **Fix each kind differently:** revise the chapter, redo the question with a model answer in mind, or add a checking step to your routine.
5. **Redo the question a week later** without the mark scheme. If you lose the same mark twice, write that point on a revision card.
:::

:::warn Do not learn old answers as scripts
Cambridge writes new questions every series. A mark scheme is useful because it shows how marks are awarded, not because the same question returns. Use past questions to practise the method.
:::

:::recap
- Paper 3: 1 hour 30 minutes, 75 marks, sections 13 to 20, answered on the paper, no calculator, no marks for brand names. The May/June 2025 paper had 12 questions of 4 to 9 marks.
- Pace: \(90 \div 75 = 1.2\) minutes per mark. Finish with about ten minutes left to check calculations, tables and pointers.
- 60% of the marks are knowledge (AO1) and 40% application (AO2): use the data and the scenario in the question.
- *Complete* means fill every blank; *write* means the answer in the form named, and for code that is Cambridge pseudocode.
- Floating point: the point is after the sign bit; a normalised mantissa starts 01 or 10; to make a number negative, take the two's complement of the mantissa.
- Boolean algebra: name one law per line. K-map: Gray code headings, groups of 1, 2, 4, 8 or 16 ones, wrap-around allowed, fewest and largest groups.
- Dijkstra and A*: visit the smallest value, update neighbours, stop when the destination is chosen, read the path backwards.
- Encryption: name the key and whose it is at every step; a signature is a digest encrypted with the sender's private key.
- Pseudocode marks are for features: header, initialisation, loop, special cases, update in the right order, return.
- Self-mark past papers with a mark scheme, and sort every lost mark as knowledge, technique or slip.
:::

:::links
- papers: [9618 past papers, mark schemes and inserts](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · every series in one place [unofficial]
- papers: [Paper 3 past papers by series](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-3/) · Physics & Maths Tutor · Paper 3 only [unofficial]
- practise: [Floating-point numbers: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/13-data-representation-/floating-point-numbers-representation-and-manipulation/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Boolean algebra and logic circuits: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/15-hardware-and-virtual-machines-/boolean-algebra-and-logic-circuits/exam-questions/) · Save My Exams · K-map and law questions [paid]
- practise: [Algorithms: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/19-computational-thinking-and-problem-solving-/algorithms/exam-questions/) · Save My Exams · searching, sorting and ADT questions [paid]
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · a second explanation of every topic [paid]
- read: [The 9618 syllabus](https://www.cambridgeinternational.org/Images/721397-2027-2029-syllabus.pdf) · Cambridge · the command words and every learning outcome

Links checked 13 November 2026.
:::

Next: [Paper 4 guide: the Practical](#cs.exam.p4)
