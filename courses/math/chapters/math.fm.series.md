@chapter math.fm.series
@title Summation of series
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 5–7 hours
@summary You will add up long series exactly. The standard results for \(\sum r\), \(\sum r^2\) and \(\sum r^3\) give sums of polynomial terms in closed form, the method of differences makes the middle of a sum cancel, and letting \(n\) grow shows when a series settles down to a finite sum to infinity.

:::why
Adding 1 000 000 terms one by one is hopeless, but a formula for the sum of the first \(n\) terms answers every such question at once. This chapter gives you two ways to find that formula: known results for sums of powers, and a trick that makes the terms cancel in pairs. The same ideas return in proof by induction, in integration by rectangles and in the series of Further Pure 2.
:::

**Before you start**, you need sigma notation and arithmetic and geometric sums from [Series: binomial expansion and progressions](#math.p1.series), partial fractions from [Partial fractions and the binomial series](#math.p3.partial), and factorising cubics from [Modulus and polynomials](#math.p3.algebra).

:::try Warm-up
Q: Find the sum of the first 20 terms of the arithmetic series \(3 + 7 + 11 + \dots\). (from [Series: binomial expansion and progressions](#math.p1.series))
A: \(a = 3\), \(d = 4\): \(S_{20} = \tfrac{20}{2}\left(2 \times 3 + 19 \times 4\right) = 10 \times 82 = 820\).
Q: Express \(\dfrac{1}{r(r+1)}\) in partial fractions. (from [Partial fractions and the binomial series](#math.p3.partial))
A: Write \(\dfrac{1}{r(r+1)} = \dfrac{A}{r} + \dfrac{B}{r+1}\), so \(1 = A(r+1) + Br\). Put \(r = 0\): \(A = 1\). Put \(r = -1\): \(B = -1\). So \(\dfrac{1}{r} - \dfrac{1}{r+1}\).
Q: Factorise \(2n^3 + 3n^2 + n\) completely. (from [Modulus and polynomials](#math.p3.algebra))
A: Take out \(n\): \(n(2n^2 + 3n + 1) = n(2n + 1)(n + 1)\).
:::

## Sigma notation

A series is a sum of terms, and \(\sum\) (capital sigma, the Greek S for "sum") is shorthand for it. The letter \(r\) under the sigma is a counter that runs through whole numbers; the **general term** \(u_r\) says what to add each time.

:::def Sigma notation
\(\displaystyle\sum_{r=m}^{n} u_r\) means \(u_m + u_{m+1} + \dots + u_n\): add the general term \(u_r\) for \(r = m, m+1, \dots, n\). The sum has \(n - m + 1\) terms.
:::

:::eg Write out and evaluate (a) \(\displaystyle\sum_{r=1}^{4} (2r + 1)\), (b) \(\displaystyle\sum_{r=3}^{6} r^2\), (c) \(\displaystyle\sum_{r=1}^{5} 3\).
(a) Put \(r = 1, 2, 3, 4\): \(3 + 5 + 7 + 9 = 24\).

(b) Put \(r = 3, 4, 5, 6\): \(9 + 16 + 25 + 36 = 86\). There are \(6 - 3 + 1 = 4\) terms.

(c) The general term does not contain \(r\), so every term is 3, and there are five of them: \(3 + 3 + 3 + 3 + 3 = 15 = 5 \times 3\).
:::

Part (c) shows the first rule below. Sums behave well with addition and with constant multiples, because you can regroup terms in any order.

:::key Rules for sigma
\[\begin{aligned}
\sum_{r=1}^{n} \left(a u_r + b v_r\right) &= a\sum_{r=1}^{n} u_r + b\sum_{r=1}^{n} v_r \\
\sum_{r=1}^{n} c &= nc \\
\sum_{r=m}^{n} u_r &= \sum_{r=1}^{n} u_r - \sum_{r=1}^{m-1} u_r
\end{aligned}\]
Here \(a\), \(b\) and \(c\) are constants. In particular \(\sum_{r=1}^{n} 1 = n\). The last rule starts a sum at \(r = m\): take the sum to \(n\), then remove the terms before \(r = m\).
:::

The rules do not cover products. In general \(\sum r^2\) is not \(\left(\sum r\right)^2\), and \(\sum (u_r v_r)\) is not \(\sum u_r \times \sum v_r\). Test with \(n = 2\): \(1^2 + 2^2 = 5\), but \((1 + 2)^2 = 9\).

## The standard results for \(\sum r\), \(\sum r^2\) and \(\sum r^3\)

You already know \(\sum r\): it is an arithmetic series with first term 1 and last term \(n\), so its sum is \(\tfrac{n}{2}(1 + n)\). The sums of the squares and the cubes have formulas too.

:::key Standard results
\[\begin{aligned}
\sum_{r=1}^{n} r &= \tfrac12 n(n+1) \\
\sum_{r=1}^{n} r^2 &= \tfrac16 n(n+1)(2n+1) \\
\sum_{r=1}^{n} r^3 &= \tfrac14 n^2(n+1)^2
\end{aligned}\]
These are on MF19, but you must quote the one you use. They add from \(r = 1\) up to \(n\). Notice that \(\sum r^3 = \left(\sum r\right)^2\).
:::

Test them with \(n = 4\): \(1 + 2 + 3 + 4 = 10 = \tfrac12 \times 4 \times 5\); \(1 + 4 + 9 + 16 = 30 = \tfrac16 \times 4 \times 5 \times 9\); \(1 + 8 + 27 + 64 = 100 = \tfrac14 \times 16 \times 25\). A quick test with \(n = 1\), \(2\) or \(3\) is also the best way to check any formula you derive from them.

:::proof Why the sum of the first n integers is n(n + 1)/2
Write the sum twice, once reversed:
\[\begin{aligned}
S &= 1 + 2 + 3 + \dots + (n - 1) + n \\
S &= n + (n - 1) + (n - 2) + \dots + 2 + 1
\end{aligned}\]
Add the two lines term by term. Every column adds to \(n + 1\) (for example \(1 + n\), \(2 + (n - 1)\)), and there are \(n\) columns. So \(2S = n(n + 1)\), and \(S = \tfrac12 n(n + 1)\).
:::

:::proof Why the sum of the squares is n(n + 1)(2n + 1)/6
Start from the identity \((r + 1)^3 - r^3 = 3r^2 + 3r + 1\), which comes from expanding \((r + 1)^3\). Add it for \(r = 1, 2, \dots, n\).

The left side telescopes (each term cancels part of the next), so it leaves \((n + 1)^3 - 1^3\). The right side is \(3\sum r^2 + 3\sum r + n\). Therefore
\[\begin{aligned}
3\sum r^2 &= (n+1)^3 - 1 - \tfrac32 n(n+1) - n \\
&= n^3 + 3n^2 + 2n - \tfrac32 n^2 - \tfrac32 n \\
&= \tfrac12 n(2n^2 + 3n + 1) = \tfrac12 n(n+1)(2n+1)
\end{aligned}\]
and dividing by 3 gives the result. The cubes are proved by induction in [Proof by induction](#math.fm.induction).
:::

:::eg Find (a) \(\displaystyle\sum_{r=1}^{20} r^2\), (b) \(\displaystyle\sum_{r=1}^{12} r^3\), (c) \(\displaystyle\sum_{r=6}^{15} r^3\).
(a) Use \(\sum r^2\) with \(n = 20\):
\[\sum_{r=1}^{20} r^2 = \tfrac16 \times 20 \times 21 \times 41 = 2870\]
(b) Use \(\sum r^3\) with \(n = 12\):
\[\sum_{r=1}^{12} r^3 = \tfrac14 \times 12^2 \times 13^2 = 36 \times 169 = 6084\]
This is also \(78^2\), because \(\sum_{r=1}^{12} r = 78\).

(c) The sum starts at \(r = 6\), so remove \(r = 1\) to \(5\) from the sum to 15:
\[\sum_{r=6}^{15} r^3 = \sum_{r=1}^{15} r^3 - \sum_{r=1}^{5} r^3 = \tfrac14 \times 15^2 \times 16^2 - \tfrac14 \times 5^2 \times 6^2\]
\[= 14400 - 225 = 14175\]
:::

:::warn Starting at r = m
To start at \(r = m\), subtract the sum to \(m - 1\), not to \(m\). In part (c) above the subtracted sum ends at 5 because the first term kept is \(r = 6\). Subtracting up to 6 would throw away a term you need.
:::

### A real context

:::eg A shop builds a pyramid of tins. The top layer is one tin, the next layer is a \(2 \times 2\) square of tins, the next a \(3 \times 3\) square, and so on, so layer \(r\) from the top has \(r^2\) tins. (a) How many tins are in a pyramid of 12 layers? (b) How many are in the bottom 8 of those 12 layers? (c) The shop has 1000 tins. What is the largest number of complete layers it can build, and how many tins are left over?
(a) The total is \(\sum_{r=1}^{12} r^2 = \tfrac16 \times 12 \times 13 \times 25 = 650\) tins.

(b) The bottom 8 layers are layers 5 to 12, so remove the top 4 layers:
\[\sum_{r=5}^{12} r^2 = 650 - \sum_{r=1}^{4} r^2 = 650 - 30 = 620\]
(c) For \(n\) layers the number of tins is \(\tfrac16 n(n+1)(2n+1)\). Try values of \(n\):
\[n = 13: \ \tfrac16 \times 13 \times 14 \times 27 = 819 \qquad n = 14: \ \tfrac16 \times 14 \times 15 \times 29 = 1015\]
The second needs more than 1000 tins, so the shop builds 13 complete layers, using 819 tins and leaving \(1000 - 819 = 181\).
:::

## Related sums

Most exam sums do not look like \(\sum r^2\). Their general term is a polynomial in \(r\), and you break it into pieces you can do.

:::steps
1. Expand the general term so it is a sum of powers of \(r\) (and a constant).
2. Split the sum with the sigma rules: \(\sum r^3\), \(\sum r^2\), \(\sum r\) and \(\sum 1 = n\).
3. Put in the standard results and write the lines with letters before simplifying.
4. Take out the common factors (usually \(n\), often \(n + 1\)) before multiplying anything out, then simplify the bracket and factorise it.
:::

:::eg Show that \(\displaystyle\sum_{r=1}^{n} r(r + 1) = \tfrac13 n(n+1)(n+2)\).
Expand: \(r(r+1) = r^2 + r\). So
\[\begin{aligned}
\sum_{r=1}^{n} r(r+1) &= \sum r^2 + \sum r \\
&= \tfrac16 n(n+1)(2n+1) + \tfrac12 n(n+1) \\
&= \tfrac16 n(n+1)\left[(2n + 1) + 3\right] \\
&= \tfrac16 n(n+1)(2n + 4) = \tfrac13 n(n+1)(n+2)
\end{aligned}\]
**Check** with \(n = 3\): \(2 + 6 + 12 = 20\), and \(\tfrac13 \times 3 \times 4 \times 5 = 20\).
:::

Taking out \(\tfrac16 n(n+1)\) is the key move. If you multiply out first you get a cubic and then have to factorise it again.

:::eg Show that \(\displaystyle\sum_{r=1}^{n} (2r - 1)^2 = \tfrac13 n(2n - 1)(2n + 1)\).
Expand: \((2r - 1)^2 = 4r^2 - 4r + 1\). Then
\[\begin{aligned}
\sum_{r=1}^{n} (2r-1)^2 &= 4\sum r^2 - 4\sum r + \sum 1 \\
&= \tfrac23 n(n+1)(2n+1) - 2n(n+1) + n \\
&= \tfrac13 n\left[2(n+1)(2n+1) - 6(n+1) + 3\right] \\
&= \tfrac13 n\left[4n^2 + 6n + 2 - 6n - 6 + 3\right] \\
&= \tfrac13 n(4n^2 - 1) = \tfrac13 n(2n-1)(2n+1)
\end{aligned}\]
The last step is the difference of two squares. **Check** with \(n = 3\): \(1 + 9 + 25 = 35\), and \(\tfrac13 \times 3 \times 5 \times 7 = 35\).
:::

:::eg Show that \(\displaystyle\sum_{r=1}^{n} r(r+1)(r+2) = \tfrac14 n(n+1)(n+2)(n+3)\).
Expand: \(r(r+1)(r+2) = r^3 + 3r^2 + 2r\). So
\[\begin{aligned}
\sum_{r=1}^{n} r(r+1)(r+2) &= \sum r^3 + 3\sum r^2 + 2\sum r \\
&= \tfrac14 n^2(n+1)^2 + \tfrac12 n(n+1)(2n+1) + n(n+1) \\
&= \tfrac14 n(n+1)\left[n(n+1) + 2(2n+1) + 4\right] \\
&= \tfrac14 n(n+1)\left(n^2 + 5n + 6\right) \\
&= \tfrac14 n(n+1)(n+2)(n+3)
\end{aligned}\]
Each of the three terms contains \(n(n + 1)\), so take that out first. The bracket \(n^2 + 5n + 6\) then factorises.
:::

### Sums to 2n, and odd and even terms

When a sum runs from \(r = n + 1\) to \(2n\), write it as the sum to \(2n\) minus the sum to \(n\). To use a standard result for \(2n\) terms, replace every \(n\) in it by \(2n\).

:::eg (a) Show that \(\displaystyle\sum_{r=n+1}^{2n} r^2 = \tfrac16 n(2n+1)(7n+1)\). (b) Find the sum of the squares of the even numbers \(2^2 + 4^2 + \dots + (2n)^2\), and check it against the sum of the first \(n\) odd squares found above.
(a) The sum is the sum to \(2n\) minus the sum to \(n\):
\[\begin{aligned}
\sum_{r=n+1}^{2n} r^2 &= \tfrac16 (2n)(2n+1)(4n+1) - \tfrac16 n(n+1)(2n+1) \\
&= \tfrac16 n(2n+1)\left[2(4n+1) - (n+1)\right] \\
&= \tfrac16 n(2n+1)(7n+1)
\end{aligned}\]
**Check** with \(n = 2\): \(3^2 + 4^2 = 25\), and \(\tfrac16 \times 2 \times 5 \times 15 = 25\).

(b) The \(r\)th even number is \(2r\), so
\[\sum_{r=1}^{n} (2r)^2 = 4\sum r^2 = \tfrac23 n(n+1)(2n+1)\]
**Check**: even squares and odd squares together make all the squares up to \((2n)^2\).
\[\begin{aligned}
\tfrac23 n(n+1)(2n+1) + \tfrac13 n(2n-1)(2n+1) &= \tfrac13 n(2n+1)\left[2(n+1) + (2n-1)\right] \\
&= \tfrac13 n(2n+1)(4n+1)
\end{aligned}\]
and \(\sum_{r=1}^{2n} r^2 = \tfrac16 (2n)(2n+1)(4n+1) = \tfrac13 n(2n+1)(4n+1)\). They agree.
:::

:::eg (Exam style) (a) Use standard results from MF19 to show that \(\displaystyle\sum_{r=1}^{n} (r + 2)(2r - 1) = \tfrac16 n(4n^2 + 15n - 1)\). (b) Hence find \(\displaystyle\sum_{r=11}^{30} (r + 2)(2r - 1)\).
**(a)** Expand: \((r + 2)(2r - 1) = 2r^2 + 3r - 2\). [B1]
\[\sum_{r=1}^{n} (r+2)(2r-1) = 2\sum r^2 + 3\sum r - 2n\]
\[= \tfrac13 n(n+1)(2n+1) + \tfrac32 n(n+1) - 2n\] [M1]
Take out \(\tfrac16 n\) and put the bracket over 6:
\[\begin{aligned}
&= \tfrac16 n\left[2(2n^2 + 3n + 1) + 9(n + 1) - 12\right] \\
&= \tfrac16 n\left(4n^2 + 15n - 1\right)
\end{aligned}\] [A1]
**Check** with \(n = 2\): \(3 \times 1 + 4 \times 3 = 15\), and \(\tfrac16 \times 2 \times 45 = 15\).

**(b)** Write \(f(n) = \tfrac16 n(4n^2 + 15n - 1)\). The sum from \(r = 11\) is \(f(30) - f(10)\), not \(f(30) - f(11)\). [M1]
\[f(30) = 5 \times 4049 = 20245, \qquad f(10) = \tfrac{10 \times 549}{6} = 915\]
\[\sum_{r=11}^{30} (r+2)(2r-1) = 20245 - 915 = 19330\] [A1]
:::

:::exam Standard results and "show that"
The three results are given in MF19, so quoting them costs nothing, but a "show that" answer needs the line where you substitute them: write \(2\sum r^2 + 3\sum r - 2n\) and then the formulas. Take out common factors before expanding, because the printed answer is nearly always factorised. For a numerical sum such as \(\sum_{r=1}^{20} r^2\), show the formula and the substitution: a bare calculator answer earns no marks.
:::

## The method of differences

Some sums have no standard result, but their terms cancel almost completely. Take \(\dfrac{1}{r} - \dfrac{1}{r+1}\) and add it for \(r = 1, 2, 3, \dots\):
\[\left(1 - \tfrac12\right) + \left(\tfrac12 - \tfrac13\right) + \left(\tfrac13 - \tfrac14\right) + \dots\]
Every term except the very first and the very last cancels with its neighbour, like the sections of a collapsing telescope. This is the **method of differences** (also called telescoping).

:::key The method of differences
If the general term can be written \(u_r = f(r) - f(r + 1)\), then
\[\sum_{r=1}^{n} \left[f(r) - f(r+1)\right] = f(1) - f(n+1)\]
If instead \(u_r = f(r) - f(r + k)\), the first \(k\) terms of \(f\) and the last \(k\) terms of \(-f\) survive, so \(2k\) terms are left. For example, with \(k = 2\):
\[\sum_{r=1}^{n} \left[f(r) - f(r+2)\right] = f(1) + f(2) - f(n+1) - f(n+2)\]
If the difference is the other way, \(u_r = f(r + 1) - f(r)\), the sum is \(f(n + 1) - f(1)\).
:::

Do not rely on the formula alone. The mark scheme looks for the written-out terms, so use the same routine every time.

:::steps
1. Write the general term as a difference \(f(r) - f(r + k)\). A fraction with two factors in the denominator needs partial fractions ([Partial fractions and the binomial series](#math.p3.partial)).
2. Write out the terms for \(r = 1, 2, 3\), then dots, then \(r = n - 1\) and \(r = n\). Writing the last **two** lines is what stops you losing terms at the far end.
3. Cross out the pairs that cancel. Collect what is left: the first few and the last few terms.
4. Simplify, usually to one fraction in \(n\), and test with \(n = 1\) or \(2\).
:::

:::eg Show that \(\dfrac{1}{r(r+1)} = \dfrac1r - \dfrac{1}{r+1}\), and hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{r(r+1)}\).
Over a common denominator: \(\dfrac1r - \dfrac{1}{r+1} = \dfrac{(r+1) - r}{r(r+1)} = \dfrac{1}{r(r+1)}\).

Now write out the terms:
\[\begin{aligned}
r = 1: &\quad \tfrac11 - \tfrac12 \\
r = 2: &\quad \tfrac12 - \tfrac13 \\
r = 3: &\quad \tfrac13 - \tfrac14 \\
&\quad \vdots \\
r = n - 1: &\quad \tfrac{1}{n-1} - \tfrac1n \\
r = n: &\quad \tfrac1n - \tfrac{1}{n+1}
\end{aligned}\]
Everything cancels except \(\tfrac11\) from the first line and \(-\tfrac{1}{n+1}\) from the last:
\[\sum_{r=1}^{n} \frac{1}{r(r+1)} = 1 - \frac{1}{n+1} = \frac{n}{n+1}\]
**Check** with \(n = 3\): \(\tfrac12 + \tfrac16 + \tfrac1{12} = \tfrac{6 + 2 + 1}{12} = \tfrac34\), and \(\tfrac{3}{4}\).
:::

:::eg Show that \(\dfrac{1}{(2r-1)(2r+1)} = \dfrac12\left(\dfrac{1}{2r-1} - \dfrac{1}{2r+1}\right)\), and hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{(2r-1)(2r+1)}\).
The bracket is \(\dfrac{(2r+1) - (2r-1)}{(2r-1)(2r+1)} = \dfrac{2}{(2r-1)(2r+1)}\), so half of it is the original fraction.

Write out the terms of the bracket:
\[\begin{aligned}
r = 1: &\quad \tfrac11 - \tfrac13 \\
r = 2: &\quad \tfrac13 - \tfrac15 \\
&\quad \vdots \\
r = n - 1: &\quad \tfrac{1}{2n-3} - \tfrac{1}{2n-1} \\
r = n: &\quad \tfrac{1}{2n-1} - \tfrac{1}{2n+1}
\end{aligned}\]
The sum of the bracket is \(1 - \tfrac{1}{2n+1}\), so
\[\sum_{r=1}^{n} \frac{1}{(2r-1)(2r+1)} = \frac12\left(1 - \frac{1}{2n+1}\right) = \frac{n}{2n+1}\]
**Check** with \(n = 2\): \(\tfrac13 + \tfrac1{15} = \tfrac25\), and \(\tfrac{2}{5}\).
:::

### Gaps of two or more

When the denominator factors differ by 2, such as \(r(r+2)\), the terms that cancel are two lines apart. Four terms survive, not two. A table shows this best. For \(\dfrac{1}{r(r+2)} = \dfrac12\left(\dfrac1r - \dfrac{1}{r+2}\right)\), the brackets contain:

| \(r\) | \(+\dfrac1r\) | \(-\dfrac{1}{r+2}\) |
|---|---|---|
| 1 | \(1\) | \(-\tfrac13\) |
| 2 | \(\tfrac12\) | \(-\tfrac14\) |
| 3 | \(\tfrac13\) | \(-\tfrac15\) |
| 4 | \(\tfrac14\) | \(-\tfrac16\) |
| \(\vdots\) | \(\vdots\) | \(\vdots\) |
| \(n-1\) | \(\tfrac{1}{n-1}\) | \(-\tfrac{1}{n+1}\) |
| \(n\) | \(\tfrac1n\) | \(-\tfrac{1}{n+2}\) |

In the middle, each \(-\tfrac13\), \(-\tfrac14\), … in the right column cancels a \(+\tfrac13\), \(+\tfrac14\), … in the left column. The left column keeps its first two entries, \(1\) and \(\tfrac12\). The right column keeps its last two, \(-\tfrac{1}{n+1}\) and \(-\tfrac{1}{n+2}\).

:::eg Find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{r(r+2)}\).
Partial fractions give \(\dfrac{1}{r(r+2)} = \dfrac12\left(\dfrac1r - \dfrac{1}{r+2}\right)\). From the table, the four surviving terms are
\[\begin{aligned}
\sum_{r=1}^{n} \frac{1}{r(r+2)} &= \frac12\left(1 + \frac12 - \frac{1}{n+1} - \frac{1}{n+2}\right) \\
&= \frac34 - \frac{2n+3}{2(n+1)(n+2)}
\end{aligned}\]
**Check** with \(n = 1\): \(\tfrac13\), and \(\tfrac34 - \tfrac{5}{12} = \tfrac13\).
:::

### Three factors, and sums that are not fractions

Three factors in the denominator use partial fractions with three terms, which you then regroup into two differences.

:::eg Find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{r(r+1)(r+2)}\).
Partial fractions: \(\dfrac{1}{r(r+1)(r+2)} = \dfrac{1/2}{r} - \dfrac{1}{r+1} + \dfrac{1/2}{r+2}\). Regroup the three pieces into two differences:
\[\frac{1}{r(r+1)(r+2)} = \frac12\left[\frac{1}{r(r+1)} - \frac{1}{(r+1)(r+2)}\right]\]
(The two fractions in the bracket over a common denominator give \(\dfrac{(r+2) - r}{r(r+1)(r+2)} = \dfrac{2}{r(r+1)(r+2)}\).) This is \(\tfrac12\left[f(r) - f(r+1)\right]\) with \(f(r) = \dfrac{1}{r(r+1)}\), so
\[\sum_{r=1}^{n} \frac{1}{r(r+1)(r+2)} = \frac12\left[f(1) - f(n+1)\right] = \frac12\left[\frac12 - \frac{1}{(n+1)(n+2)}\right]\]
\[= \frac14 - \frac{1}{2(n+1)(n+2)}\]
**Check** with \(n = 1\): \(\tfrac16\), and \(\tfrac14 - \tfrac1{12} = \tfrac16\).
:::

The method is not only for fractions. Any term you can write as \(f(r) - f(r+1)\) will do, and it can also join the polynomial sums you met earlier.

:::eg (a) Show that \(r \times r! = (r+1)! - r!\), and hence find \(\displaystyle\sum_{r=1}^{n} r \times r!\). (b) Show that \(\dfrac{1}{\sqrt{r} + \sqrt{r+1}} = \sqrt{r+1} - \sqrt{r}\), and hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{\sqrt{r} + \sqrt{r+1}}\). (c) Show that \(r(r+1)(r+2) - (r-1)r(r+1) = 3r(r+1)\), and hence find \(\displaystyle\sum_{r=1}^{n} r(r+1)\).
(a) \((r+1)! = (r+1) \times r!\), so \((r+1)! - r! = (r + 1 - 1) \times r! = r \times r!\). The sum telescopes, with \(f(r) = r!\) in the form \(f(r+1) - f(r)\):
\[\sum_{r=1}^{n} r \times r! = (n+1)! - 1! = (n+1)! - 1\]
**Check** with \(n = 3\): \(1 + 4 + 18 = 23 = 4! - 1\).

(b) Multiply top and bottom by \(\sqrt{r+1} - \sqrt{r}\) (rationalising the denominator):
\[\frac{\sqrt{r+1} - \sqrt{r}}{(\sqrt{r+1} + \sqrt{r})(\sqrt{r+1} - \sqrt{r})} = \frac{\sqrt{r+1} - \sqrt{r}}{(r+1) - r} = \sqrt{r+1} - \sqrt{r}\]
The terms are
\[(\sqrt2 - 1) + (\sqrt3 - \sqrt2) + \dots + (\sqrt{n+1} - \sqrt{n})\]
so the sum is \(\sqrt{n+1} - 1\).

(c) Take out the common factor \(r(r+1)\): \(r(r+1)\left[(r+2) - (r-1)\right] = 3r(r+1)\). With \(g(r) = r(r+1)(r+2)\) the left side is \(g(r) - g(r-1)\), which telescopes to \(g(n) - g(0)\), and \(g(0) = 0\):
\[3\sum_{r=1}^{n} r(r+1) = n(n+1)(n+2)\]
so \(\sum r(r+1) = \tfrac13 n(n+1)(n+2)\), the same answer as the sigma method.
:::

:::warn Write the last two lines
Students lose marks in three ways with differences: they write out only the first lines and guess the end; they leave out one surviving term (for a gap of 2 or 3 there are 4 or 6 terms left, not 2); and they forget the factor such as \(\tfrac12\) from the partial fractions. Always write out \(r = 1, 2, 3\) and \(r = n - 1, n\), count the survivors, and check with \(n = 1\).
:::

## Convergence and the sum to infinity

The sum to \(n\) terms, \(S_n\), changes as \(n\) grows. For \(\sum \dfrac{1}{r(r+1)}\) we found \(S_n = 1 - \dfrac{1}{n+1}\). As \(n\) gets very large, \(\dfrac{1}{n+1}\) shrinks towards 0, so \(S_n\) creeps up towards 1.

:::def Convergent series
A series **converges** if its sum to \(n\) terms \(S_n\) approaches a fixed finite value as \(n \to \infty\). That value is the **sum to infinity**, \(S_\infty = \displaystyle\sum_{r=1}^{\infty} u_r\). A series that does not converge **diverges**.
:::

:::plot The partial sums Sₙ = 1 − 1/(n + 1) of 1/(r(r + 1)) climb towards the dashed line at 1 but never reach it. S₁ = 1/2, S₃ = 3/4 and S₉ = 9/10. Only whole numbers n give partial sums: the curve joins those points to show the trend.
--f "1-1/(x+1)" --label "Sₙ = 1 − 1/(n + 1)" --x 0 10.5 --y 0 1.5 --hline 1 --pt "1,0.5,S₁ = 1/2@se" --pt "3,0.75,S₃ = 3/4@se" --pt "9,0.9,S₉ = 9/10@se" --legend tr --xlabel "n"
:::

:::key Finding a sum to infinity
1. Find \(S_n\) as an expression in \(n\) (standard results or differences).
2. Let \(n \to \infty\). Terms such as \(\dfrac1n\), \(\dfrac{1}{n+1}\), \(\dfrac{1}{2n+3}\) and \(\dfrac{1}{n^2}\) tend to 0, and so does \(\left(\tfrac12\right)^n\).
3. If \(S_n\) tends to a finite number, the series converges and that number is \(S_\infty\). If \(S_n\) grows without bound, or keeps changing between values, the series diverges.
:::

For a geometric series with common ratio \(|r| < 1\) you already know \(S_\infty = \dfrac{a}{1 - r}\) ([Series: binomial expansion and progressions](#math.p1.series)); it comes from the same idea, since \(S_n = \dfrac{a(1 - r^n)}{1 - r}\) and \(r^n \to 0\).

With the method of differences the limit is quick: \(S_\infty = f(1) - \lim\limits_{n \to \infty} f(n+1)\), which is the first term of \(f\) when \(f(n)\) tends to 0.

:::eg Find the sum to infinity of each series, or explain why it does not converge. (a) \(\displaystyle\sum_{r=1}^{\infty} \dfrac{1}{(2r-1)(2r+1)}\). (b) \(\displaystyle\sum_{r=1}^{\infty} r\). (c) \(\displaystyle\sum_{r=1}^{\infty} \dfrac{1}{\sqrt{r} + \sqrt{r+1}}\).
(a) From above, \(S_n = \dfrac{n}{2n+1} = \dfrac12 - \dfrac{1}{2(2n+1)}\), or equivalently \(\dfrac12\left(1 - \dfrac{1}{2n+1}\right)\). As \(n \to \infty\), \(\dfrac{1}{2n+1} \to 0\), so \(S_n \to \dfrac12\). The series converges and \(S_\infty = \dfrac12\).

(b) \(S_n = \tfrac12 n(n+1)\), which grows without bound as \(n \to \infty\). The series diverges.

(c) From above, \(S_n = \sqrt{n+1} - 1\), which grows without bound. The series diverges, even though each term \(\dfrac{1}{\sqrt{r} + \sqrt{r+1}}\) tends to 0.
:::

:::warn Small terms are not enough
If the terms do not tend to 0 the series cannot converge, but terms that tend to 0 do not guarantee convergence: in (c) they tend to 0 and the series still diverges. Always decide from \(S_n\), and write "as \(n \to \infty\), \(\dfrac{1}{2n+1} \to 0\), so \(S_n \to \dots\)" to earn the mark.
:::

:::eg A charity receives a legacy that pays it \(\dfrac{600}{r(r+1)}\) pounds in week \(r\), for \(r = 1, 2, 3, \dots\). (a) Find the total received in the first \(n\) weeks. (b) Show that the total can never reach £600. (c) After how many weeks does the total first exceed £595?
(a) Using \(\dfrac{1}{r(r+1)} = \dfrac1r - \dfrac{1}{r+1}\), the total is
\[S_n = 600\left(1 - \frac{1}{n+1}\right) = \frac{600n}{n+1} \text{ pounds}\]
(b) As \(n \to \infty\), \(\dfrac{1}{n+1} \to 0\), so \(S_n\) approaches \(600\) from below. Since \(\dfrac{600}{n+1} > 0\), \(S_n = 600 - \dfrac{600}{n+1} < 600\) for every \(n\).

(c) Solve \(\dfrac{600n}{n+1} > 595\):
\[600n > 595n + 595 \quad\Rightarrow\quad 5n > 595 \quad\Rightarrow\quad n > 119\]
So \(n = 120\), and the total after 120 weeks is \(\tfrac{72000}{121} = £595.04\). After 119 weeks the total is exactly £595, which does not exceed it.
:::

### Putting it together: a full exam question

Questions often chain the three ideas: a polynomial sum from the standard results, a differences sum, and a deduction about convergence.

:::eg (Exam style) (a) Use standard results from MF19 to show that \(\displaystyle\sum_{r=1}^{n} (r^2 + 3r + 1) = \tfrac13 n(n+2)(n+4)\). (b) Use the method of differences to show that \(\displaystyle\sum_{r=1}^{n} \dfrac{3}{r(r+3)} = \dfrac{11}{6} - \dfrac{1}{n+1} - \dfrac{1}{n+2} - \dfrac{1}{n+3}\). (c) Deduce the value of \(\displaystyle\sum_{r=1}^{\infty} \dfrac{3}{r(r+3)}\).
**(a)**
\[\sum r^2 + 3\sum r + \sum 1 = \tfrac16 n(n+1)(2n+1) + \tfrac32 n(n+1) + n\] [M1]
Take out \(\tfrac16 n\):
\[= \tfrac16 n\left[2n^2 + 3n + 1 + 9n + 9 + 6\right]\] [M1]
\[= \tfrac16 n\left(2n^2 + 12n + 16\right) = \tfrac13 n(n^2 + 6n + 8) = \tfrac13 n(n+2)(n+4)\] [A1]
**(b)** Partial fractions: \(\dfrac{3}{r(r+3)} = \dfrac1r - \dfrac{1}{r+3}\). [B1]

Write out the first three and the last three terms:
\[\begin{aligned}
r = 1: &\quad \tfrac11 - \tfrac14 \\
r = 2: &\quad \tfrac12 - \tfrac15 \\
r = 3: &\quad \tfrac13 - \tfrac16 \\
&\quad \vdots \\
r = n-1: &\quad \tfrac{1}{n-1} - \tfrac{1}{n+2} \\
r = n: &\quad \tfrac1n - \tfrac{1}{n+3}
\end{aligned}\] [M1]
The terms cancel in threes: the \(-\tfrac14\), \(-\tfrac15\), \(-\tfrac16\), … each cancel a later positive term. [M1] (dependent)
\[\text{Sum} = 1 + \tfrac12 + \tfrac13 - \tfrac{1}{n+1} - \tfrac{1}{n+2} - \tfrac{1}{n+3} = \tfrac{11}{6} - \tfrac{1}{n+1} - \tfrac{1}{n+2} - \tfrac{1}{n+3}\] [A1]
**Check** with \(n = 1\): \(\tfrac34\), and \(\tfrac{11}{6} - \tfrac12 - \tfrac13 - \tfrac14 = \tfrac34\).

**(c)** As \(n \to \infty\), each of \(\dfrac{1}{n+1}\), \(\dfrac{1}{n+2}\), \(\dfrac{1}{n+3}\) tends to 0, so the sum to infinity is \(\dfrac{11}{6}\). [B1]
:::

:::exam What the examiner looks for
A differences question has three predictable marks: the partial fractions (or the form \(f(r) - f(r+k)\)), written-out terms that show the cancelling, and the final simplified expression. "Deduce the sum to infinity" is worth a mark for \(S_\infty\) and needs a phrase such as "as \(n \to \infty\), \(\dfrac{1}{n+1} \to 0\)". "Explain why the series converges" wants the same phrase, and the limit. Method of differences needs no formula from MF19: it is a method, not a result.
:::

:::board
In the UK A Levels (AQA, Edexcel, OCR), summation of series is part of Further Mathematics core pure content, and Edexcel IAL Further Pure 1 includes it as well. The topics are the same as here: the standard results for \(\sum r\), \(\sum r^2\) and \(\sum r^3\), and the method of differences.
:::

:::exam What MF19 gives you
MF19 lists \(\sum r\), \(\sum r^2\) and \(\sum r^3\) (to \(n\) terms from \(r = 1\)), so you do not need to memorise them. It does not list the method of differences, partial fractions, or the identity \((r + 1)^3 - r^3 = 3r^2 + 3r + 1\). Know how to find partial fractions for \(\dfrac{1}{r(r+k)}\) and \(\dfrac{1}{(ar+b)(ar+c)}\) quickly, and remember that \(\sum 1 = n\).
:::

:::eg Spot the error: find \(\displaystyle\sum_{r=1}^{n} (3r^2 - 4)\) in the form \(\tfrac12 n(an^2 + bn + c)\), for 4 marks.
The scheme gives B1 for \(\sum 3r^2\), B1 for \(\sum 4\), M1 for combining the two results and A1 for the final form. A student wrote this answer.

Line 1: \(\sum 3r^2 = 3 \times \tfrac16 n(n+1)(2n+1) = \tfrac12 n(n+1)(2n+1)\)
Line 2: \(\sum 4 = 4\)
Line 3: \(\sum (3r^2 - 4) = \tfrac12 n(n+1)(2n+1) - 4 = \tfrac12\left(2n^3 + 3n^2 + n - 8\right)\)

Line 1 is correct. [B1]

**Line 2 is wrong.** [B0] The sum of the constant 4 over \(n\) terms is \(4n\), not 4. The student treats the number as if it were one term.

Line 3 combines the two results correctly, using the student's value. [M1] But the final form is wrong, so the accuracy mark is lost. [A0] The student scores 2 out of 4.

Correct line 2: \(\sum_{r=1}^{n} 4 = 4n\). Then
\[\begin{aligned}
\sum (3r^2 - 4) &= \tfrac12 n(n+1)(2n+1) - 4n \\
&= \tfrac12 n\left[2n^2 + 3n + 1 - 8\right] = \tfrac12 n\left(2n^2 + 3n - 7\right)
\end{aligned}\]
so \(a = 2\), \(b = 3\), \(c = -7\). **Check** with \(n = 2\): \(-1 + 8 = 7\), and \(\tfrac12 \times 2 \times (8 + 6 - 7) = 7\).
:::

:::try Start easy, finish at exam standard
Q: Evaluate \(\displaystyle\sum_{r=1}^{14} r\) and \(\displaystyle\sum_{r=1}^{14} r^3\).
A: \(\sum r = \tfrac12 \times 14 \times 15 = 105\). \(\sum r^3 = 105^2 = 11025\), or \(\tfrac14 \times 14^2 \times 15^2 = 11025\).
Q: Evaluate \(\displaystyle\sum_{r=1}^{9} r^2\) and \(\displaystyle\sum_{r=4}^{10} r^2\).
A: \(\tfrac16 \times 9 \times 10 \times 19 = 285\). Next, \(\sum_{r=1}^{10} r^2 = 385\) and \(\sum_{r=1}^{3} r^2 = 14\), so \(\sum_{r=4}^{10} r^2 = 385 - 14 = 371\).
Q: Show that \(\displaystyle\sum_{r=1}^{n} (4r - 3) = n(2n - 1)\).
A: \(4\sum r - 3\sum 1 = 2n(n+1) - 3n = 2n^2 - n = n(2n-1)\). Check with \(n = 3\): \(1 + 5 + 9 = 15 = 3 \times 5\).
Q: Show that \(\displaystyle\sum_{r=1}^{n} (r^2 - 3r + 2) = \tfrac13 n(n-1)(n-2)\).
A: \[\begin{aligned}
\textstyle\sum r^2 - 3\sum r + 2n &= \tfrac16 n(n+1)(2n+1) - \tfrac32 n(n+1) + 2n \\
&= \tfrac16 n\left[2n^2 + 3n + 1 - 9n - 9 + 12\right] \\
&= \tfrac16 n\left(2n^2 - 6n + 4\right) = \tfrac13 n(n-1)(n-2)
\end{aligned}\]
Q: Show that \(\displaystyle\sum_{r=1}^{n} r(r+3) = \tfrac13 n(n+1)(n+5)\).
A: \(\sum r^2 + 3\sum r = \tfrac16 n(n+1)(2n+1) + \tfrac32 n(n+1) = \tfrac16 n(n+1)\left[2n + 1 + 9\right] = \tfrac13 n(n+1)(n+5)\).
Q: Find the sum of the first \(n\) terms of \(2 \times 4 + 4 \times 6 + 6 \times 8 + \dots\), and evaluate it for \(n = 20\).
A: The \(r\)th term is \(2r(2r+2) = 4r(r+1)\). So the sum is \(4 \times \tfrac13 n(n+1)(n+2) = \tfrac43 n(n+1)(n+2)\), using the result for \(\sum r(r+1)\). For \(n = 20\): \(\tfrac43 \times 20 \times 21 \times 22 = 12320\). Check with \(n = 3\): \(8 + 24 + 48 = 80\).
Q: Show that \(\dfrac{1}{(r+2)(r+3)} = \dfrac{1}{r+2} - \dfrac{1}{r+3}\), and hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{(r+2)(r+3)}\).
A: The difference is \(\dfrac{(r+3) - (r+2)}{(r+2)(r+3)} = \dfrac{1}{(r+2)(r+3)}\). The terms \(\tfrac13 - \tfrac14\), \(\tfrac14 - \tfrac15\), …, \(\tfrac{1}{n+2} - \tfrac{1}{n+3}\) leave
\[\tfrac13 - \tfrac{1}{n+3} = \frac{n}{3(n+3)}\]
Q: Find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{(2r+1)(2r+3)}\) and its sum to infinity.
A: \(\dfrac{1}{(2r+1)(2r+3)} = \dfrac12\left(\dfrac{1}{2r+1} - \dfrac{1}{2r+3}\right)\). The terms leave \(\tfrac12\left(\tfrac13 - \tfrac{1}{2n+3}\right) = \dfrac{n}{3(2n+3)}\). As \(n \to \infty\), \(\tfrac{1}{2n+3} \to 0\), so \(S_\infty = \tfrac16\).
Q: Show that \(2r + 1 = (r+1)^2 - r^2\), and hence find \(\displaystyle\sum_{r=1}^{n} (2r + 1)\).
A: \((r+1)^2 - r^2 = r^2 + 2r + 1 - r^2 = 2r + 1\). The sum telescopes to \((n+1)^2 - 1^2 = n^2 + 2n\). Check with the standard results: \(2 \times \tfrac12 n(n+1) + n = n^2 + 2n\).
Q: A series has \(S_n = \dfrac{3n^2 + 1}{n^2 + 2n}\). Does it converge? If so, find the sum to infinity.
A: Divide top and bottom by \(n^2\): \(S_n = \dfrac{3 + 1/n^2}{1 + 2/n}\). As \(n \to \infty\), \(\tfrac{1}{n^2} \to 0\) and \(\tfrac2n \to 0\), so \(S_n \to 3\). The series converges and \(S_\infty = 3\).
Q: Explain why the series \(1 - 1 + 1 - 1 + 1 - \dots\) does not converge.
A: \(S_1 = 1\), \(S_2 = 0\), \(S_3 = 1\), \(S_4 = 0\), and so on. \(S_n\) alternates between 1 and 0, so it does not approach a single value as \(n \to \infty\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Show that \(\displaystyle\sum_{r=1}^{n} (3r^2 + r) = n(n+1)^2\).
A: \(3\sum r^2 + \sum r = \tfrac12 n(n+1)(2n+1) + \tfrac12 n(n+1)\) [M1]
\(= \tfrac12 n(n+1)\left[(2n + 1) + 1\right]\) [M1]
\(= \tfrac12 n(n+1)(2n+2) = n(n+1)^2\). [A1]
Q: [3 marks] ★ Find the value of \(\displaystyle\sum_{r=1}^{20} \left(r^3 - 2r\right)\).
A: \(\sum_{r=1}^{20} r^3 = \tfrac14 \times 20^2 \times 21^2 = 44100\). [B1]
\(\sum_{r=1}^{20} r = \tfrac12 \times 20 \times 21 = 210\), so \(2\sum r = 420\). [B1]
\(44100 - 420 = 43680\). [A1]
Q: [4 marks] ★★ Show that \(\displaystyle\sum_{r=n+1}^{2n} r^3 = \tfrac14 n^2(3n+1)(5n+3)\).
A: The sum is the sum to \(2n\) minus the sum to \(n\):
\[\tfrac14 (2n)^2(2n+1)^2 - \tfrac14 n^2(n+1)^2\] [M1] [A1]
Take out \(\tfrac14 n^2\) and use the difference of two squares:
\[\tfrac14 n^2\left[4(2n+1)^2 - (n+1)^2\right] = \tfrac14 n^2\left[2(2n+1) - (n+1)\right]\left[2(2n+1) + (n+1)\right]\] [M1]
\[= \tfrac14 n^2(3n+1)(5n+3)\] [A1]
Q: [5 marks] ★★ Use the method of differences to find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{(r+1)(r+3)}\) in terms of \(n\).
A: \(\dfrac{1}{(r+1)(r+3)} = \dfrac12\left(\dfrac{1}{r+1} - \dfrac{1}{r+3}\right)\). [B1]
Write out the terms \(r = 1, 2, 3, \dots, n-1, n\): the brackets begin \(\tfrac12 - \tfrac14\), \(\tfrac13 - \tfrac15\), \(\tfrac14 - \tfrac16\) and end \(\tfrac{1}{n} - \tfrac{1}{n+2}\), \(\tfrac{1}{n+1} - \tfrac{1}{n+3}\). [M1]
Four terms survive: [M1] (dependent)
\[\frac12\left(\frac12 + \frac13 - \frac{1}{n+2} - \frac{1}{n+3}\right)\] [A1]
\[= \frac{5}{12} - \frac{2n+5}{2(n+2)(n+3)}\] [A1]
Q: [4 marks] ★★ Show that \(\dfrac{r}{(r+1)!} = \dfrac{1}{r!} - \dfrac{1}{(r+1)!}\), and hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{r}{(r+1)!}\).
A: \(\dfrac{1}{r!} - \dfrac{1}{(r+1)!} = \dfrac{(r+1) - 1}{(r+1)!}\) [M1] \(= \dfrac{r}{(r+1)!}\). [A1]
The terms \(\tfrac{1}{1!} - \tfrac{1}{2!}\), \(\tfrac{1}{2!} - \tfrac{1}{3!}\), … leave \(\tfrac{1}{1!} - \tfrac{1}{(n+1)!}\), [M1] so the sum is \(1 - \dfrac{1}{(n+1)!}\). [A1]
Q: [3 marks] ★★ (a) Show that \(\displaystyle\sum_{r=1}^{n} \ln\left(\dfrac{r+1}{r}\right) = \ln(n+1)\). (b) Hence explain why \(\displaystyle\sum_{r=1}^{\infty} \ln\left(\dfrac{r+1}{r}\right)\) does not converge.
A: (a) \(\ln\left(\dfrac{r+1}{r}\right) = \ln(r+1) - \ln r\), so the terms are \(\ln 2 - \ln 1\), \(\ln 3 - \ln 2\), …, \(\ln(n+1) - \ln n\). [M1] They leave \(\ln(n+1) - \ln 1 = \ln(n+1)\). [A1]
(b) As \(n \to \infty\), \(\ln(n+1) \to \infty\), so \(S_n\) has no finite limit and the series diverges. [B1]
Q: [11 marks] ★★★ The \(r\)th term of a series is \(u_r = \dfrac{2r+1}{r^2(r+1)^2}\). (a) Show that \(u_r = \dfrac{1}{r^2} - \dfrac{1}{(r+1)^2}\). (b) Find \(\displaystyle\sum_{r=1}^{n} u_r\) in terms of \(n\). (c) Write down \(\displaystyle\sum_{r=1}^{\infty} u_r\). (d) Find the least value of \(n\) for which the sum to infinity exceeds the sum to \(n\) terms by less than 0.001. (e) Find \(\displaystyle\sum_{r=11}^{20} u_r\) as an exact fraction.
H: For (a) put the right side over the common denominator \(r^2(r+1)^2\); the numerator is \((r+1)^2 - r^2\).
H: For (d) the difference between the sum to infinity and \(S_n\) is the leftover term \(\dfrac{1}{(n+1)^2}\).
H: For (e) the sum from \(r = 11\) to 20 is \(S_{20} - S_{10}\).
A: (a) \(\dfrac{1}{r^2} - \dfrac{1}{(r+1)^2} = \dfrac{(r+1)^2 - r^2}{r^2(r+1)^2}\) [M1] \(= \dfrac{2r+1}{r^2(r+1)^2}\). [A1]
(b) The terms are \(1 - \tfrac14\), \(\tfrac14 - \tfrac19\), …, \(\tfrac{1}{n^2} - \tfrac{1}{(n+1)^2}\). [M1]
Every middle term cancels: [M1] (dependent)
\[S_n = 1 - \frac{1}{(n+1)^2}\] [A1]
(c) As \(n \to \infty\), \(\dfrac{1}{(n+1)^2} \to 0\), so \(S_\infty = 1\). [B1]
(d) \(S_\infty - S_n = \dfrac{1}{(n+1)^2} < 0.001\) [M1]
\((n+1)^2 > 1000\), so \(n + 1 > 31.6\ldots\) [A1] and the least \(n\) is 31. [A1]
(e) \(S_{20} - S_{10} = \left(1 - \tfrac{1}{441}\right) - \left(1 - \tfrac{1}{121}\right)\) [M1]
\(= \tfrac{1}{121} - \tfrac{1}{441} = \dfrac{320}{53361}\). [A1]
Q: [9 marks] (#math.p3.partial) ★★★ (a) Use standard results from MF19 to show that \(\displaystyle\sum_{r=1}^{n} r(3r-1) = n^2(n+1)\). (b) Show that \(\dfrac{1}{(3r-1)(3r+2)} = \dfrac13\left(\dfrac{1}{3r-1} - \dfrac{1}{3r+2}\right)\). (c) Hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{(3r-1)(3r+2)}\) in the form \(\dfrac{n}{k(3n+2)}\). (d) Find the sum to infinity of the series in (c).
H: For (a), expand \(r(3r - 1)\) first, then put \(3\sum r^2 - \sum r\) over a common denominator.
H: For (b), the bracket combines to \(\dfrac{(3r+2) - (3r-1)}{(3r-1)(3r+2)}\).
H: For (c), \(3(r+1) - 1 = 3r + 2\), so the terms cancel one line apart; write the first and last lines.
A: (a) \(r(3r-1) = 3r^2 - r\), so the sum is \(3\sum r^2 - \sum r\). [M1]
\[= \tfrac12 n(n+1)(2n+1) - \tfrac12 n(n+1)\] [M1]
\[= \tfrac12 n(n+1)(2n) = n^2(n+1)\] [A1]
(b) \(\dfrac13\left(\dfrac{1}{3r-1} - \dfrac{1}{3r+2}\right) = \dfrac13 \times \dfrac{(3r+2) - (3r-1)}{(3r-1)(3r+2)}\) [M1] \(= \dfrac{1}{(3r-1)(3r+2)}\). [A1]
(c) The brackets are \(\tfrac12 - \tfrac15\), \(\tfrac15 - \tfrac18\), …, \(\tfrac{1}{3n-1} - \tfrac{1}{3n+2}\). [M1]
They leave \(\dfrac13\left(\dfrac12 - \dfrac{1}{3n+2}\right)\) [A1]
\[= \frac13 \times \frac{3n}{2(3n+2)} = \frac{n}{2(3n+2)}\] [A1]
(d) As \(n \to \infty\), \(\dfrac{n}{2(3n+2)} = \dfrac{1}{2(3 + 2/n)} \to \dfrac16\), so the sum to infinity is \(\dfrac16\). [B1]
:::

:::try Stretch for A*
Q: [11 marks] ★★★ The \(r\)th triangular number is \(T_r = \tfrac12 r(r+1)\), so \(T_1 = 1\), \(T_2 = 3\), \(T_3 = 6\). Balls are stacked in a tetrahedron whose layers are triangles with \(T_1, T_2, \dots, T_n\) balls. (a) Show that the tetrahedron holds \(\displaystyle\sum_{r=1}^{n} T_r = \tfrac16 n(n+1)(n+2)\) balls. (b) Show that \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{T_r} = \dfrac{2n}{n+1}\), and write down \(\displaystyle\sum_{r=1}^{\infty} \dfrac{1}{T_r}\). (c) Find the least \(n\) for which \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{T_r} > 1.99\).
H: For (a), \(T_r = \tfrac12(r^2 + r)\). You have already found the sum of \(r(r+1)\) in this chapter.
H: For (b), \(\dfrac{1}{T_r} = \dfrac{2}{r(r+1)}\) and this has a difference form.
H: For (c), solve \(\dfrac{2n}{n+1} > 1.99\) as an inequality; \(n + 1 > 0\), so multiply through.
A: (a) \(\sum T_r = \tfrac12\left(\sum r^2 + \sum r\right)\). [M1]
\[= \tfrac12\left[\tfrac16 n(n+1)(2n+1) + \tfrac12 n(n+1)\right]\] [M1]
\[= \tfrac12 \times \tfrac16 n(n+1)\left[(2n+1) + 3\right]\] [M1]
\[= \tfrac1{12} n(n+1)(2n+4) = \tfrac16 n(n+1)(n+2)\] [A1]
(b) \(\dfrac{1}{T_r} = \dfrac{2}{r(r+1)} = 2\left(\dfrac1r - \dfrac{1}{r+1}\right)\). [B1]
The terms telescope: \(2\left(1 - \dfrac{1}{n+1}\right)\) [M1] \(= \dfrac{2n}{n+1}\). [A1]
As \(n \to \infty\), \(\dfrac{1}{n+1} \to 0\), so the sum to infinity is 2. [B1]
(c) \(\dfrac{2n}{n+1} > 1.99\) gives \(2n > 1.99n + 1.99\) [M1] so \(0.01n > 1.99\) and \(n > 199\). [A1]
The least \(n\) is 200. [A1] (For \(n = 199\) the sum is exactly 1.99, which is not greater than 1.99.)
Q: [6 marks] ★★★ (a) Show that
\[\frac{1}{r(r+1)(r+2)(r+3)} = \frac13\left[\frac{1}{r(r+1)(r+2)} - \frac{1}{(r+1)(r+2)(r+3)}\right]\]
(b) Hence find \(\displaystyle\sum_{r=1}^{n} \dfrac{1}{r(r+1)(r+2)(r+3)}\). (c) Find the sum to infinity.
H: In (a), the common denominator of the two fractions inside the bracket is \(r(r+1)(r+2)(r+3)\).
H: In (b), name \(f(r) = \dfrac{1}{r(r+1)(r+2)}\); the bracket is \(f(r) - f(r+1)\).
A: (a) Over the common denominator the bracket is \(\dfrac{(r+3) - r}{r(r+1)(r+2)(r+3)}\) [M1] \(= \dfrac{3}{r(r+1)(r+2)(r+3)}\), and one third of it is the left side. [A1]
(b) With \(f(r) = \dfrac{1}{r(r+1)(r+2)}\) the sum is \(\tfrac13\left[f(1) - f(n+1)\right]\), because the middle terms cancel. [M1]
\(f(1) = \tfrac16\), so the sum is \(\tfrac13\left[\tfrac16 - \dfrac{1}{(n+1)(n+2)(n+3)}\right]\) [A1]
\[= \frac{1}{18} - \frac{1}{3(n+1)(n+2)(n+3)}\] [A1]
(c) As \(n \to \infty\) the last fraction tends to 0, so the sum to infinity is \(\tfrac{1}{18}\). [B1]
:::

:::quiz
? What is \(\displaystyle\sum_{r=1}^{n} 5\)?
- \(5\)
+ \(5n\)
- \(5r\)
- \(5n^2\)
> There are \(n\) terms, each equal to 5, so the sum is \(5n\). Answering 5 treats the constant as a single term, which is the slip made in the Spot the error example.
? What is \(\displaystyle\sum_{r=1}^{n} (2r + 1)\)?
- \(n(n + 1)\)
+ \(n(n + 2)\)
- \((n + 1)^2\)
- \(2n + 1\)
> \(2\sum r + \sum 1 = n(n+1) + n = n(n+2)\). The answer \(n(n+1)\) forgets that \(\sum 1 = n\), and \((n+1)^2\) would be the sum starting at \(r = 0\).
? Which expression gives \(\displaystyle\sum_{r=5}^{20} r^2\)?
- \(\displaystyle\sum_{r=1}^{20} r^2 - \sum_{r=1}^{5} r^2\)
+ \(\displaystyle\sum_{r=1}^{20} r^2 - \sum_{r=1}^{4} r^2\)
- \(\displaystyle\sum_{r=1}^{15} r^2\)
- \(\displaystyle\left(\sum_{r=1}^{20} r - \sum_{r=1}^{4} r\right)^2\)
> The sum starts at \(r = 5\), so remove the terms for \(r = 1\) to 4. Removing up to 5 also throws away the term for \(r = 5\). The sum to 15 has different terms, and the square of a sum is not the sum of the squares.
? What is \(\displaystyle\sum_{r=1}^{10} r^3\)?
- \(385\)
- \(55\)
+ \(3025\)
- \(1000\)
> \(\sum r^3 = \left(\tfrac12 \times 10 \times 11\right)^2 = 55^2 = 3025\). The value 385 is \(\sum r^2\) and 55 is \(\sum r\).
? \(u_r = \dfrac{1}{r} - \dfrac{1}{r+3}\). When you add \(u_1, u_2, \dots, u_n\), how many terms are left after cancelling?
- Two
- Three
+ Six
- It depends on \(n\)
> With a gap of 3 the first three terms of \(\dfrac1r\) and the last three of \(-\dfrac{1}{r+3}\) survive, six in all (for \(n\) at least 3). A gap of \(k\) leaves \(2k\) terms.
? Which is the correct partial fractions form of \(\dfrac{1}{r(r+2)}\)?
+ \(\dfrac12\left(\dfrac1r - \dfrac{1}{r+2}\right)\)
- \(\dfrac1r - \dfrac{1}{r+2}\)
- \(\dfrac12\left(\dfrac1r + \dfrac{1}{r+2}\right)\)
- \(\dfrac1r + \dfrac{1}{r+2}\)
> The bracket \(\dfrac1r - \dfrac{1}{r+2}\) equals \(\dfrac{2}{r(r+2)}\), so the factor \(\tfrac12\) is needed. A plus sign never gives a single fraction like this.
? A series has \(S_n = \tfrac12 n(n+1)\). What happens as \(n \to \infty\)?
- \(S_n \to \tfrac12\)
- \(S_n \to 0\)
+ \(S_n\) grows without bound, so the series diverges
- \(S_n \to 1\)
> The \(n^2\) term makes \(S_n\) grow without limit. The other options pick a coefficient or let a "small" factor decide the limit.
:::

:::checklist What you can now do
- [ ] I can use sigma notation, the rules for sums, and the fact that \(\sum_{r=1}^{n} c = nc\).
- [ ] I can use the standard results for \(\sum r\), \(\sum r^2\) and \(\sum r^3\) to find the sum of a polynomial series, in factorised form.
- [ ] I can find sums that start at \(r = m\), or run from \(n + 1\) to \(2n\), by subtracting two standard sums.
- [ ] I can use partial fractions to write a general term as \(f(r) - f(r + k)\).
- [ ] I can use the method of differences, writing out the first and last terms, to find the sum of a finite series.
- [ ] I can apply the method of differences to factorials, square roots and logarithms, as well as to fractions.
- [ ] I can recognise from \(S_n\) when a series converges, and find the sum to infinity.
- [ ] I can explain why a series diverges, using what \(S_n\) does as \(n \to \infty\).
:::

:::recap
- \(\sum_{r=1}^{n} c = nc\); \(\sum_{r=m}^{n} u_r = \sum_{r=1}^{n} u_r - \sum_{r=1}^{m-1} u_r\); sums split over addition and take out constant multiples.
- MF19 gives \(\sum r = \tfrac12 n(n+1)\), \(\sum r^2 = \tfrac16 n(n+1)(2n+1)\), \(\sum r^3 = \tfrac14 n^2(n+1)^2\).
- Related sums: expand the general term, split it, substitute, take out common factors before expanding, then factorise.
- Method of differences: write \(u_r = f(r) - f(r+k)\); the first \(k\) terms of \(f\) and the last \(k\) terms of \(-f\) survive. Write the first three and the last two lines.
- Partial fractions turn \(\dfrac{1}{r(r+k)}\) into \(\dfrac1k\left(\dfrac1r - \dfrac{1}{r+k}\right)\); remember the factor.
- Other differences: \(r \times r! = (r+1)! - r!\), \(\dfrac{1}{\sqrt r + \sqrt{r+1}} = \sqrt{r+1} - \sqrt r\), \(\ln\dfrac{r+1}{r} = \ln(r+1) - \ln r\).
- A series converges when \(S_n\) tends to a finite limit as \(n \to \infty\); that limit is \(S_\infty\). Terms like \(\dfrac{1}{n+1}\) tend to 0; \(S_n\) growing without bound means divergence.
- Terms tending to 0 is not enough for convergence: decide from \(S_n\).
:::

:::links
- watch: [Method of differences](https://www.examsolutions.net/tutorials/method-differences/) · ExamSolutions · worked examples of telescoping sums with partial fractions
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · the series and method of differences booklets have graded questions with answers
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot the partial sums to see convergence
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions on series, with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Matrices: algebra, determinants and inverses](#math.fm.matrices) introduces the objects that represent transformations and solve systems of equations.
