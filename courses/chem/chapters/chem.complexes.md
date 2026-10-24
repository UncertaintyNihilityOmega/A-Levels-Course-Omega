@chapter chem.complexes
@title Complexes: colour, isomerism and stability
@level a2
@paper CAIE 9701 Paper 4
@time 6–8 hours
@summary Why complex ions are coloured, how the same atoms can be arranged in different ways, and how to measure how stable a complex is. You will learn how ligands split the d orbitals, how an electron promoted across the gap absorbs light, cis/trans and optical isomerism in complexes, and stability constants.

:::why
A solution of copper(II) sulfate is blue, add ammonia and it turns a deeper blue, add concentrated hydrochloric acid and it turns yellow-green. The metal is the same each time; only the ligands change. This chapter explains why, and then goes further: two complexes with exactly the same atoms can behave differently in the body (the cancer drug cisplatin works and its isomer does not), and a stability constant tells you how strongly a ligand holds on to a metal ion, which decides which ligand wins when two compete.
:::

**Before you start**, you should know ligands, complex ions and ligand exchange from [Transition elements](#chem.transition), stereoisomerism from [Isomerism](#chem.org.isomerism) and equilibrium constants from [Chemical equilibria](#chem.equilibria).

:::try Warm-up
Q: What is the coordination number of \(\ce{[Ni(en)3]^2+}\), where en is a bidentate ligand? (from [Transition elements](#chem.transition))
A: Three bidentate ligands form \(3 \times 2 = 6\) dative bonds, so the coordination number is 6.
Q: What must be true of the groups on a C=C bond for cis/trans isomers to exist? (from [Isomerism](#chem.org.isomerism))
A: Each carbon of the double bond must carry two different groups, and rotation about the double bond is not possible.
Q: Write the expression for \(K_c\) for \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\). (from [Chemical equilibria](#chem.equilibria))
A: \(K_c = \dfrac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}\)
:::

## Why are complexes coloured?

### Colour and light

White light is a mixture of all the colours of the spectrum. A solution looks coloured when it **absorbs** light of some frequencies and lets the rest pass through to your eye. The colour you see is made of the frequencies that were *not* absorbed, and it is called the **complementary colour** of the light absorbed.

| Colour absorbed | Colour seen |
|---|---|
| red | green |
| orange | blue |
| yellow | violet |
| green | red |
| blue | orange |
| violet | yellow |

This is a simple colour wheel: each colour is paired with the one opposite it. The frequency of visible light rises from red (lowest) through orange, yellow, green and blue to violet (highest).

The energy of the light absorbed is linked to its frequency by

\[\Delta E = hf\]

where \(\Delta E\) is the energy gap in joules, \(f\) is the frequency in hertz and \(h\) is the Planck constant. A larger energy gap means that light of **higher frequency** is absorbed.

### The d orbitals split

In a free transition-metal ion, the five 3d orbitals all have the same energy. Orbitals with the same energy are **degenerate**.

:::def Degenerate orbitals
Orbitals that have the same energy.
:::

When ligands bond to the ion, their lone pairs repel the electrons in the d orbitals. The repulsion is not the same for every d orbital, because the orbitals point in different directions. The five orbitals are no longer degenerate: they split into two sets with different energies, separated by an energy gap \(\Delta E\).

**Octahedral complexes.** Six ligands approach along the x, y and z axes. Two orbitals, \(d_{z^2}\) and \(d_{x^2-y^2}\), have lobes pointing along the axes, straight at the ligands, so they are repelled more strongly and rise in energy. The other three, \(d_{xy}\), \(d_{xz}\) and \(d_{yz}\), have lobes between the axes, so they are repelled less. The result is **two higher orbitals and three lower orbitals**.

**Tetrahedral complexes.** Four ligands approach between the axes. Now \(d_{xy}\), \(d_{xz}\) and \(d_{yz}\) are the ones that point closer to the ligands. The splitting is **upside down: three higher orbitals and two lower orbitals**, and the gap \(\Delta E\) is smaller (there are only four ligands, and none points straight at an orbital).

:::html
<figure class="fig small"><svg viewBox="0 0 340 345" role="img" aria-label="Splitting of the five 3d orbitals. In an octahedral complex the orbitals split into three lower orbitals dxy, dxz and dyz and two higher orbitals dz2 and dx2 minus y2, separated by an energy gap delta E. In a tetrahedral complex the split is reversed, with two lower orbitals and three higher orbitals, and a smaller gap"><text class="tl tc" x="190" y="16">Octahedral complex</text><text class="tl" x="2" y="36">energy</text><path class="ax" d="M10 152L10 44" marker-end="url(#ahm)"/><path class="ln thick" d="M24 97L35 97"/><path class="ln thick" d="M39 97L50 97"/><path class="ln thick" d="M54 97L65 97"/><path class="ln thick" d="M69 97L80 97"/><path class="ln thick" d="M84 97L95 97"/><text class="tl tc" x="59.5" y="125">free ion</text><text class="tl tc" x="59.5" y="142">same energy</text><path class="ln thick" d="M160 55L180 55"/><path class="ln thick" d="M186 55L206 55"/><path class="ln thick" d="M160 125L180 125"/><path class="ln thick" d="M186 125L206 125"/><path class="ln thick" d="M212 125L232 125"/><path class="ln-m thin dash" d="M101 97L154 55"/><path class="ln-m thin dash" d="M101 97L154 125"/><text class="tl tc" x="183" y="46">dz²  dx²−y²</text><text class="tl tc" x="196" y="145">dxy  dxz  dyz</text><path class="c2 sw2" d="M276 86L276 55" marker-end="url(#ah)"/><path class="c2 sw2" d="M276 94L276 125" marker-end="url(#ah)"/><text class="tl" x="288" y="94">ΔE</text><text class="tl tc" x="190" y="196">Tetrahedral complex</text><text class="tl" x="2" y="216">energy</text><path class="ax" d="M10 332L10 224" marker-end="url(#ahm)"/><path class="ln thick" d="M24 265.2L35 265.2"/><path class="ln thick" d="M39 265.2L50 265.2"/><path class="ln thick" d="M54 265.2L65 265.2"/><path class="ln thick" d="M69 265.2L80 265.2"/><path class="ln thick" d="M84 265.2L95 265.2"/><text class="tl tc" x="59.5" y="293.2">free ion</text><text class="tl tc" x="59.5" y="310.2">same energy</text><path class="ln thick" d="M160 246L180 246"/><path class="ln thick" d="M186 246L206 246"/><path class="ln thick" d="M212 246L232 246"/><path class="ln thick" d="M160 294L180 294"/><path class="ln thick" d="M186 294L206 294"/><path class="ln-m thin dash" d="M101 265.2L154 246"/><path class="ln-m thin dash" d="M101 265.2L154 294"/><text class="tl tc" x="196" y="237">dxy  dxz  dyz</text><text class="tl tc" x="183" y="314">dz²  dx²−y²</text><path class="c2 sw2" d="M276 266L276 246" marker-end="url(#ah)"/><path class="c2 sw2" d="M276 274L276 294" marker-end="url(#ah)"/><text class="tl" x="288" y="274">ΔE</text></svg><figcaption>Splitting of the 3d orbitals by the ligands. In an octahedral complex there are three lower orbitals and two higher ones. In a tetrahedral complex it is the other way round, with two lower and three higher, and the gap ΔE is smaller. The dashed lines show the free-ion energy.</figcaption></figure>
:::

:::warn Do not turn the octahedral diagram upside down
Octahedral: **two up, three down**. Tetrahedral: **three up, two down**. A common slip is to draw them the wrong way round, or to draw the tetrahedral gap larger than the octahedral one.
:::

### Promoting an electron

In a complex with a partly filled d sub-shell, an electron in a lower orbital can absorb a photon whose energy exactly matches \(\Delta E\) and be **promoted** to a vacant place in the higher set. The light of that frequency is removed from the white light that passes through the solution, so the solution shows the complementary colour.

:::html
<figure class="fig small"><svg viewBox="0 0 340 165" role="img" aria-label="Promotion of an electron: an electron in a lower d orbital absorbs light and moves to an empty place in a higher d orbital, with an energy gap delta E equal to h times f"><text class="tl" x="2" y="14">energy</text><path class="ax" d="M10 150L10 24" marker-end="url(#ahm)"/><path class="ln thick" d="M150 50L170 50"/><path class="ln thick" d="M176 50L196 50"/><path class="ln thick" d="M150 130L170 130"/><path class="ln thick" d="M176 130L196 130"/><path class="ln thick" d="M202 130L222 130"/><text class="tl" x="204" y="54">higher set</text><text class="tl" x="230" y="134">lower set</text><path class="c1 sw2" d="M160 127L160 106" marker-end="url(#ahs-red)"/><path class="c1 sw2 dash" d="M160 47L160 26" marker-end="url(#ahs-red)"/><path class="ln" d="M130 122L130 52" marker-end="url(#ah)"/><text class="tl" x="122" y="94" text-anchor="end">promotion</text><path class="c3 sw2" d="M36 52Q41.7 58 47.3 52Q53 46 58.7 52Q64.3 58 70 52Q75.7 46 81.3 52Q87 58 92.7 52Q98.3 46 104 52" marker-end="url(#ah)"/><text class="tl" x="36" y="33">light absorbed</text><text class="tl" x="36" y="76">ΔE = hf</text></svg><figcaption>A photon with energy ΔE = hf is absorbed and an electron moves from the lower set to a vacant place in the higher set. The dashed arrow shows where the electron ends up.</figcaption></figure>
:::

:::key Colour of a complex ion
1. The ligands split the d orbitals into two sets with an energy gap \(\Delta E\).
2. An electron in the lower set absorbs light of frequency \(f = \Delta E / h\) and is promoted to the higher set.
3. The colour you see is the **complementary colour** of the light absorbed.
:::

:::warn Absorption, not emission
The electron does not "fall back and emit blue light". The colour is what is *left* of the white light after the absorbed frequency has been taken out. A solution that looks blue is absorbing red and orange light.
:::

### Which ions are coloured?

Promotion needs an electron in the lower set **and** a vacant place in the higher set. A 3d⁰ ion has no d electrons to promote. A 3d¹⁰ ion has every d orbital full, so there is nowhere to promote to. Both are colourless, and the usual examples are \(\ce{Sc^3+}\) (d⁰), \(\ce{Zn^2+}\) (d¹⁰) and \(\ce{Cu+}\) (d¹⁰, as in the white precipitate of CuI). Every ion from d¹ to d⁹ is able to absorb in this way and is normally coloured.

| Ion | d electrons | Coloured? |
|---|---|---|
| \(\ce{Sc^3+}\) | 0 | no |
| \(\ce{Ti^3+}\) | 1 | yes |
| \(\ce{Cr^3+}\) | 3 | yes |
| \(\ce{Fe^3+}\) | 5 | yes |
| \(\ce{Cu^2+}\) | 9 | yes |
| \(\ce{Cu+}\) | 10 | no |
| \(\ce{Zn^2+}\) | 10 | no |

:::html
<div class="widget" data-w="chem-dsplit" data-geom="oct" data-ion="Cu2+" data-ligand="H2O"></div>
:::

Try these in order: copper(II) with water, then ammonia (the gap rises), then cyanide; switch to tetrahedral with chloride (a smaller gap); repeat with cobalt(II); then pick \(\ce{Zn^2+}\) and \(\ce{Sc^3+}\), which show no colour. The widget names the colour seen only for the copper(II) and cobalt(II) complexes of this chapter. For other ions it shows only whether higher- or lower-frequency light is absorbed, because the real colour depends on the metal ion and its charge as well as on the ligand.

:::eg Explain why the aqueous copper(II) ion, \(\ce{[Cu(H2O)6]^2+}\), is blue. [4 marks]
The six water ligands split the 3d orbitals of the \(\ce{Cu^2+}\) ion (3d⁹) into two sets with an energy gap \(\Delta E\): three lower and two higher orbitals. [B1]

An electron in the lower set absorbs light whose energy matches the gap, \(\Delta E = hf\), and is promoted to the vacant place in the higher set. [B1]

The light absorbed is in the red-orange region. [B1]

The light that is not absorbed is transmitted, and its colour, the complementary colour of the light absorbed, is blue. [B1]
:::

:::eg Explain why aqueous zinc(II) ions are colourless. [2 marks]
\(\ce{Zn^2+}\) is [Ar] 3d¹⁰, so the 3d sub-shell is full. [B1]

There is no vacant place in the higher set, so no electron can be promoted by absorbing visible light and no frequency of visible light is absorbed. [B1]
:::

### Different ligands, different colours

The size of \(\Delta E\) depends on the ligand, on the shape of the complex and on the metal ion with its oxidation state. If a ligand exchange changes any of these, \(\Delta E\) changes, so a **different frequency is absorbed** and a **different colour is seen**.

For the ligands in this chapter, \(\Delta E\) increases in the order

\[\ce{Cl-} < \ce{H2O} < \ce{NH3} < \ce{CN-}\]

and a larger \(\Delta E\) means higher-frequency light is absorbed. In the same way, a tetrahedral complex has a smaller gap than the octahedral complex of the same ion, so it absorbs lower-frequency light.

| Ligand exchange | Colour change | What changes |
|---|---|---|
| \(\ce{[Cu(H2O)6]^2+ -> [Cu(NH3)4(H2O)2]^2+}\) | blue to dark blue | ligand: ammonia gives a larger \(\Delta E\) than water, so higher-frequency light is absorbed |
| \(\ce{[Cu(H2O)6]^2+ -> [CuCl4]^2-}\) | blue to yellow-green | ligand and shape (octahedral to tetrahedral) |
| \(\ce{[Co(H2O)6]^2+ -> [CoCl4]^2-}\) | pink to blue | ligand and shape (octahedral to tetrahedral): a smaller gap, so lower-frequency light is absorbed |
| \(\ce{[Co(H2O)6]^2+ -> [Co(NH3)6]^2+}\) | pink to brown | ligand: ammonia gives a different \(\Delta E\) |

The same metal in different oxidation states also gives different colours, because the number of d electrons and the charge of the ion change the gap. Vanadium in [Transition elements](#chem.transition) is the clearest case: yellow, blue, green and violet for +5, +4, +3 and +2.

:::eg (Exam style) Explain why the colour changes from pink to blue when concentrated hydrochloric acid is added to aqueous cobalt(II) ions. [4 marks]
Chloride ions replace the water ligands in a ligand exchange: \(\ce{[Co(H2O)6]^2+ + 4Cl- <=> [CoCl4]^2- + 6H2O}\). [B1]

The complex changes from octahedral to tetrahedral. [B1]

The splitting of the d orbitals is smaller in the tetrahedral complex, so \(\Delta E\) is different and a different (lower) frequency of light is absorbed. [B1]

The colour seen is the complementary colour of the new light absorbed, so the solution is blue instead of pink. [B1]
:::

:::eg Spot the error: explain why aqueous copper(II) sulfate is blue. [3 marks]
A student wrote this answer.

Line 1: The water ligands split the d orbitals into two sets with an energy gap.
Line 2: An electron absorbs light of energy \(\Delta E = hf\) and is promoted from a lower to a higher d orbital.
Line 3: The solution is blue because it absorbs blue light.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: a solution looks the colour of the light it transmits, not the light it absorbs. A blue solution absorbs red-orange light and transmits blue. The last mark is lost [B0].**

Correct line 3: red-orange light is absorbed, and the complementary colour, blue, is transmitted. [B1]

The student scores 2 out of 3. Always say which colour is absorbed and that the colour seen is the complementary colour.
:::

## Stereoisomerism in complexes

Stereoisomers have the same structural formula but a different arrangement of atoms in space ([Isomerism](#chem.org.isomerism)). Complex ions show the same two kinds as organic molecules: cis/trans (geometrical) isomerism and optical isomerism.

### Cis/trans isomerism

The idea is the same as for alkenes. In the **cis** isomer two identical ligands are next to each other (adjacent, at 90°); in the **trans** isomer they are on opposite sides (180° apart).

**Square planar.** \(\ce{[Pt(NH3)2Cl2]}\) has two isomers. In the cis isomer the two chloride ligands (and the two ammonia ligands) are adjacent. In the trans isomer each ligand has its twin opposite.

:::html
<figure class="fig small"><svg viewBox="0 10 340 150" role="img" aria-label="Two square planar isomers of the platinum complex with two ammonia and two chloride ligands. In the trans isomer the ammonia ligands are on opposite corners of the square. In the cis isomer the two ammonia ligands are on adjacent corners"><text class="tl tc" x="85" y="65.5">Pt</text><text class="tl tc" x="38.8" y="24.7">H₃N</text><path class="ln thick" d="M73.1 51.5L51 32"/><text class="tl tc" x="130.6" y="25.2">Cl</text><path class="ln thick" d="M96.9 51.5L119 32"/><text class="tl tc" x="39.4" y="105.8">Cl</text><path class="ln thick" d="M73.1 72.5L51 92"/><text class="tl tc" x="131.2" y="106.3">NH₃</text><path class="ln thick" d="M96.9 72.5L119 92"/><text class="tl tc" x="255" y="65.5">Pt</text><text class="tl tc" x="208.8" y="24.7">H₃N</text><path class="ln thick" d="M243.1 51.5L221 32"/><text class="tl tc" x="301.2" y="24.7">NH₃</text><path class="ln thick" d="M266.9 51.5L289 32"/><text class="tl tc" x="209.4" y="105.8">Cl</text><path class="ln thick" d="M243.1 72.5L221 92"/><text class="tl tc" x="300.6" y="105.8">Cl</text><path class="ln thick" d="M266.9 72.5L289 92"/><text class="tl tc" x="85" y="138">trans</text><text class="tl tc" x="255" y="138">cis</text></svg><figcaption>The two isomers of the square planar complex [Pt(NH₃)₂Cl₂]. In the trans isomer, identical ligands are on opposite corners. In the cis isomer, they are on adjacent corners. All five atoms lie in one plane.</figcaption></figure>
:::

The cis isomer is **cisplatin**, an anticancer drug. It enters cells, where a chloride ligand is replaced by water, and the platinum then binds to DNA and stops cancer cells from dividing. The trans isomer does not bind to DNA in the same way and is not used as the drug.

**Octahedral.** \(\ce{[Co(NH3)4(H2O)2]^2+}\) also has two isomers. Place the two water ligands on opposite corners of the octahedron (trans) or on adjacent corners (cis). The same is true of \(\ce{[Ni(en)2(H2O)2]^2+}\), where each en spans two adjacent positions.

:::html
<figure class="fig small"><svg viewBox="0 25 340 170" role="img" aria-label="Trans and cis isomers of the octahedral cobalt complex with four ammonia and two water ligands. In the trans isomer the two water ligands are at the top and bottom. In the cis isomer the two water ligands are at the top and on the right"><text class="tl tc" x="85" y="95.5">Co</text><text class="tl tc" x="85" y="38.5">H₂O</text><path class="ln thick" d="M85 79.5L85 48"/><text class="tl tc" x="85" y="152.5">H₂O</text><path class="ln thick" d="M85 104.5L85 136"/><text class="tl tc" x="148" y="95.5">NH₃</text><path class="ln thick" d="M99.2 92L129 92"/><text class="tl tc" x="22" y="95.5">NH₃</text><path class="ln thick" d="M70.8 92L41 92"/><text class="tl tc" x="44.5" y="130.2">NH₃</text><path class="fi" d="M72.9 102.4L54.7 113.3L59.3 118.7Z"/><text class="tl tc" x="125.5" y="60.8">NH₃</text><path class="ln" d="M101.2 80.1L99.2 77.8M104.6 77.8L102 74.8M108 75.6L104.7 71.8M111.4 73.3L107.5 68.8M114.8 71.1L110.2 65.8"/><text class="tl tc" x="255" y="95.5">Co</text><text class="tl tc" x="255" y="38.5">H₂O</text><path class="ln thick" d="M255 79.5L255 48"/><text class="tl tc" x="255" y="152.5">NH₃</text><path class="ln thick" d="M255 104.5L255 136"/><text class="tl tc" x="318" y="95.5">H₂O</text><path class="ln thick" d="M269.2 92L299 92"/><text class="tl tc" x="192" y="95.5">NH₃</text><path class="ln thick" d="M240.8 92L211 92"/><text class="tl tc" x="214.5" y="130.2">NH₃</text><path class="fi" d="M242.9 102.4L224.7 113.3L229.3 118.7Z"/><text class="tl tc" x="295.5" y="60.8">NH₃</text><path class="ln" d="M271.2 80.1L269.2 77.8M274.6 77.8L272 74.8M278 75.6L274.7 71.8M281.4 73.3L277.5 68.8M284.8 71.1L280.2 65.8"/><text class="tl tc" x="85" y="180">trans</text><text class="tl tc" x="255" y="180">cis</text></svg><figcaption>The trans and cis isomers of [Co(NH₃)₄(H₂O)₂]²⁺. In the trans isomer the two water ligands are opposite each other (180° apart). In the cis isomer they are adjacent (90° apart). A wedge points towards you and a hashed bond points away.</figcaption></figure>
:::

**Tetrahedral complexes cannot show cis/trans isomerism.** In a tetrahedron every ligand is next to every other (all angles are 109.5°), so there is no "opposite" arrangement.

### Optical isomerism

A complex is chiral if its mirror image cannot be superposed on it. Then there are two **optical isomers** (enantiomers), which rotate the plane of plane-polarised light in opposite directions (see [Isomerism](#chem.org.isomerism)). In complexes the cause is not a carbon with four different groups but the way bidentate ligands wrap round the metal ion like the blades of a propeller.

Two complexes in the syllabus are chiral:

- \(\ce{[Ni(en)3]^2+}\): three en ligands arranged round the nickel ion give two mirror-image forms.
- the **cis** isomer of \(\ce{[Ni(en)2(H2O)2]^2+}\). The trans isomer has a plane of symmetry and is not chiral.

:::html
<figure class="fig small"><svg viewBox="0 0 340 430" role="img" aria-label="Two pairs of mirror-image complexes either side of a dashed mirror line. Top: the two optical isomers of the nickel complex with three 1,2-diaminoethane ligands; each ligand is a curved line joining two nitrogen atoms bonded to nickel. Bottom: the two optical isomers of the cis nickel complex with two 1,2-diaminoethane ligands and two water ligands"><text class="tl tc" x="82" y="96.5">Ni</text><path class="ln" d="M82 81L82 45"/><text class="tl tc" x="82" y="40.5">N</text><path class="ln" d="M90.9 83.9L89.5 82.6M94.4 81L92.2 78.9M97.8 78.1L94.8 75.3M101.3 75.2L97.5 71.7M104.7 72.3L100.2 68.1M108.1 69.4L102.9 64.5"/><text class="tl tc" x="112" y="64.5">N</text><path class="ln thick" d="M91.3 32.3Q104.1 27 109.7 50.3"/><path class="ln" d="M68 92L35.5 92"/><text class="tl tc" x="26" y="96.5">N</text><path class="fi" d="M73.8 100.8L55.9 114.7L61.1 119.5Z"/><text class="tl tc" x="52" y="128.5">N</text><path class="ln thick" d="M22.6 101.4Q17.1 116.1 42.2 121.8"/><path class="ln" d="M96 92L128.5 92"/><text class="tl tc" x="138" y="96.5">N</text><path class="ln" d="M82 103L82 139"/><text class="tl tc" x="82" y="152.5">N</text><path class="ln thick" d="M138 102Q137.8 147.8 92 148"/><text class="tl tc" x="258" y="96.5">Ni</text><path class="ln" d="M258 81L258 45"/><text class="tl tc" x="258" y="40.5">N</text><path class="ln" d="M250.5 82.6L249.1 83.9M247.8 78.9L245.6 81M245.2 75.3L242.2 78.1M242.5 71.7L238.7 75.2M239.8 68.1L235.3 72.3M237.1 64.5L231.9 69.4"/><text class="tl tc" x="228" y="64.5">N</text><path class="ln thick" d="M248.7 32.3Q235.9 27 230.3 50.3"/><path class="ln" d="M272 92L304.5 92"/><text class="tl tc" x="314" y="96.5">N</text><path class="fi" d="M266.2 100.8L278.9 119.5L284.1 114.7Z"/><text class="tl tc" x="288" y="128.5">N</text><path class="ln thick" d="M317.4 101.4Q322.9 116.1 297.8 121.8"/><path class="ln" d="M244 92L211.5 92"/><text class="tl tc" x="202" y="96.5">N</text><path class="ln" d="M258 103L258 139"/><text class="tl tc" x="258" y="152.5">N</text><path class="ln thick" d="M202 102Q202.2 147.8 248 148"/><path class="ln-m thin dash" d="M170 14V162"/><text class="tl tc" x="170" y="180">mirror</text><text class="tl tc" x="82" y="204">[Ni(en)₃]²⁺</text><text class="tl tc" x="258" y="204">[Ni(en)₃]²⁺</text><text class="tl tc" x="82" y="306.5">Ni</text><path class="ln" d="M68 302L35.5 302"/><text class="tl tc" x="26" y="306.5">N</text><path class="fi" d="M73.8 310.8L55.9 324.7L61.1 329.5Z"/><text class="tl tc" x="52" y="338.5">N</text><path class="ln thick" d="M22.6 311.4Q17.1 326.1 42.2 331.8"/><path class="ln" d="M96 302L128.5 302"/><text class="tl tc" x="138" y="306.5">N</text><path class="ln" d="M82 313L82 349"/><text class="tl tc" x="82" y="362.5">N</text><path class="ln thick" d="M138 312Q137.8 357.8 92 358"/><path class="ln" d="M82 291L82 255"/><text class="tl tc" x="82" y="250.5">H₂O</text><path class="ln" d="M90.9 293.9L89.5 292.6M93.2 292.3L91 290.2M95.5 290.6L92.5 287.8M97.8 288.9L94 285.4M100 287.3L95.5 283M102.3 285.6L97.1 280.7"/><text class="tl tc" x="112" y="274.5">H₂O</text><text class="tl tc" x="258" y="306.5">Ni</text><path class="ln" d="M272 302L304.5 302"/><text class="tl tc" x="314" y="306.5">N</text><path class="fi" d="M266.2 310.8L278.9 329.5L284.1 324.7Z"/><text class="tl tc" x="288" y="338.5">N</text><path class="ln thick" d="M317.4 311.4Q322.9 326.1 297.8 331.8"/><path class="ln" d="M244 302L211.5 302"/><text class="tl tc" x="202" y="306.5">N</text><path class="ln" d="M258 313L258 349"/><text class="tl tc" x="258" y="362.5">N</text><path class="ln thick" d="M202 312Q202.2 357.8 248 358"/><path class="ln" d="M258 291L258 255"/><text class="tl tc" x="258" y="250.5">H₂O</text><path class="ln" d="M250.5 292.6L249.1 293.9M249 290.2L246.8 292.3M247.5 287.8L244.5 290.6M246 285.4L242.2 288.9M244.5 283L240 287.3M242.9 280.7L237.7 285.6"/><text class="tl tc" x="228" y="274.5">H₂O</text><path class="ln-m thin dash" d="M170 224V372"/><text class="tl tc" x="170" y="390">mirror</text><text class="tl tc" x="82" y="414">cis-[Ni(en)₂(H₂O)₂]²⁺</text><text class="tl tc" x="258" y="414">cis-[Ni(en)₂(H₂O)₂]²⁺</text></svg><figcaption>Each pair of complexes is a mirror image across the dashed line, and the two cannot be placed on top of each other. Each curved line is one 1,2-diaminoethane ligand joining its two nitrogen atoms, N, which both bond to the nickel ion. The wedge bond points towards you and the hashed bond points away. Top: [Ni(en)₃]²⁺. Bottom: cis-[Ni(en)₂(H₂O)₂]²⁺, with the two water ligands adjacent.</figcaption></figure>
:::

Try turning one of the pair in your mind: you cannot make it match the other, just as a left hand cannot become a right hand by turning it.

:::eg Is cis-\(\ce{[Ni(en)2(H2O)2]^2+}\) chiral? Is the trans isomer?
In the cis isomer the two water ligands are adjacent. The two en ligands then wrap round the nickel ion in a twisted, propeller-like arrangement, and its mirror image cannot be superposed on it. The cis isomer is chiral and exists as two optical isomers.

In the trans isomer the water ligands are opposite each other and the two en ligands lie in one plane. That plane is a plane of symmetry, so the mirror image is the same as the original. The trans isomer is not chiral.
:::

:::eg Describe the stereoisomerism of \(\ce{[Co(NH3)4(H2O)2]^2+}\). [3 marks]
Two geometrical (cis/trans) isomers exist. [B1]

In the trans isomer the two water ligands are opposite each other, 180° apart. [B1]

In the cis isomer the two water ligands are adjacent, 90° apart. [B1]

Neither is chiral, because neither lacks a plane of symmetry: there are no optical isomers.
:::

### Polarity

A polar molecule has an overall dipole, because the individual bond dipoles do not cancel. For the neutral platinum complex:

- **cis-**\(\ce{[Pt(NH3)2Cl2]}\): the two Pt–Cl dipoles point to one side and the two Pt–N dipoles to the other, so they do not cancel. The molecule is **polar**.
- **trans-**\(\ce{[Pt(NH3)2Cl2]}\): each dipole is cancelled by the identical one directly opposite. The molecule is **non-polar**.

The polar cis isomer dissolves better in water, a polar solvent. The same reasoning applies to the octahedral ions. In trans-\(\ce{[Co(NH3)4(H2O)2]^2+}\) the two opposite water ligands cancel and the four ammonia ligands cancel, so there is no overall dipole from the ligands. In the cis isomer the dipoles do not cancel.

:::eg (Exam style) Cisplatin and transplatin are the cis and trans isomers of \(\ce{[Pt(NH3)2Cl2]}\). Draw the structure of each, and state which is polar and why. [4 marks]
Both are square planar, with platinum at the centre and the four ligands at the corners of a square. [B1]

Cisplatin: the two Cl are on adjacent corners, and the two \(\ce{NH3}\) are on the other two adjacent corners. [B1]

Transplatin: each Cl is opposite the other Cl and each \(\ce{NH3}\) opposite the other \(\ce{NH3}\). [B1]

Cisplatin is polar, because the dipoles of the two Pt–Cl bonds are on the same side and do not cancel. Transplatin is non-polar, because the opposite dipoles cancel. [B1]
:::

## Stability constants

Ligand exchange reactions are equilibria, so they have equilibrium constants. For the **formation** of a complex ion the constant has a special name.

:::def Stability constant, Kstab
The equilibrium constant for the formation of a complex ion in a solvent from its constituent ions or molecules.
:::

Take the formation of the ammine complex from the aqua ion in water:

\[\ce{[Cu(H2O)6]^2+ + 4NH3 <=> [Cu(NH3)4(H2O)2]^2+ + 4H2O}\]

The expression for \(K_{\text{stab}}\) is

\[K_{\text{stab}} = \frac{[\ce{[Cu(NH3)4(H2O)2]^2+}]}{[\ce{[Cu(H2O)6]^2+}]\,[\ce{NH3}]^4}\]

Water is **left out**. It is the solvent, present in a huge excess, so its concentration is effectively constant and is absorbed into the constant (the same convention as for \(K_c\) in a solution; see [Chemical equilibria](#chem.equilibria)). The units follow from the expression: here \(\mathrm{mol^{-4}\,dm^{12}}\).

:::key Stability constant: how to use it
- Write the expression as [complex] over [metal ion in solution] × [free ligand] raised to its coefficient. Leave out \(\ce{H2O}\) as solvent.
- The **larger** \(K_{\text{stab}}\), the more the equilibrium lies towards the complex, so the **more stable** the complex.
- If two ligands compete for a metal ion, the ligand that forms the complex with the larger \(K_{\text{stab}}\) replaces the other.
:::

:::eg Write the expression for \(K_{\text{stab}}\), with units, for \(\ce{[Co(H2O)6]^2+ + 4Cl- <=> [CoCl4]^2- + 6H2O}\).
\[K_{\text{stab}} = \frac{[\ce{[CoCl4]^2-}]}{[\ce{[Co(H2O)6]^2+}]\,[\ce{Cl-}]^4}\]
Water is omitted. The units are \(\mathrm{mol\,dm^{-3}} \div (\mathrm{mol\,dm^{-3}} \times (\mathrm{mol\,dm^{-3}})^4) = \mathrm{mol^{-4}\,dm^{12}}\).
:::

Some typical stability constants are below. They are rounded, and data books differ in the second figure, so treat them as data for the questions in this chapter: an exam question always gives the values it needs.

| Complex ion | \(K_{\text{stab}}\) | Units |
|---|---|---|
| \(\ce{[Ag(NH3)2]+}\) | \(1.6 \times 10^{7}\) | \(\mathrm{mol^{-2}\,dm^{6}}\) |
| \(\ce{[Ag(S2O3)2]^3-}\) | \(2.9 \times 10^{13}\) | \(\mathrm{mol^{-2}\,dm^{6}}\) |
| \(\ce{[Cu(NH3)4(H2O)2]^2+}\) | \(1.1 \times 10^{13}\) | \(\mathrm{mol^{-4}\,dm^{12}}\) |
| \(\ce{[Cu(EDTA)]^2-}\) | \(6.3 \times 10^{18}\) | \(\mathrm{mol^{-1}\,dm^{3}}\) |

### Calculations

Three kinds of calculation appear: finding a concentration, finding \(K_{\text{stab}}\), and comparing complexes.

:::eg (Exam style) A solution contains \(\ce{[Cu(NH3)4(H2O)2]^2+}\) at 0.0100 mol dm⁻³ with free ammonia at 0.960 mol dm⁻³. \(K_{\text{stab}} = 1.1 \times 10^{13}\ \mathrm{mol^{-4}\,dm^{12}}\). Calculate the concentration of free \(\ce{[Cu(H2O)6]^2+}\). [3 marks]
\[K_{\text{stab}} = \frac{[\ce{[Cu(NH3)4(H2O)2]^2+}]}{[\ce{[Cu(H2O)6]^2+}]\,[\ce{NH3}]^4}\] [B1]
Rearrange for the unknown:
\[[\ce{[Cu(H2O)6]^2+}] = \frac{0.0100}{1.1 \times 10^{13} \times 0.960^4}\] [M1]
\[= 1.07 \times 10^{-15}\,\mathrm{mol\,dm^{-3}}\] [A1]

The free copper(II) ion is almost absent: the ammonia has taken it into the complex.
:::

:::eg (Exam style) At equilibrium a solution contains \(\ce{[Cu(NH3)4(H2O)2]^2+}\) at \(2.50 \times 10^{-3}\) mol dm⁻³, \(\ce{[Cu(H2O)6]^2+}\) at \(1.4 \times 10^{-13}\) mol dm⁻³ and \(\ce{NH3}\) at 0.200 mol dm⁻³. Calculate \(K_{\text{stab}}\) with its units. [3 marks]
\[K_{\text{stab}} = \frac{2.50 \times 10^{-3}}{1.4 \times 10^{-13} \times 0.200^4}\] [M1]
\[= 1.1 \times 10^{13}\] [A1]
Units: \(\mathrm{mol^{-4}\,dm^{12}}\). [B1]
:::

### Which ligand wins?

Suppose a ligand L′ is added to a complex of ligand L. The exchange is

\[\ce{[ML] + L' <=> [ML'] + L}\]

and its equilibrium constant is the ratio \(K_{\text{stab}}(\ce{ML'}) \div K_{\text{stab}}(\ce{ML})\). If the new complex has the larger \(K_{\text{stab}}\), that ratio is greater than 1 and the exchange goes ahead.

:::eg (Real context) In black-and-white photography the unused silver bromide on the film is removed by thiosulfate ions ("fixing"). Use \(K_{\text{stab}}\) values to show that thiosulfate ions replace ammonia in the silver complex, and calculate the equilibrium constant for \(\ce{[Ag(NH3)2]+ + 2S2O3^2- <=> [Ag(S2O3)2]^3- + 2NH3}\).
\(K_{\text{stab}}\) for \(\ce{[Ag(S2O3)2]^3-}\) is \(2.9 \times 10^{13}\) and for \(\ce{[Ag(NH3)2]+}\) it is \(1.6 \times 10^{7}\). The thiosulfate complex has the larger \(K_{\text{stab}}\), so it is the more stable and thiosulfate replaces ammonia.

The equilibrium constant of the exchange is the ratio:
\[K = \frac{2.9 \times 10^{13}}{1.6 \times 10^{7}} = 1.8 \times 10^{6}\]
which is far greater than 1, so the exchange goes almost to completion.
:::

### Why are chelates so stable?

EDTA⁴⁻ forms very stable complexes: \(K_{\text{stab}}\) for \(\ce{[Cu(EDTA)]^2-}\) is \(6.3 \times 10^{18}\), a factor of about \(5.7 \times 10^{5}\) larger than for the ammine complex. Compare the two reactions starting from the aqua ion:

\[\ce{[Cu(H2O)6]^2+ + 4NH3 <=> [Cu(NH3)4(H2O)2]^2+ + 4H2O}\]
\[\ce{[Cu(H2O)6]^2+ + EDTA^4- <=> [Cu(EDTA)]^2- + 6H2O}\]

In the first reaction, 5 particles on the left give 5 on the right: the number of particles hardly changes. In the second, **2 particles on the left give 7 on the right**, because one EDTA ion replaces six water molecules, and six water molecules go free. More particles means more disorder, so the entropy change \(\Delta S\) is **positive**. The enthalpy change is small, because dative bonds from the donor atoms of EDTA replace six similar dative bonds from water. In \(\Delta G = \Delta H - T\Delta S\) a positive \(\Delta S\) makes \(\Delta G\) more negative, so the reaction is more favourable and \(K_{\text{stab}}\) is larger (see [Lattice energy, entropy and Gibbs free energy](#chem.lattice)).

The same applies, less strongly, to a bidentate ligand: each en replaces two water molecules. This is the **chelate effect**.

:::eg (Exam style) Explain why the complex \(\ce{[Cu(EDTA)]^2-}\) forms in preference to \(\ce{[Cu(NH3)4(H2O)2]^2+}\) when EDTA⁴⁻ is added to an ammonia complex of copper(II). [4 marks]
\[\ce{[Cu(NH3)4(H2O)2]^2+ + EDTA^4- <=> [Cu(EDTA)]^2- + 4NH3 + 2H2O}\] [B1]
The \(K_{\text{stab}}\) of the EDTA complex (\(6.3 \times 10^{18}\)) is much larger than that of the ammine complex (\(1.1 \times 10^{13}\)), so the EDTA complex is more stable. [B1]
One EDTA ion replaces six ligands (4 ammonia and 2 water molecules), so the number of particles increases from 2 to 7. [B1]
The entropy increases, \(\Delta G\) becomes more negative and the equilibrium lies to the right. [B1]
:::

:::exam Stability constants in the exam
Write the \(K_{\text{stab}}\) expression without water. Give the units (work them out from the expression). To predict an exchange, compare the two \(K_{\text{stab}}\) values and say "the complex with the larger \(K_{\text{stab}}\) is more stable". For EDTA and en, add the entropy argument: more particles formed, positive \(\Delta S\).
:::

:::try Start easy, finish at exam standard
Q: Which of these ions would you expect to be colourless: \(\ce{Sc^3+}\), \(\ce{Ti^3+}\), \(\ce{Mn^2+}\), \(\ce{Cu+}\), \(\ce{Ni^2+}\)? Explain.
A: \(\ce{Sc^3+}\) is 3d⁰ and \(\ce{Cu+}\) is 3d¹⁰. Neither can have an electron promoted between d orbitals, so both are colourless. \(\ce{Ti^3+}\) (d¹), \(\ce{Mn^2+}\) (d⁵) and \(\ce{Ni^2+}\) (d⁸) have partly filled d sub-shells and are coloured.
Q: A complex absorbs yellow light. What colour does it appear?
A: Violet, the complementary colour of yellow.
Q: Sketch the splitting of the d orbitals in a tetrahedral complex and say how it differs from octahedral.
A: Five degenerate levels split into three higher orbitals and two lower orbitals, with a gap \(\Delta E\) smaller than in the octahedral complex, which has two higher and three lower.
Q: State two things that, when changed, alter the colour of a complex of a given metal ion.
A: The ligand (a different \(\Delta E\)) and the shape of the complex (octahedral or tetrahedral). The oxidation state of the metal also changes it.
Q: Draw the isomers of \(\ce{[Pt(NH3)2Cl2]}\) and name the type of isomerism.
A: Cis and trans square planar isomers (see the figure): geometrical isomerism. In cis the two Cl are on adjacent corners of the square; in trans they are on opposite corners.
Q: Why can \(\ce{[CuCl4]^2-}\) not show cis/trans isomerism?
A: It is tetrahedral. Every ligand is adjacent to every other, with no pair of opposite positions.
Q: Write the \(K_{\text{stab}}\) expression for \(\ce{[Ag(NH3)2]+}\) formed from \(\ce{Ag+(aq)}\) and ammonia, with units.
A: \(K_{\text{stab}} = \dfrac{[\ce{[Ag(NH3)2]+}]}{[\ce{Ag+}]\,[\ce{NH3}]^2}\) with units \(\mathrm{mol^{-2}\,dm^{6}}\).
Q: \(K_{\text{stab}}\) for \(\ce{[Ag(NH3)2]+}\) is \(1.6 \times 10^{7}\ \mathrm{mol^{-2}\,dm^{6}}\). A solution has \([\ce{[Ag(NH3)2]+}] = 0.00500\) and \([\ce{NH3}] = 0.490\) mol dm⁻³. Calculate \([\ce{Ag+}]\).
A: \([\ce{Ag+}] = \dfrac{0.00500}{1.6 \times 10^{7} \times 0.490^2} = 1.30 \times 10^{-9}\) mol dm⁻³.
Q: The complex \(\ce{[Fe(H2O)6]^2+}\) is pale green, and \(\ce{[Fe(CN)6]^4-}\) is yellow. Explain why the colours differ.
A: The ligands differ, and cyanide gives a larger \(\Delta E\) than water, so the complexes absorb different frequencies of light and show different complementary colours.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Which of the ions \(\ce{Sc^3+}\), \(\ce{Ti^3+}\), \(\ce{Zn^2+}\) and \(\ce{Cu^2+}\) are colourless? Explain.
A: \(\ce{Sc^3+}\) and \(\ce{Zn^2+}\) are colourless. [B1] \(\ce{Sc^3+}\) is 3d⁰: no d electrons to promote. \(\ce{Zn^2+}\) is 3d¹⁰: no vacant d place to promote an electron to. [B1] \(\ce{Ti^3+}\) (3d¹) and \(\ce{Cu^2+}\) (3d⁹) have partly filled 3d sub-shells, so electrons can be promoted and they are coloured. [B1]
Q: [3 marks] ★ In an octahedral complex the five d orbitals are split into two sets. State how many orbitals are in each set and which is higher, and explain how this leads to colour.
A: Two orbitals in the higher set and three in the lower set. [B1] An electron in the lower set absorbs light of frequency \(f = \Delta E / h\) and is promoted to the higher set. [B1] The colour seen is the complementary colour of the light absorbed. [B1]
Q: [4 marks] ★★ Aqueous copper(II) ions are blue. When excess ammonia is added the solution turns dark blue. Explain this change.
A: Ammonia replaces water ligands in a ligand exchange, forming \(\ce{[Cu(NH3)4(H2O)2]^2+}\). [B1] The ligands are different, so the splitting \(\Delta E\) of the d orbitals changes. [B1] A different frequency of light is absorbed. [B1] The complementary colour seen is a different (deeper) blue. [B1]
Q: [4 marks] ★★ Describe the isomerism of the square planar complex \(\ce{[Pt(NH3)2Cl2]}\), and state which isomer is polar.
A: Geometrical (cis/trans) isomerism. [B1] In the cis isomer the two Cl ligands are adjacent. In the trans isomer they are opposite. [B1] The cis isomer is polar, because the bond dipoles do not cancel. [B1] In the trans isomer the dipoles cancel, so it is non-polar. [B1]
Q: [3 marks] ★★ Explain why \(\ce{[Ni(en)3]^2+}\) has optical isomers but \(\ce{[Ni(NH3)6]^2+}\) does not.
A: The three bidentate en ligands wrap round the nickel ion in a propeller-like arrangement. [B1] The structure and its mirror image cannot be superposed, so it is chiral and has two optical isomers. [B1] In \(\ce{[Ni(NH3)6]^2+}\) the six identical monodentate ligands give a symmetrical octahedron that is identical to its mirror image. [B1]
Q: [5 marks] ★★ \(K_{\text{stab}}\) for \(\ce{[Cu(NH3)4(H2O)2]^2+}\) is \(1.1 \times 10^{13}\) mol⁻⁴ dm¹². A solution contains this complex at 0.0200 mol dm⁻³ and free ammonia at 0.500 mol dm⁻³. (a) Write the \(K_{\text{stab}}\) expression. (b) Calculate the concentration of \(\ce{[Cu(H2O)6]^2+}\).
H: Rearrange the expression to make \([\ce{[Cu(H2O)6]^2+}]\) the subject.
A: (a) \(K_{\text{stab}} = \dfrac{[\ce{[Cu(NH3)4(H2O)2]^2+}]}{[\ce{[Cu(H2O)6]^2+}][\ce{NH3}]^4}\) [B1] with no \([\ce{H2O}]\). [B1]
(b) \([\ce{[Cu(H2O)6]^2+}] = \dfrac{0.0200}{1.1 \times 10^{13} \times 0.500^4}\) [M1] \(= \dfrac{0.0200}{6.875 \times 10^{11}}\) [M1] \(= 2.9 \times 10^{-14}\) mol dm⁻³ [A1]
Q: [4 marks] ★★ At equilibrium a solution contains \(\ce{[Ag(NH3)2]+}\) at 0.0400 mol dm⁻³, \(\ce{Ag+}\) at \(2.5 \times 10^{-8}\) mol dm⁻³ and \(\ce{NH3}\) at 0.300 mol dm⁻³. Calculate \(K_{\text{stab}}\), with units.
A: \(K_{\text{stab}} = \dfrac{[\ce{[Ag(NH3)2]+}]}{[\ce{Ag+}][\ce{NH3}]^2}\) [B1] \(= \dfrac{0.0400}{2.5 \times 10^{-8} \times 0.300^2}\) [M1] \(= 1.8 \times 10^{7}\) [A1] mol⁻² dm⁶. [B1]
Q: [6 marks] ★★★ EDTA⁴⁻ is added to a solution of \(\ce{[Cu(NH3)4(H2O)2]^2+}\). (a) Write the equation for the reaction. (b) Calculate the equilibrium constant for the exchange, given \(K_{\text{stab}}\) of \(\ce{[Cu(EDTA)]^2-}\) is \(6.3 \times 10^{18}\) mol⁻¹ dm³ and of the ammine complex is \(1.1 \times 10^{13}\) mol⁻⁴ dm¹². (c) Explain, in terms of entropy, why the EDTA complex is so stable.
H: The exchange constant is a ratio of the two \(K_{\text{stab}}\) values.
A: (a) \(\ce{[Cu(NH3)4(H2O)2]^2+ + EDTA^4- <=> [Cu(EDTA)]^2- + 4NH3 + 2H2O}\) [B1]
(b) \(K = \dfrac{6.3 \times 10^{18}}{1.1 \times 10^{13}}\) [M1] \(= 5.7 \times 10^{5}\) [A1] (mol³ dm⁻⁹)
(c) One EDTA ion replaces six ligands, so the number of particles rises from 2 to 7. [B1] Entropy increases (\(\Delta S\) positive). [B1] \(\Delta G = \Delta H - T\Delta S\) becomes more negative, so \(K_{\text{stab}}\) is larger. [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ The complex \(\ce{[Co(en)2Cl2]+}\) is octahedral. Draw or describe all the stereoisomers and state how many there are.
H: Treat each en as a ligand spanning two adjacent positions. Consider cis and trans, then ask which is chiral.
H: A chiral isomer counts as two.
A: Two geometrical isomers: cis, with the two Cl ligands adjacent, and trans, with the two Cl opposite. [B1 B1]
The trans isomer has a plane of symmetry, so it is not chiral. [B1]
The cis isomer is chiral, giving two optical isomers (mirror images). In total there are three stereoisomers. [B1]
Q: [4 marks] ★★★ In the body, cisplatin reacts: \(\ce{cis-[Pt(NH3)2Cl2] + H2O <=> [Pt(NH3)2Cl(H2O)]+ + Cl-}\). The concentration of chloride ions is much lower inside cells than in the blood. State the charge on the platinum ion in cisplatin, and use Le Chatelier's principle to suggest why this reaction occurs mainly inside cells.
H: Work out the oxidation state of platinum from the neutral formula, then think about what lowering \([\ce{Cl-}]\) does to the position of equilibrium.
A: The complex is neutral and the ligands \(\ce{NH3}\) are neutral, so \(x + 2(-1) = 0\) and platinum is +2. [B1 B1]
A low concentration of \(\ce{Cl-}\) removes a product from the right-hand side. [B1] By Le Chatelier's principle the equilibrium shifts to the right, so more of the aqua complex forms inside cells. [B1]
:::

:::quiz
? How many orbitals are in the higher set when the d orbitals of an octahedral complex split?
- 3
+ 2
- 5
- 1
> Octahedral: two higher (\(d_{z^2}\), \(d_{x^2-y^2}\)) and three lower. In a tetrahedral complex it is the reverse: three higher and two lower.
? A solution of a complex absorbs orange light. What colour is the solution?
- orange
- red
+ blue
- yellow
> The colour seen is the complementary colour of the light absorbed. Orange is absorbed, so the solution appears blue.
? Which ion is colourless in solution?
- \(\ce{Fe^3+}\)
- \(\ce{Cu^2+}\)
+ \(\ce{Zn^2+}\)
- \(\ce{Cr^3+}\)
> \(\ce{Zn^2+}\) is 3d¹⁰: full, so no electron can be promoted. The other three have partly filled 3d sub-shells.
? Which complex ion can show cis/trans isomerism?
- \(\ce{[CuCl4]^2-}\) (tetrahedral)
- \(\ce{[Ag(NH3)2]+}\) (linear)
- \(\ce{[Co(NH3)6]^2+}\) (octahedral, six identical ligands)
+ \(\ce{[Co(NH3)4(H2O)2]^2+}\) (octahedral)
> Cis/trans needs positions that can be adjacent or opposite, with two different ligands. A tetrahedral complex has no opposite positions, a linear one has only two, and six identical ligands give just one structure.
? Which is the correct expression for \(K_{\text{stab}}\) of \(\ce{[Cu(H2O)6]^2+ + 4NH3 <=> [Cu(NH3)4(H2O)2]^2+ + 4H2O}\)?
- \(\dfrac{[\ce{[Cu(NH3)4(H2O)2]^2+}][\ce{H2O}]^4}{[\ce{[Cu(H2O)6]^2+}][\ce{NH3}]^4}\)
- \(\dfrac{[\ce{[Cu(H2O)6]^2+}][\ce{NH3}]^4}{[\ce{[Cu(NH3)4(H2O)2]^2+}]}\)
+ \(\dfrac{[\ce{[Cu(NH3)4(H2O)2]^2+}]}{[\ce{[Cu(H2O)6]^2+}][\ce{NH3}]^4}\)
- \(\dfrac{[\ce{[Cu(NH3)4(H2O)2]^2+}]}{[\ce{[Cu(H2O)6]^2+}][\ce{NH3}]}\)
> Products over reactants, the ammonia concentration raised to its coefficient 4, and water left out because it is the solvent.
? A complex ML₂ has \([\ce{ML2}] = 0.100\), \([\ce{M}] = 1.0 \times 10^{-6}\) and \([\ce{L}] = 0.500\) mol dm⁻³. What is \(K_{\text{stab}}\) in mol⁻² dm⁶?
- \(2.0 \times 10^{5}\)
+ \(4.0 \times 10^{5}\)
- \(2.0 \times 10^{-7}\)
- \(1.0 \times 10^{5}\)
> \(K_{\text{stab}} = 0.100 / (1.0 \times 10^{-6} \times 0.500^2) = 4.0 \times 10^{5}\). Remember to square the ligand concentration.
? Why does EDTA⁴⁻ form such stable complexes?
- it is a monodentate ligand with a high charge
- the enthalpy change is large and negative
+ one EDTA ion replaces six water molecules, so the entropy increases
- it has vacant d orbitals
> The increase in the number of particles gives a large positive entropy change and a more negative \(\Delta G\). Enthalpy hardly changes because dative bonds replace dative bonds.
:::

:::checklist What you can now do
- [ ] I can explain degenerate and non-degenerate d orbitals and sketch the splitting in octahedral and tetrahedral complexes, with the correct number of orbitals in each set.
- [ ] I can explain colour using the promotion of an electron across \(\Delta E = hf\) and the complementary colour of the light absorbed.
- [ ] I can explain why d⁰ and d¹⁰ ions (\(\ce{Sc^3+}\), \(\ce{Zn^2+}\), \(\ce{Cu+}\)) are colourless.
- [ ] I can explain how different ligands give different \(\Delta E\), frequencies absorbed and colours.
- [ ] I can explain the colour changes of copper(II) and cobalt(II) complexes on ligand exchange.
- [ ] I can draw and explain cis/trans isomers of square planar and octahedral complexes, and say which complexes have none.
- [ ] I can explain the optical isomerism of \(\ce{[Ni(en)3]^2+}\) and cis-\(\ce{[Ni(en)2(H2O)2]^2+}\).
- [ ] I can state the overall polarity of the cis and trans isomers.
- [ ] I can write \(K_{\text{stab}}\) expressions without water and do calculations with \(K_{\text{stab}}\) values.
- [ ] I can use \(K_{\text{stab}}\) values to predict ligand exchange and explain the stability of EDTA complexes by entropy.
:::

:::recap
- Ligands split the five degenerate d orbitals into two sets separated by \(\Delta E\): octahedral two higher and three lower; tetrahedral three higher and two lower, with a smaller gap.
- Colour: an electron is promoted from the lower to the higher set by absorbing light with \(\Delta E = hf\). The colour seen is the complementary colour of the light absorbed. A larger \(\Delta E\) means higher-frequency light is absorbed.
- No colour for d⁰ (\(\ce{Sc^3+}\)) and d¹⁰ (\(\ce{Zn^2+}\), \(\ce{Cu+}\)). In these examples \(\Delta E\) increases Cl⁻ < H₂O < NH₃ < CN⁻.
- Ligand exchange changes \(\Delta E\) (and sometimes the shape), so the colour changes: Cu(II) blue to dark blue (NH₃) or yellow-green (Cl⁻); Co(II) pink to blue (Cl⁻).
- Cis/trans: square planar [Pt(NH₃)₂Cl₂] (cisplatin is cis, polar; trans non-polar) and octahedral [Co(NH₃)₄(H₂O)₂]²⁺, [Ni(en)₂(H₂O)₂]²⁺. A tetrahedral complex has no cis/trans.
- Optical isomers: [Ni(en)₃]²⁺ and cis-[Ni(en)₂(H₂O)₂]²⁺ (non-superposable mirror images); the trans isomer is not chiral.
- \(K_{\text{stab}}\) = equilibrium constant for formation of the complex from its ions or molecules in a solvent; water is left out. Larger \(K_{\text{stab}}\) means a more stable complex, and the ligand giving the larger \(K_{\text{stab}}\) replaces the other.
- EDTA complexes are very stable because one EDTA replaces six water molecules, increasing the number of particles (entropy increase).
:::

:::links
- read: [Complex ions - colour](https://www.chemguide.co.uk/inorganic/complexions/colour.html) · Chemguide · why complex ions are coloured, with the splitting of the d orbitals
- read: [Substitution in complex ions - ligand exchange](https://www.chemguide.co.uk/inorganic/complexions/ligandexch.html) · Chemguide · the ligand exchange reactions of copper and cobalt with their colours
- read: [Substitution in complex ions - stability constants](https://www.chemguide.co.uk/inorganic/complexions/stabconst.html) · Chemguide · stability constants and the chelate effect
- read: [Complex ions - shapes](https://www.chemguide.co.uk/inorganic/complexions/shapes.html) · Chemguide · shapes of complex ions and the isomers they show
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Arenes: benzene and its compounds](#chem.org.arenes) moves to a new family of organic compounds, with a ring of delocalised electrons that changes how they react.
