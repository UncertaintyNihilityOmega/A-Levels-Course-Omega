@chapter phys.units
@title Physical quantities, units and uncertainty
@level as
@paper CAIE P1 · P2 · P3 (AS)
@time 5–7 hours
@summary What a physical quantity is, the SI base and derived units and how to check an equation with them, unit prefixes and estimates, systematic and random errors with uncertainties added by simple rules, and scalars and vectors with their addition, subtraction and components.

:::why
Physics is the science of measurement, and a measurement is only useful if you know what it is measured in, how well you know it and, for some quantities, which way it points. This chapter gives you the language every other chapter relies on: units you can check an equation with, a way to say how far a result can be trusted, and vectors for everything that has a direction. The marks it earns are quiet ones, such as a missing unit or an uncertainty added the wrong way, and they decide the difference between an A and an A*.
:::

**Before you start**, you need only IGCSE-level ideas. If standard form or rearranging equations feels rusty, spend ten minutes on [Physics from zero](#phys.f.basics) and [Indices, surds and standard form](#math.f.powers).

:::try Warm-up
Q: Write 3.5 km in metres, in standard form. (from [Physics from zero](#phys.f.basics))
A: \(3.5\,\mathrm{km} = 3.5 \times 10^{3}\,\mathrm{m}\), because "kilo" means \(\times 1000\).
Q: Rearrange \(v = s/t\) to make \(t\) the subject. (from [Physics from zero](#phys.f.basics))
A: Multiply both sides by \(t\) and divide by \(v\): \(t = s/v\).
Q: A right-angled triangle has shorter sides 6.0 cm and 8.0 cm. Find the hypotenuse. (from [Geometry and trigonometry basics](#math.f.geometry))
A: By Pythagoras, \(\sqrt{6.0^2 + 8.0^2} = \sqrt{100} = 10\,\mathrm{cm}\).
:::

## Physical quantities and their units

Every number in physics describes something. "5.0" alone means nothing: it could be 5.0 seconds, 5.0 kilograms or 5.0 volts. A **physical quantity** is anything you can measure, and it always has two parts: a **numerical magnitude** and a **unit**.

\[\text{physical quantity} = \text{numerical magnitude} \times \text{unit}\]

For example, the length of a desk is \(1.20\,\mathrm{m}\). The number is 1.20, the unit is the metre, and the product is the length. The same length is \(120\,\mathrm{cm}\) or \(1200\,\mathrm{mm}\). The quantity does not change when you change the unit. Only the number changes, and it changes in exactly the way that keeps the product the same.

This idea explains the way Cambridge writes **tables and graph axes**. A column heading such as \(v\,/\,\mathrm{m\,s^{-1}}\) is read "\(v\) divided by metres per second", and it means that the numbers in the column are the values of \(v\) divided by the unit. So an entry of 3.2 means \(v = 3.2\,\mathrm{m\,s^{-1}}\). You will write headings and axis labels in this form throughout the course, and you must always include the unit in them.

:::warn A number without a unit
A final answer with no unit, or the wrong unit, loses the final accuracy mark, even when the number is right. In 1999 a spacecraft was lost at Mars because one team's software produced a value in pound-force seconds where another team's software expected newton seconds. Mistakes with units are not just exam mistakes. Write the unit on every line of working that has a unit, and you will catch many errors before they reach the answer.
:::

## SI base units

Physicists around the world use the same system of units, the **SI** (from the French *Système International*). It starts from a small set of **base quantities**, each with a **base unit**, and builds every other unit from them.

:::def Base quantity and base unit
A base quantity is one of the quantities from which all other quantities are built; each has a base unit defined independently of all other units. The five you must recall are in the table below.
:::

| Base quantity | Symbol | Base unit | Unit symbol |
|---|---|---|---|
| mass | \(m\) | kilogram | kg |
| length | \(l\), \(x\) | metre | m |
| time | \(t\) | second | s |
| electric current | \(I\) | ampere | A |
| thermodynamic temperature | \(T\) | kelvin | K |

The SI has two more base units, the **mole** (amount of substance, symbol mol) and the **candela** (luminous intensity). The mole appears in [Ideal gases](#phys.gases); you will not need the candela.

Notice that the **kilogram**, not the gram, is the base unit of mass. This matters whenever you use an equation such as \(F = ma\) or \(E_\mathrm{k} = \tfrac12 mv^2\): the mass must be in kilograms, or the answer will not come out in newtons or joules. Notice too that temperature in the base-unit sense is in **kelvin**. A temperature difference of 1 K equals a difference of \(1\,^\circ\mathrm{C}\), but the two scales start at different places.

### Derived units

Every other unit is a **derived unit**: it is made by multiplying or dividing base units.

:::def Derived unit
A unit formed by multiplying and/or dividing base units (and possibly using no other units). Some derived units have a special name, such as the newton or the joule.
:::

You do not need to memorise a list. You need one method, which works for every quantity in the syllabus.

:::steps
1. Write down an equation that **defines** the quantity, one with the quantity alone on the left (for example \(F = ma\)).
2. Replace each symbol on the right with its unit. Use base units, or units you have already found.
3. Simplify. Combine powers of the same base unit, and write negative powers instead of fractions (\(\mathrm{m\,s^{-2}}\), not \(\mathrm{m/s^2}\)).
:::

Here is the method applied to the units you will meet most often.

| Quantity | Defining equation | Special name | Base units |
|---|---|---|---|
| speed, velocity | \(v = s/t\) | none | \(\mathrm{m\,s^{-1}}\) |
| acceleration | \(a = \Delta v/t\) | none | \(\mathrm{m\,s^{-2}}\) |
| force | \(F = ma\) | newton, N | \(\mathrm{kg\,m\,s^{-2}}\) |
| pressure | \(p = F/A\) | pascal, Pa | \(\mathrm{kg\,m^{-1}\,s^{-2}}\) |
| work, energy | \(W = Fs\) | joule, J | \(\mathrm{kg\,m^{2}\,s^{-2}}\) |
| power | \(P = W/t\) | watt, W | \(\mathrm{kg\,m^{2}\,s^{-3}}\) |
| charge | \(Q = It\) | coulomb, C | \(\mathrm{A\,s}\) |
| potential difference | \(V = W/Q\) | volt, V | \(\mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}\) |
| resistance | \(R = V/I\) | ohm, Ω | \(\mathrm{kg\,m^{2}\,s^{-3}\,A^{-2}}\) |
| frequency | \(f = 1/T\) | hertz, Hz | \(\mathrm{s^{-1}}\) |
| density | \(\rho = m/V\) | none | \(\mathrm{kg\,m^{-3}}\) |

:::eg Show that the base units of the pascal are \(\mathrm{kg\,m^{-1}\,s^{-2}}\).
Pressure is force per unit area, \(p = F/A\). [C1]

The newton is the unit of force, and \(F = ma\) gives \(\mathrm{N} = \mathrm{kg} \times \mathrm{m\,s^{-2}} = \mathrm{kg\,m\,s^{-2}}\). [B1]

Area is a length squared, with unit \(\mathrm{m^2}\). Dividing:
\[\mathrm{Pa} = \frac{\mathrm{kg\,m\,s^{-2}}}{\mathrm{m^{2}}} = \mathrm{kg\,m^{-1}\,s^{-2}}\] [A1]
:::

:::eg Find the base units of the volt, using \(V = W/Q\).
The joule is the unit of work, \(W = Fs\), so \(\mathrm{J} = \mathrm{kg\,m\,s^{-2}} \times \mathrm{m} = \mathrm{kg\,m^{2}\,s^{-2}}\). [C1]

The coulomb comes from \(Q = It\), so \(\mathrm{C} = \mathrm{A\,s}\). [B1]

Dividing the joule by the coulomb:
\[\mathrm{V} = \frac{\mathrm{kg\,m^{2}\,s^{-2}}}{\mathrm{A\,s}} = \mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}\] [A1]
Because \(R = V/I\), the ohm is one more division by the ampere: \(\mathrm{kg\,m^{2}\,s^{-3}\,A^{-2}}\).
:::

:::exam Writing units in answers
Write units with negative indices (\(\mathrm{m\,s^{-1}}\)), not with a slash, and put a space between different units so that they cannot be read as one symbol: "m s⁻¹" is metres per second, but "ms⁻¹" would be "per millisecond". Never mix capital and small letters: the unit named after a person has a capital symbol (N, J, W, Pa, C, V, Ω, Hz), but its written-out name is lower case (newton, joule).
:::

## Homogeneous equations

An equation in physics is a statement that two things are the same. For that to make sense, both sides must be the same kind of thing: you cannot say that a length equals a time. That is a test you can run on any equation.

:::def Homogeneous equation
An equation in which every term has the same base units. In a homogeneous equation both sides have the same base units, and every quantity that is added or subtracted has the same base units as the others.
:::

To check an equation, replace every quantity with its base units and simplify each term separately. If every term comes out the same, the equation is homogeneous.

:::eg Show that the equation \(s = ut + \tfrac12 at^2\) is homogeneous.
Here \(s\) is displacement, \(u\) is initial velocity, \(a\) is acceleration and \(t\) is time.

Left-hand side: \(s\) has unit m. [B1]

First term on the right: \(ut\) has unit \(\mathrm{m\,s^{-1}} \times \mathrm{s} = \mathrm{m}\). [B1]

Second term on the right: \(\tfrac12 at^2\) has unit \(\mathrm{m\,s^{-2}} \times \mathrm{s^2} = \mathrm{m}\) (the \(\tfrac12\) has no unit). [B1]

Every term has the unit m, so the equation is homogeneous. [B1]
:::

:::eg The time period of a simple pendulum of length \(l\) is given by \(T = 2\pi\sqrt{l/g}\). Show that this is homogeneous.
The left side has unit s. [B1]

On the right, \(2\pi\) has no unit. Inside the root, \(l/g\) has unit \(\mathrm{m}/(\mathrm{m\,s^{-2}}) = \mathrm{s^{2}}\). [C1]

The square root of \(\mathrm{s^2}\) is s, so both sides have the unit s. [A1]
:::

:::key What homogeneity can and cannot tell you
**It can** show that an equation is wrong: if the two sides have different base units, the equation cannot be correct. It can also find the unit of an unknown constant, and it can suggest the form of an equation.

**It cannot** prove an equation is right. A homogeneous equation can still be false, because the test cannot see a number or a missing factor. The equation \(s = ut + at^2\) is homogeneous, but the true equation has \(\tfrac12 at^2\). The test also cannot see the difference between two quantities with the same unit, such as work and torque.

Arguments of functions such as \(\sin\), \(\ln\) and \(e^x\) must have **no unit**, so in \(N = N_0 e^{-\lambda t}\) the product \(\lambda t\) must be a pure number.
:::

:::eg The drag force on a car is modelled by \(F = kAv^2\), where \(A\) is the cross-sectional area of the car and \(v\) its speed. Find the base units of \(k\).
Make \(k\) the subject: \(k = \dfrac{F}{Av^{2}}\). [C1]

Substitute base units, with \(F\) in \(\mathrm{kg\,m\,s^{-2}}\), \(A\) in \(\mathrm{m^2}\) and \(v^2\) in \(\mathrm{m^{2}\,s^{-2}}\):
\[k = \frac{\mathrm{kg\,m\,s^{-2}}}{\mathrm{m^{2}} \times \mathrm{m^{2}\,s^{-2}}} = \mathrm{kg\,m^{-3}}\] [A1]
These are the units of density, which is no accident. Drag depends on how much air mass the car pushes aside, so \(k\) is closely related to the density of air.
:::

Homogeneity can even find an unknown power. If you suspect that the speed \(v\) of a wave on a stretched string depends on the tension \(T\) and the mass per unit length \(\mu\), try \(v = kT^{x}\mu^{y}\), where \(k\) is a number with no unit.

:::eg Use base units to find \(x\) and \(y\) in \(v = kT^x\mu^y\), where \(T\) is the tension in the string and \(\mu\) its mass per unit length.
The unit of \(v\) is \(\mathrm{m\,s^{-1}}\), of \(T\) is \(\mathrm{kg\,m\,s^{-2}}\), and of \(\mu\) is \(\mathrm{kg\,m^{-1}}\). [B1]

Match each base unit on the two sides:
\[\begin{aligned} \text{kg:}\quad & 0 = x + y \\ \text{m:}\quad & 1 = x - y \\ \text{s:}\quad & -1 = -2x \end{aligned}\] [M1]
The last line gives \(x = \tfrac12\). Then \(y = -\tfrac12\), which also satisfies the middle line. [A1]
So \(v = k\sqrt{T/\mu}\). Experiments show that \(k = 1\). Homogeneity found the form of the equation, but only an experiment or a derivation can fix the number.
:::

## Prefixes and standard form

Base units are often awkward: a cell's diameter is far smaller than a metre, and the distance to a star is far larger. A **prefix** in front of a unit multiplies it by a power of ten.

| Prefix | Symbol | Factor | Example |
|---|---|---|---|
| pico | p | \(10^{-12}\) | a capacitance of 47 pF |
| nano | n | \(10^{-9}\) | a wavelength of 550 nm |
| micro | μ | \(10^{-6}\) | a red blood cell, about 7 μm wide |
| milli | m | \(10^{-3}\) | a current of 5 mA |
| centi | c | \(10^{-2}\) | a length of 2.5 cm |
| deci | d | \(10^{-1}\) | 1 dm³ is one litre |
| kilo | k | \(10^{3}\) | a resistance of 4.7 kΩ |
| mega | M | \(10^{6}\) | a frequency of 5 MHz |
| giga | G | \(10^{9}\) | a clock speed of 3 GHz |
| tera | T | \(10^{12}\) | a frequency of 1 THz |

A prefix belongs to the unit it is written on, so it is part of the unit symbol. This is why prefixes behave in a surprising way when a unit is **squared or cubed**. The square applies to the whole unit, prefix included:
\[1\,\mathrm{mm^{2}} = (10^{-3}\,\mathrm{m})^{2} = 10^{-6}\,\mathrm{m^{2}} \qquad 1\,\mathrm{cm^{3}} = (10^{-2}\,\mathrm{m})^{3} = 10^{-6}\,\mathrm{m^{3}}\]
Beginners who write \(1\,\mathrm{mm^2} = 10^{-3}\,\mathrm{m^2}\) are wrong by a factor of a thousand. A cubic centimetre is 10⁻⁶ of a cubic metre, not 10⁻².

:::warn mm and m s
A space changes the meaning. "ms" is a millisecond, one thousandth of a second. "m s" is a metre multiplied by a second. Likewise "mm" is millimetre but "m m" would be a metre squared. Also keep apart the lower-case m (milli), the capital M (mega) and the capital T (tera, \(10^{12}\), not the tesla): \(5\,\mathrm{mN}\) is a small force and \(5\,\mathrm{MN}\) is a huge one.
:::

:::eg Convert (a) 0.35 mm² to m², (b) 2.4 cm³ to m³ and (c) a density of 8.96 g cm⁻³ to kg m⁻³. Give each answer in standard form.
(a) \(1\,\mathrm{mm^{2}} = 10^{-6}\,\mathrm{m^{2}}\), so \(0.35\,\mathrm{mm^{2}} = 0.35 \times 10^{-6} = 3.5 \times 10^{-7}\,\mathrm{m^{2}}\). [A1]

(b) \(1\,\mathrm{cm^{3}} = 10^{-6}\,\mathrm{m^{3}}\), so \(2.4\,\mathrm{cm^{3}} = 2.4 \times 10^{-6}\,\mathrm{m^{3}}\). [A1]

(c) \(1\,\mathrm{g} = 10^{-3}\,\mathrm{kg}\) and \(1\,\mathrm{cm^{3}} = 10^{-6}\,\mathrm{m^{3}}\). The cube is on the bottom, so
\[8.96\,\mathrm{g\,cm^{-3}} = 8.96 \times \frac{10^{-3}\,\mathrm{kg}}{10^{-6}\,\mathrm{m^{3}}} = 8.96 \times 10^{3}\,\mathrm{kg\,m^{-3}}\] [A1]
A quick rule: to change a density from g cm⁻³ to kg m⁻³, multiply by 1000.
:::

:::eg A car travels at \(72\,\mathrm{km\,h^{-1}}\). Express this speed in \(\mathrm{m\,s^{-1}}\). A source of red light has wavelength 650 nm. Calculate its frequency, using \(c = f\lambda\).
Speed: \(1\,\mathrm{km} = 10^{3}\,\mathrm{m}\) and \(1\,\mathrm{h} = 3600\,\mathrm{s}\), so
\[72\,\mathrm{km\,h^{-1}} = \frac{72 \times 10^{3}\,\mathrm{m}}{3600\,\mathrm{s}} = 20\,\mathrm{m\,s^{-1}}\]
(Dividing a speed in km h⁻¹ by 3.6 gives m s⁻¹.)

Light: \(\lambda = 650 \times 10^{-9} = 6.50 \times 10^{-7}\,\mathrm{m}\), and with \(c = 3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\),
\[f = \frac{c}{\lambda} = \frac{3.00 \times 10^{8}}{6.50 \times 10^{-7}} = 4.62 \times 10^{14}\,\mathrm{Hz}\]
Always convert to base units *before* you substitute, or the answer will have the wrong power of ten.
:::

The tool below converts between units and prefixes, writes numbers in standard form, and shows the base units of derived units like the newton and the farad. Use it to check your own conversions, not to replace them: in the exam you will have only your own working.

:::html
<div class="widget" data-w="units" data-tab="prefix"></div>
:::

## Making estimates

Some questions ask you to **estimate** a quantity, which means calculating a rough answer from sensible values that you choose. The aim is the right order of magnitude (the right power of ten), and a good estimate is usually within a factor of 3 of the real value. To estimate well, you need a store of reference values.

| Quantity | Typical value |
|---|---|
| mass of an adult | 70 kg |
| mass of an apple | 0.1 kg |
| height of a room | 3 m |
| walking speed | \(1.5\,\mathrm{m\,s^{-1}}\) |
| car on a motorway | \(30\,\mathrm{m\,s^{-1}}\) |
| speed of sound in air | \(340\,\mathrm{m\,s^{-1}}\) |
| diameter of an atom | \(10^{-10}\,\mathrm{m}\) |
| diameter of a nucleus | \(10^{-15}\,\mathrm{m}\) |
| wavelength of visible light | 400 nm to 700 nm |
| power of a kettle | 2 kW |
| power of a lamp | 10 W to 60 W |
| mains voltage (UK) | 230 V |
| current in a household device | 0.1 A to 10 A |
| atmospheric pressure | \(1.0 \times 10^{5}\,\mathrm{Pa}\) |
| density of water | \(1000\,\mathrm{kg\,m^{-3}}\) |
| density of air | \(1.2\,\mathrm{kg\,m^{-3}}\) |

:::steps
1. Decide which formula links what you want to what you can estimate.
2. Estimate each input from a reference value, rounded to one or two significant figures.
3. Substitute in base units, calculate, and give the answer to one or two significant figures.
4. Ask whether the answer is sensible. A 70 kg sprinter with a kinetic energy of 3 J has gone wrong.
:::

:::eg Estimate the kinetic energy of a sprinter in a 100 m race.
A sprinter's mass is about 70 kg. The world's best sprinters cover 100 m in just under 10 s, so a good athlete's top speed is about \(10\,\mathrm{m\,s^{-1}}\). [B1]

\[E_\mathrm{k} = \tfrac12 mv^2 = \tfrac12 \times 70 \times 10^2 = 3500\,\mathrm{J}\] [C1]
So the kinetic energy is of the order of \(4\,\mathrm{kJ}\) (\(3.5 \times 10^{3}\,\mathrm{J}\)). [A1]
The exact figure does not matter: any answer from about 2 kJ to 6 kJ shows the right order of magnitude.
:::

:::eg Estimate the mass of air in a classroom.
A classroom is about 8 m long, 6 m wide and 3 m high, so its volume is \(8 \times 6 \times 3 = 144\,\mathrm{m^{3}}\), about \(1.4 \times 10^{2}\,\mathrm{m^{3}}\). [B1]

The density of air is about \(1.2\,\mathrm{kg\,m^{-3}}\), so \(m = \rho V = 1.2 \times 144 = 173\,\mathrm{kg}\). [C1]
The mass of air is of the order of \(2 \times 10^{2}\,\mathrm{kg}\), about the mass of three adults. [A1]
:::

## Errors and uncertainties

No measurement is perfect. The difference between a measurement and the true value is an **error**, and physicists classify errors by how they behave when a measurement is repeated.

:::def Random error
An error that causes readings to be scattered unpredictably about the true value. Its effect is reduced by repeating the readings and taking an average.
:::

:::def Systematic error
An error that makes all readings differ from the true value by the same amount, or in the same proportion, in the same direction. It cannot be reduced by repeating the readings.
:::

:::cols
:::col Random errors
Readings scatter above and below the true value.

Causes: human reaction time, reading a scale by eye, small changes in the surroundings.

Reduce by taking **many readings** and averaging. Never removed completely.
:::
:::col Systematic errors
All readings are shifted the same way: all too high, or all too low.

Causes: a **zero error**, a wrongly calibrated instrument, a reaction time that is always late, a ruler that has shrunk.

Repeating does **not** help. Find the cause and correct for it.
:::
:::

A **zero error** is the most common systematic error. It happens when an instrument does not read zero when it should. A micrometer that shows \(+0.02\,\mathrm{mm}\) with its jaws closed makes every reading 0.02 mm too large, and a top-pan balance that reads \(-0.3\,\mathrm{g}\) with nothing on it makes every mass too small by 0.3 g. The correction is to subtract the zero reading from every measurement, taking its sign into account.

:::eg A micrometer reads \(+0.03\,\mathrm{mm}\) when its jaws are closed. A student measures a wire five times and gets 0.62, 0.63, 0.62, 0.61 and 0.63 mm. Find the corrected diameter, and say what type of error the zero error is.
Mean reading: \(\dfrac{0.62 + 0.63 + 0.62 + 0.61 + 0.63}{5} = 0.622\,\mathrm{mm}\). [C1]

The reading is too large by the zero error, so subtract it: \(0.622 - 0.03 = 0.592 \approx 0.59\,\mathrm{mm}\). [A1]

The zero error is a **systematic error**, because it shifts every reading by the same amount in the same direction, so averaging cannot remove it. [B1]
(If the micrometer had read \(-0.03\,\mathrm{mm}\), you would add 0.03 mm.)
:::

### Precision and accuracy

Everyday speech uses "precise" and "accurate" as if they meant the same thing. In physics they do not.

:::def Precision
How close repeated readings are to each other. High precision means small scatter, and it is a property of the measurements themselves; it says nothing about the true value.
:::

:::def Accuracy
How close a measured value (or the mean of readings) is to the true value.
:::

Imagine shooting at a target. The bullseye is the true value and each dot is a reading.

:::html
<figure class="fig"><svg viewBox="0 0 560 335" role="img" aria-label="Four targets. Top left: dots tightly grouped at the centre, precise and accurate. Top right: dots tightly grouped but away from the centre, precise but not accurate. Bottom left: dots widely scattered around the centre, accurate on average but not precise. Bottom right: dots widely scattered and off-centre, neither precise nor accurate."><circle class="fm s-mute sw1" cx="140" cy="75" r="60"/><circle class="ln-m" cx="140" cy="75" r="40"/><circle class="ln-m" cx="140" cy="75" r="20"/><circle class="fi" cx="140" cy="75" r="2.5"/><circle class="fa s-ink sw1" cx="134" cy="79" r="4.5"/><circle class="fa s-ink sw1" cx="145" cy="68" r="4.5"/><circle class="fa s-ink sw1" cx="148" cy="80" r="4.5"/><circle class="fa s-ink sw1" cx="137" cy="70" r="4.5"/><circle class="fa s-ink sw1" cx="142" cy="83" r="4.5"/><text class="tl tc" x="140" y="158">precise and accurate</text><circle class="fm s-mute sw1" cx="420" cy="75" r="60"/><circle class="ln-m" cx="420" cy="75" r="40"/><circle class="ln-m" cx="420" cy="75" r="20"/><circle class="fi" cx="420" cy="75" r="2.5"/><circle class="fa s-ink sw1" cx="448" cy="45" r="4.5"/><circle class="fa s-ink sw1" cx="456" cy="49" r="4.5"/><circle class="fa s-ink sw1" cx="452" cy="41" r="4.5"/><circle class="fa s-ink sw1" cx="458" cy="45" r="4.5"/><circle class="fa s-ink sw1" cx="450" cy="51" r="4.5"/><text class="tl tc" x="420" y="158">precise but not accurate</text><circle class="fm s-mute sw1" cx="140" cy="235" r="60"/><circle class="ln-m" cx="140" cy="235" r="40"/><circle class="ln-m" cx="140" cy="235" r="20"/><circle class="fi" cx="140" cy="235" r="2.5"/><circle class="fa s-ink sw1" cx="102" cy="245" r="4.5"/><circle class="fa s-ink sw1" cx="170" cy="203" r="4.5"/><circle class="fa s-ink sw1" cx="182" cy="255" r="4.5"/><circle class="fa s-ink sw1" cx="120" cy="195" r="4.5"/><circle class="fa s-ink sw1" cx="145" cy="273" r="4.5"/><text class="tl tc" x="140" y="318">accurate (on average) but not precise</text><circle class="fm s-mute sw1" cx="420" cy="235" r="60"/><circle class="ln-m" cx="420" cy="235" r="40"/><circle class="ln-m" cx="420" cy="235" r="20"/><circle class="fi" cx="420" cy="235" r="2.5"/><circle class="fa s-ink sw1" cx="372" cy="243" r="4.5"/><circle class="fa s-ink sw1" cx="405" cy="275" r="4.5"/><circle class="fa s-ink sw1" cx="380" cy="270" r="4.5"/><circle class="fa s-ink sw1" cx="400" cy="247" r="4.5"/><circle class="fa s-ink sw1" cx="410" cy="261" r="4.5"/><text class="tl tc" x="420" y="318">neither precise nor accurate</text></svg><figcaption>The bullseye is the true value and each dot is one reading. Precision is about the scatter of the dots. Accuracy is about how close their average is to the bullseye. The top-right target is the signature of a systematic error.</figcaption></figure>
:::

A systematic error damages **accuracy** (the readings are consistently off) but not precision. A random error damages **precision**. A set of readings that are all close together can be badly wrong, for example 12.31, 12.30, 12.32, 12.31 seconds for a time that should be 12.00 s, when the stopwatch runs slow. Close together means precise. Wrong means inaccurate.

:::warn Precise does not mean accurate
Many answers lose marks by saying "the readings are close to each other, so the results are accurate". Close to each other is precision. To judge accuracy, you must compare with a true or accepted value.
:::

### Uncertainty

You cannot know a measured value exactly, so you quote how far it might be from the true value.

:::def Uncertainty
The range of values within which the true value of a measured quantity is expected to lie. It is written as \(x \pm \Delta x\), where \(\Delta x\) is the **absolute uncertainty** and has the same unit as \(x\).
:::

Three ways of writing an uncertainty are in use, and you must be able to move between them.

:::formula Absolute, fractional and percentage uncertainty
\[\text{fractional uncertainty} = \frac{\Delta x}{x} \qquad\qquad \text{percentage uncertainty} = \frac{\Delta x}{x} \times 100\%\]
\(x\): the measured value · \(\Delta x\): the absolute uncertainty, in the same unit as \(x\). The fractional and percentage uncertainties have no unit.
:::

How big is \(\Delta x\)? It depends on how you measured.

- **One reading on a digital instrument**: at least plus or minus one in the last digit shown.
- **One reading on an analogue scale**: about half the smallest division, for each reading you make. A length from a ruler needs two readings (both ends), so \(\pm 1\,\mathrm{mm}\) is a sensible uncertainty for a length measured with a millimetre ruler.
- **Repeated readings**: the mean is the best value, and a good estimate of the uncertainty is **half the range** (the largest reading minus the smallest, divided by 2).
- **A timing by hand**: reaction time, around \(\pm 0.2\,\mathrm{s}\), unless you have a better reason.

Any sensible value is acceptable if you give a reason. What is not sensible is an uncertainty smaller than the resolution of the instrument.

:::eg Five timings of a trolley are 2.31 s, 2.35 s, 2.28 s, 2.33 s and 2.30 s. Give the time with its absolute and percentage uncertainty.
Mean: \(\dfrac{2.31 + 2.35 + 2.28 + 2.33 + 2.30}{5} = 2.314\,\mathrm{s}\). [C1]

Half the range: \(\dfrac{2.35 - 2.28}{2} = 0.035\,\mathrm{s}\), which is \(0.04\,\mathrm{s}\) to one significant figure. [C1]

So \(t = (2.31 \pm 0.04)\,\mathrm{s}\), where the value is given to the same number of decimal places as the uncertainty. [A1]

Percentage uncertainty: \(\dfrac{0.04}{2.31} \times 100\% = 1.7\%\). [A1]
:::

:::key How to write a final answer
Give the uncertainty to **one** significant figure (two at most), and give the value to the **same number of decimal places** as its uncertainty.

\((2.70 \pm 0.05)\,\mathrm{g\,cm^{-3}}\) is correct. \((2.7043 \pm 0.05)\,\mathrm{g\,cm^{-3}}\) has too many figures in the value, and \((2.7 \pm 0.0512)\,\mathrm{g\,cm^{-3}}\) has too many in the uncertainty. Both lose marks.
:::

### Uncertainty in a derived quantity

Most results come from a calculation, so the uncertainties in the measurements pass into the answer. The syllabus uses a simple rule, called **simple addition**: you add uncertainties. You never subtract them, because the aim is to find the largest the uncertainty could reasonably be.

:::formula Combining uncertainties
**Sum or difference** \(z = x + y\) or \(z = x - y\): add the absolute uncertainties. \(\Delta z = \Delta x + \Delta y\).

**Product or quotient** \(z = xy\) or \(z = x/y\): add the percentage (or fractional) uncertainties. \(\dfrac{\Delta z}{z} = \dfrac{\Delta x}{x} + \dfrac{\Delta y}{y}\).

**Power** \(z = x^{n}\): multiply the percentage uncertainty by \(|n|\). \(\dfrac{\Delta z}{z} = |n|\dfrac{\Delta x}{x}\).

A **constant** such as \(\pi\) or 2 has no uncertainty. A quantity in a product that is repeated (\(x\) and \(x\) again) is the same as a power, so the percentage is counted twice.
:::

:::proof Why percentages add for a product
Let \(z = xy\), where \(x\) and \(y\) both have their largest possible values.
The largest value of \(z\) is \((x + \Delta x)(y + \Delta y) = xy + x\,\Delta y + y\,\Delta x + \Delta x\,\Delta y\).
The last term is the product of two small quantities and is far smaller than the others, so ignore it.
The uncertainty in \(z\) is therefore \(\Delta z \approx x\,\Delta y + y\,\Delta x\).
Divide by \(z = xy\): \(\dfrac{\Delta z}{z} = \dfrac{\Delta y}{y} + \dfrac{\Delta x}{x}\).
So the fractional uncertainties add. The same steps with \(z = x/y\) give the same result, because dividing by \(y\) has the same worst case as multiplying.
:::

:::eg A metal cylinder has mass \(m = 112.4 \pm 0.1\,\mathrm{g}\), diameter \(d = 15.00 \pm 0.02\,\mathrm{mm}\) (micrometer) and length \(l = 80.0 \pm 0.1\,\mathrm{mm}\). Find its density and the uncertainty in the density.
The volume of a cylinder is \(V = \dfrac{\pi d^{2} l}{4}\), so \(\rho = \dfrac{m}{V} = \dfrac{4m}{\pi d^{2} l}\). [C1]

Volume: \(V = \dfrac{\pi \times 15.00^{2} \times 80.0}{4} = 14\,137\,\mathrm{mm^{3}} = 14.14\,\mathrm{cm^{3}}\), so \(\rho = \dfrac{112.4}{14.137} = 7.95\,\mathrm{g\,cm^{-3}}\). [A1]

Percentage uncertainties: mass \(\dfrac{0.1}{112.4} = 0.089\%\), diameter \(\dfrac{0.02}{15.00} = 0.133\%\) and length \(\dfrac{0.1}{80.0} = 0.125\%\). [C1]

The diameter is squared, so its percentage counts twice:
\[\frac{\Delta\rho}{\rho} = 0.089\% + 2 \times 0.133\% + 0.125\% = 0.48\%\] [M1]
\[\Delta\rho = 0.0048 \times 7.95 = 0.038 \approx 0.04\,\mathrm{g\,cm^{-3}}\]
\[\rho = (7.95 \pm 0.04)\,\mathrm{g\,cm^{-3}} = (7.95 \pm 0.04) \times 10^{3}\,\mathrm{kg\,m^{-3}}\] [A1]
Notice what dominates: the diameter contributes more than half of the total, because it is squared. To improve this experiment, measure the diameter more carefully first.
:::

:::eg A student times 20 oscillations of a pendulum and records \(31.2 \pm 0.2\,\mathrm{s}\). Find the period and its uncertainty, and explain why timing 20 oscillations is better than timing one.
The period is the time for one oscillation: \(T = \dfrac{31.2}{20} = 1.56\,\mathrm{s}\). [A1]

The 20 is a counted number with no uncertainty, so divide the uncertainty by 20 as well: \(\Delta T = \dfrac{0.2}{20} = 0.01\,\mathrm{s}\). So \(T = (1.56 \pm 0.01)\,\mathrm{s}\). [A1]

If one swing were timed, the reaction-time uncertainty of 0.2 s would apply to 1.56 s: a percentage uncertainty of 13%. With 20 swings it is \(\dfrac{0.2}{31.2} = 0.64\%\). [B1]
Timing many oscillations spreads one fixed uncertainty over many periods, so the percentage uncertainty in the period is much smaller. [B1]
:::

:::eg The length of a bar is measured as \(x = 12.4 \pm 0.2\,\mathrm{cm}\) before it is cut and \(y = 3.5 \pm 0.1\,\mathrm{cm}\) is removed. Find the length that remains, with its uncertainty.
The remaining length is \(x - y = 12.4 - 3.5 = 8.9\,\mathrm{cm}\). [A1]

For a difference, add the **absolute** uncertainties: \(0.2 + 0.1 = 0.3\,\mathrm{cm}\). [C1]
So the length is \((8.9 \pm 0.3)\,\mathrm{cm}\), a percentage uncertainty of 3.4%, which is bigger than that of either measurement (1.6% and 2.9%). [A1]
:::

:::warn Subtracting two nearly equal numbers
The absolute uncertainty of a difference is the sum of the two absolute uncertainties, but the value of the difference is small. So the percentage uncertainty can become enormous. This is why experiments avoid finding a small quantity by subtracting two big ones.
:::

:::lab Measuring the diameter of a wire accurately
:::steps
1. Close the jaws of the micrometer gently with the ratchet and record the **zero error**, with its sign. Check it again at the end.
2. Place the wire between the jaws and tighten only with the ratchet, so that the force is the same each time and the wire is not squashed.
3. Measure the diameter at **three different places** along the wire, and at **two directions at 90°** to each other at each place, because a real wire is rarely perfectly round or uniform.
4. Correct each reading for the zero error and find the mean. Use half the range of the six readings as the uncertainty (or the smallest scale division, if that is larger).
5. Work out the percentage uncertainty. Because the cross-sectional area depends on \(d^{2}\), the percentage uncertainty in the area is twice this.
:::
:::

:::eg Spot the error: the length of a rod is \(25.0 \pm 0.5\,\mathrm{cm}\) and the length of a second rod is \(20.0 \pm 0.4\,\mathrm{cm}\). Find the difference in length, with its uncertainty.
A student wrote this answer.

Line 1: difference \(= 25.0 - 20.0 = 5.0\,\mathrm{cm}\)
Line 2: percentage uncertainties are \(\dfrac{0.5}{25.0} = 2\%\) and \(\dfrac{0.4}{20.0} = 2\%\)
Line 3: total \(= 2\% + 2\% = 4\%\), and \(4\%\) of 5.0 cm is 0.2 cm
Line 4: difference \(= (5.0 \pm 0.2)\,\mathrm{cm}\)

Lines 1 and 2 are correct. [C1] **Line 3 is wrong: for a difference you must add the *absolute* uncertainties, not the percentages. Adding percentages is the rule for a product or quotient.** The final answer mark is lost. [A0]

Correct working: \(\Delta = 0.5 + 0.4 = 0.9\,\mathrm{cm}\), so the difference is \((5.0 \pm 0.9)\,\mathrm{cm}\). The percentage uncertainty is 18%, nearly five times larger than the student's 4%. [A1]
:::

:::board
AQA, OCR and Edexcel IAL teach the same SI system, the same prefixes and the same meanings of systematic error, random error, precision and accuracy. UK boards also usually combine uncertainties at A Level by simple addition, as above.
:::

## Scalars and vectors

Some quantities are completely described by a number and a unit: a mass of 3 kg, a time of 12 s. Others also need a direction: "a force of 10 N" does not say whether it pushes you up or sideways.

:::def Scalar
A quantity that has magnitude only.
:::

:::def Vector
A quantity that has both magnitude and direction.
:::

| Scalars | Vectors |
|---|---|
| distance, speed | displacement, velocity, acceleration |
| mass, time, density | force, weight, momentum |
| energy, work, power | electric field strength |
| temperature, pressure | gravitational field strength |
| charge, potential difference | magnetic flux density (later) |

:::warn Current has a direction, but it is a scalar
Electric current in a wire flows one way round a circuit, but it does not add like a vector at a junction (Kirchhoff's first law adds the numbers). Pressure acts in every direction on a surface, so it too is a scalar. The test is whether the quantity adds by arithmetic or by geometry.
:::

### Adding vectors

Two vectors are added **tip to tail**. Draw the first as an arrow. Start the second where the first ends. The **resultant** is the single arrow from the start of the first to the end of the second, and it has the same effect as the two together. The order does not matter: the sum of the vectors \(\mathbf{a} + \mathbf{b}\) is the same as \(\mathbf{b} + \mathbf{a}\).

A scale drawing works: choose a scale (say 1 cm for 10 N), draw with a ruler and protractor, and measure the resultant. Calculation is faster and more accurate:

- **At 90°:** use Pythagoras for the size, \(R = \sqrt{a^{2} + b^{2}}\), and \(\tan\theta = b/a\) for the angle.
- **At other angles:** use the **cosine rule** \(R^{2} = a^{2} + b^{2} - 2ab\cos C\), where \(C\) is the angle *inside the triangle* opposite \(R\), then the **sine rule** to find an angle. Or split each vector into components (below) and add the components.

:::html
<figure class="fig wide"><svg viewBox="20 40 560 230" role="img" aria-label="Two vector triangles. Left: a 30 newton force along the horizontal then a 40 newton force upwards at 90 degrees, with the 50 newton resultant from the start to the end at 53.1 degrees. Right: a 30 newton force then a 40 newton force at 60 degrees to the first, with a 60.8 newton resultant at 34.7 degrees; the angle inside the triangle at the join is 120 degrees."><path class="c1" d="M50 210H170" marker-end="url(#ah-phys)"/><path class="c2" d="M170 210V50" marker-end="url(#ah2-phys)"/><path class="c3" d="M50 210L170 50" marker-end="url(#ahr)"/><path class="ln-m thin" d="M158 210V198H170"/><path class="ln-m thin" d="M86 210A36 36 0 0 0 71.6 181.2"/><text class="tl ti" x="90" y="196">θ</text><text class="tl tc ta" x="110" y="232">30 N</text><text class="tl ta2" x="182" y="135">40 N</text><text class="tl te tr" x="102" y="124">R = 50 N</text><text class="tl tc" x="110" y="262">(a) forces at 90°, θ = 53.1°</text><path class="c1" d="M330 210H450" marker-end="url(#ah-phys)"/><path class="c2" d="M450 210L530 71.4" marker-end="url(#ah2-phys)"/><path class="c3" d="M330 210L530 71.4" marker-end="url(#ahr)"/><path class="ln-m thin" d="M380 210A50 50 0 0 0 371.1 181.5"/><path class="ln-m thin" d="M422 210A28 28 0 0 1 464 185.8"/><text class="tl ti" x="386" y="198">θ</text><text class="tl te" x="414" y="194">120°</text><text class="tl tc ta" x="390" y="232">30 N</text><text class="tl ta2" x="500" y="150">40 N</text><text class="tl te tr" x="418" y="128">R = 60.8 N</text><text class="tl tc" x="430" y="262">(b) forces 60° apart, θ = 34.7°</text></svg><figcaption>Vectors are added tip to tail. In (b) the forces act 60° apart when drawn from one point, so the angle inside the triangle at the join is 180° − 60° = 120°, the angle used in the cosine rule. The 30 N and 40 N forces add to less than 70 N because they do not point the same way.</figcaption></figure>
:::

:::eg Two forces of 30 N and 40 N act on a point. Find the resultant when the forces are (a) at 90° and (b) 60° apart.
(a) At 90°, the triangle has a right angle:
\[R = \sqrt{30^{2} + 40^{2}} = 50\,\mathrm{N}\] [C1]
\[\theta = \tan^{-1}\frac{40}{30} = 53.1^\circ \text{ from the 30 N force}\] [A1]

(b) Put the two forces tail to tail 60° apart. Drawn tip to tail, the angle inside the triangle between the two sides is \(180^\circ - 60^\circ = 120^\circ\). By the cosine rule
\[R^{2} = 30^{2} + 40^{2} - 2 \times 30 \times 40 \times \cos 120^\circ = 900 + 1600 + 1200 = 3700\] [C1]
so \(R = 60.8\,\mathrm{N}\). [A1]

Sine rule for the angle \(\theta\) between \(R\) and the 30 N force: \(\dfrac{\sin\theta}{40} = \dfrac{\sin 120^\circ}{60.8}\), so \(\theta = 34.7^\circ\). [A1]

**Check** by components: along the 30 N direction, \(30 + 40\cos 60^\circ = 50\,\mathrm{N}\); across, \(40\sin 60^\circ = 34.6\,\mathrm{N}\). Then \(\sqrt{50^{2} + 34.6^{2}} = 60.8\,\mathrm{N}\) and \(\tan^{-1}(34.6/50) = 34.7^\circ\). Same answer.
:::

### Subtracting vectors

To subtract a vector, add its **negative**, which is the same vector reversed: \(\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b})\). The most important use is a **change in velocity**:

\[\Delta\mathbf{v} = \mathbf{v} - \mathbf{u}\]

where \(\mathbf{u}\) is the initial velocity and \(\mathbf{v}\) the final velocity. Choose a positive direction first. Velocities in that direction are positive, and the opposite direction is negative.

:::eg A ball hits a wall at \(8.0\,\mathrm{m\,s^{-1}}\) and rebounds along the same line at \(6.0\,\mathrm{m\,s^{-1}}\). Find its change in velocity.
Take the direction towards the wall as positive. Then the initial velocity is \(u = +8.0\,\mathrm{m\,s^{-1}}\) and the final velocity is \(v = -6.0\,\mathrm{m\,s^{-1}}\) (away from the wall). [B1]

\[\Delta v = v - u = -6.0 - 8.0 = -14\,\mathrm{m\,s^{-1}}\] [C1]
The change in velocity has magnitude \(14\,\mathrm{m\,s^{-1}}\), directed **away from the wall**. [A1]
Not \(2\,\mathrm{m\,s^{-1}}\): the ball does not just slow down by 2, it stops and reverses. The change in *speed* is 2, but the change in *velocity* is 14, and the sign of the velocity has to be included.
:::

### Components of a vector

Any vector can be replaced by two **perpendicular components** that together have exactly the same effect. This is how forces and velocities on slopes and projectiles are solved: each component acts independently, in its own direction.

:::html
<figure class="fig small"><svg viewBox="30 70 400 140" role="img" aria-label="A 250 newton force arrow at 25 degrees above the horizontal, with its horizontal component 227 newton drawn below as a dashed line and its vertical component 106 newton drawn at the right as a dashed line, forming a right-angled triangle"><path class="ln-m dash" d="M60 170H241.3"/><path class="ln-m dash" d="M241.3 170V85.5"/><path class="ln-m thin" d="M229 170V158H241.3"/><path class="c1" d="M60 170L241.3 85.5" marker-end="url(#ah-phys)"/><path class="ln-m thin" d="M110 170A50 50 0 0 0 105.3 148.9"/><text class="tl" x="118" y="164">25°</text><text class="tl ta" x="62" y="140">F = 250 N</text><text class="tl tc" x="150" y="192">F cos θ = 227 N</text><text class="tl" x="252" y="132">F sin θ = 106 N</text></svg><figcaption>The horizontal component is next to the angle, so it uses cosine; the vertical component is opposite the angle, so it uses sine.</figcaption></figure>
:::

:::key Components
A vector of magnitude \(F\) at angle \(\theta\) to a chosen direction has components
\[F_{\parallel} = F\cos\theta \quad\text{(along that direction)} \qquad F_{\perp} = F\sin\theta \quad\text{(at 90° to it)}\]
The component **along** the direction from which \(\theta\) is measured uses **cosine**: the cosine is the side next to the angle. If \(\theta\) is measured from the *other* direction, the cosine and sine swap. The vector and its components form a right-angled triangle with the vector as the hypotenuse, so \(F^{2} = F_{\parallel}^{2} + F_{\perp}^{2}\).
:::

:::eg A child pulls a sledge with a rope that makes an angle of 25° with the horizontal, with a tension of 250 N. Find the horizontal and vertical components of the pull.
Draw the triangle: the rope is the hypotenuse and the angle 25° is between the rope and the horizontal. [B1]

Horizontal (next to the angle): \(250\cos 25^\circ = 227\,\mathrm{N}\). [C1]

Vertical (opposite the angle): \(250\sin 25^\circ = 106\,\mathrm{N}\). [A1]
Only the horizontal component pulls the sledge forward. The vertical component lifts slightly, so it reduces the force between the sledge and the ground.
:::

You can use the components of several vectors to add them: add all the horizontal components to get the horizontal part of the resultant, and all the vertical components to get the vertical part, then use Pythagoras to combine them. This method works for any number of vectors, so it is the one to use when there are three or more.

An optional tool for practising scale drawings and adding two vectors:

:::html
<div class="widget" data-w="resultant"></div>
:::

:::exam Set out vector answers clearly
In a vector question, state your positive direction, show the triangle or the components, and give a direction as well as a size in the final answer ("14 m s⁻¹ away from the wall", "53° above the horizontal", "bearing 010°"). A bare magnitude for a vector answer usually loses a mark.
:::

:::try Start easy, finish at exam standard
Q: Name the base unit of mass, and of electric current.
A: The kilogram (kg) and the ampere (A).
Q: Express the newton in base units.
A: From \(F = ma\): \(\mathrm{N} = \mathrm{kg} \times \mathrm{m\,s^{-2}} = \mathrm{kg\,m\,s^{-2}}\).
Q: Convert 4.7 kΩ to ohms, 250 μm to metres and 3.6 MJ to joules, in standard form.
A: \(4.7 \times 10^{3}\,\Omega\); \(2.5 \times 10^{-4}\,\mathrm{m}\); \(3.6 \times 10^{6}\,\mathrm{J}\).
Q: Convert a volume of 5.0 cm³ to m³.
A: \(1\,\mathrm{cm^{3}} = 10^{-6}\,\mathrm{m^{3}}\), so \(5.0\,\mathrm{cm^{3}} = 5.0 \times 10^{-6}\,\mathrm{m^{3}}\).
Q: Show that the equation \(v^{2} = u^{2} + 2as\) is homogeneous.
A: Left side: \(\mathrm{(m\,s^{-1})^{2}} = \mathrm{m^{2}\,s^{-2}}\). First term on the right: \(\mathrm{m^{2}\,s^{-2}}\). Second term: \(\mathrm{m\,s^{-2}} \times \mathrm{m} = \mathrm{m^{2}\,s^{-2}}\) (the 2 has no unit). Every term has the same units.
Q: A length is measured as \(8.0 \pm 0.2\,\mathrm{cm}\). Find the percentage uncertainty.
A: \(\dfrac{0.2}{8.0} \times 100\% = 2.5\%\).
Q: Which of these are vectors: speed, displacement, energy, momentum, pressure, acceleration?
A: Displacement, momentum and acceleration. Speed, energy and pressure have magnitude only.
Q: A cyclist rides 6.0 km due east and then 8.0 km due north. Find the total distance and the magnitude of the displacement.
A: Distance (scalar): \(6.0 + 8.0 = 14\,\mathrm{km}\). Displacement (vector): \(\sqrt{6.0^{2} + 8.0^{2}} = 10\,\mathrm{km}\).
Q: A 100 N force acts at 30° to the horizontal. Find its components.
A: Horizontal \(100\cos 30^\circ = 86.6\,\mathrm{N}\) and vertical \(100\sin 30^\circ = 50.0\,\mathrm{N}\).
Q: A rod has length \(l = 50.0 \pm 0.5\,\mathrm{cm}\) and is used to make a square of side \(l\). Find the area and its uncertainty.
A: Area \(= 50.0^{2} = 2500\,\mathrm{cm^{2}}\). The percentage uncertainty in \(l\) is 1.0%, so in \(l^{2}\) it is 2.0%: \(\Delta A = 0.02 \times 2500 = 50\,\mathrm{cm^{2}}\). So \(A = (2.50 \pm 0.05) \times 10^{3}\,\mathrm{cm^{2}}\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ (a) Show that the base units of the pascal are \(\mathrm{kg\,m^{-1}\,s^{-2}}\). (b) The pressure at depth \(h\) in a liquid of density \(\rho\) is \(p = \rho g h\). Show that this equation is homogeneous.
A: (a) Pressure = force / area, and the newton is \(\mathrm{kg\,m\,s^{-2}}\) [B1] so the pascal is \(\mathrm{kg\,m\,s^{-2}}/\mathrm{m^{2}} = \mathrm{kg\,m^{-1}\,s^{-2}}\). [B1] (b) The units of \(\rho g h\) are \(\mathrm{kg\,m^{-3}} \times \mathrm{m\,s^{-2}} \times \mathrm{m}\) [C1] \(= \mathrm{kg\,m^{-1}\,s^{-2}}\), the same as the units of pressure. [A1]
Q: [3 marks] ★ Estimate the power of a student running up a flight of stairs. State the values you use.
A: Mass about 60 kg, height climbed about 3 m and time about 5 s. [B1] \(P = \dfrac{mgh}{t} = \dfrac{60 \times 9.81 \times 3.0}{5.0}\) [C1] \(= 353\,\mathrm{W}\), so of the order of \(3 \times 10^{2}\,\mathrm{W}\). [A1] (Accept any answer between 200 W and 600 W that follows from sensible values.)
Q: [3 marks] ★★ A student measures the diameter of a wire with a micrometer and does not notice that it reads \(+0.04\,\mathrm{mm}\) when the jaws are closed. Her mean reading is 0.62 mm. (a) State the type of error caused. (b) Calculate the true diameter.
A: (a) A systematic error (every reading is too large by the same amount). [B1] (b) Subtract the zero error: \(0.62 - 0.04\) [C1] \(= 0.58\,\mathrm{mm}\). [A1]
Q: [4 marks] ★★ A pendulum of length \(l = 0.800 \pm 0.002\,\mathrm{m}\) has period \(T = 1.79 \pm 0.02\,\mathrm{s}\). Calculate \(g\) from \(g = 4\pi^{2}l/T^{2}\) and its percentage uncertainty.
A: \(g = \dfrac{4\pi^{2} \times 0.800}{1.79^{2}}\) [C1] \(= 9.86\,\mathrm{m\,s^{-2}}\). [A1] Percentage uncertainties: \(l\) is \(0.25\%\) and \(T\) is \(1.12\%\). [C1] The period is squared, so \(\dfrac{\Delta g}{g} = 0.25\% + 2 \times 1.12\% = 2.5\%\) (that is, \(\pm 0.2\,\mathrm{m\,s^{-2}}\)). [A1]
Q: [5 marks] ★★ An aircraft has a velocity of \(220\,\mathrm{m\,s^{-1}}\) due north through the air. A wind of \(40\,\mathrm{m\,s^{-1}}\) blows towards the east. (a) Calculate the speed of the aircraft relative to the ground. (b) Calculate the bearing of its direction of travel relative to the ground. (c) Explain why the ground speed is not \(260\,\mathrm{m\,s^{-1}}\).
A: (a) The velocities are at 90°, so \(v = \sqrt{220^{2} + 40^{2}}\) [C1] \(= 224\,\mathrm{m\,s^{-1}}\). [A1] (b) \(\tan\theta = 40/220\) [C1] so \(\theta = 10.3^\circ\) east of north, a bearing of \(010^\circ\). [A1] (c) Velocities are vectors, so they add by geometry. They would only add to 260 if they were in the same direction. [B1]
Q: [6 marks] (#phys.units) ★★★ In an experiment a wire of length \(L = 2.000 \pm 0.005\,\mathrm{m}\) and diameter \(d = 0.60 \pm 0.01\,\mathrm{mm}\) is stretched by a force \(F = 50.0 \pm 0.5\,\mathrm{N}\) and extends by \(x = 1.80 \pm 0.05\,\mathrm{mm}\). The Young modulus is \(E = \dfrac{4FL}{\pi d^{2} x}\). Calculate \(E\) and its absolute uncertainty.
H: Find the percentage uncertainty of each of the four measurements first.
H: The diameter is squared, so its percentage counts twice. Constants such as 4 and \(\pi\) have no uncertainty.
H: Convert the diameter and extension to metres before substituting.
A: \(E = \dfrac{4 \times 50.0 \times 2.000}{\pi \times (0.60 \times 10^{-3})^{2} \times 1.80 \times 10^{-3}}\) [C1] \(= 1.96 \times 10^{11}\,\mathrm{Pa}\). [A1] Percentage uncertainties: \(F\) 1.0%, \(L\) 0.25%, \(d\) 1.67% and \(x\) 2.78%. [C1] Total: \(1.0 + 0.25 + 2 \times 1.67 + 2.78\) [M1] \(= 7.4\%\). [A1] \(\Delta E = 0.074 \times 1.96 \times 10^{11} = 1.4 \times 10^{10}\,\mathrm{Pa}\), so \(E = (1.96 \pm 0.14) \times 10^{11}\,\mathrm{Pa}\) (accept \((2.0 \pm 0.1) \times 10^{11}\,\mathrm{Pa}\)). [A1]
Q: [3 marks] ★★ The drag force on a ball is \(F = \tfrac12 C \rho A v^{2}\), where \(\rho\) is the density of air, \(A\) is the cross-sectional area, \(v\) is the speed and \(C\) is a constant. Show that \(C\) has no unit.
A: Rearrange: \(C = \dfrac{2F}{\rho A v^{2}}\). [C1] Base units: \(F\) is \(\mathrm{kg\,m\,s^{-2}}\) and \(\rho A v^{2}\) is \(\mathrm{kg\,m^{-3}} \times \mathrm{m^{2}} \times \mathrm{m^{2}\,s^{-2}} = \mathrm{kg\,m\,s^{-2}}\). [B1] The units cancel, so \(C\) has no unit. [A1]
Q: [4 marks] ★★★ A ball approaches a vertical wall at \(15\,\mathrm{m\,s^{-1}}\), moving at 40° to the line perpendicular to the wall. It rebounds at the same speed and at the same angle on the other side of the perpendicular. Calculate the magnitude and direction of the ball's change in velocity.
H: Resolve the velocity into a component perpendicular to the wall and one parallel to it.
H: One component does not change. Take the direction towards the wall as positive for the other.
A: Perpendicular component towards the wall: \(15\cos 40^\circ = 11.5\,\mathrm{m\,s^{-1}}\) before, and the same away from the wall after. [C1] The parallel component, \(15\sin 40^\circ\), is unchanged, so its change is zero. [B1] \(\Delta v = -11.5 - 11.5\) [C1] \(= -23.0\,\mathrm{m\,s^{-1}}\). [A1] The change is \(23\,\mathrm{m\,s^{-1}}\) perpendicular to the wall and away from it.
:::

:::try Stretch for A*
Q: [6 marks] ★★★ (a) The gravitational constant \(G\) appears in Newton's law of gravitation, \(F = \dfrac{Gm_1m_2}{r^{2}}\). Find the base units of \(G\). (b) Kepler's third law for a planet orbiting a star of mass \(M\) in a circle of radius \(r\) can be written \(T^{2} = \dfrac{4\pi^{2}r^{3}}{GM}\). Show that this is homogeneous.
H: Make \(G\) the subject of the law of gravitation and substitute the units of force, length and mass.
H: For (b), the unit of \(\dfrac{r^3}{GM}\) should be s².
A: (a) \(G = \dfrac{Fr^{2}}{m_1m_2}\). [C1] Units: \(\dfrac{\mathrm{kg\,m\,s^{-2}} \times \mathrm{m^{2}}}{\mathrm{kg^{2}}}\) [C1] \(= \mathrm{kg^{-1}\,m^{3}\,s^{-2}}\). [A1] (b) Left side: \(\mathrm{s^{2}}\). [B1] Right side: \(GM\) has units \(\mathrm{kg^{-1}\,m^{3}\,s^{-2}} \times \mathrm{kg} = \mathrm{m^{3}\,s^{-2}}\), so \(\dfrac{r^{3}}{GM} = \dfrac{\mathrm{m^{3}}}{\mathrm{m^{3}\,s^{-2}}} = \mathrm{s^{2}}\). [C1] The numerical factor \(4\pi^{2}\) has no unit, so both sides have unit \(\mathrm{s^{2}}\). [A1]
Q: [5 marks] ★★★ The thickness of a sheet of paper is found by measuring a stack. A student measures the height of a stack of 500 sheets as \(48.0 \pm 0.5\,\mathrm{mm}\). (a) Find the thickness of one sheet with its uncertainty. (b) The student instead measures the height of the stack with 500 sheets, then removes one sheet and measures the height again: \(48.0 \pm 0.5\,\mathrm{mm}\) and \(47.9 \pm 0.5\,\mathrm{mm}\). Find the thickness from the difference and its percentage uncertainty, and comment.
H: In (a) the number of sheets is exact.
H: In (b), add the absolute uncertainties for the difference.
A: (a) Thickness \(= 48.0/500 = 0.096\,\mathrm{mm}\). [A1] The number 500 is exact, so \(\Delta t = 0.5/500 = 0.001\,\mathrm{mm}\), and \(t = (0.096 \pm 0.001)\,\mathrm{mm}\). [A1] (b) Difference \(= 48.0 - 47.9 = 0.1\,\mathrm{mm}\). [A1] Absolute uncertainty \(= 0.5 + 0.5 = 1.0\,\mathrm{mm}\), so \(t = (0.1 \pm 1.0)\,\mathrm{mm}\), a percentage uncertainty of \(1000\%\). [C1] Subtracting two nearly equal readings makes the percentage uncertainty enormous. Measuring many sheets together and dividing is far better, because the fixed uncertainty is spread across all the sheets. [B1]
:::

:::quiz
? Which of these is an SI base unit?
- newton
+ kilogram
- gram
- joule
> The kilogram is the base unit of mass. The gram is a prefixed fraction of it, and the newton and the joule are derived units.
? What are the base units of the pascal?
- \(\mathrm{kg\,m\,s^{-2}}\)
+ \(\mathrm{kg\,m^{-1}\,s^{-2}}\)
- \(\mathrm{kg\,m^{2}\,s^{-2}}\)
- \(\mathrm{kg\,m^{-2}\,s^{-2}}\)
> Pressure is force over area: \(\mathrm{kg\,m\,s^{-2}}\) divided by \(\mathrm{m^{2}}\). \(\mathrm{kg\,m\,s^{-2}}\) is the newton and \(\mathrm{kg\,m^{2}\,s^{-2}}\) is the joule.
? A student finds that an equation is homogeneous. What can she conclude?
- The equation is correct.
- The equation is wrong.
+ The equation may be correct, but could still contain a wrong numerical factor.
- The equation must contain no constants.
> Homogeneity is necessary but not sufficient. It cannot detect a missing factor such as \(\tfrac12\).
? What is 2.0 mm² in m²?
- \(2.0 \times 10^{-3}\,\mathrm{m^{2}}\)
- \(2.0 \times 10^{-9}\,\mathrm{m^{2}}\)
+ \(2.0 \times 10^{-6}\,\mathrm{m^{2}}\)
- \(2.0 \times 10^{6}\,\mathrm{m^{2}}\)
> \(1\,\mathrm{mm} = 10^{-3}\,\mathrm{m}\), so \(1\,\mathrm{mm^{2}} = (10^{-3})^{2} = 10^{-6}\,\mathrm{m^{2}}\). The first option forgets to square the prefix.
? A voltmeter reads 0.2 V when it is disconnected from any circuit. Every reading in an experiment is then 0.2 V too high. What kind of error is this?
- random error
+ systematic error
- a mistake in precision
- an uncertainty
> Every reading is shifted by the same amount in the same direction, which is a (zero) systematic error. Repeating the readings will not remove it.
? Four readings of a time are 5.01 s, 5.02 s, 5.01 s and 5.02 s, but the true time is 4.50 s. Which description is correct?
- precise and accurate
+ precise but not accurate
- accurate but not precise
- neither precise nor accurate
> The readings are close together, so they are precise. They are not close to the true value, so they are not accurate. This is typical of a systematic error.
? The radius of a sphere is measured with a percentage uncertainty of 2%. What is the percentage uncertainty in its volume \(V = \tfrac43\pi r^{3}\)?
- 2%
- 4%
+ 6%
- 8%
> The volume depends on \(r^{3}\), so the percentage is multiplied by 3. The factor \(\tfrac43\pi\) is a constant and has no uncertainty.
? Two forces of 3.0 N and 4.0 N act at a point. Which value could NOT be the size of their resultant?
- 1.0 N
- 5.0 N
- 7.0 N
+ 8.0 N
> The resultant is largest (7.0 N) when the forces point the same way and smallest (1.0 N) when they point in opposite directions. 5.0 N occurs at 90°. A resultant of 8.0 N would need the forces to add to more than the sum of their sizes.
:::

:::checklist What you can now do
- [ ] I can state that a physical quantity is a numerical magnitude and a unit, and write quantities in tables and on axes as quantity / unit.
- [ ] I can make reasonable estimates of everyday physical quantities and show the working.
- [ ] I can recall the five SI base quantities and units.
- [ ] I can find the base units of any derived unit from a defining equation.
- [ ] I can use base units to check whether an equation is homogeneous, and say what the check cannot show.
- [ ] I can use the prefixes p to T, and convert units correctly, including squares and cubes of prefixed units.
- [ ] I can distinguish systematic and random errors, including zero errors, and explain their effect on readings.
- [ ] I can distinguish precision from accuracy.
- [ ] I can find the uncertainty in a derived quantity by adding absolute or percentage uncertainties, and write the result with sensible figures.
- [ ] I can distinguish scalars from vectors, add and subtract coplanar vectors, and resolve a vector into perpendicular components.
:::

:::recap
- A physical quantity = numerical magnitude × unit. Tables and axes use "quantity / unit".
- The five base units: kilogram, metre, second, ampere, kelvin. Derived units come from defining equations (\(\mathrm{N} = \mathrm{kg\,m\,s^{-2}}\), \(\mathrm{J} = \mathrm{kg\,m^{2}\,s^{-2}}\), \(\mathrm{Pa} = \mathrm{kg\,m^{-1}\,s^{-2}}\), \(\mathrm{V} = \mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}\)).
- A homogeneous equation has the same base units in every term. Homogeneity can disprove an equation but cannot prove it.
- Prefixes: p \(10^{-12}\), n \(10^{-9}\), μ \(10^{-6}\), m \(10^{-3}\), c \(10^{-2}\), d \(10^{-1}\), k \(10^{3}\), M \(10^{6}\), G \(10^{9}\), T \(10^{12}\). Prefixes are squared and cubed with the unit: \(1\,\mathrm{mm^{2}} = 10^{-6}\,\mathrm{m^{2}}\).
- Random errors scatter readings and are reduced by averaging. Systematic errors (zero errors, calibration) shift all readings the same way and are not reduced by repeating.
- Precision: closeness of repeated readings. Accuracy: closeness to the true value.
- Uncertainties: sum or difference, add absolute uncertainties; product or quotient, add percentage uncertainties; power \(n\), multiply the percentage by \(n\). Quote uncertainty to 1 s.f. and the value to the same decimal place.
- Scalars have magnitude only; vectors have magnitude and direction. Add vectors tip to tail; subtract by adding the negative; resolve with \(F\cos\theta\) and \(F\sin\theta\).
:::

:::links
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Kinematics](#phys.kinematics)
