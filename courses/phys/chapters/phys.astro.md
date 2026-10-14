@chapter phys.astro
@title Astronomy and cosmology
@level a2
@paper CAIE P4 (A Level)
@time 5–7 hours
@summary How light alone tells us the distance, temperature, size and speed of stars and galaxies: luminosity and the inverse square law, standard candles, Wien's law and the Stefan–Boltzmann law, redshift, and Hubble's law with the Big Bang it leads to.

:::why
Nobody has visited a star, yet astronomers know how far away the stars are, how hot, how big and how fast they are moving. All of it comes from the light that arrives at a telescope, read with the physics you already know: intensity, the electromagnetic spectrum, black-body radiation and the Doppler effect. The same short chain of reasoning also leads to one of the biggest conclusions in science: the Universe is expanding, and it began in a hot, dense state.
:::

**Before you start**, you need intensity and the Doppler effect from [Waves](#phys.waves), line spectra from [Quantum physics](#phys.quantum), the kelvin scale from [Temperature](#phys.temperature), and orbits from [Gravitational fields](#phys.gravity).

:::try Warm-up
Q: A beam of light of power 3.0 W falls normally on a surface of area 0.50 m². What is the intensity? (from [Waves](#phys.waves))
A: Intensity is power per unit area: \(I = P/A = 3.0/0.50 = 6.0\,\mathrm{W\,m^{-2}}\).
Q: Why does hot hydrogen gas emit light only at certain wavelengths? (from [Quantum physics](#phys.quantum))
A: Its electrons have only certain energy levels. When an electron falls from one level to a lower one, it emits a photon whose energy equals the difference, so each pair of levels gives one fixed wavelength, a line.
Q: An ambulance siren sounds lower in pitch once the ambulance has passed you and is moving away. Explain why. (from [Waves](#phys.waves))
A: The source moves away from you, so each wavefront is emitted from further away than the one before and the waves arrive stretched out. The observed wavelength is longer, so the observed frequency is lower.
:::

## Luminosity and radiant flux intensity

A star pours out energy in every direction. Two different quantities describe this, and the whole chapter depends on keeping them apart: how much power the star **emits**, and how much of it **reaches** a detector.

:::def Luminosity
The total power of electromagnetic radiation emitted by a star.
:::

Luminosity \(L\) belongs to the star and is measured in watts. It does not depend on where you are. The Sun has \(L = 3.83 \times 10^{26}\,\mathrm{W}\), and other stars range from a small fraction of this to hundreds of thousands of times more.

:::def Radiant flux intensity
The radiant power passing normally through unit area. Its unit is \(\mathrm{W\,m^{-2}}\).
:::

Radiant flux intensity \(F\) (also called flux or apparent brightness) belongs to the **measurement**: it is the intensity of the starlight at the detector, and it falls with distance. Imagine a sphere centred on the star with a radius equal to the distance \(d\) of the detector. The star's radiation is spread uniformly over the sphere, whose area is \(4\pi d^2\), and the whole luminosity passes through it.

:::formula Inverse square law for radiant flux intensity
\[F = \frac{L}{4\pi d^2}\]
\(F\): radiant flux intensity at the observer (\(\mathrm{W\,m^{-2}}\)) · \(L\): luminosity of the star (W) · \(d\): distance from the star to the observer (m). This assumes that nothing absorbs the light on the way.
:::

:::html
<figure class="fig"><svg viewBox="20 40 280 200" role="img" aria-label="A star on the left sends light outwards in a cone that passes through a small screen of area A at distance d and a larger screen of area 4A at distance 2d. Dimension arrows show d and 2d."><path class="ln-m thin" d="M60 120L260 80M60 120L260 160"/><circle class="fa s-ink sw1" cx="60" cy="120" r="10"/><path class="ln thick" d="M160 100V140M260 80V160"/><path class="c1" d="M72 120H250" marker-end="url(#ah-phys)"/><text class="tl tc" x="160" y="82">area A</text><text class="tl tc" x="260" y="62">area 4A</text><text class="tl tc" x="60" y="150">star (L)</text><path class="ln-m thin dash" d="M60 160V228M160 140V195M260 160V228"/><path class="c1" d="M110 190H66" marker-end="url(#ah-phys)"/><path class="c1" d="M110 190H156" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="110" y="182">d</text><path class="c1" d="M160 225H66" marker-end="url(#ah-phys)"/><path class="c1" d="M160 225H256" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="160" y="217">2d</text></svg><figcaption>At twice the distance the same light is spread over four times the area, so the radiant flux intensity is a quarter. The cone is the same light seen at two distances.</figcaption></figure>
:::

Double the distance, and \(d^2\) becomes four times larger, so \(F\) falls to a quarter: this is the **inverse square law**. Increase the distance by a factor of 10 and the flux falls by a factor of 100. Use the same law for any point source of light.

:::eg Calculate the radiant flux intensity at the Earth from the Sun. (Luminosity of the Sun: \(3.83 \times 10^{26}\,\mathrm{W}\). Distance from the Sun to the Earth: \(1.50 \times 10^{11}\,\mathrm{m}\).)
\[F = \frac{L}{4\pi d^2} = \frac{3.83 \times 10^{26}}{4\pi \times (1.50 \times 10^{11})^2}\] [C1]
\[F = 1.35 \times 10^{3}\,\mathrm{W\,m^{-2}}\] [A1]
This is the **solar constant**: each square metre facing the Sun, above the atmosphere, receives about 1.35 kW.
:::

:::eg Mars is \(2.28 \times 10^{11}\,\mathrm{m}\) from the Sun. Find the radiant flux intensity of sunlight at Mars.
\[F = \frac{3.83 \times 10^{26}}{4\pi \times (2.28 \times 10^{11})^2}\] [C1] \(= 5.86 \times 10^{2}\,\mathrm{W\,m^{-2}}\). [A1]
Check with the inverse square law: Mars is 1.52 times as far as the Earth, so the flux is the Earth value divided by \(1.52^2\): \(1.355 \times 10^{3}/2.31 \approx 5.9 \times 10^{2}\,\mathrm{W\,m^{-2}}\).
:::

:::warn L is not F
Luminosity is what the star emits and is the same wherever you stand. Radiant flux intensity is what arrives, and it depends on distance. A star can look faint because it is dim (small \(L\)) or because it is far away (large \(d\)). Telling these apart is the whole point of the next section.
:::

## Standard candles

Measuring \(F\) is easy: point a detector at the star. Distance is hard. But the inverse square law gives a way to find \(d\), if the luminosity is known.

:::def Standard candle
An astronomical object of known luminosity.
:::

If you can find a standard candle in a distant galaxy, you measure its flux \(F\) and rearrange the law:
\[d = \sqrt{\frac{L}{4\pi F}}\]
A dim standard candle is far away and a bright one is near, which works like judging how far away a car is at night from its headlights, if you know they are 60 W bulbs.

The two standard candles you need to describe are these.

- **Cepheid variable stars** pulse regularly, getting brighter and fainter with a period from a few days to a few months. There is a fixed relation between the period and the luminosity: the longer the period, the more luminous the star. So you measure the period, read off the luminosity from the relation, and measure \(F\) to find the distance.
- **Type Ia supernovae** are the explosions of a certain kind of white dwarf star. They all reach about the same peak luminosity, and that luminosity is so large that these explosions can be seen in galaxies billions of light-years away.

Distances in astronomy are built up in steps, called the **distance ladder**: nearby stars have distances measured directly and are used to find the luminosity of Cepheids, which then give the distances to nearby galaxies, and those are used to check the supernovae that reach further. Each step depends on the one below it, so an error low on the ladder spreads upwards. Dust between the stars also dims the light and makes a candle seem further away than it is.

:::eg A Cepheid variable has a luminosity of \(3.0 \times 10^{30}\,\mathrm{W}\), found from its period. Its radiant flux intensity at the Earth is \(1.2 \times 10^{-12}\,\mathrm{W\,m^{-2}}\). Calculate its distance in metres and in light-years. (1 light-year = \(9.46 \times 10^{15}\,\mathrm{m}\).)
\[d = \sqrt{\frac{L}{4\pi F}} = \sqrt{\frac{3.0 \times 10^{30}}{4\pi \times 1.2 \times 10^{-12}}}\] [C1]
\[d = 4.5 \times 10^{20}\,\mathrm{m}\] [A1]
In light-years: \(\dfrac{4.46 \times 10^{20}}{9.46 \times 10^{15}} = 4.7 \times 10^{4}\) light-years, using the unrounded distance. [B1]
:::

## Stellar temperatures: black-body radiation and Wien's law

Stars are hot, dense balls of gas whose surfaces radiate very nearly like an ideal **black body**, an object that absorbs all the radiation that falls on it and emits a continuous spectrum that depends only on its temperature. If you look at a heated metal bar, you see it go from dull red to orange to white as it gets hotter: the same thing happens for a star.

The graph of intensity against wavelength for a black body is a hump. Two things happen as the temperature rises: the whole curve gets **higher** (more power at every wavelength) and the peak moves to **shorter wavelengths**.

:::html
<figure class="fig"><svg viewBox="35 20 505 262" role="img" aria-label="Intensity against wavelength for black bodies at 5000, 6000 and 7000 kelvin. Each curve is a hump. The hotter the body the higher the hump and the shorter the wavelength of its peak. The visible band from 400 to 700 nanometres is shaded."><rect class="fm" x="180" y="30" width="90" height="200"/><path class="ax" d="M60 230H520M60 230V40"/><path class="c1 sw2" d="M98 230L105 230L112 230L120 229L128 229L135 227L142 225L150 222L158 218L165 215L172 212L180 208L188 206L195 203L202 201L210 200L218 199L225 199L232 198L240 198L248 199L255 199L262 200L270 201L278 202L285 203L292 204L300 205L308 206L315 207L322 208L330 209L360 212L390 216L420 218L450 220L480 222L510 223"/><path class="c2 sw2 dash" d="M98 230L105 230L112 228L120 224L128 218L135 209L142 199L150 189L158 179L165 171L172 164L180 158L188 155L195 152L202 151L210 152L218 153L225 154L232 157L240 159L248 162L255 165L262 168L270 171L278 174L285 177L292 180L300 183L308 185L315 188L322 190L330 193L360 201L390 207L420 211L450 215L480 218L510 220"/><path class="c3 sw2" d="M98 229L105 226L112 216L120 198L128 175L135 149L142 124L150 102L158 84L165 72L172 64L180 60L188 60L195 63L202 67L210 73L218 80L225 87L232 95L240 103L248 110L255 118L262 125L270 132L278 138L285 144L292 150L300 156L308 161L315 165L322 169L330 173L360 187L390 197L420 204L450 209L480 214L510 217"/><path class="ln-m thin dash" d="M184 60V230M202 151V230M234 198V230"/><path class="ax" d="M60 230V234M210 230V234M360 230V234M510 230V234"/><text class="tl" x="68" y="38">intensity</text><text class="tl te" x="176" y="54">7000 K</text><text class="tl tc" x="215" y="143">6000 K</text><text class="tl tc" x="240" y="190">5000 K</text><text class="tl tc" x="225" y="266">visible light</text><text class="ts tc" x="60" y="249">0</text><text class="ts tc" x="210" y="249">500</text><text class="ts tc" x="360" y="249">1000</text><text class="ts tc" x="510" y="249">1500</text><text class="tl te" x="520" y="268">λ / nm</text></svg><figcaption>Black-body curves for three temperatures, on one scale. The dashed vertical lines mark the peaks, at 580 nm, 483 nm and 414 nm for 5000 K, 6000 K and 7000 K. A hotter body is brighter at every wavelength and its peak moves to shorter wavelengths. The shaded band is the visible spectrum (400 to 700 nm).</figcaption></figure>
:::

The position of the peak follows a simple law.

:::def Wien's displacement law
The wavelength at which the intensity of radiation from a black body is a maximum is inversely proportional to its thermodynamic temperature: \(\lambda_{\max} \propto 1/T\), that is \(\lambda_{\max}T = \text{constant}\).
:::

:::formula Wien's displacement law
\[\lambda_{\max} T = 2.9 \times 10^{-3}\,\mathrm{m\,K}\]
\(\lambda_{\max}\): wavelength of peak intensity (m) · \(T\): thermodynamic temperature of the surface (K). The constant is not on the data sheet: a question gives it, or gives a reference star to compare with.
:::

Hot stars are blue-white (the peak is at a short wavelength, in the blue or the ultraviolet) and cool stars are red (the peak is in the red or the infrared). The Sun has its peak near 500 nm, in the middle of the visible spectrum.

:::eg The Sun's radiation has its peak at \(\lambda_{\max} = 5.0 \times 10^{-7}\,\mathrm{m}\). Estimate the temperature of its surface.
\[T = \frac{2.9 \times 10^{-3}}{\lambda_{\max}} = \frac{2.9 \times 10^{-3}}{5.0 \times 10^{-7}}\] [C1]
\[T = 5.8 \times 10^{3}\,\mathrm{K}\] [A1]
:::

:::warn Kelvin only
Wien's law uses the **thermodynamic temperature**. Never put °C into it, and never leave an answer in kelvin when the question asks for °C (subtract 273). A temperature of 5800 K is about 5500 °C, which does not matter at this level, but an answer of 5800 °C used in the next formula would be wrong.
:::

:::eg Star X has a surface temperature of 3000 K. Find the wavelength of its peak and say what colour it looks.
\[\lambda_{\max} = \frac{2.9 \times 10^{-3}}{3000} = 9.7 \times 10^{-7}\,\mathrm{m} = 970\,\mathrm{nm}\] [C1] [A1]
This is in the infrared, beyond the red end of the visible spectrum, so most of the light that the eye can see is red and the star looks red. [B1]
:::

## The Stefan–Boltzmann law and the radius of a star

A hotter surface radiates far more power per square metre. The black-body result is that each square metre of the surface radiates a power \(\sigma T^4\), where \(\sigma\) is the Stefan–Boltzmann constant, \(5.67 \times 10^{-8}\,\mathrm{W\,m^{-2}\,K^{-4}}\) from the data sheet. A star is a sphere of radius \(r\), whose surface area is \(4\pi r^2\), so its luminosity is the power per unit area times the area.

:::def Stefan–Boltzmann law
The total power radiated per unit surface area of a black body is proportional to the fourth power of its thermodynamic temperature. For a star (a spherical black body) the luminosity is \(L = 4\pi\sigma r^2T^4\).
:::

:::formula Stefan–Boltzmann law for a star
\[L = 4\pi\sigma r^2T^4\]
\(L\): luminosity (W) · \(\sigma\): Stefan–Boltzmann constant, \(5.67 \times 10^{-8}\,\mathrm{W\,m^{-2}\,K^{-4}}\) · \(r\): radius of the star (m) · \(T\): thermodynamic temperature of its surface (K). The power per unit area is \(\sigma T^4\).
:::

The fourth power makes the law very sensitive. Double the temperature, with the same radius, and the luminosity rises by \(2^4 = 16\) times. Double the radius, and the luminosity rises by \(2^2 = 4\) times.

:::eg Calculate the luminosity of the Sun, using a surface temperature of 5800 K and a radius of \(6.96 \times 10^{8}\,\mathrm{m}\).
\[L = 4\pi\sigma r^2T^4 = 4\pi \times 5.67 \times 10^{-8} \times (6.96 \times 10^{8})^2 \times 5800^4\] [C1]
\[L = 3.9 \times 10^{26}\,\mathrm{W}\] [A1]
The accepted value is \(3.83 \times 10^{26}\,\mathrm{W}\). The small difference arises because 5800 K is a rounded temperature: the answer is very sensitive to \(T\), since \(T^4\) magnifies a 1% error in \(T\) into a 4% error in \(L\).
:::

### Estimating the radius of a star

A star is too far away for its radius to be measured directly, but it can be estimated by combining what you now know.

:::steps
1. Find \(T\) from the wavelength of peak intensity, using Wien's displacement law.
2. Find \(L\) from the flux \(F\) and distance \(d\), using \(L = 4\pi d^2F\), if \(L\) is not given.
3. Rearrange the Stefan–Boltzmann law: \(r = \sqrt{\dfrac{L}{4\pi\sigma T^4}}\).
:::

:::eg A star has a peak wavelength of 290 nm and a luminosity of \(4.0 \times 10^{28}\,\mathrm{W}\). Estimate its radius, and compare it with the radius of the Sun (\(6.96 \times 10^{8}\,\mathrm{m}\)).
\[T = \frac{2.9 \times 10^{-3}}{2.9 \times 10^{-7}} = 1.0 \times 10^{4}\,\mathrm{K}\] [C1]
\[r^2 = \frac{L}{4\pi\sigma T^4} = \frac{4.0 \times 10^{28}}{4\pi \times 5.67 \times 10^{-8} \times (1.0 \times 10^{4})^4}\] [C1]
\[r = 2.4 \times 10^{9}\,\mathrm{m}\] [A1]
This is \(2.37 \times 10^{9}/6.96 \times 10^{8} = 3.4\) times the radius of the Sun. [B1]
:::

Two stars can be compared by ratios, and this is quicker and safer than working with every constant. For the same luminosity, \(r^2T^4\) is the same, so \(r \propto 1/T^2\). A star at half the temperature of another with the same luminosity must have four times the radius: red giants are cool but huge, so they are very luminous even though each square metre of their surface radiates little.

Try the widget below. Choose a preset or set the temperature and radius yourself, and watch the peak wavelength, the luminosity and the colour. Double the temperature and see the peak move to half the wavelength while \(L\) goes up 16 times; double the radius and see \(L\) go up four times.

:::html
<div class="widget" data-w="phys-star" data-t="5800" data-r="1"></div>
:::

:::exam Radius questions
Three steps in order: \(T\) from \(\lambda_{\max}\), \(L\) from \(F\) and \(d\) (if needed), then \(r\) from the Stefan–Boltzmann law. The marks go to each substitution, so write the formula before you put numbers in. Check that you have used the **radius**, not the diameter, in \(4\pi r^2\), and that \(T\) is in kelvin and raised to the fourth power.
:::

:::eg Spot the error: the Sun has a surface temperature of 5800 K and a diameter of \(1.39 \times 10^{9}\,\mathrm{m}\). Calculate its luminosity.
A student wrote this answer.

Line 1: \(L = 4\pi\sigma r^2T^4\)
Line 2: \(L = 4\pi \times 5.67 \times 10^{-8} \times (1.39 \times 10^{9})^2 \times 5800^4\)
Line 3: \(L = 1.6 \times 10^{27}\,\mathrm{W}\)

Line 1 is the correct formula. [C1] **Line 2 uses the diameter where the radius is needed, so the area is four times too large and the answer is four times too big.** [A0]

Correct working: \(r = 1.39 \times 10^{9}/2 = 6.95 \times 10^{8}\,\mathrm{m}\), so \(L = 4\pi \times 5.67 \times 10^{-8} \times (6.95 \times 10^{8})^2 \times 5800^4 = 3.9 \times 10^{26}\,\mathrm{W}\). [A1]

Check: the Sun's luminosity is known to be about \(3.8 \times 10^{26}\,\mathrm{W}\), so \(10^{27}\) should have looked wrong at once.
:::

## Redshift

The spectrum of a star or a galaxy also tells us its motion. As in [Quantum physics](#phys.quantum), a gas of hydrogen emits or absorbs light at exact wavelengths: the lines of its spectrum. Light from a distant galaxy shows the same pattern of lines, but all of them are at **longer wavelengths** than in a laboratory.

:::def Redshift
The increase in the observed wavelength of radiation from a source that is moving away from the observer, compared with the wavelength emitted. The lines in the spectrum move towards the red end.
:::

This is the Doppler effect for light, as for the ambulance in the warm-up. A source moving away stretches the waves, so the wavelength gets longer and the frequency gets lower.

:::html
<figure class="fig"><svg viewBox="5 20 545 220" role="img" aria-label="Two spectrum strips between 400 and 700 nanometres. The upper strip is the laboratory hydrogen spectrum with four dark lines, labelled H alpha, H beta, H gamma and H delta. The lower strip is from a distant galaxy with the same four lines each moved to a longer wavelength, shown with an arrow for the H alpha line."><rect class="fm s-mute sw1" x="100" y="50" width="420" height="40"/><rect class="fi" x="113" y="50" width="2" height="40"/><rect class="fi" x="147" y="50" width="2" height="40"/><rect class="fi" x="220" y="50" width="2" height="40"/><rect class="fi" x="458" y="50" width="2" height="40"/><rect class="fm s-mute sw1" x="100" y="130" width="420" height="40"/><rect class="fi" x="130" y="130" width="2" height="40"/><rect class="fi" x="165" y="130" width="2" height="40"/><rect class="fi" x="240" y="130" width="2" height="40"/><rect class="fi" x="485" y="130" width="2" height="40"/><text class="tl te" x="92" y="74">laboratory</text><text class="tl te" x="92" y="154">galaxy</text><text class="tl tc" x="114" y="40">Hδ</text><text class="tl tc" x="148" y="40">Hγ</text><text class="tl tc" x="221" y="40">Hβ</text><text class="tl tc" x="459" y="40">Hα</text><path class="ln-m thin dash" d="M459 90V130"/><path class="c1" d="M459 112H482" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="472" y="104">Δλ</text><path class="ax" d="M100 190H520"/><path class="ax" d="M100 190V194M240 190V194M380 190V194M520 190V194"/><text class="ts tc" x="100" y="208">400</text><text class="ts tc" x="240" y="208">500</text><text class="ts tc" x="380" y="208">600</text><text class="ts tc" x="520" y="208">700</text><text class="tl te" x="520" y="226">λ / nm</text></svg><figcaption>The same four hydrogen lines in the laboratory (upper strip) and in the light of a distant galaxy (lower strip). Every line is displaced to a longer wavelength by the same fraction, here Δλ/λ = 0.030, so the line at 656.3 nm is observed at 676.0 nm.</figcaption></figure>
:::

For a source moving away at a speed \(v\) much smaller than \(c\), the fractional change in wavelength and frequency equals \(v/c\).

:::formula Redshift
\[\frac{\Delta\lambda}{\lambda} \approx \frac{\Delta f}{f} \approx \frac{v}{c}\]
\(\Delta\lambda\): observed wavelength minus emitted wavelength (m) · \(\lambda\): emitted (laboratory) wavelength · \(\Delta f\): size of the change in frequency · \(v\): recession speed of the source (\(\mathrm{m\,s^{-1}}\)) · \(c\): speed of light. Valid only when \(v \ll c\).
:::

:::eg In the spectrum of a galaxy, the hydrogen line of wavelength 656.3 nm in the laboratory is observed at 663.0 nm. Find the speed of the galaxy relative to the Earth.
\(\Delta\lambda = 663.0 - 656.3 = 6.7\,\mathrm{nm}\). [C1]
\[v = c \times \frac{\Delta\lambda}{\lambda} = 3.00 \times 10^{8} \times \frac{6.7}{656.3}\] [C1]
\[v = 3.1 \times 10^{6}\,\mathrm{m\,s^{-1}}\] [A1]
The galaxy is moving away, because the wavelength has increased. The unrounded value is \(3.06 \times 10^{6}\,\mathrm{m\,s^{-1}}\), which is 1.0% of the speed of light, so \(v \ll c\) and the approximation is fair. The wavelengths are in the same unit, so they cancel.
:::

:::eg A spectral line from another galaxy has \(\Delta\lambda/\lambda = 0.020\). How fast is it receding?
\[v = 0.020 \times 3.00 \times 10^{8} = 6.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\] [C1] [A1]
:::

## Hubble's law and the expanding Universe

When Edwin Hubble measured the redshifts of many galaxies in the 1920s and compared them with their distances (found from standard candles), two things stood out. Almost all galaxies show a redshift, so almost all are moving away from us. And the further away a galaxy is, the larger its redshift, so the faster it is receding.

:::def Hubble's law
The recession speed of a galaxy is (approximately) proportional to its distance from the observer: \(v \approx H_0d\), where \(H_0\) is the Hubble constant.
:::

:::formula Hubble's law
\[v \approx H_0d\]
\(v\): recession speed (\(\mathrm{m\,s^{-1}}\)) · \(d\): distance to the galaxy (m) · \(H_0\): the Hubble constant, \(\approx 2.3 \times 10^{-18}\,\mathrm{s^{-1}}\) (about \(70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) in astronomers' units). Only SI units are required in calculations.
:::

The unit of \(H_0\) is \(\mathrm{m\,s^{-1}}\) divided by \(\mathrm{m}\), which is \(\mathrm{s^{-1}}\).

:::html
<figure class="fig"><svg viewBox="35 4 470 292" role="img" aria-label="Recession speed against distance for eight galaxies. The points scatter slightly about a straight line through the origin. A triangle drawn on the line shows how the gradient, which is the Hubble constant, is found."><path class="ax" d="M70 250H480M70 250V30"/><path class="ax" d="M70 250V254M170 250V254M270 250V254M370 250V254M470 250V254M70 250H66M70 206H66M70 162H66M70 118H66M70 74H66M70 30H66"/><path class="c1 sw2" d="M70 250L470 48"/><circle class="fi" cx="110" cy="221" r="4"/><circle class="fi" cx="160" cy="215" r="4"/><circle class="fi" cx="200" cy="171" r="4"/><circle class="fi" cx="250" cy="166" r="4"/><circle class="fi" cx="290" cy="127" r="4"/><circle class="fi" cx="340" cy="127" r="4"/><circle class="fi" cx="380" cy="87" r="4"/><circle class="fi" cx="430" cy="76" r="4"/><path class="ln-m thin dash" d="M170 199H370M370 199V98"/><text class="tl tc" x="270" y="215">Δd</text><text class="tl ti" x="378" y="152">Δv</text><text class="tl" x="400" y="112">line: v = H₀d</text><text class="ts tc" x="70" y="268">0</text><text class="ts tc" x="170" y="268">1</text><text class="ts tc" x="270" y="268">2</text><text class="ts tc" x="370" y="268">3</text><text class="ts tc" x="470" y="268">4</text><text class="ts te" x="62" y="254">0</text><text class="ts te" x="62" y="210">2</text><text class="ts te" x="62" y="166">4</text><text class="ts te" x="62" y="122">6</text><text class="ts te" x="62" y="78">8</text><text class="ts te" x="62" y="34">10</text><text class="tl" x="76" y="22">v / 10⁶ m s⁻¹</text><text class="tl te" x="480" y="286">d / 10²⁴ m</text></svg><figcaption>Recession speed against distance for eight galaxies (illustrative data). The points lie close to a straight line through the origin, so v is proportional to d. The gradient Δv/Δd is the Hubble constant, here 2.3 × 10⁻¹⁸ s⁻¹.</figcaption></figure>
:::

:::eg A galaxy has \(v = 3.06 \times 10^{6}\,\mathrm{m\,s^{-1}}\) (from the previous example, using the unrounded value). Use Hubble's law with \(H_0 = 2.3 \times 10^{-18}\,\mathrm{s^{-1}}\) to find its distance.
\[d = \frac{v}{H_0} = \frac{3.06 \times 10^{6}}{2.3 \times 10^{-18}}\] [C1]
\[d = 1.3 \times 10^{24}\,\mathrm{m}\] [A1]
This is \(1.3 \times 10^{24}/9.46 \times 10^{15} = 1.4 \times 10^{8}\) light-years. Redshift gives a way to measure distances that standard candles cannot reach.
:::

### Why the Universe is expanding

If galaxies were simply scattered at random, some would be coming towards us and some going away. Seeing almost all of them moving away, with speed proportional to distance, means that the **space between the galaxies is expanding**. It is not that the galaxies are flying outwards through space from a centre: space itself stretches, and carries them apart. A pattern with speed proportional to distance is the pattern you get from a stretching rubber sheet marked with dots. Seen from any dot, the other dots recede, the far ones faster than the near ones. So every observer in every galaxy would see the same thing, and there is no centre.

:::analogy
Draw dots on a balloon and inflate it. As the balloon grows, every dot moves away from every other dot, and a dot twice as far from yours moves away twice as fast. No dot is the centre of the expansion (the centre of the balloon is not on its surface), and the dots themselves do not grow. The galaxies are like the dots; the stretching rubber is space.
:::

### The Big Bang and the age of the Universe

Run the expansion backwards in time. The galaxies come closer and closer together, and a long time ago all the matter was in a very small, very hot and very dense region. The Universe began in a hot, dense state and has been expanding ever since: the **Big Bang theory**. (The cosmic microwave background, a faint glow of microwaves that reaches us from every direction, is further evidence for it, though you are not asked about it.)

A rough age follows from Hubble's law. Suppose each galaxy has always moved at its present speed.

:::proof An estimate of the age of the Universe
A galaxy at distance \(d\) is now moving away at speed \(v\), and has been all the time since the Big Bang, when it was at our position (\(d = 0\)).
The time taken is \(t = d/v\).
Hubble's law gives \(v = H_0d\), so \(t = \dfrac{d}{H_0d} = \dfrac{1}{H_0}\).
The distance cancels, so every galaxy gives the same age, which is why the estimate makes sense.
The real expansion has speeded up and slowed down over time, so \(1/H_0\) is only an estimate.
:::

:::eg Estimate the age of the Universe from \(H_0 = 2.3 \times 10^{-18}\,\mathrm{s^{-1}}\). (1 year = \(3.16 \times 10^{7}\,\mathrm{s}\).)
\[t = \frac{1}{H_0} = \frac{1}{2.3 \times 10^{-18}} = 4.3 \times 10^{17}\,\mathrm{s}\] [C1]
\[t = \frac{4.35 \times 10^{17}}{3.16 \times 10^{7}} = 1.4 \times 10^{10}\,\text{years}\] [A1]
About fourteen billion years.
:::

:::warn Common misconceptions
"The Universe is expanding into empty space from a point" is wrong: the Big Bang did not happen at one place in space that we could point to, it happened everywhere. Galaxies are carried apart by the stretching of space, and their sizes, and the sizes of atoms, do not grow. Redshift is also **observed minus emitted** wavelength: \(\Delta\lambda = \lambda_{\text{observed}} - \lambda_{\text{emitted}}\), so it is positive for a receding source.
:::

:::board
AQA's Astrophysics is an option topic. OCR includes cosmology in its core content, with Hubble's law, parallax and the parsec; Cambridge needs only the content in this chapter, with distances in metres or light-years.
:::

:::try Start easy, finish at exam standard
Q: A star of luminosity \(2.0 \times 10^{27}\,\mathrm{W}\) is at a distance of \(1.0 \times 10^{17}\,\mathrm{m}\). Find the radiant flux intensity at the Earth.
A: \(F = \dfrac{L}{4\pi d^2} = \dfrac{2.0 \times 10^{27}}{4\pi \times (1.0 \times 10^{17})^2} = 1.6 \times 10^{-8}\,\mathrm{W\,m^{-2}}\).
Q: The peak wavelength of a star's radiation is 725 nm. Find its surface temperature.
A: \(T = \dfrac{2.9 \times 10^{-3}}{7.25 \times 10^{-7}} = 4.0 \times 10^{3}\,\mathrm{K}\).
Q: Find the power radiated per unit area of the surface of a star at 6000 K.
A: Power per unit area \(= \sigma T^4 = 5.67 \times 10^{-8} \times 6000^4 = 7.3 \times 10^{7}\,\mathrm{W\,m^{-2}}\).
Q: A star has radius \(1.4 \times 10^{9}\,\mathrm{m}\) and surface temperature 5000 K. Find its luminosity.
A: \(L = 4\pi\sigma r^2T^4\), so \[L = 4\pi \times 5.67 \times 10^{-8} \times (1.4 \times 10^{9})^2 \times 5000^4 = 8.7 \times 10^{26}\,\mathrm{W}\]
Q: A galaxy's spectral line has \(\Delta\lambda/\lambda = 0.0050\). Find its recession speed.
A: \(v = c \times 0.0050 = 3.00 \times 10^{8} \times 0.0050 = 1.5 \times 10^{6}\,\mathrm{m\,s^{-1}}\).
Q: A galaxy is \(2.0 \times 10^{24}\,\mathrm{m}\) away. Use \(H_0 = 2.3 \times 10^{-18}\,\mathrm{s^{-1}}\) to find its recession speed.
A: \(v = H_0d = 2.3 \times 10^{-18} \times 2.0 \times 10^{24} = 4.6 \times 10^{6}\,\mathrm{m\,s^{-1}}\).
Q: Star A has 4 times the luminosity of star B and is twice as far from the Earth. Compare the radiant flux intensities at the Earth.
A: \(F \propto L/d^2\), so \(F_A/F_B = 4/2^2 = 1\). The two stars look equally bright.
Q: Show that the unit of the Hubble constant is \(\mathrm{s^{-1}}\).
A: \(H_0 = v/d\), so its unit is \(\mathrm{m\,s^{-1}}/\mathrm{m} = \mathrm{s^{-1}}\).
Q: A type Ia supernova of luminosity \(1.0 \times 10^{36}\,\mathrm{W}\) is observed with a flux of \(2.0 \times 10^{-15}\,\mathrm{W\,m^{-2}}\). Find the distance of its galaxy in metres and in light-years.
A: \(d = \sqrt{\dfrac{L}{4\pi F}} = \sqrt{\dfrac{1.0 \times 10^{36}}{4\pi \times 2.0 \times 10^{-15}}} = 6.3 \times 10^{24}\,\mathrm{m}\), which is \(6.3 \times 10^{24}/9.46 \times 10^{15} = 6.7 \times 10^{8}\) light-years.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define the luminosity of a star.
A: The total power of electromagnetic radiation emitted by the star. [B1]
Q: [3 marks] ★ (a) State what is meant by a standard candle. (b) Describe how a standard candle is used to find the distance to a galaxy.
A: (a) An astronomical object of known luminosity. [B1] (b) Measure the radiant flux intensity \(F\) received from the candle. [B1] Then use \(F = L/(4\pi d^2)\) with the known luminosity \(L\) to calculate the distance \(d\). [B1]
Q: [2 marks] ★ The radiant flux intensity from a star at the Earth is \(4.0 \times 10^{-9}\,\mathrm{W\,m^{-2}}\). Calculate the radiant flux intensity from the same star at three times the distance.
A: \(F \propto 1/d^2\), so the flux is divided by \(3^2 = 9\): \(\dfrac{4.0 \times 10^{-9}}{9}\) [C1] \(= 4.4 \times 10^{-10}\,\mathrm{W\,m^{-2}}\). [A1]
Q: [2 marks] ★ A star's radiation has a maximum intensity at a wavelength of \(2.4 \times 10^{-7}\,\mathrm{m}\). Estimate the surface temperature of the star.
A: \(T = \dfrac{2.9 \times 10^{-3}}{2.4 \times 10^{-7}}\) [C1] \(= 1.2 \times 10^{4}\,\mathrm{K}\). [A1]
Q: [4 marks] ★★ Two stars X and Y have the same luminosity. The surface temperature of X is 6000 K and that of Y is 3000 K. (a) Calculate the ratio of the radius of Y to the radius of X. (b) State and explain which star looks redder.
A: (a) \(L = 4\pi\sigma r^2T^4\) is the same, so \(r^2T^4\) is the same and \(r \propto 1/T^2\). [C1] \(\dfrac{r_Y}{r_X} = \left(\dfrac{6000}{3000}\right)^2 = 4.0\). [A1] (b) Star Y looks redder. [B1] Its surface is cooler, so by Wien's law its peak wavelength is longer. [B1]
Q: [3 marks] ★★ A line in the spectrum of a galaxy has an emitted wavelength of 486.1 nm and is observed at 491.9 nm. Calculate the speed of the galaxy relative to the Earth and state its direction of motion.
A: \(\Delta\lambda = 491.9 - 486.1 = 5.8\,\mathrm{nm}\), so \(v = c\,\dfrac{\Delta\lambda}{\lambda} = 3.00 \times 10^{8} \times \dfrac{5.8}{486.1}\) [C1] \(= 3.6 \times 10^{6}\,\mathrm{m\,s^{-1}}\). [A1] The wavelength has increased, so the galaxy is moving away from the Earth. [B1]
Q: [4 marks] ★★ Explain how observations of redshift from galaxies lead to the Big Bang theory.
A: The spectral lines of light from distant galaxies are at longer wavelengths than in the laboratory, so the galaxies are moving away from us. [B1] The redshift, and so the speed, is greater for galaxies that are further away (Hubble's law: \(v \approx H_0d\)). [B1] This means that space is expanding, so the galaxies are moving apart. [B1] Going back in time, the galaxies were closer together, so the Universe must have started from a very small, hot, dense state: the Big Bang. [B1]
Q: [6 marks] (#phys.temperature) ★★★ The light of a star has its maximum intensity at a wavelength of \(4.6 \times 10^{-7}\,\mathrm{m}\). The radiant flux intensity at the Earth is \(1.4 \times 10^{-9}\,\mathrm{W\,m^{-2}}\) and the star is \(2.5 \times 10^{17}\,\mathrm{m}\) away. Estimate (a) the surface temperature of the star, (b) its luminosity, (c) its radius.
H: Wien's law gives \(T\), and \(F = L/(4\pi d^2)\) gives \(L\).
H: For (c) rearrange \(L = 4\pi\sigma r^2T^4\) for \(r\), using the unrounded \(T\) and \(L\).
A: (a) \(T = \dfrac{2.9 \times 10^{-3}}{4.6 \times 10^{-7}}\) [C1] \(= 6.3 \times 10^{3}\,\mathrm{K}\). [A1] (b) \(L = 4\pi d^2F = 4\pi \times (2.5 \times 10^{17})^2 \times 1.4 \times 10^{-9}\) [C1] \(= 1.1 \times 10^{27}\,\mathrm{W}\). [A1] (c) \(r = \sqrt{\dfrac{L}{4\pi\sigma T^4}}\) [C1] \(= \sqrt{\dfrac{1.0996 \times 10^{27}}{4\pi \times 5.67 \times 10^{-8} \times 6304^4}} = 9.9 \times 10^{8}\,\mathrm{m}\). [A1] This is about 1.4 times the radius of the Sun.
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Two stars P and Q have the same luminosity. The peak wavelength of P is 580 nm and that of Q is 290 nm. (a) Find the ratio of the surface temperature of Q to that of P. (b) Find the ratio of the power radiated per unit area of Q to that of P. (c) Find the ratio of the radius of P to the radius of Q.
H: Wien's law: \(T \propto 1/\lambda_{\max}\).
H: Equal luminosities mean \(r^2T^4\) is the same for both.
A: (a) \(\dfrac{T_Q}{T_P} = \dfrac{\lambda_P}{\lambda_Q}\) [C1] \(= \dfrac{580}{290} = 2.0\). [A1] (b) Power per unit area is \(\sigma T^4\), so the ratio is \(2.0^4 = 16\). [A1] (c) \(L\) is the same, so \(r_P^2T_P^4 = r_Q^2T_Q^4\) [C1] and \(\dfrac{r_P}{r_Q} = \left(\dfrac{T_Q}{T_P}\right)^2 = 4.0\). [A1] Star P is much bigger and cooler; each square metre radiates 16 times less, so it needs 16 times the area, which is four times the radius.
Q: [4 marks] ★★★ The hydrogen line of wavelength 121.6 nm is observed in the spectrum of a very distant quasar at 486.4 nm. (a) Calculate \(\Delta\lambda/\lambda\). (b) Use \(\Delta\lambda/\lambda \approx v/c\) to calculate the speed of the quasar. (c) Comment on your answer.
H: A speed greater than \(c\) is not possible.
A: (a) \(\dfrac{\Delta\lambda}{\lambda} = \dfrac{486.4 - 121.6}{121.6}\) [C1] \(= 3.0\). [A1] (b) \(v \approx 3.0c = 9.0 \times 10^{8}\,\mathrm{m\,s^{-1}}\). [A1] (c) This is greater than the speed of light, which is impossible, so the approximation \(\Delta\lambda/\lambda \approx v/c\) fails: it is valid only when \(v \ll c\), and for such large redshifts a more complete treatment is needed. [B1]
:::

:::quiz
? Which quantity, for a given star, depends on the distance from the observer?
- The luminosity
+ The radiant flux intensity
- The surface temperature
- The radius
> Luminosity, temperature and radius belong to the star. The radiant flux intensity \(F = L/(4\pi d^2)\) is what arrives at the observer and gets smaller with distance.
? The distance from a star is doubled. What happens to the radiant flux intensity?
- It halves.
+ It falls to one quarter.
- It falls to one eighth.
- It doubles.
> The same power is spread over a sphere of four times the area, so \(F \propto 1/d^2\). "Halves" would be an inverse law, not an inverse square law.
? The surface temperature of a star is doubled, with the radius unchanged. What happens to its luminosity?
- It doubles.
- It quadruples.
- It rises eight times.
+ It rises sixteen times.
> \(L \propto T^4\), and \(2^4 = 16\). Doubling the radius would only quadruple \(L\).
? A star is hotter than the Sun. How does its peak wavelength compare with the Sun's?
- It is longer, because it emits more energy.
+ It is shorter, because \(\lambda_{\max} \propto 1/T\).
- It is the same, because all stars have the same peak.
- It is longer, because hot stars look red.
> Wien's law: the hotter the surface, the shorter the peak wavelength, so hot stars look blue-white and cool stars look red.
? What is a redshift?
- A shift of the spectral lines of a source moving towards the observer to shorter wavelengths.
+ An increase in the observed wavelength of radiation from a source moving away from the observer.
- A change in the colour of a star as its temperature falls.
- A change in the speed of light as it leaves a galaxy.
> Redshift is a Doppler effect: a receding source makes the waves longer. It does not change the speed of light, and it is different from a star cooling down.
? Which statement about Hubble's law is correct?
- Distant galaxies move away more slowly than near ones.
+ The recession speed of a galaxy is approximately proportional to its distance.
- All galaxies move away at the same speed.
- The galaxies move away from a centre that is near the Milky Way.
> \(v \approx H_0d\): faster for the more distant galaxies. Every observer sees the same pattern, so there is no centre.
? What is a standard candle?
- An object whose distance is known from a direct measurement.
- An object that always has the same radiant flux intensity at the Earth.
+ An object of known luminosity.
- An object that always has the same temperature.
> If \(L\) is known and \(F\) is measured, then \(d = \sqrt{L/(4\pi F)}\) gives the distance. The flux at the Earth changes with distance, so it cannot be fixed.
:::

:::checklist What you can now do
- [ ] I can define luminosity and radiant flux intensity and use the inverse square law \(F = L/(4\pi d^2)\).
- [ ] I can explain what a standard candle is and use one, with Cepheid variables and type Ia supernovae, to find a distance.
- [ ] I can use Wien's displacement law to estimate a star's surface temperature from its peak wavelength.
- [ ] I can use the Stefan–Boltzmann law \(L = 4\pi\sigma r^2T^4\), including ratios of two stars.
- [ ] I can estimate a star's radius from \(\lambda_{\max}\), \(F\) and \(d\).
- [ ] I can use redshift \(\Delta\lambda/\lambda \approx v/c\) to find the speed of a source, and say when the approximation is valid.
- [ ] I can use Hubble's law \(v \approx H_0d\), explain how redshifts show that the Universe is expanding, and how this leads to the Big Bang theory.
:::

:::recap
- Luminosity \(L\): total power emitted by a star (W). Radiant flux intensity \(F = L/(4\pi d^2)\): power per unit area arriving at the observer (\(\mathrm{W\,m^{-2}}\)), an inverse square law.
- A standard candle has a known luminosity, so \(d = \sqrt{L/(4\pi F)}\). Cepheid variables (period gives luminosity) and type Ia supernovae (same peak luminosity) are used.
- Wien's displacement law: \(\lambda_{\max}T = 2.9 \times 10^{-3}\,\mathrm{m\,K}\). Hot stars: short \(\lambda_{\max}\), blue. Cool stars: long \(\lambda_{\max}\), red.
- Stefan–Boltzmann: \(L = 4\pi\sigma r^2T^4\); power per unit area \(\sigma T^4\). Double \(T\): \(L\) increases 16 times. For equal \(L\), \(r \propto 1/T^2\).
- Radius of a star: \(T\) from Wien, \(L\) from \(F\) and \(d\), then \(r = \sqrt{L/(4\pi\sigma T^4)}\). Use the radius, not the diameter, and kelvin.
- Redshift: \(\Delta\lambda/\lambda \approx \Delta f/f \approx v/c\) (\(v \ll c\)), with \(\Delta\lambda\) = observed minus emitted. Spectral lines of distant galaxies are at longer wavelengths: they are receding.
- Hubble's law: \(v \approx H_0d\), \(H_0 \approx 2.3 \times 10^{-18}\,\mathrm{s^{-1}}\). The Universe is expanding (space itself, with no centre); running it backwards gives the Big Bang from a hot, dense state, at about \(1/H_0 \approx 1.4 \times 10^{10}\) years ago.
:::

:::links
- explore: [Blackbody Spectrum](https://phet.colorado.edu/en/simulations/blackbody-spectrum) · PhET · change the temperature and watch the peak and the colour move
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the astronomy and cosmology questions in real papers [unofficial]
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Practical skills: measurement, tables, graphs and uncertainty](#phys.practical)
