@chapter cs.software
@title System software: operating systems and translators
@level as
@paper CAIE 9618 Paper 1
@time 4–6 hours
@summary What an operating system does and why every computer needs one, the utility programs that keep a computer healthy, how libraries and DLLs save a programmer's time, why programs need translating, how an assembler, a compiler and an interpreter differ, and which features of an IDE help you write and debug code.

:::why
Every program you have ever used, from a game to a spreadsheet, runs on top of system software that you rarely see. Paper 1 asks you to say what that software does, to name the utilities that keep a computer working, and to justify whether a program should be compiled or interpreted. These are short, precise questions where one correct term earns one mark.
:::

**Before you start**, you should know what the processor does with machine code from [Processor fundamentals and the fetch-execute cycle](#cs.processor), and what an assembler is from [Assembly language and bit manipulation](#cs.assembly).

:::try Warm-up
Q: What does an assembler translate, and into what? (from [Assembly language and bit manipulation](#cs.assembly))
A: It translates assembly language (mnemonics such as `LDD` and `ADD`) into machine code, the binary instructions the processor can execute.
Q: What is a buffer and why is one used between a processor and a printer? (from [Computers and their components](#cs.hardware))
A: A buffer is a temporary store for data in transit. The processor is much faster than the printer, so it fills the buffer quickly and carries on with other work while the printer empties it.
Q: What is an interrupt? (from [Processor fundamentals and the fetch-execute cycle](#cs.processor))
A: A signal sent to the processor, by hardware or software, to say that something needs attention at once. The processor finishes its current instruction, runs an interrupt service routine, then returns to what it was doing.
:::

## What an operating system is, and why you need one

Imagine a computer with no operating system. Every program you wrote would have to contain its own instructions for reading the keyboard, drawing on the screen and saving to the disk. Two programs running together would both try to use the same memory and the same disk sectors, and nothing would stop one from overwriting the other. Each new keyboard or printer would need new code in every program.

An operating system solves all of this once, for every program.

:::def System software
Programs that manage and operate the computer's hardware and provide a platform on which other software can run. The operating system, utility software, library programs and language translators are all system software.
:::

:::def Application software
Programs that let a user do a task that is useful to them, rather than running the computer itself. A word processor, a web browser and a program you write yourself are application software.
:::

:::def Operating system
System software that manages the computer's hardware and resources (processor time, memory, storage and peripherals), provides an interface for the user and for application programs, and controls how programs are run.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 300" role="img" aria-label="The operating system sits between the user and application software above and the hardware below. Arrows run down for requests and up for results. The operating system box lists memory, files, security, hardware and processes."><rect class="fm s-acc sw2" x="30" y="10" width="280" height="34"/><text class="tl tc" x="170" y="32">User</text><rect class="fm s-acc sw2" x="30" y="78" width="280" height="34"/><text class="tl tc" x="170" y="100">Application software</text><rect class="f1 s-acc sw2" x="30" y="146" width="280" height="76"/><text class="tl tc tb" x="170" y="168">Operating system</text><text class="tl tc" x="170" y="188">memory · files · security</text><text class="tl tc" x="170" y="206">hardware · processes</text><rect class="fm s-acc sw2" x="30" y="256" width="280" height="34"/><text class="tl tc" x="170" y="278">Hardware</text><line class="ln" x1="150" y1="48" x2="150" y2="74" marker-end="url(#ah)"/><line class="ln" x1="190" y1="74" x2="190" y2="48" marker-end="url(#ah)"/><line class="ln" x1="150" y1="116" x2="150" y2="142" marker-end="url(#ah)"/><line class="ln" x1="190" y1="142" x2="190" y2="116" marker-end="url(#ah)"/><line class="ln" x1="150" y1="226" x2="150" y2="252" marker-end="url(#ah)"/><line class="ln" x1="190" y1="252" x2="190" y2="226" marker-end="url(#ah)"/></svg><figcaption>The operating system is the layer between the programs a user runs and the hardware. Requests go down and results come back up.</figcaption></figure>
:::

When you press Save in a word processor, the word processor does not talk to the disk. It asks the operating system to save the file, and the operating system finds free space, controls the disk and reports back. The same program therefore works on any disk the operating system supports.

:::analogy
An operating system is like the manager of a large restaurant kitchen. The cooks (programs) do not decide who gets the oven, where the ingredients are kept or who may enter the cold store. The manager shares out the equipment, keeps the storeroom in order, stops two cooks using the same pan and keeps strangers out. The cooks just ask.
:::

:::key Why a computer needs an operating system
- It **hides the hardware**: programs ask the operating system to use a disk, screen or keyboard, so each program does not need code for every device.
- It **shares the resources** (processor time, memory, storage, peripherals) between the programs that want them, without clashes.
- It provides a **user interface**, so a person can start programs and manage files (a graphical interface, a touch interface or a command line).
- It **protects** the system: it keeps each program's memory separate and controls who may use which files.
:::

## The tasks an operating system manages

The syllabus names five areas of management. For each, learn what the operating system does and give a reason it is needed.

### Memory management

A program must be in main memory (RAM) to run. The operating system decides where each program is placed, gives it an area of memory when it starts and takes the memory back when it finishes, so the space can be reused. It also stops a program from reading or writing memory that belongs to another program or to the operating system itself. Without this protection, one faulty program could crash everything else.

### Process management

A **process** is a program that is being run. A modern computer seems to do many things at once: music plays while you type and a file downloads. A processor core runs only one instruction at a time, so the operating system uses **multitasking**: it gives each process a very short turn on the processor (a time slice) and switches between them so fast that they appear to run together. A part of the operating system called the scheduler decides which process runs next. (Scheduling methods are an A Level topic in [Operating systems: processes, scheduling and memory](#cs.os).)

:::def Multitasking
Running several processes at the same time, as far as the user can tell, by sharing the processor between them so that each gets short turns in rotation.
:::

### File management

Files must be stored in an organised way so they can be found again. The operating system keeps a **directory** (folder) structure, gives every file a name and a location, and tracks which sectors on the disk belong to which file. It lets you create, open, rename, copy, move and delete files. It also holds each file's **access rights** (who may read it, change it or run it).

### Security management

The operating system controls who may use the computer and what they may do. It manages **user accounts** and passwords, so each user must log in, and it applies access rights so that a user sees only their own files and cannot change system files. Many operating systems also include a firewall and malware protection, and record who did what in a log. (The measures themselves are the subject of [Security, privacy and data integrity](#cs.security).)

### Hardware management

Input, output and storage devices (peripherals) are all different. The operating system controls them through **device drivers**: small programs, one for each kind of device, that translate the operating system's general requests into the exact signals that device understands. It also uses buffers to even out speed differences, and it handles the interrupts that devices send when they need attention (a key is pressed, a print job finishes). When you plug in a new device, the operating system finds the correct driver.

:::def Device driver
A small program that lets the operating system communicate with a particular hardware device, by translating the operating system's general commands into commands that the device understands.
:::

:::key The five management tasks
| Task | What the operating system does |
|---|---|
| Memory | allocates RAM to processes, frees it afterwards, stops processes overwriting each other's memory |
| Process | shares the processor between processes (multitasking) and decides which runs next |
| File | organises directories, names and locations; creates, copies, moves and deletes files; keeps access rights |
| Security | user accounts, passwords, access rights, controlling who can use what |
| Hardware | device drivers, input and output, buffers, interrupts, peripherals |
:::

:::eg State four tasks of an operating system
State four tasks carried out by an operating system. [4 marks]

Each task is one mark, and the task must be a management area the syllabus names, not a vague phrase such as "runs the computer".

- Memory management: allocating memory to programs and protecting it from other programs. [B1]
- Process management (multitasking): sharing the processor between programs. [B1]
- File management: organising files in directories and controlling their access rights. [B1]
- Hardware (peripheral) management: using device drivers to control input and output devices. [B1]

(Security management, with user accounts and access rights, would earn the mark in place of any of these. "Provides a user interface" is also accepted by many mark schemes, but learn the five above first.)
:::

:::warn An operating system is not the same as the programs on top of it
A web browser, a word processor and a game are application software. They run on the operating system. A common wrong answer to "what does an operating system do?" lists what applications do ("lets you write documents").
:::

## Utility software

An operating system keeps the computer running, but it cannot do every housekeeping job well. **Utility software** is a set of programs that does the maintenance jobs: preparing storage, protecting it, tidying it and copying it. Most operating systems include some utilities, and others are bought or downloaded separately.

:::def Utility software
System software that carries out maintenance and housekeeping tasks for the computer, such as checking for malware, tidying a disk or making a copy of the data.
:::

You need six utilities for Paper 1. For each one, you must say what it does and why it is needed.

:::cols
:::col Disk formatter
Prepares a storage device for use. It divides the surface into **tracks and sectors** and sets up an empty file system (the index that records where files are stored). It is needed for a new disk, or to wipe and reuse an old one: formatting a used disk removes access to the files that were on it.
:::
:::col Virus checker
Scans files, and the programs that are running, for malware. It compares them with a database of known malware patterns (and watches for suspicious behaviour), then quarantines or deletes what it finds. It is needed because malware can damage or steal data, and it must be **updated regularly** so that it knows about new malware.
:::
:::

:::def Defragmentation
A utility that reorganises the files on a magnetic disk so that every file is stored in neighbouring sectors, and the free space is gathered together, which makes reading the files faster.
:::

When you save, edit and delete files for months, free space on a disk is scattered in small gaps. A new file is then split into **fragments**, stored in whichever gaps are free. Reading it means the read-write head must jump from place to place.

:::html
<figure class="fig small"><svg viewBox="0 0 340 180" role="img" aria-label="Two rows of twelve disk sectors. Before defragmentation, file A is in sectors 1, 3 and 7, file B in sectors 2, 5 and 10, file C in sectors 4, 8 and 12, and sectors 6, 9 and 11 are free. After defragmentation, A fills sectors 1 to 3, B sectors 4 to 6, C sectors 7 to 9, and sectors 10 to 12 are free."><text class="tl" x="26" y="20">Before</text><rect class="f1 s-acc sw2" x="26" y="28" width="24" height="28"/><text class="tl tc" x="38.0" y="47">A</text><rect class="f2 s-acc sw2" x="50" y="28" width="24" height="28"/><text class="tl tc" x="62.0" y="47">B</text><rect class="f1 s-acc sw2" x="74" y="28" width="24" height="28"/><text class="tl tc" x="86.0" y="47">A</text><rect class="f3 s-acc sw2" x="98" y="28" width="24" height="28"/><text class="tl tc" x="110.0" y="47">C</text><rect class="f2 s-acc sw2" x="122" y="28" width="24" height="28"/><text class="tl tc" x="134.0" y="47">B</text><rect class="fm s-acc sw2" x="146" y="28" width="24" height="28"/><rect class="f1 s-acc sw2" x="170" y="28" width="24" height="28"/><text class="tl tc" x="182.0" y="47">A</text><rect class="f3 s-acc sw2" x="194" y="28" width="24" height="28"/><text class="tl tc" x="206.0" y="47">C</text><rect class="fm s-acc sw2" x="218" y="28" width="24" height="28"/><rect class="f2 s-acc sw2" x="242" y="28" width="24" height="28"/><text class="tl tc" x="254.0" y="47">B</text><rect class="fm s-acc sw2" x="266" y="28" width="24" height="28"/><rect class="f3 s-acc sw2" x="290" y="28" width="24" height="28"/><text class="tl tc" x="302.0" y="47">C</text><text class="tl" x="26" y="84">After</text><rect class="f1 s-acc sw2" x="26" y="92" width="24" height="28"/><text class="tl tc" x="38.0" y="111">A</text><rect class="f1 s-acc sw2" x="50" y="92" width="24" height="28"/><text class="tl tc" x="62.0" y="111">A</text><rect class="f1 s-acc sw2" x="74" y="92" width="24" height="28"/><text class="tl tc" x="86.0" y="111">A</text><rect class="f2 s-acc sw2" x="98" y="92" width="24" height="28"/><text class="tl tc" x="110.0" y="111">B</text><rect class="f2 s-acc sw2" x="122" y="92" width="24" height="28"/><text class="tl tc" x="134.0" y="111">B</text><rect class="f2 s-acc sw2" x="146" y="92" width="24" height="28"/><text class="tl tc" x="158.0" y="111">B</text><rect class="f3 s-acc sw2" x="170" y="92" width="24" height="28"/><text class="tl tc" x="182.0" y="111">C</text><rect class="f3 s-acc sw2" x="194" y="92" width="24" height="28"/><text class="tl tc" x="206.0" y="111">C</text><rect class="f3 s-acc sw2" x="218" y="92" width="24" height="28"/><text class="tl tc" x="230.0" y="111">C</text><rect class="fm s-acc sw2" x="242" y="92" width="24" height="28"/><rect class="fm s-acc sw2" x="266" y="92" width="24" height="28"/><rect class="fm s-acc sw2" x="290" y="92" width="24" height="28"/><text class="tl tc" x="38.0" y="140">1</text><text class="tl tc" x="62.0" y="140">2</text><text class="tl tc" x="86.0" y="140">3</text><text class="tl tc" x="110.0" y="140">4</text><text class="tl tc" x="134.0" y="140">5</text><text class="tl tc" x="158.0" y="140">6</text><text class="tl tc" x="182.0" y="140">7</text><text class="tl tc" x="206.0" y="140">8</text><text class="tl tc" x="230.0" y="140">9</text><text class="tl tc" x="254.0" y="140">10</text><text class="tl tc" x="278.0" y="140">11</text><text class="tl tc" x="302.0" y="140">12</text><text class="tl tc" x="170" y="164">sector number</text></svg><figcaption>Three files on a magnetic disk. Before, each file is in three fragments; after defragmentation, each is in one run of neighbouring sectors. Blank sectors are free.</figcaption></figure>
:::

A magnetic disk has to move a head to the right track and wait for the sector to arrive under it; every jump costs time. The program below counts the jumps needed to read each file in the figure, for the layout before and after defragmentation. A jump is needed whenever the next sector is not the one directly after the last.

```python
before = "ABACBFACFBFC"
after = "AAABBBCCCFFF"


def jumps(layout, name):
    sectors = [i + 1 for i, letter in enumerate(layout) if letter == name]
    count = 0
    for k in range(1, len(sectors)):
        if sectors[k] != sectors[k - 1] + 1:
            count = count + 1
    return count


for name in "ABC":
    print(name, jumps(before, name), jumps(after, name))
```

Output:

```output
A 2 0
B 2 0
C 2 0
```

Each file needs two jumps before defragmentation and none afterwards, so every file is read faster. This is the whole point of the utility.

:::warn Defragmentation is for magnetic disks only
A solid state drive has no moving head, so reading scattered sectors costs no extra time and there is nothing to gain. Every move rewrites data, and flash memory wears out after a limited number of writes, so defragmenting an SSD only shortens its life.
:::

:::cols
:::col Disk contents analysis and disk repair
**Analysis** reports how the space on a disk is used: which folders and file types are largest, and which files are old, duplicated or temporary, so the user can free up space. **Repair** scans a disk for errors, such as damaged sectors or a corrupted index of files, and fixes what it can, marking bad sectors so that they are not used again. Both are needed because disks fill up and develop faults.
:::
:::col File compression
Makes a file smaller by recoding its data without losing any of it (lossless compression, from [Images, sound and compression](#cs.media)), and expands it again when needed. It is needed to save storage space and to make files faster to send over a network. Several files can be packed into one compressed file.
:::
:::

:::def Back-up software
A utility that makes copies of files or whole disks on a separate storage device or location, so that the data can be restored if the original is lost, damaged or deleted.
:::

Back-up software usually runs on a schedule, so no one has to remember. A **full back-up** copies everything. An **incremental back-up** copies only the files that changed since the previous back-up, which is much quicker and uses less storage; to restore, you need the last full back-up plus every incremental after it. A copy kept on the same disk would be lost with the disk, so back-ups are kept on a different device or in a different place, such as another building or a cloud service.

:::eg Explaining utility software
A school in Dhaka has an old computer with a magnetic hard disk. Files take longer and longer to open. (a) Name the utility that is most likely to help, and explain how it helps. [3 marks] (b) Explain why the same utility is not needed for a computer that uses a solid state drive. [2 marks]

(a) The utility is a **defragmentation** program. [B1] Over time the files have been split into fragments in scattered sectors [B1], and defragmentation moves the fragments so that each file is in neighbouring sectors, so the read-write head makes fewer movements and the file opens faster [B1].

(b) A solid state drive has no moving read-write head [B1], so scattered data takes no longer to read, and the extra writes would only wear out the flash memory [B1].
:::

:::exam Name the utility, then explain
"Describe what a utility does" gets marks for the specific action (moves fragments together, scans for known malware patterns, copies files to another device). "It speeds up the computer" is too vague on its own. Always say what the utility changes or checks, then why that helps.
:::

## Program libraries and DLL files

Programmers do not write every routine from scratch. Sorting a list, finding a square root, drawing a window and connecting to a network are needed in thousands of programs, so someone writes and tests the routine once and shares it.

:::def Program library
A collection of pre-written and tested routines (functions and procedures) that a programmer can include in a program instead of writing the code again.
:::

Python has many libraries, called modules. This program uses two from the standard library:

```python
import math
import statistics

print(math.sqrt(144), math.floor(7.9))
print(statistics.mean([4, 8, 15, 16, 23, 42]))
```

Output:

```output
12.0 7
18
```

The programmer wrote none of the square-root, rounding or averaging code. That saves time, and the routines have been tested by many people, so they are less likely to contain faults.

A library routine can reach a finished program in two ways. With **static linking**, the routine's code is copied into the program's executable file when the program is built. With **dynamic linking**, the program only holds a reference to the routine; the routine stays in a separate file, a **DLL** (dynamic link library), which is loaded and linked when the program runs.

:::def Dynamic link library (DLL)
A library file whose routines are not copied into a program but are loaded and linked to it at run time. One DLL file can be used by many programs at the same time.
:::

:::key Benefits of libraries and DLLs to the developer
- **Saves time**: the routines already exist, so the developer writes less code.
- **Reliable**: library routines have been tested, so fewer faults.
- **Specialist code**: the developer can use routines, such as graphics or encryption, that would take experts a long time to write.
- **Smaller programs** (DLL): the code is not copied into each executable, so each program file is smaller.
- **One copy shared** (DLL): several programs use the same DLL, so it takes up storage (and, when loaded, memory) once.
- **Easy to update** (DLL): replacing the DLL with a corrected version fixes every program that uses it, with no need to recompile them.
:::

A DLL has drawbacks as well. If the file is missing, deleted or replaced by a different version, the programs that depend on it may not start or may behave differently. The developer must also supply the right DLLs with the program.

:::warn DLLs do not make a program run faster
The benefits are sharing and size. Loading a DLL at run time is, if anything, a small extra step. If a question asks for a benefit to the developer, "the program runs faster" earns no mark.
:::

:::eg Benefits of a DLL (exam style)
A developer is writing a map-drawing program. The program uses a DLL that contains routines for drawing curves. Explain two benefits to the developer of using the DLL. [4 marks]

- The developer does not have to write and test the curve-drawing code, because it already exists in the DLL [B1], which saves development time [B1].
- When the authors of the DLL fix a fault, the new file can replace the old one [B1], so the program is corrected without being recompiled [B1].

(Other accepted pairs: the program file is smaller because the code is not copied into it; several programs share one copy of the DLL.)
:::

## Why programs need translating

A processor can execute only **machine code**: binary instructions, as in [Processor fundamentals and the fetch-execute cycle](#cs.processor). Nobody writes large programs in binary. People write in a high-level language such as Python, or in assembly language, and a **translator** program converts that into machine code.

:::def Source code
The program as the programmer wrote it, in a high-level language or in assembly language.
:::

:::def Object code
The machine code produced by a translator from the source code. A processor can run it directly.
:::

There are three kinds of translator.

:::def Assembler
A translator that converts a program written in assembly language into machine code. Each assembly instruction becomes one machine code instruction (a one-to-one translation).
:::

:::def Compiler
A translator that converts the whole of a high-level language program into object code in one go, and reports any errors it finds. The object code is saved and can be run later without the compiler.
:::

:::def Interpreter
A translator that takes a high-level language program one statement at a time, translates that statement and executes it at once, before moving on to the next. It does not produce a saved object code file.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 320" role="img" aria-label="Two columns. The compiler column: source code goes to the compiler, which produces object code, which runs on the CPU, and the compiler is not needed to run it. The interpreter column: source code goes to the interpreter, which translates one line at a time and runs on the CPU, with no object code kept."><text class="tl tc tb" x="80" y="20">Compiler</text><text class="tl tc tb" x="260" y="20">Interpreter</text><rect class="fm s-acc sw2" x="10" y="34" width="140" height="34"/><text class="tl tc" x="80" y="56">Source code</text><rect class="fm s-acc sw2" x="190" y="34" width="140" height="34"/><text class="tl tc" x="260" y="56">Source code</text><rect class="f1 s-acc sw2" x="10" y="102" width="140" height="34"/><text class="tl tc" x="80" y="124">Compiler</text><rect class="f1 s-acc sw2" x="190" y="102" width="140" height="44"/><text class="tl tc" x="260" y="119">Interpreter</text><text class="tl tc" x="260" y="138">one line at a time</text><rect class="fm s-acc sw2" x="10" y="170" width="140" height="34"/><text class="tl tc" x="80" y="192">Object code</text><rect class="fm s-acc sw2" x="10" y="238" width="140" height="34"/><text class="tl tc" x="80" y="260">Runs on the CPU</text><rect class="fm s-acc sw2" x="190" y="176" width="140" height="34"/><text class="tl tc" x="260" y="198">Runs on the CPU</text><text class="tl tc" x="260" y="230">no object code kept</text><text class="tl tc" x="80" y="292">the compiler is not</text><text class="tl tc" x="80" y="310">needed to run it</text><line class="ln" x1="80" y1="72" x2="80" y2="98" marker-end="url(#ah)"/><line class="ln" x1="80" y1="140" x2="80" y2="166" marker-end="url(#ah)"/><line class="ln" x1="80" y1="208" x2="80" y2="234" marker-end="url(#ah)"/><line class="ln" x1="260" y1="72" x2="260" y2="98" marker-end="url(#ah)"/><line class="ln" x1="260" y1="150" x2="260" y2="172" marker-end="url(#ah)"/></svg><figcaption>A compiler translates the whole program once and produces object code. An interpreter translates and runs one line at a time.</figcaption></figure>
:::

The two high-level translators work quite differently, and that is where the exam marks are.

:::analogy
A compiler is like translating a whole book into another language before publishing it. Translating takes a long time, but afterwards anyone can read the finished book quickly, and without you. An interpreter is like a live interpreter at a meeting: it speaks each sentence just after it is said, so you hear a reply straight away, but the work is repeated every time and you need the interpreter in the room.
:::

:::cols
:::col Compiler: benefits
- The translation is done **once**; the object code then runs **fast**, because no translation happens while it runs.
- The user does not need the compiler, only the object code, so the **source code stays hidden**.
- The compiler can examine the whole program and optimise it.
:::
:::col Compiler: drawbacks
- After any change the whole program must be **recompiled** before it can be tested, which is slow during development.
- Errors are reported **after the whole program** has been translated, as a list, and the program cannot run until they are fixed.
- The object code works only on one type of processor and operating system; a different type needs a recompile.
:::
:::

:::cols
:::col Interpreter: benefits
- The program can be **run at once**, even part-finished, so testing and changing code is quick.
- It **stops at the first error** and shows the line, which makes the fault easier to find.
- The same source code runs on any computer that has an interpreter for the language.
:::
:::col Interpreter: drawbacks
- It is **slower** to run, because each statement is translated every time it is run (a statement inside a loop is translated again on every pass).
- The **interpreter must be present** on the computer that runs the program.
- The user receives the **source code**, so it is not hidden.
:::
:::

Here is a Python program that stops at an error half way through. The first two lines run and print, because the interpreter has already executed them; the third causes a run-time error and stops the program, and the fourth never runs.

```text
print("Step 1 done")
print("Step 2 done")
print(10 / 0)
print("Step 4 never runs")
```

Output and error message:

```text
Step 1 done
Step 2 done
Traceback (most recent call last):
  File "demo.py", line 3, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

A compiler would behave differently with a **syntax error**, such as a missing bracket on line 3: it would refuse to produce any object code, and nothing at all would run. (Python also checks the whole file for syntax errors before it starts running, so for a syntax error it reports the line without running any statement. For the exam, describe the interpreter as executing and stopping at the first error.)

:::eg Justify a compiler and an interpreter (exam style)
A software company in Manila writes a payroll program and sells it to businesses. (a) Justify the use of an interpreter while the program is being developed. [3 marks] (b) Justify the use of a compiler for the version that is sold. [3 marks]

(a) The programmers can run the program after each small change without waiting for the whole program to be translated [B1]. The interpreter stops at the first error and shows the line [B1], which makes faults easy to find and correct [B1].

(b) The compiled program runs faster, because it is already in machine code and nothing is translated when it runs [B1]. The customers need only the object code, not the compiler [B1], and the source code is not given to them, so competitors cannot copy it [B1].

"Justify" asks for a reason with evidence from the scenario. A bare list of compiler facts, with no link to development or to selling the program, would score lower.
:::

### Partial compilation and interpretation

Some languages, such as Java, use both. The compiler translates the source code into **bytecode**, an intermediate code that is not the machine code of any real processor. A **virtual machine**, a program that behaves like a computer, then interprets the bytecode on the user's device.

:::def Bytecode
An intermediate code, between source code and machine code, produced by a compiler for a language such as Java. It is run by an interpreter called a virtual machine rather than directly by the processor.
:::

This combines the strengths of both. The compiler finds all syntax errors before the program is released, and the translation is already partly done, so the bytecode runs faster than interpreting source code. The same bytecode runs on any device that has a virtual machine, whatever its processor, so the company compiles once instead of once for every type of device. The source code is not given to the user.

## Integrated development environments (IDEs)

Writing code in a plain text editor works, but programmers use an **IDE**: one program that combines a code editor, a translator and debugging tools.

:::def Integrated development environment (IDE)
A program that provides a programmer with the tools needed to write, run, test and debug code in one place: a code editor, a translator and debugging tools.
:::

Python comes with a simple IDE called IDLE. It has a colour-coded editor, suggestions as you type and a debugger window with all the tools described here, in a simple form. Larger IDEs have more. The syllabus groups the features by what they do for the programmer.

:::cols
:::col Writing code
**Context-sensitive prompts** suggest what could come next, depending on where the cursor is: the rest of a keyword, a variable name already used, or the parameters a function expects. They save typing and avoid spelling mistakes in names.
:::
:::col Finding errors early
**Dynamic syntax checks** examine the code while you type and mark a mistake, such as a missing bracket, at once, before you try to run. (A simple IDE may report a syntax error only when you run the program.)
:::
:::

:::cols
:::col Presenting code
**Prettyprint** displays the code in a clear layout: keywords and strings in different colours and automatic indentation, so the structure is easy to read. **Expand and collapse** hides a block of code, such as one function or loop, to leave only its first line, so you can see the overall structure of a long program or concentrate on one part.
:::
:::col Debugging
**Single stepping** runs the program one statement at a time. A **breakpoint** is a chosen line where the program pauses so you can look at it. A **report window** (watch window) shows the current values of variables and expressions as the program runs.
:::
:::

:::def Breakpoint
A line of the program, chosen by the programmer, at which the program pauses automatically so that its state can be examined.
:::

:::def Single stepping
Running a program one statement at a time, pausing after each, so that the programmer can see the effect of each statement.
:::

:::def Prettyprint
Displaying source code in a clear layout, using colours, fonts and indentation, so that its structure is easy to read.
:::

The debugging tools work together. Set a breakpoint just before the part you suspect, run until it pauses, then single step while watching the report window. The program below should print the mean of four marks, but it prints the wrong answer.

```python
marks = [14, 9, 17, 12]
total = 0
for i in range(1, len(marks)):
    total = total + marks[i]
average = total / len(marks)
print(average)
```

Output:

```output
9.5
```

The correct mean is \((14 + 9 + 17 + 12) \div 4 = 13.0\). Single stepping through the loop with a report window that watches `i` and `total` shows:

| After the loop body runs | `i` | `total` |
|---|---|---|
| first time | 1 | 9 |
| second time | 2 | 26 |
| third time | 3 | 38 |

The first value added is 9, which is `marks[1]`. The value 14, `marks[0]`, was never added, and `i` never takes the value 0. The fault is `range(1, len(marks))`: it should be `range(len(marks))`. With that change the loop adds all four marks, and the program prints:

```python
marks = [14, 9, 17, 12]
total = 0
for i in range(len(marks)):
    total = total + marks[i]
average = total / len(marks)
print(average)
```

Output:

```output
13.0
```

:::eg Describe three debugging features (exam style)
A student's program gives the wrong answer. Describe three features of an IDE that help the student to find the fault. [3 marks]

- Single stepping: the program runs one statement at a time, so the student can see which statement first gives a wrong result. [B1]
- Breakpoints: the student marks a line and the program pauses there, so the student can skip the code that already works and examine the program just before the suspected fault. [B1]
- Report (watch) window: shows the current value of variables and expressions, so the student can see when a value changes to something unexpected. [B1]

Each feature needs a **description of what it does**, not only its name. A name with no description scores nothing in a "describe" question.
:::

:::eg Spot the error: compiler and interpreter
Question: Describe **two** differences between a compiler and an interpreter. [4 marks]

A student wrote:

```text
01  A compiler runs the program line by line and stops when it finds an error.
02  An interpreter translates the whole program first and makes a file of
03  machine code.
04  A compiler is faster because the program has already been translated.
05  An interpreter is better for finding mistakes because it stops at the
06  first error and shows the line.
```

Lines 01 to 03 have swapped the two translators: it is the **interpreter** that works line by line and stops at an error, and the **compiler** that translates everything and produces machine code (object code) [B0] [B0]. Line 04 is correct: the compiled program runs faster because no translation happens at run time [B1]. Lines 05 and 06 are correct as a statement about interpreters: it stops at the first error and shows the line [B1]. The answer scores 2 out of 4.

The student knows the right facts but has attached them to the wrong translators in the opening sentences. A corrected opening would read: "A compiler translates the whole program into object code before it runs; an interpreter translates and runs one statement at a time." Always check that each fact is attached to the right translator.
:::

:::tip Learn the comparison as pairs
For every property, have the pair ready: whole program or one line; object code or none; runs fast or slow; source hidden or not; errors listed or first only; translator needed to run or not. Then any scenario question is a matter of picking the pairs the scenario needs.
:::

:::try Start easy, finish at exam standard
Q: State what the term "system software" means, and give one example.
A: Programs that manage and operate the computer and its hardware and provide a platform for other software, for example an operating system.
Q: Which operating system task is described: "keeps the memory used by one program separate from the memory used by another"?
A: Memory management.
Q: What is a device driver?
A: A small program that allows the operating system to communicate with a particular hardware device, translating general commands into the commands the device understands.
Q: Name the utility that: (a) makes a copy of files on another device; (b) shows which folders use the most space; (c) joins up the fragments of files on a magnetic disk.
A: (a) back-up software; (b) disk contents analysis; (c) defragmentation software.
Q: Why should a virus checker be updated regularly?
A: New malware is written all the time. The virus checker compares files with a database of known malware, so it can detect new malware only when the database has been updated.
Q: State one benefit of a program library to a developer.
A: The developer saves time because the routines are already written. (Also accepted: the routines are already tested, so there are fewer faults.)
Q: A program is stored as one .exe file containing machine code, and the user does not have the program's source code. Which kind of translator produced it?
A: A compiler.
Q: Why is an interpreter useful while a program is being written?
A: The program can be run straight away after each change, and the interpreter stops at the first error and shows where it is, so faults are found and fixed quickly.
Q: Name the IDE feature that: (a) pauses the program at a chosen line; (b) shows the values of variables while the program runs; (c) suggests the rest of a word as you type.
A: (a) a breakpoint; (b) the report window (watch window); (c) context-sensitive prompts.
Q: A file of 2 GB is compressed by a utility to 0.5 GB. By what factor is it smaller?
A: \(2 \div 0.5 = 4\), so the compressed file is four times smaller (it is one quarter of the size).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Explain why a general-purpose computer needs an operating system.
A: Any three of these points:

- It provides an interface (user interface) so that the user can run programs and manage files [B1]
- It controls the hardware and peripherals, so programs do not need their own code for each device [B1]
- It manages the memory and processor time, sharing them between the programs that are running [B1]

(Also accepted for any one of the three: it manages security, with user accounts and access rights, so that data and the system are protected.)

Q: [4 marks] ★ A school technician uses disk contents analysis software and back-up software on the school server. Describe the purpose of each.
A: Disk contents analysis:

- reports how the storage space is used, for example which folders or file types take the most space [B1]
- so that the technician can find files to delete or move, or plan to add storage [B1]

Back-up software:

- makes a copy of the files on another storage device or location [B1]
- so that the data can be restored if the original is lost, damaged or deleted [B1]

Q: [6 marks] ★★ (#cs.software) A game uses a DLL that holds sound routines. Three other programs on the same computer use the same DLL. (a) Explain two benefits to the developer of using a DLL. [4] (b) Explain one drawback of using a DLL. [2]
H: Each benefit needs a point and a reason that is about the developer or the programs.
H: For (b), think about what happens if the DLL file is not there.
A: (a) Any two of the following pairs:

- the developer does not need to write the sound code [B1] so development time is saved [B1]
- one copy of the DLL is shared by all four programs [B1] so less storage space is used (and each program file is smaller) [B1]

(A third accepted pair: the DLL can be replaced by a corrected version, and all four programs are fixed without being recompiled.)

(b) If the DLL is deleted, damaged or replaced by an incompatible version [B1], the programs that use it may fail to start or work incorrectly [B1].

Q: [6 marks] ★★ A tablet is running a video call, a note-taking program and a file download at the same time. Describe how the operating system (a) manages memory, [2] (b) manages processes, [2] (c) manages the hardware. [2]
H: Memory: where does each program live, and what must not happen between them?
H: Process: there is only one processor core to share.
A: (a) Memory:

- allocates a separate area of RAM to each program [B1]
- prevents one program from overwriting the memory of another (and frees the area when a program closes) [B1]

(b) Processes:

- switches the processor between the programs, giving each a short time slice [B1]
- fast enough that they all seem to run at once (multitasking), with the scheduler deciding which runs next [B1]

(c) Hardware:

- device drivers let the operating system control the camera, microphone, screen and wireless card [B1]
- it handles interrupts from the devices (for example when data arrives) and uses buffers to hold data in transit [B1]

Q: [4 marks] ★★ A company writes a phone app in Java. The source code is compiled to bytecode, which is run by a virtual machine on each customer's phone. Explain two advantages of this approach over compiling to the machine code of one type of phone.
A: Any two pairs:

- the same bytecode can be used for every type of phone [B1] because each phone has a virtual machine that understands bytecode, so the company does not need a separate compiled version for each processor [B1]
- the customers receive bytecode, not the source code [B1] so the company's code is protected from being copied [B1]

(A third accepted pair: the bytecode is already checked and partly translated, so it runs faster than if the phone interpreted the source code, and errors were found before release.)

Q: [6 marks] ★★ A student writes a program to find the position of the lowest temperature in a list.

```python
temps = [21, 18, 25, 19]
lowest = temps[0]
position = 0
for i in range(1, len(temps)):
    if temps[i] < lowest:
        lowest = temps[i]
    position = i
print(lowest, position)
```

The program prints `18 3`, but the lowest temperature, 18, is in position 1 (counting from 0). (a) State the values of `i`, `lowest` and `position` that a report window shows after the loop body has run for the third time. [2] (b) Describe how single stepping helps the student find the fault. [2] (c) Describe how a breakpoint could be used. [2]
H: Work out the loop by hand: `i` takes the values 1, 2 and 3.
A: (a) `i` is 3 [B1], `lowest` is 18 and `position` is 3 [B1]. (The value 3 for `position` is wrong: the fault is that `position = i` is not inside the IF, so it changes on every pass.)

(b) The program runs one statement at a time [B1], so the student sees that `position` changes on a pass where `lowest` does not change, which shows where the fault is [B1].

(c) The student sets a breakpoint on the line `position = i` (or at the start of the loop) [B1] and runs the program, which pauses there so the values in the report window can be examined without stepping through earlier code [B1].

Q: [8 marks] ★★★ A student in Dhaka writes one program in assembly language for a small controller and another in Python to analyse survey data. (a) State the type of translator used for each program. [2] (b) Explain why the assembly language translator is described as "one-to-one". [2] (c) Describe two differences in the way a compiler and an interpreter report errors in a program. [4]
H: For (c), recall when the errors are reported: after the whole program, or at the first one.
A: (a) The assembly program uses an assembler [B1]; the Python program uses an interpreter [B1]. (A compiler is accepted for Python only if the answer is consistent.)

(b) Each assembly language instruction is converted into exactly one machine code instruction [B1], so the translated program has the same number of instructions as the source [B1].

(c) Any two pairs:

- a compiler translates the whole program and then reports all the errors it found [B1], whereas an interpreter reports the first error it meets and stops there [B1]
- with a compiler, no object code is produced (and so the program cannot run) until all the syntax errors are corrected [B1], whereas an interpreter runs the statements before the error, so the statements before it have already been executed [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A hospital in Kampala keeps 400 GB of patient data. Each day 5% of the 400 GB (20 GB) of data changes, and the changed data on each day is different. **Plan A** is a full back-up every night. **Plan B** is a full back-up on Sunday night and an incremental back-up on each of the next six nights, Monday to Saturday. (a) Calculate the total amount of data copied in one week, Sunday night to Saturday night, under each plan. [2] (b) The data is lost on Friday morning. State which back-ups plan B needs to restore it. [2] (c) State one advantage of plan A over plan B. [1]
H: An incremental back-up copies only what changed since the previous back-up, which is 20 GB.
H: On Friday morning the latest back-up is Thursday night's.
A: (a) Plan A copies the whole 400 GB seven times: \(7 \times 400 = 2800\) GB [B1]. Plan B copies \(400 + 6 \times 20 = 520\) GB [B1].

(b) The Sunday night full back-up [B1] and every incremental back-up after it up to Thursday night, that is Monday, Tuesday, Wednesday and Thursday [B1].

(c) Restoring is simpler and quicker, because only the latest full back-up is needed (and a damaged earlier incremental back-up does not matter) [B1].

Q: [5 marks] ★★★ A company's accounts program uses a DLL, `rates.dll`, to calculate tax. Another program installed on the same computer replaces `rates.dll` with a newer version. The accounts program then gives wrong tax figures. (a) Explain why the accounts program is affected although it has not been changed. [2] (b) Describe two ways in which the developer could prevent this problem. [3]
H: Think about what dynamic linking means: when does the program connect to the routine?
H: One fix copies the code into the program; another keeps the DLL file out of reach.
A: (a) The accounts program is linked to the DLL when it runs, not when it is built [B1], so it uses whatever version of the file is on the computer, and the new version works differently from the one the program was written for [B1].

(b) Any two methods, one mark each:

- include the routines in the program itself (static linking) so that a changed DLL cannot affect it [B1]
- supply and install a private copy of the correct version of the DLL with the program, in its own folder [B1]

(A third accepted method: the program checks the version of the DLL when it starts and warns the user if it is not the right one.)

The third mark is for explaining how one of the methods removes the cause, which is that the program uses whichever file is on the computer when it runs [B1].
:::

:::quiz
? Which is the main reason a computer needs an operating system?
- To let the user write documents and browse the web.
+ To manage the hardware and share its resources between programs.
- To translate programs into machine code.
- To make the processor run faster.
> The operating system manages hardware, memory, processes, files and security, and provides the interface. Writing documents is done by application software, translation by translators, and the processor's speed is fixed by the hardware.
? A computer has several programs open. Which operating system task stops one program from overwriting the data of another?
- File management
+ Memory management
- Hardware management
- Process management
> Memory management gives each program its own area of RAM and protects it from the others. Process management decides which program gets the processor.
? Which statement about defragmentation is correct?
- It speeds up a solid state drive by moving data closer to the processor.
- It deletes files that are not needed.
+ It stores the parts of each file in neighbouring sectors, so a magnetic disk needs fewer head movements.
- It copies files to another device in case the disk fails.
> Defragmentation re-arranges the sectors of files on a magnetic disk. Copying files elsewhere is back-up, and a solid state drive has no head to move.
? Which is a benefit to a developer of using a DLL?
- The program runs much faster.
+ One copy of the routines can be shared by several programs and updated in one place.
- The program no longer needs an operating system.
- The program cannot be affected if the DLL file is deleted.
> Sharing and easy updating are the benefits. A DLL does not speed a program up, and a missing DLL is one of its drawbacks.
? What is the main job of a compiler?
- To run the program one line at a time.
- To find the errors in the program while the user types.
+ To translate the whole high-level program into object code that can be run later.
- To convert assembly language into machine code, instruction by instruction.
> A compiler translates the whole source program. Running one line at a time describes an interpreter; the one-to-one translation of assembly language is the job of an assembler.
? A company wants customers to be unable to read its source code and wants the program to run as fast as possible. Which translation should it supply?
- Source code, run by an interpreter on each customer's computer.
+ Compiled object code.
- Source code and a compiler.
- A prettyprinted copy of the source code.
> Object code is fast because no translation occurs at run time, and the customer does not receive the source code. An interpreter needs the source, and prettyprinting only changes how source code looks.
? Which IDE feature shows the current value of a variable while a program is running?
- Prettyprint
- A breakpoint
+ A report (watch) window
- Collapsing a code block
> The report window displays the values of variables and expressions. A breakpoint only pauses the program; prettyprint is about layout.
? Why does a program compiled to Java bytecode run on different types of device?
- The bytecode is machine code for every type of processor.
- The bytecode contains the source code, so each device can recompile it.
+ Each device has a virtual machine that runs the bytecode.
- Bytecode does not need to be translated or run by anything.
> Bytecode is an intermediate code, not machine code for a real processor. A virtual machine on each device interprets it.
:::

:::checklist What you can now do
- [ ] I can explain why a computer needs an operating system and say how it differs from application software.
- [ ] I can describe the five management tasks: memory, file, security, hardware and process management.
- [ ] I can say what a device driver is and what multitasking is.
- [ ] I can describe what each utility does and why it is needed: disk formatter, virus checker, defragmentation, disk contents analysis and repair, file compression and back-up.
- [ ] I can explain why defragmentation helps a magnetic disk and not a solid state drive.
- [ ] I can explain what a program library and a DLL are, and the benefits of each to a developer.
- [ ] I can explain why a program needs a translator, and what an assembler, a compiler and an interpreter do.
- [ ] I can state benefits and drawbacks of a compiler and an interpreter, and justify one for a scenario.
- [ ] I can describe partial compilation and interpretation, as in Java with bytecode and a virtual machine.
- [ ] I can describe IDE features for writing, error detection, presentation and debugging, and use single stepping, breakpoints and a report window to find a fault.
:::

:::recap
- An operating system manages hardware and resources and gives programs and users an interface. Its tasks are memory, process, file, security and hardware management.
- A device driver lets the operating system control one kind of device; multitasking shares the processor between processes in short time slices.
- Utility software does housekeeping: a formatter prepares a disk, a virus checker scans for malware (and needs updating), defragmentation joins file fragments on a magnetic disk (not an SSD), analysis and repair report and fix disk problems, compression saves space, back-up makes a separate copy.
- A library is pre-written, tested routines. A DLL is loaded at run time and shared by programs: smaller programs, one copy, easy updating, but a missing or wrong-version DLL breaks the programs that use it.
- Processors run only machine code, so source code needs a translator. An assembler is one-to-one. A compiler translates the whole program into object code (fast to run, source hidden, errors listed, recompile after every change). An interpreter translates and runs line by line (easy to test, stops at the first error, slower, needs the interpreter, source supplied).
- Java is compiled to bytecode and the bytecode is run by a virtual machine on each device.
- An IDE gives context-sensitive prompts, dynamic syntax checks, prettyprint, collapsible code blocks, single stepping, breakpoints and a report window.
:::

:::links
- practise: [Operating systems: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/5-system-software-/operating-systems/exam-questions/) · Save My Exams · 9618-style questions on the operating system and utilities [paid]
- practise: [Language translators: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/5-system-software-/language-translators/exam-questions/) · Save My Exams · compiler, interpreter and IDE questions [paid]
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · step through the marks program line by line and watch the variables change, as in a report window
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists on compilers, interpreters and operating systems
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations of system software and translators (written for UK boards)

Links checked 13 November 2026.
:::

Next: [Security, privacy and data integrity](#cs.security)
