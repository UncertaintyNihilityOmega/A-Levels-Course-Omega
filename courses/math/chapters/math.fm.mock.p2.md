@chapter math.fm.mock.p2
@title Mock Paper 2: Further Pure Mathematics 2
@level mock
@paper CAIE 9231 Paper 2
@time 2 h
@summary A complete original mock for 9231 Paper 2 (Further Pure Mathematics 2): 8 questions, 75 marks, 2 hours, laid out like the real paper (marks 5, 7, 11, 8, 10, 10, 10, 14) and covering Maclaurin series, a reduction formula, hyperbolic integration and a first order differential equation, parametric differentiation and arc length, rectangles and bounds, a second order differential equation, roots of unity and eigenvalues. Full mark scheme with accepted alternatives; sit it in one go, mark yourself and see which chapters to revise.

:::why
Paper 2 is the A Level paper that builds on Paper 1: every question can use Paper 1 content as well as the Paper 2 topics, and several questions are a chain of "show that" and "hence" steps. The marks come from getting each given result honestly, so that the next part can use it. This mock has the same number of questions and the same spread of marks as the real paper, and every question is new. Do it under exam conditions first, then use the mark scheme to see where the method and accuracy marks are.
:::

:::exam Instructions
- Answer **all** questions. The total is **75 marks** and you have **2 hours**.
- You will need the list of formulae **MF19**: it gives the Maclaurin series, the hyperbolic identities, the logarithmic forms of the inverse hyperbolic functions and the standard derivatives and integrals, but not reduction formulae, the integrating factor, arc length, de Moivre's theorem or the matrix and vector results, which you must know. You should use a calculator where appropriate: only a scientific calculator, no graphical or symbolic algebra calculator.
- You must show all necessary working clearly; **no marks will be given for unsupported answers from a calculator**.
- Give non-exact numerical answers correct to **3 significant figures**, or **1 decimal place for angles in degrees**, unless the question says otherwise.
- The number of marks for each question or part question is shown in brackets [ ]. Roughly one and a half minutes per mark leaves a few minutes at the end.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [5 marks] (#math.fm.diff) Find the Maclaurin series for \(\cosh^{-1}(3 + x)\), up to and including the term in \(x^2\), giving your answer in the form \(\ln a + bx + cx^2\), where \(a\), \(b\) and \(c\) are exact constants.
A: Let \(f(x) = \cosh^{-1}(3 + x)\). Using the derivative of \(\cosh^{-1}\) from MF19,
\[f'(x) = \frac{1}{\sqrt{(3 + x)^2 - 1}}\]
[M1 A1]
Differentiate again, writing \(f'(x) = \left((3 + x)^2 - 1\right)^{-1/2}\):
\[f''(x) = -\frac{3 + x}{\left((3 + x)^2 - 1\right)^{3/2}}\]
[M1]
At \(x = 0\): \(f(0) = \cosh^{-1}3 = \ln\left(3 + \sqrt8\right) = \ln\left(3 + 2\sqrt2\right)\), \(f'(0) = \dfrac{1}{\sqrt8} = \dfrac{\sqrt2}{4}\) and \(f''(0) = -\dfrac{3}{8\sqrt8} = -\dfrac{3\sqrt2}{32}\). [A1] (the values at 0)
Use \(f(0) + xf'(0) + \dfrac{x^2}{2}f''(0)\):
\[\cosh^{-1}(3 + x) = \ln\left(3 + 2\sqrt2\right) + \frac{\sqrt2}{4}x - \frac{3\sqrt2}{64}x^2 + \cdots\]
[A1]
So \(a = 3 + 2\sqrt2\), \(b = \tfrac{\sqrt2}{4}\) and \(c = -\tfrac{3\sqrt2}{64}\).
:::

:::try
Q: [7 marks] (#math.fm.reduction) Let \(I_n = \displaystyle\int_0^{\pi/4}\sec^n x\,dx\), where \(n\) is a non-negative integer.

(a) By considering \(\dfrac{d}{dx}\left(\tan x\sec^{n-2}x\right)\), show that, for \(n \ge 2\),
\[(n - 1)I_n = \left(\sqrt2\right)^{n-2} + (n - 2)I_{n-2}.\]
[4]

(b) Find the exact value of \(I_6\). [3]
A: (a) Use the product rule and the chain rule:
\[\begin{aligned}\frac{d}{dx}\left(\tan x\sec^{n-2}x\right) &= \sec^2 x\sec^{n-2}x \\ &\quad + \tan x\,(n-2)\sec^{n-3}x\sec x\tan x \\ &= \sec^n x + (n-2)\tan^2 x\sec^{n-2}x\end{aligned}\]
[M1 A1]
Replace \(\tan^2 x\) by \(\sec^2 x - 1\):
\[\begin{aligned}&= \sec^n x + (n-2)\left(\sec^n x - \sec^{n-2}x\right) \\ &= (n-1)\sec^n x - (n-2)\sec^{n-2}x\end{aligned}\]
[M1]
Integrate from 0 to \(\tfrac14\pi\), where \(\tan\tfrac14\pi = 1\) and \(\sec\tfrac14\pi = \sqrt2\):
\[\left(\sqrt2\right)^{n-2} - 0 = (n-1)I_n - (n-2)I_{n-2}\]
which rearranges to the given result. [A1]

(b) With \(n = 2\): \(I_2 = \left(\sqrt2\right)^0 + 0 = 1\). [B1]
With \(n = 4\): \(3I_4 = \left(\sqrt2\right)^2 + 2I_2 = 4\), so \(I_4 = \tfrac43\). [M1]
With \(n = 6\): \(5I_6 = \left(\sqrt2\right)^4 + 4I_4 = 4 + \tfrac{16}{3} = \tfrac{28}{3}\), so \(I_6 = \dfrac{28}{15}\). [A1]
(check: \(\displaystyle\int\sec^6 x\,dx = \tan x + \tfrac23\tan^3 x + \tfrac15\tan^5 x\), which is \(1 + \tfrac23 + \tfrac15 = \tfrac{28}{15}\) at \(x = \tfrac14\pi\))
:::

:::try
Q: [11 marks] (#math.fm.integ) (a) Find the exact value of \(\displaystyle\int_0^1\frac{1}{\sqrt{x^2 + 2x + 5}}\,dx\), giving your answer in the form \(\ln k\). [4]

(b) Find the solution of the differential equation
\[\frac{dy}{dx} + y\tanh x = \cosh x\]
for which \(y = 1\) when \(x = 0\), giving \(y\) in terms of \(x\). [7]
A: (a) Complete the square: \(x^2 + 2x + 5 = (x + 1)^2 + 4\). [M1]
Use \(\displaystyle\int\frac{1}{\sqrt{x^2 + a^2}}\,dx = \sinh^{-1}\frac{x}{a}\) from MF19, with \(x + 1\) in place of \(x\) and \(a = 2\):
\[\int_0^1\frac{dx}{\sqrt{(x+1)^2 + 4}} = \left[\sinh^{-1}\frac{x+1}{2}\right]_0^1\]
[A1]
\[= \sinh^{-1}1 - \sinh^{-1}\tfrac12\]
[M1]
Use \(\sinh^{-1}x = \ln\left(x + \sqrt{x^2 + 1}\right)\):
\[= \ln\left(1 + \sqrt2\right) - \ln\frac{1 + \sqrt5}{2} = \ln\frac{2\left(1 + \sqrt2\right)}{1 + \sqrt5}\]
[A1]

(b) The integrating factor is \(e^{\int\tanh x\,dx}\). Write \(\tanh x = \dfrac{\sinh x}{\cosh x}\), where the numerator is the derivative of the denominator, so \(\displaystyle\int\tanh x\,dx = \ln\cosh x\) (this one is not in MF19). [M1]
So the integrating factor is \(e^{\ln\cosh x} = \cosh x\). [A1]
Multiply the equation by \(\cosh x\):
\[\frac{d}{dx}\left(y\cosh x\right) = \cosh^2 x\]
[M1]
Use \(\cosh^2 x = \tfrac12(1 + \cosh 2x)\) and integrate:
\[y\cosh x = \int\tfrac12(1 + \cosh 2x)\,dx\]
[M1]
\[y\cosh x = \tfrac12 x + \tfrac14\sinh 2x + c\]
[A1]
When \(x = 0\), \(y = 1\): \(1 \times 1 = 0 + 0 + c\), so \(c = 1\). [M1]
\[y = \frac{\tfrac12 x + \tfrac14\sinh 2x + 1}{\cosh x}\]
[A1]
:::

:::try
Q: [8 marks] (#math.fm.arclength) The curve \(C\) has parametric equations
\[x = t - \tanh t, \qquad y = \operatorname{sech}t, \qquad t \ge 0.\]
(a) Show that \(\dfrac{dy}{dx} = -\operatorname{cosech}t\). [3]

(b) Find the exact length of the arc of \(C\) from the point where \(t = 0\) to the point where \(t = \ln 2\). [5]
A: (a) Differentiate with respect to \(t\), using \(1 - \tanh^2 t = \operatorname{sech}^2 t\) and \(\operatorname{sech}t = (\cosh t)^{-1}\) (so \(\dfrac{d}{dt}\operatorname{sech}t = -\operatorname{sech}t\tanh t\)):
\[\frac{dx}{dt} = 1 - \operatorname{sech}^2 t = \tanh^2 t \qquad \frac{dy}{dt} = -\operatorname{sech}t\tanh t\]
[B1]
\[\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{-\operatorname{sech}t\tanh t}{\tanh^2 t}\]
[M1]
\[= -\frac{\operatorname{sech}t}{\tanh t} = -\frac{1}{\sinh t} = -\operatorname{cosech}t\]
[A1]

(b) The arc length is \(\displaystyle\int\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt\). Here
\[\begin{aligned}\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 &= \tanh^4 t + \operatorname{sech}^2 t\tanh^2 t \\ &= \tanh^2 t\left(\tanh^2 t + \operatorname{sech}^2 t\right)\end{aligned}\]
[M1]
\[= \tanh^2 t\]
[A1] (using \(\tanh^2 t + \operatorname{sech}^2 t = 1\))
So the integrand is \(\sqrt{\tanh^2 t} = \tanh t\), since \(\tanh t \ge 0\) for \(t \ge 0\). [A1]
\[\text{Length} = \int_0^{\ln 2}\tanh t\,dt\]
[M1]
\[= \left[\ln\cosh t\right]_0^{\ln 2} = \ln\frac54 - \ln 1 = \ln\frac54\]
since \(\cosh(\ln 2) = \tfrac12\left(2 + \tfrac12\right) = \tfrac54\). [A1]
:::

:::try
Q: [10 marks] (#math.fm.rectangles) (a) By sketching the graph of \(y = x^{-1/2}\) for \(x \ge 1\) and considering the areas of suitable rectangles of unit width, show that
\[\sum_{r=1}^{n}\frac{1}{\sqrt r} < 2\sqrt n - 1.\]
[5]

(b) Use a similar method to find, in terms of \(n\), a lower bound for \(\displaystyle\sum_{r=1}^{n}\frac{1}{\sqrt r}\). [3]

(c) Hence find lower and upper bounds, correct to 3 significant figures, for \(\displaystyle\sum_{r=1}^{10000}\frac{1}{\sqrt r}\). [2]
A: (a) The curve \(y = x^{-1/2}\) is decreasing. Draw rectangles of width 1 on the intervals \([r - 1, r]\) for \(r = 2, 3, \ldots, n\), each of height \(\dfrac{1}{\sqrt r}\) (the height at the right-hand end), so each rectangle lies below the curve. [B1]
The total area of these \(n - 1\) rectangles is \(\displaystyle\sum_{r=2}^{n}\frac{1}{\sqrt r}\). [M1]
This is less than the area under the curve from \(x = 1\) to \(x = n\):
\[\sum_{r=2}^{n}\frac{1}{\sqrt r} < \int_1^n x^{-1/2}\,dx\]
[M1]
\[\int_1^n x^{-1/2}\,dx = \left[2\sqrt x\right]_1^n = 2\sqrt n - 2\]
[A1]
Add the first term, \(\dfrac{1}{\sqrt1} = 1\), to both sides:
\[\sum_{r=1}^{n}\frac{1}{\sqrt r} < 2\sqrt n - 2 + 1 = 2\sqrt n - 1\]
[A1]

(b) This time draw rectangles of width 1 on \([r, r + 1]\) for \(r = 1, 2, \ldots, n\), each of height \(\dfrac{1}{\sqrt r}\) (the height at the left-hand end), so each rectangle lies above the curve. [M1]
The total area of the rectangles is greater than the area under the curve from \(x = 1\) to \(x = n + 1\):
\[\sum_{r=1}^{n}\frac{1}{\sqrt r} > \int_1^{n+1}x^{-1/2}\,dx\]
[A1]
\[\sum_{r=1}^{n}\frac{1}{\sqrt r} > 2\sqrt{n + 1} - 2\]
[A1]

(c) Put \(n = 10000\) in the results of (a) and (b): the upper bound is \(2 \times 100 - 1 = 199\) and the lower bound is \(2\sqrt{10001} - 2 = 198.01\). [M1]
So \(198 < \displaystyle\sum_{r=1}^{10000}\frac{1}{\sqrt r} < 199\) to 3 significant figures. [A1]
:::

:::try
Q: [10 marks] (#math.fm.de2) Find the solution of the differential equation
\[\frac{d^2x}{dt^2} + 4\frac{dx}{dt} + 13x = 30e^{-t},\]
given that \(x = 0\) and \(\dfrac{dx}{dt} = 0\) when \(t = 0\). Give \(x\) in terms of \(t\).
A: The auxiliary equation is \(m^2 + 4m + 13 = 0\). [M1]
\[m = \frac{-4 \pm \sqrt{16 - 52}}{2} = -2 \pm 3i\]
[A1]
The complementary function is \(x = e^{-2t}\left(A\cos 3t + B\sin 3t\right)\). [A1]
For a particular integral try \(x = ke^{-t}\), so \(\dfrac{dx}{dt} = -ke^{-t}\) and \(\dfrac{d^2x}{dt^2} = ke^{-t}\). Substituting,
\[k - 4k + 13k = 30\]
[M1]
\[10k = 30\quad\text{so}\quad k = 3\]
[A1]
The general solution is
\[x = e^{-2t}\left(A\cos 3t + B\sin 3t\right) + 3e^{-t}\]
[B1 FT]
When \(t = 0\), \(x = 0\): \(0 = A + 3\), so \(A = -3\). [M1 A1]
Differentiate (product rule for the first term):
\[\frac{dx}{dt} = e^{-2t}\left[-2(A\cos 3t + B\sin 3t) + (-3A\sin 3t + 3B\cos 3t)\right] - 3e^{-t}\]
When \(t = 0\), \(\dfrac{dx}{dt} = 0\): \(0 = -2A + 3B - 3\). With \(A = -3\) this gives \(3B = -3\), so \(B = -1\). [M1 A1]
\[x = 3e^{-t} - e^{-2t}\left(3\cos 3t + \sin 3t\right)\]
:::

:::try
Q: [10 marks] (#math.fm.complex2) (a) Solve the equation \(z^5 = 1\), giving the roots in the form \(e^{i\theta}\) where \(-\pi < \theta \le \pi\). [2]

(b) By considering the sum of the roots of the equation in (a), show that
\[\cos\tfrac25\pi + \cos\tfrac45\pi = -\tfrac12.\]
[3]

(c) Use the double angle formula to show that \(\cos\tfrac25\pi = \tfrac14\left(\sqrt5 - 1\right)\). [5]
A: (a) Write \(1 = e^{2k\pi i}\), so \(z^5 = e^{2k\pi i}\) and \(z = e^{2k\pi i/5}\). [M1]
The roots with \(-\pi < \theta \le \pi\) are \(k = 0, \pm1, \pm2\):
\[z = 1,\quad e^{\pm 2\pi i/5},\quad e^{\pm 4\pi i/5}\]
[A1]

(b) The equation \(z^5 - 1 = 0\) has no term in \(z^4\), so the sum of the roots is 0:
\[1 + e^{2\pi i/5} + e^{-2\pi i/5} + e^{4\pi i/5} + e^{-4\pi i/5} = 0\]
[M1]
Each conjugate pair gives \(e^{i\theta} + e^{-i\theta} = 2\cos\theta\): [M1]
\[1 + 2\cos\tfrac25\pi + 2\cos\tfrac45\pi = 0\]
so \(\cos\tfrac25\pi + \cos\tfrac45\pi = -\tfrac12\). [A1]

(c) Let \(c = \cos\tfrac25\pi\). The double angle formula gives \(\cos\tfrac45\pi = 2c^2 - 1\). [M1]
Substitute into (b):
\[\begin{aligned}c + 2c^2 - 1 &= -\tfrac12 \\ 4c^2 + 2c - 1 &= 0\end{aligned}\]
[A1]
\[c = \frac{-2 \pm \sqrt{4 + 16}}{8}\]
[M1]
\[c = \frac{-1 \pm \sqrt5}{4}\]
[A1]
Since \(\tfrac25\pi < \tfrac12\pi\), \(\cos\tfrac25\pi > 0\), so the negative root is rejected and \(\cos\tfrac25\pi = \tfrac14\left(\sqrt5 - 1\right)\). [A1]
:::

:::try
Q: [14 marks] (#math.fm.matrices2) The matrix \(\mathbf{A}\) is given by \(\mathbf{A} = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 0 & 1 \\ -2 & 2 & 1 \end{pmatrix}\).

(a) It is given that \(\lambda\) is an eigenvalue of \(\mathbf{A}\) with corresponding eigenvector \(\mathbf{e}\). Show that \(\mathbf{e}\) is an eigenvector of \(\mathbf{A}^2 - 2\mathbf{A}\), and state the corresponding eigenvalue. [2]

(b) Show that the eigenvalues of \(\mathbf{A}\) are \(-1\), \(1\) and \(2\). [2]

(c) Find a matrix \(\mathbf{P}\) and a diagonal matrix \(\mathbf{D}\) such that \(\mathbf{A}^2 - 2\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}\). [6]

(d) Use the characteristic equation of \(\mathbf{A}\) to show that \(\mathbf{A}^{-1} = a\mathbf{A}^2 + b\mathbf{A} + c\mathbf{I}\), where \(a\), \(b\) and \(c\) are constants to be determined. [4]
A: (a) \(\mathbf{A}\mathbf{e} = \lambda\mathbf{e}\), so \(\mathbf{A}^2\mathbf{e} = \mathbf{A}(\lambda\mathbf{e}) = \lambda\mathbf{A}\mathbf{e} = \lambda^2\mathbf{e}\). [M1]
\[\left(\mathbf{A}^2 - 2\mathbf{A}\right)\mathbf{e} = \lambda^2\mathbf{e} - 2\lambda\mathbf{e} = \left(\lambda^2 - 2\lambda\right)\mathbf{e}\]
So \(\mathbf{e}\) is an eigenvector with eigenvalue \(\lambda^2 - 2\lambda\). [A1]

(b) The characteristic equation is \(\det(\mathbf{A} - \lambda\mathbf{I}) = 0\). Expand along the first row:
\[\begin{aligned}\begin{vmatrix} 1 - \lambda & 1 & 1 \\ 2 & -\lambda & 1 \\ -2 & 2 & 1 - \lambda \end{vmatrix} &= (1 - \lambda)\left(\lambda^2 - \lambda - 2\right) \\ &\quad - (4 - 2\lambda) + (4 - 2\lambda)\end{aligned}\]
[M1]
\[= (1 - \lambda)(\lambda - 2)(\lambda + 1) = 0\]
so \(\lambda = -1\), \(1\) or \(2\). [A1]

(c) Find an eigenvector for each eigenvalue by solving \((\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}\): [M1]
\(\lambda = -1\): \(2x + y + z = 0\) (from rows 1 and 2) and \(-2x + 2y + 2z = 0\), so \(x = 0\) and \(y = -z\), giving \(\mathbf{e} = \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}\). [A1]
\(\lambda = 1\): \(y + z = 0\) and \(-2x + 2y = 0\), giving \(\mathbf{e} = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}\). [A1]
\(\lambda = 2\): \(-x + y + z = 0\) and \(2x - 2y + z = 0\), giving \(\mathbf{e} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}\). [A1]
(any non-zero multiples; check each with \(\mathbf{A}\mathbf{e} = \lambda\mathbf{e}\))
\[\mathbf{P} = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 1 & 1 \\ -1 & -1 & 0 \end{pmatrix}\]
[B1]
By (a) the eigenvalues of \(\mathbf{A}^2 - 2\mathbf{A}\) are \(\lambda^2 - 2\lambda\), which for \(\lambda = -1, 1, 2\) are \(3\), \(-1\) and \(0\). With the columns of \(\mathbf{P}\) in this order,
\[\mathbf{D} = \begin{pmatrix} 3 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}\]
[B1 FT]

(d) The characteristic equation \((\lambda + 1)(\lambda - 1)(\lambda - 2) = 0\) is \(\lambda^3 - 2\lambda^2 - \lambda + 2 = 0\). [M1]
By the Cayley–Hamilton theorem, a matrix satisfies its own characteristic equation:
\[\mathbf{A}^3 - 2\mathbf{A}^2 - \mathbf{A} + 2\mathbf{I} = \mathbf{0}\]
[A1]
Multiply by \(\mathbf{A}^{-1}\): [M1]
\[\mathbf{A}^2 - 2\mathbf{A} - \mathbf{I} + 2\mathbf{A}^{-1} = \mathbf{0}\]
\[\mathbf{A}^{-1} = -\tfrac12\mathbf{A}^2 + \mathbf{A} + \tfrac12\mathbf{I}\]
So \(a = -\tfrac12\), \(b = 1\), \(c = \tfrac12\). [A1]
:::

:::warn Where marks are usually lost on a paper like this
- **A given result you did not earn** (Questions 2(a) and 7(c)). "Show that" means every step between the start and the printed answer must appear; stating the answer after a line that does not lead to it scores no accuracy mark.
- **Forgetting the constant of integration or the condition** (Questions 3(b) and 6). Apply the initial conditions as soon as you have the general solution, and differentiate the product \(e^{-2t}(\ldots)\) with the product rule before you substitute \(t = 0\).
- **Bounds the wrong way round** (Question 5). A rectangle with its right-hand edge on a decreasing curve lies under the curve, so its area gives an upper bound for the sum when the first term is added back; check with \(n = 2\) before writing the inequality.
- **Eigenvectors that do not match the diagonal matrix** (Question 8(c)). The columns of \(\mathbf{P}\) and the entries of \(\mathbf{D}\) must be in the same order, and the entries of \(\mathbf{D}\) belong to the matrix in the question, not to \(\mathbf{A}\).
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 5 | Maclaurin series of an inverse hyperbolic function | [Further differentiation and Maclaurin series](#math.fm.diff) |
| 2 | 7 | Reduction formula for \(\int\sec^n x\,dx\) | [Reduction formulae](#math.fm.reduction) |
| 3 | 11 | Integral giving an inverse hyperbolic function; integrating factor with \(\tanh x\) | [Further integration: hyperbolic and inverse forms](#math.fm.integ) and [First order differential equations](#math.fm.de) |
| 4 | 8 | Parametric differentiation with hyperbolic functions; arc length | [Arc length and surface area](#math.fm.arclength) (and [Hyperbolic functions](#math.fm.hyperbolic)) |
| 5 | 10 | Rectangles to bound a sum | [Sums, rectangles and bounds](#math.fm.rectangles) |
| 6 | 10 | Second order differential equation with initial conditions | [Second order differential equations](#math.fm.de2) |
| 7 | 10 | Roots of unity, exact values of \(\cos\tfrac25\pi\) | [Roots of unity and complex series](#math.fm.complex2) (and [De Moivre's theorem and trigonometry](#math.fm.complex)) |
| 8 | 14 | Eigenvalues, diagonalisation, Cayley–Hamilton | [Eigenvalues and eigenvectors](#math.fm.matrices2) |
