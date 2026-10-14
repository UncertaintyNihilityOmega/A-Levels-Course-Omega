@chapter phys.oscillations
@title Oscillations
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary Simple harmonic motion: the defining equation a = −ω²x, its sine and cosine solutions, the graphs of displacement, velocity and acceleration, the exchange of kinetic and potential energy, and then damping, forced oscillations and resonance.

:::why
Almost everything that repeats is an oscillation: a guitar string, the atoms in a solid, a car on its springs, the current in a radio tuner. Simple harmonic motion is the simplest oscillation and the model for all of them, and the same three equations describe a mass on a spring, a pendulum and a vibrating molecule. Damping and resonance explain why a car glides over a bump, why a bridge can shake, and how a radio picks one station.
:::

**Before you start**, you need angular speed and radians from [Motion in a circle](#phys.circular), period and phase difference from [Waves](#phys.waves), and the sine and cosine graphs from [Trigonometry](#math.p1.trig).

:::try Warm-up
Q: A wheel turns once every 0.50 s. What is its angular speed? (from [Motion in a circle](#phys.circular))
A: \(\omega = 2\pi/T = 2\pi/0.50 = 12.6\,\mathrm{rad\,s^{-1}}\).
Q: Two points on a progressive wave are one quarter of a wavelength apart. What is their phase difference? (from [Waves](#phys.waves))
A: One whole wavelength is a phase change of \(2\pi\,\mathrm{rad}\), so a quarter of it is \(\pi/2\,\mathrm{rad}\), which is \(90^\circ\).
Q: A spring of force constant \(50\,\mathrm{N\,m^{-1}}\) is stretched by 0.10 m. How much energy does it store? (from [Deformation of solids](#phys.solids))
A: \(E = \tfrac12 kx^2 = \tfrac12 \times 50 \times 0.10^2 = 0.25\,\mathrm{J}\).
:::

## Oscillations and the words that describe them

An **oscillation** is a repeated back-and-forth motion about a fixed point. A pendulum swings, a mass bobs on a spring, the cone of a loudspeaker vibrates, and the atoms of a solid jiggle about their places. In every case there is an **equilibrium position**, the place where the object would stay at rest if it were left alone, and a force that pulls the object back towards it whenever it is displaced.

Seven words describe an oscillation. Learn the definitions: they are asked directly.

:::def Displacement (of an oscillator)
The distance of the oscillator from its equilibrium position, in a stated direction. It is a vector, so it has a sign: positive on one side of equilibrium and negative on the other.
:::

:::def Amplitude
The maximum displacement from the equilibrium position. Symbol \(x_0\).
:::

:::def Period
The time for one complete oscillation. Symbol \(T\).
:::

:::def Frequency
The number of oscillations per unit time. Symbol \(f\), in hertz (\(1\,\mathrm{Hz} = 1\,\mathrm{s^{-1}}\)).
:::

:::def Angular frequency
\(\omega = 2\pi f\), that is \(2\pi\) times the frequency. It is measured in \(\mathrm{rad\,s^{-1}}\). One complete oscillation is a phase change of \(2\pi\,\mathrm{rad}\), so \(\omega\) is the phase change per second.
:::

:::formula Period, frequency and angular frequency
\[f = \frac{1}{T} \qquad\qquad \omega = 2\pi f = \frac{2\pi}{T}\]
\(T\): period (s) · \(f\): frequency (Hz) · \(\omega\): angular frequency (\(\mathrm{rad\,s^{-1}}\)).
:::

:::warn Do not mix up f and ω
The data in a question may give \(f\), \(T\) or \(\omega\). Every equation in this chapter needs \(\omega\) in \(\mathrm{rad\,s^{-1}}\). Convert first: \(\omega = 2\pi f\) or \(2\pi/T\). A common slip is to put \(f\) where \(\omega\) belongs, which makes the answer wrong by a factor of \(2\pi \approx 6.3\). Another is to read the **peak-to-peak** height of a graph as the amplitude: the amplitude is measured from the equilibrium line to a crest, so it is half the peak-to-peak height.
:::

:::eg A guitar string vibrates at 440 Hz. Find its period and angular frequency.
\[T = \frac{1}{f} = \frac{1}{440} = 2.27 \times 10^{-3}\,\mathrm{s} \qquad \omega = 2\pi f = 2\pi \times 440 = 2.76 \times 10^{3}\,\mathrm{rad\,s^{-1}}\]
The string completes 440 oscillations every second, so each takes about 2.3 ms.
:::

### Phase difference

Two oscillators of the same frequency need not move together. One may reach its maximum displacement a little later than the other. The fraction of a cycle by which one is ahead of the other is the **phase difference** \(\Delta\phi\). A whole cycle is \(2\pi\,\mathrm{rad}\) (\(360^\circ\)), so a time lag \(\Delta t\) gives

:::formula Phase difference from a time lag
\[\Delta\phi = 2\pi\,\frac{\Delta t}{T} \qquad\text{(radians)} \qquad\quad \Delta\phi = 360^\circ \times \frac{\Delta t}{T}\]
\(\Delta t\): time by which one oscillator lags the other · \(T\): their common period. A phase difference of \(0\) means *in phase*; \(\pi\,\mathrm{rad}\) (180°) means *in antiphase* (they always move in opposite directions).
:::

A general oscillation is written \(x = x_0 \sin(\omega t + \phi)\), where \(\phi\) is the phase of the oscillator compared with a reference that has \(\phi = 0\).

:::eg Two identical pendulums have a period of 0.80 s. Pendulum B passes through its equilibrium position, moving the same way, 0.10 s after pendulum A. Find the phase difference.
\[\Delta\phi = 2\pi \times \frac{0.10}{0.80} = \frac{\pi}{4} = 0.785\,\mathrm{rad}\]
That is \(45^\circ\). Pendulum B lags pendulum A by one eighth of a cycle.
:::

## Simple harmonic motion

Pull a mass on a spring down and release it. The spring pulls it back up. The further down you pulled it, the harder the spring pulls, so the acceleration is larger when the displacement is larger. The restoring force always points towards equilibrium, opposite to the displacement. This pattern has a name.

:::def Simple harmonic motion (SHM)
Motion in which the acceleration of the object is proportional to its displacement from a fixed point and is always directed towards that point (that is, in the opposite direction to the displacement).
:::

Both halves of the definition matter. "Proportional" alone describes a car whose acceleration grows with distance travelled. "Opposite direction" is what makes the object turn round and return. The definition as an equation is

:::key The defining equation of SHM
\[a = -\omega^2 x\]
\(a\): acceleration (\(\mathrm{m\,s^{-2}}\)) · \(x\): displacement from equilibrium (m) · \(\omega\): angular frequency (\(\mathrm{rad\,s^{-1}}\)). The minus sign says that \(a\) points opposite to \(x\). The constant of proportionality is written \(\omega^2\) because it turns out to equal the square of the angular frequency of the motion.
:::

To prove that a system is SHM, you must show that the net force (and so the acceleration) is proportional to the displacement and opposite to it. You do not need the solution of the equation for that. The two standard cases are below.

:::html
<figure class="fig"><svg viewBox="8 10 630 258" role="img" aria-label="Two oscillators. Panel (a): a block on a horizontal spring displaced a distance x to the right of its dashed equilibrium line, with the force F equal to minus k x pointing left. Panel (b): a simple pendulum displaced by an angle theta from the vertical, with the weight mg pointing down and its two components along the string and at right angles to it."><rect class="fi" x="20" y="80" width="8" height="70"/><path class="ln" d="M28 150H290"/><path class="ln" d="M28 128L50 128L55.6 116L66.7 140L77.8 116L88.9 140L100 116L111.1 140L122.2 116L133.3 140L144.4 116L150 128L172 128"/><rect class="fp s-ink sw2" x="172" y="106" width="56" height="44"/><text class="tl tc" x="200" y="132">m</text><path class="ln-m thin dash" d="M160 36V176"/><text class="tl tc" x="160" y="30">equilibrium</text><path class="gr dash" d="M200 106V70"/><path class="c2" d="M200 70H140" marker-end="url(#ah2-phys)"/><text class="tl ta2" x="208" y="74">F = −kx</text><path class="gr dash" d="M200 150V176"/><path class="c1" d="M160 170H200" marker-end="url(#ah-phys)"/><text class="tl tc" x="180" y="190">x</text><rect class="fi" x="420" y="22" width="60" height="8"/><path class="ln-m thin dash" d="M450 30V200"/><path class="ln" d="M450 30L525 159.9"/><path class="ln thin" d="M450 75A45 45 0 0 0 472.5 69"/><text class="tl ti tc" x="468" y="100">θ</text><circle class="fp s-ink sw2" cx="525" cy="160" r="12"/><path class="c1" d="M525 160V240" marker-end="url(#ah-phys)"/><text class="tl ta te" x="518" y="236">mg</text><path class="c2 dash" d="M525 160L559.6 220" marker-end="url(#ah2-phys)"/><text class="tl ta2" x="566" y="230">mg cos θ</text><path class="c2" d="M525 160L490.4 180" marker-end="url(#ah2-phys)"/><text class="tl ta2 tc" x="490" y="202">mg sin θ</text><text class="tl tc" x="155" y="262">(a) Mass on a horizontal spring</text><text class="tl tc" x="500" y="262">(b) Simple pendulum</text></svg><figcaption>(a) When the block is displaced a distance x from equilibrium, the spring exerts a force of size kx back towards equilibrium. (b) The component of the weight at right angles to the string, mg sin θ, always points back towards the vertical. The component along the string is balanced by the tension at the ends of the swing.</figcaption></figure>
:::

:::proof examinable A mass on a spring moves with SHM
A mass \(m\) hangs from a spring of force constant \(k\) (the force per unit extension, from [Deformation of solids](#phys.solids)).
At equilibrium the extension is \(e\) and the weight is balanced by the spring force: \(mg = ke\).
Pull the mass a further distance \(x\) downwards. The extension is now \(e + x\), so the spring force upwards is \(k(e + x)\).
The net force upwards is \(k(e + x) - mg = kx\) (the \(ke\) cancels \(mg\)). Taking displacement downwards as positive, \(F = -kx\).
Newton's second law gives \(ma = -kx\), so \(a = -\dfrac{k}{m}\,x\).
The acceleration is proportional to the displacement and opposite to it, so the motion is SHM, with \(\omega^2 = \dfrac{k}{m}\).
The weight does not appear in the final equation: gravity only changes where the equilibrium position is.
:::

:::proof A simple pendulum moves with SHM for small angles
The bob has mass \(m\) and the string has length \(l\). It is displaced by a small angle \(\theta\) (in radians) from the vertical, a distance \(x\) along the arc.
The component of the weight along the arc, towards the vertical, is \(mg\sin\theta\). The tension has no component along the arc.
So \(ma = -mg\sin\theta\), and the minus sign shows that the force opposes the displacement.
For small angles \(\sin\theta \approx \theta\) (in radians), and \(\theta = x/l\) for an arc \(x\) of a circle of radius \(l\).
Then \(ma = -mg\,\dfrac{x}{l}\), so \(a = -\dfrac{g}{l}\,x\).
This is \(a = -\omega^2 x\) with \(\omega^2 = \dfrac{g}{l}\). The mass cancels, so the period does not depend on it.
:::

From \(\omega^2 = k/m\) and \(\omega^2 = g/l\) and \(T = 2\pi/\omega\), the periods are

:::formula Periods of a spring and a pendulum
\[T = 2\pi\sqrt{\frac{m}{k}} \qquad\qquad T = 2\pi\sqrt{\frac{l}{g}}\]
\(m\): mass (kg) · \(k\): force constant of the spring (\(\mathrm{N\,m^{-1}}\)) · \(l\): pendulum length to the centre of the bob (m) · \(g\): acceleration of free fall. The pendulum result is only valid for small angles. These two formulae are **not** on the Cambridge data sheet: a question that needs them gives them, or asks you to derive \(\omega^2\) as above.
:::

The first formula tells you that a heavier mass oscillates more slowly and a stiffer spring more quickly. The second tells you that a longer pendulum is slower, and that the period does not depend on the bob's mass or (for small swings) on the amplitude.

:::eg A 0.50 kg mass hangs on a spring of force constant \(80\,\mathrm{N\,m^{-1}}\). Find the angular frequency, the period and the frequency of its oscillations.
\[\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{80}{0.50}} = 12.6\,\mathrm{rad\,s^{-1}} \qquad T = \frac{2\pi}{\omega} = \frac{2\pi}{12.65} = 0.497\,\mathrm{s} \qquad f = \frac{1}{T} = 2.01\,\mathrm{Hz}\]
Using the unrounded \(\omega = 12.65\) in the period avoids a rounding error. Notice that the amplitude is not needed: in SHM the period does not depend on it.
:::

:::eg A pendulum has a length of 1.00 m. Find its period on the Earth, where \(g = 9.81\,\mathrm{m\,s^{-2}}\), and on the Moon, where \(g = 1.62\,\mathrm{m\,s^{-2}}\).
Earth: \(T = 2\pi\sqrt{\dfrac{1.00}{9.81}} = 2.01\,\mathrm{s}\).
Moon: \(T = 2\pi\sqrt{\dfrac{1.00}{1.62}} = 4.94\,\mathrm{s}\).
The pendulum is slower on the Moon because the restoring force is weaker there. Its mass does not matter on either world.
:::

:::analogy A shadow of circular motion
Shine a lamp on a point moving round a circle of radius \(x_0\) with steady angular speed \(\omega\), and watch its shadow on a wall at the edge of the circle. The shadow slides up and down the wall with exactly the motion of SHM of amplitude \(x_0\) and angular frequency \(\omega\). The point's speed round the circle, \(\omega x_0\), is the shadow's maximum speed, and its centripetal acceleration, \(\omega^2 x_0\), is the shadow's maximum acceleration. This is why the same symbol \(\omega\) appears in [Motion in a circle](#phys.circular) and here, and why sines and cosines describe SHM.
:::

## Solving the equation: displacement, velocity and acceleration

You are expected to recall the solution of \(a = -\omega^2 x\). If the timing starts as the oscillator passes through equilibrium,

:::key Displacement, velocity and acceleration in SHM
\[x = x_0 \sin\omega t \qquad v = v_0\cos\omega t \qquad a = -\omega^2 x_0 \sin\omega t = -\omega^2 x\]
\[v_0 = \omega x_0 \qquad\qquad a_{\max} = \omega^2 x_0\]
\(x_0\): amplitude (m) · \(v_0\): maximum speed (\(\mathrm{m\,s^{-1}}\)) · \(\omega t\) is an angle in **radians**. The velocity is the gradient of the \(x\)–\(t\) graph and the acceleration is the gradient of the \(v\)–\(t\) graph.
:::

If the timing starts with the oscillator at its maximum displacement (released from rest after being pulled aside), the sine becomes a cosine: \(x = x_0\cos\omega t\) and \(v = -\omega x_0 \sin\omega t\). Which one to use is decided by the starting condition: **at \(t = 0\), is the object at the centre (sine) or at an end (cosine)?** Both describe the same motion with a different choice of zero of time. The data sheet gives \(v = v_0 \cos\omega t\), which pairs with \(x = x_0\sin\omega t\).

:::warn Radians, not degrees
The angle \(\omega t\) is in radians. Set your calculator to radian mode before you evaluate \(\sin\omega t\) or \(\cos\omega t\). In degree mode the numbers look plausible and are wrong, and the error is silent. A quick check: \(\sin(3.77)\) should be about \(-0.59\), not \(0.066\).
:::

### Speed at a given displacement

Often you know where the object is, not when. Eliminate \(t\) between \(x\) and \(v\):

:::proof Why the speed depends on the displacement as ω√(x₀² − x²)
Start with \(x = x_0\sin\omega t\), so \(\sin\omega t = \dfrac{x}{x_0}\).
Also \(v = \omega x_0 \cos\omega t\), so \(\cos\omega t = \dfrac{v}{\omega x_0}\).
Use \(\sin^2\omega t + \cos^2\omega t = 1\): \(\dfrac{x^2}{x_0^2} + \dfrac{v^2}{\omega^2 x_0^2} = 1\).
Multiply by \(\omega^2 x_0^2\): \(\omega^2 x^2 + v^2 = \omega^2 x_0^2\).
So \(v^2 = \omega^2 (x_0^2 - x^2)\), and taking the square root gives both directions of motion.
:::

:::formula Speed at displacement x
\[v = \pm\,\omega\sqrt{x_0^2 - x^2}\]
The \(\pm\) gives the two directions of travel through the point. The speed is greatest (\(\omega x_0\)) at \(x = 0\) and zero at \(x = \pm x_0\). Do **not** write \(v = \omega x\): the speed is not proportional to the displacement (it is zero at \(x = \pm x_0\) and greatest at \(x = 0\)).
:::

:::eg A mass on a spring has amplitude 4.0 cm and period 0.40 s. Find the angular frequency, the maximum speed, the maximum acceleration, the speed when the displacement is 2.0 cm, and the time taken to move from the equilibrium position to a displacement of 2.0 cm.
\[\omega = \frac{2\pi}{T} = \frac{2\pi}{0.40} = 15.7\,\mathrm{rad\,s^{-1}}\] [C1]
\[v_0 = \omega x_0 = 15.71 \times 0.040 = 0.628\,\mathrm{m\,s^{-1}} \qquad a_{\max} = \omega^2 x_0 = 15.71^2 \times 0.040 = 9.87\,\mathrm{m\,s^{-2}}\] [A1]
Speed at 2.0 cm (convert to metres):
\[v = \omega\sqrt{x_0^2 - x^2} = 15.71\sqrt{0.040^2 - 0.020^2} = 0.544\,\mathrm{m\,s^{-1}}\] [A1]
Time from the centre: \(x = x_0\sin\omega t\) gives \(\sin\omega t = 0.020/0.040 = 0.50\), so \(\omega t = \dfrac{\pi}{6}\) (radians). [C1]
\[t = \frac{\pi/6}{15.71} = 0.0333\,\mathrm{s}\] [A1]
This is one twelfth of a period, \(T/12\). The motion is quicker near the centre: the first half of the amplitude takes \(T/12\), the second half \(T/6\), together a quarter of a cycle.
:::

:::eg A particle moves with \(x = 3.0\sin(8.0\,t)\) cm, with \(t\) in seconds. Find its frequency and period, its displacement at \(t = 0.50\,\mathrm{s}\), and the first time at which \(x = 2.0\) cm.
Compare with \(x = x_0\sin\omega t\): \(x_0 = 3.0\) cm and \(\omega = 8.0\,\mathrm{rad\,s^{-1}}\). [B1]
\[f = \frac{\omega}{2\pi} = 1.27\,\mathrm{Hz} \qquad T = \frac{2\pi}{\omega} = 0.785\,\mathrm{s}\] [A1]
At \(t = 0.50\,\mathrm{s}\), \(\omega t = 4.0\) rad (calculator in radians): \(x = 3.0\sin 4.0 = 3.0 \times (-0.757) = -2.27\) cm. [A1]
The displacement is negative: the particle is on the other side of equilibrium.
For \(x = 2.0\) cm: \(\sin 8.0t = \dfrac{2.0}{3.0}\), so \(8.0t = 0.730\) and \(t = 0.0912\,\mathrm{s}\). [A1]
:::

:::eg A mass is pulled 6.0 cm from equilibrium and released from rest. It oscillates at 1.5 Hz. Write the equation for its displacement, and find its displacement and speed 0.10 s after release.
It starts at maximum displacement, so use the cosine: \(x = x_0\cos\omega t\) with \(x_0 = 6.0\) cm and \(\omega = 2\pi \times 1.5 = 9.42\,\mathrm{rad\,s^{-1}}\). [B1]
\[x = 6.0\cos(9.42\,t)\,\mathrm{cm}\]
At \(t = 0.10\,\mathrm{s}\): \(\omega t = 0.942\) rad, so \(x = 6.0\cos 0.942 = 3.53\) cm. [A1]
Speed: \(v = \omega\sqrt{x_0^2 - x^2} = 9.42\sqrt{0.060^2 - 0.0353^2} = 0.457\,\mathrm{m\,s^{-1}}\). [A1]
It is moving towards equilibrium, which is the negative direction here, so \(v = -0.457\,\mathrm{m\,s^{-1}}\).
:::

## Graphs of SHM

The three graphs below are drawn for the same oscillator as the example above (amplitude 4.0 cm, period 0.40 s, \(x = x_0\sin\omega t\)), over two periods.

:::plot Displacement against time. The amplitude is 4.0 cm and the period is 0.40 s. The gradient of this graph at any time is the velocity.
--f "4*sin(5*pi*x)+0*sqrt(0.8-x)" --x 0 0.9 --y -5.5 5.5 --xstep 0.1 --xlabel "t / s" --ylabel "x / cm" --pt "0.1,4,x₀ = 4.0 cm@n" --pt "0.3,-4,−x₀@s"
:::

:::plot Velocity against time. It is a cosine curve with maximum \(\omega x_0 = 0.63\,\mathrm{m\,s^{-1}}\). It is zero when x is at an extreme and greatest when the oscillator passes through equilibrium. The gradient is the acceleration.
--f "0.6283*cos(5*pi*x)+0*sqrt(0.8-x)" --x 0 0.9 --y -0.8 0.8 --xstep 0.1 --xlabel "t / s" --ylabel "v / m s⁻¹" --pt "0,0.628,v₀ = 0.63 m s⁻¹@ne" --pt "0.2,-0.628,−v₀@se"
:::

:::plot Acceleration against time. It is a negative sine curve with maximum \(\omega^2 x_0 = 9.87\,\mathrm{m\,s^{-2}}\): the acceleration is greatest at the extremes of the motion, where the restoring force is greatest.
--f "-9.870*sin(5*pi*x)+0*sqrt(0.8-x)" --x 0 0.9 --y -13 13 --xstep 0.1 --xlabel "t / s" --ylabel "a / m s⁻²" --pt "0.3,9.87,a₀ = 9.87 m s⁻²@n" --pt "0.1,-9.87,−a₀@s"
:::

Compare the three graphs at the same time:

- **Velocity leads displacement by \(\pi/2\) rad** (a quarter of a cycle): the \(v\) graph reaches each feature a quarter-period before the \(x\) graph. The oscillator moves fastest when it is at the centre.
- **Acceleration is in antiphase with displacement** (a phase difference of \(\pi\) rad): when \(x\) is at its positive maximum, \(a\) is at its negative maximum. That is the minus sign in \(a = -\omega^2 x\).
- **Gradients and areas.** The gradient of \(x\)–\(t\) is \(v\), and the gradient of \(v\)–\(t\) is \(a\). The area under the \(v\)–\(t\) graph is the change in displacement, and the area under the \(a\)–\(t\) graph is the change in velocity. These are the same links as in [Kinematics](#phys.kinematics).
- When the object passes through the equilibrium position, \(x = 0\), \(a = 0\) and the speed is maximum. At the ends, \(x = \pm x_0\), \(v = 0\) and \(|a|\) is maximum.

### The acceleration–displacement graph

Plot \(a\) against \(x\) instead of against time and you get the defining equation itself: a straight line through the origin with a **negative gradient**.

:::plot Acceleration against displacement for the same oscillator is a straight line through the origin. The gradient is \(-\omega^2\). (Here the gradient is shown per centimetre.)
--f "-2.4674*x" --x -5 5 --y -13 13 --xlabel "x / cm" --ylabel "a / m s⁻²" --pt "4,-9.87,(4.0, −9.87)@sw" --pt "-4,9.87,(−4.0, 9.87)@ne"
:::

:::eg Use the graph above to find the angular frequency and the period of the oscillator.
The graph is a straight line through the origin, so \(a\) is proportional to \(-x\): the motion is SHM. [B1]
Take the point (4.0 cm, \(-9.87\,\mathrm{m\,s^{-2}}\)) and convert 4.0 cm to \(0.040\,\mathrm{m}\):
\[\text{gradient} = \frac{-9.87}{0.040} = -247\,\mathrm{s^{-2}}\] [C1]
The gradient is \(-\omega^2\), so \(\omega = \sqrt{247} = 15.7\,\mathrm{rad\,s^{-1}}\). [A1]
\[T = \frac{2\pi}{\omega} = 0.400\,\mathrm{s}\] [A1]
:::

### The velocity–displacement graph

Plotting \(v\) against \(x\) gives a closed loop. Because \(\omega^2 x^2 + v^2 = \omega^2 x_0^2\) (the equation in the proof above), the loop is an **ellipse**, with semi-axes \(x_0\) along the \(x\)-axis and \(\omega x_0\) along the \(v\)-axis.

:::html
<figure class="fig small"><svg viewBox="140 20 365 260" role="img" aria-label="Velocity against displacement for SHM: an ellipse centred on the origin, crossing the x axis at plus and minus x0 and the v axis at plus and minus omega x0, travelled clockwise."><path class="ax" d="M165 150H445M300 36V268"/><path class="c1" d="M180 150A120 100 0 0 1 420 150A120 100 0 0 1 180 150"/><path class="c1" d="M290 50H310" marker-end="url(#ah-phys)"/><path class="c1" d="M310 250H290" marker-end="url(#ah-phys)"/><text class="tl" x="450" y="155">x / cm</text><text class="tl" x="308" y="32">v / m s⁻¹</text><text class="tl" x="426" y="170">x₀</text><text class="tl te" x="174" y="170">−x₀</text><text class="tl te" x="294" y="44">ωx₀</text><text class="tl te" x="294" y="266">−ωx₀</text></svg><figcaption>The ellipse is travelled clockwise. At the right-hand end the oscillator is momentarily at rest; at the top it passes through the centre at its greatest speed.</figcaption></figure>
:::

## Energy in SHM

Energy is conserved in an undamped oscillator. At the ends of the motion the object is momentarily at rest, so its energy is all potential (stored in the stretched spring, or in the raised bob). At the centre, the speed is greatest and the energy is all kinetic. In between it is shared.

:::key Energy in SHM
\[E_K = \tfrac12 m v^2 = \tfrac12 m\omega^2\left(x_0^2 - x^2\right) \qquad E_P = \tfrac12 m\omega^2 x^2 \qquad E = E_K + E_P = \tfrac12 m\omega^2 x_0^2\]
\(E\): total energy (J) · it depends on the mass, on the square of the amplitude and on the square of the frequency. For a mass on a spring \(k = m\omega^2\), so \(E_P = \tfrac12 kx^2\) and \(E = \tfrac12 kx_0^2\), as in [Deformation of solids](#phys.solids). Also \(E = \tfrac12 m v_0^2\).
:::

The kinetic energy comes straight from \(v = \pm\omega\sqrt{x_0^2 - x^2}\). The total is the kinetic energy at \(x = 0\): \(\tfrac12 m(\omega x_0)^2\). The potential energy is whatever is left over, \(E - E_K\).

:::plot Energy against displacement for a 0.20 kg mass with \(\omega = 10\,\mathrm{rad\,s^{-1}}\) and amplitude 5.0 cm. The potential energy is a parabola with its minimum at the centre, the kinetic energy is an upside-down parabola, and they add to a constant.
--f "x**2+0*sqrt(25-x**2)" --f "25-x**2+0*sqrt(25-x**2)" --x -6 6 --y 0 38 --xlabel "x / cm" --ylabel "energy / mJ" --label "potential" --label "kinetic" --hline 25 --pt "3.4,25,total E = 25 mJ@n" --legend tr
:::

The curves meet at \(x = \pm x_0/\sqrt2\), where kinetic and potential energies are equal.

Against **time**, both energies still add to a constant, but each oscillates at **twice** the frequency of the motion. The energies are proportional to \(\sin^2\omega t\) and \(\cos^2\omega t\), and these repeat every half period. The object passes through the centre twice per cycle (once each way) and reaches an end twice, so the kinetic energy peaks twice per cycle.

:::plot Energy against time over two periods. The kinetic and potential energies each have a period of half the period of the motion, and their sum stays at 25 mJ.
--f "25*sin(2*pi*x)**2+0*sqrt(2-x)" --f "25*cos(2*pi*x)**2+0*sqrt(2-x)" --x 0 2.3 --y 0 38 --xstep 0.25 --xlabel "t / T" --ylabel "energy / mJ" --label "potential" --label "kinetic" --hline 25 --pt "0.375,25,E = 25 mJ@n" --legend tr
:::

:::eg A 0.20 kg mass oscillates with \(\omega = 10\,\mathrm{rad\,s^{-1}}\) and amplitude 0.050 m. Find the total energy, and the kinetic energy, potential energy and speed when the displacement is 0.030 m.
\[E = \tfrac12 m\omega^2 x_0^2 = \tfrac12 \times 0.20 \times 10^2 \times 0.050^2 = 0.025\,\mathrm{J}\] [C1]
\[E_K = \tfrac12 m\omega^2(x_0^2 - x^2) = \tfrac12 \times 0.20 \times 10^2 \times (0.050^2 - 0.030^2) = 0.016\,\mathrm{J}\] [A1]
\[E_P = E - E_K = 0.025 - 0.016 = 0.009\,\mathrm{J}\] [A1]
Check: \(\tfrac12 m\omega^2 x^2 = 10 \times 0.030^2 = 0.009\,\mathrm{J}\). The speed comes from \(E_K = \tfrac12 mv^2\): \(v = \sqrt{2 \times 0.016/0.20} = 0.40\,\mathrm{m\,s^{-1}}\), which agrees with \(\omega\sqrt{x_0^2 - x^2} = 10 \times 0.040\).
:::

:::eg At what displacement are the kinetic and potential energies of an oscillator equal?
\(E_K = E_P\), so each is half the total: \(\tfrac12 m\omega^2 x^2 = \tfrac12\left(\tfrac12 m\omega^2 x_0^2\right)\).
Cancel \(\tfrac12 m\omega^2\): \(x^2 = \dfrac{x_0^2}{2}\), so \(x = \pm\dfrac{x_0}{\sqrt2} = \pm 0.71\,x_0\).
For the amplitude 5.0 cm above this is \(\pm 3.5\) cm. At that point the speed is \(\omega x_0/\sqrt2\), also 71% of the maximum.
:::

Try the simulation below. Change the amplitude, frequency and mass, and watch the three graphs and the energy bars. The bars are in joules: the total stays constant until you add damping.

:::html
<div class="widget" data-w="phys-shm" data-mode="shm" data-x0="0.05" data-f="0.5"></div>
:::

:::lab Finding the force constant of a spring from its oscillations
:::steps
1. Hang a spring from a clamp and hang a mass \(m\) on it. Place a small marker (a fiducial pin) at the equilibrium position of the bottom of the mass, with the timer ready beside it.
2. Pull the mass down about 2 cm and release it. Start the stopwatch as the mass passes the marker, moving in a stated direction, and count \(n = 20\) complete oscillations. The time for 20 oscillations is about ten times larger than a reaction-time error, so the percentage uncertainty in \(T\) is small.
3. Calculate \(T = t/n\). Repeat the timing and take the mean. Keep the amplitude small and constant, so that the spring stays within its limit of proportionality.
4. Repeat for at least six masses from 0.10 kg to 0.60 kg.
5. Plot \(T^2\) (\(y\)-axis) against \(m\) (\(x\)-axis). From \(T^2 = \dfrac{4\pi^2}{k}\,m\), the graph is a straight line with gradient \(\dfrac{4\pi^2}{k}\), so \(k = \dfrac{4\pi^2}{\text{gradient}}\).
:::
The line does not pass exactly through the origin, because the spring itself has mass and also oscillates. This does not change the gradient, and so does not change \(k\).
:::

:::eg In the experiment above the gradient of the \(T^2\)–\(m\) graph is \(1.58\,\mathrm{s^2\,kg^{-1}}\). Find the force constant of the spring.
\[T^2 = \frac{4\pi^2}{k}\,m \quad\Rightarrow\quad k = \frac{4\pi^2}{\text{gradient}} = \frac{39.48}{1.58} = 25.0\,\mathrm{N\,m^{-1}}\] [C1] [A1]
:::

## Damping

A real oscillator loses energy. A pendulum slows because of air resistance and friction at the pivot, a bouncing car is slowed by its shock absorbers, and a plucked string fades as it pushes the air.

:::def Damping
The loss of energy from an oscillating system, caused by resistive forces, so that the amplitude of the oscillations decreases.
:::

A resistive force, such as drag or friction, always opposes the motion and so does negative work on the oscillator in every cycle. The energy goes to thermal energy in the surroundings. Because the energy is proportional to the square of the amplitude (\(E = \tfrac12 m\omega^2 x_0^2\)), a falling energy means a falling amplitude.

With **light damping** the amplitude falls steadily over many cycles. Each swing is a constant fraction of the one before, so the amplitude falls **exponentially**, and the period is almost unchanged. With more damping the system loses its energy so fast that it cannot complete a swing.

:::def Light damping
Damping in which the system still oscillates, with the amplitude decreasing gradually and (almost) exponentially, and the period almost unchanged.
:::

:::def Critical damping
Damping in which the system returns to its equilibrium position in the shortest possible time without oscillating.
:::

:::def Heavy damping
Damping so large that the system does not oscillate and returns to its equilibrium position more slowly than with critical damping.
:::

:::html
<figure class="fig"><svg viewBox="20 10 580 306" role="img" aria-label="Displacement against time for an oscillator released from rest at displacement x0. Light damping: oscillations whose amplitude shrinks within dashed exponential envelope lines. Critical damping: the displacement falls smoothly to zero in about one second without crossing the axis. Heavy damping: the displacement falls to zero more slowly, also without crossing the axis."><path class="ax" d="M70 30V270M70 150H580M70 270H580"/><path class="gr dash" d="M70 40L95 48.5L120 56.3L145 63.5L170 70.1L195 76.3L220 81.9L245 87.2L270 92L295 96.5L320 100.6L345 104.4L370 107.9L395 111.1L420 114.1L445 116.9L470 119.4L495 121.8L520 123.9L545 125.9L570 127.8"/><path class="gr dash" d="M70 260L95 251.5L120 243.7L145 236.5L170 229.9L195 223.7L220 218.1L245 212.8L270 208L295 203.5L320 199.4L345 195.6L370 192.1L395 188.9L420 185.9L445 183.1L470 180.6L495 178.2L520 176.1L545 174.1L570 172.2"/><path class="c1 sw2" d="M70 40L76.2 41.3L82.5 45.2L88.8 51.5L95 59.9L101.2 70.2L107.5 82L113.8 94.9L120 108.7L126.2 123L132.5 137.3L138.8 151.4L145 164.9L151.2 177.5L157.5 188.9L163.8 199L170 207.5L176.2 214.2L182.5 219.2L188.8 222.2L195 223.5L201.2 222.9L207.5 220.5L213.8 216.6L220 211.2L226.2 204.5L232.5 196.8L238.8 188.3L245 179.1L251.3 169.6L257.5 160.1L263.8 150.6L270 141.5L276.2 133L282.5 125.2L288.8 118.3L295 112.5L301.2 107.8L307.5 104.2L313.8 102L320 101L326.3 101.2L332.5 102.5L338.8 105L345 108.5L351.2 112.8L357.5 117.8L363.8 123.5L370 129.5L376.2 135.8L382.5 142.2L388.8 148.6L395 154.7L401.3 160.5L407.5 165.8L413.8 170.5L420 174.5L426.2 177.8L432.5 180.2L438.8 181.9L445 182.7L451.3 182.7L457.5 181.9L463.8 180.4L470 178.2L476.2 175.4L482.5 172.1L488.8 168.4L495 164.4L501.2 160.2L507.5 155.9L513.8 151.6L520 147.5L526.2 143.6L532.5 140L538.8 136.8L545 134L551.2 131.8L557.5 130L563.8 128.8L570 128.2"/><path class="c2 sw2" d="M70 40L82.5 44.4L95 54.4L107.5 66.7L120 79.4L132.5 91.2L145 101.8L157.5 111L170 118.7L182.5 125.1L195 130.3L207.5 134.5L220 137.9L232.5 140.6L245 142.7L257.5 144.4L270 145.7L282.5 146.7L295 147.4L307.5 148L320 148.5L332.5 148.9L345 149.1L357.5 149.3L370 149.5L382.5 149.6L395 149.7L407.5 149.8L420 149.8L432.5 149.9L445 149.9L457.5 149.9L470 149.9L482.5 150L495 150L507.5 150L520 150L532.5 150L545 150L557.5 150L570 150"/><path class="c2 sw2 dash" d="M70 40L82.5 43.7L95 50.7L107.5 58.2L120 65.4L132.5 72.2L145 78.5L157.5 84.3L170 89.6L182.5 94.4L195 98.9L207.5 103.1L220 106.8L232.5 110.3L245 113.5L257.5 116.5L270 119.2L282.5 121.7L295 124L307.5 126.1L320 128L332.5 129.8L345 131.4L357.5 132.9L370 134.3L382.5 135.6L395 136.7L407.5 137.8L420 138.8L432.5 139.7L445 140.5L457.5 141.3L470 142L482.5 142.6L495 143.2L507.5 143.8L520 144.3L532.5 144.7L545 145.2L557.5 145.6L570 145.9"/><path class="ax" d="M195 270V276M320 270V276M445 270V276M570 270V276"/><text class="ts tc" x="70" y="290">0</text><text class="ts tc" x="195" y="290">0.5</text><text class="ts tc" x="320" y="290">1.0</text><text class="ts tc" x="445" y="290">1.5</text><text class="ts tc" x="570" y="290">2.0</text><text class="tl tc" x="320" y="308">t / s</text><text class="tl" x="78" y="26">x / x₀</text><text class="tl te" x="62" y="44">x₀</text><text class="tl te" x="62" y="264">−x₀</text><path class="c1 sw2" d="M392 50H424"/><path class="c2 sw2" d="M392 72H424"/><path class="c2 sw2 dash" d="M392 94H424"/><text class="tl" x="432" y="54">light damping</text><text class="tl" x="432" y="76">critical damping</text><text class="tl" x="432" y="98">heavy damping</text></svg><figcaption>Each oscillator is released from rest at the displacement x₀. The dashed envelope curves show the exponential fall of the amplitude with light damping. With critical damping the oscillator reaches equilibrium in the shortest time; with heavy damping it takes longer. Neither of these two crosses the equilibrium line.</figcaption></figure>
:::

Damping is wanted or unwanted depending on the job.

| Situation | Damping used | Why |
|---|---|---|
| Car suspension (shock absorbers) | Close to critical | The body returns to level quickly after a bump and does not bounce |
| Door closer | Critical or slightly heavy | The door closes without swinging past the frame or crawling |
| Pointer of a measuring instrument | Close to critical | The pointer settles on the reading quickly without overshoot |
| A swing, a pendulum clock, a guitar string | Light | They should keep oscillating for a long time |

:::eg A lightly damped pendulum has an amplitude of 5.0 cm. One cycle later its amplitude is 4.5 cm. Find the fraction of its energy lost in one cycle, and its amplitude after 10 cycles.
Energy is proportional to amplitude squared, so the energy after one cycle is \(\left(\dfrac{4.5}{5.0}\right)^2 = 0.81\) of the original. [C1]
The fraction lost is \(1 - 0.81 = 0.19\), that is 19%. [A1]
The amplitude falls by the same factor 0.90 every cycle (an exponential decay), so after 10 cycles: \(5.0 \times 0.90^{10} = 1.7\,\mathrm{cm}\). [A1]
By then the energy is \(0.81^{10} = 0.12\) of the original: about an eighth.
:::

## Forced oscillations and resonance

So far the oscillator has been left alone. Now push it. A child on a swing, a loudspeaker cone driven by an amplifier, a building shaken by an earthquake: in each case an external **driver** applies a periodic force, and the system performs a **forced oscillation**. After a short time it settles down and oscillates at the frequency of the driver, **not** at its own.

:::def Natural frequency
The frequency at which a system oscillates when it is displaced and then left to oscillate freely, without damping or driving.
:::

How large is the forced oscillation? Slowly driven, the system just follows the driver. Driven very fast, it hardly moves. But when the driving frequency is close to the natural frequency, each push arrives at just the right moment to add to the motion, and the system takes energy from the driver in step with its own oscillation. The amplitude grows until the energy supplied in each cycle equals the energy lost to damping.

:::def Resonance
The large increase in amplitude of a forced oscillation that occurs when the driving frequency is equal to the natural frequency of the system. The amplitude is then a maximum.
:::

:::plot Amplitude of a forced oscillator against driving frequency, in units of the natural frequency \(f_0\). With light damping the peak is tall and narrow; with heavier damping it is lower and broader, and slightly to the left of \(f_0\).
--f "1/sqrt((1-x**2)**2+(0.2*x)**2)+0*sqrt(2.2-x)" --f "1/sqrt((1-x**2)**2+(0.6*x)**2)+0*sqrt(2.2-x)" --x 0 2.5 --y 0 6.5 --xstep 0.5 --xlabel "f / f₀" --ylabel "A / A₀" --label "light damping" --label "heavier damping" --legend tr --vline 1 --pt "0.99,5,peak at about f₀@nw"
:::

Here \(A_0\) is the amplitude at a very low driving frequency (the displacement the force alone would produce). The shape of the curve is the one to remember.

- The peak is at (or just below) the natural frequency.
- More damping makes the peak **lower** and **broader**, and moves it slightly to a **lower** frequency.
- At very low frequency the amplitude is constant, and at high frequency it falls towards zero.

Resonance is useful when you want a large response, and harmful when you do not.

| Resonance wanted | Resonance unwanted |
|---|---|
| Pushing a child on a swing once per swing, at its natural frequency | A footbridge whose natural frequency is close to the frequency of walkers' footsteps |
| An air column in a pipe or a string driven at its natural frequency, so the instrument sounds loudly | A part of an engine or a car panel that rattles at particular engine speeds |
| A radio tuning circuit set to the natural frequency of the station's signal | A building shaken by an earthquake at a frequency near its own |

Unwanted resonance is reduced by adding damping (shock absorbers, rubber mounts, or a large mass on springs that absorbs energy at the top of a tall building), or by changing the natural frequency (stiffening or adding mass) so that it no longer matches the driver.

:::eg A car of mass 1000 kg has a suspension that behaves like a single spring of force constant \(4.0 \times 10^{4}\,\mathrm{N\,m^{-1}}\). It drives along a washboard track with ridges 4.0 m apart. At what speed does the car resonate?
The natural frequency is \(f_0 = \dfrac{1}{2\pi}\sqrt{\dfrac{k}{m}} = \dfrac{1}{2\pi}\sqrt{\dfrac{4.0\times10^4}{1000}} = 1.01\,\mathrm{Hz}\). [C1]
The car meets a ridge every time it moves 4.0 m. At speed \(v\) it meets \(v/4.0\) ridges per second, which is the driving frequency. [C1]
Resonance needs \(v/4.0 = 1.01\), so \(v = 4.0\,\mathrm{m\,s^{-1}}\) (about \(14\,\mathrm{km\,h^{-1}}\)). [A1]
At a much higher speed the driving frequency is far above \(f_0\) and the car body hardly moves, which is why a driver feels the shaking ease off if they speed up.
:::

Now try the resonance simulation. Sweep the driving frequency through the natural frequency and watch the dot ride the amplitude curve. Then increase the damping and compare the three faint reference curves.

:::html
<div class="widget" data-w="phys-shm" data-mode="resonance"></div>
:::

:::lab Investigating resonance
:::steps
1. Attach a mass to the bottom of a spring and hang the spring from a rod driven vertically by a vibration generator connected to a signal generator. Set the amplitude of the signal generator to a small, fixed value.
2. Start at a driving frequency well below the natural frequency. When the oscillation is steady, measure the amplitude of the mass against a fixed ruler, or from the vertical range of a marker.
3. Increase the frequency in small steps (for example 0.1 Hz), waiting for the oscillation to become steady each time, and measure the amplitude. Take smaller steps near the peak, where the amplitude changes quickly.
4. Plot the amplitude against the driving frequency. The peak should be at the natural frequency, which you can check by timing the free oscillations of the same mass.
5. Repeat with a card attached to the mass, so that air resistance is bigger. The peak should be lower and broader.
:::
:::

:::board
AQA's formula booklet lists \(T = 2\pi\sqrt{m/k}\) for a mass on a spring and \(T = 2\pi\sqrt{l/g}\) for a simple pendulum, and writes the displacement as \(x = A\cos\omega t\), with \(A\) for the amplitude. Cambridge's data sheet has neither period formula: a question gives them when it needs them, or asks you to show that \(a = -\omega^2 x\) as above.
:::

:::eg Spot the error: a mass oscillates with \(x = 5.0\sin\omega t\) (in cm) at a frequency of 2.0 Hz. A student calculates its displacement at \(t = 0.30\) s.
A student wrote this answer.

Line 1: \(\omega = 2\pi f = 2\pi \times 2.0 = 12.57\,\mathrm{rad\,s^{-1}}\)
Line 2: \(\omega t = 12.57 \times 0.30 = 3.770\)
Line 3: \(x = 5.0\sin(3.770) = 5.0 \times 0.0657 = 0.33\) cm

Lines 1 and 2 are correct. [C1] **Line 3 is wrong: the calculator was in degree mode, so it found \(\sin 3.77^\circ\) instead of \(\sin 3.77\,\mathrm{rad}\). The answer mark is lost.** [A0]

Correct working: \(x = 5.0\sin(3.770) = 5.0 \times (-0.5878) = -2.94\) cm. [A1]

Check: \(\omega t = 3.77\) rad is a little more than \(\pi\) rad, so the oscillator has passed through equilibrium and is on the negative side, with a displacement that is negative. A positive 0.33 cm is not possible.
:::

:::eg Spot the error: a 0.20 kg mass has \(\omega = 10\,\mathrm{rad\,s^{-1}}\) and amplitude 0.050 m. Find its kinetic energy at a displacement of 0.030 m.
A student wrote this answer.

Line 1: \(v = \omega x = 10 \times 0.030 = 0.30\,\mathrm{m\,s^{-1}}\)
Line 2: \(E_K = \tfrac12 mv^2 = \tfrac12 \times 0.20 \times 0.30^2 = 0.0090\,\mathrm{J}\)

**Line 1 is wrong: \(v = \omega x\) is not an SHM equation. The speed at displacement \(x\) is \(\omega\sqrt{x_0^2 - x^2}\). Method mark lost, and so the answer mark.** [M0] [A0]

Correct working: \(v = 10\sqrt{0.050^2 - 0.030^2} = 0.40\,\mathrm{m\,s^{-1}}\), so \(E_K = \tfrac12 \times 0.20 \times 0.40^2 = 0.016\,\mathrm{J}\). [A1]

The student's 0.0090 J is actually the *potential* energy at that displacement. Checking that the kinetic and potential energies add to the total of 0.025 J would have exposed the error: \(0.0090 + 0.0090 \neq 0.025\,\mathrm{J}\).
:::

:::exam Sketching SHM graphs
When asked to sketch a graph, say or show: where the curve starts (at the centre or at an extreme), its shape (sine or cosine), its amplitude with a value on the axis, and its period marked on the time axis. A sketch with no numbers on either axis rarely earns the final mark. For damping graphs, show the curve starting at the same displacement each time, light damping crossing the time axis with decreasing peaks, and critical and heavy damping never crossing it.
:::

:::try Start easy, finish at exam standard
Q: An oscillator has a frequency of 5.0 Hz. Find its period and its angular frequency.
A: \(T = 1/f = 1/5.0 = 0.20\,\mathrm{s}\) and \(\omega = 2\pi f = 2\pi \times 5.0 = 31.4\,\mathrm{rad\,s^{-1}}\).
Q: Which of these motions is SHM, and why? (a) \(a = -25x\) (b) \(a = -4x^2\) (c) \(a = +9x\)
A: (a) is SHM: the acceleration is proportional to \(x\) and opposite to it, with \(\omega^2 = 25\), \(\omega = 5.0\,\mathrm{rad\,s^{-1}}\). (b) is not: \(a\) is proportional to \(x^2\), not \(x\). (c) is not: it points the same way as \(x\), so the object would accelerate away from the origin.
Q: A 0.80 kg mass hangs on a spring of force constant \(200\,\mathrm{N\,m^{-1}}\). Find the period of its oscillations.
A: \(\omega = \sqrt{k/m} = \sqrt{200/0.80} = 15.8\,\mathrm{rad\,s^{-1}}\), so \(T = 2\pi/\omega = 0.397\,\mathrm{s}\).
Q: An oscillator moves with \(x = 2.0\sin(5.0\,t)\) cm. Find its maximum speed and maximum acceleration.
A: \(\omega = 5.0\,\mathrm{rad\,s^{-1}}\) and \(x_0 = 0.020\,\mathrm{m}\). \(v_{\max} = \omega x_0 = 0.10\,\mathrm{m\,s^{-1}}\) and \(a_{\max} = \omega^2 x_0 = 25 \times 0.020 = 0.50\,\mathrm{m\,s^{-2}}\).
Q: An oscillator has amplitude 0.12 m and \(\omega = 3.0\,\mathrm{rad\,s^{-1}}\). Find its speed when the displacement is 0.060 m.
A: \(v = \omega\sqrt{x_0^2 - x^2} = 3.0\sqrt{0.12^2 - 0.060^2} = 0.31\,\mathrm{m\,s^{-1}}\).
Q: A 0.50 kg mass oscillates with \(\omega = 4.0\,\mathrm{rad\,s^{-1}}\) and amplitude 0.10 m. Find its total energy.
A: \(E = \tfrac12 m\omega^2 x_0^2 = \tfrac12 \times 0.50 \times 4.0^2 \times 0.10^2 = 0.040\,\mathrm{J}\).
Q: Two oscillators of frequency 2.0 Hz are such that one passes through its equilibrium position 0.125 s after the other. What is the phase difference?
A: \(T = 1/2.0 = 0.50\,\mathrm{s}\), so \(\Delta\phi = 2\pi \times 0.125/0.50 = \pi/2\,\mathrm{rad}\) (90°).
Q: A door closer is designed so that the door shuts in the shortest time without banging or swinging back. What type of damping is that?
A: Critical damping: the door returns to its closed (equilibrium) position in the shortest possible time without oscillating.
Q: A swing has a natural frequency of 0.40 Hz. A parent pushes it at 0.20 Hz, then 0.40 Hz, then 0.80 Hz. Which gives the biggest swing, and why?
A: 0.40 Hz. The driving frequency then equals the natural frequency, so the swing is in resonance and its amplitude is a maximum.
Q: A pendulum is lengthened to four times its length. What happens to its period?
A: \(T \propto \sqrt{l}\), so the period doubles.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define simple harmonic motion.
A: The acceleration is proportional to the displacement from a fixed point [B1] and is directed towards that point (opposite to the displacement). [B1]
Q: [4 marks] ★★ The acceleration \(a\) of a trolley on springs is plotted against its displacement \(x\). The graph is a straight line through the origin that passes through the point (\(-0.040\,\mathrm{m}\), \(+2.4\,\mathrm{m\,s^{-2}}\)). (a) Show that the motion is SHM, and find the angular frequency. (b) Find the period. (c) The amplitude is 0.060 m. Find the maximum speed.
H: The gradient of the line is \(-\omega^2\).
A: (a) The graph is a straight line through the origin with a negative gradient, so \(a\) is proportional to \(-x\): SHM. Gradient \(= 2.4/(-0.040) = -60\,\mathrm{s^{-2}}\) [C1] so \(\omega = \sqrt{60} = 7.7\,\mathrm{rad\,s^{-1}}\). [A1] (b) \(T = 2\pi/7.746 = 0.81\,\mathrm{s}\). [A1] (c) \(v_{\max} = \omega x_0 = 7.746 \times 0.060 = 0.46\,\mathrm{m\,s^{-1}}\). [A1]
Q: [3 marks] ★★ An oscillator has amplitude 6.0 cm and frequency 2.5 Hz. Calculate its speed when its displacement is 4.0 cm from equilibrium.
A: \(\omega = 2\pi f = 2\pi \times 2.5 = 15.7\,\mathrm{rad\,s^{-1}}\) [C1] \(v = \omega\sqrt{x_0^2 - x^2} = 15.7\sqrt{0.060^2 - 0.040^2}\) [C1] \(= 0.70\,\mathrm{m\,s^{-1}}\). [A1]
Q: [3 marks] ★★ The displacement of an oscillator is \(x = 3.0\sin(2\pi t/0.40)\) cm, with \(t\) in seconds. Sketch the graph of its velocity against time for the first 0.80 s, giving values on the axes.
H: Velocity is the gradient of the displacement graph. When the gradient of \(x\) is greatest, the speed is greatest.
A: A cosine curve, starting at its maximum positive value at \(t = 0\) (the oscillator passes through equilibrium at \(t = 0\) moving in the positive direction). [B1] Period 0.40 s: two complete cycles in 0.80 s, with the curve crossing zero at 0.10 s, 0.30 s, and so on. [B1] Amplitude \(\omega x_0 = 15.7 \times 0.030 = 0.47\,\mathrm{m\,s^{-1}}\) marked on the axis. [B1]
Q: [3 marks] ★★ A 0.40 kg mass on a spring of force constant \(25\,\mathrm{N\,m^{-1}}\) oscillates with amplitude 0.080 m. Calculate the total energy of the oscillation and the kinetic energy of the mass when its displacement is 0.050 m.
A: \(\omega^2 = k/m = 25/0.40 = 62.5\,\mathrm{s^{-2}}\) [C1] \(E = \tfrac12 m\omega^2 x_0^2 = \tfrac12 \times 0.40 \times 62.5 \times 0.080^2 = 0.080\,\mathrm{J}\). [A1] \(E_K = \tfrac12 m\omega^2(x_0^2 - x^2) = 12.5 \times (0.080^2 - 0.050^2) = 0.049\,\mathrm{J}\). [A1]
Q: [5 marks] ★★ (a) State what is meant by critical damping. (b) On one pair of axes, sketch displacement–time graphs for an oscillator that is released from rest at displacement \(x_0\) and is (i) lightly damped, (ii) critically damped, (iii) heavily damped. Label each curve.
A: (a) The system returns to its equilibrium position [B1] in the shortest possible time, without oscillating. [B1] (b) (i) Oscillations about zero with steadily decreasing amplitude and (almost) constant period. [B1] (ii) A smooth fall to zero without crossing the axis, in the shortest time. [B1] (iii) A smooth fall to zero without crossing the axis, but more slowly than (ii). [B1]
Q: [3 marks] ★★ The graph of amplitude against driving frequency for a forced oscillator has a peak near the natural frequency. The damping is now increased. Describe the changes to the graph.
A: The height of the peak is smaller. [B1] The peak is broader (the curve is flatter). [B1] The peak moves slightly to a lower frequency. [B1]
Q: [6 marks] ★★★ A test tube containing lead shot floats upright in water. The total mass of the tube is 0.045 kg and its cross-sectional area is \(3.1 \times 10^{-4}\,\mathrm{m^2}\). The tube is pushed down a small distance and released. The density of water is \(1000\,\mathrm{kg\,m^{-3}}\). (a) Explain why the upthrust increases by \(\rho g A x\) when the tube is pushed down a further distance \(x\). (b) Show that the tube then moves with SHM. (c) Calculate its period.
H: The upthrust equals the weight of water displaced. The extra volume displaced is \(Ax\). (See [Forces, density and pressure](#phys.forces).)
H: At equilibrium the upthrust equals the weight, so the net force on the displaced tube is the change in upthrust.
A: (a) The extra volume of water displaced is \(Ax\), [B1] so the extra upthrust is the weight of that water: \(\rho g A x\). [B1] (b) At equilibrium the upthrust equals the weight, so the net force is the extra upthrust, which acts upwards when the tube is pushed down: \(F = -\rho g A x\). [B1] So \(a = -\dfrac{\rho g A}{m}\,x\): proportional to \(x\) and opposite to it, which is SHM, with \(\omega^2 = \dfrac{\rho g A}{m}\). [B1] (c) \(\omega^2 = \dfrac{1000 \times 9.81 \times 3.1\times10^{-4}}{0.045} = 67.6\,\mathrm{s^{-2}}\) [C1] \(T = \dfrac{2\pi}{\omega} = 0.76\,\mathrm{s}\). [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ (a) For a pendulum of length \(l\), explain why the motion is only simple harmonic for small angles. (b) A pendulum is released from rest at an angle of 20° (0.349 rad). By what percentage is the restoring force at that angle smaller than the value \(mg\theta\) predicted by the SHM model? (c) Does the period at 20° come out larger or smaller than the small-angle value?
H: The exact restoring force is \(mg\sin\theta\).
H: For (c), a smaller force means a smaller acceleration at each point.
A: (a) The restoring force along the arc is \(mg\sin\theta\), [B1] which is proportional to the displacement \(x = l\theta\) only if \(\sin\theta \approx \theta\), that is for small angles in radians. [B1] (b) \(\sin 20^\circ = 0.3420\) and \(\theta = 0.3491\), so \(\sin\theta/\theta = 0.980\). [C1] The force is 2.0% smaller than \(mg\theta\). [A1] (c) The acceleration is smaller than the SHM value at every angle, so the pendulum moves more slowly and the period is larger than \(2\pi\sqrt{l/g}\). [B1] (A fuller calculation gives \(T \approx T_0(1 + \theta_0^2/16)\), about 0.8% longer at 20°.)
Q: [5 marks] ★★★ Two identical springs, each of force constant \(40\,\mathrm{N\,m^{-1}}\), support a 0.50 kg mass. Find the period of oscillation when (a) the springs are connected side by side (in parallel), both attached to the mass; (b) one spring is attached to the other, end to end (in series), with the mass on the lower one.
H: In parallel the springs share the displacement and their forces add. In series they share the force and their extensions add.
A: (a) When the mass moves \(x\), each spring exerts \(kx\), so the force is \(2kx\) and the effective force constant is \(80\,\mathrm{N\,m^{-1}}\). [B1] \(T = 2\pi\sqrt{0.50/80} = 0.50\,\mathrm{s}\). [A1] (b) Each spring carries the same force \(F\), and the extensions add: \(x = F/k + F/k = 2F/k\), so the effective force constant is \(k/2 = 20\,\mathrm{N\,m^{-1}}\). [B1] \(T = 2\pi\sqrt{0.50/20}\) [C1] \(= 0.99\,\mathrm{s}\). [A1] The series period is exactly twice the parallel period, because the effective force constants differ by a factor of 4.
:::

:::quiz
? Which statement describes simple harmonic motion?
+ The acceleration is proportional to the displacement from a fixed point and directed towards it.
- The acceleration is constant and directed towards a fixed point.
- The velocity is proportional to the displacement from a fixed point.
- The acceleration is proportional to the speed and opposite to the velocity.
> SHM needs \(a \propto -x\). A constant acceleration is a projectile or a falling object, and an acceleration proportional to velocity describes a resistive force, not an oscillation.
? An object in SHM is at its maximum positive displacement. What are its velocity and acceleration?
+ \(v = 0\) and \(a = -\omega^2 x_0\)
- \(v = \omega x_0\) and \(a = 0\)
- \(v = 0\) and \(a = 0\)
- \(v = \omega x_0\) and \(a = -\omega^2 x_0\)
> At an extreme the object is momentarily at rest, but the restoring force and the acceleration are at their largest, pointing back towards equilibrium. The second option describes the centre.
? What is the phase difference between the displacement and the acceleration of an oscillator in SHM?
- \(\pi/2\) rad
+ \(\pi\) rad
- 0
- \(3\pi/2\) rad
> The acceleration is \(-\omega^2 x\), so it always has the opposite sign to the displacement: they are in antiphase. The velocity differs from the displacement by \(\pi/2\) rad.
? The amplitude of an oscillator is doubled and its frequency is unchanged. What happens to its maximum speed and its total energy?
+ The maximum speed doubles and the total energy quadruples.
- The maximum speed doubles and the total energy doubles.
- Both quadruple.
- The maximum speed is unchanged and the energy doubles.
> \(v_0 = \omega x_0\) is proportional to the amplitude, and \(E = \tfrac12 m\omega^2 x_0^2\) is proportional to its square.
? What is the effect of light damping on an oscillator?
+ The amplitude decreases gradually and the period is almost unchanged.
- The amplitude is unchanged and the period increases.
- The oscillator stops after one swing.
- The frequency doubles.
> Light damping removes a fraction of the energy each cycle, so the amplitude falls exponentially, but the period hardly changes. Stopping after one swing needs heavier damping.
? A mass on a spring has a period of 1.0 s. The mass is increased to four times its value on the same spring. What is the new period?
- 0.50 s
- 1.0 s
+ 2.0 s
- 4.0 s
> \(T \propto \sqrt{m}\), so four times the mass doubles the period. A pendulum's period would not depend on the mass at all.
? An oscillator is driven at a frequency equal to its natural frequency. Which statement is correct?
+ The amplitude of the oscillations is a maximum.
- The amplitude is zero, because the driver and oscillator cancel.
- The oscillator stops oscillating at its natural frequency.
- The driver stops transferring energy.
> This is resonance: the driver supplies energy in step with the motion and the amplitude is at its greatest, limited only by damping.
? A graph of potential energy against time for an oscillator of period \(T\) is plotted. What is the period of the graph?
- \(T\)
+ \(T/2\)
- \(2T\)
- \(T/4\)
> \(E_P \propto \sin^2\omega t\), which repeats every half-cycle of the motion: the object passes each side of equilibrium once per cycle, but it is at an extreme (maximum \(E_P\)) twice per cycle.
:::

:::checklist What you can now do
- [ ] I can define displacement, amplitude, period, frequency, angular frequency and phase difference, and use \(\omega = 2\pi f = 2\pi/T\) and \(\Delta\phi = 2\pi\Delta t/T\).
- [ ] I can define simple harmonic motion and show that a mass on a spring and a small-angle pendulum have \(a = -\omega^2 x\).
- [ ] I can use \(a = -\omega^2 x\) and recall and use \(x = x_0\sin\omega t\) (or the cosine, from the start condition) in radians.
- [ ] I can use \(v = v_0\cos\omega t\) and \(v = \pm\omega\sqrt{x_0^2 - x^2}\).
- [ ] I can sketch and interpret the \(x\)–\(t\), \(v\)–\(t\), \(a\)–\(t\), \(a\)–\(x\) and \(v\)–\(x\) graphs, including their phases, gradients and areas.
- [ ] I can describe how kinetic and potential energy are exchanged in SHM, and use \(E = \tfrac12 m\omega^2 x_0^2\) and the graphs of energy against displacement and time.
- [ ] I can explain damping and sketch displacement–time graphs for light, critical and heavy damping.
- [ ] I can explain resonance, sketch the amplitude–driving-frequency graph and say how damping changes it, with examples where it is useful or harmful.
:::

:::recap
- Period \(T = 1/f\); \(\omega = 2\pi f = 2\pi/T\) in \(\mathrm{rad\,s^{-1}}\); phase difference \(\Delta\phi = 2\pi\Delta t/T\).
- SHM: acceleration proportional to displacement from a fixed point and directed towards it, \(a = -\omega^2 x\). A mass on a spring has \(\omega^2 = k/m\); a small-angle pendulum has \(\omega^2 = g/l\).
- Solutions (calculator in radians): \(x = x_0\sin\omega t\), \(v = \omega x_0\cos\omega t\), \(a_{\max} = \omega^2 x_0\), and \(v = \pm\omega\sqrt{x_0^2 - x^2}\). Use a cosine for \(x\) if the timing starts at an extreme.
- \(v\) leads \(x\) by \(\pi/2\); \(a\) is in antiphase with \(x\). The \(a\)–\(x\) graph is a straight line of gradient \(-\omega^2\); the \(v\)–\(x\) graph is an ellipse.
- Energy: \(E_K = \tfrac12 m\omega^2(x_0^2 - x^2)\), \(E_P = \tfrac12 m\omega^2 x^2\), \(E = \tfrac12 m\omega^2 x_0^2\) constant. Against time \(E_K\) and \(E_P\) have half the period of the motion.
- Damping removes energy through resistive forces. Light: amplitude decays exponentially, period almost unchanged. Critical: shortest return to equilibrium without oscillating. Heavy: slower return, no oscillation.
- Resonance: a forced oscillation has its maximum amplitude when the driving frequency equals the natural frequency. More damping gives a lower, broader peak that sits slightly below the natural frequency.
:::

:::links
- explore: [Pendulum Lab](https://phet.colorado.edu/en/simulations/pendulum-lab) · PhET · change the length, mass and angle and see the period and energy
- explore: [Masses & Springs](https://phet.colorado.edu/en/simulations/masses-and-springs) · PhET · hang masses on springs and measure the period, with damping
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Electric fields](#phys.efields)
