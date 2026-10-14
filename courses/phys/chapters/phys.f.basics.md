@chapter phys.f.basics
@title Physics from zero
@level pre
@time 4–6 hours
@summary The maths and the school physics the rest of the course assumes: standard form and significant figures, rearranging formulae, straight-line graphs, right-angled triangles, areas and volumes, then one short section each on motion, forces, energy, pressure, circuits, waves and atoms.

:::why
Physics is the subject that explains how the world works using numbers, so every topic in this course needs a small toolkit of maths and a base of school physics. If you have not met these ideas, or met them long ago, this chapter gives you everything in one place, with many short examples. If you already know them, use the quizzes to check, and move on to [Physical quantities, units and uncertainty](#phys.units).
:::

**Before you start**, you need only ordinary arithmetic: adding, multiplying, fractions and percentages. If those feel shaky, work through [Numbers, fractions and percentages](#math.f.numbers) first. The maths topics below each link to a longer chapter in the maths course.

:::try Warm-up
Q: Write 0.00042 in standard form. (from [Indices, surds and standard form](#math.f.powers))
A: \(4.2 \times 10^{-4}\). Move the decimal point four places to the right to get 4.2, so the power of ten is \(-4\).
Q: What is 12% of 250? (from [Numbers, fractions and percentages](#math.f.numbers))
A: \(0.12 \times 250 = 30\).
Q: Solve \(3x + 5 = 20\). (from [Algebra from scratch](#math.f.algebra))
A: Subtract 5 from both sides: \(3x = 15\). Divide by 3: \(x = 5\).
:::

## Numbers in physics

### Standard form

Physics uses numbers from the very small (the charge of an electron) to the very large (the distance to a star). Writing all the zeros is slow and easy to get wrong, so we use **standard form**: a number between 1 and 10, multiplied by a power of ten.

:::key Standard form
\[a \times 10^{n} \qquad\text{with } 1 \le a < 10 \text{ and } n \text{ a whole number}\]
A large number has a positive \(n\) (move the decimal point to the left to get \(a\)). A number smaller than 1 has a negative \(n\) (move the point to the right).
:::

:::eg Write 45 600 000, 0.0000072 and 602 000 000 000 000 000 000 000 in standard form.
45 600 000: move the point 7 places left to get 4.56, so \(4.56 \times 10^{7}\).

0.0000072: move the point 6 places right to get 7.2, so \(7.2 \times 10^{-6}\).

The last number is the Avogadro constant. Its first digit, 6, is followed by 23 more digits, so the point moves 23 places left to give \(6.02 \times 10^{23}\).
:::

Two values you will use all through the course are the speed of light, \(c = 3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\), and the charge of one proton, \(e = 1.60 \times 10^{-19}\,\mathrm{C}\). To multiply standard-form numbers, multiply the front numbers and add the powers: \((3.00 \times 10^{8}) \times (2.0 \times 10^{-3}) = 6.0 \times 10^{5}\). Your calculator has an EXP or \(\times 10^{x}\) key for this: press it instead of typing \(\times 10\) and a power, or the answer will be wrong. The full rules for powers are in [Indices, surds and standard form](#math.f.powers).

### Significant figures

A measurement is never exact, so the number of digits you write shows how precise it is. **Significant figures** (s.f.) are the digits that carry meaning, counted from the first non-zero digit. So 0.004 56 has 3 s.f., and 25 340 rounded to 3 s.f. is 25 300 (written \(2.53 \times 10^{4}\)). A zero at the end after a decimal point counts: 2.50 has 3 s.f., 2.5 has 2 s.f.

:::key Significant figures in answers
- When you multiply or divide, give the answer to the same number of s.f. as the **least precise** value you used.
- Carry the full calculator value through every step and round **only at the end**.
- Never give fewer than 2 s.f. in a final answer, and always give the unit.
:::

:::eg A car travels 250 m in 12 s. Find its average speed.
\[v = \frac{s}{t} = \frac{250}{12} = 20.8333\ldots\,\mathrm{m\,s^{-1}}\]
The time has 2 s.f., so the answer has 2 s.f.: \(21\,\mathrm{m\,s^{-1}}\).
:::

### Units and prefixes

Every physical quantity is a number **and** a unit. "The rod is 5" means nothing: 5 mm, 5 m and 5 km are very different rods. The scientific system of units is the SI. Its base units for the quantities in this course are the metre (m) for length, the kilogram (kg) for mass, the second (s) for time, the ampere (A) for current, the kelvin (K) for temperature and the mole (mol) for amount of substance. All other SI units are built from these: the newton is \(\mathrm{kg\,m\,s^{-2}}\), for example. [Physical quantities, units and uncertainty](#phys.units) develops this fully.

A **prefix** multiplies a unit by a power of ten, so you do not have to write the power.

| Prefix | Symbol | Multiplies by | Example |
|---|---|---|---|
| giga | G | \(10^{9}\) | 2.4 GHz = \(2.4 \times 10^{9}\) Hz |
| mega | M | \(10^{6}\) | 5.0 MW = \(5.0 \times 10^{6}\) W |
| kilo | k | \(10^{3}\) | 4.7 kΩ = \(4.7 \times 10^{3}\) Ω |
| milli | m | \(10^{-3}\) | 350 mA = 0.350 A |
| micro | μ | \(10^{-6}\) | 25 μm = \(2.5 \times 10^{-5}\) m |
| nano | n | \(10^{-9}\) | 650 nm = \(6.50 \times 10^{-7}\) m |
| pico | p | \(10^{-12}\) | 12 pF = \(1.2 \times 10^{-11}\) F |

:::warn Squared and cubed units
A prefix is part of the unit, so it is squared or cubed with it. \(1\,\mathrm{cm} = 10^{-2}\,\mathrm{m}\), so \(1\,\mathrm{cm^2} = (10^{-2})^2\,\mathrm{m^2} = 10^{-4}\,\mathrm{m^2}\) and \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\). Converting 25 cm² into m² gives \(25 \times 10^{-4} = 2.5 \times 10^{-3}\,\mathrm{m^2}\), not \(25 \times 10^{-2}\). Also, 1 litre is \(10^{-3}\,\mathrm{m^3}\), and 1 hour is 3600 s.
:::

Change to base units (m, kg, s, A) **before** you substitute into a formula. Then the answer comes out in base units too, and you never have to guess a unit.

## Rearranging formulae

A formula is a rule linking quantities, and you will often need it the other way round. Rearranging, or **changing the subject**, is the same skill as solving an equation: whatever you do to one side you must do to the other.

:::key Method for rearranging
1. Write the formula and underline the quantity you want.
2. Move the other terms away from it one at a time, **undoing the operations in the reverse order** to the one that built the formula (undo adding or subtracting first, then multiplying or dividing, then powers or roots).
3. Do exactly the same to both sides each time.
4. Substitute numbers last, in base units, and check the unit of your answer.
:::

:::eg Five rearrangements, easy to harder. Use the method for each.
**1. \(v = s/t\), find \(t\).** Multiply both sides by \(t\) to get \(vt = s\), then divide by \(v\): \(t = s/v\). A runner at \(6.0\,\mathrm{m\,s^{-1}}\) covers 540 m in \(540/6.0 = 90\,\mathrm{s}\).

**2. \(P = VI\), find \(I\).** Divide both sides by \(V\): \(I = P/V\). A 2.4 kW kettle on a 230 V supply draws \(I = 2400/230 = 10.43\ldots\), so \(10\,\mathrm{A}\) to 2 s.f.

**3. \(\rho = m/V\), find \(V\).** Multiply by \(V\): \(\rho V = m\). Divide by \(\rho\): \(V = m/\rho\). A block of mass 0.54 kg and density \(2700\,\mathrm{kg\,m^{-3}}\) has volume \(0.54/2700 = 2.0 \times 10^{-4}\,\mathrm{m^3}\).

**4. \(E = \tfrac12 mv^2\), find \(v\).** Multiply by 2: \(2E = mv^2\). Divide by \(m\): \(v^2 = 2E/m\). Take the square root: \(v = \sqrt{2E/m}\). A cyclist and bike of mass 80 kg with 1800 J of kinetic energy move at \(v = \sqrt{2 \times 1800/80} = \sqrt{45} = 6.7\,\mathrm{m\,s^{-1}}\).

**5. \(v^2 = u^2 + 2as\), find \(a\).** Subtract \(u^2\): \(v^2 - u^2 = 2as\). Divide by \(2s\): \(a = \dfrac{v^2 - u^2}{2s}\). A car speeds up from \(8.0\,\mathrm{m\,s^{-1}}\) to \(20\,\mathrm{m\,s^{-1}}\) over 120 m, so \(a = \dfrac{20^2 - 8.0^2}{2 \times 120} = \dfrac{336}{240} = 1.4\,\mathrm{m\,s^{-2}}\).
:::

:::tip Check the units
After rearranging, check the units on both sides. For \(v = \sqrt{2E/m}\): the unit of \(E\) is J = \(\mathrm{kg\,m^2\,s^{-2}}\), dividing by kg leaves \(\mathrm{m^2\,s^{-2}}\), and the square root gives \(\mathrm{m\,s^{-1}}\). If the units do not match, the rearrangement is wrong. More algebra practice is in [Algebra from scratch](#math.f.algebra).
:::

## Graphs

Graphs turn a table of numbers into a picture, and physics is full of them. Always plot the quantity you **control** on the \(x\)-axis and the quantity you **measure** on the \(y\)-axis, and label each axis as *quantity / unit*, for example \(t / \mathrm{s}\).

### Straight lines

A straight-line graph has the equation \(y = mx + c\). The **gradient** \(m\) tells you how much \(y\) changes for each 1 unit of \(x\), and the **intercept** \(c\) is the value of \(y\) where the line crosses the \(y\)-axis (where \(x = 0\)).

:::key Gradient
\[m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}\]
Draw the gradient triangle as large as the line allows: use two points on the line that are far apart (more than half of its length), not two points from a table. The gradient has a **unit**: the unit of \(y\) divided by the unit of \(x\).
:::

:::plot A cyclist's distance s from a signpost against time t. The dashed lines mark the sides of the gradient triangle.
--f "4*x+10+0*sqrt(10-x)" --x 0 11.5 --y 0 65 --hline 18 --vline 8 --pt "2,18,(2, 18)@se" --pt "8,42,(8, 42)@nw" --xlabel "t / s" --ylabel "s / m" --label "s = 4.0t + 10"
:::

:::eg Find the gradient and the \(y\)-intercept of the graph above and say what each means.
Take the two points \((2, 18)\) and \((8, 42)\), which are far apart on the line:
\[m = \frac{42 - 18}{8 - 2} = \frac{24}{6} = 4.0\,\mathrm{m\,s^{-1}}\]
The unit is metre divided by second. The gradient of a distance–time graph is the **speed**, so the cyclist rides at \(4.0\,\mathrm{m\,s^{-1}}\). The line crosses the \(y\)-axis at \(s = 10\,\mathrm{m}\): the cyclist was already 10 m from the signpost at \(t = 0\). So \(s = 4.0t + 10\).
:::

### Direct and inverse proportion

Two quantities are in **direct proportion** if doubling one doubles the other. Their graph is a straight line **through the origin**, \(y = kx\), and the gradient \(k\) is the constant of proportionality. Ohm's law for a resistor is the classic example: \(V = IR\), so a graph of \(V\) against \(I\) is a straight line through the origin whose gradient is the resistance.

:::plot Potential difference V across a resistor against current I. The graph is a straight line through the origin, so V is directly proportional to I.
--f "5*x+0*sqrt(1.1-x)" --x 0 1.3 --y 0 8 --pt "0.8,4,(0.80, 4.0)@se" --xlabel "I / A" --ylabel "V / V" --label "V = 5.0 I"
:::

The gradient is \(4.0/0.80 = 5.0\,\mathrm{V\,A^{-1}}\), which is \(5.0\,\Omega\). A straight line that does **not** pass through the origin shows a *linear* relationship but is not direct proportion. The cyclist's graph above is linear, but distance is not proportional to time, because of the 10 m head start.

Two quantities are in **inverse proportion** if doubling one halves the other: \(y = k/x\), or \(y \propto 1/x\). The graph is a curve that falls and never touches either axis. A 12 m journey at speed \(v\) takes \(t = 12/v\): twice the speed, half the time.

:::plot Time t to travel 12 m against speed v. Doubling the speed halves the time, so t is inversely proportional to v.
--f "12/x+0*sqrt(x-1)+0*sqrt(7-x)" --x 0 8 --y 0 14 --pt "2,6,(2, 6)@ne" --pt "4,3,(4, 3)@ne" --xlabel "v / m s⁻¹" --ylabel "t / s"
:::

If a relationship is \(y \propto 1/x\), then a graph of \(y\) against \(1/x\) is a straight line through the origin, and the gradient is the constant \(k\). That trick, plotting a straight line from a curve, is used constantly in practical work. [Graphs and straight lines](#math.f.graphs) has more on drawing and reading graphs.

### Area under a graph

The area between a graph and the \(x\)-axis often means something. On a speed–time graph, **distance travelled = area under the graph**, because speed × time = distance. On the same graph, the gradient is the **acceleration**.

:::plot A bus accelerating from rest. The shaded triangle has area 36 m, the distance travelled in the first 6.0 s.
--f "2*x+0*sqrt(6-x)" --x 0 7 --y 0 16 --shade "0,0,6" --pt "6,12,(6.0, 12)@nw" --xlabel "t / s" --ylabel "v / m s⁻¹"
:::

:::eg A bus accelerates uniformly from rest to \(12\,\mathrm{m\,s^{-1}}\) in 6.0 s (the graph above), then travels at a constant \(12\,\mathrm{m\,s^{-1}}\) for another 10 s. Find its acceleration and the total distance.
Acceleration is the gradient: \(a = \dfrac{12}{6.0} = 2.0\,\mathrm{m\,s^{-2}}\). [C1] [A1]

Distance in the first stage is the area of the triangle: \(\tfrac12 \times 6.0 \times 12 = 36\,\mathrm{m}\). [C1]

Distance in the second stage is a rectangle: \(12 \times 10 = 120\,\mathrm{m}\). Total \(= 36 + 120 = 156\,\mathrm{m}\), or \(1.6 \times 10^{2}\,\mathrm{m}\) to 2 s.f. [A1]
:::

:::warn Reading a graph
- Read the scale on each axis: one small square is rarely one unit.
- A **steeper** line has a **larger** gradient, but only if both graphs use the same scales.
- Do not confuse the *height* of a point with the *gradient* of the line there.
:::

## Right-angled triangles

Forces, velocities and many lengths in physics are at an angle. A right-angled triangle lets you break them into parts you can calculate. The side opposite the right angle is the **hypotenuse**, the longest side. For a chosen angle \(\theta\), the side facing it is the **opposite** and the side next to it (not the hypotenuse) is the **adjacent**.

:::html
<figure class="fig small"><svg viewBox="45 62 285 175" role="img" aria-label="A right-angled triangle with the angle theta at the bottom left. The longest side is labelled hypotenuse, the vertical side opposite and the horizontal side adjacent."><path class="c1 sw2" d="M60 200H240V80Z"/><path class="ln" d="M228 200V188H240"/><path class="ln thin" d="M95 200A35 35 0 0 0 89.1 180.6"/><text class="tl ti" x="104" y="192">θ</text><text class="tl te" x="138" y="122">hypotenuse</text><text class="tl tc" x="150" y="224">adjacent</text><text class="tl" x="250" y="144">opposite</text></svg><figcaption>The three sides of a right-angled triangle, named from the point of view of the angle θ.</figcaption></figure>
:::

:::formula Pythagoras and the three ratios
\[c^2 = a^2 + b^2 \qquad \sin\theta = \frac{\text{opp}}{\text{hyp}} \qquad \cos\theta = \frac{\text{adj}}{\text{hyp}} \qquad \tan\theta = \frac{\text{opp}}{\text{adj}}\]
\(c\) is the hypotenuse, \(a\) and \(b\) the other two sides. The memory aid is **SOH CAH TOA**. Put your calculator in **degree** mode. To find an angle, use the inverse: \(\theta = \sin^{-1}(\text{opp}/\text{hyp})\).
:::

:::eg A ramp is 3.0 m long and rises 0.60 m. Find the angle it makes with the horizontal.
The rise is opposite the angle and the ramp is the hypotenuse, so use sine:
\[\sin\theta = \frac{0.60}{3.0} = 0.20 \quad\Rightarrow\quad \theta = \sin^{-1}(0.20) = 11.5^\circ \approx 12^\circ\]
:::

### Components of a force

A force at an angle does two jobs at once, one along each of two perpendicular directions. Its **components** are the parts of the force in those directions. If a force \(F\) acts at angle \(\theta\) above the horizontal, the horizontal component is the **adjacent** side and the vertical component is the **opposite** side of the triangle.

:::html
<figure class="fig small"><svg viewBox="62 118 296 150" role="img" aria-label="A force of 40 newtons drawn from a point at 30 degrees above the horizontal, with its horizontal component Fx of 35 newtons along the base and its vertical component Fy of 20 newtons upwards on the right."><path class="c1" d="M80 230L253.2 130" marker-end="url(#ah-phys)"/><path class="c2" d="M80 230H253" marker-end="url(#ah2-phys)"/><path class="c2" d="M253 230V132" marker-end="url(#ah2-phys)"/><path class="ln thin" d="M120 230A40 40 0 0 0 114.6 210"/><text class="tl ti" x="133" y="224">θ</text><text class="tl te" x="150" y="168">F = 40 N</text><text class="tl tc" x="166" y="252">Fx = 35 N</text><text class="tl" x="266" y="185">Fy = 20 N</text><circle class="fi" cx="80" cy="230" r="4"/></svg><figcaption>A force of 40 N at θ = 30° above the horizontal. Its components are Fx = F cos θ along the base and Fy = F sin θ upwards. Both components together have the same effect as the force itself.</figcaption></figure>
:::

:::formula Resolving a force
\[F_x = F\cos\theta \qquad F_y = F\sin\theta\]
\(\theta\) is the angle between the force and the **horizontal** direction of \(F_x\). If the angle is given to the other direction, \(\sin\) and \(\cos\) swap. Always draw the triangle and use SOH CAH TOA, rather than remembering which is which.
:::

:::eg A child pulls a sledge with a rope. The tension is 40 N and the rope makes \(30^\circ\) with the horizontal ground. Find the horizontal and vertical components of the force.
Horizontal (adjacent to the angle): \(F_x = 40\cos30^\circ = 34.6\ldots\,\mathrm{N} \approx 35\,\mathrm{N}\). [C1] [A1]

Vertical (opposite the angle): \(F_y = 40\sin30^\circ = 20\,\mathrm{N}\). [A1]

Only the horizontal component pulls the sledge forwards. The vertical component lifts a little of its weight off the ground.
:::

:::eg A weight of 50 N rests on a slope at \(20^\circ\) to the horizontal. Find the component of the weight down the slope.
The angle between the weight (vertical) and the line perpendicular to the slope is also \(20^\circ\), so the component *along* the slope is the opposite side:
\[F = 50\sin20^\circ = 17.1\ldots\,\mathrm{N} \approx 17\,\mathrm{N}\]
:::

:::eg Two forces of 3.0 N and 4.0 N act at right angles. Find the size and direction of their combined force.
By Pythagoras: \(\sqrt{3.0^2 + 4.0^2} = \sqrt{25} = 5.0\,\mathrm{N}\).

The angle to the 3.0 N force is \(\tan^{-1}(4.0/3.0) = 53.1^\circ \approx 53^\circ\).
:::

Adding vectors is covered fully in [Physical quantities, units and uncertainty](#phys.units), with more trigonometry in [Geometry and trigonometry basics](#math.f.geometry).

## Areas and volumes

Many quantities in physics depend on the area or volume of an object: the pressure on a surface, the resistance of a wire, the density of a block. These are the shapes you need.

:::formula Areas and volumes
\[\text{Circle: } A = \pi r^2 = \frac{\pi d^2}{4} \qquad C = 2\pi r\]
\[\text{Sphere: } A = 4\pi r^2 \qquad V = \tfrac43\pi r^3\]
\[\text{Cylinder: } V = \pi r^2 h \qquad \text{curved area} = 2\pi r h\]
\[\text{Rectangular block: } V = l \times w \times h\]
\(r\): radius · \(d\): diameter \(= 2r\) · \(h\): height or length · volume of any prism or cylinder is cross-sectional area × length.
:::

:::warn Radius and diameter
Wire and rod sizes are given as a **diameter**. If you use the diameter where the formula wants the radius, your area comes out four times too big. Halve it first, or use \(A = \pi d^2/4\).
:::

:::eg A wire has a diameter of 0.50 mm. Find its cross-sectional area in \(\mathrm{m^2}\), and the volume of a 2.0 m length of it.
The radius is \(0.25\,\mathrm{mm} = 2.5 \times 10^{-4}\,\mathrm{m}\) (change to metres first).
\[A = \pi r^2 = \pi \times (2.5 \times 10^{-4})^2 = 1.96 \times 10^{-7}\,\mathrm{m^2}\]
To 2 s.f., the data's precision, that is \(2.0 \times 10^{-7}\,\mathrm{m^2}\). The volume of a length of wire is its cross-section times its length: \(V = AL = 1.96 \times 10^{-7} \times 2.0 = 3.9 \times 10^{-7}\,\mathrm{m^3}\).
:::

:::eg A ball has radius 0.11 m. Find its surface area and volume.
Surface area: \(4\pi r^2 = 4\pi \times 0.11^2 = 0.15\,\mathrm{m^2}\).

Volume: \(\tfrac43\pi r^3 = \tfrac43\pi \times 0.11^3 = 5.6 \times 10^{-3}\,\mathrm{m^3}\).
:::

## School physics in one page each

The A Level course assumes you know the following ideas from school physics. Each short section below states them, gives the definitions in exam wording and one worked example, then links to the chapter that develops it.

### Speed, velocity and acceleration

:::def Speed
The distance travelled per unit time: \(v = s/t\) for constant speed. Its unit is \(\mathrm{m\,s^{-1}}\).
:::

**Velocity** is speed in a stated direction. Speed has size only (a **scalar**); velocity has size and direction (a **vector**).

:::def Acceleration
The rate of change of velocity: \(a = \dfrac{\Delta v}{\Delta t}\). Its unit is \(\mathrm{m\,s^{-2}}\).
:::

:::eg A car accelerates uniformly from rest to \(27\,\mathrm{m\,s^{-1}}\) in 9.0 s. Find its acceleration.
\[a = \frac{\Delta v}{\Delta t} = \frac{27 - 0}{9.0} = 3.0\,\mathrm{m\,s^{-2}}\]
Its velocity increases by \(3.0\,\mathrm{m\,s^{-1}}\) every second. A negative acceleration is a **deceleration** if the object is moving in the positive direction.
:::

Develop this in [Kinematics](#phys.kinematics).

### Mass, weight and forces

:::def Force
A push or a pull on an object. A force can change the object's speed, direction or shape. Its unit is the newton (N).
:::

:::def Weight
The force of gravity acting on an object. \(W = mg\), where \(m\) is the mass in kg and \(g\) is the gravitational field strength. Weight is a force, measured in newtons.
:::

**Mass** is the amount of matter in an object, in kg. It does not change from place to place. Weight does, because \(g\) does: on Earth \(g = 9.81\,\mathrm{N\,kg^{-1}}\) (the same as the acceleration of free fall, \(9.81\,\mathrm{m\,s^{-2}}\)), but on the Moon it is about \(1.6\,\mathrm{N\,kg^{-1}}\).

When several forces act on an object, add them (with their directions) to get the **resultant force**. Then \(F = ma\): a resultant force makes an object accelerate. If the resultant is zero, the object stays at rest or keeps moving at constant velocity.

:::eg A student has mass 70 kg. Find her weight on Earth and on the Moon. Then, a 1200 kg car has a driving force of 3000 N and resistive forces of 800 N: find its acceleration.
On Earth: \(W = mg = 70 \times 9.81 = 687\,\mathrm{N} \approx 690\,\mathrm{N}\). On the Moon: \(W = 70 \times 1.6 = 112\,\mathrm{N} \approx 110\,\mathrm{N}\). Her mass is 70 kg in both places.

For the car, the resultant is \(3000 - 800 = 2200\,\mathrm{N}\), so \(a = F/m = 2200/1200 = 1.8\,\mathrm{m\,s^{-2}}\).
:::

Develop this in [Dynamics and momentum](#phys.dynamics) and [Forces, density and pressure](#phys.forces).

### Energy, work and power

:::def Energy
The ability to do work. It is measured in joules (J). Energy cannot be created or destroyed, only transferred from one store to another (the principle of conservation of energy).
:::

Energy is stored as kinetic energy (movement), gravitational potential energy (height), elastic energy (stretched or squashed things), thermal energy, chemical energy, nuclear energy and more. Two formulae you need now are \(E_\text{k} = \tfrac12 mv^2\) and, near the Earth's surface, \(\Delta E_\text{p} = mg\Delta h\). When a force moves an object, it does **work**: work done \(= F \times s\) (the distance moved in the direction of the force), in joules.

:::def Power
The rate of doing work, or the rate of transferring energy: \(P = \dfrac{W}{t} = \dfrac{E}{t}\). Its unit is the watt (W), where \(1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}}\).
:::

The **efficiency** of a machine is useful energy (or power) out divided by total energy (or power) in, often as a percentage.

:::eg A motor lifts a 20 kg box through 1.5 m in 3.0 s. Find the energy gained by the box, the power of the lift and the efficiency if the motor takes in 150 W of electrical power.
Energy gained: \(\Delta E_\text{p} = mg\Delta h = 20 \times 9.81 \times 1.5 = 294\,\mathrm{J} \approx 290\,\mathrm{J}\).

Useful power: \(P = E/t = 294.3/3.0 = 98\,\mathrm{W}\).

Efficiency: \(98.1/150 = 0.654\), or about 65%.
:::

Develop this in [Work, energy and power](#phys.energy).

### Pressure and density

:::def Density
The mass per unit volume of a substance: \(\rho = \dfrac{m}{V}\). Its unit is \(\mathrm{kg\,m^{-3}}\).
:::

:::def Pressure
The force acting per unit area, where the force is at right angles to the surface: \(p = \dfrac{F}{A}\). Its unit is the pascal (Pa), where \(1\,\mathrm{Pa} = 1\,\mathrm{N\,m^{-2}}\).
:::

A large force spread over a large area gives a small pressure, which is why snowshoes work, and why a sharp knife (small area) cuts better than a blunt one.

:::eg A student of weight 600 N stands on two shoes with a total contact area of \(0.040\,\mathrm{m^2}\). Find the pressure on the floor. A steel cube of side 0.020 m has mass 0.0630 kg. Find the density of the steel.
\(p = F/A = 600/0.040 = 15\,000\,\mathrm{Pa} = 1.5 \times 10^{4}\,\mathrm{Pa}\).

The volume of the cube is \(0.020^3 = 8.0 \times 10^{-6}\,\mathrm{m^3}\), so \(\rho = m/V = 0.0630/(8.0 \times 10^{-6}) = 7.9 \times 10^{3}\,\mathrm{kg\,m^{-3}}\).
:::

Develop this in [Forces, density and pressure](#phys.forces).

### Current, potential difference and resistance

:::def Electric current
The rate of flow of charge: \(I = \dfrac{Q}{t}\). Its unit is the ampere (A), where \(1\,\mathrm{A} = 1\,\mathrm{C\,s^{-1}}\). In a metal the charge carriers are electrons, but **conventional current** is drawn from the positive terminal to the negative.
:::

:::def Potential difference (p.d.)
The energy transferred per unit charge as charge passes between two points in a circuit: \(V = \dfrac{W}{Q}\). Its unit is the volt (V), where \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\).
:::

:::def Resistance
The p.d. across a component divided by the current through it: \(R = \dfrac{V}{I}\). Its unit is the ohm (Ω), where \(1\,\Omega = 1\,\mathrm{V\,A^{-1}}\).
:::

An **ammeter** goes **in series** (in the loop, so the current passes through it) and a **voltmeter** goes **in parallel** (across the component). Electrical power is \(P = VI\).

:::html
<figure class="fig"><svg viewBox="70 8 505 240" role="img" aria-label="A series circuit: a 6.0 volt cell, a 20 ohm resistor and an ammeter in one loop, with a voltmeter connected across the resistor. An arrow shows the conventional current direction."><path class="ln" d="M100 130V50H400V200H100V140"/><path class="ln" d="M84 130H116"/><path class="ln thick" d="M92 140H108"/><text class="tl" x="124" y="140">6.0 V</text><path class="ln" d="M400 70H470V170H400"/><circle class="fi" cx="400" cy="70" r="4"/><circle class="fi" cx="400" cy="170" r="4"/><rect class="fp s-ink sw2" x="392" y="90" width="16" height="60"/><text class="tl te" x="384" y="125">20 Ω</text><circle class="fp s-ink sw2" cx="250" cy="200" r="13"/><text class="tb tc" x="250" y="205">A</text><circle class="fp s-ink sw2" cx="470" cy="120" r="13"/><text class="tb tc" x="470" y="125">V</text><path class="c1" d="M190 34H250" marker-end="url(#ah-phys)"/><text class="tl ti ta tc" x="220" y="24">I</text><text class="tl tc" x="250" y="232">ammeter</text><text class="tl" x="490" y="125">voltmeter</text></svg><figcaption>A series circuit. The ammeter is in the loop, so the current passes through it. The voltmeter is across the resistor, so it measures the p.d. between the resistor's ends. The conventional current leaves the positive terminal of the cell, the long plate at the top.</figcaption></figure>
:::

:::eg In the circuit above, the cell has negligible internal resistance. Find the ammeter reading, the voltmeter reading, the power of the resistor and the charge that passes in 2.0 minutes.
The voltmeter is across the resistor, which is connected directly to the cell, so it reads \(6.0\,\mathrm{V}\).

\(I = V/R = 6.0/20 = 0.30\,\mathrm{A}\), which is the ammeter reading.

\(P = VI = 6.0 \times 0.30 = 1.8\,\mathrm{W}\).

\(Q = It = 0.30 \times 120 = 36\,\mathrm{C}\) (the time is changed to seconds first).
:::

:::warn Current is not used up
The current is the **same** at every point in a series loop: the ammeter before the resistor and one after it read the same. The charge carriers are not used up. They **transfer energy** to the resistor, which is why the p.d. across the resistor is not zero.
:::

Develop this in [Electricity](#phys.electricity) and [D.C. circuits](#phys.dc).

### Waves

:::def Wavelength
The shortest distance between two points on a wave that are in phase, for example from one crest to the next crest. Its symbol is \(\lambda\) and its unit is the metre.
:::

:::def Frequency
The number of complete waves passing a point per second. Its symbol is \(f\) and its unit is the hertz (Hz), where \(1\,\mathrm{Hz} = 1\,\mathrm{s^{-1}}\).
:::

The **period** \(T\) is the time for one complete wave, \(T = 1/f\). The **amplitude** is the maximum displacement from the rest position. All waves obey the **wave equation**:

:::formula The wave equation
\[v = f\lambda\]
\(v\): wave speed (\(\mathrm{m\,s^{-1}}\)) · \(f\): frequency (Hz) · \(\lambda\): wavelength (m). In a **transverse** wave the oscillations are at right angles to the direction the wave travels (light, water ripples). In a **longitudinal** wave they are parallel to it (sound).
:::

Light and all other **electromagnetic waves** are transverse waves that need no medium. They all travel at \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\) in a vacuum. In order of increasing frequency (and decreasing wavelength), the electromagnetic spectrum is: **radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays**.

:::eg Sound of frequency 440 Hz travels in air at \(340\,\mathrm{m\,s^{-1}}\). Find its wavelength. Then find the wavelength of a 100 MHz FM radio signal.
\(\lambda = v/f = 340/440 = 0.77\,\mathrm{m}\).

Radio waves travel at \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\), and \(100\,\mathrm{MHz} = 1.00 \times 10^{8}\,\mathrm{Hz}\), so \(\lambda = \dfrac{3.00 \times 10^{8}}{1.00 \times 10^{8}} = 3.00\,\mathrm{m}\).
:::

Develop this in [Waves](#phys.waves) and [Superposition](#phys.superposition).

### The atom and radioactivity

An atom has a tiny, dense, positively charged **nucleus** surrounded by electrons. The nucleus contains **protons** and **neutrons**, together called nucleons.

| Particle | Relative charge | Relative mass |
|---|---|---|
| proton | +1 | 1 |
| neutron | 0 | 1 |
| electron | −1 | about 1/2000 |

A nucleus is written \({}^{A}_{Z}\mathrm{X}\), where \(Z\) is the **proton number** (also the number of electrons in a neutral atom) and \(A\) is the **nucleon number** (protons plus neutrons). **Isotopes** of an element have the same \(Z\) but different numbers of neutrons. Carbon-14 has \(Z = 6\) and \(A = 14\), so it has \(14 - 6 = 8\) neutrons.

Some nuclei are unstable and emit radiation, at random, to become more stable. This is **radioactive decay**.

| Radiation | What it is | Stopped by |
|---|---|---|
| alpha (α) | a helium nucleus, 2 protons and 2 neutrons | paper, or a few centimetres of air |
| beta (β) | a fast electron from the nucleus | a few millimetres of aluminium |
| gamma (γ) | a high-frequency electromagnetic wave | not fully stopped; thick lead reduces it |

Alpha radiation is the most ionising but the least penetrating. In a decay equation the nucleon numbers and the proton numbers must each add up to the same total on both sides.

:::def Half-life
The time taken for the number of undecayed nuclei of a radioactive isotope (and so its activity) to fall to half its starting value.
:::

:::eg Radium-226 (\(Z = 88\)) emits an alpha particle. Write the decay equation. Then a sample of activity 960 Bq has a half-life of 4.0 days: find its activity after 12 days.
An alpha particle is \({}^{4}_{2}\mathrm{He}\), so the daughter has \(A = 226 - 4 = 222\) and \(Z = 88 - 2 = 86\). That is radon-222:
\[{}^{226}_{88}\mathrm{Ra} \;\to\; {}^{222}_{86}\mathrm{Rn} + {}^{4}_{2}\mathrm{He}\]
12 days is \(12/4.0 = 3\) half-lives, so the activity halves three times: \(960 \to 480 \to 240 \to 120\,\mathrm{Bq}\), or \(960/2^3 = 120\,\mathrm{Bq}\).
:::

Develop this in [Particle physics](#phys.particles) and [Nuclear physics](#phys.nuclear).

:::eg Spot the error: a cube of side 2.0 cm has mass 21.6 g. Calculate its density in \(\mathrm{kg\,m^{-3}}\).
A student wrote this answer.

Line 1: \(V = (2.0 \times 10^{-2})^3 = 8.0 \times 10^{-6}\,\mathrm{m^3}\)
Line 2: \(\rho = \dfrac{m}{V} = \dfrac{21.6}{8.0 \times 10^{-6}} = 2.7 \times 10^{6}\,\mathrm{kg\,m^{-3}}\)

Line 1 is correct: the length is converted to metres before it is cubed. [C1] **Line 2 is wrong: the mass is still in grams, but the volume is in cubic metres, so the answer is not in \(\mathrm{kg\,m^{-3}}\). The answer mark is lost.** [A0]

Correct working: \(m = 21.6\,\mathrm{g} = 0.0216\,\mathrm{kg}\), so \(\rho = 0.0216/(8.0 \times 10^{-6}) = 2.7 \times 10^{3}\,\mathrm{kg\,m^{-3}}\). [A1]

Check: \(2700\,\mathrm{kg\,m^{-3}}\) is 2.7 times the density of water, which is plausible for aluminium. A density of two million kilograms per cubic metre should have looked wrong at once. Change **every** quantity to base units before you substitute.
:::

:::try Start easy, finish at exam standard
Q: Write 0.000 35 m in standard form, and then in μm.
A: \(3.5 \times 10^{-4}\,\mathrm{m}\). Since \(1\,\mu\mathrm{m} = 10^{-6}\,\mathrm{m}\), that is \(3.5 \times 10^{-4}/10^{-6} = 350\,\mu\mathrm{m}\).
Q: Convert \(72\,\mathrm{km\,h^{-1}}\) into \(\mathrm{m\,s^{-1}}\), and \(15\,\mathrm{m\,s^{-1}}\) into \(\mathrm{km\,h^{-1}}\).
A: \(72\,\mathrm{km\,h^{-1}} = 72\,000/3600 = 20\,\mathrm{m\,s^{-1}}\). Going the other way, \(15 \times 3600/1000 = 54\,\mathrm{km\,h^{-1}}\). (To change \(\mathrm{m\,s^{-1}}\) into \(\mathrm{km\,h^{-1}}\), multiply by 3.6.)
Q: Rearrange \(v = u + at\) to make \(t\) the subject, then find \(t\) when \(u = 3.0\,\mathrm{m\,s^{-1}}\), \(v = 15\,\mathrm{m\,s^{-1}}\) and \(a = 2.0\,\mathrm{m\,s^{-2}}\).
A: Subtract \(u\): \(v - u = at\). Divide by \(a\): \(t = \dfrac{v - u}{a} = \dfrac{15 - 3.0}{2.0} = 6.0\,\mathrm{s}\).
Q: A straight line through the origin on a graph of \(V\) against \(I\) passes through the point \((0.40\,\mathrm{A}, 2.0\,\mathrm{V})\). Find its gradient, with its unit, and say what it represents.
A: \(\text{gradient} = 2.0/0.40 = 5.0\,\mathrm{V\,A^{-1}}\), which is \(5.0\,\Omega\). It is the resistance of the component.
Q: A force of 60 N acts at \(40^\circ\) above the horizontal. Find its horizontal and vertical components.
A: Horizontal: \(60\cos40^\circ = 45.96\ldots \approx 46\,\mathrm{N}\). Vertical: \(60\sin40^\circ = 38.57\ldots \approx 39\,\mathrm{N}\).
Q: A solid cylindrical rod has diameter 1.2 cm. Find its cross-sectional area in \(\mathrm{m^2}\).
A: The radius is \(0.60\,\mathrm{cm} = 6.0 \times 10^{-3}\,\mathrm{m}\), so \(A = \pi r^2 = \pi \times (6.0 \times 10^{-3})^2 = 1.1 \times 10^{-4}\,\mathrm{m^2}\).
Q: A book has mass 2.5 kg. Find its weight on Earth.
A: \(W = mg = 2.5 \times 9.81 = 24.5\ldots \approx 25\,\mathrm{N}\).
Q: A 2.0 kW kettle runs for 3.0 minutes. How much energy does it transfer?
A: \(E = Pt = 2000 \times 180 = 360\,000\,\mathrm{J} = 3.6 \times 10^{5}\,\mathrm{J}\). The time was changed to seconds first.
Q: A wave on a rope has frequency 2.0 Hz and wavelength 0.75 m. Find its speed.
A: \(v = f\lambda = 2.0 \times 0.75 = 1.5\,\mathrm{m\,s^{-1}}\).
Q: A crate weighing 800 N rests on a base of area \(0.40\,\mathrm{m^2}\). Find the pressure on the floor. How many neutrons are in a carbon-14 nucleus (\(Z = 6\))?
A: \(p = F/A = 800/0.40 = 2000\,\mathrm{Pa} = 2.0 \times 10^{3}\,\mathrm{Pa}\). The nucleon number is 14 and the proton number is 6, so \(14 - 6 = 8\) neutrons.
:::

:::try Ready for AS?
Q: [3 marks] A car accelerates uniformly from \(5.0\,\mathrm{m\,s^{-1}}\) to \(25\,\mathrm{m\,s^{-1}}\) in 8.0 s. Calculate its acceleration and the distance it travels.
H: The distance is the area under the speed–time graph, which is a trapezium.
A: \(a = \dfrac{25 - 5.0}{8.0}\) [C1] \(= 2.5\,\mathrm{m\,s^{-2}}\). [A1] Distance \(= \tfrac12 (5.0 + 25) \times 8.0 = 120\,\mathrm{m}\). [A1]
Q: [3 marks] A force of 80 N acts at \(60^\circ\) above the horizontal. Calculate its horizontal and vertical components.
A: Horizontal \(= 80\cos60^\circ\) [C1] \(= 40\,\mathrm{N}\). [A1] Vertical \(= 80\sin60^\circ = 69\,\mathrm{N}\). [A1]
Q: [4 marks] A cylindrical tank of radius 0.40 m is filled to a depth of 1.2 m with water of density \(1000\,\mathrm{kg\,m^{-3}}\). Calculate the volume of water and its mass.
A: \(V = \pi r^2 h = \pi \times 0.40^2 \times 1.2\) [C1] \(= 0.60\,\mathrm{m^3}\). [A1] \(m = \rho V = 1000 \times 0.6032\) [C1] \(= 6.0 \times 10^{2}\,\mathrm{kg}\). [A1]
Q: [3 marks] The p.d. across a lamp is 6.0 V and the current in it is 0.50 A. Calculate the resistance of the lamp and the energy it transfers in 2.0 minutes.
A: \(R = V/I = 6.0/0.50\) [C1] \(= 12\,\Omega\). [A1] \(E = VIt = 6.0 \times 0.50 \times 120 = 360\,\mathrm{J}\). [A1]
Q: [3 marks] Sound of frequency 512 Hz travels through air at \(340\,\mathrm{m\,s^{-1}}\). Calculate its wavelength. State what happens to the wavelength if the frequency doubles and the speed stays the same.
A: \(\lambda = v/f = 340/512\) [C1] \(= 0.66\,\mathrm{m}\). [A1] The wavelength halves. [B1]
:::

:::quiz
? An astronaut has a mass of 80 kg on Earth. What happens to her mass and her weight on the Moon?
- Both stay the same.
- Her mass decreases and her weight stays the same.
+ Her mass stays the same and her weight decreases.
- Both decrease by the same fraction.
> Mass is the amount of matter and does not change. Weight is the gravitational force, and the Moon's gravitational field strength is smaller. The Moon's pull is weaker, but the astronaut still contains the same amount of matter.
? In a series circuit, an ammeter before a lamp reads 0.30 A. What does an identical ammeter placed after the lamp read?
+ 0.30 A
- Less than 0.30 A, because the lamp uses up some current
- 0 A
- More than 0.30 A
> The same current flows through every part of a series loop. The lamp transfers energy from the charge, but it does not use up the charge.
? How is 0.000 072 written in standard form?
- \(7.2 \times 10^{-4}\)
+ \(7.2 \times 10^{-5}\)
- \(72 \times 10^{-6}\)
- \(7.2 \times 10^{5}\)
> The point moves five places to the right to give 7.2, so the power is \(-5\). \(72 \times 10^{-6}\) is correct in value but is not standard form, because 72 is not between 1 and 10.
? A graph of \(y\) against \(x\) is a straight line with a positive \(y\)-intercept. Which statement is correct?
- \(y\) is directly proportional to \(x\).
- \(y\) is inversely proportional to \(x\).
+ \(y\) increases linearly with \(x\), but is not proportional to \(x\).
- The gradient of the line is the \(y\)-intercept.
> Direct proportion needs a line through the origin. A line with an intercept is linear, \(y = mx + c\), but doubling \(x\) does not double \(y\).
? Which type of radiation is the **most** penetrating?
- Alpha, because it is the heaviest.
- Beta, because it is a fast electron.
+ Gamma
- All three are stopped by thin paper.
> Alpha is stopped by paper and beta by a few millimetres of aluminium, while gamma needs thick lead to reduce it. Alpha is the most ionising, but ionising strongly makes it lose energy quickly, so it is the least penetrating.
? A force of 40 N acts at \(30^\circ\) above the horizontal. What is its vertical component?
- 35 N
- 40 N
+ 20 N
- 23 N
> The vertical component is opposite the \(30^\circ\) angle, so it is \(40\sin30^\circ = 20\,\mathrm{N}\). 35 N is the horizontal component, \(40\cos30^\circ\). 23 N is \(40\tan30^\circ\), but tan is opposite over adjacent and the 40 N force is the hypotenuse. 40 N is the whole force, which only equals the vertical component if the force is vertical.
:::

:::checklist What you can now do
- [ ] I can write numbers in standard form, round to a sensible number of significant figures, and use the prefixes n, μ, m, k, M and G.
- [ ] I can rearrange a formula to make any quantity the subject, and check the units of the answer.
- [ ] I can find the gradient and intercept of a straight-line graph, with units, and recognise direct and inverse proportion.
- [ ] I can use the area under a speed–time graph as distance, and the gradient as acceleration.
- [ ] I can use Pythagoras, sine, cosine and tangent to find sides, angles and the components of a force.
- [ ] I can calculate areas and volumes of circles, spheres and cylinders, converting diameters and units correctly.
- [ ] I can state and use the school definitions of speed, acceleration, force, weight, energy, power, density, pressure, current, p.d. and resistance.
- [ ] I can use \(v = f\lambda\), name the electromagnetic spectrum in order, and describe protons, neutrons, electrons and alpha, beta and gamma radiation.
:::

:::recap
- Standard form is \(a \times 10^{n}\) with \(1 \le a < 10\). Round only at the end, to the s.f. of the least precise data, and always give the unit.
- Change to base units before substituting: \(1\,\mathrm{cm^2} = 10^{-4}\,\mathrm{m^2}\), \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\), \(1\,\mathrm{h} = 3600\,\mathrm{s}\).
- To rearrange a formula, do the same to both sides and undo operations in reverse order.
- A line \(y = mx + c\) has gradient \(\Delta y/\Delta x\) (with a unit) and intercept \(c\). Direct proportion is a straight line through the origin; inverse proportion is \(y = k/x\).
- Speed–time graph: gradient = acceleration, area = distance.
- SOH CAH TOA and Pythagoras. A force \(F\) at \(\theta\) to the horizontal has components \(F\cos\theta\) and \(F\sin\theta\).
- Circle \(\pi r^2\); sphere \(4\pi r^2\) and \(\tfrac43\pi r^3\); cylinder \(\pi r^2 h\). Wire sizes are diameters.
- \(v = s/t\), \(a = \Delta v/\Delta t\), \(W = mg\), \(F = ma\), \(E_\text{k} = \tfrac12 mv^2\), \(P = E/t\), \(\rho = m/V\), \(p = F/A\), \(Q = It\), \(V = IR\), \(P = VI\), \(v = f\lambda\).
- An atom has a nucleus of protons and neutrons with electrons around it. Alpha is stopped by paper, beta by aluminium, gamma is reduced by thick lead.
:::

:::links
- explore: [Forces and Motion: Basics](https://phet.colorado.edu/en/simulations/forces-and-motion-basics) · PhET · push objects and see force, mass and acceleration together
- explore: [Ohm's Law](https://phet.colorado.edu/en/simulations/ohms-law) · PhET · change V and R and watch the current change
- explore: [Build an Atom](https://phet.colorado.edu/en/simulations/build-an-atom) · PhET · build atoms from protons, neutrons and electrons

Links checked 13 October 2026.
:::
Next: [Physical quantities, units and uncertainty](#phys.units)
