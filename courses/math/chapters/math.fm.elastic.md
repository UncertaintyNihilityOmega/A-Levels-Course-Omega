@chapter math.fm.elastic
@title Hooke's law and elastic energy
@level fm
@paper CAIE 9231 Paper 3
@time 5–6 hours
@summary An elastic string or spring pulls or pushes with a force that grows in proportion to its extension. You will learn Hooke's law and the modulus of elasticity, find equilibrium positions for one or two strings, use the elastic energy \(\dfrac{\lambda x^2}{2l}\) in energy equations with kinetic energy, gravity and friction, and find the greatest speed and the greatest extension of a particle on a string or spring.

:::why
Ropes, bungee cords, bows, car suspensions and the springs inside a pen all store energy when they are stretched or squashed. One simple rule, Hooke's law, describes them well, and it turns an unfamiliar object into a force you can put into Newton's second law or an energy equation. Strings appear on slopes, on tables, hanging, and later in circles.
:::

**Before you start**, you need work, kinetic energy and gravitational potential energy from [Work, energy and power](#math.m.energy), friction and Newton's second law from [Newton's laws and connected particles](#math.m.newton), and resolving forces on a slope from [Forces and equilibrium](#math.m.forces).

:::try Warm-up
Q: A 2 kg block slides from rest down a smooth slope, travelling 3 m along a slope inclined at \(30^\circ\) to the horizontal. Find its speed. Take \(g = 10\). (from [Work, energy and power](#math.m.energy))
A: It drops \(3\sin 30^\circ = 1.5\) m, so \(\tfrac12 \times 2 \times v^2 = 2 \times 10 \times 1.5\), giving \(v^2 = 30\) and \(v = 5.48\) m s⁻¹.
Q: A 4 kg particle is pulled along a rough horizontal floor by a horizontal force of 20 N. The coefficient of friction is 0.3. Find its acceleration. Take \(g = 10\). (from [Newton's laws and connected particles](#math.m.newton))
A: \(R = 40\), so friction \(= 0.3 \times 40 = 12\) N, and \(20 - 12 = 4a\), giving \(a = 2\) m s⁻².
Q: A particle of weight 12 N rests on a smooth slope inclined at \(30^\circ\), held by a force parallel to the slope. Find the force. (from [Forces and equilibrium](#math.m.forces))
A: Resolve along the slope: \(F = 12\sin 30^\circ = 6\) N.
:::

## Hooke's law

Pull a rubber band: the further you stretch it, the harder it pulls back. For most strings and springs, if you do not stretch them too far, the pull is directly proportional to the stretch. That is Hooke's law. To use it you need three words.

:::def Natural length
The length \(l\) of an elastic string or spring when no force acts on it: it is neither stretched nor compressed.
:::

:::def Extension
The amount \(x\) by which an elastic string or spring is longer than its natural length: \(x = \text{current length} - l\). For a spring squashed shorter than \(l\), the same distance is called the compression.
:::

:::def Modulus of elasticity
The constant \(\lambda\) in Hooke's law (the Greek letter lambda). It is measured in newtons and measures how stiff the material is for strings of any length: a larger \(\lambda\) needs a larger force for the same strain \(x/l\). A string is **light** when its mass is negligible, so the tension is the same all along it.
:::

:::key Hooke's law
The tension \(T\) in an elastic string, or the tension or thrust in a spring, with natural length \(l\), modulus \(\lambda\) and extension (or compression) \(x\), is
\[T = \frac{\lambda x}{l}\]
\(T\) is proportional to \(x\). Doubling the extension doubles the force. The ratio \(\dfrac{\lambda}{l}\) is the **stiffness** of that particular piece (units N m⁻¹): the force per metre of extension.
:::

Notice what \(\lambda\) and \(l\) do. A string made twice as long (double \(l\)) from the same material is twice as easy to stretch by a given \(x\), because \(\dfrac{\lambda}{l}\) halves. The modulus \(\lambda\) does not change; it belongs to the material and the cross-section, not to the length.

:::exam What is given on MF19
MF19 gives \(T = \dfrac{\lambda x}{l}\) and the elastic energy \(E = \dfrac{\lambda x^2}{2l}\). It does not tell you the units, which direction the force acts, or that a string cannot push. Those you must know.
:::

### Strings and springs

A **string** can only pull. When its length is less than \(l\) it is slack and the tension is zero; it does not push. A **spring** can be stretched or compressed, and Hooke's law holds for both: when compressed by \(x\) it pushes with a **thrust** \(\dfrac{\lambda x}{l}\). Always say which you have. A question with a "light elastic string" has slack states; a question with a "light spring" (or "elastic spring") may compress.

:::eg A light elastic string has natural length 0.8 m and modulus of elasticity 24 N. (a) Find the tension when the string is stretched to a length of 1.0 m. (b) Find the length of the string when the tension is 15 N.
(a) The extension is \(x = 1.0 - 0.8 = 0.2\) m, not 1.0 m.
\[T = \frac{24 \times 0.2}{0.8} = 6\ \mathrm{N}\]
(b) Rearrange Hooke's law for the extension:
\[x = \frac{Tl}{\lambda} = \frac{15 \times 0.8}{24} = 0.5\ \mathrm{m}\]
The length is \(0.8 + 0.5 = 1.3\) m. Always add the natural length back: the question asked for the length, not the extension.
:::

:::eg A particle of mass 0.5 kg hangs in equilibrium from a fixed point by a light elastic string of natural length 0.6 m. The length of the string is 0.75 m. Find the modulus of elasticity. Take \(g = 10\).
The extension is \(0.75 - 0.6 = 0.15\) m. In equilibrium the tension balances the weight: \(T = mg = 5\) N.
\[5 = \frac{\lambda \times 0.15}{0.6} \quad\Rightarrow\quad \lambda = \frac{5 \times 0.6}{0.15} = 20\ \mathrm{N}\]
**Check**: \(\dfrac{20 \times 0.15}{0.6} = 5\) N. ✓
:::

:::warn Extension, not length
The most common lost mark in this chapter is writing the length of the string where the extension belongs. In \(T = \dfrac{\lambda x}{l}\) the bottom is the natural length and the top is the *extra* length. Write "extension \(= \dots - \dots\)" as your first line each time.
:::

## Equilibrium with elastic strings

At rest, the forces on a particle add up to zero. With an elastic string the unknown force is usually the tension, and Hooke's law then turns that tension into a length. The method is the one you know from [Forces and equilibrium](#math.m.forces), with one extra equation.

:::steps
1. Draw the particle and every force on it: weight, tension (or thrust) along each string or spring, normal reaction, friction.
2. Resolve along and across the line of motion, or vertically and horizontally.
3. Use Hooke's law to write each tension as \(\dfrac{\lambda x}{l}\) with its own \(x\).
4. Use the geometry to link the extensions to each other (for two strings, the total length is fixed).
:::

### Two strings, one on each side

When a particle on a smooth horizontal table is joined to two fixed points \(A\) and \(B\), the table gives no force along the line, so the two tensions are equal. The two lengths add to the distance \(AB\).

:::eg A particle \(P\) lies on a smooth horizontal table. It is attached to two light elastic strings: \(AP\) has natural length 0.6 m and modulus 12 N, and \(PB\) has natural length 0.5 m and modulus 15 N. The points \(A\) and \(B\) are 2.0 m apart on the table, and \(P\) is in equilibrium on the line \(AB\). Find the tension and the length \(AP\).
Let the extensions be \(x\) (in \(AP\)) and \(y\) (in \(PB\)). The tensions are equal:
\[\frac{12x}{0.6} = \frac{15y}{0.5} \quad\Rightarrow\quad 20x = 30y \quad\Rightarrow\quad x = 1.5y\]
The lengths add up to 2.0 m:
\[(0.6 + x) + (0.5 + y) = 2.0 \quad\Rightarrow\quad x + y = 0.9\]
Substitute: \(2.5y = 0.9\), so \(y = 0.36\) and \(x = 0.54\).
\[T = 20 \times 0.54 = 10.8\ \mathrm{N}, \qquad AP = 0.6 + 0.54 = 1.14\ \mathrm{m}\]
**Check**: \(30 \times 0.36 = 10.8\) N. ✓
:::

### A spring that compresses

:::eg A light spring has natural length 0.5 m and modulus of elasticity 40 N. It stands vertically on a table, and a block of mass 2 kg rests on its upper end. Find the length of the spring. Take \(g = 10\).
The block is at rest, so the spring pushes up with a thrust equal to the weight, 20 N. The spring is compressed:
\[20 = \frac{40x}{0.5} \quad\Rightarrow\quad x = 0.25\ \mathrm{m}\]
The length is \(0.5 - 0.25 = 0.25\) m. A string could not do this: it would just go slack.
:::

### A particle on a slope

On a slope, resolve along the slope. If the surface is rough, the particle can rest anywhere from "about to slide down" to "about to slide up", so the tension has a **range** and so does the extension.

:::html
<figure class="fig small"><svg viewBox="0 0 340 210" role="img" aria-label="A particle P on a slope rising to the right at 30 degrees to the horizontal. A light elastic string from P runs up the slope to a fixed point O at the top. Four forces act on P: the tension T up the slope along the string, the weight mg vertically down, the normal reaction R perpendicular to the slope, and friction F down the slope."><path class="ax" d="M20 190H300"/><path class="ln thick" d="M20 190L300 28.3"/><path class="ln-m thin dash" d="M300 190V28.3"/><path class="c3" d="M145.5 107.2L300 17.9"/><circle class="f1 s-acc sw2" cx="145.5" cy="107.2" r="9"/><rect class="f2 s-acc sw2" x="296" y="14" width="8" height="8"/><path class="c1 thick" d="M145.5 107.2L199.2 76.2" marker-end="url(#ah)"/><path class="c2 thick" d="M145.5 107.2V155.2" marker-end="url(#ah)"/><path class="c4 thick" d="M145.5 107.2L121.5 65.6" marker-end="url(#ah)"/><path class="c3 dash thick" d="M145.5 107.2L112.6 126.2" marker-end="url(#ah)"/><path class="ln thin" d="M60 190A40 40 0 0 0 54.6 170"/><text class="tl" x="70" y="185">θ</text><text class="tl" x="198" y="62">T</text><text class="tl" x="152" y="170">mg</text><text class="tl" x="104" y="66">R</text><text class="tl" x="94" y="132">F</text><text class="tl" x="308" y="16">O</text></svg><figcaption>A particle \(P\) on a rough slope held by a string from \(O\). \(T\) acts along the string, \(R\) is perpendicular to the slope, and \(F\) is shown acting down the slope, for the case in which \(P\) is about to slide up.</figcaption></figure>
:::

:::eg A particle \(P\) of mass 2 kg lies on a rough plane inclined at \(\theta\) to the horizontal, where \(\sin\theta = 0.6\) and \(\cos\theta = 0.8\). The coefficient of friction is 0.5. \(P\) is attached to one end of a light elastic string of natural length 1 m and modulus 30 N. The other end is fixed to a point \(O\) on the plane, up the line of greatest slope from \(P\). \(P\) rests in equilibrium with the string taut. Find the greatest and least possible extensions of the string. Take \(g = 10\).
Perpendicular to the plane: \(R = 2 \times 10 \times 0.8 = 16\) N, so the limiting friction is \(0.5 \times 16 = 8\) N. The weight component down the slope is \(2 \times 10 \times 0.6 = 12\) N.

About to slide **down** (friction up the slope), \(T\) is smallest: \(T + 8 = 12\), so \(T = 4\) N.

About to slide **up** (friction down the slope), \(T\) is largest: \(T = 12 + 8 = 20\) N.

The extension is \(x = \dfrac{Tl}{\lambda} = \dfrac{T}{30}\), so
\[\frac{4}{30} \le x \le \frac{20}{30} \quad\Rightarrow\quad 0.133\ \mathrm{m} \le x \le 0.667\ \mathrm{m}\]
:::

## Elastic potential energy

A stretched string stores energy: you did work to stretch it, and it can give that work back. The energy stored is the work done in stretching it, which is the area under the graph of tension against extension.

:::def Elastic potential energy (EPE)
The energy stored in a stretched string or a stretched or compressed spring. For extension (or compression) \(x\), natural length \(l\) and modulus \(\lambda\), it is \(\dfrac{\lambda x^2}{2l}\).
:::

:::key Elastic potential energy
\[E = \frac{\lambda x^2}{2l}\]
Equivalent forms: \(E = \tfrac12 T x\) (half the tension times the extension) and \(E = \tfrac12 \times\) stiffness \(\times\, x^2\). The energy depends on the **square** of the extension: stretching to twice the length stores four times the energy.
:::

:::plot Tension against extension for a string with λ = 20 N and l = 0.5 m, so T = 40x. The shaded triangle up to x = 0.3 has area ½ × 0.3 × 12 = 1.8 J, the elastic energy stored.
--f "40*x" --x 0 0.45 --y 0 20 --shade "0,0,0.3" --pt "0.3,12,(0.3, 12)@nw" --label "T = 40x" --xlabel "x (m)" --ylabel "T (N)" --legend tr
:::

:::proof Why the energy is \(\dfrac{\lambda x^2}{2l}\) (not examined)
The energy is the work done by the tension as the string extends from 0 to \(x\).
1. When the extension is \(s\), the tension is \(\dfrac{\lambda s}{l}\) (Hooke's law).
2. A small extra stretch \(\delta s\) needs work \(\dfrac{\lambda s}{l}\,\delta s\), as the force is nearly constant over it.
3. Adding all the small amounts gives the integral \(\displaystyle\int_0^x \frac{\lambda s}{l}\,ds\).
4. Integrate: \(\dfrac{\lambda}{l} \times \dfrac{s^2}{2}\), evaluated from 0 to \(x\).
5. So the work is \(\dfrac{\lambda x^2}{2l}\).
6. This is the area of the triangle under the line \(T = \dfrac{\lambda s}{l}\): half the base \(x\) times the height \(\dfrac{\lambda x}{l}\), the same answer.
:::

:::eg A light elastic string has natural length 1.5 m and modulus of elasticity 45 N. Find (a) the elastic energy stored when its extension is 0.4 m, (b) the work needed to stretch it from an extension of 0.4 m to an extension of 0.9 m.
(a)
\[E = \frac{45 \times 0.4^2}{2 \times 1.5} = \frac{7.2}{3} = 2.4\ \mathrm{J}\]
(b) The work done is the **difference** of the two energies:
\[\begin{aligned}
E_{0.9} - E_{0.4} &= \frac{45 \times 0.81}{3} - 2.4 \\
&= 12.15 - 2.4 = 9.75\ \mathrm{J}
\end{aligned}\]
Do not use \(\dfrac{\lambda (0.5)^2}{2l}\): the energy depends on the squares of the two extensions, not on the square of their difference.
:::

## Energy problems with strings and springs

The work–energy principle from [Work, energy and power](#math.m.energy) gains one more term. For a particle moving from a first position to a second position,

\[\text{KE} + \text{GPE} + \text{EPE (start)} = \text{KE} + \text{GPE} + \text{EPE (end)} + \text{work done against friction}\]

If there is a driving force add its work to the left. If there is no friction, this is conservation of energy.

:::steps
1. Name the two positions (start, end) and the extension at each. A slack string has zero EPE.
2. Choose a level for zero GPE and write the heights.
3. Write the energy equation in words, then with numbers: KE, GPE and EPE at both positions, plus work against friction.
4. Solve. For a "greatest extension" the speed is zero; for the greatest speed see the next section.
:::

### On a smooth horizontal table

:::eg A particle of mass 0.4 kg lies on a smooth horizontal table. It is attached to one end of a light elastic string of natural length 0.5 m and modulus 20 N. The other end is fixed to a point \(O\) on the table. The particle is held at 0.8 m from \(O\) and released from rest. Find its speed when the string becomes slack.
The extension at the start is \(0.8 - 0.5 = 0.3\) m, so the stored energy is
\[E = \frac{20 \times 0.3^2}{2 \times 0.5} = 1.8\ \mathrm{J}\]
The string goes slack at 0.5 m from \(O\), where all of that energy is kinetic:
\[\tfrac12 \times 0.4 \times v^2 = 1.8 \quad\Rightarrow\quad v^2 = 9\]
The speed is 3 m s⁻¹. After that the particle moves on at constant speed on the smooth table: the string only pulls, and it can only pull while stretched.
:::

:::eg A particle \(P\) of mass 0.4 kg is attached to two identical strings, each of natural length 0.5 m and modulus 10 N. The other ends are fixed to points \(A\) and \(B\), 2 m apart on a smooth horizontal table. \(P\) is held at 0.7 m from \(B\) on the line \(AB\) and released from rest. Find its speed when it passes the midpoint of \(AB\).
At the start \(AP = 1.3\) m and \(PB = 0.7\) m, so the extensions are 0.8 m and 0.2 m:
For each string \(\dfrac{\lambda}{2l} = \dfrac{10}{1} = 10\), so the energy is \(10x^2\) for an extension \(x\).
\[\begin{aligned}
E_{\text{start}} &= 10 \times 0.64 + 10 \times 0.04 = 6.8\ \mathrm{J} \\
E_{\text{mid}} &= 10 \times 0.5^2 + 10 \times 0.5^2 = 5\ \mathrm{J}
\end{aligned}\]
At the midpoint each string is 1 m long, so each extension is 0.5 m. Energy conservation:
\[6.8 = 5 + \tfrac12 \times 0.4\,v^2 \quad\Rightarrow\quad 0.2v^2 = 1.8 \quad\Rightarrow\quad v = 3\ \mathrm{m\,s^{-1}}\]
:::

### Hanging vertically

When a particle falls on a string, the string is slack for the first part of the fall, and the particle falls freely. The fall below the start is \(l + x\), the natural length plus the extension, so that is the height to use for GPE. Missing the natural length is the standard slip.

:::eg A particle of mass 0.5 kg is attached to one end of a light elastic string of natural length 1 m and modulus 20 N. The other end is attached to a fixed point \(O\). The particle is released from rest at \(O\). Find (a) the greatest extension of the string, (b) the greatest speed of the particle. Take \(g = 10\).
(a) At the lowest point the particle is momentarily at rest, so all of its lost GPE is stored as EPE. It has fallen \(1 + x\) below \(O\):
\[\begin{aligned}
0.5 \times 10 \times (1 + x) &= \frac{20x^2}{2 \times 1} \\
5 + 5x &= 10x^2 \\
2x^2 - x - 1 &= 0 \\
(2x + 1)(x - 1) &= 0
\end{aligned}\]
The extension is positive, so \(x = 1\) m. Reject \(x = -\tfrac12\).

(b) The speed is greatest when the acceleration is zero, where the tension equals the weight:
\[5 = \frac{20x}{1} \quad\Rightarrow\quad x = 0.25\ \mathrm{m}\]
Energy from \(O\) to this point (fallen 1.25 m):
\[\begin{aligned}
\tfrac12 \times 0.5\,v^2 &= 5 \times 1.25 - \frac{20 \times 0.25^2}{2} \\
&= 6.25 - 0.625 = 5.625
\end{aligned}\]
So \(v^2 = 22.5\) and \(v = 4.74\) m s⁻¹.
:::

### Maximum speed: where the acceleration is zero

A particle on a string speeds up while the pull towards the equilibrium position is still ahead of it, and slows down once it has passed that position. So its speed is greatest **at the equilibrium position**, where the resultant force is zero. That position comes from a force balance, never from "the middle". Then an energy equation from the start gives the speed. This is the standard "greatest speed" question.

:::steps
1. Resultant force zero: write the balance (tension against weight component, with friction if any) and find the extension \(x_e\).
2. Energy equation from the start to that position, with that extension.
3. Solve for \(v\).
:::

:::eg (Exam style) A light elastic string has natural length 0.5 m and modulus of elasticity 12 N. One end is attached to a fixed point \(O\) at the top of a smooth plane inclined at \(\alpha\) to the horizontal, where \(\sin\alpha = 0.6\). The other end is attached to a particle \(P\) of mass 0.8 kg. \(P\) is released from rest at the point of the plane where the string is just taut. Take \(g = 10\). (a) Find the extension of the string when \(P\) is in equilibrium. (b) Show that the greatest speed of \(P\) is 1.10 m s⁻¹, to 3 s.f. (c) Find the greatest extension of the string.
**(a)** The weight component down the plane is \(0.8 \times 10 \times 0.6 = 4.8\) N. In equilibrium the tension balances it:
\[\frac{12x}{0.5} = 4.8\] [M1]
\[x = 0.2\ \mathrm{m}\] [A1]
**(b)** The speed is greatest where the resultant force is zero, at extension 0.2 m (the answer to (a)). [B1] \(P\) has moved \(0.5 + 0.2 = 0.7\) m down the plane. Energy:
\[\tfrac12 \times 0.8\,v^2 = 4.8 \times 0.2 - \frac{12 \times 0.2^2}{2 \times 0.5}\] [M1 A1]
The start is already at the natural length, so \(P\) has moved only 0.2 m down the plane, losing GPE of \(4.8 \times 0.2\). So
\[0.4v^2 = 0.96 - 0.48 = 0.48 \quad\Rightarrow\quad v = 1.0954\ldots\] [A1]
The greatest speed is 1.10 m s⁻¹ (3 s.f.).

**(c)** At the greatest extension \(v = 0\):
\[\begin{aligned}
4.8x &= \frac{12x^2}{2 \times 0.5} \\
4.8x &= 12x^2
\end{aligned}\] [M1 A1]
\(x = 0.4\) m (reject \(x = 0\), the start). [A1]
:::

:::warn Where does the motion start?
In the example above \(P\) starts at the position where the string is just taut, so the drop *to* the position of extension \(x\) is just \(x\) along the plane. If \(P\) starts further up, the string is slack for a while, and the drop is \(l + x\) (as in the vertical example) plus any slack distance. Draw a line showing the start, the natural-length point and the end, and mark the distances.
:::

### Springs on both sides of equilibrium

A spring fixed at its lower end behaves the same way, except that compression is allowed. The particle can pass through the natural length position and stretch the spring on the other side.

:::eg (Exam style) A light spring has natural length 0.5 m and modulus of elasticity 30 N. Its lower end is fixed to a horizontal floor, and a particle \(P\) of mass 0.6 kg is attached to its upper end. Take \(g = 10\). (a) Show that \(P\) is in equilibrium when the spring is compressed by 0.1 m. (b) \(P\) is pressed down until the length of the spring is 0.2 m, then released from rest. Show that \(P\) has speed \(\sqrt3\) m s⁻¹ when the spring has its natural length. (c) Find the greatest speed of \(P\). (d) Find the greatest length of the spring during the motion.
**(a)** The thrust balances the weight:
\[\frac{30x}{0.5} = 0.6 \times 10\] [M1]
\[x = 0.1\ \mathrm{m}\] [A1]
**(b)** At the start the compression is 0.3 m, and \(P\) rises 0.3 m to reach the natural length:
\[\frac{30 \times 0.3^2}{2 \times 0.5} = \tfrac12 \times 0.6\,v^2 + 0.6 \times 10 \times 0.3\] [M1 A1]
\[2.7 = 0.3v^2 + 1.8 \quad\Rightarrow\quad v^2 = 3\] [A1]
So \(v = \sqrt3\) m s⁻¹.

**(c)** The speed is greatest where the acceleration is zero: compression 0.1 m, from (a). [B1] \(P\) has risen 0.2 m from the start:
\[\frac{30 \times 0.3^2}{2 \times 0.5} = \tfrac12 \times 0.6\,v^2 + 6 \times 0.2 + \frac{30 \times 0.1^2}{2 \times 0.5}\] [M1 A1]
\[2.7 = 0.3v^2 + 1.2 + 0.3 \quad\Rightarrow\quad v = 2\ \mathrm{m\,s^{-1}}\] [A1]
**(d)** At the highest point \(v = 0\) and the spring is stretched by \(e\). \(P\) has risen \(0.3 + e\):
\[2.7 = 6(0.3 + e) + \frac{30e^2}{2 \times 0.5}\] [M1 A1]
\[\begin{aligned}
30e^2 + 6e - 0.9 &= 0 \\
100e^2 + 20e - 3 &= 0 \\
(10e - 1)(10e + 3) &= 0
\end{aligned}\]
\(e = 0.1\) (the other root is negative). [A1]
The greatest length is \(0.5 + 0.1 = 0.6\) m. [A1]
:::

The motion in part (d) is symmetrical about the equilibrium position. The lowest point is 0.2 m below it (compression 0.3 m instead of 0.1 m) and the highest point is 0.2 m above it (extension 0.1 m, which is 0.2 m above the compression of 0.1 m). The symmetry holds for any spring that stays attached, because the resultant force is proportional to the distance from the equilibrium position. It is a good check on your answer.

### With friction

:::eg (Exam style) A particle \(P\) of mass 2 kg lies on a rough horizontal table, with coefficient of friction 0.3. It is attached to one end of a light elastic string of natural length 1 m and modulus 40 N. The other end is fixed to a point \(O\) on the table. \(P\) is held 1.5 m from \(O\) and released from rest. Take \(g = 10\). (a) Find the speed of \(P\) when the string becomes slack. (b) Find how far from \(O\) the particle comes to rest.
**(a)** The friction force is \(0.3 \times 2 \times 10 = 6\) N. The extension at the start is 0.5 m. [B1] \(P\) moves 0.5 m to the natural length:
\[\frac{40 \times 0.5^2}{2 \times 1} = \tfrac12 \times 2 \times v^2 + 6 \times 0.5\] [M1 A1]
\[5 = v^2 + 3 \quad\Rightarrow\quad v = \sqrt2 = 1.41\ \mathrm{m\,s^{-1}}\] [A1]
**(b)** After the string goes slack, only friction acts. The kinetic energy at that point is \(\tfrac12 \times 2 \times 2 = 2\) J, which is used up over a distance \(d\):
\[6d = 2 \quad\Rightarrow\quad d = \tfrac13\ \mathrm{m}\] [M1 A1]
\(P\) comes to rest \(1 - \tfrac13 = \tfrac23 = 0.667\) m from \(O\). [A1]
:::

## Strings that slacken, and a note on pitfalls

An elastic string is only a force while it is stretched. Whenever a particle on a string moves closer to the fixed end than \(l\), the string is slack, the tension is zero and the EPE is zero. So in any "greatest" or "least" problem, check what happens at the end of your answer: is the extension positive? Is the string taut at the moment of the equation? A negative extension in a string problem means the equation was written for a slack string.

:::warn Three slips to avoid
- **Using the length for \(x\).** Subtract the natural length first, in every use of \(T = \dfrac{\lambda x}{l}\) and \(E = \dfrac{\lambda x^2}{2l}\).
- **Counting EPE when the string is slack.** If the length is below \(l\), EPE is 0, not \(\dfrac{\lambda x^2}{2l}\) with a negative \(x\).
- **Forgetting the natural length in the drop.** A particle that falls on a string falls \(l + x\), not \(x\), when it starts from the fixed end.
:::

:::exam Presenting energy equations
Write the energy equation as words or with labelled terms before substituting numbers, and show each term separately (KE, GPE, EPE, work against friction). Method marks are given for a correct set of terms; one wrong term loses the accuracy mark and the answer. Keep \(g = 10\) in your working; the 9231 paper's front page says to use 10 m s⁻².
:::

## Elastic strings in circular motion

A string need not be horizontal or vertical. If a particle on an elastic string moves in a horizontal circle (a **conical pendulum**), the tension has a vertical component that holds the particle up and a horizontal component that provides the force towards the centre, and the length of the string is not known in advance: it comes from Hooke's law. That is in [Circular motion: horizontal circles](#math.fm.circular), which uses everything in this chapter.

:::board
Edexcel IAL and the UK A Levels use \(g = 9.8\) where 9231 uses \(g = 10\). Hooke's law \(T = \dfrac{\lambda x}{l}\) and elastic energy \(\dfrac{\lambda x^2}{2l}\) are the same; the notation \(\lambda\) for the modulus is the same in the UK Further Maths specifications.
:::

:::eg Spot the error: a particle of mass 0.5 kg is attached to a light elastic string of natural length 1 m and modulus 20 N. The other end is fixed at \(O\), and the particle is released from rest at \(O\). Find the greatest extension of the string. Take \(g = 10\). [4 marks]
A student wrote this answer.

Line 1: At the lowest point all the lost GPE is stored as EPE.
Line 2: \(0.5 \times 10 \times x = \dfrac{20x^2}{2 \times 1}\)
Line 3: \(5x = 10x^2\), so \(x = 0.5\) m.

Line 1 is correct, and line 2 has the right terms (GPE lost on the left, EPE on the right), so the method mark is earned. [M1]

**The slip is in the height on line 2.** The particle falls \(1 + x\), the natural length plus the extension, not \(x\). The equation is therefore not correct. [A0]

Line 3 solves the student's own equation properly, so a method mark for solving is earned, which depends on the first M1. [DM1] The answer 0.5 is wrong. [A0] The student scores 2 out of 4.

Correct: \(5(1 + x) = 10x^2\) [A1], which gives \(2x^2 - x - 1 = 0\) and \(x = 1\) m [A1].

**Check** with the force at the bottom: the tension is \(\dfrac{20 \times 1}{1} = 20\) N, four times the weight of 5 N, and a particle that is at rest there is accelerating upwards, as it should.
:::

:::try Start easy, finish at exam standard
Q: A string of natural length 0.4 m and modulus 30 N is stretched to a length of 0.7 m. Find the tension and the energy stored.
A: \(x = 0.3\) m. \(T = \dfrac{30 \times 0.3}{0.4} = 22.5\) N. \(E = \dfrac{30 \times 0.3^2}{2 \times 0.4} = 3.375\) J. (Check: \(\tfrac12 Tx = \tfrac12 \times 22.5 \times 0.3 = 3.375\).)
Q: A string has modulus 36 N. A tension of 9 N stretches it by 0.25 m. Find its natural length.
A: \(9 = \dfrac{36 \times 0.25}{l}\), so \(l = \dfrac{9}{9} = 1\) m.
Q: A light spring of natural length 0.8 m and modulus 32 N is compressed to a length of 0.6 m. Find the thrust and the elastic energy.
A: \(x = 0.2\) m. Thrust \(= \dfrac{32 \times 0.2}{0.8} = 8\) N. \(E = \dfrac{32 \times 0.04}{1.6} = 0.8\) J.
Q: A particle of mass 1.5 kg hangs at rest from a light elastic string of natural length 0.9 m and modulus 45 N. Find the length of the string. Take \(g = 10\).
A: \(T = 15\) N, so \(x = \dfrac{15 \times 0.9}{45} = 0.3\) m and the length is 1.2 m.
Q: A string of natural length 2 m and modulus 50 N carries a tension of 5 N. Find the extension and the elastic energy stored.
A: \(x = \dfrac{5 \times 2}{50} = 0.2\) m. The energy stored is \(\dfrac{50 \times 0.04}{4} = 0.5\) J, which is \(\tfrac12 \times 5 \times 0.2\).
Q: A string of natural length 0.6 m and modulus 18 N is stretched from a length of 0.8 m to a length of 1.0 m. Find the work done.
A: Extensions 0.2 m and 0.4 m. \(E = \dfrac{18}{1.2}x^2 = 15x^2\), so the work is \(15(0.16 - 0.04) = 1.8\) J.
Q: A particle of mass 0.3 kg lies on a smooth horizontal table and is attached to a fixed point \(O\) on the table by a string of natural length 0.4 m and modulus 6 N. It is released from rest 0.6 m from \(O\). Find its speed when the string becomes slack.
A: \(x = 0.2\) m, so \(E = \dfrac{6 \times 0.04}{0.8} = 0.3\) J. Then \(\tfrac12 \times 0.3\,v^2 = 0.3\), so \(v^2 = 2\) and \(v = 1.41\) m s⁻¹.
Q: A particle of mass 0.3 kg hangs in equilibrium from a fixed point by a light spring of natural length 0.6 m and modulus 15 N. Find the extension.
A: \(T = mg = 3\) N, so \(x = \dfrac{3 \times 0.6}{15} = 0.12\) m.
Q: A particle \(P\) lies on a smooth horizontal table between two points \(A\) and \(B\), 1.6 m apart, joined to each by an identical string of natural length 0.5 m and modulus 15 N. Find the tension when \(P\) is at the midpoint.
A: Each string has length 0.8 m, so \(x = 0.3\) m and \(T = \dfrac{15 \times 0.3}{0.5} = 9\) N. The two tensions balance.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] (#math.m.energy) ★ A light elastic string has natural length 0.75 m and modulus 30 N. Find the tension when the length of the string is 0.9 m, and the elastic energy stored in the string at that length.
A: Extension \(= 0.9 - 0.75 = 0.15\) m. \(T = \dfrac{30 \times 0.15}{0.75}\) [M1] \(= 6\) N. [A1]
\(E = \dfrac{30 \times 0.15^2}{2 \times 0.75}\) [M1] \(= 0.45\) J. [A1]
Q: [3 marks] ★ A particle of mass 0.3 kg hangs in equilibrium from a light spring with natural length 0.4 m, and the length of the spring is 0.46 m. Find the modulus of elasticity. Take \(g = 10\).
A: Tension equals weight: \(T = 3\) N. [B1] \(3 = \dfrac{\lambda \times 0.06}{0.4}\) [M1], so \(\lambda = 20\) N. [A1]
Q: [5 marks] ★★ A particle \(P\) lies on a smooth horizontal table. It is attached to two light elastic strings, one to each of two points \(A\) and \(B\) on the table, 1.8 m apart. String \(AP\) has natural length 0.4 m and modulus 8 N. String \(PB\) has natural length 0.6 m and modulus 18 N. \(P\) rests in equilibrium on \(AB\). Find the tension in the strings and the length \(AP\).
A: Let the extensions be \(x\) and \(y\). The tensions are equal: \(\dfrac{8x}{0.4} = \dfrac{18y}{0.6}\), so \(20x = 30y\). [M1] [A1]
The lengths: \((0.4 + x) + (0.6 + y) = 1.8\), so \(x + y = 0.8\). [M1]
Then \(x = 0.48\) and \(y = 0.32\). [A1]
\(T = 20 \times 0.48 = 9.6\) N and \(AP = 0.88\) m. [A1]
Q: [6 marks] ★★ A particle \(P\) of mass 1.5 kg lies on a rough horizontal surface. The coefficient of friction is 0.2. \(P\) is attached to one end of a light elastic string of natural length 0.6 m and modulus 15 N, the other end of which is fixed to a point \(O\) of the surface. The particle is pulled to a point where the string is 1.0 m long and released from rest. Find the speed of \(P\) when the string becomes slack. Take \(g = 10\).
A: Extension 0.4 m. EPE \(= \dfrac{15 \times 0.4^2}{2 \times 0.6} = 2\) J. [B1]
Friction \(= 0.2 \times 15 = 3\) N, [B1] and the work done against it is \(3 \times 0.4 = 1.2\) J. [M1]
\[2 = \tfrac12 \times 1.5\,v^2 + 1.2\] [M1 A1]
\(v^2 = \dfrac{0.8}{0.75} = 1.0667\), so \(v = 1.03\) m s⁻¹. [A1]
Q: [6 marks] ★★ A light elastic string has natural length 0.9 m and modulus 18 N. One end is fixed at \(O\) at the top of a smooth plane inclined at \(\beta\) to the horizontal, where \(\sin\beta = 0.8\). The other end is attached to a particle of mass 0.45 kg, which is released from rest at the point on the plane where the string is just taut. Find the extension at which the speed is greatest, and show that this greatest speed is 1.2 m s⁻¹. Take \(g = 10\).
A: Weight component: \(0.45 \times 10 \times 0.8 = 3.6\) N. The speed is greatest when the resultant force is zero. [B1]
\(\dfrac{18x}{0.9} = 3.6\) [M1], so \(x = 0.18\) m. [A1]
\[\tfrac12 \times 0.45\,v^2 = 3.6 \times 0.18 - \frac{18 \times 0.18^2}{2 \times 0.9}\] [M1 A1]
\(0.225v^2 = 0.648 - 0.324 = 0.324\), so \(v^2 = 1.44\) and \(v = 1.2\) m s⁻¹. [A1]
Q: [9 marks] ★★★ A particle \(P\) of mass 0.5 kg hangs in equilibrium from a fixed point \(O\) on a light elastic string of natural length 0.8 m and modulus 20 N. (a) Find the extension of the string. (b) \(P\) is pulled down a further 0.5 m from the equilibrium position and released from rest. Find the speed of \(P\) when the string becomes slack. (c) Find the greatest height above the point where the string became slack that \(P\) reaches. Take \(g = 10\).
H: The equilibrium position is where the tension equals the weight, 5 N.
H: At the start the extension is the answer to (a) plus 0.5 m.
H: After the string is slack, \(P\) moves under gravity alone: use \(v^2 = 2gh\) upwards.
A: (a) The tension equals the weight, 5 N. [B1] \(5 = \dfrac{20x}{0.8}\) [M1], so \(x = 0.2\) m. [A1]
(b) At the start the extension is 0.7 m. [B1] \(P\) rises 0.7 m to the natural length:
\[\frac{20 \times 0.7^2}{2 \times 0.8} = \tfrac12 \times 0.5\,v^2 + 5 \times 0.7\] [M1 A1]
\(6.125 = 0.25v^2 + 3.5\), so \(v^2 = 10.5\) and \(v = 3.24\) m s⁻¹. [A1]
(c) After the string goes slack, \(P\) is a projectile moving upwards: \(0 = 10.5 - 2 \times 10h\) [M1], so \(h = 0.525\) m. [A1]
Q: [9 marks] (#math.m.newton) ★★★ A particle \(P\) of mass 1 kg lies on a rough plane inclined at \(\alpha\) to the horizontal, where \(\sin\alpha = 0.6\). The coefficient of friction is 0.2. \(P\) is attached to a light elastic string of natural length 0.5 m and modulus 20 N, whose other end is fixed to a point \(O\) on the plane above \(P\) on a line of greatest slope. Take \(g = 10\). (a) Show that \(P\) can rest in equilibrium with the extension of the string anywhere from 0.11 m to 0.19 m. (b) \(P\) is released from rest at the point where the string is just taut. Show that it comes to rest after moving 0.22 m down the slope and that it then moves up the slope.
H: Normal reaction \(= mg\cos\alpha\) with \(\cos\alpha = 0.8\). Friction \(\le 0.2R\).
H: For (a), the least tension is when friction helps hold \(P\) from sliding down.
H: For (b), work done against friction is \(F \times\) distance; at the stopping point compare the tension with the upper limit from (a).
A: (a) \(R = 8\) N, so \(F_{\max} = 1.6\) N. [B1] The weight component is 6 N. [B1]
Least tension: \(T = 6 - 1.6 = 4.4\) N. Greatest: \(T = 6 + 1.6 = 7.6\) N. [M1]
\(x = \dfrac{Tl}{\lambda} = \dfrac{T}{40}\), so \(0.11 \le x \le 0.19\). [A1]
(b) Energy from rest at natural length to extension \(x\) (distance down the slope \(= x\)):
\[6x = \frac{20x^2}{2 \times 0.5} + 1.6x\] [M1 A1]
\(4.4x = 20x^2\), so \(x = 0.22\) m (not 0). [A1]
At \(x = 0.22\) the tension is \(40 \times 0.22 = 8.8\) N, which is more than the greatest value 7.6 N, [M1] so friction cannot hold \(P\) and it moves up the slope. [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A bungee cord has natural length 20 m. A jumper of mass 60 kg steps off a platform that is 45 m above the water, with the other end of the cord fixed to the platform. Model the jumper as a particle and the cord as a light elastic string, and take \(g = 10\). The jumper must stop at least 5 m above the water. (a) Find the least modulus of elasticity of the cord. (b) Find the greatest acceleration of the jumper when the modulus has this value.
H: The lowest point is at most \(45 - 5 = 40\) m below the platform, so the greatest extension allowed is \(40 - 20 = 20\) m.
H: A stiffer cord extends less, so "least modulus" comes from the greatest extension.
H: The acceleration is greatest at the lowest point, where the tension is greatest. Find the resultant force there.
A: (a) The fall to the lowest point is \(20 + x\) with \(x \le 20\). Energy, with the jumper at rest at both ends: [M1]
\[60 \times 10 \times (20 + x) = \frac{\lambda x^2}{2 \times 20}\] [M1 A1]
With \(x = 20\): \(600 \times 40 = 24\,000 = \dfrac{400\lambda}{40} = 10\lambda\), so \(\lambda = 2400\) N. [A1]
(b) At the lowest point \(T = \dfrac{2400 \times 20}{20} = 2400\) N. [M1] Resultant upward force \(= 2400 - 600 = 1800\) N, so \(a = \dfrac{1800}{60} = 30\) m s⁻², which is \(3g\). [A1]
Q: [6 marks] ★★★ Two light elastic strings are joined end to end to make one longer string. The first has natural length \(l_1\) and modulus \(\lambda_1\); the second has natural length \(l_2\) and modulus \(\lambda_2\). The combined string is pulled with tension \(T\) at its ends. (a) Show that the joined string behaves like one string of natural length \(l = l_1 + l_2\) whose modulus \(\lambda\) satisfies \(\dfrac{l}{\lambda} = \dfrac{l_1}{\lambda_1} + \dfrac{l_2}{\lambda_2}\). (b) Find \(\lambda\) when \(l_1 = 0.6\) m, \(\lambda_1 = 30\) N, \(l_2 = 0.4\) m and \(\lambda_2 = 20\) N.
H: The tension is the same in both strings. Find each extension in terms of \(T\).
H: The total extension is the sum of the two; compare it with \(\dfrac{Tl}{\lambda}\).
A: (a) The tension is \(T\) in both strings (the joint is light). [B1] Their extensions are \(x_1 = \dfrac{Tl_1}{\lambda_1}\) and \(x_2 = \dfrac{Tl_2}{\lambda_2}\). [M1]
The total extension is \(x = T\left(\dfrac{l_1}{\lambda_1} + \dfrac{l_2}{\lambda_2}\right)\). [M1] For one string, \(x = \dfrac{Tl}{\lambda}\), so \(\dfrac{l}{\lambda} = \dfrac{l_1}{\lambda_1} + \dfrac{l_2}{\lambda_2}\). [A1]
(b) \(l = 1.0\) and \(\dfrac{l}{\lambda} = 0.02 + 0.02 = 0.04\). [M1] So \(\lambda = \dfrac{1.0}{0.04} = 25\) N. [A1]
:::

:::quiz
? A string of natural length 2 m and modulus 40 N is stretched to a length of 2.5 m. What is the tension?
+ \(10\) N
- \(50\) N
- \(8\) N
- \(20\) N
> The extension is 0.5 m, so \(T = \dfrac{40 \times 0.5}{2} = 10\) N. The answer 50 N puts the stretched length 2.5 m in place of the extension, and 20 N forgets to divide by the natural length.
? Doubling the extension of a string multiplies the stored elastic energy by what?
+ \(4\)
- \(2\)
- \(8\)
- \(\tfrac12\)
> \(E = \dfrac{\lambda x^2}{2l}\) depends on \(x^2\), so the energy is multiplied by \(2^2 = 4\). The answer 2 is the factor for the tension, not the energy.
? A particle on a smooth horizontal table is attached to a string and pulled back, then released. The string goes slack at its natural length. Which statement is correct after that?
+ The particle moves at constant speed, because there is no horizontal force on it
- The particle slows down, because the string is still pulling it back
- The particle stops at once, because the elastic energy is zero
- The speed keeps increasing until the string is fully slack again
> A slack string exerts no force, and the table is smooth, so there is no resultant force and the speed stays constant. Elastic energy being zero does not mean the particle has stopped: the energy has become kinetic.
? A particle falls from the fixed end \(O\) of a vertical string of natural length \(l\). At the lowest point the extension is \(x\). The loss of GPE is
- \(mgx\)
+ \(mg(l + x)\)
- \(mgl\)
- \(\dfrac{mg(l + x)}{2}\)
> The particle drops through the natural length and then through the extension, so \(mg(l + x)\). Using \(mgx\) is the standard slip.
? A particle on a string on a smooth slope is released from rest at the natural length position and slides down. Where is its speed greatest?
- Where the string is longest
+ Where the tension equals the component of the weight down the slope
- Where the string is at its natural length
- At the lowest point of the motion
> The speed is greatest when the resultant force along the slope is zero, which is when \(T = mg\sin\alpha\). At the lowest point the particle is at rest for an instant, and at the natural length the tension is zero while the weight component still accelerates the particle down the slope.
? A light spring of natural length 0.5 m and modulus 20 N is compressed to a length of 0.3 m. The force it exerts is
+ A thrust of \(8\) N
- A tension of \(8\) N
- Zero, because the spring is shorter than its natural length
- A thrust of \(12\) N
> A spring pushes when compressed: \(x = 0.2\) and \(\dfrac{20 \times 0.2}{0.5} = 8\) N, a thrust. Only a string (not a spring) goes slack when shorter than \(l\).
:::

:::checklist What you can now do
- [ ] I can use Hooke's law \(T = \dfrac{\lambda x}{l}\) with the extension (not the length), and explain the modulus of elasticity.
- [ ] I can say when a string is slack and when a spring exerts a thrust.
- [ ] I can find equilibrium positions for a particle held by one or two strings or springs, including on a rough slope.
- [ ] I can use the elastic potential energy \(\dfrac{\lambda x^2}{2l}\) and know it comes from the area under the force against extension graph.
- [ ] I can write an energy equation with KE, GPE, EPE and work against friction for a particle on a string or spring.
- [ ] I can find the greatest extension (speed zero) and the greatest speed (resultant force zero) of a particle on a string or spring.
- [ ] I can handle a particle that moves from a taut to a slack string and on to a different kind of motion.
:::

:::recap
- Hooke's law: \(T = \dfrac{\lambda x}{l}\), with \(x\) the extension (length minus natural length). \(\lambda\) is in newtons.
- A string only pulls (zero when slack); a spring pushes when compressed, with the same formula.
- Elastic energy: \(E = \dfrac{\lambda x^2}{2l}\) (MF19), the area under the \(T\)–\(x\) graph; \(E = \tfrac12 Tx\).
- Two strings on a smooth table: the tensions are equal and the lengths add to the distance between the fixed points.
- Energy equation: KE + GPE + EPE at the start = the same at the end + work against friction.
- A particle falling on a string from the fixed end drops \(l + x\).
- Greatest extension: speed 0. Greatest speed: resultant force 0 (find the extension from the force balance, then use energy).
- On a rough slope the tension and the extension have a range between "about to slide down" and "about to slide up".
:::

:::links
- explore: [Masses and springs](https://phet.colorado.edu/en/simulations/masses-and-springs) · PhET · hang masses on springs, change the stiffness and watch the extension and energy
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · graded questions with answers on elastic strings and springs
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Paper 3 questions with mark schemes [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers sorted by year

Links checked 20 November 2026.
:::
Next: [Circular motion: horizontal circles](#math.fm.circular) uses angular speed and the force towards the centre to analyse a particle on a string or a disc moving in a horizontal circle, including strings that stretch.
