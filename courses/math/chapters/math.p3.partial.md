@chapter math.p3.partial
@title Partial fractions and the binomial series
@level a2
@paper CAIE P3 · Edexcel IAL P4 · AQA/OCR/Edexcel Pure Year 2
@time 8–10 hours
@summary Splitting a single algebraic fraction into simpler ones (partial fractions) for three types of denominator, and the binomial expansion of \((1 + x)^n\) for fractional and negative \(n\), including its range of validity. Both tools are combined to expand fractions.

:::why
Adding fractions merges them into one; partial fractions run that process backwards. A fraction like \(\dfrac{5x + 1}{(x - 1)(x + 2)}\) is hard to integrate or expand, but its parts \(\dfrac{2}{x - 1}\) and \(\dfrac{3}{x + 2}\) are easy. The binomial series extends the expansion of \((1 + x)^n\) from whole-number powers to square roots and reciprocals, and gives accurate approximations in science, such as relativistic energy. Both ideas are the algebra behind [Integration techniques](#math.p3.inttech).
:::

**Before you start**, you need algebraic fractions and factorising from [Algebra from scratch](#math.f.algebra), the binomial theorem for positive integers from [Series](#math.p1.series), negative and fractional indices from [Indices, surds and standard form](#math.f.powers), and the factor theorem from [Modulus and polynomials](#math.p3.algebra).

:::try Warm-up
Q: Expand \((1 + x)^4\) up to the term in \(x^2\). (from [Series](#math.p1.series))
A: \(1 + 4x + 6x^2 + \cdots\)
Q: Show that \((x - 2)\) is a factor of \(x^3 - 3x^2 + 4\). (from [Modulus and polynomials](#math.p3.algebra))
A: Put \(x = 2\): \(8 - 12 + 4 = 0\), so by the factor theorem \((x - 2)\) is a factor.
Q: Simplify \(\left(\dfrac14\right)^{-1/2}\). (from [Indices, surds and standard form](#math.f.powers))
A: A negative power turns the fraction over: \(4^{1/2} = 2\).
:::

## Partial fractions

:::def Partial fractions
Writing a single algebraic fraction as a sum of simpler fractions, each with a denominator that is one of the factors of the original denominator. For the syllabus, the numerator must have a lower degree than the denominator (a "proper" fraction).
:::

Start with what happens when you add: \(\dfrac{2}{x - 1} + \dfrac{3}{x + 2}\) \(= \dfrac{2(x + 2) + 3(x - 1)}{(x - 1)(x + 2)}\) \(= \dfrac{5x + 1}{(x - 1)(x + 2)}\). Partial fractions go from the right to the left.

There are three types of denominator in the syllabus. Each has its own template.

:::key Partial fraction templates
For a proper fraction (numerator degree lower than the denominator):
- **Distinct linear factors:** \(\dfrac{f(x)}{(ax+b)(cx+d)}\) \(= \dfrac{A}{ax+b} + \dfrac{B}{cx+d}\), and likewise for three factors.
- **A repeated linear factor:** \(\dfrac{f(x)}{(ax+b)(cx+d)^2}\) \(= \dfrac{A}{ax+b} + \dfrac{B}{cx+d} + \dfrac{C}{(cx+d)^2}\). A squared factor needs **two** terms, one for each power.
- **A quadratic factor that does not factorise:** \(\dfrac{f(x)}{(ax+b)(cx^2+d)}\) \(= \dfrac{A}{ax+b} + \dfrac{Bx+C}{cx^2+d}\). The numerator over the quadratic is **linear**.
:::

To find the constants, multiply both sides by the whole denominator and use **substitution** (put in the value of \(x\) that makes a factor zero) and **comparing coefficients** (match the coefficients of \(x^2\), \(x\) and the constant).

:::eg Express \(\dfrac{5x + 1}{(x - 1)(x + 2)}\) in partial fractions.
Write \(\dfrac{5x + 1}{(x - 1)(x + 2)}\) \(= \dfrac{A}{x - 1} + \dfrac{B}{x + 2}\). Multiply by \((x - 1)(x + 2)\):
\[5x + 1 = A(x + 2) + B(x - 1)\]
Put \(x = 1\): \(6 = 3A\), so \(A = 2\). Put \(x = -2\): \(-9 = -3B\), so \(B = 3\). Therefore
\[\frac{5x + 1}{(x - 1)(x + 2)} = \frac{2}{x - 1} + \frac{3}{x + 2}\]
Check at \(x = 0\): the left side is \(\dfrac{1}{-2} = -0.5\), and the right is \(-2 + 1.5 = -0.5\). ✓
:::

:::proof Why substituting a special value of x finds a constant (the cover-up rule)
Suppose the denominator has a factor \((x - a)\) that appears once: \(\dfrac{\mathrm{f}(x)}{(x - a)\,\mathrm{g}(x)}\) \(= \dfrac{A}{x - a} + \dfrac{\mathrm{h}(x)}{\mathrm{g}(x)}\). The last fraction stands for all the other partial fractions.
Multiply both sides by \((x - a)\). The left side becomes \(\dfrac{\mathrm{f}(x)}{\mathrm{g}(x)}\). The right side becomes \(A + \dfrac{(x - a)\,\mathrm{h}(x)}{\mathrm{g}(x)}\).
This is true for every \(x\), so it is true at \(x = a\). There the last term has the factor \((x - a) = 0\), and \(\mathrm{g}(a) \ne 0\) because \((x - a)\) appeared only once. So \(\dfrac{\mathrm{f}(a)}{\mathrm{g}(a)}\) \(= A\).
In words: cover up the factor \((x - a)\) in the original fraction, then put \(x = a\) into what is left. For \(\dfrac{5x + 1}{(x - 1)(x + 2)}\): cover \((x - 1)\) and put \(x = 1\) to get \(A = \dfrac{6}{3} = 2\).
For a squared factor, multiplying by \((x + 2)^2\) leaves \(C + B(x + 2) + \cdots\). Putting \(x = -2\) kills the \(B\) term as well, so you get \(C\) only. That is why \(B\) needs a second method, such as comparing coefficients.
:::

:::eg Express \(\dfrac{2x^2 + 5x - 1}{(x - 1)(x + 1)(x + 2)}\) in partial fractions.
Let it equal \(\dfrac{A}{x - 1} + \dfrac{B}{x + 1} + \dfrac{C}{x + 2}\). Then
\[2x^2 + 5x - 1 = A(x + 1)(x + 2) + B(x - 1)(x + 2) + C(x - 1)(x + 1)\]

\(x = 1\): \(6 = 6A\), so \(A = 1\). \(x = -1\): \(-4 = -2B\), so \(B = 2\). \(x = -2\): \(-3 = 3C\), so \(C = -1\).
\[\frac{2x^2 + 5x - 1}{(x - 1)(x + 1)(x + 2)} = \frac{1}{x - 1} + \frac{2}{x + 1} - \frac{1}{x + 2}\]
:::

For a repeated factor, substitution finds two of the constants. Find the third by comparing a coefficient or by putting in another convenient value of \(x\).

:::eg Express \(\dfrac{5x^2 + 10x + 3}{(x - 1)(x + 2)^2}\) in partial fractions.
Let it equal \(\dfrac{A}{x - 1} + \dfrac{B}{x + 2} + \dfrac{C}{(x + 2)^2}\). Then
\[5x^2 + 10x + 3 = A(x + 2)^2 + B(x - 1)(x + 2) + C(x - 1)\]
\(x = 1\): \(18 = 9A\), so \(A = 2\). \(x = -2\): \(20 - 20 + 3 = 3 = -3C\), so \(C = -1\). Compare the coefficients of \(x^2\): \(5 = A + B\), so \(B = 3\).
\[\frac{5x^2 + 10x + 3}{(x - 1)(x + 2)^2} = \frac{2}{x - 1} + \frac{3}{x + 2} - \frac{1}{(x + 2)^2}\]
Check at \(x = 0\): the left side is \(\dfrac{3}{-4} = -0.75\), and the right is \(-2 + 1.5 - 0.25 = -0.75\). ✓
:::

:::eg Express \(\dfrac{5x^2 + 2x + 7}{(x + 1)(x^2 + 4)}\) in partial fractions.
Let it equal \(\dfrac{A}{x + 1} + \dfrac{Bx + C}{x^2 + 4}\). Then \(5x^2 + 2x + 7\) \(= A(x^2 + 4) + (Bx + C)(x + 1)\).

\(x = -1\): \(5 - 2 + 7 = 10 = 5A\), so \(A = 2\). Compare \(x^2\) terms: \(5 = A + B\), so \(B = 3\). Compare constants: \(7 = 4A + C\), so \(C = -1\).
\[\frac{5x^2 + 2x + 7}{(x + 1)(x^2 + 4)} = \frac{2}{x + 1} + \frac{3x - 1}{x^2 + 4}\]
Check the \(x\) terms: \(2 = B + C = 3 - 1\). ✓
:::

:::warn Partial fraction slips
- A repeated factor \((x + 2)^2\) needs both \(\dfrac{B}{x + 2}\) and \(\dfrac{C}{(x + 2)^2}\). Leaving out the first loses the answer.
- A quadratic factor such as \(x^2 + 4\) needs a linear numerator \(Bx + C\), not just \(B\).
- Check by putting in a value such as \(x = 0\) or \(x = 1\) on both sides. If the numerator has the same or higher degree than the denominator, divide first (this is outside the syllabus).
:::

## The binomial series for any power

In [Series](#math.p1.series) you expanded \((1 + x)^n\) for positive whole \(n\), which stops after \(n + 1\) terms. The same pattern works for any rational \(n\), such as \(-1\), \(\tfrac12\) or \(-\tfrac32\), but the expansion then goes on for ever and is valid only for some values of \(x\).

:::key Binomial series
For any rational number \(n\) and \(|x| < 1\):
\[(1 + x)^n = 1 + nx + \frac{n(n-1)}{2!}x^2 + \frac{n(n-1)(n-2)}{3!}x^3 + \cdots\]
It is on MF19. If \(n\) is a positive integer the series stops and is valid for all \(x\). Otherwise it has infinitely many terms and only converges for \(|x| < 1\). You never need the general term at Cambridge level: calculate the first few terms.
:::

:::eg Expand in ascending powers of \(x\) up to \(x^3\): (a) \((1 + x)^{-1}\), (b) \((1 + x)^{1/2}\), (c) \((1 - x)^{-2}\). State the range of validity.
(a) \(n = -1\): 
\[1 + (-1)x + \dfrac{(-1)(-2)}{2}x^2 + \dfrac{(-1)(-2)(-3)}{6}x^3 = 1 - x + x^2 - x^3\]

(b) \(n = \tfrac12\): \(1 + \tfrac12 x + \dfrac{\frac12\left(-\frac12\right)}{2}x^2 + \dfrac{\frac12\left(-\frac12\right)\left(-\frac32\right)}{6}x^3\) \(= 1 + \tfrac12 x - \tfrac18 x^2 + \tfrac1{16}x^3\).

(c) Replace \(x\) by \(-x\) in \((1 + x)^{-2}\) \(= 1 - 2x + 3x^2 - 4x^3 + \cdots\): \((1 - x)^{-2}\) \(= 1 + 2x + 3x^2 + 4x^3 + \cdots\)

All three are valid for \(|x| < 1\), that is \(-1 < x < 1\).
:::

### Adapting to \((a + bx)^n\)

When the first term is not \(1\), factor it out: \((a + bx)^n\) \(= a^n\left(1 + \dfrac{bx}{a}\right)^n\). Then apply the series with \(x\) replaced by \(\dfrac{bx}{a}\). The expansion is valid when \(\left|\dfrac{bx}{a}\right| < 1\).

:::eg Expand (a) \((1 + 2x)^{-3}\) up to \(x^3\) and state when it is valid, (b) \((2 - x)^{-1/2}\) up to \(x^2\) and state when it is valid.
(a) Use \(n = -3\) with \(x\) replaced by \(2x\):
\[1 + (-3)(2x) + \frac{(-3)(-4)}{2}(2x)^2 + \frac{(-3)(-4)(-5)}{6}(2x)^3 = 1 - 6x + 24x^2 - 80x^3\]
Valid for \(|2x| < 1\), that is \(|x| < \tfrac12\).

(b) Factor out the 2: \((2 - x)^{-1/2}\) \(= 2^{-1/2}\left(1 - \dfrac x2\right)^{-1/2}\). Use \(n = -\tfrac12\) with \(u = -\dfrac x2\): \((1 + u)^{-1/2}\) \(= 1 - \tfrac12 u + \tfrac38 u^2\), so
\[\left(1 - \tfrac x2\right)^{-1/2} = 1 + \tfrac x4 + \tfrac{3x^2}{32}\]
Therefore \((2 - x)^{-1/2}\) \(= \dfrac{1}{\sqrt2}\left(1 + \tfrac x4 + \tfrac{3x^2}{32} + \cdots\right)\), valid for \(\left|\dfrac x2\right| < 1\), that is \(|x| < 2\).
:::

:::warn Validity and factoring
Factor out the constant **before** expanding, and raise it to the power \(n\): \(\sqrt{4 + x}\) \(= 2\left(1 + \tfrac x4\right)^{1/2}\), not \(4\left(1 + \cdots\right)^{1/2}\). The condition is on \(\left|\dfrac{bx}{a}\right|\), not on \(x\) alone. Write the range as an inequality, such as \(|x| < 2\) or \(-2 < x < 2\).
:::

The series gives approximations. Take a value of \(x\) inside the range and the terms shrink quickly.

:::eg Use \(\sqrt{4 + x}\) \(= 2\left(1 + \tfrac x4\right)^{1/2}\) to approximate \(\sqrt{4.04}\). A particle moves at speed \(v = 0.1c\); the factor \(\gamma\) \(= \left(1 - \dfrac{v^2}{c^2}\right)^{-1/2}\) gives how its mass appears to increase. Approximate \(\gamma\).
Expand \((1 + u)^{1/2}\) \(= 1 + \tfrac12 u - \tfrac18 u^2 + \cdots\) with \(u = \dfrac x4\): \(2\left(1 + \dfrac x8 - \dfrac{x^2}{128}\right)\) \(= 2 + \dfrac x4 - \dfrac{x^2}{64}\). Put \(x = 0.04\): \(2 + 0.01 - 0.000025 = 2.009975\). The calculator gives \(2.00997512\ldots\), so the approximation is accurate to 6 decimal places.

For \(\gamma\), let \(u = -\dfrac{v^2}{c^2} = -0.01\). \((1 + u)^{-1/2}\) \(= 1 - \tfrac12 u + \tfrac38 u^2 - \cdots\) \(= 1 + 0.005 + 0.0000375 = 1.0050375\). The exact value is \(1.0050378\ldots\), so the mass appears to increase by about \(0.5\%\) at one tenth of the speed of light.
:::

## Combining the two

To expand a fraction such as \(\dfrac{5 - x}{(1 + x)(1 - 2x)}\), split it into partial fractions, expand each with the binomial series, and add. The result is valid only where **both** expansions are valid, which is the narrower range.

:::eg (Exam style) (a) Express \(\dfrac{5 - x}{(1 + x)(1 - 2x)}\) in partial fractions. (b) Hence expand the fraction in ascending powers of \(x\) up to and including \(x^3\). (c) State the set of values of \(x\) for which the expansion is valid.
**(a)** Let \(\dfrac{5 - x}{(1 + x)(1 - 2x)}\) \(= \dfrac{A}{1 + x} + \dfrac{B}{1 - 2x}\), so \(5 - x = A(1 - 2x) + B(1 + x)\). [M1]
\(x = -1\): \(6 = 3A\), so \(A = 2\). \(x = \tfrac12\): \(4.5 = 1.5B\), so \(B = 3\). [M1 A1]
\[\frac{5 - x}{(1 + x)(1 - 2x)} = \frac{2}{1 + x} + \frac{3}{1 - 2x}\]

**(b)** \(\dfrac{2}{1 + x} = 2(1 + x)^{-1}\) \(= 2\left(1 - x + x^2 - x^3\right)\), and \(\dfrac{3}{1 - 2x} = 3(1 - 2x)^{-1}\) \(= 3\left(1 + 2x + 4x^2 + 8x^3\right)\). [M1 A1 A1]
\[\text{Sum} = (2 + 3) + (-2 + 6)x + (2 + 12)x^2 + (-2 + 24)x^3 = 5 + 4x + 14x^2 + 22x^3\] [A1]

**(c)** The first expansion needs \(|x| < 1\) and the second needs \(|2x| < 1\), that is \(|x| < \tfrac12\). Both hold when \(|x| < \tfrac12\). [B1]
Check: at \(x = 0.1\) the fraction is \(\dfrac{4.9}{1.1 \times 0.8} = 5.568\); the series gives \(5 + 0.4 + 0.14 + 0.022 = 5.562\). ✓
:::

:::eg (Exam style) The fraction \(\mathrm{f}(x)\) \(= \dfrac{5x^2 + 10x + 3}{(x - 1)(x + 2)^2}\) is given. Write down its partial fractions (found earlier), and hence find the first three terms of the expansion of \(\mathrm{f}(x)\) in ascending powers of \(x\), stating the range of validity.
From the earlier example, \(\mathrm{f}(x)\) \(= \dfrac{2}{x - 1} + \dfrac{3}{x + 2} - \dfrac{1}{(x + 2)^2}\). [B1]

Expand each term, rewriting with \(1\) as the leading term:
\[\frac{2}{x - 1} = -2(1 - x)^{-1} = -2\left(1 + x + x^2 + \cdots\right)\]
\[\frac{3}{x + 2} = \tfrac32\left(1 + \tfrac x2\right)^{-1} = \tfrac32\left(1 - \tfrac x2 + \tfrac{x^2}{4}\right)\]
\[\frac{1}{(x + 2)^2} = \tfrac14\left(1 + \tfrac x2\right)^{-2} = \tfrac14\left(1 - x + \tfrac34x^2\right)\] [M1 A1 A1]
Add: constant \(-2 + \tfrac32 - \tfrac14 = -\tfrac34\); \(x\): \(-2 - \tfrac34 + \tfrac14 = -\tfrac52\); \(x^2\): \(-2 + \tfrac38 - \tfrac3{16}\) \(= -\tfrac{29}{16}\). [M1]
\[\mathrm{f}(x) = -\tfrac34 - \tfrac52x - \tfrac{29}{16}x^2 + \cdots\] [A1]
The expansions need \(|x| < 1\) and \(\left|\tfrac x2\right| < 1\), so it is valid for \(|x| < 1\). [B1]
Check at \(x = 0\): \(\mathrm{f}(0) = -\tfrac34\). ✓
:::

:::exam What earns marks
- Show the form with constants (\(\dfrac{A}{\ldots} + \dfrac{B}{\ldots}\)) and the identity \(\text{numerator}\) \(= A(\ldots) + B(\ldots)\). Each constant is usually its own mark.
- In a binomial expansion, show the unsimplified terms (for example \(\dfrac{(-3)(-4)}{2}(2x)^2\)) before simplifying. A slip in one term still earns the method mark.
- State the validity as an inequality with \(x\) (or \(-a < x < a\)). When combining expansions, give the smaller range.
- Check partial fractions by substituting a simple value such as \(x = 0\).
:::

:::board Other boards
Edexcel IAL covers partial fractions and the binomial series for rational \(n\) in P4. UK A Levels (AQA, Edexcel, OCR) cover them in Pure Year 2. UK specifications also include partial fractions with a numerator of the same or higher degree than the denominator (improper fractions); Cambridge 9709 does not, and excludes the general term of the binomial series.
:::

:::eg Spot the error: the first terms of \((4 + 2x)^{-1/2}\)
A student wrote this answer to "Expand \((4 + 2x)^{-1/2}\) in ascending powers of \(x\) up to \(x^2\), and state when it is valid" [6 marks].

Line 1:
\[(4 + 2x)^{-1/2} = 4^{-1/2}\left(1 + \dfrac x2\right)^{-1/2} = -2\left(1 + \dfrac x2\right)^{-1/2}\]
Line 2: \(\left(1 + \dfrac x2\right)^{-1/2}\) \(= 1 - \dfrac x4 + \dfrac{3x^2}{32}\).
Line 3: \((4 + 2x)^{-1/2}\) \(= -2 + \dfrac x2 - \dfrac{3x^2}{16}\), valid for \(|x| < 2\).

**Line 1 scores [M1 A0].** The method is right: factor out \(4^{-1/2}\) and keep \(1\) as the first term. The value is wrong, because \(4^{-1/2}\) is \(\dfrac{1}{\sqrt4} = \dfrac12\), not \(-2\). A negative power means "reciprocal", not "negative". Line 2 is correct [M1 A1]. Line 3 follows from the student's constant, so it earns follow-through [A1 ft], and the validity is correct [B1]. The student scores 5 out of 6.

Correct working: \(\dfrac12\left(1 - \dfrac x4 + \dfrac{3x^2}{32}\right)\) \(= \dfrac12 - \dfrac x8 + \dfrac{3x^2}{64}\).

**Check:** the expansion of \((4 + 2x)^{-1/2}\) at \(x = 0\) must equal \(4^{-1/2} = 0.5\), which is positive. The student's series starts at \(-2\), so it cannot be right. At \(x = 0.1\): \(4.2^{-1/2} = 0.48795\) and \(0.5 - 0.0125 + 0.00046875 = 0.48797\). ✓
:::

:::try Start easy, finish at exam standard
Q: Express \(\dfrac{4x + 7}{(x + 1)(x + 2)}\) in partial fractions.
A: \(4x + 7 = A(x + 2) + B(x + 1)\). \(x = -1\): \(3 = A\). \(x = -2\): \(-1 = -B\), so \(B = 1\). The result is \(\dfrac{3}{x + 1} + \dfrac{1}{x + 2}\).
Q: Express \(\dfrac{2x^2 - 6x - 2}{x(x - 1)(x + 2)}\) in partial fractions.
A: 
\[2x^2 - 6x - 2 = A(x - 1)(x + 2) + Bx(x + 2) + Cx(x - 1)\] \(x = 0\): \(-2 = -2A\), \(A = 1\). \(x = 1\): \(-6 = 3B\), \(B = -2\). \(x = -2\): \(18 = 6C\), \(C = 3\). The result is \(\dfrac1x - \dfrac{2}{x - 1} + \dfrac{3}{x + 2}\).
Q: Express \(\dfrac{5x^2 - 7x + 6}{(x + 1)(x - 2)^2}\) in partial fractions.
A: Let it equal \(\dfrac{A}{x + 1} + \dfrac{B}{x - 2} + \dfrac{C}{(x - 2)^2}\). Then
\[5x^2 - 7x + 6 = A(x - 2)^2 + B(x + 1)(x - 2) + C(x + 1)\] \(x = -1\): \(18 = 9A\), \(A = 2\). \(x = 2\): \(12 = 3C\), \(C = 4\). Compare \(x^2\): \(5 = A + B\), so \(B = 3\). The result is \(\dfrac{2}{x + 1} + \dfrac{3}{x - 2} + \dfrac{4}{(x - 2)^2}\).
Q: Express \(\dfrac{3x^2 + x - 2}{(x - 1)(x^2 + 1)}\) in partial fractions.
A: Let it equal \(\dfrac{A}{x - 1} + \dfrac{Bx + C}{x^2 + 1}\). Then \(3x^2 + x - 2\) \(= A(x^2 + 1) + (Bx + C)(x - 1)\). \(x = 1\): \(2 = 2A\), \(A = 1\). Compare \(x^2\): \(3 = A + B\), so \(B = 2\). Compare constants: \(-2 = A - C\), so \(C = 3\). The result is \(\dfrac{1}{x - 1} + \dfrac{2x + 3}{x^2 + 1}\).
Q: Expand \((1 - 3x)^{-1/2}\) in ascending powers of \(x\) up to \(x^3\), and state when the expansion is valid.
A: With \(u = -3x\): \(1 - \tfrac12 u + \tfrac38 u^2 - \tfrac{5}{16}u^3\) \(= 1 + \tfrac32 x + \tfrac{27}{8}x^2 + \tfrac{135}{16}x^3\). Valid for \(|3x| < 1\), that is \(|x| < \tfrac13\).
Q: Find the first three terms in the expansion of \((4 + x)^{3/2}\) in ascending powers of \(x\), and state the range of validity.
A: \((4 + x)^{3/2}\) \(= 8\left(1 + \tfrac x4\right)^{3/2}\) \(= 8\left[1 + \tfrac32\cdot\tfrac x4 + \tfrac38\cdot\tfrac{x^2}{16}\right]\) \(= 8 + 3x + \tfrac{3}{16}x^2\). Valid for \(|x| < 4\).
Q: Use the expansion of \((1 + x)^{1/2}\) up to \(x^3\) with \(x = 0.04\) to estimate \(\sqrt{1.04}\) to 6 decimal places.
A: \(1 + \tfrac12 x - \tfrac18 x^2 + \tfrac1{16}x^3\) \(= 1 + 0.02 - 0.0002 + 0.000004\) \(= 1.019804\). The calculator gives \(1.019804\) to 6 d.p.
Q: Express \(\dfrac{4x + 7}{(x + 1)(x + 2)}\) in ascending powers of \(x\) up to \(x^2\), using your partial fractions, and state the range of validity.
A: \(\dfrac{3}{x + 1} + \dfrac{1}{x + 2}\). First term: \(3(1 + x)^{-1} = 3 - 3x + 3x^2\). Second: \(\tfrac12\left(1 + \tfrac x2\right)^{-1}\) \(= \tfrac12 - \tfrac x4 + \tfrac{x^2}{8}\). Sum: \(\tfrac72 - \tfrac{13}{4}x + \tfrac{25}{8}x^2\). Valid for \(|x| < 1\).
Q: (Exam style) (a) Expand \((1 - 2x)^{-1/2}\) in ascending powers of \(x\) up to \(x^3\). (b) Hence find the expansion of \(\dfrac{2 + x}{\sqrt{1 - 2x}}\) up to \(x^3\). (c) State the values of \(x\) for which the expansion is valid.
A: (a) With \(u = -2x\): \(1 - \tfrac12 u + \tfrac38 u^2 - \tfrac5{16}u^3\) \(= 1 + x + \tfrac32x^2 + \tfrac52x^3\). [M1 A1 A1] (b) Multiply by \((2 + x)\): \(2 + 2x + 3x^2 + 5x^3 + x + x^2 + \tfrac32x^3\) \(= 2 + 3x + 4x^2 + \tfrac{13}{2}x^3\). [M1 A1] (c) Valid for \(|2x| < 1\), that is \(|x| < \tfrac12\). [B1]
Q: (Exam style) (a) Express \(\dfrac{5x^2 - 7x + 6}{(x + 1)(x - 2)^2}\) in partial fractions. (b) Hence expand it in ascending powers of \(x\) up to \(x^2\). (c) State the range of validity.
A: (a) \(\dfrac{2}{x + 1} + \dfrac{3}{x - 2} + \dfrac{4}{(x - 2)^2}\). [M1 A1 A1 A1] (b) \(\dfrac{2}{x + 1} = 2(1 - x + x^2)\). \(\dfrac{3}{x - 2}\) \(= -\tfrac32\left(1 - \tfrac x2\right)^{-1}\) \(= -\tfrac32\left(1 + \tfrac x2 + \tfrac{x^2}{4}\right)\). \(\dfrac{4}{(x - 2)^2}\) \(= \left(1 - \tfrac x2\right)^{-2}\) \(= 1 + x + \tfrac34x^2\). [M1 A1] Adding: \(\tfrac32 - \tfrac74x + \tfrac{19}{8}x^2\). [A1] (c) The three expansions need \(|x| < 1\), \(|x| < 2\) and \(|x| < 2\), so \(|x| < 1\). [B1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Express \(\dfrac{7x + 1}{(x + 1)(x - 2)}\) in partial fractions.
A: \(7x + 1 = A(x - 2) + B(x + 1)\). [M1] Put \(x = -1\): \(-6 = -3A\), so \(A = 2\). [A1] Put \(x = 2\): \(15 = 3B\), so \(B = 5\). [A1] The result is \(\dfrac{2}{x + 1} + \dfrac{5}{x - 2}\).
Q: [3 marks] ★ Expand \((1 + 4x)^{-1/2}\) in ascending powers of \(x\) up to \(x^2\), and state the values of \(x\) for which the expansion is valid.
A: With \(u = 4x\): \(1 + \left(-\tfrac12\right)(4x) + \dfrac{\left(-\frac12\right)\left(-\frac32\right)}{2}(4x)^2\). [M1] This is \(1 - 2x + 6x^2\). [A1] It is valid for \(|4x| < 1\), that is \(|x| < \tfrac14\). [B1]
Q: [5 marks] ★★ Express \(\dfrac{4x^2 - 3x + 5}{(x - 1)(x^2 + 2)}\) in partial fractions.
A: Let it equal \(\dfrac{A}{x - 1} + \dfrac{Bx + C}{x^2 + 2}\), so
\[4x^2 - 3x + 5 = A(x^2 + 2) + (Bx + C)(x - 1)\]
[M1] Put \(x = 1\): \(6 = 3A\), so \(A = 2\). [A1] Compare \(x^2\): \(4 = A + B\), so \(B = 2\). [M1 A1] Compare constants: \(5 = 2A - C\), so \(C = -1\). [A1] The result is \(\dfrac{2}{x - 1} + \dfrac{2x - 1}{x^2 + 2}\). (Check the \(x\) terms: \(C - B = -3\). ✓)
Q: [5 marks] ★★ Expand \((2 + 3x)^{-2}\) in ascending powers of \(x\) up to \(x^2\), and state the values of \(x\) for which the expansion is valid.
A: Factor out \(2^{-2}\):
\[(2 + 3x)^{-2} = 2^{-2}\left(1 + \dfrac{3x}{2}\right)^{-2} = \dfrac14\left(1 + \dfrac{3x}{2}\right)^{-2}\]
[M1 A1] With \(u = \dfrac{3x}{2}\): \((1 + u)^{-2} = 1 - 2u + 3u^2\), which is \(1 - 3x + \dfrac{27x^2}{4}\). [M1] So \((2 + 3x)^{-2}\) \(= \dfrac14 - \dfrac{3x}{4} + \dfrac{27x^2}{16}\). [A1] Valid for \(\left|\dfrac{3x}{2}\right| < 1\), that is \(|x| < \tfrac23\). [B1]
Q: [5 marks] ★★ (a) Expand \(\sqrt{1 - 2x}\) in ascending powers of \(x\) up to and including \(x^3\). (b) Use your expansion with \(x = 0.01\) to estimate \(\sqrt{0.98}\) correct to 5 decimal places.
A: (a) With \(n = \tfrac12\) and \(u = -2x\): \(1 + \tfrac12 u - \tfrac18 u^2 + \tfrac1{16}u^3\). [M1] This is \(1 - x - \tfrac12 x^2 - \tfrac12 x^3\). [A1 A1] (b) \(1 - 2(0.01) = 0.98\), so
\[\sqrt{0.98} \approx 1 - 0.01 - 0.00005 - 0.0000005\]
[M1] This is \(0.9899495\), so \(\sqrt{0.98} = 0.98995\) to 5 d.p. [A1]
Q: [10 marks] ★★★ \(\mathrm{f}(x)\) \(= \dfrac{6 - 3x}{(1 - 2x)(1 + x)^2}\). (a) Express \(\mathrm{f}(x)\) in partial fractions. (b) Hence expand \(\mathrm{f}(x)\) in ascending powers of \(x\) up to and including \(x^2\). (c) State the values of \(x\) for which the expansion is valid.
H: Use the form \(\dfrac{A}{1 - 2x} + \dfrac{B}{1 + x} + \dfrac{C}{(1 + x)^2}\) and put \(x = \tfrac12\) and \(x = -1\).
H: Find \(B\) by comparing the coefficients of \(x^2\) on both sides.
H: For (b), write each part as a binomial series: \((1 - 2x)^{-1}\), \((1 + x)^{-1}\) and \((1 + x)^{-2}\).
A: (a)
\[6 - 3x = A(1 + x)^2 + B(1 - 2x)(1 + x) + C(1 - 2x)\]
[M1] Put \(x = \tfrac12\): \(4.5 = 2.25A\), so \(A = 2\). [A1] Put \(x = -1\): \(9 = 3C\), so \(C = 3\). [A1] Compare \(x^2\): \(0 = A - 2B\), so \(B = 1\). [A1] The result is \(\dfrac{2}{1 - 2x} + \dfrac{1}{1 + x} + \dfrac{3}{(1 + x)^2}\). (b)
\[\begin{aligned} 2(1 - 2x)^{-1} &= 2\left(1 + 2x + 4x^2\right) = 2 + 4x + 8x^2 \\ (1 + x)^{-1} &= 1 - x + x^2 \\ 3(1 + x)^{-2} &= 3\left(1 - 2x + 3x^2\right) = 3 - 6x + 9x^2 \end{aligned}\]
[M1 A1 A1 A1] Adding: \(6 - 3x + 18x^2\). [A1] (c) The expansions need \(|2x| < 1\) and \(|x| < 1\), so it is valid for \(|x| < \tfrac12\). [B1]
Q: [13 marks] (#math.p3.algebra) ★★★ \(\mathrm{p}(x) = x^3 - 2x^2 - 5x + 6\). (a) Show that \((x - 3)\) is a factor of \(\mathrm{p}(x)\) and factorise \(\mathrm{p}(x)\) completely. (b) Express \(\dfrac{3x^2 - 14x + 5}{x^3 - 2x^2 - 5x + 6}\) in partial fractions. (c) Hence expand the fraction in ascending powers of \(x\) up to and including \(x^2\), and state the values of \(x\) for which the expansion is valid.
H: In (a), find \(\mathrm{p}(3)\), then divide \(\mathrm{p}(x)\) by \((x - 3)\) to get a quadratic.
H: In (b), use the three linear factors and put \(x = 1\), \(x = -2\) and \(x = 3\).
H: In (c), rewrite each part so the leading term inside the bracket is \(1\), for example \(\dfrac{1}{x - 1} = -(1 - x)^{-1}\).
A: (a) \(\mathrm{p}(3) = 27 - 18 - 15 + 6 = 0\), so \((x - 3)\) is a factor. [B1] \(\mathrm{p}(x) = (x - 3)(x^2 + x - 2)\) [M1] \(= (x - 3)(x - 1)(x + 2)\). [A1] (b)
\[3x^2 - 14x + 5 = A(x + 2)(x - 3) + B(x - 1)(x - 3) + C(x - 1)(x + 2)\]
[M1] Put \(x = 1\): \(-6 = -6A\), so \(A = 1\). [A1] Put \(x = -2\): \(45 = 15B\), so \(B = 3\). [A1] Put \(x = 3\): \(-10 = 10C\), so \(C = -1\). [A1] The result is \(\dfrac{1}{x - 1} + \dfrac{3}{x + 2} - \dfrac{1}{x - 3}\). (c) Rewrite each part with \(1\) as the first term:
\[\begin{aligned} \dfrac{1}{x - 1} &= -(1 - x)^{-1} = -1 - x - x^2 \\ \dfrac{3}{x + 2} &= \tfrac32\left(1 + \tfrac x2\right)^{-1} = \tfrac32 - \tfrac34x + \tfrac38x^2 \\ -\dfrac{1}{x - 3} &= \tfrac13\left(1 - \tfrac x3\right)^{-1} = \tfrac13 + \tfrac19x + \tfrac1{27}x^2 \end{aligned}\]
[M1 A1 A1 A1] Adding gives \(\tfrac56 - \tfrac{59}{36}x - \tfrac{127}{216}x^2\). [A1] The expansions need \(|x| < 1\), \(|x| < 2\) and \(|x| < 3\), so it is valid for \(|x| < 1\). [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ (a) Express \(\dfrac{1}{r(r + 2)}\) in partial fractions. (b) Hence show that \(\dfrac{1}{1 \times 3} + \dfrac{1}{2 \times 4} + \dfrac{1}{3 \times 5} + \dfrac{1}{4 \times 6}\) \(= \dfrac{17}{30}\), by writing each term as a difference and cancelling. (c) By finding the sum of the first \(N\) terms of the same series, find its sum to infinity.
H: In (a), \(1 = A(r + 2) + Br\). Put \(r = 0\) and \(r = -2\).
H: In (b), write every term as \(\tfrac12\left(\dfrac1r - \dfrac{1}{r + 2}\right)\) and see which fractions appear twice with opposite signs.
H: In (c), only four fractions survive the cancelling. Two of them depend on \(N\): what happens to them as \(N\) gets large?
A: (a) \(1 = A(r + 2) + Br\). [M1] Put \(r = 0\): \(A = \tfrac12\). Put \(r = -2\): \(B = -\tfrac12\). So \(\dfrac{1}{r(r + 2)}\) \(= \tfrac12\left(\dfrac1r - \dfrac1{r + 2}\right)\). [A1] (b) The sum is
\[\tfrac12\left[\left(1 - \tfrac13\right) + \left(\tfrac12 - \tfrac14\right) + \left(\tfrac13 - \tfrac15\right) + \left(\tfrac14 - \tfrac16\right)\right]\]
[M1] The \(\tfrac13\) and \(\tfrac14\) cancel. [A1] That leaves \(\tfrac12\left(1 + \tfrac12 - \tfrac15 - \tfrac16\right)\) \(= \tfrac12 \times \tfrac{34}{30}\) \(= \tfrac{17}{30}\). [A1] (c) Every term cancels except the first two positives and the last two negatives: \(S_N\) \(= \tfrac12\left(1 + \tfrac12 - \dfrac{1}{N + 1} - \dfrac{1}{N + 2}\right)\). [M1] As \(N \to \infty\) the last two fractions tend to \(0\), so the sum to infinity is \(\tfrac12 \times \tfrac32 = \tfrac34\). [A1]
Q: [8 marks] ★★★ In the expansion of \((1 + ax)^n\) in ascending powers of \(x\), the coefficient of \(x\) is \(-6\) and the coefficient of \(x^2\) is \(24\). (a) Find the values of \(a\) and \(n\). (b) Find the coefficient of \(x^3\). (c) State the values of \(x\) for which the expansion is valid.
H: The coefficient of \(x\) is \(na\), and the coefficient of \(x^2\) is \(\dfrac{n(n - 1)}{2}a^2\). Write two equations.
H: From the first equation, \(a = -\dfrac{6}{n}\). Substitute it into the second.
A: (a) \(na = -6\) and \(\dfrac{n(n - 1)}{2}a^2 = 24\). [M1 A1] Substitute \(a = -\dfrac6n\): \(\dfrac{n(n - 1)}{2} \times \dfrac{36}{n^2}\) \(= 24\), so \(\dfrac{18(n - 1)}{n} = 24\). [M1] Then \(18n - 18 = 24n\), so \(n = -3\). [A1] Then \(a = 2\). [A1] (b) The coefficient is \(\dfrac{n(n - 1)(n - 2)}{6}a^3\). [M1] With \(n = -3\) and \(a = 2\) it is \(\dfrac{(-3)(-4)(-5)}{6} \times 8\), which is \(-10 \times 8 = -80\). [A1] (c) Valid for \(|2x| < 1\), that is \(|x| < \tfrac12\). [B1]
:::

:::quiz
? Which is the correct form of partial fractions for \(\dfrac{3x + 1}{(x - 1)(x + 2)^2}\)?
- \(\dfrac{A}{x - 1} + \dfrac{B}{(x + 2)^2}\)
+ \(\dfrac{A}{x - 1} + \dfrac{B}{x + 2} + \dfrac{C}{(x + 2)^2}\)
- \(\dfrac{A}{x - 1} + \dfrac{Bx + C}{(x + 2)^2}\)
- \(\dfrac{A}{x - 1} + \dfrac{B}{x + 2}\)
> A repeated linear factor needs a separate term for each power: \(\dfrac{B}{x+2}\) and \(\dfrac{C}{(x+2)^2}\). The linear numerator \(Bx + C\) is used for an irreducible quadratic, not for a squared linear factor.
? What is the coefficient of \(x^2\) in the expansion of \((1 + x)^{-2}\)?
- \(-3\)
- \(2\)
+ \(3\)
- \(-2\)
> \(\dfrac{(-2)(-3)}{2!} = 3\). The series is \(1 - 2x + 3x^2 - 4x^3 + \cdots\) Remember that two negatives multiply to a positive.
? For which values of \(x\) is the expansion of \((2 + x)^{-1}\) valid?
- \(|x| < 1\)
+ \(|x| < 2\)
- \(|x| < \tfrac12\)
- All \(x\)
> \((2 + x)^{-1}\) \(= \tfrac12\left(1 + \tfrac x2\right)^{-1}\), valid when \(\left|\tfrac x2\right| < 1\), that is \(|x| < 2\). The expansion of a negative power is never valid for all \(x\).
? In the expansion of \((4 + x)^{1/2}\), the constant term is
- \(4\)
+ \(2\)
- \(\tfrac12\)
- \(1\)
> Factor out the 4: \(\sqrt{4 + x}\) \(= 4^{1/2}\left(1 + \tfrac x4\right)^{1/2}\) \(= 2\left(\ldots\right)\), so the constant term is \(2\), not \(4\).
? The expansions of \(\dfrac{1}{1 + x}\) and \(\dfrac{1}{1 - 3x}\) are valid for \(|x| < 1\) and \(|x| < \tfrac13\) respectively. For what values of \(x\) is the expansion of their sum valid?
- \(|x| < 1\)
+ \(|x| < \tfrac13\)
- \(|x| < \tfrac43\)
- \(|x| < \tfrac23\)
> Both series must converge, so the narrower range applies: \(|x| < \tfrac13\).
:::

:::checklist What you can now do
- [ ] I can split a proper fraction with two or three different linear factors into partial fractions.
- [ ] I can split a fraction with a repeated linear factor, using one term for each power.
- [ ] I can split a fraction with an irreducible quadratic factor, using a linear numerator \(Bx + C\).
- [ ] I can find the constants by substitution and by comparing coefficients, and check my answer at \(x = 0\).
- [ ] I can expand \((1 + x)^n\) for a fractional or negative \(n\) and say that it is valid for \(|x| < 1\).
- [ ] I can expand \((a + bx)^n\) by factoring out \(a^n\) first, and give its range of validity.
- [ ] I can expand an algebraic fraction by partial fractions and the binomial series, and give the range where all parts are valid.
- [ ] I can use a series with a small \(x\) to approximate a root or a power.
:::

:::recap
- A proper fraction splits as: distinct linear factors \(\dfrac{A}{ax+b} + \dfrac{B}{cx+d}\); repeated factor \(\dfrac{A}{ax+b} + \dfrac{B}{cx+d} + \dfrac{C}{(cx+d)^2}\); quadratic factor \(\dfrac{A}{ax+b} + \dfrac{Bx+C}{cx^2+d}\).
- Find the constants by substituting convenient values of \(x\) and by comparing coefficients; check with \(x = 0\).
- \((1+x)^n\) \(= 1 + nx + \dfrac{n(n-1)}{2!}x^2\) \(+ \dfrac{n(n-1)(n-2)}{3!}x^3 + \cdots\), valid for \(|x| < 1\) when \(n\) is not a positive integer.
- For \((a + bx)^n\), factor out \(a^n\) first: \(a^n\left(1 + \dfrac{bx}{a}\right)^n\), valid for \(\left|\dfrac{bx}{a}\right| < 1\).
- To expand a fraction: partial fractions, expand each part, add; the expansion is valid where all parts are valid.
:::

:::links
- watch: [Partial fractions](https://www.examsolutions.net/tutorials/partial-fractions/) · ExamSolutions · linear and repeated factors
- watch: [Exam questions: binomial expansion](https://www.examsolutions.net/tutorials/exam-questions-binomial-expansion/) · ExamSolutions · rational powers and validity
- practise: [CAIE Pure 3 partial fractions exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/algebra-and-functions/partial-fractions/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Power Series](https://undergroundmathematics.org/power-series) · Underground Mathematics · series expansions explored deeply
- read: [Partial fractions](https://tutorial.math.lamar.edu/Classes/CalcII/PartialFractions.aspx) · Paul's Online Notes · every denominator type, worked

Links checked 3 October 2026.
:::
Next: [Integration techniques](#math.p3.inttech).
