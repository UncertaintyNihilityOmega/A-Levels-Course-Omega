@chapter math.proof
@title Proof: how mathematicians know
@level ext
@paper UK A Level (AQA 7357, Edexcel 9MA0, OCR H240) Proof · CAIE 9231 induction · the habits behind every "show that" in CAIE 9709
@time 4–6 hours
@summary What a mathematical proof is and how to write one: proof by deduction, by exhaustion, disproof by counter-example, proof by contradiction (the irrationality of the square root of 2 and the infinity of primes), a first taste of induction, and how to set out a proof so that every line has a reason.

:::why
Checking a few examples never proves a statement for all numbers, and mathematics is the one subject where "always" can be proved to mean always. Proof is also the skill behind every "show that" and "verify" in an exam, and it is a named topic in the UK A Levels and in Further Mathematics. Even if you never sit a proof question, learning to argue in careful steps makes every other chapter easier to follow and your own working easier to mark.
:::

**Before you start**, you need [Algebra from scratch](#math.f.algebra) (expanding and factorising), [Indices, surds and standard form](#math.f.powers) (the proof that \(\sqrt2\) is irrational appears there too) and a feel for the types of number in [Numbers, fractions and percentages](#math.f.numbers). The last section previews induction, which the chapter [Further Mathematics: a guided tour](#math.further) develops.

:::try Warm-up
Q: Expand \((2n + 1)^2\). (from [Algebra from scratch](#math.f.algebra))
A: \((2n + 1)(2n + 1) = 4n^2 + 2n + 2n + 1\), which simplifies to \(4n^2 + 4n + 1\).
Q: Factorise \(n^2 + n\). (from [Algebra from scratch](#math.f.algebra))
A: \(n^2 + n = n(n + 1)\).
Q: Write the recurring decimal \(0.\dot{3}\dot{6}\) as a fraction in its lowest terms. (from [Numbers, fractions and percentages](#math.f.numbers))
A: Let \(x = 0.3636\ldots\), so \(100x = 36.3636\ldots\) and \(99x = 36\). Then \(x = \dfrac{36}{99} = \dfrac{4}{11}\).
:::

## What counts as a proof?

A **statement** is a sentence that is true or false, such as "the sum of two odd numbers is even". A **conjecture** is a statement that someone believes but has not yet proved. Most statements in mathematics say something about *every* number of a kind ("for all integers \(n\)"), and that is where examples are not enough.

:::def Proof
A logical argument that starts from facts already accepted (definitions, results already proved, the rules of algebra) and reaches the statement by steps that each have a reason, so that no case is left out.
:::

Here is why examples fail. Try the expression \(n^2 + n + 41\):

| \(n\) | 1 | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| value | 43 | 47 | 53 | 71 | 151 |

The value in the second row is \(n^2 + n + 41\), and all of these are prime numbers. It is tempting to believe the expression is prime for every positive integer \(n\). In fact it is prime for \(n = 1, 2, \ldots, 39\) and then fails at \(n = 40\):
\[40^2 + 40 + 41 = 1681 = 41 \times 41\]
Thirty-nine successes proved nothing. One failure disproved everything. That asymmetry shapes the whole chapter: **to prove "for all" you need an argument; to disprove "for all" you need a single counter-example.**

:::warn Examples are not a proof
In an exam, writing "it works for \(n = 1, 2, 3\)" scores no marks as a proof. Examples are useful for finding the pattern and for checking your final line, but the proof itself must work for a general number such as \(n\), with a reason for every step.
:::

## Proof by deduction

In a **proof by deduction** you write the objects in a general algebraic form and then work forwards, line by line, to the result.

:::key Building blocks for number proofs
- An **even** number is \(2n\), where \(n\) is an integer. An **odd** number is \(2n + 1\).
- **Consecutive integers** are \(n\), \(n + 1\), \(n + 2\), and so on. Two consecutive even numbers are \(2n\) and \(2n + 2\).
- A **multiple of \(k\)** has the form \(k \times (\text{integer})\). To show a number is a multiple of \(k\), take a factor \(k\) out of the algebra.
- Use a **different letter** for each separate number (\(2a + 1\) and \(2b + 1\)), otherwise you accidentally force them to be equal.
- End by saying what you have shown, in words.
:::

:::eg Prove that the sum of any two odd numbers is even.
Let the two odd numbers be \(2a + 1\) and \(2b + 1\), where \(a\) and \(b\) are integers.
\[(2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1)\]
Since \(a + b + 1\) is an integer, the sum is \(2\) times an integer, so it is even. ∎
:::

The small box ∎ (or "QED", or "as required") marks the end of a proof.

:::eg (Exam style) Prove that the square of any odd number is one more than a multiple of \(8\).
Let the odd number be \(2n + 1\), where \(n\) is an integer. [B1]
\[(2n + 1)^2 = 4n^2 + 4n + 1 = 4n(n + 1) + 1\] [M1]
Now \(n(n + 1)\) is a product of two consecutive integers, and one of two consecutive integers is always even. So \(n(n + 1) = 2m\) for some integer \(m\). [B1]
\[(2n + 1)^2 = 4(2m) + 1 = 8m + 1\]
This is one more than a multiple of \(8\), as required. [A1]
Check: \(7^2 = 49 = 6 \times 8 + 1\). ✓
:::

:::eg Prove that \((n + 1)^2 - (n - 1)^2\) is a multiple of \(4\) for every integer \(n\).
Expand each square and subtract:
\[\begin{aligned} (n + 1)^2 - (n - 1)^2 &= (n^2 + 2n + 1) - (n^2 - 2n + 1) \\ &= 4n \end{aligned}\]
Since \(n\) is an integer, \(4n\) is a multiple of \(4\). ∎ (A faster route is the difference of two squares: \((n + 1 - (n - 1))(n + 1 + (n - 1)) = 2 \times 2n\).)
:::

## Proof by exhaustion

Sometimes there are only a few cases, and you can check every one. This is **proof by exhaustion**. The cases must be *all* the possibilities, and each must be checked in general, not with a single number.

The cleanest cases are the remainders on division. Every integer is of the form \(3k\), \(3k + 1\) or \(3k + 2\); every integer is even or odd.

:::eg (Exam style) Prove that the square of any integer is either a multiple of \(3\) or one more than a multiple of \(3\).
Every integer \(n\) is of one of three forms: \(3k\), \(3k + 1\) or \(3k + 2\), for an integer \(k\). These cover every possibility. [B1]

- If \(n = 3k\), then \(n^2 = 9k^2 = 3(3k^2)\), a multiple of \(3\). [M1]
- If \(n = 3k + 1\), then \(n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1\), one more than a multiple of \(3\). [A1]
- If \(n = 3k + 2\), then \(n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1\), one more than a multiple of \(3\). [A1]

In every case \(n^2\) is a multiple of \(3\) or one more than a multiple of \(3\). ∎
:::

:::tip Which proof method?
Look at the statement. If it says "show that this expression is always even, odd or a multiple of \(k\)", try **deduction**. If it can be split into a small number of cases (even/odd, remainder 0/1/2), use **exhaustion**. If it says "show that there are no numbers such that" or "show that it is irrational", think **contradiction**. If it says "is it true that for all ...?", test small numbers for a **counter-example** first.
:::

## Disproof by counter-example

To show that a statement about all numbers is false, find **one** case where it fails. This is a **counter-example**. You must check that the example really satisfies the conditions and really breaks the conclusion.

- **Claim:** the sum of two primes is even. **Counter-example:** \(2 + 3\). Both are prime and the sum is \(5\), which is odd.
- **Claim:** if \(n\) is prime then \(n + 2\) is prime. **Counter-example:** \(n = 7\). It is prime, but \(7 + 2 = 9\), which is \(3 \times 3\).
- **Claim:** \(n^2 > n\) for every number \(n\). **Counter-example:** \(n = \tfrac12\). Here \(n^2 = \tfrac14\), which is less than \(\tfrac12\).
- **Claim:** \(n^2 + n + 41\) is prime for all positive \(n\). **Counter-example:** \(n = 40\). The value is \(1681\), which is \(41^2\).

:::eg (Exam style) Show that the statement "\(2^n + 1\) is prime for every positive integer \(n\)" is false.
Try \(n = 3\): \(2^3 + 1 = 9\). [M1]
\(9 = 3 \times 3\) is not prime, so the statement is false. [A1]
(The values for \(n = 1, 2\) are \(3\) and \(5\), both prime: a pattern that holds for the first two cases and then breaks is typical.)
:::

## Proof by contradiction

In **proof by contradiction** you assume the statement is **false**, work logically from that assumption, and arrive at something impossible. Since correct logic cannot produce an impossibility, the assumption must be wrong, so the statement is true.

:::steps
1. Assume the opposite of what you want to prove. Say so clearly: "Suppose that ..."
2. Argue logically from that assumption.
3. Reach a statement that is false, or that contradicts the assumption or a known fact.
4. Conclude: "This is a contradiction, so the assumption is false, and the original statement is true."
:::

First a small result that we need, which is itself a proof by contradiction.

:::eg Prove that if \(n^2\) is even, then \(n\) is even.
Suppose that \(n^2\) is even but \(n\) is odd. Then \(n = 2k + 1\) and
\[n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1\]
which is odd. This contradicts the fact that \(n^2\) is even. So \(n\) must be even. ∎
:::

:::eg (Exam style) Prove that \(\sqrt2\) is irrational.
Suppose \(\sqrt2\) is rational. Then \(\sqrt2 = \dfrac pq\), where \(p\) and \(q\) are integers with no common factor (the fraction is in lowest terms). [M1]

Square both sides: \(2 = \dfrac{p^2}{q^2}\), so \(p^2 = 2q^2\). Therefore \(p^2\) is even, and by the result above \(p\) is even. [B1]
Write \(p = 2r\) for an integer \(r\): \(4r^2 = 2q^2\), so \(q^2 = 2r^2\). [M1]
Then \(q^2\) is even, so \(q\) is even. [A1]

Now both \(p\) and \(q\) are even, so they have the common factor \(2\). This contradicts the assumption that they have no common factor. Hence \(\sqrt2\) is not rational: it is irrational. [B1]
:::

Euclid's proof that the primes never run out is the other famous example. The idea is to build a number that must have a new prime factor.

:::eg (Exam style) Prove that there are infinitely many prime numbers.
Suppose there are only finitely many primes, and list them all: \(p_1, p_2, \ldots, p_k\). [B1]
Let \(N = p_1 p_2 \cdots p_k + 1\). [M1]
When \(N\) is divided by any \(p_i\) the remainder is \(1\), because \(p_1 p_2 \cdots p_k\) is a multiple of \(p_i\). So no prime on the list divides \(N\). [A1]
But \(N > 1\), so \(N\) is either prime itself or has a prime factor. Either way there is a prime that is not on the list. This contradicts the assumption that the list contained every prime, so there are infinitely many primes. [A1]
For example, with the primes \(2, 3, 5, 7, 11, 13\): \(N = 30\,031 = 59 \times 509\). The number \(N\) is not itself prime, but its factors \(59\) and \(509\) are primes not on the list.
:::

:::warn Common faults in a contradiction proof
- Not saying what is assumed. Write "Suppose that ..." at the start.
- Forgetting the "no common factor" part of the \(\sqrt2\) assumption. Without it there is no contradiction at the end.
- Stopping at the impossible statement. State the conclusion in a sentence: the assumption is false, so the original statement is true.
- Treating "the opposite" wrongly. The opposite of "all" is "at least one is not"; the opposite of "irrational" is "rational".
:::

## A taste of induction

Some statements are about *every positive integer* and are hard to prove by algebra on \(n\) alone. **Proof by induction** works like dominoes: show the first one falls, and show that whenever one falls the next one does too. The full method, with its marks, is in [Further Mathematics: a guided tour](#math.further). Here is one small example to see the shape.

:::eg Prove by induction that \(2^n \ge n + 1\) for every positive integer \(n\).
**Basis**: for \(n = 1\), \(2^1 = 2\) and \(n + 1 = 2\), so \(2 \ge 2\) is true.
**Assumption**: suppose \(2^k \ge k + 1\) for some positive integer \(k\).
**Step**: multiply both sides by \(2\):
\[2^{k+1} = 2 \cdot 2^k \ge 2(k + 1) = 2k + 2 \ge k + 2\]
The last step is true because \(k \ge 0\). The statement \(2^{k+1} \ge (k + 1) + 1\) is exactly the statement for \(n = k + 1\).
**Conclusion**: it is true for \(n = 1\), and if it is true for \(n = k\) it is true for \(n = k + 1\), so it is true for all positive integers \(n\) by induction. ∎
:::

## Writing a proof

A proof is graded like any other answer: each line must follow from the previous lines, and the reader must be able to see *why*.

:::exam How to set out a proof in an exam
- Start by defining your symbols: "Let the integers be \(n\) and \(n + 1\)."
- Write one step per line. Give a reason in words when it is not just algebra ("since \(n(n + 1)\) is a product of consecutive integers, it is even").
- Use the words **since**, **so**, **therefore**, **hence**, **as required**, and say what you have shown at the end.
- In a "show that" question, the answer is given: do not start from it. Work towards it, and keep every line of the algebra. In 9709 the nearest thing to proof is "show that", "verify" and "hence show": the same rules apply.
- Never begin with the result you want and "check" that both sides agree. That is assuming what you want to prove, which earns nothing.
:::

:::board Boards
The UK A Levels (AQA 7357, Edexcel 9MA0, OCR H240) examine proof as part of Pure Mathematics: deduction, exhaustion, disproof by counter-example and proof by contradiction. The 9709 syllabus lists no separate proof topic, but "show that" questions use the same reasoning, and proof by induction is examined in Cambridge Further Mathematics 9231. If you sit another board, check its specification for exactly which methods are required.
:::

:::eg Spot the error: prove that \(\sqrt2\) is irrational.
The question is worth 5 marks: one method mark for the assumption, one for the substitution, and three more for the reasoning and the conclusion. A student wrote this answer.

Line 1: Suppose \(\sqrt2 = \dfrac pq\), with \(p\) and \(q\) integers. [M0]
Line 2: Then \(p^2 = 2q^2\), so \(p^2\) is even, so \(p\) is even. [B1]
Line 3: Let \(p = 2r\). Then \(4r^2 = 2q^2\), so \(q^2 = 2r^2\). [M1]
Line 4: So \(q^2\) is even, so \(q\) is even. [A1]
Line 5: So \(\sqrt2\) is irrational. [B0]

**Line 1 is incomplete.** The student did not say that \(\dfrac pq\) is in lowest terms, so there is no common factor to contradict later [M0]. Lines 2 to 4 are correct (the reason in line 2 is that an odd number squared is odd) [B1] [M1] [A1]. **Line 5 jumps to the conclusion.** The student never says that \(p\) and \(q\) both being even contradicts the assumption, so the contradiction, which is the whole point of the method, is not stated [B0]. The student scores 3 out of 5.

Correct opening: "Suppose \(\sqrt2 = \dfrac pq\), where \(p\) and \(q\) are integers with no common factor." [M1] Correct ending: "Then \(p\) and \(q\) are both even, so they have a common factor of \(2\). This contradicts the assumption. Hence \(\sqrt2\) is irrational." [B1]
:::

:::try Start easy, finish at exam standard
Q: A student notices that \(n^2 - n + 11\) is prime for \(n = 1, 2, 3, 4, 5\) and says "it is always prime". Is this a proof? Find a value of \(n\) that breaks the claim.
A: No: five examples do not prove a statement about every \(n\). For \(n = 11\), \(11^2 - 11 + 11 = 121 = 11 \times 11\), which is not prime.
Q: Prove that the sum of any three consecutive integers is a multiple of \(3\).
A: Let the integers be \(n\), \(n + 1\), \(n + 2\). The sum is \(3n + 3 = 3(n + 1)\), which is \(3\) times an integer. ∎
Q: Prove that the product of two odd numbers is odd.
A: Let the numbers be \(2a + 1\) and \(2b + 1\). Then
\[\begin{aligned} (2a + 1)(2b + 1) &= 4ab + 2a + 2b + 1 \\ &= 2(2ab + a + b) + 1 \end{aligned}\]
which is one more than twice an integer, so it is odd. ∎
Q: Find a counter-example to the statement: "If \(a\) and \(b\) are irrational, then \(a + b\) is irrational."
A: Take \(a = \sqrt2\) and \(b = 3 - \sqrt2\), both irrational. Their sum is \(3\), which is rational.
Q: Prove that \(n^2 + n\) is even for every integer \(n\), using exhaustion.
A: If \(n\) is even, both \(n^2\) and \(n\) are even, so the sum is even. If \(n\) is odd, \(n^2\) and \(n\) are both odd, and odd + odd is even. These cases cover every integer. ∎
Q: [5 marks] (Exam style) Prove by contradiction that \(\sqrt3\) is irrational. You may use the fact that if \(p^2\) is a multiple of \(3\), then \(p\) is a multiple of \(3\).
A: Suppose \(\sqrt3 = \dfrac pq\), with \(p\) and \(q\) integers having no common factor. [M1] Then \(p^2 = 3q^2\), so \(p^2\) is a multiple of \(3\), and so is \(p\). [B1] Write \(p = 3r\): \(9r^2 = 3q^2\), so \(q^2 = 3r^2\). [M1] Then \(q^2\) is a multiple of \(3\), so \(q\) is a multiple of \(3\). [A1] Now \(p\) and \(q\) share the factor \(3\), which contradicts the assumption. Hence \(\sqrt3\) is irrational. [B1]
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Show that the statement "\(n^2 > 2n\) for every positive integer \(n\)" is false.
A: Try \(n = 1\): \(1^2 = 1\) and \(2n = 2\), and \(1 > 2\) is false. [M1] So \(n = 1\) is a counter-example and the statement is false. [A1] (\(n = 2\) also works: \(4 > 4\) is false.)
Q: [3 marks] ★ Prove that the sum of any two consecutive odd numbers is a multiple of \(4\).
A: Let the numbers be \(2n + 1\) and \(2n + 3\). [B1] Their sum is \(4n + 4\) [M1] \(= 4(n + 1)\), a multiple of \(4\). [A1]
Q: [4 marks] ★★ Prove that \((n + 3)^2 - (n - 1)^2\) is a multiple of \(8\) for every integer \(n\).
A: Expand: \((n^2 + 6n + 9) - (n^2 - 2n + 1)\) [M1] \(= 8n + 8\). [A1] Factorise: \(8(n + 1)\). [M1] Since \(n + 1\) is an integer, this is a multiple of \(8\). [A1]
Q: [4 marks] ★★ Prove that \(n^3 - n\) is divisible by \(6\) for every positive integer \(n\).
A: Factorise: \(n^3 - n = n(n^2 - 1) = (n - 1)n(n + 1)\), a product of three consecutive integers. [M1] Among three consecutive integers at least one is even, so the product is divisible by \(2\). [B1] Exactly one of them is a multiple of \(3\), so the product is divisible by \(3\). [B1] Since \(2\) and \(3\) share no factor, the product is divisible by \(6\). [A1]
Q: [5 marks] ★★★ Prove that the sum of the squares of two odd numbers is never a perfect square.
H: Write the two odd numbers as \(2a + 1\) and \(2b + 1\) and expand the sum of squares. What does the answer look like when divided by 4?
H: Now look at what a perfect square looks like when divided by 4. Consider an even number squared and an odd number squared separately.
A:
\[\begin{aligned} (2a + 1)^2 + (2b + 1)^2 &= 4a^2 + 4a + 1 + 4b^2 + 4b + 1 \\ &= 4(a^2 + a + b^2 + b) + 2 \end{aligned}\] [M1 A1]
So the sum is two more than a multiple of \(4\). [B1] The square of an even number is \((2m)^2 = 4m^2\), a multiple of \(4\). The square of an odd number is \((2m + 1)^2 = 4(m^2 + m) + 1\), one more than a multiple of \(4\). [B1] A number two more than a multiple of \(4\) is neither, so it is not a perfect square. [A1]
Q: [6 marks] (#math.f.powers) ★★★ Prove by contradiction that \(\sqrt5\) is irrational. You may use the fact that if \(p^2\) is a multiple of \(5\), then \(p\) is a multiple of \(5\).
H: Copy the structure of the proof for \(\sqrt2\), replacing "even" by "multiple of 5".
H: Do not forget "in lowest terms" at the start and the contradiction at the end.
A: Suppose \(\sqrt5 = \dfrac pq\), where \(p\) and \(q\) are integers with no common factor. [M1] Then \(p^2 = 5q^2\). [A1] So \(p^2\) is a multiple of \(5\), and therefore so is \(p\). [B1] Write \(p = 5r\): \(25r^2 = 5q^2\), so \(q^2 = 5r^2\). [M1] Then \(q^2\) is a multiple of \(5\), so \(q\) is a multiple of \(5\). [A1] Both \(p\) and \(q\) are multiples of \(5\), contradicting "no common factor". Hence \(\sqrt5\) is irrational. [B1]
Q: [5 marks] (#math.p1.quadratics) ★★★ (a) Prove that \(x^2 - 6x + 10 > 0\) for every real value of \(x\). (b) Show by a counter-example that the statement "\(x^2 - 6x + 8 > 0\) for every real value of \(x\)" is false.
H: Complete the square in (a). A square is never negative.
H: In (b), a counter-example is a value of \(x\) that makes the expression zero or negative. Where are its roots?
A: (a) \(x^2 - 6x + 10 = (x - 3)^2 + 1\). [M1 A1] Since \((x - 3)^2 \ge 0\) for every real \(x\), the expression is at least \(1\), so it is greater than \(0\). [B1] (b) Take \(x = 3\): \(9 - 18 + 8 = -1\), which is not greater than \(0\). [M1] So the statement is false. [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Prove that the product of four consecutive positive integers, plus \(1\), is always a perfect square.
H: Call the integers \(n\), \(n + 1\), \(n + 2\), \(n + 3\). Pair up the first and last, and the middle two. What do the products have in common?
H: Let \(m = n^2 + 3n\). Write the whole expression in terms of \(m\).
A: Let the integers be \(n\), \(n + 1\), \(n + 2\), \(n + 3\). Then \(n(n + 3) = n^2 + 3n\) and \((n + 1)(n + 2) = n^2 + 3n + 2\). [M1 A1] Let \(m = n^2 + 3n\). The expression is \(m(m + 2) + 1\) [M1] \(= m^2 + 2m + 1 = (m + 1)^2\). [A1] That is \((n^2 + 3n + 1)^2\), the square of an integer. ∎ [A1] Check: \(1 \times 2 \times 3 \times 4 + 1 = 25 = 5^2\), and \(n^2 + 3n + 1 = 5\) when \(n = 1\). ✓
Q: [4 marks] (#math.p3.logs) ★★★ Prove by contradiction that \(\log_2 3\) is irrational.
H: Suppose \(\log_2 3 = \dfrac pq\), where \(p\) and \(q\) are positive whole numbers. Turn it into an equation between powers.
H: One side of the equation will be even, the other odd.
A: Suppose \(\log_2 3 = \dfrac pq\), where \(p\) and \(q\) are positive integers (\(\log_2 3 > 0\), so both can be taken positive). [M1] Then \(2^{p/q} = 3\), so \(2^p = 3^q\). [M1] The left side is a power of \(2\), so it is even. The right side is a power of \(3\), so it is odd. [A1] An even number cannot equal an odd number, a contradiction. So \(\log_2 3\) is irrational. [A1]
:::

:::quiz
? A student shows that \(n^2 + n + 41\) is prime for \(n = 1\) up to \(10\). What can they conclude?
- the expression is prime for every positive integer \(n\)
- the expression is prime for all \(n\) up to \(40\)
+ it is prime for those ten values, and nothing more has been proved
- the expression can never be composite
> Checking cases proves nothing about the other cases. In fact \(n = 40\) gives \(1681 = 41^2\), so the pattern breaks. Any number of successes can be undone by one counter-example.
? Which expression represents any odd integer in a proof?
- \(2n\)
- \(n + 1\)
+ \(2n + 1\)
- \(n^2\)
> An odd number is one more than a multiple of \(2\). \(2n\) is even, \(n + 1\) can be odd or even, and \(n^2\) can be odd or even too.
? To disprove the statement "all prime numbers are odd", what do you need?
+ one counter-example, such as \(2\)
- ten examples that do not fit
- a proof by induction
- an algebraic argument for every prime
> A single case that satisfies the conditions and breaks the conclusion disproves a statement about "all". The number \(2\) is prime and even.
? What is the first line of a proof by contradiction that \(\sqrt2\) is irrational?
- Suppose \(\sqrt2\) is irrational.
+ Suppose \(\sqrt2 = \dfrac pq\), where \(p\) and \(q\) are integers with no common factor.
- Check that \(\sqrt2 = 1.414\).
- Square both sides.
> You assume the **opposite** of the conclusion, so you assume \(\sqrt2\) is rational, and you put it in lowest terms so there is a common factor to contradict at the end.
? Why does \(p^2 = 2q^2\) imply that \(p\) is even?
- because \(2q^2\) is a square
+ because an odd number squared is odd, so if \(p\) were odd then \(p^2\) would be odd, but \(p^2\) is even
- because \(q\) is even
- because \(p\) and \(q\) are equal
> \(p^2\) equals \(2q^2\), which is even. If \(p\) were odd, \(p^2\) would be odd. So \(p\) must be even.
:::

:::checklist What you can now do
- [ ] I can tell the difference between checking examples and proving a statement for all numbers.
- [ ] I can write even, odd, consecutive and multiple-of-\(k\) numbers algebraically and prove a result by deduction.
- [ ] I can prove a statement by exhaustion, splitting into cases that cover every possibility.
- [ ] I can disprove a statement by finding and checking a counter-example.
- [ ] I can write a proof by contradiction, starting with the opposite assumption and ending with a clear conclusion.
- [ ] I can prove that \(\sqrt2\) is irrational and that there are infinitely many primes.
- [ ] I can set out a proof so that every line has a reason, and finish with a sentence saying what has been shown.
:::

:::recap
- A proof for "all" numbers needs a general argument; one counter-example disproves a statement about all numbers.
- Deduction: write even as \(2n\), odd as \(2n + 1\), consecutive integers as \(n, n + 1, \ldots\), and take the factor out.
- Exhaustion: split into cases that cover everything (even/odd; remainders \(0, 1, 2\)) and check each in general.
- Contradiction: assume the opposite, reach something impossible, and conclude in a sentence. For \(\sqrt2\): lowest terms, \(p^2 = 2q^2\), both even.
- Induction: basis, assume \(n = k\), show \(n = k + 1\), conclude. It is examined in Further Mathematics.
- Set out: define symbols, one step per line, reasons in words, a final sentence.
:::

:::links
- read: [Mathematical Induction](https://www.mathsisfun.com/algebra/mathematical-induction.html) · Maths is Fun · the domino idea in plain words with examples
- explore: [Divisibility & Induction](https://undergroundmathematics.org/divisibility-and-induction) · Underground Mathematics · induction for divisibility problems
- practise: [Proof revision (A Level)](https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/proof/) · Physics & Maths Tutor · notes and questions on each proof method [unofficial]
- practise: [NRICH for students](https://nrich.maths.org/students) · NRICH · problems where you must justify every step

Links checked 4 October 2026.
:::
Next: [Further Mathematics: a guided tour](#math.further).
