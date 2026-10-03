@chapter math.f.geometry
@title Geometry and trigonometry basics
@level pre
@paper Prior knowledge for CAIE 9709 · Edexcel IAL · AQA/OCR/Edexcel (GCSE or IGCSE Geometry and Trigonometry)
@time 6–8 hours
@summary Angle facts, Pythagoras, sine, cosine and tangent in right-angled triangles, exact values for 30°, 45° and 60°, the sine rule, cosine rule and area formula for any triangle, circle facts, arc length, sector area and the volumes and surface areas of solids.

:::why
Trigonometry is the tool for every problem that involves angles: forces in Mechanics, bearings, vectors and the whole of the Pure trigonometry chapters. The sine rule, cosine rule and the area formula \(\tfrac12 ab\sin C\) are used again in [Circular measure](#math.p1.circular) and in Mechanics. Practise until they take seconds, not minutes.
:::

**Before you start**, you need [Algebra from scratch](#math.f.algebra) (rearranging formulas) and [Indices, surds and standard form](#math.f.powers) (square roots and exact answers). The next chapter after this one is [Quadratics](#math.p1.quadratics) in the Pure 1 course.

## Angle facts

Angles are measured in degrees: a full turn is \(360^\circ\). These facts need no proof in an exam, but you need to quote them as reasons.

:::key Angle facts
- Angles on a straight line add up to \(180^\circ\). Angles around a point add up to \(360^\circ\).
- **Vertically opposite** angles (where two lines cross) are equal.
- The angles of a triangle add up to \(180^\circ\). An **exterior angle** of a triangle equals the sum of the two interior angles opposite it.
- With parallel lines: **alternate** angles (a Z shape) are equal, **corresponding** angles (an F shape) are equal, and **co-interior** angles (a C shape) add up to \(180^\circ\).
- An **isosceles** triangle has two equal sides and two equal base angles. An **equilateral** triangle has three equal sides and three angles of \(60^\circ\).
- The interior angles of a polygon with \(n\) sides add up to \((n - 2) \times 180^\circ\). The exterior angles of any polygon add up to \(360^\circ\), so each exterior angle of a **regular** polygon is \(\dfrac{360^\circ}{n}\).
:::

:::eg Each interior angle of a regular polygon is \(156^\circ\). How many sides has the polygon? Also find the sum of the interior angles of a hexagon.
The exterior angle is \(180^\circ - 156^\circ = 24^\circ\), so \(n = \dfrac{360}{24} = 15\) sides.

For a hexagon, \(n = 6\): the sum is \((6 - 2) \times 180^\circ = 720^\circ\).
:::

## Pythagoras' theorem

:::key Pythagoras' theorem
In a right-angled triangle the square on the **hypotenuse** (the side opposite the right angle, always the longest) equals the sum of the squares on the other two sides:
\[c^2 = a^2 + b^2\]
The converse is also true: if three sides satisfy \(c^2 = a^2 + b^2\), the triangle has a right angle. The triples \(3, 4, 5\), \(5, 12, 13\), \(8, 15, 17\) and \(7, 24, 25\) are worth recognising.
:::

:::eg An isosceles triangle has sides \(13\) cm, \(13\) cm and \(10\) cm. Find its height and its area.
Drop a perpendicular from the top to the base. It bisects the base, making a right-angled triangle with hypotenuse \(13\) and base \(5\):
\[h^2 = 13^2 - 5^2 = 169 - 25 = 144, \quad h = 12\]
The height is \(12\) cm and the area is \(\tfrac12 \times 10 \times 12 = 60\) cm².
:::

## Sine, cosine and tangent

In a right-angled triangle, name the sides from the point of view of an angle \(\theta\): the **hypotenuse** is opposite the right angle, the **opposite** side is across from \(\theta\), and the **adjacent** side is next to \(\theta\).

:::key SOH CAH TOA
\[\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} \qquad \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} \qquad \tan\theta = \frac{\text{opposite}}{\text{adjacent}}\]
To find a **side**, use the ratio directly. To find an **angle**, use the inverse function: \(\theta = \sin^{-1}\left(\dfrac{\text{opp}}{\text{hyp}}\right)\). Make sure your calculator is in **degree** mode.
:::

Two more facts follow: \(\tan\theta = \dfrac{\sin\theta}{\cos\theta}\) and \(\sin^2\theta + \cos^2\theta = 1\) (from Pythagoras with hypotenuse 1). These return in [Trigonometry](#math.p1.trig).

:::eg In a right-angled triangle the hypotenuse is \(12\) cm and one angle is \(35^\circ\). Find the side opposite that angle. In another, the sides adjacent and opposite \(\theta\) are \(9\) and \(7\): find \(\theta\).
Opposite \(= 12 \sin 35^\circ = 6.883\), so the side is \(6.88\) cm (3 s.f.).

Opposite and adjacent give tangent: \(\tan\theta = \dfrac79\), so \(\theta = \tan^{-1}\left(\dfrac79\right) = 37.9^\circ\) (1 d.p.).
:::

:::def Angle of elevation and angle of depression
The angle of elevation of a point is the angle measured **up** from the horizontal to the line of sight. The angle of depression is the angle measured **down** from the horizontal.
:::

The angle of depression of a boat from a cliff equals the angle of elevation of the cliff from the boat (alternate angles).

:::eg From a point on level ground \(40\) m from the foot of a tower the angle of elevation of the top is \(28^\circ\). Find the height of the tower.
The tower is opposite the angle and the ground distance is adjacent: \(\tan 28^\circ = \dfrac{h}{40}\), so \(h = 40 \tan 28^\circ = 21.27\ldots\), or \(21.3\) m (3 s.f.).
:::

## Exact values of sin, cos and tan

For the angles \(30^\circ\), \(45^\circ\) and \(60^\circ\) you must know the exact values with no calculator. They come from two triangles: half of a square (sides 1, 1, \(\sqrt2\)) and half of an equilateral triangle of side 2 (sides 1, \(\sqrt3\), 2).

:::html
<figure class="fig wide"><svg viewBox="28 50 440 230" role="img" aria-label="Two special right-angled triangles: a triangle with two sides of length 1, hypotenuse root 2 and two angles of 45 degrees; and a triangle with hypotenuse 2, short side 1, long side root 3 and angles of 30 and 60 degrees.">
<polygon class="f1 s-acc sw2" points="60,240 200,240 60,100"/>
<path class="ln thin" d="M60 224 L76 224 L76 240"/>
<text class="tl tc" x="130" y="262">1</text>
<text class="tl tc" x="44" y="176">1</text>
<text class="tl halo" x="146" y="156">√2</text>
<text class="tl halo" x="150" y="232">45°</text>
<text class="tl halo" x="68" y="134">45°</text>
<polygon class="f2 s-acc2 sw2" points="340,240 440,240 340,67"/>
<path class="ln thin" d="M340 224 L356 224 L356 240"/>
<text class="tl tc" x="390" y="262">1</text>
<text class="tl tc" x="322" y="158">√3</text>
<text class="tl halo" x="408" y="146">2</text>
<text class="tl halo" x="402" y="231">60°</text>
<text class="tl halo" x="346" y="136">30°</text>
</svg><figcaption>Left: half a square of side 1. Right: half an equilateral triangle of side 2. Read every exact value from these two triangles.</figcaption></figure>
:::

| \(\theta\) | \(30^\circ\) | \(45^\circ\) | \(60^\circ\) |
|---|---|---|---|
| \(\sin\theta\) | \(\dfrac12\) | \(\dfrac{1}{\sqrt2} = \dfrac{\sqrt2}{2}\) | \(\dfrac{\sqrt3}{2}\) |
| \(\cos\theta\) | \(\dfrac{\sqrt3}{2}\) | \(\dfrac{1}{\sqrt2} = \dfrac{\sqrt2}{2}\) | \(\dfrac12\) |
| \(\tan\theta\) | \(\dfrac{1}{\sqrt3} = \dfrac{\sqrt3}{3}\) | \(1\) | \(\sqrt3\) |

:::exam Learn the triangles, not the table
Exact values are **not** on the MF19 formula list, so you must produce them from memory. Draw the two triangles in the margin and read the ratios from them, then you cannot mix up sine and cosine. "Show that" and "exact value" questions in Pure 1 and Pure 3 rely on this.
:::

## Triangles that are not right-angled

For any triangle, label the vertices \(A\), \(B\), \(C\) and call the side opposite each vertex \(a\), \(b\), \(c\) (the lowercase letter is **opposite** the capital letter).

:::html
<figure class="fig"><svg viewBox="33 14 522 262" role="img" aria-label="A triangle with vertices A at the top, B at the bottom left and C at the bottom right. Side a is opposite A along the bottom, side b is opposite B, and side c is opposite C.">
<polygon class="f1 s-acc sw2" points="210,40 70,230 520,230"/>
<text class="tb" x="204" y="30">A</text>
<text class="tb" x="48" y="248">B</text>
<text class="tb" x="528" y="248">C</text>
<text class="tl tb tc" x="295" y="262">a</text>
<text class="tl tb halo" x="392" y="128">b</text>
<text class="tl tb halo" x="118" y="128">c</text>
</svg><figcaption>Side \(a\) is opposite angle \(A\), side \(b\) is opposite \(B\), and side \(c\) is opposite \(C\).</figcaption></figure>
:::

:::formula Sine rule, cosine rule and area
\[\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}\]
\[a^2 = b^2 + c^2 - 2bc\cos A \qquad \cos A = \frac{b^2 + c^2 - a^2}{2bc}\]
\[\text{Area} = \tfrac12 ab\sin C\]
Use the **sine rule** when you know a side and its opposite angle (a "matching pair") and one more piece. Use the **cosine rule** when you know two sides and the angle **between** them, or all three sides. The area formula needs two sides and the **included** angle. None of these is on MF19, so learn them.
:::

:::eg In triangle \(ABC\), \(A = 42^\circ\), \(B = 71^\circ\) and \(a = 8.5\) cm. Find \(b\). Then find \(c\).
The matching pair is \(a\) and \(A\). Using the sine rule,
\[\frac{b}{\sin 71^\circ} = \frac{8.5}{\sin 42^\circ} \implies b = \frac{8.5 \sin 71^\circ}{\sin 42^\circ} = 12.01\ldots\]
So \(b = 12.0\) cm. The third angle is \(C = 180^\circ - 42^\circ - 71^\circ = 67^\circ\), and \(c = \dfrac{8.5 \sin 67^\circ}{\sin 42^\circ} = 11.7\) cm.
:::

:::eg Find side \(a\) when \(b = 7\), \(c = 9\) and \(A = 62^\circ\). Find the largest angle of a triangle with sides \(5\), \(7\) and \(10\).
Two sides and the angle between them, so use the cosine rule:
\[\begin{aligned} a^2 &= 7^2 + 9^2 - 2(7)(9)\cos 62^\circ \\ &= 130 - 126\cos 62^\circ = 70.85 \end{aligned}\]
So \(a = 8.42\) cm.

For the second triangle the largest angle \(C\) is opposite the longest side \(10\):
\[\cos C = \frac{5^2 + 7^2 - 10^2}{2(5)(7)} = \frac{-26}{70} = -0.3714\ldots, \quad C = 111.8^\circ\]
A negative cosine means an obtuse angle. The calculator gives it correctly: do not drop the minus sign.
:::

:::warn The ambiguous case of the sine rule
When you know two sides and an angle **not** between them, \(\sin B = k\) has two solutions in a triangle: \(B\) and \(180^\circ - B\). For \(a = 8\), \(b = 10\), \(A = 40^\circ\), \(\sin B = \dfrac{10 \sin 40^\circ}{8} = 0.8035\), so \(B = 53.5^\circ\) or \(B = 126.5^\circ\). Both fit because \(40 + 126.5 < 180\). If the question does not tell you which, give both. To avoid the problem, find an angle with the **cosine** rule, which gives one answer.
:::

:::eg (Exam style) In triangle \(ABC\), \(AB = 8\) cm, \(AC = 11\) cm and angle \(BAC = 58^\circ\). Find (a) \(BC\), (b) angle \(ABC\), (c) the area of the triangle.
(a) Cosine rule with the included angle:
\[BC^2 = 8^2 + 11^2 - 2(8)(11)\cos 58^\circ\] [M1]
\[BC^2 = 185 - 176\cos 58^\circ = 91.73\ldots, \quad BC = 9.58 \text{ cm}\] [A1]

(b) Use the cosine rule again to avoid the ambiguous case (keep \(BC\) as \(9.578\) from the calculator):
\[\cos B = \frac{9.578^2 + 8^2 - 11^2}{2(9.578)(8)} = 0.2267\ldots\] [M1]
\[\angle ABC = 76.9^\circ\] [A1]

(c) Area \(= \tfrac12 \times 8 \times 11 \times \sin 58^\circ\) [M1] \(= 37.3\) cm². [A1]
Check: \(\sin B = \dfrac{11 \sin 58^\circ}{9.578} = 0.974\), which gives \(76.9^\circ\) (or \(103.1^\circ\), which the cosine value rules out).
:::

:::eg (Exam style) From a point \(A\) on level ground the angle of elevation of the top of a tower is \(30^\circ\). From a point \(B\), \(50\) m closer to the tower and on the same line, the angle of elevation is \(45^\circ\). Find the exact height of the tower.
Let the height be \(h\) and \(B\) be \(x\) m from the foot. At \(B\): \(\tan 45^\circ = \dfrac{h}{x}\), so \(h = x\). [B1]

At \(A\): \(\tan 30^\circ = \dfrac{h}{x + 50}\), so \(\dfrac{1}{\sqrt3} = \dfrac{x}{x + 50}\). [M1]
\[\begin{aligned} x + 50 &= \sqrt3\,x \\ 50 &= x(\sqrt3 - 1) \\ x &= \frac{50}{\sqrt3 - 1} \end{aligned}\] [M1]
Rationalise with \((\sqrt3 + 1)\): \(x = \dfrac{50(\sqrt3 + 1)}{3 - 1} = 25(\sqrt3 + 1)\). [M1]

The tower is \(25(1 + \sqrt3)\) m, which is \(68.3\) m. [A1]
:::

## Circle facts

A **radius** joins the centre to the circle, a **chord** joins two points on the circle, a **diameter** is a chord through the centre, a **tangent** touches the circle at one point.

:::key Circle theorems you need
- A tangent is perpendicular to the radius at the point of contact.
- The angle in a semicircle is \(90^\circ\): if \(AB\) is a diameter and \(C\) is on the circle, then angle \(ACB = 90^\circ\).
- The perpendicular from the centre to a chord bisects the chord.
- Two tangents drawn from the same outside point are equal in length.
- The angle at the centre is twice the angle at the circumference on the same arc.
:::

:::eg \(PT\) is a tangent to a circle with centre \(O\) and radius \(5\) cm, touching it at \(T\). \(OP = 13\) cm. Find \(PT\). Also, \(AB\) is a diameter and \(C\) is on the circle with angle \(CAB = 35^\circ\): find angle \(ABC\).
The tangent meets the radius at a right angle, so \(OTP\) is a right-angled triangle with hypotenuse \(OP\):
\[PT^2 = 13^2 - 5^2 = 144, \quad PT = 12 \text{ cm}\]
In the second circle angle \(ACB = 90^\circ\) (angle in a semicircle), so angle \(ABC = 180^\circ - 90^\circ - 35^\circ = 55^\circ\).
:::

## Arcs, sectors and solids

A **sector** is a slice of a circle between two radii. An **arc** is part of the circumference. If the angle at the centre is \(\theta\) **degrees**, the sector is the fraction \(\dfrac{\theta}{360}\) of the whole circle.

:::key Arc length and sector area (degrees)
\[\text{arc length} = \frac{\theta}{360} \times 2\pi r \qquad \text{sector area} = \frac{\theta}{360} \times \pi r^2\]
Radians give simpler formulas, \(s = r\theta\) and \(A = \tfrac12 r^2\theta\): see [Circular measure](#math.p1.circular).
:::

:::eg A sector has radius \(8\) cm and angle \(75^\circ\). Find its arc length and area.
\[\text{Arc} = \frac{75}{360} \times 2\pi \times 8 = 10.47\ldots \approx 10.5 \text{ cm}\]
\[\text{Area} = \frac{75}{360} \times \pi \times 8^2 = 41.89\ldots \approx 41.9 \text{ cm}^2\]
:::

For solids, the volume of a **prism** (a solid with constant cross-section) is \(\text{area of cross-section} \times \text{length}\). A **cylinder** is a circular prism: \(V = \pi r^2 h\), curved surface area \(2\pi r h\). These two you must remember. The cone and sphere formulae **are** given on MF19.

| Solid | Volume | Surface area | On MF19? |
|---|---|---|---|
| Cylinder, radius \(r\), height \(h\) | \(\pi r^2 h\) | curved \(2\pi r h\) | no |
| Cone, base radius \(r\), slant height \(l\), height \(h\) | \(\tfrac13 \pi r^2 h\) | curved \(\pi r l\) | yes |
| Sphere, radius \(r\) | \(\tfrac43 \pi r^3\) | \(4\pi r^2\) | yes |

For a cone, \(l^2 = r^2 + h^2\) (Pythagoras). The curved surface area excludes the circular base.

:::eg A cone has base radius \(6\) cm and height \(8\) cm. Find its slant height, curved surface area and volume.
\(l = \sqrt{6^2 + 8^2} = 10\) cm. Curved surface area \(= \pi \times 6 \times 10 = 60\pi = 188\) cm² (3 s.f.). Volume \(= \tfrac13 \pi \times 36 \times 8 = 96\pi = 302\) cm³ (3 s.f.).
:::

:::board Other boards
Edexcel IAL and the UK A Levels assume most of this from IGCSE or GCSE. The sine rule, cosine rule and \(\tfrac12 ab\sin C\) are used in their Pure Year 1 content too. Cambridge gives none of them on MF19, so check your own board's formula booklet to see what you must memorise.
:::

:::try Start easy, finish at exam standard
Q: Find the interior and exterior angle of a regular octagon.
A: Exterior \(= 360 \div 8 = 45^\circ\). Interior \(= 180 - 45 = 135^\circ\).
Q: (a) A right-angled triangle has legs \(9\) and \(40\). Find the hypotenuse. (b) A right-angled triangle has hypotenuse \(17\) and one leg \(8\). Find the other leg.
A: (a) \(\sqrt{81 + 1600} = \sqrt{1681} = 41\). (b) \(\sqrt{289 - 64} = \sqrt{225} = 15\).
Q: (a) A right-angled triangle has hypotenuse \(15\) and an angle of \(40^\circ\). Find the side opposite the angle. (b) The hypotenuse is \(9\) and a side is \(5\). Find the angle opposite that side.
A: (a) \(15\sin 40^\circ = 9.64\). (b) \(\sin\theta = \tfrac59\), so \(\theta = 33.7^\circ\).
Q: A \(5\) m ladder rests against a vertical wall with its foot \(1.5\) m from the wall. Find the angle it makes with the ground and how high it reaches.
A: \(\cos\theta = \dfrac{1.5}{5} = 0.3\), so \(\theta = 72.5^\circ\). Height \(= \sqrt{25 - 2.25} = 4.77\) m.
Q: Find the exact value of \(\sin 45^\circ \cos 45^\circ + \tan 60^\circ \tan 30^\circ\).
A: \(\dfrac{\sqrt2}{2} \times \dfrac{\sqrt2}{2} = \dfrac12\) and \(\sqrt3 \times \dfrac{1}{\sqrt3} = 1\). The sum is \(\dfrac32\).
Q: In triangle \(ABC\), \(a = 6\), \(b = 8\), \(c = 11\). Find the largest angle.
A: The largest angle is \(C\), opposite \(11\): \(\cos C = \dfrac{36 + 64 - 121}{2 \times 6 \times 8} = \dfrac{-21}{96}\), so \(C = 102.6^\circ\).
Q: Find the area of a triangle with two sides \(7\) cm and \(9\) cm and an included angle of \(125^\circ\).
A: \(\tfrac12 \times 7 \times 9 \times \sin 125^\circ = 25.8\) cm².
Q: \(PT\) is a tangent to a circle, centre \(O\), radius \(7\) cm. \(OP = 25\) cm. Find \(PT\). A sector of radius \(12\) cm has arc length \(15\) cm; find its angle.
A: \(PT = \sqrt{625 - 49} = 24\) cm. Angle \(= \dfrac{15}{2\pi \times 12} \times 360^\circ = 71.6^\circ\).
Q: (Exam style) In triangle \(ABC\), \(AB = 12\) cm, \(BC = 9\) cm and angle \(BAC = 40^\circ\). (a) Find the two possible values of angle \(ACB\). (b) Find the area of the triangle for the acute value.
A: (a) The sine rule gives \(\dfrac{\sin C}{12} = \dfrac{\sin 40^\circ}{9}\). [M1] \(\sin C = 0.857\ldots\), so \(C = 59.0^\circ\) [A1] or \(C = 180^\circ - 59.0^\circ = 121.0^\circ\). [A1]

(b) For \(C = 59.0^\circ\), angle \(B = 180 - 40 - 59.0 = 81.0^\circ\). [M1] Area \(= \tfrac12 \times 12 \times 9 \times \sin 81.0^\circ = 53.3\) cm². [A1]
:::

:::quiz
? What is the exact value of \(\tan 60^\circ\)?
- \(\dfrac{1}{\sqrt3}\)
+ \(\sqrt3\)
- \(\dfrac{\sqrt3}{2}\)
- \(\dfrac12\)
> In the half-equilateral triangle, the side opposite \(60^\circ\) is \(\sqrt3\) and the adjacent side is \(1\), so \(\tan 60^\circ = \sqrt3\). The value \(\dfrac{1}{\sqrt3}\) is \(\tan 30^\circ\), and \(\dfrac{\sqrt3}{2}\) is \(\sin 60^\circ\).
? Which formula finds \(a\) when you know \(b\), \(c\) and angle \(A\)?
- \(\dfrac{a}{\sin A} = \dfrac{b}{\sin B}\)
- \(a^2 = b^2 + c^2\)
+ \(a^2 = b^2 + c^2 - 2bc\cos A\)
- \(a = \tfrac12 bc\sin A\)
> Two sides and the angle between them is the cosine rule. The sine rule needs a matching pair, \(a^2 = b^2 + c^2\) is Pythagoras (only for a right angle), and the last option confuses the area formula with a side length.
? A regular polygon has exterior angle \(20^\circ\). How many sides does it have?
- \(9\)
+ \(18\)
- \(16\)
- \(160\)
> The exterior angles add up to \(360^\circ\), so \(n = 360 \div 20 = 18\). Dividing \(180\) by \(20\) gives \(9\), which uses the wrong total. The number \(160\) is the interior angle, not the number of sides.
? A cone has base radius \(3\) cm and vertical height \(4\) cm. What is its curved surface area?
- \(12\pi\)
+ \(15\pi\)
- \(36\pi\)
- \(20\pi\)
> The curved surface area is \(\pi r l\) with the **slant height** \(l = \sqrt{3^2 + 4^2} = 5\), so it is \(\pi \times 3 \times 5 = 15\pi\). Using the vertical height 4 gives \(12\pi\), a very common slip, and \(36\pi\) comes from \(\pi r h\) with the wrong height.
? In triangle \(ABC\), \(a = 5\), \(b = 7\) and \(\cos C = 0.2\). What is \(c^2\)?
- \(88\)
+ \(60\)
- \(67\)
- \(59.2\)
> \(c^2 = a^2 + b^2 - 2ab\cos C = 25 + 49 - 70(0.2) = 60\). Using a plus sign gives \(88\), leaving out the factor \(2\) gives \(67\), and \(59.2\) comes from multiplying \(74\) by \(1 - 0.2\), which is not in the formula.
:::

:::recap
- Angles: triangle \(180^\circ\), straight line \(180^\circ\), point \(360^\circ\); polygon interior sum \((n - 2) \times 180^\circ\); regular polygon exterior angle \(360^\circ \div n\).
- Pythagoras \(c^2 = a^2 + b^2\) and SOH CAH TOA for right-angled triangles. Use inverse functions for angles, with the calculator in degree mode.
- Exact values at \(30^\circ\), \(45^\circ\), \(60^\circ\) come from the two special triangles. They are not on MF19.
- Sine rule: matching pair. Cosine rule: two sides and the included angle, or three sides. Area \(\tfrac12 ab\sin C\). Beware the ambiguous case with two sides and a non-included angle.
- Tangent \(\perp\) radius; angle in a semicircle \(=90^\circ\). Arc \(=\frac{\theta}{360} \times 2\pi r\), sector \(=\frac{\theta}{360} \times \pi r^2\).
- MF19 gives sphere and cone formulae; you must remember the cylinder and prism.
:::

:::links
- watch: [Exact trig ratios for 30°, 45° and 60°](https://www.examsolutions.net/tutorials/trig-ratios-multiples-30-45-60/) · ExamSolutions · the two triangles you need to remember
- practise: [High School Geometry](https://www.khanacademy.org/math/geometry) · Khan Academy · Pythagoras and right-angled trigonometry with practice
- practise: [Trigonometry](https://www.khanacademy.org/math/trigonometry) · Khan Academy · includes the sine and cosine rules
- explore: [Thinking about Geometry](https://undergroundmathematics.org/thinking-about-geometry) · Underground Mathematics · geometry problems that need real thought
- read: [Trigonometry](https://www.mathsisfun.com/algebra/trigonometry.html) · Maths is Fun · SOH CAH TOA and beyond, with interactive diagrams
- read: [Geometry index](https://www.mathsisfun.com/geometry/index.html) · Maths is Fun · angles, circles, area and volume

Links checked 3 October 2026.
:::
Next: [Quadratics](#math.p1.quadratics).
