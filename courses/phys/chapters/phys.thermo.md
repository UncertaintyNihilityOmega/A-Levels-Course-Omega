@chapter phys.thermo
@title Thermodynamics
@level a2
@paper CAIE P4 (A Level)
@time 3–5 hours
@summary Internal energy as the random kinetic and potential energy of the molecules, the work done by and on a gas (W = pΔV and the area under a p–V graph), and the first law ΔU = q + W, applied to constant-volume, constant-pressure, isothermal and adiabatic changes and to a full cycle.

:::why
A car engine, a fridge, a bicycle pump and a power station all do the same job: they move energy around, and turn some of it into work. The first law of thermodynamics is simply the conservation of energy written for a gas that is heated and squeezed, and it gives you a way of checking every energy claim: what goes in, what comes out, and what is left over as internal energy. Once you can keep the signs straight, one equation explains why a pump warms, why an aerosol can feels cold and why no engine can turn all the energy it is given into work.
:::

**Before you start**, you need the ideas of an ideal gas and the kinetic energy of molecules from [Ideal gases](#phys.gases), temperature and latent heat from [Temperature](#phys.temperature), and work done from [Work, energy and power](#phys.energy).

:::try Warm-up
Q: Calculate the mean translational kinetic energy of a molecule of an ideal gas at 400 K. (from [Ideal gases](#phys.gases))
A: \(\tfrac32 kT = 1.5 \times 1.38 \times 10^{-23} \times 400 = 8.28 \times 10^{-21}\,\mathrm{J}\).
Q: A heater keeps supplying energy to melting ice, yet the temperature stays at 0 °C. Where does the energy go? (from [Temperature](#phys.temperature))
A: It increases the potential energy of the molecules as they move apart in the liquid. The kinetic energy, and so the temperature, does not change.
Q: A force of 50 N moves an object 0.40 m in the direction of the force. How much work is done? (from [Work, energy and power](#phys.energy))
A: \(W = Fs = 50 \times 0.40 = 20\,\mathrm{J}\).
:::

## Internal energy

Every molecule in a block of metal or a cylinder of gas has kinetic energy, because it is moving or vibrating, and the molecules may also have potential energy, because of the forces between them. Add up all of these energies for every molecule and you have the **internal energy** of the object.

:::def Internal energy
The sum of a random distribution of kinetic and potential energies of the molecules of a system.
:::

The word *random* matters. The energy of a thrown ball's overall motion is not part of its internal energy. Only the disordered motion and the interaction energy of the individual molecules count.

| State | Kinetic energy of the molecules | Potential energy of the molecules |
|---|---|---|
| Solid | vibration about fixed positions | lowest: strong forces hold the molecules close together |
| Liquid | vibration and sliding | higher: the molecules are slightly further apart |
| Real gas | random translation (and rotation) | highest, but small: forces act only when molecules are close |
| Ideal gas | random translation | none: there are no forces except in collisions |

The internal energy of a system is fixed by its **state**: its pressure, volume, temperature and amount of substance. It does not depend on how the system got there. A gas at 300 K and 1.0 × 10⁵ Pa has the same internal energy whether it was warmed from a cold start or cooled from a hot one. Because of this, the change \(\Delta U\) between two states is the same along every path between them. You will use this fact to check cycle questions.

### Internal energy and temperature

From [Ideal gases](#phys.gases), the mean translational kinetic energy of a molecule is \(\tfrac32 kT\), so the temperature measures the average random kinetic energy. Raising the temperature of an object raises the mean kinetic energy of its molecules, so its internal energy rises. For an ideal gas the link is exact. There is no potential energy, so the internal energy is just the kinetic energy of all \(N\) molecules.

:::formula Internal energy of a monatomic ideal gas
\[U = \tfrac32 NkT = \tfrac32 nRT = \tfrac32 pV\]
\(U\): internal energy (J) · \(N\): number of molecules · \(n\): amount of gas (mol) · \(T\): thermodynamic temperature (K) · \(p\): pressure (Pa) · \(V\): volume (m³). \(U\) depends only on \(T\) for a given amount of gas: \(\Delta U = \tfrac32 nR\,\Delta T\). The factor \(\tfrac32\) is for a **monatomic** gas such as helium or argon. Gases of two-atom molecules also have rotational energy, so their \(U\) is larger, but it is still proportional to \(T\).
:::

The three forms are the same equation: \(Nk = nR\) and \(pV = nRT\). The last form, \(U = \tfrac32 pV\), is handy when a question gives you a p–V graph instead of a temperature.

:::plot The internal energy of 1.00 mol of a monatomic ideal gas is proportional to the thermodynamic temperature. The gradient is \(\tfrac32 R\) per mole.
--f "0.012465*x" --x 0 600 --y 0 9 --pt "300,3.7395,(300 K, 3.74 kJ)@se" --xlabel "T / K" --ylabel "U / kJ" --label "U = (3/2)RT"
:::

:::eg A cylinder holds 2.00 mol of helium, which you can treat as a monatomic ideal gas, at 300 K. Calculate its internal energy, and the increase in internal energy when it is warmed to 350 K.
\[U = \tfrac32 nRT = 1.5 \times 2.00 \times 8.31 \times 300\] [C1]
\[U = 7.48 \times 10^{3}\,\mathrm{J}\] [A1]
The temperature rise is 50.0 K (the same in kelvin and in °C), so
\[\Delta U = \tfrac32 nR\,\Delta T = 1.5 \times 2.00 \times 8.31 \times 50.0 = 1.25 \times 10^{3}\,\mathrm{J}\] [A1]
Check with the first result: \(U\) at 350 K is \(\tfrac{350}{300} \times 7.48 = 8.73\,\mathrm{kJ}\), which is 1.25 kJ more.
:::

For a solid or a liquid, a temperature rise still means more molecular kinetic energy, so the internal energy goes up. But a temperature change is not the only way to change \(U\). While ice melts at 0 °C, the internal energy rises because the molecular potential energy rises, and the temperature does not change. This is the latent heat of [Temperature](#phys.temperature) seen as a change of internal energy.

:::warn Heat, temperature and internal energy are three different things
Internal energy is something a system **has**. Energy transferred because of a temperature difference is **heating**, and the amount is \(q\). A system does not "contain heat". Saying that a gas "has 500 J of heat" scores nothing, whereas "its internal energy increases by 500 J" can score. Temperature is a measure of the *mean kinetic energy* only. A change of temperature always means a change in \(U\), but a change in \(U\) does not always mean a change in temperature (melting), and a gas whose temperature is constant can still be exchanging energy with its surroundings.
:::

## Work done by and on a gas

A gas can change its internal energy by heating, and it can also change it by doing work or having work done on it. The simplest way to see work is a gas in a cylinder with a piston.

:::html
<figure class="fig"><svg viewBox="55 22 410 190" role="img" aria-label="A horizontal cylinder closed at the left end, with gas inside and a piston of area A at the right. A dashed line marks the piston's earlier position. An arrow labelled F equals pA points right from the piston. A pair of arrows below the cylinder shows the distance moved, delta x."><rect class="fm" x="70" y="50" width="230" height="120"/><path class="ln thick" d="M70 170V50H430M70 170H430"/><rect class="fp s-ink sw2" x="300" y="52" width="14" height="116"/><path class="ln thick" d="M314 110H450"/><path class="ln thin dash" d="M190 52V168"/><text class="tl tc" x="135" y="115">gas, p</text><text class="tl tc" x="190" y="40">old position</text><text class="tl tc" x="307" y="40">piston</text><text class="tl" x="322" y="150">area A</text><path class="c1" d="M322 88H392" marker-end="url(#ah-phys)"/><text class="tl ta" x="322" y="80">F = pA</text><path class="c1" d="M245 198H192" marker-end="url(#ah-phys)"/><path class="c1" d="M245 198H298" marker-end="url(#ah-phys)"/><text class="tl ti ta tc" x="245" y="190">Δx</text></svg><figcaption>A gas at constant pressure p pushes the piston of area A with a force F = pA. When the piston moves a distance Δx, the gas does work FΔx = pAΔx. The volume swept out is AΔx, which is the increase in volume ΔV.</figcaption></figure>
:::

:::proof Work done by a gas at constant pressure
Gas at pressure \(p\) pushes on a piston of area \(A\).
Pressure is force per unit area, so the force on the piston is \(F = pA\).
The pressure is constant, so the force is constant while the piston moves a distance \(\Delta x\) in the direction of the force.
Work done by the gas \(= F\,\Delta x = pA\,\Delta x\).
The product \(A\,\Delta x\) is the volume swept out by the piston, which is the increase in volume \(\Delta V\) of the gas.
So the work done by the gas is \(p\,\Delta V\).
:::

:::formula Work done by a gas at constant pressure
\[\text{work done by the gas} = p\,\Delta V \qquad\qquad W = -p\,\Delta V\]
\(p\): pressure (Pa) · \(\Delta V\): increase in volume (m³) · \(W\): work done **on** the gas (J), the quantity used in the first law below. When the gas expands, \(\Delta V > 0\), the gas does work and \(W\) is negative. When the gas is compressed, \(\Delta V < 0\) and \(W\) is positive.
:::

Take care over **who does the work on whom**. When a gas expands it pushes the piston and the surroundings back, so *it* transfers energy to them: the work done *by* the gas is positive and the work done *on* the gas is negative. When something compresses the gas, energy flows into the gas. The size of the work is the same for both views, \(p\,|\Delta V|\). Only the sign depends on whose point of view you take. In this chapter \(W\) always means the work done **on** the system, because this is the sign the first law needs.

:::warn Volume units
\(\Delta V\) must be in cubic metres. \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\) and \(1\,\mathrm{litre} = 10^{-3}\,\mathrm{m^3}\). Using cm³ or litres with \(p\) in pascals gives an answer that is wrong by a factor of a million or a thousand. A pressure in kPa with a volume in litres gives joules directly, because \(10^{3}\,\mathrm{Pa} \times 10^{-3}\,\mathrm{m^3} = 1\,\mathrm{J}\).
:::

:::eg A balloon is inflated slowly outdoors, where the atmospheric pressure is \(1.01 \times 10^{5}\,\mathrm{Pa}\), and its volume increases from 2.0 litres to 5.0 litres. Calculate the work the balloon does on the atmosphere.
The pressure inside a slowly inflated balloon is just above atmospheric, so treat the pressure as constant. \(\Delta V = (5.0 - 2.0) \times 10^{-3} = 3.0 \times 10^{-3}\,\mathrm{m^3}\). [C1]
\[\text{work done by the gas} = p\,\Delta V = 1.01 \times 10^{5} \times 3.0 \times 10^{-3} = 3.0 \times 10^{2}\,\mathrm{J}\] [A1]
(303 J before rounding.) This is the energy the gas gives to the atmosphere, which is pushed back.
:::

### Work when the pressure changes

If the pressure changes as the gas expands, split the change into tiny steps. In each step the pressure is almost constant and the work is \(p\,\Delta V\), which is the area of a thin strip under the line on a p–V graph. Adding the strips gives the whole area.

:::key The area under a p–V graph is the work
The work done by a gas as its volume changes equals the **area under the p–V graph** between the initial and final volumes. For an expansion the gas does work; for a compression the area is the work done on the gas. With \(p\) in kPa and \(V\) in litres, the area comes out in joules.
:::

:::plot An isothermal expansion of an ideal gas with pV = 300 J. The shaded area under the curve from 2.0 L to 6.0 L is the work done by the gas.
--f "300/x" --x 1 8 --y 0 400 --shade "0,2,6" --pt "2,150,A (2.0 L, 150 kPa)@ne" --pt "6,50,B (6.0 L, 50 kPa)@ne" --xlabel "V / L" --ylabel "p / kPa" --label "pV = 300 J"
:::

:::eg Estimate the work done by the gas in the graph above as the volume increases from 2.0 L to 6.0 L, using the trapezium rule with two strips of width 2.0 L. The pressure is 150 kPa at 2.0 L, 75 kPa at 4.0 L and 50 kPa at 6.0 L.
Each strip is a trapezium, with area equal to its width times the mean of its two parallel sides. [M1]
\[\text{area} = \tfrac12(2.0)(150 + 75) + \tfrac12(2.0)(75 + 50) = 225 + 125\] [C1]
\[\text{work done by the gas} \approx 350\,\mathrm{J}\] [A1]
The curve bends upwards (it is convex), so straight-line strips lie above it and slightly overestimate. The true area for this curve is 330 J. Counting squares under a drawn graph gives an answer of this kind, and exam questions accept a result within a stated range.
:::

## The first law of thermodynamics

There are two ways to change the internal energy of a gas: transfer energy to it by **heating**, and do **work** on it. The first law of thermodynamics says that these two add up to the whole change.

:::def First law of thermodynamics
The increase in internal energy of a system is equal to the sum of the energy supplied to the system by heating and the work done on the system.
:::

:::formula The first law (Cambridge form)
\[\Delta U = q + W\]
\(\Delta U\): increase in internal energy (J) · \(q\): energy transferred **to** the system by heating (J) · \(W\): work done **on** the system (J). For a gas at constant pressure \(W = -p\,\Delta V\).
:::

The law is the conservation of energy: energy cannot be created or destroyed, so whatever you put into a system either stays there as internal energy or has been given away again. The only skill is the signs. Decide the sign of each term from the *direction* of the energy transfer, and write the sign with the number before you substitute.

| Quantity | Positive (+) | Negative (−) |
|---|---|---|
| \(q\) | energy enters the gas by heating | energy leaves the gas by heating |
| \(W\) | the gas is compressed (work done **on** the gas) | the gas expands (work done **by** the gas) |
| \(\Delta U\) | internal energy increases (an ideal gas gets hotter) | internal energy decreases (an ideal gas gets cooler) |

:::eg A gas at a constant pressure of \(1.5 \times 10^{5}\,\mathrm{Pa}\) expands from \(2.0 \times 10^{-3}\,\mathrm{m^3}\) to \(5.0 \times 10^{-3}\,\mathrm{m^3}\) while 1200 J of energy is supplied to it by heating. Calculate the change in internal energy.
The gas expands, so it does work and \(W\) is negative:
\[W = -p\,\Delta V = -1.5 \times 10^{5} \times (5.0 - 2.0) \times 10^{-3} = -450\,\mathrm{J}\] [C1]
Energy is supplied by heating, so \(q = +1200\,\mathrm{J}\). [B1]
\[\Delta U = q + W = 1200 + (-450) = +750\,\mathrm{J}\] [A1]
Of the 1200 J supplied, 450 J leaves again as work done on the surroundings and 750 J stays in the gas as extra internal energy, so its temperature rises.
:::

:::eg During one expansion a gas does 90 J of work on its surroundings, and its internal energy falls by 30 J. How much energy is transferred by heating, and in which direction?
The gas does the work, so \(W = -90\,\mathrm{J}\). The internal energy falls, so \(\Delta U = -30\,\mathrm{J}\). [B1]
Rearrange \(\Delta U = q + W\): \(q = \Delta U - W = -30 - (-90)\) [C1]
\[q = +60\,\mathrm{J}\] [A1]
The sign is positive, so 60 J flows **into** the gas by heating. The gas gave out 90 J as work but only lost 30 J of internal energy, so it must have received the other 60 J.
:::

:::warn The sign slip
Many marks are lost on the sign of \(W\). A gas that **expands** has negative \(W\) in \(\Delta U = q + W\). If you write \(\Delta U = q - W\), you must mean \(W\) as the work done *by* the gas. Pick one form, and say which one in your working. The Cambridge form is \(\Delta U = q + W\) with \(W\) the work done on the system.
:::

## Four special changes of a gas

It helps to learn what the first law becomes when something is held fixed. Each of these changes is drawn below as a line on a p–V graph. The direction of travel along the line is shown by the arrow.

:::html
<figure class="fig wide"><svg viewBox="20 0 560 392" role="img" aria-label="Four p–V graphs. (a) Constant volume: a vertical line upwards, so pressure rises with volume unchanged. (b) Constant pressure: a horizontal line to the right, with the area underneath shaded as the work done by the gas. (c) Isothermal: a falling curve, pressure decreasing as volume increases. (d) Adiabatic: a steeper falling curve than the dashed isothermal curve drawn from the same start."><text class="tl" x="50" y="24">(a) Constant volume</text><path class="ax" d="M50 150V35M50 150H250"/><text class="tl ti" x="58" y="46">p</text><text class="tl ti" x="258" y="155">V</text><path class="ln-m thin" d="M130 150V155"/><text class="ts tc" x="130" y="167">V₁</text><circle class="fi" cx="130" cy="125" r="3"/><path class="c1" d="M130 125V68" marker-end="url(#ah-phys)"/><text class="tl" x="142" y="100">heated</text><text class="tl" x="50" y="188">W = 0, so ΔU = q</text><text class="tl" x="340" y="24">(b) Constant pressure</text><rect class="fm" x="390" y="80" width="90" height="70"/><path class="ax" d="M340 150V35M340 150H540"/><text class="tl ti" x="348" y="46">p</text><text class="tl ti" x="548" y="155">V</text><path class="ln-m thin" d="M390 150V155M480 150V155"/><text class="ts tc" x="390" y="167">V₁</text><text class="ts tc" x="480" y="167">V₂</text><circle class="fi" cx="390" cy="80" r="3"/><path class="c1" d="M390 80H480" marker-end="url(#ah-phys)"/><text class="tl tc" x="435" y="72">expands</text><text class="tl tc" x="435" y="112">area =</text><text class="tl tc" x="435" y="128">work by gas</text><text class="tl" x="340" y="188">W = −pΔV (expansion)</text><text class="tl" x="50" y="222">(c) Isothermal</text><path class="ax" d="M50 348V233M50 348H250"/><text class="tl ti" x="58" y="244">p</text><text class="tl ti" x="258" y="353">V</text><path class="ln-m thin" d="M95 348V353M160 348V353"/><text class="ts tc" x="95" y="365">V₁</text><text class="ts tc" x="160" y="365">V₂</text><circle class="fi" cx="95" cy="248" r="3"/><path class="c1" d="M95 248L102 261L110 273L120 284L132 293L146 301L160 307" marker-end="url(#ah-phys)"/><text class="tl" x="168" y="311">T constant</text><text class="tl" x="50" y="386">ΔU = 0, so q = −W</text><text class="tl" x="340" y="222">(d) Adiabatic</text><path class="ax" d="M340 348V233M340 348H540"/><text class="tl ti" x="348" y="244">p</text><text class="tl ti" x="548" y="353">V</text><path class="ln-m thin" d="M385 348V353M450 348V353"/><text class="ts tc" x="385" y="365">V₁</text><text class="ts tc" x="450" y="365">V₂</text><path class="ln thin dash" d="M385 248L392 261L400 273L410 284L422 293L436 301L450 307"/><circle class="fi" cx="385" cy="248" r="3"/><path class="c1" d="M385 248L392 269L400 286L410 300L422 311L436 320L450 325" marker-end="url(#ah-phys)"/><text class="tl" x="458" y="311">isothermal</text><text class="tl" x="458" y="329">adiabatic</text><text class="tl" x="340" y="386">q = 0, so ΔU = W</text></svg><figcaption>The four changes on a p–V graph. In (b) the shaded area under the line is the work done by the gas. In (d) the solid line is the adiabatic change and the dashed line is the isothermal curve from the same start: the adiabatic pressure falls faster, because the gas also cools as it expands.</figcaption></figure>
:::

| Change | Held fixed | Work \(W\) (on the gas) | Energy by heating \(q\) | \(\Delta U\) |
|---|---|---|---|---|
| Constant volume | \(V\) | 0 | \(= \Delta U\) | \(q\) |
| Constant pressure | \(p\) | \(-p\,\Delta V\) | \(\Delta U - W\) | \(q + W\) |
| Isothermal (ideal gas) | \(T\) | \(-q\) | \(-W\) | 0 |
| Adiabatic | no heating | \(\Delta U\) | 0 | \(W\) |

### Constant volume

The piston cannot move, so no work is done: \(W = 0\). All the energy supplied by heating goes into internal energy, \(\Delta U = q\). If it is an ideal gas, the temperature rises and the pressure rises in proportion (the pressure law).

:::eg 0.500 mol of helium (monatomic ideal gas) in a rigid container is heated from 300 K to 400 K. Calculate the energy supplied by heating.
The volume is fixed, so \(W = 0\) and \(q = \Delta U\). [B1]
\[q = \Delta U = \tfrac32 nR\,\Delta T = 1.5 \times 0.500 \times 8.31 \times 100\] [C1]
\[q = 623\,\mathrm{J}\] [A1]
:::

### Constant pressure

When the gas is heated at constant pressure it expands, so energy supplied by heating does two jobs: it raises the internal energy and it pays for the work done pushing the piston out.

:::eg 2.00 mol of helium (monatomic ideal gas) is heated at constant pressure so that its temperature rises by 50.0 K. Calculate the energy supplied by heating, and the fraction of it that does work on the surroundings.
Internal energy: \(\Delta U = \tfrac32 nR\,\Delta T = 1.5 \times 2.00 \times 8.31 \times 50.0 = 1246.5\,\mathrm{J}\). [C1]
For an ideal gas \(p\,\Delta V = nR\,\Delta T\), so the work done *on* the gas is \(W = -nR\,\Delta T = -2.00 \times 8.31 \times 50.0 = -831\,\mathrm{J}\). [C1]
\[q = \Delta U - W = 1246.5 + 831 = 2.08 \times 10^{3}\,\mathrm{J}\] [A1]
The fraction used as work is \(831/2077.5 = 0.40\), or 40%. [A1] The other 60% stays as internal energy. This is why it takes more energy to warm a gas by 1 K at constant pressure than at constant volume.
:::

### Isothermal change

An **isothermal** change takes place at constant temperature. For an ideal gas the internal energy depends only on temperature, so \(\Delta U = 0\) and the first law gives \(q = -W\). When the gas expands, \(W\) is negative, so \(q\) is positive: energy flows in by heating to replace exactly what the gas gives out as work. In practice the change has to be slow, with the gas in good thermal contact with its surroundings, so that the heating can keep up. Boyle's law (\(pV\) constant) describes it, and the curve on the p–V graph is the one you met in [Ideal gases](#phys.gases).

:::eg An ideal gas in a cylinder is in a water bath, and its temperature stays at 300 K as it expands slowly and does 80 J of work on a piston. Calculate the energy transferred by heating, and state the direction.
The temperature is constant and the gas is ideal, so \(\Delta U = 0\). [B1]
The gas does the work, so \(W = -80\,\mathrm{J}\). [B1]
\[q = \Delta U - W = 0 - (-80) = +80\,\mathrm{J}\] [A1]
The positive sign shows that 80 J flows **into** the gas from the water. A gas that expands without any heating would cool down.
:::

### Adiabatic change

An **adiabatic** change is one in which no energy is transferred to or from the gas by heating, \(q = 0\). The gas may be perfectly insulated, or the change may be too fast for any heating to take place. Then \(\Delta U = W\): all the work goes into the internal energy.

- **Compressed adiabatically**: \(W > 0\), so \(\Delta U > 0\) and the gas **warms**. A bicycle pump gets hot at the barrel end during a fast push, partly for this reason.
- **Expanded adiabatically**: \(W < 0\), so \(\Delta U < 0\) and the gas **cools**. The gas that escapes from an aerosol can does work pushing the atmosphere out of the way, with no time to take in energy by heating, and so the spray feels cold.

An adiabatic expansion is *steeper* on a p–V graph than an isothermal one from the same start. During the isothermal expansion the heating keeps the temperature up. During the adiabatic expansion the gas cools as well as expanding, so the pressure falls further.

:::eg Explain, using the first law, why the temperature of the air in a bicycle pump rises when the plunger is pushed in quickly.
The plunger does work on the air, so \(W\) is positive. [B1]
The compression is so fast that very little energy can leave by heating, so \(q \approx 0\) and \(\Delta U = W\), so \(\Delta U\) is positive. [B1]
The internal energy of the air rises, which means the mean kinetic energy of the molecules rises, so the temperature rises. [B1]
If the plunger is pushed in slowly, energy leaves by heating as fast as the work is done, the temperature stays near room temperature, and the change is close to isothermal.
:::

:::lab Showing that a gas warms when it is compressed quickly
:::steps
1. Use a strong gas syringe containing air at room temperature. Seal the nozzle through a bung that also holds a fine thermocouple or fast thermistor probe, with the tip in the gas, connected to a data logger set to record every 0.05 s. Clamp the syringe. Do not hold the barrel, because a hand warms it.
2. Record the temperature until it is steady. Push the plunger in by a fixed volume, for example from 60 cm³ to 20 cm³, in about 0.2 s, and hold it there. Keep logging until the temperature has returned to its starting value.
3. Repeat with the same change of volume made slowly, over about a minute. Repeat each run three times and take the mean of the peak rise.
4. Plot temperature \(\theta\) against time \(t\) for both runs on the same axes.
:::
The fast compression gives a sharp rise in temperature, which then falls back as energy leaves through the syringe walls by heating. The slow compression gives almost no rise, because the energy leaves as quickly as the work is done. This agrees with the first law: when \(q \approx 0\), \(\Delta U = W\). Use a probe of small thermal capacity and short response time, because a bulky thermometer cannot follow a change lasting less than a second. Compress by the same volume each time, and allow time between runs for the gas to return to room temperature.
:::

## A complete cycle

An engine does not just expand a gas once. It takes a gas through a **cycle** of changes that returns it to its starting state, ready to start again. Because the final state is the starting state, the internal energy returns to its starting value, so over a complete cycle \(\Delta U = 0\). From the first law, \(q + W = 0\) for the whole cycle: the **net** energy supplied by heating equals the **net** work done by the gas.

:::key Work and cycles
On a p–V graph, the net work in a cycle is the **area enclosed** by the loop. If the loop is traced **clockwise** the gas does net work on its surroundings (a heat engine, as in a car). If it is traced **anticlockwise**, net work is done on the gas and energy is pumped out by heating (a refrigerator). Over one cycle, \(\Delta U = 0\), so net \(q\) = −(net \(W\)).
:::

:::html
<figure class="fig small"><svg viewBox="36 36 360 240" role="img" aria-label="A p–V graph of a triangular cycle ABC traced clockwise. A is at 2.0 by 10 to the minus 3 cubic metres and 1.0 by 10 to the 5 pascals, B is directly above A at 3.0 by 10 to the 5 pascals, and C is to the right of B at 4.0 by 10 to the minus 3 cubic metres. The triangle is shaded."><path class="fm" d="M190 185V95H310Z"/><path class="ax" d="M70 230V45M70 230H380"/><path class="ln thin dash" d="M70 185H190M70 95H190M190 185V230M310 95V230"/><path class="ln-m thin" d="M65 185H70M65 95H70M190 230V235M310 230V235"/><text class="ts te" x="62" y="189">1.0</text><text class="ts te" x="62" y="99">3.0</text><text class="ts tc" x="190" y="247">2.0</text><text class="ts tc" x="310" y="247">4.0</text><text class="tl" x="78" y="52">p / 10⁵ Pa</text><text class="tl tc" x="225" y="266">V / 10⁻³ m³</text><path class="c1" d="M190 182V102" marker-end="url(#ah-phys)"/><path class="c1" d="M194 95H304" marker-end="url(#ah-phys)"/><path class="c1" d="M304 99L196 181" marker-end="url(#ah-phys)"/><circle class="fi" cx="190" cy="185" r="4"/><circle class="fi" cx="190" cy="95" r="4"/><circle class="fi" cx="310" cy="95" r="4"/><text class="tl te" x="182" y="203">A</text><text class="tl te" x="182" y="91">B</text><text class="tl" x="318" y="91">C</text><text class="tl te" x="182" y="145">constant V</text><text class="tl tc" x="250" y="84">constant p</text><text class="tl tc" x="230" y="122">net work</text></svg><figcaption>A triangular cycle A → B → C → A, traced clockwise. The shaded area is the net work done by the gas in one cycle. A → B is at constant volume, B → C at constant pressure, and C → A is a straight line on the graph.</figcaption></figure>
:::

:::eg A monatomic ideal gas goes round the cycle in the graph above. Find \(q\), \(W\) and \(\Delta U\) for each stage, and the net work done by the gas in one cycle.
For a monatomic ideal gas \(U = \tfrac32 pV\), so use the corners: \(U_A = 1.5 \times 1.0 \times 10^{5} \times 2.0 \times 10^{-3} = 300\,\mathrm{J}\), \(U_B = 900\,\mathrm{J}\), \(U_C = 1.5 \times 3.0 \times 10^{5} \times 4.0 \times 10^{-3} = 1800\,\mathrm{J}\). [C1]
**A → B** (constant volume): \(W = 0\), \(\Delta U = 900 - 300 = +600\,\mathrm{J}\), so \(q = +600\,\mathrm{J}\). [A1]
**B → C** (constant pressure): \(W = -3.0 \times 10^{5} \times 2.0 \times 10^{-3} = -600\,\mathrm{J}\), \(\Delta U = 1800 - 900 = +900\,\mathrm{J}\), so \(q = \Delta U - W = +1500\,\mathrm{J}\). [A1]
**C → A**: the work done on the gas is the area under the line, a trapezium: \(W = \tfrac12(3.0 + 1.0) \times 10^{5} \times 2.0 \times 10^{-3} = +400\,\mathrm{J}\). \(\Delta U = 300 - 1800 = -1500\,\mathrm{J}\), so \(q = \Delta U - W = -1900\,\mathrm{J}\). [A1]

| Stage | \(q\) / J | \(W\) / J | \(\Delta U\) / J |
|---|---|---|---|
| A → B | +600 | 0 | +600 |
| B → C | +1500 | −600 | +900 |
| C → A | −1900 | +400 | −1500 |
| Whole cycle | +200 | −200 | 0 |

The net work done **by** the gas is 200 J. [A1] This equals the area of the triangle, \(\tfrac12 \times 2.0 \times 10^{-3} \times 2.0 \times 10^{5} = 200\,\mathrm{J}\), and the net energy supplied by heating (\(600 + 1500 - 1900\)) is also 200 J. [B1]
:::

The table has a pattern you can use as a check: the \(\Delta U\) column must add to zero, and each row must obey \(\Delta U = q + W\).

:::tip Engines and fridges
In a petrol engine, burning fuel supplies energy by heating (\(q > 0\)) to a gas that expands and pushes the piston (\(W < 0\)). The gas must then be compressed again and the waste gas expelled, which takes work \(W > 0\) but less than the expansion gave out, and the engine loses energy by heating to the exhaust and the cooling system. The net work out is the area of the loop, and it is always smaller than the energy put in by heating. In the cycle above, 2100 J of energy enters by heating for a net 200 J of work, and the rest leaves as heating. A fridge runs the same cycle anticlockwise: a compressor does work on the gas, and more energy leaves by heating at the back than was taken in from the food inside.
:::

:::board
AQA writes the first law as \(Q = \Delta U + W\), where \(W\) is the work done **by** the gas, so an expanding gas has positive \(W\). This is the same physics with the other sign convention for work: \(\Delta U = q + W_\text{on}\) and \(W_\text{by} = -W_\text{on}\). The Cambridge papers use \(\Delta U = q + W\) with \(W\) the work done **on** the system, so use that form in every Cambridge answer. Boards also differ in how much of this topic they examine, so check your own specification.
:::

:::eg Spot the error: A gas is compressed by a piston, which does 150 J of work on it, and 40 J of energy leaves the gas by heating. Find the increase in internal energy.
A student wrote this answer.

Line 1: \(q = -40\,\mathrm{J}\) and \(W = +150\,\mathrm{J}\)
Line 2: \(\Delta U = q - W = -40 - 150 = -190\,\mathrm{J}\)
Line 3: the internal energy decreases by 190 J.

Line 1 is correct: energy leaves the gas, so \(q\) is negative, and the gas is compressed, so \(W\) is positive. [B1] **Line 2 is wrong: with \(W\) the work done on the gas, the first law is \(\Delta U = q + W\), not \(q - W\). The method mark and the answer mark are lost.** [C0] [A0]

Correct working: \(\Delta U = q + W = -40 + 150 = +110\,\mathrm{J}\). [C1] [A1] The internal energy increases by 110 J.

Check: the gas received 150 J as work and gave away only 40 J, so it must have gained energy overall. A decrease of 190 J should have looked wrong at once.
:::

:::try Start easy, finish at exam standard
Q: State what is meant by the internal energy of a gas, and why the internal energy of an ideal gas has no potential energy part.
A: Internal energy is the sum of the random kinetic and potential energies of its molecules. In an ideal gas there are no forces between the molecules except in collisions, so there is no potential energy, and the internal energy is the kinetic energy only.
Q: A gas at \(2.0 \times 10^{5}\,\mathrm{Pa}\) is compressed at constant pressure from \(6.0 \times 10^{-3}\,\mathrm{m^3}\) to \(2.0 \times 10^{-3}\,\mathrm{m^3}\). Calculate the work done on the gas.
A: \(\Delta V = -4.0 \times 10^{-3}\,\mathrm{m^3}\), so \(W = -p\,\Delta V = -2.0 \times 10^{5} \times (-4.0 \times 10^{-3}) = +800\,\mathrm{J}\). The work is positive because the gas is compressed.
Q: 500 J of energy is supplied to a gas by heating and 200 J of work is done on it. Find \(\Delta U\).
A: \(\Delta U = q + W = 500 + 200 = 700\,\mathrm{J}\).
Q: A gas loses 300 J by heating while it does 120 J of work on its surroundings. Find \(\Delta U\), and say whether an ideal gas gets hotter or cooler.
A: \(q = -300\,\mathrm{J}\) and \(W = -120\,\mathrm{J}\), so \(\Delta U = -420\,\mathrm{J}\). The internal energy decreases, so an ideal gas gets cooler.
Q: Find the internal energy of 0.25 mol of a monatomic ideal gas at 300 K.
A: \(U = \tfrac32 nRT = 1.5 \times 0.25 \times 8.31 \times 300 = 934.9\,\mathrm{J}\), which is 0.93 kJ to 2 significant figures.
Q: A sample of ideal gas has its temperature raised at constant volume. State the value of \(W\), and what \(q\) equals.
A: The volume does not change, so no work is done and \(W = 0\). Then \(\Delta U = q\): all the energy supplied by heating increases the internal energy.
Q: In an isothermal change of an ideal gas, 60 J of work is done on the gas. State \(\Delta U\) and \(q\).
A: The temperature is constant, so \(\Delta U = 0\). Then \(q = \Delta U - W = 0 - 60 = -60\,\mathrm{J}\): 60 J of energy leaves the gas by heating.
Q: Explain why a gas cools when it expands rapidly into the air.
A: It does work on the air so \(W < 0\). The expansion is too fast for energy to enter by heating, so \(q = 0\) and \(\Delta U = W < 0\). The internal energy falls and the temperature falls.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the internal energy of a system.
A: The sum of a random distribution of kinetic energies and potential energies [B1] of the molecules of the system. [B1]
Q: [3 marks] ★ State the first law of thermodynamics in the form \(\Delta U = q + W\), and say what each of the three terms means.
A: \(\Delta U\) is the increase in internal energy of the system. [B1] \(q\) is the energy supplied to the system by heating. [B1] \(W\) is the work done on the system (negative when the gas expands). [B1]
Q: [2 marks] ★ A gas at a constant pressure of \(1.20 \times 10^{5}\,\mathrm{Pa}\) expands from \(250\,\mathrm{cm^3}\) to \(650\,\mathrm{cm^3}\). Calculate the work done by the gas.
A: \(\Delta V = 400\,\mathrm{cm^3} = 4.00 \times 10^{-4}\,\mathrm{m^3}\) and work done \(= p\,\Delta V = 1.20 \times 10^{5} \times 4.00 \times 10^{-4}\) [C1] \(= 48.0\,\mathrm{J}\). [A1]
Q: [3 marks] ★★ Explain why the internal energy of a fixed amount of an ideal gas depends only on its thermodynamic temperature.
A: There are no forces between the molecules of an ideal gas except during collisions, so the molecules have no potential energy. [B1] The internal energy is then just the sum of the random kinetic energies of the molecules. [B1] The mean kinetic energy of a molecule is \(\tfrac32 kT\), which depends only on \(T\), so \(U = \tfrac32 NkT\) depends only on \(T\). [B1]
Q: [3 marks] ★★ The gas in a can of spray paint escapes quickly through the nozzle and the can becomes cold. Use the first law to explain why.
A: The escaping gas expands and pushes back the air, so it does work on the surroundings and \(W\) is negative. [B1] The change is too fast for energy to be transferred by heating, so \(q \approx 0\) and \(\Delta U = W\), which is negative. [B1] The internal energy decreases, so the mean kinetic energy of the molecules falls and the temperature falls. [B1]
Q: [7 marks] ★★ A fixed mass of gas is taken through the cycle X → Y → Z → X. The table gives some values for each stage, and some are missing. Complete the missing values, and then find the net work done by the gas in one cycle.

| Stage | \(q\) / J | \(W\) / J | \(\Delta U\) / J |
|---|---|---|---|
| X → Y | ? | 0 | +340 |
| Y → Z | +160 | −210 | ? |
| Z → X | ? | +180 | ? |

A: X → Y: \(\Delta U = q + W\) gives \(340 = q + 0\), so \(q = +340\,\mathrm{J}\). [A1] Y → Z: \(\Delta U = 160 + (-210)\) [C1] \(= -50\,\mathrm{J}\). [A1] The gas returns to X, so \(\Delta U\) over the whole cycle is zero: [C1] Z → X has \(\Delta U = -(340 - 50) = -290\,\mathrm{J}\), [A1] and \(q = \Delta U - W = -290 - 180 = -470\,\mathrm{J}\). [A1] The net work done on the gas is \(0 - 210 + 180 = -30\,\mathrm{J}\), so the gas does 30 J of net work. [B1] (This equals the net energy supplied by heating, \(340 + 160 - 470 = 30\,\mathrm{J}\).)
Q: [4 marks] ★★★ A block of ice of mass 0.250 kg melts completely at 0 °C and atmospheric pressure, \(1.01 \times 10^{5}\,\mathrm{Pa}\). The specific latent heat of fusion of ice is \(3.34 \times 10^{5}\,\mathrm{J\,kg^{-1}}\), the density of ice is \(917\,\mathrm{kg\,m^{-3}}\) and the density of water is \(1000\,\mathrm{kg\,m^{-3}}\). (a) Calculate the energy supplied by heating. (b) Calculate the work done on the ice and water as it melts. (c) Hence show that the increase in internal energy is almost equal to the energy supplied by heating.
H: Find the volume of the ice and of the water from \(V = m/\rho\). Ice is less dense than water, so the volume falls.
H: The pressure is constant, so \(W = -p\,\Delta V\) with a negative \(\Delta V\).
A: (a) \(q = mL = 0.250 \times 3.34 \times 10^{5}\) [C1] \(= 8.35 \times 10^{4}\,\mathrm{J}\). [A1] (b) \(V_\text{ice} = 0.250/917 = 2.73 \times 10^{-4}\,\mathrm{m^3}\) and \(V_\text{water} = 2.50 \times 10^{-4}\,\mathrm{m^3}\), so \(\Delta V = -2.26 \times 10^{-5}\,\mathrm{m^3}\), and \(W = -p\,\Delta V = +2.3\,\mathrm{J}\). [A1] (c) \(\Delta U = q + W = 8.35 \times 10^{4} + 2.3\), and \(W\) is about 0.003% of \(q\), so \(\Delta U \approx q\). [B1] Almost all the energy goes into the potential energy of the molecules.
Q: [6 marks] ★★★ A fixed mass of monatomic ideal gas goes round a cycle R → S → T → R. R → S is at constant pressure \(1.0 \times 10^{5}\,\mathrm{Pa}\) from \(2.0 \times 10^{-3}\,\mathrm{m^3}\) to \(6.0 \times 10^{-3}\,\mathrm{m^3}\). S → T is a straight line on a p–V graph, to a pressure of \(5.0 \times 10^{5}\,\mathrm{Pa}\) at \(2.0 \times 10^{-3}\,\mathrm{m^3}\). T → R is at constant volume. (a) Calculate the net work done on the gas in one cycle. (b) State the net energy transferred by heating in one cycle, and its direction. (c) Calculate the energy transferred by heating in stage T → R.
H: The net work is the area of the triangle. Decide whether the loop is clockwise or anticlockwise to find who does net work on whom.
H: For (c), \(U = \tfrac32 pV\) at T and at R. The volume is constant, so \(W = 0\).
A: (a) Base \(= 4.0 \times 10^{-3}\,\mathrm{m^3}\) and height \(= 4.0 \times 10^{5}\,\mathrm{Pa}\), so area \(= \tfrac12 \times\) base \(\times\) height [C1] \(= 800\,\mathrm{J}\). The loop R → S → T → R is traced anticlockwise, so the work done is on the gas: \(+800\,\mathrm{J}\). [A1] [B1] (b) Over a whole cycle \(\Delta U = 0\), so \(q = -W = -800\,\mathrm{J}\): 800 J leaves the gas by heating. [B1] (c) \(\Delta U = \tfrac32(p_\text{R}V_\text{R} - p_\text{T}V_\text{T}) = 1.5 \times (1.0 - 5.0) \times 10^{5} \times 2.0 \times 10^{-3} = -1200\,\mathrm{J}\) [C1] and \(W = 0\), so \(q = -1200\,\mathrm{J}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A sealed syringe holds 0.0100 mol of a monatomic ideal gas at 300 K. The plunger is pushed in, so that 12.0 J of work is done on the gas. (a) The compression is so fast that no energy leaves by heating. Find the new temperature. (b) The experiment is repeated with a very slow compression that does the same 12.0 J of work, with the syringe in a water bath at 300 K. State the change in internal energy, and the energy transferred by heating. (c) After the fast compression, the plunger is held in place and the gas cools back to 300 K. State the energy transferred by heating during the cooling.
H: In (a), \(q = 0\) so \(\Delta U = W\), and \(\Delta U = \tfrac32 nR\,\Delta T\).
H: In (c), the gas finishes at the same temperature as it started, so its internal energy is back to its original value.
A: (a) \(q = 0\), so \(\Delta U = W = +12.0\,\mathrm{J}\). [B1] Then \(\Delta T = \dfrac{\Delta U}{\tfrac32 nR} = \dfrac{12.0}{1.5 \times 0.0100 \times 8.31}\) [C1] \(= 96.3\,\mathrm{K}\), so the new temperature is \(396\,\mathrm{K}\). [A1] (b) The temperature stays at 300 K, so \(\Delta U = 0\). [B1] Then \(q = -W = -12.0\,\mathrm{J}\): 12.0 J leaves the gas by heating, into the water. [B1] (c) The internal energy falls by 12.0 J while \(W = 0\), so \(q = -12.0\,\mathrm{J}\). [B1] In both cases the 12.0 J of work ends up in the surroundings as heating. The difference is that the fast compression leaves the gas hot for a while.
Q: [4 marks] ★★★ A monatomic ideal gas is heated at constant pressure. Show that 40% of the energy supplied by heating is used to do work on the surroundings.
H: Write \(p\,\Delta V = nR\,\Delta T\) and \(\Delta U = \tfrac32 nR\,\Delta T\), then add them to find \(q\).
A: The work done by the gas is \(p\,\Delta V = nR\,\Delta T\), so \(W = -nR\,\Delta T\). [M1] The internal energy increases by \(\Delta U = \tfrac32 nR\,\Delta T\). [M1] The first law gives \(q = \Delta U - W = \tfrac32 nR\,\Delta T + nR\,\Delta T = \tfrac52 nR\,\Delta T\). [M1] The fraction used as work is \(\dfrac{nR\,\Delta T}{\tfrac52 nR\,\Delta T} = \dfrac25 = 40\%\). [A1]
:::

:::quiz
? What is the internal energy of a block of ice that is melting at 0 °C, compared with the same block just before it started to melt?
+ It is greater, because the potential energy of the molecules increases while their mean kinetic energy stays the same.
- It is the same, because the temperature does not change.
- It is less, because ice is cooling the water around it.
- It is greater, because the molecules move faster.
> The energy supplied goes into the potential energy of the molecules, so \(U\) rises. The kinetic energy and the temperature do not change. Temperature constant does not mean \(U\) constant.
? A gas expands at constant pressure \(p\), and its volume increases by \(\Delta V\). What is the work done **on** the gas?
+ \(-p\,\Delta V\)
- \(+p\,\Delta V\)
- \(-\Delta V/p\)
- zero, because the pressure is constant
> The gas pushes the piston out, so it does work on the surroundings and the work done on the gas is negative. \(+p\,\Delta V\) is the work done *by* the gas. The pressure being constant makes the calculation easier, not the work zero.
? In \(\Delta U = q + W\), a gas is compressed and loses energy by heating, with \(q = -30\,\mathrm{J}\) and \(W = +50\,\mathrm{J}\). What is \(\Delta U\)?
+ \(+20\,\mathrm{J}\)
- \(-20\,\mathrm{J}\)
- \(-80\,\mathrm{J}\)
- \(+80\,\mathrm{J}\)
> \(\Delta U = -30 + 50 = +20\,\mathrm{J}\). \(-80\,\mathrm{J}\) would use the wrong sign for \(W\), and \(+80\,\mathrm{J}\) would use the wrong sign for \(q\).
? An ideal gas expands isothermally and does 200 J of work. What is the energy transferred to the gas by heating?
+ \(+200\,\mathrm{J}\)
- 0, because the temperature is constant
- \(-200\,\mathrm{J}\)
- It cannot be found without knowing the temperature.
> The internal energy of an ideal gas depends only on temperature, so \(\Delta U = 0\) and \(q = -W = +200\,\mathrm{J}\). Energy must flow in to replace the work done. Constant temperature does not mean no energy transfer.
? Why does the air in a bicycle pump warm up when the plunger is pushed in very quickly?
+ Work is done on the air and there is no time for energy to leave by heating, so its internal energy rises.
- The pump is heated by the surroundings.
- The molecules get bigger when they are squeezed.
- The air is heated by friction between the molecules and the plunger only.
> With \(q \approx 0\), \(\Delta U = W\), and \(W\) is positive for a compression. The surroundings are cooler than the air, and the molecules do not change size.
? A gas is taken round a clockwise loop on a p–V graph. What does the area enclosed by the loop represent?
+ The net work done by the gas in one cycle.
- The net work done on the gas in one cycle.
- The change in internal energy in one cycle.
- The total energy supplied by heating in one cycle.
> A clockwise loop means that the gas does more work in expanding than is done on it in being compressed, so the area is the net work done *by* the gas. The change in internal energy over a cycle is zero.
? Which statement about the internal energy of an ideal gas is correct?
+ It depends only on the thermodynamic temperature (and the amount of gas).
- It depends on both temperature and volume.
- It includes the potential energy of the molecules.
- It is zero at 273 K.
> There are no forces between the molecules of an ideal gas, so there is no potential energy, and the kinetic energy depends only on \(T\). The internal energy is zero only at absolute zero, 0 K.
:::

:::checklist What you can now do
- [ ] I can define internal energy as the sum of the random kinetic and potential energies of the molecules, and explain why it is fixed by the state of the system.
- [ ] I can relate a rise in temperature to an increase in internal energy, and explain why melting increases \(U\) with no temperature change.
- [ ] I can use \(U = \tfrac32 nRT\) for a monatomic ideal gas, and explain why an ideal gas has no potential energy.
- [ ] I can derive and use \(W = p\,\Delta V\) at constant pressure, and say whether the work is done by the gas or on it.
- [ ] I can find the work from the area under a p–V graph, including for a cycle.
- [ ] I can state and use the first law \(\Delta U = q + W\), with the correct signs.
- [ ] I can apply the first law to constant-volume, constant-pressure, isothermal and adiabatic changes.
- [ ] I can fill in a table of \(q\), \(W\) and \(\Delta U\) for a cycle and explain why \(\Delta U = 0\) for the whole cycle.
:::

:::recap
- Internal energy: the sum of the random kinetic and potential energies of the molecules. It is fixed by the state (\(p\), \(V\), \(T\)) of the system. Its change is the same along every path between two states.
- Temperature measures the mean kinetic energy of the molecules, so a rise in temperature means a rise in \(U\). Melting and boiling raise \(U\) with no temperature change (potential energy rises).
- An ideal gas has no molecular potential energy, so \(U\) depends only on \(T\). For a monatomic gas \(U = \tfrac32 nRT = \tfrac32 pV\), and \(\Delta U = \tfrac32 nR\,\Delta T\).
- Work done by a gas at constant pressure is \(p\,\Delta V\) (Pa and m³). The area under a p–V graph is the work. \(W = -p\,\Delta V\) is the work done **on** the gas, negative for an expansion.
- First law: \(\Delta U = q + W\) (\(q\): energy supplied by heating; \(W\): work done on the system).
- Constant volume: \(W = 0\), \(\Delta U = q\). Constant pressure: \(W = -p\,\Delta V\). Isothermal (ideal gas): \(\Delta U = 0\), \(q = -W\). Adiabatic: \(q = 0\), \(\Delta U = W\) (a quick compression warms the gas, a quick expansion cools it).
- Over a complete cycle \(\Delta U = 0\), so net \(q\) = −net \(W\). The net work is the area of the loop: clockwise means net work by the gas.
- Exam traps: sign of \(W\), "heat" instead of internal energy, volume in cm³ or litres, and temperature in °C in \(U = \tfrac32 nRT\).
:::

:::links
- explore: [Gas Properties](https://phet.colorado.edu/en/simulations/gas-properties) · PhET · heat and compress a gas and watch the temperature and pressure change
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the thermodynamics questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Oscillations](#phys.oscillations)
