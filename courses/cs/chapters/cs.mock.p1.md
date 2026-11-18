@chapter cs.mock.p1
@title Mock Paper 1: Theory Fundamentals
@level mock
@paper CAIE 9618 Paper 1
@time 1 h 30 min
@summary A full-length Paper 1 mock: nine scenario questions worth 75 marks that cover sections 1 to 8, from number systems, images, sound and compression, through networks, hardware, logic circuits, the processor and an assembly trace, system software, security and data integrity, to ethics and a relational database with SQL. Every answer is a full mark scheme with one mark point per mark.

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
Q: [8 marks] (#cs.data) A weather station in Quito records readings from its sensors as binary numbers.

(a) A temperature change of −45 is stored as an 8-bit two's complement integer. Show the 8-bit two's complement representation of −45. [2]

(b) Two stored values, 01101001 and 00110111, are added using 8-bit two's complement integers. Show the addition and state, with a reason, whether overflow has occurred. [3]

(c) The station stores the rainfall total 2058 millimetres in binary coded decimal (BCD), using four bits for each digit. Write the BCD representation. [2]

(d) State one practical use of BCD. [1]
A: (a)

- 45 in 8-bit binary is 00101101 [B1]
- inverting gives 11010010 and adding 1 gives 11010011 [B1]

(b) The addition, column by column from the right, with the carries:

```text
    0 1 1 0 1 0 0 1     (105)
  + 0 0 1 1 0 1 1 1     (55)
  -----------------
    1 0 1 0 0 0 0 0
```

- the result is 10100000 [B1]
- overflow has occurred [B1]
- two positive numbers (leftmost bit 0) have given a result with leftmost bit 1, which is negative; the true sum, 160, is greater than 127, the largest 8-bit two's complement number [B1]

(c)

- each digit is written in its own four bits: 2 is 0010, 0 is 0000, 5 is 0101 and 8 is 1000 [B1]
- the whole value is 0010 0000 0101 1000 [B1]

(d)

- a digital display (a clock, a calculator or a meter) that shows each decimal digit separately [B1] (accept: financial amounts, where decimal digits must be stored exactly)
:::

:::try
Q: [8 marks] (#cs.media) A museum in Cairo scans paintings and records tour guides.

(a) A scanned painting is stored as a bitmap 1024 pixels wide and 512 pixels high, with a colour depth of 24 bits. Calculate the file size in mebibytes (MiB). Ignore the file header and show your working. [3]

(b) A guide's voice message lasts 30 seconds. It is recorded with a sampling rate of 8000 samples per second and a sampling resolution of 16 bits, on one channel. Calculate the size of the sound file in kilobytes (kB, where 1 kB = 1000 bytes). Show your working. [3]

(c) One row of 24 pixels in a simple two-colour image is shown. W is a white pixel and B is a black pixel.

`WWWWWWWWWBBBWWWWWWWWBBBB`

Show the row after run-length encoding (RLE), writing each run as the number of pixels followed by the colour letter. [2]
A: (a)

- number of bits: 1024 × 512 × 24 [B1]
- divide by 8 to give bytes: \(1024 \times 512 \times 24 \div 8 = 1\,572\,864\) bytes [B1]
- divide by \(1024 \times 1024\) to give 1.5 MiB [B1]

(b)

- number of bits: 8000 × 16 × 30 [B1]
- \(8000 \times 16 \times 30 = 3\,840\,000\) bits, divided by 8 gives 480 000 bytes [B1]
- divide by 1000 to give 480 kB [B1]

(c) The row is `9W3B8W4B`.

- the first two runs are correct (9W then 3B) [B1]
- all four runs are correct, in order (8W then 4B) [B1]
:::

:::try
Q: [8 marks] (#cs.networks) A medical centre in Windhoek has 30 computers in one building. The computers are connected in a star topology. The centre's website is hosted on the internet.

(a) Describe how a data packet sent from one computer to another travels in the star network. [3]

(b) The centre considered a bus topology. Justify the choice of a star topology instead. [2]

(c) A receptionist types the web address of the centre's website into a browser. The browser needs the IP address of the web server. Describe how the Domain Name Service (DNS) provides it. [3]
A: (a)

- the sending computer sends the packet along its own cable to the central switch [B1]
- the switch reads the destination address in the packet [B1]
- the switch sends the packet along only the cable to the destination computer [B1] (accept: a hub sends it to every computer, and only the destination accepts it)

(b)

- a break in one cable stops only the one computer connected to it, so the other 29 keep working (in a bus, a break in the main cable can stop the whole network) [B1]
- on a switched star each computer has its own cable, so there are fewer collisions and the network stays fast when many staff use it [B1]

(c)

- the browser sends the domain name of the website to a DNS server [B1]
- the DNS server looks up the domain name in its database and finds the matching IP address (if it does not hold it, it asks another DNS server) [B1]
- the IP address is returned to the browser, which uses it to contact the web server [B1]
:::

:::try
Q: [5 marks] (#cs.hardware) A digital camera in a tourist shop in Cusco stores photographs on a flash memory card. The camera's processor runs a program that is stored in ROM.

(a) Describe how a flash memory card stores data and how it keeps the data when the camera is switched off. [3]

(b) State what the ROM holds and explain why the camera also needs RAM. [2]
A: (a)

- the card is made of a grid of flash memory cells (transistors), using NAND or NOR technology [B1]
- each cell has a floating gate that can trap electrons: charge trapped or not trapped represents a binary 1 or 0 [B1]
- the trapped charge stays in the gate without power, so the data is kept when the camera is off (the memory is non-volatile) [B1]

(b)

- the ROM holds the camera's start-up program (the firmware), which is read when the camera is switched on and is not changed in use [B1]
- RAM holds the photograph being processed, the settings and the working data of the program while the camera is on, because RAM can be written to as well as read [B1]
:::

:::try
Q: [8 marks] (#cs.logic) A logic circuit has three inputs, A, B and C, and one output, X. P and Q are the outputs of the first two gates.

<figure class="fig"><svg viewBox="0 0 400 165" role="img" aria-label="Logic circuit with inputs A, B and C and output X. A and B feed an XOR gate whose output is labelled P. B and C feed a NOR gate whose output is labelled Q. B is joined to both gates by a dot. P and Q feed an OR gate whose output is X."><g transform="translate(110 30)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><path class="ln" fill="none" d="M-6 0 C1 12 1 28 -6 40"/></g><g transform="translate(110 100)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><g transform="translate(280 65)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/></g><text class="tl tb" x="12" y="44">A</text><text class="tl tb" x="12" y="89">B</text><text class="tl tb" x="12" y="134">C</text><polyline class="ln" fill="none" points="30,40 108,40"/><polyline class="ln" fill="none" points="30,85 70,85"/><polyline class="ln" fill="none" points="70,85 70,60 108,60"/><polyline class="ln" fill="none" points="70,85 70,110 114,110"/><circle class="fi" cx="70" cy="85" r="3.5"/><polyline class="ln" fill="none" points="30,130 114,130"/><polyline class="ln" fill="none" points="152,50 240,50 240,75 284,75"/><polyline class="ln" fill="none" points="160,120 250,120 250,95 284,95"/><polyline class="ln" fill="none" points="322,85 372,85"/><text class="tl tb" x="378" y="89">X</text><text class="tl" x="190" y="40">P</text><text class="tl" x="196" y="140">Q</text></svg><figcaption>The circuit for Question 5. The dot on B shows that B is joined to both gates. P and Q label the wires between the gates.</figcaption></figure>

(a) Write the logic expression for the circuit, in terms of A, B and C. [3]

(b) Complete the truth table for the circuit. The columns P and Q are for your working. [3]

| A | B | C | P | Q | X |
|---|---|---|---|---|---|
| 0 | 0 | 0 | | | |
| 0 | 0 | 1 | | | |
| 0 | 1 | 0 | | | |
| 0 | 1 | 1 | | | |
| 1 | 0 | 0 | | | |
| 1 | 0 | 1 | | | |
| 1 | 1 | 0 | | | |
| 1 | 1 | 1 | | | |

(c) A conveyor motor M is switched on (M = 1) when the main switch S is on (S = 1) and either the guard G is closed (G = 1) or the override O is pressed (O = 1). Write a logic expression for M. [2]
A: (a) `X = (A XOR B) OR (B NOR C)`

- `A XOR B` for the first gate, P [B1]
- `B NOR C` for the second gate, Q (accept `NOT (B OR C)`) [B1]
- the two joined with OR to give X [B1]

(b)

| A | B | C | P | Q | X |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 |

- the P column is correct: 0 0 1 1 1 1 0 0 [B1]
- the Q column is correct: 1 0 0 0 1 0 0 0 [B1]
- the X column is correct for the candidate's P and Q (P OR Q) [B1]

(c) `M = S AND (G OR O)`

- `G OR O` bracketed, for the guard or the override [B1]
- joined to S with AND (accept `(S AND G) OR (S AND O)`) [B1]
:::

:::try
Q: [11 marks] (#cs.assembly) A processor has a program counter (PC), a current instruction register (CIR), an accumulator (ACC) and an index register (IX).

(a) State the purpose of the PC and of the CIR. [2]

(b) Explain how a large cache memory can improve the performance of the processor. [2]

(c) The assembly language program below is stored from address 100. It uses the instructions shown in the table.

| Instruction | Explanation |
|---|---|
| `LDR #n` | Load the number n into IX |
| `LDX <address>` | Indexed addressing: the address used is the given address plus the contents of IX. Copy the contents of that address to ACC |
| `CMP #n` | Compare the contents of ACC with the number n |
| `JPE <address>` | Following a compare instruction, jump to the address if the compare was True |
| `AND Bn` | Bitwise AND of the contents of ACC with the binary number n |
| `OUT` | Output to the screen the character whose ASCII value is in ACC |
| `INC <register>` | Add 1 to the contents of the register (ACC or IX) |
| `JMP <address>` | Jump to the address |
| `END` | Return control to the operating system |

```text
100   LDR #0
101   LDX 200
102   CMP #0
103   JPE 108
104   AND B11011111
105   OUT
106   INC IX
107   JMP 101
108   END
```

Address 200 holds 103 (the ASCII value of the letter g) and address 201 holds 0. The ASCII values of the capital letters start at 65 for A.

(i) Complete the trace table. Write a value in a column only on the row where the register changes or a character is output. [4]

| Instruction address | ACC | IX | OUTPUT |
|---|---|---|---|
| 100 | | | |
| 101 | | | |
| 102 | | | |
| 103 | | | |
| 104 | | | |
| 105 | | | |
| 106 | | | |
| 107 | | | |
| 101 | | | |
| 102 | | | |
| 103 | | | |
| 108 | | | |

(ii) State what the program does. [1]

(iii) Explain why the instruction at address 101 uses indexed addressing. [2]
A: (a)

- the PC holds the address of the next instruction to be fetched [B1]
- the CIR holds the instruction that is currently being decoded and executed [B1]

(b)

- the cache is fast memory close to the processor that holds frequently used (or recently used) instructions and data [B1]
- the processor finds them there without waiting for the slower main memory, so fewer fetches from RAM are needed and instructions run sooner [B1]

(c)(i)

| Instruction address | ACC | IX | OUTPUT |
|---|---|---|---|
| 100 | | 0 | |
| 101 | 103 | | |
| 102 | | | |
| 103 | | | |
| 104 | 71 | | |
| 105 | | | G |
| 106 | | 1 | |
| 107 | | | |
| 101 | 0 | | |
| 102 | | | |
| 103 | | | |
| 108 | | | |

- IX is 0 after address 100 and 1 after address 106 [B1]
- ACC is 103 at the first address 101 [B1]
- ACC is 71 at address 104, and G is the only output (at address 105) [B1]
- ACC is 0 at the second address 101, with no other cell filled [B1]

(ii)

- it outputs the letters stored from address 200 onwards as capital letters, stopping at the first 0 [B1] (accept: it converts lower case letters to upper case and displays them)

(iii)

- the address used is 200 plus the contents of IX [B1]
- adding 1 to IX each time round the loop makes the same instruction read the next item (201, 202, …) [B1]
:::

:::try
Q: [9 marks] (#cs.software) A software company in Pune writes a records program for a hospital.

(a) The program runs under an operating system. Describe two tasks that the operating system carries out as part of memory management. [2]

(b) The programmers use an integrated development environment (IDE) to find a logic error. Describe how each of these three features helps to find the error: single stepping, a breakpoint and a variable report window. [3]

(c) The hospital stores patient records on a network. Describe how each of these helps to keep the records secure: a firewall and encryption. [4]
A: (a) Any two of these points, one mark each:

- allocates areas of memory to each program that is running
- stops one program from overwriting the memory used by another
- keeps track of which areas of memory are free and which are in use, and frees the memory when a program ends
- moves data between RAM and secondary storage when RAM is full (virtual memory)

Two correct points [B1] [B1]

(b)

- single stepping runs one line (or statement) at a time, so the programmer can see where the program first behaves wrongly [B1]
- a breakpoint stops the program at a chosen line, so the programmer can inspect the program's state at that point without stepping through all the earlier lines [B1]
- the variable report window shows the current value of the variables, so a wrong value can be seen as soon as it appears [B1]

(c)

- a firewall monitors the data coming into and out of the network [B1]
- it blocks data that does not meet the rules set (for example from a certain IP address or on a certain port), so unauthorised users cannot reach the records [B1]
- encryption scrambles the records, using an algorithm and a key, into cipher text [B1]
- if the data is intercepted or stolen, it cannot be understood without the key to decrypt it [B1]
:::

:::try
Q: [7 marks] (#cs.security) A hospital in Dhaka sends a block of data between two computers. Each byte has seven data bits and one parity bit, which is the leftmost bit. Even parity is used. After the four data bytes, a fifth byte, the parity byte, holds the even parity of each column.

One bit changed during transmission. The block that was received is shown.

| | Parity bit | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 |
|---|---|---|---|---|---|---|---|---|
| Byte 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| Byte 2 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 |
| Byte 3 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Byte 4 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| Parity byte | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

(a) Identify the byte and the bit that changed. [2]

(b) Explain how the parity bits and the parity byte allow you to find the bit that changed. [2]

(c) An open-source licence is used for the hospital's records software. Describe two things that an open-source licence allows users to do with the software. [2]

(d) State one difference between an open-source licence and a shareware licence. [1]
A: (a)

- the error is in Byte 3 [B1]
- the changed bit is bit 4 (it should be 0 and was received as 1) [B1]

(b)

- the number of 1s in Byte 3 is odd (5), so the row parity is wrong; every other byte has an even number of 1s [B1]
- the number of 1s in the bit 4 column is odd (3), so the column parity is wrong; the changed bit is where the wrong row and the wrong column meet [B1]

(c) Any two of these points, one mark each:

- run the software for any purpose
- read, study and change the source code
- pass on copies of the software to other people
- distribute the changed version

Two correct points [B1] [B1]

(d)

- an open-source licence gives access to the source code, but shareware does not (accept: shareware is free only for a trial period or with limited features, then the user must pay) [B1]
:::

:::try
Q: [11 marks] (#cs.databases) A veterinary clinic in Colombo records every visit in one table. The primary key is VisitID.

VISIT(VisitID, VisitDate, PetID, PetName, Species, OwnerID, OwnerName, OwnerPhone, VetID, VetName, Fee)

Each pet has one owner, an owner may have several pets, and a vet treats many pets.

(a) Explain why the table is not in third normal form (3NF). [2]

(b) Design a set of tables in 3NF for this data. For each table give its name and its fields, show the primary key in bold and mark each foreign key with an asterisk (\*). [4]

(c) After normalisation, part of the database is shown.

VET

| VetID | VetName |
|---|---|
| V1 | Dr Silva |
| V2 | Dr Perera |
| V3 | Dr Rajan |

VISIT

| VisitID | VisitDate | PetID | VetID | Fee |
|---|---|---|---|---|
| 1 | 2027-03-02 | P1 | V2 | 1500 |
| 2 | 2027-03-02 | P3 | V1 | 2500 |
| 3 | 2027-03-04 | P2 | V1 | 3200 |
| 4 | 2027-03-05 | P1 | V3 | 2200 |
| 5 | 2027-03-09 | P4 | V2 | 4000 |

Write an SQL query that outputs the visit date, the vet's name and the fee of every visit where the fee is more than 2000, in order of visit date, earliest first. [5]
A: (a)

- fields such as PetName, Species and OwnerID depend on PetID, OwnerName and OwnerPhone depend on OwnerID, and VetName depends on VetID: they depend on another non-key field, not on the key VisitID [B1]
- in 3NF no non-key field may depend on another non-key field (this is a transitive dependency), so the table is not in 3NF and the pet, owner and vet details are repeated for every visit [B1]

(b) One possible design:

| Table | Fields |
|---|---|
| OWNER | **OwnerID**, OwnerName, OwnerPhone |
| PET | **PetID**, PetName, Species, OwnerID\* |
| VET | **VetID**, VetName |
| VISIT | **VisitID**, VisitDate, PetID\*, VetID\*, Fee |

- OWNER table with OwnerID as the primary key [B1]
- PET table with PetID as the primary key and OwnerID as a foreign key [B1]
- VET table with VetID as the primary key [B1]
- VISIT table with VisitID as the primary key and PetID and VetID as foreign keys [B1]

(c)

```text
SELECT VISIT.VisitDate, VET.VetName, VISIT.Fee
FROM VISIT
INNER JOIN VET ON VISIT.VetID = VET.VetID
WHERE VISIT.Fee > 2000
ORDER BY VISIT.VisitDate
```

- `SELECT` with the three fields [B1]
- `FROM VISIT` [B1]
- `INNER JOIN VET ON VISIT.VetID = VET.VetID` (the join on the matching VetID) [B1]
- `WHERE VISIT.Fee > 2000` [B1]
- `ORDER BY VISIT.VisitDate` (earliest first is the default) [B1]

For the data shown, the query outputs four rows: 2027-03-02, Dr Silva, 2500; 2027-03-04, Dr Silva, 3200; 2027-03-05, Dr Rajan, 2200; 2027-03-09, Dr Perera, 4000.
:::

Next: [Mock Paper 2: Problem-solving and Programming](#cs.mock.p2)
