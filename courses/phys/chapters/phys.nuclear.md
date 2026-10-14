@chapter phys.nuclear
@title Nuclear physics
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary Mass–energy equivalence, nuclear equations, mass defect and binding energy, the binding energy per nucleon curve and why fusion and fission release energy, and the random, exponential nature of radioactive decay with activity, decay constant and half-life.

:::why
Nuclear reactions release roughly a million times more energy per kilogram of fuel than burning, which is why a tiny reactor core can power a city and why the Sun shines for billions of years. The same physics tells hospitals how long a radioactive tracer lasts and tells archaeologists how old a piece of charcoal is. This chapter links the energy of the nucleus to its mass, and then describes how fast unstable nuclei decay.
:::

**Before you start**, you need nuclide notation, decay equations and the atomic mass unit from [Particle physics](#phys.particles), exponential decay from [Capacitance](#phys.capacitance), logarithms from [Logarithms and exponentials](#math.p3.logs), and the electronvolt from [Quantum physics](#phys.quantum).

:::try Warm-up
Q: Complete the equation \(^{14}_{\;6}\mathrm{C} \rightarrow {}^{14}_{\;7}\mathrm{N} + \dots\) (from [Particle physics](#phys.particles))
A: A \(\beta^-\) decay: \(^{14}_{\;6}\mathrm{C} \rightarrow {}^{14}_{\;7}\mathrm{N} + {}^{\;0}_{-1}\mathrm{e} + \bar{\nu}\). Nucleon number 14 = 14 + 0 + 0 and charge 6 = 7 − 1 + 0.
Q: A capacitor discharges through a resistor with a time constant of 2.0 s. What fraction of its charge remains after 4.0 s? (from [Capacitance](#phys.capacitance))
A: \(Q/Q_0 = e^{-t/RC} = e^{-4.0/2.0} = e^{-2} = 0.14\).
Q: Convert 2.5 MeV into joules. (from [Quantum physics](#phys.quantum))
A: \(2.5 \times 10^{6} \times 1.60 \times 10^{-19} = 4.0 \times 10^{-13}\,\mathrm{J}\).
:::

## Mass and energy are equivalent

In 1905 Einstein showed that mass and energy are two forms of one conserved quantity. A body of mass \(m\) has an energy equivalent to \(mc^2\), and when its energy changes, its mass changes too.

:::formula Mass–energy equivalence
\[E = mc^2 \qquad\qquad \Delta E = c^2\,\Delta m\]
\(E\): energy (J) · \(m\): mass (kg) · \(c\): speed of light, \(3.00 \times 10^{8}\,\mathrm{m\,s^{-1}}\) · \(\Delta m\): the change in mass (kg). Because \(c^2\) is so large, a small mass change is a large energy change.
:::

In a chemical reaction the mass change is far too small to measure. Burning 1 kg of coal releases about \(3.0 \times 10^{7}\,\mathrm{J}\), a change of mass of \(3.0 \times 10^{7}/(3.00 \times 10^{8})^2 = 3.3 \times 10^{-10}\,\mathrm{kg}\). In a nuclear reaction the change is large enough to detect: it is the reason nuclear energy is so concentrated.

Mass and energy are conserved together. In a nuclear reaction the total rest mass of the products is slightly less than that of the reactants, and the difference appears as kinetic energy of the products (and as gamma photons). Mass and energy are not separate things that happen to be swapped: the mass really is the energy.

:::eg Calculate the energy equivalent of 1 u in joules and in MeV, using the data-sheet values.
\(E = mc^2 = 1.66 \times 10^{-27} \times (3.00 \times 10^{8})^2\) [C1] \(= 1.494 \times 10^{-10}\,\mathrm{J}\). [A1]

In MeV: \(\dfrac{1.494 \times 10^{-10}}{1.60 \times 10^{-13}} = 934\,\mathrm{MeV}\), since \(1\,\mathrm{MeV} = 1.60 \times 10^{-13}\,\mathrm{J}\). [A1]

Many tables quote 931.5 MeV, which comes from more precise constants. Use the data-sheet values unless the question gives a conversion. This gives the useful rule **1 u is equivalent to 934 MeV**, which turns a mass defect in u straight into an energy in MeV.
:::

:::eg What energy is equivalent to a mass of 1.0 g? The Sun radiates \(3.8 \times 10^{26}\,\mathrm{W}\): at what rate does its mass decrease?
\(E = mc^2 = 1.0 \times 10^{-3} \times (3.00 \times 10^{8})^2 = 9.0 \times 10^{13}\,\mathrm{J}\). A 100 W lamp would use that much energy in about \(9 \times 10^{11}\) seconds, roughly \(3 \times 10^{4}\) years.

The Sun loses \(3.8 \times 10^{26}\) J every second, so \(\dfrac{\Delta m}{\Delta t} = \dfrac{P}{c^2} = \dfrac{3.8 \times 10^{26}}{(3.00 \times 10^{8})^2} = 4.2 \times 10^{9}\,\mathrm{kg\,s^{-1}}\). The Sun is so massive that this loss is negligible on a human timescale.
:::

## Nuclear equations

A nuclear equation shows the nuclei and particles in a reaction. Two quantities are conserved, and you check them at every step.

:::key Balancing a nuclear equation
The **nucleon number** \(A\) (the top number) adds up to the same total on both sides.
The **proton number** \(Z\) (the bottom number, which gives the charge) adds up to the same total on both sides.
:::

Rutherford produced the first artificial change of one element into another in 1919 by firing alpha particles at nitrogen. The reaction is the syllabus example:

\[{}^{14}_{\;7}\mathrm{N} + {}^{4}_{2}\mathrm{He} \rightarrow {}^{17}_{\;8}\mathrm{O} + {}^{1}_{1}\mathrm{H}\]

Check it: nucleon number \(14 + 4 = 18 = 17 + 1\), and proton number \(7 + 2 = 9 = 8 + 1\). The nucleus \({}^{1}_{1}\mathrm{H}\) is a proton.

:::eg Uranium-235 absorbs a neutron and splits: \({}^{235}_{\;92}\mathrm{U} + {}^{1}_{0}\mathrm{n} \rightarrow {}^{141}_{\;56}\mathrm{Ba} + {}^{92}_{36}\mathrm{Kr} + x\,{}^{1}_{0}\mathrm{n}\). Find \(x\).
Nucleon number: \(235 + 1 = 236 = 141 + 92 + x \times 1\), so \(x = 3\). [M1] [A1]

Proton number check: \(92 + 0 = 92 = 56 + 36 + 0\), so the equation balances. The three neutrons released can go on to split further nuclei: this is how a chain reaction can start.
:::

:::eg Complete the equation \({}^{238}_{\;92}\mathrm{U} \rightarrow {}^{234}_{\;90}\mathrm{Th} + \dots\) and name the particle.
Nucleon number: \(238 - 234 = 4\). Proton number: \(92 - 90 = 2\). [B1]

The particle is \({}^{4}_{2}\mathrm{He}\), an alpha particle. [B1]
:::

## Mass defect and binding energy

Weigh a helium-4 nucleus very carefully. It contains 2 protons and 2 neutrons, and it is **lighter** than the four separate nucleons. The missing mass is the **mass defect**.

:::def Mass defect
The difference between the total mass of the separate nucleons and the mass of the nucleus.
:::

The missing mass has become energy. When nucleons come together to form a nucleus, energy is released, and the same energy must be supplied to pull the nucleus apart again.

:::def Binding energy
The minimum energy required to separate a nucleus into its constituent protons and neutrons. (Equivalently, the energy released when the nucleus is formed from separate nucleons.)
:::

:::formula Mass defect and binding energy
\[\Delta m = Zm_p + (A - Z)m_n - m_\text{nucleus} \qquad E_B = c^2\,\Delta m \qquad \text{binding energy per nucleon} = \frac{E_B}{A}\]
\(Z\): proton number · \(A\): nucleon number · \(m_p, m_n\): masses of a proton and a neutron · \(m_\text{nucleus}\): mass of the nucleus alone. If \(\Delta m\) is in u, then \(E_B\) in MeV is \(\Delta m \times 934\).
:::

The **binding energy per nucleon** tells you how tightly bound the nucleons are on average. A larger value means a more stable nucleus: more energy per nucleon would be needed to break it up.

:::eg The masses are: proton 1.007 276 u, neutron 1.008 665 u, helium-4 nucleus 4.001 506 u. Calculate the mass defect, the binding energy and the binding energy per nucleon of helium-4.
Separate nucleons: \(2 \times 1.007\,276 + 2 \times 1.008\,665 = 4.031\,882\,\mathrm{u}\).
\(\Delta m = 4.031\,882 - 4.001\,506 = 0.030\,376\,\mathrm{u}\). [C1] \(= 0.030\,376 \times 1.66 \times 10^{-27} = 5.04 \times 10^{-29}\,\mathrm{kg}\). [A1]

\(E_B = c^2\,\Delta m = 5.04 \times 10^{-29} \times (3.00 \times 10^{8})^2\) [C1] \(= 4.54 \times 10^{-12}\,\mathrm{J} = 28.4\,\mathrm{MeV}\). [A1]

Binding energy per nucleon \(= \dfrac{28.4}{4} = 7.1\,\mathrm{MeV}\). [A1]
:::

:::warn Nuclear mass or atomic mass
The formula needs the mass of the **nucleus**. Tables often give the mass of the whole atom, which includes the electrons. If you use an atomic mass for one item and a nuclear mass for another, the electrons are not cancelled, and the answer is wrong by the mass of the electrons: for helium that is two electrons, \(2 \times 5.49 \times 10^{-4}\,\mathrm{u} = 1.1 \times 10^{-3}\,\mathrm{u}\), about 1 MeV. Use nuclear masses throughout unless the question tells you otherwise.
:::

## Binding energy per nucleon against nucleon number

If you plot the binding energy per nucleon for every nucleus, a pattern emerges. The graph is one of the most important in the course.

:::html
<figure class="fig wide"><svg viewBox="45 0 610 298" role="img" aria-label="Graph of binding energy per nucleon in MeV against nucleon number A from 0 to 250. The curve rises steeply for the lightest nuclei, with a spike at helium-4 at about 7.1 MeV, then rises more slowly to a broad maximum of about 8.8 MeV at iron-56, and falls slowly to about 7.6 MeV for uranium-235. A rightward arrow labelled fusion lies under the rising part of the curve and a leftward arrow labelled fission lies under the falling part."><path class="ax" d="M80 250V20" marker-end="url(#ah)"/><path class="ax" d="M80 250H645" marker-end="url(#ah)"/><path class="ln" d="M190 250V255M300 250V255M410 250V255M520 250V255M630 250V255M80 206H75M80 162H75M80 118H75M80 74H75M80 30H75"/><text class="ts tc" x="190" y="268">50</text><text class="ts tc" x="300" y="268">100</text><text class="ts tc" x="410" y="268">150</text><text class="ts tc" x="520" y="268">200</text><text class="ts tc" x="630" y="268">250</text><text class="ts te" x="71" y="209">2</text><text class="ts te" x="71" y="165">4</text><text class="ts te" x="71" y="121">6</text><text class="ts te" x="71" y="77">8</text><text class="ts te" x="71" y="33">10</text><text class="tl" x="88" y="16">binding energy per nucleon / MeV</text><text class="tl te" x="645" y="290">nucleon number A</text><path class="c1" d="M82.2 250L84.4 225.6L88.8 94.5L93.2 132.7L106.4 81C109.3 78.8 112.3 76.1 115.2 74.4C121.1 71.2 126.9 69.8 132.8 68.3C144.5 65.2 156.3 63.8 168 61.9C179.7 60 191.5 56.6 203.2 56.6C223.7 56.6 244.3 57.3 264.8 58.2C291.2 59.3 317.6 60.9 344 62.8C366 64.4 388 66.8 410 68.5C452.5 71.7 495.1 73.3 537.6 76.9C557.4 78.5 577.2 81 597 83"/><circle class="fa" cx="84.4" cy="225.6" r="4"/><circle class="fa" cx="88.8" cy="94.5" r="4"/><circle class="fa" cx="106.4" cy="81" r="4"/><circle class="fa" cx="203.2" cy="56.6" r="4"/><circle class="fa" cx="597" cy="83" r="4"/><path class="ln-m thin" d="M88.8 90V68"/><text class="tl" x="84" y="62">⁴He</text><text class="tl" x="92" y="229">²H</text><text class="tl" x="112" y="104">¹²C</text><text class="tl tc" x="203" y="42">⁵⁶Fe (8.8 MeV)</text><text class="tl tc" x="597" y="70">²³⁵U</text><path class="c2" d="M124 180H196" marker-end="url(#ah2-phys)"/><path class="c2" d="M597 180H352" marker-end="url(#ah2-phys)"/><text class="tl tc" x="160" y="172">fusion</text><text class="tl tc" x="475" y="172">fission</text></svg><figcaption>Binding energy per nucleon rises steeply for light nuclei (with a spike at helium-4), peaks near iron-56 and falls slowly for heavy nuclei. Fusion moves light nuclei towards the peak and fission moves a heavy nucleus towards it, so both increase the binding energy per nucleon.</figcaption></figure>
:::

:::key The shape of the curve
- The curve rises steeply from hydrogen-2 (about 1.1 MeV per nucleon), with a **spike at helium-4** (about 7.1 MeV): this nucleus is unusually stable.
- It reaches a **broad maximum of about 8.8 MeV near \(A = 56\)** (iron and nickel). These are the most stable nuclei.
- It then falls slowly, to about **7.6 MeV for uranium-235**.
- A nucleus with a larger binding energy per nucleon is more stable.
:::

The curve falls on the right because a heavy nucleus has many protons, whose electrostatic repulsion works against the short-range attraction that binds the nucleons. It is low on the left because a light nucleus has most of its nucleons at the surface, where they have few neighbours to be attracted to.

## Fusion and fission

:::def Nuclear fusion
The joining of two light nuclei to form a heavier nucleus.
:::

:::def Nuclear fission
The splitting of a heavy nucleus into two lighter nuclei of similar mass (and neutrons).
:::

Look again at the curve. Fusion moves nuclei from the steep left side up towards the peak, and fission moves a nucleus from the right side towards the peak. Either way, the products have a **higher binding energy per nucleon** than the reactants.

:::key Why fusion and fission release energy
The products are more tightly bound, so the total binding energy rises. Energy equal to this rise is released, and since the energy comes from mass, the total rest mass of the products is **less** than that of the reactants:
\[E_\text{released} = c^2\,\Delta m \qquad \Delta m = \text{(mass of reactants)} - \text{(mass of products)}\]
\(\Delta m\) is positive when energy is released. The energy appears as kinetic energy of the products and as gamma photons.
:::

- **Fusion** needs the nuclei to get very close, but they are both positive and repel each other. They must therefore have a huge kinetic energy, which means a very high temperature (millions of kelvin) and high pressure. These conditions exist in the core of a star. In the Sun, hydrogen nuclei fuse into helium.
- **Fission** can begin when a heavy nucleus such as uranium-235 absorbs a neutron and becomes unstable. It splits into two medium-sized nuclei and releases two or three neutrons. If these neutrons go on to split other nuclei, a **chain reaction** results. A nuclear reactor controls the number of neutrons so that the chain reaction runs steadily.

:::eg Using the curve, estimate the energy released when one nucleus of uranium-235 splits into two fragments with a mean binding energy per nucleon of 8.5 MeV. (The binding energy per nucleon of uranium-235 is 7.6 MeV.)
Binding energy per nucleon increases by \(8.5 - 7.6 = 0.9\,\mathrm{MeV}\). [C1]

This applies to all 235 nucleons, so the energy released is \(235 \times 0.9\) [C1] \(\approx 2 \times 10^{2}\,\mathrm{MeV}\). [A1]

Real fission releases about 200 MeV per nucleus, which is consistent. Compare 200 MeV with the few electronvolts of a chemical reaction: that is why nuclear fuel is so concentrated.
:::

:::eg A deuterium nucleus \(({}^{2}_{1}\mathrm{H})\) and a tritium nucleus \(({}^{3}_{1}\mathrm{H})\) fuse: \({}^{2}_{1}\mathrm{H} + {}^{3}_{1}\mathrm{H} \rightarrow {}^{4}_{2}\mathrm{He} + {}^{1}_{0}\mathrm{n}\). Calculate the energy released, using these nuclear masses: deuterium 2.013 553 u, tritium 3.015 501 u, helium-4 4.001 506 u, neutron 1.008 665 u.
Mass of reactants: \(2.013\,553 + 3.015\,501 = 5.029\,054\,\mathrm{u}\). Mass of products: \(4.001\,506 + 1.008\,665 = 5.010\,171\,\mathrm{u}\).
\(\Delta m = 5.029\,054 - 5.010\,171 = 0.018\,883\,\mathrm{u}\). [C1]

\(E = c^2\,\Delta m = 0.018\,883 \times 1.66 \times 10^{-27} \times (3.00 \times 10^{8})^2\) [C1] \(= 2.8 \times 10^{-12}\,\mathrm{J}\). [A1] In MeV that is \(0.018\,883 \times 934 = 17.6\,\mathrm{MeV}\). [A1]

This reaction is the main candidate for fusion power plants, because it works at a lower temperature than other fusion reactions.
:::

:::eg Each fission of uranium-235 releases about 200 MeV. The molar mass of uranium-235 is \(0.235\,\mathrm{kg\,mol^{-1}}\). Compare the energy from fissioning 1.0 kg of it with burning 1.0 kg of coal, which releases \(3.0 \times 10^{7}\,\mathrm{J}\).
Number of nuclei in 1.0 kg: \(\dfrac{1.0}{0.235} \times 6.02 \times 10^{23} = 2.56 \times 10^{24}\). [C1]

Energy per fission: \(200 \times 1.60 \times 10^{-13} = 3.2 \times 10^{-11}\,\mathrm{J}\), so the energy from 1.0 kg is \(2.56 \times 10^{24} \times 3.2 \times 10^{-11} = 8.2 \times 10^{13}\,\mathrm{J}\). [C1]

Ratio to coal: \(\dfrac{8.2 \times 10^{13}}{3.0 \times 10^{7}} = 2.7 \times 10^{6}\). [A1]

One kilogram of uranium-235 gives about 2.7 million times as much energy as one kilogram of coal.
:::

## Random and spontaneous decay

Some nuclei are unstable and change into other nuclei by emitting alpha, beta or gamma radiation, which you met in [Particle physics](#phys.particles). Two features of this decay are essential.

:::def Spontaneous
Not affected by external factors such as temperature or pressure. A nucleus decays without any outside prompt, and heating, cooling or squeezing the sample does not change the rate.
:::

:::def Random
It cannot be predicted when a particular nucleus will decay, but each nucleus has a constant probability of decay per unit time.
:::

Like tossing a coin, you cannot say which toss will give heads, but you can say that about half of a large number will. In the same way, you cannot say which nucleus in a sample will decay next, but you can predict very accurately how many of a large number will decay in a given time.

### Evidence from count-rate fluctuations

A Geiger–Müller (G-M) tube detects each radioactive particle that enters it as a click, and a counter totals the clicks. Count them for equal time intervals, such as 10 s, from a source of long half-life. The counts **fluctuate**: they might read 52, 61, 47, 55, 49, 58. If decay were regular, like a clock, every count would be the same. The variation shows that decays happen at unpredictable moments, which is the random nature of decay.

For random events, a count of \(N\) typically varies by about \(\sqrt{N}\), so a count of 400 varies by about 20, which is 5%. To measure a count rate to 1% you need about 10 000 counts.

A G-M tube also counts radiation that does not come from your source, such as cosmic rays and radioactive rocks. This is the **background count rate**. It is measured with the source removed (and far away), and subtracted from every reading to give the **corrected count rate**.

:::eg A G-M tube records 180 counts in one minute with a source in place. With the source removed it records 75 counts in 5.0 minutes. Calculate the corrected count rate.
Background rate: \(75/5.0 = 15\) counts per minute. [C1]

Corrected count rate: \(180 - 15 = 165\) counts per minute. [A1]

Count the background for longer than the source, as here, because the background is small and its random fluctuation matters more.
:::

## Activity, decay constant and half-life

:::def Activity
The number of nuclei that decay per unit time. It is measured in becquerel: \(1\,\mathrm{Bq} = 1\) decay per second.
:::

:::def Decay constant
The probability that an individual nucleus will decay per unit time. Its symbol is \(\lambda\), and its unit is \(\mathrm{s^{-1}}\) (or \(\mathrm{h^{-1}}\), \(\mathrm{year^{-1}}\), whatever time unit you use).
:::

If each of \(N\) undecayed nuclei has a probability \(\lambda\) of decaying every second, then about \(\lambda N\) nuclei decay each second. That is the activity.

:::formula Activity and the decay constant
\[A = \lambda N\]
\(A\): activity (Bq) · \(\lambda\): decay constant (\(\mathrm{s^{-1}}\)) · \(N\): number of undecayed nuclei in the sample. A sample with twice as many nuclei has twice the activity. The activity is also the rate at which \(N\) falls: \(A = -\Delta N/\Delta t\).
:::

The activity is not the same as the count rate. A detector sees only the fraction of the decays whose radiation reaches it, so the count rate is proportional to the activity but smaller.

### Why the decay is exponential

The activity is \(\lambda N\), so as nuclei decay and \(N\) falls, the activity falls in proportion. The rate of decay is always proportional to what is left: this is the pattern that gives an exponential decay, as in the [discharge of a capacitor](#phys.capacitance) (see also [Logarithms and exponentials](#math.p3.logs)).

:::formula Exponential decay
\[x = x_0\,e^{-\lambda t}\]
\(x\) can be the number of undecayed nuclei \(N\), the activity \(A\), or the corrected count rate \(C\). \(x_0\) is its value at \(t = 0\), \(\lambda\) is the decay constant and \(t\) is the time. All three decay with the same \(\lambda\).
:::

:::def Half-life
The time taken for the number of undecayed nuclei (or the activity) of an isotope to fall to half of its initial value.
:::

The half-life is **constant** for a given isotope: it takes the same time to fall from 800 Bq to 400 Bq as from 100 Bq to 50 Bq. The activity, the number of nuclei and the corrected count rate all have the same half-life. After \(n\) half-lives, the fraction left is \(\left(\tfrac12\right)^n\).

| Time | 0 | \(t_{1/2}\) | \(2t_{1/2}\) | \(3t_{1/2}\) | \(4t_{1/2}\) |
|---|---|---|---|---|---|
| Fraction left | 1 | 1/2 | 1/4 | 1/8 | 1/16 |

:::proof Why \(\lambda = 0.693/t_{1/2}\)
At \(t = t_{1/2}\), \(N = \tfrac12 N_0\). Put this into \(N = N_0 e^{-\lambda t}\).
\(\tfrac12 N_0 = N_0 e^{-\lambda t_{1/2}}\), so \(\tfrac12 = e^{-\lambda t_{1/2}}\).
Take natural logarithms: \(\ln\tfrac12 = -\lambda t_{1/2}\), and \(\ln\tfrac12 = -\ln 2\).
So \(\ln 2 = \lambda t_{1/2}\), and since \(\ln 2 = 0.693\), \(\lambda = \dfrac{0.693}{t_{1/2}}\).
:::

:::formula Half-life and decay constant
\[\lambda = \frac{0.693}{t_{1/2}} \qquad\text{equivalently}\qquad t_{1/2} = \frac{0.693}{\lambda}\]
A large decay constant means a short half-life. Keep the units consistent: if \(t_{1/2}\) is in hours, \(\lambda\) is in \(\mathrm{h^{-1}}\). Convert to seconds when you need an activity in becquerel.
:::

:::plot The activity of a sample of iodine-131 (half-life 8.0 days). Equal fractions fall away in equal times: the activity halves every 8.0 days.
--f "40*exp(-0.0866*x)+0*sqrt(33-x)" --x 0 38 --y 0 50 --pt "8,20,20 MBq@ne" --pt "16,10,10 MBq@ne" --pt "24,5,5 MBq@ne" --xlabel "t / days" --ylabel "A / MBq" --xstep 8
:::

The decay curve is useful, but a straight line is easier to analyse. Take natural logarithms of \(A = A_0 e^{-\lambda t}\):
\[\ln A = \ln A_0 - \lambda t\]
A graph of \(\ln A\) (or \(\ln N\), or \(\ln C\)) against \(t\) is a **straight line with gradient \(-\lambda\)** and \(y\)-intercept \(\ln A_0\). This is the standard way to find a decay constant from data (see [Planning, analysis and evaluation](#phys.planning)).

:::plot The same data plotted as ln A against t is a straight line. The gradient is −λ and the y-intercept is ln A₀.
--f "3.689-0.0866*x+0*sqrt(32-x)" --x 0 37 --y 0 5.2 --pt "0,3.689,ln A₀ = 3.69@ne" --xlabel "t / days" --ylabel "ln (A / MBq)" --xstep 8
:::

Now try it. A grid of nuclei decays at random. Run it several times with a small number of nuclei, then a large number, and notice how closely the steps follow the smooth curve.

:::html
<div class="widget" data-w="phys-halflife" data-n0="400" data-thalf="5"></div>
:::

:::lab Measuring a half-life with a G-M tube
:::steps
1. With no source nearby, count for 10 minutes to find the background count rate. Remove all other sources from the bench.
2. Place a source with a half-life of a few minutes (a protactinium generator, if your school has one) at a fixed distance from the G-M tube. Handle it only with tongs and return it to its box straight afterwards.
3. Record the counts in each successive interval, for example every 30 s, for at least three half-lives. Keep the distance and the geometry exactly the same throughout.
4. Subtract the background rate from each count rate to find the corrected count rate \(C\).
5. Plot \(\ln C\) against \(t\) and draw the best-fit line. The gradient is \(-\lambda\), so \(t_{1/2} = 0.693/\lambda\). Alternatively read off the times for \(C\) to halve on a graph of \(C\) against \(t\) and take the mean.
:::
:::

To make this accurate, count for long intervals (each reading should hold thousands of counts if possible), repeat the whole run, and measure the background carefully. If the source has a very long half-life, an experiment like this cannot work, because the count rate does not change in the time you have. Teachers then use a dice model: each die is a nucleus, and each throw removes the sixes, so the number left falls by about one sixth each throw.

:::eg Iodine-131 has a half-life of 8.0 days. Find the fraction left after 20 days, and the time for the activity to fall to 5.0% of its initial value.
\(\lambda = \dfrac{0.693}{8.0} = 0.0866\,\mathrm{day^{-1}}\). [C1]

Fraction after 20 days: \(\dfrac{A}{A_0} = e^{-\lambda t} = e^{-0.0866 \times 20} = 0.177\). [A1]

For 5.0%: \(0.050 = e^{-\lambda t}\), so \(\lambda t = \ln\dfrac{1}{0.050} = 3.00\). [C1] \(t = \dfrac{3.00}{0.0866} = 35\,\mathrm{days}\). [A1]

Check: 35 days is 4.3 half-lives, and \(\left(\tfrac12\right)^{4.3} = 0.05\).
:::

:::eg A sample contains \(1.0\,\mu\mathrm{g}\) of americium-241, the isotope in smoke detectors. Its half-life is 432 years and its molar mass is \(0.241\,\mathrm{kg\,mol^{-1}}\). Calculate its activity. (1 year \(= 3.15 \times 10^{7}\,\mathrm{s}\).)
Number of nuclei: \(N = \dfrac{1.0 \times 10^{-9}\,\mathrm{kg}}{0.241\,\mathrm{kg\,mol^{-1}}} \times 6.02 \times 10^{23} = 2.5 \times 10^{15}\). [C1]

\(\lambda = \dfrac{0.693}{432 \times 3.15 \times 10^{7}} = 5.1 \times 10^{-11}\,\mathrm{s^{-1}}\). [C1]

\(A = \lambda N = 5.1 \times 10^{-11} \times 2.5 \times 10^{15}\) [C1] \(= 1.3 \times 10^{5}\,\mathrm{Bq}\). [A1]

A tiny mass has a large activity because the nuclei decay quickly on the scale of a second, even though the half-life is hundreds of years. The long half-life means the detector keeps working for decades.
:::

:::eg A fossil sample of charcoal has an activity of 0.12 Bq per gram of carbon, from carbon-14. Living wood has 0.23 Bq per gram. The half-life of carbon-14 is 5730 years. Estimate the age of the charcoal.
While a tree lives it takes in carbon-14 from the air, so its activity per gram stays at 0.23 Bq. Once it dies the activity decays.

\(\dfrac{A}{A_0} = e^{-\lambda t}\), so \(t = \dfrac{1}{\lambda}\ln\dfrac{A_0}{A}\) with \(\lambda = \dfrac{0.693}{5730}\). [C1]

\(t = \dfrac{5730}{0.693} \times \ln\dfrac{0.23}{0.12}\) [C1] \(= 8268 \times 0.651 = 5.4 \times 10^{3}\,\mathrm{years}\). [A1]

This works for samples up to about 50 000 years old. After that, the remaining activity is too small to separate from the background.
:::

:::warn Common errors with half-life
After **two** half-lives a quarter is left, not nothing, and not half. The half-life of the **activity** is the same as the half-life of the number of nuclei, because \(A = \lambda N\). Count rate is not activity. And \(\lambda = 0.693/t_{1/2}\), never \(0.693 \times t_{1/2}\): check that a long half-life gives a small \(\lambda\).
:::

:::board
AQA's specification includes the nuclear radius formula, \(R = R_0 A^{1/3}\). The Cambridge 9702 syllabus does not, so you will not be asked to use it; everything you need for Cambridge is in this chapter.
:::

:::eg Spot the error: the half-life of a nuclide is 12 hours. Calculate its decay constant.
A student wrote this answer.

Line 1: \(t_{1/2} = 12\,\mathrm{h}\)
Line 2: \(\lambda = 0.693 \times t_{1/2} = 0.693 \times 12 = 8.3\,\mathrm{h^{-1}}\)

Line 1 is correct. **Line 2 is wrong: the relation is \(\lambda = 0.693/t_{1/2}\), not a product.** The method mark is lost, and so is the answer. [M0] [A0]

Correct working: \(\lambda = \dfrac{0.693}{12} = 0.058\,\mathrm{h^{-1}}\). [A1]

Check: a decay constant of \(8.3\,\mathrm{h^{-1}}\) would mean that each nucleus has a probability of more than 8 of decaying per hour, which is impossible for a half-life of 12 hours. A long half-life must give a small \(\lambda\).
:::

:::try Start easy, finish at exam standard
Q: Calculate the energy equivalent of a mass of 2.0 mg.
A: \(E = mc^2 = 2.0 \times 10^{-6} \times (3.00 \times 10^{8})^2 = 1.8 \times 10^{11}\,\mathrm{J}\).
Q: A reaction has a mass defect of 0.0100 u. How much energy is released, in MeV?
A: \(0.0100 \times 934 = 9.34\,\mathrm{MeV}\), using \(1\,\mathrm{u} \equiv 934\,\mathrm{MeV}\).
Q: Complete \({}^{226}_{\;88}\mathrm{Ra} \rightarrow {}^{222}_{\;86}\mathrm{Rn} + \dots\)
A: Nucleon number \(226 - 222 = 4\) and proton number \(88 - 86 = 2\), so the particle is \({}^{4}_{2}\mathrm{He}\), an alpha particle.
Q: The nucleus of iron-56 has a binding energy of 492 MeV. Find its binding energy per nucleon, and state whether it is more or less stable than uranium-235, which has 7.6 MeV per nucleon.
A: \(492/56 = 8.8\,\mathrm{MeV}\). It is larger than 7.6 MeV, so iron-56 is more stable.
Q: Explain why fusion reactions need a very high temperature.
A: The nuclei are both positively charged, so they repel each other. To get close enough to fuse they need very high kinetic energy, which means a very high temperature.
Q: A count rate of 150 counts per minute is recorded with a source, and the background is 30 counts per minute. What is the corrected count rate?
A: \(150 - 30 = 120\) counts per minute.
Q: The decay constant of a nuclide is \(2.0 \times 10^{-4}\,\mathrm{s^{-1}}\). Calculate its half-life.
A: \(t_{1/2} = \dfrac{0.693}{\lambda} = \dfrac{0.693}{2.0 \times 10^{-4}} = 3.5 \times 10^{3}\,\mathrm{s}\), about 58 minutes.
Q: The activity of a source falls from 640 Bq to 40 Bq in 20 minutes. Find its half-life.
A: \(640 \rightarrow 320 \rightarrow 160 \rightarrow 80 \rightarrow 40\) is 4 half-lives, so \(t_{1/2} = 20/4 = 5.0\) minutes.
Q: A sample contains \(3.0 \times 10^{12}\) undecayed nuclei with decay constant \(4.0 \times 10^{-6}\,\mathrm{s^{-1}}\). Calculate its activity.
A: \(A = \lambda N = 4.0 \times 10^{-6} \times 3.0 \times 10^{12} = 1.2 \times 10^{7}\,\mathrm{Bq}\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the binding energy of a nucleus.
A: The minimum energy required [B1] to separate a nucleus into its constituent protons and neutrons. [B1]
Q: [3 marks] ★ Sketch a graph of binding energy per nucleon against nucleon number. Label the region where fusion occurs and the region where fission occurs.
A: The curve rises steeply for light nuclei to a broad maximum of about 8.8 MeV at \(A \approx 56\) (iron). [B1] It then falls slowly, to about 7.6 MeV at \(A = 235\). [B1] Fusion is labelled on the rising part (light nuclei, left of the peak) and fission on the falling part (heavy nuclei, right of the peak). [B1]
Q: [4 marks] ★★ Two deuterium nuclei fuse: \({}^{2}_{1}\mathrm{H} + {}^{2}_{1}\mathrm{H} \rightarrow {}^{3}_{2}\mathrm{He} + {}^{1}_{0}\mathrm{n}\). The nuclear masses are: deuterium 2.013 553 u, helium-3 3.014 932 u, neutron 1.008 665 u. (a) Calculate the mass difference in kg. (b) Calculate the energy released, in J.
A: (a) The reactants have mass \(4.027\,106\,\mathrm{u}\) and the products \(4.023\,597\,\mathrm{u}\), so \(\Delta m = 0.003\,509\,\mathrm{u}\) [C1] \(= 0.003\,509 \times 1.66 \times 10^{-27} = 5.8 \times 10^{-30}\,\mathrm{kg}\). [A1] (b) \(E = c^2\,\Delta m = 5.8 \times 10^{-30} \times (3.00 \times 10^{8})^2\) [C1] \(= 5.2 \times 10^{-13}\,\mathrm{J}\). [A1]
Q: [3 marks] ★★ Use the graph of binding energy per nucleon against nucleon number to explain why energy is released when a nucleus of uranium-235 undergoes fission.
A: Uranium-235 has a binding energy per nucleon of about 7.6 MeV, which is lower than that of the two fragments (about 8.5 MeV). [B1] So the total binding energy increases and the fragments are more tightly bound. [B1] The total mass of the products is less than that of the original nucleus, and this mass difference is released as energy (\(E = c^2\,\Delta m\)), mainly as kinetic energy of the fragments. [B1]
Q: [3 marks] ★★ A G-M tube and counter record these counts in successive 10 s intervals from a source of very long half-life: 52, 61, 47, 55, 49, 58. (a) Explain how the readings show that radioactive decay is random. (b) State how you would find the corrected count rate.
A: (a) The counts differ from one interval to the next although nothing in the experiment changes. [B1] If decays occurred at regular intervals the counts would be the same; the variation shows that the times of the decays are unpredictable. [B1] (b) Measure the background count rate with the source removed and subtract it from the count rate with the source. [B1]
Q: [4 marks] ★★ A sample contains \(1.0\,\mu\mathrm{g}\) of cobalt-60, of molar mass \(0.060\,\mathrm{kg\,mol^{-1}}\) and half-life 5.3 years. (a) Calculate the number of undecayed nuclei. (b) Calculate the activity. (1 year \(= 3.15 \times 10^{7}\,\mathrm{s}\).)
A: (a) \(N = \dfrac{1.0 \times 10^{-9}}{0.060} \times 6.02 \times 10^{23}\) [C1] \(= 1.0 \times 10^{16}\). [A1] (b) \(\lambda = \dfrac{0.693}{5.3 \times 3.15 \times 10^{7}} = 4.2 \times 10^{-9}\,\mathrm{s^{-1}}\), and \(A = \lambda N\) [C1] \(= 4.2 \times 10^{7}\,\mathrm{Bq}\). [A1]
Q: [6 marks] ★★★ The count rate from a radioactive source is measured with a G-M tube. The background is 24 counts per minute. The total count rates at times 0, 1.0, 2.0, 3.0, 4.0 and 5.0 minutes are 544, 417, 321, 248, 194 and 152 counts per minute. (a) Explain why a graph of the natural logarithm of the corrected count rate against time is a straight line. (b) Use the first and last readings to find the decay constant. (c) Find the half-life.
H: Subtract the background from every reading before taking logarithms.
H: The gradient of the line is \(-\lambda\); use \(\ln C = \ln C_0 - \lambda t\) between two points.
A: (a) The corrected rate follows \(C = C_0 e^{-\lambda t}\), [B1] so \(\ln C = \ln C_0 - \lambda t\), which has the form \(y = mx + c\) with gradient \(-\lambda\). [B1] (b) Corrected rates: \(544 - 24 = 520\) and \(152 - 24 = 128\) counts per minute. [B1] \(\lambda = \dfrac{\ln(520/128)}{5.0}\) [C1] \(= 0.28\,\mathrm{min^{-1}}\). [A1] (c) \(t_{1/2} = \dfrac{0.693}{0.28} = 2.5\) minutes. [A1]
Q: [5 marks] ★★★ Technetium-99m, used as a tracer in hospitals, has a half-life of 6.0 hours. A dose is prepared with an activity of 350 MBq, and the patient is injected 9.0 hours later. (a) Calculate the activity of the dose when it is injected. (b) Suggest one reason why a short half-life suits a medical tracer, and one reason why it should not be much shorter than a few hours.
H: First find \(\lambda\) in \(\mathrm{h^{-1}}\), then use \(A = A_0 e^{-\lambda t}\).
A: (a) \(\lambda = \dfrac{0.693}{6.0} = 0.1155\,\mathrm{h^{-1}}\) [C1] and \(A = 350\,e^{-0.1155 \times 9.0}\) [C1] \(= 1.2 \times 10^{2}\,\mathrm{MBq}\). [A1] (b) A short half-life means the activity, and so the dose of radiation to the patient, falls quickly after the scan, so little radioactive material is left in the body. [B1] A half-life of a few hours is still long enough to prepare, transport and inject the dose and to carry out the scan. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A sample contains two radioactive isotopes, X with a half-life of 2.0 hours and Y with a half-life of 10 hours. Each has an initial activity of 800 Bq. (a) State the total initial activity. (b) Calculate the total activity after 10 hours. (c) Calculate the total activity after 30 hours, and say which isotope accounts for almost all of it. (d) Explain why a graph of the natural logarithm of the total activity against time is not a straight line, and how the half-life of Y could be found from it.
H: Each isotope decays on its own, so add the activities at each time.
H: After 10 hours X has gone through 5 half-lives, and Y through 1.
A: (a) \(800 + 800 = 1600\,\mathrm{Bq}\). [B1] (b) X: \(800 \times (\tfrac12)^5 = 25\,\mathrm{Bq}\); Y: \(800 \times \tfrac12 = 400\,\mathrm{Bq}\); [C1] total \(425\,\mathrm{Bq}\). [A1] (c) X: \(800 \times (\tfrac12)^{15} = 0.02\,\mathrm{Bq}\); Y: \(800 \times (\tfrac12)^3 = 100\,\mathrm{Bq}\), so the total is about 100 Bq, almost all from Y. [A1] (d) The total is the sum of two exponentials, and the logarithm of a sum is not a straight line: the line is steep at first while X dominates, then becomes straight with a smaller gradient. [B1] At late times only Y contributes, so the gradient of that straight section is \(-\lambda_Y\), and \(t_{1/2} = 0.693/\lambda_Y\). [B1]
Q: [6 marks] ★★★ The binding energies per nucleon are: hydrogen-2, 1.11 MeV; hydrogen-3, 2.83 MeV; helium-4, 7.07 MeV; uranium-235, 7.6 MeV, with fission fragments of average 8.5 MeV. (a) Calculate the energy released when deuterium and tritium fuse to helium-4 and a neutron, using the binding energies. (b) Calculate the energy released per nucleon for this fusion reaction and for the fission of uranium-235, and compare them.
H: Total binding energy is the binding energy per nucleon multiplied by the number of nucleons. The neutron has no binding energy of its own.
A: (a) The energy released is the binding energy of the products minus that of the reactants. [B1] Helium-4: \(4 \times 7.07 = 28.28\,\mathrm{MeV}\); reactants: \(2 \times 1.11 + 3 \times 2.83 = 10.71\,\mathrm{MeV}\). [C1] Energy released \(= 28.28 - 10.71 = 17.6\,\mathrm{MeV}\). [A1] (b) Fusion: 5 nucleons take part, so \(17.57/5 = 3.5\,\mathrm{MeV}\) per nucleon. Fission: \(235 \times (8.5 - 7.6)/235 = 0.90\,\mathrm{MeV}\) per nucleon. [C1] Fusion releases about four times as much energy per nucleon as fission. [A1] Fusion is the more energetic process per kilogram of fuel, but it needs a far higher temperature. [B1]
:::

:::quiz
? What is the mass defect of a nucleus?
+ The difference between the total mass of the separate nucleons and the mass of the nucleus
- The mass of the neutrons in the nucleus
- The mass that is lost when the nucleus decays
- The difference in mass between a proton and a neutron
> The nucleus is lighter than its separate nucleons, and the missing mass is the binding energy converted into mass by \(E = mc^2\). It is a property of the nucleus, not of a decay.
? Which nuclei have the highest binding energy per nucleon?
+ Those near iron-56
- The lightest nuclei, such as hydrogen-2
- The heaviest nuclei, such as uranium-235
- Helium-4 only
> The curve peaks at about 8.8 MeV near \(A = 56\). Light nuclei and heavy nuclei have lower values, although helium-4 is a local spike.
? Why does nuclear fission release energy?
+ The fragments have a higher binding energy per nucleon than the original nucleus.
- The fragments have a lower binding energy per nucleon than the original nucleus.
- Mass is destroyed and the energy is lost as heat.
- The neutrons carry the energy of the original nucleus.
> Moving towards the peak of the curve means the products are more tightly bound, and the total mass drops by \(\Delta m\), released as \(c^2\,\Delta m\). Mass is not destroyed: it becomes energy.
? What does it mean to say that radioactive decay is random?
+ It is impossible to predict when a given nucleus will decay, but each has a constant probability per unit time.
- The rate of decay changes unpredictably with temperature.
- Different nuclei decay at different constant rates, chosen at random.
- Decay only occurs when nuclei are disturbed.
> Randomness is about which nucleus and when, with a fixed probability \(\lambda\) per unit time. Temperature has no effect on decay, which is spontaneous.
? A radioactive sample has a half-life of 4.0 hours. What fraction of the original nuclei remains after 12 hours?
+ 1/8
- 1/3
- 1/4
- 0
> 12 hours is 3 half-lives, so the fraction is \((\tfrac12)^3 = 1/8\). "1/3" comes from dividing 12 by 4 and keeping the 3, and 1/4 is the fraction after only two half-lives. The nuclei never all vanish at a fixed time, so 0 is wrong.
? A graph of ln(activity) against time for a radioactive sample is a straight line. What does its gradient equal?
+ \(-\lambda\)
- \(\lambda\)
- \(-t_{1/2}\)
- \(\ln A_0\)
> From \(\ln A = \ln A_0 - \lambda t\), the gradient is minus the decay constant and the intercept is \(\ln A_0\). The gradient is negative because the activity falls.
? Which statement about activity and count rate is correct?
+ The count rate is proportional to the activity, because the detector intercepts only some of the radiation.
- They are always equal.
- The count rate is the number of nuclei in the sample.
- The activity depends on the detector used.
> The detector sees only a fraction of the decays, so its count rate is proportional to the activity but smaller. The activity is a property of the source, not of the detector.
? A nuclide has a decay constant \(\lambda\). Which expression gives its activity when \(N\) nuclei are present?
+ \(\lambda N\)
- \(N/\lambda\)
- \(\lambda/N\)
- \(\lambda N^2\)
> The probability per unit time that each nucleus decays is \(\lambda\), so \(N\) nuclei give \(\lambda N\) decays per unit time.
:::

:::checklist What you can now do
- [ ] I can use \(E = mc^2\) and \(\Delta E = c^2\,\Delta m\), and convert between u, kg, J and MeV.
- [ ] I can write and balance nuclear equations using nucleon number and proton number.
- [ ] I can define and use mass defect and binding energy, and calculate the binding energy per nucleon.
- [ ] I can sketch the binding energy per nucleon curve and describe its shape.
- [ ] I can define fusion and fission and use the curve to explain why each releases energy.
- [ ] I can calculate the energy released in a nuclear reaction from the masses of the nuclei.
- [ ] I can explain that decay is spontaneous and random, and use count-rate fluctuations as the evidence.
- [ ] I can define activity, decay constant and half-life, and use \(A = \lambda N\) and \(\lambda = 0.693/t_{1/2}\).
- [ ] I can sketch and use \(x = x_0 e^{-\lambda t}\) for \(N\), \(A\) and the corrected count rate, including a \(\ln\)-graph.
:::

:::recap
- \(E = mc^2\) and \(\Delta E = c^2\,\Delta m\). With the data-sheet constants, 1 u is equivalent to 1.494 × 10⁻¹⁰ J, or 934 MeV.
- Nuclear equations conserve nucleon number \(A\) and proton number \(Z\).
- Mass defect: total mass of separate nucleons minus mass of the nucleus. Binding energy: minimum energy to separate the nucleus into its nucleons, \(E_B = c^2\,\Delta m\). Use nuclear masses.
- The binding energy per nucleon curve rises steeply to a spike at helium-4, peaks at about 8.8 MeV near \(A = 56\), and falls to about 7.6 MeV for uranium-235. A higher value means a more stable nucleus.
- Fusion (light nuclei join) and fission (a heavy nucleus splits) both move towards the peak. The products have a higher binding energy per nucleon and a smaller total mass, and the mass difference is released as energy.
- Decay is spontaneous (not affected by temperature or pressure) and random (the time is unpredictable; constant probability \(\lambda\) per unit time). Count-rate fluctuations are the evidence. Subtract the background.
- \(A = \lambda N\). Activity is in Bq; \(\lambda\) is the probability of decay per unit time. Half-life: time for \(N\) or \(A\) to halve. \(\lambda = 0.693/t_{1/2}\).
- \(x = x_0 e^{-\lambda t}\) for \(N\), \(A\) or corrected count rate. After \(n\) half-lives \((1/2)^n\) is left. \(\ln x\) against \(t\) is a straight line with gradient \(-\lambda\).
:::

:::links
- explore: [Alpha Decay](https://phet.colorado.edu/en/simulations/alpha-decay) · PhET · watch single nuclei decay at random and see the half-life emerge
- explore: [Beta Decay](https://phet.colorado.edu/en/simulations/beta-decay) · PhET · a neutron turns into a proton, an electron and an antineutrino
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the nuclear physics questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Medical physics](#phys.medical)
