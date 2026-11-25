@chapter math.fm.com
@title Centres of mass
@level fm
@paper CAIE 9231 Paper 3 · Edexcel IAL Mechanics 2 · UK A Level Further Mechanics
@time 5–6 hours
@summary The weight of a body acts as one force at its centre of mass. You will take moments of forces about a point, find the centre of mass of a set of particles, use the standard results on MF19 for triangles, hemispheres, cones, arcs and sectors, and build the centre of mass of composite laminas, solids and wire frameworks from their parts, including parts that are removed. You will also find the angle at which a body hangs when it is suspended from a point.

:::why
Where a body balances decides whether a ladder slips, a crane topples, a bottle stands up or lies down, and how a mobile hangs. Engineers reduce a complicated shape to one point at which gravity can be taken to act. Once you can find that point for a combination of simple shapes, the next chapter on equilibrium becomes a matter of applying the same few ideas.
:::

**Before you start**, you need resolving forces from [Forces and equilibrium](#math.m.forces), the area of a sector from [Circular measure](#math.p1.circular) and \(\tan\theta\) from [Trigonometry](#math.p1.trig). Take **\(g = 10\,\mathrm{m\,s^{-2}}\)** where weights are needed.

:::try Warm-up
Q: A force of \(20\) N acts at \(60^\circ\) to the horizontal. Find its vertical component. (from [Forces and equilibrium](#math.m.forces))
A: \(20\sin 60^\circ = 17.3\) N.
Q: Find the area of a sector of a circle of radius \(4\) cm and angle \(1.5\) radians. (from [Circular measure](#math.p1.circular))
A: \(A = \tfrac12r^2\theta = \tfrac12 \times 16 \times 1.5 = 12\ \text{cm}^2\).
Q: Find the angle \(\theta\) with \(\tan\theta = 0.75\). (from [Trigonometry](#math.p1.trig))
A: \(\theta = \tan^{-1}0.75 = 36.9^\circ\).
:::

## Moments: the turning effect of a force

A force can push a body along, and it can also turn it. A door swings because you push at the handle, far from the hinge; push near the hinge and it hardly moves. The turning effect depends on the size of the force and on how far from the pivot its line of action lies.

:::def Moment of a force
The moment of a force about a point \(O\) is the force multiplied by the **perpendicular distance** from \(O\) to the line of action of the force: \(M = F \times d\). It is measured in N m and has a sense, clockwise or anticlockwise.
:::

The word **perpendicular** is the whole difficulty. If the force acts along the rod, or the line of the force passes through \(O\), then \(d = 0\) and the moment is zero. When the force is at angle \(\varphi\) to the rod and acts at distance \(x\) along it from \(O\), you have two equivalent ways to find the moment:

:::key Moment of a force at an angle
For a force \(F\) at angle \(\varphi\) to the rod, acting at distance \(x\) from \(O\) along the rod:
\[M = F\sin\varphi \times x\]
Either resolve \(F\) into the part perpendicular to the rod (\(F\sin\varphi\)) and multiply by \(x\), or find the perpendicular distance from \(O\) to the line of action (\(x\sin\varphi\)) and multiply by \(F\). The result is the same. Choose a sense (say anticlockwise positive) and keep to it.
:::

:::eg A light rod \(AB\) of length \(4\) m lies along a horizontal line, with \(A\) at the origin. Forces act on it: \(10\) N vertically downwards at \(1\) m from \(A\), \(6\) N vertically upwards at \(3\) m from \(A\), and \(12\) N at \(B\) directed at \(30^\circ\) above the rod (pointing away from \(A\)). Find the total moment of the forces about \(A\).
Take anticlockwise as positive.

The \(10\) N force turns the rod clockwise about \(A\): \(-10 \times 1 = -10\) N m.

The \(6\) N force turns it anticlockwise: \(+6 \times 3 = +18\) N m.

The \(12\) N force is at \(30^\circ\) to the rod, so its component perpendicular to the rod is \(12\sin 30^\circ = 6\) N, upwards, at \(4\) m: \(+6 \times 4 = +24\) N m. The component along the rod, \(12\cos 30^\circ\), passes through \(A\) and has no moment.
\[\text{total} = -10 + 18 + 24 = 32\ \text{N m anticlockwise}\]
:::

## The centre of mass

Every particle in a body is pulled down by gravity. All those little weights are parallel forces, and for any body there is one point where the single force equal to the total weight would have exactly the same effect, however the body is turned.

:::def Centre of mass
The point \(G\) through which the weight of a body acts, whatever its orientation. A body suspended from, or balanced on, a point is in equilibrium only if \(G\) is vertically below, or vertically above, that point.
:::

For a **uniform** body (the same density everywhere) \(G\) is the centre of its shape, found by symmetry when there is any.

:::key Centres of mass by symmetry (uniform bodies)
- A uniform **rod**: its midpoint. A **rectangle** or **parallelogram** lamina: where the diagonals meet. A **circular disc** or **ring**, a **sphere**, a **cylinder** or a **cuboid**: the centre.
- If a body has a **line (or plane) of symmetry**, \(G\) lies on it. With two such lines, \(G\) is where they cross.
- A body is made of **parts**, and the centre of mass of the whole follows from the parts (next sections).
:::

## Particles: the centre of mass formula

For a few particles you can find \(G\) by taking moments. Let particles of mass \(m_1, m_2, \dots, m_n\) lie at \(x_1, x_2, \dots, x_n\) on a line. The weight of the whole system, \((\sum m)g\), acts at \(G\), at position \(\bar x\). Moments about the origin must agree, because the single force is equivalent to the many:
\[(\textstyle\sum m)g\,\bar x = m_1gx_1 + m_2gx_2 + \dots = g\textstyle\sum mx\]
The \(g\) cancels. Do the same with the \(y\) coordinates.

:::key Centre of mass of particles
For masses \(m_i\) at \((x_i, y_i)\):
\[\bar x = \frac{\sum m_ix_i}{\sum m_i} \qquad \bar y = \frac{\sum m_iy_i}{\sum m_i}\]
It is the mass-weighted mean position. The three steps: choose an origin and axes, tabulate each mass and position, then divide each sum of "mass times distance" by the total mass.
:::

:::eg Masses of \(2\) kg, \(3\) kg and \(5\) kg are at \((1, 0)\), \((4, 2)\) and \((-1, 3)\) (distances in metres). Find the centre of mass.
\[\sum m = 10\]
\[\bar x = \frac{2(1) + 3(4) + 5(-1)}{10} = \frac{9}{10} = 0.9 \qquad \bar y = \frac{2(0) + 3(2) + 5(3)}{10} = \frac{21}{10} = 2.1\]
\(G = (0.9, 2.1)\). The point lies inside the triangle of the three particles, as it always does.
:::

:::eg A uniform rod \(AB\) of mass \(4\) kg and length \(6\) m carries a particle of mass \(2\) kg at \(A\) and a particle of mass \(5\) kg at \(B\). Find the distance of the centre of mass of the system from \(A\).
Measure from \(A\) along the rod. The rod's own weight acts at its midpoint, \(3\) m from \(A\).

| Part | Mass (kg) | Distance from \(A\) (m) | Mass \(\times\) distance |
|---|---|---|---|
| particle at \(A\) | 2 | 0 | 0 |
| rod | 4 | 3 | 12 |
| particle at \(B\) | 5 | 6 | 30 |
| total | 11 | | 42 |
\[\bar x = \frac{42}{11} = 3.82\ \text{m from } A\ (3\ \text{s.f.})\]
The heavy end \(B\) pulls the centre of mass beyond the midpoint of the rod, 3 m from \(A\).
:::

## Results you are given: MF19

The centres of mass of some uniform shapes need integration to prove. The syllabus does not ask you to prove them: they are **printed in the formula list MF19**, and you quote them.

:::key Centres of mass given on MF19
| Uniform body | Position of centre of mass |
|---|---|
| Triangular lamina | \(\tfrac23\) of the way along a median from a vertex (that is, \(\tfrac13\) of the height above a base) |
| Solid hemisphere, radius \(r\) | \(\tfrac{3r}{8}\) from the centre of the plane face, on the axis |
| Hemispherical shell, radius \(r\) | \(\tfrac{r}{2}\) from the centre of the plane face, on the axis |
| Solid cone or pyramid, height \(h\) | \(\tfrac34h\) from the vertex (\(\tfrac14h\) from the base), on the axis |
| Circular arc, radius \(r\), angle \(2\alpha\) | \(\dfrac{r\sin\alpha}{\alpha}\) from the centre, on the axis of symmetry |
| Sector of a circle, radius \(r\), angle \(2\alpha\) | \(\dfrac{2r\sin\alpha}{3\alpha}\) from the centre, on the axis of symmetry |
\(\alpha\) is in radians and is **half** the angle at the centre. A **shell** is the curved surface only; a **solid** is the whole body.
:::

Three consequences you will use constantly.

- **The triangle.** The centre of mass of a triangular lamina is the **centroid**, the point where the medians meet. Its coordinates are the **mean of the vertices' coordinates**: for vertices \((x_1, y_1)\), \((x_2, y_2)\), \((x_3, y_3)\) it is \(\left(\dfrac{x_1 + x_2 + x_3}{3}, \dfrac{y_1 + y_2 + y_3}{3}\right)\).
- **The semicircle is a sector.** A semicircular lamina is a sector with \(\alpha = \tfrac\pi2\), so its centre of mass is \(\dfrac{2r\sin\frac\pi2}{3 \times \frac\pi2} = \dfrac{4r}{3\pi}\) from the centre of the straight edge. Likewise a **semicircular arc** has \(\alpha = \tfrac\pi2\): \(\dfrac{r}{\pi/2} = \dfrac{2r}{\pi}\). The semicircle results are not in the table: you must get them from the sector and arc rows.
- **Cone, hemisphere, cylinder.** The solid cone is \(\tfrac14h\) from its base. The solid hemisphere is \(\tfrac38r\) from its plane face. The cylinder is at the middle of its axis.

:::eg (a) Find the centre of mass of a triangular lamina with vertices \((0, 0)\), \((9, 0)\) and \((3, 6)\). (b) A uniform semicircular lamina has radius \(6\) cm. Find the distance of its centre of mass from the centre of the straight edge.
**(a)** Mean of the vertices:
\[\bar x = \frac{0 + 9 + 3}{3} = 4, \qquad \bar y = \frac{0 + 0 + 6}{3} = 2\]
The centre of mass is \((4, 2)\). Check: it is \(\tfrac13\) of the height (6) above the base.

**(b)** A semicircle is a sector with \(2\alpha = \pi\), so \(\alpha = \tfrac\pi2\):
\[\frac{2r\sin\alpha}{3\alpha} = \frac{2 \times 6 \times 1}{3 \times \frac\pi2} = \frac{8}{\pi} = 2.55\ \text{cm}\]
:::

:::proof Why the cone is a quarter of the way up (not examined)
Slice a cone of height \(h\) into thin discs parallel to the base. A disc at distance \(y\) from the vertex has radius proportional to \(y\), so its volume is proportional to \(y^2\,dy\). The centre of mass distance from the vertex is
\[\frac{\int_0^h y \times y^2\,dy}{\int_0^h y^2\,dy} = \frac{h^4/4}{h^3/3} = \frac{3h}{4}\]
So \(G\) is \(\tfrac34h\) from the vertex and \(\tfrac14h\) from the base. The solid cone is thickest at the base, so \(G\) is nearer the base than the vertex, and the answer reflects that.
:::

## Composite laminas

A **lamina** is a flat body so thin that it is treated as a region of a plane. A uniform lamina has mass proportional to **area**, so area stands in for mass in the formula. Break the shape into rectangles, triangles, circles and sectors whose centres you know.

:::steps
1. Draw the lamina, choose an origin and the \(x\) and \(y\) axes, and label every length.
2. Split it into standard shapes. If part has been removed, treat the full shape and the hole separately.
3. Make a table: for each part, the area (as the mass), the \(x\) coordinate and the \(y\) coordinate of its centre of mass.
4. Use \(\bar x = \dfrac{\sum A\,x}{\sum A}\) and the same for \(\bar y\), counting a **removed part as a negative area**.
5. Check: if the lamina has an axis of symmetry the answer lies on it, and \(G\) must lie where you would expect it to.
:::

:::eg A uniform lamina is shaped like an L with equal arms: it has vertices \((0,0)\), \((6,0)\), \((6,2)\), \((2,2)\), \((2,6)\), \((0,6)\). Find its centre of mass.
Split it into a horizontal rectangle \(6 \times 2\) and a vertical rectangle \(2 \times 4\) (on top of the first).

| Part | Area | \(x\) | \(y\) | \(Ax\) | \(Ay\) |
|---|---|---|---|---|---|
| lower rectangle | 12 | 3 | 1 | 36 | 12 |
| upper rectangle | 8 | 1 | 4 | 8 | 32 |
| total | 20 | | | 44 | 44 |
\[\bar x = \frac{44}{20} = 2.2, \qquad \bar y = \frac{44}{20} = 2.2\]
**Check**: the shape is symmetric about the line \(y = x\), so \(\bar x\) must equal \(\bar y\). ✓. The point \((2.2, 2.2)\) is in the corner of the L, where the two arms overlap, which is where the mass is concentrated.
:::

For a shape that is not symmetric both coordinates need working, and the figure below helps you keep the parts straight.

:::html
<figure class="fig small"><svg viewBox="10 15 270 225" role="img" aria-label="An L-shaped lamina ABCDEF drawn on x and y axes with A at the origin. AB is 8 along the x axis, BC is 3, CD is 5, DE is 4 up, EF is 3 and FA is 7 up the y axis. A dashed line splits it into a lower rectangle 8 by 3 with centre of mass G1 at (4, 1.5) and an upper rectangle 3 by 4 with centre of mass G2 at (1.5, 5). The centre of mass G of the whole lamina is at (19/6, 8/3), on the line joining G1 and G2.">
  <polygon class="fm s-acc sw2" points="40,200 216,200 216,134 106,134 106,46 40,46"/>
  <path class="ln-m thin dash" d="M40 134H106"/>
  <path class="ln-m thin" d="M128 167L73 90"/>
  <circle class="fi" cx="128" cy="167" r="3"/>
  <circle class="fi" cx="73" cy="90" r="3"/>
  <circle class="fr" cx="109.7" cy="141.3" r="4"/>
  <path class="ax" d="M216 200H252" marker-end="url(#ah)"/>
  <path class="ax" d="M40 46V24" marker-end="url(#ah)"/>
  <text class="tl" x="256" y="204">x</text>
  <text class="tl" x="46" y="30">y</text>
  <text class="tl halo" x="134" y="182">G₁</text>
  <text class="tl halo" x="56" y="84" text-anchor="middle">G₂</text>
  <text class="tl halo" x="124" y="158">G</text>
  <text class="tl" x="128" y="216" text-anchor="middle">8</text>
  <text class="tl" x="224" y="170">3</text>
  <text class="tl" x="161" y="128" text-anchor="middle">5</text>
  <text class="tl" x="114" y="94">4</text>
  <text class="tl" x="73" y="38" text-anchor="middle">3</text>
  <text class="tl" x="32" y="127" text-anchor="end">7</text>
  <text class="tl" x="28" y="214" text-anchor="end">A</text>
  <text class="tl" x="222" y="216">B</text>
  <text class="tl" x="222" y="130">C</text>
  <text class="tl" x="112" y="126">D</text>
  <text class="tl" x="110" y="42">E</text>
  <text class="tl" x="28" y="42" text-anchor="end">F</text>
</svg><figcaption>The L-shaped lamina ABCDEF of the next example. The dashed line splits it into a lower rectangle with centre of mass G₁ and an upper rectangle with centre of mass G₂. The centre of mass G of the whole lamina lies on the line G₁G₂, nearer to the heavier lower part.</figcaption></figure>
:::

:::eg (Exam style) A uniform lamina \(ABCDEF\) is in the shape of an L, with \(A = (0, 0)\), \(B = (8, 0)\), \(C = (8, 3)\), \(D = (3, 3)\), \(E = (3, 7)\), \(F = (0, 7)\), lengths in centimetres (the figure above). Find the distance of the centre of mass from (a) \(AF\), (b) \(AB\).
Split along the dashed line into rectangle \(ABCX\) (\(8 \times 3\)) and rectangle \(XDEF\) (\(3 \times 4\)), where \(X = (0, 3)\). Areas are proportional to masses.
\[\text{areas: } 24 \text{ and } 12, \text{ total } 36\] [B1]
The centres of the rectangles are at \((4, 1.5)\) and \((1.5, 5)\). [B1]

**(a)** Taking moments about \(AF\) (the \(y\) axis):
\[36\bar x = 24 \times 4 + 12 \times 1.5\] [M1]
\[\bar x = \frac{96 + 18}{36} = \frac{19}{6} = 3.17\ \text{cm}\] [A1]
**(b)** Moments about \(AB\) (the \(x\) axis):
\[36\bar y = 24 \times 1.5 + 12 \times 5\] [M1]
\[\bar y = \frac{36 + 60}{36} = \frac83 = 2.67\ \text{cm}\] [A1]
**Check**: \(G = (3.17, 2.67)\) lies on the line from \((4, 1.5)\) to \((1.5, 5)\), nearer to the larger part. It is the mass-weighted mean of the two centres.
:::

:::eg (Exam style) A uniform square lamina has side \(10\) cm. A circular hole of radius \(2\) cm is cut out, with its centre \(3\) cm from each of two adjacent sides. Find the distance of the centre of mass of the remaining lamina from each of those two sides.
Take the corner as the origin and the two sides as axes, so the square has centre \((5, 5)\) and the hole has centre \((3, 3)\). A removed part is a **negative mass**.

| Part | Area | \(x\) | \(y\) |
|---|---|---|---|
| full square | 100 | 5 | 5 |
| hole | \(-4\pi\) | 3 | 3 |
| remaining | \(100 - 4\pi\) | \(\bar x\) | \(\bar y\) |
\[\left(100 - 4\pi\right)\bar x = 100 \times 5 - 4\pi \times 3\] [M1 A1]
\[\bar x = \frac{500 - 12\pi}{100 - 4\pi} = \frac{462.3}{87.43} = 5.29\ \text{cm}\] [A1]
By symmetry about the diagonal through the origin, \(\bar y = \bar x = 5.29\) cm. [B1]
**Check**: the hole is nearer the origin, so the centre of mass of what remains is pushed away from the origin, past \(5\). ✓
:::

:::eg A uniform lamina is formed by joining a semicircle of radius \(3\) cm along its diameter to one of the \(6\) cm sides of a rectangle that is \(6\) cm by \(5\) cm. Find the distance of its centre of mass from the joining line, and say which side it is on.
Measure along the axis of symmetry from the joining line, taking the semicircle side as positive.

The rectangle has area \(30\) and its centre is \(2.5\) cm on the other side: \(x = -2.5\). The semicircle has area \(\tfrac12\pi \times 3^2 = 4.5\pi = 14.14\) and, from the sector formula with \(\alpha = \tfrac\pi2\), its centre is \(\dfrac{4 \times 3}{3\pi} = \dfrac{4}{\pi} = 1.273\) cm from the diameter: \(x = +1.273\).
\[\bar x = \frac{30(-2.5) + 4.5\pi(1.273)}{30 + 4.5\pi} = \frac{-75 + 18}{44.14} = -1.29\ \text{cm}\]
The centre of mass is \(1.29\) cm from the joining line, on the rectangle's side. (The larger part pulls it that way.)
:::

## Composite solids

A **uniform solid** has mass proportional to **volume**. The method is the same as for laminas, with volumes in place of areas, and the centre of mass of every part lies on a common axis of symmetry, so one distance is needed. The volumes you need:

:::key Volumes for composite solids
\[\text{cylinder } \pi r^2h \qquad \text{cone } \tfrac13\pi r^2h \qquad \text{hemisphere } \tfrac23\pi r^3\]
Common factors (the \(\pi\), and often the radius) cancel, so work with the simplified values; just be consistent. The centre of mass of each part is on the axis, at the distances in the MF19 table: **measure all distances from the same point** and give each one a sign.
:::

:::eg (Exam style) A solid is made by joining a uniform solid cone, of base radius \(6\) cm and height \(9\) cm, to a uniform solid hemisphere of radius \(6\) cm, so that the plane faces coincide. (a) Find the distance of the centre of mass of the solid from the plane face where they join. (b) The cone has height \(h\) and the hemisphere radius \(r\), with the same base radius. Show that the centre of mass is in the common plane face when \(h = \sqrt3\,r\).
**(a)** Measure distance from the common plane face, positive into the cone.

Cone: volume \(\tfrac13\pi \times 36 \times 9 = 108\pi\), with its centre of mass \(\tfrac14 \times 9 = 2.25\) from the base, so at \(+2.25\). [B1]

Hemisphere: volume \(\tfrac23\pi \times 216 = 144\pi\), with its centre of mass \(\tfrac38 \times 6 = 2.25\) from the plane face, on the other side: \(-2.25\). [B1]

Moments about the common face:
\[(108\pi + 144\pi)\bar x = 108\pi(2.25) + 144\pi(-2.25)\] [M1]
\[\bar x = \frac{2.25(108 - 144)}{252} = -0.321\ \text{cm}\] [A1]
The centre of mass is \(0.321\) cm from the plane face, **inside the hemisphere**. [B1]

**(b)** The common face passes through \(G\) when the total moment about it is zero:
\[\tfrac13\pi r^2h \times \tfrac14h = \tfrac23\pi r^3 \times \tfrac38r\] [M1]
\[\frac{h^2}{12} = \frac{r^2}{4} \quad\Rightarrow\quad h^2 = 3r^2\] [A1]
So \(h = \sqrt3\,r\). [A1]
**Check**: for part (a), \(r = 6\) gives \(h = 10.4\); the cone there is shorter (\(h = 9\)), so it has less moment and \(G\) is on the hemisphere's side. ✓
:::

:::eg (Exam style) A uniform solid cone has base radius \(8\) cm and height \(16\) cm. A solid hemisphere of radius \(4\) cm, with its plane face in the base of the cone and the same centre, is removed. Find the distance of the centre of mass of the remaining solid from the plane base.
Measure along the axis from the base towards the vertex.

Cone: volume \(\tfrac13\pi \times 64 \times 16 = \tfrac{1024\pi}{3}\), centre of mass at \(\tfrac14 \times 16 = 4\). [B1]

Hemisphere: volume \(\tfrac23\pi \times 64 = \tfrac{128\pi}{3}\), centre of mass at \(\tfrac38 \times 4 = 1.5\). [B1]

The hemisphere is removed, so treat it as negative mass:

| Part | Volume (\(\div\pi\)) | Distance from base |
|---|---|---|
| cone | \(\tfrac{1024}{3}\) | 4 |
| hemisphere (removed) | \(-\tfrac{128}{3}\) | 1.5 |
| remaining solid | \(\tfrac{896}{3}\) | \(\bar x\) |
\[\tfrac{896}{3}\bar x = \tfrac{1024}{3} \times 4 - \tfrac{128}{3} \times 1.5\] [M1 A1]
\[\bar x = \frac{4096 - 192}{896} = \frac{3904}{896} = \frac{61}{14} = 4.36\ \text{cm}\] [A1]
**Check**: the whole cone has \(G\) at \(4\) cm. Removing the material near the base moves \(G\) towards the vertex, so a little more than \(4\) is right. ✓
:::

:::eg (Exam style) A solid is made of a uniform solid cylinder, of radius \(r\) and height \(h\), with a uniform solid hemisphere of radius \(r\) attached to one end, the plane face of the hemisphere coinciding with the end of the cylinder. (a) Show that the distance of the centre of mass from the free flat end of the cylinder is \(\dfrac{6h^2 + 8rh + 3r^2}{4(3h + 2r)}\). (b) The solid has \(r = 5\) cm and \(h = 8\) cm and is freely suspended from a point \(A\) on the rim of the free flat end. Find the angle between the axis of the solid and the vertical.
**(a)** Measure from the free flat end of the cylinder, along the axis.

Cylinder: volume \(\pi r^2h\), centre at \(\tfrac12h\). [B1]

Hemisphere: volume \(\tfrac23\pi r^3\), centre at \(h + \tfrac38r\). [B1]
\[\left(\pi r^2h + \tfrac23\pi r^3\right)\bar x = \pi r^2h \times \tfrac12h + \tfrac23\pi r^3\left(h + \tfrac38r\right)\] [M1]
Divide by \(\pi r^2\) and multiply by 12:
\[\left(12h + 8r\right)\bar x = 6h^2 + 8rh + 3r^2\] [M1]
\[\bar x = \frac{6h^2 + 8rh + 3r^2}{4(3h + 2r)}\] [A1]
**(b)** With \(r = 5\) and \(h = 8\): \(\bar x = \dfrac{6(64) + 8(40) + 3(25)}{4(24 + 10)} = \dfrac{779}{136} = 5.728\) cm. [B1]

When the solid hangs freely, \(G\) is vertically below \(A\). The axis passes through the centre of the flat end \(O\) at distance \(5\) from \(A\), and \(G\) is on the axis, \(5.728\) from the flat end. In the right-angled triangle \(AOG\), the angle \(\theta\) at \(G\) between the axis and the line \(GA\) (which is vertical) satisfies
\[\tan\theta = \frac{AO}{OG} = \frac{5}{5.728}\] [M1]
\[\theta = 41.1^\circ\] [A1]
The axis makes \(41.1^\circ\) with the vertical.
**Check**: \(\bar x\) lies between \(\tfrac12h = 4\) (cylinder alone) and \(h + \tfrac38r = 9.875\) (hemisphere alone), nearer to the cylinder because it is heavier. ✓
:::

:::warn Mass, not length
The commonest losses of marks: using the **lengths** of the parts (the heights of the cone and hemisphere) as if they were masses; measuring one part from the base and another from the vertex; and forgetting that the cone's centre of mass is \(\tfrac14h\) **from the base**, not from the vertex. Draw the solid, mark every centre of mass with its distance from one chosen point, and write down the volumes before you start.
:::

## Wire frameworks

A framework made of uniform wire has mass proportional to **length**. A straight piece has its centre of mass at its midpoint; a circular arc uses the MF19 arc formula.

:::eg A framework is made from a uniform wire bent into a right-angled triangle \(ABC\) with \(AB = 3\), \(BC = 4\) and \(AC = 5\) (all in cm), right-angled at \(B\). Find the distance of its centre of mass from \(AB\) and from \(BC\).
Take \(B\) as the origin, \(BC\) along the \(x\) axis and \(BA\) along the \(y\) axis. Mass is proportional to length.

| Side | Length | \(x\) | \(y\) |
|---|---|---|---|
| \(BA\) | 3 | 0 | 1.5 |
| \(BC\) | 4 | 2 | 0 |
| \(AC\) | 5 | 2 | 1.5 |
| total | 12 | | |
\[\bar x = \frac{3(0) + 4(2) + 5(2)}{12} = \frac{18}{12} = 1.5\ \text{cm}, \qquad \bar y = \frac{3(1.5) + 4(0) + 5(1.5)}{12} = \frac{12}{12} = 1\ \text{cm}\]
So \(G\) is \(1.5\) cm from \(AB\) and \(1\) cm from \(BC\). It is not the centroid of the triangular lamina \((\tfrac43, 1)\): a wire frame and a lamina of the same shape have different centres of mass.
:::

:::eg A uniform wire is bent into a semicircular arc of radius \(10\) cm, and the two ends of the arc are joined by a straight piece of the same wire along the diameter. Find the distance of the centre of mass from the diameter.
Take the diameter as the \(x\) axis and the axis of symmetry as the \(y\) axis.

The arc has length \(\pi r = 10\pi\) and, with \(\alpha = \tfrac\pi2\), its centre of mass is \(\dfrac{r\sin\alpha}{\alpha} = \dfrac{2r}{\pi} = \dfrac{20}{\pi}\) from the diameter. The diameter has length \(20\) and its centre of mass is on the \(x\) axis.
\[\bar y = \frac{10\pi \times \frac{20}{\pi} + 20 \times 0}{10\pi + 20} = \frac{200}{10\pi + 20} = \frac{20}{\pi + 2} = 3.89\ \text{cm}\]
The centre of mass is \(3.89\) cm from the diameter, on the same side as the arc.
:::

## Bodies hanging freely

If a body hangs freely from a point \(P\), its weight acts at \(G\), and the only other force acts at \(P\). For equilibrium these two forces must be along the same vertical line, so **\(G\) is vertically below \(P\)**. This one fact fixes the way the body hangs, and gives the angle of any chosen line in the body with the vertical.

:::html
<figure class="fig small"><svg viewBox="10 15 290 225" role="img" aria-label="The L-shaped lamina of the previous figure hanging freely from the vertex A. A dashed vertical line runs from A down through the centre of mass G, so G is directly below A. The edge AF makes an angle theta with this vertical. The angle theta satisfies tan theta equals the x coordinate of G divided by the y coordinate of G, which is 19 over 16.">
  <path class="ln thick" d="M150 26V40"/>
  <path class="ln-m thin dash" d="M150 40V232"/>
  <polygon class="fm s-acc sw2" points="150,40 36.6,174.6 87.1,217.1 158,133 225.3,189.7 267.8,139.2"/>
  <path class="ln-m thin" d="M150 80A40 40 0 0 0 180.6 65.8"/>
  <circle class="fi" cx="150" cy="40" r="3"/>
  <circle class="fr" cx="150" cy="131.1" r="4"/>
  <text class="tl" x="158" y="34">A</text>
  <text class="tl halo" x="140" y="136" text-anchor="end">G</text>
  <text class="tl" x="274" y="143">F</text>
  <text class="tl" x="30" y="178" text-anchor="end">B</text>
  <text class="tl" x="168" y="96">θ</text>
  <text class="tl" x="156" y="226">vertical</text>
</svg><figcaption>The L-shaped lamina hanging freely from A. G is vertically below A, so the dashed vertical through A passes through G. The edge AF makes the angle θ with it, where tan θ = x̄ ÷ ȳ.</figcaption></figure>
:::

:::eg (Exam style) The L-shaped lamina of the earlier example (\(A = (0,0)\), \(F = (0, 7)\), centre of mass at \(\left(\tfrac{19}{6}, \tfrac83\right)\)) is freely suspended from the vertex \(A\). Find the angle that \(AF\) makes with the vertical.
When the lamina hangs, \(G\) is vertically below \(A\). [B1]

Measured from \(A\), \(G\) is \(\tfrac{19}{6}\) along \(AB\) and \(\tfrac83\) along \(AF\). The line \(AG\) is vertical, so the angle \(\theta\) between \(AF\) and \(AG\) has
\[\tan\theta = \frac{\text{distance of } G \text{ from } AF}{\text{distance of } G \text{ along } AF} = \frac{19/6}{8/3} = \frac{19}{16}\] [M1 A1]
\[\theta = 49.9^\circ\] [A1]
**Check**: from the figure, \(AF\) is the edge sloping down to the right at about \(50^\circ\) from the vertical dashed line. ✓
:::

:::exam What MF19 gives you, and the form of the question
MF19 gives the standard results in the table above (triangle, hemisphere solid and shell, cone and pyramid, arc, sector). It does **not** give the semicircle results (use \(\alpha = \tfrac\pi2\)), cylinder and cuboid (by symmetry), or the formula for combining parts: learn \(\bar x = \dfrac{\sum mx}{\sum m}\). A "show that" question expects the volumes or areas, the distances from the common point, the moment equation, and the answer, so write each as its own line. Questions are often set as an expression in \(r\) and \(h\), or ask you to find a dimension that puts \(G\) in a particular place: set up the equation, and solve.
:::

:::board
Edexcel IAL Mechanics 2 includes centres of mass of composite bodies, in a form close to this chapter, and Edexcel and the UK boards take \(g = 9.8\) where 9231 takes \(g = 10\); the centre of mass positions themselves do not depend on \(g\).
:::

:::eg Spot the error: a solid is a uniform cone of base radius \(4\) cm and height \(12\) cm, joined at its base to a uniform solid cylinder of radius \(4\) cm and height \(6\) cm. Find the distance of its centre of mass from the common face (4 marks).
A student wrote this answer.

Line 1: Cone volume \(\tfrac13\pi \times 16 \times 12 = 64\pi\), cylinder volume \(\pi \times 16 \times 6 = 96\pi\)
Line 2: Cone: \(G\) is \(\tfrac34 \times 12 = 9\) cm from the common face. Cylinder: \(G\) is \(3\) cm from the common face on the other side.
Line 3: \(160\bar x = 64 \times 9 - 96 \times 3\), so \(\bar x = \dfrac{576 - 288}{160} = 1.8\) cm

Line 1 is correct. [B1] The method in line 3 is right: volumes as masses, moments about the common face. [M1]

**Line 2 is wrong for the cone.** [B0] The \(\tfrac34h\) of the MF19 table is measured from the **vertex**. From the common face, which is the base, the cone's centre of mass is \(\tfrac14 \times 12 = 3\) cm. The cylinder's \(3\) cm is right. The answer is wrong. [A0] The student scores 2 out of 4.

Correct line 3: \(160\bar x = 64(3) - 96(3) = -96\), so \(\bar x = -0.6\): the centre of mass is \(0.6\) cm from the common face, in the cylinder.

**Check**: the heavier cylinder (volume \(96\pi\)) is on that side, so \(G\) is on its side of the common face. ✓
:::

:::try Start easy, finish at exam standard
Q: Masses of \(1\) kg, \(4\) kg and \(5\) kg are at \(x = 0\), \(x = 2\) and \(x = 7\) on a line. Find the position of the centre of mass.
A: \(\bar x = \dfrac{0 + 8 + 35}{10} = 4.3\).
Q: A uniform rod \(PQ\) of length \(2\) m is acted on by a force of \(15\) N at \(Q\), at \(40^\circ\) to the rod. Find the moment of the force about \(P\).
A: \(15\sin 40^\circ \times 2 = 19.3\) N m.
Q: Find the centre of mass of a triangular lamina with vertices \((1, 2)\), \((7, 2)\) and \((4, 8)\).
A: \(\bar x = \dfrac{1 + 7 + 4}{3} = 4\), \(\bar y = \dfrac{2 + 2 + 8}{3} = 4\).
Q: A uniform solid hemisphere has radius \(8\) cm. How far is its centre of mass from the centre of its plane face?
A: \(\tfrac38 \times 8 = 3\) cm.
Q: A uniform solid cone has height \(20\) cm. How far is its centre of mass from the vertex? From the base?
A: From the vertex \(\tfrac34 \times 20 = 15\) cm; from the base \(5\) cm.
Q: A uniform circular arc of radius \(9\) cm subtends an angle of \(120^\circ\) at the centre. Find the distance of its centre of mass from the centre of the circle.
A: \(2\alpha = 120^\circ = \tfrac{2\pi}{3}\), so \(\alpha = \tfrac\pi3\). Distance \(\dfrac{r\sin\alpha}{\alpha} = \dfrac{9 \times 0.8660}{1.0472} = 7.44\) cm.
Q: A uniform lamina is a rectangle \(6 \times 4\) with a smaller rectangle \(2 \times 2\) removed from one corner. Find the centre of mass if the large rectangle has corners \((0,0)\) and \((6,4)\) and the removed one is \([4,6] \times [2,4]\).
A: Areas \(24\) and \(-4\); centres \((3, 2)\) and \((5, 3)\). \(\bar x = \dfrac{72 - 20}{20} = 2.6\), \(\bar y = \dfrac{48 - 12}{20} = 1.8\).
Q: A uniform lamina is a rectangle \(6\) cm wide and \(4\) cm tall with an isosceles triangle of base \(6\) cm and height \(3\) cm on one \(6\) cm side. Find the distance of the centre of mass from the opposite side.
A: Rectangle: area \(24\) at \(2\). Triangle: area \(9\) at \(4 + 1 = 5\). \(\bar y = \dfrac{48 + 45}{33} = 2.82\) cm.
Q: Two particles of mass \(m\) and \(3m\) are \(12\) cm apart. How far from the lighter one is the centre of mass?
A: \(\bar x = \dfrac{3m \times 12}{4m} = 9\) cm from the lighter particle.
Q: A framework is a uniform wire in the shape of an equilateral triangle \(ABC\) of side \(a\). Where is its centre of mass?
A: By symmetry, at the centre of the triangle (the centroid), a distance \(\dfrac{a}{2\sqrt3}\) from each side.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Particles of mass \(1\) kg, \(2\) kg and \(5\) kg are at \((0, 0)\), \((4, 3)\) and \((-2, 5)\). Find the coordinates of the centre of mass.
A: \(\sum m = 8\). \(\bar x = \dfrac{0 + 8 - 10}{8} = -0.25\) [M1 A1], \(\bar y = \dfrac{0 + 6 + 25}{8} = 3.875\). [A1]
Q: [3 marks] ★ A light rod \(OA\) of length \(2.4\) m has a force of \(15\) N applied at \(A\), at \(40^\circ\) to the rod. Find the moment of the force about \(O\).
A: The component perpendicular to the rod is \(15\sin 40^\circ\). [B1] Moment \(= 15\sin 40^\circ \times 2.4\) [M1] \(= 23.1\) N m. [A1]
Q: [5 marks] ★★ A uniform rectangular lamina has corners \((0,0)\), \((9,0)\), \((9,4)\) and \((0,4)\) (in cm). A rectangle with corners \((6, 2)\), \((9, 2)\), \((9, 4)\), \((6, 4)\) is cut out. Find the centre of mass of the remaining lamina.
A: Areas: whole \(36\) at \((4.5, 2)\), removed \(6\) at \((7.5, 3)\), remaining \(30\). [B1 B1]
\(30\bar x = 36(4.5) - 6(7.5)\) [M1], \(\bar x = \dfrac{117}{30} = 3.9\). [A1]
\(30\bar y = 36(2) - 6(3) = 54\), \(\bar y = 1.8\). [A1]
Q: [5 marks] ★★ A solid consists of a uniform cylinder of radius \(3\) cm and height \(4\) cm with a uniform cone of base radius \(3\) cm and height \(6\) cm joined to one end. Find the distance of the centre of mass from the free end of the cylinder.
A: Volumes (\(\div\pi\)): cylinder \(9 \times 4 = 36\) at \(2\); cone \(\tfrac13 \times 9 \times 6 = 18\) at \(4 + \tfrac14 \times 6 = 5.5\). [B1 B1]
\(54\bar x = 36(2) + 18(5.5)\) [M1 A1], \(\bar x = \dfrac{171}{54} = 3.17\) cm. [A1]
Q: [5 marks] ★★ A uniform lamina consists of a rectangle \(8\) cm by \(5\) cm with a semicircle of diameter \(8\) cm attached along one of the \(8\) cm sides. Find the distance of the centre of mass of the lamina from the opposite \(8\) cm side.
A: Rectangle: area \(40\), centre at \(2.5\) from the far side. Semicircle: area \(\tfrac12\pi \times 16 = 8\pi\). [B1]
Centre of the semicircle: \(\dfrac{4 \times 4}{3\pi} = \dfrac{16}{3\pi} = 1.698\) from its diameter, using the sector result with \(\alpha = \tfrac\pi2\). [B1]
So its distance from the far side is \(5 + 1.698 = 6.698\). [B1]
\[(40 + 8\pi)\bar y = 40(2.5) + 8\pi(6.698)\] [M1]
\[\bar y = \frac{100 + 168.3}{65.13} = 4.12\ \text{cm}\] [A1]
Q: [9 marks] (#math.p1.trig) ★★★ A uniform lamina is made by joining a square \(ABCD\) of side \(6\) cm to an isosceles triangle with base \(CD\) and height \(4\) cm, so that the triangle stands on the side \(CD\) and the shape is symmetrical about the line through the midpoints of \(AB\) and \(CD\). (a) Find the distance of the centre of mass of the lamina from \(AB\). (b) The lamina is freely suspended from \(A\). Find the angle that \(AD\) makes with the vertical. (c) Without calculation, state the angle that \(BC\) makes with the vertical when the lamina hangs from \(B\), with a reason.
H: The lamina is symmetric, so \(G\) is on the axis of symmetry, \(3\) cm from \(AD\).
H: The triangle's centre of mass is \(\tfrac13\) of its height above its base.
H: When hanging from \(A\), \(G\) is below \(A\): use \(\tan\theta = \dfrac{\text{distance of } G \text{ from } AD}{\text{distance of } G \text{ from } AB}\).
A: (a) Areas: square \(36\), triangle \(\tfrac12 \times 6 \times 4 = 12\). [B1]
Heights above \(AB\): square \(3\), triangle \(6 + \tfrac43 = \tfrac{22}{3}\). [B1]
\(48\bar y = 36(3) + 12\left(\tfrac{22}{3}\right) = 196\) [M1], so \(\bar y = \tfrac{49}{12} = 4.08\) cm. [A1]
By symmetry \(G\) is \(3\) cm from \(AD\). [B1]
(b) \(G\) is vertically below \(A\), so \(\tan\theta = \dfrac{3}{49/12}\) [M1] \(= \dfrac{36}{49}\). [A1] \(\theta = 36.3^\circ\). [A1]
(c) The shape is symmetric about the axis through the midpoints of \(AB\) and \(CD\), so the angle is again \(36.3^\circ\). [B1]
Q: [7 marks] (#math.p1.circular) ★★★ A uniform wire of length \(15\pi + 30\) cm is bent into a semicircular arc of radius \(15\) cm, with a straight piece of wire joining its ends along the diameter \(AB\). The framework hangs freely from \(A\). Find the angle that \(AB\) makes with the horizontal.
H: The arc has length \(15\pi\) and the diameter \(30\). Use the arc formula with \(\alpha = \tfrac\pi2\).
H: \(G\) is vertically below \(A\): \(AG\) is vertical, and \(AB\) makes an angle \(\varphi\) with the horizontal with \(\tan\varphi = \dfrac{\bar y}{15}\), where \(\bar y\) is the distance of \(G\) from \(AB\).
A: Lengths: arc \(15\pi\), diameter \(30\). [B1]
The arc's centre of mass is \(\dfrac{2r}{\pi} = \dfrac{30}{\pi}\) from the diameter. [B1]
\[(15\pi + 30)\bar y = 15\pi \times \frac{30}{\pi} + 30 \times 0 = 450\] [M1]
\[\bar y = \frac{450}{15\pi + 30} = \frac{30}{\pi + 2} = 5.83\ \text{cm}\] [A1]
\(G\) is vertically below \(A\) and is \(15\) cm along \(AB\) from \(A\) (by symmetry) and \(\bar y\) from it. [B1]
\(\tan\varphi = \dfrac{5.834}{15}\) [M1] so \(\varphi = 21.3^\circ\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A uniform solid cylinder has radius \(r\) and height \(h\). A uniform solid hemisphere of the same material and radius \(r\) is attached to one end. (a) Show that the centre of mass of the combined solid is in the plane where the two join if and only if \(h = \dfrac{r}{\sqrt2}\). (b) Find \(h\) when \(r = 10\) cm.
H: Take moments about the join: the two parts must have equal and opposite moments.
H: The cylinder's centre is \(\tfrac12h\) on one side, the hemisphere's \(\tfrac38r\) on the other.
A: Cylinder: volume \(\pi r^2h\), centre of mass \(\tfrac12h\) from the join. [B1] Hemisphere: volume \(\tfrac23\pi r^3\), centre \(\tfrac38r\) on the other side. [B1]
For \(G\) to be in the join the moments must balance:
\[\pi r^2h \times \tfrac12h = \tfrac23\pi r^3 \times \tfrac38r\] [M1]
\[\tfrac12r^2h^2 = \tfrac14r^4 \quad\Rightarrow\quad h^2 = \tfrac12r^2\] [A1]
\(h = \dfrac{r}{\sqrt2}\), which proves the statement. [A1] For \(r = 10\), \(h = 7.07\) cm. [B1]
Q: [6 marks] ★★★ A uniform circular disc has centre \(C\) and radius \(2a\). A circular hole of radius \(a\) is cut out, with its centre \(H\) at distance \(a\) from \(C\). The point \(P\) is on the rim, with \(CP\) perpendicular to \(CH\). Show that the centre of mass of the remaining lamina is at distance \(\tfrac13a\) from \(C\), on the opposite side of \(C\) from \(H\), and find the angle between \(CP\) and the vertical when the lamina hangs freely from \(P\).
H: Treat the hole as negative mass: areas \(4\pi a^2\) and \(-\pi a^2\).
H: With \(C\) as origin and \(H = (a, 0)\), \(P = (0, 2a)\); \(G\) is vertically below \(P\).
A: Areas: disc \(4\pi a^2\) at \(C\), hole \(\pi a^2\) at \(H\). [B1]
\(3\pi a^2\bar x = 4\pi a^2(0) - \pi a^2(a)\) [M1], so \(\bar x = -\tfrac13a\): the distance is \(\tfrac13a\) on the side away from \(H\). [A1]
With \(P = (0, 2a)\), \(G\) is vertically below \(P\), and \(\tan\theta = \dfrac{a/3}{2a}\) [M1] \(= \tfrac16\) [A1], so \(\theta = 9.46^\circ\) between \(CP\) and the vertical. [A1]
:::

:::quiz
? Where is the centre of mass of a uniform solid cone of height \(h\)?
+ \(\tfrac14h\) from the base, on the axis
- \(\tfrac12h\) from the base, on the axis
- \(\tfrac13h\) from the base, on the axis
- \(\tfrac14h\) from the vertex, on the axis
> The MF19 result is \(\tfrac34h\) from the vertex, which is \(\tfrac14h\) from the base. \(\tfrac13h\) is the answer for a triangular lamina, and \(\tfrac12h\) would be a cylinder.
? A uniform solid is made of a cone and a hemisphere with the same base radius. To find its centre of mass by moments, which should be used as the "masses"?
+ The volumes of the two parts
- The heights of the two parts
- The surface areas of the two parts
- The base radii of the two parts
> The body is uniform, so mass is proportional to volume. Heights and radii are not masses, and surface area matters only for a hollow shell.
? A circular hole is cut in a uniform lamina. In the table for \(\bar x\), how is the hole entered?
- With its area as a positive mass at the hole's centre
+ With its area as a negative mass at the hole's centre
- It is ignored, because there is no material there
- With zero mass, but at the centre of the lamina
> Subtracting a part is the same as adding a negative mass at that part's centre of mass. Ignoring the hole gives the centre of the full lamina.
? A uniform lamina hangs freely from a corner \(P\). Which statement is true in equilibrium?
+ The centre of mass is vertically below \(P\)
- The centre of mass is at the same height as \(P\)
- The longest edge is vertical
- The centre of mass is on the line \(P\) to the opposite corner
> The weight at \(G\) and the reaction at \(P\) must act on one vertical line, so \(G\) is directly below \(P\). The longest edge is vertical only in special cases.
? The centre of mass of a uniform semicircular lamina of radius \(r\) is at what distance from the centre of the straight edge?
+ \(\dfrac{4r}{3\pi}\)
- \(\dfrac{2r}{\pi}\)
- \(\dfrac{r}{2}\)
- \(\dfrac{3r}{8}\)
> The sector formula \(\dfrac{2r\sin\alpha}{3\alpha}\) with \(\alpha = \tfrac\pi2\) gives \(\dfrac{4r}{3\pi}\). The value \(\dfrac{2r}{\pi}\) is for a semicircular wire (arc), \(\dfrac{r}{2}\) for a hemispherical shell, and \(\dfrac{3r}{8}\) for a solid hemisphere.
? A uniform wire is bent into the shape of a triangle. How does its centre of mass compare with that of a uniform lamina of the same shape?
- They are the same point
+ They are in general different points, because the wire's mass is proportional to length and the lamina's to area
- The wire's is always at the circumcentre
- The wire's is always at a vertex
> For a wire each side counts by its length at its midpoint; for a lamina the whole area is spread over the triangle. The example in this chapter gives \((1.5, 1)\) for the wire and \(\left(\tfrac43, 1\right)\) for the lamina.
:::

:::checklist What you can now do
- [ ] I can find the moment of a force about a point, using the perpendicular distance or the perpendicular component.
- [ ] I can state that the weight of a body acts at its centre of mass, and find the centre of mass of a uniform body by symmetry.
- [ ] I can find the centre of mass of a set of particles in a line or plane.
- [ ] I can use the MF19 results for triangles, hemispheres, cones, arcs and sectors, including the semicircle as a sector with \(\alpha = \tfrac\pi2\).
- [ ] I can find the centre of mass of a composite lamina, including one with a part removed.
- [ ] I can find the centre of mass of a composite solid made from cylinders, cones and hemispheres, and of a wire framework.
- [ ] I can find the angle at which a lamina or solid hangs when it is freely suspended from a point.
:::

:::recap
- Moment \(= F \times\) perpendicular distance: use \(F\sin\varphi \times x\) for a force at angle \(\varphi\) to a rod. Choose a sense and keep to it.
- The weight acts at the centre of mass \(G\). A line or plane of symmetry contains \(G\).
- \(\bar x = \dfrac{\sum mx}{\sum m}\), \(\bar y = \dfrac{\sum my}{\sum m}\): mass \(\propto\) area (lamina), volume (solid), length (wire).
- MF19: triangle \(\tfrac23\) along a median from the vertex; solid hemisphere \(\tfrac38r\); hemispherical shell \(\tfrac12r\); cone \(\tfrac34h\) from the vertex (\(\tfrac14h\) from the base); arc \(\dfrac{r\sin\alpha}{\alpha}\); sector \(\dfrac{2r\sin\alpha}{3\alpha}\) (angle \(2\alpha\)).
- Semicircle lamina \(\dfrac{4r}{3\pi}\) and arc \(\dfrac{2r}{\pi}\) come from \(\alpha = \tfrac\pi2\).
- A removed part has negative mass. Measure every distance from one point.
- A body hanging freely from \(P\) has \(G\) vertically below \(P\); \(\tan\theta = \dfrac{\text{horizontal offset}}{\text{vertical distance}}\).
:::

:::links
- watch: [Composite laminas playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiGwlCjUDNys8kZTVhE46ee) · ExamSolutions (YouTube) · worked centre of mass questions for laminas and solids
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · centres of mass booklets with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Further Mechanics questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Equilibrium of a rigid body](#math.fm.rigid) uses moments and centres of mass to solve problems on ladders, hinged rods, toppling and sliding.
