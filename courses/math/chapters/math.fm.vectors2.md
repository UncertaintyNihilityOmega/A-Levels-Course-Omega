@chapter math.fm.vectors2
@title Vectors: intersections, angles and distances
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary Lines and planes can meet, miss, be parallel or lie inside one another. You will decide which, find where a line meets a plane, drop a perpendicular from a point to a plane, find the angle between a line and a plane and between two planes, find the line where two planes meet, and find the shortest distance between two skew lines and the line that joins them at right angles.

:::why
Real objects are made of lines and planes: a laser beam hitting a mirror, a drone flying over a sloping roof, two pipes passing each other in a building, the ridge where two roof slopes meet. Every question an engineer asks about them (where, how steep, how close) is one of the questions in this chapter, and each is answered by the same few tools: the scalar product, the vector product and one equation to solve.
:::

**Before you start**, you need the equation of a plane in its three forms and the vector product from [Vectors: the vector product and planes](#math.fm.vectors), and lines, skew lines, angles and the foot of a perpendicular from [Vectors](#math.p3.vectors).

:::try Warm-up
Q: Find \((1, 2, 3) \times (2, 0, 1)\). (from [Vectors: the vector product and planes](#math.fm.vectors))
A: \(\mathbf{i}\): \(2 \times 1 - 3 \times 0 = 2\). \(\mathbf{j}\): \(3 \times 2 - 1 \times 1 = 5\). \(\mathbf{k}\): \(1 \times 0 - 2 \times 2 = -4\). The result is \((2, 5, -4)\).
Q: Find the Cartesian equation of the plane through \((1, 0, 2)\) with normal \(2\mathbf{i} - \mathbf{j} + 3\mathbf{k}\). (from [Vectors: the vector product and planes](#math.fm.vectors))
A: \(p = 2 - 0 + 6 = 8\), so \(2x - y + 3z = 8\).
Q: Find the acute angle between lines with directions \((1, 2, 2)\) and \((2, 2, 3)\). (from [Vectors](#math.p3.vectors))
A: The scalar product is \(2 + 4 + 6 = 12\), and the lengths are \(3\) and \(\sqrt{17}\). So \(\cos\theta = \dfrac{12}{3\sqrt{17}} = 0.970\) and \(\theta = 14.0^\circ\).
:::

## A line and a plane

A line and a plane in three dimensions have three possible relationships. The line can cut the plane at a single point, it can run parallel to the plane without touching it, or it can lie completely inside the plane.

:::key Line and plane
Let the line be \(\mathbf{r} = \mathbf{a} + t\mathbf{b}\) and the plane \(\mathbf{r}\cdot\mathbf{n} = p\).
1. Compute \(\mathbf{b}\cdot\mathbf{n}\). If it is **not zero**, the line meets the plane at exactly one point.
2. If \(\mathbf{b}\cdot\mathbf{n} = 0\), the line is parallel to the plane. Then test one point of the line: if \(\mathbf{a}\cdot\mathbf{n} = p\), the **line lies in the plane**; if not, the line is **parallel to the plane and does not meet it**.
:::

To find the meeting point, write the coordinates of a general point of the line in terms of \(t\), and substitute them into the Cartesian equation of the plane. This gives an equation in \(t\). One solution is one point; no solution is parallel; "0 = 0", true for every \(t\), is a line in the plane.

:::eg The line \(l\) has equation \(\mathbf{r} = \begin{pmatrix}1\\0\\2\end{pmatrix} + t\begin{pmatrix}2\\1\\-1\end{pmatrix}\) and the plane \(\Pi\) has equation \(3x + y - 2z = 8\). Find the point where \(l\) meets \(\Pi\).
A general point of \(l\) is \((1 + 2t,\ t,\ 2 - t)\). Substitute into the plane:
\[\begin{aligned}
3(1 + 2t) + t - 2(2 - t) &= 8 \\
3 + 6t + t - 4 + 2t &= 8 \\
9t - 1 &= 8
\end{aligned}\]
So \(t = 1\), and the point is \((3, 1, 1)\).

**Check** in the plane: \(9 + 1 - 2 = 8\). ✓ Also \(\mathbf{b}\cdot\mathbf{n} = 6 + 1 + 2 = 9 \ne 0\), as it must be for a single meeting point.
:::

:::eg The same line \(l\) is used with the planes \(\Pi_1: x + y + 3z = 7\) and \(\Pi_2: x + y + 3z = 10\). Decide how \(l\) and each plane are related.
Both planes have \(\mathbf{n} = (1, 1, 3)\), and \(\mathbf{b}\cdot\mathbf{n} = 2 + 1 - 3 = 0\), so \(l\) is parallel to both planes (or lies in one). Substitute \((1 + 2t,\ t,\ 2 - t)\) to see which:
\[\begin{aligned}
(1 + 2t) + t + 3(2 - t) &= 7 + 0 \times t \\
7 &= 7 \quad\text{for \(\Pi_1\)}
\end{aligned}\]
The \(t\) terms cancel and the equation is true for every \(t\): \(l\) lies in \(\Pi_1\). For \(\Pi_2\) the same working gives \(7 = 10\), which is never true: \(l\) is parallel to \(\Pi_2\) and does not meet it.
:::

:::warn Test with the dot product, not the cross product
A line is parallel to a plane when its direction is **perpendicular to the normal**: \(\mathbf{b}\cdot\mathbf{n} = 0\). A line with \(\mathbf{b} \times \mathbf{n} = \mathbf{0}\) is perpendicular to the plane, which is a different case. And "parallel" is only half the answer: say whether the line is in the plane or outside it.
:::

:::eg (Exam style) The line \(l\) has equation \(\mathbf{r} = \begin{pmatrix}2\\0\\-1\end{pmatrix} + t\begin{pmatrix}1\\2\\-1\end{pmatrix}\) and the plane \(\Pi\) has equation \(x - 2y + 3z = 5\). (a) Find the coordinates of the point where \(l\) meets \(\Pi\). (b) Find the acute angle between \(l\) and \(\Pi\).
**(a)** A general point of \(l\) is \((2 + t,\ 2t,\ -1 - t)\). [M1]
Substitute into the plane:
\[(2 + t) - 2(2t) + 3(-1 - t) = 5\] [M1]
\[-1 - 6t = 5, \quad t = -1\] [A1]
The point is \((1, -2, 0)\). [A1]

**(b)** The angle \(\varphi\) between a line and a plane comes from the formula developed in the next section, \(\sin\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\). Here \(\mathbf{b}\cdot\mathbf{n} = 1 - 4 - 3 = -6\), \(|\mathbf{b}| = \sqrt6\) and \(|\mathbf{n}| = \sqrt{14}\):
\[\sin\varphi = \frac{6}{\sqrt6\sqrt{14}}\] [M1]
\[= 0.6547\] [A1]
\[\varphi = 40.9^\circ\] [A1]
:::

## The foot of the perpendicular and the distance from a plane

The shortest distance from a point \(P\) to a plane is along the line through \(P\) perpendicular to the plane. That line has direction \(\mathbf{n}\), the normal, so it is easy to write down. Where it meets the plane is the **foot of the perpendicular**.

:::def Foot of the perpendicular
The **foot of the perpendicular** from a point \(P\) to a plane is the point \(F\) of the plane for which \(PF\) is perpendicular to the plane. The length \(PF\) is the shortest distance from \(P\) to the plane, called the perpendicular distance.
:::

:::steps
1. Write the line through \(P\) with direction \(\mathbf{n}\): \(\mathbf{r} = \mathbf{p} + t\mathbf{n}\).
2. Substitute its coordinates into the equation of the plane and solve for \(t\).
3. Put \(t\) back to get the foot \(F\). The distance is \(PF = |t||\mathbf{n}|\).
4. For the **reflection** of \(P\) in the plane, go twice as far: the image is \(\mathbf{p} + 2t\mathbf{n}\), so that \(F\) is the midpoint of \(P\) and its image.
:::

Doing this once with letters gives a formula for the distance that is quick when only the distance is wanted. It is not on MF19, so it is worth deriving to see where it comes from.

:::eg Derive the distance of the point \(P(x_1, y_1, z_1)\) from the plane \(ax + by + cz = d\).
Let \(\mathbf{n} = (a, b, c)\) and \(\mathbf{p} = (x_1, y_1, z_1)\). The perpendicular through \(P\) is \(\mathbf{r} = \mathbf{p} + t\mathbf{n}\), with coordinates \((x_1 + ta,\ y_1 + tb,\ z_1 + tc)\). It meets the plane when
\[\begin{aligned}
a(x_1 + ta) + b(y_1 + tb) + c(z_1 + tc) &= d \\
(ax_1 + by_1 + cz_1) + t(a^2 + b^2 + c^2) &= d \\
t &= \frac{d - (ax_1 + by_1 + cz_1)}{a^2 + b^2 + c^2}
\end{aligned}\]
The distance from \(P\) to the foot is \(|t||\mathbf{n}|\), and \(|\mathbf{n}|^2 = a^2 + b^2 + c^2\), so
\[PF = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}\]
:::

:::key Distance from a point to a plane
The distance of \(P(x_1, y_1, z_1)\) from the plane \(ax + by + cz = d\) is
\[\frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}\]
In vector form, for the plane \(\mathbf{r}\cdot\mathbf{n} = p\), it is \(\dfrac{|\mathbf{p}\cdot\mathbf{n} - p|}{|\mathbf{n}|}\). The sign of the number inside the modulus tells you which side of the plane \(P\) is on.
:::

:::eg Find the foot of the perpendicular from \(P(3, -1, 4)\) to the plane \(2x + 3y - z = -8\), the distance of \(P\) from the plane, and the reflection of \(P\) in the plane.
The normal is \((2, 3, -1)\). The perpendicular is \(\mathbf{r} = (3, -1, 4) + t(2, 3, -1)\), with general point \((3 + 2t,\ -1 + 3t,\ 4 - t)\). Substitute:
\[\begin{aligned}
2(3 + 2t) + 3(-1 + 3t) - (4 - t) &= -8 \\
6 + 4t - 3 + 9t - 4 + t &= -8 \\
14t - 1 &= -8
\end{aligned}\]
So \(t = -\tfrac12\), and the foot is \(F = \left(3 - 1,\ -1 - \tfrac32,\ 4 + \tfrac12\right) = (2, -2.5, 4.5)\).

The distance is \(|t||\mathbf{n}| = \tfrac12\sqrt{14} = 1.87\) (3 s.f.). The formula agrees: \(\dfrac{|6 - 3 - 4 + 8|}{\sqrt{14}} = \dfrac{7}{\sqrt{14}} = 1.87\).

The reflection goes twice as far: \(\mathbf{p} + 2t\mathbf{n} = (3, -1, 4) - (2, 3, -1) = (1, -4, 5)\). **Check**: the midpoint of \((3, -1, 4)\) and \((1, -4, 5)\) is \((2, -2.5, 4.5) = F\). ✓
:::

The distance from a point to a plane gives the distance between two **parallel** planes: take any point of one plane and find its distance from the other. The planes \(2x + 3y - z = -8\) and \(2x + 3y - z = 5\) are a distance \(\dfrac{|{-8} - 5|}{\sqrt{14}} = \dfrac{13}{\sqrt{14}} = 3.47\) apart, because the difference of the constants over \(|\mathbf{n}|\) is all that matters. It also gives the distance between a line and a plane parallel to it, using any point of the line.

:::eg A drone is at the point \(D(3, 3, 8)\), with coordinates in metres and \(z\) the height. A roof is the plane \(2z - y = 6\). Find the shortest distance from the drone to the roof, and the point of the roof directly nearest to it.
Write the roof as \(0x - y + 2z = 6\), with normal \((0, -1, 2)\) and \(|\mathbf{n}| = \sqrt5\). Then \(\mathbf{n}\cdot\mathbf{d} = -3 + 16 = 13\), and the distance is
\[\frac{|13 - 6|}{\sqrt5} = \frac{7}{\sqrt5} = 3.13\ \mathrm{m}\]
The perpendicular is \((3,\ 3 - t,\ 8 + 2t)\). Substituting: \(-(3 - t) + 2(8 + 2t) = 13 + 5t = 6\), so \(t = -\tfrac75\). The nearest point of the roof is \((3,\ 4.4,\ 5.2)\).

**Check**: \(2(5.2) - 4.4 = 6\). ✓
:::

:::eg (Exam style) The point \(A\) has coordinates \((-1, 3, -2)\) and the plane \(\Pi\) has equation \(2x - y + 2z = 9\). (a) Find the coordinates of the foot of the perpendicular from \(A\) to \(\Pi\). (b) Find the perpendicular distance from \(A\) to \(\Pi\). (c) Find the coordinates of the reflection of \(A\) in \(\Pi\).
**(a)** The perpendicular has the direction of the normal:
\[\mathbf{r} = \begin{pmatrix}-1\\3\\-2\end{pmatrix} + t\begin{pmatrix}2\\-1\\2\end{pmatrix}\] [M1]
Substitute into the plane:
\[2(-1 + 2t) - (3 - t) + 2(-2 + 2t) = 9\] [M1]
\[9t - 9 = 9, \quad t = 2\] [A1]
The foot is \(F(3, 1, 2)\). [A1]

**(b)** \(AF = 2|(2, -1, 2)| = 2 \times 3 = 6\). [B1]

**(c)** \(F\) is the midpoint of \(A\) and its image \(A'\), so \(A' = 2F - A\): [M1]
\[A' = (6 + 1,\ 2 - 3,\ 4 + 2) = (7, -1, 6)\] [A1]
:::

## The angle between a line and a plane

A line meets a plane at some angle \(\varphi\), measured between the line and the plane itself: the angle between the line and its shadow (its projection) on the plane. The normal is easier to work with, because the scalar product gives the angle between the line and the normal. In the flat cross-section below, which contains the line and the normal, the plane is seen edge-on.

:::html
<figure class="fig small"><svg viewBox="20 25 300 180" role="img" aria-label="A side view of a plane seen edge-on as a horizontal line. A normal n rises vertically from a point X on the plane. A line l passes through X, rising to the right at an angle phi above the plane, and continuing below the plane as a dashed line. A dotted vertical segment from the top of l down to the plane gives the projection of l on the plane. The angle between l and the normal is marked theta, and a small square marks the right angle between the normal and the plane."><path class="ln" d="M30 150L310 150"/><path class="c3 sw2" d="M170 150L170 40" marker-end="url(#ah)"/><path class="c1 sw2" d="M170 150L269.6 66.4"/><path class="c1 sw2 dash" d="M170 150L116.4 195"/><path class="ln thin dot" d="M269.6 66.4L269.6 150"/><path class="ln thin" d="M170 138L182 138L182 150"/><path class="ln thin" d="M210 150A40 40 0 0 0 200.6 124.3"/><path class="ln thin" d="M170 95A55 55 0 0 1 212.1 114.6"/><text class="tl tb" x="178" y="48">n</text><text class="tl tb" x="276" y="66">l</text><text class="tl tb" x="36" y="168">Π</text><text class="tl" x="219" y="137">φ</text><text class="tl" x="197" y="90">θ</text><text class="tl" x="180" y="168">projection of l</text></svg><figcaption>The angle \(\varphi\) between the line \(l\) and the plane \(\Pi\) is the angle between \(l\) and its projection on the plane. The angle \(\theta\) between \(l\) and the normal \(\mathbf{n}\) satisfies \(\theta + \varphi = 90^\circ\).</figcaption></figure>
:::

:::def Angle between a line and a plane
The **angle between a line and a plane** is the acute angle between the line and its projection onto the plane. It is \(0^\circ\) when the line is parallel to the plane or lies in it, and \(90^\circ\) when the line is perpendicular to the plane.
:::

Because \(\mathbf{n}\) is at \(90^\circ\) to the plane, the angle \(\theta\) between \(l\) and the normal and the angle \(\varphi\) between \(l\) and the plane add up to \(90^\circ\). So \(\sin\varphi = \cos\theta\), and \(\cos\theta\) comes from the scalar product.

:::key Angle between a line and a plane
For a line with direction \(\mathbf{b}\) and a plane with normal \(\mathbf{n}\), the acute angle \(\varphi\) between them is given by
\[\sin\varphi = \frac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\]
The modulus makes the answer acute whichever way \(\mathbf{n}\) points. If \(\mathbf{b}\cdot\mathbf{n} = 0\), then \(\varphi = 0\): the line is parallel to the plane.
:::

:::eg Find the acute angle between the line \(\mathbf{r} = (1, 0, 2) + t(2, 1, -1)\) and the plane \(3x + y - 2z = 8\).
\(\mathbf{b} = (2, 1, -1)\) and \(\mathbf{n} = (3, 1, -2)\). Then \(\mathbf{b}\cdot\mathbf{n} = 6 + 1 + 2 = 9\), \(|\mathbf{b}| = \sqrt6\) and \(|\mathbf{n}| = \sqrt{14}\), so
\[\sin\varphi = \frac{9}{\sqrt6\sqrt{14}} = 0.9820 \quad\Longrightarrow\quad \varphi = 79.1^\circ\]
The line is steep against the plane, close to perpendicular, which fits the large value of \(\mathbf{b}\cdot\mathbf{n}\).
:::

:::warn Sine, not cosine
For the angle between a line and a plane the scalar product goes into \(\sin\varphi\). Using \(\cos\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\) gives the angle with the **normal**, the complement. In the example it would give \(10.9^\circ\) instead of \(79.1^\circ\). A quick sense check: a line almost along the normal makes a large angle with the plane.
:::

Here is the line and plane of that example. Look at the readout for the angle, then change the direction numbers of the line so that \(\mathbf{b}\cdot\mathbf{n}\) gets smaller: the angle falls, and it reaches \(0^\circ\) when the line becomes parallel to the plane (try the direction \(1, -1, 1\), which is perpendicular to the normal \((3, 1, -2)\)).

:::html
<div class="widget" data-w="fm-planes" data-planes="3,1,-2,8" data-line="1,0,2|2,1,-1"></div>
:::

## The angle between two planes

The angle between two planes is the angle between their normals. Draw the two planes edge-on and the normals are at right angles to each, so the angle between the normals equals the angle between the planes. A plane has two normal directions (\(\mathbf{n}\) and \(-\mathbf{n}\)), so the angle can come out acute or obtuse: take the acute one.

:::key Angle between two planes
For planes with normals \(\mathbf{n}_1\) and \(\mathbf{n}_2\), the acute angle \(\theta\) between them satisfies
\[\cos\theta = \frac{|\mathbf{n}_1\cdot\mathbf{n}_2|}{|\mathbf{n}_1||\mathbf{n}_2|}\]
Here the scalar product goes into **cosine**: you are comparing two normals.
:::

:::eg Find the acute angle between the planes \(2x + 3y - z = -8\) and \(x - y + 2z = 3\).
\(\mathbf{n}_1 = (2, 3, -1)\) and \(\mathbf{n}_2 = (1, -1, 2)\). Then \(\mathbf{n}_1\cdot\mathbf{n}_2 = 2 - 3 - 2 = -3\), \(|\mathbf{n}_1| = \sqrt{14}\) and \(|\mathbf{n}_2| = \sqrt6\):
\[\cos\theta = \frac{|-3|}{\sqrt{14}\sqrt6} = 0.3273 \quad\Longrightarrow\quad \theta = 70.9^\circ\]
(The scalar product itself would give \(109.1^\circ\); the acute angle is its supplement.)
:::

:::eg The roof \(2z - y = 6\) slopes up from the ground. Find the angle it makes with the horizontal.
The roof has normal \((0, -1, 2)\). The horizontal ground \(z = 0\) has normal \((0, 0, 1)\). Then
\[\cos\theta = \frac{|0 + 0 + 2|}{\sqrt5 \times 1} = \frac{2}{\sqrt5} = 0.8944 \quad\Longrightarrow\quad \theta = 26.6^\circ\]
This matches the slope: the roof rises 0.5 m for every 1 m across, and \(\tan^{-1}0.5 = 26.6^\circ\). ✓
:::

## The line where two planes meet

Two planes that are not parallel meet in a straight line. That line lies in both planes, so its direction is perpendicular to both normals, and the vector product \(\mathbf{n}_1 \times \mathbf{n}_2\) supplies it. You also need one point that lies in both planes.

:::steps
1. Direction: \(\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2\) (cancel any common factor). If this is \(\mathbf{0}\), the planes are parallel and there is no line of intersection.
2. A point: set one coordinate to a convenient number (usually 0) in **both** equations and solve the two equations for the other two coordinates.
3. Write \(\mathbf{r} = \mathbf{a} + t\mathbf{d}\).
4. Check that the point and the point \(\mathbf{a} + \mathbf{d}\) both satisfy both equations.
:::

:::eg Find an equation of the line where the planes \(\Pi_1: x + 2y - 2z = 5\) and \(\Pi_2: 2x - y + z = 5\) meet.
The normals are \((1, 2, -2)\) and \((2, -1, 1)\), so
\[\mathbf{d} = \begin{pmatrix}1\\2\\-2\end{pmatrix} \times \begin{pmatrix}2\\-1\\1\end{pmatrix} = \begin{pmatrix}2 \times 1 - (-2)(-1)\\ (-2)(2) - 1 \times 1\\ 1 \times (-1) - 2 \times 2\end{pmatrix} = \begin{pmatrix}0\\-5\\-5\end{pmatrix}\]
The direction is \((0, 1, 1)\). For a point, put \(z = 0\):
\[x + 2y = 5, \qquad 2x - y = 5\]
From the second, \(y = 2x - 5\). Then \(x + 4x - 10 = 5\), so \(x = 3\) and \(y = 1\): the point \((3, 1, 0)\) lies in both planes. The line is
\[\mathbf{r} = \begin{pmatrix}3\\1\\0\end{pmatrix} + t\begin{pmatrix}0\\1\\1\end{pmatrix}\]
**Check** the point at \(t = 1\), which is \((3, 2, 1)\): \(3 + 4 - 2 = 5\) ✓ and \(6 - 2 + 1 = 5\) ✓.

**Another way.** Let \(z = t\) and solve for \(x\) and \(y\): \(x + 2y = 5 + 2t\) and \(2x - y = 5 - t\) give \(x = 3\) and \(y = 1 + t\). So the points are \((3,\ 1 + t,\ t)\), the same line.
:::

:::warn Choosing the coordinate to set to zero
If the direction \(\mathbf{d}\) has a zero \(z\) component, the line is parallel to the plane \(z = 0\), so setting \(z = 0\) gives two equations with no common solution. For \(x + 2y + z = 6\) and \(2x + 4y - z = 9\), the direction is \((-6, 3, 0)\), parallel to \((-2, 1, 0)\). Setting \(z = 0\) gives \(x + 2y = 6\) and \(2x + 4y = 9\), which clash. Set \(x = 0\) instead: \(2y + z = 6\) and \(4y - z = 9\), so \(y = 2.5\), \(z = 1\), and the line is \(\mathbf{r} = (0, 2.5, 1) + t(-2, 1, 0)\). If one choice fails, try another coordinate.
:::

Here are the two planes of the worked example. The tool draws the line where they meet and gives the angle between the planes and the direction of the line. It describes the line by its point **closest to the origin**, so its point is \((3, 0.5, -0.5)\), the point \((3, 1 + t, t)\) with \(t = -\tfrac12\), not \((3, 1, 0)\). Both describe the same line.

:::html
<div class="widget" data-w="fm-planes" data-planes="1,2,-2,5; 2,-1,1,5"></div>
:::

:::eg (Exam style) The planes \(\Pi_1\) and \(\Pi_2\) have equations \(2x + y - z = 4\) and \(x - y + 2z = 5\). (a) Find the acute angle between \(\Pi_1\) and \(\Pi_2\). (b) Find a vector equation of the line of intersection of \(\Pi_1\) and \(\Pi_2\).
**(a)** The normals are \(\mathbf{n}_1 = (2, 1, -1)\) and \(\mathbf{n}_2 = (1, -1, 2)\).
\[\mathbf{n}_1\cdot\mathbf{n}_2 = 2 - 1 - 2 = -1\] [M1]
\[|\mathbf{n}_1| = |\mathbf{n}_2| = \sqrt6, \qquad \cos\theta = \frac{|-1|}{\sqrt6\sqrt6}\] [M1]
\[= \tfrac16\] [A1]
\[\theta = 80.4^\circ\] [A1]

**(b)** The direction is
\[\mathbf{n}_1 \times \mathbf{n}_2 = \begin{pmatrix}1 \times 2 - (-1)(-1)\\ (-1)(1) - 2 \times 2\\ 2 \times (-1) - 1 \times 1\end{pmatrix}\] [M1]
\[= \begin{pmatrix}1\\-5\\-3\end{pmatrix}\] [A1]
For a point, put \(z = 0\): \(2x + y = 4\) and \(x - y = 5\). Adding gives \(3x = 9\), so \(x = 3\) and \(y = -2\). [M1]
\[\mathbf{r} = \begin{pmatrix}3\\-2\\0\end{pmatrix} + t\begin{pmatrix}1\\-5\\-3\end{pmatrix}\] [A1]
**Check** at \(t = 1\), the point \((4, -7, -3)\): \(8 - 7 + 3 = 4\) ✓ and \(4 + 7 - 6 = 5\) ✓.
:::

## Skew lines: the shortest distance

Lines that are not parallel and do not meet are **skew** ([Vectors](#math.p3.vectors)). There is exactly one segment joining a point \(P\) of the first line to a point \(Q\) of the second that is perpendicular to both lines. It is the **common perpendicular**, and its length \(PQ\) is the shortest distance between the lines.

:::html
<figure class="fig small"><svg viewBox="20 40 300 165" role="img" aria-label="Two skew lines drawn in perspective: the line l1 runs across the picture nearly horizontally, and the line l2 slopes down from the upper left to the lower right, so they appear to cross but do not meet. A vertical segment PQ joins a point P on l1 to a point Q on l2 above it. The segment is labelled d."><path class="c1 sw2" d="M30 160L290 130"/><path class="c2 sw2" d="M70 50L250 190"/><path class="ln thin" d="M130 148.5L130 96.7"/><circle class="fi" cx="130" cy="148.5" r="3"/><circle class="fi" cx="130" cy="96.7" r="3"/><text class="tl tb" x="278" y="124">l₁</text><text class="tl tb" x="256" y="196">l₂</text><text class="tl tb" x="124" y="166">P</text><text class="tl tb" x="138" y="90">Q</text><text class="tl" x="114" y="126">d</text></svg><figcaption>The skew lines \(l_1\) and \(l_2\). The segment \(PQ\) is perpendicular to both; its length \(d\) is the shortest distance between the lines. The drawing is in perspective, so the right angles at \(P\) and \(Q\) do not look like right angles, and the lines seem to cross although they do not meet.</figcaption></figure>
:::

:::def Common perpendicular
The **common perpendicular** of two skew lines is the unique line that meets both and is perpendicular to both. The part of it between the two lines has the shortest length of any segment joining a point of one line to a point of the other.
:::

Let \(l_1\) be \(\mathbf{r} = \mathbf{a}_1 + s\mathbf{b}_1\) and \(l_2\) be \(\mathbf{r} = \mathbf{a}_2 + t\mathbf{b}_2\). The common perpendicular has the direction of \(\mathbf{n} = \mathbf{b}_1 \times \mathbf{b}_2\), which is perpendicular to both directions. Now take any two points, \(A_1\) on \(l_1\) and \(A_2\) on \(l_2\). The length of the shortest distance is the part of the vector \(\overrightarrow{A_1A_2}\) that points along \(\mathbf{n}\): its scalar product with the **unit** vector \(\hat{\mathbf{n}}\).

:::key Shortest distance between skew lines
\[d = \frac{|(\mathbf{a}_2 - \mathbf{a}_1)\cdot(\mathbf{b}_1 \times \mathbf{b}_2)|}{|\mathbf{b}_1 \times \mathbf{b}_2|}\]
This needs \(\mathbf{b}_1 \times \mathbf{b}_2 \ne \mathbf{0}\) (the lines are not parallel). If the answer is \(0\), the lines intersect. The formula is not on MF19.
:::

:::eg Find the shortest distance between \(l_1: \mathbf{r} = (2, 0, 1) + s(1, 1, 2)\) and \(l_2: \mathbf{r} = (0, 3, 2) + t(2, -1, 0)\).
First the common direction:
\[\mathbf{n} = \begin{pmatrix}1\\1\\2\end{pmatrix} \times \begin{pmatrix}2\\-1\\0\end{pmatrix} = \begin{pmatrix}1 \times 0 - 2 \times (-1)\\ 2 \times 2 - 1 \times 0\\ 1 \times (-1) - 1 \times 2\end{pmatrix} = \begin{pmatrix}2\\4\\-3\end{pmatrix}\]
It is not \(\mathbf{0}\), so the lines are not parallel. Then \(\mathbf{a}_2 - \mathbf{a}_1 = (-2, 3, 1)\), so \((\mathbf{a}_2 - \mathbf{a}_1)\cdot\mathbf{n} = -4 + 12 - 3 = 5\), and \(|\mathbf{n}| = \sqrt{4 + 16 + 9} = \sqrt{29}\):
\[d = \frac{5}{\sqrt{29}} = 0.928\]
The distance is not zero, so the lines do not meet: they are skew.
:::

If you are asked to **find the common perpendicular**, or the points \(P\) and \(Q\), the formula is not enough. Use general points and the two perpendicularity conditions.

:::steps
1. Write a general point \(P\) on \(l_1\) (parameter \(s\)) and \(Q\) on \(l_2\) (parameter \(t\)).
2. Find \(\overrightarrow{PQ}\) in terms of \(s\) and \(t\).
3. Set \(\overrightarrow{PQ}\cdot\mathbf{b}_1 = 0\) and \(\overrightarrow{PQ}\cdot\mathbf{b}_2 = 0\), and solve the two equations for \(s\) and \(t\).
4. Find \(P\) and \(Q\); the distance is \(|PQ|\) and the common perpendicular is the line through \(P\) and \(Q\) (direction \(\mathbf{b}_1 \times \mathbf{b}_2\)).
:::

:::eg Find the shortest distance between \(l_1: \mathbf{r} = (0, 1, 2) + s(1, 2, 2)\) and \(l_2: \mathbf{r} = (1, 2, -1) + t(2, 2, 3)\), and an equation of the common perpendicular.
General points: \(P = (s,\ 1 + 2s,\ 2 + 2s)\) and \(Q = (1 + 2t,\ 2 + 2t,\ -1 + 3t)\). Then
\[\overrightarrow{PQ} = \begin{pmatrix}1 + 2t - s\\ 1 + 2t - 2s\\ -3 + 3t - 2s\end{pmatrix}\]
Perpendicular to \(\mathbf{b}_1 = (1, 2, 2)\):
\[(1 + 2t - s) + 2(1 + 2t - 2s) + 2(-3 + 3t - 2s) = 12t - 9s - 3 = 0\]
so \(4t - 3s = 1\). Perpendicular to \(\mathbf{b}_2 = (2, 2, 3)\):
\[2(1 + 2t - s) + 2(1 + 2t - 2s) + 3(-3 + 3t - 2s) = 17t - 12s - 5 = 0\]
From the first, \(t = \dfrac{1 + 3s}{4}\). Put into the second: \(\dfrac{17(1 + 3s)}{4} - 12s = 5\), so \(17 + 51s - 48s = 20\), \(s = 1\) and \(t = 1\).

Then \(P = (1, 3, 4)\) and \(Q = (3, 4, 2)\), so \(\overrightarrow{PQ} = (2, 1, -2)\) and the distance is \(\sqrt{4 + 1 + 4} = 3\).

The common perpendicular is \(\mathbf{r} = (1, 3, 4) + u(2, 1, -2)\).

**Check** with the formula: \(\mathbf{b}_1 \times \mathbf{b}_2 = (2, 1, -2)\), \(\mathbf{a}_2 - \mathbf{a}_1 = (1, 1, -3)\), and \((1, 1, -3)\cdot(2, 1, -2) = 2 + 1 + 6 = 9\), so \(d = \dfrac{9}{3} = 3\). ✓ The direction \((2, 1, -2)\) of \(\overrightarrow{PQ}\) agrees with \(\mathbf{b}_1 \times \mathbf{b}_2\).
:::

:::warn Parallel lines
If \(\mathbf{b}_1 \times \mathbf{b}_2 = \mathbf{0}\), the lines are parallel and the formula would divide by zero. The distance between parallel lines is the distance from any point of one to the other line, found with the method in the next section.
:::

## The distance from a point to a line

In [Vectors](#math.p3.vectors) you found the foot of the perpendicular from a point to a line by solving a scalar product equal to zero. The vector product gives the distance directly. For the point \(P\) and the line \(\mathbf{r} = \mathbf{a} + t\mathbf{b}\), let \(A\) be the point with position vector \(\mathbf{a}\) and \(\theta\) the angle between \(\overrightarrow{AP}\) and \(\mathbf{b}\). The perpendicular distance is \(|\overrightarrow{AP}|\sin\theta\), and \(|\overrightarrow{AP} \times \mathbf{b}| = |\overrightarrow{AP}||\mathbf{b}|\sin\theta\).

:::key Distance from a point to a line
\[d = \frac{|\overrightarrow{AP} \times \mathbf{b}|}{|\mathbf{b}|}\]
where \(A\) is any point of the line and \(\mathbf{b}\) its direction. This is the parallelogram's area divided by its base.
:::

:::eg Find the distance from \(P(4, 0, 5)\) to the line \(\mathbf{r} = (1, 0, 2) + t(1, 2, 2)\), and the distance from the origin to the line \(\mathbf{r} = (1, 0, 2) + t(2, 1, -1)\).
With \(A(1, 0, 2)\): \(\overrightarrow{AP} = (3, 0, 3)\) and \(\mathbf{b} = (1, 2, 2)\).
\[\overrightarrow{AP} \times \mathbf{b} = \begin{pmatrix}0 \times 2 - 3 \times 2\\ 3 \times 1 - 3 \times 2\\ 3 \times 2 - 0 \times 1\end{pmatrix} = \begin{pmatrix}-6\\-3\\6\end{pmatrix}\]
The length is \(\sqrt{36 + 9 + 36} = 9\) and \(|\mathbf{b}| = 3\), so the distance is \(\dfrac93 = 3\). This agrees with the foot-of-the-perpendicular method in [Vectors](#math.p3.vectors) (the foot there was \((2, 2, 4)\), at distance 3 from \(P\)).

For the origin and the second line: \(\overrightarrow{AO} = (-1, 0, -2)\), \(\mathbf{b} = (2, 1, -1)\).
\[\overrightarrow{AO} \times \mathbf{b} = \begin{pmatrix}0 \times (-1) - (-2)(1)\\ (-2)(2) - (-1)(-1)\\ (-1)(1) - 0 \times 2\end{pmatrix} = \begin{pmatrix}2\\-5\\-1\end{pmatrix}\]
The length is \(\sqrt{30}\) and \(|\mathbf{b}| = \sqrt6\), so the distance is \(\sqrt{5} = 2.24\).
:::

## An unknown that fixes the distance

Examiners often put an unknown into one line and give the distance. The distance formula then becomes an equation, with a modulus.

:::eg (Exam style) The line \(l_1\) has equation \(\mathbf{r} = (1, 0, 2) + s(1, 2, 2)\) and the line \(l_2\) has equation \(\mathbf{r} = (3, 1, k) + t(2, 2, 3)\), where \(k\) is a constant. The shortest distance between \(l_1\) and \(l_2\) is 5. Find the possible values of \(k\).
The common direction:
\[\mathbf{n} = \begin{pmatrix}1\\2\\2\end{pmatrix} \times \begin{pmatrix}2\\2\\3\end{pmatrix} = \begin{pmatrix}2 \times 3 - 2 \times 2\\ 2 \times 2 - 1 \times 3\\ 1 \times 2 - 2 \times 2\end{pmatrix}\] [M1]
\[= \begin{pmatrix}2\\1\\-2\end{pmatrix}, \quad |\mathbf{n}| = 3\] [A1]
The difference of the points is \(\mathbf{a}_2 - \mathbf{a}_1 = (2, 1, k - 2)\), so
\[(\mathbf{a}_2 - \mathbf{a}_1)\cdot\mathbf{n} = 4 + 1 - 2(k - 2)\] [M1]
\[= 9 - 2k\] [A1]
The distance is 5:
\[\frac{|9 - 2k|}{3} = 5\] [M1]
\[9 - 2k = 15 \quad\text{or}\quad 9 - 2k = -15\]
\[k = -3 \quad\text{or}\quad k = 12\] [A1] [A1]

**Check** \(k = 12\): \(9 - 24 = -15\), and \(\dfrac{15}{3} = 5\) ✓. Note that \(9 - 2k = 0\) when \(k = 4.5\): for that value the distance is 0 and the lines meet.
:::

:::exam Modulus and two answers
A given distance leads to \(|\ldots| = \text{number}\) and so to **two** values: forgetting the second loses the last mark. State the common perpendicular's direction with its working (the M1 is for the vector product), and give \(k\) exactly.
:::

:::board
The Cambridge syllabus asks for the angle between a line and a plane, the angle between two planes, the line of intersection and the shortest distance between skew lines. The same material is in the UK Further Mathematics specifications (for example Edexcel Core Pure), where the vector product is used in the same way; Cambridge examples set the problem in three dimensions with given coordinates and ask for exact or 3 s.f. values.
:::

:::eg Spot the error: find the acute angle between the line \(\mathbf{r} = (0, 1, 0) + t(1, 2, 2)\) and the plane \(2x - y + 2z = 3\), for 3 marks (M1 for \(\mathbf{b}\cdot\mathbf{n}\) with the two lengths, M1 for the correct relation between the angle and the plane, A1 for the angle).
A student wrote this answer.

Line 1: \(\mathbf{b} = (1, 2, 2)\), \(\mathbf{n} = (2, -1, 2)\), \(\mathbf{b}\cdot\mathbf{n} = 2 - 2 + 4 = 4\)
Line 2: \(|\mathbf{b}| = 3\) and \(|\mathbf{n}| = 3\)
Line 3: \(\cos\varphi = \dfrac{4}{3 \times 3}\), so \(\varphi = 63.6^\circ\)

Lines 1 and 2 are correct. [M1]

**Line 3 uses cosine where sine is needed.** [M0] [A0] The scalar product gives the angle with the normal, not with the plane. The student found the angle with the normal, \(63.6^\circ\), and forgot to subtract it from \(90^\circ\) (or to use sine). The student scores 1 out of 3.

Correct line 3: \(\sin\varphi = \dfrac49\), so \(\varphi = 26.4^\circ\). [M1] [A1]
:::

:::try Start easy, finish at exam standard
Q: The line \(\mathbf{r} = (1, 1, 0) + t(1, -1, 2)\) meets the plane \(2x + y - z = 6\). Find the point of intersection.
A: The point \((1 + t,\ 1 - t,\ 2t)\) satisfies \(2(1 + t) + (1 - t) - 2t = 6\), so \(3 - t = 6\) and \(t = -3\). The point is \((-2, 4, -6)\). Check: \(-4 + 4 + 6 = 6\).
Q: Decide whether the line \(\mathbf{r} = (0, 1, 2) + t(1, 2, -1)\) lies in, is parallel to, or meets the plane (a) \(3x - y + z = 1\), (b) \(3x - y + z = 4\).
A: \(\mathbf{b}\cdot\mathbf{n} = 3 - 2 - 1 = 0\) in both, so the line is parallel to the plane or in it. The point \((0, 1, 2)\) gives \(0 - 1 + 2 = 1\). (a) The constant is 1, so the line lies in the plane. (b) The constant is 4, so the line is parallel to the plane and does not meet it.
Q: Find the distance of \(P(2, -1, 3)\) from the plane \(x + 2y - 2z = 5\).
A: \(2 - 2 - 6 = -6\), and \(|-6 - 5| = 11\). With \(|\mathbf{n}| = 3\) the distance is \(\dfrac{11}{3} = 3.67\).
Q: Find the foot of the perpendicular from \((1, 2, 3)\) to the plane \(x + y + z = 12\), and the distance.
A: The line \((1 + t,\ 2 + t,\ 3 + t)\) meets the plane when \(6 + 3t = 12\), so \(t = 2\). The foot is \((3, 4, 5)\) and the distance is \(2\sqrt3 = 3.46\).
Q: Find the reflection of the origin in the plane \(2x - y + 2z = 9\).
A: The line \(t(2, -1, 2)\) meets the plane when \(9t = 9\), so \(t = 1\) and the foot is \((2, -1, 2)\). The image is twice that: \((4, -2, 4)\).
Q: Find the acute angle between the line \(\mathbf{r} = (1, 0, 0) + t(1, 1, 1)\) and the plane \(z = 0\).
A: \(\mathbf{n} = (0, 0, 1)\), \(\mathbf{b}\cdot\mathbf{n} = 1\), \(|\mathbf{b}| = \sqrt3\). So \(\sin\varphi = \dfrac{1}{\sqrt3}\) and \(\varphi = 35.3^\circ\).
Q: Find the acute angle between the planes \(x + y + z = 3\) and \(z = 0\).
A: \(\cos\theta = \dfrac{1}{\sqrt3 \times 1}\), so \(\theta = 54.7^\circ\).
Q: Find a vector equation of the line where \(x + y + z = 6\) meets \(x - y + 2z = 0\).
A: The direction is \((1, 1, 1) \times (1, -1, 2) = (3, -1, -2)\). Put \(z = 0\): \(x + y = 6\) and \(x - y = 0\), so \(x = y = 3\). The line is \(\mathbf{r} = (3, 3, 0) + t(3, -1, -2)\). Check at \(t = 1\), the point \((6, 2, -2)\): \(6 + 2 - 2 = 6\) and \(6 - 2 - 4 = 0\).
Q: Find the shortest distance between the lines \(\mathbf{r} = (1, 2, 3) + s(1, 0, 1)\) and \(\mathbf{r} = (0, 1, 1) + t(1, 1, 0)\).
A: \(\mathbf{n} = (1, 0, 1) \times (1, 1, 0) = (-1, 1, 1)\). \(\mathbf{a}_2 - \mathbf{a}_1 = (-1, -1, -2)\), whose scalar product with \(\mathbf{n}\) is \(1 - 1 - 2 = -2\). The distance is \(\dfrac{2}{\sqrt3} = 1.15\).
Q: Find the distance from \(P(1, 1, 1)\) to the line \(\mathbf{r} = (0, 0, 2) + t(1, 2, 2)\).
A: \(\overrightarrow{AP} = (1, 1, -1)\). The vector product with \((1, 2, 2)\) is \((4, -3, 1)\), of length \(\sqrt{26}\). The distance is \(\dfrac{\sqrt{26}}{3} = 1.70\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ The line \(l\) has equation \(\mathbf{r} = \begin{pmatrix}3\\-1\\2\end{pmatrix} + t\begin{pmatrix}-1\\2\\1\end{pmatrix}\) and the plane \(\Pi\) has equation \(2x + y - z = 1\). Find the coordinates of the point where \(l\) meets \(\Pi\).
A: The point is \((3 - t,\ -1 + 2t,\ 2 + t)\), and \(2(3 - t) + (-1 + 2t) - (2 + t) = 1\). [M1]
\(3 - t = 1\), so \(t = 2\). [A1]
The point is \((1, 3, 4)\). [A1]
Q: [4 marks] ★ Find the acute angle between the line with direction \(\mathbf{i} - 2\mathbf{j} + 2\mathbf{k}\) and the plane \(2x + 3y + 6z = 5\).
A: \(\mathbf{b}\cdot\mathbf{n} = 2 - 6 + 12 = 8\). [M1]
\(|\mathbf{b}| = 3\) and \(|\mathbf{n}| = 7\), so \(\sin\varphi = \dfrac{8}{21}\). [M1] [A1]
\(\varphi = 22.4^\circ\). [A1]
Q: [5 marks] ★★ The plane \(\Pi\) has equation \(2x + y + 2z = 2\) and the point \(P\) has coordinates \((4, -1, 2)\). (a) Find the coordinates of the foot of the perpendicular from \(P\) to \(\Pi\). (b) Find the distance of \(P\) from \(\Pi\).
A: (a) The perpendicular is \((4 + 2t,\ -1 + t,\ 2 + 2t)\). [M1]
\(2(4 + 2t) + (-1 + t) + 2(2 + 2t) = 11 + 9t = 2\) [M1], so \(t = -1\). [A1]
The foot is \((2, -2, 0)\). [A1]
(b) The distance is \(|t||\mathbf{n}| = 1 \times 3 = 3\). [B1]
Q: [7 marks] ★★ The planes \(\Pi_1\) and \(\Pi_2\) have equations \(x + 2y + 2z = 7\) and \(2x - 3y + 6z = 11\). (a) Find the acute angle between the planes. (b) Show that \((1, 1, 2)\) lies in both planes, and find a vector equation of their line of intersection.
A: (a) \(\mathbf{n}_1\cdot\mathbf{n}_2 = 2 - 6 + 12 = 8\), \(|\mathbf{n}_1| = 3\), \(|\mathbf{n}_2| = 7\). [M1]
\(\cos\theta = \dfrac{8}{21}\) [A1], so \(\theta = 67.6^\circ\). [A1]
(b) \(1 + 2 + 4 = 7\) and \(2 - 3 + 12 = 11\), so the point is in both planes. [B1]
The direction is \(\begin{pmatrix}1\\2\\2\end{pmatrix} \times \begin{pmatrix}2\\-3\\6\end{pmatrix} = \begin{pmatrix}2 \times 6 - 2 \times (-3)\\ 2 \times 2 - 1 \times 6\\ 1 \times (-3) - 2 \times 2\end{pmatrix}\) [M1] \(= \begin{pmatrix}18\\-2\\-7\end{pmatrix}\). [A1]
\(\mathbf{r} = \begin{pmatrix}1\\1\\2\end{pmatrix} + t\begin{pmatrix}18\\-2\\-7\end{pmatrix}\). [A1]
Q: [5 marks] ★★ Find the shortest distance between the lines \(\mathbf{r} = (1, 0, -2) + s(2, 1, -1)\) and \(\mathbf{r} = (0, 2, 2) + t(1, -1, 3)\).
A: \(\mathbf{n} = \begin{pmatrix}2\\1\\-1\end{pmatrix} \times \begin{pmatrix}1\\-1\\3\end{pmatrix} = \begin{pmatrix}1 \times 3 - (-1)(-1)\\ (-1)(1) - 2 \times 3\\ 2 \times (-1) - 1 \times 1\end{pmatrix}\) [M1] \(= \begin{pmatrix}2\\-7\\-3\end{pmatrix}\). [A1]
\(\mathbf{a}_2 - \mathbf{a}_1 = (-1, 2, 2 + 2) = (-1, 2, 4)\), and the scalar product with \(\mathbf{n}\) is \(-2 - 14 - 12 = -28\). [M1]
\(|\mathbf{n}| = \sqrt{62}\), so \(d = \dfrac{28}{\sqrt{62}}\) [M1] \(= 3.56\). [A1]
Q: [14 marks] (#math.fm.vectors) ★★★ The points \(A\), \(B\), \(C\) have coordinates \((1, 0, 2)\), \((2, 1, 0)\), \((0, 2, 1)\). The plane \(\Pi_2\) has equation \(2x - y + 2z = 6\). (a) Find a Cartesian equation of the plane \(\Pi_1\) through \(A\), \(B\) and \(C\). (b) Find the acute angle between \(\Pi_1\) and \(\Pi_2\). (c) Find a vector equation of the line \(l\) where \(\Pi_1\) and \(\Pi_2\) meet. (d) Find the distance of \(B\) from \(l\).
H: For (a), \(\overrightarrow{AB} = (1, 1, -2)\) and \(\overrightarrow{AC} = (-1, 2, -1)\); the plane has a very simple equation.
H: For (c), the point \((0, 0, 3)\) lies in both planes once you have \(\Pi_1\).
H: For (d), use \(\dfrac{|\overrightarrow{PB} \times \mathbf{d}|}{|\mathbf{d}|}\) with \(P\) any point on \(l\) and \(\mathbf{d}\) the direction of \(l\).
A: (a) \(\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}1 \times (-1) - (-2)(2)\\ (-2)(-1) - 1 \times (-1)\\ 1 \times 2 - 1 \times (-1)\end{pmatrix}\) [M1] \(= \begin{pmatrix}3\\3\\3\end{pmatrix}\). [A1]
A normal is \((1, 1, 1)\), and \(p = 1 + 0 + 2 = 3\) [M1], so \(\Pi_1: x + y + z = 3\). [A1]
(b) \(\mathbf{n}_1\cdot\mathbf{n}_2 = 2 - 1 + 2 = 3\), \(|\mathbf{n}_1| = \sqrt3\) and \(|\mathbf{n}_2| = 3\). [M1]
\(\cos\theta = \dfrac{3}{3\sqrt3} = \dfrac{1}{\sqrt3}\) [A1], so \(\theta = 54.7^\circ\). [A1]
(c) \(\mathbf{n}_1 \times \mathbf{n}_2 = \begin{pmatrix}1 \times 2 - 1 \times (-1)\\ 1 \times 2 - 1 \times 2\\ 1 \times (-1) - 1 \times 2\end{pmatrix} = \begin{pmatrix}3\\0\\-3\end{pmatrix}\) [M1], so the direction is \((1, 0, -1)\). [A1]
The point \((0, 0, 3)\) is in both planes: \(0 + 0 + 3 = 3\) and \(0 - 0 + 6 = 6\). [M1]
\(\mathbf{r} = \begin{pmatrix}0\\0\\3\end{pmatrix} + t\begin{pmatrix}1\\0\\-1\end{pmatrix}\). [A1]
(d) With \(P = (0, 0, 3)\) and \(B = (2, 1, 0)\), \(\overrightarrow{PB} = (2, 1, -3)\). [M1]
\(\overrightarrow{PB} \times \mathbf{d} = \begin{pmatrix}1 \times (-1) - (-3) \times 0\\ (-3)(1) - 2 \times (-1)\\ 2 \times 0 - 1 \times 1\end{pmatrix} = \begin{pmatrix}-1\\-1\\-1\end{pmatrix}\) [M1]
The distance is \(\dfrac{\sqrt3}{\sqrt2} = 1.22\). [A1]
Q: [9 marks] ★★★ The line \(l\) has equation \(\mathbf{r} = (1, -1, 2) + t(1, 2, 1)\) and the plane \(\Pi\) has equation \(3x - y + az = b\), where \(a\) and \(b\) are constants. (a) Given that \(l\) is parallel to \(\Pi\), find the value of \(a\). (b) For this value of \(a\), the distance between \(l\) and \(\Pi\) is \(\sqrt{11}\). Find the two possible values of \(b\). (c) For the larger value of \(b\), find the coordinates of the foot of the perpendicular from \((1, -1, 2)\) to \(\Pi\).
H: Parallel means \(\mathbf{b}\cdot\mathbf{n} = 0\).
H: The distance between a line and a parallel plane is the distance of any point of the line from the plane; use \((1, -1, 2)\).
H: For (c) the perpendicular has direction \(\mathbf{n}\).
A: (a) \(\mathbf{b}\cdot\mathbf{n} = 3 - 2 + a = 0\) [M1], so \(a = -1\). [A1]
(b) With \(\mathbf{n} = (3, -1, -1)\), \(|\mathbf{n}| = \sqrt{11}\), and the point \((1, -1, 2)\) gives \(3 + 1 - 2 = 2\). [M1]
\[\frac{|2 - b|}{\sqrt{11}} = \sqrt{11}\] [M1]
\(|2 - b| = 11\), so \(b = 13\) or \(b = -9\). [A1] [A1]
(c) For \(b = 13\) the perpendicular is \((1 + 3t,\ -1 - t,\ 2 - t)\) [M1] and \(3(1 + 3t) + (1 + t) - (2 - t) = 2 + 11t = 13\), so \(t = 1\). [M1]
The foot is \((4, -2, 1)\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A laser beam is fired from the point \(A(5, -3, 10)\) in the direction \(\mathbf{d} = (-1, 2, -4)\) and meets a plane mirror \(2x - y + 2z = 9\) at the point \(H\). (a) Find the coordinates of \(H\). (b) The reflected beam leaves \(H\) with direction \(\mathbf{d}' = \mathbf{d} - 2\dfrac{\mathbf{d}\cdot\mathbf{n}}{|\mathbf{n}|^2}\mathbf{n}\), where \(\mathbf{n}\) is a normal to the mirror. Explain why this is the direction, and find a vector equation of the reflected beam.
H: Along the beam, \(A + t\mathbf{d}\); substitute into the mirror's equation.
H: A reflection keeps the part of \(\mathbf{d}\) along the mirror and reverses the part along the normal. The part along \(\mathbf{n}\) is \(\dfrac{\mathbf{d}\cdot\mathbf{n}}{|\mathbf{n}|^2}\mathbf{n}\).
A: (a) The beam is \((5 - t,\ -3 + 2t,\ 10 - 4t)\), and \(2(5 - t) - (-3 + 2t) + 2(10 - 4t) = 33 - 12t = 9\). [M1] So \(t = 2\) [A1] and \(H = (3, 1, 2)\). [A1]
(b) Split \(\mathbf{d}\) into a part along \(\mathbf{n}\), \(\mathbf{d}_n = \dfrac{\mathbf{d}\cdot\mathbf{n}}{|\mathbf{n}|^2}\mathbf{n}\), and a part in the mirror, \(\mathbf{d} - \mathbf{d}_n\). Reflection reverses the first and keeps the second, so \(\mathbf{d}' = \mathbf{d} - 2\mathbf{d}_n\). [B1]
\(\mathbf{d}\cdot\mathbf{n} = -2 - 2 - 8 = -12\) and \(|\mathbf{n}|^2 = 9\), so \(\mathbf{d}' = (-1, 2, -4) + \tfrac83(2, -1, 2)\). [M1]
\(\mathbf{d}' = \tfrac13(13, -2, 4)\) [A1], and the reflected beam is \(\mathbf{r} = (3, 1, 2) + u(13, -2, 4)\). [A1] The length check \(|\mathbf{d}'|^2 = \tfrac{169 + 4 + 16}{9} = 21 = |\mathbf{d}|^2\) confirms the speed is unchanged.
Q: [7 marks] ★★★ The planes \(\Pi_1: x + 2y - 2z = 3\) and \(\Pi_2: 4x - 3z = 0\) meet in a line. (a) A point \((x, y, z)\) is equidistant from \(\Pi_1\) and \(\Pi_2\). Show that \(5(x + 2y - 2z - 3) = \pm 3(4x - 3z)\). (b) Hence find Cartesian equations of the two planes that bisect the angle between \(\Pi_1\) and \(\Pi_2\). (c) Show that the two bisecting planes are perpendicular.
H: The distance from \((x, y, z)\) to \(\Pi_1\) is \(\dfrac{|x + 2y - 2z - 3|}{3}\); find the distance to \(\Pi_2\) in the same way.
H: Two quantities have equal moduli when they are equal or opposite.
A: (a) The distance to \(\Pi_1\) is \(\dfrac{|x + 2y - 2z - 3|}{3}\) and to \(\Pi_2\) is \(\dfrac{|4x - 3z|}{5}\). [B1] [B1]
Equal distances give \(\dfrac{x + 2y - 2z - 3}{3} = \pm\dfrac{4x - 3z}{5}\), so \(5(x + 2y - 2z - 3) = \pm 3(4x - 3z)\). [M1]
(b) With the plus sign: \(5x + 10y - 10z - 15 = 12x - 9z\), so \(-7x + 10y - z = 15\), that is \(7x - 10y + z = -15\). [A1]
With the minus sign: \(5x + 10y - 10z - 15 = -12x + 9z\), so \(17x + 10y - 19z = 15\). [A1]
(c) The normals are \((7, -10, 1)\) and \((17, 10, -19)\), and \(119 - 100 - 19 = 0\). [M1] The scalar product is zero, so the planes are perpendicular. [A1]
:::

:::quiz
? A line has direction \(\mathbf{b}\) and a plane has normal \(\mathbf{n}\), with \(\mathbf{b}\cdot\mathbf{n} = 0\). What does this tell you?
+ The line is parallel to the plane or lies in it
- The line is perpendicular to the plane
- The line meets the plane at exactly one point
- The line is skew to the plane
> \(\mathbf{b}\cdot\mathbf{n} = 0\) means the direction is perpendicular to the normal, so it lies along the plane. A line perpendicular to the plane would have \(\mathbf{b}\) parallel to \(\mathbf{n}\), meaning \(\mathbf{b} \times \mathbf{n} = \mathbf{0}\). "Skew" applies to pairs of lines only.
? Which formula gives the acute angle \(\varphi\) between a line (direction \(\mathbf{b}\)) and a plane (normal \(\mathbf{n}\))?
+ \(\sin\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\)
- \(\cos\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\)
- \(\sin\varphi = \dfrac{|\mathbf{b} \times \mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\)
- \(\tan\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\)
> The scalar product gives the cosine of the angle with the normal, which is \(90^\circ - \varphi\), so it gives \(\sin\varphi\). Using cosine gives the angle with the normal; the vector product version gives \(\cos\varphi\) instead.
? How do you find the direction of the line where two planes meet?
+ Take the vector product of the two normals
- Take the scalar product of the two normals
- Add the two normals
- Use either normal, since both are perpendicular to the line
> The line lies in both planes, so its direction is perpendicular to both normals, which is what \(\mathbf{n}_1 \times \mathbf{n}_2\) gives. The scalar product is a number, and a single normal is perpendicular to the line but not parallel to it.
? What is the distance of \(P(1, 2, 3)\) from the plane \(2x - y + 2z = 3\)?
+ \(1\)
- \(3\)
- \(2\)
- \(-1\)
> \(2 - 2 + 6 = 6\), then \(|6 - 3| = 3\), and \(|\mathbf{n}| = 3\): the distance is 1. The answer 3 forgets to divide by \(|\mathbf{n}|\), 2 forgets to subtract the constant, and a distance is never negative.
? Two skew lines have directions \(\mathbf{b}_1\), \(\mathbf{b}_2\) and points \(\mathbf{a}_1\), \(\mathbf{a}_2\). Which expression gives the shortest distance?
+ \(\dfrac{|(\mathbf{a}_2 - \mathbf{a}_1)\cdot(\mathbf{b}_1 \times \mathbf{b}_2)|}{|\mathbf{b}_1 \times \mathbf{b}_2|}\)
- \(\dfrac{|(\mathbf{a}_2 - \mathbf{a}_1) \times (\mathbf{b}_1 \times \mathbf{b}_2)|}{|\mathbf{b}_1 \times \mathbf{b}_2|}\)
- \(\dfrac{|(\mathbf{a}_2 - \mathbf{a}_1)\cdot\mathbf{b}_1|}{|\mathbf{b}_1|}\)
- \(|\mathbf{a}_2 - \mathbf{a}_1|\)
> The distance is the part of \(\mathbf{a}_2 - \mathbf{a}_1\) along the common perpendicular's direction, found with a scalar product with the unit vector \(\mathbf{b}_1 \times \mathbf{b}_2\) divided by its length. The last two options use the length of an arbitrary vector between the lines, which is not the shortest.
? The planes \(\Pi_1\) and \(\Pi_2\) have normals \((1, 0, 0)\) and \((1, 1, 1)\). What is the acute angle between them?
+ \(54.7^\circ\)
- \(90^\circ\)
- \(35.3^\circ\)
- \(45^\circ\)
> \(\cos\theta = \dfrac{1}{1 \times \sqrt3}\), so \(\theta = 54.7^\circ\): you compare the normals with cosine. \(90^\circ\) would need a scalar product of zero, and \(35.3^\circ\) comes from putting the scalar product into sine, which is the line-and-plane formula.
:::

:::checklist What you can now do
- [ ] I can decide whether a line lies in a plane, is parallel to it or meets it, and find the point of intersection when it exists.
- [ ] I can find the foot of the perpendicular from a point to a plane, the distance, and the reflection of the point in the plane.
- [ ] I can find the distance between a point and a plane, and between parallel planes, from the formula.
- [ ] I can find the angle between a line and a plane, using \(\sin\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\).
- [ ] I can find the angle between two planes from their normals.
- [ ] I can find a vector equation of the line of intersection of two planes.
- [ ] I can find the shortest distance between two skew lines, and an equation for their common perpendicular.
- [ ] I can find the distance from a point to a line with the vector product.
- [ ] I can use a given distance or angle to find an unknown constant in an equation of a line or plane.
:::

:::recap
- Line \(\mathbf{r} = \mathbf{a} + t\mathbf{b}\) and plane normal \(\mathbf{n}\): \(\mathbf{b}\cdot\mathbf{n} \ne 0\) gives one point (substitute into the plane); \(\mathbf{b}\cdot\mathbf{n} = 0\) gives parallel or in the plane (test a point).
- Distance of \((x_1, y_1, z_1)\) from \(ax + by + cz = d\): \(\dfrac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}\). The foot is on the line through the point with direction \(\mathbf{n}\); the reflection goes twice as far.
- Line and plane: \(\sin\varphi = \dfrac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}\). Two planes: \(\cos\theta = \dfrac{|\mathbf{n}_1\cdot\mathbf{n}_2|}{|\mathbf{n}_1||\mathbf{n}_2|}\).
- Line of intersection of two planes: direction \(\mathbf{n}_1 \times \mathbf{n}_2\), plus a point found by setting one coordinate to a number (change the coordinate if the equations clash).
- Skew lines: \(d = \dfrac{|(\mathbf{a}_2 - \mathbf{a}_1)\cdot(\mathbf{b}_1 \times \mathbf{b}_2)|}{|\mathbf{b}_1 \times \mathbf{b}_2|}\). For the common perpendicular use \(\overrightarrow{PQ}\cdot\mathbf{b}_1 = \overrightarrow{PQ}\cdot\mathbf{b}_2 = 0\).
- Point to line: \(\dfrac{|\overrightarrow{AP} \times \mathbf{b}|}{|\mathbf{b}|}\).
- A given distance leads to \(|\ldots| = \text{number}\), so two values. None of these formulas is on MF19.
:::

:::links
- watch: [Shortest distance between two skew lines](https://www.examsolutions.net/tutorials/shortest-distance-between-two-skew-lines/) · ExamSolutions · the formula and the general-point method, step by step
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · lines and planes questions with answers
- practise: [Linear algebra](https://www.khanacademy.org/math/linear-algebra) · Khan Academy · planes, projections and exercises
- explore: [Desmos 3D](https://www.desmos.com/3d) · Desmos · draw two planes and the line where they meet
- explore: [GeoGebra 3D](https://www.geogebra.org/3d) · GeoGebra · two skew lines and their common perpendicular
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 vector questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Hyperbolic functions](#math.fm.hyperbolic) starts Further Pure Mathematics 2 with the functions \(\sinh x\) and \(\cosh x\), which behave like trigonometric functions but are built from \(\mathrm{e}^x\).
