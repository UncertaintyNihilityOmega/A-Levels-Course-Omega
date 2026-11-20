@chapter math.fm.matrices2
@title Eigenvalues and eigenvectors
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary A matrix usually turns a vector to point in a new direction, but some special directions are only stretched. You will find these eigenvectors and their stretch factors (the eigenvalues) for 2×2 and 3×3 matrices, prove simple properties from the definition, write a matrix as QDQ⁻¹ to find its powers, and use the fact that a matrix satisfies its own characteristic equation to find powers and inverses.

:::why
Applying a matrix over and over (the next generation of a population, the next step of a recurrence, the next hour of a mixing process) is hard to see directly. Along an eigenvector the matrix does something very simple: it multiplies by a number. If you can split a problem into eigenvector directions, a hundred steps cost no more than one. This is one of the most used ideas in applied mathematics, from search engines to quantum mechanics, and the Further Mathematics papers test it in several forms: finding eigenvalues, proving properties, diagonalising and finding powers.
:::

**Before you start**, you need determinants and inverses from [Matrices: algebra, determinants and inverses](#math.fm.matrices), invariant lines from [Matrices as transformations](#math.fm.transform), the factor theorem for cubics from [Modulus and polynomials](#math.p3.algebra), and the idea that a homogeneous system has non-zero solutions only when the determinant is zero, from [Three equations, three planes](#math.fm.systems). The sum and product of the roots of a cubic, from [Roots of polynomial equations](#math.fm.roots), give a quick check on every characteristic equation.

:::try Warm-up
Q: The matrix \(\begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\) maps \((1, 1)\) to which point? (from [Matrices as transformations](#math.fm.transform))
A: \(\begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \end{pmatrix}\): the point \((4, 4)\), on the same line through the origin.
Q: Factorise \(\lambda^3 - 6\lambda^2 + 11\lambda - 6\), given that \(\lambda = 1\) is a root. (from [Modulus and polynomials](#math.p3.algebra))
A: Divide by \((\lambda - 1)\): \(\lambda^3 - 6\lambda^2 + 11\lambda - 6 = (\lambda - 1)(\lambda^2 - 5\lambda + 6) = (\lambda - 1)(\lambda - 2)(\lambda - 3)\).
Q: Does \(x + y = 0\), \(2x + 2y = 0\) have a solution other than \(x = y = 0\)? (from [Three equations, three planes](#math.fm.systems))
A: Yes. The determinant \(\begin{vmatrix} 1 & 1 \\ 2 & 2 \end{vmatrix} = 0\), and the equations say \(y = -x\), so \((t, -t)\) is a solution for every \(t\).
:::

## Directions that are only stretched

Apply \(\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\) to a few vectors.
\[\begin{aligned}
\mathbf{A}\begin{pmatrix} 1 \\ 0 \end{pmatrix} &= \begin{pmatrix} 3 \\ 2 \end{pmatrix} \\
\mathbf{A}\begin{pmatrix} 1 \\ 1 \end{pmatrix} &= \begin{pmatrix} 4 \\ 4 \end{pmatrix} = 4\begin{pmatrix} 1 \\ 1 \end{pmatrix} \\
\mathbf{A}\begin{pmatrix} 1 \\ -2 \end{pmatrix} &= \begin{pmatrix} 1 \\ -2 \end{pmatrix} = 1\begin{pmatrix} 1 \\ -2 \end{pmatrix}
\end{aligned}\]
The first vector is turned into a different direction. The second is stretched by a factor of 4 and the third is not changed at all. Those two directions, \(y = x\) and \(y = -2x\), are exactly the invariant lines through the origin that you found for this matrix in [Matrices as transformations](#math.fm.transform).

:::def Eigenvalue and eigenvector
Let \(\mathbf{A}\) be a square matrix. A non-zero vector \(\mathbf{e}\) is an **eigenvector** of \(\mathbf{A}\) if
\[\mathbf{Ae} = \lambda\mathbf{e}\]
for some number \(\lambda\). The number \(\lambda\) is the **eigenvalue** of \(\mathbf{A}\) belonging to \(\mathbf{e}\). The vector \(\mathbf{e}\) must not be the zero vector, because \(\mathbf{A0} = \lambda\mathbf{0}\) is true for every \(\lambda\) and tells you nothing.
:::

The word "eigen" is German for "own" or "characteristic". An eigenvector is a direction that belongs to the matrix. The eigenvalue says what the matrix does along that direction: it multiplies lengths by \(\lambda\). A negative eigenvalue flips the vector to point the opposite way, and an eigenvalue of 0 collapses it to the origin.

Try the matrix in the tool below. The two directions that it only stretches are drawn, and the panel lists the eigenvalues and eigenvector directions. Then try the presets. A shear has only one direction that does not move, and a rotation has none, so its eigenvalues are not real.

:::html
<div class="widget" data-w="fm-matrix" data-m="3,1,2,2" data-shape="triangle" data-show="grid,det,eigen" data-presets="rotation,reflection,shear,stretch,enlargement"></div>
:::

:::warn Any non-zero multiple is also an eigenvector
If \(\mathbf{Ae} = \lambda\mathbf{e}\), then for any number \(k \ne 0\), \(\mathbf{A}(k\mathbf{e}) = k\mathbf{Ae} = \lambda(k\mathbf{e})\). So \(\begin{pmatrix} 2 \\ 2 \end{pmatrix}\) and \(\begin{pmatrix} -3 \\ -3 \end{pmatrix}\) are eigenvectors too. An eigenvector is a direction, and you choose the simplest vector along it. The eigenvalue does not change.
:::

## The characteristic equation

To find eigenvalues, rewrite \(\mathbf{Ae} = \lambda\mathbf{e}\) as \(\mathbf{Ae} - \lambda\mathbf{Ie} = \mathbf{0}\), which is
\[(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}\]
(The identity matrix \(\mathbf{I}\) is needed: you cannot subtract a number from a matrix.) This is a system of homogeneous equations, as in [Three equations, three planes](#math.fm.systems). It has a non-zero solution \(\mathbf{e}\) exactly when the matrix \(\mathbf{A} - \lambda\mathbf{I}\) is singular.

:::def Characteristic equation
For a square matrix \(\mathbf{A}\), the equation
\[\det(\mathbf{A} - \lambda\mathbf{I}) = 0\]
is its **characteristic equation**. Its roots are the eigenvalues of \(\mathbf{A}\). For an \(n \times n\) matrix it is a polynomial equation of degree \(n\).
:::

For a \(2 \times 2\) matrix \(\begin{pmatrix} a & b \\ c & d \end{pmatrix}\),
\[\det(\mathbf{A} - \lambda\mathbf{I}) = (a - \lambda)(d - \lambda) - bc = \lambda^2 - (a + d)\lambda + (ad - bc)\]
The number \(a + d\), the sum of the entries on the leading diagonal, is the **trace** of \(\mathbf{A}\), written \(\operatorname{tr}\mathbf{A}\).

:::key The characteristic equation of a 2×2 matrix
\[\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A} = 0\]
The two eigenvalues add up to the trace and multiply to the determinant. Use this to check your roots. (For a quadratic, this is the sum and product of roots from [Roots of polynomial equations](#math.fm.roots).)
:::

You can always write the characteristic equation as \(\det(\mathbf{A} - \lambda\mathbf{I}) = 0\), and an exam question may ask you to **show** it, so keep the working visible. The shortcut formula above is a quick way to check your answer.

:::eg Find the eigenvalues of \(\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\).
\[\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 3 - \lambda & 1 \\ 2 & 2 - \lambda \end{vmatrix} = (3 - \lambda)(2 - \lambda) - 2\]
\[= \lambda^2 - 5\lambda + 4 = (\lambda - 1)(\lambda - 4)\]
So the eigenvalues are \(\lambda = 1\) and \(\lambda = 4\). **Check**: the trace is \(3 + 2 = 5 = 1 + 4\) and the determinant is \(6 - 2 = 4 = 1 \times 4\).
:::

## Finding eigenvectors

For each eigenvalue \(\lambda\), solve \((\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}\). The matrix \(\mathbf{A} - \lambda\mathbf{I}\) is singular, so its rows are multiples of each other and you get one equation (in the \(2 \times 2\) case), which fixes the direction.

:::eg Find the eigenvectors of \(\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\).
For \(\lambda = 4\): \(\mathbf{A} - 4\mathbf{I} = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}\). Let \(\mathbf{e} = \begin{pmatrix} x \\ y \end{pmatrix}\). Both rows give the same equation, \(-x + y = 0\), so \(y = x\). An eigenvector is \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\).

For \(\lambda = 1\): \(\mathbf{A} - \mathbf{I} = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}\). Both rows give \(2x + y = 0\), so \(y = -2x\). An eigenvector is \(\begin{pmatrix} 1 \\ -2 \end{pmatrix}\).

**Check** with the definition, as at the start of the chapter: \(\mathbf{A}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = 4\begin{pmatrix} 1 \\ 1 \end{pmatrix}\) and \(\mathbf{A}\begin{pmatrix} 1 \\ -2 \end{pmatrix} = 1\begin{pmatrix} 1 \\ -2 \end{pmatrix}\).
:::

If you find that the two rows of \(\mathbf{A} - \lambda\mathbf{I}\) are **not** multiples of each other, the only solution is \(\mathbf{e} = \mathbf{0}\) and \(\lambda\) is not an eigenvalue: look for an error in the characteristic equation.

:::eg (Exam style) The matrix \(\mathbf{B} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}\). Find the eigenvalues of \(\mathbf{B}\) and a corresponding eigenvector for each.
The characteristic equation is
\[\det(\mathbf{B} - \lambda\mathbf{I}) = (4 - \lambda)(1 - \lambda) + 2 = 0\] [M1]
\[\lambda^2 - 5\lambda + 6 = 0\] [A1]
\[(\lambda - 2)(\lambda - 3) = 0, \quad \lambda = 2 \text{ or } 3\] [A1]
For \(\lambda = 2\): \(\begin{pmatrix} 2 & -2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\) gives \(x = y\), so an eigenvector is \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\). [M1]
For \(\lambda = 3\): \(\begin{pmatrix} 1 & -2 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\) gives \(x = 2y\), so an eigenvector is \(\begin{pmatrix} 2 \\ 1 \end{pmatrix}\). [A1]

**Check**: the trace is \(5 = 2 + 3\), the determinant is \(4 + 2 = 6 = 2 \times 3\), and \(\mathbf{B}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \end{pmatrix} = 3\begin{pmatrix} 2 \\ 1 \end{pmatrix}\).
:::

### Zero and negative eigenvalues

Eigenvalues can be zero or negative. A zero eigenvalue means \(\mathbf{Ae} = \mathbf{0}\) for a non-zero \(\mathbf{e}\), so \(\mathbf{A}\) is singular: \(\det\mathbf{A} = 0\), since the product of the eigenvalues is the determinant. A negative eigenvalue reverses the direction. The reflection in the line \(y = x\) has matrix \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\), eigenvalues \(1\) (along the mirror, \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\)) and \(-1\) (perpendicular to it, \(\begin{pmatrix} 1 \\ -1 \end{pmatrix}\), which is flipped).

:::eg Find the eigenvalues and eigenvectors of \(\mathbf{A} = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}\).
The trace is 4 and the determinant is \(4 - 4 = 0\), so \(\lambda^2 - 4\lambda = 0\) and the eigenvalues are \(\lambda = 0\) and \(\lambda = 4\).

For \(\lambda = 0\): \(\mathbf{A}\mathbf{e} = \mathbf{0}\) gives \(2x + 4y = 0\), so \(x = -2y\): \(\begin{pmatrix} 2 \\ -1 \end{pmatrix}\).
For \(\lambda = 4\): \(\begin{pmatrix} -2 & 4 \\ 1 & -2 \end{pmatrix}\) gives \(x = 2y\): \(\begin{pmatrix} 2 \\ 1 \end{pmatrix}\).

The eigenvalue 0 matches \(\det\mathbf{A} = 0\): the matrix squashes the whole plane onto the line \(y = \tfrac12 x\). **Check**: \(\mathbf{A}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\).
:::

:::board
For Cambridge 9231, eigenvalues and eigenvectors are tested for 2×2 and 3×3 matrices with **real and distinct** eigenvalues only. A matrix with a repeated eigenvalue (such as a shear) or with complex eigenvalues (such as a rotation) will not be set in a question. You will see them in the widget above, but you do not need to find their eigenvectors.
:::

## Three by three matrices

The method is the same, with a cubic characteristic equation and three eigenvalues. Expand \(\det(\mathbf{A} - \lambda\mathbf{I})\) along the row or column with most zeros, keeping the brackets together as long as you can so that the expression factorises.

For a general \(3 \times 3\) matrix the expansion can be written in terms of three numbers that you can read straight from \(\mathbf{A}\):

:::key The characteristic equation of a 3×3 matrix
\[\lambda^3 - (\operatorname{tr}\mathbf{A})\lambda^2 + c\lambda - \det\mathbf{A} = 0\]
where \(\operatorname{tr}\mathbf{A}\) is the sum of the diagonal entries and \(c\) is the sum of the three \(2 \times 2\) minors obtained by deleting row \(i\) and column \(i\) for \(i = 1, 2, 3\). Note the \(\lambda^3\) term: the expansion of \(\det(\mathbf{A} - \lambda\mathbf{I})\) itself starts with \(-\lambda^3\), so this form has been multiplied by \(-1\).
:::

Because the eigenvalues are the roots of this cubic, [Roots of polynomial equations](#math.fm.roots) says that they add up to \(\operatorname{tr}\mathbf{A}\), their products in pairs add up to \(c\), and their product is \(\det\mathbf{A}\). These three facts check any set of eigenvalues you find.

To solve the cubic, use the factor theorem from [Modulus and polynomials](#math.p3.algebra): try \(\lambda = \pm 1, \pm 2, \dots\) (divisors of \(\det\mathbf{A}\)) until one gives 0, then divide. For eigenvectors, solve \((\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}\). Because the matrix is singular, one equation is redundant: take two independent equations. A fast way is the vector product of two rows of \(\mathbf{A} - \lambda\mathbf{I}\): the eigenvector is perpendicular to both rows, so it is parallel to their vector product.

:::eg (Exam style) The matrix \(\mathbf{A} = \begin{pmatrix} 3 & 2 & 2 \\ 1 & 2 & 0 \\ -1 & -1 & 1 \end{pmatrix}\). (a) Show that the characteristic equation of \(\mathbf{A}\) is \(\lambda^3 - 6\lambda^2 + 11\lambda - 6 = 0\). (b) Find the eigenvalues. (c) Find an eigenvector for each eigenvalue.
**(a)** Expand \(\det(\mathbf{A} - \lambda\mathbf{I})\) along the second row, which has a zero:
\[\begin{vmatrix} 3 - \lambda & 2 & 2 \\ 1 & 2 - \lambda & 0 \\ -1 & -1 & 1 - \lambda \end{vmatrix} = -1\begin{vmatrix} 2 & 2 \\ -1 & 1 - \lambda \end{vmatrix} + (2 - \lambda)\begin{vmatrix} 3 - \lambda & 2 \\ -1 & 1 - \lambda \end{vmatrix}\] [M1]
\[\begin{aligned}
&= -(4 - 2\lambda) + (2 - \lambda)(\lambda^2 - 4\lambda + 5) \\
&= -\lambda^3 + 6\lambda^2 - 11\lambda + 6
\end{aligned}\] [M1] [A1]
Setting this to 0 and multiplying by \(-1\) gives \(\lambda^3 - 6\lambda^2 + 11\lambda - 6 = 0\), as required.
**(b)** \(\lambda = 1\) gives \(1 - 6 + 11 - 6 = 0\), so \((\lambda - 1)\) is a factor. [M1]
\[(\lambda - 1)(\lambda^2 - 5\lambda + 6) = (\lambda - 1)(\lambda - 2)(\lambda - 3)\]
The eigenvalues are 1, 2 and 3. [A1]
**(c)** For \(\lambda = 1\), \(\mathbf{A} - \mathbf{I} = \begin{pmatrix} 2 & 2 & 2 \\ 1 & 1 & 0 \\ -1 & -1 & 0 \end{pmatrix}\). The last two rows give \(x + y = 0\) and the first then gives \(z = 0\). An eigenvector is \(\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}\). [M1] [A1]
For \(\lambda = 2\), \(\mathbf{A} - 2\mathbf{I} = \begin{pmatrix} 1 & 2 & 2 \\ 1 & 0 & 0 \\ -1 & -1 & -1 \end{pmatrix}\). The second row gives \(x = 0\) and then \(y + z = 0\). An eigenvector is \(\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}\). [A1]
For \(\lambda = 3\), \(\mathbf{A} - 3\mathbf{I} = \begin{pmatrix} 0 & 2 & 2 \\ 1 & -1 & 0 \\ -1 & -1 & -2 \end{pmatrix}\). The first row gives \(y = -z\) and the second \(x = y\). An eigenvector is \(\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}\). [A1]

**Check** the cubic with the shortcut: the trace is 6, the three \(2 \times 2\) minors are 2, 5, 4 (sum 11) and \(\det\mathbf{A} = 6\). Check an eigenvector by multiplying: \(\mathbf{A}\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \\ -3 \end{pmatrix}\).
:::

The vector-product method gives the eigenvector for \(\lambda = 2\) in one line: the first two rows of \(\mathbf{A} - 2\mathbf{I}\) are \((1, 2, 2)\) and \((1, 0, 0)\), and
\[\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \times \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 2 \\ -2 \end{pmatrix}\]
which is a multiple of \(\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}\). If the two rows you pick are multiples of each other the vector product is zero: pick a different pair.

:::warn The sign of the cubic term
\(\det(\mathbf{A} - \lambda\mathbf{I})\) starts with \(-\lambda^3\), not \(+\lambda^3\). Setting it equal to 0 and multiplying by \(-1\) gives the same roots. Writing \(\lambda^3 - \operatorname{tr}\mathbf{A}\,\lambda^2 + \dots\) directly is fine, but if you write \(+\operatorname{tr}\mathbf{A}\,\lambda^2\) without flipping the other signs, the trace check fails.
:::

If a \(3 \times 3\) matrix is triangular (all zeros below the diagonal, or all above), its eigenvalues are simply its diagonal entries, because the determinant of \(\mathbf{A} - \lambda\mathbf{I}\) is the product of its diagonal entries \((a_{ii} - \lambda)\).

## Proving properties from the definition

Everything about eigenvectors comes from the single equation \(\mathbf{Ae} = \lambda\mathbf{e}\). Multiplying both sides by \(\mathbf{A}\) again, or by another matrix, produces the rules below. The Further Mathematics papers ask you to prove some of them, so the proofs are examinable and the marks are for the steps.

:::key Eigenvalues of related matrices
If \(\mathbf{Ae} = \lambda\mathbf{e}\) with \(\mathbf{e} \ne \mathbf{0}\), then \(\mathbf{e}\) is also an eigenvector of each matrix below, with the eigenvalue shown:
- \(\mathbf{A}^n\) (\(n\) a positive integer): \(\lambda^n\)
- \(k\mathbf{A}\): \(k\lambda\)
- \(\mathbf{A} + k\mathbf{I}\): \(\lambda + k\)
- \(\mathbf{A}^{-1}\) (when it exists): \(\dfrac{1}{\lambda}\)
- any polynomial in \(\mathbf{A}\), such as \(\mathbf{A}^2 - 3\mathbf{A} + 2\mathbf{I}\): the same polynomial in \(\lambda\), here \(\lambda^2 - 3\lambda + 2\)
:::

:::eg (Exam style) The matrix \(\mathbf{A}\) has eigenvalue \(\lambda\) with eigenvector \(\mathbf{e}\). (a) Show that \(\lambda^2\) is an eigenvalue of \(\mathbf{A}^2\). (b) Prove by induction that \(\lambda^n\) is an eigenvalue of \(\mathbf{A}^n\) for every positive integer \(n\).
**(a)**
\[\mathbf{A}^2\mathbf{e} = \mathbf{A}(\mathbf{Ae}) = \mathbf{A}(\lambda\mathbf{e})\] [M1]
\[= \lambda\mathbf{Ae} = \lambda^2\mathbf{e}\] [A1]
**(b)** The claim is that \(\mathbf{A}^n\mathbf{e} = \lambda^n\mathbf{e}\).
When \(n = 1\) this is \(\mathbf{Ae} = \lambda\mathbf{e}\), which is given, so it is true. [B1]
Assume that it is true for \(n = k\): \(\mathbf{A}^k\mathbf{e} = \lambda^k\mathbf{e}\). [B1]
Then
\[\mathbf{A}^{k+1}\mathbf{e} = \mathbf{A}(\mathbf{A}^k\mathbf{e}) = \mathbf{A}(\lambda^k\mathbf{e})\] [M1]
\[= \lambda^k\mathbf{Ae} = \lambda^{k+1}\mathbf{e}\] [A1]
So it is true for \(n = k + 1\). It is true for \(n = 1\), so by induction it is true for all positive integers \(n\). [A1]
:::

:::eg (Exam style) The square matrix \(\mathbf{A}\) is invertible and has eigenvalue \(\lambda\) with eigenvector \(\mathbf{e}\). (a) Show that \(\lambda \ne 0\) and that \(\dfrac{1}{\lambda}\) is an eigenvalue of \(\mathbf{A}^{-1}\). (b) The eigenvalues of \(\mathbf{A}\) are 2, \(-1\) and 4. Find the eigenvalues of \(\mathbf{A}^{-1} + 3\mathbf{I}\).
**(a)** If \(\lambda = 0\) then \(\mathbf{Ae} = \mathbf{0}\), and multiplying by \(\mathbf{A}^{-1}\) gives \(\mathbf{e} = \mathbf{0}\), which contradicts \(\mathbf{e} \ne \mathbf{0}\). So \(\lambda \ne 0\). [B1]
Multiply \(\mathbf{Ae} = \lambda\mathbf{e}\) on the left by \(\mathbf{A}^{-1}\):
\[\mathbf{A}^{-1}\mathbf{Ae} = \lambda\mathbf{A}^{-1}\mathbf{e}\] [M1]
\[\mathbf{e} = \lambda\mathbf{A}^{-1}\mathbf{e}, \quad \text{so} \quad \mathbf{A}^{-1}\mathbf{e} = \frac{1}{\lambda}\mathbf{e}\] [A1]
**(b)** \(\mathbf{A}^{-1}\) has eigenvalues \(\tfrac12\), \(-1\) and \(\tfrac14\), and adding \(3\mathbf{I}\) adds 3 to each: [M1]
\[\tfrac72, \quad 2, \quad \tfrac{13}{4}\] [A1]
:::

:::warn Eigenvalues of a sum are not the sums of eigenvalues
The rules above work because they are about one matrix, \(\mathbf{A}\), and the same vector \(\mathbf{e}\). The eigenvalues of \(\mathbf{A} + \mathbf{B}\) are generally **not** the eigenvalues of \(\mathbf{A}\) plus those of \(\mathbf{B}\), and the eigenvalues of \(\mathbf{AB}\) are not the products. Use the rules only for powers, multiples, inverses and polynomials of a single matrix.
:::

## Diagonalisation: writing A as QDQ⁻¹

Suppose \(\mathbf{A}\) is a \(2 \times 2\) matrix with eigenvalues \(\lambda_1\), \(\lambda_2\) and eigenvectors \(\mathbf{e}_1\), \(\mathbf{e}_2\). Put the eigenvectors into the columns of a matrix \(\mathbf{Q}\) and the eigenvalues, in the same order, on the diagonal of \(\mathbf{D}\):
\[\mathbf{Q} = \begin{pmatrix} \mathbf{e}_1 & \mathbf{e}_2 \end{pmatrix}, \qquad \mathbf{D} = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}\]
Then
\[\mathbf{AQ} = \begin{pmatrix} \mathbf{Ae}_1 & \mathbf{Ae}_2 \end{pmatrix} = \begin{pmatrix} \lambda_1\mathbf{e}_1 & \lambda_2\mathbf{e}_2 \end{pmatrix} = \mathbf{QD}\]
because multiplying \(\mathbf{Q}\) on the right by \(\mathbf{D}\) scales each column by its eigenvalue. If \(\mathbf{Q}\) has an inverse (it does when the eigenvalues are distinct), multiply on the right by \(\mathbf{Q}^{-1}\).

:::key Diagonalisation
If \(\mathbf{A}\) has distinct real eigenvalues, then
\[\mathbf{A} = \mathbf{QDQ}^{-1}\]
where the columns of \(\mathbf{Q}\) are eigenvectors of \(\mathbf{A}\) and \(\mathbf{D}\) is the diagonal matrix of the eigenvalues, **in the same order as the columns**. Different orders give different valid \(\mathbf{Q}\) and \(\mathbf{D}\) pairs, but a column and its eigenvalue always stay together.
:::

The power of this form is that the middle \(\mathbf{Q}^{-1}\mathbf{Q}\) cancels:
\[\mathbf{A}^2 = \mathbf{QDQ}^{-1}\mathbf{QDQ}^{-1} = \mathbf{QD}^2\mathbf{Q}^{-1}\]
and so on.

:::key Powers of a matrix
\[\mathbf{A}^n = \mathbf{QD}^n\mathbf{Q}^{-1}, \qquad \mathbf{D}^n = \begin{pmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{pmatrix}\]
The same holds for \(3 \times 3\) matrices, with \(\mathbf{D}^n = \operatorname{diag}(\lambda_1^n, \lambda_2^n, \lambda_3^n)\). Powering a diagonal matrix just powers each entry.
:::

:::eg (Exam style) The matrix \(\mathbf{B} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}\) has eigenvalues 2 and 3 with eigenvectors \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\) and \(\begin{pmatrix} 2 \\ 1 \end{pmatrix}\). (a) Write \(\mathbf{B}\) in the form \(\mathbf{QDQ}^{-1}\) and find \(\mathbf{Q}^{-1}\). (b) Show that \(\mathbf{B}^n = \begin{pmatrix} 2 \cdot 3^n - 2^n & 2^{n+1} - 2 \cdot 3^n \\ 3^n - 2^n & 2^{n+1} - 3^n \end{pmatrix}\). (c) Find \(\mathbf{B}^5\).
**(a)** Take the eigenvectors in the order of the eigenvalues 2, 3:
\[\mathbf{Q} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}, \qquad \mathbf{D} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\] [B1] [B1]
\(\det\mathbf{Q} = 1 - 2 = -1\), so
\[\mathbf{Q}^{-1} = \frac{1}{-1}\begin{pmatrix} 1 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}\] [M1] [A1]
**(b)**
\[\mathbf{B}^n = \mathbf{QD}^n\mathbf{Q}^{-1} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 2^n & 0 \\ 0 & 3^n \end{pmatrix}\begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 2^n & 2 \cdot 3^n \\ 2^n & 3^n \end{pmatrix}\begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 2 \cdot 3^n - 2^n & 2^{n+1} - 2 \cdot 3^n \\ 3^n - 2^n & 2^{n+1} - 3^n \end{pmatrix}\] [A1]
**(c)** With \(n = 5\), \(2^5 = 32\) and \(3^5 = 243\):
\[\mathbf{B}^5 = \begin{pmatrix} 454 & -422 \\ 211 & -179 \end{pmatrix}\] [A1]

**Check** with \(n = 1\): \(\begin{pmatrix} 6 - 2 & 4 - 6 \\ 3 - 2 & 4 - 3 \end{pmatrix} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}\), and with \(n = 0\) you get \(\mathbf{I}\).
:::

:::warn Q and D in different orders
The most common error is to list the eigenvalues in \(\mathbf{D}\) in one order and the eigenvectors in \(\mathbf{Q}\) in another. If column 1 of \(\mathbf{Q}\) belongs to \(\lambda = 3\), the first entry of \(\mathbf{D}\) must be 3. Always check by multiplying \(\mathbf{Q}\mathbf{Q}^{-1}\) to confirm \(\mathbf{I}\), and test the first step with \(\mathbf{A}\mathbf{Q} = \mathbf{Q}\mathbf{D}\).
:::

### A real context: population in two towns

:::eg Every year 20% of the people in town \(A\) move to town \(B\), and 30% of the people in \(B\) move to \(A\); nobody else moves. The populations in year \(n\) are \(a_n\) and \(b_n\). Initially \(a_0 = 10000\) and \(b_0 = 40000\). Find \(a_n\) and \(b_n\), and say what happens in the long run.
In matrix form,
\[\begin{pmatrix} a_{n+1} \\ b_{n+1} \end{pmatrix} = \mathbf{M}\begin{pmatrix} a_n \\ b_n \end{pmatrix}, \qquad \mathbf{M} = \frac{1}{10}\begin{pmatrix} 8 & 3 \\ 2 & 7 \end{pmatrix}\]
so \(\begin{pmatrix} a_n \\ b_n \end{pmatrix} = \mathbf{M}^n\begin{pmatrix} 10000 \\ 40000 \end{pmatrix}\).

The trace is \(1.5\) and the determinant is \(\dfrac{56 - 6}{100} = 0.5\), so \(\lambda^2 - 1.5\lambda + 0.5 = 0\), giving \((\lambda - 1)(\lambda - 0.5) = 0\). For \(\lambda = 1\): \(-2x + 3y = 0\), so \(\begin{pmatrix} 3 \\ 2 \end{pmatrix}\). For \(\lambda = 0.5\): \(3x + 3y = 0\), so \(\begin{pmatrix} 1 \\ -1 \end{pmatrix}\).

\[\mathbf{Q} = \begin{pmatrix} 3 & 1 \\ 2 & -1 \end{pmatrix}, \quad \mathbf{D} = \begin{pmatrix} 1 & 0 \\ 0 & \frac12 \end{pmatrix}, \quad \mathbf{Q}^{-1} = \frac15\begin{pmatrix} 1 & 1 \\ 2 & -3 \end{pmatrix}\]
Put \(h = \left(\tfrac12\right)^n\):
\[\mathbf{M}^n = \frac15\begin{pmatrix} 3 & h \\ 2 & -h \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 2 & -3 \end{pmatrix} = \frac15\begin{pmatrix} 3 + 2h & 3 - 3h \\ 2 - 2h & 2 + 3h \end{pmatrix}\]
Then
\[a_n = \frac15\left[(3 + 2h)10000 + (3 - 3h)40000\right] = 30000 - 20000\left(\tfrac12\right)^n\]
and \(b_n = 50000 - a_n = 20000 + 20000\left(\tfrac12\right)^n\).

**Check** \(n = 1\): \(a_1 = 30000 - 10000 = 20000\), and directly \(0.8 \times 10000 + 0.3 \times 40000 = 20000\). As \(n \to \infty\), \(h \to 0\): the populations approach 30000 and 20000, in the ratio \(3 : 2\) of the eigenvector for \(\lambda = 1\). The eigenvalue 1 is the steady state, and the eigenvalue \(\tfrac12\) says how fast the difference fades (it halves every year).
:::

### A 3×3 example

:::eg (Exam style) The matrix \(\mathbf{A} = \begin{pmatrix} 3 & 2 & 2 \\ 1 & 2 & 0 \\ -1 & -1 & 1 \end{pmatrix}\) has eigenvalues 1, 2, 3 with eigenvectors \(\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}\), \(\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}\), \(\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}\) respectively. (a) Write down matrices \(\mathbf{Q}\) and \(\mathbf{D}\) such that \(\mathbf{A} = \mathbf{QDQ}^{-1}\). (b) Find \(\mathbf{Q}^{-1}\). (c) Hence find \(\mathbf{A}^4\).
**(a)**
\[\mathbf{Q} = \begin{pmatrix} 1 & 0 & 1 \\ -1 & 1 & 1 \\ 0 & -1 & -1 \end{pmatrix}, \qquad \mathbf{D} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}\] [B1] [B1]
**(b)** \(\det\mathbf{Q} = 1(-1 + 1) - 0 + 1(1 - 0) = 1\). The matrix of cofactors is
\[\begin{pmatrix} 0 & -1 & 1 \\ -1 & -1 & 1 \\ -1 & -2 & 1 \end{pmatrix}\] [M1]
and transposing and dividing by 1:
\[\mathbf{Q}^{-1} = \begin{pmatrix} 0 & -1 & -1 \\ -1 & -1 & -2 \\ 1 & 1 & 1 \end{pmatrix}\] [A1]
**(c)** \(\mathbf{D}^4 = \operatorname{diag}(1, 16, 81)\), so
\[\mathbf{A}^4 = \mathbf{QD}^4\mathbf{Q}^{-1} = \begin{pmatrix} 1 & 0 & 81 \\ -1 & 16 & 81 \\ 0 & -16 & -81 \end{pmatrix}\begin{pmatrix} 0 & -1 & -1 \\ -1 & -1 & -2 \\ 1 & 1 & 1 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 81 & 80 & 80 \\ 65 & 66 & 50 \\ -65 & -65 & -49 \end{pmatrix}\] [A1]

**Check** that \(\mathbf{QQ}^{-1} = \mathbf{I}\): the first row of \(\mathbf{Q}\) with the first column of \(\mathbf{Q}^{-1}\) is \(1(0) + 0(-1) + 1(1) = 1\), and with the second column \(1(-1) + 0 + 1(1) = 0\). The trace of \(\mathbf{A}^4\) is \(81 + 66 - 49 = 98 = 1 + 16 + 81\).
:::

:::eg Spot the error: the matrix \(\mathbf{B} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}\) has eigenvalue 2 with eigenvector \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\) and eigenvalue 3 with eigenvector \(\begin{pmatrix} 2 \\ 1 \end{pmatrix}\). Write \(\mathbf{B}\) as \(\mathbf{QDQ}^{-1}\) and find \(\mathbf{Q}^{-1}\) (4 marks).
A student wrote this answer.

Line 1: \(\mathbf{Q} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\), \(\mathbf{D} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\)
Line 2: \(\det\mathbf{Q} = 1\), so \(\mathbf{Q}^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}\)

In line 1, the columns of \(\mathbf{Q}\) are valid eigenvectors, in the order \(\lambda = 3\) then \(\lambda = 2\). [B1]

**But \(\mathbf{D}\) lists the eigenvalues in the order 2 then 3, so the columns of \(\mathbf{Q}\) and the entries of \(\mathbf{D}\) do not match.** [B0] The product \(\mathbf{QDQ}^{-1}\) comes out as \(\begin{pmatrix} 1 & 2 \\ -1 & 4 \end{pmatrix}\), not \(\mathbf{B}\). The correct \(\mathbf{D}\) for this \(\mathbf{Q}\) is \(\operatorname{diag}(3, 2)\).

Line 2 is correct for the \(\mathbf{Q}\) the student wrote: the determinant is \(2 - 1 = 1\) and the inverse is right. [M1] [A1] The student scores 3 out of 4.

**Check** with the corrected \(\mathbf{D}\): \(\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 6 & 2 \\ 3 & 2 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}\).
:::

## The Cayley–Hamilton theorem

Replace \(\lambda\) by \(\mathbf{A}\) in the characteristic equation and something remarkable happens: the result is the zero matrix.

:::key Cayley–Hamilton theorem
Every square matrix satisfies its own characteristic equation. If the characteristic equation is \(\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A} = 0\), then
\[\mathbf{A}^2 - (\operatorname{tr}\mathbf{A})\mathbf{A} + (\det\mathbf{A})\mathbf{I} = \mathbf{O}\]
For a \(3 \times 3\) matrix with characteristic equation \(\lambda^3 + p\lambda^2 + q\lambda + r = 0\), \(\mathbf{A}^3 + p\mathbf{A}^2 + q\mathbf{A} + r\mathbf{I} = \mathbf{O}\). The constant term becomes a multiple of \(\mathbf{I}\), because you cannot add a number to a matrix.
:::

:::proof Why it is true for a 2×2 matrix
Let \(\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\). Then
\[\mathbf{A}^2 = \begin{pmatrix} a^2 + bc & b(a + d) \\ c(a + d) & d^2 + bc \end{pmatrix}\]
and \((a + d)\mathbf{A} = \begin{pmatrix} a^2 + ad & b(a + d) \\ c(a + d) & ad + d^2 \end{pmatrix}\).
Subtract: \(\mathbf{A}^2 - (a + d)\mathbf{A} = \begin{pmatrix} bc - ad & 0 \\ 0 & bc - ad \end{pmatrix} = -(ad - bc)\mathbf{I}\).
So \(\mathbf{A}^2 - (a + d)\mathbf{A} + (ad - bc)\mathbf{I} = \mathbf{O}\). The same idea works for any size but the algebra is longer, and the general proof is not required for the examination.
:::

Why is this useful? It lets you write a high power of \(\mathbf{A}\) in terms of lower ones, and an inverse in terms of powers, without finding any eigenvalue.

:::eg The matrix \(\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\) has trace 5 and determinant 4. Use the Cayley–Hamilton theorem to find \(\mathbf{A}^{-1}\) and \(\mathbf{A}^4\).
The characteristic equation is \(\lambda^2 - 5\lambda + 4 = 0\), so
\[\mathbf{A}^2 = 5\mathbf{A} - 4\mathbf{I}\]
**Inverse**: rearrange to \(4\mathbf{I} = 5\mathbf{A} - \mathbf{A}^2 = \mathbf{A}(5\mathbf{I} - \mathbf{A})\), so
\[\mathbf{A}^{-1} = \frac14(5\mathbf{I} - \mathbf{A}) = \frac14\begin{pmatrix} 2 & -1 \\ -2 & 3 \end{pmatrix}\]
**Powers**: multiply by \(\mathbf{A}\) and substitute again.
\[\begin{aligned}
\mathbf{A}^3 &= 5\mathbf{A}^2 - 4\mathbf{A} = 5(5\mathbf{A} - 4\mathbf{I}) - 4\mathbf{A} = 21\mathbf{A} - 20\mathbf{I} \\
\mathbf{A}^4 &= 21\mathbf{A}^2 - 20\mathbf{A} = 21(5\mathbf{A} - 4\mathbf{I}) - 20\mathbf{A} = 85\mathbf{A} - 84\mathbf{I}
\end{aligned}\]
\[\mathbf{A}^4 = \begin{pmatrix} 255 - 84 & 85 \\ 170 & 170 - 84 \end{pmatrix} = \begin{pmatrix} 171 & 85 \\ 170 & 86 \end{pmatrix}\]
**Check** with diagonalisation: the eigenvalues are 1 and 4, so \(\mathbf{A}^4\) has trace \(1 + 256 = 257 = 171 + 86\).
:::

:::eg (Exam style) The matrix \(\mathbf{A} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 3 \end{pmatrix}\). (a) Show that the characteristic equation of \(\mathbf{A}\) is \(\lambda^3 - 6\lambda^2 + 11\lambda - 7 = 0\). (b) Use the Cayley–Hamilton theorem to express \(\mathbf{A}^{-1}\) in terms of \(\mathbf{A}^2\), \(\mathbf{A}\) and \(\mathbf{I}\), and find \(\mathbf{A}^{-1}\). (c) Express \(\mathbf{A}^4\) in the form \(a\mathbf{A}^2 + b\mathbf{A} + c\mathbf{I}\).
**(a)** Expand along the first row:
\[\begin{vmatrix} 1 - \lambda & 1 & 0 \\ 0 & 2 - \lambda & 1 \\ 1 & 0 & 3 - \lambda \end{vmatrix} = (1 - \lambda)\left[(2 - \lambda)(3 - \lambda)\right] - 1\left[0 - 1\right]\] [M1]
\[\begin{aligned}
&= (1 - \lambda)(\lambda^2 - 5\lambda + 6) + 1 \\
&= -\lambda^3 + 6\lambda^2 - 11\lambda + 7
\end{aligned}\] [M1] [A1]
So \(\lambda^3 - 6\lambda^2 + 11\lambda - 7 = 0\).
**(b)** By the theorem, \(\mathbf{A}^3 - 6\mathbf{A}^2 + 11\mathbf{A} - 7\mathbf{I} = \mathbf{O}\). [B1]
Rearrange: \(7\mathbf{I} = \mathbf{A}^3 - 6\mathbf{A}^2 + 11\mathbf{A} = \mathbf{A}(\mathbf{A}^2 - 6\mathbf{A} + 11\mathbf{I})\), so
\[\mathbf{A}^{-1} = \frac17\left(\mathbf{A}^2 - 6\mathbf{A} + 11\mathbf{I}\right)\] [M1]
With \(\mathbf{A}^2 = \begin{pmatrix} 1 & 3 & 1 \\ 1 & 4 & 5 \\ 4 & 1 & 9 \end{pmatrix}\) [A1]:
\[\mathbf{A}^{-1} = \frac17\begin{pmatrix} 6 & -3 & 1 \\ 1 & 3 & -1 \\ -2 & 1 & 2 \end{pmatrix}\] [A1]
**(c)** \(\mathbf{A}^3 = 6\mathbf{A}^2 - 11\mathbf{A} + 7\mathbf{I}\), so
\[\begin{aligned}
\mathbf{A}^4 &= 6\mathbf{A}^3 - 11\mathbf{A}^2 + 7\mathbf{A} \\
&= 6(6\mathbf{A}^2 - 11\mathbf{A} + 7\mathbf{I}) - 11\mathbf{A}^2 + 7\mathbf{A} \\
&= 25\mathbf{A}^2 - 59\mathbf{A} + 42\mathbf{I}
\end{aligned}\] [M1] [A1]

**Check** of (b): the determinant is 7 (from the constant term) and the first row of \(\mathbf{A}\) times the first column of \(\mathbf{A}^{-1}\) is \(\tfrac17(6 + 1) = 1\).
:::

:::exam What MF19 gives you, and the form of the question
MF19 has no formulas for eigenvalues, eigenvectors or Cayley–Hamilton: learn the definition \(\mathbf{Ae} = \lambda\mathbf{e}\), the characteristic equation \(\det(\mathbf{A} - \lambda\mathbf{I}) = 0\) and \(\mathbf{A} = \mathbf{QDQ}^{-1}\). Read the question's form carefully. If it asks for matrices \(\mathbf{P}\) and \(\mathbf{D}\) in a stated form, give exactly that form, with the columns of \(\mathbf{P}\) in the order of the entries of \(\mathbf{D}\). When it says "show that", write the determinant expansion in full, then check the trace, determinant and (for \(3 \times 3\)) the sum of minors against your result. Where you are asked to find a power, the form \(\mathbf{QD}^n\mathbf{Q}^{-1}\) is expected, and unsupported answers from a calculator's matrix mode score no marks.
:::

:::try Start easy, finish at exam standard
Q: Find the eigenvalues of \(\begin{pmatrix} 5 & 4 \\ 1 & 2 \end{pmatrix}\) and an eigenvector for each.
A: Trace 7, determinant 6: \(\lambda^2 - 7\lambda + 6 = 0\), so \(\lambda = 1\) or \(6\). For \(\lambda = 1\): \(4x + 4y = 0\), \(\begin{pmatrix} 1 \\ -1 \end{pmatrix}\). For \(\lambda = 6\): \(-x + 4y = 0\), \(\begin{pmatrix} 4 \\ 1 \end{pmatrix}\).
Q: Show that \(\begin{pmatrix} 3 \\ 1 \end{pmatrix}\) is an eigenvector of \(\begin{pmatrix} 4 & 3 \\ 1 & 2 \end{pmatrix}\) and state the eigenvalue.
A: \(\begin{pmatrix} 4 & 3 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 15 \\ 5 \end{pmatrix} = 5\begin{pmatrix} 3 \\ 1 \end{pmatrix}\), so it is an eigenvector with eigenvalue 5.
Q: The matrix \(\begin{pmatrix} 2 & k \\ 3 & 1 \end{pmatrix}\) has an eigenvalue 4. Find \(k\) and the other eigenvalue.
A: \(\det(\mathbf{A} - 4\mathbf{I}) = (2 - 4)(1 - 4) - 3k = 6 - 3k = 0\), so \(k = 2\). The trace is 3, so the other eigenvalue is \(3 - 4 = -1\). Check: the determinant is \(2 - 6 = -4 = 4 \times (-1)\).
Q: Find the eigenvalues of \(\begin{pmatrix} 2 & 1 & 0 \\ 0 & 3 & 0 \\ 1 & 3 & 1 \end{pmatrix}\), and an eigenvector for the largest.
A: Expand along the second row: \(\det(\mathbf{A} - \lambda\mathbf{I}) = (3 - \lambda)(2 - \lambda)(1 - \lambda)\), so \(\lambda = 1, 2, 3\). For \(\lambda = 3\): \(-x + y = 0\) and \(x + 3y - 2z = 0\), so \(y = x\) and \(z = 2x\): \(\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}\).
Q: The matrix \(\mathbf{A}\) has eigenvalues 2 and \(-3\). Find the eigenvalues of \(\mathbf{A}^2 - 2\mathbf{A} + 3\mathbf{I}\).
A: Apply \(\lambda^2 - 2\lambda + 3\) to each: for 2, \(4 - 4 + 3 = 3\); for \(-3\), \(9 + 6 + 3 = 18\). The eigenvalues are 3 and 18.
Q: The matrix \(\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\) has eigenvalues 1 and 3. Find the eigenvalues of \(\mathbf{A}^{-1}\) and check with the trace of \(\mathbf{A}^{-1}\).
A: The eigenvalues of \(\mathbf{A}^{-1}\) are \(1\) and \(\tfrac13\). Directly, \(\mathbf{A}^{-1} = \tfrac13\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}\), whose trace is \(\tfrac43 = 1 + \tfrac13\).
Q: Write \(\begin{pmatrix} 5 & 4 \\ 1 & 2 \end{pmatrix}\) in the form \(\mathbf{QDQ}^{-1}\) and find its cube.
A: Order the eigenvalues as 6, 1: \(\mathbf{Q} = \begin{pmatrix} 4 & 1 \\ 1 & -1 \end{pmatrix}\), \(\mathbf{D} = \begin{pmatrix} 6 & 0 \\ 0 & 1 \end{pmatrix}\), and \(\mathbf{Q}^{-1} = \dfrac15\begin{pmatrix} 1 & 1 \\ 1 & -4 \end{pmatrix}\). Then \(\mathbf{A}^3 = \mathbf{Q}\operatorname{diag}(216, 1)\mathbf{Q}^{-1} = \dfrac15\begin{pmatrix} 864 + 1 & 864 - 4 \\ 216 - 1 & 216 + 4 \end{pmatrix} = \begin{pmatrix} 173 & 172 \\ 43 & 44 \end{pmatrix}\).
Q: Show that \(\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\) satisfies \(\mathbf{A}^2 = 5\mathbf{A} + 2\mathbf{I}\), and hence find \(\mathbf{A}^{-1}\) and \(\mathbf{A}^3\).
A: \(\mathbf{A}^2 = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix} = \begin{pmatrix} 5 + 2 & 10 \\ 15 & 20 + 2 \end{pmatrix}\). Then \(2\mathbf{I} = \mathbf{A}^2 - 5\mathbf{A} = \mathbf{A}(\mathbf{A} - 5\mathbf{I})\), so \(\mathbf{A}^{-1} = \tfrac12(\mathbf{A} - 5\mathbf{I}) = \begin{pmatrix} -2 & 1 \\ \frac32 & -\frac12 \end{pmatrix}\). And \(\mathbf{A}^3 = 5\mathbf{A}^2 + 2\mathbf{A} = 27\mathbf{A} + 10\mathbf{I} = \begin{pmatrix} 37 & 54 \\ 81 & 118 \end{pmatrix}\).
Q: Write down the eigenvalues of \(\begin{pmatrix} 2 & 7 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & -1 \end{pmatrix}\) and explain how.
A: The matrix is triangular, so \(\det(\mathbf{A} - \lambda\mathbf{I}) = (2 - \lambda)(3 - \lambda)(-1 - \lambda)\) and the eigenvalues are the diagonal entries \(2, 3, -1\).
Q: Show that \(\begin{pmatrix} 2 & -1 \\ -6 & 3 \end{pmatrix}\) has an eigenvalue 0 and find its eigenvectors.
A: The determinant is \(6 - 6 = 0\) and the trace is 5, so \(\lambda^2 - 5\lambda = 0\), \(\lambda = 0\) or \(5\). For \(\lambda = 0\): \(2x - y = 0\), \(\begin{pmatrix} 1 \\ 2 \end{pmatrix}\). For \(\lambda = 5\): \(-3x - y = 0\), \(\begin{pmatrix} 1 \\ -3 \end{pmatrix}\).
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ Find the eigenvalues of \(\mathbf{M} = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix}\) and a corresponding eigenvector for each.
A: \(\det(\mathbf{M} - \lambda\mathbf{I}) = (1 - \lambda)(3 - \lambda) - 8 = 0\) [M1], so \(\lambda^2 - 4\lambda - 5 = 0\). [A1] \((\lambda - 5)(\lambda + 1) = 0\), so \(\lambda = 5\) or \(-1\). [A1]
For \(\lambda = 5\): \(-4x + 4y = 0\), eigenvector \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\). [M1] For \(\lambda = -1\): \(2x + 4y = 0\), eigenvector \(\begin{pmatrix} 2 \\ -1 \end{pmatrix}\). [A1]
Q: [4 marks] ★ The \(3 \times 3\) matrix \(\mathbf{A}\) has eigenvalues 1, 2 and 5. Find \(\operatorname{tr}\mathbf{A}\) and \(\det\mathbf{A}\), and find the eigenvalues of \(\mathbf{A}^2 - \mathbf{A}\).
A: \(\operatorname{tr}\mathbf{A} = 1 + 2 + 5 = 8\). [B1] \(\det\mathbf{A} = 1 \times 2 \times 5 = 10\). [B1]
The eigenvalues of \(\mathbf{A}^2 - \mathbf{A}\) are \(\lambda^2 - \lambda\) [M1]: \(0\), \(2\) and \(20\). [A1]
Q: [5 marks] ★★ The matrix \(\mathbf{A}\) has eigenvalue \(\lambda\) with eigenvector \(\mathbf{e}\). (a) Show that \(\mathbf{e}\) is an eigenvector of \(\mathbf{A}^2 - 4\mathbf{A}\), with eigenvalue \(\lambda^2 - 4\lambda\). (b) Given that \(\mathbf{A} = \begin{pmatrix} 3 & 2 \\ 2 & 0 \end{pmatrix}\), find the eigenvalues of \(\mathbf{A}^2 - 4\mathbf{A}\).
H: Use \(\mathbf{A}^2\mathbf{e} = \lambda^2\mathbf{e}\) from the work on powers.
A: (a) \((\mathbf{A}^2 - 4\mathbf{A})\mathbf{e} = \mathbf{A}^2\mathbf{e} - 4\mathbf{Ae}\) [M1] \(= \lambda^2\mathbf{e} - 4\lambda\mathbf{e} = (\lambda^2 - 4\lambda)\mathbf{e}\). [A1]
(b) \(\lambda^2 - 3\lambda - 4 = 0\) so \(\lambda = 4\) or \(-1\). [M1 A1] The eigenvalues of \(\mathbf{A}^2 - 4\mathbf{A}\) are \(16 - 16 = 0\) and \(1 + 4 = 5\). [A1]
Q: [8 marks] ★★ The matrix \(\mathbf{A} = \begin{pmatrix} 1 & 2 & 2 \\ -3 & 1 & 3 \\ 3 & 2 & 0 \end{pmatrix}\). (a) Show that the characteristic equation is \(\lambda^3 - 2\lambda^2 - 5\lambda + 6 = 0\). (b) Find the eigenvalues. (c) Find an eigenvector for the largest eigenvalue.
H: Expand along the first row and look for the common factor \((1 - \lambda)\).
H: For (c), take the vector product of the first two rows of \(\mathbf{A} - 3\mathbf{I}\).
A: (a) Expand along the first row:
\[\begin{aligned}
\det(\mathbf{A} - \lambda\mathbf{I}) = {} &(1 - \lambda)\left[(1 - \lambda)(-\lambda) - 6\right] \\
&- 2\left[3\lambda - 9\right] + 2\left[-6 - 3(1 - \lambda)\right]
\end{aligned}\] [M1]
The last two terms give \(-6\lambda + 18\) and \(-18 + 6\lambda\), which cancel, so
\[\det(\mathbf{A} - \lambda\mathbf{I}) = (1 - \lambda)(\lambda^2 - \lambda - 6) = -\lambda^3 + 2\lambda^2 + 5\lambda - 6\] [M1] [A1]
and setting this to 0 gives \(\lambda^3 - 2\lambda^2 - 5\lambda + 6 = 0\).
(b) \((1 - \lambda)(\lambda - 3)(\lambda + 2) = 0\) [M1] so \(\lambda = 1\), \(3\) or \(-2\). [A1]
(c) For \(\lambda = 3\), \(\mathbf{A} - 3\mathbf{I} = \begin{pmatrix} -2 & 2 & 2 \\ -3 & -2 & 3 \\ 3 & 2 & -3 \end{pmatrix}\). [M1] The vector product of the first two rows is \(\begin{pmatrix} 10 \\ 0 \\ 10 \end{pmatrix}\) [M1], so an eigenvector is \(\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}\). [A1]
Q: [9 marks] ★★★ The sequence \(a_n\) is defined by \(a_0 = 0\), \(a_1 = 1\) and \(a_{n+2} = 5a_{n+1} - 6a_n\). Let \(\mathbf{M} = \begin{pmatrix} 5 & -6 \\ 1 & 0 \end{pmatrix}\), so that \(\begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix} = \mathbf{M}\begin{pmatrix} a_n \\ a_{n-1} \end{pmatrix}\). (a) Find the eigenvalues and eigenvectors of \(\mathbf{M}\). (b) Write \(\mathbf{M}\) as \(\mathbf{QDQ}^{-1}\). (c) Hence find a formula for \(a_n\).
H: The characteristic equation of \(\mathbf{M}\) is the same as the auxiliary equation of the recurrence.
H: \(\begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix} = \mathbf{M}^n\begin{pmatrix} a_1 \\ a_0 \end{pmatrix} = \mathbf{M}^n\begin{pmatrix} 1 \\ 0 \end{pmatrix}\).
H: Use \(\mathbf{Q}^{-1}\begin{pmatrix} 1 \\ 0 \end{pmatrix}\) first, then multiply by \(\mathbf{D}^n\), then by \(\mathbf{Q}\).
A: (a) \(\det(\mathbf{M} - \lambda\mathbf{I}) = (5 - \lambda)(-\lambda) + 6 = 0\) [M1] so \(\lambda^2 - 5\lambda + 6 = 0\). [A1] \(\lambda = 2\) or \(3\). [A1]
For \(\lambda = 2\): \(3x - 6y = 0\), \(\begin{pmatrix} 2 \\ 1 \end{pmatrix}\). For \(\lambda = 3\): \(2x - 6y = 0\), \(\begin{pmatrix} 3 \\ 1 \end{pmatrix}\). [A1]
(b) Ordering the eigenvalues 3, 2: \(\mathbf{Q} = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}\), \(\mathbf{D} = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}\). [B1] \(\mathbf{Q}^{-1} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}\). [B1]
(c) \(\mathbf{M}^n\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \mathbf{QD}^n\begin{pmatrix} 1 \\ -1 \end{pmatrix}\) [M1] \(= \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 3^n \\ -2^n \end{pmatrix} = \begin{pmatrix} 3^{n+1} - 2^{n+1} \\ 3^n - 2^n \end{pmatrix}\). [A1]
So \(a_n = 3^n - 2^n\). [A1]
Q: [8 marks] (#math.fm.roots) ★★★ The \(3 \times 3\) matrix \(\mathbf{A}\) has characteristic equation \(\lambda^3 - 3\lambda^2 + \lambda + 2 = 0\). (a) Write down \(\operatorname{tr}\mathbf{A}\) and \(\det\mathbf{A}\). (b) Find a cubic equation whose roots are the squares of the eigenvalues of \(\mathbf{A}\), that is the eigenvalues of \(\mathbf{A}^2\). (c) Write down \(\det(\mathbf{A}^2)\) and the sum of the eigenvalues of \(\mathbf{A}^2\).
H: The eigenvalues are the roots \(\alpha, \beta, \gamma\) of the cubic. What does \(\sum\alpha\) say about the trace?
H: For squares, put the odd powers of \(\lambda\) on one side, put \(\lambda = \sqrt{y}\) and square both sides (see [Roots of polynomial equations](#math.fm.roots)).
A: (a) The sum of the roots is 3, so \(\operatorname{tr}\mathbf{A} = 3\). [B1] The product of the roots is \(-2\), so \(\det\mathbf{A} = -2\). [B1]
(b) \(\lambda^3 + \lambda = 3\lambda^2 - 2\), so \(\lambda(\lambda^2 + 1) = 3\lambda^2 - 2\). [M1] With \(\lambda = \sqrt{y}\): \(\sqrt{y}\,(y + 1) = 3y - 2\). Square: [M1]
\[\begin{aligned}
y(y + 1)^2 &= (3y - 2)^2 \\
y^3 + 2y^2 + y &= 9y^2 - 12y + 4 \\
y^3 - 7y^2 + 13y - 4 &= 0
\end{aligned}\] [M1] [A1]
(c) \(\det(\mathbf{A}^2) = 4\) (the product of the new roots). [B1] The sum of the eigenvalues of \(\mathbf{A}^2\) is 7. [B1]
Q: [9 marks] ★★ The matrix \(\mathbf{N} = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 2 \end{pmatrix}\). (a) Show that the characteristic equation of \(\mathbf{N}\) is \(\lambda^3 - 4\lambda^2 + 5\lambda - 4 = 0\). (b) Use the Cayley–Hamilton theorem to find \(\mathbf{N}^{-1}\). (c) Express \(\mathbf{N}^4\) in the form \(a\mathbf{N}^2 + b\mathbf{N} + c\mathbf{I}\).
H: In (b), write \(\mathbf{N}^3 - 4\mathbf{N}^2 + 5\mathbf{N} = 4\mathbf{I}\) and take a factor \(\mathbf{N}\) out of the left side.
A: (a) \(\det(\mathbf{N} - \lambda\mathbf{I}) = (1 - \lambda)\left[(1 - \lambda)(2 - \lambda)\right] - 2\left[0 - 1\right]\) [M1]
\[\begin{aligned}
&= (1 - \lambda)^2(2 - \lambda) + 2 \\
&= -\lambda^3 + 4\lambda^2 - 5\lambda + 4
\end{aligned}\] [M1] [A1]
so the characteristic equation is \(\lambda^3 - 4\lambda^2 + 5\lambda - 4 = 0\).
(b) By the theorem, \(\mathbf{N}^3 - 4\mathbf{N}^2 + 5\mathbf{N} - 4\mathbf{I} = \mathbf{O}\), [B1] so \(4\mathbf{I} = \mathbf{N}(\mathbf{N}^2 - 4\mathbf{N} + 5\mathbf{I})\) and \(\mathbf{N}^{-1} = \tfrac14(\mathbf{N}^2 - 4\mathbf{N} + 5\mathbf{I})\). [M1]
\(\mathbf{N}^2 = \begin{pmatrix} 1 & 4 & 2 \\ 1 & 1 & 3 \\ 3 & 2 & 4 \end{pmatrix}\) [A1] so
\[\mathbf{N}^{-1} = \frac14\begin{pmatrix} 2 & -4 & 2 \\ 1 & 2 & -1 \\ -1 & 2 & 1 \end{pmatrix}\] [A1]
(c) \(\mathbf{N}^4 = 4\mathbf{N}^3 - 5\mathbf{N}^2 + 4\mathbf{N}\), and \(\mathbf{N}^3 = 4\mathbf{N}^2 - 5\mathbf{N} + 4\mathbf{I}\), so
\[\mathbf{N}^4 = 4(4\mathbf{N}^2 - 5\mathbf{N} + 4\mathbf{I}) - 5\mathbf{N}^2 + 4\mathbf{N} = 11\mathbf{N}^2 - 16\mathbf{N} + 16\mathbf{I}\] [M1] [A1]
Q: [9 marks] ★★★ Two tanks, \(A\) and \(B\), are joined by pipes. Each hour 30% of the liquid in \(A\) moves to \(B\) and 10% of the liquid in \(B\) moves to \(A\). The volumes in litres after \(n\) hours are \(a_n\) and \(b_n\), with \(a_0 = 80\) and \(b_0 = 0\). (a) Write \(\begin{pmatrix} a_{n+1} \\ b_{n+1} \end{pmatrix} = \mathbf{M}\begin{pmatrix} a_n \\ b_n \end{pmatrix}\) and show that the eigenvalues of \(\mathbf{M}\) are 1 and \(0.6\), with eigenvectors \(\begin{pmatrix} 1 \\ 3 \end{pmatrix}\) and \(\begin{pmatrix} 1 \\ -1 \end{pmatrix}\). (b) Find \(\mathbf{M}^n\). (c) Find \(a_n\) and \(b_n\), and the volumes in the long run.
H: The first column of \(\mathbf{M}\) is what happens to the liquid in \(A\): 70% stays and 30% moves.
H: Take \(\mathbf{Q} = \begin{pmatrix} 1 & 1 \\ 3 & -1 \end{pmatrix}\) and \(\mathbf{D} = \operatorname{diag}(1, 0.6)\); then \(\mathbf{Q}^{-1} = \dfrac14\begin{pmatrix} 1 & 1 \\ 3 & -1 \end{pmatrix}\).
A: (a) \(\mathbf{M} = \begin{pmatrix} 0.7 & 0.1 \\ 0.3 & 0.9 \end{pmatrix}\). [B1] The trace is \(1.6\) and the determinant is \(0.63 - 0.03 = 0.6\), so \(\lambda^2 - 1.6\lambda + 0.6 = 0\) [M1], \((\lambda - 1)(\lambda - 0.6) = 0\). [A1] For \(\lambda = 1\): \(-0.3x + 0.1y = 0\), \(\begin{pmatrix} 1 \\ 3 \end{pmatrix}\); for \(\lambda = 0.6\): \(0.1x + 0.1y = 0\), \(\begin{pmatrix} 1 \\ -1 \end{pmatrix}\). [A1]
(b) With \(h = 0.6^n\): \(\mathbf{M}^n = \mathbf{QD}^n\mathbf{Q}^{-1} = \dfrac14\begin{pmatrix} 1 & h \\ 3 & -h \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 3 & -1 \end{pmatrix}\) [M1] \(= \dfrac14\begin{pmatrix} 1 + 3h & 1 - h \\ 3 - 3h & 3 + h \end{pmatrix}\). [A1]
(c) \(a_n = \dfrac{80(1 + 3h)}{4} = 20 + 60(0.6)^n\) [M1] and \(b_n = 60 - 60(0.6)^n\). [A1] As \(n \to \infty\), \(a_n \to 20\) and \(b_n \to 60\) litres. [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Suppose that \(\mathbf{A}\) has two different eigenvalues \(\lambda_1 \ne \lambda_2\), with eigenvectors \(\mathbf{e}_1\) and \(\mathbf{e}_2\). Prove that \(\mathbf{e}_2\) is not a multiple of \(\mathbf{e}_1\). (This is why \(\mathbf{Q}\) has an inverse when the eigenvalues are distinct.)
H: Suppose \(\mathbf{e}_2 = k\mathbf{e}_1\) and apply \(\mathbf{A}\) to both sides.
H: You get two expressions for \(\mathbf{Ae}_2\). What does subtracting them give?
A: Suppose \(\mathbf{e}_2 = k\mathbf{e}_1\) for some number \(k\); \(k \ne 0\) since \(\mathbf{e}_2 \ne \mathbf{0}\). [B1]
Apply \(\mathbf{A}\): \(\mathbf{Ae}_2 = k\mathbf{Ae}_1 = k\lambda_1\mathbf{e}_1 = \lambda_1\mathbf{e}_2\). [M1] [A1]
But also \(\mathbf{Ae}_2 = \lambda_2\mathbf{e}_2\), so \((\lambda_1 - \lambda_2)\mathbf{e}_2 = \mathbf{0}\). [M1]
Since \(\lambda_1 \ne \lambda_2\) this forces \(\mathbf{e}_2 = \mathbf{0}\), a contradiction. So \(\mathbf{e}_2\) is not a multiple of \(\mathbf{e}_1\). [A1]
Q: [8 marks] ★★★ The Fibonacci numbers are \(F_0 = 0\), \(F_1 = 1\), \(F_{n+1} = F_n + F_{n-1}\). Let \(\mathbf{M} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\), so that \(\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \mathbf{M}\begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}\). (a) Show that the eigenvalues of \(\mathbf{M}\) are \(\varphi = \dfrac{1 + \sqrt5}{2}\) and \(\psi = \dfrac{1 - \sqrt5}{2}\), and that \(\begin{pmatrix} \varphi \\ 1 \end{pmatrix}\) and \(\begin{pmatrix} \psi \\ 1 \end{pmatrix}\) are corresponding eigenvectors. (b) Hence show that \(F_n = \dfrac{\varphi^n - \psi^n}{\sqrt5}\).
H: The characteristic equation is \(\lambda^2 - \lambda - 1 = 0\); note that \(\varphi^2 = \varphi + 1\) and \(\psi^2 = \psi + 1\).
H: \(\mathbf{M}^n\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \mathbf{QD}^n\mathbf{Q}^{-1}\begin{pmatrix} 1 \\ 0 \end{pmatrix}\), and \(\det\mathbf{Q} = \varphi - \psi = \sqrt5\).
A: (a) \(\lambda^2 - \lambda - 1 = 0\) [M1], so \(\lambda = \dfrac{1 \pm \sqrt5}{2}\). [A1]
\(\mathbf{M}\begin{pmatrix} \varphi \\ 1 \end{pmatrix} = \begin{pmatrix} \varphi + 1 \\ \varphi \end{pmatrix} = \begin{pmatrix} \varphi^2 \\ \varphi \end{pmatrix} = \varphi\begin{pmatrix} \varphi \\ 1 \end{pmatrix}\), and the same for \(\psi\). [A1]
(b) \(\mathbf{Q} = \begin{pmatrix} \varphi & \psi \\ 1 & 1 \end{pmatrix}\), \(\det\mathbf{Q} = \varphi - \psi = \sqrt5\), \(\mathbf{Q}^{-1} = \dfrac{1}{\sqrt5}\begin{pmatrix} 1 & -\psi \\ -1 & \varphi \end{pmatrix}\). [B1]
\[\mathbf{M}^n\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \mathbf{Q}\begin{pmatrix} \varphi^n & 0 \\ 0 & \psi^n \end{pmatrix}\frac{1}{\sqrt5}\begin{pmatrix} 1 \\ -1 \end{pmatrix}\] [M1]
\[= \frac{1}{\sqrt5}\begin{pmatrix} \varphi^{n+1} - \psi^{n+1} \\ \varphi^n - \psi^n \end{pmatrix}\] [A1]
The second row is \(F_n\), so \(F_n = \dfrac{\varphi^n - \psi^n}{\sqrt5}\). [A1] [A1]
:::

:::quiz
? What does it mean to say that \(\lambda\) is an eigenvalue of the matrix \(\mathbf{A}\)?
- \(\mathbf{Ae} = \lambda\) for some vector \(\mathbf{e}\)
+ \(\mathbf{Ae} = \lambda\mathbf{e}\) for some non-zero vector \(\mathbf{e}\)
- \(\det\mathbf{A} = \lambda\)
- \(\mathbf{Ae} = \lambda\mathbf{e}\) for every vector \(\mathbf{e}\)
> The equation must be between vectors, and the eigenvector must be non-zero, since \(\mathbf{A0} = \lambda\mathbf{0}\) holds for any \(\lambda\). The relation need only hold for special vectors, not for every vector.
? The characteristic equation of \(\begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}\) is
+ \(\lambda^2 - 6\lambda + 5 = 0\)
- \(\lambda^2 + 6\lambda + 5 = 0\)
- \(\lambda^2 - 6\lambda + 11 = 0\)
- \(\lambda^2 - 6\lambda - 5 = 0\)
> The trace is 6 and the determinant is \(8 - 3 = 5\), so \(\lambda^2 - 6\lambda + 5 = 0\). The sign of the middle term is minus the trace; the constant is the determinant (not \(8 + 3\)).
? The eigenvalues of a \(3 \times 3\) matrix are 2, 3 and 4. What is its determinant?
- 9
+ 24
- 14
- 1
> The determinant is the product of the eigenvalues, \(2 \times 3 \times 4 = 24\). The sum, 9, is the trace.
? The invertible matrix \(\mathbf{A}\) has eigenvalue 5. An eigenvalue of \(\mathbf{A}^{-1}\) is
- \(-5\)
- 5
+ \(\dfrac15\)
- \(\dfrac{1}{25}\)
> \(\mathbf{Ae} = 5\mathbf{e}\) gives \(\mathbf{e} = 5\mathbf{A}^{-1}\mathbf{e}\), so \(\mathbf{A}^{-1}\mathbf{e} = \tfrac15\mathbf{e}\). The inverse takes the reciprocal, not the negative.
? In \(\mathbf{A} = \mathbf{QDQ}^{-1}\), column 2 of \(\mathbf{Q}\) is an eigenvector. Which entry of \(\mathbf{D}\) is its eigenvalue?
- the entry in row 1, column 2
- the entry in row 1, column 1
+ the entry in row 2, column 2
- any entry: the order does not matter
> \(\mathbf{D}\) is diagonal and its second diagonal entry goes with the second column of \(\mathbf{Q}\). The order matters: columns and diagonal entries must be paired.
? A matrix satisfies \(\mathbf{A}^2 - 5\mathbf{A} + 4\mathbf{I} = \mathbf{O}\). Which is correct?
- \(\mathbf{A}^{-1} = 5\mathbf{I} - \mathbf{A}\)
+ \(\mathbf{A}^{-1} = \tfrac14(5\mathbf{I} - \mathbf{A})\)
- \(\mathbf{A}^{-1} = \tfrac14(\mathbf{A} - 5\mathbf{I})\)
- \(\mathbf{A}^{-1} = \mathbf{A}^2 - 5\mathbf{A}\)
> Write \(4\mathbf{I} = 5\mathbf{A} - \mathbf{A}^2 = \mathbf{A}(5\mathbf{I} - \mathbf{A})\) and divide by 4. Dropping the 4 is the common slip; the sign comes from moving \(\mathbf{A}^2\) across.
? \(\mathbf{e}\) is an eigenvector of \(\mathbf{A}\). Which of these is also an eigenvector of \(\mathbf{A}\) with the same eigenvalue?
+ \(-3\mathbf{e}\)
- \(\mathbf{e} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}\)
- \(\mathbf{0}\)
- \(\mathbf{e}^2\)
> Any non-zero multiple of an eigenvector is an eigenvector with the same eigenvalue. Adding a different vector breaks the property, and the zero vector is never an eigenvector.
:::

:::checklist What you can now do
- [ ] I can state what a characteristic equation, an eigenvalue and an eigenvector are, and use \(\mathbf{Ae} = \lambda\mathbf{e}\).
- [ ] I can find the eigenvalues and eigenvectors of a \(2 \times 2\) matrix and check them with the trace and determinant.
- [ ] I can find the characteristic cubic of a \(3 \times 3\) matrix, solve it, and find an eigenvector for each eigenvalue.
- [ ] I can prove from \(\mathbf{Ae} = \lambda\mathbf{e}\) that \(\lambda^n\) is an eigenvalue of \(\mathbf{A}^n\), and find the eigenvalues of \(\mathbf{A}^{-1}\), \(k\mathbf{A}\) and polynomials in \(\mathbf{A}\).
- [ ] I can write a matrix as \(\mathbf{QDQ}^{-1}\), keeping the columns of \(\mathbf{Q}\) in the order of the entries of \(\mathbf{D}\).
- [ ] I can use \(\mathbf{A}^n = \mathbf{QD}^n\mathbf{Q}^{-1}\) to find powers of \(2 \times 2\) and \(3 \times 3\) matrices.
- [ ] I can use the Cayley–Hamilton theorem to find \(\mathbf{A}^{-1}\) and higher powers of a matrix.
:::

:::recap
- \(\mathbf{Ae} = \lambda\mathbf{e}\) with \(\mathbf{e} \ne \mathbf{0}\): \(\lambda\) is an eigenvalue, \(\mathbf{e}\) an eigenvector; any non-zero multiple of \(\mathbf{e}\) works too.
- Characteristic equation: \(\det(\mathbf{A} - \lambda\mathbf{I}) = 0\). For \(2 \times 2\): \(\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A} = 0\). For \(3 \times 3\): \(\lambda^3 - (\operatorname{tr}\mathbf{A})\lambda^2 + c\lambda - \det\mathbf{A} = 0\), with \(c\) the sum of the three diagonal \(2 \times 2\) minors.
- The eigenvalues add to the trace and multiply to the determinant.
- Eigenvectors: solve \((\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}\); for \(3 \times 3\), use two independent rows and their vector product.
- If \(\mathbf{Ae} = \lambda\mathbf{e}\): \(\mathbf{A}^n\mathbf{e} = \lambda^n\mathbf{e}\), \(\mathbf{A}^{-1}\mathbf{e} = \lambda^{-1}\mathbf{e}\), \((\mathbf{A} + k\mathbf{I})\mathbf{e} = (\lambda + k)\mathbf{e}\); proofs are examinable.
- \(\mathbf{A} = \mathbf{QDQ}^{-1}\) with eigenvectors in the columns of \(\mathbf{Q}\) and the eigenvalues in the same order on the diagonal of \(\mathbf{D}\); \(\mathbf{A}^n = \mathbf{QD}^n\mathbf{Q}^{-1}\).
- Cayley–Hamilton: \(\mathbf{A}\) satisfies its characteristic equation, with the constant replaced by a multiple of \(\mathbf{I}\). Use it for \(\mathbf{A}^{-1}\) and for powers.
- 9231 uses real, distinct eigenvalues only.
:::

:::links
- watch: [Eigenvalues and eigenvectors](https://www.examsolutions.net/tutorials/eigenvalues-and-eigenvectors/) · ExamSolutions · the characteristic equation and eigenvectors, step by step
- watch: [Eigenvectors and eigenvalues](https://www.3blue1brown.com/lessons/eigenvalues) · 3Blue1Brown · the geometric picture of vectors that are only stretched
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · graded questions with answers on eigenvalues, diagonalisation and Cayley–Hamilton
- practise: [Linear algebra](https://www.khanacademy.org/math/linear-algebra) · Khan Academy · eigenvalues and eigenvectors with exercises
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot a matrix acting on a point and watch the invariant directions
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [First order differential equations](#math.fm.de) solves equations that link a function to its derivative, using integrating factors and substitutions.

