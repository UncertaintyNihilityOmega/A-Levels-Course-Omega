@chapter chem.states
@title States of matter
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 5–7 hours
@summary Why gases exert pressure, when a real gas behaves like an ideal one, and how to use pV = nRT to find volumes, amounts and relative molecular masses. You will also meet the four types of solid structure (giant ionic, simple molecular, giant molecular and giant metallic) and use them to explain and predict melting points, conductivity and solubility.

:::why
Almost everything you can touch is a gas, a liquid or a solid, and its behaviour is decided by how its particles are arranged and how strongly they attract each other. The gas laws let chemists work out how much gas a reaction makes (an airbag, a fire extinguisher, a car exhaust), and the four structure types explain why diamond cuts glass, graphite writes on paper, salt dissolves in water and iodine turns to a purple vapour when warmed. Examiners ask both kinds of question every year, and the "explain the property" answers all follow the same pattern that you will learn here.
:::

**Before you start**, you should know how to calculate amounts in moles from [Moles and stoichiometry](#chem.moles), and the forces between molecules from [Shapes of molecules and intermolecular forces](#chem.shapes) and [Chemical bonding](#chem.bonding).

:::try Warm-up
Q: Calculate the amount of carbon dioxide in 4.40 g of \(\ce{CO2}\). (from [Moles and stoichiometry](#chem.moles))
A: \(M_r = 12.0 + 2(16.0) = 44.0\), so \(n = 4.40 / 44.0 = 0.100\) mol.
Q: What type of force acts between non-polar molecules such as \(\ce{I2}\), and is it stronger or weaker than a covalent bond? (from [Shapes of molecules and intermolecular forces](#chem.shapes))
A: Instantaneous dipole–induced dipole (id-id) forces. They are much weaker than the covalent bond inside each molecule.
Q: Name the type of bonding in magnesium oxide and name the particles it contains. (from [Chemical bonding](#chem.bonding))
A: Ionic bonding: magnesium ions \(\ce{Mg^2+}\) and oxide ions \(\ce{O^2-}\), held together by strong electrostatic attraction.
:::

## Three states, one idea

Every substance can be a solid, a liquid or a gas. The difference is a contest between two things: the energy the particles have (they are always moving) and the attraction between them.

| State | Particle arrangement | Particle movement | Attraction between particles |
|---|---|---|---|
| solid | fixed positions, usually a regular pattern | vibrate about fixed positions | strong enough to hold the particles in place |
| liquid | close together, no pattern | slide past each other | strong enough to keep them touching |
| gas | far apart, no pattern | fast, random and in straight lines between collisions | too weak to matter |

Heating a solid gives its particles more energy, until they can break free from their neighbours and it melts. Heating a liquid until the particles escape from each other makes it boil. The stronger the attractions, the more energy this takes, so the higher the melting point and boiling point. The second half of this chapter uses that idea to explain the properties of solids. The first half studies gases, where the attractions are small enough to ignore, at least to start with.

## The particle picture of a gas

### Why a gas exerts pressure

The particles of a gas move randomly at high speed in every direction. They collide with each other and with the walls of their container. Each collision with a wall pushes on it a little. A gas contains vast numbers of particles, so there are billions of collisions every second, and together they make a steady push on the whole wall.

:::def Gas pressure
The force per unit area exerted by a gas on the walls of its container, caused by the collisions of gas molecules with the walls. It is measured in pascals (Pa), where 1 Pa = 1 N m⁻².
:::

This picture explains how pressure changes without any formula:

- **Push the same gas into a smaller volume.** The molecules have less distance to travel between collisions with the walls, so they hit the walls more often. The pressure rises.
- **Heat the gas at constant volume.** The molecules move faster, so they hit the walls more often and harder. The pressure rises.
- **Add more gas.** There are more molecules, so there are more collisions. The pressure rises.

Temperature measures the average kinetic energy of the particles. At 0 K (−273 °C) particle motion would stop, which is why gas calculations use the kelvin scale, where the temperature in kelvin is the temperature in °C plus 273.

### The ideal gas

Real gases are complicated: their molecules attract each other and take up space. Chemists therefore invent a simpler model gas that obeys a simple equation exactly.

:::def Ideal gas
A gas that obeys the equation \(pV = nRT\) at all temperatures and pressures. The molecules of an ideal gas have zero volume (they are points) and there are no forces of attraction between them.
:::

An ideal gas does not exist, but many real gases at ordinary conditions behave almost like one. The model is useful because those two assumptions make the mathematics simple. Both are only approximately true for real gas molecules, and the next section shows where they stop working.

## When a real gas is not ideal

A real gas molecule has a volume, and real molecules attract each other. Both of these are small effects at room temperature and atmospheric pressure, because the molecules are then very far apart compared with their size. They become important in two situations.

| Condition | What goes wrong | Effect |
|---|---|---|
| **High pressure** | The molecules are squeezed close together. The volume of the molecules is no longer negligible compared with the volume of the container. | The real gas takes up more volume than the ideal equation predicts. |
| **Low temperature** | The molecules move slowly. Their kinetic energy is too small to ignore the attractions between them, so the molecules pull on each other. | The real gas has a lower pressure than the ideal equation predicts, and at a low enough temperature it condenses to a liquid. |

:::key When does a gas behave most like an ideal gas?
At **low pressure** (the molecules are far apart, so their own volume is negligible) and **high temperature** (the molecules move so fast that the attractions between them have little effect).
:::

Some gases are closer to ideal than others. Helium and hydrogen, with very few electrons, have very weak id-id forces, so they stay close to ideal behaviour over a wide range of conditions. Ammonia has hydrogen bonds between its molecules (see [Shapes of molecules and intermolecular forces](#chem.shapes)), so it deviates much more, and it is easy to liquefy.

:::warn Two separate reasons
"Real gases deviate because of intermolecular forces" is only half of the answer. Examiners want both causes: the molecules have **volume** (important at high pressure) and there are **attractive forces** between them (important at low temperature). Link each cause to its condition.
:::

## The ideal gas equation

### The equation and its units

For an ideal gas, four quantities are linked by one equation.

:::formula The ideal gas equation
\[pV = nRT\]
\(p\) = pressure in pascals (Pa), \(V\) = volume in cubic metres (m³), \(n\) = amount of gas in moles, \(R\) = the gas constant, 8.31 J K⁻¹ mol⁻¹, \(T\) = temperature in kelvin (K).
:::

The equation only works with these units. Most exam questions give the pressure, volume or temperature in other units, so the first step is always to convert.

| Quantity | Given as | Convert to | How |
|---|---|---|---|
| temperature | °C | K | add 273 (25 °C = 298 K) |
| pressure | kPa | Pa | × 1000 (101 kPa = 101 000 Pa) |
| volume | dm³ | m³ | ÷ 1000 (1 dm³ = 10⁻³ m³) |
| volume | cm³ | m³ | ÷ 1 000 000 (1 cm³ = 10⁻⁶ m³) |

:::warn The unit traps
Three slips cost marks in nearly every set of answers: using the temperature in °C, leaving the volume in dm³ or cm³, and leaving the pressure in kPa. If you put every quantity in SI units (Pa, m³, K), the answer comes out in the right unit with no further thought. The volume then comes out in m³, and you convert it back to dm³ (× 1000) or cm³ (× 1 000 000) at the end.
:::

You will rearrange the equation in three ways, depending on the unknown:

\[V = \frac{nRT}{p} \qquad n = \frac{pV}{RT} \qquad T = \frac{pV}{nR}\]

:::eg Calculate the volume of 0.0500 mol of a gas at 298 K and 101 kPa. Give the answer in dm³.
The pressure is \(p = 101\,000\) Pa and \(T = 298\) K, both in SI units already.
\[V = \frac{nRT}{p} = \frac{0.0500 \times 8.31 \times 298}{101\,000} = 1.226 \times 10^{-3}\,\mathrm{m^3}\] [M1] [A1]
Convert to dm³: \(1.226 \times 10^{-3} \times 1000 = 1.23\,\mathrm{dm^3}\). [A1]
:::

### Checking the molar volume

In [Moles and stoichiometry](#chem.moles) you used "24.0 dm³ per mole at room conditions" and "22.4 dm³ at s.t.p." Those numbers come from \(pV = nRT\) with \(n = 1\). At 298 K and 101 kPa:

\[V = \frac{1 \times 8.31 \times 298}{101\,000} = 0.02452\,\mathrm{m^3} = 24.5\,\mathrm{dm^3}\]

The value 24.0 dm³ mol⁻¹ in the Data section matches a room temperature of about 20 °C (293 K). At s.t.p. (273 K and 101 kPa) the same calculation gives 22.5 dm³; the Data section's 22.4 dm³ mol⁻¹ comes from more precise values (R = 8.314, T = 273.15 K, p = 101.325 kPa). When a question says "at room temperature and pressure", use 24.0 dm³ mol⁻¹. When it gives you a temperature and a pressure, use \(pV = nRT\).

### Using pV = nRT

:::eg A 250 cm³ flask contains 0.608 g of a gas at 27 °C and a pressure of 152 kPa. Calculate the amount of gas, then its relative molecular mass, and identify the gas.
Convert to SI units: \(T = 27 + 273 = 300\) K, \(p = 152\,000\) Pa, \(V = 250 \times 10^{-6} = 2.50 \times 10^{-4}\,\mathrm{m^3}\). [B1]
\[n = \frac{pV}{RT} = \frac{152\,000 \times 2.50 \times 10^{-4}}{8.31 \times 300} = 0.01524\,\mathrm{mol}\] [M1]
\[M_r = \frac{m}{n} = \frac{0.608}{0.01524} = 39.9\] [M1] [A1]
The relative atomic mass of argon is 39.9, and a noble gas is a single atom, so the gas is argon.
:::

Notice that the question asked for \(M_r\) and the calculation went through \(n\). You can also combine the two steps. Because \(n = m / M_r\), the equation becomes \(pV = \dfrac{m}{M_r}RT\), so:

:::formula Relative molecular mass of a gas
\[M_r = \frac{mRT}{pV}\]
\(m\) = mass of the gas in grams, with \(p\) in Pa, \(V\) in m³ and \(T\) in K. The result is in g mol⁻¹, and it is the relative molecular mass when written without units.
:::

If a question gives the **density** of a gas, \(\rho\) in g dm⁻³, then \(m / V\) equals \(\rho\) per dm³, so use \(\rho \times 1000\) in g m⁻³: \(M_r = \dfrac{(\rho \times 1000)RT}{p}\).

### A ratio shortcut

When the amount of gas stays the same and only conditions change, \(pV = nRT\) says that \(pV/T\) is constant. If the volume is fixed as well, then \(p/T\) is constant.

:::eg A sealed 2.00 dm³ container of gas is at 300 K and 100 kPa. It is heated to 360 K. What is the new pressure?
The amount \(n\) and the volume \(V\) do not change, so \(p / T\) is constant. [M1]
\[p_2 = p_1 \times \frac{T_2}{T_1} = 100 \times \frac{360}{300} = 120\,\mathrm{kPa}\] [A1]
Temperatures must be in kelvin here as well. The result also fits the particle picture: faster molecules hit the walls harder and more often.
:::

### Finding the relative molecular mass of a volatile liquid

How does a chemist find the \(M_r\) of an unknown liquid in the laboratory? Use a liquid that boils below about 100 °C, vaporise a known mass of it, and measure the volume of the vapour.

:::lab Mr of a volatile liquid with a gas syringe
Draw about 0.2 g of the liquid into a small syringe or sealed capsule and weigh it exactly. Inject the sample through a rubber septum into a gas syringe sitting in an oven or heating jacket at a temperature above the liquid's boiling point (for example 373 K, with the actual temperature read on a thermometer). The liquid vaporises, and the plunger moves out. Wait until the volume stops changing, then read the volume and record the pressure of the room from a barometer. Weigh the empty syringe again to find the exact mass of liquid used. Safety: the oven and syringe are hot, so use tongs or heat-resistant gloves, and keep flammable liquids away from naked flames.
:::

:::eg 0.240 g of a volatile liquid was vaporised in a gas syringe. The vapour had a volume of 83.0 cm³ at 373 K and a pressure of 101 kPa. The empirical formula of the liquid is \(\ce{C2H4O}\). Find its relative molecular mass and its molecular formula.
Convert: \(V = 83.0 \times 10^{-6} = 8.30 \times 10^{-5}\,\mathrm{m^3}\) and \(p = 101\,000\) Pa. [B1]
\[M_r = \frac{mRT}{pV} = \frac{0.240 \times 8.31 \times 373}{101\,000 \times 8.30 \times 10^{-5}} = 88.7\] [M1] [A1]
The empirical formula mass of \(\ce{C2H4O}\) is \(2(12.0) + 4(1.0) + 16.0 = 44.0\). [B1]
\(88.7 / 44.0 = 2.02\), which is 2 to the nearest whole number, so the molecular formula is \(\ce{C4H8O2}\). [A1]
:::

:::eg (Real context) Many driver airbags are inflated by nitrogen made when sodium azide, \(\ce{NaN3}\), decomposes in a few hundredths of a second: \(\ce{2NaN3 -> 2Na + 3N2}\). Calculate the volume of nitrogen at 350 K and 101 kPa made from 65.0 g of sodium azide.
\(M_r(\ce{NaN3}) = 23.0 + 3(14.0) = 65.0\), so \(n(\ce{NaN3}) = 65.0 / 65.0 = 1.00\) mol. [B1]
From the equation, 2 mol of \(\ce{NaN3}\) gives 3 mol of \(\ce{N2}\), so \(n(\ce{N2}) = 1.00 \times 3/2 = 1.50\) mol. [M1]
\[V = \frac{nRT}{p} = \frac{1.50 \times 8.31 \times 350}{101\,000} = 0.04320\,\mathrm{m^3} = 43.2\,\mathrm{dm^3}\] [M1] [A1]
The hot gas fills a bag of this size, which is why a small solid charge can protect a driver. The sodium metal that also forms is made harmless by a second reaction in the airbag unit.
:::

Here is the same idea as an experiment you can try on screen. The physics course has an ideal gas widget that links all four variables.

:::html
<div class="widget" data-w="phys-gas"></div>
:::

Try changing the temperature at constant volume and watch the pressure; then compress the gas at constant temperature. If the widget does not load, the two ratio examples above show the same results.

## Four types of structure

Gases are the easy case, because the particles hardly interact. In solids they interact strongly, and what matters is **which** particles are in the solid and **what** holds them together. All solids you need fall into four types.

:::def Giant ionic lattice
A regular three-dimensional arrangement of positive and negative ions, held together by strong electrostatic attraction between oppositely charged ions. Examples: NaCl and MgO.
:::

:::def Simple molecular structure
A structure made of separate small molecules, with strong covalent bonds inside each molecule and only weak intermolecular forces between the molecules. Examples: \(\ce{I2}\), buckminsterfullerene \(\ce{C60}\), ice.
:::

:::def Giant molecular structure (giant covalent structure)
A huge network of atoms held together by covalent bonds throughout the whole structure. There are no separate molecules. Examples: diamond, graphite and silicon(IV) oxide, \(\ce{SiO2}\).
:::

:::def Giant metallic lattice
A regular lattice of positive metal ions surrounded by a "sea" of delocalised electrons. The metallic bond is the electrostatic attraction between the positive ions and the delocalised electrons. Example: copper.
:::

### Giant ionic: sodium chloride and magnesium oxide

In sodium chloride the \(\ce{Na+}\) and \(\ce{Cl-}\) ions alternate in all three directions, like a three-dimensional chessboard. Each \(\ce{Na+}\) is surrounded by six \(\ce{Cl-}\) ions and each \(\ce{Cl-}\) by six \(\ce{Na+}\) ions. Magnesium oxide has the same arrangement, with \(\ce{Mg^2+}\) and \(\ce{O^2-}\). The figure below shows a flat slice of the pattern.

:::html
<figure class="fig"><svg viewBox="0 20 610 215" role="img" aria-label="Left: a flat slice of the sodium chloride lattice, a four by four grid of alternating small positive sodium ions and larger negative chloride ions. Right: a four by four grid of positive copper ions with small delocalised electrons between them"><circle class="f1 s-acc sw2" cx="69" cy="40" r="9"/><text class="tl tc" x="69" y="45">+</text><circle class="f2 s-acc sw2" cx="103" cy="40" r="13"/><text class="tl tc" x="103" y="45">−</text><circle class="f1 s-acc sw2" cx="137" cy="40" r="9"/><text class="tl tc" x="137" y="45">+</text><circle class="f2 s-acc sw2" cx="171" cy="40" r="13"/><text class="tl tc" x="171" y="45">−</text><circle class="f2 s-acc sw2" cx="69" cy="74" r="13"/><text class="tl tc" x="69" y="79">−</text><circle class="f1 s-acc sw2" cx="103" cy="74" r="9"/><text class="tl tc" x="103" y="79">+</text><circle class="f2 s-acc sw2" cx="137" cy="74" r="13"/><text class="tl tc" x="137" y="79">−</text><circle class="f1 s-acc sw2" cx="171" cy="74" r="9"/><text class="tl tc" x="171" y="79">+</text><circle class="f1 s-acc sw2" cx="69" cy="108" r="9"/><text class="tl tc" x="69" y="113">+</text><circle class="f2 s-acc sw2" cx="103" cy="108" r="13"/><text class="tl tc" x="103" y="113">−</text><circle class="f1 s-acc sw2" cx="137" cy="108" r="9"/><text class="tl tc" x="137" y="113">+</text><circle class="f2 s-acc sw2" cx="171" cy="108" r="13"/><text class="tl tc" x="171" y="113">−</text><circle class="f2 s-acc sw2" cx="69" cy="142" r="13"/><text class="tl tc" x="69" y="147">−</text><circle class="f1 s-acc sw2" cx="103" cy="142" r="9"/><text class="tl tc" x="103" y="147">+</text><circle class="f2 s-acc sw2" cx="137" cy="142" r="13"/><text class="tl tc" x="137" y="147">−</text><circle class="f1 s-acc sw2" cx="171" cy="142" r="9"/><text class="tl tc" x="171" y="147">+</text><text class="tl tc" x="120" y="186">sodium chloride, NaCl</text><circle class="f1 s-acc sw2" cx="62" cy="212" r="9"/><text class="tl" x="76" y="217">Na⁺</text><circle class="f2 s-acc sw2" cx="130" cy="212" r="13"/><text class="tl" x="147" y="217">Cl⁻</text><circle class="fm s-acc sw2" cx="369" cy="40" r="10"/><text class="tl tc" x="369" y="45">+</text><circle class="fm s-acc sw2" cx="403" cy="40" r="10"/><text class="tl tc" x="403" y="45">+</text><circle class="fm s-acc sw2" cx="437" cy="40" r="10"/><text class="tl tc" x="437" y="45">+</text><circle class="fm s-acc sw2" cx="471" cy="40" r="10"/><text class="tl tc" x="471" y="45">+</text><circle class="fm s-acc sw2" cx="369" cy="74" r="10"/><text class="tl tc" x="369" y="79">+</text><circle class="fm s-acc sw2" cx="403" cy="74" r="10"/><text class="tl tc" x="403" y="79">+</text><circle class="fm s-acc sw2" cx="437" cy="74" r="10"/><text class="tl tc" x="437" y="79">+</text><circle class="fm s-acc sw2" cx="471" cy="74" r="10"/><text class="tl tc" x="471" y="79">+</text><circle class="fm s-acc sw2" cx="369" cy="108" r="10"/><text class="tl tc" x="369" y="113">+</text><circle class="fm s-acc sw2" cx="403" cy="108" r="10"/><text class="tl tc" x="403" y="113">+</text><circle class="fm s-acc sw2" cx="437" cy="108" r="10"/><text class="tl tc" x="437" y="113">+</text><circle class="fm s-acc sw2" cx="471" cy="108" r="10"/><text class="tl tc" x="471" y="113">+</text><circle class="fm s-acc sw2" cx="369" cy="142" r="10"/><text class="tl tc" x="369" y="147">+</text><circle class="fm s-acc sw2" cx="403" cy="142" r="10"/><text class="tl tc" x="403" y="147">+</text><circle class="fm s-acc sw2" cx="437" cy="142" r="10"/><text class="tl tc" x="437" y="147">+</text><circle class="fm s-acc sw2" cx="471" cy="142" r="10"/><text class="tl tc" x="471" y="147">+</text><circle class="fi" cx="381" cy="57" r="2.5"/><circle class="fi" cx="420" cy="52" r="2.5"/><circle class="fi" cx="459" cy="57" r="2.5"/><circle class="fi" cx="391" cy="91" r="2.5"/><circle class="fi" cx="420" cy="86" r="2.5"/><circle class="fi" cx="454" cy="86" r="2.5"/><circle class="fi" cx="391" cy="130" r="2.5"/><circle class="fi" cx="420" cy="120" r="2.5"/><circle class="fi" cx="449" cy="125" r="2.5"/><text class="tl tc" x="420" y="186">copper, Cu</text><circle class="fm s-acc sw2" cx="330" cy="212" r="10"/><text class="tl tc" x="330" y="217">+</text><text class="tl" x="345" y="217">metal ion</text><circle class="fi" cx="430" cy="212" r="2.5"/><text class="tl" x="440" y="217">delocalised electron</text></svg><figcaption>Left: a flat slice through the sodium chloride lattice. Positive and negative ions alternate, so every ion is next to ions of the opposite charge. Right: a slice through a metal such as copper, with positive ions in fixed positions and small delocalised electrons that can move between them.</figcaption></figure>
:::

### Simple molecular: iodine, buckminsterfullerene and ice

**Iodine** is made of \(\ce{I2}\) molecules. The two atoms in each molecule are joined by a strong covalent bond, but the molecules are held to each other only by weak id-id forces. When iodine is warmed it turns directly from a solid to a purple vapour (it **sublimes**), because only the weak id-id forces have to be overcome. The I–I bonds are not broken.

**Buckminsterfullerene**, \(\ce{C60}\), is a ball of 60 carbon atoms, like a football made of hexagons and pentagons, with strong covalent bonds inside the ball. Each ball is a separate molecule and the balls attract each other only by id-id forces. So \(\ce{C60}\) is **simple molecular**, even though it is made of one element and the molecule is large. It is a solid at room temperature because 60 carbon atoms have many electrons, and so the id-id forces between the balls are strong enough to hold them in a solid.

**Ice** is made of water molecules joined by hydrogen bonds. Each water molecule forms hydrogen bonds to four others, two through its hydrogen atoms and two through the lone pairs on its oxygen atom. The molecules sit in an open arrangement of rings with empty space in the middle of each ring. When ice melts, some of the hydrogen bonds break and the molecules move closer together. That is why ice is **less dense** than liquid water and floats on it.

### Giant molecular: diamond, graphite and silicon(IV) oxide

In **diamond** every carbon atom forms four covalent bonds to four other carbon atoms, in a tetrahedral arrangement. The bonds continue in every direction, so a diamond is one giant molecule. There are no free electrons, because all four outer electrons of each carbon atom are in bonds.

In **graphite** every carbon atom forms three covalent bonds to three others, in flat layers of hexagons. The fourth outer electron of each carbon atom is **delocalised**: it is free to move anywhere along its layer. (Diagrams, like the one below, often draw these electrons between the layers.) The layers are held together only by weak id-id forces.

:::html
<figure class="fig"><svg viewBox="0 25 640 185" role="img" aria-label="Left: one layer of graphite seen from above, a flat sheet of joined hexagons of carbon atoms. Right: three layers of graphite seen from the side, with delocalised electrons between the layers"><path class="ln thick" d="M60 46L39 58L39 82L60 94L81 82L81 58Z"/><path class="ln thick" d="M102 46L81 58L81 82L102 94L122 82L122 58Z"/><path class="ln thick" d="M143 46L122 58L122 82L143 94L164 82L164 58Z"/><path class="ln thick" d="M81 82L60 94L60 118L81 130L102 118L102 94Z"/><path class="ln thick" d="M122 82L102 94L102 118L122 130L143 118L143 94Z"/><path class="ln thick" d="M60 118L39 130L39 154L60 166L81 154L81 130Z"/><path class="ln thick" d="M102 118L81 130L81 154L102 166L122 154L122 130Z"/><path class="ln thick" d="M143 118L122 130L122 154L143 166L164 154L164 130Z"/><text class="tl tc" x="101" y="190">one layer, from above</text><path class="ln thick" d="M226 60H366"/><path class="ln thick" d="M226 110H366"/><path class="ln thick" d="M226 160H366"/><circle class="f1 s-acc sw2" cx="236" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="256" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="276" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="296" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="316" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="336" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="356" cy="60" r="5"/><circle class="f1 s-acc sw2" cx="236" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="256" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="276" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="296" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="316" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="336" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="356" cy="110" r="5"/><circle class="f1 s-acc sw2" cx="236" cy="160" r="5"/><circle class="f1 s-acc sw2" cx="256" cy="160" r="5"/><circle class="f1 s-acc sw2" cx="276" cy="160" r="5"/><circle class="f1 s-acc sw2" cx="296" cy="160" r="5"/><circle class="f1 s-acc sw2" cx="316" cy="160" r="5"/><circle class="f1 s-acc sw2" cx="336" cy="160" r="5"/><circle class="f1 s-acc sw2" cx="356" cy="160" r="5"/><circle class="fi" cx="240" cy="85" r="2.5"/><circle class="fi" cx="262" cy="85" r="2.5"/><circle class="fi" cx="284" cy="85" r="2.5"/><circle class="fi" cx="306" cy="85" r="2.5"/><circle class="fi" cx="328" cy="85" r="2.5"/><circle class="fi" cx="350" cy="85" r="2.5"/><circle class="fi" cx="240" cy="135" r="2.5"/><circle class="fi" cx="262" cy="135" r="2.5"/><circle class="fi" cx="284" cy="135" r="2.5"/><circle class="fi" cx="306" cy="135" r="2.5"/><circle class="fi" cx="328" cy="135" r="2.5"/><circle class="fi" cx="350" cy="135" r="2.5"/><text class="tl" x="378" y="64">strong covalent bonds in a layer</text><text class="tl" x="378" y="89">delocalised electrons</text><text class="tl" x="378" y="139">weak id-id forces between layers</text><text class="tl tc" x="296" y="190">three layers, from the side</text></svg><figcaption>Graphite. Left: each carbon atom is bonded to three others in a flat sheet of hexagons. Right: the sheets stack with delocalised electrons between them, held together only by weak forces, so the layers can slide over each other.</figcaption></figure>
:::

**Silicon(IV) oxide**, \(\ce{SiO2}\) (the main compound in sand and quartz), has a structure like diamond: every silicon atom is bonded to four oxygen atoms, and every oxygen atom is bonded to two silicon atoms, in a network that continues throughout the crystal. The formula \(\ce{SiO2}\) shows only the ratio of atoms, because there are no separate \(\ce{SiO2}\) molecules.

### Giant metallic: copper

A metal is a lattice of positive ions in fixed positions. Each copper atom has given up some of its outer electrons, and these electrons are delocalised: they no longer belong to one atom but move freely through the whole lattice. The metallic bond is the attraction between the positive ions and this sea of electrons. It acts in all directions, so the lattice is held together strongly.

## Structure explains properties

The properties of a solid depend on **what must be overcome** when it melts, dissolves or conducts. Work through the same three questions for every substance: what particles are present, what holds them together, and are any charged particles free to move?

### Melting point and boiling point

| Structure | What is overcome when it melts | Melting point |
|---|---|---|
| giant ionic | strong electrostatic attraction between oppositely charged ions throughout the lattice | high |
| simple molecular | only weak intermolecular forces between molecules (id-id, pd-pd or hydrogen bonds); the covalent bonds inside the molecules stay intact | low |
| giant molecular | strong covalent bonds throughout the structure | very high |
| giant metallic | strong attraction between the positive ions and the delocalised electrons | usually high |

Magnesium oxide melts at a higher temperature than sodium chloride because its ions have charges of 2+ and 2− instead of 1+ and 1−, which makes the electrostatic attraction in the lattice stronger (see [Lattice energy and Born–Haber cycles](#chem.lattice)). Among simple molecular substances, the melting point rises with the number of electrons (stronger id-id forces) and rises when hydrogen bonds are present, so \(\ce{I2}\) is a solid and ice melts at 0 °C, but \(\ce{H2}\) and \(\ce{N2}\) are gases at room temperature.

:::warn Melting never breaks covalent bonds in a simple molecular substance
"Iodine has a low melting point because the covalent bonds are weak" is wrong. The I–I bonds are strong and are not broken at all when iodine melts or sublimes. Say "weak id-id forces **between** the molecules". For giant molecular substances the opposite is true: the covalent bonds themselves must be broken, and that is why the melting points are so high.
:::

### Electrical conductivity

A substance conducts electricity when it contains charged particles that are free to move: electrons or ions.

| Structure | Solid | Molten or dissolved |
|---|---|---|
| giant ionic | does not conduct: ions are fixed in the lattice | conducts: ions are free to move |
| simple molecular | does not conduct: no charged particles | does not conduct (neutral molecules), unless it reacts with water to form ions |
| diamond, \(\ce{SiO2}\) | does not conduct: all electrons are held in bonds | does not conduct |
| graphite | conducts: delocalised electrons move along the layers | (does not melt under normal conditions) |
| giant metallic | conducts: delocalised electrons are free to move | conducts |

### Solubility

Dissolving needs the particles of the substance to be pulled apart and surrounded by solvent molecules, and the attractions to the solvent must pay back the energy spent separating the solute.

- **Giant ionic** solids usually dissolve in water. Water is polar, so its δ− oxygen atoms are attracted to positive ions and its δ+ hydrogen atoms to negative ions. This attraction is strong enough to pull ions out of the lattice. Many ionic compounds with highly charged ions, such as MgO, are insoluble because the lattice attraction is too strong.
- **Simple molecular** substances: those with polar molecules, or those that can form hydrogen bonds with water, dissolve in water. Non-polar substances such as \(\ce{I2}\) do not dissolve well in water, but dissolve in non-polar solvents like hexane, where they form id-id forces with the solvent.
- **Giant molecular** substances do not dissolve in water or in any ordinary solvent: no solvent can pay back the energy of breaking covalent bonds.
- **Metals** do not dissolve in water or organic solvents; some react with water or acids instead.

:::key Properties of the four types
| Structure | Examples | m.p. and b.p. | Conductivity | Solubility in water |
|---|---|---|---|---|
| giant ionic | NaCl, MgO | high | solid: no; molten or dissolved: yes | often soluble |
| simple molecular | \(\ce{I2}\), \(\ce{C60}\), ice | low | no | polar: soluble; non-polar: insoluble |
| giant molecular | diamond, graphite, \(\ce{SiO2}\) | very high | graphite only (solid) | insoluble |
| giant metallic | Cu | high | yes (solid and molten) | insoluble |
:::

### Explaining the special cases

:::eg Explain why graphite conducts electricity but diamond does not. [3 marks]
In graphite, each carbon atom forms only three covalent bonds, so one outer electron per atom is not used in bonding. [B1]
These electrons are delocalised between the layers and are free to move through the structure, so they carry the current. [B1]
In diamond, every carbon atom forms four covalent bonds, so all the outer electrons are held in bonds and none are free to move. [B1]
:::

:::eg Explain why ice is less dense than liquid water. [2 marks]
In ice, each water molecule is held by hydrogen bonds in an open lattice with empty space between the molecules. [B1]
When ice melts, some hydrogen bonds break and the molecules move closer together, so the same number of molecules occupies a smaller volume and liquid water is denser. [B1]
:::

:::eg Explain why graphite is soft and slippery but diamond is the hardest natural substance. [3 marks]
In graphite, the layers are held by only weak id-id forces, so they slide over each other easily. [B1]
In diamond every carbon is held by four strong covalent bonds in all directions. [B1]
Moving any atom would require breaking strong bonds, so diamond is very hard. [B1]
:::

## Deducing structure and bonding from data

Exam questions give you properties (melting point, conductivity, solubility) and ask what the structure is. Use the questions in order.

:::steps
1. Does it conduct as a **solid**? If yes it is a metal (it also conducts when molten) or graphite (it does not melt readily and is soft). Metals are shiny and malleable.
2. If it does not conduct as a solid, does it conduct when **molten or dissolved**? If yes, it is **giant ionic**: ions are free to move only when the lattice is broken up.
3. If it never conducts, look at the melting point. **Very high** (above about 1000 °C) and insoluble means **giant molecular**. **Low** means **simple molecular**.
4. Check the solubility for confirmation: soluble in water and conducting when dissolved points to ionic; soluble only in non-polar solvents points to simple molecular.
:::

:::eg The table shows data for this question. Deduce the structure and bonding of each substance, A to E.
| Substance | m.p. / °C | Conducts as solid? | Conducts when molten? | Soluble in water? |
|---|---|---|---|---|
| A | 800 | no | yes | yes |
| B | 1090 | yes | yes | no |
| C | 114 | no | no | no |
| D | 1700 | no | no | no |
| E | does not melt below 3500 | yes | (not melted) | no |

A conducts only when molten and dissolves, so it is **giant ionic**: ions free to move only when the lattice is broken. [B1]
B conducts as a solid and when molten, so it is **giant metallic**, with delocalised electrons. [B1]
C has a low melting point and does not conduct, so it is **simple molecular** (the molecules are held by weak intermolecular forces). [B1]
D has a high melting point and does not conduct or dissolve, so it is **giant molecular** (a covalent network, like \(\ce{SiO2}\)). [B1]
E conducts as a solid but has an extremely high melting point and is insoluble: **graphite** (giant molecular with delocalised electrons). [B1]
:::

:::eg Spot the error: explain why silicon(IV) oxide has a much higher melting point than solid carbon dioxide. [3 marks]
A student wrote this answer.

Line 1: \(\ce{SiO2}\) is a giant molecular structure, with every silicon atom bonded to four oxygen atoms in a network.
Line 2: To melt it, the many strong Si–O covalent bonds must be broken, which needs a lot of energy.
Line 3: \(\ce{CO2}\) is simple molecular, so when it sublimes the C=O covalent bonds break, but these are weaker than the Si–O bonds.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: the C=O bonds inside each \(\ce{CO2}\) molecule are strong and are not broken when solid carbon dioxide sublimes. Only the weak id-id forces between the molecules are overcome. The mark is lost [B0].**

Correct line 3: \(\ce{CO2}\) is simple molecular, so only weak id-id forces between molecules are overcome, which needs little energy. [B1]

The student scores 2 out of 3. Whenever a question compares a simple molecular substance with a giant one, say clearly which interactions are overcome: forces between molecules, or covalent bonds.
:::

:::tip Answer pattern for "explain the property"
Name the structure, say which particles are present, say what holds them together (or what is free to move), and link that to the property. For example: "NaCl is a giant ionic lattice. The strong electrostatic attraction between oppositely charged ions needs much energy to overcome, so the melting point is high."
:::

:::try Start easy, finish at exam standard
Q: Convert: (a) 250 cm³ to m³, (b) 2.5 dm³ to m³, (c) 25 °C to K, (d) 120 kPa to Pa.
A: (a) \(250 \times 10^{-6} = 2.50 \times 10^{-4}\,\mathrm{m^3}\). (b) \(2.5 \times 10^{-3}\,\mathrm{m^3}\). (c) 298 K. (d) \(1.20 \times 10^5\) Pa.
Q: Use the particle picture to explain why the pressure of a gas rises when it is compressed into a smaller volume at constant temperature.
A: The molecules have the same average speed but less distance to travel between collisions with the walls, so they collide with the walls more often. More collisions per second per unit area means a higher pressure.
Q: Calculate the volume of 0.200 mol of a gas at 350 K and 100 kPa, in dm³.
A: \(V = nRT / p = 0.200 \times 8.31 \times 350 / 100\,000 = 5.817 \times 10^{-3}\,\mathrm{m^3} = 5.82\,\mathrm{dm^3}\).
Q: How many moles of gas are in a 500 cm³ flask at 20 °C and 101 kPa?
A: \(T = 293\) K, \(V = 5.00 \times 10^{-4}\,\mathrm{m^3}\), \(p = 101\,000\) Pa. \(n = pV/RT = 101\,000 \times 5.00 \times 10^{-4} / (8.31 \times 293) = 0.0207\) mol.
Q: 0.350 g of a gas occupies 215 cm³ at 300 K and 101 kPa. Calculate its relative molecular mass.
A: \[M_r = \frac{mRT}{pV} = \frac{0.350 \times 8.31 \times 300}{101\,000 \times 2.15 \times 10^{-4}} = 40.2\]
Q: Classify each as giant ionic, simple molecular, giant molecular or giant metallic: (a) MgO, (b) \(\ce{C60}\), (c) \(\ce{SiO2}\), (d) Cu, (e) ice.
A: (a) giant ionic. (b) simple molecular. (c) giant molecular. (d) giant metallic. (e) simple molecular, with hydrogen bonds between the molecules.
Q: Explain why solid sodium chloride does not conduct electricity but molten sodium chloride does.
A: In the solid the ions are held in fixed positions in the lattice, so no charged particles can move. When molten, the lattice has broken up and the ions are free to move and carry the current.
Q: Iodine sublimes easily when warmed, but diamond does not melt at any ordinary temperature. Explain the difference.
A: Iodine is simple molecular: only weak id-id forces between \(\ce{I2}\) molecules are overcome, which takes little energy. Diamond is giant molecular: the strong covalent bonds throughout the structure would all have to be broken.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State two assumptions made about particles in an ideal gas.
A: The particles have zero volume (they are points). [B1]
There are no forces of attraction between the particles. [B1]
Q: [4 marks] ★ Calculate the volume, in cm³, of 0.640 g of oxygen gas, \(\ce{O2}\), at 300 K and 100 kPa.
A: \(M_r(\ce{O2}) = 32.0\), so \(n = 0.640 / 32.0 = 0.0200\) mol. [B1]
\(V = nRT / p\) with \(p = 100\,000\) Pa. [M1]
\(V = 0.0200 \times 8.31 \times 300 / 100\,000 = 4.986 \times 10^{-4}\,\mathrm{m^3}\) [M1]
\(= 499\,\mathrm{cm^3}\) [A1]
Q: [4 marks] ★★ 0.139 g of a volatile liquid was vaporised and the vapour had a volume of 60.0 cm³ at 373 K and 100 kPa. Calculate the relative molecular mass of the liquid.
H: Convert the volume to m³ and the pressure to Pa first.
A: \(V = 60.0 \times 10^{-6} = 6.00 \times 10^{-5}\,\mathrm{m^3}\) and \(p = 100\,000\) Pa. [B1]
\(n = pV / RT = 100\,000 \times 6.00 \times 10^{-5} / (8.31 \times 373) = 1.936 \times 10^{-3}\) mol [M1]
\(M_r = m / n = 0.139 / 1.936 \times 10^{-3}\) [M1]
\(= 71.8\) [A1]
Q: [4 marks] ★★ (#chem.moles) Calcium carbonate is heated strongly: \(\ce{CaCO3 -> CaO + CO2}\). Calculate the volume of carbon dioxide, in dm³, formed from 2.50 g of calcium carbonate at 1000 K and 101 kPa.
H: Work out the amount of \(\ce{CaCO3}\) first, then use the 1 : 1 ratio.
A: \(M_r(\ce{CaCO3}) = 40.1 + 12.0 + 3(16.0) = 100.1\). [B1]
\(n(\ce{CO2}) = n(\ce{CaCO3}) = 2.50 / 100.1 = 0.02498\) mol [M1]
\(V = nRT / p = 0.02498 \times 8.31 \times 1000 / 101\,000\) [M1]
\(= 2.055 \times 10^{-3}\,\mathrm{m^3} = 2.05\,\mathrm{dm^3}\) [A1]
Q: [3 marks] ★★ Explain why a real gas deviates from ideal behaviour at high pressure and at low temperature.
A: At high pressure the molecules are close together, so the volume of the molecules is no longer negligible compared with the volume of the container. [B1]
At low temperature the molecules move slowly, so the attractive forces between molecules become significant. [B1]
These cause the real gas to deviate from \(pV = nRT\) (the volume is larger at high pressure; at low temperature the pressure is lower and the gas can condense). [B1]
Q: [5 marks] ★★ Substances W, X, Y and Z have these properties. W: melting point 3550 °C, does not conduct, insoluble. X: melting point 115 °C, does not conduct, insoluble in water but soluble in hexane. Y: melting point 990 °C, does not conduct as a solid but conducts when molten, soluble in water. Z: melting point 1060 °C, conducts as a solid, insoluble. Identify the structure of each and explain the melting point of W and of X.
H: Use the order of the questions in the "Deducing structure" steps.
A: W is giant molecular, X is simple molecular, Y is giant ionic and Z is giant metallic. [B1] [B1] (B1 for any two correct, B1 for all four)
W has strong covalent bonds throughout the structure, which need a large amount of energy to break. [B1]
X has only weak intermolecular forces between molecules, which are easily overcome. [B1]
The covalent bonds within the molecules of X are not broken on melting. [B1]
Q: [6 marks] ★★★ Compare the structures of diamond, graphite and buckminsterfullerene, \(\ce{C60}\), and use them to explain why diamond is hard, graphite conducts and \(\ce{C60}\) has a lower melting point than diamond.
H: Each carbon atom forms a different number of covalent bonds in each. Decide whether each is giant or simple.
A: Diamond: each carbon forms four covalent bonds in a giant tetrahedral network, so it is hard. [B1] [B1] (B1 for the structure, B1 for the explanation)
Graphite: each carbon forms three covalent bonds in layers and has one delocalised electron, which can move and so conducts. [B1] [B1]
\(\ce{C60}\) is simple molecular: separate molecules joined by weak id-id forces. [B1]
Only these weak forces are overcome when it melts or sublimes, not covalent bonds, so the melting point is much lower than diamond. [B1]
Q: [6 marks] ★★★ (#chem.moles) A hydrocarbon gas has a density of 2.35 g dm⁻³ at 300 K and 101 kPa. It contains 82.8% carbon by mass, the rest being hydrogen. Calculate its relative molecular mass, then find its empirical formula and molecular formula.
H: Density in g dm⁻³ multiplied by 1000 gives g m⁻³.
H: Divide each percentage by the Ar to get a ratio, then scale to whole numbers.
A: \(M_r = \rho RT / p = 2350 \times 8.31 \times 300 / 101\,000\) [M1] \(= 58.0\) [A1]
C : H ratio \(= 82.8 / 12.0 : 17.2 / 1.0 = 6.90 : 17.2 = 1 : 2.49\) [M1]
Multiplying by 2 gives 2 : 5, so the empirical formula is \(\ce{C2H5}\). [A1]
The empirical formula mass is 29.0, and \(58.0 / 29.0 = 2\) [B1], so the molecular formula is \(\ce{C4H10}\). [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ In the gas syringe experiment, the end of the syringe outside the oven is cooler than the oven, and a small fraction of the vapour condenses there before the volume is read. A student whose liquid has a true \(M_r\) of 88.7 loses 5.0% of the vapour in this way. Explain the effect on the calculated \(M_r\) and calculate the value the student would report.
H: The mass of liquid used does not change. What happens to the volume, and so to \(n\)?
A: The volume of vapour measured is smaller than it should be, so the calculated \(n = pV/RT\) is too small. [B1]
\(M_r = m / n\), so the calculated \(M_r\) is too large. [B1]
Only 95.0% of the vapour is measured, so \(n\) is 0.950 of the true amount. [M1]
Reported \(M_r = 88.7 / 0.950 = 93.4\). [A1]
Q: [6 marks] ★★★ The molar volume of an ideal gas at 298 K and 101 kPa is about 24.5 dm³. One mole of liquid water, \(M_r = 18.0\), has a volume of 18.0 cm³ (density 1.00 g cm⁻³). (a) Calculate the volume of 1.00 mol of an ideal gas at 298 K and 101 kPa and the percentage of it that could be occupied by the molecules themselves, if the liquid volume is taken as the greatest volume the molecules can take up. (b) The pressure is raised 100-fold at constant temperature. Calculate the new percentage for an ideal gas, and explain what this shows about real gases at high pressure.
H: Pressure up by 100 means the volume of an ideal gas falls by 100.
A: (a) \(V = 1 \times 8.31 \times 298 / 101\,000 = 0.02452\,\mathrm{m^3} = 24\,520\,\mathrm{cm^3}\). [M1] [A1] (M1 for the substitution, A1 for the volume)
Percentage \(= 18.0 / 24\,520 \times 100 = 0.0734\%\). [M1]
(b) New volume \(= 24\,520 / 100 = 245.2\,\mathrm{cm^3}\), so the percentage \(= 18.0 / 245.2 \times 100 = 7.34\%\). [A1]
At 100 times the pressure the molecules fill an upper limit of about 7% of the space, so their own volume can no longer be ignored. [B1]
This is why the ideal gas equation, which assumes zero particle volume, fails at high pressure. [B1]
:::

:::quiz
? What causes the pressure of a gas?
+ Collisions of gas molecules with the walls of the container
- The weight of the gas pressing down on the container
- Collisions between gas molecules
- Repulsion between gas molecules
> Pressure is the force per unit area from molecules hitting the walls. Collisions between molecules do not touch the walls, and ideal gas molecules have no forces between them at all.
? Under which conditions does a real gas behave most like an ideal gas?
- High pressure and low temperature
- High pressure and high temperature
- Low pressure and low temperature
+ Low pressure and high temperature
> Low pressure keeps the molecules far apart (their volume is negligible), and high temperature makes them fast enough to ignore the attractions.
? What is the volume of 1.00 mol of an ideal gas at 300 K and 100 kPa?
- 0.0249 dm³
- 22.4 dm³
+ 24.9 dm³
- 24 900 dm³
> \(V = 8.31 \times 300 / 100\,000 = 0.02493\,\mathrm{m^3} = 24.9\,\mathrm{dm^3}\). 0.0249 forgets to convert m³ to dm³, 22.4 is the s.t.p. value (273 K), and 24 900 uses 100 instead of 100 000 for the pressure.
? Which of these substances conducts electricity when solid?
- sodium chloride
- diamond
+ graphite
- silicon(IV) oxide
> Graphite has delocalised electrons that move along its layers. Sodium chloride conducts only when molten or dissolved, while diamond and \(\ce{SiO2}\) have no free electrons or ions.
? What happens to the bonds when iodine sublimes?
- The covalent bonds between iodine atoms break.
+ The weak id-id forces between \(\ce{I2}\) molecules are overcome.
- The ionic bonds in the lattice break.
- Hydrogen bonds between \(\ce{I2}\) molecules break.
> Iodine is simple molecular. Only the weak forces between molecules are overcome; each \(\ce{I2}\) molecule stays intact, so the vapour is made of \(\ce{I2}\) molecules.
? Which statement about \(\ce{C60}\) is correct?
- It is a giant covalent structure, like diamond.
+ It is simple molecular, with weak forces between its molecules.
- It is metallic, because it contains only one element.
- It conducts electricity as delocalised electrons move between the atoms.
> \(\ce{C60}\) consists of separate balls of 60 atoms, so it is simple molecular with a much lower melting point than diamond.
? Why is ice less dense than liquid water?
+ Hydrogen bonds hold the molecules in an open lattice with empty spaces.
- Ice molecules are larger than water molecules.
- There are fewer hydrogen bonds in the liquid, so the molecules are further apart.
- Ice has covalent bonds between the molecules.
> In ice every molecule is hydrogen-bonded to four others in an open arrangement. On melting, some bonds break and molecules pack more closely.
:::

:::checklist What you can now do
- [ ] I can explain gas pressure in terms of collisions of gas molecules with the walls of the container.
- [ ] I can state the two assumptions of an ideal gas (zero particle volume and no intermolecular forces) and explain when and why real gases deviate (high pressure, low temperature).
- [ ] I can use \(pV = nRT\) in SI units to find a volume, an amount, a pressure or a temperature.
- [ ] I can find the relative molecular mass of a volatile liquid from the mass, volume, temperature and pressure of its vapour using \(M_r = mRT/pV\).
- [ ] I can describe the structures of giant ionic (NaCl, MgO), simple molecular (\(\ce{I2}\), \(\ce{C60}\), ice), giant molecular (\(\ce{SiO2}\), graphite, diamond) and giant metallic (Cu) substances.
- [ ] I can explain the melting point, boiling point, electrical conductivity and solubility of each type in terms of structure and bonding.
- [ ] I can deduce the structure and bonding of a substance from given data.
:::

:::recap
- Gas pressure comes from molecules colliding with the walls of the container. Temperature in kelvin is °C + 273.
- An ideal gas has zero particle volume and no intermolecular forces. A real gas is most ideal at low pressure and high temperature, and deviates at high pressure (molecules have volume) and low temperature (molecules attract each other).
- \(pV = nRT\) with p in Pa, V in m³, T in K, R = 8.31 J K⁻¹ mol⁻¹. 1 dm³ = 10⁻³ m³ and 1 cm³ = 10⁻⁶ m³. \(M_r = mRT/pV\). At 298 K and 101 kPa the molar volume is 24.5 dm³; 24.0 dm³ is used at "room temperature and pressure".
- Giant ionic (NaCl, MgO): high m.p.; conducts only when molten or dissolved; often soluble in water.
- Simple molecular (\(\ce{I2}\), \(\ce{C60}\), ice): low m.p. because only weak forces between molecules are overcome (covalent bonds stay); does not conduct. \(\ce{C60}\) is simple molecular. Ice is less dense than water because of its open hydrogen-bonded lattice.
- Giant molecular (diamond, graphite, \(\ce{SiO2}\)): very high m.p., covalent bonds broken; insoluble. Diamond does not conduct; graphite conducts through delocalised electrons and is soft because the layers slide.
- Giant metallic (Cu): positive ions in a sea of delocalised electrons; conducts as a solid; high m.p.; insoluble.
- Deduce structures from: conducts as solid? conducts molten or dissolved? melting point?
:::

:::links
- read: [Ideal gases](https://www.chemguide.co.uk/physical/kt/idealgases.html) · Chemguide · the ideal gas equation and the assumptions behind it, with worked examples
- read: [Giant covalent structures](https://www.chemguide.co.uk/atoms/structures/giantcov.html) · Chemguide · diamond, graphite and silicon dioxide explained with diagrams
- read: [Molecular structures](https://www.chemguide.co.uk/atoms/structures/molecular.html) · Chemguide · simple molecular substances, their melting points and why they do not conduct
- read: [Ionic structures](https://www.chemguide.co.uk/atoms/structures/ionicstruct.html) · Chemguide · the sodium chloride lattice and why ionic solids melt at high temperatures
- practise: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [Chemical energetics](#chem.energetics) shows how much energy is released or absorbed when particles rearrange in a reaction.
