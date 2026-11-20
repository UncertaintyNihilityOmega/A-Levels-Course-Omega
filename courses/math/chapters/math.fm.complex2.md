@chapter math.fm.complex2
@title Roots of unity and complex series
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–7 hours
@summary The equation \(z^n = w\) has exactly \(n\) solutions, and they are the corners of a regular polygon. You will find the \(n\)th roots of unity and of any complex number, use them to factorise \(z^n - 1\) and to get exact trigonometric values, place the vertices of regular polygons, and sum series of sines and cosines by turning them into geometric or binomial series of complex numbers.

:::why
A quadratic has two roots and a cubic three, but \(z^n = 1\) has \(n\) roots and they are all neat: equally spaced points on a circle. That symmetry runs through engineering (a signal split into \(n\) equal phases, the fast Fourier transform that compresses every digital photo and call) and through pure mathematics, where it gives exact values such as \(\cos\dfrac{2\pi}{5} = \dfrac{\sqrt5 - 1}{4}\). The second half of the chapter turns a hard sum of sines and cosines into an easy geometric series.
:::

**Before you start**, you need de Moivre's theorem and the \(z + z^{-1}\) results from [De Moivre's theorem and trigonometry](#math.fm.complex), the sum of a geometric series and the binomial expansion from [Series: binomial expansion and progressions](#math.p1.series), and the roots-and-coefficients relations from [Roots of polynomial equations](#math.fm.roots).

:::try Warm-up
Q: Write down the sum of the first \(n\) terms of the geometric series with first term 1 and common ratio \(r \neq 1\). (from [Series: binomial expansion and progressions](#math.p1.series))
A: \(1 + r + r^2 + \dots + r^{n-1} = \dfrac{r^n - 1}{r - 1}\), which is also \(\dfrac{1 - r^n}{1 - r}\).
Q: Find \((1 + \mathrm{i})^4\), using modulus–argument form. (from [De Moivre's theorem and trigonometry](#math.fm.complex))
A: \(1 + \mathrm{i} = \sqrt2\left(\cos\dfrac\pi4 + \mathrm{i}\sin\dfrac\pi4\right)\), so \((1 + \mathrm{i})^4 = 4(\cos\pi + \mathrm{i}\sin\pi) = -4\).
Q: Write down the sum and the product of the roots of \(z^3 - 8 = 0\). (from [Roots of polynomial equations](#math.fm.roots))
A: There is no \(z^2\) term, so the sum is 0. The product is \(-\dfrac{d}{a} = 8\).
:::

## The \(n\)th roots of unity

The equation \(z^n = 1\) has the obvious solution \(z = 1\). Are there others? Write an unknown solution as \(z = r(\cos\theta + \mathrm{i}\sin\theta)\) and use de Moivre's theorem:
\[r^n(\cos n\theta + \mathrm{i}\sin n\theta) = 1\]
The number 1 has modulus 1 and argument 0, so equate moduli and then arguments. The moduli give \(r^n = 1\), and as \(r > 0\) is real, \(r = 1\). The arguments must be equal **up to a multiple of \(2\pi\)**, because adding a full turn does not change a complex number:
\[n\theta = 2\pi k, \quad\text{so}\quad \theta = \frac{2\pi k}{n}, \quad k \text{ an integer}\]
Different integers \(k\) give different points only until the angle goes once round the circle: \(k = n\) gives the same point as \(k = 0\). So there are exactly \(n\) distinct solutions, \(k = 0, 1, \dots, n - 1\).

:::def \(n\)th roots of unity
The \(n\) solutions of \(z^n = 1\). They are \(\mathrm{e}^{2\pi k\mathrm{i}/n} = \cos\dfrac{2\pi k}{n} + \mathrm{i}\sin\dfrac{2\pi k}{n}\) for \(k = 0, 1, \dots, n - 1\).
:::

:::key Roots of unity
Write \(\omega = \mathrm{e}^{2\pi\mathrm{i}/n}\). The \(n\)th roots of unity are
\[1, \ \omega, \ \omega^2, \ \dots, \ \omega^{n-1}\]
They lie on the unit circle at the corners of a regular \(n\)-sided polygon with one corner at 1, and neighbouring roots are \(\dfrac{2\pi}{n}\) apart. Each root is the previous one multiplied by \(\omega\), which rotates it through \(\dfrac{2\pi}{n}\).
:::

:::html
<figure class="fig small"><svg viewBox="10 20 310 260" role="img" aria-label="An Argand diagram with the unit circle and the six solutions of z to the power 6 equals 1 marked as the corners of a regular hexagon: 1, e to the i pi over 3, e to the 2 i pi over 3, minus 1, e to the minus 2 i pi over 3, and e to the minus i pi over 3. The angle between neighbouring roots is 60 degrees.">
<line class="ln" x1="50.0" y1="150.0" x2="307.0" y2="150.0" marker-end="url(#ah)"/>
<line class="ln" x1="175.0" y1="262.0" x2="175.0" y2="32.0" marker-end="url(#ah)"/>
<circle class="ln-m thin dash" cx="175.0" cy="150.0" r="100.0" fill="none"/>
<polygon class="fm s-acc sw2" points="275.0,150.0 225.0,63.4 125.0,63.4 75.0,150.0 125.0,236.6 225.0,236.6"/>
<line class="ln-m thin" x1="175.0" y1="150.0" x2="275.0" y2="150.0"/>
<line class="ln-m thin" x1="175.0" y1="150.0" x2="225.0" y2="63.4"/>
<line class="ln-m thin" x1="175.0" y1="150.0" x2="125.0" y2="63.4"/>
<line class="ln-m thin" x1="175.0" y1="150.0" x2="75.0" y2="150.0"/>
<line class="ln-m thin" x1="175.0" y1="150.0" x2="125.0" y2="236.6"/>
<line class="ln-m thin" x1="175.0" y1="150.0" x2="225.0" y2="236.6"/>
<circle class="fi" cx="275.0" cy="150.0" r="3.5"/>
<circle class="fi" cx="225.0" cy="63.4" r="3.5"/>
<circle class="fi" cx="125.0" cy="63.4" r="3.5"/>
<circle class="fi" cx="75.0" cy="150.0" r="3.5"/>
<circle class="fi" cx="125.0" cy="236.6" r="3.5"/>
<circle class="fi" cx="225.0" cy="236.6" r="3.5"/>
<path class="ln-m" d="M205.0 150.0A30 30 0 0 0 190.0 124.0" fill="none"/>
<text class="tl tc" x="214.8" y="131.0">π/3</text>
<text class="tl" x="280.0" y="167.0">1</text>
<text class="tl" x="233.0" y="55.4">ω</text>
<text class="tl te" x="119.0" y="55.4">ω²</text>
<text class="tl te" x="71.0" y="142.0">ω³ = −1</text>
<text class="tl te" x="119.0" y="252.6">ω⁴</text>
<text class="tl" x="233.0" y="252.6">ω⁵</text>
<text class="tl te" x="308.0" y="166.0">Re</text>
<text class="tl" x="183.0" y="38.0">Im</text>
</svg><figcaption>The six solutions of \(z^6 = 1\) are the corners of a regular hexagon on the unit circle, with \(\omega = \mathrm{e}^{\mathrm{i}\pi/3}\). Neighbouring roots are \(\pi/3\) apart.</figcaption></figure>
:::

:::warn The \(2\pi k\) is where roots are lost
The step \(n\theta = 2\pi k\) is the heart of the method. A student who writes \(n\theta = 0\) finds only \(z = 1\) and loses the other \(n - 1\) roots. Whenever you equate arguments, add \(2\pi k\) (or \(2k\pi\)) and let \(k\) run through \(n\) consecutive integers.
:::

:::eg Write down the fourth roots of unity in the form \(a + b\mathrm{i}\), and the sixth roots in exponential form with \(-\pi < \theta \leq \pi\).
For \(n = 4\), \(\omega = \mathrm{e}^{\mathrm{i}\pi/2} = \mathrm{i}\), so the roots are \(1, \mathrm{i}, \mathrm{i}^2, \mathrm{i}^3\), that is \(1, \ \mathrm{i}, \ -1, \ -\mathrm{i}\). Each really does satisfy \(z^4 = 1\).

For \(n = 6\) the roots are \(\mathrm{e}^{\mathrm{i}\pi k/3}\) for \(k = 0, \dots, 5\). The arguments \(0, \dfrac\pi3, \dfrac{2\pi}{3}, \pi, \dfrac{4\pi}{3}, \dfrac{5\pi}{3}\) must be brought into \(-\pi < \theta \leq \pi\): subtract \(2\pi\) from the last two. The roots are
\[1, \ \mathrm{e}^{\mathrm{i}\pi/3}, \ \mathrm{e}^{2\mathrm{i}\pi/3}, \ -1, \ \mathrm{e}^{-2\mathrm{i}\pi/3}, \ \mathrm{e}^{-\mathrm{i}\pi/3}\]
:::

### Properties of the roots of unity

Three properties are used again and again.

**Conjugate pairs.** The conjugate of \(\mathrm{e}^{\mathrm{i}\alpha}\) is \(\mathrm{e}^{-\mathrm{i}\alpha}\), so the conjugate of \(\omega^k\) is \(\omega^{-k} = \omega^{n-k}\). The roots (apart from 1, and \(-1\) when \(n\) is even) come in conjugate pairs, which is what we expect: \(z^n - 1\) has real coefficients.

**Powers.** \(\omega^n = 1\), and any power of \(\omega\) is another root: \(\omega^{n+1} = \omega\). So you can reduce a power by subtracting multiples of \(n\) from the exponent.

**The sum is zero.** For \(n \geq 2\),
\[1 + \omega + \omega^2 + \dots + \omega^{n-1} = 0\]

:::eg (Exam style) Let \(\omega = \mathrm{e}^{2\pi\mathrm{i}/n}\) where \(n \geq 2\). Show that \(1 + \omega + \omega^2 + \dots + \omega^{n-1} = 0\). [3]
The left side is a geometric series with first term 1, common ratio \(\omega\) and \(n\) terms: [M1]
\[1 + \omega + \dots + \omega^{n-1} = \frac{\omega^n - 1}{\omega - 1}\] [A1]
Now \(\omega^n = \mathrm{e}^{2\pi\mathrm{i}} = 1\), and \(\omega \neq 1\) because \(n \geq 2\), so the denominator is not zero and the sum is \(\dfrac{0}{\omega - 1} = 0\). [A1]
:::

There is a second reason, which is a good check. The roots of \(z^n - 1 = 0\) add up to \(-\dfrac ba\), and the polynomial has no \(z^{n-1}\) term, so the sum is zero by [Roots of polynomial equations](#math.fm.roots). And a picture explains it: the vectors from the centre to the corners of a regular polygon cancel.

**The cube roots of unity** are the most-used case. Here \(\omega = \mathrm{e}^{2\pi\mathrm{i}/3} = -\dfrac12 + \dfrac{\sqrt3}{2}\mathrm{i}\), and the three roots are \(1\), \(\omega\) and \(\omega^2 = \mathrm{e}^{4\pi\mathrm{i}/3} = -\dfrac12 - \dfrac{\sqrt3}{2}\mathrm{i} = \omega^*\). Their special identities are

:::key The cube roots of unity
\[\omega^3 = 1, \qquad 1 + \omega + \omega^2 = 0, \qquad \omega^2 = \omega^* = \frac1\omega\]
Any power of \(\omega\) reduces by removing multiples of 3 from the exponent: \(\omega^7 = \omega\), \(\omega^8 = \omega^2\).
:::

:::eg Show that \((a + b\omega)(a + b\omega^2) = a^2 - ab + b^2\), where \(\omega\) is a complex cube root of unity, \(\omega \neq 1\), and \(a, b\) are real.
\[\begin{aligned}
(a + b\omega)(a + b\omega^2) &= a^2 + ab\omega^2 + ab\omega + b^2\omega^3 \\
&= a^2 + ab(\omega + \omega^2) + b^2
\end{aligned}\]
Since \(1 + \omega + \omega^2 = 0\), \(\omega + \omega^2 = -1\). Also \(\omega^3 = 1\) was used for the last term. So the product is \(a^2 - ab + b^2\).

**Check** with \(a = 1\), \(b = 1\): \((1 + \omega)(1 + \omega^2) = 1 + \omega + \omega^2 + \omega^3 = 0 + 1 = 1\), and \(1 - 1 + 1 = 1\).
:::

:::warn Which \(\omega\)?
In this chapter \(\omega = \mathrm{e}^{2\pi\mathrm{i}/n}\) for whatever \(n\) the question is about: for cube roots it is \(-\dfrac12 + \dfrac{\sqrt3}{2}\mathrm{i}\), for sixth roots it is \(\mathrm{e}^{\mathrm{i}\pi/3}\). A question will say what \(\omega\) is. Do not carry the value of \(\omega\) from the cube roots into a sixth-root question.
:::

Here are the roots of unity for any \(n\) up to 12. Check that they sum to zero by reading the readout, then set \(n\) to 5 and look at the real parts: they give the exact values you will find later in this chapter.

:::html
<div class="widget" data-w="fm-demoivre" data-mode="roots" data-z="1,0" data-n="5"></div>
:::

## The roots of any complex number

The same method solves \(z^n = w\) for any non-zero \(w\). Write \(w\) in modulus–argument form and, as before, allow for full turns of the argument.

:::key Solving \(z^n = w\)
Let \(w = R(\cos\theta + \mathrm{i}\sin\theta)\). The \(n\) solutions of \(z^n = w\) are
\[z_k = R^{1/n}\left(\cos\frac{\theta + 2\pi k}{n} + \mathrm{i}\sin\frac{\theta + 2\pi k}{n}\right)\]
for \(k = 0, 1, \dots, n - 1\). They lie on the circle of radius \(R^{1/n}\) at the corners of a regular \(n\)-gon, \(\dfrac{2\pi}{n}\) apart, and \(z_k = z_0\omega^k\).
:::

:::steps
1. Write \(w\) in modulus–argument form, \(R\), \(\theta\), with \(\theta\) in \(-\pi < \theta \leq \pi\). Sketch \(w\) to get the quadrant right.
2. The modulus of each root is \(R^{1/n}\) (a positive real \(n\)th root).
3. The argument of the root is \(\dfrac{\theta + 2\pi k}{n}\). Find \(n\) consecutive values of \(k\) that give arguments in \(-\pi < \phi \leq \pi\) (usually \(k = 0, \pm1, \pm2, \dots\), not always \(0\) to \(n - 1\)).
4. Convert to \(a + b\mathrm{i}\) only if asked.
5. Check: the roots are \(\dfrac{2\pi}{n}\) apart and add up to 0.
:::

:::eg Solve \(z^4 = -16\), giving the solutions in the form \(a + b\mathrm{i}\).
\(-16 = 16(\cos\pi + \mathrm{i}\sin\pi)\), so \(R = 16\) and \(\theta = \pi\). Each root has modulus \(16^{1/4} = 2\) and argument \(\dfrac{\pi + 2\pi k}{4}\):

\[\frac\pi4, \quad \frac{3\pi}{4}, \quad \frac{5\pi}{4}, \quad \frac{7\pi}{4} \quad\text{for } k = 0, 1, 2, 3\]
The last two are outside \(-\pi < \phi \leq \pi\): subtract \(2\pi\) to get \(-\dfrac{3\pi}{4}\) and \(-\dfrac\pi4\). Then \(z = 2\left(\cos\phi + \mathrm{i}\sin\phi\right)\) with \(\cos\dfrac\pi4 = \sin\dfrac\pi4 = \dfrac{\sqrt2}{2}\):
\[z = \sqrt2 + \sqrt2\,\mathrm{i}, \quad -\sqrt2 + \sqrt2\,\mathrm{i}, \quad -\sqrt2 - \sqrt2\,\mathrm{i}, \quad \sqrt2 - \sqrt2\,\mathrm{i}\]
**Check**: \(\left(\sqrt2 + \sqrt2\,\mathrm{i}\right)^2 = 2 + 4\mathrm{i} - 2 = 4\mathrm{i}\), and \((4\mathrm{i})^2 = -16\). The four roots are the corners of a square of side \(2\sqrt2\) and they sum to 0.
:::

:::eg Solve \(z^3 = 8\mathrm{i}\), giving the answers in the form \(a + b\mathrm{i}\).
\(8\mathrm{i}\) has modulus 8 and argument \(\dfrac\pi2\). The roots have modulus \(8^{1/3} = 2\) and argument \(\dfrac{\pi/2 + 2\pi k}{3} = \dfrac\pi6 + \dfrac{2\pi k}{3}\). For \(k = 0, 1, -1\) the arguments are \(\dfrac\pi6\), \(\dfrac{5\pi}{6}\) and \(-\dfrac\pi2\); all three are in \(-\pi < \phi \leq \pi\).
\[\begin{aligned}
z_0 &= 2\left(\cos\tfrac\pi6 + \mathrm{i}\sin\tfrac\pi6\right) = \sqrt3 + \mathrm{i} \\
z_1 &= 2\left(\cos\tfrac{5\pi}{6} + \mathrm{i}\sin\tfrac{5\pi}{6}\right) = -\sqrt3 + \mathrm{i} \\
z_{-1} &= 2\left(\cos\left(-\tfrac\pi2\right) + \mathrm{i}\sin\left(-\tfrac\pi2\right)\right) = -2\mathrm{i}
\end{aligned}\]
**Check**: \((-2\mathrm{i})^3 = -8\mathrm{i}^3 = 8\mathrm{i}\), and the three roots sum to \(\sqrt3 - \sqrt3 - 0 + (1 + 1 - 2)\mathrm{i} = 0\).
:::

:::eg (Exam style) Solve the equation \(z^3 = -4 + 4\mathrm{i}\). Give the roots in the form \(r\mathrm{e}^{\mathrm{i}\theta}\), where \(r > 0\) and \(-\pi < \theta \leq \pi\), with \(r\) to 3 significant figures where it is not exact. [5]
The number \(-4 + 4\mathrm{i}\) has modulus \(\sqrt{16 + 16} = 4\sqrt2\) and, in the second quadrant, argument \(\dfrac{3\pi}{4}\). [B1]

The roots have argument \(\dfrac{3\pi/4 + 2\pi k}{3} = \dfrac\pi4 + \dfrac{2\pi k}{3}\). [M1]

The modulus of each root is \(\left(4\sqrt2\right)^{1/3} = \left(2^{5/2}\right)^{1/3} = 2^{5/6} = 1.78\). [A1]

For \(k = 0\) the argument is \(\dfrac\pi4\). [A1] For \(k = 1\) it is \(\dfrac\pi4 + \dfrac{2\pi}{3} = \dfrac{11\pi}{12}\), and for \(k = -1\) it is \(\dfrac\pi4 - \dfrac{2\pi}{3} = -\dfrac{5\pi}{12}\). [A1]
\[z = 1.78\,\mathrm{e}^{\mathrm{i}\pi/4}, \quad 1.78\,\mathrm{e}^{11\mathrm{i}\pi/12}, \quad 1.78\,\mathrm{e}^{-5\mathrm{i}\pi/12}\]
**Check**: the arguments are \(\dfrac{2\pi}{3}\) apart, and cubing the first root gives modulus \(2^{5/2} = 4\sqrt2\) and argument \(\dfrac{3\pi}{4}\).
:::

### Polygons and geometry

Because the roots are equally spaced, they are the corners of a regular polygon, and if you know one root you can find the others by rotating. The roots of \(z^n = w\) are \(z_0, z_0\omega, z_0\omega^2, \dots\): multiply by \(\omega\) to turn through \(\dfrac{2\pi}{n}\) about the centre.

:::eg One cube root of a complex number \(w\) is \(1 + \mathrm{i}\). Find the other two cube roots of \(w\) in the form \(a + b\mathrm{i}\).
The other roots are \((1 + \mathrm{i})\omega\) and \((1 + \mathrm{i})\omega^2\), where \(\omega = -\dfrac12 + \dfrac{\sqrt3}{2}\mathrm{i}\).
\[\begin{aligned}
(1 + \mathrm{i})\omega &= -\tfrac12 - \tfrac{\sqrt3}{2} + \left(\tfrac{\sqrt3}{2} - \tfrac12\right)\mathrm{i} \\
&= -\tfrac{1 + \sqrt3}{2} + \tfrac{\sqrt3 - 1}{2}\mathrm{i} \\[4pt]
(1 + \mathrm{i})\omega^2 &= -\tfrac12 + \tfrac{\sqrt3}{2} - \left(\tfrac{\sqrt3}{2} + \tfrac12\right)\mathrm{i} \\
&= \tfrac{\sqrt3 - 1}{2} - \tfrac{\sqrt3 + 1}{2}\mathrm{i}
\end{aligned}\]
**Check**: the three roots sum to \(0\). The real parts are \(1 - \dfrac{1 + \sqrt3}{2} + \dfrac{\sqrt3 - 1}{2} = 0\) and the imaginary parts are \(1 + \dfrac{\sqrt3 - 1}{2} - \dfrac{\sqrt3 + 1}{2} = 0\). And \(w = (1 + \mathrm{i})^3 = -2 + 2\mathrm{i}\).
:::

If the centre of the polygon is a point \(c\) other than the origin, rotate about \(c\): the vertices are \(c + (z_0 - c)\omega^k\). The distance from the centre to a vertex is \(R = |z_0 - c|\), and two neighbouring vertices are
\[|z_1 - z_0| = R\left|\omega - 1\right| = 2R\sin\frac\pi n\]
apart, because \(\left|\mathrm{e}^{\mathrm{i}\alpha} - 1\right| = 2\sin\dfrac\alpha2\) for \(0 < \alpha < 2\pi\) (shown in the \(C + \mathrm{i}S\) section below). The polygon has area \(\dfrac n2R^2\sin\dfrac{2\pi}{n}\): it is \(n\) triangles, each with two sides \(R\) and angle \(\dfrac{2\pi}{n}\) between them.

:::eg An equilateral triangle \(ABC\) has its centre at the point \(1 + 2\mathrm{i}\) in the Argand diagram and one vertex, \(A\), at \(4 + 6\mathrm{i}\). Find the other two vertices and the area of the triangle.
The centre is \(c = 1 + 2\mathrm{i}\), and \(A - c = 3 + 4\mathrm{i}\), so \(R = 5\). The other vertices are \(c + (3 + 4\mathrm{i})\omega\) and \(c + (3 + 4\mathrm{i})\omega^2\), with \(\omega = -\dfrac12 + \dfrac{\sqrt3}{2}\mathrm{i}\):
\[\begin{aligned}
(3 + 4\mathrm{i})\omega &= -\tfrac32 - 2\sqrt3 + \left(\tfrac{3\sqrt3}{2} - 2\right)\mathrm{i} \\
(3 + 4\mathrm{i})\omega^2 &= -\tfrac32 + 2\sqrt3 - \left(\tfrac{3\sqrt3}{2} + 2\right)\mathrm{i}
\end{aligned}\]
Adding \(c = 1 + 2\mathrm{i}\) to each:
\[\begin{aligned}
B &= \left(-\tfrac12 - 2\sqrt3\right) + \tfrac{3\sqrt3}{2}\mathrm{i} \approx -3.96 + 2.60\mathrm{i} \\
C &= \left(-\tfrac12 + 2\sqrt3\right) - \tfrac{3\sqrt3}{2}\mathrm{i} \approx 2.96 - 2.60\mathrm{i}
\end{aligned}\]
**Check**: the centre is the mean of the vertices, so \(A + B + C = 3c = 3 + 6\mathrm{i}\). The real parts give \(4 - \tfrac12 - 2\sqrt3 - \tfrac12 + 2\sqrt3 = 3\) and the imaginary parts give \(6 + \tfrac{3\sqrt3}{2} - \tfrac{3\sqrt3}{2} = 6\).

The area is \(\dfrac32R^2\sin\dfrac{2\pi}{3} = \dfrac32 \times 25 \times \dfrac{\sqrt3}{2} = \dfrac{75\sqrt3}{4} = 32.5\) (3 s.f.).
:::

:::eg Five wind turbines stand at the corners of a regular pentagon. The centre is at the origin of a map, with distances in metres, one turbine is at the point \(200\) on the real axis, and the map is the Argand diagram. Find the positions of the others, the distance between neighbouring turbines, and the area enclosed by the pentagon.
The turbines are at \(200\,\mathrm{e}^{2\pi k\mathrm{i}/5}\) for \(k = 0, \dots, 4\), that is at
\[200, \quad 200\,\mathrm{e}^{\pm2\pi\mathrm{i}/5}, \quad 200\,\mathrm{e}^{\pm4\pi\mathrm{i}/5}\]
in complex form, which is \(200\), \(61.8 \pm 190.2\mathrm{i}\) and \(-161.8 \pm 117.6\mathrm{i}\) (3 s.f.).

Neighbouring turbines are \(2R\sin\dfrac\pi5 = 400\sin36^\circ = 235\) m apart (3 s.f.).

The area is \(\dfrac52R^2\sin\dfrac{2\pi}{5} = \dfrac52 \times 40\,000 \times \sin72^\circ = 95\,100\,\mathrm{m^2}\) (3 s.f.).
:::

## Factorising \(z^n - 1\) into real factors

The roots of unity give a factorisation of \(z^n - 1\) into linear factors,
\[z^n - 1 = (z - 1)(z - \omega)(z - \omega^2)\dots\left(z - \omega^{n-1}\right)\]
The linear factors with complex roots come in conjugate pairs, and the product of a pair is a **real** quadratic:
\[\left(z - \mathrm{e}^{\mathrm{i}\alpha}\right)\left(z - \mathrm{e}^{-\mathrm{i}\alpha}\right) = z^2 - 2\cos\alpha\,z + 1\]
because the sum of the pair is \(2\cos\alpha\) and their product is \(1\). So every \(z^n - 1\) factorises into real linear and real quadratic factors, with the quadratics \(z^2 - 2\cos\dfrac{2\pi k}{n}z + 1\).

:::eg Factorise \(z^6 - 1\) into real linear and quadratic factors.
The sixth roots are \(1\), \(-1\), \(\mathrm{e}^{\pm\mathrm{i}\pi/3}\) and \(\mathrm{e}^{\pm2\mathrm{i}\pi/3}\). The real roots give \((z - 1)(z + 1)\). The pair with \(\alpha = \dfrac\pi3\) gives \(z^2 - 2\cos\dfrac\pi3z + 1 = z^2 - z + 1\), and the pair with \(\alpha = \dfrac{2\pi}{3}\) gives \(z^2 - 2\cos\dfrac{2\pi}{3}z + 1 = z^2 + z + 1\). So
\[z^6 - 1 = (z - 1)(z + 1)\left(z^2 - z + 1\right)\left(z^2 + z + 1\right)\]
**Check** with \(z = 2\): \(63 = 1 \times 3 \times 3 \times 7\).
:::

:::eg (Exam style) (a) Find the roots of \(z^5 = 1\). [2] (b) Show that \(z^5 - 1 = (z - 1)Q_1(z)Q_2(z)\), where \(Q_1(z) = z^2 - 2\cos\dfrac{2\pi}{5}z + 1\) and \(Q_2(z) = z^2 - 2\cos\dfrac{4\pi}{5}z + 1\). [3] (c) Hence show that \(\cos\dfrac{2\pi}{5} = \dfrac{\sqrt5 - 1}{4}\). [6]
**(a)** \(z = \mathrm{e}^{2\pi k\mathrm{i}/5}\) for \(k = 0, \pm1, \pm2\). [M1]

The roots are \(1\), \(\mathrm{e}^{\pm2\pi\mathrm{i}/5}\) and \(\mathrm{e}^{\pm4\pi\mathrm{i}/5}\). [A1]

**(b)** The factors for the conjugate pairs are \(\left(z - \mathrm{e}^{\mathrm{i}\alpha}\right)\left(z - \mathrm{e}^{-\mathrm{i}\alpha}\right)\). [M1]
\[= z^2 - \left(\mathrm{e}^{\mathrm{i}\alpha} + \mathrm{e}^{-\mathrm{i}\alpha}\right)z + 1 = z^2 - 2\cos\alpha\,z + 1\] [M1]
With \(\alpha = \dfrac{2\pi}{5}\) and \(\alpha = \dfrac{4\pi}{5}\), together with \(z - 1\) for the root 1, this gives the factorisation. [A1]

**(c)** Let \(p = \cos\dfrac{2\pi}{5} + \cos\dfrac{4\pi}{5}\) and \(q = \cos\dfrac{2\pi}{5}\cos\dfrac{4\pi}{5}\). The two quadratics multiply to
\[z^4 - 2pz^3 + (2 + 4q)z^2 - 2pz + 1\] [M1]
and multiplying by \(z - 1\) gives
\[z^5 - (2p + 1)z^4 + (2 + 4q + 2p)z^3 - \dots\]
This must equal \(z^5 - 1\), which has no \(z^4\) or \(z^3\) term. [M1]

Comparing the \(z^4\) terms, \(2p + 1 = 0\), so \(p = -\dfrac12\). Then the \(z^3\) terms give \(2 + 4q + 2p = 0\), so \(q = -\dfrac14\). [A1]

The two cosines are the roots of \(x^2 - px + q = 0\), that is \(4x^2 + 2x - 1 = 0\), so
\[x = \frac{-2 \pm \sqrt{4 + 16}}{8} = \frac{-1 \pm \sqrt5}{4}\] [M1 A1]
Since \(\dfrac{2\pi}{5}\) is in the first quadrant, \(\cos\dfrac{2\pi}{5} > 0\), so \(\cos\dfrac{2\pi}{5} = \dfrac{\sqrt5 - 1}{4}\) (and \(\cos\dfrac{4\pi}{5} = -\dfrac{\sqrt5 + 1}{4}\)). [A1]
**Check**: \(\cos72^\circ = 0.3090\) and \(\dfrac{\sqrt5 - 1}{4} = 0.3090\).
:::

## Equations that reduce to roots of unity

Many equations are roots of unity in disguise. A ratio such as \(\dfrac{z + 1}{z}\) is a new variable, and if its \(n\)th power is 1 then it is an \(n\)th root of unity. The next two examples are built from \((z + 1)^n = z^n\).

:::eg Solve \((z + 1)^4 = z^4\) and show that all the roots have real part \(-\dfrac12\).
\(z = 0\) is not a solution, so divide by \(z^4\): \(\left(\dfrac{z + 1}{z}\right)^4 = 1\). Therefore \(\dfrac{z + 1}{z}\) is a fourth root of unity: \(1, \mathrm{i}, -1, -\mathrm{i}\).

\(\dfrac{z + 1}{z} = 1\) has no solution, because it gives \(1 + \dfrac1z = 1\), that is \(\dfrac1z = 0\). The equation \((z + 1)^4 = z^4\) has the \(z^4\) terms cancelling, so it has degree 3, and three roots.

Put \(\dfrac{z + 1}{z} = u\): \(1 + \dfrac1z = u\) so \(z = \dfrac{1}{u - 1}\).
\[\begin{aligned}
u = \mathrm{i}: \quad z &= \frac{1}{\mathrm{i} - 1} = \frac{-1 - \mathrm{i}}{2} \\
u = -1: \quad z &= \frac{1}{-2} = -\frac12 \\
u = -\mathrm{i}: \quad z &= \frac{1}{-\mathrm{i} - 1} = \frac{-1 + \mathrm{i}}{2}
\end{aligned}\]
Every root has real part \(-\dfrac12\), so they lie on a vertical line, not on a circle.
:::

The pattern is general, and a half-angle step makes the answer trigonometric.

:::eg (Exam style) Show that the roots of \((z + 1)^6 = z^6\) are \(z = -\dfrac12 - \dfrac12\mathrm{i}\cot\dfrac{k\pi}{6}\) for \(k = 1, 2, 3, 4, 5\). [6]
\(z = 0\) is not a root, so divide by \(z^6\): [B1]
\[\left(\frac{z + 1}{z}\right)^6 = 1\]
So \(\dfrac{z + 1}{z} = \mathrm{e}^{2\pi k\mathrm{i}/6} = \mathrm{e}^{k\pi\mathrm{i}/3}\) for some \(k\), and \(z = \dfrac{1}{\mathrm{e}^{k\pi\mathrm{i}/3} - 1}\). [M1]

Use \(\mathrm{e}^{\mathrm{i}\alpha} - 1 = \mathrm{e}^{\mathrm{i}\alpha/2}\left(\mathrm{e}^{\mathrm{i}\alpha/2} - \mathrm{e}^{-\mathrm{i}\alpha/2}\right) = 2\mathrm{i}\sin\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\) with \(\alpha = \dfrac{k\pi}{3}\): [M1]
\[z = \frac{\mathrm{e}^{-\mathrm{i}k\pi/6}}{2\mathrm{i}\sin\dfrac{k\pi}{6}} = \frac{\cos\dfrac{k\pi}{6} - \mathrm{i}\sin\dfrac{k\pi}{6}}{2\mathrm{i}\sin\dfrac{k\pi}{6}}\] [M1]
Divide each term of the numerator by the denominator; \(\dfrac{1}{\mathrm{i}} = -\mathrm{i}\):
\[z = \frac{-\mathrm{i}\cot\dfrac{k\pi}{6}}{2} - \frac12 = -\frac12 - \frac12\mathrm{i}\cot\frac{k\pi}{6}\] [A1]
The value \(k = 0\) is excluded because it gives \(\dfrac{z + 1}{z} = 1\), which has no solution (and \(\cot0\) is undefined). So \(k = 1, \dots, 5\). [A1]
**Check** with \(k = 3\): \(\cot\dfrac\pi2 = 0\), so \(z = -\dfrac12\), and \(\left(\dfrac12\right)^6 = \left(-\dfrac12\right)^6\) ✓.
:::

## Summing series: the \(C + \mathrm{i}S\) method

A sum such as \(\cos\theta + \cos2\theta + \dots + \cos n\theta\) has no easy real method. The idea is to add an imaginary partner. If \(C\) is the sum of the cosines and \(S\) the sum of the matching sines, then \(C + \mathrm{i}S\) is a sum of terms \(\cos r\theta + \mathrm{i}\sin r\theta = \mathrm{e}^{\mathrm{i}r\theta} = z^r\) with \(z = \mathrm{e}^{\mathrm{i}\theta}\): a **geometric series** (or a **binomial** one). Sum it, then take real and imaginary parts.

:::steps
1. Define \(C\) as the sum you want and \(S\) as the same sum with sine in place of cosine (or the reverse).
2. Form \(C + \mathrm{i}S\) and write each term as a power of \(z = \mathrm{e}^{\mathrm{i}\theta}\) (or \(\cos r\theta + \mathrm{i}\sin r\theta\)).
3. Sum it: a geometric series with ratio \(z\), or a binomial expansion \((1 + z)^n\) if there are binomial coefficients.
4. Simplify with the half-angle step: \(\mathrm{e}^{\mathrm{i}\alpha} - 1 = 2\mathrm{i}\sin\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\) and \(\mathrm{e}^{\mathrm{i}\alpha} + 1 = 2\cos\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\).
5. Take the real part for \(C\) and the imaginary part for \(S\).
:::

The half-angle step makes the fraction real up to a phase. It uses \(\mathrm{e}^{\mathrm{i}\alpha/2} - \mathrm{e}^{-\mathrm{i}\alpha/2} = 2\mathrm{i}\sin\dfrac\alpha2\), the \(z - z^{-1}\) result of [De Moivre's theorem and trigonometry](#math.fm.complex).

:::eg Show that \(\displaystyle\sum_{r=0}^{n-1}\mathrm{e}^{\mathrm{i}r\theta} = \mathrm{e}^{\mathrm{i}(n-1)\theta/2}\,\frac{\sin\frac{n\theta}{2}}{\sin\frac\theta2}\), and hence find \(\displaystyle\sum_{r=0}^{n-1}\cos r\theta\) and \(\displaystyle\sum_{r=0}^{n-1}\sin r\theta\). Assume \(\theta\) is not a multiple of \(2\pi\).
The series is geometric with first term 1 and ratio \(z = \mathrm{e}^{\mathrm{i}\theta}\), and \(z \neq 1\):
\[\sum_{r=0}^{n-1}z^r = \frac{z^n - 1}{z - 1} = \frac{\mathrm{e}^{\mathrm{i}n\theta} - 1}{\mathrm{e}^{\mathrm{i}\theta} - 1}\]
Use the half-angle step on top and bottom:
\[\frac{2\mathrm{i}\sin\frac{n\theta}{2}\,\mathrm{e}^{\mathrm{i}n\theta/2}}{2\mathrm{i}\sin\frac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}} = \mathrm{e}^{\mathrm{i}(n-1)\theta/2}\,\frac{\sin\frac{n\theta}{2}}{\sin\frac\theta2}\]
The factor \(\dfrac{\sin(n\theta/2)}{\sin(\theta/2)}\) is real, so the real part is \(\cos\dfrac{(n-1)\theta}{2}\) times it and the imaginary part is \(\sin\dfrac{(n-1)\theta}{2}\) times it:
\[\sum_{r=0}^{n-1}\cos r\theta = \frac{\cos\frac{(n-1)\theta}{2}\sin\frac{n\theta}{2}}{\sin\frac\theta2}, \qquad \sum_{r=0}^{n-1}\sin r\theta = \frac{\sin\frac{(n-1)\theta}{2}\sin\frac{n\theta}{2}}{\sin\frac\theta2}\]
**Check** with \(n = 4\) and \(\theta = \dfrac\pi3\): the cosines are \(1 + \tfrac12 - \tfrac12 - 1 = 0\) and the formula gives \(\dfrac{\cos\frac\pi2\sin\frac{2\pi}{3}}{\sin\frac\pi6} = 0\). The sines are \(0 + \tfrac{\sqrt3}{2} + \tfrac{\sqrt3}{2} + 0 = \sqrt3\) and the formula gives \(\dfrac{1 \times \frac{\sqrt3}{2}}{\frac12} = \sqrt3\).
:::

Putting \(\theta = \dfrac{2\pi}{n}\) makes \(\sin\dfrac{n\theta}{2} = \sin\pi = 0\), so the sum is 0: the sum of the \(n\)th roots of unity again. The modulus of the half-angle step is also a **distance**: \(\left|\mathrm{e}^{\mathrm{i}\theta} - 1\right| = \left|2\mathrm{i}\sin\dfrac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}\right| = 2\sin\dfrac\theta2\) for \(0 < \theta < 2\pi\), which is the chord formula used for the polygon above.

:::eg (Exam style) (a) By considering \(\displaystyle\sum_{r=1}^n\mathrm{e}^{\mathrm{i}(2r-1)\theta}\), show that \(\cos\theta + \cos3\theta + \dots + \cos(2n - 1)\theta = \dfrac{\sin2n\theta}{2\sin\theta}\), where \(\sin\theta \neq 0\). [6] (b) Hence find \(\displaystyle\sum_{r=1}^{10}\cos\frac{(2r - 1)\pi}{21}\). [2]
**(a)** Let \(C = \displaystyle\sum_{r=1}^n\cos(2r - 1)\theta\) and \(S = \displaystyle\sum_{r=1}^n\sin(2r - 1)\theta\). Then \(C + \mathrm{i}S = \displaystyle\sum_{r=1}^n\mathrm{e}^{\mathrm{i}(2r-1)\theta}\). [B1]

This is a geometric series with first term \(\mathrm{e}^{\mathrm{i}\theta}\), ratio \(\mathrm{e}^{2\mathrm{i}\theta}\) and \(n\) terms: [M1]
\[C + \mathrm{i}S = \mathrm{e}^{\mathrm{i}\theta}\,\frac{\mathrm{e}^{2\mathrm{i}n\theta} - 1}{\mathrm{e}^{2\mathrm{i}\theta} - 1}\] [A1]
Apply the half-angle step: \(\mathrm{e}^{2\mathrm{i}n\theta} - 1 = 2\mathrm{i}\sin n\theta\,\mathrm{e}^{\mathrm{i}n\theta}\) and \(\mathrm{e}^{2\mathrm{i}\theta} - 1 = 2\mathrm{i}\sin\theta\,\mathrm{e}^{\mathrm{i}\theta}\). [M1]
\[C + \mathrm{i}S = \mathrm{e}^{\mathrm{i}\theta}\,\frac{2\mathrm{i}\sin n\theta\,\mathrm{e}^{\mathrm{i}n\theta}}{2\mathrm{i}\sin\theta\,\mathrm{e}^{\mathrm{i}\theta}} = \frac{\sin n\theta}{\sin\theta}\,\mathrm{e}^{\mathrm{i}n\theta}\] [A1]
Take the real part: \(C = \dfrac{\sin n\theta\cos n\theta}{\sin\theta} = \dfrac{\sin2n\theta}{2\sin\theta}\). [A1]

**(b)** The sum has \(n = 10\) and \(\theta = \dfrac\pi{21}\), so it equals \(\dfrac{\sin\dfrac{20\pi}{21}}{2\sin\dfrac\pi{21}}\). [M1]

Since \(\sin\dfrac{20\pi}{21} = \sin\left(\pi - \dfrac\pi{21}\right) = \sin\dfrac\pi{21}\), the sum is \(\dfrac12\). [A1]
**Check**: the imaginary part gives \(S = \dfrac{\sin^2n\theta}{\sin\theta}\), so \(C^2 + S^2 = \dfrac{\sin^2 n\theta}{\sin^2\theta}\), the squared modulus of the geometric sum.
:::

### Binomial series

When the terms carry binomial coefficients, \(\binom nr\), the sum \(\displaystyle\sum\binom nr z^r\) is \((1 + z)^n\) by the binomial theorem, and the half-angle step is \(1 + \mathrm{e}^{\mathrm{i}\theta} = 2\cos\dfrac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}\).

:::eg (Exam style) (a) Show that \(\displaystyle\sum_{r=0}^n\binom nr\sin r\theta = 2^n\cos^n\frac\theta2\,\sin\frac{n\theta}{2}\). [5] (b) Hence find \(\displaystyle\sum_{r=0}^5\binom5r\sin\frac{r\pi}{2}\). [2]
**(a)** Let \(C = \displaystyle\sum_{r=0}^n\binom nr\cos r\theta\) and \(S = \displaystyle\sum_{r=0}^n\binom nr\sin r\theta\). Then \(C + \mathrm{i}S = \displaystyle\sum_{r=0}^n\binom nr\mathrm{e}^{\mathrm{i}r\theta}\). [B1]

By the binomial theorem this is
\[C + \mathrm{i}S = \left(1 + \mathrm{e}^{\mathrm{i}\theta}\right)^n\] [M1]
Now \(1 + \mathrm{e}^{\mathrm{i}\theta} = \mathrm{e}^{\mathrm{i}\theta/2}\left(\mathrm{e}^{-\mathrm{i}\theta/2} + \mathrm{e}^{\mathrm{i}\theta/2}\right) = 2\cos\dfrac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}\), so [M1]
\[C + \mathrm{i}S = 2^n\cos^n\frac\theta2\,\mathrm{e}^{\mathrm{i}n\theta/2}\] [A1]
The imaginary part is \(S = 2^n\cos^n\dfrac\theta2\sin\dfrac{n\theta}{2}\). [A1]

**(b)** With \(n = 5\) and \(\theta = \dfrac\pi2\): \(S = 2^5\cos^5\dfrac\pi4\sin\dfrac{5\pi}{4} = 32 \times \left(\dfrac{\sqrt2}{2}\right)^5 \times \left(-\dfrac{\sqrt2}{2}\right)\) [M1]
\[= -32 \times \left(\frac{\sqrt2}{2}\right)^6 = -32 \times \frac18 = -4\] [A1]
**Check** term by term: the terms are \(5\), \(0\), \(-10\), \(0\) and \(1\), and they add to \(-4\).
:::

The real part of the same expansion gives \(\displaystyle\sum_{r=0}^n\binom nr\cos r\theta = 2^n\cos^n\dfrac\theta2\cos\dfrac{n\theta}{2}\).

### Infinite series

A geometric series converges when the ratio has modulus less than 1. The ratio here is \(\dfrac z2\), with \(|z| = 1\), so \(\left|\dfrac z2\right| = \dfrac12 < 1\), and the sum to infinity \(\dfrac{1}{1 - \text{ratio}}\) works exactly as for real numbers (MF19 gives \(S_\infty\)).

:::eg Find \(\displaystyle\sum_{r=0}^\infty\left(\tfrac12\right)^r\cos r\theta\).
Let \(C\) be the sum and \(S = \displaystyle\sum_{r=0}^\infty\left(\tfrac12\right)^r\sin r\theta\). With \(z = \mathrm{e}^{\mathrm{i}\theta}\),
\[C + \mathrm{i}S = \sum_{r=0}^\infty\left(\frac z2\right)^r = \frac{1}{1 - \frac z2} = \frac{2}{2 - \mathrm{e}^{\mathrm{i}\theta}}\]
because \(\left|\dfrac z2\right| = \dfrac12 < 1\). Multiply the top and bottom by the conjugate of the denominator, \(2 - \cos\theta + \mathrm{i}\sin\theta\):
\[C + \mathrm{i}S = \frac{2(2 - \cos\theta + \mathrm{i}\sin\theta)}{(2 - \cos\theta)^2 + \sin^2\theta} = \frac{2(2 - \cos\theta + \mathrm{i}\sin\theta)}{5 - 4\cos\theta}\]
Taking the real part:
\[C = \frac{2(2 - \cos\theta)}{5 - 4\cos\theta} = \frac{4 - 2\cos\theta}{5 - 4\cos\theta}\]
and the imaginary part is \(S = \dfrac{2\sin\theta}{5 - 4\cos\theta}\).

**Check**: for \(\theta = 0\) the sum is \(1 + \tfrac12 + \tfrac14 + \dots = 2\), and \(C = \dfrac{2}{1} = 2\). For \(\theta = \pi\) it is \(1 - \tfrac12 + \tfrac14 - \dots = \tfrac23\), and \(C = \dfrac{6}{9} = \tfrac23\).
:::

:::eg Five identical sources send out waves that are each \(\theta\) out of phase with the one before, so the waves are \(\cos(\omega t + r\theta)\) for \(r = 0, 1, 2, 3, 4\). The resultant is the real part of \(\mathrm{e}^{\mathrm{i}\omega t}\displaystyle\sum_{r=0}^4\mathrm{e}^{\mathrm{i}r\theta}\), and its amplitude is the modulus of that sum, \(\left|\dfrac{\sin\frac{5\theta}{2}}{\sin\frac\theta2}\right|\). Find the amplitude of the resultant when (a) \(\theta = 30^\circ\), (b) \(\theta = 72^\circ\).
(a) \(\dfrac{\sin75^\circ}{\sin15^\circ} = \dfrac{0.9659}{0.2588} = 3.73\) (3 s.f.). The waves reinforce each other (five equal waves in step would give 5).

(b) \(\theta = 72^\circ = \dfrac{2\pi}{5}\), so \(\dfrac{5\theta}{2} = 180^\circ\) and \(\sin180^\circ = 0\). The amplitude is 0: the waves cancel completely. This is the sum of the fifth roots of unity, \(1 + \omega + \omega^2 + \omega^3 + \omega^4 = 0\): the five phasors form a regular pentagon and return to the start.
:::

:::exam What MF19 gives you, and what it does not
MF19 gives the sum of a geometric series, including \(S_\infty\), and the binomial expansion, so quote them. It does not give de Moivre's theorem, the formula for the roots of \(z^n = w\), \(z^n \pm z^{-n}\) or the half-angle steps for \(\mathrm{e}^{\mathrm{i}\theta} \pm 1\): learn them. In "find the roots" questions give every root, in the form asked (check the interval for the argument), and keep \(\pi\) and surds exact. In sum questions show the line \(C + \mathrm{i}S = \dots\): it earns a mark, and it tells the examiner the method.
:::

:::board
In UK Further Maths (Edexcel, AQA and OCR) the \(n\)th roots of a complex number and their place as the corners of a regular polygon are core content, as here. The \(C + \mathrm{i}S\) summation method is also met there.
:::

:::eg Spot the error: show that \(1 + \cos\theta + \cos2\theta + \cos3\theta = \dfrac{\cos\frac{3\theta}{2}\sin2\theta}{\sin\frac\theta2}\), for 4 marks.
A student wrote this answer.

Line 1: \(C + \mathrm{i}S = 1 + z + z^2 + z^3 = \dfrac{z^4 - 1}{z - 1}\), where \(z = \mathrm{e}^{\mathrm{i}\theta}\)
Line 2: \(= \dfrac{2\mathrm{i}\sin2\theta}{2\mathrm{i}\sin\frac\theta2}\)
Line 3: \(= \dfrac{\sin2\theta}{\sin\frac\theta2}\), which is real, so \(C = \dfrac{\sin2\theta}{\sin\frac\theta2}\)

Line 1 is the correct start. [M1]

**Line 2 uses the right idea but drops the phase factors.** [M1] [A0] \(z^4 - 1 = \mathrm{e}^{4\mathrm{i}\theta} - 1 = 2\mathrm{i}\sin2\theta\,\mathrm{e}^{2\mathrm{i}\theta}\) and \(z - 1 = 2\mathrm{i}\sin\dfrac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}\). The student left out \(\mathrm{e}^{2\mathrm{i}\theta}\) and \(\mathrm{e}^{\mathrm{i}\theta/2}\). Their sum is real, so \(S = 0\), which cannot be right: \(\sin\theta + \sin2\theta + \sin3\theta\) is positive for small \(\theta\). The student scores 2 out of 4 and does not reach the result.

Correct line 2: \(\dfrac{2\mathrm{i}\sin2\theta\,\mathrm{e}^{2\mathrm{i}\theta}}{2\mathrm{i}\sin\frac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}} = \dfrac{\sin2\theta}{\sin\frac\theta2}\mathrm{e}^{3\mathrm{i}\theta/2}\). [A1]
Line 3: the real part is \(\dfrac{\sin2\theta}{\sin\frac\theta2}\cos\dfrac{3\theta}{2}\), as required. [A1]

**Check** with \(\theta = \dfrac\pi3\): the sum is \(1 + \tfrac12 - \tfrac12 - 1 = 0\). The correct formula gives \(\dfrac{\cos\frac\pi2\sin\frac{2\pi}{3}}{\sin\frac\pi6} = 0\), but the student's formula gives \(\dfrac{\sin\frac{2\pi}{3}}{\sin\frac\pi6} = \sqrt3\).
:::

:::try Start easy, finish at exam standard
Q: Write down all the solutions of \(z^8 = 1\) in exponential form, and say which are real.
A: \(z = \mathrm{e}^{2\pi k\mathrm{i}/8} = \mathrm{e}^{k\pi\mathrm{i}/4}\) for \(k = 0, \pm1, \pm2, \pm3, 4\). The real ones are \(k = 0\) and \(k = 4\): \(z = 1\) and \(z = -1\).
Q: \(\omega = \mathrm{e}^{2\pi\mathrm{i}/3}\). Simplify \(\omega^{7} + \omega^{5}\).
A: \(\omega^7 = \omega\) (since \(\omega^3 = 1\)) and \(\omega^5 = \omega^2\), so \(\omega^7 + \omega^5 = \omega + \omega^2 = -1\).
Q: Solve \(z^3 = -27\), giving answers in the form \(a + b\mathrm{i}\).
A: \(-27 = 27(\cos\pi + \mathrm{i}\sin\pi)\), so \(z = 3\,\mathrm{e}^{\mathrm{i}(\pi + 2\pi k)/3}\), and \(k = 0, 1, -1\) give arguments \(\dfrac\pi3, \pi, -\dfrac\pi3\): \(z = \dfrac32 + \dfrac{3\sqrt3}{2}\mathrm{i}\), \(-3\), \(\dfrac32 - \dfrac{3\sqrt3}{2}\mathrm{i}\).
Q: Solve \(z^4 = 8(-1 + \sqrt3\,\mathrm{i})\), giving the roots in the form \(r\mathrm{e}^{\mathrm{i}\theta}\) with \(-\pi < \theta \leq \pi\).
A: The modulus of \(-1 + \sqrt3\,\mathrm{i}\) is 2 and its argument is \(\dfrac{2\pi}{3}\), so \(w\) has modulus 16. The roots have modulus 2 and argument \(\dfrac{2\pi/3 + 2\pi k}{4} = \dfrac\pi6 + \dfrac{\pi k}{2}\). For \(k = 0, 1, -1, -2\): \(2\mathrm{e}^{\mathrm{i}\pi/6}\), \(2\mathrm{e}^{2\mathrm{i}\pi/3}\), \(2\mathrm{e}^{-\mathrm{i}\pi/3}\), \(2\mathrm{e}^{-5\mathrm{i}\pi/6}\).
Q: Write down the value of \(\cos\dfrac{2\pi}{7} + \cos\dfrac{4\pi}{7} + \cos\dfrac{6\pi}{7}\).
A: The seventh roots of unity sum to 0. Their real parts are \(1\) and \(\cos\dfrac{2\pi k}{7}\) for \(k = 1, \dots, 6\), which come in equal pairs (\(k\) and \(7 - k\)): \(1 + 2\left(\cos\dfrac{2\pi}{7} + \cos\dfrac{4\pi}{7} + \cos\dfrac{6\pi}{7}\right) = 0\). The sum is \(-\dfrac12\).
Q: Factorise \(z^4 - 1\) into real factors, and solve \(z^4 = 1\).
A: \(z^4 - 1 = (z - 1)(z + 1)\left(z^2 + 1\right)\), from the roots \(\pm1\) and \(\pm\mathrm{i}\) (the pair \(\pm\mathrm{i}\) gives \(z^2 - 2\cos\dfrac\pi2z + 1 = z^2 + 1\)). The solutions are \(1, -1, \mathrm{i}, -\mathrm{i}\).
Q: Solve \(z^4 + z^2 + 1 = 0\), giving the roots in exponential form.
A: Put \(u = z^2\): \(u^2 + u + 1 = 0\), so \(u = \mathrm{e}^{\pm2\pi\mathrm{i}/3}\) (the complex cube roots of unity). Then \(z = \pm\mathrm{e}^{\pm\mathrm{i}\pi/3}\), that is \(\mathrm{e}^{\mathrm{i}\pi/3}\), \(\mathrm{e}^{-\mathrm{i}\pi/3}\), \(\mathrm{e}^{2\mathrm{i}\pi/3}\), \(\mathrm{e}^{-2\mathrm{i}\pi/3}\).
Q: A regular hexagon has its centre at the origin and one vertex at 4. Write down the other vertices and the length of a side.
A: The vertices are \(4\mathrm{e}^{\mathrm{i}\pi k/3}\): \(4\), \(2 + 2\sqrt3\,\mathrm{i}\), \(-2 + 2\sqrt3\,\mathrm{i}\), \(-4\), \(-2 - 2\sqrt3\,\mathrm{i}\), \(2 - 2\sqrt3\,\mathrm{i}\). The side is \(2 \times 4\sin\dfrac\pi6 = 4\).
Q: Find \(\displaystyle\sum_{r=0}^\infty\left(\tfrac13\right)^r\sin r\theta\).
A: \(C + \mathrm{i}S = \dfrac{1}{1 - \frac z3} = \dfrac{3}{3 - \mathrm{e}^{\mathrm{i}\theta}} = \dfrac{3(3 - \cos\theta + \mathrm{i}\sin\theta)}{10 - 6\cos\theta}\). The imaginary part is \(S = \dfrac{3\sin\theta}{10 - 6\cos\theta}\).
Q: Evaluate \(\displaystyle\sum_{r=0}^4\binom4r\cos\frac{r\pi}{2}\), using the real part of \(\left(1 + \mathrm{e}^{\mathrm{i}\theta}\right)^4\).
A: \(C = 2^4\cos^4\dfrac\theta2\cos\dfrac{4\theta}{2}\) with \(\theta = \dfrac\pi2\): \(16 \times \left(\dfrac{\sqrt2}{2}\right)^4 \times \cos\pi = 16 \times \dfrac14 \times (-1) = -4\). Direct: \(1 + 0 - 6 + 0 + 1 = -4\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Solve \(z^6 = 1\), giving the solutions in the form \(\mathrm{e}^{\mathrm{i}\theta}\) with \(-\pi < \theta \leq \pi\).
A: \(z = \mathrm{e}^{2\pi k\mathrm{i}/6}\). [M1] The arguments are \(\dfrac{k\pi}{3}\) for six consecutive integers \(k\). [A1] \(z = 1, \mathrm{e}^{\pm\mathrm{i}\pi/3}, \mathrm{e}^{\pm2\mathrm{i}\pi/3}, -1\). [A1]
Q: [5 marks] ★★ Solve \(z^3 = -27\mathrm{i}\), giving the roots in the form \(r\mathrm{e}^{\mathrm{i}\theta}\) with \(r > 0\) and \(-\pi < \theta \leq \pi\).
A: \(|{-27\mathrm{i}}| = 27\) and \(\arg = -\dfrac\pi2\). [B1] The roots have argument \(\dfrac{-\pi/2 + 2\pi k}{3}\). [M1] The modulus is \(27^{1/3} = 3\). [A1] For \(k = 0\): \(-\dfrac\pi6\). [A1] For \(k = 1\): \(\dfrac\pi2\) and for \(k = -1\): \(-\dfrac{5\pi}{6}\). [A1] The roots are \(3\mathrm{e}^{-\mathrm{i}\pi/6}\), \(3\mathrm{e}^{\mathrm{i}\pi/2}\), \(3\mathrm{e}^{-5\mathrm{i}\pi/6}\).
Q: [5 marks] ★★ Let \(\omega = \mathrm{e}^{2\pi\mathrm{i}/5}\). (a) Show that \(1 + \omega + \omega^2 + \omega^3 + \omega^4 = 0\). (b) Hence show that \(\cos\dfrac{2\pi}{5} + \cos\dfrac{4\pi}{5} = -\dfrac12\).
A: (a) The sum is geometric: \(\dfrac{\omega^5 - 1}{\omega - 1}\) [M1] \(= 0\), because \(\omega^5 = 1\) and \(\omega \neq 1\). [A1]
(b) Take real parts:
\[1 + \cos\frac{2\pi}{5} + \cos\frac{4\pi}{5} + \cos\frac{6\pi}{5} + \cos\frac{8\pi}{5} = 0\] [M1]
Now \(\cos\dfrac{6\pi}{5} = \cos\dfrac{4\pi}{5}\) and \(\cos\dfrac{8\pi}{5} = \cos\dfrac{2\pi}{5}\). [M1] So \(1 + 2\left(\cos\dfrac{2\pi}{5} + \cos\dfrac{4\pi}{5}\right) = 0\), which gives the result. [A1]
Q: [6 marks] ★★ A regular pentagon has its centre at the origin of an Argand diagram and one vertex at \(4\). (a) Write down the complex numbers representing the other four vertices. (b) Find the length of a side, giving your answer to 3 significant figures. (c) Find the area of the pentagon, to 3 significant figures.
A: (a) The vertices are \(4\mathrm{e}^{2\pi k\mathrm{i}/5}\) for \(k = 1, \dots, 4\), that is \(4\mathrm{e}^{\pm2\pi\mathrm{i}/5}\) and \(4\mathrm{e}^{\pm4\pi\mathrm{i}/5}\). [B1]
(b) The side is \(\left|4\mathrm{e}^{2\pi\mathrm{i}/5} - 4\right| = 4\left|\mathrm{e}^{\mathrm{i}\alpha} - 1\right|\) with \(\alpha = \dfrac{2\pi}{5}\). [M1] \(= 8\sin\dfrac\pi5\) [M1] \(= 4.70\). [A1]
(c) The area is \(5 \times \tfrac12 \times 4^2 \times \sin\dfrac{2\pi}{5}\) [M1] \(= 38.0\). [A1]
Q: [7 marks] ★★ (a) Find the roots of \(z^6 = 1\) and hence factorise \(z^6 - 1\) into real linear and quadratic factors. (b) Hence solve \(z^4 + z^2 + 1 = 0\), giving the roots in exponential form.
A: (a) The roots are \(\mathrm{e}^{\mathrm{i}k\pi/3}\) for \(k = 0, \pm1, \pm2, 3\). [B1] The conjugate pairs give \(z^2 - 2\cos\alpha\,z + 1\). [M1] With \(\alpha = \dfrac\pi3\) and \(\dfrac{2\pi}{3}\) these are \(z^2 - z + 1\) and \(z^2 + z + 1\). [A1] So
\[z^6 - 1 = (z - 1)(z + 1)\left(z^2 - z + 1\right)\left(z^2 + z + 1\right)\] [A1]
(b) \(z^6 - 1 = \left(z^2 - 1\right)\left(z^4 + z^2 + 1\right)\), so \(z^4 + z^2 + 1 = \left(z^2 - z + 1\right)\left(z^2 + z + 1\right)\). [M1 M1] The roots are those of the two quadratics: \(\mathrm{e}^{\pm\mathrm{i}\pi/3}\) and \(\mathrm{e}^{\pm2\mathrm{i}\pi/3}\). [A1]
Q: [8 marks] ★★ (a) Show that \(\displaystyle\sum_{r=0}^\infty\left(\tfrac14\right)^r\cos r\theta = \dfrac{4(4 - \cos\theta)}{17 - 8\cos\theta}\) and find the sum of \(\displaystyle\sum_{r=0}^\infty\left(\tfrac14\right)^r\sin r\theta\). (b) Hence find \(\displaystyle\sum_{r=0}^\infty\left(\tfrac14\right)^r\sin\dfrac{r\pi}{2}\).
A: (a) \(C + \mathrm{i}S = \displaystyle\sum_{r=0}^\infty\left(\dfrac{\mathrm{e}^{\mathrm{i}\theta}}{4}\right)^r\). [M1] The ratio has modulus \(\dfrac14 < 1\), so the series converges. [B1] The sum is \(\dfrac{1}{1 - \frac14\mathrm{e}^{\mathrm{i}\theta}} = \dfrac{4}{4 - \mathrm{e}^{\mathrm{i}\theta}}\). [M1] Multiply by the conjugate: \(\dfrac{4(4 - \cos\theta + \mathrm{i}\sin\theta)}{17 - 8\cos\theta}\). [M1] The real part is \(\dfrac{4(4 - \cos\theta)}{17 - 8\cos\theta}\) [A1] and the imaginary part is \(\dfrac{4\sin\theta}{17 - 8\cos\theta}\). [A1]
(b) Put \(\theta = \dfrac\pi2\) in the imaginary part: \(\dfrac{4 \times 1}{17 - 0}\) [M1] \(= \dfrac{4}{17}\). [A1]
Q: [10 marks] (#math.fm.roots) ★★★ (a) Show that the roots of \(z^6 + z^5 + z^4 + z^3 + z^2 + z + 1 = 0\) are \(\mathrm{e}^{2\pi k\mathrm{i}/7}\) for \(k = 1, 2, \dots, 6\). (b) Use the substitution \(w = z + \dfrac1z\) to show that the equation becomes \(w^3 + w^2 - 2w - 1 = 0\). (c) Hence find the exact values of \(\cos\dfrac{2\pi}{7} + \cos\dfrac{4\pi}{7} + \cos\dfrac{6\pi}{7}\) and \(\cos\dfrac{2\pi}{7}\cos\dfrac{4\pi}{7}\cos\dfrac{6\pi}{7}\).
H: Multiply the equation by \(z - 1\). Is \(z = 1\) a root of the original equation?
H: Divide by \(z^3\), and use \(z^3 + z^{-3} = w^3 - 3w\) and \(z^2 + z^{-2} = w^2 - 2\).
H: The values of \(w\) are \(2\cos\dfrac{2\pi k}{7}\). Which \(k\) give different values? Use the sum and the product of the roots of the cubic.
A: (a) Multiplying by \(z - 1\) gives \(z^7 - 1 = 0\), so \(z = \mathrm{e}^{2\pi k\mathrm{i}/7}\). [M1] \(z = 1\) does not satisfy the original equation (the left side is 7), so \(k = 1, \dots, 6\). [A1 A1]
(b) Divide by \(z^3\): \(z^3 + z^{-3} + z^2 + z^{-2} + z + z^{-1} + 1 = 0\). [M1] With \(z^3 + z^{-3} = w^3 - 3w\) and \(z^2 + z^{-2} = w^2 - 2\): [M1] \(w^3 - 3w + w^2 - 2 + w + 1 = 0\), which is \(w^3 + w^2 - 2w - 1 = 0\). [A1]
(c) For \(z = \mathrm{e}^{\mathrm{i}\alpha}\), \(w = 2\cos\alpha\), and \(k\) and \(7 - k\) give the same \(w\). So the roots of the cubic are \(2\cos\dfrac{2\pi}{7}\), \(2\cos\dfrac{4\pi}{7}\), \(2\cos\dfrac{6\pi}{7}\). [B1] Their sum is \(-1\), so \(\cos\dfrac{2\pi}{7} + \cos\dfrac{4\pi}{7} + \cos\dfrac{6\pi}{7} = -\dfrac12\). [M1 A1] Their product is \(-\dfrac{d}{a} = 1\), so \(8\cos\dfrac{2\pi}{7}\cos\dfrac{4\pi}{7}\cos\dfrac{6\pi}{7} = 1\) and the product of the cosines is \(\dfrac18\). [A1]
Q: [8 marks] ★★★ (a) Use the expansion of \(\left(1 - \mathrm{e}^{\mathrm{i}\theta}\right)^4\) to show that
\[1 - 4\cos\theta + 6\cos2\theta - 4\cos3\theta + \cos4\theta = 16\sin^4\frac\theta2\cos2\theta\]
(b) Hence find the value of the left side when \(\theta = \dfrac\pi2\).
H: The binomial coefficients are 1, 4, 6, 4, 1 and the signs alternate: \(\sum\binom4r(-1)^rz^r = (1 - z)^4\).
H: \(1 - \mathrm{e}^{\mathrm{i}\theta} = -2\mathrm{i}\sin\dfrac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}\). What is \((-2\mathrm{i})^4\)?
A: (a) \(C + \mathrm{i}S = \displaystyle\sum_{r=0}^4(-1)^r\binom4r\mathrm{e}^{\mathrm{i}r\theta} = \left(1 - \mathrm{e}^{\mathrm{i}\theta}\right)^4\). [B1] \(1 - \mathrm{e}^{\mathrm{i}\theta} = \mathrm{e}^{\mathrm{i}\theta/2}\left(\mathrm{e}^{-\mathrm{i}\theta/2} - \mathrm{e}^{\mathrm{i}\theta/2}\right) = -2\mathrm{i}\sin\dfrac\theta2\,\mathrm{e}^{\mathrm{i}\theta/2}\). [M1 A1] Raise to the power 4: \((-2\mathrm{i})^4 = 16\), so \(C + \mathrm{i}S = 16\sin^4\dfrac\theta2\,\mathrm{e}^{2\mathrm{i}\theta}\). [M1 A1] The real part is \(C = 16\sin^4\dfrac\theta2\cos2\theta\). [A1]
(b) \(16\sin^4\dfrac\pi4\cos\pi = 16 \times \dfrac14 \times (-1) = -4\). [M1 A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ The \(n\)th roots of unity are \(1, \omega, \dots, \omega^{n-1}\) where \(\omega = \mathrm{e}^{2\pi\mathrm{i}/n}\). (a) By considering \(\dfrac{z^n - 1}{z - 1}\), show that \(\displaystyle\prod_{k=1}^{n-1}\left(1 - \omega^k\right) = n\). (b) Explain why \(\left|1 - \omega^k\right|\) is the distance from the vertex 1 to the vertex \(\omega^k\) of the polygon, and deduce that the product of the distances from one vertex of a regular \(n\)-gon inscribed in a unit circle to all the other vertices is \(n\). (c) Show that \(\left|1 - \omega^k\right| = 2\sin\dfrac{k\pi}{n}\), and hence find the exact value of \(\sin\dfrac\pi6\sin\dfrac{2\pi}{6}\sin\dfrac{3\pi}{6}\sin\dfrac{4\pi}{6}\sin\dfrac{5\pi}{6}\).
H: \(z^n - 1 = (z - 1)\prod_{k=1}^{n-1}(z - \omega^k)\). Also \(\dfrac{z^n - 1}{z - 1} = 1 + z + \dots + z^{n-1}\).
H: Put \(z = 1\) in both forms.
H: \(\mathrm{e}^{\mathrm{i}\alpha} - 1 = 2\mathrm{i}\sin\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\).
A: (a) \(z^n - 1 = (z - 1)\prod_{k=1}^{n-1}(z - \omega^k)\), so \(1 + z + \dots + z^{n-1} = \prod_{k=1}^{n-1}(z - \omega^k)\). [M1 M1] At \(z = 1\) the left side is \(n\), so \(\prod_{k=1}^{n-1}\left(1 - \omega^k\right) = n\). [A1]
(b) The distance between the points \(1\) and \(\omega^k\) in the Argand diagram is \(\left|\omega^k - 1\right|\), which is \(\left|1 - \omega^k\right|\). [B1] Take the modulus of the product in (a): \(\prod\left|1 - \omega^k\right| = n\), the product of the distances. [A1]
(c) \(\left|\mathrm{e}^{\mathrm{i}\alpha} - 1\right| = \left|2\mathrm{i}\sin\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\right| = 2\sin\dfrac\alpha2\) with \(\alpha = \dfrac{2k\pi}{n}\), giving \(2\sin\dfrac{k\pi}{n}\). [M1] So \(\prod_{k=1}^{n-1}2\sin\dfrac{k\pi}{n} = n\), and \(\prod\sin\dfrac{k\pi}{n} = \dfrac{n}{2^{n-1}}\). [M1] For \(n = 6\): \(\dfrac{6}{32} = \dfrac{3}{16}\). [A1]
Q: [4 marks] ★★★ Show that the sum of the squares of the distances from one vertex of a regular \(n\)-gon inscribed in the unit circle to all the \(n\) vertices (including itself) is \(2n\).
H: The squared distance is \(\left|1 - \omega^k\right|^2 = \left(1 - \omega^k\right)\left(1 - \omega^{-k}\right)\).
A: \(\left|1 - \omega^k\right|^2 = 2 - \omega^k - \omega^{-k} = 2 - 2\cos\dfrac{2\pi k}{n}\). [M1] Sum over \(k = 0, \dots, n - 1\): \(2n - 2\sum_{k=0}^{n-1}\cos\dfrac{2\pi k}{n}\). [M1] The cosines are the real parts of the \(n\)th roots of unity, which add to 0, so their sum is 0. [M1] The total is \(2n\). [A1]
:::

:::quiz
? How many solutions does \(z^5 = 1\) have, and where are they?
+ five, at the corners of a regular pentagon on the unit circle, with one at 1
- five, all on the real axis
- one, \(z = 1\)
- two, \(z = 1\) and \(z = -1\)
> A degree-5 equation has five roots, counting complex ones. They all have modulus 1 and arguments \(\dfrac{2\pi k}{5}\). A student who writes the argument equation as \(5\theta = 0\) misses the \(2\pi k\) and finds only \(z = 1\).
? What is \(1 + \omega + \omega^2 + \dots + \omega^{n-1}\), where \(\omega = \mathrm{e}^{2\pi\mathrm{i}/n}\) and \(n \geq 2\)?
+ \(0\)
- \(1\)
- \(n\)
- \(-1\)
> The sum is \(\dfrac{\omega^n - 1}{\omega - 1} = 0\) because \(\omega^n = 1\). The value \(n\) is what you get if you put \(\omega = 1\) in each term, but \(\omega \neq 1\).
? Which of these is a solution of \(z^3 = -1\)?
+ \(\mathrm{e}^{\mathrm{i}\pi/3}\)
- \(\mathrm{e}^{2\mathrm{i}\pi/3}\)
- \(\mathrm{e}^{\mathrm{i}\pi/6}\)
- \(\mathrm{e}^{-\mathrm{i}\pi/6}\)
> The arguments of the solutions are \(\dfrac{\pi + 2\pi k}{3}\): \(\dfrac\pi3\), \(\pi\) and \(-\dfrac\pi3\). The number \(\mathrm{e}^{2\mathrm{i}\pi/3}\) cubes to \(1\), not \(-1\); the others have the wrong argument after cubing.
? When you solve \(z^n = w\), how many different values of \(k\) do you use in \(\dfrac{\theta + 2\pi k}{n}\)?
+ \(n\), consecutive integers
- \(n + 1\)
- \(n - 1\), because \(k = 0\) gives the same root as the original
- as many as you like, since every \(k\) gives a different root
> There are \(n\) roots. Using \(n + 1\) values repeats the first root, and using only \(n - 1\) loses one. After \(n\) steps the argument has turned through \(2\pi\) and the roots repeat.
? \(\left(z - \mathrm{e}^{\mathrm{i}\alpha}\right)\left(z - \mathrm{e}^{-\mathrm{i}\alpha}\right)\) equals
+ \(z^2 - 2\cos\alpha\,z + 1\)
- \(z^2 - 2\sin\alpha\,z + 1\)
- \(z^2 - 2\cos\alpha\,z - 1\)
- \(z^2 + 1\)
> The sum of the pair is \(2\cos\alpha\) and the product is \(\mathrm{e}^{\mathrm{i}\alpha}\mathrm{e}^{-\mathrm{i}\alpha} = 1\). The choice with \(-1\) takes the product as \(-1\); \(z^2 + 1\) is only the case \(\alpha = \dfrac\pi2\).
? To sum \(\displaystyle\sum_{r=1}^n\cos r\theta\) by the \(C + \mathrm{i}S\) method you
+ form \(C + \mathrm{i}S = \displaystyle\sum_{r=1}^n\mathrm{e}^{\mathrm{i}r\theta}\), sum the geometric series and take the real part
- add \(\cos r\theta + \sin r\theta\) for each term and sum directly
- multiply \(C\) by \(S\)
- take the imaginary part of the sum
> The sum of cosines is the **real** part of the geometric series \(\sum\mathrm{e}^{\mathrm{i}r\theta}\); the sines are its imaginary part. \(C\) and \(S\) are added with a factor of \(\mathrm{i}\), never multiplied or combined without it.
? The solutions of \(z^n = w\) are separated, in argument, by
+ \(\dfrac{2\pi}{n}\)
- \(\dfrac\pi n\)
- \(2\pi\)
- \(n\)
> Each root is the previous one multiplied by \(\omega = \mathrm{e}^{2\pi\mathrm{i}/n}\), a rotation of \(\dfrac{2\pi}{n}\). \(\dfrac\pi n\) is half that gap, and \(2\pi\) is a whole turn.
:::

:::checklist What you can now do
- [ ] I can find the \(n\)th roots of unity, write them in exponential form and sketch them as a regular polygon.
- [ ] I can show that the \(n\)th roots of unity sum to zero, and use \(1 + \omega + \omega^2 = 0\) for the cube roots.
- [ ] I can solve \(z^n = w\) for any complex number \(w\), giving every root with its argument in \(-\pi < \theta \leq \pi\).
- [ ] I can use one root and the rotation \(\omega\) to find the other roots, and find the vertices, side and area of a regular polygon.
- [ ] I can factorise \(z^n - 1\) into real linear and quadratic factors and use the factorisation to find exact trigonometric values.
- [ ] I can solve equations such as \((z + 1)^n = z^n\) by reducing them to roots of unity.
- [ ] I can sum a finite series of sines or cosines by the \(C + \mathrm{i}S\) method with a geometric series and the half-angle step.
- [ ] I can sum a series such as \(\displaystyle\sum\binom nr\sin r\theta\) using the binomial theorem, and an infinite series with ratio of modulus less than 1.
:::

:::recap
- \(z^n = 1\) has \(n\) roots \(\mathrm{e}^{2\pi k\mathrm{i}/n}\), \(k = 0, \dots, n - 1\): the corners of a regular \(n\)-gon on the unit circle; neighbours are \(\dfrac{2\pi}{n}\) apart.
- They sum to 0 (geometric series); for the cube roots \(1 + \omega + \omega^2 = 0\), \(\omega^3 = 1\), \(\omega^2 = \omega^*\).
- \(z^n = w = R\,\mathrm{e}^{\mathrm{i}\theta}\): \(z_k = R^{1/n}\mathrm{e}^{\mathrm{i}(\theta + 2\pi k)/n}\); choose \(n\) consecutive \(k\) so the arguments are in \((-\pi, \pi]\); \(z_k = z_0\omega^k\).
- Polygon with centre \(c\): vertices \(c + (z_0 - c)\omega^k\); side \(2R\sin\dfrac\pi n\); area \(\dfrac n2R^2\sin\dfrac{2\pi}{n}\).
- \(z^n - 1 = (z - 1)\prod\left(z^2 - 2\cos\dfrac{2\pi k}{n}z + 1\right)\) (with \(z + 1\) too when \(n\) is even); compare coefficients for exact cosines.
- \((z + 1)^n = z^n\): divide by \(z^n\) and put \(\dfrac{z + 1}{z} = \mathrm{e}^{2\pi k\mathrm{i}/n}\), \(k \neq 0\).
- \(C + \mathrm{i}S\): sum \(\sum\mathrm{e}^{\mathrm{i}r\theta}\) as a geometric or binomial series, use \(\mathrm{e}^{\mathrm{i}\alpha} \mp 1 = 2\mathrm{i}\sin\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\) or \(2\cos\dfrac\alpha2\,\mathrm{e}^{\mathrm{i}\alpha/2}\), then take the real and imaginary parts.
- \(\displaystyle\sum_{r=0}^n\binom nr\mathrm{e}^{\mathrm{i}r\theta} = 2^n\cos^n\dfrac\theta2\,\mathrm{e}^{\mathrm{i}n\theta/2}\).
:::

:::links
- watch: [De Moivre's theorem](https://www.examsolutions.net/tutorials/de-moivres-theorem/) · ExamSolutions · includes roots of complex numbers, worked step by step
- watch: [Euler's formula with introductory group theory](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · why the roots of unity are rotations
- read: [Intuitive understanding of Euler's formula](https://betterexplained.com/articles/intuitive-understanding-of-eulers-formula/) · BetterExplained · \(\mathrm{e}^{\mathrm{i}\theta}\) as a point on the unit circle
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · the complex-numbers booklets include roots and series, with answers
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Three equations, three planes](#math.fm.systems) turns to systems of linear equations, and uses the rank of a matrix to say when three planes meet in a point, a line or not at all.
