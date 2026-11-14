@chapter cs.assembly
@title Assembly language and bit manipulation
@level as
@paper CAIE 9618 Paper 1
@time 6–8 hours
@summary How a processor's instructions are written as assembly language and machine code, how a two-pass assembler translates a program, the instruction set and its five addressing modes, how to trace a program and write short ones, and how shifts and masks (AND, OR, XOR) test, set and clear individual bits to monitor and control a device.

:::why
Assembly language is the closest a programmer gets to the processor. Every other language you will use, from Python to the pseudocode in Paper 2, is eventually turned into the simple instructions you meet here. Paper 1 prints a short instruction set and a memory table, and asks you to trace the program, to say what an instruction does, to complete an assembler's symbol table, or to write a few instructions that set or test a bit. All of these are exact skills with exact answers: once you have the method, you can score every mark.
:::

**Before you start**, you should be comfortable with binary and hexadecimal from [Number systems and binary arithmetic](#cs.data), and with the registers and the fetch-execute cycle from [Processor fundamentals and the fetch-execute cycle](#cs.processor).

:::try Warm-up
Q: Write the denary number 44 as an 8-bit binary number. (from [Number systems and binary arithmetic](#cs.data))
A: \(44 = 32 + 8 + 4\), so the binary number is 00101100.
Q: What does the register transfer `MAR ← [PC]` do, and which register is increased next? (from [Processor fundamentals and the fetch-execute cycle](#cs.processor))
A: It copies the address in the program counter into the memory address register. The program counter is increased next: `PC ← [PC] + 1`.
Q: In the ASCII code, the capital letter A is 65. What is the code of the capital letter D? (from [Number systems and binary arithmetic](#cs.data))
A: The capitals are in alphabetical order, so D is three after A: \(65 + 3 = 68\).
:::

:::note The simple machine used in this chapter
The programs in this chapter run on a simple machine with one general purpose register (the accumulator, ACC) and an index register (IX). Each register and each memory location holds **8 bits**, so a stored number is between 0 and 255. A question in the exam states the size of the registers if it matters. Programs start at address 100, and data is kept at higher addresses, so that instructions and data do not overlap.
:::

## From machine code to assembly language

The processor can only carry out instructions written as binary numbers. A program in that form is **machine code**. A programmer who writes in machine code has to remember that, say, `0000100001101000` means "load the contents of address 104 into the accumulator". Nobody does this for long.

:::def Machine code
The program instructions written in binary, in the form that the processor can execute directly. Each instruction is made of an opcode and, usually, an operand.
:::

:::def Opcode and operand
The **opcode** (operation code) is the part of an instruction that says which operation to carry out, such as load, add or jump. The **operand** is the part that says what to carry out the operation on: usually an address or a number.
:::

:::def Assembly language
A low-level programming language in which each instruction is written with a short, readable name, called a mnemonic (such as `LDD`, `ADD`, `STO`), instead of a binary opcode, and in which memory locations can be given names, called labels. There is one assembly instruction for each machine code instruction, and each type of processor has its own assembly language.
:::

:::def Mnemonic
A short, memorable abbreviation used in assembly language for an opcode: `ADD` for add, `STO` for store, `JMP` for jump.
:::

:::def Assembler
A program that translates a program written in assembly language into machine code. The assembler is a language translator, like a compiler, but it is simpler because every assembly instruction translates into exactly one machine code instruction.
:::

Writing `ADD 105` is much easier to read, to write and to correct than a row of 16 ones and zeros, and the assembler does the boring translation. A label such as `TOTAL` also means that the programmer does not have to work out the address of every variable by hand.

### What a machine code instruction looks like

In this chapter's machine each instruction is 16 bits: a 6-bit opcode followed by a 10-bit operand (the address or number). The opcode values below were made up for this chapter. Real processors use different ones, so an exam question always prints the codes it needs.

| Assembly instruction | Opcode (6 bits) |
|---|---|
| `LDD` | 000010 |
| `ADD` (an address) | 000111 |
| `STO` | 000110 |
| `END` | 010011 |

The instruction `LDD 104` becomes the opcode for `LDD`, 000010, followed by 104 as a 10-bit binary number. \(104 = 64 + 32 + 8\), which is 0001101000 in 10 bits. The whole instruction is therefore:

```text
000010 0001101000
```

Because there is exactly one machine instruction for each assembly instruction, the translation is a direct lookup. That is why an assembler is much simpler than a compiler, which has to turn one line of Python or pseudocode into many machine instructions.

:::warn Assembly is not portable
Machine code and assembly language are different for every type of processor. A program written in the assembly language of one processor will not run on a processor of a different design, and has to be rewritten. A program in a high-level language needs only to be translated again.
:::

### Why use assembly language

Assembly language is still used when a programmer needs something that high-level languages hide: the exact timing of instructions, direct control of a device, or the smallest possible program for a tiny processor, such as one inside a toy or a sensor. Programs written this way can be fast and compact. The costs are that they are slow to write, hard to read and debug, and tied to one type of processor.

## The instruction set

The syllabus uses one example instruction set, and a Paper 1 question prints the part of it that the question uses, with a short explanation of each instruction. You are not expected to memorise it, but you must be able to read it quickly and to use it exactly. Learn the pattern, and you can pick up any similar set.

| Instruction | Operand | Explanation |
|---|---|---|
| `LDM` | `#n` | Load the number n into ACC (immediate addressing). |
| `LDD` | `<address>` | Load the contents of the location at the given address into ACC (direct addressing). |
| `LDI` | `<address>` | The location at the given address holds another address. Load into ACC the contents of that second location (indirect addressing). |
| `LDX` | `<address>` | Load into ACC the contents of the location whose address is the given address plus the contents of IX (indexed addressing). |
| `LDR` | `#n` | Load the number n into IX. |
| `MOV` | `IX` | Copy the contents of ACC into IX. |
| `STO` | `<address>` | Store the contents of ACC at the given address. |
| `ADD` | `<address>` | Add the contents of the location at the given address to ACC; the result stays in ACC. |
| `ADD` | `#n`, `Bn` or `&n` | Add the number n to ACC. |
| `SUB` | `<address>` | Subtract the contents of the location at the given address from ACC. |
| `SUB` | `#n`, `Bn` or `&n` | Subtract the number n from ACC. |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX). |
| `DEC` | `<register>` | Subtract 1 from the contents of the register (ACC or IX). |
| `JMP` | `<address>` | Jump to the given address (the next instruction fetched is the one there). |
| `CMP` | `<address>` | Compare the contents of ACC with the contents of the location at the given address. The result (True if they are equal) is recorded. |
| `CMP` | `#n` | Compare the contents of ACC with the number n. |
| `CMI` | `<address>` | Indirect compare: the location at the given address holds another address; compare ACC with the contents of that second location. |
| `JPE` | `<address>` | After a compare, jump to the given address if the result was True (the values were equal). |
| `JPN` | `<address>` | After a compare, jump to the given address if the result was False (the values were not equal). |
| `IN` | | Key in a character; its ASCII value is stored in ACC. |
| `OUT` | | Output to the screen the character whose ASCII value is in ACC. |
| `END` | | Return control to the operating system (the program ends). |
| `AND` | `#n`, `Bn`, `&n` or `<address>` | Bitwise AND of ACC with the operand; the result is in ACC. |
| `OR` | `#n`, `Bn`, `&n` or `<address>` | Bitwise OR of ACC with the operand; the result is in ACC. |
| `XOR` | `#n`, `Bn`, `&n` or `<address>` | Bitwise XOR of ACC with the operand; the result is in ACC. |
| `LSL` | `#n` | Shift the bits in ACC n places to the left; zeros enter on the right. |
| `LSR` | `#n` | Shift the bits in ACC n places to the right; zeros enter on the left. |

Three notation rules are worth learning now:

- A number in an operand starts with `#` if it is denary (`#25`), with `B` if binary (`B00011001`) and with `&` if hexadecimal (`&19`). All three are the same number, 25.
- A **label** is a name followed by a colon, written before an instruction or before a piece of data: `LOOP: ADD COUNT` or `TOTAL: 0`. In operands the label is written without the colon, and stands for the address of that line.
- A line that holds only data, such as `TOTAL: 0`, takes one memory location, like an instruction.

### The five groups of instructions

The syllabus groups the instructions by purpose. The names of the groups are examined, so know which instruction belongs where.

| Group | Instructions | What the group does |
|---|---|---|
| Data movement | `LDM`, `LDD`, `LDI`, `LDX`, `LDR`, `MOV`, `STO` | Copies values between memory and the registers. |
| Input and output | `IN`, `OUT` | Moves a character between the keyboard or screen and ACC. |
| Arithmetic | `ADD`, `SUB`, `INC`, `DEC` | Calculates, with the result in ACC (or in IX for `INC IX` and `DEC IX`). |
| Unconditional jump | `JMP` | Always moves to the given address. |
| Compare and conditional jump | `CMP`, `CMI`, then `JPE` or `JPN` | The compare records True or False; the jump uses it. |

The logic and shift instructions (`AND`, `OR`, `XOR`, `LSL`, `LSR`) form the bit manipulation group, explained at the end of this chapter, and `END` stops the program. A good habit: for each instruction, say to yourself what it changes (ACC, IX, memory or the PC) and what it leaves alone.

:::warn Easy mistakes with the instruction set
- `LDD 150` loads the **contents** of location 150. `LDM #150` loads the **number** 150. The `#` is the difference.
- `INC` and `DEC` change a **register** (`INC ACC`, `INC IX`), not a memory location. To add 1 to a stored number, load it, increase it and store it again.
- `ADD 150` adds the contents of address 150; `ADD #150` adds the number 150.
- `JPE` and `JPN` look at the result of the **most recent** compare. Nothing else (not an `ADD`, not a `LDD`) sets or changes it.
- `CMP` does not change ACC; it only records True or False.
:::

## Addressing modes

The operand of an instruction can mean several different things. How the processor finds the value it needs from the operand is the **addressing mode**. Five are in the syllabus.

:::def Immediate addressing
The operand is the value itself. `LDM #5` loads the number 5.
:::

:::def Direct addressing
The operand is the address of the location that holds the value. `LDD 200` loads the contents of location 200.
:::

:::def Indirect addressing
The operand is the address of a location that holds the **address** of the value. The processor follows the address to find the value: `LDI 200` reads location 200, and uses what is there as the address of the value to load.
:::

:::def Indexed addressing
The address that the processor uses is the operand plus the contents of the index register. `LDX 200` with IX holding 2 loads the contents of location 202.
:::

:::def Relative addressing
The operand is an offset from the address of the current instruction, so the address used is found by adding the operand to the address of the instruction. It is used mostly with jumps: "jump 3 locations forward".
:::

A memory table, with an address column and a contents column, is the clearest way to see the difference. Suppose memory holds the following, and IX holds 2.

| Address | Contents |
|---|---|
| 200 | 205 |
| 201 | 7 |
| 202 | 31 |
| 203 | 12 |
| 204 | 50 |
| 205 | 99 |

| Instruction | What the processor does | ACC afterwards |
|---|---|---|
| `LDM #200` | Immediate: the operand is the value. | 200 |
| `LDD 200` | Direct: the value is in location 200. | 205 |
| `LDI 200` | Indirect: location 200 holds 205, so the value is in location 205. | 99 |
| `LDX 200` | Indexed: the address is \(200 + 2 = 202\), so the value is in location 202. | 31 |

All four use the same operand, 200, and give four different answers. This is a favourite exam question.

:::analogy Four ways to ask for a book
Immediate: you hand someone the book itself. Direct: you tell them the shelf number where the book is. Indirect: you tell them the number of a shelf that holds a note, and the note gives the number of the shelf with the book. Indexed: you give them the first shelf of a row, and say "take the third one along"; the number you add is the index.
:::

:::eg Indexed addressing to step through an array
An array of five test scores is stored in locations 150 to 154: 12, 30, 25, 8 and 41 (in that order). Show how `LDX 150` reads each score as IX takes the values 0 to 4.

Each time the processor adds the contents of IX to the operand 150.

- IX = 0: the address is 150, so ACC becomes 12.
- IX = 1: the address is 151, so ACC becomes 30.
- IX = 2: the address is 152, so ACC becomes 25.
- IX = 3: the address is 153, so ACC becomes 8.
- IX = 4: the address is 154, so ACC becomes 41.

The instruction never changes. Only the contents of IX change, with `INC IX`. That is why indexed addressing is the natural way to process an array in a loop.
:::

### Relative addressing

The example instruction set has no instruction that uses relative addressing, so a question that uses it defines the instruction itself. Suppose a question says that `JMR #n` jumps n locations forward from the address of the `JMR` instruction (a negative n jumps backward). If a `JMR #3` is stored at address 105, the next instruction to be fetched is at \(105 + 3 = 108\). If a `JMR #-2` is stored at address 105, the next instruction is at \(105 - 2 = 103\). The benefit of relative addressing is that the program still works if the whole program is moved to a different part of memory, because all the jumps move with it.

## Tracing a program

To **trace** a program, you act as the processor: you carry out the instructions one at a time, and record every change. Examiners print a **trace table** with one column for each register or memory location whose value changes. The method:

:::steps
1. Write down the starting contents of every memory location the program uses (they are in the memory table in the question).
2. Start at the first instruction and take the instructions in address order.
3. For each instruction, write one row: the address, the instruction, and the new value of anything it changes. Leave the other cells blank.
4. A jump changes which instruction comes next: after a jump, continue at the address of its target.
5. After a `CMP`, record True or False. At the next `JPE` or `JPN`, use that result to decide whether to jump.
6. Stop at `END`. Collect any output in the output column.
:::

In the tables in this chapter a cell is filled when the instruction **writes** that register or location, even if it writes the same value as before. The Address column is the address of the instruction that was executed. Memory contents are shown as denary numbers unless the question says otherwise.

### A first trace

:::eg Tracing an addition (exam style)
The program below adds two numbers. Instructions and data are stored from address 100. The label `START` marks the first instruction, and `FIRST`, `SECOND` and `TOTAL` mark the data. Complete a trace table for the program. [5 marks]

```text
100  START:  LDD FIRST
101          ADD SECOND
102          STO TOTAL
103          END
104  FIRST:  7
105  SECOND: 5
106  TOTAL:  0
```

| Address | Instruction | ACC | IX | [TOTAL] | OUTPUT |
|---|---|---|---|---|---|
| start | | | | 0 | |
| 100 | LDD FIRST | 7 | | | |
| 101 | ADD SECOND | 12 | | | |
| 102 | STO TOTAL | | | 12 | |
| 103 | END | | | | |

- `LDD FIRST` loads the contents of FIRST (location 104), which is 7, into ACC [B1]
- `ADD SECOND` adds the contents of SECOND (5), so ACC becomes 12 [B1]
- `STO TOTAL` stores 12 in location 106 [B1]
- no change to IX and no output [B1]
- the program stops at `END` with TOTAL holding 12 [B1]
:::

You can run this program yourself in the widget at the end of this section.

### A loop

A loop in assembly language is a compare and a jump backward. This program multiplies 6 by 2 the long way, by adding 6 to a total twice. Location 200 holds the number to add, 201 holds the number of times still to add, and 202 holds the total.

:::eg Tracing a loop (exam style)
Trace this program until it ends. Show the contents of locations 201 and 202, and the result of each compare. [8 marks]

```text
100          LDM #0
101          STO 202
102  LOOP:   LDD 202
103          ADD 200
104          STO 202
105          LDD 201
106          SUB #1
107          STO 201
108          CMP #0
109          JPN LOOP
110          END
200          6
201          2
202          0
```

| Address | Instruction | ACC | IX | 201 | 202 | Compare | OUTPUT |
|---|---|---|---|---|---|---|---|
| start | | | | 2 | 0 | | |
| 100 | LDM #0 | 0 | | | | | |
| 101 | STO 202 | | | | 0 | | |
| 102 | LDD 202 | 0 | | | | | |
| 103 | ADD 200 | 6 | | | | | |
| 104 | STO 202 | | | | 6 | | |
| 105 | LDD 201 | 2 | | | | | |
| 106 | SUB #1 | 1 | | | | | |
| 107 | STO 201 | | | 1 | | | |
| 108 | CMP #0 | | | | | FALSE | |
| 109 | JPN LOOP | | | | | | |
| 102 | LDD 202 | 6 | | | | | |
| 103 | ADD 200 | 12 | | | | | |
| 104 | STO 202 | | | | 12 | | |
| 105 | LDD 201 | 1 | | | | | |
| 106 | SUB #1 | 0 | | | | | |
| 107 | STO 201 | | | 0 | | | |
| 108 | CMP #0 | | | | | TRUE | |
| 109 | JPN LOOP | | | | | | |
| 110 | END | | | | | | |

- initialises the total in location 202 to 0 (rows 100 and 101) [B1]
- the first pass of the loop adds 6 to the total, giving 6 in location 202 [B1]
- location 201 is reduced from 2 to 1 [B1]
- the first compare of ACC with 0 is FALSE, so `JPN LOOP` jumps back to address 102 [B1]
- the second pass gives 12 in location 202 [B1]
- location 201 is reduced from 1 to 0 [B1]
- the second compare is TRUE, so `JPN LOOP` does **not** jump [B1]
- the program continues to `END` with 12 in location 202 [B1]
:::

Look at row 109 the first time. The `JPN` is carried out, and the next row is address 102: the jump is visible in the Address column, not in a cell. On the second time the compare is TRUE, so there is no jump, and the next address is 110. The trace shows 12 = 6 × 2.

:::key The loop pattern
A counting loop in assembly language has four parts: set the counter before the loop; do the work, labelled with the loop's first line; change the counter (load it, `DEC ACC` or `SUB #1`, store it); then `CMP #0` and a jump back (`JPN` to repeat while the counter is not zero). A pseudocode `REPEAT … UNTIL Count = 0` becomes exactly this.
:::

```pseudocode
Count ← 2
REPEAT
   Total ← Total + 6
   Count ← Count - 1
UNTIL Count = 0
```

The pseudocode above and the assembly program do the same thing: the `UNTIL` condition is tested after the body, which is why the compare and jump come at the end of the assembly loop.

### Input and output with ASCII codes

`IN` waits for a key and stores its ASCII code in ACC. `OUT` shows the character for the code in ACC. A question gives the codes it needs: for example "the ASCII code of `a` is 97 and of `A` is 65". Because the lower-case letters come \(97 - 65 = 32\) after the capitals, subtracting 32 turns a lower-case letter into a capital.

:::eg Reading and writing characters
The program below reads a character, changes it and displays it. The user types `q` (ASCII code 113). The ASCII code of `Q` is 81. State the character output and show the trace.

```text
100  IN
101  SUB #32
102  OUT
103  END
```

| Address | Instruction | ACC | IX | OUTPUT |
|---|---|---|---|---|
| 100 | IN | 113 | | |
| 101 | SUB #32 | 81 | | |
| 102 | OUT | | | Q |
| 103 | END | | | |

`IN` stores the code 113 for `q`. `SUB #32` leaves 81. `OUT` displays the character with code 81, which is `Q`. The program converts a lower-case letter to a capital (it assumes the user typed a lower-case letter).
:::

### Indexed addressing in a loop

This program adds up the numbers in an array. The array is stored from address 111 and ends with a 0, which marks the end (a **sentinel**). IX holds the position in the array.

:::eg Adding an array with the index register
Trace this program. Show IX, the total (the location labelled TOTAL, 114) and the compare result. [exam style, 8 marks]

```text
100          LDR #0
101          LDM #0
102          STO TOTAL
103  LOOP:   LDX ARRAY
104          CMP #0
105          JPE DONE
106          ADD TOTAL
107          STO TOTAL
108          INC IX
109          JMP LOOP
110  DONE:   END
111  ARRAY:  4
112          9
113          0
114  TOTAL:  0
```

| Address | Instruction | ACC | IX | [TOTAL] | Compare | OUTPUT |
|---|---|---|---|---|---|---|
| start | | | | 0 | | |
| 100 | LDR #0 | | 0 | | | |
| 101 | LDM #0 | 0 | | | | |
| 102 | STO TOTAL | | | 0 | | |
| 103 | LDX ARRAY | 4 | | | | |
| 104 | CMP #0 | | | | FALSE | |
| 105 | JPE DONE | | | | | |
| 106 | ADD TOTAL | 4 | | | | |
| 107 | STO TOTAL | | | 4 | | |
| 108 | INC IX | | 1 | | | |
| 109 | JMP LOOP | | | | | |
| 103 | LDX ARRAY | 9 | | | | |
| 104 | CMP #0 | | | | FALSE | |
| 105 | JPE DONE | | | | | |
| 106 | ADD TOTAL | 13 | | | | |
| 107 | STO TOTAL | | | 13 | | |
| 108 | INC IX | | 2 | | | |
| 109 | JMP LOOP | | | | | |
| 103 | LDX ARRAY | 0 | | | | |
| 104 | CMP #0 | | | | TRUE | |
| 105 | JPE DONE | | | | | |
| 110 | END | | | | | |

- IX set to 0 and the total set to 0 before the loop [B1]
- first element 4 loaded by `LDX ARRAY` [B1]
- first compare FALSE and 4 added, TOTAL becomes 4 [B1]
- `INC IX` makes IX 1 [B1]
- second element 9 loaded and added, TOTAL becomes 13 [B1]
- `INC IX` makes IX 2 [B1]
- the third element, the sentinel 0, is loaded and the compare is TRUE [B1]
- `JPE DONE` jumps to `END`, with 13 in TOTAL [B1]
:::

There is one point that surprises students: the program never needs to know how many numbers there are, because the sentinel stops the loop. The cost is that 0 cannot be one of the numbers.

### Try it: a simulator

The widget below runs the assembly language of this chapter. Choose a program from the list, press Step to run one instruction at a time (the registers and the memory table change as you go), or press Run. Then edit the program in the box and run your own version: change the second number in `sum`, change the array in `indexed`, or type a new character for `upper`.

:::html
<div class="widget" data-w="cs-asm" data-program="indexed" data-mode="run"></div>
:::

## Writing assembly programs

In the exam you also write programs. The skill is to break the job into the instruction patterns you already know.

:::key Patterns to know
- **Add two stored numbers:** `LDD A`, `ADD B`, `STO C`.
- **Update a stored number:** load it (`LDD X`), change it (`ADD #1`, `SUB #1`), store it (`STO X`).
- **Make a decision:** put the value in ACC, `CMP` it with something, then `JPE` or `JPN` to the code for one of the two cases; both cases then continue at a common `END` or label.
- **Repeat:** a label at the start of the body; a counter that is changed and tested at the end; `JPN` back to the label.
- **Process an array:** `LDR #0`, then `LDX` with the array's first address inside a loop, and `INC IX` each time.
:::

:::eg Writing a program (exam style)
Location 150 holds 12 and location 151 holds 30. Write assembly language to add the two numbers, subtract 5, and store the result in location 152. [5 marks]

```text
100  LDD 150
101  ADD 151
102  SUB #5
103  STO 152
104  END
150  12
151  30
```

- `LDD 150` to load the first number into ACC [B1]
- `ADD 151` to add the second number [B1]
- `SUB #5`, using `#` because 5 is a number and not an address [B1]
- `STO 152` to store the result [B1]
- `END` [B1]

(`LDM #150` for the first line is wrong: it loads the number 150, not the contents of location 150.) After the program, location 152 holds \(12 + 30 - 5 = 37\).
:::

:::eg Spot the error: a trace that uses the wrong addressing mode
Question: Location 150 holds 25. Trace the program and give the final contents of location 151. [4 marks]

```text
100  LDM #20
101  ADD 150
102  STO 151
103  END
150  25
```

A student wrote this trace table:

| Address | Instruction | ACC | 151 |
|---|---|---|---|
| 100 | LDM #20 | 20 | |
| 101 | ADD 150 | 170 | |
| 102 | STO 151 | | 170 |
| 103 | END | | |

`LDM #20` loads 20 into ACC [B1]. **`ADD 150` adds the contents of location 150, which is 25, to give 45. The student added the number 150, which would be written `ADD #150`, so the ACC value is wrong** [B0]. `STO 151` stores the value that ACC holds, so the stored 170 is consistent with the student's own ACC [B1]. `END` stops the program [B1]. The answer scores 3 out of 4. The correct trace has 45 in ACC and then 45 in location 151.

Before you accept any trace, look at every operand and ask: does it have a `#`? If not, it is an address, and you must go to the memory table to fetch the contents.
:::

## The two-pass assembler

An assembler translates the whole program. A label may be used **before** it is defined: on the first line of the program above, `LDD FIRST` refers to a label that is not defined until address 104. If the assembler translated each line as it read it, it would not yet know the address of `FIRST`. The solution is to read the program twice. Cambridge calls this a **two-pass assembler**.

:::def Symbol table
A table made by the assembler that lists each label in the program with the address it stands for. The assembler uses it in the second pass to replace labels in operands with addresses.
:::

:::def Two-pass assembler
An assembler that reads the source program twice. In the first pass it builds the symbol table. In the second pass it translates each instruction into machine code, using the symbol table to find the address of every label.
:::

:::key The two passes
**Pass 1**
1. Read the program one line at a time, keeping a count of the address (starting at the program's first address).
2. Ignore blank lines and remove comments.
3. If a line starts with a label, add the label and the current address to the symbol table.
4. Add 1 to the address, and move to the next line.

**Pass 2**
1. Read each line again.
2. Look up the opcode of the mnemonic in the opcode table.
3. If the operand is a label, replace it with its address from the symbol table; if it is a number, convert it to binary.
4. Write out the machine code instruction (the opcode followed by the operand), and a binary word for each data location.
5. Report an error for anything that cannot be translated, such as an unknown mnemonic or a label that is not in the symbol table.
:::

:::eg Applying the two-pass assembler (exam style)
Use the program from the earlier trace, with its labels. (a) Complete the symbol table produced by pass 1. [3 marks] (b) Using the opcode table given earlier in the chapter, write the machine code produced by pass 2 for the three instructions and for the first data word `FIRST`. [4 marks]

```text
100  START:   LDD FIRST
101           ADD SECOND
102           STO TOTAL
103           END
104  FIRST:   7
105  SECOND:  5
106  TOTAL:   0
```

(a) Pass 1 reads each line and records each label with the address of its line:

| Label | Address |
|---|---|
| START | 100 |
| FIRST | 104 |
| SECOND | 105 |
| TOTAL | 106 |

- one correct row (START or FIRST) [B1]
- SECOND and TOTAL correct [B1]
- no entries for lines without a label [B1]

(b) Pass 2 replaces each mnemonic by its opcode, and each label by its address from the table, in 10 bits: \(104 = 0001101000\), \(105 = 0001101001\) and \(106 = 0001101010\).

| Address | Instruction | Machine code |
|---|---|---|
| 100 | `LDD FIRST` | 000010 0001101000 |
| 101 | `ADD SECOND` | 000111 0001101001 |
| 102 | `STO TOTAL` | 000110 0001101010 |
| 103 | `END` | 010011 0000000000 |
| 104 | `FIRST: 7` | 0000000000000111 |

- `LDD FIRST` translated with the opcode 000010 and the address 104 [B1]
- `ADD SECOND` and `STO TOTAL` translated correctly [B1]
- `END` with the opcode 010011 [B1]
- the data word 7 written as a 16-bit binary number [B1]
:::

Pass 1 needs to read the whole program before pass 2 starts, because `LDD FIRST` is on line 100 and `FIRST` is not defined until line 104. A one-pass assembler would have to leave blanks and come back to fill them in.

## Bit manipulation

So far every operation worked on whole numbers. Many devices need something different: a control register of 8 bits, where each bit means something different. One bit says whether a motor is on, another whether a door is open. To work with the individual bits, the processor uses shifts and logic operations.

### Shifts

A **shift** moves every bit of a binary number a number of places to the left or to the right. The bits that move off the end are lost, and the empty places are filled. There are three kinds of shift, and they differ in what fills the empty places.

:::def Logical shift
A shift in which the bits move to the left or right and the empty places are filled with zeros. A bit shifted off the end is lost. A logical shift is for unsigned binary numbers and for bit patterns.
:::

:::def Arithmetic shift
A shift in which the sign bit is kept. An arithmetic shift right fills the empty places on the left with copies of the sign bit; an arithmetic shift left works like a logical shift left but is used on two's complement numbers. It is used to multiply or divide a two's complement number by a power of 2.
:::

:::def Cyclic shift
A shift in which the bit that falls off one end is put back in at the other end, so no bit is lost. (It is also called a rotation.)
:::

In the instruction set, only the logical shifts are provided, `LSL #n` and `LSR #n`. Arithmetic and cyclic shifts appear in questions that describe them, and you must be able to carry them out on a pattern.

:::eg Logical shifts on an 8-bit number
ACC holds 00010110 (denary 22). Show the result of `LSL #1` and of `LSR #2`.

`LSL #1`: every bit moves one place left and a 0 enters on the right: 00010110 becomes 00101100, which is 44.

`LSR #2`: every bit moves two places right and two 0s enter on the left: 00010110 becomes 00000101, which is 5. The two bits that fell off the end (10) are lost, so \(22 \div 4 = 5\) with the remainder discarded.
:::

:::key Shifts multiply and divide
A logical shift left by 1 place **multiplies** an unsigned binary number by 2. A shift left by \(n\) places multiplies by \(2^n\). A logical shift right by \(n\) places **divides** by \(2^n\), keeping the whole-number part (the remainder is lost). This only works if no 1-bit is lost off the end. Shifting is much faster than multiplication, and a compiler may use it.
:::

What if a 1 is lost? In 8 bits, shifting 10010110 (denary 150) left by one place gives 00101100 (denary 44), not 300: the leading 1 is lost, because 300 does not fit in 8 bits. A shift left loses the high-order bit just as an addition can overflow.

### Arithmetic shifts and the sign bit

For a two's complement number, the leftmost bit is the sign. A **logical** right shift puts a 0 in the sign position, so a negative number becomes positive, and the result is wrong. An **arithmetic** right shift puts a copy of the sign bit into the empty place, so the sign stays and the number is divided by 2.

:::eg Logical and arithmetic right shifts of a negative number
The 8-bit two's complement number 11110000 is \(-16\). Show a logical right shift and an arithmetic right shift by 1 place.

- Logical: 11110000 becomes 01111000, which is \(+120\). This is not \(-8\): the 0 put into the sign bit has made the number positive.
- Arithmetic: 11110000 becomes 11111000, which is \(-8\): the sign bit 1 is copied into the empty place, so the sign is kept and \(-16 \div 2 = -8\).
:::

An arithmetic shift left by 1 place of 11111000 (\(-8\)) gives 11110000 (\(-16\)), correctly doubled. But an arithmetic shift left of 01000000 (+64) gives 10000000, which is \(-128\): the sign has changed, so the answer is wrong. This is overflow: the result is too big for 8 bits.

### Cyclic shifts

In a cyclic shift, the bit that leaves one end enters at the other. A cyclic left shift of 10010110 by 1 place moves the leftmost 1 round to the right: 00101101. A cyclic right shift by 1 place moves the rightmost 0 round to the left: 01001011. Shifting left by 3 places gives 10110100. Since no bit is lost, shifting by 8 places gives back the original pattern.

### Masks: AND, OR and XOR

A **mask** is a bit pattern that is combined with another pattern, using AND, OR or XOR, to look at or change particular bits and leave the others alone. The logic works one bit at a time (bitwise): the left bit of one pattern is combined with the left bit of the other, and so on.

:::def Mask
A binary pattern used with a logic operation (AND, OR or XOR) to test, set, clear or toggle selected bits of another pattern, leaving the other bits unchanged.
:::

The bits of an 8-bit pattern are numbered from the right, starting at 0: the rightmost bit is **bit 0** and the leftmost is **bit 7**. A mask that picks out bit 3 has a 1 in the bit 3 place and 0 elsewhere: 00001000.

:::key Using masks
| To … | Use | Mask | Why it works |
|---|---|---|---|
| **test** a bit | AND | 1 in the bit to test, 0 elsewhere | AND with 0 gives 0, AND with 1 leaves the bit: the result is 0 only if the tested bit is 0 |
| **clear** a bit (make it 0) | AND | 0 in the bit to clear, 1 elsewhere | AND with 0 forces 0; AND with 1 leaves the other bits alone |
| **set** a bit (make it 1) | OR | 1 in the bit to set, 0 elsewhere | OR with 1 forces 1; OR with 0 leaves the other bits alone |
| **toggle** a bit (flip it) | XOR | 1 in the bit to flip, 0 elsewhere | XOR with 1 inverts the bit; XOR with 0 leaves it alone |
:::

:::eg Applying a mask
ACC holds 10110110. Show the result of (a) `AND B00001111`, (b) `OR B00000001`, (c) `XOR B11110000`.

(a) AND keeps only the bits that are 1 in both patterns. 10110110 AND 00001111 = 00000110. The top four bits are cleared and the bottom four are kept.

(b) OR puts a 1 where either pattern has one. 10110110 OR 00000001 = 10110111. Bit 0 has been set.

(c) XOR gives 1 where the bits differ. 10110110 XOR 11110000 = 01000110. The top four bits are flipped and the bottom four stay the same.
:::

Test, set and toggle all use the pattern *load the register, apply the mask, store it back (if it has changed)*. To clear bit 2, for example, the mask is 11111011.

### Monitoring and controlling a device

A device such as a greenhouse controller might use one byte of memory for its eight sensors (bit 3 is the door sensor, and so on) and one byte for its eight lights or switches. The program reads the sensor byte, tests one bit with a mask, and if the bit is set it changes a bit of the output byte.

:::eg Testing a bit and displaying the result
Location 109 is the status register of a machine. Bit 3 is 1 when the lid is open. The program below shows `Y` if the lid is open and `N` if it is closed. The ASCII codes of `N` and `Y` are 78 and 89. ACC is shown in binary in the trace table. Trace the program when location 109 holds 01101100.

```text
100          LDD STATUS
101          AND B00001000
102          CMP #0
103          JPN ISON
104          LDM #78
105          JMP SHOW
106  ISON:   LDM #89
107  SHOW:   OUT
108          END
109  STATUS: B01101100
```

| Address | Instruction | ACC | Compare | OUTPUT |
|---|---|---|---|---|
| 100 | LDD STATUS | 01101100 | | |
| 101 | AND B00001000 | 00001000 | | |
| 102 | CMP #0 | | FALSE | |
| 103 | JPN ISON | | | |
| 106 | LDM #89 | 01011001 | | |
| 107 | OUT | | | Y |
| 108 | END | | | |

The mask 00001000 clears every bit except bit 3. The result is 00001000 (not zero) because bit 3 of the status is 1, so the compare with 0 is FALSE, `JPN ISON` jumps to line 106, and the program outputs `Y`. If bit 3 had been 0, the AND would have given 00000000, the compare would have been TRUE, there would have been no jump, and `N` would have been output.
:::

:::eg Switching on a light
Location 108 holds the sensor byte and location 109 the light controller byte. When bit 3 of the sensor byte is set, bit 0 of the light byte must be set to 1 to switch the light on, leaving the other bits alone. Write the program and trace it when the sensor byte is 00101100 and the light byte is 01000100. [7 marks]

```text
100          LDD SENSORS
101          AND B00001000
102          CMP #0
103          JPE FINISH
104          LDD LIGHTS
105          OR B00000001
106          STO LIGHTS
107  FINISH: END
108  SENSORS: B00101100
109  LIGHTS: B01000100
```

| Address | Instruction | ACC | [LIGHTS] | Compare |
|---|---|---|---|---|
| start | | | 01000100 | |
| 100 | LDD SENSORS | 00101100 | | |
| 101 | AND B00001000 | 00001000 | | |
| 102 | CMP #0 | | | FALSE |
| 103 | JPE FINISH | | | |
| 104 | LDD LIGHTS | 01000100 | | |
| 105 | OR B00000001 | 01000101 | | |
| 106 | STO LIGHTS | | 01000101 | |
| 107 | END | | | |

- the sensor byte is loaded and tested with the mask B00001000 [B1]
- `CMP #0` compares the result with zero [B1]
- `JPE FINISH` skips the light code when the sensor bit is 0 [B1]
- the light byte is loaded [B1]
- `OR B00000001` sets bit 0 and leaves all other bits unchanged [B1]
- the new value is stored back with `STO` [B1]
- the program ends at `END` with the light byte 01000101 [B1]
:::

The light byte must be loaded first, changed and stored back, because the other bits of that byte belong to other devices: only bit 0 may change. Writing the value B00000001 straight into location 109 would have switched off every other bit. This is the reason for using a mask with `OR`.

## Practice

:::try Start easy, finish at exam standard
Q: Put each instruction in its group: `LDX`, `OUT`, `JMP`, `SUB`, `CMP`, `JPE`, `STO`.
A: Data movement: `LDX`, `STO`. Input and output: `OUT`. Unconditional jump: `JMP`. Arithmetic: `SUB`. Compare: `CMP`. Conditional jump: `JPE`. (`JPE` and `CMP` together form a decision.)
Q: What is the difference between `LDM #40` and `LDD 40`?
A: `LDM #40` loads the number 40 (immediate addressing). `LDD 40` loads the contents of the location at address 40 (direct addressing).
Q: ACC holds 7. State ACC after `ADD #5`, then `SUB #3`, then `INC ACC`.
A: After `ADD #5` it is 12, after `SUB #3` it is 9, and after `INC ACC` it is 10.
Q: IX holds 3. `LDX 100` is carried out. Which location is read?
A: \(100 + 3 = 103\).
Q: ACC holds B10110110. State the result of `AND B00001111`, and say what the mask has done.
A: B00000110. The mask cleared the top four bits and kept the bottom four.
Q: ACC holds B00000101. State the result of `LSL #3` and the denary values before and after.
A: B00101000. Before: 5. After: 40. A shift left by 3 multiplies by \(2^3 = 8\).
Q: A program reaches `CMP #9` with ACC holding 9, then `JPN DONE`. Does it jump?
A: No. The compare is TRUE (equal), and `JPN` only jumps if the result is FALSE, so the program continues with the next instruction.
Q: ACC holds 65. `ADD #2` and `OUT` are carried out. The ASCII code of `A` is 65. What is displayed?
A: ACC is 67, so the character displayed is `C`, two letters after `A`.
Q: A `JMR #4` instruction (relative jump: n locations forward from the instruction's own address) is stored at address 120. Where does the next instruction come from?
A: \(120 + 4 = 124\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The memory contents are shown in the table, and IX holds 1. State the contents of ACC after each instruction is carried out (each one starts again with the same memory).

| Address | Contents |
|---|---|
| 150 | 153 |
| 151 | 8 |
| 152 | 20 |
| 153 | 41 |
| 154 | 5 |

(a) `LDM #150` (b) `LDD 150` (c) `LDI 150` (d) `LDX 150`
A: (a) 150 [B1] (b) 153 [B1] (c) 41, because location 150 holds 153 and location 153 holds 41 [B1] (d) 8, because the address is \(150 + 1 = 151\) [B1]

Q: [4 marks] ★ Describe the difference between machine code and assembly language, and state the purpose of an assembler.
A: One mark for each point:

- machine code is written in binary, and can be executed directly by the processor [B1]
- assembly language uses mnemonics (and labels) instead of binary [B1]
- an assembler translates an assembly language program into machine code [B1]
- there is one machine code instruction for each assembly language instruction [B1]

Q: [5 marks] ★★ (#cs.assembly) A programmer has written this assembly language program. An assembler uses two passes to translate it. (a) Complete the symbol table made in the first pass. (b) Explain why the assembler needs a second pass.

```text
100  BEGIN:  LDD LIMIT
101  AGAIN:  SUB #1
102          STO LIMIT
103          CMP #0
104          JPN AGAIN
105          LDD TOTAL
106          END
107  LIMIT:  3
108  TOTAL:  20
```

H: Count the address of each line, including the data lines, and write down every label.
A: (a) The symbol table:

| Label | Address |
|---|---|
| BEGIN | 100 |
| AGAIN | 101 |
| LIMIT | 107 |
| TOTAL | 108 |

- BEGIN 100 and AGAIN 101 [B1]
- LIMIT 107 [B1]
- TOTAL 108 [B1]

(b) The instruction at address 100 uses the label `LIMIT` [B1], but `LIMIT` is not defined until address 107, so the assembler cannot know its address until it has read the whole program; the second pass can then use the symbol table [B1].

Q: [6 marks] ★★ A program reads a character from the keyboard. The ASCII code of `A` is 65 and of `*` is 42. Trace the program when the user types `A`, and state what is output when the user types `B` (code 66).

```text
100          IN
101          CMP #65
102          JPE SAME
103          INC ACC
104          OUT
105          END
106  SAME:   LDM #42
107          OUT
108          END
```

H: JPE only jumps if the compare was TRUE.
A: The trace for the character A:

| Address | Instruction | ACC | Compare | OUTPUT |
|---|---|---|---|---|
| 100 | IN | 65 | | |
| 101 | CMP #65 | | TRUE | |
| 102 | JPE SAME | | | |
| 106 | LDM #42 | 42 | | |
| 107 | OUT | | | * |
| 108 | END | | | |

- `IN` stores 65 in ACC [B1]
- `CMP #65` gives TRUE [B1]
- `JPE SAME` jumps to address 106 (the next row is 106, not 103) [B1]
- `LDM #42` loads 42 [B1]
- `OUT` outputs `*` [B1]

For `B`: ACC is 66, the compare is FALSE, there is no jump, `INC ACC` makes 67 and `OUT` displays `C`. [B1]

Q: [5 marks] ★★ Location 150 holds 12 and location 151 holds 30. Write an assembly language program, using only the instructions in the instruction set table, to add the two numbers, subtract 5, and store the result in location 152.
A: A model answer:

```text
LDD 150
ADD 151
SUB #5
STO 152
END
```

- `LDD 150` [B1]
- `ADD 151` [B1]
- `SUB #5` [B1]
- `STO 152` [B1]
- `END` [B1]

(Accept labels, or the instructions in a different order that gives the same result, such as `LDD 151` first.)

Q: [4 marks] ★★ An 8-bit register holds the status of a heating system. Write the single instruction that is carried out on ACC, after the register has been loaded into ACC, to (a) set bit 6, (b) clear bit 2, (c) toggle bit 0, (d) leave only bit 7 (so that the result is zero if bit 7 is 0).
H: Bit 0 is the rightmost bit. Use OR to set, AND to clear or test, and XOR to toggle.
A: (a) `OR B01000000` [B1] (b) `AND B11111011` [B1] (c) `XOR B00000001` [B1] (d) `AND B10000000` [B1]

Q: [8 marks] ★★★ (#cs.assembly) The four test marks of a student are stored in locations 150 to 153 (12, 30, 25 and 8). Location 161 holds 4, the number of marks. Write an assembly language program that uses the index register and a loop to add the four marks and store the total in location 160.
H: Set IX and the total to 0 before the loop; decide how the loop ends (the count in location 161 goes down by 1 each time).
H: Compare ACC with 0 after the count has been reduced and stored.
A: A model answer, which stores 75 in location 160:

```text
100          LDR #0
101          LDM #0
102          STO 160
103  LOOP:   LDX 150
104          ADD 160
105          STO 160
106          INC IX
107          LDD 161
108          DEC ACC
109          STO 161
110          CMP #0
111          JPN LOOP
112          END
150          12
151          30
152          25
153          8
161          4
```

- `LDR #0` to set IX to 0 [B1]
- the total in location 160 set to 0 before the loop [B1]
- a label at the first instruction of the loop body [B1]
- `LDX 150` to read the current mark, and `ADD 160` to add the running total [B1]
- `STO 160` to store the running total [B1]
- `INC IX` to move to the next mark [B1]
- the count in 161 loaded, reduced by 1 and stored [B1]
- `CMP #0` then `JPN LOOP` to repeat until the count is zero, then `END` [B1]

Q: [6 marks] ★★★ ACC holds the 8-bit pattern shown each time. Give the result of (a) a logical shift left by 2 places of 00001101, (b) a logical shift right by 3 places of 11001000, (c) an arithmetic shift right by 1 place of 11001000 (a two's complement number), (d) a cyclic shift left by 2 places of 10110001. For (a) and (b) say what has happened to the denary value.
H: Write each pattern with its eight bits and move them one place at a time.
A: (a) 00110100 [B1], which is 52: the value 13 has been multiplied by 4 [B1]
(b) 00011001 [B1], which is 25: the value 200 has been divided by 8 (200 ÷ 8 = 25) [B1]
(c) 11100100 [B1], the sign bit is copied into the empty place, so \(-56\) becomes \(-28\)
(d) 11000110 [B1], the two bits leaving on the left (10) re-enter on the right
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Location 130 holds a number between 0 and 25. Write an assembly language program that stores ten times that number in location 131, using `LSL` and `ADD` but no loop. Show that it works when location 130 holds 7.
H: \(10x = 8x + 2x\).
H: Store \(2x\) in location 131 first.
A: A model answer:

```text
LDD 130
LSL #1
STO 131
LDD 130
LSL #3
ADD 131
STO 131
END
```

- `LDD 130` then `LSL #1` to give \(2x\) [B1]
- `STO 131` to keep \(2x\) [B1]
- `LDD 130` again, then `LSL #3` to give \(8x\) [B1]
- `ADD 131` to add \(2x\) giving \(10x\) and `STO 131` [B1]
- with 7: \(7 \times 2 = 14\), \(7 \times 8 = 56\) and \(56 + 14 = 70\) is stored [B1]

Q: [7 marks] ★★★ Location 117 holds an 8-bit pattern, B10110100. Write a program that counts how many bits in the pattern are 1 and stores the count in location 118. Use location 119 as a loop counter. State the value stored for this pattern.
H: Test bit 0 with `AND #1`, add it to the count, then shift the pattern right by one place. Repeat 8 times.
H: The count of 1s in B10110100 is 4.
A: A model answer:

```text
100          LDM #0
101          STO 118
102          LDM #8
103          STO 119
104  LOOP:   LDD 117
105          AND #1
106          ADD 118
107          STO 118
108          LDD 117
109          LSR #1
110          STO 117
111          LDD 119
112          SUB #1
113          STO 119
114          CMP #0
115          JPN LOOP
116          END
117          B10110100
118          0
119          0
```

- the count initialised to 0 and the loop counter set to 8 [B1]
- `AND #1` (or an equivalent mask) isolates bit 0 [B1]
- the isolated bit (0 or 1) is added to the count and stored [B1]
- the pattern is shifted right with `LSR #1` and stored back, so the next bit reaches bit 0 [B1]
- the loop counter is reduced and stored [B1]
- `CMP #0` and `JPN LOOP` repeat until the counter is zero [B1]
- the value stored in location 118 is 4 [B1]
:::

:::quiz
? Which instruction loads the number 25 into the accumulator?
- `LDD 25`
+ `LDM #25`
- `LDI 25`
- `LDX 25`
> `LDM #25` is immediate addressing: the operand is the value. `LDD 25` loads the contents of location 25, `LDI 25` follows an address stored in location 25, and `LDX 25` adds IX to the address.
? Location 200 holds 205, location 205 holds 99 and IX holds 2. What does `LDI 200` load into ACC?
- 205
- 200
+ 99
- the contents of location 202
> Indirect addressing reads location 200 to get the address 205, and loads the contents of location 205, which is 99. The answer 205 would be direct addressing, and location 202 would be indexed addressing.
? What does `JPN LOOP` do?
- Jumps to LOOP if the last compare was True.
+ Jumps to LOOP if the last compare was False.
- Always jumps to LOOP.
- Jumps to LOOP if ACC is negative.
> JPN means jump if the compare result was False (not equal). JPE is the one that jumps when the compare was True.
? What is the job of the first pass of a two-pass assembler?
- To generate the machine code for each instruction.
+ To build the symbol table of labels and their addresses.
- To run the program.
- To find the logic errors in the program.
> The first pass reads the whole program and records each label with its address. Machine code is made in the second pass, once every label's address is known.
? Which mask and operation clears bit 3 of an 8-bit pattern and leaves the other bits alone?
- `OR B00001000`
- `AND B00001000`
+ `AND B11110111`
- `XOR B11110111`
> AND with 0 forces a bit to 0 and AND with 1 leaves it alone, so the mask has 0 only in bit 3. `OR B00001000` would set the bit, and `AND B00001000` would keep only bit 3.
? ACC holds B00001010 (10). What is the result of `LSL #2`?
- B00000010
+ B00101000
- B00001100
- B00010100
> Shifting left by two places multiplies by 4: 10 × 4 = 40, which is B00101000. B00010100 is a shift by one place (20).
? An 8-bit two's complement number 10000100 (\(-124\)) is shifted right by 1 place with a logical shift. Why is the result wrong?
- A logical shift cannot be done on 8-bit numbers.
+ A 0 enters the sign bit, so the result is positive: 01000010.
- The bits are rotated, so the number is unchanged.
- The right shift multiplies instead of dividing.
> A logical shift fills with zeros, which changes the sign bit of a negative number. An arithmetic shift copies the sign bit and gives 11000010, which is \(-62\).
? Which statement about `INC` is correct?
- `INC 150` adds 1 to the contents of location 150.
- `INC` only works on the program counter.
+ `INC IX` adds 1 to the index register, and `INC ACC` adds 1 to the accumulator.
- `INC` sets the compare result.
> INC and DEC take a register (ACC or IX) as the operand. To add 1 to a stored number you load it, add 1 and store it again.
:::

:::checklist What you can now do
- [ ] I can explain the relationship between assembly language and machine code, and state what an opcode, an operand, a mnemonic and an assembler are.
- [ ] I can describe the two passes of an assembler, complete a symbol table and translate a short program.
- [ ] I can trace a simple program in a trace table, with a memory table, loops, compares and output.
- [ ] I can name the groups of instructions and say what each instruction in the instruction set does.
- [ ] I can use immediate, direct, indirect, indexed and relative addressing and say which location is read.
- [ ] I can write short assembly language programs: add numbers, count with a loop, use IX with an array.
- [ ] I can carry out logical, arithmetic and cyclic shifts, left and right, and use shifts to multiply and divide.
- [ ] I can use AND, OR and XOR with masks to test, clear, set and toggle bits, and use them to monitor and control a device.
:::

:::recap
- Machine code is binary (opcode + operand) and is executed directly. Assembly language uses mnemonics and labels, one instruction for each machine instruction, and an assembler translates it.
- `LDM #n` loads a number; `LDD a` the contents of a; `LDI a` the contents of the location whose address is in a; `LDX a` the contents of location a + IX. `INC` and `DEC` change a register.
- Addressing modes: immediate (the value), direct (its address), indirect (the address of its address), indexed (address + IX), relative (offset from the current instruction).
- `CMP` records True or False; `JPE` jumps if True and `JPN` if False. Nothing else sets the result.
- Tracing: one row per instruction, a cell filled for each register or location that is written, and a jump shown by the next address.
- A two-pass assembler: pass 1 builds the symbol table (labels with addresses); pass 2 uses the opcode table and the symbol table to produce machine code. Two passes are needed because a label can be used before it is defined.
- A logical shift left multiplies an unsigned number by 2 per place; a logical shift right divides by 2 per place. An arithmetic right shift keeps the sign bit. A cyclic shift puts the bit that leaves back at the other end.
- Masks: AND tests or clears a bit, OR sets a bit, XOR toggles a bit. Bit 0 is the rightmost bit.
:::

:::links
- practise: [Assembly language: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/4-processor-fundamentals-/assembly-language-/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Bit manipulation: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/4-processor-fundamentals-/bit-manipulation/exam-questions/) · Save My Exams · shifts and masks questions with mark schemes [paid]
- explore: [A little-man computer simulator](https://www.101computing.net/lmc-simulator/) · 101 Computing · write a short assembly program and step through it
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on how processors and low-level code work
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · notes on every 9618 topic [paid]

Links checked 13 November 2026.
:::

Next: [System software: operating systems and translators](#cs.software)
