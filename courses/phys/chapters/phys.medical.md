@chapter phys.medical
@title Medical physics
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary How hospitals look inside the body without cutting it open: ultrasound pulses and the reflections at tissue boundaries, X-rays and CT scans with the attenuation law that gives them contrast, and PET scans that locate a radioactive tracer from the gamma rays of positron annihilation.

:::why
Waves, quantum physics and radioactivity are not only theory: a hospital uses all three every day. Ultrasound shows a baby in the womb with no radiation at all, X-rays and CT scans show bones and organs by how much of a beam each part absorbs, and a PET scan shows which tissue is busy by tracking a radioactive tracer. This chapter applies ideas you already own to real instruments, and every instrument turns into an exam calculation that you can do from first principles.
:::

**Before you start**, you need intensity and wave speed from [Waves](#phys.waves), photons and electronvolts from [Quantum physics](#phys.quantum), exponential decay from [Nuclear physics](#phys.nuclear), and positrons from [Particle physics](#phys.particles).

:::try Warm-up
Q: Ultrasound of frequency 3.0 MHz travels through soft tissue at \(1540\,\mathrm{m\,s^{-1}}\). Find its wavelength. (from [Waves](#phys.waves))
A: \(\lambda = v/f = 1540/(3.0 \times 10^{6}) = 5.1 \times 10^{-4}\,\mathrm{m}\), about 0.51 mm.
Q: Find the energy, in joules and in keV, of an X-ray photon of wavelength 0.10 nm. (from [Quantum physics](#phys.quantum))
A: \(E = hc/\lambda\), so \[E = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{1.0 \times 10^{-10}} = 1.99 \times 10^{-15}\,\mathrm{J}\] Divide by \(1.60 \times 10^{-19}\,\mathrm{J\,eV^{-1}}\): 12 keV.
Q: What fraction of a radioactive sample is left after two half-lives? (from [Nuclear physics](#phys.nuclear))
A: Each half-life halves the number of nuclei, so after two the fraction is \(\tfrac12 \times \tfrac12 = \tfrac14\).
:::

## Ultrasound and the piezoelectric effect

**Ultrasound** is sound with a frequency above 20 kHz, the upper limit of human hearing. Medical scanners use frequencies from about 1 MHz to 15 MHz. Like all sound it is a longitudinal wave that needs a medium, and it travels through soft tissue at about \(1540\,\mathrm{m\,s^{-1}}\). You will see in a moment why such a high frequency is chosen.

To make and detect these waves you need a device that turns electrical signals into vibrations and vibrations back into electrical signals. A **piezoelectric crystal** does both.

:::def Piezoelectric effect
A piezoelectric crystal changes shape when a potential difference is applied across it, and it generates an e.m.f. across it when its shape is changed (when it is squeezed or stretched).
:::

Quartz and some ceramics have this property. The two halves of the effect are the same physics running in opposite directions: electrical energy to mechanical energy, and mechanical energy to electrical energy. A **transducer** is any device that converts one form of energy to another, and the **ultrasound transducer** in a scanner probe is a thin piezoelectric crystal with a metal electrode on each face.

:::html
<figure class="fig"><svg viewBox="5 5 515 262" role="img" aria-label="Cross-section of an ultrasound probe. A case holds a backing block above a thin piezoelectric crystal with electrodes joined to an a.c. supply. Below the case are a gel layer and soft tissue. A pulse arrow goes down into the tissue to a boundary and an echo arrow comes back up."><rect class="fm s-mute sw1" x="190" y="30" width="120" height="120" rx="4"/><rect class="fm2 s-ink sw1" x="200" y="40" width="100" height="92"/><rect class="f1 s-acc sw2" x="200" y="132" width="100" height="16"/><rect class="fm s-mute sw1" x="190" y="150" width="120" height="8"/><rect class="fm2 s-mute sw1" x="170" y="158" width="170" height="97"/><path class="ln" d="M215 132V18H110V87M200 140H110V113"/><circle class="fp s-ink sw2" cx="110" cy="100" r="13"/><text class="tb tc" x="110" y="105">~</text><text class="tl te" x="92" y="104">a.c. supply</text><path class="c1" d="M250 166V218" marker-end="url(#ah-phys)"/><path class="c2" d="M290 218V166" marker-end="url(#ah2-phys)"/><path class="ln-m thin dash" d="M170 226H340"/><text class="tl te" x="243" y="196">pulse</text><text class="tl" x="298" y="196">echo</text><text class="tl" x="178" y="178">tissue</text><text class="tl" x="178" y="243">tissue boundary</text><path class="ln-m thin" d="M349 60L302 60M349 124L302 138M349 174L312 154"/><text class="tl" x="355" y="64">backing block</text><text class="tl" x="355" y="127">piezoelectric crystal</text><text class="tl" x="355" y="178">gel</text></svg><figcaption>An ultrasound probe. The same crystal sends the pulse and, a moment later, receives the echo. The backing block stops the crystal ringing, so the pulse is short. The gel fills the gap between probe and skin.</figcaption></figure>
:::

:::steps
1. **Generation.** An alternating p.d. from the scanner is applied across the crystal. The crystal expands and contracts with the same frequency, so its face pushes the tissue back and forth and sends out an ultrasound wave. The p.d. is chosen at the crystal's resonant frequency, because at resonance the crystal vibrates with the largest amplitude, so it sends out the most intense wave for the energy supplied (see [Oscillations](#phys.oscillations)).
2. **Pulses.** The p.d. is applied for only about a microsecond. The backing block, made of a material that absorbs vibrations, damps the crystal so that it stops vibrating almost at once. The result is a short pulse of ultrasound, usually two or three cycles long.
3. **Detection.** After the pulse has gone, the crystal waits. Echoes returning from inside the body arrive as pressure variations that squeeze and stretch the crystal. By the second half of the piezoelectric effect it generates an alternating e.m.f. of the same frequency. This is amplified and sent to a computer.
:::

The probe spends nearly all of its time listening: one pulse lasts about a microsecond, and the echoes take tens of microseconds to return. That is why a single crystal can do both jobs.

:::eg Calculate the wavelength of 5.0 MHz ultrasound in soft tissue and explain why frequencies of megahertz are used in scanners.
\[\lambda = \frac{v}{f} = \frac{1540}{5.0 \times 10^{6}} = 3.1 \times 10^{-4}\,\mathrm{m}\] [C1] [A1]
This is 0.31 mm. A wave is reflected only by structures that are not much smaller than its wavelength, so a wavelength of a few tenths of a millimetre lets the scanner show structures about a millimetre in size. [B1] Audible sound has wavelengths of metres in tissue and would show nothing so small.
:::

## Pulse-echo imaging

Ultrasound is reflected at a **boundary** between two different tissues. The scanner sends a short pulse into the body, measures how long each echo takes to return and uses the speed of sound to turn that time into a distance. This is the same idea as the echo of your shout from a cliff, or the sonar of a ship.

The pulse travels from the probe to the boundary and back, a distance \(2d\), at speed \(v\). So the time of the echo is \(t = 2d/v\):

:::formula Depth from an echo
\[d = \frac{vt}{2}\]
\(d\): depth of the boundary (m) · \(v\): speed of sound in the tissue (\(\mathrm{m\,s^{-1}}\)) · \(t\): time between sending the pulse and receiving the echo (s). The factor 2 is there because the pulse goes there **and back**.
:::

:::eg An echo from a boundary in soft tissue returns 65 μs after the pulse was sent. How deep is the boundary? (Speed of sound in soft tissue: \(1540\,\mathrm{m\,s^{-1}}\), typical.)
\[d = \frac{vt}{2} = \frac{1540 \times 65 \times 10^{-6}}{2}\] [C1]
\[d = 5.0 \times 10^{-2}\,\mathrm{m} = 5.0\,\mathrm{cm}\] [A1]
:::

### A-scans and B-scans

An **A-scan** (amplitude scan) uses one fixed probe pointing in one direction. The computer plots the amplitude of the returning signal against time, which is the same as against depth. Each boundary on the beam's path gives a spike, and a larger spike means a larger fraction of the pulse was reflected there.

:::html
<figure class="fig"><svg viewBox="0 0 540 232" role="img" aria-label="An A-scan. Above, a probe on the left sends a beam through soft tissue past boundaries at 3.0, 6.0 and 9.0 centimetres, the last being bone. Below, an amplitude against time trace shows the transmitted pulse at time zero and echoes at 39, 78 and 117 microseconds, the bone echo being largest."><rect class="fm s-mute sw1" x="90" y="26" width="400" height="44"/><rect class="f2 s-ink sw1" x="450" y="26" width="40" height="44"/><path class="ln-m" d="M210 26V70M330 26V70"/><rect class="f2 s-ink sw2" x="58" y="34" width="32" height="28"/><text class="tl te" x="52" y="52">probe</text><path class="c1" d="M100 40H200" marker-end="url(#ah-phys)"/><path class="c2" d="M200 56H100" marker-end="url(#ah2-phys)"/><text class="tl tc" x="210" y="18">3.0 cm</text><text class="tl tc" x="330" y="18">6.0 cm</text><text class="tl tc" x="450" y="18">9.0 cm</text><text class="tl tc" x="470" y="52">bone</text><path class="ln-m thin dash" d="M210 70V150M330 70V170M450 70V130"/><path class="ax" d="M80 200H520M80 200V100"/><text class="tl" x="88" y="110">echo amplitude</text><path class="c1 sw2" d="M90 200V126"/><text class="tl" x="98" y="138">pulse sent</text><path class="c1 sw2" d="M210 200V150M330 200V170M450 200V130"/><text class="tl" x="218" y="160">echo 1</text><text class="tl" x="338" y="180">echo 2</text><text class="tl" x="458" y="140">bone echo</text><path class="ax" d="M90 200V204M210 200V204M330 200V204M450 200V204"/><text class="ts tc" x="90" y="219">0</text><text class="ts tc" x="210" y="219">39</text><text class="ts tc" x="330" y="219">78</text><text class="ts tc" x="450" y="219">117</text><text class="tl te" x="520" y="219">t / μs</text></svg><figcaption>An A-scan through tissue with boundaries at 3.0 cm, 6.0 cm and 9.0 cm (speed of sound 1540 m s⁻¹). Each echo arrives at t = 2d/v, so the time axis is also a depth axis. The bone gives the biggest echo.</figcaption></figure>
:::

A **B-scan** (brightness scan) makes a two-dimensional picture. The probe is moved across the skin, or contains a row of many small crystals that each send a pulse in turn. Every pulse gives one A-scan, but now each echo is shown as a **dot whose brightness depends on the echo's amplitude** instead of a spike. The computer lines the rows of dots up side by side, one per beam position, and the result is a cross-section of the body, such as a foetus in the womb.

:::eg An ultrasound scanner images to a depth of 15 cm in soft tissue. Calculate the shortest time that must pass between sending one pulse and the next, and the greatest number of pulses per second.
The echo from the deepest boundary takes \(t = 2d/v = 2 \times 0.15/1540\) [C1] \(= 1.9 \times 10^{-4}\,\mathrm{s}\). [A1]
A new pulse sent sooner would produce echoes that mix with those from the last pulse. The greatest rate is \(1/t\), using the unrounded value of \(t\) (\(1.948 \times 10^{-4}\,\mathrm{s}\)): \(5.1 \times 10^{3}\) pulses per second. [A1]
:::

:::eg Two boundaries in tissue are 2.0 mm apart along the beam. By how much do their echoes differ in arrival time? A pulse of three cycles at 5.0 MHz is used. Can the scanner show the two boundaries separately?
The echo from the further boundary has an extra \(2 \times 2.0\) mm to travel: \(\Delta t = \dfrac{2\Delta d}{v} = \dfrac{2 \times 2.0 \times 10^{-3}}{1540}\) [C1] \(= 2.6 \times 10^{-6}\,\mathrm{s} = 2.6\,\mu\mathrm{s}\). [A1]
The pulse lasts \(3/f = 3/(5.0 \times 10^{6}) = 0.60\,\mu\mathrm{s}\), which is shorter than \(2.6\,\mu\mathrm{s}\), so the echoes arrive as two separate pulses and the boundaries can be told apart. [B1]
:::

This is why the pulse must be short and why the backing block matters: a long pulse makes echoes from close boundaries overlap into one blur. A higher frequency has a shorter wavelength and, for the same number of cycles, a shorter pulse, so the detail improves. The price of a higher frequency is more **attenuation**, which you meet below: high frequencies are absorbed more, so they cannot reach deep. Scanners therefore use about 3 MHz for deep organs and higher frequencies for structures near the skin.

:::lab Measuring the speed of ultrasound by pulse-echo
:::steps
1. Place an ultrasound transmitter and receiver side by side facing a flat reflecting board, with a metre rule along the line to the board. Connect the receiver to an oscilloscope, triggered by the transmitter's pulse.
2. Put the board at a measured distance \(d\) from the transmitter. Read the time \(t\) between the transmitted pulse and the echo on the oscilloscope screen, using a large number of divisions to keep the percentage uncertainty small.
3. Repeat for at least six distances, from about 0.20 m to 1.50 m.
4. Plot \(t\) (y-axis) against \(d\). Because \(t = 2d/v\), the graph is a straight line through the origin with gradient \(2/v\), so \(v = 2/\text{gradient}\).
:::
:::

:::eg A student's graph of echo time \(t\) against distance \(d\) is a straight line through the origin with gradient \(5.88 \times 10^{-3}\,\mathrm{s\,m^{-1}}\). Find the speed of the ultrasound.
The gradient is \(2/v\), so \(v = \dfrac{2}{5.88 \times 10^{-3}}\) [C1] \(= 3.40 \times 10^{2}\,\mathrm{m\,s^{-1}}\). [A1]
This is the speed of sound in air, as expected for a classroom set-up.
:::

:::warn Forgetting that the echo goes there and back
The clock measures a round trip. If you use \(d = vt\) you get **twice** the real depth. Always divide by 2, or write \(2d = vt\) before you substitute.
:::

Ultrasound has a good safety record: it is not ionising, so at the intensities of diagnostic scanning it does not damage cells in the way X-rays can. That is why it is the first choice for imaging a foetus, and it also images the heart and soft tissues such as the liver and muscle. It cannot image through bone or air, as the next section explains.

## Acoustic impedance and reflection

How much of the pulse comes back from a boundary? That depends on how different the two media are. The property that matters is the **acoustic impedance**, which measures how much a medium resists the passage of sound.

:::def Specific acoustic impedance
The product of the density of a medium and the speed of sound in that medium: \(Z = \rho c\).
:::

\(\rho\) is the density in \(\mathrm{kg\,m^{-3}}\) and \(c\) the speed of sound in \(\mathrm{m\,s^{-1}}\), so \(Z\) is in \(\mathrm{kg\,m^{-2}\,s^{-1}}\). A boundary between two media with the same \(Z\) reflects nothing: the pulse carries straight on. The bigger the difference between the two \(Z\) values, the more is reflected.

:::def Intensity reflection coefficient
The ratio of the reflected intensity to the incident intensity at a boundary: \(I_R/I_0\).
:::

:::formula Intensity reflection coefficient
\[\frac{I_R}{I_0} = \frac{(Z_1 - Z_2)^2}{(Z_1 + Z_2)^2}\]
\(I_0\): intensity of the incident wave · \(I_R\): intensity of the reflected wave · \(Z_1, Z_2\): specific acoustic impedances of the two media. The rest, \(I_0 - I_R\), is transmitted through the boundary.
:::

The formula is the same whichever medium is \(Z_1\). It gives 0 when \(Z_1 = Z_2\), and it approaches 1 when one \(Z\) is far bigger than the other. It is about **intensity**, not amplitude. Typical values used in this chapter are:

| Medium | Density / \(\mathrm{kg\,m^{-3}}\) | Speed / \(\mathrm{m\,s^{-1}}\) | \(Z\) / \(\mathrm{kg\,m^{-2}\,s^{-1}}\) |
|---|---|---|---|
| air | 1.3 | 330 | \(4.3 \times 10^{2}\) |
| soft tissue | 1060 | 1540 | \(1.63 \times 10^{6}\) |
| bone | 1900 | 4000 | \(7.6 \times 10^{6}\) |

:::eg Calculate the intensity reflection coefficient at a boundary between soft tissue and bone, using the table above.
Soft tissue: \(Z_1 = 1060 \times 1540 = 1.63 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\). Bone: \(Z_2 = 1900 \times 4000 = 7.6 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\). [C1]
\[\frac{I_R}{I_0} = \frac{(1.6324 - 7.6)^2}{(1.6324 + 7.6)^2}\] [C1]
\[\frac{I_R}{I_0} = \frac{5.9676^2}{9.2324^2} = 0.418\] [A1]
So 42% of the intensity is reflected and 58% is transmitted. [B1] A boundary with bone gives a large echo and also hides what lies behind it, because the bone also attenuates the rest strongly.
:::

:::eg Calculate the reflection coefficient at a boundary between air and soft tissue. Explain why a gel is used between the probe and the skin.
\[\frac{I_R}{I_0} = \frac{(429 - 1.6324 \times 10^{6})^2}{(429 + 1.6324 \times 10^{6})^2} = 0.999\] [C1] [A1]
So 99.9% of the ultrasound is reflected and only 0.1% enters the body, if there is any air between the probe and the skin. [B1]
The gel has an acoustic impedance close to that of skin (take \(1.50 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\)) and fills every gap, so there is no air layer. Then \(\dfrac{I_R}{I_0} = \dfrac{(1.50 - 1.6324)^2}{(1.50 + 1.6324)^2} = 1.8 \times 10^{-3}\), so over 99.8% passes into the body. [C1] [A1]
:::

:::warn Impedance, not speed
The reflection coefficient needs \(Z = \rho c\), not the speed alone and not the density alone. Two media can have very different densities and speeds and still have similar \(Z\), and then there is hardly any echo. Check the units too: \(Z\) is in \(\mathrm{kg\,m^{-2}\,s^{-1}}\).
:::

## Attenuation

An ultrasound pulse loses intensity as it travels, even when it does not meet a boundary. Some of its energy is absorbed and becomes thermal energy, and some is scattered away from the beam. The gradual loss of intensity is called **attenuation**, and it follows an exponential law, as radioactive decay does.

:::def Attenuation
The gradual loss of intensity of a beam as it passes through a medium. For a parallel beam the transmitted intensity is \(I = I_0 e^{-\mu x}\), where \(\mu\) is the attenuation coefficient (also called the linear absorption coefficient) of the medium.
:::

:::formula Attenuation law
\[I = I_0 e^{-\mu x}\]
\(I_0\): intensity entering the medium · \(I\): intensity after a thickness \(x\) · \(\mu\): attenuation coefficient (\(\mathrm{m^{-1}}\), or \(\mathrm{cm^{-1}}\)) · \(x\) in the same length unit as \(1/\mu\). This law holds for ultrasound and for X-rays.
:::

The coefficient \(\mu\) is large for a medium that attenuates strongly, and it depends on the frequency of the ultrasound: it is greater for higher frequencies. For soft tissue at 3 MHz, a typical value is \(\mu = 35\,\mathrm{m^{-1}}\). Equal thicknesses always remove equal fractions: if the first 2 cm halves the intensity, the next 2 cm halves what is left.

:::plot Attenuation of 3 MHz ultrasound in soft tissue (μ = 0.35 cm⁻¹). Every 1.98 cm of tissue halves the intensity.
--f "exp(-0.35*x)+0*sqrt(7-x)" --x 0 8.5 --y 0 1.3 --pt "1.98,0.5,x½ = 2.0 cm@ne" --pt "3.96,0.25,4.0 cm@ne" --xlabel "x / cm" --ylabel "I / I₀"
:::

The distance that halves the intensity is the **half-value thickness**, \(x_{1/2}\). Put \(I = \tfrac12 I_0\): \(e^{-\mu x_{1/2}} = \tfrac12\), so \(\mu x_{1/2} = \ln 2\) and \(x_{1/2} = 0.693/\mu\), exactly as \(t_{1/2} = 0.693/\lambda\) for decay. A graph of \(\ln I\) against \(x\) is a straight line with gradient \(-\mu\).

:::lab Finding the attenuation coefficient of a material for gamma rays
:::steps
1. Place a gamma source, a Geiger-Müller tube and counter in a line with a fixed gap. Measure the background count rate with the source removed, over a long time.
2. Put sheets of the material between source and tube, increasing the thickness \(x\) in equal steps (use a micrometer or calipers on the stack). At each thickness count for long enough to collect several hundred counts.
3. Subtract the background rate to get the corrected count rate \(C\) at each thickness. The count rate is proportional to the intensity.
4. Plot \(\ln C\) against \(x\). The line has gradient \(-\mu\), because \(\ln C = \ln C_0 - \mu x\).
:::
:::

:::eg In an attenuation experiment the corrected count rate is \(820\,\mathrm{s^{-1}}\) with no absorber and \(165\,\mathrm{s^{-1}}\) behind a 16 mm thickness of aluminium. Find \(\mu\) in \(\mathrm{m^{-1}}\).
\[\ln\frac{165}{820} = -\mu x\] so \(\mu = \dfrac{\ln(820/165)}{16 \times 10^{-3}}\) [C1] \(= 1.0 \times 10^{2}\,\mathrm{m^{-1}}\). [A1]
:::

:::eg A pulse of ultrasound reflects from a boundary 4.0 cm deep in soft tissue (\(\mu = 35\,\mathrm{m^{-1}}\)). What fraction of the intensity has survived attenuation when the echo returns to the probe?
The pulse crosses the tissue twice, so \(x = 2 \times 4.0\,\mathrm{cm} = 0.080\,\mathrm{m}\). [B1]
\[\frac{I}{I_0} = e^{-\mu x} = e^{-35 \times 0.080}\] [C1] \(= 0.061\), or 6.1%. [A1]
Only 6% of the intensity survives attenuation even before the loss at the boundary itself is counted.
:::

:::eg Find the half-value thickness of soft tissue for 3 MHz ultrasound (\(\mu = 35\,\mathrm{m^{-1}}\)).
\[x_{1/2} = \frac{0.693}{\mu} = \frac{0.693}{35}\] [C1] \(= 0.020\,\mathrm{m} = 2.0\,\mathrm{cm}\). [A1]
:::

The echo that returns to the probe has been through **both** effects: attenuation on the way there, the loss at the boundary, and attenuation on the way back. Multiply the three factors.

:::eg Ultrasound travels in soft tissue to a boundary with bone 3.0 cm deep and the echo returns to the probe. Use \(\mu = 35\,\mathrm{m^{-1}}\) and the impedances in the table. What fraction of the intensity at the probe comes back?
Distance in tissue there and back: \(x = 2 \times 3.0 = 6.0\,\mathrm{cm} = 0.060\,\mathrm{m}\). [B1]
Attenuation factor: \(e^{-35 \times 0.060} = 0.1225\). [C1]
Reflection: \(0.418\) at the boundary (from the example above), so the fraction that returns is \(0.1225 \times 0.418\) [C1] \(= 0.051\), about 5.1%. [A1]
The reflection happens once, but the attenuation happens over the whole path.
:::

:::exam Echo intensity questions
Write the chain of factors in order, one line each: \(e^{-\mu x}\) down to the boundary, then \(I_R/I_0\) at the boundary, then \(e^{-\mu x}\) back. The distance in the exponent is the one-way distance for each leg, so for there and back with the same tissue you may combine them as \(e^{-\mu \times 2d}\). The usual lost mark is using \(d\) instead of \(2d\).
:::

## X-rays: how they are produced

X-rays are electromagnetic waves of very short wavelength, about \(10^{-11}\,\mathrm{m}\) for diagnostic use, so each photon carries a large energy (tens of keV). They are produced when fast electrons are suddenly stopped by a metal target.

:::html
<figure class="fig"><svg viewBox="70 58 420 242" role="img" aria-label="An X-ray tube. Inside an evacuated glass tube a heated filament in a cup at the left gives off electrons that are accelerated to the right by a high voltage towards a slanted tungsten target in an anode block. An X-ray beam leaves downward through the glass. A high voltage supply joins the cathode and anode below."><rect class="fm s-mute sw1" x="120" y="90" width="320" height="110" rx="30"/><path class="f2 s-ink sw2" d="M310 100H420V190H350Z"/><path class="ln" d="M178 118H158V172H178"/><path class="ln thick" d="M165 128L172 138L162 148L172 158L165 165"/><path class="ln" d="M158 145H90V272H262M420 145H470V272H272"/><path class="ln" d="M272 262V282"/><path class="ln thick" d="M262 266V278"/><path class="c1" d="M186 130H316" marker-end="url(#ah-phys)"/><path class="c1" d="M186 145H324" marker-end="url(#ah-phys)"/><path class="c1" d="M186 160H331" marker-end="url(#ah-phys)"/><path class="c2" d="M332 150V250" marker-end="url(#ah2-phys)"/><path class="ln-m thin" d="M160 86V116M365 86V98"/><text class="tl tc" x="160" y="78">filament (cathode)</text><text class="tl tc" x="365" y="78">tungsten target (anode)</text><text class="tl tc" x="250" y="122">electrons</text><text class="tl tc" x="230" y="222">evacuated glass tube</text><text class="tl" x="342" y="248">X-ray beam</text><text class="tl tc" x="267" y="254">high voltage</text></svg><figcaption>An X-ray tube. The filament is heated by its own low-voltage supply (not drawn), so it emits electrons. The high voltage between cathode and anode accelerates them to the target, which gives out the X-ray beam. Most of the energy becomes thermal energy in the target.</figcaption></figure>
:::

:::steps
1. **Electron source.** A low-voltage supply heats the filament (the cathode) until it is white hot. Electrons gain enough energy to escape from its surface, which is **thermionic emission**. A hotter filament releases more electrons each second, so the filament temperature controls the **tube current**.
2. **Acceleration.** A high p.d. \(V\), typically tens of kilovolts, between cathode and anode accelerates the electrons across the tube. An electron gains kinetic energy \(eV\). The tube is evacuated so that the electrons do not collide with air molecules on the way.
3. **Target.** The electrons strike a metal target, usually tungsten, set at an angle so the X-ray beam leaves through a window. Tungsten has a very high melting point, which matters because only about 1% of the electrons' energy becomes X-rays; the other 99% heats the target.
4. **Cooling.** The target is mounted on a thick copper block, often cooled by oil or water, and in many tubes the anode spins so the electron beam keeps hitting a fresh part of it.
:::

### The X-ray spectrum and the minimum wavelength

The X-rays emerge with a **continuous spectrum** of wavelengths. An electron that slows down in the field of a target atom gives out a photon (this is called "braking radiation"), and it can lose any part of its energy, so the photons have all energies from nearly zero up to the whole kinetic energy \(eV\). Superimposed on the continuous spectrum are a few sharp **characteristic lines**: an incoming electron knocks an inner electron out of a target atom, an outer electron falls into the gap, and the atom emits a photon with the energy difference between the two energy levels (see [Quantum physics](#phys.quantum)). The lines are at fixed wavelengths set by the target metal, not by the voltage.

:::html
<figure class="fig"><svg viewBox="40 18 470 262" role="img" aria-label="Intensity against wavelength for X-rays. A solid continuous curve for 80 kV starts at a minimum wavelength of 1.55 and has two tall characteristic spikes. A dashed curve for 120 kV starts at a smaller minimum wavelength of 1.04 and is higher everywhere."><path class="ax" d="M60 230H490M60 230V40"/><path class="c1 sw2" d="M184 230L186 227L190 221L195 214L201 208L208 202L215 196L223 191L231 188L240 184L250 182L260 180L271 178L282 177L293 177L305 177L317 177L330 177L343 177L357 178L370 179L384 180L399 180L414 181L429 182L444 183L460 184"/><path class="c2 sw2 dash" d="M143 230L145 217L150 197L155 176L162 157L170 141L178 130L187 121L197 115L207 112L219 110L230 110L242 111L255 113L268 115L282 118L296 121L311 124L326 127L341 130L357 133L373 137L390 140L407 143L424 146L442 148L460 151"/><path class="c1 sw2" d="M208 202V90M228 189V65"/><path class="ax" d="M143 230V234M184 230V234M220 230V234M300 230V234M380 230V234M460 230V234M60 230V234"/><text class="tl" x="68" y="38">intensity</text><text class="tl tc" x="218" y="55">characteristic lines</text><text class="tl" x="330" y="66">solid: 80 kV</text><text class="tl" x="330" y="84">dashed: 120 kV</text><text class="ts tc" x="60" y="249">0</text><text class="ts tc" x="143" y="249">1.04</text><text class="ts tc" x="184" y="249">1.55</text><text class="ts tc" x="220" y="249">2</text><text class="ts tc" x="300" y="249">3</text><text class="ts tc" x="380" y="249">4</text><text class="ts tc" x="460" y="249">5</text><text class="tl te" x="490" y="268">λ / 10⁻¹¹ m</text></svg><figcaption>X-ray spectra for two tube voltages (characteristic lines are drawn on the solid curve only). The minimum wavelengths, 1.55 × 10⁻¹¹ m at 80 kV and 1.04 × 10⁻¹¹ m at 120 kV, come from hc/λ = eV. A higher voltage shifts the cut-off to a shorter wavelength and raises the whole curve.</figcaption></figure>
:::

The sharp cut-off at the short-wavelength end is the key to the calculation. The most energetic photon is made when one electron gives **all** of its kinetic energy \(eV\) to one photon. A photon of energy \(hc/\lambda\) cannot have more than \(eV\), so there is a shortest wavelength.

:::proof The minimum wavelength of X-rays
An electron accelerated from rest through a p.d. \(V\) gains kinetic energy \(eV\).
The most energetic photon takes all of this energy, so \(E_{\max} = eV\).
A photon of wavelength \(\lambda\) has energy \(E = hc/\lambda\).
So the shortest wavelength is given by \(\dfrac{hc}{\lambda_{\min}} = eV\).
Rearranging, \(\lambda_{\min} = \dfrac{hc}{eV}\).
No photon has more energy than one electron has, so no wavelength is shorter than \(\lambda_{\min}\).
:::

:::formula Minimum wavelength
\[\lambda_{\min} = \frac{hc}{eV}\]
\(h\): Planck constant · \(c\): speed of light · \(e\): elementary charge · \(V\): accelerating p.d. of the tube. The maximum photon energy is \(eV\), which is \(V\) electronvolts.
:::

:::eg An X-ray tube works at 80 kV. Calculate the shortest wavelength of the X-rays and the energy of the most energetic photon in keV.
\[\lambda_{\min} = \frac{hc}{eV} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{1.60 \times 10^{-19} \times 80 \times 10^{3}}\] [C1]
\[\lambda_{\min} = 1.55 \times 10^{-11}\,\mathrm{m}\] [A1]
The most energetic photon has energy \(eV\), which is 80 keV. [B1]
:::

### Changing the voltage and the current

Two settings of the tube control different things.

- **Tube voltage \(V\).** Raising \(V\) gives each electron more energy, so \(\lambda_{\min}\) becomes shorter, the photons are more energetic and the beam is **more penetrating**. The total X-ray intensity also rises.
- **Tube current \(I\).** The current is the number of electrons per second hitting the target times \(e\). Raising it increases the number of photons per second, so the intensity is greater at every wavelength, but \(\lambda_{\min}\) is **unchanged**, because each electron still has \(eV\).

:::warn Which setting changes what
The minimum wavelength depends only on the accelerating p.d. A bigger tube current gives a more intense beam of the same wavelengths. Answers that say "a higher current gives shorter wavelengths" lose the mark.
:::

:::eg An X-ray tube runs at 80 kV with a tube current of 15 mA. How many electrons hit the target each second? What is the power supplied, how much leaves as X-rays and how much heats the target? Take 1% as the fraction that becomes X-rays.
Electrons per second: \(\dfrac{I}{e} = \dfrac{15 \times 10^{-3}}{1.60 \times 10^{-19}}\) [C1] \(= 9.4 \times 10^{16}\,\mathrm{s^{-1}}\). [A1]
Power supplied: \(P = IV = 15 \times 10^{-3} \times 80 \times 10^{3}\) [C1] \(= 1.2 \times 10^{3}\,\mathrm{W}\). Of this about 1% is X-rays (12 W) and the remaining 99% (about 1.2 kW) heats the target, which is why the cooling is needed. [A1]
:::

## X-ray imaging and contrast

An X-ray image is a **shadow picture**. The beam passes through the body and falls on a detector (traditionally photographic film, now usually an electronic detector). Each part of the body attenuates the beam by \(I = I_0 e^{-\mu x}\) with its own value of \(\mu\). Where the beam has passed through more attenuating material, less X-ray intensity reaches the detector.

The attenuation coefficient depends on the material and on the photon energy. It is larger for denser material and for atoms with a larger proton number, so **bone** (rich in calcium) has a much larger \(\mu\) than **soft tissue**, which is mainly light elements. And a higher-energy beam has a smaller \(\mu\) in every material, so it is more penetrating. On film, a region that receives more X-rays is blacker, so a dense bone appears pale against dark soft tissue.

:::def Contrast (X-ray imaging)
The difference in the degree of blackening (brightness) between different regions of an image. A large difference in the intensities reaching the detector gives a high contrast.
:::

The contrast between two paths through the body is the ratio of the intensities that emerge along them.

:::eg A beam crosses a limb 10 cm thick. Along path A the beam meets only soft tissue (\(\mu = 30\,\mathrm{m^{-1}}\)). Along path B it crosses 3.0 cm of bone (\(\mu = 150\,\mathrm{m^{-1}}\)) and 7.0 cm of soft tissue. Compare the intensities that emerge, taking these as typical values.
Path A: \(\dfrac{I_A}{I_0} = e^{-30 \times 0.100} = e^{-3.0}\) [C1] \(= 0.050\). [A1]
Path B: the exponents add, \(\mu x = 150 \times 0.030 + 30 \times 0.070 = 4.5 + 2.1 = 6.6\), so \(\dfrac{I_B}{I_0} = e^{-6.6}\) [C1] \(= 1.4 \times 10^{-3}\). [A1]
\[\frac{I_A}{I_B} = e^{6.6 - 3.0} = e^{3.6} \approx 37\] [A1]
About 37 times more intensity emerges through soft tissue than along the bone path: a high contrast, so the bone is clearly visible.
:::

Soft tissues have very similar values of \(\mu\), so an ordinary X-ray cannot separate one organ from another: the contrast is poor. There are three standard improvements.

- **Contrast media.** The patient swallows a **barium meal** (barium has a large proton number, so a large \(\mu\)) so the stomach and intestines show up clearly, or is injected with an iodine compound that fills blood vessels. The medium has a much larger attenuation coefficient than the surrounding tissue, so the organ shows as a sharp shape.
- **Choice of tube voltage.** A lower voltage gives a lower energy beam, where the \(\mu\) values of different tissues differ more, so the contrast improves. The price is a higher dose to the patient, because less of the beam gets through.
- **Reducing scattered radiation.** A lead grid between patient and detector blocks X-rays that have been scattered sideways, which would otherwise blur the dark and light regions together.

:::tip Contrast is not sharpness
Contrast is the difference in brightness between regions. **Sharpness** is how clearly the edges are drawn. A small X-ray source and a detector close to the patient give sharper edges, because the shadows have less blur. In an exam, read which one the question asks for.
:::

:::eg Spot the error: an echo from a boundary in soft tissue returns 52 μs after the pulse was sent. Calculate the depth of the boundary.
A student wrote this answer, using \(1540\,\mathrm{m\,s^{-1}}\) for the speed of sound in soft tissue.

Line 1: \(d = vt = 1540 \times 52 \times 10^{-6}\)
Line 2: \(d = 0.080\,\mathrm{m} = 8.0\,\mathrm{cm}\)

The formula in Line 1 is wrong: the pulse travels to the boundary and back, so \(vt\) is the **total** distance \(2d\), not the depth. [C0] **The depth is half of \(vt\), so the answer is twice as large as it should be.** [A0]

Correct working: \(d = \dfrac{vt}{2} = \dfrac{1540 \times 52 \times 10^{-6}}{2}\) [C1] \(= 0.040\,\mathrm{m} = 4.0\,\mathrm{cm}\). [A1]

Check: the pulse travels about 8 cm in 52 μs, which fits \(1540 \times 52 \times 10^{-6} = 0.080\,\mathrm{m}\), and half of it is the depth to the boundary.
:::

## CT scanning

An ordinary X-ray image squashes all the tissue along the beam into one flat picture, so structures lie on top of each other and soft tissue is hard to see. **Computed tomography (CT)** solves this by taking X-ray images of one thin slice from many angles and letting a computer rebuild the slice.

:::html
<figure class="fig"><svg viewBox="40 6 470 270" role="img" aria-label="A CT scanner. On the left, a ring with an X-ray tube at the top and a row of detectors at the bottom sends a fan beam through the body of a patient lying on a table. An arrow shows the tube and detectors rotating round the patient. An arrow to the right leads from the computer to a stack of 2D slices that form a 3D image."><circle class="fm s-mute sw1" cx="170" cy="140" r="110"/><circle class="fp s-mute sw1" cx="170" cy="140" r="76"/><rect class="fm2 s-ink sw1" x="112" y="183" width="116" height="8"/><ellipse class="f1 s-acc sw1" cx="170" cy="145" rx="52" ry="38"/><path class="ln-m thin" d="M170 58L205 226M170 58L135 226"/><circle class="f2 s-ink sw1" cx="205" cy="226" r="4"/><circle class="f2 s-ink sw1" cx="196" cy="229" r="4"/><circle class="f2 s-ink sw1" cx="188" cy="231" r="4"/><circle class="f2 s-ink sw1" cx="179" cy="233" r="4"/><circle class="f2 s-ink sw1" cx="170" cy="233" r="4"/><circle class="f2 s-ink sw1" cx="161" cy="233" r="4"/><circle class="f2 s-ink sw1" cx="152" cy="231" r="4"/><circle class="f2 s-ink sw1" cx="144" cy="229" r="4"/><circle class="f2 s-ink sw1" cx="135" cy="226" r="4"/><rect class="f2 s-ink sw2" x="157" y="36" width="26" height="22"/><text class="tl tc" x="170" y="22">X-ray tube</text><text class="tl tc" x="170" y="160">body</text><path class="ln-m thin" d="M80 247L131 229"/><text class="tl" x="50" y="262">detectors</text><path class="c3" d="M290 62Q322 140 290 218" marker-end="url(#ahr)"/><text class="tl" x="296" y="50">rotates</text><text class="tl tc" x="349" y="162">computer</text><path class="c1" d="M322 176H376" marker-end="url(#ah-phys)"/><path class="f1 s-acc sw1" d="M392 84H472L494 70H414Z"/><path class="f1 s-acc sw1" d="M392 109H472L494 95H414Z"/><path class="f1 s-acc sw1" d="M392 134H472L494 120H414Z"/><path class="f1 s-acc sw1" d="M392 159H472L494 145H414Z"/><path class="f1 s-acc sw1" d="M392 184H472L494 170H414Z"/><text class="tl tc" x="443" y="56">2D slices</text><text class="tl tc" x="443" y="216">stacked: 3D image</text></svg><figcaption>A CT scanner seen end-on. The tube and the row of detectors rotate together round the patient, so every thin slice is imaged from many angles. The computer builds a 2D image of the slice. The table then moves the patient along the axis and the next slice is scanned. The 2D slices are stacked into a 3D image.</figcaption></figure>
:::

:::steps
1. A narrow, fan-shaped X-ray beam passes through one thin slice of the patient. A row of detectors on the opposite side of the ring measures the intensity that emerges along every path of the fan.
2. The tube and the detectors rotate together round the patient, so that the same slice is imaged from many different angles. At each angle the detectors record how much each path through the slice attenuated the beam.
3. A computer combines all of these images (all the attenuation data from different angles) into a single **2D image of the slice**, in which each point has the attenuation of the tissue at that place.
4. The table moves the patient a small step along the axis, and the process is repeated for the next slice, and so on.
5. The computer combines the 2D images of the many slices into a **3D image** of the structure, which can be turned and cut at any plane.
:::

CT has clear advantages over a single X-ray image. Structures no longer overlap, because each point in a slice is located separately. The detectors are sensitive and the computer can show small differences in \(\mu\), so soft tissues such as the brain, liver and tumours are visible, and the 3D image can be viewed from any direction. The disadvantage is **dose**: a CT scan is made of many X-ray images, so the patient receives much more ionising radiation than from one ordinary X-ray. The scan is therefore used when the information is needed, not routinely.

## PET scanning

**Positron emission tomography (PET)** is different in kind from the techniques so far. Ultrasound and X-rays send radiation **into** the body from outside. In PET the radiation comes from **inside** the body, from radioactive nuclei that the patient has been given.

:::def Tracer
A substance containing radioactive nuclei that can be introduced into the body and is then absorbed by the tissue being studied.
:::

The most common PET tracer is fluorine-18 (half-life 110 minutes) attached to a molecule similar to glucose. Active tissue, such as the brain, the heart muscle and many tumours, uses glucose quickly, so it takes up more tracer than inactive tissue. The tracer therefore collects where the tissue is working hardest, and the aim is to image **where the tracer is** and so how much of it each tissue has taken up. Fluorine-18 decays by **β⁺ decay** (see [Particle physics](#phys.particles)):
\[\mathrm{^{18}_{\;9}F \;\rightarrow\; ^{18}_{\;8}O + ^{\;0}_{+1}e + \nu_e}\]
A proton in the nucleus changes into a neutron, emitting a **positron** (the antiparticle of the electron) and a neutrino.

### Annihilation

The positron travels only about a millimetre through the tissue, slowing down as it collides with atoms, and then meets an electron. A particle and its antiparticle cannot coexist: they **annihilate**.

:::def Annihilation
The interaction of a particle with its antiparticle in which their total mass is converted into energy, as photons. Mass–energy and momentum are conserved.
:::

When a positron and an electron, almost at rest, annihilate, the total energy is \(2m_ec^2\). It cannot become a single photon, because the momentum would not be conserved: before the collision the total momentum is about zero, and a single photon always carries momentum \(E/c\). **Two photons** travelling in opposite directions have equal and opposite momenta that add to zero. Equal momenta mean equal energies, since \(E = pc\) for a photon, so each photon carries \(m_ec^2\).

:::eg Calculate the energy, in joules and in MeV, of each photon from the annihilation of a stationary electron and positron. Use the data sheet value for the electron mass.
\[E = m_ec^2 = 9.11 \times 10^{-31} \times (3.00 \times 10^{8})^2\] [C1]
\[E = 8.20 \times 10^{-14}\,\mathrm{J}\] [A1]
In electronvolts: \(\dfrac{8.20 \times 10^{-14}}{1.60 \times 10^{-19}} = 5.12 \times 10^{5}\,\mathrm{eV} = 0.512\,\mathrm{MeV}\). [A1]
(The accepted value, found with more precise constants, is 0.511 MeV: the slight difference comes from rounding the data sheet values. Use the data sheet figures in calculations.) The wavelength \(hc/E\) is \(2.43 \times 10^{-12}\,\mathrm{m}\), in the gamma-ray region.
:::

:::eg Show that the two photons from the annihilation of a stationary electron and positron must travel in opposite directions.
The momentum of each photon is \(p = E/c = m_ec = 9.11 \times 10^{-31} \times 3.00 \times 10^{8} = 2.73 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}\). [C1] [A1]
Before the annihilation the positron and electron are almost at rest, so the total momentum is almost zero. [B1]
Momentum is conserved and is a vector, so the two photons must have momenta of equal size in opposite directions, adding to zero. [B1]
:::

:::warn Each photon, not both together
The total energy released is \(2m_ec^2\) (1.02 MeV), but it is shared between **two** photons. Each photon has \(m_ec^2\), which is 0.512 MeV with data sheet values. In exam answers, always say "each".
:::

### Detecting the photons and building the image

The gamma photons have so much energy that they pass out of the body easily, and a **ring of detectors** around the patient picks them up. Each detector registers when a photon arrives. Two photons detected at almost the same instant on opposite sides of the ring must have come from the same annihilation, which therefore took place somewhere on the line between the two detectors.

:::html
<figure class="fig"><svg viewBox="0 10 520 280" role="img" aria-label="A PET scan. A ring of twenty-four detectors surrounds a circular cross-section of the patient. An annihilation event inside the body, a little left of centre, sends two gamma photons along a line in opposite directions to two highlighted detectors on opposite sides of the ring."><circle class="fm s-mute sw1" cx="280" cy="150" r="80"/><circle class="f2 s-ink sw1" cx="400" cy="150" r="7"/><circle class="f2 s-ink sw1" cx="396" cy="181" r="7"/><circle class="f3 s-red sw1" cx="384" cy="210" r="7"/><circle class="f2 s-ink sw1" cx="365" cy="235" r="7"/><circle class="f2 s-ink sw1" cx="340" cy="254" r="7"/><circle class="f2 s-ink sw1" cx="311" cy="266" r="7"/><circle class="f2 s-ink sw1" cx="280" cy="270" r="7"/><circle class="f2 s-ink sw1" cx="249" cy="266" r="7"/><circle class="f2 s-ink sw1" cx="220" cy="254" r="7"/><circle class="f2 s-ink sw1" cx="195" cy="235" r="7"/><circle class="f2 s-ink sw1" cx="176" cy="210" r="7"/><circle class="f2 s-ink sw1" cx="164" cy="181" r="7"/><circle class="f2 s-ink sw1" cx="160" cy="150" r="7"/><circle class="f2 s-ink sw1" cx="164" cy="119" r="7"/><circle class="f3 s-red sw1" cx="176" cy="90" r="7"/><circle class="f2 s-ink sw1" cx="195" cy="65" r="7"/><circle class="f2 s-ink sw1" cx="220" cy="46" r="7"/><circle class="f2 s-ink sw1" cx="249" cy="34" r="7"/><circle class="f2 s-ink sw1" cx="280" cy="30" r="7"/><circle class="f2 s-ink sw1" cx="311" cy="34" r="7"/><circle class="f2 s-ink sw1" cx="340" cy="46" r="7"/><circle class="f2 s-ink sw1" cx="365" cy="65" r="7"/><circle class="f2 s-ink sw1" cx="384" cy="90" r="7"/><circle class="f2 s-ink sw1" cx="396" cy="119" r="7"/><path class="c1" d="M246 131L375 205" marker-end="url(#ah-phys)"/><path class="c1" d="M236 124L186 95" marker-end="url(#ah-phys)"/><circle class="fi" cx="241" cy="127" r="4"/><text class="tl ta" x="300" y="152">γ</text><text class="tl ta" x="203" y="95">γ</text><text class="tl" x="20" y="215">annihilation event</text><path class="ln-m thin" d="M100 200L237 130"/><text class="tl tc" x="280" y="208">patient</text><text class="tl" x="420" y="44">detector ring</text><path class="ln-m thin" d="M412 48L372 62"/></svg><figcaption>A PET ring seen end-on. The positron annihilates close to where it was emitted, a little left of centre, and the two photons leave in opposite directions. The two highlighted detectors register them. The photon that has the shorter path (towards the upper left) arrives first.</figcaption></figure>
:::

The scanner can do better than "somewhere on the line". It records the **arrival time** of each photon with great accuracy. If the annihilation is exactly at the centre of the ring, both photons travel the same distance and arrive together. If it is at a distance \(x\) from the middle, one photon has \(x\) less to travel and the other \(x\) more, so the path difference is \(2x\) and the arrival times differ by \(\Delta t = 2x/c\).

:::formula Position along the line from the arrival times
\[x = \frac{c\,\Delta t}{2}\]
\(x\): distance of the annihilation from the midpoint of the line between the two detectors (m) · \(\Delta t\): difference between the arrival times of the two photons (s) · \(c\): speed of light. The photon that arrives first came from the half of the line nearer to its detector.
:::

:::eg Two annihilation photons are detected 0.30 ns apart. How far from the midpoint of the line joining the detectors did the annihilation take place?
\[x = \frac{c\,\Delta t}{2} = \frac{3.00 \times 10^{8} \times 0.30 \times 10^{-9}}{2}\] [C1]
\[x = 4.5 \times 10^{-2}\,\mathrm{m} = 4.5\,\mathrm{cm}\] [A1] on the side of the detector that received its photon first.
:::

The computer collects many thousands of such events. Each one marks a point on a line, and the places where many lines cross are the places where the tracer is concentrated. The result is an image of the **tracer concentration** in the tissue: bright where a lot of tracer decayed, dim where little did. A PET scan shows how tissue is working, which a CT image of the same region cannot show. The two scans are often combined.

### Why the half-life must be short

Fluorine-18 has a half-life of 110 minutes (6600 s). A short half-life matters in two ways. The tracer must give enough decays during the scan to build an image, so it cannot be too long-lived, and it must not stay radioactive in the patient for days, so the dose is limited. But it cannot be too short either, because the tracer is made in a cyclotron and must be delivered to the hospital and injected. A half-life of about two hours balances these needs.

:::eg A patient is injected with a fluorine-18 tracer of activity 370 MBq. Calculate the decay constant of fluorine-18 and the activity 4.0 hours later. (Half-life of fluorine-18: 110 minutes.)
\[\lambda = \frac{0.693}{t_{1/2}} = \frac{0.693}{110 \times 60} = 1.05 \times 10^{-4}\,\mathrm{s^{-1}}\] [C1]
\[A = A_0e^{-\lambda t} = 370\,e^{-0.693 \times 240/110}\] [C1] \(= 82\,\mathrm{MBq}\). [A1]
Using \(t = 4.0 \times 60 = 240\) minutes in the same unit as the half-life gives the same exponent as using seconds. After 4.0 hours 22% of the activity is left.
:::

### Choosing the technique

| | Ultrasound | X-ray | CT | PET |
|---|---|---|---|---|
| Radiation | sound pulses, not ionising | X-rays, ionising | many X-ray images, ionising | gamma rays from a tracer, ionising |
| What it shows | boundaries between soft tissues, in 2D | shadow of dense structures such as bone | 3D structure with soft tissue detail | how active the tissue is |
| Dose | none | low | higher | moderate |

:::board
AQA teaches medical physics as one of its optional topics, so only some AQA students study it. In Cambridge 9702 it is compulsory A Level content, examined like every other topic. The physics is the same wherever it is taught; Cambridge needs only what is here.
:::

:::eg Spot the error: a student states that each photon from the annihilation of a stationary electron and positron has energy \(2m_ec^2\). Find the line that is wrong.
The student wrote: "The total mass converted is \(2m_e\), so the energy released is \(2m_ec^2\) = \(2 \times 8.20 \times 10^{-14} = 1.64 \times 10^{-13}\,\mathrm{J}\). This is the energy of the photon."

The total energy released is indeed \(2m_ec^2 = 1.64 \times 10^{-13}\,\mathrm{J}\). [C1] **The error is the last sentence: there are two photons, and the energy is shared equally between them, so each photon has \(m_ec^2 = 8.20 \times 10^{-14}\,\mathrm{J}\).** [A0]

Correct: two photons are needed to conserve momentum, with equal and opposite momenta and so equal energies, each \(8.20 \times 10^{-14}\,\mathrm{J}\) (0.512 MeV). [A1]
:::

:::try Start easy, finish at exam standard
Q: Ultrasound of frequency 2.5 MHz travels in soft tissue at \(1540\,\mathrm{m\,s^{-1}}\). Find its wavelength.
A: \(\lambda = v/f = 1540/(2.5 \times 10^{6}) = 6.2 \times 10^{-4}\,\mathrm{m}\), about 0.62 mm.
Q: An echo returns from a boundary 80 μs after the pulse. Find the depth in soft tissue (\(1540\,\mathrm{m\,s^{-1}}\)).
A: \(d = vt/2 = 1540 \times 80 \times 10^{-6}/2 = 0.062\,\mathrm{m}\), about 6.2 cm.
Q: Water has density \(1000\,\mathrm{kg\,m^{-3}}\) and the speed of sound in it is \(1480\,\mathrm{m\,s^{-1}}\). Find its acoustic impedance, with the unit.
A: \(Z = \rho c = 1000 \times 1480 = 1.48 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\).
Q: A boundary separates two media with \(Z_1 = 1.60 \times 10^{6}\) and \(Z_2 = 1.70 \times 10^{6}\) (both in \(\mathrm{kg\,m^{-2}\,s^{-1}}\)). Find the intensity reflection coefficient.
A: \(\dfrac{(1.60 - 1.70)^2}{(1.60 + 1.70)^2} = \dfrac{0.0100}{10.89} = 9.2 \times 10^{-4}\). Almost nothing is reflected, because the two impedances are almost equal.
Q: An X-ray beam passes through 5.0 cm of soft tissue (\(\mu = 30\,\mathrm{m^{-1}}\)). What fraction of the intensity is transmitted?
A: \(I/I_0 = e^{-30 \times 0.050} = e^{-1.5} = 0.22\), so 22%.
Q: Find the shortest X-ray wavelength produced by a tube at 50 kV.
A: \(\lambda_{\min} = \dfrac{hc}{eV} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{1.60 \times 10^{-19} \times 50 \times 10^{3}} = 2.5 \times 10^{-11}\,\mathrm{m}\).
Q: What fraction of a fluorine-18 tracer is left after 330 minutes (half-life 110 minutes)?
A: 330 minutes is 3 half-lives, so the fraction is \((\tfrac12)^3 = \tfrac18 = 0.125\), or 12.5%.
Q: Explain why a PET scanner counts only photons that arrive at two detectors at almost the same time.
A: Two photons from the same annihilation leave in opposite directions at the speed of light, so they reach opposite detectors almost together. A single photon, or two arriving at different times, comes from different events or from scattering, so it cannot be used to place an annihilation on a line.
Q: State what happens to the minimum wavelength of an X-ray tube if (a) the tube voltage is doubled, (b) the tube current is doubled.
A: (a) \(\lambda_{\min} = hc/eV\), so it halves. (b) It is unchanged. A larger current only means more photons per second.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define the specific acoustic impedance of a medium.
A: The product of the density of the medium and the speed of sound in the medium. [B1]
Q: [3 marks] (#phys.quantum) ★ An X-ray tube operates at 65 kV. Calculate (a) the minimum wavelength of the X-rays, (b) the maximum energy of an X-ray photon in eV.
A: (a) \(\lambda_{\min} = \dfrac{hc}{eV} = \dfrac{6.63 \times 10^{-34} \times 3.00 \times 10^{8}}{1.60 \times 10^{-19} \times 65 \times 10^{3}}\) [C1] \(= 1.9 \times 10^{-11}\,\mathrm{m}\). [A1] (b) The maximum photon energy equals the kinetic energy of one electron, \(eV\), which is \(6.5 \times 10^{4}\,\mathrm{eV}\). [B1]
Q: [4 marks] ★★ Explain how a piezoelectric transducer is used to generate pulses of ultrasound and to detect their echoes.
A: A crystal changes shape when a p.d. is applied across it. [B1] An alternating p.d. at the crystal's resonant frequency makes it vibrate with a large amplitude and send out ultrasound. [B1] The returning echoes squeeze the crystal and, because it generates an e.m.f. when its shape changes, the crystal produces an alternating p.d. at the echo's frequency. [B1] The same crystal is used for both jobs, because the pulse lasts only a microsecond and a backing block damps the vibrations so the crystal is ready to detect the echo. [B1]
Q: [4 marks] ★★ The acoustic impedance of air is \(4.3 \times 10^{2}\,\mathrm{kg\,m^{-2}\,s^{-1}}\) and that of skin is \(1.7 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\). (a) Calculate the intensity reflection coefficient for a boundary between air and skin. (b) Explain why a gel is used between the probe and the skin.
A: (a) \(\dfrac{I_R}{I_0} = \dfrac{(1.7 \times 10^{6} - 4.3 \times 10^{2})^2}{(1.7 \times 10^{6} + 4.3 \times 10^{2})^2}\) [C1] \(= 0.999\). [A1] (b) The gel fills the air gap, so the ultrasound passes from the probe through a medium of acoustic impedance close to that of skin. [B1] The reflection coefficient is then very small, so almost all of the intensity enters the body instead of being reflected at the surface. [B1]
Q: [3 marks] ★★ (a) State what is meant by the contrast of an X-ray image. (b) Explain how a barium meal improves the contrast of an image of the digestive system.
A: (a) The difference in the degree of blackening (brightness) between different regions of the image. [B1] (b) Barium has a large attenuation coefficient (it absorbs X-rays strongly), much greater than that of the surrounding soft tissue. [B1] So less intensity reaches the detector behind the digestive system than behind the tissue around it, which makes the difference in blackening, and so the contrast, greater. [B1]
Q: [4 marks] ★★ An X-ray beam crosses an arm 6.0 cm thick. Path A passes through soft tissue only (\(\mu = 30\,\mathrm{m^{-1}}\)). Path B passes through 2.0 cm of bone (\(\mu = 150\,\mathrm{m^{-1}}\)) and 4.0 cm of soft tissue. (a) Calculate \(I/I_0\) for each path. (b) Calculate \(I_A/I_B\) and comment on the contrast.
A: (a) \(\dfrac{I_A}{I_0} = e^{-30 \times 0.060}\) [C1] \(= 0.17\). [A1] \(\dfrac{I_B}{I_0} = e^{-(150 \times 0.020 + 30 \times 0.040)} = e^{-4.2} = 0.015\). [A1] (b) \(\dfrac{I_A}{I_B} = e^{2.4} = 11\), a high contrast, so the bone shows clearly. [A1]
Q: [4 marks] ★★ Describe how a CT scan produces a 3D image of an organ.
A: A thin, fan-shaped X-ray beam passes through one slice of the body, and a ring of detectors on the other side records the transmitted intensity. [B1] The tube and detectors rotate round the patient so the slice is imaged from many angles. [B1] A computer combines these images into a 2D image of the slice. [B1] The patient is moved along the axis and the process is repeated, and the computer combines the 2D images of many slices into a 3D image. [B1]
Q: [5 marks] (#phys.nuclear) ★★★ A PET scan uses a tracer that decays by β⁺ decay. (a) Calculate the energy of each photon produced when a stationary positron and a stationary electron annihilate. (b) Explain, using conservation of momentum, why two photons are produced and why they leave in opposite directions with equal energies.
H: The energy released is the mass of both particles converted to energy, \(2m_ec^2\).
H: A photon has momentum \(E/c\).
A: (a) The energy of each photon is \(m_ec^2 = 9.11 \times 10^{-31} \times (3.00 \times 10^{8})^2\) [C1] \(= 8.20 \times 10^{-14}\,\mathrm{J}\) (0.512 MeV). [A1] (b) Before the annihilation the total momentum is zero (the particles are at rest). [B1] A single photon always has momentum \(E/c\), so one photon would leave non-zero momentum: two photons are needed, with momenta of equal size in opposite directions. [B1] Equal momenta mean equal energies, because \(E = pc\) for each photon. [B1]
Q: [7 marks] ★★★ A pulse of ultrasound of intensity \(5.0 \times 10^{2}\,\mathrm{W\,m^{-2}}\) enters soft tissue (\(\mu = 35\,\mathrm{m^{-1}}\)) and travels 5.0 cm to a boundary with bone. Use acoustic impedances of \(1.63 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\) for tissue and \(7.60 \times 10^{6}\,\mathrm{kg\,m^{-2}\,s^{-1}}\) for bone, and assume no intensity is lost when the pulse enters the tissue. Calculate (a) the intensity reflection coefficient at the boundary, (b) the intensity of the pulse when it arrives at the boundary, (c) the intensity of the reflected pulse just after reflection, (d) the intensity of the echo when it returns to the surface.
H: Attenuation happens over the 5.0 cm in each direction; the reflection coefficient is a ratio of intensities.
H: For (d) start from your answer to (c) and attenuate over the same 5.0 cm again.
A: (a) \(\dfrac{I_R}{I_0} = \dfrac{(7.60 - 1.63)^2}{(7.60 + 1.63)^2}\) [C1] \(= 0.418\). [A1] (b) \(I = 5.0 \times 10^{2}\,e^{-35 \times 0.050}\) [C1] \(= 87\,\mathrm{W\,m^{-2}}\). [A1] (c) \(0.418 \times 87 = 36\,\mathrm{W\,m^{-2}}\). [A1] (d) \(I = 36\,e^{-35 \times 0.050}\) [C1] \(= 6.3\,\mathrm{W\,m^{-2}}\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ An X-ray beam of a typical diagnostic quality has attenuation coefficients of \(30\,\mathrm{m^{-1}}\) in soft tissue and \(2700\,\mathrm{m^{-1}}\) in lead. (a) Calculate the half-value thickness of each. (b) Calculate the fraction of the intensity transmitted by a 1.0 mm lead sheet. (c) Calculate the thickness of lead that reduces the intensity to 1.0% of its initial value.
H: Half-value thickness is \(0.693/\mu\).
H: For (c) take natural logs: \(I/I_0 = 0.010 = e^{-\mu x}\), so \(x = \ln(100)/\mu\).
A: (a) \(x_{1/2} = 0.693/\mu\): tissue \(0.693/30\) [C1] \(= 2.3 \times 10^{-2}\,\mathrm{m}\) (2.3 cm), [A1] lead \(0.693/2700 = 2.6 \times 10^{-4}\,\mathrm{m}\) (0.26 mm). [A1] The lead is about 90 times thinner for the same effect. (b) \(\dfrac{I}{I_0} = e^{-2700 \times 1.0 \times 10^{-3}}\) [C1] \(= e^{-2.7} = 0.067\), about 6.7%. [A1] (c) \(x = \dfrac{\ln 100}{2700}\) [C1] \(= 1.7 \times 10^{-3}\,\mathrm{m} = 1.7\,\mathrm{mm}\). [A1]
Q: [5 marks] ★★★ In a PET scanner the two detectors of a pair record photons from one annihilation 1.2 ns apart. (a) Calculate how far from the midpoint of the line between the detectors the annihilation took place, and say on which side. (b) The timing of each detector is uncertain by 0.20 ns, so the arrival time difference is uncertain by 0.20 ns. Calculate the uncertainty in the position along the line. (c) The positron travels about 1 mm before it annihilates. Explain why this limits the sharpness of a PET image whatever the timing accuracy.
H: Path difference \(= 2x\), time difference \(= 2x/c\).
A: (a) \(x = \dfrac{c\,\Delta t}{2} = \dfrac{3.00 \times 10^{8} \times 1.2 \times 10^{-9}}{2}\) [C1] \(= 0.18\,\mathrm{m}\), on the side of the detector that received its photon first. [A1] (b) \(\delta x = \dfrac{c\,\delta(\Delta t)}{2} = \dfrac{3.00 \times 10^{8} \times 0.20 \times 10^{-9}}{2}\) [C1] \(= 0.030\,\mathrm{m} = 3.0\,\mathrm{cm}\). [A1] (c) The scanner finds where the positron annihilated, not where the nucleus decayed, so the image of the tracer is blurred by about a millimetre. [B1]
:::

:::quiz
? What does a piezoelectric crystal do?
+ It changes shape when a p.d. is applied and generates an e.m.f. when its shape changes.
- It changes shape when a p.d. is applied but cannot generate an e.m.f.
- It generates an e.m.f. when heated and changes shape when cooled.
- It emits X-rays when its shape changes.
> Both halves of the effect are needed: the first sends the ultrasound and the second detects the echo. The other options mix up the piezoelectric effect with thermal or other effects.
? An echo returns 40 μs after a pulse in soft tissue (\(1540\,\mathrm{m\,s^{-1}}\)). How deep is the boundary?
- 6.2 cm
+ 3.1 cm
- 1.5 cm
- 12 cm
> The pulse travels there and back, so \(d = vt/2 = 1540 \times 40 \times 10^{-6}/2 = 0.031\,\mathrm{m}\). 6.2 cm uses \(d = vt\), and the other two come from dividing or multiplying again by 2.
? Why is a gel used between an ultrasound probe and the skin?
+ Air has a very different acoustic impedance from tissue, so without the gel almost all the ultrasound would be reflected at the skin.
- The gel cools the crystal so that it does not overheat.
- The gel increases the speed of the ultrasound in tissue.
- The gel amplifies the echoes before they reach the crystal.
> The gel has an impedance close to that of skin and removes the air gap. It does not change the speed of the ultrasound in tissue and does not amplify anything.
? The accelerating p.d. of an X-ray tube is doubled and the current is kept the same. What happens to the minimum wavelength?
- It is doubled.
- It is unchanged.
+ It is halved.
- It is reduced to a quarter.
> \(\lambda_{\min} = hc/eV\), so it is inversely proportional to \(V\). Doubling \(V\) halves \(\lambda_{\min}\). The current affects only how many photons are produced.
? Which change makes the beam from an X-ray tube more intense but leaves the minimum wavelength unchanged?
+ Increasing the tube current
- Increasing the accelerating p.d.
- Using a target with a higher melting point
- Moving the detector closer to the target
> A larger current means more electrons hit the target each second, and so more photons per second. Each electron still has energy \(eV\), so \(\lambda_{\min}\) does not change.
? What is the advantage of a CT scan compared with a single X-ray image?
- It uses no ionising radiation.
- It is cheaper and quicker.
+ It combines many images of a slice from different angles, so overlapping structures can be separated and a 3D image built.
- It uses a tracer that collects in active tissue.
> CT uses many X-ray images, so the dose is higher, not lower. The tracer is the technique of PET.
? What is the energy of each photon produced when a stationary electron and positron annihilate?
+ About 0.51 MeV
- About 1.02 MeV
- About 0.26 MeV
- It depends on how fast the positron was emitted from the nucleus.
> Each of the two photons has \(m_ec^2\) = 0.51 MeV. 1.02 MeV is the total energy, shared between two photons. The positron slows down in the tissue before it annihilates, so its emission speed does not matter.
:::

:::checklist What you can now do
- [ ] I can describe how a piezoelectric transducer generates and detects ultrasound.
- [ ] I can use \(d = vt/2\) and explain A-scans and B-scans.
- [ ] I can define acoustic impedance and use \(Z = \rho c\) and \(I_R/I_0 = (Z_1 - Z_2)^2/(Z_1 + Z_2)^2\), including why a gel is used.
- [ ] I can use \(I = I_0e^{-\mu x}\) for ultrasound and X-rays, including the half-value thickness and echo intensities.
- [ ] I can explain how X-rays are produced, and calculate \(\lambda_{\min}\) from the accelerating p.d.
- [ ] I can explain contrast in X-ray imaging and how it can be improved.
- [ ] I can describe how CT builds a 2D and then a 3D image.
- [ ] I can explain how PET works: tracer, β⁺ decay, annihilation, the photon energy, the detectors and the arrival times.
:::

:::recap
- Ultrasound is above 20 kHz (medical: 1–15 MHz). A piezoelectric crystal changes shape when a p.d. is applied and generates an e.m.f. when its shape changes, so one crystal sends pulses and detects echoes. A backing block damps it to keep the pulses short.
- Echo depth: \(d = vt/2\), because the pulse goes there and back. A-scan: amplitude against time. B-scan: many A-scans shown as brightness dots build a 2D image.
- Specific acoustic impedance \(Z = \rho c\). \(I_R/I_0 = (Z_1 - Z_2)^2/(Z_1 + Z_2)^2\), for intensity. Air–skin reflects almost everything, so a gel is used. Tissue–bone reflects a lot.
- Attenuation \(I = I_0e^{-\mu x}\), for ultrasound and X-rays, with half-value thickness \(x_{1/2} = 0.693/\mu\). An echo is attenuated on the way there and the way back, and reflected once.
- X-rays: electrons from a hot filament are accelerated through \(V\) onto a tungsten target; about 1% of the energy becomes X-rays, the rest heats the target. \(\lambda_{\min} = hc/eV\). Raising \(V\) gives shorter wavelengths and a more penetrating beam; raising the current gives more photons, with the same \(\lambda_{\min}\).
- Contrast is the difference in blackening between regions. Bone has a much larger \(\mu\) than soft tissue; contrast media such as barium and iodine have large \(\mu\) too.
- CT: many X-ray images of a thin slice from different angles are combined by a computer into a 2D image; the table moves and the 2D images are stacked into a 3D image. More detail, higher dose.
- PET: a tracer containing a β⁺ emitter (for example fluorine-18, half-life 110 minutes) goes to active tissue. The positron annihilates with an electron into two photons of \(m_ec^2\) (0.512 MeV with data sheet values) in opposite directions, conserving energy and momentum. Detectors in a ring and the arrival time difference (\(x = c\Delta t/2\)) build an image of the tracer concentration.
:::

:::links
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions on medical physics [unofficial]
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the medical physics questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Astronomy and cosmology](#phys.astro)
