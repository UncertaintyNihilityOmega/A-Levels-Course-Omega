@chapter phys.superposition
@title Superposition
@level as
@paper CAIE P1 · P2 · P3 (AS)
@time 7–9 hours
@summary What happens when waves meet: the principle of superposition, stationary waves on strings, in air columns and with microwaves, diffraction, interference and coherence, Young's double-slit experiment, and the diffraction grating.

:::why
When two waves meet they do not bounce off each other: they pass through and add up. That one rule explains why a guitar string sings at only certain frequencies, why noise-cancelling headphones work, why a CD shimmers with colours, and how Thomas Young showed in 1801 that light is a wave. The same rules give physicists a ruler as fine as the wavelength of light, which is how spectrometers identify the elements in distant stars.
:::

**Before you start**, you need the wave vocabulary from [Waves](#phys.waves): wavelength, frequency, phase difference and \(v = f\lambda\).

:::try Warm-up
Q: A wave has frequency 440 Hz and travels at \(340\,\mathrm{m\,s^{-1}}\). Find its wavelength. (from [Waves](#phys.waves))
A: \(\lambda = v/f = 340/440 = 0.773\,\mathrm{m}\).
Q: Two points on a wave of wavelength 0.80 m are 0.20 m apart along the wave. Find their phase difference. (from [Waves](#phys.waves))
A: \(0.20/0.80 = \tfrac14\) of a wavelength, so \(\phi = \tfrac14 \times 360^\circ = 90^\circ\) (\(\pi/2\) rad).
Q: A wave has intensity \(I\). Its amplitude is tripled. What is the new intensity? (from [Waves](#phys.waves))
A: \(I \propto A^2\), so the intensity becomes \(3^2 I = 9I\).
Q: A small angle \(\theta\) satisfies \(\tan\theta = y/L\). Find \(\theta\) in degrees when \(y = 0.020\,\mathrm{m}\) and \(L = 2.0\,\mathrm{m}\). (from [Physical quantities, units and uncertainty](#phys.units))
A: \(\tan\theta = 0.020/2.0 = 0.010\), so \(\theta = 0.573^\circ\). For such a small angle, \(\sin\theta \approx \tan\theta \approx \theta\) (in radians).
:::

## The principle of superposition

Throw two stones into a pond. The ripples cross each other, and where they cross the water surface is higher in some places and calmer in others. Yet after crossing, each set of ripples carries on as if the other had never been there. Waves pass through each other and **add**.

:::def Principle of superposition
When two or more waves meet at a point, the resultant displacement is the sum of the displacements that the individual waves would have produced at that point.
:::

Displacement has a **direction**, so the addition must keep signs: up is positive and down is negative. A pulse of \(+3.0\,\mathrm{mm}\) meeting a pulse of \(-5.0\,\mathrm{mm}\) gives \(-2.0\,\mathrm{mm}\) for as long as they overlap.

When two waves of the same frequency meet, the result depends on their **phase difference** \(\phi\) at the point.

- **Constructive superposition:** the waves are in phase (\(\phi = 0^\circ, 360^\circ, \dots\)), crests meet crests, and the resultant amplitude is the sum of the amplitudes.
- **Destructive superposition:** the waves are in antiphase (\(\phi = 180^\circ, 540^\circ, \dots\)), crests meet troughs, and the resultant amplitude is the difference of the amplitudes. If the amplitudes are equal the resultant is zero.

:::plot In phase: wave 1 has amplitude 1.0, wave 2 has amplitude 0.6. The resultant has amplitude 1.6.
--f "sin(x)" --f "0.6*sin(x)" --f "1.6*sin(x)" --deg --x 0 360 --y -2 2 --xstep 90 --xlabel "phase / °" --ylabel "displacement" --label "wave 1" --label "wave 2" --label "resultant" --legend tr
:::

:::plot In antiphase: the same two waves with a phase difference of 180°. The resultant has amplitude 1.0 − 0.6 = 0.4.
--f "sin(x)" --f "-0.6*sin(x)" --f "0.4*sin(x)" --deg --x 0 360 --y -2 2 --xstep 90 --xlabel "phase / °" --ylabel "displacement" --label "wave 1" --label "wave 2" --label "resultant" --legend tr
:::

Waves from two sources reach a point having travelled different distances. The extra distance travelled by one wave is the **path difference**.

:::def Path difference
The difference in the distances travelled by two waves from their sources to the point where they meet.
:::

A path difference of one whole wavelength is a phase difference of 360°, so a path difference \(\Delta x\) gives a phase difference \(\phi = 2\pi\Delta x/\lambda\) (as in [Waves](#phys.waves)). For two sources that emit **in phase**:

:::key Conditions for interference at a point (sources in phase)
\[\text{constructive: } \Delta x = n\lambda \qquad\qquad \text{destructive: } \Delta x = \left(n + \tfrac12\right)\lambda\]
\(\Delta x\): path difference (m) · \(\lambda\): wavelength (m) · \(n = 0, 1, 2, \dots\) A path difference of \(\tfrac12\lambda, 1\tfrac12\lambda, 2\tfrac12\lambda \dots\) gives destructive superposition.
:::

## Stationary waves

Fix one end of a rope and shake the other. A pulse travels to the fixed end, is reflected and comes back. If you shake at the right frequency, the incoming and reflected waves superpose to give a pattern that does not move along the rope: some points never move, and others swing with a large amplitude. This is a **stationary wave** (or standing wave).

:::def Stationary wave
A wave pattern produced by the superposition of two progressive waves of the same frequency (and similar amplitude) travelling in opposite directions, with fixed points of zero amplitude and no net transfer of energy along the wave.
:::

:::def Node
A point on a stationary wave where the amplitude is zero.
:::

:::def Antinode
A point on a stationary wave where the amplitude is a maximum.
:::

### The graphical method

Draw the two travelling waves at one instant, add their displacements point by point, then repeat a fraction of a period later. The figure shows a wave moving to the right (solid line), an identical wave moving to the left (dashed line) and their sum (thicker line) at four instants. Each wave moves a distance \(vt\), which is \(\lambda/8\) in \(T/8\) and \(\lambda/4\) in \(T/4\).

:::html
<figure class="fig"><svg viewBox="0 0 520 482" role="img" aria-label="Four panels showing two travelling waves and their sum at t equals 0, T over 8, T over 4 and T over 2. The right-moving wave is a solid line, the left-moving wave is a dashed line, and the sum is a thicker line. At t equals 0 the waves coincide and the sum is largest. At T over 4 the waves are in antiphase everywhere and the sum is a flat line. At T over 2 the sum has again the largest amplitude but is inverted. The sum is always zero at the same points, the nodes, and largest halfway between them, the antinodes."><path class="c1 sw2" d="M100 10H130"/><text class="tl" x="136" y="14">wave moving right</text><path class="c2 sw2 dash" d="M270 10H300"/><text class="tl" x="306" y="14">wave moving left</text><path class="c3 sw3" d="M425 10H455"/><text class="tl" x="461" y="14">sum</text><path class="ln thin dash" d="M80 28V450M200 28V450M320 28V450M440 28V450"/><path class="ax" d="M80 90H440M80 196H440M80 302H440M80 408H440"/><path class="c1 sw2" d="M80 90C85 87 100 76 110 72C120 67 130 64 140 64C150 64 160 67 170 72C180 76 190 84 200 90C210 96 220 104 230 108C240 113 250 116 260 116C270 116 280 113 290 108C300 104 310 96 320 90C330 84 340 76 350 72C360 67 370 64 380 64C390 64 400 67 410 72C420 76 435 87 440 90"/><path class="c2 sw2 dash" d="M80 90C85 87 100 76 110 72C120 67 130 64 140 64C150 64 160 67 170 72C180 76 190 84 200 90C210 96 220 104 230 108C240 113 250 116 260 116C270 116 280 113 290 108C300 104 310 96 320 90C330 84 340 76 350 72C360 67 370 64 380 64C390 64 400 67 410 72C420 76 435 87 440 90"/><path class="c3 sw3" d="M80 90C85 84 100 62 110 53C120 45 130 38 140 38C150 38 160 45 170 53C180 62 190 78 200 90C210 102 220 118 230 127C240 135 250 142 260 142C270 142 280 135 290 127C300 118 310 102 320 90C330 78 340 62 350 53C360 45 370 38 380 38C390 38 400 45 410 53C420 62 435 84 440 90"/><path class="c1 sw2" d="M80 214C85 211 100 202 110 196C120 190 130 182 140 178C150 173 160 170 170 170C180 170 190 173 200 178C210 182 220 190 230 196C240 202 250 210 260 214C270 219 280 222 290 222C300 222 310 219 320 214C330 210 340 202 350 196C360 190 370 182 380 178C390 173 400 170 410 170C420 170 435 176 440 178"/><path class="c2 sw2 dash" d="M80 178C85 176 100 170 110 170C120 170 130 173 140 178C150 182 160 190 170 196C180 202 190 210 200 214C210 219 220 222 230 222C240 222 250 219 260 214C270 210 280 202 290 196C300 190 310 182 320 178C330 173 340 170 350 170C360 170 370 173 380 178C390 182 400 190 410 196C420 202 435 211 440 214"/><path class="c3 sw3" d="M80 196C85 192 100 176 110 170C120 164 130 159 140 159C150 159 160 164 170 170C180 176 190 187 200 196C210 205 220 216 230 222C240 228 250 233 260 233C270 233 280 228 290 222C300 216 310 205 320 196C330 187 340 176 350 170C360 164 370 159 380 159C390 159 400 164 410 170C420 176 435 192 440 196"/><path class="c1 sw2" d="M80 328C85 327 100 325 110 320C120 316 130 308 140 302C150 296 160 288 170 284C180 279 190 276 200 276C210 276 220 279 230 284C240 288 250 296 260 302C270 308 280 316 290 320C300 325 310 328 320 328C330 328 340 325 350 320C360 316 370 308 380 302C390 296 400 288 410 284C420 279 435 277 440 276"/><path class="c2 sw2 dash" d="M80 276C85 277 100 279 110 284C120 288 130 296 140 302C150 308 160 316 170 320C180 325 190 328 200 328C210 328 220 325 230 320C240 316 250 308 260 302C270 296 280 288 290 284C300 279 310 276 320 276C330 276 340 279 350 284C360 288 370 296 380 302C390 308 400 316 410 320C420 325 435 327 440 328"/><path class="c3 sw3" d="M80 302H440"/><path class="c1 sw2" d="M80 408C85 411 100 422 110 426C120 431 130 434 140 434C150 434 160 431 170 426C180 422 190 414 200 408C210 402 220 394 230 390C240 385 250 382 260 382C270 382 280 385 290 390C300 394 310 402 320 408C330 414 340 422 350 426C360 431 370 434 380 434C390 434 400 431 410 426C420 422 435 411 440 408"/><path class="c2 sw2 dash" d="M80 408C85 411 100 422 110 426C120 431 130 434 140 434C150 434 160 431 170 426C180 422 190 414 200 408C210 402 220 394 230 390C240 385 250 382 260 382C270 382 280 385 290 390C300 394 310 402 320 408C330 414 340 422 350 426C360 431 370 434 380 434C390 434 400 431 410 426C420 422 435 411 440 408"/><path class="c3 sw3" d="M80 408C85 414 100 436 110 445C120 453 130 460 140 460C150 460 160 453 170 445C180 436 190 420 200 408C210 396 220 380 230 371C240 363 250 356 260 356C270 356 280 363 290 371C300 380 310 396 320 408C330 420 340 436 350 445C360 453 370 460 380 460C390 460 400 453 410 445C420 436 435 414 440 408"/><text class="tl" x="10" y="94">t = 0</text><text class="tl" x="10" y="200">t = T/8</text><text class="tl" x="10" y="306">t = T/4</text><text class="tl" x="10" y="412">t = T/2</text><text class="tb tc" x="140" y="31">A</text><text class="tb tc" x="260" y="349">A</text><text class="tb tc" x="380" y="31">A</text><text class="tb tc" x="80" y="476">N</text><text class="tb tc" x="200" y="476">N</text><text class="tb tc" x="320" y="476">N</text><text class="tb tc" x="440" y="476">N</text></svg><figcaption>The graphical method. At every instant the thicker line (sum) is the sum of the other two. The sum is always zero at the nodes N (the dashed vertical lines), which are λ/2 apart, and swings most halfway between them at the antinodes A. At T/4 the two waves cancel exactly everywhere for an instant, yet the energy has not vanished: it is stored in the motion of the string, which is about to move again.</figcaption></figure>
:::

Two features of the graph are worth remembering. First, the nodes stay at the same points, **half a wavelength** apart; the antinodes lie half-way between them, also half a wavelength apart. So the distance between a node and the next antinode is \(\lambda/4\). Second, between two adjacent nodes all the particles move up together and down together, in phase, but with different amplitudes. The particles in the **next** loop move in the opposite direction, in antiphase.

| | Progressive wave | Stationary wave |
|---|---|---|
| Energy | transferred along the wave | not transferred along the wave |
| Amplitude | the same for every particle | zero at nodes, maximum at antinodes, varies in between |
| Phase | phase difference between points depends on their separation | all points between adjacent nodes in phase; adjacent loops in antiphase |
| Pattern | moves with speed \(v\) | does not move |
| Wavelength | distance between adjacent points in phase | twice the distance between adjacent nodes |

Use the tool below to watch the stationary wave appear as the two travelling waves add. Change the harmonic number and count the nodes. Note that the string is drawn in slow motion: a real string oscillates tens or hundreds of times each second.

:::html
<div class="widget" data-w="phys-wave" data-mode="stationary" data-n="3"></div>
:::

## Stationary wave experiments

A stationary wave needs a wave to be reflected back on itself. It happens easily in a stretched string, in a pipe of air and with microwaves bouncing off a metal plate. In each case the wave pattern is stable only at certain frequencies, the **resonant frequencies**, because the ends must be nodes or antinodes.

### A stretched string

A string fixed at both ends has a node at each end. The longest wavelength that fits is when the string is a half-wavelength long. Each higher pattern adds another half-wavelength:

:::html
<figure class="fig"><svg viewBox="0 0 520 215" role="img" aria-label="The first three stationary waves on a string fixed at both ends: one loop with L equal to lambda over 2, two loops with L equal to lambda, and three loops with L equal to three lambda over 2."><path class="ln thick" d="M120 25V65M420 25V65M120 95V135M420 95V135M120 165V205M420 165V205"/><path class="c3" d="M120 45C132 42 170 32 195 28C220 24 245 21 270 21C295 21 320 24 345 28C370 32 408 42 420 45"/><path class="c3" d="M120 45C132 48 170 58 195 62C220 66 245 69 270 69C295 69 320 66 345 62C370 58 408 48 420 45"/><path class="c3" d="M120 115C126 112 145 102 158 98C170 94 182 91 195 91C208 91 220 94 232 98C245 102 258 109 270 115C282 121 295 128 308 132C320 136 332 139 345 139C358 139 370 136 382 132C395 128 414 118 420 115"/><path class="c3" d="M120 115C126 118 145 128 158 132C170 136 182 139 195 139C208 139 220 136 232 132C245 128 258 121 270 115C282 109 295 102 308 98C320 94 332 91 345 91C358 91 370 94 382 98C395 102 414 112 420 115"/><path class="c3" d="M120 185C124 182 137 172 145 168C153 164 162 161 170 161C178 161 187 164 195 168C203 172 212 179 220 185C228 191 237 198 245 202C253 206 262 209 270 209C278 209 287 206 295 202C303 198 312 191 320 185C328 179 337 172 345 168C353 164 362 161 370 161C378 161 387 164 395 168C403 172 416 182 420 185"/><path class="c3" d="M120 185C124 188 137 198 145 202C153 206 162 209 170 209C178 209 187 206 195 202C203 198 212 191 220 185C228 179 237 172 245 168C253 164 262 161 270 161C278 161 287 164 295 168C303 172 312 179 320 185C328 191 337 198 345 202C353 206 362 209 370 209C378 209 387 206 395 202C403 198 416 188 420 185"/><circle class="fi" cx="120" cy="45" r="3.5"/><circle class="fi" cx="420" cy="45" r="3.5"/><circle class="fi" cx="120" cy="115" r="3.5"/><circle class="fi" cx="270" cy="115" r="3.5"/><circle class="fi" cx="420" cy="115" r="3.5"/><circle class="fi" cx="120" cy="185" r="3.5"/><circle class="fi" cx="220" cy="185" r="3.5"/><circle class="fi" cx="320" cy="185" r="3.5"/><circle class="fi" cx="420" cy="185" r="3.5"/><text class="tl" x="10" y="49">n = 1</text><text class="tl" x="10" y="119">n = 2</text><text class="tl" x="10" y="189">n = 3</text><text class="tl" x="430" y="49">L = λ/2</text><text class="tl" x="430" y="119">L = λ</text><text class="tl" x="430" y="189">L = 3λ/2</text></svg><figcaption>The first three modes of a string of length L fixed at both ends. The dots mark the nodes. The nth mode has n loops and L = nλ/2, so λ = 2L/n.</figcaption></figure>
:::

:::formula Stationary waves on a string
\[L = \frac{n\lambda}{2} \qquad\Rightarrow\qquad \lambda = \frac{2L}{n} \qquad\text{and}\qquad f_n = \frac{v}{\lambda} = \frac{nv}{2L}\]
\(L\): length of the string (m) · \(n\): number of loops = 1, 2, 3, … (the harmonic number) · \(v\): speed of the wave on the string (m s⁻¹). The resonant frequencies are whole-number multiples of the lowest frequency \(f_1\).
:::

:::html
<figure class="fig"><svg viewBox="0 0 540 205" role="img" aria-label="Apparatus: a signal generator is wired to a vibration generator at the left end of a horizontal string. The string runs to a bridge and then over a pulley to a hanging mass. Three loops of a stationary wave are drawn between the vibrator and the bridge, and the length L between them is marked."><rect class="f1 s-ink sw2" x="10" y="20" width="90" height="46"/><text class="tl tc" x="55" y="40">signal</text><text class="tl tc" x="55" y="56">generator</text><path class="ln" d="M100 43H160V95"/><rect class="f1 s-ink sw2" x="130" y="95" width="60" height="40"/><text class="tl tc" x="160" y="160">vibration</text><text class="tl tc" x="160" y="176">generator</text><path class="ln thin" d="M410 115H480"/><path class="c3" d="M190 115Q226.7 71 263.3 115Q300.0 159 336.7 115Q373.3 71 410.0 115"/><path class="c3" d="M190 115Q226.7 159 263.3 115Q300.0 71 336.7 115Q373.3 159 410.0 115"/><path class="ln" d="M410 115L400 140H420Z"/><text class="tl tc" x="410" y="158">bridge</text><circle class="fp s-ink sw2" cx="480" cy="115" r="10"/><text class="tl tc" x="480" y="94">pulley</text><path class="ln" d="M490 115V152"/><rect class="f2 s-ink sw2" x="478" y="152" width="24" height="26"/><text class="tl tc" x="490" y="198">masses</text><path class="c1" d="M300 62H194" marker-end="url(#ah-phys)"/><path class="c1" d="M300 62H406" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="300" y="54">L</text></svg><figcaption>A string is driven by a vibration generator at the left and held at the right by a bridge, with a hanging mass to set the tension. At a resonant frequency a stationary wave appears with a node at each end. Here the string vibrates with three loops (n = 3); the two curves show its extreme positions.</figcaption></figure>
:::

:::lab Stationary waves on a string
:::steps
1. Set up the vibration generator, string, bridge, pulley and masses as shown. Measure the distance \(L\) between the vibrator end and the bridge with a metre rule.
2. Start at a low frequency on the signal generator and increase it slowly. At certain frequencies the string forms large, clear loops. Adjust the frequency until the amplitude of the loops is greatest and the pattern is steady.
3. Record the frequency for the first, second, third and later patterns, counting the number of loops \(n\) each time.
4. For each pattern, \(\lambda = 2L/n\). Calculate the wave speed from \(v = f\lambda\): it should be the same for every pattern (it depends only on the tension and the string).
5. Plot \(f\) against \(n\): a straight line through the origin with gradient \(f_1 = v/2L\).
:::
:::

:::eg A string of length 1.20 m is fixed at both ends. It resonates with three loops when the frequency is 150 Hz. Find the wavelength, the speed of waves on the string and the lowest resonant frequency.
Three loops: \(L = 3\lambda/2\), so \(\lambda = 2L/3\) [C1] \(= 2 \times 1.20/3 = 0.80\,\mathrm{m}\). [A1]

\[v = f\lambda = 150 \times 0.80 = 120\,\mathrm{m\,s^{-1}}\] [A1]
The lowest frequency (one loop) is \(f_1 = f_3/3 = 150/3 = 50\,\mathrm{Hz}\). [B1] Check: \(f_1 = v/2L = 120/2.40 = 50\,\mathrm{Hz}\). The next resonance after 150 Hz is 200 Hz.
:::

### Microwaves

A microwave transmitter sends waves towards a flat metal plate. The plate reflects them back along the same line, and the incident and reflected waves superpose to give a stationary wave. The plate is a **node**, because the electric field cannot be large in a conductor. A small detector (a probe connected to a meter) is moved along the line between the transmitter and the plate: the meter reading falls to nearly zero at each node and peaks at each antinode.

:::html
<figure class="fig"><svg viewBox="0 0 540 175" role="img" aria-label="A microwave transmitter on the left sends microwaves to a metal plate on the right. A probe on the line between them can be moved to find the nodes, marked as dots on the line, which are a distance lambda over 2 apart."><rect class="f1 s-ink sw2" x="10" y="52" width="70" height="40"/><text class="tl tc" x="45" y="114">microwave</text><text class="tl tc" x="45" y="130">transmitter</text><path class="ln thick" d="M470 20V124"/><text class="tl tc" x="470" y="146">metal plate</text><path class="c1" d="M100 32H190" marker-end="url(#ah-phys)"/><text class="tl ta tc" x="145" y="24">microwaves</text><path class="ln thin" d="M80 72H470"/><circle class="fi" cx="470" cy="72" r="3.5"/><circle class="fi" cx="414" cy="72" r="3.5"/><circle class="fi" cx="358" cy="72" r="3.5"/><circle class="fi" cx="302" cy="72" r="3.5"/><circle class="fi" cx="246" cy="72" r="3.5"/><circle class="fi" cx="190" cy="72" r="3.5"/><rect class="f2 s-ink sw2" x="254" y="58" width="14" height="28"/><path class="c2" d="M240 48H296" marker-end="url(#ah2-phys)"/><text class="tl tc" x="261" y="106">probe</text><path class="ln thin dash" d="M302 80V104M358 80V104"/><path class="c1" d="M330 100H306" marker-end="url(#ah-phys)"/><path class="c1" d="M330 100H354" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="330" y="124">λ/2</text></svg><figcaption>The probe is moved along the line, and the meter reading falls to a minimum at each node (dots). Adjacent nodes are λ/2 apart.</figcaption></figure>
:::

Adjacent nodes are \(\lambda/2\) apart, so measure the distance across several nodes and divide, which reduces the percentage uncertainty. If the distance between \(N\) successive nodes is \(d\), there are \(N - 1\) gaps and \(\lambda = 2d/(N-1)\).

:::eg The distance between 5 successive nodes of a stationary microwave pattern is 5.6 cm. Find the wavelength and the frequency of the microwaves, which travel at \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\).
Five nodes make 4 gaps, each \(\lambda/2\), so \(4 \times \lambda/2 = 5.6\,\mathrm{cm}\) [C1] and \(\lambda = 2.8\,\mathrm{cm}\). [A1]

\[f = \frac{c}{\lambda} = \frac{3.00 \times 10^{8}}{0.028} = 1.07 \times 10^{10}\,\mathrm{Hz}\] [A1]
This is a typical microwave frequency of about 10 GHz.
:::

### Air columns

Sound waves in a pipe reflect from the ends. A **closed** end is always a **node** of displacement (the air cannot move through a wall), and an **open** end is an **antinode** (the air is free to move). Ignore end corrections: they are neglected in this course.

:::html
<figure class="fig"><svg viewBox="0 0 520 292" role="img" aria-label="Left column: pipes closed at the left end with the first three stationary waves, a node at the closed end and an antinode at the open end, for L equal to lambda over 4, 3 lambda over 4 and 5 lambda over 4. Right column: pipes open at both ends, with an antinode at each end, for L equal to lambda over 2, lambda and 3 lambda over 2."><text class="tb tc" x="125" y="18">closed at one end</text><text class="tb tc" x="395" y="18">open at both ends</text><path class="ln" d="M30 32H220M30 88H220M30 122H220M30 178H220M30 212H220M30 268H220"/><path class="ln thick" d="M30 32V88M30 122V178M30 212V268"/><path class="ln" d="M300 32H490M300 88H490M300 122H490M300 178H490M300 212H490M300 268H490"/><path class="c3" d="M30 60C46 58 93 50 125 47C157 44 204 43 220 42"/><path class="c3" d="M30 60C46 62 93 70 125 73C157 76 204 77 220 78"/><path class="c3" d="M300 42C308 43 332 44 348 47C363 50 379 56 395 60C411 64 427 70 442 73C458 76 482 77 490 78"/><path class="c3" d="M300 78C308 77 332 76 348 73C363 70 379 64 395 60C411 56 427 50 442 47C458 44 482 43 490 42"/><path class="c3" d="M30 150C35 148 51 140 62 137C72 134 83 132 93 132C104 132 114 134 125 137C136 140 146 146 157 150C167 154 178 160 188 163C199 166 215 167 220 168"/><path class="c3" d="M30 150C35 152 51 160 62 163C72 166 83 168 93 168C104 168 114 166 125 163C136 160 146 154 157 150C167 146 178 140 188 137C199 134 215 133 220 132"/><path class="c3" d="M300 132C304 133 316 134 324 137C332 140 340 146 348 150C355 154 363 160 371 163C379 166 387 168 395 168C403 168 411 166 419 163C427 160 435 154 442 150C450 146 458 140 466 137C474 134 486 133 490 132"/><path class="c3" d="M300 168C304 167 316 166 324 163C332 160 340 154 348 150C355 146 363 140 371 137C379 134 387 132 395 132C403 132 411 134 419 137C427 140 435 146 442 150C450 154 458 160 466 163C474 166 486 167 490 168"/><path class="c3" d="M30 240C33 238 43 230 49 227C55 224 62 222 68 222C74 222 81 224 87 227C93 230 100 236 106 240C112 244 119 250 125 253C131 256 138 258 144 258C150 258 157 256 163 253C169 250 176 244 182 240C188 236 195 230 201 227C207 224 217 223 220 222"/><path class="c3" d="M30 240C33 242 43 250 49 253C55 256 62 258 68 258C74 258 81 256 87 253C93 250 100 244 106 240C112 236 119 230 125 227C131 224 138 222 144 222C150 222 157 224 163 227C169 230 176 236 182 240C188 244 195 250 201 253C207 256 217 257 220 258"/><path class="c3" d="M300 222C303 223 311 224 316 227C321 230 326 236 332 240C337 244 342 250 348 253C353 256 358 258 363 258C369 258 374 256 379 253C384 250 390 244 395 240C400 236 406 230 411 227C416 224 421 222 427 222C432 222 437 224 442 227C448 230 453 236 458 240C464 244 469 250 474 253C479 256 487 257 490 258"/><path class="c3" d="M300 258C303 257 311 256 316 253C321 250 326 244 332 240C337 236 342 230 348 227C353 224 358 222 363 222C369 222 374 224 379 227C384 230 390 236 395 240C400 244 406 250 411 253C416 256 421 258 427 258C432 258 437 256 442 253C448 250 453 244 458 240C464 236 469 230 474 227C479 224 487 223 490 222"/><text class="tl tc" x="125" y="106">L = λ/4</text><text class="tl tc" x="125" y="196">L = 3λ/4</text><text class="tl tc" x="125" y="284">L = 5λ/4</text><text class="tl tc" x="395" y="106">L = λ/2</text><text class="tl tc" x="395" y="196">L = λ</text><text class="tl tc" x="395" y="284">L = 3λ/2</text></svg><figcaption>The curves show the amplitude of the oscillation of the air along each pipe (an envelope, not a picture of the pipe's air). A closed end is a node and an open end is an antinode.</figcaption></figure>
:::

:::formula Resonance in pipes
\[\text{closed at one end: } L = \frac{\lambda}{4},\ \frac{3\lambda}{4},\ \frac{5\lambda}{4},\dots \qquad\qquad \text{open at both ends: } L = \frac{\lambda}{2},\ \lambda,\ \frac{3\lambda}{2},\dots\]
A closed pipe resonates only at odd multiples of its lowest frequency: \(f_1, 3f_1, 5f_1, \dots\) An open pipe resonates at \(f_1, 2f_1, 3f_1, \dots\)
:::

:::eg A pipe of length 0.30 m is closed at one end. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Find the two lowest resonant frequencies. Then find the lowest resonant frequency if both ends of the pipe are open.
Closed pipe, lowest mode: \(L = \lambda/4\), so \(\lambda = 4 \times 0.30 = 1.20\,\mathrm{m}\) [C1] and \(f_1 = \dfrac{340}{1.20} = 283\,\mathrm{Hz}\). [A1]

The next mode is \(L = 3\lambda/4\), with \(f = 3f_1 = 850\,\mathrm{Hz}\). [A1]

Open at both ends: \(L = \lambda/2\), so \(\lambda = 0.60\,\mathrm{m}\) and \(f_1 = \dfrac{340}{0.60} = 567\,\mathrm{Hz}\). [A1] Opening the end raises the lowest frequency by a factor of 2: this is why a closed organ pipe of the same length sounds an octave lower.
:::

### Measuring the speed of sound with a resonance tube

A tube is clamped vertically with its lower end in a tall cylinder of water. A tuning fork of known frequency \(f\) is sounded above the open top, and the tube is raised or lowered so that the length of air above the water changes. Where the air column resonates, the sound is clearly louder.

:::html
<figure class="fig small"><svg viewBox="40 0 260 262" role="img" aria-label="A vertical tube dips into a tall cylinder of water. A tuning fork is held above the open top of the tube. The length of the air column from the top of the tube to the water surface is labelled L."><rect class="fm s-mute sw1" x="90" y="60" width="120" height="180"/><rect class="f2" x="91" y="140" width="118" height="99"/><rect class="fp s-ink sw2" x="130" y="30" width="40" height="170"/><rect class="f2" x="131" y="140" width="38" height="59"/><path class="ln thin" d="M90 140H210"/><path class="ln" d="M138 4V18C138 26 154 26 154 18V4"/><path class="ln" d="M146 26V30"/><text class="tl" x="162" y="14">tuning fork</text><path class="ln thin dash" d="M170 30H252M210 140H252"/><path class="c1" d="M240 85V34" marker-end="url(#ah-phys)"/><path class="c1" d="M240 85V136" marker-end="url(#ah-phys)"/><text class="tl ti" x="246" y="89">L</text><text class="tl" x="44" y="39">tube</text><path class="ln thin" d="M78 35H130"/><text class="tl tc" x="150" y="226">water</text></svg><figcaption>Raise or lower the tube to change the air column length L. The air column resonates when its length is λ/4, 3λ/4, 5λ/4 and so on.</figcaption></figure>
:::

:::lab Speed of sound with a resonance tube and a tuning fork
:::steps
1. Hold a vibrating tuning fork of known frequency \(f\) just above the open top of the tube. Start with a short air column.
2. Lower the tube slowly into the water (making the air column longer) until the sound gets noticeably louder. Measure the length \(L_1\) from the top of the tube to the water surface.
3. Continue lengthening the air column to find the next louder position, \(L_2\), and a third if the cylinder is tall enough.
4. Successive resonances are \(\lambda/2\) apart, so \(\lambda = 2(L_2 - L_1)\). Use the **difference**: the exact position of the antinode at the open end is slightly above the tube top (end correction), but it is the same for both lengths and cancels in the subtraction.
5. Calculate \(v = f\lambda\) and repeat with a different tuning fork. The values of \(v\) should agree.
:::
:::

:::eg A tuning fork of frequency 512 Hz is used with a resonance tube. The first two resonances occur at air-column lengths 0.163 m and 0.493 m. Find the wavelength and the speed of sound.
Successive resonances differ by \(\lambda/2\): \(\dfrac{\lambda}{2} = 0.493 - 0.163 = 0.330\,\mathrm{m}\), so \(\lambda = 0.660\,\mathrm{m}\). [C1] [A1]

\[v = f\lambda = 512 \times 0.660 = 338\,\mathrm{m\,s^{-1}}\] [A1]
Check: the first resonance should be near \(\lambda/4 = 0.165\,\mathrm{m}\), and it is 0.163 m. The small difference is the end correction, which cancels in the subtraction.
:::

## Diffraction

Waves do not travel only in straight lines. When a wave passes through a gap or round the edge of an obstacle it spreads out into the region behind.

:::def Diffraction
The spreading of a wave as it passes through a gap or around the edge of an obstacle.
:::

A ripple tank shows it well. Plane waves approach a barrier with a gap in it. The size of the effect depends on the **gap width compared with the wavelength**.

:::html
<figure class="fig"><svg viewBox="0 0 500 205" role="img" aria-label="Two ripple tank diagrams. Left: plane waves meet a barrier whose gap is about one wavelength wide; the waves emerge as semicircular waves spreading widely. Right: plane waves meet a barrier whose gap is about six wavelengths wide; the waves pass through nearly straight, with only slight curving at the edges."><path class="ln" d="M20 20V180M40 20V180M60 20V180M80 20V180"/><rect class="fi" x="96" y="16" width="8" height="74"/><rect class="fi" x="96" y="110" width="8" height="74"/><path class="ln" d="M103 80A20 20 0 0 1 103 120M107 61A40 40 0 0 1 107 139M110 41A60 60 0 0 1 110 159M114 21A80 80 0 0 1 114 179"/><text class="tl tc" x="100" y="199">gap ≈ λ</text><path class="ln" d="M290 20V180M310 20V180M330 20V180M350 20V180"/><rect class="fi" x="366" y="16" width="8" height="24"/><rect class="fi" x="366" y="160" width="8" height="24"/><path class="ln" d="M390 40V160M410 40V160M430 40V160"/><path class="ln" d="M390 40A20 20 0 0 0 386 29M390 160A20 20 0 0 1 386 172M410 40A40 40 0 0 0 403 17M410 160A40 40 0 0 1 403 183M430 40A60 60 0 0 0 419 6M430 160A60 60 0 0 1 419 194"/><text class="tl tc" x="370" y="199">gap ≈ 6λ</text></svg><figcaption>Diffraction at a gap. The wavelength (the spacing of the wavefronts) is the same before and after the gap. A gap about as wide as the wavelength gives strong spreading, almost semicircular waves; a gap many wavelengths wide leaves the waves almost straight, with spreading only at the edges.</figcaption></figure>
:::

- When the gap is about **the same size as the wavelength**, the diffraction is greatest: the waves leave as nearly circular wavefronts.
- When the gap is **much wider than the wavelength**, the waves go through almost unchanged. Only a little curving occurs at the edges and there is a sharp "shadow" behind the barrier.
- When the gap is **much narrower than the wavelength**, very little energy gets through, but what does spreads widely.
- The wavelength, frequency and speed do not change: only the direction of travel of the wave spreads out.

:::lab Diffraction in a ripple tank
:::steps
1. Set up the ripple tank with the bar producing plane waves. Place two barriers in the water to make a gap, and freeze the pattern with the stroboscope.
2. Start with a gap several wavelengths wide and sketch the wavefronts beyond the gap.
3. Move the barriers closer to narrow the gap until it is about one wavelength wide. Sketch the new pattern.
4. Keep the gap fixed and change the frequency of the vibrator: a lower frequency gives a longer wavelength and so more spreading.
:::
:::

This explains everyday observations. You hear someone speaking round a corner because sound has a wavelength of about 0.1 m to 1 m, comparable to the size of a doorway, so it diffracts strongly. You cannot see round the corner, because the wavelength of light (about \(5 \times 10^{-7}\,\mathrm{m}\)) is thousands of times smaller than a doorway, so light diffracts so little that it appears to travel in straight lines.

:::eg Long-wave radio has a frequency of 200 kHz and FM radio has a frequency of 100 MHz. Find both wavelengths and explain why long-wave radio can be received behind a hill but FM radio is often poor there.
Long wave: \(\lambda = \dfrac{c}{f} = \dfrac{3.00 \times 10^{8}}{2.00 \times 10^{5}} = 1500\,\mathrm{m}\). FM: \(\lambda = \dfrac{3.00 \times 10^{8}}{1.00 \times 10^{8}} = 3.00\,\mathrm{m}\). [C1] [A1]

A hill is comparable in size to the long-wave wavelength, so the waves diffract round it strongly. [B1] The FM wavelength is much smaller than the hill, so there is little diffraction and a radio "shadow" behind the hill. [B1]
:::

## Interference and coherence

You can see the effect of superposition at a larger scale when two sources produce waves of the same type. At some points the waves arrive in phase and the amplitude is large, at others they arrive in antiphase and it is small. This is called interference.

:::def Interference
The superposition of two or more waves to give a resultant wave whose amplitude depends on the phase difference between the waves.
:::

For the pattern to stay in place long enough to see, the phase difference at each point must stay constant.

:::def Coherence
Two sources are coherent if they emit waves with a constant phase difference. Coherent sources must have the same frequency.
:::

Two separate light bulbs are **not** coherent. Each atom emits short bursts of light with random phase, so the phase difference between the bulbs changes randomly billions of times a second and there is no steady pattern: the interference averages out to uniform brightness. To get coherent sources, use one source and split it (two slits in front of a laser, two loudspeakers on one signal generator), so that any change in the source affects both in the same way.

:::html
<figure class="fig"><svg viewBox="0 0 500 292" role="img" aria-label="Two coherent point sources S1 and S2 on the left, three wavelengths apart. Solid curves are lines of constructive interference labelled n equals 0, 1 and 2 (the curves with n equals 1 and 2 appear on both sides of the central line). Dashed curves between them are lines of destructive interference."><path class="ln thin dash" d="M60 138L65 137L71 137L76 137L82 137L88 136L95 135L102 135L109 134L118 133L127 131L137 130L148 128L161 126L175 124L191 122L208 119L228 116L250 112L275 108L303 103L334 98L369 92L409 86"/><path class="ln thin dash" d="M60 152L65 153L71 153L76 153L82 153L88 154L95 155L102 155L109 156L118 157L127 159L137 160L148 162L161 164L175 166L191 168L208 171L228 174L250 178L275 182L303 187L334 192L369 198L409 204"/><path class="ln thin dash" d="M60 122L65 122L69 122L74 121L79 120L85 118L91 116L97 114L103 111L111 108L119 104L128 100L138 95L149 89L161 83L175 75L190 67L207 57L227 46L249 34L273 20"/><path class="ln thin dash" d="M60 168L65 168L69 168L74 169L79 170L85 172L91 174L97 176L103 179L111 182L119 186L128 190L138 195L149 201L161 207L175 215L190 223L207 233L227 244L249 256L273 270"/><path class="ln thin dash" d="M60 108L63 107L66 106L69 105L72 103L76 101L79 97L83 93L88 89L92 83L98 77L103 70L110 61L117 52L124 41L133 28L143 14"/><path class="ln thin dash" d="M60 182L63 183L66 184L69 185L72 187L76 189L79 193L83 197L88 201L92 207L98 213L103 220L110 229L117 238L124 249L133 262L143 276"/><path class="c3" d="M60 145L450 145"/><path class="c3" d="M60 130L65 130L70 130L76 129L81 128L87 127L93 126L100 124L107 123L115 120L124 118L134 115L145 112L156 108L170 103L185 98L202 93L220 86L241 79L265 71L292 62L322 51L356 39L394 26L437 11"/><path class="c3" d="M60 160L65 160L70 160L76 161L81 162L87 163L93 164L100 166L107 167L115 170L124 172L134 175L145 178L156 182L170 187L185 192L202 197L220 204L241 211L265 219L292 228L322 239L356 251L394 264L437 279"/><path class="c3" d="M60 115L64 115L68 114L72 113L77 111L81 109L86 107L92 104L97 100L104 96L111 91L118 85L127 78L136 70L147 62L159 52L172 40L187 28L203 13"/><path class="c3" d="M60 175L64 175L68 176L72 177L77 179L81 181L86 183L92 186L97 190L104 194L111 199L118 205L127 212L136 220L147 228L159 238L172 250L187 262L203 277"/><circle class="fi" cx="60" cy="100" r="5"/><circle class="fi" cx="60" cy="190" r="5"/><text class="tl te" x="50" y="104">S₁</text><text class="tl te" x="50" y="194">S₂</text><text class="tl" x="456" y="149">n = 0</text><text class="tl" x="442" y="15">n = 1</text><text class="tl" x="442" y="283">n = 1</text><text class="tl" x="208" y="17">n = 2</text><text class="tl" x="208" y="281">n = 2</text></svg><figcaption>Lines along which two coherent sources in phase give constructive interference (solid, path difference nλ) and destructive interference (dashed, path difference (n + ½)λ). The sources here are three wavelengths apart, so there are only a few lines. A detector moved across the pattern finds alternate maxima and minima.</figcaption></figure>
:::

The conditions for observable interference fringes from two sources are:

1. The sources must be **coherent**: constant phase difference, so the same frequency.
2. The waves must be of the **same type** and, for transverse waves such as light, **polarised in the same plane** (the oscillations must lie along the same direction, or they cannot fully cancel).
3. The amplitudes at the point should be **similar**, otherwise the minima are not quite zero and the fringes are faint.
4. For light, the sources should be **close together** and the screen far away, so that the fringes are far enough apart to see.

Interference is demonstrated with every kind of wave:

- **Water waves:** two dippers fixed to the same vibrating bar make circular waves of the same frequency. Lines of calm water (destructive) and large ripples (constructive) fan outwards.
- **Sound:** connect two loudspeakers to one signal generator (so they are coherent) and walk across the room in front of them. The loudness rises and falls as you cross constructive and destructive regions.
- **Microwaves:** direct a beam at a metal plate with two parallel slits. A detector moved along an arc on the far side finds a series of maxima and minima.
- **Light:** the double-slit experiment, below.

:::eg Two loudspeakers A and B are connected to the same signal generator, which has a frequency of 850 Hz. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). A microphone at point P is 3.0 m from A and 3.6 m from B. Is the sound at P loud or quiet? What if P is moved to a point 3.0 m from A and 3.4 m from B?
\(\lambda = v/f = 340/850 = 0.40\,\mathrm{m}\). [C1]

First point: path difference \(= 3.6 - 3.0 = 0.60\,\mathrm{m} = 1.5\lambda\). [C1] That is a half-integer number of wavelengths, so the waves arrive in antiphase and the sound is **quiet** (destructive). [A1]

Second point: path difference \(= 0.40\,\mathrm{m} = 1.0\lambda\), a whole number of wavelengths, so the sound is **loud** (constructive). [A1]
(Real rooms reflect sound, so the minima are never completely silent.)
:::

## Young's double-slit experiment

In 1801 Thomas Young passed light through two narrow slits very close together and saw a pattern of bright and dark stripes on a screen, called **fringes**. This could only be explained if light is a wave, since particles passing through two slits would give two bright strips, not many.

A single narrow slit (or a laser beam) lights up two slits S₁ and S₂, so they are coherent sources. Light from each slit spreads out by diffraction and the two beams overlap on the screen. A bright fringe appears where the path difference is a whole number of wavelengths, a dark fringe where it is a half-integer number.

:::html
<figure class="fig"><svg viewBox="0 0 540 270" role="img" aria-label="Double-slit geometry. Light from the left meets a barrier with two slits S1 and S2 a distance a apart. The screen is a distance D to the right. Rays from both slits reach a point P on the screen, a distance x from the central point O. The diagram is not to scale."><path class="c1" d="M20 150H104" marker-end="url(#ah-phys)"/><text class="tl tc" x="62" y="142">light</text><path class="ln thick" d="M160 30V122M160 128V172M160 178V250"/><path class="ln thick" d="M450 30V250"/><circle class="fi" cx="450" cy="150" r="3"/><circle class="fi" cx="450" cy="110" r="3"/><circle class="fi" cx="450" cy="70" r="3"/><circle class="fi" cx="450" cy="190" r="3"/><circle class="fi" cx="450" cy="230" r="3"/><path class="ln thin" d="M160 125L450 110M160 175L450 110"/><path class="c1" d="M140 150V127" marker-end="url(#ah-phys)"/><path class="c1" d="M140 150V173" marker-end="url(#ah-phys)"/><text class="tl ti te" x="128" y="154">a</text><text class="tl te" x="150" y="116">S₁</text><text class="tl te" x="150" y="196">S₂</text><path class="ln thin dash" d="M450 150H496M450 110H496"/><path class="c1" d="M490 130V113" marker-end="url(#ah-phys)"/><path class="c1" d="M490 130V147" marker-end="url(#ah-phys)"/><text class="tl ti" x="498" y="134">x</text><text class="tl" x="458" y="142">O</text><text class="tl" x="458" y="102">P</text><path class="ln thin dash" d="M160 250V262M450 250V262"/><path class="c1" d="M305 262H164" marker-end="url(#ah-phys)"/><path class="c1" d="M305 262H446" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="305" y="256">D</text></svg><figcaption>Not to scale: in a real experiment a is under a millimetre, while D is a metre or more. O is the centre of the pattern (equal path lengths, a bright fringe) and P is the next bright fringe, a distance x from O. The dots on the screen show where the bright fringes are.</figcaption></figure>
:::

The fringes are equally spaced, and the **fringe separation** \(x\) is the distance between the centres of adjacent bright fringes (or adjacent dark fringes).

:::formula Double-slit interference
\[\lambda = \frac{ax}{D} \qquad\text{or}\qquad x = \frac{\lambda D}{a}\]
\(\lambda\): wavelength of the light (m) · \(a\): separation of the centres of the two slits (m) · \(x\): fringe separation on the screen (m) · \(D\): distance from the slits to the screen (m). Valid for \(D \gg a\) (small angles).
:::

:::proof Deriving \(\lambda = ax/D\)
Let the bright fringe next to the central one be at a distance \(x\) from the centre O. Let the line from the midpoint of the slits to this fringe make a small angle \(\theta\) with the line to O.
For \(D \gg a\), the rays from the slits to the point on the screen are almost parallel, and the extra distance travelled by the ray from the further slit is \(a\sin\theta\) (the short side of a right-angled triangle with hypotenuse \(a\)).
A bright fringe needs a path difference of one whole wavelength, so \(a\sin\theta = \lambda\).
For a small angle, \(\sin\theta \approx \tan\theta = x/D\).
So \(a \times \dfrac{x}{D} = \lambda\), which gives \(\lambda = \dfrac{ax}{D}\).
The same argument for the nth fringe gives a distance \(nx\) from O, so the spacing is the same between all adjacent fringes.
:::

:::plot The intensity across the screen for \(a = 0.50\,\mathrm{mm}\), \(D = 2.0\,\mathrm{m}\), \(\lambda = 600\,\mathrm{nm}\). The bright fringes are equally spaced, \(x = 2.4\,\mathrm{mm}\) apart, with a dark fringe halfway between each pair. (An idealised pattern from very narrow slits; the brightness of a real pattern fades away from the centre.)
--f "cos(pi*x/2.4)**2" --x -6 6 --y 0 1.4 --xlabel "y / mm" --ylabel "I / I₀" --pt "0,1,centre@n" --pt "2.4,1,next maximum@ne"
:::

:::eg In a double-slit experiment the slit separation is 0.50 mm and the screen is 2.0 m from the slits. The distance across ten fringe spacings is 24 mm. Find the wavelength of the light.
\[x = \frac{24}{10} = 2.4\,\mathrm{mm}\] [C1]
\[\lambda = \frac{ax}{D} = \frac{0.50 \times 10^{-3} \times 2.4 \times 10^{-3}}{2.0} = 6.0 \times 10^{-7}\,\mathrm{m} = 600\,\mathrm{nm}\] [A1]
Measuring across ten spacings and dividing makes the percentage uncertainty in \(x\) ten times smaller than measuring one spacing alone.
:::

:::eg A red laser (λ = 633 nm) lights slits 0.25 mm apart. The screen is 1.5 m away. Find the fringe separation. Then state, with a reason, the effect on the pattern of (a) halving the slit separation, (b) using a blue laser.
\[x = \frac{\lambda D}{a} = \frac{633 \times 10^{-9} \times 1.5}{0.25 \times 10^{-3}} = 3.8 \times 10^{-3}\,\mathrm{m} = 3.8\,\mathrm{mm}\] [C1] [A1]
(a) \(x \propto 1/a\), so halving \(a\) doubles \(x\): the fringes are twice as far apart. [B1] (b) Blue light has a shorter wavelength, and \(x \propto \lambda\), so the fringes move closer together. [B1]
:::

With **white light**, each colour makes its own fringe pattern with a different spacing (red has the largest, violet the smallest). At the centre all colours have zero path difference, so the central fringe is **white**. On either side, the fringes of different colours separate, giving coloured fringes with violet nearest the centre; further out they overlap and wash out to a nearly uniform white.

:::lab Measuring the wavelength of laser light with a double slit
:::steps
1. Shine a laser (**never look into the beam; do not let it reflect into anyone's eyes**) through a double slit of known separation \(a\) onto a distant white screen.
2. Measure the distance \(D\) from the slits to the screen with a metre rule or tape. Make it as large as possible.
3. Measure the distance across as many fringes as are clear (for example 10 spacings) using a ruler on the screen, then divide to get \(x\).
4. Calculate \(\lambda = ax/D\). Repeat for several values of \(D\), plot \(x\) against \(D\), and find \(\lambda\) from the gradient: gradient \(= \lambda/a\).
:::
:::

Change the slit separation, the screen distance and the colour in the tool below. Watch how the fringe separation responds, and check that the readout agrees with \(x = \lambda D/a\).

:::html
<div class="widget" data-w="phys-fringes" data-mode="double" data-a="0.5" data-d="2.0" data-lambda="600"></div>
:::

## The diffraction grating

A **diffraction grating** is a plate with a very large number of equally spaced parallel slits: typically 100 to 1000 per millimetre. Light passing through each slit diffracts, and the beams from all the slits interfere. The result is a small number of very sharp bright spots (the **maxima**) at definite angles, much brighter and sharper than double-slit fringes.

The **grating spacing** \(d\) is the distance between the centres of adjacent slits. If the grating has \(N\) lines per metre, then \(d = 1/N\). For example, 300 lines per millimetre is \(N = 3.00 \times 10^{5}\) lines per metre, so \(d = 3.33\,\mathrm{\mu m}\).

:::html
<figure class="fig wide"><svg viewBox="0 0 600 300" role="img" aria-label="Left: parallel light meets a diffraction grating, and maxima leave at angles to the straight-through direction: the zero order straight ahead, the first orders at angle theta above and below, and the second orders at larger angles. Right: an enlarged view of two adjacent slits a distance d apart, showing that the rays at angle theta have a path difference of d sin theta."><path class="c1" d="M20 150H130" marker-end="url(#ah-phys)"/><path class="ln thick" d="M140 40V260"/><text class="tl tc" x="140" y="30">grating</text><path class="ln" d="M140 150H380"/><path class="ln" d="M140 150L356 71"/><path class="ln" d="M140 150L356 229"/><path class="ln" d="M140 150L257 41"/><path class="ln" d="M140 150L257 259"/><path class="ln thin dash" d="M140 150H210"/><path class="ln thin" d="M200 150A60 60 0 0 0 196 130"/><text class="tl ti" x="206" y="143">θ</text><text class="tl" x="386" y="154">n = 0</text><text class="tl" x="362" y="70">n = 1</text><text class="tl" x="362" y="240">n = −1</text><text class="tl" x="262" y="38">n = 2</text><text class="tl" x="262" y="272">n = −2</text><circle class="fi" cx="470" cy="100" r="4"/><circle class="fi" cx="470" cy="150" r="4"/><text class="tl te" x="460" y="104">S₁</text><text class="tl te" x="460" y="154">S₂</text><path class="ln" d="M470 100L570 54"/><path class="ln" d="M470 150L570 104"/><path class="ln thin dash" d="M470 100L489 141"/><path class="c3" d="M470 150L489 141"/><path class="ln thin dash" d="M470 150H550"/><path class="ln thin" d="M530 150A60 60 0 0 0 524.5 124.9"/><text class="tl ti" x="536" y="143">θ</text><path class="c1" d="M436 125V102" marker-end="url(#ah-phys)"/><path class="c1" d="M436 125V148" marker-end="url(#ah-phys)"/><text class="tl ti te" x="428" y="129">d</text><text class="tl" x="492" y="170">d sin θ</text><text class="tl tc" x="520" y="200">two adjacent slits</text><text class="tl tc" x="520" y="216">(enlarged)</text></svg><figcaption>Left: a grating gives a zero-order beam straight ahead and orders n = ±1, ±2, … at larger and larger angles. Right: for rays leaving at angle θ, the ray from the lower slit travels an extra distance d sin θ (the thick segment), so adjacent slits reinforce when d sin θ = nλ.</figcaption></figure>
:::

:::formula The diffraction grating
\[d\sin\theta = n\lambda \qquad\qquad d = \frac{1}{N}\]
\(d\): distance between adjacent slits (m) · \(\theta\): angle between the straight-through direction and the nth order · \(n\): order of the maximum (0, 1, 2, …) · \(\lambda\): wavelength (m) · \(N\): number of lines per unit length (m⁻¹). The highest order that can be seen is the largest whole number with \(n < d/\lambda\), because \(\sin\theta\) cannot be more than 1.
:::

:::proof Deriving \(d\sin\theta = n\lambda\)
Consider light from two adjacent slits of a grating, leaving in a direction at angle \(\theta\) to the straight-through direction. A distant screen (or a lens) brings the parallel rays together.
The rays are almost parallel, and the ray from the lower slit has to travel an extra distance compared with the ray from the upper slit. That distance is the short side of a right-angled triangle with hypotenuse \(d\) and angle \(\theta\), so the path difference is \(d\sin\theta\).
Light from the two slits reinforces when the path difference is a whole number of wavelengths: \(d\sin\theta = n\lambda\).
The same condition holds for every pair of adjacent slits, so all the slits reinforce in the same directions. At any other angle, the contributions from all the slits cancel in pairs, so the maxima are sharp and the rest of the screen is dark.
:::

:::eg A grating has 300 lines per millimetre. Monochromatic light of wavelength 589 nm falls normally on it. Find the angles of the first and second order maxima, the highest order and the total number of maxima.
\[d = \frac{1}{3.00 \times 10^{5}} = 3.33 \times 10^{-6}\,\mathrm{m}\] [C1]
First order: \(\sin\theta_1 = \dfrac{\lambda}{d} = \dfrac{589 \times 10^{-9}}{3.33 \times 10^{-6}} = 0.1767\), so \(\theta_1 = 10.2^\circ\). [A1]

Second order: \(\sin\theta_2 = 2 \times 0.1767 = 0.3534\), so \(\theta_2 = 20.7^\circ\). [A1]

Highest order: \(d/\lambda = 3.33 \times 10^{-6} / 589 \times 10^{-9} = 5.66\), so \(n_{\max} = 5\). [B1] There are maxima on both sides and in the centre: \(2 \times 5 + 1 = 11\) in total. [B1]
:::

A grating separates colours. For white light, the zero order is white (all wavelengths have \(\theta = 0\)), and each higher order is a **spectrum**, with violet (smaller \(\lambda\)) at a smaller angle than red. Because \(n\lambda\) is what matters, the higher-order spectra are wider, and they begin to overlap.

:::lab Measuring the wavelength of light with a diffraction grating
:::steps
1. Mount the grating at right angles to a laser beam, a distance \(L\) from a screen. Make sure the beam hits the grating at normal incidence.
2. Mark the positions of the spots on the screen. Measure the distance \(2y\) between the two first-order spots (one on each side of the centre), then halve it to find \(y\). Measure \(L\) with a rule.
3. Calculate the angle \(\theta = \tan^{-1}(y/L)\). Do not use \(y/L\) as if it were \(\sin\theta\) unless the angle is very small.
4. Calculate \(\lambda = d\sin\theta/n\), with \(d = 1/N\) from the number of lines per metre stamped on the grating.
5. Repeat for higher orders and take a mean. Higher orders have larger \(\theta\), so the same uncertainty in \(y\) is a smaller percentage of \(y\).
:::
:::

:::eg A laser beam falls normally on a grating with 600 lines per millimetre. On a screen 1.50 m from the grating the two first-order spots are 1.24 m apart. Find the wavelength of the laser light.
\[y = \frac{1.24}{2} = 0.62\,\mathrm{m} \qquad \theta = \tan^{-1}\!\left(\frac{0.62}{1.50}\right) = 22.5^\circ\] [C1]
\[d = \frac{1}{6.00 \times 10^{5}} = 1.67 \times 10^{-6}\,\mathrm{m}\]
\[\lambda = d\sin\theta = 1.67 \times 10^{-6} \times \sin 22.5^\circ = 6.37 \times 10^{-7}\,\mathrm{m} = 637\,\mathrm{nm}\] [C1] [A1]
:::

Explore a grating in the tool below. Change the lines per millimetre and the wavelength, and watch the orders spread out, and the highest order change. Switch on white light to see the spectra of the different orders overlap.

:::html
<div class="widget" data-w="phys-fringes" data-mode="grating" data-n="300" data-lambda="589"></div>
:::

:::eg White light covers 400 nm to 700 nm. Explain why the first-order and second-order spectra from a grating do not overlap, but the second and third orders do. A grating has 300 lines per millimetre: find the angular range of the overlap between the second and third orders.
The first order extends to red at \(\sin\theta = 700 \times 10^{-9}/d\). The second order starts with violet at \(\sin\theta = 2 \times 400 \times 10^{-9}/d = 800 \times 10^{-9}/d\), which is larger: there is a gap. [B1]

The third order starts at violet \(3 \times 400 = 1200\,\mathrm{nm}\) (over \(d\)), but the second order ends at red \(2 \times 700 = 1400\,\mathrm{nm}\) (over \(d\)). Because \(1200 < 1400\), the third-order violet appears at a smaller angle than the second-order red: they overlap. [B1]

With \(d = 3.33\,\mathrm{\mu m}\): third-order violet \(\sin\theta = 1200/3333 = 0.360\), so \(\theta = 21.1^\circ\); second-order red \(\sin\theta = 1400/3333 = 0.420\), so \(\theta = 24.8^\circ\). The overlap is from \(21.1^\circ\) to \(24.8^\circ\). [A1]
:::

:::warn Mix-ups to avoid
**\(a\) and \(d\):** \(a\) is the separation of two slits in Young's experiment, \(d\) is the separation of adjacent slits on a grating, and \(d = 1/N\). **Lines per millimetre:** change to lines per metre before taking the reciprocal. **Small angles:** \(\lambda = ax/D\) is only valid when the angles are small; the grating formula \(d\sin\theta = n\lambda\) is exact, but to find \(\theta\) from measurements use \(\tan^{-1}(y/L)\). **Number of maxima:** the highest order \(n_{\max}\) gives \(2n_{\max} + 1\) maxima in total, not \(n_{\max}\). **Diffraction:** the wave does not change wavelength or frequency when it diffracts. **Stationary wave wavelength:** it is twice the distance between adjacent nodes, not the distance itself.
:::

:::board
AQA and OCR use the same equations. AQA writes the double-slit equation as \(w = \lambda D/s\), with fringe width \(w\) and slit separation \(s\). AQA also uses the equation for the speed of a wave on a string, \(c = \sqrt{T/\mu}\), which Cambridge does not require.
:::

:::eg Spot the error: the distance between adjacent minima of a stationary microwave pattern is 1.4 cm. The speed of microwaves is \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\). Find the frequency.
A student wrote this answer.

Line 1: \(\lambda = 1.4\,\mathrm{cm} = 0.014\,\mathrm{m}\)
Line 2: \(f = \dfrac{c}{\lambda} = \dfrac{3.00 \times 10^{8}}{0.014} = 2.14 \times 10^{10}\,\mathrm{Hz}\)

**Line 1 is wrong: adjacent nodes (or minima) are \(\lambda/2\) apart, so the wavelength is twice the distance measured, 2.8 cm. The answer mark is lost, although the method in line 2 is right.** [C1] [A0]

Correct working: \(\lambda = 2 \times 1.4 = 2.8\,\mathrm{cm}\), \(f = \dfrac{3.00 \times 10^{8}}{0.028} = 1.07 \times 10^{10}\,\mathrm{Hz}\). [A1]

Check: microwave ovens use 2.45 GHz, and microwaves used in school experiments are about 10 GHz, so \(10^{10}\,\mathrm{Hz}\) is the right order of size, and the student's answer is exactly double.
:::

:::try Start easy, finish at exam standard
Q: Two waves meet in phase, with amplitudes 3.0 mm and 2.0 mm. What is the resultant amplitude? What if they meet in antiphase?
A: In phase: \(3.0 + 2.0 = 5.0\,\mathrm{mm}\). In antiphase: \(3.0 - 2.0 = 1.0\,\mathrm{mm}\).
Q: The distance between adjacent nodes of a stationary wave on a string is 0.35 m, and the waves travel at \(140\,\mathrm{m\,s^{-1}}\). Find the wavelength and frequency.
A: \(\lambda = 2 \times 0.35 = 0.70\,\mathrm{m}\) and \(f = v/\lambda = 140/0.70 = 200\,\mathrm{Hz}\).
Q: A string 0.60 m long is fixed at both ends. Write down the wavelength of the first harmonic and of the second harmonic.
A: First: \(L = \lambda/2\), so \(\lambda = 1.2\,\mathrm{m}\). Second: \(L = \lambda\), so \(\lambda = 0.60\,\mathrm{m}\).
Q: A pipe 0.25 m long is closed at one end. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). Find the lowest resonant frequency.
A: \(L = \lambda/4\), so \(\lambda = 1.0\,\mathrm{m}\) and \(f = 340/1.0 = 340\,\mathrm{Hz}\).
Q: Two coherent sources emit in phase with wavelength 0.30 m. State the type of superposition at a point where the path difference is 0.90 m, and at a point where it is 0.75 m.
A: \(0.90/0.30 = 3\) wavelengths: constructive. \(0.75/0.30 = 2.5\) wavelengths: destructive.
Q: In a double-slit experiment, \(a = 0.40\,\mathrm{mm}\), \(D = 1.5\,\mathrm{m}\) and \(\lambda = 550\,\mathrm{nm}\). Find the fringe separation.
A: \(x = \dfrac{\lambda D}{a} = \dfrac{550 \times 10^{-9} \times 1.5}{0.40 \times 10^{-3}} = 2.1 \times 10^{-3}\,\mathrm{m} = 2.1\,\mathrm{mm}\).
Q: A diffraction grating has 200 lines per millimetre. Find the slit spacing \(d\).
A: \(N = 2.00 \times 10^{5}\,\mathrm{m^{-1}}\), so \(d = 1/N = 5.0 \times 10^{-6}\,\mathrm{m} = 5.0\,\mathrm{\mu m}\).
Q: Light of wavelength 500 nm falls normally on a grating of 400 lines per millimetre. Find the angle of the first-order maximum.
A: \(d = 2.50\,\mathrm{\mu m}\), so \(\sin\theta = \lambda/d = 0.20\) and \(\theta = 11.5^\circ\).
Q: In a ripple tank, plane waves pass through a gap. The gap is widened from about one wavelength to five wavelengths. Describe the change in the waves beyond the gap.
A: With the narrow gap, the waves spread out widely beyond the gap in almost circular wavefronts. With the wide gap, the waves go through almost straight with only slight spreading at the edges, so the diffraction is less. The wavelength does not change.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ State what is meant by coherent sources.
A: Sources that have a constant phase difference between the waves they emit (and so the same frequency). [B1]
Q: [3 marks] ★ Explain how a stationary wave is formed on a stretched string fixed at both ends.
A: A wave travelling along the string is reflected at the fixed end, so the incident and reflected waves of the same frequency travel in opposite directions and superpose. [B1] At the nodes the two waves are always in antiphase, so there is destructive superposition and the displacement is always zero. [B1] At the antinodes the waves are always in phase, so there is constructive superposition and the amplitude is a maximum. [B1]
Q: [4 marks] ★★ A pipe of length 0.34 m is closed at one end and open at the other. The speed of sound in air is \(340\,\mathrm{m\,s^{-1}}\). State where there is a node and an antinode for the lowest-frequency stationary wave, and calculate the two lowest resonant frequencies. End corrections may be neglected.
A: There is a node at the closed end and an antinode at the open end. [B1] \(L = \lambda/4\), so \(\lambda = 4 \times 0.34 = 1.36\,\mathrm{m}\) [C1] and \(f_1 = 340/1.36 = 250\,\mathrm{Hz}\). [A1] The next resonance has \(L = 3\lambda/4\), at \(3f_1 = 750\,\mathrm{Hz}\). [A1]
Q: [3 marks] ★★ In a double-slit experiment with monochromatic light, the slit separation is halved and the distance from the slits to the screen is doubled. State and explain the effect on the fringe separation.
A: The fringe separation is given by \(x = \lambda D/a\), so \(x \propto D/a\). [B1] Halving \(a\) doubles \(x\). [B1] Doubling \(D\) doubles \(x\) again, so the fringe separation becomes four times larger. [B1]
Q: [4 marks] ★★ Two loudspeakers A and B are connected to the same signal generator, which has a frequency of 850 Hz. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). (a) Calculate the wavelength of the sound. (b) A microphone is placed at P, which is 3.0 m from A and 3.6 m from B. State whether the sound at P is loud or quiet and explain why.
A: (a) \(\lambda = v/f = 340/850\) [C1] \(= 0.40\,\mathrm{m}\). [A1] (b) The path difference is \(0.60\,\mathrm{m} = 1.5\lambda\), [B1] a half-integer number of wavelengths, so the waves arrive in antiphase: destructive interference and the sound is quiet. [B1]
Q: [4 marks] ★★ A diffraction grating has 500 lines per millimetre. Light of wavelength 650 nm falls normally on it. Calculate the highest order of maximum that can be observed and the angle at which it occurs.
A: \(d = \dfrac{1}{5.00 \times 10^{5}} = 2.00 \times 10^{-6}\,\mathrm{m}\). [C1] The maximum order has \(n < d/\lambda = 3.08\), so \(n = 3\). [A1] \(\sin\theta = \dfrac{3\lambda}{d} = \dfrac{3 \times 650 \times 10^{-9}}{2.00 \times 10^{-6}} = 0.975\) [C1] so \(\theta = 77.2^\circ\). [A1]
Q: [6 marks] ★★★ Describe how you would use a diffraction grating of 300 lines per millimetre and a laser to determine the wavelength of the laser light. Include a sample calculation using the measurements shown, and state the main source of uncertainty. A student measures a distance of 0.730 m between the two first-order spots on a screen placed 2.00 m from the grating.
H: Which distance and which angle do you need? Remember to halve the distance between the two first-order spots.
H: Do not forget to find the angle from \(\tan\theta = y/L\), then use \(d\sin\theta = n\lambda\).
A: Direct the laser beam at normal incidence onto the grating, with a screen at a measured distance \(L\) behind it. [B1] Measure the distance between the first-order spots on both sides of the central spot, and \(L\); half of the distance is \(y = 0.365\,\mathrm{m}\). [B1] \(\theta = \tan^{-1}(0.365/2.00) = 10.3^\circ\) [C1] and \(d = 1/(3.00 \times 10^{5}) = 3.33 \times 10^{-6}\,\mathrm{m}\). \(\lambda = d\sin\theta\) [C1] \(= 3.33 \times 10^{-6} \times \sin 10.3^\circ = 5.98 \times 10^{-7}\,\mathrm{m}\) (598 nm). [A1] The main uncertainty is the measurement of \(y\), because the spots have a width and so their centres are hard to locate; this can be reduced by using a larger \(L\), measuring the distance across several orders, or using a higher order. [B1]
Q: [5 marks] ★★★ Light containing two wavelengths, 480 nm and 640 nm, falls normally on a grating with 400 lines per millimetre. (a) The lowest-order maximum for which both wavelengths appear at the same angle is formed by order \(n_1\) of the 480 nm light and order \(n_2\) of the 640 nm light. Find \(n_1\) and \(n_2\). (b) Calculate the angle at which these two maxima coincide.
H: At the same angle, \(d\sin\theta\) is the same for both, so \(n_1 \times 480 = n_2 \times 640\).
H: The ratio 480 : 640 simplifies to 3 : 4.
A: (a) At the same angle \(d\sin\theta = n_1\lambda_1 = n_2\lambda_2\), so \(n_1/n_2 = 640/480 = 4/3\). [C1] The smallest whole numbers are \(n_1 = 4\) and \(n_2 = 3\). [A1] (b) \(d = 2.50\,\mathrm{\mu m}\) and \(\sin\theta = \dfrac{4 \times 480 \times 10^{-9}}{2.50 \times 10^{-6}} = 0.768\) [C1] so \(\theta = 50.2^\circ\). [A1] Both orders exist, because \(d/\lambda\) is 5.2 for the 480 nm light and 3.9 for the 640 nm light. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Two loudspeakers are 1.5 m apart and emit in phase at 1700 Hz. The speed of sound is \(340\,\mathrm{m\,s^{-1}}\). A listener walks along a line parallel to the line joining the speakers, 4.0 m away from it, starting opposite the midpoint. (a) Calculate the wavelength. (b) The first quiet position is at a distance \(y\) from the midpoint. Show that \(y = 0.272\,\mathrm{m}\) by finding the path difference at that point exactly, without any small-angle approximation. (c) Compare it with the value from \(x = \lambda D/a\) and explain why the two differ.
H: A quiet position needs a path difference of \(\lambda/2\).
H: Use Pythagoras: the distances from the listener to the two speakers are \(\sqrt{4.0^2 + (y + 0.75)^2}\) and \(\sqrt{4.0^2 + (y - 0.75)^2}\).
A: (a) \(\lambda = 340/1700\) [C1] \(= 0.200\,\mathrm{m}\). [A1] (b) The two distances are \(\sqrt{4.0^2 + 1.022^2} = 4.1285\,\mathrm{m}\) and \(\sqrt{4.0^2 + 0.478^2} = 4.0285\,\mathrm{m}\) [M1], whose difference is \(0.100\,\mathrm{m} = \lambda/2\), so this is the first minimum. [A1] (c) The small-angle formula gives \(x = \lambda D/a = 0.200 \times 4.0/1.5 = 0.533\,\mathrm{m}\) so the first minimum is at \(x/2 = 0.267\,\mathrm{m}\), about 2% smaller than the exact 0.272 m. [B1] The formula assumes that the distance to the listener is \(D\) and that \(\sin\theta \approx \tan\theta\); at \(y = 0.27\,\mathrm{m}\) the angle is not small enough for this to be exact (the distance to the listener is actually more than \(D\)). [B1]
Q: [5 marks] ★★★ White light (400 nm to 700 nm) falls normally on a grating of 300 lines per millimetre. (a) Explain why the first-order and second-order spectra do not overlap. (b) Show that the second- and third-order spectra overlap. (c) Calculate the angles at which the overlap begins and ends.
H: Compare the largest value of \(n\lambda\) in one order with the smallest value in the next.
A: (a) The first order ends with red at \(1 \times 700 = 700\,\mathrm{nm}\), but the second starts with violet at \(2 \times 400 = 800\,\mathrm{nm}\). Since \(\sin\theta = n\lambda/d\), \(700 < 800\) means the first order ends at a smaller angle than the second begins. [B1] (b) The second order ends with red at \(2 \times 700 = 1400\,\mathrm{nm}\) and the third begins with violet at \(3 \times 400 = 1200\,\mathrm{nm}\). Since \(1200 < 1400\), the third-order violet is at a smaller angle than the second-order red, so they overlap. [B1] (c) \(d = 3.33\,\mathrm{\mu m}\). The overlap begins where third-order violet appears: \(\sin\theta = 1200/3333 = 0.360\) [C1] so \(\theta = 21.1^\circ\). [A1] It ends at the second-order red: \(\sin\theta = 1400/3333 = 0.420\) so \(\theta = 24.8^\circ\). [A1]
:::

:::quiz
? Two waves of equal frequency meet at a point and the resultant amplitude is zero. Which statement must be true?
- The waves have different amplitudes.
- The waves are in phase.
+ The waves have equal amplitudes and a phase difference of 180°.
- The waves are travelling in the same direction.
> Complete cancellation requires equal amplitudes and antiphase (a path difference of a half-integer number of wavelengths). In phase waves add; unequal amplitudes cannot cancel fully.
? Which statement about a stationary wave on a string is correct?
- Energy is transferred along the string.
- All points on the string oscillate with the same amplitude.
- Points between two adjacent nodes oscillate with a phase difference that increases along the string.
+ All points between two adjacent nodes oscillate in phase.
> Within one loop, every point reaches its maximum at the same time, with an amplitude that depends on the position. The neighbouring loop oscillates in antiphase.
? A pipe is closed at one end. What is the length of the pipe, in terms of the wavelength \(\lambda\), when the lowest-frequency stationary wave forms?
+ \(\lambda/4\)
- \(\lambda/2\)
- \(\lambda\)
- \(3\lambda/4\)
> The closed end is a node and the open end is an antinode, a distance of a quarter of a wavelength. \(\lambda/2\) is the lowest mode for a pipe open at both ends, and \(3\lambda/4\) is the second mode of the closed pipe.
? Why do two separate filament lamps not produce an interference pattern?
- Light waves cannot interfere.
+ Their light has no constant phase difference between them, so they are not coherent.
- Their light has different speeds.
- The light is not diffracted.
> Light from separate lamps is made of random, independent bursts, so the phase difference changes irregularly and the pattern averages out. Light waves do interfere, and all light travels at the same speed in air.
? In a double-slit experiment, the distance between the slits and the screen is increased. What happens to the fringe separation?
+ It increases.
- It decreases.
- It stays the same.
- The fringes disappear.
> \(x = \lambda D/a\), so \(x\) is proportional to \(D\): a longer distance spreads the pattern out.
? A diffraction grating is replaced by one with more lines per millimetre. What happens to the angle of the first-order maximum for the same light?
+ It increases.
- It decreases.
- It stays the same.
- There is no first-order maximum.
> More lines per millimetre means a smaller spacing \(d\), and \(\sin\theta = \lambda/d\) becomes larger, so the angle increases.
? For which gap does a wave of wavelength 0.020 m diffract most?
- 2.0 m
- 0.20 m
+ 0.020 m
- 20 m
> Diffraction is greatest when the gap is about the same size as the wavelength. For a gap many times wider than the wavelength, the waves pass through almost undisturbed.
? Light of wavelength 630 nm falls on a grating with spacing 2.0 μm. How many maxima appear on the screen, including the central one?
- 3
- 6
+ 7
- 9
> \(d/\lambda = 2000/630 = 3.17\), so the highest order is 3. There are 3 orders on each side plus the central maximum: \(2 \times 3 + 1 = 7\). Counting only one side gives 3 and counting orders without the centre gives 6.
:::

:::checklist What you can now do
- [ ] I can explain and use the principle of superposition, including constructive and destructive superposition and path difference.
- [ ] I can explain how a stationary wave forms using a graphical method, and identify nodes and antinodes.
- [ ] I can find the wavelength of a stationary wave from the positions of its nodes or antinodes.
- [ ] I can describe stationary-wave experiments with a stretched string, microwaves and an air column, and use them to find a wavelength or a speed.
- [ ] I can explain diffraction and describe how the gap width compared with the wavelength changes it, for example in a ripple tank.
- [ ] I can define interference and coherence, and state the conditions for observable two-source fringes.
- [ ] I can describe two-source interference with water waves, sound, light and microwaves.
- [ ] I can use \(\lambda = ax/D\) for a double slit and explain how the pattern changes with \(a\), \(D\) and \(\lambda\).
- [ ] I can use \(d\sin\theta = n\lambda\), find the maximum order, and describe how to measure a wavelength with a diffraction grating.
:::

:::recap
- Superposition: the resultant displacement is the sum of the individual displacements. Constructive when the path difference is \(n\lambda\), destructive when it is \((n + \tfrac12)\lambda\) (sources in phase).
- A stationary wave comes from two waves of the same frequency travelling in opposite directions. Nodes (zero amplitude) and antinodes are \(\lambda/2\) apart, and no energy is transferred along the wave. Points in one loop are in phase; adjacent loops are in antiphase.
- String fixed at both ends: \(L = n\lambda/2\). Pipe closed at one end: \(L = \lambda/4, 3\lambda/4, \dots\) Pipe open at both ends: \(L = \lambda/2, \lambda, \dots\)
- Microwaves reflected from a metal plate: adjacent nodes \(\lambda/2\) apart. Resonance tube: successive resonances \(\lambda/2\) apart, which removes the end correction.
- Diffraction: spreading at a gap or edge, greatest when the gap is about one wavelength. Wavelength and frequency do not change.
- Coherent sources have a constant phase difference. Observable fringes need coherent sources, similar amplitudes and the same polarisation.
- Double slit: \(\lambda = ax/D\), with \(D \gg a\). Halving \(a\) doubles \(x\); white light gives a white central fringe and coloured fringes.
- Grating: \(d\sin\theta = n\lambda\), \(d = 1/N\), highest order \(n < d/\lambda\), and \(2n_{\max} + 1\) maxima in all. Sharper and brighter than double-slit fringes. Violet is deviated less than red; the second and third spectra overlap.
:::

:::links
- explore: [Wave Interference](https://phet.colorado.edu/en/simulations/wave-interference) · PhET · see water, sound and light waves interfere from two sources and change the slit separation
- explore: [Wave on a String](https://phet.colorado.edu/en/simulations/wave-on-a-string) · PhET · reflect pulses from a fixed end and watch stationary waves form
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the superposition questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Electricity](#phys.electricity)
