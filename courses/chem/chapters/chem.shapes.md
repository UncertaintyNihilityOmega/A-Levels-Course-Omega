@chapter chem.shapes
@title Shapes of molecules and intermolecular forces
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 6–8 hours
@summary How to predict the shape and bond angles of any molecule or ion by counting electron pairs, how to tell whether a molecule is polar, and how the forces between molecules (id–id, pd–pd and hydrogen bonding) explain boiling points and the strange behaviour of water.

:::why
Shape is the link between a formula and the real behaviour of a substance. Carbon dioxide and sulfur dioxide are both made of a central atom and two oxygen atoms, yet one is a non-polar gas that dissolves poorly and the other is a polar gas that causes acid rain. Water is a bent molecule, and that bend is why it is liquid at room temperature, why ice floats and why life exists at all. Drug molecules and enzymes work only when their shapes fit. This chapter gives you one simple rule, that electron pairs repel, and then uses it to predict shapes, polarity and boiling points.
:::

**Before you start**, you should be able to draw dot-and-cross diagrams, count lone pairs and work out electronegativity differences, all from [Chemical bonding](#chem.bonding), and know what an electron shell is from [Atomic structure](#chem.atoms).

:::try Warm-up
Q: How many outer electrons does a nitrogen atom have, and how many bonding pairs and lone pairs does it have in ammonia, \(\ce{NH3}\)? (from [Chemical bonding](#chem.bonding))
A: Five outer electrons (Group 15). In ammonia it has 3 bonding pairs (one to each H) and 1 lone pair: 3 × 2 + 2 = 8 electrons.
Q: The Pauling values are H 2.1 and Cl 3.0. Which atom in H–Cl carries the partial negative charge, and is the bond polar? (from [Chemical bonding](#chem.bonding))
A: Chlorine, the more electronegative atom, carries δ−. The difference is 0.9, so the bond is polar covalent.
Q: What angle do the four sp³ orbitals of carbon make with each other in methane? (from [Chemical bonding](#chem.bonding))
A: 109.5°, pointing to the corners of a tetrahedron.
:::

## Electron pairs repel

Every shape in this chapter comes from one idea. Electrons carry a negative charge, so the pairs of electrons in the outer shell of an atom repel one another. They move as far apart as they can, and the atoms attached to them go along for the ride.

:::analogy
Tie two balloons together by their necks and they point in opposite directions. Tie three and they spread out flat, like a three-bladed propeller. Tie four and they form a pyramid shape with a triangle base. The balloons are pushing against each other in the same way as electron pairs, and the shape they settle in is the one that keeps them as far apart as possible.
:::

Chemists call this **valence shell electron pair repulsion** theory, VSEPR for short (say "vesper"). To use it you need two words.

:::def Bonding pair and lone pair
A bonding pair is a pair of electrons shared between two atoms in a covalent bond. A lone pair is a pair of outer-shell electrons on one atom that is not involved in bonding.
:::

Count **regions of electron density** around the central atom: each lone pair is one region and each bond is one region. A **double or triple bond counts as one region only**, because all the electrons of a multiple bond lie along the same line between the same two nuclei and push on their neighbours together.

:::key The VSEPR rules
1. Electron pairs (regions of electron density) around a central atom repel each other and arrange themselves as far apart as possible.
2. A double or triple bond is **one** region.
3. Lone pairs repel more strongly than bonding pairs: lone pair–lone pair repulsion > lone pair–bonding pair repulsion > bonding pair–bonding pair repulsion.
4. The **shape** of a molecule is the arrangement of its atoms only. Lone pairs affect the shape but are not part of its name.
:::

Rule 3 has a reason. A bonding pair is held between two nuclei, so it is pulled into the gap between the atoms. A lone pair is attracted by one nucleus only, so it spreads out more and takes up more room around the central atom. It pushes harder on its neighbours and squeezes the bond angles together. In the tetrahedral family each lone pair closes the bond angle by about 2.5° from the ideal 109.5°.

## Counting the electron pairs

To predict a shape you first need the number of pairs around the central atom. You can count them from the formula without drawing a diagram.

:::steps
1. Find the central atom: the atom that the others are bonded to (in \(\ce{NH3}\) it is N, in \(\ce{SO2}\) it is S).
2. Write down its number of outer electrons, which is its group number for Groups 1 and 2, and the group number minus 10 for Groups 13 to 17.
3. Add 1 for each hydrogen or halogen atom attached (each shares one electron with the central atom). Add 0 for each oxygen atom, because oxygen completes its own octet by sharing two electrons from the central atom and brings nothing extra to the total.
4. Adjust for charge: add 1 for each negative charge on the ion and subtract 1 for each positive charge.
5. Divide the total by 2. This is the number of electron pairs (regions of electron density) around the central atom.
6. Count the atoms attached to the central atom. Each is a bonding region. The remaining pairs are **lone pairs**.
:::

If you have a displayed formula, there is a quicker check: regions = number of atoms attached + number of lone pairs on the central atom. Use it for molecules with triple bonds such as \(\ce{HCN}\), where the steps above do not apply.

:::eg Work out the number of electron pairs, bonding pairs and lone pairs around the central atom in (a) \(\ce{CO3^2-}\), (b) \(\ce{SO2}\), (c) \(\ce{NH4+}\), (d) \(\ce{H3O+}\).
(a) \(\ce{CO3^2-}\): carbon has 4 outer electrons. The three oxygen atoms add 0. The ion has a 2− charge, so add 2: total 6, which is 3 pairs. Three oxygen atoms are attached, so 3 bonding pairs and 0 lone pairs.

(b) \(\ce{SO2}\): sulfur has 6 outer electrons and the oxygen atoms add 0: total 6, which is 3 pairs. Two oxygen atoms are attached, so 2 bonding regions (one for each S=O) and 1 lone pair.

(c) \(\ce{NH4+}\): nitrogen has 5, the four hydrogen atoms add 4 and the 1+ charge subtracts 1: total 8, which is 4 pairs. Four atoms are attached, so 4 bonding pairs and 0 lone pairs.

(d) \(\ce{H3O+}\): oxygen has 6, three hydrogen atoms add 3 and the 1+ charge subtracts 1: total 8, which is 4 pairs. Three atoms are attached, so 3 bonding pairs and 1 lone pair.
:::

The number of pairs fixes the **arrangement** of the regions. The number of lone pairs then fixes the shape. We take the arrangements in order, from 2 pairs to 6.

## Two pairs: linear

Two regions are furthest apart when they point in opposite directions, 180° apart. The atoms lie in a straight line: the shape is **linear**.

Beryllium chloride, \(\ce{BeCl2}\), is a good example. Beryllium has 2 outer electrons and the two chlorine atoms add 2, so there are 4 electrons, 2 pairs, both bonding. The shape is linear and the Cl–Be–Cl angle is 180°. Note that beryllium has only 4 electrons around it: it does not complete an octet.

In carbon dioxide, \(\ce{O=C=O}\), carbon has two double bonds. Each double bond is one region, so there are 2 regions, 0 lone pairs and the shape is linear with an O–C–O angle of 180°. Ethyne, \(\ce{H-C#C-H}\), and hydrogen cyanide, \(\ce{H-C#N}\), are also linear around each carbon atom for the same reason: two regions.

## Three pairs: trigonal planar

Three regions are furthest apart when they lie in one plane, 120° apart. With no lone pair the shape is **trigonal planar**.

Boron trifluoride, \(\ce{BF3}\), has boron with 3 outer electrons and three fluorine atoms adding 3: total 6, 3 pairs, all bonding. The shape is trigonal planar and the F–B–F angle is 120°. Boron is another atom with fewer than 8 electrons (6) around it. The carbonate ion \(\ce{CO3^2-}\) and the nitrate ion \(\ce{NO3-}\) (N: 5 + 1 = 6, so 3 pairs) are also trigonal planar with 120° angles, and so is \(\ce{SO3}\) (sulfur 6, so 3 pairs).

Sulfur dioxide, \(\ce{SO2}\), also has three regions, but one is a lone pair. The two S=O regions and the lone pair are arranged in a triangle, but the **shape** is the arrangement of the atoms only, so the molecule is **non-linear** (bent). The lone pair repels the bonding regions more strongly, so the O–S–O angle is a little less than 120°.

## Four pairs: tetrahedral, pyramidal and non-linear

Four regions are furthest apart at the corners of a **tetrahedron**, 109.5° apart. This is the arrangement for the largest family of molecules, and the lone pairs change the shape.

:::formula Where does 109.5° come from?
A regular tetrahedron has its four corners at \((1,1,1)\), \((1,-1,-1)\), \((-1,1,-1)\) and \((-1,-1,1)\) from its centre. The angle between two of these directions satisfies \(\cos\theta = \dfrac{(1)(1)+(1)(-1)+(1)(-1)}{3} = -\dfrac{1}{3}\), so \(\theta = 109.47^{\circ}\), which is written 109.5°.
:::

**No lone pairs: tetrahedral.** In methane, \(\ce{CH4}\), carbon has 4 outer electrons and four hydrogen atoms add 4: total 8, 4 pairs, all bonding. The shape is **tetrahedral** with H–C–H angles of 109.5°. The same is true for any species with four bonding pairs and no lone pair: the ammonium ion \(\ce{NH4+}\), \(\ce{SiCl4}\), the tetrachloroaluminate ion \(\ce{AlCl4-}\) and the sulfate ion \(\ce{SO4^2-}\) are all tetrahedral with angles of 109.5°.

**One lone pair: pyramidal.** In ammonia, \(\ce{NH3}\), nitrogen has 5 electrons and the three hydrogen atoms add 3: total 8, 4 pairs, 3 bonding and 1 lone. The four pairs point to the corners of a tetrahedron, but only three corners carry an atom. The atoms form a pyramid with nitrogen at the top: the shape is **pyramidal**. The lone pair pushes the three N–H bonds together, so the H–N–H angle is 107°. The oxonium ion \(\ce{H3O+}\) (3 bonding pairs, 1 lone pair) is also pyramidal with an angle of about 107°, and so is phosphorus trichloride \(\ce{PCl3}\) (P: 5 + 3 = 8).

**Two lone pairs: non-linear.** In water, \(\ce{H2O}\), oxygen has 6 electrons and the two hydrogen atoms add 2: total 8, 4 pairs, 2 bonding and 2 lone. Two corners of the tetrahedron carry an atom and two carry a lone pair. The atoms form a V: the shape is **non-linear** (bent). The two lone pairs push harder still, and the H–O–H angle is 104.5°.

:::html
<figure class="fig"><svg viewBox="-11 21 644 187" role="img" aria-label="Drawings of carbon dioxide (linear, 180°), boron trifluoride (trigonal planar, 120°), methane (tetrahedral, 109.5°), ammonia (pyramidal, 107°) and water (non-linear, 104.5°)"><text class="tl tc" x="64" y="98.5">C</text><text class="tl tc" x="8" y="98.5">O</text><text class="tl tc" x="120" y="98.5">O</text><path class="ln thick" d="M55.5 92.5L16.5 92.5"/><path class="ln thick" d="M55.5 97.5L16.5 97.5"/><path class="ln thick" d="M72.5 92.5L111.5 92.5"/><path class="ln thick" d="M72.5 97.5L111.5 97.5"/><text class="tl tc ta" x="64" y="75">180°</text><text class="tl tc" x="192" y="98.5">B</text><text class="tl tc" x="192" y="46.5">F</text><path class="ln thick" d="M192 83.5L192 54.5"/><text class="tl tc" x="147" y="124.5">F</text><path class="ln thick" d="M183.5 99.9L155.5 116.1"/><text class="tl tc" x="237" y="124.5">F</text><path class="ln thick" d="M200.5 99.9L228.5 116.1"/><text class="tl tc ta" x="192" y="139">120°</text><text class="tl tc" x="320" y="98.5">C</text><text class="tl tc" x="320" y="46.5">H</text><path class="ln thick" d="M320 83.5L320 54.5"/><text class="tl tc" x="275" y="124.5">H</text><path class="ln thick" d="M311.5 99.9L283.5 116.1"/><text class="tl tc" x="361" y="130.5">H</text><path class="fi" d="M328.5 101.6L347 121.2L351.9 114.9Z"/><text class="tl tc" x="365.9" y="74.1">H</text><path class="ln dash thick" d="M328.5 90.5L357.4 75.1"/><text class="tl tc ta" x="314" y="139">109.5°</text><text class="tl tc" x="448" y="98.5">N</text><circle class="fi" cx="445" cy="79" r="1.7"/><circle class="fi" cx="451" cy="79" r="1.7"/><text class="tl tc" x="403.9" y="126.1">H</text><path class="ln thick" d="M439.5 100.3L412.4 117.2"/><text class="tl tc" x="486.6" y="133.3">H</text><path class="fi" d="M456.5 102.7L472.5 122.4L477.8 116.5Z"/><text class="tl tc" x="496.2" y="79">H</text><path class="ln dash thick" d="M456.5 91.6L487.7 79"/><text class="tl tc ta" x="446" y="139">107°</text><text class="tl tc" x="576" y="92.5">O</text><circle class="fi" cx="559" cy="73" r="1.7"/><circle class="fi" cx="565" cy="73" r="1.7"/><circle class="fi" cx="587" cy="73" r="1.7"/><circle class="fi" cx="593" cy="73" r="1.7"/><text class="tl tc" x="538" y="121.9">H</text><path class="ln thick" d="M567.5 95.6L546.5 111.8"/><text class="tl tc" x="614" y="121.9">H</text><path class="ln thick" d="M584.5 95.6L605.5 111.8"/><text class="tl tc ta" x="576" y="139">104.5°</text><text class="tl tc" x="64" y="172">CO₂</text><text class="tl tc ta" x="64" y="190">linear</text><text class="tl tc" x="192" y="172">BF₃</text><text class="tl tc ta" x="192" y="190">trigonal planar</text><text class="tl tc" x="320" y="172">CH₄</text><text class="tl tc ta" x="320" y="190">tetrahedral</text><text class="tl tc" x="448" y="172">NH₃</text><text class="tl tc ta" x="448" y="190">pyramidal</text><text class="tl tc" x="576" y="172">H₂O</text><text class="tl tc ta" x="576" y="190">non-linear</text></svg><figcaption>Shapes with two, three and four electron pairs. A plain line lies in the plane of the page, a filled wedge points towards you and a dashed line points away. Pairs of dots are lone pairs. The number under each drawing is its bond angle.</figcaption></figure>
:::

In drawings of three-dimensional shapes, a **plain line** is a bond in the plane of the paper, a **filled wedge** is a bond coming towards you and a **dashed line** is a bond going away from you. Examiners expect this convention when you draw a shape.

:::key The tetrahedral family
| Bonding pairs | Lone pairs | Shape | Bond angle | Example |
|---|---|---|---|---|
| 4 | 0 | tetrahedral | 109.5° | \(\ce{CH4}\), \(\ce{NH4+}\) |
| 3 | 1 | pyramidal | 107° | \(\ce{NH3}\), \(\ce{H3O+}\) |
| 2 | 2 | non-linear | 104.5° | \(\ce{H2O}\) |

All have 4 pairs of electrons in a tetrahedral arrangement. Each lone pair reduces the angle by about 2.5°: 109.5°, then 107°, then 104.5°.
:::

:::warn Do not name the shape after the pairs
Ammonia has four pairs in a tetrahedral arrangement, but its **shape** is pyramidal, because only the atoms are named. Writing "ammonia is tetrahedral" loses the mark. Water is non-linear, not "tetrahedral" and not "linear".
:::

## Five and six pairs

The third period and below can hold more than 8 electrons (see [Chemical bonding](#chem.bonding)), so molecules with five and six bonding pairs exist.

**Five pairs: trigonal bipyramidal.** Phosphorus pentafluoride, \(\ce{PF5}\), has P: 5 + 5 = 10 electrons, 5 pairs, all bonding. The most stable arrangement is a **trigonal bipyramid**: three fluorine atoms in a triangle around the middle of the molecule, at 120° to each other (the **equatorial** positions), and one fluorine above and one below (the **axial** positions). The axial bonds are at 90° to the equatorial ones and 180° to each other. A trigonal bipyramid therefore has two different bond angles, 120° and 90°. \(\ce{PCl5}\) has the same shape.

**Six pairs: octahedral.** Sulfur hexafluoride, \(\ce{SF6}\), has S: 6 + 6 = 12 electrons, 6 pairs, all bonding. Six regions are furthest apart pointing along three axes at right angles: one up, one down, one left, one right, one forwards, one back. The shape is **octahedral** (eight faces) and every F–S–F angle between neighbours is 90°.

:::html
<figure class="fig"><svg viewBox="19 26 613 200" role="img" aria-label="Phosphorus pentafluoride, trigonal bipyramidal, with angles of 180°, 120° and 90°, and sulfur hexafluoride, octahedral, with angles of 90° and 180°"><text class="tl tc" x="110" y="103.5">P</text><text class="tl tc" x="110" y="51.5">F</text><path class="ln thick" d="M110 88.5L110 59.5"/><text class="tl tc" x="110" y="155.5">F</text><path class="ln thick" d="M110 111.5L110 140.5"/><text class="tl tc" x="58" y="103.5">F</text><path class="ln thick" d="M101.5 100L66.5 100"/><text class="tl tc" x="155" y="129.5">F</text><path class="fi" d="M118.5 104.9L141.5 122.8L145.5 115.9Z"/><text class="tl tc" x="155" y="77.5">F</text><path class="ln dash thick" d="M118.5 95.1L146.5 78.9"/><text class="tl tc" x="104" y="190">PF₅</text><text class="tl tc ta" x="104" y="208">trigonal bipyramidal</text><text class="tl" x="185" y="66">180°: axial to axial</text><text class="tl" x="185" y="90">120°: equatorial pair</text><text class="tl" x="185" y="114">90°: axial–equatorial</text><text class="tl tc" x="420" y="103.5">S</text><text class="tl tc" x="420" y="51.5">F</text><path class="ln thick" d="M420 88.5L420 59.5"/><text class="tl tc" x="420" y="155.5">F</text><path class="ln thick" d="M420 111.5L420 140.5"/><text class="tl tc" x="368" y="103.5">F</text><path class="ln thick" d="M411.5 100L376.5 100"/><text class="tl tc" x="472" y="103.5">F</text><path class="ln thick" d="M428.5 100L463.5 100"/><text class="tl tc" x="385.8" y="134.3">F</text><path class="fi" d="M411.5 107.7L394.6 117.5L400 123.4Z"/><text class="tl tc" x="454.2" y="72.7">F</text><path class="ln dash thick" d="M428.5 92.3L445.7 76.9"/><text class="tl tc" x="420" y="190">SF₆</text><text class="tl tc ta" x="420" y="208">octahedral</text><text class="tl" x="505" y="66">90°: adjacent F</text><text class="tl" x="505" y="90">180°: opposite F</text></svg><figcaption>PF₅ has five bonding pairs: two axial (up and down) and three equatorial. SF₆ has six bonding pairs along three axes at right angles. Wedges and dashes mean the same as in the previous figure.</figcaption></figure>
:::

### Lone pairs on five and six pairs (unfamiliar species)

The same rules predict shapes you have never met. You will not be asked to memorise them, but you may be given a formula and asked to work out the shape. Use the pair count and these two facts:

- In a trigonal bipyramid, lone pairs go in **equatorial** positions. There each lone pair has only two neighbours at 90°, while an axial position would put it at 90° from three neighbours.
- In an octahedron, a second lone pair goes **opposite** the first, as far away as possible (180° apart).

| Species | Pairs | Bonding + lone | Arrangement | Shape |
|---|---|---|---|---|
| \(\ce{SF4}\) | 5 | 4 + 1 | trigonal bipyramidal | see-saw |
| \(\ce{ClF3}\) | 5 | 3 + 2 | trigonal bipyramidal | T-shaped |
| \(\ce{BrF5}\) | 6 | 5 + 1 | octahedral | square pyramidal |
| \(\ce{ICl4-}\) | 6 | 4 + 2 | octahedral | square planar |

Their bond angles are based on 90°, 120° and 180°, squeezed slightly by the lone pairs.

## Try the shapes yourself

Use the tool below to build any arrangement from 2 to 6 pairs. Drag the picture to turn it. Pick a preset or set the number of bonding pairs and lone pairs yourself.

:::html
<div class="widget" data-w="chem-vsepr" data-preset="NH3"></div>
:::

Start from methane. Add a lone pair and watch the angle close to 107°, add a second and it closes again to 104.5°. Then choose \(\ce{SF6}\) and add lone pairs one by one to see why the second lone pair goes opposite the first.

## Summary of shapes

:::key Shapes and bond angles
| Pairs | Bonding | Lone | Shape | Bond angle | Example |
|---|---|---|---|---|---|
| 2 | 2 | 0 | linear | 180° | \(\ce{CO2}\), \(\ce{BeCl2}\) |
| 3 | 3 | 0 | trigonal planar | 120° | \(\ce{BF3}\), \(\ce{CO3^2-}\), \(\ce{NO3-}\) |
| 3 | 2 | 1 | non-linear | a little under 120° | \(\ce{SO2}\) |
| 4 | 4 | 0 | tetrahedral | 109.5° | \(\ce{CH4}\), \(\ce{NH4+}\), \(\ce{SiCl4}\), \(\ce{AlCl4-}\), \(\ce{SO4^2-}\) |
| 4 | 3 | 1 | pyramidal | 107° | \(\ce{NH3}\), \(\ce{H3O+}\), \(\ce{PCl3}\) |
| 4 | 2 | 2 | non-linear | 104.5° | \(\ce{H2O}\) |
| 5 | 5 | 0 | trigonal bipyramidal | 120° and 90° | \(\ce{PF5}\), \(\ce{PCl5}\) |
| 6 | 6 | 0 | octahedral | 90° | \(\ce{SF6}\) |
:::

:::eg Predict the shape of phosphorus trichloride, \(\ce{PCl3}\), and the Cl–P–Cl bond angle.
Phosphorus is in Group 15, so it has 5 outer electrons. The three chlorine atoms add 3: total 8, which is 4 pairs. [B1]

Three pairs are bonding and one is a lone pair. [B1]

Four pairs form a tetrahedral arrangement. With one lone pair on the phosphorus, the atoms form a pyramid: the shape is **pyramidal**. [B1]

The lone pair repels the bonding pairs more strongly than they repel each other, so the angle is less than 109.5°: about 107°. [B1]
:::

:::eg Predict the shape of the sulfate ion, \(\ce{SO4^2-}\), and its O–S–O bond angle.
Sulfur has 6 outer electrons. The four oxygen atoms add 0 and the 2− charge adds 2: total 8, which is 4 pairs. [B1]

Four atoms are attached to the sulfur, so there are 4 bonding pairs and no lone pairs. [B1]

Four bonding pairs around a central atom give a **tetrahedral** shape with an angle of **109.5°**. [B1]
:::

### Shapes in organic molecules

The same rule works at every atom of a larger molecule. Count the regions around each atom (atoms attached plus lone pairs):

- a carbon with four single bonds (such as the carbon of \(\ce{CH3}\)) has 4 regions: tetrahedral, about 109.5°;
- a carbon in a C=C double bond has 3 regions (two atoms plus the double bond as one): trigonal planar, about 120°, so all the atoms of ethene \(\ce{CH2=CH2}\) lie in one flat plane;
- a carbon in a C≡C or C≡N triple bond, or with two C=O double bonds, has 2 regions: linear, 180°;
- the oxygen in an alcohol, R–OH, has 2 bonding regions and 2 lone pairs, like water: non-linear, about 104.5°.

These are the same angles as the hybridisation of [Chemical bonding](#chem.bonding): sp³ is tetrahedral, sp² is trigonal planar and sp is linear. You will use them again in [Introduction to organic chemistry](#chem.org.intro) and [Isomerism](#chem.org.isomerism).

## Polar bonds and polar molecules

A bond between atoms of different electronegativity is **polar**: the shared pair is pulled towards the more electronegative atom, which becomes δ− while the other becomes δ+ (see [Chemical bonding](#chem.bonding)). Chemists draw this as an arrow with a small cross at the δ+ end, pointing at the δ− end.

:::def Dipole moment
A measure of the polarity of a bond or molecule: the size of the partial charges multiplied by the distance between them. It has a direction, drawn from the δ+ end to the δ− end.
:::

A molecule is **polar** if it has an overall dipole moment. Whether it does depends on two things: whether its bonds are polar, and the **shape** of the molecule. Dipoles are like forces, and they add as arrows. If equal dipoles point in opposite directions, they cancel.

:::html
<figure class="fig"><svg viewBox="-17 34 647 162" role="img" aria-label="Bond dipole arrows in carbon dioxide, water, tetrachloromethane and trichloromethane; the dipoles cancel in CO2 and CCl4 but not in H2O and CHCl3"><text class="tl tc" x="60" y="93.5">C</text><text class="tl tc" x="2" y="93.5">O</text><text class="tl tc" x="118" y="93.5">O</text><path class="ln thick" d="M48.5 90L10.5 90" marker-end="url(#ahs)"/><path class="ln thick" d="M48.5 86L48.5 94"/><path class="ln thick" d="M71.5 90L109.5 90" marker-end="url(#ahs)"/><path class="ln thick" d="M71.5 94L71.5 86"/><text class="tl tc" x="185" y="71.5">O</text><text class="tl tc" x="139.1" y="107">H</text><path class="ln thick" d="M150.6 94.6L176.5 74.6" marker-end="url(#ahs)"/><path class="ln thick" d="M153.1 97.8L148.2 91.4"/><text class="tl tc" x="230.9" y="107">H</text><path class="ln thick" d="M219.4 94.6L193.5 74.6" marker-end="url(#ahs)"/><path class="ln thick" d="M221.8 91.4L216.9 97.8"/><path class="c2 sw2" d="M247 112L247 64" marker-end="url(#ah)"/><path class="c2 sw2" d="M251 112L243 112"/><text class="tl tc" x="247" y="132">net dipole</text><text class="tl tc" x="355" y="93.5">C</text><text class="tl tc" x="311" y="59.5">Cl</text><path class="ln thick" d="M343.5 81.1L323 65.3" marker-end="url(#ahs)"/><path class="ln thick" d="M345.9 77.9L341.1 84.3"/><text class="tl tc" x="399" y="59.5">Cl</text><path class="ln thick" d="M366.5 81.1L387 65.3" marker-end="url(#ahs)"/><path class="ln thick" d="M368.9 84.3L364.1 77.9"/><text class="tl tc" x="311" y="127.5">Cl</text><path class="ln thick" d="M343.5 98.9L323 114.7" marker-end="url(#ahs)"/><path class="ln thick" d="M341.1 95.7L345.9 102.1"/><text class="tl tc" x="399" y="127.5">Cl</text><path class="ln thick" d="M366.5 98.9L387 114.7" marker-end="url(#ahs)"/><path class="ln thick" d="M364.1 102.1L368.9 95.7"/><text class="tl tc" x="482" y="93.5">C</text><text class="tl tc" x="438" y="59.5">H</text><path class="ln thick" d="M473.5 83.4L446.5 62.6"/><text class="tl tc" x="526" y="59.5">Cl</text><path class="ln thick" d="M493.5 81.1L514 65.3" marker-end="url(#ahs)"/><path class="ln thick" d="M495.9 84.3L491.1 77.9"/><text class="tl tc" x="438" y="127.5">Cl</text><path class="ln thick" d="M470.5 98.9L450 114.7" marker-end="url(#ahs)"/><path class="ln thick" d="M468.1 95.7L472.9 102.1"/><text class="tl tc" x="526" y="127.5">Cl</text><path class="ln thick" d="M493.5 98.9L514 114.7" marker-end="url(#ahs)"/><path class="ln thick" d="M491.1 102.1L495.9 95.7"/><path class="c2 sw2" d="M550 76L576 96" marker-end="url(#ah)"/><path class="c2 sw2" d="M547.6 79.2L552.4 72.8"/><text class="tl tc" x="580" y="62">net dipole</text><text class="tl tc" x="60" y="160">CO₂</text><text class="tl tc ta" x="60" y="178">non-polar</text><text class="tl tc" x="185" y="160">H₂O</text><text class="tl tc ta" x="185" y="178">polar</text><text class="tl tc" x="355" y="160">CCl₄</text><text class="tl tc ta" x="355" y="178">non-polar</text><text class="tl tc" x="482" y="160">CHCl₃</text><text class="tl tc ta" x="482" y="178">polar</text></svg><figcaption>Each arrow is a bond dipole: the cross is at the δ+ end and the head points to the δ− end. In CO₂ and CCl₄ the dipoles cancel. In H₂O and CHCl₃ they do not, so a separate arrow shows the net dipole. The C–H bond is drawn as a plain line because it is almost non-polar. CCl₄ and CHCl₃ are drawn flat; the real molecules are tetrahedral.</figcaption></figure>
:::

- **Carbon dioxide** has two polar C=O bonds (3.5 − 2.5 = 1.0), but the molecule is linear. The two dipoles are equal and opposite, so they cancel: \(\ce{CO2}\) is **non-polar**.
- **Water** has two polar O–H bonds (3.5 − 2.1 = 1.4) in a V-shaped molecule. The two dipoles do not point in opposite directions, so they add to an overall dipole that points from the hydrogen side towards the oxygen: \(\ce{H2O}\) is **polar**.
- **Tetrachloromethane**, \(\ce{CCl4}\), has four polar C–Cl bonds (3.0 − 2.5 = 0.5) arranged in a perfect tetrahedron. The dipoles cancel in pairs, so \(\ce{CCl4}\) is non-polar.
- **Trichloromethane**, \(\ce{CHCl3}\), has one C–Cl bond replaced by C–H. The three C–Cl dipoles are no longer balanced by a fourth, so they leave an overall dipole: \(\ce{CHCl3}\) is polar.

:::key When is a molecule polar?
A molecule is non-polar if its bonds are non-polar (such as \(\ce{Cl2}\) or \(\ce{O2}\)) **or** if its polar bonds are arranged symmetrically so that the dipoles cancel (\(\ce{CO2}\), \(\ce{BF3}\), \(\ce{CH4}\), \(\ce{CCl4}\), \(\ce{SF6}\), \(\ce{PCl5}\), \(\ce{BeCl2}\)). A molecule is polar if it has polar bonds that do not cancel. A lone pair on the central atom usually makes a molecule polar (\(\ce{NH3}\), \(\ce{H2O}\), \(\ce{SO2}\), \(\ce{PCl3}\)).
:::

:::warn Polar bonds do not always make polar molecules
"CO₂ has polar bonds, so it is polar" is the commonest wrong answer in this topic. Always ask two questions: are the bonds polar, and does the shape make the dipoles cancel? Only a molecule that fails to cancel is polar overall.
:::

:::lab Which liquids are polar?
Run a thin stream of liquid from a burette tap and hold a plastic rod, charged by rubbing it with a cloth, near the stream. A stream of water or propanone bends towards the rod, whichever sign of charge the rod carries, because polar molecules turn so that their opposite end faces the rod. A stream of hexane does not bend. Hexane is flammable and harmful: your teacher should do the hexane part, in a fume cupboard or well-ventilated room away from flames.
:::

:::eg Explain why trichloromethane, \(\ce{CHCl3}\), is polar but tetrachloromethane, \(\ce{CCl4}\), is non-polar. [4 marks]
Both molecules have four regions of electron density around carbon and no lone pairs, so both are tetrahedral. [B1]

In \(\ce{CCl4}\) the four C–Cl bonds are polar (C 2.5, Cl 3.0), but they are identical and arranged symmetrically in a tetrahedron, so the dipoles cancel and there is no overall dipole. [B1]

In \(\ce{CHCl3}\) one C–Cl bond is replaced by C–H, which is almost non-polar (difference 0.4). [B1]

The three C–Cl dipoles are not balanced by a fourth, so they do not cancel and the molecule has an overall dipole. [B1]
:::

## Forces between molecules

Covalent bonds hold the atoms **within** a molecule together. But something must also hold **one molecule to the next**: without it, every molecular substance would be a gas at every temperature. These attractions between molecules are called intermolecular forces. They are far weaker than covalent bonds.

To see how much weaker, compare two energies for water. Boiling 1 mol of water separates the molecules from each other: this takes about 41 kJ. Breaking the covalent bonds in 1 mol of water molecules would take 2 × 460 = 920 kJ (two O–H bonds, each 460 kJ mol⁻¹), more than 20 times more. When a molecular substance melts or boils, its **covalent bonds stay intact**: only the intermolecular forces are overcome.

:::def van der Waals' forces
The generic term for all intermolecular forces: instantaneous dipole–induced dipole (id–id) forces and permanent dipole–permanent dipole (pd–pd) forces, which include hydrogen bonding.
:::

There are three kinds to learn. Id–id forces act between **all** molecules. Pd–pd forces act as well in polar molecules. Hydrogen bonding is a specially strong form of pd–pd force.

### Instantaneous dipole–induced dipole forces

Why do non-polar substances such as helium, methane and iodine ever condense? The electrons in an atom or molecule are always moving. At any instant they may be bunched slightly to one side, so that side is briefly δ− and the other side briefly δ+. That is an **instantaneous dipole**. It lasts only a fraction of a second and then the electrons shift again.

For that moment, the instantaneous dipole disturbs the neighbouring molecule. Its electrons are repelled from the δ− side and attracted to the δ+ side, so the neighbour becomes a dipole too: an **induced dipole**. The δ+ end of one molecule now attracts the δ− end of the other. The dipoles change all the time, but they change together, so the attraction is always there.

:::def Instantaneous dipole–induced dipole (id–id) forces
Attractions between molecules caused by a temporary (instantaneous) dipole in one molecule, which induces a dipole in a neighbouring molecule. They act between all atoms and molecules, polar or not. They are also called London dispersion forces.
:::

:::html
<figure class="fig small"><svg viewBox="-1 33 301 131" role="img" aria-label="Two atoms, the first with an instantaneous dipole, the second with a dipole induced by the first, attracting each other"><path class="ln" d="M66 70a29 29 0 1 0 58 0a29 29 0 1 0 -58 0"/><path class="ln" d="M196 70a29 29 0 1 0 58 0a29 29 0 1 0 -58 0"/><text class="tl tc ta" x="80" y="75">δ−</text><text class="tl tc ta" x="110" y="75">δ+</text><text class="tl tc ta" x="210" y="75">δ−</text><text class="tl tc ta" x="240" y="75">δ+</text><path class="ln" d="M134 70L186 70" marker-end="url(#ah)"/><text class="tl tc" x="160" y="58">attract</text><text class="tl tc" x="95" y="128">instantaneous</text><text class="tl tc" x="95" y="146">dipole</text><text class="tl tc" x="225" y="128">induced</text><text class="tl tc" x="225" y="146">dipole</text></svg><figcaption>An instantaneous dipole in one particle (electrons momentarily on the left) attracts the electrons of its neighbour towards its δ+ end, so the neighbour becomes an induced dipole. The δ+ end of the first then attracts the δ− end of the second.</figcaption></figure>
:::

The strength of id–id forces depends on two things.

**1. The number of electrons.** A molecule with more electrons has a larger electron cloud. A larger cloud is easier to distort, so bigger instantaneous dipoles form and the attraction is stronger. More electrons also means a larger relative molecular mass, so id–id forces generally increase with \(M_r\).

| Substance | Electrons per molecule | State at room temperature |
|---|---|---|
| \(\ce{F2}\) | 18 | gas |
| \(\ce{Cl2}\) | 34 | gas |
| \(\ce{Br2}\) | 70 | liquid |
| \(\ce{I2}\) | 106 | solid |

The same pattern appears in the alkanes. Methane (10 electrons) boils at about −162 °C, ethane (18) at −89 °C, propane (26) at −42 °C and butane (34) at −0.5 °C. Each \(\ce{CH2}\) added to the chain adds 8 electrons and raises the boiling point.

**2. The surface area of contact.** Id–id forces act only where molecules touch. A long, straight molecule can lie alongside its neighbours and touches them over a large area. A compact, branched molecule of the same \(M_r\) is more ball-like, touches its neighbours at fewer points, and so has weaker forces.

| Isomer of \(\ce{C5H12}\) | Shape | Boiling point / °C |
|---|---|---|
| pentane | straight chain | 36 |
| 2-methylbutane | one branch | 28 |
| 2,2-dimethylpropane | two branches, almost spherical | 9.5 |

:::story A gecko on the ceiling
A gecko can run up a glass window and hang from the ceiling by one toe. Each foot carries hundreds of thousands of microscopic hairs, which bring the molecules of the foot very close to the molecules of the surface. Each contact gives only a weak id–id attraction, but there are so many that together they hold the animal up. Peeling a toe off at an angle breaks the contacts a few at a time, which is why the gecko can let go so easily.
:::

### Permanent dipole–permanent dipole forces

Polar molecules have a dipole all the time. The δ+ end of one molecule is attracted to the δ− end of its neighbour. These **permanent dipole–permanent dipole (pd–pd) forces** are in addition to id–id forces, so a polar molecule is held more strongly than a non-polar molecule with a similar number of electrons.

:::def Permanent dipole–permanent dipole (pd–pd) forces
Attractions between the δ+ end of one polar molecule and the δ− end of a neighbouring polar molecule.
:::

A good test case is propanone, \(\ce{CH3COCH3}\), and butane, \(\ce{CH3CH2CH2CH3}\). Both have \(M_r\) = 58.0 and similar numbers of electrons (32 and 34), so their id–id forces are almost the same. But propanone has a polar C=O bond and the molecule is polar, so it also has pd–pd forces. Propanone boils at 56 °C and butane at −0.5 °C.

:::eg Explain why propanone (b.p. 56 °C) has a higher boiling point than butane (b.p. −0.5 °C), although both have \(M_r\) = 58.0. [3 marks]
Butane is non-polar, so its molecules are held together only by id–id forces. [B1]

Propanone has a polar C=O bond (O is more electronegative than C) and the molecule is polar, so it has pd–pd forces as well as id–id forces. [B1]

The total attraction is stronger in propanone, so more energy is needed to overcome the forces between its molecules. [B1]
:::

### Hydrogen bonding

Hydrogen bonding is the strongest intermolecular force. It is a special case of pd–pd attraction, and it needs three things.

:::def Hydrogen bond
An attraction between a hydrogen atom that is covalently bonded to a very electronegative atom (here N or O) and a lone pair of electrons on a nitrogen or oxygen atom of another molecule. It is a special case of a pd–pd force.
:::

1. A hydrogen atom bonded to a very electronegative atom, N or O. The bond is so polar that the hydrogen is strongly δ+. It is also tiny and has no inner electrons, so its δ+ charge can be approached very closely.
2. A **lone pair** on an N or O atom in a neighbouring molecule.
3. The O–H···O (or N–H···N, O–H···N, N–H···O) must lie in a **straight line**.

In this syllabus hydrogen bonding is the N–H and O–H case, as in \(\ce{NH3}\), \(\ce{H2O}\), alcohols, amines and carboxylic acids.

:::html
<figure class="fig small"><svg viewBox="20 40 301 128" role="img" aria-label="Two water molecules joined by a hydrogen bond: the hydrogen atom of one, labelled delta plus, points along a straight line at a lone pair on the oxygen atom of the other, labelled delta minus"><text class="tl tc" x="90" y="103.5">O</text><text class="tl tc" x="140" y="103.5">H</text><path class="ln thick" d="M98.5 100L131.5 100"/><text class="tl tc" x="78" y="150">H</text><path class="ln thick" d="M87 111.5L81 135"/><circle class="fi" cx="83" cy="82" r="1.7"/><circle class="fi" cx="89" cy="82" r="1.7"/><circle class="fi" cx="68" cy="89" r="1.7"/><circle class="fi" cx="68" cy="95" r="1.7"/><text class="tl tc" x="240" y="103.5">O</text><text class="tl tc" x="269.4" y="141.5">H</text><path class="ln thick" d="M248.5 111L260.9 127"/><text class="tl tc" x="269.4" y="65.5">H</text><path class="ln thick" d="M248.5 89L260.9 73"/><circle class="fi" cx="225" cy="97" r="1.7"/><circle class="fi" cx="225" cy="103" r="1.7"/><circle class="fi" cx="231" cy="118" r="1.7"/><circle class="fi" cx="237" cy="118" r="1.7"/><path class="ln dash thick" d="M148.5 100L219 100"/><text class="tl tc ta" x="140" y="76">δ+</text><text class="tl tc ta" x="88" y="70">δ−</text><text class="tl tc ta" x="240" y="70">δ−</text><text class="tl tc" x="190" y="146">hydrogen bond</text><path class="ln-m thin" d="M190 130L190 108"/></svg><figcaption>A hydrogen bond between two water molecules. The δ+ hydrogen of the left molecule points at a lone pair on the δ− oxygen of the right molecule, and O–H···O lies in a straight line. Dots are lone pairs.</figcaption></figure>
:::

:::exam Drawing a hydrogen bond for full marks
Draw at least two molecules. Show the lone pair on the O (or N) that receives the bond, the δ+ on the H and the δ− on the O (or N). Draw the hydrogen bond as a dashed line, label it "hydrogen bond", and make O–H···O a straight line. A bond drawn to a hydrogen atom that is joined to carbon loses marks.
:::

:::warn Not every hydrogen can hydrogen-bond
The hydrogen atoms in \(\ce{CH4}\) or in the \(\ce{CH3}\) groups of ethanol do **not** form hydrogen bonds. A C–H bond is almost non-polar (C 2.5 and H 2.1 differ by only 0.4), whereas O–H differs by 1.4 and N–H by 0.9. Ethanol forms hydrogen bonds through its O–H group only. Methoxymethane, \(\ce{CH3OCH3}\), has the same formula as ethanol but no O–H bond, so its molecules do not hydrogen-bond to each other, and it boils at a much lower temperature.
:::

:::cols
:::col Strength of the forces between molecules
Hydrogen bonding is stronger than pd–pd forces, which are stronger than id–id forces **of a similar-sized molecule**. But a large molecule can have id–id forces larger than the pd–pd forces of a small one.
:::
:::col Why this matters in answers
Name every force that is present, say which is strongest, and link it to the energy needed. "Water has hydrogen bonding, so a high boiling point" gets only part of the marks.
:::
:::

## Boiling points and hydrogen bonding

Look at the boiling points of the hydrides of Groups 14 and 16. Down Group 14 they rise steadily: more electrons, stronger id–id forces. Down Group 16 the same trend is there from \(\ce{H2S}\) to \(\ce{H2Te}\), but water breaks the pattern completely.

| Group 14 hydride | Electrons | Boiling point / °C | Group 16 hydride | Electrons | Boiling point / °C |
|---|---|---|---|---|---|
| \(\ce{CH4}\) | 10 | −162 | \(\ce{H2O}\) | 10 | 100 |
| \(\ce{SiH4}\) | 18 | −112 | \(\ce{H2S}\) | 18 | −60 |
| \(\ce{GeH4}\) | 36 | −88 | \(\ce{H2Se}\) | 36 | −41 |
| \(\ce{SnH4}\) | 54 | −52 | \(\ce{H2Te}\) | 54 | −2 |

Methane and water have the same number of electrons (10), so their id–id forces are similar, yet water boils 262 °C higher. Hydrogen bonding is responsible. Without it, extrapolating the Group 16 trend backwards would make water boil well below −60 °C and a gas at room temperature. Ammonia (the Group 15 hydride) shows the same sort of jump, though smaller.

Water forms more hydrogen bonds per molecule than ammonia. Every hydrogen bond uses one δ+ H atom and one lone pair. A water molecule has 2 H atoms and 2 lone pairs, so it takes part in up to 4 hydrogen bonds, which is 2 bonds per molecule because each bond is shared by two molecules. An ammonia molecule has 3 H atoms but only 1 lone pair, and the scarcer of the two sets the limit: 1 bond per molecule. More hydrogen bonds mean more energy is needed to separate the molecules.

:::eg Methane boils at −162 °C, ammonia at −33 °C and water at 100 °C. Explain this order. [5 marks]
Methane is non-polar and has only id–id forces between its molecules, which are weak. [B1]

Ammonia has hydrogen bonds (N–H···N), formed between the δ+ H of one molecule and the lone pair on the N of another. [B1]

Hydrogen bonds are stronger than id–id forces, so more energy is needed to separate ammonia molecules than methane molecules. [B1]

Water also has hydrogen bonds, and each molecule can form more of them than ammonia: two H atoms and two lone pairs, against three H atoms but only one lone pair for ammonia. [B1]

So the attraction between water molecules is the strongest, and the most energy is needed to overcome it. [B1]
:::

## The unusual properties of water

Hydrogen bonding explains three properties of water that make it stand out from other small molecules.

**1. High melting and boiling points.** As above: a lot of energy is needed to break the hydrogen bonds between molecules, so water is a liquid at room temperature.

**2. High surface tension.** A molecule in the bulk of the liquid is pulled in all directions by hydrogen bonds from its neighbours. A molecule at the surface has neighbours below and beside it but none above, so it is pulled sideways and inwards. The surface behaves like a stretched skin, which lets insects such as pond skaters walk on water.

**3. Ice is less dense than liquid water.** Almost every other substance is denser as a solid, because the particles pack more closely. In ice, each water molecule forms **four** hydrogen bonds, two with its own H atoms and two through the lone pairs on O, in a tetrahedral arrangement. This builds an open, hexagonal lattice with a lot of empty space. When ice melts, some of the hydrogen bonds break and the molecules move closer together, so liquid water is denser than ice. Water is densest at about 4 °C.

:::eg Explain why ice floats on water, and calculate the volume of ice formed when a 330 cm³ can of water (density 1.00 g cm⁻³) freezes. The density of ice is 0.917 g cm⁻³. [4 marks]
In ice, each molecule forms four hydrogen bonds in a rigid, open lattice with empty spaces, which holds the molecules further apart than in liquid water. [B1]

The same mass occupies a greater volume, so ice is less dense than water and floats. [B1]

Mass of water = 330 cm³ × 1.00 g cm⁻³ = 330 g. [B1]
\[V(\text{ice}) = \frac{330}{0.917} = 360\,\mathrm{cm^3}\] [A1]

The volume increases by about 9%, so a sealed can can split when its contents freeze.
:::

:::tip Why this matters in a pond
Because ice floats, a lake freezes from the top down, and the ice layer insulates the water below. If ice were denser than water it would sink, the lake would freeze from the bottom up and fish would have nowhere to survive the winter.
:::

## Bonds are stronger than intermolecular forces

Chemists use "bond" for the strong forces inside a substance and "force" for the weak ones between molecules. In general:

:::key Strength of the types of bonding
Ionic, covalent and metallic bonds are generally much stronger than intermolecular forces. Among intermolecular forces: hydrogen bonds > pd–pd forces > id–id forces, for molecules of similar size.
:::

This is why molecular substances (such as iodine or ice) melt and boil at low temperatures, and giant ionic, metallic and covalent structures (such as sodium chloride or diamond) at high temperatures. When iodine sublimes or water boils, covalent bonds do **not** break. The next chapter, [States of matter](#chem.states), links these forces to the properties of solids, liquids and gases.

:::exam Explaining a boiling point
Follow these steps in the order below. 1. Say what kind of particles are separated (molecules). 2. Name every intermolecular force present in each substance. 3. Compare strengths, giving the reason (more electrons, extra pd–pd, hydrogen bonding, larger contact area). 4. Say more energy is needed to overcome the stronger forces. Never say "the covalent bonds break" when a molecular substance boils.
:::

:::eg Spot the error: Explain why the bond angle in water (104.5°) is smaller than in methane (109.5°). [3 marks]
A student wrote this answer.

Line 1: Both molecules have four pairs of electrons around the central atom, which repel to give a tetrahedral arrangement.
Line 2: In water two of the pairs are lone pairs, which are held closer to the nucleus and so repel less strongly than bonding pairs.
Line 3: This closes the bond angle from 109.5° to 104.5°.

Line 1 is correct [B1]. **Line 2 is wrong: a lone pair is attracted by only one nucleus, so it spreads out further and repels MORE strongly than a bonding pair. The student's own line 3 contradicts line 2, because weaker repulsion could not close the angle [B0].** Line 3 is correct as a statement of the result [B1].

Correct line 2: lone pairs repel more strongly than bonding pairs, so the two lone pairs push the two bonding pairs closer together. [B1]

The student scores 2 out of 3. Lone pairs repel **more**, and that is the whole explanation.
:::

:::try Start easy, finish at exam standard
Q: Give the number of bonding pairs and lone pairs on the central atom in (a) \(\ce{PH3}\), (b) \(\ce{SiCl4}\), (c) \(\ce{BF3}\), (d) \(\ce{H3O+}\).
A: (a) P: 5 + 3 = 8, 4 pairs: 3 bonding, 1 lone. (b) Si: 4 + 4 = 8, 4 pairs: 4 bonding, 0 lone. (c) B: 3 + 3 = 6, 3 pairs: 3 bonding, 0 lone. (d) O: 6 + 3 − 1 = 8, 4 pairs: 3 bonding, 1 lone.
Q: Name the shape and give the bond angle of each species in the previous question.
A: (a) \(\ce{PH3}\) pyramidal, about 107°. (b) \(\ce{SiCl4}\) tetrahedral, 109.5°. (c) \(\ce{BF3}\) trigonal planar, 120°. (d) \(\ce{H3O+}\) pyramidal, about 107°.
Q: Predict the shape and bond angle of the amide ion, \(\ce{NH2-}\).
A: N: 5 + 2 + 1 (the 1− charge) = 8, which is 4 pairs: 2 bonding and 2 lone. The shape is non-linear, with an angle of about 104.5°, like water.
Q: Give the shape at each carbon atom of propene, \(\ce{CH3CH=CH2}\).
A: The \(\ce{CH3}\) carbon has four single bonds: tetrahedral, about 109.5°. Each carbon of the C=C double bond has 3 regions (two atoms and the double bond): trigonal planar, about 120°.
Q: Carbon dioxide has polar bonds but is a non-polar molecule. Explain.
A: Each C=O bond is polar (O is more electronegative), but \(\ce{CO2}\) is linear, so the two equal dipoles point in opposite directions and cancel. There is no overall dipole.
Q: State which intermolecular forces are present in (a) argon, (b) hydrogen chloride, (c) methanol, \(\ce{CH3OH}\).
A: (a) id–id only (argon atoms are non-polar). (b) id–id and pd–pd (H–Cl is polar). (c) id–id, pd–pd and hydrogen bonding (the molecule has an O–H group).
Q: Which of \(\ce{CH3OH}\), \(\ce{CH3OCH3}\), \(\ce{CH3NH2}\) and \(\ce{CH3F}\) can form hydrogen bonds with other molecules of the same substance?
A: \(\ce{CH3OH}\) (it has an O–H bond) and \(\ce{CH3NH2}\) (it has N–H bonds). \(\ce{CH3OCH3}\) and \(\ce{CH3F}\) have no hydrogen atom bonded to N or O, so there are none in the pure liquid.
Q: Explain why the boiling point of iodine is higher than that of chlorine.
A: Both are non-polar, so the forces are id–id. An iodine molecule has 106 electrons against 34 in chlorine, so its electron cloud is larger and easier to distort. The instantaneous dipoles are larger and the attraction between molecules is stronger. More energy is needed to overcome it.
Q: What happens to the covalent bonds in a water molecule when water boils? What is overcome?
A: Nothing: the O–H bonds stay intact. The hydrogen bonds (and other intermolecular forces) between molecules are overcome.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the shape and bond angle of (a) \(\ce{BF3}\), (b) \(\ce{SF6}\), (c) \(\ce{H2O}\).
A: (a) trigonal planar, 120° [B1] (b) octahedral, 90° [B1] (c) non-linear, 104.5° [B1]
Q: [6 marks] ★★ For each of (a) \(\ce{PCl3}\), (b) \(\ce{CO3^2-}\), (c) \(\ce{AlCl4-}\): calculate the number of electron pairs around the central atom and give the shape and bond angle.
H: Add the outer electrons of the central atom, one for each Cl, and the charge (+1 for a 1− charge, +2 for a 2− charge). Oxygen adds 0.
A: (a) P: 5 + 3 = 8, which is 4 pairs: 3 bonding and 1 lone [B1]. Pyramidal, about 107° [B1].
(b) C: 4 + 2 = 6, which is 3 pairs, all bonding [B1]. Trigonal planar, 120° [B1].
(c) Al: 3 + 4 + 1 = 8, which is 4 pairs, all bonding [B1]. Tetrahedral, 109.5° [B1].
Q: [4 marks] ★★ Explain why \(\ce{CO2}\) is a non-polar molecule but \(\ce{SO2}\) is polar.
H: Think of the shapes first. How many lone pairs does the central atom have in each?
A: The C=O bonds in \(\ce{CO2}\) are polar. [B1] The molecule is linear (two regions, no lone pair), so the two dipoles are equal and opposite and cancel. [B1]
In \(\ce{SO2}\) the sulfur has three regions, one of them a lone pair, so the molecule is non-linear. [B1] The two S=O dipoles do not cancel, so there is an overall dipole. [B1]
Q: [3 marks] ★★ Explain why iodine has a higher boiling point than chlorine.
A: Both are non-polar and have id–id forces between molecules. [B1] An iodine molecule has more electrons (106 against 34), so a larger, more easily distorted electron cloud and stronger instantaneous dipoles. [B1] More energy is needed to overcome the stronger id–id forces. [B1]
Q: [5 marks] ★★ The boiling points of pentane, 2-methylbutane and 2,2-dimethylpropane, all \(\ce{C5H12}\), are 36 °C, 28 °C and 9.5 °C. Explain why they differ, although they have the same \(M_r\).
H: The isomers have the same number of electrons. What differs about the shape of the molecules?
A: All three are non-polar, so the only intermolecular forces are id–id forces. [B1] They have the same number of electrons, so differences come from the shape. [B1] Pentane is a straight chain and touches its neighbours along its whole length, so it has the largest contact area and the strongest forces. [B1] 2,2-dimethylpropane is almost spherical, so it touches its neighbours at few points and has the weakest forces. [B1] The weaker the forces, the less energy is needed to separate the molecules, so the lower the boiling point. [B1]
Q: [4 marks] ★★ (#chem.moles) A sealed plastic bottle contains 500 cm³ of water of density 1.00 g cm⁻³, which freezes. The density of ice is 0.917 g cm⁻³. Calculate the volume of the ice, and explain the change in density using hydrogen bonding.
H: The mass does not change when water freezes. Volume = mass ÷ density.
A: Mass of water = 500 cm³ × 1.00 g cm⁻³ = 500 g. [B1]
\(V(\text{ice}) = 500 / 0.917\) [M1] \(= 545\,\mathrm{cm^3}\) [A1]
In ice each molecule forms four hydrogen bonds in an open lattice with empty space, so the molecules are further apart than in liquid water. [B1]
Q: [6 marks] ★★★ Propanone, \(\ce{CH3COCH3}\) (\(M_r\) = 58.0), butane (\(M_r\) = 58.0) and propan-1-ol, \(\ce{CH3CH2CH2OH}\) (\(M_r\) = 60.0), have boiling points of 56 °C, −0.5 °C and 97 °C. Explain the order of boiling points by naming the forces in each substance.
H: Which has a polar C=O bond? Which has an O–H bond?
A: Butane is non-polar: it has only id–id forces, the weakest, so it has the lowest boiling point. [B1] [B1]
Propanone is polar (C=O): it has pd–pd forces in addition to id–id forces. [B1] The stronger attraction raises the boiling point above that of butane. [B1]
Propan-1-ol has an O–H group, so its molecules form hydrogen bonds as well as id–id forces. [B1] Hydrogen bonds are stronger than pd–pd forces, so it has the highest boiling point. [B1]
Q: [7 marks] ★★★ Ammonia reacts with boron trifluoride, \(\ce{BF3}\), to form \(\ce{H3N-BF3}\). (a) State the shape of \(\ce{NH3}\) and of \(\ce{BF3}\). (b) Explain, in terms of electrons, how the N–B bond forms and name this type of bond. (c) Predict the shape around boron in \(\ce{H3N-BF3}\) and the F–B–F bond angle. (d) Explain why \(\ce{BF3}\) is non-polar although the B–F bonds are polar.
H: Count the electrons around boron in \(\ce{BF3}\). How does nitrogen help?
A: (a) \(\ce{NH3}\) is pyramidal [B1]; \(\ce{BF3}\) is trigonal planar [B1].
(b) Boron in \(\ce{BF3}\) has only 6 electrons in its outer shell, so it has an empty orbital. [B1] The lone pair on nitrogen is donated into it to form a coordinate (dative covalent) bond. [B1]
(c) Boron now has 4 bonding pairs and no lone pair: tetrahedral [B1], with an angle of 109.5°. (This is one mark in total for the shape and angle.)
(d) The B–F bonds are polar (F is much more electronegative than B). [B1] The molecule is trigonal planar and symmetrical, so the three dipoles cancel. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Chlorine trifluoride, \(\ce{ClF3}\), is an unfamiliar molecule. (a) Calculate the number of electron pairs around chlorine and the number of lone pairs. (b) Give the arrangement of the electron pairs and say where the lone pairs go and why. (c) Name the shape of the molecule and say whether it is polar.
H: Chlorine is in Group 17, so it has 7 outer electrons. Each F adds 1.
H: In a trigonal bipyramid the 120° positions are less crowded than the axial ones.
A: (a) Cl: 7 + 3 = 10, which is 5 pairs: 3 bonding and 2 lone. [B1] [B1]
(b) The five pairs form a trigonal bipyramid. The two lone pairs go in equatorial positions [B1], where each has only two neighbours at 90° instead of three. [B1]
(c) The three F atoms lie in a T: the molecule is T-shaped, and the dipoles do not cancel, so it is polar. [B1]
Q: [6 marks] ★★★ The tetrachloroiodate(III) ion, \(\ce{ICl4-}\), has a square planar shape. Show how the VSEPR rules lead to this shape, and explain why the four I–Cl bond dipoles cancel.
H: Count 7 + 4 + 1. Where is the second lone pair in an octahedron, relative to the first?
H: Work out the net effect of four equal dipoles in a square.
A: Iodine: 7 + 4 + 1 (for the 1− charge) = 12, which is 6 pairs. [B1] There are 4 bonding pairs and 2 lone pairs. [B1]
Six pairs give an octahedral arrangement. [B1] The two lone pairs repel each other most strongly, so they take positions opposite each other, 180° apart. [B1]
That leaves the four chlorine atoms in one plane at 90° to each other: square planar. [B1]
The four equal I–Cl dipoles point outwards in opposite pairs in a symmetrical square, so they cancel. [B1]
:::

:::quiz
? Which species has a tetrahedral shape?
- \(\ce{NH3}\)
- \(\ce{H2O}\)
+ \(\ce{NH4+}\)
- \(\ce{BF3}\)
> \(\ce{NH4+}\) has four bonding pairs and no lone pair. \(\ce{NH3}\) has four pairs but one is a lone pair, so it is pyramidal; \(\ce{H2O}\) is non-linear; \(\ce{BF3}\) has three pairs and is trigonal planar.
? Why is the H–O–H angle in water smaller than the H–C–H angle in methane?
- Oxygen is more electronegative than carbon.
+ The two lone pairs on oxygen repel the bonding pairs more strongly than bonding pairs repel each other.
- Water molecules form hydrogen bonds.
- Oxygen has two bonds and carbon has four.
> Lone pairs spread out more than bonding pairs and so repel more strongly, closing the angle. Electronegativity and hydrogen bonding do not set the angle inside one molecule.
? How many lone pairs are on the sulfur atom in the sulfite ion, \(\ce{SO3^2-}\)?
- 0
+ 1
- 2
- 3
> S: 6 + 2 (the 2− charge) = 8, which is 4 pairs. Three oxygen atoms are attached, so 3 bonding pairs and 1 lone pair. With 0 lone pairs you would have the trigonal planar \(\ce{SO3}\) instead.
? Which molecule is non-polar although it contains polar bonds?
- \(\ce{SO2}\)
- \(\ce{NH3}\)
+ \(\ce{CCl4}\)
- \(\ce{CHCl3}\)
> The four equal C–Cl dipoles in the tetrahedral \(\ce{CCl4}\) cancel. \(\ce{SO2}\), \(\ce{NH3}\) and \(\ce{CHCl3}\) have dipoles that do not cancel.
? Which pair of molecules can both form hydrogen bonds with molecules of their own kind?
- \(\ce{CH4}\) and \(\ce{HCl}\)
+ \(\ce{NH3}\) and \(\ce{CH3OH}\)
- \(\ce{CH3F}\) and \(\ce{H2S}\)
- \(\ce{CH3OCH3}\) and \(\ce{CH3CHO}\)
> Hydrogen bonding needs an H atom on N or O and a lone pair on N or O. Both \(\ce{NH3}\) and \(\ce{CH3OH}\) have these. Neither HCl, \(\ce{CH3F}\), \(\ce{H2S}\), \(\ce{CH3OCH3}\) nor \(\ce{CH3CHO}\) has a hydrogen atom bonded to N or O.
? Why does the boiling point rise from \(\ce{F2}\) to \(\ce{I2}\)?
- The covalent bond gets stronger.
- The molecules get more polar.
+ The molecules have more electrons, so the id–id forces are stronger.
- Hydrogen bonds form between the molecules.
> The halogens are non-polar and have no hydrogen bonding. The F–F bond is weaker than Cl–Cl and the bonds are not broken on boiling anyway. More electrons means a larger, more easily distorted cloud and stronger id–id forces.
? 1.00 kg of water freezes to ice of density 0.917 g cm⁻³. What volume does the ice occupy?
- 917 cm³
- 1000 cm³
+ 1090 cm³
- 83 cm³
> Volume = mass ÷ density = 1000 g ÷ 0.917 g cm⁻³ = 1090 cm³ (3 s.f.). Multiplying instead of dividing gives 917 cm³. The volume is greater than 1000 cm³ because ice is less dense than water.
? What is overcome when ethanol boils?
- the O–H covalent bonds
- the C–C covalent bonds
+ hydrogen bonds and other intermolecular forces between molecules
- ionic bonds between ethanol molecules
> Boiling separates molecules. The covalent bonds inside each molecule stay as they are. Ethanol is a molecular substance and has no ionic bonds.
:::

:::checklist What you can now do
- [ ] I can use electron-pair repulsion (VSEPR) to explain the shape of a molecule, with lone pairs repelling more than bonding pairs and a multiple bond counted as one region.
- [ ] I can give the shape and bond angle of BF₃, CO₂, CH₄, NH₃, H₂O, SF₆ and PF₅.
- [ ] I can count electron pairs and predict the shape and bond angle of analogous species such as NH₄⁺, H₃O⁺, SO₂, PCl₅, SiCl₄, CO₃²⁻, NO₃⁻ and AlCl₄⁻.
- [ ] I can predict whether a molecule is polar from the polarity of its bonds and its shape, and explain why symmetrical molecules such as CO₂, BF₃ and CH₄ are non-polar.
- [ ] I can define van der Waals' forces and describe id–id and pd–pd forces and how they depend on electrons, contact area and polarity.
- [ ] I can describe hydrogen bonding, limited to N–H and O–H, and draw it correctly between two molecules.
- [ ] I can use intermolecular forces to explain and compare the boiling points of substances.
- [ ] I can explain the anomalous properties of water: high melting and boiling points, high surface tension and ice being less dense than water.
- [ ] I can say why ionic, covalent and metallic bonds are generally stronger than intermolecular forces, and what is and is not broken when a molecular substance boils.
:::

:::recap
- Electron pairs repel and take up positions as far apart as possible. A double or triple bond is one region. Lone pair–lone pair > lone pair–bonding pair > bonding pair–bonding pair repulsion.
- Count the pairs: outer electrons of the central atom + 1 for each H or halogen + 0 for each O (double bonded) ± charge, then divide by 2. Bonding pairs = atoms attached; the rest are lone pairs.
- 2 pairs linear 180° (CO₂, BeCl₂); 3 pairs trigonal planar 120° (BF₃, CO₃²⁻, NO₃⁻), SO₂ non-linear; 4 pairs tetrahedral 109.5° (CH₄, NH₄⁺, SiCl₄, AlCl₄⁻, SO₄²⁻), pyramidal 107° (NH₃, H₃O⁺, PCl₃), non-linear 104.5° (H₂O); 5 pairs trigonal bipyramidal 120° and 90° (PF₅, PCl₅); 6 pairs octahedral 90° (SF₆).
- Lone pairs go equatorial in a trigonal bipyramid and opposite each other in an octahedron (ClF₃ T-shaped, ICl₄⁻ square planar).
- A molecule is polar if its bond dipoles do not cancel. Symmetrical molecules (CO₂, BF₃, CH₄, CCl₄, SF₆) are non-polar; a lone pair on the central atom usually makes a molecule polar.
- Van der Waals' forces are all intermolecular forces: id–id (all molecules; stronger with more electrons and more contact area), pd–pd (polar molecules) and hydrogen bonding (H on N or O, with a lone pair on N or O in a straight line).
- Water's high boiling point, high surface tension and less dense ice come from hydrogen bonding; ice has an open lattice with four hydrogen bonds per molecule.
- Intermolecular forces are much weaker than covalent, ionic or metallic bonds. When a molecular substance boils, only the intermolecular forces are overcome.
:::

:::links
- read: [Shapes of molecules and ions](https://www.chemguide.co.uk/atoms/bonding/shapes.html) · Chemguide · VSEPR step by step, with lone pairs and the unusual shapes
- read: [Van der Waals' forces](https://www.chemguide.co.uk/atoms/bonding/vdw.html) · Chemguide · id–id and pd–pd forces explained slowly
- read: [Hydrogen bonding](https://www.chemguide.co.uk/atoms/bonding/hbond.html) · Chemguide · why water and ammonia behave unusually
- read: [Bonding menu](https://www.chemguide.co.uk/atoms/bondingmenu.html) · Chemguide · every topic on bonding in one place
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [States of matter](#chem.states) uses these forces to explain why solids, liquids and gases behave as they do.
