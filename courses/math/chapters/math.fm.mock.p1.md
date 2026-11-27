@chapter math.fm.mock.p1
@title Mock Paper 1: Further Pure Mathematics 1
@level mock
@paper CAIE 9231 Paper 1
@time 2 h
@summary A complete original mock for 9231 Paper 1 (Further Pure Mathematics 1): 7 questions, 75 marks, 2 hours, laid out like the real paper (marks 8, 7, 7, 9, 13, 16, 15) and covering series, roots, induction, matrices, polar curves, vectors and planes, and rational functions. Full mark scheme with accepted alternatives; sit it in one go, mark yourself and see which chapters to revise.

:::why
Paper 1 is the compulsory Further Pure paper: it is the whole of the pure part of the AS and 30% of the A Level. It has few questions and each one is long, so the marks come from setting out a multi-part argument without losing the thread. This mock has the same number of questions, the same spread of marks and the same kinds of task as the real paper, but every question is new. Do it under exam conditions first, then use the mark scheme to see what the examiner is looking for line by line.
:::

:::exam Instructions
- Answer **all** questions. The total is **75 marks** and you have **2 hours**.
- You will need the list of formulae **MF19**. You should use a calculator where appropriate: only a scientific calculator, no graphical or symbolic algebra calculator.
- You must show all necessary working clearly; **no marks will be given for unsupported answers from a calculator**.
- Give non-exact numerical answers correct to **3 significant figures**, or **1 decimal place for angles in degrees**, unless the question says otherwise.
- The number of marks for each question or part question is shown in brackets [ ]. Roughly one and a half minutes per mark leaves a few minutes at the end.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [8 marks] (#math.fm.series) (a) Use standard results from the list of formulae (MF19) to show that
\[\sum_{r=1}^{n}(2r-1)(3r+1) = \tfrac12 n\left(an^2 + bn + c\right),\]
where \(a\), \(b\) and \(c\) are integers to be determined. [3]

(b) Use the method of differences to find \(\displaystyle\sum_{r=1}^{n}\frac{1}{(r+1)(r+3)}\) in terms of \(n\). [4]

(c) Deduce the value of \(\displaystyle\sum_{r=1}^{\infty}\frac{1}{(r+1)(r+3)}\). [1]
A: (a) Expand the bracket: \((2r-1)(3r+1) = 6r^2 - r - 1\). [B1]
Use the standard results for \(\sum r^2\), \(\sum r\) and \(\sum 1\):
\[\begin{aligned}\sum_{r=1}^{n}(6r^2 - r - 1) &= 6 \times \frac{n(n+1)(2n+1)}{6} \\ &\quad - \frac{n(n+1)}{2} - n\end{aligned}\]
[M1]
Take out the factor \(\tfrac12 n\):
\[\begin{aligned}&= \tfrac12 n\big[2(n+1)(2n+1) - (n+1) - 2\big] \\ &= \tfrac12 n\left(4n^2 + 5n - 1\right)\end{aligned}\]
So \(a = 4\), \(b = 5\), \(c = -1\). [A1]

(b) Split the term into partial fractions: \(\dfrac{1}{(r+1)(r+3)} = \dfrac12\left(\dfrac{1}{r+1} - \dfrac{1}{r+3}\right)\). [B1]
Write out the first and last terms:
\[\begin{aligned}r=1:&\ \tfrac12\left(\tfrac12 - \tfrac14\right) \\ r=2:&\ \tfrac12\left(\tfrac13 - \tfrac15\right) \\ r=3:&\ \tfrac12\left(\tfrac14 - \tfrac16\right) \\ &\ \vdots \\ r=n-1:&\ \tfrac12\left(\tfrac1n - \tfrac{1}{n+2}\right) \\ r=n:&\ \tfrac12\left(\tfrac{1}{n+1} - \tfrac{1}{n+3}\right)\end{aligned}\]
[M1]
Every term from \(\tfrac14\) to \(\tfrac{1}{n+1}\) cancels, leaving \(\tfrac12\left(\tfrac12 + \tfrac13 - \tfrac{1}{n+2} - \tfrac{1}{n+3}\right)\). [A1] (this mark needs all four remaining terms correct)
\[\sum_{r=1}^{n}\frac{1}{(r+1)(r+3)} = \frac{5}{12} - \frac{2n+5}{2(n+2)(n+3)}\]
[A1]

(c) As \(n \to \infty\), both fractions in \(n\) tend to 0, so the sum to infinity is \(\dfrac{5}{12}\). [B1]
:::

:::try
Q: [7 marks] (#math.fm.roots) The cubic equation \(x^3 + 2x^2 - 5x + 7 = 0\) has roots \(\alpha\), \(\beta\) and \(\gamma\).

(a) Find a cubic equation whose roots are \(2\alpha + 1\), \(2\beta + 1\) and \(2\gamma + 1\). [3]

(b) Find the value of \(\alpha^2 + \beta^2 + \gamma^2\). [2]

(c) Find the value of \(\alpha^3 + \beta^3 + \gamma^3\). [2]
A: (a) Let \(y = 2x + 1\), so \(x = \dfrac{y-1}{2}\). [B1]
Substitute into the cubic:
\[\left(\frac{y-1}{2}\right)^3 + 2\left(\frac{y-1}{2}\right)^2 - 5\left(\frac{y-1}{2}\right) + 7 = 0\]
[M1]
Multiply by 8 and expand:
\[\begin{aligned}(y-1)^3 + 4(y-1)^2 - 20(y-1) + 56 &= 0 \\ y^3 + y^2 - 25y + 79 &= 0\end{aligned}\]
[A1] (any non-zero multiple; the equation may be written in \(x\))

(b) From the equation: \(\sum\alpha = -2\) and \(\sum\alpha\beta = -5\), so
\[\alpha^2 + \beta^2 + \gamma^2 = \left(\sum\alpha\right)^2 - 2\sum\alpha\beta\]
[M1]
\[= (-2)^2 - 2(-5) = 14\]
[A1]

(c) Each root satisfies the equation, so \(\alpha^3 = -2\alpha^2 + 5\alpha - 7\), and similarly for \(\beta\) and \(\gamma\). Add the three equations:
\[\alpha^3 + \beta^3 + \gamma^3 = -2(14) + 5(-2) - 3(7)\]
[M1]
\[= -59\]
[A1] (alternative: \(\left(\sum\alpha\right)^3 - 3\sum\alpha\sum\alpha\beta + 3\alpha\beta\gamma\) with \(\alpha\beta\gamma = -7\), M1 A1)
:::

:::try
Q: [7 marks] (#math.fm.induction) The sequence \(u_1, u_2, u_3, \ldots\) is such that \(u_1 = 1\) and \(u_{n+1} = 3u_n + 2\) for \(n \ge 1\).

(a) Prove by induction that \(u_n = 2 \times 3^{n-1} - 1\) for all positive integers \(n\). [5]

(b) Deduce that \(u_{n+1} - u_n\) is divisible by 4 for all positive integers \(n\). [2]
A: (a) When \(n = 1\): \(2 \times 3^0 - 1 = 1 = u_1\), so the formula is true for \(n = 1\). [B1]
Assume the formula is true for \(n = k\), that is \(u_k = 2 \times 3^{k-1} - 1\). [B1]
Then
\[\begin{aligned}u_{k+1} &= 3u_k + 2 \\ &= 3\left(2 \times 3^{k-1} - 1\right) + 2\end{aligned}\]
[M1]
\[u_{k+1} = 2 \times 3^k - 3 + 2 = 2 \times 3^k - 1\]
[A1]
This is the formula with \(n = k + 1\). The formula is true for \(n = 1\), and if it is true for \(n = k\) then it is true for \(n = k + 1\). Hence, by induction, it is true for all positive integers \(n\). [A1]

(b) Use the formula for \(u_{n+1}\) and \(u_n\):
\[\begin{aligned}u_{n+1} - u_n &= \left(2 \times 3^n - 1\right) \\ &\quad - \left(2 \times 3^{n-1} - 1\right)\end{aligned}\]
[M1]
\[= 2 \times 3^{n-1}(3 - 1) = 4 \times 3^{n-1}\]
Since \(3^{n-1}\) is an integer, \(u_{n+1} - u_n\) is divisible by 4. [A1]
:::

:::try
Q: [9 marks] (#math.fm.transform) The matrix \(\mathbf{M}\) is given by \(\mathbf{M} = \begin{pmatrix} 4 & -3 \\ 2 & -1 \end{pmatrix}\).

(a) Show that the line \(y = x\) is a line of invariant points of the transformation in the \(x\)–\(y\) plane represented by \(\mathbf{M}\). [2]

(b) Find the equation of the other invariant line through the origin. [4]

(c) The point \(P\) is mapped by \(\mathbf{M}\) to the point \((10, 6)\). Find the coordinates of \(P\). [3]
A: (a) A general point on \(y = x\) is \((x, x)\):
\[\begin{pmatrix} 4 & -3 \\ 2 & -1 \end{pmatrix}\begin{pmatrix} x \\ x \end{pmatrix} = \begin{pmatrix} 4x - 3x \\ 2x - x \end{pmatrix}\]
[M1]
\[= \begin{pmatrix} x \\ x \end{pmatrix}\]
so every point on \(y = x\) is mapped to itself. [A1]

(b) A point on the line \(y = mx\) is \((x, mx)\). Its image is
\[\begin{pmatrix} 4 - 3m \\ 2 - m \end{pmatrix}x.\]
[M1]
The image is on the same line when \(2 - m = m(4 - 3m)\), [M1] which gives
\[3m^2 - 5m + 2 = 0\]
[A1]
\[(3m - 2)(m - 1) = 0\]
\(m = 1\) is the line of invariant points, so the other invariant line is \(y = \tfrac23 x\) (or \(3y = 2x\)). [A1]
(Alternative: find the eigenvalues 1 and 2 and the eigenvector \(\begin{pmatrix} 3 \\ 2 \end{pmatrix}\) for 2, M1 M1 A1 A1.)

(c) \(\det\mathbf{M} = 4(-1) - (-3)(2) = 2\). [B1]
\[\mathbf{M}^{-1} = \frac12\begin{pmatrix} -1 & 3 \\ -2 & 4 \end{pmatrix}\]
[M1]
\[\begin{pmatrix} x \\ y \end{pmatrix} = \frac12\begin{pmatrix} -1 & 3 \\ -2 & 4 \end{pmatrix}\begin{pmatrix} 10 \\ 6 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}\]
So \(P\) is \((4, 2)\). [A1] (check: \(\mathbf{M}\begin{pmatrix} 4 \\ 2 \end{pmatrix} = \begin{pmatrix} 10 \\ 6 \end{pmatrix}\))
:::

:::try
Q: [13 marks] (#math.fm.polar) The curve \(C\) has polar equation \(r = 4\sin 2\theta\), for \(0 \le \theta \le \tfrac12\pi\).

(a) Sketch \(C\). [2]

(b) Find the area of the region enclosed by \(C\). [4]

The circle \(S\) has polar equation \(r = 2\).

(c) Show that \(C\) and \(S\) intersect where \(\theta = \tfrac{1}{12}\pi\) and where \(\theta = \tfrac{5}{12}\pi\). [2]

(d) Find, in exact form, the area of the region that is inside \(C\) and outside \(S\). [5]
A: (a) A single loop that starts at the pole, leaving along the initial line (\(\theta = 0\)), and returns to the pole along \(\theta = \tfrac12\pi\), tangent to each line there. [B1]
The loop is symmetrical about \(\theta = \tfrac14\pi\), where \(r\) has its greatest value 4, and it lies in the first quadrant. [B1]

(b) Area \(= \tfrac12\displaystyle\int_0^{\pi/2} r^2\,d\theta = \tfrac12\int_0^{\pi/2} 16\sin^2 2\theta\,d\theta\). [M1]
Use \(\sin^2 2\theta = \tfrac12(1 - \cos 4\theta)\):
\[\text{Area} = 4\int_0^{\pi/2}(1 - \cos 4\theta)\,d\theta\]
[M1]
\[= 4\left[\theta - \tfrac14\sin 4\theta\right]_0^{\pi/2}\]
[A1]
\[= 4 \times \tfrac12\pi = 2\pi\]
[A1]

(c) At an intersection \(4\sin 2\theta = 2\), so \(\sin 2\theta = \tfrac12\). [M1]
\(2\theta = \tfrac16\pi\) or \(\tfrac56\pi\) in the range \(0 \le 2\theta \le \pi\), so \(\theta = \tfrac{1}{12}\pi\) or \(\theta = \tfrac{5}{12}\pi\). [A1]

(d) Between \(\theta = \tfrac{1}{12}\pi\) and \(\tfrac{5}{12}\pi\) the curve \(C\) is outside \(S\) (since \(r > 2\)). The required area is
\[\tfrac12\int_{\pi/12}^{5\pi/12}\left(16\sin^2 2\theta - 4\right)d\theta\]
[M1]
Using \(16\sin^2 2\theta = 8 - 8\cos 4\theta\), the integrand becomes \(\tfrac12(4 - 8\cos 4\theta)\):
\[\text{Area} = \int_{\pi/12}^{5\pi/12}(2 - 4\cos 4\theta)\,d\theta\]
[M1]
\[= \left[2\theta - \sin 4\theta\right]_{\pi/12}^{5\pi/12}\]
[A1]
\[= \tfrac23\pi - \left(\sin\tfrac53\pi - \sin\tfrac13\pi\right)\]
[M1]
\[= \tfrac23\pi + \sqrt3\]
[A1]
:::

:::try
Q: [16 marks] (#math.fm.vectors) The points \(A\), \(B\) and \(C\) have position vectors \(\mathbf{i} + 2\mathbf{j}\), \(3\mathbf{i} + \mathbf{k}\) and \(-\mathbf{i}\) respectively.

(a) Find the equation of the plane \(ABC\), giving your answer in the form \(ax + by + cz = d\). [5]

(b) Find the acute angle between the plane \(ABC\) and the plane with equation \(2x + y - z = 4\). [4]

The point \(D\) has position vector \(t\mathbf{i} - 2\mathbf{j} + 2\mathbf{k}\).

(c) Find the values of \(t\) such that the shortest distance between the lines \(AB\) and \(CD\) is 2. [7]
A: (a) \(\overrightarrow{AB} = \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix}\) and \(\overrightarrow{AC} = \begin{pmatrix} -2 \\ -2 \\ 0 \end{pmatrix}\). [M1]
A normal to the plane is
\[\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix} (-2)(0) - (1)(-2) \\ (1)(-2) - (2)(0) \\ (2)(-2) - (-2)(-2) \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \\ -8 \end{pmatrix}\]
[M1] so a normal is \(\begin{pmatrix} 1 \\ -1 \\ -4 \end{pmatrix}\). [A1]
The plane is \(x - y - 4z = d\). Using \(A\): \(d = 1 - 2 - 0 = -1\). [M1]
The plane \(ABC\) is \(x - y - 4z = -1\) (or any multiple). [A1]
(Check with \(B\): \(3 - 0 - 4 = -1\); with \(C\): \(-1 - 0 - 0 = -1\).)

(b) The normals are \(\mathbf{n}_1 = \begin{pmatrix} 1 \\ -1 \\ -4 \end{pmatrix}\) and \(\mathbf{n}_2 = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}\). [B1]
\[\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{|\mathbf{n}_1||\mathbf{n}_2|}\]
[M1]
\[\mathbf{n}_1 \cdot \mathbf{n}_2 = 2 - 1 + 4 = 5 \quad\text{so}\quad \cos\theta = \frac{5}{\sqrt{18}\sqrt{6}}\]
[A1]
The acute angle is \(61.2^\circ\). [A1]

(c) \(AB\) has direction \(\mathbf{d}_1 = \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix}\) and \(\overrightarrow{CD} = \begin{pmatrix} t + 1 \\ -2 \\ 2 \end{pmatrix}\). [B1]
A vector perpendicular to both lines is
\[\mathbf{n} = \mathbf{d}_1 \times \overrightarrow{CD} = \begin{pmatrix} -2 \\ t - 3 \\ 2t - 2 \end{pmatrix}\]
[M1 A1]
The shortest distance is the component of \(\overrightarrow{AC}\) along \(\mathbf{n}\): [M1]
\[\overrightarrow{AC}\cdot\mathbf{n} = (-2)(-2) + (-2)(t - 3) + 0 = 10 - 2t\]
[A1]
\[|\mathbf{n}|^2 = 4 + (t - 3)^2 + (2t - 2)^2 = 5t^2 - 14t + 17\]
The distance is 2, so
\[\begin{aligned}(10 - 2t)^2 &= 4\left(5t^2 - 14t + 17\right) \\ 16t^2 - 16t - 32 &= 0 \\ t^2 - t - 2 &= 0\end{aligned}\]
[M1]
\[(t - 2)(t + 1) = 0\]
So \(t = 2\) or \(t = -1\). [A1]
:::

:::try
Q: [15 marks] (#math.fm.rational) The curve \(C\) has equation \(y = \dfrac{x(x + 3)}{x - 1}\).

(a) Find the equations of the asymptotes of \(C\). [2]

(b) Find the coordinates of any stationary points on \(C\). [4]

(c) Sketch \(C\), stating the coordinates of the intersections with the axes. [3]

(d) Sketch the curve with equation \(y^2 = \dfrac{x(x + 3)}{x - 1}\), stating the coordinates of the stationary points and of the intersections with the axes. [2]

(e) Find the set of values of \(x\) for which \(\dfrac{x(x + 3)}{x - 1} \le 2x\). [4]
A: (a) The denominator is zero when \(x = 1\), so \(x = 1\) is a vertical asymptote. [B1]
Divide: \(x^2 + 3x = (x - 1)(x + 4) + 4\), so \(y = x + 4 + \dfrac{4}{x - 1}\). As \(x \to \pm\infty\), \(y \to x + 4\), so \(y = x + 4\) is an oblique asymptote. [B1]

(b) Differentiate \(y = x + 4 + 4(x - 1)^{-1}\):
\[\frac{dy}{dx} = 1 - \frac{4}{(x - 1)^2} = \frac{x^2 - 2x - 3}{(x - 1)^2}\]
[M1 A1] (the quotient rule gives the same result)
Stationary points: \(\dfrac{dy}{dx} = 0\), so \((x - 3)(x + 1) = 0\). [M1]
The stationary points are \((-1, 1)\) and \((3, 9)\). [A1]

(c) The sketch has two branches, one on each side of \(x = 1\), approaching both asymptotes (the curve below \(y = x + 4\) on the left, above it on the right). [B1]
On the left, the curve passes through \((-3, 0)\) and \((0, 0)\) (the only intersections with the axes), with a maximum at \((-1, 1)\), and tends to \(-\infty\) as \(x \to 1^-\). [B1]
On the right, the curve comes down from \(+\infty\) beside \(x = 1\) to a minimum at \((3, 9)\), then rises towards \(y = x + 4\). [B1]

(d) The curve exists only where \(\dfrac{x(x + 3)}{x - 1} \ge 0\), that is \(-3 \le x \le 0\) or \(x > 1\), and it is symmetrical about the \(x\)-axis.
For \(-3 \le x \le 0\) there is a closed loop through \((-3, 0)\) and \((0, 0)\) with the points \((-1, 1)\) and \((-1, -1)\) as its highest and lowest points. [B1]
For \(x > 1\) there are two branches, mirror images in the \(x\)-axis, with \(x = 1\) as a vertical asymptote; the upper branch has its lowest point at \((3, 3)\) and the lower branch its highest at \((3, -3)\). [B1]

(e) Multiply both sides by \((x - 1)^2 > 0\), which keeps the inequality the same way round:
\[x(x + 3)(x - 1) \le 2x(x - 1)^2\]
[M1]
Collect and factorise, without dividing by \(x\):
\[\begin{aligned}x(x - 1)\left[(x + 3) - 2(x - 1)\right] &\le 0 \\ x(x - 1)(5 - x) &\le 0\end{aligned}\]
[M1]
The critical values are \(0\), \(1\) and \(5\). [A1]
The cubic is negative for \(0 < x < 1\) and for \(x > 5\), and zero at \(x = 0\) and \(x = 5\); \(x = 1\) is excluded because the original expression is not defined there:
\[0 \le x < 1 \quad\text{or}\quad x \ge 5\]
[A1]
:::

:::warn Where marks are usually lost on a paper like this
- **Cancelling without showing it** (Question 1(b)). The method of differences needs the first and last few terms written out; "the terms cancel" with no list earns neither the method mark nor the accuracy mark.
- **Sign and order slips in the vector product** (Question 6(a)). Write the components with their brackets, check the normal against all three points, and only then write the equation.
- **Dividing by a factor that can be zero** (Question 7(e)). Dividing the inequality by \(x\) loses the solution \(x = 0\) and can reverse the inequality. Multiply by the square \((x - 1)^2\) and factorise instead.
- **Outside and inside the wrong way round** (Question 5(d)). The area between two polar curves is \(\tfrac12\int\left(r_1^2 - r_2^2\right)d\theta\), where \(r_1\) is the outer curve, never \(\tfrac12\int(r_1 - r_2)^2\,d\theta\).
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 8 | Standard sums, method of differences | [Summation of series](#math.fm.series) |
| 2 | 7 | Roots of a cubic, substitution, sums of powers | [Roots of polynomial equations](#math.fm.roots) |
| 3 | 7 | Induction on a recurrence, then a deduction | [Proof by induction](#math.fm.induction) |
| 4 | 9 | Invariant points and lines, determinant and inverse | [Matrices as transformations](#math.fm.transform) (and [Matrices: algebra, determinants and inverses](#math.fm.matrices)) |
| 5 | 13 | A polar loop, area, intersection with a circle | [Polar coordinates](#math.fm.polar) |
| 6 | 16 | Plane, angle between planes, distance between skew lines | [Vectors: the vector product and planes](#math.fm.vectors) and [Vectors: intersections, angles and distances](#math.fm.vectors2) |
| 7 | 15 | Oblique asymptote, turning points, \(y^2 = f(x)\), an inequality | [Rational functions and their graphs](#math.fm.rational) and [Graphs related to y = f(x)](#math.fm.graphs) |

Next: [Mock Paper 2: Further Pure Mathematics 2](#math.fm.mock.p2)
