@chapter cs.boolean
@title Boolean algebra, Karnaugh maps, adders and flip-flops
@level a2
@paper CAIE 9618 Paper 3
@time 6–8 hours
@summary Boolean algebra and its laws (including De Morgan's laws), simplifying logic expressions by algebra and with Karnaugh maps, the half adder and full adder (and how full adders chain to add binary numbers), and the SR and JK flip-flops that store one bit.

:::why
Every processor is built from logic gates, and every gate costs money, space, time and power. Boolean algebra lets you take a circuit that works and rewrite it as a smaller circuit that gives exactly the same outputs. The same gates, joined in two special patterns, add binary numbers (adders) and remember a bit (flip-flops), so this chapter shows how the arithmetic unit and the registers of the [processor](#cs.processor) are made. Paper 3 asks you to simplify expressions, fill in Karnaugh maps, complete adder truth tables and describe flip-flops.
:::

**Before you start**, you should know the six gates, truth tables and how to write a logic expression from [Logic gates and logic circuits](#cs.logic), and binary addition from [Number systems and binary arithmetic](#cs.data).

:::try Warm-up
Q: What is the output of a NAND gate when A = 1 and B = 1? And for a NOR gate when A = 0 and B = 0? (from [Logic gates and logic circuits](#cs.logic))
A: NAND gives 0 (NOT of 1 AND 1). NOR gives 1 (NOT of 0 OR 0).
Q: Write an expression, using AND, OR and NOT, for the truth table where X = 1 only in the rows A = 0, B = 1 and A = 1, B = 0. (from [Logic gates and logic circuits](#cs.logic))
A: Take one term for each row where X = 1: \(X = (\text{NOT } A \text{ AND } B) \text{ OR } (A \text{ AND NOT } B)\). This is the XOR function.
Q: Add the binary numbers 0101 and 0011. (from [Number systems and binary arithmetic](#cs.data))
A: Work from the right with carries: 0101 + 0011 = 1000 (that is \(5 + 3 = 8\)).
:::

## Boolean algebra: writing logic as algebra

You already write logic as words: `X = (A AND B) OR NOT C`. **Boolean algebra** is the same thing written with symbols, plus a set of laws that tell you which rewrites are safe. It works with only two values, 0 and 1, so every law can be proved by a truth table.

:::def Boolean algebra
A branch of algebra in which every variable has one of two values, 0 or 1 (false or true), and the operations are AND, OR and NOT. Its laws allow an expression to be rewritten in a simpler form that gives the same output for every combination of inputs.
:::

In this chapter the operations are written in two ways. Learn to move between them without thinking.

| In words (as in the logic chapter) | In Boolean algebra | Meaning |
|---|---|---|
| `A AND B` | \(A \cdot B\) | 1 only when both are 1 |
| `A OR B` | \(A + B\) | 1 when at least one is 1 |
| `NOT A` | \(\text{NOT } A\) | the opposite of A |

Many textbooks and past papers write NOT with a bar over the letter, or as A′ or ¬A. They all mean NOT. This course writes \(\text{NOT } A\) so that every line prints clearly. In your own handwriting, use the form your teacher uses.

:::warn The plus sign is OR, not addition
In Boolean algebra \(1 + 1 = 1\), because "1 OR 1" is 1. The product \(A \cdot B\) is AND, so it can only be 0 or 1 as well. Never carry a digit: nothing in Boolean algebra is bigger than 1. (The adders later in this chapter do the real addition, using the XOR gate for the sum digit.)
:::

The three operations have an order, like multiplication and addition in arithmetic. **NOT** applies first, then **AND** (\(\cdot\)), then **OR** (\(+\)). Brackets override the order.

:::key Order of operations
1. Brackets first.
2. NOT, which applies only to the one item after it (or to a whole bracket).
3. AND (\(\cdot\)).
4. OR (\(+\)).

So \(A + B \cdot C\) means \(A + (B \cdot C)\), and \(\text{NOT } A \cdot B\) means \((\text{NOT } A) \cdot B\), which is not the same as \(\text{NOT}(A \cdot B)\).
:::

Two input rows are enough to see the order matter. Take \(A = 1\), \(B = 0\), \(C = 0\). Then \(A + B \cdot C = 1 + 0 = 1\), but \((A + B) \cdot C = 1 \cdot 0 = 0\).

## The laws of Boolean algebra

Each law below is true for every value of its variables. You can prove any of them by writing out the truth table of both sides and seeing the columns match. The laws come in pairs: swap AND with OR, and 0 with 1, and one form of a law turns into the other.

:::key The laws of Boolean algebra
| Law | AND form | OR form |
|---|---|---|
| Identity | \(A \cdot 1 = A\) | \(A + 0 = A\) |
| Null (domination) | \(A \cdot 0 = 0\) | \(A + 1 = 1\) |
| Idempotent | \(A \cdot A = A\) | \(A + A = A\) |
| Complement | \(A \cdot \text{NOT } A = 0\) | \(A + \text{NOT } A = 1\) |
| Double complement | \(\text{NOT}(\text{NOT } A) = A\) | (one form only) |
| Commutative | \(A \cdot B = B \cdot A\) | \(A + B = B + A\) |
| Associative | \((A \cdot B) \cdot C = A \cdot (B \cdot C)\) | \((A + B) + C = A + (B + C)\) |
| Distributive | \(A \cdot (B + C) = A \cdot B + A \cdot C\) | \(A + B \cdot C = (A + B) \cdot (A + C)\) |
| Absorption | \(A \cdot (A + B) = A\) | \(A + A \cdot B = A\) |
| De Morgan's | \(\text{NOT}(A \cdot B) = \text{NOT } A + \text{NOT } B\) | \(\text{NOT}(A + B) = \text{NOT } A \cdot \text{NOT } B\) |
:::

Some of these you would guess. The two that surprise most students are the OR form of the distributive law (OR also distributes over AND, which ordinary algebra does not allow) and absorption. Check absorption with a truth table, since it is the law you will use most.

| A | B | \(A \cdot B\) | \(A + A \cdot B\) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

The last column is identical to the column for A, so \(A + A \cdot B = A\). In words: if A is already 1, adding "A AND B" changes nothing; if A is 0, then "A AND B" is 0 as well. The extra term is absorbed.

The distributive law \(A \cdot (B + C) = A \cdot B + A \cdot C\) is how you factorise: it works backwards too. In \(A \cdot B + A \cdot \text{NOT } B\), the common factor A comes out, leaving \(A \cdot (B + \text{NOT } B)\). That one move starts most simplifications.

:::eg Check the OR form of the distributive law with a truth table
Show that \(A + B \cdot C = (A + B) \cdot (A + C)\) for every input. [4 marks]

Three variables give eight rows. Work out each side separately.

| A | B | C | \(B \cdot C\) | \(A + B \cdot C\) | \(A + B\) | \(A + C\) | \((A + B) \cdot (A + C)\) |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

- all eight input combinations listed [B1]
- \(B \cdot C\) and \(A + B \cdot C\) correct in every row [B1]
- \(A + B\), \(A + C\) and their product correct in every row [B1]
- the two result columns are identical, so the law holds [B1]
:::

## De Morgan's laws

De Morgan's laws tell you how NOT passes through a bracket. They are the most examined laws in this topic, and they explain why NAND and NOR gates exist.

:::def De Morgan's laws
Two laws: NOT(A AND B) = NOT A OR NOT B, and NOT(A OR B) = NOT A AND NOT B. The NOT of a whole bracket is found by applying NOT to each item, and swapping AND with OR.
:::

In algebra: \(\text{NOT}(A \cdot B) = \text{NOT } A + \text{NOT } B\) and \(\text{NOT}(A + B) = \text{NOT } A \cdot \text{NOT } B\). A memory aid: **break the bracket, change the sign** (AND becomes OR, OR becomes AND), and put a NOT on each part.

| A | B | NOT(A AND B) | NOT A OR NOT B | NOT(A OR B) | NOT A AND NOT B |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 |

Columns 3 and 4 match, and columns 5 and 6 match. The first law says that NAND is the same as "NOT A OR NOT B". The second says that NOR is the same as "NOT A AND NOT B". Each gate is therefore two different circuits that give the same truth table.

The laws extend to more variables, one step at a time. \(\text{NOT}(A \cdot B \cdot C) = \text{NOT } A + \text{NOT } B + \text{NOT } C\), and each NOT on a variable that is already inverted cancels by the double complement law.

:::eg Apply De Morgan's law
Write \(X = \text{NOT}(\text{NOT } A \cdot B)\) without a NOT over a bracket, and simplify. [3 marks]

\[
\begin{aligned}
X &= \text{NOT}(\text{NOT } A \cdot B) \\
  &= \text{NOT}(\text{NOT } A) + \text{NOT } B \quad \text{(De Morgan's law: break the bracket, change AND to OR)} \\
  &= A + \text{NOT } B \quad \text{(double complement)}
\end{aligned}
\]

- De Morgan's law applied, giving \(\text{NOT}(\text{NOT } A) + \text{NOT } B\) [B1]
- the sign changed from AND to OR [B1]
- the double complement removed, giving \(A + \text{NOT } B\) [B1]
:::

:::warn Common De Morgan mistakes
- Changing the NOT but **not** the AND or OR: \(\text{NOT}(A \cdot B) = \text{NOT } A \cdot \text{NOT } B\) is wrong. It is true for NOR, not NAND.
- Putting a NOT on only one part: \(\text{NOT}(A + B) = \text{NOT } A + B\) is wrong.
- Forgetting that a NOT already on a variable cancels with the new one.
:::

### NAND and NOR are universal gates

De Morgan's laws have a practical use. Any logic circuit can be built from **NAND gates alone**, or from NOR gates alone. A factory that makes only one kind of gate can build everything, which is cheap and reliable.

- NOT from NAND: \(A \text{ NAND } A = \text{NOT}(A \cdot A) = \text{NOT } A\), by the idempotent law.
- AND from NAND: \(\text{NOT}(A \text{ NAND } B)\) is \(A \cdot B\), so put a NAND-made NOT on the output.
- OR from NAND: \(\text{NOT } A \text{ NAND NOT } B = \text{NOT}(\text{NOT } A \cdot \text{NOT } B) = A + B\), by De Morgan's law and the double complement.

## Simplifying expressions with Boolean algebra

A circuit built directly from a truth table is usually much bigger than it needs to be. Simplifying means finding an equivalent expression with fewer terms and fewer gates. The plan is the same every time.

:::steps
1. Look for a common factor and take it out (distributive law).
2. Look for a variable and its opposite in the same bracket: \(A + \text{NOT } A = 1\) or \(A \cdot \text{NOT } A = 0\) (complement law).
3. Remove 1s and 0s (identity and null laws), and repeated terms (idempotent law).
4. Look for a short term that absorbs a longer one (absorption law).
5. Apply De Morgan's law to any NOT over a bracket first, so every NOT sits on a single variable.
6. Stop when no law makes the expression shorter.
:::

Write one step per line and name the law on every line. Examiners give a mark per law used correctly, so an unlabelled line risks the mark.

:::eg A first simplification
Simplify \(X = A \cdot B + A \cdot \text{NOT } B\), naming each law. [3 marks]

\[
\begin{aligned}
X &= A \cdot B + A \cdot \text{NOT } B \\
  &= A \cdot (B + \text{NOT } B) \quad \text{(distributive law: A is the common factor)} \\
  &= A \cdot 1 \quad \text{(complement law)} \\
  &= A \quad \text{(identity law)}
\end{aligned}
\]

- common factor A taken out, giving \(A \cdot (B + \text{NOT } B)\) [B1]
- \(B + \text{NOT } B = 1\) by the complement law [B1]
- \(A \cdot 1 = A\) by the identity law [B1]

So the circuit's output is simply A, and no gates are needed at all.
:::

:::eg Absorption and the complement law together
Simplify \(X = A \cdot B + A \cdot B \cdot C + \text{NOT } A \cdot B\). [4 marks]

\[
\begin{aligned}
X &= A \cdot B + A \cdot B \cdot C + \text{NOT } A \cdot B \\
  &= A \cdot B + \text{NOT } A \cdot B \quad \text{(absorption: } A \cdot B + A \cdot B \cdot C = A \cdot B \text{)} \\
  &= B \cdot (A + \text{NOT } A) \quad \text{(distributive law: B is the common factor)} \\
  &= B \cdot 1 \quad \text{(complement law)} \\
  &= B \quad \text{(identity law)}
\end{aligned}
\]

- absorption used to remove \(A \cdot B \cdot C\) [B1]
- B taken out as a common factor [B1]
- complement law, \(A + \text{NOT } A = 1\) [B1]
- identity law, giving \(X = B\) [B1]
:::

:::eg Using De Morgan's laws first
Simplify \(X = \text{NOT}(A + B) + \text{NOT}(A \cdot B)\). [4 marks]

\[
\begin{aligned}
X &= \text{NOT}(A + B) + \text{NOT}(A \cdot B) \\
  &= \text{NOT } A \cdot \text{NOT } B + (\text{NOT } A + \text{NOT } B) \quad \text{(De Morgan's laws on both brackets)} \\
  &= (\text{NOT } A + \text{NOT } A \cdot \text{NOT } B) + \text{NOT } B \quad \text{(commutative and associative laws: regroup)} \\
  &= \text{NOT } A + \text{NOT } B \quad \text{(absorption: } \text{NOT } A + \text{NOT } A \cdot \text{NOT } B = \text{NOT } A \text{)}
\end{aligned}
\]

- De Morgan's law applied to \(\text{NOT}(A + B)\) [B1]
- De Morgan's law applied to \(\text{NOT}(A \cdot B)\) [B1]
- terms regrouped so that \(\text{NOT } A\) and \(\text{NOT } A \cdot \text{NOT } B\) are together [B1]
- absorption used, giving \(\text{NOT } A + \text{NOT } B\) [B1]

This is the NAND function: \(\text{NOT } A + \text{NOT } B = \text{NOT}(A \cdot B)\). The simplified circuit is one NAND gate instead of a NOR, a NAND, an OR and several NOT gates.
:::

A very useful result, which you can prove with the laws and then use as a shortcut, is \(A + \text{NOT } A \cdot B = A + B\).

:::proof examinable A useful shortcut: A + NOT A · B = A + B
\[
\begin{aligned}
A + \text{NOT } A \cdot B &= (A + \text{NOT } A) \cdot (A + B) \quad \text{(distributive law, OR form)} \\
  &= 1 \cdot (A + B) \quad \text{(complement law)} \\
  &= A + B \quad \text{(identity law)}
\end{aligned}
\]
The shortcut says that "A OR (NOT A AND B)" is just "A OR B": if A is 0, then NOT A is 1 and the term reduces to B. Its dual form is \(A \cdot (\text{NOT } A + B) = A \cdot B\).
:::

### Checking a simplification by computer

A simplification is only correct if the two expressions give the same output for **every** input. With three variables there are only eight inputs, so a short program can test them all. This is the same idea as comparing two truth-table columns. In Python, `and`, `or` and `not` are the AND, OR and NOT operators, and `product` from the `itertools` module produces every combination of inputs.

The program below tests one simplification. By the shortcut above, \(A \cdot B + A \cdot \text{NOT } B \cdot C = A \cdot (B + \text{NOT } B \cdot C) = A \cdot (B + C)\). Does the shorter expression really match the longer one?

```python
from itertools import product

def original(a, b, c):
    return (a and b) or (a and not b and c)

def simplified(a, b, c):
    return a and (b or c)

same = True
for a, b, c in product([False, True], repeat=3):
    if original(a, b, c) != simplified(a, b, c):
        same = False
        print("different at", int(a), int(b), int(c))
print("Same truth table:", same)
```

Output:

```output
Same truth table: True
```

If you made an algebra slip, the program would name an input where the two expressions disagree, which is also where to look for the mistake.

### From a truth table: sum of products, then simplify

In [Logic gates and logic circuits](#cs.logic) you wrote an expression for a truth table by taking one AND term for each row where X is 1. That form has a name.

:::def Sum of products
A Boolean expression written as an OR of AND terms (products), for example \(A \cdot B + \text{NOT } A \cdot C\). A sum of products can be written directly from a truth table by making one product for each row where the output is 1, with NOT on every variable that is 0 in that row.
:::

:::eg From a truth table to a simplified expression
A circuit has inputs A, B and C. Its output X is 1 for the input rows 011, 100, 101 and 111, and 0 for all other rows. Write X as a sum of products and simplify it. [5 marks]

Each row where X = 1 gives one product, with NOT on every variable that is 0 in the row:

| A | B | C | X | Product for the row |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | |
| 0 | 0 | 1 | 0 | |
| 0 | 1 | 0 | 0 | |
| 0 | 1 | 1 | 1 | \(\text{NOT } A \cdot B \cdot C\) |
| 1 | 0 | 0 | 1 | \(A \cdot \text{NOT } B \cdot \text{NOT } C\) |
| 1 | 0 | 1 | 1 | \(A \cdot \text{NOT } B \cdot C\) |
| 1 | 1 | 0 | 0 | |
| 1 | 1 | 1 | 1 | \(A \cdot B \cdot C\) |

\[
\begin{aligned}
X &= \text{NOT } A \cdot B \cdot C + A \cdot \text{NOT } B \cdot \text{NOT } C + A \cdot \text{NOT } B \cdot C + A \cdot B \cdot C \\
  &= (A \cdot \text{NOT } B \cdot \text{NOT } C + A \cdot \text{NOT } B \cdot C) + (\text{NOT } A \cdot B \cdot C + A \cdot B \cdot C) \quad \text{(commutative and associative laws: regroup)} \\
  &= A \cdot \text{NOT } B \cdot (\text{NOT } C + C) + B \cdot C \cdot (\text{NOT } A + A) \quad \text{(distributive law: common factors)} \\
  &= A \cdot \text{NOT } B \cdot 1 + B \cdot C \cdot 1 \quad \text{(complement law)} \\
  &= A \cdot \text{NOT } B + B \cdot C \quad \text{(identity law)}
\end{aligned}
\]

- four products written, one for each row where X = 1 [B1]
- terms paired so that each pair differs in one variable [B1]
- common factors taken out [B1]
- complement law used on \(\text{NOT } C + C\) and \(\text{NOT } A + A\) [B1]
- final answer \(X = A \cdot \text{NOT } B + B \cdot C\) [B1]

The four-product circuit needed four 3-input AND gates, one 4-input OR gate and several NOT gates. The simplified circuit needs two 2-input AND gates, one 2-input OR gate and one NOT gate. The two circuits give the same output for all eight inputs.
:::

Keep this example. The Karnaugh map in a later section solves the same problem in a few seconds, and gives the same answer.

## Half adders and full adders

A computer adds numbers with logic gates. Start with the smallest case: adding two single bits. The four possible sums are \(0 + 0 = 0\), \(0 + 1 = 1\), \(1 + 0 = 1\) and \(1 + 1 = 10\) (two in binary). The result needs two digits, a **sum** digit and a **carry** digit.

:::def Half adder
A logic circuit that adds two single binary digits, A and B, and gives two outputs: a sum S and a carry C. S = A XOR B and C = A AND B.
:::

| A | B | S (sum) | C (carry) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

:::html
<figure class="fig small"><svg viewBox="0 0 345 160" role="img" aria-label="A half adder. Inputs A and B each go to two gates. An XOR gate gives the sum S, and an AND gate gives the carry C. S = A XOR B and C = A AND B."><g transform="translate(150 25)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><path class="ln" fill="none" d="M-6 0 C1 12 1 28 -6 40"/></g><g transform="translate(150 95)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><text class="tl" x="14" y="39">A</text><polyline class="ln" fill="none" points="30,35 148,35"/><polyline class="ln" fill="none" points="60,35 60,105 150,105"/><circle class="fi" cx="60" cy="35" r="3"/><text class="tl" x="14" y="129">B</text><polyline class="ln" fill="none" points="30,125 150,125"/><polyline class="ln" fill="none" points="90,125 90,55 148,55"/><circle class="fi" cx="90" cy="125" r="3"/><polyline class="ln" fill="none" points="192,45 240,45"/><text class="tl" x="248" y="49">S = A XOR B</text><polyline class="ln" fill="none" points="190,115 240,115"/><text class="tl" x="248" y="119">C = A AND B</text></svg><figcaption>A half adder: one XOR gate and one AND gate share the inputs A and B. The XOR output is the sum S; the AND output is the carry C.</figcaption></figure>
:::

A half adder is enough for the right-hand column of a sum, but it cannot add a **carry in** from the column before. Every other column has three bits to add: A, B and the carry from the previous column. That needs a full adder.

:::def Full adder
A logic circuit that adds three single binary digits: two input bits A and B and a carry in Cin. It gives a sum S and a carry out Cout. It can be built from two half adders and an OR gate.
:::

The full adder is built in two stages. The first half adder adds A and B. The second half adder adds the first sum to the carry in. The carry out is 1 if either half adder produced a carry (they can never both do so, which is why a plain OR gate is enough).

:::html
<figure class="fig"><svg viewBox="0 0 590 170" role="img" aria-label="A full adder built from two half adders and an OR gate. Half adder 1 adds A and B, giving a partial sum and a first carry. Half adder 2 adds that partial sum to the carry in Cin, giving the final Sum. The OR gate combines the two carries into Cout."><text class="tl" x="14" y="14">Cin</text><polyline class="ln" fill="none" points="40,10 270,10 270,40 290,40"/><text class="tl" x="14" y="44">A</text><polyline class="ln" fill="none" points="30,40 90,40"/><text class="tl" x="14" y="74">B</text><polyline class="ln" fill="none" points="30,70 90,70"/><rect class="fm s-acc sw2" x="90" y="25" width="100" height="60"/><rect class="fm s-acc sw2" x="290" y="25" width="100" height="60"/><text class="tl tc" x="140" y="49">Half</text><text class="tl tc" x="140" y="70">adder</text><text class="tl tc" x="340" y="49">Half</text><text class="tl tc" x="340" y="70">adder</text><text class="tl" x="96" y="44">A</text><text class="tl" x="96" y="74">B</text><text class="tl te" x="184" y="44">S</text><text class="tl te" x="184" y="74">C</text><text class="tl" x="296" y="44">A</text><text class="tl" x="296" y="74">B</text><text class="tl te" x="384" y="44">S</text><text class="tl te" x="384" y="74">C</text><polyline class="ln" fill="none" points="190,40 232,40 232,70 290,70"/><polyline class="ln" fill="none" points="190,70 205,70 205,130 474,130"/><polyline class="ln" fill="none" points="390,40 530,40"/><text class="tl" x="536" y="44">Sum</text><polyline class="ln" fill="none" points="390,70 430,70 430,110 474,110"/><g transform="translate(470 100)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/></g><polyline class="ln" fill="none" points="512,120 530,120"/><text class="tl" x="536" y="124">Cout</text></svg><figcaption>A full adder: half adder 1 adds A and B; half adder 2 adds its sum to the carry in; an OR gate joins the two carries to give the carry out.</figcaption></figure>
:::

Here is the truth table, with the working columns so that you can follow each half adder. S1 and C1 are the outputs of half adder 1; C2 is the carry from half adder 2.

| A | B | Cin | S1 (A XOR B) | C1 (A AND B) | S (S1 XOR Cin) | C2 (S1 AND Cin) | Cout (C1 OR C2) |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |

Read the last two columns as the full adder's truth table. The sum S is 1 when an odd number of the three inputs are 1 (one or three of them), and Cout is 1 when two or three of the inputs are 1. Check the row \(1 + 1 + 1\): the total is three, which is binary 11, so the sum digit is 1 and the carry is 1.

:::key Full adder expressions
- \(S = A \text{ XOR } B \text{ XOR } \text{Cin}\)
- \(\text{Cout} = A \cdot B + \text{Cin} \cdot (A \text{ XOR } B)\), which simplifies to \(A \cdot B + B \cdot \text{Cin} + A \cdot \text{Cin}\)
:::

### Adding whole numbers: the ripple-carry adder

To add two 4-bit numbers, use four full adders in a row, one for each bit position. The carry out of each adder is the carry in of the adder on its left. The carry ripples from the right-hand end to the left. The adder for the rightmost bit has no carry to receive, so its carry in is 0 (a half adder would do that job).

:::html
<figure class="fig"><svg viewBox="0 0 600 150" role="img" aria-label="Four full adders chained to add two 4-bit numbers. Each box adds one bit position. Its carry out goes to the carry in of the box on its left. The carry into the rightmost box is 0, and the leftmost box gives the final carry out."><rect class="fm s-acc sw2" x="70" y="45" width="90" height="50"/><text class="tl tc" x="115" y="74">Full adder</text><text class="tl tc" x="92" y="14">A3</text><text class="tl tc" x="138" y="14">B3</text><polyline class="ln" fill="none" points="92,22 92,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="138,22 138,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="115,95 115,118" marker-end="url(#ah)"/><text class="tl tc" x="115" y="136">S3</text><rect class="fm s-acc sw2" x="200" y="45" width="90" height="50"/><text class="tl tc" x="245" y="74">Full adder</text><text class="tl tc" x="222" y="14">A2</text><text class="tl tc" x="268" y="14">B2</text><polyline class="ln" fill="none" points="222,22 222,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="268,22 268,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="245,95 245,118" marker-end="url(#ah)"/><text class="tl tc" x="245" y="136">S2</text><rect class="fm s-acc sw2" x="330" y="45" width="90" height="50"/><text class="tl tc" x="375" y="74">Full adder</text><text class="tl tc" x="352" y="14">A1</text><text class="tl tc" x="398" y="14">B1</text><polyline class="ln" fill="none" points="352,22 352,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="398,22 398,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="375,95 375,118" marker-end="url(#ah)"/><text class="tl tc" x="375" y="136">S1</text><rect class="fm s-acc sw2" x="460" y="45" width="90" height="50"/><text class="tl tc" x="505" y="74">Full adder</text><text class="tl tc" x="482" y="14">A0</text><text class="tl tc" x="528" y="14">B0</text><polyline class="ln" fill="none" points="482,22 482,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="528,22 528,45" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="505,95 505,118" marker-end="url(#ah)"/><text class="tl tc" x="505" y="136">S0</text><polyline class="ln" fill="none" points="200,70 160,70" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="330,70 290,70" marker-end="url(#ah)"/><polyline class="ln" fill="none" points="460,70 420,70" marker-end="url(#ah)"/><text class="tl tc" x="180" y="62">C3</text><text class="tl tc" x="310" y="62">C2</text><text class="tl tc" x="440" y="62">C1</text><polyline class="ln" fill="none" points="70,70 45,70" marker-end="url(#ah)"/><text class="tl" x="8" y="74">Cout</text><polyline class="ln" fill="none" points="580,70 550,70" marker-end="url(#ah)"/><text class="tl" x="588" y="74">0</text></svg><figcaption>A ripple-carry adder: four full adders in a row for bits 3 to 0, with the carry passed from each adder to the next on its left.</figcaption></figure>
:::

:::eg Adding 0110 and 0111 through four full adders
Show the inputs and outputs of each full adder when 0110 (6) and 0111 (7) are added. [4 marks]

Start at bit 0, on the right. Each row uses the carry from the row above.

| Bit | A | B | Cin | S | Cout |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 1 | 1 | 1 |
| 3 | 0 | 0 | 1 | 1 | 0 |

The sum bits, from bit 3 down to bit 0, are 1, 1, 0, 1, so the result is 1101, which is 13 in denary. The final carry out is 0, so the result fits in four bits.

- bit 0 stage: inputs 0, 1 and carry in 0 give S = 1, Cout = 0 [B1]
- bit 1 stage: inputs 1, 1 and the carry 0 give S = 0, Cout = 1 [B1]
- bits 2 and 3 stages use the carry from the stage before, giving sums 1 and 1 [B1]
- result 1101 (13), with a final carry out of 0 [B1]
:::

If the final carry out is 1, the answer has overflowed: it needs one more bit than the adder has. A processor sets a flag when this happens. The ripple-carry design is simple, but each stage must wait for the carry from the stage before it, so a wider adder is slower.

The same truth-table method works for any circuit. The syllabus says that **gates may have more than two inputs** in these questions: a 3-input AND gives 1 only if all three inputs are 1, and a 3-input OR gives 1 if at least one input is 1. Complete such truth tables with working columns, as in the full adder.

## Flip-flops: circuits that remember

Every circuit so far is **combinational**: its output depends only on its inputs at that moment. A computer also needs to remember bits, for a register, a cache or a stored result. For that you need a circuit whose output depends on what happened before. The simplest such circuit is a flip-flop.

:::def Flip-flop
A logic circuit with two stable states that stores one bit of data. It keeps its output until its inputs make it change, and it holds the bit for as long as it has power.
:::

### The SR flip-flop

The **SR flip-flop** has two inputs, S (set) and R (reset), and two outputs, Q and NOT Q. It is made from two NOR gates, with the output of each gate fed back as an input to the other.

:::def SR flip-flop
A flip-flop with a set input S and a reset input R. Setting S to 1 makes Q = 1 (set). Setting R to 1 makes Q = 0 (reset). With both inputs 0 it keeps its stored bit. S and R must never both be 1.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 355 205" role="img" aria-label="An SR flip-flop made from two NOR gates joined in a loop. Input R goes to the top NOR gate, whose output is Q. Input S goes to the bottom NOR gate, whose output is NOT Q. Each output also feeds the other gate."><g transform="translate(150 30)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><g transform="translate(150 120)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><text class="tl" x="14" y="44">R</text><polyline class="ln" fill="none" points="30,40 154,40"/><text class="tl" x="14" y="164">S</text><polyline class="ln" fill="none" points="30,160 154,160"/><polyline class="ln" fill="none" points="200,50 300,50"/><text class="tl" x="306" y="54">Q</text><polyline class="ln" fill="none" points="200,140 300,140"/><text class="tl" x="306" y="144">NOT Q</text><polyline class="ln" fill="none" points="270,50 270,95 130,95 130,130 154,130"/><circle class="fi" cx="270" cy="50" r="3"/><polyline class="ln" fill="none" points="255,140 255,110 140,110 140,60 154,60"/><circle class="fi" cx="255" cy="140" r="3"/></svg><figcaption>An SR flip-flop from two cross-coupled NOR gates. The output of each gate is fed back to an input of the other.</figcaption></figure>
:::

Follow the circuit as the inputs change. Remember that a NOR gate gives 1 only when both its inputs are 0. The top gate has inputs R and NOT Q and gives Q. The bottom gate has inputs S and Q and gives NOT Q.

- **Set, S = 1 and R = 0.** The bottom gate has an input of 1, so NOT Q = 0. The top gate now has inputs R = 0 and NOT Q = 0, so Q = 1. The flip-flop is set.
- **Hold, S = 0 and R = 0**, after the set. The bottom gate has inputs 0 and Q = 1, so NOT Q stays 0, and the top gate keeps Q = 1. The loop holds the value, which is the memory.
- **Reset, S = 0 and R = 1.** The top gate has an input of 1, so Q = 0. The bottom gate now has inputs S = 0 and Q = 0, so NOT Q = 1. The flip-flop is reset.
- **Invalid, S = 1 and R = 1.** Both gates have an input of 1, so both outputs are 0. That breaks the rule that Q and NOT Q are opposites, and when the inputs return to 0 together, which output wins is unpredictable.

| S | R | Q (after) | NOT Q (after) | State |
|---|---|---|---|---|
| 0 | 0 | unchanged | unchanged | no change (the bit is stored) |
| 1 | 0 | 1 | 0 | set |
| 0 | 1 | 0 | 1 | reset |
| 1 | 1 | 0 | 0 | invalid: must not be used |

This table is for the NOR version. A flip-flop built from NAND gates works with inverted inputs (its "no change" row is S = 1, R = 1 and its invalid row is S = 0, R = 0), so check which gates a question uses before you answer.

Here is a sequence of inputs, starting with Q = 0. Each row shows the outputs after the gates have settled.

| Step | S | R | Q | NOT Q | What happened |
|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 1 | holds the stored 0 |
| 2 | 1 | 0 | 1 | 0 | set |
| 3 | 0 | 0 | 1 | 0 | holds the stored 1 |
| 4 | 0 | 1 | 0 | 1 | reset |
| 5 | 0 | 0 | 0 | 1 | holds the stored 0 |
| 6 | 1 | 1 | 0 | 0 | invalid |

Steps 3 and 5 are the important ones. The inputs are the same (0 and 0), but the outputs are different, because the circuit remembers what came before. That is why one flip-flop stores one bit.

### The JK flip-flop

The SR flip-flop has two weaknesses. It has an invalid input, and its output can change at any moment an input changes, which makes it hard to coordinate with the rest of a computer. The **JK flip-flop** fixes both.

:::def JK flip-flop
A clocked flip-flop with inputs J and K and outputs Q and NOT Q. J = 1 with K = 0 sets Q to 1; J = 0 with K = 1 resets Q to 0; J = K = 0 keeps Q; and J = K = 1 toggles Q to the opposite value. It has no invalid input.
:::

It is an SR flip-flop with two 3-input AND gates in front. A **clock** input, CLK, is an input to both AND gates.

:::html
<figure class="fig small"><svg viewBox="0 0 355 215" role="img" aria-label="A JK flip-flop built from an SR flip-flop of two NOR gates with two 3-input AND gates in front. The top AND gate takes Q, K and the clock CLK and feeds the top NOR gate, whose output is Q. The bottom AND gate takes CLK, J and NOT Q and feeds the bottom NOR gate, whose output is NOT Q."><g transform="translate(110 20)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><g transform="translate(110 140)"><path class="fm s-acc sw2" d="M0 0 H20 A20 20 0 0 1 20 40 H0 Z"/></g><g transform="translate(200 30)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><g transform="translate(200 130)"><path class="fm s-acc sw2" d="M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z"/><circle class="fm s-acc sw2" cx="46" cy="20" r="4"/></g><text class="tl" x="14" y="44">K</text><polyline class="ln" fill="none" points="30,40 110,40"/><text class="tl" x="4" y="104">CLK</text><polyline class="ln" fill="none" points="30,100 70,100"/><polyline class="ln" fill="none" points="70,52 70,148 110,148"/><polyline class="ln" fill="none" points="70,52 110,52"/><circle class="fi" cx="70" cy="100" r="3"/><text class="tl" x="14" y="164">J</text><polyline class="ln" fill="none" points="30,160 110,160"/><polyline class="ln" fill="none" points="150,40 204,40"/><polyline class="ln" fill="none" points="150,160 204,160"/><polyline class="ln" fill="none" points="250,50 300,50"/><text class="tl" x="306" y="54">Q</text><polyline class="ln" fill="none" points="250,150 300,150"/><text class="tl" x="306" y="154">NOT Q</text><polyline class="ln" fill="none" points="270,50 270,8 95,8 95,28 110,28"/><polyline class="ln" fill="none" points="270,50 270,100 180,100 180,140 204,140"/><circle class="fi" cx="270" cy="50" r="3"/><polyline class="ln" fill="none" points="260,150 260,200 95,200 95,172 110,172"/><polyline class="ln" fill="none" points="260,150 260,110 190,110 190,60 204,60"/><circle class="fi" cx="260" cy="150" r="3"/></svg><figcaption>A JK flip-flop: two 3-input AND gates, controlled by the clock CLK, in front of an SR flip-flop. Q and NOT Q are fed back to the AND gates.</figcaption></figure>
:::

The top AND gate has inputs K, CLK and Q, and drives R. The bottom AND gate has inputs J, CLK and NOT Q, and drives S. Two facts follow.

1. **The clock controls when the output can change.** If CLK = 0, both AND gates output 0, so S = R = 0 and the SR flip-flop simply holds its bit, whatever J and K are. Only when a clock pulse arrives (CLK = 1) can J and K act. In a computer, the same clock signal goes to every flip-flop, so every stored bit changes at the same moment as the rest of the machine.
2. **S and R can never both be 1.** The bottom gate needs NOT Q = 1 and the top gate needs Q = 1, and Q and NOT Q are opposites, so only one of them can pass a 1. This removes the invalid state. Instead, when J = K = 1, whichever gate is open changes Q, so Q **toggles**.

| J | K | Q before the clock pulse | Q after the clock pulse | State |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | no change |
| 0 | 0 | 1 | 1 | no change |
| 0 | 1 | 0 | 0 | reset |
| 0 | 1 | 1 | 0 | reset |
| 1 | 0 | 0 | 1 | set |
| 1 | 0 | 1 | 1 | set |
| 1 | 1 | 0 | 1 | toggle |
| 1 | 1 | 1 | 0 | toggle |

:::key Flip-flop truth tables to learn
- **SR** (NOR version): 00 hold, 10 set (Q = 1), 01 reset (Q = 0), 11 invalid.
- **JK**: 00 hold, 10 set, 01 reset, 11 toggle (Q becomes NOT Q), all on a clock pulse.
- A JK flip-flop with J = K = 1 changes on every clock pulse, so Q goes through one full cycle (0 then 1 then 0) for every two clock pulses: it divides the clock frequency by 2.
:::

:::eg Tracing a JK flip-flop
A JK flip-flop starts with Q = 0. Inputs (J, K) are (1, 0), (0, 0), (0, 1), (1, 1), (1, 1) and (0, 0) at six successive clock pulses. State Q after each pulse. [3 marks]

| Pulse | J | K | Q after the pulse | Why |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | set |
| 2 | 0 | 0 | 1 | no change |
| 3 | 0 | 1 | 0 | reset |
| 4 | 1 | 1 | 1 | toggle (0 becomes 1) |
| 5 | 1 | 1 | 0 | toggle (1 becomes 0) |
| 6 | 0 | 0 | 0 | no change |

- pulses 1 to 3 give 1, 1, 0 [B1]
- pulses 4 and 5 toggle, giving 1 then 0 [B1]
- pulse 6 holds the value, giving 0 [B1]
:::

### Flip-flops as data storage

A flip-flop stores exactly one bit and keeps it for as long as power is supplied. Eight flip-flops side by side store one byte. A processor's registers (the accumulator, the program counter and the others from [Processor fundamentals and the fetch-execute cycle](#cs.processor)) are rows of flip-flops, and so is the static memory (SRAM) described in [Computers and their components](#cs.hardware). That is why SRAM is fast and needs no refreshing, and why it costs more per bit than the capacitor-based DRAM: each bit needs several transistors to make its flip-flop.

## Karnaugh maps

Boolean algebra simplifies any expression, but it needs you to spot which law to use next, and it is easy to stop too early. A **Karnaugh map** (K-map) turns the search into a picture. It works for up to four variables, which is exactly what exams ask.

:::def Karnaugh map
A grid that shows the output of a logic expression for every combination of its inputs, with one cell for each row of the truth table. The cells are arranged so that neighbouring cells differ in only one input. Groups of neighbouring 1s are then read off as simplified product terms.
:::

The cells must be arranged in **Gray code** order, not in ordinary binary order.

:::def Gray code
A sequence of binary numbers in which only one bit changes from each number to the next. For two bits the order is 00, 01, 11, 10.
:::

Why does this matter? Two neighbouring cells differ in exactly one variable, so the term for the pair no longer depends on that variable, as in \(A \cdot B + A \cdot \text{NOT } B = A\). With the order 00, 01, 10, 11, the cells 01 and 10 would be neighbours although both bits differ, and the trick would fail.

### Drawing the map

For three variables, one variable runs down the side and two along the top. Here are the cell numbers. A cell's number is the inputs read as one binary number, with A as the leftmost bit, so ABC = 101 is cell 5.

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 1 | 3 | 2 |
| 1 | 4 | 5 | 7 | 6 |

For four variables, AB runs down the side and CD along the top, both in Gray code.

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 0 | 1 | 3 | 2 |
| 01 | 4 | 5 | 7 | 6 |
| 11 | 12 | 13 | 15 | 14 |
| 10 | 8 | 9 | 11 | 10 |

A map for two variables is a 2 by 2 grid with A down the side and B along the top. You fill each cell with the output X from the truth table: a 1 where X = 1 and a 0 where X = 0. Take care to place each row of the truth table in the right cell: row 011 goes in row A = 0, column BC = 11.

:::key Reading a Karnaugh map
1. Fill the map from the truth table (or the expression): 1 in the cell of every input where X = 1, 0 elsewhere.
2. Circle **groups of 1s**. A group must be a rectangle with 1, 2, 4, 8 or 16 cells (never 3, 5, 6 or 7), and must contain no 0.
3. **Wrap-around** is allowed: the left and right edges touch, and the top and bottom edges touch. On a 4-by-4 map the four corners form one group of 4.
4. Make every group **as large as possible**, and use the **fewest groups** that cover every 1. Groups may **overlap**. A 1 may be in more than one group.
5. Each group gives one **product term**. Keep the variables that stay the same inside the group: write the plain letter if it is 1 and NOT before it if it is 0. Drop any variable that takes both values.
6. OR the product terms together.
:::

A group of 2 drops one variable, a group of 4 drops two, a group of 8 drops three. The bigger the group, the shorter the term.

:::eg Simplify a 3-variable function with a map
Use a Karnaugh map to simplify the function with output X = 1 for rows 011, 100, 101 and 111 (the function from the sum-of-products example). [4 marks]

Rows 011, 100, 101 and 111 are cells 3, 4, 5 and 7.

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

There are three groups of two that could be drawn:

- cells 4 and 5 (row A = 1, columns 00 and 01): A stays 1, B stays 0, C changes, giving \(A \cdot \text{NOT } B\);
- cells 3 and 7 (column BC = 11): B and C stay 1, A changes, giving \(B \cdot C\);
- cells 5 and 7 (row A = 1, columns 01 and 11): A and C stay 1, B changes, giving \(A \cdot C\).

Cell 4 is only in the first group, and cell 3 is only in the second group, so both of those groups are needed. Together they cover cells 3, 4, 5 and 7, so the third group adds nothing.

\[ X = A \cdot \text{NOT } B + B \cdot C \]

- map filled correctly, with 1 in cells 3, 4, 5 and 7 [B1]
- group of cells 4 and 5 identified, giving \(A \cdot \text{NOT } B\) [B1]
- group of cells 3 and 7 identified, giving \(B \cdot C\) [B1]
- the terms joined with OR, giving the minimal expression [B1]

This is the answer the algebra gave earlier, found without naming any law. The unneeded group \(A \cdot C\) is why "fewest groups" is part of the rule.
:::

:::eg Karnaugh map for the carry out of a full adder
Use a map to find a simplified expression for Cout in the full adder truth table. [3 marks]

Cout is 1 for rows 011, 101, 110 and 111, which are cells 3, 5, 6 and 7.

| A \ B Cin | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 |

Group cells 3 and 7 (B = 1, Cin = 1), cells 5 and 7 (A = 1, Cin = 1) and cells 6 and 7 (A = 1, B = 1). All three groups are needed, because cells 3, 5 and 6 each belong to only one group.

\[ \text{Cout} = B \cdot \text{Cin} + A \cdot \text{Cin} + A \cdot B \]

- map filled with 1s in cells 3, 5, 6 and 7 [B1]
- three groups of two identified [B1]
- expression \(A \cdot B + B \cdot \text{Cin} + A \cdot \text{Cin}\) [B1]

The sum S cannot be simplified in this way. Its 1s are in cells 1, 2, 4 and 7, and none of them touches another, so every group is a single cell. That is the XOR pattern, a checkerboard of 1s, and a map shows at a glance that no grouping exists.
:::

### Four variables, and wrapping round the edges

With four variables the groups can be 2, 4 or 8 cells, and the wrap-around becomes important. The figure shows a worked map, with each group drawn in a different line style.

:::html
<figure class="fig small"><svg viewBox="0 0 300 290" role="img" aria-label="A 4-variable Karnaugh map with rows AB and columns CD in Gray code order 00, 01, 11, 10. Ones are in cells 0, 1, 2, 5, 6, 7, 8, 9, 10 and 14. Group 1, solid outline: cells 0, 1, 8 and 9, which wrap from the bottom edge to the top edge, giving NOT B AND NOT C. Group 2, dashed outline: cells 5 and 7, giving NOT A AND B AND D. Group 3, dotted outline: cells 2, 6, 10 and 14, the whole CD = 10 column, giving C AND NOT D."><text class="tl tc" x="166" y="22">CD</text><text class="tl" x="8" y="44">AB</text><text class="tl tc" x="91" y="44">00</text><text class="tl tc" x="141" y="44">01</text><text class="tl tc" x="191" y="44">11</text><text class="tl tc" x="241" y="44">10</text><text class="tl te" x="58" y="74">00</text><text class="tl te" x="58" y="110">01</text><text class="tl te" x="58" y="146">11</text><text class="tl te" x="58" y="182">10</text><rect class="fm s-acc sw1" x="66" y="52" width="50" height="36"/><text class="tl tc tb" x="91" y="75">1</text><rect class="fm s-acc sw1" x="116" y="52" width="50" height="36"/><text class="tl tc tb" x="141" y="75">1</text><rect class="fm s-acc sw1" x="166" y="52" width="50" height="36"/><text class="tl tc tb" x="191" y="75">0</text><rect class="fm s-acc sw1" x="216" y="52" width="50" height="36"/><text class="tl tc tb" x="241" y="75">1</text><rect class="fm s-acc sw1" x="66" y="88" width="50" height="36"/><text class="tl tc tb" x="91" y="111">0</text><rect class="fm s-acc sw1" x="116" y="88" width="50" height="36"/><text class="tl tc tb" x="141" y="111">1</text><rect class="fm s-acc sw1" x="166" y="88" width="50" height="36"/><text class="tl tc tb" x="191" y="111">1</text><rect class="fm s-acc sw1" x="216" y="88" width="50" height="36"/><text class="tl tc tb" x="241" y="111">1</text><rect class="fm s-acc sw1" x="66" y="124" width="50" height="36"/><text class="tl tc tb" x="91" y="147">0</text><rect class="fm s-acc sw1" x="116" y="124" width="50" height="36"/><text class="tl tc tb" x="141" y="147">0</text><rect class="fm s-acc sw1" x="166" y="124" width="50" height="36"/><text class="tl tc tb" x="191" y="147">0</text><rect class="fm s-acc sw1" x="216" y="124" width="50" height="36"/><text class="tl tc tb" x="241" y="147">1</text><rect class="fm s-acc sw1" x="66" y="160" width="50" height="36"/><text class="tl tc tb" x="91" y="183">1</text><rect class="fm s-acc sw1" x="116" y="160" width="50" height="36"/><text class="tl tc tb" x="141" y="183">1</text><rect class="fm s-acc sw1" x="166" y="160" width="50" height="36"/><text class="tl tc tb" x="191" y="183">0</text><rect class="fm s-acc sw1" x="216" y="160" width="50" height="36"/><text class="tl tc tb" x="241" y="183">1</text><rect class="c1 sw2" fill="none" rx="8" x="72" y="58" width="88" height="24"/><rect class="c1 sw2" fill="none" rx="8" x="72" y="166" width="88" height="24"/><rect class="c2 sw2 dash" fill="none" rx="8" x="122" y="94" width="88" height="24"/><rect class="c3 sw2 dot" fill="none" rx="8" x="222" y="58" width="38" height="132"/><text class="tl" x="20" y="224">Group 1 (solid): NOT B AND NOT C</text><text class="tl" x="20" y="244">Group 2 (dashed): NOT A AND B AND D</text><text class="tl" x="20" y="264">Group 3 (dotted): C AND NOT D</text></svg><figcaption>A 4-variable Karnaugh map for X = (NOT B AND NOT C) OR (NOT A AND B AND D) OR (C AND NOT D). Group 1 has a solid outline, group 2 a dashed outline and group 3 a dotted outline.</figcaption></figure>
:::

:::eg A 4-variable map with wrap-around
A function X of four inputs A, B, C and D is 1 when the inputs, read as the binary number ABCD, are 0, 1, 2, 5, 6, 7, 8, 9, 10 or 14, and 0 otherwise. Use a Karnaugh map to find the simplest expression. [6 marks]

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 1 | 1 | 0 | 1 |
| 01 | 0 | 1 | 1 | 1 |
| 11 | 0 | 0 | 0 | 1 |
| 10 | 1 | 1 | 0 | 1 |

Look for the biggest groups first.

- **Group 1, cells 0, 1, 8 and 9** (four cells). The rows 00 and 10 are at the top and bottom edges, and the top and bottom edges are neighbours, so these four cells form a group that wraps round. B stays 0 and C stays 0; A and D change. Term: \(\text{NOT } B \cdot \text{NOT } C\).
- **Group 2, cells 5 and 7** (two cells, row AB = 01). A stays 0, B stays 1, D stays 1; C changes. Term: \(\text{NOT } A \cdot B \cdot D\).
- **Group 3, cells 2, 6, 10 and 14** (four cells). This is the whole right-hand column, CD = 10. C stays 1 and D stays 0; A and B change. Term: \(C \cdot \text{NOT } D\).

All ten 1s are covered, and no 1 can be added to a bigger group, so

\[ X = \text{NOT } B \cdot \text{NOT } C + \text{NOT } A \cdot B \cdot D + C \cdot \text{NOT } D \]

- map filled correctly with ten 1s [B1]
- group of 4 using the wrap-around (cells 0, 1, 8, 9) giving \(\text{NOT } B \cdot \text{NOT } C\) [B1]
- group of 2 (cells 5 and 7) giving \(\text{NOT } A \cdot B \cdot D\) [B1]
- group of 4 in the right-hand column giving \(C \cdot \text{NOT } D\) [B1]
- every 1 is covered and no group contains a 0 [B1]
- the three terms joined with OR [B1]
:::

Now try it yourself. The map below starts with the function you have just solved. Press **Solve** to see the groups. Then switch cells to see how the answer changes.

:::html
<div class="widget" data-w="cs-kmap" data-vars="4" data-ones="0,1,2,5,6,7,8,9,10,14"></div>
:::

Things to try. Turn cell 14 off and solve again: the whole right-hand column is no longer a group, and the answer needs four groups instead of three. Clear the map and fill only the four corners 0, 2, 8 and 10: one group of four that wraps in both directions, giving \(\text{NOT } B \cdot \text{NOT } D\). Switch to 3 variables and fill the cells 1, 2, 4 and 7 (the sum of a full adder): there are no groups bigger than one cell, so the map cannot shorten an XOR-type function.

:::warn Karnaugh map mistakes
- **Axes in binary order** (00, 01, 10, 11) instead of Gray code (00, 01, 11, 10). The groups then come out wrong.
- **Groups of 3, 5 or 6**. A group is a rectangle of 1, 2, 4, 8 or 16 cells. Three 1s in a row are a group of 2 plus another group that overlaps it.
- **Missing the wrap-around**, so that a pair at opposite edges is left as two separate single cells.
- **Stopping at a small group** when a bigger one exists, or using more groups than needed.
- **Writing the wrong sign for a variable**: a variable that is 0 in the group needs a NOT.
- **Putting a 0 inside a group**.
:::

### Why use a Karnaugh map?

:::key Benefits of Karnaugh maps
- The simplified expression needs **fewer gates and fewer connections**, so the circuit is cheaper, smaller, uses less power and (with fewer gates for the signal to pass through) is faster.
- It is a **visual, systematic method**: you do not have to decide which law to apply next, so it is quicker and less error-prone than algebra for up to four variables.
- It gives the **simplest sum of products** directly, and shows when no simplification is possible.
:::

The limits are also worth knowing. A map becomes very awkward beyond four or five variables, because the neighbours are no longer all next to each other on the page. For large functions, designers use computer programs that follow a method of the same kind. And a function may have more than one correct minimal answer (two different groupings with the same number of terms), so a marker accepts any correct simplest form.

:::eg Spot the error: the map with the wrong axes
Question: Simplify the function X = 1 for cells 1, 2, 3 and 6, using a Karnaugh map with three variables A, B, C. [4 marks]

A student drew this map:

| A \ BC | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |

The student circled the three 1s in the top row as one group of three and the 1 under the 10 column as another, giving \(X = \text{NOT } A + A \cdot B \cdot \text{NOT } C\). The marks are awarded as follows.

Cells 1, 2, 3 and 6 are placed in the right rows [B1]. **The column headings are in binary order (00, 01, 10, 11), not Gray code (00, 01, 11, 10), so the columns 10 and 11 are in the wrong places and the neighbours are not true neighbours [B0].** A group of three is not allowed [B0]. The final expression is not equivalent to the function [B0]. The answer scores 1 out of 4.

The corrected map puts the headings in the order 00, 01, 11, 10:

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 |

Now the three 1s in the top row are still not a group of 3, so use two groups of two. Cells 1 and 3 (column 01 and 11, row 0) give \(\text{NOT } A \cdot C\). Cells 2 and 6 (column 10, both rows) give \(B \cdot \text{NOT } C\). Cells 2 and 3 are also next to each other, but cells 1 and 3 plus cells 2 and 6 already cover every 1. The correct answer is \(X = \text{NOT } A \cdot C + B \cdot \text{NOT } C\).
:::

:::eg Spot the error: De Morgan's law
Question: Simplify \(X = \text{NOT}(A \cdot B) \cdot A\). [3 marks]

A student wrote:

\[
\begin{aligned}
X &= \text{NOT}(A \cdot B) \cdot A \\
  &= \text{NOT } A \cdot \text{NOT } B \cdot A \quad \text{(De Morgan's law)} \\
  &= 0 \quad \text{(complement law)}
\end{aligned}
\]

**The first step is wrong: De Morgan's law changes the AND to an OR, so \(\text{NOT}(A \cdot B) = \text{NOT } A + \text{NOT } B\) [B0].** The complement law is used correctly on the line the student had, because \(\text{NOT } A \cdot A = 0\) [B1]. The final answer is wrong [B0]. The answer scores 1 out of 3.

The correct working:

\[
\begin{aligned}
X &= (\text{NOT } A + \text{NOT } B) \cdot A \quad \text{(De Morgan's law)} \\
  &= \text{NOT } A \cdot A + \text{NOT } B \cdot A \quad \text{(distributive law)} \\
  &= 0 + A \cdot \text{NOT } B \quad \text{(complement law)} \\
  &= A \cdot \text{NOT } B \quad \text{(identity law)}
\end{aligned}
\]

A quick test would have caught the slip. Try A = 1 and B = 0: the original expression gives \(\text{NOT}(0) \cdot 1 = 1\), but the student's answer gives 0.
:::

:::try Start easy, finish at exam standard
Q: Write \(A \text{ AND } (B \text{ OR NOT } C)\) in Boolean algebra using the symbols \(\cdot\), \(+\) and NOT.
A: \(A \cdot (B + \text{NOT } C)\).
Q: State the value of each: (a) \(A + 1\); (b) \(A \cdot 0\); (c) \(A + \text{NOT } A\); (d) \(A \cdot A\).
A: (a) 1, null law; (b) 0, null law; (c) 1, complement law; (d) \(A\), idempotent law.
Q: Use De Morgan's law to write \(\text{NOT}(A + B + C)\) without a NOT over a bracket.
A: \(\text{NOT } A \cdot \text{NOT } B \cdot \text{NOT } C\). The OR becomes AND and each variable is inverted.
Q: Simplify \(X = A \cdot B + A \cdot \text{NOT } B \cdot C\) using the useful shortcut.
A: Take A out as a common factor: \(X = A \cdot (B + \text{NOT } B \cdot C)\). The shortcut \(B + \text{NOT } B \cdot C = B + C\) gives \(X = A \cdot (B + C)\), which is \(A \cdot B + A \cdot C\).
Q: Complete the truth table of a half adder for the input A = 1, B = 1, and say which gate gives each output.
A: S = 0 (XOR gate) and C = 1 (AND gate), because \(1 + 1 = 10\) in binary.
Q: A full adder has A = 1, B = 0 and Cin = 1. State S and Cout.
A: The three inputs add to 2, which is 10 in binary, so S = 0 and Cout = 1.
Q: An SR flip-flop made from NOR gates has Q = 1. State the output Q after S = 0, R = 1.
A: Q = 0. R = 1 resets the flip-flop.
Q: An SR flip-flop is set (Q = 1). Both inputs are now 0. What is Q, and why?
A: Q stays 1. With S = R = 0 the feedback loop holds the stored value.
Q: A JK flip-flop has Q = 1 and receives J = 1, K = 1 on a clock pulse. State Q afterwards.
A: Q = 0: with J = K = 1 the output toggles.
Q: State the order of the headings along the top of a 3-variable Karnaugh map for BC.
A: 00, 01, 11, 10 (Gray code).
Q: A group on a Karnaugh map has 8 cells in a 4-variable map. How many variables does its term contain?
A: One. An 8-cell group removes three of the four variables.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Complete the truth table for a full adder, which has inputs A, B and a carry in Cin and outputs a sum S and a carry out Cout. The rows with A = 0 and B = 0 are given.

| A | B | Cin | S | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | | |
| 0 | 1 | 1 | | |
| 1 | 0 | 0 | | |
| 1 | 0 | 1 | | |
| 1 | 1 | 0 | | |
| 1 | 1 | 1 | | |

H: Add the three input bits in each row. The sum digit is the right-hand digit of the result and the carry is the left-hand digit.
A: Add the three bits and write the total in binary.

| A | B | Cin | S | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

- S correct for rows 3 and 4 (1, 0) [B1]
- S correct for rows 5 to 8 (1, 0, 0, 1) [B1]
- Cout correct for rows 3 and 4 (0, 1) [B1]
- Cout correct for rows 5 to 8 (0, 1, 1, 1) [B1]

Q: [4 marks] ★★ Simplify \(X = (A + B) \cdot (A + \text{NOT } B) \cdot C\), naming the law used at each step.
H: Look at the first two brackets. They both contain A, so the OR form of the distributive law can combine them.
A: Combine the first two brackets, then simplify.

\[
\begin{aligned}
X &= (A + B \cdot \text{NOT } B) \cdot C \quad \text{(distributive law)} \\
  &= (A + 0) \cdot C \quad \text{(complement law)} \\
  &= A \cdot C \quad \text{(identity law)}
\end{aligned}
\]

- the first two brackets combined to \(A + B \cdot \text{NOT } B\) using the distributive law [B1]
- \(B \cdot \text{NOT } B = 0\) by the complement law [B1]
- \(A + 0 = A\) by the identity law [B1]
- final answer \(X = A \cdot C\) [B1]

Q: [6 marks] ★★ (a) Use De Morgan's laws to simplify \(X = \text{NOT}(A \cdot \text{NOT } B) \cdot \text{NOT}(\text{NOT } A \cdot B)\), showing each step. [5] (b) State how the simplified expression can be made from one XOR gate and one other gate. [1]
H: Apply De Morgan's law to each bracket, then remove double complements, then expand the product.
A: (a)
\[
\begin{aligned}
X &= (\text{NOT } A + \text{NOT}(\text{NOT } B)) \cdot (\text{NOT}(\text{NOT } A) + \text{NOT } B) \quad \text{(De Morgan's law, twice)} \\
  &= (\text{NOT } A + B) \cdot (A + \text{NOT } B) \quad \text{(double complement)} \\
  &= \text{NOT } A \cdot A + \text{NOT } A \cdot \text{NOT } B + B \cdot A + B \cdot \text{NOT } B \quad \text{(distributive law)} \\
  &= 0 + \text{NOT } A \cdot \text{NOT } B + A \cdot B + 0 \quad \text{(complement law)} \\
  &= A \cdot B + \text{NOT } A \cdot \text{NOT } B \quad \text{(identity law)}
\end{aligned}
\]

- De Morgan's law applied to both brackets [B1]
- double complements removed, giving \((\text{NOT } A + B) \cdot (A + \text{NOT } B)\) [B1]
- brackets multiplied out with the distributive law [B1]
- complement law used on \(\text{NOT } A \cdot A\) and \(B \cdot \text{NOT } B\) [B1]
- final answer \(A \cdot B + \text{NOT } A \cdot \text{NOT } B\) [B1]

(b) An XOR gate followed by a NOT gate: the output is 1 when A and B are equal. [B1]

Q: [4 marks] ★★ The output X of a circuit with inputs A, B and C is 1 for the input rows 000, 001, 011 and 111 only. Complete a Karnaugh map for X and use it to write the simplest sum of products.
H: Rows 000, 001, 011 and 111 are cells 0, 1, 3 and 7. Use Gray code on the headings.
A:

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |

Group cells 0 and 1: A = 0 and B = 0 stay, C changes, giving \(\text{NOT } A \cdot \text{NOT } B\). Group cells 3 and 7: B = 1 and C = 1 stay, A changes, giving \(B \cdot C\). Cell 1 is also next to cell 3, but the two groups already cover all four 1s.

\[ X = \text{NOT } A \cdot \text{NOT } B + B \cdot C \]

- map filled with 1s in cells 0, 1, 3 and 7 and 0 elsewhere, with Gray code headings [B1]
- group of cells 0 and 1 giving \(\text{NOT } A \cdot \text{NOT } B\) [B1]
- group of cells 3 and 7 giving \(B \cdot C\) [B1]
- terms joined with OR [B1]

Q: [5 marks] ★★ An SR flip-flop is made from two NOR gates and starts with Q = 1. The inputs (S, R) take these values in order: (0, 0), (0, 1), (0, 0), (1, 0), (1, 1). Complete a table of Q and NOT Q after each change, and state what is wrong with the last input.
H: Use the rules: 10 sets, 01 resets, 00 holds. Think about what happens when both NOR gates have an input of 1.
A:

| S | R | Q | NOT Q |
|---|---|---|---|
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

- the first row holds Q = 1, NOT Q = 0 [B1]
- the second row resets: Q = 0, NOT Q = 1 [B1]
- the third row holds Q = 0, NOT Q = 1 [B1]
- the fourth row sets: Q = 1, NOT Q = 0 [B1]
- the last input is invalid: both outputs are 0 (so Q and NOT Q are not opposites), and the state afterwards is unpredictable [B1]

Q: [6 marks] ★★ (a) State what J = 1 and K = 1 does to the output of a JK flip-flop on a clock pulse. [1] (b) Explain the role of the clock in a JK flip-flop. [2] (c) Explain why a JK flip-flop has no invalid input although an SR flip-flop has one. [3]
H: For (c), think about which AND gates can be open at the same time when Q is 1.
A: (a) The output Q toggles (changes to the opposite value). [B1]

(b) The outputs can change only when a clock pulse arrives [B1]; between pulses the flip-flop holds its value whatever J and K are, so changes happen in step with the rest of the system (synchronised) [B1].

(c) The AND gates that feed the SR flip-flop use the outputs Q and NOT Q as inputs [B1]. The gate for the set input needs NOT Q = 1 and the gate for the reset input needs Q = 1 [B1]. Q and NOT Q are opposites, so S and R can never both be 1 [B1].

Q: [8 marks] ★★★ A function X has four inputs A, B, C and D. X is 1 when the inputs, read as the binary number ABCD, are 3, 4, 5, 7, 11, 12, 13 or 15, and 0 otherwise. (a) Complete a Karnaugh map for X. [2] (b) Draw the groups and write the simplest sum of products. [4] (c) State two benefits of using a Karnaugh map rather than simplifying with algebra. [2]
H: The cells 4, 5, 12 and 13 form a block in the middle of the left side. Look at the column CD = 11 as well.
A: (a)

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 0 | 0 | 1 | 0 |
| 01 | 1 | 1 | 1 | 0 |
| 11 | 1 | 1 | 1 | 0 |
| 10 | 0 | 0 | 1 | 0 |

- all eight 1s placed in the correct cells [B1]
- Gray code headings used on both axes [B1]

(b) The column CD = 11 (cells 3, 7, 11, 15) is a group of 4: C and D stay 1, giving \(C \cdot D\). [B1] The block of cells 4, 5, 12, 13 (rows AB = 01 and 11, columns CD = 00 and 01) is a group of 4: B stays 1 and C stays 0, giving \(B \cdot \text{NOT } C\). [B1] The group 5, 7, 13, 15 (\(B \cdot D\)) is a valid group, but it is not needed because every 1 is already covered. [B1]

\[ X = B \cdot \text{NOT } C + C \cdot D \]  [B1]

(c) Any two of: a visual, systematic method that is less likely to contain errors; quicker than algebra for up to four variables; leads to the simplest expression, so a circuit with fewer gates (cheaper, faster, uses less power). [B1] [B1]

Q: [7 marks] ★★★ A computer adds two 3-bit numbers with three full adders joined in a row. The numbers are 101 and 011. (a) Complete a table showing A, B, Cin, S and Cout for each adder, starting with the adder for the right-hand bit, whose carry in is 0. [4] (b) State the result and the final carry out, and say what the final carry out of 1 tells you. [2] (c) State why the adder for the right-hand bit could be a half adder. [1]
H: Remember that the carry out of one adder is the carry in of the next adder on its left.
A: (a)

| Bit | A | B | Cin | S | Cout |
|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 2 | 1 | 0 | 1 | 0 | 1 |

- bit 0: \(1 + 1 + 0\) gives S = 0, Cout = 1 [B1]
- bit 1: \(0 + 1 + 1\) gives S = 0, Cout = 1 [B1]
- bit 2: \(1 + 0 + 1\) gives S = 0, Cout = 1 [B1]
- each carry out used as the carry in of the next adder to the left [B1]

(b) The sum bits are 000 and the final carry out is 1, so the result is 1000 (denary 8) [B1]. The carry out of 1 means the result is too big for 3 bits: overflow [B1].

(c) The right-hand column has only two bits to add, because there is no carry in [B1].
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Show that an XOR gate can be built from four NAND gates joined as follows. Gate N1 has inputs A and B. Gate N2 has inputs A and the output of N1. Gate N3 has inputs B and the output of N1. Gate N4 has the outputs of N2 and N3 as its inputs and gives X. Prove that \(X = A \text{ XOR } B\) using Boolean algebra, then use the result to say how many gates this needs compared with building XOR as \(\text{NOT } A \cdot B + A \cdot \text{NOT } B\).
H: Write each gate as an expression, for example \(N1 = \text{NOT}(A \cdot B)\), and use De Morgan's laws.
H: Expand \(N2 = \text{NOT}(A \cdot N1)\) using De Morgan's law, and note that \(A \cdot \text{NOT}(A \cdot B) = A \cdot \text{NOT } B\).
A: Write each gate in turn.

\[
\begin{aligned}
N1 &= \text{NOT}(A \cdot B) \\
N2 &= \text{NOT}(A \cdot N1) = \text{NOT } A + \text{NOT}(N1) = \text{NOT } A + A \cdot B = \text{NOT } A + B \\
N3 &= \text{NOT}(B \cdot N1) = \text{NOT } B + \text{NOT}(N1) = \text{NOT } B + A \cdot B = \text{NOT } B + A \\
X &= \text{NOT}(N2 \cdot N3) = \text{NOT}((\text{NOT } A + B) \cdot (A + \text{NOT } B))
\end{aligned}
\]

The lines for N2 and N3 use the shortcut \(P + \text{NOT } P \cdot Q = P + Q\): for N2, \(P = \text{NOT } A\), so \(\text{NOT } A + A \cdot B = \text{NOT } A + B\). The product in the last line was multiplied out in an earlier practice question: \((\text{NOT } A + B) \cdot (A + \text{NOT } B) = A \cdot B + \text{NOT } A \cdot \text{NOT } B\). So \(X = \text{NOT}(A \cdot B + \text{NOT } A \cdot \text{NOT } B)\). This is the opposite of "A and B are equal", which is true exactly when the inputs differ, so \(X = A \text{ XOR } B\).

- N2 and N3 written as expressions using De Morgan's law [B1]
- the shortcut or absorption used to simplify N2 and N3 [B1]
- X written as NOT of a product of N2 and N3 [B1]
- result shown to equal \(A \text{ XOR } B\), for example by a truth table or by algebra [B1]
- four NAND gates, compared with two AND gates, one OR gate and two NOT gates (five gates of three kinds) [B1]

Q: [6 marks] ★★★ A 2-bit number P is stored as the bits A (the more significant) and B. A 2-bit number Q is stored as C (the more significant) and D. A circuit outputs X = 1 when P is greater than Q. (a) List the cell numbers (ABCD read as binary) where X = 1. [2] (b) Use a Karnaugh map to find the simplest sum of products. [4]
H: Write P = 2A + B and Q = 2C + D, and test all sixteen combinations: for example, P = 3 and Q = 2 is ABCD = 1110, which is cell 14.
H: Draw the map. One group is the whole of rows AB = 11 and 10 in the columns where C = 0.
A: (a) \(P > Q\) for the cells 4, 8, 9, 12, 13 and 14. For example, cell 4 is ABCD = 0100: P = 1, Q = 0. Cell 14 is 1110: P = 3, Q = 2. [B2] (b)

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 0 | 0 | 0 | 0 |
| 01 | 1 | 0 | 0 | 0 |
| 11 | 1 | 1 | 0 | 1 |
| 10 | 1 | 1 | 0 | 0 |

Group cells 8, 9, 12 and 13 (A = 1, C = 0): \(A \cdot \text{NOT } C\). Group cells 12 and 14 (A = 1, B = 1, D = 0): \(A \cdot B \cdot \text{NOT } D\). Group cells 4 and 12 (B = 1, C = 0, D = 0): \(B \cdot \text{NOT } C \cdot \text{NOT } D\).

\[ X = A \cdot \text{NOT } C + A \cdot B \cdot \text{NOT } D + B \cdot \text{NOT } C \cdot \text{NOT } D \]

- map filled correctly [B1]
- group of 4 giving \(A \cdot \text{NOT } C\) [B1]
- groups of 2 giving \(A \cdot B \cdot \text{NOT } D\) and \(B \cdot \text{NOT } C \cdot \text{NOT } D\) [B1]
- the three terms joined with OR [B1]
:::

:::quiz
? Which law makes \(A + A \cdot B\) equal to A?
- Distributive law
- Complement law
+ Absorption law
- Idempotent law
> The extra term \(A \cdot B\) is absorbed because A already covers it. The idempotent law is \(A + A = A\), and the complement law is \(A + \text{NOT } A = 1\).
? Which is the correct application of De Morgan's law to \(\text{NOT}(A \cdot B)\)?
- \(\text{NOT } A \cdot \text{NOT } B\)
+ \(\text{NOT } A + \text{NOT } B\)
- \(\text{NOT } A + B\)
- \(A + B\)
> The AND changes to OR and each variable is inverted. \(\text{NOT } A \cdot \text{NOT } B\) is the result for NOR, not for NAND, because the sign was not changed.
? What is the value of \(1 + 1\) in Boolean algebra?
- 2
- 10
+ 1
- 0
> \(+\) means OR, and 1 OR 1 is 1. The values 2 and 10 are binary addition, which is done by an adder, not by the OR operation.
? How many of the three inputs of a full adder must be 1 for the carry out to be 1?
- exactly three
- exactly one
+ at least two
- an odd number
> The three bits add to two or three, which needs a carry. With one input at 1 the total is 1 and there is no carry. An odd number of 1s (one or three) is the rule for the sum S, not the carry.
? An SR flip-flop made from NOR gates has S = 0 and R = 0 after being set. What is Q?
- 0
+ 1
- it is unpredictable
- it is the opposite of S
> With both inputs 0 the cross-coupled gates hold the stored value, so Q stays 1. Q is unpredictable only after S = R = 1 is released.
? What does a JK flip-flop do when J = 1 and K = 1 at a clock pulse?
- It stores the invalid state.
- It resets Q to 0.
+ It toggles Q to the opposite value.
- It ignores the pulse.
> J = K = 1 is the toggle row. The SR flip-flop has an invalid state at 11, but the JK flip-flop does not.
? Which order is correct for the headings along the top of a 3-variable Karnaugh map (BC)?
- 00, 01, 10, 11
+ 00, 01, 11, 10
- 00, 10, 01, 11
- 11, 10, 01, 00
> Gray code changes one bit at a time: 00, 01, 11, 10. Binary order puts 01 next to 10, and these differ in two bits.
? Which of these is a valid group on a Karnaugh map?
- three cells in a row
+ four cells at the corners of a 4-by-4 map
- six cells in a 2-by-3 block
- two cells joined diagonally
> The four corners are neighbours because the map wraps in both directions. Groups must have 1, 2, 4, 8 or 16 cells in a rectangle, so 3 and 6 are not allowed, and a diagonal pair differs in two variables.
? Which statement about a flip-flop is correct?
- It stores one byte.
- It has no memory of earlier inputs.
+ It stores one bit for as long as power is supplied.
- Its output depends only on its current inputs.
> A flip-flop remembers one bit; a byte needs eight. Its output depends on its stored state as well as its inputs, unlike a combinational circuit.
:::

:::checklist What you can now do
- [ ] I can complete truth tables for circuits that have more than two inputs or gates with more than two inputs, including a half adder and a full adder.
- [ ] I can describe how a full adder is built from two half adders and an OR gate, and how full adders are chained to add binary numbers.
- [ ] I can draw an SR flip-flop from two NOR gates, derive its truth table and explain why S = R = 1 is invalid.
- [ ] I can describe a JK flip-flop, derive its truth table, and explain the role of the clock and why it has no invalid state.
- [ ] I can explain how flip-flops store one bit and are used in registers and static memory.
- [ ] I can state the laws of Boolean algebra and De Morgan's laws, and prove them with a truth table.
- [ ] I can simplify a Boolean expression or the expression for a circuit by algebra, naming the law at each step.
- [ ] I can write a sum of products from a truth table.
- [ ] I can fill in a Karnaugh map in Gray code order for 2, 3 or 4 variables, group the 1s (including wrap-around) and write the simplified expression.
- [ ] I can explain the benefits of Karnaugh maps.
:::

:::recap
- Boolean algebra: \(\cdot\) is AND, \(+\) is OR, NOT inverts. Order: brackets, NOT, AND, OR. \(1 + 1 = 1\).
- Laws: identity, null, idempotent, complement, double complement, commutative, associative, distributive (both forms), absorption, De Morgan's.
- De Morgan's laws: \(\text{NOT}(A \cdot B) = \text{NOT } A + \text{NOT } B\) and \(\text{NOT}(A + B) = \text{NOT } A \cdot \text{NOT } B\): break the bracket, change the sign, invert each part.
- Simplify by taking out common factors, using \(A + \text{NOT } A = 1\), absorption and De Morgan's laws, naming each law. A sum of products comes from the rows where X = 1.
- Half adder: S = A XOR B, C = A AND B. Full adder: two half adders and an OR; S = A XOR B XOR Cin; Cout = 1 when at least two inputs are 1. Full adders chained add whole numbers (the carry ripples left).
- SR flip-flop (NOR): 10 set, 01 reset, 00 no change, 11 invalid. JK flip-flop (clocked): 00 no change, 10 set, 01 reset, 11 toggle; no invalid state. A flip-flop stores one bit; registers and SRAM are made of them.
- Karnaugh map: Gray code headings 00, 01, 11, 10; groups of 1, 2, 4, 8 in rectangles; wrap-around allowed; overlap allowed; biggest groups; each group gives one product term (keep the unchanging variables).
- Benefits of a map: fewer gates (cheaper, faster, less power) and a quick, visual, systematic method for up to four variables.
:::

:::links
- practise: [Boolean algebra and logic circuits: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/15-hardware-and-virtual-machines-/boolean-algebra-and-logic-circuits/exam-questions/) · Save My Exams · 9618-style questions with mark schemes, by difficulty [paid]
- explore: [Logicly demo](https://logic.ly/demo/) · Logicly · build the half adder, full adder and an SR latch from gates and flip the inputs
- explore: [Logic gate challenges](https://www.101computing.net/logic-gates-circuits/) · 101 Computing · logic circuit challenges with truth tables
- explore: [Nand2Tetris](https://www.nand2tetris.org/) · Nand2Tetris · build a whole computer from NAND gates (stretch)
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists on how computers work
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations and questions on logic and Boolean algebra (written for UK boards)

Links checked 13 November 2026.
:::

Next: [Operating systems: processes, scheduling and memory](#cs.os)
