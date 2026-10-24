@chapter chem.analysis2
@title Chromatography and NMR spectroscopy
@level a2
@paper CAIE 9701 Paper 4
@time 7–9 hours
@summary Chromatography separates a mixture, and NMR spectroscopy shows how the atoms in one molecule are arranged. You will learn how to use Rf values and retention times, how to count carbon and hydrogen environments, how to read chemical shifts, peak areas and the n + 1 splitting rule, and how to put IR, mass and NMR evidence together to find an unknown structure.

:::why
Almost every new medicine, food additive and forensic sample passes through two questions: what is in this mixture, and what exactly is each substance? Chromatography answers the first by separating the mixture. NMR spectroscopy answers the second, because it shows how the carbon and hydrogen atoms of a molecule are joined. A chemist who has both can name a compound that has never been seen before, and so can you after this chapter.
:::

**Before you start**, you should know how to read an infrared spectrum and a mass spectrum from [Infrared spectroscopy and mass spectrometry](#chem.analysis), the intermolecular forces from [Shapes of molecules and intermolecular forces](#chem.shapes), and how organic formulas are written from [Introduction to organic chemistry](#chem.org.intro).

:::try Warm-up
Q: A compound's IR spectrum has a strong, sharp absorption at 1715 cm⁻¹ and nothing between 2500 and 3600 cm⁻¹. What can you say about it? (from [Infrared spectroscopy and mass spectrometry](#chem.analysis))
A: The 1715 cm⁻¹ absorption is a C=O bond (carbonyl range 1670–1740). With no O–H absorption, it is not an alcohol or a carboxylic acid: it is a carbonyl compound such as an aldehyde, ketone or ester.
Q: What is the strongest type of intermolecular force between propanone molecules? (from [Shapes of molecules and intermolecular forces](#chem.shapes))
A: Permanent dipole–dipole forces. The C=O bond is polar, but propanone has no H bonded to O, so it cannot form hydrogen bonds with itself.
Q: Write the displayed formula of ethanol and say how many of its hydrogen atoms are bonded to carbon and how many to oxygen. (from [Introduction to organic chemistry](#chem.org.intro))
A: \(\ce{CH3-CH2-O-H}\) written with every bond. Five hydrogen atoms are bonded to carbon (three on the \(\ce{CH3}\), two on the \(\ce{CH2}\)) and one to oxygen.
:::

## Chromatography: separating by speed

Chromatography separates the substances in a mixture because they move at different speeds. Every chromatography experiment has two phases.

:::def Stationary phase
The solid, or the liquid held on a solid support, that stays in place during chromatography.
:::

:::def Mobile phase
The liquid or gas that moves through or over the stationary phase and carries the mixture with it.
:::

Each substance in the mixture constantly swaps between the two phases. For part of the time it is held on the stationary phase, and for part of the time it is carried along by the mobile phase. A substance that is held strongly spends most of its time stuck and moves slowly. A substance that is held weakly and dissolves well in the mobile phase moves quickly. After a while the substances have travelled different distances, and the mixture is separated.

:::analogy
Imagine a river carrying twigs over a muddy bank. A sticky twig keeps catching on the mud and is left behind. A smooth twig hardly touches the mud and is swept far downstream. The river is the mobile phase, the mud is the stationary phase, and the twigs are the substances in the mixture.
:::

The syllabus asks about two types: thin-layer chromatography (TLC), which suits small amounts of liquid solutions, and gas–liquid chromatography (GLC), which suits mixtures that can be vaporised.

## Thin-layer chromatography (TLC)

In TLC the stationary phase is a thin layer of a solid powder, such as **silica** (silicon dioxide) or **aluminium oxide**, spread on a flat support of glass, plastic or aluminium sheet. The mobile phase is a solvent, which can be polar (such as ethanol or water) or non-polar (such as hexane), and which creeps up the plate by capillary action.

### Running a plate

:::steps
1. Draw a **baseline** across the plate near the bottom with a **pencil**. Ink would dissolve in the solvent and run up the plate with the samples; pencil graphite does not.
2. Put a small spot of each solution on the baseline with a fine capillary tube. Keep the spots small and well apart. Spot known compounds (standards) beside the unknown mixture.
3. Stand the plate in a beaker or tank with a little solvent. The baseline must be **above the solvent level**, or the spots would dissolve into the pool instead of travelling up the plate. Cover the beaker with a lid so the air fills with solvent vapour and the solvent does not evaporate from the plate.
4. When the solvent is close to the top, take out the plate and at once mark the **solvent front** with a pencil, because it dries and vanishes in seconds.
5. Dry the plate. If the spots are colourless, make them visible (see below).
6. Measure the distance from the baseline to the solvent front, and from the baseline to the centre of each spot.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 262" role="img" aria-label="A TLC plate standing in solvent. Three lanes labelled X, mixture and Y. Spot X is 4.5 cm above the baseline, spot Y is lower, and the mixture lane shows both. The solvent front is 7.5 cm above the baseline."><path class="ln thick" d="M120 26L250 26L250 246L120 246Z"/><rect class="fa" x="100" y="222" width="170" height="30"/><path class="ln-m thin dash" d="M120 200L250 200"/><path class="ln-m thin dash" d="M120 50L250 50"/><ellipse class="fm2" cx="145" cy="110" rx="8" ry="5"/><circle class="fi" cx="145" cy="200" r="1.8"/><ellipse class="fm2" cx="185" cy="110" rx="8" ry="5"/><ellipse class="fm2" cx="185" cy="146" rx="8" ry="5"/><circle class="fi" cx="185" cy="200" r="1.8"/><ellipse class="fm2" cx="225" cy="146" rx="8" ry="5"/><circle class="fi" cx="225" cy="200" r="1.8"/><text class="tl tc" x="145" y="18">X</text><text class="tl tc" x="185" y="18">mixture</text><text class="tl tc" x="225" y="18">Y</text><text class="tl" x="110" y="54" text-anchor="end">solvent front</text><text class="tl" x="110" y="204" text-anchor="end">pencil baseline</text><text class="tl" x="110" y="238" text-anchor="end">solvent level</text><path class="ln-m thin dash" d="M250 110L282 110"/><path class="ln" d="M282 200L282 114" marker-end="url(#ah)"/><path class="ln-m thin dash" d="M250 50L312 50"/><path class="ln" d="M312 200L312 54" marker-end="url(#ah)"/><text class="tl halo tc" x="282" y="168">4.5 cm</text><text class="tl halo tc" x="312" y="124">7.5 cm</text></svg><figcaption>A developed TLC plate. The small dots on the baseline show where the three samples were placed. The mixture has separated into two spots, which match the standards X and Y. Distances are measured from the baseline to the solvent front and to the centre of each spot.</figcaption></figure>
:::

### Making colourless spots visible

Many compounds are colourless. Two simple ways of finding them are to look at the plate under **ultraviolet light** (plates with a fluorescent indicator glow, and a compound that absorbs the UV shows as a dark spot), or to put the plate in a closed jar with a few crystals of **iodine**, whose vapour stains many organic compounds brown. Some compounds have their own locating agent: ninhydrin is sprayed on plates to find amino acids (see [Amines, amides and amino acids](#chem.org.nitrogen)). Circle the spots in pencil straight away, because they fade.

### Why the spots separate

The silica or aluminium oxide surface is **polar**: it is covered with oxygen atoms and O–H groups. A polar compound, such as an alcohol or a carboxylic acid, forms strong attractions with that surface, by hydrogen bonds or permanent dipole–dipole forces. This sticking to a solid surface is called **adsorption**. A non-polar compound, such as an alkane, has only weak id–id forces with the surface and is hardly adsorbed.

Two things therefore decide how far a spot travels:

- **Adsorption on the stationary phase.** The more strongly a compound is adsorbed, the less time it spends moving, and the shorter its distance.
- **Solubility in the mobile phase.** The more soluble a compound is in the solvent, the more of its time is spent travelling with the solvent, and the greater its distance.

A polar solvent competes with the compound for the surface and dissolves polar compounds well, so it carries all the spots further. A non-polar solvent leaves polar compounds stuck near the baseline.

### The Rf value

The distance a spot moves depends on how far the solvent travelled, and that changes from plate to plate. Dividing by the distance moved by the solvent removes this problem.

:::def Rf value
\(R_f = \dfrac{\text{distance moved by the spot}}{\text{distance moved by the solvent front}}\), with both distances measured from the baseline.
:::

An Rf value has **no unit**, and it is always **between 0 and 1**. A value above 1 means a spot has moved further than the solvent, which is impossible, so the distances have been measured wrongly. A spot that has not left the baseline has Rf = 0.

:::eg Calculate the Rf values of X and Y in the plate shown above.
The solvent front moved 7.5 cm from the baseline, and spot X moved 4.5 cm. [M1]
\[R_f(\text{X}) = \frac{4.5}{7.5} = 0.60\] [A1]
Spot Y moved 2.7 cm, so
\[R_f(\text{Y}) = \frac{2.7}{7.5} = 0.36\] [A1]
Y has the smaller Rf, so it was held more strongly by the polar stationary phase (or it is less soluble in the solvent).
:::

### Reading a plate

:::key Interpreting a chromatogram
- The number of spots is **at least** the number of substances in the mixture. Two compounds with the same Rf would overlap as a single spot.
- A spot in the mixture's lane at the same height as a standard may be that standard. Rf values only compare when the **same plate material, solvent and temperature** are used, and the safest comparison is on the same plate, as in the figure.
- Matching Rf values suggest, but do not prove, that two compounds are the same. Repeating with a different solvent, where two different compounds are unlikely to match twice, is stronger evidence.
:::

:::eg A student runs an unknown dye mixture, P, beside three standards on one plate. The solvent front moves 8.0 cm. The mixture gives spots at 2.0 cm and 5.6 cm. Standard A gives one spot at 2.0 cm, standard B at 4.0 cm and standard C at 5.6 cm. Which standards are in the mixture? Calculate the Rf value of the higher spot.
Spots at the same distance from the baseline, on the same plate, have the same Rf. [B1]
The mixture's spot at 2.0 cm matches A and the spot at 5.6 cm matches C. B has no matching spot, so the mixture contains A and C but not B. [B1]
\[R_f = \frac{5.6}{8.0} = 0.70\] [A1]
The mixture could also contain another substance that happens to have the same Rf as A or C, so the result is evidence, not proof.
:::

## Gas–liquid chromatography (GLC)

TLC cannot separate compounds that are gases or that are hard to dissolve. **Gas–liquid chromatography** separates mixtures of compounds that can be turned into a vapour without decomposing. It is also called gas chromatography (GC).

:::html
<figure class="fig small"><svg viewBox="0 0 320 268" role="img" aria-label="Block diagram of a gas–liquid chromatograph: carrier gas, injector, column in an oven, detector and recorder, joined by arrows"><rect class="fm s-acc" x="40" y="10" width="240" height="32" rx="8"/><text class="tl tc" x="160" y="31">carrier gas (N₂ or He)</text><path class="ln" d="M160 42L160 64" marker-end="url(#ah)"/><rect class="fm s-acc" x="40" y="64" width="240" height="32" rx="8"/><text class="tl tc" x="160" y="85">injector (vaporises sample)</text><path class="ln" d="M160 96L160 118" marker-end="url(#ah)"/><rect class="fm s-acc" x="40" y="118" width="240" height="32" rx="8"/><text class="tl tc" x="160" y="139">column in a hot oven</text><path class="ln" d="M160 150L160 172" marker-end="url(#ah)"/><rect class="fm s-acc" x="40" y="172" width="240" height="32" rx="8"/><text class="tl tc" x="160" y="193">detector</text><path class="ln" d="M160 204L160 226" marker-end="url(#ah)"/><rect class="fm s-acc" x="40" y="226" width="240" height="32" rx="8"/><text class="tl tc" x="160" y="247">recorder (chromatogram)</text></svg><figcaption>The parts of a gas–liquid chromatograph. The sample is injected into a stream of unreactive carrier gas, which carries it through the column.</figcaption></figure>
:::

:::def Stationary phase in GLC
A high boiling point, non-polar liquid held on a solid support packed in (or coating the wall of) a long coiled column.
:::

:::def Mobile phase in GLC
An unreactive gas, such as nitrogen or helium, which carries the vaporised sample through the column. It is called the carrier gas.
:::

:::steps
1. A tiny sample is injected into the hot injector, where it vaporises, and the carrier gas sweeps it into the column.
2. The column sits in an oven, so every component stays as a vapour. Each component dissolves in the liquid stationary phase, evaporates again, dissolves again, and so on, while the gas carries it forward.
3. Components that spend more time dissolved in the stationary phase come out later.
4. At the end of the column a detector gives a signal when a component arrives. The recorder plots signal against time: the **chromatogram**.
:::

:::def Retention time
The time taken for a component to travel through the column, from injection to the detector, measured to the top of its peak.
:::

### What decides the retention time

The stationary phase is non-polar, so a molecule dissolves in it by **id–id forces**. The bigger the molecule, the larger its electron cloud, the stronger the id–id forces with the liquid, and the longer it stays in the column. A compound with strong intermolecular forces of its own is also less volatile, so it spends more time as a liquid and less time as a vapour in the carrier gas. Both effects make the **retention time longer** for a molecule that is less volatile and interacts more strongly with the stationary phase.

For the alcohols ethanol, propan-1-ol and butan-1-ol, the retention time rises with chain length, because each extra \(\ce{CH2}\) adds to the id–id forces. A retention time depends on the column, its temperature and the gas flow, so you compare it with a **standard** run under exactly the same conditions. Two different compounds can share a retention time, so GLC alone, like TLC alone, suggests an identity and does not prove it.

:::html
<figure class="fig small"><svg viewBox="0 0 340 200" role="img" aria-label="A chromatogram with three peaks numbered 1, 2 and 3, with retention times 1.8, 3.5 and 5.4 minutes"><path class="ax" d="M30 130H322" marker-end="url(#ahm)"/><path class="ax" d="M30 130V16" marker-end="url(#ahm)"/><path class="ln-m thin" d="M30 130L30 134"/><text class="ts tc" x="30" y="147">0</text><path class="ln-m thin" d="M65 130L65 134"/><text class="ts tc" x="65" y="147">1</text><path class="ln-m thin" d="M100 130L100 134"/><text class="ts tc" x="100" y="147">2</text><path class="ln-m thin" d="M135 130L135 134"/><text class="ts tc" x="135" y="147">3</text><path class="ln-m thin" d="M170 130L170 134"/><text class="ts tc" x="170" y="147">4</text><path class="ln-m thin" d="M205 130L205 134"/><text class="ts tc" x="205" y="147">5</text><path class="ln-m thin" d="M240 130L240 134"/><text class="ts tc" x="240" y="147">6</text><path class="ln-m thin" d="M275 130L275 134"/><text class="ts tc" x="275" y="147">7</text><path class="ln-m thin" d="M310 130L310 134"/><text class="ts tc" x="310" y="147">8</text><text class="tl" x="38" y="12">detector response</text><text class="tl tc" x="176" y="190">retention time / min</text><path class="c1 sw2" d="M77.2 129.5L79 128.6L80.8 126.8L82.5 123.5L84.2 118L86 110.3L87.8 100.9L89.5 91.6L91.3 84.6L93 82L94.8 84.6L96.5 91.6L98.3 100.9L100 110.3L101.8 118L103.5 123.5L105.2 126.8L107 128.6L108.7 129.5"/><path class="ln-m thin dash" d="M93 84L93 130"/><text class="tl tc" x="93" y="75">1</text><text class="tl tc" x="93" y="166">1.8</text><path class="c1 sw2" d="M126.2 129.2L129.2 127.9L132.1 125.3L135 120.3L137.9 112L140.8 100.4L143.8 86.3L146.7 72.3L149.6 61.9L152.5 58L155.4 61.9L158.3 72.3L161.3 86.3L164.2 100.4L167.1 112L170 120.3L172.9 125.3L175.8 127.9L178.8 129.2"/><path class="ln-m thin dash" d="M152.5 60L152.5 130"/><text class="tl tc" x="152.5" y="51">2</text><text class="tl tc" x="152.5" y="166">3.5</text><path class="c1 sw2" d="M198 129.7L200.3 129.1L202.7 128L205 125.9L207.3 122.5L209.7 117.7L212 111.8L214.3 106L216.7 101.6L219 100L221.3 101.6L223.7 106L226 111.8L228.3 117.7L230.7 122.5L233 125.9L235.3 128L237.7 129.1L240 129.7"/><path class="ln-m thin dash" d="M219 102L219 130"/><text class="tl tc" x="219" y="93">3</text><text class="tl tc" x="219" y="166">5.4</text></svg><figcaption>A chromatogram of a three-component mixture. The retention time of each component is read at the top of its peak, below the time axis. The area under a peak shows how much of that component there is.</figcaption></figure>
:::

### Percentage composition from peak areas

The area under a peak is proportional to the amount of that component that passed the detector, provided the detector responds equally to every component. The syllabus asks you to assume that it does.

:::formula Percentage composition from a chromatogram
\[\text{percentage of a component} = \frac{\text{area of its peak}}{\text{total area of all the peaks}} \times 100\]
Use areas, not heights: a tall thin peak can hold less than a short wide one. For a narrow peak, area \(\approx \tfrac12 \times \text{base} \times \text{height}\).
:::

:::eg The chromatogram above was printed at 1 cm per minute. Peak 1 has a height of 4.0 cm and a base of 0.6 cm. Peak 2 has height 6.0 cm and base 1.0 cm. Peak 3 has height 2.5 cm and base 0.8 cm. Calculate the percentage of each component, treating each peak as a triangle.
Area of a triangle \(= \tfrac12 \times \text{base} \times \text{height}\). [B1]
Peak 1: \(\tfrac12 \times 0.6 \times 4.0 = 1.2\); peak 2: \(\tfrac12 \times 1.0 \times 6.0 = 3.0\); peak 3: \(\tfrac12 \times 0.8 \times 2.5 = 1.0\) (units: cm²). [M1]
Total area \(= 1.2 + 3.0 + 1.0 = 5.2\). [M1]
\[\text{peak 1} = \frac{1.2}{5.2} \times 100 = 23.1\,\%\qquad \text{peak 2} = \frac{3.0}{5.2} \times 100 = 57.7\,\%\qquad \text{peak 3} = \frac{1.0}{5.2} \times 100 = 19.2\,\%\] [A1]
The three percentages add to 100.0 %.
:::

:::cols
:::col TLC
- Stationary phase: a solid (silica or aluminium oxide) on a flat support.
- Mobile phase: a liquid solvent.
- Measured: Rf value, distance moved by spot ÷ distance moved by solvent front.
- Compounds are held by adsorption and dissolved by the solvent.
:::
:::col GLC
- Stationary phase: a high boiling point non-polar liquid on a solid support.
- Mobile phase: an unreactive gas (nitrogen, helium).
- Measured: retention time, and peak areas for composition.
- Compounds dissolve in the liquid and are carried by the gas.
:::
:::

:::lab GC–MS in the forensic laboratory
In a forensic or environmental laboratory the end of a gas chromatograph is often joined to a mass spectrometer. The column separates a mixture, such as a sample of drink or river water, and the mass spectrometer records the molecular ion and fragments of each component as it emerges. The retention time and the mass spectrum together identify each compound far more reliably than either alone (see [Infrared spectroscopy and mass spectrometry](#chem.analysis)).
:::

:::warn Three common slips in chromatography
- Measuring the spot distance from the bottom edge of the plate. Measure from the **baseline** to the **centre** of the spot.
- Using peak heights instead of areas for percentage composition.
- Saying that a "long retention time means a large molecule". It means stronger interaction with the stationary phase and lower volatility, and you must say so.
:::

## Nuclear magnetic resonance (NMR) spectroscopy

Chromatography tells you how many substances there are. NMR spectroscopy tells you how the atoms of one pure compound are arranged. A hospital MRI scanner uses the same effect on the hydrogen atoms of the body.

Some atomic nuclei, including \(^{1}\)H (a proton) and \(^{13}\)C, behave like tiny magnets. In a strong magnetic field they can absorb radio-frequency radiation. The exact frequency depends on the electrons around the nucleus, because electrons partly **shield** it from the field. A nucleus in a different part of the molecule has different electrons around it and absorbs at a slightly different frequency. The spectrometer records these frequencies as peaks, and the peaks reveal the structure.

:::def Chemical environment
The surroundings of an atom in a molecule. Two atoms are in the same chemical environment when they are bonded in the same way and are equivalent by the symmetry of the molecule.
:::

:::def Chemical shift
The position of an NMR signal relative to the signal of the standard, tetramethylsilane (TMS). It is given the symbol δ and is measured in parts per million (ppm).
:::

The electrons give you a rule that explains every shift in the Data table. An atom next to an **electronegative** atom such as O or Cl has electron density pulled away from it. It is less shielded, and its signal appears at a **larger δ** (the left of the spectrum). An atom far from electronegative atoms is well shielded and appears at a smaller δ (the right). So the shift is a clue to what the atom is next to.

Two NMR spectra are on your syllabus: ¹³C NMR, which shows the carbon atoms, and ¹H NMR, which shows the hydrogen atoms. Only about 1.1 % of carbon atoms are \(^{13}\)C; the same figure gave the [M+1] peak in mass spectrometry. The more common \(^{12}\)C has no magnetic behaviour and gives no signal. At A Level you only need to count and read the lines, not to explain why \(^{13}\)C is weak.

## ¹³C NMR: counting carbon environments

In a ¹³C NMR spectrum each carbon **environment** gives one signal, a single line. Carbon atoms that are equivalent by symmetry give the same line. So the number of lines is the number of different carbon environments, and it often tells you how symmetrical a molecule is.

:::key How to count ¹³C environments
1. Draw the structure with every carbon visible.
2. Look for symmetry: carbon atoms that you could swap by a mirror plane or rotation, such as the two \(\ce{CH3}\) groups of propan-2-ol, are equivalent.
3. Count the groups of equivalent carbon atoms. That number is the number of peaks.
:::

| Compound | Carbon environments | Number of peaks |
|---|---|---|
| propan-1-ol, \(\ce{CH3CH2CH2OH}\) | \(\ce{CH3}\), \(\ce{CH2}\), \(\ce{CH2OH}\) | 3 |
| propan-2-ol, \(\ce{(CH3)2CHOH}\) | two equivalent \(\ce{CH3}\), \(\ce{CHOH}\) | 2 |
| propanone, \(\ce{(CH3)2CO}\) | two equivalent \(\ce{CH3}\), C=O | 2 |
| methyl propanoate, \(\ce{CH3CH2COOCH3}\) | \(\ce{CH3}\), \(\ce{CH2}\), C=O, \(\ce{OCH3}\) | 4 |
| benzene, \(\ce{C6H6}\) | all six carbons equivalent | 1 |
| methylbenzene, \(\ce{C6H5CH3}\) | \(\ce{CH3}\); the ring carbon holding the methyl group; the two ring carbons next to it; the two next to those; the carbon opposite | 5 |

In propan-2-ol the two methyl groups are equivalent but the central carbon is different, so there are two peaks from three carbon atoms. In methylbenzene the ring has a mirror plane through the substituted carbon and the opposite carbon, so the six ring carbons give four lines.

### Reading the shift

The shift of each line tells you what kind of carbon it is. These ranges are in the Data booklet.

| Type of carbon | δ / ppm |
|---|---|
| \(sp^3\) alkyl | 0–50 |
| \(sp^3\) next to an alkene or arene | 25–50 |
| \(sp^3\) next to a carbonyl or carboxyl group | 30–65 |
| \(sp^3\) next to a halogen | 30–60 |
| \(sp^3\) next to oxygen | 50–70 |
| \(sp\) nitrile, C≡N | 100–125 |
| \(sp^2\) alkene or arene | 110–160 |
| \(sp^2\) carboxyl, RCOOH or RCOOR | 160–185 |
| \(sp^2\) carbonyl, RCHO or RCOR | 190–220 |

The ranges overlap, so a shift narrows the possibilities and does not always name the group. The big gaps do help: a line near 200 ppm can only be an aldehyde or ketone C=O, one near 170 ppm an acid or ester, and a line from 110 to 160 ppm comes from a C=C or a benzene ring.

:::html
<figure class="fig small"><svg viewBox="0 0 322 176" role="img" aria-label="A sketch of the 13C NMR spectrum of methyl propanoate with four single lines at 175, 52, 27 and 9 ppm, on a scale from 220 on the left to 0 on the right"><path class="ax" d="M14 130H310"/><path class="ln-m thin" d="M45.1 130L45.1 134"/><text class="ts tc" x="45.1" y="147">200</text><path class="ln-m thin" d="M107.8 130L107.8 134"/><text class="ts tc" x="107.8" y="147">150</text><path class="ln-m thin" d="M170.5 130L170.5 134"/><text class="ts tc" x="170.5" y="147">100</text><path class="ln-m thin" d="M233.3 130L233.3 134"/><text class="ts tc" x="233.3" y="147">50</text><path class="ln-m thin" d="M296 130L296 134"/><text class="ts tc" x="296" y="147">0</text><text class="tl tc" x="158" y="168">δ / ppm</text><path class="c1 sw3" d="M76.5 130L76.5 88"/><path class="c1 sw3" d="M230.8 130L230.8 30"/><path class="c1 sw3" d="M262.1 130L262.1 56"/><path class="c1 sw3" d="M284.7 130L284.7 82"/><text class="tl tc" x="76.5" y="81">175 C=O</text><text class="tl tc" x="230.8" y="23">52 OCH₃</text><text class="tl tc" x="262.1" y="49">27 CH₂</text><text class="tl tc" x="284.7" y="75">9 CH₃</text></svg><figcaption>A sketch of the ¹³C NMR spectrum of methyl propanoate. The scale runs from high δ on the left to low δ on the right. Four carbon environments give four lines: the ester C=O is in the 160–185 range, the OCH₃ carbon in the 50–70 range, and the two alkyl carbons in the 0–50 range. Line heights are not used in this course.</figcaption></figure>
:::

:::eg How many peaks are there in the ¹³C NMR spectrum of each of the four alcohols of formula \(\ce{C4H10O}\)? Butan-1-ol, butan-2-ol, 2-methylpropan-1-ol and 2-methylpropan-2-ol.
Draw each structure and group the equivalent carbons. [B1]

:::html
<figure class="fig small"><svg viewBox="0 0 340 310" role="img" aria-label="Skeletal formulas of butan-1-ol, butan-2-ol, 2-methylpropan-1-ol and 2-methylpropan-2-ol, labelled with 4, 4, 3 and 2 carbon-13 peaks"><path class="ln thick" d="M10 60L45 40L80 60L115 40L141 54"/><text class="tl" x="146" y="62">OH</text><text class="tl tc" x="80" y="102">butan-1-ol</text><text class="tl ta tc" x="80" y="120">4 peaks</text><path class="ln thick" d="M190 60L225 40L260 60L295 40"/><path class="ln thick" d="M225 40L225 26"/><text class="tl tc" x="225" y="18">OH</text><text class="tl tc" x="242" y="102">butan-2-ol</text><text class="tl ta tc" x="242" y="120">4 peaks</text><path class="ln thick" d="M24 190L45 178L80 198L115 178"/><path class="ln thick" d="M80 198L80 230"/><text class="tl tc" x="12" y="200">OH</text><text class="tl tc" x="80" y="278">2-methylpropan-1-ol</text><text class="tl ta tc" x="80" y="296">3 peaks</text><path class="ln thick" d="M203 214L235 200L267 214"/><path class="ln thick" d="M235 200L235 186"/><path class="ln thick" d="M235 200L235 234"/><text class="tl tc" x="235" y="178">OH</text><text class="tl tc" x="235" y="278">2-methylpropan-2-ol</text><text class="tl ta tc" x="235" y="296">2 peaks</text></svg><figcaption>The four alcohols \(\ce{C4H10O}\) and the number of ¹³C peaks of each.</figcaption></figure>
:::

Butan-1-ol, \(\ce{CH3CH2CH2CH2OH}\): all four carbons are different, so **4** peaks. [A1]
Butan-2-ol, \(\ce{CH3CH(OH)CH2CH3}\): the two ends are different (one \(\ce{CH3}\) is next to \(\ce{CHOH}\), the other next to \(\ce{CH2}\)), so **4** peaks. [A1]
2-methylpropan-1-ol, \(\ce{(CH3)2CHCH2OH}\): the two methyl groups are equivalent, so \(\ce{CH3}\), \(\ce{CH}\), \(\ce{CH2OH}\) give **3** peaks. [A1]
2-methylpropan-2-ol, \(\ce{(CH3)3COH}\): the three methyl groups are equivalent, so \(\ce{CH3}\) and the carbon holding OH give **2** peaks. [A1]

¹³C counting alone cannot tell butan-1-ol from butan-2-ol, since both give four peaks. The shifts, or the ¹H spectrum, would be needed. The caption of the figure says "peaks" because that is the term the exam uses.
:::

:::warn Count environments, not carbons
Propan-2-ol has three carbon atoms but gives **two** peaks. Always look for symmetry before counting. The reverse mistake also happens: benzene has six carbon atoms but only one peak, while methylbenzene has seven carbon atoms and five peaks.
:::

## ¹H NMR: four pieces of evidence

A ¹H NMR spectrum gives four pieces of evidence about the hydrogen atoms in the molecule.

1. The **number of signals**: how many different hydrogen environments there are.
2. The **chemical shift** of each signal: what the hydrogens are next to.
3. The **area** under each signal: how many hydrogens are in each environment.
4. The **splitting** of each signal: how many hydrogens are on the neighbouring carbon atoms.

### The number of signals

The counting is the same as for carbon, but now the unit is a hydrogen environment. Hydrogens on the same carbon are normally equivalent, and hydrogens on different carbons are equivalent only when symmetry swaps them.

Ethanol, \(\ce{CH3CH2OH}\), has three environments: the \(\ce{CH3}\) hydrogens, the \(\ce{CH2}\) hydrogens and the O–H hydrogen, so **3** signals. Propan-2-ol, \(\ce{(CH3)2CHOH}\), also has three: the six hydrogens of the two equivalent methyl groups, the C–H, and the O–H. Ethane, \(\ce{CH3CH3}\), has just one signal, since all six hydrogens are equivalent.

### The chemical shift

The same electron rule applies: hydrogens next to electronegative atoms or groups appear at a larger δ. The values to use are those in the Data booklet.

| Type of hydrogen | δ / ppm |
|---|---|
| alkane \(\ce{-CH3}\), \(\ce{-CH2-}\), \(\ce{>CH-}\) | 0.9–1.7 |
| alkyl next to C=O | 2.2–3.0 |
| alkyl next to an aromatic ring | 2.3–3.0 |
| alkyl next to an electronegative atom (\(\ce{CH3-O}\), \(\ce{-CH2-O}\), \(\ce{-CH2-Cl}\)) | 3.2–4.0 |
| attached to an alkene, \(\ce{=CHR}\) | 4.5–6.0 |
| attached to an aromatic ring, H–Ar | 6.0–9.0 |
| aldehyde, HCOR | 9.3–10.5 |
| alcohol, ROH | 0.5–6.0 |
| phenol, Ar–OH | 4.5–7.0 |
| carboxylic acid, RCOOH | 9.0–13.0 |
| alkyl amine, R–NH– | 1.0–5.0 |
| aryl amine, Ar–NH₂ | 3.0–6.0 |
| amide, RCONHR | 5.0–12.0 |

The O–H and N–H shifts are wide because they depend on the solvent and the concentration, since these atoms form hydrogen bonds.

### The area of a signal

The area under each signal is proportional to the number of hydrogen atoms that cause it. The spectrometer draws an **integration trace**, a line that steps up as it passes each signal. The height of each step gives the area. Compare the step heights as a ratio, and divide by the smallest to get whole numbers.

:::eg An integration trace for a compound of formula \(\ce{C4H8O2}\) has step heights of 12.0 mm, 8.0 mm and 12.0 mm for its three signals. How many hydrogen atoms cause each signal?
The ratio of the step heights is \(12.0 : 8.0 : 12.0 = 3 : 2 : 3\), found by dividing each height by 4.0. [M1]
The ratio adds up to \(3 + 2 + 3 = 8\), which is the number of hydrogens in \(\ce{C4H8O2}\). So the signals come from 3, 2 and 3 hydrogen atoms. [A1]
:::

If the ratio adds up to half the number of hydrogens in the formula (or another fraction), double (or multiply) it until it matches. An integration ratio of 1 : 1 for a compound with eight hydrogens means 4 : 4, not 1 : 1.

### Splitting: the n + 1 rule

Many signals are not a single line. They are split into a group of lines. The hydrogen nuclei on the **adjacent carbon atoms** act as tiny magnets, and each one slightly changes the field that the signal's hydrogens feel. This splits the signal.

:::key The n + 1 rule
A signal from hydrogens that have **n equivalent hydrogens on the adjacent carbon atoms** is split into **n + 1** lines.
:::

| n | Lines (n + 1) | Name | Relative heights |
|---|---|---|---|
| 0 | 1 | singlet | 1 |
| 1 | 2 | doublet | 1 : 1 |
| 2 | 3 | triplet | 1 : 2 : 1 |
| 3 | 4 | quartet | 1 : 3 : 3 : 1 |
| 4 or more | 5 or more | multiplet | 1 : 4 : 6 : 4 : 1 and so on |

The heights follow Pascal's triangle, where each number is the sum of the two above it. Where a signal has many lines, the outer ones are too small to see and the examiner simply says "multiplet".

:::html
<figure class="fig small"><svg viewBox="0 0 330 170" role="img" aria-label="Two splitting patterns: a triplet of three lines with heights in the ratio 1 : 2 : 1 for two neighbouring hydrogens, and a quartet of four lines with heights 1 : 3 : 3 : 1 for three neighbouring hydrogens"><path class="ax" d="M15 118H155"/><path class="c1 sw3" d="M71 118L71 98"/><text class="tl tc" x="71" y="90">1</text><path class="c1 sw3" d="M85 118L85 78"/><text class="tl tc" x="85" y="70">2</text><path class="c1 sw3" d="M99 118L99 98"/><text class="tl tc" x="99" y="90">1</text><text class="tl tc" x="85" y="138">triplet: 3 lines</text><text class="tl tc" x="85" y="156">n = 2 neighbouring H</text><path class="ax" d="M175 118H315"/><path class="c1 sw3" d="M224 118L224 98"/><text class="tl tc" x="224" y="90">1</text><path class="c1 sw3" d="M238 118L238 58"/><text class="tl tc" x="238" y="50">3</text><path class="c1 sw3" d="M252 118L252 58"/><text class="tl tc" x="252" y="50">3</text><path class="c1 sw3" d="M266 118L266 98"/><text class="tl tc" x="266" y="90">1</text><text class="tl tc" x="245" y="138">quartet: 4 lines</text><text class="tl tc" x="245" y="156">n = 3 neighbouring H</text></svg><figcaption>A triplet and a quartet. The numbers above the lines are their relative heights. The gaps between lines are drawn much wider than in a real spectrum so that you can count them.</figcaption></figure>
:::

Four rules decide which hydrogens split which signals.

- **Only hydrogens on adjacent carbon atoms split a signal.** Hydrogens on the same carbon do not split each other. A \(\ce{CH3}\) group with no hydrogen on the next carbon (such as \(\ce{CH3-C=O}\) or \(\ce{CH3-O-}\)) is a singlet.
- **Equivalent hydrogens do not split each other.** The three hydrogens of one \(\ce{CH3}\) group give a single signal, not a multiplet.
- **A group that sits between two others splits both ways.** Add up the hydrogens on both neighbours, if they are equivalent or look alike. In \(\ce{CH3CH2CH2OH}\) the middle \(\ce{CH2}\) has 3 + 2 = 5 neighbours and gives 6 lines, which you call a multiplet.
- **O–H and N–H hydrogens are usually not split, and do not split their neighbours.** They exchange rapidly with other molecules, and appear as singlets.

:::warn n + 1, not n
Three neighbouring hydrogens make a **quartet**, not a triplet. If a student counts the lines they must get n + 1, and if they predict the pattern they must add 1. Counting the hydrogens **on the same carbon** instead of the neighbouring carbon is the other common slip.
:::

A few patterns turn up again and again, and recognising them speeds up every structure problem.

| Fragment | Signals |
|---|---|
| \(\ce{CH3CH2-X}\) (X with no hydrogens on its first atom) | \(\ce{CH2}\): quartet (2H); \(\ce{CH3}\): triplet (3H) |
| \(\ce{(CH3)2CH-X}\) | \(\ce{CH3}\): doublet (6H); \(\ce{CH}\): multiplet (1H) |
| \(\ce{CH3-C=O}\) or \(\ce{CH3-O-}\) with nothing on the next atom | singlet (3H) |
| \(\ce{-CH2CH2-}\) between two different groups | two triplets (2H each) |

### Predicting a spectrum

To predict a ¹H NMR spectrum, go through the molecule environment by environment.

:::eg (Exam style) Predict the ¹H NMR spectrum of ethyl ethanoate, \(\ce{CH3COOCH2CH3}\). Give the number of signals, the shift range from the Data booklet, the relative area and the splitting of each.
There are three hydrogen environments: \(\ce{CH3CO}\), \(\ce{OCH2}\) and \(\ce{CH3CH2}\), so three signals. [B1]

| Hydrogens | δ range | Area | Neighbouring H | Splitting |
|---|---|---|---|---|
| \(\ce{CH3-C=O}\) | 2.2–3.0 | 3 | 0 | singlet |
| \(\ce{-O-CH2-}\) | 3.2–4.0 | 2 | 3 | quartet |
| \(\ce{CH3-CH2}\) | 0.9–1.7 | 3 | 2 | triplet |

The \(\ce{CH3CO}\) signal is a singlet in the range for alkyl next to C=O. [B1]
The \(\ce{OCH2}\) signal is a quartet in the range for alkyl next to an electronegative atom, because the neighbouring \(\ce{CH3}\) gives n = 3. [B1]
The \(\ce{CH3}\) signal is a triplet in the alkane range, because the neighbouring \(\ce{CH2}\) gives n = 2. [B1]
The areas are in the ratio 3 : 2 : 3. The oxygen atom of the ester stops the \(\ce{CH3CO}\) group from seeing the ethyl group, since the oxygen is between them and has no hydrogens.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 196" role="img" aria-label="A sketch of the 1H NMR spectrum of ethyl ethanoate on a scale from 12 on the left to 0 on the right: a quartet at 3.9 with area 2H, a singlet at 2.3 with area 3H, a triplet at 1.3 with area 3H, and the TMS line at 0"><path class="ax" d="M12 134H322"/><path class="ln-m thin" d="M304 134L304 138"/><text class="ts tc" x="304" y="151">0</text><path class="ln-m thin" d="M256.7 134L256.7 138"/><text class="ts tc" x="256.7" y="151">2</text><path class="ln-m thin" d="M209.3 134L209.3 138"/><text class="ts tc" x="209.3" y="151">4</text><path class="ln-m thin" d="M162 134L162 138"/><text class="ts tc" x="162" y="151">6</text><path class="ln-m thin" d="M114.7 134L114.7 138"/><text class="ts tc" x="114.7" y="151">8</text><path class="ln-m thin" d="M67.3 134L67.3 138"/><text class="ts tc" x="67.3" y="151">10</text><path class="ln-m thin" d="M20 134L20 138"/><text class="ts tc" x="20" y="151">12</text><text class="tl tc" x="162" y="188">δ / ppm</text><path class="c1 sw2" d="M204.2 134L204.2 126.5"/><path class="c1 sw2" d="M209.2 134L209.2 111.5"/><path class="c1 sw2" d="M214.2 134L214.2 111.5"/><path class="c1 sw2" d="M219.2 134L219.2 126.5"/><text class="tl tc" x="211.7" y="170">2H</text><path class="c1 sw2" d="M249.6 134L249.6 44"/><text class="tl tc" x="249.6" y="170">3H</text><path class="c1 sw2" d="M268.2 134L268.2 111.5"/><path class="c1 sw2" d="M273.2 134L273.2 89"/><path class="c1 sw2" d="M278.2 134L278.2 111.5"/><text class="tl tc" x="273.2" y="170">3H</text><path class="c1 sw2" d="M304 134L304 94"/><text class="tl tc" x="304" y="87">TMS</text></svg><figcaption>A sketch of the ¹H NMR spectrum of ethyl ethanoate. From the left: the OCH₂ quartet (2H), the CH₃CO singlet (3H) and the CH₃ triplet (3H), then the TMS line at δ = 0. The shifts are typical values inside the Data booklet ranges; real spectra differ by a few tenths of a ppm.</figcaption></figure>
:::

### TMS, and the solvent

Chemical shifts are measured against a standard so that spectra from different instruments can be compared.

:::def TMS (tetramethylsilane)
\(\ce{Si(CH3)4}\), the standard for NMR shifts, whose signal is defined as δ = 0 ppm.
:::

TMS is used because all twelve of its hydrogens (and all four of its carbons) are equivalent, so it gives **one sharp signal**. It is **chemically inert**, so it does not react with the sample. It is **volatile**, so it can be removed from the sample by evaporation afterwards. And its signal is at the far right, **upfield of nearly every other signal**, so it does not overlap with the sample's signals, since silicon is less electronegative than carbon and the hydrogens are strongly shielded.

The sample is dissolved in a solvent for the spectrum. If the solvent contained ordinary hydrogen, its signal would drown the sample's. So the solvent is **deuterated**: a solvent in which the hydrogen atoms are replaced by deuterium, \(^{2}\)H or D, such as deuterated chloroform, \(\ce{CDCl3}\). Deuterium does not absorb in the region of a ¹H spectrum, so the solvent gives no ¹H signal.

### The D₂O test for O–H and N–H

Because an O–H signal can appear almost anywhere from 0.5 to 6.0 ppm, how do you know which signal it is? Shake the sample with a few drops of heavy water, \(\ce{D2O}\) (deuterium oxide). The O–H hydrogen swaps with deuterium:

\[\ce{R-OH + D2O <=> R-OD + HOD}\]

Deuterium does not show in the ¹H spectrum, so the O–H signal **disappears**. N–H hydrogens do the same, and so do the O–H of a carboxylic acid and a phenol. Signals from hydrogens on carbon do not change.

:::eg The ¹H NMR spectrum of ethanol in \(\ce{CDCl3}\) has signals at δ 1.2 (triplet, 3H), δ 2.6 (singlet, 1H) and δ 3.7 (quartet, 2H). A few drops of \(\ce{D2O}\) are added and the spectrum is run again. What happens, and why?
The signal at δ 2.6 disappears. [B1]
It is the O–H hydrogen. It exchanges with deuterium from \(\ce{D2O}\) to give O–D, and deuterium gives no ¹H signal. [B1]
The signals at 1.2 and 3.7 are from hydrogens on carbon, which do not exchange, so they stay. [B1]
:::

## The structure-solving method

Real problems give you a mixture of evidence. Work through it in this order, so that no clue is missed and every conclusion is checked.

:::steps
1. **Molecular formula.** Use the molecular ion in the mass spectrum (and the [M+1] and [M+2] peaks if given) to get the formula. Count the hydrogen atoms: you need this to check the integration.
2. **Functional groups from IR.** Use the Data table for C=O, O–H, N–H, C≡N and so on.
3. **Count the ¹³C signals.** This tells you how many carbon environments, so how symmetric the molecule is. Check the shifts for C=O, C=C or ring carbons.
4. **¹H shifts.** Match each signal to a group using the table.
5. **Integration.** Turn the step heights into whole numbers adding up to the number of hydrogens.
6. **Splitting.** Use n + 1 on each signal to find the neighbours of each group.
7. **Assemble the pieces** into a structure that uses every atom of the formula.
8. **Check.** Predict the whole spectrum of your structure and make sure it fits every piece of evidence, including the ¹³C count.
:::

:::eg A compound has the molecular formula \(\ce{C3H6O2}\). Its ¹H NMR spectrum has two signals, both singlets: δ 2.3 (area 3) and δ 3.7 (area 3). Identify the compound.
There are two hydrogen environments of 3H each, which adds up to six hydrogens, matching the formula. [B1]
Both signals are singlets, so neither group has hydrogens on an adjacent carbon. [B1]
δ 2.3 is in the range 2.2–3.0 for \(\ce{CH3}\) next to C=O, and δ 3.7 is in the range 3.2–4.0 for \(\ce{CH3}\) next to an electronegative atom, \(\ce{CH3-O}\). [B1]
Putting \(\ce{CH3-C=O}\) and \(\ce{CH3-O}\) together with the two oxygen atoms gives \(\ce{CH3COOCH3}\), **methyl ethanoate**. [A1]
Check: two carbon environments for the methyl groups plus a C=O makes three, so ¹³C should show three peaks. An isomer, propanoic acid \(\ce{CH3CH2COOH}\), would show a triplet and a quartet and a very downfield acid signal, so it does not fit.
:::

:::eg (Exam style, combined evidence) Compound Q has these properties. Mass spectrum: M⁺ at m/e 72 with abundance 20.0 %, [M+1]⁺ abundance 0.88 %, and fragments at m/e 57, 43 and 29. IR: strong absorption at 1715 cm⁻¹ and nothing between 2500 and 3600 cm⁻¹. ¹H NMR: δ 1.0 (triplet, 3H), δ 2.1 (singlet, 3H), δ 2.4 (quartet, 2H). ¹³C NMR: four peaks, at δ 8, 30, 37 and 209. Identify Q.
**Carbons.** \(n = \dfrac{100 \times 0.88}{1.1 \times 20.0} = 4.0\), so four carbon atoms. [M1] [A1]
**Formula.** Four carbons weigh 48, leaving 24. IR shows a C=O (one oxygen, 16), leaving 8 for hydrogen, so Q is \(\ce{C4H8O}\). [M1] The areas 3 + 3 + 2 = 8 match. [B1]
**Groups.** The IR absorption at 1715 cm⁻¹ is in the carbonyl range, and there is no O–H, so it is an aldehyde or ketone. The ¹³C peak at 209 is in the 190–220 range for C=O. [B1]
**¹H signals.** δ 2.1 singlet 3H is \(\ce{CH3-C=O}\) with no neighbouring hydrogens. [B1] δ 2.4 quartet 2H is \(\ce{CH2}\) next to C=O with three neighbours, so it is next to a \(\ce{CH3}\); δ 1.0 triplet 3H is that \(\ce{CH3}\), next to a \(\ce{CH2}\). [B1] So the pieces are \(\ce{CH3CO-}\) and \(\ce{-CH2CH3}\).
**Fragments.** m/e 43 is \(\ce{CH3CO+}\); 57 is \(\ce{CH3CH2CO+}\) (72 − 15, loss of \(\ce{CH3}\)); 29 is \(\ce{CH3CH2+}\). [B1]
Q is **butanone**, \(\ce{CH3COCH2CH3}\). [A1]
Check: four different carbons give four ¹³C peaks, which agrees. The aldehyde isomer butanal, \(\ce{CH3CH2CH2CHO}\), has a signal at δ 9.3–10.5, which Q does not.
:::

:::exam Showing your reasoning
Marks go to each deduction, so write one line for each piece of evidence: "δ 2.4, quartet, 2H: \(\ce{CH2}\) next to C=O, next to a \(\ce{CH3}\)". A bare answer with the right compound but no reasoning often scores very little, and a wrong structure with correct deductions still earns most of the marks.
:::

## Predicting and checking with the NMR tool

Use the tool below to see how real structures give their spectra. Choose a molecule, then switch between the ¹H and ¹³C views. In the ¹H view, tick the D₂O box and watch the O–H signal go. Click or tab to a signal to see which hydrogens it comes from.

:::html
<div class="widget" data-w="chem-nmr" data-mol="ethanol" data-mode="h"></div>
:::

Things to try: compare propan-1-ol with propan-2-ol (the middle \(\ce{CH2}\) of propan-1-ol has five neighbours, whereas the CH of propan-2-ol has six); compare ethanal with propanone to see why an aldehyde signal is near 10; and see how many ¹³C peaks propanone and propan-2-ol have.

:::board
AQA also asks for the explanation of the n + 1 rule only as a pattern, and some questions use high-resolution spectra. Cambridge 9701 only asks you to apply the n + 1 rule to the signals shown.
:::

:::eg Spot the error: predict the ¹H NMR spectrum of ethanol, \(\ce{CH3CH2OH}\). [4 marks]
A student wrote this answer.

Line 1: There are three signals, because there are three hydrogen environments.
Line 2: The \(\ce{CH3}\) signal (3H) is a doublet, because there are two hydrogens on the next carbon.
Line 3: The \(\ce{CH2}\) signal (2H) is a quartet in the range 3.2–4.0.
Line 4: The O–H signal (1H) is a singlet.

Line 1 is correct [B1]. **Line 2 is wrong: two neighbouring hydrogens give n + 1 = 3 lines, a triplet, not a doublet. The student used n instead of n + 1 [B0].** Line 3 is correct [B1], and line 4 is correct [B1].

Correct line 2: the \(\ce{CH3}\) signal is a triplet (3 lines, 1 : 2 : 1) in the range 0.9–1.7. [B1]

The student scores 3 out of 4. Always write the sum "n = 2, so 2 + 1 = 3 lines" until the rule is automatic.
:::

:::try Start easy, finish at exam standard
Q: The solvent front on a TLC plate moved 6.4 cm. A spot moved 2.4 cm. Calculate the Rf value.
A: \(R_f = 2.4 / 6.4 = 0.375\), so 0.38 (2 s.f.). It has no unit.
Q: A student calculates an Rf value of 1.3 for a spot. What has gone wrong?
A: An Rf cannot be more than 1, since a spot cannot move further than the solvent front. The student has probably measured the spot's distance from the wrong place (such as the bottom edge of the plate) or mixed up the two distances.
Q: Why is the baseline on a TLC plate drawn in pencil and kept above the level of the solvent?
A: Pencil does not dissolve in the solvent, but ink would run up the plate. If the baseline were below the solvent level, the samples would dissolve into the solvent instead of travelling up the plate.
Q: In GLC, the retention time of ethanol is shorter than that of butan-1-ol. Explain.
A: Butan-1-ol has more carbon atoms, so stronger id–id forces with the non-polar liquid stationary phase, and it is less volatile. It spends longer dissolved in the stationary phase, so it takes longer to reach the detector.
Q: A GLC trace has three peaks with areas of 3.0, 9.0 and 3.0 units. Calculate the percentage of the largest.
A: Total area \(= 3.0 + 9.0 + 3.0 = 15.0\). \(9.0 / 15.0 \times 100 = 60.0\,\%\).
Q: State the number of peaks in the ¹³C NMR spectrum of (a) ethanol, (b) propanone, (c) 2,2-dimethylpropane, \(\ce{C(CH3)4}\), (d) ethanoic acid.
A: (a) 2 (\(\ce{CH3}\), \(\ce{CH2OH}\)). (b) 2 (two equivalent \(\ce{CH3}\), C=O). (c) 2 (four equivalent \(\ce{CH3}\), one central carbon). (d) 2 (\(\ce{CH3}\), \(\ce{COOH}\)).
Q: How many signals are there in the ¹H NMR spectrum of (a) ethane, (b) propanone, (c) ethanal?
A: (a) 1: all six hydrogens are equivalent. (b) 1: all six hydrogens are in two equivalent \(\ce{CH3}\) groups. (c) 2: \(\ce{CH3}\) and \(\ce{CHO}\).
Q: What splitting pattern would a \(\ce{CH2}\) group show if it had (a) no hydrogens on adjacent carbons, (b) one, (c) two, (d) three?
A: (a) singlet. (b) doublet. (c) triplet. (d) quartet.
Q: Give the shift range and splitting of the \(\ce{CHO}\) signal in ethanal, \(\ce{CH3CHO}\).
A: The aldehyde hydrogen is in the range 9.3–10.5. The adjacent \(\ce{CH3}\) has three hydrogens, so it is a quartet.
Q: Explain why TMS is used as the NMR standard.
A: All twelve hydrogens are equivalent so it gives a single sharp signal; it is chemically inert; it is volatile so it is easily removed; and its signal is at δ = 0, upfield of most other signals.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ On a TLC plate, the baseline is 1.0 cm from the bottom of the plate, the solvent front reached 8.5 cm from the bottom, and a spot is centred 5.1 cm from the bottom. Calculate the Rf value of the spot.
A: Distance moved by spot \(= 5.1 - 1.0 = 4.1\) cm; distance moved by solvent front \(= 8.5 - 1.0 = 7.5\) cm. [M1]
\(R_f = 4.1 / 7.5\) [M1]
\(= 0.55\) (0.547 to 3 s.f.), no unit. [A1]
Q: [3 marks] ★ Two compounds, P and Q, are separated by TLC on silica with a non-polar solvent. P has Rf = 0.20 and Q has Rf = 0.75. Explain which of the two is the more polar.
A: P is more polar. [B1]
P is adsorbed more strongly on the polar silica (by hydrogen bonds or permanent dipole–dipole forces), so it spends more time held on the stationary phase. [B1]
Q is more soluble in the non-polar solvent, so it is carried further. [B1]
Q: [4 marks] ★★ A mixture of ethanol, propan-1-ol and butan-1-ol is analysed by GLC. The three peaks have retention times of 1.2, 2.5 and 4.8 min and areas of 5.2, 9.1 and 3.9 units. (a) Which peak is propan-1-ol? Explain. (b) Calculate the percentage of propan-1-ol in the mixture.
H: Longer chains have more electrons and stronger id–id forces with the stationary phase.
A: (a) The peak at 2.5 min. The retention time increases with chain length because of stronger id–id forces with the liquid stationary phase, so the order is ethanol, propan-1-ol, butan-1-ol. [B1] [B1]
(b) Total area \(= 5.2 + 9.1 + 3.9 = 18.2\) [M1]
\(9.1 / 18.2 \times 100 = 50.0\,\%\) [A1]
Q: [3 marks] ★ State the number of peaks in the ¹³C NMR spectrum of (a) pentan-3-one, \(\ce{CH3CH2COCH2CH3}\), (b) pentan-2-one, \(\ce{CH3COCH2CH2CH3}\), (c) 1,4-dimethylbenzene.
H: Look for symmetry first. 1,4-dimethylbenzene has a mirror plane through both methyl-bearing ring carbons.
A: (a) 3: \(\ce{CH3}\), \(\ce{CH2}\), C=O, since the two ethyl groups are equivalent. [B1]
(b) 5: all five carbons are different. [B1]
(c) 3: the two \(\ce{CH3}\) groups, the two ring carbons holding them, and the four ring carbons bearing hydrogen are each equivalent, so \(\ce{CH3}\), C–CH₃ and C–H give three. [B1]
Q: [4 marks] ★★ Predict the ¹H NMR spectrum of propan-2-ol, \(\ce{(CH3)2CHOH}\): the number of signals, and the area, splitting and shift range of each.
A: Three signals (three hydrogen environments). [B1]
\(\ce{(CH3)2}\): area 6, doublet (one neighbouring H), 0.9–1.7. [B1]
\(\ce{CH}\): area 1, multiplet (seven lines from six neighbouring H), 3.2–4.0. [B1]
O–H: area 1, singlet, 0.5–6.0. [B1]
Q: [4 marks] ★★ (a) Give two reasons why TMS is used as the standard in NMR spectroscopy. (b) Why is the solvent \(\ce{CDCl3}\) used rather than \(\ce{CHCl3}\)? (c) How does adding \(\ce{D2O}\) identify an O–H signal?
A: (a) Any two: one sharp signal because all the hydrogens are equivalent; inert; volatile so easily removed; signal at δ = 0, away from other signals. [B1] [B1]
(b) \(\ce{CHCl3}\) would give its own ¹H signal, and deuterium does not absorb in the ¹H region, so \(\ce{CDCl3}\) gives no ¹H signal. [B1]
(c) The O–H hydrogen exchanges with deuterium and its signal disappears. [B1]
Q: [6 marks] ★★ Compound R has the formula \(\ce{C4H8O2}\). Its IR spectrum has a strong absorption at 1740 cm⁻¹ and one at 1190 cm⁻¹, and no absorption between 2500 and 3600 cm⁻¹. Its ¹H NMR spectrum has three signals: δ 1.1 (triplet, 3H), δ 2.3 (quartet, 2H) and δ 3.7 (singlet, 3H). Deduce the structure of R and explain your reasoning.
H: Decide the functional group first. Then use splitting to join the pieces.
A: 1740 cm⁻¹ is C=O in the ester range (1710–1750) and 1190 is C–O; there is no broad O–H, so R is an ester. [B1]
δ 3.7, singlet, 3H: \(\ce{CH3-O}\) (range 3.2–4.0) with no neighbouring hydrogens. [B1]
δ 2.3, quartet, 2H: \(\ce{CH2}\) next to C=O (range 2.2–3.0), with three neighbouring hydrogens, so it is next to a \(\ce{CH3}\). [B1]
δ 1.1, triplet, 3H: \(\ce{CH3}\) (range 0.9–1.7) next to the \(\ce{CH2}\). [B1]
Structure: \(\ce{CH3CH2COOCH3}\), methyl propanoate. [B1]
It has four carbon environments, so four peaks in the ¹³C spectrum. [B1]
Q: [7 marks] ★★★ Compound S has the formula \(\ce{C3H7Cl}\). Its mass spectrum has peaks at m/e 78 and 80 with heights in the ratio 3 : 1. Its ¹H NMR spectrum has three signals: δ 1.0 (triplet, 3H), δ 1.7 (multiplet, 2H) and δ 3.5 (triplet, 2H). (a) Explain what the mass spectrum shows about the halogen. (b) Identify S, using the NMR data. (c) Explain why the isomer 2-chloropropane does not fit.
H: 2-chloropropane is \(\ce{CH3CHClCH3}\). How many signals would it give, and how would they split?
A: (a) The two peaks 2 mass units apart in a 3 : 1 ratio show one chlorine atom, from \(^{35}\)Cl and \(^{37}\)Cl in the ratio 3 : 1. [B1]
(b) δ 3.5, triplet, 2H: \(\ce{CH2}\) next to Cl (range 3.2–4.0) with two neighbouring hydrogens. [B1]
δ 1.0, triplet, 3H: \(\ce{CH3}\) next to a \(\ce{CH2}\). [B1]
δ 1.7, multiplet, 2H: a \(\ce{CH2}\) between them, with 3 + 2 = 5 neighbours. [B1]
S is 1-chloropropane, \(\ce{CH3CH2CH2Cl}\). [B1]
(c) 2-chloropropane has only two hydrogen environments, so two signals, not three. [B1]
They would be a doublet (6H) and a multiplet (1H), not two triplets. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Compound T has the formula \(\ce{C7H8O}\). Its ¹³C NMR spectrum has five peaks. Its ¹H NMR spectrum has four signals: δ 2.3 (singlet, 3H), δ 5.0 (singlet, 1H), δ 6.8 (doublet, 2H) and δ 7.1 (doublet, 2H). After shaking with \(\ce{D2O}\), the signal at δ 5.0 disappears. Identify T.
H: A benzene ring with two substituents that sit opposite each other has a mirror plane. How many different ring hydrogens does it have, and how are they split?
H: The signal that disappears with \(\ce{D2O}\) is O–H. The range for phenol O–H is 4.5–7.0.
A: The signal at δ 5.0 disappears with \(\ce{D2O}\), so it is O–H. It is in the phenol range 4.5–7.0, so T is a phenol. [B1]
δ 2.3, singlet, 3H, is \(\ce{CH3}\) attached to the ring (range 2.3–3.0) with no neighbouring hydrogens. [B1]
The two doublets at 6.8 and 7.1 (2H each) are in the aromatic range 6.0–9.0. Each ring hydrogen has one hydrogen on the adjacent carbon, which gives a doublet. [B1]
Two doublets of 2H each mean two pairs of equivalent ring hydrogens: the ring has two substituents opposite each other (1,4). [B1]
T is 4-methylphenol. Five ¹³C peaks agree: \(\ce{CH3}\), the ring carbon bonded to \(\ce{CH3}\), the ring carbon bonded to OH, and two pairs of CH carbons. [B1]
Q: [5 marks] ★★★ Methoxyethane \(\ce{CH3OCH2CH3}\), propan-1-ol and propan-2-ol all have the formula \(\ce{C3H8O}\). (a) Give the number of ¹³C peaks of each. (b) Give the number of ¹H signals of each. (c) Explain how adding \(\ce{D2O}\) would help to tell methoxyethane from the other two.
H: Methoxyethane has no O–H group.
A: (a) Methoxyethane 3, propan-1-ol 3, propan-2-ol 2. [B1]
(b) Methoxyethane 3 (\(\ce{CH3O}\), \(\ce{OCH2}\), \(\ce{CH3}\)); propan-1-ol 4 (\(\ce{CH3}\), \(\ce{CH2}\), \(\ce{CH2O}\), O–H); propan-2-ol 3 (\(\ce{CH3}\) ×2, \(\ce{CH}\), O–H). [B1] [B1]
(c) Propan-1-ol and propan-2-ol both have an O–H signal that disappears when \(\ce{D2O}\) is added. [B1]
Methoxyethane has no hydrogen on oxygen, so none of its signals disappears. [B1]
:::

:::quiz
? A TLC plate has a solvent front that moved 8.0 cm. A spot moved 6.0 cm. What is its Rf value?
- 1.33
+ 0.75
- 0.25
- 6.0
> Rf = 6.0 / 8.0 = 0.75. The value 1.33 comes from dividing the wrong way round, and an Rf can never be above 1. An Rf has no unit.
? Why is the baseline of a TLC plate drawn in pencil?
- Pencil is easier to see.
+ Graphite does not dissolve in the solvent.
- Ink reacts with silica.
- Pencil makes the spots move faster.
> Ink contains dyes that dissolve in the solvent and run up the plate with the samples, giving false spots. Graphite is insoluble.
? In gas–liquid chromatography, which of these makes the retention time of a compound longer?
- A less polar stationary phase.
- A lower boiling point of the compound.
+ Stronger interaction with the stationary phase.
- A faster flow of carrier gas.
> A compound that interacts strongly with the liquid stationary phase (and is less volatile) is held back longer. A faster gas flow shortens every retention time.
? How many peaks are there in the ¹³C NMR spectrum of propan-2-ol?
- 3
+ 2
- 1
- 4
> Propan-2-ol has three carbon atoms but the two methyl groups are equivalent by symmetry, so there are two environments: \(\ce{CH3}\) and \(\ce{CHOH}\).
? A \(\ce{CH2}\) group in an organic molecule is next to a \(\ce{CH3}\) group and to a carbon with no hydrogens. How is its ¹H NMR signal split?
- a triplet
+ a quartet
- a doublet
- a singlet
> The \(\ce{CH3}\) group has 3 hydrogens on the adjacent carbon, so n = 3 and n + 1 = 4 lines: a quartet. The other neighbour has no hydrogens and adds nothing.
? What happens to an O–H signal in a ¹H NMR spectrum when the sample is shaken with \(\ce{D2O}\)?
- It moves to a higher δ.
- It becomes a triplet.
+ It disappears.
- It doubles in area.
> The O–H hydrogen exchanges with deuterium, and deuterium does not give a signal in a ¹H spectrum. Hydrogens on carbon do not exchange.
? The integration ratio of the three signals of a compound with the formula \(\ce{C4H8O2}\) is 3 : 2 : 3. How many hydrogen atoms cause the signal with ratio 2?
- 1
+ 2
- 3
- 8
> The ratio adds up to 8, the number of hydrogens in the formula, so each number is the actual number of hydrogens.
:::

:::checklist What you can now do
- [ ] I can describe thin-layer chromatography, with the stationary and mobile phases, the baseline and the solvent front.
- [ ] I can calculate an Rf value and use Rf values of standards to interpret a chromatogram.
- [ ] I can explain Rf differences by adsorption on the stationary phase and solubility in the mobile phase.
- [ ] I can describe gas–liquid chromatography, its two phases and the meaning of retention time.
- [ ] I can find percentage composition from peak areas and explain retention times by interaction with the stationary phase.
- [ ] I can deduce the number of carbon environments in a ¹³C NMR spectrum, predict the number of peaks, and use the shift table.
- [ ] I can deduce proton environments from chemical shift, relative numbers from peak area, and neighbours from the n + 1 rule.
- [ ] I can predict the shifts and splitting of a ¹H NMR spectrum from a structure.
- [ ] I can state why TMS is the standard and why deuterated solvents are used, and use \(\ce{D2O}\) to identify O–H and N–H signals.
- [ ] I can combine IR, mass and NMR evidence to deduce a structure.
:::

:::recap
- TLC: stationary phase silica or aluminium oxide on a support, mobile phase a solvent, baseline in pencil above the solvent level. Rf = distance moved by spot ÷ distance moved by solvent front, from the baseline, between 0 and 1 with no unit. A high Rf means weaker adsorption and greater solubility in the solvent.
- GLC: stationary phase a high boiling point non-polar liquid on a solid support, mobile phase an unreactive gas. Retention time is longer for a less volatile compound that interacts more strongly with the stationary phase. Percentage composition = peak area ÷ total area × 100.
- ¹³C NMR: one line per carbon environment; equivalent carbons by symmetry give one line. Ranges: alkyl 0–50, next to O 50–70, C=C or ring 110–160, ester or acid C=O 160–185, ketone or aldehyde C=O 190–220.
- ¹H NMR: number of signals = number of hydrogen environments; shift shows what the hydrogens are next to; area ratio = ratio of hydrogens; n neighbouring hydrogens split a signal into n + 1 lines (singlet, doublet, triplet, quartet, multiplet).
- Hydrogens on the same carbon, and equivalent hydrogens, do not split each other. O–H and N–H signals are usually singlets.
- TMS, \(\ce{Si(CH3)4}\): δ = 0, one sharp signal, inert, volatile, upfield. Deuterated solvents (\(\ce{CDCl3}\)) give no ¹H signal. \(\ce{D2O}\) makes O–H and N–H signals disappear.
- Structure solving: formula, IR groups, ¹³C count, ¹H shifts, integration, splitting, assemble, check.
:::

:::links
- read: [Thin layer chromatography](https://www.chemguide.co.uk/analysis/chromatography/thinlayer.html) · Chemguide · how a TLC plate is run, why the spots separate, and Rf values
- read: [Gas-liquid chromatography](https://www.chemguide.co.uk/analysis/chromatography/gas.html) · Chemguide · how the column, carrier gas and detector work, and retention times
- read: [The background to NMR spectroscopy](https://www.chemguide.co.uk/analysis/nmr/background.html) · Chemguide · what a proton NMR spectrum is and what chemical shift means
- read: [High resolution NMR spectra](https://www.chemguide.co.uk/analysis/nmr/highres.html) · Chemguide · the n + 1 rule and splitting patterns explained
- read: [Interpreting C-13 NMR spectra](https://www.chemguide.co.uk/analysis/nmr/interpretc13.html) · Chemguide · counting carbon environments and reading shifts
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 24 October 2026.
:::

Next: [Practical skills and qualitative analysis](#chem.practical) turns from spectra to the laboratory: titrations, measurements, graphs and the tests for ions.
