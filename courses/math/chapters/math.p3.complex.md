@chapter math.p3.complex
@title Complex numbers
@level a2
@paper CAIE P3 (Further Mathematics on other boards)
@time 9–11 hours
@summary Complex numbers \(z = x + iy\): arithmetic in Cartesian form, conjugates and division, equating real and imaginary parts, roots of polynomials in conjugate pairs, the Argand diagram, modulus and argument, polar and exponential form, square roots of a complex number, and loci such as circles, perpendicular bisectors and half-lines.

:::why
The equation \(x^2 + 1 = 0\) has no real solution, yet quadratics and cubics with no real roots keep arising. Complex numbers close that gap: every polynomial has all its roots among them. They are also the language of anything that rotates or oscillates. An alternating-current circuit has an impedance \(R + iX\), the real part for resistance and the imaginary part for the effect of coils and capacitors. Multiplying by a complex number rotates and scales a point in the plane, and this single idea explains why sine and cosine waves behave as they do.
:::

**Before you start**, you need quadratics and the discriminant from [Quadratics](#math.p1.quadratics), the factor theorem from [Algebra from scratch](#math.f.algebra), radians and exact trigonometric values from [Circular measure](#math.p1.circular) and [Trigonometry](#math.p1.trig), and the equation of a circle from [Coordinate geometry: lines and circles](#math.p1.coord).

:::try Warm-up
Q: Find the discriminant of \(x^2 - 6x + 25\) and say what it tells you. (from [Quadratics](#math.p1.quadratics))
A: \(b^2 - 4ac = 36 - 100 = -64\). It is negative, so there are no real roots.
Q: Write down the exact values of \(\cos\dfrac\pi3\) and \(\sin\dfrac{2\pi}{3}\). (from [Trigonometry](#math.p1.trig))
A: \(\cos\dfrac\pi3 = \dfrac12\) and \(\sin\dfrac{2\pi}3 = \dfrac{\sqrt3}{2}\).
Q: Write down the equation of the circle with centre \((3, 2)\) and radius \(2\). (from [Coordinate geometry: lines and circles](#math.p1.coord))
A: \((x - 3)^2 + (y - 2)^2 = 4\).
:::

## The number i

:::def Imaginary unit and complex number
The **imaginary unit** \(i\) is defined by \(i^2 = -1\). A **complex number** has the form \(z = x + iy\) where \(x\) and \(y\) are real. We call \(x\) the **real part**, \(\mathrm{Re}\,z\), and \(y\) the **imaginary part**, \(\mathrm{Im}\,z\) (a real number, without the \(i\)).
:::

Add and subtract by combining real parts and imaginary parts. Multiply by expanding brackets as usual and replacing \(i^2\) by \(-1\).

:::eg Given \(z_1 = 3 + 2i\) and \(z_2 = 1 - 4i\), find \(z_1 + z_2\), \(z_1 - z_2\) and \(z_1z_2\).
\(z_1 + z_2 = 4 - 2i\) and \(z_1 - z_2 = 2 + 6i\).
\[z_1z_2 = (3 + 2i)(1 - 4i) = 3 - 12i + 2i - 8i^2 = 3 - 10i + 8 = 11 - 10i\]
:::

## Conjugates and division

:::def Complex conjugate
The **complex conjugate** of \(z = x + iy\) is \(z^* = x - iy\). The product of a number and its conjugate is real:
\[zz^* = (x + iy)(x - iy) = x^2 + y^2\]
:::

To divide, multiply the top and the bottom by the **conjugate of the denominator**. This turns the denominator into a real number, just as rationalising does for surds.

:::eg Express \(\dfrac{5 + i}{2 - i}\) in the form \(x + iy\).
Multiply top and bottom by \(2 + i\), the conjugate of the denominator:
\[\frac{(5 + i)(2 + i)}{(2 - i)(2 + i)} = \frac{10 + 5i + 2i + i^2}{4 + 1} = \frac{9 + 7i}{5} = \frac95 + \frac75 i\]
:::

## Equating real and imaginary parts

Two complex numbers are equal exactly when their real parts are equal **and** their imaginary parts are equal. So one complex equation gives two real equations.

:::eg (a) Find real numbers \(a\) and \(b\) such that \((a + ib)(1 + 2i) = 5 + 5i\). (b) Solve \(z + 2z^* = 6 - 4i\).
(a) Expand: \((a + ib)(1 + 2i)\) \(= a + 2ai + bi + 2bi^2\) \(= (a - 2b) + (2a + b)i\). Equate real parts: \(a - 2b = 5\); imaginary parts: \(2a + b = 5\). Solving: \(a = 3\), \(b = -1\).

(b) Let \(z = x + iy\), so \(z^* = x - iy\). Then \(z + 2z^* = 3x - iy\). Equating: \(3x = 6\) and \(-y = -4\), so \(z = 2 + 4i\).
:::

## Roots of polynomials

Using \(i\), every quadratic can be solved. When the discriminant is negative, the roots are complex, and they come as a **conjugate pair**.

:::key Conjugate pairs
If a polynomial has **real** coefficients and \(a + ib\) is a root, then its conjugate \(a - ib\) is also a root. The two roots give the real quadratic factor
\[(z - (a + ib))(z - (a - ib)) = z^2 - 2az + (a^2 + b^2)\]
:::

:::proof Why non-real roots of a real polynomial come in conjugate pairs
Two facts about conjugates, each checked from \(z = x + iy\): \((z_1 + z_2)^* = z_1^* + z_2^*\) and \((z_1z_2)^* = z_1^*z_2^*\). A real number is its own conjugate.
Let \(\mathrm{p}(z)\) \(= a_nz^n + \cdots + a_1z + a_0\) with every \(a_k\) real, and suppose \(\mathrm{p}(w) = 0\) for some complex \(w\).
Take the conjugate of both sides of \(a_nw^n + \cdots + a_1w + a_0 = 0\). The right side is \(0^* = 0\).
On the left, the conjugate of a sum is the sum of the conjugates, and the conjugate of each product is \(a_k^*(w^*)^k = a_k(w^*)^k\), since \(a_k\) is real. So \(a_n(w^*)^n + \cdots + a_1w^* + a_0 = 0\).
That says \(\mathrm{p}(w^*) = 0\): the conjugate \(w^*\) is a root too. If \(w\) is not real then \(w^* \ne w\), so the roots come in pairs.
:::

:::eg (a) Solve \(z^2 - 4z + 13 = 0\). (b) Given that \(2 + i\) is a root of \(z^3 - 6z^2 + 13z - 10 = 0\), find the other roots.
(a) By the quadratic formula, \(z = \dfrac{4 \pm \sqrt{16 - 52}}{2}\) \(= \dfrac{4 \pm \sqrt{-36}}{2}\) \(= 2 \pm 3i\).

(b) The coefficients are real, so \(2 - i\) is also a root. The quadratic factor is \(z^2 - 4z + 5\) (sum of roots \(4\), product \(2^2 + 1^2 = 5\)). Divide: \(z^3 - 6z^2 + 13z - 10\) \(= (z - 2)(z^2 - 4z + 5)\). The roots are \(2\), \(2 + i\) and \(2 - i\).
:::

## The Argand diagram, modulus and argument

:::def Argand diagram
An **Argand diagram** plots \(z = x + iy\) as the point \((x, y)\): the real axis is horizontal and the imaginary axis is vertical. The number \(z\) can also be pictured as the vector from the origin to that point.
:::

:::def Modulus and argument
The **modulus** of \(z = x + iy\) is its distance from the origin, \(|z| = \sqrt{x^2 + y^2}\). The **argument**, \(\arg z\), is the angle from the positive real axis to the line from the origin to \(z\), measured anticlockwise. Unless told otherwise, take \(-\pi < \arg z \le \pi\), the principal value. (Cambridge also accepts \(0 \le \arg z < 2\pi\).)
:::

Always sketch the point to find the correct quadrant. Use \(\tan^{-1}\left|\tfrac yx\right|\) to find the acute angle \(\alpha\) with the real axis, then adjust: in the second quadrant \(\arg z = \pi - \alpha\); in the third, \(\arg z = -(\pi - \alpha)\); in the fourth, \(\arg z = -\alpha\).

:::eg Find the modulus and argument of (a) \(-1 + \sqrt3\,i\) and (b) \(-2 - 2i\), giving the arguments in radians.
(a) \(|z| = \sqrt{1 + 3} = 2\). The point is in the second quadrant; the acute angle is \(\tan^{-1}\sqrt3 = \tfrac\pi3\), so \(\arg z = \pi - \tfrac\pi3\) \(= \tfrac{2\pi}3\) (\(2.09\) to 3 s.f.).
(b) \(|z| = \sqrt{4 + 4} = 2\sqrt2\). The point is in the third quadrant; the acute angle is \(\tfrac\pi4\), so \(\arg z\) \(= -\left(\pi - \tfrac\pi4\right)\) \(= -\tfrac{3\pi}4\) (\(-2.36\) to 3 s.f.).
:::

## Polar and exponential form

If \(|z| = r\) and \(\arg z = \theta\), then \(x = r\cos\theta\) and \(y = r\sin\theta\), so
\[z = r(\cos\theta + i\sin\theta) = re^{i\theta}\]
This is the **modulus–argument form** (polar form), and the second expression is the **exponential form**.
Multiplying in polar form is simple, because the angles behave like indices:

:::key Multiplying and dividing in polar form
\[|z_1z_2| = |z_1||z_2| \qquad \arg(z_1z_2) = \arg z_1 + \arg z_2\]
\[\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|} \qquad \arg\frac{z_1}{z_2} = \arg z_1 - \arg z_2\]
In exponential form: \(r_1e^{i\theta_1}\times r_2e^{i\theta_2}\) \(= r_1r_2e^{i(\theta_1 + \theta_2)}\).
:::

Multiplication by a complex number **scales** by its modulus and **rotates** by its argument. In particular, multiplying by \(i\) (modulus 1, argument \(\tfrac\pi2\)) rotates a point through a quarter turn anticlockwise. Taking the conjugate reflects the point in the real axis.

:::proof Why moduli multiply and arguments add
Let \(z_1 = r_1(\cos\alpha + i\sin\alpha)\) and \(z_2 = r_2(\cos\beta + i\sin\beta)\). Multiply, expanding as usual and using \(i^2 = -1\):
\[z_1z_2 = r_1r_2\Big[(\cos\alpha\cos\beta - \sin\alpha\sin\beta) + i(\sin\alpha\cos\beta + \cos\alpha\sin\beta)\Big]\]
The compound angle formulae from [Further trigonometry](#math.p3.trig) say that the real bracket is \(\cos(\alpha + \beta)\) and the imaginary bracket is \(\sin(\alpha + \beta)\). So
\[z_1z_2 = r_1r_2\big[\cos(\alpha + \beta) + i\sin(\alpha + \beta)\big]\]
This has modulus \(r_1r_2\) and argument \(\alpha + \beta\). (An argument may need \(\pm2\pi\) to bring it into the principal range.)
For division, let \(w = \dfrac{z_1}{z_2}\), so \(z_1 = z_2w\). By the result above, \(|z_1| = |z_2||w|\) and \(\arg z_1 = \arg z_2 + \arg w\). Rearranging, \(|w| = \dfrac{|z_1|}{|z_2|}\) and \(\arg w = \arg z_1 - \arg z_2\).
:::

:::eg Let \(z_1 = 1 + i\) and \(z_2 = -1 + \sqrt3\,i\). Find the modulus and argument of \(z_1z_2\) and of \(\dfrac{z_1}{z_2}\).
\(|z_1| = \sqrt2\), \(\arg z_1 = \tfrac\pi4\); \(|z_2| = 2\), \(\arg z_2 = \tfrac{2\pi}3\).
\(|z_1z_2| = 2\sqrt2\) and \(\arg(z_1z_2)\) \(= \tfrac\pi4 + \tfrac{2\pi}3\) \(= \tfrac{11\pi}{12}\) (\(2.88\)).
\(\left|\dfrac{z_1}{z_2}\right|\) \(= \dfrac{\sqrt2}2\) and \(\arg\dfrac{z_1}{z_2}\) \(= \tfrac\pi4 - \tfrac{2\pi}3\) \(= -\tfrac{5\pi}{12}\) (\(-1.31\)).
:::

The widget shows the effect of each operation on the Argand diagram. Drag the sliders for \(z_1\) and \(z_2\) and watch the modulus multiply and the arguments add.

:::html
<div class="widget" data-w="argand" data-mode="ops" data-z1="3,2" data-z2="1,-1"></div>
:::

## Square roots of a complex number

To find \(\sqrt{a + bi}\), write \((x + iy)^2 = a + bi\), expand, and equate real and imaginary parts. The two resulting equations give the two roots, which are always negatives of each other.

:::eg Find the square roots of \(5 + 12i\) in the form \(x + iy\).
Let \((x + iy)^2 = 5 + 12i\). Then \(x^2 - y^2 = 5\) and \(2xy = 12\), so \(y = \dfrac6x\). Substituting: \(x^2 - \dfrac{36}{x^2} = 5\), so \(x^4 - 5x^2 - 36 = 0\), that is \((x^2 - 9)(x^2 + 4) = 0\). Since \(x\) is real, \(x^2 = 9\) and \(x = \pm3\), giving \(y = \pm2\) with the same sign. The square roots are \(\pm(3 + 2i)\).

Check: \((3 + 2i)^2 = 9 + 12i - 4 = 5 + 12i\) ✓.
:::

## Loci in the Argand diagram

A **locus** is the set of points \(z\) satisfying a condition. Three kinds appear in the syllabus.

:::key The three loci
- \(|z - a| = k\): the distance from \(z\) to the point \(a\) is \(k\). It is a **circle**, centre \(a\), radius \(k\).
- \(|z - a| = |z - b|\): \(z\) is equally far from \(a\) and \(b\). It is the **perpendicular bisector** of the line joining \(a\) and \(b\).
- \(\arg(z - a) = \alpha\): the line from \(a\) to \(z\) makes angle \(\alpha\) with the real axis direction. It is a **half-line** starting at \(a\) (not including \(a\) itself).
For inequalities, \(|z - a| < k\) is the inside of the circle, \(>\) the outside; a solid line means \(\le\) or \(\ge\), a dashed line means \(<\) or \(>\).
:::

:::eg Describe and sketch (a) \(|z - 3 - 2i| = 2\), (b) \(|z - 1| = |z - i|\), (c) \(\arg(z - 1 - i) = \tfrac\pi4\).
(a) \(z - 3 - 2i = z - (3 + 2i)\), so this is a circle with centre \(3 + 2i\), that is \((3, 2)\), and radius \(2\).
(b) The points \(1\) and \(i\) are \((1, 0)\) and \((0, 1)\). The locus is their perpendicular bisector. With \(z = x + iy\): \((x - 1)^2 + y^2 = x^2 + (y - 1)^2\) gives \(-2x + 1 = -2y + 1\), so \(y = x\).
(c) A half-line from \((1, 1)\) at \(45^\circ\) to the real-axis direction, that is the part of \(y = x\) with \(x > 1\), excluding the end point \((1, 1)\).
:::

The widget draws each of these. Change the centre, radius or angle, and use the shading option to show an inequality.

:::html
<div class="widget" data-w="argand" data-mode="locus" data-locus="circle" data-a="3,2" data-k="2"></div>
:::

:::eg (Exam style) On an Argand diagram, shade the region \(R\) whose points satisfy both \(|z - 3 - 2i| \le 2\) and \(|z - 3| \le |z - 3 - 4i|\). Find the area of \(R\).
The first condition is the disc with centre \((3, 2)\) and radius \(2\). [B1] The second says \(z\) is at least as close to \(3\) as to \(3 + 4i\); the perpendicular bisector of \((3, 0)\) and \((3, 4)\) is the line \(y = 2\), and the region is the side containing \((3, 0)\), that is \(y \le 2\). [B1 B1]
The line \(y = 2\) passes through the centre of the disc, so \(R\) is the lower half of the disc. [M1]
Area \(= \tfrac12\pi(2)^2 = 2\pi\). [A1]
:::

:::html
<figure class="fig small"><svg viewBox="0 0 290 215" role="img" aria-label="Argand diagram showing the lower half of a disc with centre 3 plus 2i and radius 2, bounded above by the line imaginary part equals 2 and touching the real axis at 3."><path class="ax" d="M20 190H280" marker-end="url(#ahm)"/><path class="ax" d="M40 205V8" marker-end="url(#ahm)"/><path class="fi" d="M78 114A76 76 0 0 0 230 114Z"/><circle class="ln thin dash" cx="154" cy="114" r="76"/><path class="c1" d="M78 114A76 76 0 0 0 230 114"/><path class="ln" d="M78 114H230"/><circle class="fa" cx="154" cy="114" r="3"/><text class="tl" x="160" y="106">3 + 2i</text><text class="tl ti" x="276" y="182" text-anchor="end">Re</text><text class="tl ti" x="46" y="18">Im</text><text class="tl halo" x="86" y="130">R</text><text class="tl halo" x="232" y="108">y = 2</text><text class="ts tc" x="154" y="204">3</text><text class="ts te" x="35" y="118">2</text></svg><figcaption>The region \(R\): the lower half of the disc \(|z - 3 - 2i| \le 2\), below the line \(y = 2\). The disc touches the real axis at \(3\).</figcaption></figure>
:::

## An application: impedance

:::eg (Real context) In an alternating-current circuit, a component's impedance is a complex number \(Z = R + iX\) ohms, where \(R\) is the resistance and \(X\) the reactance. Two components in parallel have impedances \(Z_1 = 3 + 4i\) and \(Z_2 = 1 - 2i\). The combined impedance \(Z\) satisfies \(\dfrac1Z = \dfrac1{Z_1} + \dfrac1{Z_2}\). Find \(Z\) in the form \(x + iy\) and its modulus and argument.
\(\dfrac1Z = \dfrac{Z_1 + Z_2}{Z_1Z_2}\), so \(Z = \dfrac{Z_1Z_2}{Z_1 + Z_2}\). Now \(Z_1Z_2 = (3 + 4i)(1 - 2i)\) \(= 3 - 6i + 4i - 8i^2 = 11 - 2i\), and \(Z_1 + Z_2 = 4 + 2i\).
\[Z = \frac{11 - 2i}{4 + 2i} = \frac{(11 - 2i)(4 - 2i)}{16 + 4} = \frac{44 - 22i - 8i + 4i^2}{20} = \frac{40 - 30i}{20} = 2 - 1.5i\]
The modulus is \(|Z| = \sqrt{4 + 2.25} = 2.5\) ohms, and the argument is \(\tan^{-1}\left(-\tfrac{1.5}{2}\right)\) \(= -0.644\) radians (3 s.f.). The modulus is the size of the opposition to the current; the argument is the phase difference between voltage and current.
:::

## Long exam questions

Long complex-number questions combine algebra with the diagram. A sketch is usually worth marks of its own, so draw it even when the question does not insist.

:::eg (Exam style) The polynomial \(\mathrm{p}(z) = z^3 - 4z^2 + 14z - 20\). (a) Show that \(1 + 3i\) is a root of \(\mathrm{p}(z) = 0\). (b) Find the other two roots. (c) The three roots are plotted on an Argand diagram. Find the area of the triangle whose vertices are the three roots.
**(a)** \((1 + 3i)^2 = 1 + 6i + 9i^2 = -8 + 6i\). [M1] Then
\[(1 + 3i)^3 = (1 + 3i)(-8 + 6i) = -8 + 6i - 24i + 18i^2 = -26 - 18i \quad [M1]\]
\[\mathrm{p}(1 + 3i) = (-26 - 18i) - 4(-8 + 6i) + 14(1 + 3i) - 20 = (-26 + 32 + 14 - 20) + (-18 - 24 + 42)i = 0 \quad [A1]\]
**(b)** The coefficients are real, so the conjugate \(1 - 3i\) is also a root. [B1] The quadratic factor has sum of roots \(2\) and product \(1^2 + 3^2 = 10\): \(z^2 - 2z + 10\). [M1]
Divide:
\[z^3 - 4z^2 + 14z - 20 = (z^2 - 2z + 10)(z - 2)\]
The constant terms agree, because \(10 \times (-2) = -20\). [M1] The third root is \(z = 2\). [A1]

**(c)** The vertices are \((2, 0)\), \((1, 3)\) and \((1, -3)\). [B1] The side joining \((1, 3)\) and \((1, -3)\) is vertical with length \(6\), and the point \((2, 0)\) is \(1\) unit from the line \(x = 1\). [M1]
\[\text{Area} = \tfrac12 \times 6 \times 1 = 3 \quad [A1]\]
:::

:::eg (Exam style) (a) Sketch on one Argand diagram the locus \(|z - 2 - i| = 2\) and the locus \(\arg(z - 1) = \dfrac\pi4\). (b) Show that exactly one complex number satisfies both conditions, and find it in the form \(x + iy\), with exact values. (c) Find the greatest value of \(|z|\) for points on the circle \(|z - 2 - i| = 2\).
**(a)** The first locus is a circle with centre \((2, 1)\) and radius \(2\). [B1 B1] The second is a half-line starting at \((1, 0)\) and rising at \(45^\circ\) to the real-axis direction. The point \((1, 0)\) is not on it, so mark the end with an open dot. [B1 B1]

**(b)** The half-line lies on \(y = x - 1\), with \(x > 1\). The circle is \((x - 2)^2 + (y - 1)^2 = 4\). Substitute \(y = x - 1\): \((x - 2)^2 + (x - 2)^2 = 4\). [M1]
So \((x - 2)^2 = 2\), giving \(x = 2 \pm \sqrt2\). [A1 A1] Only \(x > 1\) is on the half-line: \(2 - \sqrt2 = 0.59\) is rejected. [B1]
Then \(y = x - 1 = 1 + \sqrt2\), so \(z = (2 + \sqrt2) + (1 + \sqrt2)i\). [A1]

**(c)** The point of the circle furthest from the origin lies on the line from the origin through the centre. Its distance is the distance to the centre plus the radius: \(|2 + i| + 2\). [M1] The greatest value is \(\sqrt5 + 2 = 4.24\). [A1]
Check (b): the point is \((2 + \sqrt2,\ 1 + \sqrt2)\), so the vector from the centre \((2, 1)\) is \((\sqrt2, \sqrt2)\), which has length \(\sqrt{2 + 2} = 2\). ✓
:::

:::eg Spot the error: the argument in the wrong quadrant
A student answered "Express \(-2 + 2i\) in the form \(re^{i\theta}\), with \(-\pi < \theta \le \pi\)" [4 marks].

Line 1: \(r = \sqrt{(-2)^2 + 2^2} = 2\sqrt2\).
Line 2: \(\tan\theta = \dfrac{2}{-2} = -1\), so \(\theta = -\dfrac\pi4\).
Line 3: \(-2 + 2i = 2\sqrt2\,e^{-i\pi/4}\).

Line 1 scores [B1]. Line 2 finds the acute angle \(\dfrac\pi4\) [M1], but it does not adjust for the quadrant [M0], so the final answer is wrong [A0]: the calculator gives an angle between \(-\dfrac\pi2\) and \(\dfrac\pi2\), which is never in the second quadrant. The student scores 2 out of 4.

Correct working: the point \((-2, 2)\) is in the second quadrant, so \(\theta = \pi - \dfrac\pi4\) \(= \dfrac{3\pi}{4}\) and \(-2 + 2i = 2\sqrt2\,e^{3i\pi/4}\).

**Check:** \(2\sqrt2\,e^{-i\pi/4}\) \(= 2\sqrt2\left(\dfrac{1}{\sqrt2} - \dfrac{i}{\sqrt2}\right)\) \(= 2 - 2i\), which is in the fourth quadrant, not the second. Always sketch the point first.
:::

:::exam What earns marks
- **Show the working in Cartesian form**: expand brackets, replace \(i^2\) by \(-1\), and for division show the multiplication by the conjugate. The syllabus asks for full working.
- For a non-real root of a polynomial with real coefficients, **state that the conjugate is also a root**, then use the sum and product to form the quadratic factor.
- **Arguments**: sketch to find the quadrant, give the answer in radians (or exact multiples of \(\pi\)), in \(-\pi < \theta \le \pi\) unless told otherwise.
- **Loci**: label the centre and radius of a circle, the end point of a half-line, and shade the region clearly. Write the points that bound the region.
- Learn the rules for the modulus and argument of a product and a quotient; the formula booklet will not do the work for you.
:::

:::board Other boards
Complex numbers are part of Cambridge Paper 3. Edexcel IAL and the UK A Levels (AQA, OCR, Edexcel) teach them in Further Mathematics, not in the main Pure Mathematics course. If you are taking one of those boards, check your specification before spending time on this chapter.
:::

:::try Start easy, finish at exam standard
Q: Express \((2 + 3i)(4 - i)\) in the form \(x + iy\).
A: \(8 - 2i + 12i - 3i^2 = 8 + 10i + 3\) \(= 11 + 10i\).
Q: Express \(\dfrac{7 + i}{1 + i}\) in the form \(x + iy\).
A: \(\dfrac{(7 + i)(1 - i)}{(1 + i)(1 - i)}\) \(= \dfrac{7 - 7i + i - i^2}{2}\) \(= \dfrac{8 - 6i}{2} = 4 - 3i\).
Q: Solve \(z^2 + 2z + 10 = 0\).
A: \(z = \dfrac{-2 \pm \sqrt{4 - 40}}{2}\) \(= \dfrac{-2 \pm 6i}{2} = -1 \pm 3i\).
Q: Find the modulus and the argument (in radians, 3 s.f.) of \(-\sqrt3 - i\).
A: \(|z| = \sqrt{3 + 1} = 2\). The point is in the third quadrant, the acute angle is \(\tan^{-1}\tfrac{1}{\sqrt3}\) \(= \tfrac\pi6\), so \(\arg z\) \(= -\left(\pi - \tfrac\pi6\right)\) \(= -\tfrac{5\pi}{6} = -2.62\).
Q: Find the square roots of \(8 + 6i\).
A: \(x^2 - y^2 = 8\) and \(xy = 3\), so \(x^4 - 8x^2 - 9 = 0\), \((x^2 - 9)(x^2 + 1) = 0\), \(x = \pm3\), \(y = \pm1\). The roots are \(\pm(3 + i)\).
Q: Given \(z_1 = 3e^{i\pi/6}\) and \(z_2 = 2e^{i\pi/3}\), find \(z_1z_2\) and \(\dfrac{z_1}{z_2}\) in modulus–argument form, and write \(z_1z_2\) in the form \(x + iy\).
A: \(z_1z_2 = 6e^{i\pi/2} = 6i\). \(\dfrac{z_1}{z_2} = \tfrac32e^{-i\pi/6}\).
Q: Solve \(z + 2z^* = 9 - 2i\), giving \(z\) in the form \(x + iy\).
A: With \(z = x + iy\): \(3x - iy = 9 - 2i\), so \(x = 3\) and \(y = 2\); \(z = 3 + 2i\).
Q: Describe the locus \(|z - 2| = |z + 2i|\) and find its Cartesian equation.
A: The perpendicular bisector of the points \(2\) and \(-2i\). \((x - 2)^2 + y^2 = x^2 + (y + 2)^2\) gives \(-4x + 4 = 4y + 4\), so \(y = -x\).
Q: (Exam style) Show that \(z = 3\) is a root of \(z^3 - 5z^2 + 11z - 15 = 0\), and find the other two roots.
A: \(27 - 45 + 33 - 15 = 0\) ✓. Divide by \(z - 3\): \(z^3 - 5z^2 + 11z - 15\) \(= (z - 3)(z^2 - 2z + 5)\). Then \(z^2 - 2z + 5 = 0\) gives \(z = \dfrac{2 \pm \sqrt{4 - 20}}{2}\) \(= 1 \pm 2i\). The roots are \(3\), \(1 + 2i\) and \(1 - 2i\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Express \(\dfrac{4 - 3i}{1 + 2i}\) in the form \(x + iy\).
A: Multiply top and bottom by \(1 - 2i\): \(\dfrac{(4 - 3i)(1 - 2i)}{(1 + 2i)(1 - 2i)}\). [M1] The numerator is \(4 - 8i - 3i + 6i^2 = -2 - 11i\) and the denominator is \(1 + 4 = 5\). [A1] The result is \(-\dfrac25 - \dfrac{11}{5}i\). [A1]
Q: [3 marks] ★ Solve the equation \(z^2 - 6z + 25 = 0\).
A: \(z = \dfrac{6 \pm \sqrt{36 - 100}}{2}\). [M1] \(= \dfrac{6 \pm \sqrt{-64}}{2}\) \(= \dfrac{6 \pm 8i}{2}\). [A1] So \(z = 3 + 4i\) or \(z = 3 - 4i\). [A1]
Q: [5 marks] ★★ Find the real numbers \(a\) and \(b\) such that \((a + bi)(2 - i) = 8 + i\).
A: Expand:
\[(a + bi)(2 - i) = 2a - ai + 2bi - bi^2 = (2a + b) + (2b - a)i\]
[M1 A1] Equate real parts: \(2a + b = 8\); imaginary parts: \(2b - a = 1\). [M1] From the second, \(a = 2b - 1\), so \(4b - 2 + b = 8\) and \(b = 2\). [A1] Then \(a = 3\). [A1]
Q: [5 marks] ★★ Given that \(3 - 2i\) is a root of \(z^3 - 5z^2 + 7z + 13 = 0\), find the other two roots.
A: The coefficients are real, so \(3 + 2i\) is also a root. [B1] The quadratic factor is \(z^2 - 6z + 13\) (sum \(6\), product \(9 + 4 = 13\)). [M1] Then
\[z^3 - 5z^2 + 7z + 13 = (z^2 - 6z + 13)(z + 1)\]
found by division or by comparing constants. [M1 A1] The other roots are \(3 + 2i\) and \(-1\). [A1]
Q: [6 marks] ★★ Find the square roots of \(7 - 24i\), in the form \(x + iy\).
A: Let \((x + iy)^2 = 7 - 24i\), so \(x^2 - y^2 = 7\) and \(2xy = -24\). [M1 A1 A1] Then \(y = -\dfrac{12}{x}\), so \(x^2 - \dfrac{144}{x^2} = 7\), which is \(x^4 - 7x^2 - 144 = 0\). [M1] Factorise: \((x^2 - 16)(x^2 + 9) = 0\), so \(x = \pm4\). [A1] The square roots are \(4 - 3i\) and \(-4 + 3i\). [A1]
Q: [8 marks] ★★ Let \(z = 1 + \sqrt3\,i\) and \(w = -\sqrt3 + i\). (a) Find the modulus and argument of \(z\) and of \(w\), giving the arguments as multiples of \(\pi\). (b) Find the modulus and argument of \(zw\) and of \(\dfrac zw\), with the arguments in the range \(-\pi < \theta \le \pi\).
A: (a) \(|z| = 2\) and \(\arg z = \dfrac\pi3\). [B1 B1] \(|w| = 2\); \(w\) is in the second quadrant with acute angle \(\dfrac\pi6\), so \(\arg w = \dfrac{5\pi}{6}\). [B1 B1] (b) \(|zw| = 4\) and \(\arg(zw) = \dfrac\pi3 + \dfrac{5\pi}6\) \(= \dfrac{7\pi}{6}\), which is \(-\dfrac{5\pi}{6}\) in the principal range. [M1 A1] \(\left|\dfrac zw\right| = 1\) and \(\arg\dfrac zw\) \(= \dfrac\pi3 - \dfrac{5\pi}6\) \(= -\dfrac\pi2\). [M1 A1]
Q: [10 marks] (#math.p1.coord) ★★★ The complex number \(z\) satisfies \(|z - 4 - 3i| \le 3\). (a) Sketch the region of the Argand diagram that represents \(z\). (b) Find the greatest value of \(|z|\). (c) Find the greatest value of \(\arg z\), correct to 3 significant figures. (d) State the least value of \(\arg z\) and explain your answer.
H: The region is a disc. Find its centre and radius from the inequality, and note the distance from the origin to the centre.
H: For (c), draw the tangent from the origin to the circle. The radius to the point of contact is perpendicular to the tangent, which gives a right-angled triangle.
H: The greatest argument is the argument of the centre plus the angle between the centre line and the tangent.
A: (a) A solid circle with centre \((4, 3)\) and radius \(3\), with its inside shaded. [B1 B1] (b) The distance from the origin to the centre is \(\sqrt{16 + 9} = 5\), so the greatest \(|z| = 5 + 3 = 8\). [M1 A1] (c) In the right-angled triangle formed by the origin, the centre and the point of contact, the hypotenuse is \(5\) and the side opposite the angle \(\varphi\) at the origin is the radius \(3\), so \(\sin\varphi = \dfrac35\) and \(\varphi = 0.6435\). [M1 A1] \(\arg(4 + 3i) = \tan^{-1}\dfrac34\) \(= 0.6435\). So the greatest argument is \(0.6435 + 0.6435 = 1.29\). [M1 A1] (d) The least argument is \(0.6435 - 0.6435 = 0\): the circle touches the real axis at \(4\) (the radius \(3\) equals the height of the centre), so the real axis is the tangent. [B1 B1]
:::

:::try Stretch for A*
Q: [9 marks] ★★★ (a) Write \(1\) as \(1 \times e^{2k\pi i}\), where \(k\) is an integer, and use the rule for powers of \(re^{i\theta}\) to find all the complex numbers \(z\) with \(z^3 = 1\), with \(-\pi < \arg z \le \pi\). (b) Show that the points representing these three numbers on an Argand diagram are the vertices of an equilateral triangle, and find its area.
H: Put \(z = re^{i\theta}\). Then \(z^3 = r^3e^{3i\theta}\). Compare modulus and argument with those of \(1\).
H: For the area, all three points are on a circle of radius \(1\) centred at the origin, with equal angles between them.
A: (a) Let \(z = re^{i\theta}\). Then \(z^3 = r^3e^{3i\theta} = e^{2k\pi i}\). [M1] Moduli: \(r^3 = 1\), so \(r = 1\). [A1] Arguments: \(3\theta = 2k\pi\), so \(\theta = \dfrac{2k\pi}{3}\). [M1] With \(-\pi < \theta \le \pi\), \(k = -1, 0, 1\) give \(z = e^{-2\pi i/3}\), \(1\) and \(e^{2\pi i/3}\). [A1] (b) All three have modulus \(1\), so they lie on the unit circle, with arguments \(120^\circ\) apart, so the chords between them are equal and the triangle is equilateral. [B1] The numbers are \(1\) and \(-\dfrac12 \pm \dfrac{\sqrt3}{2}i\). The side between \(1\) and \(-\dfrac12 + \dfrac{\sqrt3}{2}i\) is \(\sqrt{\left(\dfrac32\right)^2 + \left(\dfrac{\sqrt3}{2}\right)^2}\) \(= \sqrt3\). [M1 A1] Area \(= \tfrac12 \times \sqrt3 \times \sqrt3 \times \sin 60^\circ\). [M1] \(= \dfrac{3\sqrt3}{4} = 1.30\). [A1]
Q: [6 marks] ★★★ The complex number \(z\) satisfies \(|z| = 1\) and \(z \ne -1\). (a) Show that \(z^* = \dfrac1z\). (b) Let \(w = \dfrac{z - 1}{z + 1}\). Show that \(w^* = -w\). (c) What does this tell you about \(\mathrm{Re}\,w\)? (d) Check this when \(z = \dfrac{3 + 4i}{5}\).
H: For (a), remember that \(zz^* = |z|^2\).
H: For (b), take the conjugate of \(w\) and replace \(z^*\) by \(\dfrac1z\). Then multiply the top and bottom by \(z\).
A: (a) \(zz^* = |z|^2 = 1\) [M1], so \(z^* = \dfrac1z\). [A1] (b) \(w^* = \dfrac{z^* - 1}{z^* + 1}\) \(= \dfrac{\frac1z - 1}{\frac1z + 1}\). [M1] Multiply top and bottom by \(z\): \(w^* = \dfrac{1 - z}{1 + z}\). [M1] This is \(-\dfrac{z - 1}{z + 1} = -w\). [A1] (c) If \(w = a + bi\) then \(w^* = a - bi = -a - bi\), so \(a = 0\): \(\mathrm{Re}\,w = 0\), and \(w\) is purely imaginary. [B1] (d) \(|z| = \dfrac{\sqrt{9 + 16}}{5} = 1\). 
\[w = \dfrac{-0.4 + 0.8i}{1.6 + 0.8i} = \dfrac{(-0.4 + 0.8i)(1.6 - 0.8i)}{3.2} = \dfrac{1.6i}{3.2} = 0.5i\]
This is purely imaginary. ✓
:::

:::quiz
? What is \((1 + i)^2\)?
- \(2\)
+ \(2i\)
- \(1 + i\)
- \(0\)
> \((1 + i)^2 = 1 + 2i + i^2 = 1 + 2i - 1\) \(= 2i\).
? If \(z = 3 - 4i\), what is \(zz^*\)?
- \(-7\)
- \(7\)
+ \(25\)
- \(9 + 16i\)
> \(zz^* = (3 - 4i)(3 + 4i) = 9 + 16 = 25\) \(= |z|^2\), always real and non-negative.
? What is \(\arg(-1 - i)\) in the principal range?
- \(\tfrac{3\pi}4\)
- \(\tfrac\pi4\)
+ \(-\tfrac{3\pi}4\)
- \(-\tfrac\pi4\)
> The point is in the third quadrant, so the argument is negative; the acute angle is \(\tfrac\pi4\), giving \(-(\pi - \tfrac\pi4) = -\tfrac{3\pi}{4}\).
? A cubic with real coefficients has roots \(2\) and \(1 + 3i\). What is the third root?
- \(-1 - 3i\)
- \(1\)
+ \(1 - 3i\)
- \(-2\)
> Non-real roots of a polynomial with real coefficients occur in conjugate pairs, so \(1 - 3i\) must also be a root.
? Which locus is a straight line?
- \(|z - 2| = 3\)
+ \(|z - 2| = |z - 6i|\)
- \(|z| \le 3\)
- \(|z| = 3\)
> Equal distance from two fixed points is a perpendicular bisector, a straight line. \(|z - 2| = 3\) and \(|z| = 3\) are circles, and \(|z| \le 3\) is a disc.
:::

:::checklist What you can now do
- [ ] I can add, subtract, multiply and divide complex numbers in the form \(x + iy\), showing the working.
- [ ] I can find the real and imaginary parts, the modulus, the argument and the conjugate of a complex number.
- [ ] I can equate real and imaginary parts to solve a complex equation or to find an unknown.
- [ ] I can use the conjugate root theorem to find the other roots of a polynomial with real coefficients.
- [ ] I can draw an Argand diagram and find the modulus and argument in the right quadrant.
- [ ] I can multiply and divide in polar or exponential form, using the rules for modulus and argument.
- [ ] I can find the two square roots of a complex number in exact Cartesian form.
- [ ] I can sketch and describe the loci \(|z - a| = k\), \(|z - a| = |z - b|\) and \(\arg(z - a) = \alpha\), and shade a region.
:::

:::recap
- \(i^2 = -1\); \(z = x + iy\) has real part \(x\) and imaginary part \(y\). Multiply out and replace \(i^2\) by \(-1\).
- \(z^* = x - iy\); \(zz^* = x^2 + y^2\). To divide, multiply top and bottom by the conjugate of the denominator.
- Equal complex numbers have equal real parts and equal imaginary parts. Roots of a real polynomial come in conjugate pairs.
- \(|z| = \sqrt{x^2 + y^2}\); \(\arg z\) is the angle from the positive real axis, \(-\pi < \theta \le \pi\). Sketch to find the quadrant.
- \(z = r(\cos\theta + i\sin\theta)\) \(= re^{i\theta}\). Multiply: moduli multiply, arguments add. Divide: moduli divide, arguments subtract.
- Square roots of \(a + bi\): put \((x + iy)^2 = a + bi\) and equate parts.
- Loci: \(|z - a| = k\) circle; \(|z - a| = |z - b|\) perpendicular bisector; \(\arg(z - a) = \alpha\) half-line from \(a\).
:::

:::links
- watch: [Square roots of a complex number](https://www.examsolutions.net/tutorials/square-roots-complex-number/) · ExamSolutions · equating real and imaginary parts
- watch: [Exam questions: loci in the complex plane](https://www.examsolutions.net/tutorials/exam-questions-loci-in-the-complex-plane/) · ExamSolutions · circles, bisectors and half-lines
- watch: [e^(iπ) in 3.14 minutes, using dynamics](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · why re^(iθ) is a point on a circle
- practise: [CAIE Pure 3 Argand diagram exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/complex-numbers/argand-diagrams/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [GeoGebra calculator](https://www.geogebra.org/calculator) · GeoGebra · draw loci and check your sketches
- read: [A visual, intuitive guide to imaginary numbers](https://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/) · BetterExplained · multiplying by i as a rotation

Links checked 3 October 2026.
:::
Next: [Representing and summarising data](#math.s1.data).
