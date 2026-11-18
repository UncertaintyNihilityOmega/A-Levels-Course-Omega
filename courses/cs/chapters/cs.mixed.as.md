@chapter cs.mixed.as
@title Mixed practice: AS (Papers 1 and 2)
@level guide
@paper CAIE 9618 Papers 1 and 2
@time 6–8 hours
@summary Eighteen Paper 1 style questions across sections 1 to 8 and twelve Paper 2 style questions across sections 9 to 12, in mixed order, with mark points and full model pseudocode, plus synoptic items that join topics and a quiz on the misconceptions that cost AS students marks.

:::why
In a real exam the topics do not arrive in chapter order. A question on binary can sit next to one on networks, and a Paper 2 question can ask for a validation function that uses string functions, a loop and a check digit at once. Practising one chapter at a time hides whether you can recognise what a question is asking. This chapter mixes everything, so you practise the skill the exam really tests: choosing the right idea quickly.
:::

## How to use this chapter

Before you start, read [Paper 1 guide: Theory Fundamentals](#cs.exam.p1) and [Paper 2 guide: Problem-solving and Programming](#cs.exam.p2). Every question carries a **revise link**: use it after you have tried the question, not before.

:::steps
1. **Choose a set** and a block of time. The Paper 1 style set is worth 90 marks, which is \(90 \times 1.2 = 108\) minutes at the Paper 1 pace of 1.2 minutes a mark. The Paper 2 style set is worth 69 marks, which is \(69 \times 1.6 = 110.4\) minutes, about 110, at the Paper 2 pace of 1.6 minutes a mark. Do not do both in one sitting.
2. **Write the answers by hand,** on paper, before you open any answer. For Paper 2 style questions, write in pseudocode and nothing else.
3. **Open one answer at a time.** Mark each mark point, in a different colour, and write the total beside the question.
4. **Record the section** of every question you lost marks on, then use its revise link and redo the question a few days later.
:::

The stars show difficulty: ★ one method, ★★ two steps, ★★★ several parts or topics joined together. The questions are in mixed order on purpose. The Paper 2 style questions refer to "the insert": use the list of functions and operators in the [Paper 2 guide](#cs.exam.p2) in its place.

:::exam Marking your own work
Give a mark only when the answer **says** the mark point, in your own words or the mark scheme's. A point that is nearly there earns nothing. If you cannot decide, do not give the mark. You will learn more from an honest 60 than from a generous 70.
:::

:::try Paper 1 style: sections 1 to 8
Q: [6 marks] ★★ (#cs.security) A warehouse in Kumasi gives every product a five-digit code followed by a modulo-11 check digit. The weights for the five digits are 6, 5, 4, 3 and 2 (from left to right), and the check digit is \(11 - \text{remainder}\), where the remainder is the total divided by 11.

(a) Calculate the check digit for the code 41627. Show your working. [4]

(b) A clerk enters the six-digit code 416724, where the last digit is the check digit with weight 1. Show whether the system accepts the code. [2]
H: Multiply each digit by its weight, then add the products.
H: For (b), the six digits have weights 6, 5, 4, 3, 2 and 1; a valid code has a total that is a multiple of 11.
A: (a) The products are \(4 \times 6 = 24\), \(1 \times 5 = 5\), \(6 \times 4 = 24\), \(2 \times 3 = 6\) and \(7 \times 2 = 14\). [M1]

The total is \(24 + 5 + 24 + 6 + 14 = 73\). [A1]

\(73 = 11 \times 6 + 7\), so the remainder is 7. [M1]

The check digit is \(11 - 7 = 4\), so the full code is 416274. [A1]

(b) The total with the check digit weighted 1 is [M1]

\[4 \times 6 + 1 \times 5 + 6 \times 4 + 7 \times 3 + 2 \times 2 + 4 \times 1 = 82\]

\(82 = 11 \times 7 + 5\), which is not a multiple of 11, so the code is rejected. [A1] (A transposition of two digits is caught because the weights are different.)

Q: [7 marks] ★★ (#cs.data) (a) Convert the denary number 181 into an 8-bit binary number. [2]

(b) Convert the same number into hexadecimal. [1]

(c) A processor stores whole numbers in 8-bit two's complement. Show how it calculates \(52 - 75\) by adding, and state the answer as a denary number. [4]
H: Write 181 as a sum of powers of 2: start with 128.
H: Subtract by adding the two's complement of 75: invert, then add 1.
A: (a) \(181 = 128 + 32 + 16 + 4 + 1\) (or repeated division by 2 with the remainders read upwards). [M1] The binary number is 10110101. [A1]

(b) Split into groups of four bits: 1011 is B and 0101 is 5, so the hexadecimal number is B5. [B1]

(c) 52 in binary is 00110100. [B1]

75 is 01001011. Inverting gives 10110100, and adding 1 gives 10110101, which is \(-75\). [B1]

Adding: 00110100 + 10110101 = 11101001 (the carry out of the leftmost column is not needed). [B1]

The leftmost bit is 1, so the number is negative: inverting 11101001 gives 00010110, and adding 1 gives 00010111 which is 23. The answer is \(-23\). [B1]

Q: [5 marks] ★★ (#cs.logic) The vent of a greenhouse opens (V = 1) when the temperature is too high (T = 1) and it is not raining (R = 0). The vent also opens whenever the manual switch is on (M = 1).

(a) Write a logic expression for V in terms of T, R and M. [2]

(b) Complete the truth table for the expression. [3]

| T | R | M | V |
|---|---|---|---|
| 0 | 0 | 0 | |
| 0 | 0 | 1 | |
| 0 | 1 | 0 | |
| 0 | 1 | 1 | |
| 1 | 0 | 0 | |
| 1 | 0 | 1 | |
| 1 | 1 | 0 | |
| 1 | 1 | 1 | |
A: (a) `V = (T AND NOT R) OR M`

- `T AND NOT R` for "too high and not raining" [B1]
- `OR M` joining the manual switch [B1]

(b)

| T | R | M | V |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

- the four rows with M = 1 all give V = 1 [B1]
- the row T = 1, R = 0, M = 0 gives V = 1 [B1]
- the other three rows (M = 0 with T = 0, or with R = 1) give V = 0 [B1]

Q: [4 marks] ★★ (#cs.networks) A language school in Madrid has 120 staff and students who use the school's computers for timetables, student records and shared teaching files. The school is deciding between a client-server network and a peer-to-peer network. Justify the use of a client-server network. [4]
H: Use the numbers in the scenario: 120 people, shared records.
A: One mark for each developed point, linked to the school.

- The server stores the timetables, records and teaching files in one place, so all 120 users see the same up-to-date version [B1]
- Backups are made from one place (the server), so student records are not lost if a computer fails [B1]
- User accounts and access rights are managed centrally, so only administrative staff can see student records [B1]
- The server is a powerful computer built to answer many requests at once, whereas 120 users in a peer-to-peer network would be sharing files from ordinary computers that slow down while they are used for other work [B1]

Q: [5 marks] ★★ (#cs.media) A game studio in Seoul stores a sprite sheet as a bitmap 256 pixels wide and 128 pixels high with a colour depth of 16 bits. Ignore the file header.

(a) Calculate the size of the file in KiB, showing your working. [3]

(b) The studio changes the colour depth to 8 bits. State the new file size and one effect on the image. [2]
H: Write each number as a power of 2.
A: (a) Size in bits \(= 256 \times 128 \times 16 = 2^{8} \times 2^{7} \times 2^{4} = 2^{19}\). [M1]

Divide by 8 to get bytes: \(2^{19} \div 2^{3} = 2^{16} = 65\,536\) bytes. [M1]

Divide by 1024 (\(2^{10}\)) to get KiB: \(2^{16} \div 2^{10} = 2^{6} = 64\) KiB. [A1]

(b) The new file size is 32 KiB, half the original, because each pixel needs half as many bits. [B1]

Fewer colours are available (256 instead of 65 536), so the image may look less smooth or realistic, with visible bands of colour. [B1]

Q: [4 marks] ★★ (#cs.software) A games studio in Montreal releases a game to players who have no programming tools on their computers. Justify the use of a compiler, rather than an interpreter, to translate the game. [4]
A: One mark for each of:

- A compiler translates the whole program once into machine code, so the game runs without any translation while it is played [B1]
- The machine code runs faster, so the graphics and controls respond quickly [B1]
- Players only need the executable file, not the compiler or the source code, so nothing has to be installed [B1]
- The source code is not given to the players, so other companies cannot copy or change the game [B1]

(All syntax errors being reported before the game is released is a further correct point.)

Q: [4 marks] ★ (#cs.processor) The fetch stage of the fetch-execute cycle can be written in register transfer notation. The first step is `MAR ← [PC]`.

(a) Write the other three steps of the fetch stage, in order. [3]

(b) State what is held in the CIR at the end of the fetch stage. [1]
A: (a)

```text
PC ← [PC] + 1
MDR ← [[MAR]]
CIR ← [MDR]
```

- `PC ← [PC] + 1` [B1]
- `MDR ← [[MAR]]` (the contents of the memory location whose address is in the MAR) [B1]
- `CIR ← [MDR]` [B1]

(b) The instruction that has just been fetched, which is to be decoded and executed. [B1]

Q: [6 marks] ★★★ (#cs.databases) A wholesaler in Mombasa stores order lines in one table, ORDERITEM(**OrderID**, **ItemCode**, ItemName, Quantity, CustomerID, CustomerName). The primary key is the pair of fields OrderID and ItemCode.

(a) Explain why the table is not in second normal form. [2]

(b) Write a design in third normal form. Show each table as TABLE(**PrimaryKey**, Field, ForeignKey\*). [4]
H: Ask of every field: does it depend on the whole key, part of it, or on another non-key field?
A: (a) ItemName depends only on ItemCode [B1], which is part of the composite primary key, not on the whole key (OrderID and ItemCode together) [B1].

(b)

- ITEM(**ItemCode**, ItemName) [B1]
- CUSTOMER(**CustomerID**, CustomerName) [B1]
- ORDERS(**OrderID**, CustomerID\*) with CustomerID as a foreign key [B1]
- ORDERLINE(**OrderID**\*, **ItemCode**\*, Quantity), where the two fields together form the primary key and each is a foreign key [B1]

(CustomerName depends on CustomerID and CustomerID depends on OrderID, so both must leave the original table. Accept the order table called ORDER or an equivalent name.)

Q: [5 marks] ★★ (#cs.hardware) A greenhouse in Nairobi has a computer that keeps the temperature at or above 18 degrees Celsius. Describe how the system uses a sensor, the processor and an actuator, with feedback, to do this. [5]
A: One mark for each of:

- A temperature sensor measures the temperature and produces an analogue signal [B1]
- An analogue-to-digital converter (ADC) changes the signal into digital data for the processor [B1]
- The processor compares the reading with the stored value of 18 [B1]
- If the reading is below 18, the processor sends a signal to the actuator (the heater, switched on through a relay or a digital-to-analogue converter) [B1]
- The sensor keeps measuring, so the new temperature is fed back to the processor, and the heater is switched off when the reading is at or above 18 [B1] (this is feedback)

Q: [4 marks] ★ (#cs.media) A row of 15 pixels is stored as the letters AAAABBBCCCCCCAA.

(a) Write the row using run-length encoding (RLE), with the count before the letter. [2]

(b) Explain why RLE makes the data larger for the row ABCABCABC. [2]
A: (a) `4A 3B 6C 2A`

- the four counts 4, 3, 6 and 2 [B1]
- each count with the correct letter [B1]

(b) Every run has a length of 1, so each pixel becomes a count and a value (`1A 1B 1C …`) [B1]. Each pixel is now stored with two items instead of one, so the encoded data is larger than the original [B1].

Q: [6 marks] ★★ (#cs.security) (a) Describe phishing. [2]

(b) Describe pharming. [2]

(c) State one way of reducing the risk of each of them. [2]
A: (a)

- A message, such as an email or a text, appears to come from a trusted organisation [B1]
- It persuades the user to follow a link to a fake website and to type in private details [B1]

(b)

- Malicious code on the user's computer, or a changed record on a DNS server, redirects the browser [B1]
- The user is sent to a fake website even though they typed the correct web address [B1]

(c)

- Phishing: do not click links in unexpected messages (go to the organisation's site by typing the address); check the sender's address [B1]
- Pharming: use anti-spyware or anti-virus software to find and remove the malicious code; check the website's address and security before entering details [B1]

Q: [8 marks] ★★★ (#cs.assembly) A pump controller has two bytes of memory. Location 150 is the status byte: bit 6 is 1 when the tank is empty. Location 151 is the control byte: bit 1 is the pump switch (1 means on). Bits are numbered from 0 at the right.

The program must switch the pump on when the tank is empty (bit 6 of location 150 is 1) and off when it is not. It must not change any other bit of location 151. The program starts at address 100. The instructions available are shown.

| Instruction | Explanation |
|---|---|
| `LDD <address>` | Load the contents of the address into ACC |
| `STO <address>` | Store the contents of ACC at the address |
| `AND Bn` | Bitwise AND of the contents of ACC with the binary number n |
| `OR Bn` | Bitwise OR of the contents of ACC with the binary number n |
| `CMP #n` | Compare the contents of ACC with the denary number n |
| `JPE <address>` | Following a compare instruction, jump to the address if the compare was True |
| `END` | Return control to the operating system |

(a) Write the program. [6]

(b) Location 150 holds 01001000 and location 151 holds 10100001. State the value in location 151 when the program ends, and explain your answer. [2]
H: Test bit 6 with a mask that has a 1 only in bit 6, then compare the result with 0.
H: Set a bit with OR and a mask with a 1 in that bit. Clear a bit with AND and a mask with a 0 in that bit.
A: (a) One possible program:

```text
100   LDD 150
101   AND B01000000
102   CMP #0
103   JPE 108
104   LDD 151
105   OR B00000010
106   STO 151
107   END
108   LDD 151
109   AND B11111101
110   STO 151
111   END
```

- `LDD 150` loads the status byte [B1]
- `AND B01000000` keeps only bit 6 [B1]
- `CMP #0` followed by `JPE` to the switch-off part (the result is 0 when the tank is not empty) [B1]
- switch-on part: load 151, `OR B00000010` and store it back [B1]
- switch-off part: load 151, `AND B11111101` and store it back [B1]
- `END` after the switch-on part, so it does not run on into the switch-off part, and `END` at the end [B1]

(Accept labels instead of addresses, and the two branches the other way round with `JPN`.)

(b) The value is 10100011. [B1] Bit 6 of 01001000 is 1, so the AND gives 01000000, the compare with 0 is False, the jump is not taken, and the OR sets bit 1 of 10100001 without changing any other bit. [B1]

Q: [5 marks] ★★ (#cs.internet) (a) State two differences between an IPv4 address and an IPv6 address. [2]

(b) Describe how the Domain Name Service (DNS) finds the IP address of a website when its address is typed into a browser. [3]
A: (a)

- IPv4 is 32 bits long and IPv6 is 128 bits long [B1]
- IPv4 is written as four denary numbers from 0 to 255 separated by full stops; IPv6 is written as eight groups of four hexadecimal digits separated by colons [B1]

(b)

- The browser extracts the domain name from the URL and sends it to a DNS server [B1]
- The DNS server looks up the domain name in its records and returns the matching IP address [B1]
- If the server does not hold the record, it asks another DNS server, until the address is found; the browser then uses the IP address to contact the web server [B1]

Q: [4 marks] ★★ (#cs.ethics) A programmer at a fitness-app company in Kampala discovers that the company is selling users' health records to an advertiser without asking the users.

(a) State two principles of professional ethics that the company breaches. [2]

(b) Describe what the programmer should do. [2]
A: (a)

- respect confidentiality and privacy: users' data is used for a purpose they did not agree to [B1]
- act in the public interest: the users' wellbeing and privacy are put second [B1]

(Being honest with users about what happens to their data is also correct. Any two principles earn the marks.)

(b)

- Raise the concern with a manager or the company's ethics or data protection officer, and refuse to take part in the sale [B1]
- If nothing is done, report it to a professional body such as the BCS or IEEE, or to the authority that regulates data protection [B1]

Q: [5 marks] ★★★ (#cs.sql) A food wholesaler stores two tables. CUSTOMER(**CustomerID**, CustomerName, City) and ORDERS(**OrderID**, CustomerID\*, Total). A small part of the data is shown.

| CustomerID | CustomerName | City |
|---|---|---|
| C1 | Amara Stores | Mombasa |
| C2 | Bashir Foods | Nairobi |
| C3 | Chege Traders | Mombasa |

| OrderID | CustomerID | Total |
|---|---|---|
| O1 | C1 | 250 |
| O2 | C2 | 120 |
| O3 | C1 | 80 |
| O4 | C3 | 300 |
| O5 | C2 | 60 |
| O6 | C3 | 45 |

Write an SQL query to show the name and the total value of all orders for each customer in Mombasa, in alphabetical order of customer name. State the output for the data shown. [5]
H: "For each" means GROUP BY; the name and the value come from different tables.
A:

```text
SELECT Customer.CustomerName, SUM(Orders.Total)
FROM Customer
INNER JOIN Orders ON Customer.CustomerID = Orders.CustomerID
WHERE Customer.City = 'Mombasa'
GROUP BY Customer.CustomerName
ORDER BY Customer.CustomerName;
```

- `SELECT` with the customer name and `SUM(Orders.Total)` [B1]
- `FROM Customer INNER JOIN Orders` with `ON Customer.CustomerID = Orders.CustomerID` [B1]
- `WHERE` on the city, with the text in quotes [B1]
- `GROUP BY` the customer name [B1]
- `ORDER BY` the customer name [B1]

Output:

| CustomerName | SUM(Orders.Total) |
|---|---|
| Amara Stores | 330 |
| Chege Traders | 345 |

Q: [4 marks] ★★ (#cs.processor) A user presses a key while a spreadsheet program is running. The key press generates an interrupt. Describe how the processor handles the interrupt. [4]
A: One mark for each of:

- At the end of the fetch-execute cycle, after the current instruction has finished, the processor detects the interrupt and checks its priority against the running program [B1]
- The contents of the registers, including the PC, are saved, usually on a stack [B1]
- The address of the interrupt service routine (ISR) is loaded into the PC, and the ISR runs [B1]
- When the ISR finishes, the saved register values are restored and the interrupted program carries on from where it stopped [B1]

Q: [4 marks] ★★ (#cs.hardware) A games console uses SRAM for the processor's cache and DRAM for its main memory. Explain why. [4]
A:

- SRAM is faster than DRAM because it does not need to be refreshed [B1], so it suits the cache, which the processor uses all the time [B1]
- DRAM is cheaper and stores more data in the same space [B1], so a large main memory can be built at a reasonable price; the data in it must be refreshed constantly, which makes it slower [B1]

Q: [4 marks] ★★ (#cs.software) A tablet runs a game, a music player and a messaging app at the same time.

(a) Describe two tasks the operating system carries out in memory management. [2]

(b) Describe two tasks the operating system carries out in file management. [2]
A: (a)

- allocating an area of RAM to each program when it starts [B1]
- stopping one program from overwriting the memory of another [B1]

(Freeing the memory when a program is closed, so it can be reused, is also correct.)

(b)

- organising files in folders (directories) with names and locations [B1]
- creating, copying, moving, renaming and deleting files, or controlling which users have access rights to each file [B1]
:::

## Synoptic items

Some of the best exam questions join two or three topics, and several are in these sets. In the Paper 1 style set, the pump controller question joins **bit manipulation and a control system**, the check-digit question joins **validation and arithmetic with remainders**, and the wholesaler's SQL query is written against the **normalised design** you met in the normalisation question. In the Paper 2 style set, the product-code function joins **string functions, a loop, a check digit and a function**. When you meet a question that seems to belong to two chapters, split it into its parts and tick off each topic in turn.

:::try Paper 2 style: sections 9 to 12
Q: [4 marks] ★ (#cs.algorithms) A program for a school in Accra stores the mathematics marks of 40 pupils (whole numbers from 0 to 100), calculates the mean mark and sets a flag to say whether the class has passed (a mean of at least 50). Complete the identifier table. [4]

| Identifier | Data type | Description |
|---|---|---|
| Marks | | the marks of the 40 pupils |
| Total | | the sum of all the marks |
| Average | | the mean mark |
| ClassPassed | | TRUE if the mean is at least 50 |
A: 

| Identifier | Data type | Description |
|---|---|---|
| Marks | `ARRAY[1:40] OF INTEGER` | the marks of the 40 pupils |
| Total | `INTEGER` | the sum of all the marks |
| Average | `REAL` | the mean mark |
| ClassPassed | `BOOLEAN` | TRUE if the mean is at least 50 |

- Marks: a one-dimensional array of 40 integers [B1]
- Total: INTEGER [B1]
- Average: REAL, because the mean has a fractional part [B1]
- ClassPassed: BOOLEAN [B1]

Q: [5 marks] ★★ (#cs.algorithms) The structured English below describes a program for a recycling centre in Lima.

1. Set Total to 0.0 and Count to 0.
2. Input the mass of a bag in kilograms (the value -1 means there are no more bags).
3. While the mass is not -1: add the mass to Total, add 1 to Count, and input the next mass.
4. If Count is greater than 0, output the mean mass (Total divided by Count). Otherwise output "No bags".

Write pseudocode for the algorithm. [5]
H: Input the first mass before the loop, and the next one at the end of the loop.
A: One possible answer:

```pseudocode
DECLARE Total, Mass, Mean : REAL
DECLARE Count : INTEGER

Total ← 0.0
Count ← 0
INPUT Mass
WHILE Mass <> -1
   Total ← Total + Mass
   Count ← Count + 1
   INPUT Mass
ENDWHILE
IF Count > 0 THEN
   Mean ← Total / Count
   OUTPUT Mean
ELSE
   OUTPUT "No bags"
ENDIF
```

- `Total` and `Count` initialised to 0.0 and 0 [B1]
- the first mass input before the loop [B1]
- a `WHILE` loop that stops when the mass is -1, with the mass added to `Total` and 1 added to `Count` [B1]
- the next mass input inside the loop, at the end [B1]
- `IF Count > 0` with the mean calculated and output, and `"No bags"` otherwise [B1]

Q: [5 marks] ★★ (#cs.testing) Complete the trace table for this pseudocode. Write a value only when the variable changes. [5]

```pseudocode
DECLARE Word, Result : STRING
DECLARE Index : INTEGER

Word ← "Level"
Result ← ""
FOR Index ← LENGTH(Word) TO 1 STEP -1
   Result ← Result & MID(Word, Index, 1)
NEXT Index
IF Result = Word THEN
   OUTPUT "Same"
ELSE
   OUTPUT "Different"
ENDIF
```

| Index | Result | OUTPUT |
|---|---|---|
| | | |
H: Comparisons of strings are case sensitive.
A: The loop counts down from 5 to 1 and joins the characters in reverse order.

| Index | Result | OUTPUT |
|---|---|---|
| | "" | |
| 5 | "l" | |
| 4 | "le" | |
| 3 | "lev" | |
| 2 | "leve" | |
| 1 | "leveL" | |
| | | Different |

- Index takes the values 5, 4, 3, 2 and 1 [B1]
- Result starts as an empty string [B1]
- the first three results are "l", "le" and "lev" [B1]
- the last two results are "leve" and "leveL" [B1]
- "leveL" is not equal to "Level", because the comparison is case sensitive, so the output is Different [B1]

Q: [6 marks] ★★ (#cs.datatypes) A shop in Nairobi stores its stock in an array of records, as declared below.

```pseudocode
TYPE StockItem
   DECLARE ItemCode : STRING
   DECLARE Quantity : INTEGER
ENDTYPE

DECLARE Stock : ARRAY[1:100] OF StockItem
```

Write a procedure `Sell` that takes an item code and a number sold. It searches `Stock` for the item and stops as soon as it is found. If the item is found and there is enough stock, the quantity is reduced by the number sold. If there is not enough stock, it outputs "Not enough stock". If the item is not in the array, it outputs "Item not found". [6]
H: Use a flag and a `WHILE` loop so the search stops at the first match.
A: One possible answer:

```pseudocode
PROCEDURE Sell(Code : STRING, Sold : INTEGER)
   DECLARE Index : INTEGER
   DECLARE Found : BOOLEAN

   Index ← 1
   Found ← FALSE
   WHILE Index <= 100 AND Found = FALSE
      IF Stock[Index].ItemCode = Code THEN
         Found ← TRUE
      ELSE
         Index ← Index + 1
      ENDIF
   ENDWHILE
   IF Found = FALSE THEN
      OUTPUT "Item not found"
   ELSE
      IF Stock[Index].Quantity >= Sold THEN
         Stock[Index].Quantity ← Stock[Index].Quantity - Sold
      ELSE
         OUTPUT "Not enough stock"
      ENDIF
   ENDIF
ENDPROCEDURE
```

- procedure header with the two parameters [B1]
- a loop that stops when the item is found or the end of the array is reached [B1]
- each `ItemCode` compared with the code, using dot notation, and the index moved on only when it does not match [B1]
- "Item not found" output if the whole array was searched without a match [B1]
- the quantity compared with the number sold (`>=`) [B1]
- the quantity reduced when there is enough, and "Not enough stock" output otherwise [B1]

Q: [5 marks] ★★ (#cs.datatypes) The array `Marks` holds six integers and must be sorted so that the **largest** mark comes first. The pseudocode below is an efficient bubble sort with three gaps.

```pseudocode
DECLARE Marks : ARRAY[1:6] OF INTEGER
DECLARE Temp, Last, Index : INTEGER
DECLARE Swapped : BOOLEAN

Last ← 5
REPEAT
   Swapped ← FALSE
   FOR Index ← 1 TO (a) ..........
      IF Marks[Index] (b) .......... Marks[Index + 1] THEN
         Temp ← Marks[Index]
         (c) ..........
         Marks[Index + 1] ← Temp
         Swapped ← TRUE
      ENDIF
   NEXT Index
   Last ← Last - 1
UNTIL Swapped = FALSE OR Last = 0
```

(a) Write the missing code for the gaps (a), (b) and (c). [3]

(b) The array holds 34, 71, 50, 88, 62 and 45. State the contents of the array after the first pass of the loop. [2]
A: (a)

- gap (a): `Last` [B1]
- gap (b): `<` (a smaller mark is swapped with the larger one after it, so the largest goes first) [B1]
- gap (c): `Marks[Index] ← Marks[Index + 1]` [B1]

(b) 71, 50, 88, 62, 45, 34

Each comparison moves 34 one place to the right until it is last. [B1] The other five marks are in the order shown. [B1]

Q: [6 marks] ★★ (#cs.procedures) A cinema in Lima charges a price for each ticket. A booking of 10 or more tickets receives a discount of 15%.

(a) Write a function `TicketCost` that takes the number of tickets (an INTEGER) and the price of one ticket (a REAL) and returns the total cost (a REAL) after any discount. [4]

(b) Write one statement that outputs the cost of 12 tickets at a price of 5.00 each. [1]

(c) State the value returned by the function for that booking. [1]
A: (a) One possible answer:

```pseudocode
FUNCTION TicketCost(Tickets : INTEGER, Price : REAL) RETURNS REAL
   DECLARE Total : REAL

   Total ← Tickets * Price
   IF Tickets >= 10 THEN
      Total ← Total * 0.85
   ENDIF
   RETURN Total
ENDFUNCTION
```

- function header with both parameters and `RETURNS REAL`, closed with `ENDFUNCTION` [B1]
- the total calculated as tickets multiplied by price [B1]
- the discount applied when `Tickets >= 10` (a total of 85% of the original) [B1]
- the total returned [B1]

(b) `OUTPUT TicketCost(12, 5.00)` [B1] (a function is used in an expression, so there is no `CALL`)

(c) \(12 \times 5.00 = 60.00\), and \(60.00 \times 0.85 = 51.00\), so the value is 51.0. [B1]

Q: [4 marks] ★★ (#cs.procedures) Write a procedure `Swap` that exchanges the values of two INTEGER variables passed to it, so that the change is seen by the program that calls it. Then write the statement that uses it to swap the variables `First` and `Second`. [4]
A: One possible answer:

```pseudocode
PROCEDURE Swap(BYREF A : INTEGER, BYREF B : INTEGER)
   DECLARE Temp : INTEGER

   Temp ← A
   A ← B
   B ← Temp
ENDPROCEDURE

CALL Swap(First, Second)
```

- both parameters passed `BYREF`, so the caller's variables change [B1]
- a temporary variable declared and used [B1]
- the three assignments in the correct order: `Temp ← A`, `A ← B`, `B ← Temp` [B1]
- `CALL Swap(First, Second)`, because a procedure is run with `CALL` [B1]

Q: [7 marks] ★★★ (#cs.structures) A queue of up to 6 integers is stored in the array `Queue[1:6]`. The global variable `FrontPointer` is 1 and `RearPointer` is 0 when the queue is empty. The queue is empty when `FrontPointer > RearPointer`.

(a) These operations are carried out on an empty queue: enqueue 14, enqueue 9, dequeue, enqueue 21, dequeue. State the values of `FrontPointer` and `RearPointer` after them. [2]

(b) State the item returned by the next dequeue. [1]

(c) Write a function `Dequeue` that returns the item at the front of the queue and removes it, or returns -1 if the queue is empty. [4]
H: Adding an item moves the rear pointer up by one; removing one moves the front pointer up by one.
A: (a) After the five operations, `FrontPointer` is 3 [B1] and `RearPointer` is 3 [B1].

| Operation | FrontPointer | RearPointer | Returned |
|---|---|---|---|
| start | 1 | 0 | |
| enqueue 14 | 1 | 1 | |
| enqueue 9 | 1 | 2 | |
| dequeue | 2 | 2 | 14 |
| enqueue 21 | 2 | 3 | |
| dequeue | 3 | 3 | 9 |

(b) The next dequeue returns 21. [B1]

(c) One possible answer:

```pseudocode
FUNCTION Dequeue() RETURNS INTEGER
   DECLARE Item : INTEGER

   IF FrontPointer > RearPointer THEN
      RETURN -1
   ELSE
      Item ← Queue[FrontPointer]
      FrontPointer ← FrontPointer + 1
      RETURN Item
   ENDIF
ENDFUNCTION
```

- function header with `RETURNS INTEGER` [B1]
- the empty test `FrontPointer > RearPointer`, returning -1 [B1]
- the item at the front read from `Queue[FrontPointer]` [B1]
- `FrontPointer` increased by 1 and the item returned [B1]

Q: [7 marks] ★★★ (#cs.structures) A club keeps the names of its members, one per line, in the text file `Names.txt`, which already exists. Write a procedure `AddName` that takes a name as a parameter. If the name is already in the file, the procedure outputs "Already present". Otherwise it adds the name to the end of the file. [7]
H: You must read the whole file first, close it, and only then open it again for adding.
A: One possible answer:

```pseudocode
PROCEDURE AddName(NewName : STRING)
   DECLARE Line : STRING
   DECLARE Found : BOOLEAN

   Found ← FALSE
   OPENFILE "Names.txt" FOR READ
   WHILE NOT EOF("Names.txt") AND Found = FALSE
      READFILE "Names.txt", Line
      IF Line = NewName THEN
         Found ← TRUE
      ENDIF
   ENDWHILE
   CLOSEFILE "Names.txt"
   IF Found = TRUE THEN
      OUTPUT "Already present"
   ELSE
      OPENFILE "Names.txt" FOR APPEND
      WRITEFILE "Names.txt", NewName
      CLOSEFILE "Names.txt"
   ENDIF
ENDPROCEDURE
```

- file opened for reading [B1]
- a loop that continues until the end of the file (or the name is found), using `EOF` [B1]
- each line read with `READFILE` and compared with the name [B1]
- the file closed after searching [B1]
- "Already present" output when the name was found [B1]
- the file opened for appending (not writing, which would erase it) when not found [B1]
- the name written with `WRITEFILE` and the file closed [B1]

Q: [5 marks] ★★ (#cs.development) A program for a sports day in Kingston is split into three modules. `Main` calls them in order.

| Module | What it does |
|---|---|
| `InputTime` | asks the user for a race time in seconds and gives it to `Main` |
| `CalcPoints` | takes a race time (REAL) and gives back the points won (INTEGER) |
| `ShowResult` | takes a runner's name (STRING) and points (INTEGER) and outputs them |

(a) For each module, state whether it should be a procedure or a function, with a reason. [3]

(b) Write the header line of `CalcPoints` and of `ShowResult`. [2]
A: (a)

- `InputTime` is a function, because it gives a value (the time) back to `Main` [B1]
- `CalcPoints` is a function, because it returns the points [B1]
- `ShowResult` is a procedure, because it only outputs and returns nothing [B1]

(b)

```pseudocode
FUNCTION CalcPoints(RaceTime : REAL) RETURNS INTEGER
PROCEDURE ShowResult(Name : STRING, Points : INTEGER)
```

- `FUNCTION CalcPoints(RaceTime : REAL) RETURNS INTEGER` [B1]
- `PROCEDURE ShowResult(Name : STRING, Points : INTEGER)` [B1]

Q: [6 marks] ★★ (#cs.testing) A program accepts the age of a pupil. The age must be a whole number from 11 to 19 inclusive; any other input is rejected with a message.

(a) Complete the test plan. [4]

| Data | Type of test data | Expected result |
|---|---|---|
| 15 | | |
| 11 | | |
| 19 | | |
| ten | | |

(b) The tester enters 11 and the program rejects it. Name the type of error and suggest its likely cause. [2]
A: (a)

| Data | Type of test data | Expected result |
|---|---|---|
| 15 | normal | accepted |
| 11 | extreme (boundary) | accepted |
| 19 | extreme (boundary) | accepted |
| ten | abnormal | rejected with a message |

- 15: normal data, accepted [B1]
- 11: extreme data, accepted [B1]
- 19: extreme data, accepted [B1]
- "ten": abnormal data (not a number), rejected [B1]

(b) A logic error [B1]: the condition probably uses `>` instead of `>=`, so the lowest valid age is wrongly rejected [B1].

Q: [9 marks] ★★★ (#cs.procedures) A shop gives every product a six-character code: five digits followed by a modulo-11 check character. The check character is a digit, or the letter X when the check digit is 10. To validate a code, the five digits are multiplied by the weights 6, 5, 4, 3 and 2 (from the left), the value of the check character (X counts as 10) is added, and the total must be a multiple of 11. For example, 30591X is valid, because \(18 + 0 + 20 + 27 + 2 = 67\) and \(67 + 10 = 77 = 7 \times 11\).

Write a function `ValidProduct` that takes a STRING and returns TRUE if it is a valid code and FALSE otherwise. Refer to the insert for the functions you may use. [9]
H: Test the length first, then the five digits one at a time with `MID` and `IS_NUM`; the weight of position \(n\) is \(7 - n\).
H: Deal with the check character after the loop: `X` is worth 10.
A: One possible answer:

```pseudocode
FUNCTION ValidProduct(Code : STRING) RETURNS BOOLEAN
   DECLARE Index, Total, CheckValue : INTEGER
   DECLARE CheckChar : STRING

   IF LENGTH(Code) <> 6 THEN
      RETURN FALSE
   ENDIF
   Total ← 0
   FOR Index ← 1 TO 5
      IF NOT IS_NUM(MID(Code, Index, 1)) THEN
         RETURN FALSE
      ENDIF
      Total ← Total + STR_TO_NUM(MID(Code, Index, 1)) * (7 - Index)
   NEXT Index
   CheckChar ← RIGHT(Code, 1)
   IF CheckChar = "X" THEN
      CheckValue ← 10
   ELSE
      IF NOT IS_NUM(CheckChar) THEN
         RETURN FALSE
      ENDIF
      CheckValue ← STR_TO_NUM(CheckChar)
   ENDIF
   IF ((Total + CheckValue) MOD 11) = 0 THEN
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION
```

- function header with a STRING parameter and `RETURNS BOOLEAN`, closed with `ENDFUNCTION` [B1]
- the length tested and FALSE returned if it is not 6 [B1]
- a loop through the first five characters, each extracted with `MID` [B1]
- each of those characters tested with `IS_NUM` and FALSE returned if it is not a digit [B1]
- each digit converted with `STR_TO_NUM` and multiplied by its weight (6 down to 2) [B1]
- the products added into a total that starts at 0 [B1]
- the check character taken from the end of the code, with `X` given the value 10 and any other character converted to a number (FALSE if it is not a digit) [B1]
- the check value added to the total and the result tested with `MOD 11` [B1]
- TRUE returned when the remainder is 0 and FALSE otherwise, so every path returns a value [B1]

(Accept the weights calculated with a counter that counts down from 6, and the total tested in the form `(Total + CheckValue) MOD 11 = 0`, bracketed.)
:::

## Quiz: AS misconceptions

:::quiz Where AS students lose marks
? A file is 3 KiB. How many bytes is that?
- 3000
+ 3072
- 3024
- 2048
> A kibibyte is 2¹⁰ = 1024 bytes, so 3 KiB is 3 × 1024 = 3072 bytes. 3000 uses the decimal kilobyte.
? What is the largest positive number an 8-bit two's complement integer can hold?
- 255
- 256
- 128
+ 127
> The leftmost bit is the sign, leaving 7 bits for the size: the range is −128 to 127. 255 is the largest unsigned 8-bit number.
? How many bits does one hexadecimal digit represent?
- 2
+ 4
- 8
- 16
> One hex digit has 16 possible values, which is 2⁴, so it stands for exactly four bits. That is why B5 is the byte 1011 0101.
? What is the output of an XOR gate when both of its inputs are 1?
+ 0
- 1
- It depends on the gate's position in the circuit.
- It cannot be worked out from the inputs.
> XOR is true when the inputs are different. With 1 and 1 they are the same, so the output is 0. An OR gate would give 1.
? A byte is sent with even parity. Two bits of the byte are changed in transmission. What does the parity check report?
- An error, because the data changed.
+ Nothing: the number of 1s is still even, so the error is not detected.
- An error in exactly the two bits that changed.
- That the byte is correct and has been checked.
> Two flipped bits change the count of 1s by an even amount, so the parity is unchanged. A parity check detects one wrong bit but not two, and it never says which bit is wrong.
? Which statement about a firewall is correct?
- It finds and removes viruses from the computer's files.
+ It examines the data entering and leaving a network or computer and blocks what breaks its rules.
- It encrypts all the data sent over the internet.
- It prevents a user from typing a wrong password.
> A firewall checks network traffic against rules. Finding and removing malware is the job of anti-virus software, and scrambling data is encryption.
? A program checks that an age typed in is a whole number from 11 to 19. What does this validation prove?
- The age is correct.
+ The age is reasonable and in the right form, but it may still be wrong.
- The person typed the age twice.
- The age has been checked against the register.
> Validation only checks that data is sensible. A user who types 17 instead of 18 passes a range check. Checking that data was copied correctly is verification, such as double entry.
? A table has the primary key (OrderID, ItemCode) and the field ItemName, which depends only on ItemCode. In which normal form does this table first fail?
- first normal form
+ second normal form
- third normal form
- it is in third normal form
> A field that depends on only part of a composite key breaks second normal form. A third normal form fault is a field that depends on another non-key field.
? Which statement about an interpreter is correct?
- It translates the whole program into an executable file before it is run.
+ It translates and runs the program one line at a time, so it stops at the first error.
- It produces machine code that runs faster than compiled code.
- It is needed only for the assembly language.
> An interpreter does not create a file of machine code: the source is translated every time it runs. The first statement describes a compiler, and the third is the wrong way round.
? A procedure must add a line to the end of an existing text file without losing the old lines. How should the file be opened?
- FOR READ
- FOR WRITE
+ FOR APPEND
- FOR RANDOM
> FOR WRITE creates a new, empty file and the old lines are lost. FOR APPEND adds to the end. FOR READ does not allow writing at all.
:::

:::recap
- Do mixed practice by hand and against the clock: 1.2 minutes a mark in Paper 1 style questions and 1.6 minutes a mark in Paper 2 style questions.
- Each question has a revise link: use it after your attempt, and record the section where you lost marks.
- Conversions and arithmetic need working: powers of two for sizes, the two's complement method, the weights for a check digit.
- Assembly masks: AND tests or clears, OR sets, XOR toggles; compare with 0 and jump.
- Normalise by asking whether each field depends on the whole key and nothing else; then write SQL with `INNER JOIN … ON`, `WHERE`, `GROUP BY` and `ORDER BY`.
- Pseudocode: declare, indent, close every structure, use the insert's functions, return a value from a function, close every file, and APPEND to extend.
- Test data: normal, abnormal and extreme; a rejected boundary value is a logic error.
- Misconceptions to remember: kibi is 1024, a parity check misses two bit errors, validation is not correctness, a firewall is not anti-virus.
:::

:::links
- practise: [Data representation: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/1-information-representation/data-representation/exam-questions/) · Save My Exams · section 1 questions with mark schemes [paid]
- practise: [Networks and the internet: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/2-communication-/networks-and-the-internet/exam-questions/) · Save My Exams · section 2 questions [paid]
- practise: [Assembly language: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/4-processor-fundamentals-/assembly-language-/exam-questions/) · Save My Exams · trace and mask questions [paid]
- practise: [Constructs: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/constructs/exam-questions/) · Save My Exams · pseudocode selection and loop questions [paid]
- papers: [9618 past papers, inserts and mark schemes](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · Papers 1 and 2 by series [unofficial]
- practise: [SQLBolt](https://sqlbolt.com/) · SQLBolt · interactive SQL exercises to run queries like the ones here
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run a Python version of an algorithm line by line to check a trace table

Links checked 13 November 2026.
:::

Next: [Paper 3 guide: Advanced Theory](#cs.exam.p3)
