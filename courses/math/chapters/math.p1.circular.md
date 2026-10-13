@chapter math.p1.circular
@title Circular measure
@level as
@paper CAIE P1 · Edexcel IAL P1 · AQA/OCR/Edexcel Pure Year 1
@time 4–6 hours
@summary Radians as a measure of angle, converting between radians and degrees, arc length \(s = r\theta\), sector area \(A = \tfrac12 r^2\theta\), segments, and problems that combine sectors with triangles.

:::why
Calculus and advanced trigonometry work cleanly only when angles are in radians: \(\dfrac{d}{dx}(\sin x) = \cos x\) is true only for \(x\) in radians. Radians also make arc length and sector area simple formulas. Circular-measure questions in Paper 1 combine arcs, sectors, triangles and Pythagoras, so it pays to know the formulas cold and to draw a clear diagram each time.
:::

**Before you start**, you need arc length and sector area in degrees, the sine and cosine rules and the area formula \(\tfrac12 ab\sin C\) from [Geometry and trigonometry basics](#math.f.geometry). Radians are used again in [Trigonometry](#math.p1.trig) and in calculus.

:::try Warm-up
Q: Find the length of an arc of a circle of radius 6 cm with angle \(60^\circ\) at the centre. (from [Geometry and trigonometry basics](#math.f.geometry))
A: \(\dfrac{60}{360} \times 2\pi \times 6 = 2\pi = 6.28\) cm.
Q: Find the area of a triangle with two sides 7 cm and 10 cm and an angle of \(30^\circ\) between them. (from [Geometry and trigonometry basics](#math.f.geometry))
A: \(\tfrac12 \times 7 \times 10 \times \sin 30^\circ = 17.5\,\mathrm{cm^2}\).
Q: Solve \(r^2 + 2r - 24 = 0\) for positive \(r\). (from [Quadratics](#math.p1.quadratics))
A: \((r + 6)(r - 4) = 0\), so \(r = 4\) (the root \(-6\) is rejected).
:::

## What a radian is

Degrees come from dividing a full turn into 360 arbitrary parts. Radians come from the circle itself.

:::def Radian
One radian is the angle at the centre of a circle subtended by an arc whose length equals the radius. An angle of \(\theta\) radians at the centre of a circle of radius \(r\) cuts off an arc of length \(r\theta\).
:::

:::html
<figure class="fig"><svg viewBox="70 50 330 185" role="img" aria-label="A sector of a circle with two radii of length r and an arc also of length r. The angle between the radii is one radian.">
<path class="f1 s-acc sw2" d="M120 200L270 200A150 150 0 0 0 201.05 73.78Z"/>
<path class="ln-m" d="M160 200A40 40 0 0 0 141.6 166.3"/>
<circle class="fi" cx="120" cy="200" r="3.5"/>
<text class="tl tc" x="195" y="222">r</text>
<text class="tl halo" x="146" y="128" text-anchor="end">r</text>
<text class="tl" x="262" y="120">arc length r</text>
<text class="tl halo" x="166" y="188">1 rad</text>
</svg><figcaption>When the arc is as long as the radius, the angle at the centre is one radian, about \(57.3^\circ\).</figcaption></figure>
:::

The whole circumference is \(2\pi r\), which is \(2\pi\) radiuses, so a full turn is \(2\pi\) radians. This gives the conversion.

:::key Radians and degrees
\[2\pi \text{ radians} = 360^\circ \qquad \pi \text{ radians} = 180^\circ\]
- Degrees to radians: multiply by \(\dfrac{\pi}{180}\).
- Radians to degrees: multiply by \(\dfrac{180}{\pi}\).
Radian conversion is **not** on MF19. Remember \(\pi = 180^\circ\) and you can rebuild everything.
:::

| Degrees | \(30^\circ\) | \(45^\circ\) | \(60^\circ\) | \(90^\circ\) | \(180^\circ\) | \(270^\circ\) | \(360^\circ\) |
|---|---|---|---|---|---|---|---|
| Radians | \(\dfrac{\pi}{6}\) | \(\dfrac{\pi}{4}\) | \(\dfrac{\pi}{3}\) | \(\dfrac{\pi}{2}\) | \(\pi\) | \(\dfrac{3\pi}{2}\) | \(2\pi\) |

:::eg Convert \(72^\circ\) and \(135^\circ\) to radians, and \(2.5\) radians and \(\dfrac{7\pi}{6}\) to degrees.
\(72^\circ = 72 \times \dfrac{\pi}{180} = \dfrac{2\pi}{5}\) radians, which is \(1.26\) (3 s.f.).

\(135^\circ = 135 \times \dfrac{\pi}{180} = \dfrac{3\pi}{4}\) radians, which is \(2.36\) (3 s.f.).

\(2.5\) radians \(= 2.5 \times \dfrac{180}{\pi} = 143.2^\circ\) (1 d.p.). \(\dfrac{7\pi}{6}\) radians \(= \dfrac{7 \times 180}{6} = 210^\circ\).
:::

:::tip Radian mode
When an angle has no degree sign, it is in radians. Set the calculator to **RAD** mode before you evaluate \(\sin\), \(\cos\) or \(\tan\) of it. Check yourself: \(\sin 1\) is \(0.841\) in radian mode and \(0.0175\) in degree mode. Angles like \(\dfrac{\pi}{3}\) are best left exact in answers. Cambridge accepts either \(\dfrac{\pi}{3}\) or \(1.05\) (3 s.f.) unless the question says "exact".
:::

## Arc length and sector area

A **sector** is the region between two radii and an arc. A **minor sector** has an angle under \(\pi\); a **major sector** is more than \(\pi\). If the angle at the centre is \(\theta\) radians, the arc is the fraction \(\dfrac{\theta}{2\pi}\) of the circumference, and the sector is the same fraction of the area:

\[s = \frac{\theta}{2\pi} \times 2\pi r = r\theta \qquad A = \frac{\theta}{2\pi} \times \pi r^2 = \tfrac12 r^2\theta\]

:::formula Arc length and sector area
For a sector of radius \(r\) and angle \(\theta\) **in radians**:
\[s = r\theta \qquad A = \tfrac12 r^2\theta\]
Both are given on MF19, but only for radians. The perimeter of a sector is \(2r + r\theta\) (two radii plus the arc).
:::

:::eg A sector has radius \(6\) cm and angle \(1.2\) radians. Find its arc length, perimeter and area.
\(s = r\theta = 6 \times 1.2 = 7.2\) cm. The perimeter is \(2 \times 6 + 7.2 = 19.2\) cm. The area is \(\tfrac12 \times 36 \times 1.2 = 21.6\) cm².
:::

:::eg (a) An arc of length \(10\) cm is cut from a circle of radius \(8\) cm. Find the angle at the centre. (b) A sector with angle \(0.9\) radians has area \(45\) cm². Find the radius. (c) A sector of radius \(8\) cm has perimeter \(30\) cm. Find its angle and area.
(a) \(10 = 8\theta\), so \(\theta = 1.25\) radians.

(b) \(45 = \tfrac12 r^2 (0.9) = 0.45r^2\), so \(r^2 = 100\) and \(r = 10\) cm.

(c) The arc is \(30 - 2 \times 8 = 14\) cm, so \(\theta = \dfrac{14}{8} = 1.75\) radians. The area is \(\tfrac12 \times 64 \times 1.75 = 56\) cm².
:::

:::warn Degrees in a radian formula
The formulas \(s = r\theta\) and \(A = \tfrac12 r^2\theta\) work only when \(\theta\) is in radians. If the angle is given in degrees, convert it first. Do not put \(60\) into \(r\theta\) and expect an answer in centimetres. Also, "perimeter of a sector" includes the two straight radii; "arc length" does not.
:::

:::proof Why s = rθ and A = ½r²θ
**Arc length.** One radian is the angle at the centre when the arc is exactly as long as the radius. An angle of \(\theta\) radians is \(\theta\) times as big, so its arc is \(\theta\) times as long: \(s = r\theta\). Equivalently, \(\theta = \dfrac{s}{r}\), which is the definition.

**Sector area.** A full turn is \(2\pi\) radians, so a sector of angle \(\theta\) is the fraction \(\dfrac{\theta}{2\pi}\) of the whole circle. Its area is that fraction of \(\pi r^2\):
\[A = \frac{\theta}{2\pi} \times \pi r^2 = \tfrac12 r^2\theta\]
Since \(s = r\theta\), this is also \(A = \tfrac12 rs\). It matches the area of a triangle with base \(s\) and height \(r\): a thin sector is almost a triangle, and the formula is exact.

:::html
<div class="widget" data-w="proof" data-proof="sector"></div>
:::
:::

:::proof Why the chord length is 2r sin(θ/2)
Draw the perpendicular from the centre \(O\) to the chord \(AB\). It cuts the isosceles triangle \(OAB\) into two congruent right-angled triangles, and it cuts angle \(AOB\) into two angles of \(\dfrac{\theta}{2}\).
In one of them the hypotenuse is \(r\) and the side opposite the angle \(\dfrac{\theta}{2}\) is half the chord. So \(\dfrac{AB}{2} = r\sin\dfrac{\theta}{2}\), which gives \(AB = 2r\sin\dfrac{\theta}{2}\).
:::

## Triangles and segments

A **chord** joins two points on a circle. It cuts the circle into two **segments**. The minor segment is the region between the chord and the shorter arc.

If the chord \(AB\) subtends angle \(\theta\) at the centre \(O\), then triangle \(OAB\) is isosceles with two sides \(r\) and included angle \(\theta\). Its area is \(\tfrac12 r^2\sin\theta\), and the cosine rule gives the chord, or you can split the triangle in two right-angled triangles to get \(AB = 2r\sin\dfrac{\theta}{2}\).

:::key Segment
Area of segment \(=\) area of sector \(-\) area of triangle \(OAB\):
\[A_{\text{segment}} = \tfrac12 r^2\theta - \tfrac12 r^2\sin\theta = \tfrac12 r^2(\theta - \sin\theta)\]
Chord length \(AB = 2r\sin\dfrac{\theta}{2}\). The segment formula is **not** on MF19, but you can rebuild it in seconds from \(\tfrac12 r^2\theta\) and \(\tfrac12 ab\sin C\). Use radian mode for \(\sin\theta\).
:::

:::eg A chord subtends an angle of \(0.8\) radians at the centre of a circle of radius \(10\) cm. Find the area of the minor segment. A second chord subtends \(1.4\) radians in a circle of radius \(8\) cm: find its length.
Segment area \(= \tfrac12 (10)^2 (0.8 - \sin 0.8) = 50(0.8 - 0.7174) = 4.13\) cm² (3 s.f.).

Chord \(= 2 \times 8 \times \sin 0.7 = 16 \times 0.6442 = 10.3\) cm (3 s.f.). Check with the cosine rule: \(\sqrt{64 + 64 - 128\cos 1.4} = \sqrt{128 - 21.8} = 10.3\). ✓
:::

:::eg (Exam style) A circle has centre \(O\) and radius \(6\) cm. A chord \(AB\) subtends an angle of \(2.1\) radians at \(O\). The minor segment is shaded. Find (a) the perimeter and (b) the area of the shaded segment.
**(a)** Arc \(AB = 6 \times 2.1 = 12.6\) cm. [M1] Chord \(AB = 2 \times 6 \times \sin\dfrac{2.1}{2} = 10.41\) cm. [M1 A1] Perimeter \(= 12.6 + 10.41 = 23.0\) cm (3 s.f.). [A1]

**(b)** Area of segment \(= \tfrac12 (6)^2 (2.1 - \sin 2.1)\) [M1]
\[= 18(2.1 - 0.8632) = 22.3 \text{ cm}^2\] [A1]
Check: sector \(= 18 \times 2.1 = 37.8\), triangle \(= 18 \sin 2.1 = 15.54\), and \(37.8 - 15.54 = 22.26\). ✓
:::

## Problems with sectors and triangles together

In harder questions the circle is centred at a vertex of a triangle, so the arc is part of the boundary of the region. Draw the diagram, mark every known length and angle, then split the region into shapes you can find: sectors, triangles, segments. Subtract an inner piece from an outer piece for a "shaded" region.

:::eg (Exam style) In triangle \(ABC\) the angle at \(B\) is a right angle, \(AB = 6\) cm and \(BC = 8\) cm. A circular arc with centre \(A\) and radius \(6\) cm joins \(B\) to the point \(D\) on \(AC\). Find (a) angle \(BAC\) in radians, (b) the area of the region \(BCD\) bounded by \(BC\), \(CD\) and the arc \(BD\), and (c) its perimeter.
**(a)** \(\tan\angle BAC = \dfrac86 = \dfrac43\), so angle \(BAC = \tan^{-1}\tfrac43 = 0.9273\) radians. [M1 A1]

**(b)** The area of the region is the triangle minus the sector \(ABD\). Triangle \(ABC\): \(\tfrac12 \times 6 \times 8 = 24\). [B1] Sector \(ABD\): \(\tfrac12 \times 6^2 \times 0.9273 = 16.69\). [M1]
\[\text{Region} = 24 - 16.69 = 7.31 \text{ cm}^2\] [A1]

**(c)** \(AC = \sqrt{6^2 + 8^2} = 10\), so \(CD = 10 - 6 = 4\) cm. [B1] Arc \(BD = 6 \times 0.9273 = 5.564\). The perimeter is \(BC + CD + \text{arc} = 8 + 4 + 5.564 = 17.6\) cm (3 s.f.). [M1 A1]
:::

:::eg (Exam style) A sector of a circle has perimeter \(24\) cm and area \(32\) cm². Find the two possible values of the radius \(r\) and the corresponding angles \(\theta\).
Perimeter: \(2r + r\theta = 24\), so \(r\theta = 24 - 2r\). [M1]
Area: \(\tfrac12 r^2\theta = 32\). Substitute \(r\theta\):
\[\tfrac12 r(24 - 2r) = 32 \implies 12r - r^2 = 32 \implies r^2 - 12r + 32 = 0\] [M1 A1]
\[(r - 4)(r - 8) = 0 \implies r = 4 \text{ or } r = 8\] [A1]
When \(r = 4\): \(\theta = \dfrac{24 - 8}{4} = 4\) radians. When \(r = 8\): \(\theta = \dfrac{24 - 16}{8} = 1\) radian. [A1]
Both are valid since \(0 < \theta < 2\pi\). Check \(r = 4\): area \(= \tfrac12 \times 16 \times 4 = 32\). ✓
:::

:::eg (Exam style) In triangle \(OAB\), \(OA = OB = 7\) cm and \(AB = 10\) cm. A circle with centre \(O\) and radius \(7\) cm passes through \(A\) and \(B\). Find (a) angle \(AOB\) in radians, (b) the length of the minor arc \(AB\), (c) the area of the sector \(OAB\), (d) the area of the segment between the chord \(AB\) and the arc.
**(a)** Three sides are known, so use the cosine rule:
\[\cos AOB = \frac{7^2 + 7^2 - 10^2}{2 \times 7 \times 7} = \frac{-2}{98}\] [M1 A1]
\[\angle AOB = 1.591 \text{ radians (3 d.p.)}\] [A1]
The cosine is slightly negative, so the angle is just over a right angle (\(\tfrac{\pi}{2} = 1.571\)). Check the calculator is in radian mode.

**(b)** Arc \(= 7 \times 1.591 = 11.1\) cm. [M1 A1]

**(c)** Sector \(= \tfrac12 \times 7^2 \times 1.591 = 39.0\) cm². [M1 A1]

**(d)** Triangle \(OAB = \tfrac12 \times 7 \times 7 \times \sin 1.591 = 24.5\) cm² (\(\sin 1.591 = 0.9998\)). [M1] Segment \(= 39.0 - 24.5 = 14.5\) cm². [A1]
Check: with full calculator values, the segment is \(\tfrac12 \times 49 \times (1.5912 - 0.9998) = 14.49\). ✓
:::

:::exam Radians in exam answers
- Give angles in radians to 3 s.f. or as a multiple of \(\pi\). A question that uses radians never wants degrees.
- Keep the angle's full calculator value in later steps (for example 0.9273 above), and round only at the end.
- Keep a **clear sketch**: label \(r\), \(\theta\), arcs, chords and right angles. Marks go for the right sub-areas even when the final arithmetic slips.
:::

:::board Other boards
Edexcel IAL (in P1) and the UK A Levels test the same formulas for arc length, sector area and segments, and also use radians throughout calculus. Small-angle approximations, such as \(\sin\theta \approx \theta\), appear in the UK specifications but are not in Cambridge 9709.
:::

:::eg Spot the error: a chord subtends an angle of \(1.1\) radians at the centre of a circle of radius \(6\) cm. Find the area of the minor segment.
A student wrote this answer.

Line 1: Area \(= \tfrac12 r^2(\theta - \sin\theta)\)
Line 2: \(= \tfrac12 \times 36 \times (1.1 - \sin 1.1)\)
Line 3: \(= 18 \times (1.1 - 0.0192) = 19.5\,\mathrm{cm^2}\)

Lines 1 and 2 are correct [M1]. **Line 3 loses the accuracy mark [A0].** The calculator was in **degree** mode, so \(\sin 1.1\) was calculated as \(\sin 1.1^\circ = 0.0192\). The angle is in radians, so the calculator must be in radian mode: \(\sin 1.1 = 0.8912\).

Correct line 3: \(18 \times (1.1 - 0.8912) = 18 \times 0.2088 = 3.76\,\mathrm{cm^2}\). [A1]

**Sense check:** the sector has area \(\tfrac12 \times 36 \times 1.1 = 19.8\,\mathrm{cm^2}\), and the segment is the sector minus triangle \(OAB\). The student's answer of 19.5 would leave a triangle of area only 0.3, but a triangle with two sides of 6 cm enclosing 1.1 radians has area \(\tfrac12 \times 36 \times 0.8912 = 16.0\,\mathrm{cm^2}\). Check the mode of your calculator before every radian question.
:::

:::try Start easy, finish at exam standard
Q: Convert (a) \(150^\circ\) to radians in terms of \(\pi\), (b) \(0.8\) radians to degrees, (c) \(\dfrac{5\pi}{12}\) radians to degrees.
A: (a) \(150 \times \dfrac{\pi}{180} = \dfrac{5\pi}{6}\). (b) \(0.8 \times \dfrac{180}{\pi} = 45.8^\circ\). (c) \(\dfrac{5 \times 180}{12} = 75^\circ\).
Q: A sector has radius \(12\) cm and angle \(\dfrac{\pi}{3}\). Find the exact arc length and area.
A: Arc \(= 12 \times \dfrac{\pi}{3} = 4\pi\) cm. Area \(= \tfrac12 \times 144 \times \dfrac{\pi}{3} = 24\pi\) cm².
Q: An arc of length \(15\) cm subtends an angle of \(1.2\) radians at the centre. Find the radius and the sector area.
A: \(r = \dfrac{15}{1.2} = 12.5\) cm. Area \(= \tfrac12 \times 12.5^2 \times 1.2 = 93.75\) cm².
Q: A sector has radius \(5\) cm and perimeter \(16\) cm. Find its angle and area.
A: Arc \(= 16 - 10 = 6\), so \(\theta = 1.2\). Area \(= \tfrac12 \times 25 \times 1.2 = 15\) cm².
Q: Find the area of the minor segment cut off by a chord that subtends \(1.5\) radians in a circle of radius \(8\) cm.
A: \(\tfrac12 \times 64 \times (1.5 - \sin 1.5) = 32 \times (1.5 - 0.9975) = 16.1\) cm².
Q: A sector of radius \(r\) has angle \(\theta\) and perimeter \(P\). Show that its area is \(\tfrac12 r(P - 2r)\).
A: The arc is \(P - 2r = r\theta\). Area \(= \tfrac12 r^2\theta = \tfrac12 r \times (r\theta) = \tfrac12 r(P - 2r)\).
Q: The minute hand of a clock is \(9\) cm long. How far does the tip move in 20 minutes, and what area does the hand sweep?
A: Twenty minutes is a third of a turn, so \(\theta = \dfrac{2\pi}{3}\). Distance \(= 9 \times \dfrac{2\pi}{3} = 6\pi = 18.8\) cm. Area \(= \tfrac12 \times 81 \times \dfrac{2\pi}{3} = 27\pi = 84.8\) cm².
Q: Triangle \(PQR\) has \(PQ = PR = 10\) cm and angle \(QPR = 0.9\) radians. A circular arc with centre \(P\) and radius \(10\) cm joins \(Q\) to \(R\). Find the area of the region between the arc and the chord \(QR\).
A: This is a segment: \(\tfrac12 \times 100 \times (0.9 - \sin 0.9) = 50 \times (0.9 - 0.7833) = 5.83\) cm².
Q: (Exam style) The diagram shows a sector \(OAB\) of a circle of radius \(9\) cm. The angle \(AOB\) is \(\theta\) radians, and the arc \(AB\) has length \(12.6\) cm. (a) Find \(\theta\). (b) Find the area of the sector. (c) Find the area of the triangle \(OAB\) and hence of the shaded segment.
A: (a) \(\theta = \dfrac{12.6}{9} = 1.4\). [M1 A1] (b) \(\tfrac12 \times 81 \times 1.4 = 56.7\) cm². [M1 A1] (c) Triangle \(= \tfrac12 \times 81 \times \sin 1.4 = 40.5 \times 0.98545 = 39.9\) cm². [M1] Segment \(= 56.7 - 39.9 = 16.8\) cm². [A1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ (a) Write \(150^\circ\) in radians, in terms of \(\pi\). (b) Write 1.8 radians in degrees, correct to 1 decimal place.
A: (a) \(150 \times \dfrac{\pi}{180} = \dfrac{5\pi}{6}\). [B1] (b) \(1.8 \times \dfrac{180}{\pi}\) [M1] \(= 103.1^\circ\). [A1]
Q: [4 marks] ★ A sector of a circle has radius 9 cm and angle 0.8 radians. Find its arc length, its perimeter and its area.
A: Arc length \(= 9 \times 0.8 = 7.2\) cm. [B1] Perimeter \(= 2 \times 9 + 7.2 = 25.2\) cm. [B1] Area \(= \tfrac12 \times 81 \times 0.8\) [M1] \(= 32.4\,\mathrm{cm^2}\) (3 s.f.). [A1]
Q: [4 marks] ★★ A sector has radius 8 cm and area \(40\,\mathrm{cm^2}\). Find the angle at the centre and the perimeter of the sector.
A: \(\tfrac12 \times 64 \times \theta = 40\) [M1] so \(\theta = 1.25\) radians. [A1] The arc length is \(8 \times 1.25 = 10\) cm [B1] and the perimeter is \(16 + 10 = 26\) cm. [A1]
Q: [4 marks] ★★ A sector has area \(36\,\mathrm{cm^2}\) and arc length 12 cm. Find the radius and the angle at the centre.
A: \(A = \tfrac12 rs\), so \(36 = \tfrac12 \times r \times 12\). [M1] \(r = 6\) cm. [A1] \(\theta = \dfrac{s}{r} = \dfrac{12}{6}\) [M1] \(= 2\) radians. [A1]
Q: [6 marks] ★★ A chord \(AB\) subtends an angle of 1.2 radians at the centre \(O\) of a circle of radius 7 cm. Find (a) the area of the minor segment, (b) the perimeter of the minor segment.
A: (a) Area \(= \tfrac12 \times 49 \times (1.2 - \sin 1.2)\) [M1] \(= 24.5 \times 0.2680 = 6.57\,\mathrm{cm^2}\) (3 s.f.). [A1] (b) Arc \(= 7 \times 1.2 = 8.4\) cm. [B1] Chord \(AB = 2 \times 7 \times \sin 0.6\) [M1] \(= 7.905\) cm. [A1] Perimeter \(= 8.4 + 7.905 = 16.3\) cm (3 s.f.). [A1]
Q: [7 marks] (#math.p1.quadratics) ★★★ A sector of a circle with radius \(r\) cm has a perimeter of 20 cm. (a) Show that the area of the sector is \(A = 10r - r^2\). (b) By completing the square, find the greatest possible area of the sector, and the angle at the centre when the area is greatest.
H: Write the perimeter as \(2r + s = 20\) and find the arc length \(s\) in terms of \(r\).
H: The area of a sector is \(\tfrac12 rs\). Substitute your \(s\).
H: For (b), write \(10r - r^2\) as \(25 - (r - 5)^2\).
A: (a) \(2r + s = 20\), so \(s = 20 - 2r\). [B1] \(A = \tfrac12 rs = \tfrac12 r(20 - 2r)\) [M1] \(= 10r - r^2\). [A1] (b) \(A = 25 - (r - 5)^2\). [M1 A1] The greatest area is \(25\,\mathrm{cm^2}\), when \(r = 5\). [A1] Then \(s = 10\) and \(\theta = \dfrac{s}{r} = 2\) radians. [B1]
Q: [9 marks] (#math.f.geometry) ★★★ A circle has centre \(O\) and radius 5 cm. The tangents from a point \(T\) touch the circle at \(A\) and \(B\), and \(OT = 13\) cm. (a) Find the length \(TA\). (b) Find angle \(AOB\) in radians. (c) Find the area of the region bounded by \(TA\), \(TB\) and the minor arc \(AB\).
H: A tangent is perpendicular to the radius, so triangle \(OAT\) is right-angled at \(A\).
H: In triangle \(OAT\), \(\cos\) of angle \(AOT\) is \(\dfrac{OA}{OT}\). Angle \(AOB\) is twice angle \(AOT\).
H: The region is the kite \(OATB\) minus the sector \(OAB\).
A: (a) \(TA^2 = 13^2 - 5^2 = 144\), so \(TA = 12\) cm. [M1 A1] (b) \(\cos(\angle AOT) = \tfrac{5}{13}\), so \(\angle AOT = 1.176\) radians. [M1 A1] \(\angle AOB = 2 \times 1.176 = 2.35\) radians (3 s.f.). [A1] (c) The kite is two triangles: area \(= 2 \times \tfrac12 \times 5 \times 12 = 60\). [B1] The sector has area \(\tfrac12 \times 25 \times 2.352 = 29.4\). [M1 A1] The region has area \(60 - 29.4 = 30.6\,\mathrm{cm^2}\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A sector of paper has radius 12 cm and angle \(\dfrac{4\pi}{3}\) radians. The two straight edges are joined to make a hollow cone. Find (a) the radius of the base of the cone, (b) the vertical height of the cone, (c) the curved surface area of the cone, and check it against the area of the sector.
H: When the edges are joined, the arc of the sector becomes the circumference of the base of the cone.
H: The radius of the sector, 12 cm, becomes the slant height of the cone.
A: (a) The arc length is \(12 \times \dfrac{4\pi}{3} = 16\pi\). [B1] This is the base circumference, so \(2\pi r = 16\pi\) and \(r = 8\) cm. [M1 A1] (b) The slant height is 12 cm: \(h = \sqrt{12^2 - 8^2} = \sqrt{80} = 8.94\) cm. [M1 A1] (c) The curved surface area is the area of the sector: \(\tfrac12 \times 144 \times \dfrac{4\pi}{3} = 96\pi = 302\,\mathrm{cm^2}\). [A1] Check with \(\pi r l = \pi \times 8 \times 12 = 96\pi\). [B1]
Q: [5 marks] ★★★ A chord subtends an angle of \(\dfrac{\pi}{2}\) at the centre of a circle of radius \(r\). (a) Show that the area of the minor segment is \(\dfrac{r^2(\pi - 2)}{4}\). (b) Find the exact length of the chord, and the area of the segment as a percentage of the area of the circle, to 3 significant figures.
H: Use the segment formula \(\tfrac12 r^2(\theta - \sin\theta)\) with \(\theta = \dfrac{\pi}{2}\); you know \(\sin\dfrac{\pi}{2}\).
H: For the chord, use \(2r\sin\dfrac{\theta}{2}\) or Pythagoras in the right-angled isosceles triangle.
A: (a) Area \(= \tfrac12 r^2\left(\dfrac{\pi}{2} - \sin\dfrac{\pi}{2}\right) = \tfrac12 r^2\left(\dfrac{\pi}{2} - 1\right)\) [M1] \(= \dfrac{r^2(\pi - 2)}{4}\). [A1] (b) The chord is \(2r\sin\dfrac{\pi}{4} = r\sqrt{2}\). [B1] The segment as a fraction of the circle is \(\dfrac{r^2(\pi - 2)/4}{\pi r^2} = \dfrac{\pi - 2}{4\pi}\) [M1] \(= 0.0908\), that is 9.08%. [A1]
:::

:::quiz
? What is \(\dfrac{4\pi}{3}\) radians in degrees?
- \(60^\circ\)
- \(120^\circ\)
+ \(240^\circ\)
- \(270^\circ\)
> \(\dfrac{4\pi}{3} \times \dfrac{180}{\pi} = 240^\circ\). Writing \(\pi = 180^\circ\) makes it \(\dfrac{4 \times 180}{3}\). The value \(120^\circ\) is \(\dfrac{2\pi}{3}\), where the 4 was missed.
? A sector has radius \(5\) cm and angle \(0.8\) radians. What is the arc length?
- \(2\pi\) cm
- \(6.25\) cm
+ \(4\) cm
- \(10\) cm\(^2\)
> The arc length is \(r\theta = 5 \times 0.8 = 4\) cm. The area formula would give \(\tfrac12 \times 25 \times 0.8 = 10\) cm², the wrong quantity and the wrong unit. Dividing \(r\) by \(\theta\) gives \(6.25\).
? Which is the correct formula for the area of the minor segment, with \(\theta\) in radians?
- \(\tfrac12 r^2\theta\)
- \(\tfrac12 r^2(\theta + \sin\theta)\)
+ \(\tfrac12 r^2(\theta - \sin\theta)\)
- \(\tfrac12 r^2\sin\theta\)
> A segment is the sector minus the triangle: \(\tfrac12 r^2\theta - \tfrac12 r^2\sin\theta\). The first option is the whole sector, the last is only the triangle, and the plus sign adds the triangle instead of removing it.
? A calculator in degree mode gives \(\sin(1.2) = 0.0209\). What went wrong?
- The angle is too small.
+ The calculator should be in radian mode.
- \(\sin\) of a radian is always small.
- The answer should be multiplied by \(\pi\).
> The angle 1.2 has no degree sign, so it is in radians. In degree mode the calculator treats it as \(1.2^\circ\). In radian mode \(\sin 1.2 = 0.932\).
? A sector has radius 10 cm and perimeter 36 cm. What is its arc length?
- \(36\) cm
- \(26\) cm
+ \(16\) cm
- \(6\) cm
> The perimeter is two radii plus the arc: \(36 = 20 + s\), so \(s = 16\). Stopping at 26 forgets that there are two radii to subtract.
? A sector has radius 4 cm and angle \(\dfrac{\pi}{2}\). What is its area in \(\mathrm{cm^2}\)?
- \(2\pi\)
+ \(4\pi\)
- \(8\pi\)
- \(\dfrac{\pi}{2}\)
> \(A = \tfrac12 r^2\theta = \tfrac12 \times 16 \times \dfrac{\pi}{2} = 4\pi\). Forgetting the \(\tfrac12\) gives \(8\pi\), and \(2\pi\) is the arc length \(r\theta\).
:::

:::checklist What you can now do
- [ ] I can convert between degrees and radians, using exact multiples of \(\pi\) where I can.
- [ ] I can use \(s = r\theta\) and \(A = \tfrac12 r^2\theta\) to find arc lengths, angles, radii and areas of sectors.
- [ ] I can find the perimeter and area of a sector, a triangle and a segment.
- [ ] I can solve problems that combine sectors with triangles, using Pythagoras, sine and cosine rules.
- [ ] I can tell when my calculator must be in radian mode.
:::

:::recap
- \(\pi\) radians \(= 180^\circ\). Multiply by \(\dfrac{\pi}{180}\) to go to radians, and by \(\dfrac{180}{\pi}\) to go to degrees.
- Arc length \(s = r\theta\), sector area \(A = \tfrac12 r^2\theta\), sector perimeter \(2r + r\theta\) (radians only).
- Segment area \(= \tfrac12 r^2(\theta - \sin\theta)\); chord \(= 2r\sin\dfrac{\theta}{2}\). Neither is on MF19: rebuild them from sector and triangle.
- In composite problems: draw it, label it, split into sectors and triangles, then add or subtract areas.
- Calculator in radian mode when the angle has no degree sign.
:::

:::links
- watch: [Arcs, sectors and segments](https://www.examsolutions.net/tutorials/arcs-sectors-segments/) · ExamSolutions · s = rθ and A = ½r²θ in use
- watch: [Exam questions: arcs, sectors and segments](https://www.examsolutions.net/tutorials/exam-questions-arcs-sectors-and-segments/) · ExamSolutions · exam-style questions solved on video
- practise: [CAIE Pure 1 radians exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/trigonometry/circular-measure-radians/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [Trigonometry](https://www.khanacademy.org/math/trigonometry) · Khan Academy · the radians unit, with practice
- papers: [9709 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-1/) · Physics & Maths Tutor · circular measure appears in Paper 1 [unofficial]

Links checked 3 October 2026.
:::
Next: [Trigonometry](#math.p1.trig).
