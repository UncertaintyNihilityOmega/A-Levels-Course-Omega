@chapter math.fm.arclength
@title Arc length and surface area
@level fm
@paper CAIE 9231 Paper 2
@time 5–6 hours
@summary You will use integration to find the length of a curve given in Cartesian form, parametrically or in polar coordinates, and the area of the surface formed when a curve is rotated about the x-axis or the y-axis. The curves in exam questions are chosen so that the square root simplifies, and you will learn to spot why.
:::why
A cable hung between two poles, the rim of a heart-shaped cam, the metal in a satellite dish: each needs the length of a curve or the area of a curved surface, and neither can be found with a ruler. Integration does it by cutting the curve into tiny straight pieces, using Pythagoras on each, and adding them up. The idea is old and simple; the skill is in choosing the right form of the formula, and in noticing when the expression under the root is a perfect square.
:::

**Before you start**, you need polar coordinates from [Polar coordinates](#math.fm.polar), parametric differentiation from [Further differentiation](#math.p3.diff), volumes of revolution from [Integration](#math.p1.integ), and the hyperbolic functions and substitutions from [Hyperbolic functions](#math.fm.hyperbolic) and [Further integration: hyperbolic and inverse forms](#math.fm.integ).

:::try Warm-up
Q: A curve has parametric equations \(x = t^2\), \(y = t^3\). Find \(\dfrac{dy}{dx}\). (from [Further differentiation](#math.p3.diff))
A: \(\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt} = \dfrac{3t^2}{2t} = \dfrac{3t}{2}\).
Q: Show that \(\sqrt{1 + \sinh^2x} = \cosh x\). (from [Hyperbolic functions](#math.fm.hyperbolic))
A: \(\cosh^2x - \sinh^2x = 1\), so \(1 + \sinh^2x = \cosh^2x\), and \(\cosh x > 0\) for every \(x\), so the root is \(\cosh x\).
Q: Find the volume formed when the region under \(y = \sqrt x\) from \(x = 0\) to \(x = 4\) is rotated through \(2\pi\) about the \(x\)-axis. (from [Integration](#math.p1.integ))
A: \(V = \pi\displaystyle\int_0^4y^2\,dx = \pi\int_0^4x\,dx = \pi\left[\tfrac{x^2}{2}\right]_0^4 = 8\pi\).
:::

## The length of a curve

Take two points \(P\) and \(Q\) on a curve, very close together. The curve between them is almost a straight chord. Call the horizontal and vertical steps \(\delta x\) and \(\delta y\) (the Greek letter delta, a small change), and the chord length \(\delta s\). The right-angled triangle gives \(\delta s^2 = \delta x^2 + \delta y^2\).

:::html
<figure class="fig small"><svg viewBox="40 40 290 150" role="img" aria-label="A curve rising to the right with two close points P at (x, y) and Q at (x + delta x, y + delta y). A straight chord joins P to Q and is labelled delta s. A dashed horizontal line from P, labelled delta x, and a dashed vertical line up to Q, labelled delta y, complete a right-angled triangle.">
<path class="c1 sw2" fill="none" d="M90.0 184.0 L102.5 180.6 L115.0 176.5 L127.5 171.6 L140.0 166.0 L152.5 159.6 L165.0 152.5 L177.5 144.6 L190.0 136.0 L202.5 126.6 L215.0 116.5 L227.5 105.6 L240.0 94.0 L252.5 81.6 L265.0 68.5 L277.5 54.6"/>
<line class="c2 sw2" x1="152.5" y1="159.6" x2="240.0" y2="94.0"/>
<line class="ln-m thin dash" x1="152.5" y1="159.6" x2="240.0" y2="159.6"/>
<line class="ln-m thin dash" x1="240.0" y1="159.6" x2="240.0" y2="94.0"/>
<path class="ln-m thin" fill="none" d="M232.0 159.6 L232.0 151.6 L240.0 151.6"/>
<circle class="fi" cx="152.5" cy="159.6" r="3.5"/>
<circle class="fi" cx="240.0" cy="94.0" r="3.5"/>
<text class="tl halo" x="82" y="148">P (x, y)</text>
<text class="tl halo" x="100" y="80">Q (x + δx, y + δy)</text>
<text class="tl halo" x="166" y="122">δs</text>
<text class="tl halo" x="186" y="178">δx</text>
<text class="tl halo" x="248" y="134">δy</text>
</svg><figcaption>A small piece of a curve between \(P\) and \(Q\). The chord \(\delta s\) is the hypotenuse of a right-angled triangle with sides \(\delta x\) and \(\delta y\), so \(\delta s^2 = \delta x^2 + \delta y^2\).</figcaption></figure>
:::

:::def Arc length
The length of a curve between two of its points, measured along the curve. It is the limit of the total length of straight chords joining closely spaced points on the curve, as the spacing tends to zero.
:::

:::def Surface of revolution
The surface formed when a curve is rotated through \(2\pi\) about a straight line (here the \(x\)-axis or the \(y\)-axis). Its area is the quantity this chapter calls the surface area.
:::

Divide by \(\delta x^2\): \(\left(\dfrac{\delta s}{\delta x}\right)^2 = 1 + \left(\dfrac{\delta y}{\delta x}\right)^2\). In the limit as the pieces shrink, \(\dfrac{\delta y}{\delta x}\) becomes \(\dfrac{dy}{dx}\), and adding the lengths of the pieces becomes an integral.

:::proof Why the arc length formulas hold
Cut the curve into \(n\) small pieces, with the \(i\)th piece having steps \(\delta x_i\) and \(\delta y_i\).
1. By Pythagoras the \(i\)th chord has length \(\delta s_i = \sqrt{\delta x_i^2 + \delta y_i^2}\).
2. Take \(\delta x_i\) out of the root: \(\delta s_i = \sqrt{1 + \left(\dfrac{\delta y_i}{\delta x_i}\right)^2}\,\delta x_i\).
3. The total length of the chords is \(\displaystyle\sum_i\sqrt{1 + \left(\dfrac{\delta y_i}{\delta x_i}\right)^2}\,\delta x_i\).
4. As the pieces shrink, each chord tends to the arc and \(\dfrac{\delta y_i}{\delta x_i}\) tends to \(\dfrac{dy}{dx}\). The sum becomes \(\displaystyle\int\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2}\,dx\).
5. For a curve given by \(x(t)\), \(y(t)\), write \(\delta s_i = \sqrt{\left(\dfrac{\delta x_i}{\delta t}\right)^2 + \left(\dfrac{\delta y_i}{\delta t}\right)^2}\,\delta t\); the limit is \(\displaystyle\int\sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2}\,dt\).
6. Swapping the roles of \(x\) and \(y\) gives the form with \(\dfrac{dx}{dy}\).
:::

:::key Arc length
The length \(s\) of a curve from \(A\) to \(B\) is \(\displaystyle\int_A^B ds\), where
\[\begin{aligned}
\text{Cartesian, } y(x): \quad s &= \int_{x_A}^{x_B}\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx \\
\text{Cartesian, } x(y): \quad s &= \int_{y_A}^{y_B}\sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy \\
\text{parametric: } \quad s &= \int_{t_A}^{t_B}\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt \\
\text{polar: } \quad s &= \int_{\theta_A}^{\theta_B}\sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta
\end{aligned}\]
The limits go from the smaller value of the variable to the larger, so \(s > 0\). **None of these formulae is on MF19**: learn them. The polar form is explained in the polar section below.
:::

Notice the structure: every formula is the square root of a sum of two squares. The plain Cartesian form is the parametric form with \(t = x\), because then \(\dfrac{dx}{dt} = 1\).

There is a useful way to read the parametric formula. If \(t\) is time and \((x, y)\) is the position of a particle, then \(\dfrac{dx}{dt}\) and \(\dfrac{dy}{dt}\) are the components of its velocity, and \(\sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2}\) is its **speed**. The arc length is the speed integrated over time: the distance the particle travels. This is why a length is never negative, and why it is the same for any way of parametrising the curve.

:::tip Which form do I use?
- The curve is given as \(y = f(x)\): use the \(dx\) form. If it is easier to solve for \(x\), use the \(dy\) form.
- The curve is given by \(x(t)\) and \(y(t)\): use the \(dt\) form. Do not eliminate \(t\) first.
- The curve is given as \(r = f(\theta)\): use the \(d\theta\) form. Do not convert to Cartesian coordinates.
In every case differentiate first, then look for a perfect square under the root before you try to integrate.
:::

### Cartesian curves

:::eg (Exam style) Find the exact length of the curve \(y = x^{3/2}\) from \(x = 0\) to \(x = 4\), and give the value to 3 significant figures.
\[\frac{dy}{dx} = \tfrac32x^{1/2}\] [B1]
\[s = \int_0^4\sqrt{1 + \tfrac94x}\,dx\] [M1]
Substitute \(u = 1 + \tfrac94x\), so \(du = \tfrac94dx\). The limits become \(u = 1\) and \(u = 10\):
\[s = \tfrac49\int_1^{10}u^{1/2}\,du\] [M1]
\[s = \tfrac49 \times \tfrac23\left[u^{3/2}\right]_1^{10} = \tfrac{8}{27}\left(10\sqrt{10} - 1\right)\] [A1]
\[s = 9.07\] [A1]
**Check**: the straight line from \((0, 0)\) to \((4, 8)\) has length \(\sqrt{80} = 8.94\), and a curve is longer than the straight line joining its ends; the path along the axes, \(4 + 8 = 12\), is longer than the curve. And \(8.94 < 9.07 < 12\).
:::

An awkward root that will not simplify is rare in exams. The curves are chosen so that \(1 + \left(\dfrac{dy}{dx}\right)^2\) is a **perfect square** (or becomes one through an identity), and the root disappears. A quick test: if \(\dfrac{dy}{dx}\) is of the form \(\dfrac{p}{2} - \dfrac{1}{2p}\) or \(\sinh\) of something, expect \(1 + \left(\dfrac{dy}{dx}\right)^2 = \left(\dfrac{p}{2} + \dfrac{1}{2p}\right)^2\) or \(\cosh^2\).

:::eg (Exam style) The curve \(C\) has equation \(y = \dfrac{x^2}{4} - \tfrac12\ln x\) for \(x > 0\). (a) Show that \(1 + \left(\dfrac{dy}{dx}\right)^2 = \left(\dfrac x2 + \dfrac{1}{2x}\right)^2\). (b) Find the exact length of \(C\) from \(x = 1\) to \(x = e\).
**(a)** \(\dfrac{dy}{dx} = \dfrac x2 - \dfrac{1}{2x}\). [B1]
\[\begin{aligned}
1 + \left(\frac{dy}{dx}\right)^2 &= 1 + \frac{x^2}{4} - 2 \times \frac x2 \times \frac{1}{2x} + \frac{1}{4x^2} \\
&= \frac{x^2}{4} + \frac12 + \frac{1}{4x^2}
\end{aligned}\] [M1]
This is \(\left(\dfrac x2 + \dfrac{1}{2x}\right)^2\), since the cross term of that square is \(2 \times \dfrac x2 \times \dfrac{1}{2x} = \dfrac12\). [A1]
**(b)** For \(x > 0\) the bracket is positive, so the root is \(\dfrac x2 + \dfrac{1}{2x}\):
\[s = \int_1^e\left(\frac x2 + \frac{1}{2x}\right)dx\] [M1]
\[s = \left[\frac{x^2}{4} + \frac12\ln x\right]_1^e\] [A1]
\[s = \left(\frac{e^2}{4} + \frac12\right) - \frac14 = \frac{e^2 + 1}{4}\] [A1]
**Check**: \(\dfrac{e^2 + 1}{4} = 2.10\). The curve goes from \((1, \tfrac14)\) to \(\left(e, \tfrac{e^2}{4} - \tfrac12\right) = (2.72, 1.35)\), which are \(\sqrt{1.72^2 + 1.10^2} = 2.04\) apart. The arc is a little longer, as it should be.
:::

The hanging cable is the most famous example, and it needs the identity \(1 + \sinh^2 = \cosh^2\).

:::plot A cable hangs between poles at \(x = -20\) and \(x = 20\) (metres) in the curve \(y = 25\cosh\dfrac{x}{25}\). It is lowest at \((0, 25)\) and 33.4 m high at each pole.
--f "12.5*(exp(x/25)+exp(-x/25))" --label "y = 25 cosh(x/25)" --x -30 30 --y 0 55 --pt "-20,33.44,A@s" --pt "20,33.44,B@s" --pt "0,25,lowest point (0, 25)@se" --legend tr
:::

:::eg (Exam style) A cable hangs between two poles 40 m apart. With the origin at ground level midway between the poles, its shape is \(y = 25\cosh\dfrac{x}{25}\) for \(-20 \le x \le 20\), with lengths in metres. Find the length of the cable.
\[\frac{dy}{dx} = \sinh\frac{x}{25}\] [B1]
\[1 + \left(\frac{dy}{dx}\right)^2 = 1 + \sinh^2\frac{x}{25} = \cosh^2\frac{x}{25}\] [M1]
Since \(\cosh\) is positive, \(\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} = \cosh\dfrac{x}{25}\). [A1]
\[s = \int_{-20}^{20}\cosh\frac{x}{25}\,dx = \left[25\sinh\frac{x}{25}\right]_{-20}^{20}\] [M1]
\[s = 50\sinh 0.8 = 44.4\ \text{m}\] [A1]
**Check**: the poles are 40 m apart, and 44.4 m is a little longer, as expected for a cable that sags by 8.4 m.
:::

Sometimes a curve is easier to describe with \(x\) as a function of \(y\). Then use the \(dy\) form; the algebra is identical with the letters swapped.

:::eg (Exam style) Find the exact length of the curve \(x = \tfrac12y^2\) from \(y = 0\) to \(y = 2\).
\[\frac{dx}{dy} = y\] [B1]
\[s = \int_0^2\sqrt{1 + y^2}\,dy\] [M1]
The root has the form \(\sqrt{1 + y^2}\), so substitute \(y = \sinh u\), \(dy = \cosh u\,du\), and \(\sqrt{1 + \sinh^2u} = \cosh u\): [M1]
\[s = \int\cosh^2u\,du = \int\tfrac12(1 + \cosh 2u)\,du = \tfrac12u + \tfrac14\sinh 2u\] [A1]
The upper limit \(y = 2\) gives \(\sinh u = 2\), so \(u = \sinh^{-1}2\) and \(\cosh u = \sqrt{1 + 4} = \sqrt5\). Also \(\tfrac14\sinh 2u = \tfrac12\sinh u\cosh u\). The lower limit gives \(u = 0\). [M1]
\[s = \tfrac12\sinh^{-1}2 + \tfrac12 \times 2 \times \sqrt5 = \sqrt5 + \tfrac12\sinh^{-1}2\] [A1]
**Check**: \(\sinh^{-1}2 = \ln\left(2 + \sqrt5\right) = 1.444\), so \(s = 2.236 + 0.722 = 2.96\). The chord from \((0, 0)\) to \((2, 2)\) is \(2.83\) long: the arc is a little longer.
:::

:::warn Square both derivatives, and keep the 1
The commonest lost marks are an unsquared derivative (writing \(\sqrt{1 + \frac{dy}{dx}}\)), a missing \(1\) (writing \(\sqrt{\left(\frac{dy}{dx}\right)^2}\), which is just \(\frac{dy}{dx}\)), and forgetting to take the square root at the end. The formula is \(\sqrt{1 + (\text{derivative})^2}\). In the parametric form there is no 1: it is \(\sqrt{(\ldots)^2 + (\ldots)^2}\).
:::

## Parametric curves

When \(x\) and \(y\) both depend on a parameter \(t\), the chord has \(\delta x = \dfrac{dx}{dt}\delta t\) and \(\delta y = \dfrac{dy}{dt}\delta t\), and Pythagoras gives \(ds = \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2}\,dt\). You do not need \(\dfrac{dy}{dx}\) at all.

A quick consistency check: the curve \(x = t^2\), \(y = t^3\) is the curve \(y = x^{3/2}\) from the first example, with \(x = 4\) when \(t = 2\). The parametric formula gives
\[s = \int_0^2\sqrt{4t^2 + 9t^4}\,dt = \int_0^2t\sqrt{4 + 9t^2}\,dt = \left[\tfrac{1}{27}\left(4 + 9t^2\right)^{3/2}\right]_0^2 = \tfrac{1}{27}\left(40^{3/2} - 8\right)\]
which is \(9.07\), the same number as before, and equal to \(\tfrac{8}{27}\left(10\sqrt{10} - 1\right)\) since \(40^{3/2} = 80\sqrt{10}\).

:::eg (Exam style) The cycloid is traced by a point on the rim of a rolling wheel. It has parametric equations \(x = 3(t - \sin t)\), \(y = 3(1 - \cos t)\) for \(0 \le t \le 2\pi\). Find the length of one arch.
\[\frac{dx}{dt} = 3(1 - \cos t) \qquad \frac{dy}{dt} = 3\sin t\] [B1]
\[\begin{aligned}
\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 &= 9\left(1 - 2\cos t + \cos^2t + \sin^2t\right) \\
&= 9(2 - 2\cos t)
\end{aligned}\] [M1]
Use \(1 - \cos t = 2\sin^2\tfrac t2\):
\[\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 36\sin^2\frac t2\] [A1]
For \(0 \le t \le 2\pi\), \(\tfrac t2\) runs from 0 to \(\pi\), where \(\sin\tfrac t2 \ge 0\), so the root is \(6\sin\tfrac t2\) with no modulus. [B1]
\[s = \int_0^{2\pi}6\sin\frac t2\,dt = \left[-12\cos\frac t2\right]_0^{2\pi}\] [M1]
\[s = 12 + 12 = 24\] [A1]
**Check**: one arch is \(6\pi = 18.8\) wide and 6 high, and it is a humped path. 24 lies between the width 18.8 and the 'over and down' path \(18.8 + 12 = 30.8\), and it equals 8 times the wheel radius \(3\), a known property of the cycloid.
:::

:::eg Find the total length of the astroid \(x = \cos^3t\), \(y = \sin^3t\), for \(0 \le t \le 2\pi\).
\[\frac{dx}{dt} = -3\cos^2t\sin t \qquad \frac{dy}{dt} = 3\sin^2t\cos t\]
\[\begin{aligned}
\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 &= 9\sin^2t\cos^2t\left(\cos^2t + \sin^2t\right) \\
&= 9\sin^2t\cos^2t
\end{aligned}\]
The root is \(3\left|\sin t\cos t\right|\), and the modulus matters: over a full turn \(\sin t\cos t\) is negative in two of the four quadrants. By symmetry the four arcs have equal length, so take \(0 \le t \le \tfrac\pi2\), where \(\sin t\cos t \ge 0\):
\[\text{one arc} = \int_0^{\pi/2}3\sin t\cos t\,dt = \left[\tfrac32\sin^2t\right]_0^{\pi/2} = \tfrac32\]
The total length is \(4 \times \tfrac32 = 6\).

**Check**: the curve lies in the unit square and runs from \((1, 0)\) to \((0, 1)\) in each quadrant, a straight-line distance of \(\sqrt2 = 1.41\). The arc is \(1.5\), a little longer.
:::

:::warn The root of a square is a modulus
\(\sqrt{9\sin^2t\cos^2t}\) is \(3|\sin t\cos t|\), not \(3\sin t\cos t\). Over an interval where the sign changes, integrating the signed expression gives 0 (or a smaller value) instead of the length. Split the interval, or use symmetry on an interval where the sign is fixed, and **say** why the root is positive there.
:::

## Polar curves

For a polar curve \(r = f(\theta)\), use \(x = r\cos\theta\) and \(y = r\sin\theta\) with \(r\) a function of \(\theta\). The polar formula follows from the parametric one.

:::proof Why the polar arc length formula holds
Take \(\theta\) as the parameter, with \(x = r\cos\theta\) and \(y = r\sin\theta\), and write \(r'\) for \(\dfrac{dr}{d\theta}\).
1. By the product rule \(\dfrac{dx}{d\theta} = r'\cos\theta - r\sin\theta\).
2. Likewise \(\dfrac{dy}{d\theta} = r'\sin\theta + r\cos\theta\).
3. Square and add: the cross terms \(\mp 2rr'\sin\theta\cos\theta\) cancel, leaving
\[\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2 = r'^2\left(\cos^2\theta + \sin^2\theta\right) + r^2\left(\sin^2\theta + \cos^2\theta\right)\]
4. Since \(\cos^2\theta + \sin^2\theta = 1\), this is \(r^2 + r'^2\).
5. Put it into the parametric formula: \(s = \displaystyle\int\sqrt{r^2 + \left(\dfrac{dr}{d\theta}\right)^2}\,d\theta\).
:::

A check on the formula: a circle \(r = a\) has \(\dfrac{dr}{d\theta} = 0\), so \(s = \displaystyle\int_0^{2\pi}a\,d\theta = 2\pi a\), the circumference. Also remember that the polar **arc length** formula has \(r^2 + (r')^2\) under a root, while the polar **area** formula from [Polar coordinates](#math.fm.polar) is \(\tfrac12\int r^2\,d\theta\). Do not mix them.

:::eg (Exam style) Show that the cardioid \(r = a(1 + \cos\theta)\), \(0 \le \theta \le 2\pi\), has length \(8a\).
\[\frac{dr}{d\theta} = -a\sin\theta\] [B1]
\[\begin{aligned}
r^2 + \left(\frac{dr}{d\theta}\right)^2 &= a^2\left[(1 + \cos\theta)^2 + \sin^2\theta\right] \\
&= a^2(2 + 2\cos\theta)
\end{aligned}\] [M1]
Use \(1 + \cos\theta = 2\cos^2\tfrac\theta2\):
\[r^2 + \left(\frac{dr}{d\theta}\right)^2 = 4a^2\cos^2\frac\theta2\] [A1]
The curve is symmetrical about the initial line, so the length is twice the length for \(0 \le \theta \le \pi\). There \(\tfrac\theta2\) runs from 0 to \(\tfrac\pi2\), and \(\cos\tfrac\theta2 \ge 0\), so the root is \(2a\cos\tfrac\theta2\):
\[s = 2\int_0^\pi2a\cos\frac\theta2\,d\theta\] [M1]
\[s = 2\left[4a\sin\frac\theta2\right]_0^\pi = 8a\] [A1]
**Check** with \(a = 1\): the cardioid fits in a box \(2.25\) wide and \(2.60\) high, whose perimeter is \(9.7\), and it is longer than a circle of radius 1 (circumference \(6.28\)). The length \(8\) lies between.
:::

:::eg The spiral \(r = 2e^\theta\) is drawn for \(0 \le \theta \le 1\). Find its length.
\(\dfrac{dr}{d\theta} = 2e^\theta\), so
\[r^2 + \left(\frac{dr}{d\theta}\right)^2 = 4e^{2\theta} + 4e^{2\theta} = 8e^{2\theta}\]
The root is \(2\sqrt2\,e^\theta\) (positive), so
\[s = \int_0^12\sqrt2\,e^\theta\,d\theta = 2\sqrt2\left(e - 1\right) = 4.86\]
**Check**: the spiral goes from \(r = 2\) to \(r = 2e = 5.44\), so its length is at least the radial change \(3.44\), and at most that plus an arc of radius \(5.44\) turning through 1 radian, which is \(3.44 + 5.44 \approx 8.87\). The answer \(4.86\) lies between. (It is \(\sqrt2\) times the radial change, a property of this spiral.)
:::

:::eg Find the length of the spiral \(r = \theta\) for \(0 \le \theta \le 2\).
\(\dfrac{dr}{d\theta} = 1\), so \(r^2 + \left(\dfrac{dr}{d\theta}\right)^2 = \theta^2 + 1\) and \(s = \displaystyle\int_0^2\sqrt{\theta^2 + 1}\,d\theta\). This is exactly the integral of the parabola \(x = \tfrac12y^2\) a few pages back, with \(\theta\) in place of \(y\), so \(s = \sqrt5 + \tfrac12\sinh^{-1}2 = 2.96\). Two quite different curves have the same length.
:::

## Surfaces of revolution

Spin a curve about the \(x\)-axis. It sweeps out a surface, such as a bowl, a vase or a dish. To find its area, cut the curve into tiny pieces of length \(\delta s\). Each piece, spun about the axis, sweeps out a thin band: a ring with circumference \(2\pi y\) (the circle traced by a point at height \(y\)) and width \(\delta s\) (measured along the curve, not along the axis). The band's area is about \(2\pi y\,\delta s\), and adding the bands gives an integral.

:::proof Why the surface area is \(2\pi\int y\,ds\)
1. A piece of the curve of length \(\delta s\), at height \(y\) above the \(x\)-axis, is nearly straight.
2. Rotated once about the \(x\)-axis, it sweeps out a thin band of a cone, or of a cylinder if the piece is parallel to the axis.
3. Cut the band along a straight line and unroll it: it is almost a rectangle with one side equal to the circumference of the circle swept by the piece, \(2\pi y\), and the other equal to the length of the piece, \(\delta s\).
4. So the area of the band is \(\delta S \approx 2\pi y\,\delta s\).
5. Adding the bands for all the pieces and letting them shrink gives \(S = \displaystyle\int2\pi y\,ds\).
6. For rotation about the \(y\)-axis the circle swept by a piece has radius \(x\), so \(y\) is replaced by \(x\).
:::

:::key Surface area of revolution
For a curve on one side of the axis (all \(y \ge 0\), or all \(x \ge 0\)), rotated through \(2\pi\):
\[\begin{aligned}
\text{about the } x\text{-axis: } S &= 2\pi\int y\,ds \\
\text{about the } y\text{-axis: } S &= 2\pi\int x\,ds
\end{aligned}\]
with \(ds = \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2}\,dx\) (Cartesian) or \(ds = \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2}\,dt\) (parametric). The variable in front of \(ds\) is the distance **from the axis of rotation**. These formulae are not on MF19.
:::

:::note Polar curves
Surface areas of revolution for polar curves are **not** in the 9231 syllabus. You may meet them in other courses, but you do not need them here.
:::

Before using the formula in a new situation, test it on a surface whose area you already know.

:::eg Show that rotating the semicircle \(y = \sqrt{R^2 - x^2}\), \(-R \le x \le R\), about the \(x\)-axis gives a sphere of surface area \(4\pi R^2\).
\(\dfrac{dy}{dx} = \dfrac{-x}{\sqrt{R^2 - x^2}} = -\dfrac xy\), so
\[1 + \left(\frac{dy}{dx}\right)^2 = 1 + \frac{x^2}{y^2} = \frac{y^2 + x^2}{y^2} = \frac{R^2}{y^2}\]
and \(y\,ds = y \times \dfrac Ry\,dx = R\,dx\). Then
\[S = 2\pi\int_{-R}^RR\,dx = 2\pi R \times 2R = 4\pi R^2\]
The formula gives the known result. A useful by-product: \(y\sqrt{1 + (y')^2}\) simplified to the constant \(R\), which is why the integral was so easy.
:::

Another surface you know is the cone. A straight line through the origin, \(y = kx\), rotated about the \(x\)-axis gives a cone with radius \(r = kh\) and slant height \(l = h\sqrt{1 + k^2}\) at \(x = h\), and the formula should reproduce the standard curved area \(\pi rl\).

:::eg Rotate the line \(y = \tfrac12x\) for \(0 \le x \le 6\) about the \(x\)-axis. Find the area of the curved surface of the cone formed, and check it with \(\pi rl\).
\(\dfrac{dy}{dx} = \tfrac12\), so \(ds = \sqrt{1 + \tfrac14}\,dx = \tfrac{\sqrt5}{2}\,dx\), and
\[S = 2\pi\int_0^6\tfrac12x \times \frac{\sqrt5}{2}\,dx = \frac{\pi\sqrt5}{2}\left[\frac{x^2}{2}\right]_0^6 = 9\sqrt5\,\pi\]
This is \(63.2\) to 3 s.f. **Check**: at \(x = 6\) the radius is \(r = 3\) and the slant height is \(l = \sqrt{6^2 + 3^2} = \sqrt{45}\), so \(\pi rl = 3\sqrt{45}\,\pi = 9\sqrt5\,\pi\). The two agree.
:::

:::eg (Exam style) The curve \(y = \cosh x\) for \(0 \le x \le \ln 2\) is rotated through \(2\pi\) about the \(x\)-axis. Find the exact area of the surface formed.
\[\frac{dy}{dx} = \sinh x, \qquad ds = \sqrt{1 + \sinh^2x}\,dx = \cosh x\,dx\] [B1]
\[S = 2\pi\int_0^{\ln 2}\cosh x \times \cosh x\,dx = 2\pi\int_0^{\ln 2}\cosh^2x\,dx\] [M1]
Use \(\cosh^2x = \tfrac12(1 + \cosh 2x)\), from the identity \(\cosh 2x = 2\cosh^2x - 1\): [M1]
\[S = \pi\left[x + \tfrac12\sinh 2x\right]_0^{\ln 2}\] [A1]
Now \(\sinh(2\ln 2) = \dfrac{4 - \frac14}{2} = \dfrac{15}{8}\), so
\[S = \pi\left(\ln 2 + \tfrac{15}{16}\right) = 5.12\] [A1]
**Check**: this is \(2\pi\) times the integral \(\displaystyle\int_0^{\ln 2}\cosh^2x\,dx = \tfrac12\ln 2 + \tfrac{15}{32}\), which is the \(C_2\) of [Reduction formulae](#math.fm.reduction).
:::

When the rotation is about the \(y\)-axis, the distance from the axis is \(x\). A common mistake is to carry on using \(y\).

:::eg (Exam style) The curve \(y = x^2\) for \(0 \le x \le 1\) is rotated through \(2\pi\) about the \(y\)-axis to form a bowl. Find the exact area of the curved surface.
\[\frac{dy}{dx} = 2x\] [B1]
The distance from the \(y\)-axis is \(x\), so
\[S = 2\pi\int_0^1x\sqrt{1 + 4x^2}\,dx\] [M1]
Substitute \(u = 1 + 4x^2\), \(du = 8x\,dx\), with limits \(u = 1\) to \(5\): [M1]
\[S = 2\pi \times \tfrac18\int_1^5u^{1/2}\,du = \frac{\pi}{4} \times \tfrac23\left[u^{3/2}\right]_1^5 = \frac\pi6\left(5\sqrt5 - 1\right)\] [A1]
\[S = 5.33\] [A1]
**Check**: the rim is a circle of radius 1 and the bowl is 1 high. A flat disc of radius 1 has area \(\pi = 3.14\); a cone with the same rim and height has area \(\pi\sqrt2 = 4.44\); the bowl bulges further, and \(5.33\) is larger, as expected.
:::

Surfaces from parametric curves use the same formula with \(ds\) in terms of \(t\).

:::eg (Exam style) A parabolic dish is made by rotating the curve with parametric equations \(x = t^2\), \(y = 2t\), for \(0 \le t \le 1\), through \(2\pi\) about the \(x\)-axis, with lengths in metres. Find the area of metal needed, to 3 significant figures.
\[\frac{dx}{dt} = 2t, \qquad \frac{dy}{dt} = 2\] [B1]
\[\frac{ds}{dt} = \sqrt{4t^2 + 4} = 2\sqrt{1 + t^2}\] [M1 A1]
\[S = 2\pi\int_0^1y\,\frac{ds}{dt}\,dt = 2\pi\int_0^12t \times 2\sqrt{1 + t^2}\,dt = 8\pi\int_0^1t\sqrt{1 + t^2}\,dt\] [M1]
Substitute \(u = 1 + t^2\), \(du = 2t\,dt\):
\[S = 8\pi \times \tfrac12 \times \tfrac23\left[u^{3/2}\right]_1^2 = \frac{8\pi}{3}\left(2\sqrt2 - 1\right)\] [M1]
\[S = 15.3\ \text{m}^2\] [A1]
**Check**: the rim has radius \(y = 2\) at \(t = 1\) and the dish is 1 m deep. A flat disc of radius 2 has area \(4\pi = 12.6\), so \(15.3\) for a curved dish is sensible.
:::

:::warn Axis of rotation, and the \(2\pi\)
For a surface the key slips are: using \(y\) when rotating about the \(y\)-axis (the factor is the distance from the axis); leaving out the \(2\pi\); and putting \(ds\) in the wrong form (a missing square, or \(dx\) left over after the substitution). Write \(S = 2\pi\int(\text{distance from axis})\,ds\) before filling in the pieces.
:::

:::exam Formulae, exact answers and checking
None of these formulae is on MF19: learn the four arc length forms and the surface area forms. "Find the exact length" means a surd, logarithm or multiple of \(\pi\), not a decimal; "to 3 significant figures" means a decimal from a calculator. Where the question says "show that", the line that makes the root a perfect square earns a method mark. Always say why a root is positive, and after finding a length, compare it with the straight line between the end points: a length shorter than the chord is wrong.
:::

:::board
Arc length and surface area of revolution are part of the Cambridge 9231 syllabus (outcome 2.4d); this chapter describes 9231 only. Other boards place these topics differently, so check the content list of your own Further Maths specification before relying on this chapter.
:::

:::eg Spot the error: The curve \(x = t^2\), \(y = \tfrac13t^3\) is drawn for \(0 \le t \le 2\). Find its length [5 marks].
A student wrote this answer.

Line 1: \(\dfrac{dx}{dt} = 2t\), \(\dfrac{dy}{dt} = t^2\)
Line 2: \(s = \displaystyle\int_0^2\sqrt{4t^2 + t^4}\,dt = \int_0^2t\sqrt{4 + t^2}\,dt\)
Line 3: Let \(u = 4 + t^2\), \(du = 2t\,dt\), so \(s = \displaystyle\int_4^8\sqrt u\,du\)
Line 4: \(s = \tfrac23\left[u^{3/2}\right]_4^8 = \tfrac23\left(8^{3/2} - 4^{3/2}\right) = 9.75\)

Line 1 is correct. [B1] Line 2 uses the parametric formula and simplifies the root correctly. [M1] [A1] Line 3 chooses a suitable substitution, so it earns the method mark. [M1]

**Line 3 contains the slip, and line 4 loses the accuracy mark.** Since \(du = 2t\,dt\), the integral \(\displaystyle\int t\sqrt{4 + t^2}\,dt\) is \(\tfrac12\displaystyle\int\sqrt u\,du\), not \(\displaystyle\int\sqrt u\,du\): the factor \(\tfrac12\) was dropped, so the answer is double what it should be. [A0] The student scores 4 out of 5.

Correct lines 3 and 4: \(s = \tfrac12\displaystyle\int_4^8\sqrt u\,du = \tfrac13\left(8^{3/2} - 4^{3/2}\right) = \dfrac{16\sqrt2 - 8}{3}\). [A1]

**Check** against the chord: the curve runs from \((0, 0)\) to \((4, \tfrac83)\), a distance of \(\sqrt{16 + 7.11} = 4.81\). The correct length \(\dfrac{16\sqrt2 - 8}{3} = 4.88\) is just above it, but the student's \(9.75\) is twice as long, and could not be the length of such a gently curving arc.
:::

:::try Start easy, finish at exam standard
Q: Find the exact length of \(y = \tfrac13\left(x^2 + 2\right)^{3/2}\) from \(x = 0\) to \(x = 3\).
A: \(\dfrac{dy}{dx} = x\sqrt{x^2 + 2}\), so \(1 + \left(\dfrac{dy}{dx}\right)^2 = 1 + x^2\left(x^2 + 2\right) = \left(x^2 + 1\right)^2\). Then \(s = \displaystyle\int_0^3\left(x^2 + 1\right)dx = \left[\tfrac{x^3}{3} + x\right]_0^3 = 12\).
Q: Find the length of \(y = \ln\cos x\) from \(x = 0\) to \(x = \tfrac\pi3\), to 3 s.f.
A: \(\dfrac{dy}{dx} = -\tan x\), so \(1 + \tan^2x = \sec^2x\) and \(s = \displaystyle\int_0^{\pi/3}\sec x\,dx = \left[\ln\left(\sec x + \tan x\right)\right]_0^{\pi/3} = \ln\left(2 + \sqrt3\right) = 1.32\).
Q: Find the length of the curve \(x = e^t\cos t\), \(y = e^t\sin t\) for \(0 \le t \le 1\), to 3 s.f.
A: \(\dfrac{dx}{dt} = e^t(\cos t - \sin t)\), \(\dfrac{dy}{dt} = e^t(\sin t + \cos t)\), so the sum of squares is \(2e^{2t}\) and \(s = \displaystyle\int_0^1\sqrt2\,e^t\,dt = \sqrt2(e - 1) = 2.43\).
Q: Find the exact length of \(x = 3t^2\), \(y = 2t^3\) for \(0 \le t \le 1\).
A: \(\dfrac{dx}{dt} = 6t\), \(\dfrac{dy}{dt} = 6t^2\), so \(ds = 6t\sqrt{1 + t^2}\,dt\) and \(s = \left[2\left(1 + t^2\right)^{3/2}\right]_0^1 = 2\left(2\sqrt2 - 1\right)\).
Q: Show that the polar curve \(r = 4\cos\theta\) for \(0 \le \theta \le \pi\) has length \(4\pi\).
A: \(\dfrac{dr}{d\theta} = -4\sin\theta\), so \(r^2 + \left(\dfrac{dr}{d\theta}\right)^2 = 16\cos^2\theta + 16\sin^2\theta = 16\) and \(s = \displaystyle\int_0^\pi4\,d\theta = 4\pi\). (The curve is a circle of diameter 4.)
Q: The curve \(y = 2\sqrt x\) for \(0 \le x \le 3\) is rotated about the \(x\)-axis. Find the exact surface area.
A: \(\dfrac{dy}{dx} = \dfrac{1}{\sqrt x}\), so \(y\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} = 2\sqrt x\sqrt{\dfrac{x+1}{x}} = 2\sqrt{x + 1}\). Then \(S = 2\pi\displaystyle\int_0^32\sqrt{x + 1}\,dx = 4\pi \times \tfrac23\left[(x + 1)^{3/2}\right]_0^3 = \dfrac{8\pi}{3} \times 7 = \dfrac{56\pi}{3}\).
Q: The curve \(y = \tfrac12x^2\) for \(0 \le x \le \sqrt3\) is rotated about the \(y\)-axis. Find the exact surface area.
A: \(\dfrac{dy}{dx} = x\), \(ds = \sqrt{1 + x^2}\,dx\), and \(S = 2\pi\displaystyle\int_0^{\sqrt3}x\sqrt{1 + x^2}\,dx = 2\pi\left[\tfrac13\left(1 + x^2\right)^{3/2}\right]_0^{\sqrt3} = \dfrac{2\pi}{3}(8 - 1) = \dfrac{14\pi}{3}\).
Q: The curve \(x = 2\cos t\), \(y = 2\sin t\) for \(0 \le t \le \tfrac\pi2\) is rotated about the \(x\)-axis. Find the surface area, and say what surface it is.
A: \(\dfrac{ds}{dt} = \sqrt{4\sin^2t + 4\cos^2t} = 2\), so \(S = 2\pi\displaystyle\int_0^{\pi/2}2\sin t \times 2\,dt = 8\pi\left[-\cos t\right]_0^{\pi/2} = 8\pi\). It is a hemisphere of radius 2, whose curved surface is \(2\pi \times 2^2 = 8\pi\).
Q: Write down, without evaluating, an integral for the length of \(y = \sin x\) for \(0 \le x \le \pi\), and evaluate it with a calculator to 3 s.f.
A: \(\dfrac{dy}{dx} = \cos x\), so \(s = \displaystyle\int_0^\pi\sqrt{1 + \cos^2x}\,dx = 3.82\).
Q: Find the length of \(y = x^2\) from \(x = 0\) to \(x = 1\) to 3 s.f.
A: \(s = \displaystyle\int_0^1\sqrt{1 + 4x^2}\,dx\). With \(2x = \sinh u\), this is \(\tfrac12\displaystyle\int\cosh^2u\,du\), giving \(\tfrac{\sqrt5}{2} + \tfrac14\sinh^{-1}2 = 1.48\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find the exact length of the curve \(y = \tfrac23(x - 1)^{3/2}\) from \(x = 2\) to \(x = 5\).
A: \(\dfrac{dy}{dx} = (x - 1)^{1/2}\), so \(\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} = \sqrt x\). [B1]
\(s = \displaystyle\int_2^5\sqrt x\,dx\) [M1] \(= \tfrac23\left(5\sqrt5 - 2\sqrt2\right)\). [A1]
Q: [5 marks] ★★ The curve \(C\) has parametric equations \(x = 4(\cos t + t\sin t)\), \(y = 4(\sin t - t\cos t)\). Find the length of \(C\) for \(0 \le t \le \tfrac\pi2\).
A: \(\dfrac{dx}{dt} = 4(-\sin t + \sin t + t\cos t) = 4t\cos t\). [B1]
\(\dfrac{dy}{dt} = 4(\cos t - \cos t + t\sin t) = 4t\sin t\). [B1]
\(\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2 = 16t^2\), so \(\dfrac{ds}{dt} = 4t\) for \(t \ge 0\). [M1 A1]
\(s = \displaystyle\int_0^{\pi/2}4t\,dt = \left[2t^2\right]_0^{\pi/2} = \dfrac{\pi^2}{2}\). [A1]
Q: [6 marks] ★★ The polar curve \(C\) has equation \(r = \theta^2\) for \(0 \le \theta \le \sqrt3\). Find the exact length of \(C\).
A: \(\dfrac{dr}{d\theta} = 2\theta\). [B1]
\(r^2 + \left(\dfrac{dr}{d\theta}\right)^2 = \theta^4 + 4\theta^2 = \theta^2\left(\theta^2 + 4\right)\). [M1]
\(s = \displaystyle\int_0^{\sqrt3}\theta\sqrt{\theta^2 + 4}\,d\theta\) [A1] (\(\theta \ge 0\)).
Substitute \(u = \theta^2 + 4\), \(du = 2\theta\,d\theta\): [M1]
\(s = \tfrac12\displaystyle\int_4^7u^{1/2}\,du = \tfrac13\left[u^{3/2}\right]_4^7\) [A1] \(= \dfrac{7\sqrt7 - 8}{3}\). [A1]
Q: [5 marks] ★★ The part of the circle \(y = \sqrt{9 - x^2}\) with \(1 \le x \le 2\) is rotated through \(2\pi\) about the \(x\)-axis. Find the exact area of the surface formed.
A: \(\dfrac{dy}{dx} = \dfrac{-x}{\sqrt{9 - x^2}}\), so \(1 + \left(\dfrac{dy}{dx}\right)^2 = \dfrac{9}{9 - x^2}\). [B1]
\(y\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} = \sqrt{9 - x^2} \times \dfrac{3}{\sqrt{9 - x^2}} = 3\). [M1 A1]
\(S = 2\pi\displaystyle\int_1^23\,dx\) [M1] \(= 6\pi\). [A1]
Q: [12 marks] (#math.fm.reduction) ★★★ The cycloid \(C\) has parametric equations \(x = 2(t - \sin t)\), \(y = 2(1 - \cos t)\) for \(0 \le t \le 2\pi\). (a) Show that \(\dfrac{ds}{dt} = 4\sin\dfrac t2\). (b) Find the length of \(C\). (c) The curve \(C\) is rotated through \(2\pi\) about the \(x\)-axis. Show that the area of the surface formed is \(\dfrac{256\pi}{3}\).
H: In (a), use \(1 - \cos t = 2\sin^2\dfrac t2\) to turn \(\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2\) into a perfect square.
H: In (c), \(y = 4\sin^2\dfrac t2\), so the integrand is a multiple of \(\sin^3\dfrac t2\). Put \(u = \dfrac t2\).
H: Use \(\displaystyle\int_0^\pi\sin^3u\,du = 2\int_0^{\pi/2}\sin^3u\,du\) and the reduction formula for \(\int_0^{\pi/2}\sin^nu\,du\).
A: (a) \(\dfrac{dx}{dt} = 2(1 - \cos t)\), \(\dfrac{dy}{dt} = 2\sin t\). [B1]
\(\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2 = 4(2 - 2\cos t) = 16\sin^2\dfrac t2\). [M1 A1]
For \(0 \le t \le 2\pi\), \(\sin\dfrac t2 \ge 0\), so \(\dfrac{ds}{dt} = 4\sin\dfrac t2\). [A1]
(b) \(s = \displaystyle\int_0^{2\pi}4\sin\dfrac t2\,dt = \left[-8\cos\dfrac t2\right]_0^{2\pi}\) [M1] \(= 16\). [A1 A1]
(c) \(S = 2\pi\displaystyle\int_0^{2\pi}y\,\dfrac{ds}{dt}\,dt = 2\pi\int_0^{2\pi}4\sin^2\dfrac t2 \times 4\sin\dfrac t2\,dt = 32\pi\int_0^{2\pi}\sin^3\dfrac t2\,dt\). [M1 A1]
With \(u = \dfrac t2\), \(dt = 2\,du\): \(S = 64\pi\displaystyle\int_0^\pi\sin^3u\,du = 128\pi\int_0^{\pi/2}\sin^3u\,du\). [M1]
The reduction formula gives \(\displaystyle\int_0^{\pi/2}\sin^3u\,du = \dfrac23 \times 1 = \dfrac23\). [M1]
\(S = 128\pi \times \dfrac23 = \dfrac{256\pi}{3}\). [A1]
Q: [10 marks] (#math.fm.polar) ★★★ The curve \(C\) has polar equation \(r = e^{\theta/2}\) for \(0 \le \theta \le \pi\). (a) Find the exact length of \(C\). (b) Find the exact area of the region bounded by \(C\), the initial line and the half-line \(\theta = \pi\). (c) The point \(P\) on \(C\) has parameter \(\theta = \alpha\), and the length of the arc of \(C\) from \(\theta = 0\) to \(P\) is 10. Find \(\alpha\) to 3 s.f.
H: \(\dfrac{dr}{d\theta} = \dfrac12e^{\theta/2}\), so \(r^2 + \left(\dfrac{dr}{d\theta}\right)^2 = \tfrac54e^\theta\).
H: The area of a sector is \(\tfrac12\displaystyle\int r^2\,d\theta\), from [Polar coordinates](#math.fm.polar).
H: For (c), write the arc length as a function of \(\alpha\) and solve for \(e^{\alpha/2}\).
A: (a) \(\dfrac{dr}{d\theta} = \tfrac12e^{\theta/2}\). [B1] \(r^2 + \left(\dfrac{dr}{d\theta}\right)^2 = e^\theta + \tfrac14e^\theta = \tfrac54e^\theta\). [M1]
\(s = \displaystyle\int_0^\pi\dfrac{\sqrt5}{2}e^{\theta/2}\,d\theta\) [A1] \(= \sqrt5\left[e^{\theta/2}\right]_0^\pi = \sqrt5\left(e^{\pi/2} - 1\right)\). [A1]
(b) \(A = \tfrac12\displaystyle\int_0^\pi r^2\,d\theta = \tfrac12\int_0^\pi e^\theta\,d\theta\) [M1] \(= \tfrac12\left(e^\pi - 1\right)\). [A1 A1]
(c) \(\sqrt5\left(e^{\alpha/2} - 1\right) = 10\) [M1], so \(e^{\alpha/2} = 1 + \dfrac{10}{\sqrt5} = 5.472\) [A1] and \(\alpha = 2\ln 5.472 = 3.40\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A soap film is stretched between two circular rings and forms the surface obtained by rotating \(y = \cosh x\) about the \(x\)-axis for \(0 \le x \le a\). (a) Show that the area of the film is \(S = \pi\left(a + \sinh a\cosh a\right)\). (b) Show that the volume enclosed by the film and the two end discs is \(V = \tfrac\pi2\left(a + \sinh a\cosh a\right)\). (c) Hence show that \(S = 2V\), and find \(S\) when \(a = \ln 2\).
H: Both integrals involve \(\displaystyle\int_0^a\cosh^2x\,dx\); use \(\cosh^2x = \tfrac12(1 + \cosh 2x)\) and \(\sinh 2x = 2\sinh x\cosh x\).
H: The volume is \(\pi\displaystyle\int y^2\,dx\); the surface area is \(2\pi\displaystyle\int y\,ds\), and \(ds = \cosh x\,dx\).
A: (a) \(ds = \cosh x\,dx\), so \(S = 2\pi\displaystyle\int_0^a\cosh^2x\,dx\). [M1] \(= \pi\displaystyle\int_0^a(1 + \cosh 2x)\,dx = \pi\left[x + \tfrac12\sinh 2x\right]_0^a\). [M1 A1]
Since \(\tfrac12\sinh 2a = \sinh a\cosh a\), \(S = \pi\left(a + \sinh a\cosh a\right)\). [A1]
(b) \(V = \pi\displaystyle\int_0^a\cosh^2x\,dx\) [M1] \(= \tfrac\pi2\left[x + \tfrac12\sinh 2x\right]_0^a = \tfrac\pi2\left(a + \sinh a\cosh a\right)\). [A1]
(c) \(S = 2V\), since the integrals are the same except for the factor 2. [B1]
For \(a = \ln 2\): \(\sinh a\cosh a = \tfrac34 \times \tfrac54 = \tfrac{15}{16}\), so \(S = \pi\left(\ln 2 + \tfrac{15}{16}\right) = 5.12\). [B1]
Q: [6 marks] ★★★ The curve with polar equation \(r = a\sin^3\dfrac\theta3\) for \(0 \le \theta \le 3\pi\), where \(a > 0\), is a closed loop. Show that its length is \(\dfrac{3\pi a}{2}\).
H: Differentiate with the chain rule: \(\dfrac{dr}{d\theta} = a\sin^2\dfrac\theta3\cos\dfrac\theta3\).
H: Factor \(\sin^4\dfrac\theta3\) out of \(r^2 + \left(\dfrac{dr}{d\theta}\right)^2\), leaving \(\sin^2 + \cos^2\).
H: Use \(\sin^2\dfrac\theta3 = \tfrac12\left(1 - \cos\dfrac{2\theta}{3}\right)\).
A: \(\dfrac{dr}{d\theta} = a\sin^2\dfrac\theta3\cos\dfrac\theta3\). [B1]
\(r^2 + \left(\dfrac{dr}{d\theta}\right)^2 = a^2\sin^4\dfrac\theta3\left(\sin^2\dfrac\theta3 + \cos^2\dfrac\theta3\right) = a^2\sin^4\dfrac\theta3\). [M1 A1]
For \(0 \le \theta \le 3\pi\), \(\sin\dfrac\theta3 \ge 0\), so the root is \(a\sin^2\dfrac\theta3\). [A1]
\(s = a\displaystyle\int_0^{3\pi}\tfrac12\left(1 - \cos\dfrac{2\theta}{3}\right)d\theta = \tfrac a2\left[\theta - \tfrac32\sin\dfrac{2\theta}{3}\right]_0^{3\pi}\) [M1] \(= \dfrac{3\pi a}{2}\). [A1]
:::

:::quiz
? Which is the correct formula for the length of \(y = f(x)\) from \(x = a\) to \(x = b\)?
+ \(\displaystyle\int_a^b\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2}\,dx\)
- \(\displaystyle\int_a^b\left(1 + \left(\dfrac{dy}{dx}\right)^2\right)dx\)
- \(\displaystyle\int_a^b\sqrt{1 + \dfrac{dy}{dx}}\,dx\)
- \(\displaystyle\int_a^b\sqrt{\left(\dfrac{dy}{dx}\right)^2}\,dx\)
> The root comes from Pythagoras on a small chord, and the derivative is squared inside it. Leaving out the root, the square or the 1 gives the other three options, which respectively give a squared length, the wrong slope term and the length of the \(y\)-change only.
? A curve has parametric equations \(x(t)\), \(y(t)\). Its length is
+ \(\displaystyle\int\sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2}\,dt\)
- \(\displaystyle\int\sqrt{1 + \left(\dfrac{dy}{dt}\right)^2}\,dt\)
- \(\displaystyle\int\left(\dfrac{dx}{dt} + \dfrac{dy}{dt}\right)dt\)
- \(\displaystyle\int\sqrt{1 + \left(\dfrac{dy}{dx}\right)^2}\,dt\)
> Both components of the velocity enter, each squared, and there is no extra 1 because \(\dfrac{dx}{dt}\) already takes its place. Adding the components without squaring gives \(\Delta x + \Delta y\), the length of an L-shaped path.
? Which expression is the length of a polar curve \(r = f(\theta)\)?
+ \(\displaystyle\int\sqrt{r^2 + \left(\dfrac{dr}{d\theta}\right)^2}\,d\theta\)
- \(\displaystyle\int\tfrac12r^2\,d\theta\)
- \(\displaystyle\int\sqrt{1 + \left(\dfrac{dr}{d\theta}\right)^2}\,d\theta\)
- \(\displaystyle\int r\,d\theta\)
> The second option is the area of a sector, a different quantity. The third forgets that the circular part of the motion has size \(r\,d\theta\). The fourth is the length only when \(r\) is constant, and it fails for every other curve.
? The curve \(y = x^3\) for \(0 \le x \le 1\) is rotated about the \(y\)-axis. Which integral gives the surface area?
+ \(2\pi\displaystyle\int_0^1x\sqrt{1 + 9x^4}\,dx\)
- \(2\pi\displaystyle\int_0^1x^3\sqrt{1 + 9x^4}\,dx\)
- \(\pi\displaystyle\int_0^1x^6\,dx\)
- \(2\pi\displaystyle\int_0^1x\,dx\)
> About the \(y\)-axis the radius of the circle swept is \(x\), so \(x\) multiplies \(ds\). Using \(y = x^3\) is the \(x\)-axis formula, the third option is a volume, and the fourth leaves out \(ds\).
? Which is \(\sqrt{9\sin^2t\cos^2t}\) for \(t\) in \(\left[0, \pi\right]\)?
+ \(3\left|\sin t\cos t\right|\)
- \(3\sin t\cos t\)
- \(9\sin t\cos t\)
- \(3\sin^2t\cos t\)
> A root is never negative, so the square root of a square is a modulus. \(3\sin t\cos t\) is negative on \(\left(\tfrac\pi2, \pi\right)\), and integrating it there would subtract length. The other options mis-handle the 9 or the square.
? The surface of a sphere of radius \(R\) is formed by rotating a semicircle. What does \(2\pi\displaystyle\int y\,ds\) give for \(y = \sqrt{R^2 - x^2}\), \(-R \le x \le R\)?
+ \(4\pi R^2\)
- \(2\pi R^2\)
- \(\pi R^2\)
- \(\tfrac43\pi R^3\)
> Here \(y\,ds = R\,dx\), so \(S = 2\pi R \times 2R = 4\pi R^2\), the known surface area of a sphere. \(\tfrac43\pi R^3\) is the volume, and \(2\pi R^2\) is the area of a hemisphere.
:::

:::checklist What you can now do
- [ ] I can derive the arc length formula from a small chord and state the Cartesian, parametric and polar forms.
- [ ] I can find the arc length of a curve \(y = f(x)\) or \(x = g(y)\), and recognise when \(1 + \left(\dfrac{dy}{dx}\right)^2\) is a perfect square.
- [ ] I can find the arc length of a parametric curve, using identities and moduli correctly.
- [ ] I can find the arc length of a polar curve, using \(r^2 + \left(\dfrac{dr}{d\theta}\right)^2\).
- [ ] I can find the surface area formed by rotating a Cartesian curve about the \(x\)-axis or the \(y\)-axis.
- [ ] I can find the surface area formed by rotating a parametric curve about an axis.
- [ ] I can give an exact answer or a 3 s.f. answer as asked, and check a length against the straight line joining the end points.
:::

:::recap
- A chord has \(\delta s^2 = \delta x^2 + \delta y^2\); the length of a curve is \(\int ds\).
- Cartesian \(y(x)\): \(s = \int\sqrt{1 + (y')^2}\,dx\); for \(x(y)\): \(\int\sqrt{1 + (dx/dy)^2}\,dy\).
- Parametric: \(s = \int\sqrt{\dot x^2 + \dot y^2}\,dt\), with \(\dot x = \dfrac{dx}{dt}\) and \(\dot y = \dfrac{dy}{dt}\); polar: \(s = \int\sqrt{r^2 + (dr/d\theta)^2}\,d\theta\). None of these is on MF19.
- Exam curves make the root a perfect square: \(1 + \sinh^2 = \cosh^2\), \(\sin^2 + \cos^2 = 1\), \(1 - \cos t = 2\sin^2\tfrac t2\), or \(\left(\tfrac p2 + \tfrac1{2p}\right)^2\). A root is non-negative: use a modulus or a sign argument.
- Surface of revolution: \(S = 2\pi\int(\text{distance from the axis})\,ds\): \(y\) for the \(x\)-axis, \(x\) for the \(y\)-axis. Polar surface areas are not examined.
- Check a length against the chord joining its ends, and test a surface formula on a sphere or a cone.
:::

:::links
- practise: [Further integration booklets](https://madasmaths.com/archive_maths_booklets_further_topics_integration.html) · MadAsMaths · free booklets with answers on arc length and surface area
- read: [Arc length](https://tutorial.math.lamar.edu/Classes/CalcII/ArcLength.aspx) · Paul's Online Notes · the Cartesian, parametric and polar forms, with examples
- read: [Surface area](https://tutorial.math.lamar.edu/Classes/CalcII/SurfaceArea.aspx) · Paul's Online Notes · surfaces of revolution about both axes
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot the cycloid, cardioid and astroid from this chapter
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [De Moivre's theorem and trigonometry](#math.fm.complex) turns complex numbers into rotations, and uses them to prove trigonometric identities and find roots.
