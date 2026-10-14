@chapter phys.gravity
@title Gravitational fields
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary Gravitational field strength and field lines, Newton's law of gravitation, g = GM/r², circular orbits and geostationary satellites, and gravitational potential and potential energy, which are negative and zero at infinity.

:::why
Gravity holds the Moon on its path, puts satellites in orbit for GPS, television and weather forecasting, and decides how much energy it takes to leave the Earth at all. One law, \(F = Gm_1m_2/r^2\), explains all of it, and this chapter turns that law into the working tools of A Level: field strength, orbital speed and period, potential and potential energy. The same ideas return in [Electric fields](#phys.efields), where the inverse-square law and the potential are just as important.
:::

**Before you start**, you need circular motion from [Motion in a circle](#phys.circular) and \(\Delta E_\text{P} = mg\Delta h\) from [Work, energy and power](#phys.energy).

:::try Warm-up
Q: A satellite completes one orbit every 90 minutes. Find its angular speed. (from [Motion in a circle](#phys.circular))
A: \(T = 90 \times 60 = 5400\,\mathrm{s}\), so \(\omega = 2\pi/T = 1.2 \times 10^{-3}\,\mathrm{rad\,s^{-1}}\).
Q: A climber of mass 80 kg climbs 500 m. How much gravitational potential energy does she gain? (from [Work, energy and power](#phys.energy))
A: \(\Delta E_\text{P} = mg\Delta h = 80 \times 9.81 \times 500 = 3.9 \times 10^{5}\,\mathrm{J}\).
Q: What is the weight of a 65 kg person at the Earth's surface? (from [Dynamics and momentum](#phys.dynamics))
A: \(W = mg = 65 \times 9.81 = 640\,\mathrm{N}\) (to 2 significant figures).
:::

## Fields of force

Two magnets attract each other across empty space, and the Earth pulls on a falling apple without touching it. Physicists describe this "action at a distance" with a **field**: the region around an object in which another object feels a force. The source changes the space around it, and any other object placed there feels the effect.

:::def Gravitational field
A region of space in which a mass experiences a force.
:::

A big mass makes a stronger field than a small one, and a heavier object placed in the field feels a bigger force. To describe the field itself, independent of the object you test it with, divide out the mass of the object.

:::def Gravitational field strength
The gravitational force per unit mass acting on a small test mass placed at that point in the field. \(g = F/m\).
:::

The unit is \(\mathrm{N\,kg^{-1}}\). Since \(1\,\mathrm{N} = 1\,\mathrm{kg\,m\,s^{-2}}\), this is the same as \(\mathrm{m\,s^{-2}}\), so field strength and the acceleration of free fall are the same quantity. At the surface of the Earth, \(g = 9.81\,\mathrm{N\,kg^{-1}}\): every kilogram feels a pull of 9.81 N. Field strength is a **vector**: its direction is the direction of the force on a mass, here towards the centre of the Earth.

### Field lines

A **field line** shows the direction of the force on a small mass placed in the field, and an arrow on the line shows the direction. Where lines are closer together the field is stronger. Lines never cross, because the field has only one direction at each point.

:::html
<figure class="fig wide"><svg viewBox="30 0 515 255" role="img" aria-label="Two field-line diagrams. Left: a planet with eight straight radial field lines, spaced evenly round it, with arrows pointing towards the planet. Right: five equally spaced parallel vertical lines pointing down towards a flat surface."><text class="tl tc" x="150" y="18">Radial field round a planet</text><path class="ln" d="M255 140L194 140"/><path class="c1" d="M234 140L216 140" marker-end="url(#ah-phys)"/><path class="ln" d="M224.2 65.8L181.1 108.9"/><path class="c1" d="M209.4 80.6L196.7 93.3" marker-end="url(#ah-phys)"/><path class="ln" d="M150 35L150 96"/><path class="c1" d="M150 56L150 74" marker-end="url(#ah-phys)"/><path class="ln" d="M75.8 65.8L118.9 108.9"/><path class="c1" d="M90.6 80.6L103.3 93.3" marker-end="url(#ah-phys)"/><path class="ln" d="M45 140L106 140"/><path class="c1" d="M66 140L84 140" marker-end="url(#ah-phys)"/><path class="ln" d="M75.8 214.2L118.9 171.1"/><path class="c1" d="M90.6 199.4L103.3 186.7" marker-end="url(#ah-phys)"/><path class="ln" d="M150 245L150 184"/><path class="c1" d="M150 224L150 206" marker-end="url(#ah-phys)"/><path class="ln" d="M224.2 214.2L181.1 171.1"/><path class="c1" d="M209.4 199.4L196.7 186.7" marker-end="url(#ah-phys)"/><circle class="f1 s-acc sw2" cx="150" cy="140" r="40"/><text class="tl tc" x="150" y="144">planet</text><text class="tl tc" x="430" y="18">Uniform field near the surface</text><path class="ln" d="M370 45V186M400 45V186M430 45V186M460 45V186M490 45V186"/><path class="c1" d="M370 100V126" marker-end="url(#ah-phys)"/><path class="c1" d="M400 100V126" marker-end="url(#ah-phys)"/><path class="c1" d="M430 100V126" marker-end="url(#ah-phys)"/><path class="c1" d="M460 100V126" marker-end="url(#ah-phys)"/><path class="c1" d="M490 100V126" marker-end="url(#ah-phys)"/><rect class="fm s-mute sw1" x="350" y="190" width="160" height="32"/><text class="tl tc" x="430" y="210">surface of the Earth</text></svg><figcaption>Left: around a planet the lines are radial and get closer together nearer the surface, so the field gets stronger there. Right: close to the surface, over a distance that is tiny compared with the radius, the lines are parallel and equally spaced, so the field is uniform.</figcaption></figure>
:::

The two pictures are the same field seen at different scales. A small patch near the surface of a large sphere looks flat, and the radial lines in that patch are almost parallel. That is why we can treat \(g\) as constant for everyday heights, and why we need the radial picture for orbits.

## Newton's law of gravitation

Newton realised that the force that makes an apple fall is the same force that keeps the Moon in orbit, and that it depends on the two masses and on their separation.

:::def Newton's law of gravitation
The gravitational force between two point masses is proportional to the product of their masses and inversely proportional to the square of their separation.
:::

:::formula Newton's law of gravitation
\[F = \frac{Gm_1m_2}{r^2}\]
\(F\): force on each mass (N) · \(G\): gravitational constant, \(6.67 \times 10^{-11}\,\mathrm{N\,m^2\,kg^{-2}}\) · \(m_1, m_2\): the two masses (kg) · \(r\): distance **between the centres** (m).
:::

Four points to keep in mind:

- The force is always **attractive**.
- The two masses pull each other with forces of the same size and opposite direction, whatever their masses: they are a Newton's third law pair. The Earth pulls the Moon exactly as hard as the Moon pulls the Earth.
- A uniform sphere, such as a planet or a star, acts on anything **outside** it as if all its mass were concentrated at its centre. So \(r\) is the distance from the centre of the sphere, and a planet can be treated as a point mass.
- It is an **inverse-square law**: \(F \propto 1/r^2\). Double the distance and the force falls to one quarter. Triple it and the force falls to one ninth. Halve the distance and the force becomes four times larger.

:::eg Find the force between the Earth and the Moon. The mass of the Earth is \(5.97 \times 10^{24}\,\mathrm{kg}\), the mass of the Moon is \(7.35 \times 10^{22}\,\mathrm{kg}\), and their centres are \(3.84 \times 10^{8}\,\mathrm{m}\) apart.
\[F = \frac{Gm_1m_2}{r^2} = \frac{6.67 \times 10^{-11} \times 5.97 \times 10^{24} \times 7.35 \times 10^{22}}{\left(3.84 \times 10^{8}\right)^2}\] [C1]
\[F = 1.98 \times 10^{20}\,\mathrm{N}\] [A1]
Each body pulls on the other with this force.
:::

:::eg Two students of mass 70 kg stand 1.0 m apart. Calculate the gravitational force between them and compare it with the weight of one student.
\[F = \frac{6.67 \times 10^{-11} \times 70 \times 70}{1.0^2} = 3.3 \times 10^{-7}\,\mathrm{N}\] [C1] [A1]
The weight of one student is \(70 \times 9.81 = 690\,\mathrm{N}\), about two billion times bigger. The gravitational force between everyday objects is far too small to notice: you only see gravity when one of the masses is as big as a planet.
:::

:::eg A satellite experiences a gravitational force of 8.0 kN when it is at the surface of the Earth. What force does it experience when it is at a height equal to twice the radius of the Earth above the surface?
At a height of 2 radii the distance from the **centre** is \(R + 2R = 3R\), three times the original distance. [B1]

The force is inversely proportional to \(r^2\), so it falls by a factor \(3^2 = 9\): \(F = 8.0/9 = 0.89\,\mathrm{kN}\). [A1]
:::

:::warn r is measured from the centre
The most common error in this chapter is to use the height above the surface, or the radius of a planet when the object is above it, as \(r\). Always write \(r = R + h\) first, where \(R\) is the radius of the planet and \(h\) is the height above its surface.
:::

## The field strength of a point mass

Put the definition of field strength and Newton's law together. A small mass \(m\) at distance \(r\) from a point mass or uniform sphere \(M\) feels a force \(GMm/r^2\). The field strength at that point is the force per unit mass.

:::proof examinable Gravitational field strength of a point mass
By Newton's law of gravitation, the force on a small mass \(m\) at distance \(r\) from a point mass \(M\) is \(F = \dfrac{GMm}{r^2}\).
By definition, the gravitational field strength is the force per unit mass: \(g = \dfrac{F}{m}\).
Substitute for \(F\): \(g = \dfrac{GMm}{r^2m}\).
The test mass \(m\) cancels, so \(g\) does not depend on it:
\[g = \frac{GM}{r^2}\]
The field strength is directed towards the mass \(M\).
:::

:::formula Field strength of a point mass or uniform sphere
\[g = \frac{GM}{r^2}\]
\(g\): gravitational field strength (\(\mathrm{N\,kg^{-1}}\)) · \(M\): mass producing the field (kg) · \(r\): distance from the centre of \(M\) (m), directed towards the centre. Outside the planet, \(g \propto 1/r^2\).
:::

:::eg Calculate the gravitational field strength at the surface of the Earth, using \(M = 5.97 \times 10^{24}\,\mathrm{kg}\) and \(R = 6.37 \times 10^{6}\,\mathrm{m}\).
\[g = \frac{GM}{R^2} = \frac{6.67 \times 10^{-11} \times 5.97 \times 10^{24}}{\left(6.37 \times 10^{6}\right)^2}\] [C1] \(= 9.81\,\mathrm{N\,kg^{-1}}\). [A1]
This agrees with the measured acceleration of free fall. (The product \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\) for the Earth appears in every orbit calculation: working it out once saves time.)
:::

:::eg The International Space Station orbits 408 km above the Earth's surface. Calculate the field strength there and compare it with the value at the surface.
\(r = 6.37 \times 10^{6} + 4.08 \times 10^{5} = 6.778 \times 10^{6}\,\mathrm{m}\). [C1]

\[g = \frac{GM}{r^2} = \frac{3.98 \times 10^{14}}{\left(6.778 \times 10^{6}\right)^2} = 8.66\,\mathrm{N\,kg^{-1}}\] [C1] [A1]
This is 88% of the surface value. Gravity is still strong at the height of the station: it is certainly not "zero gravity".
:::

:::warn Astronauts are not beyond gravity
The astronauts on the station weigh almost as much as on the ground, in the sense that gravity pulls on them with 88% of its surface strength. They seem weightless because they and the station are both in **free fall**: they fall towards the Earth at the same rate, and the station's floor never pushes up on them. Their sideways speed is so large that they keep missing the ground.
:::

### Why g is nearly constant near the surface

The graph of \(g\) against \(r\) falls steeply, but near the surface it is almost flat.

:::plot Gravitational field strength of the Earth against distance from its centre. It falls as 1/r² outside the surface, reaching one quarter of its surface value at r = 2R.
--f "398.2/x**2" --x 6.37 45 --y 0 12 --pt "6.37,9.81,surface: 9.81 N kg⁻¹@ne" --pt "12.74,2.45,r = 2R: 2.45@ne" --pt "42.2,0.22,geostationary orbit@nw" --xlabel "r / 10⁶ m" --ylabel "g / N kg⁻¹" --label "g = GM/r²"
:::

If you climb 1.0 km, \(r\) changes from \(6.37 \times 10^{6}\) m to \(6.371 \times 10^{6}\) m, a change of only 0.016%. Because \(g\) depends on \(1/r^2\), it changes by about twice that, 0.031%. Even the top of Mount Everest, at about 8.8 km, has \(g\) smaller by only 0.28%. For heights that are a tiny fraction of the Earth's radius, the radial field lines are indistinguishable from parallel ones, \(g\) is constant, and the potential energy change is \(mg\Delta h\). Over larger distances, as for a satellite, \(g\) varies greatly and you must use \(GM/r^2\).

## Circular orbits

An object in a circular orbit moves in a circle, so by [Motion in a circle](#phys.circular) it needs a centripetal force. In orbit, the gravitational force is the **only** force on the satellite, so it is the centripetal force.

:::formula Circular orbit
\[\frac{GMm}{r^2} = \frac{mv^2}{r} = mr\omega^2 \qquad\Rightarrow\qquad v = \sqrt{\frac{GM}{r}}\]
\(M\): mass of the body at the centre · \(m\): mass of the orbiting object · \(r\): orbital radius, from the centre of \(M\). The satellite's mass cancels: all satellites at the same radius move at the same speed, whatever their mass. A larger orbit means a **smaller** speed.
:::

Now put \(v = 2\pi r/T\) into this equation to find the period.

:::proof examinable Kepler's third law for circular orbits
A satellite of mass \(m\) orbits a body of mass \(M\) in a circle of radius \(r\) with period \(T\).
The gravitational force provides the centripetal force: \(\dfrac{GMm}{r^2} = mr\omega^2\).
The angular speed is \(\omega = \dfrac{2\pi}{T}\), so \(\dfrac{GMm}{r^2} = mr\dfrac{4\pi^2}{T^2}\).
Cancel \(m\) and multiply both sides by \(r^2\): \(GM = \dfrac{4\pi^2r^3}{T^2}\).
Rearrange:
\[T^2 = \frac{4\pi^2}{GM}\,r^3\]
So \(T^2 \propto r^3\): a graph of \(T^2\) against \(r^3\) is a straight line through the origin, with gradient \(4\pi^2/GM\).
:::

The ratio \(T^2/r^3\) depends only on the mass at the centre. All planets orbiting the Sun share one ratio, and all satellites of the Earth share another. If you measure the radius and period of a moon, you can find the mass of its planet.

:::eg Calculate the orbital speed and period of the International Space Station, which orbits at radius \(6.778 \times 10^{6}\,\mathrm{m}\). Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\) for the Earth.
\[v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{3.98 \times 10^{14}}{6.778 \times 10^{6}}}\] [C1] \(= 7.66 \times 10^{3}\,\mathrm{m\,s^{-1}}\). [A1]

\[T = \frac{2\pi r}{v}\] [C1] \(= 5.56 \times 10^{3}\,\mathrm{s} = 92.6\) minutes. [A1]

The station goes round the Earth about 16 times a day, and its astronauts see a sunrise roughly every 90 minutes.
:::

:::eg Io orbits Jupiter in a circle of radius \(4.22 \times 10^{8}\,\mathrm{m}\) with a period of 1.77 days. Calculate the mass of Jupiter.
\(T = 1.77 \times 86400 = 1.529 \times 10^{5}\,\mathrm{s}\). [C1]

From \(T^2 = \dfrac{4\pi^2r^3}{GM}\):
\[M = \frac{4\pi^2r^3}{GT^2} = \frac{4\pi^2 \times \left(4.22 \times 10^{8}\right)^3}{6.67 \times 10^{-11} \times \left(1.529 \times 10^{5}\right)^2}\] [C1]
\[M = 1.90 \times 10^{27}\,\mathrm{kg}\] [A1]
The mass of Io cancelled and was not needed. Astronomers find the mass of every planet with a moon this way.
:::

:::eg Calculate the orbital period of the Moon about the Earth, using \(r = 3.84 \times 10^{8}\,\mathrm{m}\).
\[T = 2\pi\sqrt{\frac{r^3}{GM}} = 2\pi\sqrt{\frac{\left(3.84 \times 10^{8}\right)^3}{3.98 \times 10^{14}}} = 2.37 \times 10^{6}\,\mathrm{s}\] [C1] [A1]
That is 27.4 days, close to the 27.3 days the Moon actually takes to orbit the Earth.
:::

## Geostationary orbits

Communications and television satellites need to stay in one place in the sky, so that a fixed dish on the ground can point at them. This is possible in one special orbit.

:::def Geostationary orbit
An orbit in which a satellite stays above the same point on the Equator. Its period is 24 hours, it moves from west to east, and its orbit is in the plane of the Equator.
:::

All four conditions are needed, and each has a reason:

- **Period 24 hours**: the satellite must go round once in the time that the Earth turns once, so that the two keep step.
- **West to east**: this is the direction the Earth rotates, so the satellite and the ground below it turn the same way.
- **Directly above the Equator**: the centre of any orbit must be the centre of the Earth, because gravity points there. Only an orbit in the plane of the Equator can stay over a point of the Earth's surface as it turns, because every other orbit swings north and south of it.
- **A single height**: for a period of 24 hours, \(T^2 = 4\pi^2r^3/GM\) fixes the radius, as the next example shows.

:::eg Calculate the radius of a geostationary orbit, and the height of the satellite above the Earth's surface. Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\) and \(R = 6.37 \times 10^{6}\,\mathrm{m}\).
The period is 24 hours: \(T = 24 \times 3600 = 8.64 \times 10^{4}\,\mathrm{s}\). [C1]

From \(GM = 4\pi^2r^3/T^2\):
\[r^3 = \frac{GMT^2}{4\pi^2} = \frac{3.98 \times 10^{14} \times \left(8.64 \times 10^{4}\right)^2}{4\pi^2} = 7.53 \times 10^{22}\,\mathrm{m^3}\] [C1]
so \(r = 4.22 \times 10^{7}\,\mathrm{m}\). [A1]

Height \(h = r - R = 4.22 \times 10^{7} - 6.37 \times 10^{6} = 3.59 \times 10^{7}\,\mathrm{m}\), that is \(3.6 \times 10^{4}\,\mathrm{km}\). [A1]

The speed is \(v = 2\pi r/T = 3.07 \times 10^{3}\,\mathrm{m\,s^{-1}}\), much slower than the space station, and \(g\) at this radius is only \(0.22\,\mathrm{N\,kg^{-1}}\).
:::

The geostationary orbit is used for television, telephone links and weather observation of one half of the globe. Its disadvantage is the great distance: a radio signal takes about a quarter of a second to travel up to the satellite and back down. Satellites that must observe the surface in detail, such as the space station and imaging satellites, use **low Earth orbits** a few hundred kilometres up, with periods of about 90 minutes. A **polar orbit** passes over both poles: because the Earth turns beneath it, the satellite passes over every part of the surface in turn, which suits mapping and monitoring the whole planet.

:::html
<figure class="fig small"><svg viewBox="20 12 410 395" role="img" aria-label="View from above the North Pole. The Earth is a small circle at the centre with a point P on the Equator. A dashed circle of radius about 6.6 Earth radii is the geostationary orbit, with a satellite on the line from the centre through P. A much smaller circle just outside the Earth is the orbit of the International Space Station. An arrow along the geostationary orbit points anticlockwise, west to east."><path class="ln-m thin dash" d="M210 210L340.8 79.2"/><path class="ln-m dash" d="M395 210A185 185 0 1 1 25 210A185 185 0 1 1 395 210"/><path class="c1" d="M257.9 31.3A185 185 0 0 0 162.1 31.3" marker-end="url(#ah-phys)"/><circle class="f1 s-acc sw2" cx="210" cy="210" r="28"/><text class="tl tc" x="210" y="214">Earth</text><path class="ln-m thin" d="M239.8 210A29.8 29.8 0 1 1 180.2 210A29.8 29.8 0 1 1 239.8 210"/><path class="ln-m thin" d="M188.9 231.1L152 258"/><text class="tl te" x="146" y="268">ISS orbit</text><circle class="fi" cx="229.8" cy="190.2" r="3.5"/><text class="tl tc" x="252" y="196">P</text><rect class="fp s-ink sw2" x="334.8" y="75.2" width="12" height="8"/><text class="tl" x="354" y="72">satellite</text><text class="tl tc" x="210" y="55">moves west to east</text><text class="tl tc" x="210" y="330">geostationary orbit</text><text class="tl tc" x="210" y="347">r = 4.22 × 10⁷ m</text></svg><figcaption>Looking down on the North Pole, the Earth turns anticlockwise. The satellite in geostationary orbit travels the same way and takes the same 24 hours, so it stays on the line through the point P on the Equator. The sizes are to scale: the geostationary orbit is 6.6 Earth radii from the centre, and the ISS orbit is almost touching the surface.</figcaption></figure>
:::

Now explore orbits yourself. Choose a body, move the radius slider and watch the period, speed and energies change. Then press the geostationary button and see the satellite stay above one point of the Earth.

:::html
<div class="widget" data-w="phys-orbit" data-body="earth" data-r="42200"></div>
:::

Look for three things. First, the time scale: every period is sped up by the same factor, so the comparison between orbits is honest. Second, \(T^2/r^3\) stays the same when you change the radius, so the point on the second graph slides along a straight line through the origin. Third, a larger orbit has a **lower** speed but a **higher** total energy.

## Gravitational potential

A satellite far from the Earth has more gravitational energy than one near it. To measure this for any mass, you divide the energy by the mass, as you divided force by mass to get field strength. The result is the **gravitational potential**. Its zero is chosen at infinite distance, where the field has faded to nothing.

:::def Gravitational potential
At a point, the work done per unit mass in bringing a small test mass from infinity to that point.
:::

:::formula Gravitational potential of a point mass
\[\phi = -\frac{GM}{r}\]
\(\phi\): gravitational potential (\(\mathrm{J\,kg^{-1}}\)) · \(M\): mass producing the field (kg) · \(r\): distance from its centre (m). Potential is **negative** everywhere, rises towards zero as \(r\) increases, and is zero at infinity.
:::

Why negative? Gravity is attractive, so as a mass moves in from infinity the gravitational field does work on it and the mass loses potential energy: it ends up below the zero at infinity. Equivalently, you must *supply* energy to take the mass back to infinity, so the work done in bringing it in from infinity is negative. The nearer to the planet, the more negative the potential.

:::proof Why φ = −GM/r
Move a small mass \(m\) from infinity to distance \(r\) from a point mass \(M\). At distance \(x\) the gravitational pull is \(GMm/x^2\), directed inwards.
To bring the mass in without speeding it up, an outward force of the same size must hold it back. This force points outwards while the mass moves inwards, so the work done by this force is negative.
Adding up the work over all the small steps from \(x = \infty\) to \(x = r\) (the area under the force–distance graph) gives \(-\dfrac{GMm}{r}\).
The work done per unit mass is this divided by \(m\), so \(\phi = -\dfrac{GM}{r}\).
:::

:::plot Gravitational potential of the Earth against distance from its centre. It is negative everywhere, and its gradient at any point is the field strength there.
--f "-398.2/x" --x 6.37 45 --y -70 5 --pt "6.37,-62.5,surface: −62.5 MJ kg⁻¹@se" --pt "42.2,-9.4,geostationary: −9.4 MJ kg⁻¹@nw" --xlabel "r / 10⁶ m" --ylabel "φ / MJ kg⁻¹" --label "φ = −GM/r"
:::

The gradient of the \(\phi\)–\(r\) graph is \(d\phi/dr = +GM/r^2\), the field strength. So the field strength is minus the potential gradient, with the direction pointing towards decreasing potential: \(g = -\dfrac{d\phi}{dr}\). Steep slope near the planet means strong field. (The units agree: \(\mathrm{MJ\,kg^{-1}}\) per \(10^{6}\,\mathrm{m}\) is \(\mathrm{N\,kg^{-1}}\).)

A surface that joins points of equal potential is an **equipotential**. Round a point mass the equipotentials are spheres, and the field lines cross them at right angles. Moving a mass along an equipotential needs no work, because \(\Delta\phi = 0\).

The work done in moving a mass \(m\) between two points is **mass times the change in potential**. This is the general version of \(mg\Delta h\):

:::formula Change in gravitational potential energy
\[\Delta E_\text{P} = m\,\Delta\phi\]
\(\Delta\phi\): the potential at the final point minus the potential at the starting point (\(\mathrm{J\,kg^{-1}}\)). If the mass moves to a higher potential (further out), \(\Delta\phi > 0\) and the mass gains energy.
:::

Near the surface, \(\phi(R+h) - \phi(R) = GM\left(\dfrac{1}{R} - \dfrac{1}{R+h}\right) = \dfrac{GMh}{R(R+h)} \approx \dfrac{GM}{R^2}h = gh\) for \(h \ll R\), which is the familiar \(mg\Delta h\) once you multiply by \(m\).

:::eg Calculate the gravitational potential at the surface of the Earth and at the geostationary radius \(4.22 \times 10^{7}\,\mathrm{m}\). Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\) and \(R = 6.37 \times 10^{6}\,\mathrm{m}\).
At the surface: \(\phi = -\dfrac{GM}{R} = -\dfrac{3.98 \times 10^{14}}{6.37 \times 10^{6}}\) [C1] \(= -6.25 \times 10^{7}\,\mathrm{J\,kg^{-1}}\). [A1]

At the geostationary radius: \(\phi = -\dfrac{3.98 \times 10^{14}}{4.22 \times 10^{7}} = -9.43 \times 10^{6}\,\mathrm{J\,kg^{-1}}\). [A1]

Both are negative, and the second is closer to zero, the value at infinity.
:::

:::warn Potential is a scalar
Field strength is a vector, so the fields of two bodies add as vectors and can cancel. Potential is a **scalar**: to find the potential at a point near two masses, add the two numbers, with their signs. The potential from a body is always negative, so the total can never cancel to zero, however far apart the bodies are.
:::

## Gravitational potential energy

The potential energy of a mass \(m\) in the field is its mass times the potential.

:::def Gravitational potential energy
The work done in bringing two point masses from infinite separation to their positions. For masses \(M\) and \(m\) a distance \(r\) apart, \(E_\text{P} = -\dfrac{GMm}{r}\).
:::

:::formula Gravitational potential energy of two point masses
\[E_\text{P} = m\phi = -\frac{GMm}{r}\]
\(E_\text{P}\): gravitational potential energy (J) · \(M, m\): the two masses (kg) · \(r\): distance between their centres (m). It is **negative**, with zero at infinite separation, and it increases (becomes less negative) as the masses move apart.
:::

The equation \(E_\text{P} = mgh\) is only valid for small heights near the surface, where \(g\) is constant. The equation \(E_\text{P} = -GMm/r\) always works, but it gives energies with the zero at infinity, so only *changes* in \(E_\text{P}\) are measurable.

:::eg A satellite of mass 1000 kg is lifted from the surface of the Earth to the height of the space station, 408 km. Calculate the increase in its gravitational potential energy using the potential, and compare it with \(mg\Delta h\). Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\).
\[\Delta E_\text{P} = GMm\left(\frac{1}{R} - \frac{1}{r}\right) = 3.98 \times 10^{14} \times 1000 \times \left(\frac{1}{6.37 \times 10^{6}} - \frac{1}{6.778 \times 10^{6}}\right)\] [C1]
\[\Delta E_\text{P} = 3.76 \times 10^{9}\,\mathrm{J}\] [A1]
The approximation gives \(mg\Delta h = 1000 \times 9.81 \times 4.08 \times 10^{5} = 4.00 \times 10^{9}\,\mathrm{J}\), about 6% too large, because \(g\) is smaller at the top than at the bottom. [B1]
:::

A satellite in orbit has both kinetic and potential energy. For a circular orbit, the equation of motion gives a neat result:

:::formula Energies of a satellite in a circular orbit
\[E_\text{K} = \frac{GMm}{2r} \qquad E_\text{P} = -\frac{GMm}{r} \qquad E_\text{total} = E_\text{K} + E_\text{P} = -\frac{GMm}{2r}\]
Derived from \(\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}\), which gives \(mv^2 = \dfrac{GMm}{r}\) and so \(E_\text{K} = \tfrac12mv^2 = \dfrac{GMm}{2r}\). Notice \(E_\text{K} = -\tfrac12E_\text{P}\), and the total energy is negative: the satellite is bound to the Earth.
:::

As a satellite moves to a larger orbit, \(E_\text{K}\) **decreases** (it moves more slowly) while \(E_\text{P}\) increases by twice as much, so the total energy increases: you must supply energy to raise an orbit, even though the satellite ends up slower.

:::eg A satellite of mass 500 kg is moved from rest on the surface of the Earth to a geostationary orbit. Calculate the energy needed, ignoring the satellite's kinetic energy at the surface due to the Earth's rotation. Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\).
Increase in potential energy:
\[\begin{aligned} \Delta E_\text{P} &= GMm\left(\frac{1}{R} - \frac{1}{r}\right) \\ &= 3.98 \times 10^{14} \times 500 \times \left(\frac{1}{6.37 \times 10^{6}} - \frac{1}{4.22 \times 10^{7}}\right) \end{aligned}\] [C1]
\[\Delta E_\text{P} = 2.65 \times 10^{10}\,\mathrm{J}\] [A1]

In orbit the satellite also has kinetic energy: \(E_\text{K} = \dfrac{GMm}{2r} = 2.36 \times 10^{9}\,\mathrm{J}\). [C1]

Total energy to supply: \(2.65 \times 10^{10} + 2.36 \times 10^{9} = 2.89 \times 10^{10}\,\mathrm{J}\). [A1]

The surface kinetic energy from the Earth's rotation is about \(5 \times 10^{7}\,\mathrm{J}\), only 0.2% of this, so ignoring it is a good approximation.
:::

:::eg Calculate the minimum speed with which a projectile must leave the surface of the Earth to escape from the Earth's gravitational field. (This idea is beyond the syllabus outcomes, but it is a standard application of potential energy.)
To escape, the mass must reach infinity, where \(E_\text{P} = 0\). The least energy is needed if it arrives there with no kinetic energy, so its total energy at infinity is zero. Energy is conserved, so at the surface \(E_\text{K} + E_\text{P} = 0\):
\[\tfrac12mv^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad v = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{2 \times 3.98 \times 10^{14}}{6.37 \times 10^{6}}} = 1.12 \times 10^{4}\,\mathrm{m\,s^{-1}}\]
The mass \(m\) cancelled, so the escape speed is the same for a grain of sand and a spacecraft. Energy is a scalar, so the direction of launch does not matter either (apart from atmosphere and obstacles). This is 11.2 km per second.
:::

:::board
AQA writes the gravitational potential as \(V_\text{grav} = -GM/r\) and gives \(g = -\Delta V/\Delta r\) explicitly; Edexcel IAL and OCR use the same results with their own symbols. The content is the same as in Cambridge.
:::

:::eg Spot the error: calculate the gravitational force on a satellite of mass 1000 kg when it is 600 km above the surface of the Earth. Use \(M = 5.97 \times 10^{24}\,\mathrm{kg}\) and \(R = 6.37 \times 10^{6}\,\mathrm{m}\).
A student wrote this answer.

Line 1: \(F = \dfrac{GMm}{r^2}\)
Line 2: \(F = \dfrac{6.67 \times 10^{-11} \times 5.97 \times 10^{24} \times 1000}{\left(6.0 \times 10^{5}\right)^2} = 1.1 \times 10^{6}\,\mathrm{N}\)

Line 1 is correct. [C1] **Line 2 is wrong: the student used the height above the surface as \(r\). The distance in Newton's law is measured from the centre of the Earth, so \(r = R + h\). The answer mark is lost.** [A0]

Correct working: \(r = 6.37 \times 10^{6} + 6.0 \times 10^{5} = 6.97 \times 10^{6}\,\mathrm{m}\), so \(F = \dfrac{6.67 \times 10^{-11} \times 5.97 \times 10^{24} \times 1000}{\left(6.97 \times 10^{6}\right)^2} = 8.2 \times 10^{3}\,\mathrm{N}\). [A1]

Check: a force of 1.1 MN would be more than 100 times the satellite's weight at the surface (9.8 kN), although it is further from the Earth. The force must be a little less than 9.8 kN.
:::

:::try Start easy, finish at exam standard
Q: Define gravitational field strength, and state its unit.
A: The gravitational force per unit mass acting on a small test mass at a point, \(g = F/m\). The unit is \(\mathrm{N\,kg^{-1}}\) (equal to \(\mathrm{m\,s^{-2}}\)).
Q: The distance between two small masses is tripled. By what factor does the force between them change?
A: \(F \propto 1/r^2\), so it falls by a factor of \(3^2 = 9\).
Q: The Moon has mass \(7.35 \times 10^{22}\,\mathrm{kg}\) and radius \(1.74 \times 10^{6}\,\mathrm{m}\). Find the field strength at its surface.
A: \(g = \dfrac{GM}{R^2} = \dfrac{6.67 \times 10^{-11} \times 7.35 \times 10^{22}}{\left(1.74 \times 10^{6}\right)^2} = 1.62\,\mathrm{N\,kg^{-1}}\), about one sixth of the Earth's.
Q: Jupiter has mass \(1.90 \times 10^{27}\,\mathrm{kg}\) and radius \(6.99 \times 10^{7}\,\mathrm{m}\). Find the field strength at its cloud tops.
A: \(g = \dfrac{6.67 \times 10^{-11} \times 1.90 \times 10^{27}}{\left(6.99 \times 10^{7}\right)^2} = 25.9\,\mathrm{N\,kg^{-1}}\), about 2.6 times the Earth's.
Q: A satellite orbits the Earth at radius \(7.2 \times 10^{6}\,\mathrm{m}\). Find its orbital speed. Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\).
A: \(v = \sqrt{GM/r} = \sqrt{3.98 \times 10^{14}/7.2 \times 10^{6}} = 7.4 \times 10^{3}\,\mathrm{m\,s^{-1}}\).
Q: The Earth orbits the Sun at \(1.50 \times 10^{11}\,\mathrm{m}\) with a period of 365.25 days. Calculate the mass of the Sun.
A: \(T = 365.25 \times 86400 = 3.156 \times 10^{7}\,\mathrm{s}\), so \(M = \dfrac{4\pi^2r^3}{GT^2} = \dfrac{4\pi^2 \times (1.50 \times 10^{11})^3}{6.67 \times 10^{-11} \times (3.156 \times 10^{7})^2} = 2.01 \times 10^{30}\,\mathrm{kg}\).
Q: Explain why a satellite in a geostationary orbit must be above the Equator.
A: The centre of its orbit must be the centre of the Earth, because gravity provides the centripetal force. Only an orbit in the equatorial plane stays over one point of the surface as the Earth turns; any other orbit would swing north and south of that point.
Q: State the value of the gravitational potential at infinity, and explain why the potential at the surface of a planet is negative.
A: It is zero at infinity. Gravity is attractive, so the field does work as a mass moves in from infinity, and the mass has less energy than at infinity: the potential is negative.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the gravitational potential at a point in a gravitational field.
A: The work done per unit mass [B1] in bringing a small test mass from infinity to that point. [B1]
Q: [2 marks] ★ Explain why the gravitational potential near a planet is negative.
A: The potential is defined as zero at infinity. [B1] The gravitational force is attractive, so the field does work as the mass moves in from infinity (or energy has to be supplied to move it back to infinity), so the energy and potential are lower than zero. [B1]
Q: [2 marks] ★ A point mass \(M\) produces a gravitational field. Derive an expression for the gravitational field strength \(g\) at distance \(r\) from it.
A: By Newton's law of gravitation, the force on a small mass \(m\) is \(F = GMm/r^2\). [M1] The field strength is the force per unit mass, \(g = F/m = GM/r^2\). [A1]
Q: [3 marks] ★★ A satellite orbits the Earth at a height of 350 km above the surface. Calculate the gravitational field strength at this height. The mass of the Earth is \(5.97 \times 10^{24}\,\mathrm{kg}\) and its radius is \(6.37 \times 10^{6}\,\mathrm{m}\).
A: \(r = 6.37 \times 10^{6} + 3.50 \times 10^{5} = 6.72 \times 10^{6}\,\mathrm{m}\) [C1] \(g = \dfrac{GM}{r^2} = \dfrac{6.67 \times 10^{-11} \times 5.97 \times 10^{24}}{\left(6.72 \times 10^{6}\right)^2}\) [C1] \(= 8.82\,\mathrm{N\,kg^{-1}}\). [A1]
Q: [4 marks] ★★ Phobos orbits Mars in a circle of radius \(9.38 \times 10^{6}\,\mathrm{m}\). The mass of Mars is \(6.42 \times 10^{23}\,\mathrm{kg}\). Calculate the orbital period of Phobos in hours.
A: The gravitational force provides the centripetal force, \(\dfrac{GMm}{r^2} = mr\omega^2\). [C1] With \(\omega = 2\pi/T\), \(T^2 = \dfrac{4\pi^2r^3}{GM}\). [C1] \(T^2 = \dfrac{4\pi^2 \times \left(9.38 \times 10^{6}\right)^3}{6.67 \times 10^{-11} \times 6.42 \times 10^{23}}\) so \(T = 2.76 \times 10^{4}\,\mathrm{s}\). [A1] \(T = 2.76 \times 10^{4}/3600 = 7.66\) hours. [A1]
Q: [6 marks] ★★ (a) State three conditions that a satellite must satisfy to be in a geostationary orbit. (b) Show that the radius of a geostationary orbit about the Earth is about \(4.2 \times 10^{7}\,\mathrm{m}\). Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\) for the Earth.
A: (a) Any three of: orbit period of 24 hours; moving from west to east; orbit in the plane of the Equator (directly above the Equator). [B1] [B1] [B1] (b) \(GM/r^2 = r\omega^2\), so \(r^3 = GMT^2/4\pi^2\), with \(T = 8.64 \times 10^{4}\,\mathrm{s}\). [C1] \(r^3 = \dfrac{3.98 \times 10^{14} \times \left(8.64 \times 10^{4}\right)^2}{4\pi^2}\) [C1] \(= 7.53 \times 10^{22}\,\mathrm{m^3}\), so \(r = 4.2 \times 10^{7}\,\mathrm{m}\). [A1]
Q: [6 marks] ★★★ A satellite of mass 1200 kg moves from a circular orbit of radius \(7.0 \times 10^{6}\,\mathrm{m}\) to a circular orbit of radius \(1.40 \times 10^{7}\,\mathrm{m}\) about the Earth. Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\). (a) Show that the kinetic energy of a satellite in a circular orbit is \(GMm/2r\). (b) Calculate the increase in the total energy of the satellite. (c) State and explain what happens to the kinetic energy of the satellite.
H: Write the total energy as \(E_\text{K} + E_\text{P}\). It simplifies to \(-GMm/2r\).
H: The total energy increases because the satellite has been given energy by its rocket engines.
A: (a) Gravity provides the centripetal force: \(\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}\), so \(mv^2 = \dfrac{GMm}{r}\). [M1] \(E_\text{K} = \tfrac12mv^2 = \dfrac{GMm}{2r}\). [A1] (b) \(E_\text{total} = E_\text{K} + E_\text{P} = \dfrac{GMm}{2r} - \dfrac{GMm}{r} = -\dfrac{GMm}{2r}\). [B1] Initially \(-\dfrac{3.98 \times 10^{14} \times 1200}{2 \times 7.0 \times 10^{6}} = -3.41 \times 10^{10}\,\mathrm{J}\) and finally \(-1.71 \times 10^{10}\,\mathrm{J}\). [C1] The increase is \(1.71 \times 10^{10}\,\mathrm{J}\). [A1] (c) The kinetic energy decreases (from \(3.41 \times 10^{10}\,\mathrm{J}\) to \(1.71 \times 10^{10}\,\mathrm{J}\)), because the orbital speed \(v = \sqrt{GM/r}\) is smaller in the larger orbit. [B1]
Q: [5 marks] ★★★ At some point on the line between the Earth and the Moon, the resultant gravitational field strength is zero. The distance between their centres is \(3.84 \times 10^{8}\,\mathrm{m}\). The mass of the Earth is \(5.97 \times 10^{24}\,\mathrm{kg}\) and the mass of the Moon is \(7.35 \times 10^{22}\,\mathrm{kg}\). Calculate the distance of this point from the centre of the Earth.
H: Let the distance from the Earth be \(x\), so the distance from the Moon is \(d - x\). The two field strengths must be equal in size.
H: Take the square root of both sides to avoid a quadratic equation.
A: Between the two bodies the fields point in opposite directions, so the resultant is zero when their sizes are equal. [B1] \(\dfrac{GM_\text{E}}{x^2} = \dfrac{GM_\text{M}}{(d-x)^2}\) [C1] so \(\dfrac{d - x}{x} = \sqrt{\dfrac{M_\text{M}}{M_\text{E}}} = 0.111\) [M1] giving \(x = \dfrac{d}{1.111}\) [A1] \(= 3.46 \times 10^{8}\,\mathrm{m}\) from the centre of the Earth. [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A satellite of mass 800 kg moves in a circular orbit of radius \(6.70 \times 10^{6}\,\mathrm{m}\) round the Earth. Atmospheric drag removes \(5.0 \times 10^{8}\,\mathrm{J}\) of its total energy and the orbit stays circular. (a) Show that the total energy of a satellite in a circular orbit is \(-GMm/2r\). (b) Explain why the satellite's speed increases although it has lost energy. (c) Calculate the new orbital radius and the change in speed. Use \(GM = 3.98 \times 10^{14}\,\mathrm{m^3\,s^{-2}}\).
H: For (b), the total energy is \(-GMm/2r\), so a more negative total energy means a smaller \(r\). What does the orbital speed formula say about a smaller \(r\)?
H: For (c), first find the total energy before, subtract the loss, and then find \(r\) from the new total energy.
A: (a) \(E_\text{K} = \dfrac{GMm}{2r}\) (from \(GMm/r^2 = mv^2/r\)) [M1] and \(E_\text{P} = -\dfrac{GMm}{r}\), so the sum is \(-\dfrac{GMm}{2r}\). [A1] (b) The total energy has become more negative, so \(r\) decreases. [B1] The speed \(v = \sqrt{GM/r}\) is larger in a smaller orbit, so the satellite speeds up: it falls to a lower orbit and gains kinetic energy at the expense of potential energy. [B1] (c) Initially \(E = -\dfrac{3.98 \times 10^{14} \times 800}{2 \times 6.70 \times 10^{6}} = -2.38 \times 10^{10}\,\mathrm{J}\), and after the loss \(E = -2.43 \times 10^{10}\,\mathrm{J}\). [C1] The new radius is \(r = \dfrac{GMm}{2|E|} = 6.56 \times 10^{6}\,\mathrm{m}\), a drop of 138 km. [A1] The speed rises from \(7.71 \times 10^{3}\) to \(7.79 \times 10^{3}\,\mathrm{m\,s^{-1}}\), an increase of \(81\,\mathrm{m\,s^{-1}}\). [A1]
Q: [6 marks] ★★★ Two identical stars, each of mass \(1.99 \times 10^{30}\,\mathrm{kg}\) (the mass of the Sun), orbit their common centre in circles. The distance between them is \(3.0 \times 10^{11}\,\mathrm{m}\). (a) Show that each star moves with speed \(v = \sqrt{GM/2d}\), where \(M\) is the mass of one star and \(d\) is their separation. (b) Calculate the period of the orbit, in years.
H: Each star orbits the midpoint, so the radius of each circle is \(d/2\), but the force between them depends on the full separation \(d\).
H: The period is the circumference of the circle divided by the speed.
A: (a) The gravitational force on each star provides its centripetal force: \(\dfrac{GM^2}{d^2} = \dfrac{Mv^2}{d/2}\). [M1] The radius of each orbit is \(d/2\), not \(d\). [M1] So \(v^2 = \dfrac{GM}{2d}\) and \(v = \sqrt{GM/2d}\). [A1] (b) \(v = \sqrt{\dfrac{6.67 \times 10^{-11} \times 1.99 \times 10^{30}}{2 \times 3.0 \times 10^{11}}} = 1.49 \times 10^{4}\,\mathrm{m\,s^{-1}}\) and \(T = \dfrac{2\pi(d/2)}{v} = \dfrac{\pi d}{v}\) [C1] \(= 6.3 \times 10^{7}\,\mathrm{s}\), [A1] which is \(6.3 \times 10^{7}/3.156 \times 10^{7} = 2.0\) years. [A1]
:::

:::quiz
? What do the field lines of a planet look like?
+ Straight lines pointing radially inwards, closer together near the surface
- Straight lines pointing radially outwards
- Parallel lines of equal spacing everywhere
- Closed loops round the planet
> Gravity is attractive, so the lines point inwards, and the field is stronger where the lines are closer. Parallel equally spaced lines describe a uniform field, which is only a good approximation over a small region.
? The distance between the centres of two masses is doubled. What happens to the gravitational force between them?
+ It falls to one quarter.
- It falls to one half.
- It falls to one eighth.
- It doubles.
> The force is inversely proportional to the square of the distance, so \((1/2)^2 = 1/4\). One half would be an inverse (not inverse-square) law.
? At the surface of a planet of radius \(R\) the field strength is \(g_0\). What is the field strength at a height \(R\) above the surface?
+ \(g_0/4\)
- \(g_0/2\)
- \(g_0/9\)
- \(0\)
> The distance from the centre is \(2R\), so \(g = GM/(2R)^2 = g_0/4\). Using the height \(R\) as the distance would give \(g_0\) again, and \(g_0/9\) is the value at a height \(2R\).
? Astronauts in the space station appear weightless. What is the main reason?
+ They and the station are in free fall around the Earth.
- The Earth's gravity is zero at that height.
- They are beyond the pull of the Earth's gravity.
- The Moon's gravity cancels the Earth's.
> The field strength is still about 88% of the surface value. The astronauts and the station accelerate towards the Earth at the same rate, so there is no contact force between them.
? Why is the gravitational potential of a planet negative?
+ Gravity is attractive and the potential is defined to be zero at infinity.
- The planet has a negative mass.
- The force is always directed downwards.
- Potential is the negative of the field strength.
> A mass loses energy as it falls in from infinity, so its potential energy is below zero. The planet's mass is positive, and the sign of the potential has nothing to do with the direction of the force.
? A satellite moves from a low circular orbit to a higher one. What happens to its kinetic energy and total energy?
+ Kinetic energy decreases and total energy increases.
- Both decrease.
- Kinetic energy increases and total energy decreases.
- Both increase.
> The orbital speed \(\sqrt{GM/r}\) is smaller at larger \(r\), so \(E_\text{K}\) decreases. The total energy \(-GMm/2r\) becomes less negative, so it increases: energy had to be supplied.
? Which satellite is in a geostationary orbit?
+ One in the Equator's plane, moving west to east, with a period of 24 hours
- One over the poles with a period of 24 hours
- One in the Equator's plane, moving east to west, with a period of 12 hours
- One moving west to east with a period of 24 hours, in a plane tilted at 45° to the Equator
> All conditions are needed. A tilted orbit with a 24 hour period traces a figure of eight over the ground, and a polar orbit moves over every part of the Earth in turn.
? The distance between two masses is doubled. What happens to the gravitational potential energy \(E_\text{P} = -GMm/r\) of the pair?
+ It becomes half as negative (it increases).
- It doubles (it becomes more negative).
- It becomes a quarter as negative.
- It stays the same.
> \(E_\text{P} \propto 1/r\), so doubling \(r\) halves its magnitude, and because the value is negative it increases towards zero. A quarter would be the result for the force, which goes as \(1/r^2\).
:::

:::checklist What you can now do
- [ ] I can define a gravitational field and gravitational field strength, and draw field lines for a radial and a uniform field.
- [ ] I can use Newton's law of gravitation, with \(r\) measured from the centre, and treat a uniform sphere as a point mass.
- [ ] I can derive \(g = GM/r^2\) and use it, and explain why \(g\) is nearly constant near the surface.
- [ ] I can analyse a circular orbit by equating the gravitational force to the centripetal force, and derive and use \(T^2 \propto r^3\).
- [ ] I can state and explain the conditions for a geostationary orbit and calculate its radius.
- [ ] I can define gravitational potential and use \(\phi = -GM/r\), and explain why it is negative.
- [ ] I can use \(E_\text{P} = -GMm/r\), calculate the energy to change orbit, and use \(E_\text{K} = GMm/2r\).
:::

:::recap
- Gravitational field: a region where a mass feels a force. Field strength \(g = F/m\), in \(\mathrm{N\,kg^{-1}}\), directed towards the mass. Field lines point towards the planet, closer together where the field is stronger; they are parallel and equally spaced near the surface (uniform field).
- Newton's law: \(F = Gm_1m_2/r^2\), always attractive, an inverse-square law, with \(r\) measured between the centres. A uniform sphere acts as a point mass at its centre.
- \(g = GM/r^2\) (derived by dividing \(F\) by \(m\)). Near the surface \(g\) is nearly constant because a small height change barely changes \(r\).
- Circular orbit: gravity provides the centripetal force, \(v = \sqrt{GM/r}\), \(T^2 = 4\pi^2r^3/GM\). The satellite's mass does not matter; a bigger orbit means a slower speed and a longer period.
- Geostationary: period 24 h, west to east, directly above the Equator, so it stays over one point. \(r = 4.22 \times 10^{7}\,\mathrm{m}\), height \(3.6 \times 10^{4}\,\mathrm{km}\).
- Gravitational potential: work done per unit mass in bringing a small mass from infinity. \(\phi = -GM/r\), negative, zero at infinity, a scalar. \(g = -d\phi/dr\).
- \(E_\text{P} = -GMm/r\); \(\Delta E_\text{P} = m\Delta\phi\). In a circular orbit \(E_\text{K} = GMm/2r\) and \(E_\text{total} = -GMm/2r\).
- Use \(r = R + h\). Astronauts are in free fall, not beyond gravity. \(E_\text{P} = mgh\) only for small heights.
:::

:::links
- explore: [Gravity and Orbits](https://phet.colorado.edu/en/simulations/gravity-and-orbits) · PhET · change the masses and distances and see the orbits and the force vectors
- explore: [Gravity Force Lab: Basics](https://phet.colorado.edu/en/simulations/gravity-force-lab-basics) · PhET · see how the force changes with mass and distance
- explore: [My Solar System](https://phet.colorado.edu/en/simulations/my-solar-system) · PhET · build a system of bodies and watch it evolve

Links checked 13 October 2026.
:::
Next: [Temperature](#phys.temperature)
