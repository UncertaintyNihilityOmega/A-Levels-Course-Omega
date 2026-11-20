@chapter math.fm.vectors
@title Vectors: the vector product and planes
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–7 hours
@summary The vector product \(\mathbf{a} \times \mathbf{b}\) of two vectors is a new vector, perpendicular to both, whose length is the area of the parallelogram they span. You will learn to compute it, use it for areas, and use it to write the equation of a plane in vector, Cartesian and parametric form, move between the three forms, and find the plane through three points.

:::why
A line in three dimensions is easy to describe with one direction, but a flat surface needs two directions, and the clean way to pin it down is a single vector at right angles to it. The vector product builds that perpendicular vector for you. The same idea describes the roof of a house, the face of a crystal, the screen in a computer-graphics scene and the plane a drone must stay above.
:::

**Before you start**, you need vectors in three dimensions, the scalar product and the vector equation of a line from [Vectors](#math.p3.vectors), and the \(3 \times 3\) determinant from [Matrices: algebra, determinants and inverses](#math.fm.matrices). This chapter is about the vector product and the plane; the next, [Vectors: intersections, angles and distances](#math.fm.vectors2), uses both to solve problems about lines and planes together.

:::try Warm-up
Q: Find the angle between \(\mathbf{a} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}\) and \(\mathbf{b} = 2\mathbf{i} - \mathbf{j} + 2\mathbf{k}\). (from [Vectors](#math.p3.vectors))
A: \(\mathbf{a}\cdot\mathbf{b} = 2 - 2 + 4 = 4\) and \(|\mathbf{a}| = |\mathbf{b}| = 3\), so \(\cos\theta = \tfrac49\) and \(\theta = 63.6^\circ\).
Q: Write down a vector equation of the line through \(A(1, 2, 0)\) and \(B(3, -1, 4)\). (from [Vectors](#math.p3.vectors))
A: The direction is \(\overrightarrow{AB} = \begin{pmatrix}2\\-3\\4\end{pmatrix}\), so \(\mathbf{r} = \begin{pmatrix}1\\2\\0\end{pmatrix} + t\begin{pmatrix}2\\-3\\4\end{pmatrix}\).
Q: Find the determinant of \(\begin{pmatrix}2 & -3\\1 & 4\end{pmatrix}\). (from [Matrices: algebra, determinants and inverses](#math.fm.matrices))
A: \(2 \times 4 - (-3) \times 1 = 8 + 3 = 11\).
:::

## The vector product

The scalar product of two vectors is a number. The **vector product** is a vector: it is perpendicular to both of the vectors you multiply, and its length measures how far from parallel they are. Two vectors that point the same way have vector product zero, and two perpendicular vectors give the largest length.

:::def Vector product
The **vector product** (or cross product) of two vectors \(\mathbf{a}\) and \(\mathbf{b}\) is
\[\mathbf{a} \times \mathbf{b} = |\mathbf{a}||\mathbf{b}|\sin\theta\ \hat{\mathbf{n}}\]
where \(\theta\) is the angle between \(\mathbf{a}\) and \(\mathbf{b}\) (when both point away from the same point), and \(\hat{\mathbf{n}}\) is the unit vector perpendicular to both \(\mathbf{a}\) and \(\mathbf{b}\) whose direction is given by the right-hand rule.
:::

**The right-hand rule.** Point the fingers of your right hand along \(\mathbf{a}\), then curl them towards \(\mathbf{b}\), through the smaller angle between them. Your thumb points along \(\hat{\mathbf{n}}\), and so along \(\mathbf{a} \times \mathbf{b}\).

:::html
<figure class="fig small"><svg viewBox="20 25 300 175" role="img" aria-label="A parallelogram lying flat with a vertex at O. Its sides are the vectors a, pointing to the right, and b, pointing away to the back left of a. The angle between a and b is marked theta. An arrow labelled a cross b rises vertically from O, perpendicular to the parallelogram."><polygon class="fm s-acc sw2" points="70,170 220,170 270,125 120,125"/><path class="c1 sw2" d="M70 170L210 170" marker-end="url(#ah)"/><path class="c2 sw2" d="M70 170L112 131" marker-end="url(#ah)"/><path class="c3 sw2" d="M70 170L70 52" marker-end="url(#ah)"/><path class="ln thin" d="M94 170A24 24 0 0 0 87.8 153.9"/><text class="tl tb" x="140" y="190">a</text><text class="tl tb" x="84" y="138">b</text><text class="tl" x="100" y="160">θ</text><text class="tl tb" x="84" y="62">a × b</text></svg><figcaption>The vector product \(\mathbf{a} \times \mathbf{b}\) stands at right angles to the flat parallelogram on \(\mathbf{a}\) and \(\mathbf{b}\). Its length is the area of that parallelogram. Curl the fingers of your right hand from \(\mathbf{a}\) to \(\mathbf{b}\) and your thumb points along \(\mathbf{a} \times \mathbf{b}\).</figcaption></figure>
:::

The definition tells you what the answer looks like but it is awkward for calculation, because you rarely know the angle. In an exam you work from components.

:::key The vector product in components
For \(\mathbf{a} = a_1\mathbf{i} + a_2\mathbf{j} + a_3\mathbf{k}\) and \(\mathbf{b} = b_1\mathbf{i} + b_2\mathbf{j} + b_3\mathbf{k}\),
\[\mathbf{a} \times \mathbf{b} = (a_2b_3 - a_3b_2)\mathbf{i} + (a_3b_1 - a_1b_3)\mathbf{j} + (a_1b_2 - a_2b_1)\mathbf{k}\]
In column form:
\[\mathbf{a} \times \mathbf{b} = \begin{pmatrix}a_2b_3 - a_3b_2\\ a_3b_1 - a_1b_3\\ a_1b_2 - a_2b_1\end{pmatrix}\]
Both forms must be learned: the vector product is not on MF19.
:::

The formula is hard to remember as it stands. Two memory aids give the same result.

:::steps
1. **Determinant layout.** Write \(\mathbf{i}\), \(\mathbf{j}\), \(\mathbf{k}\) in the top row, the components of \(\mathbf{a}\) in the second and of \(\mathbf{b}\) in the third, and expand along the top row, remembering the middle sign is minus (shown below).
2. **Cover-up.** For the \(\mathbf{i}\) component, cover the first component of both vectors and take the \(2 \times 2\) determinant of what is left (top row times bottom row, minus the other diagonal). For \(\mathbf{k}\), cover the third. For \(\mathbf{j}\), do the same with the second, **then reverse the sign** (equivalently, the \(\mathbf{j}\) component is \(a_3b_1 - a_1b_3\), the cover-up result written the other way round).
:::

The determinant layout, expanded along the top row:
\[\mathbf{a} \times \mathbf{b} = \begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k}\\ a_1 & a_2 & a_3\\ b_1 & b_2 & b_3\end{vmatrix} = \mathbf{i}\begin{vmatrix}a_2 & a_3\\ b_2 & b_3\end{vmatrix} - \mathbf{j}\begin{vmatrix}a_1 & a_3\\ b_1 & b_3\end{vmatrix} + \mathbf{k}\begin{vmatrix}a_1 & a_2\\ b_1 & b_2\end{vmatrix}\]

:::eg Find \(\mathbf{a} \times \mathbf{b}\) for \(\mathbf{a} = \begin{pmatrix}2\\-1\\3\end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix}1\\4\\-2\end{pmatrix}\), and check the answer.
Take each component in turn.
\[\begin{aligned}
\mathbf{i}:&\ (-1)(-2) - (3)(4) = 2 - 12 = -10 \\
\mathbf{j}:&\ (3)(1) - (2)(-2) = 3 + 4 = 7 \\
\mathbf{k}:&\ (2)(4) - (-1)(1) = 8 + 1 = 9
\end{aligned}\]
So \(\mathbf{a} \times \mathbf{b} = \begin{pmatrix}-10\\7\\9\end{pmatrix}\).

**Check** that the result is perpendicular to both vectors, using the scalar product:
\[\begin{aligned}
\begin{pmatrix}-10\\7\\9\end{pmatrix}\cdot\mathbf{a} &= -20 - 7 + 27 = 0 \\
\begin{pmatrix}-10\\7\\9\end{pmatrix}\cdot\mathbf{b} &= -10 + 28 - 18 = 0
\end{aligned}\]
:::

That check takes ten seconds and catches nearly every slip, so make it a habit. It matters most for the \(\mathbf{j}\) component, where the sign is easy to lose.

### Properties of the vector product

:::key Properties
- \(\mathbf{b} \times \mathbf{a} = -(\mathbf{a} \times \mathbf{b})\): swapping the order reverses the direction. The vector product is **not commutative**.
- \(\mathbf{a} \times \mathbf{a} = \mathbf{0}\), and \(\mathbf{a} \times \mathbf{b} = \mathbf{0}\) exactly when \(\mathbf{a}\) and \(\mathbf{b}\) are parallel (or one of them is the zero vector), because \(\sin 0^\circ = \sin 180^\circ = 0\).
- \(\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}\) and \((k\mathbf{a}) \times \mathbf{b} = k(\mathbf{a} \times \mathbf{b})\).
- \(\mathbf{a} \times \mathbf{b}\) is perpendicular to \(\mathbf{a}\) and to \(\mathbf{b}\), and \(|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta\).
- \(\mathbf{i} \times \mathbf{j} = \mathbf{k}\), \(\mathbf{j} \times \mathbf{k} = \mathbf{i}\), \(\mathbf{k} \times \mathbf{i} = \mathbf{j}\) (going round \(\mathbf{i}, \mathbf{j}, \mathbf{k}\) in order is positive), and each reversed product is the negative.
:::

For the vectors above, \(\mathbf{b} \times \mathbf{a} = \begin{pmatrix}10\\-7\\-9\end{pmatrix}\), the negative of \(\mathbf{a} \times \mathbf{b}\).

:::proof Why the component form is perpendicular to both vectors
Write \(\mathbf{c} = \mathbf{a} \times \mathbf{b}\) with the components above and form \(\mathbf{a}\cdot\mathbf{c}\):
\[\begin{aligned}
\mathbf{a}\cdot\mathbf{c} &= a_1(a_2b_3 - a_3b_2) + a_2(a_3b_1 - a_1b_3) + a_3(a_1b_2 - a_2b_1) \\
&= a_1a_2b_3 - a_1a_3b_2 + a_2a_3b_1 - a_1a_2b_3 + a_1a_3b_2 - a_2a_3b_1
\end{aligned}\]
The six terms cancel in pairs: \(a_1a_2b_3\) with \(-a_1a_2b_3\), \(a_1a_3b_2\) with \(-a_1a_3b_2\), and \(a_2a_3b_1\) with \(-a_2a_3b_1\). So \(\mathbf{a}\cdot\mathbf{c} = 0\), and \(\mathbf{c}\) is perpendicular to \(\mathbf{a}\). The same cancellation shows \(\mathbf{b}\cdot\mathbf{c} = 0\).
:::

:::proof Why the length is \(|\mathbf{a}||\mathbf{b}|\sin\theta\)
Square the three components of \(\mathbf{a} \times \mathbf{b}\) and add. Each bracket gives two squares and one cross term, so
\[\begin{aligned}
|\mathbf{a} \times \mathbf{b}|^2 &= a_2^2b_3^2 + a_3^2b_2^2 + a_3^2b_1^2 + a_1^2b_3^2 + a_1^2b_2^2 + a_2^2b_1^2 \\
&\quad - 2a_2a_3b_2b_3 - 2a_1a_3b_1b_3 - 2a_1a_2b_1b_2
\end{aligned}\]
Now expand \(|\mathbf{a}|^2|\mathbf{b}|^2 = (a_1^2 + a_2^2 + a_3^2)(b_1^2 + b_2^2 + b_3^2)\), which has the three terms \(a_i^2b_i^2\) and the six terms above, and subtract \((\mathbf{a}\cdot\mathbf{b})^2 = (a_1b_1 + a_2b_2 + a_3b_3)^2\), which has the same three terms \(a_i^2b_i^2\) plus the three cross terms \(2a_ia_jb_ib_j\). The \(a_i^2b_i^2\) cancel and what is left is the expression above:
\[|\mathbf{a} \times \mathbf{b}|^2 = |\mathbf{a}|^2|\mathbf{b}|^2 - (\mathbf{a}\cdot\mathbf{b})^2\]
Now use \(\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta\):
\[|\mathbf{a} \times \mathbf{b}|^2 = |\mathbf{a}|^2|\mathbf{b}|^2(1 - \cos^2\theta) = |\mathbf{a}|^2|\mathbf{b}|^2\sin^2\theta\]
Take the square root: \(\sin\theta \ge 0\) for \(0^\circ \le \theta \le 180^\circ\), so \(|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta\).
:::

:::eg Find a unit vector perpendicular to both \(\mathbf{a} = \begin{pmatrix}2\\-1\\3\end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix}1\\4\\-2\end{pmatrix}\). Then use the vector product to find the angle between them.
A vector perpendicular to both is \(\mathbf{a} \times \mathbf{b} = \begin{pmatrix}-10\\7\\9\end{pmatrix}\), found above. Its length is
\[|\mathbf{a} \times \mathbf{b}| = \sqrt{100 + 49 + 81} = \sqrt{230}\]
A unit vector is \(\dfrac{1}{\sqrt{230}}\begin{pmatrix}-10\\7\\9\end{pmatrix}\). The negative of it is also a unit vector perpendicular to both.

For the angle, \(|\mathbf{a}| = \sqrt{14}\) and \(|\mathbf{b}| = \sqrt{21}\), so
\[\sin\theta = \frac{\sqrt{230}}{\sqrt{14}\sqrt{21}} = 0.8845\]
This gives \(\theta = 62.2^\circ\) or \(117.8^\circ\): a sine alone cannot tell acute from obtuse. The scalar product settles it: \(\mathbf{a}\cdot\mathbf{b} = 2 - 4 - 6 = -8\), which is negative, so the angle is obtuse and \(\theta = 117.8^\circ\).
:::

:::warn The vector product does not give the sign of the angle
\(\sin\theta\) is the same for \(\theta\) and \(180^\circ - \theta\), and \(|\mathbf{a} \times \mathbf{b}|\) is a length, so it cannot say which. To find an angle between two vectors, use the scalar product; use the vector product for a perpendicular direction or an area.
:::

### Areas

The parallelogram with sides \(\mathbf{a}\) and \(\mathbf{b}\) has base \(|\mathbf{a}|\) and perpendicular height \(|\mathbf{b}|\sin\theta\), so its area is \(|\mathbf{a}||\mathbf{b}|\sin\theta\). That is exactly \(|\mathbf{a} \times \mathbf{b}|\), which is why the figure above shows the vector product standing on a parallelogram.

:::key Areas from the vector product
The parallelogram with adjacent sides \(\overrightarrow{AB}\) and \(\overrightarrow{AD}\) has area \(|\overrightarrow{AB} \times \overrightarrow{AD}|\).
The triangle \(ABC\) has area
\[\tfrac12|\overrightarrow{AB} \times \overrightarrow{AC}|\]
because it is half of the parallelogram with sides \(\overrightarrow{AB}\) and \(\overrightarrow{AC}\).
:::

:::eg Find the area of triangle \(ABC\) where \(A(1, 2, 0)\), \(B(3, 0, 1)\) and \(C(3, 3, 4)\).
The two sides from \(A\) are
\[\overrightarrow{AB} = \begin{pmatrix}2\\-2\\1\end{pmatrix}, \qquad \overrightarrow{AC} = \begin{pmatrix}2\\1\\4\end{pmatrix}\]
The vector product:
\[\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}(-2)(4) - (1)(1)\\ (1)(2) - (2)(4)\\ (2)(1) - (-2)(2)\end{pmatrix} = \begin{pmatrix}-9\\-6\\6\end{pmatrix}\]
Its length is \(\sqrt{81 + 36 + 36} = \sqrt{153} = 3\sqrt{17}\), so the area is \(\tfrac32\sqrt{17} = 6.18\) square units (3 s.f.).
:::

:::eg A triangular roof panel has corners at \(A(0, 0, 2)\), \(B(6, 0, 2)\) and \(C(2, 5, 4)\), with coordinates in metres. Find its area.
Here \(\overrightarrow{AB} = \begin{pmatrix}6\\0\\0\end{pmatrix}\) and \(\overrightarrow{AC} = \begin{pmatrix}2\\5\\2\end{pmatrix}\). Then
\[\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}0 \times 2 - 0 \times 5\\ 0 \times 2 - 6 \times 2\\ 6 \times 5 - 0 \times 2\end{pmatrix} = \begin{pmatrix}0\\-12\\30\end{pmatrix}\]
The length is \(\sqrt{144 + 900} = \sqrt{1044} = 6\sqrt{29}\), so the area is \(3\sqrt{29} = 16.2\,\mathrm{m^2}\) (3 s.f.). The panel is not as small as its horizontal footprint suggests: seen from above it covers only \(\tfrac12 \times 6 \times 5 = 15\,\mathrm{m^2}\), and the slope adds the rest.
:::

## The equation of a plane

A plane is a flat surface that extends for ever. You can fix it in two ways: by one point and the direction it faces, or by one point and two directions that lie along it. The first leads to the equation \(\mathbf{r}\cdot\mathbf{n} = p\) and the Cartesian form; the second to the parametric form.

:::def Plane and normal vector
A **plane** is a flat two-dimensional surface in three-dimensional space. A **normal vector** \(\mathbf{n}\) to a plane is any non-zero vector perpendicular to the plane (so perpendicular to every line lying in it). All normal vectors of one plane are parallel, so \(\mathbf{n}\) can be multiplied by any non-zero number.
:::

### Normal form: \(\mathbf{r}\cdot\mathbf{n} = p\)

Let the plane pass through the point \(A\) with position vector \(\mathbf{a}\), and have normal \(\mathbf{n}\). Take any point \(R\) of the plane, with position vector \(\mathbf{r}\). Then \(\overrightarrow{AR} = \mathbf{r} - \mathbf{a}\) lies in the plane, so it is perpendicular to \(\mathbf{n}\):

\[(\mathbf{r} - \mathbf{a})\cdot\mathbf{n} = 0 \quad\Longrightarrow\quad \mathbf{r}\cdot\mathbf{n} = \mathbf{a}\cdot\mathbf{n}\]

The right-hand side \(\mathbf{a}\cdot\mathbf{n}\) is a number, which we call \(p\).

:::html
<figure class="fig small"><svg viewBox="20 28 300 160" role="img" aria-label="A flat parallelogram representing the plane Pi. A point A lies inside it. An arrow labelled n rises from A, perpendicular to the plane. A second arrow, labelled AR, lies in the plane from A towards a second point R. A small square marks the right angle between n and AR."><polygon class="fm s-acc sw2" points="40,170 230,170 300,110 110,110"/><path class="c3 sw2" d="M150 145L150 44" marker-end="url(#ah)"/><path class="c1 sw2" d="M150 145L233 135" marker-end="url(#ah)"/><path class="ln thin" d="M150 133L161.9 131.6L161.9 143.6"/><circle class="fi" cx="150" cy="145" r="3"/><circle class="fi" cx="245" cy="133" r="3"/><text class="tl tb" x="164" y="56">n</text><text class="tl tb" x="134" y="161">A</text><text class="tl tb" x="252" y="130">R</text><text class="tl" x="186" y="160">AR</text><text class="tl tb" x="70" y="158">Π</text></svg><figcaption>The plane \(\Pi\) through \(A\) with normal \(\mathbf{n}\). For every point \(R\) in the plane the vector \(\overrightarrow{AR}\) is perpendicular to \(\mathbf{n}\), which is what \((\mathbf{r} - \mathbf{a})\cdot\mathbf{n} = 0\) says.</figcaption></figure>
:::

Now put \(\mathbf{n} = \begin{pmatrix}a\\b\\c\end{pmatrix}\) and \(\mathbf{r} = \begin{pmatrix}x\\y\\z\end{pmatrix}\). The scalar product \(\mathbf{r}\cdot\mathbf{n}\) is \(ax + by + cz\), so the same equation is written without vectors.

:::key Equations of a plane
For a plane through the point \(A\) with normal \(\mathbf{n} = a\mathbf{i} + b\mathbf{j} + c\mathbf{k}\):
\[\mathbf{r}\cdot\mathbf{n} = p \qquad\text{where } p = \mathbf{a}\cdot\mathbf{n}\]
\[ax + by + cz = d \qquad\text{where } d = p\]
The coefficients of \(x\), \(y\), \(z\) in the Cartesian form are the components of a normal vector. Multiplying the whole equation by a non-zero number gives the same plane (with a different normal of the same direction).
:::

:::eg Find the vector and Cartesian equations of the plane through \(A(1, -2, 4)\) with normal vector \(\mathbf{n} = 2\mathbf{i} + 3\mathbf{j} - \mathbf{k}\).
Find \(p\) from the given point:
\[p = \mathbf{a}\cdot\mathbf{n} = 1(2) + (-2)(3) + 4(-1) = 2 - 6 - 4 = -8\]
The vector equation is \(\mathbf{r}\cdot\begin{pmatrix}2\\3\\-1\end{pmatrix} = -8\), and the Cartesian equation is
\[2x + 3y - z = -8\]
**Check** with the point \(A\): \(2(1) + 3(-2) - 4 = -8\). ✓ The equation \(4x + 6y - 2z = -16\) describes the same plane.
:::

:::eg Decide whether each of the points \(P(2, 1, 3)\) and \(Q(2, -1, 1)\) lies in the plane \(x - 2y + 4z = 8\).
A point is in the plane exactly when its coordinates satisfy the equation, so substitute each into the left-hand side.
For \(P(2, 1, 3)\): \(2 - 2 + 12 = 12\), which is not 8, so \(P\) is not in the plane.
For \(Q(2, -1, 1)\): \(2 + 2 + 4 = 8\), so \(Q\) is in the plane.
:::

### How far is the plane from the origin?

The plane \(\mathbf{r}\cdot\mathbf{n} = p\) is a fixed distance from \(O\). If \(\mathbf{n}\) is a **unit** vector, that distance is \(|p|\): the scalar product \(\mathbf{r}\cdot\hat{\mathbf{n}}\) is the length of the part of \(\mathbf{r}\) along the normal, and it is the same for every point of the plane. If \(\mathbf{n}\) is not a unit vector, divide through by \(|\mathbf{n}|\).

:::key Distance of a plane from the origin
The plane \(\mathbf{r}\cdot\mathbf{n} = p\), that is \(ax + by + cz = d\), is at distance
\[\frac{|p|}{|\mathbf{n}|} = \frac{|d|}{\sqrt{a^2 + b^2 + c^2}}\]
from the origin. The foot of the perpendicular from \(O\) to the plane is \(\dfrac{p}{|\mathbf{n}|^2}\mathbf{n}\).
:::

:::eg Find the distance from the origin to the plane \(2x + 3y - z = -8\), and the foot of the perpendicular from \(O\).
\(|\mathbf{n}| = \sqrt{4 + 9 + 1} = \sqrt{14}\), so the distance is \(\dfrac{|-8|}{\sqrt{14}} = \dfrac{8}{\sqrt{14}} = 2.14\) (3 s.f.).

The foot is \(\dfrac{-8}{14}\begin{pmatrix}2\\3\\-1\end{pmatrix} = \begin{pmatrix}-\tfrac87\\-\tfrac{12}{7}\\ \tfrac47\end{pmatrix}\).

**Check** that this point is in the plane: \(2\left(-\tfrac87\right) + 3\left(-\tfrac{12}{7}\right) - \tfrac47 = -\tfrac{16 + 36 + 4}{7} = -8\). ✓
:::

Two planes with the same normal direction are **parallel**: their equations differ only in the number on the right. So \(2x + 3y - z = -8\) and \(2x + 3y - z = 5\) are parallel planes, and so is \(4x + 6y - 2z = 1\).

Here is a tool to see a plane and its normal. It starts with \(3x - 2y + z = 6\); change the numbers to move the plane, and turn the view with the buttons or by dragging.

:::html
<div class="widget" data-w="fm-planes" data-planes="3,-2,1,6"></div>
:::

Try changing only the number on the right: the plane slides along its normal and the distance from \(O\) changes. Then change the coefficients and watch the normal arrow turn.

### Parametric form: \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\)

A line needs one direction. A plane needs two directions that are not parallel, because you can then reach any point of it by moving some distance along one and some along the other.

:::def Vector (parametric) equation of a plane
\[\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\]
where \(\mathbf{a}\) is the position vector of a **point** in the plane, \(\mathbf{b}\) and \(\mathbf{c}\) are two **non-parallel direction vectors** lying in the plane, and \(\lambda\) and \(\mu\) are real parameters.
:::

A normal vector of this plane is perpendicular to both directions, so it is the vector product \(\mathbf{n} = \mathbf{b} \times \mathbf{c}\). That single fact converts parametric form to the other two.

:::warn Point or direction?
In \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\) only the first vector is a point. The other two are directions, and they must **not** be parallel. Two usual slips: using the position vector of a second point as a direction (use the difference of two points), and choosing two directions that are multiples of each other, which describes only a line.
:::

:::eg Find a Cartesian equation of the plane \(\mathbf{r} = \begin{pmatrix}1\\0\\2\end{pmatrix} + \lambda\begin{pmatrix}1\\2\\0\end{pmatrix} + \mu\begin{pmatrix}0\\1\\3\end{pmatrix}\).
**Method 1: the vector product.** The normal is
\[\mathbf{n} = \begin{pmatrix}1\\2\\0\end{pmatrix} \times \begin{pmatrix}0\\1\\3\end{pmatrix} = \begin{pmatrix}2 \times 3 - 0 \times 1\\ 0 \times 0 - 1 \times 3\\ 1 \times 1 - 2 \times 0\end{pmatrix} = \begin{pmatrix}6\\-3\\1\end{pmatrix}\]
The plane passes through \((1, 0, 2)\), so \(p = 6 - 0 + 2 = 8\). The plane is \(6x - 3y + z = 8\).

**Method 2: eliminate the parameters.** Write out the coordinates:
\[x = 1 + \lambda, \qquad y = 2\lambda + \mu, \qquad z = 2 + 3\mu\]
From the first, \(\lambda = x - 1\). From the third, \(\mu = \dfrac{z - 2}{3}\). Substitute both into the second:
\[\begin{aligned}
y &= 2(x - 1) + \frac{z - 2}{3} \\
3y &= 6x - 6 + z - 2 \\
6x - 3y + z &= 8
\end{aligned}\]
Both methods agree. **Check** a direction: \(6(1) - 3(2) + 0 = 0\) and \(6(0) - 3(1) + 3 = 0\), so both directions are perpendicular to the normal.
:::

Going the other way, from a Cartesian equation to a parametric one, you need a point on the plane and two non-parallel directions in it. A direction \(\mathbf{b}\) lies in the plane \(ax + by + cz = d\) exactly when \(\mathbf{b}\cdot\mathbf{n} = 0\).

:::steps
1. Find any point on the plane by choosing two coordinates and solving for the third (for example, \(y = z = 0\)).
2. Find two non-parallel vectors with \(\mathbf{b}\cdot\mathbf{n} = 0\) (put a zero in one place and swap and negate the other two entries of \(\mathbf{n}\)), or use the differences of three points of the plane.
3. Write \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\).
4. Check that \(\mathbf{b}\) and \(\mathbf{c}\) are not parallel and that \(\mathbf{b}\cdot\mathbf{n} = \mathbf{c}\cdot\mathbf{n} = 0\).
:::

:::eg Find a vector equation of the plane \(3x - 2y + z = 6\) in the form \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\).
The normal is \(\mathbf{n} = (3, -2, 1)\). A point on the plane: put \(y = z = 0\), then \(3x = 6\), so \(\mathbf{a} = (2, 0, 0)\).

Directions with \(\mathbf{b}\cdot\mathbf{n} = 0\): \(\mathbf{b} = (1, 0, -3)\) works, since \(3 + 0 - 3 = 0\); so does \(\mathbf{c} = (0, 1, 2)\), since \(0 - 2 + 2 = 0\). They are not multiples of each other, so
\[\mathbf{r} = \begin{pmatrix}2\\0\\0\end{pmatrix} + \lambda\begin{pmatrix}1\\0\\-3\end{pmatrix} + \mu\begin{pmatrix}0\\1\\2\end{pmatrix}\]
**Check** with the vector product: \(\mathbf{b} \times \mathbf{c} = \begin{pmatrix}0 \times 2 - (-3) \times 1\\ (-3) \times 0 - 1 \times 2\\ 1 \times 1 - 0 \times 0\end{pmatrix} = \begin{pmatrix}3\\-2\\1\end{pmatrix}\), which is \(\mathbf{n}\). ✓

Many answers are correct. Another is \(\mathbf{r} = (0, 0, 6) + \lambda(2, 3, 0) + \mu(1, 0, -3)\).
:::

### The plane through three points

Three points that are not in a line lie in exactly one plane. Use two of them to make two directions, and the vector product to find the normal.

:::steps
1. Form two vectors in the plane, for example \(\overrightarrow{AB}\) and \(\overrightarrow{AC}\).
2. Their vector product \(\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}\) is a normal.
3. Find \(p = \mathbf{a}\cdot\mathbf{n}\) from any one of the points.
4. Write \(\mathbf{r}\cdot\mathbf{n} = p\) or the Cartesian form, and check the other two points.
:::

:::eg (Exam style) The points \(A\), \(B\) and \(C\) have coordinates \((2, 1, -1)\), \((4, 0, 1)\) and \((3, 3, 2)\). Find the Cartesian equation of the plane through \(A\), \(B\) and \(C\).
The two vectors in the plane:
\[\overrightarrow{AB} = \begin{pmatrix}2\\-1\\2\end{pmatrix}, \qquad \overrightarrow{AC} = \begin{pmatrix}1\\2\\3\end{pmatrix}\] [M1]
The vector product gives a normal:
\[\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}(-1)(3) - (2)(2)\\ (2)(1) - (2)(3)\\ (2)(2) - (-1)(1)\end{pmatrix}\] [M1]
\[\mathbf{n} = \begin{pmatrix}-7\\-4\\5\end{pmatrix}\] [A1]
Use the point \(A\) to find the constant:
\[-7(2) - 4(1) + 5(-1) = -14 - 4 - 5 = -23\] [M1]
The plane is \(-7x - 4y + 5z = -23\), which is the same as
\[7x + 4y - 5z = 23\] [A1]
**Check** with \(B\): \(28 + 0 - 5 = 23\) ✓, and with \(C\): \(21 + 12 - 10 = 23\) ✓.
:::

In the exam the marks go to the working in this order: a pair of vectors in the plane, the vector product, the correct normal, the constant, the equation. A final check with the other two points is not marked but is how you catch a slip in the normal.

:::exam Three points, one plane
A question that asks for "the equation of the plane through \(A\), \(B\) and \(C\)" does not say which form. Give the Cartesian form \(ax + by + cz = d\) unless the question names another, and say what you are doing: "A normal is \(\overrightarrow{AB} \times \overrightarrow{AC}\)". Using the vector product as a normal to the plane is expected and needs no further justification; use all three points to check.
:::

### Other ways to fix a plane

The same idea, "find two directions in the plane and cross them", solves a family of problems. In each, name the two directions first.

:::eg Find the Cartesian equation of the plane that contains the line \(l: \mathbf{r} = \begin{pmatrix}1\\2\\0\end{pmatrix} + t\begin{pmatrix}2\\1\\-1\end{pmatrix}\) and the point \(P(3, -1, 4)\).
Directions in the plane: the direction of the line, \(\mathbf{d} = (2, 1, -1)\), and the vector from a point on the line, \(A(1, 2, 0)\), to \(P\):
\[\overrightarrow{AP} = \begin{pmatrix}2\\-3\\4\end{pmatrix}\]
The normal is
\[\mathbf{d} \times \overrightarrow{AP} = \begin{pmatrix}(1)(4) - (-1)(-3)\\ (-1)(2) - (2)(4)\\ (2)(-3) - (1)(2)\end{pmatrix} = \begin{pmatrix}1\\-10\\-8\end{pmatrix}\]
Use \(A\): \(p = 1 - 20 + 0 = -19\). The plane is \(x - 10y - 8z = -19\).

**Check** with \(P\): \(3 + 10 - 32 = -19\). ✓ Check another point of the line, at \(t = 1\), which is \((3, 3, -1)\): \(3 - 30 + 8 = -19\). ✓
:::

:::eg Find the plane that is the perpendicular bisector of \(AB\), where \(A(1, 2, 3)\) and \(B(5, 0, 7)\). That is, the set of points equidistant from \(A\) and \(B\).
The plane is perpendicular to \(AB\), so a normal is \(\overrightarrow{AB} = (4, -2, 4)\), which we can shorten to \((2, -1, 2)\). It passes through the midpoint of \(AB\), \(M(3, 1, 5)\). Then
\[p = 2(3) - 1(1) + 2(5) = 15\]
The plane is \(2x - y + 2z = 15\).

**Check** that \(A\) and \(B\) are on opposite sides at equal distances: the left side gives \(2 - 2 + 6 = 6\) at \(A\) and \(10 - 0 + 14 = 24\) at \(B\), which are \(9\) below and \(9\) above \(15\). ✓
:::

Two lines that meet (or that are parallel) also lie in one plane. If they meet, their two directions are the two directions of the plane and the meeting point is a point of it. If they are parallel, use the common direction and the vector between a point on each. Two **skew** lines are not in any plane together.

:::eg The lines \(l_1: \mathbf{r} = \begin{pmatrix}0\\1\\1\end{pmatrix} + s\begin{pmatrix}1\\1\\0\end{pmatrix}\) and \(l_2: \mathbf{r} = \begin{pmatrix}1\\0\\-3\end{pmatrix} + t\begin{pmatrix}0\\1\\2\end{pmatrix}\) meet at the point \(M(1, 2, 1)\). Find the Cartesian equation of the plane that contains both lines, and the equation of the parallel plane through \((1, 1, 1)\).
Check the meeting point: \(s = 1\) gives \((1, 2, 1)\) on \(l_1\), and \(t = 2\) gives \((1, 2, 1)\) on \(l_2\). ✓

The directions of the lines lie in the plane, so
\[\mathbf{n} = \begin{pmatrix}1\\1\\0\end{pmatrix} \times \begin{pmatrix}0\\1\\2\end{pmatrix} = \begin{pmatrix}1 \times 2 - 0 \times 1\\ 0 \times 0 - 1 \times 2\\ 1 \times 1 - 1 \times 0\end{pmatrix} = \begin{pmatrix}2\\-2\\1\end{pmatrix}\]
Use \(M\): \(p = 2 - 4 + 1 = -1\), so the plane is \(2x - 2y + z = -1\). **Check** the other points: \((0, 1, 1)\) gives \(-2 + 1 = -1\) ✓ and \((1, 0, -3)\) gives \(2 - 3 = -1\) ✓.

A parallel plane has the same normal and a different constant. Through \((1, 1, 1)\): \(2 - 2 + 1 = 1\), so the plane is \(2x - 2y + z = 1\).
:::

:::eg A roof is a plane through the points \(P(0, 0, 3)\), \(Q(6, 0, 3)\) and \(R(0, 4, 5)\), with coordinates in metres and \(z\) the height. Find its equation, and the height of the roof above the point with \(x = 3\), \(y = 3\).
\[\overrightarrow{PQ} = \begin{pmatrix}6\\0\\0\end{pmatrix}, \qquad \overrightarrow{PR} = \begin{pmatrix}0\\4\\2\end{pmatrix}\]
\[\overrightarrow{PQ} \times \overrightarrow{PR} = \begin{pmatrix}0\\-12\\24\end{pmatrix} = 12\begin{pmatrix}0\\-1\\2\end{pmatrix}\]
A normal is \((0, -1, 2)\). Using \(P\): \(p = 0 - 0 + 6 = 6\), so the roof is
\[-y + 2z = 6 \quad\text{or}\quad z = 3 + \tfrac12 y\]
At \(x = 3\), \(y = 3\): \(z = 3 + 1.5 = 4.5\) m. The roof rises 0.5 m for every metre in the \(y\) direction and does not change with \(x\), which agrees with the zero \(x\) component of the normal.
:::

The next chapter, [Vectors: intersections, angles and distances](#math.fm.vectors2), uses this roof again to find the slope and the distance of a drone above it.

:::board
The vector product and the equations of planes are Further Mathematics content on the UK specifications (Edexcel, AQA and OCR) as well; none of it is in single A Level Mathematics. In 9231 they are in Paper 1.
:::

:::exam What MF19 gives you
The vector product and the forms of a plane are not on MF19: learn \(\mathbf{a} \times \mathbf{b}\) in components, \(|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta\), and the three forms of a plane. Learn also \(\mathbf{r}\cdot\mathbf{n} = p\) with \(p = \mathbf{a}\cdot\mathbf{n}\). Give exact values (\(3\sqrt{17}\)) or 3 s.f., and angles to 1 d.p. unless the question says otherwise.
:::

:::eg Spot the error: find \(\mathbf{a} \times \mathbf{b}\) for \(\mathbf{a} = \begin{pmatrix}2\\1\\-3\end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix}4\\-1\\2\end{pmatrix}\), for 3 marks (M1 for the method, A1 for two correct components, A1 for all three).
A student wrote this answer.

Line 1: \(\mathbf{i}\): \((1)(2) - (-3)(-1) = 2 - 3 = -1\)
Line 2: \(\mathbf{j}\): \((2)(2) - (-3)(4) = 4 + 12 = 16\)
Line 3: \(\mathbf{k}\): \((2)(-1) - (1)(4) = -2 - 4 = -6\)
Line 4: \(\mathbf{a} \times \mathbf{b} = \begin{pmatrix}-1\\16\\-6\end{pmatrix}\)

Lines 1 and 3 are correct, and the method is right. [M1] Two components are correct. [A1]

**Line 2 has the wrong sign.** [A0] The student used \(a_1b_3 - a_3b_1\), which is \(\mathbf{j}\) in the determinant layout before the minus sign is applied. The correct component is \(a_3b_1 - a_1b_3 = (-3)(4) - (2)(2) = -16\). [A1] The student scores 2 out of 3.

**Check** that would have caught it: \(\mathbf{a}\cdot(\mathbf{a} \times \mathbf{b}) = -2 + 16 + 18 = 32 \ne 0\), but the correct vector \(\begin{pmatrix}-1\\-16\\-6\end{pmatrix}\) gives \(-2 - 16 + 18 = 0\). ✓
:::

:::try Start easy, finish at exam standard
Q: Find \(\mathbf{a} \times \mathbf{b}\) for \(\mathbf{a} = \begin{pmatrix}3\\-1\\2\end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix}1\\4\\-2\end{pmatrix}\).
A: \(\mathbf{i}\): \((-1)(-2) - (2)(4) = -6\). \(\mathbf{j}\): \((2)(1) - (3)(-2) = 8\). \(\mathbf{k}\): \((3)(4) - (-1)(1) = 13\). So \(\mathbf{a} \times \mathbf{b} = \begin{pmatrix}-6\\8\\13\end{pmatrix}\). Check with \(\mathbf{a}\): \(-18 - 8 + 26 = 0\).
Q: Show that \(\mathbf{a} = \begin{pmatrix}2\\-4\\6\end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix}-1\\2\\-3\end{pmatrix}\) are parallel using the vector product.
A: \(\mathbf{i}\): \((-4)(-3) - (6)(2) = 0\). \(\mathbf{j}\): \((6)(-1) - (2)(-3) = 0\). \(\mathbf{k}\): \((2)(2) - (-4)(-1) = 0\). The product is \(\mathbf{0}\), so the vectors are parallel (indeed \(\mathbf{a} = -2\mathbf{b}\)).
Q: Find a vector perpendicular to both \(\begin{pmatrix}1\\0\\2\end{pmatrix}\) and \(\begin{pmatrix}3\\-1\\1\end{pmatrix}\).
A: The vector product: \(\mathbf{i}\): \(0 \times 1 - 2 \times (-1) = 2\); \(\mathbf{j}\): \(2 \times 3 - 1 \times 1 = 5\); \(\mathbf{k}\): \(1 \times (-1) - 0 \times 3 = -1\). The vector is \(\begin{pmatrix}2\\5\\-1\end{pmatrix}\) (or any multiple).
Q: Find the area of the triangle with vertices \(P(3, 0, 0)\), \(Q(0, 4, 0)\) and \(R(0, 0, 2)\).
A: \(\overrightarrow{PQ} = (-3, 4, 0)\) and \(\overrightarrow{PR} = (-3, 0, 2)\). Their vector product is \(\begin{pmatrix}8\\6\\12\end{pmatrix} = 2\begin{pmatrix}4\\3\\6\end{pmatrix}\), of length \(2\sqrt{61}\). Area \(= \sqrt{61} = 7.81\).
Q: Write down the vector and Cartesian equations of the plane through \((2, 0, -1)\) with normal \(\mathbf{i} - 2\mathbf{j} + 3\mathbf{k}\).
A: \(p = 2 + 0 - 3 = -1\). The plane is \(\mathbf{r}\cdot(\mathbf{i} - 2\mathbf{j} + 3\mathbf{k}) = -1\), that is \(x - 2y + 3z = -1\).
Q: Find the distance of the plane \(2x - y + 4z = 8\) from the origin.
A: \(|\mathbf{n}| = \sqrt{4 + 1 + 16} = \sqrt{21}\), so the distance is \(\dfrac{8}{\sqrt{21}} = 1.75\) (3 s.f.).
Q: Does the point \((1, 2, -1)\) lie in the plane \(3x + y - 2z = 7\)?
A: \(3 + 2 + 2 = 7\). Yes, it does.
Q: Find a Cartesian equation of the plane \(\mathbf{r} = \begin{pmatrix}1\\1\\0\end{pmatrix} + \lambda\begin{pmatrix}1\\0\\2\end{pmatrix} + \mu\begin{pmatrix}0\\3\\1\end{pmatrix}\).
A: \(\mathbf{n} = \begin{pmatrix}0 \times 1 - 2 \times 3\\ 2 \times 0 - 1 \times 1\\ 1 \times 3 - 0 \times 0\end{pmatrix} = \begin{pmatrix}-6\\-1\\3\end{pmatrix}\). Then \(p = -6 - 1 + 0 = -7\), so \(-6x - y + 3z = -7\), that is \(6x + y - 3z = 7\).
Q: Find the plane through \(A(1, 1, 1)\), \(B(2, 0, 3)\) and \(C(0, 2, 2)\).
A: \(\overrightarrow{AB} = (1, -1, 2)\), \(\overrightarrow{AC} = (-1, 1, 1)\). The product is \(\begin{pmatrix}-3\\-3\\0\end{pmatrix}\), so a normal is \((1, 1, 0)\) and \(p = 1 + 1 = 2\). The plane is \(x + y = 2\). All three points satisfy it.
Q: Write the plane \(x + 2y - z = 4\) in the form \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\).
A: A point is \((4, 0, 0)\). Two directions with \(\mathbf{b}\cdot\mathbf{n} = 0\): \((-2, 1, 0)\) and \((1, 0, 1)\). One answer is \(\mathbf{r} = \begin{pmatrix}4\\0\\0\end{pmatrix} + \lambda\begin{pmatrix}-2\\1\\0\end{pmatrix} + \mu\begin{pmatrix}1\\0\\1\end{pmatrix}\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find \(\mathbf{a} \times \mathbf{b}\), where \(\mathbf{a} = \begin{pmatrix}4\\-1\\2\end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix}-1\\3\\1\end{pmatrix}\).
A: \(\mathbf{a} \times \mathbf{b} = \begin{pmatrix}(-1)(1) - (2)(3)\\ (2)(-1) - (4)(1)\\ (4)(3) - (-1)(-1)\end{pmatrix}\) [M1] \(= \begin{pmatrix}-7\\-6\\11\end{pmatrix}\). [A1] [A1]
Q: [4 marks] ★ The points \(A\), \(B\) and \(C\) have coordinates \((2, -1, 0)\), \((3, 1, 2)\) and \((-1, 2, 1)\). Find the area of triangle \(ABC\).
A: \(\overrightarrow{AB} = (1, 2, 2)\) and \(\overrightarrow{AC} = (-3, 3, 1)\). [B1]
\(\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}2 \times 1 - 2 \times 3\\ 2 \times (-3) - 1 \times 1\\ 1 \times 3 - 2 \times (-3)\end{pmatrix}\) [M1] \(= \begin{pmatrix}-4\\-7\\9\end{pmatrix}\). [A1]
Area \(= \tfrac12\sqrt{16 + 49 + 81} = \tfrac12\sqrt{146} = 6.04\). [A1]
Q: [5 marks] ★★ The points \(A\), \(B\) and \(C\) have coordinates \((1, 0, -1)\), \((2, 3, 1)\) and \((0, 1, 4)\). Find the Cartesian equation of the plane \(ABC\).
A: \(\overrightarrow{AB} = (1, 3, 2)\) and \(\overrightarrow{AC} = (-1, 1, 5)\). [M1]
\(\mathbf{n} = \begin{pmatrix}3 \times 5 - 2 \times 1\\ 2 \times (-1) - 1 \times 5\\ 1 \times 1 - 3 \times (-1)\end{pmatrix}\) [M1] \(= \begin{pmatrix}13\\-7\\4\end{pmatrix}\). [A1]
Using \(A\): \(13 - 0 - 4 = 9\). [M1] The plane is \(13x - 7y + 4z = 9\). [A1]
Q: [5 marks] ★★ The plane \(\Pi\) has equation \(\mathbf{r} = \begin{pmatrix}2\\-1\\3\end{pmatrix} + \lambda\begin{pmatrix}1\\-2\\0\end{pmatrix} + \mu\begin{pmatrix}3\\1\\-1\end{pmatrix}\). (a) Find a Cartesian equation of \(\Pi\). (b) Show that the point \((0, 3, 3)\) lies in \(\Pi\).
A: (a) \(\mathbf{n} = \begin{pmatrix}(-2)(-1) - 0 \times 1\\ 0 \times 3 - 1 \times (-1)\\ 1 \times 1 - (-2)(3)\end{pmatrix}\) [M1] \(= \begin{pmatrix}2\\1\\7\end{pmatrix}\). [A1]
\(p = 4 - 1 + 21 = 24\) [M1], so \(2x + y + 7z = 24\). [A1]
(b) \(0 + 3 + 21 = 24\), so the point lies in \(\Pi\). [B1]
Q: [7 marks] ★★ The points \(A\) and \(B\) have coordinates \((-1, 2, 3)\) and \((3, 0, -1)\). The plane \(\Pi\) is the perpendicular bisector of \(AB\): every point of \(\Pi\) is the same distance from \(A\) as from \(B\). (a) Find a Cartesian equation of \(\Pi\). (b) Find the distance of \(\Pi\) from the origin.
A: (a) The midpoint is \((1, 1, 1)\). [B1] A normal is \(\overrightarrow{AB} = (4, -2, -4)\), or \((2, -1, -2)\). [M1] [A1]
\(p = 2 - 1 - 2 = -1\) [M1], so \(2x - y - 2z = -1\). [A1]
(b) \(|\mathbf{n}| = \sqrt{4 + 1 + 4} = 3\), so the distance is \(\dfrac{|-1|}{3}\) [M1] \(= \dfrac13\). [A1]
Q: [10 marks] (#math.p3.vectors) ★★★ The line \(l\) has equation \(\mathbf{r} = \begin{pmatrix}0\\1\\3\end{pmatrix} + t\begin{pmatrix}1\\-1\\2\end{pmatrix}\) and the point \(P\) has coordinates \((2, 2, -1)\). (a) Show that \(P\) does not lie on \(l\). (b) Find a Cartesian equation of the plane \(\Pi\) containing \(l\) and \(P\). (c) The points \(A\) and \(B\) on \(l\) correspond to \(t = 0\) and \(t = 2\). Find the area of triangle \(ABP\).
H: For (a), equate the \(x\) coordinates to find \(t\), then test the \(y\) coordinate.
H: For (b), two directions in the plane are the direction of \(l\) and \(\overrightarrow{AP}\), where \(A\) is on \(l\).
H: For (c), \(\overrightarrow{AB} = 2\mathbf{d}\), and \(\overrightarrow{AB} \times \overrightarrow{AP}\) is twice the vector product you found in (b).
A: (a) \(x = t = 2\) gives \(y = 1 - 2 = -1 \ne 2\). [M1] So \(P\) is not on \(l\). [A1]
(b) \(A = (0, 1, 3)\) and \(\overrightarrow{AP} = (2, 1, -4)\). [B1]
\(\mathbf{n} = \begin{pmatrix}1\\-1\\2\end{pmatrix} \times \begin{pmatrix}2\\1\\-4\end{pmatrix} = \begin{pmatrix}(-1)(-4) - 2 \times 1\\ 2 \times 2 - 1 \times (-4)\\ 1 \times 1 - (-1)(2)\end{pmatrix}\) [M1] \(= \begin{pmatrix}2\\8\\3\end{pmatrix}\). [A1]
\(p = 0 + 8 + 9 = 17\) [M1], so \(2x + 8y + 3z = 17\). [A1]
Check with \(P\): \(4 + 16 - 3 = 17\).
(c) \(\overrightarrow{AB} = 2(1, -1, 2) = (2, -2, 4)\), so \(\overrightarrow{AB} \times \overrightarrow{AP} = 2\begin{pmatrix}2\\8\\3\end{pmatrix}\). [M1]
Area \(= \tfrac12 \times 2\sqrt{4 + 64 + 9} = \sqrt{77}\) [M1] \(= 8.77\). [A1]
Q: [11 marks] ★★★ The points \(A\), \(B\), \(C\) have coordinates \((1, 0, 0)\), \((0, 2, 0)\), \((0, 0, 3)\) and \(O\) is the origin. (a) Find a Cartesian equation of the plane \(ABC\). (b) Find the area of triangle \(ABC\). (c) Find the distance of \(O\) from the plane \(ABC\). (d) Hence find the volume of the tetrahedron \(OABC\), using volume \(= \tfrac13 \times\) base area \(\times\) height.
H: For (a), \(\overrightarrow{AB} = (-1, 2, 0)\) and \(\overrightarrow{AC} = (-1, 0, 3)\).
H: The vector product you found in (a) is also the one you need for (b).
H: In (d) take triangle \(ABC\) as the base, so the height is the distance from \(O\) found in (c).
A: (a) \(\overrightarrow{AB} = (-1, 2, 0)\), \(\overrightarrow{AC} = (-1, 0, 3)\). [M1]
\(\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}2 \times 3 - 0 \times 0\\ 0 \times (-1) - (-1)(3)\\ (-1)(0) - 2 \times (-1)\end{pmatrix}\) [M1] \(= \begin{pmatrix}6\\3\\2\end{pmatrix}\). [A1]
Using \(A\): \(p = 6\) [M1], so \(6x + 3y + 2z = 6\). [A1]
(b) \(\left|\overrightarrow{AB} \times \overrightarrow{AC}\right| = \sqrt{36 + 9 + 4} = 7\) [M1], so the area is \(\tfrac72\). [A1]
(c) Distance \(= \dfrac{6}{7}\) [M1 A1].
(d) Volume \(= \tfrac13 \times \tfrac72 \times \tfrac67\) [M1] \(= 1\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The tetrahedron \(OABC\) has \(O\) at the origin, \(A(4, 0, 0)\), \(B(0, 6, 0)\) and \(C(2, 3, h)\), where \(h > 0\). (a) Show that the volume of a tetrahedron \(OABC\) is \(\tfrac16\left|\mathbf{c}\cdot(\mathbf{a} \times \mathbf{b})\right|\), where \(\mathbf{a}\), \(\mathbf{b}\), \(\mathbf{c}\) are the position vectors of \(A\), \(B\), \(C\). (b) The volume is 12. Find \(h\).
H: The base \(OAB\) has area \(\tfrac12|\mathbf{a} \times \mathbf{b}|\). The height is the length of the part of \(\mathbf{c}\) along the unit normal \(\dfrac{\mathbf{a} \times \mathbf{b}}{|\mathbf{a} \times \mathbf{b}|}\).
H: Use volume \(= \tfrac13 \times\) base \(\times\) height, and the scalar product to find the component of \(\mathbf{c}\) along the normal.
A: (a) Base \(OAB\) has area \(\tfrac12|\mathbf{a} \times \mathbf{b}|\). [B1] The height of \(C\) above the plane \(OAB\) is the component of \(\mathbf{c}\) along the unit normal, \(\dfrac{|\mathbf{c}\cdot(\mathbf{a} \times \mathbf{b})|}{|\mathbf{a} \times \mathbf{b}|}\). [M1]
\[V = \tfrac13 \times \tfrac12|\mathbf{a} \times \mathbf{b}| \times \frac{|\mathbf{c}\cdot(\mathbf{a} \times \mathbf{b})|}{|\mathbf{a} \times \mathbf{b}|} = \tfrac16|\mathbf{c}\cdot(\mathbf{a} \times \mathbf{b})|\] [A1]
(b) \(\mathbf{a} \times \mathbf{b} = \begin{pmatrix}0\\0\\24\end{pmatrix}\). [M1] Then \(\mathbf{c}\cdot(\mathbf{a} \times \mathbf{b}) = 24h\), so \(V = 4h\). [A1] \(4h = 12\), so \(h = 3\). [A1]
Q: [6 marks] ★★★ A plane meets the axes at \(A(p, 0, 0)\), \(B(0, q, 0)\) and \(C(0, 0, r)\), where \(p, q, r > 0\). (a) Show that its equation is \(\dfrac{x}{p} + \dfrac{y}{q} + \dfrac{z}{r} = 1\). (b) Find the areas of the triangles \(OAB\), \(OBC\), \(OCA\) and \(ABC\) for \(p = 2\), \(q = 3\), \(r = 6\), and check that the area of \(ABC\) squared equals the sum of the squares of the other three.
H: For (a), check that each of the three points satisfies the equation, and that the equation is linear in \(x, y, z\).
H: For \(ABC\), use \(\overrightarrow{AB} \times \overrightarrow{AC}\) with \(\overrightarrow{AB} = (-2, 3, 0)\) and \(\overrightarrow{AC} = (-2, 0, 6)\).
A: (a) The equation is of the form \(ax + by + cz = d\), so it is a plane. [B1] \(A\) gives \(\frac{p}{p} = 1\), \(B\) gives \(\frac{q}{q} = 1\) and \(C\) gives \(\frac{r}{r} = 1\), so all three points lie in it; three non-collinear points fix the plane. [B1]
(b) \(OAB\): \(\tfrac12 \times 2 \times 3 = 3\); \(OBC\): \(\tfrac12 \times 3 \times 6 = 9\); \(OCA\): \(\tfrac12 \times 6 \times 2 = 6\). [B1]
\(\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix}18\\12\\6\end{pmatrix}\) [M1], so the area of \(ABC\) is \(\tfrac12\sqrt{324 + 144 + 36} = 3\sqrt{14}\). [A1]
\(\left(3\sqrt{14}\right)^2 = 126 = 9 + 81 + 36\). [B1]
:::

:::quiz
? What is \(\mathbf{j} \times \mathbf{i}\)?
+ \(-\mathbf{k}\)
- \(\mathbf{k}\)
- \(\mathbf{0}\)
- \(-\mathbf{j}\)
> Going \(\mathbf{i}\) to \(\mathbf{j}\) gives \(+\mathbf{k}\), so reversing the order gives \(-\mathbf{k}\). The answer \(\mathbf{k}\) forgets that the product is not commutative; \(\mathbf{0}\) is the result only for parallel vectors.
? \(\mathbf{a} \times \mathbf{b} = \mathbf{0}\) for two non-zero vectors. What does that tell you?
+ \(\mathbf{a}\) and \(\mathbf{b}\) are parallel
- \(\mathbf{a}\) and \(\mathbf{b}\) are perpendicular
- \(\mathbf{a}\) and \(\mathbf{b}\) have the same length
- \(\mathbf{a}\) and \(\mathbf{b}\) are not in the same plane
> The length \(|\mathbf{a}||\mathbf{b}|\sin\theta\) is zero only when \(\sin\theta = 0\), that is when the vectors are parallel. Perpendicular vectors have \(\mathbf{a}\cdot\mathbf{b} = 0\) instead, which is the scalar product.
? Which is a normal vector to the plane \(3x - 2y + 5z = 7\)?
+ \(\begin{pmatrix}3\\-2\\5\end{pmatrix}\)
- \(\begin{pmatrix}3\\-2\\5\\7\end{pmatrix}\)
- \(\begin{pmatrix}7\\3\\-2\end{pmatrix}\)
- \(\begin{pmatrix}3\\2\\5\end{pmatrix}\)
> The coefficients of \(x, y, z\) form a normal vector, with their signs. The 7 is the constant \(d\), not part of the normal, and changing the sign of one component changes the direction.
? What is the distance of the plane \(2x - y + 2z = 9\) from the origin?
+ \(3\)
- \(9\)
- \(1\)
- \(\dfrac{9}{\sqrt{5}}\)
> \(|\mathbf{n}| = \sqrt{4 + 1 + 4} = 3\), so the distance is \(9 \div 3 = 3\). The answer 9 forgets to divide by \(|\mathbf{n}|\); 1 divides the wrong way round; \(\dfrac{9}{\sqrt5}\) leaves one coefficient out of \(|\mathbf{n}|\) (\(4 + 1 = 5\) instead of \(4 + 1 + 4 = 9\)).
? Which is a correct vector equation of the plane \(3x - 2y + z = 6\)?
+ \(\mathbf{r} = (2, 0, 0) + \lambda(1, 0, -3) + \mu(0, 1, 2)\)
- \(\mathbf{r} = (2, 0, 0) + \lambda(3, -2, 1) + \mu(0, 1, 2)\)
- \(\mathbf{r} = (1, 0, 0) + \lambda(1, 0, -3) + \mu(0, 1, 2)\)
- \(\mathbf{r} = (2, 0, 0) + \lambda(1, 0, -3) + \mu(2, 0, -6)\)
> Directions must satisfy \(\mathbf{b}\cdot\mathbf{n} = 0\) and not be parallel, and the first vector must be a point of the plane. The second option uses the normal itself as a direction, the third starts at \((1, 0, 0)\), which gives \(3 \ne 6\), and in the fourth the two directions are parallel, so it describes only a line.
? A triangle has sides \(\overrightarrow{AB}\) and \(\overrightarrow{AC}\). What is its area?
+ \(\tfrac12\left|\overrightarrow{AB} \times \overrightarrow{AC}\right|\)
- \(\left|\overrightarrow{AB} \times \overrightarrow{AC}\right|\)
- \(\tfrac12\overrightarrow{AB}\cdot\overrightarrow{AC}\)
- \(\tfrac12\left|\overrightarrow{AB}\right|\left|\overrightarrow{AC}\right|\)
> The vector product's length is the area of the parallelogram, so the triangle is half of it. The scalar product gives a number related to the cosine of the angle, not an area, and the last option is a right-angled triangle's area, which needs \(\sin\theta\) in general.
:::

:::checklist What you can now do
- [ ] I can recall and use \(\mathbf{a} \times \mathbf{b} = |\mathbf{a}||\mathbf{b}|\sin\theta\,\hat{\mathbf{n}}\) and its component form, and check a result is perpendicular to both vectors.
- [ ] I can use the properties of the vector product: it reverses on swapping the vectors, and it is zero for parallel vectors.
- [ ] I can find the area of a triangle or parallelogram from a vector product.
- [ ] I can write the equation of a plane in the forms \(\mathbf{r}\cdot\mathbf{n} = p\) and \(ax + by + cz = d\), and read off a normal vector.
- [ ] I can write the equation of a plane as \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\) and find its normal with \(\mathbf{b} \times \mathbf{c}\).
- [ ] I can convert a plane between vector, Cartesian and parametric forms.
- [ ] I can find the plane through three points, through a line and a point, and the perpendicular bisector of two points.
- [ ] I can find the distance of a plane from the origin and decide whether a point lies in a plane.
:::

:::recap
- \(\mathbf{a} \times \mathbf{b} = |\mathbf{a}||\mathbf{b}|\sin\theta\,\hat{\mathbf{n}}\) with \(\hat{\mathbf{n}}\) from the right-hand rule. In components the \(\mathbf{i}\), \(\mathbf{j}\), \(\mathbf{k}\) parts are \(a_2b_3 - a_3b_2\), \(a_3b_1 - a_1b_3\) and \(a_1b_2 - a_2b_1\).
- \(\mathbf{a} \times \mathbf{b}\) is perpendicular to both; \(\mathbf{b} \times \mathbf{a} = -\mathbf{a} \times \mathbf{b}\); it is \(\mathbf{0}\) for parallel vectors. Check every result with two scalar products.
- Parallelogram area \(|\mathbf{a} \times \mathbf{b}|\); triangle area \(\tfrac12|\overrightarrow{AB} \times \overrightarrow{AC}|\).
- Plane with normal \(\mathbf{n}\) through \(A\): \(\mathbf{r}\cdot\mathbf{n} = p\), \(p = \mathbf{a}\cdot\mathbf{n}\); Cartesian \(ax + by + cz = d\) with \(\mathbf{n} = (a, b, c)\).
- Parametric form \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}\): one point, two non-parallel directions; the normal is \(\mathbf{b} \times \mathbf{c}\).
- Three points: normal \(\overrightarrow{AB} \times \overrightarrow{AC}\), then \(p\) from one point, and check with the others.
- Distance of the plane from the origin: \(\dfrac{|p|}{|\mathbf{n}|}\). Parallel planes have parallel normals.
- None of this is on MF19.
:::

:::links
- watch: [Cross products](https://www.3blue1brown.com/lessons/cross-products) · 3Blue1Brown · why the vector product is the area and the perpendicular direction, with animations
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · vectors and planes questions with answers
- practise: [Linear algebra](https://www.khanacademy.org/math/linear-algebra) · Khan Academy · cross product and planes, with exercises
- explore: [Desmos 3D](https://www.desmos.com/3d) · Desmos · type a plane such as 3x - 2y + z = 6 and rotate it
- explore: [GeoGebra 3D](https://www.geogebra.org/3d) · GeoGebra · draw three points and the plane through them
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 vector and plane questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Vectors: intersections, angles and distances](#math.fm.vectors2) uses planes and the vector product to find where lines and planes meet, and the angles and distances between them.
