@chapter cs.os
@title Operating systems: processes, scheduling and memory
@level a2
@paper CAIE 9618 Paper 3
@time 5–7 hours
@summary How an operating system keeps the processor and memory busy: how it hides the hardware, how a process moves between the running, ready and blocked states, how first come first served, shortest job first, shortest remaining time and round robin choose the next process (with Gantt charts and average waiting times), how the kernel handles interrupts, and how paging, segmentation and virtual memory work, including page replacement and disk thrashing.

:::why
A computer has one processor core, a limited amount of memory and a handful of devices, yet it appears to run a browser, a music player and a download at once. The operating system makes that possible by deciding, many times a second, which process gets the processor and which pages stay in memory. Paper 3 asks you to draw state diagrams, build Gantt charts and calculate average waiting times, and to explain virtual memory and thrashing, so this chapter works through each of those with full examples.
:::

**Before you start**, you should know the tasks of an operating system from [System software: operating systems and translators](#cs.software) and how interrupts work from [Processor fundamentals and the fetch-execute cycle](#cs.processor).

:::try Warm-up
Q: What does "multitasking" mean? (from [System software: operating systems and translators](#cs.software))
A: The operating system shares the processor between several processes by giving each a short time slice in turn, so that they appear to run at the same time.
Q: When does the processor check whether an interrupt is waiting? (from [Processor fundamentals and the fetch-execute cycle](#cs.processor))
A: At the end of each fetch-execute cycle, after the current instruction has been executed.
Q: Which small program lets the operating system control a particular device such as a printer? (from [System software: operating systems and translators](#cs.software))
A: A device driver.
:::

## Maximising the use of resources

A computer's **resources** are the things programs need in order to run: processor time, main memory, storage and input/output devices. The operating system's first job at this level is to keep these resources busy and to share them fairly, because an idle resource is wasted money.

The processor is the best example. It works in nanoseconds, but a disk takes milliseconds to deliver data, which is millions of times longer. If a program asks for a file and the processor simply waits, the fastest part of the computer sits idle.

:::eg Why the processor must not wait
A program computes for 2 ms, then waits 8 ms for the disk, and repeats this cycle. How busy is the processor if this is the only program? How busy is it if the operating system keeps up to five such programs in memory and runs another whenever one is waiting? Assume the waits of the programs do not clash with each other. [3 marks]

One program uses the processor for 2 ms in every 10 ms, which is \(2 \div 10 = 20\%\). [B1]

Each extra program uses the gaps. With \(n\) programs the processor is busy for \(n \times 20\%\) of the time, up to a limit of 100%: two programs give 40%, three give 60% and four give 80%. [B1]

With five programs the processor is busy for \(5 \times 2 = 10\) ms in every 10 ms, so it is never idle: 100%. [B1]

This is an idealised calculation: real programs do not fit together so neatly, and switching between programs costs a little time. But it shows the principle that **while one process waits for input or output, the operating system gives the processor to another**.
:::

The operating system maximises the use of resources in these ways:

- **Processor.** It keeps several processes in memory, runs one at a time, and switches to another when the running one has to wait (multi-tasking), so the processor is not left idle.
- **Memory.** It loads only the parts of programs that are needed, shares memory between processes, and uses secondary storage as an extension of main memory (virtual memory, later in this chapter).
- **Input/output devices.** It uses buffers and queues, so that a slow printer does not hold up the program that sent the job, and one device is shared fairly between users.

### How the user interface hides the hardware

A user does not need to know how many sectors a file uses or which wires carry a keypress. The operating system presents a **user interface** and hides the hardware's complexity behind layers.

:::def User interface
The part of the operating system (or of a program) that lets a person communicate with the computer. A graphical user interface (GUI) uses windows, icons, menus and a pointer. A command-line interface (CLI) uses typed commands.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 262" role="img" aria-label="Layers between a user and the hardware, from top to bottom: the user; application software; the user interface (graphical or command line); the operating system, with its kernel and system calls; device drivers; the hardware, which is the processor, memory and devices."><rect class="fm s-acc sw2" x="20" y="8" width="290" height="28" rx="4"/><text class="tl tc" x="165" y="27">The user</text><rect class="fm s-acc sw2" x="20" y="48" width="290" height="28" rx="4"/><text class="tl tc" x="165" y="67">Application software</text><rect class="fm s-acc sw2" x="20" y="88" width="290" height="28" rx="4"/><text class="tl tc" x="165" y="107">User interface (GUI or command line)</text><rect class="fm s-acc sw2" x="20" y="128" width="290" height="28" rx="4"/><text class="tl tc" x="165" y="147">Operating system: kernel and system calls</text><rect class="fm s-acc sw2" x="20" y="168" width="290" height="28" rx="4"/><text class="tl tc" x="165" y="187">Device drivers</text><rect class="fm s-acc sw2" x="20" y="208" width="290" height="28" rx="4"/><text class="tl tc" x="165" y="227">Hardware: processor, memory, devices</text><polyline class="ln" fill="none" points="165,36 165,48" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="165,76 165,88" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="165,116 165,128" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="165,156 165,168" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="165,196 165,208" marker-end="url(#ah)"/></svg><figcaption>The user never deals with the hardware directly. Each layer hides the details of the layer below it.</figcaption></figure>
:::

Each layer talks only to the layer next to it. When you click Save in a word processor, the application asks the operating system to save a file (a **system call**). The operating system finds free space, works out which sectors to use, and passes simple commands to the **device driver** for the disk. The driver turns them into the exact signals that one particular disk understands. You see none of this.

:::key How the interface hides complexity
- The user works with files, windows and menus, not sectors, memory addresses or signals.
- Programs ask the operating system for a service through **system calls**, instead of controlling hardware themselves.
- **Device drivers** hide the differences between devices: the same application can print on any printer that has a driver.
- The operating system manages memory and the processor, so each program behaves as though it had the machine to itself.
:::

## Processes

:::def Process
A program that is being executed. It consists of the program's instructions, its data and the values in the registers (including the program counter) that show how far it has got. One program may be run as several processes at once.
:::

A program is a file of instructions stored on disk. A process is that program **running**. If two people open the same word processor, there is one program and two processes. The operating system must remember, for each process, what it was doing: the contents of the registers, where it had reached in memory and what it is waiting for. This information is saved in a block of data (often called a **process control block**) whenever the process is stopped.

:::def Multi-tasking
Running several processes at the same time, as far as the user can see, by letting the processor run each process for a short time (a time slice) and then switching to another, so that all of them make progress.
:::

A single processor core executes one instruction at a time, so only one process can be running at any instant. Multi-tasking creates the illusion of many by switching very fast, typically many times per second.

### The three process states

At any moment, a process is in one of three states.

:::def Running
The state of a process that is currently being executed by the processor. In a computer with one processor core, only one process is running at a time.
:::

:::def Ready
The state of a process that is able to run, with everything it needs except the processor, and is waiting in a queue for its turn.
:::

:::def Blocked
The state of a process that cannot continue until some event happens, such as the completion of an input or output operation, so it cannot use the processor even if it is offered one.
:::

Many books also show a **New** state (a process being created) and a **Terminated** state (a process that has finished). The figure shows all five.

:::html
<figure class="fig"><svg viewBox="0 0 660 270" role="img" aria-label="Process state diagram. Five boxes: New, Ready, Running, Blocked and Terminated. New goes to Ready when the process is admitted. Ready goes to Running when the scheduler dispatches it. Running goes back to Ready when its time slice ends. Running goes to Blocked when it waits for input, output or an event. Blocked goes to Ready when that input, output or event completes. Running goes to Terminated when the process finishes. There is no arrow from Blocked to Running."><rect class="fm s-acc sw2" x="10" y="50" width="80" height="40" rx="6"/><text class="tl tc tb" x="50" y="75">New</text><rect class="fm s-acc sw2" x="170" y="50" width="90" height="40" rx="6"/><text class="tl tc tb" x="215" y="75">Ready</text><rect class="fm s-acc sw2" x="380" y="50" width="100" height="40" rx="6"/><text class="tl tc tb" x="430" y="75">Running</text><rect class="fm s-acc sw2" x="240" y="200" width="100" height="40" rx="6"/><text class="tl tc tb" x="290" y="225">Blocked</text><rect class="fm s-acc sw2" x="530" y="200" width="100" height="40" rx="6"/><text class="tl tc tb" x="580" y="225">Terminated</text><polyline class="ln" fill="none" points="90,70 168,70" marker-end="url(#ah)"/><text class="tl tc" x="129" y="62">admitted</text><polyline class="ln" fill="none" points="260,60 378,60" marker-end="url(#ah)"/><text class="tl tc" x="319" y="46">dispatched</text><polyline class="ln" fill="none" points="378,80 262,80" marker-end="url(#ah)"/><text class="tl tc" x="319" y="102">time slice ends</text><polyline class="ln" fill="none" points="440,90 440,220 342,220" marker-end="url(#ah)"/><text class="tl" x="448" y="150">waits for I/O</text><text class="tl" x="448" y="171">or an event</text><polyline class="ln" fill="none" points="240,220 215,220 215,92" marker-end="url(#ah)"/><text class="tl te" x="207" y="150">I/O or event</text><text class="tl te" x="207" y="171">completes</text><polyline class="ln" fill="none" points="480,70 580,70 580,198" marker-end="url(#ah)"/><text class="tl" x="588" y="140">finishes</text></svg><figcaption>The life of a process. Only three of the states (Running, Ready, Blocked) are examined in detail; a Blocked process can only move to Ready, never straight to Running.</figcaption></figure>
:::

| From | To | Event that causes it |
|---|---|---|
| New | Ready | the process is created and admitted to the queue |
| Ready | Running | the scheduler picks it and gives it the processor (it is "dispatched") |
| Running | Ready | its time slice ends (a timer interrupt), or it is pre-empted |
| Running | Blocked | it asks for input or output, or waits for another event |
| Blocked | Ready | the input or output finishes, or the event happens (an interrupt) |
| Running | Terminated | it finishes |

:::warn Blocked goes to ready, never straight to running
When the disk finishes, the waiting process does not get the processor at once. The operating system moves it to the ready queue, and it runs when the scheduler chooses it. There is no arrow from Blocked to Running, and no arrow from Ready to Blocked (a process must be running to ask for input or output).
:::

:::eg Process states (exam style)
A process in a computer is running. It asks for a record from a disk. State the state changes of the process, in order, until it is running again, giving the cause of each. [4 marks]

- The process moves from running to blocked, because it must wait for the disk. [B1]
- The processor is given to another ready process, so it is not idle. [B1]
- When the disk has found the record it sends an interrupt, and the process moves from blocked to ready. [B1]
- The scheduler later chooses it and it moves from ready to running. [B1]
:::

## Scheduling

When several processes are ready, the operating system has to choose one. That choice is **scheduling**.

:::def Scheduling
The method by which the operating system decides which process in the ready queue is given the processor next, and for how long.
:::

A good scheduler tries to keep the processor busy, give every process a fair share, keep the average waiting time short and make interactive programs respond quickly. These goals pull against each other, so there are several algorithms.

Operating systems have more than one scheduler. A **high-level (long-term) scheduler** decides which programs are loaded from disk into memory as processes. The **low-level (short-term) scheduler**, which this section is about, decides which of the ready processes in memory gets the processor next. It runs very often, so it must be fast. It is part of the kernel, described later.

:::def Pre-emptive and non-pre-emptive
In a **pre-emptive** scheduling algorithm the operating system can take the processor away from the running process before it has finished (for example when its time slice ends or a shorter process arrives). In a **non-pre-emptive** algorithm a process keeps the processor until it finishes or blocks.
:::

### Measuring a schedule

To compare algorithms you need some measurements. All times are in the same unit, for example milliseconds.

:::def Burst time
The amount of processor time a process needs to finish.
:::

:::def Turnaround time and waiting time
The **turnaround time** of a process is the time from its arrival until it finishes: completion time − arrival time. Its **waiting time** is the time it spends in the ready queue: turnaround time − burst time.
:::

A **Gantt chart** is a bar that shows which process has the processor at each moment, with the times along it. Throughout this chapter the same four processes are used, each with an arrival time and a burst time. For these examples only the processor is modelled (no process waits for input or output).

| Process | Arrival time | Burst time |
|---|---|---|
| A | 0 | 5 |
| B | 1 | 3 |
| C | 2 | 8 |
| D | 3 | 2 |

:::key Rules used for ties
- If two processes could be chosen equally, choose the one that arrived first; if they arrived together, choose by name.
- A new process pre-empts the running one (shortest remaining time) only if it needs strictly less time than the running one has left.
- In round robin, a process that arrives while another is running, or at the moment a time slice ends, joins the queue **before** the process whose slice has just ended.

Exam questions state any rule they need, so read the question for it. These are the rules this chapter and its widget use.
:::

### First come first served (FCFS)

:::def First come first served (FCFS)
A non-pre-emptive scheduling algorithm that runs processes in the order in which they arrive in the ready queue. Each process keeps the processor until it finishes.
:::

It is the queue at a shop. A has the processor from 0 to 5. B (arrived at 1), C (arrived at 2) and D (arrived at 3) have been waiting. B runs from 5 to 8, C from 8 to 16 and D from 16 to 18.

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---|---|---|---|---|---|
| A | 0 | 5 | 5 | 5 | 0 |
| B | 1 | 3 | 8 | 7 | 4 |
| C | 2 | 8 | 16 | 14 | 6 |
| D | 3 | 2 | 18 | 15 | 13 |

The average waiting time is \((0 + 4 + 6 + 13) \div 4 = 23 \div 4 = 5.75\), and the average turnaround time is \((5 + 7 + 14 + 15) \div 4 = 41 \div 4 = 10.25\).

FCFS is simple to write and perfectly fair in order of arrival, and no process is ever starved. Its weakness is the **convoy effect**: D needs only 2 units but waits 13, because the long process C is ahead of it.

### Shortest job first (SJF)

:::def Shortest job first (SJF)
A non-pre-emptive scheduling algorithm that, whenever the processor becomes free, chooses the ready process with the shortest burst time. Once started, a process runs until it finishes.
:::

At time 0 only A has arrived, so A runs from 0 to 5, even though B arrives at 1 and is shorter (SJF never interrupts). At time 5 the ready processes are B (3), C (8) and D (2). The shortest is D, so D runs from 5 to 7. Then B (3) runs from 7 to 10, and C from 10 to 18.

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---|---|---|---|---|---|
| A | 0 | 5 | 5 | 5 | 0 |
| B | 1 | 3 | 10 | 9 | 6 |
| C | 2 | 8 | 18 | 16 | 8 |
| D | 3 | 2 | 7 | 4 | 2 |

The average waiting time is \((0 + 6 + 8 + 2) \div 4 = 16 \div 4 = 4\), better than FCFS. Short processes no longer wait behind long ones. (When all the processes are ready at the same moment, SJF gives the lowest possible average waiting time of any order.) Its drawbacks are that the operating system must **know or estimate each process's burst time** in advance (which is difficult), and a long process can be **starved**: if short processes keep arriving, C may never reach the front.

:::def Starvation
A situation in which a process is ready to run but is never chosen because the scheduling algorithm keeps preferring other processes.
:::

### Shortest remaining time (SRT)

:::def Shortest remaining time (SRT)
A pre-emptive version of shortest job first. Whenever a process arrives or finishes, the process with the least processor time still to do is chosen, and a running process is pre-empted if a new process needs less time than the running process has left.
:::

Follow the chart one decision at a time.

- Time 0: only A is here (5 left). A runs.
- Time 1: B arrives needing 3. A has 4 left. \(3 < 4\), so B pre-empts A.
- Time 2: C arrives needing 8. B has 2 left, so B keeps going. Time 3: D arrives needing 2. B has 1 left, so B keeps going.
- Time 4: B finishes. The ready processes are A (4 left), C (8) and D (2). D runs until time 6.
- Time 6: A (4 left) and C (8): A runs until 10. Then C runs until 18.

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---|---|---|---|---|---|
| A | 0 | 5 | 10 | 10 | 5 |
| B | 1 | 3 | 4 | 3 | 0 |
| C | 2 | 8 | 18 | 16 | 8 |
| D | 3 | 2 | 6 | 3 | 1 |

The average waiting time is \((5 + 0 + 8 + 1) \div 4 = 14 \div 4 = 3.5\), the best of the four. SRT gives short processes a very quick service, but it needs burst-time estimates, it carries the cost of extra switches, and a long process such as C can be starved by a stream of short ones.

### Round robin (RR)

:::def Round robin (RR)
A pre-emptive scheduling algorithm in which each process in the ready queue is given the processor for at most a fixed time slice (the quantum), in turn. A process that has not finished when its quantum ends goes to the back of the queue.
:::

Round robin is built for time-sharing systems, where many users need quick responses. Every ready process gets a turn within a short time, so no process is starved. Here is the schedule for the four processes with a quantum of 2. The queue column shows the ready queue after the slice, with the arrivals added first, as the rules say.

| Slice | Process | Times | Left after | Ready queue after the slice |
|---|---|---|---|---|
| 1 | A | 0 to 2 | 3 | B, C, A |
| 2 | B | 2 to 4 | 1 | C, A, D, B |
| 3 | C | 4 to 6 | 6 | A, D, B, C |
| 4 | A | 6 to 8 | 1 | D, B, C, A |
| 5 | D | 8 to 10 | 0 | B, C, A |
| 6 | B | 10 to 11 | 0 | C, A |
| 7 | C | 11 to 13 | 4 | A, C |
| 8 | A | 13 to 14 | 0 | C |
| 9 | C | 14 to 16 | 2 | C |
| 10 | C | 16 to 18 | 0 | (empty) |

On the chart, slices 9 and 10 are drawn as one bar for C from 14 to 18, because no other process is waiting and C simply carries on.

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---|---|---|---|---|---|
| A | 0 | 5 | 14 | 14 | 9 |
| B | 1 | 3 | 11 | 10 | 7 |
| C | 2 | 8 | 18 | 16 | 8 |
| D | 3 | 2 | 10 | 7 | 5 |

The average waiting time is \((9 + 7 + 8 + 5) \div 4 = 29 \div 4 = 7.25\). That is longer than the other three here, but notice that every process starts within a few time units, which matters when people are waiting at a keyboard.

The size of the quantum is a trade-off. Each switch between processes costs time, so a **very small quantum** wastes time on switching. A **very large quantum** makes every process run to the end of its burst, so round robin turns into first come first served and short jobs wait behind long ones. The table shows the effect on these four processes (switches are changes from one process to another).

| Quantum | Average waiting time | Switches between processes |
|---|---|---|
| 1 | 6.5 | 13 |
| 2 | 7.25 | 8 |
| 3 | 6 | 5 |
| 4 | 7 | 5 |
| 5 | 5.5 | 4 |

There is no simple rule: the best quantum depends on the burst times. Real systems choose a quantum long enough that most interactive requests finish within one slice, but short enough to respond quickly.

### Comparing the four algorithms

:::html
<figure class="fig"><svg viewBox="0 0 624 262" role="img" aria-label="Four Gantt charts for the same four processes (A arrives at 0 and needs 5 units, B arrives at 1 and needs 3, C arrives at 2 and needs 8, D arrives at 3 and needs 2). First come first served: A 0 to 5, B 5 to 8, C 8 to 16, D 16 to 18. Shortest job first: A 0 to 5, D 5 to 7, B 7 to 10, C 10 to 18. Shortest remaining time: A 0 to 1, B 1 to 4, D 4 to 6, A 6 to 10, C 10 to 18. Round robin with quantum 2: A 0 to 2, B 2 to 4, C 4 to 6, A 6 to 8, D 8 to 10, B 10 to 11, C 11 to 13, A 13 to 14, C 14 to 18."><text class="tl" x="8" y="29">FCFS</text><rect class="fm s-acc sw2" x="62" y="10" width="150" height="26"/><text class="tl tc tb" x="137" y="28">A</text><rect class="fm s-acc sw2" x="212" y="10" width="90" height="26"/><text class="tl tc tb" x="257" y="28">B</text><rect class="fm s-acc sw2" x="302" y="10" width="240" height="26"/><text class="tl tc tb" x="422" y="28">C</text><rect class="fm s-acc sw2" x="542" y="10" width="60" height="26"/><text class="tl tc tb" x="572" y="28">D</text><text class="tl tc" x="62" y="52">0</text><text class="tl tc" x="212" y="52">5</text><text class="tl tc" x="302" y="52">8</text><text class="tl tc" x="542" y="52">16</text><text class="tl tc" x="602" y="52">18</text><text class="tl" x="8" y="91">SJF</text><rect class="fm s-acc sw2" x="62" y="72" width="150" height="26"/><text class="tl tc tb" x="137" y="90">A</text><rect class="fm s-acc sw2" x="212" y="72" width="60" height="26"/><text class="tl tc tb" x="242" y="90">D</text><rect class="fm s-acc sw2" x="272" y="72" width="90" height="26"/><text class="tl tc tb" x="317" y="90">B</text><rect class="fm s-acc sw2" x="362" y="72" width="240" height="26"/><text class="tl tc tb" x="482" y="90">C</text><text class="tl tc" x="62" y="114">0</text><text class="tl tc" x="212" y="114">5</text><text class="tl tc" x="272" y="114">7</text><text class="tl tc" x="362" y="114">10</text><text class="tl tc" x="602" y="114">18</text><text class="tl" x="8" y="153">SRT</text><rect class="fm s-acc sw2" x="62" y="134" width="30" height="26"/><text class="tl tc tb" x="77" y="152">A</text><rect class="fm s-acc sw2" x="92" y="134" width="90" height="26"/><text class="tl tc tb" x="137" y="152">B</text><rect class="fm s-acc sw2" x="182" y="134" width="60" height="26"/><text class="tl tc tb" x="212" y="152">D</text><rect class="fm s-acc sw2" x="242" y="134" width="120" height="26"/><text class="tl tc tb" x="302" y="152">A</text><rect class="fm s-acc sw2" x="362" y="134" width="240" height="26"/><text class="tl tc tb" x="482" y="152">C</text><text class="tl tc" x="62" y="176">0</text><text class="tl tc" x="92" y="176">1</text><text class="tl tc" x="182" y="176">4</text><text class="tl tc" x="242" y="176">6</text><text class="tl tc" x="362" y="176">10</text><text class="tl tc" x="602" y="176">18</text><text class="tl" x="8" y="215">RR (2)</text><rect class="fm s-acc sw2" x="62" y="196" width="60" height="26"/><text class="tl tc tb" x="92" y="214">A</text><rect class="fm s-acc sw2" x="122" y="196" width="60" height="26"/><text class="tl tc tb" x="152" y="214">B</text><rect class="fm s-acc sw2" x="182" y="196" width="60" height="26"/><text class="tl tc tb" x="212" y="214">C</text><rect class="fm s-acc sw2" x="242" y="196" width="60" height="26"/><text class="tl tc tb" x="272" y="214">A</text><rect class="fm s-acc sw2" x="302" y="196" width="60" height="26"/><text class="tl tc tb" x="332" y="214">D</text><rect class="fm s-acc sw2" x="362" y="196" width="30" height="26"/><text class="tl tc tb" x="377" y="214">B</text><rect class="fm s-acc sw2" x="392" y="196" width="60" height="26"/><text class="tl tc tb" x="422" y="214">C</text><rect class="fm s-acc sw2" x="452" y="196" width="30" height="26"/><text class="tl tc tb" x="467" y="214">A</text><rect class="fm s-acc sw2" x="482" y="196" width="120" height="26"/><text class="tl tc tb" x="542" y="214">C</text><text class="tl tc" x="62" y="238">0</text><text class="tl tc" x="122" y="238">2</text><text class="tl tc" x="182" y="238">4</text><text class="tl tc" x="242" y="238">6</text><text class="tl tc" x="302" y="238">8</text><text class="tl tc" x="362" y="238">10</text><text class="tl tc" x="392" y="238">11</text><text class="tl tc" x="452" y="238">13</text><text class="tl tc" x="482" y="238">14</text><text class="tl tc" x="602" y="238">18</text></svg><figcaption>The same four processes under four algorithms. Each bar shows which process has the processor, and the numbers under it are times.</figcaption></figure>
:::

| Algorithm | Pre-emptive? | Average waiting time (these processes) | Benefits | Drawbacks |
|---|---|---|---|---|
| FCFS | No | 5.75 | simple; fair by arrival; no starvation | convoy effect: short processes wait behind long ones |
| SJF | No | 4 | low average waiting time; good for short jobs | needs burst-time estimates; long processes can starve |
| SRT | Yes | 3.5 | very fast for short processes; lowest average waiting time here | needs estimates; long processes can starve; more switching |
| RR | Yes | 7.25 | fair; no starvation; good response time for interactive users | higher average waiting time; the quantum must be chosen well; switching cost |

Use the tool below to change the processes. Switch between the algorithms and watch the Gantt chart and the waiting times change. Then try these: give process A a burst of 12 and see what SJF and SRT do to it; set the quantum to 1 and to 5; make every process arrive at 0 and compare FCFS with SJF.

:::html
<div class="widget" data-w="cs-sched" data-algo="rr" data-q="2" data-procs="A:0:5,B:1:3,C:2:8,D:3:2"></div>
:::

:::eg Draw a Gantt chart and calculate the average waiting time (exam style)
Four processes arrive at a computer.

| Process | Arrival time | Burst time |
|---|---|---|
| P | 0 | 4 |
| Q | 1 | 5 |
| R | 2 | 2 |
| S | 4 | 3 |

The computer uses round robin with a time quantum of 2. If a process arrives at the same moment as another process's time slice ends, the new process joins the queue first. Draw the Gantt chart as a list of time slices and calculate the average waiting time. [5 marks]

Build the queue slice by slice. At time 0 the queue is P.

- P runs from 0 to 2 (2 left). Q has arrived at 1, R at 2, so the queue is Q, R, P.
- Q runs from 2 to 4 (3 left). S arrives at 4, and joins before Q. The queue is R, P, S, Q.
- R runs from 4 to 6 and finishes. Queue: P, S, Q.
- P runs from 6 to 8 and finishes. Queue: S, Q.
- S runs from 8 to 10 (1 left). Queue: Q, S.
- Q runs from 10 to 12 (1 left). Queue: S, Q.
- S runs from 12 to 13 and finishes. Q runs from 13 to 14 and finishes.

Gantt chart: P (0–2), Q (2–4), R (4–6), P (6–8), S (8–10), Q (10–12), S (12–13), Q (13–14).

Completion times: P 8, Q 14, R 6, S 13. Waiting time = completion − arrival − burst:

| Process | Completion | Waiting time |
|---|---|---|
| P | 8 | \(8 - 0 - 4 = 4\) |
| Q | 14 | \(14 - 1 - 5 = 8\) |
| R | 6 | \(6 - 2 - 2 = 2\) |
| S | 13 | \(13 - 4 - 3 = 6\) |

Average waiting time: \((4 + 8 + 2 + 6) \div 4 = 20 \div 4 = 5\).

- first three slices P, Q, R drawn correctly with times [B1]
- P (6–8) and S (8–10), with S before Q because S joined the queue first [B1]
- the final slices Q (10–12), S (12–13), Q (13–14) [B1]
- waiting time of each process (4, 8, 2 and 6) [B1]
- average waiting time 5 [B1]
:::

## The kernel and interrupts

:::def Kernel
The core part of the operating system. It is loaded first, stays in main memory and has full control of the hardware. It handles interrupts, carries out the low-level scheduling of processes, manages memory and controls devices through drivers.
:::

The kernel is the part of the operating system that is always running in the background. Programs and utilities that you use are built on top of it, and they reach the hardware only by asking the kernel through system calls.

Two of its roles are examined: handling interrupts and low-level scheduling. They work together.

:::def Interrupt handler
The routine in the kernel (the interrupt service routine) that is run when an interrupt signal arrives. It deals with the cause of the interrupt, for example a finished disk transfer, and then returns control so that processing can continue.
:::

An interrupt is a signal that tells the processor an event needs attention (as in [Processor fundamentals and the fetch-execute cycle](#cs.processor)). Three kinds matter here:

- **Timer interrupt.** A hardware timer sends an interrupt at fixed intervals. It marks the end of the running process's time slice.
- **Input/output interrupt.** A device (a disk, a keyboard, a network card) sends one when it has finished or needs service.
- **Error and software interrupts.** A program tries to do something illegal, or asks for a system service.

:::steps
1. A timer interrupt arrives while process A is running. The processor finishes the current instruction and then checks for interrupts.
2. The kernel's interrupt handler runs. It saves the state of process A (the program counter and the other registers) and marks A as ready.
3. The low-level scheduler chooses the next process, say B, from the ready queue.
4. The kernel loads B's saved registers, including its program counter, into the processor.
5. B runs. Later, the same steps give A another turn, and A continues exactly where it stopped, because its state was saved.
:::

Swapping one process for another in this way is called a **context switch**. It is pure overhead, because no useful work is done while it happens, and that is why a very small quantum is wasteful.

An I/O interrupt works in the same way. When a disk has finished reading, its interrupt makes the kernel run its handler, which moves the process that was waiting from blocked to ready. The process is not started: the scheduler decides later when it runs.

:::eg Describe the use of a timer interrupt (exam style)
Describe how the kernel uses a timer interrupt to share the processor between processes. [3 marks]

- A timer sends an interrupt at regular intervals, when the running process's time slice has ended. [B1]
- The interrupt handler saves the state (such as the registers and the program counter) of the running process and puts it in the ready queue. [B1]
- The low-level scheduler chooses the next ready process, and its saved state is loaded into the processor so that it runs. [B1]
:::

## Memory management: paging and segmentation

Every process needs main memory, and there is not enough for every process to have all of what it wants. The operating system divides memory into pieces and decides where each piece goes. There are two ways to divide it.

### Paging

:::def Paging
A memory management method in which a process's memory is divided into fixed-size blocks called pages, and main memory is divided into blocks of the same size called frames. Any page can be placed in any free frame, so the pages of one process need not be next to each other.
:::

:::def Page and frame
A **page** is a fixed-size block of a process's logical memory. A **frame** is a fixed-size block of physical main memory that holds one page. Pages and frames are the same size.
:::

:::def Page table
A table kept by the operating system for each process that records, for every page, the frame of main memory in which it is stored (or that it is not in main memory).
:::

A program uses **logical addresses**, which run from 0 up to the size of the program, as though it had a block of memory to itself. The hardware turns each logical address into a **physical address** in RAM using the page table.

:::html
<figure class="fig"><svg viewBox="0 0 640 300" role="img" aria-label="Paging. A process has four pages numbered 0 to 3. The page table says page 0 is in frame 1, page 1 is in frame 2, page 2 is not in RAM and is on disk, and page 3 is in frame 4. RAM has five frames, numbered 0 to 4: frame 0 holds a page of another process, frame 1 holds page 0, frame 2 holds page 1, frame 3 is free, and frame 4 holds page 3. Arrows run from the page table entries to the frames."><text class="tl" x="10" y="20">Pages of the process</text><text class="tl" x="210" y="20">Page table</text><text class="tl" x="440" y="20">RAM (frames)</text><rect class="fm s-acc sw2" x="10" y="40" width="100" height="36"/><text class="tl tc" x="60" y="63">Page 0</text><polyline class="ln" fill="none" points="110,58 210,58" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="210" y="40" width="130" height="36"/><text class="tl" x="220" y="63">0: frame 1</text><rect class="fm s-acc sw2" x="10" y="76" width="100" height="36"/><text class="tl tc" x="60" y="99">Page 1</text><polyline class="ln" fill="none" points="110,94 210,94" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="210" y="76" width="130" height="36"/><text class="tl" x="220" y="99">1: frame 2</text><rect class="fm s-acc sw2" x="10" y="112" width="100" height="36"/><text class="tl tc" x="60" y="135">Page 2</text><polyline class="ln" fill="none" points="110,130 210,130" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="210" y="112" width="130" height="36"/><text class="tl" x="220" y="135">2: on disk</text><rect class="fm s-acc sw2" x="10" y="148" width="100" height="36"/><text class="tl tc" x="60" y="171">Page 3</text><polyline class="ln" fill="none" points="110,166 210,166" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="210" y="148" width="130" height="36"/><text class="tl" x="220" y="171">3: frame 4</text><rect class="fm s-acc sw2" x="440" y="40" width="130" height="36"/><text class="tl" x="450" y="63">0: other process</text><rect class="fm s-acc sw2" x="440" y="76" width="130" height="36"/><text class="tl" x="450" y="99">1: page 0</text><rect class="fm s-acc sw2" x="440" y="112" width="130" height="36"/><text class="tl" x="450" y="135">2: page 1</text><rect class="fm s-acc sw2" x="440" y="148" width="130" height="36"/><text class="tl" x="450" y="171">3: free</text><rect class="fm s-acc sw2" x="440" y="184" width="130" height="36"/><text class="tl" x="450" y="207">4: page 3</text><polyline class="ln" fill="none" points="340,58 370,58 370,94 438,94" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="340,94 355,94 355,130 438,130" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="340,166 385,166 385,202 438,202" marker-end="url(#ah)"/><rect class="fm s-acc sw2 dash" x="210" y="232" width="130" height="36"/><text class="tl tc" x="275" y="255">Disk: page 2</text></svg><figcaption>Pages of one process (left) are placed in any free frames of RAM (right). The page table records where each page is, or that it is on disk.</figcaption></figure>
:::

To translate a logical address, split it into a page number and an offset within the page:

- page number = logical address DIV page size
- offset = logical address MOD page size
- physical address = (frame number × page size) + offset

:::eg Translating logical addresses
A process uses pages of 256 bytes. Its page table is: page 0 is in frame 1, page 1 in frame 2, page 2 is not in main memory, page 3 is in frame 4. Find the physical address for the logical addresses 300 and 800, and say what happens for 600. [4 marks]

Address 300: \(300 \text{ DIV } 256 = 1\), \(300 \text{ MOD } 256 = 44\). Page 1 is in frame 2, so the physical address is \(2 \times 256 + 44 = 556\). [B1]

Address 800: \(800 \text{ DIV } 256 = 3\), \(800 \text{ MOD } 256 = 32\). Page 3 is in frame 4, so the physical address is \(4 \times 256 + 32 = 1056\). [B1]

Address 600: \(600 \text{ DIV } 256 = 2\), \(600 \text{ MOD } 256 = 88\). Page 2 is not in main memory, so the hardware raises a **page fault**. [B1] The page must be fetched from disk into a free frame and the page table updated; only then can the address be formed as that frame number × 256 + 88. [B1]

The syllabus asks you to explain paging, not to calculate with it, but the calculation shows what the page table is for.
:::

Because every page is the same size, any free frame will do, so the operating system never has to find a large gap. The cost is that the last page of a process is usually only partly full, which wastes a little space inside it.

### Segmentation

:::def Segmentation
A memory management method in which a process's memory is divided into variable-sized blocks called segments, each of which holds a logical part of the program, such as its code, its data or its stack. Each segment has its own base address and size limit in a segment table.
:::

A segment follows the structure of the program, so it is as large or small as that part needs. A logical address is a pair: a segment number and an offset inside the segment. The segment table records where each segment starts in RAM (its base) and how long it is (its limit). An offset beyond the limit is an error, which protects one segment from another.

:::eg Translating a segment address
A process has this segment table.

| Segment | Content | Base address | Limit (size) |
|---|---|---|---|
| 0 | code | 2000 | 600 |
| 1 | data | 5000 | 300 |
| 2 | stack | 9000 | 200 |

Find the physical address for the logical address (segment 1, offset 120), and say what happens for (segment 1, offset 350). [2 marks]

Segment 1 starts at 5000, and \(120 < 300\), so the physical address is \(5000 + 120 = 5120\). [B1]

The offset 350 is larger than the segment's limit of 300, so the address is outside the segment and the operating system reports an error (it stops the program). [B1]
:::

### The difference between paging and segmentation

| | Paging | Segmentation |
|---|---|---|
| Size of the blocks | fixed (every page and frame is the same size) | variable (each segment has its own size) |
| How the blocks are chosen | by the system, with no regard to what is in them | by the programmer or compiler, as logical parts such as code, data and stack |
| What the table holds | the frame number for each page | the base address and limit for each segment |
| Address | a page number and an offset | a segment number and an offset |
| Wasted space | a little in the last page of a process | gaps of unused memory can appear between segments of different sizes |

:::warn A page is fixed size, a segment is not
A very common error is to say "pages and segments are both blocks of memory" and stop. The marks are for the differences: fixed against variable size, and physical division by the system against logical division by the program's structure.
:::

## Virtual memory

:::def Virtual memory
A technique in which part of secondary storage (the swap area) is used as an extension of main memory, so that programs and data larger than the available RAM can be used. Only the parts that are needed are in RAM, and the rest stay on disk until they are needed.
:::

Suppose a computer has 4 GiB of RAM, and you start programs whose total size is 6 GiB. Without virtual memory they would not all fit. With virtual memory, the operating system keeps the pages that are being used in RAM and the others in the swap area of the disk. A program thinks it has memory for all of its addresses.

Virtual memory is usually built on paging. The page table has an entry for every page of the process, with a marker that says whether the page is in RAM or on disk. When the processor uses a page, one of two things happens.

:::steps
1. **The page is in RAM.** The page table gives its frame and the access goes ahead.
2. **The page is not in RAM, so a page fault occurs.** An interrupt calls the kernel.
3. The kernel finds the page on disk and a free frame. If there is no free frame, it first chooses a page in RAM to remove (page replacement, below). If that page was changed, it is written back to disk.
4. The process is blocked while the disk transfers the page, and another process uses the processor meanwhile.
5. The page table is updated and the page is marked as being in RAM. The process becomes ready, and when it runs again it repeats the instruction that faulted.
:::

:::def Page fault
An interrupt generated when a process tries to use a page that is not in main memory. The operating system must load the page from secondary storage.
:::

:::key Virtual memory: benefits and drawbacks
**Benefits:** programs can be larger than the RAM; more processes can be in memory at once (so the processor is busier); only the pages in use take up RAM.

**Drawbacks:** a page fault means a disk access, which is thousands of times slower than RAM; if page faults are too frequent the computer becomes very slow (disk thrashing); the swap area uses disk space.
:::

### Page replacement

When RAM is full and a page must be brought in, the operating system must choose a page to remove. The choice is made by a **page replacement algorithm**.

:::def Page replacement
The method used by the operating system to choose which page in main memory is removed (or overwritten) to make room for a page that must be loaded from disk.
:::

Two common algorithms:

- **First in first out (FIFO).** Remove the page that has been in RAM longest. It is simple, but the oldest page may be one that is used all the time.
- **Least recently used (LRU).** Remove the page that has not been used for the longest time. It follows the idea that a page not used recently is unlikely to be needed soon, so it usually causes fewer page faults, but the system must keep a record of when each page was last used.

:::eg FIFO against LRU
A process is allowed 3 frames. It uses the pages in this order: 4, 1, 2, 4, 1, 3, 4, 1, 5, 4, 1, 2. Compare the number of page faults for FIFO and LRU. [4 marks]

In the table each list shows the pages in RAM, oldest first for FIFO and least recently used first for LRU.

| Page used | FIFO: pages in RAM | Fault? | LRU: pages in RAM | Fault? |
|---|---|---|---|---|
| 4 | 4 | yes | 4 | yes |
| 1 | 4, 1 | yes | 4, 1 | yes |
| 2 | 4, 1, 2 | yes | 4, 1, 2 | yes |
| 4 | 4, 1, 2 | | 1, 2, 4 | |
| 1 | 4, 1, 2 | | 2, 4, 1 | |
| 3 | 1, 2, 3 | yes | 4, 1, 3 | yes |
| 4 | 2, 3, 4 | yes | 1, 3, 4 | |
| 1 | 3, 4, 1 | yes | 3, 4, 1 | |
| 5 | 4, 1, 5 | yes | 4, 1, 5 | yes |
| 4 | 4, 1, 5 | | 1, 5, 4 | |
| 1 | 4, 1, 5 | | 5, 4, 1 | |
| 2 | 1, 5, 2 | yes | 4, 1, 2 | yes |

- the first three pages cause faults in both algorithms [B1]
- FIFO removes the oldest page (4) when 3 is loaded, although 4 is used again at once [B1]
- LRU removes the least recently used page (2), so 4 and 1 stay in RAM [B1]
- FIFO has 8 page faults and LRU has 6 [B1]
:::

### Disk thrashing

:::def Disk thrashing
A situation in which the operating system spends most of its time moving pages between main memory and disk, instead of running processes, because there are so many page faults. The computer becomes extremely slow although the processor seems busy.
:::

Thrashing begins when the total of the pages that the running processes need at once is larger than the RAM. Each process keeps having its pages removed to make room for the others, and then needs them straight back. The result is a chain reaction.

1. Too many processes are in memory for the amount of RAM, so each has too few frames.
2. Every process page-faults frequently, and each fault waits for a disk transfer.
3. The processes spend most of their time blocked, waiting for pages, so the processor is idle for much of the time.
4. The operating system sees the low processor use and may admit more processes, which makes it worse.

The effect on speed is huge, because a disk is so much slower than RAM. If a RAM access takes 100 ns and a page fault takes 10 ms (10 000 000 ns), then with one fault in every 1000 accesses the time for 1000 accesses is \(999 \times 100 + 1 \times 10\,000\,000 = 10\,099\,900\) ns, an average of 10 099.9 ns per access: about 101 times slower than when there are no faults.

:::key Preventing thrashing
- Add more RAM.
- Run fewer processes at the same time, so that each has enough frames.
- Use a better page replacement algorithm, so that the pages in use stay in RAM.
- Close programs or use smaller programs.
:::

:::warn Thrashing is not "the disk is full"
It is also not the processor overheating or a hard disk failing. Thrashing is excessive swapping of pages between RAM and disk, caused by too many page faults. A full disk would be a different problem.
:::

:::eg Spot the error: the state diagram
Question: A process is blocked because it is waiting for a keyboard input. The key is pressed. Describe what happens to the process. [3 marks]

A student wrote: "The keyboard sends an interrupt, and the process goes from blocked to running because it can continue now."

The keyboard sending an interrupt is correct [B1]. **The process does not go straight from blocked to running: it moves from blocked to ready, and runs when the scheduler chooses it, so the transition is wrong [B0].** The idea that the process can continue is correct, but the scheduler is not mentioned [B1]. The answer scores 2 out of 3.

A full answer: the keyboard sends an interrupt, the kernel's interrupt handler moves the process from blocked to ready, and the process runs only when the low-level scheduler selects it.
:::

:::eg Spot the error: explaining thrashing
Question: Explain what is meant by disk thrashing. [3 marks]

A student wrote: "Thrashing happens when the hard disk becomes full, so the computer cannot save any more files and it slows down."

**The cause is wrong: thrashing is not caused by a full disk. It is caused by too many page faults [B0].** The answer says that the computer slows down, which is true [B1]. It does not say that pages are being swapped between RAM and the disk, or that the system spends more time swapping than processing [B0]. The answer scores 1 out of 3.

A correct answer says that the processes need more pages than fit in RAM, so pages are constantly swapped between RAM and disk, and the computer spends more time swapping pages than executing processes.
:::

:::try Start easy, finish at exam standard
Q: Name the three process states examined in this chapter.
A: Running, ready and blocked.
Q: State the event that moves a process from the running state to the ready state.
A: Its time slice ends (a timer interrupt), or it is pre-empted.
Q: A process is blocked waiting for a disk read. State what must happen before it can run again.
A: The disk must finish and send an interrupt, so the process moves to ready; then the scheduler must choose it.
Q: Define "pre-emptive" scheduling.
A: A pre-emptive algorithm lets the operating system take the processor from a running process before it has finished.
Q: Three processes arrive together at time 0 with burst times X = 4, Y = 1 and Z = 3. Using first come first served in the order X, Y, Z, calculate the waiting time of each and the average.
A: X runs 0 to 4, Y 4 to 5, Z 5 to 8. Waiting times are 0, 4 and 5, so the average is \(9 \div 3 = 3\).
Q: For the processes in the previous question, use shortest job first and calculate the average waiting time.
A: The order is Y (1), Z (3), X (4). Y waits 0, Z waits 1 and X waits 4, so the average is \(5 \div 3\), which is about 1.67 (exactly \(5/3\)). SJF is better than FCFS here (3).
Q: State one drawback of shortest job first.
A: The burst time of each process must be known or estimated in advance, and long processes can be starved.
Q: A round robin scheduler has a quantum of 3, and a process needs 7 units. Into how many time slices does it run (if it has to wait its turn each time)?
A: Three slices: 3, 3 and 1.
Q: State the difference between a page and a segment.
A: A page is a fixed-size block, chosen by the system; a segment is a variable-size block that is a logical part of a program.
Q: A page size is 100 bytes. Which page and offset is logical address 372 in?
A: Page 3 (\(372 \text{ DIV } 100\)), offset 72 (\(372 \text{ MOD } 100\)). Real pages are powers of 2, but 100 keeps the arithmetic simple.
Q: State what a page fault is.
A: An interrupt that happens when a process uses a page that is not in main memory, so that the operating system must load it from disk.
Q: Give two ways to stop disk thrashing.
A: Add more RAM, or run fewer processes at once.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ A process is running. State the state change caused by each event. (i) Its time slice ends. (ii) It asks for a record to be read from a disk. (iii) The disk has finished and sends an interrupt. (iv) The scheduler chooses it from the ready queue.
H: Use the three states running, ready and blocked. A blocked process cannot go straight to running.
A: (i) running to ready [B1]; (ii) running to blocked [B1]; (iii) blocked to ready [B1]; (iv) ready to running [B1].

Q: [3 marks] ★ Describe how a timer interrupt allows an operating system to run several processes in turn on one processor.
H: Think about what the kernel does with the running process, and what it does next.
A: The marks are:

- the timer sends an interrupt at regular intervals, which ends the time slice of the running process [B1]
- the kernel saves the state (registers and program counter) of the running process and puts it into the ready queue [B1]
- the scheduler chooses the next process from the ready queue, and its saved state is loaded into the processor so that it continues from where it stopped [B1]

Q: [5 marks] ★★ Four processes arrive at a computer that uses round robin with a quantum of 2. A process that arrives when another's time slice ends joins the queue before it.

| Process | Arrival time | Burst time |
|---|---|---|
| E | 0 | 3 |
| F | 1 | 4 |
| G | 2 | 1 |
| H | 5 | 2 |

(a) Draw the Gantt chart as a list of time slices. [3] (b) Calculate the average waiting time. [2]
H: Keep a queue. At time 2, F and G have both arrived, and they join before E.
H: Waiting time = completion time − arrival time − burst time.
A: (a) E (0–2), F (2–4), G (4–5), E (5–6), F (6–8), H (8–10).

The queue after E's first slice is F, G, E. After F's slice (2 to 4) it is G, E, F. G finishes at 5, and H arrives at 5, so the queue is E, F, H. E runs 5 to 6 and finishes; F runs 6 to 8 and finishes; H runs 8 to 10 and finishes.

- E (0–2), F (2–4) and G (4–5) correct [B1]
- E (5–6) next, after G finishes [B1]
- F (6–8) before H (8–10), because F had rejoined the queue before H arrived [B1]

(b) Completion times: E 6, F 8, G 5, H 10. Waiting times: E \(6 - 0 - 3 = 3\), F \(8 - 1 - 4 = 3\), G \(5 - 2 - 1 = 2\), H \(10 - 5 - 2 = 3\). [B1] Average \(= (3 + 3 + 2 + 3) \div 4 = 11 \div 4 = 2.75\). [B1]

Q: [4 marks] ★★ Four processes arrive as shown.

| Process | Arrival time | Burst time |
|---|---|---|
| W | 0 | 6 |
| X | 1 | 2 |
| Y | 2 | 4 |
| Z | 3 | 1 |

Calculate the average waiting time for first come first served and for shortest job first (non-pre-emptive), and state which is smaller.
H: Under SJF, at time 6 the ready processes are X, Y and Z.
A: FCFS: W 0–6, X 6–8, Y 8–12, Z 12–13. Waiting times: W 0, X \(6 - 1 = 5\), Y \(8 - 2 = 6\), Z \(12 - 3 = 9\). [B1] Average \(= 20 \div 4 = 5\). [B1]

SJF: W 0–6, then Z (1) 6–7, X (2) 7–9, Y (4) 9–13. Waiting times: W 0, Z \(6 - 3 = 3\), X \(7 - 1 = 6\), Y \(9 - 2 = 7\). [B1] Average \(= 16 \div 4 = 4\), which is smaller than FCFS (5). [B1]

Q: [4 marks] ★★ A process uses pages of 512 bytes. Its page table is: page 0 in frame 3, page 1 in frame 0, page 2 in frame 5. Calculate the physical address for (a) the logical address 1300, and (b) the logical address 700. [2 marks each]
H: Page number = address DIV 512. Offset = address MOD 512.
A: (a) \(1300 \text{ DIV } 512 = 2\) and \(1300 \text{ MOD } 512 = 276\). [B1] Page 2 is in frame 5, so the physical address is \(5 \times 512 + 276 = 2836\). [B1]

(b) \(700 \text{ DIV } 512 = 1\) and \(700 \text{ MOD } 512 = 188\). [B1] Page 1 is in frame 0, so the physical address is \(0 \times 512 + 188 = 188\). [B1]

Q: [5 marks] ★★ Explain how virtual memory allows a program that is larger than the computer's RAM to run, and how disk thrashing can occur.
H: Three marks for virtual memory, two for thrashing.
A: The marks are:

- Part of the secondary storage is used as an extension of RAM [B1]
- Only the pages that the program is using are kept in RAM and the rest stay on the disk [B1]
- When a page that is needed is not in RAM, it is loaded from the disk and another page is swapped out, so the program can be larger than RAM [B1]
- If too many processes are running (or RAM is too small), page faults happen very often [B1]
- The operating system then spends more time swapping pages between RAM and disk than running the processes, which is thrashing [B1]

Q: [8 marks] ★★★ The computers in a school computer room in Kampala have 2 GiB of RAM. When students open many programs at once, a computer becomes very slow and the disk light flashes almost continuously, even though the processor is not busy.

(a) Name the problem that is occurring. [1] (b) Explain why it makes the computer slow. [3] (c) State two ways the problem could be reduced. [2] (d) Describe what a page fault is and what the operating system does when one occurs. [2]
H: The clue is the flashing disk light with an idle processor.
A: (a) Disk thrashing. [B1]

(b) Together the programs need more pages than fit in RAM, so pages must be swapped between RAM and the disk all the time [B1]. Disk access is far slower than RAM access [B1]. The processes spend most of their time blocked, waiting for pages, so little real work is done and the processor is idle [B1].

(c) Any two: add more RAM; close some programs (run fewer processes); use a better page replacement algorithm. [B1] [B1]

(d) A page fault is an interrupt that occurs when a process uses a page that is not in RAM [B1]. The operating system loads the page from the disk into a free frame (replacing another page if there is none) and updates the page table, while the process is blocked [B1].

Q: [7 marks] ★★★ Four processes arrive at a computer that uses shortest remaining time scheduling.

| Process | Arrival time | Burst time |
|---|---|---|
| J | 0 | 7 |
| K | 2 | 4 |
| L | 4 | 1 |
| M | 5 | 4 |

(a) Draw the Gantt chart as a list of time slices. [3] (b) Calculate the average waiting time. [2] (c) Explain one drawback of shortest remaining time shown by the process J. [2]
H: At time 2, K needs 4 and J has 5 left. At time 4, K has 2 left and L needs 1.
A: (a) J (0–2), K (2–4), L (4–5), K (5–7), M (7–11), J (11–16).

- J (0–2) then K (2–4), because K needs less than the 5 that J has left [B1]
- L (4–5) pre-empts K (which has 2 left), then K (5–7) [B1]
- M (7–11), then J (11–16) [B1]

(b) Completion times: J 16, K 7, L 5, M 11. Waiting times: J \(16 - 0 - 7 = 9\), K \(7 - 2 - 4 = 1\), L \(5 - 4 - 1 = 0\), M \(11 - 5 - 4 = 2\). [B1] Average \(= 12 \div 4 = 3\). [B1]

(c) J is the longest process, and it has to wait until all the shorter processes have finished (it finishes last, with a waiting time of 9) [B1]. If shorter processes kept arriving, J might never be chosen: it would be starved [B1].
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A process uses 3 frames and the page sequence 1, 2, 3, 1, 2, 4, 1, 2, 5, 1, 2, 3. (a) Calculate the number of page faults using FIFO and using LRU. [4] (b) Explain why FIFO gives more faults on this sequence. [2]
H: Pages 1 and 2 are used again and again. See which algorithm keeps them in RAM.
H: Make a table like the earlier example, with one row for each page used.
A: (a) FIFO: the frames hold 1; 1, 2; 1, 2, 3 (three faults); the next 1 and 2 are hits; 4 replaces 1 (the oldest) giving 2, 3, 4; then 1 is a fault and replaces 2 (3, 4, 1); then 2 is a fault and replaces 3 (4, 1, 2); 5 replaces 4 (1, 2, 5); the next 1 and 2 are hits; 3 replaces 1 (2, 5, 3). That is 8 faults in total. [B1] [B1]

LRU: three faults to start with; the next 1 and 2 are hits; 4 replaces 3, the least recently used (1, 2, 4); then 1 and 2 are hits; 5 replaces 4 (1, 2, 5); then 1 and 2 are hits; 3 replaces 5 (1, 2, 3). That is 6 faults in total. [B1] [B1]

(b) Pages 1 and 2 are used constantly. FIFO removes the page that has been in RAM longest, and that is often 1 or 2, so it has to load them again [B1]. LRU keeps recently used pages and removes the page that has not been used for longest, so 1 and 2 stay in RAM [B1].

Q: [5 marks] ★★★ Three processes each need 12 time units of processor time and all arrive at time 0. The computer uses round robin. Each switch from one process to a different one takes 1 time unit, during which no process runs. (a) For quanta of 2, 6 and 12, state the number of switches. [1] (b) State the time at which all three have finished for each quantum. [1] (c) State the time at which the third process first starts to run for each quantum. [1] (d) Explain the trade-off between a small and a large quantum. [2]
H: With equal bursts the order is always A, B, C, A, B, C, and so on.
H: The total time is 36 plus the time spent switching.
A: (a) With a quantum of 2 there are 18 slices, so 17 switches; with 6 there are 6 slices and 5 switches; with 12 there are 3 slices and 2 switches. [B1]

(b) Total time \(= 36 + \text{switches}\): 53, 41 and 38. [B1]

(c) The third process C starts after one slice of A, a switch, one slice of B and a switch: \(2q + 2\), which is 6, 14 and 26. [B1]

(d) A small quantum gives each process a turn quickly (good response), but there are many switches, which waste time [B1]. A large quantum wastes little time on switching, but processes wait a long time for their first turn, and it behaves like first come first served [B1].
:::

:::quiz
? Which state change is **not** possible for a process?
- running to blocked
- blocked to ready
- ready to running
+ blocked to running
> A blocked process must first become ready when the event it was waiting for has happened, and then the scheduler chooses it. A direct change from blocked to running does not exist.
? What does a timer interrupt do in a multi-tasking system?
- It starts the disk transfer.
+ It ends the running process's time slice, so the kernel can switch to another process.
- It moves a process from blocked to running.
- It removes a page from RAM.
> The timer marks the end of a time slice. The kernel then saves the process's state and the scheduler selects the next one.
? What is the difference between shortest job first and shortest remaining time?
- SJF is fair and SRT is not.
+ SRT can pre-empt a running process when a shorter one arrives, but SJF lets it finish.
- SJF uses a quantum and SRT does not.
- SRT does not need to know the burst times.
> SRT is the pre-emptive version of SJF. Both need the burst times to be known or estimated, and neither uses a time quantum.
? Which problem is most associated with first come first served?
+ A short process can wait a long time behind a long process.
- A long process can be starved by a stream of short ones.
- It needs the burst time of every process.
- It causes disk thrashing.
> This is the convoy effect. Starvation of long processes and the need for burst times belong to SJF and SRT.
? In round robin, what happens if the time quantum is longer than every process's burst time?
+ It behaves like first come first served.
- It behaves like shortest job first.
- No process ever finishes.
- Every process is starved.
> Each process runs to the end of its burst in its first slice, in order of arrival, which is first come first served.
? How does a page differ from a segment?
- A page is stored on disk and a segment in RAM.
+ A page is a fixed-size block; a segment is a variable-size block that is a logical part of the program.
- A page is variable size and a segment is fixed size.
- A segment holds only code.
> The reverse of the second option is a common slip. Pages and frames are the same fixed size, but segments follow the program's own structure.
? What is a page fault?
- An error in the program's code.
+ An interrupt that occurs when a page that is needed is not in main memory.
- A hard disk failure.
- The removal of a page from RAM.
> The operating system must load the page from secondary storage. A page fault is a normal event in virtual memory, but too many of them cause thrashing.
? Which statement describes disk thrashing?
- The hard disk is full, so no more files can be saved.
+ The operating system spends most of its time swapping pages between RAM and disk, and little time running processes.
- The processor overheats because it runs too fast.
- Too few pages are in the swap area.
> Thrashing is caused by too many page faults, usually because too many processes are competing for too little RAM.
? Which page replacement algorithm removes the page that has been in RAM the longest?
+ FIFO (first in first out)
- LRU (least recently used)
- shortest remaining time
- round robin
> FIFO removes the oldest page whether or not it is still being used. LRU removes the page that has gone unused for longest. The other two are scheduling algorithms, not page replacement methods.
:::

:::checklist What you can now do
- [ ] I can explain how an operating system maximises the use of the processor, memory and input/output devices.
- [ ] I can explain how a user interface and device drivers hide the complexity of the hardware.
- [ ] I can define a process, explain multi-tasking and describe the running, ready and blocked states with the event that causes each change.
- [ ] I can explain why scheduling is needed and describe first come first served, shortest job first, shortest remaining time and round robin, with their benefits and drawbacks.
- [ ] I can draw a Gantt chart for a set of processes under each algorithm and calculate the waiting time and turnaround time.
- [ ] I can describe the kernel as the interrupt handler and the low-level scheduler, and describe what happens when a timer or input/output interrupt occurs.
- [ ] I can describe paging (pages, frames and the page table) and segmentation, and explain the difference.
- [ ] I can explain virtual memory, page faults and page replacement (FIFO and LRU).
- [ ] I can explain what disk thrashing is, how it happens and how to reduce it.
:::

:::recap
- The operating system keeps resources busy: while one process waits for input or output, the processor runs another. The user interface and device drivers hide the hardware.
- A process is a program being run. States: **running**, **ready**, **blocked**. Ready to running when the scheduler chooses it; running to ready when the time slice ends; running to blocked when it waits for I/O; blocked to ready (never straight to running) when the I/O finishes.
- Turnaround time = completion − arrival. Waiting time = turnaround − burst.
- FCFS: in order of arrival, simple, convoy effect. SJF: shortest burst first, non-pre-emptive, low average waiting time, needs estimates, may starve. SRT: pre-emptive SJF. RR: fixed quantum, fair, pre-emptive; too small wastes time switching, too large becomes FCFS.
- The kernel handles interrupts and does low-level scheduling. A timer interrupt ends a time slice: the state is saved, the scheduler picks the next ready process and its state is loaded (a context switch).
- Paging: fixed-size pages and frames, a page table, physical address = frame × page size + offset. Segmentation: variable-size logical segments, with a base and a limit.
- Virtual memory uses disk as an extension of RAM. A page fault loads a missing page. Page replacement chooses the page to remove: FIFO (oldest) or LRU (least recently used).
- Disk thrashing: so many page faults that the system spends more time swapping pages than running processes. Fix: more RAM, fewer processes.
:::

:::links
- practise: [Purposes of an operating system: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/16-system-software-/purposes-of-an-operating-system-os/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists on how operating systems work
- watch: [Craig 'n' Dave](https://www.youtube.com/@craigndave) · Craig 'n' Dave · A Level topic videos on operating systems (UK boards; content overlaps 9618)
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations and questions on operating systems (written for UK boards)
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · watch a program run one step at a time, as the kernel does with a process

Links checked 13 November 2026.
:::

Next: [Compilers, BNF and Reverse Polish notation](#cs.translators)
