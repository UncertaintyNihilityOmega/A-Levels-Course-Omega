@chapter math.fm.matrices
@title Matrices: algebra, determinants and inverses
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary A matrix is a rectangle of numbers that can be added, scaled and multiplied by clear rules. You will learn those rules for matrices of up to three rows and columns, find determinants and decide when a matrix is singular, build the inverse of a 2×2 and a 3×3 matrix, use \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\), and solve matrix equations and simultaneous equations with an inverse.

:::why
A matrix packs a whole set of linear equations, or a geometric transformation, into one object, and then lets you do algebra on it. Two chapters later you will see that a 2×2 matrix is a transformation of the plane, and in the Paper 2 chapters you will use matrices to solve three equations in three unknowns and to find eigenvalues. Everything there rests on the rules in this chapter: how to multiply, what a determinant tells you, and how to undo a matrix.
:::

**Before you start**, you need to solve simultaneous equations and rearrange formulae ([Algebra from scratch](#math.f.algebra)), to solve quadratics and use the discriminant ([Quadratics](#math.p1.quadratics)), and to factorise cubics with the factor theorem ([Modulus and polynomials](#math.p3.algebra)). Nothing in 9709 teaches matrices, so this chapter starts from zero.

:::try Warm-up
Q: Solve the simultaneous equations \(2x + 3y = 12\) and \(x - y = 1\). (from [Algebra from scratch](#math.f.algebra))
A: From the second, \(x = 1 + y\). Then \(2 + 2y + 3y = 12\), so \(y = 2\) and \(x = 3\).
Q: Find the values of \(k\) for which \(x^2 + kx + 9 = 0\) has equal roots. (from [Quadratics](#math.p1.quadratics))
A: The discriminant is zero: \(k^2 - 36 = 0\), so \(k = 6\) or \(k = -6\).
Q: Solve \(k^3 - 7k + 6 = 0\). (from [Modulus and polynomials](#math.p3.algebra))
A: \(k = 1\) is a root, so \((k - 1)\) is a factor: \(k^3 - 7k + 6 = (k - 1)(k^2 + k - 6) = (k - 1)(k - 2)(k + 3)\). The roots are 1, 2 and \(-3\).
:::

## What a matrix is

A **matrix** is a rectangular array of numbers in brackets. The plural is matrices. Here are three:
\[\mathbf{A} = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix} \qquad \mathbf{B} = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix} \qquad \mathbf{c} = \begin{pmatrix} 5 \\ -2 \\ 7 \end{pmatrix}\]
Matrices are named with bold capital letters. The syllabus uses matrices with at most three rows and three columns.

:::def Order of a matrix
A matrix with \(m\) rows and \(n\) columns has order \(m \times n\) ("\(m\) by \(n\)"). Rows come first. A matrix with the same number of rows and columns is **square**. The numbers inside are its **entries** (or elements).
:::

In the three matrices above, \(\mathbf{A}\) is \(2 \times 2\), \(\mathbf{B}\) is \(2 \times 3\) and \(\mathbf{c}\) is \(3 \times 1\) (a column). Rows are counted downwards and columns across, so the entry in row 2, column 3 of \(\mathbf{B}\) is 1.

:::def Equal matrices
Two matrices are equal when they have the same order and every pair of matching entries is equal.
:::

### Adding, subtracting and scaling

You add or subtract matrices of the same order by adding or subtracting matching entries. A matrix of one order can never be added to a matrix of another order. To multiply a matrix by a number (a **scalar**), multiply every entry.

:::key Addition and scalar multiples
For matrices of the same order, \((\mathbf{A} + \mathbf{B})_{ij} = A_{ij} + B_{ij}\) and \((k\mathbf{A})_{ij} = kA_{ij}\). Both obey the usual rules of algebra: \(\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}\), \(k(\mathbf{A} + \mathbf{B}) = k\mathbf{A} + k\mathbf{B}\).
:::

:::eg Given \(\mathbf{A} = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 0 & 5 \\ -2 & 1 \end{pmatrix}\), find \(\mathbf{A} + \mathbf{B}\), \(\mathbf{A} - \mathbf{B}\) and \(3\mathbf{A} - 2\mathbf{B}\).
Work entry by entry.
\[\mathbf{A} + \mathbf{B} = \begin{pmatrix} 2 + 0 & -1 + 5 \\ 3 - 2 & 4 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 1 & 5 \end{pmatrix}\]
\[\mathbf{A} - \mathbf{B} = \begin{pmatrix} 2 - 0 & -1 - 5 \\ 3 + 2 & 4 - 1 \end{pmatrix} = \begin{pmatrix} 2 & -6 \\ 5 & 3 \end{pmatrix}\]
For \(3\mathbf{A} - 2\mathbf{B}\), scale first and then subtract:
\[3\mathbf{A} - 2\mathbf{B} = \begin{pmatrix} 6 & -3 \\ 9 & 12 \end{pmatrix} - \begin{pmatrix} 0 & 10 \\ -4 & 2 \end{pmatrix} = \begin{pmatrix} 6 & -13 \\ 13 & 10 \end{pmatrix}\]
:::

Two matrices play the roles that 0 and 1 play for numbers.

:::def Zero matrix and identity matrix
The **zero matrix** \(\mathbf{O}\) has every entry 0 (of any order); \(\mathbf{A} + \mathbf{O} = \mathbf{A}\). The **identity matrix** \(\mathbf{I}\) is square, with 1 on the leading diagonal (top left to bottom right) and 0 everywhere else:
\[\mathbf{I}_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \qquad \mathbf{I}_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\]
Multiplying by \(\mathbf{I}\) changes nothing: \(\mathbf{A}\mathbf{I} = \mathbf{I}\mathbf{A} = \mathbf{A}\). The identity is also called the unit matrix.
:::

## Multiplying matrices

Multiplication is the operation with the real content. It looks odd at first, but it is built so that a matrix can stand for "do this to a vector", and so that doing one matrix after another is a product (the next chapter shows why).

:::def Product of two matrices
If \(\mathbf{A}\) is \(m \times n\) and \(\mathbf{B}\) is \(n \times p\), the product \(\mathbf{AB}\) is the \(m \times p\) matrix whose entry in row \(i\), column \(j\) is
\[(\mathbf{AB})_{ij} = A_{i1}B_{1j} + A_{i2}B_{2j} + \dots + A_{in}B_{nj}\]
that is, row \(i\) of \(\mathbf{A}\) multiplied term by term with column \(j\) of \(\mathbf{B}\) and added.
:::

:::key When does the product exist?
\(\mathbf{AB}\) exists only if the number of **columns** of \(\mathbf{A}\) equals the number of **rows** of \(\mathbf{B}\). Then the order of the product is (rows of \(\mathbf{A}\)) \(\times\) (columns of \(\mathbf{B}\)):
\[(m \times n)(n \times p) \longrightarrow m \times p\]
The two inner numbers must match and they disappear; the outer numbers give the order of the answer.
:::

:::eg Find \(\mathbf{AB}\), where \(\mathbf{A} = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix}\). Explain why \(\mathbf{BA}\) does not exist.
\(\mathbf{A}\) is \(2 \times 2\) and \(\mathbf{B}\) is \(2 \times 3\). The inner numbers match (2 and 2), so \(\mathbf{AB}\) exists and is \(2 \times 3\).

Row 1 of \(\mathbf{A}\) is \((2, -1)\). Multiply it with each column of \(\mathbf{B}\) in turn:
\[\begin{aligned}
\text{column 1: } & 2(1) + (-1)(-1) = 3 \\
\text{column 2: } & 2(0) + (-1)(3) = -3 \\
\text{column 3: } & 2(2) + (-1)(1) = 3
\end{aligned}\]
Row 2 of \(\mathbf{A}\) is \((3, 4)\):
\[\begin{aligned}
\text{column 1: } & 3(1) + 4(-1) = -1 \\
\text{column 2: } & 3(0) + 4(3) = 12 \\
\text{column 3: } & 3(2) + 4(1) = 10
\end{aligned}\]
\[\mathbf{AB} = \begin{pmatrix} 3 & -3 & 3 \\ -1 & 12 & 10 \end{pmatrix}\]
For \(\mathbf{BA}\) we would need the columns of \(\mathbf{B}\) (3) to equal the rows of \(\mathbf{A}\) (2). They do not, so \(\mathbf{BA}\) does not exist.
:::

A quick way to keep track: put a finger on row \(i\) of the left matrix and another on column \(j\) of the right matrix, multiply the pairs you touch and add.

:::eg With \(\mathbf{C} = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix}\) and \(\mathbf{D} = \begin{pmatrix} 1 & 2 \\ 0 & -1 \\ 3 & 1 \end{pmatrix}\), find \(\mathbf{CD}\) and \(\mathbf{DC}\), and state their orders.
\(\mathbf{C}\) is \(2 \times 3\) and \(\mathbf{D}\) is \(3 \times 2\). Both products exist, but they are different sizes: \(\mathbf{CD}\) is \(2 \times 2\) and \(\mathbf{DC}\) is \(3 \times 3\).
\[\mathbf{CD} = \begin{pmatrix} 1 + 0 + 6 & 2 + 0 + 2 \\ -1 + 0 + 3 & -2 - 3 + 1 \end{pmatrix} = \begin{pmatrix} 7 & 4 \\ 2 & -4 \end{pmatrix}\]
For \(\mathbf{DC}\), each row of \(\mathbf{D}\) meets each column of \(\mathbf{C}\):
\[\mathbf{DC} = \begin{pmatrix} 1 - 2 & 0 + 6 & 2 + 2 \\ 0 + 1 & 0 - 3 & 0 - 1 \\ 3 - 1 & 0 + 3 & 6 + 1 \end{pmatrix} = \begin{pmatrix} -1 & 6 & 4 \\ 1 & -3 & -1 \\ 2 & 3 & 7 \end{pmatrix}\]
:::

### The rules of multiplication

Multiplication of numbers obeys \(ab = ba\). Matrices do not.

:::key Rules for matrix products
Whenever the products are defined:
- \((\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})\) (associative), so you can write \(\mathbf{ABC}\);
- \(\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{AB} + \mathbf{AC}\) and \((\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{AC} + \mathbf{BC}\) (distributive);
- \(\mathbf{AI} = \mathbf{IA} = \mathbf{A}\);
- **in general \(\mathbf{AB} \ne \mathbf{BA}\)**: matrix multiplication is not commutative.
Powers are repeated products of a square matrix: \(\mathbf{A}^2 = \mathbf{AA}\), \(\mathbf{A}^3 = \mathbf{AAA}\), and \(\mathbf{A}^0 = \mathbf{I}\).
:::

One counterexample is enough to show that \(\mathbf{AB} \ne \mathbf{BA}\).

:::eg Show that \(\mathbf{AB} \ne \mathbf{BA}\) for \(\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 3 & 0 \\ 1 & 1 \end{pmatrix}\).
\[\mathbf{AB} = \begin{pmatrix} 3 + 2 & 0 + 2 \\ 0 + 1 & 0 + 1 \end{pmatrix} = \begin{pmatrix} 5 & 2 \\ 1 & 1 \end{pmatrix}\]
\[\mathbf{BA} = \begin{pmatrix} 3 + 0 & 6 + 0 \\ 1 + 0 & 2 + 1 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 1 & 3 \end{pmatrix}\]
The two results differ, so \(\mathbf{AB} \ne \mathbf{BA}\).
:::

The lack of commutativity has consequences you will meet again and again. \((\mathbf{A} + \mathbf{B})^2 = \mathbf{A}^2 + \mathbf{AB} + \mathbf{BA} + \mathbf{B}^2\), which is not \(\mathbf{A}^2 + 2\mathbf{AB} + \mathbf{B}^2\). And \(\mathbf{AB} = \mathbf{O}\) does not mean that \(\mathbf{A}\) or \(\mathbf{B}\) is the zero matrix.

:::eg For the same \(\mathbf{A}\) and \(\mathbf{B}\), find \((\mathbf{A} + \mathbf{B})^2\) in two ways, and show that \(\mathbf{A}^2 + 2\mathbf{AB} + \mathbf{B}^2\) is a different matrix.
\(\mathbf{A} + \mathbf{B} = \begin{pmatrix} 4 & 2 \\ 1 & 2 \end{pmatrix}\), so
\[(\mathbf{A} + \mathbf{B})^2 = \begin{pmatrix} 16 + 2 & 8 + 4 \\ 4 + 2 & 2 + 4 \end{pmatrix} = \begin{pmatrix} 18 & 12 \\ 6 & 6 \end{pmatrix}\]
Now the expansion. \(\mathbf{A}^2 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}\) and \(\mathbf{B}^2 = \begin{pmatrix} 9 & 0 \\ 4 & 1 \end{pmatrix}\), with \(\mathbf{AB}\) and \(\mathbf{BA}\) from above:
\[\mathbf{A}^2 + \mathbf{AB} + \mathbf{BA} + \mathbf{B}^2 = \begin{pmatrix} 1 + 5 + 3 + 9 & 4 + 2 + 6 + 0 \\ 0 + 1 + 1 + 4 & 1 + 1 + 3 + 1 \end{pmatrix} = \begin{pmatrix} 18 & 12 \\ 6 & 6 \end{pmatrix}\]
which agrees. The wrong expansion gives \(\mathbf{A}^2 + 2\mathbf{AB} + \mathbf{B}^2 = \begin{pmatrix} 20 & 8 \\ 6 & 4 \end{pmatrix}\), which does not.
:::

Matrix products also organise real data. In this example the rule "columns of the left matrix equal rows of the right" is what makes the answer meaningful: each shop's sales row is combined with each price column.

:::eg Three shops sell two kinds of loaf. The weekly sales are in the matrix \(\mathbf{S}\), with one row per shop and the columns for white and wholemeal loaves. The matrix \(\mathbf{P}\) gives the selling price and the cost to make each loaf, in pounds, with a row per kind of loaf:
\[\mathbf{S} = \begin{pmatrix} 40 & 25 \\ 30 & 50 \\ 20 & 10 \end{pmatrix} \qquad \mathbf{P} = \begin{pmatrix} 4.50 & 3.00 \\ 6.00 & 4.00 \end{pmatrix}\]
Find \(\mathbf{SP}\), say what its entries mean, and find each shop's weekly profit.
\(\mathbf{S}\) is \(3 \times 2\) and \(\mathbf{P}\) is \(2 \times 2\), so \(\mathbf{SP}\) is \(3 \times 2\).
\[\mathbf{SP} = \begin{pmatrix} 40(4.5) + 25(6) & 40(3) + 25(4) \\ 30(4.5) + 50(6) & 30(3) + 50(4) \\ 20(4.5) + 10(6) & 20(3) + 10(4) \end{pmatrix} = \begin{pmatrix} 330 & 220 \\ 435 & 290 \\ 150 & 100 \end{pmatrix}\]
Row \(i\) is shop \(i\): the first column is its weekly takings and the second is its weekly cost, both in pounds. Profit is takings minus cost: \(330 - 220 = 110\), \(435 - 290 = 145\) and \(150 - 100 = 50\), that is £110, £145 and £50.
:::

:::warn Order matters
\(\mathbf{AB}\) means "\(\mathbf{A}\) on the left, \(\mathbf{B}\) on the right", and the order in which you write a product is part of the answer. When you simplify, never swap the factors, and when you multiply both sides of an equation by a matrix, put it on the same side on both sides.
:::

A matrix can satisfy an equation of its own, which is a favourite exam idea because it lets you write a power in terms of lower ones.

:::eg (Exam style) The matrix \(\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}\). (a) Find \(\mathbf{A}^2\). (b) Find constants \(p\) and \(q\) such that \(\mathbf{A}^2 = p\mathbf{A} + q\mathbf{I}\). (c) Hence find \(\mathbf{A}^{-1}\).
**(a)**
\[\mathbf{A}^2 = \begin{pmatrix} 4 + 1 & 2 + 3 \\ 2 + 3 & 1 + 9 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 5 & 5 \\ 5 & 10 \end{pmatrix}\] [A1]
**(b)** Compare with \(p\mathbf{A} + q\mathbf{I} = \begin{pmatrix} 2p + q & p \\ p & 3p + q \end{pmatrix}\). The off-diagonal entries give \(p = 5\), and then \(2p + q = 5\) gives \(q = -5\). [M1]
Check the last entry: \(3(5) - 5 = 10\). So \(\mathbf{A}^2 = 5\mathbf{A} - 5\mathbf{I}\). [A1]
**(c)** Rearrange: \(\mathbf{A}^2 - 5\mathbf{A} = -5\mathbf{I}\), so \(\mathbf{A}(\mathbf{A} - 5\mathbf{I}) = -5\mathbf{I}\). [M1]
Divide by \(-5\):
\[\mathbf{A}^{-1} = -\tfrac15(\mathbf{A} - 5\mathbf{I}) = -\tfrac15\begin{pmatrix} -3 & 1 \\ 1 & -2 \end{pmatrix} = \tfrac15\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\] [A1]
**Check**: the first row of \(\mathbf{A}\) times the first column of \(\tfrac15\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\) is \(\tfrac15(6 - 1) = 1\), as it should be.
:::

The method in (c) is the key. \(\mathbf{A}^{-1}\) is the matrix that cancels \(\mathbf{A}\); you meet it properly in a moment. Notice how the same equation also gives higher powers: \(\mathbf{A}^3 = \mathbf{A}\mathbf{A}^2 = 5\mathbf{A}^2 - 5\mathbf{A} = 20\mathbf{A} - 25\mathbf{I}\).

## Determinants and singular matrices

Every square matrix has a number attached to it that says whether it can be undone. For a 2×2 matrix it is simple.

:::def Determinant of a 2×2 matrix
For \(\mathbf{M} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\), the determinant is
\[\det \mathbf{M} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc\]
:::

The determinant of a product is the product of the determinants: \(\det(\mathbf{AB}) = \det \mathbf{A} \times \det \mathbf{B}\). You can use this fact without proving it; the next chapter gives it a geometric meaning.

:::def Singular and non-singular
A square matrix \(\mathbf{M}\) is **singular** if \(\det \mathbf{M} = 0\), and **non-singular** if \(\det \mathbf{M} \ne 0\). A singular matrix has no inverse.
:::

:::eg Find \(\det \mathbf{N}\) for \(\mathbf{N} = \begin{pmatrix} 3 & -2 \\ 4 & 5 \end{pmatrix}\). Show that \(\begin{pmatrix} 6 & 9 \\ 2 & 3 \end{pmatrix}\) is singular. Find the values of \(k\) for which \(\begin{pmatrix} k & 4 \\ 3 & k + 1 \end{pmatrix}\) is singular.
\[\det \mathbf{N} = 3 \times 5 - (-2) \times 4 = 15 + 8 = 23\]
For the second matrix, \(6 \times 3 - 9 \times 2 = 18 - 18 = 0\), so it is singular.

For the third, set the determinant to zero:
\[\begin{aligned}
k(k + 1) - 4 \times 3 &= 0 \\
k^2 + k - 12 &= 0 \\
(k + 4)(k - 3) &= 0
\end{aligned}\]
The matrix is singular for \(k = -4\) and \(k = 3\).
:::

### The inverse of a 2×2 matrix

:::def Inverse matrix
The **inverse** of a square matrix \(\mathbf{M}\), written \(\mathbf{M}^{-1}\), is the matrix with
\[\mathbf{M}\mathbf{M}^{-1} = \mathbf{M}^{-1}\mathbf{M} = \mathbf{I}\]
It exists exactly when \(\mathbf{M}\) is non-singular, and then it is unique.
:::

:::key Inverse of a 2×2 matrix
\[\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\]
"Swap the diagonal entries, change the signs of the other two, divide by the determinant."
:::

You can see why it works by multiplying out: \(\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad - bc & 0 \\ 0 & ad - bc \end{pmatrix} = (ad - bc)\mathbf{I}\). Dividing by \(ad - bc\) gives \(\mathbf{I}\), which is possible only when \(ad - bc \ne 0\).

:::eg Find the inverse of \(\mathbf{N} = \begin{pmatrix} 3 & -2 \\ 4 & 5 \end{pmatrix}\), and check it.
\(\det \mathbf{N} = 23\). Swap 3 and 5, change the signs of \(-2\) and 4:
\[\mathbf{N}^{-1} = \frac{1}{23}\begin{pmatrix} 5 & 2 \\ -4 & 3 \end{pmatrix}\]
**Check**:
\[\mathbf{N}\mathbf{N}^{-1} = \frac{1}{23}\begin{pmatrix} 15 + 8 & 6 - 6 \\ 20 - 20 & 8 + 15 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\]
:::

The top-left entry is \(3(5) + (-2)(-4) = 23\): the product of two negatives is easy to get wrong, and the check catches it at once.

## 3×3 determinants

For a 3×3 matrix you reduce to 2×2 determinants by expanding along a row.

:::def Minor and cofactor
In a 3×3 matrix, the **minor** of an entry is the determinant of the 2×2 matrix left when you delete the row and column containing that entry. The **cofactor** is the minor with a sign: \(+\) or \(-\) according to the position in the chessboard pattern
\[\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}\]
The entry in row \(i\), column \(j\) has sign \((-1)^{i + j}\).
:::

:::key Determinant of a 3×3 matrix
Expand along the first row: multiply each entry by its cofactor and add. For \(\mathbf{M} = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}\),
\[\det \mathbf{M} = a\begin{vmatrix} e & f \\ h & i \end{vmatrix} - b\begin{vmatrix} d & f \\ g & i \end{vmatrix} + c\begin{vmatrix} d & e \\ g & h \end{vmatrix}\]
\[= a(ei - fh) - b(di - fg) + c(dh - eg)\]
You may expand along any row or any column, using the signs of the chessboard pattern: the answer is the same. Choose the row or column with the most zeros.
:::

:::eg Find the determinant of \(\mathbf{E} = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 1 \\ 1 & 2 & 5 \end{pmatrix}\).
Expand along the first row. The signs are \(+ - +\).
\[\begin{aligned}
\det \mathbf{E} &= 2\begin{vmatrix} 4 & 1 \\ 2 & 5 \end{vmatrix} - 1\begin{vmatrix} 0 & 1 \\ 1 & 5 \end{vmatrix} + 3\begin{vmatrix} 0 & 4 \\ 1 & 2 \end{vmatrix} \\
&= 2(20 - 2) - 1(0 - 1) + 3(0 - 4) \\
&= 36 + 1 - 12 = 25
\end{aligned}\]
Take care with the middle term: it has a minus sign in front and the minor is \(-1\), so the term is \(+1\).
:::

:::eg Find the determinant of \(\mathbf{F} = \begin{pmatrix} 3 & 0 & 2 \\ 1 & 4 & 0 \\ 5 & 0 & 1 \end{pmatrix}\).
Column 2 has two zeros, so expand down it. The only non-zero entry is 4, in row 2, column 2, whose sign is \(+\). Delete row 2 and column 2:
\[\det \mathbf{F} = 4\begin{vmatrix} 3 & 2 \\ 5 & 1 \end{vmatrix} = 4(3 - 10) = -28\]
:::

Row and column expansion is the same idea; you only change which entries you multiply and which signs go with them. If you are unsure, expand along the first row as well and compare.

:::warn Scaling a matrix scales the determinant by \(k^n\)
For an \(n \times n\) matrix, \(\det(k\mathbf{A}) = k^n \det \mathbf{A}\), because every one of the \(n\) rows is multiplied by \(k\). For the matrix \(\mathbf{E}\) above, \(\det(2\mathbf{E}) = 2^3 \times 25 = 200\), not 50. For a 2×2 matrix, \(\det(3\mathbf{N}) = 9 \times 23\).
:::

## The inverse of a 3×3 matrix

The 2×2 rule is a special case of a general method: write down the cofactors, transpose, divide by the determinant.

:::def Transpose
The **transpose** \(\mathbf{M}^{T}\) of a matrix is found by writing its rows as columns. If \(\mathbf{M}\) is \(m \times n\), then \(\mathbf{M}^{T}\) is \(n \times m\).
:::

:::steps
1. Find \(\det \mathbf{M}\). If it is 0, stop: there is no inverse.
2. Find the nine minors (delete a row and a column, take the 2×2 determinant).
3. Apply the chessboard signs \(+ - + / - + - / + - +\) to get the **matrix of cofactors**.
4. **Transpose** it. The result is called the adjugate.
5. Divide every entry by \(\det \mathbf{M}\).
:::

:::key Inverse of a 3×3 matrix
\[\mathbf{M}^{-1} = \frac{1}{\det \mathbf{M}}\,(\text{matrix of cofactors})^{T}\]
:::

:::eg Find the inverse of \(\mathbf{G} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 2 \end{pmatrix}\).
**Determinant.** Expand along row 1:
\[\det \mathbf{G} = 1(2 - 0) - 1(0 - 1) + 0 = 2 + 1 = 3\]
The determinant is not 0, so the inverse exists.

**Minors.** Delete the row and column of each entry in turn:
\[\begin{aligned}
&\text{row 1: } \begin{vmatrix} 1 & 1 \\ 0 & 2 \end{vmatrix} = 2, \quad \begin{vmatrix} 0 & 1 \\ 1 & 2 \end{vmatrix} = -1, \quad \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} = -1 \\
&\text{row 2: } \begin{vmatrix} 1 & 0 \\ 0 & 2 \end{vmatrix} = 2, \quad \begin{vmatrix} 1 & 0 \\ 1 & 2 \end{vmatrix} = 2, \quad \begin{vmatrix} 1 & 1 \\ 1 & 0 \end{vmatrix} = -1 \\
&\text{row 3: } \begin{vmatrix} 1 & 0 \\ 1 & 1 \end{vmatrix} = 1, \quad \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} = 1, \quad \begin{vmatrix} 1 & 1 \\ 0 & 1 \end{vmatrix} = 1
\end{aligned}\]
**Cofactors.** Apply the signs \(+ - + / - + - / + - +\):
\[\begin{pmatrix} 2 & -(-1) & -1 \\ -2 & 2 & -(-1) \\ 1 & -1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 & -1 \\ -2 & 2 & 1 \\ 1 & -1 & 1 \end{pmatrix}\]
**Transpose, then divide by 3:**
\[\mathbf{G}^{-1} = \frac13\begin{pmatrix} 2 & -2 & 1 \\ 1 & 2 & -1 \\ -1 & 1 & 1 \end{pmatrix}\]
**Check** that \(\mathbf{G}\mathbf{G}^{-1} = \mathbf{I}\):
\[\mathbf{G}\mathbf{G}^{-1} = \frac13\begin{pmatrix} 2 + 1 + 0 & -2 + 2 + 0 & 1 - 1 + 0 \\ 0 + 1 - 1 & 0 + 2 + 1 & 0 - 1 + 1 \\ 2 + 0 - 2 & -2 + 0 + 2 & 1 + 0 + 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\]
:::

:::tip A cheap check on the cofactors
The first row of \(\mathbf{G}\) times the first column of the adjugate is \(1(2) + 1(1) + 0(-1) = 3\), which is \(\det \mathbf{G}\). In general each row of \(\mathbf{M}\) multiplied by the matching row of cofactors (the same pairing as in the determinant expansion) gives \(\det \mathbf{M}\), and multiplying by a different row of cofactors gives 0. Use this to catch a wrong sign before you finish.
:::

:::warn Where the marks go in a 3×3 inverse
There are three places to slip: a cofactor sign, forgetting to transpose, and forgetting to divide by the determinant. Because \(\mathbf{G}\) here is not symmetric, leaving out the transpose gives a different, wrong matrix. If your answer fails the check \(\mathbf{M}\mathbf{M}^{-1} = \mathbf{I}\), look at these three first.
:::

### Unknown constants

Exam questions often put an unknown \(k\) in a matrix and ask when it is singular, or for the inverse "in terms of \(k\)".

:::eg (Exam style) The matrix \(\mathbf{M} = \begin{pmatrix} 1 & k & 0 \\ 2 & 1 & -1 \\ 0 & 3 & k \end{pmatrix}\). Find the values of \(k\) for which \(\mathbf{M}\) is singular.
Expand along the first row. The third entry is 0, so that term vanishes.
\[\det \mathbf{M} = 1(k + 3) - k(2k - 0) + 0\] [M1]
\[= -2k^2 + k + 3\] [A1]
\(\mathbf{M}\) is singular when \(\det \mathbf{M} = 0\):
\[\begin{aligned}
2k^2 - k - 3 &= 0 \\
(2k - 3)(k + 1) &= 0
\end{aligned}\] [M1]
So \(k = \tfrac32\) or \(k = -1\). [A1]
:::

:::eg (Exam style) Find the inverse of \(\mathbf{P} = \begin{pmatrix} 2 & k \\ 3 & 5 \end{pmatrix}\) in terms of \(k\), and state the value of \(k\) for which it does not exist.
\[\det \mathbf{P} = 10 - 3k\] [B1]
\[\mathbf{P}^{-1} = \frac{1}{10 - 3k}\begin{pmatrix} 5 & -k \\ -3 & 2 \end{pmatrix}\] [M1 A1]
This exists unless \(10 - 3k = 0\), so \(\mathbf{P}\) has no inverse when \(k = \tfrac{10}{3}\). [B1]
:::

## The inverse of a product

If you put on your socks and then your shoes, you undo that by taking off your shoes first and then your socks. Inverses of products work the same way.

:::key Inverse of a product
If \(\mathbf{A}\) and \(\mathbf{B}\) are non-singular, so is \(\mathbf{AB}\), and
\[(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\]
For three matrices, \((\mathbf{ABC})^{-1} = \mathbf{C}^{-1}\mathbf{B}^{-1}\mathbf{A}^{-1}\): reverse the order and invert each.
:::

:::proof Why the order reverses
Multiply \(\mathbf{AB}\) by the proposed inverse:
\[\begin{aligned}
(\mathbf{AB})(\mathbf{B}^{-1}\mathbf{A}^{-1}) &= \mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1} \\
&= \mathbf{A}\mathbf{I}\mathbf{A}^{-1} \\
&= \mathbf{A}\mathbf{A}^{-1} = \mathbf{I}
\end{aligned}\]
The first step uses associativity, the second that \(\mathbf{B}\mathbf{B}^{-1} = \mathbf{I}\), and the last that \(\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}\). The product is \(\mathbf{I}\), so \(\mathbf{B}^{-1}\mathbf{A}^{-1}\) is the inverse of \(\mathbf{AB}\) (and the same working in the other order shows \(\mathbf{B}^{-1}\mathbf{A}^{-1}\mathbf{AB} = \mathbf{I}\)).
:::

:::eg (Exam style) The matrices \(\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}\). Find \(\mathbf{A}^{-1}\), \(\mathbf{B}^{-1}\) and \((\mathbf{AB})^{-1}\), and verify your answer by finding \(\mathbf{AB}\) and its inverse directly.
\(\det \mathbf{A} = 6 - 5 = 1\) and \(\det \mathbf{B} = 3 - 2 = 1\).
\[\mathbf{A}^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} \qquad \mathbf{B}^{-1} = \begin{pmatrix} 3 & -2 \\ -1 & 1 \end{pmatrix}\] [B1]
Reverse the order for the product:
\[(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1} = \begin{pmatrix} 3 & -2 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\] [M1]
\[= \begin{pmatrix} 9 + 10 & -3 - 4 \\ -3 - 5 & 1 + 2 \end{pmatrix} = \begin{pmatrix} 19 & -7 \\ -8 & 3 \end{pmatrix}\] [A1]
**Verify**: \(\mathbf{AB} = \begin{pmatrix} 3 & 7 \\ 8 & 19 \end{pmatrix}\), whose determinant is \(57 - 56 = 1\), so its inverse is \(\begin{pmatrix} 19 & -7 \\ -8 & 3 \end{pmatrix}\), as found. [B1]
:::

The wrong order, \(\mathbf{A}^{-1}\mathbf{B}^{-1}\), gives \(\begin{pmatrix} 10 & -7 \\ -17 & 12 \end{pmatrix}\), a different matrix. The order is not a matter of taste.

## Matrix equations and simultaneous equations

An equation with an unknown matrix is solved by multiplying by an inverse, and **the side you multiply on matters**.

:::key Solving matrix equations
- If \(\mathbf{AX} = \mathbf{B}\), multiply on the **left** by \(\mathbf{A}^{-1}\): \(\mathbf{X} = \mathbf{A}^{-1}\mathbf{B}\).
- If \(\mathbf{XA} = \mathbf{B}\), multiply on the **right** by \(\mathbf{A}^{-1}\): \(\mathbf{X} = \mathbf{B}\mathbf{A}^{-1}\).
\(\mathbf{A}^{-1}\mathbf{B}\) and \(\mathbf{B}\mathbf{A}^{-1}\) are usually different matrices. Write the step \(\mathbf{A}^{-1}\mathbf{AX} = \mathbf{A}^{-1}\mathbf{B}\) so that the inverse is on the same side of both sides.
:::

:::eg With \(\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 1 & 4 \\ 0 & -1 \end{pmatrix}\), solve (a) \(\mathbf{AX} = \mathbf{B}\), (b) \(\mathbf{XA} = \mathbf{B}\).
From before, \(\mathbf{A}^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\).

(a) Multiply on the left by \(\mathbf{A}^{-1}\):
\[\mathbf{X} = \mathbf{A}^{-1}\mathbf{B} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\begin{pmatrix} 1 & 4 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 3 & 13 \\ -5 & -22 \end{pmatrix}\]
(b) Multiply on the right by \(\mathbf{A}^{-1}\):
\[\mathbf{X} = \mathbf{B}\mathbf{A}^{-1} = \begin{pmatrix} 1 & 4 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} -17 & 7 \\ 5 & -2 \end{pmatrix}\]
The two answers are different. **Check** (a): the first row of \(\mathbf{A}\) times the first column of \(\mathbf{X}\) is \(2(3) + 1(-5) = 1\), which is the top-left entry of \(\mathbf{B}\).
:::

### Simultaneous equations

Simultaneous equations are a matrix equation \(\mathbf{Mx} = \mathbf{b}\): the rows of \(\mathbf{M}\) hold the coefficients, \(\mathbf{x}\) is the column of unknowns and \(\mathbf{b}\) the column of right-hand sides. If \(\mathbf{M}\) is non-singular, \(\mathbf{x} = \mathbf{M}^{-1}\mathbf{b}\). The case where \(\mathbf{M}\) is singular, where there may be no solution or infinitely many, is treated geometrically in [Three equations, three planes](#math.fm.systems).

:::eg Use the inverse of \(\mathbf{N} = \begin{pmatrix} 3 & -2 \\ 4 & 5 \end{pmatrix}\) to solve \(3x - 2y = 5\), \(4x + 5y = -1\).
In matrix form, \(\begin{pmatrix} 3 & -2 \\ 4 & 5 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \end{pmatrix}\). Using \(\mathbf{N}^{-1}\) from earlier:
\[\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{23}\begin{pmatrix} 5 & 2 \\ -4 & 3 \end{pmatrix}\begin{pmatrix} 5 \\ -1 \end{pmatrix} = \frac{1}{23}\begin{pmatrix} 25 - 2 \\ -20 - 3 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}\]
So \(x = 1\) and \(y = -1\). **Check**: \(3(1) - 2(-1) = 5\) and \(4(1) + 5(-1) = -1\).
:::

:::eg Use \(\mathbf{G}^{-1}\) from above to solve \(x + y = 3\), \(y + z = 5\), \(x + 2z = 7\).
The coefficient matrix is \(\mathbf{G}\) and the right-hand side is \(\begin{pmatrix} 3 \\ 5 \\ 7 \end{pmatrix}\):
\[\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \frac13\begin{pmatrix} 2 & -2 & 1 \\ 1 & 2 & -1 \\ -1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 5 \\ 7 \end{pmatrix} = \frac13\begin{pmatrix} 6 - 10 + 7 \\ 3 + 10 - 7 \\ -3 + 5 + 7 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\]
**Check** in the third equation: \(1 + 2(3) = 7\).
:::

:::board
Edexcel Further Mathematics (9FM0) Core Pure also teaches matrices of up to 3×3, with determinants, inverses and the rule \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\) in the same notation, so the algebra of this chapter carries over; the 9231 syllabus restricts matrices to at most three rows and three columns.
:::

:::exam What the paper gives you
MF19 contains no formulae for matrices: learn the 2×2 inverse, the 3×3 expansion and the cofactor method. A calculator with a matrix mode may be used to check, but the paper says no marks are given for unsupported answers from a calculator, so show the working (the determinant expansion, the cofactors, the product) the way this chapter does. Give inverses with the factor \(\dfrac{1}{\det}\) outside, as exact fractions. Questions say "find the values of \(k\) for which \(\mathbf{M}\) is singular" or "find \(\mathbf{M}^{-1}\) in terms of \(k\)": set \(\det \mathbf{M} = 0\), and write the inverse with \(\dfrac{1}{\det \mathbf{M}}\) in front.
:::

:::eg Spot the error: for the matrix \(\mathbf{N} = \begin{pmatrix} 1 & 2 & k \\ 3 & 1 & 0 \\ 2 & k & 1 \end{pmatrix}\), find the values of \(k\) for which \(\mathbf{N}\) is singular (4 marks).
A student wrote this answer.

Line 1: \(\det \mathbf{N} = 1(1 - 0) - 2(3 - 0) + k(3k - 2)\)
Line 2: \(= 1 - 6 + k(3k + 2) = 3k^2 + 2k - 5\)
Line 3: \(3k^2 + 2k - 5 = 0\), so \((3k + 5)(k - 1) = 0\) and \(k = 1\) or \(k = -\tfrac53\)

Line 1 is a correct first-row expansion. [M1]

**Line 2 has an arithmetic slip, so the accuracy mark is lost.** [A0] The minor of the third entry is \(3 \times k - 1 \times 2 = 3k - 2\) (as line 1 shows), but the student wrote \(+2\) when multiplying out, so the determinant should be \(3k^2 - 2k - 5\).

Line 3 sets the determinant to 0 and solves the quadratic correctly from the wrong determinant, so the method mark and the follow-through accuracy mark are earned. [M1] [A1] (FT) The student scores 3 out of 4.

Correct line 3: \(3k^2 - 2k - 5 = (3k - 5)(k + 1) = 0\), so \(k = -1\) or \(k = \tfrac53\). **Check** \(k = -1\): \(\det = 1(1) - 2(3) + (-1)(-3 - 2) = 1 - 6 + 5 = 0\).
:::

:::try Start easy, finish at exam standard
Q: Given \(\mathbf{A} = \begin{pmatrix} 4 & 0 \\ -1 & 2 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 1 & 3 \\ 2 & -2 \end{pmatrix}\), find \(2\mathbf{A} + 3\mathbf{B}\).
A: \(\begin{pmatrix} 8 & 0 \\ -2 & 4 \end{pmatrix} + \begin{pmatrix} 3 & 9 \\ 6 & -6 \end{pmatrix} = \begin{pmatrix} 11 & 9 \\ 4 & -2 \end{pmatrix}\).
Q: For the same \(\mathbf{A}\) and \(\mathbf{B}\), find \(\mathbf{AB}\) and \(\mathbf{BA}\).
A: \(\mathbf{AB} = \begin{pmatrix} 4 & 12 \\ -1 + 4 & -3 - 4 \end{pmatrix} = \begin{pmatrix} 4 & 12 \\ 3 & -7 \end{pmatrix}\). \(\mathbf{BA} = \begin{pmatrix} 4 - 3 & 6 \\ 8 + 2 & -4 \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 10 & -4 \end{pmatrix}\). They differ.
Q: A matrix \(\mathbf{P}\) is \(3 \times 2\) and \(\mathbf{Q}\) is \(2 \times 4\). State the order of \(\mathbf{PQ}\), and say whether \(\mathbf{QP}\) exists.
A: \(\mathbf{PQ}\) is \(3 \times 4\). \(\mathbf{QP}\) would need the 4 columns of \(\mathbf{Q}\) to equal the 3 rows of \(\mathbf{P}\), so it does not exist.
Q: Find \(\det \begin{pmatrix} 7 & -3 \\ 2 & 5 \end{pmatrix}\) and the inverse of the matrix.
A: \(\det = 35 + 6 = 41\). The inverse is \(\dfrac{1}{41}\begin{pmatrix} 5 & 3 \\ -2 & 7 \end{pmatrix}\).
Q: Find the values of \(k\) for which \(\begin{pmatrix} k & 3 \\ 12 & k + 1 \end{pmatrix}\) is singular.
A: \(k(k + 1) - 36 = 0\), so \(k^2 + k - 36 = 0\) and \(k = \dfrac{-1 \pm \sqrt{145}}{2}\).
Q: Find \(\det \begin{pmatrix} 1 & 3 & 0 \\ 2 & -1 & 4 \\ 0 & 5 & 2 \end{pmatrix}\).
A: Expand along row 1: \(1(-2 - 20) - 3(4 - 0) + 0 = -22 - 12 = -34\).
Q: A \(3 \times 3\) matrix \(\mathbf{M}\) has \(\det \mathbf{M} = 4\). Find \(\det(3\mathbf{M})\) and \(\det(\mathbf{M}^2)\).
A: \(\det(3\mathbf{M}) = 3^3 \times 4 = 108\). \(\det(\mathbf{M}^2) = 4 \times 4 = 16\).
Q: Find the inverse of \(\mathbf{M} = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}\).
A: \(\det \mathbf{M} = 2(1 - 0) - 0 + 1(1 - 0) = 3\). The cofactors are \(\begin{pmatrix} 1 & -1 & 1 \\ 1 & 2 & -2 \\ -1 & 1 & 2 \end{pmatrix}\), so \(\mathbf{M}^{-1} = \dfrac13\begin{pmatrix} 1 & 1 & -1 \\ -1 & 2 & 1 \\ 1 & -2 & 2 \end{pmatrix}\).
Q: Given \(\mathbf{A}^{-1} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}\) and \(\mathbf{B}^{-1} = \begin{pmatrix} 1 & 0 \\ 4 & 1 \end{pmatrix}\), find \((\mathbf{AB})^{-1}\).
A: \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1} = \begin{pmatrix} 1 & 0 \\ 4 & 1 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 11 & 6 \end{pmatrix}\).
Q: Solve \(\begin{pmatrix} 2 & 1 \\ 7 & 4 \end{pmatrix}\mathbf{X} = \begin{pmatrix} 3 & 1 \\ 10 & 2 \end{pmatrix}\).
A: \(\det = 8 - 7 = 1\), so the inverse of the left matrix is \(\begin{pmatrix} 4 & -1 \\ -7 & 2 \end{pmatrix}\), and \(\mathbf{X} = \begin{pmatrix} 4 & -1 \\ -7 & 2 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ 10 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ -1 & -3 \end{pmatrix}\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Given \(\mathbf{P} = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 1 & 4 \end{pmatrix}\) and \(\mathbf{Q} = \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ 5 & 3 \end{pmatrix}\), find \(\mathbf{PQ}\) and state the order of \(\mathbf{QP}\).
A: \(\mathbf{PQ} = \begin{pmatrix} 2 + 0 + 0 & 1 + 2 + 0 \\ 6 + 0 + 20 & 3 - 1 + 12 \end{pmatrix}\) [M1] \(= \begin{pmatrix} 2 & 3 \\ 26 & 14 \end{pmatrix}\). [A1]
\(\mathbf{QP}\) is \(3 \times 3\). [B1]
Q: [3 marks] ★ Find the values of \(k\) for which \(\begin{pmatrix} k & 6 \\ 1 & k - 5 \end{pmatrix}\) is singular.
A: \(\det = k(k - 5) - 6\) [M1] \(= k^2 - 5k - 6\). Setting this to zero, \((k - 6)(k + 1) = 0\), [A1] so \(k = 6\) or \(k = -1\). [A1]
Q: [5 marks] ★★ The matrix \(\mathbf{M} = \begin{pmatrix} 4 & -3 \\ 2 & -1 \end{pmatrix}\). Find \(\mathbf{M}^{-1}\), and hence solve \(4x - 3y = 5\), \(2x - y = 3\).
A: \(\det \mathbf{M} = -4 + 6 = 2\). [B1] \(\mathbf{M}^{-1} = \dfrac12\begin{pmatrix} -1 & 3 \\ -2 & 4 \end{pmatrix}\). [M1 A1]
\(\begin{pmatrix} x \\ y \end{pmatrix} = \dfrac12\begin{pmatrix} -1 & 3 \\ -2 & 4 \end{pmatrix}\begin{pmatrix} 5 \\ 3 \end{pmatrix} = \dfrac12\begin{pmatrix} 4 \\ 2 \end{pmatrix}\) [M1] so \(x = 2\), \(y = 1\). [A1]
Q: [5 marks] ★★ The non-singular matrices \(\mathbf{A}\) and \(\mathbf{B}\) have \(\mathbf{A}^{-1} = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix}\) and \(\mathbf{B}^{-1} = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix}\). (a) Find \((\mathbf{AB})^{-1}\). (b) Find \(\mathbf{A}\).
A: (a) \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\) [M1] \(= \begin{pmatrix} 2 - 3 & 4 - 5 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ 1 & 2 \end{pmatrix}\). [A1]
(b) \(\det \mathbf{A}^{-1} = 5 - 6 = -1\). [M1] \(\mathbf{A} = (\mathbf{A}^{-1})^{-1} = \dfrac{1}{-1}\begin{pmatrix} 5 & -2 \\ -3 & 1 \end{pmatrix}\) [A1] \(= \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}\). [A1]
Q: [4 marks] ★★ Given \(\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}\) and \(\mathbf{B} = \begin{pmatrix} 1 & 0 \\ 4 & -1 \end{pmatrix}\), find the matrix \(\mathbf{X}\) such that \(\mathbf{XA} = \mathbf{B}\).
A: \(\det \mathbf{A} = 1\) and \(\mathbf{A}^{-1} = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}\). [B1]
Multiply on the right: \(\mathbf{X} = \mathbf{B}\mathbf{A}^{-1}\). [M1]
\(\mathbf{X} = \begin{pmatrix} 1 & 0 \\ 4 & -1 \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}\) [M1] \(= \begin{pmatrix} 2 & -1 \\ 13 & -7 \end{pmatrix}\). [A1]
Q: [5 marks] ★★ The matrix \(\mathbf{M} = \begin{pmatrix} 2 & 1 & k \\ 1 & 0 & 1 \\ 3 & k & 1 \end{pmatrix}\). Show that \(\mathbf{M}\) is non-singular for every real value of \(k\).
A: Expanding along row 1, \(\det \mathbf{M} = 2(0 - k) - 1(1 - 3) + k(k - 0)\) [M1] \(= k^2 - 2k + 2\). [A1]
Complete the square: \(\det \mathbf{M} = (k - 1)^2 + 1\) [M1] and this is at least 1 for every real \(k\). [A1]
(Alternatively the discriminant is \((-2)^2 - 4(1)(2) = -4 < 0\).) So \(\det \mathbf{M} \ne 0\) and \(\mathbf{M}\) is non-singular for all real \(k\). [B1]
Q: [11 marks] (#math.p3.algebra) ★★★ The matrix \(\mathbf{M} = \begin{pmatrix} k & 1 & 1 \\ 1 & k & 1 \\ 1 & 1 & k \end{pmatrix}\). (a) Show that \(\det \mathbf{M} = k^3 - 3k + 2\). (b) Find the values of \(k\) for which \(\mathbf{M}\) is singular. (c) Given that \(k = 2\), find \(\mathbf{M}^{-1}\).
H: In (b), check that \(k = 1\) is a root, then use the factor theorem to divide.
H: When \(k = 2\) every entry on the leading diagonal has cofactor \(2^2 - 1 = 3\); work out one off-diagonal cofactor and notice the symmetry.
H: Check your inverse by multiplying the first row of \(\mathbf{M}\) by the first column of your answer.
A: (a) \(\det \mathbf{M} = k(k^2 - 1) - 1(k - 1) + 1(1 - k)\) [M1 A1] \(= k^3 - k - 2k + 2 = k^3 - 3k + 2\). [A1]
(b) \(k = 1\) gives \(1 - 3 + 2 = 0\), so \((k - 1)\) is a factor. [B1]
\(k^3 - 3k + 2 = (k - 1)(k^2 + k - 2)\) [M1] \(= (k - 1)^2(k + 2)\). [A1]
\(\mathbf{M}\) is singular for \(k = 1\) and \(k = -2\). [A1]
(c) With \(k = 2\), \(\det \mathbf{M} = 1^2 \times 4 = 4\). [B1] The cofactor matrix is \(\begin{pmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{pmatrix}\). [M1 A1] It is symmetric, so the transpose is the same, and
\(\mathbf{M}^{-1} = \dfrac14\begin{pmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{pmatrix}\). [A1]
Q: [8 marks] ★★★ The matrix \(\mathbf{A} = \begin{pmatrix} 1 & 2 \\ -1 & -1 \end{pmatrix}\). (a) Show that \(\mathbf{A}^2 = -\mathbf{I}\). (b) Hence write \(\mathbf{A}^{-1}\) in terms of \(\mathbf{A}\) and find it. (c) Find \(\mathbf{A}^{2026}\). (d) Show that \((\mathbf{I} + \mathbf{A})^2 = 2\mathbf{A}\).
H: In (b), multiply \(\mathbf{A}^2 = -\mathbf{I}\) by \(\mathbf{A}^{-1}\) on the left.
H: In (c), find \(\mathbf{A}^4\) first and use it to cut the power down.
H: In (d), expand \((\mathbf{I} + \mathbf{A})(\mathbf{I} + \mathbf{A})\) in full: \(\mathbf{I}\) commutes with everything.
A: (a) \(\mathbf{A}^2 = \begin{pmatrix} 1 - 2 & 2 - 2 \\ -1 + 1 & -2 + 1 \end{pmatrix}\) [M1] \(= \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -\mathbf{I}\). [A1]
(b) \(\mathbf{A}^{-1}\mathbf{A}^2 = -\mathbf{A}^{-1}\), so \(\mathbf{A} = -\mathbf{A}^{-1}\) and \(\mathbf{A}^{-1} = -\mathbf{A}\) [M1] \(= \begin{pmatrix} -1 & -2 \\ 1 & 1 \end{pmatrix}\). [A1]
(c) \(\mathbf{A}^4 = (-\mathbf{I})^2 = \mathbf{I}\), and \(2026 = 4 \times 506 + 2\), so \(\mathbf{A}^{2026} = \mathbf{A}^2\) [M1] \(= -\mathbf{I}\). [A1]
(d) \((\mathbf{I} + \mathbf{A})^2 = \mathbf{I} + 2\mathbf{A} + \mathbf{A}^2\) [M1] \(= \mathbf{I} + 2\mathbf{A} - \mathbf{I} = 2\mathbf{A}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The matrix \(\mathbf{S} = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}\). (a) Show that \(\mathbf{S}^3 = \mathbf{I}\). (b) Hence write \(\mathbf{S}^{-1}\) as a power of \(\mathbf{S}\) and find \(\mathbf{S}^{100}\).
H: Find \(\mathbf{S}^2\) first and then multiply by \(\mathbf{S}\).
H: If \(\mathbf{S}^3 = \mathbf{I}\), then \(\mathbf{S}\mathbf{S}^2 = \mathbf{I}\). What does that say about the inverse?
A: (a) \(\mathbf{S}^2 = \begin{pmatrix} 0 - 1 & 0 + 1 \\ 0 - 1 & -1 + 1 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ -1 & 0 \end{pmatrix}\). [M1 A1]
\(\mathbf{S}^3 = \mathbf{S}^2\mathbf{S}\): row 1 of \(\mathbf{S}^2\) times column 1 of \(\mathbf{S}\) is \(-1(0) + 1(1) = 1\), and times column 2 is \(-1(-1) + 1(-1) = 0\); row 2 gives \(-1(0) + 0(1) = 0\) and \(-1(-1) + 0(-1) = 1\). So \(\mathbf{S}^3 = \mathbf{I}\). [A1]
(b) \(\mathbf{S}\mathbf{S}^2 = \mathbf{I}\), so \(\mathbf{S}^{-1} = \mathbf{S}^2 = \begin{pmatrix} -1 & 1 \\ -1 & 0 \end{pmatrix}\). [B1]
\(100 = 3 \times 33 + 1\), so \(\mathbf{S}^{100} = (\mathbf{S}^3)^{33}\mathbf{S} = \mathbf{S}\) [M1] \(= \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}\). [A1]
Q: [7 marks] ★★★ Find every \(2 \times 2\) matrix \(\mathbf{B}\) that commutes with \(\mathbf{J} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\), that is \(\mathbf{JB} = \mathbf{BJ}\). Hence write down two different matrices that commute with \(\mathbf{J}\) and are not multiples of \(\mathbf{I}\).
H: Let \(\mathbf{B} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\) and work out both products.
H: Compare the four entries of \(\mathbf{JB}\) and \(\mathbf{BJ}\) one at a time.
A: \(\mathbf{JB} = \begin{pmatrix} a + c & b + d \\ c & d \end{pmatrix}\) and \(\mathbf{BJ} = \begin{pmatrix} a & a + b \\ c & c + d \end{pmatrix}\). [M1 A1 A1]
Equal entries: \(a + c = a\) gives \(c = 0\); \(b + d = a + b\) gives \(d = a\); the other two entries then agree. [M1 A1]
So \(\mathbf{B} = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}\). [A1]
For example \(\begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}\) and \(\begin{pmatrix} 3 & 2 \\ 0 & 3 \end{pmatrix}\) commute with \(\mathbf{J}\). [B1]
:::

:::quiz
? What is the order of \(\mathbf{AB}\) when \(\mathbf{A}\) is \(2 \times 3\) and \(\mathbf{B}\) is \(3 \times 4\)?
+ \(2 \times 4\)
- \(3 \times 3\)
- \(2 \times 3\)
- It does not exist
> The inner numbers (3 and 3) match and disappear, leaving rows of \(\mathbf{A}\) by columns of \(\mathbf{B}\): \(2 \times 4\). \(3 \times 3\) mixes up the inner numbers, and \(\mathbf{BA}\), not \(\mathbf{AB}\), is the product that fails to exist.
? What is \(\begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}^{-1}\)?
+ \(\begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}\)
- \(\begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}\)
- \(\begin{pmatrix} -3 & 5 \\ 1 & -2 \end{pmatrix}\)
- \(\begin{pmatrix} \tfrac12 & \tfrac15 \\ 1 & \tfrac13 \end{pmatrix}\)
> The determinant is \(6 - 5 = 1\). Swap the diagonal, change the signs of the other two: \(\begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}\). Forgetting the sign changes gives the second option, changing the wrong signs gives the third, and inverting each entry is meaningless.
? \(\mathbf{A}\) and \(\mathbf{B}\) are non-singular. What is \((\mathbf{AB})^{-1}\)?
- \(\mathbf{A}^{-1}\mathbf{B}^{-1}\)
+ \(\mathbf{B}^{-1}\mathbf{A}^{-1}\)
- \(\mathbf{AB}^{-1}\)
- \(\dfrac{1}{\mathbf{AB}}\)
> The order reverses: \(\mathbf{AB}\mathbf{B}^{-1}\mathbf{A}^{-1} = \mathbf{I}\). Writing the inverses in the same order is the classic slip, and dividing by a matrix has no meaning.
? A \(3 \times 3\) matrix \(\mathbf{M}\) has \(\det \mathbf{M} = 5\). What is \(\det(2\mathbf{M})\)?
+ \(40\)
- \(10\)
- \(20\)
- \(25\)
> Each of the three rows is doubled, so the determinant is multiplied by \(2^3 = 8\): \(8 \times 5 = 40\). The answer 10 treats it as \(2 \det \mathbf{M}\).
? \(\mathbf{XA} = \mathbf{B}\), where \(\mathbf{A}\) is non-singular. What is \(\mathbf{X}\)?
- \(\mathbf{A}^{-1}\mathbf{B}\)
+ \(\mathbf{B}\mathbf{A}^{-1}\)
- \(\mathbf{B} - \mathbf{A}\)
- \(\dfrac{\mathbf{B}}{\mathbf{A}}\)
> \(\mathbf{A}\) is on the right of \(\mathbf{X}\), so multiply on the right by \(\mathbf{A}^{-1}\): \(\mathbf{X} = \mathbf{B}\mathbf{A}^{-1}\). \(\mathbf{A}^{-1}\mathbf{B}\) solves \(\mathbf{AX} = \mathbf{B}\) instead.
? Which sign goes with the entry in row 2, column 3 of a \(3 \times 3\) matrix when you find its cofactor?
+ \(-\)
- \(+\)
- It depends on the entry
- No sign: cofactors are always positive
> The sign is \((-1)^{i + j} = (-1)^{5} = -1\). The chessboard pattern starts with \(+\) at top left and alternates.
? Which matrix is singular?
+ \(\begin{pmatrix} 2 & 6 \\ 1 & 3 \end{pmatrix}\)
- \(\begin{pmatrix} 2 & 6 \\ 3 & 1 \end{pmatrix}\)
- \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\)
- \(\begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix}\)
> \(2 \times 3 - 6 \times 1 = 0\), so the first matrix is singular. The others have determinants \(-16\), \(-1\) and \(-1\); a matrix with a zero entry is not automatically singular.
:::

:::checklist What you can now do
- [ ] I can add, subtract and multiply matrices, state when a product exists and give its order, and recognise the zero and identity matrices.
- [ ] I can show by counterexample that \(\mathbf{AB} \ne \mathbf{BA}\), and use associativity and powers of a square matrix.
- [ ] I can find the determinant of a 2×2 and a 3×3 matrix, expanding along any row or column.
- [ ] I can say when a matrix is singular, and find the values of an unknown for which it is.
- [ ] I can find the inverse of a 2×2 matrix and a 3×3 matrix (cofactors, transpose, divide by the determinant) and check it.
- [ ] I can use \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\), including for three matrices.
- [ ] I can solve \(\mathbf{AX} = \mathbf{B}\) and \(\mathbf{XA} = \mathbf{B}\), and use an inverse to solve two or three simultaneous equations.
- [ ] I can use \(\det(k\mathbf{A}) = k^n\det\mathbf{A}\) and \(\det(\mathbf{AB}) = \det\mathbf{A}\det\mathbf{B}\).
:::

:::recap
- Order is rows \(\times\) columns. \((m \times n)(n \times p)\) gives \(m \times p\): the inner numbers must match.
- Entry \((i, j)\) of \(\mathbf{AB}\) is row \(i\) of \(\mathbf{A}\) times column \(j\) of \(\mathbf{B}\). Multiplication is associative and distributive but **not commutative**.
- \(\mathbf{AI} = \mathbf{IA} = \mathbf{A}\). Zero matrix: \(\mathbf{A} + \mathbf{O} = \mathbf{A}\).
- \(\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc\); a 3×3 determinant is \(a(ei - fh) - b(di - fg) + c(dh - eg)\), signs \(+ - +\) along the first row, chessboard pattern in general.
- Singular means \(\det = 0\): no inverse. \(\det(\mathbf{AB}) = \det\mathbf{A}\det\mathbf{B}\) and \(\det(k\mathbf{A}) = k^n\det\mathbf{A}\).
- 2×2 inverse: \(\dfrac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\). 3×3 inverse: minors, chessboard signs, transpose, divide by the determinant; check \(\mathbf{MM}^{-1} = \mathbf{I}\).
- \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\); \((\mathbf{ABC})^{-1} = \mathbf{C}^{-1}\mathbf{B}^{-1}\mathbf{A}^{-1}\).
- \(\mathbf{AX} = \mathbf{B}\) gives \(\mathbf{X} = \mathbf{A}^{-1}\mathbf{B}\); \(\mathbf{XA} = \mathbf{B}\) gives \(\mathbf{X} = \mathbf{B}\mathbf{A}^{-1}\). \(\mathbf{Mx} = \mathbf{b}\) gives \(\mathbf{x} = \mathbf{M}^{-1}\mathbf{b}\).
:::

:::links
- practise: [Matrices](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices) · Khan Academy · operations, determinants and inverses with instant feedback
- watch: [Matrix multiplication as composition](https://www.3blue1brown.com/lessons/matrix-multiplication) · 3Blue1Brown · why the product has its odd-looking rule
- watch: [The determinant](https://www.3blue1brown.com/lessons/determinant) · 3Blue1Brown · what a determinant measures
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · find the matrix and inverse tutorials in the Further Pure list
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · free booklets with answers on matrices
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Matrices as transformations](#math.fm.transform) shows how a 2×2 matrix moves every point of the plane, and what its determinant and inverse mean geometrically.
