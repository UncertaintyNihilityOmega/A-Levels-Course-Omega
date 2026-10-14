@chapter phys.solids
@title Deformation of solids
@level as
@paper CAIE P1 · P2 · P3 (AS)
@time 4–6 hours
@summary How solids stretch and compress under force: Hooke's law and the spring constant, stress, strain and the Young modulus, the experiment to measure it, elastic and plastic behaviour, and the energy stored in a deformed material as the area under a force–extension graph.

:::why
Bridges, cables, climbing ropes, springs in a car's suspension and the bones in your legs all survive because they deform a small amount and then return to shape. Engineers need to know how far a material stretches under a load and when it will fail for good. This chapter gives you the rules for both, and the energy ideas you met in [Work, energy and power](#phys.energy) explain what happens to the energy you put into a stretched material.
:::

**Before you start**, you need work done and the area under a force–displacement graph from [Work, energy and power](#phys.energy), pressure as force per area from [Forces, density and pressure](#phys.forces), and areas and powers of ten from [Physical quantities, units and uncertainty](#phys.units).

:::try Warm-up
Q: A force of 30 N moves an object 0.50 m in the direction of the force. How much work is done? (from [Work, energy and power](#phys.energy))
A: \(W = Fs = 30 \times 0.50 = 15\,\mathrm{J}\).
Q: A force of 600 N is spread over an area of \(0.020\,\mathrm{m^2}\). Find the pressure. (from [Forces, density and pressure](#phys.forces))
A: \(p = F/A = 600/0.020 = 3.0 \times 10^{4}\,\mathrm{Pa}\).
Q: Calculate the cross-sectional area, in \(\mathrm{m^2}\), of a wire of diameter 0.50 mm. (from [Physical quantities, units and uncertainty](#phys.units))
A: Radius \(= 0.25\,\mathrm{mm} = 0.25 \times 10^{-3}\,\mathrm{m}\), so \(A = \pi r^2 = \pi \times (0.25 \times 10^{-3})^2 = 2.0 \times 10^{-7}\,\mathrm{m^2}\) (1.96 before rounding).
:::

## Tension, compression and load

Solid objects change shape when forces act on them. In this chapter, forces and deformations are in **one dimension only**: along a straight line, like a spring or a wire.

- A **tensile force** pulls the object from both ends and tends to stretch it. The object is in **tension**.
- A **compressive force** pushes inward at both ends and tends to squash it. The object is in **compression**.

An object can only be deformed if forces act on it in **pairs**, in opposite directions. Pull on a spring with your hand and the spring pulls back, and the spring is stretched by both forces together. If the force acted from one side only, the spring would just accelerate.

:::def Load
The force applied to deform an object.
:::

:::def Extension
The increase in length of an object when it is stretched.
:::

:::def Compression
The decrease in length of an object when it is squashed.
:::

Extension and compression are measured in the same units as length (metres). The **original length** is the length before the load is applied.

## Hooke's law and the spring constant

Hang a mass on a spring, then a second mass, then a third. For a spring, the extension grows by the same amount each time. That regularity is Hooke's law.

:::def Hooke's law
The extension of an object is proportional to the load applied, provided the limit of proportionality is not exceeded.
:::

:::def Limit of proportionality
The point beyond which the extension is no longer proportional to the load.
:::

:::formula Hooke's law and the spring constant
\[F = kx\]
\(F\): load (N) · \(x\): extension or compression (m) · \(k\): spring constant (\(\mathrm{N\,m^{-1}}\)). The graph of \(F\) against \(x\) is a straight line through the origin, with gradient \(k\).
:::

:::def Spring constant
The force per unit extension (or compression): \(k = F/x\), measured in \(\mathrm{N\,m^{-1}}\). A stiff spring has a large \(k\).
:::

The spring constant belongs to the **object**: a long spring has a smaller \(k\) than a short one made of the same wire. A spring obeys \(F = kx\) for a compression in the same way, with the force pushing outward.

:::eg A spring of spring constant \(40\,\mathrm{N\,m^{-1}}\) hangs from a clamp, with a 0.50 kg mass on its end. Calculate the extension of the spring. A different spring, with \(k = 200\,\mathrm{N\,m^{-1}}\), is compressed by 5.0 cm. What force does it exert?
The load is the weight of the mass: \(F = mg = 0.50 \times 9.81 = 4.9\,\mathrm{N}\). [C1]

\[x = \frac{F}{k} = \frac{4.905}{40} = 0.12\,\mathrm{m}\] [A1] (0.123 m before rounding to 2 significant figures)
For the second spring, change 5.0 cm to 0.050 m first: \(F = kx = 200 \times 0.050 = 10\,\mathrm{N}\). [A1]
:::

### Springs in series and parallel

Combined springs are not in the syllabus outcomes, but questions use them often and the reasoning is short.

:::proof Springs in series and in parallel
**Series** (end to end): the same force \(F\) acts through each spring, because each pulls on the next. The extensions add: \(x = x_1 + x_2\).
Using \(x = F/k\) for each: \(\dfrac{F}{k} = \dfrac{F}{k_1} + \dfrac{F}{k_2}\), and dividing by \(F\) gives \(\dfrac{1}{k} = \dfrac{1}{k_1} + \dfrac{1}{k_2}\).
**Parallel** (side by side, sharing the load): both springs have the same extension \(x\), and the forces add: \(F = F_1 + F_2\).
Using \(F = kx\) for each: \(kx = k_1 x + k_2 x\), and dividing by \(x\) gives \(k = k_1 + k_2\).
:::

Two springs of 60 and \(90\,\mathrm{N\,m^{-1}}\) in parallel give \(150\,\mathrm{N\,m^{-1}}\), stiffer than either. In series they give \(\dfrac{60 \times 90}{60 + 90} = 36\,\mathrm{N\,m^{-1}}\), softer than either. Notice that the formulae have the same form as the resistor formulae in [D.C. circuits](#phys.dc), with the series and parallel rules swapped.

## Stress, strain and the Young modulus

A thick steel rope and a thin steel wire stretch by different amounts under the same load, though they are the same material. To describe the **material** rather than the sample, we divide out its size.

:::def Stress
The force per unit cross-sectional area: \(\sigma = F/A\). It is measured in pascals (\(1\,\mathrm{Pa} = 1\,\mathrm{N\,m^{-2}}\)), the same unit as pressure.
:::

:::def Strain
The extension per unit original length: \(\varepsilon = x/L\). It is a ratio of two lengths, so it has **no unit**.
:::

Stress shows how hard the material is being pulled (per unit area of metal), and strain shows how much it has stretched in proportion to its length. Within the limit of proportionality, a bigger stress gives a proportionally bigger strain, and the constant of proportionality is a property of the material.

:::def Young modulus
The ratio of stress to strain: \(E = \sigma/\varepsilon\), for a material loaded within its limit of proportionality. It is measured in pascals.
:::

:::formula Stress, strain and the Young modulus
\[\sigma = \frac{F}{A} \qquad \varepsilon = \frac{x}{L} \qquad E = \frac{\sigma}{\varepsilon} = \frac{FL}{Ax}\]
\(F\): tensile force (N) · \(A\): cross-sectional area (\(\mathrm{m^2}\)) · \(x\): extension (m) · \(L\): original length (m) · \(E\): Young modulus (Pa). For a wire of diameter \(d\), \(A = \pi d^2/4\).
:::

Typical values of the Young modulus (these vary with the exact alloy or sample):

| Material | Typical \(E\) / Pa |
|---|---|
| steel | \(2 \times 10^{11}\) |
| copper | \(1.2 \times 10^{11}\) |
| glass | \(7 \times 10^{10}\) |
| rubber | \(10^{7}\) |

The Young modulus is enormous for metals, which are very stiff, and tiny for rubber, which stretches easily. The **Young modulus is a property of the material**, whereas the **spring constant is a property of the object**. Combine the two definitions and you get the link: since \(F = (EA/L)\,x\), the spring constant of a wire is \(k = EA/L\).

:::eg A steel wire of original length 2.5 m and diameter 0.40 mm carries a load of 25 N, and its extension is 2.5 mm. Calculate (a) the stress, (b) the strain and (c) the Young modulus.
(a) Cross-sectional area: \(A = \pi r^2 = \pi (0.20 \times 10^{-3})^2 = 1.26 \times 10^{-7}\,\mathrm{m^2}\). [C1]
\[\sigma = \frac{F}{A} = \frac{25}{1.26 \times 10^{-7}} = 2.0 \times 10^{8}\,\mathrm{Pa}\] [A1]
(b) \(\varepsilon = \dfrac{x}{L} = \dfrac{2.5 \times 10^{-3}}{2.5} = 1.0 \times 10^{-3}\) (no unit). [A1]
(c) \(E = \dfrac{\sigma}{\varepsilon} = \dfrac{1.99 \times 10^{8}}{1.0 \times 10^{-3}} = 2.0 \times 10^{11}\,\mathrm{Pa}\). [A1]
The result matches the typical value for steel. Keep the radius, not the diameter, inside \(\pi r^2\), and change millimetres to metres before you substitute.
:::

:::eg How far does a copper wire of length 3.0 m and diameter 0.50 mm stretch when a load of 15 N is hung from it? (\(E = 1.2 \times 10^{11}\,\mathrm{Pa}\))
Rearrange \(E = \dfrac{FL}{Ax}\) for the extension:
\[x = \frac{FL}{AE} = \frac{15 \times 3.0}{(1.96 \times 10^{-7}) \times (1.2 \times 10^{11})}\] [C1]
\[x = 1.9 \times 10^{-3}\,\mathrm{m} = 1.9\,\mathrm{mm}\] [A1]
The strain is only \(1.9 \times 10^{-3}/3.0 = 6.4 \times 10^{-4}\). Metals stretch by tiny fractions of their length, and that is why measuring \(E\) needs a long wire and careful readings.
:::

Stress, strain and \(E\) work for **compression** exactly as for tension: the force squashes the material, \(x\) is the decrease in length, and the same Young modulus applies (for the small deformations of this chapter). Bones, building columns and the legs of a table are all in compression.

:::eg A femur (thigh bone) of length 0.45 m and cross-sectional area \(3.0\,\mathrm{cm^2}\) carries a compressive load of 0.70 kN. Take \(E = 1.8 \times 10^{10}\,\mathrm{Pa}\). Calculate the stress, the strain and the amount by which the bone is shortened.
Change the units first: \(A = 3.0\,\mathrm{cm^2} = 3.0 \times 10^{-4}\,\mathrm{m^2}\) and \(F = 700\,\mathrm{N}\). [C1]
\[\sigma = \frac{F}{A} = \frac{700}{3.0 \times 10^{-4}} = 2.3 \times 10^{6}\,\mathrm{Pa}\] [A1]
\[\varepsilon = \frac{\sigma}{E} = \frac{2.33 \times 10^{6}}{1.8 \times 10^{10}} = 1.3 \times 10^{-4}\] [A1] (no unit)
The decrease in length is \(x = \varepsilon L = (1.30 \times 10^{-4}) \times 0.45 = 5.8 \times 10^{-5}\,\mathrm{m}\) (0.058 mm). [A1]
There is one square centimetre of conversion to watch: \(1\,\mathrm{cm^2} = 10^{-4}\,\mathrm{m^2}\), not \(10^{-2}\,\mathrm{m^2}\). The bone shortens by less than the thickness of a hair, so it stays well inside its elastic region.
:::

### Stress–strain graphs

A force–extension graph describes one particular sample. Plot **stress against strain** instead and the graph describes the **material**: a thick and a thin wire of the same metal give the same line. Within the limit of proportionality the line is straight, and

\[\text{gradient of the stress–strain graph} = \frac{\sigma}{\varepsilon} = E\]

so the steeper line belongs to the stiffer material. (On a force–extension graph the gradient is the spring constant \(k = EA/L\) of that sample instead.)

:::plot Stress against strain for steel and copper, within their limits of proportionality. The steeper line is the stiffer material. Note the powers of ten in the axis labels.
--f "2.0*x" --f "1.2*x" --x 0 0.5 --y 0 1.4 --xstep 0.1 --xlabel "ε / 10⁻³" --ylabel "σ / 10⁸ Pa" --label "steel" --label "copper" --legend tr
:::

:::eg Use the graph to find the Young modulus of each metal.
Steel: at \(\varepsilon = 0.50 \times 10^{-3}\), \(\sigma = 1.0 \times 10^{8}\,\mathrm{Pa}\), so \(E = \dfrac{1.0 \times 10^{8}}{0.50 \times 10^{-3}}\) [C1] \(= 2.0 \times 10^{11}\,\mathrm{Pa}\). [A1]
Copper: at \(\varepsilon = 0.50 \times 10^{-3}\), \(\sigma = 0.60 \times 10^{8}\,\mathrm{Pa}\), so \(E = 1.2 \times 10^{11}\,\mathrm{Pa}\). [A1]
Read the powers of ten from the axis labels: "\(\varepsilon / 10^{-3}\)" means that a reading of 0.50 is a strain of \(0.50 \times 10^{-3}\). The line passes through the origin, so one point far along it is enough; for a line that does not, take two points far apart.
:::

## Measuring the Young modulus of a metal wire

Because the extension is so small, the experiment uses a **long, thin wire**: a long wire has a larger extension for the same strain, and a thin wire has a larger stress (and hence strain) for the same load. Both make the extension easier to measure, which reduces its percentage uncertainty.

:::html
<figure class="fig"><svg viewBox="15 30 550 208" role="img" aria-label="Apparatus for the Young modulus of a wire: a long horizontal wire clamped at the left, passing over a pulley at the right with slotted masses hanging from it, a marker on the wire next to a fixed metre rule, and the original length L measured from the clamp to the marker."><rect class="f1 s-acc sw2" x="30" y="70" width="30" height="60"/><text class="tl tc" x="45" y="150">clamp</text><path class="ln" d="M60 100H520"/><text class="tl tc" x="160" y="92">test wire</text><path class="ln thin dash" d="M360 52V96"/><path class="c1" d="M210 56H62" marker-end="url(#ah-phys)"/><path class="c1" d="M210 56H358" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="210" y="48">L</text><path class="fa" d="M354 100H366L360 116Z"/><rect class="fm s-mute sw1" x="300" y="132" width="140" height="16"/><path class="ln-m thin" d="M314 132V140M328 132V140M342 132V140M356 132V140M370 132V140M384 132V140M398 132V140M412 132V140M426 132V140"/><text class="tl tc" x="370" y="172">marker and fixed metre rule</text><circle class="fp s-ink sw2" cx="520" cy="118" r="18"/><text class="tl tc" x="520" y="84">pulley</text><path class="ln" d="M538 118V188"/><rect class="f1 s-acc sw2" x="526" y="188" width="24" height="12"/><rect class="f1 s-acc sw2" x="526" y="200" width="24" height="12"/><rect class="f1 s-acc sw2" x="526" y="212" width="24" height="12"/><text class="tl te" x="516" y="212">slotted masses</text></svg><figcaption>The marker moves along the metre rule as masses are added. The original length L is measured from the clamp to the marker with the load on its first (small) value, and the extension is read from the rule.</figcaption></figure>
:::

:::lab Measuring the Young modulus of a metal wire
:::steps
1. Clamp the wire firmly at one end and pass it over a pulley, as in the figure, with a mass hanger on the other end. Fix a metre rule next to the wire, with a marker (a small tape flag) attached to the wire against the rule. Put a box of soft material on the floor under the masses, and wear safety goggles in case the wire snaps.
2. Add a small load to straighten the wire. Measure the original length \(L\) from the clamp to the marker with a metre rule or tape.
3. Measure the diameter of the wire with a micrometer at several places along its length and in two perpendicular directions at each place. Take the mean, and calculate \(A = \pi d^2/4\).
4. Add slotted masses one at a time, and read the extension \(x\) from the rule each time. Record the load \(F = mg\) and \(x\) in a table. Then remove the masses one at a time and check that the marker returns to its starting reading: if it does, the wire has not been stretched beyond its elastic limit.
5. Plot a graph of \(F\) (on the \(y\)-axis) against \(x\). It is a straight line through the origin for a metal within the limit of proportionality. Find the gradient, which is \(F/x = EA/L\).
6. Calculate \(E = \text{gradient} \times \dfrac{L}{A}\).
:::
:::

Using a graph is better than a single reading, because a line of best fit averages out random errors. The diameter appears squared in \(A\), so its percentage uncertainty doubles, which is why many readings with a micrometer are taken. A reference wire next to the test wire (Searle's apparatus) removes errors caused by the support moving or the temperature changing.

:::eg In a Young modulus experiment with a copper wire, the original length is 1.80 m and the mean diameter is 0.50 mm. A graph of load against extension is a straight line of gradient \(13\,\mathrm{N\,mm^{-1}}\). Calculate the Young modulus of copper.
Convert the gradient to base units: \(13\,\mathrm{N\,mm^{-1}} = 13 \times 10^{3}\,\mathrm{N\,m^{-1}}\). [C1]

Area: \(A = \pi (0.25 \times 10^{-3})^2 = 1.96 \times 10^{-7}\,\mathrm{m^2}\). [C1]
\[E = \text{gradient} \times \frac{L}{A} = \frac{1.3 \times 10^{4} \times 1.80}{1.96 \times 10^{-7}}\] [C1]
\[E = 1.2 \times 10^{11}\,\mathrm{Pa}\] [A1]
:::

## Elastic and plastic deformation

Bend a paper clip a little and it springs back. Bend it a lot and it stays bent. These two behaviours are called elastic and plastic.

:::def Elastic deformation
Deformation in which the object returns to its original shape and size when the load is removed.
:::

:::def Plastic deformation
Deformation in which the object does not return to its original shape when the load is removed. Some of the extension is permanent.
:::

:::def Elastic limit
The maximum load (or stress) beyond which the object will not return to its original length when the load is removed.
:::

For many metals, the limit of proportionality and the elastic limit are close together, and the elastic limit may be slightly further along. A material can be elastic but not proportional, such as rubber. The graph shows what happens to a ductile metal wire as the load rises.

:::html
<figure class="fig"><svg viewBox="45 5 535 295" role="img" aria-label="Force against extension graph for a metal wire. The line is straight from the origin O to P, the limit of proportionality. The curve continues through E, the elastic limit, into the plastic region and reaches the breaking point. If unloaded from U, the line returns parallel to OP and meets the extension axis at a permanent extension."><path class="ax" d="M70 250V25" marker-end="url(#ah)"/><path class="ax" d="M70 250H555" marker-end="url(#ah)"/><text class="tl" x="78" y="26">F</text><text class="tl te" x="64" y="266">O</text><text class="tl te" x="572" y="272">x</text><path class="c1" d="M70 250L170 120Q200 81 270 60Q340 40 400 44Q430 46 445 80"/><path class="c2" d="M337.5 46L180.6 250" marker-end="url(#ah2-phys)"/><circle class="fa" cx="170" cy="120" r="5"/><circle class="fa" cx="187.5" cy="101.6" r="5"/><circle class="fa" cx="337.5" cy="46" r="5"/><circle class="fa" cx="445" cy="80" r="5"/><text class="tl te" x="160" y="120">P</text><text class="tl te" x="180" y="94">E</text><text class="tl tc" x="337" y="32">U</text><text class="tl" x="454" y="84">breaks</text><text class="tl" x="268" y="176">unloading line,</text><text class="tl" x="268" y="194">parallel to OP</text><path class="c1" d="M125.3 270H72" marker-end="url(#ah-phys)"/><path class="c1" d="M125.3 270H178.6" marker-end="url(#ah-phys)"/><text class="tl tc" x="125" y="292">permanent extension</text></svg><figcaption>P is the limit of proportionality and E the elastic limit. Past E the wire deforms plastically. Unloading from U, the extension falls along a line parallel to OP, and the wire is left with a permanent extension.</figcaption></figure>
:::

Read the graph from the origin outwards.

- **O to P**: a straight line through the origin. Hooke's law holds, and the Young modulus applies. The wire is elastic.
- **P to E**: the curve bends, so extension is no longer proportional to load, but the wire still returns to its original length when the load is removed.
- **Beyond E**: plastic deformation. The extension keeps growing, and when the load is removed the wire is left permanently longer.
- **Unloading from U**: the force falls along a line **parallel** to the original straight line OP. When the force reaches zero, the extension left is the permanent extension.

Energy is not all given back when a wire is stretched past its elastic limit. The work done in loading is the area under the loading curve from O to U. On unloading, the wire gives back only the area under the unloading line (a triangle). The **area between the loading curve and the unloading line** is the energy that stays in the wire: it has gone into rearranging the metal's structure and heating it.

:::eg A copper wire is loaded beyond its elastic limit to a force of 60 N, where its extension is 6.0 mm. The area under the loading curve is 0.25 J. When the load is removed, the wire is left with a permanent extension of 3.6 mm. Calculate the energy recovered on unloading and the energy dissipated in the wire.
The unloading line is straight, from (6.0 mm, 60 N) down to (3.6 mm, 0), so the energy recovered is a triangle:
\[E = \tfrac12 \times 60 \times (6.0 - 3.6) \times 10^{-3}\] [C1]
\[E = 0.072\,\mathrm{J}\] [A1]
Energy dissipated \(= 0.25 - 0.072 = 0.18\,\mathrm{J}\). [A1]
Less than a third of the work done comes back. This is why a car's crumple zone is made of metal that deforms plastically: it absorbs the kinetic energy instead of returning it.
:::

Different materials behave differently.

:::html
<figure class="fig wide"><svg viewBox="0 0 620 215" role="img" aria-label="Three force against extension curves side by side: a brittle material, a straight line that ends abruptly at breaking; a ductile metal, a straight section then a long curve and breaking; a polymer such as rubber, a smooth S-shaped curve."><path class="ax" d="M30 170V20" marker-end="url(#ah)"/><path class="ax" d="M30 170H190" marker-end="url(#ah)"/><path class="c1" d="M30 170L120 40"/><path class="ln" d="M114 34L126 46M126 34L114 46"/><text class="tl tc" x="105" y="196">brittle: glass</text><path class="ax" d="M230 170V20" marker-end="url(#ah)"/><path class="ax" d="M230 170H390" marker-end="url(#ah)"/><path class="c1" d="M230 170L265 75Q285 40 320 36Q355 32 365 45"/><path class="ln" d="M359 39L371 51M371 39L359 51"/><text class="tl tc" x="310" y="196">ductile: copper</text><path class="ax" d="M430 170V20" marker-end="url(#ah)"/><path class="ax" d="M430 170H590" marker-end="url(#ah)"/><path class="c1" d="M430 170C470 100 480 105 515 100C545 96 560 70 575 30"/><text class="tl tc" x="510" y="196">polymer: rubber</text><text class="tl" x="38" y="30">F</text><text class="tl" x="238" y="30">F</text><text class="tl" x="438" y="30">F</text><text class="tl" x="176" y="162">x</text><text class="tl" x="376" y="162">x</text><text class="tl" x="576" y="162">x</text></svg><figcaption>A brittle material breaks with almost no plastic region. A ductile metal has a long plastic region. A polymer such as rubber stretches a long way, is not proportional at any point, and returns to its length when unloaded.</figcaption></figure>
:::

A **brittle** material, such as glass or cast iron, snaps soon after its elastic region, with hardly any plastic deformation. A **ductile** material, such as copper, can be drawn out into a wire because it has a long plastic region. A **polymeric** material, such as rubber, stretches a long way and is elastic, but the extension is not proportional to the load.

Try the widget below. Choose a material and slide the load up. Stay below the limit of proportionality and the Young modulus stays constant. Push past it, then press **Remove load** and see the permanent extension appear.

:::html
<div class="widget" data-w="phys-stretch" data-material="copper" data-l="2.0" data-d="0.50"></div>
:::

:::warn Limit of proportionality is not the elastic limit
Hooke's law (and the Young modulus) apply **only up to the limit of proportionality**. The elastic limit can be at a slightly higher load: between the two points the wire is elastic but not proportional. Always write "limit of proportionality" for the point where the straight line ends, and "elastic limit" for the point beyond which the deformation becomes permanent.
:::

## Energy stored in a deformed material

To stretch a spring, you must pull, and the force acts through a distance. So work is done, and the energy is stored as **elastic potential energy** in the material. If the spring is released, this energy is transferred back.

The force changes as the spring stretches, so \(W = Fx\) does not apply. But the work done is the **area under the force–extension graph**, as you saw in [Work, energy and power](#phys.energy).

:::proof Elastic potential energy \(\tfrac12 Fx\)
For a material within its limit of proportionality, the graph of \(F\) against \(x\) is a straight line through the origin.
The work done in stretching from zero to extension \(x\) is the area under the line from 0 to \(x\).
That area is a triangle with base \(x\) and height \(F\), the final force.
Area \(= \tfrac12 \times \text{base} \times \text{height} = \tfrac12 Fx\).
No energy is dissipated if the deformation is elastic, so this work is stored as elastic potential energy: \(E_\mathrm{P} = \tfrac12 Fx\).
Using \(F = kx\) gives \(E_\mathrm{P} = \tfrac12 (kx)x = \tfrac12 kx^2\).
:::

:::formula Elastic potential energy
\[E_\mathrm{P} = \tfrac12 Fx = \tfrac12 kx^2\]
\(E_\mathrm{P}\): elastic potential energy (J) · \(F\): final force (N) · \(x\): extension (m) · \(k\): spring constant (\(\mathrm{N\,m^{-1}}\)). Valid only within the limit of proportionality. For any other graph, find the area under it.
:::

:::plot The graph of force against extension for the spring in the earlier example (\(k = 40\,\mathrm{N\,m^{-1}}\)) is a straight line. The shaded triangle is the energy stored when the extension is 0.123 m.
--f "40*x" --x 0 0.2 --y 0 10 --xstep 0.05 --shade "0,0,0.1226" --pt "0.1226,4.905,(0.123 m, 4.9 N)@nw" --xlabel "x / m" --ylabel "F / N" --label "F = 40x"
:::

:::eg Calculate the energy stored in the spring with \(k = 40\,\mathrm{N\,m^{-1}}\) when it supports the 0.50 kg mass (extension 0.123 m). Then find the energy stored if the extension is doubled.
\[E_\mathrm{P} = \tfrac12 Fx = \tfrac12 \times 4.905 \times 0.1226\] [C1]
\[E_\mathrm{P} = 0.30\,\mathrm{J}\] [A1]
Check with the other form: \(\tfrac12 kx^2 = \tfrac12 \times 40 \times 0.1226^2 = 0.30\,\mathrm{J}\).
If the extension doubles, \(E_\mathrm{P}\) is proportional to \(x^2\), so it becomes four times as large: 1.2 J.
:::

If the graph is a curve, there is no formula. Estimate the area by counting squares or by splitting it into trapezia.

:::eg A rubber band is stretched and the force is measured at several extensions. Estimate the energy stored when the extension is 10.0 cm. The table shows the readings.

| \(x\) / cm | 0 | 2.0 | 4.0 | 6.0 | 8.0 | 10.0 |
|---|---|---|---|---|---|---|
| \(F\) / N | 0 | 1.5 | 2.5 | 3.2 | 4.0 | 5.5 |

The graph is not a straight line, so use the area under it. Split it into five strips, each 2.0 cm \(= 0.020\,\mathrm{m}\) wide, and treat each as a trapezium, \(\tfrac12(F_1 + F_2)\Delta x\): [C1]
\[\begin{aligned} E &= 0.020 \times \left[\tfrac12 (0 + 1.5) + \tfrac12 (1.5 + 2.5) + \tfrac12 (2.5 + 3.2) + \tfrac12 (3.2 + 4.0) + \tfrac12 (4.0 + 5.5)\right] \\ &= 0.020 \times [0.75 + 2.0 + 2.85 + 3.6 + 4.75] = 0.020 \times 13.95 = 0.28\,\mathrm{J} \end{aligned}\] [A1]
:::

For a wire, stress is force per area and strain is extension per length, so the energy per unit volume works out as \(\tfrac12 \sigma\varepsilon\). You may see this, but Cambridge does not require it.

:::board
AQA and OCR also use the terms "yield point", "breaking stress" and "ultimate tensile strength", and AQA expects the energy per unit volume \(\tfrac12 \sigma\varepsilon\). The Cambridge syllabus needs only the terms in this chapter. All boards agree on Hooke's law, the Young modulus and \(\tfrac12 Fx\).
:::

:::exam Describing the Young modulus experiment
A "describe an experiment" question rewards a sequence of distinct points: the measurements (original length with a rule, diameter with a micrometer at several places), the procedure (load added in steps, extension read each time, check by unloading), the graph (\(F\) against \(x\)) and how the result is obtained (\(E = \text{gradient} \times L/A\)). Add one safety point (goggles, a box under the masses) and one reason for a long thin wire. Six separate points score six marks, so do not write the same point twice.
:::

:::eg Spot the error: a steel wire of diameter 0.40 mm carries a load of 25 N. Calculate the stress in the wire.
A student wrote this answer.

Line 1: \(A = \pi r^2 = \pi \times (0.40 \times 10^{-3})^2 = 5.03 \times 10^{-7}\,\mathrm{m^2}\)
Line 2: \(\sigma = F/A = 25/(5.03 \times 10^{-7}) = 5.0 \times 10^{7}\,\mathrm{Pa}\)

**Line 1 is wrong: 0.40 mm is the diameter, so the radius is 0.20 mm. The area is four times too large and the stress four times too small. The substitution mark and the answer mark are lost.** [C0] [A0]

Correct working: \(A = \pi (0.20 \times 10^{-3})^2 = 1.26 \times 10^{-7}\,\mathrm{m^2}\), so \(\sigma = 25/(1.26 \times 10^{-7})\) [C1] \(= 2.0 \times 10^{8}\,\mathrm{Pa}\). [A1]

Check: a wire this thin carrying 25 N should have a stress of a few hundred megapascals, about the same as the limit of proportionality of steel. A tenth of that would not make sense for such a thin wire.
:::

:::try Start easy, finish at exam standard
Q: A spring extends by 0.060 m when a force of 3.0 N is applied. What is its spring constant?
A: \(k = F/x = 3.0/0.060 = 50\,\mathrm{N\,m^{-1}}\).
Q: A wire of original length 2.0 m extends by 1.0 mm. Calculate the strain.
A: \(\varepsilon = x/L = 1.0 \times 10^{-3}/2.0 = 5.0 \times 10^{-4}\). It has no unit.
Q: A force of 80 N is applied to a rod of cross-sectional area \(4.0 \times 10^{-6}\,\mathrm{m^2}\). Calculate the stress.
A: \(\sigma = F/A = 80/(4.0 \times 10^{-6}) = 2.0 \times 10^{7}\,\mathrm{Pa}\).
Q: A spring has \(k = 100\,\mathrm{N\,m^{-1}}\). Calculate the energy stored when it is extended by 0.10 m.
A: \(E_\mathrm{P} = \tfrac12 kx^2 = \tfrac12 \times 100 \times 0.10^2 = 0.50\,\mathrm{J}\). (Not \(Fx = 1.0\,\mathrm{J}\): the force grows from zero, so only half of \(Fx\) is stored.)
Q: Two identical springs, each with \(k = 80\,\mathrm{N\,m^{-1}}\), are joined end to end. What is the spring constant of the combination?
A: In series, \(\dfrac{1}{k} = \dfrac{1}{80} + \dfrac{1}{80} = \dfrac{2}{80}\), so \(k = 40\,\mathrm{N\,m^{-1}}\).
Q: A wire of Young modulus \(2.0 \times 10^{11}\,\mathrm{Pa}\) has a strain of \(1.5 \times 10^{-3}\). Calculate the stress.
A: \(\sigma = E\varepsilon = 2.0 \times 10^{11} \times 1.5 \times 10^{-3} = 3.0 \times 10^{8}\,\mathrm{Pa}\).
Q: The straight part of a stress–strain graph passes through the origin and the point (strain \(1.5 \times 10^{-3}\), stress \(1.8 \times 10^{8}\,\mathrm{Pa}\)). Find the Young modulus of the material.
A: \(E = \text{gradient} = \dfrac{1.8 \times 10^{8}}{1.5 \times 10^{-3}} = 1.2 \times 10^{11}\,\mathrm{Pa}\) (a value typical of copper).
Q: A wire is replaced by another of the same material and length but double the diameter. The same load is applied. How does the extension change?
A: The area is four times larger (\(A \propto d^2\)), and \(x = FL/(AE)\) so the extension is four times smaller.
Q: Explain the difference between the limit of proportionality and the elastic limit.
A: Up to the limit of proportionality, extension is proportional to load. Up to the elastic limit, the object returns to its original length when the load is removed. The elastic limit may be slightly beyond the limit of proportionality.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the Young modulus.
A: The ratio of stress to strain. [B1] Stress is force per unit cross-sectional area and strain is extension per unit original length (valid within the limit of proportionality). [B1]
Q: [2 marks] ★ A copper wire of diameter 0.80 mm carries a tension of 30 N. Calculate the stress in the wire.
A: \(\sigma = F/A = \dfrac{30}{\pi \times (0.40 \times 10^{-3})^2}\) [C1] \(= 6.0 \times 10^{7}\,\mathrm{Pa}\). [A1]
Q: [3 marks] ★★ A spring obeys Hooke's law. A force of 6.0 N extends it by 0.025 m. (a) Calculate its spring constant. (b) Calculate the energy stored when its extension is 0.040 m.
A: (a) \(k = F/x = 6.0/0.025 = 240\,\mathrm{N\,m^{-1}}\). [C1] (b) \(E_\mathrm{P} = \tfrac12 kx^2 = \tfrac12 \times 240 \times 0.040^2\) [C1] \(= 0.19\,\mathrm{J}\). [A1]
Q: [4 marks] ★★ In an experiment, a steel wire of original length 2.40 m and diameter 0.32 mm is loaded. A graph of load \(F\) against extension \(x\) is a straight line through the origin passing through the point (4.0 mm, 27 N). Calculate the Young modulus of the steel.
H: Find the gradient first, in \(\mathrm{N\,m^{-1}}\), then use gradient \(\times L/A\).
A: Gradient \(= 27/(4.0 \times 10^{-3}) = 6750\,\mathrm{N\,m^{-1}}\). [C1] Area \(A = \pi (0.16 \times 10^{-3})^2 = 8.04 \times 10^{-8}\,\mathrm{m^2}\). [C1] \(E = \text{gradient} \times L/A = 6750 \times 2.40/(8.04 \times 10^{-8})\) [C1] \(= 2.0 \times 10^{11}\,\mathrm{Pa}\). [A1]
Q: [6 marks] ★★ Describe an experiment to determine the Young modulus of a metal in the form of a long wire. You may draw a diagram.
A: A long thin wire is clamped at one end, with a load hanging from the other end (or over a pulley). [B1] The original length is measured with a metre rule or tape. [B1] The diameter is measured with a micrometer at several places and in perpendicular directions, and the mean is used to find the area. [B1] Masses are added in steps and the extension is measured each time, using a marker against a rule. [B1] \(F\) is plotted against \(x\), giving a straight line through the origin. [B1] \(E = \text{gradient} \times L/A\). [B1] (Other creditable points, up to the total of 6: unloading to check that the wire returns to its original length; goggles or a box under the masses; a long thin wire gives a larger extension and a smaller percentage uncertainty.)
Q: [3 marks] ★★ The table shows the force needed to stretch a piece of elastic cord. Estimate the energy stored when the extension is 40 mm.

| \(x\) / mm | 0 | 10 | 20 | 30 | 40 |
|---|---|---|---|---|---|
| \(F\) / N | 0 | 2.0 | 3.5 | 5.5 | 9.5 |

H: The energy is the area under the graph. Use trapezia, each 10 mm \(= 0.010\,\mathrm{m}\) wide.
A: Energy = area under the \(F\)–\(x\) graph. [C1]
\[\begin{aligned} E &= 0.010 \times \left[\tfrac12(0 + 2.0) + \tfrac12(2.0 + 3.5) + \tfrac12(3.5 + 5.5) + \tfrac12(5.5 + 9.5)\right] \\ &= 0.010 \times 15.75 = 0.16\,\mathrm{J} \end{aligned}\] [C1] [A1]
Q: [5 marks] ★★★ A steel wire of length 2.0 m and diameter 0.60 mm is joined end to end to a copper wire of length 1.0 m and diameter 0.30 mm. The same tension acts in both wires. The Young modulus of steel is \(2.0 \times 10^{11}\,\mathrm{Pa}\) and that of copper is \(1.2 \times 10^{11}\,\mathrm{Pa}\). (a) Show that the extension of the copper wire is about 3.3 times the extension of the steel wire. (b) The tension is 60 N. Calculate the total extension of the two wires.
H: Use \(x = FL/(AE)\) for each wire; \(F\) is the same, and \(A \propto d^2\).
A: (a) \(x = \dfrac{FL}{AE}\), and \(F\) is the same, so \(\dfrac{x_\text{Cu}}{x_\text{steel}} = \dfrac{L_\text{Cu}}{L_\text{steel}} \times \dfrac{A_\text{steel}}{A_\text{Cu}} \times \dfrac{E_\text{steel}}{E_\text{Cu}}\) [C1] \(= 0.50 \times 4.0 \times 1.67 = 3.3\). [A1] (b) \(x_\text{steel} = \dfrac{60 \times 2.0}{\pi (0.30 \times 10^{-3})^2 \times 2.0 \times 10^{11}} = 2.1\,\mathrm{mm}\) [C1] and \(x_\text{Cu} = \dfrac{60 \times 1.0}{\pi (0.15 \times 10^{-3})^2 \times 1.2 \times 10^{11}} = 7.1\,\mathrm{mm}\). [C1] Total \(= 9.2\,\mathrm{mm}\). [A1]
Q: [6 marks] ★★★ A mass of 0.50 kg is released from rest 0.30 m above the top of a light vertical spring of spring constant \(120\,\mathrm{N\,m^{-1}}\), fixed at its lower end. The spring is compressed as the mass lands on it and comes to rest at the lowest point. Ignore air resistance. (a) Calculate the speed of the mass just before it touches the spring. (b) Show that the greatest compression \(x\) of the spring satisfies \(60x^2 - 4.9x - 1.5 = 0\). (c) Calculate \(x\).
H: At the lowest point the mass is at rest, so all the lost gravitational potential energy is stored in the spring.
H: The mass falls a total distance \(0.30 + x\).
A: (a) \(v = \sqrt{2gh} = \sqrt{2 \times 9.81 \times 0.30}\) [C1] \(= 2.4\,\mathrm{m\,s^{-1}}\). [A1] (b) Loss of gravitational energy = energy stored in the spring: \(mg(0.30 + x) = \tfrac12 kx^2\). [M1] \(0.50 \times 9.81 \times (0.30 + x) = 60x^2\), so \(60x^2 - 4.9x - 1.5 = 0\). [A1] (c) \(x = \dfrac{4.9 + \sqrt{4.9^2 + 4 \times 60 \times 1.5}}{2 \times 60}\) [C1] \(= 0.20\,\mathrm{m}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ In a Young modulus experiment, the following are measured: original length \(L = 2.500 \pm 0.005\,\mathrm{m}\), diameter \(d = 0.400 \pm 0.005\,\mathrm{mm}\), and a load \(F = 25.0 \pm 0.2\,\mathrm{N}\) produces an extension \(x = 2.50 \pm 0.05\,\mathrm{mm}\). (a) Calculate the Young modulus. (b) Calculate the percentage uncertainty in the value. (c) State which measurement makes the largest contribution to the uncertainty, and suggest an improvement.
H: \(E = \dfrac{4FL}{\pi d^2 x}\): the diameter is squared, so its percentage uncertainty is doubled.
H: Add the percentage uncertainties of \(F\), \(L\), \(x\) and twice that of \(d\).
A: (a) \(E = \dfrac{4FL}{\pi d^2 x} = \dfrac{4 \times 25.0 \times 2.500}{\pi \times (0.400 \times 10^{-3})^2 \times 2.50 \times 10^{-3}}\) [C1] \(= 1.99 \times 10^{11}\,\mathrm{Pa}\). [A1] (b) Percentage uncertainties: \(F\): 0.8%, \(L\): 0.2%, \(d\): 1.25%, counted twice as 2.5%, \(x\): 2.0%. [M1] Total \(= 0.8 + 0.2 + 2.5 + 2.0 = 5.5\%\), so \(E = (2.0 \pm 0.1) \times 10^{11}\,\mathrm{Pa}\). [A1] (c) The diameter contributes most (2.5%). [B1] Take many micrometer readings along the wire and average them, or use a larger extension (a longer or thinner wire, within the limit of proportionality) to reduce the percentage uncertainty in \(x\). [B1]
Q: [6 marks] ★★★ Two springs of spring constants \(60\,\mathrm{N\,m^{-1}}\) and \(90\,\mathrm{N\,m^{-1}}\) are connected side by side (in parallel). This pair is connected end to end (in series) with a third spring of spring constant \(100\,\mathrm{N\,m^{-1}}\), and a load of 12 N hangs from the arrangement. (a) Calculate the spring constant of the whole arrangement. (b) Calculate its extension. (c) Calculate the extension of the parallel pair and of the third spring. (d) Calculate the total energy stored.
H: The parallel pair behaves as one spring of constant \(k_1 + k_2\). Then treat two springs in series.
H: In a series arrangement the same force acts in each part, and the extensions add.
A: (a) The parallel pair has \(k = 60 + 90 = 150\,\mathrm{N\,m^{-1}}\). [C1] In series with 100: \(\dfrac{150 \times 100}{150 + 100} = 60\,\mathrm{N\,m^{-1}}\). [A1] (b) \(x = F/k = 12/60 = 0.20\,\mathrm{m}\). [A1] (c) Pair: \(12/150 = 0.080\,\mathrm{m}\); third spring: \(12/100 = 0.12\,\mathrm{m}\) (together 0.20 m). [A1] (d) \(E_\mathrm{P} = \tfrac12 Fx = \tfrac12 \times 12 \times 0.20\) [C1] \(= 1.2\,\mathrm{J}\). [A1]
:::

:::quiz
? A copper wire and a steel wire have the same length and the same diameter, and carry the same load. Which quantity is the same in both wires?
+ The stress
- The strain
- The extension
- The Young modulus
> Stress is \(F/A\), which depends only on the load and the area, so it is the same. The steel wire has a larger Young modulus, so it has a smaller strain and a smaller extension.
? What is the unit of strain?
- Pa
- m
- N m⁻¹
+ It has no unit.
> Strain is extension divided by original length, a ratio of two lengths. Pa is the unit of stress, and N m⁻¹ is the unit of spring constant.
? The diameter of a wire is doubled, the load and the material staying the same. What happens to the stress in the wire?
- It doubles.
+ It becomes four times smaller.
- It halves.
- It stays the same.
> The area is proportional to the diameter squared, so doubling the diameter makes the area four times larger, and \(\sigma = F/A\) is four times smaller.
? A spring with \(k = 100\,\mathrm{N\,m^{-1}}\) is extended by 0.10 m. What energy is stored?
- 10 J
- 1.0 J
+ 0.50 J
- 5.0 J
> \(E_\mathrm{P} = \tfrac12 kx^2 = 0.5 \times 100 \times 0.01 = 0.50\,\mathrm{J}\). 1.0 J is \(Fx\), which forgets the half because the force rises from zero.
? On a force–extension graph, what does the area under the line represent?
+ The work done in stretching (the energy stored, if the deformation is elastic)
- The spring constant
- The Young modulus
- The extension
> Work is force multiplied by distance moved in the direction of the force, so the area under the graph is the work done. The spring constant is the gradient.
? A metal wire is stretched beyond its elastic limit and then the load is removed. What happens?
- It returns to its original length.
+ It is left with a permanent extension.
- It breaks.
- It becomes shorter than its original length.
> Beyond the elastic limit the deformation is plastic, so some extension remains after the load is removed. The wire does not necessarily break.
? Two identical springs are connected in parallel. How does the combination compare with one spring?
- It is half as stiff.
+ It is twice as stiff.
- It has the same stiffness.
- It is four times as stiff.
> In parallel the load is shared, so for a given load each spring extends by half as much. The combination has \(k = k_1 + k_2 = 2k\).
:::

:::checklist What you can now do
- [ ] I can explain that deformation is caused by tensile or compressive forces, and use the terms load, extension, compression and limit of proportionality.
- [ ] I can state and use Hooke's law and the spring constant \(k = F/x\).
- [ ] I can define and use stress, strain and the Young modulus, and find \(E\) from the gradient of a stress–strain graph.
- [ ] I can describe an experiment to determine the Young modulus of a metal wire.
- [ ] I can distinguish elastic from plastic deformation and the elastic limit from the limit of proportionality.
- [ ] I can explain that the area under a force–extension graph is the work done, and find the energy dissipated when a wire is loaded past its elastic limit and unloaded.
- [ ] I can find elastic potential energy from the area under a graph and use \(E_\mathrm{P} = \tfrac12 Fx = \tfrac12 kx^2\).
:::

:::recap
- Load causes extension (tension) or compression. Hooke's law: extension is proportional to load up to the limit of proportionality; \(F = kx\), and \(k\) (N m⁻¹) belongs to the object.
- Stress \(\sigma = F/A\) (Pa). Strain \(\varepsilon = x/L\) (no unit). Young modulus \(E = \sigma/\varepsilon = FL/(Ax)\) (Pa), a property of the material: the gradient of a stress–strain graph.
- Young modulus experiment: a long thin wire, \(L\) with a rule, \(d\) with a micrometer in several places, add loads in steps, plot \(F\) against \(x\), \(E = \text{gradient} \times L/A\).
- Elastic: returns to its original length when the load is removed. Plastic: permanent extension. Beyond the elastic limit, unloading follows a line parallel to the original straight line.
- Area under the force–extension graph = work done. Past the elastic limit, the area between the loading curve and the unloading line is dissipated. Within the limit of proportionality: \(E_\mathrm{P} = \tfrac12 Fx = \tfrac12 kx^2\).
- Springs: series \(1/k = 1/k_1 + 1/k_2\); parallel \(k = k_1 + k_2\).
:::

:::links
- explore: [Hooke's Law](https://phet.colorado.edu/en/simulations/hookes-law) · PhET · stretch and compress springs, and see force, energy and the spring constant change together
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the deformation of solids questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Waves](#phys.waves)
