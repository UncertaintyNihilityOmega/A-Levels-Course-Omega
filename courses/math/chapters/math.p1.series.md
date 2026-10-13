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

:::try Warm-up
Q: Expand \((2 + 3x)^2\). (from [Algebra from scratch](#math.f.algebra))
A: \(4 + 12x + 9x^2\).
Q: Evaluate \(2^{-3} \times 16^{1/2}\). (from [Indices, surds and standard form](#math.f.powers))
A: \(\dfrac18 \times 4 = \dfrac12\).
Q: Solve \(n^2 + n - 56 = 0\) for positive \(n\). (from [Quadratics](#math.p1.quadratics))
A: \((n + 8)(n - 7) = 0\), so \(n = 7\) (reject \(-8\)).
:::

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

:::proof Why each number in Pascal's triangle is the sum of the two above it
The claim is \(\dbinom{n}{r} + \dbinom{n}{r + 1} = \dbinom{n + 1}{r + 1}\). Write both terms on the left with factorials:
\[\frac{n!}{r!\,(n - r)!} + \frac{n!}{(r + 1)!\,(n - r - 1)!}\]
Give them a common denominator \((r + 1)!\,(n - r)!\). The first fraction needs a factor \((r + 1)\) on top and the second needs \((n - r)\):
\[\frac{n!\,(r + 1) + n!\,(n - r)}{(r + 1)!\,(n - r)!} = \frac{n!\,(n + 1)}{(r + 1)!\,(n - r)!}\]
Since \(n!\,(n + 1) = (n + 1)!\), and \((n + 1) - (r + 1) = n - r\), this is
\[\frac{(n + 1)!}{(r + 1)!\,\big((n + 1) - (r + 1)\big)!} = \binom{n + 1}{r + 1}\]
So two neighbouring numbers in row \(n\) add up to the number between them in row \(n + 1\).

:::html
<div class="widget" data-w="proof" data-proof="pascal"></div>
:::
:::

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

:::proof Where the sum of an arithmetic series comes from
Write the sum of the first \(n\) terms, then write it again in reverse order, and add the two lines term by term.
\[\begin{aligned} S_n &= a + (a + d) + \dots + (l - d) + l \\ S_n &= l + (l - d) + \dots + (a + d) + a \end{aligned}\]
Every pair in a column adds to the same value, \(a + l\): for example \((a + d) + (l - d) = a + l\). There are \(n\) columns, so
\[2S_n = n(a + l) \qquad\text{and}\qquad S_n = \frac{n}{2}(a + l)\]
The last term is \(l = a + (n - 1)d\), so \(S_n = \dfrac{n}{2}\big(2a + (n - 1)d\big)\).

:::html
<div class="widget" data-w="proof" data-proof="apsum"></div>
:::
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

:::proof Where the sum of a geometric series comes from
Write \(S_n\), multiply it by \(r\), and subtract:
\[\begin{aligned} S_n &= a + ar + ar^2 + \dots + ar^{n-1} \\ rS_n &= \phantom{a + {}} ar + ar^2 + \dots + ar^{n-1} + ar^n \end{aligned}\]
Almost every term appears in both lines and cancels. Only the first term of the top line and the last term of the bottom line are left:
\[S_n - rS_n = a - ar^n\]
Factorise both sides: \(S_n(1 - r) = a(1 - r^n)\). Dividing by \(1 - r\), which is allowed when \(r \neq 1\), gives
\[S_n = \frac{a(1 - r^n)}{1 - r}\]

:::html
<div class="widget" data-w="proof" data-proof="gpsum"></div>
:::
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

:::proof Why the sum to infinity is a/(1 − r)
Start from \(S_n = \dfrac{a(1 - r^n)}{1 - r}\). Suppose \(-1 < r < 1\). Then \(r^n\) is a number between \(-1\) and 1 raised to a bigger and bigger power, so it shrinks towards 0. For \(r = 0.5\): \(0.5, 0.25, 0.125, 0.0625, \dots\).
As \(n\) grows, \(1 - r^n\) gets closer and closer to \(1\), so \(S_n\) gets closer and closer to \(\dfrac{a}{1 - r}\). That limit is \(S_\infty\).
If \(|r| \geq 1\), \(r^n\) does not shrink to 0 (it stays at size 1 or grows), so \(S_n\) has no limit.
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

:::eg Spot the error: find the 15th term and the sum of the first 15 terms of the AP \(7, 10, 13, \ldots\)
A student wrote this answer.

Line 1: \(a = 7\), \(d = 3\)
Line 2: \(u_{15} = a + nd = 7 + 15 \times 3 = 52\)
Line 3: \(S_{15} = \tfrac{15}{2}(a + l) = \tfrac{15}{2}(7 + 52) = 442.5\)

Line 1 is correct [B1]. **Line 2 scores [M0 A0]:** the formula is \(u_n = a + (n - 1)d\), not \(a + nd\), so the method mark is lost as well as the accuracy mark. The student has counted one step too many. Line 3 uses the right sum formula with the student's own last term, so the follow-through method mark is still earned [M1], but the answer is wrong [A0].

Correct working: \(u_{15} = 7 + 14 \times 3 = 49\) [M1 A1], and \(S_{15} = \tfrac{15}{2}(7 + 49) = 420\). [M1 A1]

**Check:** the first term is \(u_1 = 7\). Putting \(n = 1\) into the student's formula gives \(7 + 3 = 10\), which is the second term. A check on \(n = 1\) exposes the slip in seconds.
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

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find the first four terms in the expansion of \((1 + 2x)^5\) in ascending powers of \(x\).
A: \[(1 + 2x)^5 = 1 + \binom51(2x) + \binom52(2x)^2 + \binom53(2x)^3 + \cdots\] [M1] \(= 1 + 10x + 40x^2 + 80x^3 + \cdots\) [A1 A1]
Q: [3 marks] ★ The first three terms of an AP are 5, 9, 13. Find the 30th term and the sum of the first 30 terms.
A: \(a = 5\), \(d = 4\), so \(u_{30} = 5 + 29 \times 4 = 121\). [B1] \(S_{30} = \tfrac{30}{2}(5 + 121)\) [M1] \(= 1890\). [A1]
Q: [4 marks] ★★ A geometric progression has third term 12 and sixth term 96. Find the first term, the common ratio and the sum of the first 8 terms.
A: \(ar^2 = 12\) and \(ar^5 = 96\), so \(r^3 = 8\) [M1] and \(r = 2\). [A1] \(a = \dfrac{12}{4} = 3\). [A1] \(S_8 = \dfrac{3(2^8 - 1)}{2 - 1} = 765\). [A1]
Q: [5 marks] ★★ Find the coefficient of \(x^2\) in the expansion of \((2 + x)(1 - 3x)^4\).
A: \((1 - 3x)^4 = 1 + 4(-3x) + 6(-3x)^2 + \cdots\) [M1] \(= 1 - 12x + 54x^2 - \cdots\) [A1 A1] The \(x^2\) term of the product comes from \(2 \times 54x^2\) and \(x \times (-12x)\). [M1] Coefficient \(= 108 - 12 = 96\). [A1]
Q: [5 marks] ★★ The first term of an AP is 3 and the common difference is 4. Find the least value of \(n\) for which the sum of the first \(n\) terms exceeds 500.
A: \(S_n = \tfrac{n}{2}\big(6 + 4(n - 1)\big) = n(2n + 1)\). [M1 A1] \(S_{15} = 15 \times 31 = 465 < 500\) [M1] and \(S_{16} = 16 \times 33 = 528 > 500\). [A1] So the least value is \(n = 16\). [A1]
Q: [4 marks] ★★ A geometric series has first term 10 and sum to infinity 25. Find the common ratio and the sum of the first three terms.
A: \(\dfrac{10}{1 - r} = 25\), so \(1 - r = 0.4\). [M1] \(r = 0.6\). [A1] \(S_3 = \dfrac{10(1 - 0.6^3)}{1 - 0.6}\) [M1] \(= 19.6\). [A1]
Q: [10 marks] (#math.p1.quadratics) ★★★ The 1st, 2nd and 5th terms of an arithmetic progression are the first three terms of a geometric progression. The AP has first term 3 and common difference \(d\), where \(d \neq 0\). (a) Show that \(d = 6\). (b) Find the sum of the first 10 terms of the AP. (c) Find the sum of the first 10 terms of the GP. (d) Find the least number of terms of the GP for which the sum exceeds one million.
H: The terms of the AP are \(3, 3 + d, 3 + 2d, \ldots\) The 5th term is \(3 + 4d\). For a GP, the middle term squared equals the product of the other two.
H: You get a quadratic in \(d\) with a factor \(d\). The condition \(d \neq 0\) removes one root.
H: The GP is \(3, 9, 27, \ldots\) For (d), try values of \(n\) in \(S_n\) rather than using logarithms.
A: (a) \((3 + d)^2 = 3(3 + 4d)\). [M1] \(9 + 6d + d^2 = 9 + 12d\), so \(d^2 - 6d = 0\). [A1] \(d(d - 6) = 0\), and \(d \neq 0\), so \(d = 6\). [A1] (b) \(S_{10} = \tfrac{10}{2}(2 \times 3 + 9 \times 6) = 300\). [M1 A1] (c) The GP is \(3, 9, 27, \ldots\) with \(r = 3\), so \(S_{10} = \dfrac{3(3^{10} - 1)}{3 - 1} = 88\,572\). [M1 A1] (d) \(S_n = \dfrac{3(3^n - 1)}{2}\). \(S_{12} = 797\,160 < 10^6\). [M1 A1] \(S_{13} = 2\,391\,483 > 10^6\), so the least number of terms is 13. [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A geometric series has first term \(a\) and common ratio \(r\), where \(|r| < 1\). The sum to infinity is six times the second term. Find the two possible values of \(r\), in exact form.
H: The second term is \(ar\). Write the condition as an equation containing \(a\) and \(r\), then divide by \(a\).
H: You get a quadratic in \(r\). Both roots must satisfy \(|r| < 1\); check.
A: \(\dfrac{a}{1 - r} = 6ar\). [M1] Dividing by \(a\) (\(a \neq 0\)): \(1 = 6r(1 - r)\), so \(6r^2 - 6r + 1 = 0\). [A1] \(r = \dfrac{6 \pm \sqrt{36 - 24}}{12} = \dfrac{6 \pm 2\sqrt3}{12} = \dfrac{3 \pm \sqrt3}{6}\). [M1 A1] The values are 0.789 and 0.211, both between \(-1\) and 1, so both are valid. [A1]
Q: [4 marks] ★★★ In the expansion of \((1 + ax)^6\), where \(a \neq 0\), the coefficient of \(x^3\) is 4 times the coefficient of \(x^2\). Find \(a\), and the coefficient of \(x^4\).
H: The coefficient of \(x^2\) is \(\binom62 a^2\). Write the coefficient of \(x^3\) similarly and form the equation.
H: Divide both sides by \(20a^2\); you may, because \(a \neq 0\).
A: \(\dbinom63 a^3 = 4\dbinom62 a^2\), so \(20a^3 = 60a^2\). [M1] Dividing by \(20a^2\) (\(a \neq 0\)): \(a = 3\). [A1] The coefficient of \(x^4\) is \(\dbinom64 \times 3^4 = 15 \times 81\) [M1] \(= 1215\). [A1]
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

:::checklist What you can now do
- [ ] I can use factorials and \(\binom{n}{r}\), and read coefficients from Pascal's triangle.
- [ ] I can expand \((a + b)^n\) for positive integer \(n\), and find a particular term or coefficient.
- [ ] I can find the \(n\)th term and the sum of the first \(n\) terms of an arithmetic progression.
- [ ] I can find the \(n\)th term and the sum of the first \(n\) terms of a geometric progression.
- [ ] I can say when a geometric series converges and find its sum to infinity.
- [ ] I can use "in AP" (\(2b = a + c\)) and "in GP" (\(b^2 = ac\)).
- [ ] I can solve problems that involve more than one progression, or a progression in a real context.
:::

:::recap
- \(n! = n(n-1)\cdots 1\), \(\dbinom nr = \dfrac{n!}{r!(n-r)!}\). Use Pascal's triangle or the nCr key.
- \((a + b)^n = \sum \dbinom nr a^{n-r}b^r\): \(n + 1\) terms, powers of \(a\) falling and powers of \(b\) rising. Put the second term in brackets, signs included.
- AP: \(u_n = a + (n-1)d\), \(S_n = \tfrac n2(2a + (n-1)d)\); in AP means \(2b = a + c\).
- GP: \(u_n = ar^{n-1}\), \(S_n = \dfrac{a(1 - r^n)}{1 - r}\); in GP means \(b^2 = ac\). Sum to infinity \(\dfrac{a}{1 - r}\) only if \(|r| < 1\).
- For two progressions, write each condition as an equation in \(a\), \(d\) or \(r\) and solve simultaneously.
:::

:::links
- watch: [Binomial expansion for positive integer powers](https://www.examsolutions.net/tutorials/binomial-expansion-for-positive-integer-powers/) · ExamSolutions · Pascal's triangle and ⁿCᵣ
- watch: [Exam questions: geometric series](https://www.examsolutions.net/tutorials/geometric-series-exam-questions/) · ExamSolutions · sums and sums to infinity in exam style
- practise: [CAIE Pure 1 binomial expansion exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/series/binomial-expansion/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [CAIE Pure 1 geometric progressions exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/series/geometric-progressions/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Sequences](https://undergroundmathematics.org/sequences) · Underground Mathematics · problems on APs, GPs and beyond
- explore: [Counting & Binomials](https://undergroundmathematics.org/counting-and-binomials) · Underground Mathematics · why binomial coefficients count things

Links checked 3 October 2026.
:::
Next: [Differentiation](#math.p1.diff) measures how fast a quantity changes.
