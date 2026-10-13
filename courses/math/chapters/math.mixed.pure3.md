@chapter math.mixed.pure3
@title Mixed practice: Pure 2 and 3
@level ref
@paper CAIE 9709 Papers 2 and 3 · Edexcel IAL P2, P3 and P4 · UK Pure Year 2
@time 3–4 hours
@summary Twenty-nine short questions that mix every topic of Pure 2 and Pure 3 (modulus and polynomials, logarithms, trigonometry, differentiation, integration, numerical methods, partial fractions, vectors, differential equations and complex numbers), ordered from ★ to ★★★. Each answer is a mark scheme, and each question names the chapter to revise.

:::why
Papers 2 and 3 sit on top of Paper 1, and their questions mix techniques inside a single answer: partial fractions then integration, a differential equation then a logarithm. Practising topics one at a time cannot train that. This page is mixed on purpose, so each question starts with the real task: working out which tools it needs.
:::

:::tip How to use this page
Do the questions in order, a few at a time, on paper. ★ questions are one idea (2 to 3 marks), ★★ questions are exam standard for one part of a Paper 2 or 3 question, ★★★ questions need two or more ideas together. A few ★★★ questions use content that is Paper 3 only (parts, substitution, vectors, differential equations, complex numbers); if you sit Paper 2 only, skip those and use the Revise links on the rest. Keep a list of the chapters that come up more than once: they are your weak spots.
:::

:::try Warm-up ★
Q: [2 marks] (#math.p3.logs) ★ Evaluate \(2\log_3 6 - \log_3 4\), giving your answer as an integer.
A: Use the power law and the subtraction law: \(\log_3 6^2 - \log_3 4 = \log_3\dfrac{36}{4}\). [M1]
\(\log_3 9 = 2\). [A1]
Q: [2 marks] (#math.p3.diff) ★ Differentiate \(y = e^{3x} + \ln(2x)\) with respect to \(x\).
A: \(\dfrac{d}{dx}e^{3x} = 3e^{3x}\). [B1]
\(\dfrac{d}{dx}\ln(2x) = \dfrac{1}{x}\). So \(\dfrac{dy}{dx} = 3e^{3x} + \dfrac1x\). [B1]
Q: [3 marks] (#math.p3.integ) ★ Find \(\displaystyle\int \Big(e^{2x} + \frac{1}{3x + 1}\Big)\,dx\).
A: \(\displaystyle\int e^{2x}\,dx = \tfrac12 e^{2x}\). [B1]
\(\displaystyle\int\frac{1}{3x + 1}\,dx = \tfrac13\ln|3x + 1|\). [B1]
The whole answer is \(\tfrac12 e^{2x} + \tfrac13\ln|3x + 1| + c\). [B1]
Q: [2 marks] (#math.p3.algebra) ★ Solve the equation \(|2x - 1| = 5\).
A: Either \(2x - 1 = 5\) or \(2x - 1 = -5\). [M1]
So \(x = 3\) or \(x = -2\). [A1]
Q: [3 marks] (#math.p3.complex) ★ The complex number \(z\) is \(3 + 4i\). Find \(|z|\) and \(\arg z\), giving the argument in radians correct to 3 significant figures.
A: \(|z| = \sqrt{3^2 + 4^2} = 5\). [B1]
The point \((3, 4)\) is in the first quadrant, so \(\arg z = \tan^{-1}\dfrac43\). [M1]
\(\arg z = 0.927\) radians. [A1]
Q: [2 marks] (#math.p3.vectors) ★ Find the magnitude of the vector \(\mathbf{a} = 2\mathbf{i} - 3\mathbf{j} + 6\mathbf{k}\).
A: \(|\mathbf{a}| = \sqrt{2^2 + (-3)^2 + 6^2}\) [M1] \(= \sqrt{49} = 7\). [A1]
Q: [3 marks] (#math.p3.trig) ★ Use the formula for \(\sin(A + B)\) to show that \(\sin 75^\circ = \dfrac{\sqrt{6} + \sqrt{2}}{4}\).
A: Write 75° as a sum of two standard angles:
\[ \begin{aligned} \sin 75^\circ &= \sin(45^\circ + 30^\circ) \\ &= \sin 45^\circ\cos 30^\circ \\ &\quad + \cos 45^\circ\sin 30^\circ \end{aligned} \]
[M1]
\[ = \frac{\sqrt2}{2}\times\frac{\sqrt3}{2} + \frac{\sqrt2}{2}\times\frac12 \]
[M1] \(= \dfrac{\sqrt6 + \sqrt2}{4}\). [A1]
Q: [2 marks] (#math.p3.numerical) ★ Show that the equation \(x^3 + x - 3 = 0\) has a root between \(x = 1\) and \(x = 2\).
A: Let \(f(x) = x^3 + x - 3\). Then \(f(1) = -1\) and \(f(2) = 7\). [M1]
The function is continuous and changes sign, so there is a root between 1 and 2. [A1]
:::

:::try Exam standard ★★
Q: [3 marks] (#math.p3.algebra) ★★ The polynomial \(f(x) = x^3 - 2x^2 + ax + 6\) leaves a remainder of 12 when divided by \((x - 3)\). Find the value of \(a\).
A: By the remainder theorem \(f(3) = 12\): [M1]
\(27 - 18 + 3a + 6 = 12\), so \(15 + 3a = 12\). [A1]
Hence \(a = -1\). [A1]
Q: [3 marks] (#math.p3.partial) ★★ Express \(\dfrac{5}{(x - 1)(x + 4)}\) in partial fractions.
A: Write \(\dfrac{5}{(x - 1)(x + 4)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 4}\), so \(5 = A(x + 4) + B(x - 1)\). [M1]
Put \(x = 1\): \(5 = 5A\), so \(A = 1\). [A1]
Put \(x = -4\): \(5 = -5B\), so \(B = -1\). [A1]
The answer is \(\dfrac{1}{x - 1} - \dfrac{1}{x + 4}\).
Q: [4 marks] (#math.p3.partial) ★★ Expand \((1 + 2x)^{-1/2}\) in ascending powers of \(x\), up to and including the term in \(x^2\), and state the set of values of \(x\) for which the expansion is valid.
A: Use \((1 + u)^{-1/2} = 1 - \tfrac12 u + \tfrac38 u^2 - \cdots\) with \(u = 2x\): [M1]
\[ 1 - \tfrac12(2x) + \tfrac38(2x)^2 = 1 - x + \tfrac32 x^2 \]
[A1] [A1] The expansion is valid for \(|2x| < 1\), that is \(|x| < \tfrac12\). [B1]
Q: [3 marks] (#math.p3.diff) ★★ Find the \(x\)-coordinates of the stationary points of the curve \(y = x^2 e^{-x}\).
A: Use the product rule: \(\dfrac{dy}{dx} = 2xe^{-x} - x^2e^{-x}\). [M1]
\(= x(2 - x)e^{-x}\). [A1]
Since \(e^{-x} > 0\), the derivative is zero when \(x = 0\) or \(x = 2\). [A1]
Q: [3 marks] (#math.p3.diff) ★★ Find the gradient of the curve \(y = \dfrac{x^2 + 1}{x - 2}\) at the point where \(x = 3\).
A: Use the quotient rule: \(\dfrac{dy}{dx} = \dfrac{2x(x - 2) - (x^2 + 1)}{(x - 2)^2}\). [M1]
\[ \frac{dy}{dx} = \frac{x^2 - 4x - 1}{(x - 2)^2} \]
[A1] At \(x = 3\): \(\dfrac{9 - 12 - 1}{1} = -4\). [A1]
Q: [5 marks] (#math.p3.trig) ★★ Solve the equation \(2\cos 2\theta + 3\sin\theta = 1\) for \(0^\circ \le \theta \le 360^\circ\).
A: Use \(\cos 2\theta = 1 - 2\sin^2\theta\): [M1]
\[ \begin{aligned} 2 - 4\sin^2\theta + 3\sin\theta &= 1 \\ 4\sin^2\theta - 3\sin\theta - 1 &= 0 \end{aligned} \]
[A1] Factorise: \((4\sin\theta + 1)(\sin\theta - 1) = 0\), so \(\sin\theta = -\tfrac14\) or \(\sin\theta = 1\). [M1]
\(\sin\theta = 1\) gives \(\theta = 90^\circ\). [A1]
\(\sin\theta = -\tfrac14\) gives \(\theta = 194.5^\circ\) or \(345.5^\circ\). [A1]
Q: [3 marks] (#math.p3.integ) ★★ Find the exact value of \(\displaystyle\int_0^{\pi/2}\sin^2x\,dx\).
A: Use \(\sin^2x = \tfrac12(1 - \cos 2x)\): [M1]
\[ \int_0^{\pi/2}\tfrac12(1 - \cos 2x)\,dx = \Big[\tfrac12 x - \tfrac14\sin 2x\Big]_0^{\pi/2} \]
[A1] \(= \tfrac{\pi}{4} - 0 = \tfrac{\pi}{4}\). [A1]
Q: [4 marks] (#math.p3.logs) ★★ Solve the equation \(5^{x+1} = 3^{2x}\), giving your answer correct to 3 significant figures.
A: Take logarithms of both sides: \((x + 1)\ln 5 = 2x\ln 3\). [M1] [A1]
Collect the terms in \(x\): \(x(2\ln 3 - \ln 5) = \ln 5\). [M1]
\[ x = \frac{\ln 5}{2\ln 3 - \ln 5} = 2.74 \]
[A1]
Q: [3 marks] (#math.p3.logs) ★★ The variables \(x\) and \(y\) satisfy \(y = Ae^{bx}\). The graph of \(\ln y\) against \(x\) is a straight line through the points \((0, 1.2)\) and \((2, 2.8)\). Find \(A\) and \(b\).
A: Taking logs: \(\ln y = \ln A + bx\), so the intercept is \(\ln A\) and the gradient is \(b\). [M1]
The gradient is \(\dfrac{2.8 - 1.2}{2 - 0} = 0.8\), so \(b = 0.8\). [A1]
The intercept is 1.2, so \(A = e^{1.2} = 3.32\). [A1]
Q: [3 marks] (#math.p3.complex) ★★ Express \(\dfrac{2 + 3i}{1 - i}\) in the form \(a + bi\).
A: Multiply the numerator and denominator by the conjugate \(1 + i\): [M1]
\[ \frac{(2 + 3i)(1 + i)}{(1 - i)(1 + i)} = \frac{2 + 2i + 3i - 3}{2} \]
[A1] \(= -\tfrac12 + \tfrac52 i\). [A1]
Q: [4 marks] (#math.p3.vectors) ★★ The points \(A\), \(B\) and \(C\) have position vectors \(2\mathbf{i} + \mathbf{j} - \mathbf{k}\), \(4\mathbf{i} - \mathbf{j}\) and \(3\mathbf{i} + 3\mathbf{j} + \mathbf{k}\). Find angle \(ABC\).
A: \(\overrightarrow{BA} = (-2, 2, -1)\) and \(\overrightarrow{BC} = (-1, 4, 1)\). [M1]
\(\overrightarrow{BA}\cdot\overrightarrow{BC} = 2 + 8 - 1 = 9\). [M1] [A1]
The magnitudes are \(|\overrightarrow{BA}| = 3\) and \(|\overrightarrow{BC}| = \sqrt{18}\), so \(\cos ABC = \dfrac{9}{3\sqrt{18}} = \dfrac{1}{\sqrt2}\) and angle \(ABC = 45^\circ\). [A1]
Q: [4 marks] (#math.p3.diffeq) ★★ Solve the differential equation \(\dfrac{dy}{dx} = 2xy\) given that \(y = 3\) when \(x = 0\).
A: Separate the variables: \(\displaystyle\int\frac{1}{y}\,dy = \int 2x\,dx\). [M1]
\(\ln y = x^2 + c\). [A1]
When \(x = 0\), \(y = 3\): \(c = \ln 3\). [M1]
So \(\ln y = x^2 + \ln 3\), that is \(y = 3e^{x^2}\). [A1]
Q: [3 marks] (#math.p3.numerical) ★★ The iterative formula \(x_{n+1} = \sqrt[3]{7 - x_n}\) is used to find a root of \(x^3 + x - 7 = 0\). Starting with \(x_1 = 1.5\), find the root correct to 3 significant figures, giving each iterate to 4 decimal places.
A: \(x_2 = \sqrt[3]{5.5} = 1.7652\), \(x_3 = 1.7363\), \(x_4 = 1.7395\). [M1] [A1]
\(x_5 = 1.7392\) and the values have settled, so the root is 1.74. [A1]
Q: [3 marks] (#math.p3.inttech) ★★ Find the exact value of \(\displaystyle\int_0^1\frac{x}{x^2 + 1}\,dx\).
A: The numerator is half the derivative of the denominator, so the integral has the form \(\dfrac{f'(x)}{f(x)}\): [M1]
\[ \int_0^1\frac{x}{x^2 + 1}\,dx = \Big[\tfrac12\ln(x^2 + 1)\Big]_0^1 \]
[A1] \(= \tfrac12\ln 2 - \tfrac12\ln 1 = \tfrac12\ln 2\). [A1]
:::

:::try Stretch ★★★
Q: [5 marks] (#math.p3.inttech) ★★★ Find the exact value of \(\displaystyle\int_0^1 xe^{2x}\,dx\).
A: Integrate by parts with \(u = x\) and \(\dfrac{dv}{dx} = e^{2x}\), so \(v = \tfrac12 e^{2x}\): [M1]
\[ \begin{aligned} \int_0^1 xe^{2x}\,dx &= \Big[\tfrac12 xe^{2x}\Big]_0^1 \\ &\quad - \int_0^1\tfrac12 e^{2x}\,dx \end{aligned} \]
[A1] The antiderivative is \(\tfrac12 xe^{2x} - \tfrac14 e^{2x}\). [A1]
Apply the limits: [M1]
\[ \Big(\tfrac12 e^2 - \tfrac14 e^2\Big) - \Big(0 - \tfrac14\Big) = \tfrac14(e^2 + 1) \]
[A1]
Q: [6 marks] (#math.p3.inttech) ★★★ Use the substitution \(u = x + 1\) to find the exact value of \(\displaystyle\int_0^3 x\sqrt{x + 1}\,dx\).
A: With \(u = x + 1\), \(x = u - 1\) and \(du = dx\). [B1]
When \(x = 0\), \(u = 1\); when \(x = 3\), \(u = 4\). The integrand becomes \((u - 1)\sqrt{u}\). [M1]
\[ \int_1^4 \big(u^{3/2} - u^{1/2}\big)\,du \]
[A1] \(= \Big[\tfrac25 u^{5/2} - \tfrac23 u^{3/2}\Big]_1^4\). [M1] [A1]
\[ \begin{aligned} &\Big(\tfrac{64}{5} - \tfrac{16}{3}\Big) - \Big(\tfrac25 - \tfrac23\Big) \\ &= \tfrac{112}{15} + \tfrac{4}{15} = \tfrac{116}{15} \end{aligned} \]
[A1]
Q: [4 marks] (#math.p3.complex) ★★★ Solve the equation \(z^2 = 5 - 12i\), giving your answers in the form \(a + bi\).
A: Let \(z = x + iy\). Then \(z^2 = x^2 - y^2 + 2xyi\), so \(x^2 - y^2 = 5\) and \(2xy = -12\). [M1] [A1]
From the second equation \(y = -\dfrac{6}{x}\). Substituting: \(x^4 - 5x^2 - 36 = 0\), so \((x^2 - 9)(x^2 + 4) = 0\). [M1]
For real \(x\), \(x^2 = 9\), so \(x = \pm 3\) and \(y = \mp 2\): \(z = 3 - 2i\) or \(z = -3 + 2i\). [A1]
Q: [6 marks] (#math.p3.diffeq) ★★★ A cup of tea cools in a room at 20 °C. Its temperature \(\theta\) °C at time \(t\) minutes satisfies \(\dfrac{d\theta}{dt} = -k(\theta - 20)\), where \(k\) is a positive constant. Initially \(\theta = 100\), and after 10 minutes \(\theta = 60\). Find the temperature after 20 minutes.
A: Separate the variables: \(\displaystyle\int\frac{1}{\theta - 20}\,d\theta = -k\int dt\). [M1]
\(\ln(\theta - 20) = -kt + c\). [A1]
When \(t = 0\), \(\theta - 20 = 80\), so \(\theta - 20 = 80e^{-kt}\). [A1]
When \(t = 10\): \(40 = 80e^{-10k}\), so \(e^{-10k} = \tfrac12\). [M1] [A1]
At \(t = 20\): \(\theta - 20 = 80\big(e^{-10k}\big)^2 = 80 \times \tfrac14 = 20\), so \(\theta = 40\) °C. [A1]
Q: [5 marks] (#math.p3.diff) ★★★ A curve has parametric equations \(x = t^2\), \(y = t^3 - 3t\). The tangent to the curve at the point where \(t = 2\) meets the \(y\)-axis at the point \(P\). Find the coordinates of \(P\).
A: \(\dfrac{dx}{dt} = 2t\) and \(\dfrac{dy}{dt} = 3t^2 - 3\), so \(\dfrac{dy}{dx} = \dfrac{3t^2 - 3}{2t}\). [M1]
At \(t = 2\) the gradient is \(\dfrac{9}{4}\). [A1]
The point is \((4, 8 - 6) = (4, 2)\). [B1]
The tangent is \(y - 2 = \tfrac94(x - 4)\); put \(x = 0\): [M1]
\(y = 2 - 9 = -7\), so \(P = (0, -7)\). [A1]
Q: [6 marks] (#math.p3.vectors) ★★★ The point \(P\) has position vector \(\mathbf{i} + 5\mathbf{j} + 2\mathbf{k}\). The line \(l\) has equation \(\mathbf{r} = \mathbf{j} + 2\mathbf{k} + t(\mathbf{i} + 2\mathbf{j} - \mathbf{k})\). Find the position vector of the foot of the perpendicular from \(P\) to \(l\), and the distance from \(P\) to \(l\).
A: A general point on \(l\) is \(F = (t,\ 1 + 2t,\ 2 - t)\). [M1]
\(\overrightarrow{PF} = (t - 1,\ 2t - 4,\ -t)\). For the perpendicular, \(\overrightarrow{PF}\) is perpendicular to the direction \((1, 2, -1)\): [M1]
\[ \begin{aligned} (t - 1) + 2(2t - 4) + t &= 0 \\ 6t - 9 &= 0 \\ t &= \tfrac32 \end{aligned} \]
[A1] The foot of the perpendicular is \(F = \tfrac32\mathbf{i} + 4\mathbf{j} + \tfrac12\mathbf{k}\). [A1]
\(\overrightarrow{PF} = (\tfrac12, -1, -\tfrac32)\), so the distance is \(|\overrightarrow{PF}|\): [M1]
\(\sqrt{\tfrac14 + 1 + \tfrac94} = \sqrt{3.5} = 1.87\). [A1]
Q: [6 marks] (#math.p3.trig) ★★★ (a) Express \(5\cos\theta - 12\sin\theta\) in the form \(R\cos(\theta + \alpha)\), where \(R > 0\) and \(0^\circ < \alpha < 90^\circ\). [3]

(b) Hence find the greatest and least values of \(\dfrac{1}{14 + 5\cos\theta - 12\sin\theta}\). [3]
A: (a) Expanding,
\[ \begin{aligned} R\cos(\theta + \alpha) &= R\cos\alpha\cos\theta \\ &\quad - R\sin\alpha\sin\theta \end{aligned} \]
so \(R\cos\alpha = 5\) and \(R\sin\alpha = 12\).
\(R = \sqrt{25 + 144} = 13\). [B1] \(\tan\alpha = \dfrac{12}{5}\). [M1] \(\alpha = 67.4^\circ\). [A1]

(b) The denominator is \(14 + 13\cos(\theta + \alpha)\), which takes every value from \(14 - 13 = 1\) to \(14 + 13 = 27\). [M1]
The expression is greatest when the denominator is least: the greatest value is \(\dfrac11 = 1\). [A1]
It is least when the denominator is greatest: the least value is \(\dfrac{1}{27}\). [A1]
:::
