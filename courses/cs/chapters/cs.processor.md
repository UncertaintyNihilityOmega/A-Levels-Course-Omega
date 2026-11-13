@chapter cs.processor
@title Processor fundamentals and the fetch-execute cycle
@level as
@paper CAIE 9618 Paper 1
@time 5–7 hours
@summary What is inside a processor and how it runs a program: the Von Neumann model and the stored program concept, the registers (PC, MAR, MDR, CIR, ACC, IX, status register), the ALU, control unit, clock and buses, what makes a processor faster, the ports on a computer, the fetch-execute cycle in register transfer notation, and how interrupts are detected and handled.

:::why
Every program you will ever run, from a game to a spreadsheet, is carried out by the same tiny loop inside the processor: fetch an instruction, work out what it means, do it, repeat. Paper 1 asks you to name the parts of the processor, to describe exactly what each register holds, to write the fetch-execute cycle as register transfers, and to explain how an interrupt pauses one program so that another job can be done. This chapter builds that picture from zero, and the next chapter, [Assembly language and bit manipulation](#cs.assembly), uses it to trace real programs.
:::

**Before you start**, you should know how binary numbers and hexadecimal work, from [Number systems and binary arithmetic](#cs.data). It also helps to have met main memory, RAM and ROM in [Computers and their components](#cs.hardware).

:::try Warm-up
Q: How many different values can a 4-bit binary number hold, and what is the largest denary value? (from [Number systems and binary arithmetic](#cs.data))
A: \(2^4 = 16\) different values, from 0 to 15. The largest denary value is 15 (binary 1111).
Q: Write the denary number 10 as 4-bit binary and as one hexadecimal digit. (from [Number systems and binary arithmetic](#cs.data))
A: Binary 1010 and hexadecimal A, because \(8 + 2 = 10\).
Q: In Python, what does `total = total + 1` do when `total` is 7? (from [Programming from zero](#cs.f.basics))
A: It works out the right-hand side first (7 + 1 = 8) and then stores 8 in `total`. The arrow in a register transfer, `PC ← [PC] + 1`, works the same way: read, calculate, store.
:::

## The Von Neumann model

A processor on its own can do nothing: it needs instructions to follow. The big question of early computer design was where those instructions should live. The first electronic machines were rewired by hand for each new job. The idea that changed this, set out in the 1940s by John von Neumann and others, is the one every ordinary computer still uses.

:::def Stored program concept
The idea that program instructions and the data they work on are both stored, in binary, in the same main memory. The processor fetches the instructions from memory one at a time, in sequence, and executes them.
:::

Because instructions are just numbers in memory, loading a different program means putting different numbers into memory. Nothing is rewired. The same computer can be a word processor now and a game a minute later. It also means that a program can be treated as data: a compiler is a program whose output is another program, and an operating system loads programs from a disk into memory before running them.

:::def Von Neumann model
A computer architecture in which a single processor reads both instructions and data from one shared main memory, using the same buses, and carries out the stored instructions one after another.
:::

The model has three parts that you must be able to name and place:

- the **processor** (CPU), which contains the control unit, the arithmetic logic unit and the registers;
- the **main memory**, which the Cambridge syllabus calls the **immediate access store (IAS)**, holding both the program and its data;
- the **input and output devices**, which connect to the processor through buses.

Memory is divided into numbered locations. The number of a location is its **address**. A location holds one item, such as a number or one instruction. The processor reads an item by sending the address along a bus; the memory answers with the contents.

:::analogy A kitchen
Think of a cook following a recipe. The recipe book and the ingredients are both kept on the same shelves (main memory), so the cook can only go to one place at a time. The cook (the processor) keeps a finger on the line of the recipe being followed (the program counter), reads one instruction, does it, then moves to the next line. A recipe that says "skip to step 8 if the oven is hot" is a jump: the finger moves somewhere else.
:::

### The processor in one picture

:::html
<figure class="fig"><svg viewBox="0 0 700 360" role="img" aria-label="Diagram of a Von Neumann computer. A large box labelled CPU contains the control unit, the arithmetic logic unit (ALU), the system clock, a cache, and a box of registers listing PC, MAR, MDR, CIR, ACC, IX and the status register. To the right, outside the CPU, are a box labelled main memory (IAS) and a box labelled input and output devices. Three lines labelled address bus, data bus and control bus run from the CPU to main memory. The address bus has an arrowhead only at the memory end, so it is one way. The data bus and control bus have arrowheads at both ends. A fourth line labelled same three buses joins the CPU to the input and output devices."><rect class="fm s-acc sw2" x="20" y="20" width="380" height="320"/><text class="tl tb" x="36" y="44">CPU (processor)</text><rect class="f1 s-acc sw2" x="40" y="60" width="160" height="60"/><text class="tl tc" x="120" y="86">Control unit</text><text class="tl tc" x="120" y="104">(CU)</text><rect class="f1 s-acc sw2" x="220" y="60" width="160" height="60"/><text class="tl tc" x="300" y="86">Arithmetic logic</text><text class="tl tc" x="300" y="104">unit (ALU)</text><rect class="fm2 s-acc sw2" x="40" y="140" width="160" height="40"/><text class="tl tc" x="120" y="165">System clock</text><rect class="fm2 s-acc sw2" x="40" y="200" width="160" height="130"/><text class="tl tc tb" x="120" y="226">Cache</text><text class="tl tc" x="120" y="256">copies of data and</text><text class="tl tc" x="120" y="276">instructions in use</text><rect class="fm2 s-acc sw2" x="220" y="140" width="160" height="190"/><text class="tl tc tb" x="300" y="162">Registers</text><text class="tl" x="240" y="186">PC</text><text class="tl" x="240" y="206">MAR</text><text class="tl" x="240" y="226">MDR</text><text class="tl" x="240" y="246">CIR</text><text class="tl" x="240" y="266">ACC</text><text class="tl" x="240" y="286">IX</text><text class="tl" x="240" y="306">Status register</text><rect class="fm s-acc sw2" x="540" y="60" width="140" height="140"/><text class="tl tc tb" x="610" y="122">Main memory</text><text class="tl tc" x="610" y="142">(IAS)</text><rect class="fm s-acc sw2" x="540" y="240" width="140" height="90"/><text class="tl tc" x="610" y="280">Input and output</text><text class="tl tc" x="610" y="300">devices</text><text class="tl tc" x="470" y="82">address bus</text><path class="ln thick" d="M400 90 L536 90" marker-end="url(#ah)"/><text class="tl tc" x="470" y="122">data bus</text><path class="ln thick" d="M400 130 L536 130" marker-end="url(#ah)"/><path class="ln thick" d="M440 130 L404 130" marker-end="url(#ah)"/><text class="tl tc" x="470" y="162">control bus</text><path class="ln thick" d="M400 170 L536 170" marker-end="url(#ah)"/><path class="ln thick" d="M440 170 L404 170" marker-end="url(#ah)"/><text class="tl tc" x="470" y="268">same three buses</text><path class="ln thick" d="M400 285 L536 285" marker-end="url(#ah)"/><path class="ln thick" d="M440 285 L404 285" marker-end="url(#ah)"/></svg><figcaption>The Von Neumann model. Addresses travel one way, from the processor to memory; data and control signals travel both ways. Input and output devices use the same buses (through their controllers and ports).</figcaption></figure>
:::

## Inside the processor

### The arithmetic logic unit, control unit and clock

:::def Arithmetic logic unit (ALU)
The part of the processor that carries out arithmetic operations (such as add and subtract), logical operations (such as AND, OR and NOT), shifts and comparisons on the data it is given.
:::

:::def Control unit (CU)
The part of the processor that fetches each instruction, decodes it and sends control signals to the other components (the ALU, the registers, memory and the input and output devices) so that the instruction is carried out, in the right order.
:::

:::def System clock
A circuit that produces a regular stream of electrical pulses. Every operation inside the computer is timed by these pulses, so that components stay synchronised. Its speed, the number of pulses (clock cycles) per second, is the clock speed, measured in hertz (Hz).
:::

The three work as a team. The control unit is the manager: it reads the instruction and tells the others what to do. The ALU is the calculator: it adds, compares and shifts when told to. The clock is the metronome: each step of the work happens on a tick. A processor with a clock speed of 2 GHz has \(2 \times 10^9\) ticks every second.

### Registers

:::def Register
A very small, very fast storage location inside the processor. It holds one item (a number, an address or an instruction) while the processor is working with it. Registers are much faster than main memory because they are part of the processor itself.
:::

Registers come in two kinds. A **general purpose register** can hold any data the programmer wants, and instructions can use it for any job. A **special purpose register** has one fixed job that the processor depends on. In the example instruction set of this course there is one general purpose register, the accumulator, and several special purpose ones. Learn each of the following with its exact job. This is the most reliably examined part of the topic.

:::def Program counter (PC)
A special purpose register that holds the address of the next instruction to be fetched. It is increased by 1 during each fetch, so that it points at the following instruction, and it is overwritten with a new address when the program jumps.
:::

:::def Memory address register (MAR)
A special purpose register that holds the address of the memory location that is about to be read from or written to.
:::

:::def Memory data register (MDR)
A special purpose register that holds the data or the instruction that has just been read from memory, or the data that is about to be written to memory. All data passing between the processor and main memory goes through it.
:::

:::def Current instruction register (CIR)
A special purpose register that holds the instruction that is currently being decoded and executed. The control unit splits it into an opcode (what to do) and an operand (what to do it to).
:::

:::def Accumulator (ACC)
A register that holds the data being worked on and the results of calculations done by the ALU. In this course's instruction set it is the one general purpose register.
:::

:::def Index register (IX)
A register that holds a number which is added to the address in an instruction to give the address actually used. It is used for indexed addressing, for example to step through the items of an array.
:::

:::def Status register (SR)
A register whose individual bits (flags) are set or cleared by the processor to record the result of an operation, for example whether a result was zero, whether it was negative, or whether it caused a carry or an overflow. Conditional jump instructions look at these bits.
:::

| Register | What it holds | One exam sentence |
|---|---|---|
| PC | an address | The address of the next instruction to be fetched. |
| MAR | an address | The address of the memory location being read from or written to. |
| MDR | data or an instruction | The value just read from memory, or about to be written to it. |
| CIR | an instruction | The instruction being decoded and executed. |
| ACC | data | Data being worked on, and the result of an ALU operation. |
| IX | a number | A value added to an address to form the address used. |
| SR | flag bits | The outcome of the last operation, used by conditional jumps. |

:::warn MAR and MDR are different jobs
The most common slip is to mix up the two. The MAR holds an **address** (where). The MDR holds **contents** (what). To read memory you put the address in the MAR and the contents arrive in the MDR. To write memory you put the address in the MAR, the value in the MDR, and the value is copied into the location. Likewise the PC holds the address of the next instruction, but the CIR holds the instruction itself.
:::

### Main memory: the immediate access store

:::def Immediate access store (IAS)
The main memory of the computer (RAM): the memory that the processor can address directly. It holds the program and the data that are currently in use. When the computer is switched off, the contents of RAM are lost, so programs are kept on backing storage and copied into the IAS to be run.
:::

The processor cannot run a program that is still on the hard disk or flash drive: the instructions have to be copied into the IAS first, because only the IAS (and the cache and registers) can be reached at the speed of the processor.

## Buses

A **bus** is a set of parallel wires that carries signals between components. Each wire carries one bit at a time, so a bus with 8 wires carries 8 bits at once. There are three buses between the processor and memory.

:::def Address bus
A bus that carries the address of a memory location or input and output device, from the processor to memory. It is one-way (unidirectional): the processor sends addresses and memory never sends one back.
:::

:::def Data bus
A bus that carries data and instructions between the processor, memory and the input and output devices. It is two-way (bidirectional): data is read from memory to the processor and written from the processor to memory.
:::

:::def Control bus
A bus that carries control signals between the processor and the other components, such as read and write signals, clock signals, and the interrupt request signal. It is two-way: the control unit sends read, write and clock signals, while devices send signals such as an interrupt request back to the processor.
:::

### How bus width matters

The **width** of a bus is the number of wires (bits) it has. The two widths that matter are different in effect.

:::key Address bus width and data bus width
- An address bus with \(n\) wires can send \(2^n\) different addresses, so the processor can address at most \(2^n\) memory locations. **Adding one wire doubles the memory that can be addressed.**
- A data bus with \(w\) wires carries \(w\) bits in one transfer. A wider data bus moves more data per transfer, so fewer transfers are needed to move the same amount of data.
:::

:::eg How much memory can be addressed? (with working)
A small control computer has an address bus with 16 wires and stores one byte in each location. (a) How many locations can it address? (b) How much memory is that? (c) A second model has a 32-bit data bus. How many transfers does it need to move a 128-bit item, compared with a model that has an 8-bit data bus?

(a) With 16 wires there are \(2^{16}\) different addresses: \(2^{16} = 65\,536\) locations.

(b) At one byte per location the memory is 65 536 bytes. As \(2^{16} = 2^{6} \times 2^{10} = 64 \times 1024\), that is 64 kibibytes (64 KiB).

(c) A 128-bit item on a 32-bit bus needs \(128 \div 32 = 4\) transfers. On an 8-bit bus it needs \(128 \div 8 = 16\) transfers, four times as many.
:::

:::warn The address bus is one way
Do not write that the address bus is "two-way" or that it "carries data". It carries addresses only, from the processor to memory. The data bus is the two-way one, and the control bus is two-way as well.
:::

## What makes a processor perform better

Performance means how much work a computer does in a given time. Four factors in the syllabus affect it. For each one, learn the effect and the reason, and the limit.

:::key Performance factors
- **Clock speed.** A higher clock speed gives more clock cycles per second, so more instructions are carried out per second. The limit: a faster clock makes the processor hotter and uses more power, and the memory and buses may not be able to keep up.
- **Number of cores.** A core is a complete processing unit (its own ALU, control unit and registers). A processor with more cores can run several streams of instructions at once, for example different programs, or different parts of one program. The limit: the program must be written so that its work can be split between cores, and the cores share memory and buses, so doubling the cores does **not** double the speed.
- **Bus width.** A wider data bus moves more bits per transfer, so data reaches the processor sooner. A wider address bus lets the processor address more memory, so larger programs and more programs can be held in the IAS without having to use slow backing storage.
- **Cache size.** Cache is a small amount of very fast memory, between the processor and the IAS, that holds copies of the instructions and data used most often or most recently. When the processor finds what it needs in cache, it avoids a slow read from main memory. A larger cache holds more, so it is more likely to contain what the processor asks for.
- **Type of processor.** Different processor designs do different amounts of work per clock cycle, so two processors with the same clock speed and number of cores can perform differently.
:::

:::def Cache
A small amount of very fast memory, placed between the processor and the main memory (or inside the processor), that stores copies of the data and instructions that are used frequently, so that they can be read much faster than from the IAS.
:::

:::def Core
A complete processing unit inside a processor chip, with its own ALU, control unit and registers. A multi-core processor has two or more cores, so it can carry out more than one set of instructions at the same time.
:::

:::eg Why a larger cache helps (illustration, not for the exam)
Suppose reading from cache takes 2 ns and reading from main memory takes 50 ns. A program makes 100 reads. If all 100 go to main memory, they take \(100 \times 50 = 5000\) ns. If 90 of them are found in cache and 10 are not, they take \(90 \times 2 + 10 \times 50 = 180 + 500 = 680\) ns. A larger cache raises the number found in cache, so the total time falls. (The numbers are invented to show the effect; the exam asks for the reason, not a calculation.)
:::

:::warn More cores do not mean twice the speed
"Dual core means twice as fast" is wrong. A single-threaded program uses only one core. A program that can be split up is limited by the parts that must run in order, and by the cores sharing memory. Say "can run more tasks at the same time, if the software is written to use them", not "faster".
:::

### Exam practice for this section

:::eg Explaining the effect of bus width (exam style)
A designer replaces a computer's 16-bit data bus with a 64-bit data bus. Explain how this affects the performance of the computer. [2 marks]

A wider data bus carries more bits in each transfer (64 instead of 16) [B1], so fewer transfers are needed to move the same instruction or data between memory and the processor, which means the program runs faster [B1].

(Accept "more data can be sent at the same time". Reject "the computer is faster" on its own, and "the bus is faster": the width is the number of bits, not the speed.)
:::

## Ports

A **port** is a socket on the computer into which a cable from an external device is plugged. Three are named in the syllabus.

:::def USB port
Universal Serial Bus. A port that transfers data in serial (one bit after another) in both directions between the computer and many types of device, such as keyboards, mice, printers and storage drives. One port can serve several devices through a hub, devices can be connected while the computer is on, and the cable can supply power to a small device.
:::

:::def HDMI port
High-Definition Multimedia Interface. A port that carries digital video and digital audio together in one cable, for connecting a computer to a screen, television or projector.
:::

:::def VGA port
Video Graphics Array. An older port that carries an analogue video signal only (no sound) to a screen. Because the signal is analogue, the picture can lose quality, especially over a long cable.
:::

| Port | Signal | Typical use |
|---|---|---|
| USB | digital, serial, data (and power) | keyboards, mice, printers, storage, phone charging |
| HDMI | digital video and audio | monitors, televisions, projectors |
| VGA | analogue video only | older monitors and projectors |

## The fetch-execute cycle

A program is a list of instructions in memory. To run it, the processor repeats the same cycle again and again, billions of times a second:

1. **Fetch** the next instruction from memory into the processor.
2. **Decode** it: work out what it means.
3. **Execute** it: carry it out.

:::def Fetch-execute cycle
The repeated process in which the processor fetches an instruction from main memory, decodes it and executes it. It continues until the program ends or the processor is stopped.
:::

### Register transfer notation

Exam questions ask for the cycle in **register transfer notation** (RTN): a short, exact way of writing what moves where. The arrow means "is loaded with". Square brackets mean "the contents of".

:::key Register transfer notation
- `[PC]` means "the contents of the PC".
- `[[MAR]]` means "the contents of the memory location whose address is in the MAR". (Double brackets: the contents of the contents.)
- `MAR ← [PC]` means "copy the contents of the PC into the MAR".
- `PC ← [PC] + 1` means "add 1 to the contents of the PC and store the answer in the PC".
:::

### The fetch stage

The fetch stage is the same for every instruction:

:::key The fetch stage
```text
MAR ← [PC]
PC ← [PC] + 1
MDR ← [[MAR]]
CIR ← [MDR]
```

1. The address of the next instruction is copied from the PC to the MAR.
2. The PC is increased by 1, so that it now points at the following instruction. (It can be done at the same time as the memory read in step 3, because it does not need the memory.)
3. The instruction at the address in the MAR is read from memory into the MDR.
4. The instruction is copied from the MDR into the CIR.
:::

The PC is incremented **during the fetch**, before the instruction is executed. This is why a jump instruction works by simply overwriting the PC: the new address replaces the already incremented one.

### The decode and execute stages

During **decode**, the control unit splits the instruction in the CIR into its two parts: the **opcode**, which says which operation to do, and the **operand**, which says what to do it to (an address or a number). It works out which control signals are needed. During **execute**, those signals are sent and the operation is carried out. What happens depends on the instruction. The steps below use the same notation; in these, "the address part of the instruction" is the number after the opcode.

| Instruction | Execute stage in register transfer notation |
|---|---|
| `LDM #5` (load the number 5 into ACC) | `ACC ← 5` |
| `LDD 200` (load the contents of address 200 into ACC) | `MAR ← 200`, then `MDR ← [[MAR]]`, then `ACC ← [MDR]` |
| `ADD 201` (add the contents of address 201 to ACC) | `MAR ← 201`, `MDR ← [[MAR]]`, then `ACC ← [ACC] + [MDR]` |
| `STO 202` (store ACC in address 202) | `MAR ← 202`, `MDR ← [ACC]`, then `[[MAR]] ← [MDR]` |
| `JMP 100` (jump to address 100) | `PC ← 100` |

The instructions are described fully in [Assembly language and bit manipulation](#cs.assembly). What matters here is the pattern: an instruction that needs a value from memory puts the address in the MAR and gets the value back in the MDR; an instruction that stores puts the value in the MDR and writes it to the address in the MAR; a jump simply changes the PC.

### Following the cycle on a real program

The program below adds two numbers. Instructions are stored from address 100, and the two numbers are stored in addresses 200 and 201. Address 202 is where the answer will go. In the tables, memory contents are written as assembly instructions to keep them readable; in the real machine they are binary numbers.

```text
100  LDD 200
101  ADD 201
102  STO 202
103  END
200  7
201  5
```

The first two instructions of the program, one register transfer per row. A cell is filled only on the row where the register changes. The PC starts at 100.

| Step | Register transfer | PC | MAR | MDR | CIR | ACC |
|---|---|---|---|---|---|---|
| start | | 100 | | | | |
| 1 | `MAR ← [PC]` | | 100 | | | |
| 2 | `PC ← [PC] + 1` | 101 | | | | |
| 3 | `MDR ← [[MAR]]` | | | LDD 200 | | |
| 4 | `CIR ← [MDR]` | | | | LDD 200 | |
| 5 | `MAR ← 200` | | 200 | | | |
| 6 | `MDR ← [[MAR]]` | | | 7 | | |
| 7 | `ACC ← [MDR]` | | | | | 7 |
| 8 | `MAR ← [PC]` | | 101 | | | |
| 9 | `PC ← [PC] + 1` | 102 | | | | |
| 10 | `MDR ← [[MAR]]` | | | ADD 201 | | |
| 11 | `CIR ← [MDR]` | | | | ADD 201 | |
| 12 | `MAR ← 201` | | 201 | | | |
| 13 | `MDR ← [[MAR]]` | | | 5 | | |
| 14 | `ACC ← [ACC] + [MDR]` | | | | | 12 |

Read down the PC column: it was 100, then 101 after the first fetch, then 102 after the second. The MAR is used twice per instruction here: first for the instruction, then for the data. The MDR is used twice as well: first it holds the instruction, then the number read from memory. Steps 15 to 21 do the same for `STO 202`, which ends with the value 12 being written into address 202, and then `END` stops the program.

### A compare and a conditional jump

A program that makes decisions needs two instructions working together: a **compare**, which checks two values and records the result in the status register, and a **conditional jump**, which looks at that result. The ALU does the comparing. The program below compares the accumulator with 5 and jumps to address 104 if they are equal.

```text
100  LDM #5
101  CMP #5
102  JPE 104
103  END
104  END
```

The table starts just after `LDM #5` has been executed (so the PC is 101 and the accumulator holds 5) and follows the next two instructions. The MAR and MDR rows are in the table so the steps are numbered correctly, but only the registers PC, CIR, ACC and the status register (SR) are shown.

| Step | Register transfer | PC | CIR | ACC | SR |
|---|---|---|---|---|---|
| start | | 101 | LDM #5 | 5 | |
| 1 | `MAR ← [PC]` | | | | |
| 2 | `PC ← [PC] + 1` | 102 | | | |
| 3 | `MDR ← [[MAR]]` | | | | |
| 4 | `CIR ← [MDR]` | | CMP #5 | | |
| 5 | `compare [ACC] with 5; status ← TRUE` | | | | TRUE |
| 6 | `MAR ← [PC]` | | | | |
| 7 | `PC ← [PC] + 1` | 103 | | | |
| 8 | `MDR ← [[MAR]]` | | | | |
| 9 | `CIR ← [MDR]` | | JPE 104 | | |
| 10 | `test the status register: TRUE` | | | | |
| 11 | `PC ← 104` | 104 | | | |

At step 11 the PC, which was about to point at `END` at address 103, is overwritten with 104. The next fetch therefore reads the instruction at 104. If the status register had held FALSE at step 10, the jump would not happen and the PC would stay at 103. Notice again that the incremented PC (step 7) is what the jump replaces.

### Try it: the cycle one transfer at a time

The widget below runs this program in the mode that shows every register transfer. Press Step to see each transfer, and watch the PC, MAR, MDR and CIR. Then change the program (for example, make the second number 9) and run it again.

:::html
<div class="widget" data-w="cs-asm" data-program="sum" data-mode="fe"></div>
:::

:::exam Describing the cycle
When a question says "describe the fetch-execute cycle" or "describe what happens during the fetch stage", write the register transfers **and** a sentence for each, in the right order: address from PC to MAR; PC incremented; instruction fetched from the address in MAR to the MDR; instruction copied to the CIR; then decoded by the control unit and executed. One mark per register or step: name the register each time.
:::

:::eg Spot the error: the fetch stage
Question: Write the register transfers for the **fetch** stage of the fetch-execute cycle. [4 marks]

A student wrote:

```text
01  MAR ← [PC]
02  MAR ← [MAR] + 1
03  MDR ← [[MAR]]
04  CIR ← [MDR]
```

Line 01 copies the address of the next instruction into the MAR [B1]. **Line 02 adds 1 to the MAR instead of the PC. The increment mark is lost, and the instruction is read from the wrong address in line 03** [B0]. Line 03 reads the contents of the addressed location into the MDR [B1]. Line 04 copies the instruction into the CIR [B1]. The answer scores 3 out of 4.

The correct second line is `PC ← [PC] + 1`: the PC is the register that always holds the address of the next instruction. Only the PC is incremented; the MAR is loaded each time from the PC.
:::

## Interrupts

So far the processor runs one program from start to end. But a computer must also react to events: a key is pressed, a printer runs out of paper, a timer expires. If the processor had to keep checking each device in turn it would waste most of its time. The solution is the interrupt.

:::def Interrupt
A signal sent to the processor, by hardware or by software, to say that something needs attention. The processor pauses the program it is running, deals with the event, and then carries on with the program.
:::

:::def Interrupt service routine (ISR)
The program code that is run to handle one particular kind of interrupt. Each type of interrupt has its own ISR (an interrupt service handling routine), stored in memory, and the processor loads its start address into the PC to run it.
:::

### Causes and applications of interrupts

| Source | Examples |
|---|---|
| Hardware | a key is pressed or the mouse is clicked; a printer is out of paper or has finished; a disk has finished transferring data; the power is failing |
| Software | an error such as a division by zero or an attempt to use memory that does not belong to the program; a program asking the operating system for input or output; a program that has ended |
| Timer | a clock signal at regular intervals, used by the operating system to share the processor between programs |

Interrupts have many applications: reading a keystroke immediately, so typing feels instant; letting a printer or disk work on its own and tell the processor when it needs more data; stopping a program that has made an error without crashing the whole computer; and the timer interrupt that lets the operating system run many programs at once, giving each a short turn.

### When interrupts are detected

The processor does not stop in the middle of an instruction. At the **end of each fetch-execute cycle**, after the current instruction has been executed, the processor checks whether an interrupt signal is waiting. If there is none, the next cycle starts as normal.

:::html
<figure class="fig small"><svg viewBox="0 0 320 370" role="img" aria-label="Flow diagram of the fetch-execute cycle with an interrupt check. Boxes from top to bottom: Fetch, Decode, Execute, then a box asking Interrupt flagged. Arrows run down between them. From the interrupt box a line labelled no goes along the right side back up to Fetch. A downward arrow labelled yes leads to a box reading Save registers, run ISR, restore, and a line from that box also joins the return line to Fetch."><rect class="fm s-acc sw2" x="10" y="15" width="150" height="40"/><text class="tl tc" x="85" y="40">Fetch</text><path class="ln" d="M85 55 L85 83" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="10" y="85" width="150" height="40"/><text class="tl tc" x="85" y="110">Decode</text><path class="ln" d="M85 125 L85 153" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="10" y="155" width="150" height="40"/><text class="tl tc" x="85" y="180">Execute</text><path class="ln" d="M85 195 L85 223" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="10" y="225" width="150" height="40"/><text class="tl tc" x="85" y="250">Interrupt flagged?</text><path class="ln" d="M160 245 L200 245 L200 35 L164 35" marker-end="url(#ah)"/><text class="tl" x="208" y="140">back to the</text><text class="tl" x="208" y="158">next fetch</text><text class="tl" x="208" y="232">no</text><path class="ln" d="M85 265 L85 297" marker-end="url(#ah)"/><text class="tl" x="95" y="287">yes</text><rect class="fm2 s-acc sw2" x="10" y="300" width="150" height="56"/><text class="tl tc" x="85" y="324">Save registers,</text><text class="tl tc" x="85" y="342">run ISR, restore</text><path class="ln" d="M160 328 L200 328 L200 245"/></svg><figcaption>The interrupt check sits at the end of every cycle. With no interrupt the cycle simply continues; with one the ISR is run first.</figcaption></figure>
:::

### How an interrupt is handled

:::key Handling an interrupt
1. An interrupt signal arrives on the control bus (or a flag is set).
2. The processor finishes the current instruction, then checks for interrupts at the end of the fetch-execute cycle.
3. It checks the **priority** of the interrupt. If it is lower than the priority of the program that is running, it waits (or is ignored for now); if it is higher, it is handled.
4. The contents of the registers (most importantly the PC, which says where to resume, and the ACC and the status register) are **saved**, usually on a stack in memory.
5. The address of the ISR is loaded into the PC.
6. The ISR runs, using the normal fetch-execute cycle.
7. When the ISR has finished, the saved register values are **restored**, including the saved PC.
8. The interrupted program carries on from where it stopped, as if nothing had happened.
:::

The saved registers are the whole point. If the processor did not restore the PC, it would not know where to continue; if it did not restore the ACC, a calculation that was half done would be spoiled. The interrupted program is never aware that it was paused.

:::eg Following one interrupt (exam style)
A program is stored from address 100. The instruction at address 102 has just been executed when a key-press interrupt arrives. The ISR for the keyboard starts at address 900. State the value in the PC (a) when the interrupt is detected, (b) just after the ISR's address has been loaded into it, and (c) after the ISR has finished. Explain why the value in (a) must be saved. [4 marks]

(a) The PC is 103: it was incremented during the fetch of the instruction at 102, so it holds the address of the next instruction [B1].

(b) The PC is 900, the start address of the ISR, which replaces the 103 [B1].

(c) The saved value 103 is restored to the PC [B1]. The value must be saved because the PC will be overwritten with the ISR's address; without the saved 103, the processor would not know where to resume the interrupted program [B1].
:::

:::warn Interrupts are not "polling"
An interrupt does not make the processor check each device in turn. The device sends the signal when it needs attention, and the processor responds at the end of the cycle. Also, the processor does not drop the instruction it was in the middle of: the current instruction always finishes first.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State what is stored in (a) the MAR, (b) the MDR, (c) the CIR.
A: (a) The address of the memory location being read from or written to. (b) The data or instruction just read from memory, or about to be written to it. (c) The instruction currently being decoded and executed.
Q: Which register is increased by 1 during each fetch, and why?
A: The program counter, so that it points at the next instruction in the sequence.
Q: An address bus has 10 wires. How many locations can be addressed?
A: \(2^{10} = 1024\) locations.
Q: Write the register transfers for `STO 202` after the instruction is in the CIR. Memory location 202 receives the contents of the accumulator.
A: `MAR ← 202`, then `MDR ← [ACC]`, then `[[MAR]] ← [MDR]`.
Q: A user plugs a monitor into a computer with a cable that carries digital video and sound. Which port is it, and which older port carries video only?
A: HDMI. VGA is the older port, and it is analogue.
Q: State two causes of a hardware interrupt and one cause of a software interrupt.
A: Hardware: a key press; a printer out of paper. Software: a division by zero (or a program asking for input or output).
Q: A computer has a 4 GHz clock. How many clock cycles does it make each second? Write the answer in standard form.
A: 4 GHz is \(4 \times 10^9\) hertz, so it makes \(4 \times 10^9\) cycles each second.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A processor contains an ALU, a control unit and a system clock. Describe the purpose of each.
A: One mark each.

- The ALU carries out arithmetic (such as add and subtract) and logic operations (such as AND and OR) on data [B1]
- The control unit fetches and decodes instructions and sends control signals to the other components so that they are carried out [B1]
- The system clock produces regular pulses that keep the operations of the components synchronised, and sets the speed at which instructions are processed [B1]

Q: [4 marks] ★ Four statements describe registers. Write the name of the register that matches each.
(a) It holds the address of the next instruction to be fetched.
(b) It holds the data that has just been read from memory.
(c) It holds the result of the last arithmetic operation done by the ALU.
(d) It holds the instruction that is being decoded.
A: (a) Program counter (PC) [B1] (b) Memory data register (MDR) [B1] (c) Accumulator (ACC) [B1] (d) Current instruction register (CIR) [B1]

Q: [2 marks] ★★ A computer's processor has a 32-bit address bus. State how many memory locations it can address, and explain why a student who thinks the memory is "32 locations" is wrong.
H: Each wire carries one bit, and a bit has two values.
A: \(2^{32}\) locations (4 294 967 296) [B1]. Each wire can carry 0 or 1, so \(n\) wires give \(2^n\) different addresses, not \(n\) of them [B1].

Q: [4 marks] ★★ A video-conferencing company is choosing a computer with a faster processor. Describe **two** factors that change the performance of a processor, giving the effect of each.
A: Any two factors with their effect, for example:

- Clock speed: a higher clock speed means more clock cycles per second [B1], so more instructions are carried out each second [B1]
- Number of cores: more cores [B1] means more instructions or tasks can be carried out at the same time, if the software can be divided between the cores [B1]

(Also accept, with the same two-part pattern: a bigger cache holds more frequently used data and instructions, so there are fewer slow reads from main memory; a wider data bus carries more bits at once, so fewer transfers are needed.)

Q: [5 marks] ★★ (#cs.processor) The accumulator holds 7. The instruction `ADD 201` has just been fetched into the CIR, and location 201 holds 5. Write the register transfers for the execute stage of this instruction, and state the value in the accumulator at the end.
H: The value is not in the CIR, only its address is. Which register is used to read memory?
A: One mark for each correct transfer.

```text
MAR ← 201
MDR ← [[MAR]]
ACC ← [ACC] + [MDR]
```

- `MAR ← 201` [B1]
- `MDR ← [[MAR]]` [B1]
- `ACC ← [ACC] + [MDR]` [B1]
- the contents of location 201 (5) are read into the MDR [B1]
- the accumulator holds 12 at the end [B1]

Q: [5 marks] ★★ A bus company in Lima has a computer that controls ticket machines. Describe how the processor deals with an interrupt from a ticket machine that has run out of paper.
A: One mark for each point:

- the processor completes the instruction it is executing, and at the end of the fetch-execute cycle it checks for an interrupt [B1]
- it checks the priority of the interrupt compared with the current task [B1]
- the contents of the registers (such as the PC and the ACC) are saved, for example on a stack [B1]
- the address of the interrupt service routine is loaded into the PC and the routine is run [B1]
- the saved register contents are restored when the routine finishes, and the interrupted program continues [B1]

Q: [6 marks] ★★★ (#cs.processor) The program below is stored in memory, starting at address 100. The PC holds 100. Complete the register transfers for the fetch stage of the instruction at address 100, then state the contents of the PC, MAR, MDR and CIR at the end of the fetch stage.

```text
100  LDM #9
101  STO 210
102  END
```

H: The fetch stage is the same for every instruction.
H: The MDR holds the instruction itself after the memory read.
A: The register transfers, one mark each:

- `MAR ← [PC]` [B1]
- `PC ← [PC] + 1` [B1]
- `MDR ← [[MAR]]` [B1]
- `CIR ← [MDR]` [B1]

The contents at the end of the fetch stage:

- PC 101 and MAR 100 [B1]
- MDR and CIR both hold `LDM #9` [B1]

Q: [6 marks] ★★★ A school in Lagos runs a computer room. The technician says: "Adding a second processor core will make every program twice as fast, and doubling the address bus width from 16 to 32 wires doubles the memory the computer can use." Evaluate each statement.
H: For the second statement, work out how many locations 16 and 32 wires give.
A: One mark per point.

- first statement: a second core lets two tasks run at the same time [B1]
- but it only helps if the program is written so that its work can be split between the cores, so a program that runs in one step at a time gains nothing [B1]
- the cores also share memory and buses, so the speed-up is less than double even with suitable software [B1]
- second statement: doubling the wires from 16 to 32 does not double the memory [B1]
- 16 wires give \(2^{16} = 65\,536\) locations and 32 wires give \(2^{32}\) locations, which is \(2^{16}\) (65 536) times as many [B1]
- adding **one** wire doubles the number of addresses [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A processor has a 12-bit address bus, a 16-bit data bus, and stores one 16-bit word in each memory location. (a) How many words of memory can it address, and how many bits is that in total? (b) A program holds 3000 instructions of 16 bits each. Show that the program fits in memory, and state how many locations are unused. (c) The designer wants the computer to have 10 000 more words of memory than it has now, using the smallest address bus that is wide enough. Find the width needed, and show that it works.
H: Work with powers of 2: \(2^{12}\), \(2^{13}\) and so on.
H: In (c) the total number of words wanted is the present 4096 plus 10 000.
A: (a) \(2^{12} = 4096\) words [B1], so \(4096 \times 16 = 65\,536\) bits [B1].
(b) 3000 words is less than 4096 [B1], so the program fits, and \(4096 - 3000 = 1096\) locations are unused [B1].
(c) The memory needed is at least \(4096 + 10\,000 = 14\,096\) words [B1]. \(2^{13} = 8192\) is too small and \(2^{14} = 16\,384 \ge 14\,096\), so 14 wires are needed [B1].

Q: [5 marks] ★★★ A mobile phone is running a music player when a text message arrives (a hardware interrupt) and the user, at the same moment, presses the screen to pause the music (also an interrupt). The text message has a lower priority than the screen press. Describe what the processor does, in order, and state what would go wrong if the processor did not save the registers when it handled the first interrupt.
H: Interrupts are checked at the end of each fetch-execute cycle, and the higher priority is handled first.
A: One mark per point.

- the current instruction of the music player is completed before anything else [B1]
- at the end of the cycle the processor checks the interrupts and finds both [B1]
- it handles the screen press first, because its priority is higher: registers saved, ISR address loaded into the PC, ISR runs [B1]
- registers are then restored, and the processor handles the text message the same way (or returns to the music player if the message has not been handled yet; both orders end by restoring the music player) [B1]
- without the saved PC, the processor could not return to the instruction after the one that was interrupted, and without the saved ACC, a calculation in the music player could be lost or corrupted [B1]
:::

:::quiz
? Which register holds the address of the next instruction to be fetched?
- MAR
- CIR
+ PC
- ACC
> The program counter holds the address of the next instruction. The MAR holds the address of the location being read or written at that moment, and the CIR holds the instruction itself.
? What does the register transfer `MDR ← [[MAR]]` mean?
- Copy the address in the MDR into the MAR.
+ Copy the contents of the memory location whose address is in the MAR into the MDR.
- Copy the contents of the MAR into the MDR.
- Add the MAR to the MDR.
> The double brackets mean "the contents of the location whose address is in the MAR". Copying the contents of the MAR itself would be written `MDR ← [MAR]`.
? An address bus has 8 wires. How many locations can the processor address?
- 8
- 16
+ 256
- 65 536
> Each wire carries a bit, so there are \(2^8 = 256\) different addresses. Answering 8 treats the width as the count, and 65 536 is the answer for 16 wires.
? Which statement about the buses is correct?
- The address bus is two-way and the data bus is one-way.
+ The address bus is one-way and the data bus is two-way.
- All three buses are one-way.
- The address bus carries data to the processor.
> Addresses only ever go from the processor to memory. Data goes both ways: read from memory and written to it.
? When is the PC incremented?
- After the instruction has been executed.
- Only when a jump is executed.
+ During the fetch stage, before the instruction is executed.
- When the interrupt is detected.
> The PC is increased in the fetch stage so that it already points at the next instruction. A jump then overwrites it with a new address.
? A computer's processor is changed from one core to four cores. What can be said for certain?
- Every program will now run four times faster.
+ Software written to use several cores can carry out more tasks at the same time.
- The clock speed has been multiplied by four.
- The computer can address four times as much memory.
> More cores allow tasks to run in parallel, but only if the software can be split up. Clock speed and memory are unaffected.
? When does the processor check whether an interrupt is waiting?
- At any moment, even in the middle of an instruction.
+ At the end of each fetch-execute cycle.
- Only when the program ends.
- Only at the start of the fetch stage of the first instruction.
> The current instruction always finishes first. The check at the end of every cycle lets the processor react quickly without breaking an instruction in the middle.
? Why are the registers saved before an interrupt service routine runs?
- To make the ISR run faster.
+ So that the interrupted program can carry on exactly where it stopped when the ISR has finished.
- To delete the program that was running.
- Because the ISR needs the PC to be zero.
> The ISR will overwrite the PC (and probably other registers). Restoring the saved values afterwards lets the interrupted program resume unaware that it was paused.
:::

:::checklist What you can now do
- [ ] I can explain the Von Neumann model and the stored program concept.
- [ ] I can state the purpose of the PC, MAR, MDR, CIR, ACC, IX and status register, and the difference between general and special purpose registers.
- [ ] I can describe the ALU, control unit, system clock and immediate access store.
- [ ] I can describe the address bus, data bus and control bus, and work out the memory addressed by an address bus width.
- [ ] I can explain how processor type, number of cores, bus width, clock speed and cache affect performance, with the limits.
- [ ] I can describe the USB, HDMI and VGA ports.
- [ ] I can write the fetch stage, and the execute stage of simple instructions, in register transfer notation.
- [ ] I can state the causes of interrupts and describe when they are detected and how they are handled, including the ISR.
:::

:::recap
- Stored program concept: instructions and data are both in main memory (the IAS) in binary, and instructions are fetched and executed in sequence.
- The CPU has an ALU (arithmetic and logic), a control unit (decodes, sends control signals), a clock (synchronises) and registers.
- PC: address of the next instruction. MAR: address being read or written. MDR: data or instruction just read or about to be written. CIR: the current instruction. ACC: data and ALU results. IX: modifies addresses. Status register: flag bits for the result of operations.
- Address bus: one way, processor to memory; \(n\) wires give \(2^n\) addresses. Data bus: two-way; its width is the bits per transfer. Control bus: two-way, carries read, write, clock and interrupt signals.
- Performance: higher clock speed (more cycles per second, more heat), more cores (only if the software can use them), wider data bus (fewer transfers), bigger cache (fewer slow reads from main memory).
- Ports: USB serial, many devices, power; HDMI digital video and audio; VGA analogue video only.
- Fetch: `MAR ← [PC]`, `PC ← [PC] + 1`, `MDR ← [[MAR]]`, `CIR ← [MDR]`; then decode and execute. `[ ]` is "contents of", `[[MAR]]` is "the contents of the location whose address is in the MAR".
- Interrupts are checked at the end of each cycle. If the priority is high enough: save the registers, load the ISR address into the PC, run the ISR, restore the registers, resume.
:::

:::links
- practise: [CPU architecture: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/4-processor-fundamentals-/central-processing-unit-cpu-architecture/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- explore: [A little-man computer simulator](https://www.101computing.net/lmc-simulator/) · 101 Computing · step through a tiny program and watch the fetch-execute cycle
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on how processors work, by university computer scientists
- read: [Computing basics](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · free explanations of bits, computers and the internet
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · notes on every 9618 topic [paid]

Links checked 13 November 2026.
:::

Next: [Assembly language and bit manipulation](#cs.assembly)
