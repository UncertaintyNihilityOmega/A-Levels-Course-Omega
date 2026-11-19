@chapter cs.translators
@title Compilers, BNF and Reverse Polish notation
@level a2
@paper CAIE 9618 Paper 3
@time 5–7 hours
@summary How an interpreter runs a program without producing a translated copy, the four stages of compilation (lexical analysis, syntax analysis, code generation and optimisation), how a language's grammar is written in BNF and syntax diagrams, and how Reverse Polish notation lets a stack evaluate an expression.

:::why
Every program you have ever run was translated first, and the translator is itself a program written by people who had to decide exactly what a legal program looks like. Paper 3 asks you to describe the stages a compiler goes through, to write and check a grammar in BNF, and to convert and evaluate expressions in Reverse Polish notation. These are small, precise skills, and they are among the most mechanical marks on the paper once you know the method.
:::

**Before you start**, you should know what an assembler, a compiler and an interpreter are from [System software: operating systems and translators](#cs.software), how a stack works from [Text files, stacks, queues and linked lists](#cs.structures), and the assembly instructions in [Assembly language and bit manipulation](#cs.assembly).

:::try Warm-up
Q: A program has a mistake in its last line. Which kind of translator, a compiler or an interpreter, reports it only after translating the whole program? (from [System software: operating systems and translators](#cs.software))
A: A compiler. It translates the whole program and then reports its errors. An interpreter has already run the earlier lines when it reaches the mistake.
Q: Start with an empty stack. Push 4, push 9, pop, push 2, pop. Which values are popped, in order, and what is left? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: 9 is popped first, then 2. The value 4 is left, because a stack gives back the most recent value first.
Q: What is the value of `3 + 4 * 2`, and which operator is applied first? (from [Programming from zero: Python and pseudocode](#cs.f.basics))
A: The value is 11. The `*` is applied first, because multiplication has higher precedence than addition: \(4 \times 2 = 8\), then \(3 + 8 = 11\).
:::

## How an interpreter runs a program

You already know that a translator turns source code into something a processor can run. A **compiler** does that for the whole program before it runs. An **interpreter** works differently, and Paper 3 asks you to describe exactly how.

:::def Interpretation
Running a program by taking its source code one statement at a time, analysing each statement and executing it immediately, so that no translated (object code) version of the program is ever produced.
:::

An interpreter never writes an object code file. The source code is the only thing it holds, and the interpreter program must be present on the computer every time the program runs.

:::key The interpreter cycle
1. Read the next statement of the source code.
2. Analyse it: check that it follows the rules of the language and work out what it asks for.
3. Execute it at once, by running a routine that is already part of the interpreter and does what that kind of statement means.
4. Go to the next statement (a loop or a selection decides which one) and repeat, until the program ends or an error is found.
5. If a statement breaks the rules, report the error and stop.
:::

Two consequences follow, and both are exam material.

- **Errors are reported only when the interpreter reaches them.** Statements before a mistake have already run and may already have produced output.
- **A statement inside a loop is analysed again on every pass**, because the interpreter keeps no translated copy. This is a main reason interpreted programs run more slowly.

The Python program below is a tiny interpreter for a made-up language with three commands: `SET` gives a variable a value, `ADD` adds to a variable and `PRINT` displays it. The loop is the interpreter cycle. Line 4 of the program uses a variable that was never set.

A note on the Python (an optional check, not examined here). `variables = {}` makes a **dictionary**, which pairs a name with a value, so `variables["Total"] = 10` stores 10 under the name `Total` and `variables["Total"]` looks it up again. Looking up a name that is not in the dictionary raises a `KeyError`, and `try: ... except KeyError:` catches that error and runs a different piece of code instead of stopping the program. `enumerate(program, start=1)` hands the loop each line together with its line number, counting from 1.

```python
program = [
    "SET Total 10",
    "ADD Total 5",
    "PRINT Total",
    "ADD Count 1",
    "PRINT Total",
]
variables = {}


def execute(line):
    parts = line.split()
    if parts[0] == "SET":
        variables[parts[1]] = int(parts[2])
    elif parts[0] == "ADD":
        variables[parts[1]] = variables[parts[1]] + int(parts[2])
    elif parts[0] == "PRINT":
        print(variables[parts[1]])


for number, line in enumerate(program, start=1):
    try:
        execute(line)
    except KeyError:
        print(f"Error on line {number}: the variable in '{line}' has no value")
        break
```

Output:

```output
15
Error on line 4: the variable in 'ADD Count 1' has no value
```

Lines 1 to 3 ran, and `15` was displayed before the error was found. Line 5 never ran. A compiler would have reported the problem before running anything.

:::eg Interpreter or compiler: what happens at the error? (exam style)
A program of 200 lines has a mistake in line 150: it uses a command that does not exist. Describe what happens when the program is run (a) using an interpreter and (b) after being compiled. [4 marks]

For each translator say what is done with lines 1 to 149 and what happens at the mistake.

(a) Interpreter
- Statements 1 to 149 are analysed and executed one at a time, so any output they produce appears. [B1]
- When line 150 is reached the error is reported and the program stops. [B1]

(b) Compiler
- The whole program is analysed before anything is run, so the mistake in line 150 is reported at the start and none of the program runs. [B1]
- No object code is produced until the mistake is corrected and the program is compiled again. [B1]
:::

## The stages of compilation

A compiler does not translate in one jump. It passes the program through stages, and each stage takes the output of the one before. Cambridge names four, in this order.

| Stage | Takes in | Produces | Errors it finds |
|---|---|---|---|
| Lexical analysis | the source code, as text | a list of tokens and a symbol table | illegal symbols, badly formed names |
| Syntax analysis | the tokens | a parse tree (or a report of an error) | statements that break the grammar |
| Code generation | the checked program and the symbol table | object code | few; it assumes the program is correct |
| Optimisation | the object code | better object code | none |

### Lexical analysis

The source code is only a long string of characters. The first stage turns it into the pieces that later stages can work with.

:::def Lexical analysis
The first stage of compilation. It removes white space (spaces, tabs and blank lines) and comments from the source code, splits what is left into tokens, and builds the symbol table.
:::

:::def Token
The smallest meaningful unit of a program, such as a keyword, an identifier, a constant, an operator or a bracket. Lexical analysis replaces the characters of the source code with a list of tokens.
:::

:::def Symbol table
A table built during compilation that records every identifier in the program (variables, constants, procedures and functions) with details such as its data type and, later, the memory address it is given.
:::

The lexical analyser reads characters until it has recognised one token, then starts on the next. It looks each word up in a **keyword table**, the fixed list of words that have a special meaning in the language (`IF`, `THEN`, `OUTPUT`). A word found in that table becomes a keyword token. A word that is not in it, and is allowed as a name, is an identifier: it becomes an identifier token and is added to the symbol table if it is not there already.

Take the line `IF Mark >= 50 THEN   // a pass`. The comment and the spaces are discarded and five tokens remain.

| Characters | Token type |
|---|---|
| `IF` | keyword |
| `Mark` | identifier (entered in the symbol table) |
| `>=` | operator |
| `50` | constant (a number) |
| `THEN` | keyword |

Here is the same job in Python. The function uses a pattern to recognise numbers, words and operators, and builds the symbol table as it goes. The third line of source code contains a character the language does not allow.

A note on the Python (an optional check, not examined here). `symbol_table` is a dictionary, a pairing of a name with a value, and `symbol_table.setdefault(name, ...)` adds the name only if it is not already there. `TOKEN` is a **regular expression**: a compact rule written as text for "a number, or a word, or an operator". `re.compile` prepares it, `match.lastgroup` says which of the three alternatives matched (`number`, `word` or `operator`), and the details of the pattern are not examined.

```python
import re

KEYWORDS = {"IF", "THEN", "ELSE", "ENDIF", "OUTPUT"}
TOKEN = re.compile(r"\s*(?:(?P<number>\d+)|(?P<word>[A-Za-z][A-Za-z0-9]*)|(?P<operator>(?:>=|<=|<>|[-+*/=<>()])))")


def tokenise(line, symbol_table):
    line = line.split("//")[0].rstrip()
    tokens = []
    position = 0
    while position < len(line):
        match = TOKEN.match(line, position)
        if match is None:
            bad = line[position:].lstrip()[0]
            raise ValueError(f"lexical error: '{bad}' is not allowed")
        kind = match.lastgroup
        text = match.group(kind)
        if kind == "word":
            if text in KEYWORDS:
                kind = "keyword"
            else:
                kind = "identifier"
                symbol_table.setdefault(text, len(symbol_table) + 1)
        tokens.append((kind, text))
        position = match.end()
    return tokens


table = {}
for source in ["IF Mark >= 50 THEN   // a pass", "OUTPUT Mark + Bonus", "OUTPUT Mark # 2"]:
    try:
        print(tokenise(source, table))
    except ValueError as problem:
        print(problem)
print(table)
```

Output:

```output
[('keyword', 'IF'), ('identifier', 'Mark'), ('operator', '>='), ('number', '50'), ('keyword', 'THEN')]
[('keyword', 'OUTPUT'), ('identifier', 'Mark'), ('operator', '+'), ('identifier', 'Bonus')]
lexical error: '#' is not allowed
{'Mark': 1, 'Bonus': 2}
```

Each identifier is entered once. `Mark` appears in two lines but has one entry, number 1. A **lexical error** is a symbol or word that cannot form any token: here, the `#`.

:::eg Describing lexical analysis (exam style)
Describe the purpose of lexical analysis. [3 marks]

The question says "describe", so give characteristics. Three separate points earn three marks.

- It removes white space and comments from the source code. [B1]
- It splits the source code into tokens, looking keywords up in a keyword table. [B1]
- It enters each identifier in the symbol table (with its data type, when known). [B1]

A fourth point that would also earn a mark: it reports lexical errors, such as a symbol that is not part of the language.
:::

### Syntax analysis

The tokens are in order, but are they a legal program? `Total ← 5 +` is made of perfectly good tokens and is still wrong, because `+` needs a value after it.

:::def Syntax analysis
The second stage of compilation. It checks the list of tokens against the rules (the grammar) of the language and, if they follow it, builds a parse tree. Any statement that breaks the rules is reported as a syntax error.
:::

:::def Parse tree
A tree that shows how a statement is built from the rules of the grammar. The tokens of the statement are the leaves, and every other node is a rule.
:::

The rules of a language are written precisely in BNF or in syntax diagrams, which are the next two sections of this chapter. A syntax analyser is a program that follows those rules. If a statement cannot be matched, it reports a **syntax error** such as a missing `ENDIF`, an unclosed bracket or a statement with no operand.

### Code generation

:::def Code generation
The stage that turns the checked program into object code, the machine code (or a lower-level language) that the processor can run. It uses the symbol table to give every variable a memory address.
:::

Suppose the symbol table gives `Price` address 200, `Tax` address 201 and `Total` address 202. The statement `Total ← Price + Tax - 5` becomes four instructions. They are shown here in assembly language, using the instructions from [Assembly language and bit manipulation](#cs.assembly), so that you can read them. A real compiler produces the binary form.

```text
LDD 200      // load the value at address 200 (Price) into ACC
ADD 201      // add the value at address 201 (Tax)
SUB #5       // subtract the number 5
STO 202      // store ACC at address 202 (Total)
```

If `Price` holds 40 and `Tax` holds 6, ACC holds 40, then 46, then 41, and 41 is stored in address 202.

### Optimisation

:::def Optimisation
The stage that improves the object code so that the program runs faster or uses less memory, without changing what the program does.
:::

The last clause matters most. An optimiser is only allowed to make changes that leave every result the same. Here are the kinds of change you can describe, each with a before and an after.

**Calculate a constant once.** In `Seconds ← 60 * 60 * 24`, every value is known while compiling, so the compiler does the sum and stores `Seconds ← 86400`. The multiplications never happen when the program runs.

**Remove code that does nothing.** A value that is stored and never used again, or code that can never be reached, is deleted. The object code is smaller.

**Move work out of a loop.** In this pseudocode, `Rate * 12` has the same value on every pass.

```pseudocode
FOR Index ← 1 TO 1000
   Fee[Index] ← Price[Index] + Rate * 12
NEXT Index
```

The optimiser works the multiplication out once, before the loop, and keeps the result.

```pseudocode
Annual ← Rate * 12
FOR Index ← 1 TO 1000
   Fee[Index] ← Price[Index] + Annual
NEXT Index
```

The first version multiplies 1000 times and the second once, a saving of 999 multiplications.

**Remove a repeated instruction.** In object code, a value stored and then immediately loaded back is already in the accumulator:

```text
STO 202
LDD 202
```

The `LDD 202` can be deleted (as long as no jump lands on it). Searching the whole object code for patterns like this takes time, which is one reason optimising makes compiling slower.

:::exam Naming the stages
A question may ask for the stages in order, or which stage does a job. The order is lexical analysis, syntax analysis, code generation, optimisation. Tokens and the symbol table come from the first stage, the parse tree from the second, object code from the third, and a faster or smaller program from the fourth. An interpreter does not do code generation or optimisation: it executes each statement directly.
:::

## Writing grammar rules: BNF

A syntax analyser needs a precise definition of every legal statement. English is too loose ("a name is some letters and digits"), so languages are defined with a formal notation.

:::def Backus-Naur Form (BNF)
A formal notation for writing the rules of a language. Each rule defines one non-terminal in terms of terminals and other non-terminals.
:::

:::def Terminal
A symbol that appears exactly as written in the language and cannot be broken down any further, for example `7`, `+` or `THEN`.
:::

:::def Non-terminal
A name written in angle brackets, such as `<digit>`, that stands for part of the language. It is defined by another rule.
:::

:::key BNF notation
- `<name>` is a non-terminal. Anything else is a terminal and appears exactly as written.
- `::=` means "is defined as".
- `|` means "or". It separates the alternatives of a rule.
- Items written side by side must appear in that order.
- A rule that uses its own name is **recursive**. This is how BNF says "repeat".
- Every non-terminal used on the right of a rule needs a rule of its own.
:::

The simplest rules list alternatives:

```text
<digit> ::= 0|1|2|3|4|5|6|7|8|9
```

An integer is one or more digits. BNF has no "one or more" symbol, so the rule uses recursion: an integer is a digit, or a digit followed by an integer.

```text
<integer> ::= <digit> | <digit><integer>
```

### Checking a string: derivation

To show that a string is valid, start from the rule and replace non-terminals until only the string is left. Each line is called a step of the derivation. Here is `407`:

The symbol ⇒ means "is replaced, in one step, by".

```text
<integer>
⇒ <digit><integer>
⇒ 4<integer>
⇒ 4<digit><integer>
⇒ 40<integer>
⇒ 40<digit>
⇒ 407
```

Lines 1 and 3 replace `<integer>` using the second alternative (`<digit><integer>`, a digit followed by an integer), and line 5 uses the first alternative (`<digit>`, just a digit) to finish. The other lines replace a `<digit>` by an actual digit. The same derivation can be drawn as a parse tree, with `<integer>` at the top and the digits at the leaves.

```text
<integer>
+-- <digit>: 4
+-- <integer>
    +-- <digit>: 0
    +-- <integer>
        +-- <digit>: 7
```

A string is invalid when no derivation exists. `12a` is invalid because `a` cannot come from `<digit>`. The empty string is invalid because every alternative of `<integer>` starts with a digit.

A BNF rule translates almost word for word into a recursive Python function, because the rule is itself recursive. The functions below check an integer, and a locker code that is defined in the next example. A function may call itself: here `is_integer` calls itself on the string without its first character (`text[1:]` means "the text from position 1 onwards"). cs.recursion ([Recursion](#cs.recursion)) explains this properly, so for now read it as a copy of the BNF rule: an integer is a digit followed by an integer.

```python
def is_digit(text):
    return len(text) == 1 and text in "0123456789"


def is_integer(text):
    if text == "":
        return False
    if len(text) == 1:
        return is_digit(text)
    return is_digit(text[0]) and is_integer(text[1:])


def is_block(text):
    return text in ("A", "B", "C", "D")


def is_number(text):
    return 1 <= len(text) <= 3 and all(is_digit(c) for c in text)


def is_locker_code(text):
    return len(text) >= 3 and is_block(text[0]) and text[1] == "-" and is_number(text[2:])


for test in ["407", "12a", ""]:
    print(repr(test), "is an integer:", is_integer(test))
for test in ["B-27", "D-304", "E-5", "C-1234", "A27", "B-"]:
    print(repr(test), "is a locker code:", is_locker_code(test))
```

Output:

```output
'407' is an integer: True
'12a' is an integer: False
'' is an integer: False
'B-27' is a locker code: True
'D-304' is a locker code: True
'E-5' is a locker code: False
'C-1234' is a locker code: False
'A27' is a locker code: False
'B-' is a locker code: False
```

:::eg Is each string valid? (exam style)
A school gives every library tag a colour and a number. The grammar is:

```text
<tag>    ::= <colour><number>
<colour> ::= R|G|B
<number> ::= <digit> | <digit><number>
<digit>  ::= 1|2|3
```

State whether each string is valid, with a reason. (a) `G213` (b) `R` (c) `B40` (d) `3G` [4 marks]

Check each string against the rules from the top: first a colour, then a number made of one or more digits, and the only digits allowed are 1, 2 and 3.

- (a) `G213` is valid: `G` is a `<colour>` and `213` is a `<number>` made of the digits 2, 1 and 3. [B1]
- (b) `R` is invalid: a `<tag>` needs a `<number>` after the colour, and there is none. [B1]
- (c) `B40` is invalid: `0` and `4` are not in `<digit>`, which allows only 1, 2 and 3. [B1]
- (d) `3G` is invalid: the colour must come first, and `3` is not a `<colour>`. [B1]
:::

### Writing BNF

Writing a rule from a description is the other half of the skill. Work in this order.

:::steps
1. Find the smallest building blocks (a digit, a letter, a fixed character) and give each a rule using `|`.
2. Write the rule for the whole item as a sequence of those blocks, in order.
3. Use **recursion** only for "any number of" something. For "exactly three" or "one to three", write the sequence out.
4. Test your rules on one valid string and one invalid string.
:::

:::eg Writing BNF for a locker code (exam style)
A school in Kampala labels lockers with a code such as `B-27` or `D-304`: a block letter from A to D, then a hyphen, then a number of one to three digits. Write BNF rules that define a locker code. [4 marks]

The building blocks are the block letter and the digit. The code is the block, the hyphen and then the number. The number is limited to three digits, so it needs no recursion.

```text
<code>   ::= <block>-<number>
<block>  ::= A|B|C|D
<digit>  ::= 0|1|2|3|4|5|6|7|8|9
<number> ::= <digit> | <digit><digit> | <digit><digit><digit>
```

- `<code>` is the block, the terminal `-` and the number, in that order. [B1]
- `<block>` lists exactly A, B, C and D as alternatives. [B1]
- `<digit>` lists the ten digits. [B1]
- `<number>` allows one, two or three digits (and no more). [B1]

Test: `B-27` is `<block>` B, the hyphen and a two-digit number, so it is valid. `E-5` is not, because E is not a `<block>`.
:::

Alternatives cannot be grouped, because BNF has no brackets, so `|` splits a whole rule. Use a helper rule when you need "this or that" in the middle of something. An identifier that starts with a letter and continues with letters or digits is a good example.

```text
<identifier> ::= <letter> | <letter><rest>
<rest>       ::= <letter> | <digit> | <letter><rest> | <digit><rest>
<letter>     ::= A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
<digit>      ::= 0|1|2|3|4|5|6|7|8|9
```

`TOTAL2` is valid. `2TOTAL` is not, because an identifier must start with a `<letter>`. (A rule with the recursion on the left, `<identifier> ::= <letter> | <identifier><letter> | <identifier><digit>`, defines the same strings and is also correct.)

:::warn The bar splits the whole rule
`<code> ::= <letter>|<digit><digit>` means a code is **either** a letter **or** two digits. It does not mean a letter followed by a digit or a letter. To say "a letter, then a digit or a letter", write a helper rule: `<char> ::= <letter>|<digit>` and `<code> ::= <letter><char>`.
:::

:::warn Recursion does not count
A rule such as `<number> ::= <digit> | <digit><number>` allows a number of any length. If the question says "one to three digits" or "exactly four digits", the recursive version loses the mark. Write the sequences out.
:::

## Syntax diagrams

The same grammar can be drawn. A **syntax diagram** is a map: you follow the arrows from the left to the right, and every route that gets you through is a valid string.

:::def Syntax diagram
A diagram that shows the rules of a language as paths. Rectangles are non-terminals (each has its own diagram), rounded boxes are terminals (written exactly as shown), arrows give the order, a split in the path is a choice and a path that loops back is repetition.
:::

The first diagram is the rule for an integer.

:::html
<figure class="fig small"><svg viewBox="0 0 340 150" role="img" aria-label="A syntax diagram for the rule integer. A line enters from the left, passes through one rectangle labelled digit, and leaves on the right. A second line loops from after the rectangle back to before it, so the digit can be repeated. Below, a key says a rectangle is a non-terminal with its own rule and a rounded box is a terminal written exactly as shown."><text class="tl tb" x="12" y="20">&lt;integer&gt;</text><path class="ln" d="M12 80 H128" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="130" y="64" width="76" height="32"/><text class="tl tc" x="168" y="85">digit</text><path class="ln" d="M206 80 H326" marker-end="url(#ah)"/><path class="ln" d="M245 80 V44 H116 V80" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="12" y="104" width="24" height="14"/><text class="tl" x="44" y="116">non-terminal: has its own rule</text><rect class="fm s-acc sw2" x="12" y="126" width="24" height="14" rx="7"/><text class="tl" x="44" y="138">terminal: written exactly as shown</text></svg><figcaption>The syntax diagram for an integer. Follow the arrows: one digit, then either leave or loop back for another digit. It means the same as the BNF rule <code>&lt;integer&gt; ::= &lt;digit&gt; | &lt;digit&gt;&lt;integer&gt;</code>.</figcaption></figure>
:::

Each BNF idea has a drawing.

| BNF idea | In a syntax diagram |
|---|---|
| a sequence, `<a><b>` | boxes one after another along one path |
| alternatives, `<a> \| <b>` | the path splits, one branch through each box, and the branches join again |
| repetition, a recursive rule | a path that loops back to an earlier point |
| an optional part | a path that goes round (bypasses) the box |
| a terminal, such as `-` | a rounded box |

The second diagram has three digit boxes with paths over the top of the second and third.

:::html
<figure class="fig small"><svg viewBox="0 0 340 110" role="img" aria-label="A syntax diagram for the rule number. A line enters from the left and passes through three rectangles in a row, each labelled digit. Lines above the row let a reader skip the second digit and the third digit, so a number has one, two or three digits."><text class="tl tb" x="12" y="20">&lt;number&gt;</text><path class="ln" d="M10 80 H34" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="36" y="64" width="52" height="32"/><text class="tl tc" x="62" y="85">digit</text><path class="ln" d="M88 80 H110" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="112" y="64" width="52" height="32"/><text class="tl tc" x="138" y="85">digit</text><path class="ln" d="M164 80 H186" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="188" y="64" width="52" height="32"/><text class="tl tc" x="214" y="85">digit</text><path class="ln" d="M240 80 H326" marker-end="url(#ah)"/><path class="ln" d="M100 80 V40 H252 V80"/><path class="ln" d="M176 80 V40"/><path class="ln" d="M140 40 H152" marker-end="url(#ah)"/></svg><figcaption>A syntax diagram for a number of one to three digits. The lines above the boxes let you skip the second digit, the third digit, or both.</figcaption></figure>
:::

:::eg From a syntax diagram to BNF
Write a BNF rule for the diagram of `<number>` above. [2 marks]

Read the path from the left. The first digit box cannot be skipped. The paths above let you leave out the second digit and the third, so a number is one, two or three digits.

```text
<number> ::= <digit> | <digit><digit> | <digit><digit><digit>
```

- The rule uses the non-terminal `<digit>` in each alternative. [B1]
- The alternatives give exactly one, two and three digits. [B1]
:::

Going the other way, from BNF to a diagram, draw one box for each item in a sequence, a split for each `|`, and a loop for each recursive rule. A diagram that is drawn with a rectangle where a terminal should be, or with an arrow missing, loses the mark: the shapes carry meaning.

## Grammar for expressions, and why precedence is built in

A real grammar also has to say what `A + B * 3` means. Notice that the grammar below has three levels. A **factor** is a single value or a bracketed expression. A **term** is factors joined by `*` or `/`. An **expression** is terms joined by `+` or `-`.

```text
<expression> ::= <term> | <expression> + <term> | <expression> - <term>
<term>       ::= <factor> | <term> * <factor> | <term> / <factor>
<factor>     ::= <number> | <variable> | ( <expression> )
```

The two names on the last line need rules as well, as in the earlier examples: `<number>` is one or more digits and `<variable>` is a single capital letter. The validator further down treats them the same way.

The levels build precedence into the grammar. In `A + B * 3`, the only way to derive the `*` is inside a `<term>`, which sits underneath the `+` of the expression. So `B * 3` is grouped first, as it must be. The parse tree shows it:

```text
<expression>
+-- <expression>
|   +-- <term>
|       +-- <factor>: A
+-- "+"
+-- <term>
    +-- <term>
    |   +-- <factor>: B
    +-- "*"
    +-- <factor>: 3
```

A recursive validator for this grammar has one function for each non-terminal. The rules that start with their own name (`<expression> ::= <expression> + <term>`) would make a function call itself forever, so the code uses a `while` loop to say "a term, then any number of (`+` or `-`, then a term)". Each function returns the position after the part it recognised, or `None` if it failed.

```python
def expression(tokens, pos):
    pos = term(tokens, pos)
    while pos is not None and pos < len(tokens) and tokens[pos] in ("+", "-"):
        pos = term(tokens, pos + 1)
    return pos


def term(tokens, pos):
    pos = factor(tokens, pos)
    while pos is not None and pos < len(tokens) and tokens[pos] in ("*", "/"):
        pos = factor(tokens, pos + 1)
    return pos


def factor(tokens, pos):
    if pos >= len(tokens):
        return None
    token = tokens[pos]
    if token.isdigit() or (len(token) == 1 and token.isalpha() and token.isupper()):
        return pos + 1
    if token == "(":
        pos = expression(tokens, pos + 1)
        if pos is not None and pos < len(tokens) and tokens[pos] == ")":
            return pos + 1
    return None


def is_valid(text):
    tokens = text.split()
    return expression(tokens, 0) == len(tokens)


for test in ["A + B * 3", "( A + B ) * C", "A + * B", "( A + B", "A B", "", "7"]:
    print(repr(test), is_valid(test))
```

Output:

```output
'A + B * 3' True
'( A + B ) * C' True
'A + * B' False
'( A + B' False
'A B' False
'' False
'7' True
```

A string is valid only if the parser uses up every token: in `A B` the first factor ends at position 1, which is not the end, so the result is `False`.

## Reverse Polish notation

The way you normally write an expression, with the operator between its two operands, is called **infix**. It needs brackets and precedence rules. In `A + B * C` you must know that `*` comes first, and to add first you must write `(A + B) * C`. A machine has to look ahead and remember to cope.

:::def Reverse Polish Notation (RPN)
A way of writing an expression with every operator after its operands (also called postfix notation). It needs no brackets and no precedence rules, and it can be evaluated from left to right using one stack.
:::

| Infix | Reverse Polish |
|---|---|
| `A + B` | `A B +` |
| `A + B * C` | `A B C * +` |
| `(A + B) * C` | `A B + C *` |
| `A - B - C` | `A B - C -` |
| `A - (B - C)` | `A B C - -` |

Notice that the order of the operands never changes. Only the operators move, and each lands straight after its two operands.

### Infix to RPN, by hand

:::steps
1. Put brackets round every operator and its two operands, working in order of precedence: `*` and `/` before `+` and `-`, and left to right when the operators are equal. Existing brackets stay.
2. Move each operator to the position of the closing bracket that belongs to it.
3. Delete all the brackets.
:::

:::eg Infix to RPN
Convert `(A + B) * (C - D) / E` to Reverse Polish notation. [2 marks]

`*` and `/` have equal precedence, so they work left to right: first the multiplication, then the division by E.

- Bracket every operation: `(((A + B) * (C - D)) / E)`
- Move each operator to its closing bracket: `(((A B +) (C D -) *) E /)`
- Delete the brackets: `A B + C D - * E /`

The mark scheme gives one mark for the two bracketed parts in the right order (`A B +` and `C D -`) [B1] and one for the operators `*` and `/` in the right places [B1].
:::

The same result comes from a picture. An expression can be drawn as a tree with each operator above its two operands. Reading the tree in **post-order**, which means visit the left subtree, then the right subtree, then the node itself, gives the RPN. Post-order traversal of trees is covered in [Abstract data types: stacks, queues, lists, trees and graphs](#cs.adts).

:::html
<figure class="fig small"><svg viewBox="0 0 340 262" role="img" aria-label="An expression tree. The root is the divide operator. Its left child is a multiply operator and its right child is the variable E. The multiply operator has two children: a plus operator with leaves A and B, and a minus operator with leaves C and D. Reading the tree in post-order gives A B + C D - * E /."><line class="ln" x1="159.4" y1="44.6" x2="120.6" y2="83.4"/><line class="ln" x1="180.6" y1="44.6" x2="219.4" y2="83.4"/><line class="ln" x1="100.4" y1="105.5" x2="69.6" y2="142.5"/><line class="ln" x1="119.6" y1="105.5" x2="150.4" y2="142.5"/><line class="ln" x1="53.3" y1="167.4" x2="36.7" y2="200.6"/><line class="ln" x1="66.7" y1="167.4" x2="83.3" y2="200.6"/><line class="ln" x1="153.3" y1="167.4" x2="136.7" y2="200.6"/><line class="ln" x1="166.7" y1="167.4" x2="183.3" y2="200.6"/><circle class="fm s-acc sw2" cx="170" cy="34" r="15"/><text class="tl tc tb" x="170" y="39">/</text><circle class="fm s-acc sw2" cx="110" cy="94" r="15"/><text class="tl tc tb" x="110" y="99">*</text><circle class="f1 s-acc sw2" cx="230" cy="94" r="15"/><text class="tl tc tb" x="230" y="99">E</text><circle class="fm s-acc sw2" cx="60" cy="154" r="15"/><text class="tl tc tb" x="60" y="159">+</text><circle class="fm s-acc sw2" cx="160" cy="154" r="15"/><text class="tl tc tb" x="160" y="159">-</text><circle class="f1 s-acc sw2" cx="30" cy="214" r="15"/><text class="tl tc tb" x="30" y="219">A</text><circle class="f1 s-acc sw2" cx="90" cy="214" r="15"/><text class="tl tc tb" x="90" y="219">B</text><circle class="f1 s-acc sw2" cx="130" cy="214" r="15"/><text class="tl tc tb" x="130" y="219">C</text><circle class="f1 s-acc sw2" cx="190" cy="214" r="15"/><text class="tl tc tb" x="190" y="219">D</text><text class="tl tc" x="170" y="254">post-order: A B + C D - * E /</text></svg><figcaption>The expression tree for (A + B) * (C - D) / E. Visit the left subtree, then the right subtree, then the node itself (post-order) and you read off the RPN.</figcaption></figure>
:::

In Python, a tree can be a tuple (operator, left, right) and a leaf a string. The post-order walk is then a three-line function, and so is the method a compiler uses to turn a tree into RPN. The conversion function below uses a stack of operators instead, which works on the tokens directly: an operand goes straight to the output, an operator waits on the stack until an operator of lower precedence arrives, a closing bracket or the end of the expression pushes the waiting operators out. Equal precedence leaves the earlier operator first.

```python
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def to_rpn(tokens):
    output = []
    operators = []
    for token in tokens:
        if token in PRECEDENCE:
            while operators and operators[-1] != "(" and PRECEDENCE[operators[-1]] >= PRECEDENCE[token]:
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()
        else:
            output.append(token)
    while operators:
        output.append(operators.pop())
    return output


for infix in ["A + B * C", "( A + B ) * C", "A - B - C", "( A + B ) * ( C - D ) / E"]:
    print(infix, "->", " ".join(to_rpn(infix.split())))


def post_order(node):
    if isinstance(node, str):
        return [node]
    operator, left, right = node
    return post_order(left) + post_order(right) + [operator]


tree = ("/", ("*", ("+", "A", "B"), ("-", "C", "D")), "E")
print(" ".join(post_order(tree)))
```

Output:

```output
A + B * C -> A B C * +
( A + B ) * C -> A B + C *
A - B - C -> A B - C -
( A + B ) * ( C - D ) / E -> A B + C D - * E /
A B + C D - * E /
```

### Evaluating RPN with a stack

This is the part a computer finds easy, and it is the reason RPN exists.

:::key Evaluating RPN
Read the tokens from left to right with an empty stack.
- An **operand** (a number or a variable's value): push it.
- An **operator**: pop twice, apply the operator, push the result. The **first value popped is the right-hand operand** and the second is the left-hand one, so for `-` and `/` it is `second popped − first popped`.
- At the end the stack holds one value, the answer.
:::

The widget below does both jobs. In **Convert to RPN**, press Next to watch the operator stack and the output grow, one token at a time. In **Evaluate RPN**, step through the evaluation and watch the stack. The starting example is the one used in this chapter. Change the expression to one of your own, or set the values of the variables, and check your own working against the widget's.

:::html
<div class="widget" data-w="cs-rpn" data-expr="(A + B) * (C - D) / E" data-vals="A=3,B=5,C=9,D=4,E=2"></div>
:::

:::eg Evaluating RPN with a stack (exam style)
The RPN expression `A B + C D - * E /` is to be evaluated with A = 3, B = 5, C = 9, D = 4 and E = 2. Show the contents of the stack after each token is processed, and give the result. [4 marks]

Process the tokens in order. For each operator, pop the right-hand value first.

| Token | Action | Stack (bottom to top) |
|---|---|---|
| A | push 3 | 3 |
| B | push 5 | 3, 5 |
| + | pop 5 and 3; 3 + 5 = 8; push 8 | 8 |
| C | push 9 | 8, 9 |
| D | push 4 | 8, 9, 4 |
| - | pop 4 and 9; 9 − 4 = 5; push 5 | 8, 5 |
| * | pop 5 and 8; 8 × 5 = 40; push 40 | 40 |
| E | push 2 | 40, 2 |
| / | pop 2 and 40; 40 ÷ 2 = 20; push 20 | 20 |

- Operands pushed in the right order, with the stack correct after the first `+` (8). [B1]
- The subtraction applied as 9 − 4 = 5 (second value popped minus first), giving the stack 8, 5. [B1]
- The multiplication giving 40. [B1]
- The division applied as 40 ÷ 2, giving the result 20. [B1]
:::

Here is the same evaluation in Python, with a list as the stack. It prints the stack after every token, so the output is the table above. Because `/` in Python always gives a real number, the answer prints as `20.0`.

```python
def evaluate_rpn(tokens, values):
    stack = []
    for token in tokens:
        if token in ("+", "-", "*", "/"):
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(left / right)
        elif token in values:
            stack.append(values[token])
        else:
            stack.append(int(token))
        print(token, stack)
    return stack.pop()


answer = evaluate_rpn("A B + C D - * E /".split(), {"A": 3, "B": 5, "C": 9, "D": 4, "E": 2})
print("Answer:", answer)
```

Output:

```output
A [3]
B [3, 5]
+ [8]
C [8, 9]
D [8, 9, 4]
- [8, 5]
* [40]
E [40, 2]
/ [20.0]
Answer: 20.0
```

:::warn The order of the operands for - and /
`9 4 -` means \(9 - 4 = 5\), not \(4 - 9\). The second value popped is the left-hand operand. Popping the top value and calling it the left-hand one is the most common wrong answer in RPN evaluation, and it makes every subtraction and division wrong.
:::

### RPN back to infix

An examiner may go the other way. Use a stack of strings: when you meet an operator, pop two strings, join them with the operator inside brackets, and push the result.

:::eg RPN to infix
Convert `P Q R - S * +` to an infix expression. [3 marks]

Push `P`, `Q` and `R`. Then deal with each operator in turn.

- `-`: pop `R` and `Q`, push `(Q - R)`. The stack is `P`, `(Q - R)`. [B1]
- Push `S`. Then `*`: pop `S` and `(Q - R)`, push `((Q - R) * S)`. [B1]
- `+`: pop `((Q - R) * S)` and `P`, push `(P + ((Q - R) * S))`. Removing the brackets that are not needed gives `P + (Q - R) * S`. [B1]

Check by evaluating both forms with P = 2, Q = 7, R = 3, S = 5: RPN gives \(7 - 3 = 4\), \(4 \times 5 = 20\), \(2 + 20 = 22\), and the infix gives \(2 + 4 \times 5 = 22\).
:::

### Why compilers and interpreters use RPN

- **No brackets and no precedence rules.** The position of each operator already says what happens first, so the order of the work is fixed once the expression is converted.
- **One left-to-right pass.** The evaluator reads each token once and never looks ahead or goes back.
- **One stack.** An operand is pushed, and an operator needs only the top two values. Stacks are cheap and the processor can do them quickly.
- **It matches the expression tree.** A compiler's parse tree becomes an expression tree, and its post-order traversal is RPN. The code generator then turns each RPN token into an instruction: an operand becomes a load, an operator becomes an arithmetic instruction that works on the values just loaded.

:::analogy
Think of a stack of plates in a canteen. Operands are plates added to the pile. An operator says "take the top two plates, combine them, and put the result back on top". You never need to look at the plates underneath.
:::

:::eg Spot the error: ignoring precedence
Question: Convert `K * L + M * N` to Reverse Polish notation. [3 marks]

A student wrote `K L * M + N *`.

The first part, `K L *`, is correct: K and L are multiplied first [B1]. The student then carried on strictly left to right: `M +` adds M to the product at once, which is not allowed because `M * N` must be calculated first, so the second mark is lost [B0]. The final `N *` multiplies the sum by N, so the last mark is lost too [B0]. **The slip was treating every operator as equal.** The answer scores 1 out of 3.

Because `*` has higher precedence than `+`, there are two products, then the sum. Bracketing shows it: `((K * L) + (M * N))`. Moving each operator to its closing bracket gives `K L * M N * +`.
:::

:::eg Spot the error: the bar in BNF
Question: A PIN is exactly four digits. Write BNF rules for a PIN. [3 marks]

A student wrote:

```text
<pin>   ::= <digit>|<digit>|<digit>|<digit>
<digit> ::= 0|1|2|3|4|5|6|7|8|9
```

The rule for `<digit>` is correct and complete [B1]. The rule for `<pin>` uses the non-terminal `<digit>` [B1]. **The `|` means "or", so this rule says a PIN is one digit, not four. The mark for four digits in sequence is lost** [B0]. The answer scores 2 out of 3. The correct rule has no bars: `<pin> ::= <digit><digit><digit><digit>`.
:::

:::try Start easy, finish at exam standard
Q: What is a token? Give two examples from the statement `OUTPUT Count + 1`.
A: A token is the smallest meaningful unit of a program, produced by lexical analysis. Examples: the keyword `OUTPUT`, the identifier `Count`, the operator `+` and the constant `1`. Any two are correct.
Q: Put these in the order a compiler carries them out: code generation, syntax analysis, optimisation, lexical analysis.
A: Lexical analysis, syntax analysis, code generation, optimisation.
Q: Name the stage of compilation that finds each error. (a) `Cost$ ← 4` where `$` is not a legal symbol. (b) `Total ← 5 +` (c) A missing `ENDIF` at the end of an `IF` statement.
A: (a) Lexical analysis, because `$` cannot form a token. (b) Syntax analysis, because the tokens break the grammar (`+` has no operand). (c) Syntax analysis, because the tokens do not follow the grammar of an `IF` statement.
Q: The grammar is `<bit> ::= 0|1` and `<bits> ::= <bit> | <bit><bits>`. Which of `1011`, `102` and the empty string are valid?
A: `1011` is valid: every character is a `<bit>`. `102` is invalid, because 2 is not a `<bit>`. The empty string is invalid, because `<bits>` must contain at least one `<bit>`.
Q: Write one BNF rule for `<grade>`, which is one of the letters A, B or C.
A: `<grade> ::= A|B|C`
Q: Convert `(P + Q) / R - S` to Reverse Polish notation.
A: Bracket it: `(((P + Q) / R) - S)`. Move each operator to its closing bracket: `(((P Q +) R /) S -)`. The answer is `P Q + R / S -`.
Q: Evaluate the RPN expression `12 3 - 4 *`.
A: Push 12 and 3. The `-` pops 3, then 12, and gives \(12 - 3 = 9\). Push 4. The `*` pops 4, then 9, and gives \(9 \times 4 = 36\). The answer is 36.
Q: Evaluate `6 2 / 3 4 * +`.
A: \(6 / 2 = 3\), so the stack is 3. Push 3 and 4, and the `*` gives 12, so the stack is 3, 12. The `+` gives \(3 + 12 = 15\). The answer is 15.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Describe the purpose of syntax analysis.
A: Three points, one mark each:

- It checks the tokens against the grammar (the rules) of the language [B1]
- It reports a syntax error when a statement breaks the rules [B1]
- It builds a parse tree for a statement that is correct [B1]

(Accept also: it uses the tokens produced by lexical analysis, and it passes a correct program on to code generation.)

Q: [4 marks] ★ Describe how an interpreter executes a program without producing a translated version of it.
A: Four points, one mark each:

- It takes one statement of the source code at a time [B1]
- It analyses the statement to check that it follows the rules of the language [B1]
- It executes the statement immediately, using a routine in the interpreter that does what the statement means [B1]
- It then moves on to the next statement and repeats [B1]

(Accept also: it stops and reports an error when it reaches a statement that is wrong; no object code is stored, so the source code is analysed again every time the program runs.)

Q: [4 marks] ★★ A bakery in Porto labels each tray with a code such as `S42Z`: one letter from R, S or T, then exactly two digits, then the letter X or Z. Write BNF rules that define a tray code.
H: Give each small part a rule first: the first letter, the digit, the last letter.
H: "Exactly two digits" means writing `<digit>` twice. Do not use recursion.
A: One possible answer:

```text
<tray>  ::= <first><digit><digit><last>
<first> ::= R|S|T
<last>  ::= X|Z
<digit> ::= 0|1|2|3|4|5|6|7|8|9
```

- `<tray>` is the first letter, two digits and the last letter in that order [B1]
- `<first>` is R, S or T and `<last>` is X or Z [B1]
- `<digit>` lists the ten digits [B1]
- exactly two digits, with no recursion (accept: `<digit><digit>` written out) [B1]

Q: [4 marks] ★★ A school stores room codes using these rules:

```text
<room>   ::= <floor><number>
<floor>  ::= G|1|2
<number> ::= <digit><digit>
<digit>  ::= 0|1|2|3|4|5|6|7|8|9
```

State whether each code is valid, and give a reason for each: (a) `G07` (b) `214` (c) `3` (d) `2A5`
A: Each answer needs the decision and a reason.

- (a) `G07` is valid: G is a `<floor>` and 07 is two digits [B1]
- (b) `214` is valid: 2 is a `<floor>` and 14 is two digits [B1]
- (c) `3` is invalid: 3 is not a `<floor>` (accept: there are no two digits after it) [B1]
- (d) `2A5` is invalid: A is not a `<digit>` (accept: a `<number>` must be two digits) [B1]

Q: [4 marks] ★★ (a) Convert `X * (Y + Z)` to Reverse Polish notation. [2] (b) Convert `X * Y + Z / W` to Reverse Polish notation. [2]
A: (a) Bracket the parts: `(X * (Y + Z))`. The addition is inside the brackets, so it comes first: `X Y Z + *`.

- `Y Z +` in the right place after X [B1]
- `*` last [B1]

(b) The multiplication and the division come before the addition: `((X * Y) + (Z / W))`, giving `X Y * Z W / +`.

- `X Y *` and `Z W /` in order [B1]
- `+` last [B1]

Q: [4 marks] ★★ The RPN expression `W X + Y * Z -` is evaluated with W = 4, X = 6, Y = 3 and Z = 7. Show the stack after each token and give the result.
A: Process the tokens in order.

| Token | Action | Stack (bottom to top) |
|---|---|---|
| W | push 4 | 4 |
| X | push 6 | 4, 6 |
| + | 4 + 6 = 10 | 10 |
| Y | push 3 | 10, 3 |
| * | 10 × 3 = 30 | 30 |
| Z | push 7 | 30, 7 |
| - | 30 − 7 = 23 | 23 |

- the first two values pushed and the first addition giving 10 [B1]
- `Y` pushed and the multiplication giving 30 [B1]
- `Z` pushed and the subtraction done as 30 − 7 (not 7 − 30) [B1]
- the result 23 [B1]

Q: [6 marks] ★★★ A kiosk accepts discount codes written with these rules:

```text
<code>   ::= <series>-<digit><digit>
<series> ::= <letter> | <letter><letter>
<letter> ::= K|M|P
<digit>  ::= 1|2|3|4
```

(a) State whether each code is valid, with a reason: `KM-41`, `P-5`, `MK-3`. [3] (b) Describe a syntax diagram for `<code>`: the boxes, the shape of each and how they are joined. [3]
H: In (a), check the series first, then the hyphen, then the two digits.
H: In (b), a rectangle means a non-terminal and a rounded box a terminal.
A: (a)

- `KM-41` is valid: KM is two letters from K, M, P; the hyphen is there; 41 is two digits from 1 to 4 [B1]
- `P-5` is invalid: 5 is not a `<digit>` (and there is only one digit) [B1]
- `MK-3` is invalid: only one digit follows the hyphen (a `<code>` needs two) [B1]

(b)

- a rectangle for `<series>`, then a rounded box for the terminal `-`, then two rectangles for `<digit>`, joined by arrows left to right [B1]
- a path that lets the series have one or two letters (a loop or a bypass round a second `<letter>` box) [B1]
- `<series>` and `<digit>` are non-terminals, so they are rectangles, and the hyphen is a terminal, so it is a rounded box [B1]

Q: [5 marks] ★★★ (a) Draw the expression tree for `(A + B * C) / (D - E)`. [3] (b) Write the post-order traversal of your tree as an RPN expression. [2]
H: Draw `B * C` first: it is the first operation inside the left bracket.
H: The root is the last operation to be carried out.
A: (a) The root is `/`. Its left child is `+`, with A on the left and `*` on the right (the `*` has children B and C). Its right child is `-`, with children D and E.

- the root is `/` with the two bracketed parts as its children [B1]
- `*` (with B and C) is a child of `+`, with A as the other child, because `*` comes before `+` [B1]
- `-` with children D and E on the right [B1]

(b) Visit the left subtree, then the right subtree, then the root: `A B C * + D E - /`.

- left subtree `A B C * +` [B1]
- right subtree `D E -` followed by `/` [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A clock program accepts a time such as `07:45` or `23:59`: two digits for the hour (00 to 23), a colon and two digits for the minute (00 to 59). Write BNF rules that accept exactly the valid times. Then explain why the rule `<hour> ::= <digit><digit>` is not good enough.
H: The first hour digit is 0, 1 or 2. What can follow a 2?
H: Make a helper rule for the digit that follows a 2.
A: One possible answer:

```text
<time>    ::= <hour>:<minute>
<hour>    ::= 0<digit> | 1<digit> | 2<late>
<late>    ::= 0|1|2|3
<minute>  ::= <tens><digit>
<tens>    ::= 0|1|2|3|4|5
<digit>   ::= 0|1|2|3|4|5|6|7|8|9
```

- `<time>` is the hour, the terminal `:` and the minute [B1]
- hours starting with 0 or 1 may be followed by any digit [B1]
- hours starting with 2 may be followed only by 0 to 3, using a helper rule [B1]
- minutes: a first digit from 0 to 5 and then any digit [B1]
- `<digit>` defined as the ten digits [B1]
- `<hour> ::= <digit><digit>` would accept `24`, `37` and `99`, which are not hours; the grammar must restrict the second digit when the first is 2 and the first digit to 0, 1 or 2 [B1]

Q: [5 marks] ★★★ The stack's greatest size matters, because a processor has only a few registers to hold it. (a) What is the greatest number of values on the stack at any time when `P Q R S T + + + +` is evaluated? [1] (b) Write `((P + Q) + R) + S` in RPN and state the greatest stack size. [2] (c) Explain why the two expressions give different greatest sizes although both add the same kind of values. [2]
H: Draw the stack after each token for (a): operands keep arriving before any operator.
H: In (b), every `+` comes straight after two operands are available.
A: (a) All five operands are pushed before the first `+`, so the greatest size is 5 [B1].

(b) `P Q + R + S +`. After P and Q the stack holds 2 values, then `+` leaves 1, R makes 2, `+` leaves 1, S makes 2 and the last `+` leaves 1. The greatest size is 2 [B1] [B1].

(c) In `P Q R S T + + + +` the operators all wait until the end, so every operand has to be held on the stack together [B1]. In `P Q + R + S +` each operator is used as soon as its two operands are ready, so values never build up [B1].
:::

:::quiz
? Which stage of compilation removes comments and white space and creates the symbol table?
- Syntax analysis
+ Lexical analysis
- Code generation
- Optimisation
> Lexical analysis works on the characters of the source code. Syntax analysis then checks the order of the tokens, which no longer contain comments or spaces.
? What happens when an interpreter reaches a statement that breaks the rules of the language?
- Nothing is run, because the whole program is checked first
- The statement is skipped and the next one is run
+ The statements before it have already run, and it reports the error and stops
- It stores the faulty statement in an object code file
> An interpreter executes statements as it reads them, so earlier output has already appeared. Checking the whole program first is what a compiler does.
? In BNF, what does `<a> ::= <b> | <c><d>` mean?
- An `<a>` is a `<b>` followed by a `<c>` and a `<d>`
+ An `<a>` is either a `<b>`, or a `<c>` followed by a `<d>`
- An `<a>` is a `<b>` or a `<c>`, and then always a `<d>`
- An `<a>` must contain all of `<b>`, `<c>` and `<d>`
> The bar separates whole alternatives: either `<b>`, or the two-item sequence `<c><d>`. The bar does not bind a smaller group, because BNF has no brackets.
? What is the Reverse Polish form of `A - B - C`?
- `A B C - -`
+ `A B - C -`
- `A - B - C`
- `C B A - -`
> Operators of equal precedence work left to right, so `(A - B)` comes first: `A B -`, then C is subtracted. `A B C - -` is the answer for `A - (B - C)`.
? What is the value of the RPN expression `20 4 - 2 /`?
+ 8
- -8
- 18
- 3
> \(20 - 4 = 16\), and \(16 / 2 = 8\). -8 comes from taking 4 − 20 (the operands the wrong way round). 18 comes from reading it as infix `20 - 4 / 2`, and 3 from \((20 / 4) - 2\).
? Why do compilers and interpreters convert expressions to RPN?
- Because RPN uses fewer variables
- Because brackets are not allowed in programs
+ Because a single stack can evaluate it from left to right, with no brackets or precedence rules
- Because RPN gives a more accurate answer than infix
> Evaluating needs only one pass and one stack. The two notations give the same value.
? What must an optimiser never change?
- The number of instructions
- The memory addresses used
+ The results the program produces
- The names of the variables
> Optimisation exists to make the program faster or smaller, so it changes the instructions. It must still give the same results.
:::

:::checklist What you can now do
- [ ] I can describe how an interpreter executes a program one statement at a time without producing a translated version.
- [ ] I can describe lexical analysis: removing white space and comments, producing tokens, using a keyword table and building the symbol table.
- [ ] I can describe syntax analysis and parse trees, code generation and optimisation, and give a before and an after example of optimisation.
- [ ] I can say which stage of compilation finds which kind of error.
- [ ] I can read BNF, decide whether a string is valid and show the derivation.
- [ ] I can write BNF rules for an identifier or a code format, using recursion only where the length is unlimited.
- [ ] I can convert between BNF and syntax diagrams.
- [ ] I can convert infix expressions to Reverse Polish notation and back, with the correct precedence.
- [ ] I can evaluate an RPN expression with a stack, showing the stack at each step, with the operands the right way round.
- [ ] I can explain why compilers and interpreters use Reverse Polish notation.
:::

:::recap
- An interpreter reads, analyses and executes one statement at a time and produces no object code. It reports an error only when it reaches the statement, after earlier statements have run. Statements in a loop are analysed again each time.
- Compilation has four stages, in order: lexical analysis (white space and comments removed, tokens, keyword table, symbol table), syntax analysis (tokens checked against the grammar, parse tree, syntax errors), code generation (object code, addresses from the symbol table) and optimisation (faster or smaller code with the same results).
- BNF: `<non-terminal>` in angle brackets, `::=` "is defined as", `|` "or", side by side means in order, recursion means repetition. The bar splits the whole rule. Use recursion only for unlimited length.
- A syntax diagram uses rectangles for non-terminals, rounded boxes for terminals, arrows for order, branches for choice and loops for repetition.
- Reverse Polish notation puts the operator after its operands. Convert by bracketing in precedence order, moving each operator to its closing bracket and deleting the brackets. Equal precedence works left to right.
- Evaluate RPN with a stack: push operands; for an operator pop twice (the first popped is the right operand), apply it and push the result. One value is left: the answer.
- RPN needs no brackets or precedence rules and is evaluated in one pass with one stack. A tree read in post-order gives RPN.
:::

:::links
- practise: [Translation software: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/16-system-software-/translation-software/exam-questions/) · Save My Exams · 9618-style questions on compilation, BNF and RPN with mark schemes [paid]
- explore: [Reverse Polish notation](https://www.101computing.net/reverse-polish-notation/) · 101 Computing · convert and evaluate expressions and watch the stack
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste the RPN evaluator and watch the stack list change line by line
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists, including compilers and language design
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · notes on every 9618 topic [paid]

Links checked 13 November 2026.
:::

Next: [Encryption, SSL/TLS and digital certificates](#cs.security2)
