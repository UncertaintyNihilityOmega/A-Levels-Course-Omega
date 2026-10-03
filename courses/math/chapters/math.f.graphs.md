@chapter math.f.graphs
@title Graphs and straight lines
@level pre
@paper Prior knowledge for CAIE 9709 · Edexcel IAL · AQA/OCR/Edexcel (GCSE or IGCSE Algebra)
@time 5–6 hours
@summary Coordinates, gradient and the equation y = mx + c, sketching lines, recognising the shape of the standard curves, and finding where graphs meet.

:::why
A graph turns an equation into a picture, and many A Level questions are easier to see than to calculate. Every Pure topic uses graphs: you will sketch curves, read off roots, find tangents and compare areas. The straight line comes first because gradient, the steepness of a line, is the idea that differentiation extends to curves.
:::

**Before you start**, you need [Algebra from scratch](#math.f.algebra) and [Indices, surds and standard form](#math.f.powers). This chapter ends at the point where [Coordinate geometry](#math.p1.coord) begins.

## Coordinates and plotting

A point is located by its **coordinates** \((x, y)\): go \(x\) units along the horizontal axis (right if positive) and \(y\) units up the vertical axis (up if positive). The axes cross at the **origin** \(O(0, 0)\) and divide the plane into four quadrants. The point where a graph crosses the \(y\)-axis is the **\(y\)-intercept** (there \(x = 0\)). Where it crosses the \(x\)-axis the point is an **\(x\)-intercept** (there \(y = 0\)). The \(x\)-intercepts of a curve are its **roots**.

To plot a graph from its equation, make a table of values, plot the points and join them with a smooth curve (or a ruler for a straight line). On a calculator, or in the widget below, the machine does this for you, but in the exam you must be able to sketch the shape by hand.

:::def Sketch
A sketch shows the shape of a graph and labels the key features: where it crosses the axes, turning points and asymptotes if they exist. It does not need an accurate scale, but it must show the correct shape, and the labelled values must be right.
:::

## Gradient and straight lines

The **gradient** of a line measures how steep it is:

\[\text{gradient} = \frac{\text{change in } y}{\text{change in } x} = \frac{\text{rise}}{\text{run}}\]

:::key Gradient from two points
The line through \((x_1, y_1)\) and \((x_2, y_2)\) has gradient
\[m = \frac{y_2 - y_1}{x_2 - x_1}\]
A positive gradient goes up from left to right, a negative gradient goes down, a horizontal line has \(m = 0\), and a vertical line has no gradient (its equation is \(x = k\)). Parallel lines have equal gradients.
:::

:::plot The line through P(1, 3) and Q(5, 11): the rise is 8 for a run of 4, so the gradient is 2. The line meets the y-axis at (0, 1).
--f "2*x+1" --label "y = 2x + 1" --x -2 7 --y -3 13 --pt "1,3,P(1, 3)@se" --pt "5,11,Q(5, 11)@se" --pt "0,1,(0, 1)@se" --legend tl
:::

:::key The equation \(y = mx + c\)
Every straight line that is not vertical has an equation \(y = mx + c\), where \(m\) is the gradient and \(c\) is the \(y\)-intercept. Every point on the line has \(x\) and \(y\) that satisfy the equation.
:::

Use the widget to see how the two numbers control the line: change \(m\) to tilt it, and \(c\) to slide it up and down. Set \(m = 0\) for a horizontal line.

:::html
<div class="widget" data-w="graph" data-fns="m*x + c" data-x="-6,6" data-y="-6,6" data-params="m=1,-5,5,0.5; c=0,-5,5,0.5" data-labels="y = mx + c"></div>
:::

:::eg Find the gradient of the line through \(A(1, 3)\) and \(B(5, 11)\), and its equation.
\[m = \frac{11 - 3}{5 - 1} = \frac84 = 2\]
So the line is \(y = 2x + c\). The point \(A\) is on the line, so its coordinates fit: \(3 = 2(1) + c\), which gives \(c = 1\). The line is \(y = 2x + 1\).
Check with \(B\): \(2(5) + 1 = 11\). ✓
:::

:::eg State the gradient and \(y\)-intercept of (a) \(y = 5 - 3x\), (b) \(2y = 4x + 6\), (c) \(3x + 2y = 12\), and sketch (c).
(a) Rewrite as \(y = -3x + 5\): gradient \(-3\), intercept \(5\).

(b) Divide by 2 to get \(y = 2x + 3\): gradient \(2\), intercept \(3\).

(c) Rearrange: \(2y = 12 - 3x\), so \(y = -\tfrac32 x + 6\). The gradient is \(-\tfrac32\) and the \(y\)-intercept is \(6\). For the sketch find both intercepts: put \(x = 0\) to get \(y = 6\); put \(y = 0\) to get \(3x = 12\), so \(x = 4\). Draw a line through \((0, 6)\) and \((4, 0)\); it slopes down to the right.
:::

:::tip Sketching a line quickly
Put \(x = 0\) to find where it crosses the \(y\)-axis, then put \(y = 0\) to find where it crosses the \(x\)-axis. Two points fix a line, and the intercepts are the easiest two. For a line through the origin, such as \(y = 2x\), choose any other point.
:::

:::eg A taxi charges a fixed fee of $3 plus $2 for each kilometre. Write the cost \(C\) in terms of the distance \(d\) km, and say what the gradient and intercept mean.
\(C = 2d + 3\). The gradient \(2\) is the cost per kilometre (dollars per km). The intercept \(3\) is the cost for a journey of \(0\) km, which is the fixed fee. When \(d = 7.5\), \(C = 18\).
:::

Direct proportion (\(y = kx\)) gives a straight line through the origin. Equations of lines in other forms, perpendicular lines and the distance between points come in [Coordinate geometry](#math.p1.coord).

## The shapes of standard graphs

You need to recognise these graphs from their equations without a table of values. The shape matters most; each curve has one or two features to label.

| Equation | Name | Key features |
|---|---|---|
| \(y = x^2\) | quadratic | U-shaped, symmetric about the \(y\)-axis, minimum at \((0, 0)\). \(y = -x^2\) is upside down. |
| \(y = x^3\) | cubic | Rises from bottom left to top right through \((0, 0)\), flat for a moment at the origin. \(y = -x^3\) is the mirror image. |
| \(y = \dfrac{1}{x}\) | reciprocal | Two separate branches in opposite quadrants. It never touches either axis (the axes are **asymptotes**), and \(x = 0\) is not allowed. |
| \(y = \dfrac{1}{x^2}\) | reciprocal squared | Two branches, both above the \(x\)-axis, symmetric about the \(y\)-axis. |
| \(y = a^x\), \(a > 1\) | exponential growth | Passes through \((0, 1)\), rises faster and faster, never reaches the \(x\)-axis. |
| \(y = a^{-x}\) | exponential decay | Passes through \((0, 1)\), falls towards the \(x\)-axis from the left. |

:::def Asymptote
A line that a curve gets closer and closer to but never touches (or touches only for extreme values). For \(y = \dfrac1x\) the asymptotes are the two axes.
:::

:::plot The quadratic \(y = x^2\) and its reflection \(y = -x^2\) in the x-axis. Both pass through the origin, which is the turning point.
--f "x**2" --f "-(x**2)" --label "y = x²" --label "y = −x²" --x -3 3 --y -9 9 --legend tl
:::

:::plot The cubic \(y = x^3\) and \(y = -x^3\). Both pass through the origin and flatten briefly there.
--f "x**3" --f "-(x**3)" --label "y = x³" --label "y = −x³" --x -2.5 2.5 --y -12 12 --legend tl
:::

:::plot The reciprocal graphs \(y = 1/x\) and \(y = 1/x^2\). Neither crosses an axis, and neither is defined at x = 0.
--f "1/x" --f "1/x**2" --label "y = 1/x" --label "y = 1/x²" --x -4 4 --y -4 4 --legend tr
:::

:::plot Exponential growth \(y = 2^x\) and decay \(y = 2^{-x}\). Both pass through (0, 1) and never touch the x-axis.
--f "2**x" --f "2**(-x)" --label "y = 2ˣ" --label "y = 2⁻ˣ" --x -4 4 --y -1 10 --pt "0,1,(0, 1)@ne" --legend tr
:::

:::warn Curves are smooth
A quadratic is a smooth U, not a V, and the bottom is rounded, not flat. A reciprocal graph never crosses an axis, so do not let the branches touch it. Sketches that join the two branches of \(y = \tfrac1x\) across the \(y\)-axis lose the mark.
:::

## Where graphs meet

The point where two graphs cross has coordinates that fit **both** equations. So you find intersections by setting the two expressions for \(y\) equal and solving.

:::steps
1. Write both equations as \(y = \ldots\)
2. Set the right-hand sides equal and rearrange to \(0\) on one side.
3. Solve for \(x\) (the quadratic methods are in [Quadratics](#math.p1.quadratics)).
4. Substitute each \(x\) into the **simpler** equation to find \(y\). Write each answer as a point.
:::

:::plot The line y = x + 2 cuts the parabola y = x² at (−1, 1) and (2, 4), the two solutions of x² = x + 2.
--f "x**2" --f "x+2" --label "y = x²" --label "y = x + 2" --x -3 4 --y -2 10 --pt "-1,1,(−1, 1)@se" --pt "2,4,(2, 4)@se" --legend tl
:::

:::eg Solve \(x^2 = x + 2\) by graphs, and then algebraically.
Graph \(y = x^2\) and \(y = x + 2\) as in the figure. They meet where \(x = -1\) and \(x = 2\), so those are the solutions.

Algebraically: \(x^2 - x - 2 = 0\), so \((x - 2)(x + 1) = 0\) and \(x = 2\) or \(x = -1\). The two methods agree. ✓
:::

:::eg (Exam style) The line \(l\) passes through \(A(2, 5)\) and \(B(6, -3)\). (a) Find the equation of \(l\). (b) Find the coordinates of the points where \(l\) crosses the axes.
(a) Gradient \(= \dfrac{-3 - 5}{6 - 2} = -2\). [M1 A1] So \(y = -2x + c\). Using \(A\): \(5 = -2(2) + c\), so \(c = 9\). [M1]
\[y = -2x + 9\] [A1]
Check with \(B\): \(-2(6) + 9 = -3\). ✓

(b) On the \(y\)-axis \(x = 0\), giving \(y = 9\). On the \(x\)-axis \(y = 0\), giving \(2x = 9\) and \(x = 4.5\). [M1] The points are \((0, 9)\) and \((4.5, 0)\). [A1]
:::

:::eg (Exam style) Find the coordinates of the points where the line \(y = 2x + 3\) meets the curve \(y = x^2\).
Set the expressions equal: \(x^2 = 2x + 3\). [M1]
\[x^2 - 2x - 3 = 0\] [M1]
\[(x - 3)(x + 1) = 0 \implies x = 3 \text{ or } x = -1\] [A1]
Use the line to find \(y\): when \(x = 3\), \(y = 9\); when \(x = -1\), \(y = 1\). The points are \((3, 9)\) and \((-1, 1)\). [A1]
Check in the curve: \(3^2 = 9\) and \((-1)^2 = 1\). ✓
:::

:::exam Finding the second coordinate
After you find the \(x\)-values, the question asks for **coordinates**. A solution with only \(x\)-values loses the final mark. Substitute into the line (the simpler equation) and check in the curve.
:::

:::try Start easy, finish at exam standard
Q: Find the gradient of the line through (a) \((2, 1)\) and \((6, 9)\), (b) \((-1, 7)\) and \((3, 1)\).
A: (a) \(\dfrac{9 - 1}{6 - 2} = 2\). (b) \(\dfrac{1 - 7}{3 - (-1)} = \dfrac{-6}{4} = -\dfrac32\).
Q: Write down the gradient and \(y\)-intercept of (a) \(y = 4 - x\), (b) \(2y - 6x = 10\), (c) \(4x + 5y = 20\).
A: (a) gradient \(-1\), intercept \(4\). (b) \(y = 3x + 5\), so gradient \(3\), intercept \(5\). (c) \(y = -\tfrac45 x + 4\), so gradient \(-\tfrac45\), intercept \(4\).
Q: Find the equation of the line with gradient \(\tfrac12\) through the point \((4, 3)\).
A: \(y = \tfrac12 x + c\) and \(3 = 2 + c\), so \(c = 1\). The line is \(y = \tfrac12 x + 1\).
Q: Sketch \(5x - 2y = 10\), labelling the intercepts.
A: When \(x = 0\), \(y = -5\); when \(y = 0\), \(x = 2\). The line passes through \((0, -5)\) and \((2, 0)\) and slopes up to the right (gradient \(\tfrac52\)).
Q: Which of these lines are parallel? \(y = 3x + 1\), \(2y = 6x - 5\), \(y = -3x + 2\), \(3y = x + 4\).
A: Gradients: \(3\), \(3\), \(-3\), \(\tfrac13\). So \(y = 3x + 1\) and \(2y = 6x - 5\) are parallel.
Q: Sketch (a) \(y = -x^3\), (b) \(y = \dfrac{1}{x}\) and (c) \(y = 3^x\), stating one important feature of each.
A: (a) Falls from top left to bottom right through the origin. (b) Two branches in the first and third quadrants; the axes are asymptotes. (c) Rises from just above the \(x\)-axis on the left, through \((0, 1)\), faster and faster.
Q: A water tank holds 200 litres and loses water at a steady rate. After 4 minutes it holds 140 litres. Find \(V\) in terms of the time \(t\) minutes, and when the tank is empty.
A: Gradient \(= \dfrac{140 - 200}{4 - 0} = -15\) litres per minute, and \(V = 200 - 15t\). Empty when \(200 - 15t = 0\), so \(t = 13\tfrac13\) minutes.
Q: Find the points where the line \(y = x + 1\) meets the curve \(y = x^2 - 5\).
A: \(x^2 - 5 = x + 1\), so \(x^2 - x - 6 = 0\) and \((x - 3)(x + 2) = 0\). Then \(x = 3, y = 4\) or \(x = -2, y = -1\). The points are \((3, 4)\) and \((-2, -1)\).
Q: (Exam style) The line \(l\) is parallel to \(y = 3x - 1\) and passes through \(A(2, -5)\). (a) Find the equation of \(l\). (b) The line \(l\) meets the curve \(y = x^2 - 2x - 5\) at \(A\) and at a second point \(B\). Find the coordinates of \(B\).
A: (a) Parallel lines have the same gradient, 3. [B1] Then \(-5 = 3(2) + c\), so \(c = -11\). [M1] The line is \(y = 3x - 11\). [A1]

(b) \(x^2 - 2x - 5 = 3x - 11\), so \(x^2 - 5x + 6 = 0\). [M1] Then \((x - 2)(x - 3) = 0\). The root \(x = 2\) is point \(A\), so \(B\) has \(x = 3\) and \(y = 3(3) - 11 = -2\). [A1] \(B = (3, -2)\). Check in the curve: \(9 - 6 - 5 = -2\). ✓
:::

:::quiz
? What is the gradient of the line \(2y = 8 - 4x\)?
- \(-4\)
+ \(-2\)
- \(2\)
- \(4\)
> Divide by 2 first: \(y = 4 - 2x\), so the gradient is \(-2\). The gradient is the coefficient of \(x\) only after \(y\) is on its own with coefficient 1.
? The line through \((1, 2)\) and \((3, 8)\) has gradient
- \(\dfrac13\)
- \(\dfrac{10}{4}\)
+ \(3\)
- \(6\)
> \(m = \dfrac{8 - 2}{3 - 1} = 3\). Mixing up the order, for instance \(\dfrac{3 - 1}{8 - 2}\), gives \(\tfrac13\), and \(\dfrac{8 + 2}{3 + 1}\) adds instead of subtracting.
? Which equation could be the graph that has two branches, one in the first quadrant and one in the third?
- \(y = x^3\)
- \(y = \dfrac{1}{x^2}\)
+ \(y = \dfrac{1}{x}\)
- \(y = 2^x\)
> \(y = \tfrac1x\) is positive when \(x\) is positive and negative when \(x\) is negative, so its branches are in quadrants 1 and 3. \(y = \tfrac{1}{x^2}\) is always positive, so both branches are above the axis.
? The line \(y = x + 6\) meets the curve \(y = x^2\) where
- \(x = 6\) only
- \(x = -3\) and \(x = 2\)
+ \(x = 3\) and \(x = -2\)
- \(x = 1\) and \(x = -6\)
> \(x^2 = x + 6\) gives \(x^2 - x - 6 = 0\), so \((x - 3)(x + 2) = 0\). The signs in the factors are easy to swap: \(x = -3\) and \(x = 2\) come from \((x + 3)(x - 2) = x^2 + x - 6\), which is a different equation.
:::

:::recap
- Gradient \(m = \dfrac{y_2 - y_1}{x_2 - x_1}\); parallel lines have equal gradients; the equation is \(y = mx + c\).
- To find \(c\), substitute a point on the line. To sketch a line, find the two intercepts.
- Know the shapes of \(x^2\), \(x^3\), \(\dfrac1x\), \(\dfrac1{x^2}\), \(a^x\) and \(a^{-x}\), and their asymptotes and key points.
- Graphs meet where their \(y\)-values are equal: set the right-hand sides equal and solve. Then find the \(y\)-coordinates.
:::

:::links
- watch: [Equation of a line from a point and a gradient](https://www.examsolutions.net/tutorials/equation-of-a-line-given-the-gradient-and-point/) · ExamSolutions · the y − y₁ = m(x − x₁) form in action
- practise: [Algebra 1](https://www.khanacademy.org/math/algebra) · Khan Academy · units on linear equations and graphs
- explore: [Graphing Lines](https://phet.colorado.edu/en/simulations/graphing-lines) · PhET · drag a line and watch m and c change
- explore: [Graphing Quadratics](https://phet.colorado.edu/en/simulations/graphing-quadratics) · PhET · vertex, roots and axis of symmetry you can move
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot any graph from this chapter and test your sketches
- explore: [Geometry of Equations](https://undergroundmathematics.org/geometry-of-equations) · Underground Mathematics · connect equations to the shapes they draw

Links checked 3 October 2026.
:::
Next: [Geometry and trigonometry basics](#math.f.geometry).
