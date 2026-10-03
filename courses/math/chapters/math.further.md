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

Induction is like a line of dominoes: the first falls, and each one knocks over the next.

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

:::try Test yourself on the tour
Q: Complete the inductive step to prove \(\displaystyle\sum_{r=1}^{n} r = \frac{n(n+1)}{2}\), given that it is true for \(n = k\).
A: For \(n = k + 1\): \(\dfrac{k(k+1)}{2} + (k + 1) = (k + 1)\left(\dfrac{k}{2} + 1\right) = \dfrac{(k+1)(k+2)}{2}\), which is the formula with \(n = k + 1\).
Q: Find the determinant and the inverse of \(\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}\).
A: \(\det = 4 - 6 = -2\). Inverse \(= \dfrac{1}{-2}\begin{pmatrix}4 & -2\\ -3 & 1\end{pmatrix} = \begin{pmatrix}-2 & 1\\ 1.5 & -0.5\end{pmatrix}\).
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
:::

:::recap
- 9231 has four papers: FP1 and FP2 (2 h, 75 marks each), FM and FS (1 h 30, 50 marks each). AS is Paper 1 with Paper 3 or Paper 4.
- Induction: basis, assume \(n = k\), show \(n = k + 1\), conclude.
- Matrices: \(\det = ad - bc\); the inverse needs \(\det \neq 0\); the determinant is the area scale factor.
- Roots of a cubic: sum \(= -b/a\), pair-sum \(= c/a\), product \(= -d/a\).
- Method of differences: split terms so the sum telescopes.
- Polar area \(\tfrac12\int r^2\,d\theta\); hyperbolic functions follow \(\cosh^2 - \sinh^2 = 1\); Maclaurin series approximate a function by a polynomial; de Moivre handles powers; second-order DEs use the auxiliary equation.
:::

:::note Learn more online
- **Watch:** [e^(iπ) in 3.14 minutes, using dynamics](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · a taste of complex exponentials
- **Practise:** [NRICH for students](https://nrich.maths.org/students) · NRICH · problems for students who love maths
- **Explore:** [Divisibility & Induction](https://undergroundmathematics.org/divisibility-and-induction) · Underground Mathematics · proof by induction, explored
- **Explore:** [Hyperbolic Functions](https://undergroundmathematics.org/hyperbolic-functions) · Underground Mathematics · a first look at cosh and sinh
- **Explore:** [Power Series](https://undergroundmathematics.org/power-series) · Underground Mathematics · towards Maclaurin series
- **Papers:** [9231 Further Pure 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · see what Further Maths questions look like *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Mathematics: the course map](#math.overview) to plan your path.
