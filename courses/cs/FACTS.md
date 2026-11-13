# FACTS: Computer Science

Verified exam facts and the syllabus learning outcomes (LEAD, 13 November 2026). Sources: the 9618 syllabus for
2027–2029 (version 3, October 2026), the 2027–2029 Pseudocode Guide (version 1), and the May/June 2025 question
papers 9618/11, 9618/21 (with its insert), 9618/31 and 9618/41 (front pages read in full). Nothing here is assumed.

## The qualification
- Cambridge International AS & A Level Computer Science 9618, syllabus for exams in 2027, 2028 and 2029. Exams in the
  June and November series. Previous study recommended: IGCSE or O Level Computer Science (not required).
- About 180 guided learning hours for AS, about 360 for the full A Level.
- AS Level = Papers 1 and 2. A Level = all four papers. Routes: AS only; A Level staged over two years (AS marks
  carried forward); A Level in one series. AS grades a–e; A Level grades A*–E.
- **Calculators must not be used in any paper** (syllabus page 11, and printed on the front of Papers 1, 2 and 3).
- Cannot be combined in the same series with 9626 Information Technology.

## The papers (syllabus page 11)
| Paper | Title | Time | Marks | Content | Weighting |
|---|---|---|---|---|---|
| 1 | Theory Fundamentals | 1 h 30 min | 75 | sections 1–8 | 50% of AS, 25% of A Level |
| 2 | Fundamental Problem-solving and Programming Skills | 2 h | 75 | sections 9–12 | 50% of AS, 25% of A Level |
| 3 | Advanced Theory | 1 h 30 min | 75 | sections 13–20 | 25% of A Level |
| 4 | Practical | 2 h 30 min | 75 | sections 19–20, except low-level and declarative programming | 25% of A Level |
- Papers 1, 2, 3: written, externally assessed, "answer all questions", some short and some longer answers.
- Paper 2: candidates write answers in **pseudocode**; "will not be required to write programming code"; an
  **Insert** lists the pseudocode built-in functions and operators.
- Paper 4: on a computer with no internet or email; Java (console mode), Visual Basic .NET (console mode) or
  Python (console mode). Candidates submit program code and evidence of testing in an evidence document.
  Tasks are based around a small number of scenarios. Source files given will not contain binary files.

### Assessment objectives
- AO1 knowledge and understanding; AO2 application (analyse problems in computational terms); AO3 design, program
  and evaluate computer systems.
- AS: AO1 30%, AO2 40%, AO3 30%. A Level: AO1 30%, AO2 30%, AO3 40%.
- By paper: P1 AO1 60 / AO2 40; P2 AO2 40 / AO3 60; P3 AO1 60 / AO2 40; P4 AO3 100.

### Command words (syllabus page 41, the Cambridge meanings)
Analyse, Assess, Calculate, Comment, Compare, Complete (add to a diagram or table), Consider, Contrast, Define,
Demonstrate, Describe (state the points / give characteristics and main features), Develop, Discuss, Draw ("draw a
line to match a term with a description"), Evaluate, Examine, Explain (set out purposes or reasons, say why and/or
how, with evidence), Give, Identify (name/select/recognise), Justify (support a case with evidence/argument),
Outline, Predict, Sketch, State (express in clear terms), Suggest, Summarise, Write (write an answer in a specific
way).

## What each paper prints and allows (front pages, May/June 2025)
### Paper 1 (9618/11, May/June 2025)
- 1 hour 30 minutes. "You must answer on the question paper. No additional materials are needed."
- Instructions: answer all questions; black or dark blue pen; HB pencil for diagrams, graphs or rough working;
  **"Calculators must not be used in this paper."**
- Information: total 75 marks; marks for each part in brackets [ ]; **"No marks will be awarded for using brand
  names of software packages or hardware."**
- That paper: 20 pages, 8 questions (4 to 14 marks each: 4, 13, 7, 6, 13, 14, 11, 7). Scenario-based questions
  (a video-conference company, a shop, a furniture company database, buying a computer, a banker's data).
- The assembly-language question prints the part of the instruction set it uses (a table of opcode, operand,
  explanation), so the instruction set is never memorised; questions print memory contents to trace.
- Logic questions give a circuit or a statement and ask for an expression or a truth table (with working space).

### Paper 2 (9618/21, May/June 2025)
- 2 hours. Answer on the question paper. **"You will need: Insert (enclosed)"**; "The insert contains all the
  resources referred to in the questions." Calculators must not be used. No marks for brand names.
- That paper: 20 pages, 7 questions, 75 marks. Questions start "Refer to the insert for the list of pseudocode
  functions and operators." Style: a scenario per question; identifier tables, flowcharts with logic errors to
  find, decomposition, trace tables (dry run of given pseudocode), stacks and queues with pointers, "write
  efficient pseudocode for the procedure …", modules that read and write a text file, structure-chart style module
  descriptions, a final long question built round several modules.
- **The insert (4 pages)** lists, with examples:
  - String and character functions: LEFT, RIGHT, MID(ThisString, x, y) (y characters from position x),
    LENGTH, TO_UPPER, TO_LOWER (CHAR or STRING), NUM_TO_STR, STR_TO_NUM, IS_NUM, ASC (ASCII value), CHR.
    Notes: a string of length 1 may be CHAR or STRING; a CHAR may be assigned to or concatenated with a STRING;
    a STRING longer than 1 cannot be assigned to a CHAR.
  - Numeric: INT(x) (integer part), RAND(x) (real in 0 to x, not including x).
  - Date (DD/MM/YYYY): DAY, MONTH, YEAR, DAYINDEX (Sunday = 1), SETDATE(Day, Month, Year), TODAY().
  - Text file: EOF(FileName) (TRUE if no more lines; error if the file is not open in READ mode).
  - Operators: & (concatenate), AND, OR, NOT, MOD (10 MOD 3 = 1), DIV (10 DIV 3 = 3); comparison = > < >= <= <>
    (case sensitive for CHAR/STRING; REAL and INTEGER may be compared; records cannot be compared).
  - An error is generated if a function call is badly formed or an operator gets a value of the wrong type.
- So: string-function names in the course follow the insert (TO_UPPER, TO_LOWER, LEFT …). The 2027–2029
  Pseudocode Guide itself lists only RIGHT, LENGTH, MID, LCASE, UCASE, INT, RAND and says string functions "will
  always be provided in examinations". Questions use only what the insert of that paper gives.

### Paper 3 (9618/31, May/June 2025)
- 1 hour 30 minutes. Answer on the question paper. No additional materials. Calculators must not be used. 75 marks.
  No marks for brand names.
- That paper: 16 pages, 12 questions of 4 to 9 marks (floating point, TCP/IP layers, a linked list, a truth table
  to simplify, interpreters, syntax diagrams, multi-tasking, SSL/TLS, graphs in AI, a class to design, a pseudocode
  algorithm to complete).

### Paper 4 (9618/41, May/June 2025)
- 2 hours 30 minutes. "You will need: Candidate source files (listed on page 2), evidence.doc".
- Instructions: carry out every instruction in each task; save work using the file names given; no internet or
  email; save work in the evidence document, or no marks for that task; use Java (console mode), Python (console
  mode) or Visual Basic (console mode); **a mark of zero if another language is used**. 75 marks.
- Page 2: open evidence.doc, save it as evidence_ + centre number_candidate number; "A class declaration can be used
  to declare a record. If the programming language used does not support arrays, a list can be used instead."
- That paper: 12 pages, **3 questions: 20, 25 and 30 marks** (a circular queue in a global 1D array of 20 with
  head/tail pointers and a counter; reading a text file, splitting the data and writing it to several text files;
  a binary tree designed with OOP: classes Node and Tree, a recursive in-order output). Each part says "Save your
  program as Question1_J25 … copy and paste the program code into part 1(a) in the evidence document" and testing
  parts ask for a screenshot of the output.

## Pseudocode conventions (2027–2029 Pseudocode Guide, version 1)
- Monospaced font; indentation usually three spaces; keywords in upper case; identifiers in mixed case
  (NumberOfPlayers), letters, digits and underscore only, start with a letter, case insensitive.
- Comments `//`. Data types INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE. Literals: REAL always has a digit on both
  sides of the point (4.0, 0.3); CHAR in single quotes 'x'; STRING in double quotes; dates dd/mm/yyyy.
- `DECLARE Counter : INTEGER` · `CONSTANT HourlyRate = 6.50` (constants use =, only literal values) ·
  assignment `Counter ← Counter + 1`.
- Arrays: `DECLARE StudentNames : ARRAY[1:30] OF STRING`, `DECLARE Board : ARRAY[1:3,1:3] OF CHAR`, element
  `Board[2,3]`; lower bound usually 1; whole-array assignment allowed between arrays of the same size and type;
  never `Names[1 TO 30] ← ""` (use a loop).
- User-defined types: `TYPE Season = (Spring, Summer, Autumn, Winter)`; `TYPE TIntPointer = ^INTEGER`;
  record `TYPE StudentRecord … DECLARE LastName : STRING … ENDTYPE`, fields by dot notation `Pupil1.LastName`;
  set `TYPE LetterSet = SET OF CHAR` and `DEFINE Vowels ('A','E','I','O','U'): LetterSet`; `MyPointer ← ^ThisSeason`,
  `MyPointer^` is the value pointed to.
- `INPUT Answer`; `OUTPUT "You have ", Lives, " lives left"` (comma-separated values).
- Operators: + – * / (/ always gives REAL), DIV, MOD; = <> < > <= >=; AND OR NOT; & joins strings.
- `IF … THEN … ELSE … ENDIF`; `CASE OF Move … 'W' : … OTHERWISE : … ENDCASE` (ranges `1 TO 5 :`; first matching
  case only).
- `FOR Index ← 1 TO 30 … NEXT Index` (optional `STEP`, may be negative; runs zero times if start > end);
  `REPEAT … UNTIL <condition>` (at least once); `WHILE <condition> … ENDWHILE` (maybe zero times).
- `PROCEDURE Name(P : INTEGER) … ENDPROCEDURE`, called with `CALL Name(5)`;
  `FUNCTION Max(A : INTEGER, B : INTEGER) RETURNS INTEGER … RETURN … ENDFUNCTION`, called inside an expression,
  never with CALL; `BYREF`/`BYVAL` before parameters (default BYVAL); never BYREF to a function.
- Text files: `OPENFILE "F.txt" FOR READ` (or WRITE, APPEND), `READFILE "F.txt", Line`, `WRITEFILE "F.txt", Data`,
  `EOF("F.txt")`, `CLOSEFILE "F.txt"`. Random files: `OPENFILE … FOR RANDOM`, `SEEK`, `GETRECORD`, `PUTRECORD`.
- OOP: `CLASS Pet … ENDCLASS`, `PRIVATE Name : STRING`, `PUBLIC PROCEDURE NEW(GivenName : STRING)` (constructor),
  `CLASS Cat INHERITS Pet`, `SUPER.NEW(GivenName)`, `MyCat ← NEW Cat("Kitty", "Shorthaired")`, `Player.SetAttempts(5)`.
  Members public unless stated.

## Assembly language (syllabus 4.2, 4.3: the example instruction set)
LDM #n (immediate, load n to ACC) · LDD <address> (direct) · LDI <address> (indirect) · LDX <address> (indexed:
address + IX) · LDR #n (load n to IX) · MOV <register> (ACC to IX) · STO <address> · ADD <address> / ADD #n/Bn/&n ·
SUB <address> / SUB #n/Bn/&n · INC <register> / DEC <register> (ACC or IX) · JMP <address> · CMP <address> /
CMP #n · CMI <address> (indirect compare) · JPE <address> (jump if compare True) · JPN <address> (jump if False) ·
IN (key in a character, ASCII to ACC) · OUT (output the character whose ASCII value is in ACC) · END.
Bit manipulation: AND / XOR / OR with #n, Bn, &n or <address>; LSL #n and LSR #n (logical shifts, zeros in).
Labels: `<label>: <opcode> <operand>` and `<label>: <data>`. One general-purpose register (ACC); IX is the index
register; # denary, B binary (B01001010), & hexadecimal (&4A). Papers print the subset they use.

## Learning outcomes, AS (Papers 1 and 2)
**1.1 Data representation.** Binary prefixes vs decimal prefixes (kibi/kilo, mebi/mega, gibi/giga, tebi/tera).
Binary, denary, hexadecimal, BCD, one's and two's complement; convert integers between bases/representations;
binary addition and subtraction with positive and negative integers; overflow; practical uses of BCD and hex;
character data in binary: ASCII, extended ASCII, Unicode (no codes to memorise).
**1.2 Multimedia.** Bitmaps: pixel, file header, image resolution, screen resolution, colour depth/bit depth;
estimate bitmap file size; effects of changing resolution and colour depth on quality and size. Vector graphics:
drawing object, property, drawing list; justify bitmap vs vector. Sound: sampling, sampling rate, sampling
resolution, analogue and digital data; effect of rate and resolution on file size and accuracy.
**1.3 Compression.** Need for compression; lossy vs lossless and justify one; how text, bitmap, vector and sound
files can be compressed, including run-length encoding (RLE).
**2.1 Networks including the internet.** Purpose and benefits of networking; LAN and WAN; client-server and
peer-to-peer (roles, subnetwork models, benefits, drawbacks, justify); thin and thick client; bus, star, mesh,
hybrid topologies, how packets travel in each, justify a topology; cloud computing, public and private, benefits
and drawbacks; wired vs wireless; copper cable, fibre-optic, radio waves (incl. WiFi), microwaves, satellites;
LAN hardware: switch, server, NIC, WNIC, WAP, cables, bridge, repeater; role of a router; Ethernet, collisions,
CSMA/CD; bit streaming, real-time and on-demand, importance of bit rate/broadband speed; WWW vs internet; internet
hardware: modems, PSTN, dedicated lines, cell phone network; IP addresses: IPv4 and IPv6 format, subnetting, how an
IP address is associated with a device, public vs private (security), static vs dynamic; URL and the role of DNS.
**3.1 Computers and their components.** Need for input, output, primary memory, secondary (incl. removable)
storage; embedded systems (benefits, drawbacks); principal operations of laser printer, 3D printer, microphone,
speakers, magnetic hard disk, solid state (flash) memory, optical disc reader/writer, touchscreen, VR headset;
buffers; RAM vs ROM and their uses; SRAM vs DRAM (uses, reasons); PROM, EPROM, EEPROM; monitoring and control
systems: the difference, sensors (temperature, pressure, infra-red, sound) and actuators, feedback.
**3.2 Logic gates and logic circuits.** Symbols and functions of NOT, AND, OR, NAND, NOR, XOR (two inputs except
NOT); truth tables; construct a circuit, a truth table or a logic expression from a problem statement, a circuit,
an expression or a truth table.
**4.1 CPU architecture.** Von Neumann model and the stored program concept; registers, general vs special purpose:
PC, MDR, MAR, ACC, IX, CIR, Status Register; ALU, CU, system clock, Immediate Access Store (IAS); address, data and
control buses; performance: processor type and number of cores, bus width, clock speed, cache; ports USB, HDMI,
VGA; stages of the fetch-execute cycle in register transfer notation; interrupts: causes, applications, Interrupt
Service handling Routine (ISR), when they are detected in the F-E cycle, how they are handled.
**4.2 Assembly language.** Relationship to machine code; stages of a two-pass assembler, applied to a program;
trace a program; instruction groups: data movement, input and output, arithmetic, unconditional and conditional
jumps, compare; addressing modes: immediate, direct, indirect, indexed, relative.
**4.3 Bit manipulation.** Logical, arithmetic and cyclic shifts, left and right; bit manipulation to monitor or
control a device; test and set a bit with masks (AND, OR, XOR).
**5.1 Operating systems.** Why an OS is needed; memory, file, security, hardware (I/O, peripherals) and process
management; utilities: disk formatter, virus checker, defragmentation, disk contents analysis/repair, file
compression, back-up; program libraries and DLLs, benefits to the developer.
**5.2 Language translators.** Need for an assembler, a compiler, an interpreter; benefits and drawbacks of compiler
vs interpreter, justify each; partial compilation then interpretation (Java); IDE features: context-sensitive
prompts, dynamic syntax checks, prettyprint, expand and collapse code blocks, single stepping, breakpoints,
variables/expressions report window.
**6.1 Data security.** Security vs privacy vs integrity; security of data and of the system; measures: user
accounts, passwords, authentication (digital signatures, biometrics), firewall, anti-virus, anti-spyware,
encryption; threats: malware (virus, spyware), hackers, phishing, pharming; ways to restrict risks; protecting
data: encryption, access rights.
**6.2 Data integrity.** Validation: range, format, length, presence, existence, limit check, check digit;
verification during entry (visual check, double entry) and transfer (parity check byte and block, checksum).
**7.1 Ethics and ownership.** Ethics for computing professionals; professional bodies BCS and IEEE; acting
ethically or unethically in a situation; copyright legislation; licences: Free Software Foundation, Open Source
Initiative, shareware, commercial, justify one; AI: impact (social, economic, environmental) and applications.
**8.1 Database concepts.** Limitations of a file-based approach; how a relational database addresses them; terms:
entity, table, record, field, tuple, attribute, primary key, candidate key, secondary key, foreign key,
relationship (one-to-many, one-to-one, many-to-many), referential integrity, indexing; E-R diagrams;
normalisation 1NF, 2NF, 3NF; explain why tables are or are not in 3NF; produce a normalised design.
**8.2 DBMS.** Features that address file-based issues: data management incl. data dictionary, data modelling,
logical schema, data integrity, data security (backups, access rights for individuals/groups); developer
interface; query processor.
**8.3 DDL and DML.** DBMS uses DDL for structure and DML for queries and maintenance; SQL is the industry standard;
DDL: CREATE DATABASE, CREATE TABLE with CHARACTER, VARCHAR(n), BOOLEAN, INTEGER, REAL, DATE, TIME; ALTER TABLE;
PRIMARY KEY (field); FOREIGN KEY (field) REFERENCES Table (Field). DML on at most two tables: SELECT … FROM,
WHERE, ORDER BY, GROUP BY, INNER JOIN, SUM, COUNT, AVG; INSERT INTO, DELETE FROM, UPDATE.
**9.1 Computational thinking.** Abstraction (need, benefits, purpose, produce an abstract model); decomposition
into sub-problems leading to modules (procedure/function).
**9.2 Algorithms.** An algorithm is a sequence of defined steps; identifier names and an identifier table;
pseudocode with input, process, output; sequence, selection, iteration; document with structured English, a
flowchart or pseudocode; pseudocode from structured English or a flowchart; flowchart from structured English or
pseudocode; stepwise refinement; logic statements in a solution.
**10.1 Data types and records.** Choose types (INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE, ARRAY, FILE); purpose
of a record; define a record in pseudocode; read from and save to a record.
**10.2 Arrays.** Index, upper and lower bound; choose 1D or 2D; pseudocode for 1D and 2D arrays; bubble sort;
linear search.
**10.3 Files.** Why files are needed; pseudocode for text files of one or more lines.
**10.4 ADTs (introduction).** An ADT is data plus operations; stack, queue, linked list; key features and justify
use; add, edit and delete data (no pseudocode required for these structures); how each can be implemented with
arrays.
**11.1 Programming basics.** Pseudocode from a flowchart or structured English; constants, variables, assignment,
arithmetic and logical expressions, keyboard input, console output; built-in functions and library routines
(others will be provided; string functions always given).
**11.2 Constructs.** IF with ELSE and nested IF; CASE; count-controlled, post-condition and pre-condition loops;
justify a loop choice.
**11.3 Structured programming.** Define and use procedures (where appropriate; none, one or more parameters; by
reference or by value) and functions (used in an expression; return value replaces the call); terms: header,
interface, parameter, argument, return value; efficient pseudocode.
**12.1 Program development life cycle.** Purpose; waterfall, iterative, RAD (principles, benefits, drawbacks);
analysis, design, coding, testing, maintenance.
**12.2 Program design.** Structure charts (purpose, construct, parameters between modules, pseudocode from one);
state-transition diagrams.
**12.3 Testing and maintenance.** Exposing and avoiding faults; syntax, logic and run-time errors, locate and
correct; dry run, walkthrough, white-box, black-box, integration, alpha, beta, acceptance, stub testing; test
strategy and test plan; normal, abnormal, extreme/boundary test data; perfective, adaptive, corrective
maintenance; amend an existing program.

## Learning outcomes, A Level (Papers 3 and 4)
**13.1 User-defined data types.** Why needed; non-composite: enumerated, pointer; composite: set, record,
class/object; choose and design a type for a problem.
**13.2 File organisation and access.** Serial, sequential (key field), random (record key); sequential access for
serial and sequential files, direct access for sequential and random files; hashing algorithms to read and write
a random/sequential file.
**13.3 Floating point.** Format of binary floating-point numbers using two's complement mantissa and exponent;
effect of changing the bit allocation (range vs precision); convert to and from denary; normalise and why;
approximation; underflow and overflow; rounding errors.
**14.1 Protocols.** Why protocols are essential; protocol stack, each layer with its own function; TCP/IP four
layers (Application, Transport, Internet, Link): purpose of each, application when a message is sent between
hosts; HTTP, FTP, POP3, IMAP, SMTP, BitTorrent (peer-to-peer file sharing).
**14.2 Circuit and packet switching.** Each: benefits, drawbacks, where applicable; the router in packet switching;
how packet switching passes messages across a network including the internet.
**15.1 Processors.** RISC vs CISC; interrupt handling on each; pipelining and registers in RISC; SISD, SIMD, MISD,
MIMD; massively parallel computers; virtual machines: concept, roles, benefits, limitations.
**15.2 Boolean algebra and logic circuits.** Truth tables incl. half adder and full adder (gates may have more
than two inputs); SR and JK flip-flops: circuit, truth table, role as storage; Boolean algebra and De Morgan's
laws; simplify; Karnaugh maps (benefits, solve problems).
**16.1 OS purposes.** Maximising use of resources; how the user interface hides hardware complexity; process
management: multi-tasking, process, states running/ready/blocked; scheduling: round robin, shortest job first,
first come first served, shortest remaining time; the kernel as interrupt handler and low-level scheduling;
virtual memory, paging, segmentation, their difference, page replacement, disk thrashing.
**16.2 Translation software.** How an interpreter executes without a translated version; compilation stages:
lexical analysis, syntax analysis, code generation, optimisation; grammar in syntax diagrams or BNF; Reverse Polish
Notation for evaluating expressions.
**17.1 Encryption.** Public key, private key, plain text, cipher text, encryption, symmetric and asymmetric; sending
a private message to an individual; sending a verified message to the public; quantum cryptography (purpose,
benefits, drawbacks); SSL/TLS (purpose, client-server use, when appropriate); digital certificates (how acquired,
how used to produce digital signatures).
**18.1 AI.** Graphs in AI: purpose and structure; A* and Dijkstra searches on a graph (no algorithms to write);
artificial neural networks and machine learning; deep learning, machine learning, reinforcement learning, reasons
for each; supervised and unsupervised learning; back propagation of errors; regression methods.
**19.1 Algorithms.** Linear and binary search (write both; conditions for binary search; performance vs number of
items); insertion sort and bubble sort (write both; performance depends on initial order and number of items);
ADTs: find in a linked list and a binary tree; insert into a stack, queue, linked list, binary tree; delete from a
stack, queue, linked list; graph as an ADT (features, justify; no code); implement an ADT from another ADT or from
built-in types: stack, queue, linked list, dictionary, binary tree; compare algorithms by time and memory, Big O
for time and space complexity.
**19.2 Recursion.** Essential features; how it is expressed; write and trace recursive algorithms; when it is
beneficial; what a compiler must do (stacks and unwinding).
**20.1 Programming paradigms.** Meaning of a paradigm; low-level (addressing modes immediate, direct, indirect,
indexed, relative); imperative/procedural; OOP terms: objects, properties/attributes, methods, classes,
inheritance, polymorphism, containment (aggregation), encapsulation, getters, setters, instances; design classes
and write OOP code; declarative: write facts and rules from supplied information and code that satisfies a goal.
**20.2 File processing and exception handling.** Open (read, write, append) and close a file; read and write a
record; file operations on serial, sequential and random files; exceptions and why handling matters; when to use
it; write exception-handling code.
