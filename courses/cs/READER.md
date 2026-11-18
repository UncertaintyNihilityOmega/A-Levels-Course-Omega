# READER: Computer Science

## cs.overview
Taught: the four 9618 papers (times, marks, how answered), AS vs A Level, the topic map by chapter, assessment objectives AO1-AO3, command words (State, Identify, Describe, Explain, Justify, Complete, Write, Draw), the study order.
Assumed: nothing (a few terms are only named: pseudocode, trace table, cache, MAR).

## cs.f.basics
Taught: program, algorithm, input-process-output, source code, interpreter, sequence/selection/iteration, pseudocode, OUTPUT/print, strings and quotes, comments (// and #), variable, assignment (← and =), DECLARE, constant, data types INTEGER/REAL/STRING/BOOLEAN, int()/float()/str(), + - * / DIV MOD (// %), operator order and brackets, INPUT/input(), comparisons (= <> and == !=), AND OR NOT, IF/ELSE/ENDIF and elif, FOR/WHILE/REPEAT-UNTIL and range, running total, infinite loop, LENGTH/MID/& and len/slice/upper, syntax/run-time/logic errors, reading a Python error, trace table, random numbers (RAND, randint).
Assumed: nothing.

## cs.data
Taught: bit, byte, nibble, 2^n patterns, MSB/LSB, place values, KiB/MiB/GiB/TiB and kB/MB/GB/TB, binary-denary and denary-binary (place values and repeated division), hexadecimal and its uses, BCD, one's and two's complement, range of n-bit two's complement, binary addition, subtraction by adding the two's complement, overflow (signed and unsigned), ASCII/extended ASCII/Unicode, character codes in order.
Assumed: functions (def/return), bitwise &, list comprehensions and .encode (Python blocks); register, MAC address, memory address, assembly language and ASC (named in passing).

## cs.media
Taught: bitmap, pixel, colour depth, image and screen resolution, file header, bitmap size = width x height x depth, effects of changing them, vector graphic (drawing object, property, drawing list) and when to use it, analogue/digital, sampling, sampling rate and resolution, sound size, lossless vs lossy, RLE, dictionary compression.
Assumed: mono/stereo/channels, bandwidth, streaming (used undefined); Python def, lists of lists and tuple unpacking (code blocks).

## cs.networks
Taught: network, LAN/WAN, client-server and peer-to-peer, thin/thick client, topology, bus/star/mesh/hybrid (and how a frame travels), frame vs packet, links in a full mesh, transmission media (copper, fibre, radio, microwave, satellite), bandwidth, NIC/WNIC/MAC address, switch (learning table), WAP, bridge, repeater, router, default gateway, Ethernet, collision, CSMA/CD, CSMA/CA, cloud computing (public/private).
Assumed: CALL and procedures (CSMA/CD pseudocode); f-strings, list comprehensions, tuples and sorted(key=) (code blocks); IP address and routing table (used in the topology section before the router section).

## cs.internet
Taught: internet vs World Wide Web, ISP, modem, PSTN, dedicated line, cell phone network, bit streaming (real-time vs on-demand), buffer, bit rate and Mbps vs MB, IPv4 and IPv6 (validity, shortening with ::), network and host part, subnet mask and prefix, network address (AND), broadcast address, usable hosts 2^h - 2, same-subnet test, subnetting, public and private addresses, NAT, static and dynamic addresses, DHCP, URL parts, DNS lookup (resolver, cache).
Assumed: arrays (Octets[Index] in the pseudocode); functions, split/join and the ipaddress module (code blocks); what a broadcast is at first use; firewall (named).

## cs.hardware
Taught: input/output devices, primary memory vs secondary storage, removable storage, laser printer, 3D printer, speaker, VR headset, microphone, capacitive/resistive/infra-red touchscreens, hard disk (platters, tracks, sectors, seek time, latency), flash/SSD (floating gate, wear levelling), optical disc (pits and lands), choosing storage, buffer and its size, RAM/ROM, volatile, bootstrap, firmware, SRAM/DRAM, PROM/EPROM/EEPROM, embedded system, sensor, actuator, ADC/DAC, monitoring vs control system, feedback, two-limit control loop.
Assumed: flip-flop and cache (used in the SRAM definition), BIOS, relay; CALL and function calls (pseudocode loop); f-string format specs (Python).

## cs.logic
Taught: logic gate, truth table, logic expression, NOT/AND/OR/NAND/NOR/XOR (symbols, rules, tables, the circle means NOT), 2^n rows in binary counting order, working columns, bracket rules for expressions (NOT applies to the next item only), evaluating an expression, expression to circuit and circuit to expression (label the wires), junction dot vs crossing wires, problem statement to gates ("neither ... nor" = NOR), truth table to expression (one AND term per row where X = 1, joined with OR), half adder (Sum = XOR, Carry = AND), NAND-only gates.
Assumed: Python def/return and f-string alignment (:<4) in the gates program; the title "Data representation" for cs.data in Before you start; "sum of products" (named, never glossed).

## cs.processor
Taught: stored program concept, Von Neumann model, CPU/IAS/I-O, ALU, control unit, system clock and Hz, registers (PC, MAR, MDR, CIR, ACC, IX, status register), general vs special purpose, address/data/control bus and bus width (2^n addresses), performance factors (clock speed, cores, bus width, cache, processor type), USB/HDMI/VGA, fetch-execute cycle, register transfer notation ([PC], [[MAR]], ←), fetch stage, decode (opcode/operand), execute stage of LDM/LDD/ADD/STO/JMP/CMP/JPE, interrupt, ISR, when interrupts are detected, priority, saving and restoring registers.
Assumed: compiler (named in the stored program paragraph); indexed addressing and conditional jump (named in the IX and SR definitions, taught next chapter); stack (interrupt step 4); single-threaded program; buses (used in the Von Neumann definition before the Buses section); [[MAR]] on the left of the arrow (STO row); command words Evaluate and Show that.

## cs.assembly
Taught: machine code, opcode and operand, mnemonic, assembly language, assembler, 16-bit instruction layout (6-bit opcode, 10-bit operand), the instruction set (LDM, LDD, LDI, LDX, LDR, MOV, STO, ADD, SUB, INC, DEC, JMP, CMP, CMI, JPE, JPN, IN, OUT, END, AND, OR, XOR, LSL, LSR), #n / Bn / &n, labels, five instruction groups, five addressing modes, tracing with a trace table (incl. loops, compare and jump, IN/OUT with ASCII, indexed loop with a sentinel), writing short programs, two-pass assembler and symbol table, logical/arithmetic/cyclic shifts (multiply and divide by powers of 2), masks (AND tests and clears, OR sets, XOR toggles), bit 0 is the rightmost bit, monitoring and controlling a device byte.
Assumed: compiler (compared with the assembler before it is taught); "8 bits per memory location" in the machine note against 16-bit instructions and 10-bit addresses; Bn and &n used in the instruction table before the notation rules; "status register" used for a memory byte in the device example (the processor chapter taught it as a CPU register); comments (Pass 1 step 2, never shown).

## cs.software
Taught: system software vs application software, operating system and why it is needed, the five management tasks (memory, process with multitasking and time slices, file, security, hardware with device drivers), utility software (formatter, virus checker, defragmentation, disk contents analysis and repair, file compression, back-up full/incremental), program library, static vs dynamic linking, DLL, source code and object code, assembler, compiler, interpreter and their benefits/drawbacks, bytecode and virtual machine, IDE features (context-sensitive prompts, dynamic syntax check, prettyprint, expand/collapse, single stepping, breakpoint, report window).
Assumed: Python import and module.function calls, enumerate and the letter F for a free sector in the defragmentation program; list indexing from 0 and range(a, b) in the IDE examples; def/return and list comprehension in the code blocks.

## cs.security
Taught: data security vs privacy vs integrity, hacker, malware, virus, spyware, phishing, pharming, user account and password, authentication (know/have/are), biometrics, digital signature (named), firewall, anti-virus and anti-spyware, encryption (plaintext, ciphertext, key), access rights, validation vs verification, validation checks (range, limit, length, presence, format, existence, check digit), modulo-11 check digit (and modulo 10), visual check and double entry, parity bit (even/odd), block parity and locating an error, checksum (total mod 256), what each method can and cannot detect.
Assumed: the insert and the functions ASC, STR_TO_NUM, NUM_TO_STR, IS_NUM and single-quote characters in the pseudocode; ARRAY declarations and the linear search "from cs.datatypes" (a later chapter) in the existence check; ord/chr, format(..., "07b"), .count, nested lists and the one-line "x if c else y" in the code blocks; def/return.

## cs.ethics
Taught: ethics vs law, why professionals carry extra responsibility, principles of a professional code, BCS and IEEE and what professional bodies do, judging a scenario (action, who is affected, principle, impact), copyright and why it is needed, software piracy, licences (free software and copyleft, open source, shareware, commercial, freeware), choosing a licence, AI applications, social/economic/environmental impact of AI, bias.
Assumed: command word Discuss (used without definition); "trained on data" (only gestured at; machine learning is a later chapter).

## cs.databases
Taught: file-based approach and its limitations (redundancy, inconsistency, data dependence, security, integrity, new questions), update/insertion/deletion anomalies, relational database, entity, table, record (tuple), field (attribute), primary/composite/candidate/secondary/foreign keys, table design notation, 1:1, 1:M, M:M and the link table, entity-relationship diagram (crow's foot), referential integrity and orphan records, index (benefit and cost), dependency, normalisation 1NF/2NF/3NF with a worked example, DBMS features (data management, data modelling, integrity, security), data dictionary, logical schema, developer interface, query processor.
Assumed: record and field (Before you start and Warm-up point to cs.datatypes, which comes later in the course); DBMS and SQL used before the DBMS section; VARCHAR and CHARACTER in the data dictionary table; atomic (Try answer); command word Evaluate.
