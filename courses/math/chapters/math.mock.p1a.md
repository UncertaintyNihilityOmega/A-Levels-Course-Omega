@chapter math.mock.p1a
@title Mock paper: Pure 1 (A)
@level mock
@paper CAIE 9709 Paper 1 · Edexcel IAL P1 · UK Pure Year 1
@time 1 h 50 min
@summary A complete original mock for Paper 1 (Pure Mathematics 1): 11 questions, 75 marks, 1 hour 50 minutes, rising in difficulty, with a full mark scheme. Sit it in one go, then mark yourself and see which chapters to revise.

:::why
A mock paper is the closest thing to the real exam that you can do at home. It tests the one thing that practice questions cannot: staying accurate for nearly two hours while you decide, question by question, how much time to spend. Treat it as the real thing and the result will tell you the truth.
:::

:::exam Instructions
- Answer **all** questions. The total is **75 marks** and you have **1 hour 50 minutes**, about 1.5 minutes per mark.
- You may use a scientific calculator and the MF19 formula booklet. Graphical calculators and calculators with symbolic algebra, differentiation or integration are **not** allowed.
- Show every step. A correct answer with no working may score no marks, and a calculator answer needs the working that led to it.
- Give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**, unless the question says otherwise. Angles in radians are not converted unless asked.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [3 marks] (#math.p1.series) Find the coefficient of \(x^2\) in the expansion of \((3 - 2x)^5\).
A: The term in \(x^2\) is \(\binom{5}{2}\,3^3\,(-2x)^2\). [M1] The binomial coefficient is \(\binom{5}{2} = 10\). [A1]
\[ 10 \times 27 \times 4 = 1080 \]
The coefficient is 1080. [A1]
:::

:::try
Q: [4 marks] (#math.p1.quadratics) Find the set of values of \(k\) for which the equation \(x^2 + 2kx + (k + 6) = 0\) has two distinct real roots.
A: Two distinct real roots need \(b^2 - 4ac > 0\): [M1]
\[ (2k)^2 - 4(k + 6) > 0 \quad\Rightarrow\quad k^2 - k - 6 > 0 \]
[A1] This factorises as \((k - 3)(k + 2) > 0\), so the critical values are \(k = -2\) and \(k = 3\). [M1]
The graph of \(k^2 - k - 6\) is ∪-shaped, so it is positive outside the roots: \(k < -2\) or \(k > 3\). [A1]
:::

:::try
Q: [5 marks] (#math.p1.trig) Solve the equation \(2\sin^2\theta + 3\cos\theta = 3\) for \(0^\circ \le \theta \le 360^\circ\).
A: Use \(\sin^2\theta = 1 - \cos^2\theta\): [M1]
\[ 2(1 - \cos^2\theta) + 3\cos\theta = 3 \quad\Rightarrow\quad 2\cos^2\theta - 3\cos\theta + 1 = 0 \]
[A1] This factorises as \((2\cos\theta - 1)(\cos\theta - 1) = 0\), so \(\cos\theta = \tfrac12\) or \(\cos\theta = 1\). [M1]
\(\cos\theta = \tfrac12\) gives \(\theta = 60^\circ\) or \(300^\circ\). [A1]
\(\cos\theta = 1\) gives \(\theta = 0^\circ\) or \(360^\circ\). [A1]
:::

:::try
Q: [3 marks] (#math.p1.series) The second term of an arithmetic progression is 8 and the sum of the first 12 terms is 258. Find the first term and the common difference.
A: Let the first term be \(a\) and the common difference \(d\). The second term gives \(a + d = 8\). [M1]
The sum gives \(\tfrac{12}{2}(2a + 11d) = 258\), so \(2a + 11d = 43\). [M1]
Subtract twice the first equation (\(2a + 2d = 16\)): \(9d = 27\), so \(d = 3\) and \(a = 5\). [A1]
:::

:::try
Q: [6 marks] (#math.p1.series) The first term of a geometric progression is 20 and its sum to infinity is 80.

(a) Find the common ratio. [2]

(b) Find the least value of \(n\) for which the sum of the first \(n\) terms exceeds 79. [4]
A: (a) \(S_\infty = \dfrac{a}{1 - r}\), so \(\dfrac{20}{1 - r} = 80\). [M1] Then \(1 - r = \tfrac14\), so \(r = \tfrac34\). [A1]

(b) The sum of \(n\) terms is
\[ S_n = \frac{20\big(1 - (3/4)^n\big)}{1 - 3/4} = 80\big(1 - (3/4)^n\big) \]
[M1]
We need \(80(1 - (3/4)^n) > 79\), which gives \((3/4)^n < \tfrac{1}{80}\). [M1]
Take logarithms; dividing by \(\ln(3/4)\), which is negative, reverses the inequality:
\[ n > \frac{\ln(1/80)}{\ln(3/4)} = \frac{\ln 80}{\ln(4/3)} = 15.2\ldots \]
[M1] The least integer is \(n = 16\). [A1]
:::

:::try
Q: [9 marks] (#math.p1.functions) The function \(f\) is defined by \(f(x) = 2x^2 - 12x + 6\) for \(x \ge k\).

(a) Express \(f(x)\) in the form \(a(x + b)^2 + c\). [3]

(b) State the smallest value of \(k\) for which \(f\) is one-one. [1]

(c) For this value of \(k\), find an expression for \(f^{-1}(x)\) and state the domain of \(f^{-1}\). [3]

(d) Find the coordinates of the point where the graphs of \(y = f(x)\) and \(y = f^{-1}(x)\) meet. [2]
A: (a) Take out the factor 2 from the terms in \(x\) and complete the square:
\[ 2x^2 - 12x + 6 = 2(x^2 - 6x) + 6 = 2\big[(x - 3)^2 - 9\big] + 6 \]
[M1] This is \(2(x - 3)^2 - 12\). So \(a = 2\), \(b = -3\) [A1] and \(c = -12\). [A1]

(b) The vertex is at \(x = 3\), so the smallest value is \(k = 3\). [B1]

(c) Let \(y = 2(x - 3)^2 - 12\) and make \(x\) the subject: \((x - 3)^2 = \dfrac{y + 12}{2}\). [M1] Since \(x \ge 3\) we take the positive root: \(f^{-1}(x) = 3 + \sqrt{\dfrac{x + 12}{2}}\). [A1]
The domain of \(f^{-1}\) is the range of \(f\): \(x \ge -12\). [B1]

(d) The graphs of \(f\) and \(f^{-1}\) meet on the line \(y = x\), so solve \(f(x) = x\): \(2x^2 - 13x + 6 = 0\), which factorises as \((2x - 1)(x - 6) = 0\). [M1]
We need \(x \ge 3\), so \(x = 6\) and the point is \((6, 6)\). [A1]
:::

:::try
Q: [8 marks] (#math.p1.coord) A circle has equation \(x^2 + y^2 - 6x + 4y - 12 = 0\).

(a) Find the coordinates of the centre and the radius of the circle. [3]

(b) Show that the point \(A(7, 1)\) lies on the circle. [1]

(c) Find the equation of the tangent to the circle at \(A\), giving your answer in the form \(ax + by + c = 0\), where \(a\), \(b\) and \(c\) are integers. [4]
A: (a) Complete the square in \(x\) and in \(y\): \((x - 3)^2 - 9 + (y + 2)^2 - 4 - 12 = 0\). [M1]
\[ (x - 3)^2 + (y + 2)^2 = 25 \]
The centre is \((3, -2)\) [A1] and the radius is 5. [A1]

(b) Substituting \(x = 7\), \(y = 1\): \(49 + 1 - 42 + 4 - 12 = 0\), so \(A\) lies on the circle. [B1]

(c) The gradient of the radius from \(C(3, -2)\) to \(A(7, 1)\) is \(\dfrac{1 - (-2)}{7 - 3} = \dfrac34\). [M1] [A1]
The tangent is perpendicular to the radius, so its gradient is \(-\tfrac43\). [M1]
\[ y - 1 = -\tfrac43(x - 7) \quad\Rightarrow\quad 3y - 3 = -4x + 28 \quad\Rightarrow\quad 4x + 3y - 31 = 0 \]
[A1]
:::

:::try
Q: [7 marks] (#math.p1.diff) A curve has equation \(y = 2x^3 - 9x^2 + 12x + 1\).

(a) Find the coordinates of the stationary points of the curve. [5]

(b) Determine the nature of each stationary point. [2]
A: (a) \(\dfrac{dy}{dx} = 6x^2 - 18x + 12\). [M1] [A1]
Set \(\dfrac{dy}{dx} = 0\): \(x^2 - 3x + 2 = 0\), so \((x - 1)(x - 2) = 0\) and \(x = 1\) or \(x = 2\). [M1]
When \(x = 1\), \(y = 2 - 9 + 12 + 1 = 6\). When \(x = 2\), \(y = 16 - 36 + 24 + 1 = 5\). The stationary points are \((1, 6)\) [A1] and \((2, 5)\). [A1]

(b) \(\dfrac{d^2y}{dx^2} = 12x - 18\). [M1] At \(x = 1\) it is \(-6 < 0\), so \((1, 6)\) is a maximum; at \(x = 2\) it is \(6 > 0\), so \((2, 5)\) is a minimum. [A1]
:::

:::try
Q: [9 marks] (#math.p1.circular) A circle has centre \(O\) and radius 6 cm. The chord \(AB\) cuts off a segment of the circle, and angle \(AOB = 2.2\) radians. (Work in radians throughout.)

(a) Find the length of the minor arc \(AB\). [2]

(b) Find the area of the segment bounded by the arc \(AB\) and the chord \(AB\). [4]

(c) Find the perimeter of this segment. [3]
A: (a) Arc length \(s = r\theta = 6 \times 2.2\) [M1] \(= 13.2\) cm. [A1]

(b) The area of the sector \(OAB\) is \(\tfrac12 r^2\theta = \tfrac12 \times 36 \times 2.2 = 39.6\) cm². [M1]
The area of the triangle \(OAB\) is \(\tfrac12 r^2 \sin\theta = 18\sin 2.2 = 14.55\ldots\) cm². [M1]
The segment is the sector minus the triangle: \(39.6 - 14.55\ldots\) [M1] \(= 25.0\) cm². [A1]

(c) The chord is \(AB = 2 \times 6 \times \sin 1.1 = 10.69\ldots\) cm (or by the cosine rule). [M1] [A1]
The perimeter is \(13.2 + 10.69\ldots = 23.9\) cm. [A1]
:::

:::try
Q: [10 marks] (#math.p1.diff) An open tank (it has no lid) is a cuboid with a square base of side \(x\) metres and height \(h\) metres. Its volume is 32 m³.

(a) Show that the total surface area \(A\) m² of the tank is given by \(A = x^2 + \dfrac{128}{x}\). [3]

(b) Find the value of \(x\) for which \(A\) is a minimum, and find this minimum area. [5]

(c) Justify that this value of \(A\) is a minimum. [2]
A: (a) The volume is \(x^2 h = 32\), so \(h = \dfrac{32}{x^2}\). [B1]
The area is the base plus four sides: \(A = x^2 + 4xh\). [M1]
\[ A = x^2 + 4x \times \frac{32}{x^2} = x^2 + \frac{128}{x} \]
[A1]

(b) Write \(A = x^2 + 128x^{-1}\), so \(\dfrac{dA}{dx} = 2x - 128x^{-2} = 2x - \dfrac{128}{x^2}\). [M1] [A1]
Setting \(\dfrac{dA}{dx} = 0\) gives \(x^3 = 64\), so \(x = 4\). [M1] [A1]
The minimum area is \(A = 16 + \dfrac{128}{4} = 48\) m². [A1]

(c) \(\dfrac{d^2A}{dx^2} = 2 + \dfrac{256}{x^3}\). [M1] At \(x = 4\) this is \(2 + 4 = 6 > 0\), so \(A\) is a minimum. [A1]
:::

:::try
Q: [11 marks] (#math.p1.integ) The curve \(y = x^2\) and the line \(y = 2x + 3\) intersect at two points. The region \(R\) is bounded by the curve and the line.

(a) Find the \(x\)-coordinates of the points of intersection. [3]

(b) Find the exact area of \(R\). [4]

(c) The region \(R\) is rotated through 360° about the \(x\)-axis. Find the volume of the solid formed, giving your answer correct to 3 significant figures. [4]
A: (a) Equate: \(x^2 = 2x + 3\), so \(x^2 - 2x - 3 = 0\). [M1] This factorises as \((x - 3)(x + 1) = 0\). [M1] So \(x = -1\) and \(x = 3\). [A1]

(b) The line is above the curve between the intersections, so
\[ \text{Area} = \int_{-1}^{3} (2x + 3 - x^2)\,dx = \Big[x^2 + 3x - \tfrac13 x^3\Big]_{-1}^{3} \]
[M1] [A1] The value at \(x = 3\) is \(9 + 9 - 9 = 9\), and at \(x = -1\) it is \(1 - 3 + \tfrac13 = -\tfrac53\). [M1] So the area is \(9 + \tfrac53 = \tfrac{32}{3}\). [A1]

(c) The volume is the volume from the line minus the volume from the curve:
\[ V = \pi\int_{-1}^{3} \big[(2x + 3)^2 - x^4\big]\,dx \]
[M1] Integrating, \(\displaystyle V = \pi\Big[\tfrac16(2x + 3)^3 - \tfrac15 x^5\Big]_{-1}^{3}\). [A1]
At \(x = 3\): \(\tfrac{729}{6} - \tfrac{243}{5} = 72.9\). At \(x = -1\): \(\tfrac16 + \tfrac15 = \tfrac{11}{30}\). [M1]
So \(V = \pi\big(72.9 - \tfrac{11}{30}\big) = \tfrac{1088}{15}\pi = 228\) (3 s.f.). [A1]
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 3 | Binomial expansion | [Series: binomial expansion and progressions](#math.p1.series) |
| 2 | 4 | Discriminant | [Quadratics](#math.p1.quadratics) |
| 3 | 5 | Trigonometric equation | [Trigonometry](#math.p1.trig) |
| 4 | 3 | Arithmetic progression | [Series: binomial expansion and progressions](#math.p1.series) |
| 5 | 6 | Geometric progression | [Series: binomial expansion and progressions](#math.p1.series) |
| 6 | 9 | Functions, inverse | [Functions](#math.p1.functions) |
| 7 | 8 | Circle and tangent | [Coordinate geometry: lines and circles](#math.p1.coord) |
| 8 | 7 | Stationary points | [Differentiation](#math.p1.diff) |
| 9 | 9 | Arc, sector, segment | [Circular measure](#math.p1.circular) |
| 10 | 10 | Optimisation | [Differentiation](#math.p1.diff) |
| 11 | 11 | Area and volume | [Integration](#math.p1.integ) |
