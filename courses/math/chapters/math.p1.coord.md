@chapter math.p1.coord
@title Coordinate geometry: lines and circles
@level as
@paper CAIE P1 · Edexcel IAL P1–P2 · AQA/OCR/Edexcel Pure Year 1
@time 7–9 hours
@summary Distance, midpoint and gradient; the equation of a line in three forms; parallel and perpendicular lines and perpendicular bisectors; the equation of a circle, its centre and radius; tangents; and where a line meets a circle.

:::why
Coordinate geometry turns shapes into algebra, so a geometric question can be settled by solving an equation. It is a core Paper 1 topic, and it links to almost every other topic: tangents in calculus, quadratics and the discriminant, and vectors. The skills are simple to state, but exam answers lose marks through slips with signs and gradients, so the chapter shows each step.
:::

**Before you start**, you need gradient and \(y = mx + c\) from [Graphs and straight lines](#math.f.graphs), Pythagoras from [Geometry and trigonometry basics](#math.f.geometry) and quadratics from [Quadratics](#math.p1.quadratics). Write every answer in the form the question asks for.

## Distance, midpoint and gradient

Take two points \(A(x_1, y_1)\) and \(B(x_2, y_2)\). The horizontal step from \(A\) to \(B\) is \(x_2 - x_1\), and the vertical step is \(y_2 - y_1\). These are the two legs of a right-angled triangle whose hypotenuse is \(AB\). Pythagoras gives the distance, and the average of the coordinates gives the midpoint.

:::formula Distance, midpoint, gradient
For \(A(x_1, y_1)\) and \(B(x_2, y_2)\):
\[AB = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\]
\[\text{midpoint} = \left(\frac{x_1 + x_2}{2},\ \frac{y_1 + y_2}{2}\right) \qquad \text{gradient} = \frac{y_2 - y_1}{x_2 - x_1}\]
These are **not** on MF19. Learn them.
:::

:::eg Find the distance, midpoint and gradient of \(AB\) where \(A\) is \((-2, 1)\) and \(B\) is \((4, 5)\).
The steps are \(4 - (-2) = 6\) across and \(5 - 1 = 4\) up.
\[AB = \sqrt{6^2 + 4^2} = \sqrt{52} = 2\sqrt{13}\]
The midpoint is \(\left(\dfrac{-2 + 4}{2}, \dfrac{1 + 5}{2}\right) = (1, 3)\) and the gradient is \(\dfrac46 = \dfrac23\).
:::

Midpoints also run backwards. If \(M\) is the midpoint of \(AB\), then \(B\) is as far from \(M\) as \(A\) is, in the opposite direction.

:::eg \(M(3, 4)\) is the midpoint of \(AB\), and \(A\) is \((-1, 7)\). Find \(B\).
From \(A\) to \(M\) the steps are \(+4\) across and \(-3\) up. Repeat them from \(M\): \(B = (3 + 4, 4 - 3) = (7, 1)\). Check the midpoint: \(\left(\frac{-1 + 7}{2}, \frac{7 + 1}{2}\right) = (3, 4)\). ✓
:::

## The equation of a straight line

You already know \(y = mx + c\). It is useful when you know the gradient and the \(y\)-intercept. When you know the gradient and **any** point, the other two forms are quicker.

:::key Three forms of a line
- \(y = mx + c\): gradient \(m\), \(y\)-intercept \(c\).
- \(y - y_1 = m(x - x_1)\): gradient \(m\), passes through \((x_1, y_1)\). The \(y_1\) and \(x_1\) change sign inside the brackets.
- \(ax + by + c = 0\) with \(a\), \(b\), \(c\) integers: the general form. The gradient is \(-\dfrac{a}{b}\).
:::

To find a line through two points, find the gradient first, then put one of the points into the second form. When a question says "in the form \(ax + by + c = 0\)", clear fractions so that \(a\), \(b\), \(c\) are integers.

:::eg Find the equation of the line through \((3, -1)\) with gradient \(2\), and of the line through \(P(1, 5)\) and \(Q(4, -1)\). Give both in the form \(ax + by + c = 0\).
First line: \(y - (-1) = 2(x - 3)\), so \(y + 1 = 2x - 6\) and
\[2x - y - 7 = 0\]
Second line: the gradient is \(\dfrac{-1 - 5}{4 - 1} = -2\). Then \(y - 5 = -2(x - 1)\), so \(y = -2x + 7\) and
\[2x + y - 7 = 0\]
Check with \(Q\): \(2(4) + (-1) - 7 = 0\). ✓
:::

:::eg Find the gradient and \(y\)-intercept of \(3x + 4y = 12\), and the area of the triangle formed by the line and the axes.
Rearrange: \(4y = -3x + 12\), so \(y = -\tfrac34 x + 3\). The gradient is \(-\tfrac34\) and the \(y\)-intercept is \(3\). The line meets the \(x\)-axis where \(y = 0\), so \(3x = 12\) and \(x = 4\). The triangle has base \(4\) and height \(3\), so its area is \(\tfrac12 \times 4 \times 3 = 6\).
:::

## Parallel and perpendicular lines

Parallel lines have equal gradients. Perpendicular lines have gradients that multiply to \(-1\): turn the gradient upside down and change its sign.

:::key Parallel and perpendicular
- Parallel: \(m_1 = m_2\).
- Perpendicular: \(m_1 m_2 = -1\), so \(m_2 = -\dfrac{1}{m_1}\). A gradient of \(\tfrac23\) becomes \(-\tfrac32\), and a gradient of \(-4\) becomes \(\tfrac14\).
:::

:::eg Find the equation of the line through \((2, 5)\) that is perpendicular to \(3x + 4y = 12\).
The line \(3x + 4y = 12\) has gradient \(-\tfrac34\) (found above). The perpendicular gradient is \(\tfrac43\). Then
\[\begin{aligned} y - 5 &= \tfrac43 (x - 2) \\ 3y - 15 &= 4x - 8 \\ 4x - 3y + 7 &= 0 \end{aligned}\]
Check: at \((2, 5)\), \(8 - 15 + 7 = 0\). ✓
:::

:::def Perpendicular bisector
The line that passes through the midpoint of a line segment \(AB\) at right angles to \(AB\). Every point on it is the same distance from \(A\) as from \(B\).
:::

To find it you need two things: the midpoint, and the perpendicular gradient.

:::eg Find the equation of the perpendicular bisector of \(A(1, 2)\) and \(B(7, 6)\).
Midpoint: \(\left(\dfrac{1 + 7}{2}, \dfrac{2 + 6}{2}\right) = (4, 4)\). Gradient of \(AB\): \(\dfrac{6 - 2}{7 - 1} = \dfrac23\), so the perpendicular gradient is \(-\dfrac32\).
\[\begin{aligned} y - 4 &= -\tfrac32 (x - 4) \\ 2y - 8 &= -3x + 12 \\ 3x + 2y - 20 &= 0 \end{aligned}\]
Check: the midpoint \((4, 4)\) fits, as \(12 + 8 - 20 = 0\). ✓
:::

:::warn Gradient slips
Do not find the perpendicular gradient and then use the old gradient in the equation. Do not forget the minus sign when you flip: \(\tfrac23\) becomes \(-\tfrac32\), not \(\tfrac32\). When a point is substituted into \(y - y_1 = m(x - x_1)\), the signs of both coordinates flip: \((3, -1)\) gives \(y + 1 = m(x - 3)\).
:::

## Intersection of lines

Two lines meet at a point whose coordinates satisfy both equations, so solve them as simultaneous equations (see [Algebra from scratch](#math.f.algebra)). If the gradients are equal and the intercepts differ, the lines are parallel and never meet.

:::eg (Exam style) The points \(A(-2, 1)\) and \(B(6, 5)\) are given. (a) Find the equation of the perpendicular bisector of \(AB\). (b) The bisector meets the \(x\)-axis at \(C\). Find the coordinates of \(C\) and show that \(AC = BC\). (c) Find the area of triangle \(ABC\).
**(a)** The midpoint of \(AB\) is \(M(2, 3)\). [B1] The gradient of \(AB\) is \(\dfrac{5 - 1}{6 - (-2)} = \dfrac12\), so the perpendicular gradient is \(-2\). [M1]
\[y - 3 = -2(x - 2) \implies y = -2x + 7\] [A1]

**(b)** Put \(y = 0\): \(x = 3.5\), so \(C = (3.5, 0)\). [B1] Then
\[AC^2 = (3.5 + 2)^2 + 1^2 = 31.25 \qquad BC^2 = (6 - 3.5)^2 + 5^2 = 31.25\] [M1]
Since \(AC^2 = BC^2\), \(AC = BC\). [A1]

**(c)** \(AB = \sqrt{8^2 + 4^2} = \sqrt{80} = 4\sqrt5\) and \(CM = \sqrt{1.5^2 + 3^2} = \sqrt{11.25} = \tfrac32\sqrt5\). \(CM\) is perpendicular to \(AB\), so it is the height. [M1]
\[\text{Area} = \tfrac12 \times 4\sqrt5 \times \tfrac32\sqrt5 = 15\] [A1]
:::

## The equation of a circle

A circle is the set of all points at a fixed distance \(r\) (the **radius**) from a fixed point (the **centre**). If the centre is \((a, b)\) and \((x, y)\) is any point on the circle, the distance formula gives \(\sqrt{(x - a)^2 + (y - b)^2} = r\). Squaring both sides gives the equation.

:::key Equation of a circle
Centre \((a, b)\), radius \(r\):
\[(x - a)^2 + (y - b)^2 = r^2\]
Expanded: \(x^2 + y^2 + 2gx + 2fy + c = 0\), with centre \((-g, -f)\) and radius \(\sqrt{g^2 + f^2 - c}\). The \(x^2\) and \(y^2\) terms must have the same coefficient and there is no \(xy\) term. The circle equation is **not** on MF19.
:::

:::eg Write down the equation of the circle with centre \((3, -2)\) and radius \(5\), and expand it.
\[(x - 3)^2 + (y + 2)^2 = 25\]
The signs inside the brackets are the opposite of the centre's coordinates. Expanding: \(x^2 - 6x + 9 + y^2 + 4y + 4 = 25\), so
\[x^2 + y^2 - 6x + 4y - 12 = 0\]
:::

To go the other way, from the expanded form to the centre and radius, **complete the square** in \(x\) and in \(y\) (see [Quadratics](#math.p1.quadratics)). You can use the \(g\), \(f\) shortcut, but completing the square is safer under exam pressure.

:::eg Find the centre and radius of the circle \(x^2 + y^2 + 8x - 2y + 8 = 0\).
Group the \(x\) terms and the \(y\) terms and complete the square:
\[\begin{aligned} (x^2 + 8x) + (y^2 - 2y) + 8 &= 0 \\ (x + 4)^2 - 16 + (y - 1)^2 - 1 + 8 &= 0 \\ (x + 4)^2 + (y - 1)^2 &= 9 \end{aligned}\]
The centre is \((-4, 1)\) and the radius is \(3\).
:::

:::warn Circle slips
The centre has the **opposite** sign from the brackets: \((x + 4)^2\) means \(a = -4\). The right-hand side is \(r^2\), not \(r\): the radius of \((x - 1)^2 + (y - 2)^2 = 49\) is \(7\). If the right-hand side comes out negative or zero, there is no circle (or only a point).
:::

:::eg \(A(-1, 2)\) and \(B(5, -6)\) are the ends of a diameter of a circle. Find its equation.
The centre is the midpoint of \(AB\): \(\left(\dfrac{-1 + 5}{2}, \dfrac{2 - 6}{2}\right) = (2, -2)\). The radius is half the diameter: \(AB = \sqrt{6^2 + 8^2} = 10\), so \(r = 5\). The equation is
\[(x - 2)^2 + (y + 2)^2 = 25\]
:::

:::html
<figure class="fig"><svg viewBox="30 10 360 292" role="img" aria-label="A circle with centre C at (3, minus 2) and radius 5, with a tangent line touching it at P (6, 2). The radius CP is perpendicular to the tangent.">
<path class="ax" d="M40 120H340"/>
<path class="ax" d="M115 20V320"/>
<text class="tl ti" x="344" y="116">x</text>
<text class="tl ti" x="121" y="30">y</text>
<circle class="f1 s-acc sw2" cx="190" cy="170" r="125"/>
<path class="c2 thick" d="M205 25L340 126.25"/>
<path class="ln dash" d="M190 170L265 70"/>
<path class="ln thin" d="M256.6 81.2L267.8 89.6L276.2 78.4"/>
<circle class="fi" cx="190" cy="170" r="3.5"/>
<circle class="fi" cx="265" cy="70" r="3.5"/>
<text class="tl halo" x="198" y="190">C(3, −2)</text>
<text class="tl halo" x="276" y="62">P(6, 2)</text>
<text class="tl halo ta2" x="228" y="30">tangent</text>
</svg><figcaption>The tangent at \(P\) is perpendicular to the radius \(CP\). The radius has gradient \(\tfrac43\), so the tangent has gradient \(-\tfrac34\).</figcaption></figure>
:::

## Tangents and normals to a circle

:::def Tangent to a circle
A straight line that touches the circle at exactly one point, called the point of contact. It is perpendicular to the radius drawn to that point.
:::

The **normal** at the point is the line through the point and the centre.

:::steps
1. Check the point is on the circle (substitute its coordinates).
2. Find the gradient of the radius from the centre to the point.
3. The tangent gradient is the negative reciprocal.
4. Use \(y - y_1 = m(x - x_1)\) with the point of contact.
:::

:::eg Show that \(P(6, 2)\) lies on the circle \((x - 3)^2 + (y + 2)^2 = 25\) and find the equation of the tangent at \(P\).
\((6 - 3)^2 + (2 + 2)^2 = 9 + 16 = 25\), so \(P\) is on the circle. The centre is \(C(3, -2)\), so the radius \(CP\) has gradient \(\dfrac{2 - (-2)}{6 - 3} = \dfrac43\). The tangent has gradient \(-\tfrac34\):
\[\begin{aligned} y - 2 &= -\tfrac34 (x - 6) \\ 4y - 8 &= -3x + 18 \\ 3x + 4y - 26 &= 0 \end{aligned}\]
:::

:::tip Two other circle facts
The angle in a semicircle is a right angle, so for a diameter \(AB\) and a point \(C\) on the circle, the gradients of \(AC\) and \(BC\) multiply to \(-1\). A perpendicular from the centre to a chord meets the chord at its midpoint. Both are used in the next examples.
:::

:::eg \(A(-1, 2)\) and \(B(5, -6)\) are ends of a diameter of the circle \((x - 2)^2 + (y + 2)^2 = 25\). Show that \(C(6, 1)\) is on the circle and that angle \(ACB\) is a right angle.
\((6 - 2)^2 + (1 + 2)^2 = 16 + 9 = 25\), so \(C\) is on the circle. The gradient of \(AC\) is \(\dfrac{1 - 2}{6 - (-1)} = -\dfrac17\) and the gradient of \(BC\) is \(\dfrac{1 - (-6)}{6 - 5} = 7\). The product is \(-\tfrac17 \times 7 = -1\), so \(AC\) is perpendicular to \(BC\) and angle \(ACB = 90^\circ\).
:::

## Where a line meets a circle

Substitute the equation of the line into the equation of the circle. This gives a quadratic in one letter, and its discriminant \(b^2 - 4ac\) tells you the number of intersections (see [Quadratics](#math.p1.quadratics)).

:::key Line and circle
Substitute the line into the circle to get a quadratic.
- \(b^2 - 4ac > 0\): the line cuts the circle at two points.
- \(b^2 - 4ac = 0\): the line touches the circle: it is a **tangent**.
- \(b^2 - 4ac < 0\): the line misses the circle.
:::

:::eg Find the values of \(k\) for which the line \(y = x + k\) meets the circle \(x^2 + y^2 = 8\) at two points, is a tangent, or misses the circle.
Substitute \(y = x + k\): \(x^2 + (x + k)^2 = 8\), so
\[2x^2 + 2kx + k^2 - 8 = 0\]
The discriminant is \((2k)^2 - 4(2)(k^2 - 8) = 4k^2 - 8k^2 + 64 = 64 - 4k^2\).
- Two points: \(64 - 4k^2 > 0\), so \(k^2 < 16\) and \(-4 < k < 4\).
- Tangent: \(k = 4\) or \(k = -4\).
- Misses: \(k < -4\) or \(k > 4\).

Check: when \(k = 4\), \(x = -2\) and \(y = 2\), and \((-2)^2 + 2^2 = 8\). ✓
:::

:::eg (Exam style) The circle \(C\) has equation \(x^2 + y^2 - 6x + 4y - 12 = 0\). (a) Find the centre and radius of \(C\). (b) The line \(y = 2x - 3\) meets \(C\) at \(A\) and \(B\). Find the coordinates of \(A\) and \(B\), and the length \(AB\) in exact form.
**(a)** Complete the square:
\[(x - 3)^2 - 9 + (y + 2)^2 - 4 - 12 = 0 \implies (x - 3)^2 + (y + 2)^2 = 25\] [M1 A1]
The centre is \((3, -2)\) and the radius is \(5\). [A1]

**(b)** Substitute \(y = 2x - 3\): \((x - 3)^2 + (2x - 1)^2 = 25\). [M1]
\[\begin{aligned} x^2 - 6x + 9 + 4x^2 - 4x + 1 &= 25 \\ 5x^2 - 10x - 15 &= 0 \\ x^2 - 2x - 3 &= 0 \end{aligned}\] [A1]
So \((x - 3)(x + 1) = 0\), giving \(x = 3\) or \(x = -1\). The points are \(A(3, 3)\) and \(B(-1, -5)\). [A1]
\[AB = \sqrt{4^2 + 8^2} = \sqrt{80} = 4\sqrt5\] [A1]
Check: the midpoint of \(AB\) is \((1, -1)\). The line from the centre \((3, -2)\) to it has gradient \(-\tfrac12\), and \(-\tfrac12 \times 2 = -1\), so it is perpendicular to the chord, as it must be.
:::

## A circle through three points

Any three points that are not on a line lie on exactly one circle. The centre is equally far from all three, so it lies on the perpendicular bisector of each pair. Find two bisectors and solve them together.

:::eg Find the equation of the circle through \(A(6, 2)\), \(B(3, 3)\) and \(D(-2, -2)\).
Perpendicular bisector of \(AB\): midpoint \((4.5, 2.5)\); gradient of \(AB\) is \(\dfrac{3 - 2}{3 - 6} = -\tfrac13\), so the perpendicular gradient is \(3\). Then \(y - 2.5 = 3(x - 4.5)\), so \(y = 3x - 11\).

Perpendicular bisector of \(AD\): midpoint \((2, 0)\); gradient of \(AD\) is \(\dfrac{2 + 2}{6 + 2} = \tfrac12\), so the perpendicular gradient is \(-2\). Then \(y = -2(x - 2) = -2x + 4\).

The centre is where they meet: \(3x - 11 = -2x + 4\), so \(x = 3\) and \(y = -2\). The radius is the distance to \(A\): \(\sqrt{3^2 + 4^2} = 5\). The equation is \((x - 3)^2 + (y + 2)^2 = 25\). Check \(B\): \(0 + 25 = 25\). ✓
:::

:::exam Exam technique
- Write the **form** asked for (\(y = mx + c\) or \(ax + by + c = 0\)) and make sure \(a\), \(b\), \(c\) are integers if the question says so.
- "Show that" a point is on a circle: substitute and show both sides equal. "Show that" a line is a tangent: show the discriminant is zero (or the gradient of the radius times the gradient of the line is \(-1\)).
- Method marks go for the midpoint, the perpendicular gradient, and the substitution. Keep surds exact in lengths unless asked for decimals.
:::

:::board Other boards
Edexcel IAL has straight lines in P1 and circles in P2; the UK A Levels (AQA, Edexcel, OCR) include both in Pure Year 1. UK specifications usually give the circle only as \((x - a)^2 + (y - b)^2 = r^2\) and rely on completing the square for the expanded form. Parametric forms of lines and circles belong to later chapters in every board.
:::

:::try Start easy, finish at exam standard
Q: Find the distance and midpoint of \(A(-3, 4)\) and \(B(5, -2)\).
A: Steps \(8\) and \(-6\): \(AB = \sqrt{64 + 36} = 10\). Midpoint \((1, 1)\).
Q: Find the equation of the line through \((-2, 3)\) with gradient \(-\tfrac12\), in the form \(ax + by + c = 0\).
A: \(y - 3 = -\tfrac12 (x + 2)\), so \(2y - 6 = -x - 2\) and \(x + 2y - 4 = 0\).
Q: Find the equation of the line through \((1, -2)\) and \((5, 6)\).
A: Gradient \(= \dfrac{6 + 2}{5 - 1} = 2\). \(y + 2 = 2(x - 1)\), so \(y = 2x - 4\).
Q: Lines \(l_1: 2x + 3y = 6\) and \(l_2: kx - 6y = 5\) are parallel. Find \(k\), then find the line through \((3, 1)\) perpendicular to \(l_1\).
A: \(l_1\) has gradient \(-\tfrac23\) and \(l_2\) has gradient \(\tfrac{k}{6}\), so \(\tfrac k6 = -\tfrac23\) and \(k = -4\). The perpendicular gradient is \(\tfrac32\): \(y - 1 = \tfrac32 (x - 3)\), so \(3x - 2y - 7 = 0\).
Q: Find the equation of the perpendicular bisector of \(P(-1, 4)\) and \(Q(5, 0)\).
A: Midpoint \((2, 2)\); gradient of \(PQ\) is \(-\tfrac23\), so the perpendicular gradient is \(\tfrac32\). \(y - 2 = \tfrac32 (x - 2)\), which gives \(3x - 2y - 2 = 0\).
Q: Write down the equation of the circle with centre \((-1, 4)\) passing through \((2, 8)\).
A: \(r^2 = 3^2 + 4^2 = 25\), so \((x + 1)^2 + (y - 4)^2 = 25\).
Q: Find the centre and radius of \(x^2 + y^2 - 10x + 6y + 18 = 0\).
A: \((x - 5)^2 - 25 + (y + 3)^2 - 9 + 18 = 0\), so \((x - 5)^2 + (y + 3)^2 = 16\). Centre \((5, -3)\), radius \(4\).
Q: Show that the line \(y = x + 6\) is a tangent to the circle \(x^2 + y^2 = 18\), and find the point of contact.
A: \(x^2 + (x + 6)^2 = 18\), so \(2x^2 + 12x + 18 = 0\) and \(x^2 + 6x + 9 = 0\). The discriminant is \(36 - 36 = 0\), so the line is a tangent. Then \((x + 3)^2 = 0\), \(x = -3\), \(y = 3\): the point is \((-3, 3)\).
Q: Find the equation of the tangent to the circle \((x - 1)^2 + (y + 2)^2 = 20\) at \((3, 2)\).
A: Check: \(4 + 16 = 20\). ✓ The radius from \((1, -2)\) to \((3, 2)\) has gradient \(\tfrac42 = 2\), so the tangent gradient is \(-\tfrac12\). \(y - 2 = -\tfrac12 (x - 3)\), so \(x + 2y - 7 = 0\).
Q: (Exam style) The circle \(C\) has centre \((2, -1)\) and passes through \(A(5, 3)\). (a) Find the equation of \(C\). (b) Find the equation of the tangent at \(A\), in the form \(ax + by + c = 0\). (c) The tangent meets the \(x\)-axis at \(T\). Find the area of triangle \(CAT\).
A: (a) \(r^2 = 3^2 + 4^2 = 25\). [M1] \((x - 2)^2 + (y + 1)^2 = 25\). [A1]

(b) The gradient of \(CA\) is \(\tfrac43\), so the tangent gradient is \(-\tfrac34\). [M1] \(y - 3 = -\tfrac34 (x - 5)\), so \(4y - 12 = -3x + 15\) and \(3x + 4y - 27 = 0\). [A1]

(c) At \(y = 0\): \(x = 9\), so \(T = (9, 0)\). [B1] Triangle \(CAT\) is right-angled at \(A\). \(CA = 5\) and \(AT = \sqrt{4^2 + 3^2} = 5\). [M1] Area \(= \tfrac12 \times 5 \times 5 = 12.5\). [A1]
Q: (Exam style) Find the values of \(k\) for which the line \(y = kx + 5\) does not meet the circle \(x^2 + y^2 = 9\).
A: \(x^2 + (kx + 5)^2 = 9\) gives \((1 + k^2)x^2 + 10kx + 16 = 0\). [M1] No intersection needs \(100k^2 - 64(1 + k^2) < 0\). [M1] So \(36k^2 < 64\), \(k^2 < \tfrac{16}{9}\), and \(-\tfrac43 < k < \tfrac43\). [A1]
:::

:::quiz
? What is the gradient of a line perpendicular to \(2x - 5y = 10\)?
- \(\dfrac25\)
- \(-\dfrac25\)
+ \(-\dfrac52\)
- \(\dfrac52\)
> The line is \(y = \tfrac25 x - 2\), with gradient \(\tfrac25\). The perpendicular gradient is the negative reciprocal, \(-\tfrac52\). The option \(\tfrac25\) is the gradient of the original, \(-\tfrac25\) changes the sign only, and \(\tfrac52\) flips only.
? What are the centre and radius of \((x + 3)^2 + (y - 2)^2 = 49\)?
- centre \((3, -2)\), radius \(49\)
- centre \((-3, 2)\), radius \(49\)
- centre \((3, -2)\), radius \(7\)
+ centre \((-3, 2)\), radius \(7\)
> The centre has the opposite signs to the brackets, and the right-hand side is \(r^2\), so \(r = 7\). Two common slips are keeping the signs from the brackets and quoting \(r^2\) as the radius.
? The midpoint of \(AB\) is \((4, -1)\) and \(A\) is \((7, 3)\). What are the coordinates of \(B\)?
- \((5.5, 1)\)
- \((10, 7)\)
- \((11, 2)\)
+ \((1, -5)\)
> From \(A\) to the midpoint the change is \(-3\) across and \(-4\) up, so \(B = (4 - 3, -1 - 4) = (1, -5)\). Averaging \(A\) and the midpoint gives \((5.5, 1)\), which is not \(B\). Adding the coordinates gives \((11, 2)\), and stepping away from the midpoint in the wrong direction gives \((10, 7)\).
? The line \(y = 2x + k\) is a tangent to the circle \(x^2 + y^2 = 5\). What are the values of \(k\)?
- \(k = 5\) only
- \(k = \pm 1\)
+ \(k = \pm 5\)
- \(k = \pm\sqrt5\)
> Substituting gives \(5x^2 + 4kx + k^2 - 5 = 0\). The discriminant is \(16k^2 - 20(k^2 - 5) = 100 - 4k^2\), which is zero when \(k^2 = 25\), so \(k = \pm 5\). The value \(\sqrt5\) is the radius, which is not the same thing.
:::

:::recap
- Distance \(\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\); midpoint is the average of the coordinates; gradient is rise over run. None is on MF19.
- Line forms: \(y = mx + c\), \(y - y_1 = m(x - x_1)\), \(ax + by + c = 0\). Parallel: equal gradients. Perpendicular: \(m_1 m_2 = -1\).
- Perpendicular bisector: midpoint plus perpendicular gradient.
- Circle: \((x - a)^2 + (y - b)^2 = r^2\), centre \((a, b)\). From the expanded form, complete the square; the centre has the opposite signs to the brackets.
- Tangent \(\perp\) radius. Angle in a semicircle is \(90^\circ\). The perpendicular from the centre to a chord bisects the chord.
- Line and circle: substitute, then use the discriminant (two points, tangent, or miss).
- Circle through three points: two perpendicular bisectors meet at the centre.
:::

:::note Learn more online
- **Watch:** [Equation of a straight line](https://www.examsolutions.net/tutorials/equation-of-a-straight-line/) · ExamSolutions · y = mx + c from two points
- **Watch:** [Perpendicular bisector](https://www.examsolutions.net/tutorials/equation-perpendicular-bisector/) · ExamSolutions · a favourite step in circle questions
- **Practise:** [CAIE Pure 1 straight-line exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/coordinate-geometry/equation-of-a-straight-line/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Practise:** [CAIE Pure 1 circles exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/coordinate-geometry/circles/exam-questions/) · Save My Exams · tangents, chords and intersections *(some content paid)*
- **Explore:** [Circles](https://undergroundmathematics.org/circles) · Underground Mathematics · problems on circle geometry and equations
- **Explore:** [GeoGebra calculator](https://www.geogebra.org/calculator) · GeoGebra · plot a line and a circle and find where they meet

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Circular measure](#math.p1.circular).
