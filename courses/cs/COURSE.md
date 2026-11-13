# COURSE: Computer Science (cs)

The rules for every chapter of this course. A Writer reads this file, kit/STYLE.md, the gold chapter and its own
packages/`Pn`.md, nothing else. Written by the Specialist (LEAD, 13 November 2026).

## Scope and board
- Cambridge International AS & A Level Computer Science **9618**, syllabus for exams in **2027, 2028 and 2029**
  (version 3, October 2026): https://www.cambridgeinternational.org/Images/721397-2027-2029-syllabus.pdf
- Pseudocode authority: the **2027–2029 Pseudocode Guide** (version 1):
  https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf. FACTS.md has its rules.
- Papers (FACTS.md has every detail): **1** Theory Fundamentals (1 h 30, 75 marks, sections 1–8), **2** Fundamental
  Problem-solving and Programming Skills (2 h, 75, sections 9–12, answers in pseudocode, an insert of functions),
  **3** Advanced Theory (1 h 30, 75, sections 13–20), **4** Practical (2 h 30, 75, sections 19–20 except low-level and
  declarative, on a computer, Python/Java/VB.NET, evidence document). **No calculator in any paper.**
- The course: 49 chapters in course.json order. Start here (map, programming from zero) → AS theory (P1) → AS
  programming (P2) → A Level theory (P3) → A Level programming (P3 and P4) → Python for Paper 4 → paper guides,
  mixed practice, mocks.
- Students are complete beginners: many have never programmed. [Programming from zero](#cs.f.basics) teaches
  Python and pseudocode from nothing; every later chapter assumes only earlier chapters.

## Code in this course (the most important rules)
- **Two languages, always labelled.** Cambridge pseudocode (exactly as the 2027–2029 guide writes it) and
  **Python 3** (the Paper 4 language this course teaches; Java and VB.NET are not taught). The page shows code
  blocks without a language label, so the sentence before every block says which it is ("In pseudocode:",
  "The same in Python:", "Output:").
- Fenced blocks: ` ```pseudocode `, ` ```python `, ` ```output ` (what a program prints) and ` ```text ` (anything
  else: a file's contents, a console with typed input). Never put marks, maths or `:::` lines inside a fence.
  Fences work inside `:::eg` and inside `:::try` answers (blank line before and after the fence).
- **Pseudocode style** (FACTS.md "Pseudocode conventions"): keywords in capitals; identifiers in PascalCase
  (`TotalScore`, `Index`); indent 3 spaces; `←` for assignment (type the character ←, never `<-`); `=` in
  `CONSTANT Rate = 0.2` only; `DECLARE X : INTEGER`; `ARRAY[1:30] OF STRING`; `NEXT Index` repeats the identifier;
  `ENDIF`, `ENDWHILE`, `ENDCASE`, `ENDPROCEDURE`, `ENDFUNCTION`, `ENDTYPE`, `ENDCLASS` as one word; `CALL` for
  procedures, never for functions; `//` comments; `OUTPUT "Total: ", Total`; REAL literals with a digit on both
  sides of the point (`0.0`, `4.5`); CHAR in single quotes; STRING in double quotes. Arrays start at 1 unless the
  question says otherwise. String functions follow the Paper 2 insert: `LEFT`, `RIGHT`, `MID(S, Start, Length)`,
  `LENGTH`, `TO_UPPER`, `TO_LOWER`, `NUM_TO_STR`, `STR_TO_NUM`, `IS_NUM`, `ASC`, `CHR`, `INT`, `RAND`, `MOD`,
  `DIV`, `&`, `EOF`; a question that needs any other function defines it in the question.
- **Python style**: Python 3.12+, standard library only, PEP 8 spacing, no f-string tricks a beginner cannot read
  (simple f-strings are fine). Names in snake_case (`total_score`) unless the example mirrors a Paper 4 task, where
  the task's names are kept (`HeadPointer`, `Queue`). A record is a class with an `__init__` (as Paper 4 allows);
  arrays are lists; a Cambridge array `[1:n]` becomes a Python list of n items with index i − 1, or a list of n + 1
  with element 0 unused: say which. Show input with `input()` only when the example needs it.
- **Every Python block runs.** `checks/<id>.py` reads the chapter, runs every ` ```python ` block in order (each in
  a fresh namespace, inside a temporary folder so file examples work), and asserts that its output equals the
  ` ```output ` block that follows it, if there is one. Input: the check supplies the typed values and echoes them,
  so an output block shows the console exactly as a user sees it. The gold chapter's checks file has the helper:
  copy it unchanged.
- **Every pseudocode algorithm is checked too**: the checks file translates it into Python and asserts every value
  the chapter states (outputs, trace-table rows, final array contents, counts of comparisons or swaps).
- Trace tables are Markdown tables: one column per variable (plus OUTPUT), one row per change, blank cells where
  nothing changes, as Cambridge prints them.
- Assembly (cs.assembly, cs.paradigms): only the instruction set in FACTS.md, in ` ```text ` blocks, with the
  table of the instructions used printed in the question (as Paper 1 does).
- SQL in ` ```text ` blocks, keywords in capitals, one clause per line; only the statements FACTS.md lists.
- Logic: write expressions as `X = (A AND B) OR NOT C` in text, and in maths only for Boolean algebra at A Level
  (\(\overline{A}\) is not allowed by the kit: write \(\text{NOT } A\) or \(A'\) and say which; this course uses
  `NOT A` everywhere, and \(A \cdot B\), \(A + B\) only inside the cs.boolean algebra sections).

## Data values and conventions
- Binary prefixes: kibi = 2¹⁰ = 1024, mebi = 2²⁰, gibi = 2³⁰, tebi = 2⁴⁰ (KiB, MiB, GiB, TiB); decimal kilo = 10³,
  mega = 10⁶, giga = 10⁹, tera = 10¹². 1 byte = 8 bits. Use the prefix the question uses.
- Bitmap size = width × height × colour depth (bits), ÷ 8 for bytes; sound size = sample rate × resolution ×
  seconds (× channels), ÷ 8 for bytes. Ignore the header unless told otherwise; say so.
- Hex digits in capitals (`4A`); Cambridge assembly prefixes `#` denary, `B` binary, `&` hex.
- No calculator: every exam-style calculation uses numbers a student can do by hand (powers of 2, small products).
- Dates DD/MM/YYYY in pseudocode, as the insert assumes.
- Numbers in chapters follow the kit rules (checks recompute them); computing answers are usually exact, so give
  exact values, not 3 s.f.

## Depth and tone
- Depth of the finished Maths and Physics courses: a topic chapter is long (typically 6,000–10,000 words), builds
  from zero to full exam depth, and has every kit/STYLE.md section. The gold chapter is the model.
- Mark schemes in this course: Cambridge CS mark schemes award one mark per **mark point**. Write `[B1]` for each
  mark point (theory and pseudocode), `[M1]`/`[A1]` only where a method mark really controls an answer mark (a
  calculation). For "write pseudocode/program code" answers: the full model answer in a fence, then a bullet list
  of the mark points, one `[B1]` each, then any "accept/reject" notes in round brackets.
- Theory answers: one point per mark, the precise term first ("The **MAR** holds the address …"). Use the command
  words as Cambridge defines them (FACTS.md): "Describe" gives characteristics, "Explain" gives reasons,
  "Justify" supports a choice with evidence from the scenario.
- Never use brand names of software or hardware in answers (Papers 1–3 award no marks for them): "a word
  processor", not a product name. Python itself is fine (it is the programming language).
- Scenarios are realistic and international (a school in Lagos, a clinic in Lahore, a bus company in Lima), with
  plain names and no stereotypes.

## Course rules
- Every topic chapter: `:::why`, warm-up, `:::def` cards in exam wording, `:::key` boxes for rules and algorithm
  templates, worked examples (at least one exam-style with marks), Spot the error, try questions, Exam practice ★
  to ★★★ (6–8), Stretch for A* (1–2), quiz (6+), checklist (one line per learning outcome in FACTS.md), recap,
  `:::links`, `Next:`.
- AS chapters use only AS terms; A Level material is labelled "(A Level)" and comes last.
- Exam-style questions are original and in Cambridge's style: a short scenario, then parts (a), (b) … with marks.
  Paper 2 questions refer to "the insert" for functions; never tell students to look anything else up.
- Paper guides point to real past papers (links below); never copy or paraphrase a real question.
- Practice questions never reuse a worked example's data or scenario.

## Board box rule
`:::board` only with one board and one difference you are sure of; most chapters have none. Sure facts:
- AQA A Level Computer Science (7517): Paper 1 is an on-screen exam that uses a skeleton program released before the
  exam; there is a non-exam assessment programming project.
- OCR A Level Computer Science (H446): a non-exam assessment programming project is part of the qualification.
Cambridge 9618 has no coursework: programming is tested by Paper 2 (pseudocode on paper) and Paper 4 (on a
computer in the exam).

## Widgets (one package each; course.json "packages" lists them)
cs-binary (P2), cs-ip (P3), cs-logic (P4), cs-asm (P5), cs-check (P6), cs-sql (P7), cs-trace (P8), cs-stack (P9),
cs-float (P11), cs-pipeline (P12), cs-kmap and cs-sched (P13), cs-rpn (P14), cs-path (P15), cs-sort (P16),
cs-calls (P17). A later chapter may use an earlier package's widget. Specs are in the package files.

## Gold chapter
**cs.datatypes** (Data types, records and arrays): read it before writing. It shows the code-block rules, the
mark-point style, trace tables, Spot the error with code, and the checks file that runs every Python block.

## Packages
P1 map and programming from zero · P2 number systems, media · P3 networks, internet · P4 hardware, logic gates ·
P5 processor, assembly · P6 system software, security, ethics · P7 databases, SQL · P8 algorithms, constructs ·
P9 arrays (gold), procedures, files and first ADTs · P10 development, testing · P11 user-defined types, floating
point · P12 protocols, processors · P13 Boolean algebra, OS · P14 translators, encryption · P15 AI ·
P16 searching, sorting, ADTs · P17 recursion, OOP · P18 paradigms, file processing, Python for Paper 4 ·
P19 AS guides and mixed practice · P20 A Level guides and mixed practice · P21 Mocks 1 and 2 · P22 Mocks 3 and 4.

## Verified links for `:::links`
Use only these (each answered 200). Mark [paid] and [unofficial] as shown.

Topic questions (Save My Exams, CIE 9618, by syllabus topic; [paid]; base
`https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/` + the path, all checked):
`1-information-representation/data-representation/exam-questions/` ·
`1-information-representation/multimedia/exam-questions/` · `1-information-representation/compression/exam-questions/` ·
`2-communication-/networks-and-the-internet/exam-questions/` · `3-hardware-/computers-and-components/exam-questions/` ·
`3-hardware-/logic-gates-and-logic-circuits/exam-questions/` ·
`4-processor-fundamentals-/central-processing-unit-cpu-architecture/exam-questions/` ·
`4-processor-fundamentals-/assembly-language-/exam-questions/` · `4-processor-fundamentals-/bit-manipulation/exam-questions/` ·
`5-system-software-/operating-systems/exam-questions/` · `5-system-software-/language-translators/exam-questions/` ·
`6-security-privacy-and-data-integrity-/data-security/exam-questions/` ·
`6-security-privacy-and-data-integrity-/data-integrity/exam-questions/` ·
`10-data-types-and-structures-/data-types-and-records/exam-questions/` · `10-data-types-and-structures-/arrays/exam-questions/` ·
`10-data-types-and-structures-/files/exam-questions/` ·
`10-data-types-and-structures-/introduction-to-abstract-data-types-adt/exam-questions/` ·
`11-programming-/programming-basics/exam-questions/` · `11-programming-/constructs/exam-questions/` ·
`11-programming-/structured-programming/exam-questions/` ·
`12-software-development-/program-development-life-cycle/exam-questions/` ·
`12-software-development-/program-design-/exam-questions/` ·
`12-software-development-/program-testing-and-maintenance/exam-questions/` ·
`13-data-representation-/user-defined-data-types/exam-questions/` ·
`13-data-representation-/file-organisation-and-access-/exam-questions/` ·
`13-data-representation-/floating-point-numbers-representation-and-manipulation/exam-questions/` ·
`14-communication-and-internet-technologies-/protocols/exam-questions/` ·
`14-communication-and-internet-technologies-/circuit-switching-packet-switching/exam-questions/` ·
`15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/exam-questions/` ·
`15-hardware-and-virtual-machines-/boolean-algebra-and-logic-circuits/exam-questions/` ·
`16-system-software-/purposes-of-an-operating-system-os/exam-questions/` ·
`16-system-software-/translation-software/exam-questions/` ·
`17-security-/encryption-encryption-protocols-and-digital-certificates/exam-questions/` ·
`18-artificial-intelligence-ai-/artificial-intelligence-ai/exam-questions/` ·
`19-computational-thinking-and-problem-solving-/algorithms/exam-questions/` ·
`19-computational-thinking-and-problem-solving-/recursion/exam-questions/` ·
`20-further-programming-/programming-paradigms/exam-questions/` ·
`20-further-programming-/object-oriented-programming/exam-questions/` ·
`20-further-programming-/file-processing-and-exception-handling/exam-questions/`
(No Save My Exams topic page exists for 7 Ethics, 8 Databases or 9 Algorithm design; use the others below.)

Read, watch, explore, practise:
- read: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/ · Save My Exams · 9618 revision notes [paid]
- read: https://znotes.org/caie/as-level/computer-science-9618/ · ZNotes · free 9618 AS summary notes
- read: https://adacomputerscience.org/ · Ada Computer Science · free topic explanations and questions (written for UK boards)
- read: https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf · Cambridge · the official pseudocode guide
- read: https://www.cambridgeinternational.org/Images/721397-2027-2029-syllabus.pdf · Cambridge · the syllabus
- read: https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/ · Cambridge · the 9618 page (syllabus, guide, specimen papers)
- read: https://docs.python.org/3/tutorial/ · Python.org · the official tutorial; also `…/tutorial/controlflow.html`,
  `…/tutorial/datastructures.html`, `…/tutorial/inputoutput.html`, `…/tutorial/errors.html`, `…/tutorial/classes.html`
- read: https://www.w3schools.com/python/ · W3Schools · short Python lessons with try-it boxes; also
  `…/python/python_lists.asp`, `python_strings.asp`, `python_functions.asp`, `python_classes.asp`,
  `python_file_handling.asp`, `python_try_except.asp`
- read: https://www.w3schools.com/sql/ · W3Schools · SQL lessons; also `…/sql/sql_join_inner.asp`, `…/sql/sql_groupby.asp`
- read: https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL · MDN · what a URL is
- read: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview · MDN · how HTTP works
- read: https://www.khanacademy.org/computing/computers-and-internet · Khan Academy · bits, the internet, security (free)
- read: https://www.khanacademy.org/computing/computer-science/algorithms · Khan Academy · searching, sorting, recursion
- read: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search · Khan Academy · binary search step by step
- read: https://www.khanacademy.org/computing/computer-science/cryptography · Khan Academy · ciphers to public keys
- read: https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/ · GeeksforGeeks · bubble sort in several languages
- read: https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/ · GeeksforGeeks · insertion sort
- read: https://home.unicode.org/ · Unicode Consortium · what Unicode is
- read: https://www.bcs.org/ · BCS · the professional body for IT (ethics chapter)
- read: https://opensource.org/licenses · Open Source Initiative · the approved open-source licences
- read: https://ico.org.uk/for-organisations/ · ICO (UK) · data protection guidance, an example of a regulator
- explore: https://pythontutor.com/visualize.html · Python Tutor · run Python line by line and watch every variable
- explore: https://visualgo.net/en/sorting · VisuAlgo · animated sorts; also `…/en/list` (stacks, queues, linked lists),
  `…/en/bst`, `…/en/hashtable`, `…/en/recursion`, `…/en/graphds`, `…/en/sssp` (shortest paths)
- explore: https://www.cs.usfca.edu/~galles/visualization/Algorithms.html · USF · data-structure animations
- explore: https://logic.ly/demo/ · Logicly · build logic circuits in the browser
- explore: https://www.101computing.net/logic-gates-circuits/ · 101 Computing · logic gate challenges
- explore: https://www.101computing.net/binary-converter/ · 101 Computing · binary conversion practice
- explore: https://www.101computing.net/floating-point-binary-converter/ · 101 Computing · floating point converter
- explore: https://www.101computing.net/lmc-simulator/ · 101 Computing · a little-man computer to step through
- explore: https://www.101computing.net/reverse-polish-notation/ · 101 Computing · RPN and stacks
- explore: https://www.101computing.net/dijkstras-shortest-path-algorithm/ · 101 Computing · Dijkstra worked through
- explore: https://www.101computing.net/a-star-search-algorithm/ · 101 Computing · A* worked through
- explore: https://playground.tensorflow.org/ · TensorFlow Playground · train a small neural network in the browser
- explore: https://swish.swi-prolog.org/ · SWISH · run Prolog facts and rules online (declarative programming)
- explore: https://www.nand2tetris.org/ · Nand2Tetris · build a computer from NAND gates (stretch)
- practise: https://sqlbolt.com/ · SQLBolt · interactive SQL lessons and exercises
- practise: https://exercism.org/tracks/python · Exercism · free Python exercises with feedback
- practise: https://cs50.harvard.edu/x/ · Harvard CS50 · free introductory course with problem sets
- watch: https://www.youtube.com/@Computerphile · Computerphile · short videos by university computer scientists
- watch: https://www.youtube.com/@craigndave · Craig 'n' Dave · A Level topic videos (UK boards; content overlaps 9618)
- watch: https://www.youtube.com/watch?v=aircAruvnKk · 3Blue1Brown · "But what is a neural network?"
- watch: https://www.3blue1brown.com/lessons/neural-networks · 3Blue1Brown · the neural network lesson series
- papers: https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618 · PapaCambridge · 9618 past papers, mark schemes and inserts [unofficial]
- papers: https://www.physicsandmathstutor.com/past-papers/a-level-computer-science/caie-paper-1/ (also `caie-paper-2/`,
  `caie-paper-3/`, `caie-paper-4/`) · Physics & Maths Tutor · 9618 past papers by paper [unofficial]

Links checked 13 November 2026.
