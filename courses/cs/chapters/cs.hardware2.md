@chapter cs.hardware2
@title Processors, parallel processing and virtual machines
@level a2
@paper CAIE 9618 Paper 3
@time 4–6 hours
@summary How RISC and CISC processors differ, how pipelining overlaps the stages of instructions and why registers matter, how interrupts are handled on each kind of processor, the four architectures SISD, SIMD, MISD and MIMD, what makes a massively parallel computer, and what a virtual machine is, with its uses, benefits and limitations.

:::why
A phone, a laptop and a weather-forecasting supercomputer all run programs, but their processors are built very differently, and the differences explain why a phone battery lasts all day, why a graphics card can draw millions of pixels at once, and why a single physical server can pretend to be ten computers. Paper 3 asks you to compare RISC with CISC, to complete a pipeline diagram, to identify an architecture from a description, and to give the benefits and limitations of a virtual machine. These are exact, short answers, and each follows from one or two ideas in this chapter.
:::

**Before you start**, you should know the fetch-execute cycle, the registers and interrupts, from [Processor fundamentals and the fetch-execute cycle](#cs.processor), and you should have seen assembly language, from [Assembly language and bit manipulation](#cs.assembly). Virtual machines and bytecode first appeared in [System software: operating systems and translators](#cs.software).

:::try Warm-up
Q: During the fetch stage, which register is increased by 1, and why? (from [Processor fundamentals and the fetch-execute cycle](#cs.processor))
A: The program counter, so that it holds the address of the next instruction.
Q: When does the processor check whether an interrupt is waiting? (from [Processor fundamentals and the fetch-execute cycle](#cs.processor))
A: At the end of each fetch-execute cycle, after the current instruction has been executed.
Q: A program is written in Java, compiled to bytecode and run on a phone. What runs the bytecode? (from [System software: operating systems and translators](#cs.software))
A: A virtual machine on the phone, which interprets the bytecode.
:::

## Instruction sets: RISC and CISC

Every processor understands a fixed list of instructions, such as the `LDD`, `ADD` and `STO` of the example instruction set in [Assembly language and bit manipulation](#cs.assembly). This list, and the way each instruction is stored in binary, is the processor's **instruction set**. Designers can choose between two philosophies.

- Give the processor **many powerful instructions**, so that one instruction can do a lot of work. Programs are short, but the processor's control unit is complicated.
- Give the processor **few, simple instructions**, each of which can be done very quickly. Programs are longer, but the processor is simpler and each instruction is fast.

:::def CISC (Complex Instruction Set Computer)
A processor with a large instruction set of many complex instructions. A single instruction may carry out several steps (for example, read two values from memory, add them and write the answer back) and may take several clock cycles. Instructions have different lengths.
:::

:::def RISC (Reduced Instruction Set Computer)
A processor with a small instruction set of simple instructions. Most instructions are carried out in one clock cycle, all instructions have the same length, and only the load and store instructions access memory. A RISC processor has many general purpose registers and uses pipelining.
:::

### The same job on each processor

Suppose a program must add the numbers in memory locations X and Y and store the result in Z. The instructions below are written for this explanation only. They are **not** the exam's instruction set. The clock cycle counts are numbers chosen for the example, to show the idea: real processors vary.

| Processor | Instructions | Number of instructions | Cycles in this example |
|---|---|---|---|
| CISC | `ADD Z, X, Y` (add two memory values and store the answer in memory) | 1 | 6 (the one instruction takes 6 cycles) |
| RISC | `LOAD R1, X` then `LOAD R2, Y` then `ADD R3, R1, R2` then `STORE R3, Z` | 4 | 4 (each instruction takes 1 cycle) |

The CISC version is shorter. It saves memory for the program, and a compiler has little work to do, because one instruction does what the programmer wrote. The RISC version needs four instructions, so the program is longer, but each instruction is simple, takes one cycle and has the same length. The calculation is done on **registers** (R1, R2, R3), and memory is touched only by the load and store instructions.

The next sections explain why designers choose the RISC approach for many modern processors, and the answer is largely **pipelining**.

### The differences

| Feature | RISC | CISC |
|---|---|---|
| Instruction set | Small, with simple instructions | Large, with many complex instructions |
| Time for an instruction | Mostly one clock cycle | Often several clock cycles, and it varies |
| Instruction length | All the same (fixed) | Different lengths (variable) |
| Registers | Many general purpose registers | Fewer registers |
| Access to memory | Only the load and store instructions; arithmetic uses registers | Many instructions can use memory directly |
| Control unit | Simple, built from fixed circuits | Complex, often driven by a stored set of micro-instructions (microcode: a small stored program inside the control unit that carries out each complex instruction) |
| Pipelining | Easy, and used heavily | Harder, because instructions differ in length and time |
| Program size | Larger (more instructions) | Smaller (fewer instructions) |
| Work for the compiler | More: it must build complex jobs from simple instructions and manage the registers | Less |
| Typical use | Processors in phones and tablets, where low power matters | Processors in many desktop and laptop computers |

:::key RISC and CISC in one line each
- **RISC:** few, simple, equal-length instructions, mostly one cycle each, many registers, load and store only touch memory, designed for pipelining.
- **CISC:** many complex, different-length instructions, several cycles each, fewer registers, instructions can work on memory directly, shorter programs.
:::

Two remarks help you to avoid wrong answers. First, RISC is **not** "slower because it has fewer instructions". A RISC program has more instructions to carry out, but each one is so quick and so regular that the processor can overlap them, and the overall speed can be as good as a CISC processor. Second, the two families have moved closer together. Many modern CISC processors translate their complex instructions into simple internal operations, and use pipelines too. The exam asks for the classic differences in the table.

:::warn "RISC is slower because it has fewer instructions"
The size of the instruction set says nothing about the speed of a program. What matters is the number of instructions in the program, the number of clock cycles each takes and the length of the clock cycle. RISC has more instructions per program but fewer cycles per instruction, and it overlaps them in a pipeline.
:::

## Pipelining

The fetch-execute cycle has stages. In the processor chapter you met them as fetch, decode and execute. For a pipeline they are usually divided into five, each of which takes one clock cycle and uses different parts of the processor.

:::def Pipelining
A technique that overlaps the stages of several instructions. While one instruction is being executed, the next is being decoded and the one after that is being fetched, so that every part of the processor is busy and one instruction can finish in every clock cycle.
:::

| Stage | Short name | What happens |
|---|---|---|
| Instruction fetch | IF | The instruction is read from memory (or the cache) into the processor, and the program counter is increased |
| Instruction decode | ID | The control unit decodes the instruction to find what it does and which registers it needs |
| Operand fetch | OF | The values that the instruction needs (the operands) are read from the registers |
| Instruction execute | EX | The ALU carries out the operation (or calculates an address) |
| Result write back | WB | The result is written to a register (or, for a store, to memory) |

:::analogy Washing, drying and folding
Three loads of laundry need washing, drying and folding, and each step takes an hour. Doing one load at a time takes 3 × 3 = 9 hours, with the washing machine idle while the dryer is working. Instead, start the second wash as soon as the first load moves to the dryer, and the third as soon as the second moves on. The three loads take 5 hours, and every machine is busy most of the time. A single load still takes 3 hours, but loads now **finish** every hour. A pipeline works in the same way.
:::

### The timing diagram

Four instructions, I1 to I4, are carried out without pipelining and with pipelining. A table with one row for each instruction and one column for each clock cycle is a **timing diagram**. First, with no pipelining, an instruction starts only when the one before has finished all five stages: the total is \(5 \times 4 = 20\) cycles.

With pipelining, instruction 2 starts one cycle after instruction 1, instruction 3 one cycle after instruction 2, and so on:

| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| I1 | IF | ID | OF | EX | WB | | | |
| I2 | | IF | ID | OF | EX | WB | | |
| I3 | | | IF | ID | OF | EX | WB | |
| I4 | | | | IF | ID | OF | EX | WB |

The four instructions take **8 cycles** instead of 20. The first instruction needs all 5 cycles to get through (the pipeline has to fill), and then one more instruction finishes in each of the 3 following cycles. In cycle 4, for example, four instructions are in progress at once: I1 is executing, I2 is in operand fetch, I3 is being decoded, and I4 is being fetched.

:::key Clock cycles with and without a pipeline
For \(n\) instructions and \(k\) stages (no branches or other delays):
- Without pipelining: \(k \times n\) cycles.
- With pipelining: \(k + n - 1\) cycles (the first instruction takes \(k\) cycles, and each of the other \(n - 1\) instructions finishes one cycle later).
:::

:::eg Completing a pipeline diagram (exam style)
A processor has a five-stage pipeline (IF, ID, OF, EX, WB) and carries out four instructions, I1 to I4, with no delays. The row for I1 is shown. Complete the table and state how many clock cycles the four instructions take. [4 marks]

| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| I1 | IF | ID | OF | EX | WB | | | |
| I2 | | | | | | | | |
| I3 | | | | | | | | |
| I4 | | | | | | | | |

The answer is the table shown just above, with a total of 8 clock cycles.

- I2 starts in cycle 2, one cycle after I1, and has the five stages in cycles 2 to 6 [B1]
- I3 starts in cycle 3 and has its stages in cycles 3 to 7 [B1]
- I4 starts in cycle 4 and has its stages in cycles 4 to 8 [B1]
- the total is 8 clock cycles, which is \(5 + 4 - 1\) [B1]
:::

In Python, the two formulas, with the number of extra cycles lost to a branch (explained below) as an option:

```python
STAGES = 5

def cycles_pipelined(instructions, branch_at=0):
    cycles = STAGES + instructions - 1
    if 0 < branch_at < instructions:
        cycles = cycles + (STAGES - 2)
    return cycles

def cycles_not_pipelined(instructions):
    return STAGES * instructions

for n in (1, 4, 10, 1000):
    print(n, "instructions: pipelined", cycles_pipelined(n), "cycles, not pipelined", cycles_not_pipelined(n), "cycles")
print("Jump at instruction 3 of 6:", cycles_pipelined(6, 3), "cycles")
```

Output:

```output
1 instructions: pipelined 5 cycles, not pipelined 5 cycles
4 instructions: pipelined 8 cycles, not pipelined 20 cycles
10 instructions: pipelined 14 cycles, not pipelined 50 cycles
1000 instructions: pipelined 1004 cycles, not pipelined 5000 cycles
Jump at instruction 3 of 6: 13 cycles
```

Look at the first two lines of the output. **A single instruction takes 5 cycles either way**: pipelining does not make any one instruction faster. What it improves is the **throughput**, the number of instructions finished each second. With 1000 instructions the pipeline needs 1004 cycles against 5000, a speed-up of \(5000 \div 1004 \approx 4.98\), nearly the number of stages. A clock of 2 GHz has a cycle of 0.5 nanoseconds, so the four instructions take \(8 \times 0.5 = 4\) ns with the pipeline and \(20 \times 0.5 = 10\) ns without it.

:::eg The time for a program
A program of 1 000 000 instructions runs on a processor with a clock speed of 2 GHz and a five-stage pipeline. Ignore jumps and stalls. How long does it take (a) with the pipeline and (b) if each instruction had to finish before the next one started?

One clock cycle lasts \(1 \div (2 \times 10^9) = 0.5\) ns.

(a) With the pipeline: \(5 + 1\,000\,000 - 1 = 1\,000\,004\) cycles, which is \(1\,000\,004 \times 0.5\ \text{ns} = 500\,002\) ns, about 0.5 ms.

(b) Without it: \(5 \times 1\,000\,000 = 5\,000\,000\) cycles, which is \(5\,000\,000 \times 0.5\ \text{ns} = 2\,500\,000\) ns = 2.5 ms.

The pipeline is almost five times as fast (\(5\,000\,000 \div 1\,000\,004 \approx 5.0\)). The four extra cycles that fill the pipeline are a tiny part of a long program, which is why the benefit is largest for long runs of instructions.
:::

### Try it: the pipeline widget

The widget draws the timing diagram for any number of instructions from 3 to 10, with pipelining switched on or off. Switch between the two and watch the number of cycles change. Then choose an instruction that is a **branch** and watch what happens to the instructions behind it (explained in the next section).

:::html
<div class="widget" data-w="cs-pipeline" data-n="6" data-branch="3"></div>
:::

### Why pipelines stall: hazards

A pipeline only runs at full speed if every instruction can go straight on to the next stage. When it cannot, the pipeline has to wait, and this is called a **hazard**.

:::def Pipeline hazard
A situation that stops the next instruction from going into its next stage in the next cycle, so the pipeline must wait or throw instructions away.
:::

- **A branch (a jump).** The processor does not know whether a jump is taken, or where to, until the instruction has been executed. By then the next instructions have already been fetched and are moving along the pipeline, and they are the wrong ones. They are **flushed** (thrown away) and fetching starts again at the target. In the five-stage pipeline here, a jump is settled at the end of the execute stage, and the three instructions behind it (in the IF, ID and OF stages) are flushed, which costs 3 clock cycles. (In real processors, the cost varies, and a technique called branch prediction guesses the outcome to reduce it.)
- **Waiting for data.** An instruction needs a value that an earlier instruction has not yet written back. The later instruction waits (a stall) until the value is ready.

:::eg The cost of a branch
Six instructions, I1 to I6, are listed in the order in which they are carried out in the five-stage pipeline. I3 is a jump that is taken, so I4 is the instruction at the jump's target, not the one that follows I3 in memory. How many clock cycles are needed? Compare with not pipelining.

With no jump, the six instructions would need \(5 + 6 - 1 = 10\) cycles. I3 finishes executing at the end of cycle 6 (it starts in cycle 3, and EX is its fourth stage). At that moment the three instructions fetched behind it (in IF, ID and OF) came from the wrong place, and are flushed. The right instruction I4 is fetched in cycle 7, three cycles later than it would have been. So every following instruction finishes 3 cycles later and the total is \(10 + 3 = 13\) cycles, which is what the Python program above prints for a jump at instruction 3 of 6.

Without pipelining, the six instructions need \(5 \times 6 = 30\) cycles, and a jump costs nothing extra because the next instruction is only fetched when the jump has finished. The pipeline is still more than twice as fast: \(30 \div 13 \approx 2.3\).
:::

:::eg A stall for data
Two instructions follow each other: `ADD R3, R1, R2` and then `SUB R5, R3, R4`. The second needs the value that the first writes into R3. In this model an instruction can only read a register in the cycle after the instruction that writes it has finished its write back stage. Show the timing diagram and the number of cycles for the two instructions.

`ADD` fetches in cycle 1, decodes in 2, reads its operands in 3, executes in 4 and writes R3 in cycle 5. `SUB` is fetched in cycle 2 and decoded in cycle 3. Its operand fetch would be in cycle 4, but R3 is not written until cycle 5, so `SUB` may not read it until cycle 6. It waits (stalls) for cycles 4 and 5.

| Instruction in the pipeline | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| ADD R3, R1, R2 | IF | ID | OF | EX | WB | | | |
| SUB R5, R3, R4 | | IF | ID | stall | stall | OF | EX | WB |

The two instructions take 8 cycles instead of the 6 that \(5 + 2 - 1\) gives with no delay. Real processors reduce such stalls by passing a result directly to the next instruction as soon as it is calculated (forwarding), and a compiler can reduce them by putting unrelated instructions in between.
:::

### Registers in a RISC processor

A RISC processor has a large number of general purpose registers, and its design depends on them.

:::key Why registers matter in a RISC processor
- Arithmetic and logic instructions work **only on registers**, so the operand fetch stage reads a register, which is very fast, and not memory, which is much slower. Each stage can take the same short time.
- **Only the load and store instructions use memory.** Other instructions never compete for memory, so the fetch stage can read the next instruction while an instruction is being executed.
- A **large number** of registers lets the compiler keep the values that a program is using in registers, which reduces the number of loads and stores and so the number of slow memory accesses.
- Registers can hold the values passed to a procedure, and some designs have separate sets of registers for interrupt routines, so that the interrupted program's values need not be copied to memory.
:::

### Why RISC suits pipelining

A pipeline works best when the stages are of equal length and every instruction goes through the same stages. RISC provides exactly that.

- **Fixed-length instructions** make fetching and decoding simple, because the processor knows where each instruction ends.
- **Most instructions take one cycle**, so each stage takes a similar time and no stage holds up the others.
- **Load and store only touch memory** and the others use registers, so there are fewer clashes and delays.
- A **simple control unit** leaves room on the chip for the extra registers.

A CISC instruction that takes six cycles, with a variable length and operands in memory, does not fit neatly into a five-stage pipeline, which is why pipelining is harder to do well in a CISC processor.

:::eg Spot the error: what pipelining does
Question: Explain what is meant by pipelining and why it makes a processor faster. [3 marks]

A student wrote:

```text
01  Pipelining overlaps the stages of different instructions, so that the next instruction starts before the last one has finished.
02  This makes each instruction run five times faster, because there are five stages.
03  More instructions are finished in a given time because each part of the processor is always busy.
```

Line 01 describes the overlap [B1]. **Line 02 is wrong: pipelining does not make any one instruction faster. An instruction still goes through all five stages and takes 5 cycles. The processor is faster because it finishes one instruction in every cycle (more throughput)** [B0]. Line 03 gives the reason for the improvement [B1]. The answer scores 2 out of 3.

The corrected line 02 is: "Each instruction still takes the same time, but a new instruction is finished in every clock cycle, so the number of instructions completed in a second increases."
:::

## Interrupts on RISC and CISC processors

You know the steps from [Processor fundamentals and the fetch-execute cycle](#cs.processor): the processor checks for interrupts at the end of each fetch-execute cycle, compares the priority, saves the registers, loads the address of the interrupt service routine (ISR) into the PC, runs the ISR, restores the registers and carries on. On a RISC or a CISC processor the steps are the same. What differs is how long they take and what the pipeline and the registers have to do.

**A CISC processor** has instructions of different lengths, some taking many cycles. The processor finishes the current instruction (or reaches a point inside a long instruction where it can stop safely) before it accepts the interrupt, so the delay before the ISR starts **varies** from one moment to another. The registers that the ISR will change are normally saved by copying them to a stack in memory, and copied back afterwards.

**A RISC processor** has short instructions of about the same length, so the delay before the interrupt is accepted is short and more predictable. A pipelined processor has several instructions part-done when the interrupt arrives. It must decide what to do with them: the ones that are far enough on are allowed to **finish**, and those that are not are **discarded**. The processor saves the address of the first instruction that has not been completed, so that after the ISR those instructions are fetched again. Because a RISC processor has many registers, some designs keep a separate set for the ISR. That means the interrupted program's values need not be copied to memory, so the switch to the ISR is quick.

:::key Interrupts and the pipeline
1. An interrupt arrives, and the processor accepts it at the end of an instruction (after checking its priority).
2. The instructions in the pipeline are completed or discarded.
3. The PC is saved, as the address of the first instruction that is not completed, with the other registers (copied to memory, or kept by using a separate register set).
4. The address of the ISR is loaded into the PC and the ISR runs.
5. The saved values are restored, the discarded instructions are fetched again, and the program carries on as if nothing had happened.
:::

:::eg An interrupt in a pipeline (exam style)
Instructions of a program are stored at consecutive addresses, one instruction in each address. A timer interrupt is accepted when the instruction at address 203 has just been completed. The instructions at 204, 205 and 206 are already in the pipeline but have not been executed. The processor discards them. The ISR starts at address 900. State what happens to the PC, and to the three instructions. [4 marks]

- the PC is saved with the other registers, and the value saved is 204, the address of the first instruction that has not been completed [B1]
- the instructions at 204, 205 and 206 are discarded, because they have not been executed, so nothing they started has to be undone [B1]
- the address of the ISR, 900, is loaded into the PC and the ISR runs [B1]
- when the ISR has finished, the saved values are restored, so the PC is 204 again and the three instructions are fetched again, and the program carries on [B1]
:::

## Flynn's classification: SISD, SIMD, MISD and MIMD

A computer can be described by how many **instructions** it carries out at the same time and how many pieces of **data** those instructions work on. A "stream" is a sequence of instructions or of data. This gives four architectures.

| | One data stream | Many data streams |
|---|---|---|
| **One instruction stream** | SISD | SIMD |
| **Many instruction streams** | MISD | MIMD |

:::def SISD (Single Instruction, Single Data)
An architecture in which one processor carries out one instruction at a time, on one item of data at a time. There is no parallel processing. A traditional single-core computer is SISD.
:::

:::def SIMD (Single Instruction, Multiple Data)
An architecture in which one instruction is carried out on many items of data at the same time, by several processing units under the control of one control unit. Graphics processors and vector processors use SIMD. (A vector processor is a processor whose instructions work on a whole list of numbers at once.)
:::

:::def MISD (Multiple Instruction, Single Data)
An architecture in which several processors carry out different instructions on the same item of data at the same time. It is rarely used, and is found mainly in systems that need to be fault tolerant (to keep working correctly even when part of the system fails), where several processors work on the same data and their answers are compared.
:::

:::def MIMD (Multiple Instruction, Multiple Data)
An architecture in which several processors, each with its own control unit, carry out different instructions on different data at the same time. Multicore processors, and clusters of computers, are MIMD. (A cluster is many complete computers joined by a fast network and used as one.)
:::

| Architecture | Example | Why it fits |
|---|---|---|
| SISD | A simple single-core computer or a basic microcontroller | One instruction after another, with one data item |
| SIMD | A graphics processor brightening every pixel of a photo | One operation (add 10) is wanted for a huge number of items |
| MISD | A fault-tolerant system in which several processors process the same sensor reading and the answers are compared | Rare: the same data, different processing |
| MIMD | A multicore processor running a browser, a music player and a download | Different programs, or different parts of one, on their own data |

:::eg SIMD, step by step
An image has 1024 pixels. A program must add 10 to the brightness of every pixel. How many steps does it take (a) on a SISD processor that adds to one pixel in each step, and (b) on a SIMD processor that adds to 8 pixels in each step?

(a) \(1024\) steps, one for each pixel.

(b) \(1024 \div 8 = 128\) steps. The same add instruction is applied to 8 pixels at once. SIMD is 8 times faster here, because every pixel needs exactly the same operation.
:::

:::eg Identify the architecture (exam style)
Name the architecture (SISD, SIMD, MISD or MIMD) described in each statement. [4 marks]

(a) A processor with four cores, in which each core runs a different program on its own data.
(b) A single-core processor that carries out one instruction at a time on one item of data.
(c) A graphics processor that applies one instruction to a whole row of pixels at once.
(d) A rarely used system in which several processors carry out different operations on one item of data, and compare the results to find faults.

- (a) MIMD [B1]
- (b) SISD [B1]
- (c) SIMD [B1]
- (d) MISD [B1]
:::

:::warn SIMD or MIMD?
Both use many processing units. In **SIMD** every unit does the **same instruction** at the same time, on different data. In **MIMD** every processor can do a **different instruction** on different data. A multicore laptop is MIMD, and the many small units of a graphics processor work in the SIMD way.
:::

## Massively parallel computers

:::def Massively parallel computer
A computer with a very large number of processors (thousands or more) that work on different parts of one problem at the same time. Each processor has its own memory, and the processors are connected by a very fast network that they use to pass data to each other.
:::

The characteristics to know:

- **a very large number of processors**, often thousands or even millions of cores;
- **each processor has its own memory**, so the processors do not fight over one shared memory (they pass messages to each other instead);
- a **fast interconnection network** joins the processors, because they must share intermediate results;
- the problem is **divided into parts** that run at the same time, so programs must be written specially, to be parallel;
- it is expensive to build and run (it needs a lot of power and cooling), so it is used only for tasks too big for other computers.

Uses include weather forecasting, climate models, simulating the folding of proteins, modelling the airflow around an aircraft, analysing very large sets of data and training large AI systems. These are problems that are made of many similar calculations, for example one for each square of a grid laid over the Earth.

### Why 1000 processors are not 1000 times faster

Part of almost every program cannot be shared, because one step needs the answer to the one before, or the processors have to wait for each other to pass data. That part limits the speed-up.

:::eg Limits to parallel speed-up
A task takes 100 seconds on one processor. 10 seconds of it cannot be shared among processors. The other 90 seconds can be divided equally among any number of processors. How long does the task take on 100 processors and on 1000 processors? What is the greatest possible speed-up?

On 100 processors the time is \(10 + 90 \div 100 = 10.9\) s, a speed-up of \(100 \div 10.9 \approx 9.2\).

On 1000 processors the time is \(10 + 90 \div 1000 = 10.09\) s, a speed-up of \(100 \div 10.09 \approx 9.9\).

However many processors are used, the 10 seconds remains, so the time can never be less than 10 s, and the speed-up can never be more than \(100 \div 10 = 10\). Ten times as many processors (from 100 to 1000) gained only a little. This is why a massively parallel computer is only worth building for problems that are almost completely parallel.
:::

A massively parallel computer is different from an ordinary multicore processor. A multicore processor has a few cores that share one memory, and is MIMD. A massively parallel computer has a vast number of processors, each with its own memory. Some are built as a cluster of many complete computers joined by a fast network.

| Feature | Multicore processor | Massively parallel computer |
|---|---|---|
| Number of processing units | A few (two, four, eight, or a few dozen) | Thousands or more |
| Memory | The cores share the memory of the computer (and perhaps a cache) | Each processor has its own memory |
| How they communicate | Through the shared memory and the buses inside the computer | Through a very fast network, by sending messages |
| Architecture | MIMD | MIMD (many are built from MIMD nodes, some parts may use SIMD) |
| Typical use | Everyday computers: running several programs at once | Huge scientific and engineering problems, such as forecasting the weather |

:::exam Choosing an architecture
When a question describes a task, ask two things. Is the **same instruction** applied to **many data items** (SIMD, for example the same change to every pixel)? Or are **different instructions** carried out at the same time on different data (MIMD, for example different programs, or different parts of a simulation)? A question that asks for a **characteristic** of a massively parallel computer wants the number of processors, the separate memory of each, the fast network and the splitting of the problem.
:::

## Virtual machines

:::def Virtual machine (VM)
Software that imitates (emulates) a complete computer. A program running in a virtual machine behaves as if it were running on a real computer with its own processor, memory and storage, although the virtual machine is only a program running on a real computer.
:::

:::def Host
The physical computer on which virtual machines run, together with the software (the hypervisor) that manages them.
:::

:::def Guest
An operating system, with its applications, that runs inside a virtual machine. A host can run several guests at the same time.
:::

:::def Hypervisor
The software that creates and manages virtual machines. It shares the host's processor, memory and storage among the guests and keeps the guests separate from each other.
:::

:::html
<figure class="fig"><svg viewBox="0 0 600 262" role="img" aria-label="A physical computer running three virtual machines. From the bottom: a wide box for the physical hardware (processor, memory, storage); above it a wide box for the hypervisor, which manages the virtual machines; above that three separate columns, each labelled Virtual machine 1, 2 or 3, each with a guest operating system box and an applications box on top of it."><rect class="fm s-acc sw2" x="20" y="210" width="560" height="40"/><text class="tl tc" x="300" y="235">Physical hardware: processor, memory, storage</text><rect class="fm2 s-acc sw2" x="20" y="160" width="560" height="40"/><text class="tl tc" x="300" y="185">Hypervisor (manages the virtual machines)</text><text class="tl tc" x="106.5" y="36">Virtual machine 1</text><rect class="f1 s-acc sw2" x="20" y="50" width="173" height="45"/><text class="tl tc" x="106.5" y="77">Applications</text><rect class="f1 s-acc sw2" x="20" y="105" width="173" height="45"/><text class="tl tc" x="106.5" y="132">Guest operating system</text><text class="tl tc" x="299.5" y="36">Virtual machine 2</text><rect class="f1 s-acc sw2" x="213" y="50" width="173" height="45"/><text class="tl tc" x="299.5" y="77">Applications</text><rect class="f1 s-acc sw2" x="213" y="105" width="173" height="45"/><text class="tl tc" x="299.5" y="132">Guest operating system</text><text class="tl tc" x="493.5" y="36">Virtual machine 3</text><rect class="f1 s-acc sw2" x="407" y="50" width="173" height="45"/><text class="tl tc" x="493.5" y="77">Applications</text><rect class="f1 s-acc sw2" x="407" y="105" width="173" height="45"/><text class="tl tc" x="493.5" y="132">Guest operating system</text></svg><figcaption>The hypervisor shares the one set of hardware among three virtual machines. Each guest operating system believes it has a whole computer to itself, and the three cannot see each other.</figcaption></figure>
:::

The hypervisor may run directly on the hardware, or as a program inside an ordinary operating system. Either way, it creates each virtual machine out of a share of the real processor time, memory and disk space. The guest operating system is not aware that the processor, memory and devices are imitations.

Hypervisors come in two forms. One runs **directly on the hardware** and has no ordinary operating system under it, which is the usual form on the servers of a data centre because it has the least overhead. The other runs as a **program inside an ordinary operating system** (the host operating system), which is the usual form on a personal computer where someone wants to try another operating system.

There is a second kind of virtual machine. A **process virtual machine** is made to run one program, not a whole operating system. The Java virtual machine from [System software: operating systems and translators](#cs.software) is an example: it runs bytecode, so the same bytecode works on every device that has such a virtual machine, whatever its processor.

### The roles of virtual machines

| Role | How a virtual machine helps |
|---|---|
| Running software for a different operating system | A computer that runs one operating system can run a guest with another, to use a program that is written for the guest |
| Testing | A programmer tests a new program on several operating systems, on one physical computer, and can restore a clean guest after each test |
| Running old software | An old program that needs an old operating system keeps working in a guest, after the real old computer has been thrown away |
| Server consolidation | Many separate servers, each using only a small part of its processor, are replaced by virtual machines on a few physical servers |
| Security and isolation | Suspicious software or a risky web page can be opened in a guest. If it harms the guest, the host is not affected |
| Cloud computing | A provider rents out virtual machines to customers, who share the provider's physical servers |

:::eg Server consolidation
A company has six old servers, each of which uses on average 12% of its processor. It plans to replace them with virtual machines on one new host. Each virtual machine adds an overhead of 2% of the host's processor. Will one host be enough?

The six servers need \(6 \times 12 = 72\%\) of a host. The overhead is \(6 \times 2 = 12\%\). The total is \(72 + 12 = 84\%\), which is less than 100%, so one host can run all six. It would have 16% of its capacity left, but little room for growth, so the company would probably choose a host with a margin of safety.
:::

### Benefits and limitations

:::cols
:::col Benefits
- **Several operating systems on one computer**, without buying more computers
- **Isolation:** a fault, a crash or malware in one virtual machine does not affect the host or the others
- **Lower costs:** fewer physical machines, so less money for hardware, power, cooling and space
- **Easy to copy, save and restore:** a virtual machine is a file, so a snapshot, a backup or a copy to another host is simple
- **Safe testing** of new software, and old software can be kept going
:::
:::col Limitations
- **Slower than the real hardware**, because the hypervisor adds overhead to every operation
- Every virtual machine takes a share of the **processor, memory and storage**, so the host must be powerful, and too many guests slow them all
- The guest **cannot use all of the hardware directly** (some special devices or graphics features are not available or are slower), so a test may not match a real machine
- **If the host fails, every guest fails with it**
- Setting up and managing many virtual machines needs skill, and a licence may be needed for each guest operating system
:::
:::

:::eg Virtual machine for a scenario (exam style)
A software company writes an application that must work on three different operating systems. It has one powerful computer. Describe how virtual machines help the company, and state one limitation. [4 marks]

- the one computer can run three virtual machines, each with a different guest operating system, so the application can be tested on all three without buying three computers [B1]
- a fault or crash in the application in one virtual machine does not affect the others or the host, and each can be reset to a clean state after a test [B1]
- limitation: a virtual machine is slower than a real computer because of the overhead of the hypervisor, so the speed measured in testing may not match the real one [B1]
- the host must share its processor and memory between all the guests, so it must be powerful, and devices such as graphics hardware may not behave as on a real computer [B1]
:::

:::exam Virtual machine questions in a scenario
Name the benefit or limitation, then tie it to the scenario in the question. "It is isolated" scores less than "a crash in the test virtual machine cannot damage the bank's live accounting system". For a limitation, "it is slower" should be followed by the reason: the hypervisor adds a layer, and the guests share one set of hardware.
:::

:::warn "A virtual machine is faster than the real thing"
A virtual machine runs on a real machine, and its work goes through the hypervisor, so it is not faster. The point of a virtual machine is flexibility, isolation and efficient use of hardware, not speed.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State two differences between RISC and CISC processors.
A: For example: RISC has a small set of simple instructions and CISC a large set of complex instructions; RISC instructions have a fixed length and CISC instructions vary in length; RISC has more registers.
Q: A processor has a five-stage pipeline. How many clock cycles do 3 instructions take (a) with pipelining, (b) without pipelining, and with no delays?
A: (a) \(5 + 3 - 1 = 7\) cycles. (b) \(5 \times 3 = 15\) cycles.
Q: Which architecture is described by "one instruction applied to many items of data at the same time"?
A: SIMD.
Q: Why do some designs of RISC processor keep separate registers for an interrupt routine?
A: So that the values of the interrupted program do not have to be copied to memory and back, which makes the change to the ISR and back quick.
Q: Give two uses of massively parallel computers.
A: Weather forecasting and climate modelling (also simulations of molecules, analysis of very large data sets).
Q: What is the name of the software that creates and manages virtual machines?
A: A hypervisor.
Q: A processor has a clock of 4 GHz. How long is one clock cycle, and how long do 8 cycles take?
A: A cycle is \(1 \div (4 \times 10^9) = 0.25\) ns, so 8 cycles take \(8 \times 0.25 = 2\) ns.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Give four differences between a RISC processor and a CISC processor.
A: One mark for each difference, up to four. Each must be a comparison. Four of these:

- RISC has a small set of simple instructions, whereas CISC has a large set of complex ones [B1]
- most RISC instructions take one clock cycle, whereas CISC instructions often take several [B1]
- RISC instructions are all the same length, whereas CISC instructions vary in length [B1]
- RISC has many general purpose registers, whereas CISC has fewer [B1]

(Also accept: in RISC only load and store instructions access memory, whereas in CISC many instructions can use memory directly; RISC is designed for pipelining, which is harder in CISC.)

Q: [4 marks] ★ Name the architecture (SISD, SIMD, MISD or MIMD) described in each statement. (a) The simple controller in a washing machine carries out one instruction at a time on one value at a time. (b) A vector processor adds two lists of 64 numbers, element by element, with a single instruction. (c) Each computer in a cluster runs its own part of a weather simulation on its own data. (d) Three flight computers each process the same speed reading with a different program, and their answers are compared to check that they agree.
A: One mark each.

- (a) SISD [B1]
- (b) SIMD [B1]
- (c) MIMD [B1]
- (d) MISD [B1]

Q: [4 marks] ★★ A processor has a five-stage pipeline: instruction fetch (IF), instruction decode (ID), operand fetch (OF), instruction execute (EX) and result write back (WB). Five instructions, J1 to J5, are carried out. Instruction J1 has IF in cycle 1, ID in cycle 2, OF in cycle 3, EX in cycle 4 and WB in cycle 5, and each of the others starts one cycle after the one before. Complete the table for J2 to J5 and state the number of cycles for the five instructions. There are no delays.

| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| J1 | IF | ID | OF | EX | WB | | | | |
| J2 | | | | | | | | | |
| J3 | | | | | | | | | |
| J4 | | | | | | | | | |
| J5 | | | | | | | | | |

A: The completed table:

| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| J1 | IF | ID | OF | EX | WB | | | | |
| J2 | | IF | ID | OF | EX | WB | | | |
| J3 | | | IF | ID | OF | EX | WB | | |
| J4 | | | | IF | ID | OF | EX | WB | |
| J5 | | | | | IF | ID | OF | EX | WB |

- J2 has its five stages in cycles 2 to 6 [B1]
- J3 has its five stages in cycles 3 to 7 [B1]
- J4 and J5 have their stages in cycles 4 to 8 and 5 to 9 [B1]
- the five instructions take 9 clock cycles, which is \(5 + 5 - 1\) [B1]

Q: [3 marks] ★★ Explain why a RISC processor is well suited to pipelining.
H: Think about the length of the instructions, the time each takes and how memory is used.
A: One mark for each point, up to three.

- all instructions are the same length, so fetching and decoding are simple and every instruction can pass through the same stages [B1]
- most instructions take one clock cycle, so the stages take equal times and no stage holds up the others [B1]
- only the load and store instructions use memory and the others use registers, so there are fewer delays and clashes, and the operand fetch is quick [B1]

Q: [4 marks] ★★ A small bank has bought new computers. Its accounting program only works on an old operating system that the new computers cannot run, and staff also need to open email attachments from unknown senders safely. Describe two ways in which virtual machines can help the bank, and give two limitations.
A: One mark for each point, up to four.

- a virtual machine with the old operating system as its guest runs the accounting program on the new hardware [B1]
- an attachment can be opened in a separate virtual machine, so that any malware stays inside it and the host and the other virtual machines are not affected (the virtual machine can then be deleted or restored) [B1]
- a virtual machine runs more slowly than a real computer because of the overhead of the hypervisor [B1]
- each virtual machine uses a share of the host's processor and memory, so the host must be powerful, and if the host fails all the virtual machines fail with it [B1]

Q: [6 marks] ★★★ (a) Describe two characteristics of a massively parallel computer. [2 marks] (b) A task takes 200 seconds on one processor. 20 seconds of it cannot be shared, and the other 180 seconds can be divided equally among any number of processors. Calculate the time it takes on 2000 processors. [2 marks] (c) A million processors are used instead of 2000. Explain why the time is hardly different. [2 marks]
H: The part that cannot be shared is the same however many processors there are.
A: (a) Any two of: a very large number of processors; each processor has its own memory; the processors are joined by a fast network; the problem is divided up and the parts are run at the same time [B1] [B1].

(b) The shared part takes \(180 \div 2000 = 0.09\) s [M1], so the total is \(20 + 0.09 = 20.09\) s [A1].

(c) The 20 seconds that cannot be shared remains whatever the number of processors, so the time can never be less than 20 s [B1]. With 2000 processors it is already 20.09 s, and with a million it is only 20.00018 s, so the extra processors save almost nothing [B1].

Q: [5 marks] ★★★ A pipelined RISC processor is running a program when an interrupt arrives, with instructions part-way through the pipeline. Describe how the processor deals with the interrupt, and explain why having many registers helps.
H: Say what happens to the instructions in the pipeline, and what is saved.
A: One mark for each point, up to five.

- the processor accepts the interrupt at the end of an instruction (after checking the priority) [B1]
- the instructions in the pipeline are either completed or discarded [B1]
- the address of the next instruction that has not been completed is saved (in the PC), with the contents of the other registers [B1]
- the address of the ISR is loaded into the PC, the ISR runs, and the saved values are then restored, so that the discarded instructions are fetched again and the program resumes [B1]
- with many registers, some can be kept for the ISR (or the values can be saved quickly), so the interrupted program's values do not all have to be copied to memory, and the change is quick [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A graphics processor adds 10 to the brightness of every pixel of an image that has 4096 pixels. (a) State how many steps are needed on a SISD processor that handles one pixel in each step. [1 mark] (b) State how many steps are needed on a SIMD processor that handles 16 pixels in each step, and the speed-up compared with (a). [2 marks] (c) The program is changed so that each pixel needs a different instruction, depending on its value. Explain why SIMD is a poor choice, and name the architecture that suits. [3 marks]
H: SIMD applies one instruction to all the data in a step.
A: (a) 4096 steps [B1].

(b) \(4096 \div 16 = 256\) steps [B1], a speed-up of \(4096 \div 256 = 16\) times [B1].

(c) SIMD carries out the same instruction on all the pixels in one step [B1], so pixels that need different instructions cannot be processed in the same step, and the advantage is lost [B1]. MIMD suits it, because each processor can carry out a different instruction on its own data [B1].

Q: [6 marks] ★★★ A five-stage pipeline (IF, ID, OF, EX, WB) carries out 8 instructions, listed in the order in which they are carried out. The fourth is a jump that is taken, so the fifth instruction in the list is at the jump's target and not the next one in memory. (a) State the number of clock cycles if there were no jump. [1 mark] (b) Explain why the jump adds cycles, and calculate the total with the jump. [3 marks] (c) The processor has a clock of 2.5 GHz. Calculate the time for the 8 instructions with the jump. [2 marks]
H: The jump is settled at the end of the execute stage, and the instructions fetched behind it are wrong.
A: (a) \(5 + 8 - 1 = 12\) cycles [B1].

(b) The jump is not settled until the end of its execute stage, and by then the three instructions behind it (in IF, ID and OF) are wrong and have to be flushed [B1]. The correct next instruction is fetched three cycles later than it would have been, so 3 cycles are added [B1]. The total is \(12 + 3 = 15\) cycles [B1].

(c) One cycle is \(1 \div (2.5 \times 10^9) = 0.4\) ns [B1], so the time is \(15 \times 0.4 = 6\) ns [B1].
:::

:::quiz
? Which statement about a RISC processor is correct?
- It has a large number of complex instructions of different lengths.
+ It has a small set of simple instructions, mostly of one clock cycle each, and only load and store access memory.
- It has very few registers.
- It cannot use pipelining.
> RISC means a reduced set of simple instructions of the same length, with many registers and load and store as the only instructions that touch memory. This makes pipelining easy. The first option describes CISC.
? A five-stage pipeline carries out 10 instructions with no delays. How many clock cycles are needed?
- 10
- 50
+ 14
- 15
> With a pipeline the time is \(k + n - 1 = 5 + 10 - 1 = 14\) cycles. 50 is the time without pipelining (\(5 \times 10\)), and 15 forgets that the first instruction fills the pipeline.
? What does pipelining improve?
- The time one instruction takes from start to finish.
+ The number of instructions finished in a given time.
- The size of the instruction set.
- The number of registers.
> One instruction still takes all five stages, but a new instruction finishes every cycle, so the throughput increases.
? What happens to the instructions behind a jump that is taken, when the jump is carried out in a pipeline?
- They are carried out as normal.
+ They have been fetched wrongly, so they are flushed and fetching starts at the target.
- They are carried out twice.
- The processor stops until the next interrupt.
> The processor does not know the outcome of the jump until it has been executed. The instructions that were fetched behind it are the wrong ones, and are thrown away.
? A graphics processor applies the same operation to a whole row of pixels in one step. Which architecture is this?
- SISD
+ SIMD
- MISD
- MIMD
> One instruction on many data items is SIMD. MIMD would mean different instructions on different data.
? Which statement describes a massively parallel computer?
- It has one very fast processor with a large shared memory.
+ It has a very large number of processors, each with its own memory, connected by a fast network, working on parts of one problem.
- It has two or four cores that share one cache.
- It runs one program on one data item at a time.
> A massively parallel computer has thousands or more processors, each with its own memory, connected by a fast network. Two or four cores sharing memory describe an ordinary multicore processor.
? What is the job of a hypervisor?
- To translate a program into machine code.
+ To create and manage virtual machines and share the host's hardware among them.
- To increase the clock speed of the processor.
- To connect the computer to the internet.
> The hypervisor creates the virtual machines, shares the processor, memory and storage among them and keeps them apart.
? Which is a limitation of a virtual machine?
- It cannot run more than one operating system.
+ It runs more slowly than the real hardware, because of the overhead of the hypervisor.
- It cannot be copied or saved.
- It makes malware spread to the host.
> The extra layer of the hypervisor adds overhead. Running several operating systems, easy copies and isolation are benefits.
:::

:::checklist What you can now do
- [ ] I can describe RISC and CISC processors and state the differences between them.
- [ ] I can describe how interrupts are handled on RISC and CISC processors.
- [ ] I can explain the importance of pipelining and of registers in a RISC processor, and complete a pipeline timing diagram.
- [ ] I can describe the four architectures SISD, SIMD, MISD and MIMD and give an example of each.
- [ ] I can describe the characteristics of massively parallel computers.
- [ ] I can explain what a virtual machine is, give examples of its role, and state its benefits and limitations.
:::

:::recap
- **CISC:** many complex instructions of different lengths, several cycles each, few registers, instructions work on memory, short programs, microcode. **RISC:** few simple instructions of equal length, mostly one cycle, many registers, only load and store touch memory, designed for pipelining, more work for the compiler.
- **Pipelining** overlaps the stages of instructions: fetch, decode, operand fetch, execute, write back. For \(n\) instructions and \(k\) stages: \(k + n - 1\) cycles with, and \(k \times n\) without. One instruction is no faster: the throughput is greater.
- A jump flushes the instructions behind it (three cycles lost in the five-stage example), and an instruction that waits for data stalls the pipeline.
- RISC suits pipelining: fixed-length instructions, one cycle each, register operands, only load and store use memory. Many registers keep data close to the ALU, and some designs keep a separate set for interrupt routines.
- Interrupts on both: the current instruction finishes, the registers and PC are saved, the ISR runs, the registers are restored. CISC delays vary with the instruction. A pipelined RISC processor completes or discards the instructions in the pipeline and fetches the discarded ones again.
- **SISD** one instruction, one data item. **SIMD** one instruction, many data items (graphics processors). **MISD** many instructions, one data item (rare, fault tolerance). **MIMD** many instructions, many data items (multicore, clusters).
- **Massively parallel computer:** very many processors, each with its own memory, joined by a fast network, working on parts of one problem. The part that cannot be shared limits the speed-up.
- **Virtual machine:** software that imitates a computer, run by a hypervisor on a host, with guest operating systems. Roles: other operating systems, testing, old software, server consolidation, isolation, cloud. Benefits: separation, lower cost, easy to copy and restore. Limitations: slower, shares the host's resources, limited access to hardware, one host failure affects all.
:::

:::links
- practise: [Processors, parallel processing and virtual machines: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on processors and computer architecture by university computer scientists
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · notes on every 9618 topic [paid]
- explore: [Nand2Tetris](https://www.nand2tetris.org/) · Nand2Tetris · build a computer from simple gates, to see how a processor is made (stretch)

Links checked 13 November 2026.
:::

Next: [Boolean algebra, Karnaugh maps, adders and flip-flops](#cs.boolean)
