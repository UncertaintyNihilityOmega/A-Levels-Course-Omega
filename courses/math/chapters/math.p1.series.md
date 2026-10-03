@chapter math.p1.series
@title Series: binomial expansion and progressions
@level as
@paper CAIE P1 · Edexcel IAL P2 · AQA/OCR/Edexcel Pure Year 1
@time 7–9 hours
@summary Binomial expansions of \((a + b)^n\) for positive integers \(n\), with \(n!\) and \(\binom{n}{r}\); arithmetic progressions; geometric progressions, including convergence and the sum to infinity; and problems that combine progressions.

:::why
Series let you add up long lists of numbers with a formula instead of a calculator, and the binomial theorem expands powers like \((2 + 3x)^{10}\) without multiplying out ten brackets. They model savings plans, loan repayments, bouncing balls and depreciation, and they are the foundation of the binomial distribution in Statistics. The formulas are on MF19, so the skill is choosing the right one and setting up the equations.
:::

**Before you start**, you need expanding brackets and indices ([Algebra from scratch](#math.f.algebra), [Indices, surds and standard form](#math.f.powers)), and simultaneous and quadratic equations ([Quadratics](#math.p1.quadratics)). A recurring decimal in [Numbers, fractions and percentages](#math.f.numbers) is a geometric series in disguise.

## Factorials and binomial coefficients

:::def Factorial
For a positive integer \(n\), \(n!\) ("\(n\) factorial") is the product of the integers from \(n\) down to \(1\): \(n! = n \times (n-1) \times \cdots \times 2 \times 1\). By definition \(0! = 1\).
:::

So \(5! = 120\), and \(\dfrac{7!}{5!} = 7 \times 6 = 42\): cancel before you multiply.

:::def Binomial coefficient
\(\dbinom{n}{r}\) (read "\(n\) choose \(r\)", also written \({}^{n}C_{r}\)) is the number of ways to choose \(r\) items from \(n\):
\[\binom{n}{r} = \frac{n!}{r!\,(n - r)!}\]
:::

On a calculator use the \(\mathrm{nCr}\) key. By hand, cancel: \(\dbinom{7}{3} = \dfrac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35\). Two facts save time: \(\dbinom{n}{0} = \dbinom{n}{n} = 1\), and \(\dbinom{n}{r} = \dbinom{n}{n - r}\) (choosing which to take is the same as choosing which to leave). Also \(\dbinom{n}{1} = n\).

**Pascal's triangle** lists the coefficients. Each number is the sum of the two above it, and row \(n\) gives \(\dbinom{n}{0}, \dbinom{n}{1}, \ldots, \dbinom{n}{n}\).

| Row \(n\) | Coefficients |
|---|---|
| 0 | 1 |
| 1 | 1 1 |
| 2 | 1 2 1 |
| 3 | 1 3 3 1 |
| 4 | 1 4 6 4 1 |
| 5 | 1 5 10 10 5 1 |
| 6 | 1 6 15 20 15 6 1 |

## The binomial theorem

Multiply out \((a + b)^3\) and you get \(a^3 + 3a^2b + 3ab^2 + b^3\), with coefficients \(1, 3, 3, 1\), which is row 3 of Pascal's triangle. This pattern holds for every positive integer \(n\).

:::key Binomial theorem
For a positive integer \(n\):
\[(a + b)^n = a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{r}a^{n-r}b^r + \cdots + b^n\]
The general term (the term in \(b^r\)) is \(\dbinom{n}{r}a^{n-r}b^r\). The powers of \(a\) fall from \(n\) to \(0\), the powers of \(b\) rise from \(0\) to \(n\), and the powers in each term add up to \(n\). The expansion has \(n + 1\) terms. It is on MF19.
:::

When you expand \((1 + x)^n\) the expression is \(1 + nx + \dfrac{n(n-1)}{2!}x^2 + \cdots\): this "ascending powers of \(x\)" form is used when the question asks for the first few terms.

:::eg Expand \((2 + 3x)^4\).
Here \(a = 2\), \(b = 3x\), \(n = 4\), and the coefficients are \(1, 4, 6, 4, 1\):
\[\begin{aligned} (2 + 3x)^4 &= 2^4 + 4(2^3)(3x) + 6(2^2)(3x)^2 + 4(2)(3x)^3 + (3x)^4 \\ &= 16 + 96x + 216x^2 + 216x^3 + 81x^4 \end{aligned}\]
Check with \(x = 1\): \((5)^4 = 625\) and \(16 + 96 + 216 + 216 + 81 = 625\). ✓
:::

:::warn Brackets and signs in each term
Put each part of the second term in brackets, including its sign and its number: \((3x)^2 = 9x^2\), not \(3x^2\). With a minus, \((-2x)^3 = -8x^3\), so the sign alternates in \((1 - 2x)^n\). The coefficient of a term includes the number you get from \(a^{n-r}b^r\), not just \(\dbinom{n}{r}\).
:::

:::eg Find the coefficient of \(x^3\) in the expansion of \((3 - 2x)^5\), and the first three terms of \((2 + x)^6\) in ascending powers of \(x\).
The term in \(x^3\) uses \(r = 3\): \(\dbinom{5}{3}(3)^2(-2x)^3 = 10 \times 9 \times (-8x^3) = -720x^3\). The coefficient is \(-720\).

For \((2 + x)^6\): \(2^6 + \dbinom61 2^5 x + \dbinom62 2^4 x^2 + \cdots = 64 + 192x + 240x^2 + \cdots\)
:::

A term "independent of \(x\)" (a **constant term**) is the one where the powers of \(x\) cancel. Find the general term, collect the power of \(x\), and set it to zero.

:::eg Find the term independent of \(x\) in the expansion of \(\left(2x - \dfrac1x\right)^6\).
The general term is \(\dbinom6r (2x)^{6-r}\left(-\dfrac1x\right)^r = \dbinom6r 2^{6-r}(-1)^r x^{6-r}x^{-r} = \dbinom6r 2^{6-r}(-1)^r x^{6-2r}\). For a constant term \(6 - 2r = 0\), so \(r = 3\):
\[\binom63 \times 2^3 \times (-1)^3 = 20 \times 8 \times (-1) = -160\]
:::

When the expansion is multiplied by another bracket, find which products give the power you need.

:::eg Find the coefficient of \(x^4\) in the expansion of \((1 + 2x)(1 - x)^6\).
The expansion of \((1 - x)^6\) has coefficients \(1, -6, 15, -20, 15, -6, 1\) (alternating signs, from row 6). The \(x^4\) term of the product comes from \(1 \times (15x^4)\) and \(2x \times (-20x^3)\):
\[15 + 2(-20) = -25\]
The coefficient of \(x^4\) is \(-25\).
:::

:::eg (Exam style) The coefficient of \(x^2\) in the expansion of \((1 + kx)^7\), where \(k > 0\), is \(84\). (a) Find the value of \(k\). (b) Find the coefficient of \(x^3\).
**(a)** The term in \(x^2\) is \(\dbinom72(kx)^2 = 21k^2x^2\). [M1 A1]
\[21k^2 = 84 \implies k^2 = 4\] [M1]
Since \(k > 0\), \(k = 2\). [A1]

**(b)** The term in \(x^3\) is \(\dbinom73(2x)^3 = 35 \times 8x^3 = 280x^3\). [M1] The coefficient is \(280\). [A1]
:::

## Arithmetic progressions

A **sequence** is a list of numbers in order, \(u_1, u_2, u_3, \ldots\). A **series** is the sum of the terms of a sequence.

:::def Arithmetic progression (AP)
A sequence in which each term is found by adding the same constant, the **common difference** \(d\), to the previous term. If the first term is \(a\), the terms are \(a, a + d, a + 2d, \ldots\)
:::

The \(n\)th term is \(u_n = a + (n-1)d\). To find the sum of the first \(n\) terms, write the sum forwards and backwards and add: every pair of terms adds to the same value (first + last), and there are \(n\) pairs, giving \(2S_n = n(a + l)\) where \(l\) is the last term.

:::formula Arithmetic progression
\[u_n = a + (n-1)d \qquad S_n = \frac{n}{2}\big(2a + (n-1)d\big) = \frac{n}{2}(a + l)\]
\(a\) is the first term, \(d\) the common difference, \(n\) the number of terms and \(l\) the last term. Both are on MF19. Three numbers \(a, b, c\) are in AP if and only if \(b - a = c - b\), that is \(2b = a + c\).
:::

:::eg Find the 20th term and the sum of the first 20 terms of the AP \(7, 11, 15, \ldots\)
Here \(a = 7\) and \(d = 4\).
\[u_{20} = 7 + 19 \times 4 = 83\]
\[S_{20} = \frac{20}{2}(2 \times 7 + 19 \times 4) = 10 \times 90 = 900\]
Check with the last-term form: \(\dfrac{20}{2}(7 + 83) = 900\). ✓
:::

:::eg Find the sum of all the multiples of \(3\) between \(100\) and \(400\).
The first multiple is \(102\) and the last is \(399\). They form an AP with \(d = 3\). The number of terms is \(\dfrac{399 - 102}{3} + 1 = 100\). Then
\[S_{100} = \frac{100}{2}(102 + 399) = 50 \times 501 = 25\,050\]
:::

:::eg The 5th term of an AP is \(17\) and the 9th term is \(29\). Find \(a\) and \(d\), the sum of the first 10 terms, and the smallest \(n\) for which \(S_n > 200\).
\(a + 4d = 17\) and \(a + 8d = 29\). Subtract: \(4d = 12\), so \(d = 3\) and \(a = 5\).

\(S_{10} = \dfrac{10}{2}(10 + 27) = 185\).

\(S_n = \dfrac n2(10 + 3(n-1)) = \dfrac{n(3n + 7)}{2}\). Then \(S_{10} = 185 < 200\) and \(S_{11} = \dfrac{11 \times 40}{2} = 220 > 200\), and the sum increases with \(n\). So the smallest \(n\) is \(11\).
:::

## Geometric progressions

:::def Geometric progression (GP)
A sequence in which each term is found by multiplying the previous term by the same constant, the **common ratio** \(r\). If the first term is \(a\), the terms are \(a, ar, ar^2, \ldots\)
:::

The \(n\)th term is \(u_n = ar^{n-1}\). For the sum, subtract \(rS_n\) from \(S_n\): nearly everything cancels, leaving \(S_n(1 - r) = a(1 - r^n)\).

:::formula Geometric progression
\[u_n = ar^{n-1} \qquad S_n = \frac{a(1 - r^n)}{1 - r} = \frac{a(r^n - 1)}{r - 1} \quad (r \ne 1)\]
Use the first form when \(|r| < 1\) and the second when \(r > 1\), which avoids negatives. Three numbers \(a, b, c\) are in GP if \(\dfrac ba = \dfrac cb\), that is \(b^2 = ac\). All are on MF19.
:::

:::eg Find the 8th term and the sum of the first 8 terms of the GP \(6, 12, 24, \ldots\)
\(a = 6\) and \(r = 2\). \(u_8 = 6 \times 2^7 = 768\).
\[S_8 = \frac{6(2^8 - 1)}{2 - 1} = 6 \times 255 = 1530\]
:::

:::eg A GP has third term \(18\) and sixth term \(486\). Find the first term, the common ratio and \(S_6\).
\(ar^2 = 18\) and \(ar^5 = 486\). Divide: \(r^3 = \dfrac{486}{18} = 27\), so \(r = 3\). Then \(a = \dfrac{18}{9} = 2\). \(S_6 = \dfrac{2(3^6 - 1)}{3 - 1} = 728\).
:::

### Sum to infinity

If \(|r| < 1\), the terms \(ar^n\) get smaller and smaller, and the sum of the first \(n\) terms gets closer to a limit. We say the series **converges**. Since \(r^n \to 0\), the formula for \(S_n\) becomes:

:::key Sum to infinity
A geometric series converges if and only if \(-1 < r < 1\), and then
\[S_\infty = \frac{a}{1 - r}\]
If \(|r| \ge 1\), the series does not converge and \(S_\infty\) does not exist. The formula is on MF19, but you must state or check \(|r| < 1\).
:::

:::eg Find the sum to infinity of \(40, -20, 10, -5, \ldots\) For which values of \(x\) does the series \(3 + 3\left(\dfrac x4\right) + 3\left(\dfrac x4\right)^2 + \cdots\) converge?
Here \(a = 40\) and \(r = -\tfrac12\). Since \(|r| < 1\), \(S_\infty = \dfrac{40}{1 + \frac12} = \dfrac{80}{3}\).

The second series has \(r = \dfrac x4\). It converges when \(\left|\dfrac x4\right| < 1\), that is \(-4 < x < 4\).
:::

:::eg Write \(0.\dot{2}\dot{7}\) as a fraction using a geometric series, and find the total distance travelled by a ball dropped from \(5\) m that bounces back to \(0.6\) of its previous height each time.
\(0.272727\ldots = 0.27 + 0.0027 + 0.000027 + \cdots\), a GP with \(a = 0.27\) and \(r = 0.01\):
\[S_\infty = \frac{0.27}{1 - 0.01} = \frac{27}{99} = \frac{3}{11}\]
The ball falls \(5\) m, then each bounce is up and down: heights \(3, 1.8, 1.08, \ldots\) (GP with \(a = 3\), \(r = 0.6\)), each counted twice.
\[\text{distance} = 5 + 2 \times \frac{3}{1 - 0.6} = 5 + 2 \times 7.5 = 20 \text{ m}\]
:::

## Progressions in real contexts

Look for the wording. A **fixed amount** added each period is an AP; a **fixed percentage** change each period is a GP, with ratio \(1 + \frac{p}{100}\) for an increase and \(1 - \frac{p}{100}\) for a decrease (see [Numbers, fractions and percentages](#math.f.numbers)). When the question asks "in which year does it first exceed", write the formula for the \(n\)th term, then test values of \(n\) either side of the boundary.

:::eg A job pays $24 000 in the first year and the salary rises by $1500 each year. A car costs $18 000 and loses 15% of its value each year. (a) In which year does the salary first exceed $40 000, and what is the total earned in the first 12 years? (b) After how many whole years is the car first worth less than $6000?
(a) The salaries form an AP with \(a = 24\,000\) and \(d = 1500\), so \(u_n = 24\,000 + 1500(n - 1)\). Test: \(u_{11} = 24\,000 + 15\,000 = 39\,000 < 40\,000\) and \(u_{12} = 24\,000 + 16\,500 = 40\,500 > 40\,000\). The salary first exceeds $40 000 in year 12. The total over 12 years is
\[S_{12} = \frac{12}{2}\big(2 \times 24\,000 + 11 \times 1500\big) = 6 \times 64\,500 = 387\,000\]
So the total is $387 000.

(b) The value after \(n\) years is a GP: \(18\,000 \times 0.85^n\) (the multiplier is \(1 - 0.15 = 0.85\)). Test values: after 6 years \(18\,000 \times 0.85^6 = 6788.69 > 6000\), and after 7 years \(18\,000 \times 0.85^7 = 5770.39 < 6000\). Since the values keep falling, the car is first worth less than $6000 after 7 years.
:::

## More than one progression

Exam questions often make an AP and a GP from the same numbers. Use the AP formulas with \(a\) and \(d\), the GP condition \(b^2 = ac\), and solve the simultaneous equations. Write down each condition separately before you combine them.

:::eg (Exam style) The first term of an AP is \(4\) and the common difference is \(d\), where \(d \ne 0\). The 1st, 2nd and 4th terms of this AP are the first three terms of a GP. (a) Find \(d\). (b) Find the common ratio of the GP and the sum of the first 10 terms of the AP.
**(a)** The terms are \(4\), \(4 + d\), \(4 + 3d\). [B1] For a GP, \(b^2 = ac\):
\[(4 + d)^2 = 4(4 + 3d)\] [M1]
\[16 + 8d + d^2 = 16 + 12d \implies d^2 - 4d = 0 \implies d(d - 4) = 0\] [A1]
Since \(d \ne 0\), \(d = 4\). [A1]

**(b)** The terms are \(4, 8, 16\), so the common ratio is \(2\). [B1] For the AP, \(S_{10} = \dfrac{10}{2}(2 \times 4 + 9 \times 4) = 5 \times 44 = 220\). [M1 A1]
:::

:::eg (Exam style) A geometric series has second term \(12\) and sum to infinity \(64\). Find the two possible values of the common ratio, and the first term in each case.
\(ar = 12\) and \(\dfrac{a}{1 - r} = 64\). From the second, \(a = 64(1 - r)\). [M1]
Substitute: \(64r(1 - r) = 12\), so \(16r^2 - 16r + 3 = 0\). [M1 A1]
\[(4r - 1)(4r - 3) = 0 \implies r = \tfrac14 \text{ or } r = \tfrac34\] [A1]
Both satisfy \(|r| < 1\). If \(r = \tfrac14\), \(a = 48\); if \(r = \tfrac34\), \(a = 16\). [A1]
Check: \(48 \times \tfrac14 = 12\) and \(16 \times \tfrac34 = 12\). ✓
:::

:::exam Choosing AP or GP
- "Common difference", "increases by the same amount", "each month $20 more": **AP**. "Common ratio", "increases by 5% each year", "halves each time": **GP**.
- Write what the unknowns are (\(a\), \(d\) or \(r\)) and form one equation for each condition, as in the 5th and 9th term example above.
- For "smallest \(n\)" in an AP, work with the formula and an inequality (or test values); the use of logarithms for GPs is in [Logarithms](#math.p3.logs).
- Keep the exact form until the last step. State "since \(|r| < 1\)" before using \(S_\infty\).
:::

:::board Other boards
Edexcel IAL, AQA, OCR and Edexcel (UK) all include the binomial theorem for positive integers, APs, GPs and the sum to infinity in their first Pure year. Several UK boards also expect sigma notation \(\sum_{r=1}^{n}\) and sequences defined by a recurrence relation \(u_{n+1} = f(u_n)\). Cambridge 9709 uses the formulae in the form above, and the binomial series for fractional or negative \(n\) is in [Partial fractions and the binomial series](#math.p3.partial).
:::

:::try Start easy, finish at exam standard
Q: Evaluate (a) \(\dbinom83\), (b) \(\dfrac{7!}{5!\,2!}\), (c) \(\dbinom{10}{10}\).
A: (a) \(\dfrac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56\). (b) \(\dfrac{7 \times 6}{2} = 21\). (c) \(1\).
Q: Expand \((1 + 2x)^5\) up to and including the term in \(x^3\).
A: \(1 + 5(2x) + 10(2x)^2 + 10(2x)^3 = 1 + 10x + 40x^2 + 80x^3\).
Q: Find the coefficient of \(x^4\) in the expansion of \((2 - x)^6\).
A: \(\dbinom64 (2)^2 (-x)^4 = 15 \times 4 \times x^4 = 60x^4\). The coefficient is \(60\).
Q: Find the term independent of \(x\) in the expansion of \(\left(x + \dfrac2x\right)^6\).
A: The general term is \(\dbinom6r x^{6-r}\left(\dfrac2x\right)^r = \dbinom6r 2^r x^{6-2r}\). For \(r = 3\): \(20 \times 8 = 160\).
Q: Find the coefficient of \(x^2\) in the expansion of \((3 + x)(1 - 2x)^5\).
A: \((1 - 2x)^5 = 1 - 10x + 40x^2 - \cdots\). The \(x^2\) term comes from \(3 \times 40x^2\) and \(x \times (-10x)\): \(120 - 10 = 110\).
Q: The 3rd term of an AP is \(11\) and the 8th term is \(31\). Find \(a\), \(d\) and \(S_{12}\).
A: \(a + 2d = 11\), \(a + 7d = 31\), so \(5d = 20\), \(d = 4\), \(a = 3\). \(S_{12} = 6(6 + 44) = 300\).
Q: Find the sum of all the multiples of \(7\) that are less than \(100\).
A: \(7, 14, \ldots, 98\): \(n = 14\). \(S = \dfrac{14}{2}(7 + 98) = 735\).
Q: Find the 10th term and the sum of the first 10 terms of the GP \(3, 6, 12, \ldots\)
A: \(u_{10} = 3 \times 2^9 = 1536\). \(S_{10} = 3(2^{10} - 1) = 3069\).
Q: A geometric series has first term \(20\) and sum to infinity \(25\). Find the common ratio and the second term.
A: \(\dfrac{20}{1 - r} = 25\), so \(1 - r = 0.8\) and \(r = 0.2\). The second term is \(20 \times 0.2 = 4\).
Q: (Exam style) In the expansion of \((2 + ax)^6\), the coefficient of \(x\) equals the coefficient of \(x^2\), and \(a \ne 0\). Find \(a\) and the coefficient of \(x^3\).
A: Coefficient of \(x\): \(\dbinom61 2^5 a = 192a\). Coefficient of \(x^2\): \(\dbinom62 2^4 a^2 = 240a^2\). [M1 A1] Equal: \(192a = 240a^2\), so \(a = \dfrac{192}{240} = 0.8\). [M1 A1] The \(x^3\) coefficient is \(\dbinom63 2^3 a^3 = 160 \times 0.512 = 81.92\). This is exact, so give it in full. [M1 A1]
Q: (Exam style) The first term of an AP is \(2\) and the common difference is \(d\ (d \neq 0)\). The 2nd, 5th and 14th terms of the AP are in GP. Find \(d\), the common ratio of the GP and the sum of the first 20 terms of the AP.
A: The terms are \(2 + d\), \(2 + 4d\), \(2 + 13d\). [B1] \((2 + 4d)^2 = (2 + d)(2 + 13d)\) gives \(4 + 16d + 16d^2 = 4 + 28d + 13d^2\). [M1 A1] So \(3d^2 = 12d\) and \(d = 4\). [A1] The terms are \(6, 18, 54\), so \(r = 3\). [A1] \(S_{20} = 10(4 + 19 \times 4) = 800\). [A1]
:::

:::quiz
? What is the coefficient of \(x^2\) in the expansion of \((1 - 2x)^4\)?
+ \(24\)
- \(-24\)
- \(6\)
- \(12\)
> The term is \(\dbinom42(-2x)^2 = 6 \times 4x^2 = 24x^2\). The square makes the sign positive. Forgetting to square the \(2\) gives \(6\), using the \(2\) only once gives \(12\), and \(-24\) is a sign slip.
? In the AP \(5, 9, 13, \ldots\), which term equals \(101\)?
- \(24\)
+ \(25\)
- \(26\)
- \(20\)
> \(5 + (n-1)4 = 101\) gives \(n - 1 = 24\) and \(n = 25\). The value \(24\) is the answer to \(n - 1\), a very common off-by-one slip.
? Which of these geometric series has a sum to infinity?
- \(3 + 6 + 12 + \cdots\)
+ \(8 - 4 + 2 - \cdots\)
- \(2 + 2 + 2 + \cdots\)
- \(1 - 1.5 + 2.25 - \cdots\)
> The series \(8 - 4 + 2 - \cdots\) has \(r = -\tfrac12\), and \(|r| < 1\). The others have \(r = 2\), \(r = 1\) and \(r = -1.5\), so their terms do not get smaller. A negative ratio is not enough to prevent convergence: what matters is \(|r| < 1\).
? The numbers \(3\), \(k\), \(12\) are consecutive terms of an AP. What is \(k\)?
- \(6\)
+ \(7.5\)
- \(9\)
- \(36\)
> In an AP, \(2k = 3 + 12\), so \(k = 7.5\). The value \(6\) is what you get if the numbers are in GP (\(k^2 = 36\)). Always check which type of progression the question names.
? The numbers \(2\), \(k\) and \(18\) are consecutive terms of a geometric progression, with \(k > 0\). What is \(k\)?
- \(10\)
- \(16\)
+ \(6\)
- \(36\)
> In a GP, \(k^2 = 2 \times 18 = 36\), so \(k = 6\) (the common ratio is \(3\)). The value \(10\) is the middle of an AP, found by averaging. The value \(36\) is \(k^2\) before taking the square root, and \(16\) is \(18 - 2\).
:::

:::recap
- \(n! = n(n-1)\cdots 1\), \(\dbinom nr = \dfrac{n!}{r!(n-r)!}\). Use Pascal's triangle or the nCr key.
- \((a + b)^n = \sum \dbinom nr a^{n-r}b^r\): \(n + 1\) terms, powers of \(a\) falling and powers of \(b\) rising. Put the second term in brackets, signs included.
- AP: \(u_n = a + (n-1)d\), \(S_n = \tfrac n2(2a + (n-1)d)\); in AP means \(2b = a + c\).
- GP: \(u_n = ar^{n-1}\), \(S_n = \dfrac{a(1 - r^n)}{1 - r}\); in GP means \(b^2 = ac\). Sum to infinity \(\dfrac{a}{1 - r}\) only if \(|r| < 1\).
- For two progressions, write each condition as an equation in \(a\), \(d\) or \(r\) and solve simultaneously.
:::

:::note Learn more online
- **Watch:** [Binomial expansion for positive integer powers](https://www.examsolutions.net/tutorials/binomial-expansion-for-positive-integer-powers/) · ExamSolutions · Pascal's triangle and ⁿCᵣ
- **Watch:** [Exam questions: geometric series](https://www.examsolutions.net/tutorials/geometric-series-exam-questions/) · ExamSolutions · sums and sums to infinity in exam style
- **Practise:** [CAIE Pure 1 binomial expansion exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/series/binomial-expansion/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Practise:** [CAIE Pure 1 geometric progressions exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/series/geometric-progressions/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Sequences](https://undergroundmathematics.org/sequences) · Underground Mathematics · problems on APs, GPs and beyond
- **Explore:** [Counting & Binomials](https://undergroundmathematics.org/counting-and-binomials) · Underground Mathematics · why binomial coefficients count things

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Differentiation](#math.p1.diff) measures how fast a quantity changes.
