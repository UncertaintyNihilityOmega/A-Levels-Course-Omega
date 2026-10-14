@chapter phys.circular
@title Motion in a circle
@level a2
@paper CAIE P4 (A Level)
@time 4–6 hours
@summary Angles in radians, angular speed, why an object moving in a circle at constant speed is still accelerating, and the centripetal force that causes it, with cars on bends, conical pendulums and vertical circles.

:::why
Wheels, turbines, hard disks, planets and the electrons in a mass spectrometer all move in circles, and one idea explains every one of them: a body going round a circle needs a resultant force pointing at the centre. This chapter gives you that idea as two short equations, \(F = mv^2/r\) and \(F = mr\omega^2\). The next chapter, [Gravitational fields](#phys.gravity), uses them to explain orbits, and [Magnetic fields](#phys.magnetic) uses them for charged particles.
:::

**Before you start**, you need \(F = ma\) from [Dynamics and momentum](#phys.dynamics) and the idea of radians from [Circular measure](#math.p1.circular), which this chapter re-teaches from zero.

:::try Warm-up
Q: A resultant force of 3600 N acts on a car of mass 1200 kg. What is its acceleration, and in which direction? (from [Dynamics and momentum](#phys.dynamics))
A: \(a = F/m = 3600/1200 = 3.0\,\mathrm{m\,s^{-2}}\), in the same direction as the resultant force.
Q: A car drives round a roundabout at a steady \(12\,\mathrm{m\,s^{-1}}\). Is its velocity constant? Explain. (from [Kinematics](#phys.kinematics))
A: No. Velocity is a vector, so a change in direction is a change in velocity even when the speed stays the same.
Q: A force of 50 N acts at 30° above the horizontal. Find its horizontal component. (from [Physical quantities, units and uncertainty](#phys.units))
A: \(50\cos 30^\circ = 43\,\mathrm{N}\) (to 2 significant figures).
:::

## Measuring angles in radians

You already measure angles in degrees. A degree is an arbitrary size: 360 of them make a full turn only because ancient mathematicians liked the number 360. Physics uses a more natural unit, the **radian**, because it links an angle directly to a length along the circle.

:::def Radian
The angle subtended at the centre of a circle by an arc equal in length to the radius.
:::

:::def Angular displacement
The angle through which an object has moved around a circle, measured from a reference line.
:::

:::html
<figure class="fig small"><svg viewBox="85 35 180 125" role="img" aria-label="A circle sector with centre O. Two radii of length r make an angle theta, and the arc between their ends also has length r, so the angle is one radian."><path class="ln" d="M110 130H205M110 130L161.3 50.1"/><path class="c3" d="M205 130A95 95 0 0 0 161.3 50.1"/><path class="ln-m thin" d="M136 130A26 26 0 0 0 124 108.1"/><circle class="fi" cx="110" cy="130" r="4"/><text class="tl te" x="100" y="148">O</text><text class="tl ti tc" x="147" y="114">θ</text><text class="tl ti tc" x="157" y="147">r</text><text class="tl ti tc" x="123" y="84">r</text><text class="tl" x="208" y="78">arc = r</text></svg><figcaption>When the arc has the same length as the radius, the angle at the centre is exactly one radian. A whole circle has an arc of length 2πr, so it contains 2π radians.</figcaption></figure>
:::

A complete circle has a circumference of \(2\pi r\), which is \(2\pi\) radius-lengths, so a full turn is \(2\pi\) radians. Half a turn is \(\pi\) radians, and one radian is about \(57.3^\circ\).

:::formula Radians, degrees and arc length
\[2\pi\,\mathrm{rad} = 360^\circ \qquad \theta/\mathrm{rad} = \theta/^\circ \times \frac{\pi}{180} \qquad s = r\theta\]
\(s\): arc length (m) · \(r\): radius (m) · \(\theta\): angle at the centre (**in radians**). The equation \(s = r\theta\) is the definition of the radian rewritten: an angle of \(\theta\) radians cuts off an arc of \(\theta\) radius-lengths.
:::

The radian is a ratio of two lengths, so it has no true unit. Write "rad" anyway, so the reader knows you did not mean degrees.

:::eg Convert 150° into radians and 0.75 rad into degrees.
\[150^\circ = 150 \times \frac{\pi}{180} = 2.62\,\mathrm{rad} \qquad 0.75\,\mathrm{rad} = 0.75 \times \frac{180}{\pi} = 43.0^\circ\]
Check: 150° is a little less than \(180^\circ = \pi \approx 3.14\,\mathrm{rad}\), so 2.62 rad is sensible.
:::

:::eg A bicycle wheel of radius 0.34 m rolls through 2.5 complete turns without slipping. Find the angular displacement of a point on the rim and the distance the bicycle travels.
Each turn is \(2\pi\) rad, so \(\theta = 2.5 \times 2\pi = 15.7\,\mathrm{rad}\). [C1]

A rolling wheel lays down a length of tyre equal to the arc it turns through, so the distance is \(s = r\theta = 0.34 \times 15.7\) [C1] \(= 5.3\,\mathrm{m}\). [A1]
:::

:::warn Calculator mode
Set your calculator to radians before you use \(\sin\), \(\cos\) or \(\tan\) of an angle in radians. A wrong mode gives wrong answers with no warning. In this chapter you will mostly use radians only for \(\omega\) and \(s = r\theta\), but a conical pendulum below needs an angle in degrees for its trigonometry.
:::

## Angular speed

Speed in a straight line is distance per second. Going round a circle, the natural quantity is the angle turned through per second.

:::def Angular speed
The rate of change of angular displacement: \(\omega = \dfrac{\Delta\theta}{\Delta t}\). It is measured in radians per second (\(\mathrm{rad\,s^{-1}}\)).
:::

One complete circle takes the **period** \(T\), during which the angle changes by \(2\pi\). The number of circles per second is the frequency \(f = 1/T\). So

:::formula Angular speed, period and linear speed
\[\omega = \frac{2\pi}{T} = 2\pi f \qquad\qquad v = r\omega\]
\(\omega\): angular speed (\(\mathrm{rad\,s^{-1}}\)) · \(T\): period (s) · \(f\): frequency (Hz) · \(v\): linear speed along the circle (\(\mathrm{m\,s^{-1}}\)) · \(r\): radius of the circle (m).
:::

:::proof Why v = rω
In a short time \(\Delta t\) the object turns through \(\Delta\theta\).
The distance it travels along the circle is the arc length, \(\Delta s = r\,\Delta\theta\) (from \(s = r\theta\)).
Its speed is \(v = \Delta s/\Delta t = r\,\Delta\theta/\Delta t\).
But \(\Delta\theta/\Delta t = \omega\), so \(v = r\omega\).
Every point on a turning wheel has the same \(\omega\) (it takes the same time to go round), but the points far from the axle have a larger \(r\), so they move faster.
:::

:::eg The Earth turns once in 24 hours. Find its angular speed and the speed of a point on the Equator. The radius of the Earth is \(6.37 \times 10^{6}\,\mathrm{m}\).
The period is \(T = 24 \times 3600 = 8.64 \times 10^{4}\,\mathrm{s}\).
\[\omega = \frac{2\pi}{T} = \frac{2\pi}{8.64 \times 10^{4}} = 7.27 \times 10^{-5}\,\mathrm{rad\,s^{-1}}\] [C1] [A1]
A point on the Equator moves in a circle whose radius is the radius of the Earth:
\[v = r\omega = 6.37 \times 10^{6} \times 7.27 \times 10^{-5} = 463\,\mathrm{m\,s^{-1}}\] [C1] [A1]
You are moving at about 460 m s⁻¹ with the planet, and you do not feel it, because the speed is steady. (The unrounded value of \(\omega\) is carried into the second step, and only the answer is rounded.)
:::

:::eg A hard-disk platter spins at 7200 revolutions per minute. Find its angular speed and the speed of a point 4.0 cm from the axis.
Revolutions per minute become revolutions per second: \(f = 7200/60 = 120\,\mathrm{Hz}\). [C1]

\(\omega = 2\pi f = 2\pi \times 120 = 754\,\mathrm{rad\,s^{-1}}\). [A1]

\(v = r\omega = 0.040 \times 754 = 30\,\mathrm{m\,s^{-1}}\). [A1]

A point twice as far from the axis moves twice as fast, but it still goes round once in the same time: every point of the platter has the same \(\omega\).
:::

:::warn Radians only
\(v = r\omega\) works only when \(\omega\) is in **radians** per second. Revolutions per minute or degrees per second give wrong answers. To change rpm into \(\mathrm{rad\,s^{-1}}\), multiply by \(2\pi/60\). Also check that \(r\) is the **radius**, not the diameter.
:::

## Why moving in a circle means accelerating

Imagine a car on a roundabout at a steady \(12\,\mathrm{m\,s^{-1}}\). The speedometer never moves, yet the passengers feel pushed sideways. The reason is that **acceleration is the rate of change of velocity**, and velocity is a vector: it has a direction as well as a size. The car's direction changes all the time, so its velocity changes all the time, so it is accelerating, even though its speed is constant.

:::html
<figure class="fig small"><svg viewBox="60 35 240 235" role="img" aria-label="A circle with centre O and four points on it. At each point a velocity arrow v is drawn along the tangent and an acceleration arrow a points from the point towards the centre O. The motion is anticlockwise."><path class="ln-m" d="M270 150A90 90 0 1 1 90 150A90 90 0 1 1 270 150"/><path class="c1" d="M180 60H140" marker-end="url(#ah-phys)"/><path class="c3" d="M180 60V100" marker-end="url(#ahr)"/><path class="c1" d="M270 150V110" marker-end="url(#ah-phys)"/><path class="c3" d="M270 150H230" marker-end="url(#ahr)"/><path class="c1" d="M180 240H220" marker-end="url(#ah-phys)"/><path class="c3" d="M180 240V200" marker-end="url(#ahr)"/><path class="c1" d="M90 150V190" marker-end="url(#ah-phys)"/><path class="c3" d="M90 150H130" marker-end="url(#ahr)"/><circle class="fi" cx="180" cy="60" r="4"/><circle class="fi" cx="270" cy="150" r="4"/><circle class="fi" cx="180" cy="240" r="4"/><circle class="fi" cx="90" cy="150" r="4"/><circle class="fi" cx="180" cy="150" r="3"/><text class="tl te" x="172" y="166">O</text><text class="tl ti tc" x="160" y="50">v</text><text class="tl ti" x="188" y="90">a</text><text class="tl ti" x="281" y="130">v</text><text class="tl ti tc" x="250" y="141">a</text><text class="tl ti tc" x="200" y="258">v</text><text class="tl ti" x="188" y="222">a</text><text class="tl ti te" x="80" y="174">v</text><text class="tl ti tc" x="110" y="141">a</text></svg><figcaption>Uniform circular motion, anticlockwise. The speed is constant, but the velocity v always points along the tangent, so it keeps turning. The acceleration a at every point is towards the centre.</figcaption></figure>
:::

At each instant the velocity is along the **tangent** to the circle, and the acceleration points along the radius to the **centre**. The two are at right angles, which is why the speed does not change: an acceleration perpendicular to the velocity changes only its direction.

:::def Centripetal acceleration
The acceleration of an object moving in a circle, directed towards the centre of the circle.
:::

The size of this acceleration follows from a small piece of geometry, which also shows where \(v^2/r\) comes from.

:::proof Why a = v²/r
An object moves at constant speed \(v\) round a circle of radius \(r\). In a short time \(\Delta t\) it moves from P to Q, turning through a small angle \(\Delta\theta\), so its velocity turns through the same angle \(\Delta\theta\).
Draw the two velocity vectors \(\mathbf{v}_1\) and \(\mathbf{v}_2\) from one point. They have the same length \(v\) and the angle \(\Delta\theta\) between them.
The change in velocity \(\Delta\mathbf{v} = \mathbf{v}_2 - \mathbf{v}_1\) joins their tips. For a small angle the arc is almost a straight line, so \(|\Delta\mathbf{v}| \approx v\,\Delta\theta\) (arc = radius × angle, with radius \(v\)).
The acceleration is \(|\Delta\mathbf{v}|/\Delta t = v\,\Delta\theta/\Delta t = v\omega\).
The vector \(\Delta\mathbf{v}\) points to the centre side of the circle, so the acceleration is towards the centre.
Using \(\omega = v/r\) gives \(a = v\omega = v^2/r\), and using \(v = r\omega\) gives \(a = r\omega^2\).
:::

:::html
<figure class="fig wide"><svg viewBox="15 30 425 200" role="img" aria-label="Left: part of a circle with centre O. Points P and Q are separated by a small angle delta theta at O. Velocity arrows v1 at P and v2 at Q are tangents. Right: the two velocity vectors drawn from one point, with the change in velocity delta v joining their tips and pointing downwards, towards the centre side."><path class="ln-m" d="M229.6 106.4A130 130 0 0 0 30.4 106.4"/><path class="ln-m thin dash" d="M130 190L174.5 67.8M130 190L85.5 67.8"/><path class="c1" d="M174.5 67.8L127.5 50.7" marker-end="url(#ah-phys)"/><path class="c1" d="M85.5 67.8L38.6 84.9" marker-end="url(#ah-phys)"/><path class="ln-m thin" d="M143.7 152.4A40 40 0 0 0 116.3 152.4"/><circle class="fi" cx="130" cy="190" r="3"/><circle class="fi" cx="174.5" cy="67.8" r="4"/><circle class="fi" cx="85.5" cy="67.8" r="4"/><text class="tl tc" x="130" y="208">O</text><text class="tl tc" x="130" y="132">Δθ</text><text class="tl tc" x="183" y="90">P</text><text class="tl tc" x="77" y="90">Q</text><text class="tl ti tc" x="150" y="44">v₁</text><text class="tl ti tc" x="52" y="68">v₂</text><path class="c1" d="M420 170L316.6 132.4" marker-end="url(#ah-phys)"/><path class="c1" d="M420 170L316.6 207.6" marker-end="url(#ah-phys)"/><path class="c3" d="M316.6 132.4V207.6" marker-end="url(#ahr)"/><path class="ln-m thin" d="M377.7 154.6A45 45 0 0 0 377.7 185.4"/><circle class="fi" cx="420" cy="170" r="3"/><text class="tl tc" x="350" y="174">Δθ</text><text class="tl ti tc" x="368" y="132">v₁</text><text class="tl ti tc" x="368" y="216">v₂</text><text class="tl te" x="308" y="174">Δv</text></svg><figcaption>Left: the object moves from P to Q while the angle at the centre changes by Δθ. Right: the same two velocity vectors drawn from one point. They have equal lengths, and Δv = v₂ − v₁ points towards the centre side, so the acceleration is towards the centre.</figcaption></figure>
:::

:::formula Centripetal acceleration
\[a = \frac{v^2}{r} = r\omega^2 \qquad (= v\omega)\]
\(a\): centripetal acceleration (\(\mathrm{m\,s^{-2}}\)), directed towards the centre · \(v\): speed · \(r\): radius · \(\omega\): angular speed. Which form to use depends on what you are given: \(v\) with \(r\), or \(\omega\) with \(r\).
:::

:::eg The Earth moves round the Sun in a circle of radius \(1.50 \times 10^{11}\,\mathrm{m}\) in 365.25 days. Find its centripetal acceleration.
\(T = 365.25 \times 86400 = 3.156 \times 10^{7}\,\mathrm{s}\), so \(\omega = \dfrac{2\pi}{T} = 1.99 \times 10^{-7}\,\mathrm{rad\,s^{-1}}\). [C1]

\(a = r\omega^2 = 1.50 \times 10^{11} \times \left(1.99 \times 10^{-7}\right)^2\) [C1] \(= 5.95 \times 10^{-3}\,\mathrm{m\,s^{-2}}\), towards the Sun. [A1]

This is tiny compared with \(g\), but it acts for ever, and over a year it turns the Earth's velocity through a full circle. (The next chapter shows that the Sun's gravity supplies this acceleration.)
:::

## Centripetal force

By Newton's second law, an acceleration needs a resultant force in the same direction. Multiply \(a = v^2/r\) by the mass:

:::def Centripetal force
The resultant force towards the centre of the circle needed for circular motion.
:::

:::formula Centripetal force
\[F = \frac{mv^2}{r} = mr\omega^2\]
\(F\): resultant force towards the centre (N) · \(m\): mass (kg) · \(v\): speed (\(\mathrm{m\,s^{-1}}\)) · \(r\): radius (m) · \(\omega\): angular speed (\(\mathrm{rad\,s^{-1}}\)). The force is always directed **towards the centre**.
:::

A force of constant size, always perpendicular to the velocity, therefore produces uniform circular motion. Because the force is perpendicular to the motion, it does no work on the object (work = force × distance moved in the direction of the force, and that distance is zero), so the kinetic energy and speed stay constant. Only the direction changes.

"Centripetal force" is **not** a new kind of force. It is a job description: whatever real forces act on the object, their resultant towards the centre must equal \(mv^2/r\). Name the real force that does the job.

| Situation | The real force towards the centre |
|---|---|
| Stone whirled on a string | tension in the string |
| Car on a flat bend | friction between the tyres and the road |
| Planet or satellite in orbit | gravitational attraction of the body it orbits |
| Rider on a rotor, pressed on the wall | normal contact force of the wall |
| Charged particle in a magnetic field | magnetic force on the particle |
| Bob of a conical pendulum | horizontal component of the tension |

:::plot The centripetal force on a 1200 kg car on a bend of radius 50 m rises with the square of the speed: doubling the speed needs four times the force.
--f "24*x**2" --x 0 25 --y 0 15000 --pt "15,5400,(15 m s⁻¹, 5400 N)@se" --xlabel "v / m s⁻¹" --ylabel "F / N" --label "F = mv²/r"
:::

:::eg A car of mass 1200 kg takes a flat bend of radius 50 m at \(15\,\mathrm{m\,s^{-1}}\). What friction force do the tyres need? What is the greatest speed if the road can supply at most 7200 N?
The friction force provides the centripetal force:
\[F = \frac{mv^2}{r} = \frac{1200 \times 15^2}{50}\] [C1] \(= 5400\,\mathrm{N}\) towards the centre. [A1]

At the limit, \(F_\text{max} = mv_\text{max}^2/r\), so
\[v_\text{max} = \sqrt{\frac{F_\text{max}\,r}{m}} = \sqrt{\frac{7200 \times 50}{1200}} = 17\,\mathrm{m\,s^{-1}}\] [C1] [A1]
The mass appears in both \(F_\text{max}\) and \(mv^2/r\) here only because the friction limit was given as a force. On a wet road \(F_\text{max}\) falls, and so does the safe speed.
:::

:::html
<figure class="fig small"><svg viewBox="10 78 320 170" role="img" aria-label="Rear view of a car on a flat road. Three forces act from its centre: weight W downwards, 11.8 kilonewtons; normal contact force R upwards, 11.8 kilonewtons; friction F to the left, towards the centre of the bend, 5.4 kilonewtons."><path class="ln" d="M20 214H320"/><rect class="fp s-ink sw2" x="190" y="130" width="90" height="56" rx="6"/><circle class="fp s-ink sw2" cx="205" cy="200" r="14"/><circle class="fp s-ink sw2" cx="265" cy="200" r="14"/><circle class="fi" cx="235" cy="158" r="3.5"/><path class="c1" d="M235 158V205" marker-end="url(#ah-phys)"/><path class="c1" d="M235 158V108" marker-end="url(#ah-phys)"/><path class="c2" d="M235 158H170" marker-end="url(#ah2-phys)"/><text class="tl tc" x="235" y="232">W = 11.8 kN</text><text class="tl tc" x="235" y="98">R = 11.8 kN</text><text class="tl te" x="164" y="152">F = 5.4 kN</text><text class="tl" x="22" y="200">← centre of the bend</text></svg><figcaption>The car seen from behind, with the bend curving to the left. Weight and the normal contact force cancel, so the only horizontal force is friction, and it is the centripetal force.</figcaption></figure>
:::

:::eg A 0.25 kg mass on a string moves in a horizontal circle of radius 0.80 m on a smooth table, making 1.5 revolutions every second. Find the tension in the string.
\(\omega = 2\pi f = 2\pi \times 1.5 = 9.42\,\mathrm{rad\,s^{-1}}\). [C1]

The tension is the only horizontal force, so it is the centripetal force:
\[T = mr\omega^2 = 0.25 \times 0.80 \times 9.42^2\] [C1] \(= 18\,\mathrm{N}\). [A1]

Because \(\omega\) enters squared, spinning the mass twice as fast would need four times the tension (71 N, from the unrounded 17.8 N).
:::

:::warn There is no "centrifugal force"
Passengers in a turning car feel pushed outwards, so many students draw an outward "centrifugal force". No such force acts on the car or on you. What you feel is your own **inertia**: your body wants to carry on in a straight line, and the car door pushes you inwards to make you turn. If a string whirling a ball suddenly breaks, the ball does not fly outwards along the radius. It moves off in a straight line along the **tangent**, the direction of its velocity at that instant, because no force is left to turn it.
:::

:::warn Do not draw the centripetal force as an extra arrow
On a free-body diagram, draw only real forces: weight, tension, friction, normal contact force, and so on. Then say that their **resultant** towards the centre equals \(mv^2/r\). A "centripetal force" arrow drawn in addition to the real ones counts the same force twice.
:::

:::lab Checking F = mrω² with a whirling bung
:::steps
1. Thread a nylon cord through a short glass tube. Tie a rubber bung of mass \(m\) to the top end and hang a mass \(M\) from the bottom end. The tension in the cord is then \(Mg\), and it is the centripetal force on the bung.
2. Fix a paper-clip marker on the cord just below the tube, so that the length of cord from the top of the tube to the centre of the bung is a measured \(r\) (metre rule).
3. Whirl the bung in a horizontal circle above your head, adjusting the speed so that the marker stays just below the tube. Then \(r\) stays constant.
4. Time 20 revolutions with a stopwatch, repeat and average, and divide by 20 to find the period \(T\). Timing many turns makes your reaction time small compared with the time measured.
5. Repeat for at least five values of \(r\) between about 0.3 m and 0.9 m, with the same \(m\) and \(M\).
6. From \(Mg = mr\omega^2 = mr(2\pi/T)^2\) you get \(T^2 = \dfrac{4\pi^2 m}{Mg}\,r\). Plot \(T^2\) against \(r\). A straight line through the origin confirms the relationship, and the gradient is \(4\pi^2 m/(Mg)\).
:::
The main problems are friction between the cord and the tube (so the tension at the bung is not exactly \(Mg\)) and the marker drifting up or down during a run. If the cord slopes downwards, measure \(r\) along the cord: the horizontal component of the tension and the radius of the circle both shrink by the same factor, so the result is unchanged.
:::

:::eg In the whirling-bung experiment the bung has mass 0.020 kg and the hanging mass is 0.100 kg. The gradient of the graph of \(T^2\) against \(r\) is \(0.80\,\mathrm{s^2\,m^{-1}}\). Find the tension from the gradient and compare it with the weight of the hanging mass.
The gradient is \(4\pi^2 m/F\), so \(F = \dfrac{4\pi^2 m}{\text{gradient}} = \dfrac{4\pi^2 \times 0.020}{0.80}\) [C1] \(= 0.99\,\mathrm{N}\). [A1]

The weight of the hanging mass is \(Mg = 0.100 \times 9.81 = 0.981\,\mathrm{N}\). [B1] The two agree to within about 1%, which supports \(F = mr\omega^2\). A tension a little below \(Mg\) would point to friction at the tube.
:::

## Worked problems with real forces

The method never changes: draw the real forces, choose the direction towards the centre, write "resultant force towards the centre = \(mv^2/r\) (or \(mr\omega^2\))", and use balance (no acceleration) in the perpendicular direction.

### A conical pendulum

A bob on a string swings in a horizontal circle, so the string sweeps out a cone. There is no vertical acceleration, so the vertical forces balance. The horizontal component of the tension is the only force towards the centre.

:::html
<figure class="fig small"><svg viewBox="60 15 255 230" role="img" aria-label="A conical pendulum. A string of length L from a pivot at the top makes an angle theta with the vertical and carries a bob moving in a horizontal circle of radius r, drawn as a dashed ellipse. The tension T acts along the string towards the pivot and the weight W downwards."><path class="ln thick" d="M120 30H200"/><path class="ln-m thin dash" d="M160 30V177.2"/><path class="ln-m thin dash" d="M75 177.2A85 22 0 1 0 245 177.2A85 22 0 1 0 75 177.2"/><path class="ln-m thin dash" d="M160 177.2H245"/><path class="ln" d="M160 30L245 177.2"/><path class="ln-m thin" d="M160 80A50 50 0 0 0 185 73.3"/><circle class="fp s-ink sw2" cx="245" cy="177.2" r="10"/><path class="c1" d="M245 177.2L210 116.6" marker-end="url(#ah-phys)"/><path class="c1" d="M245 177.2V235" marker-end="url(#ah-phys)"/><circle class="fi" cx="160" cy="30" r="3.5"/><circle class="fi" cx="160" cy="177.2" r="3"/><text class="tl tc" x="180" y="98">θ</text><text class="tl ti tc" x="192" y="124">L</text><text class="tl ti tc" x="200" y="171">r</text><text class="tl ti" x="238" y="140">T</text><text class="tl" x="255" y="232">W = mg</text></svg><figcaption>The bob moves in a horizontal circle of radius r. The string makes angle θ with the vertical. The two forces are the tension T and the weight W; the horizontal component of T points to the centre of the circle.</figcaption></figure>
:::

:::formula Conical pendulum
\[\text{vertical: } T\cos\theta = mg \qquad \text{horizontal: } T\sin\theta = mr\omega^2 \qquad\Rightarrow\qquad \tan\theta = \frac{r\omega^2}{g}\]
Divide the two equations to remove \(T\) and \(m\). The radius is \(r = L\sin\theta\) for a string of length \(L\).
:::

:::eg A bob of mass 0.20 kg hangs on a string of length 0.80 m, which makes an angle of \(30^\circ\) with the vertical as the bob moves in a horizontal circle. Find the tension, the speed of the bob and the period.
Vertical: \(T\cos 30^\circ = mg\), so \(T = \dfrac{0.20 \times 9.81}{\cos 30^\circ} = 2.3\,\mathrm{N}\). [C1] [A1]

The radius of the circle is \(r = 0.80\sin 30^\circ = 0.40\,\mathrm{m}\). Then \(\omega^2 = \dfrac{g\tan\theta}{r} = \dfrac{9.81 \times \tan 30^\circ}{0.40} = 14.2\,\mathrm{rad^2\,s^{-2}}\), so \(\omega = 3.76\,\mathrm{rad\,s^{-1}}\). [C1]

Speed: \(v = r\omega = 0.40 \times 3.76 = 1.5\,\mathrm{m\,s^{-1}}\). [A1]

Period: \(T_\text{period} = \dfrac{2\pi}{\omega} = 1.7\,\mathrm{s}\). [A1]

The mass cancelled out of \(\omega\): a heavier bob at the same angle would go round at the same rate.
:::

### A ball in a vertical circle

In a vertical circle the weight points the same way at every point, but the centre moves from "above" to "below" the ball, so the tension needed changes round the circle. Energy also changes: the ball is slowest at the top and fastest at the bottom, so use energy conservation to find the speed at one point from the other.

:::html
<figure class="fig small"><svg viewBox="150 10 220 300" role="img" aria-label="A ball on a string moving in a vertical circle, anticlockwise. At the top the tension T and the weight W both point down, towards the centre. At the bottom the tension T points up, towards the centre, and the weight W points down. The velocity v is along the tangent at each point."><path class="ln-m thin dash" d="M260 50A100 100 0 1 0 260 250A100 100 0 1 0 260 50"/><path class="ln-m thin" d="M260 60V240"/><circle class="fi" cx="260" cy="150" r="3.5"/><circle class="fp s-ink sw2" cx="260" cy="50" r="10"/><circle class="fp s-ink sw2" cx="260" cy="250" r="10"/><path class="c1" d="M260 60V105" marker-end="url(#ah-phys)"/><path class="c1" d="M273 57V92" marker-end="url(#ah-phys)"/><path class="c2" d="M248 50H200" marker-end="url(#ah2-phys)"/><path class="c1" d="M260 240V180" marker-end="url(#ah-phys)"/><path class="c1" d="M260 260V295" marker-end="url(#ah-phys)"/><path class="c2" d="M272 250H320" marker-end="url(#ah2-phys)"/><text class="tl ti te" x="252" y="92">T</text><text class="tl" x="282" y="84">W</text><text class="tl ti tc" x="224" y="42">v</text><text class="tl ti te" x="252" y="214">T</text><text class="tl" x="268" y="292">W</text><text class="tl ti tc" x="296" y="268">v</text></svg><figcaption>Top and bottom of the circle. At the top, tension and weight both point to the centre. At the bottom, the tension must exceed the weight, because their difference is the centripetal force. The arrow lengths show only that T is largest at the bottom.</figcaption></figure>
:::

:::formula Vertical circle (ball of mass m on a string, radius r)
\[\text{bottom: } T_\text{b} - mg = \frac{mv_\text{b}^2}{r} \qquad \text{top: } T_\text{t} + mg = \frac{mv_\text{t}^2}{r}\]
\[\text{energy: } \tfrac12 mv_\text{b}^2 = \tfrac12 mv_\text{t}^2 + mg(2r) \quad\Rightarrow\quad v_\text{b}^2 = v_\text{t}^2 + 4gr\]
The tension is largest at the bottom and smallest at the top. The string stays taut only if \(T_\text{t} \geq 0\), which needs \(v_\text{t}^2 \geq gr\). So the **minimum speed at the top** is \(v_\text{t} = \sqrt{gr}\), and the minimum speed at the bottom for the ball to complete the circle is \(v_\text{b} = \sqrt{5gr}\).
:::

:::eg A ball of mass 0.20 kg is whirled on a string of length 0.60 m in a vertical circle. At the bottom its speed is \(6.0\,\mathrm{m\,s^{-1}}\). Find the tension at the bottom, the speed at the top and the tension at the top.
Bottom: the resultant force towards the centre (up) is \(T - mg = mv^2/r\), so
\[T_\text{b} = mg + \frac{mv_\text{b}^2}{r} = 0.20 \times 9.81 + \frac{0.20 \times 6.0^2}{0.60}\] [C1] \(= 14\,\mathrm{N}\). [A1]

The top is a height \(2r = 1.2\,\mathrm{m}\) higher. The kinetic energy lost equals the gravitational potential energy gained:
\[v_\text{t}^2 = v_\text{b}^2 - 4gr = 36 - 4 \times 9.81 \times 0.60 = 12.5\,\mathrm{m^2\,s^{-2}}\] [C1]
so \(v_\text{t} = 3.5\,\mathrm{m\,s^{-1}}\). [A1]

Top: both forces point to the centre (down), so \(T + mg = mv^2/r\) and
\[T_\text{t} = \frac{0.20 \times 12.5}{0.60} - 0.20 \times 9.81 = 2.2\,\mathrm{N}\] [C1] [A1]
This is positive, so the string stays taut. With a bottom speed of only \(4.0\,\mathrm{m\,s^{-1}}\), the formula would give \(v_\text{t}^2 < 0\): the string would go slack before the top, and the ball would leave the circle. The minimum bottom speed is \(\sqrt{5gr} = 5.4\,\mathrm{m\,s^{-1}}\).
:::

### Over the top of a hump-back bridge

A car on a hump-back bridge moves on part of a vertical circle with the centre **below** the car. Weight points down (towards the centre) and the normal contact force \(N\) from the road points up, so

\[mg - N = \frac{mv^2}{r} \qquad\Rightarrow\qquad N = mg - \frac{mv^2}{r}\]

The faster the car goes, the smaller \(N\) becomes. When \(N = 0\) the road no longer pushes on the tyres, and the car loses contact with it: this happens at \(v = \sqrt{gr}\), the speed at which weight alone provides the centripetal force.

:::eg A car of mass 900 kg crosses a hump-back bridge, which is part of a circle of radius 40 m, at \(15\,\mathrm{m\,s^{-1}}\). Find the normal contact force from the road on the car at the top and the speed at which the car would leave the road.
\[N = mg - \frac{mv^2}{r} = 900 \times 9.81 - \frac{900 \times 15^2}{40}\] [C1] \(= 8829 - 5063 = 3.8 \times 10^{3}\,\mathrm{N}\). [A1]

The car leaves the road when \(N = 0\): \(v = \sqrt{gr} = \sqrt{9.81 \times 40}\) [C1] \(= 20\,\mathrm{m\,s^{-1}}\). [A1]

At \(15\,\mathrm{m\,s^{-1}}\) the passengers feel lighter, because the road pushes up with only 3.8 kN instead of the 8.8 kN of their weight.
:::

### Charged particles and satellites

Two later chapters need only the equation you have just met. A charged particle of charge \(q\) moving at speed \(v\) at right angles to a magnetic field of flux density \(B\) feels a force \(Bqv\) at right angles to its velocity, so it moves in a circle with \(Bqv = mv^2/r\). An electron of speed \(2.0 \times 10^{7}\,\mathrm{m\,s^{-1}}\) in a field of \(1.0\,\mathrm{mT}\) moves on a circle of radius \(r = mv/(Be) = 0.11\,\mathrm{m}\) (more in [Magnetic fields](#phys.magnetic)). A satellite orbits because the Earth's gravitational pull is the centripetal force: the whole of [Gravitational fields](#phys.gravity) is this chapter with a particular force in place of \(F\).

:::board
Cambridge, AQA, Edexcel IAL and OCR all teach circular motion with the same equations. Some textbooks write \(\omega = v/r\) first and \(v = r\omega\) second; they are the same equation. UK specifications use "centripetal force" and "centripetal acceleration" in the same way as above.
:::

:::eg Spot the error: a turntable of radius 0.15 m turns at 33 revolutions per minute. Calculate the speed of a point on its edge.
A student wrote this answer.

Line 1: \(\omega = 33\) revolutions per minute
Line 2: \(v = r\omega = 0.15 \times 33 = 5.0\,\mathrm{m\,s^{-1}}\)

**Line 2 is wrong: \(v = r\omega\) needs \(\omega\) in radians per second, and 33 rpm is not that. The substitution mark is lost because the wrong quantity was substituted.** [C0] [A0]

Correct working: \(\omega = 33 \times \dfrac{2\pi}{60}\) [C1] \(= 3.46\,\mathrm{rad\,s^{-1}}\), so \(v = 0.15 \times 3.46 = 0.52\,\mathrm{m\,s^{-1}}\). [A1]

Check: \(5.0\,\mathrm{m\,s^{-1}}\) is the speed of a sprinter, far too fast for the edge of a record player. A speed of about half a metre per second is sensible.
:::

:::try Start easy, finish at exam standard
Q: Convert 72° to radians and 3.5 rad to degrees.
A: \(72 \times \pi/180 = 1.26\,\mathrm{rad}\) and \(3.5 \times 180/\pi = 201^\circ\).
Q: A point on a fan blade is 0.18 m from the axis. It turns through 40°. How far along its circular path does it move?
A: \(\theta = 40 \times \pi/180 = 0.698\,\mathrm{rad}\), so \(s = r\theta = 0.18 \times 0.698 = 0.13\,\mathrm{m}\).
Q: The second hand of a clock is 0.12 m long. Find its angular speed and the speed of its tip.
A: \(T = 60\,\mathrm{s}\), so \(\omega = 2\pi/60 = 0.105\,\mathrm{rad\,s^{-1}}\) and \(v = r\omega = 0.12 \times 0.105 = 1.3 \times 10^{-2}\,\mathrm{m\,s^{-1}}\).
Q: A town at latitude 52° rotates with the Earth. The circle it travels on has radius \(R\cos 52^\circ\), where \(R = 6.37 \times 10^{6}\,\mathrm{m}\). Find its speed.
A: \(r = 6.37 \times 10^{6} \times \cos 52^\circ = 3.92 \times 10^{6}\,\mathrm{m}\) and \(\omega = 7.27 \times 10^{-5}\,\mathrm{rad\,s^{-1}}\), so \(v = r\omega = 285\,\mathrm{m\,s^{-1}}\), less than at the Equator because the circle is smaller.
Q: A car of mass 1000 kg drives at \(20\,\mathrm{m\,s^{-1}}\) round a bend of radius 80 m. Find its centripetal acceleration and the centripetal force.
A: \(a = v^2/r = 20^2/80 = 5.0\,\mathrm{m\,s^{-2}}\) and \(F = ma = 1000 \times 5.0 = 5.0 \times 10^{3}\,\mathrm{N}\).
Q: A 0.30 kg ball is whirled on a string of length 0.90 m at 2.0 revolutions per second, in a horizontal circle on a smooth table. Find the tension.
A: \(\omega = 2\pi \times 2.0 = 12.6\,\mathrm{rad\,s^{-1}}\), so \(T = mr\omega^2 = 0.30 \times 0.90 \times 12.6^2 = 43\,\mathrm{N}\).
Q: Explain why a centripetal force does no work on an object moving in a circle.
A: The force is always perpendicular to the velocity, so the object has no displacement in the direction of the force. Work done is force times displacement in the direction of the force, so it is zero, and the kinetic energy and speed do not change.
Q: A car takes a bend at \(10\,\mathrm{m\,s^{-1}}\). By what factor must the friction force increase to take the same bend at \(20\,\mathrm{m\,s^{-1}}\)? What if the radius were half as large at \(10\,\mathrm{m\,s^{-1}}\)?
A: \(F \propto v^2\), so doubling the speed gives \(2^2 = 4\) times the force. \(F \propto 1/r\), so halving the radius gives twice the force.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define the radian.
A: The angle subtended at the centre of a circle by an arc equal in length to the radius. [B1]
Q: [3 marks] ★ A car wheel of radius 0.30 m turns through 25 complete revolutions in 4.0 s. The car does not skid. Calculate the angular speed of the wheel and the speed of the car.
A: \(\omega = \dfrac{25 \times 2\pi}{4.0}\) [C1] \(= 39\,\mathrm{rad\,s^{-1}}\). [A1] \(v = r\omega = 0.30 \times 39.3 = 12\,\mathrm{m\,s^{-1}}\). [A1]
Q: [2 marks] ★ A satellite moves at constant speed in a circle round the Earth. Explain why the satellite is accelerating.
A: Its velocity changes because its direction of motion keeps changing, even though the speed is constant. [B1] Acceleration is the rate of change of velocity, so it accelerates, towards the centre of the circle. [B1]
Q: [4 marks] ★★ A car of mass 1400 kg takes a flat bend of radius 80 m. The road can supply a maximum friction force of 7.0 kN. (a) Calculate the maximum speed on the bend. (b) The road is wet and the maximum friction force halves. State the new maximum speed.
A: (a) \(F = mv^2/r\), so \(v^2 = \dfrac{7000 \times 80}{1400}\) [C1] \(= 400\) [C1] so \(v = 20\,\mathrm{m\,s^{-1}}\). [A1] (b) \(v \propto \sqrt{F}\), so the speed falls to \(20/\sqrt{2} = 14\,\mathrm{m\,s^{-1}}\). [A1]
Q: [5 marks] ★★ A bob of mass 0.15 kg hangs from a string of length 0.50 m and moves in a horizontal circle of radius 0.30 m. (a) Show that the angle of the string to the vertical is \(37^\circ\) and calculate the tension. (b) Calculate the period of the motion.
H: Draw the right-angled triangle with hypotenuse 0.50 m and the radius 0.30 m as the opposite side.
H: Vertically the tension component balances the weight; horizontally the other component gives \(mr\omega^2\).
A: (a) \(\sin\theta = 0.30/0.50 = 0.60\), so \(\theta = 37^\circ\). [B1] \(T\cos\theta = mg\) so \(T = \dfrac{0.15 \times 9.81}{0.80}\) [C1] \(= 1.8\,\mathrm{N}\). [A1] (b) \(T\sin\theta = mr\omega^2\), so \(\omega^2 = \dfrac{1.84 \times 0.60}{0.15 \times 0.30}\) [C1] \(= 24.5\), \(\omega = 4.95\,\mathrm{rad\,s^{-1}}\), and the period is \(2\pi/\omega = 1.3\,\mathrm{s}\). [A1]
Q: [6 marks] ★★★ A bucket and water of total mass 0.50 kg are swung on a rope of length 0.90 m in a vertical circle. At the top of the circle the speed is \(3.5\,\mathrm{m\,s^{-1}}\). (a) Calculate the tension in the rope at the top. (b) Use energy conservation to find the speed at the bottom. (c) Calculate the tension at the bottom.
H: At the top both the weight and the tension point to the centre.
H: The bucket falls through \(2r\) between the top and the bottom.
A: (a) \(T + mg = mv^2/r\), so \(T = \dfrac{0.50 \times 3.5^2}{0.90} - 0.50 \times 9.81\) [C1] \(= 1.9\,\mathrm{N}\). [A1] (b) \(\tfrac12 mv_\text{b}^2 = \tfrac12 mv_\text{t}^2 + mg(2r)\), so \(v_\text{b}^2 = 3.5^2 + 4 \times 9.81 \times 0.90\) [C1] \(= 47.6\), \(v_\text{b} = 6.9\,\mathrm{m\,s^{-1}}\). [A1] (c) \(T - mg = mv_\text{b}^2/r\), so \(T = 0.50 \times 9.81 + \dfrac{0.50 \times 47.6}{0.90}\) [C1] \(= 31\,\mathrm{N}\). [A1]
Q: [6 marks] ★★★ A fairground rotor is a vertical cylinder of radius 2.5 m. It turns about its vertical axis at 0.50 revolutions per second, and a rider of mass 60 kg is pressed against the wall. (a) Calculate the normal contact force of the wall on the rider. (b) Calculate the friction force that holds the rider up. (c) The rotor now turns twice as fast. State and explain what happens to the normal contact force and to the friction force.
H: The normal contact force is the only horizontal force on the rider, so it is the centripetal force.
H: The rider is not moving vertically, so the vertical forces balance.
A: (a) \(\omega = 2\pi \times 0.50 = \pi\,\mathrm{rad\,s^{-1}}\) [C1] and \(N = mr\omega^2 = 60 \times 2.5 \times \pi^2 = 1.5 \times 10^{3}\,\mathrm{N}\). [A1] (b) The rider has no vertical acceleration, so friction equals weight [B1]: \(F = mg = 60 \times 9.81 = 5.9 \times 10^{2}\,\mathrm{N}\). [A1] (c) \(N \propto \omega^2\), so the normal contact force becomes four times larger. [B1] The friction force is still equal to the weight, so it is unchanged. [B1]
:::

The first stretch problem uses this cross-section of a banked track.

:::html
<figure class="fig small"><svg viewBox="25 70 290 160" role="img" aria-label="Cross-section of a banked track rising from left to right at angle theta to the horizontal. A car, shown as a dot on the surface, has weight W downwards and the normal contact force N at right angles to the track, tilted towards the left, which is the centre of the bend."><path class="ln" d="M40 200L300 105.4"/><path class="ln-m thin dash" d="M40 200H140"/><path class="ln-m thin" d="M110 200A70 70 0 0 0 105.8 176.1"/><text class="tl tc" x="127" y="189">θ</text><circle class="fi" cx="170" cy="152.7" r="5"/><path class="c1" d="M170 152.7V207.7" marker-end="url(#ah-phys)"/><path class="c1" d="M170 152.7L146.1 86.9" marker-end="url(#ah-phys)"/><text class="tl ti te" x="140" y="90">N</text><text class="tl" x="180" y="206">W = mg</text></svg><figcaption>A cross-section of the track with the centre of the bend to the left. Weight and the normal contact force are the only forces; the horizontal component of N points to the centre.</figcaption></figure>
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A car travels round a banked circular track of radius 120 m. The outer edge of the track is higher than the inner edge, so the surface is inclined at \(15^\circ\) to the horizontal. At one particular speed, no sideways friction is needed. (a) By resolving the normal contact force \(N\) vertically and horizontally, show that this speed satisfies \(v^2 = rg\tan\theta\). (b) Calculate the speed. (c) Explain what happens if the car goes faster than this speed.
H: Only two real forces act: the weight and the normal contact force, which is at right angles to the track surface, so it leans towards the centre.
H: The horizontal component of \(N\) is the centripetal force; the vertical component balances the weight.
A: (a) \(N\cos\theta = mg\) [M1] and \(N\sin\theta = mv^2/r\). [M1] Dividing gives \(\tan\theta = \dfrac{v^2}{rg}\), so \(v^2 = rg\tan\theta\). [A1] (b) \(v^2 = 120 \times 9.81 \times \tan 15^\circ = 315\), so \(v = 18\,\mathrm{m\,s^{-1}}\). [A1] (c) Without friction the car would need a bigger centripetal force than the horizontal component of \(N\) can give, so it would slide outwards up the slope. [B1] Friction down the slope, towards the centre, then supplies the extra force. [B1]
Q: [6 marks] ★★★ A small ball is released from rest on a smooth track that leads into a vertical loop of radius \(r = 0.40\,\mathrm{m}\). (a) Show that the ball at the top of the loop must have a speed of at least \(\sqrt{gr}\) to stay in contact with the track. (b) Show that it must be released from a height of at least \(2.5r\) above the bottom of the loop. (c) Calculate this height for the loop above and the speed of the ball at the bottom.
H: At the limit the track pushes on the ball with zero force at the top, so the weight alone is the centripetal force.
H: Use the speed at the top in energy conservation from the release point to the top, at height \(2r\).
A: (a) At the top, weight and normal contact force \(N\) both point to the centre: \(N + mg = mv^2/r\). [B1] The ball stays in contact if \(N \geq 0\), so \(mv^2/r \geq mg\), that is \(v \geq \sqrt{gr}\). [M1] (b) Energy: \(mgh = mg(2r) + \tfrac12 mv^2\) [M1] with \(v^2 = gr\) gives \(h = 2r + r/2 = 2.5r\). [A1] (c) \(h = 2.5 \times 0.40 = 1.0\,\mathrm{m}\). [A1] The speed at the bottom comes from \(\tfrac12 mv^2 = mgh\), so \(v = \sqrt{2 \times 9.81 \times 1.0} = 4.4\,\mathrm{m\,s^{-1}}\). [A1]
:::

:::quiz
? What is the size of one radian?
+ The angle subtended at the centre by an arc equal in length to the radius
- The angle subtended at the centre by an arc equal in length to the diameter
- The angle at which the arc is exactly 1 m long
- 360 divided by 2
> One radian is the angle at the centre when arc length equals the radius, about 57.3°. The diameter version would be 2 rad, and arc length alone says nothing without the radius.
? A body moves in a circle at constant speed. Which statement is correct?
+ Its acceleration has constant size and points to the centre.
- Its acceleration is zero because its speed is constant.
- Its acceleration points along the direction of motion.
- Its acceleration points away from the centre.
> Acceleration is a change of velocity, and the direction of the velocity keeps changing. The acceleration is perpendicular to the velocity, towards the centre. Zero acceleration needs constant velocity, not just constant speed.
? A stone whirled on a string in a horizontal circle is released when the string breaks. Which path does it take, seen from above?
+ A straight line along the tangent to the circle at that point
- A straight line away from the centre along the radius
- It continues round the circle for a while
- A curve that spirals outwards
> With no resultant force, it keeps the velocity it had at that moment, which is along the tangent. An outward radial path would need an outward "centrifugal" force, which does not exist.
? A car takes a bend at \(10\,\mathrm{m\,s^{-1}}\). It then takes the same bend at \(20\,\mathrm{m\,s^{-1}}\). By what factor must the centripetal force increase?
+ 4
- 2
- 8
- It stays the same
> \(F = mv^2/r\), so \(F \propto v^2\) and doubling the speed gives four times the force. A factor of 2 would be correct if \(F \propto v\).
? A ball moves on a string in a vertical circle at varying speed. Where is the tension greatest?
+ At the bottom
- At the top
- At the side, level with the centre
- It is the same everywhere
> At the bottom, the tension must exceed the weight (\(T - mg = mv^2/r\)) and the ball is also moving fastest. At the top, the weight helps provide the centripetal force, so the tension is least.
? Which statement about the centripetal force is correct?
+ It is the resultant of the real forces towards the centre.
- It is an extra force that acts in addition to tension, weight and friction.
- It acts outwards and balances the real forces.
- It does work, which increases the speed.
> Centripetal force names the job done by the real forces. It is not an extra force, it points inwards, and it is perpendicular to the motion, so it does no work.
? A car crosses the top of a hump-back bridge. How does the normal contact force \(N\) from the road compare with the car's weight \(mg\)?
+ \(N\) is smaller than \(mg\).
- \(N\) is larger than \(mg\).
- \(N\) equals \(mg\).
- \(N\) is zero at any speed.
> The resultant force towards the centre (down) is \(mg - N = mv^2/r\), which is positive, so \(N < mg\). \(N\) would be larger on the bottom of a dip.
:::

:::checklist What you can now do
- [ ] I can define the radian and angular displacement, convert between degrees and radians, and use \(s = r\theta\).
- [ ] I can define angular speed and use \(\omega = 2\pi/T\), \(\omega = 2\pi f\) and \(v = r\omega\), converting revolutions per minute.
- [ ] I can explain why a body moving in a circle at constant speed is accelerating, and give the direction of the acceleration.
- [ ] I can use \(a = v^2/r\) and \(a = r\omega^2\) for centripetal acceleration.
- [ ] I can explain that a constant force perpendicular to the velocity gives uniform circular motion and does no work.
- [ ] I can use \(F = mv^2/r\) and \(F = mr\omega^2\), and name the real force that provides the centripetal force.
- [ ] I can solve problems on a flat bend, a conical pendulum, a vertical circle and a hump-back bridge.
- [ ] I can explain why there is no centrifugal force.
:::

:::recap
- One radian is the angle at the centre when the arc equals the radius. \(2\pi\,\mathrm{rad} = 360^\circ\) and \(s = r\theta\) (\(\theta\) in radians).
- Angular speed \(\omega = \Delta\theta/\Delta t = 2\pi/T = 2\pi f\), in \(\mathrm{rad\,s^{-1}}\). Linear speed \(v = r\omega\).
- In circular motion at constant speed the velocity changes direction, so there is an acceleration \(a = v^2/r = r\omega^2\) directed towards the centre.
- The resultant force towards the centre is \(F = mv^2/r = mr\omega^2\). It is not an extra force: it is the resultant of tension, friction, gravity, normal contact or magnetic forces.
- A force perpendicular to the velocity does no work, so the speed is constant.
- There is no centrifugal force. If the force stops, the object moves off along the tangent.
- Conical pendulum: \(T\cos\theta = mg\) and \(T\sin\theta = mr\omega^2\). Vertical circle: \(T_\text{b} - mg = mv^2/r\) at the bottom, \(T_\text{t} + mg = mv^2/r\) at the top, with a minimum speed of \(\sqrt{gr}\) at the top.
- Convert rpm to \(\mathrm{rad\,s^{-1}}\) with \(2\pi/60\), and use the radius, not the diameter.
:::

:::links
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Gravitational fields](#phys.gravity)
