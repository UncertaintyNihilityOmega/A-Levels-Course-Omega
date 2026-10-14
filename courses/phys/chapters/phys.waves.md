@chapter phys.waves
@title Waves
@level as
@paper CAIE P1 · P2 (AS)
@time 7–9 hours
@summary How waves carry energy without carrying matter: the words and graphs used to describe a wave, the wave equation, oscilloscope readings, intensity, transverse and longitudinal waves, the Doppler effect for sound, the electromagnetic spectrum, and polarisation with Malus's law.

:::why
Almost everything you see, hear and send to a phone is a wave. Light, sound, radio, Wi-Fi, X-rays and the ripples on a pond all follow the same few rules, so one set of ideas (wavelength, frequency, speed, amplitude, intensity) lets you handle all of them. This chapter is the vocabulary and the toolkit for [Superposition](#phys.superposition), where waves meet and produce interference patterns, and for [Quantum physics](#phys.quantum), where light turns out to behave as particles as well.
:::

**Before you start**, you need speed from [Kinematics](#phys.kinematics), unit prefixes from [Physical quantities, units and uncertainty](#phys.units), and power from [Work, energy and power](#phys.energy). Sine curves are drawn here, so [Trigonometry](#math.p1.trig) helps, but every curve is explained as it appears. You also need the order of colours in the visible spectrum from IGCSE: red, orange, yellow, green, blue, indigo, violet.

:::try Warm-up
Q: A cyclist travels 45 m in 3.0 s at constant speed. What is the speed? (from [Kinematics](#phys.kinematics))
A: \(v = \dfrac{s}{t} = \dfrac{45}{3.0} = 15\,\mathrm{m\,s^{-1}}\).
Q: Write a wavelength of 650 nm in metres, in standard form. (from [Physical quantities, units and uncertainty](#phys.units))
A: \(1\,\mathrm{nm} = 10^{-9}\,\mathrm{m}\), so \(650\,\mathrm{nm} = 6.50 \times 10^{-7}\,\mathrm{m}\).
Q: A 60 W lamp is switched on for 2.0 minutes. How much energy does it transfer? (from [Work, energy and power](#phys.energy))
A: \(E = Pt = 60 \times 120 = 7200\,\mathrm{J} = 7.2\,\mathrm{kJ}\). Change minutes into seconds first.
:::

## What a wave is

Drop a stone in a pond and a ring of ripples spreads out. A cork floating on the water does not travel with the ripples: it bobs up and down on the spot as each ripple passes. The ripples carry **energy** across the pond, but the water, and the cork, stay roughly where they were. That is the central idea of this chapter.

:::def Progressive wave
A wave that transfers energy from one place to another.
:::

A wave begins when a **source** makes something oscillate. The oscillation is passed from each particle of the **medium** (rope, spring, water, air) to its neighbour, because neighbouring particles are linked by forces. Each particle repeats the motion of the one before it, a little later. Energy moves along the medium, but each particle only oscillates about its own **equilibrium position**.

Three standard demonstrations show this:

- **A long rope.** Hold one end and move your hand up and down. A wave moves along the rope, but a ribbon tied to the rope just moves up and down.
- **A long soft spring (a "slinky").** Push and pull one end along the length of the spring. Bunched-up coils (compressions) travel along it, while each coil moves forwards and backwards over a short distance.
- **A ripple tank.** A shallow tray of water has a motor-driven bar or a small dipper that touches the surface. A lamp above the tank casts a shadow pattern of the wave crests onto a white screen below, and a stroboscope (or a camera) makes the moving pattern look still.

In a ripple tank you describe waves using **wavefronts** and **rays**. A wavefront is a line joining points that are at the same stage of their oscillation, such as the crests. A ray is a line showing the direction in which the wave travels, and it is always at right angles to the wavefronts.

:::html
<figure class="fig"><svg viewBox="0 0 560 196" role="img" aria-label="Two ripple tank patterns. Left: a straight bar vibrating at the left produces straight parallel wavefronts with parallel rays pointing right at right angles to them. Right: a small dipper produces circular wavefronts with rays pointing outwards along the radii."><path class="ln thick" d="M30 20V160"/><path class="ln" d="M70 20V160M110 20V160M150 20V160M190 20V160"/><path class="c1" d="M40 50H228" marker-end="url(#ah-phys)"/><path class="c1" d="M40 90H228" marker-end="url(#ah-phys)"/><path class="c1" d="M40 130H228" marker-end="url(#ah-phys)"/><path class="c1" d="M130 172H112" marker-end="url(#ah-phys)"/><path class="c1" d="M130 172H148" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="130" y="166">λ</text><text class="tl tc" x="130" y="192">plane waves</text><circle class="ln thin" cx="400" cy="88" r="18"/><circle class="ln" cx="400" cy="88" r="36"/><circle class="ln" cx="400" cy="88" r="54"/><circle class="ln" cx="400" cy="88" r="72"/><circle class="fi" cx="400" cy="88" r="4"/><path class="c1" d="M406 88H484" marker-end="url(#ah-phys)"/><path class="c1" d="M394 88H316" marker-end="url(#ah-phys)"/><path class="c1" d="M400 82V4" marker-end="url(#ah-phys)"/><path class="c1" d="M400 94V172" marker-end="url(#ah-phys)"/><path class="c1" d="M404 84L455 33" marker-end="url(#ah-phys)"/><path class="c1" d="M396 84L345 33" marker-end="url(#ah-phys)"/><path class="c1" d="M404 92L455 143" marker-end="url(#ah-phys)"/><path class="c1" d="M396 92L345 143" marker-end="url(#ah-phys)"/><text class="tl tc" x="400" y="192">circular waves</text></svg><figcaption>Wavefronts (the straight lines and circles) are drawn at one instant, one wavelength apart. Rays (arrows) show the direction of travel and always cross wavefronts at right angles. The bar produces plane waves, the small dipper produces circular waves.</figcaption></figure>
:::

:::lab Seeing a wave in a ripple tank
:::steps
1. Fill the tank with about 5 mm of water and level it. Place the lamp above the tank and a white screen below it.
2. Lower the bar (or the dipper) so that it just touches the water, then switch on the motor. A pattern of bright and dark lines appears on the screen.
3. Freeze the pattern with the stroboscope. Count the number of wavefronts between two marked points on the screen and divide the length by the number of wavelengths to find \(\lambda\).
4. Measure the frequency from the motor setting, or by counting the strobe flashes per second at which the pattern looks still. Then use \(v = f\lambda\) (derived below) to find the wave speed.
:::
:::

## Describing a wave

Waves are described with a small set of terms. Learn the exact wording, because "define" questions give a mark for each correct phrase.

:::def Displacement (of a wave)
The distance of a point on the wave from its equilibrium position, in a stated direction.
:::

:::def Amplitude
The maximum displacement of a point on the wave from its equilibrium position.
:::

:::def Wavelength
The distance between two adjacent points on a wave that are in phase (for example, two adjacent crests).
:::

:::def Period
The time taken for one complete oscillation of a point on the wave.
:::

:::def Frequency
The number of complete oscillations per unit time. One oscillation per second is 1 hertz (Hz).
:::

:::def Wave speed
The distance travelled by the wave energy (the wavefront) per unit time.
:::

:::def Phase difference
The fraction of a cycle by which one oscillation leads or lags another, expressed in degrees or radians.
:::

Displacement and amplitude have the same unit as the quantity that oscillates: metres for a rope, pascals for the pressure variation in a sound wave. The period and frequency are linked by

:::formula Period and frequency
\[f = \frac{1}{T}\]
\(f\): frequency (Hz) · \(T\): period (s). A source of frequency 50 Hz has \(T = 1/50 = 0.020\,\mathrm{s}\), and a period of 5.0 ms means \(f = 200\,\mathrm{Hz}\).
:::

### Two different graphs

A wave depends on **position** and on **time** at once, so one graph can only show one of them. This is the most common source of lost marks in the whole topic, so be clear about which graph you have.

1. A **displacement against distance** graph is a snapshot of the whole wave at one instant. It looks like the wave on the rope. The horizontal distance between two adjacent crests is the **wavelength** \(\lambda\).
2. A **displacement against time** graph follows **one particle** as time passes. The horizontal distance between two adjacent crests is the **period** \(T\).

Both graphs below describe the same wave on a rope, which travels to the right with amplitude 4.0 cm, wavelength 2.0 m and frequency 0.50 Hz. The second graph is for the particle at \(x = 0.50\,\mathrm{m}\), which is at a crest at \(t = 0\).

:::plot Displacement against distance at \(t = 0\) for the rope wave. The crests are 2.0 m apart, so \(\lambda = 2.0\,\mathrm{m}\), and the amplitude is 4.0 cm.
--f "4*sin(pi*x)" --x 0 4 --y -5.5 5.5 --xlabel "x / m" --ylabel "y / cm" --pt "0.5,4,crest@n" --pt "2.5,4,next crest, 2.0 m away@n" --pt "1.5,-4,trough@s"
:::

:::plot Displacement against time for the particle at \(x = 0.50\,\mathrm{m}\). The crests are 2.0 s apart, so \(T = 2.0\,\mathrm{s}\).
--f "4*cos(pi*x)" --x 0 4 --y -5.5 5.5 --xlabel "t / s" --ylabel "y / cm" --pt "0,4,crest@ne" --pt "2,4,next crest, 2.0 s later@n" --pt "1,-4,trough@s"
:::

The wavelength and period give the speed: \(v = \lambda/T = 2.0/2.0 = 1.0\,\mathrm{m\,s^{-1}}\). Neither graph shows this speed on its own.

:::warn Amplitude is not peak-to-peak
Amplitude is measured from the **equilibrium position** to a crest (or a trough). The distance from a trough to the next crest is twice the amplitude. In the graphs above the amplitude is 4.0 cm and the peak-to-peak height is 8.0 cm.
:::

### Phase difference

Points on a wave that are a whole number of wavelengths apart are doing exactly the same thing at the same time: they are **in phase**. Two points half a wavelength apart do opposite things (one at a crest, the other at a trough): they are in **antiphase**, a phase difference of 180°.

One complete cycle is 360° or \(2\pi\) radians. A distance \(x\) along the wave is the fraction \(x/\lambda\) of a cycle, so

:::formula Phase difference
\[\phi = \frac{x}{\lambda} \times 360^\circ \qquad\text{or}\qquad \phi = \frac{2\pi x}{\lambda}\]
\(\phi\): phase difference between two points on a wave (° or rad) · \(x\): their separation along the wave (m) · \(\lambda\): wavelength (m). In the same way, two oscillations of period \(T\) that reach their crests a time \(\Delta t\) apart have \(\phi = (\Delta t/T) \times 360^\circ\).
:::

:::eg Two points on a wave of wavelength 1.2 m are 0.30 m apart along the wave. Find their phase difference in degrees and in radians.
The separation is the fraction \(0.30/1.2 = 0.25\) of a wavelength, a quarter of a cycle. [C1]

\[\phi = 0.25 \times 360^\circ = 90^\circ \qquad\text{or}\qquad \phi = \frac{2\pi \times 0.30}{1.2} = \frac{\pi}{2}\,\mathrm{rad} = 1.57\,\mathrm{rad}\] [A1]
When one point is at a crest, the other is passing through its equilibrium position.
:::

### Which way is a particle moving?

On a snapshot, every particle is for an instant at the displacement shown, and they are all moving. To find the direction, imagine the curve a very short time later: it has slid a tiny distance in the direction of travel. Then read the new displacement of the particle.

:::html
<figure class="fig"><svg viewBox="0 0 560 226" role="img" aria-label="A wave moving to the right, drawn as a snapshot. Point K at a crest is momentarily at rest. Point P just to the right of the crest, on the falling part of the curve, has an arrow pointing up. Point Q on the rising part of the curve, after the trough, has an arrow pointing down. Two crests are joined by a dimension arrow labelled wavelength."><path class="ax" d="M30 110H530"/><path class="c3" d="M40 110C45 105 60 86 70 78C80 71 90 65 100 65C110 65 120 71 130 78C140 86 150 99 160 110C170 121 180 134 190 142C200 149 210 155 220 155C230 155 240 149 250 142C260 134 270 121 280 110C290 99 300 86 310 78C320 71 330 65 340 65C350 65 360 71 370 78C380 86 390 99 400 110C410 121 420 134 430 142C440 149 450 155 460 155C470 155 480 149 490 142C500 134 515 115 520 110"/><path class="ln thin dash" d="M100 65V212M340 65V212"/><path class="c1" d="M220 212H104" marker-end="url(#ah-phys)"/><path class="c1" d="M220 212H336" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="220" y="205">λ</text><circle class="fi" cx="100" cy="65" r="4"/><text class="tl tc" x="100" y="53">K</text><circle class="fi" cx="130" cy="78.2" r="4"/><path class="c2" d="M130 72V38" marker-end="url(#ah2-phys)"/><text class="tl tc" x="130" y="30">P</text><circle class="fi" cx="250" cy="141.8" r="4"/><path class="c2" d="M250 148V182" marker-end="url(#ah2-phys)"/><text class="tl tc" x="250" y="198">Q</text><path class="c1" d="M390 34H470" marker-end="url(#ah-phys)"/><text class="tl ta tc" x="430" y="26">wave direction</text></svg><figcaption>The wave moves to the right. Slide the curve a little to the right: P then sees a higher part of the curve, so P moves up. Q sees a lower part, so Q moves down. K, at the crest, is momentarily at rest.</figcaption></figure>
:::

The rule for a wave moving to the **right**: particles on a part of the curve that slopes **downwards** (left to right) are moving **up**, and particles on an **upward** slope are moving **down**. A particle at a crest or a trough is momentarily at rest, and a particle crossing the equilibrium position moves fastest. If the wave moves to the left, every direction reverses.

Try it yourself in the tool below. Drag the points P and Q along the wave and watch their phase difference and the displacement–time graph of P. Then slow the wave by lowering the frequency, and change the wavelength to see how the phase difference between two fixed points changes.

:::html
<div class="widget" data-w="phys-wave" data-mode="progressive" data-a="2" data-lambda="4" data-f="0.5"></div>
:::

:::eg The graphs above describe a wave on a rope. State the wavelength, period, frequency and speed of the wave, and the phase difference between the particles at \(x = 0.50\,\mathrm{m}\) and \(x = 1.50\,\mathrm{m}\).
From the displacement–distance graph, the crests are at 0.50 m and 2.50 m, so \(\lambda = 2.0\,\mathrm{m}\). [B1]

From the displacement–time graph, the crests are at 0 and 2.0 s, so \(T = 2.0\,\mathrm{s}\) and \(f = 1/T = 0.50\,\mathrm{Hz}\). [B1]

Speed: \(v = \lambda/T = 2.0/2.0 = 1.0\,\mathrm{m\,s^{-1}}\). [A1]

The points are 1.0 m apart, which is half a wavelength, so their phase difference is \(180^\circ\) (\(\pi\) rad): one is at a crest and the other at a trough. [B1]
:::

## The wave equation

Because the wave moves forward one wavelength in each period, its speed, frequency and wavelength are linked by one of the most useful equations in physics.

:::proof examinable Deriving the wave equation \(v = f\lambda\)
Consider a wave of wavelength \(\lambda\), period \(T\) and frequency \(f\).
In one period \(T\), a particle completes one oscillation, and the wave pattern moves forward by exactly one wavelength \(\lambda\).
Speed is distance divided by time, so \(v = \dfrac{\lambda}{T}\).
Frequency is the reciprocal of the period, so \(\dfrac{1}{T} = f\).
Substitute: \(v = \dfrac{\lambda}{T} = \lambda \times \dfrac{1}{T} = f\lambda\).
:::

:::formula The wave equation
\[v = f\lambda\]
\(v\): wave speed (m s⁻¹) · \(f\): frequency (Hz) · \(\lambda\): wavelength (m). This holds for every progressive wave.
:::

The source fixes the **frequency**: the wave cannot oscillate at a different frequency from the thing that starts it. The **medium** fixes the speed. So when a wave enters a different medium, the speed and the wavelength change but the frequency does not.

:::eg A radio station broadcasts at 98.5 MHz. Radio waves travel at \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\) in air. Find the wavelength.
\[\lambda = \frac{v}{f} = \frac{3.00 \times 10^{8}}{98.5 \times 10^{6}}\] [C1]
\[\lambda = 3.05\,\mathrm{m}\] [A1]
Convert megahertz to hertz first: \(1\,\mathrm{MHz} = 10^{6}\,\mathrm{Hz}\). Quote the answer to three significant figures, the same as the data.
:::

:::eg A loudspeaker emits a note of frequency 256 Hz. The speed of sound in air is \(340\,\mathrm{m\,s^{-1}}\). Find the wavelength. The note then travels into helium, where the speed of sound is \(1000\,\mathrm{m\,s^{-1}}\) (to two significant figures). Find the frequency and wavelength in helium.
In air: \(\lambda = v/f = 340/256 = 1.33\,\mathrm{m}\). [C1] [A1]

The frequency is set by the loudspeaker, so it is still 256 Hz in helium. [B1] The wavelength becomes \(\lambda = 1000/256 = 3.9\,\mathrm{m}\) (2 s.f.). [A1]
:::

## The cathode-ray oscilloscope

An oscilloscope (c.r.o.) is a graph-plotting voltmeter. It shows how a p.d. changes with time, so it turns an electrical signal, or the sound from a microphone, into a picture of a wave. The screen is a grid of squares, usually 1 cm by 1 cm, called divisions.

- The **time-base** moves a spot across the screen at a steady rate. Its setting is a time per division (for example \(2.0\,\mathrm{ms\,cm^{-1}}\)), so the **horizontal** axis is a time axis. The width of one cycle in divisions, times the setting, is the **period**.
- The **\(y\)-gain** sets how many volts move the spot up by one division (for example \(0.50\,\mathrm{V\,cm^{-1}}\)). The vertical height in divisions, times the setting, is a p.d. The **amplitude** is half the peak-to-peak height.

:::html
<figure class="fig"><svg viewBox="20 10 490 366" role="img" aria-label="An oscilloscope screen with a grid ten divisions wide and eight high. A sine wave trace has four complete cycles across the screen. One cycle is 2.5 divisions wide and the trace is 3.0 divisions from trough to crest. The time-base is 2.0 milliseconds per centimetre and the y-gain is 0.50 volts per centimetre."><rect class="fp s-ink sw2" x="30" y="20" width="400" height="320"/><path class="ln-m thin" d="M70 20V340M110 20V340M150 20V340M190 20V340M230 20V340M270 20V340M310 20V340M350 20V340M390 20V340M30 60H430M30 100H430M30 140H430M30 180H430M30 220H430M30 260H430M30 300H430"/><path class="c3" d="M30 180C32 173 38 148 42 138C47 128 51 120 55 120C59 120 63 128 68 138C72 148 76 166 80 180C84 194 88 212 92 222C97 232 101 240 105 240C109 240 113 232 118 222C122 212 126 194 130 180C134 166 138 148 142 138C147 128 151 120 155 120C159 120 163 128 168 138C172 148 176 166 180 180C184 194 188 212 192 222C197 232 201 240 205 240C209 240 213 232 218 222C222 212 226 194 230 180C234 166 238 148 242 138C247 128 251 120 255 120C259 120 263 128 268 138C272 148 276 166 280 180C284 194 288 212 292 222C297 232 301 240 305 240C309 240 313 232 318 222C322 212 326 194 330 180C334 166 338 148 342 138C347 128 351 120 355 120C359 120 363 128 368 138C372 148 376 166 380 180C384 194 388 212 392 222C397 232 401 240 405 240C409 240 413 232 418 222C422 212 428 187 430 180"/><path class="ln thin dash" d="M55 120V90M155 120V90"/><path class="c1" d="M105 96H58" marker-end="url(#ah-phys)"/><path class="c1" d="M105 96H152" marker-end="url(#ah-phys)"/><text class="tl tc halo" x="105" y="84">2.5 cm</text><path class="ln thin dash" d="M55 120H440M105 240H440"/><path class="c1" d="M440 180V124" marker-end="url(#ah-phys)"/><path class="c1" d="M440 180V236" marker-end="url(#ah-phys)"/><text class="tl" x="448" y="184">3.0 cm</text><text class="tl tc" x="230" y="364">time-base 2.0 ms cm⁻¹ · y-gain 0.50 V cm⁻¹</text></svg><figcaption>A trace on an oscilloscope screen. One cycle is 2.5 cm wide and the trace is 3.0 cm from trough to crest. With the settings shown, these readings give the period and the amplitude.</figcaption></figure>
:::

:::eg Read the frequency and the amplitude from the oscilloscope trace above. The time-base is \(2.0\,\mathrm{ms\,cm^{-1}}\) and the y-gain is \(0.50\,\mathrm{V\,cm^{-1}}\).
One cycle spans 2.5 cm, so the period is \(T = 2.5 \times 2.0 = 5.0\,\mathrm{ms}\). [C1]

\[f = \frac{1}{T} = \frac{1}{5.0 \times 10^{-3}} = 200\,\mathrm{Hz}\] [A1]
The peak-to-peak height is 3.0 cm, which is \(3.0 \times 0.50 = 1.5\,\mathrm{V}\). [C1] The amplitude is half of that: \(0.75\,\mathrm{V}\). [A1]
:::

:::eg The time-base of the oscilloscope above is changed to \(1.0\,\mathrm{ms\,cm^{-1}}\). How many complete cycles of the same signal fit across the 10 cm wide screen?
One cycle now spans \(5.0\,\mathrm{ms} / 1.0\,\mathrm{ms\,cm^{-1}} = 5.0\,\mathrm{cm}\). [C1] Across 10 cm there are \(10/5.0 = 2\) complete cycles. [A1] A smaller time per division spreads the wave out, so fewer cycles are visible. The amplitude is unchanged, because the y-gain is unchanged.
:::

:::lab Finding the frequency of a tuning fork
:::steps
1. Connect a microphone to the oscilloscope input. Strike the tuning fork and hold it close to the microphone.
2. Adjust the time-base until two to four cycles fill the screen, and adjust the y-gain until the trace is large but fits.
3. Measure the width of several complete cycles (for example 4 cycles) and divide, to reduce the reading uncertainty. Multiply by the time-base setting to get the period \(T\).
4. Calculate \(f = 1/T\) and compare it with the frequency stamped on the fork.
:::
:::

:::exam Oscilloscope questions
Always write the multiplication: "number of divisions × setting". Convert units before using \(f = 1/T\): milliseconds to seconds. For the amplitude, halve the peak-to-peak height, and say you did. If the time-base is switched off, the spot only moves up and down on a vertical line and no wave shape is visible.
:::

## Energy and intensity

A progressive wave transfers energy, so we can ask how much arrives at a detector.

:::def Intensity
The power per unit area incident at right angles to the direction of travel of the wave.
:::

:::formula Intensity
\[I = \frac{P}{A}\]
\(I\): intensity (W m⁻²) · \(P\): power carried by the wave (W) · \(A\): area at right angles to the direction of travel (m²).
:::

:::eg A laser beam of power 5.0 mW has a circular cross-section of diameter 2.0 mm. Find the intensity of the beam.
Area: \(A = \pi r^2 = \pi \times (1.0 \times 10^{-3})^2 = 3.14 \times 10^{-6}\,\mathrm{m^2}\) [C1]
\[I = \frac{P}{A} = \frac{5.0 \times 10^{-3}}{3.14 \times 10^{-6}} = 1.6 \times 10^{3}\,\mathrm{W\,m^{-2}}\] [A1]
This is more than the intensity of sunlight on the ground (about \(10^{3}\,\mathrm{W\,m^{-2}}\)), which is why you should never shine a laser at anyone's eyes.
:::

### Intensity and amplitude

The energy carried by a wave comes from the oscillating particles, and the energy of an oscillation is proportional to the **square** of its amplitude. A wave with twice the amplitude therefore carries four times the power through the same area.

:::key Intensity and amplitude
\[I \propto A^2\]
\(A\) here is the amplitude of the wave. If the amplitude is multiplied by 3, the intensity is multiplied by 9. Equivalently, the amplitude is proportional to \(\sqrt{I}\).
:::

### Waves spreading out from a point

A small source that sends energy equally in every direction spreads its power over the surface of a sphere. At distance \(r\) the area is \(4\pi r^2\), so

:::formula Intensity from a point source
\[I = \frac{P}{4\pi r^2}\]
\(P\): power radiated by the source (W) · \(r\): distance from the source (m). So \(I \propto 1/r^2\): the **inverse square law**. This assumes none of the energy is absorbed on the way.
:::

:::html
<figure class="fig small"><svg viewBox="30 28 290 192" role="img" aria-label="A point source S on the left sends rays outwards. A screen at distance r has area A, a screen at distance 2r has area 4A and a screen at distance 3r has area 9A, so the same power is spread over larger areas."><path class="ln" d="M50 100L290 55M50 100L290 145"/><path class="ln thick" d="M130 85V115M210 70V130M290 55V145"/><circle class="fi" cx="50" cy="100" r="5"/><text class="tl te" x="42" y="105">S</text><text class="tl tc" x="130" y="76">A</text><text class="tl tc" x="210" y="61">4A</text><text class="tl tc" x="290" y="46">9A</text><path class="c1" d="M90 150H54" marker-end="url(#ah-phys)"/><path class="c1" d="M90 150H126" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="90" y="144">r</text><path class="c1" d="M130 178H54" marker-end="url(#ah-phys)"/><path class="c1" d="M130 178H206" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="130" y="172">2r</text><path class="c1" d="M170 206H54" marker-end="url(#ah-phys)"/><path class="c1" d="M170 206H286" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="170" y="200">3r</text></svg><figcaption>Doubling the distance from the source spreads the same power over four times the area, so the intensity falls to a quarter. Trebling the distance gives a ninth.</figcaption></figure>
:::

:::eg A point source radiates 60 W equally in all directions. Find the intensity at 2.0 m and at 4.0 m, and the ratio of the amplitudes at these two distances.
At 2.0 m: \(I = \dfrac{60}{4\pi \times 2.0^2}\) [C1] \(= 1.19\,\mathrm{W\,m^{-2}}\). [A1]

At 4.0 m: \(I = \dfrac{60}{4\pi \times 4.0^2} = 0.298\,\mathrm{W\,m^{-2}}\). [A1]

The distance doubled, so the intensity fell to a quarter. Because \(I \propto A^2\), the amplitude fell to a half: \(A_{4.0}/A_{2.0} = \sqrt{1/4} = 0.50\). [B1]
:::

:::warn Intensity is proportional to amplitude squared
A common wrong answer says that doubling the amplitude doubles the intensity. The rule is \(I \propto A^2\): doubling the amplitude makes the intensity four times bigger. In the other direction, an intensity that falls to a quarter means the amplitude falls to a half, not a quarter.
:::

## Transverse and longitudinal waves

The direction in which the particles oscillate gives the two types of wave.

:::def Transverse wave
A wave in which the oscillations of the particles are perpendicular to the direction of energy transfer (the direction of travel of the wave).
:::

:::def Longitudinal wave
A wave in which the oscillations of the particles are parallel to the direction of energy transfer.
:::

| | Transverse wave | Longitudinal wave |
|---|---|---|
| Oscillations | at right angles to the direction of travel | along the direction of travel |
| Pattern | crests and troughs | compressions and rarefactions |
| Examples | light and all electromagnetic waves, waves on a rope, ripples on water | sound in air, a push-pull wave along a spring |
| Needs a medium? | electromagnetic waves do not; the others do | yes |
| Can be polarised? | yes | no |

In a **compression** the particles are closer together than normal, so the pressure is high. In a **rarefaction** they are further apart, so the pressure is low.

### Graphs of a longitudinal wave

A longitudinal wave is also drawn as a graph of displacement against distance. A displacement is a distance along the direction of travel, and a positive displacement is, by convention, to the right. The graph looks exactly like the graph of a transverse wave, but it means something different: a point on the curve above the axis is a particle displaced to the **right**, and a point below the axis is displaced to the **left**.

:::html
<figure class="fig"><svg viewBox="20 10 520 225" role="img" aria-label="A row of 23 particles of a longitudinal wave, bunched into compressions labelled C and spread out in rarefactions labelled R, above a displacement-distance graph. Dashed lines join each compression and rarefaction to the graph. Compressions are at the points where the graph crosses the axis going downwards, and rarefactions where it crosses going upwards."><circle class="fi" cx="40.0" cy="44" r="4"/><circle class="fi" cx="69.1" cy="44" r="4"/><circle class="fi" cx="94.0" cy="44" r="4"/><circle class="fi" cx="113.1" cy="44" r="4"/><circle class="fi" cx="128.0" cy="44" r="4"/><circle class="fi" cx="142.9" cy="44" r="4"/><circle class="fi" cx="162.0" cy="44" r="4"/><circle class="fi" cx="186.9" cy="44" r="4"/><circle class="fi" cx="216.0" cy="44" r="4"/><circle class="fi" cx="245.1" cy="44" r="4"/><circle class="fi" cx="270.0" cy="44" r="4"/><circle class="fi" cx="289.1" cy="44" r="4"/><circle class="fi" cx="304.0" cy="44" r="4"/><circle class="fi" cx="318.9" cy="44" r="4"/><circle class="fi" cx="338.0" cy="44" r="4"/><circle class="fi" cx="362.9" cy="44" r="4"/><circle class="fi" cx="392.0" cy="44" r="4"/><circle class="fi" cx="421.1" cy="44" r="4"/><circle class="fi" cx="446.0" cy="44" r="4"/><circle class="fi" cx="465.1" cy="44" r="4"/><circle class="fi" cx="480.0" cy="44" r="4"/><circle class="fi" cx="494.9" cy="44" r="4"/><circle class="fi" cx="514.0" cy="44" r="4"/><path class="ln-m thin" d="M40 54V60M62 54V60M84 54V60M106 54V60M128 54V60M150 54V60M172 54V60M194 54V60M216 54V60M238 54V60M260 54V60M282 54V60M304 54V60M326 54V60M348 54V60M370 54V60M392 54V60M414 54V60M436 54V60M458 54V60M480 54V60M502 54V60M524 54V60"/><text class="tb tc" x="128" y="28">C</text><text class="tb tc" x="304" y="28">C</text><text class="tb tc" x="480" y="28">C</text><text class="tb tc" x="216" y="28">R</text><text class="tb tc" x="392" y="28">R</text><path class="ln thin dash" d="M128 66V195M304 66V195M480 66V195M216 66V195M392 66V195"/><path class="ax" d="M30 150H534"/><path class="c3" d="M40 150C44 145 55 128 62 122C69 115 77 110 84 110C91 110 99 115 106 122C113 128 121 141 128 150C135 159 143 172 150 178C157 185 165 190 172 190C179 190 187 185 194 178C201 172 209 159 216 150C223 141 231 128 238 122C245 115 253 110 260 110C267 110 275 115 282 122C289 128 297 141 304 150C311 159 319 172 326 178C333 185 341 190 348 190C355 190 363 185 370 178C377 172 385 159 392 150C399 141 407 128 414 122C421 115 429 110 436 110C443 110 451 115 458 122C465 128 473 141 480 150C487 159 495 172 502 178C509 185 520 188 524 190"/><text class="tl" x="36" y="98">s (+ right)</text><text class="tl" x="520" y="140">x</text><path class="c1" d="M216 216H132" marker-end="url(#ah-phys)"/><path class="c1" d="M216 216H300" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="216" y="209">λ</text></svg><figcaption>The top row shows 23 particles at one instant (short marks show where each would be in the absence of the wave). Particles to the left of a compression C are displaced to the right and those to its right are displaced to the left, so they bunch up. On the graph, C is where the curve crosses the axis going down and R is where it crosses going up. The displacement s is positive when a particle moves to the right.</figcaption></figure>
:::

To find a compression from the graph, look for a point of **zero displacement** where the curve is **sloping downwards**. Particles on the left of that point have positive displacement (to the right) and particles on the right of it have negative displacement (to the left), so they all move towards the point. A rarefaction is at a point of zero displacement with the curve sloping **upwards**. The distance between two compressions (or two rarefactions) is the wavelength.

:::eg A longitudinal wave in a spring has wavelength 0.40 m and frequency 15 Hz. Find its speed. Particle X is displaced 3.0 mm to the right at one instant. State the phase difference between X and a particle 0.60 m further along.
\[v = f\lambda = 15 \times 0.40 = 6.0\,\mathrm{m\,s^{-1}}\] [C1] [A1]
The separation is \(0.60/0.40 = 1.5\) wavelengths, so the phase difference is \(1.5 \times 360^\circ = 540^\circ\), which is the same as \(180^\circ\) (antiphase). [B1] The second particle is displaced 3.0 mm to the left, if the wave has the same amplitude there. [B1]
:::

## The Doppler effect

An ambulance siren sounds higher as it approaches you and drops in pitch as it passes. The siren itself has not changed: the frequency that you **observe** is different from the frequency of the **source**.

:::def Doppler effect
The change in the observed frequency of a wave when the source of the waves moves relative to the observer.
:::

Imagine the source emits one wavefront every period \(T_\text{s} = 1/f_\text{s}\). Each wavefront spreads out in a circle from the point where it was emitted. The source moves on, so the circles are not centred on the same point.

:::html
<figure class="fig"><svg viewBox="110 5 360 272" role="img" aria-label="Five circular wavefronts emitted at equal time intervals by a source that moves to the right. The circles are bunched together in front of the source (right) and spread apart behind it (left). Observer A is ahead of the source and observer B is behind it."><circle class="ln thin" cx="291.2" cy="130" r="22"/><circle class="ln thin" cx="282.4" cy="130" r="44"/><circle class="ln thin" cx="273.6" cy="130" r="66"/><circle class="ln thin" cx="264.8" cy="130" r="88"/><circle class="ln thin" cx="256" cy="130" r="110"/><circle class="fi" cx="300" cy="130" r="5"/><path class="c1" d="M240 258H310" marker-end="url(#ah-phys)"/><text class="tl ta" x="318" y="262">source velocity</text><circle class="fp s-ink sw2" cx="450" cy="130" r="5"/><text class="tl tc" x="450" y="152">A</text><circle class="fp s-ink sw2" cx="130" cy="130" r="5"/><text class="tl tc" x="130" y="152">B</text><text class="tl te" x="290" y="135">S</text></svg><figcaption>The source S moves to the right at 0.4 of the wave speed. Wavefronts are closer together ahead of S (shorter wavelength, observer A hears a higher frequency) and further apart behind S (longer wavelength, observer B hears a lower frequency).</figcaption></figure>
:::

Ahead of the source the wavelength is shortened, behind it the wavelength is lengthened. The speed of sound relative to the air does not depend on the motion of the source, so shorter wavelength means higher frequency, and longer wavelength means lower frequency. The syllabus only needs a **moving source and a stationary observer**.

:::formula The Doppler effect for sound
\[f_\text{o} = \frac{f_\text{s}\,v}{v \pm v_\text{s}}\]
\(f_\text{o}\): observed frequency (Hz) · \(f_\text{s}\): frequency of the source (Hz) · \(v\): speed of sound (m s⁻¹) · \(v_\text{s}\): speed of the source (m s⁻¹). Use **\(v - v_\text{s}\)** (minus) when the source moves **towards** the observer, and **\(v + v_\text{s}\)** (plus) when it moves **away**.
:::

:::proof Deriving the formula from the wavelength
A source of frequency \(f_\text{s}\) emits a wavefront every \(T = 1/f_\text{s}\).
In one period, the first wavefront travels a distance \(vT\) towards the observer.
In the same time, the source moves a distance \(v_\text{s}T\) in the same direction.
So the next wavefront is only \(vT - v_\text{s}T = (v - v_\text{s})T\) behind the first: the observed wavelength is \(\lambda_\text{o} = (v - v_\text{s})/f_\text{s}\).
The waves still travel at speed \(v\) through the air, so the observer receives \(f_\text{o} = \dfrac{v}{\lambda_\text{o}} = \dfrac{f_\text{s}\,v}{v - v_\text{s}}\).
For a source moving away, the wavefronts are \(vT + v_\text{s}T\) apart and the same argument gives \(f_\text{o} = \dfrac{f_\text{s}\,v}{v + v_\text{s}}\).
:::

:::eg An ambulance travels at \(25\,\mathrm{m\,s^{-1}}\) with its siren sounding at 700 Hz. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Find the frequency heard by a stationary observer when the ambulance is approaching and when it is receding.
Approaching (source moves towards the observer, so use \(v - v_\text{s}\)):
\[f_\text{o} = \frac{700 \times 340}{340 - 25}\] [C1]
\[f_\text{o} = 756\,\mathrm{Hz}\] [A1]
Receding (use \(v + v_\text{s}\)):
\[f_\text{o} = \frac{700 \times 340}{340 + 25} = 652\,\mathrm{Hz}\] [A1]
The approaching frequency is higher than 700 Hz and the receding frequency is lower, as it must be.
:::

:::eg A train sounds a horn of frequency 480 Hz as it approaches a station at constant speed. A person on the platform hears 510 Hz. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Find the speed of the train.
\[510 = \frac{480 \times 340}{340 - v_\text{s}}\] [C1]
Rearrange: \(340 - v_\text{s} = \dfrac{480 \times 340}{510} = 320\), so \(v_\text{s} = 340 - 320 = 20\,\mathrm{m\,s^{-1}}\). [A1]
:::

The same effect happens for light from a moving source. The light from distant galaxies is shifted to lower frequencies (a red shift) because they move away from us, which is how astronomers know the Universe is expanding. This is covered in [Astronomy and cosmology](#phys.astro). Radar speed guns and ultrasound blood-flow scanners also use frequency changes of waves reflected from a moving object.

## The electromagnetic spectrum

Light is one member of a family of waves that all share the same nature. **All electromagnetic waves are transverse waves that travel with the same speed in free space (a vacuum), \(c = 3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\).** They consist of oscillating electric and magnetic fields at right angles to each other and to the direction of travel, so unlike sound they need **no medium**. They differ only in frequency and wavelength, linked by \(c = f\lambda\).

| Region | Approximate wavelength in free space |
|---|---|
| Radio waves | more than \(10^{-1}\,\mathrm{m}\) (up to \(10^{4}\,\mathrm{m}\) and beyond) |
| Microwaves | \(10^{-3}\,\mathrm{m}\) to \(10^{-1}\,\mathrm{m}\) |
| Infrared | \(7 \times 10^{-7}\,\mathrm{m}\) to \(10^{-3}\,\mathrm{m}\) |
| Visible light | \(4 \times 10^{-7}\,\mathrm{m}\) to \(7 \times 10^{-7}\,\mathrm{m}\) |
| Ultraviolet | \(10^{-8}\,\mathrm{m}\) to \(4 \times 10^{-7}\,\mathrm{m}\) |
| X-rays | \(10^{-13}\,\mathrm{m}\) to \(10^{-8}\,\mathrm{m}\) |
| Gamma rays | less than about \(10^{-11}\,\mathrm{m}\) |

These are approximate, and the boundaries are not sharp. X-rays and gamma rays overlap in wavelength: they differ in how they are produced (X-rays by electrons, gamma rays by atomic nuclei). **Wavelengths from 400 nm to 700 nm in free space are visible to the human eye**: violet is at the short-wavelength end and red at the long end.

:::html
<figure class="fig"><svg viewBox="0 20 550 140" role="img" aria-label="The electromagnetic spectrum on a logarithmic wavelength scale from ten thousand metres on the left to ten to the minus thirteen metres on the right, in order: radio waves, microwaves, infrared, a narrow visible band, ultraviolet and X-rays, with gamma rays overlapping the short-wavelength end of the X-ray band."><rect class="f1 s-ink sw1" x="20" y="60" width="150" height="26"/><rect class="f2 s-ink sw1" x="170" y="60" width="60" height="26"/><rect class="f3 s-ink sw1" x="230" y="60" width="94.6" height="26"/><rect class="fa s-ink sw1" x="324.6" y="60" width="7.4" height="26"/><rect class="f1 s-ink sw1" x="332" y="60" width="48" height="26"/><rect class="f2 s-ink sw1" x="380" y="60" width="150" height="26"/><rect class="f3 s-ink sw1" x="470" y="92" width="60" height="24"/><text class="tl tc" x="95" y="52">radio waves</text><text class="tl tc" x="200" y="52">microwaves</text><text class="tl tc" x="277" y="52">infrared</text><text class="tl tc" x="356" y="52">ultraviolet</text><text class="tl tc" x="455" y="52">X-rays</text><text class="tl tc" x="500" y="109">γ-rays</text><path class="ln thin" d="M328 86V108"/><text class="tl tc" x="328" y="124">visible</text><path class="ln" d="M20 132H530"/><path class="ln" d="M20 132V138M80 132V138M140 132V138M200 132V138M260 132V138M320 132V138M380 132V138M440 132V138M500 132V138"/><text class="ts tc" x="20" y="150">10⁴</text><text class="ts tc" x="80" y="150">10²</text><text class="ts tc" x="140" y="150">1</text><text class="ts tc" x="200" y="150">10⁻²</text><text class="ts tc" x="260" y="150">10⁻⁴</text><text class="ts tc" x="320" y="150">10⁻⁶</text><text class="ts tc" x="380" y="150">10⁻⁸</text><text class="ts tc" x="440" y="150">10⁻¹⁰</text><text class="ts tc" x="500" y="150">10⁻¹²</text></svg><figcaption>The regions drawn on a logarithmic wavelength scale (in metres), long wavelengths on the left. Visible light is a very narrow band, 400 nm to 700 nm. The gamma-ray and X-ray regions overlap.</figcaption></figure>
:::

:::eg Calculate the frequencies that correspond to wavelengths of 400 nm and 700 nm in free space. Then find the wavelength of the 2.45 GHz microwaves used in a microwave oven.
Rearrange the wave equation with \(v = c\): \(f = c/\lambda\). [C1]

\[f_{400} = \frac{3.00 \times 10^{8}}{400 \times 10^{-9}} = 7.50 \times 10^{14}\,\mathrm{Hz} \qquad f_{700} = \frac{3.00 \times 10^{8}}{700 \times 10^{-9}} = 4.29 \times 10^{14}\,\mathrm{Hz}\] [A1]
Microwave oven: \(\lambda = \dfrac{3.00 \times 10^{8}}{2.45 \times 10^{9}} = 0.122\,\mathrm{m}\), or 12.2 cm, in the microwave range. [A1]
:::

:::warn Electromagnetic waves and media
Electromagnetic waves do not need a medium: sunlight reaches the Earth through the vacuum of space. Do not confuse them with sound, which is a longitudinal wave and **cannot** travel through a vacuum. In a medium such as glass, light travels slower than \(c\), but "all electromagnetic waves travel at the same speed" is true in free space.
:::

## Polarisation

A wave on a rope can oscillate up and down, from side to side, or at any angle in between, as long as it is at right angles to the direction of travel. Now pass the rope through a narrow vertical slit in a board. A vertical oscillation passes through, but a horizontal oscillation is blocked: the slit only lets through oscillations in one plane.

:::def Plane polarised wave
A wave in which the oscillations are in one plane only, and that plane contains the direction of travel of the wave.
:::

:::html
<figure class="fig"><svg viewBox="0 -4 520 164" role="img" aria-label="A rope wave oscillating vertically travels from the left. It passes through a board with a vertical slit and continues oscillating. At a second board with a horizontal slit the wave is stopped, and the rope beyond is flat. Small square icons beside the top of each board show the slit as seen by the oncoming wave."><path class="c3" d="M20 80C30 66 40 52 50 52C60 52 70 66 80 80C90 94 100 108 110 108C120 108 130 94 140 80C150 66 160 52 170 52C180 52 183 56 190 80"/><path class="ln thick" d="M190 14V74M190 86V138"/><path class="c3" d="M190 80C196 94 210 108 220 108C230 108 240 94 250 80C260 66 270 52 280 52C290 52 300 66 310 80"/><path class="ln thick" d="M310 14V74M310 86V138"/><path class="c3" d="M310 80H500"/><rect class="f1 s-ink sw1" x="198" y="16" width="22" height="22"/><rect class="fp" x="207" y="18" width="4" height="18"/><rect class="f1 s-ink sw1" x="318" y="16" width="22" height="22"/><rect class="fp" x="320" y="25" width="18" height="4"/><text class="tl tc" x="190" y="10">board 1</text><text class="tl tc" x="310" y="10">board 2</text><text class="tl tc" x="250" y="154">vertical slit: wave passes</text><text class="tl tc" x="430" y="154">horizontal slit: blocked</text></svg><figcaption>A transverse wave on a rope, with each slit shown face-on in the small square beside its board. A vertical slit passes the vertical oscillations. A second slit rotated through 90° blocks them completely. This cannot happen with a longitudinal wave, whose oscillations are along the rope, so a longitudinal wave cannot be polarised.</figcaption></figure>
:::

Only **transverse** waves can be polarised. A longitudinal wave oscillates along its direction of travel, so there is no sideways direction to select: a slit of any orientation passes it. The fact that light can be polarised is the evidence that light is a transverse wave.

Light from a lamp or the Sun is **unpolarised**: it is a mixture of waves with oscillations in every plane at right angles to the direction of travel. A **polarising filter** (such as Polaroid) lets through only the component of the oscillation along its **transmission axis**. After the filter the light is plane polarised. Polarising filters are used in:

- **Polaroid sunglasses**, which block the partly polarised glare reflected from roads and water.
- **LCD screens** (phones, calculators, monitors), where a liquid crystal layer rotates the plane of polarisation between two crossed filters, so that each pixel can be switched between light and dark.
- **Radio and TV aerials**, which must be aligned parallel to the transmitting aerial to pick up the most signal.
- **A microwave demonstration:** a metal grille between a microwave transmitter and its receiver blocks the waves when the bars are parallel to the electric field, and lets them through when the grille is rotated through 90°.

### Malus's law

Now suppose plane-polarised light of intensity \(I_0\) reaches a filter whose transmission axis makes an angle \(\theta\) with the plane of polarisation of the light. Only the component of the oscillation along the axis gets through. The amplitude is reduced by the factor \(\cos\theta\), and because intensity is proportional to amplitude squared, the intensity is reduced by \(\cos^2\theta\).

:::formula Malus's law
\[I = I_0\cos^2\theta\]
\(I_0\): intensity of the plane-polarised light incident on the filter (W m⁻²) · \(I\): intensity transmitted (W m⁻²) · \(\theta\): angle between the plane of polarisation of the incident light and the transmission axis of the filter.
:::

:::plot Malus's law: the transmitted intensity \(I/I_0 = \cos^2\theta\) as the filter is rotated through 360°. The intensity is maximum at 0° and 180°, and zero when the axis is at 90° or 270° to the plane of polarisation.
--f "cos(x)**2" --deg --x 0 360 --y 0 1.15 --xlabel "θ / °" --ylabel "I / I₀" --xstep 90 --pt "180,1,maximum@n" --pt "45,0.5,I₀/2@ne"
:::

:::eg Plane-polarised light of intensity \(8.0\,\mathrm{W\,m^{-2}}\) falls on a polarising filter. Its transmission axis is at \(30^\circ\) to the plane of polarisation. Find the transmitted intensity.
\[I = I_0\cos^2\theta = 8.0 \times \cos^2 30^\circ\] [C1]
\[I = 8.0 \times 0.75 = 6.0\,\mathrm{W\,m^{-2}}\] [A1]
Square the cosine, not the angle: \(\cos^2 30^\circ = (0.866)^2 = 0.75\).
:::

With a **series of filters**, apply the law to each filter in turn. The light leaving one filter is polarised along that filter's axis, so the angle for the next filter is the angle between the **two axes**.

:::html
<figure class="fig"><svg viewBox="10 0 540 236" role="img" aria-label="Top row: vertically polarised light of intensity I zero meets a filter with a vertical axis and then a filter with a horizontal axis; no light emerges. Bottom row: the same two filters with a third filter between them whose axis is at 45 degrees; the intensity is I zero after the first filter, I zero over two after the 45 degree filter and I zero over four after the last."><path class="c1" d="M20 62H114" marker-end="url(#ah-phys)"/><path class="ln thick" d="M130 28V96"/><path class="c1" d="M146 62H284" marker-end="url(#ah-phys)"/><path class="ln thick" d="M300 28V96"/><path class="ln dash thin" d="M316 62H420"/><text class="tl tc" x="130" y="20">1 (0°)</text><text class="tl tc" x="300" y="20">2 (90°)</text><text class="tl tc" x="68" y="50">I₀</text><text class="tl tc" x="215" y="50">I₀</text><text class="tl tc" x="480" y="66">I = 0</text><path class="c1" d="M20 180H114" marker-end="url(#ah-phys)"/><path class="ln thick" d="M130 146V214"/><path class="c1" d="M146 180H214" marker-end="url(#ah-phys)"/><path class="ln thick" d="M230 146V214"/><path class="c1" d="M246 180H314" marker-end="url(#ah-phys)"/><path class="ln thick" d="M330 146V214"/><path class="c1" d="M346 180H440" marker-end="url(#ah-phys)"/><text class="tl tc" x="130" y="138">1 (0°)</text><text class="tl tc" x="230" y="138">3 (45°)</text><text class="tl tc" x="330" y="138">2 (90°)</text><text class="tl tc" x="68" y="168">I₀</text><text class="tl tc" x="180" y="168">I₀</text><text class="tl tc" x="280" y="168">I₀/2</text><text class="tl tc" x="393" y="168">I₀/4</text></svg><figcaption>Top: two filters with axes at 90° to each other (crossed) stop plane-polarised light completely. Bottom: a third filter at 45° between them lets I₀/4 through. Adding a filter can increase the transmitted light, because it turns the plane of polarisation in two smaller steps.</figcaption></figure>
:::

:::eg Plane-polarised light of intensity \(I_0\), polarised vertically, passes through a vertical filter, a filter at \(45^\circ\) to the vertical, and a horizontal filter, in that order. Find the final intensity. What is it if the \(45^\circ\) filter is removed?
After the vertical filter (\(\theta = 0^\circ\)): \(I_1 = I_0\cos^2 0^\circ = I_0\).

After the \(45^\circ\) filter: \(I_2 = I_0\cos^2 45^\circ = \tfrac12 I_0\). [C1]
The horizontal filter is at \(45^\circ\) to the \(45^\circ\) filter: \(I_3 = I_2\cos^2 45^\circ = \tfrac12 \times \tfrac12 I_0 = \tfrac14 I_0\). [A1]
Without the \(45^\circ\) filter the two remaining filters are at \(90^\circ\): \(I = I_0\cos^2 90^\circ = 0\). [B1]
:::

:::eg Plane-polarised light of intensity \(12\,\mathrm{W\,m^{-2}}\) passes through a filter with its axis at \(20^\circ\) to the plane of polarisation, and then through a second filter with its axis at \(50^\circ\) to the first. Find the final intensity.
\[I_1 = 12\cos^2 20^\circ = 12 \times 0.883 = 10.6\,\mathrm{W\,m^{-2}}\] [C1]
\[I_2 = I_1\cos^2 50^\circ = 10.6 \times 0.413 = 4.4\,\mathrm{W\,m^{-2}}\] [A1]
The angle in the second step is between the **axes of the two filters**, which is given as 50°.
:::

The syllabus does not ask you to calculate what a filter does to **unpolarised** light. (For reference, an ideal filter passes half of the intensity of unpolarised light and polarises what it passes.)

:::board
Cambridge examines Malus's law only for light that is already plane polarised. Edexcel IAL and AQA also state that an ideal filter halves the intensity of unpolarised light, which Cambridge does not examine. AQA and OCR treat the Doppler effect for light (\(\Delta f / f = v/c\)) in their astrophysics options; Cambridge AS covers only sound with a moving source.
:::

:::eg Spot the error: an ambulance siren of frequency 700 Hz approaches a stationary observer at \(25\,\mathrm{m\,s^{-1}}\). The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Find the observed frequency.
A student wrote this answer.

Line 1: the source is approaching, so \(f_\text{o} = \dfrac{f_\text{s}\,v}{v + v_\text{s}}\)
Line 2: \(f_\text{o} = \dfrac{700 \times 340}{340 + 25} = 652\,\mathrm{Hz}\)

**Line 1 is wrong: for a source moving towards the observer the denominator is \(v - v_\text{s}\) (the wavefronts are squeezed). The formula mark is lost and the answer mark with it.** [C0] [A0]

Correct working: \(f_\text{o} = \dfrac{700 \times 340}{340 - 25} = 756\,\mathrm{Hz}\). [C1] [A1]

Check: an approaching source must sound higher than 700 Hz, and 652 Hz is lower, so the answer should have looked wrong at once.
:::

:::try Start easy, finish at exam standard
Q: A wave has frequency 5.0 Hz and wavelength 0.30 m. Find its speed.
A: \(v = f\lambda = 5.0 \times 0.30 = 1.5\,\mathrm{m\,s^{-1}}\).
Q: A source vibrates at 50 Hz. Write down the period in milliseconds.
A: \(T = 1/f = 1/50 = 0.020\,\mathrm{s} = 20\,\mathrm{ms}\).
Q: Two points on a wave of wavelength 0.60 m are 0.40 m apart along the wave. Find their phase difference in degrees and in radians.
A: Fraction of a cycle \(= 0.40/0.60 = \tfrac23\), so \(\phi = \tfrac23 \times 360^\circ = 240^\circ\) and \(\phi = \tfrac23 \times 2\pi = \tfrac{4\pi}{3} = 4.19\,\mathrm{rad}\).
Q: An oscilloscope time-base is set at \(5.0\,\mathrm{ms\,cm^{-1}}\). One complete cycle of a signal is 4.0 cm wide on the screen. Find the frequency of the signal.
A: \(T = 4.0 \times 5.0 = 20\,\mathrm{ms}\), so \(f = 1/(20 \times 10^{-3}) = 50\,\mathrm{Hz}\).
Q: The intensity of sunlight on a solar panel of area \(0.40\,\mathrm{m^2}\) is \(0.50\,\mathrm{kW\,m^{-2}}\) at right angles to the panel. Find the power that arrives on the panel.
A: \(P = IA = 500 \times 0.40 = 200\,\mathrm{W}\). Change kW into W first.
Q: The amplitude of a wave is multiplied by 3. By what factor does the intensity change?
A: \(I \propto A^2\), so the intensity is multiplied by \(3^2 = 9\).
Q: A source of frequency 1000 Hz moves away from a stationary observer at \(30\,\mathrm{m\,s^{-1}}\). The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Find the observed frequency.
A: The source recedes, so \(f_\text{o} = \dfrac{1000 \times 340}{340 + 30} = 919\,\mathrm{Hz}\).
Q: Calculate the frequency of blue light of wavelength 450 nm in free space.
A: \(f = c/\lambda = \dfrac{3.00 \times 10^{8}}{450 \times 10^{-9}} = 6.67 \times 10^{14}\,\mathrm{Hz}\).
Q: Plane-polarised light of intensity \(10\,\mathrm{W\,m^{-2}}\) meets a filter at \(60^\circ\) to its plane of polarisation. Find the transmitted intensity. What happens at \(90^\circ\)?
A: \(I = 10\cos^2 60^\circ = 10 \times 0.25 = 2.5\,\mathrm{W\,m^{-2}}\). At \(90^\circ\), \(\cos 90^\circ = 0\), so no light is transmitted.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define the wavelength of a wave.
A: The distance between two adjacent points on the wave that are in phase (for example two adjacent crests). [B1]
Q: [3 marks] ★ State three differences between a transverse wave and a longitudinal wave.
A: In a transverse wave the oscillations are perpendicular to the direction of energy transfer, in a longitudinal wave they are parallel to it. [B1] A transverse wave has crests and troughs, a longitudinal wave has compressions and rarefactions. [B1] A transverse wave can be polarised, a longitudinal wave cannot. [B1] (Other valid contrasts: light and rope waves against sound and springs, for any one of the three marks.)
Q: [3 marks] ★★ A detector at a distance of 3.0 m from a small source that radiates equally in all directions receives an intensity of \(0.40\,\mathrm{W\,m^{-2}}\). None of the energy is absorbed on the way. Calculate the intensity at a distance of 6.0 m, and the ratio of the amplitudes of the waves at 6.0 m and 3.0 m.
A: Intensity is inversely proportional to the square of the distance, so doubling the distance divides it by 4: \(I = 0.40/4\) [C1] \(= 0.10\,\mathrm{W\,m^{-2}}\). [A1] Amplitude is proportional to the square root of intensity, so the amplitude ratio is \(\sqrt{0.10/0.40} = 0.50\). [A1]
Q: [4 marks] ★★ A microphone connected to an oscilloscope shows the sound from a tuning fork. The time-base is \(0.50\,\mathrm{ms\,cm^{-1}}\) and one cycle of the trace is 4.0 cm wide. The speed of sound in air is \(340\,\mathrm{m\,s^{-1}}\). Calculate the frequency of the sound and its wavelength.
A: \(T = 4.0 \times 0.50 = 2.0\,\mathrm{ms}\) [C1] so \(f = 1/(2.0 \times 10^{-3}) = 500\,\mathrm{Hz}\). [A1] \(\lambda = v/f = 340/500\) [C1] \(= 0.68\,\mathrm{m}\). [A1]
Q: [3 marks] ★★ Plane-polarised light of intensity \(6.0\,\mathrm{W\,m^{-2}}\) passes through two polarising filters. The axis of the first is at \(40^\circ\) to the plane of polarisation of the light, and the axis of the second is at \(50^\circ\) to the axis of the first. Calculate the final intensity.
A: \(I_1 = 6.0\cos^2 40^\circ = 3.52\,\mathrm{W\,m^{-2}}\) [C1] then \(I_2 = 3.52\cos^2 50^\circ\) [C1] \(= 1.5\,\mathrm{W\,m^{-2}}\). [A1]
Q: [3 marks] ★★ A radio station broadcasts at a frequency of 94.6 MHz. The speed of electromagnetic waves in free space is \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\). Calculate the wavelength, and state the region of the electromagnetic spectrum in which these waves lie.
A: \(\lambda = c/f = \dfrac{3.00 \times 10^{8}}{94.6 \times 10^{6}}\) [C1] \(= 3.17\,\mathrm{m}\). [A1] This wavelength (more than \(10^{-1}\,\mathrm{m}\)) is in the radio region. [B1]
Q: [5 marks] ★★★ A racing car emits sound of a constant frequency \(f_\text{s}\) as it passes a stationary observer at constant speed. The observer measures a frequency of 1380 Hz as the car approaches and 1020 Hz as it recedes. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Calculate the speed of the car and the frequency \(f_\text{s}\).
H: Write one Doppler equation for each case. They both contain \(f_\text{s}\) and \(v_\text{s}\).
H: Divide one equation by the other so that \(f_\text{s}\) cancels.
A: \(1380 = \dfrac{340f_\text{s}}{340 - v_\text{s}}\) and \(1020 = \dfrac{340f_\text{s}}{340 + v_\text{s}}\) [C1] Dividing: \(\dfrac{1380}{1020} = \dfrac{340 + v_\text{s}}{340 - v_\text{s}}\) [M1] so \(\dfrac{23}{17} = \dfrac{340 + v_\text{s}}{340 - v_\text{s}}\). Then \(23(340 - v_\text{s}) = 17(340 + v_\text{s})\), which gives \(40v_\text{s} = 6 \times 340\) and \(v_\text{s} = 51\,\mathrm{m\,s^{-1}}\). [A1] Then \(f_\text{s} = \dfrac{1380 \times (340 - 51)}{340}\) [C1] \(= 1173\,\mathrm{Hz} \approx 1.2 \times 10^{3}\,\mathrm{Hz}\). [A1]
Q: [7 marks] ★★★ A transverse wave travels along a stretched string in the positive \(x\)-direction. A graph of displacement against distance at \(t = 0\) is a sine curve with amplitude 2.0 mm and crests at \(x = 0.15\,\mathrm{m}\) and \(x = 0.75\,\mathrm{m}\). A graph of displacement against time for one particle shows crests 20 ms apart. (a) Calculate the wavelength, the frequency and the speed of the wave. (b) Particle M is at \(x = 0.30\,\mathrm{m}\) and particle N is at \(x = 0.45\,\mathrm{m}\). Calculate the phase difference between them. (c) State the direction of motion of M at \(t = 0\), with a reason.
H: The wavelength comes from the distance graph and the period from the time graph.
H: Between a crest at 0.15 m and a trough at 0.45 m, the curve slopes downwards, and M is on this part.
A: (a) \(\lambda = 0.75 - 0.15 = 0.60\,\mathrm{m}\) [B1] \(f = \dfrac{1}{T} = \dfrac{1}{0.020}\) [C1] \(= 50\,\mathrm{Hz}\) [A1] \(v = f\lambda = 50 \times 0.60 = 30\,\mathrm{m\,s^{-1}}\) [A1] (b) The separation is \(0.15\,\mathrm{m} = \lambda/4\) [C1] so the phase difference is \(90^\circ\) (\(\pi/2\) rad). [A1] (c) M moves upwards (in the positive displacement direction), because the wave moves to the right and the curve to the left of M is higher than at M. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ (a) A source of sound of frequency \(f_\text{s}\) moves directly towards a stationary observer at speed \(v_\text{s}\). The speed of sound is \(v\). Show that the observed frequency is \(f_\text{o} = f_\text{s}v/(v - v_\text{s})\). (b) Show that, for \(v_\text{s}\) much smaller than \(v\), the fractional change in frequency is approximately \(v_\text{s}/v\). (c) A bat flying at \(6.0\,\mathrm{m\,s^{-1}}\) emits a call at 50 kHz towards a stationary moth. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Calculate the frequency detected by the moth, and compare the fractional change with \(v_\text{s}/v\).
H: In one period of the source, the wavefront moves \(vT\) and the source moves \(v_\text{s}T\).
H: For (b), write \(\dfrac{1}{1 - x} \approx 1 + x\) when \(x\) is small.
A: (a) In one period \(T = 1/f_\text{s}\), the first wavefront moves \(vT\) and the source moves \(v_\text{s}T\), so the next wavefront follows at a distance \(\lambda_\text{o} = (v - v_\text{s})T\). [M1] The waves travel at \(v\), so \(f_\text{o} = \dfrac{v}{\lambda_\text{o}} = \dfrac{v}{(v - v_\text{s})T} = \dfrac{f_\text{s}v}{v - v_\text{s}}\). [A1] (b) \(f_\text{o} = f_\text{s}\dfrac{1}{1 - v_\text{s}/v} \approx f_\text{s}(1 + v_\text{s}/v)\) so \(\dfrac{f_\text{o} - f_\text{s}}{f_\text{s}} \approx \dfrac{v_\text{s}}{v}\). [M1] (c) \(f_\text{o} = \dfrac{50 \times 340}{340 - 6.0}\) [C1] \(= 50.9\,\mathrm{kHz}\). [A1] The fractional change is \(0.898/50 = 1.80\%\), compared with \(v_\text{s}/v = 6.0/340 = 1.76\%\): the approximation is accurate to a few per cent of the shift. [B1]
Q: [6 marks] ★★★ A small dipper in a ripple tank sends circular waves outwards across the water. The power carried by the waves is constant, none is absorbed, and the depth is uniform. (a) Explain why the energy per second crossing each unit length of a circular wavefront falls as \(1/r\), where \(r\) is the distance from the dipper. (b) Deduce how the amplitude of the ripples depends on \(r\). (c) The amplitude at \(r = 4.0\,\mathrm{cm}\) is \(1.2\,\mathrm{mm}\). Calculate the amplitude at \(r = 9.0\,\mathrm{cm}\).
H: The wavefront is a circle of circumference \(2\pi r\), so the same power is spread along a length proportional to \(r\).
H: Intensity is proportional to amplitude squared.
A: (a) The same power \(P\) crosses every circle, and a circle of radius \(r\) has length \(2\pi r\). [B1] The power per unit length is \(P/(2\pi r)\), which is proportional to \(1/r\). [B1] (b) Intensity is proportional to amplitude squared, so \(A^2 \propto 1/r\) [M1] and \(A \propto 1/\sqrt{r}\). [A1] (c) \(\dfrac{A_9}{A_4} = \sqrt{\dfrac{4.0}{9.0}} = \dfrac{2}{3}\) [C1] so \(A_9 = \dfrac{2}{3} \times 1.2 = 0.80\,\mathrm{mm}\). [A1]
:::

:::quiz
? Two points on a wave are a quarter of a wavelength apart. What is their phase difference?
- 45°
+ 90°
- 180°
- 360°
> A quarter of a wavelength is a quarter of a cycle: \(\tfrac14 \times 360^\circ = 90^\circ\). 180° is half a wavelength, and 360° is one whole wavelength (in phase).
? The amplitude of a wave is doubled. What happens to its intensity?
- It doubles.
+ It is multiplied by 4.
- It is multiplied by 8.
- It is unchanged.
> Intensity is proportional to the square of the amplitude, so doubling the amplitude gives \(2^2 = 4\) times the intensity. "It doubles" treats intensity as proportional to amplitude.
? Which of these waves can be polarised?
- Sound waves in air
- A push-pull wave along a spring
+ Visible light
- Ultrasound
> Only transverse waves can be polarised. Sound, ultrasound and waves along a spring (pushed and pulled) are longitudinal. Light is an electromagnetic wave, and all electromagnetic waves are transverse.
? A longitudinal wave is shown as a displacement–distance graph. Where is the centre of a compression?
- At a crest of the graph
- At a trough of the graph
+ Where the graph crosses the axis going downwards
- Where the graph crosses the axis going upwards
> Particles on the left have a positive displacement (to the right) and particles on the right have a negative displacement (to the left), so they move towards the point of zero displacement where the curve slopes down. Crests and troughs are points of maximum displacement, not of bunching.
? A source of sound moves away from a stationary observer. Which statement is correct?
+ The observer receives waves of longer wavelength and lower frequency than the source emits.
- The speed of the waves in the air decreases, so the frequency decreases.
- The source emits a lower frequency because it is moving.
- The observer receives waves of shorter wavelength and lower frequency.
> The speed of sound is set by the air, not the source. The source emits the same frequency, but its motion stretches the wavelength between wavefronts reaching the observer, so \(f = v/\lambda\) falls.
? The distance from a point source is doubled. What happens to the intensity?
- It halves.
+ It falls to one quarter.
- It falls to one eighth.
- It doubles.
> The same power is spread over four times the area (\(4\pi r^2\)), so the intensity is one quarter. A half would be right for ripples spreading out in a circle (in two dimensions), not for a point source in three dimensions.
? Plane-polarised light of intensity \(I_0\) passes through a filter whose axis is at 45° to the plane of polarisation. What is the transmitted intensity?
- \(I_0\)
+ \(I_0/2\)
- \(I_0/4\)
- \(I_0/\sqrt{2}\)
> \(I = I_0\cos^2 45^\circ = I_0 \times \tfrac12\). The factor \(1/\sqrt{2}\) is the amplitude ratio, not the intensity ratio.
? Which statement about electromagnetic waves in free space is correct?
+ They all travel at \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\).
- X-rays travel faster than radio waves because their frequency is higher.
- They are longitudinal waves.
- They need a material medium to travel through.
> In free space, all electromagnetic waves are transverse and travel at the same speed \(c\); frequency and wavelength differ, but their product \(f\lambda\) is always \(c\).
:::

:::checklist What you can now do
- [ ] I can describe wave motion in ropes, springs and ripple tanks, and say that a progressive wave transfers energy but not matter.
- [ ] I can define displacement, amplitude, wavelength, period, frequency, wave speed and phase difference, and find phase differences in degrees and radians.
- [ ] I can read wavelength, period and amplitude from displacement–distance and displacement–time graphs, and tell which way a particle is moving.
- [ ] I can derive and use \(v = f\lambda\).
- [ ] I can use the time-base and y-gain of an oscilloscope to find the frequency and the amplitude of a signal.
- [ ] I can use \(I = P/A\), \(I = P/4\pi r^2\) and \(I \propto A^2\).
- [ ] I can compare transverse and longitudinal waves and interpret graphs of both.
- [ ] I can use \(f_\text{o} = f_\text{s}v/(v \pm v_\text{s})\) for a moving source of sound.
- [ ] I can state that all electromagnetic waves are transverse with speed \(c\) in free space, and recall the wavelength ranges of the regions of the spectrum, including visible light at 400–700 nm.
- [ ] I can explain polarisation, and use Malus's law for one filter or a series of filters.
:::

:::recap
- A progressive wave transfers energy by oscillations of the medium. The particles oscillate about fixed positions and do not travel with the wave.
- A displacement–distance graph gives the wavelength, a displacement–time graph gives the period. Amplitude is the maximum displacement from equilibrium (half the peak-to-peak height).
- Phase difference \(= (x/\lambda) \times 360^\circ = 2\pi x/\lambda\). Whole wavelengths apart: in phase. Half a wavelength apart: antiphase (180°).
- Wave equation \(v = f\lambda\), derived from \(v = \lambda/T\) and \(f = 1/T\). The source fixes the frequency, the medium fixes the speed.
- Oscilloscope: period \(=\) (width of a cycle in divisions) \(\times\) time-base; amplitude \(=\) half the peak-to-peak height \(\times\) y-gain.
- Intensity \(I = P/A\) (W m⁻²); \(I \propto A^2\); for a point source \(I = P/4\pi r^2\), so doubling the distance gives a quarter of the intensity.
- Transverse: oscillations perpendicular to the direction of travel (can be polarised). Longitudinal: oscillations parallel to it (compressions and rarefactions; cannot be polarised).
- Doppler effect for sound with a moving source: \(f_\text{o} = f_\text{s}v/(v \pm v_\text{s})\), minus for approaching (higher frequency), plus for receding (lower).
- All electromagnetic waves are transverse and travel at \(c = 3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\) in free space. Visible light is about 400–700 nm.
- Malus's law: \(I = I_0\cos^2\theta\) for plane-polarised light through a filter. Crossed filters transmit nothing, and a third filter at 45° between them lets \(I_0/4\) through.
:::

:::links
- explore: [Wave on a String](https://phet.colorado.edu/en/simulations/wave-on-a-string) · PhET · change frequency, amplitude and damping and see a wave travel along a string
- explore: [Waves Intro](https://phet.colorado.edu/en/simulations/waves-intro) · PhET · compare water, sound and light waves
- explore: [Sound Waves](https://phet.colorado.edu/en/simulations/sound-waves) · PhET · see compressions and rarefactions and hear how frequency changes pitch
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the waves questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Superposition](#phys.superposition)
