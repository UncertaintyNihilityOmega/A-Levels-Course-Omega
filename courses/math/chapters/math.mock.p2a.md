@chapter math.mock.p2a
@title Mock paper: Pure 2 (A)
@level mock
@paper CAIE 9709 Paper 2 · Edexcel IAL P2 · UK Pure Year 1 and 2
@time 1 h 15 min
@summary A complete original mock for Paper 2 (Pure Mathematics 2): 9 questions, 50 marks, 1 hour 15 minutes, rising in difficulty, with a full mark scheme. Sit it in one go, then mark yourself and see which chapters to revise.

:::why
Paper 2 is short and fast: 50 marks in 75 minutes is 1.5 minutes per mark, the same pace as Paper 1 but with less room to recover from a slow start. A timed mock is the best way to learn where your own minutes go.
:::

:::exam Instructions
- Answer **all** questions. The total is **50 marks** and you have **1 hour 15 minutes**.
- You may use a scientific calculator and the MF19 formula booklet. Graphical calculators and calculators with symbolic algebra, differentiation or integration are **not** allowed.
- Show every step. A correct answer with no working may score no marks.
- Give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**, unless the question says otherwise.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [3 marks] (#math.p3.logs) Solve the equation \(3^{2x+1} = 5\), giving your answer correct to 3 significant figures.
A: Take logarithms of both sides and bring down the power: \((2x + 1)\ln 3 = \ln 5\). [M1]
\[ 2x + 1 = \frac{\ln 5}{\ln 3} = 1.465\ldots \]
[A1] So \(x = 0.232\) (3 s.f.). [A1]
:::

:::try
Q: [4 marks] (#math.p3.algebra) Solve the inequality \(|x - 2| < 3|x + 1|\).
A: Both sides are non-negative, so square them: \((x - 2)^2 < 9(x + 1)^2\). [M1]
\[ x^2 - 4x + 4 < 9x^2 + 18x + 9 \quad\Rightarrow\quad 8x^2 + 22x + 5 > 0 \]
[A1] This factorises as \((4x + 1)(2x + 5) > 0\), with critical values \(x = -\tfrac14\) and \(x = -\tfrac52\). [M1]
The graph is ∪-shaped, so the solution is \(x < -\tfrac52\) or \(x > -\tfrac14\). [A1]
:::

:::try
Q: [4 marks] (#math.p3.algebra) The polynomial \(f(x) = 2x^3 + ax^2 - 7x + 6\) has \((x - 2)\) as a factor.

(a) Find the value of \(a\). [2]

(b) Find the remainder when \(f(x)\) is divided by \((x + 1)\). [2]
A: (a) By the factor theorem \(f(2) = 0\): \(16 + 4a - 14 + 6 = 0\). [M1] So \(4a = -8\) and \(a = -2\). [A1]

(b) By the remainder theorem the remainder is \(f(-1)\), with \(a = -2\): [M1]
\[ f(-1) = -2 - 2 + 7 + 6 = 9 \]
[A1]
:::

:::try
Q: [5 marks] (#math.p3.trig) Solve the equation \(2\sec^2\theta - 5\tan\theta - 5 = 0\) for \(0^\circ \le \theta \le 180^\circ\).
A: Use \(\sec^2\theta = 1 + \tan^2\theta\): [M1]
\[ 2 + 2\tan^2\theta - 5\tan\theta - 5 = 0 \quad\Rightarrow\quad 2\tan^2\theta - 5\tan\theta - 3 = 0 \]
[A1] This factorises as \((2\tan\theta + 1)(\tan\theta - 3) = 0\), so \(\tan\theta = -\tfrac12\) or \(\tan\theta = 3\). [M1]
\(\tan\theta = 3\) gives \(\theta = 71.6^\circ\). [A1]
\(\tan\theta = -\tfrac12\) gives \(\theta = 180^\circ - 26.6^\circ = 153.4^\circ\). [A1]
:::

:::try
Q: [5 marks] (#math.p3.logs) The variables \(x\) and \(y\) satisfy \(y = Kx^n\), where \(K\) and \(n\) are constants. The graph of \(\ln y\) against \(\ln x\) is a straight line passing through the points \((1, 2.5)\) and \((3, 6.5)\). Find the values of \(n\) and \(K\).
A: Taking natural logarithms: \(\ln y = n\ln x + \ln K\), so the graph has gradient \(n\) and intercept \(\ln K\). [M1]
The gradient is \(\dfrac{6.5 - 2.5}{3 - 1} = 2\), so \(n = 2\). [A1]
The line is \(\ln y - 2.5 = 2(\ln x - 1)\), so the intercept is \(2.5 - 2 = 0.5\). [M1] [A1]
So \(\ln K = 0.5\) and \(K = e^{0.5} = 1.65\) (3 s.f.). [A1]
:::

:::try
Q: [5 marks] (#math.p3.diff) A curve has parametric equations \(x = t^2 + 2t\), \(y = 3t - t^3\). Find the equation of the tangent to the curve at the point where \(t = 2\), giving your answer in the form \(ax + by = c\), where \(a\), \(b\) and \(c\) are integers.
A: \(\dfrac{dx}{dt} = 2t + 2\) and \(\dfrac{dy}{dt} = 3 - 3t^2\), so
\[ \frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3 - 3t^2}{2t + 2} \]
[M1] [A1] At \(t = 2\) the gradient is \(\dfrac{3 - 12}{6} = -\tfrac32\). The point is \(x = 4 + 4 = 8\), \(y = 6 - 8 = -2\), so \((8, -2)\). [B1]
The tangent is \(y + 2 = -\tfrac32(x - 8)\). [M1]
\[ 2y + 4 = -3x + 24 \quad\Rightarrow\quad 3x + 2y = 20 \]
[A1]
:::

:::try
Q: [5 marks] (#math.p3.integ) (a) Use the trapezium rule with 4 strips of equal width to estimate \(\displaystyle\int_0^2 \sqrt{1 + x^3}\,dx\), giving your answer correct to 3 significant figures. [3]

(b) The graph of \(y = \sqrt{1 + x^3}\) curves upwards (it is convex) between \(x = 0\) and \(x = 2\). State, with a reason, whether your answer to part (a) is an over-estimate or an under-estimate. [2]
A: (a) The strip width is \(h = 0.5\). The values of \(y\) at \(x = 0, 0.5, 1, 1.5, 2\) are \(1,\ 1.0607,\ 1.4142,\ 2.0917,\ 3\). [B1]
\[ \text{Estimate} = \tfrac12 \times 0.5\,\big[1 + 3 + 2(1.0607 + 1.4142 + 2.0917)\big] \]
[M1] \(= 0.25 \times 13.133 = 3.28\) (3 s.f.). [A1]

(b) The tops of the trapezia are chords of the curve, and for a curve that bends upwards each chord lies above the curve. [B1]
So the trapezia contain more area than lies under the curve: the answer is an over-estimate. [B1]
:::

:::try
Q: [8 marks] (#math.p3.numerical) (a) Show that the equation \(x^3 - 3x - 5 = 0\) has a root between 2 and 3. [2]

(b) Show that this equation can be written as \(x = \sqrt[3]{3x + 5}\). [1]

(c) Use the iterative formula \(x_{n+1} = \sqrt[3]{3x_n + 5}\) with \(x_1 = 2\) to find the root correct to 3 significant figures. Show the value of each iterate to 4 decimal places. [3]

(d) Confirm that your answer to part (c) is correct to 3 significant figures by considering a change of sign. [2]
A: (a) Let \(f(x) = x^3 - 3x - 5\). Then \(f(2) = 8 - 6 - 5 = -3\) and \(f(3) = 27 - 9 - 5 = 13\). [M1] The function is continuous and the sign changes, so there is a root between 2 and 3. [A1]

(b) Rearranging, \(x^3 = 3x + 5\), so \(x = \sqrt[3]{3x + 5}\). [B1]

(c) The iterates are \(x_2 = 2.2240\), \(x_3 = 2.2684\), \(x_4 = 2.2770\), \(x_5 = 2.2786\) and \(x_6 = 2.2789\). [M1] [A1]
The iterates have settled at 2.28 to 3 s.f., so the root is 2.28. [A1]

(d) Take \(f(2.275) = -0.0505\) and \(f(2.285) = 0.0755\). [M1] The sign changes, so the root lies in \((2.275, 2.285)\), which means it is 2.28 to 3 s.f. [A1]
:::

:::try
Q: [11 marks] (#math.p3.diff) The curve \(C\) has equation \(y = e^{2x} - 8e^x\).

(a) Find the \(x\)-coordinate of the point where \(C\) crosses the \(x\)-axis. [2]

(b) Find the exact coordinates of the stationary point of \(C\). [4]

(c) Determine the nature of this stationary point. [1]

(d) The region \(R\) is bounded by \(C\), the \(x\)-axis and the \(y\)-axis. Find the exact area of \(R\). [4]
A: (a) Put \(y = 0\): \(e^x(e^x - 8) = 0\). [M1] Since \(e^x > 0\), \(e^x = 8\) and \(x = \ln 8\). [A1]

(b) \(\dfrac{dy}{dx} = 2e^{2x} - 8e^x\). [M1] Setting this to zero, \(2e^x(e^x - 4) = 0\), so \(e^x = 4\) and \(x = \ln 4\). [A1]
Then \(y = 4^2 - 8 \times 4 = -16\), so the stationary point is \((\ln 4, -16)\). [M1] [A1]

(c) \(\dfrac{d^2y}{dx^2} = 4e^{2x} - 8e^x = 64 - 32 = 32 > 0\) at \(e^x = 4\), so it is a minimum. [B1]

(d) Between \(x = 0\) and \(x = \ln 8\) the curve is below the \(x\)-axis (at \(x = 0\), \(y = -7\)), so the area is minus the integral:
\[ \text{Area} = -\int_0^{\ln 8} (e^{2x} - 8e^x)\,dx = -\Big[\tfrac12 e^{2x} - 8e^x\Big]_0^{\ln 8} \]
[M1] [A1] At \(x = \ln 8\): \(\tfrac12 \times 64 - 64 = -32\). At \(x = 0\): \(\tfrac12 - 8 = -\tfrac{15}{2}\). [M1]
So the area is \(-\big(-32 + \tfrac{15}{2}\big) = \tfrac{49}{2}\). [A1]
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 3 | Equation with the unknown in an index | [Logarithms and exponentials](#math.p3.logs) |
| 2 | 4 | Modulus inequality | [Modulus and polynomials](#math.p3.algebra) |
| 3 | 4 | Factor and remainder theorems | [Modulus and polynomials](#math.p3.algebra) |
| 4 | 5 | Trigonometric equation with sec | [Further trigonometry](#math.p3.trig) |
| 5 | 5 | Reducing \(y = Kx^n\) to a straight line | [Logarithms and exponentials](#math.p3.logs) |
| 6 | 5 | Parametric differentiation, tangent | [Further differentiation](#math.p3.diff) |
| 7 | 5 | Trapezium rule | [Further integration](#math.p3.integ) |
| 8 | 8 | Locating a root, iteration | [Numerical solution of equations](#math.p3.numerical) |
| 9 | 11 | Exponential curve: stationary point, area | [Further differentiation](#math.p3.diff) and [Further integration](#math.p3.integ) |
