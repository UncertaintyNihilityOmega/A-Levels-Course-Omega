@chapter math.mock.p3a
@title Mock paper: Pure 3 (A)
@level mock
@paper CAIE 9709 Paper 3 · Edexcel IAL P3 and P4 · UK Pure Year 2
@time 1 h 50 min
@summary A complete original mock for Paper 3 (Pure Mathematics 3): 11 questions, 75 marks, 1 hour 50 minutes, rising in difficulty, with a full mark scheme. Sit it in one go, then mark yourself and see which chapters to revise.

:::why
Paper 3 is the paper that decides the top grades in 9709: it carries the full A Level Pure content, and it is marked with 55% of the marks for application and communication. Questions here ask you to combine topics, so this mock mixes algebra, calculus, vectors and complex numbers the way the real paper does.
:::

:::exam Instructions
- Answer **all** questions. The total is **75 marks** and you have **1 hour 50 minutes**.
- You may use a scientific calculator and the MF19 formula booklet. Graphical calculators and calculators with symbolic algebra, differentiation or integration are **not** allowed.
- Show every step. A correct answer with no working may score no marks.
- Give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**, unless the question says otherwise.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [3 marks] (#math.p3.logs) Solve the equation \(\ln(2x + 1) - \ln x = 1\), giving your answer correct to 3 significant figures.
A: Combine the logarithms: \(\ln\dfrac{2x + 1}{x} = 1\). [M1]
Take exponentials of both sides: \(\dfrac{2x + 1}{x} = e\), so \(2x + 1 = ex\). [M1]
\[ \begin{aligned} x(e - 2) &= 1 \\ x &= \frac{1}{e - 2} = 1.39 \end{aligned} \]
[A1]
:::

:::try
Q: [4 marks] (#math.p3.partial) Expand \((2 - x)^{-2}\) in ascending powers of \(x\), up to and including the term in \(x^2\), and state the set of values of \(x\) for which the expansion is valid.
A: Take out the factor of 2: \((2 - x)^{-2} = 2^{-2}\big(1 - \tfrac{x}{2}\big)^{-2}\). [M1]
The expansion of \((1 + u)^{-2}\) is \(1 - 2u + 3u^2 + \cdots\), here with \(u = -\tfrac{x}{2}\): [M1]
\[ \begin{aligned} &\tfrac14\Big(1 + x + \tfrac34 x^2 + \cdots\Big) \\ &= \tfrac14 + \tfrac14 x + \tfrac{3}{16}x^2 + \cdots \end{aligned} \]
[A1] The expansion is valid when \(\big|\tfrac{x}{2}\big| < 1\), that is \(|x| < 2\). [A1]
:::

:::try
Q: [5 marks] (#math.p3.diff) A curve has equation \(x^2 + xy + y^2 = 7\). Find the gradient of the curve at the point \((1, 2)\).
A: Differentiate both sides with respect to \(x\), using the product rule for \(xy\) and the chain rule for \(y^2\): [M1]
\[ 2x + y + x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0 \]
[A1] Collect the terms in \(\dfrac{dy}{dx}\): \((x + 2y)\dfrac{dy}{dx} = -(2x + y)\). [M1]
\[ \frac{dy}{dx} = -\frac{2x + y}{x + 2y} \]
[A1] At \((1, 2)\) (which lies on the curve, since \(1 + 2 + 4 = 7\)) the gradient is \(-\dfrac{4}{5}\). [A1]
:::

:::try
Q: [6 marks] (#math.p3.trig) (a) Express \(3\sin\theta + 4\cos\theta\) in the form \(R\sin(\theta + \alpha)\), where \(R > 0\) and \(0^\circ < \alpha < 90^\circ\). [3]

(b) Hence solve \(3\sin\theta + 4\cos\theta = 2\) for \(0^\circ \le \theta \le 360^\circ\). [3]
A: (a) Expanding,
\[ \begin{aligned} R\sin(\theta + \alpha) &= R\cos\alpha\,\sin\theta \\ &\quad + R\sin\alpha\,\cos\theta \end{aligned} \]
so \(R\cos\alpha = 3\) and \(R\sin\alpha = 4\).
\(R = \sqrt{3^2 + 4^2} = 5\). [B1] \(\tan\alpha = \dfrac43\). [M1] So \(\alpha = 53.1^\circ\). [A1]

(b) The equation becomes \(5\sin(\theta + 53.13^\circ) = 2\), so \(\sin(\theta + 53.13^\circ) = 0.4\). [M1]
The values of \(\theta + 53.13^\circ\) between \(53.13^\circ\) and \(413.13^\circ\) are \(156.42^\circ\) and \(383.58^\circ\), because \(\sin^{-1}0.4 = 23.58^\circ\) and \(180^\circ - 23.58^\circ = 156.42^\circ\). So \(\theta = 103.3^\circ\) [A1] or \(\theta = 330.4^\circ\). [A1]
:::

:::try
Q: [5 marks] (#math.p3.inttech) Find the exact value of \(\displaystyle\int_1^e x^2\ln x\,dx\).
A: Integrate by parts with \(u = \ln x\) and \(\dfrac{dv}{dx} = x^2\), so \(\dfrac{du}{dx} = \dfrac1x\) and \(v = \tfrac13 x^3\): [M1]
\[ \begin{aligned} \int_1^e x^2\ln x\,dx &= \Big[\tfrac13 x^3\ln x\Big]_1^e \\ &\quad - \int_1^e \tfrac13 x^2\,dx \end{aligned} \]
[A1] The remaining integral is \(\tfrac19 x^3\), so the antiderivative is \(\tfrac13 x^3\ln x - \tfrac19 x^3\). [A1]
Apply the limits: [M1]
\[ \begin{aligned} &\Big(\tfrac13 e^3 - \tfrac19 e^3\Big) - \Big(0 - \tfrac19\Big) \\ &= \tfrac29 e^3 + \tfrac19 = \tfrac19(2e^3 + 1) \end{aligned} \]
[A1]
:::

:::try
Q: [7 marks] (#math.p3.diffeq) The depth of water in a tank at time \(t\) minutes is \(h\) metres. Water leaves the tank at a rate such that \(\dfrac{dh}{dt} = -k\sqrt{h}\), where \(k\) is a positive constant. Initially the depth is 9 m, and after 5 minutes it is 4 m.

(a) Solve the differential equation, to find a relationship between \(h\), \(t\) and \(k\). [3]

(b) Find the value of \(k\). [2]

(c) Find the time taken for the tank to empty. [2]
A: (a) Separate the variables: \(\displaystyle\int h^{-1/2}\,dh = -k\int dt\). [M1]
\[ 2\sqrt{h} = -kt + c \]
[A1] When \(t = 0\), \(h = 9\), so \(2 \times 3 = c\) and \(c = 6\): \(2\sqrt{h} = 6 - kt\). [A1]

(b) When \(t = 5\), \(h = 4\): \(2 \times 2 = 6 - 5k\). [M1] So \(5k = 2\) and \(k = 0.4\). [A1]

(c) The tank is empty when \(h = 0\): \(0 = 6 - 0.4t\). [M1] So \(t = 15\) minutes. [A1]
:::

:::try
Q: [6 marks] (#math.p3.inttech) Use the substitution \(u = 1 + \sqrt{x}\) to find the exact value of \(\displaystyle\int_0^4 \frac{1}{1 + \sqrt{x}}\,dx\).
A: From \(u = 1 + \sqrt{x}\) we get \(x = (u - 1)^2\), so \(\dfrac{dx}{du} = 2(u - 1)\). [B1]
When \(x = 0\), \(u = 1\); when \(x = 4\), \(u = 3\). [M1]
\[ \begin{aligned} \int_0^4 \frac{dx}{1 + \sqrt{x}} &= \int_1^3 \frac{2(u - 1)}{u}\,du \\ &= 2\int_1^3 \Big(1 - \frac1u\Big)du \end{aligned} \]
[A1] Integrating gives \(2\big[u - \ln u\big]_1^3\). [M1] [A1]
\[ 2\big[(3 - \ln 3) - (1 - 0)\big] = 4 - 2\ln 3 \]
[A1]
:::

:::try
Q: [8 marks] (#math.p3.complex) The complex number \(1 + i\) is a root of the cubic equation \(z^3 - 3z^2 + 4z - 2 = 0\).

(a) Write down another complex root and find the third root. [4]

(b) Express \(1 + i\) in the form \(re^{i\theta}\), where \(r > 0\) and \(-\pi < \theta \le \pi\). [2]

(c) Use your answer to part (b) to find \((1 + i)^8\). [2]
A: (a) The coefficients are real, so complex roots come in conjugate pairs: \(1 - i\) is also a root. [B1]
The quadratic with roots \(1 + i\) and \(1 - i\) is \((z - 1 - i)(z - 1 + i) = z^2 - 2z + 2\). [M1]
Divide the cubic by it:
\[ z^3 - 3z^2 + 4z - 2 = (z^2 - 2z + 2)(z - 1) \]
[M1]
So the third root is \(z = 1\). [A1]

(b) \(r = |1 + i| = \sqrt{2}\) [B1] and \(\theta = \arg(1 + i) = \dfrac{\pi}{4}\), so \(1 + i = \sqrt{2}\,e^{i\pi/4}\). [B1]

(c) \((1 + i)^8 = (\sqrt{2})^8\,e^{i\,8\pi/4} = 16e^{2\pi i}\). [M1]
Since \(e^{2\pi i} = 1\), \((1 + i)^8 = 16\). [A1]
:::

:::try
Q: [8 marks] (#math.p3.vectors) The line \(l_1\) has equation \(\mathbf{r} = \begin{pmatrix}1\\2\\-1\end{pmatrix} + \lambda\begin{pmatrix}2\\1\\3\end{pmatrix}\) and the line \(l_2\) has equation \(\mathbf{r} = \begin{pmatrix}2\\4\\1\end{pmatrix} + \mu\begin{pmatrix}1\\-1\\1\end{pmatrix}\).

(a) Show that the lines intersect and find the position vector of the point of intersection. [5]

(b) Find the acute angle between the lines. [3]
A: (a) Equating the three components: \(1 + 2\lambda = 2 + \mu\), \(2 + \lambda = 4 - \mu\) and \(-1 + 3\lambda = 1 + \mu\). [M1]
Adding the first two equations: \(3 + 3\lambda = 6\), so \(\lambda = 1\), and then \(\mu = 1\). [M1] [A1]
Check the third equation: \(-1 + 3 = 2\) and \(1 + 1 = 2\), so all three agree and the lines intersect. [A1]
Substituting \(\lambda = 1\) into \(l_1\): the position vector is \(3\mathbf{i} + 3\mathbf{j} + 2\mathbf{k}\). [A1]

(b) The direction vectors are \(\mathbf{d}_1 = (2, 1, 3)\) and \(\mathbf{d}_2 = (1, -1, 1)\), with \(\mathbf{d}_1\cdot\mathbf{d}_2 = 2 - 1 + 3 = 4\). [M1]
\[ \cos\theta = \frac{4}{\sqrt{14}\,\sqrt{3}} = \frac{4}{\sqrt{42}} \]
[A1] So \(\theta = 51.9^\circ\). [A1]
:::

:::try
Q: [12 marks] (#math.p3.partial) Let \(\mathrm{f}(x) = \dfrac{7x + 4}{(x + 2)(1 - 2x)}\).

(a) Express \(\mathrm{f}(x)\) in partial fractions. [4]

(b) Hence obtain the expansion of \(\mathrm{f}(x)\) in ascending powers of \(x\), up to and including the term in \(x^2\), and state the set of values of \(x\) for which the expansion is valid. [4]

(c) Find the exact value of \(\displaystyle\int_0^{1/4} \mathrm{f}(x)\,dx\), giving your answer in the form \(a\ln 2 + b\ln 3\). [4]
A: (a) Write \(\dfrac{7x + 4}{(x + 2)(1 - 2x)} = \dfrac{A}{x + 2} + \dfrac{B}{1 - 2x}\), so \(7x + 4 = A(1 - 2x) + B(x + 2)\). [M1]
Put \(x = -2\): \(-10 = 5A\), so \(A = -2\). [M1] [A1]
Put \(x = \tfrac12\): \(\tfrac{15}{2} = \tfrac52 B\), so \(B = 3\). [A1]
So \(\mathrm{f}(x) = -\dfrac{2}{x + 2} + \dfrac{3}{1 - 2x}\).

(b) Write the first fraction with a leading 1 in the bracket:
\[ -\frac{2}{x + 2} = -\big(1 + \tfrac{x}{2}\big)^{-1} = -\big(1 - \tfrac{x}{2} + \tfrac{x^2}{4} - \cdots\big) \]
[M1] Do the same for the second fraction:
\[ \frac{3}{1 - 2x} = 3(1 - 2x)^{-1} = 3\big(1 + 2x + 4x^2 + \cdots\big) \]
[A1]
Adding the two expansions: \(\mathrm{f}(x) = 2 + \tfrac{13}{2}x + \tfrac{47}{4}x^2 + \cdots\) [A1]
The first expansion needs \(|x| < 2\) and the second needs \(|x| < \tfrac12\), so both are valid when \(|x| < \tfrac12\). [B1]

(c) \(\displaystyle\int \mathrm{f}(x)\,dx = -2\ln(x + 2) - \tfrac32\ln(1 - 2x)\). [M1] [A1]
Apply the limits \(0\) and \(\tfrac14\): the value at \(\tfrac14\) is \(-2\ln\tfrac94 - \tfrac32\ln\tfrac12 = -4\ln 3 + \tfrac{11}{2}\ln 2\), and the value at 0 is \(-2\ln 2\). [M1]
\[ \int_0^{1/4}\mathrm{f}(x)\,dx = \tfrac{15}{2}\ln 2 - 4\ln 3 \]
[A1]
:::

:::try
Q: [11 marks] (#math.p3.numerical) The curve \(C\) has equation \(y = 2\tan^{-1}x - x\) for \(x \ge 0\).

(a) Find the \(x\)-coordinate of the stationary point of \(C\) and the exact value of the \(y\)-coordinate. [4]

(b) Show that the equation \(2\tan^{-1}x = x\) has a root between \(x = 2\) and \(x = 3\). [2]

(c) Use the iterative formula \(x_{n+1} = 2\tan^{-1}(x_n)\) with \(x_1 = 2.3\) to find this root correct to 3 significant figures, giving each iterate to 4 decimal places. [3]

(d) Find the exact value of \(\displaystyle\int_0^2 \frac{6}{4 + x^2}\,dx\). [2]
A: (a) \(\dfrac{dy}{dx} = \dfrac{2}{1 + x^2} - 1\). [M1] [A1]
Setting this to zero: \(1 + x^2 = 2\), so \(x = 1\) for \(x \ge 0\). [A1]
Then \(y = 2\tan^{-1}1 - 1 = \dfrac{\pi}{2} - 1\). [A1]

(b) Let \(g(x) = 2\tan^{-1}x - x\). Then \(g(2) = 0.214\) and \(g(3) = -0.502\). [M1] The sign changes and \(g\) is continuous, so there is a root between 2 and 3. [A1]

(c) The iterates are \(x_2 = 2.3213\), \(x_3 = 2.3281\), \(x_4 = 2.3302\), \(x_5 = 2.3308\) and \(x_6 = 2.3310\). [M1] [A1]
The iterates have settled at 2.33 to 3 s.f., so the root is 2.33. [A1]

(d) Use \(\displaystyle\int \frac{1}{a^2 + x^2}\,dx = \frac1a\tan^{-1}\frac{x}{a}\) with \(a = 2\): [M1]
\[ 6 \times \tfrac12\Big[\tan^{-1}\tfrac{x}{2}\Big]_0^2 = 3\tan^{-1}1 = \tfrac{3\pi}{4} \]
[A1]
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 3 | Laws of logarithms | [Logarithms and exponentials](#math.p3.logs) |
| 2 | 4 | Binomial series, rational index | [Partial fractions and the binomial series](#math.p3.partial) |
| 3 | 5 | Implicit differentiation | [Further differentiation](#math.p3.diff) |
| 4 | 6 | The form \(R\sin(\theta + \alpha)\) | [Further trigonometry](#math.p3.trig) |
| 5 | 5 | Integration by parts | [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech) |
| 6 | 7 | Separable differential equation | [Differential equations](#math.p3.diffeq) |
| 7 | 6 | Integration by substitution | [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech) |
| 8 | 8 | Cubic with complex roots, polar form | [Complex numbers](#math.p3.complex) |
| 9 | 8 | Lines in three dimensions | [Vectors](#math.p3.vectors) |
| 10 | 12 | Partial fractions, expansion, integration | [Partial fractions and the binomial series](#math.p3.partial) |
| 11 | 11 | \(\tan^{-1}x\), root-finding, \(\dfrac{1}{x^2 + a^2}\) | [Numerical solution of equations](#math.p3.numerical) and [Further differentiation](#math.p3.diff) |
