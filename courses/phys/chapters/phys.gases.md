@chapter phys.gases
@title Ideal gases
@level a2
@paper CAIE P4 (A Level) · P5
@time 6–8 hours
@summary How to count particles with the mole, the gas laws and the ideal gas equation of state in two forms (pV = nRT and pV = NkT), the assumptions of the kinetic theory, the derivation of pV = ⅓Nm⟨c²⟩ from molecules hitting a wall, the root-mean-square speed, and why the mean kinetic energy of a molecule is (3/2)kT.

:::why
The air in a bicycle tyre, the gas in a camping stove, the atmosphere of a planet and the helium in a balloon all obey the same few rules. This chapter takes you from experiments you can do with a syringe to a result that links the large-scale pressure of a gas to the speeds of its invisible molecules. It is one of the most powerful ideas in physics: the pressure and the temperature that we measure are the average effect of enormous numbers of tiny collisions.
:::

**Before you start**, you need temperature and the kelvin scale from [Temperature](#phys.temperature), force as the rate of change of momentum from [Dynamics and momentum](#phys.dynamics), and pressure as force per unit area from [Forces, density and pressure](#phys.forces).

:::try Warm-up
Q: Convert 27 °C to kelvin. (from [Temperature](#phys.temperature))
A: \(T = 27 + 273.15 = 300\,\mathrm{K}\) (300.15 K before rounding).
Q: A ball of mass 0.20 kg hits a wall at \(5.0\,\mathrm{m\,s^{-1}}\) and rebounds along the same line at the same speed. What is the change in its momentum? (from [Dynamics and momentum](#phys.dynamics))
A: Taking the initial direction as positive, \(\Delta p = m(-v) - mv = -2mv\), so the magnitude is \(2 \times 0.20 \times 5.0 = 2.0\,\mathrm{kg\,m\,s^{-1}}\).
Q: A force of 240 N acts on an area of \(0.0040\,\mathrm{m^2}\). What pressure does it exert? (from [Forces, density and pressure](#phys.forces))
A: \(p = F/A = 240/0.0040 = 6.0 \times 10^{4}\,\mathrm{Pa}\).
:::

## The mole and the Avogadro constant

A glass of water contains about \(10^{25}\) molecules. Counting them one at a time is hopeless, so physicists count in large batches called **moles**, in the same way that you buy eggs by the dozen. Amount of substance is a base quantity in the SI system, with symbol \(n\) and base unit the **mole** (mol).

:::def Mole
The amount of substance that contains as many particles as there are atoms in 0.012 kg of carbon-12.
:::

:::def Avogadro constant
The number of particles in one mole of a substance: \(N_A = 6.02 \times 10^{23}\,\mathrm{mol^{-1}}\).
:::

One mole of any substance contains \(N_A\) particles, whether they are atoms, molecules or electrons. The particles could be atoms (helium) or molecules (nitrogen, \(\mathrm{N_2}\)); say which. The number of particles \(N\) in an amount \(n\) is

\[N = nN_A\]

The **molar mass** \(M\) is the mass of one mole, in \(\mathrm{kg\,mol^{-1}}\). Helium has \(M = 0.0040\,\mathrm{kg\,mol^{-1}}\), nitrogen (\(\mathrm{N_2}\)) \(0.028\), oxygen (\(\mathrm{O_2}\)) \(0.032\). Questions give you these. From \(M\) you can find the number of moles in a mass \(m_\text{total}\) of gas, and the mass of one molecule:

\[n = \frac{m_\text{total}}{M} \qquad\qquad m = \frac{M}{N_A}\]

:::warn Four symbols, four meanings
\(n\) is the number of **moles**, \(N\) is the number of **molecules**, \(M\) is the mass of one **mole** (kg per mol) and \(m\) is the mass of one **molecule** (kg). Mixing them up is the commonest source of wrong powers of ten. Molar mass is often written in g per mol in a data table: always change it to kg per mol.
:::

:::eg A sample of helium has a mass of 2.0 g. Calculate the number of atoms in the sample, and the mass of one helium atom. Take \(M = 0.0040\,\mathrm{kg\,mol^{-1}}\).
\[n = \frac{m_\text{total}}{M} = \frac{2.0 \times 10^{-3}}{0.0040} = 0.50\,\mathrm{mol}\] [C1]
\[N = nN_A = 0.50 \times 6.02 \times 10^{23} = 3.0 \times 10^{23}\] [A1]
\[m = \frac{M}{N_A} = \frac{0.0040}{6.02 \times 10^{23}} = 6.6 \times 10^{-27}\,\mathrm{kg}\] [A1]
Check with atomic mass units: a helium atom has a mass of about 4 u, and \(4 \times 1.66 \times 10^{-27} = 6.6 \times 10^{-27}\,\mathrm{kg}\).
:::

## The gas laws

Three experimental laws describe how a **fixed mass** of gas behaves when two of the three quantities pressure \(p\), volume \(V\) and temperature \(T\) change. In every case the temperature must be a thermodynamic temperature in kelvin.

- **Boyle's law:** at constant temperature, the pressure of a fixed mass of gas is inversely proportional to its volume: \(pV = \) constant.
- **Charles's law:** at constant pressure, the volume of a fixed mass of gas is proportional to its thermodynamic temperature: \(V \propto T\).
- **The pressure law:** at constant volume, the pressure of a fixed mass of gas is proportional to its thermodynamic temperature: \(p \propto T\).

:::plot Pressure against volume for a fixed mass of gas at two temperatures. Each curve has pV constant, 200 J at 300 K and 300 J at 450 K. The higher temperature gives the upper curve.
--f "200/x" --f "300/x" --x 1 10 --y 0 320 --pt "4,50,T = 300 K@sw" --pt "4,75,T = 450 K@ne" --xlabel "V / L" --ylabel "p / kPa"
:::

Each curve is called an **isotherm** (constant temperature). Plot \(p\) against \(1/V\) instead and each is a straight line through the origin, with gradient equal to the constant \(pV\).

:::lab Boyle's law with a syringe
:::steps
1. Trap a known volume of air in a syringe whose tip is joined by a short rigid tube to a pressure gauge. Make sure there are no leaks.
2. Push the plunger in slowly, so the air stays at room temperature, and wait a few seconds before each reading. Record the volume \(V\) from the syringe scale and the pressure \(p\) from the gauge, for at least six volumes.
3. Include the volume of the connecting tube in \(V\), or plot against the syringe volume and accept an intercept.
4. Plot \(p\) against \(1/V\). A straight line through the origin shows \(pV\) is constant, and the gradient is \(pV\), which equals \(nRT\).
:::
Moving the plunger slowly matters, because compressing a gas warms it. Wait until the gas is again at room temperature, otherwise the temperature is not constant and the law appears not to hold.
:::

### The pressure law and absolute zero

Seal a fixed mass of gas in a flask of constant volume. Warm it in a water bath and measure its pressure at several Celsius temperatures. The graph is a straight line, but it does not pass through the origin of the Celsius axis. Extend the line backwards, **extrapolating** it, and it reaches zero pressure at \(-273\,^\circ\mathrm{C}\). Whatever the gas and however much there is, the lines meet the axis at the same temperature.

:::html
<figure class="fig"><svg viewBox="20 24 640 232" role="img" aria-label="A graph of pressure against Celsius temperature for a gas at constant volume. A solid straight line runs from 0 to 100 degrees Celsius, rising from 100 to 137 kilopascals. A dashed extension of the line goes down to the temperature axis at minus 273 degrees Celsius, where the pressure is zero."><path class="ax" d="M60 200H600M450 200V36"/><path class="c1 dash" d="M94.9 200L450 90"/><path class="c1" d="M450 90L580 49.7"/><path class="ln-m thin" d="M94.9 200V206M190 200V206M320 200V206M450 200V206M580 200V206M445 90H450"/><text class="ts tc" x="94.9" y="220">−273</text><text class="ts tc" x="190" y="220">−200</text><text class="ts tc" x="320" y="220">−100</text><text class="ts tc" x="450" y="220">0</text><text class="ts tc" x="580" y="220">100</text><text class="ts te" x="441" y="94">100</text><text class="tl" x="606" y="204">θ / °C</text><text class="tl" x="458" y="46">p / kPa</text><text class="tl tc" x="95" y="242">absolute zero</text><text class="tl tc" x="290" y="176">extrapolated</text><text class="tl tc" x="520" y="112">readings</text></svg><figcaption>For a fixed mass of gas at constant volume the pressure rises in equal steps with the Celsius temperature. The readings (solid) can only be taken between the freezing and boiling points of the water bath, but the straight line extrapolates (dashed) to zero pressure at −273 °C. If the axis is changed to \(T/\mathrm{K} = \theta/^\circ\mathrm{C} + 273.15\), the line passes through the origin and \(p \propto T\).</figcaption></figure>
:::

This is the experimental reason for the thermodynamic scale. Pressure cannot be negative, so there is a lowest possible temperature, at which the pressure of an ideal gas would fall to zero. This is **absolute zero**. On the kelvin scale, \(0\,\mathrm{K} = -273.15\,^\circ\mathrm{C}\), the same graph passes through the origin, and \(p \propto T\) is a direct proportion. The same happens with volume at constant pressure (Charles's law). Real gases condense into liquids before they get that cold, so the experiment only extrapolates.

:::lab The pressure law and absolute zero
:::steps
1. Seal a flask of air to a pressure gauge or sensor with a short length of tube. Immerse the flask up to its neck in a water bath with a thermometer.
2. Stir the bath and wait for thermal equilibrium: gas, flask and water must all be at the thermometer's temperature. Record \(p\) and \(\theta\).
3. Warm the bath in steps of about 10 °C up to about 90 °C. At each step stir and wait, then record \(p\) and \(\theta\).
4. Plot \(p\) against \(\theta\) and draw the best-fit straight line. Extend it back until \(p = 0\); the intercept on the \(\theta\) axis is the temperature of absolute zero, about \(-273\,^\circ\mathrm{C}\). Plotting \(p\) against \(T = \theta + 273.15\) gives a line through the origin.
:::
Keep the volume of tube outside the bath small: that gas is at room temperature and would spoil the constant-volume assumption. Stir to avoid the gas being cooler than the thermometer. The long extrapolation magnifies small errors in the gradient, so the intercept is only roughly \(-273\,^\circ\mathrm{C}\).
:::

## The ideal gas equation of state

Combine the three laws for a fixed mass of gas and you find that \(pV/T\) is constant. Doubling the amount of gas at the same \(p\) and \(T\) doubles \(V\), so \(pV\) must be proportional to the amount too.

:::def Ideal gas
A gas that obeys \(pV \propto T\) (that is, \(pV = nRT\)) at all pressures, volumes and temperatures, where \(T\) is the thermodynamic temperature.
:::

:::formula Equation of state of an ideal gas
\[pV = nRT \qquad\qquad pV = NkT\]
\(p\): pressure (Pa) · \(V\): volume (\(\mathrm{m^3}\)) · \(n\): amount of gas (mol) · \(R\): molar gas constant \(8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}\) · \(T\): thermodynamic temperature (K) · \(N\): number of molecules · \(k\): Boltzmann constant \(1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}\). The two forms are linked by \(k = R/N_A\).
:::

Both forms are the same law, because \(n = N/N_A\) gives \(nR = (N/N_A)R = Nk\). The Boltzmann constant is the gas constant **per molecule**: \(k = \dfrac{R}{N_A} = \dfrac{8.31}{6.02 \times 10^{23}} = 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}\). Use \(pV = nRT\) when you are given moles and \(pV = NkT\) when you are given a number of molecules.

Real gases follow the ideal law closely when the pressure is low and the temperature is high compared with the temperature at which they liquefy. Then the molecules are far apart, so their size and the forces between them hardly matter. Air at room temperature and atmospheric pressure is close to ideal. At high pressure or near the boiling point, the molecules are close together and a real gas deviates.

:::steps
1. Write down the equation and which form you will use, \(nRT\) or \(NkT\).
2. Change everything to SI: pressure in Pa (1 kPa = 1000 Pa), volume in \(\mathrm{m^3}\) (\(1\,\mathrm{L} = 10^{-3}\,\mathrm{m^3}\); \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\)), temperature in **kelvin**, mass in kg.
3. Rearrange for the unknown and substitute. Keep full precision; round at the end.
:::

:::eg Calculate the number of molecules in 1.0 \(\mathrm{m^3}\) of air at a pressure of \(1.01 \times 10^{5}\,\mathrm{Pa}\) and a temperature of 20 °C.
\(T = 20 + 273.15 = 293.15\,\mathrm{K}\). [C1]
\[N = \frac{pV}{kT} = \frac{1.01 \times 10^{5} \times 1.0}{1.38 \times 10^{-23} \times 293.15}\] [C1]
\[N = 2.5 \times 10^{25}\] [A1]
That is about \(2.5 \times 10^{19}\) molecules in every cubic millimetre of the air around you.
:::

:::eg A gas cylinder of volume 0.020 \(\mathrm{m^3}\) contains helium at a pressure of \(1.5 \times 10^{7}\,\mathrm{Pa}\) and a temperature of 15 °C. Calculate the mass of helium, and the pressure if the cylinder is heated to 40 °C. (\(M = 0.0040\,\mathrm{kg\,mol^{-1}}\))
\(T_1 = 288.15\,\mathrm{K}\) and \(T_2 = 313.15\,\mathrm{K}\).
\[n = \frac{pV}{RT} = \frac{1.5 \times 10^{7} \times 0.020}{8.31 \times 288.15} = 125\,\mathrm{mol}\] [C1]
\[m_\text{total} = nM = 125.3 \times 0.0040 = 0.50\,\mathrm{kg}\] [A1]
The volume and amount are fixed, so \(p \propto T\):
\[p_2 = p_1 \times \frac{T_2}{T_1} = 1.5 \times 10^{7} \times \frac{313.15}{288.15} = 1.6 \times 10^{7}\,\mathrm{Pa}\] [A1]
:::

### Changes of state of a fixed mass

When the mass of gas is fixed, \(n\) does not change and \(\dfrac{pV}{T}\) is constant:

\[\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}\]

Pressure and volume can be in any units that are the same on both sides, because the units cancel in the ratio. The temperature must always be in kelvin.

:::eg An air bubble of volume 4.0 \(\mathrm{cm^3}\) forms at the bottom of a lake, where the pressure is \(3.0 \times 10^{5}\,\mathrm{Pa}\) and the temperature is 280 K. It rises to the surface, where the pressure is \(1.0 \times 10^{5}\,\mathrm{Pa}\) and the temperature is 290 K. Find the volume of the bubble at the surface.
\[\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}\] [C1]
\[V_2 = V_1 \times \frac{p_1}{p_2} \times \frac{T_2}{T_1} = 4.0 \times \frac{3.0 \times 10^{5}}{1.0 \times 10^{5}} \times \frac{290}{280}\] [C1]
\[V_2 = 12\,\mathrm{cm^3}\] [A1] (12.4 before rounding)
Pressure falling to a third would triple the volume; the warmer water adds the small extra factor 290/280.
:::

:::eg A car tyre contains air at an absolute pressure of \(2.0 \times 10^{5}\,\mathrm{Pa}\) when the temperature is 10 °C. After a long drive the temperature of the air is 35 °C. Assuming the volume is constant, find the new pressure.
Constant volume and amount, so \(p \propto T\). \(T_1 = 283.15\,\mathrm{K}\) and \(T_2 = 308.15\,\mathrm{K}\). [C1]
\[p_2 = p_1 \times \frac{T_2}{T_1} = 2.0 \times 10^{5} \times \frac{308.15}{283.15}\] [C1]
\[p_2 = 2.2 \times 10^{5}\,\mathrm{Pa}\] [A1]
:::

:::warn Absolute and gauge pressure
Tyre gauges show the pressure **above** atmospheric pressure. The gas laws need the absolute pressure: add atmospheric pressure (about \(1.0 \times 10^{5}\,\mathrm{Pa}\)) to a gauge reading before you use them. Questions that give "absolute pressure" or the pressure "of the gas" mean the full value.
:::

When the amount of gas changes (a leak, or a pump), use \(pV = nRT\) before and after. At constant \(V\) and \(T\), the amount \(n\) is proportional to the pressure.

:::eg An oxygen cylinder of volume 0.040 \(\mathrm{m^3}\) is at a pressure of \(3.2 \times 10^{5}\,\mathrm{Pa}\) at 290 K. After some of the gas has been used, the pressure is \(2.0 \times 10^{5}\,\mathrm{Pa}\) at the same temperature. Calculate the mass of oxygen used. (\(M = 0.032\,\mathrm{kg\,mol^{-1}}\))
At the same \(V\) and \(T\), \(n = pV/(RT)\), so the amount used is
\[\Delta n = \frac{\Delta p\,V}{RT} = \frac{(3.2 - 2.0) \times 10^{5} \times 0.040}{8.31 \times 290}\] [C1]
\[\Delta n = 1.99\,\mathrm{mol}\] [A1]
The mass used is \(\Delta n\,M = 1.99 \times 0.032 = 0.064\,\mathrm{kg}\) (64 g). [A1]
:::

A useful variant gives the density of a gas. With \(n = m_\text{total}/M\) the equation of state is \(pV = \dfrac{m_\text{total}}{M}RT\), so the density is

\[\rho = \frac{m_\text{total}}{V} = \frac{pM}{RT}\]

At the same \(p\) and \(T\), a gas with a larger molar mass is denser. That is why helium balloons rise in air.

:::eg Calculate the density of nitrogen (\(M = 0.028\,\mathrm{kg\,mol^{-1}}\)) at \(1.01 \times 10^{5}\,\mathrm{Pa}\) and 300 K.
\[\rho = \frac{pM}{RT} = \frac{1.01 \times 10^{5} \times 0.028}{8.31 \times 300}\] [C1]
\[\rho = 1.1\,\mathrm{kg\,m^{-3}}\] [A1] (1.13 before rounding)
:::

## The kinetic theory of gases

The ideal gas law describes how a gas behaves. The kinetic theory explains **why**, by modelling the gas as a huge number of tiny moving particles. The model has a list of assumptions, and you need to state them in exam wording.

:::key Basic assumptions of the kinetic theory of an ideal gas
1. A gas contains a very large number of molecules, in continuous random motion.
2. The volume of the molecules is negligible compared with the volume of the container.
3. There are no forces between molecules, except during a collision.
4. Collisions between molecules, and with the walls, are perfectly elastic.
5. The time of a collision is negligible compared with the time between collisions.
6. Newton's laws of motion apply to the molecules.
:::

"Molecules are very small" earns nothing: say that their **volume** is negligible compared with that of the container. Assumption 3 means a molecule between collisions moves in a straight line at constant speed. In an ideal gas the molecules have no potential energy, and the internal energy is purely kinetic.

### How molecules create pressure

A molecule that hits the wall of its container and rebounds has had its momentum changed by the wall. By Newton's second law, the wall exerts a force on the molecule, and by Newton's third law the molecule exerts an equal and opposite force on the wall.

1. A molecule collides with the wall and rebounds, so its momentum changes.
2. The rate of change of momentum is a force on the molecule, and an equal and opposite force acts on the wall.
3. There are enormous numbers of collisions every second on every part of the wall, so the forces blend into a steady force. The force per unit area is the pressure.

Heating the gas makes the molecules faster, so each collision has a larger change of momentum and collisions are more frequent, so the pressure rises. Reducing the volume makes collisions with a wall more frequent for the same speeds, so the pressure rises too. That is Boyle's law.

:::html
<figure class="fig"><svg viewBox="40 30 340 176" role="img" aria-label="A box of side L with a molecule moving to the right between two opposite walls. An arrow labelled before points right towards the right wall with momentum plus m c x. A second arrow labelled after points left away from the right wall with momentum minus m c x. A dimension arrow below shows the length L."><rect class="fp s-mute sw1" x="60" y="50" width="300" height="110"/><path class="ln thick" d="M60 50V160M360 50V160"/><circle class="fi" cx="130" cy="105" r="5"/><path class="c1" d="M200 85H350" marker-end="url(#ah-phys)"/><path class="c2" d="M350 125H200" marker-end="url(#ah2-phys)"/><text class="tl tc" x="275" y="77">before: +mc<tspan dy="4" font-size="10">x</tspan></text><text class="tl tc" x="275" y="150">after: −mc<tspan dy="4" font-size="10">x</tspan></text><path class="c1" d="M210 186H62" marker-end="url(#ah-phys)"/><path class="c1" d="M210 186H358" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="210" y="180">L</text></svg><figcaption>One molecule travelling along the \(x\) direction between two walls a distance \(L\) apart. At the right-hand wall its momentum changes from \(+mc_x\) to \(-mc_x\), a change of magnitude \(2mc_x\). The two arrows show the same path before and after the collision.</figcaption></figure>
:::

:::html
<figure class="fig small"><svg viewBox="70 60 250 200" role="img" aria-label="A box in three dimensions with a long arrow c from one bottom corner to the opposite top corner. Three shorter arrows along the box edges from that corner are labelled c x, c y and c z. The velocity c is the diagonal of the box whose edges are c x, c y and c z."><path class="ln thin dash" d="M100 120H220M160 190H280M160 90H280M160 90V190M220 120V220M280 90V190M100 120L160 90M220 120L280 90M220 220L280 190M160 190L100 220M100 220V120M100 220H220"/><path class="c1" d="M100 220L280 90" marker-end="url(#ah-phys)"/><path class="c2" d="M100 220H218" marker-end="url(#ah2-phys)"/><path class="c2" d="M100 220V122" marker-end="url(#ah2-phys)"/><path class="c2" d="M100 220L158 191" marker-end="url(#ah2-phys)"/><text class="tl ti" x="288" y="88">c</text><text class="tl tc" x="160" y="240">c<tspan dy="4" font-size="10">x</tspan></text><text class="tl te" x="92" y="172">c<tspan dy="4" font-size="10">y</tspan></text><text class="tl" x="164" y="207">c<tspan dy="4" font-size="10">z</tspan></text></svg><figcaption>A molecule's velocity \(c\) is the diagonal of a box whose edges are its components \(c_x\), \(c_y\) and \(c_z\). By Pythagoras in three dimensions, \(c^2 = c_x^2 + c_y^2 + c_z^2\).</figcaption></figure>
:::

:::proof examinable The pressure of an ideal gas: \(pV = \tfrac13 Nm\langle c^2\rangle\)
A cube of side \(L\) (volume \(V = L^3\)) contains \(N\) molecules, each of mass \(m\). Look first at one molecule with velocity components \(c_x\), \(c_y\), \(c_z\) and at the walls perpendicular to \(x\).
The collision with the wall is elastic, so \(c_x\) reverses. The momentum changes from \(+mc_x\) to \(-mc_x\), a change of magnitude \(2mc_x\).
The molecule crosses to the opposite wall and back, a distance \(2L\) at speed \(c_x\), so the time between collisions with the same wall is \(t = 2L/c_x\).
The average force on the wall is the rate of change of momentum: \(F = \dfrac{2mc_x}{2L/c_x} = \dfrac{mc_x^2}{L}\).
The area of the wall is \(L^2\), so the pressure from this molecule is \(\dfrac{mc_x^2}{L^3} = \dfrac{mc_x^2}{V}\).
For all \(N\) molecules, add the contributions: \(p = \dfrac{m}{V}\left(c_{x1}^2 + c_{x2}^2 + \dots\right) = \dfrac{Nm}{V}\langle c_x^2\rangle\), where \(\langle c_x^2\rangle\) is the mean value of \(c_x^2\).
For each molecule \(c^2 = c_x^2 + c_y^2 + c_z^2\), so \(\langle c^2\rangle = \langle c_x^2\rangle + \langle c_y^2\rangle + \langle c_z^2\rangle\). The motion is random and no direction is special, so the three means are equal: \(\langle c_x^2\rangle = \tfrac13\langle c^2\rangle\).
Therefore \(p = \dfrac{1}{3}\dfrac{Nm\langle c^2\rangle}{V}\), that is \(pV = \tfrac13 Nm\langle c^2\rangle\).
:::

Collisions between molecules are ignored in this proof: they exchange momentum, but they do not change the total, so the result does not change. The shape of the container does not matter either.

:::formula Pressure of an ideal gas from the kinetic theory
\[pV = \tfrac13 Nm\langle c^2\rangle \qquad\qquad p = \tfrac13\rho\langle c^2\rangle\]
\(N\): number of molecules · \(m\): mass of one molecule · \(\langle c^2\rangle\): mean-square speed (\(\mathrm{m^2\,s^{-2}}\)) · \(\rho = Nm/V\): density of the gas.
:::

The second form follows at once, since \(Nm/V\) is the mass of gas per unit volume, which is the density \(\rho\).

### Mean-square speed and r.m.s. speed

The molecules of a gas have a wide spread of speeds, and the equation uses their mean-square speed. To find it you **square** each speed, **average** the squares, and (to get a speed again) take the **root**.

:::def Root-mean-square (r.m.s.) speed
The square root of the mean of the squares of the speeds of the molecules: \(c_\text{r.m.s.} = \sqrt{\langle c^2\rangle}\).
:::

The mean speed \(\langle c\rangle\) and the r.m.s. speed are different. The r.m.s. speed is always larger, because squaring gives extra weight to the fastest molecules. Notice that \(\langle c^2\rangle\) is the mean of the squares, whereas \(\langle c\rangle^2\) is the square of the mean: they are not equal.

:::eg Five molecules have speeds of 200, 300, 400, 500 and \(600\,\mathrm{m\,s^{-1}}\). Calculate (a) the mean speed and (b) the r.m.s. speed.
(a) Mean speed \(= \dfrac{200 + 300 + 400 + 500 + 600}{5} = 400\,\mathrm{m\,s^{-1}}\). [A1]
(b) Mean-square speed: \(\langle c^2\rangle = \dfrac{200^2 + 300^2 + 400^2 + 500^2 + 600^2}{5} = \dfrac{9.0 \times 10^{5}}{5} = 1.8 \times 10^{5}\,\mathrm{m^2\,s^{-2}}\). [C1]
\[c_\text{r.m.s.} = \sqrt{1.8 \times 10^{5}} = 424\,\mathrm{m\,s^{-1}} \approx 4.2 \times 10^{2}\,\mathrm{m\,s^{-1}}\] [A1]
The r.m.s. speed, 424, is bigger than the mean speed, 400.
:::

The simulation below shows molecules moving in a box. Change the temperature and watch the speeds and the r.m.s. speed in the histogram; compress the box and see how the number of wall hits changes; choose helium, nitrogen or oxygen to see how mass affects the speed.

:::html
<div class="widget" data-w="phys-gas" data-n="60" data-t="300" data-gas="n2"></div>
:::

:::eg A gas has density \(1.20\,\mathrm{kg\,m^{-3}}\) at a pressure of \(1.01 \times 10^{5}\,\mathrm{Pa}\). Estimate the r.m.s. speed of its molecules.
\[p = \tfrac13\rho\langle c^2\rangle \quad\Rightarrow\quad \langle c^2\rangle = \frac{3p}{\rho} = \frac{3 \times 1.01 \times 10^{5}}{1.20}\] [C1]
\[\langle c^2\rangle = 2.53 \times 10^{5}\,\mathrm{m^2\,s^{-2}} \quad\Rightarrow\quad c_\text{r.m.s.} = 5.0 \times 10^{2}\,\mathrm{m\,s^{-1}}\] [A1] (502 before rounding)
This is the same order as the speed of sound in air (about \(340\,\mathrm{m\,s^{-1}}\)), which is no coincidence: sound is passed on by the molecules themselves.
:::

## Temperature and the kinetic energy of molecules

Compare the two expressions for \(pV\): one from the kinetic theory and one from experiment.

:::proof examinable The mean kinetic energy of a molecule is \(\tfrac32 kT\)
From the kinetic theory, \(pV = \tfrac13 Nm\langle c^2\rangle\).
From the equation of state, \(pV = NkT\).
The left-hand sides are equal, so \(\tfrac13 Nm\langle c^2\rangle = NkT\).
Divide by \(N\) and multiply by 3: \(m\langle c^2\rangle = 3kT\).
Divide by 2: \(\tfrac12 m\langle c^2\rangle = \tfrac32 kT\).
The left-hand side is the mean translational kinetic energy of one molecule.
:::

:::formula Mean translational kinetic energy of a molecule
\[\langle E_K\rangle = \tfrac12 m\langle c^2\rangle = \tfrac32 kT \qquad\qquad c_\text{r.m.s.} = \sqrt{\frac{3kT}{m}}\]
\(T\): thermodynamic temperature (K) · \(m\): mass of one molecule (kg) · \(k = 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}\). The mean kinetic energy per molecule depends only on \(T\), not on the gas. For \(n\) moles the total translational kinetic energy is \(\tfrac32 nRT\).
:::

Two points matter. At the same temperature, every ideal gas has the same mean kinetic energy per molecule, so a **lighter** molecule is moving **faster**: \(c_\text{r.m.s.} \propto 1/\sqrt{m}\). Helium atoms are fast, oxygen molecules are slow. And since the kinetic energy is proportional to \(T\), temperature is a measure of the average random kinetic energy of the molecules. At absolute zero, the molecules have no kinetic energy.

The total translational kinetic energy of the \(N\) molecules is \(N \times \tfrac32 kT = \tfrac32 nRT\), because \(Nk = nR\). In an ideal gas there are no forces between molecules and so there is no potential energy: this total is the **internal energy** of a monatomic ideal gas, a point you will use in [Thermodynamics](#phys.thermo).

:::eg Calculate the mean translational kinetic energy of a molecule of an ideal gas at 27 °C.
\(T = 27 + 273.15 = 300.15\,\mathrm{K}\). [C1]
\[\langle E_K\rangle = \tfrac32 kT = 1.5 \times 1.38 \times 10^{-23} \times 300.15\] [C1]
\[\langle E_K\rangle = 6.2 \times 10^{-21}\,\mathrm{J}\] [A1] (6.21 before rounding)
The same value applies to hydrogen, helium, nitrogen or any other ideal gas at this temperature.
:::

:::eg Calculate the r.m.s. speed of nitrogen molecules (\(M = 0.028\,\mathrm{kg\,mol^{-1}}\)) at 300 K, and compare it with the r.m.s. speed of helium atoms (\(M = 0.0040\,\mathrm{kg\,mol^{-1}}\)) at the same temperature.
Mass of a nitrogen molecule: \(m = \dfrac{0.028}{6.02 \times 10^{23}} = 4.65 \times 10^{-26}\,\mathrm{kg}\). [C1]
\[c_\text{r.m.s.} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3 \times 1.38 \times 10^{-23} \times 300}{4.65 \times 10^{-26}}} = 5.2 \times 10^{2}\,\mathrm{m\,s^{-1}}\] [A1] (517 before rounding)
For helium, \(m = 6.64 \times 10^{-27}\,\mathrm{kg}\), and the same method gives \(1.4 \times 10^{3}\,\mathrm{m\,s^{-1}}\) (1370). [A1]
The ratio of the speeds is \(\sqrt{28/4.0} = 2.6\): a helium atom is 7 times lighter, so it is \(\sqrt{7}\) times faster at the same temperature.
:::

:::eg By what factor does the r.m.s. speed of the molecules of a gas change when its temperature is raised from 27 °C to 327 °C?
\(c_\text{r.m.s.} \propto \sqrt{T}\), and temperatures must be in kelvin: \(T_1 = 300.15\,\mathrm{K}\) and \(T_2 = 600.15\,\mathrm{K}\). [C1]
\[\frac{c_2}{c_1} = \sqrt{\frac{600.15}{300.15}} = 1.41\] [A1]
The speed increases by a factor of 1.41. Using the Celsius numbers instead (327/27 ≈ 12) would give a factor of \(\sqrt{12} = 3.5\), which is wrong: only a ratio of thermodynamic temperatures is meaningful.
:::

:::board
AQA and OCR use the same equations and assumptions, including \(pV = \tfrac13 Nm\langle c^2\rangle\) and \(\tfrac32 kT\). AQA also asks for the historical development of the gas laws and for Brownian motion as evidence for molecular motion. Some specifications write the mean-square speed as \(\overline{c^2}\).
:::

:::eg Spot the error: a flask of volume \(5.0 \times 10^{-3}\,\mathrm{m^3}\) contains 0.20 mol of an ideal gas at 27 °C. Calculate the pressure.
A student wrote this answer.

Line 1: \(pV = nRT\), so \(p = \dfrac{nRT}{V}\) [C1]
Line 2: \(p = \dfrac{0.20 \times 8.31 \times 27}{5.0 \times 10^{-3}} = 9.0 \times 10^{3}\,\mathrm{Pa}\)

Line 1 is correct. [C1] **Line 2 uses 27 in place of the thermodynamic temperature: \(T\) must be in kelvin, \(27 + 273.15 = 300.15\,\mathrm{K}\).** The answer is about 11 times too small. [A0]

Correct working: \(p = \dfrac{0.20 \times 8.31 \times 300.15}{5.0 \times 10^{-3}} = 1.0 \times 10^{5}\,\mathrm{Pa}\). [A1]

The result should have looked wrong: 0.20 mol in 5 litres at room temperature gives about atmospheric pressure, \(10^{5}\,\mathrm{Pa}\).
:::

:::try Start easy, finish at exam standard
Q: Calculate the number of moles in 0.016 kg of oxygen (\(M = 0.032\,\mathrm{kg\,mol^{-1}}\)), and the number of molecules.
A: \(n = 0.016/0.032 = 0.50\,\mathrm{mol}\) and \(N = nN_A = 0.50 \times 6.02 \times 10^{23} = 3.0 \times 10^{23}\).
Q: Find the mass of one atom of helium (\(M = 0.0040\,\mathrm{kg\,mol^{-1}}\)).
A: \(m = M/N_A = 0.0040/(6.02 \times 10^{23}) = 6.6 \times 10^{-27}\,\mathrm{kg}\).
Q: A gas at \(2.0 \times 10^{5}\,\mathrm{Pa}\) in a volume of \(0.010\,\mathrm{m^3}\) is compressed slowly to \(0.0050\,\mathrm{m^3}\) at the same temperature. Find the new pressure.
A: Boyle's law: \(p_2 = p_1V_1/V_2 = 2.0 \times 10^{5} \times 0.010/0.0050 = 4.0 \times 10^{5}\,\mathrm{Pa}\).
Q: A sealed container of gas at \(1.00 \times 10^{5}\,\mathrm{Pa}\) and 20 °C is heated to 80 °C. Find the new pressure.
A: \(p \propto T\): \(p_2 = 1.00 \times 10^{5} \times 353.15/293.15 = 1.2 \times 10^{5}\,\mathrm{Pa}\).
Q: Calculate the volume of one mole of an ideal gas at \(1.01 \times 10^{5}\,\mathrm{Pa}\) and 0 °C.
A: \(V = nRT/p = 1 \times 8.31 \times 273.15/(1.01 \times 10^{5}) = 2.25 \times 10^{-2}\,\mathrm{m^3}\), that is 22.5 litres.
Q: Calculate the mean translational kinetic energy of a molecule of an ideal gas at 300 K, and at 600 K.
A: At 300 K, \(\tfrac32 kT = 1.5 \times 1.38 \times 10^{-23} \times 300 = 6.2 \times 10^{-21}\,\mathrm{J}\). It is proportional to \(T\), so at 600 K it is twice as large, \(1.2 \times 10^{-20}\,\mathrm{J}\).
Q: Five molecules have speeds 100, 200, 300, 400 and \(500\,\mathrm{m\,s^{-1}}\). Calculate the mean speed and the r.m.s. speed.
A: Mean \(= 1500/5 = 300\,\mathrm{m\,s^{-1}}\). \(\langle c^2\rangle = (1 + 4 + 9 + 16 + 25) \times 10^{4}/5 = 1.1 \times 10^{5}\), so \(c_\text{r.m.s.} = 332\,\mathrm{m\,s^{-1}}\).
Q: Oxygen (\(M = 0.032\)) and nitrogen (\(M = 0.028\)) are at the same temperature. Which has the greater r.m.s. speed, and why?
A: Nitrogen. The mean kinetic energy per molecule is the same, \(\tfrac32 kT\), so the molecule with the smaller mass has the greater speed (\(c_\text{r.m.s.} \propto 1/\sqrt{m}\)), by a factor \(\sqrt{32/28} = 1.07\).
Q: State why a real gas at high pressure does not obey \(pV = nRT\) closely.
A: At high pressure the molecules are close together, so their own volume is no longer negligible compared with the container, and the forces between them are no longer negligible.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State two assumptions of the kinetic theory of an ideal gas.
A: Any two from: molecules are in continuous random motion; the volume of the molecules is negligible compared with the volume of the container; there are no forces between molecules except during collisions; collisions are elastic; the duration of a collision is negligible compared with the time between collisions. [B1] [B1]
Q: [3 marks] ★ A flask of volume \(2.5 \times 10^{-3}\,\mathrm{m^3}\) contains an ideal gas at a pressure of \(1.2 \times 10^{5}\,\mathrm{Pa}\) and a temperature of 27 °C. Calculate the amount of gas in moles and the number of molecules.
A: \(T = 300.15\,\mathrm{K}\) and \(n = \dfrac{pV}{RT} = \dfrac{1.2 \times 10^{5} \times 2.5 \times 10^{-3}}{8.31 \times 300.15}\) [C1] \(= 0.12\,\mathrm{mol}\). [A1] \(N = nN_A = 0.1203 \times 6.02 \times 10^{23} = 7.2 \times 10^{22}\). [A1]
Q: [3 marks] ★★ Explain, in terms of molecules, how a gas exerts a pressure on the walls of its container.
A: Molecules collide with the wall and rebound, so their momentum changes. [B1] The rate of change of momentum is the force on the molecule, so by Newton's third law there is an equal force on the wall. [B1] A very large number of collisions each second gives a steady average force, and the force per unit area is the pressure. [B1]
Q: [5 marks] ★★ Derive the expression \(pV = \tfrac13 Nm\langle c^2\rangle\) for the pressure of an ideal gas, where \(N\) is the number of molecules, each of mass \(m\), in a cube of volume \(V\).
H: Start with one molecule bouncing between two opposite faces, and work out the force it exerts on the wall.
A: Change of momentum at one collision is \(2mc_x\). [B1] Time between collisions with the same wall is \(2L/c_x\), so the force is \(\dfrac{2mc_x}{2L/c_x} = \dfrac{mc_x^2}{L}\) (rate of change of momentum). [B1] Pressure \(= \) force/area \(= \dfrac{mc_x^2}{L^3}\) for one molecule, so for \(N\) molecules \(p = \dfrac{Nm\langle c_x^2\rangle}{V}\). [B1] Since \(c^2 = c_x^2 + c_y^2 + c_z^2\) and the motion is random, \(\langle c_x^2\rangle = \tfrac13\langle c^2\rangle\). [B1] Therefore \(pV = \tfrac13 Nm\langle c^2\rangle\). [B1]
Q: [3 marks] ★★ Calculate the r.m.s. speed of oxygen molecules (\(M = 0.032\,\mathrm{kg\,mol^{-1}}\)) at 20 °C.
A: \(m = \dfrac{0.032}{6.02 \times 10^{23}} = 5.32 \times 10^{-26}\,\mathrm{kg}\) and \(T = 293.15\,\mathrm{K}\). [C1] \(c_\text{r.m.s.} = \sqrt{\dfrac{3kT}{m}} = \sqrt{\dfrac{3 \times 1.38 \times 10^{-23} \times 293.15}{5.32 \times 10^{-26}}}\) [C1] \(= 4.8 \times 10^{2}\,\mathrm{m\,s^{-1}}\). [A1]
Q: [3 marks] ★★ Use \(pV = \tfrac13 Nm\langle c^2\rangle\) and \(pV = NkT\) to show that the mean translational kinetic energy of a molecule of an ideal gas is \(\tfrac32 kT\).
A: Equating, \(\tfrac13 Nm\langle c^2\rangle = NkT\). [M1] So \(m\langle c^2\rangle = 3kT\), [M1] and \(\tfrac12 m\langle c^2\rangle = \tfrac32 kT\), which is the mean translational kinetic energy per molecule. [A1]
Q: [6 marks] ★★★ Two flasks are joined by a tube with a closed tap. Flask A has volume \(2.0 \times 10^{-3}\,\mathrm{m^3}\), and holds gas at \(1.5 \times 10^{5}\,\mathrm{Pa}\) and 300 K. Flask B has volume \(3.0 \times 10^{-3}\,\mathrm{m^3}\), and holds the same gas at \(1.0 \times 10^{5}\,\mathrm{Pa}\) and 400 K. The tap is opened. Flask A is kept at 300 K and flask B at 400 K. Calculate the final pressure.
H: Work with \(nR = pV/T\) for each flask. The total amount of gas is conserved.
H: When the tap is open, the gas can flow until the pressure is the same in both flasks.
A: The gas flows until the pressure is equal throughout. [B1] Initially, \(n_AR = \dfrac{1.5 \times 10^{5} \times 2.0 \times 10^{-3}}{300} = 1.00\,\mathrm{J\,K^{-1}}\) [C1] and \(n_BR = \dfrac{1.0 \times 10^{5} \times 3.0 \times 10^{-3}}{400} = 0.75\,\mathrm{J\,K^{-1}}\). [C1] Total amount is conserved: \((n_A + n_B)R = 1.75\). [M1] In the final state, \(p\left(\dfrac{V_A}{T_A} + \dfrac{V_B}{T_B}\right) = (n_A + n_B)R\), so \(p \times \left(\dfrac{2.0 \times 10^{-3}}{300} + \dfrac{3.0 \times 10^{-3}}{400}\right) = 1.75\). [C1] \(p = 1.2 \times 10^{5}\,\mathrm{Pa}\). [A1]
Q: [5 marks] ★★★ The escape speed from the surface of the Earth is \(1.1 \times 10^{4}\,\mathrm{m\,s^{-1}}\). (a) Calculate the r.m.s. speed of hydrogen molecules (\(\mathrm{H_2}\), \(M = 0.0020\,\mathrm{kg\,mol^{-1}}\)) at 300 K. (b) The r.m.s. speed is much less than the escape speed, but the Earth's atmosphere contains almost no hydrogen. Suggest why.
H: In (b), think about the distribution of speeds, and the very long time involved.
A: (a) \(m = \dfrac{0.0020}{6.02 \times 10^{23}} = 3.32 \times 10^{-27}\,\mathrm{kg}\). [C1] \(c_\text{r.m.s.} = \sqrt{\dfrac{3 \times 1.38 \times 10^{-23} \times 300}{3.32 \times 10^{-27}}}\) [C1] \(= 1.9 \times 10^{3}\,\mathrm{m\,s^{-1}}\). [A1] (b) The molecules have a range of speeds, so a small fraction of them have speeds much greater than the r.m.s. speed. [B1] Over millions of years, those that are fast enough escape, and so the hydrogen is gradually lost. [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A vessel contains 1.0 mol of helium (\(M = 0.0040\,\mathrm{kg\,mol^{-1}}\)) and 1.0 mol of argon (\(M = 0.040\,\mathrm{kg\,mol^{-1}}\)), both treated as ideal gases, in a volume of \(0.050\,\mathrm{m^3}\) at 300 K. (a) State the ratio of the mean kinetic energy of a helium atom to that of an argon atom. (b) Calculate the ratio of their r.m.s. speeds. (c) Calculate the total pressure. (d) State whether the argon atoms or the helium atoms contribute more to the pressure, with a reason.
H: The two gases are in thermal equilibrium, so they are at the same temperature.
H: Use \(pV = nRT\) with the total number of moles.
A: (a) The mean kinetic energy, \(\tfrac32 kT\), depends only on temperature, so the ratio is 1. [B1] (b) \(c_\text{r.m.s.} \propto 1/\sqrt{m}\), so \(\dfrac{c_\text{He}}{c_\text{Ar}} = \sqrt{\dfrac{0.040}{0.0040}} = 3.2\). [C1] [A1] (c) \(p = \dfrac{nRT}{V} = \dfrac{2.0 \times 8.31 \times 300}{0.050}\) [C1] \(= 1.0 \times 10^{5}\,\mathrm{Pa}\). [A1] (d) Equal contributions: each gas has the same number of molecules in the same volume at the same temperature, so each exerts half of the total pressure. [B1] (Helium atoms are faster but lighter: the momentum transfers per collision are smaller, and they cancel exactly in \(\tfrac13 Nm\langle c^2\rangle\).) [B1]
Q: [7 marks] ★★★ (a) Show that the pressure of an ideal gas can be written \(p = \tfrac13\rho\langle c^2\rangle\), where \(\rho\) is the density. (b) The density of air at the surface of Venus is about \(65\,\mathrm{kg\,m^{-3}}\) at a pressure of \(9.2 \times 10^{6}\,\mathrm{Pa}\). Calculate the r.m.s. speed of its molecules, and (c) use \(\tfrac12 m\langle c^2\rangle = \tfrac32 kT\) with the mean molecular mass \(7.3 \times 10^{-26}\,\mathrm{kg}\) to estimate the temperature.
H: Density is mass per volume: \(Nm/V\).
H: For (c), rearrange for \(T\) using \(\langle c^2\rangle\) from (b).
A: (a) \(pV = \tfrac13 Nm\langle c^2\rangle\) gives \(p = \tfrac13\dfrac{Nm}{V}\langle c^2\rangle\), [M1] and \(Nm/V\) is the mass per unit volume, \(\rho\), so \(p = \tfrac13\rho\langle c^2\rangle\). [A1] (b) \(\langle c^2\rangle = \dfrac{3p}{\rho} = \dfrac{3 \times 9.2 \times 10^{6}}{65}\) [C1] \(= 4.25 \times 10^{5}\,\mathrm{m^2\,s^{-2}}\), so \(c_\text{r.m.s.} = 6.5 \times 10^{2}\,\mathrm{m\,s^{-1}}\). [A1] (c) \(T = \dfrac{m\langle c^2\rangle}{3k} = \dfrac{7.3 \times 10^{-26} \times 4.25 \times 10^{5}}{3 \times 1.38 \times 10^{-23}}\) [C1] \(= 7.5 \times 10^{2}\,\mathrm{K}\). [A1] This is about 480 °C, hot enough to melt lead. [B1]
:::

:::quiz
? What is the definition of the Avogadro constant?
+ The number of particles in one mole of a substance
- The number of molecules in one kilogram of gas
- The mass of one mole of a substance
- The number of atoms in one litre of gas at room temperature
> \(N_A = 6.02 \times 10^{23}\,\mathrm{mol^{-1}}\) is the number of particles per mole. The mass of one mole is the molar mass, and a litre of gas does not contain a fixed number of atoms: that depends on \(p\) and \(T\).
? In the equation \(pV = nRT\), which unit must be used for the temperature?
+ Kelvin
- Degrees Celsius
- Either, as long as \(R\) is chosen to match
- Joules
> The law holds for the thermodynamic temperature, and \(R = 8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}\) is for kelvin. Using Celsius gives an answer many times too small.
? A fixed mass of an ideal gas is kept at constant volume and its thermodynamic temperature is doubled. What happens to the pressure?
+ It doubles.
- It halves.
- It increases by a factor of \(\sqrt{2}\).
- It stays the same, because the volume is fixed.
> At constant \(V\) (and \(n\)), \(p \propto T\). The volume being fixed is exactly why the pressure must change. \(\sqrt{2}\) applies to the r.m.s. speed.
? Which is a basic assumption of the kinetic theory of an ideal gas?
- The molecules have no mass.
+ The volume of the molecules is negligible compared with the volume of the container.
- The molecules are stationary between collisions.
- The collisions between molecules are inelastic.
> The molecules have mass, they move in straight lines at constant speed between collisions, and collisions are elastic.
? Which expression gives the pressure of an ideal gas of N molecules of mass m in a volume V?
+ \(\dfrac{Nm\langle c^2\rangle}{3V}\)
- \(\dfrac{Nm\langle c\rangle^2}{3V}\)
- \(\dfrac{Nm\langle c^2\rangle}{V}\)
- \(\dfrac{N\langle c^2\rangle}{3mV}\)
> The mean-square speed is the mean of the squares, \(\langle c^2\rangle\), not the square of the mean speed, and the factor \(\tfrac13\) comes from the three dimensions.
? How does the r.m.s. speed of the molecules of a gas compare with their mean speed?
+ The r.m.s. speed is greater, because squaring gives the fastest molecules more weight.
- They are always equal.
- The r.m.s. speed is smaller, because it is a square root.
- The r.m.s. speed is zero, because velocities cancel.
> If all the molecules had exactly the same speed the two would match, but with a spread of speeds the r.m.s. speed is always the larger of the two.
? Helium and neon are at the same temperature. Neon atoms are five times as massive as helium atoms. How does the mean translational kinetic energy per atom compare?
+ It is the same for both.
- It is five times greater for neon.
- It is five times greater for helium.
- It is \(\sqrt{5}\) times greater for neon.
> The mean translational kinetic energy per molecule is \(\tfrac32 kT\), which depends only on the temperature. The lighter helium atoms have the greater speed, by a factor \(\sqrt{5}\).
? Why is a gas in a sealed tyre at a higher pressure after a long journey?
+ The molecules move faster, so they hit the walls harder and more often.
- There are more molecules in the tyre.
- The molecules are bigger.
- The molecules gain mass as they warm.
> A rise in temperature increases the mean kinetic energy of the molecules, so each collision involves a larger momentum change and collisions happen more often. The amount of gas and the molecules themselves are unchanged.
:::

:::checklist What you can now do
- [ ] I can state that amount of substance is a base quantity with the mole as its unit, and use \(N = nN_A\), \(n = m_\text{total}/M\) and \(m = M/N_A\).
- [ ] I can state Boyle's law, the pressure law and Charles's law, and explain how the pressure law leads to absolute zero.
- [ ] I can define an ideal gas, and use \(pV = nRT\) and \(pV = NkT\) with \(k = R/N_A\), always in SI units and kelvin.
- [ ] I can solve problems on gases with changing \(p\), \(V\) and \(T\), including changes in the amount of gas, and the density of a gas.
- [ ] I can state the basic assumptions of the kinetic theory of gases in exam wording.
- [ ] I can explain how molecular motion causes the pressure of a gas, and derive \(pV = \tfrac13 Nm\langle c^2\rangle\).
- [ ] I can define and calculate the r.m.s. speed, and tell it apart from the mean speed.
- [ ] I can derive and use \(\tfrac12 m\langle c^2\rangle = \tfrac32 kT\) and \(c_\text{r.m.s.} = \sqrt{3kT/m}\).
:::

:::recap
- One mole contains \(N_A = 6.02 \times 10^{23}\) particles. \(N = nN_A\), \(n = m_\text{total}/M\), \(m = M/N_A\) (molar mass in kg per mol).
- Fixed mass of gas: Boyle \(pV\) constant at constant \(T\); pressure law \(p \propto T\) at constant \(V\); Charles \(V \propto T\) at constant \(p\). Extrapolating the graph of \(p\) against \(\theta\) gives zero pressure at \(-273\,^\circ\mathrm{C}\).
- Ideal gas: \(pV = nRT = NkT\), with \(k = R/N_A = 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}\). Always use kelvin, pascals and cubic metres. For a fixed mass, \(p_1V_1/T_1 = p_2V_2/T_2\).
- Kinetic-theory assumptions: very many molecules in random motion; negligible molecular volume; no forces except in collisions; elastic collisions; negligible collision time.
- Molecules change momentum at the wall; the force per unit area is the pressure. \(pV = \tfrac13 Nm\langle c^2\rangle = \tfrac13\rho V\langle c^2\rangle\). The derivation uses \(2mc_x\), time \(2L/c_x\), and \(\langle c_x^2\rangle = \tfrac13\langle c^2\rangle\).
- \(c_\text{r.m.s.} = \sqrt{\langle c^2\rangle}\), always larger than the mean speed.
- Mean translational kinetic energy per molecule \(= \tfrac32 kT\), the same for every ideal gas at the same \(T\). Lighter molecules are faster: \(c_\text{r.m.s.} = \sqrt{3kT/m}\). Total for \(n\) moles: \(\tfrac32 nRT\).
:::

:::links
- explore: [Gas Properties](https://phet.colorado.edu/en/simulations/gas-properties) · PhET · pump in molecules, change the volume and temperature, and watch the pressure
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the ideal-gas questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Thermodynamics](#phys.thermo)
