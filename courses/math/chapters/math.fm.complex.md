@chapter math.fm.complex
@title De Moivre's theorem and trigonometry
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary De Moivre's theorem says that \((\cos\theta + \mathrm{i}\sin\theta)^n = \cos n\theta + \mathrm{i}\sin n\theta\). You will see why it is true, prove it by induction, use it to find powers of complex numbers, and use it to write \(\cos 5\theta\) or \(\tan 5\theta\) in powers of \(\cos\theta\) or \(\tan\theta\), and powers such as \(\sin^6\theta\) in multiple angles. These identities then give integrals and exact trigonometric values.

:::why
Multiplying complex numbers adds their angles. That one fact turns a long calculation, such as raising \(1 - \mathrm{i}\) to the power 10, into a single rotation. It also links two parts of mathematics that look unrelated: powers of complex numbers and the trigonometry of multiple angles. Engineers use it for alternating currents and signals, and in Paper 2 it gives some of the most reliable marks, because the method is the same every time.
:::

**Before you start**, you need modulus–argument and exponential form from [Complex numbers](#math.p3.complex), the binomial expansion from [Series: binomial expansion and progressions](#math.p1.series), the compound angle formulae from [Further trigonometry](#math.p3.trig), and the structure of a proof by induction from [Proof by induction](#math.fm.induction).

:::try Warm-up
Q: Write \(1 + \sqrt3\,\mathrm{i}\) in the form \(r(\cos\theta + \mathrm{i}\sin\theta)\). (from [Complex numbers](#math.p3.complex))
A: \(r = \sqrt{1 + 3} = 2\) and \(\tan\theta = \sqrt3\) in the first quadrant, so \(\theta = \dfrac\pi3\): \(2\left(\cos\dfrac\pi3 + \mathrm{i}\sin\dfrac\pi3\right)\).
Q: Expand \((1 + x)^5\). (from [Series: binomial expansion and progressions](#math.p1.series))
A: The coefficients are \(1, 5, 10, 10, 5, 1\), so \((1 + x)^5 = 1 + 5x + 10x^2 + 10x^3 + 5x^4 + x^5\).
Q: Write down \(\cos(A + B)\) and \(\sin(A + B)\). (from [Further trigonometry](#math.p3.trig))
A: \(\cos(A + B) = \cos A\cos B - \sin A\sin B\) and \(\sin(A + B) = \sin A\cos B + \cos A\sin B\).
:::

## What de Moivre's theorem says

In [Complex numbers](#math.p3.complex) you saw that multiplying two complex numbers multiplies their moduli and adds their arguments. Multiply a number by itself again and again and the same thing happens each time: the modulus is multiplied by \(r\) and the argument grows by \(\theta\). After \(n\) multiplications the modulus is \(r^n\) and the argument is \(n\theta\). That is the whole theorem. It is named after the French-born mathematician Abraham de Moivre (1667–1754).

:::key De Moivre's theorem
For every integer \(n\),
\[(\cos\theta + \mathrm{i}\sin\theta)^n = \cos n\theta + \mathrm{i}\sin n\theta\]
In exponential form, \(\left(\mathrm{e}^{\mathrm{i}\theta}\right)^n = \mathrm{e}^{\mathrm{i}n\theta}\). For a general complex number \(z = r(\cos\theta + \mathrm{i}\sin\theta)\),
\[z^n = r^n(\cos n\theta + \mathrm{i}\sin n\theta)\]
so \(|z^n| = |z|^n\) and \(\arg z^n = n\arg z\), after adding or subtracting multiples of \(2\pi\) to bring the argument into \(-\pi < \arg z^n \leq \pi\).
:::

:::def Principal argument
The argument \(\theta\) of a non-zero complex number that lies in the interval \(-\pi < \theta \leq \pi\). Any \(\theta + 2k\pi\), for an integer \(k\), points the same way, but 9231 answers use the principal value unless the question says otherwise.
:::

:::def Multiple-angle formula
A formula that writes \(\cos n\theta\), \(\sin n\theta\) or \(\tan n\theta\) as an expression in \(\cos\theta\), \(\sin\theta\) or \(\tan\theta\). For example \(\cos3\theta = 4\cos^3\theta - 3\cos\theta\).
:::

The picture shows what happens on the unit circle. Multiplying by \(z = \cos\theta + \mathrm{i}\sin\theta\) rotates a point through \(\theta\) anticlockwise and does not change its distance from \(O\). Starting at 1 and multiplying again and again gives \(z\), \(z^2\), \(z^3\), each a further turn of \(\theta\).

:::html
<figure class="fig small"><svg viewBox="20 20 270 260" role="img" aria-label="An Argand diagram with the unit circle. The point z on the circle makes an angle theta of 50 degrees with the real axis. The points z squared and z cubed lie on the same circle at angles 2 theta and 3 theta, each one a further rotation by theta. The point z to the power minus one lies at angle minus theta, below the real axis.">
<line class="ln" x1="32.0" y1="150.0" x2="272.0" y2="150.0" marker-end="url(#ah)"/>
<line class="ln" x1="150.0" y1="262.0" x2="150.0" y2="32.0" marker-end="url(#ah)"/>
<circle class="ln-m thin dash" cx="150.0" cy="150.0" r="100.0" fill="none"/>
<line class="c1" x1="150.0" y1="150.0" x2="214.3" y2="73.4"/>
<line class="c1" x1="150.0" y1="150.0" x2="132.6" y2="51.5"/>
<line class="c1" x1="150.0" y1="150.0" x2="63.4" y2="100.0"/>
<line class="c3 dash" x1="150.0" y1="150.0" x2="214.3" y2="226.6"/>
<circle class="fi" cx="214.3" cy="73.4" r="3.5"/>
<circle class="fi" cx="132.6" cy="51.5" r="3.5"/>
<circle class="fi" cx="63.4" cy="100.0" r="3.5"/>
<circle class="fi" cx="214.3" cy="226.6" r="3.5"/>
<path class="ln-m" d="M184.0 150.0A34 34 0 0 0 171.9 124.0" fill="none"/>
<path class="ln-m" d="M171.9 124.0A34 34 0 0 0 144.1 116.5" fill="none"/>
<path class="ln-m" d="M144.1 116.5A34 34 0 0 0 120.6 133.0" fill="none"/>
<path class="ln-m" d="M184.0 150.0A34 34 0 0 1 171.9 176.0" fill="none"/>
<text class="tl tc" x="198.9" y="131.2">θ</text>
<text class="tl tc" x="164.0" y="101.8">θ</text>
<text class="tl tc" x="119.0" y="109.8">θ</text>
<text class="tl tc" x="198.9" y="176.8">−θ</text>
<text class="tl" x="222.3" y="73.4">z</text>
<text class="tl te" x="128.6" y="45.5">z²</text>
<text class="tl te" x="59.4" y="96.0">z³</text>
<text class="tl" x="222.3" y="238.6">z⁻¹</text>
<text class="tl te" x="273.0" y="166.0">Re</text>
<text class="tl" x="158.0" y="38.0">Im</text>
<text class="tl tc" x="250.0" y="164.0">1</text>
<text class="tl te" x="142.0" y="166.0">O</text>
</svg><figcaption>On the unit circle, multiplying by \(z = \cos\theta + \mathrm{i}\sin\theta\) turns a point through \(\theta\) anticlockwise. So \(z^2\) and \(z^3\) are at \(2\theta\) and \(3\theta\), and dividing by \(z\) turns it back: \(z^{-1}\) is at \(-\theta\).</figcaption></figure>
:::

Dividing by \(z\) undoes the multiplication, so it turns the point back through \(\theta\). That is why the theorem holds for negative integers too: \(z^{-1}\) has modulus \(\dfrac1r\) and argument \(-\theta\), and \(z^{-n}\) has modulus \(r^{-n}\) and argument \(-n\theta\). On the unit circle \(z^{-1}\) is the mirror image of \(z\) in the real axis, which is the conjugate: \(z^{-1} = z^* = \cos\theta - \mathrm{i}\sin\theta\).

Here is the same idea with a modulus that is not 1. The widget draws \(z, z^2, \dots, z^n\) joined in order. With \(r = 1\) the points stay on the unit circle; with \(r > 1\) they spiral outwards and with \(r < 1\) inwards. Drag \(n\) below zero to see the negative powers, and watch the readout: \(|z^n| = r^n\), while the argument \(n\theta\) is reduced to \(-\pi < \arg \leq \pi\).

:::html
<div class="widget" data-w="fm-demoivre" data-mode="powers" data-z="1.1,0.5" data-n="6"></div>
:::

## Proving de Moivre's theorem

The syllabus asks you to **prove** the theorem for a positive integer exponent, usually by induction. The proof is short, and it is examined as a "prove that" question with marks for each of the four parts of an induction.

:::eg (Exam style) Prove by induction that \((\cos\theta + \mathrm{i}\sin\theta)^n = \cos n\theta + \mathrm{i}\sin n\theta\) for every positive integer \(n\). [5]
Let \(P(n)\) be the statement \((\cos\theta + \mathrm{i}\sin\theta)^n = \cos n\theta + \mathrm{i}\sin n\theta\).

For \(n = 1\) both sides equal \(\cos\theta + \mathrm{i}\sin\theta\), so \(P(1)\) is true. [B1]

Assume \(P(k)\) is true for some positive integer \(k\):
\[(\cos\theta + \mathrm{i}\sin\theta)^k = \cos k\theta + \mathrm{i}\sin k\theta\] [B1]
Then multiply both sides by \(\cos\theta + \mathrm{i}\sin\theta\):
\[(\cos\theta + \mathrm{i}\sin\theta)^{k+1} = (\cos k\theta + \mathrm{i}\sin k\theta)(\cos\theta + \mathrm{i}\sin\theta)\] [M1]
Expand the right side and use \(\mathrm{i}^2 = -1\):
\[\begin{aligned}
&= (\cos k\theta\cos\theta - \sin k\theta\sin\theta) \\
&\quad + \mathrm{i}(\sin k\theta\cos\theta + \cos k\theta\sin\theta) \\
&= \cos(k + 1)\theta + \mathrm{i}\sin(k + 1)\theta
\end{aligned}\] [A1]
So \(P(k)\) true implies \(P(k + 1)\) true. As \(P(1)\) is true, \(P(n)\) is true for all positive integers \(n\), by induction. [A1]
:::

The marks follow the pattern in [Proof by induction](#math.fm.induction): a base case, the hypothesis, the step, the conclusion. The step needs the compound angle formulae from the warm-up, and that is where the algebra is.

Now the other integers. \(n = 0\) is trivial, because both sides equal 1. For a negative integer write \(n = -m\) with \(m\) positive; the result for positive \(m\) is then enough.

:::eg (Exam style) Given that de Moivre's theorem holds for positive integers, show that it holds for \(n = -m\), where \(m\) is a positive integer. [3]
\[(\cos\theta + \mathrm{i}\sin\theta)^{-m} = \frac{1}{(\cos\theta + \mathrm{i}\sin\theta)^m} = \frac{1}{\cos m\theta + \mathrm{i}\sin m\theta}\] [B1]
Multiply top and bottom by the conjugate \(\cos m\theta - \mathrm{i}\sin m\theta\):
\[\frac{\cos m\theta - \mathrm{i}\sin m\theta}{\cos^2 m\theta + \sin^2 m\theta} = \cos m\theta - \mathrm{i}\sin m\theta\] [M1]
Since \(\cos(-m\theta) = \cos m\theta\) and \(\sin(-m\theta) = -\sin m\theta\), this is \(\cos(-m)\theta + \mathrm{i}\sin(-m)\theta\). [A1]
:::

### Rational exponents

The theorem is also used with a fractional exponent \(\dfrac pq\). Then it gives **one** value of the power, the one found by dividing the argument: \((\cos\theta + \mathrm{i}\sin\theta)^{p/q} = \cos\dfrac{p\theta}{q} + \mathrm{i}\sin\dfrac{p\theta}{q}\). To see why this is a valid value, raise it to the power \(q\) with the integer theorem: you get \(\cos p\theta + \mathrm{i}\sin p\theta\), which is \((\cos\theta + \mathrm{i}\sin\theta)^p\). A power with exponent \(\dfrac1q\) has \(q\) different values, though, and the other \(q - 1\) come from adding multiples of \(2\pi\) to the argument first. [Roots of unity and complex series](#math.fm.complex2) finds them all; here you use the value that comes from the principal argument.

:::eg Find the value of \((-8)^{1/3}\) given by de Moivre's theorem, using the principal argument of \(-8\).
\(-8 = 8(\cos\pi + \mathrm{i}\sin\pi)\), because \(\arg(-8) = \pi\). Raise to the power \(\dfrac13\):
\[(-8)^{1/3} = 8^{1/3}\left(\cos\frac\pi3 + \mathrm{i}\sin\frac\pi3\right) = 2\left(\tfrac12 + \tfrac{\sqrt3}{2}\mathrm{i}\right) = 1 + \sqrt3\,\mathrm{i}\]
**Check**: \((1 + \sqrt3\,\mathrm{i})^3 = 2^3(\cos\pi + \mathrm{i}\sin\pi) = -8\). The real cube root, \(-2\), is a different value of \((-8)^{1/3}\); there are three in all.
:::

## Powers of complex numbers

To raise a complex number to a power, **convert to modulus–argument form, apply the theorem, and convert back only if the question asks for \(a + b\mathrm{i}\)**. It is far quicker than multiplying out, and it works for any exponent.

:::steps
1. Find \(r = |z|\) and \(\theta = \arg z\) (check the quadrant with a sketch).
2. Write \(z^n = r^n(\cos n\theta + \mathrm{i}\sin n\theta)\).
3. Bring the argument into \(-\pi < \theta \leq \pi\) by adding or subtracting multiples of \(2\pi\), unless the question allows any form.
4. Evaluate the exact values of cosine and sine if you need \(a + b\mathrm{i}\).
:::

:::eg Express \((1 - \mathrm{i})^{10}\) in the form \(a + b\mathrm{i}\).
\(|1 - \mathrm{i}| = \sqrt2\) and \(\arg(1 - \mathrm{i}) = -\dfrac\pi4\), since the point is in the fourth quadrant. So
\[\begin{aligned}
(1 - \mathrm{i})^{10} &= \left(\sqrt2\right)^{10}\left(\cos\left(-\tfrac{10\pi}{4}\right) + \mathrm{i}\sin\left(-\tfrac{10\pi}{4}\right)\right) \\
&= 32\left(\cos\left(-\tfrac{5\pi}{2}\right) + \mathrm{i}\sin\left(-\tfrac{5\pi}{2}\right)\right)
\end{aligned}\]
Add \(2\pi\) to the argument: \(-\dfrac{5\pi}{2} + 2\pi = -\dfrac\pi2\), so
\[(1 - \mathrm{i})^{10} = 32\left(\cos\left(-\tfrac\pi2\right) + \mathrm{i}\sin\left(-\tfrac\pi2\right)\right) = -32\mathrm{i}\]
**Check** by squaring: \((1 - \mathrm{i})^2 = -2\mathrm{i}\), and \((-2\mathrm{i})^5 = -32\,\mathrm{i}^5 = -32\mathrm{i}\).
:::

:::eg Express \(\left(\sqrt3 + \mathrm{i}\right)^{-5}\) in the form \(a + b\mathrm{i}\).
\(|\sqrt3 + \mathrm{i}| = 2\) and \(\arg(\sqrt3 + \mathrm{i}) = \dfrac\pi6\). A negative exponent gives a reciprocal modulus and a negative argument:
\[\left(\sqrt3 + \mathrm{i}\right)^{-5} = 2^{-5}\left(\cos\left(-\tfrac{5\pi}{6}\right) + \mathrm{i}\sin\left(-\tfrac{5\pi}{6}\right)\right)\]
Now \(\cos\left(-\dfrac{5\pi}{6}\right) = -\dfrac{\sqrt3}{2}\) and \(\sin\left(-\dfrac{5\pi}{6}\right) = -\dfrac12\), so
\[\left(\sqrt3 + \mathrm{i}\right)^{-5} = \frac{1}{32}\left(-\frac{\sqrt3}{2} - \frac{\mathrm{i}}{2}\right) = -\frac{\sqrt3 + \mathrm{i}}{64}\]
**Check**: \(\left(\sqrt3 + \mathrm{i}\right)^5 = 32\left(\cos\dfrac{5\pi}{6} + \mathrm{i}\sin\dfrac{5\pi}{6}\right) = -16\sqrt3 + 16\mathrm{i}\), and \(\dfrac{1}{-16\sqrt3 + 16\mathrm{i}}\) is \(-\dfrac{\sqrt3 + \mathrm{i}}{64}\) after multiplying top and bottom by the conjugate.
:::

:::warn Do not forget the modulus, or the quadrant
Two slips lose most of the marks here. The first is to raise only the angle to the power \(n\) and leave the modulus alone: \(r^n\) matters whenever \(r \neq 1\). The second is to find the argument from \(\tan^{-1}\dfrac{b}{a}\) without checking the quadrant, so that \(-1 + \mathrm{i}\) gets \(-\dfrac\pi4\) instead of \(\dfrac{3\pi}{4}\). Sketch the point first.
:::

:::eg (Exam style) The complex number \(w\) is \(\dfrac{\sqrt3 + \mathrm{i}}{1 - \mathrm{i}}\). (a) Express \(w\) in the form \(r(\cos\theta + \mathrm{i}\sin\theta)\), where \(r > 0\) and \(-\pi < \theta \leq \pi\). [4] (b) Find \(w^6\) in the form \(a + b\mathrm{i}\). [2] (c) Find the smallest positive integer \(n\) for which \(w^n\) is real, and state the value of \(w^n\) for that \(n\). [3]
**(a)** \(\sqrt3 + \mathrm{i}\) has modulus 2 and argument \(\dfrac\pi6\). [B1] \(1 - \mathrm{i}\) has modulus \(\sqrt2\) and argument \(-\dfrac\pi4\). [B1]

Divide the moduli and subtract the arguments:
\[|w| = \frac{2}{\sqrt2} = \sqrt2, \qquad \arg w = \frac\pi6 + \frac\pi4 = \frac{5\pi}{12}\] [M1]
\[w = \sqrt2\left(\cos\frac{5\pi}{12} + \mathrm{i}\sin\frac{5\pi}{12}\right)\] [A1]
**(b)** By de Moivre's theorem,
\[w^6 = \left(\sqrt2\right)^6\left(\cos\frac{5\pi}{2} + \mathrm{i}\sin\frac{5\pi}{2}\right) = 8(0 + \mathrm{i})\] [M1]
\[w^6 = 8\mathrm{i}\] [A1]
**(c)** \(w^n\) is real when \(\sin\dfrac{5n\pi}{12} = 0\), that is when \(\dfrac{5n\pi}{12}\) is a multiple of \(\pi\). [M1]

So \(\dfrac{5n}{12}\) must be an integer. Since 5 and 12 have no common factor, \(n\) must be a multiple of 12, and the smallest is \(n = 12\). [A1]
\[w^{12} = \left(\sqrt2\right)^{12}(\cos5\pi + \mathrm{i}\sin5\pi) = 64 \times (-1) = -64\] [A1]
**Check** with (b): \(w^{12} = \left(w^6\right)^2 = (8\mathrm{i})^2 = -64\).
:::

### A real context: scaling and rotating

Computer graphics, signal processing and robotics all use the fact that multiplying by one complex number scales and rotates in a single step. Repeating the step is a power.

:::eg A drawing program builds a spiral. It starts at the point \(1\) in the complex plane and, at each step, multiplies the current point by \(z = 1.1(\cos15^\circ + \mathrm{i}\sin15^\circ)\). After \(n\) steps the point is \(z^n\). (a) Find the position after 24 steps. (b) Find the first step at which the point lies on the negative real axis, and its position. (c) Find the number of steps after which the distance from the origin first exceeds 100.
Each step multiplies the distance from \(O\) by 1.1 and turns the point through \(15^\circ\), so after \(n\) steps the distance is \(1.1^n\) and the angle is \(15n\) degrees.

(a) The angle is \(24 \times 15^\circ = 360^\circ\), a full turn, so the point is on the positive real axis, at a distance \(1.1^{24} = 9.85\) (3 s.f.). The position is \(9.85\).

(b) The point is on the negative real axis when \(15n \equiv 180\) modulo 360, and the first such \(n\) is \(n = 12\). The distance is \(1.1^{12} = 3.14\) (3 s.f.), so the point is at \(-3.14\).

(c) We need \(1.1^n > 100\), so \(n > \dfrac{\ln100}{\ln1.1} = 48.3\). The first whole number is \(n = 49\). Check the neighbours: \(1.1^{48} = 97.0 < 100\) and \(1.1^{49} = 107 > 100\).
:::

## Multiple angles: \(\cos n\theta\), \(\sin n\theta\), \(\tan n\theta\) in powers

De Moivre's theorem has two sides. Read from right to left it says that \(\cos n\theta + \mathrm{i}\sin n\theta\) is a power. Expand that power with the binomial theorem and the real and imaginary parts give formulae for \(\cos n\theta\) and \(\sin n\theta\) in terms of \(\cos\theta\) and \(\sin\theta\). Write \(c = \cos\theta\) and \(s = \sin\theta\) to keep the lines short.

:::steps
1. Write \(\cos n\theta + \mathrm{i}\sin n\theta = (c + \mathrm{i}s)^n\).
2. Expand the right side with the binomial theorem, which MF19 gives. Reduce the powers of i: \(\mathrm{i}^2 = -1\), \(\mathrm{i}^3 = -\mathrm{i}\), \(\mathrm{i}^4 = 1\), \(\mathrm{i}^5 = \mathrm{i}\), and so on.
3. Equate real parts for \(\cos n\theta\) and imaginary parts for \(\sin n\theta\). This works because \(c\) and \(s\) are real.
4. To get a single function, replace \(s^2\) by \(1 - c^2\) (or \(c^2\) by \(1 - s^2\)).
:::

:::eg Use de Moivre's theorem to express \(\cos3\theta\) and \(\sin3\theta\) in terms of \(\cos\theta\) and \(\sin\theta\) respectively.
\[\begin{aligned}
(c + \mathrm{i}s)^3 &= c^3 + 3c^2(\mathrm{i}s) + 3c(\mathrm{i}s)^2 + (\mathrm{i}s)^3 \\
&= c^3 + 3\mathrm{i}c^2s - 3cs^2 - \mathrm{i}s^3 \\
&= (c^3 - 3cs^2) + \mathrm{i}(3c^2s - s^3)
\end{aligned}\]
The real part gives \(\cos3\theta = c^3 - 3cs^2\). Replace \(s^2\) by \(1 - c^2\):
\[\cos3\theta = c^3 - 3c(1 - c^2) = 4c^3 - 3c\]
The imaginary part gives \(\sin3\theta = 3c^2s - s^3\). Replace \(c^2\) by \(1 - s^2\):
\[\sin3\theta = 3(1 - s^2)s - s^3 = 3s - 4s^3\]
**Check** with \(\theta = 0\): \(\cos0 = 1 = 4 - 3\). With \(\theta = \dfrac\pi2\): \(\sin\dfrac{3\pi}{2} = -1 = 3 - 4\).
:::

The expansion is where marks are won or lost, so be systematic: write the binomial coefficients first, then the powers of \(\mathrm{i}\), then collect. For \(n = 5\) the coefficients are \(1, 5, 10, 10, 5, 1\).

:::eg (Exam style) (a) Use de Moivre's theorem to show that \(\cos5\theta = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta\). [5] (b) Hence show that \(\cos^2\dfrac\pi{10} = \dfrac{5 + \sqrt5}{8}\). [4]
**(a)** By de Moivre's theorem, \(\cos5\theta\) is the real part of \((c + \mathrm{i}s)^5\). [B1]
\[(c + \mathrm{i}s)^5 = c^5 + 5c^4(\mathrm{i}s) + 10c^3(\mathrm{i}s)^2 + 10c^2(\mathrm{i}s)^3 + 5c(\mathrm{i}s)^4 + (\mathrm{i}s)^5\] [M1]
The terms with an even power of \(\mathrm{i}\) are real:
\[\cos5\theta = c^5 - 10c^3s^2 + 5cs^4\] [A1]
Replace \(s^2\) by \(1 - c^2\):
\[\begin{aligned}
\cos5\theta &= c^5 - 10c^3(1 - c^2) + 5c(1 - c^2)^2 \\
&= c^5 - 10c^3 + 10c^5 + 5c - 10c^3 + 5c^5
\end{aligned}\] [M1]
\[\cos5\theta = 16c^5 - 20c^3 + 5c\] [A1]
**(b)** Put \(\theta = \dfrac\pi{10}\), so \(5\theta = \dfrac\pi2\) and \(\cos5\theta = 0\):
\[16c^5 - 20c^3 + 5c = 0, \quad c(16c^4 - 20c^2 + 5) = 0\] [M1]
Since \(c = \cos\dfrac\pi{10} \neq 0\), \(16c^4 - 20c^2 + 5 = 0\), a quadratic in \(c^2\):
\[c^2 = \frac{20 \pm \sqrt{400 - 320}}{32} = \frac{5 \pm \sqrt5}{8}\] [M1 A1]
The two roots correspond to \(\theta = \dfrac\pi{10}\) and \(\theta = \dfrac{3\pi}{10}\), which both give \(\cos5\theta = 0\). The cosine is larger for the smaller angle, so \(\cos^2\dfrac\pi{10}\) is the larger root: \(\dfrac{5 + \sqrt5}{8}\). [A1]
**Check**: \(\cos18^\circ = 0.9511\), and \(\dfrac{5 + \sqrt5}{8} = 0.9045 = 0.9511^2\).
:::

The same method gives \(\sin5\theta\) from the imaginary part: the terms with an odd power of \(\mathrm{i}\). The result, in terms of \(\sin\theta\), is \(16s^5 - 20s^3 + 5s\), and you will use it in the exam practice.

### \(\tan n\theta\)

A tangent is a ratio, so write \(\tan n\theta = \dfrac{\sin n\theta}{\cos n\theta}\), take the imaginary and real parts of the same expansion, and divide top and bottom by \(c^n\). Every \(\dfrac sc\) becomes \(t = \tan\theta\).

:::eg Use de Moivre's theorem to express \(\tan3\theta\) in terms of \(t = \tan\theta\).
From the expansion above, \(\sin3\theta = 3c^2s - s^3\) and \(\cos3\theta = c^3 - 3cs^2\). Divide the numerator and the denominator by \(c^3\):
\[\tan3\theta = \frac{3c^2s - s^3}{c^3 - 3cs^2} = \frac{3t - t^3}{1 - 3t^2}\]
**Check** with \(\theta = \dfrac\pi{12}\): \(\tan\dfrac\pi4 = 1\), and with \(t = 2 - \sqrt3\) the right side is \(\dfrac{3t - t^3}{1 - 3t^2} = 1\).
:::

:::eg (Exam style) (a) Use de Moivre's theorem to show that \(\tan5\theta = \dfrac{5t - 10t^3 + t^5}{1 - 10t^2 + 5t^4}\), where \(t = \tan\theta\). [4] (b) Hence find the exact value of \(\tan^2\dfrac\pi5\). [4]
**(a)** \(\tan5\theta = \dfrac{\sin5\theta}{\cos5\theta}\), where \(\cos5\theta + \mathrm{i}\sin5\theta = (c + \mathrm{i}s)^5\). [M1]

From the expansion in the previous example, the real part is \(c^5 - 10c^3s^2 + 5cs^4\) and the imaginary part is \(5c^4s - 10c^2s^3 + s^5\). [M1]
\[\tan5\theta = \frac{5c^4s - 10c^2s^3 + s^5}{c^5 - 10c^3s^2 + 5cs^4}\]
Divide the numerator and the denominator by \(c^5\): [M1]
\[\tan5\theta = \frac{5t - 10t^3 + t^5}{1 - 10t^2 + 5t^4}\] [A1]
**(b)** For \(\theta = \dfrac\pi5\), \(\tan5\theta = \tan\pi = 0\), so the numerator is zero. As \(t \neq 0\):
\[t^4 - 10t^2 + 5 = 0\] [M1]
\[t^2 = \frac{10 \pm \sqrt{100 - 20}}{2} = 5 \pm 2\sqrt5\] [M1 A1]
Since \(\dfrac\pi5 < \dfrac\pi4\), \(\tan\dfrac\pi5 < 1\), so \(\tan^2\dfrac\pi5 < 1\). Now \(5 + 2\sqrt5 > 1\) and \(5 - 2\sqrt5 = 0.528 < 1\), so
\[\tan^2\frac\pi5 = 5 - 2\sqrt5\] [A1]
**Check**: \(\tan36^\circ = 0.7265\) and \(0.7265^2 = 0.5279\).
:::

:::warn Three habits that lose marks in multiple-angle questions
**Powers of i.** In \((c + \mathrm{i}s)^5\), the term \(10c^3(\mathrm{i}s)^2\) is \(-10c^3s^2\), not \(+10c^3s^2\). Write out \(\mathrm{i}^2 = -1\), \(\mathrm{i}^3 = -\mathrm{i}\), \(\mathrm{i}^4 = 1\), \(\mathrm{i}^5 = \mathrm{i}\) before you start.

**Squared brackets.** \((1 - c^2)^2 = 1 - 2c^2 + c^4\); it is not \(1 - c^4\).

**The wrong function.** To express \(\cos n\theta\) in powers of \(\cos\theta\), replace \(s^2\) by \(1 - c^2\). To express \(\sin n\theta\) in powers of \(\sin\theta\), replace \(c^2\) by \(1 - s^2\). For \(\sin n\theta\) with even \(n\) there is always a left-over factor of \(\cos\theta\), which cannot be removed.
:::

## Powers of \(\sin\theta\) and \(\cos\theta\) in multiple angles

The method reverses. Let \(z = \cos\theta + \mathrm{i}\sin\theta\). By de Moivre's theorem \(z^n = \cos n\theta + \mathrm{i}\sin n\theta\) and \(z^{-n} = \cos n\theta - \mathrm{i}\sin n\theta\). Adding and subtracting gives two results that do all the work.

:::key The two key results
For \(z = \cos\theta + \mathrm{i}\sin\theta\) and every positive integer \(n\),
\[z^n + z^{-n} = 2\cos n\theta \qquad z^n - z^{-n} = 2\mathrm{i}\sin n\theta\]
In particular \(z + \dfrac1z = 2\cos\theta\) and \(z - \dfrac1z = 2\mathrm{i}\sin\theta\).
:::

So \((2\cos\theta)^n = \left(z + \dfrac1z\right)^n\) and \((2\mathrm{i}\sin\theta)^n = \left(z - \dfrac1z\right)^n\). Expand the right side with the binomial theorem. The terms come in pairs \(z^k\) and \(z^{-k}\), and each pair is \(2\cos k\theta\) (or \(2\mathrm{i}\sin k\theta\)).

:::steps
1. Write \((2\cos\theta)^n = \left(z + z^{-1}\right)^n\), or \((2\mathrm{i}\sin\theta)^n = \left(z - z^{-1}\right)^n\).
2. Expand with the binomial theorem. Simplify each term to a power of \(z\): \(\left(z^{-1}\right)^2 = z^{-2}\).
3. Pair each term \(z^k\) with its partner \(z^{-k}\) and replace the pair by \(2\cos k\theta\) (or \(2\mathrm{i}\sin k\theta\)). A middle term with no \(z\) stays as a number.
4. Divide by the power of 2 (and by \(\mathrm{i}^n\) for sine).
:::

:::eg Express \(\cos^4\theta\) in terms of \(\cos2\theta\) and \(\cos4\theta\).
\[\begin{aligned}
(2\cos\theta)^4 = \left(z + \tfrac1z\right)^4 &= z^4 + 4z^2 + 6 + 4z^{-2} + z^{-4} \\
&= \left(z^4 + z^{-4}\right) + 4\left(z^2 + z^{-2}\right) + 6 \\
&= 2\cos4\theta + 8\cos2\theta + 6
\end{aligned}\]
Divide by \(2^4 = 16\):
\[\cos^4\theta = \frac{\cos4\theta + 4\cos2\theta + 3}{8}\]
**Check** with \(\theta = 0\): \(\cos^40 = 1 = \dfrac{1 + 4 + 3}{8}\).
:::

For sine the factor \(\mathrm{i}^n\) appears. With an even power it is real (\(\mathrm{i}^4 = 1\), \(\mathrm{i}^6 = -1\)); with an odd power it is imaginary and cancels against the \(\mathrm{i}\) in \(2\mathrm{i}\sin k\theta\).

:::eg Express \(\sin^3\theta\) in terms of \(\sin\theta\) and \(\sin3\theta\).
\[\begin{aligned}
(2\mathrm{i}\sin\theta)^3 = \left(z - \tfrac1z\right)^3 &= z^3 - 3z + 3z^{-1} - z^{-3} \\
&= \left(z^3 - z^{-3}\right) - 3\left(z - z^{-1}\right) \\
&= 2\mathrm{i}\sin3\theta - 6\mathrm{i}\sin\theta
\end{aligned}\]
The left side is \(8\mathrm{i}^3\sin^3\theta = -8\mathrm{i}\sin^3\theta\). Divide both sides by \(-8\mathrm{i}\):
\[\sin^3\theta = \frac{3\sin\theta - \sin3\theta}{4}\]
**Check** with \(\theta = \dfrac\pi2\): \(1 = \dfrac{3 - (-1)}{4}\).
:::

:::proof Why \(z^n + z^{-n} = 2\cos n\theta\)
Apply de Moivre's theorem to the exponents \(n\) and \(-n\), which it allows for any integer:
\[z^n = \cos n\theta + \mathrm{i}\sin n\theta \qquad z^{-n} = \cos(-n\theta) + \mathrm{i}\sin(-n\theta)\]
Cosine is even and sine is odd, so \(z^{-n} = \cos n\theta - \mathrm{i}\sin n\theta\). Add the two lines: the imaginary parts cancel and \(z^n + z^{-n} = 2\cos n\theta\). Subtract: the real parts cancel and \(z^n - z^{-n} = 2\mathrm{i}\sin n\theta\).
:::

The next example is the standard question of this type. Even powers of sine have a constant term, and the signs in the expansion alternate.

:::eg (Exam style) Use de Moivre's theorem to show that \(\sin^6\theta = \dfrac{1}{32}(10 - 15\cos2\theta + 6\cos4\theta - \cos6\theta)\). [6]
Let \(z = \cos\theta + \mathrm{i}\sin\theta\). Then \(z - \dfrac1z = 2\mathrm{i}\sin\theta\), so
\[\left(z - \tfrac1z\right)^6 = (2\mathrm{i}\sin\theta)^6 = -64\sin^6\theta\] [B1]
because \(\mathrm{i}^6 = (\mathrm{i}^2)^3 = -1\). Expand the left side with the coefficients 1, 6, 15, 20, 15, 6, 1:
\[\begin{aligned}
\left(z - \tfrac1z\right)^6 = z^6 - 6z^4 + 15z^2 - 20 \\
+ 15z^{-2} - 6z^{-4} + z^{-6}
\end{aligned}\] [M1 A1]
Pair \(z^k\) with \(z^{-k}\), using \(z^k + z^{-k} = 2\cos k\theta\): [M1]
\[\begin{aligned}
&= \left(z^6 + z^{-6}\right) - 6\left(z^4 + z^{-4}\right) \\
&\quad + 15\left(z^2 + z^{-2}\right) - 20 \\
&= 2\cos6\theta - 12\cos4\theta + 30\cos2\theta - 20
\end{aligned}\] [A1]
Equate and divide by \(-64\):
\[\sin^6\theta = \frac{20 - 30\cos2\theta + 12\cos4\theta - 2\cos6\theta}{64} = \frac{1}{32}\left(10 - 15\cos2\theta + 6\cos4\theta - \cos6\theta\right)\] [A1]
**Check** with \(\theta = \dfrac\pi2\): \(\sin^6\dfrac\pi2 = 1\), and \(\dfrac{1}{32}(10 + 15 + 6 + 1) = 1\).
:::

Products of sine and cosine use both results together. If \(\sin^m\theta\cos^n\theta\) has mixed powers, write \(\sin^m\theta = \dfrac{\left(z - z^{-1}\right)^m}{(2\mathrm{i})^m}\) and \(\cos^n\theta = \dfrac{\left(z + z^{-1}\right)^n}{2^n}\), multiply the two expansions, then pair terms. A shortcut for the common case \(\sin^2\theta\cos^2\theta\): \(\left(z - z^{-1}\right)\left(z + z^{-1}\right) = z^2 - z^{-2}\), so it is better to combine the brackets first.

### Integrals of powers of sine and cosine

Once \(\cos^n\theta\) or \(\sin^n\theta\) is a sum of \(\cos k\theta\) or \(\sin k\theta\) terms, it integrates term by term, using \(\displaystyle\int\cos k\theta\,d\theta = \dfrac{\sin k\theta}{k}\). That is much quicker than reduction formulae, and works without the by-parts steps of [Integration techniques](#math.p3.inttech).

:::eg Find \(\displaystyle\int_0^{\pi/2}\cos^5\theta\,d\theta\), using the expansion of \(\cos^5\theta\) in multiple angles.
\[\begin{aligned}
(2\cos\theta)^5 = \left(z + \tfrac1z\right)^5 &= z^5 + 5z^3 + 10z + 10z^{-1} + 5z^{-3} + z^{-5} \\
&= 2\cos5\theta + 10\cos3\theta + 20\cos\theta
\end{aligned}\]
So \(\cos^5\theta = \dfrac{1}{16}\left(\cos5\theta + 5\cos3\theta + 10\cos\theta\right)\), and
\[\begin{aligned}
\int_0^{\pi/2}\cos^5\theta\,d\theta &= \frac{1}{16}\left[\frac{\sin5\theta}{5} + \frac{5\sin3\theta}{3} + 10\sin\theta\right]_0^{\pi/2} \\
&= \frac{1}{16}\left(\frac15 - \frac53 + 10\right) = \frac{1}{16} \times \frac{128}{15} = \frac{8}{15}
\end{aligned}\]
Here \(\sin\dfrac{5\pi}{2} = 1\), \(\sin\dfrac{3\pi}{2} = -1\) and \(\sin\dfrac\pi2 = 1\).
:::

:::eg The voltage across a resistor is \(V = 4\cos^2 t\) volts, so the power in it is proportional to \(V^2 = 16\cos^4 t\). Find the mean value of \(V^2\) over one full period, \(0 \leq t \leq 2\pi\).
Use \(\cos^4t = \dfrac{\cos4t + 4\cos2t + 3}{8}\), so \(V^2 = 2\cos4t + 8\cos2t + 6\). The mean over a period is \(\dfrac{1}{2\pi}\displaystyle\int_0^{2\pi}V^2\,dt\):
\[\frac{1}{2\pi}\left[\frac{\sin4t}{2} + 4\sin2t + 6t\right]_0^{2\pi} = \frac{1}{2\pi} \times 12\pi = 6\]
Every cosine term integrates to zero over whole periods, so only the constant 6 is left. The mean of \(V^2\) is 6 (in volts squared).
:::

## Using the identities: equations and exact values

A multiple-angle identity turns a trigonometric equation into a polynomial one. The roots-and-coefficients relations from [Roots of polynomial equations](#math.fm.roots) then give exact values that a calculator can only approximate.

:::eg (Exam style) (a) Use de Moivre's theorem to show that \(\cos3\theta = 4\cos^3\theta - 3\cos\theta\). [3] (b) Show that the roots of \(x^3 - 3x - 1 = 0\) are \(2\cos\dfrac\pi9\), \(2\cos\dfrac{5\pi}{9}\) and \(2\cos\dfrac{7\pi}{9}\). [4] (c) Hence find the exact value of \(\cos\dfrac\pi9\cos\dfrac{5\pi}{9}\cos\dfrac{7\pi}{9}\). [2]
**(a)** The real part of \((c + \mathrm{i}s)^3\) is \(c^3 - 3cs^2\). [M1 A1]
\[\cos3\theta = c^3 - 3c(1 - c^2) = 4c^3 - 3c\] [A1]
**(b)** Let \(x = 2\cos\theta\). Then \(x^3 - 3x = 8c^3 - 6c = 2(4c^3 - 3c) = 2\cos3\theta\). [M1]

So \(x^3 - 3x - 1 = 0\) becomes \(2\cos3\theta = 1\), that is \(\cos3\theta = \dfrac12\). [M1]

Then \(3\theta = \dfrac\pi3, \dfrac{5\pi}{3}, \dfrac{7\pi}{3}\), giving \(\theta = \dfrac\pi9, \dfrac{5\pi}{9}, \dfrac{7\pi}{9}\), and these three angles have different cosines. [A1]

A cubic has at most three roots, so these are all of them: \(2\cos\dfrac\pi9\), \(2\cos\dfrac{5\pi}{9}\), \(2\cos\dfrac{7\pi}{9}\). [A1]
**(c)** The product of the roots of \(x^3 - 3x - 1 = 0\) is \(-\dfrac{d}{a} = 1\):
\[8\cos\frac\pi9\cos\frac{5\pi}{9}\cos\frac{7\pi}{9} = 1\] [M1]
\[\cos\frac\pi9\cos\frac{5\pi}{9}\cos\frac{7\pi}{9} = \frac18\] [A1]
**Check**: \(\cos20^\circ \times \cos100^\circ \times \cos140^\circ = 0.9397 \times (-0.1736) \times (-0.7660) = 0.1250\).
:::

The sum of the roots is zero, because the cubic has no \(x^2\) term. So the same result gives \(\cos\dfrac\pi9 + \cos\dfrac{5\pi}{9} + \cos\dfrac{7\pi}{9} = 0\), a neat fact that you would not find by calculator without noticing it.

:::exam What MF19 gives you, and what it does not
MF19 gives the binomial expansion of \((a + b)^n\) and the compound-angle and double-angle identities. It does **not** give de Moivre's theorem, \(z^n + z^{-n} = 2\cos n\theta\) or the multiple-angle expansions: learn them. In a "show that" question write every line of the expansion and the powers of \(\mathrm{i}\); the answer is given, so the marks are for the working. Keep answers exact (fractions, surds, multiples of \(\pi\)) unless the question asks for decimals.
:::

:::board
In UK Further Maths (Edexcel, AQA and OCR) de Moivre's theorem and the \(n\)th roots of a complex number are core content, so the methods in this chapter and the next carry over.
:::

:::eg Spot the error: use de Moivre's theorem to show that \(\cos4\theta = 8\cos^4\theta - 8\cos^2\theta + 1\), for 4 marks.
A student wrote this answer.

Line 1: \((c + \mathrm{i}s)^4 = c^4 + 4c^3(\mathrm{i}s) + 6c^2(\mathrm{i}s)^2 + 4c(\mathrm{i}s)^3 + (\mathrm{i}s)^4\)
Line 2: Real part: \(\cos4\theta = c^4 - 6c^2s^2 + s^4\)
Line 3: \(\cos4\theta = c^4 - 6c^2(1 - c^2) + \left(1 - c^4\right)\)
Line 4: \(\cos4\theta = c^4 - 6c^2 + 6c^4 + 1 - c^4 = 6c^4 - 6c^2 + 1\)

Line 1 is the correct expansion. [M1] Line 2 takes the real terms correctly. [A1]

**Line 3 has the right method but the wrong algebra.** [M1] [A0] The student replaced \(s^2\) by \(1 - c^2\) correctly in the middle term, but wrote \(s^4 = (1 - c^2)^2 = 1 - c^4\). The correct expansion is \((1 - c^2)^2 = 1 - 2c^2 + c^4\). The student scores 3 out of 4, and the final line does not match the answer given, which should have prompted a check.

Correct line 3: \(c^4 - 6c^2(1 - c^2) + \left(1 - 2c^2 + c^4\right)\), which gives \(c^4 - 6c^2 + 6c^4 + 1 - 2c^2 + c^4 = 8c^4 - 8c^2 + 1\).

**Check** with \(\theta = 0\): \(\cos0 = 1\), and the student's formula gives \(6 - 6 + 1 = 1\) too, so \(\theta = 0\) cannot expose the slip. Try \(\theta = \dfrac\pi3\): \(\cos\dfrac{4\pi}{3} = -\dfrac12\), the correct formula gives \(8 \times \dfrac1{16} - 8 \times \dfrac14 + 1 = -\dfrac12\), and the student's gives \(6 \times \dfrac1{16} - 6 \times \dfrac14 + 1 = -\dfrac18\).
:::

:::try Start easy, finish at exam standard
Q: Use de Moivre's theorem to write \((\cos20^\circ + \mathrm{i}\sin20^\circ)^6\) in the form \(a + b\mathrm{i}\).
A: \(\cos120^\circ + \mathrm{i}\sin120^\circ = -\dfrac12 + \dfrac{\sqrt3}{2}\mathrm{i}\).
Q: Simplify \(\dfrac{(\cos\theta + \mathrm{i}\sin\theta)^3}{(\cos2\theta + \mathrm{i}\sin2\theta)^2}\).
A: The numerator is \(\cos3\theta + \mathrm{i}\sin3\theta\) and the denominator is \(\cos4\theta + \mathrm{i}\sin4\theta\). Dividing subtracts the arguments: \(\cos(-\theta) + \mathrm{i}\sin(-\theta) = \cos\theta - \mathrm{i}\sin\theta\).
Q: \(z = 2\left(\cos\dfrac\pi9 + \mathrm{i}\sin\dfrac\pi9\right)\). Find \(|z^7|\) and \(\arg z^7\).
A: \(|z^7| = 2^7 = 128\) and \(\arg z^7 = \dfrac{7\pi}{9}\), which is already in \(-\pi < \theta \leq \pi\).
Q: Find \((-1 - \mathrm{i})^5\) in the form \(a + b\mathrm{i}\).
A: The modulus is \(\sqrt2\) and the argument is \(-\dfrac{3\pi}{4}\). So the fifth power has modulus \(4\sqrt2\) and argument \(-\dfrac{15\pi}{4} + 4\pi = \dfrac\pi4\): \(4\sqrt2\left(\dfrac{\sqrt2}{2} + \dfrac{\sqrt2}{2}\mathrm{i}\right) = 4 + 4\mathrm{i}\).
Q: Find the value given by de Moivre's theorem for \((-1 + \sqrt3\,\mathrm{i})^{1/2}\), using the principal argument.
A: The modulus is 2 and the argument is \(\dfrac{2\pi}{3}\). So the value is \(\sqrt2\left(\cos\dfrac\pi3 + \mathrm{i}\sin\dfrac\pi3\right) = \dfrac{\sqrt2}{2} + \dfrac{\sqrt6}{2}\mathrm{i}\).
Q: Use \((c + \mathrm{i}s)^2\) to obtain the double-angle formulae for \(\cos2\theta\) and \(\sin2\theta\).
A: \((c + \mathrm{i}s)^2 = c^2 - s^2 + 2\mathrm{i}cs\). The real part gives \(\cos2\theta = c^2 - s^2\) and the imaginary part gives \(\sin2\theta = 2sc\).
Q: Use de Moivre's theorem to show that \(\tan4\theta = \dfrac{4t - 4t^3}{1 - 6t^2 + t^4}\), where \(t = \tan\theta\).
A: \((c + \mathrm{i}s)^4\) has real part \(c^4 - 6c^2s^2 + s^4\) and imaginary part \(4c^3s - 4cs^3\). Dividing top and bottom by \(c^4\) gives \(\dfrac{4t - 4t^3}{1 - 6t^2 + t^4}\).
Q: Express \(\sin^2\theta\cos^2\theta\) in terms of \(\cos4\theta\).
A: \(\sin\theta\cos\theta = \dfrac{z^2 - z^{-2}}{4\mathrm{i}}\), so \(\sin^2\theta\cos^2\theta = \dfrac{z^4 - 2 + z^{-4}}{-16} = \dfrac{2 - 2\cos4\theta}{16} = \dfrac{1 - \cos4\theta}{8}\).
Q: Using \(\sin^4\theta = \dfrac{3 - 4\cos2\theta + \cos4\theta}{8}\), find \(\displaystyle\int_0^\pi\sin^4\theta\,d\theta\).
A: \(\dfrac18\left[3\theta - 2\sin2\theta + \dfrac{\sin4\theta}{4}\right]_0^\pi = \dfrac{3\pi}{8}\).
Q: Show that \(\left(\mathrm{e}^{\mathrm{i}\theta} + \mathrm{e}^{-\mathrm{i}\theta}\right)^2 = 2 + 2\cos2\theta\).
A: Expanding gives \(\mathrm{e}^{2\mathrm{i}\theta} + 2 + \mathrm{e}^{-2\mathrm{i}\theta} = 2 + 2\cos2\theta\), because \(\mathrm{e}^{2\mathrm{i}\theta} + \mathrm{e}^{-2\mathrm{i}\theta} = 2\cos2\theta\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Use de Moivre's theorem to find \(\left(\sqrt3 - \mathrm{i}\right)^6\).
A: The modulus is 2 and the argument is \(-\dfrac\pi6\). [B1] \(\left(\sqrt3 - \mathrm{i}\right)^6 = 2^6\left(\cos(-\pi) + \mathrm{i}\sin(-\pi)\right)\) [M1] \(= -64\). [A1]
Q: [4 marks] ★ Express \(\left(1 - \sqrt3\,\mathrm{i}\right)^{-4}\) in the form \(a + b\mathrm{i}\), giving exact values.
A: The modulus is 2 and the argument is \(-\dfrac\pi3\). [B1] Raise to the power \(-4\): \(2^{-4}\left(\cos\dfrac{4\pi}{3} + \mathrm{i}\sin\dfrac{4\pi}{3}\right)\). [M1 A1] \(= \dfrac{1}{16}\left(-\dfrac12 - \dfrac{\sqrt3}{2}\mathrm{i}\right) = -\dfrac{1 + \sqrt3\,\mathrm{i}}{32}\). [A1]
Q: [4 marks] ★★ Use de Moivre's theorem to show that \(\sin4\theta = 4\sin\theta\cos\theta\cos2\theta\).
A: The imaginary part of \((c + \mathrm{i}s)^4\) is \(4c^3s - 4cs^3\). [M1 A1] \(= 4cs(c^2 - s^2)\) [M1] \(= 4\sin\theta\cos\theta\cos2\theta\), using \(\cos2\theta = c^2 - s^2\). [A1]
Q: [6 marks] ★★ (a) Use \(z = \cos\theta + \mathrm{i}\sin\theta\) to show that \(\cos^3\theta = \dfrac14(\cos3\theta + 3\cos\theta)\). (b) Hence find \(\displaystyle\int_0^{\pi/3}\cos^3\theta\,d\theta\) exactly.
A: (a) \(\left(z + z^{-1}\right)^3 = (2\cos\theta)^3\). [B1] \(\left(z + z^{-1}\right)^3 = z^3 + 3z + 3z^{-1} + z^{-3}\) [M1] \(= 2\cos3\theta + 6\cos\theta\). [A1] So \(8\cos^3\theta = 2\cos3\theta + 6\cos\theta\) and \(\cos^3\theta = \dfrac14(\cos3\theta + 3\cos\theta)\). [A1]
(b) \(\dfrac14\left[\dfrac{\sin3\theta}{3} + 3\sin\theta\right]_0^{\pi/3}\) [M1] \(= \dfrac14\left(0 + \dfrac{3\sqrt3}{2}\right) = \dfrac{3\sqrt3}{8}\). [A1]
Q: [7 marks] ★★ (a) Show that \(\tan3\theta = \dfrac{3t - t^3}{1 - 3t^2}\), where \(t = \tan\theta\). (b) Hence find the exact value of \(\tan\dfrac\pi{12}\).
A: (a) \(\sin3\theta = 3c^2s - s^3\) and \(\cos3\theta = c^3 - 3cs^2\) from the imaginary and real parts of \((c + \mathrm{i}s)^3\). [M1 A1] Divide top and bottom by \(c^3\): \(\tan3\theta = \dfrac{3t - t^3}{1 - 3t^2}\). [A1]
(b) Put \(\theta = \dfrac\pi{12}\): \(\tan\dfrac\pi4 = 1\), so \(3t - t^3 = 1 - 3t^2\) [M1] and \(t^3 - 3t^2 - 3t + 1 = 0\). [A1] Factorise: \((t + 1)\left(t^2 - 4t + 1\right) = 0\), so \(t = -1\) or \(t = 2 \pm \sqrt3\). [M1] Since \(0 < \dfrac\pi{12} < \dfrac\pi4\), \(0 < t < 1\), so \(t = 2 - \sqrt3\). [A1]
Q: [5 marks] ★★ Show that \(\left(1 + \cos\theta + \mathrm{i}\sin\theta\right)^n = 2^n\cos^n\dfrac\theta2\left(\cos\dfrac{n\theta}{2} + \mathrm{i}\sin\dfrac{n\theta}{2}\right)\).
A: \(1 + \cos\theta = 2\cos^2\dfrac\theta2\) [M1] and \(\sin\theta = 2\sin\dfrac\theta2\cos\dfrac\theta2\). [M1] So \(1 + \cos\theta + \mathrm{i}\sin\theta = 2\cos\dfrac\theta2\left(\cos\dfrac\theta2 + \mathrm{i}\sin\dfrac\theta2\right)\). [A1] Raise to the power \(n\): \(2^n\cos^n\dfrac\theta2\left(\cos\dfrac\theta2 + \mathrm{i}\sin\dfrac\theta2\right)^n\) [M1] and apply de Moivre's theorem to the bracket. [A1]
Q: [10 marks] (#math.fm.roots) ★★★ (a) Use de Moivre's theorem to show that \(\sin5\theta = 16\sin^5\theta - 20\sin^3\theta + 5\sin\theta\). (b) Show that the roots of \(16x^4 - 20x^2 + 5 = 0\) are \(\pm\sin\dfrac\pi5\) and \(\pm\sin\dfrac{2\pi}{5}\). (c) Use the product of the roots to show that \(\sin\dfrac\pi5\sin\dfrac{2\pi}{5} = \dfrac{\sqrt5}{4}\).
H: The imaginary part of \((c + \mathrm{i}s)^5\) is \(5c^4s - 10c^2s^3 + s^5\). Replace \(c^2\) by \(1 - s^2\).
H: For (b), \(\sin5\theta = 0\) when \(\theta = \pm\dfrac\pi5\) and \(\pm\dfrac{2\pi}{5}\). Divide the equation by \(x\) first, because \(x = 0\) is also a root of \(\sin5\theta = 0\).
H: For (c), a quartic \(ax^4 + \dots + e = 0\) has product of roots \(\dfrac ea\). Two of the four roots are negative.
A: (a) The imaginary part of \((c + \mathrm{i}s)^5\) is \(5c^4s - 10c^2s^3 + s^5\). [M1 A1] Replace \(c^2\) by \(1 - s^2\): \(5s(1 - s^2)^2 - 10s^3(1 - s^2) + s^5\) [M1] \(= 16s^5 - 20s^3 + 5s\). [A1]
(b) With \(x = \sin\theta\), \(\sin5\theta = 0\) gives \(x\left(16x^4 - 20x^2 + 5\right) = 0\). [M1] \(\theta = \pm\dfrac\pi5, \pm\dfrac{2\pi}{5}\) all give \(\sin5\theta = 0\) and \(x \neq 0\), and the four values \(x = \pm\sin\dfrac\pi5, \pm\sin\dfrac{2\pi}{5}\) are different, so they are the four roots of the quartic. [A1 A1]
(c) The product of the roots is \(\dfrac{5}{16}\). [B1] The product is \(\sin^2\dfrac\pi5\sin^2\dfrac{2\pi}{5}\), since two roots are negative. [M1] Both sines are positive, so \(\sin\dfrac\pi5\sin\dfrac{2\pi}{5} = \sqrt{\dfrac5{16}} = \dfrac{\sqrt5}{4}\). [A1]
Q: [9 marks] (#math.p3.integ) ★★★ (a) Use de Moivre's theorem to show that \(16\sin^5\theta = \sin5\theta - 5\sin3\theta + 10\sin\theta\). (b) Hence find \(\displaystyle\int_0^{\pi/3}\sin^5\theta\,d\theta\) in exact form.
H: Expand \(\left(z - z^{-1}\right)^5\) with the coefficients 1, 5, 10, 10, 5, 1 and alternating signs. Remember \(\mathrm{i}^5 = \mathrm{i}\).
H: Pair the terms: \(z^5 - z^{-5} = 2\mathrm{i}\sin5\theta\), and so on. Divide by \(32\mathrm{i}\).
H: In (b), \(\cos\dfrac{5\pi}{3} = \dfrac12\), \(\cos\pi = -1\) and \(\cos\dfrac\pi3 = \dfrac12\).
A: (a) \((2\mathrm{i}\sin\theta)^5 = 32\mathrm{i}\sin^5\theta\) and equals \(\left(z - z^{-1}\right)^5\). [B1] \(= z^5 - 5z^3 + 10z - 10z^{-1} + 5z^{-3} - z^{-5}\) [M1 A1]
\[\begin{aligned}
&= \left(z^5 - z^{-5}\right) - 5\left(z^3 - z^{-3}\right) \\
&\quad + 10\left(z - z^{-1}\right)
\end{aligned}\] [M1]
which is \(2\mathrm{i}\left(\sin5\theta - 5\sin3\theta + 10\sin\theta\right)\), and dividing by \(2\mathrm{i}\) gives \(16\sin^5\theta = \sin5\theta - 5\sin3\theta + 10\sin\theta\). [A1]
(b) \(\dfrac{1}{16}\left[-\dfrac{\cos5\theta}{5} + \dfrac{5\cos3\theta}{3} - 10\cos\theta\right]_0^{\pi/3}\) [M1 A1]
\[\begin{aligned}
&= \frac{1}{16}\left(\left(-\tfrac{1}{10} - \tfrac53 - 5\right) \right. \\
&\qquad \left. - \left(-\tfrac15 + \tfrac53 - 10\right)\right)
\end{aligned}\] [M1]
\(= \dfrac{1}{16} \times \dfrac{53}{30} = \dfrac{53}{480}\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ (a) Show that, for \(0 < \theta < \dfrac\pi2\) and every positive integer \(n\), \(\left(1 + \mathrm{i}\tan\theta\right)^n + \left(1 - \mathrm{i}\tan\theta\right)^n = \dfrac{2\cos n\theta}{\cos^n\theta}\). (b) Hence solve \((1 + \mathrm{i}x)^3 + (1 - \mathrm{i}x)^3 = 0\) for real \(x\), giving exact answers.
H: Write \(1 + \mathrm{i}\tan\theta\) over the common denominator \(\cos\theta\).
H: In (b) put \(x = \tan\theta\) and use the result for \(n = 3\), or expand the cubes directly.
A: (a) \(1 + \mathrm{i}\tan\theta = \dfrac{\cos\theta + \mathrm{i}\sin\theta}{\cos\theta}\) and \(1 - \mathrm{i}\tan\theta = \dfrac{\cos\theta - \mathrm{i}\sin\theta}{\cos\theta}\). [B1] By de Moivre's theorem the \(n\)th powers are \(\dfrac{\cos n\theta \pm \mathrm{i}\sin n\theta}{\cos^n\theta}\). [M1 A1] Adding, the imaginary parts cancel and the sum is \(\dfrac{2\cos n\theta}{\cos^n\theta}\). [A1]
(b) Expanding directly, \((1 + \mathrm{i}x)^3 + (1 - \mathrm{i}x)^3 = 2\left(1 - 3x^2\right)\), because the imaginary terms cancel. [M1] So \(1 - 3x^2 = 0\) and \(x = \pm\dfrac{1}{\sqrt3}\). [M1 A1] This agrees with part (a): \(x = \tan\theta\) with \(\cos3\theta = 0\) gives \(\theta = \dfrac\pi6\), and \(\tan\dfrac\pi6 = \dfrac1{\sqrt3}\).
Q: [6 marks] ★★★ The points \(P_n\) in the complex plane are given by \(P_n = (1 + \mathrm{i})^n\) for \(n = 0, 1, 2, \dots\). (a) Show that the triangle \(OP_nP_{n+1}\) has area \(2^{n-1}\). (b) Find the total area of the first ten triangles, \(n = 0\) to \(n = 9\).
H: \(1 + \mathrm{i}\) has modulus \(\sqrt2\) and argument \(\dfrac\pi4\). What are \(|P_n|\) and the angle \(P_nOP_{n+1}\)?
H: Use area \(= \tfrac12ab\sin C\). Part (b) is a geometric series.
A: (a) \(|P_n| = 2^{n/2}\) and \(|P_{n+1}| = 2^{(n+1)/2}\). [B1] The angle at \(O\) is \(\dfrac\pi4\). [B1] The area is \(\tfrac12 \times 2^{n/2} \times 2^{(n+1)/2} \times \sin\dfrac\pi4\) [M1] \(= \tfrac12 \times 2^{n + 1/2} \times \dfrac{1}{\sqrt2} = 2^{n-1}\). [A1]
(b) The areas are \(\tfrac12, 1, 2, \dots, 256\), a geometric series with first term \(\tfrac12\), ratio 2 and 10 terms. [M1] The sum is \(\dfrac{\tfrac12\left(2^{10} - 1\right)}{2 - 1} = 511.5\). [A1]
:::

:::quiz
? What is \((\cos\theta + \mathrm{i}\sin\theta)^n\), for an integer \(n\)?
+ \(\cos n\theta + \mathrm{i}\sin n\theta\)
- \(\cos^n\theta + \mathrm{i}\sin^n\theta\)
- \(n\cos\theta + \mathrm{i}n\sin\theta\)
- \(\cos\theta^n + \mathrm{i}\sin\theta^n\)
> De Moivre's theorem multiplies the **angle** by \(n\). Raising each part to the power \(n\) separately is not valid, and multiplying the whole expression by \(n\) gives a number of the wrong size.
? \(\left(2\left(\cos20^\circ + \mathrm{i}\sin20^\circ\right)\right)^3\) equals
+ \(8(\cos60^\circ + \mathrm{i}\sin60^\circ)\)
- \(6(\cos60^\circ + \mathrm{i}\sin60^\circ)\)
- \(8(\cos20^\circ + \mathrm{i}\sin20^\circ)\)
- \(2(\cos60^\circ + \mathrm{i}\sin60^\circ)\)
> The modulus is cubed (\(2^3 = 8\)) and the argument is multiplied by 3 (\(60^\circ\)). Multiplying the modulus by 3 gives 6; leaving the angle unchanged or the modulus unchanged each forgets half of the theorem.
? When \(\left(z + z^{-1}\right)^4\) is expanded, what is the term that does not contain \(z\)?
+ \(6\)
- \(4\)
- \(1\)
- \(0\)
> The middle term of the binomial expansion has coefficient \(\binom42 = 6\) and \(z^2z^{-2} = 1\). The coefficient 4 belongs to the \(z^2\) and \(z^{-2}\) terms.
? For \(z = \cos\theta + \mathrm{i}\sin\theta\), what is \(z - \dfrac1z\)?
+ \(2\mathrm{i}\sin\theta\)
- \(2\sin\theta\)
- \(2\cos\theta\)
- \(0\)
> \(z^{-1} = \cos\theta - \mathrm{i}\sin\theta\), so the real parts cancel and the imaginary parts add: \(2\mathrm{i}\sin\theta\). Leaving out the \(\mathrm{i}\) is a common slip, and \(2\cos\theta\) is \(z + z^{-1}\).
? To express \(\tan5\theta\) in powers of \(t = \tan\theta\), after expanding \((c + \mathrm{i}s)^5\) you divide the numerator and the denominator by
+ \(\cos^5\theta\)
- \(\sin^5\theta\)
- \(\cos\theta\)
- nothing: the expansion is already in terms of \(t\)
> Each term has total degree 5 in \(c\) and \(s\), so dividing by \(c^5\) turns every term into a power of \(\dfrac sc = t\). Dividing by \(c\) alone leaves powers of \(c\) behind.
? \(\arg z = \dfrac{3\pi}{4}\). What is the principal argument of \(z^3\)?
+ \(\dfrac\pi4\)
- \(\dfrac{9\pi}{4}\)
- \(\dfrac{3\pi}{4}\)
- \(-\dfrac\pi4\)
> \(3 \times \dfrac{3\pi}{4} = \dfrac{9\pi}{4}\), which is outside \(-\pi < \theta \leq \pi\). Subtract \(2\pi\) to get \(\dfrac\pi4\). Leaving \(\dfrac{9\pi}{4}\) is correct as a value of the argument but not the principal one.
? What is \(\left(\cos\theta + \mathrm{i}\sin\theta\right)^{-n}\)?
+ \(\cos n\theta - \mathrm{i}\sin n\theta\)
- \(-\cos n\theta - \mathrm{i}\sin n\theta\)
- \(\cos n\theta + \mathrm{i}\sin n\theta\)
- \(\dfrac{1}{\cos n\theta} + \dfrac{\mathrm{i}}{\sin n\theta}\)
> A negative exponent negates the argument: \(\cos(-n\theta) = \cos n\theta\) and \(\sin(-n\theta) = -\sin n\theta\). Negating the whole expression, or taking reciprocals of the parts separately, is not what the theorem says.
:::

:::checklist What you can now do
- [ ] I can state de Moivre's theorem for positive and negative integers and explain it as a scaling and rotation of the Argand diagram.
- [ ] I can prove de Moivre's theorem for a positive integer by induction.
- [ ] I can find powers of a complex number in modulus–argument form, with the argument in \(-\pi < \theta \leq \pi\).
- [ ] I can use the theorem with a rational exponent to find one value of a root, and say why there are more.
- [ ] I can express \(\cos n\theta\), \(\sin n\theta\) and \(\tan n\theta\) in powers of \(\cos\theta\), \(\sin\theta\) or \(\tan\theta\) by expanding \((c + \mathrm{i}s)^n\).
- [ ] I can express powers of \(\sin\theta\) and \(\cos\theta\) in multiple angles using \(z + z^{-1} = 2\cos\theta\) and \(z - z^{-1} = 2\mathrm{i}\sin\theta\).
- [ ] I can integrate powers of \(\sin\theta\) and \(\cos\theta\) by first writing them in multiple angles.
- [ ] I can use a multiple-angle identity to find exact trigonometric values, and relate them to the roots and coefficients of a polynomial.
:::

:::recap
- De Moivre: \((\cos\theta + \mathrm{i}\sin\theta)^n = \cos n\theta + \mathrm{i}\sin n\theta\) for every integer \(n\); \(z^n = r^n(\cos n\theta + \mathrm{i}\sin n\theta)\).
- Geometry: multiplying by \(z\) scales by \(r\) and rotates by \(\theta\); \(z^n\) does it \(n\) times; \(z^{-1}\) reverses it.
- Proof by induction: base case, hypothesis, step with the compound angle formulae, conclusion (5 marks).
- Powers of a complex number: modulus to the power \(n\), argument times \(n\), reduced to \((-\pi, \pi]\).
- Multiple angles: expand \((c + \mathrm{i}s)^n\); real part gives \(\cos n\theta\), imaginary part gives \(\sin n\theta\); divide by \(c^n\) for \(\tan n\theta\).
- Powers: \(z^n + z^{-n} = 2\cos n\theta\) and \(z^n - z^{-n} = 2\mathrm{i}\sin n\theta\); expand \(\left(z \pm z^{-1}\right)^n\) and pair terms.
- Integrate powers of sine and cosine term by term after converting to multiple angles.
- Check every identity at one or two values of \(\theta\).
:::

:::links
- watch: [De Moivre's theorem](https://www.examsolutions.net/tutorials/de-moivres-theorem/) · ExamSolutions · the theorem and its uses, worked step by step
- watch: [Euler's formula with introductory group theory](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · why multiplying by \(\mathrm{e}^{\mathrm{i}\theta}\) is a rotation
- read: [Intuitive understanding of Euler's formula](https://betterexplained.com/articles/intuitive-understanding-of-eulers-formula/) · BetterExplained · a gentle second explanation of the same idea
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · the complex-numbers booklets have graded questions with answers
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Roots of unity and complex series](#math.fm.complex2) uses the \(n\) values of a root of a complex number, and the sum of a series of sines and cosines, both found with de Moivre's theorem.
