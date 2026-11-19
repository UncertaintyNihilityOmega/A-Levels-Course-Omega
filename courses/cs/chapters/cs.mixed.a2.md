@chapter cs.mixed.a2
@title Mixed practice: A Level (Papers 3 and 4)
@level guide
@paper CAIE 9618 Papers 3 and 4
@time 8–10 hours
@summary Eighteen Paper 3 style questions across sections 13 to 20 in mixed order, with mark points and revise links, and five Paper 4 style programming tasks with data, expected output, a full Python model solution that runs and mark points, plus a quiz on the misconceptions that cost A Level students marks.

:::why
In a real exam the topics do not arrive in chapter order. A floating-point conversion can sit next to a question on encryption, and a Paper 4 task can ask for a linked list, a text file and an exception handler in the same program. Practising one chapter at a time hides whether you can recognise what a question is asking and which method it needs. This chapter mixes everything, so you practise the skill the exams test: choosing the right idea quickly, then carrying it out without a slip.
:::

## How to use this chapter

Before you start, read [Paper 3 guide: Advanced Theory](#cs.exam.p3) and [Paper 4 guide: the Practical](#cs.exam.p4). Every question carries a **revise link**: use it after you have tried the question, not before.

:::steps
1. **Choose a set** and a block of time. The Paper 3 style set is worth 121 marks, which is \(121 \times 1.2 = 145.2\) minutes, about 145, at the Paper 3 pace of 1.2 minutes a mark. That is more than one paper, so do it in two sittings of nine questions. The Paper 4 style set is worth 52 marks, which is \(52 \times 2 = 104\) minutes at the Paper 4 rate of 2 minutes a mark. Do not do both sets in one day.
2. **Write the Paper 3 answers by hand,** on paper, before you open any answer. Write pseudocode in the Cambridge style and nothing else.
3. **Do the Paper 4 tasks at a computer** in plain Python, with no help. Save each program, run it, and compare your output with the expected output before you open the answer.
4. **Open one answer at a time.** Mark each mark point, in a different colour, and write the total beside the question.
5. **Record the section** of every question you lost marks on, use its revise link, and redo the question a few days later.
:::

The stars show difficulty: ★ one method, ★★ two steps, ★★★ several parts or topics joined together. The questions are in mixed order on purpose.

:::exam Marking your own work
Give a mark only when the answer **says** the mark point, in your own words or the mark scheme's. A point that is nearly there earns nothing. For a Paper 4 task, give a feature mark only if the feature is in your code **and** your program produces the expected output. If you cannot decide, do not give the mark. You will learn more from an honest 70 than from a generous 85.
:::

:::try Paper 3 style: sections 13 to 20
Q: [5 marks] ★ (#cs.usertypes) A shop in Cape Town records the stock level of each item as one of three values: in stock, low stock or out of stock.

(a) Write pseudocode to define an enumerated type `StockLevel` with these three values and to declare a variable `Level` of that type. [3]

(b) State one advantage of using the enumerated type rather than storing the level as the integers 1, 2 and 3. [1]

(c) A pointer type is defined by `TYPE TIntPointer = ^INTEGER`. State what a variable of this type holds. [1]
H: An enumerated type is a list of names.
A: (a)

```pseudocode
TYPE StockLevel = (InStock, LowStock, OutOfStock)
DECLARE Level : StockLevel
```

- `TYPE StockLevel =` followed by the values in brackets [B1]
- the three values `InStock`, `LowStock` and `OutOfStock` separated by commas [B1]
- `DECLARE Level : StockLevel` [B1]

(b) The values are meaningful names, so the code is easier to read (and a value outside the three cannot be stored). [B1]

(c) The memory address of (a reference to) an integer variable. [B1]

Q: [6 marks] ★★ (#cs.usertypes) A random file has 7 slots, numbered 1 to 7. The address of a record is calculated as `(Key MOD 7) + 1`. If the slot is already used, the next slot is tried (linear probing), and after slot 7 the search goes back to slot 1. The file starts empty. Records with these keys are stored in this order: 15, 22, 9, 31, 12.

(a) Show the slot in which each record is stored. [4]

(b) A program searches the file for the key 29. Explain how the program finds that the key is not in the file. [2]
H: Work out each key MOD 7 first. A collision moves the record on by one slot.
A: (a) The calculated addresses are \(15 \text{ MOD } 7 = 1\) so slot 2; \(22 \text{ MOD } 7 = 1\) so slot 2; \(9 \text{ MOD } 7 = 2\) so slot 3; \(31 \text{ MOD } 7 = 3\) so slot 4; \(12 \text{ MOD } 7 = 5\) so slot 6.

| Slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Key stored | | 15 | 22 | 9 | 31 | 12 | |

- 15 is stored in slot 2 and 12 in slot 6 (their calculated slots are free) [B1]
- 22 collides with 15 at slot 2, so it is stored in slot 3 [B1]
- 9 collides with 22 at slot 3, so it is stored in slot 4 [B1]
- 31 collides with 9 at slot 4, so it is stored in slot 5 [B1]

(b) \(29 \text{ MOD } 7 = 1\), so the program starts at slot 2 and checks each slot in turn: 15, 22, 9, 31 and 12 are all different from 29. [B1]

Slot 7 is empty, so the search stops, because 29 would have been stored there (or earlier) if it were in the file: the key is not in the file. [B1]

Q: [7 marks] ★★ (#cs.float) A computer stores real numbers using 8 bits for the mantissa and 4 bits for the exponent, both in two's complement. The binary point is after the sign bit of the mantissa.

(a) Convert the floating-point number with mantissa 01101000 and exponent 0011 to denary. [2]

(b) Show how the number \(-2.5\) is stored in normalised form. [3]

(c) State the largest positive number that can be stored in normalised form, and the bit patterns of its mantissa and exponent. [2]
H: For (b), find the pattern for +2.5 first, then change the sign of the mantissa.
A: (a) The exponent 0011 is 3, so the binary point moves three places to the right. [B1]

The mantissa 0.1101000 becomes 0110.1000, which is \(4 + 2 + 0.5 = 6.5\). [B1]

(b) \(2.5 = 10.1_2 = 0.101 \times 2^{2}\), so the positive mantissa is 01010000 and the exponent is 0010. [B1]

Invert 01010000 to give 10101111, and add 1 to give 10110000. [B1]

The stored number is mantissa 10110000, exponent 0010. The first two bits of the mantissa are different, so it is normalised. [B1]

(c) The largest mantissa is 01111111 and the largest exponent is 0111. [B1]

The value is \(\tfrac{127}{128} \times 2^{7} = 127\). [B1]

Q: [8 marks] ★★ (#cs.networks2) A student sends an email, with an attached photograph, from her laptop to a friend in another country.

(a) Describe the part played by each of the four layers of the TCP/IP protocol stack as the email is sent. [4]

(b) State the protocol used to send the email to the mail server, and a protocol the friend can use to read it while it stays on the server. [2]

(c) The email travels across the internet by packet switching. Explain one benefit of packet switching over circuit switching for this purpose. [2]
H: Take the layers from the top down: Application, Transport, Internet, Link.
A: (a) One mark for each layer.

- Application layer: the email program and its protocol prepare the message and the attachment to be sent [B1]
- Transport layer: breaks the data into packets (segments), numbers them and uses port numbers, so that the packets can be put back in order and missing ones sent again [B1]
- Internet layer: adds the IP addresses of the sender and the receiver to each packet and routes it towards the destination [B1]
- Link layer: puts the packets into frames with the hardware (MAC) addresses and sends them over the physical medium [B1]

(b) SMTP is used to send the email [B1]. IMAP is used to read it while it stays on the server [B1].

(c) The email is split into packets and each packet can take a different route, so if one route is busy or fails, the packets still arrive by another route [B1]. No dedicated connection has to be kept for the whole time, so the same links are shared by many users, which uses the network more efficiently than a line reserved for one call [B1].

Q: [6 marks] ★★ (#cs.hardware2) (a) State two differences between a RISC processor and a CISC processor. [2]

(b) A processor has a five-stage pipeline. It carries out 8 instructions with no delays. Calculate the number of clock cycles needed with the pipeline and without it. [3]

(c) A graphics processor applies the same instruction to the data of many pixels at the same time. State the type of parallel processing, using Flynn's classification. [1]
A: (a) Any two.

- RISC has a small set of simple instructions; CISC has a large set of complex instructions [B1]
- RISC instructions usually take one clock cycle (and are all the same length); CISC instructions may take several cycles and different lengths [B1]
- (accept: RISC has more registers and relies on pipelining; CISC has fewer registers and does more work in each instruction)

(b) Without a pipeline: \(5 \times 8 = 40\) clock cycles. [B1]

With a pipeline, the first instruction takes 5 cycles and each of the other 7 finishes one cycle later. [B1]

\(5 + 8 - 1 = 12\) clock cycles. [B1]

(c) SIMD (Single Instruction, Multiple Data). [B1]

Q: [5 marks] ★★ (#cs.boolean) Simplify the expression \(X = A \cdot B + A \cdot \text{NOT } B + \text{NOT } A \cdot B\). Write the law used on each line. [5]
H: Take the first two terms together and factorise out A.
A: \(X = A \cdot (B + \text{NOT } B) + \text{NOT } A \cdot B\) (distributive law) [B1]

\(X = A \cdot 1 + \text{NOT } A \cdot B\) (complement law: \(B + \text{NOT } B = 1\)) [B1]

\(X = A + \text{NOT } A \cdot B\) (identity law: \(A \cdot 1 = A\)) [B1]

\(X = (A + \text{NOT } A) \cdot (A + B)\) (distributive law, in the form \(P + Q \cdot R = (P + Q) \cdot (P + R)\)) [B1]

\(X = 1 \cdot (A + B) = A + B\) (complement law, then identity law) [B1]

(The result \(A + B\) is the OR gate: check the row A = 0, B = 1, where both expressions give 1.)

Q: [7 marks] ★★★ (#cs.boolean) (a) A half adder has two inputs, A and B. Write a Boolean expression for each of its outputs, the sum S and the carry C, and state what the half adder adds. [3]

(b) A full adder adds A, B and a carry in, Cin. State the values of the sum S and the carry out Cout when A = 1, B = 1 and Cin = 1. [2]

(c) A JK flip-flop has Q = 0. State the value of Q after a clock pulse when (i) J = 1 and K = 1 and (ii) J = 0 and K = 0. [2]
A: (a) `S = A XOR B` [B1]

`C = A AND B` [B1]

It adds two single bits and gives a sum bit and a carry bit. [B1]

(b) \(1 + 1 + 1 = 11_2\), so S = 1 [B1] and Cout = 1 [B1].

(c) (i) J = 1 and K = 1 makes the output toggle (change to the opposite value), so Q becomes 1. [B1]

(ii) J = 0 and K = 0 leaves the output unchanged, so Q stays 0. [B1]

Q: [8 marks] ★★★ (#cs.os) A computer uses round robin scheduling with a time slice of 3 units. Three processes arrive as shown.

| Process | Arrival time | Burst time |
|---|---|---|
| P1 | 0 | 6 |
| P2 | 1 | 3 |
| P3 | 2 | 3 |

A process that arrives while another is running joins the ready queue before the process whose time slice has ended. The processor does no other work.

(a) Show which process has the processor in each period, from time 0 until all three have finished. [4]

(b) Calculate the average waiting time of the three processes. [2]

(c) Explain what is meant by disk thrashing in a computer that uses virtual memory. [2]
H: Waiting time = completion time − arrival time − burst time.
A: (a)

| Time | 0 to 3 | 3 to 6 | 6 to 9 | 9 to 12 |
|---|---|---|---|---|
| Process running | P1 | P2 | P3 | P1 |

- P1 runs from 0 to 3 and goes to the back of the queue, behind P2 and P3 which arrived during its slice [B1]
- P2 runs from 3 to 6 and finishes [B1]
- P3 runs from 6 to 9 and finishes [B1]
- P1 runs from 9 to 12 and finishes [B1]

(b) The completion times are P1 12, P2 6 and P3 9. The waiting times are \(12 - 0 - 6 = 6\) for P1, \(6 - 1 - 3 = 2\) for P2 and \(9 - 2 - 3 = 4\) for P3. [B1]

The average is \((6 + 2 + 4) \div 3 = 4\) time units. [B1]

(c) The processor spends most of its time swapping pages between main memory and the disk, so little useful work is done. [B1]

It happens when there are too many processes for the amount of RAM, so a page that has just been replaced is needed again almost at once. [B1]

Q: [7 marks] ★★ (#cs.translators) (a) A product code is one capital letter followed by one or more digits, for example K7 or Q4096. The rules `<Letter> ::= A|B|C| … |Z` and `<Digit> ::= 0|1|2| … |9` are already defined. Write BNF rules for `<Number>`, one or more digits, and for `<Code>`. [3]

(b) The expression `A * B + C / D` is written in infix notation. Write it in Reverse Polish notation, and evaluate it using a stack when A = 6, B = 5, C = 8 and D = 4. [4]
H: In BNF, a repeated item is written as a rule that uses itself.
A: (a)

```text
<Code> ::= <Letter><Number>
<Number> ::= <Digit> | <Digit><Number>
```

- `<Code> ::= <Letter><Number>` [B1]
- `<Number> ::= <Digit>` as the alternative for a single digit [B1]
- `<Digit><Number>` as the recursive alternative, so that any number of digits is allowed [B1]

(b) Multiplication and division come first: `A B * C D / +`. [B1] [B1] (one mark for the two operations in the right places, one mark for the `+` last)

Evaluating `6 5 * 8 4 / +`: 6 and 5 are pushed, and `*` replaces them with 30. [B1] Then 8 and 4 are pushed, `/` replaces them with 2, and `+` replaces 30 and 2 with 32. [B1]

Q: [7 marks] ★★ (#cs.security2) A bank's website uses SSL/TLS.

(a) Describe how the customer's browser uses the bank's digital certificate to set up a secure connection. [4]

(b) Explain why the data sent after the connection is set up is encrypted with a symmetric key, and not with the bank's public key. [2]

(c) Name the organisation that issues a digital certificate. [1]
A: (a) One mark for each of:

- the bank's server sends its digital certificate to the browser [B1]
- the browser checks the certificate: it is signed by a certificate authority (whose public key the browser holds) and is in date and for this website [B1]
- the browser takes the bank's public key from the certificate and uses it to encrypt a session key [B1]
- the bank decrypts the session key with its private key, so both ends now share a secret key [B1]

(b) Symmetric encryption is much faster than asymmetric encryption, so a large amount of data can be sent without delay. [B1]

Both ends already hold the session key, so no further key has to be sent (using the bank's public key for every message would need far more processing). [B1]

(c) A certificate authority (CA). [B1]

Q: [8 marks] ★★★ (#cs.ai) A road network has six towns. The roads and their lengths in kilometres are: S–B 6, B–A 2, B–D 4, A–G 5, A–C 4, A–D 6, C–D 3. The table gives the estimated distance from each town to G, found from a map.

| Town | S | A | B | C | D | G |
|---|---|---|---|---|---|---|
| Estimate to G | 11 | 4 | 6 | 7 | 9 | 0 |

(a) State what the values g, h and f mean in the A* algorithm. [2]

(b) Use the A* algorithm to find the route from S to G. Show the town chosen at each step with its values of g, h and f. [4]

(c) State the route found and its length. [1]

(d) Explain why A* examines fewer towns than Dijkstra's algorithm would on this network. [1]
H: At each step choose the town with the smallest f in the open list.
A: (a) g is the cost of the path from the start to the town so far [B1]. h is the estimated (heuristic) cost from the town to the goal, and \(f = g + h\); the town with the smallest f is chosen next [B1].

(b)

| Step | Town chosen | g | h | f |
|---|---|---|---|---|
| 1 | S | 0 | 11 | 11 |
| 2 | B | 6 | 6 | 12 |
| 3 | A | 8 | 4 | 12 |
| 4 | G | 13 | 0 | 13 |

- S is chosen first with f = 11 [B1]
- B is chosen with g = 6 and f = 12 (D is also found, with g = 10 and f = 19) [B1]
- A is chosen with g = 8 and f = 12 [B1]
- G is chosen with g = 13 and f = 13, because C and D have f = 19 [B1]

(c) S, B, A, G, with a length of \(6 + 2 + 5 = 13\) km. [B1]

(d) The estimates make C and D look much worse (f = 19) than G (f = 13), so A* never visits them, while Dijkstra would visit D (10) and C (12) before G (13). [B1]

Q: [5 marks] ★★ (#cs.ml) A clinic in Lahore has thousands of past appointment records. Each is labelled "attended" or "missed". The clinic wants a program that predicts whether a new booking will be missed.

(a) State the type of machine learning that is suitable, and explain why. [2]

(b) The program uses an artificial neural network. Describe how back propagation is used to train it. [3]
A: (a) Supervised learning [B1], because the training data is labelled with the correct outcome, so the program can learn from the examples (and compare its prediction with the label) [B1].

(b) One mark for each of:

- the output of the network is compared with the correct (labelled) output, and the error is calculated [B1]
- the error is passed backwards through the layers of the network [B1]
- the weights (and biases) are adjusted to reduce the error, and the process is repeated with many examples [B1]

Q: [6 marks] ★★ (#cs.algorithms2) The array `Values` holds these 12 values in ascending order.

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 5 | 9 | 14 | 21 | 26 | 33 | 40 | 47 | 52 | 61 | 70 | 84 |

A binary search sets `Low` to 1 and `High` to 12. Each time it sets `Mid ← (Low + High) DIV 2`. If the value at `Mid` is less than the target, `Low ← Mid + 1`; if it is greater, `High ← Mid - 1`.

(a) Complete a trace table for a search for the target 47. [4]

(b) State the time complexity, in Big O notation, of a binary search and of a bubble sort. [2]
A: (a)

| Low | High | Mid | Values[Mid] | Result |
|---|---|---|---|---|
| 1 | 12 | 6 | 33 | 47 > 33, so Low becomes 7 |
| 7 | 12 | 9 | 52 | 47 < 52, so High becomes 8 |
| 7 | 8 | 7 | 40 | 47 > 40, so Low becomes 8 |
| 8 | 8 | 8 | 47 | found at index 8 |

- first row: Mid = 6 and Low becomes 7 [B1]
- second row: Mid = 9 and High becomes 8 [B1]
- third row: Mid = 7 and Low becomes 8 [B1]
- fourth row: Mid = 8, the value 47 is found at index 8 [B1]

(b) Binary search: \(O(\log n)\) [B1]. Bubble sort: \(O(n^2)\) [B1].

Q: [8 marks] ★★★ (#cs.adts) (a) The values 38, 20, 55, 12, 30, 47, 62 and 25 are inserted, in this order, into an empty binary search tree. Complete a table that shows the left child and the right child of every node. [3]

(b) State the order in which the values are output by an in-order traversal of this tree. [1]

(c) A circular queue uses the array `Queue[1:5]`. `HeadPointer` is 1, `TailPointer` is 0 and `Count` is 0 at the start. To add an item, `TailPointer ← (TailPointer MOD 5) + 1` is done first and the item is stored at `Queue[TailPointer]`. To remove an item, it is read from `Queue[HeadPointer]` and then `HeadPointer ← (HeadPointer MOD 5) + 1` is done. `Count` is changed each time. The items A, B, C and D are added, two items are removed, and then E, F and G are added. State the contents of `Queue[1]` to `Queue[5]`, and the final values of `HeadPointer`, `TailPointer` and `Count`. [4]
H: A smaller value goes to the left, a larger one to the right. For (c), the tail pointer wraps from 5 back to 1.
A: (a)

| Node | Left child | Right child |
|---|---|---|
| 38 | 20 | 55 |
| 20 | 12 | 30 |
| 55 | 47 | 62 |
| 30 | 25 | none |
| 12 | none | none |
| 47 | none | none |
| 62 | none | none |
| 25 | none | none |

- 38 is the root, with 20 on its left and 55 on its right [B1]
- 12 and 30 are the children of 20, and 47 and 62 the children of 55 [B1]
- 25 is the left child of 30, and every other node has no children [B1]

(b) 12, 20, 25, 30, 38, 47, 55, 62 (ascending order). [B1]

(c) After A to D are added, `TailPointer` is 4. Removing two items removes A and B and moves `HeadPointer` to 3. E goes in position 5, then the pointer wraps to 1 for F and to 2 for G.

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| F | G | C | D | E |

- contents F, G, C, D, E in positions 1 to 5 [B1]
- `HeadPointer` is 3 [B1]
- `TailPointer` is 2 (it wrapped round from 5 to 1) [B1]
- `Count` is 5, so the queue is full [B1]

Q: [6 marks] ★★★ (#cs.recursion) This recursive function counts the digits of a positive whole number.

```pseudocode
FUNCTION Digits(N : INTEGER) RETURNS INTEGER
   IF N < 10 THEN
      RETURN 1
   ELSE
      RETURN 1 + Digits(N DIV 10)
   ENDIF
ENDFUNCTION
```

(a) State the base case of the function. [1]

(b) Complete a trace for the call `Digits(4821)`, showing each call, its parameter and the value it returns. [3]

(c) Explain how the stack is used when the function runs. [2]
A: (a) When `N < 10`, the function returns 1 without calling itself. [B1]

(b)

| Call | N | Value returned |
|---|---|---|
| Digits(4821) | 4821 | 4 |
| Digits(482) | 482 | 3 |
| Digits(48) | 48 | 2 |
| Digits(4) | 4 | 1 |

- the calls are made with N = 4821, 482, 48 and 4 [B1]
- `Digits(4)` is the base case and returns 1 [B1]
- the calls return 2, 3 and 4 in turn, as the answers come back up [B1]

(c) Each call puts its parameter and the return address on the stack, so the calls wait on the stack while the next call is made. [B1]

When the base case returns, the entries are removed in the reverse order (last in, first out), and each one uses the value that was returned to it. [B1]

Q: [7 marks] ★★★ (#cs.oop) A library keeps a record of each book: its title and whether it is on loan. A reference book is a kind of book that can never be borrowed.

(a) Write pseudocode for a class `Book` with a private title and a private on-loan flag, a constructor that sets the title and marks the book as not on loan, and a function `Borrow` that returns FALSE if the book is already on loan, and otherwise marks it as on loan and returns TRUE. [4]

(b) Write pseudocode for a class `Reference` that inherits from `Book`, calls the parent constructor, and replaces `Borrow` so that it always returns FALSE. [3]
A: 

```pseudocode
CLASS Book
   PRIVATE Title : STRING
   PRIVATE OnLoan : BOOLEAN

   PUBLIC PROCEDURE NEW(GivenTitle : STRING)
      Title ← GivenTitle
      OnLoan ← FALSE
   ENDPROCEDURE

   PUBLIC FUNCTION Borrow() RETURNS BOOLEAN
      IF OnLoan = TRUE THEN
         RETURN FALSE
      ELSE
         OnLoan ← TRUE
         RETURN TRUE
      ENDIF
   ENDFUNCTION
ENDCLASS

CLASS Reference INHERITS Book
   PUBLIC PROCEDURE NEW(GivenTitle : STRING)
      SUPER.NEW(GivenTitle)
   ENDPROCEDURE

   PUBLIC FUNCTION Borrow() RETURNS BOOLEAN
      RETURN FALSE
   ENDFUNCTION
ENDCLASS
```

- (a) `CLASS Book` with the private attributes `Title` and `OnLoan` of the right types [B1]
- (a) constructor `NEW` that sets `Title` and sets `OnLoan` to FALSE [B1]
- (a) `Borrow` is a `FUNCTION` that returns FALSE when the book is on loan [B1]
- (a) otherwise sets `OnLoan` to TRUE and returns TRUE [B1]
- (b) `CLASS Reference INHERITS Book` with `ENDCLASS` [B1]
- (b) the constructor calls `SUPER.NEW(GivenTitle)` [B1]
- (b) `Borrow` has the same name and header as in `Book` and returns FALSE every time (polymorphism: the same call behaves differently for a `Reference`) [B1]

Q: [10 marks] ★★★ (#cs.paradigms) (a) A travel company stores direct flights as facts.

```text
flight(lima, cusco).
flight(lima, quito).
flight(quito, bogota).
flight(cusco, puno).
```

(i) Write a rule `connects(X, Z)` that is true when there is a flight from X to some city and a flight from that city to Z. [3]

(ii) State every result, in order, for the goal `connects(lima, Where)`. [2]

(iii) State the result of the goal `connects(cusco, Where)`. [1]

(b) A low-level program uses the instructions in the table. The numbers after the addresses are the values stored there. IX is the index register and ACC is the accumulator.

| Instruction | Explanation |
|---|---|
| `LDR #n` | Load the number n into IX |
| `LDX <address>` | Load the contents of the address (the given address + the contents of IX) into ACC |
| `ADD <address>` | Add the contents of the address to ACC |
| `STO <address>` | Store the contents of ACC at the address |
| `END` | Return control to the operating system |

```text
100   LDR #2
101   LDX 300
102   ADD 301
103   STO 303
104   END
300   10
301   20
302   30
303   0
```

State the address from which `LDX 300` loads, and the contents of ACC and of address 303 when the program ends. [4]
H: Cities start with a lower-case letter, variables with a capital. For (b), add IX to the address.
A: (a)(i)

```text
connects(X, Z) IF flight(X, Y) AND flight(Y, Z).
```

- head `connects(X, Z)` followed by `IF` [B1]
- the two conditions `flight(X, Y)` and `flight(Y, Z)` joined with `AND` [B1]
- the same variable `Y` in both conditions, and a full stop at the end [B1]

(ii) The system tries the facts in order. The first flight from `lima` is to `cusco`, and `flight(cusco, puno)` gives `Where = puno`. The second is to `quito`, and `flight(quito, bogota)` gives `Where = bogota`.

- `Where = puno` [B1]
- `Where = bogota` [B1]

(iii) false: the only flight from `cusco` is to `puno`, and there is no flight from `puno`. [B1]

(b) IX holds 2, so `LDX 300` uses the address \(300 + 2 = 302\). [B1]

ACC receives 30, the contents of address 302. [B1]

`ADD 301` adds 20, so ACC is 50. [B1]

`STO 303` stores 50, so address 303 holds 50 and ACC holds 50 at the end. [B1]

Q: [5 marks] ★★ (#cs.fileproc) (a) A program asks the user for the name of a file and reads it. Explain why the program should use exception handling. [2]

(b) A random file holds student records. State the purpose of each of the pseudocode commands `SEEK`, `GETRECORD` and `PUTRECORD`. [3]
A: (a) The file may not exist, or may not be readable or may contain bad data, and without exception handling the program stops with an error message (crashes). [B1]

With exception handling the error is detected and dealt with, for example by showing a message and asking again, so the program continues. [B1]

(b) `SEEK` moves to the address (position) of the record in the file. [B1]

`GETRECORD` reads the record at that address into a variable. [B1]

`PUTRECORD` writes a record from a variable to that address, replacing the record stored there. [B1]
:::

## Paper 4 style tasks

The tasks below are in the Paper 4 style: a short scenario, named items, data, test code and an expected output. Do them at a computer, in plain Python in console mode. Write the program, run it, and compare your output with the expected output before you look at the answer. The model solutions create their own sample files in their first lines so that each one runs on its own; in the exam the file is given to you. The names are the task's names, as in the exam.

:::try Paper 4 style: programming tasks
Q: [10 marks] ★★ (#cs.adts) A calculator evaluates expressions in Reverse Polish notation, written with spaces between the items. A text file `Expressions.txt` holds these lines.

```text
3 4 +
2 3 4 * +
10 2 3 + -
6 7 * 2 -
8 +
```

(a) Write a class `Stack` that holds up to 10 integers in an array. It has a pointer `TopPointer` that is \(-1\) when the stack is empty, a method `Push(Item)` that returns `False` if the stack is full and otherwise stores the item and returns `True`, and a method `Pop()` that returns `None` if the stack is empty and otherwise removes and returns the top item. [5]

(b) Write a function `EvaluateRPN(Text)` that uses a `Stack` to evaluate an expression that contains whole numbers and the operators `+`, `-` and `*`. It returns the result, or `None` if an operator does not have two numbers to use. [3]

(c) Write a program that reads every line of the file, calls the function and outputs the expression, an equals sign and the result, or `Error` if the function returns `None`. Run it and copy the output. [2]

The expected output is:

```text
3 4 + = 7
2 3 4 * + = 14
10 2 3 + - = 5
6 7 * 2 - = 40
8 + = Error
```
H: The first value popped is the right-hand operand. For `10 2 3 + -`, the subtraction is \(10 - 5\).
A: 

```python
class Stack:
    def __init__(self):
        self.Items = [0] * 10
        self.TopPointer = -1

    def Push(self, Item):
        if self.TopPointer == 9:
            return False
        self.TopPointer = self.TopPointer + 1
        self.Items[self.TopPointer] = Item
        return True

    def Pop(self):
        if self.TopPointer == -1:
            return None
        Item = self.Items[self.TopPointer]
        self.TopPointer = self.TopPointer - 1
        return Item


def EvaluateRPN(Text):
    Operands = Stack()
    for Token in Text.split():
        if Token in ("+", "-", "*"):
            Right = Operands.Pop()
            Left = Operands.Pop()
            if Right is None or Left is None:
                return None
            if Token == "+":
                Result = Left + Right
            elif Token == "-":
                Result = Left - Right
            else:
                Result = Left * Right
            Operands.Push(Result)
        else:
            Operands.Push(int(Token))
    return Operands.Pop()


with open("Expressions.txt", "w") as File:
    File.write("3 4 +\n2 3 4 * +\n10 2 3 + -\n6 7 * 2 -\n8 +\n")

with open("Expressions.txt", "r") as File:
    for Line in File:
        Expression = Line.strip()
        Answer = EvaluateRPN(Expression)
        if Answer is None:
            print(Expression, "= Error")
        else:
            print(Expression, "=", Answer)
```

```output
3 4 + = 7
2 3 4 * + = 14
10 2 3 + - = 5
6 7 * 2 - = 40
8 + = Error
```

- (a) class `Stack` with an array of 10 elements and `TopPointer` set to \(-1\) in the constructor [B1]
- (a) `Push` returns `False` when `TopPointer` is 9 [B1]
- (a) `Push` increases the pointer, stores the item and returns `True` [B1]
- (a) `Pop` returns `None` when the stack is empty [B1]
- (a) `Pop` reads the top item, decreases the pointer and returns the item [B1]
- (b) the text is split into items, and a number is converted with `int` and pushed [B1]
- (b) an operator pops two values, the right operand first, and returns `None` if either is missing [B1]
- (b) the correct operation for `+`, `-` and `*` is done and the result is pushed, and the final value is popped and returned [B1]
- (c) the file is opened for reading and every line is processed, with `strip` [B1]
- (c) the output has the expected form, with `Error` for the last line, and is copied [B1]

(Accept `float` instead of `int`, a list with `append` and `pop` if the task had allowed it, and any message for an operator with too few numbers if the task did not give one.)

Q: [12 marks] ★★★ (#cs.oop) A teacher stores whole numbers in a binary search tree, designed with object-oriented programming.

(a) Write a class `Node` with the attributes `Value`, `Left` and `Right`. A new node holds a value and has no children (`None`). [2]

(b) Write a class `Tree` with an attribute `Root` that is `None` when the tree is empty. [1]

(c) Write a recursive method `Insert(Value)` of `Tree` that adds a value. A value that is smaller than a node's value goes to the left; any other value goes to the right. [4]

(d) Write a recursive method `InOrder()` that returns a list of the values in ascending order. [2]

(e) Write a recursive method `Height()` that returns the number of levels in the tree (0 for an empty tree). [2]

(f) Write a program that creates a tree, outputs the height of the empty tree, inserts the values 45, 28, 63, 17, 36, 52, 71 and 40 in this order, and outputs the values in order and the height. Run it and copy the output. [1]

The expected output is:

```text
Empty tree height: 0
In order: 17 28 36 40 45 52 63 71
Height: 4
```
H: For the recursive methods, write the case that stops the recursion first (an empty position).
A: 

```python
class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Left = None
        self.Right = None


class Tree:
    def __init__(self):
        self.Root = None

    def Insert(self, Value):
        self.Root = self.InsertFrom(self.Root, Value)

    def InsertFrom(self, Current, Value):
        if Current is None:
            return Node(Value)
        if Value < Current.Value:
            Current.Left = self.InsertFrom(Current.Left, Value)
        else:
            Current.Right = self.InsertFrom(Current.Right, Value)
        return Current

    def InOrder(self):
        Output = []
        self.InOrderFrom(self.Root, Output)
        return Output

    def InOrderFrom(self, Current, Output):
        if Current is not None:
            self.InOrderFrom(Current.Left, Output)
            Output.append(Current.Value)
            self.InOrderFrom(Current.Right, Output)

    def Height(self):
        return self.HeightFrom(self.Root)

    def HeightFrom(self, Current):
        if Current is None:
            return 0
        return 1 + max(self.HeightFrom(Current.Left), self.HeightFrom(Current.Right))


Numbers = Tree()
print("Empty tree height:", Numbers.Height())
for Value in [45, 28, 63, 17, 36, 52, 71, 40]:
    Numbers.Insert(Value)
print("In order:", *Numbers.InOrder())  # print(*items) prints each item of the list, separated by spaces
print("Height:", Numbers.Height())
```

```output
Empty tree height: 0
In order: 17 28 36 40 45 52 63 71
Height: 4
```

- (a) class `Node` with a constructor that stores `Value` [B1] and sets `Left` and `Right` to `None` [B1]
- (b) class `Tree` with `Root` set to `None` in the constructor [B1]
- (c) base case: an empty position (`None`) returns a new `Node` [B1]
- (c) a smaller value is inserted in the left subtree by a recursive call [B1]
- (c) any other value is inserted in the right subtree by a recursive call [B1]
- (c) the child link is updated with the result and the root is updated in `Insert` [B1]
- (d) base case: an empty position does nothing [B1]
- (d) left subtree, then the node's value, then right subtree, in that order [B1]
- (e) an empty position gives 0 [B1]
- (e) 1 plus the larger of the heights of the two subtrees [B1]
- (f) the program inserts the eight values in order and outputs the three lines of the expected output [B1]

(The height is 4 because the longest path is 45, 28, 36, 40. A method that uses a `while` loop instead of recursion does not earn the recursion marks if the question asks for a recursive method.)

Q: [12 marks] ★★ (#cs.fileproc) A shop company records its sales in a text file `Sales.txt`. Each line has the branch, the item and the quantity, separated by commas.

```text
North,Pen,40
South,Book,12
North,Book,5
East,Pen,x
West,Pen,22
South,Pen,18
```

Write a program with a function `ProcessSales(FileName)` that:

- reads every line of the file, and outputs `Bad line`, the line number, a colon and the line if the quantity is not a whole number, and does not process that line [5]
- writes the item and quantity of each valid line, as `item,quantity`, to a text file named after its branch (for example `North.txt`) [3]
- outputs for each branch the number of sales and the total quantity [2]
- outputs `File not found:` and the file name, and stops, if the file does not exist [2]

Test the function with `Sales.txt`, then output the lines of `North.txt`, then test it with a file `Missing.txt`. Run the program and copy the output.

The expected output is:

```text
Bad line 4: East,Pen,x
North: 2 sales, 45 items
South: 2 sales, 30 items
West: 1 sales, 22 items
North.txt holds:
Pen,40
Book,5
File not found: Missing.txt
```
H: Keep the valid lines of each branch in a dictionary of lists, then write the files when the whole file has been read.
A: 

```python
def ProcessSales(FileName):
    Groups = {}
    LineNumber = 0
    try:
        with open(FileName, "r") as Source:
            for Line in Source:
                LineNumber = LineNumber + 1
                Fields = Line.strip().split(",")
                try:
                    Quantity = int(Fields[2])
                except (ValueError, IndexError):  # a tuple of names catches either error
                    print("Bad line " + str(LineNumber) + ": " + Line.strip())
                    continue
                Branch = Fields[0]
                if Branch not in Groups:
                    Groups[Branch] = []
                Groups[Branch].append((Fields[1], Quantity))
    except FileNotFoundError:
        print("File not found:", FileName)
        return
    for Branch in Groups:
        Total = 0
        with open(Branch + ".txt", "w") as Out:
            for Item, Quantity in Groups[Branch]:
                Out.write(Item + "," + str(Quantity) + "\n")
                Total = Total + Quantity
        print(Branch + ":", len(Groups[Branch]), "sales,", Total, "items")


with open("Sales.txt", "w") as File:
    File.write("North,Pen,40\nSouth,Book,12\nNorth,Book,5\nEast,Pen,x\nWest,Pen,22\nSouth,Pen,18\n")

ProcessSales("Sales.txt")
print("North.txt holds:")
with open("North.txt", "r") as File:
    for Line in File:
        print(Line.strip())
ProcessSales("Missing.txt")
```

```output
Bad line 4: East,Pen,x
North: 2 sales, 45 items
South: 2 sales, 30 items
West: 1 sales, 22 items
North.txt holds:
Pen,40
Book,5
File not found: Missing.txt
```

- the file is opened for reading and every line is read in a loop [B1]
- each line is cleaned with `strip` and split with `split(",")` [B1]
- the quantity is converted with `int` [B1]
- a bad quantity is caught (`except ValueError`) and the line is not processed [B1]
- the message has `Bad line`, the correct line number (4), a colon and the line [B1]
- the valid lines are grouped by branch [B1]
- one file per branch is opened for writing and each line is written as `item,quantity` with a new line [B1] [B1]
- the number of sales and the total quantity are output for each branch [B1] [B1]
- `FileNotFoundError` is caught and `File not found:` is output with the name, and the function stops [B1] [B1]

(The output shows the bad line, the three branch totals, the contents of `North.txt` and the missing-file message, so the screenshot is evidence for most of these features. Accept a version that writes the files as it reads, with mode `"a"`, if the files are removed first. A file that is not closed, or not opened with `with`, may lose its last lines.)

Q: [10 marks] ★★★ (#cs.adts) A linked list is stored in two global arrays of 6 nodes, `Data` and `Pointer`. Index 0 is not used, so node numbers are the list indexes 1 to 6 and the pointer 0 means no node. `StartPointer` is the first node of the list and `FreePointer` is the first node of the free list. The list holds whole numbers in ascending order.

(a) Write a procedure `InitialiseList` that makes the list empty and links all six nodes into the free list. [2]

(b) Write a function `InsertItem(NewItem)` that takes a node from the free list and inserts the item in the correct place, returning `True`, or returns `False` if there is no free node. [4]

(c) Write a function `DeleteItem(Target)` that removes the node that holds `Target`, returns the node to the free list and returns `True`, or returns `False` if the item is not in the list. [2]

(d) Write a procedure `OutputList` that outputs the items in order on one line. [1]

(e) Test the program: insert 40, 10, 30, 20, 50, 60 and 70 (outputting `Inserted` or `Full:` and the number), output the list, delete 30, output the list, insert 25, output the list, and output the two pointers. Run it and copy the output. [1]

The expected output is:

```text
Inserted 40
Inserted 10
Inserted 30
Inserted 20
Inserted 50
Inserted 60
Full: 70
10 20 30 40 50 60
Deleted 30: True
10 20 40 50 60
Inserted 25: True
10 20 25 40 50 60
StartPointer 2 FreePointer 0
```
H: A new node must point to the rest of the list before the previous node points to the new node.
A: 

```python
Data = [0] * 7
Pointer = [0] * 7
StartPointer = 0
FreePointer = 1


def InitialiseList():
    global StartPointer, FreePointer
    StartPointer = 0
    FreePointer = 1
    for Index in range(1, 6):
        Pointer[Index] = Index + 1
    Pointer[6] = 0


def InsertItem(NewItem):
    global StartPointer, FreePointer
    if FreePointer == 0:
        return False
    NewNode = FreePointer
    FreePointer = Pointer[NewNode]
    Data[NewNode] = NewItem
    Previous = 0
    Current = StartPointer
    while Current != 0 and Data[Current] < NewItem:
        Previous = Current
        Current = Pointer[Current]
    Pointer[NewNode] = Current
    if Previous == 0:
        StartPointer = NewNode
    else:
        Pointer[Previous] = NewNode
    return True


def DeleteItem(Target):
    global StartPointer, FreePointer
    Previous = 0
    Current = StartPointer
    while Current != 0 and Data[Current] != Target:
        Previous = Current
        Current = Pointer[Current]
    if Current == 0:
        return False
    if Previous == 0:
        StartPointer = Pointer[Current]
    else:
        Pointer[Previous] = Pointer[Current]
    Pointer[Current] = FreePointer
    FreePointer = Current
    return True


def OutputList():
    Current = StartPointer
    Items = []
    while Current != 0:
        Items.append(Data[Current])
        Current = Pointer[Current]
    print(*Items)  # print(*items) prints each item of the list, separated by spaces


InitialiseList()
for Number in [40, 10, 30, 20, 50, 60, 70]:
    if InsertItem(Number):
        print("Inserted", Number)
    else:
        print("Full:", Number)
OutputList()
print("Deleted 30:", DeleteItem(30))
OutputList()
print("Inserted 25:", InsertItem(25))
OutputList()
print("StartPointer", StartPointer, "FreePointer", FreePointer)
```

```output
Inserted 40
Inserted 10
Inserted 30
Inserted 20
Inserted 50
Inserted 60
Full: 70
10 20 30 40 50 60
Deleted 30: True
10 20 40 50 60
Inserted 25: True
10 20 25 40 50 60
StartPointer 2 FreePointer 0
```

- (a) `StartPointer` set to 0 and `FreePointer` set to 1 [B1]
- (a) a loop links each node to the next, and the last node has pointer 0 [B1]
- (b) returns `False` if `FreePointer` is 0 [B1]
- (b) takes the first free node, moves `FreePointer` on and stores the item [B1]
- (b) a loop follows the pointers, with the end-of-list test first, to find the place [B1]
- (b) the new node's pointer is set before the previous pointer or `StartPointer` is changed, and `True` is returned [B1]
- (c) finds the node and the previous node, and returns `False` if it is not found; makes the previous node (or `StartPointer`) skip it [B1]
- (c) puts the node at the front of the free list and returns `True` [B1]
- (d) follows the list from `StartPointer` to 0 and outputs every item in order [B1]
- (e) the test program gives the expected output, showing that 70 is refused and that the freed node is reused for 25 [B1]

Q: [8 marks] ★★ (#cs.usertypes) A school stores student records in a hash table with 7 positions, numbered 0 to 6. Each record is an object of a class `Student` with the attributes `StudentID` (an integer) and `Name`. The position of a record is `StudentID MOD 7`. If the position is taken, the next position is tried, and after position 6 the search wraps to position 0.

(a) Write the class `Student` and the global array `Table`, with every position empty. [2]

(b) Write a function `Store(Record)` that stores a record using this method and returns the position used, or \(-1\) if the table is full. [3]

(c) Write a function `Find(Key)` that returns the name of the student with that `StudentID`, or `Not found`. [2]

(d) Test the program by storing students 1042 Aisha, 2056 Boris, 3011 Chen, 4077 Dara, 2113 Emeka and 5023 Farah, outputting the position of each, and then outputting the results of `Find(2113)` and `Find(9999)`. Run it and copy the output. [1]

The expected output is:

```text
Stored 1042 in slot 6
Stored 2056 in slot 5
Stored 3011 in slot 1
Stored 4077 in slot 3
Stored 2113 in slot 0
Stored 5023 in slot 4
Emeka
Not found
```
H: The student 2113 has the same position as 1042. For `Find`, stop at an empty position.
A: 

```python
class Student:
    def __init__(self, StudentID, Name):
        self.StudentID = StudentID
        self.Name = Name


Table = [None] * 7


def Hash(Key):
    return Key % 7


def Store(Record):
    Address = Hash(Record.StudentID)
    for Step in range(7):
        Slot = (Address + Step) % 7
        if Table[Slot] is None:
            Table[Slot] = Record
            return Slot
    return -1


def Find(Key):
    Address = Hash(Key)
    for Step in range(7):
        Slot = (Address + Step) % 7
        if Table[Slot] is None:
            return "Not found"
        if Table[Slot].StudentID == Key:
            return Table[Slot].Name
    return "Not found"


Students = [(1042, "Aisha"), (2056, "Boris"), (3011, "Chen"), (4077, "Dara"),
            (2113, "Emeka"), (5023, "Farah")]
for StudentID, Name in Students:
    print("Stored", StudentID, "in slot", Store(Student(StudentID, Name)))
print(Find(2113))
print(Find(9999))
```

```output
Stored 1042 in slot 6
Stored 2056 in slot 5
Stored 3011 in slot 1
Stored 4077 in slot 3
Stored 2113 in slot 0
Stored 5023 in slot 4
Emeka
Not found
```

- (a) class `Student` with a constructor that stores both attributes [B1]
- (a) `Table = [None] * 7` [B1]
- (b) the position is calculated with `MOD 7` [B1]
- (b) a loop tries the next positions, wrapping round with `MOD 7`, and stores the record in the first empty one [B1]
- (b) returns the position used, and \(-1\) if the loop ends without storing [B1]
- (c) starts at the calculated position and follows the same probing, stopping at an empty position and returning `Not found` [B1]
- (c) returns the name when the `StudentID` matches [B1]
- (d) the test gives the expected output: Emeka was stored in slot 0 because slot 6 was taken by 1042, and 9999 is not found [B1]

(Calculated positions: \(1042 \text{ MOD } 7 = 6\), \(2056 \text{ MOD } 7 = 5\), \(3011 \text{ MOD } 7 = 1\), \(4077 \text{ MOD } 7 = 3\), \(2113 \text{ MOD } 7 = 6\) and \(5023 \text{ MOD } 7 = 4\). The record 2113 collides at 6 and wraps to 0.)
:::

## Quiz: A Level misconceptions

:::quiz Where A Level students lose marks
? A floating-point number has a negative mantissa. It is normalised when the mantissa starts with
- 11
+ 10
- 01
- 00
> The first two bits of a normalised mantissa are different: 01 for a positive number and 10 for a negative one. A mantissa starting 11 can still be shifted left to gain a significant bit.

? A student circles three neighbouring 1s on a Karnaugh map as one group. What is wrong?
- nothing: any group of neighbouring 1s is allowed
- groups must be circled in a square shape only
+ groups must have 1, 2, 4, 8 or 16 cells, so three 1s need a group of 2 and another group
- groups must include a 0 to show where the edge is
> A group of three cannot be read as a single product term. Use a group of 2 and a second group (the second group may overlap the first).

? A student uses Dijkstra's algorithm to find the shortest route from S to T. When should the algorithm stop?
- when T first receives a distance
+ when T is the unvisited vertex with the smallest distance
- when every edge has been looked at once
- when the first complete path from S to T is found
> A vertex's distance is final only when it is chosen as the smallest. T can get a distance early that a longer-looking route improves later.

? A process in the blocked state is waiting for a disk read. The read finishes. What happens next?
- the process goes straight to the running state
+ the process goes to the ready state
- the process goes back to the blocked state
- the process is removed from memory
> The scheduler decides which ready process runs. A blocked process never goes straight to running.

? A Reverse Polish expression is `8 2 -`. A student evaluates it as \(-6\). What is the correct result, and what went wrong?
- 10, because the operator is always an addition
- 4, because the numbers are divided
+ 6, because the first value popped is the right-hand operand (2), so the sum is 8 − 2
- \(-6\), because the operator subtracts the first number from the second
> Pop the right operand first (2), then the left operand (8), and calculate left − right = 6. Reversing the order gives \(2 - 8 = -6\).

? What is encrypted to make a digital signature?
- the whole message, with the receiver's public key
- the whole message, with the sender's private key
+ the digest of the message, with the sender's private key
- the digest of the message, with the receiver's public key
> The signature proves who sent the message and that it is unchanged. The digest is encrypted with the sender's private key, and the receiver checks it with the sender's public key.

? Which key does a digital certificate contain?
- the owner's private key
+ the owner's public key
- the certificate authority's private key
- the browser's session key
> A certificate links an identity to a public key and is signed by the certificate authority. A private key must never be shared.

? A recursive function has no base case. What happens when it runs?
- it runs faster than a loop
- it returns 0
+ the calls never stop, the stack grows until it overflows and the program fails
- the compiler removes the function
> Without a base case every call makes another call. Each one uses space on the stack, until there is none left.

? In a declarative language, which of these is a variable?
- `ortiz`
+ `Teacher`
- `r12`
- `maths`
> Variables start with a capital letter, and constants (names of things) start with a lower-case letter.

? What is the greatest number of comparisons that a binary search needs for a sorted array of 1000 items?
- 1000
- 500
+ 10
- 100
> Each comparison halves the items left. \(2^{9} = 512\) is less than 1000 and \(2^{10} = 1024\) is more, so 10 comparisons are enough.

? Two keys give the same hash address. What does this mean?
- the program has a bug that must be fixed
- the file is corrupt
+ a collision: normal, and handled by a rule such as linear probing
- the keys are equal
> Many keys share a small number of addresses, so collisions are expected. The file needs a rule to find another slot.
:::

:::recap
- Mix the sections: the exam does not announce the topic. Find the method first (floating point, K-map, trace, pseudocode), then do it, with every step shown.
- Marks are for mark points (theory) or for features of code (Paper 4). A point earns a mark only when it is written, with the key named.
- Write pseudocode in the Cambridge style by hand for Paper 3; write Python in console mode, with the task's names, for Paper 4.
- Test with normal, boundary and erroneous data, and check that your output matches the expected output before you paste a screenshot.
- Review every lost mark: knowledge, technique or slip. Redo the question after a few days.
:::

:::links
- practise: [Floating-point numbers: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/13-data-representation-/floating-point-numbers-representation-and-manipulation/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Protocols: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/14-communication-and-internet-technologies-/protocols/exam-questions/) · Save My Exams · TCP/IP and application protocol questions [paid]
- practise: [Programming paradigms: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/20-further-programming-/programming-paradigms/exam-questions/) · Save My Exams · declarative and low-level questions [paid]
- practise: [Exercism: Python track](https://exercism.org/tracks/python) · Exercism · free Python exercises with feedback
- papers: [Paper 3 past papers by series](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-3/) · Physics & Maths Tutor · Paper 3 only [unofficial]
- papers: [Paper 4 past papers by series](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-4/) · Physics & Maths Tutor · Paper 4 only [unofficial]
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists

Links checked 13 November 2026.
:::

Next: [Mock Paper 1: Theory Fundamentals](#cs.mock.p1)
