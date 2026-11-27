@chapter math.fm.mixed.pure
@title Mixed practice: Further Pure
@level guide
@paper CAIE 9231 Papers 1 and 2
@time 4–6 hours
@summary Thirty-one short questions that mix every topic of Further Pure Mathematics 1 and 2: series, roots, matrices and transformations, induction, rational functions and graphs, polar curves, vectors and planes, then hyperbolic functions, Maclaurin series, integration, reduction formulae, arc length, de Moivre, systems, eigenvalues and differential equations. The first two blocks are Paper 1 only, the last two mix both papers, and the order goes from ★ to ★★★. Each answer is a mark scheme, and each question names the chapter to revise.

:::why
In the exam you are not told which chapter a question comes from. Practising one topic at a time trains the method but not the first step, which is recognising what the question needs: a "show that" with a method of differences, a plane and a skew line, a differential equation that wants an integrating factor. This page is mixed on purpose. No two neighbouring questions come from the same chapter, so each one starts with the real task: working out which tool to pick up.
:::

:::tip How to use this page
Do the questions in order, a few at a time, on paper, and mark yourself with the scheme. The page has four blocks: Further Pure 1 warm-up, Further Pure 1 exam standard, Mixed Further Pure 1 and 2, and Stretch. **Each block numbers its questions from 1**, so this page refers to a question by its block and number (for example "exam standard 4" is question 4 of the Further Pure 1 exam standard block). The first two blocks are Further Pure 1 only (the Paper 1 content, which Paper 2 also assumes); the last two mix Paper 1 and Paper 2 content. ★ questions are one idea (2 to 4 marks), ★★ questions are one part of an exam question, ★★★ questions need two or more ideas in one answer. When you lose a mark, follow the chapter link in brackets and redo one worked example there before moving on. MF19 is available for every question: it gives the sums of \(r\), \(r^2\) and \(r^3\), the Maclaurin series, the hyperbolic identities and the standard derivatives and integrals, but not reduction formulae, the arc length and surface area formulae, de Moivre's theorem, the vector product or the matrix methods, which you must know. Give non-exact answers to 3 significant figures and angles in degrees to 1 decimal place.
:::

:::try Further Pure 1 warm-up ★
Q: [3 marks] (#math.fm.series) ★ Use standard results from MF19 to find the value of \(\displaystyle\sum_{r=1}^{12}\left(r^2 + 3r\right)\).
A: \(\displaystyle\sum_{r=1}^{12}r^2 = \frac{12 \times 13 \times 25}{6} = 650\). [B1]
\(\displaystyle\sum_{r=1}^{12}3r = 3 \times \frac{12 \times 13}{2} = 234\). [B1]
The total is \(650 + 234 = 884\). [B1]
Q: [3 marks] (#math.fm.matrices) ★ Given \(\mathbf{A} = \begin{pmatrix} 1 & 2 & 0 \\ 3 & -1 & 2 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 2 & 1 \\ 0 & 3 \\ 1 & -1 \end{pmatrix}\), find \(\mathbf{A}\mathbf{B}\) and state the order of \(\mathbf{B}\mathbf{A}\).
A: Each entry of \(\mathbf{A}\mathbf{B}\) is a row of \(\mathbf{A}\) times a column of \(\mathbf{B}\):
\[\mathbf{A}\mathbf{B} = \begin{pmatrix} 2 + 0 + 0 & 1 + 6 + 0 \\ 6 + 0 + 2 & 3 - 3 - 2 \end{pmatrix}\]
[M1]
\[= \begin{pmatrix} 2 & 7 \\ 8 & -2 \end{pmatrix}\]
[A1]
\(\mathbf{B}\) is \(3 \times 2\) and \(\mathbf{A}\) is \(2 \times 3\), so \(\mathbf{B}\mathbf{A}\) is \(3 \times 3\). [B1]
Q: [3 marks] (#math.fm.roots) ★ The roots of \(2x^2 - 6x + 3 = 0\) are \(\alpha\) and \(\beta\). Find the value of \(\alpha^2 + \beta^2\).
A: \(\alpha + \beta = 3\) and \(\alpha\beta = \tfrac32\). [B1]
\(\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta\). [M1]
\(= 9 - 3 = 6\). [A1]
Q: [3 marks] (#math.fm.polar) ★ (a) Find the Cartesian coordinates of the point with polar coordinates \(\left(4, \tfrac13\pi\right)\). [1]

(b) Find a Cartesian equation of the curve with polar equation \(r = 6\cos\theta\). [2]
A: (a) \(\left(4\cos\tfrac13\pi,\ 4\sin\tfrac13\pi\right) = \left(2, 2\sqrt3\right)\). [B1]

(b) Multiply both sides by \(r\): \(r^2 = 6r\cos\theta\). [M1]
Use \(r^2 = x^2 + y^2\) and \(r\cos\theta = x\): \(x^2 + y^2 = 6x\). [A1] (a circle of radius 3 with centre \((3, 0)\))
Q: [3 marks] (#math.fm.vectors) ★ The vectors \(\mathbf{a}\) and \(\mathbf{b}\) are \(\mathbf{i} + 2\mathbf{j} - \mathbf{k}\) and \(3\mathbf{i} + 2\mathbf{k}\). Find \(\mathbf{a} \times \mathbf{b}\), and the area of the triangle with sides \(\mathbf{a}\) and \(\mathbf{b}\).
A: \[\mathbf{a} \times \mathbf{b} = \begin{pmatrix} 2 \times 2 - (-1) \times 0 \\ (-1) \times 3 - 1 \times 2 \\ 1 \times 0 - 2 \times 3 \end{pmatrix}\]
[M1]
\[= \begin{pmatrix} 4 \\ -5 \\ -6 \end{pmatrix}\]
[A1]
Area \(= \tfrac12|\mathbf{a} \times \mathbf{b}| = \tfrac12\sqrt{16 + 25 + 36} = \tfrac12\sqrt{77} = 4.39\). [A1]
Q: [2 marks] (#math.fm.rational) ★ Find the equations of the asymptotes of the curve \(y = \dfrac{x^2 + 1}{x - 1}\).
A: The denominator is zero at \(x = 1\), so \(x = 1\) is a vertical asymptote. [B1]
Divide: \(x^2 + 1 = (x - 1)(x + 1) + 2\), so \(y = x + 1 + \dfrac{2}{x - 1}\). As \(x \to \pm\infty\), \(y \to x + 1\), so \(y = x + 1\) is an oblique asymptote. [B1]
Q: [2 marks] (#math.fm.induction) ★ Given that \(7^k - 1\) is divisible by 6 for some positive integer \(k\), show that \(7^{k+1} - 1\) is divisible by 6.
A: \(7^{k+1} - 1 = 7\left(7^k - 1\right) + 6\). [M1]
\(7^k - 1\) is a multiple of 6, so both terms on the right are multiples of 6, and so is \(7^{k+1} - 1\). [A1]
Q: [4 marks] (#math.fm.transform) ★ The matrix \(\mathbf{R}\) represents a rotation through \(90^\circ\) anticlockwise about the origin, and \(\mathbf{S}\) represents a reflection in the line \(y = x\). Find the single matrix that represents the reflection followed by the rotation, and describe the transformation it represents.
A: \(\mathbf{R} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\). [B1]
\(\mathbf{S} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\). [B1]
\(\mathbf{S}\) first and then \(\mathbf{R}\) is the product \(\mathbf{R}\mathbf{S}\) (the first transformation is on the right): [M1]
\[\mathbf{R}\mathbf{S} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}\]
This is a reflection in the \(y\)-axis. [A1]
:::

:::try Further Pure 1 exam standard ★★
Q: [3 marks] (#math.fm.graphs) ★★ The curve \(y = f(x)\) has equation \(y = x^2 - 4x\). Sketch the curve \(y = \dfrac{1}{f(x)}\), stating the equations of the asymptotes and the coordinates of the turning point.
A: \(f(x) = x(x - 4)\) is zero at \(x = 0\) and \(x = 4\), so \(y = \dfrac{1}{f(x)}\) has vertical asymptotes \(x = 0\) and \(x = 4\), and the horizontal asymptote \(y = 0\). [B1]
Between the asymptotes \(f(x)\) takes values from \(-4\) up to 0 (its minimum is \(f(2) = -4\)), so \(\dfrac{1}{f(x)} \le -\dfrac14\): the middle branch lies below the \(x\)-axis with its maximum at \(\left(2, -\tfrac14\right)\). [B1]
For \(x < 0\) and for \(x > 4\), \(f(x) > 0\): each outer branch lies above the \(x\)-axis, rising to \(+\infty\) at the asymptote and approaching \(y = 0\) as \(|x| \to \infty\). The curve does not meet either axis. [B1]
Q: [6 marks] (#math.fm.vectors2) ★★ The line \(l\) has equation \(\mathbf{r} = \mathbf{i} + 2\mathbf{k} + \lambda(2\mathbf{i} + \mathbf{j} - \mathbf{k})\) and the plane \(\Pi\) has equation \(x + 2y + 3z = 10\).

(a) Find the coordinates of the point where \(l\) meets \(\Pi\). [3]

(b) Find the acute angle between \(l\) and \(\Pi\). [3]
A: (a) A point of \(l\) is \((1 + 2\lambda,\ \lambda,\ 2 - \lambda)\). Substitute into the plane: [M1]
\[(1 + 2\lambda) + 2\lambda + 3(2 - \lambda) = 10 \quad\Rightarrow\quad 7 + \lambda = 10\]
\(\lambda = 3\). [A1]
The point is \((7, 3, -1)\). [A1]

(b) The direction of \(l\) is \(\mathbf{d} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}\) and a normal to \(\Pi\) is \(\mathbf{n} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\). For the angle \(\varphi\) between a line and a plane,
\[\sin\varphi = \frac{|\mathbf{d} \cdot \mathbf{n}|}{|\mathbf{d}||\mathbf{n}|}\]
[M1]
\[= \frac{|2 + 2 - 3|}{\sqrt6\sqrt{14}} = \frac{1}{\sqrt{84}}\]
[A1]
\(\varphi = 6.3^\circ\). [A1]
Q: [5 marks] (#math.fm.series) ★★ (a) Show that \(\dfrac{1}{r(r + 2)} = \dfrac12\left(\dfrac1r - \dfrac{1}{r + 2}\right)\). [1]

(b) Hence use the method of differences to find \(\displaystyle\sum_{r=1}^{n}\frac{1}{r(r + 2)}\) in terms of \(n\). [3]

(c) Deduce the value of \(\displaystyle\sum_{r=1}^{\infty}\frac{1}{r(r + 2)}\). [1]
A: (a) \(\dfrac12\left(\dfrac1r - \dfrac{1}{r + 2}\right) = \dfrac12 \times \dfrac{(r + 2) - r}{r(r + 2)} = \dfrac{1}{r(r + 2)}\). [B1]

(b) Write out the terms:
\[\begin{aligned}r=1:&\ \tfrac12\left(1 - \tfrac13\right) \\ r=2:&\ \tfrac12\left(\tfrac12 - \tfrac14\right) \\ r=3:&\ \tfrac12\left(\tfrac13 - \tfrac15\right) \\ &\ \vdots \\ r=n:&\ \tfrac12\left(\tfrac1n - \tfrac{1}{n+2}\right)\end{aligned}\]
[M1]
All the terms cancel except \(1\) and \(\tfrac12\) at the start and \(\tfrac{1}{n+1}\) and \(\tfrac{1}{n+2}\) at the end:
\[\sum_{r=1}^{n} = \tfrac12\left(1 + \tfrac12 - \tfrac{1}{n+1} - \tfrac{1}{n+2}\right)\]
[A1]
\[= \frac34 - \frac{2n + 3}{2(n + 1)(n + 2)}\]
[A1]

(c) As \(n \to \infty\) the fraction in \(n\) tends to 0, so the sum to infinity is \(\dfrac34\). [B1]
Q: [5 marks] (#math.fm.roots) ★★ The cubic equation \(x^3 - 4x^2 + 5x - 7 = 0\) has roots \(\alpha\), \(\beta\) and \(\gamma\).

(a) Find the value of \(\alpha^2 + \beta^2 + \gamma^2\). [2]

(b) Find a cubic equation with roots \(\dfrac1\alpha\), \(\dfrac1\beta\) and \(\dfrac1\gamma\). [3]
A: (a) \(\sum\alpha = 4\) and \(\sum\alpha\beta = 5\), so
\[\alpha^2 + \beta^2 + \gamma^2 = \left(\sum\alpha\right)^2 - 2\sum\alpha\beta\]
[M1]
\[= 16 - 10 = 6\]
[A1]

(b) Let \(y = \dfrac1x\), so \(x = \dfrac1y\). [B1]
\[\frac{1}{y^3} - \frac{4}{y^2} + \frac5y - 7 = 0\]
[M1]
Multiply by \(y^3\): \(1 - 4y + 5y^2 - 7y^3 = 0\), that is \(7y^3 - 5y^2 + 4y - 1 = 0\). [A1]
Q: [4 marks] (#math.fm.polar) ★★ Find the area of the region enclosed by the cardioid with polar equation \(r = 2 + 2\cos\theta\), for \(0 \le \theta \le 2\pi\).
A: \[\text{Area} = \tfrac12\int_0^{2\pi}(2 + 2\cos\theta)^2\,d\theta\]
[M1]
Expand and use \(\cos^2\theta = \tfrac12(1 + \cos 2\theta)\):
\[\begin{aligned}\text{Area} &= 2\int_0^{2\pi}\left(1 + 2\cos\theta + \cos^2\theta\right)d\theta \\ &= 2\int_0^{2\pi}\left(\tfrac32 + 2\cos\theta + \tfrac12\cos 2\theta\right)d\theta\end{aligned}\]
[M1]
\[= 2\left[\tfrac32\theta + 2\sin\theta + \tfrac14\sin 2\theta\right]_0^{2\pi}\]
[A1]
\[= 2 \times 3\pi = 6\pi\]
[A1]
Q: [5 marks] (#math.fm.matrices) ★★ The matrix \(\mathbf{M}\) is \(\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}\). Show that \(\mathbf{M}\) is non-singular and find \(\mathbf{M}^{-1}\).
A: Expand \(\det\mathbf{M}\) along the first row:
\[\det\mathbf{M} = 1(0 - 24) - 2(0 - 20) + 3(0 - 5) = -24 + 40 - 15 = 1\]
[M1 A1]
This is not zero, so \(\mathbf{M}\) is non-singular.
The matrix of cofactors is
\[\begin{pmatrix} -24 & 20 & -5 \\ 18 & -15 & 4 \\ 5 & -4 & 1 \end{pmatrix}\]
[M1 A1]
Transpose it and divide by \(\det\mathbf{M} = 1\):
\[\mathbf{M}^{-1} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}\]
[A1]
(check: row 1 of \(\mathbf{M}\) times column 1 of \(\mathbf{M}^{-1}\) is \(-24 + 40 - 15 = 1\))
Q: [5 marks] (#math.fm.induction) ★★ Prove by induction that \(\displaystyle\sum_{r=1}^{n}r(r + 1) = \frac{n(n + 1)(n + 2)}{3}\) for all positive integers \(n\).
A: When \(n = 1\): the left-hand side is \(1 \times 2 = 2\) and the right-hand side is \(\dfrac{1 \times 2 \times 3}{3} = 2\), so the result is true for \(n = 1\). [B1]
Assume the result is true for \(n = k\). [B1]
Then
\[\sum_{r=1}^{k+1}r(r + 1) = \frac{k(k + 1)(k + 2)}{3} + (k + 1)(k + 2)\]
[M1]
\[= \frac{(k + 1)(k + 2)(k + 3)}{3}\]
[A1]
This is the result with \(n = k + 1\). The result is true for \(n = 1\), and true for \(n = k + 1\) whenever it is true for \(n = k\), so by induction it is true for all positive integers \(n\). [A1]
:::

:::try Mixed Further Pure 1 and 2 ★★
Q: [5 marks] (#math.fm.hyperbolic) ★★ (a) Prove that \(\sinh 2x \equiv 2\sinh x\cosh x\). [3]

(b) Hence solve the equation \(\sinh 2x = 3\sinh x\), giving any solutions that are not exact correct to 3 significant figures. [2]
A: (a) Use the definitions \(\sinh x = \tfrac12\left(e^x - e^{-x}\right)\) and \(\cosh x = \tfrac12\left(e^x + e^{-x}\right)\):
\[2\sinh x\cosh x = 2 \times \tfrac12\left(e^x - e^{-x}\right) \times \tfrac12\left(e^x + e^{-x}\right)\]
[M1]
\[= \tfrac12\left(e^{2x} - e^{-2x}\right)\]
[A1]
\[= \sinh 2x\]
[A1]

(b) \(2\sinh x\cosh x = 3\sinh x\), so \(\sinh x(2\cosh x - 3) = 0\). [M1]
Either \(\sinh x = 0\), so \(x = 0\), or \(\cosh x = \tfrac32\), so \(x = \pm\cosh^{-1}1.5 = \pm0.962\). [A1]
The solutions are \(x = 0\) and \(x = \pm0.962\).
Q: [4 marks] (#math.fm.series) ★★ Use standard results from MF19 to show that \(\displaystyle\sum_{r=n+1}^{2n}r^2 = \frac{n(2n + 1)(7n + 1)}{6}\).
A: The sum from \(n + 1\) to \(2n\) is the sum to \(2n\) less the sum to \(n\):
\[\sum_{r=n+1}^{2n}r^2 = \sum_{r=1}^{2n}r^2 - \sum_{r=1}^{n}r^2\]
[M1]
\[= \frac{2n(2n + 1)(4n + 1)}{6} - \frac{n(n + 1)(2n + 1)}{6}\]
[A1]
Take out the common factor \(\dfrac{n(2n + 1)}{6}\):
\[= \frac{n(2n + 1)}{6}\left[2(4n + 1) - (n + 1)\right]\]
[M1]
\[= \frac{n(2n + 1)(7n + 1)}{6}\]
[A1]
(check \(n = 1\): the sum is \(2^2 = 4\) and the formula gives \(\tfrac{1 \times 3 \times 8}{6} = 4\))
Q: [3 marks] (#math.fm.integ) ★★ Find \(\displaystyle\int\sinh^2 x\,dx\).
A: \(\cosh 2x = 1 + 2\sinh^2 x\), so \(\sinh^2 x = \tfrac12(\cosh 2x - 1)\). [M1]
\[\int\sinh^2 x\,dx = \tfrac12\int(\cosh 2x - 1)\,dx\]
[A1]
\[= \tfrac14\sinh 2x - \tfrac12 x + c\]
[A1]
Q: [3 marks] (#math.fm.transform) ★★ A triangle of area 6 is transformed by the matrix \(\mathbf{M} = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}\). Find the area of the image of the triangle.
A: \(\det\mathbf{M} = 3 \times 4 - 1 \times 2 = 10\). [B1]
The area scale factor is \(|\det\mathbf{M}|\). [M1]
The image has area \(10 \times 6 = 60\). [A1]
Q: [4 marks] (#math.fm.complex) ★★ Use de Moivre's theorem to express \(\left(\sqrt3 - i\right)^5\) in the form \(a + bi\), where \(a\) and \(b\) are exact.
A: \(\left|\sqrt3 - i\right| = 2\) and \(\arg\left(\sqrt3 - i\right) = -\tfrac16\pi\). [B1]
\[\left(\sqrt3 - i\right)^5 = 2^5\left[\cos\left(-\tfrac16\pi\right) + i\sin\left(-\tfrac16\pi\right)\right]^5\]
[M1]
\[= 32\left[\cos\left(-\tfrac56\pi\right) + i\sin\left(-\tfrac56\pi\right)\right]\]
[A1]
\[= 32\left(-\tfrac{\sqrt3}{2} - \tfrac12 i\right) = -16\sqrt3 - 16i\]
[A1]
Q: [5 marks] (#math.fm.de) ★★ Find the solution of the differential equation \(\dfrac{dy}{dx} - 2y = e^{3x}\) for which \(y = 2\) when \(x = 0\).
A: The integrating factor is \(e^{\int -2\,dx} = e^{-2x}\). [B1]
\[\frac{d}{dx}\left(ye^{-2x}\right) = e^{3x} \times e^{-2x} = e^x\]
[M1]
\[ye^{-2x} = e^x + c\]
[A1]
When \(x = 0\), \(y = 2\): \(2 = 1 + c\), so \(c = 1\). [M1]
\[y = e^{3x} + e^{2x}\]
[A1]
Q: [6 marks] (#math.fm.systems) ★★ Consider the equations
\[\begin{aligned}x + y + z &= 1 \\ x + 2y + 3z &= 4 \\ 2x + 3y + kz &= 5\end{aligned}\]
where \(k\) is a constant.

(a) Show that the equations have a unique solution unless \(k = 4\). [3]

(b) For \(k = 4\), show that the equations are consistent and find the line of intersection of the three planes. [3]
A: (a) The determinant of the coefficient matrix is
\[\begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & k \end{vmatrix} = 1(2k - 9) - 1(k - 6) + 1(3 - 4)\]
[M1]
\[= k - 4\]
[A1]
There is a unique solution when the determinant is not zero, that is unless \(k = 4\). [A1]

(b) When \(k = 4\) the left-hand side of the third equation is the sum of the left-hand sides of the first two, and \(1 + 4 = 5\), so the third equation follows from the first two: the equations are consistent. [M1]
Subtract the first two equations: \(y + 2z = 3\). Let \(z = \lambda\), so \(y = 3 - 2\lambda\) and \(x = 1 - y - z = \lambda - 2\). [M1]
\[\mathbf{r} = \begin{pmatrix} -2 \\ 3 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}\]
[A1]
Q: [5 marks] (#math.fm.diff) ★★ Given that \(y = e^{\sin x}\):

(a) show that \(\dfrac{d^2y}{dx^2} = y\left(\cos^2 x - \sin x\right)\). [2]

(b) Find the Maclaurin series for \(y\) up to and including the term in \(x^3\). [3]
A: (a) \(\dfrac{dy}{dx} = \cos x\,e^{\sin x} = y\cos x\). [M1]
Differentiate again, using the product rule:
\[\frac{d^2y}{dx^2} = \frac{dy}{dx}\cos x - y\sin x = y\cos^2 x - y\sin x\]
[A1]

(b) At \(x = 0\): \(y = 1\), \(\dfrac{dy}{dx} = 1\) and \(\dfrac{d^2y}{dx^2} = 1\). [M1]
Differentiate \(y'' = y(\cos^2 x - \sin x)\) once more:
\[y''' = y'\left(\cos^2 x - \sin x\right) + y\left(-2\cos x\sin x - \cos x\right)\]
so at \(x = 0\), \(y''' = 1 \times 1 + 1 \times (-1) = 0\). [A1]
\[y = 1 + x + \tfrac12 x^2 + 0 \times x^3 + \cdots\]
So \(y \approx 1 + x + \tfrac12 x^2\) (the coefficient of \(x^3\) is zero). [A1]
Q: [4 marks] (#math.fm.matrices2) ★★ Find the eigenvalues of the matrix \(\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\) and a corresponding eigenvector for each.
A: The characteristic equation is \(\det(\mathbf{A} - \lambda\mathbf{I}) = (3 - \lambda)(2 - \lambda) - 2 = 0\), that is
\[\lambda^2 - 5\lambda + 4 = 0\]
[M1]
\(\lambda = 1\) or \(\lambda = 4\). [A1]
For \(\lambda = 1\): \(\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{0}\) gives \(2x + y = 0\), so \(\begin{pmatrix} 1 \\ -2 \end{pmatrix}\). [M1]
For \(\lambda = 4\): \(\begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{0}\) gives \(x = y\), so \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\). [A1]
(any non-zero multiples)
:::

:::try Stretch ★★★
Q: [6 marks] (#math.fm.vectors2) ★★★ The point \(P\) has coordinates \((1, 2, 0)\) and the plane \(\Pi\) has equation \(2x - y + 2z = 9\).

(a) Find the coordinates of the foot \(F\) of the perpendicular from \(P\) to \(\Pi\). [4]

(b) Find the distance \(PF\). [1]

(c) Find the position vector of the reflection of \(P\) in \(\Pi\). [1]
A: (a) A normal to \(\Pi\) is \(\mathbf{n} = \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}\), so the perpendicular through \(P\) is \(\mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} + t\begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}\). [M1]
Its point \((1 + 2t,\ 2 - t,\ 2t)\) is on \(\Pi\) when
\[2(1 + 2t) - (2 - t) + 2(2t) = 9\]
[M1]
\[9t = 9\]
\(t = 1\). [A1]
\(F = (3, 1, 2)\). [A1] (check: \(6 - 1 + 4 = 9\))

(b) \(\overrightarrow{PF} = \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}\), so \(PF = \sqrt{4 + 1 + 4} = 3\). [B1]

(c) The reflection \(P'\) is as far beyond \(\Pi\) as \(P\) is before it: \(\overrightarrow{OP'} = \overrightarrow{OP} + 2\overrightarrow{PF} = \begin{pmatrix} 5 \\ 0 \\ 4 \end{pmatrix}\). [B1]
Q: [6 marks] (#math.fm.reduction) ★★★ Let \(I_n = \displaystyle\int_0^1 x^n e^{-x}\,dx\), for \(n \ge 0\).

(a) Show that \(I_n = nI_{n-1} - e^{-1}\) for \(n \ge 1\). [3]

(b) Find the exact value of \(I_3\). [3]
A: (a) Integrate by parts with \(u = x^n\) and \(\dfrac{dv}{dx} = e^{-x}\), so \(v = -e^{-x}\): [M1]
\[I_n = \left[-x^n e^{-x}\right]_0^1 + n\int_0^1 x^{n-1}e^{-x}\,dx\]
[A1]
\[I_n = -e^{-1} + nI_{n-1}\]
[A1]

(b) \(I_0 = \displaystyle\int_0^1 e^{-x}\,dx = 1 - e^{-1}\). [B1]
\(I_1 = I_0 - e^{-1} = 1 - 2e^{-1}\) and \(I_2 = 2I_1 - e^{-1} = 2 - 5e^{-1}\). [M1]
\(I_3 = 3I_2 - e^{-1} = 6 - 16e^{-1}\). [A1]
Q: [6 marks] (#math.fm.de2) ★★★ Find the general solution of the differential equation \(\dfrac{d^2y}{dx^2} + 2\dfrac{dy}{dx} + 5y = 10x\).
A: The auxiliary equation is \(m^2 + 2m + 5 = 0\). [M1]
\(m = \dfrac{-2 \pm \sqrt{4 - 20}}{2} = -1 \pm 2i\). [A1]
The complementary function is \(y = e^{-x}\left(A\cos 2x + B\sin 2x\right)\). [A1]
For a particular integral try \(y = ax + b\), so \(y' = a\) and \(y'' = 0\): [M1]
\[2a + 5(ax + b) = 10x\]
Comparing coefficients: \(5a = 10\), so \(a = 2\), and \(2a + 5b = 0\), so \(b = -\tfrac45\). [A1]
The general solution is
\[y = e^{-x}\left(A\cos 2x + B\sin 2x\right) + 2x - \tfrac45\]
[A1]
Q: [6 marks] (#math.fm.rational) ★★★ The curve \(C\) has equation \(y = \dfrac{x^2 + 1}{x - 1}\).

(a) By forming a quadratic equation in \(x\), find the set of values of \(y\) for which the equation has a real solution for \(x\). [4]

(b) Hence find the coordinates of the stationary points of \(C\). [2]
A: (a) \(y(x - 1) = x^2 + 1\), so \(x^2 - yx + (y + 1) = 0\). [M1]
For real \(x\) the discriminant is non-negative:
\[y^2 - 4(y + 1) \ge 0\]
[M1]
\[y^2 - 4y - 4 \ge 0\]
[A1]
The roots of \(y^2 - 4y - 4 = 0\) are \(y = 2 \pm 2\sqrt2\), so \(y \le 2 - 2\sqrt2\) or \(y \ge 2 + 2\sqrt2\). [A1]

(b) The two boundary values \(y = 2 \pm 2\sqrt2\) are where the discriminant is zero, so each is given by a repeated root \(x = \dfrac y2 = 1 \pm \sqrt2\). The curve reaches the height \(y = 2 \pm 2\sqrt2\) at one value of \(x\) only, so it touches that horizontal line there: a stationary point. [M1]
The stationary points are \(\left(1 + \sqrt2,\ 2 + 2\sqrt2\right)\) and \(\left(1 - \sqrt2,\ 2 - 2\sqrt2\right)\). [A1]
Q: [7 marks] (#math.fm.complex2) ★★★ (a) Solve the equation \(z^3 = 8i\), giving the roots in the form \(re^{i\theta}\) where \(r > 0\) and \(-\pi < \theta \le \pi\). [4]

(b) The roots in (a) are represented by the points \(A\), \(B\) and \(C\) on an Argand diagram. Find the area of triangle \(ABC\). [3]
A: (a) Write \(8i = 8e^{i(\pi/2 + 2k\pi)}\). [M1]
\[z = 2e^{i(\pi/6 + 2k\pi/3)}\]
[M1 A1]
For \(k = 0, 1, 2\), and moving the last argument into the range \(-\pi < \theta \le \pi\), the roots are
\[2e^{i\pi/6}, \qquad 2e^{5i\pi/6}, \qquad 2e^{-i\pi/2}\]
[A1]

(b) The three points are on the circle \(|z| = 2\) with equal angles \(\tfrac23\pi\) between them, so the triangle is made of three triangles with sides 2 and 2 and angle \(\tfrac23\pi\) at the origin. [M1]
Each has area \(\tfrac12 \times 2 \times 2 \times \sin\tfrac23\pi = \sqrt3\). [A1]
The area of \(ABC\) is \(3\sqrt3\). [A1]
Q: [7 marks] (#math.fm.arclength) ★★★ The curve \(C\) has equation \(y = \cosh x\) for \(0 \le x \le \ln 3\).

(a) Find the length of \(C\). [4]

(b) The arc is rotated through \(2\pi\) radians about the \(x\)-axis. Find, in exact form, the area of the surface generated. [3]
A: (a) \(\dfrac{dy}{dx} = \sinh x\), so \(1 + \left(\dfrac{dy}{dx}\right)^2 = 1 + \sinh^2 x = \cosh^2 x\). [M1 A1]
\[\text{Length} = \int_0^{\ln 3}\cosh x\,dx = \left[\sinh x\right]_0^{\ln 3}\]
[M1]
\[= \tfrac12\left(3 - \tfrac13\right) = \tfrac43\]
[A1]

(b) \[S = 2\pi\int_0^{\ln 3}y\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = 2\pi\int_0^{\ln 3}\cosh^2 x\,dx\]
[M1]
\[= \pi\int_0^{\ln 3}(1 + \cosh 2x)\,dx = \pi\left[x + \tfrac12\sinh 2x\right]_0^{\ln 3}\]
[A1]
Since \(\sinh(2\ln 3) = \tfrac12\left(9 - \tfrac19\right) = \tfrac{40}{9}\),
\[S = \pi\left(\ln 3 + \tfrac{20}{9}\right)\]
[A1]
Q: [5 marks] (#math.fm.induction) ★★★ The matrix \(\mathbf{M}\) is \(\begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix}\). Prove by induction that \(\mathbf{M}^n = \begin{pmatrix} 1 + 2n & -2n \\ 2n & 1 - 2n \end{pmatrix}\) for all positive integers \(n\).
A: When \(n = 1\) the formula gives \(\begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix} = \mathbf{M}\), so it is true for \(n = 1\). [B1]
Assume it is true for \(n = k\). [B1]
Then \(\mathbf{M}^{k+1} = \mathbf{M}^k\mathbf{M}\):
\[\begin{pmatrix} 1 + 2k & -2k \\ 2k & 1 - 2k \end{pmatrix}\begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix}\]
[M1]
\[= \begin{pmatrix} 3 + 2k & -2 - 2k \\ 2 + 2k & -1 - 2k \end{pmatrix} = \begin{pmatrix} 1 + 2(k+1) & -2(k+1) \\ 2(k+1) & 1 - 2(k+1) \end{pmatrix}\]
[A1]
This is the formula with \(n = k + 1\). The formula is true for \(n = 1\), and true for \(n = k + 1\) whenever it is true for \(n = k\), so by induction it is true for all positive integers \(n\). [A1]
:::

## Where the questions come from

Each block restarts at question 1, so a question is named by its block and number.

| Chapter | Questions (block and number) |
|---|---|
| [Roots of polynomial equations](#math.fm.roots) | warm-up 3, exam standard 4 |
| [Summation of series](#math.fm.series) | warm-up 1, exam standard 3, mixed 2 |
| [Matrices: algebra, determinants and inverses](#math.fm.matrices) | warm-up 2, exam standard 6 |
| [Matrices as transformations](#math.fm.transform) | warm-up 8, mixed 4 |
| [Proof by induction](#math.fm.induction) | warm-up 7, exam standard 7, stretch 7 |
| [Rational functions and their graphs](#math.fm.rational) | warm-up 6, stretch 4 |
| [Graphs related to y = f(x)](#math.fm.graphs) | exam standard 1 |
| [Polar coordinates](#math.fm.polar) | warm-up 4, exam standard 5 |
| [Vectors: the vector product and planes](#math.fm.vectors) | warm-up 5 |
| [Vectors: intersections, angles and distances](#math.fm.vectors2) | exam standard 2, stretch 1 |
| [Hyperbolic functions](#math.fm.hyperbolic) | mixed 1 |
| [Further differentiation and Maclaurin series](#math.fm.diff) | mixed 8 |
| [Further integration: hyperbolic and inverse forms](#math.fm.integ) | mixed 3 |
| [Reduction formulae](#math.fm.reduction) | stretch 2 |
| [Arc length and surface area](#math.fm.arclength) | stretch 6 |
| [De Moivre's theorem and trigonometry](#math.fm.complex) | mixed 5 |
| [Roots of unity and complex series](#math.fm.complex2) | stretch 5 |
| [Three equations, three planes](#math.fm.systems) | mixed 7 |
| [Eigenvalues and eigenvectors](#math.fm.matrices2) | mixed 9 |
| [First order differential equations](#math.fm.de) | mixed 6 |
| [Second order differential equations](#math.fm.de2) | stretch 3 |

Rectangles and bounds ([Sums, rectangles and bounds](#math.fm.rectangles)) has no question here: practise it with Question 5 of [Mock Paper 2](#math.fm.mock.p2).

:::recap
- Mixed practice trains the first step: read the question, name the chapter, then choose the method. Do a few questions at a time and keep a list of the chapters you had to look up.
- The warm-up and exam standard blocks are Paper 1 content; Paper 2 assumes all of it, so a Paper 2 question can start from a plane, a matrix or a method of differences.
- Every lost mark has a name: a method mark you did not show, an accuracy mark lost in the algebra, or a given result you did not reach honestly. Write the name next to the question and fix that habit first.
- When the questions feel easy, sit [Mock Paper 1](#math.fm.mock.p1) and [Mock Paper 2](#math.fm.mock.p2) under exam conditions.
:::

Next: [Mixed practice: Further Mechanics and Statistics](#math.fm.mixed.applied)
