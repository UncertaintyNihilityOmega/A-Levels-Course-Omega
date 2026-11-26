@chapter math.fm.transform
@title Matrices as transformations
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 5–7 hours
@summary Every 2×2 matrix moves the points of the plane, and its columns tell you exactly how. You will write down the matrices for rotations, reflections, enlargements, stretches and shears, combine and undo transformations with matrix products and inverses, use the determinant as an area scale factor, and find invariant points and invariant lines.

:::why
Geometry and algebra meet here. A matrix is a rule that sends each point to a new point; the product of matrices is "do one transformation after another"; the inverse is "undo it"; and the determinant says how much areas grow. Computer graphics, robotics and physics all rest on this, and in the Paper 2 chapters the invariant lines you find here become the eigenvectors of a matrix.
:::

**Before you start**, you need matrix products, determinants and inverses from [Matrices: algebra, determinants and inverses](#math.fm.matrices), exact values of sines and cosines from [Trigonometry](#math.p1.trig), and equations of lines through the origin from [Coordinate geometry](#math.p1.coord).

:::try Warm-up
Q: Write down the exact values of \(\cos 30^\circ\) and \(\sin 30^\circ\). (from [Trigonometry](#math.p1.trig))
A: \(\cos 30^\circ = \dfrac{\sqrt3}{2}\) and \(\sin 30^\circ = \dfrac12\).
Q: Solve \(2m^2 + m - 1 = 0\). (from [Quadratics](#math.p1.quadratics))
A: \((2m - 1)(m + 1) = 0\), so \(m = \tfrac12\) or \(m = -1\).
Q: Find \(\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 4 \end{pmatrix}\). (from [Matrices: algebra, determinants and inverses](#math.fm.matrices))
A: \(\begin{pmatrix} 3 + 8 \\ 4 \end{pmatrix} = \begin{pmatrix} 11 \\ 4 \end{pmatrix}\).
:::

## A matrix moves points

A point \((x, y)\) can be written as a column \(\begin{pmatrix} x \\ y \end{pmatrix}\) (its position vector). Multiplying a 2×2 matrix by this column gives another column, which is another point:
\[\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} ax + by \\ cx + dy \end{pmatrix}\]
So each matrix \(\mathbf{M}\) sends every point \(P\) to an **image** \(P'\), and we say \(\mathbf{M}\) represents a **transformation** of the \(x\)-\(y\) plane. The origin always stays where it is, because \(\mathbf{M}\begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\). The syllabus restricts itself to these origin-fixing, "linear" transformations.

### The columns are the images of the axes

The next idea makes the whole chapter easy. Take the two points \((1, 0)\) and \((0, 1)\), which are the ends of the unit vectors \(\mathbf{i}\) and \(\mathbf{j}\):
\[\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ c \end{pmatrix} \qquad \begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} b \\ d \end{pmatrix}\]

:::key The columns of a matrix
The first column of \(\mathbf{M}\) is the image of \((1, 0)\) and the second column is the image of \((0, 1)\). To find the matrix of a transformation, work out where it sends \((1, 0)\) and \((0, 1)\) and write the results as columns.
This is enough to know the whole transformation, because every point is \(x\mathbf{i} + y\mathbf{j}\) and so its image is \(x\) times the first column plus \(y\) times the second.
:::

:::eg A transformation sends \((1, 0)\) to \((3, 1)\) and \((0, 1)\) to \((-2, 2)\). Write down its matrix and find the image of \((2, 3)\).
The images are the columns:
\[\mathbf{M} = \begin{pmatrix} 3 & -2 \\ 1 & 2 \end{pmatrix}\]
The image of \((2, 3)\) is
\[\begin{pmatrix} 3 & -2 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 - 6 \\ 2 + 6 \end{pmatrix} = \begin{pmatrix} 0 \\ 8 \end{pmatrix}\]
So \((2, 3)\) is sent to \((0, 8)\). **Check**: \(2 \times (3, 1) + 3 \times (-2, 2) = (0, 8)\).
:::

Here is the picture for the matrix \(\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\). The unit square \(OABC\) is mapped to the parallelogram \(OAB'C'\).

:::html
<figure class="fig small"><svg viewBox="0 50 290 150" role="img" aria-label="The unit square OABC with O at the origin, A at (1, 0), B at (1, 1) and C at (0, 1), and its image under the matrix with rows 1 2 and 0 1: the parallelogram OAB′C′ with A unchanged, C′ at (2, 1) and B′ at (3, 1). Both have area 1.">
<line class="ax" x1="20" y1="150" x2="275" y2="150" marker-end="url(#ah)"/>
<line class="ax" x1="40" y1="165" x2="40" y2="62" marker-end="url(#ah)"/>
<polygon class="f2 s-acc2 sw2" points="40,150 110,150 250,80 180,80"/>
<polygon class="f1 s-acc sw2" points="40,150 110,150 110,80 40,80"/>
<text class="tl" x="22" y="166">O</text>
<text class="tl tc" x="110" y="170">A, A′</text>
<text class="tl tc" x="110" y="70">B</text>
<text class="tl tc" x="180" y="70">C′</text>
<text class="tl tc" x="250" y="70">B′</text>
<text class="tl tc" x="26" y="84">C</text>
<text class="tl" x="268" y="168">x</text>
<text class="tl" x="48" y="66">y</text>
</svg><figcaption>The unit square \(OABC\) and its image under \(\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\). The first column \((1, 0)\) is where \(A\) goes (it does not move); the second column \((2, 1)\) is where \(C\) goes, so \(C'\) is \((2, 1)\). Both shapes have area 1: this is a shear, and \(\det = 1\).</figcaption></figure>
:::

Try the tool below. It draws a shape and its image under the matrix whose four entries you set, with the images of \(\mathbf{i}\) and \(\mathbf{j}\) as arrows. Change the second column and watch the top of the shape slide; set the first column to \((0, 1)\) and the second to \((-1, 0)\) and the shape turns through a quarter turn.

:::html
<div class="widget" data-w="fm-matrix" data-m="1,2,0,1" data-shape="square" data-show="grid,det" data-presets="rotation,reflection,shear,stretch,enlargement"></div>
:::

## The standard transformations

Each of these is found by asking where \((1, 0)\) and \((0, 1)\) go. All angles are measured **anticlockwise** from the positive \(x\)-axis, and rotation angles are positive when anticlockwise.

:::key Rotation about the origin
A rotation through \(\theta\) anticlockwise about \(O\) sends \((1, 0)\) to \((\cos\theta, \sin\theta)\) and \((0, 1)\) to \((-\sin\theta, \cos\theta)\):
\[\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\]
For example, \(90^\circ\) gives \(\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\), \(180^\circ\) gives \(\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}\), and \(-90^\circ\) (a quarter turn clockwise) gives \(\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\).
:::

For the first column, a point one unit along the \(x\)-axis turns to the point at angle \(\theta\) on the unit circle, which is \((\cos\theta, \sin\theta)\). The point \((0, 1)\) starts at \(90^\circ\), so it ends at angle \(\theta + 90^\circ\), which is \((-\sin\theta, \cos\theta)\).

:::key Reflection in the line \(y = x\tan\theta\)
A reflection in the line through \(O\) at angle \(\theta\) to the \(x\)-axis sends \((1, 0)\) to \((\cos 2\theta, \sin 2\theta)\) and \((0, 1)\) to \((\sin 2\theta, -\cos 2\theta)\):
\[\begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}\]
Special cases: \(x\)-axis (\(\theta = 0\)) \(\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\); \(y\)-axis \(\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}\); \(y = x\) \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\); \(y = -x\) \(\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\).
:::

The reason is that a reflection in a mirror at angle \(\theta\) sends a point at angle \(\phi\) to the point at angle \(2\theta - \phi\): the mirror line bisects the angle between a point and its image (both are the same distance from \(O\)), so the point is \(\theta - \phi\) on one side of the mirror and its image is \(\theta - \phi\) on the other, at angle \(\theta + (\theta - \phi) = 2\theta - \phi\). So \((1, 0)\), at \(\phi = 0\), goes to angle \(2\theta\), and \((0, 1)\), at \(\phi = 90^\circ\), goes to angle \(2\theta - 90^\circ\), whose cosine and sine are \(\sin 2\theta\) and \(-\cos 2\theta\). This uses the shift of \(90^\circ\) between the graphs of sine and cosine: \(\cos(\alpha - 90^\circ) = \sin\alpha\) and \(\sin(\alpha - 90^\circ) = -\cos\alpha\), here with \(\alpha = 2\theta\).

:::key Enlargement, stretch and shear
- **Enlargement**, centre \(O\), scale factor \(k\): \(\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}\). Distances from \(O\) are multiplied by \(k\).
- **Stretch** parallel to the \(x\)-axis, scale factor \(k\): \(\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}\). Every \(x\)-coordinate is multiplied by \(k\) and the \(y\)-coordinates do not change, so the \(y\)-axis is the invariant line. Stretch parallel to the \(y\)-axis: \(\begin{pmatrix} 1 & 0 \\ 0 & k \end{pmatrix}\).
- **Shear** with the \(x\)-axis invariant: \(\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}\), which sends \((0, 1)\) to \((k, 1)\) and keeps \((1, 0)\) fixed. With the \(y\)-axis invariant: \(\begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}\).
:::

:::eg Write down the matrix for (a) a reflection in the line \(y = \sqrt3\,x\), (b) a shear with the \(x\)-axis invariant that sends \((0, 1)\) to \((3, 1)\), and say what \((1, 1)\) goes to under (b).
(a) The line \(y = \sqrt3\,x\) makes an angle \(\theta\) with \(\tan\theta = \sqrt3\), so \(\theta = 60^\circ\) and \(2\theta = 120^\circ\). Here \(\cos 120^\circ = -\tfrac12\) and \(\sin 120^\circ = \tfrac{\sqrt3}{2}\):
\[\begin{pmatrix} -\tfrac12 & \tfrac{\sqrt3}{2} \\ \tfrac{\sqrt3}{2} & \tfrac12 \end{pmatrix}\]
(b) The first column is \((1, 0)\), the second is \((3, 1)\):
\[\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \end{pmatrix}\]
The point \((1, 1)\) goes to \((4, 1)\); its height is unchanged, as in any shear that keeps the \(x\)-axis fixed.
:::

### Naming a transformation from its matrix

To describe a matrix geometrically, look at the images of \((1, 0)\) and \((0, 1)\) and compare with the list above. The question may also ask for "the type of each transformation" and "the order": a matrix that is not on the list is usually a product of two that are.

:::eg (Exam style) The matrix \(\mathbf{M} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}\) represents the combination of two transformations, a rotation and a stretch. State the type of each transformation, with full details, and make clear the order in which they are applied.
The rotation matrix with \(\theta = 90^\circ\) is \(\mathbf{R} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\). Try rotating first, then applying a matrix \(\mathbf{A}\), so that \(\mathbf{M} = \mathbf{AR}\). Multiply on the right by \(\mathbf{R}^{-1}\):
\[\mathbf{A} = \mathbf{M}\mathbf{R}^{-1} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\] [M1]
The matrix \(\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\) is a stretch, parallel to the \(x\)-axis, scale factor 2. [A1]
So \(\mathbf{M}\) is a rotation through \(90^\circ\) anticlockwise about \(O\), followed by a stretch parallel to the \(x\)-axis with scale factor 2. [B1]
**Check** with \((1, 0)\): the rotation sends it to \((0, 1)\) and the stretch leaves \((0, 1)\) alone. The first column of \(\mathbf{M}\) is \((0, 1)\). With \((0, 1)\): the rotation sends it to \((-1, 0)\) and the stretch doubles it to \((-2, 0)\), the second column.
:::

## Combining and undoing transformations

### Composite transformations

Suppose \(\mathbf{B}\) is applied first and then \(\mathbf{A}\). A point \(\mathbf{x}\) goes to \(\mathbf{Bx}\), and then to \(\mathbf{A}(\mathbf{Bx}) = (\mathbf{AB})\mathbf{x}\).

:::key Order of a composite
The matrix \(\mathbf{AB}\) represents "\(\mathbf{B}\) first, then \(\mathbf{A}\)". The matrix nearest the point acts first, so you read the product from right to left. For three transformations, \(\mathbf{ABC}\) means \(\mathbf{C}\), then \(\mathbf{B}\), then \(\mathbf{A}\).
:::

:::eg Find the single matrix for a reflection in the line \(y = x\) followed by a rotation through \(90^\circ\) anticlockwise about \(O\). Then find the matrix for the same two transformations in the opposite order, and describe both.
Let \(\mathbf{B} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\) (reflection) and \(\mathbf{A} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\) (rotation).

Reflection first, then rotation: the rotation matrix is on the left.
\[\mathbf{AB} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}\]
This is a reflection in the \(y\)-axis. **Check** with \((1, 0)\): the reflection in \(y = x\) gives \((0, 1)\), and the rotation sends that to \((-1, 0)\).

Rotation first, then reflection:
\[\mathbf{BA} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\]
This is a reflection in the \(x\)-axis. The two orders give different transformations, just as \(\mathbf{AB} \ne \mathbf{BA}\).
:::

:::warn Which way round?
"A followed by B" is the matrix \(\mathbf{BA}\), with the second transformation on the **left**. Writing the matrices in the order you read the words is the commonest way to lose the marks in this topic. Test your product with the point \((1, 0)\): apply the transformations to it one at a time and compare with the first column.
:::

### Inverse transformations

If \(\mathbf{M}\) is non-singular, the transformation that undoes it is represented by \(\mathbf{M}^{-1}\), because \(\mathbf{M}^{-1}(\mathbf{Mx}) = \mathbf{x}\).

:::key Inverse transformations
- The inverse of a rotation through \(\theta\) is a rotation through \(-\theta\).
- The inverse of an enlargement with scale factor \(k\) is an enlargement with scale factor \(\tfrac1k\); the inverse of a stretch or shear reverses it: \(\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & -k \\ 0 & 1 \end{pmatrix}\).
- A reflection is its own inverse: reflecting twice returns every point.
- \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\): to undo "\(\mathbf{B}\) then \(\mathbf{A}\)", undo \(\mathbf{A}\) first and then undo \(\mathbf{B}\), as in [Matrices: algebra, determinants and inverses](#math.fm.matrices).
:::

## Determinant and area

:::key Area scale factor
Under the transformation with matrix \(\mathbf{M}\), areas are multiplied by \(|\det\mathbf{M}|\). If \(\det\mathbf{M} < 0\), the transformation also reverses orientation (anticlockwise becomes clockwise, as in a reflection). If \(\det\mathbf{M} = 0\), the whole plane is flattened onto a line (or a point) and areas become 0.
\[\text{area of image} = |\det\mathbf{M}| \times \text{area of object}\]
:::

:::proof Why the determinant is the area scale factor
The unit square has area 1 and corners \(O\), \((1, 0)\), \((1, 1)\) and \((0, 1)\). Under \(\begin{pmatrix} a & b \\ c & d \end{pmatrix}\), these go to \(O\), \((a, c)\), \((a + b, c + d)\) and \((b, d)\): a parallelogram with sides along the vectors \((a, c)\) and \((b, d)\). The area of a parallelogram with sides \(\begin{pmatrix} a \\ c \end{pmatrix}\) and \(\begin{pmatrix} b \\ d \end{pmatrix}\) is \(|ad - bc|\). To see this, take \(a, b, c, d > 0\) with \(ad > bc\) and draw the rectangle from \(O\) to \((a + b, c + d)\) round the parallelogram, whose area is \((a + b)(c + d) = ac + ad + bc + bd\). The corners left over are two triangles of area \(\tfrac12 ac\), two triangles of area \(\tfrac12 bd\) and two rectangles of area \(bc\), a total of \(ac + bd + 2bc\). Subtracting leaves \(ad - bc\). (For other signs the same working gives \(\pm(ad - bc)\), and area is never negative.) The diagonal from \(O\) to \((a + b, c + d)\) cuts the parallelogram into two equal triangles, so the triangle with vertices \(O\), \((a, c)\) and \((b, d)\) has area \(\tfrac12|ad - bc|\); this formula for a triangle with one vertex at \(O\) is used below. So the unit square's area becomes \(|\det\mathbf{M}|\). Every shape is made of tiny squares, and a linear map scales each one by the same factor, so every area is multiplied by \(|\det\mathbf{M}|\).
:::

The determinant of a composite is the product of the determinants, \(\det(\mathbf{AB}) = \det\mathbf{A}\det\mathbf{B}\), which fits: the scale factors multiply. Rotations and shears have determinant 1 (areas are preserved), reflections have \(-1\), an enlargement with scale factor \(k\) has \(k^2\), and a stretch with scale factor \(k\) has \(k\).

:::eg The triangle with vertices \((1, 1)\), \((4, 1)\) and \((1, 3)\) is transformed by \(\mathbf{M} = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}\). Find the area of the image.
The triangle has base 3 and height 2, so its area is \(\tfrac12 \times 3 \times 2 = 3\).
\[\det\mathbf{M} = 8 - 3 = 5\]
The area of the image is \(5 \times 3 = 15\).

**Check** by finding the image vertices: \(\mathbf{M}(1, 1) = (3, 7)\), \(\mathbf{M}(4, 1) = (9, 16)\), \(\mathbf{M}(1, 3) = (5, 15)\). Take the image vertex \((3, 7)\) as the origin of a triangle: the other two vertices are at \((6, 9)\) and \((2, 8)\) from it, and the triangle formula \(\tfrac12|ad - bc|\) from the proof above gives \(\tfrac12\left|6 \times 8 - 2 \times 9\right| = \tfrac12 \times 30 = 15\).
:::

A singular matrix does not preserve the shape of the plane at all. For \(\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\), every point \((x, y)\) goes to \((x + 2y, 2x + 4y)\), which is \((x + 2y)(1, 2)\): the whole plane collapses onto the line \(y = 2x\), and no inverse exists.

:::eg A designer enlarges a logo of area \(18\,\mathrm{cm^2}\) with these steps. First, a stretch with scale factor 3 parallel to the \(x\)-axis. Second, a reflection in the \(x\)-axis (to make a mirror image). Third, a shear \(\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\). Find the single matrix for the whole process, and the area of the final logo.
The matrices in order are \(\mathbf{S} = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}\), \(\mathbf{R} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\) and \(\mathbf{H} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\). Stretch first, so the stretch is on the right: the total is \(\mathbf{HRS}\). Do the right-hand pair first:
\[\mathbf{RS} = \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} \qquad \mathbf{HRS} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 3 & -2 \\ 0 & -1 \end{pmatrix}\]
The determinant is \(3 \times (-1) - 0 = -3\), which is \(3 \times (-1) \times 1\) as expected. The area scale factor is 3, so the final area is \(3 \times 18 = 54\,\mathrm{cm^2}\). The negative sign says the logo is a mirror image of the original.
:::

## Invariant points and invariant lines

Some points and lines are not moved, or not moved off themselves. You need to tell these two ideas apart.

:::def Invariant point
A point \(P\) is **invariant** (unchanged) under a transformation if its image is \(P\) itself. For a matrix \(\mathbf{M}\), \(\mathbf{Mx} = \mathbf{x}\). The origin is always invariant. If every point of a line is invariant, the line is a **line of invariant points**.
:::

:::def Invariant line
A line is **invariant** if the image of every point on it lies on the same line. The points may move along the line (for example, an enlargement moves them away from \(O\)); a line of invariant points is an invariant line whose points do not move at all.
:::

### Invariant points

Rewrite \(\mathbf{Mx} = \mathbf{x}\) as \((\mathbf{M} - \mathbf{I})\mathbf{x} = \mathbf{0}\) and solve the two equations. If the two equations are the same, you have a whole line of invariant points; if \(\mathbf{M} - \mathbf{I}\) is non-singular, the origin is the only one.

:::eg Find the invariant points of the transformation with matrix \(\mathbf{M} = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}\).
Put \(\mathbf{M}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}\):
\[\begin{aligned}
3x - 2y &= x \\
x &= y
\end{aligned}\]
The first equation gives \(2x - 2y = 0\), which is also \(x = y\). The two equations are the same, so every point on the line \(y = x\) is invariant. The transformation has a line of invariant points, \(y = x\).
:::

A rotation through an angle that is not a multiple of \(360^\circ\) has only the origin invariant (even a half turn moves every point except \(O\)). A shear \(\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}\) has the whole \(x\)-axis invariant, and a reflection has its mirror line invariant.

### Invariant lines through the origin

Take a line through the origin, \(y = mx\), and a general point on it, \((x, mx)\). Its image under \(\begin{pmatrix} a & b \\ c & d \end{pmatrix}\) is
\[\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} x \\ mx \end{pmatrix} = \begin{pmatrix} (a + bm)x \\ (c + dm)x \end{pmatrix}\]
This lies on \(y = mx\) when the \(y\)-coordinate is \(m\) times the \(x\)-coordinate: \(c + dm = m(a + bm)\).

:::key Invariant lines through \(O\)
The line \(y = mx\) is invariant under \(\begin{pmatrix} a & b \\ c & d \end{pmatrix}\) exactly when
\[bm^2 + (a - d)m - c = 0\]
The \(y\)-axis (\(x = 0\)) is invariant exactly when \(b = 0\), since \((0, y)\) goes to \((by, dy)\), and that is on the \(y\)-axis only if \(b = 0\). The quadratic can have two, one or no real roots.
:::

:::eg (Exam style) Find the equations of the invariant lines through the origin of the transformation with matrix \(\mathbf{M} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\). State which of them is a line of invariant points.
A general point on \(y = mx\) is \((x, mx)\), with image
\[\begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} x \\ mx \end{pmatrix} = \begin{pmatrix} (3 + m)x \\ (2 + 2m)x \end{pmatrix}\] [M1]
This lies on the same line when \(2 + 2m = m(3 + m)\): [M1]
\[\begin{aligned}
m^2 + m - 2 &= 0 \\
(m + 2)(m - 1) &= 0
\end{aligned}\] [A1]
So \(m = 1\) or \(m = -2\): the invariant lines are \(y = x\) and \(y = -2x\). [A1]
The \(y\)-axis is not invariant, since \(b = 1 \ne 0\).
For \(y = -2x\), the image of \((x, -2x)\) is \((x, -2x)\) itself, so it is a line of invariant points. For \(y = x\), \((x, x)\) goes to \((4x, 4x)\): the points slide along the line, so it is invariant but not a line of invariant points. [B1]
:::

Use the tool below with the matrix \(\begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\) already set. It draws the invariant lines through the origin as dashed lines. Change the entries and watch the lines appear, merge and vanish: for a shear there is only one; for a rotation there are none; for a reflection there are two, and one of them is the mirror.

:::html
<div class="widget" data-w="fm-matrix" data-m="3,1,2,2" data-shape="triangle" data-show="grid,det,invariant" data-presets="rotation,reflection,shear,stretch,enlargement"></div>
:::

### Invariant lines that do not pass through the origin

For a line \(y = mx + c\) with \(c \ne 0\), take the point \((x, mx + c)\), find its image \((x', y')\), and compare \(y'\) with \(mx' + c\). The line is invariant if they are equal for every \(x\).

:::eg The matrix \(\mathbf{M} = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}\) has invariant lines through \(O\) given by \(-2m^2 + 3m - 1 = 0\), that is \(m = 1\) and \(m = \tfrac12\). Decide whether the lines \(y = x + c\) and \(y = \tfrac12 x + c\) are invariant for \(c \ne 0\).
The point \((x, x + c)\) on the first line has image
\[\begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} x \\ x + c \end{pmatrix} = \begin{pmatrix} x - 2c \\ x \end{pmatrix}\]
For this to be on the same line we need \(x = (x - 2c) + c\), that is \(c = 0\). So \(y = x + c\) maps to \(y = x + 2c\), a different line: not invariant for \(c \ne 0\).

The point \((x, \tfrac12 x + c)\) on the second line has image
\[\begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} x \\ \tfrac12 x + c \end{pmatrix} = \begin{pmatrix} 2x - 2c \\ x \end{pmatrix}\]
Check: \(\tfrac12(2x - 2c) + c = x\), which is the \(y\)-coordinate. So the image lies on the same line, and every line \(y = \tfrac12 x + c\) is invariant.
:::

The exam wording "show that every line of gradient 1 is invariant" is this idea with a given matrix: take \((x, x + c)\), find the image, and show the image lies on \(y = x + c\) for every \(x\) and \(c\).

:::eg (Exam style) Show that every line of gradient 1 is invariant under the transformation with matrix \(\mathbf{M} = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix}\).
A line of gradient 1 is \(y = x + c\). A general point on it is \((x, x + c)\). [B1]
\[\begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} x \\ x + c \end{pmatrix} = \begin{pmatrix} 2x - x - c \\ x \end{pmatrix} = \begin{pmatrix} x - c \\ x \end{pmatrix}\] [M1]
Call the image \((x', y')\). Then \(x' = x - c\) and \(y' = x\), so \(y' = x' + c\). [A1]
The image lies on \(y = x + c\), so every line of gradient 1 is invariant. [A1]
:::

:::warn Line of invariant points or invariant line?
An **invariant line** is mapped onto itself, with the points free to move along it. A **line of invariant points** has every point fixed. A shear keeps the \(x\)-axis fixed point by point, and also maps every line \(y = c\) to itself (sliding the points along). Questions use the two terms precisely, so answer the one asked.
:::

:::board
Edexcel Further Mathematics (9FM0, Core Pure) also teaches 2×2 matrices as transformations, with the area scale factor and invariant points and lines. In 9231 the matrices in this chapter are 2×2 only, and eigenvalues and eigenvectors come later, in Paper 2.
:::

:::exam What the paper gives you
MF19 does not list any transformation matrices, so you must learn the rotation and reflection matrices or derive them in a few seconds from the columns \((\cos\theta, \sin\theta)\) and \((-\sin\theta, \cos\theta)\). Rotation angles are anticlockwise unless the question says otherwise, and a description of a transformation needs its type and its details: centre and angle for a rotation, the mirror line for a reflection, the scale factor and centre for an enlargement, the invariant line and the direction for a stretch or shear. When a matrix is described as "two transformations", the order matters and must be stated.
:::

:::eg Spot the error: the matrix \(\mathbf{A}\) represents a reflection in the \(x\)-axis and \(\mathbf{B}\) a rotation through \(90^\circ\) anticlockwise about \(O\). (a) Find the matrix for reflection in the \(x\)-axis followed by the rotation. (b) Find the image of \((2, 1)\) under the combined transformation. (6 marks)
A student wrote this answer.

Line 1: \(\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\), \(\mathbf{B} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\)
Line 2: reflection followed by rotation is \(\mathbf{AB} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\)
Line 3: \(\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ -2 \end{pmatrix}\)

Line 1 gives both matrices correctly. [B1] [B1]

**Line 2 multiplies in the wrong order, so it earns no marks.** [M0] [A0] "Reflection then rotation" means the rotation acts last, so it goes on the left: the matrix is \(\mathbf{BA}\), not \(\mathbf{AB}\). The student's matrix is a reflection in \(y = -x\).

Line 3 multiplies the matrix by the point correctly, using the student's matrix, so the method mark is earned and the accuracy mark follows through. [M1] [A1] (FT) The student scores 4 out of 6.

Correct working: \(\mathbf{BA} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\), and the image of \((2, 1)\) is \((1, 2)\). **Check** step by step: the reflection in the \(x\)-axis sends \((2, 1)\) to \((2, -1)\), and the rotation sends \((x, y)\) to \((-y, x)\), giving \((1, 2)\).
:::

:::try Start easy, finish at exam standard
Q: Write down the matrix of the transformation that sends \((1, 0)\) to \((2, -1)\) and \((0, 1)\) to \((4, 3)\), and find the image of \((1, 1)\).
A: The matrix is \(\begin{pmatrix} 2 & 4 \\ -1 & 3 \end{pmatrix}\). The image of \((1, 1)\) is the sum of the columns: \((6, 2)\).
Q: Write down the matrix for a rotation through \(90^\circ\) clockwise about \(O\), and use it to find the image of \((3, 2)\).
A: The matrix is \(\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\). The image of \((3, 2)\) is \((2, -3)\).
Q: State the transformation represented by (a) \(\begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix}\), (b) \(\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}\), (c) \(\begin{pmatrix} 1 & 0 \\ 4 & 1 \end{pmatrix}\).
A: (a) A stretch parallel to the \(y\)-axis with scale factor 5. (b) A rotation through \(180^\circ\) about \(O\) (also an enlargement with scale factor \(-1\)). (c) A shear with the \(y\)-axis invariant, sending \((1, 0)\) to \((1, 4)\).
Q: Find the single matrix for a reflection in the line \(y = x\) followed by a reflection in the \(x\)-axis, and describe the combined transformation.
A: Reflection in \(y = x\) first, \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\), then reflection in the \(x\)-axis \(\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\). The product is \(\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\), a rotation through \(90^\circ\) clockwise about \(O\).
Q: Find the area of the image of a shape of area 6 under \(\begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix}\).
A: \(\det = 8 - 3 = 5\), so the area is \(5 \times 6 = 30\).
Q: Write down the inverse of the transformation with matrix \(\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\), and describe it.
A: The inverse matrix is \(\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}\), a shear with the \(x\)-axis invariant sending \((0, 1)\) to \((-2, 1)\): it undoes the original shear.
Q: Show that \(\begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}\) is singular and describe what it does to the plane.
A: \(\det = 4 - 4 = 0\). Every point \((x, y)\) goes to \((4x + 2y, 2x + y) = (2x + y)(2, 1)\), so the whole plane is sent onto the line \(y = \tfrac12 x\).
Q: Find the invariant points of \(\begin{pmatrix} 2 & 1 \\ 2 & 3 \end{pmatrix}\).
A: \(2x + y = x\) gives \(x + y = 0\), and \(2x + 3y = y\) gives \(2x + 2y = 0\), the same line. So \(y = -x\) is a line of invariant points.
Q: Find the equations of the invariant lines through the origin of \(\begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}\).
A: \(bm^2 + (a - d)m - c = 2m^2 - m - 3 = 0\), so \((2m - 3)(m + 1) = 0\) and the lines are \(y = \tfrac32 x\) and \(y = -x\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ (a) Write down the matrix \(\mathbf{R}\) for a rotation through \(60^\circ\) anticlockwise about \(O\), in exact form. (b) Find the image of \((4, 0)\) under \(\mathbf{R}\).
A: (a) \(\mathbf{R} = \begin{pmatrix} \cos 60^\circ & -\sin 60^\circ \\ \sin 60^\circ & \cos 60^\circ \end{pmatrix}\) [B1] \(= \begin{pmatrix} \tfrac12 & -\tfrac{\sqrt3}{2} \\ \tfrac{\sqrt3}{2} & \tfrac12 \end{pmatrix}\). [B1]
(b) \(\mathbf{R}\begin{pmatrix} 4 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 2\sqrt3 \end{pmatrix}\) [M1], so the image is \((2, 2\sqrt3)\). [A1]
Q: [3 marks] ★ Describe the transformation represented by (a) \(\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\), (b) \(\begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix}\).
A: (a) A reflection [B1] in the line \(y = -x\). [B1]
(b) A stretch parallel to the \(y\)-axis with scale factor 4 (the \(x\)-axis is invariant). [B1]
Q: [6 marks] ★★ (a) Find the single matrix \(\mathbf{T}\) for a reflection in the line \(y = x\) followed by an enlargement with scale factor 3 about \(O\). (b) A triangle of area 4 is transformed by \(\mathbf{T}\). Find the area of the image.
A: (a) The reflection matrix is \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\) and the enlargement matrix is \(\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}\). [B1] [B1]
The enlargement is applied second, so it is on the left: [M1]
\(\mathbf{T} = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix}\). [A1]
(b) \(\det\mathbf{T} = -9\), so the area scale factor is 9 [M1] and the area is \(36\). [A1]
Q: [4 marks] ★★ Find the invariant points of the transformation with matrix \(\begin{pmatrix} 5 & -2 \\ 4 & -1 \end{pmatrix}\).
A: \(\begin{pmatrix} 5 & -2 \\ 4 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}\) [M1] gives \(5x - 2y = x\) and \(4x - y = y\), [A1] and both reduce to \(y = 2x\). [A1]
So every point on the line \(y = 2x\) is invariant: it is a line of invariant points. [B1]
Q: [5 marks] ★★ Find the equations of the invariant lines through the origin of the transformation with matrix \(\mathbf{M} = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}\).
A: The image of \((x, mx)\) is \(((1 + 2m)x, (3 + 2m)x)\). [M1]
It lies on \(y = mx\) when \(3 + 2m = m(1 + 2m)\), [M1] that is \(2m^2 - m - 3 = 0\). [A1]
\((2m - 3)(m + 1) = 0\), [M1] so the lines are \(y = \tfrac32 x\) and \(y = -x\). [A1]
(The \(y\)-axis is not invariant, because the top-right entry is not 0.)
Q: [6 marks] ★★ The matrix \(\mathbf{N} = \begin{pmatrix} k & 1 \\ 2 & 3 \end{pmatrix}\) transforms a region of area 5 into a region of area 55. Find the possible values of \(k\), and state for which of them the image is a mirror image of the original (orientation reversed).
A: \(\det\mathbf{N} = 3k - 2\). [M1 A1]
The area scale factor is \(|3k - 2| = \dfrac{55}{5} = 11\). [M1]
\(3k - 2 = 11\) gives \(k = \dfrac{13}{3}\). [A1] \(3k - 2 = -11\) gives \(k = -3\). [A1]
Orientation is reversed when \(\det\mathbf{N} < 0\), that is for \(k = -3\). [B1]
Q: [11 marks] (#math.p1.trig) ★★★ (a) Write down the matrices \(\mathbf{R}\) for rotation through \(45^\circ\) anticlockwise about \(O\) and \(\mathbf{S}\) for reflection in the \(x\)-axis. (b) The matrix \(\mathbf{T}\) represents the rotation followed by the reflection. Find \(\mathbf{T}\) in exact form. (c) Show that \(\mathbf{T}\) represents a reflection in a line through \(O\), and find the exact gradient of the line. (d) Find \(\det\mathbf{T}\) and \(\mathbf{T}^{-1}\).
H: Rotation first means \(\mathbf{S}\) is on the left: \(\mathbf{T} = \mathbf{SR}\).
H: Compare \(\mathbf{T}\) with \(\begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}\) to read off \(\cos 2\alpha\) and \(\sin 2\alpha\), then use \(\tan 22.5^\circ = \sqrt2 - 1\).
H: A reflection is its own inverse.
A: (a) \(\mathbf{R} = \dfrac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\) [B1] and \(\mathbf{S} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\). [B1]
(b) \(\mathbf{T} = \mathbf{SR}\) [M1] \(= \dfrac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ -1 & -1 \end{pmatrix}\). [A1]
(c) \(\mathbf{T}\) has the form \(\begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}\) with \(\cos 2\alpha = \dfrac{1}{\sqrt2}\) and \(\sin 2\alpha = -\dfrac{1}{\sqrt2}\), [B1] so \(2\alpha = -45^\circ\). [M1]
The mirror line is at \(\alpha = -22.5^\circ\) to the \(x\)-axis, [A1] with gradient \(\tan(-22.5^\circ) = -(\sqrt2 - 1) = 1 - \sqrt2\). [A1]
(d) \(\det\mathbf{T} = \tfrac12(-1 - 1) = -1\). [B1] The inverse is \(\dfrac{1}{-1}\) times the matrix with the diagonal swapped and the other signs changed, [M1] which is \(\mathbf{T}\) itself: \(\mathbf{T}^{-1} = \mathbf{T}\), as for any reflection. [A1]
Q: [13 marks] (#math.fm.matrices) ★★★ The matrix \(\mathbf{M} = \begin{pmatrix} 1 & 1 \\ -2 & 4 \end{pmatrix}\). (a) Find the equations of the two invariant lines through the origin. (b) The triangle \(T\) has vertices \(O\), \((1, 1)\) and \((1, 2)\). Find the area of \(T\), the vertices of its image \(T'\) under \(\mathbf{M}\), and the area of \(T'\). Verify that the ratio of the areas is \(\det\mathbf{M}\). (c) Find \(\mathbf{M}^{-1}\) and state the area scale factor of the transformation it represents.
H: Use \(bm^2 + (a - d)m - c = 0\) with \(a = 1\), \(b = 1\), \(c = -2\), \(d = 4\).
H: The vertices of \(T\) lie on the two invariant lines you found. Where do they go?
H: The area scale factor of the inverse is the reciprocal.
A: (a) The image of \((x, mx)\) is \(((1 + m)x, (-2 + 4m)x)\). [M1] It lies on \(y = mx\) if \(-2 + 4m = m(1 + m)\), [M1] so \(m^2 - 3m + 2 = 0\) [A1] and \((m - 1)(m - 2) = 0\). [M1] The invariant lines are \(y = x\) and \(y = 2x\). [A1]
(b) The area of \(T\) is \(\tfrac12|1 \times 2 - 1 \times 1| = \tfrac12\). [B1] \(\mathbf{M}(1, 1) = (2, 2)\) and \(\mathbf{M}(1, 2) = (3, 6)\), so \(T'\) has vertices \(O\), \((2, 2)\) and \((3, 6)\). [M1 A1] Its area is \(\tfrac12|2 \times 6 - 2 \times 3| = 3\), [A1] and \(3 \div \tfrac12 = 6 = \det\mathbf{M}\) (\(= 4 + 2\)). [B1]
(c) \(\mathbf{M}^{-1} = \dfrac16\begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}\) [M1 A1] and its area scale factor is \(\dfrac16\). [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The matrix \(\mathbf{M} = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}\), where \(\sin\theta \ne 0\). Find the invariant points of \(\mathbf{M}\), and use double-angle formulae to show that they form the line \(y = x\tan\tfrac{\theta}{2}\).
H: Write \(\mathbf{M}\mathbf{x} = \mathbf{x}\) as two equations and solve for \(y\) in terms of \(x\).
H: Use \(1 - \cos\theta = 2\sin^2\tfrac{\theta}{2}\) and \(\sin\theta = 2\sin\tfrac{\theta}{2}\cos\tfrac{\theta}{2}\).
A: The first row gives \(x\cos\theta + y\sin\theta = x\), so \((\cos\theta - 1)x + y\sin\theta = 0\). [M1 A1]
\(y = \dfrac{1 - \cos\theta}{\sin\theta}\,x\). [A1]
With the identities, \(\dfrac{1 - \cos\theta}{\sin\theta} = \dfrac{2\sin^2\frac{\theta}{2}}{2\sin\frac{\theta}{2}\cos\frac{\theta}{2}} = \tan\dfrac{\theta}{2}\), [M1] so \(y = x\tan\dfrac{\theta}{2}\). [A1]
The second row, \(x\sin\theta - y\cos\theta = y\), gives \(y = \dfrac{\sin\theta}{1 + \cos\theta}x\), which is the same line (since \(\dfrac{\sin\theta}{1 + \cos\theta} = \tan\dfrac{\theta}{2}\)); so the invariant points are exactly this line. [B1]
Q: [6 marks] ★★★ Reflection in the line \(y = x\tan\alpha\) is followed by reflection in the line \(y = x\tan\beta\). Show that the combined transformation is a rotation about \(O\), and find its angle. Give the rotation when the mirrors are the \(x\)-axis and the line \(y = x\tan 30^\circ\).
H: The second reflection is on the left of the product.
H: Use \(\cos(A - B) = \cos A\cos B + \sin A\sin B\) and \(\sin(A - B) = \sin A\cos B - \cos A\sin B\).
A: The product is
\[\begin{pmatrix} \cos 2\beta & \sin 2\beta \\ \sin 2\beta & -\cos 2\beta \end{pmatrix}\begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}\] [M1]
Its entries are
\[\begin{pmatrix} \cos 2\beta\cos 2\alpha + \sin 2\beta\sin 2\alpha & \cos 2\beta\sin 2\alpha - \sin 2\beta\cos 2\alpha \\ \sin 2\beta\cos 2\alpha - \cos 2\beta\sin 2\alpha & \sin 2\beta\sin 2\alpha + \cos 2\beta\cos 2\alpha \end{pmatrix}\] [A1]
By the compound angle formulae this is
\[\begin{pmatrix} \cos(2\beta - 2\alpha) & -\sin(2\beta - 2\alpha) \\ \sin(2\beta - 2\alpha) & \cos(2\beta - 2\alpha) \end{pmatrix}\] [M1 A1]
a rotation through \(2(\beta - \alpha)\) anticlockwise about \(O\). [A1]
With \(\alpha = 0\) and \(\beta = 30^\circ\), the rotation is through \(60^\circ\) anticlockwise. [B1]
:::

:::quiz
? The matrix \(\begin{pmatrix} 2 & 5 \\ 3 & 1 \end{pmatrix}\) represents a transformation. Where does it send the point \((1, 0)\)?
+ \((2, 3)\)
- \((2, 5)\)
- \((5, 1)\)
- \((3, 1)\)
> The image of \((1, 0)\) is the first column, \((2, 3)\). The first row, \((2, 5)\), is a common slip, and \((0, 1)\) would go to the second column, \((5, 1)\).
? The matrix \(\mathbf{AB}\) represents which order of transformations?
- \(\mathbf{A}\) first, then \(\mathbf{B}\)
+ \(\mathbf{B}\) first, then \(\mathbf{A}\)
- Both at once, so the order does not matter
- \(\mathbf{A}\) and \(\mathbf{B}\) in either order, as long as both are rotations
> \(\mathbf{AB}\mathbf{x} = \mathbf{A}(\mathbf{Bx})\): \(\mathbf{B}\) acts on the point first. Rotations about the same centre happen to commute, but reflections generally do not, so the order is part of the answer.
? A transformation has matrix \(\mathbf{M}\) with \(\det\mathbf{M} = -4\). What happens to a region of area 3?
+ It becomes a mirror-image region of area 12
- It becomes a region of area \(-12\)
- It becomes a mirror-image region of area 4
- It becomes a region of area \(\tfrac34\)
> The area scale factor is \(|\det\mathbf{M}| = 4\), so the area is 12; the negative sign says that orientation is reversed. Areas are never negative.
? What is the matrix for a reflection in the line \(y = x\)?
- \(\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\)
+ \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\)
- \(\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\)
- \(\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\)
> \((1, 0)\) goes to \((0, 1)\) and \((0, 1)\) goes to \((1, 0)\), so the columns are \((0, 1)\) and \((1, 0)\). The first option is the reflection in the \(x\)-axis and the third is a quarter turn; the last is singular, so it flattens the plane.
? A shear fixes the \(x\)-axis point by point and sends \((0, 1)\) to \((3, 1)\). Which is true?
+ Every line \(y = c\) is an invariant line, and the \(x\)-axis is a line of invariant points
- Every line \(y = c\) is a line of invariant points
- Only the \(x\)-axis is invariant
- No lines are invariant
> The matrix is \(\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}\), and \((x, c)\) goes to \((x + 3c, c)\): the point slides along \(y = c\), so each line is invariant but only \(c = 0\) has every point fixed.
? The matrix \(\mathbf{M}\) represents "\(\mathbf{P}\) then \(\mathbf{Q}\)". Which transformation undoes it?
+ \(\mathbf{Q}^{-1}\) first, then \(\mathbf{P}^{-1}\)
- \(\mathbf{P}^{-1}\) first, then \(\mathbf{Q}^{-1}\)
- \(\mathbf{P}\) first, then \(\mathbf{Q}\) again
- \(\mathbf{M}^{T}\)
> \(\mathbf{M} = \mathbf{QP}\), so \(\mathbf{M}^{-1} = \mathbf{P}^{-1}\mathbf{Q}^{-1}\): undo the last step first.
:::

:::checklist What you can now do
- [ ] I can find the matrix of a transformation from the images of \((1, 0)\) and \((0, 1)\).
- [ ] I can write down the matrices for rotations, reflections in lines through \(O\), enlargements, stretches and shears.
- [ ] I can describe a transformation from its matrix, and split a matrix into two named transformations in a stated order.
- [ ] I can find the matrix of a combination of transformations, remembering that \(\mathbf{AB}\) means \(\mathbf{B}\) first.
- [ ] I can find and describe the inverse of a transformation.
- [ ] I can use \(|\det\mathbf{M}|\) as the area scale factor and say when orientation is reversed.
- [ ] I can find the invariant points of a matrix and tell a line of invariant points from an invariant line.
- [ ] I can find the invariant lines through the origin, and show that every line of a given gradient is invariant.
:::

:::recap
- The columns of \(\mathbf{M}\) are the images of \((1, 0)\) and \((0, 1)\).
- Rotation \(\theta\) anticlockwise: \(\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\). Reflection in \(y = x\tan\theta\): \(\begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}\). Enlargement \(\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}\); stretch \(\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}\) or \(\begin{pmatrix} 1 & 0 \\ 0 & k \end{pmatrix}\); shear \(\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}\).
- \(\mathbf{AB}\) means "\(\mathbf{B}\) first, then \(\mathbf{A}\)"; the inverse transformation has matrix \(\mathbf{M}^{-1}\), and \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\).
- Area scale factor \(= |\det\mathbf{M}|\); \(\det < 0\) reverses orientation; \(\det = 0\) flattens the plane onto a line.
- Invariant points: \(\mathbf{Mx} = \mathbf{x}\), that is \((\mathbf{M} - \mathbf{I})\mathbf{x} = \mathbf{0}\). Invariant lines through \(O\): \(y = mx\) with \(bm^2 + (a - d)m - c = 0\); the \(y\)-axis when \(b = 0\).
- A line of invariant points is invariant, but an invariant line need not be a line of invariant points.
:::

:::links
- watch: [Linear transformations](https://www.3blue1brown.com/lessons/linear-transformations) · 3Blue1Brown · the "columns are the images of i and j" idea, animated
- watch: [Invariant points](https://www.examsolutions.net/tutorials/matrices-invariant-points/) · ExamSolutions · finding invariant points step by step
- watch: [The determinant](https://www.3blue1brown.com/lessons/determinant) · 3Blue1Brown · the determinant as an area scale factor
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · free booklets with answers on transformations and invariant lines
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot a shape and its image under a matrix you define
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Proof by induction](#math.fm.induction) shows how to prove a result for every positive integer, including formulae for sums, recurrences, divisibility and powers of a matrix.
