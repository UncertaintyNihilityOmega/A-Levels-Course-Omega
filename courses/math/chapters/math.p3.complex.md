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
(a) Expand: \((a + ib)(1 + 2i) = a + 2ai + bi + 2bi^2 = (a - 2b) + (2a + b)i\). Equate real parts: \(a - 2b = 5\); imaginary parts: \(2a + b = 5\). Solving: \(a = 3\), \(b = -1\).

(b) Let \(z = x + iy\), so \(z^* = x - iy\). Then \(z + 2z^* = 3x - iy\). Equating: \(3x = 6\) and \(-y = -4\), so \(z = 2 + 4i\).
:::

## Roots of polynomials

Using \(i\), every quadratic can be solved. When the discriminant is negative, the roots are complex, and they come as a **conjugate pair**.

:::key Conjugate pairs
If a polynomial has **real** coefficients and \(a + ib\) is a root, then its conjugate \(a - ib\) is also a root. The two roots give the real quadratic factor
\[(z - (a + ib))(z - (a - ib)) = z^2 - 2az + (a^2 + b^2)\]
:::

:::eg (a) Solve \(z^2 - 4z + 13 = 0\). (b) Given that \(2 + i\) is a root of \(z^3 - 6z^2 + 13z - 10 = 0\), find the other roots.
(a) By the quadratic formula, \(z = \dfrac{4 \pm \sqrt{16 - 52}}{2} = \dfrac{4 \pm \sqrt{-36}}{2} = 2 \pm 3i\).

(b) The coefficients are real, so \(2 - i\) is also a root. The quadratic factor is \(z^2 - 4z + 5\) (sum of roots \(4\), product \(2^2 + 1^2 = 5\)). Divide: \(z^3 - 6z^2 + 13z - 10 = (z - 2)(z^2 - 4z + 5)\). The roots are \(2\), \(2 + i\) and \(2 - i\).
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
(a) \(|z| = \sqrt{1 + 3} = 2\). The point is in the second quadrant; the acute angle is \(\tan^{-1}\sqrt3 = \tfrac\pi3\), so \(\arg z = \pi - \tfrac\pi3 = \tfrac{2\pi}3\) (\(2.09\) to 3 s.f.).
(b) \(|z| = \sqrt{4 + 4} = 2\sqrt2\). The point is in the third quadrant; the acute angle is \(\tfrac\pi4\), so \(\arg z = -\left(\pi - \tfrac\pi4\right) = -\tfrac{3\pi}4\) (\(-2.36\) to 3 s.f.).
:::

## Polar and exponential form

If \(|z| = r\) and \(\arg z = \theta\), then \(x = r\cos\theta\) and \(y = r\sin\theta\), so
\[z = r(\cos\theta + i\sin\theta) = re^{i\theta}\]
This is the **modulus–argument form** (polar form), and the second expression is the **exponential form**.
Multiplying in polar form is simple, because the angles behave like indices:

:::key Multiplying and dividing in polar form
\[|z_1z_2| = |z_1||z_2| \qquad \arg(z_1z_2) = \arg z_1 + \arg z_2\]
\[\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|} \qquad \arg\frac{z_1}{z_2} = \arg z_1 - \arg z_2\]
In exponential form: \(r_1e^{i\theta_1}\times r_2e^{i\theta_2} = r_1r_2e^{i(\theta_1 + \theta_2)}\).
:::

Multiplication by a complex number **scales** by its modulus and **rotates** by its argument. In particular, multiplying by \(i\) (modulus 1, argument \(\tfrac\pi2\)) rotates a point through a quarter turn anticlockwise. Taking the conjugate reflects the point in the real axis.

:::eg Let \(z_1 = 1 + i\) and \(z_2 = -1 + \sqrt3\,i\). Find the modulus and argument of \(z_1z_2\) and of \(\dfrac{z_1}{z_2}\).
\(|z_1| = \sqrt2\), \(\arg z_1 = \tfrac\pi4\); \(|z_2| = 2\), \(\arg z_2 = \tfrac{2\pi}3\).
\(|z_1z_2| = 2\sqrt2\) and \(\arg(z_1z_2) = \tfrac\pi4 + \tfrac{2\pi}3 = \tfrac{11\pi}{12}\) (\(2.88\)).
\(\left|\dfrac{z_1}{z_2}\right| = \dfrac{\sqrt2}2\) and \(\arg\dfrac{z_1}{z_2} = \tfrac\pi4 - \tfrac{2\pi}3 = -\tfrac{5\pi}{12}\) (\(-1.31\)).
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
\(\dfrac1Z = \dfrac{Z_1 + Z_2}{Z_1Z_2}\), so \(Z = \dfrac{Z_1Z_2}{Z_1 + Z_2}\). Now \(Z_1Z_2 = (3 + 4i)(1 - 2i) = 3 - 6i + 4i - 8i^2 = 11 - 2i\), and \(Z_1 + Z_2 = 4 + 2i\).
\[Z = \frac{11 - 2i}{4 + 2i} = \frac{(11 - 2i)(4 - 2i)}{16 + 4} = \frac{44 - 22i - 8i + 4i^2}{20} = \frac{40 - 30i}{20} = 2 - 1.5i\]
The modulus is \(|Z| = \sqrt{4 + 2.25} = 2.5\) ohms, and the argument is \(\tan^{-1}\left(-\tfrac{1.5}{2}\right) = -0.644\) radians (3 s.f.). The modulus is the size of the opposition to the current; the argument is the phase difference between voltage and current.
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
A: \(8 - 2i + 12i - 3i^2 = 8 + 10i + 3 = 11 + 10i\).
Q: Express \(\dfrac{7 + i}{1 + i}\) in the form \(x + iy\).
A: \(\dfrac{(7 + i)(1 - i)}{(1 + i)(1 - i)} = \dfrac{7 - 7i + i - i^2}{2} = \dfrac{8 - 6i}{2} = 4 - 3i\).
Q: Solve \(z^2 + 2z + 10 = 0\).
A: \(z = \dfrac{-2 \pm \sqrt{4 - 40}}{2} = \dfrac{-2 \pm 6i}{2} = -1 \pm 3i\).
Q: Find the modulus and the argument (in radians, 3 s.f.) of \(-\sqrt3 - i\).
A: \(|z| = \sqrt{3 + 1} = 2\). The point is in the third quadrant, the acute angle is \(\tan^{-1}\tfrac{1}{\sqrt3} = \tfrac\pi6\), so \(\arg z = -\left(\pi - \tfrac\pi6\right) = -\tfrac{5\pi}{6} = -2.62\).
Q: Find the square roots of \(8 + 6i\).
A: \(x^2 - y^2 = 8\) and \(xy = 3\), so \(x^4 - 8x^2 - 9 = 0\), \((x^2 - 9)(x^2 + 1) = 0\), \(x = \pm3\), \(y = \pm1\). The roots are \(\pm(3 + i)\).
Q: Given \(z_1 = 3e^{i\pi/6}\) and \(z_2 = 2e^{i\pi/3}\), find \(z_1z_2\) and \(\dfrac{z_1}{z_2}\) in modulus–argument form, and write \(z_1z_2\) in the form \(x + iy\).
A: \(z_1z_2 = 6e^{i\pi/2} = 6i\). \(\dfrac{z_1}{z_2} = \tfrac32e^{-i\pi/6}\).
Q: Solve \(z + 2z^* = 9 - 2i\), giving \(z\) in the form \(x + iy\).
A: With \(z = x + iy\): \(3x - iy = 9 - 2i\), so \(x = 3\) and \(y = 2\); \(z = 3 + 2i\).
Q: Describe the locus \(|z - 2| = |z + 2i|\) and find its Cartesian equation.
A: The perpendicular bisector of the points \(2\) and \(-2i\). \((x - 2)^2 + y^2 = x^2 + (y + 2)^2\) gives \(-4x + 4 = 4y + 4\), so \(y = -x\).
Q: (Exam style) Show that \(z = 3\) is a root of \(z^3 - 5z^2 + 11z - 15 = 0\), and find the other two roots.
A: \(27 - 45 + 33 - 15 = 0\) ✓. Divide by \(z - 3\): \(z^3 - 5z^2 + 11z - 15 = (z - 3)(z^2 - 2z + 5)\). Then \(z^2 - 2z + 5 = 0\) gives \(z = \dfrac{2 \pm \sqrt{4 - 20}}{2} = 1 \pm 2i\). The roots are \(3\), \(1 + 2i\) and \(1 - 2i\).
:::

:::quiz
? What is \((1 + i)^2\)?
- \(2\)
+ \(2i\)
- \(1 + i\)
- \(0\)
> \((1 + i)^2 = 1 + 2i + i^2 = 1 + 2i - 1 = 2i\).
? If \(z = 3 - 4i\), what is \(zz^*\)?
- \(-7\)
- \(7\)
+ \(25\)
- \(9 + 16i\)
> \(zz^* = (3 - 4i)(3 + 4i) = 9 + 16 = 25 = |z|^2\), always real and non-negative.
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

:::recap
- \(i^2 = -1\); \(z = x + iy\) has real part \(x\) and imaginary part \(y\). Multiply out and replace \(i^2\) by \(-1\).
- \(z^* = x - iy\); \(zz^* = x^2 + y^2\). To divide, multiply top and bottom by the conjugate of the denominator.
- Equal complex numbers have equal real parts and equal imaginary parts. Roots of a real polynomial come in conjugate pairs.
- \(|z| = \sqrt{x^2 + y^2}\); \(\arg z\) is the angle from the positive real axis, \(-\pi < \theta \le \pi\). Sketch to find the quadrant.
- \(z = r(\cos\theta + i\sin\theta) = re^{i\theta}\). Multiply: moduli multiply, arguments add. Divide: moduli divide, arguments subtract.
- Square roots of \(a + bi\): put \((x + iy)^2 = a + bi\) and equate parts.
- Loci: \(|z - a| = k\) circle; \(|z - a| = |z - b|\) perpendicular bisector; \(\arg(z - a) = \alpha\) half-line from \(a\).
:::

:::note Learn more online
- **Watch:** [Square roots of a complex number](https://www.examsolutions.net/tutorials/square-roots-complex-number/) · ExamSolutions · equating real and imaginary parts
- **Watch:** [Exam questions: loci in the complex plane](https://www.examsolutions.net/tutorials/exam-questions-loci-in-the-complex-plane/) · ExamSolutions · circles, bisectors and half-lines
- **Watch:** [e^(iπ) in 3.14 minutes, using dynamics](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · why re^(iθ) is a point on a circle
- **Practise:** [CAIE Pure 3 Argand diagram exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/complex-numbers/argand-diagrams/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [GeoGebra calculator](https://www.geogebra.org/calculator) · GeoGebra · draw loci and check your sketches
- **Read:** [A visual, intuitive guide to imaginary numbers](https://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/) · BetterExplained · multiplying by i as a rotation

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Representing and summarising data](#math.s1.data).
