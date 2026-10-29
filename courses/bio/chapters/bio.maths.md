@chapter bio.maths
@title Maths skills for biology
@level as
@paper CAIE 9700 Papers 1, 2 and 3
@time 4–5 hours
@summary Every biology paper gives you numbers to handle. You will learn the unit prefixes and conversions, standard form, estimation, significant figures, the symbols the papers use, averages, ratios, percentage change and percentage error, areas and volumes, magnification, how to choose and draw a graph, how to find a rate from a gradient or a tangent, and how to use lg.

:::why
In Papers 2 and 3, a large share of the marks is for handling numbers: converting units, working out a percentage, reading a rate from a graph, or saying how precise a measurement is. At AS, 40% of all the marks are for handling and applying information (assessment objective AO2). No paper has a formula sheet or a data booklet, but every paper lets you use a calculator, so the formulae in this chapter are ones you must remember and the arithmetic is the part the calculator does. Nearly every mark here is method, and method can be learned.
:::

**Before you start**, you should know the units of size and \(M = I/A\) from [Microscopy and magnification](#bio.microscopy), and surface area to volume ratio from [Movement across membranes](#bio.movement). The rate of an enzyme reaction is in [Enzymes](#bio.enzymes).

:::try Warm-up
Q: A cell is 0.045 mm across. Give this length in µm. (from [Microscopy and magnification](#bio.microscopy))
A: \(0.045 \times 1000 = 45\,\mathrm{\mu m}\). Going from mm to the smaller unit µm, you multiply by 1000.
Q: A drawing of a cell is 36 mm long and the cell is really 12 µm long. What is the magnification? (from [Microscopy and magnification](#bio.microscopy))
A: Convert to the same unit: 36 mm = 36 000 µm. \(M = I/A = 36\,000 \div 12 = \times 3000\).
Q: Calculate the surface area to volume ratio of a cube with sides of 3 cm. (from [Movement across membranes](#bio.movement))
A: Surface area \(= 6 \times 3^2 = 54\,\mathrm{cm^2}\); volume \(= 3^3 = 27\,\mathrm{cm^3}\). The ratio is \(54 : 27 = 2 : 1\).
:::

## Units and prefixes

A measurement is a number and a unit. Biology covers a huge range of sizes, so the SI units come with **prefixes**: a letter in front of the unit that multiplies it by a power of ten.

| prefix | symbol | multiplies by | example |
|---|---|---|---|
| giga | G | \(10^{9}\) | gigabase (sequencing a genome) |
| mega | M | \(10^{6}\) | megapascal |
| kilo | k | \(10^{3}\) | kilojoule (kJ), kilogram (kg) |
| milli | m | \(10^{-3}\) | millimetre (mm), millimole (mmol) |
| micro | µ | \(10^{-6}\) | micrometre (µm), microgram (µg) |
| nano | n | \(10^{-9}\) | nanometre (nm) |

Notice that micro (µ) and milli (m) look alike. A micrometre is a thousand times smaller than a millimetre, and mixing them up gives an answer wrong by a factor of 1000.

:::key Converting units
1. Write down the conversion that links the two units: \(1\,\mathrm{mm} = 1000\,\mathrm{\mu m}\), \(1\,\mathrm{\mu m} = 1000\,\mathrm{nm}\), \(1\,\mathrm{dm^3} = 1000\,\mathrm{cm^3}\), \(1\,\mathrm{kg} = 1000\,\mathrm{g}\), \(1\,\mathrm{g} = 1000\,\mathrm{mg}\), \(1\,\mathrm{min} = 60\,\mathrm{s}\).
2. Going to a **smaller** unit, the number gets **bigger**, so multiply. Going to a **larger** unit, the number gets smaller, so divide.
3. Check that the answer is sensible: 0.35 mm is a small number of mm, so it must be a few hundred µm.
:::

A volume of \(1\,\mathrm{dm^3}\) is a cube 10 cm by 10 cm by 10 cm, which is 1000 cm³, so converting cm³ to dm³ means dividing by 1000 (not by 10 or 100). A concentration such as \(0.5\,\mathrm{mol\,dm^{-3}}\) is "0.5 mol in every dm³". Choose units so the numbers are easy to read: cell sizes in µm, oxygen volumes in cm³, masses in g. Use the same unit for all the numbers in a calculation, or convert first.

:::eg Convert (a) 0.35 mm to µm, (b) 4.2 µm to mm, (c) 250 cm³ to dm³, (d) a rate of 0.90 cm³ min⁻¹ to cm³ s⁻¹.
(a) mm to µm is to a smaller unit, so multiply by 1000.

\[\begin{aligned} 0.35 \times 1000 &= 350\,\mathrm{\mu m} \end{aligned}\]

(b) µm to mm is to a larger unit, so divide by 1000.

\[\begin{aligned} 4.2 \div 1000 &= 0.0042\,\mathrm{mm} \end{aligned}\]

(c) cm³ to dm³: divide by 1000.

\[\begin{aligned} 250 \div 1000 &= 0.25\,\mathrm{dm^3} \end{aligned}\]

(d) One minute is 60 s, so the gas is released over 60 times as many seconds and the rate per second is 60 times smaller.

\[\begin{aligned} 0.90 \div 60 &= 0.015\,\mathrm{cm^3\,s^{-1}} \end{aligned}\]
:::

:::warn Dividing when you should multiply
The commonest slip is going the wrong way. A quick test: a µm is a tiny unit, so the same length measured in µm is always a bigger number than in mm. If your answer for a length in µm is smaller than its value in mm, you divided instead of multiplying.
:::

## Decimals and standard form

Very large and very small numbers are written in **standard form** so that you do not lose a zero.

:::def Standard form
A number written as \(a \times 10^{n}\), where \(a\) is at least 1 and less than 10 and \(n\) is a whole number (negative for numbers smaller than 1).
:::

To write 0.000 62 in standard form, move the decimal point until the number is between 1 and 10 (four places to the right), and write the number of places as a negative power: \(6.2 \times 10^{-4}\). For 48 000 000, move the point seven places to the left: \(4.8 \times 10^{7}\). Check by asking if the answer is big or small: a small number has a negative power.

On a calculator, enter \(6.2 \times 10^{-4}\) with the **EXP** (or ×10ˣ) key: 6.2, EXP, (−), 4. Do not type "× 10" and then a power, because many calculators then give the wrong result. When you multiply numbers in standard form you multiply the front numbers and add the powers; when you divide, you divide the front numbers and subtract the powers.

:::eg A culture contains \(3.2 \times 10^{7}\) bacteria per cm³. How many bacteria are in 0.25 cm³? Give the answer in standard form.
Multiply the number per cm³ by the volume.

\[\begin{aligned} 3.2 \times 10^{7} \times 0.25 &= 0.8 \times 10^{7} \\ &= 8.0 \times 10^{6}\ \text{bacteria} \end{aligned}\]

The first line is not yet in standard form, because 0.8 is less than 1. Move the decimal point one place to the right and lower the power by one.
:::

## Estimating an answer

A calculator does what you type, not what you meant. Before you trust an answer, **estimate** it: round each number to one significant figure and do the sum in your head. If the estimate and the calculator disagree by a factor of 10, you mistyped something.

:::eg Estimate \(3.9 \times 10^{-3} \times 410\), then check with a calculator.
Round to one significant figure: \(3.9 \times 10^{-3} \approx 4 \times 10^{-3}\) and \(410 \approx 400\).

\[\begin{aligned} 4 \times 10^{-3} \times 400 &= 1600 \times 10^{-3} \\ &= 1.6 \end{aligned}\]

The calculator gives \(3.9 \times 10^{-3} \times 410 = 1.599 = 1.60\) (3 significant figures), which agrees with the estimate.
:::

Estimation also helps in biology: a plant cell is tens of µm across, so a calculation that gives a cell 4 m long has gone wrong somewhere.

## Significant figures and decimal places

A **decimal place** (d.p.) is a digit after the decimal point. A **significant figure** (s.f.) is a digit that carries information, counted from the first non-zero digit. So 0.0450 has three significant figures (4, 5 and the final 0, which shows the value was measured to the nearest 0.0001) but only four decimal places. 250 has two or three, depending on whether the zero was measured; standard form removes the doubt: \(2.5 \times 10^{2}\) has two.

:::key The significant figures rule (Cambridge)
1. The answer to a calculation has the **same number of significant figures as the least precise data you used, or one more**.
2. Keep every digit on your calculator **during** the working. Round once, at the end.
3. Record measurements to the precision of the instrument, with the same number of decimal places down a column: a ruler marked in mm gives 4.0 cm, not 4 cm; a balance reading 0.01 g gives 2.50 g, not 2.5 g.
:::

:::eg A student collected 4.7 cm³ of gas in 15 s. Calculate the mean rate of gas production, with a suitable number of significant figures.
\[\begin{aligned} \text{rate} &= \frac{4.7}{15} \\ &= 0.3133\ldots\,\mathrm{cm^3\,s^{-1}} \end{aligned}\]

Both numbers have 2 significant figures, so the answer should have 2 or 3: 0.31 or 0.313 \(\mathrm{cm^3\,s^{-1}}\). Giving 0.3 loses a figure unnecessarily; giving 0.313333 claims a precision the measurements do not have.
:::

:::warn Rounding in the middle
If a calculation has several steps, do not write down a rounded value and then use it. Rounding 11.678 to 11.7 early and then dividing can change the third figure of the answer. Use the calculator's memory (or the answer key) to carry the full value to the next step.
:::

## Symbols and table headings

You need to recognise these symbols and use them correctly.

| symbol | meaning | example |
|---|---|---|
| \(<\) | less than | pH \(< 7\) is acidic |
| \(>\) | greater than | rate at 40 °C \(>\) rate at 20 °C |
| \(\le\) | less than or equal to | \(0 \le x \le 100\) |
| \(\ge\) | greater than or equal to | mass \(\ge 2.00\) g |
| \(\propto\) | is directly proportional to | rate \(\propto\) enzyme concentration |
| \(\Sigma\) | the sum of | mean \(= \Sigma x \div n\) |
| \(/\) (solidus) | "per": in a heading, the unit follows it | temperature / °C |

The solidus is how you head a table column or label a graph axis: **quantity / unit**. So "time / s" means the numbers below are times in seconds, and "volume of oxygen / cm³" is read "volume of oxygen in cm³". The units go in the heading and never in the body of the table (see [Practical skills: investigations](#bio.practical)).

"Directly proportional" has a precise meaning: if one quantity doubles, so does the other, and a graph of one against the other is a straight line through the origin.

## Averages and range

:::def Mean
The sum of all the values divided by the number of values: \(\Sigma x \div n\).
:::

:::def Median
The middle value when the values are written in order. If there are two middle values, the median is halfway between them.
:::

:::def Mode
The value that occurs most often.
:::

:::def Range
The spread of the data, from the lowest value to the highest. Give both values (for example "38 to 52 mm"), or the difference between them (14 mm).
:::

Use the **mean** for most measurements, the **median** when a few extreme values would drag the mean away from the middle, and the **mode** for categories (the most common blood group or the most common number of petals). Before you calculate a mean, look for an **anomalous result**, one that does not fit the pattern. Leave it out of the mean and say that you did.

:::eg The lengths of ten leaves from one plant were 42, 38, 45, 41, 38, 52, 40, 38, 44 and 43 mm. Calculate the mean, median, mode and range.
**Mean**: add the values and divide by the number of values.

\[\begin{aligned} \Sigma x &= 421 \\ \text{mean} &= 421 \div 10 \\ &= 42.1\,\mathrm{mm} \end{aligned}\]

**Median**: write the values in order: 38, 38, 38, 40, 41, 42, 43, 44, 45, 52. There are two middle values, 41 and 42, so the median is \((41 + 42) \div 2 = 41.5\,\mathrm{mm}\).

**Mode**: 38 mm, which occurs three times.

**Range**: 38 mm to 52 mm, a difference of 14 mm.

The longest leaf (52 mm) pulls the mean above the median. A measurement this far from the rest would be worth checking.
:::

## Ratios

A **ratio** compares two quantities of the same kind. Write it in its simplest form by dividing both numbers by the same factor, or as \(n : 1\) by dividing both by the second number.

:::eg (a) A cross gave 108 red-flowered and 36 white-flowered plants. Write the ratio in its simplest form. (b) A surface area of 45 cm² and a volume of 12 cm³ are compared. Write the ratio in the form \(n : 1\).
(a) Divide both numbers by 36.

\[\begin{aligned} 108 : 36 &= 3 : 1 \end{aligned}\]

(b) Divide both numbers by 12.

\[\begin{aligned} 45 : 12 &= 3.75 : 1 \end{aligned}\]

Use the \(n : 1\) form when you compare ratios: 3.75 : 1 is clearly bigger than 2 : 1, while 45 : 12 and 2 : 1 are harder to compare at a glance.
:::

To share a quantity in a ratio, add the parts first. A 120 cm³ mixture in the ratio 3 : 1 has \(3 + 1 = 4\) parts, each \(120 \div 4 = 30\,\mathrm{cm^3}\), so the two volumes are 90 cm³ and 30 cm³.

:::warn "1 : 4" is not "1 in 5"
A dilution of "1 part stock to 4 parts water" is the ratio 1 : 4 and makes a total of 5 parts, so the stock is diluted to \(\tfrac{1}{5}\) of its concentration. Read the wording of the question: "1 in 5" and "1 : 5" are not the same thing.
:::

## Percentages

To find one quantity as a percentage of another, divide the part by the whole and multiply by 100: 18 out of 24 is \(18 \div 24 \times 100 = 75\%\).

:::formula Percentage change
\[\text{percentage change} = \frac{\text{final value} - \text{initial value}}{\text{initial value}} \times 100\]
A positive answer is a percentage increase (or gain) and a negative answer is a percentage decrease (or loss). Always divide by the **initial** value, the one you started with.
:::

:::eg Pieces of seaweed were weighed before and after 30 minutes in a salt solution. Calculate the percentage change in mass for each piece.
| piece | initial mass / g | final mass / g |
|---|---|---|
| A | 4.20 | 4.62 |
| B | 3.85 | 3.47 |
| C | 5.10 | 4.59 |

Use the formula for each piece, dividing by the initial mass. The change in mass is final minus initial. [B1]

\[\begin{aligned} \text{A: } \frac{4.62 - 4.20}{4.20} \times 100 &= +10.0\% \end{aligned}\]

\[\begin{aligned} \text{B: } \frac{3.47 - 3.85}{3.85} \times 100 &= -9.87\% \end{aligned}\]

\[\begin{aligned} \text{C: } \frac{4.59 - 5.10}{5.10} \times 100 &= -10.0\% \end{aligned}\]

Piece A gained 10.0% [A1]. Piece B lost 9.87%, written as \(-9.87\%\) [A1]. Piece C lost 10.0% [A1].

Piece B is the smallest of the three, so its mass change of 0.38 g is the least, yet its percentage loss is about the same as C's (0.51 g). A percentage change allows a fair comparison between pieces with different starting masses.
:::

### Percentage error

No measurement is perfect. The **uncertainty** is how far a reading could be from the true value, and a **percentage error** says how big that is compared with the reading.

:::formula Percentage error
\[\text{percentage error} = \frac{\text{uncertainty}}{\text{measured value}} \times 100\]
For a single reading, the uncertainty is **half the smallest division** of the instrument (so a reading on a scale marked every 0.2 cm³ has an uncertainty of \(\pm 0.1\,\mathrm{cm^3}\)). If a value is found by subtracting two readings (a start and an end), the two uncertainties add.
:::

:::eg A 10 cm³ measuring cylinder has divisions every 0.2 cm³. Calculate the percentage error when it is used to measure (a) 6.0 cm³ and (b) 2.0 cm³. Suggest how to reduce the error in (b).
The smallest division is 0.2 cm³, so the uncertainty is half of this: \(\pm 0.1\,\mathrm{cm^3}\).

\[\begin{aligned} \text{(a) } \frac{0.1}{6.0} \times 100 &= 1.7\% \end{aligned}\]

\[\begin{aligned} \text{(b) } \frac{0.1}{2.0} \times 100 &= 5.0\% \end{aligned}\]

The same instrument has three times the percentage error on the smaller volume, because the fixed uncertainty is a larger fraction of a small reading. To reduce the error in (b), use a smaller instrument with finer divisions, such as a 5 cm³ graduated pipette or a 2 cm³ syringe marked every 0.1 cm³, so the uncertainty is smaller compared with the volume measured.
:::

:::tip Which measurement matters most?
The measurement with the biggest percentage error is the biggest source of uncertainty in the results. To improve an investigation, fix that one first: that is what an examiner wants when you are asked for "an improvement to the measurement".
:::

## Areas, perimeters and volumes

The papers print no formulae, so these must be memorised.

:::formula Shapes you must be able to calculate
- **Rectangle**: area \(= l \times w\); perimeter \(= 2(l + w)\).
- **Triangle**: area \(= \tfrac12 \times \text{base} \times \text{height}\).
- **Circle** (radius \(r\)): area \(= \pi r^2\); circumference \(= 2\pi r\). The radius is half the diameter.
- **Cuboid**: volume \(= l \times w \times h\); surface area \(= 2(lw + lh + wh)\).
- **Cylinder** (radius \(r\), length \(h\)): volume \(= \pi r^2 h\); surface area of the curved side \(= 2\pi r h\); each flat end \(= \pi r^2\).
:::

In biology these appear as the area of a field of view (a circle), the area of a leaf or a clear zone on a plate, and the surface area to volume ratio of a block of tissue, which is the idea behind [Movement across membranes](#bio.movement). A cylinder of potato cut with a cork borer is a cylinder; an agar block is a cuboid.

:::eg A cylinder of potato has a diameter of 1.0 cm and a length of 3.0 cm, and both ends are cut flat. Calculate its volume, its total surface area and its surface area to volume ratio.
The radius is half the diameter, \(r = 0.50\,\mathrm{cm}\).

**Volume**:

\[\begin{aligned} V &= \pi r^2 h \\ &= \pi \times 0.50^2 \times 3.0 \\ &= 2.36\,\mathrm{cm^3} \end{aligned}\]

**Surface area**: two flat ends plus the curved side.

\[\begin{aligned} A &= 2\pi r^2 + 2\pi r h \\ &= 2\pi \times 0.50^2 + 2\pi \times 0.50 \times 3.0 \\ &= 11.0\,\mathrm{cm^2} \end{aligned}\]

**Ratio**: divide the unrounded values.

\[\begin{aligned} \frac{A}{V} &= \frac{10.9956}{2.3562} \\ &= 4.67 \end{aligned}\]

The surface area to volume ratio is \(4.67 : 1\) (the units are cm⁻¹).
:::

:::eg A circular clear zone of diameter 14 mm formed around an antibiotic disc on an agar plate. Calculate the area of the clear zone.
The radius is \(14 \div 2 = 7.0\,\mathrm{mm}\).

\[\begin{aligned} \text{area} &= \pi r^2 \\ &= \pi \times 7.0^2 \\ &= 154\,\mathrm{mm^2} \end{aligned}\]

A common slip is to use the diameter in place of the radius; that would give four times too large an area.
:::

## Magnification and actual size

You met \(M = I/A\) in [Microscopy and magnification](#bio.microscopy). Rearranging gives the triangle I = A × M, A = I ÷ M, M = I ÷ A. The only trap is units: the image size and the actual size must be in the **same unit** before you divide.

:::eg A photomicrograph of a plant cell is magnified ×1500. The cell in the photomicrograph is 54 mm long. Calculate its actual length in µm.
\[\begin{aligned} A &= \frac{I}{M} \\ &= \frac{54\,\mathrm{mm}}{1500} \\ &= 0.036\,\mathrm{mm} \end{aligned}\]

Convert to µm: \(0.036 \times 1000 = 36\,\mathrm{\mu m}\).
:::

With a **scale bar**, measure the bar with a ruler and use the length it represents as the actual size. A bar 20 mm long that represents 5 µm gives \(M = 20\,000\,\mathrm{\mu m} \div 5\,\mathrm{\mu m} = \times 4000\).

## Choosing and drawing graphs

A graph or chart turns a table of numbers into a picture. Choose the type from the kind of data.

| type | use it when | how it is drawn |
|---|---|---|
| **Line graph** | both variables are continuous numbers (time, temperature, concentration) | points plotted, joined by a line or curve |
| **Bar chart** | one variable is a category, or the data are discontinuous (species, blood group, treatment) | separate bars of equal width, with gaps between |
| **Histogram** | continuous data grouped into classes, to show a frequency distribution (the lengths of 60 leaves) | bars **touch**; the x-axis is a continuous scale; the y-axis is frequency |
| **Pie chart** | showing the share of each category in a whole | each sector has an angle of \(\text{fraction} \times 360^\circ\) |

:::eg Choose the best type of graph for each data set. (a) The mean heart rate of a student in water at five temperatures. (b) The number of plants of each of four species in a quadrat. (c) The lengths of 60 leaves, grouped into classes of 10 mm. (d) The percentage of a meal's energy that comes from carbohydrate, lipid and protein.
(a) **Line graph**: temperature is a continuous independent variable, so the points can be joined or a best-fit line drawn.

(b) **Bar chart**: the species are categories, so the bars are separate and the x-axis has the species names.

(c) **Histogram**: this is the frequency of a continuous measurement in classes, so the bars touch and the y-axis is the number of leaves.

(d) **Pie chart**: three parts of one whole. The sector angle for a share of 55% is \(0.55 \times 360 = 198^\circ\).
:::

:::key Drawing a graph
1. The **independent variable** (the one you change) goes on the **x-axis**; the dependent variable (the one you measure) on the **y-axis**.
2. Label each axis with the **quantity / unit**, exactly as in the table heading.
3. Choose a scale that uses **more than half** of the grid in each direction, with simple steps (1, 2, 5 or 10 per large square, never 3 or 7). Start at zero unless that would waste most of the grid.
4. Plot every point as a small **cross** or a **dot in a circle**.
5. If the data show a clear trend and the points scatter, draw a **line of best fit**: a smooth curve or a ruled straight line with points on both sides. If you cannot say what happens between points, join them with **ruled straight lines**.
6. Do not extend a line beyond the data unless the question says you can.
:::

The next skill is turning one form of information into another. A table of numbers can become a graph, and a straight-line graph can become an equation, \(y = mx + c\), where \(m\) is the gradient and \(c\) is the value of \(y\) where the line crosses the y-axis. If the line goes through the origin, \(c = 0\) and \(y \propto x\).

:::plot Oxygen taken up by germinating seeds in a closed tube. The graph is a straight line through the origin: \(V = 0.12\,t\).
--f "0.12*x" --x 0 40 --y 0 7 --xlabel "time / min" --ylabel "volume of oxygen / cm³" --label "V = 0.12t" --pt "40,4.8,4.8 cm³ at 40 min@nw" --legend tr --alt "A straight line through the origin rises steadily to 4.8 cm cubed of oxygen at 40 minutes."
:::

## Rates from graphs

:::def Rate of change
How much a quantity changes per unit of another quantity, usually time. It is found from the gradient of a graph of the quantity against time.
:::

On a **straight-line** graph, the rate is the same everywhere. Pick two points far apart on the line, find the change in \(y\) and the change in \(x\), and divide. For the graph above, between 0 and 40 min:

\[\begin{aligned} \text{gradient} &= \frac{4.8 - 0}{40 - 0} \\ &= 0.12\,\mathrm{cm^3\,min^{-1}} \end{aligned}\]

The unit of a gradient is the unit of \(y\) divided by the unit of \(x\). On a **curve**, the rate changes from point to point. To find the rate at one moment, draw a **tangent**.

:::def Tangent
A straight line that touches a curve at one point and has the same slope as the curve at that point. It does not cross the curve where it touches it.
:::

:::key Finding the rate at a point on a curve
1. Mark the point on the curve (for example at \(t = 2\) min).
2. Lay a ruler against the curve at that point, with the curve on the same side of the ruler either side of the point. Check that the angles between the ruler and the curve look equal on both sides. Draw the line.
3. Make a large right-angled triangle under the tangent. Read two points on the tangent, far apart. **Use points on the tangent, not points on the curve.**
4. Rate \(= \dfrac{\text{change in } y}{\text{change in } x}\), with units.
:::

:::plot Product formed in a reaction over time, with a tangent drawn at t = 2 min. The tangent touches the curve at 11.7 cm³ and passes through (0, 3.5) and (6, 28.1), so its gradient is the rate at 2 min.
--f "24*(1-exp(0-x/3))" --f "11.678+4.1073*(x-2)+0*sqrt(x)+0*sqrt(6-x)" --label "product formed" --label "tangent at t = 2 min" --x 0 10 --y 0 32 --xlabel "time / min" --ylabel "product / cm³" --pt "2,11.68,touches at t = 2 min@se" --legend tr --alt "The product curve rises steeply at first, then more and more slowly, and almost levels off at 24 cm cubed. A straight tangent touches the curve at 2 minutes, where the product is 11.7 cm cubed, and rises to 28.1 cm cubed at 6 minutes."
:::

:::eg The table gives the volume of product formed in a reaction. A tangent at 2 min passes through (0, 3.5) and (6, 28.1) on the graph above. Find the rate of reaction at 2 min and compare it with the rate at 6 min.
| time / min | product / cm³ |
|---|---|
| 0 | 0.0 |
| 1 | 6.8 |
| 2 | 11.7 |
| 3 | 15.2 |
| 4 | 17.7 |
| 5 | 19.5 |
| 6 | 20.8 |
| 8 | 22.3 |
| 10 | 23.1 |

Draw a tangent that touches the curve at 2 min. [B1]

Choose two points on the tangent far apart and find the changes in \(y\) and \(x\). [M1]

\[\begin{aligned} \text{rate at 2 min} &= \frac{28.1 - 3.5}{6 - 0} \\ &= 4.1\,\mathrm{cm^3\,min^{-1}} \end{aligned}\]

The rate at 2 min is \(4.1\,\mathrm{cm^3\,min^{-1}}\) [A1]. The units are the unit of \(y\) divided by the unit of \(x\). [B1]

At 6 min a tangent would be much flatter: its gradient is about \(1.1\,\mathrm{cm^3\,min^{-1}}\). The rate falls with time because the reactants are being used up, which is why a tangent, not the mean rate over the whole experiment, is needed to give the rate at one time.
:::

:::warn A chord is not a tangent
Joining two points of the curve with a ruler gives a **chord**, whose gradient is the mean rate between those two points. It is not the rate at a point. Also, never use the plotted data points to calculate the tangent's gradient unless they lie on the tangent line: read the two points from the tangent itself.
:::

## Logarithms (lg)

The **logarithm** (lg, base 10) of a number is the power of 10 that gives it: \(\lg 1000 = 3\) because \(10^3 = 1000\); \(\lg 0.01 = -2\) because \(10^{-2} = 0.01\). Use the **log** key on a calculator. To go back, use the \(10^x\) key.

Biology uses logs in two main places. **pH** is a log scale: \(\mathrm{pH} = -\lg[\ce{H+}]\), so each unit of pH is a ten-fold change in hydrogen ion concentration. **Counts** that change by powers of ten, such as numbers of bacteria, are easier to plot as \(\lg(\text{count})\), so that each step up the axis means "ten times as many".

:::eg (a) A solution has a hydrogen ion concentration of \(3.2 \times 10^{-5}\,\mathrm{mol\,dm^{-3}}\). Calculate its pH. (b) A culture contains \(4.0 \times 10^{5}\) bacteria per cm³. Calculate \(\lg\) of this count. (c) A culture has \(\lg(\text{count}) = 7.30\). How many bacteria per cm³ does it contain?
(a)

\[\begin{aligned} \mathrm{pH} &= -\lg(3.2 \times 10^{-5}) \\ &= 4.49 \end{aligned}\]

(b)

\[\begin{aligned} \lg(4.0 \times 10^{5}) &= 5.60 \end{aligned}\]

(c) Use the \(10^x\) key.

\[\begin{aligned} 10^{7.30} &= 2.0 \times 10^{7}\ \text{bacteria per cm}^3 \end{aligned}\]
:::

## Putting it together in an exam

:::exam Calculation questions
Write the formula, substitute with the units, and give the answer with units and the right number of significant figures. A calculation scores method marks (M1) for the formula and the substitution, and an accuracy mark (A1) for the answer, so a wrong final answer can still score marks when the working is shown. Command words: **calculate** means work out a number; **estimate** means find an approximate value; **describe** a graph means give the trend with figures and units. If the question says "show your working", the marks are for the working.
:::

:::eg Spot the error: calculate the percentage change in mass of a plant tissue that fell from 8.0 g to 6.0 g. [3]
A student wrote this answer.

Line 1: change in mass \(= 6.0 - 8.0 = -2.0\) g
Line 2: percentage change \(= -2.0 \div 6.0 \times 100\)
Line 3: \(= -33\%\)

Line 1 is correct: the change is the final value minus the initial value [B1]. **Line 2 is wrong: the student divided by the final mass (6.0 g). A percentage change is always the change divided by the initial mass (8.0 g). The method mark is lost [M0], and so is the accuracy mark in Line 3 [A0].**

Correct Line 2: \(-2.0 \div 8.0 \times 100\), giving \(-25\%\) in Line 3. With that change the answer scores 3 marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: Convert 2.5 mg to g, and 0.40 dm³ to cm³.
A: mg to g divides by 1000: \(2.5 \div 1000 = 0.0025\,\mathrm{g}\). dm³ to cm³ multiplies by 1000: \(0.40 \times 1000 = 400\,\mathrm{cm^3}\).
Q: Write 0.000 047 and 6 200 000 in standard form.
A: \(4.7 \times 10^{-5}\) and \(6.2 \times 10^{6}\).
Q: How many significant figures are there in 0.0705, in 120 and in \(1.20 \times 10^{2}\)?
A: 0.0705 has 3 (the zero between 7 and 5 counts, the leading zeros do not). 120 is ambiguous (2 or 3); \(1.20 \times 10^{2}\) has 3.
Q: A student wrote "reaction rate ∝ time". Explain what is wrong with this statement and give a correct statement about rate and enzyme concentration.
A: Rate is the amount of product per unit time; it is not proportional to time (a rate is a ratio, change divided by time). A correct statement: the rate of an enzyme reaction \(\propto\) enzyme concentration (when substrate is in excess), meaning doubling the enzyme concentration doubles the rate.
Q: The heights of seven seedlings were 18, 22, 19, 22, 25, 20 and 22 mm. Find the mean, median, mode and range.
A: Sum \(= 148\), mean \(= 148 \div 7 = 21.1\,\mathrm{mm}\). In order: 18, 19, 20, 22, 22, 22, 25, so the median is 22 mm. Mode: 22 mm. Range: 18 to 25 mm, a difference of 7 mm.
Q: A beetroot sample lost mass, from 6.40 g to 5.76 g. Calculate the percentage change in mass.
A: \((5.76 - 6.40) \div 6.40 \times 100 = -10.0\%\), a 10.0% loss.
Q: A burette is read as 23.40 cm³ at the start and 31.60 cm³ at the end, with divisions every 0.10 cm³. State the volume used and its percentage error.
A: Volume used \(= 31.60 - 23.40 = 8.20\,\mathrm{cm^3}\). Each reading has an uncertainty of \(\pm 0.05\,\mathrm{cm^3}\) (half a division), so the difference has \(\pm 0.10\,\mathrm{cm^3}\). Percentage error \(= 0.10 \div 8.20 \times 100 = 1.2\%\).
Q: A rectangular leaf measures 8.4 cm by 3.5 cm. Calculate its area and perimeter.
A: Area \(= 8.4 \times 3.5 = 29.4\,\mathrm{cm^2}\). Perimeter \(= 2(8.4 + 3.5) = 23.8\,\mathrm{cm}\).
Q: Calculate the area of a circular field of view of diameter 0.45 mm.
A: \(r = 0.225\,\mathrm{mm}\). Area \(= \pi \times 0.225^2 = 0.159\,\mathrm{mm^2}\).
Q: A group of 100 fish contained 46 of species X, 32 of species Y, 14 of species Z and 8 of species W. Calculate the angle of the Y sector on a pie chart.
A: \(32 \div 100 \times 360 = 115^\circ\) (115.2 to 3 significant figures is 115°).
Q: A tangent to a curve passes through (2, 6.0) and (8, 15.0). Calculate the rate in cm³ s⁻¹ if the axes are volume in cm³ and time in s.
A: Gradient \(= (15.0 - 6.0) \div (8 - 2) = 1.5\,\mathrm{cm^3\,s^{-1}}\).
:::

The graph below is for the third question of the exam practice.

:::plot Gas collected from a reaction, with a tangent at t = 3 min.
--f "15*(1-exp(0-x/4))" --f "7.914+1.7714*(x-3)+0*sqrt(x)+0*sqrt(8-x)" --label "gas collected" --label "tangent at 3 min" --x 0 12 --y 0 20 --xlabel "time / min" --ylabel "volume of gas / cm³" --pt "3,7.91,touches at 3 min@se" --legend tr --alt "The gas volume rises steeply at first, then more slowly, and levels off near 15 cm cubed. A straight tangent touches the curve at 3 minutes at 7.9 cm cubed and rises to 16.8 cm cubed at 8 minutes."
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ A mitochondrion is 2.5 µm long. Express this length in mm, in standard form.
A: 1 µm \(= 10^{-3}\) mm, so divide by 1000: \(2.5 \div 1000\) [M1] \(= 2.5 \times 10^{-3}\) mm [A1]
Q: [2 marks] ★ A student's resting heart rate was 72 beats per minute. After exercise it was 138 beats per minute. Calculate the percentage increase.
A: \((138 - 72) \div 72 \times 100\) [M1] \(= 91.7\%\) [A1]
Q: [4 marks] ★★ A student counted the stomata in nine fields of view of a leaf: 12, 15, 11, 14, 13, 14, 16, 14 and 12. (a) Calculate the mean number. (b) State the mode and the median. (c) State the range.
H: Put the numbers in order before you look for the median.
A: (a) Sum \(= 121\), mean \(= 121 \div 9\) [M1] \(= 13.4\) [A1]
(b) Mode \(= 14\); median \(= 14\) (ordered: 11, 12, 12, 13, 14, 14, 14, 15, 16, the fifth is 14). [B1]
(c) Range: 11 to 16, or 5. [B1]
Q: [5 marks] ★★ The graph of the volume of gas collected from a reaction is plotted in the graph above these questions, with a tangent drawn at 3 min. (a) The tangent passes through (0, 2.6) and (8, 16.8). Calculate the rate of reaction at 3 min. (b) The mean rate over the first 3 min is greater than the rate at 3 min. Explain why. The gas volume at 3 min is 7.9 cm³.

H: Gradient = change in \(y\) ÷ change in \(x\), read from the two points on the tangent.
H: For (b), think about what happens to the amount of the reactants as the time goes on.
A: (a) Gradient \(= (16.8 - 2.6) \div (8 - 0)\) [M1] \(= 1.8\,\mathrm{cm^3\,min^{-1}}\) [A1] (units needed) [B1]
(b) The mean rate over 3 min is \(7.9 \div 3 = 2.6\,\mathrm{cm^3\,min^{-1}}\), higher than the rate at 3 min, because the rate was higher earlier. [B1]
The reactants were being used up as the reaction went on, so the reaction slowed down. [B1] (Also credit: the gradient of the curve is steepest at 0 min.)
Q: [4 marks] ★★ A student measures 12 cm³ of a solution with a 25 cm³ measuring cylinder marked every 1 cm³. (a) Calculate the percentage error in the reading. (b) Suggest one change that would reduce the percentage error, and explain why it works.
A: (a) Uncertainty \(= \pm 0.5\,\mathrm{cm^3}\) (half a division) [B1]; \(0.5 \div 12 \times 100\) [M1] \(= 4.2\%\) [A1]
(b) Use a 10 cm³ measuring cylinder, or a graduated pipette or syringe, with finer divisions, so the uncertainty is smaller compared with the volume. [B1]
Q: [5 marks] ★★ A cylinder of agar of diameter 1.2 cm and length 4.0 cm has flat ends. (a) Calculate its volume. (b) Calculate its total surface area. (c) Calculate its surface area to volume ratio.
H: The radius is half the diameter. The surface area includes both ends and the curved side.
A: (a) \(V = \pi r^2 h = \pi \times 0.60^2 \times 4.0\) [M1] \(= 4.52\,\mathrm{cm^3}\) [A1]
(b) \(A = 2\pi r^2 + 2\pi r h = 2\pi \times 0.60^2 + 2\pi \times 0.60 \times 4.0\) [M1] \(= 17.3\,\mathrm{cm^2}\) [A1]
(c) \(17.34 \div 4.524 = 3.83\), so \(3.83 : 1\) [A1]
Q: [6 marks] ★★★ A bacterial culture was sampled every 2 hours. The counts were \(2.5 \times 10^{3}\), \(1.6 \times 10^{4}\), \(1.0 \times 10^{5}\) and \(6.4 \times 10^{5}\) cells per cm³ at 0, 2, 4 and 6 hours. (a) Calculate \(\lg\) of the count at each time. (b) Describe how the count changes from one sample to the next, using figures. (c) Explain why plotting \(\lg(\text{count})\) rather than the count is useful here.
H: Use the lg key. Look at the difference between each pair of lg values.
A: (a) \(\lg\) values: 3.40, 4.20, 5.00, 5.81 [B1] [B1] (B1 for any two correct, B1 for all four)
(b) Each count is 6.4 times the one before: \(1.6 \times 10^{4} \div 2.5 \times 10^{3}\) [M1] \(= 6.4\) every 2 hours [A1]
(c) The counts range over several powers of ten, so a normal axis would squash the early values. [B1]
On the lg axis the points fall on a straight line, because equal increases of lg mean equal multiplication of the count. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A student compares the percentage errors of three measurements in an investigation of the mass change of potato discs: a mass of 2.50 g on a balance reading to 0.01 g; a volume of 4.0 cm³ in a syringe marked every 0.1 cm³; and a time of 30 s on a stopwatch reading to 1 s. (a) Calculate the percentage error of each. (b) State which measurement should be improved first and suggest how. (c) Explain why a student who measures the mass of a piece of tissue before and after treatment should be careful to use the same balance both times.
H: Half the smallest division is the uncertainty for each reading.
H: For (c), if the same balance has a fixed error, what happens when you subtract the two readings?
A: (a) Mass: \(0.005 \div 2.50 \times 100 = 0.2\%\) [B1]. Volume: \(0.05 \div 4.0 \times 100 = 1.3\%\) [B1]. Time: \(0.5 \div 30 \times 100 = 1.7\%\) [B1]
(b) The time has the largest percentage error, and the stopwatch is not the problem: the reaction time of the person starting and stopping it is. [B1] Improve by timing a longer period (the same absolute uncertainty becomes a smaller percentage) or by using a data logger. [B1]
(c) A fixed (systematic) error in the balance is the same on both readings and cancels when the difference is found. [B1]
Q: [6 marks] ★★★ Cells in a culture double in number every \(T\) hours. A student plots \(\lg(\text{count})\) against time and gets a straight line with a gradient of 0.15 per hour. (a) Calculate the increase in \(\lg\) when the count doubles (use \(\lg 2 = 0.301\)). (b) Calculate the doubling time \(T\). (c) Calculate the factor by which the count increases in 10 hours.
H: A straight line on this graph means a constant increase of lg per hour.
A: (a) \(\lg 2 = 0.301\), so the lg increases by 0.301 each time the count doubles. [B1] Doubling multiplies the count by 2, and multiplying adds the logs. [B1]
(b) \(T = 0.301 \div 0.15\) [M1] \(= 2.0\) hours [A1]
(c) The lg increases by \(0.15 \times 10 = 1.5\) [M1], a factor of \(10^{1.5} = 32\) [A1]
(Also credit: 5 doublings in 10 hours is \(2^5 = 32\).)
:::

:::quiz
? Which is the correct conversion?
+ 35 µm = 0.035 mm
- 35 µm = 35 000 mm
- 35 µm = 0.35 mm
- 35 µm = 3.5 × 10⁻⁶ mm
> A µm is one-thousandth of a mm, so a length in mm is the number of µm divided by 1000. 35 000 multiplies instead of dividing, and 0.35 divides by 100.
? A value is written \(8.0 \times 10^{-3}\). Which statement is correct?
+ It equals 0.0080.
- It equals 8000.
- It equals 0.080.
- It equals −8.0 × 3.
> A negative power of ten gives a number smaller than 1: \(8.0 \times 10^{-3} = 8.0 \div 1000 = 0.0080\).
? A calculation uses data with 3, 2 and 4 significant figures. How many significant figures should the answer have?
+ 2 or 3
- 3 or 4
- 2 only
- 4 or 5
> The answer matches the least precise data (2 significant figures) or has one more (3). Matching the most precise data claims too much precision.
? The mass of a tissue rose from 5.0 g to 6.0 g. What is the percentage change?
+ +20%
- +17%
- +1.0%
- +100%
> The change is 1.0 g, and 1.0 ÷ 5.0 (the initial mass) × 100 = 20%. Dividing by the final mass gives the wrong 17%.
? A tangent is drawn to a curve of volume against time. What does its gradient give?
+ the rate of reaction at the point where it touches the curve
- the mean rate of reaction over the whole experiment
- the total volume produced
- the time taken for the reaction to finish
> The tangent has the same slope as the curve at one point, so its gradient is the rate at that moment. The mean rate over the whole experiment comes from the chord between its start and its end.
? Which data should be shown on a histogram?
+ the lengths of 80 leaves, grouped into classes of 5 mm
- the number of leaves on each of six tree species
- the mean mass of a plant at five temperatures
- the share of the leaves that are damaged or healthy
> A histogram shows the frequency distribution of continuous data in classes, with the bars touching. Species are categories (bar chart), five temperatures are a continuous independent variable (line graph) and a share of a whole is a pie chart.
? A thermometer is marked every 1 °C. What is the uncertainty of a single reading, and the percentage error for a reading of 20 °C?
+ ±0.5 °C and 2.5%
- ±1 °C and 5.0%
- ±0.5 °C and 0.025%
- ±0.1 °C and 0.5%
> The uncertainty is half the smallest division, 0.5 °C, and \(0.5 \div 20 \times 100 = 2.5\%\). The full division (1 °C) overstates the uncertainty, and 0.025% forgets to multiply by 100.
? What does "y ∝ x" mean?
+ y is directly proportional to x: doubling x doubles y
- y is greater than x
- y is the sum of all the values of x
- y increases by a fixed amount when x increases
> The symbol ∝ means "is directly proportional to", so the graph of y against x is a straight line through the origin. > means "greater than" and Σ means "the sum of".
:::

:::checklist What you can now do
- [ ] I can use the prefixes giga, mega, kilo, milli, micro and nano, convert between units (including cm³ and dm³, and seconds and minutes) and choose sensible units.
- [ ] I can write numbers in decimal and standard form and use a calculator for the arithmetic, squares, square roots, reciprocals, logs and means.
- [ ] I can estimate the result of a calculation and use the estimate to check an answer.
- [ ] I can apply the Cambridge significant figures rule, working with unrounded values and rounding at the end, and record data to a consistent precision.
- [ ] I can use the symbols <, >, ≤, ≥, ∝ and Σ and write table headings and axis labels as quantity / unit.
- [ ] I can calculate and choose between the mean, median, mode and range.
- [ ] I can use ratios and calculate percentages, percentage change and percentage error.
- [ ] I can calculate areas and perimeters of rectangles, triangles and circles, and surface areas and volumes of cuboids and cylinders.
- [ ] I can calculate magnification and actual size.
- [ ] I can choose between a line graph, bar chart, histogram and pie chart, plot data correctly and decide between joining points and drawing a line of best fit.
- [ ] I can find a rate from the gradient of a straight line and from a tangent to a curve, and I can use lg.
:::

:::recap
- Prefixes: G \(10^9\), M \(10^6\), k \(10^3\), m \(10^{-3}\), µ \(10^{-6}\), n \(10^{-9}\). To a smaller unit, multiply; to a larger unit, divide. 1 dm³ = 1000 cm³.
- Standard form: \(a \times 10^n\) with \(1 \le a < 10\). Estimate with one significant figure to check a calculator answer.
- Answers have the same number of significant figures as the least precise data, or one more. Keep full values in the working and round at the end.
- Mean = \(\Sigma x \div n\); median = middle value; mode = most common; range = highest and lowest.
- Percentage change = (final − initial) ÷ initial × 100. Percentage error = uncertainty ÷ reading × 100, with uncertainty = half the smallest division for one reading.
- Circle: \(\pi r^2\) and \(2\pi r\). Cuboid volume \(lwh\). Cylinder volume \(\pi r^2 h\), curved surface \(2\pi r h\), each end \(\pi r^2\). Actual size = image ÷ magnification.
- Line graph for continuous data, bar chart for categories, histogram (touching bars) for frequency of grouped continuous data, pie chart for shares of a whole. Independent variable on the x-axis, axes labelled quantity / unit.
- Rate from a gradient: change in \(y\) ÷ change in \(x\). On a curve, use a tangent, not a chord, and read points on the tangent.
- \(\lg\) is the power of 10; \(\mathrm{pH} = -\lg[\ce{H+}]\).
:::

:::links
- practise: [Practical skills and maths: topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/practical-skills/) · Physics & Maths Tutor · notes and questions on handling data
- practise: [Topic questions (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topic-questions/) · Save My Exams · exam-style questions with mark schemes, some free [paid]
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [CAIE A Level Biology notes](https://znotes.org/caie/as-biology-9700/) · ZNotes · concise AS notes for revision
- papers: [Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-2/) · Physics & Maths Tutor · look for the calculation questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Practical skills: investigations (Paper 3)](#bio.practical)
