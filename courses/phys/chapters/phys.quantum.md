@chapter phys.quantum
@title Quantum physics
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary Light as photons of energy hf, the electronvolt and photon momentum, the photoelectric effect and Einstein's equation, the de Broglie wavelength and electron diffraction, and the discrete energy levels that give atoms their line spectra.

:::why
A solar cell, a camera sensor, an LED and a neon sign all work because light and matter swap energy in fixed packets, not smoothly. Classical physics, with its continuous waves, could not explain this, and its failure started quantum physics. This chapter gives you the photon, the photoelectric effect, the wave behaviour of electrons and the energy levels of atoms, which is where the modern picture of matter begins.
:::

**Before you start**, you need the electromagnetic spectrum and \(c = f\lambda\) from [Waves](#phys.waves), diffraction and interference from [Superposition](#phys.superposition), and the energy gained by a charge moving through a p.d. from [Electric fields](#phys.efields).

:::try Warm-up
Q: Find the frequency of light of wavelength 500 nm. (from [Waves](#phys.waves))
A: \(f = c/\lambda = \dfrac{3.00 \times 10^{8}}{500 \times 10^{-9}} = 6.00 \times 10^{14}\,\mathrm{Hz}\). Convert nanometres to metres first.
Q: A beam of light spreads out after passing through a very narrow slit. What does that tell you about light? (from [Superposition](#phys.superposition))
A: Diffraction and interference are wave behaviours: only waves spread out like this, so light can behave as a wave.
Q: An electron is accelerated from rest through a p.d. of 100 V. How much energy does it gain? (from [Electric fields](#phys.efields))
A: \(W = eV = 1.60 \times 10^{-19} \times 100 = 1.60 \times 10^{-17}\,\mathrm{J}\).
:::

## Light as photons

For two centuries physicists argued about whether light was a stream of particles or a wave. Interference and diffraction settled it in favour of waves. Then experiments on light striking metal surfaces, described later in this chapter, showed something that a smooth wave cannot do: light hands over its energy in **lumps**. Each lump is a **photon**.

:::def Photon
A quantum (discrete packet) of electromagnetic energy.
:::

A photon is not a tiny ball you can see. It is the smallest amount of energy that a beam of a given frequency can give to anything. A beam cannot give half a photon, just as you cannot pay 0.5 of a penny.

:::formula Energy of a photon
\[E = hf = \frac{hc}{\lambda}\]
\(E\): energy of one photon (J) · \(h\): the Planck constant, \(6.63 \times 10^{-34}\,\mathrm{J\,s}\) · \(f\): frequency (Hz) · \(c\): speed of light, \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\) · \(\lambda\): wavelength in a vacuum (m). Photon energy depends only on frequency: higher frequency (shorter wavelength) means more energy per photon.
:::

The second form comes from \(c = f\lambda\), so \(f = c/\lambda\). Use whichever form matches the data you are given, and always change nanometres into metres first.

:::eg Compare the energy of one photon of a 100 MHz radio wave with one photon of an X-ray of wavelength 0.10 nm. Why do we notice individual photons for X-rays but never for radio waves?
Radio photon: \(E = hf = 6.63 \times 10^{-34} \times 100 \times 10^{6} = 6.63 \times 10^{-26}\,\mathrm{J}\).
X-ray photon: \(E = \dfrac{hc}{\lambda} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{0.10 \times 10^{-9}} = 1.99 \times 10^{-15}\,\mathrm{J}\).
The X-ray photon carries \(3.0 \times 10^{10}\) times as much energy. A radio transmitter sends out so many photons per second, each so small, that the energy looks perfectly smooth. A single X-ray photon carries enough energy to ionise an atom, so its arrival is a separate, detectable event.
:::

### Intensity and photon flux

A beam of single-frequency radiation delivers its power as a stream of photons. If \(N\) photons arrive every second and each carries \(hf\), the power of the beam is \(P = N\,hf\). Dividing by the area gives the intensity from [Waves](#phys.waves).

:::key Intensity of a photon beam
\[P = N\,hf \qquad\qquad I = \frac{P}{A} = \frac{N}{A}\,hf\]
\(N\): number of photons per second · \(N/A\): the photon flux, the number of photons crossing unit area each second. For a fixed frequency, doubling the intensity means doubling the number of photons per second, not the energy of each one.
:::

:::eg A laser pointer has a power of 5.0 mW and a wavelength of 650 nm. How many photons does it emit each second?
Energy of one photon: \(E = \dfrac{hc}{\lambda} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{650 \times 10^{-9}} = 3.06 \times 10^{-19}\,\mathrm{J}\). [C1]

Photons per second: \(N = \dfrac{P}{E} = \dfrac{5.0 \times 10^{-3}}{3.06 \times 10^{-19}}\) [C1] \(= 1.6 \times 10^{16}\,\mathrm{s^{-1}}\). [A1]

So even a weak laser sends out about ten million billion photons every second. That is why light seems continuous.
:::

## The electronvolt

In joules, the energies in atoms are inconveniently small, around \(10^{-19}\,\mathrm{J}\). Physicists use a unit of the right size.

:::def Electronvolt (eV)
The energy gained by an electron when it is accelerated through a potential difference of 1 V.
:::

The energy gained by a charge \(Q\) through a p.d. \(V\) is \(QV\). For an electron, \(Q = e\), so one electronvolt is \(1.60 \times 10^{-19}\,\mathrm{C} \times 1\,\mathrm{V}\):

:::formula Electronvolt conversion
\[1\,\mathrm{eV} = 1.60 \times 10^{-19}\,\mathrm{J}\]
To change eV into J, multiply by \(1.60 \times 10^{-19}\). To change J into eV, divide by it. Prefixes work as usual: \(1\,\mathrm{keV} = 10^{3}\,\mathrm{eV}\) and \(1\,\mathrm{MeV} = 10^{6}\,\mathrm{eV}\).
:::

An electron accelerated from rest through \(V\) volts gains exactly \(V\) electronvolts of kinetic energy, so an electron gun running at 150 V produces electrons of 150 eV. That direct link between volts and electronvolts is why the unit is so handy.

:::eg Calculate the energy of a photon of wavelength 450 nm (blue light) in joules and in electronvolts.
\(E = \dfrac{hc}{\lambda} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{450 \times 10^{-9}}\) [C1] \(= 4.42 \times 10^{-19}\,\mathrm{J}\). [A1]

In electronvolts: \(\dfrac{4.42 \times 10^{-19}}{1.60 \times 10^{-19}} = 2.76\,\mathrm{eV}\). [A1]
:::

:::eg Find the photon energy, in eV, at each end of the visible spectrum, 700 nm (red) and 400 nm (violet).
Red: \(E = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{700 \times 10^{-9}} = 2.84 \times 10^{-19}\,\mathrm{J} = 1.78\,\mathrm{eV}\).
Violet: \(E = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{400 \times 10^{-9}} = 4.97 \times 10^{-19}\,\mathrm{J} = 3.11\,\mathrm{eV}\).
So visible photons carry roughly 1.8 to 3.1 eV, and anything above that (ultraviolet, X-rays) carries more.
:::

:::tip A shortcut for photon energies in eV
Since \(hc/e = 1.243 \times 10^{-6}\,\mathrm{V\,m}\), a photon of wavelength \(\lambda\) in nanometres has energy about \(1240/\lambda\) in eV. Check: \(1240/450 = 2.76\,\mathrm{eV}\). Use it to check your working, but show the full calculation in an exam.
:::

:::warn Do not mix eV and joules
In \(hf = \Phi + \tfrac12 mv^2\) every term must be in joules, or every term in eV. A kinetic energy in \(\tfrac12 mv^2\) with \(m\) in kg and \(v\) in m s⁻¹ is always in joules. Changing between the two is the most common slip in this topic, so write the unit beside every number.
:::

## Photon momentum

A photon has no mass, yet it carries momentum. The relationship follows from the energy of a photon and from relativity (not needed at this level): the momentum of a photon is its energy divided by the speed of light.

:::formula Momentum of a photon
\[p = \frac{E}{c} = \frac{hf}{c} = \frac{h}{\lambda}\]
\(p\): momentum (kg m s⁻¹) · \(E\): photon energy (J) · \(c\): speed of light · \(h\): Planck constant · \(\lambda\): wavelength (m). A shorter wavelength means a larger momentum.
:::

When a photon is absorbed by a surface, its momentum is transferred to the surface, so a beam of light pushes on what it hits. The force is the rate of change of momentum, from [Dynamics](#phys.dynamics). A photon reflected straight back reverses its momentum, so the change is \(2p\), twice as much as when it is absorbed.

:::eg Calculate the momentum of a photon of wavelength 650 nm.
\(p = \dfrac{h}{\lambda} = \dfrac{6.63 \times 10^{-34}}{650 \times 10^{-9}}\) [C1] \(= 1.02 \times 10^{-27}\,\mathrm{kg\,m\,s^{-1}}\). [A1]
:::

:::eg A beam of power 5.0 mW and wavelength 650 nm is completely absorbed by a black surface. Show that the force on the surface is \(P/c\) and calculate it.
The force equals the momentum delivered per second, \(F = N\,p\), where \(N\) is the number of photons per second. [B1]

\(N = P/E\) and \(p = E/c\), so \(F = \dfrac{P}{E} \times \dfrac{E}{c} = \dfrac{P}{c}\). [C1]

\(F = \dfrac{5.0 \times 10^{-3}}{3.00 \times 10^{8}} = 1.7 \times 10^{-11}\,\mathrm{N}\). [A1]

The force is tiny, but in space there is no air resistance to hide it.
:::

:::eg A spacecraft of mass 5.0 kg carries a perfectly reflecting solar sail of area 200 m². Sunlight of intensity \(1.4\,\mathrm{kW\,m^{-2}}\) falls straight on the sail. Find the force on it and the speed it gains in one day from rest.
Power striking the sail: \(P = IA = 1400 \times 200 = 2.8 \times 10^{5}\,\mathrm{W}\).
Absorbing would give \(P/c = 9.3 \times 10^{-4}\,\mathrm{N}\). Each photon is reflected, so the momentum change doubles: \(F = \dfrac{2P}{c} = \dfrac{2 \times 2.8 \times 10^{5}}{3.00 \times 10^{8}} = 1.9 \times 10^{-3}\,\mathrm{N}\).
Acceleration: \(a = F/m = 3.7 \times 10^{-4}\,\mathrm{m\,s^{-2}}\). In one day (86 400 s): \(v = at = 32\,\mathrm{m\,s^{-1}}\).
A small push, but it never stops, and it needs no fuel. Solar sails have flown in space.
:::

## The photoelectric effect

Metals contain conduction electrons that move freely inside the metal but cannot easily leave it. If light of high enough frequency shines on a clean metal surface, electrons are ejected from the surface. This is **photoelectric emission**, and the ejected electrons are called **photoelectrons**.

:::lab A gold-leaf electroscope with a zinc plate
:::steps
1. Clean a zinc plate with emery paper to remove the oxide layer, and fix it on the cap of a gold-leaf electroscope.
2. Charge the plate **negatively** (for example by induction or with a rubbed polythene rod) so that the gold leaf rises.
3. Shine a bright filament lamp on the plate. The leaf stays up, however close or bright the lamp is.
4. Replace the lamp with an ultraviolet (UV) lamp. The leaf slowly falls: the plate is losing its negative charge.
5. Place a sheet of glass between the UV lamp and the plate. Glass absorbs UV, and the leaf stops falling.
6. Repeat with the plate **positively** charged. The leaf does not fall.
:::
:::

UV photons give electrons enough energy to leave the zinc. A negative plate repels the escaping electrons, so the charge leaks away. A positive plate pulls them straight back, so nothing is lost. Visible photons do not carry enough energy for zinc, however many of them arrive.

A tube lets you study the emission quantitatively. The metal plate (the **emitter**) and a second electrode (the **collector**) sit in an evacuated tube, so the electrons are not stopped by air. A sensitive ammeter measures the **photoelectric current**.

:::html
<figure class="fig"><svg viewBox="85 4 420 270" role="img" aria-label="An evacuated glass tube containing a metal plate on the left, the emitter, and a collector plate on the right. Light of frequency f arrives from above and strikes the emitter. Three arrows show photoelectrons travelling from the emitter to the collector. Wires from both plates pass through a microammeter below the tube."><rect class="fm s-mute sw1" x="100" y="60" width="380" height="130" rx="40"/><path class="ln" d="M196 170V225H287M313 225H424V170"/><circle class="fp s-ink sw2" cx="300" cy="225" r="13"/><text class="tb tc" x="300" y="230">A</text><rect class="fi" x="190" y="80" width="12" height="90"/><rect class="fi" x="420" y="80" width="8" height="90"/><path class="c2" d="M270 22L206 90" marker-end="url(#ah2-phys)"/><text class="tl" x="282" y="24">light, frequency f</text><path class="c1" d="M215 110H380" marker-end="url(#ah-phys)"/><path class="c1" d="M215 128H380" marker-end="url(#ah-phys)"/><path class="c1" d="M215 146H380" marker-end="url(#ah-phys)"/><text class="tl tc" x="300" y="100">photoelectrons</text><text class="tl tc" x="310" y="178">evacuated tube</text><text class="tl te" x="188" y="212">emitter</text><text class="tl" x="432" y="212">collector</text><text class="tl tc" x="300" y="262">microammeter</text></svg><figcaption>Light of frequency f strikes the emitter. If f is high enough, photoelectrons cross the vacuum to the collector, and the microammeter measures the photoelectric current.</figcaption></figure>
:::

### What experiments show

:::key Observations of photoelectric emission
1. Photoelectrons are emitted only if the frequency of the light is at least a certain minimum value, the **threshold frequency**, which depends on the metal. Below it, no electrons are emitted, however intense the light and however long it shines.
2. Emission begins immediately, with no measurable delay, even for very dim light above the threshold.
3. The **maximum kinetic energy** of the photoelectrons increases with the frequency of the light but does **not** depend on its intensity.
4. Above the threshold, the number of photoelectrons emitted per second, and so the photoelectric current, is **proportional to the intensity**.
:::

The wave theory of light, which treats light as a smooth wave spreading its energy across the whole wavefront, fails on the first three.

:::cols
:::col The wave theory predicts
Any frequency should work if the light is intense enough, because a bigger wave carries more energy.

A dim wave should take time to build up enough energy in one electron: a delay.

More intense light should eject electrons with more kinetic energy.
:::
:::col What is observed
There is a sharp threshold frequency. Intensity makes no difference below it.

Emission is immediate.

Maximum kinetic energy is independent of intensity and increases with frequency.
:::
:::

### Einstein's explanation

In 1905 Einstein explained all four observations by taking the photon seriously.

- Light arrives as photons, each with energy \(hf\).
- One photon interacts with **one** electron and gives it all its energy, in a single event. The chance of one electron absorbing two photons at once is negligible at ordinary intensities.
- The electron must do work to escape from the metal. The smallest energy needed is the work function.

:::def Work function (Φ)
The minimum energy needed to remove an electron from the surface of a metal.
:::

An electron that leaves with the minimum energy loss has the most kinetic energy. Electrons from deeper inside lose extra energy on the way out, so they leave with less. That is why the equation gives a **maximum** kinetic energy.

:::formula The photoelectric equation
\[hf = \Phi + \tfrac12 mv_{\max}^2\]
\(hf\): energy of the photon (J) · \(\Phi\): work function of the metal (J) · \(\tfrac12 mv_{\max}^2\): maximum kinetic energy of a photoelectron (J). Energy is conserved: photon energy = energy to escape + kinetic energy.
:::

At the threshold the photon just supplies the work function and the electron leaves with no kinetic energy: \(hf_0 = \Phi\).

:::def Threshold frequency
The minimum frequency of electromagnetic radiation that can cause photoelectric emission from a metal.
:::

:::def Threshold wavelength
The maximum wavelength of electromagnetic radiation that can cause photoelectric emission from a metal.
:::

:::formula Threshold frequency and wavelength
\[f_0 = \frac{\Phi}{h} \qquad\qquad \lambda_0 = \frac{c}{f_0} = \frac{hc}{\Phi}\]
Light with \(f \geq f_0\) (equivalently \(\lambda \leq \lambda_0\)) ejects electrons. A larger work function means a higher threshold frequency and a shorter threshold wavelength.
:::

:::analogy
Think of a high-jump bar set at \(\Phi\). Each photon is one jump by one electron. A jump that clears the bar by 0.5 m is a photon of energy \(\Phi + 0.5\). A crowd of jumpers who each reach only 80% of the bar height never clears it, however many of them there are. Many weak photons cannot add up their energies, because each electron can use only one.
:::

:::eg Sodium has a work function of 2.3 eV. Light of wavelength 400 nm falls on a clean sodium surface. Calculate (a) the maximum kinetic energy of the photoelectrons, (b) their maximum speed, (c) the threshold wavelength.
(a) Work function in joules: \(\Phi = 2.3 \times 1.60 \times 10^{-19} = 3.68 \times 10^{-19}\,\mathrm{J}\). [B1]

Photon energy: \(hc/\lambda = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{400 \times 10^{-9}} = 4.97 \times 10^{-19}\,\mathrm{J}\).

\(\tfrac12 mv_{\max}^2 = hf - \Phi = 4.97 \times 10^{-19} - 3.68 \times 10^{-19}\) [C1] \(= 1.29 \times 10^{-19}\,\mathrm{J}\) (0.81 eV). [A1]

(b) \(v_{\max} = \sqrt{\dfrac{2 \times 1.29 \times 10^{-19}}{9.11 \times 10^{-31}}}\) [C1] \(= 5.3 \times 10^{5}\,\mathrm{m\,s^{-1}}\). [A1]

(c) \(\lambda_0 = \dfrac{hc}{\Phi} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{3.68 \times 10^{-19}}\) [C1] \(= 5.4 \times 10^{-7}\,\mathrm{m}\), that is 540 nm. [A1]

Check: 400 nm is shorter than 540 nm, so this light is above the threshold. Light of 600 nm would eject nothing from sodium.
:::

### The graph of maximum kinetic energy against frequency

Rearrange the photoelectric equation into the form \(y = mx + c\):
\[\tfrac12 mv_{\max}^2 = hf - \Phi\]
A graph of the maximum kinetic energy (\(y\)) against frequency (\(x\)) is a straight line with these features.

- The **gradient is \(h\)**, the same for every metal, so lines for different metals are **parallel**. (In electronvolts the gradient is \(h/e\).)
- The **\(x\)-intercept is the threshold frequency** \(f_0\). Below it no electrons are emitted, so the physical line starts there.
- The **\(y\)-intercept of the extrapolated line is \(-\Phi\)**.

:::html
<figure class="fig"><svg viewBox="5 0 600 275" role="img" aria-label="Graph of maximum kinetic energy in electronvolts against frequency in units of 10 to the 14 hertz. Two parallel straight lines rise to the right: sodium crosses the frequency axis at 5.55 and zinc at 10.4. Each line is dashed where it is extended back below the axis to its negative intercept, minus 2.3 electronvolts for sodium and minus 4.3 electronvolts for zinc."><path class="ax" d="M80 262V14" marker-end="url(#ah)"/><path class="ax" d="M80 115H548" marker-end="url(#ah)"/><path class="c1 dash" d="M80 188.6L290.9 115"/><path class="c1" d="M290.9 115L536 29.5"/><path class="c2 dash" d="M80 252.6L474.3 115"/><path class="c2" d="M474.3 115L536 93.5"/><path class="ln" d="M156 115V120M232 115V120M308 115V120M384 115V120M460 115V120M536 115V120M80 83H75M80 51H75M80 19H75"/><text class="ts tc halo" x="156" y="132">2</text><text class="ts tc halo" x="232" y="132">4</text><text class="ts tc halo" x="308" y="132">6</text><text class="ts tc halo" x="384" y="132">8</text><text class="ts tc halo" x="460" y="132">10</text><text class="ts tc halo" x="536" y="132">12</text><text class="ts te" x="71" y="86">1</text><text class="ts te" x="71" y="54">2</text><text class="ts te" x="71" y="22">3</text><text class="tl te" x="73" y="129">O</text><circle class="fa" cx="290.9" cy="115" r="4"/><circle class="fa" cx="474.3" cy="115" r="4"/><circle class="fa" cx="80" cy="188.6" r="4"/><circle class="fa" cx="80" cy="252.6" r="4"/><text class="tl te" x="285" y="104">f₀ (Na)</text><text class="tl te" x="468" y="104">f₀ (Zn)</text><text class="tl te" x="72" y="193">−2.3 eV</text><text class="tl te" x="72" y="257">−4.3 eV</text><text class="tl" x="86" y="14">KEmax / eV</text><text class="tl te" x="548" y="152">f / 10¹⁴ Hz</text><text class="tl" x="544" y="33">sodium</text><text class="tl" x="544" y="97">zinc</text></svg><figcaption>Both lines have the same gradient, h/e. Each is solid where electrons are emitted (above its threshold frequency) and dashed where it is extended back to the vertical axis, which it meets at −Φ in electronvolts. A larger work function shifts the line to the right.</figcaption></figure>
:::

:::eg Use the graph above to find the work function of zinc in electronvolts, and the maximum kinetic energy of photoelectrons from sodium when the frequency is \(8.0 \times 10^{14}\,\mathrm{Hz}\).
The zinc line crosses the frequency axis at \(f_0 = 10.4 \times 10^{14}\,\mathrm{Hz}\). [B1]

\(\Phi = hf_0 = 6.63 \times 10^{-34} \times 10.4 \times 10^{14}\) [C1] \(= 6.9 \times 10^{-19}\,\mathrm{J}\), which is \(\dfrac{6.9 \times 10^{-19}}{1.60 \times 10^{-19}} = 4.3\,\mathrm{eV}\). [A1] (It agrees with the \(y\)-intercept, \(-4.3\,\mathrm{eV}\).)

On the sodium line at \(8.0 \times 10^{14}\,\mathrm{Hz}\), the height is about 1.0 eV. [B1]
:::

### Intensity: current changes, kinetic energy does not

Suppose the frequency is above threshold and you double the intensity. Twice as many photons arrive every second. Each photon still has energy \(hf\) and each frees at most one electron, so twice as many electrons leave every second: the **photoelectric current doubles**. But each electron still received its energy from one photon of energy \(hf\), so the **maximum kinetic energy is unchanged**.

:::plot Above the threshold, the photoelectric current is proportional to the intensity: a straight line through the origin.
--f "0.8*x" --x 0 6 --y 0 5.4 --xlabel "relative intensity" --ylabel "I / μA" --label "I ∝ intensity"
:::

:::plot The maximum kinetic energy of the photoelectrons does not change with intensity at a fixed frequency: a horizontal line.
--f "0.81+0*x" --x 0 6 --y 0 1.6 --xlabel "relative intensity" --ylabel "KEmax / eV" --label "constant"
:::

:::warn Constant power is not constant intensity of photons
If you raise the frequency but keep the **power** of the beam the same, each photon carries more energy, so fewer photons arrive each second and the current **falls**. For 2.0 mW of light, the number of photons per second is \(4.0 \times 10^{15}\,\mathrm{s^{-1}}\) at 400 nm but only \(3.0 \times 10^{15}\,\mathrm{s^{-1}}\) at 300 nm: three quarters as many. Current is proportional to photons per second, not to power.
:::

:::eg Explain why doubling the intensity of the light, at a fixed frequency above the threshold, doubles the photoelectric current but does not change the maximum kinetic energy of the photoelectrons.
Doubling the intensity doubles the number of photons arriving per second, and each photon frees at most one electron, so the number of electrons emitted per second doubles. [B1]

Each electron is freed by a single photon, and the photon energy \(hf\) depends only on the frequency, which has not changed. [B1]

So the energy available to each electron, and therefore \(\tfrac12 mv_{\max}^2 = hf - \Phi\), is unchanged. [B1]
:::

:::exam Writing the photoelectric explanation
Examiners reward these words in order: **one photon**, **one electron**, **energy \(hf\)**, **work function**, **threshold**. A reliable pattern is: "A photon gives all its energy to one electron. If \(hf < \Phi\), the electron cannot escape, whatever the number of photons. If \(hf > \Phi\), the extra energy is the kinetic energy." Never say that brighter light gives the electrons more energy: it gives more photons.
:::

Now try it. Choose a metal and move the wavelength from the infrared to the ultraviolet. Look for the threshold, then raise the intensity below it (nothing) and above it (more electrons, same speed).

:::html
<div class="widget" data-w="phys-photo" data-metal="sodium" data-lambda="400"></div>
:::

### Stopping potential

The kinetic energy of the fastest photoelectrons can be measured by making the collector negative. A reverse p.d. repels the electrons, and when it is just large enough that even the fastest cannot reach the collector, the current is zero. This p.d. is the **stopping potential** \(V_s\) (a useful idea, though this syllabus does not use the term). The work done against the field equals the kinetic energy lost:

\[eV_s = \tfrac12 mv_{\max}^2\]

:::eg What stopping potential brings the photoelectrons in the sodium example above to rest?
\(eV_s = \tfrac12 mv_{\max}^2 = 1.29 \times 10^{-19}\,\mathrm{J}\), so \(V_s = \dfrac{1.29 \times 10^{-19}}{1.60 \times 10^{-19}} = 0.81\,\mathrm{V}\).
The stopping potential in volts has the same number as the kinetic energy in electronvolts: 0.81 V, 0.81 eV.
:::

:::lab Finding the Planck constant with a photocell
:::steps
1. Connect a photocell to a sensitive current meter and a variable reverse p.d. (from a potential divider, as in [D.C. circuits](#phys.dc)), with a voltmeter across the cell.
2. Shine light of known frequency on the cell, using coloured filters or LEDs of known wavelength. Keep the lamp the same distance away each time and shield the cell from room light.
3. Increase the reverse p.d. until the photocurrent just falls to zero, and record \(V_s\). The current dies away gradually, so plot current against p.d. for each colour and extrapolate to zero if the end is blurred.
4. Repeat for at least five different frequencies.
5. Since \(eV_s = hf - \Phi\), \(V_s = \dfrac{h}{e}f - \dfrac{\Phi}{e}\). Plot \(V_s\) against \(f\). The gradient is \(h/e\), so \(h = e \times \text{gradient}\). The intercept on the frequency axis is \(f_0\), and the \(y\)-intercept is \(-\Phi/e\).
:::
:::

:::eg In a photocell experiment the graph of \(V_s\) against frequency has gradient \(4.1 \times 10^{-15}\,\mathrm{V\,s}\). Find the Planck constant.
\(h = e \times \text{gradient}\) [C1] \(= 1.60 \times 10^{-19} \times 4.1 \times 10^{-15} = 6.6 \times 10^{-34}\,\mathrm{J\,s}\). [A1]
Check the units: \(\mathrm{C \times V\,s} = \mathrm{J\,s}\), because \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\).
:::

## Wave–particle duality

Two sets of evidence now pull in opposite directions.

:::cols
:::col Evidence for a wave nature
Light **diffracts** at a narrow slit and **interferes** in a double-slit pattern, with bright and dark fringes. Only waves do this, because the pattern comes from the superposition of waves, as in [Superposition](#phys.superposition).
:::
:::col Evidence for a particle nature
The **photoelectric effect**: threshold frequency, energy delivered in single packets, and kinetic energy set by \(hf\) and not by intensity. Only a particle picture explains these.
:::
:::

Electromagnetic radiation therefore shows both behaviours: it spreads like a wave and exchanges energy like a particle. Which one you see depends on the experiment. This is called **wave–particle duality**. The surprising next step was to ask whether matter can do the same.

### Electron diffraction

Fast electrons are fired at a very thin film of graphite, whose atoms are arranged in regular layers. The electrons that pass through hit a fluorescent screen and make it glow.

:::html
<figure class="fig"><svg viewBox="15 0 635 270" role="img" aria-label="An evacuated tube. On the left a hot cathode and an anode connected to an accelerating supply of p.d. V produce an electron beam. The beam passes through a thin graphite film and spreads into two cones of diffracted electrons that strike a fluorescent screen at the right. A separate small picture shows the pattern on the screen: two concentric rings."><rect class="fm s-mute sw1" x="30" y="20" width="490" height="190" rx="40"/><path class="ln" d="M70 121V225H105M113 225H130V145"/><path class="ln thick" d="M105 219V231"/><path class="ln" d="M113 212V238"/><circle class="fi" cx="70" cy="115" r="6"/><path class="ln thick" d="M130 85V108M130 122V145"/><path class="c1" d="M138 115H244" marker-end="url(#ah-phys)"/><path class="ln thick" d="M250 95V135"/><path class="c2" d="M254 115L498 75" marker-end="url(#ah2-phys)"/><path class="c2" d="M254 115L498 155" marker-end="url(#ah2-phys)"/><path class="c2" d="M254 115L498 45" marker-end="url(#ah2-phys)"/><path class="c2" d="M254 115L498 185" marker-end="url(#ah2-phys)"/><path class="ln thick" d="M500 40V190"/><circle class="c1" cx="590" cy="115" r="20"/><circle class="c1" cx="590" cy="115" r="35"/><circle class="fi" cx="590" cy="115" r="3"/><text class="tl tc" x="70" y="95">cathode</text><text class="tl tc" x="130" y="75">anode</text><text class="tl tc" x="190" y="102">electron beam</text><text class="tl tc" x="250" y="80">thin graphite film</text><text class="tl tc" x="370" y="203">diffracted electrons</text><text class="tl te" x="505" y="232">fluorescent screen</text><text class="tl tc" x="110" y="258">accelerating p.d. V</text><text class="tl tc" x="590" y="172">pattern on screen</text></svg><figcaption>Electrons accelerated through V pass through a thin graphite film. Instead of a single spot, the screen shows concentric rings, a diffraction pattern. A larger p.d. gives a shorter wavelength and smaller rings.</figcaption></figure>
:::

If electrons were only particles, you would expect most of them to go straight through, with a smear of scattered ones. Instead you see **concentric rings**: a diffraction pattern, like the one that light gives. The rings arise because the electrons behave as waves that diffract at the regularly spaced atoms of the graphite and then interfere. So electrons, which were thought of as particles, show a wave nature.

- Diffraction is significant only when the wavelength is comparable with the spacing of the diffracting objects. The rings tell us the electron wavelength is about the spacing of atoms, of the order \(10^{-10}\,\mathrm{m}\).
- Raise the accelerating p.d. and the rings **shrink**: faster electrons have a **shorter** wavelength, so they are diffracted through smaller angles.

### The de Broglie wavelength

In 1924 de Broglie suggested that every moving particle has a wavelength linked to its momentum, in the same way as a photon (\(p = h/\lambda\)).

:::def De Broglie wavelength
The wavelength associated with a moving particle.
:::

:::formula The de Broglie wavelength
\[\lambda = \frac{h}{p} = \frac{h}{mv}\]
\(\lambda\): de Broglie wavelength (m) · \(h\): Planck constant · \(p\): momentum of the particle (kg m s⁻¹) · \(m\): mass (kg) · \(v\): speed (m s⁻¹). The more momentum, the shorter the wavelength.
:::

For an electron accelerated from rest through a p.d. \(V\), you will often need the momentum from the energy.

:::proof Momentum and wavelength of an accelerated electron
The electron gains kinetic energy \(eV\) from the p.d.: \(\tfrac12 mv^2 = eV\).
Multiply both sides by \(2m\): \(m^2v^2 = 2meV\).
The left side is \(p^2\), so \(p = \sqrt{2meV}\).
Substitute into \(\lambda = h/p\): \(\lambda = \dfrac{h}{\sqrt{2meV}}\).
So \(\lambda \propto 1/\sqrt{V}\): quadrupling the p.d. halves the wavelength.
:::

:::eg Calculate the de Broglie wavelength of an electron accelerated from rest through a p.d. of 150 V. Comment on the answer.
\(p = \sqrt{2meV} = \sqrt{2 \times 9.11 \times 10^{-31} \times 1.60 \times 10^{-19} \times 150}\) [C1] \(= 6.61 \times 10^{-24}\,\mathrm{kg\,m\,s^{-1}}\).

\(\lambda = \dfrac{h}{p} = \dfrac{6.63 \times 10^{-34}}{6.61 \times 10^{-24}}\) [C1] \(= 1.0 \times 10^{-10}\,\mathrm{m}\). [A1]

This is about the spacing between atoms in a crystal, which is why a crystal or graphite film diffracts such electrons.
:::

:::eg Calculate the de Broglie wavelength of a cricket ball of mass 0.16 kg moving at \(30\,\mathrm{m\,s^{-1}}\). Why do we not see cricket balls diffract?
\(\lambda = \dfrac{h}{mv} = \dfrac{6.63 \times 10^{-34}}{0.16 \times 30} = 1.4 \times 10^{-34}\,\mathrm{m}\).
This is about \(10^{19}\) times smaller than a nucleus. No gap or obstacle is anywhere near that small, so diffraction is far too tiny to detect. Wave behaviour appears only for very light particles such as electrons, where \(p\) is small.
:::

:::eg In an electron diffraction tube the accelerating p.d. is raised so that the speed of the electrons increases. State and explain what happens to the radius of the rings on the screen.
A larger speed means a larger momentum \(p = mv\), so the de Broglie wavelength \(\lambda = h/p\) decreases. [B1]

The diffraction angle is smaller for a shorter wavelength (the angle is about \(\lambda\) divided by the spacing). [B1]

So the rings move closer to the centre: their radii decrease. [B1]
:::

:::warn Momentum, not energy
In \(\lambda = h/p\), \(p\) is the **momentum**. If you know the kinetic energy \(E_k\), find \(p = \sqrt{2mE_k}\) first. Using \(h/E_k\) gives a wavelength with the wrong unit.
:::

## Energy levels and line spectra

Heat a solid filament and it glows with a smooth, **continuous spectrum** of all colours. Heat a gas at low pressure, such as the neon in a sign, and it emits only a few particular wavelengths: separate bright **lines** on a dark background. Each element has its own set of lines, like a fingerprint. A continuous wave model cannot explain that. Photons can.

In an **isolated atom**, such as one in a low-pressure gas, the electrons can only have certain energies.

:::def Energy level
One of the discrete values of energy that an electron in an isolated atom can have.
:::

The energies are measured from zero, the energy of an electron that has just escaped the atom. The electron is bound, so it has **negative** energy. The lowest level is the **ground state**; the higher levels are **excited states**. The energy needed to remove an electron from the ground state to infinity is the **ionisation energy**: 13.6 eV for hydrogen.

:::html
<figure class="fig"><svg viewBox="62 10 393 430" role="img" aria-label="Energy-level diagram for hydrogen. Horizontal lines at minus 13.6, minus 3.40, minus 1.51 and minus 0.85 electronvolts for n equals 1 to 4, and a dashed line at zero for ionisation. Six downward arrows show transitions: 2 to 1, 3 to 1, 4 to 1, 3 to 2, 4 to 2 and 4 to 3."><path class="ln-m thin dash" d="M120 30H380"/><path class="ln thick" d="M120 54.6H380M120 73.8H380M120 128.6H380M120 424.4H380"/><path class="c1" d="M150 128.6V422" marker-end="url(#ah-phys)"/><path class="c1" d="M186 73.8V422" marker-end="url(#ah-phys)"/><path class="c1" d="M222 54.6V422" marker-end="url(#ah-phys)"/><path class="c1" d="M258 73.8V126" marker-end="url(#ah-phys)"/><path class="c1" d="M294 54.6V126" marker-end="url(#ah-phys)"/><path class="c1" d="M330 54.6V71.5" marker-end="url(#ah-phys)"/><text class="tl te" x="112" y="34">n = ∞</text><text class="tl te" x="112" y="58.6">n = 4</text><text class="tl te" x="112" y="77.8">n = 3</text><text class="tl te" x="112" y="132.6">n = 2</text><text class="tl te" x="112" y="428.4">n = 1</text><text class="tl" x="388" y="34">0</text><text class="tl" x="388" y="58.6">−0.85 eV</text><text class="tl" x="388" y="77.8">−1.51 eV</text><text class="tl" x="388" y="132.6">−3.40 eV</text><text class="tl" x="388" y="428.4">−13.6 eV</text><text class="tl" x="156" y="395">2→1</text><text class="tl" x="192" y="395">3→1</text><text class="tl" x="228" y="395">4→1</text><text class="tl" x="264" y="108">3→2</text><text class="tl" x="300" y="108">4→2</text><text class="tl" x="336" y="68">4→3</text></svg><figcaption>The first four energy levels of hydrogen, drawn to scale. Each arrow is one de-excitation: the atom emits one photon whose energy equals the drop. Four levels give six possible lines.</figcaption></figure>
:::

An electron can move between levels only by gaining or losing exactly the energy difference.

:::formula Photon emitted or absorbed in a transition
\[hf = E_1 - E_2 = \frac{hc}{\lambda}\]
\(E_1\): energy of the higher level · \(E_2\): energy of the lower level · \(f, \lambda\): frequency and wavelength of the photon. The photon energy equals the energy gap, so a large drop gives a short wavelength.
:::

- **Emission.** An excited atom drops from \(E_1\) to a lower level \(E_2\) and emits **one** photon of energy \(E_1 - E_2\), in a random direction.
- **Absorption.** An atom absorbs a photon only if its energy equals a gap between levels **exactly**, and the electron jumps up. A photon with any other energy passes by. (A photon with energy above the ionisation energy can still ionise the atom, and the extra energy goes to the electron as kinetic energy.)
- **Excitation by collision.** A fast electron can excite an atom by giving up an amount of energy equal to a gap, keeping the rest as kinetic energy. This is how electric discharges make gases glow.

:::eg An electron in a hydrogen atom drops from \(n = 3\) to \(n = 2\). Find the wavelength of the photon emitted and say whether it is visible.
The energy released: \(E = E_3 - E_2 = -1.51 - (-3.40) = 1.89\,\mathrm{eV}\), so \(E = 1.89 \times 1.60 \times 10^{-19} = 3.02 \times 10^{-19}\,\mathrm{J}\). [C1]

\(\lambda = \dfrac{hc}{E} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{3.02 \times 10^{-19}}\) [C1] \(= 6.58 \times 10^{-7}\,\mathrm{m}\), that is 658 nm. [A1]

This lies between 400 nm and 700 nm, so it is visible: it is the red line of hydrogen. [B1]
:::

The six transitions between four levels give:

| Transition | Energy / eV | Wavelength / nm | Region |
|---|---|---|---|
| 4 → 3 | 0.66 | 1880 | infrared |
| 4 → 2 | 2.55 | 488 | visible |
| 3 → 2 | 1.89 | 658 | visible |
| 4 → 1 | 12.75 | 97.5 | ultraviolet |
| 3 → 1 | 12.09 | 103 | ultraviolet |
| 2 → 1 | 10.20 | 122 | ultraviolet |

An atom with \(n\) levels can emit at most \(\dfrac{n(n-1)}{2}\) different photon energies, because there is one line for each pair of levels. For \(n = 4\) that is 6; for \(n = 5\) it is 10.

### Emission and absorption spectra

:::html
<figure class="fig"><svg viewBox="75 5 500 245" role="img" aria-label="Three horizontal strips drawn against a wavelength scale from 400 to 700 nanometres. The first is a plain bright strip, a continuous spectrum. The second is a dark strip with four bright lines at 411, 435, 488 and 658 nanometres, an emission spectrum. The third is a bright strip with dark lines at the same four wavelengths, an absorption spectrum."><text class="tl" x="90" y="22">continuous spectrum (hot solid)</text><rect class="fp s-ink sw1" x="90" y="30" width="420" height="36"/><text class="tl" x="90" y="92">emission spectrum (hot gas at low pressure)</text><rect class="fi" x="90" y="100" width="420" height="36"/><rect class="fp" x="104.4" y="100" width="3" height="36"/><rect class="fp" x="137.9" y="100" width="3" height="36"/><rect class="fp" x="211" y="100" width="3" height="36"/><rect class="fp" x="449.9" y="100" width="3" height="36"/><text class="tl" x="90" y="162">absorption spectrum (cool gas in front of a hot source)</text><rect class="fp s-ink sw1" x="90" y="170" width="420" height="36"/><rect class="fi" x="104.4" y="170" width="3" height="36"/><rect class="fi" x="137.9" y="170" width="3" height="36"/><rect class="fi" x="211" y="170" width="3" height="36"/><rect class="fi" x="449.9" y="170" width="3" height="36"/><path class="ax" d="M90 220H520"/><path class="ln" d="M90 220V226M230 220V226M370 220V226M510 220V226"/><text class="ts tc" x="90" y="240">400</text><text class="ts tc" x="230" y="240">500</text><text class="ts tc" x="370" y="240">600</text><text class="ts tc" x="510" y="240">700</text><text class="tl" x="524" y="224">λ / nm</text></svg><figcaption>Bright lines on a dark background (emission) and dark lines on a bright background (absorption) appear at the same wavelengths for the same element. The four lines drawn are the visible lines of hydrogen, from the transitions 3→2, 4→2, 5→2 and 6→2.</figcaption></figure>
:::

:::cols
:::col Emission line spectrum
A hot gas at low pressure is excited, for example by an electric discharge. Atoms drop between levels and emit photons only at the wavelengths that match the gaps. The result is **bright lines on a dark background**.
:::
:::col Absorption line spectrum
White light, which contains every wavelength, passes through a cool gas. Photons whose energy matches a gap are absorbed. The atoms re-emit the energy in all directions, so little of it continues in the original direction. The result is **dark lines on a bright, continuous background**, at the same wavelengths as the bright emission lines of that element.
:::
:::

Astronomers use this. The dark lines in sunlight show which elements are in the cooler outer layers of the Sun, and helium was first identified in the Sun's spectrum before anyone found it on Earth.

:::eg A hydrogen atom in its ground state is hit by a free electron of kinetic energy 11 eV. Which transitions can the collision cause, and with what energy does the electron move away?
The ground state is at \(-13.6\,\mathrm{eV}\). The gap to \(n = 2\) is \(13.6 - 3.40 = 10.2\,\mathrm{eV}\), which is less than 11 eV, so the atom can be excited to \(n = 2\). [B1]

The gap to \(n = 3\) is \(13.6 - 1.51 = 12.1\,\mathrm{eV}\), more than 11 eV, so no higher level can be reached. [B1]

The electron keeps \(11 - 10.2 = 0.8\,\mathrm{eV}\) of kinetic energy. [A1]
:::

:::eg What is the longest wavelength of a photon that can ionise a hydrogen atom in its ground state? What kinetic energy does the electron have if the photon has an energy of 20 eV?
The minimum photon energy is the ionisation energy, \(13.6\,\mathrm{eV} = 13.6 \times 1.60 \times 10^{-19} = 2.18 \times 10^{-18}\,\mathrm{J}\).
\(\lambda_{\max} = \dfrac{hc}{E} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{2.18 \times 10^{-18}} = 9.14 \times 10^{-8}\,\mathrm{m}\), that is 91.4 nm, in the ultraviolet.
With a 20 eV photon, the energy left for the electron is \(20 - 13.6 = 6.4\,\mathrm{eV}\).
:::

:::board
Cambridge asks for the photoelectric equation, \(\lambda = h/p\) and \(hf = E_1 - E_2\) without naming the stopping potential. Other specifications ask for it by name and for how it is measured, which is why the stopping-potential section above is worth knowing. The core equations are the same in every specification.
:::

:::eg Spot the error: calculate the de Broglie wavelength of an electron accelerated from rest through 150 V.
A student wrote this answer.

Line 1: kinetic energy \(E_k = eV = 1.60 \times 10^{-19} \times 150 = 2.4 \times 10^{-17}\,\mathrm{J}\)
Line 2: \(\lambda = \dfrac{h}{E_k} = \dfrac{6.63 \times 10^{-34}}{2.4 \times 10^{-17}} = 2.8 \times 10^{-17}\,\mathrm{m}\)

Line 1 is correct. [C1] **Line 2 is wrong: the de Broglie formula uses the momentum \(p\), not the energy.** The answer mark is lost. [A0]

Correct working: \(p = \sqrt{2mE_k} = \sqrt{2 \times 9.11 \times 10^{-31} \times 2.4 \times 10^{-17}} = 6.61 \times 10^{-24}\,\mathrm{kg\,m\,s^{-1}}\), so \(\lambda = h/p = 1.0 \times 10^{-10}\,\mathrm{m}\). [A1]

Check: a wavelength of \(10^{-17}\,\mathrm{m}\) is far smaller than a nucleus, so it should have looked wrong immediately.
:::

:::try Start easy, finish at exam standard
Q: Calculate the energy, in eV, of a photon with a frequency of \(4.5 \times 10^{14}\,\mathrm{Hz}\).
A: \(E = hf = 6.63 \times 10^{-34} \times 4.5 \times 10^{14} = 2.98 \times 10^{-19}\,\mathrm{J}\), and \(2.98 \times 10^{-19}/1.60 \times 10^{-19} = 1.9\,\mathrm{eV}\).
Q: Change 2.4 eV into joules and \(3.2 \times 10^{-19}\,\mathrm{J}\) into electronvolts.
A: \(2.4 \times 1.60 \times 10^{-19} = 3.84 \times 10^{-19}\,\mathrm{J}\), and \(3.2 \times 10^{-19}/1.60 \times 10^{-19} = 2.0\,\mathrm{eV}\).
Q: Caesium has a work function of 2.1 eV. Find its threshold wavelength.
A: \(\Phi = 2.1 \times 1.60 \times 10^{-19} = 3.36 \times 10^{-19}\,\mathrm{J}\), and \(\lambda_0 = hc/\Phi = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{3.36 \times 10^{-19}} = 5.9 \times 10^{-7}\,\mathrm{m}\) (590 nm).
Q: Ultraviolet light of wavelength 300 nm falls on zinc, of work function 4.3 eV. Are photoelectrons emitted?
A: Photon energy \(= hc/\lambda = 6.63 \times 10^{-19}\,\mathrm{J} = 4.14\,\mathrm{eV}\), which is less than 4.3 eV. So no photoelectrons are emitted, however intense the light.
Q: Calculate the momentum of a photon of wavelength 500 nm.
A: \(p = h/\lambda = \dfrac{6.63 \times 10^{-34}}{500 \times 10^{-9}} = 1.3 \times 10^{-27}\,\mathrm{kg\,m\,s^{-1}}\).
Q: An electron moves at \(2.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\). Find its de Broglie wavelength.
A: \(\lambda = \dfrac{h}{mv} = \dfrac{6.63 \times 10^{-34}}{9.11 \times 10^{-31} \times 2.0 \times 10^{6}} = 3.6 \times 10^{-10}\,\mathrm{m}\).
Q: An electron in hydrogen falls from \(n = 2\) to \(n = 1\). Find the photon's energy and wavelength, and say whether it is visible.
A: \(E = 13.6 - 3.40 = 10.2\,\mathrm{eV} = 1.63 \times 10^{-18}\,\mathrm{J}\). \(\lambda = hc/E = 1.22 \times 10^{-7}\,\mathrm{m}\) (122 nm). It is ultraviolet, so it is not visible.
Q: A 60 W lamp turns 5.0% of its power into visible light of mean wavelength 550 nm. How many photons of visible light does it emit each second?
A: Visible power \(= 0.050 \times 60 = 3.0\,\mathrm{W}\). Photon energy \(= hc/\lambda = 3.62 \times 10^{-19}\,\mathrm{J}\). \(N = 3.0/3.62 \times 10^{-19} = 8.3 \times 10^{18}\,\mathrm{s^{-1}}\).
Q: A student says: "A very bright red lamp should eject electrons from zinc, because it delivers so much energy." Explain why this is wrong.
A: Energy arrives in photons, and one photon gives its energy to one electron. A red photon has energy below the 4.3 eV work function of zinc, so no electron can escape. More photons per second do not help, because the energies cannot be added.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define the work function of a metal.
A: The minimum energy needed to remove an electron from the surface of the metal. [B1]
Q: [2 marks] ★ A sodium vapour lamp emits light of wavelength 590 nm. Calculate the energy of one photon, in eV.
A: \(E = \dfrac{hc}{\lambda} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{590 \times 10^{-9}} = 3.37 \times 10^{-19}\,\mathrm{J}\) [C1] \(= 2.1\,\mathrm{eV}\). [A1]
Q: [3 marks] ★★ Light of fixed frequency, above the threshold frequency, falls on a metal. Explain why the maximum kinetic energy of the photoelectrons does not depend on the intensity of the light, whereas the photoelectric current is proportional to the intensity.
A: Each photon gives all its energy \(hf\) to one electron, and \(hf\) depends only on the frequency, so the maximum kinetic energy \(hf - \Phi\) is the same for any intensity. [B1] A larger intensity means more photons per second. [B1] Each photon frees at most one electron, so more electrons are emitted per second and the current is proportional to the intensity. [B1]
Q: [3 marks] ★★ Ultraviolet light of wavelength 254 nm falls on a calcium surface of work function 2.9 eV. Calculate the maximum speed of the photoelectrons.
A: \(\tfrac12 mv_{\max}^2 = \dfrac{hc}{\lambda} - \Phi = 7.83 \times 10^{-19} - 2.9 \times 1.60 \times 10^{-19}\) [C1] \(= 3.19 \times 10^{-19}\,\mathrm{J}\). \(v_{\max} = \sqrt{\dfrac{2 \times 3.19 \times 10^{-19}}{9.11 \times 10^{-31}}}\) [C1] \(= 8.4 \times 10^{5}\,\mathrm{m\,s^{-1}}\). [A1]
Q: [3 marks] ★★ Describe how an electron diffraction experiment provides evidence for the wave nature of electrons.
A: A beam of electrons of the same speed passes through a thin graphite film (a regular arrangement of atoms) and strikes a fluorescent screen. [B1] A pattern of concentric rings is seen, a diffraction pattern, and diffraction and interference are wave properties. [B1] The rings are produced only if the wavelength is about the spacing of the atoms, and the de Broglie wavelength of the electrons is of that size. [B1]
Q: [4 marks] ★★ Electrons are accelerated from rest through a p.d. of 600 V. (a) Calculate the de Broglie wavelength of the electrons. (b) The p.d. is increased to 2400 V. State the new wavelength.
A: (a) \(p = \sqrt{2meV}\) with \(V = 600\,\mathrm{V}\) [C1] \(= 1.32 \times 10^{-23}\,\mathrm{kg\,m\,s^{-1}}\), so \(\lambda = \dfrac{h}{p} = \dfrac{6.63 \times 10^{-34}}{1.32 \times 10^{-23}}\) [C1] \(= 5.0 \times 10^{-11}\,\mathrm{m}\). [A1] (b) \(\lambda \propto 1/\sqrt{V}\), and the p.d. has increased by a factor of 4, so \(\lambda\) halves, to \(2.5 \times 10^{-11}\,\mathrm{m}\). [B1]
Q: [6 marks] ★★★ The four lowest energy levels of an atom X are \(-9.0\,\mathrm{eV}\), \(-5.0\,\mathrm{eV}\), \(-3.0\,\mathrm{eV}\) and \(-2.0\,\mathrm{eV}\). (a) State the number of different spectral lines that can be emitted by transitions between these levels. (b) Calculate the longest wavelength emitted. (c) Calculate the shortest wavelength emitted. (d) State which of the lines are in the visible spectrum (400 nm to 700 nm).
H: Longest wavelength means smallest photon energy, so the smallest gap between two levels.
H: Find every gap first: between \(-9.0\) and \(-5.0\), and so on. Convert the smallest and largest from eV into joules.
A: (a) Four levels give \(4 \times 3/2 = 6\) lines. [B1] (b) The smallest gap is \(-3.0\) to \(-2.0\,\mathrm{eV}\), which is 1.0 eV, so \(\lambda = \dfrac{hc}{E} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{1.0 \times 1.60 \times 10^{-19}}\) [C1] \(= 1.2 \times 10^{-6}\,\mathrm{m}\). [A1] (c) The largest gap is \(-9.0\) to \(-2.0\,\mathrm{eV}\), which is 7.0 eV, so \(\lambda = \dfrac{hc}{7.0 \times 1.60 \times 10^{-19}}\) [C1] \(= 1.8 \times 10^{-7}\,\mathrm{m}\). [A1] (d) The gaps are 1.0, 2.0, 3.0, 4.0, 6.0 and 7.0 eV. Wavelengths between 400 nm and 700 nm need 1.8 to 3.1 eV, so the 2.0 eV line (622 nm) and the 3.0 eV line (414 nm) are visible. [B1]
Q: [5 marks] ★★★ A student measures the maximum kinetic energy of photoelectrons from a metal for five frequencies. The frequencies, in units of \(10^{14}\,\mathrm{Hz}\), are 6.0, 7.0, 8.0, 9.0 and 10.0, and the kinetic energies, in eV, are 0.19, 0.60, 1.01, 1.43 and 1.84. The best-fit line passes through the first and last points. (a) Use the line to find a value for the Planck constant. (b) Find the work function of the metal in eV. (c) The experiment is repeated with a metal of greater work function. State how the graph differs.
H: Gradient in SI units: change the eV into joules and the frequency into hertz.
H: At the threshold the kinetic energy is zero, so extrapolate to find \(f_0\), or use the \(y\)-intercept \(-\Phi\).
A: (a) gradient \(= \dfrac{(1.84 - 0.19) \times 1.60 \times 10^{-19}}{(10.0 - 6.0) \times 10^{14}}\) [C1] \(= 6.6 \times 10^{-34}\,\mathrm{J\,s}\), the Planck constant. [A1] (b) The \(y\)-intercept is \(0.19 - 0.4125 \times 6.0 = -2.3\,\mathrm{eV}\) (gradient 0.4125 eV per \(10^{14}\,\mathrm{Hz}\)), [C1] so \(\Phi = 2.3\,\mathrm{eV}\). [A1] (c) A parallel line (same gradient) shifted to the right, with a larger threshold frequency. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A photon and an electron both have a wavelength of 0.10 nm. (a) Show that their momenta are equal and calculate it. (b) Calculate the energy of the photon, in keV. (c) Calculate the kinetic energy of the electron, in eV. (d) Suggest why electrons are better than X-rays for probing very small structures with a short wavelength, if energy damage is to be small.
H: Both obey \(p = h/\lambda\), so the momenta match. For the electron use \(E_k = p^2/2m\).
H: For (d), compare the energies delivered to the sample for the same wavelength.
A: (a) For both, \(p = h/\lambda\) [M1] \(= \dfrac{6.63 \times 10^{-34}}{0.10 \times 10^{-9}} = 6.6 \times 10^{-24}\,\mathrm{kg\,m\,s^{-1}}\), so the momenta are equal. [A1] (b) \(E = pc = 6.63 \times 10^{-24} \times 3.00 \times 10^{8} = 1.99 \times 10^{-15}\,\mathrm{J}\) [C1] \(= 12.4\,\mathrm{keV}\). [A1] (c) \(E_k = \dfrac{p^2}{2m} = \dfrac{(6.63 \times 10^{-24})^2}{2 \times 9.11 \times 10^{-31}} = 2.41 \times 10^{-17}\,\mathrm{J} = 151\,\mathrm{eV}\). [A1] (d) For the same wavelength (and so the same detail), the electron carries about 80 times less energy than the photon, so electrons deposit much less energy in the sample. [B1]
Q: [6 marks] ★★★ A laser of power 20 W and wavelength 532 nm is directed straight at a small, perfectly reflecting mirror, which reflects the beam straight back. (a) Calculate the number of photons reaching the mirror per second. (b) Show that the force on the mirror is \(2P/c\) and calculate it. (c) Calculate the greatest mass the light could support against gravity.
H: Each photon's momentum changes from \(+p\) to \(-p\).
H: Use the acceleration of free fall, \(g = 9.81\,\mathrm{m\,s^{-2}}\).
A: (a) \(E = hc/\lambda = 3.74 \times 10^{-19}\,\mathrm{J}\) [C1] so \(N = P/E = 5.3 \times 10^{19}\,\mathrm{s^{-1}}\). [A1] (b) The change in momentum per photon is \(2p\), so \(F = N \times 2p = \dfrac{P}{E} \times \dfrac{2E}{c} = \dfrac{2P}{c}\) [M1] \(= \dfrac{2 \times 20}{3.00 \times 10^{8}} = 1.3 \times 10^{-7}\,\mathrm{N}\). [A1] (c) The weight equals the force: \(m = \dfrac{F}{g} = \dfrac{1.33 \times 10^{-7}}{9.81}\) [C1] \(= 1.4 \times 10^{-8}\,\mathrm{kg}\), about 14 micrograms. [A1] So even a 20 W laser supports only a few specks of dust.
:::

:::quiz
? Which quantity decides the energy of one photon of electromagnetic radiation?
+ Its frequency
- The intensity of the beam
- The number of photons in the beam
- The distance travelled from the source
> \(E = hf\), so the energy per photon depends only on frequency. Intensity changes how many photons arrive each second, not how much each carries.
? Light above the threshold frequency falls on a metal. The intensity is doubled. What happens to the maximum kinetic energy of the photoelectrons?
+ It stays the same.
- It doubles.
- It halves.
- It increases, but by less than double.
> Each electron receives its energy from one photon, and the photon energy has not changed. Only the number of electrons per second doubles.
? On a graph of the maximum kinetic energy of photoelectrons against frequency, what does the gradient give?
+ The Planck constant
- The work function
- The threshold frequency
- The charge on an electron
> The gradient of \(hf - \Phi\) against \(f\) is \(h\), the same for all metals. The work function is minus the \(y\)-intercept and the threshold frequency is the \(x\)-intercept.
? What is 1 eV?
+ \(1.60 \times 10^{-19}\,\mathrm{J}\)
- \(1.60 \times 10^{-19}\,\mathrm{V}\)
- \(6.25 \times 10^{18}\,\mathrm{J}\)
- \(1.60 \times 10^{-19}\,\mathrm{C}\)
> One electronvolt is the energy gained by an electron through 1 V, \(e \times 1\,\mathrm{V} = 1.60 \times 10^{-19}\,\mathrm{J}\). The volt is a unit of p.d., and the coulomb a unit of charge.
? Which observation could the wave theory of light NOT explain?
+ Photoelectrons are emitted instantly even from very dim light above the threshold.
- Light is diffracted at a narrow slit.
- Light waves form fringes in a double-slit experiment.
- The light from a lamp spreads out as it travels.
> A smooth wave should take time to build up enough energy in one electron, but emission is immediate. Diffraction, interference and spreading are all explained by waves.
? Electrons are accelerated through a larger p.d. in an electron diffraction tube. What happens to the de Broglie wavelength?
+ It decreases.
- It increases.
- It stays the same.
- It is proportional to the p.d.
> A larger p.d. gives a larger momentum, and \(\lambda = h/p\) decreases. Strictly \(\lambda \propto 1/\sqrt{V}\), so it does not increase and it is not proportional to \(V\).
? Why does the emission spectrum of a hot gas consist of separate lines?
+ The electrons in the atoms can only have certain energies, so only certain photon energies are emitted.
- The atoms in the gas collide and emit only a few photons.
- The gas absorbs all the other wavelengths before they leave.
- The atoms vibrate at only a few frequencies.
> Transitions between discrete energy levels release photons of fixed energy \(hf = E_1 - E_2\). Collisions only excite the atoms; the lines come from the level structure.
? A cool gas is placed between a white-light source and a spectrometer. What is seen?
+ Dark lines on a bright, continuous background
- Bright lines on a dark background
- A continuous spectrum with no lines
- A single bright line
> The gas absorbs only photons whose energies match its gaps, and re-emits them in all directions. The dark lines are at the wavelengths of the gas's own emission lines.
:::

:::checklist What you can now do
- [ ] I can state that electromagnetic radiation has a particulate nature, define a photon, and use \(E = hf\) and \(E = hc/\lambda\), including the number of photons per second in a beam.
- [ ] I can use the electronvolt and convert between eV and J.
- [ ] I can recall and use \(p = E/c = h/\lambda\) for the momentum of a photon.
- [ ] I can describe the photoelectric effect and explain why the wave theory cannot account for it.
- [ ] I can explain photoelectric emission using photon energy and the work function, and use \(hf = \Phi + \tfrac12 mv_{\max}^2\), the threshold frequency and the threshold wavelength.
- [ ] I can explain why the maximum kinetic energy is independent of intensity while the photoelectric current is proportional to it.
- [ ] I can analyse a graph of maximum kinetic energy against frequency to find \(h\), \(\Phi\) and \(f_0\).
- [ ] I can explain how electron diffraction shows the wave nature of particles, and use \(\lambda = h/p\).
- [ ] I can explain energy levels and emission and absorption line spectra, and use \(hf = E_1 - E_2\).
:::

:::recap
- A photon is a quantum of electromagnetic energy: \(E = hf = hc/\lambda\), with momentum \(p = E/c = h/\lambda\). Intensity \(= (N/A)hf\).
- \(1\,\mathrm{eV} = 1.60 \times 10^{-19}\,\mathrm{J}\): the energy gained by an electron through 1 V. Keep all terms in joules or all in eV.
- Photoelectric emission: one photon gives all its energy to one electron. \(hf = \Phi + \tfrac12 mv_{\max}^2\). Below \(f_0 = \Phi/h\) (above \(\lambda_0 = hc/\Phi\)) no emission, whatever the intensity.
- Maximum kinetic energy depends on frequency, not on intensity. Current is proportional to the number of photons per second, so to intensity at fixed frequency.
- Kinetic energy against frequency: straight line, gradient \(h\), \(x\)-intercept \(f_0\), \(y\)-intercept \(-\Phi\), parallel for all metals.
- Interference and diffraction show a wave nature. The photoelectric effect shows a particle nature. Electron diffraction (rings through graphite) shows that particles have wave properties.
- De Broglie: \(\lambda = h/p = h/mv\). For an accelerated electron \(p = \sqrt{2meV}\), so \(\lambda \propto 1/\sqrt{V}\).
- Isolated atoms have discrete negative energy levels. A transition emits or absorbs one photon: \(hf = E_1 - E_2\). Emission spectra are bright lines on dark; absorption spectra are dark lines on a bright background. \(n\) levels give up to \(n(n-1)/2\) lines.
:::

:::links
- explore: [Photoelectric Effect](https://phet.colorado.edu/en/simulations/photoelectric) · PhET · change the metal, the wavelength and the intensity and watch the photoelectrons
- explore: [Models of the Hydrogen Atom](https://phet.colorado.edu/en/simulations/models-of-the-hydrogen-atom) · PhET · fire light at hydrogen and see which transitions occur
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the quantum physics questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Nuclear physics](#phys.nuclear)
