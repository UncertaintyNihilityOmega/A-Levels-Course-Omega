@chapter math.further
@title Further Mathematics: a guided tour
@level ext
@paper CAIE 9231 · Edexcel IAL Further Pure · UK Further Mathematics A Level
@time 5–7 hours
@summary Further Mathematics is a second A Level for students who love maths. This tour shows what the course contains, who should take it, and gives one small worked example from each major topic: proof by induction, matrices, roots of polynomials, the method of differences, polar coordinates, hyperbolic functions, Maclaurin series, de Moivre's theorem and second-order differential equations.

:::why
If you enjoy the Pure chapters of this course and want more, Further Mathematics is where maths gets bigger. It is the natural choice if you plan to study mathematics, physics, engineering, computer science or economics at a demanding university, and some universities ask for it or value it highly. This chapter is a tour, not a full course: its aim is to let you taste each topic and decide whether the subject is for you.
:::

**Before you start**, it helps to have worked through [Differentiation](#math.p1.diff), [Integration](#math.p1.integ), [Complex numbers](#math.p3.complex), [Series](#math.p1.series) and [Differential equations](#math.p3.diffeq). Nothing here is needed for the other chapters.

:::try Warm-up
Q: Find the modulus and argument of \(1 + i\). (from [Complex numbers](#math.p3.complex))
A: \(|1 + i| = \sqrt{1^2 + 1^2} = \sqrt2\), and the point \((1, 1)\) makes an angle of \(\tfrac\pi4\) with the real axis, so \(\arg(1 + i) = \tfrac\pi4\).
Q: Write \(\dfrac{1}{r(r + 1)}\) as partial fractions. (from [Partial fractions and the binomial series](#math.p3.partial))
A: \(\dfrac{1}{r(r + 1)} = \dfrac{A}{r} + \dfrac{B}{r + 1}\) gives \(1 = A(r + 1) + Br\). Put \(r = 0\): \(A = 1\). Put \(r = -1\): \(B = -1\). So it equals \(\dfrac1r - \dfrac1{r + 1}\).
Q: Find the sum of the first \(20\) terms of the arithmetic series \(3 + 7 + 11 + \ldots\). (from [Series](#math.p1.series))
A: \(S_{20} = \dfrac{20}{2}\big[2(3) + 19(4)\big]\), which is \(10 \times 82 = 820\).
:::

## What Further Mathematics is

Cambridge International **Further Mathematics 9231** is a separate qualification from 9709 Mathematics. It has four papers.

| Paper | Name | Duration | Marks |
|---|---|---|---|
| 1 | Further Pure Mathematics 1 (FP1) | 2 h | 75 |
| 2 | Further Pure Mathematics 2 (FP2) | 2 h | 75 |
| 3 | Further Mechanics (FM) | 1 h 30 min | 50 |
| 4 | Further Probability & Statistics (FS) | 1 h 30 min | 50 |

The AS Further Mathematics qualification is **Paper 1 plus Paper 3, or Paper 1 plus Paper 4**. The formula list MF19 is shared with 9709, which is why it holds some formulae that 9709 itself does not need.

- **Further Pure** (Papers 1 and 2) covers the topics in this tour. They continue the algebra, calculus and complex numbers of 9709 Pure at a more abstract level.
- **Further Mechanics** and **Further Probability & Statistics** extend the ideas in [Mechanics](#math.m.forces) and [Probability and statistics](#math.s1.data).

:::tip Who should take Further Mathematics?
Take it if you enjoy proving things and solving problems that have no template, if you are strong in A Level Mathematics, and if your target degree (or your ambition) is in a mathematical subject. It adds a heavy workload, so check with your school how it is timetabled and how it is combined with your other subjects.
:::

:::board
- **Edexcel IAL**: Further Mathematics has its own Further Pure units, plus Further Mechanics and Further Statistics units. The names differ from CAIE, but many topics overlap.
- **UK A Level (AQA, Edexcel, OCR)**: Further Mathematics is a separate A Level with compulsory pure content and optional applied papers. Poisson, complex numbers, matrices and the other topics in this tour belong to it, not to the single Maths A Level.
:::

## Proof by induction

:::def Proof by induction
A method of proving that a statement holds for every positive integer \(n\): show that it is true for \(n = 1\), and show that whenever it is true for \(n = k\) it must also be true for \(n = k + 1\).
:::

Induction is like a line of dominoes: the first falls, and each one knocks over the next. The other proof methods (deduction, exhaustion, counter-example and contradiction) are in [Proof: how mathematicians know](#math.proof).

:::steps
1. **Basis**: show the statement is true for \(n = 1\).
2. **Assumption**: assume it is true for \(n = k\).
3. **Step**: show that it is then true for \(n = k + 1\).
4. **Conclusion**: so it is true for all positive integers \(n\) by induction.
:::

:::eg Prove by induction that \(1 + 3 + 5 + \dots + (2n - 1) = n^2\).
**Basis**: \(n = 1\): the left side is 1 and the right side is \(1^2 = 1\). ✓
**Assumption**: suppose \(1 + 3 + \dots + (2k - 1) = k^2\).
**Step**: for \(n = k + 1\), add the next term \((2k + 1)\):
\[k^2 + (2k + 1) = (k + 1)^2\]
This is the statement for \(n = k + 1\). So if it is true for \(k\), it is true for \(k + 1\); it is true for \(n = 1\), so it is true for all positive integers \(n\).
:::

:::eg (Exam style) Prove by induction that \(\displaystyle\sum_{r=1}^{n} r^2 = \frac{n(n+1)(2n+1)}{6}\) for all positive integers \(n\). [5 marks]
For \(n = 1\): the left side is 1, and the right side is \(\dfrac{1 \times 2 \times 3}{6} = 1\). ✓ [B1]
Assume it is true for \(n = k\): \(\displaystyle\sum_{r=1}^{k} r^2 = \dfrac{k(k+1)(2k+1)}{6}\). [B1]
For \(n = k + 1\), add the next term:
\[\frac{k(k+1)(2k+1)}{6} + (k+1)^2 = \frac{(k+1)\left[k(2k+1) + 6(k+1)\right]}{6}\] [M1]
\[= \frac{(k+1)(2k^2 + 7k + 6)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}\] [A1]
This is the formula with \(n = k + 1\). It is true for \(n = 1\), and true for \(k + 1\) whenever it is true for \(k\), so it is true for all positive integers \(n\). [A1]
:::

## Matrices

:::def Matrix
A rectangular array of numbers, written in brackets. A matrix with 2 rows and 2 columns is a \(2 \times 2\) matrix. Matrices represent systems of equations and transformations of the plane.
:::

For \(\mathbf{A} = \begin{pmatrix}a & b\\ c & d\end{pmatrix}\), the **determinant** is \(\det\mathbf{A} = ad - bc\), and, when \(\det\mathbf{A} \neq 0\), the **inverse** is
\[\mathbf{A}^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d & -b\\ -c & a\end{pmatrix}\]
The determinant is also the factor by which the transformation changes area.

:::eg Let \(\mathbf{A} = \begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}\). Find \(\mathbf{A}^{-1}\) and use it to solve \(2x + y = 4\), \(5x + 3y = 11\).
\(\det\mathbf{A} = 2 \times 3 - 1 \times 5 = 1\), so \(\mathbf{A}^{-1} = \begin{pmatrix}3 & -1\\ -5 & 2\end{pmatrix}\).
The equations are \(\mathbf{A}\begin{pmatrix}x\\ y\end{pmatrix} = \begin{pmatrix}4\\ 11\end{pmatrix}\), so
\[\begin{pmatrix}x\\ y\end{pmatrix} = \mathbf{A}^{-1}\begin{pmatrix}4\\ 11\end{pmatrix} = \begin{pmatrix}12 - 11\\ -20 + 22\end{pmatrix} = \begin{pmatrix}1\\ 2\end{pmatrix}\]
Check: \(2(1) + 2 = 4\) and \(5(1) + 3(2) = 11\). ✓
:::

## Roots of polynomial equations

If \(\alpha, \beta, \gamma\) are the roots of \(ax^3 + bx^2 + cx + d = 0\), then
\[\alpha + \beta + \gamma = -\frac{b}{a} \qquad \alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a} \qquad \alpha\beta\gamma = -\frac{d}{a}\]
You can find expressions in the roots without solving the equation.

:::proof Where the sum and product of the roots come from
If \(\alpha\), \(\beta\) and \(\gamma\) are the roots of \(ax^3 + bx^2 + cx + d = 0\), the cubic factorises as \(a(x - \alpha)(x - \beta)(x - \gamma)\) (the factor theorem, three times).

Expand the brackets, two at a time:
\[(x - \alpha)(x - \beta) = x^2 - (\alpha + \beta)x + \alpha\beta\]
Multiply by \((x - \gamma)\) and collect terms:
\[x^3 - (\alpha + \beta + \gamma)x^2 + (\alpha\beta + \beta\gamma + \gamma\alpha)x - \alpha\beta\gamma\]
So \(ax^3 + bx^2 + cx + d\) equals \(a\) times this. Compare coefficients with \(ax^3 + bx^2 + cx + d\), dividing by \(a\):
\[\frac{b}{a} = -(\alpha + \beta + \gamma) \qquad \frac{c}{a} = \alpha\beta + \beta\gamma + \gamma\alpha \qquad \frac{d}{a} = -\alpha\beta\gamma\]
Rearranged, these are the three results above. The same idea gives the sum \(-\dfrac{b}{a}\) and product \(\dfrac{c}{a}\) of the roots of a quadratic.
:::

:::eg The roots of \(x^3 - 5x^2 + 8x - 3 = 0\) are \(\alpha, \beta, \gamma\). Find \(\alpha^2 + \beta^2 + \gamma^2\), and the cubic with roots \(2\alpha, 2\beta, 2\gamma\).
\(\alpha + \beta + \gamma = 5\), \(\alpha\beta + \beta\gamma + \gamma\alpha = 8\), \(\alpha\beta\gamma = 3\).
\[\alpha^2 + \beta^2 + \gamma^2 = (\alpha + \beta + \gamma)^2 - 2(\alpha\beta + \beta\gamma + \gamma\alpha) = 25 - 16 = 9\]
For the new roots put \(y = 2x\), so \(x = \tfrac y2\):
\[\left(\tfrac y2\right)^3 - 5\left(\tfrac y2\right)^2 + 8\left(\tfrac y2\right) - 3 = 0 \quad\Rightarrow\quad y^3 - 10y^2 + 32y - 24 = 0\]
:::

## Series and the method of differences

Some sums collapse when each term is split into two parts that cancel with their neighbours. This is the **method of differences**, a telescoping trick.

:::eg Find \(\displaystyle\sum_{r=1}^{n}\frac{1}{r(r+1)}\) and its limit as \(n \to \infty\).
Split with partial fractions: \(\dfrac{1}{r(r+1)} = \dfrac1r - \dfrac1{r+1}\). Then
\[\left(1 - \tfrac12\right) + \left(\tfrac12 - \tfrac13\right) + \dots + \left(\tfrac1n - \tfrac{1}{n+1}\right) = 1 - \frac{1}{n+1}\]
All the middle terms cancel. As \(n \to \infty\), the sum tends to 1. Check with \(n = 4\): \(\tfrac12 + \tfrac16 + \tfrac1{12} + \tfrac1{20} = 0.8 = 1 - \tfrac15\). ✓
:::

## Polar coordinates

A point can be given by its distance \(r\) from the origin and the angle \(\theta\) from the positive \(x\)-axis. A curve \(r = f(\theta)\) can be simple in polar form and awkward in \(x\)–\(y\) form. The area enclosed is
\[A = \frac12\int_{\alpha}^{\beta} r^2\,d\theta\]

:::eg Find the area enclosed by the cardioid \(r = 2(1 + \cos\theta)\), \(0 \le \theta \le 2\pi\).
\[A = \frac12\int_0^{2\pi} 4(1 + \cos\theta)^2\,d\theta = 2\int_0^{2\pi}\left(1 + 2\cos\theta + \tfrac12 + \tfrac12\cos 2\theta\right)d\theta\]
using \(\cos^2\theta = \tfrac12(1 + \cos 2\theta)\). The \(\cos\theta\) and \(\cos 2\theta\) terms integrate to 0 over a full period, leaving
\[A = 2\int_0^{2\pi}\tfrac32\,d\theta = 2 \times \tfrac32 \times 2\pi = 6\pi\]
:::

## Hyperbolic functions

\[\sinh x = \frac{e^x - e^{-x}}{2} \qquad \cosh x = \frac{e^x + e^{-x}}{2}\]
They behave like \(\sin\) and \(\cos\) but with an important sign change: \(\cosh^2 x - \sinh^2 x = 1\), \(\dfrac{d}{dx}\sinh x = \cosh x\) and \(\dfrac{d}{dx}\cosh x = \sinh x\). A hanging chain takes the shape of a cosh curve.

:::proof Why \(\cosh^2 x - \sinh^2 x = 1\)
Use the definitions \(\cosh x = \dfrac{e^x + e^{-x}}{2}\) and \(\sinh x = \dfrac{e^x - e^{-x}}{2}\).

Square each, using \((e^x)(e^{-x}) = e^0 = 1\):
\[\cosh^2 x = \frac{e^{2x} + 2 + e^{-2x}}{4} \qquad \sinh^2 x = \frac{e^{2x} - 2 + e^{-2x}}{4}\]
Subtract. The \(e^{2x}\) and \(e^{-2x}\) terms cancel:
\[\cosh^2 x - \sinh^2 x = \frac{2 - (-2)}{4} = 1\]
Compare \(\cos^2 x + \sin^2 x = 1\): the sign is different because \(\cosh\) and \(\sinh\) come from the hyperbola \(X^2 - Y^2 = 1\), while \(\cos\) and \(\sin\) come from the circle \(X^2 + Y^2 = 1\).
:::

:::eg Solve \(\sinh x = \dfrac34\).
Let \(\sinh x = \tfrac34\). Then \(\cosh x = \sqrt{1 + \sinh^2 x} = \sqrt{1 + \tfrac9{16}} = \tfrac54\), and \(e^x = \sinh x + \cosh x = \tfrac34 + \tfrac54 = 2\), so \(x = \ln 2 = 0.693\).
:::

## Maclaurin series

Many functions can be written as an infinite polynomial. For a function \(f(x)\) with derivatives at \(0\),
\[f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots\]
The more terms you keep, the better the approximation near \(x = 0\).

:::eg Find the first three non-zero terms of the Maclaurin series of \(\ln(1 + x)\), and use them to estimate \(\ln 1.1\).
\(f(x) = \ln(1 + x)\), \(f(0) = 0\). \(f'(x) = \dfrac{1}{1 + x}\), \(f'(0) = 1\). \(f''(x) = -\dfrac{1}{(1 + x)^2}\), \(f''(0) = -1\). \(f'''(x) = \dfrac{2}{(1 + x)^3}\), \(f'''(0) = 2\). So
\[\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots\]
With \(x = 0.1\): \(0.1 - 0.005 + 0.000333 = 0.0953\). The calculator value of \(\ln 1.1\) is \(0.0953102\), so three terms are already accurate to 4 decimal places.
:::

## Complex numbers: de Moivre's theorem

For any integer \(n\):
\[(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta\]
Powers and roots of complex numbers become simple in modulus–argument form.

:::eg Find \((1 + i)^8\).
\(|1 + i| = \sqrt2\) and \(\arg(1 + i) = \tfrac\pi4\), so \(1 + i = \sqrt2\left(\cos\tfrac\pi4 + i\sin\tfrac\pi4\right)\).
\[(1 + i)^8 = (\sqrt2)^8\left(\cos 2\pi + i\sin 2\pi\right) = 16\]
:::

## Second-order differential equations

An equation of the form \(a\dfrac{d^2y}{dx^2} + b\dfrac{dy}{dx} + cy = 0\) has solutions found from the **auxiliary equation** \(am^2 + bm + c = 0\). Two real roots \(m_1, m_2\) give \(y = Ae^{m_1x} + Be^{m_2x}\). Complex roots \(m = p \pm qi\) give \(y = e^{px}(A\cos qx + B\sin qx)\), the shape of oscillations such as springs and circuits.

:::eg Solve \(y'' - 5y' + 6y = 0\).
The auxiliary equation is \(m^2 - 5m + 6 = 0\), so \((m - 2)(m - 3) = 0\) and \(m = 2\) or \(m = 3\). The general solution is
\[y = Ae^{2x} + Be^{3x}\]
where \(A\) and \(B\) are constants fixed by two initial conditions.
:::

:::exam Moving from 9709 to 9231
Further Mathematics rewards the habits that A Level Mathematics already trains: write every step, state your method, check answers by substitution, and learn the proofs. A grade in A Level Mathematics is a good indicator that the extra pace is manageable.
:::

:::eg Spot the error: prove by induction that \(4^n - 1\) is divisible by \(3\) for all positive integers \(n\).
The question is worth 5 marks. A student wrote this answer.

Line 1: For \(n = 1\), \(4^1 - 1 = 3\), which is divisible by \(3\). [B1]
Line 2: Assume that \(4^k - 1\) is divisible by \(3\). [B1]
Line 3: Then \(4^{k+1} - 1 = 4 \cdot 4^k - 1 = 4(4^k - 1) - 1\). [M1]
Line 4: \(4(4^k - 1)\) is divisible by \(3\), so \(4^{k+1} - 1\) is divisible by \(3\). [A0] [A0]

Lines 1 to 3 start well: a correct basis, a correct assumption, and a plan to pull out the assumed factor \(4^k - 1\). **Line 3 contains an arithmetic slip.** \(4(4^k - 1) = 4 \cdot 4^k - 4\), so to get back to \(4 \cdot 4^k - 1\) you must **add 3**, not subtract 1. Line 4 then claims the result without noticing that the leftover \(-1\) is not a multiple of \(3\): the argument as written proves nothing, so both accuracy marks are lost. The student scores 3 out of 5.

Correct step: \(4^{k+1} - 1 = 4 \cdot 4^k - 1 = 4(4^k - 1) + 3\). [A1] The first part is divisible by \(3\) by the assumption, and \(3\) is divisible by \(3\), so \(4^{k+1} - 1\) is divisible by \(3\). It is true for \(n = 1\), and true for \(k + 1\) whenever it is true for \(k\), so it is true for all positive integers \(n\) by induction. [A1]

Check: \(k = 3\) gives \(4^4 - 1 = 255\) and \(4(4^3 - 1) + 3 = 4(63) + 3 = 255\). ✓
:::

:::try Test yourself on the tour
Q: Complete the inductive step to prove \(\displaystyle\sum_{r=1}^{n} r = \frac{n(n+1)}{2}\), given that it is true for \(n = k\).
A: For \(n = k + 1\):
\[\dfrac{k(k+1)}{2} + (k + 1) = (k + 1)\left(\dfrac{k}{2} + 1\right) = \dfrac{(k+1)(k+2)}{2}\]
This is the formula with \(n = k + 1\).
Q: Find the determinant and the inverse of \(\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}\).
A: \(\det = 4 - 6 = -2\). Inverse:
\[\dfrac{1}{-2}\begin{pmatrix}4 & -2\\ -3 & 1\end{pmatrix} = \begin{pmatrix}-2 & 1\\ 1.5 & -0.5\end{pmatrix}\]
Q: The roots of \(x^3 - 6x^2 + 11x - 6 = 0\) are \(\alpha, \beta, \gamma\). Find \(\alpha^2 + \beta^2 + \gamma^2\) and check against the actual roots 1, 2, 3.
A: \(\alpha + \beta + \gamma = 6\) and \(\alpha\beta + \beta\gamma + \gamma\alpha = 11\), so the sum of squares is \(36 - 22 = 14\). Check: \(1 + 4 + 9 = 14\). ✓
Q: Use the method of differences to find \(\displaystyle\sum_{r=1}^{9}\frac{1}{r(r+1)}\).
A: The sum is \(1 - \dfrac{1}{n+1}\) with \(n = 9\), which is \(1 - \dfrac1{10} = \dfrac{9}{10}\).
Q: Evaluate \(\sinh(\ln 3)\) using the definition.
A: \(\sinh(\ln 3) = \dfrac{e^{\ln 3} - e^{-\ln 3}}{2} = \dfrac{3 - \tfrac13}{2} = \dfrac43\).
Q: Use the Maclaurin series \(e^x \approx 1 + x + \dfrac{x^2}{2} + \dfrac{x^3}{6}\) to estimate \(e^{0.2}\).
A: \(1 + 0.2 + 0.02 + 0.001333 = 1.2213\). The calculator value is \(1.2214\).
Q: Find \((\sqrt3 + i)^6\).
A: \(|\sqrt3 + i| = 2\) and the argument is \(\tfrac\pi6\), so the result is \(2^6(\cos\pi + i\sin\pi) = -64\).
Q: Solve \(y'' + 4y = 0\).
A: The auxiliary equation \(m^2 + 4 = 0\) gives \(m = \pm 2i\), so \(y = A\cos 2x + B\sin 2x\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Find the exact value of \(\cosh(\ln 2)\).
A: \(\cosh(\ln 2) = \dfrac{e^{\ln 2} + e^{-\ln 2}}{2}\) [M1] \(= \dfrac{2 + \tfrac12}{2} = \dfrac54\). [A1]
Q: [4 marks] ★ Let \(\mathbf{A} = \begin{pmatrix}3 & 2\\ 4 & 3\end{pmatrix}\). Find \(\mathbf{A}^{-1}\) and use it to solve \(3x + 2y = 5\) and \(4x + 3y = 8\).
A: \(\det\mathbf{A} = 3(3) - 2(4) = 1\), so [M1] \(\mathbf{A}^{-1} = \begin{pmatrix}3 & -2\\ -4 & 3\end{pmatrix}\). [A1] Then \(\begin{pmatrix}x\\ y\end{pmatrix} = \begin{pmatrix}3 & -2\\ -4 & 3\end{pmatrix}\begin{pmatrix}5\\ 8\end{pmatrix}\) [M1] \(= \begin{pmatrix}-1\\ 4\end{pmatrix}\), so \(x = -1\) and \(y = 4\). [A1]
Q: [5 marks] ★★ Prove by induction that \(\displaystyle\sum_{r=1}^{n} r(r + 1) = \frac{n(n + 1)(n + 2)}{3}\) for all positive integers \(n\).
A: For \(n = 1\), the left side is \(1 \times 2 = 2\) and the right side is \(\dfrac{1 \times 2 \times 3}{3} = 2\). ✓ [B1] Assume it is true for \(n = k\): \(\displaystyle\sum_{r=1}^{k} r(r + 1) = \dfrac{k(k + 1)(k + 2)}{3}\). [B1] For \(n = k + 1\) add the next term: \(\dfrac{k(k + 1)(k + 2)}{3} + (k + 1)(k + 2)\) [M1] \(= \dfrac{(k + 1)(k + 2)(k + 3)}{3}\), [A1] which is the formula with \(n = k + 1\). It is true for \(n = 1\) and true for \(k + 1\) whenever it is true for \(k\), so it is true for all positive integers \(n\). [A1]
Q: [4 marks] ★★ The roots of \(x^3 - 4x^2 + x + 6 = 0\) are \(\alpha\), \(\beta\) and \(\gamma\). Without solving the equation, find (a) \(\alpha^2 + \beta^2 + \gamma^2\), (b) \(\dfrac1\alpha + \dfrac1\beta + \dfrac1\gamma\).
A: \(\alpha + \beta + \gamma = 4\), \(\alpha\beta + \beta\gamma + \gamma\alpha = 1\) and \(\alpha\beta\gamma = -6\). (a) \(\alpha^2 + \beta^2 + \gamma^2 = 4^2 - 2(1)\) [M1] \(= 14\). [A1] (b) \(\dfrac1\alpha + \dfrac1\beta + \dfrac1\gamma = \dfrac{\alpha\beta + \beta\gamma + \gamma\alpha}{\alpha\beta\gamma}\) [M1] \(= -\dfrac16\). [A1] Check with the actual roots \(2, 3, -1\): \(4 + 9 + 1 = 14\) and \(\tfrac12 + \tfrac13 - 1 = -\tfrac16\). ✓
Q: [5 marks] ★★ (a) Express \(\dfrac{1}{(2r - 1)(2r + 1)}\) in partial fractions. (b) Use the method of differences to show that \(\displaystyle\sum_{r=1}^{n}\frac{1}{(2r - 1)(2r + 1)} = \frac{n}{2n + 1}\). (c) Find the sum to infinity.
A: (a)
\[\dfrac{1}{(2r - 1)(2r + 1)} = \dfrac12\left(\dfrac{1}{2r - 1} - \dfrac{1}{2r + 1}\right)\] [M1 A1]
(b) Writing out the terms,
\[\tfrac12\left(1 - \tfrac13\right) + \tfrac12\left(\tfrac13 - \tfrac15\right) + \dots + \tfrac12\left(\tfrac{1}{2n - 1} - \tfrac{1}{2n + 1}\right)\]
everything cancels except the first and last parts. [M1] The sum is \(\tfrac12\left(1 - \dfrac{1}{2n + 1}\right) = \dfrac{n}{2n + 1}\). [A1] (c) As \(n \to \infty\), \(\dfrac{n}{2n + 1} \to \dfrac12\). [B1]
Q: [4 marks] ★★ Find \((1 - i)^6\).
A: \(|1 - i| = \sqrt2\) and \(\arg(1 - i) = -\tfrac\pi4\), so
\[1 - i = \sqrt2\left(\cos\left(-\tfrac\pi4\right) + i\sin\left(-\tfrac\pi4\right)\right)\] [M1 A1]
By de Moivre,
\[(1 - i)^6 = (\sqrt2)^6\left(\cos\left(-\tfrac{3\pi}{2}\right) + i\sin\left(-\tfrac{3\pi}{2}\right)\right)\] [M1]
This is \(8(0 + i) = 8i\). [A1] Check: \((1 - i)^2 = -2i\), and \((-2i)^3 = -8i^3 = 8i\). ✓
Q: [7 marks] (#math.p3.diffeq) ★★★ Solve \(\dfrac{d^2y}{dx^2} + 4\dfrac{dy}{dx} + 13y = 0\), given that \(y = 2\) and \(\dfrac{dy}{dx} = -1\) when \(x = 0\).
H: Write the auxiliary equation \(m^2 + 4m + 13 = 0\). Are its roots real?
H: Complex roots \(p \pm qi\) give \(y = e^{px}(A\cos qx + B\sin qx)\).
H: Use \(y(0) = 2\) first to find \(A\). Then differentiate the product to use the second condition.
A: The auxiliary equation is \(m^2 + 4m + 13 = 0\). [M1] Then \(m = \dfrac{-4 \pm \sqrt{16 - 52}}{2} = -2 \pm 3i\). [A1] So \(y = e^{-2x}(A\cos 3x + B\sin 3x)\). [A1] When \(x = 0\), \(y = A = 2\). [B1] Differentiating (product rule):
\[\dfrac{dy}{dx} = e^{-2x}\big[-2(A\cos 3x + B\sin 3x) - 3A\sin 3x + 3B\cos 3x\big]\] [M1] At \(x = 0\): \(-2A + 3B = -1\), so \(-4 + 3B = -1\) and \(B = 1\). [A1] The solution is \(y = e^{-2x}(2\cos 3x + \sin 3x)\). [A1]
Q: [7 marks] (#math.p3.diff) ★★★ (a) Find the first three non-zero terms of the Maclaurin series of \(e^x\sin x\). (b) Use your series to estimate \(\displaystyle\int_0^{0.2} e^x\sin x\,dx\), giving your answer to 3 significant figures.
H: Use the product rule to find the first three derivatives of \(f(x) = e^x\sin x\), then evaluate each at \(x = 0\).
H: In the Maclaurin series the coefficient of \(x^n\) is \(\dfrac{f^{(n)}(0)}{n!}\), starting with \(f(0)\).
A: (a) \(f = e^x\sin x\), so \(f(0) = 0\). \(f' = e^x(\sin x + \cos x)\), so \(f'(0) = 1\). [M1 A1] \(f'' = 2e^x\cos x\), so \(f''(0) = 2\). \(f''' = 2e^x(\cos x - \sin x)\), so \(f'''(0) = 2\). [M1 A1] The series is \(x + \dfrac{2}{2}x^2 + \dfrac{2}{6}x^3 = x + x^2 + \dfrac{x^3}{3} + \dots\) [A1] (b)
\[\int_0^{0.2}\left(x + x^2 + \tfrac{x^3}{3}\right)dx = \left[\tfrac{x^2}{2} + \tfrac{x^3}{3} + \tfrac{x^4}{12}\right]_0^{0.2}\] [M1]
\[= 0.02 + 0.002667 + 0.000133 = 0.0228\] [A1] The exact value is \(0.02280\ldots\), so the estimate is accurate to 3 significant figures.
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Prove by induction that \(n^3 + 2n\) is divisible by \(3\) for every positive integer \(n\).
H: In the step, expand \((k + 1)^3 + 2(k + 1)\) and look for the expression \(k^3 + 2k\) inside it.
H: What is left over should be a multiple of 3.
A: For \(n = 1\): \(1 + 2 = 3\), which is divisible by \(3\). [B1] Assume that \(k^3 + 2k\) is divisible by \(3\). [B1] Then
\[\begin{aligned} (k + 1)^3 + 2(k + 1) &= k^3 + 3k^2 + 3k + 1 + 2k + 2 \\ &= (k^3 + 2k) + 3(k^2 + k + 1) \end{aligned}\] [M1 A1] The first bracket is divisible by \(3\) by the assumption and the second term is a multiple of \(3\), so the sum is divisible by \(3\). It is true for \(n = 1\) and true for \(k + 1\) whenever it is true for \(k\), so it is true for all positive integers \(n\). [A1]
Q: [4 marks] ★★★ The curve \(r = \sin 2\theta\) for \(0 \le \theta \le \dfrac\pi2\) is one petal of a four-petal flower. Find the exact area of that petal.
H: Use the polar area formula \(A = \tfrac12\int r^2\,d\theta\) with the given limits.
H: Write \(\sin^2 2\theta\) using the double-angle identity \(\cos 4\theta = 1 - 2\sin^2 2\theta\).
A: \(A = \tfrac12\int_0^{\pi/2}\sin^2 2\theta\,d\theta\). [M1] Since \(\sin^2 2\theta = \dfrac{1 - \cos 4\theta}{2}\), [M1]
\[A = \tfrac14\int_0^{\pi/2}(1 - \cos 4\theta)\,d\theta = \tfrac14\left[\theta - \dfrac{\sin 4\theta}{4}\right]_0^{\pi/2}\] [A1] At \(\theta = \tfrac\pi2\), \(\sin 2\pi = 0\), so \(A = \tfrac14\cdot\tfrac\pi2 = \dfrac\pi8\). [A1] Check: four petals have total area \(4 \times \dfrac\pi8 = \dfrac\pi2\), which is half the area \(\pi\) of the unit circle \(r = 1\). The flower lies inside that circle, so this is plausible.
:::

:::quiz Check your understanding
? Which pair of papers forms the AS Further Mathematics qualification (9231)?
- Paper 3 plus Paper 4
- Paper 2 plus Paper 4
+ Paper 1 plus Paper 3, or Paper 1 plus Paper 4
- Paper 1 plus Paper 2
> The AS qualification is Paper 1 with either Paper 3 (Further Mechanics) or Paper 4 (Further Probability and Statistics).
? In proof by induction, what must you show after assuming the result for \(n = k\)?
- that it is true for \(n = k - 1\)
+ that it is true for \(n = k + 1\)
- that it is true for \(n = 2k\)
- that \(k\) is positive
> The inductive step passes from \(k\) to \(k + 1\), like the domino knocking over the next one.
? Which identity is correct for hyperbolic functions?
- \(\cosh^2 x + \sinh^2 x = 1\)
+ \(\cosh^2 x - \sinh^2 x = 1\)
- \(\cosh^2 x - \sinh^2 x = -1\)
- \(\cosh x + \sinh x = 1\)
> The sign differs from the circular identity \(\cos^2 + \sin^2 = 1\). Check with \(x = 0\): \(\cosh 0 = 1\), \(\sinh 0 = 0\).
? For a \(2 \times 2\) matrix, what does the determinant tell you about the transformation?
- the angle of rotation
+ the factor by which areas change
- the direction of the stretch
- the length of the diagonal
> The determinant is the area scale factor. A zero determinant means the matrix has no inverse.
? A student proves the inductive step \(n = k \Rightarrow n = k + 1\) for a statement but never checks \(n = 1\). What has been proved?
- the statement is true for every positive integer
- the statement is true for \(n = 1\) only
+ nothing: the dominoes are lined up, but the first one has not been pushed
- the statement is false
> Without the basis case, the step only says "if it is true for one value, it is true for the next". Nothing says it is true for any value at all. For example, "\(n = n + 1\)" passes the step (add 1 to both sides) but is never true.
? The roots of \(x^3 - 2x^2 + 3x - 4 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). What is \(\alpha\beta\gamma\)?
- \(-4\)
+ \(4\)
- \(2\)
- \(3\)
> The product of the roots is \(-\dfrac{d}{a} = -\dfrac{-4}{1} = 4\). The option \(-4\) forgets the minus sign in the formula, \(2\) is the sum of the roots, and \(3\) is the sum of the products in pairs.
:::

:::checklist What you can now do
- [ ] I can say what the four 9231 papers are and who Further Mathematics suits.
- [ ] I can write a proof by induction with a basis, an assumption, a step and a conclusion.
- [ ] I can find the determinant and inverse of a 2 × 2 matrix and use them to solve equations.
- [ ] I can use the sum and product of the roots of a polynomial to find other expressions in the roots.
- [ ] I can sum a series with the method of differences and say what it tends to.
- [ ] I can find the area enclosed by a polar curve.
- [ ] I can work with sinh and cosh from their definitions and use cosh² x − sinh² x = 1.
- [ ] I can find a Maclaurin series from derivatives and use it to approximate a value or an integral.
- [ ] I can use de Moivre's theorem to find a power of a complex number.
- [ ] I can solve a second-order differential equation using the auxiliary equation, including initial conditions.
:::

:::recap
- 9231 has four papers: FP1 and FP2 (2 h, 75 marks each), FM and FS (1 h 30, 50 marks each). AS is Paper 1 with Paper 3 or Paper 4.
- Induction: basis, assume \(n = k\), show \(n = k + 1\), conclude.
- Matrices: \(\det = ad - bc\); the inverse needs \(\det \neq 0\); the determinant is the area scale factor.
- Roots of a cubic: sum \(= -b/a\), pair-sum \(= c/a\), product \(= -d/a\).
- Method of differences: split terms so the sum telescopes.
- Polar area \(\tfrac12\int r^2\,d\theta\); hyperbolic functions follow \(\cosh^2 - \sinh^2 = 1\); Maclaurin series approximate a function by a polynomial; de Moivre handles powers; second-order DEs use the auxiliary equation.
:::

:::links
- watch: [e^(iπ) in 3.14 minutes, using dynamics](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · a taste of complex exponentials
- practise: [NRICH for students](https://nrich.maths.org/students) · NRICH · problems for students who love maths
- explore: [Divisibility & Induction](https://undergroundmathematics.org/divisibility-and-induction) · Underground Mathematics · proof by induction, explored
- explore: [Hyperbolic Functions](https://undergroundmathematics.org/hyperbolic-functions) · Underground Mathematics · a first look at cosh and sinh
- explore: [Power Series](https://undergroundmathematics.org/power-series) · Underground Mathematics · towards Maclaurin series
- papers: [9231 Further Pure 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · see what Further Maths questions look like [unofficial]

Links checked 3 October 2026.
:::
Next: [Mathematics: the course map](#math.overview) to plan your path.
