@chapter cs.logic
@title Logic gates and logic circuits
@level as
@paper CAIE 9618 Paper 1
@time 5–6 hours
@summary The six logic gates (NOT, AND, OR, NAND, NOR, XOR), their symbols, definitions and truth tables, and how to move between a problem statement, a logic expression, a logic circuit and a truth table in any direction.

:::why
Every decision a computer makes comes down to circuits that combine 0s and 1s: whether two numbers are equal, whether a door alarm should sound, whether a result has overflowed. Paper 1 turns this into reliable marks: draw a circuit from an expression, write the expression for a circuit, complete a truth table. Once you know the six gates and work in a fixed order, these questions become routine, and every mark is for a small, checkable step.
:::

**Before you start**, you should know how binary numbers are written, from [Data representation](#cs.data), and what a sensor does, from [Computers and their components](#cs.hardware).

:::try Warm-up
Q: True or false: "A number qualifies if it is greater than 10 AND less than 20." Does 15 qualify? (from [Programming from zero](#cs.f.basics))
A: True. 15 is greater than 10 and less than 20, so both parts are true.
Q: What is 1 + 1 in binary, and what is carried? (from [Data representation](#cs.data))
A: \(1 + 1 = 10\) in binary: the digit is 0 and 1 is carried to the next column.
Q: Which part of a control system turns the analogue signal from a sensor into digital data? (from [Computers and their components](#cs.hardware))
A: The analogue-to-digital converter (ADC).
:::

## Logic gates and truth tables

A computer stores everything as 0s and 1s, and its processor is built from circuits that take 0s and 1s in and give a 0 or a 1 out. The smallest of these circuits are **logic gates**. A gate is built from a few transistors (tiny electronic switches), and a modern processor contains billions of them, joined together to add numbers, compare values and decide what to do next.

:::def Logic gate
An electronic component that takes one or two binary inputs (0 or 1) and produces one binary output, according to a fixed rule (a logic function).
:::

:::def Truth table
A table that lists every possible combination of the inputs to a gate or circuit and the output for each combination.
:::

:::def Logic expression
A statement that gives the output of a logic circuit in terms of its inputs, using the names of gates (AND, OR, NOT, NAND, NOR, XOR) and brackets, for example \(X = (A \text{ AND } B) \text{ OR NOT } C\).
:::

In this chapter 1 means "on" or "true" and 0 means "off" or "false". Truth tables are written with 1 and 0. When a problem describes something real, such as a door sensor, the first job is to say what 1 means. Inputs are labelled with capital letters A, B, C, and the output is labelled X.

## The six gates

You must know six gates. For each one, learn three things: what the output does (a one-sentence rule), its symbol, and its truth table.

:::html
<figure class="fig"><svg viewBox="0 0 600 250" role="img" aria-label="The six logic gate symbols: NOT, AND and OR in the top row; NAND, NOR and XOR in the bottom row. Each has input wires labelled A and B (NOT has only A), an output wire labelled X, and its expression under it. NOT is a triangle with a small circle on its output. AND has a flat back and a rounded front. OR has a curved back and a pointed front. NAND is AND with the small circle, NOR is OR with the small circle, and XOR is OR with an extra curved line behind it."><text class="tl tb tc" x="100" y="24">NOT</text><g transform="translate(70 40)"><path class="fm s-acc sw2" d="M0 0 L28 20 L0 40 Z"/><circle class="fm s-acc sw2" cx="32" cy="20" r="4"/></g><polyline class="ln" fill="none" points="34,60 70,60"/><text class="tl tc" x="20" y="64">A</text><polyline class="ln" fill="none" points="106,60 128,60"/><text class="tl" x="134" y="64">X</text><text class="tl tc" x="100" y="108">X = NOT A</text><text class="tl tb tc" x="300" y="24">AND</text><g transform="translate(270 40)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><polyline class="ln" fill="none" points="234,50 270,50"/><text class="tl tc" x="220" y="54">A</text><polyline class="ln" fill="none" points="234,70 270,70"/><text class="tl tc" x="220" y="74">B</text><polyline class="ln" fill="none" points="310,60 332,60"/><text class="tl" x="338" y="64">X</text><text class="tl tc" x="300" y="108">X = A AND B</text><text class="tl tb tc" x="500" y="24">OR</text><g transform="translate(470 40)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/></g><polyline class="ln" fill="none" points="434,50 474,50"/><text class="tl tc" x="420" y="54">A</text><polyline class="ln" fill="none" points="434,70 474,70"/><text class="tl tc" x="420" y="74">B</text><polyline class="ln" fill="none" points="512,60 534,60"/><text class="tl" x="540" y="64">X</text><text class="tl tc" x="500" y="108">X = A OR B</text><text class="tl tb tc" x="100" y="154">NAND</text><g transform="translate(70 170)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/><circle class="fm s-acc sw2" cx="44" cy="20" r="4"/></g><polyline class="ln" fill="none" points="34,180 70,180"/><text class="tl tc" x="20" y="184">A</text><polyline class="ln" fill="none" points="34,200 70,200"/><text class="tl tc" x="20" y="204">B</text><polyline class="ln" fill="none" points="118,190 140,190"/><text class="tl" x="146" y="194">X</text><text class="tl tc" x="100" y="238">X = A NAND B</text><text class="tl tb tc" x="300" y="154">NOR</text><g transform="translate(270 170)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><polyline class="ln" fill="none" points="234,180 274,180"/><text class="tl tc" x="220" y="184">A</text><polyline class="ln" fill="none" points="234,200 274,200"/><text class="tl tc" x="220" y="204">B</text><polyline class="ln" fill="none" points="320,190 342,190"/><text class="tl" x="348" y="194">X</text><text class="tl tc" x="300" y="238">X = A NOR B</text><text class="tl tb tc" x="500" y="154">XOR</text><g transform="translate(470 170)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><path class="ln" fill="none" d="M-6 0 C1 12 1 28 -6 40"/></g><polyline class="ln" fill="none" points="434,180 468,180"/><text class="tl tc" x="420" y="184">A</text><polyline class="ln" fill="none" points="434,200 468,200"/><text class="tl tc" x="420" y="204">B</text><polyline class="ln" fill="none" points="512,190 534,190"/><text class="tl" x="540" y="194">X</text><text class="tl tc" x="500" y="238">X = A XOR B</text></svg><figcaption>The six gates with their expressions. A small circle on the output means NOT. Every gate except NOT has two inputs.</figcaption></figure>
:::

Look for the pattern in the symbols. The small circle on an output always means "NOT", so NAND is an AND with a circle and NOR is an OR with a circle. XOR is an OR with an extra curved line across the back. Draw the shapes exactly, because an examiner marks the symbol: an AND with a pointed front is an OR.

### NOT

:::def NOT gate
A gate with one input whose output is the opposite of the input: the output is 1 when the input is 0, and 0 when the input is 1.
:::

| A | X = NOT A |
|---|---|
| 0 | 1 |
| 1 | 0 |

### AND

:::def AND gate
A gate with two inputs whose output is 1 only when both inputs are 1.
:::

### OR

:::def OR gate
A gate with two inputs whose output is 1 when at least one input is 1 (and 0 only when both inputs are 0).
:::

### NAND

:::def NAND gate
A gate with two inputs whose output is the opposite of an AND gate: the output is 0 only when both inputs are 1, and 1 otherwise. NAND means NOT AND.
:::

### NOR

:::def NOR gate
A gate with two inputs whose output is the opposite of an OR gate: the output is 1 only when both inputs are 0, and 0 otherwise. NOR means NOT OR.
:::

### XOR

:::def XOR gate
A gate with two inputs (exclusive OR) whose output is 1 when the inputs are different (exactly one input is 1), and 0 when they are the same.
:::

Here are the truth tables of all five two-input gates in one table, so you can compare them column by column.

:::key The five two-input gates
| A | B | A AND B | A OR B | A NAND B | A NOR B | A XOR B |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

- AND: 1 only if **both** are 1. OR: 1 if **at least one** is 1.
- NAND is the opposite of AND in every row. NOR is the opposite of OR in every row.
- XOR is OR **except** when both inputs are 1: it is 1 when the inputs **differ**.
:::

The Python program below builds the table from six small functions, using the operators `&` (and), `|` (or) and `^` (xor) on 0 and 1. Run it to see the truth tables come out exactly as above.

```python
def NOT(a):
    return 1 - a
def AND(a, b):
    return a & b
def OR(a, b):
    return a | b
def NAND(a, b):
    return NOT(AND(a, b))
def NOR(a, b):
    return NOT(OR(a, b))
def XOR(a, b):
    return a ^ b

print("A B | AND OR NAND NOR XOR")
for a in (0, 1):
    for b in (0, 1):
        print(f"{a} {b} | {AND(a, b):<4}{OR(a, b):<3}{NAND(a, b):<5}{NOR(a, b):<4}{XOR(a, b)}")
```

Output:

```output
A B | AND OR NAND NOR XOR
0 0 | 0   0  1    1   0
0 1 | 0   1  1    0   1
1 0 | 0   1  1    0   1
1 1 | 1   1  0    0   0
```

Notice that NAND and NOR are built from the other functions, exactly as their names say: `NAND` returns `NOT(AND(a, b))`.

:::warn Three slips that cost marks
- **NAND is not "NOT A AND NOT B".** NAND is NOT (A AND B), which is 0 only when both inputs are 1. "NOT A AND NOT B" is 1 only when both inputs are 0, and that is the NOR gate.
- **XOR gives 0 when both inputs are 1.** It is not the same as OR. "XOR means either one, but not both."
- **The small circle means NOT.** An AND symbol with a circle is NAND, not "AND with a different style". Leaving the circle off, or adding it to the wrong gate, loses the mark.
:::

:::note Two inputs only
At AS Level every gate except NOT has exactly two inputs. A chain such as A AND B AND C is built from two gates: one AND for A and B, and a second AND for that result and C. Do not draw a gate with three input wires.
:::

Try the gates yourself. Pick a gate, then press the A and B buttons to switch the inputs between 0 and 1: the output changes, and the matching row of the truth table is marked.

:::html
<div class="widget" data-w="cs-logic" data-tab="gates" data-gate="XOR"></div>
:::

## Truth tables for a circuit with more inputs

A circuit may have three or four inputs, so the truth table needs a **row for every possible combination**. With one input there are 2 rows, with two inputs there are 4, and every extra input doubles the number of rows.

:::key Rows in a truth table
A circuit with \(n\) inputs has \(2^n\) rows: 2 inputs give 4 rows, 3 inputs give 8 rows, 4 inputs give 16 rows. List the input combinations in **binary counting order**, 000, 001, 010, 011, 100, 101, 110, 111, with A as the left-hand column. Then no combination is missed or repeated.
:::

Missing rows is the commonest way to lose a mark in a truth-table question, so write the left-hand columns first and count the rows. With A as the left-hand column, A is 0 for the first half of the rows and 1 for the second half; B alternates in pairs; C alternates in every row.

### Working columns

For a circuit with more than one gate, do not work out the output in one go. Add a **working column** for the output of each gate, and fill the columns one at a time, from the gates nearest the inputs towards X. Each column is simple, so errors are rare, and an examiner who sees a wrong final column can still give credit for correct working.

:::eg A truth table with working columns
Complete the truth table for \(X = (A \text{ AND } B) \text{ OR NOT } C\).

Call the output of the AND gate P and the output of the NOT gate Q. Then \(P = A \text{ AND } B\), \(Q = \text{NOT } C\) and \(X = P \text{ OR } Q\). List the eight input combinations, then fill P, then Q, then X.

| A | B | C | P = A AND B | Q = NOT C | X = P OR Q |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 |

P is 1 only in the last two rows, where A and B are both 1. Q is the opposite of C in every row. X is 1 whenever P or Q is 1: five of the eight rows.
:::

Python can produce the same table, which is a good way to check your own working. Each row is computed in the same order as the working columns.

```python
print("A B C | P Q | X")
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            p = a & b
            q = 1 - c
            x = p | q
            print(a, b, c, "|", p, q, "|", x)
```

Output:

```output
A B C | P Q | X
0 0 0 | 0 1 | 1
0 0 1 | 0 0 | 0
0 1 0 | 0 1 | 1
0 1 1 | 0 0 | 0
1 0 0 | 0 1 | 1
1 0 1 | 0 0 | 0
1 1 0 | 1 1 | 1
1 1 1 | 1 0 | 1
```

The tool below does the same for any expression you type. It lists the truth table with one working column for every gate in the expression. Try the example, then change it. Then press **Test me**: the X column turns into buttons, and you fill in the outputs yourself before the tool marks them.

:::html
<div class="widget" data-w="cs-logic" data-tab="expr" data-expr="(A AND B) OR NOT C"></div>
:::

## Writing logic expressions

A circuit can be described in words, in a drawing or in a **logic expression**. An expression is the shortest of the three, but it has to be written carefully, because the order in which the gates are applied must be clear.

:::key Rules for writing an expression
- Write a two-input gate between its inputs: `A AND B`, `A NOR B`. Write NOT before its input: `NOT C`.
- Put **brackets round every gate that feeds another gate**: `(A AND B) OR NOT C`. Work out the inner brackets first.
- NOT applies only to the **one item** after it. `NOT A AND B` means `(NOT A) AND B`. To invert a whole gate output, bracket it: `NOT (A AND B)`.
- Never mix two different gates without brackets. Write `(A AND B) OR C`, never `A AND B OR C`.
:::

The third rule matters because the two forms give different answers. Take A = 1 and B = 0.

| Expression | Working | Result |
|---|---|---|
| `(NOT A) AND B` | NOT 1 = 0, then 0 AND 0 | 0 |
| `NOT (A AND B)` | 1 AND 0 = 0, then NOT 0 | 1 |

### Evaluating an expression

To find X for a given set of inputs, replace each letter by its value and work from the innermost brackets outwards, one gate at a time.

:::eg Evaluate an expression
Find X for \(X = (A \text{ OR } B) \text{ AND NOT } C\) when A = 0, B = 1 and C = 0, and when A = 1, B = 0 and C = 1.

First case: \(A \text{ OR } B = 0 \text{ OR } 1 = 1\) and \(\text{NOT } C = \text{NOT } 0 = 1\), so \(X = 1 \text{ AND } 1 = 1\).

Second case: \(A \text{ OR } B = 1 \text{ OR } 0 = 1\) and \(\text{NOT } C = \text{NOT } 1 = 0\), so \(X = 1 \text{ AND } 0 = 0\).
:::

Other books write the gates as symbols: \(A \cdot B\) for AND, \(A + B\) for OR and a bar over a letter for NOT. In this course expressions use the gate names, as above. The symbols come back when you study Boolean algebra at A Level.

## From an expression to a circuit

To draw a circuit for an expression, find the **last** gate first and then work backwards to the inputs.

:::steps
1. Find the gate whose output is X. It is the gate that is not inside any bracket (apart from the whole expression). For `(A AND B) OR NOT C` it is the OR gate.
2. Its two inputs are the two parts either side of it. Here they are `(A AND B)` and `NOT C`.
3. A part that is a single letter is an input wire. A part that is a bracket or a NOT is another gate, so repeat step 2 for it.
4. Draw the circuit with the inputs on the left and X on the right. Use the exact gate symbols. Label every input and the output.
5. Where one input feeds two gates, draw a junction dot so it is clear that the wire is joined.
:::

:::html
<figure class="fig"><svg viewBox="0 0 430 175" role="img" aria-label="Logic circuit with inputs A, B and C and output X. A and B feed an AND gate whose output, labelled P, goes to an OR gate. C feeds a NOT gate whose output, labelled Q, goes to the other input of the OR gate. The OR gate output is X."><g transform="translate(110 35)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><g transform="translate(110 115)"><path class="fm s-acc sw2" d="M0 0 L28 20 L0 40 Z"/><circle class="fm s-acc sw2" cx="32" cy="20" r="4"/></g><g transform="translate(270 75)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/></g><text class="tl tb" x="12" y="49">A</text><text class="tl tb" x="12" y="69">B</text><text class="tl tb" x="12" y="139">C</text><polyline class="ln" fill="none" points="30,45 110,45"/><polyline class="ln" fill="none" points="30,65 110,65"/><polyline class="ln" fill="none" points="30,135 110,135"/><polyline class="ln" fill="none" points="150,55 210,55 210,85 274,85"/><polyline class="ln" fill="none" points="146,135 230,135 230,105 274,105"/><polyline class="ln" fill="none" points="312,95 362,95"/><text class="tl tb" x="368" y="99">X</text><text class="tl" x="172" y="47">P</text><text class="tl" x="172" y="152">Q</text></svg><figcaption>The circuit for X = (A AND B) OR NOT C. P and Q label the wires between the gates.</figcaption></figure>
:::

The figure follows the steps. The OR gate gives X. One of its inputs, P, is the output of an AND gate that takes A and B. The other input, Q, is the output of a NOT gate that takes C. These are the same P and Q as the working columns in the truth table above, which is why the table and the circuit match.

## From a circuit to an expression

To write the expression for a circuit, go the other way: start at the inputs and name every wire.

:::steps
1. Give each gate's output a label (P, Q, R, …), working from the left.
2. Write a short expression for each gate in terms of its input wires, for example \(P = A \text{ OR } B\).
3. Substitute these into the last gate's expression, from the left, until only A, B, C … and the gates remain.
4. Put brackets round each substituted part.
:::

:::html
<figure class="fig"><svg viewBox="0 0 420 175" role="img" aria-label="Logic circuit with inputs A and B and output X, built from four gates. A and B each go to an OR gate and to an AND gate. The OR output is labelled P. The AND output Q goes through a NOT gate, whose output is labelled R. P and R feed a second AND gate whose output is X. The wires from A and B cross without a dot where they are not joined."><g transform="translate(150 25)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/></g><g transform="translate(150 105)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><g transform="translate(220 105)"><path class="fm s-acc sw2" d="M0 0 L28 20 L0 40 Z"/><circle class="fm s-acc sw2" cx="32" cy="20" r="4"/></g><g transform="translate(310 65)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><text class="tl tb" x="12" y="39">A</text><text class="tl tb" x="12" y="139">B</text><polyline class="ln" fill="none" points="30,35 154,35"/><polyline class="ln" fill="none" points="30,135 150,135"/><polyline class="ln" fill="none" points="60,35 60,115 150,115"/><polyline class="ln" fill="none" points="80,135 80,55 154,55"/><circle class="fi" cx="60" cy="35" r="3.5"/><circle class="fi" cx="80" cy="135" r="3.5"/><polyline class="ln" fill="none" points="192,45 282,45 282,75 310,75"/><polyline class="ln" fill="none" points="190,125 220,125"/><polyline class="ln" fill="none" points="256,125 292,125 292,95 310,95"/><polyline class="ln" fill="none" points="350,85 400,85"/><text class="tl tb" x="406" y="89">X</text><text class="tl" x="212" y="38">P</text><text class="tl" x="200" y="142">Q</text><text class="tl" x="268" y="142">R</text></svg><figcaption>X = (A OR B) AND NOT (A AND B). Wires that cross without a dot are not joined.</figcaption></figure>
:::

:::eg Write the expression for a circuit, then complete its truth table
The figure shows a circuit with inputs A and B and output X. Write the logic expression for X, and complete the truth table.

Label the gate outputs. The OR gate takes A and B, so \(P = A \text{ OR } B\). The lower AND gate takes A and B, so \(Q = A \text{ AND } B\). The NOT gate inverts Q, so \(R = \text{NOT } Q\). The last AND gate takes P and R, so \(X = P \text{ AND } R\).

Substitute from the left. R becomes `NOT (A AND B)` and P becomes `(A OR B)`, so

\[ X = (A \text{ OR } B) \text{ AND NOT } (A \text{ AND } B). \]

| A | B | P = A OR B | Q = A AND B | R = NOT Q | X = P AND R |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

The X column, 0 1 1 0, is the truth table of an **XOR** gate. This circuit does the job of one XOR gate with four simpler gates: "at least one input is 1 (OR), but not both (NOT AND)".
:::

Look at the wires in the figure. A and B each go to two gates, so each has a dot where the wire splits. Two wires cross near the lower left of the figure without a dot. In a circuit diagram, **a dot means the wires are joined and no dot means they merely cross**.

## From a problem statement to a circuit

Real exam questions often describe a situation in words. Translate it in two steps: first say what each input and the output **means**, then turn the words into gates. The linking words give the gates away.

:::key Words to gates
| The statement says | Gate or part |
|---|---|
| "A and B", "both A and B" | A AND B |
| "A or B", "A or B or both", "either" | A OR B |
| "not A", "A is off" | NOT A |
| "A but not B", "A and not B" | A AND NOT B |
| "not both A and B" | A NAND B |
| "neither A nor B" | A NOR B |
| "A or B, but not both", "A and B are different" | A XOR B |
:::

:::eg A burglar alarm with three inputs
A shop in Kampala has an alarm. The alarm sounds (X = 1) when the shop door is open **and** the alarm is armed, **or** when the panic button is pressed. Write the logic expression, draw the circuit and complete a truth table.

Start by deciding what each input means.

| Input | Meaning when it is 1 | Meaning when it is 0 |
|---|---|---|
| A | the door is open | the door is closed |
| B | the alarm is armed | the alarm is off |
| C | the panic button is pressed | the button is not pressed |
| X | the alarm sounds | the alarm is silent |

"Open **and** armed" is `A AND B`. "**or** the panic button is pressed" joins that to C with OR. So \(X = (A \text{ AND } B) \text{ OR } C\).

:::html
<figure class="fig"><svg viewBox="0 0 380 125" role="img" aria-label="Logic circuit for a burglar alarm with inputs A, B and C and output X. A and B feed an AND gate. Its output and C feed an OR gate, whose output is X."><g transform="translate(100 35)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><g transform="translate(230 45)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/></g><text class="tl tb" x="12" y="49">A</text><text class="tl tb" x="12" y="69">B</text><text class="tl tb" x="12" y="104">C</text><polyline class="ln" fill="none" points="30,45 100,45"/><polyline class="ln" fill="none" points="30,65 100,65"/><polyline class="ln" fill="none" points="30,100 200,100 200,75 234,75"/><polyline class="ln" fill="none" points="140,55 234,55"/><polyline class="ln" fill="none" points="272,65 322,65"/><text class="tl tb" x="328" y="69">X</text></svg><figcaption>The alarm circuit X = (A AND B) OR C. A is the door sensor, B the arming switch and C the panic button.</figcaption></figure>
:::

| A | B | C | P = A AND B | X = P OR C |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 |

The alarm sounds in five of the eight rows: whenever C is 1, and also when the door is open and the alarm is armed with C = 0.
:::

:::eg A kiln controller (exam style)
A kiln for pottery in Nairobi has a heater. The heater is switched on (X = 1) only when the kiln is below the target temperature **and** the door is closed, **and** the overheat sensor is **not** triggered. Input A is 1 when the kiln is below the target temperature, input B is 1 when the door is closed and input C is 1 when the overheat sensor is triggered.

(a) Write a logic expression for X. [2 marks]

(b) Complete a truth table for the expression, with working columns. [3 marks]

(a) "Below the target and the door closed" is \(A \text{ AND } B\). "Not triggered" is NOT C. Join them with AND, because all three conditions must hold.

\[ X = (A \text{ AND } B) \text{ AND NOT } C \]

- `A AND B` as a bracketed part [B1]
- combined with `NOT C` using AND, with brackets that make the order clear [B1]

(b) Let \(P = A \text{ AND } B\) and \(Q = \text{NOT } C\), so \(X = P \text{ AND } Q\).

| A | B | C | P | Q | X |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

- all eight combinations of A, B and C, with no row missing or repeated [B1]
- working columns P and Q correct [B1]
- X column correct: 1 only when A = 1, B = 1 and C = 0 [B1]

The heater is on in exactly one row: the kiln is cold, the door is shut and nothing is overheating.
:::

## From a truth table to an expression

Sometimes you are given a truth table and must find an expression that produces it. There is a method that always works, and at AS Level you do not have to simplify the result.

:::key Truth table to expression (sum of products)
1. Look only at the rows where \(X = 1\).
2. For each of those rows, write a term that is 1 for that row and 0 for every other row: join the inputs with AND, and write **NOT** in front of every input that is **0** in the row.
3. Join the terms with OR.
:::

A term built this way is 1 only for its own row, because every input has to have the right value for the AND to give 1. The OR then lets any of the chosen rows switch X on.

:::eg Expression from a truth table
Find an expression for X from this truth table.

| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

X is 1 in two rows. Row 01 (A = 0, B = 1) gives the term `NOT A AND B`. Row 10 (A = 1, B = 0) gives `A AND NOT B`. Join them:

\[ X = (\text{NOT } A \text{ AND } B) \text{ OR } (A \text{ AND NOT } B) \]

This is the XOR function again, now built from AND, OR and NOT. An answer with this expression is correct at AS Level, even though one XOR gate does the same job.
:::

With three inputs, each term has three parts. Use brackets so that only two-input gates are needed.

:::eg Three inputs
Find an expression for X from this table, where X is 1 in rows 001, 100 and 110.

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Write one term for each row where X = 1, with NOT in front of every input that is 0:

- row 001: `(NOT A AND NOT B) AND C`
- row 100: `(A AND NOT B) AND NOT C`
- row 110: `(A AND B) AND NOT C`

\[
\begin{aligned}
X ={}& ((\text{NOT } A \text{ AND NOT } B) \text{ AND } C) \text{ OR } \\
& ((A \text{ AND NOT } B) \text{ AND NOT } C) \text{ OR } \\
& ((A \text{ AND } B) \text{ AND NOT } C)
\end{aligned}
\]

To check, try row 100: the second term is \((1 \text{ AND NOT } 0) \text{ AND NOT } 0 = 1\), so X = 1, which matches the table. Try a row with X = 0, such as 101: every term has a part that is 0, so X = 0.
:::

You can tidy such expressions. For example, the last two terms above combine into the single term `A AND NOT C`. Simplifying is a skill for Boolean algebra at A Level, so at AS Level the unsimplified answer earns full marks.

:::warn Truth-table slips
- Using the rows where X is **0** instead of the rows where X is **1**.
- Forgetting the NOT on an input that is 0 in the row.
- Writing the terms without brackets, so the order of the gates is unclear.
- Dropping a row in the table so that a term is missing: count the 1s in the X column and make sure you have that many terms.
:::

## Spot the error

:::eg Spot the error: a working column
Question: Complete the truth table for \(X = (A \text{ XOR } B) \text{ AND } C\). Use P as a working column for \(A \text{ XOR } B\). [3 marks]

A student wrote:

| A | B | C | P | X |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

The eight combinations of A, B and C are all present and in order [B1]. **The P column is wrong in the last two rows: when A and B are both 1, an XOR gate gives 0, but the student wrote 1, treating the gate as an OR** [B0]. The X column is the AND of the student's own P with C in every row, so it earns the mark by follow-through from the working column [B1]. The answer scores 2 out of 3.

The correct P column is 0, 0, 1, 1, 1, 1, 0, 0, and then X is 0, 0, 0, 1, 0, 1, 0, 0, so the last row should be 0, not 1. The lesson is to check each working column against the truth table of its gate, especially XOR in the row 11.
:::

:::try Start easy, finish at exam standard
Q: Give the output of each gate when A = 1 and B = 1: AND, OR, NAND, NOR and XOR.
A: AND gives 1, OR gives 1, NAND gives 0, NOR gives 0 and XOR gives 0.
Q: Name the gate whose output is 1 only when its two inputs are different.
A: XOR.
Q: How many rows does the truth table of a circuit with four inputs need? How many for five inputs?
A: \(2^4 = 16\) rows for four inputs, and \(2^5 = 32\) rows for five inputs.
Q: Find X for \(X = (A \text{ OR } B) \text{ AND NOT } C\) when A = 0, B = 1 and C = 0.
A: \(0 \text{ OR } 1 = 1\); \(\text{NOT } 0 = 1\); \(1 \text{ AND } 1 = 1\). So X = 1.
Q: Write an expression that is 1 only when A is 1 and B is 0.
A: `A AND NOT B`.
Q: Complete the truth table for \(X = \text{NOT } A \text{ OR } B\).
A: Remember that NOT applies to A only.

| A | B | NOT A | X |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 |

Q: Describe the circuit for \(X = \text{NOT } (A \text{ OR } B) \text{ AND } C\), using the gates AND, OR and NOT only.
A: An OR gate takes A and B. Its output goes into a NOT gate. The output of the NOT gate and C go into an AND gate, whose output is X. (The OR gate followed by NOT is the same as a NOR gate.)
Q: In the alarm circuit \(X = (A \text{ AND } B) \text{ OR } C\), how many of the eight rows give X = 1, and which input being 1 is enough on its own?
A: Five rows give X = 1. C being 1 is enough on its own, because OR gives 1 if either input is 1.
Q: Write an expression for "X is 1 only when neither A nor B is 1" and name the single gate that does the same job.
A: \(X = \text{NOT } (A \text{ OR } B)\). A single NOR gate does the same job.
Q: A student draws an OR gate with a small circle on its output. Which gate is it, and what is its output when A = 1 and B = 0?
A: It is a NOR gate. With A = 1 and B = 0 the OR output would be 1, and the circle inverts it, so the output is 0.
:::

Questions 2 and 3 of the exam practice refer to this circuit.

:::html
<figure class="fig"><svg viewBox="0 0 390 160" role="img" aria-label="Logic circuit with inputs A, B and C and output X. A and B feed a NAND gate. B and C feed a NOR gate. B is joined to both gates by a dot. The outputs of the NAND and the NOR gates feed an XOR gate whose output is X."><g transform="translate(110 30)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/><circle class="fm s-acc sw2" cx="44" cy="20" r="4"/></g><g transform="translate(110 100)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><g transform="translate(270 65)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><path class="ln" fill="none" d="M-6 0 C1 12 1 28 -6 40"/></g><text class="tl tb" x="12" y="44">A</text><text class="tl tb" x="12" y="89">B</text><text class="tl tb" x="12" y="134">C</text><polyline class="ln" fill="none" points="30,40 110,40"/><polyline class="ln" fill="none" points="30,85 70,85"/><polyline class="ln" fill="none" points="70,85 70,60 110,60"/><polyline class="ln" fill="none" points="70,85 70,110 114,110"/><circle class="fi" cx="70" cy="85" r="3.5"/><polyline class="ln" fill="none" points="30,130 114,130"/><polyline class="ln" fill="none" points="158,50 226,50 226,75 268,75"/><polyline class="ln" fill="none" points="160,120 246,120 246,95 268,95"/><polyline class="ln" fill="none" points="312,85 362,85"/><text class="tl tb" x="368" y="89">X</text></svg><figcaption>The circuit for exam practice questions 2 and 3. The dot on B shows that B is joined to both gates.</figcaption></figure>
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State the name of the logic gate that (a) gives an output of 1 only when both of its inputs are 0, and (b) gives an output of 1 only when its two inputs are different. [1] [1]
A: (a) NOR [B1] (b) XOR [B1]

Q: [3 marks] ★ Write the logic expression for the circuit in the figure above. The circuit has inputs A, B and C and output X.
H: Name the output of each of the first two gates, then say what the last gate does with them.
A: \(X = (A \text{ NAND } B) \text{ XOR } (B \text{ NOR } C)\)

- the NAND gate has inputs A and B: `A NAND B` [B1]
- the NOR gate has inputs B and C: `B NOR C` [B1]
- the XOR gate combines the two outputs to give X, with brackets [B1]

Q: [4 marks] ★★ (#cs.logic) Complete a truth table for the circuit in question 2, with a working column for the output of each of the first two gates.
H: Call the NAND output P and the NOR output Q, so that \(X = P \text{ XOR } Q\).
A: List all eight rows, then fill P, Q and X.

| A | B | C | P = A NAND B | Q = B NOR C | X = P XOR Q |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 |

- all eight input combinations present, with no repeats [B1]
- P column correct [B1]
- Q column correct [B1]
- X column correct [B1]

Q: [5 marks] ★★ A garden sprinkler in Lahore opens its valve (X = 1) when the soil is dry **and** it is **not** raining, **or** when the manual override switch is on. Input D is 1 when the soil is dry, input R is 1 when it is raining and input M is 1 when the override is on. (a) Write a logic expression for X. [2] (b) Describe the circuit that you would draw, using only AND, OR and NOT gates. [3]
H: "Dry and not raining" is a part by itself, so put it in a bracket.
A: (a) \(X = (D \text{ AND NOT } R) \text{ OR } M\)

- `D AND NOT R` in a bracket [B1]
- joined to M using OR [B1]

(b) The circuit has three gates:

- a NOT gate whose input is R [B1]
- an AND gate whose inputs are D and the output of the NOT gate [B1]
- an OR gate whose inputs are the output of the AND gate and M, and whose output is X [B1]

Q: [4 marks] ★★ The truth table shows the output X for three inputs A, B and C. X is 1 only in rows 010 and 111. Write a logic expression for X.

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

H: Use only the rows where X = 1, and put NOT in front of each input that is 0.
A: One possible answer:

\[ X = ((\text{NOT } A \text{ AND } B) \text{ AND NOT } C) \text{ OR } ((A \text{ AND } B) \text{ AND } C) \]

- term for row 010: `(NOT A AND B) AND NOT C` [B1]
- term for row 111: `(A AND B) AND C` [B1]
- the two terms joined with OR [B1]
- no term for a row where X = 0, and the brackets make the order of the gates clear [B1]

Q: [5 marks] ★★ A greenhouse fan in Manila runs (X = 1) when the temperature is high **or** the humidity is high, but not when the power-saver switch is on. Input A is 1 when the temperature is high, B is 1 when the humidity is high and C is 1 when the power-saver switch is on. (a) Write a logic expression for X. [2] (b) Complete a truth table with working columns. [3]
A: (a) \(X = (A \text{ OR } B) \text{ AND NOT } C\)

- `A OR B` as a bracketed part [B1]
- combined with `NOT C` using AND [B1]

(b) Let \(P = A \text{ OR } B\) and \(Q = \text{NOT } C\).

| A | B | C | P | Q | X |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

- all eight combinations of inputs [B1]
- working columns P and Q correct [B1]
- X column correct [B1]

Q: [5 marks] ★★★ A student says that the circuit \(X = (\text{NOT } A) \text{ OR } (\text{NOT } B)\) does the same job as a single NAND gate. Complete a truth table for the expression with working columns, add a column for \(A \text{ NAND } B\), and state whether the student is correct.
H: Use working columns for NOT A and NOT B.
A: The student is correct, as the table shows.

| A | B | NOT A | NOT B | (NOT A) OR (NOT B) | A NAND B |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |

- all four input combinations [B1]
- NOT A and NOT B columns correct [B1]
- the OR column correct (1, 1, 1, 0) [B1]
- the NAND column correct (1, 1, 1, 0) [B1]
- the columns are identical in every row, so the student is correct [B1]

Q: [6 marks] ★★★ A strongroom in Dhaka has three keys, A, B and C. The door opens (X = 1) only when **exactly two** of the three keys are turned. A key that is turned is 1. (a) Complete the X column of a truth table for all eight combinations. [2] (b) Write a logic expression for X. [4]
H: Part (a): exactly two 1s in the row means the rows 011, 101 and 110.
H: Part (b): one term for each row where X = 1.
A: (a) X = 1 in rows 011, 101 and 110, and 0 in the other five rows:

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

- all eight rows listed [B1]
- X column correct [B1]

(b) One possible answer:

\[
\begin{aligned}
X ={}& ((\text{NOT } A \text{ AND } B) \text{ AND } C) \text{ OR } \\
& ((A \text{ AND NOT } B) \text{ AND } C) \text{ OR } \\
& ((A \text{ AND } B) \text{ AND NOT } C)
\end{aligned}
\]

- term for row 011: `(NOT A AND B) AND C` [B1]
- term for row 101: `(A AND NOT B) AND C` [B1]
- term for row 110: `(A AND B) AND NOT C` [B1]
- the three terms joined with OR and no other terms [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A chip factory makes only NAND gates, because every other gate can be built from them. Show how to build (a) a NOT gate, (b) an AND gate and (c) an OR gate using NAND gates only, and show that each works. Name the inputs A and B, and use as many NAND gates as you need.
H: What does a NAND gate do when its two inputs are joined to the same wire?
H: An AND gate is a NAND gate followed by a NOT. An OR gate gives 1 when NOT A or NOT B is 1.
A: (a) Join both inputs of one NAND gate to A. The output is \(A \text{ NAND } A\): when A = 0 it is 1, and when A = 1 it is 0, which is NOT A.

(b) Feed A and B into a NAND gate, then join both inputs of a second NAND gate to its output. The first gate gives NOT (A AND B), and the second inverts it, giving \(A \text{ AND } B\).

(c) Use a NAND gate with both inputs joined to A, and another with both inputs joined to B. This makes NOT A and NOT B. Feed these into a third NAND gate. The output is \((\text{NOT } A) \text{ NAND } (\text{NOT } B)\). It is 0 only when NOT A and NOT B are both 1, which is when A and B are both 0, so it is \(A \text{ OR } B\).

- NOT: both inputs of a NAND gate joined to A [B1]
- explanation that this inverts the input (0 gives 1, 1 gives 0) [B1]
- AND: a NAND gate followed by a second NAND gate with its inputs joined [B1]
- explanation that the second gate inverts the NAND output [B1]
- OR: A and B each inverted by a NAND gate with joined inputs, then combined in a third NAND gate [B1]
- explanation that the output is 0 only when both A and B are 0 [B1]

Q: [5 marks] ★★★ A computer adds two single binary digits A and B. The result has two digits: a Sum digit and a Carry digit, as in \(1 + 1 = 10\). State which gate gives the Sum and which gives the Carry, and complete the truth table.
H: Write out the four additions 0 + 0, 0 + 1, 1 + 0 and 1 + 1 in binary.
A: Sum is \(A \text{ XOR } B\) and Carry is \(A \text{ AND } B\).

| A | B | Sum | Carry |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

- Sum is given by an XOR gate [B1]
- Carry is given by an AND gate [B1]
- Sum column correct (0, 1, 1, 0) [B1]
- Carry column correct (0, 0, 0, 1) [B1]
- the row 1, 1 shows \(1 + 1 = 10\): the digit is 0 and 1 is carried [B1]

(This pair of gates is called a half adder. It is the first step towards the adder circuits in the processor, which you will meet in [Boolean algebra and logic circuits](#cs.boolean) at A Level.)
:::

:::quiz
? What is the output of a NAND gate when both inputs are 1?
- 1
+ 0
- It depends on the gate that follows.
- 2
> NAND is the opposite of AND, and AND gives 1 when both inputs are 1, so NAND gives 0. NAND gives 1 in all the other three rows.
? Which gate gives an output of 1 only when its inputs are different?
- OR
- NOR
+ XOR
- NAND
> XOR is "exclusive OR": exactly one input must be 1. OR is also 1 when both inputs are 1, which is the case that XOR excludes.
? How many rows are in the truth table of a circuit with three inputs?
- 3
- 6
+ 8
- 9
> Each input doubles the number of rows, so three inputs give \(2^3 = 8\) rows. Counting 3 rows or 9 rows comes from adding or squaring instead of doubling.
? Which expression means "the NOT of A, then AND with B"?
+ `(NOT A) AND B`
- `NOT (A AND B)`
- `NOT A OR B`
- `A AND NOT B`
> NOT applies only to the item straight after it, so `NOT A AND B` is `(NOT A) AND B`. The second option inverts the whole AND, and the last swaps which input is inverted.
? What does the NOR gate output when A = 0 and B = 0?
- 0
+ 1
- 0 only if A is 1
- It has no output when both are 0.
> NOR is NOT OR: OR of 0 and 0 is 0, and NOT 0 is 1. NOR is 1 only in the first row.
? For \(X = (A \text{ AND } B) \text{ OR NOT } C\), what is X when A = 1, B = 0 and C = 0?
+ 1
- 0
- 1 only if B is 1
- It cannot be found without a truth table.
> \(A \text{ AND } B = 1 \text{ AND } 0 = 0\), but \(\text{NOT } C = \text{NOT } 0 = 1\), and \(0 \text{ OR } 1 = 1\). One input of an OR gate being 1 is enough.
? In a circuit diagram, what does a filled dot where two wires meet show?
- The wires cross but are not joined.
+ The wires are joined.
- A NOT gate.
- A fault in the circuit.
> A dot means that the wires are connected, so a signal on one is also on the other. Wires that merely cross have no dot.
? You are given a truth table and asked for an expression using the sum-of-products method. Which rows do you use?
- the rows where X = 0
+ the rows where X = 1
- every row
- only the first and last rows
> Each row where X is 1 gives a term that is 1 for that row only, and the terms are ORed together. Rows with X = 0 need no term, because the OR gives 0 when no term is 1.
:::

:::checklist What you can now do
- [ ] I can draw the symbols for NOT, AND, OR, NAND, NOR and XOR, and know that the circle on an output means NOT.
- [ ] I can define each gate in one sentence and write its truth table.
- [ ] I can complete a truth table for a circuit or expression with up to three inputs, with working columns and no missing rows.
- [ ] I can write a logic expression for a circuit by labelling the wires between the gates.
- [ ] I can draw a logic circuit for an expression, working from the last gate back to the inputs.
- [ ] I can turn a problem statement into an expression, saying what each input means.
- [ ] I can write an expression from a truth table using the rows where X = 1.
- [ ] I can say when a dot on a wire means "joined" and when crossing wires are not joined.
:::

:::recap
- A logic gate takes one or two binary inputs and gives one binary output. A truth table lists every input combination and the output for each. A circuit with \(n\) inputs has \(2^n\) rows, listed in binary counting order.
- NOT inverts. AND is 1 only if both inputs are 1. OR is 1 if at least one input is 1. NAND is NOT AND (0 only for 1, 1). NOR is NOT OR (1 only for 0, 0). XOR is 1 when the inputs differ.
- The small circle on a symbol means NOT. NAND is not "NOT A AND NOT B"; XOR gives 0 for 1, 1.
- Write expressions with the gate names and brackets round every gate that feeds another gate. NOT applies only to the next item.
- For a truth table, add a working column for the output of each gate and fill the columns from left to right.
- Circuit to expression: label each gate output P, Q, R and substitute. Expression to circuit: start from the last gate. A dot on a wire means joined; crossing without a dot does not.
- Problem statement to expression: say what each input means, then "and" is AND, "or" is OR, "not" is NOT, "neither … nor" is NOR.
- Truth table to expression: one AND term for each row where X = 1, with NOT before each input that is 0, joined with OR.
:::

:::links
- practise: [Logic gates and logic circuits: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/3-hardware-/logic-gates-and-logic-circuits/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- explore: [Logicly demo](https://logic.ly/demo/) · Logicly · build the circuits from this chapter by dragging gates onto a canvas
- explore: [Logic gate challenges](https://www.101computing.net/logic-gates-circuits/) · 101 Computing · build and test circuits from problem statements
- watch: [Craig 'n' Dave](https://www.youtube.com/@craigndave) · Craig 'n' Dave · A Level topic videos on logic gates and truth tables
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations of logic gates and circuits, with questions

Links checked 13 November 2026.
:::

Next: [Processor fundamentals and the fetch-execute cycle](#cs.processor)
