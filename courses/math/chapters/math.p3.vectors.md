@chapter math.p3.vectors
@title Vectors
@level a2
@paper CAIE P3 · Edexcel IAL P4 · AQA/OCR/Edexcel Pure Year 2
@time 9–11 hours
@summary Vectors in two and three dimensions: components, magnitude, unit and position vectors, the vector equation of a line \(\mathbf{r} = \mathbf{a} + t\mathbf{b}\), deciding whether two lines are parallel, intersecting or skew, the scalar product for angles and perpendicular distances, and problems set in a cuboid.

:::why
A single number cannot say where a drone is, how a force pulls, or which way a ship is heading. A vector carries both size and direction, and in three dimensions it is the natural way to describe points, lines and the angles between them. The same algebra describes a drone's flight path, a ray of light meeting a mirror and the edges of a building in a computer game. In the exam, three-dimensional geometry is a self-contained set of procedures: once you know them, the questions are routine.
:::

**Before you start**, you need Pythagoras' theorem and the cosine rule from [Geometry from scratch](#math.f.geometry), coordinate geometry from [Coordinate geometry: lines and circles](#math.p1.coord) and simultaneous equations from [Algebra from scratch](#math.f.algebra).

## Vectors and components

:::def Vector and scalar
A **vector** has a magnitude (size) and a direction. A **scalar** has magnitude only, such as a length or a mass. Write a vector in bold, \(\mathbf{a}\), or from \(A\) to \(B\) as \(\overrightarrow{AB}\).
:::

In components, a vector is written as a column or with the unit vectors \(\mathbf{i}\), \(\mathbf{j}\), \(\mathbf{k}\), which have length 1 and point along the \(x\)-, \(y\)- and \(z\)-axes.
\[\mathbf{a} = \begin{pmatrix}2\\-3\\6\end{pmatrix} = 2\mathbf{i} - 3\mathbf{j} + 6\mathbf{k}\]

Add, subtract and scale by working on each component separately: \(\begin{pmatrix}1\\2\\3\end{pmatrix} + 2\begin{pmatrix}0\\-1\\4\end{pmatrix} = \begin{pmatrix}1\\0\\11\end{pmatrix}\). Geometrically, adding vectors joins them head to tail. Two vectors are **parallel** if one is a multiple of the other.

:::key Magnitude and unit vector
For \(\mathbf{a} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}\), the magnitude is
\[|\mathbf{a}| = \sqrt{x^2 + y^2 + z^2}\]
A **unit vector** in the direction of \(\mathbf{a}\) is \(\dfrac{\mathbf{a}}{|\mathbf{a}|}\), which has magnitude 1.
:::

:::eg Find the magnitude of \(\mathbf{a} = 2\mathbf{i} - 3\mathbf{j} + 6\mathbf{k}\), a unit vector parallel to \(\mathbf{a}\), and the value of \(\lambda\) for which \(\mathbf{a}\) is parallel to \(\mathbf{b} = \lambda\mathbf{i} + 6\mathbf{j} - 12\mathbf{k}\).
\(|\mathbf{a}| = \sqrt{4 + 9 + 36} = 7\). The unit vector is \(\tfrac17(2\mathbf{i} - 3\mathbf{j} + 6\mathbf{k})\).
For parallel vectors, \(\mathbf{b} = m\mathbf{a}\). Comparing the \(\mathbf{k}\)-components: \(-12 = 6m\), so \(m = -2\). Check the \(\mathbf{j}\)-components: \(-2\times(-3) = 6\) ✓. So \(\lambda = -2\times 2 = -4\).
:::

## Position vectors and displacements

:::def Position vector
The **position vector** of a point \(A\) is \(\overrightarrow{OA}\), the vector from the origin \(O\) to \(A\). It is written \(\mathbf{a}\), and its components are the coordinates of \(A\).
:::

The key move is the displacement between two points. To go from \(A\) to \(B\), go back to the origin and then out to \(B\):

:::key Displacement and midpoint
\[\overrightarrow{AB} = \mathbf{b} - \mathbf{a}\]
The midpoint \(M\) of \(AB\) has position vector \(\tfrac12(\mathbf{a} + \mathbf{b})\). If \(OABC\) is a parallelogram, then \(\overrightarrow{OB} = \overrightarrow{OA} + \overrightarrow{OC}\).
:::

:::eg The points \(A\) and \(B\) have coordinates \((1, 2, 3)\) and \((4, -2, 5)\). Find \(\overrightarrow{AB}\), the distance \(AB\) and the midpoint of \(AB\). \(C\) is the point \((1, 3, 2)\). If \(OAB'C\) is a parallelogram, find \(B'\).
\(\overrightarrow{AB} = \begin{pmatrix}4\\-2\\5\end{pmatrix} - \begin{pmatrix}1\\2\\3\end{pmatrix} = \begin{pmatrix}3\\-4\\2\end{pmatrix}\), and \(AB = \sqrt{9 + 16 + 4} = \sqrt{29} = 5.39\) (3 s.f.).
The midpoint has position vector \(\tfrac12\left[\begin{pmatrix}1\\2\\3\end{pmatrix} + \begin{pmatrix}4\\-2\\5\end{pmatrix}\right] = \begin{pmatrix}2.5\\0\\4\end{pmatrix}\), so the midpoint is \((2.5, 0, 4)\).
For the parallelogram, \(\overrightarrow{OB'} = \overrightarrow{OA} + \overrightarrow{OC} = \begin{pmatrix}2\\5\\5\end{pmatrix}\), so \(B'\) is \((2, 5, 5)\).
:::

## The vector equation of a line

A line is fixed by a point on it and a direction. If \(A\) is a point with position vector \(\mathbf{a}\) and the line is parallel to \(\mathbf{b}\), then any point on the line is reached by going to \(A\) and then moving a multiple of \(\mathbf{b}\) along the line.

:::key Vector equation of a line
\[\mathbf{r} = \mathbf{a} + t\mathbf{b}\]
where \(\mathbf{a}\) is the position vector of a point on the line, \(\mathbf{b}\) is a **direction vector** and \(t\) is a scalar parameter. Each value of \(t\) gives one point on the line.
:::

The equation of a line is not unique: any point on the line works for \(\mathbf{a}\), and any multiple of \(\mathbf{b}\) works as the direction. To find the line through two points \(A\) and \(B\), use \(\mathbf{a}\) as the point and \(\overrightarrow{AB}\) as the direction.

:::eg Find a vector equation of the line through \(A(1, 2, -1)\) and \(B(3, 5, 1)\). Does the point \(P(5, 8, 3)\) lie on the line? Does \(Q(4, 7, 2)\)?
\(\overrightarrow{AB} = \begin{pmatrix}2\\3\\2\end{pmatrix}\), so \(\mathbf{r} = \begin{pmatrix}1\\2\\-1\end{pmatrix} + t\begin{pmatrix}2\\3\\2\end{pmatrix}\).
For \(P\), the \(x\)-coordinate: \(1 + 2t = 5\) gives \(t = 2\). Check the others: \(y = 2 + 6 = 8\) ✓ and \(z = -1 + 4 = 3\) ✓. So \(P\) lies on the line.
For \(Q\): \(1 + 2t = 4\) gives \(t = 1.5\), but then \(y = 2 + 4.5 = 6.5 \ne 7\). So \(Q\) is not on the line.
:::

:::eg (Real context) A drone takes off and flies so that its position, in metres relative to a base \(O\), is \(\mathbf{r} = \begin{pmatrix}0\\0\\40\end{pmatrix} + t\begin{pmatrix}6\\8\\-2\end{pmatrix}\), where \(t\) is the time in seconds and the \(z\)-axis points up. Find its speed, when it reaches the ground and how far it has flown by then.
The velocity is the direction vector, so the speed is \(\sqrt{36 + 64 + 4} = \sqrt{104} = 10.2\) m s\(^{-1}\) (3 s.f.).
The ground is \(z = 0\): \(40 - 2t = 0\), so \(t = 20\) s, at the point \((120, 160, 0)\).
Distance flown \(= 20\sqrt{104} = 204\) m (3 s.f.).
:::

## Parallel, intersecting or skew

Two lines in 3D have exactly three possibilities. Compare the directions first.

:::key Relationship between two lines
1. **Parallel**: the direction vectors are multiples of each other.
2. **Not parallel, and they meet**: **intersecting**, at one point.
3. **Not parallel, and they never meet**: **skew**. This can only happen in three dimensions; in two dimensions, lines that are not parallel always meet.
:::

To test for intersection, equate the position vectors, write one equation for each component, solve two of them for the two parameters, and **check the answers in the third equation**. If it fails, the lines are skew.

:::eg Show that \(l_1: \mathbf{r} = \begin{pmatrix}1\\2\\3\end{pmatrix} + s\begin{pmatrix}1\\-1\\2\end{pmatrix}\) and \(l_2: \mathbf{r} = \begin{pmatrix}1\\-1\\8\end{pmatrix} + t\begin{pmatrix}2\\1\\-1\end{pmatrix}\) intersect, and find the point of intersection.
The directions are not multiples, so the lines are not parallel. Equate components:
\[x: 1 + s = 1 + 2t \qquad y: 2 - s = -1 + t \qquad z: 3 + 2s = 8 - t\]
From \(x\): \(s = 2t\). Put in \(y\): \(2 - 2t = -1 + t\), so \(t = 1\) and \(s = 2\). Check in \(z\): left side \(3 + 4 = 7\), right side \(8 - 1 = 7\) ✓. The lines intersect, at \(s = 2\): the point with position vector \(\begin{pmatrix}3\\0\\7\end{pmatrix}\), that is \((3, 0, 7)\).
:::

:::eg Show that \(l_1\) above and \(l_3: \mathbf{r} = \begin{pmatrix}1\\-1\\0\end{pmatrix} + u\begin{pmatrix}2\\1\\-1\end{pmatrix}\) are skew.
The directions \(\begin{pmatrix}1\\-1\\2\end{pmatrix}\) and \(\begin{pmatrix}2\\1\\-1\end{pmatrix}\) are not multiples of each other. Equate: \(x\): \(s = 2u\); \(y\): \(2 - s = -1 + u\) gives \(u = 1\), \(s = 2\). The \(z\)-equation \(3 + 2s = -u\) would need \(7 = -1\), which is false. So there is no common point and the lines are skew.
:::

## The scalar product

:::def Scalar product
The **scalar product** (dot product) of \(\mathbf{a} = a_1\mathbf{i} + a_2\mathbf{j} + a_3\mathbf{k}\) and \(\mathbf{b} = b_1\mathbf{i} + b_2\mathbf{j} + b_3\mathbf{k}\) is
\[\mathbf{a}\cdot\mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3 = |\mathbf{a}||\mathbf{b}|\cos\theta\]
where \(\theta\) is the angle between the vectors when both point away from the same point. The result is a number, not a vector. Both forms are on MF19.
:::

Two results follow at once. The angle is found from \(\cos\theta = \dfrac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\). And two non-zero vectors are **perpendicular** exactly when \(\mathbf{a}\cdot\mathbf{b} = 0\), because \(\cos 90^\circ = 0\).

:::eg Find the angle between \(\mathbf{a} = 2\mathbf{i} - \mathbf{j} + 2\mathbf{k}\) and \(\mathbf{b} = \mathbf{i} + 2\mathbf{j} - 2\mathbf{k}\). Then find \(\angle ABC\) for \(A(1, 0, 2)\), \(B(3, 1, 0)\), \(C(2, 3, 1)\).
\(\mathbf{a}\cdot\mathbf{b} = 2 - 2 - 4 = -4\) and \(|\mathbf{a}| = |\mathbf{b}| = 3\), so \(\cos\theta = -\dfrac49\) and \(\theta = 116.4^\circ\) (1 d.p.). The angle is obtuse because the product is negative.

For \(\angle ABC\), use the two vectors **away from \(B\)**: \(\overrightarrow{BA} = \begin{pmatrix}-2\\-1\\2\end{pmatrix}\) and \(\overrightarrow{BC} = \begin{pmatrix}-1\\2\\1\end{pmatrix}\). Then \(\overrightarrow{BA}\cdot\overrightarrow{BC} = 2 - 2 + 2 = 2\), \(|\overrightarrow{BA}| = 3\) and \(|\overrightarrow{BC}| = \sqrt6\):
\[\cos\angle ABC = \frac{2}{3\sqrt6} = 0.2722 \quad\Longrightarrow\quad \angle ABC = 74.2^\circ\]
:::

:::warn Angles with the scalar product
Both vectors must **leave the same point**. For \(\angle ABC\), use \(\overrightarrow{BA}\) and \(\overrightarrow{BC}\), not \(\overrightarrow{AB}\) and \(\overrightarrow{BC}\) (that would give \(180^\circ\) minus the angle). For the angle between two **lines**, use the direction vectors, and if the question asks for the acute angle, take the positive value of the dot product.
:::

## The angle between two lines

The angle between two lines is the angle between their direction vectors. Lines meet at an acute and an obtuse angle that add up to \(180^\circ\); the question usually asks for the **acute** angle, so take \(|\mathbf{a}\cdot\mathbf{b}|\).

:::eg Find the acute angle between \(l_1\) and \(l_2\) above.
The directions are \(\mathbf{d}_1 = \begin{pmatrix}1\\-1\\2\end{pmatrix}\) and \(\mathbf{d}_2 = \begin{pmatrix}2\\1\\-1\end{pmatrix}\). Then \(\mathbf{d}_1\cdot\mathbf{d}_2 = 2 - 1 - 2 = -1\) and \(|\mathbf{d}_1| = |\mathbf{d}_2| = \sqrt6\), so
\[\cos\theta = \frac{|-1|}{\sqrt6\times\sqrt6} = \frac16 \quad\Longrightarrow\quad \theta = 80.4^\circ\]
(The dot product itself gives \(\cos\theta = -\tfrac16\), the obtuse angle of \(99.6^\circ\).)
:::

## Foot of the perpendicular and shortest distance

The shortest distance from a point \(P\) to a line is along the perpendicular. Let \(F\) be the **foot of the perpendicular**, the point on the line closest to \(P\). Then \(\overrightarrow{PF}\) is perpendicular to the line's direction, so the dot product is zero.

:::key Finding the foot of the perpendicular
1. Write a general point \(X\) on the line, with position vector \(\mathbf{a} + t\mathbf{b}\).
2. Find \(\overrightarrow{PX}\) in terms of \(t\).
3. Solve \(\overrightarrow{PX}\cdot\mathbf{b} = 0\) for \(t\).
4. Put \(t\) back to get \(F\); the perpendicular distance is \(|\overrightarrow{PF}|\).
:::

:::eg The line \(l\) has equation \(\mathbf{r} = \begin{pmatrix}1\\0\\2\end{pmatrix} + t\begin{pmatrix}1\\2\\2\end{pmatrix}\) and \(P\) is the point \((4, 0, 5)\). Find the foot of the perpendicular from \(P\) to \(l\) and the perpendicular distance.
A general point \(X\) is \((1 + t,\ 2t,\ 2 + 2t)\), so \(\overrightarrow{PX} = \begin{pmatrix}t - 3\\2t\\2t - 3\end{pmatrix}\).
Perpendicular to the direction: \((t - 3)(1) + (2t)(2) + (2t - 3)(2) = 9t - 9 = 0\), so \(t = 1\).
The foot is \(F(2, 2, 4)\). Then \(\overrightarrow{PF} = \begin{pmatrix}-2\\2\\-1\end{pmatrix}\) and the distance is \(\sqrt{4 + 4 + 1} = 3\).
:::

## Solids

Problems set in a cuboid or pyramid start by choosing axes. Put the origin at a vertex, and the axes along three edges that meet there. Then every vertex gets coordinates and every edge a vector. Draw the solid, label each vertex, and write the coordinates in a list.

:::html
<figure class="fig small"><svg viewBox="0 52 250 144" role="img" aria-label="A cuboid OABCDEFG with O at the front bottom left. OA is 6 along the x direction, OC is 4 into the page along the y direction and OD is 3 vertically upwards; D, E, F and G are above O, A, B and C."><path class="ln" d="M40 170L184 170M184 170L220 146M40 98L184 98M184 98L220 74M220 74L76 74M76 74L40 98M40 170L40 98M184 170L184 98M220 146L220 74"/><path class="ln dash thin" d="M40 170L76 146M76 146L220 146M76 146L76 74"/><text class="tl tb" x="28" y="182">O</text><text class="tl tb" x="188" y="184">A</text><text class="tl tb" x="228" y="152">B</text><text class="tl tb" x="62" y="144">C</text><text class="tl tb" x="26" y="96">D</text><text class="tl tb" x="172" y="92">E</text><text class="tl tb" x="228" y="72">F</text><text class="tl tb" x="72" y="66">G</text><text class="tl ti halo" x="112" y="186">6 i</text><text class="tl ti halo" x="216" y="168">4 j</text><text class="tl ti halo" x="16" y="138">3 k</text></svg><figcaption>The cuboid \(OABCDEFG\). \(O\) is the origin, \(OA = 6\) along \(\mathbf{i}\), \(OC = 4\) along \(\mathbf{j}\) and \(OD = 3\) along \(\mathbf{k}\). Dashed lines are hidden edges.</figcaption></figure>
:::

With these axes, \(A(6,0,0)\), \(B(6,4,0)\), \(C(0,4,0)\), \(D(0,0,3)\), \(E(6,0,3)\), \(F(6,4,3)\) and \(G(0,4,3)\).

:::eg (Exam style) For the cuboid \(OABCDEFG\) in the figure, find (a) \(\overrightarrow{OF}\) and \(|\overrightarrow{OF}|\), (b) \(\angle EOG\), and (c) the acute angle between the diagonals \(OF\) and \(AG\).
(a) \(\overrightarrow{OF} = \begin{pmatrix}6\\4\\3\end{pmatrix}\), so \(|\overrightarrow{OF}| = \sqrt{36 + 16 + 9} = \sqrt{61} = 7.81\). [B1]
(b) \(\overrightarrow{OE} = \begin{pmatrix}6\\0\\3\end{pmatrix}\) and \(\overrightarrow{OG} = \begin{pmatrix}0\\4\\3\end{pmatrix}\). The dot product is \(0 + 0 + 9 = 9\), with \(|\overrightarrow{OE}| = \sqrt{45}\) and \(|\overrightarrow{OG}| = 5\). [M1]
\[\cos\angle EOG = \frac{9}{5\sqrt{45}} = 0.2683 \quad\Longrightarrow\quad \angle EOG = 74.4^\circ\quad [A1]\]
(c) \(\overrightarrow{AG} = \begin{pmatrix}0\\4\\3\end{pmatrix} - \begin{pmatrix}6\\0\\0\end{pmatrix} = \begin{pmatrix}-6\\4\\3\end{pmatrix}\). Then \(\overrightarrow{OF}\cdot\overrightarrow{AG} = -36 + 16 + 9 = -11\), and \(|\overrightarrow{AG}| = \sqrt{61}\) too. [M1] So \(\cos\theta = \dfrac{|-11|}{61}\) and the acute angle is \(79.6^\circ\). [A1]
:::

:::exam What earns marks
- **Show the vector subtraction** (\(\overrightarrow{AB} = \mathbf{b} - \mathbf{a}\)) with the numbers written out; the method mark is for the correct subtraction.
- For **intersection**, show all three component equations, solve two of them, and **check the third** (a mark). A "skew" conclusion needs the contradiction stated.
- For **angles**, state the vectors used, the dot product, both magnitudes, then the angle to 1 decimal place (or 3 s.f.), and the acute angle where asked. The scalar product formulae are on MF19.
- The question may give a line in the form \(\mathbf{r} = \ldots\) or as separate coordinate equations; convert and keep to the same form throughout.
:::

:::board Other boards
Edexcel IAL P4 and the Year 2 Pure courses (AQA, OCR, Edexcel) all treat vector lines, intersection, the scalar product and perpendicular distances; some also give Cartesian forms of a line such as \(\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z + 1}{2}\). The vector (cross) product belongs to Further Mathematics and is not needed for Cambridge 9709.
:::

:::try Start easy, finish at exam standard
Q: Find \(|\mathbf{a}|\) and a unit vector in the direction of \(\mathbf{a} = 3\mathbf{i} - 4\mathbf{j} + 12\mathbf{k}\).
A: \(|\mathbf{a}| = \sqrt{9 + 16 + 144} = 13\). The unit vector is \(\tfrac1{13}(3\mathbf{i} - 4\mathbf{j} + 12\mathbf{k})\).
Q: \(A\) is \((2, -1, 3)\) and \(B\) is \((-1, 3, 5)\). Find \(\overrightarrow{AB}\), the distance \(AB\) and the midpoint of \(AB\).
A: \(\overrightarrow{AB} = \begin{pmatrix}-3\\4\\2\end{pmatrix}\); \(AB = \sqrt{29} = 5.39\); the midpoint is \((0.5, 1, 4)\).
Q: Find a vector equation of the line through \((1, 0, -2)\) and \((3, -2, 1)\). Does \((7, -6, 7)\) lie on it?
A: The direction is \(\begin{pmatrix}2\\-2\\3\end{pmatrix}\), so \(\mathbf{r} = \begin{pmatrix}1\\0\\-2\end{pmatrix} + t\begin{pmatrix}2\\-2\\3\end{pmatrix}\). For \(x = 7\), \(t = 3\), and then \(y = -6\) and \(z = -2 + 9 = 7\). Yes, it does.
Q: Find the angle between \(\mathbf{a} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}\) and \(\mathbf{b} = 2\mathbf{i} - 3\mathbf{j} + 6\mathbf{k}\).
A: \(\mathbf{a}\cdot\mathbf{b} = 2 - 6 + 12 = 8\), \(|\mathbf{a}| = 3\), \(|\mathbf{b}| = 7\), so \(\cos\theta = \dfrac{8}{21}\) and \(\theta = 67.6^\circ\).
Q: Find \(k\) so that \(k\mathbf{i} + 2\mathbf{j} - \mathbf{k}\) is perpendicular to \(3\mathbf{i} - \mathbf{j} + 4\mathbf{k}\).
A: The dot product is zero: \(3k - 2 - 4 = 0\), so \(k = 2\).
Q: The lines \(l_1: \mathbf{r} = \begin{pmatrix}1\\3\\2\end{pmatrix} + s\begin{pmatrix}2\\-1\\1\end{pmatrix}\) and \(l_2: \mathbf{r} = \begin{pmatrix}-1\\0\\1\end{pmatrix} + t\begin{pmatrix}2\\1\\1\end{pmatrix}\) intersect. Find the point of intersection and the acute angle between the lines.
A: \(y\): \(3 - s = t\); \(z\): \(2 + s = 1 + t\). So \(2 + s = 4 - s\), giving \(s = 1\), \(t = 2\). Check \(x\): \(1 + 2 = 3\) and \(-1 + 4 = 3\) ✓. The point is \((3, 2, 3)\). The directions have dot product \(4 - 1 + 1 = 4\) and each magnitude is \(\sqrt6\), so \(\cos\theta = \tfrac46 = \tfrac23\), \(\theta = 48.2^\circ\).
Q: Show that \(\mathbf{r} = \begin{pmatrix}1\\0\\0\end{pmatrix} + s\begin{pmatrix}0\\1\\1\end{pmatrix}\) and \(\mathbf{r} = \begin{pmatrix}0\\1\\0\end{pmatrix} + t\begin{pmatrix}1\\0\\2\end{pmatrix}\) are skew.
A: The directions are not parallel. \(x\): \(1 = t\); \(y\): \(s = 1\); \(z\): \(s = 2t\) would need \(1 = 2\), which is false. So the lines do not meet and are skew.
Q: The line \(\mathbf{r} = \begin{pmatrix}0\\1\\2\end{pmatrix} + t\begin{pmatrix}1\\1\\1\end{pmatrix}\) and the point \(P(3, 1, 5)\). Find the foot of the perpendicular from \(P\) to the line, and the perpendicular distance.
A: \(X = (t, 1 + t, 2 + t)\), so \(\overrightarrow{PX} = \begin{pmatrix}t - 3\\t\\t - 3\end{pmatrix}\). The dot product with the direction: \(3t - 6 = 0\), so \(t = 2\). The foot is \((2, 3, 4)\) and the distance is \(\left|\begin{pmatrix}-1\\2\\-1\end{pmatrix}\right| = \sqrt6 = 2.45\).
Q: (Exam style) In the cuboid \(OABCDEFG\) of the figure, find the acute angle between \(OF\) and \(BD\).
A: \(\overrightarrow{OF} = \begin{pmatrix}6\\4\\3\end{pmatrix}\) and \(\overrightarrow{BD} = \begin{pmatrix}-6\\-4\\3\end{pmatrix}\). The dot product is \(-36 - 16 + 9 = -43\), and each magnitude is \(\sqrt{61}\). So \(\cos\theta = \dfrac{43}{61}\) and the acute angle is \(45.2^\circ\).
:::

:::quiz
? \(A\) is \((1, 4, -2)\) and \(B\) is \((3, 1, 4)\). What is \(\overrightarrow{AB}\)?
- \(\begin{pmatrix}-2\\3\\-6\end{pmatrix}\)
+ \(\begin{pmatrix}2\\-3\\6\end{pmatrix}\)
- \(\begin{pmatrix}4\\5\\2\end{pmatrix}\)
- \(\begin{pmatrix}2\\3\\6\end{pmatrix}\)
> \(\overrightarrow{AB} = \mathbf{b} - \mathbf{a}\): end minus start. The first option is \(\overrightarrow{BA}\).
? What does \(\mathbf{a}\cdot\mathbf{b} = 0\) tell you about two non-zero vectors?
- They are parallel.
+ They are perpendicular.
- They have equal magnitude.
- One is a unit vector.
> \(\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta\), which is zero only when \(\cos\theta = 0\), that is \(\theta = 90^\circ\).
? Lines \(l_1\) and \(l_2\) are not parallel, and solving two of the three component equations gives values that fail the third. What can you conclude?
- The lines are parallel.
- The lines intersect.
+ The lines are skew.
- Nothing, because you need a fourth equation.
> If the values of \(s\) and \(t\) from two components do not satisfy the third, there is no common point, and non-parallel lines with no common point are skew.
? Which vectors do you use for the angle \(\angle PQR\)?
- \(\overrightarrow{PQ}\) and \(\overrightarrow{QR}\)
+ \(\overrightarrow{QP}\) and \(\overrightarrow{QR}\)
- \(\overrightarrow{PQ}\) and \(\overrightarrow{RQ}\)
- \(\overrightarrow{PR}\) and \(\overrightarrow{QR}\)
> Both vectors must start at \(Q\), the vertex of the angle. Using \(\overrightarrow{PQ}\) and \(\overrightarrow{QR}\) gives \(180^\circ\) minus the angle.
? A line has equation \(\mathbf{r} = \begin{pmatrix}1\\2\\3\end{pmatrix} + t\begin{pmatrix}1\\1\\2\end{pmatrix}\). Which is also a correct equation of the same line?
- \(\mathbf{r} = \begin{pmatrix}1\\2\\3\end{pmatrix} + t\begin{pmatrix}1\\1\\3\end{pmatrix}\)
+ \(\mathbf{r} = \begin{pmatrix}2\\3\\5\end{pmatrix} + s\begin{pmatrix}2\\2\\4\end{pmatrix}\)
- \(\mathbf{r} = \begin{pmatrix}2\\3\\4\end{pmatrix} + s\begin{pmatrix}1\\1\\2\end{pmatrix}\)
- \(\mathbf{r} = \begin{pmatrix}1\\1\\2\end{pmatrix} + t\begin{pmatrix}1\\2\\3\end{pmatrix}\)
> \((2, 3, 5)\) is on the line (at \(t = 1\)) and \((2, 2, 4)\) is twice the direction. In the third option the point \((2, 3, 4)\) is not on the line, as \(t = 1\) gives \(z = 5\).
:::

:::recap
- A vector has magnitude \(\sqrt{x^2 + y^2 + z^2}\) and direction; a unit vector is \(\mathbf{a}/|\mathbf{a}|\). Parallel vectors are multiples.
- \(\overrightarrow{AB} = \mathbf{b} - \mathbf{a}\); the midpoint is \(\tfrac12(\mathbf{a} + \mathbf{b})\); for a parallelogram \(OABC\), \(\overrightarrow{OB} = \overrightarrow{OA} + \overrightarrow{OC}\).
- A line: \(\mathbf{r} = \mathbf{a} + t\mathbf{b}\), with a point and a direction. It is not unique.
- Two lines: parallel (directions are multiples), intersecting (all three component equations satisfied) or skew (neither).
- \(\mathbf{a}\cdot\mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3 = |\mathbf{a}||\mathbf{b}|\cos\theta\); perpendicular if zero. Use vectors that start at the same point.
- Foot of a perpendicular: general point \(X\) on the line, then \(\overrightarrow{PX}\cdot\mathbf{b} = 0\). Distance is \(|\overrightarrow{PF}|\).
:::

:::note Learn more online
- **Watch:** [Intersecting and skew lines](https://www.examsolutions.net/tutorials/vectors-intersecting-skew-lines/) · ExamSolutions · the three-equation test
- **Watch:** [Exam questions: parallel, intersecting and skew lines](https://www.examsolutions.net/tutorials/exam-questions-parallel-intersecting-and-skew-lines/) · ExamSolutions · exam-style questions solved on video
- **Practise:** [CAIE Pure 3 vector lines and scalar product exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/vectors/vector-equations-of-lines-and-the-scalar-product/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [GeoGebra 3D calculator](https://www.geogebra.org/3d) · GeoGebra · plot two lines in 3D and rotate them to see if they meet
- **Explore:** [Vector Geometry](https://undergroundmathematics.org/vector-geometry) · Underground Mathematics · rich problems on lines and angles
- **Read:** [Understanding the dot product](https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/) · BetterExplained · what a·b measures

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Complex numbers](#math.p3.complex).
