@chapter math.fm.systems
@title Three equations, three planes
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 4–6 hours
@summary Three linear equations in three unknowns are one matrix equation, and each equation is a plane. You will solve the system when the matrix is non-singular, decide what happens when it is singular (a common line, or no common point), tell the arrangements of three planes apart from the equations alone, solve consistent systems with a parameter, and find the values of an unknown that change the picture.

:::why
Three equations in three unknowns turn up whenever three quantities are linked by three measurements: prices, currents in a circuit, amounts of ingredients. Sometimes the equations fix a single answer, sometimes they leave a whole line of answers, and sometimes they contradict each other. A matrix tells you which case you are in before you start, and the picture of three planes tells you what the answer means. The same ideas, with right-hand sides of zero, lead straight to the eigenvalues in the next chapter.
:::

**Before you start**, you need matrix inverses and determinants from [Matrices: algebra, determinants and inverses](#math.fm.matrices), and planes, normals and the vector product from [Vectors: the vector product and planes](#math.fm.vectors). Lines of intersection are met again in [Vectors: intersections, angles and distances](#math.fm.vectors2).

:::try Warm-up
Q: Find the inverse of \(\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}\). (from [Matrices: algebra, determinants and inverses](#math.fm.matrices))
A: The determinant is \(3 \times 2 - 1 \times 5 = 1\), so the inverse is \(\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}\).
Q: Find the Cartesian equation of the plane with normal \(\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}\) through the point \((2, 1, 3)\). (from [Vectors: the vector product and planes](#math.fm.vectors))
A: \(x + 2y - z = d\) with \(d = 2 + 2 - 3 = 1\), so \(x + 2y - z = 1\).
Q: Evaluate the determinant below. (from [Matrices: algebra, determinants and inverses](#math.fm.matrices))
\[\begin{vmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & 0 & 1 \end{vmatrix}\]
A: Expand along the first row:
\[1(1 - 0) - 2(0 - 6) + 0 = 1 + 12 = 13\]
:::

## Equations as a matrix equation

Three equations in the unknowns \(x\), \(y\), \(z\) look like this:
\[\begin{aligned}
a_1x + b_1y + c_1z &= d_1 \\
a_2x + b_2y + c_2z &= d_2 \\
a_3x + b_3y + c_3z &= d_3
\end{aligned}\]
Multiplying a matrix by a column reads along each row, so the three lines say the same as one matrix equation.

:::key A system as \(\mathbf{Ax} = \mathbf{b}\)
\[\begin{pmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix}\]
\(\mathbf{A}\) holds the coefficients (row \(i\) is equation \(i\), column \(j\) is the unknown \(j\)), \(\mathbf{x}\) is the column of unknowns and \(\mathbf{b}\) is the column of right-hand sides. An unknown missing from an equation has coefficient 0.
:::

You must be able to go both ways: from equations to a matrix equation, and back.

:::eg Write \(2x + z = 5\), \(y - 3z = 1\), \(x + y + z = 6\) as a matrix equation. Then write \(\begin{pmatrix} 1 & -2 & 0 \\ 3 & 1 & -1 \\ 0 & 4 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 7 \\ 0 \\ -5 \end{pmatrix}\) as three equations.
In the first system the first equation has no \(y\), the second has no \(x\). Put in the zeros:
\[\begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & -3 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \\ 6 \end{pmatrix}\]
In the second, multiply each row by the column of unknowns:
\[\begin{aligned}
x - 2y &= 7 \\
3x + y - z &= 0 \\
4y + 2z &= -5
\end{aligned}\]
:::

:::eg A bakery sells three items at fixed prices: muffins, scones and loaves. An order of 3 muffins, 2 scones and 1 loaf costs £16; 1 muffin, 4 scones and 2 loaves cost £22; 2 muffins, 1 scone and 3 loaves cost £19. Write this as a matrix equation and find the price of each item.
Let the prices in pounds be \(m\), \(s\) and \(l\).
\[\begin{pmatrix} 3 & 2 & 1 \\ 1 & 4 & 2 \\ 2 & 1 & 3 \end{pmatrix}\begin{pmatrix} m \\ s \\ l \end{pmatrix} = \begin{pmatrix} 16 \\ 22 \\ 19 \end{pmatrix}\]
Solve by elimination. The second equation gives \(m = 22 - 4s - 2l\). Substitute into the other two:
\[\begin{aligned}
3(22 - 4s - 2l) + 2s + l &= 16 \;\Rightarrow\; 10s + 5l = 50 \;\Rightarrow\; 2s + l = 10 \\
2(22 - 4s - 2l) + s + 3l &= 19 \;\Rightarrow\; 7s + l = 25
\end{aligned}\]
Subtract: \(5s = 15\), so \(s = 3\), then \(l = 10 - 6 = 4\) and \(m = 22 - 12 - 8 = 2\).

Muffins cost £2, scones £3 and loaves £4. **Check** in the third equation: \(2(2) + 3 + 3(4) = 19\).
:::

## Each equation is a plane

In [Vectors: the vector product and planes](#math.fm.vectors) you met the plane \(ax + by + cz = d\): its normal is \(\begin{pmatrix} a \\ b \\ c \end{pmatrix}\), which is one row of \(\mathbf{A}\). So a system of three equations is three planes, and a solution is a point lying on all three. The questions "how many solutions?" and "how do three planes meet?" are the same question.

Three planes can meet in only a few ways, and each way has its own algebra. This chapter sorts them out. First the good case, where the rows of \(\mathbf{A}\) are completely independent.

## A unique solution: the matrix is non-singular

If \(\det \mathbf{A} \ne 0\), then \(\mathbf{A}^{-1}\) exists, and multiplying \(\mathbf{Ax} = \mathbf{b}\) on the left by it gives the answer in one step.

:::key Non-singular case
If \(\det \mathbf{A} \ne 0\), the system \(\mathbf{Ax} = \mathbf{b}\) has exactly one solution, \(\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}\), for every \(\mathbf{b}\). Geometrically, the three planes meet at a single point.
:::

There is a geometric reason. The determinant of the matrix whose rows are the three normals equals the scalar triple product \(\mathbf{n}_1 \cdot (\mathbf{n}_2 \times \mathbf{n}_3)\). Its size is the volume of the slanted box (a parallelepiped) with the three normals as edges, and it is zero exactly when the box is flat, that is, when the three normals lie in one plane. If the determinant is non-zero, the normals do not lie in one plane, so no direction is parallel to all three planes, and the planes must cross at one point.

:::eg (Exam style) The matrix \(\mathbf{M} = \begin{pmatrix} 2 & 1 & 3 \\ -1 & -1 & 0 \\ -1 & -2 & -1 \end{pmatrix}\). (a) Find \(\det \mathbf{M}\). (b) Find \(\mathbf{M}^{-1}\). (c) Hence solve \(2x + y + 3z = 9\), \(-x - y = 1\), \(-x - 2y - z = 0\), and describe the three planes geometrically.
**(a)** Expand along the first row:
\[\det \mathbf{M} = 2(1 - 0) - 1(1 - 0) + 3(2 - 1)\] [M1]
\[= 2 - 1 + 3 = 4\] [A1]
**(b)** The matrix of cofactors, each minor with its sign, is
\[\begin{pmatrix} 1 & -1 & 1 \\ -5 & 1 & 3 \\ 3 & -3 & -1 \end{pmatrix}\] [M1]
Transpose it, then divide by the determinant:
\[\mathbf{M}^{-1} = \frac14\begin{pmatrix} 1 & -5 & 3 \\ -1 & 1 & -3 \\ 1 & 3 & -1 \end{pmatrix}\] [A1] [A1]
**(c)** The system is \(\mathbf{Mx} = \begin{pmatrix} 9 \\ 1 \\ 0 \end{pmatrix}\), so
\[\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \frac14\begin{pmatrix} 1 & -5 & 3 \\ -1 & 1 & -3 \\ 1 & 3 & -1 \end{pmatrix}\begin{pmatrix} 9 \\ 1 \\ 0 \end{pmatrix}\] [M1]
\[= \frac14\begin{pmatrix} 4 \\ -8 \\ 12 \end{pmatrix} = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}\] [A1]
So \(x = 1\), \(y = -2\), \(z = 3\). The determinant is not zero, so the three planes meet at the single point \((1, -2, 3)\).

**Check** in the second equation: \(-1 - (-2) = 1\). In the third: \(-1 + 4 - 3 = 0\).
:::

Try the three planes of that example below. The widget shows the point where they meet and reports it as "meet at a single point". Drag the picture to turn it, then change one coefficient and watch the verdict.

:::html
<div class="widget" data-w="fm-planes" data-planes="2,1,3,9; -1,-1,0,1; -1,-2,-1,0"></div>
:::

## A singular matrix: no unique solution

If \(\det \mathbf{A} = 0\), the matrix has no inverse and \(\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}\) fails. The system cannot have exactly one solution, but there are two quite different possibilities, and the determinant alone cannot tell you which.

:::def Consistent and inconsistent
A system of equations is **consistent** if it has at least one solution, and **inconsistent** if it has none.
:::

:::def Singular matrix
A square matrix with determinant 0. It has no inverse. The equations \(\mathbf{Ax} = \mathbf{b}\) with \(\mathbf{A}\) singular have either no solution or infinitely many.
:::

Look at the equations
\[\begin{aligned}
x + 2y - z &= 4 \\
2x - y + 3z &= 3 \\
3x + y + 2z &= c
\end{aligned}\]
Add the first two equations, term by term: \(3x + y + 2z = 7\). The left-hand side of the third equation is exactly the sum of the other two. So if the third equation is to be true as well, its right-hand side must be \(4 + 3 = 7\). With \(c = 7\) the third equation says nothing new and the three planes share a line. With any other \(c\) the third equation contradicts the first two, and there is no solution. The matrix is the same in both cases, so the determinant cannot distinguish them.

:::key Singular matrix: look for the row relation
If \(\det \mathbf{A} = 0\) and no two rows are multiples of each other, one row is a combination of the other two, say \(\text{row 3} = p \times \text{row 1} + q \times \text{row 2}\). Find \(p\) and \(q\) by matching two columns, then test the third.
- If \(d_3 = p\,d_1 + q\,d_2\), the third equation follows from the first two: the system is **consistent**, with infinitely many solutions.
- If \(d_3 \ne p\,d_1 + q\,d_2\), the equations contradict each other (elimination gives \(0 = k\) with \(k \ne 0\)): the system is **inconsistent**.
:::

:::eg (Exam style) (a) Show that the system \(x + 2y - z = 4\), \(2x - y + 3z = 3\), \(3x + y + 2z = 7\) is consistent. (b) Find a vector equation of the line of solutions. (c) The 7 in the third equation is changed to 8. Describe the arrangement of the three planes.
**(a)** The sum of the first two equations is \(3x + y + 2z = 4 + 3\). [M1]
The left side is the left side of the third equation and \(4 + 3 = 7\), so the third equation follows from the first two. The system is consistent. [A1]
**(b)** Eliminate \(x\) between the first two equations. From the first, \(x = 4 - 2y + z\). Substitute into the second:
\[\begin{aligned}
2(4 - 2y + z) - y + 3z &= 3 \\
8 - 5y + 5z &= 3 \\
y &= z + 1
\end{aligned}\] [M1]
Let \(z = \lambda\). Then \(y = 1 + \lambda\) and \(x = 4 - 2(1 + \lambda) + \lambda = 2 - \lambda\). [A1]
\[\mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}\] [A1]
**(c)** Now \(3x + y + 2z\) would have to equal both 7 and 8, so the system is inconsistent. [M1]
No two normals are parallel, since \(\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}\), \(\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}\), \(\begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}\) are not multiples of each other, so each pair of planes meets in a line and the three lines never meet: a triangular prism. [A1]

**Check** the direction of the line with the vector product of the first two normals: \(\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \times \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 \\ -5 \\ -5 \end{pmatrix}\), which is \(-5\) times the direction found.
:::

### The arrangements of three planes

When \(\det \mathbf{A} = 0\), the three normals lie in one plane, so there is a direction at right angles to all three normals, and that direction is parallel to all three planes. Look along it and each plane is edge-on, so it shows up as a line. The figure below shows the four cases drawn that way with \(\det \mathbf{A} = 0\) and no two planes coinciding. The table after it lists all seven arrangements: the "corner of a room", a single common point (the case \(\det \mathbf{A} \ne 0\), in the widget above), the four in the figure, and the two where planes coincide.

:::def Sheaf
Three planes that share exactly one common line, like the pages of a book meeting at its spine. The system is consistent with a one-parameter family of solutions.
:::

:::def Triangular prism
Three planes, no two parallel, that meet pairwise in three parallel lines and have no common point. Seen end-on they form a triangle. The system is inconsistent.
:::

:::html
<figure class="fig small"><svg viewBox="30 0 300 520" role="img" aria-label="Four stacked panels, each showing three planes seen end-on as three lines labelled P1, P2 and P3. First, a sheaf: three lines cross at one point, a dot, which is the common line seen end-on. Second, a triangular prism: the three lines form a small triangle and have no common point. Third, two parallel planes and a third: P1 and P2 are two parallel horizontal lines and P3 is a steep line crossing both. Fourth, three parallel planes: three parallel sloping lines that never meet."><path class="c1 sw2" d="M58.0 87.0L282.0 27.0"/><path class="c2 sw2" d="M162.0 87.0L178.0 27.0"/><path class="c3 sw2" d="M140.0 27.0L200.0 87.0"/><circle class="fi" cx="170.0" cy="57.0" r="3.5"/><text class="tl tb" x="292" y="29">P₁</text><text class="tl tb" x="183" y="22">P₂</text><text class="tl tb" x="208" y="99">P₃</text><text class="tl" x="170" y="127" text-anchor="middle">Sheaf: a common line</text><path class="c1 sw2" d="M142.9 215.0L177.5 155.0"/><path class="c2 sw2" d="M50.0 193.5L290.0 193.5"/><path class="c3 sw2" d="M162.5 155.0L197.1 215.0"/><text class="tl tb" x="184" y="151">P₁</text><text class="tl tb" x="300" y="198">P₂</text><text class="tl tb" x="204" y="229">P₃</text><text class="tl" x="170" y="255" text-anchor="middle">Triangular prism: no common point</text><path class="c1 sw2" d="M50.0 298.0L290.0 298.0"/><path class="c2 sw2" d="M50.0 328.0L290.0 328.0"/><path class="c3 sw2" d="M159.1 343.0L180.9 283.0"/><text class="tl tb" x="300" y="303">P₁</text><text class="tl tb" x="300" y="333">P₂</text><text class="tl tb" x="186" y="279">P₃</text><text class="tl" x="170" y="383" text-anchor="middle">Two parallel planes and a third</text><path class="c1 sw2" d="M50.0 444.0L205.3 411.0"/><path class="c2 sw2" d="M50.0 466.5L290.0 415.5"/><path class="c3 sw2" d="M134.7 471.0L290.0 438.0"/><text class="tl tb" x="215" y="414">P₁</text><text class="tl tb" x="300" y="418">P₂</text><text class="tl tb" x="300" y="441">P₃</text><text class="tl" x="170" y="511" text-anchor="middle">Three parallel planes</text></svg><figcaption>Three planes seen end-on, looking along the direction in which they are all parallel to a line: each plane is a line. The dot in the sheaf is the common line of the three planes. In the prism the three pairs of planes meet in three parallel lines, forming the triangle.</figcaption></figure>
:::

:::key The cases for three planes
| Picture | How to recognise it | Solutions |
|---|---|---|
| Three planes meet at a point | determinant not zero | one point |
| Sheaf | determinant zero, no two normals parallel, row relation also holds for the right-hand sides | a line |
| Triangular prism | determinant zero, no two normals parallel, row relation fails for the right-hand sides (\(0 = k\)) | none |
| Two parallel planes, a third crossing them | exactly two normals parallel, right-hand sides not in the same ratio | none |
| Three parallel planes | all three normals parallel, right-hand sides not all in one ratio | none |
| Two planes coincide, a third crossing | two equations are multiples of each other, right-hand sides included | a line |
| All three coincide | all three equations are multiples of one equation | a plane |
:::

Only the sheaf and the "coinciding" rows give solutions when \(\det \mathbf{A} = 0\). Everything else gives none.

:::warn Singular does not mean no solution
\(\det \mathbf{A} = 0\) means only "not exactly one solution". Always test for consistency. The two commonest lost marks in this topic are writing "no solution" because the determinant is zero, and describing a system with a common line as a triangular prism. A sheaf has solutions; a prism has none.
:::

### When two rows are multiples

If two of the equations have proportional left-hand sides, the two planes are parallel or identical, and you read the answer from the right-hand sides.

:::eg (Exam style) The planes \(\Pi_1\), \(\Pi_2\), \(\Pi_3\) have equations \(x + 2y + z = 4\), \(2x + 4y + 2z = a\) and \(x - y + z = 4\). (a) Find the value of \(a\) for which the three planes have a common line, and find a vector equation of the line. (b) State the arrangement of the planes when \(a \ne 8\).
**(a)** The normal to \(\Pi_2\) is \(2\) times the normal to \(\Pi_1\), so the planes are parallel. [B1]
They coincide when the equation of \(\Pi_2\) is twice that of \(\Pi_1\), so \(a = 2 \times 4 = 8\). [B1]
Then the common points of all three planes are the points of \(\Pi_1\) and \(\Pi_3\). Direction of the line:
\[\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \times \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ -3 \end{pmatrix}\] [M1]
which is parallel to \(\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}\). [A1]
A point: put \(z = 0\), so \(x + 2y = 4\) and \(x - y = 4\). Then \(3y = 0\), \(y = 0\), \(x = 4\). [M1]
\[\mathbf{r} = \begin{pmatrix} 4 \\ 0 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}\] [A1]
**(b)** If \(a \ne 8\), \(\Pi_1\) and \(\Pi_2\) are distinct parallel planes, so no point lies on both. [B1] \(\Pi_3\) is not parallel to them (its normal is not a multiple of theirs) and cuts each in a line, so there is no common point. [B1]

**Check** the line lies on \(\Pi_2\) for \(a = 8\): \(2(4 + \lambda) + 4(0) + 2(-\lambda) = 8\).
:::

## Solving a consistent system

When the system is consistent but \(\det \mathbf{A} = 0\), you cannot write a single answer. The solutions form a line (one free parameter) or a plane (two). The method is to keep only the independent equations and let the unknown that is left over be a parameter.

:::steps
1. Find the relation between the rows and confirm that the system is consistent.
2. Discard the equation that follows from the others (a row that is a combination of the rest).
3. Put one unknown equal to a parameter, \(\lambda\), and solve the remaining equations for the other two unknowns in terms of \(\lambda\).
4. Write the answer as \(x = \dots\), \(y = \dots\), \(z = \lambda\), or as a vector equation \(\mathbf{r} = \mathbf{a} + \lambda\mathbf{d}\). The direction \(\mathbf{d}\) can be checked against the vector product of the normals of the two planes you kept.
:::

:::eg Show that \(x - y + 2z = 1\), \(2x + y - z = 5\), \(3x + z = c\) is consistent only when \(c = 6\), and when \(c = 6\) find all solutions.
The third row \((3, 0, 1)\) is the sum of the first two rows \((1, -1, 2)\) and \((2, 1, -1)\). So the third equation follows from the first two if \(c = 1 + 5 = 6\), and contradicts them otherwise.

For \(c = 6\), keep the first two equations. Adding them: \(3x + z = 6\), so \(z = 6 - 3x\). Let \(x = \lambda\), so \(z = 6 - 3\lambda\). From the second equation, \(y = 5 - 2x + z = 5 - 2\lambda + 6 - 3\lambda = 11 - 5\lambda\).
\[\mathbf{r} = \begin{pmatrix} 0 \\ 11 \\ 6 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -5 \\ -3 \end{pmatrix}\]
**Check** in the third equation: \(3\lambda + 6 - 3\lambda = 6\).
:::

If two of the three equations are the same plane, only two independent equations remain, and you proceed in the same way. If all three are the same plane, one equation remains and two unknowns are free: for \(x + y + z = 3\), let \(y = \mu\) and \(z = \lambda\), so \(x = 3 - \mu - \lambda\).

The widget below shows a sheaf: three planes with the row relation holding for the constants, so they share a line (drawn). Change the last number in the third equation from 7 to anything else, and the verdict changes from a common line to a triangular prism, with no change to the matrix.

:::html
<div class="widget" data-w="fm-planes" data-planes="1,2,-1,4; 2,-1,3,3; 3,1,2,7"></div>
:::

## An unknown in the equations

A very common exam question puts a letter \(k\) in the matrix or in the right-hand side. The determinant, as a function of \(k\), is zero for particular values of \(k\). For every other value there is a unique solution. For each special value you test for consistency and describe the planes.

:::steps
1. Find \(\det \mathbf{A}\) in terms of \(k\) and solve \(\det \mathbf{A} = 0\).
2. For any other \(k\), state that there is a unique solution (and find it if asked).
3. For each value of \(k\) from step 1, substitute it and look for the row relation. Test the right-hand sides.
4. Describe the geometry: a sheaf if consistent with no parallel normals, a prism if not.
:::

:::eg (Exam style) The system \(x + 2z = 3\), \(-x - 2y + kz = 1\), \(3x + ky + 2z = 5\) is written as \(\mathbf{Ax} = \mathbf{b}\). (a) Show that the system has a unique solution unless \(k = 2\) or \(k = -4\). (b) Show that the system is consistent when \(k = 2\), and find the general solution. (c) Show that the system is inconsistent when \(k = -4\) and describe the three planes.
**(a)** Expand \(\det \mathbf{A}\) along the first row:
\[\det \begin{pmatrix} 1 & 0 & 2 \\ -1 & -2 & k \\ 3 & k & 2 \end{pmatrix} = 1(-4 - k^2) - 0 + 2(-k + 6)\] [M1]
\[= -k^2 - 2k + 8\] [A1]
The solution is unique when \(\det \mathbf{A} \ne 0\). Solve \(k^2 + 2k - 8 = 0\):
\[(k + 4)(k - 2) = 0\] [M1]
so \(\det \mathbf{A} = 0\) only when \(k = 2\) or \(k = -4\). [A1]
**(b)** For \(k = 2\) the rows are \((1, 0, 2)\), \((-1, -2, 2)\), \((3, 2, 2)\). Row 3 is \(2 \times\) row 1 minus row 2. [M1]
The constants satisfy \(5 = 2 \times 3 - 1\), so the third equation is a consequence of the first two: consistent. [A1]
From the first equation \(x = 3 - 2z\). The second gives \(-(3 - 2z) - 2y + 2z = 1\), so \(y = 2z - 2\). [M1]
Let \(z = \lambda\):
\[x = 3 - 2\lambda, \quad y = -2 + 2\lambda, \quad z = \lambda\] [A1]
**(c)** For \(k = -4\) the rows are \((1, 0, 2)\), \((-1, -2, -4)\), \((3, -4, 2)\). Row 3 is \(5 \times\) row 1 \(+ 2 \times\) row 2. [M1]
The constants would need \(5 \times 3 + 2 \times 1 = 17\), but the third constant is 5, so the system is inconsistent. [A1]
No two of the normals are parallel, so the planes form a triangular prism. [B1]

**Check** (b) in the third equation: \(3(3 - 2\lambda) + 2(-2 + 2\lambda) + 2\lambda = 9 - 4 + 0\lambda = 5\).
:::

Sometimes the unknown sits in the right-hand side, as in the example with \(c\) above. Then the matrix is fixed, \(\det \mathbf{A}\) is a number, and the question is whether the constants satisfy the row relation.

:::exam Show your relation between the rows
The mark schemes reward the row relation (or an elimination ending in \(0 = 0\) or \(0 = k\)) and the comparison of the constants. "The determinant is 0, so no solution" earns nothing for the conclusion. When the question asks for "the arrangement of the planes", name it: sheaf (common line), triangular prism, or parallel planes. MF19 gives no formula for any of this: you need the cofactor method for inverses and the vector product for directions.
:::

## The equations with zero on the right

The case \(\mathbf{b} = \mathbf{0}\) always has the solution \(\mathbf{x} = \mathbf{0}\) (three planes through the origin). So the only question is whether there are other solutions, and the determinant answers it.

:::key Homogeneous equations
For \(\mathbf{Ax} = \mathbf{0}\):
- if \(\det \mathbf{A} \ne 0\) the only solution is \(\mathbf{x} = \mathbf{0}\);
- if \(\det \mathbf{A} = 0\) there are also non-zero solutions, always infinitely many: a line through the origin (a sheaf through \(O\)), or a plane through the origin.
:::

This is the idea behind eigenvectors in [Eigenvalues and eigenvectors](#math.fm.matrices2): you will choose a number \(\lambda\) that makes a matrix singular so that \(\mathbf{Ax} = \mathbf{0}\) has a non-zero solution.

:::eg Find the non-zero solutions of \(x + 2y - z = 0\), \(2x - y + 3z = 0\), \(3x + y + 2z = 0\).
The matrix is the one from the sheaf example, with determinant 0, and row 3 is row 1 plus row 2, so the third equation is redundant. Use the first two. From the first, \(x = z - 2y\). Substituting into the second: \(2z - 4y - y + 3z = 0\), so \(y = z\) and \(x = -z\).
\[\begin{pmatrix} x \\ y \\ z \end{pmatrix} = t\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}\]
for any non-zero \(t\). The solutions form a line through the origin. **Check** in the third equation: \(-3 + 1 + 2 = 0\).
:::

## Planes in other forms

Questions often give planes as \(\mathbf{r} \cdot \mathbf{n} = p\) or through a point with two directions. Convert each to \(ax + by + cz = d\) first: for \(\mathbf{r} \cdot \mathbf{n} = p\) the numbers are the components of \(\mathbf{n}\) and \(d = p\). For a plane given as \(\mathbf{r} = \mathbf{a} + s\mathbf{u} + t\mathbf{v}\), take \(\mathbf{n} = \mathbf{u} \times \mathbf{v}\) and \(d = \mathbf{a} \cdot \mathbf{n}\), as in [Vectors: the vector product and planes](#math.fm.vectors). Then use the matrix methods above.

:::eg Three planes have equations \(\mathbf{r} \cdot \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = 3\), \(\mathbf{r} \cdot \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} = 3\) and \(\mathbf{r} \cdot \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix} = 6\). Describe how they meet.
In Cartesian form: \(x + y + z = 3\), \(2x - y + z = 3\), \(3x + 2z = 6\).
The third normal \(\begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix}\) is the sum of the first two, and \(3 + 3 = 6\) matches the third constant. So the third equation follows from the first two: the planes are consistent. No two normals are parallel, so they form a sheaf. Adding the first two equations gives \(3x + 2z = 6\) again, and the common line is
\[\mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} -2 \\ -1 \\ 3 \end{pmatrix}\]
(put \(z = 3\lambda\); then \(x = 2 - 2\lambda\) and \(y = 3 - x - z = 1 - \lambda\)). **Check**: \(2x - y + z = 4 - 4\lambda - 1 + \lambda + 3\lambda = 3\).
:::

:::board
Cambridge 9231 words this topic as "consistency or inconsistency" of three equations in three unknowns, to be related to the singularity of the matrix and interpreted geometrically as lines and planes: three planes meeting at a point, in a common line, or with no common point. It stays with three equations in three unknowns, so the methods here (inverse, elimination and the row relation) are all you need.
:::

:::eg Spot the error: the system \(x + 2y + z = 5\), \(3x - y + 2z = 6\), \(4x + y + 3z = 11\) is given. (a) Show that the matrix of coefficients is singular. (b) Determine whether the system has any solutions. The question is worth 4 marks.
A student wrote this answer.

Line 1: \(\det = 1(-3 - 2) - 2(9 - 8) + 1(3 + 4) = -5 - 2 + 7 = 0\), so the matrix is singular.
Line 2: The determinant is zero, so the equations have no solution.

Line 1 is correct and shows the expansion. [M1] [A1]

**Line 2 draws the conclusion from the determinant alone, which is not valid.** [M0] [A0] A singular matrix gives no solution or infinitely many, and the student never tested the constants. Row 3 is row 1 plus row 2, and \(5 + 6 = 11\), so the system is consistent. The student scores 2 out of 4.

Correct line 2: row 3 is row 1 plus row 2 and the constants add up, so there are infinitely many solutions (a sheaf). The marks for this line would be [M1] [A1]. **Check** with two solutions: \((1, 1, 2)\) gives \(1 + 2 + 2 = 5\), \(3 - 1 + 4 = 6\) and \(4 + 1 + 6 = 11\); and \((6, 2, -5)\) gives \(6 + 4 - 5 = 5\), \(18 - 2 - 10 = 6\) and \(24 + 2 - 15 = 11\).
:::

:::try Start easy, finish at exam standard
Q: Write \(2x - y + 3z = 5\), \(x + 4y = 2\), \(3y - z = 0\) as a matrix equation.
A: \(\begin{pmatrix} 2 & -1 & 3 \\ 1 & 4 & 0 \\ 0 & 3 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 5 \\ 2 \\ 0 \end{pmatrix}\). The second equation has no \(z\) and the third has no \(x\), so each of those entries is 0.
Q: Write \(\begin{pmatrix} 1 & 0 & 2 \\ 3 & -1 & 0 \\ 0 & 2 & 5 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ -3 \end{pmatrix}\) as three equations.
A: \(x + 2z = 4\), \(3x - y = 1\), \(2y + 5z = -3\).
Q: Solve \(x + y + z = 6\), \(2x - y + z = 3\), \(x + 2y - z = 2\).
A: Eliminate \(z\). The first plus the third gives \(2x + 3y = 8\), and the first minus the second gives \(-x + 2y = 3\). Then \(x = 2y - 3\), so \(4y - 6 + 3y = 8\), \(y = 2\) and \(x = 1\). Finally \(z = 6 - 1 - 2 = 3\). The solution is \((1, 2, 3)\); check in the second equation: \(2 - 2 + 3 = 3\).
Q: Find \(\det\) of \(\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}\) and of \(\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}\). Which gives a unique solution to \(\mathbf{Ax} = \mathbf{b}\) for every \(\mathbf{b}\)?
A: Expand along the first row:
\[\begin{aligned}
\text{first: } &1(50 - 48) - 2(40 - 42) + 3(32 - 35) = 2 + 4 - 9 = -3 \\
\text{second: } &1(45 - 48) - 2(36 - 42) + 3(32 - 35) = -3 + 12 - 9 = 0
\end{aligned}\]
Only the first gives a unique solution for every \(\mathbf{b}\), because only its determinant is not zero.
Q: The planes \(x + y + z = 3\), \(x - y + z = 1\), \(2x + 2z = 4\) are given. Find how they meet.
A: Row 3 is row 1 plus row 2 and \(3 + 1 = 4\), so the system is consistent. Subtracting the first two gives \(2y = 2\), \(y = 1\); then \(x + z = 2\). With \(x = \lambda\): \((\lambda, 1, 2 - \lambda)\), a common line (sheaf).
Q: The planes \(x + y + z = 3\), \(x - y + z = 1\), \(2x + 2z = 5\) are given. Find how they meet.
A: The rows are as in the last question but \(3 + 1 \ne 5\). So the system is inconsistent. No two normals are parallel, so the planes form a triangular prism.
Q: Three planes are \(x + y - z = 2\), \(2x + 2y - 2z = 4\) and \(3x - y + z = 2\). How do they meet?
A: The second equation is twice the first, so these two planes coincide. The third meets that plane in a line: adding the first and third gives \(4x = 4\), \(x = 1\), then \(y - z = 1\). A common line: \((1, 1 + \lambda, \lambda)\).
Q: Three planes are \(x + 2y - z = 1\), \(2x + 4y - 2z = 5\) and \(3x + 6y - 3z = 2\). How do they meet?
A: All three normals are multiples of \(\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}\), so the planes are parallel. The constants \(1, 5, 2\) are not in the ratio \(1 : 2 : 3\), so no two coincide: three distinct parallel planes, no common point.
Q: For which value of \(c\) does \(x + y + z = 1\), \(2x - y + 4z = 5\), \(3x + 5z = c\) have solutions?
A: Row 3 is row 1 plus row 2: \((3, 0, 5)\), so \(c = 1 + 5 = 6\). For \(c = 6\) there are infinitely many solutions. For any other \(c\) there are none.
Q: Show that \(x + 2y + z = 0\), \(2x + y - z = 0\), \(3x + 3y = 0\) has solutions other than \(x = y = z = 0\), and find them.
A: Row 3 is row 1 plus row 2, so the third equation is redundant and the determinant is 0. Adding the first two equations gives \(3x + 3y = 0\), so \(y = -x\). The first equation then gives \(x - 2x + z = 0\), so \(z = x\). The solutions are \((t, -t, t)\) for any \(t\); check in the second equation: \(2t - t - t = 0\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The matrix \(\mathbf{M} = \begin{pmatrix} 2 & 1 & 3 \\ 1 & -1 & 2 \\ 0 & 4 & 5 \end{pmatrix}\). Find \(\det \mathbf{M}\) and state whether \(2x + y + 3z = 1\), \(x - y + 2z = 2\), \(4y + 5z = 0\) has a unique solution.
A: \(\det \mathbf{M} = 2(-5 - 8) - 1(5 - 0) + 3(4 - 0)\) [M1] \(= -26 - 5 + 12\) [A1] \(= -19\). [A1]
The determinant is not zero, so the system has a unique solution. [B1]
Q: [4 marks] ★ Solve \(2x + y - z = -1\), \(x + 3y + z = 0\), \(3x - 2y + 2z = 9\).
A: Add the first two: \(3x + 4y = -1\) [M1]. Eliminate \(z\) from the second and third: \(2 \times\) (second) \(-\) third gives \(-x + 8y = -9\) [M1]. Then \(x = 8y + 9\) and \(24y + 27 + 4y = -1\), so \(y = -1\) and \(x = 1\) [A1]. Then \(z = -x - 3y = 2\), so \((x, y, z) = (1, -1, 2)\). [A1]
Q: [4 marks] ★ A farmer mixes three feeds. Per kilogram they contain protein, fibre and fat in the amounts (in units) \((2, 1, 1)\), \((1, 2, 1)\) and \((3, 1, 2)\) for feeds \(X\), \(Y\) and \(Z\) respectively. A ration of \(x\) kg of \(X\), \(y\) kg of \(Y\) and \(z\) kg of \(Z\) must contain 11 units of protein, 8 of fibre and 7 of fat. (a) Write this as a matrix equation. (b) Given that the inverse of the matrix is \(\dfrac12\begin{pmatrix} 3 & 1 & -5 \\ -1 & 1 & 1 \\ -1 & -1 & 3 \end{pmatrix}\), find \(x\), \(y\) and \(z\).
A: (a) Protein: \(2x + y + 3z = 11\), fibre: \(x + 2y + z = 8\), fat: \(x + y + 2z = 7\). So \(\begin{pmatrix} 2 & 1 & 3 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 11 \\ 8 \\ 7 \end{pmatrix}\). [B1]
(b) \(\mathbf{x} = \dfrac12\begin{pmatrix} 3 & 1 & -5 \\ -1 & 1 & 1 \\ -1 & -1 & 3 \end{pmatrix}\begin{pmatrix} 11 \\ 8 \\ 7 \end{pmatrix}\) [M1] \(= \dfrac12\begin{pmatrix} 6 \\ 4 \\ 2 \end{pmatrix}\) [A1] so \(x = 3\), \(y = 2\), \(z = 1\). [A1]
Q: [6 marks] ★★ Find the values of \(k\) for which \(kx + y + z = 0\), \(x + ky + z = 0\), \(x + y + kz = 0\) has non-zero solutions, and solve the equations when \(k = -2\).
H: The system has non-zero solutions exactly when the determinant of the coefficient matrix is 0.
H: The determinant factorises: look for the factor \((k - 1)\) twice.
A: \(\det = k(k^2 - 1) - 1(k - 1) + 1(1 - k)\) [M1] \(= (k - 1)(k^2 + k - 2) = (k - 1)^2(k + 2)\). [A1]
Non-zero solutions need \(\det = 0\) [M1] so \(k = 1\) or \(k = -2\). [A1]
For \(k = -2\): the first two equations \(-2x + y + z = 0\) and \(x - 2y + z = 0\) subtract to \(-3x + 3y = 0\), so \(x = y\) and then \(z = x\). [M1] The solutions are \((t, t, t)\). [A1]
Q: [7 marks] ★★ The system \(x + y + 2z = 1\), \(3x - y + z = 11\), \(-x + 3y + kz = -9\) is given. (a) Show that there is a unique solution unless \(k = 3\). (b) Show that the system is consistent when \(k = 3\), and find a vector equation of the line of solutions.
H: Expand the determinant along the first row; it is linear in \(k\).
H: When \(k = 3\), find the relation \(\text{row 3} = p\,\text{row 1} + q\,\text{row 2}\) and test the constants.
A: (a) \(\det = 1(-k - 3) - 1(3k + 1) + 2(9 - 1)\) [M1] \(= 12 - 4k\). [A1] This is zero only for \(k = 3\), so the solution is unique unless \(k = 3\). [A1]
(b) For \(k = 3\), row 3 is \(2 \times\) row 1 \(-\) row 2: \((2 - 3, 2 + 1, 4 - 1) = (-1, 3, 3)\). [M1]
The constants give \(2 \times 1 - 11 = -9\), which matches, so the system is consistent. [A1]
Adding the first two equations: \(4x + 3z = 12\). Let \(z = 4\lambda\): \(x = 3 - 3\lambda\) and \(y = 1 - x - 2z = -2 - 5\lambda\). [M1]
\(\mathbf{r} = \begin{pmatrix} 3 \\ -2 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} -3 \\ -5 \\ 4 \end{pmatrix}\) [A1]
Q: [6 marks] ★★ The planes \(\Pi_1\), \(\Pi_2\), \(\Pi_3\) have equations \(3x - y + 2z = 4\), \(6x - 2y + 4z = c\) and \(x + y - z = 0\). (a) Find the value of \(c\) for which the planes have a common line and find a vector equation for it. (b) Describe the arrangement of the planes when \(c\) takes any other value.
A: (a) The second equation has twice the left-hand side of the first, so \(\Pi_1\) and \(\Pi_2\) coincide when \(c = 8\). [B1]
The line is \(\Pi_1 \cap \Pi_3\). Direction: \(\begin{pmatrix} 3 \\ -1 \\ 2 \end{pmatrix} \times \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} -1 \\ 5 \\ 4 \end{pmatrix}\). [M1 A1]
Point: put \(z = 0\): \(3x - y = 4\), \(x + y = 0\), so \(x = 1\), \(y = -1\). \(\mathbf{r} = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} -1 \\ 5 \\ 4 \end{pmatrix}\). [A1]
(b) For \(c \ne 8\), \(\Pi_1\) and \(\Pi_2\) are distinct parallel planes and \(\Pi_3\) crosses both: no common point. [B1] [B1]
Q: [8 marks] ★★★ The system \(x + y + z = 2\), \(2x + 3y + 4z = 5\), \(3x + 4y + 5z = a\) is given. (a) Show that the matrix of coefficients is singular. (b) Find the value of \(a\) for which the system is consistent. (c) For this value of \(a\), find the general solution. (d) State the geometrical arrangement of the planes when \(a\) takes any other value.
H: Compare row 3 with row 1 plus row 2.
H: For (c), keep the first two equations and eliminate \(x\).
A: (a) \(\det = 1(15 - 16) - 1(10 - 12) + 1(8 - 9) = -1 + 2 - 1 = 0\). [M1 A1]
(b) Row 3 is row 1 plus row 2, so the system is consistent only if \(a = 2 + 5 = 7\). [M1 A1]
(c) From the first, \(x = 2 - y - z\). The second gives \(4 - 2y - 2z + 3y + 4z = 5\), so \(y = 1 - 2z\) and \(x = 1 + z\). [M1]
With \(z = \lambda\): \(\mathbf{r} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}\). [A1 A1]
(d) For \(a \ne 7\) the system is inconsistent and no two normals are parallel, so the planes form a triangular prism. [B1]
Q: [9 marks] (#math.fm.vectors2) ★★★ The planes \(\Pi_1\), \(\Pi_2\), \(\Pi_3\) have equations \(x + y - z = 2\), \(2x - y + z = 1\) and \(4x + ay + z = b\). (a) Find a vector equation of the line \(l\) in which \(\Pi_1\) and \(\Pi_2\) meet. (b) Find the value of \(a\) for which \(l\) is parallel to \(\Pi_3\), and then the value of \(b\) for which \(l\) lies in \(\Pi_3\). (c) For \(a = 1\) and \(b = 7\), find the coordinates of the point where the three planes meet.
H: The direction of \(l\) is the vector product of the normals of \(\Pi_1\) and \(\Pi_2\).
H: A line is parallel to a plane when its direction is perpendicular to the plane's normal.
H: In (c), put a general point of \(l\) into the equation of \(\Pi_3\).
A: (a) \(\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \times \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -3 \\ -3 \end{pmatrix}\), parallel to \(\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}\). [M1 A1]
Adding the first two equations: \(3x = 3\), so \(x = 1\), and then \(y - z = 1\). A point is \((1, 1, 0)\). \(\mathbf{r} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}\). [A1]
(b) The direction is perpendicular to the normal of \(\Pi_3\): \(\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ a \\ 1 \end{pmatrix} = a + 1 = 0\), so \(a = -1\). [M1 A1]
The point \((1, 1, 0)\) is on \(\Pi_3\) when \(4 - 1 + 0 = b\), so \(b = 3\). [M1 A1]
(c) Put \((1, 1 + \lambda, \lambda)\) into \(4x + y + z = 7\): \(4 + 1 + \lambda + \lambda = 7\), so \(\lambda = 1\). [M1] The point is \((1, 2, 1)\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Find all real values of \(a\) and \(b\) for which \(x + y + z = 1\), \(x + ay + z = b\), \(x + y + az = 2\) has (i) a unique solution, (ii) infinitely many solutions, (iii) no solution. Describe the three planes when \(a = 1\).
H: Subtract the first equation from the other two.
H: What do the left-hand sides look like when \(a = 1\)?
A: Subtract the first equation from each of the others: \((a - 1)y = b - 1\) and \((a - 1)z = 1\). [M1]
If \(a \ne 1\): \(z = \dfrac{1}{a - 1}\), \(y = \dfrac{b - 1}{a - 1}\) and \(x = 1 - y - z\): a unique solution for every \(b\). [M1 A1]
If \(a = 1\): the second subtracted equation reads \(0 = 1\), which is never true, so there is no solution for any \(b\) (and never infinitely many). [A1]
(i) \(a \ne 1\), any \(b\); (ii) no values; (iii) \(a = 1\), any \(b\). [A1]
With \(a = 1\) all three equations have the left-hand side \(x + y + z\), so the planes are parallel (with \(b = 1\) the first two coincide); the right-hand sides \(1, b, 2\) cannot all be equal, so there is no common point. [A1]
Q: [7 marks] ★★★ A 12 V battery is connected in series with a \(5\,\Omega\) resistor, and then to two branches in parallel: one with a \(2\,\Omega\) resistor and one with a resistor of \(k\,\Omega\), where \(k > 0\). The currents are \(I_1\) in the battery, \(I_2\) in the \(2\,\Omega\) branch and \(I_3\) in the \(k\,\Omega\) branch. Kirchhoff's laws give \(I_1 - I_2 - I_3 = 0\), \(5I_1 + 2I_2 = 12\) and \(2I_2 - kI_3 = 0\). (a) Write the equations as a matrix equation. (b) Show that the matrix is non-singular for all \(k > 0\). (c) Find \(I_3\) in terms of \(k\).
H: Expand the determinant along the first row and look at the sign of the result when \(k > 0\).
H: From the third equation \(I_3 = \dfrac{2I_2}{k}\). Substitute into the first, then the second.
A: (a) \(\begin{pmatrix} 1 & -1 & -1 \\ 5 & 2 & 0 \\ 0 & 2 & -k \end{pmatrix}\begin{pmatrix} I_1 \\ I_2 \\ I_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 12 \\ 0 \end{pmatrix}\). [B1]
(b) \(\det = 1(-2k - 0) + 1(-5k - 0) - 1(10 - 0)\) [M1] \(= -7k - 10\). [A1] For \(k > 0\) this is negative, so it is never zero and the solution is unique. [A1]
(c) \(I_3 = \dfrac{2I_2}{k}\) and \(I_1 = I_2 + I_3 = I_2\left(1 + \dfrac2k\right)\). Substitute into \(5I_1 + 2I_2 = 12\): \(I_2\left(7 + \dfrac{10}{k}\right) = 12\) [M1] so \(I_2 = \dfrac{12k}{7k + 10}\). [A1] Then \(I_3 = \dfrac{24}{7k + 10}\). [A1]
:::

:::quiz
? The matrix \(\mathbf{A}\) of a system \(\mathbf{Ax} = \mathbf{b}\) has \(\det \mathbf{A} = 0\). What can you say?
- The system has no solution
- The system has infinitely many solutions
+ The system has either no solution or infinitely many solutions
- The only solution is \(\mathbf{x} = \mathbf{0}\)
> A singular matrix removes the guarantee of a unique solution; the constants then decide. "No solution" and "infinitely many" are each possible, and \(\mathbf{x} = \mathbf{0}\) is a solution only when \(\mathbf{b} = \mathbf{0}\).
? Row 3 of the matrix is row 1 plus row 2, but \(d_3 \ne d_1 + d_2\). How do the planes meet?
- In a single point
- In a common line, a sheaf
+ In a triangular prism: no common point
- As three parallel planes
> The relation between the rows fails for the constants, so the equations contradict each other. With no two normals parallel, each pair of planes meets in a line and the three lines are parallel but different. A sheaf needs the constants to obey the same relation.
? The planes \(x + y + z = 2\), \(2x + 2y + 2z = 7\) and \(x - y = 0\) have normals with exactly two parallel. What is the arrangement?
+ Two distinct parallel planes cut by a third: no common point
- A sheaf
- Three planes meeting at a point
- Two planes coincide and a third cuts them in a line
> The second equation would be \(2x + 2y + 2z = 4\) if it coincided with the first, but the constant is 7. So the first two are distinct parallel planes and nothing lies on both.
? Which statement about \(\mathbf{Ax} = \mathbf{0}\) is true?
- If \(\det \mathbf{A} \ne 0\) there are infinitely many solutions
- It may have no solution
+ If \(\det \mathbf{A} = 0\) there are non-zero solutions
- If \(\det \mathbf{A} = 0\) the only solution is \(\mathbf{x} = \mathbf{0}\)
> \(\mathbf{x} = \mathbf{0}\) always works, so the equations are never inconsistent. It is the only solution exactly when \(\mathbf{A}\) is non-singular.
? If \(\det \mathbf{A} \ne 0\), what is the solution of \(\mathbf{Ax} = \mathbf{b}\)?
- \(\mathbf{x} = \mathbf{bA}^{-1}\)
+ \(\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}\)
- \(\mathbf{x} = \dfrac{\mathbf{b}}{\mathbf{A}}\)
- \(\mathbf{x} = \mathbf{A}\mathbf{b}^{-1}\)
> Multiply on the left by \(\mathbf{A}^{-1}\). Matrices cannot be divided, and \(\mathbf{bA}^{-1}\) is not even defined for a column \(\mathbf{b}\).
? Two of three equations describe the same plane and the third plane crosses it. The solution set is
- a single point
+ a line
- a plane
- empty
> The two equal planes impose one condition, the third plane another, and two independent conditions on three unknowns leave one free parameter: a line.
:::

:::checklist What you can now do
- [ ] I can write three linear equations in three unknowns as \(\mathbf{Ax} = \mathbf{b}\), and write a matrix equation back as three equations.
- [ ] I can solve a system with a non-singular matrix using the inverse, or by elimination, and say that the planes meet at a point.
- [ ] I can state that a singular matrix gives either no solution or infinitely many, and decide which by finding the relation between the rows.
- [ ] I can define consistent and inconsistent, and describe the seven arrangements of three planes with the algebra of each.
- [ ] I can solve a consistent singular system with a parameter and write the solution as a line.
- [ ] I can find the values of an unknown that make the matrix singular, and decide consistency for each.
- [ ] I can interpret the geometry: common point, common line (sheaf), triangular prism, parallel planes.
- [ ] I can state when \(\mathbf{Ax} = \mathbf{0}\) has non-zero solutions.
:::

:::recap
- A system of three equations is \(\mathbf{Ax} = \mathbf{b}\); each row of \(\mathbf{A}\) is the normal of a plane.
- \(\det \mathbf{A} \ne 0\): unique solution \(\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}\); the planes meet at a point.
- \(\det \mathbf{A} = 0\): no unique solution. Test consistency with the row relation and the constants.
- Consistent with no two normals parallel: a sheaf (common line). Inconsistent with no two normals parallel: a triangular prism.
- Parallel normals: look at the constants; distinct parallel planes give no solution, coinciding planes leave a line (or a plane if all three coincide).
- Solutions of a consistent singular system: a line with one parameter, or a plane with two.
- Letter \(k\) in the matrix: solve \(\det \mathbf{A} = 0\), then test consistency at each value.
- \(\mathbf{Ax} = \mathbf{0}\) has non-zero solutions exactly when \(\det \mathbf{A} = 0\).
:::

:::links
- watch: [The determinant](https://www.3blue1brown.com/lessons/determinant) · 3Blue1Brown · why the determinant being zero squashes space, which is why a singular matrix has no inverse
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · worked examples of three equations and three planes
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · graded questions with answers on matrices, systems and planes
- practise: [Linear algebra](https://www.khanacademy.org/math/linear-algebra) · Khan Academy · systems of equations and matrices
- explore: [Desmos 3D](https://www.desmos.com/3d) · Desmos · draw three planes and turn them to see a sheaf or a prism
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Eigenvalues and eigenvectors](#math.fm.matrices2) turns the question "when does \(\mathbf{Ax} = \mathbf{0}\) have a non-zero solution?" into a way of finding the directions a matrix only stretches.
