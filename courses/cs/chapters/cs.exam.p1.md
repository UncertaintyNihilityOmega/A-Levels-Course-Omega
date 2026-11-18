@chapter cs.exam.p1
@title Paper 1 guide: Theory Fundamentals
@level guide
@paper CAIE 9618 Paper 1
@time 2–3 hours
@summary What Paper 1 prints and allows, how to share 90 minutes across 75 marks, the kinds of question each syllabus section produces, how to answer each command word for full marks, five model answers and a marked trace, the habits that lose marks, and a revision plan that links every Paper 1 chapter.

:::why
Paper 1 is the first AS paper and it is all theory, so the marks go to students who write exactly what a mark scheme looks for: the right term, one point per mark, tied to the scenario. Two students who know the same facts can score very differently. This guide shows what the paper looks like, how to spend the 90 minutes, and how to turn what you know into marks.
:::

## The paper at a glance

| Feature | Paper 1 |
|---|---|
| Title | Theory Fundamentals |
| Time | 1 hour 30 minutes |
| Marks | 75 |
| Syllabus content | sections 1 to 8 (data representation, communication, hardware, processor fundamentals, system software, security, ethics, databases) |
| Weighting | 50% of AS Level, 25% of A Level |
| Where you answer | on the question paper itself; no additional materials |
| Questions | answer all of them: some short, some longer |

The front page of the May/June 2025 paper (9618/11) told candidates to write in black or dark blue pen, to use an HB pencil only for diagrams, graphs or rough working, and that **calculators must not be used**. Under "Information" it said that the total is 75 marks, that the marks for each part are shown in brackets `[ ]`, and that **no marks will be awarded for using brand names of software packages or hardware**.

That paper had 20 pages and 8 questions of 4, 13, 7, 6, 13, 14, 11 and 7 marks, adding to 75. Each question was built on a scenario: a video-conference company, a shop, a furniture company's database, someone buying a computer, a banker's data. Treat that as an example of the style, not a rule: other papers have a different number of questions and different mark totals, and the topics move from series to series. What stays the same is the style: a short scenario, then parts (a), (b), (c) with the marks in brackets.

The assembly-language question **prints the instructions it uses** (opcode, operand and an explanation of each), so you never memorise the instruction set. It also prints the contents of memory for you to trace. Logic questions give you a circuit or a statement and ask for an expression or a truth table, usually with space to work in.

:::exam What the assessment objectives mean for you
Paper 1 is 60% AO1 (knowledge and understanding) and 40% AO2 (applying knowledge to a problem). The AO1 marks are the definitions, descriptions and conversions you have learned. The AO2 marks are the answers that need the scenario: "justify a topology for this school", "explain the effect on this file". Learning the facts is half the paper; using them on the scenario is the other half.
:::

## Spending 90 minutes on 75 marks

There are 90 minutes for 75 marks, so each mark is worth \(90 \div 75 = 1.2\) minutes, a little over a minute. Use that as a rule of thumb to decide how long a question deserves, and to notice when you are overspending.

| Marks | Minutes at 1.2 per mark | Round to |
|---|---|---|
| 4 | 4.8 | 5 |
| 6 | 7.2 | 7 |
| 7 | 8.4 | 8 |
| 11 | 13.2 | 13 |
| 13 | 15.6 | 16 |
| 14 | 16.8 | 17 |

The eight questions of the May/June 2025 paper would be paced at about 5, 16, 8, 7, 16, 17, 13 and 8 minutes, which add up to the full 90. In practice, plan to **finish the last question with about ten minutes left**, so you can check the work that is easy to get wrong: arithmetic, truth tables and trace tables.

:::steps
1. **First minute:** turn the pages and read the first line of every question. Pick no order yet, but see which topics are there.
2. **Answer in the order that suits you.** A question you are sure of gives marks quickly and steadies you for the rest. Number the question clearly where you answer.
3. **Never leave a gap.** A blank scores zero; a sensible attempt may score a mark. Mark schemes give no negative marks.
4. **At 10 minutes before the end,** stop starting new work. Go back to every calculation and every table and recheck it.
:::

:::tip Marks are the clock
If a 4-mark question has taken you ten minutes, you have written too much on it or you are stuck. Write what you have, put a small star by the question, and move on. Come back if time is left.
:::

## What each section tends to ask

Cambridge sets original questions every series, so no one can tell you what will appear. What can be said is what **kinds of question** each section produces. Practise each kind until the method is automatic.

| Syllabus section | Chapter | Question types to practise |
|---|---|---|
| 1 Data representation, multimedia, compression | [Number systems and binary arithmetic](#cs.data), [Images, sound and compression](#cs.media) | conversions between binary, denary, hexadecimal and BCD with working; two's complement and binary addition or subtraction with overflow; file-size estimates **without a calculator**; the effect of changing resolution, colour depth, sampling rate or sampling resolution; lossy against lossless; run-length encoding |
| 2 Communication and the internet | [Networks](#cs.networks), [The internet](#cs.internet) | justify a topology, client-server or peer-to-peer; benefits and drawbacks; what a router, switch or WAP does; IPv4 and IPv6 format; public and private addresses; the role of DNS; how streaming works |
| 3 Hardware | [Computers and their components](#cs.hardware), [Logic gates and logic circuits](#cs.logic) | "describe how a device works" as an ordered sequence; RAM, ROM, SRAM and DRAM compared; embedded, monitoring and control systems with sensors and actuators; circuit to expression to truth table, in any direction |
| 4 Processor fundamentals | [Processor fundamentals](#cs.processor), [Assembly language and bit manipulation](#cs.assembly) | registers and buses; register transfer notation for the fetch stage; interrupts; assembly traces with a memory table; masks and shifts; stages of an assembler |
| 5 System software | [System software](#cs.software) | why an operating system is needed; the five kinds of management; utilities; compiler against interpreter, justified; IDE features |
| 6 Security, privacy and integrity | [Security, privacy and data integrity](#cs.security) | name the threat, the measure and how it works; choose a validation or verification check and say what it catches; calculate a check digit or a parity bit |
| 7 Ethics and ownership | [Ethics, ownership and the impact of AI](#cs.ethics) | act ethically or unethically in a stated situation; choose and justify a licence; impact of AI |
| 8 Databases | [Databases](#cs.databases), [DBMS and SQL](#cs.sql) | limitations of files; keys and relationships; normalise a table to 3NF; a DDL or DML statement; state the output of a query |

Notice how often the verbs are *describe*, *explain*, *justify* and *complete*. The next section shows exactly what each one needs.

## Command words: what each one asks you to do

Every question starts with a command word, and the command word decides what an answer has to contain. Cambridge defines them in its syllabus. These are the meanings that matter most for Paper 1, with what each one means for an answer.

| Command word | Cambridge meaning | What the answer contains |
|---|---|---|
| **State**, **Give**, **Identify** | express in clear terms; name, select or recognise | the term or the value only, one point per mark; no explanation is needed |
| **Describe** | state the points; give the characteristics and main features | a list of facts, steps or features, each one a different correct point |
| **Explain** | set out purposes or reasons; say why and/or how, with evidence | a point **and its reason**: "because", "so that", "which means" |
| **Justify** | support a case with evidence or argument | the choice, then reasons **taken from the scenario** |
| **Complete** | add to a diagram or table | fill every blank in the layout given |
| **Calculate** | work out a numerical answer | the working, then the answer with its unit |
| **Define** | give the precise meaning | the exact meaning in one or two sentences, using the correct term |

Four more words appear often. **Outline** and **Suggest** are best answered like *Describe* (several short, different points). **Compare** and **Contrast** need both items in the same sentence: "A uses … whereas B uses …". These last four are this course's advice rather than Cambridge's definitions.

### How many points does an answer need?

A mark scheme gives **one mark per mark point**, so the number in the brackets tells you how many different correct points to write. For a 4-mark *describe* question, write at least four different points, and one or two extra if you have time, because one of your points may be marked as too vague. For a 3-mark *explain* question, write three point-and-reason pairs, or a point with two reasons if that is how the content falls.

:::warn Repeating a point does not earn a second mark
"The disk is fast. It reads quickly." is one point said twice. Before you write a sentence, ask: "Is this a new fact the examiner can tick?" If not, replace it.
:::

### Answering "justify" and other scenario questions

A *justify* or *suggest* question is AO2: it wants your knowledge applied. A general fact scores nothing unless you connect it to the scenario. Follow this pattern.

:::steps
1. **Choose** the option the question asks about (or the best one), in one short phrase.
2. **Give a feature** of that choice that matters here.
3. **Link it to the scenario** with a detail you have copied from the question: the number of users, the setting, the risk.
4. **Repeat** with a second feature, until you have one pair per mark.
:::

:::exam Use the scenario's own words
A scenario states two or three facts on purpose: "30 computers", "in a library", "the users are not computer experts", "a large number of customers". An answer that quotes one of them ("because the library has many users") shows the examiner you are answering this question and not reciting a notes page.
:::

## Calculations without a calculator

The paper says **calculators must not be used**, so every number can be done by hand. The trick is to use powers of two as the examiners do.

:::eg Estimating a file size by hand
A sports club in Quito stores a photograph as a bitmap of 1024 pixels wide and 512 pixels high with a colour depth of 16 bits. Calculate the size of the file in mebibytes. Ignore the file header. [3 marks]

Write each number as a power of two, so the sum becomes an addition of powers: \(1024 = 2^{10}\), \(512 = 2^{9}\), \(16 = 2^{4}\).

Size in bits \(= 2^{10} \times 2^{9} \times 2^{4} = 2^{23}\). [M1]

Divide by 8 (that is \(2^{3}\)) to turn bits into bytes: \(2^{23} \div 2^{3} = 2^{20}\) bytes. [M1]

A mebibyte is \(2^{20}\) bytes, so the file is **1 MiB**. [A1]
:::

The same approach works for sound. A recording at 8000 samples per second, 16 bits per sample, mono (one channel), for 30 seconds holds \(8000 \times 16 \times 30 = 3\,840\,000\) bits, and \(3\,840\,000 \div 8 = 480\,000\) bytes. Do the three multiplications in the order that gives you round numbers (here \(8000 \times 30 = 240\,000\) first), and always finish with the division by 8.

:::warn Bits and bytes
The most common lost mark in a file-size question is the missing division by 8. After the last multiplication, ask: "Is this bits or bytes?" Also use the prefix the question uses: kibi and mebi are powers of two, kilo and mega are powers of ten.
:::

Conversions work the same way: show each step. A mark scheme gives a method mark for the working and an answer mark for the result, so an answer with correct working and one slip in the arithmetic still scores. A bare wrong answer scores nothing.

## Five model answers

The answers below show what a full-mark answer looks like for the question styles that carry the most marks: *describe*, *explain*, *justify*, a trace and an SQL query. After each is the mark scheme, one `[B1]` per mark point.

:::eg Describe: a speaker
Describe how a speaker produces sound from a digital sound file. [5 marks]

A *describe* answer is a list of different facts. Follow the signal from the file to the air, naming each part. Five marks means five different correct points; there are six or more to choose from.

- The digital data is passed to a digital-to-analogue converter (DAC). [B1]
- The DAC produces a varying electrical (analogue) signal. [B1]
- The signal passes through a coil of wire that is attached to a cone and sits next to a permanent magnet. [B1]
- The changing current makes the coil an electromagnet, so it is attracted to and repelled by the permanent magnet and moves backwards and forwards. [B1]
- The coil moves the cone, which vibrates and pushes the air, producing sound waves. [B1]

(The signal being amplified, a bigger signal giving a louder sound and a faster change giving a higher pitch are also correct points. A mark scheme often lists more points than the marks available: the maximum is 5.)
:::

:::eg Explain: sampling resolution
A radio station in Nairobi records interviews. The sound engineer changes the sampling resolution from 8 bits to 16 bits. Explain the effect on the sound file. [4 marks]

An *explain* answer gives an effect and its reason. Two effects are needed (quality and size), each with a "because".

- Each sample is stored with more bits, so more levels are available. [B1]
- Each measured value is closer to the true height of the sound wave, so the digital sound is a more accurate copy of the original. [B1]
- Each sample now needs 16 bits instead of 8. [B1]
- So the file is larger, because the file size is the sampling rate × the sampling resolution × the time. [B1]

(Accept "the file is twice the size" for the third and fourth points together if the reasoning is clear. Reject "the file is bigger" with no reason: it is a statement, not an explanation.)
:::

:::eg Justify: lossless compression
A newspaper in Accra scans its old printed pages into bitmap images for a permanent archive. Each page is mostly paper-coloured background with lines of small black print. Justify the use of lossless compression, such as run-length encoding (RLE), for the archive. [4 marks]

The scenario gives three usable facts: it is an archive (permanent), the print is small, and the background is plain. A *justify* answer must use them.

- Lossless compression allows the original image to be rebuilt exactly, so no part of the page is lost from a permanent archive. [B1]
- Lossy compression would permanently remove some detail, so the small print could become unreadable. [B1]
- Large areas of the background are one colour, so there are long runs of identical pixels. [B1]
- RLE stores each run as a count and a value, so these runs take much less space and the archive needs less storage. [B1]
:::

:::eg Trace: an assembly program
The table shows the instructions used in this program. The ASCII code of the character B is 66. The program is stored from address 100, and the data it uses is stored at addresses 120 to 122. [6 marks]

| Instruction | Explanation |
|---|---|
| `LDD <address>` | Load the contents of the address into ACC |
| `ADD <address>` | Add the contents of the address to ACC |
| `SUB #n` | Subtract the denary number n from ACC |
| `STO <address>` | Store the contents of ACC at the address |
| `CMP #n` | Compare the contents of ACC with the denary number n |
| `JPN <address>` | Following a compare instruction, jump to the address if the compare was False |
| `OUT` | Output the character whose ASCII value is in ACC |
| `END` | Return control to the operating system |

```text
Address   Instruction
100       LDD 122
101       ADD 120
102       STO 122
103       LDD 121
104       SUB #1
105       STO 121
106       CMP #0
107       JPN 100
108       LDD 122
109       OUT
110       END
120       33
121       2
122       0
```

Complete the trace table. Write a value only in the cell where it changes.

A trace table has one row for each instruction executed, in the order the processor executes them. Follow the program, not the listing: `JPN 100` sends the processor back to address 100, so addresses 100 to 107 appear twice.

| Instruction address | ACC | 120 | 121 | 122 | OUTPUT |
|---|---|---|---|---|---|
| (start) | | 33 | 2 | 0 | |
| 100 | 0 | | | | |
| 101 | 33 | | | | |
| 102 | | | | 33 | |
| 103 | 2 | | | | |
| 104 | 1 | | | | |
| 105 | | | 1 | | |
| 106 | | | | | |
| 107 | | | | | |
| 100 | 33 | | | | |
| 101 | 66 | | | | |
| 102 | | | | 66 | |
| 103 | 1 | | | | |
| 104 | 0 | | | | |
| 105 | | | 0 | | |
| 106 | | | | | |
| 107 | | | | | |
| 108 | 66 | | | | |
| 109 | | | | | B |
| 110 | | | | | |

The program adds the number at 120 to the running total at 122, and counts down the value at 121. At the second `CMP #0`, ACC holds 0, so the compare is True and `JPN` does not jump. The total is \(33 \times 2 = 66\), which is output as the character with ASCII code 66.

- first pass loads 0 into ACC, then 33, and stores 33 at address 122 [B1]
- 121 becomes 1, with ACC showing 2 then 1 on the way [B1]
- the processor returns from 107 to 100 for a second pass (the instruction addresses 100 to 107 appear twice) [B1]
- on the second pass ACC becomes 66 and 66 is stored at address 122 [B1]
- 121 becomes 0, and the jump at 107 is not taken, so the next address is 108 [B1]
- 66 is loaded into ACC and the output is B [B1]
:::

:::eg Write an SQL query
A bike-hire company in Medellín stores two tables. BIKE(**BikeID**, Model, DailyRate) and HIRE(**HireID**, BikeID\*, HireDate, Days), where BikeID in HIRE is a foreign key. A small part of the data is shown.

| BikeID | Model | DailyRate |
|---|---|---|
| B1 | Andes | 9 |
| B2 | Sierra | 12 |
| B3 | Pampa | 8 |
| B4 | Coast | 10 |

| HireID | BikeID | HireDate | Days |
|---|---|---|---|
| H1 | B1 | 2026-02-27 | 3 |
| H2 | B2 | 2026-03-02 | 2 |
| H3 | B1 | 2026-03-05 | 4 |
| H4 | B3 | 2026-03-09 | 1 |
| H5 | B2 | 2026-03-15 | 5 |
| H6 | B1 | 2026-03-20 | 2 |
| H7 | B4 | 2026-02-14 | 7 |

Write an SQL query to display each model with the total number of days it was hired on or after 1 March 2026, in alphabetical order of model. State the output for the data shown. [5 marks]

The model name is in BIKE and the days are in HIRE, so the query needs a join. "Each model" signals GROUP BY, "total" signals SUM, and "on or after 1 March 2026" is a condition on single rows, so it goes in WHERE.

```text
SELECT Bike.Model, SUM(Hire.Days)
FROM Bike
INNER JOIN Hire ON Bike.BikeID = Hire.BikeID
WHERE Hire.HireDate >= '2026-03-01'
GROUP BY Bike.Model
ORDER BY Bike.Model;
```

- `SELECT` with the model and `SUM(Hire.Days)` [B1]
- `FROM Bike INNER JOIN Hire` [B1]
- `ON Bike.BikeID = Hire.BikeID` [B1]
- `WHERE` with the date condition, with the date in quotes [B1]
- `GROUP BY Bike.Model` and `ORDER BY Bike.Model` [B1]

Output (the two February hires are left out, so Coast does not appear):

| Model | SUM(Hire.Days) |
|---|---|
| Andes | 6 |
| Pampa | 1 |
| Sierra | 7 |
:::

## Common ways to lose marks

| The slip | Why it costs marks | The fix |
|---|---|---|
| A brand name ("a famous search engine", a product name) | the paper says no marks are awarded for brand names | write "a search engine", "a word processor", "a laptop computer" |
| "faster", "better", "easier", "more secure" with no reason | a comparison word is vague on its own | say what is faster and why: "faster because the switch sends frames only to the destination port" |
| a conversion with no working | the method mark is lost, and one slip then loses everything | show each division or each column |
| forgetting to divide by 8 | bits are not bytes | label every number bits or bytes |
| a truth table with missing rows | \(n\) inputs need \(2^n\) rows | write the input rows in counting order first, then fill each output column |
| wrong register names (MBR, memory register) | the registers are PC, MAR, MDR, CIR, ACC and IX | learn the six names and what each holds |
| describing when asked to explain | a list of facts has no reasons | add "because" to each point |
| saying a firewall "stops viruses" | a firewall checks network traffic; anti-virus software finds malware | name each measure with its own job |
| writing a key as a field only | a table design needs primary and foreign keys marked | underline or bold the primary key and mark each foreign key |
| not answering the scenario | a general fact is AO1 only | copy one detail from the question into each point |

## Technique check

Try these quick items before the longer practice in [Mixed practice: AS (Papers 1 and 2)](#cs.mixed.as).

:::try Technique check
Q: A Paper 1 question is worth 9 marks. About how long should it take, at the pace of this guide?
A: \(9 \times 1.2 = 10.8\) minutes, so about 11 minutes.

Q: The question says "Describe how a touchscreen detects a touch. [4 marks]". How many different correct points should the answer contain?
A: At least four, one for each mark, and one or two extra in case a point is too vague to earn credit.

Q: Improve this answer to "Justify the use of a star topology for a school with 30 computers [3 marks]": "A star is better because it is faster."
A: "Better" and "faster" are vague and have no link to the scenario. A full answer: each of the 30 computers has its own cable to the switch, so a damaged cable affects only one computer; the switch sends frames only to the destination, so there are no collisions on the 30 cables; a new computer can be added by connecting one more cable to the switch.

Q: A student adds 1011 0110 and 0000 1101 in binary and writes only the answer. Why is it risky to show no carries, and what is the correct answer?
A: A mark scheme gives a method mark for the working shown and an answer mark for the result. With no working, a wrong answer has nothing to credit; with the carries shown, a slip in one column keeps the method mark. The correct answer is 1100 0011 (\(182 + 13 = 195\)).

Q: State two things you would do in the last ten minutes of the paper.
A: Recheck every calculation (including the division by 8 in a file size) and recheck every truth table and trace table row by row; then add a point to any answer where the marks are not yet matched by points.
:::

## Revision plan

Work through the paper in four stages. Spend the most time where you lose most marks, not where you feel comfortable.

:::steps
1. **Learn:** work through each chapter below and tick its checklist. Every `:::def` card is exam wording: learn it.
2. **Practise by topic:** do the exam practice in each chapter, then the topic questions linked at the end of the chapter.
3. **Mix topics:** the real paper mixes every section. Do the "Paper 1 style" set in [Mixed practice: AS (Papers 1 and 2)](#cs.mixed.as), choosing questions in a random order.
4. **Time yourself:** do [Mock Paper 1](#cs.mock.p1) in 90 minutes, then past papers (below), then mark them against the mark scheme.
:::

The tracker below counts the checklist items you have ticked in every Paper 1 chapter.

:::progress P1
:::

## Past papers and self-marking

Real Paper 1 question papers and mark schemes are free to download. Do them under timed conditions, with a pen, and without a calculator.

- [PapaCambridge](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) keeps 9618 papers, mark schemes and inserts together (an unofficial site).
- [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-1/) sorts Paper 1 papers by series (an unofficial site).
- The [Cambridge 9618 page](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/) has the syllabus and specimen papers.

:::steps
1. **Mark with a different colour pen,** using the mark scheme, one mark point at a time. Do not mark generously.
2. **Look at the wording.** A mark scheme shows an accepted answer, and often words to reject. Learn the precise term it uses, and copy it in your next answer.
3. **Sort every lost mark** into one of three kinds: *knowledge* (you did not know it), *technique* (you knew it, but wrote it vaguely or too briefly) or *slip* (arithmetic, a missing row, a misread question).
4. **Fix each kind differently:** revise the chapter, redo the question with a model answer in mind, or add a checking step to your routine.
5. **Redo the question a week later** without the mark scheme. If you lose the same mark twice, write that point on a revision card.
:::

:::warn Do not learn old answers as scripts
Cambridge writes new questions every series. A mark scheme is useful because it shows how marks are awarded, not because the same question returns. Use past questions to practise the method.
:::

:::recap
- Paper 1: 1 hour 30 minutes, 75 marks, sections 1 to 8, answered on the paper, no calculator, no marks for brand names, HB pencil for diagrams. The May/June 2025 paper had 8 scenario questions of 4 to 14 marks.
- Pace: \(90 \div 75 = 1.2\) minutes per mark. Leave about ten minutes at the end to check calculations, truth tables and trace tables.
- One mark point per mark: *state* gives the term, *describe* gives different facts, *explain* gives point and reason, *justify* ties reasons to the scenario.
- Do file-size sums with powers of two, show every step, and divide by 8 to reach bytes.
- A trace table has one row per instruction executed and follows jumps; Paper 1 prints the instructions it uses.
- SQL: copy names exactly; join with `ON`; group "for each"; quote text and dates; one mark per clause.
- Lose fewer marks by avoiding brand names, vague words, missing working, missing truth-table rows and answers that ignore the scenario.
- Self-mark past papers with a mark scheme, and sort every lost mark as knowledge, technique or slip.
:::

:::links
- papers: [9618 past papers, mark schemes and inserts](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · every series in one place [unofficial]
- papers: [Paper 1 past papers by series](https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-1/) · Physics & Maths Tutor · Paper 1 only [unofficial]
- practise: [Data representation: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/1-information-representation/data-representation/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Logic gates and circuits: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/3-hardware-/logic-gates-and-logic-circuits/exam-questions/) · Save My Exams · circuit, expression and truth-table questions [paid]
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · a second explanation of every topic [paid]
- read: [AS summary notes](https://znotes.org/caie/as-level/computer-science-9618/) · ZNotes · free AS notes
- read: [The 9618 syllabus](https://www.cambridgeinternational.org/Images/721397-2027-2029-syllabus.pdf) · Cambridge · the command words and every learning outcome

Links checked 13 November 2026.
:::

Next: [Paper 2 guide: Problem-solving and Programming](#cs.exam.p2)
