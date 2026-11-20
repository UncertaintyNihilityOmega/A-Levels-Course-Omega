@chapter math.fm.induction
@title Proof by induction
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 5–7 hours
@summary Induction proves a statement for every positive integer in two steps: show it is true for the first case, and show that if it is true for one case it is true for the next. You will prove formulae for sums, divisibility results, formulae for terms of a recurrence relation, powers of a 2×2 matrix and nth derivatives, set out the proof the way the mark scheme wants it, and learn to guess a formula from a few cases and then prove it.

:::why
A formula can be right for \(n = 1, 2, 3, \dots, 39\) and still be wrong at \(n = 40\). Testing cases never proves a general result, but induction does, in a finite number of lines. In Further Mathematics it is a skill examined in its own right: there are marks for the layout as well as the algebra, and the layout is the same every time.
:::

**Before you start**, you need the sums \(\sum r\), \(\sum r^2\) and \(\sum r^3\) from [Summation of series](#math.fm.series), matrix products from [Matrices: algebra, determinants and inverses](#math.fm.matrices), the idea of proof from [Proof: how mathematicians know](#math.proof), and the product rule from [Further differentiation](#math.p3.diff).

:::try Warm-up
Q: Evaluate \(\displaystyle\sum_{r=1}^{4} r^2\), and check it against \(\tfrac16 n(n + 1)(2n + 1)\) at \(n = 4\). (from [Summation of series](#math.fm.series))
A: \(1 + 4 + 9 + 16 = 30\), and \(\tfrac16 \times 4 \times 5 \times 9 = 30\).
Q: Find \(\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^2\). (from [Matrices: algebra, determinants and inverses](#math.fm.matrices))
A: \(\begin{pmatrix} 1 + 0 & 1 + 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\).
Q: Differentiate \(x\mathrm{e}^x\). (from [Further differentiation](#math.p3.diff))
A: By the product rule, \(\dfrac{d}{dx}(x\mathrm{e}^x) = \mathrm{e}^x + x\mathrm{e}^x = (x + 1)\mathrm{e}^x\).
:::

## The idea of induction

:::analogy Dominoes
Imagine an infinite row of dominoes, numbered 1, 2, 3, \(\dots\). You want to know that every domino falls. You need only two facts. First, domino 1 falls (push it). Second, whenever domino \(k\) falls, it knocks over domino \(k + 1\). Then domino 1 knocks over domino 2, which knocks over domino 3, and so on forever. Nobody checked each domino; the chain does the work.
:::

:::def Proof by induction
A method of proving that a statement \(P(n)\), which depends on a positive integer \(n\), is true for every positive integer \(n\). You prove \(P(1)\) (the **base case**) and you prove that, if \(P(k)\) is true for some positive integer \(k\) (the **assumption**), then \(P(k + 1)\) is true (the **inductive step**).
:::

To prove \(P(n)\) for all \(n \ge 1\):

:::key Proof by induction: the four steps
1. **Base case.** Show \(P(1)\) is true, by substituting \(n = 1\) into both sides.
2. **Assumption.** Write: "Assume the result is true for \(n = k\)", and write out \(P(k)\) in full. (\(k\) is some particular positive integer.)
3. **Inductive step.** Show that \(P(k + 1)\) follows. Write out \(P(k + 1)\) as the target, start from the left side, and use the assumption in the working.
4. **Conclusion.** "The result is true for \(n = 1\). If it is true for \(n = k\), then it is true for \(n = k + 1\). So by mathematical induction, it is true for all positive integers \(n\)."
In 9231 mark schemes these earn **B1** (base case), **B1** (assumption), **M1 A1** (inductive step) and **A1** (conclusion).
:::

The mark scheme wants the specific words, so write all four steps every time. Examiners cannot award the conclusion mark for a proof with no stated assumption, and they cannot award the step marks if the assumption never appears in the working.

### A first full proof

:::eg (Exam style) Prove by mathematical induction that \(\displaystyle\sum_{r=1}^{n} r^3 = \tfrac14 n^2(n + 1)^2\) for all positive integers \(n\).
**Base case**, \(n = 1\): the left side is \(1^3 = 1\) and the right side is \(\tfrac14 \times 1^2 \times 2^2 = 1\). So the result is true for \(n = 1\). [B1]

**Assumption**: assume the result is true for \(n = k\), that is
\[\sum_{r=1}^{k} r^3 = \tfrac14 k^2(k + 1)^2\] [B1]
**Inductive step**: the target is \(\displaystyle\sum_{r=1}^{k+1} r^3 = \tfrac14(k + 1)^2(k + 2)^2\). Add the \((k + 1)\)th term to both sides of the assumption:
\[\sum_{r=1}^{k+1} r^3 = \tfrac14 k^2(k + 1)^2 + (k + 1)^3\] [M1]
Take out the common factor \(\tfrac14(k + 1)^2\):
\[\begin{aligned}
&= \tfrac14(k + 1)^2\left[k^2 + 4(k + 1)\right] \\
&= \tfrac14(k + 1)^2(k^2 + 4k + 4) \\
&= \tfrac14(k + 1)^2(k + 2)^2
\end{aligned}\] [A1]
This is the formula with \(n = k + 1\).

**Conclusion**: the result is true for \(n = 1\), and if it is true for \(n = k\) then it is true for \(n = k + 1\). So by mathematical induction it is true for all positive integers \(n\). [A1]
:::

Notice the habit that makes sums easy: write the target for \(n = k + 1\) first, in factorised form, so you know what you are aiming at and can see which common factor to take out.

:::warn Three ways to lose the marks
1. Writing "assume true for all \(n\)". That is the thing you are trying to prove. You assume it for **one** value, \(n = k\).
2. Not using the assumption. If your inductive step could be done without \(P(k)\), it is not an inductive step. The assumed formula must be visible in the first line of the working.
3. Leaving out "true for \(n = 1\)" or "for all positive integers \(n\)" in the conclusion.
:::

## Proving sums

For a sum, the left side of \(P(k + 1)\) is the left side of \(P(k)\) plus one more term, so you replace the old sum by its assumed value and add the new term.

:::eg (Exam style) Prove by induction that \(\displaystyle\sum_{r=1}^{n} r\,2^r = (n - 1)2^{n+1} + 2\) for all positive integers \(n\).
**Base case**, \(n = 1\): the left side is \(1 \times 2 = 2\) and the right side is \(0 \times 4 + 2 = 2\). True for \(n = 1\). [B1]

**Assumption**: assume true for \(n = k\): \(\displaystyle\sum_{r=1}^{k} r\,2^r = (k - 1)2^{k+1} + 2\). [B1]

**Inductive step**: the next term is \((k + 1)2^{k+1}\).
\[\sum_{r=1}^{k+1} r\,2^r = (k - 1)2^{k+1} + 2 + (k + 1)2^{k+1}\] [M1]
\[\begin{aligned}
&= 2^{k+1}\left[(k - 1) + (k + 1)\right] + 2 \\
&= 2k \times 2^{k+1} + 2 \\
&= k \times 2^{k+2} + 2 \\
&= \left((k + 1) - 1\right)2^{(k+1)+1} + 2
\end{aligned}\] [A1]
which is the formula for \(n = k + 1\).

**Conclusion**: true for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
:::

Sums of fractions work the same way: you meet a common denominator and a factorisation.

:::eg Prove by induction that \(\displaystyle\sum_{r=1}^{n} \frac{1}{r(r + 1)} = \frac{n}{n + 1}\) for all positive integers \(n\).
**Base case**, \(n = 1\): the left side is \(\dfrac{1}{1 \times 2} = \dfrac12\) and the right side is \(\dfrac{1}{2}\). True.

**Assumption**: assume \(\displaystyle\sum_{r=1}^{k} \frac{1}{r(r + 1)} = \frac{k}{k + 1}\).

**Inductive step**: the target is \(\dfrac{k + 1}{k + 2}\). Add the next term:
\[\begin{aligned}
\sum_{r=1}^{k+1} \frac{1}{r(r + 1)} &= \frac{k}{k + 1} + \frac{1}{(k + 1)(k + 2)} \\
&= \frac{k(k + 2) + 1}{(k + 1)(k + 2)} = \frac{(k + 1)^2}{(k + 1)(k + 2)} = \frac{k + 1}{k + 2}
\end{aligned}\]
This is the formula for \(n = k + 1\).

**Conclusion**: true for \(n = 1\), and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
:::

You could also prove this one by splitting \(\dfrac{1}{r(r+1)}\) into partial fractions and using the method of differences ([Summation of series](#math.fm.series)). The question says "by induction", so you must set out the four steps.

## Proving divisibility

To show that an expression \(f(n)\) is divisible by \(d\) for all \(n\), the assumption is "\(f(k)\) is divisible by \(d\)", often written \(f(k) = dm\) for some integer \(m\). In the inductive step, look at \(f(k + 1)\) and try to express it as
\[f(k + 1) = f(k) + (\text{a multiple of } d) \qquad\text{or}\qquad f(k + 1) = c\,f(k) + (\text{a multiple of } d)\]
for a number \(c\). Then both pieces are multiples of \(d\), so \(f(k + 1)\) is too.

:::eg Prove by induction that \(7^n - 1\) is divisible by 6 for all positive integers \(n\).
**Base case**, \(n = 1\): \(7^1 - 1 = 6\), which is divisible by 6.

**Assumption**: assume \(7^k - 1\) is divisible by 6, so \(7^k - 1 = 6m\) for some integer \(m\).

**Inductive step**: let \(f(n) = 7^n - 1\). Write \(f(k + 1)\) in terms of \(f(k)\):
\[\begin{aligned}
f(k + 1) &= 7^{k+1} - 1 = 7 \times 7^k - 1 \\
&= 7(7^k - 1) + 7 - 1 \\
&= 7(6m) + 6 = 6(7m + 1)
\end{aligned}\]
\(7m + 1\) is an integer, so \(f(k + 1)\) is divisible by 6.

**Conclusion**: true for \(n = 1\), and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
:::

:::eg (Exam style) Prove by induction that \(3^{2n} + 7\) is divisible by 8 for all positive integers \(n\).
**Base case**, \(n = 1\): \(3^2 + 7 = 16 = 8 \times 2\). True for \(n = 1\). [B1]

**Assumption**: assume \(3^{2k} + 7\) is divisible by 8. [B1]

**Inductive step**: let \(f(n) = 3^{2n} + 7\). Subtract:
\[\begin{aligned}
f(k + 1) - f(k) &= 3^{2k+2} + 7 - 3^{2k} - 7 \\
&= 9 \times 3^{2k} - 3^{2k} = 8 \times 3^{2k}
\end{aligned}\] [M1]
So \(f(k + 1) = f(k) + 8 \times 3^{2k}\). Here \(f(k)\) is divisible by 8 by the assumption and \(8 \times 3^{2k}\) is divisible by 8, so \(f(k + 1)\) is divisible by 8. [A1]

**Conclusion**: true for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction \(3^{2n} + 7\) is divisible by 8 for all positive integers \(n\). [A1]
:::

When the expression is a polynomial in \(n\), the difference \(f(k + 1) - f(k)\) has lower degree, and you often need a second argument (for example that \(k(k + 1)\) is always even).

:::eg Prove by induction that \(n^3 + 11n\) is divisible by 6 for all positive integers \(n\).
**Base case**, \(n = 1\): \(1 + 11 = 12 = 6 \times 2\). True.

**Assumption**: assume \(k^3 + 11k\) is divisible by 6.

**Inductive step**: let \(f(n) = n^3 + 11n\).
\[\begin{aligned}
f(k + 1) - f(k) &= (k + 1)^3 + 11(k + 1) - k^3 - 11k \\
&= k^3 + 3k^2 + 3k + 1 + 11k + 11 - k^3 - 11k \\
&= 3k^2 + 3k + 12 = 3k(k + 1) + 12
\end{aligned}\]
The product \(k(k + 1)\) of two consecutive integers is even, so \(3k(k + 1)\) is a multiple of 6, and 12 is a multiple of 6. So \(f(k + 1) = f(k) + (\text{a multiple of } 6)\) is divisible by 6.

**Conclusion**: true for \(n = 1\), and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
:::

## Recurrence relations

:::def Recurrence relation
A rule that gives each term of a sequence in terms of the term before it, such as \(u_{n+1} = 4u_n - 3\), together with the first term \(u_1\). Repeating the rule produces the whole sequence.
:::

Induction proves a formula for \(u_n\), the \(n\)th term, without repeating the rule \(n - 1\) times. The assumption is the formula for \(u_k\); the inductive step puts it into the recurrence to get \(u_{k+1}\).

:::eg The sequence \(u_n\) has \(u_1 = 1\) and \(u_{n+1} = 3u_n - 1\). Prove by induction that \(u_n = \tfrac12\left(3^{n-1} + 1\right)\).
**Base case**, \(n = 1\): \(\tfrac12(3^0 + 1) = 1 = u_1\). True.

**Assumption**: assume \(u_k = \tfrac12\left(3^{k-1} + 1\right)\).

**Inductive step**:
\[\begin{aligned}
u_{k+1} &= 3u_k - 1 = \tfrac32\left(3^{k-1} + 1\right) - 1 \\
&= \tfrac12\left(3^k + 3 - 2\right) = \tfrac12\left(3^k + 1\right)
\end{aligned}\]
This is the formula with \(n = k + 1\).

**Conclusion**: true for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction. (The terms are 1, 2, 5, 14, \(\dots\).)
:::

:::eg (Exam style) The sequence \(u_1, u_2, u_3, \dots\) is defined by \(u_1 = 2\) and \(u_{n+1} = 4u_n - 3\). Prove by induction that \(u_n = 4^{n-1} + 1\) for all positive integers \(n\).
**Base case**, \(n = 1\): the formula gives \(4^0 + 1 = 2\), which is \(u_1\). True for \(n = 1\). [B1]

**Assumption**: assume \(u_k = 4^{k-1} + 1\). [B1]

**Inductive step**: use the recurrence, and then the assumption:
\[\begin{aligned}
u_{k+1} &= 4u_k - 3 = 4\left(4^{k-1} + 1\right) - 3 \\
&= 4^k + 4 - 3 = 4^k + 1
\end{aligned}\] [M1]
This is the formula with \(n = k + 1\), since \(4^{(k+1)-1} + 1 = 4^k + 1\). [A1]

**Conclusion**: true for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
**Check**: \(u_2 = 4 \times 2 - 3 = 5\) and \(4^1 + 1 = 5\); \(u_3 = 4 \times 5 - 3 = 17\) and \(4^2 + 1 = 17\).
:::

:::eg A savings plan starts with £3 in week 1, and each week the balance doubles and £1 is added, so \(u_{n+1} = 2u_n + 1\) with \(u_1 = 3\). Prove that the balance in week \(n\) is \(u_n = 2^{n+1} - 1\) pounds.
**Base case**: \(n = 1\): \(2^2 - 1 = 3 = u_1\). True.

**Assumption**: assume \(u_k = 2^{k+1} - 1\).

**Inductive step**:
\[u_{k+1} = 2u_k + 1 = 2\left(2^{k+1} - 1\right) + 1 = 2^{k+2} - 1\]
which is the formula with \(n = k + 1\).

**Conclusion**: true for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction. In week 10 the balance is \(2^{11} - 1 = \pounds 2047\).
:::

## Powers of a matrix

For a square matrix, \(\mathbf{M}^{k+1} = \mathbf{M}^k\mathbf{M}\) (or \(\mathbf{M}\mathbf{M}^k\); both orders give the same matrix, because powers of one matrix commute). The assumption is a formula for \(\mathbf{M}^k\); multiply it by \(\mathbf{M}\) and simplify each entry ([Matrices: algebra, determinants and inverses](#math.fm.matrices)).

:::eg (Exam style) The matrix \(\mathbf{M} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\). Prove by induction that \(\mathbf{M}^n = \begin{pmatrix} 2^n & n2^{n-1} \\ 0 & 2^n \end{pmatrix}\) for all positive integers \(n\).
**Base case**, \(n = 1\): the formula gives \(\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\) (since \(1 \times 2^0 = 1\)), which is \(\mathbf{M}\). True. [B1]

**Assumption**: assume \(\mathbf{M}^k = \begin{pmatrix} 2^k & k2^{k-1} \\ 0 & 2^k \end{pmatrix}\). [B1]

**Inductive step**:
\[\mathbf{M}^{k+1} = \mathbf{M}^k\mathbf{M} = \begin{pmatrix} 2^k & k2^{k-1} \\ 0 & 2^k \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 2^{k+1} & 2^k + k2^k \\ 0 & 2^{k+1} \end{pmatrix} = \begin{pmatrix} 2^{k+1} & (k + 1)2^k \\ 0 & 2^{k+1} \end{pmatrix}\] [A1]
This is the formula with \(n = k + 1\), because \((k + 1)2^{(k+1)-1} = (k + 1)2^k\).

**Conclusion**: true for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
:::

In the entry \(2^k + k2^k\), the term \(k2^{k-1} \times 2\) is \(k2^k\) and the term \(2^k \times 1\) is \(2^k\); keep the powers of 2 together and factorise. The bottom-left entry is 0 whatever \(k\) is, because both products contain a zero.

## Conjecture, then prove

Sometimes you are not given the formula. If the problem lists a few cases and asks "find a formula for ...", work out the first few values, look for the pattern, state it as a conjecture, and prove it by induction.

:::note Why a pattern is not enough
The expression \(n^2 + n + 41\) is prime for \(n = 0, 1, 2, \dots, 39\): forty cases in a row. At \(n = 40\) it is \(1600 + 40 + 41 = 1681 = 41^2\), which is not prime. A pattern that holds for forty cases still fails. Only a proof settles it, which is why the conjecture stage is followed by induction.
:::

:::eg Find \(\displaystyle S_n = \sum_{r=1}^{n} r \times r!\) for \(n = 1, 2, 3, 4\), conjecture a formula for \(S_n\), and prove it by induction. (Recall \(r! = r(r - 1)\cdots 2 \times 1\).)
Compute the terms: \(1 \times 1! = 1\), \(2 \times 2! = 4\), \(3 \times 3! = 18\), \(4 \times 4! = 96\). Then
\[S_1 = 1, \quad S_2 = 5, \quad S_3 = 23, \quad S_4 = 119\]
Compare with factorials: \(2! = 2\), \(3! = 6\), \(4! = 24\), \(5! = 120\). Each \(S_n\) is one less than a factorial: \(S_n = (n + 1)! - 1\). This is the conjecture.

**Base case**, \(n = 1\): \(2! - 1 = 1 = S_1\). True.

**Assumption**: assume \(S_k = (k + 1)! - 1\).

**Inductive step**: add the \((k + 1)\)th term \((k + 1) \times (k + 1)!\):
\[\begin{aligned}
S_{k+1} &= (k + 1)! - 1 + (k + 1)(k + 1)! \\
&= (k + 1)!\,\left[1 + (k + 1)\right] - 1 \\
&= (k + 2)(k + 1)! - 1 = (k + 2)! - 1
\end{aligned}\]
This is the formula with \(n = k + 1\).

**Conclusion**: true for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so \(S_n = (n + 1)! - 1\) for all positive integers \(n\) by induction.
:::

The same approach works for derivatives. The first few derivatives show a pattern, and the inductive step differentiates the assumed formula once more.

:::eg (Exam style) Find the first three derivatives of \(y = x\mathrm{e}^x\), conjecture a formula for the \(n\)th derivative \(\dfrac{d^ny}{dx^n}\), and prove it by induction.
By the product rule,
\[\frac{dy}{dx} = (x + 1)\mathrm{e}^x \qquad \frac{d^2y}{dx^2} = (x + 2)\mathrm{e}^x \qquad \frac{d^3y}{dx^3} = (x + 3)\mathrm{e}^x\] [B1]
The pattern suggests \(\dfrac{d^ny}{dx^n} = (x + n)\mathrm{e}^x\). [B1]

**Base case**, \(n = 1\): \((x + 1)\mathrm{e}^x\), as above. True. [B1]

**Assumption**: assume \(\dfrac{d^ky}{dx^k} = (x + k)\mathrm{e}^x\). [B1]

**Inductive step**: differentiate once more with the product rule:
\[\frac{d^{k+1}y}{dx^{k+1}} = \frac{d}{dx}\left[(x + k)\mathrm{e}^x\right] = \mathrm{e}^x + (x + k)\mathrm{e}^x\] [M1]
\[= (x + k + 1)\mathrm{e}^x\] [A1]
This is the formula with \(n = k + 1\).

**Conclusion**: true for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction \(\dfrac{d^ny}{dx^n} = (x + n)\mathrm{e}^x\) for all positive integers \(n\). [A1]
:::

:::eg (Exam style) The matrix \(\mathbf{B} = \begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix}\). (a) Find \(\mathbf{B}^2\) and \(\mathbf{B}^3\). (b) Suggest a formula for \(\mathbf{B}^n\). (c) Prove your formula by induction.
**(a)**
\[\mathbf{B}^2 = \begin{pmatrix} 9 - 4 & -6 + 2 \\ 6 - 2 & -4 + 1 \end{pmatrix} = \begin{pmatrix} 5 & -4 \\ 4 & -3 \end{pmatrix}\] [M1 A1]
\[\mathbf{B}^3 = \mathbf{B}^2\mathbf{B} = \begin{pmatrix} 15 - 8 & -10 + 4 \\ 12 - 6 & -8 + 3 \end{pmatrix} = \begin{pmatrix} 7 & -6 \\ 6 & -5 \end{pmatrix}\] [A1]
**(b)** The entries go up by 2 each time: \(\mathbf{B}^n = \begin{pmatrix} 1 + 2n & -2n \\ 2n & 1 - 2n \end{pmatrix}\), which fits \(n = 1, 2, 3\). [B1]

**(c)** *Base case*, \(n = 1\): the formula gives \(\begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix} = \mathbf{B}\). True. [B1]
*Assumption*: assume \(\mathbf{B}^k = \begin{pmatrix} 1 + 2k & -2k \\ 2k & 1 - 2k \end{pmatrix}\). [B1]
*Inductive step*:
\[\mathbf{B}^{k+1} = \mathbf{B}^k\mathbf{B} = \begin{pmatrix} 1 + 2k & -2k \\ 2k & 1 - 2k \end{pmatrix}\begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 3 + 6k - 4k & -2 - 4k + 2k \\ 6k + 2 - 4k & -4k - 1 + 2k \end{pmatrix} = \begin{pmatrix} 3 + 2k & -2 - 2k \\ 2 + 2k & -1 - 2k \end{pmatrix}\] [A1]
This is \(\begin{pmatrix} 1 + 2(k + 1) & -2(k + 1) \\ 2(k + 1) & 1 - 2(k + 1) \end{pmatrix}\), the formula for \(n = k + 1\).
*Conclusion*: true for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
:::

:::board
Edexcel Further Mathematics (9FM0, Core Pure) also proves results by induction, with the same types: sums of series, divisibility and powers of a matrix. The layout (base case, assumption, inductive step, conclusion) is the same as the one used here.
:::

:::exam Setting out a proof by induction
Use the layout of this chapter every time: base case with both sides shown, the assumption written out, the target for \(n = k + 1\), working that visibly uses the assumption, and a full conclusion. "Prove" and "show that" mean that every line must be justified, and a final line must arrive at the given result exactly. MF19 gives \(\sum r\), \(\sum r^2\) and \(\sum r^3\), but a question that says "prove by induction" wants induction, not a quoted formula. In a divisibility proof, say why each piece is a multiple of the divisor. Where the base case is not \(n = 1\) (for example "\(n \ge 5\)"), start at the stated value, and say "for all integers \(n \ge 5\)" in the conclusion.
:::

:::eg Spot the error: prove by induction that \(\displaystyle\sum_{r=1}^{n} r(r + 1) = \tfrac13 n(n + 1)(n + 2)\) for all positive integers \(n\). (5 marks)
A student wrote this answer.

Line 1: When \(n = 1\), LHS \(= 1 \times 2 = 2\) and RHS \(= \tfrac13 \times 1 \times 2 \times 3 = 2\). True for \(n = 1\).
Line 2: Assume true for \(n = k\): \(\displaystyle\sum_{r=1}^{k} r(r + 1) = \tfrac13 k(k + 1)(k + 2)\).
Line 3: Then \(\displaystyle\sum_{r=1}^{k+1} r(r + 1) = \tfrac13 k(k + 1)(k + 2) + (k + 1)(k + 2)\)
Line 4: \(= (k + 1)(k + 2)\left(\tfrac13 k + 1\right) = \tfrac13(k + 1)(k + 2)(k + 3)\)
Line 5: So the result is true for \(n = k + 1\).

Line 1 checks the base case with both sides. [B1]
Line 2 states the assumption for one value of \(k\). [B1]
Lines 3 and 4 add the next term, use the assumption, factorise and reach the \(n = k + 1\) formula. [M1] [A1]

**Line 5 is an incomplete conclusion, so the final mark is lost.** [A0] A correct conclusion says that the result is true for \(n = 1\), that if it is true for \(n = k\) then it is true for \(n = k + 1\), and that by mathematical induction it is true for all positive integers \(n\). The student scores 4 out of 5.

Correct line 5: "The result is true for \(n = 1\). If it is true for \(n = k\), then it is true for \(n = k + 1\). So by mathematical induction it is true for all positive integers \(n\)." [A1]
:::

:::try Start easy, finish at exam standard
Q: For \(P(n)\): \(\displaystyle\sum_{r=1}^{n} r^2 = \tfrac16 n(n + 1)(2n + 1)\), write down \(P(k)\) and the target \(P(k + 1)\).
A: \(P(k)\): \(\displaystyle\sum_{r=1}^{k} r^2 = \tfrac16 k(k + 1)(2k + 1)\). Target \(P(k + 1)\): \(\displaystyle\sum_{r=1}^{k+1} r^2 = \tfrac16(k + 1)(k + 2)(2k + 3)\).
Q: Prove by induction that \(\displaystyle\sum_{r=1}^{n} (2r - 1) = n^2\).
A: Base case: \(n = 1\): LHS \(= 1\), RHS \(= 1\). Assume \(\displaystyle\sum_{r=1}^{k} (2r - 1) = k^2\). Then \(\displaystyle\sum_{r=1}^{k+1} (2r - 1) = k^2 + 2(k + 1) - 1 = k^2 + 2k + 1 = (k + 1)^2\). True for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
Q: Prove by induction that \(\displaystyle\sum_{r=1}^{n} 2^{r-1} = 2^n - 1\).
A: Base case: \(n = 1\): LHS \(= 2^0 = 1\), RHS \(= 2 - 1 = 1\). Assume the result for \(n = k\). Then \(\displaystyle\sum_{r=1}^{k+1} 2^{r-1} = 2^k - 1 + 2^k = 2 \times 2^k - 1 = 2^{k+1} - 1\). True for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
Q: Prove by induction that \(4^n + 5\) is divisible by 3 for all positive integers \(n\).
A: Base case: \(4 + 5 = 9 = 3 \times 3\). Assume \(4^k + 5\) is divisible by 3. Then \(\left(4^{k+1} + 5\right) - \left(4^k + 5\right) = 3 \times 4^k\), a multiple of 3. So \(4^{k+1} + 5\) is a multiple of 3 plus a multiple of 3. True for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
Q: A sequence has \(u_1 = 1\) and \(u_{n+1} = u_n + 2n + 1\). Prove by induction that \(u_n = n^2\).
A: Base case: \(u_1 = 1 = 1^2\). Assume \(u_k = k^2\). Then \(u_{k+1} = k^2 + 2k + 1 = (k + 1)^2\). True for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
Q: A sequence has \(u_1 = 1\) and \(u_{n+1} = 2u_n + 1\). Find the first four terms and conjecture a formula for \(u_n\).
A: \(u_1 = 1\), \(u_2 = 3\), \(u_3 = 7\), \(u_4 = 15\), each one less than a power of 2: the conjecture is \(u_n = 2^n - 1\).
Q: Show that \(\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}\) for all positive integers \(n\).
A: Base case: \(n = 1\) gives the matrix itself. Assume the result for \(n = k\). Then \(\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & k + 1 \\ 0 & 1 \end{pmatrix}\). True for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
Q: A student checks that \(n^2 - n + 11\) is prime for \(n = 1, 2, 3, 4, 5\) and says the proof is complete. Why is it not, and what would be a counterexample?
A: Five cases do not prove a statement for every \(n\), and no inductive step has been shown. At \(n = 11\), \(121 - 11 + 11 = 121 = 11^2\), which is not prime.
Q: Prove by induction that \(6^n - 1\) is divisible by 5 for all positive integers \(n\).
A: Base case: \(6 - 1 = 5\). Assume \(6^k - 1 = 5m\). Then \(6^{k+1} - 1 = 6(6^k - 1) + 5 = 30m + 5 = 5(6m + 1)\). True for \(n = 1\) and true for \(k\) implies true for \(k + 1\), so true for all positive integers \(n\) by induction.
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ Prove by mathematical induction that \(\displaystyle\sum_{r=1}^{n} (3r - 1) = \tfrac12 n(3n + 1)\) for all positive integers \(n\).
A: Base case, \(n = 1\): LHS \(= 2\) and RHS \(= \tfrac12 \times 4 = 2\). [B1]
Assume \(\displaystyle\sum_{r=1}^{k} (3r - 1) = \tfrac12 k(3k + 1)\). [B1]
\(\displaystyle\sum_{r=1}^{k+1} (3r - 1) = \tfrac12 k(3k + 1) + 3(k + 1) - 1\) [M1]
\(= \tfrac12\left(3k^2 + k + 6k + 4\right) = \tfrac12(3k + 4)(k + 1) = \tfrac12(k + 1)\left(3(k + 1) + 1\right)\). [A1]
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
Q: [5 marks] ★ Prove by mathematical induction that \(5^n - 1\) is divisible by 4 for all positive integers \(n\).
A: Base case, \(n = 1\): \(5 - 1 = 4\), divisible by 4. [B1]
Assume \(5^k - 1\) is divisible by 4, so \(5^k - 1 = 4m\). [B1]
\(5^{k+1} - 1 = 5(5^k - 1) + 4\) [M1] \(= 20m + 4 = 4(5m + 1)\), divisible by 4. [A1]
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
Q: [5 marks] ★★ The sequence \(u_n\) is defined by \(u_1 = 3\) and \(u_{n+1} = 3u_n - 4\). Prove by induction that \(u_n = 3^{n-1} + 2\) for all positive integers \(n\).
A: Base case, \(n = 1\): \(3^0 + 2 = 3 = u_1\). [B1]
Assume \(u_k = 3^{k-1} + 2\). [B1]
\(u_{k+1} = 3u_k - 4 = 3\left(3^{k-1} + 2\right) - 4\) [M1] \(= 3^k + 6 - 4 = 3^k + 2 = 3^{(k+1)-1} + 2\). [A1]
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
Q: [5 marks] ★★ The matrix \(\mathbf{C} = \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix}\). Prove by induction that \(\mathbf{C}^n = \begin{pmatrix} 1 & 0 \\ 3(2^n - 1) & 2^n \end{pmatrix}\) for all positive integers \(n\).
A: Base case, \(n = 1\): the formula gives \(\begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix} = \mathbf{C}\). [B1]
Assume \(\mathbf{C}^k = \begin{pmatrix} 1 & 0 \\ 3(2^k - 1) & 2^k \end{pmatrix}\). [B1]
\(\mathbf{C}^{k+1} = \mathbf{C}^k\mathbf{C} = \begin{pmatrix} 1 & 0 \\ 3(2^k - 1) & 2^k \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix}\) [M1]
\(= \begin{pmatrix} 1 & 0 \\ 3 \times 2^k - 3 + 3 \times 2^k & 2^{k+1} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 3(2^{k+1} - 1) & 2^{k+1} \end{pmatrix}\). [A1]
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
Q: [5 marks] ★★ Prove by induction that \(\dfrac{d^n}{dx^n}\left(x\mathrm{e}^{-x}\right) = (-1)^n(x - n)\mathrm{e}^{-x}\) for all positive integers \(n\).
A: Base case, \(n = 1\): \(\dfrac{d}{dx}(x\mathrm{e}^{-x}) = \mathrm{e}^{-x} - x\mathrm{e}^{-x} = (1 - x)\mathrm{e}^{-x}\), and the formula gives \(-(x - 1)\mathrm{e}^{-x}\). True. [B1]
Assume \(\dfrac{d^k}{dx^k}\left(x\mathrm{e}^{-x}\right) = (-1)^k(x - k)\mathrm{e}^{-x}\). [B1]
Differentiate: \((-1)^k\left[\mathrm{e}^{-x} - (x - k)\mathrm{e}^{-x}\right]\) [M1] \(= (-1)^k(1 + k - x)\mathrm{e}^{-x} = (-1)^{k+1}\left(x - (k + 1)\right)\mathrm{e}^{-x}\). [A1]
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
Q: [8 marks] ★★ Let \(S_n = \dfrac{1}{1 \times 3} + \dfrac{1}{3 \times 5} + \dots + \dfrac{1}{(2n - 1)(2n + 1)}\). (a) Find \(S_1\), \(S_2\) and \(S_3\), and conjecture a formula for \(S_n\). (b) Prove your formula by induction.
A: (a) \(S_1 = \dfrac13\), \(S_2 = \dfrac13 + \dfrac{1}{15} = \dfrac25\), \(S_3 = \dfrac25 + \dfrac{1}{35} = \dfrac37\). [B1 B1]
Conjecture: \(S_n = \dfrac{n}{2n + 1}\). [B1]
(b) Base case, \(n = 1\): \(\dfrac{1}{3}\), as found. [B1]
Assume \(S_k = \dfrac{k}{2k + 1}\). [B1]
\(S_{k+1} = \dfrac{k}{2k + 1} + \dfrac{1}{(2k + 1)(2k + 3)} = \dfrac{k(2k + 3) + 1}{(2k + 1)(2k + 3)}\) [M1]
\(= \dfrac{(2k + 1)(k + 1)}{(2k + 1)(2k + 3)} = \dfrac{k + 1}{2(k + 1) + 1}\). [A1]
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
Q: [10 marks] (#math.fm.series) ★★★ (a) Use the standard results for \(\sum r^2\) and \(\sum r\) to show that \(\displaystyle\sum_{r=1}^{n} r(r + 2) = \tfrac16 n(n + 1)(2n + 7)\). (b) Prove the same result by induction. (c) Hence find \(\displaystyle\sum_{r=11}^{30} r(r + 2)\).
H: In (a), write \(r(r + 2) = r^2 + 2r\) and factorise \(n(n + 1)\) out of the sum of the two standard results.
H: In (b), the target for \(n = k + 1\) is \(\tfrac16(k + 1)(k + 2)(2k + 9)\); factorise \((k + 1)\) from the two terms you have.
H: In (c), find the sum to 30 terms and subtract the sum to 10 terms.
A: (a) \(\displaystyle\sum_{r=1}^{n} (r^2 + 2r) = \tfrac16 n(n + 1)(2n + 1) + 2 \times \tfrac12 n(n + 1)\) [M1 A1]
\(= \tfrac16 n(n + 1)\left[(2n + 1) + 6\right] = \tfrac16 n(n + 1)(2n + 7)\). [A1]
(b) Base case, \(n = 1\): LHS \(= 1 \times 3 = 3\) and RHS \(= \tfrac16 \times 1 \times 2 \times 9 = 3\). [B1] Assume the result for \(n = k\). [B1]
\(\displaystyle\sum_{r=1}^{k+1} r(r + 2) = \tfrac16 k(k + 1)(2k + 7) + (k + 1)(k + 3)\) [M1]
\(= \tfrac16(k + 1)\left[2k^2 + 7k + 6k + 18\right] = \tfrac16(k + 1)(k + 2)(2k + 9)\), [A1] the formula with \(n = k + 1\).
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
(c) The sum from 11 to 30 is \(S_{30} - S_{10} = \tfrac16 \times 30 \times 31 \times 67 - \tfrac16 \times 10 \times 11 \times 27\) [M1] \(= 10385 - 495 = 9890\). [A1]
Q: [12 marks] ★★★ The matrix \(\mathbf{D} = \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}\). (a) Find \(\mathbf{D}^2\) and \(\mathbf{D}^3\). (b) Suggest a formula for \(\mathbf{D}^n\). (c) Prove your formula by induction. (d) Use your formula to show that \(\det(\mathbf{D}^n) = 1\) for every positive integer \(n\), and explain why this agrees with \(\det\mathbf{D}\).
H: Multiply \(\mathbf{D}^2\) by \(\mathbf{D}\) to get \(\mathbf{D}^3\), then look at how each entry changes with \(n\).
H: In the inductive step, find \(\mathbf{D}^k\mathbf{D}\) one entry at a time and compare each with \(\mathbf{D}^{k+1}\) from your formula.
H: For (d), use \(ad - bc\) on your formula and expand.
A: (a) \(\mathbf{D}^2 = \begin{pmatrix} 4 - 1 & 2 \\ -2 & -1 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ -2 & -1 \end{pmatrix}\) [M1 A1] and \(\mathbf{D}^3 = \mathbf{D}^2\mathbf{D} = \begin{pmatrix} 4 & 3 \\ -3 & -2 \end{pmatrix}\). [A1]
(b) \(\mathbf{D}^n = \begin{pmatrix} n + 1 & n \\ -n & 1 - n \end{pmatrix}\). [B1]
(c) Base case, \(n = 1\): \(\begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix} = \mathbf{D}\). [B1] Assume \(\mathbf{D}^k = \begin{pmatrix} k + 1 & k \\ -k & 1 - k \end{pmatrix}\). [B1]
\(\mathbf{D}^{k+1} = \mathbf{D}^k\mathbf{D} = \begin{pmatrix} k + 1 & k \\ -k & 1 - k \end{pmatrix}\begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}\) [M1]
\(= \begin{pmatrix} 2k + 2 - k & k + 1 \\ -2k - 1 + k & -k \end{pmatrix} = \begin{pmatrix} k + 2 & k + 1 \\ -k - 1 & -k \end{pmatrix}\), [A1] which is the formula for \(n = k + 1\).
True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\). So by mathematical induction true for all positive integers \(n\). [A1]
(d) \(\det(\mathbf{D}^n) = (n + 1)(1 - n) - n(-n) = 1 - n^2 + n^2 = 1\). [M1 A1]
\(\det\mathbf{D} = 0 + 1 = 1\) and \(\det(\mathbf{D}^n) = (\det\mathbf{D})^n = 1\), which agrees. [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ Prove by induction that \(2^n > n^2\) for all integers \(n \ge 5\). (Check \(n = 2, 3, 4\) to see why the base case must be 5.)
H: Check the first few cases: \(2^2 = 4 = 2^2\), \(2^3 = 8 < 9\), \(2^4 = 16 = 4^2\). The inequality first holds at \(n = 5\).
H: From \(2^k > k^2\), double both sides: \(2^{k+1} > 2k^2\). Then show \(2k^2 \ge (k + 1)^2\) when \(k \ge 5\).
A: Base case, \(n = 5\): \(2^5 = 32 > 25 = 5^2\). [B1]
Assume \(2^k > k^2\) for some integer \(k \ge 5\). [B1]
Then \(2^{k+1} = 2 \times 2^k > 2k^2\). [M1]
Now \(2k^2 - (k + 1)^2 = k^2 - 2k - 1 = (k - 1)^2 - 2\), which is at least \(16 - 2 = 14 > 0\) for \(k \ge 5\). [M1 A1]
So \(2^{k+1} > 2k^2 > (k + 1)^2\). [A1]
True for \(n = 5\); if true for \(n = k\) (\(k \ge 5\)) then true for \(n = k + 1\). So by mathematical induction true for all integers \(n \ge 5\). [A1]
Q: [7 marks] ★★★ A sequence has \(u_1 = 1\), \(u_2 = 5\) and \(u_{n+2} = 5u_{n+1} - 6u_n\). Prove by induction that \(u_n = 3^n - 2^n\) for all positive integers \(n\). (Here the step from \(n = k + 2\) needs two earlier terms, so the assumption and the base case each cover two values.)
H: Check the formula for both \(n = 1\) and \(n = 2\).
H: Assume it is true for \(n = k\) **and** \(n = k + 1\), and substitute both into the recurrence.
A: Base cases: \(n = 1\): \(3 - 2 = 1 = u_1\); \(n = 2\): \(9 - 4 = 5 = u_2\). True for \(n = 1\) and \(n = 2\). [B1 B1]
Assume the result is true for \(n = k\) and \(n = k + 1\): \(u_k = 3^k - 2^k\) and \(u_{k+1} = 3^{k+1} - 2^{k+1}\). [B1]
\(u_{k+2} = 5u_{k+1} - 6u_k = 5\left(3^{k+1} - 2^{k+1}\right) - 6\left(3^k - 2^k\right)\) [M1]
\(= 15 \times 3^k - 10 \times 2^k - 6 \times 3^k + 6 \times 2^k = 9 \times 3^k - 4 \times 2^k\) [A1]
\(= 3^{k+2} - 2^{k+2}\), the formula for \(n = k + 2\). [A1]
True for \(n = 1\) and \(n = 2\); if true for \(n = k\) and \(n = k + 1\) then true for \(n = k + 2\). So by mathematical induction true for all positive integers \(n\). [A1]
:::

:::quiz
? What is the purpose of the base case in a proof by induction?
+ It shows the result is true for the first value, so the chain of implications has a start
- It proves the result for all values of \(n\)
- It is only a check that the formula looks sensible
- It shows that the inductive step is correct
> Without a first domino the chain never starts. The inductive step alone only says "if true for \(k\) then true for \(k + 1\)", which is true even for a false statement like \(n = n + 1\).
? Which sentence is the correct assumption?
- Assume the result is true for all positive integers \(n\)
+ Assume the result is true for \(n = k\)
- Assume the result is true for \(n = k + 1\)
- Assume the result is false for \(n = k\)
> You assume the result for one value \(k\) and prove it for \(k + 1\). Assuming it for all \(n\) is the conclusion; assuming it for \(k + 1\) is the target you must reach.
? In the inductive step for \(\sum_{r=1}^{n} r^2 = \tfrac16 n(n + 1)(2n + 1)\), which term is added to the assumed sum?
+ \((k + 1)^2\)
- \(k^2\)
- \(\tfrac16(k + 1)(k + 2)(2k + 3)\)
- \(n^2\)
> The sum to \(k + 1\) terms is the sum to \(k\) terms plus the \((k + 1)\)th term, \((k + 1)^2\). Adding \(k^2\) again repeats a term and the target is the answer, not something you add.
? A divisibility proof shows \(f(k + 1) = f(k) + 12 \times 5^k\), where \(f(k)\) is divisible by 12. What can you conclude?
+ \(f(k + 1)\) is divisible by 12
- \(f(k + 1)\) is divisible by 5
- Nothing, because \(5^k\) is not a multiple of 12
- \(f(k)\) is divisible by \(12 \times 5^k\)
> Both \(f(k)\) (by the assumption) and \(12 \times 5^k\) are multiples of 12, so their sum is a multiple of 12. It does not matter that \(5^k\) alone is not.
? A statement is true for \(n = 1, 2, 3, 4, 5\). Which is the best conclusion?
- It is true for all \(n\)
- It is probably true for all \(n\), and so is proved
+ Nothing is proved: it needs an inductive step, and a general proof
- It is false
> Cases do not prove a general statement: \(n^2 + n + 41\) is prime for \(n = 0\) to 39 and then fails. Use the cases to guess a formula, and then prove it.
? What is the best finish to a proof by induction?
+ True for \(n = 1\); if true for \(n = k\) then true for \(n = k + 1\); so true for all positive integers \(n\) by induction
- Hence the result is proved
- So the result is true for \(n = k + 1\)
- Therefore the formula works for \(n = 1\) and \(n = k\)
> The conclusion must combine the base case and the inductive step and name the induction. A bare "hence proved" or "true for \(k + 1\)" loses the final mark.
:::

:::checklist What you can now do
- [ ] I can set out a proof by induction with base case, assumption, inductive step and conclusion.
- [ ] I can prove a formula for a sum, for example \(\sum r^3\) or \(\sum r\,2^r\), by adding the \((k + 1)\)th term.
- [ ] I can prove that an expression is divisible by a given integer, using \(f(k + 1) - f(k)\) or \(f(k + 1) - mf(k)\).
- [ ] I can prove a formula for the \(n\)th term of a recurrence relation such as \(u_{n+1} = 3u_n - 1\).
- [ ] I can prove a formula for the \(n\)th power of a 2×2 matrix.
- [ ] I can work out a few cases, conjecture a formula (for example for \(\sum r \times r!\) or the \(n\)th derivative of \(x\mathrm{e}^x\)) and prove it by induction.
- [ ] I can recognise that a pattern checked for a few cases is not a proof, and use induction with a base case other than \(n = 1\).
:::

:::recap
- Four steps: **base case** (\(n = 1\), both sides shown), **assumption** (true for \(n = k\), written out), **inductive step** (show \(n = k + 1\), using the assumption), **conclusion** (true for \(n = 1\), \(k\) implies \(k + 1\), so true for all positive integers \(n\) by induction).
- Marks: B1 base case, B1 assumption, M1 A1 inductive step, A1 conclusion.
- Sums: add the \((k + 1)\)th term to the assumed sum and factorise to match the target.
- Divisibility: write \(f(k + 1) - f(k)\) or \(f(k + 1) - mf(k)\) as a multiple of the divisor, and say why each piece is a multiple.
- Recurrences: substitute the assumed formula for \(u_k\) into \(u_{k+1} = \dots\). Matrices: \(\mathbf{M}^{k+1} = \mathbf{M}^k\mathbf{M}\). Derivatives: differentiate the assumed \(n\)th derivative once more.
- Conjecture from the first few cases, then prove; a pattern is never a proof.
- Never "assume true for all \(n\)", always use the assumption in the working, and never omit the conclusion.
:::

:::links
- watch: [Induction: divisibility proofs](https://www.examsolutions.net/tutorials/divisibility-and-multiple-test-proofs/) · ExamSolutions · the divisibility method step by step
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · find the induction tutorials for sums and matrices in the Further Pure list
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · free induction booklet with answers
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 induction questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Rational functions and their graphs](#math.fm.rational) turns to sketching curves such as \(y = \dfrac{x^2 + 1}{x - 2}\), with asymptotes and the set of values the function takes.
