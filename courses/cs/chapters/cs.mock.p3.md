@chapter cs.mock.p3
@title Mock Paper 3: Advanced Theory
@level mock
@paper CAIE 9618 Paper 3
@time 1 h 30 min
@summary A full-length Paper 3 mock: twelve scenario questions worth 75 marks that cover sections 13 to 20, from floating-point numbers, user-defined types, protocols and switching, processors, a Karnaugh map, scheduling, BNF and Reverse Polish notation, public keys and digital signatures, a shortest-path graph and machine learning, to a binary tree in arrays, a class in pseudocode and declarative facts and rules. Every answer is a full mark scheme with one mark point per mark.

:::exam Read these instructions first
- You have **1 hour 30 minutes**. The clock above starts when you open the paper. Stop at the end of the time, then press **Finish** to see the mark schemes.
- Answer **all** questions. Write your answers on paper (or type them), as you would on the question paper.
- **Calculators must not be used** in this paper. Every calculation can be done by hand.
- The marks for each part of a question are shown in brackets, for example [3]. The total for the paper is **75 marks**.
- **No marks will be awarded for using brand names** of software packages or hardware.
- Use the **marks in brackets** to decide how many different points to make: one mark is one separate, correct point.
- Plan about 1.2 minutes per mark: a 5-mark question deserves about 6 minutes.
- When the time is up, press Finish, mark each answer honestly (a mark only for a point actually made), enter your mark for each question, and use the chapters listed to revise.
:::

:::try
Q: [7 marks] (#cs.float) A computer stores real numbers in floating-point form. The mantissa has 10 bits and the exponent has 4 bits, both in two's complement. The binary point is after the first bit of the mantissa.

(a) The mantissa is 0101100000 and the exponent is 0011. Calculate the denary value of the number. [2]

(b) Show the normalised floating-point representation of −3.25. Show your working. [3]

(c) A different number is stored with the mantissa 0001101100 and the exponent 0100. State why this representation is not normalised, and show the normalised form of the same number. [2]
A: (a)

- the exponent 0011 is 3, so the binary point moves three places to the right: 0101100000 is 0.101100000 × 2³, which is 0101.100000 [B1]
- 101.1 in binary is 5.5 in denary [B1]

(b)

- 3.25 in binary is 11.01, which is 0.1101 × 2², so the positive mantissa is 0110100000 and the exponent is 0010 [B1]
- the negative mantissa is found by inverting 0110100000 to give 1001011111 and adding 1, which gives 1001100000 [B1]
- the answer is mantissa 1001100000 and exponent 0010; it is normalised because the first two bits are different (10) [B1]

(c)

- not normalised because the first two bits of the mantissa are both 0 (so the mantissa has leading zeros and wastes precision) [B1]
- shifting the mantissa left two places gives 0110110000 and reducing the exponent by 2 gives 0010 (the number is 3.375 in both forms) [B1]
:::

:::try
Q: [6 marks] (#cs.usertypes) A language school in Prague gives lessons on the five weekdays only. A program for the school uses user-defined data types.

(a) Write pseudocode to define an enumerated data type `Weekday` whose possible values are Mon, Tue, Wed, Thu and Fri. [2]

(b) Write a pseudocode statement to declare a variable `LessonDay` of this type and a statement to assign the value Wed to it. Give one reason why an enumerated type is better than storing the day as an integer from 1 to 5. [2]

(c) A pointer type `DayPointer` is to point to a value of type `Weekday`. Write pseudocode to define the pointer type, declare a variable `NextLesson` of that type and make it point to `LessonDay`. [2]
A: (a)

```pseudocode
TYPE Weekday = (Mon, Tue, Wed, Thu, Fri)
```

- the keyword `TYPE`, the name `Weekday` and `=` [B1]
- the five values inside brackets, separated by commas [B1]

(b)

```pseudocode
DECLARE LessonDay : Weekday
LessonDay ← Wed
```

- both statements correct (declaration with the type name, assignment with `←` and no quotation marks) [B1]
- only the listed values can be stored, so an invalid day such as 6 or "Sat" is impossible (accept: the code is easier to read because the value has a name) [B1]

(c)

```pseudocode
TYPE DayPointer = ^Weekday
DECLARE NextLesson : DayPointer
NextLesson ← ^LessonDay
```

- `TYPE DayPointer = ^Weekday` [B1]
- the variable declared with the pointer type and `NextLesson ← ^LessonDay` (the pointer holds the address of `LessonDay`) [B1]
:::

:::try
Q: [6 marks] (#cs.networks2) A student in Kigali downloads a large video file from a website. Later she makes a voice call to a friend over the telephone network.

(a) The download uses the TCP/IP protocol stack. State the purpose of the Transport layer and of the Internet layer in the download. [2]

(b) Describe how a message is sent across the internet by packet switching. [2]

(c) The voice call uses circuit switching. State two features of circuit switching. [2]
A: (a)

- Transport layer: splits the data into packets (segments) that are numbered, so that the receiver can check for missing packets and put them back in order (accept: uses port numbers to pass the data to the correct application) [B1]
- Internet layer: adds the IP addresses of the sender and the destination to each packet, so that routers can forward it [B1]

(b)

- the message is split into packets, and each packet has a header containing the destination address and a sequence number [B1]
- each packet is routed independently by routers and may take a different route; the packets are reassembled in order at the destination [B1]

(c)

- a dedicated path (circuit) is set up between the two callers before any data is sent [B1]
- the whole path is reserved for the call, even when nobody is speaking, so the bandwidth is not shared [B1] (accept instead: all the data takes the same route, so it arrives in order with no reassembly; the circuit is released when the call ends)
:::

:::try
Q: [5 marks] (#cs.hardware2) A games console has a RISC processor with a four-stage pipeline. The stages are fetch, decode, execute and write back. Each stage takes one clock cycle. The console is also able to run old games written for a different processor.

(a) A program of 6 instructions with no jumps is run. Calculate the number of clock cycles needed (i) without pipelining and (ii) with pipelining. [2]

(b) State two features of a RISC processor that make pipelining easier to use. [2]

(c) The old games run inside a virtual machine. State one benefit of using a virtual machine for this. [1]
A: (a)

- without pipelining: \(6 \times 4 = 24\) cycles [B1]
- with pipelining: \(4 + (6 - 1) = 9\) cycles [B1]

(b)

- every instruction is a simple one that takes the same time (one cycle) to execute, so the stages stay in step [B1]
- instructions have a fixed length, so the next instruction can be fetched before the current one is decoded [B1] (accept instead: only load and store instructions access memory, so few slow instructions hold up the pipeline; many general-purpose registers, so fewer memory accesses are needed)

(c)

- software written for one type of processor can run unchanged on a different one, because the virtual machine imitates the old hardware (accept: the old games cannot damage the console) [B1]
:::

:::try
Q: [7 marks] (#cs.boolean) A greenhouse controller switches a fan on (X = 1) according to three sensors. A is 1 when the temperature is high, B is 1 when the door is open and C is 1 when the humidity is high. The truth table shows when the fan is on.

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

(a) Complete the Karnaugh map (K-map) for X. [2]

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | | | | |
| 1 | | | | |

(b) Draw loops on your K-map and write a simplified Boolean expression for X. [4]

(c) The state of the fan is stored by a JK flip-flop whose output Q is 0. State the value of Q after a clock pulse when J = 1 and K = 1. [1]
A: (a) the completed K-map:

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |

- row A = 0 correct: 1 1 0 0 [B1]
- row A = 1 correct: 1 1 1 0 [B1]

(b)

- a loop of four 1s: both rows, columns 00 and 01 [B1]
- a loop of two 1s: row A = 1, columns 01 and 11 [B1]
- the loop of four gives NOT B, because B is 0 in every cell of the loop [B1]
- the loop of two gives A AND C, and the expression is X = NOT B OR (A AND C) [B1]

(c)

- Q becomes 1 (when J = 1 and K = 1 the output toggles, that is, it changes to the opposite value) [B1]
:::

:::try
Q: [6 marks] (#cs.os) A computer uses shortest remaining time (SRT) scheduling. A newly arrived process pre-empts the running process if its burst time is less than the remaining time of the running process. Three processes arrive as shown. Times are in milliseconds (ms).

| Process | Arrival time | Burst time |
|---|---|---|
| P1 | 0 | 6 |
| P2 | 1 | 4 |
| P3 | 2 | 1 |

(a) Describe the blocked state of a process. [2]

(b) State the time at which each of the three processes finishes. Show your working. [3]

(c) The waiting time of a process is its finish time minus its arrival time minus its burst time. Calculate the average waiting time. [1]
A: (a)

- the process is waiting for an event, such as an input or output operation to finish, before it can continue [B1]
- it cannot run even if the processor is free; when the event happens it moves to the ready state [B1]

(b)

- P1 runs from 0 to 1, then P2 arrives with burst 4, which is less than the 5 ms that P1 has left, so P2 runs from 1 to 2 [B1]
- P3 arrives at 2 with burst 1, less than the 3 ms that P2 has left, so P3 runs from 2 to 3 and finishes at 3 ms [B1]
- P2 then runs from 3 to 6 and finishes at 6 ms, and P1 runs from 6 to 11 and finishes at 11 ms [B1]

(c)

- waiting times: P1 \(11 - 0 - 6 = 5\), P2 \(6 - 1 - 4 = 1\), P3 \(3 - 2 - 1 = 0\); the average is \((5 + 1 + 0) \div 3 = 2\) ms [B1]
:::

:::try
Q: [6 marks] (#cs.translators) A booking system accepts a time of day written as two digits, a colon and two digits, for example 07:45. The rules are written in Backus-Naur Form (BNF).

```text
<time> ::= <hour>:<minute>
<hour> ::= 0<digit> | 1<digit>
<digit> ::= 0|1|2|3|4|5|6|7|8|9
```

(a) Write the rule for `<minute>` so that a minute is any value from 00 to 59. You may use `<digit>`. [2]

(b) Using your rule, state whether each of 07:45 and 12:60 is valid, and give a reason for each. [2]

(c) The system evaluates `9 2 - 4 *`, written in Reverse Polish notation (RPN), using a stack. Show the contents of the stack after each item is processed and state the result. [2]
A: (a) One possible answer:

```text
<minute> ::= 0<digit> | 1<digit> | 2<digit> | 3<digit> | 4<digit> | 5<digit>
```

- the rule has the form `<minute> ::=` with alternatives separated by `|` [B1]
- the first digit is limited to 0, 1, 2, 3, 4 or 5, each followed by `<digit>` (accept a helper rule such as `<tens> ::= 0|1|2|3|4|5` with `<minute> ::= <tens><digit>`) [B1]

(b)

- 07:45 is valid: the hour 07 matches `0<digit>` and the minute 45 matches `4<digit>` [B1]
- 12:60 is not valid: the hour 12 is valid but the minute 60 is not, because no minute rule starts with 6 [B1]

(c)

| Item | Stack after the item (top on the right) |
|---|---|
| 9 | 9 |
| 2 | 9, 2 |
| - | 7 |
| 4 | 7, 4 |
| * | 28 |

- stack contents correct after each of the five items (9; 9, 2; 7; 7, 4; 28) [B1]
- the result is 28 [B1]
:::

:::try
Q: [5 marks] (#cs.security2) A clinic in Oslo sends a patient report to a specialist in another country over the internet. The clinic and the specialist each have a pair of keys, one public and one private.

(a) The clinic wants only the specialist to be able to read the report. State which key is used to encrypt the report and which key is used to decrypt it, and explain why nobody else can read it. [3]

(b) The specialist also needs to be sure that the report really came from the clinic and was not changed on the way. Describe how a digital signature is used to do this. [2]
A: (a)

- the report is encrypted with the specialist's public key [B1]
- the report is decrypted with the specialist's private key [B1]
- only the specialist holds the private key, and the public key cannot be used to decrypt the cipher text, so nobody else can read it [B1]

(b)

- the clinic creates a digest of the report with a hashing algorithm and encrypts the digest with the clinic's private key; this is the digital signature, sent with the report [B1]
- the specialist decrypts the signature with the clinic's public key and compares the digest with one calculated from the received report; if they match, the report came from the clinic and was not changed [B1]
:::

:::try
Q: [8 marks] (#cs.ai) A courier company in Nairobi uses a graph to model the roads between six depots, P, Q, R, S, T and U. The number on each road is its length in kilometres.

<figure class="fig small"><svg viewBox="0 0 360 246" role="img" aria-label="A graph with six labelled points P, Q, R, S, T and U joined by nine roads. The lengths in kilometres are: P to Q 4, P to R 2, Q to R 1, Q to S 5, R to S 8, R to T 10, S to T 2, S to U 6 and T to U 3."><line class="ln" x1="38" y1="122" x2="118" y2="44"/><line class="ln" x1="38" y1="122" x2="118" y2="200"/><line class="ln" x1="118" y1="44" x2="118" y2="200"/><line class="ln" x1="118" y1="44" x2="222" y2="104"/><line class="ln" x1="118" y1="200" x2="222" y2="104"/><line class="ln" x1="118" y1="200" x2="252" y2="202"/><line class="ln" x1="222" y1="104" x2="252" y2="202"/><line class="ln" x1="222" y1="104" x2="330" y2="136"/><line class="ln" x1="252" y1="202" x2="330" y2="136"/><circle class="f1 s-acc sw2" cx="38" cy="122" r="16"/><text class="tl tb tc" x="38" y="126">P</text><circle class="f1 s-acc sw2" cx="118" cy="44" r="16"/><text class="tl tb tc" x="118" y="48">Q</text><circle class="f1 s-acc sw2" cx="118" cy="200" r="16"/><text class="tl tb tc" x="118" y="204">R</text><circle class="f1 s-acc sw2" cx="222" cy="104" r="16"/><text class="tl tb tc" x="222" y="108">S</text><circle class="f1 s-acc sw2" cx="252" cy="202" r="16"/><text class="tl tb tc" x="252" y="206">T</text><circle class="f1 s-acc sw2" cx="330" cy="136" r="16"/><text class="tl tb tc" x="330" y="140">U</text><text class="tl tc halo" x="86.4" y="95.6">4</text><text class="tl tc halo" x="69.6" y="173.6">2</text><text class="tl tc halo" x="108" y="126">1</text><text class="tl tc halo" x="164" y="88.4">5</text><text class="tl tc halo" x="178.1" y="164.8">8</text><text class="tl tc halo" x="184.8" y="217">10</text><text class="tl tc halo" x="226.5" y="160.2">2</text><text class="tl tc halo" x="272.6" y="135.5">6</text><text class="tl tc halo" x="298.8" y="182.2">3</text></svg><figcaption>The road network for Question 9. Each number is the length of the road in kilometres.</figcaption></figure>

Dijkstra's algorithm is used to find the shortest route from depot P. The table shows the first two rows, in the order that the depots are finalised.

| Depot | Shortest distance from P (km) | Previous depot |
|---|---|---|
| P | 0 | none |
| R | 2 | P |
| Q | | |
| S | | |
| T | | |
| U | | |

(a) Complete the table for Q, S, T and U. [4]

(b) State the shortest route from P to U and its length. [2]

(c) The company also trains an artificial neural network to read handwritten depot codes from photographs that have been labelled with the correct code. State the type of machine learning used and describe the purpose of back propagation. [2]
A: (a)

| Depot | Shortest distance from P (km) | Previous depot |
|---|---|---|
| P | 0 | none |
| R | 2 | P |
| Q | 3 | R |
| S | 8 | Q |
| T | 10 | S |
| U | 13 | T |

- Q: 3 via R (\(2 + 1\)), which is shorter than 4 directly from P [B1]
- S: 8 via Q (\(3 + 5\)), shorter than 10 via R (\(2 + 8\)) [B1]
- T: 10 via S (\(8 + 2\)), shorter than 12 via R (\(2 + 10\)) [B1]
- U: 13 via T (\(10 + 3\)), shorter than 14 via S (\(8 + 6\)) [B1]

(b)

- the route is P, R, Q, S, T, U (found by following the previous depots back from U) [B1]
- its length is 13 km [B1]

(c)

- supervised learning, because the training photographs are labelled with the correct answer [B1]
- back propagation works out the error between the network's output and the correct output, and uses it to adjust the weights (working back from the output layer) so that the error is reduced [B1]
:::

:::try
Q: [6 marks] (#cs.adts) A museum stores the catalogue numbers of its exhibits in a binary tree held in three global arrays. The value 0 in a pointer means there is no node. `RootPointer` holds the index of the root node, and the node at index 7 has not been used.

| Index | `LeftPtr` | `Data` | `RightPtr` |
|---|---|---|---|
| 1 | 2 | 40 | 3 |
| 2 | 5 | 25 | 4 |
| 3 | 6 | 60 | 0 |
| 4 | 0 | 31 | 0 |
| 5 | 0 | 18 | 0 |
| 6 | 0 | 52 | 0 |
| 7 | 0 | | 0 |

`RootPointer` is 1.

(a) The function `FindNode` is called with the target 52 and then with the target 35. For each call, write the indexes of the nodes that are visited, in order, and the value returned. The function returns the index of the node that holds the target, or 0 if the target is not in the tree. [2]

(b) Complete the pseudocode of the function by writing the missing items. [4]

```pseudocode
FUNCTION FindNode(Target : INTEGER) RETURNS INTEGER
   DECLARE Current : INTEGER
   Current ← ........
   WHILE Current <> 0 AND ........
      IF Target < Data[Current] THEN
         Current ← ........
      ELSE
         Current ← ........
      ENDIF
   ENDWHILE
   RETURN ........
ENDFUNCTION
```
A: (a)

- target 52: nodes 1, 3 and 6 are visited, and 6 is returned [B1]
- target 35: nodes 1, 2 and 4 are visited, and 0 is returned [B1]

(b)

```pseudocode
FUNCTION FindNode(Target : INTEGER) RETURNS INTEGER
   DECLARE Current : INTEGER
   Current ← RootPointer
   WHILE Current <> 0 AND Data[Current] <> Target
      IF Target < Data[Current] THEN
         Current ← LeftPtr[Current]
      ELSE
         Current ← RightPtr[Current]
      ENDIF
   ENDWHILE
   RETURN Current
ENDFUNCTION
```

- `RootPointer` [B1]
- `Data[Current] <> Target` (the test that Current is not 0 is written first, so no array element 0 is read) [B1]
- `LeftPtr[Current]` in the first branch and `RightPtr[Current]` in the second [B1]
- `Current` returned (the index of the node, or 0 when the search ends at no node) [B1]
:::

:::try
Q: [5 marks] (#cs.oop) A concert hall sells tickets. The class diagrams show two classes. A `VIPTicket` is a kind of `Ticket`.

| Ticket |
|---|
| Seat : STRING |
| Price : REAL |
| NEW(GivenSeat : STRING, GivenPrice : REAL) |
| GetPrice() : REAL |

| VIPTicket (inherits from Ticket) |
|---|
| Lounge : BOOLEAN |
| NEW(GivenSeat : STRING, GivenPrice : REAL, GivenLounge : BOOLEAN) |

(a) Write pseudocode for the class `Ticket`. The attributes are private and `NEW` is the constructor. [3]

(b) Write pseudocode for the class `VIPTicket`. [2]
A: (a)

```pseudocode
CLASS Ticket
   PRIVATE Seat : STRING
   PRIVATE Price : REAL
   PUBLIC PROCEDURE NEW(GivenSeat : STRING, GivenPrice : REAL)
      Seat ← GivenSeat
      Price ← GivenPrice
   ENDPROCEDURE
   PUBLIC FUNCTION GetPrice() RETURNS REAL
      RETURN Price
   ENDFUNCTION
ENDCLASS
```

- `CLASS Ticket` and `ENDCLASS`, with both attributes declared `PRIVATE` with their types [B1]
- the constructor `NEW` with the two parameters, assigning them to the attributes [B1]
- `GetPrice` as a function `RETURNS REAL` that returns `Price` [B1]

(b)

```pseudocode
CLASS VIPTicket INHERITS Ticket
   PRIVATE Lounge : BOOLEAN
   PUBLIC PROCEDURE NEW(GivenSeat : STRING, GivenPrice : REAL, GivenLounge : BOOLEAN)
      SUPER.NEW(GivenSeat, GivenPrice)
      Lounge ← GivenLounge
   ENDPROCEDURE
ENDCLASS
```

- `CLASS VIPTicket INHERITS Ticket` with `PRIVATE Lounge : BOOLEAN` [B1]
- the constructor with three parameters that calls `SUPER.NEW(GivenSeat, GivenPrice)` and then assigns `Lounge` [B1]
:::

:::try
Q: [8 marks] (#cs.paradigms) An animal shelter keeps these clauses in a knowledge base.

| Clause | Meaning |
|---|---|
| 1 `person(zara).` | Zara is a person |
| 2 `person(kwame).` | Kwame is a person |
| 3 `person(ines).` | Ines is a person |
| 4 `pet(milo).` | Milo is a pet at the shelter |
| 5 `pet(luna).` | Luna is a pet at the shelter |
| 6 `pet(biscuit).` | Biscuit is a pet at the shelter |
| 7 `pet(pepper).` | Pepper is a pet at the shelter |
| 8 `allergic(zara, milo).` | Zara is allergic to Milo |
| 9 `allergic(kwame, luna).` | Kwame is allergic to Luna |
| 10 `allergic(kwame, pepper).` | Kwame is allergic to Pepper |
| 11 `allergic(ines, biscuit).` | Ines is allergic to Biscuit |
| 12 `visited(zara, luna).` | Zara has visited Luna |
| 13 `visited(ines, milo).` | Ines has visited Milo |
| 14 `visited(kwame, biscuit).` | Kwame has visited Biscuit |
| 15 `visited(ines, pepper).` | Ines has visited Pepper |

(a) Omar is a new person. He has visited Rosie, a new pet at the shelter. Write three clauses to record this. [3]

(b) Using the variable X, the goal `allergic(kwame, X)` returns X = luna, pepper. Write the result returned by the goal `visited(ines, X)`. [1]

(c) A person may adopt a pet if the person is a person, the pet is a pet and the person is not allergic to the pet. Complete the rule. [4]

`may_adopt(Person, Pet)`
`IF`
A: One possible answer for (a) and (c):

```text
person(omar).
pet(rosie).
visited(omar, rosie).
may_adopt(Person, Pet) IF person(Person) AND pet(Pet) AND NOT allergic(Person, Pet).
```

- (a) `person(omar).` [B1]
- (a) `pet(rosie).` [B1]
- (a) `visited(omar, rosie).` with the person first and the pet second, as in the table [B1]
- (b) X = milo, pepper (clauses 13 and 15, in that order) [B1]
- (c) `person(Person)` and `pet(Pet)` as conditions joined by `AND` [B1]
- (c) `NOT allergic(Person, Pet)` [B1]
- (c) the `NOT` condition last, using the same variables as the head [B1]
- (c) the head `may_adopt(Person, Pet)` followed by `IF`, with every condition joined by `AND` (the comma form is also accepted) [B1]
:::

Next: [Mock Paper 4: Practical](#cs.mock.p4)
