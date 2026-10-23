@chapter chem.analysis
@title Infrared spectroscopy and mass spectrometry
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 5–7 hours
@summary Infrared spectra show which bonds a molecule contains, and mass spectra show its mass and how it breaks up. You will learn to read an IR spectrum with the Data table, find a molecular mass from M⁺, use the [M+1] and [M+2] peaks to count carbon atoms and spot chlorine or bromine, and calculate relative atomic masses from isotope abundances.

:::why
When a new compound is made, whether in a drug company, a forensic laboratory or an exam question, the first job is to find out what it is. Infrared (IR) spectroscopy tells you which bonds are present, and mass spectrometry tells you the molecular mass and the pieces the molecule breaks into. Together they identify most simple organic compounds in a few minutes. Paper 2 and Paper 4 both give you spectra to interpret, so the skill is worth practising until it is automatic.
:::

**Before you start**, you should know what isotopes are and how relative atomic mass is defined from [Atomic structure](#chem.atoms), and the functional groups and their names from [Introduction to organic chemistry](#chem.org.intro). The tests in [Organic synthesis (AS)](#chem.org.synthesis) are the chemical way of finding groups; this chapter is the instrument way. Chromatography and NMR spectroscopy come at A Level: [Chromatography and NMR spectroscopy](#chem.analysis2).

:::try Warm-up
Q: Chlorine has two isotopes, \(\ce{^{35}Cl}\) and \(\ce{^{37}Cl}\). How do their atoms differ? (from [Atomic structure](#chem.atoms))
A: They have the same number of protons (17) and electrons, but different numbers of neutrons: 18 and 20.
Q: Name the functional group in \(\ce{CH3CH2CHO}\) and in \(\ce{CH3COCH3}\). (from [Introduction to organic chemistry](#chem.org.intro))
A: An aldehyde (CHO at the end of the chain) and a ketone (C=O inside the chain).
Q: Define relative atomic mass. (from [Atomic structure](#chem.atoms))
A: The weighted mean mass of an atom of the element, taking account of its isotopes, relative to \(\tfrac{1}{12}\) of the mass of an atom of carbon-12.
:::

## Infrared spectroscopy

### Bonds vibrate, and absorb infrared radiation

The atoms in a molecule are never still. Each covalent bond acts like a spring: it stretches and relaxes many trillions of times a second, and it can also bend. A bond vibrates at a frequency that depends on two things: how strong the bond is, and how heavy the atoms are. Stronger bonds and lighter atoms vibrate faster.

If infrared radiation of exactly that frequency falls on the molecule, the bond **absorbs** it and vibrates more strongly. Radiation of other frequencies passes straight through. An **IR spectrometer** shines a range of infrared frequencies through a sample and records which ones are absorbed. Because a C=O bond vibrates at a different frequency from an O–H bond, the pattern of absorptions shows which bonds are in the molecule.

Infrared radiation is described by its **wavenumber**, the number of waves in one centimetre:

:::def Wavenumber
The number of wavelengths in one centimetre of radiation, \(\tilde{\nu} = 1/\lambda\) with \(\lambda\) in cm, measured in cm⁻¹. A larger wavenumber means a higher frequency and a higher energy.
:::

For example, radiation of wavenumber 3000 cm⁻¹ has \(\lambda = 1/3000 = 3.33 \times 10^{-4}\,\mathrm{cm}\), which is 3.33 micrometres. Organic compounds absorb between about 4000 and 500 cm⁻¹.

:::analogy
A bond is like a guitar string. A thin, tight string (a light atom on a strong bond, such as O–H) vibrates at a high pitch. A thick, loose string (two heavier atoms joined by a weaker single bond, such as C–O) vibrates at a lower one. A triple bond is a tighter string than a double bond, which is tighter than a single bond. The spectrometer finds the notes.
:::

### The IR spectrum and the Data table

An IR spectrum plots **transmittance** (the percentage of radiation that gets through the sample) against wavenumber. Where the sample absorbs, less radiation gets through, so each absorption appears as a **downward dip**. Wavenumber is plotted **from high on the left to low on the right**: this is the opposite of most graphs and is a favourite trap.

The Data section of the syllabus gives the wavenumber range for each bond. You are given this table in the exam, so you do not need to memorise numbers, but you must know how to use it and which ranges overlap.

| Bond | Wavenumber range / cm⁻¹ | Appears in |
|---|---|---|
| O–H, hydroxy | 3200–3600 | alcohols |
| O–H, carboxyl | 2500–3000 | carboxylic acids |
| N–H | 3300–3500 | amines and amides |
| C–H | 2850–2950 | alkyl groups, nearly every organic compound |
| C≡N | 2200–2250 | nitriles |
| C=O, carbonyl and carboxyl | 1670–1740 | aldehydes, ketones, carboxylic acids |
| C=O, ester | 1710–1750 | esters |
| C=O, amide | 1640–1690 | amides |
| C=C | 1500–1680 | alkenes and arenes |
| C–O | 1040–1300 | alcohols, esters, carboxylic acids |

The region **below about 1500 cm⁻¹** is called the **fingerprint region**. It holds a dense pattern of absorptions from many bending and stretching motions of the whole molecule, which differs for every compound even when the functional groups are the same. If the fingerprint region of an unknown matches a spectrum in a database, the compound is identified. At AS you use the region above about 1500 cm⁻¹ to find groups, and you may use the C–O range, which sits in the fingerprint region, as supporting evidence.

:::warn Four traps in reading a spectrum
1. **The axis runs backwards.** 4000 is on the left and 500 on the right. A dip at the left of the sheet is a high wavenumber.
2. **Use the range, not a single number.** Say "an absorption at about 1710 cm⁻¹, in the range 1670–1740, so C=O". Do not quote one number from the table.
3. **Shape matters.** An alcohol O–H is a broad dip; a carboxylic acid O–H is *very* broad and extends under the C–H absorptions; a C=O is a sharp, strong dip.
4. **C–H is everywhere.** The C–H absorption at 2850–2950 is in almost every organic compound, so it identifies nothing. Look for the other absorptions.
:::

### Three spectra to compare

The three sketches below show where each compound absorbs. They are drawn to show the positions and shapes only, using the syllabus ranges; a real spectrum has more small dips in the fingerprint region.

:::html
<figure class="fig small"><svg viewBox="0 0 340 194" role="img" aria-label="Sketch of the infrared spectrum of ethanol: a broad O–H dip centred near 3350, a C–H dip just below 3000 and a C–O dip near 1060 cm⁻¹"><path class="ax" d="M40 150 H325" marker-end="url(#ahm)"/><path class="ax" d="M40 150 V16" marker-end="url(#ahm)"/><path class="ln-m thin" d="M40 150 v4"/><text class="ts tc" x="40" y="166">4000</text><path class="ln-m thin" d="M120 150 v4"/><text class="ts tc" x="120" y="166">3000</text><path class="ln-m thin" d="M200 150 v4"/><text class="ts tc" x="200" y="166">2000</text><path class="ln-m thin" d="M240 150 v4"/><text class="ts tc" x="240" y="166">1500</text><path class="ln-m thin" d="M280 150 v4"/><text class="ts tc" x="280" y="166">1000</text><path class="ln-m thin" d="M320 150 v4"/><text class="ts tc" x="320" y="166">500</text><text class="tl tc" x="180" y="186">wavenumber / cm⁻¹</text><text class="tl" x="46" y="14">transmittance / %</text><path class="ln-m thin dash" d="M240 22 V150"/><text class="tl" x="245" y="14">fingerprint</text><path class="c1 sw2" d="M40 32L62 32.2L64 32.5L66 32.9L68 33.8L70 35.2L72 37.6L74 41.1L76 46.1L78 52.8L80 61L82 70.6L84 80.7L86 90.3L88 98.4L90 103.7L92 105.6L94 103.7L96 98.4L98 90.3L100 80.7L102 70.6L104 61L106 52.8L108 46.1L110 41.1L112 37.6L114 35.2L116 33.9L118 34.2L120 39.3L122 54.3L124 75.4L126 85.4L128 83.6L130 77L132 52.9L134 35.8L136 32.3L236 32.1L238 32.8L240 36.6L242 45L244 50.7L246 48.1L248 49.3L250 50.7L252 41L254 33.6L256 32.1L264 32L266 32.4L268 35L270 46.8L272 75.1L274 107.5L276 111.5L278 82.2L280 51.1L282 36.5L284 34.1L286 39.5L288 50.4L290 54.7L292 46L294 36.3L296 32.7L298 32.1L320 32"/><text class="tl tc" x="92" y="122">O–H</text><text class="tl tc" x="127.2" y="104">C–H</text><text class="tl tc" x="275.2" y="132">C–O</text></svg><figcaption>Sketch of the IR spectrum of ethanol. The O–H dip is broad and lies at 3200–3600 cm⁻¹. There is no C=O dip between 1670 and 1740 cm⁻¹.</figcaption></figure>
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 194" role="img" aria-label="Sketch of the infrared spectrum of ethanoic acid: a very broad O–H dip between 2500 and 3000, a sharp strong C=O dip near 1710 and a C–O dip near 1280 cm⁻¹"><path class="ax" d="M40 150 H325" marker-end="url(#ahm)"/><path class="ax" d="M40 150 V16" marker-end="url(#ahm)"/><path class="ln-m thin" d="M40 150 v4"/><text class="ts tc" x="40" y="166">4000</text><path class="ln-m thin" d="M120 150 v4"/><text class="ts tc" x="120" y="166">3000</text><path class="ln-m thin" d="M200 150 v4"/><text class="ts tc" x="200" y="166">2000</text><path class="ln-m thin" d="M240 150 v4"/><text class="ts tc" x="240" y="166">1500</text><path class="ln-m thin" d="M280 150 v4"/><text class="ts tc" x="280" y="166">1000</text><path class="ln-m thin" d="M320 150 v4"/><text class="ts tc" x="320" y="166">500</text><text class="tl tc" x="180" y="186">wavenumber / cm⁻¹</text><text class="tl" x="46" y="14">transmittance / %</text><path class="ln-m thin dash" d="M240 22 V150"/><text class="tl" x="245" y="14">fingerprint</text><path class="c1 sw2" d="M40 32L66 32.3L68 32.3L70 32.5L72 32.6L74 32.8L76 33L78 33.3L80 33.7L82 34.1L84 34.6L86 35.3L88 36L90 37L92 38L94 39.3L96 40.7L98 42.3L100 44.1L102 46.2L104 48.4L106 50.9L108 53.6L110 56.4L112 59.4L114 62.5L116 65.7L118 69L120 73.2L122 80L124 89.3L126 93.9L128 91.1L130 88.2L132 88.4L134 89.7L136 90.9L138 91.6L140 91.8L142 91.6L144 90.9L146 89.7L148 88.1L150 86.1L152 83.8L154 81.2L156 78.3L158 75.3L160 72.1L162 68.9L164 65.7L166 62.5L168 59.4L170 56.4L172 53.6L174 50.9L176 48.4L178 46.2L180 44.1L182 42.3L184 40.7L186 39.3L188 38L190 37L192 36L194 35.3L196 34.6L198 34.1L200 33.7L202 33.3L204 33L206 32.8L208 32.6L210 32.5L212 32.3L214 32.3L216 32.7L218 38L220 63.6L222 107.7L224 114L226 72L228 40.8L230 32.9L232 32.1L238 32.1L240 32.9L242 38L244 51.5L246 63.8L248 58.4L250 46.3L252 49.7L254 71.2L256 97L258 105L260 87.6L262 60.6L264 42L266 34.4L268 32.4L270 32.2L272 32.7L274 34L276 37L278 42.5L280 50.6L282 59.8L284 66.8L286 68.7L288 64.5L290 56.2L292 47.1L294 40L296 35.5L298 33.3L300 32.4L302 32.1L320 32"/><text class="tl tc" x="140" y="116">O–H</text><text class="tl tc" x="223.2" y="137">C=O</text><text class="tl tc" x="257.6" y="122">C–O</text></svg><figcaption>Sketch of the IR spectrum of ethanoic acid. The carboxyl O–H dip is very broad (2500–3000 cm⁻¹), and the C=O dip is sharp and strong (1670–1740 cm⁻¹).</figcaption></figure>
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 194" role="img" aria-label="Sketch of the infrared spectrum of propanone: a C–H dip just below 3000 and a sharp strong C=O dip near 1715 cm⁻¹, with no O–H dip"><path class="ax" d="M40 150 H325" marker-end="url(#ahm)"/><path class="ax" d="M40 150 V16" marker-end="url(#ahm)"/><path class="ln-m thin" d="M40 150 v4"/><text class="ts tc" x="40" y="166">4000</text><path class="ln-m thin" d="M120 150 v4"/><text class="ts tc" x="120" y="166">3000</text><path class="ln-m thin" d="M200 150 v4"/><text class="ts tc" x="200" y="166">2000</text><path class="ln-m thin" d="M240 150 v4"/><text class="ts tc" x="240" y="166">1500</text><path class="ln-m thin" d="M280 150 v4"/><text class="ts tc" x="280" y="166">1000</text><path class="ln-m thin" d="M320 150 v4"/><text class="ts tc" x="320" y="166">500</text><text class="tl tc" x="180" y="186">wavenumber / cm⁻¹</text><text class="tl" x="46" y="14">transmittance / %</text><path class="ln-m thin dash" d="M240 22 V150"/><text class="tl" x="245" y="14">fingerprint</text><path class="c1 sw2" d="M40 32L114 32.2L116 33.3L118 38.6L120 51.2L122 66.3L124 71.6L126 69.1L128 65.5L130 53L132 39.1L134 33.2L136 32.1L214 32L216 32.9L218 41L220 72.9L222 115.7L224 109.3L226 64.2L228 38L230 32.5L232 32L238 32L240 32.5L242 36.6L244 49L246 56.5L248 53.2L250 57.9L252 58.3L254 46.6L256 38.7L258 41.4L260 49.4L262 54.8L264 52.3L266 44.2L268 37L270 33.4L272 32.3L320 32"/><text class="tl tc" x="125.6" y="96">C–H</text><text class="tl tc" x="222.8" y="138">C=O</text></svg><figcaption>Sketch of the IR spectrum of propanone. The sharp, strong C=O dip is the main feature, and there is no broad dip at 3200–3600 or 2500–3000 cm⁻¹, so no O–H group.</figcaption></figure>
:::

Compare the three. Ethanol has the broad O–H dip but no C=O. Ethanoic acid has both, with the O–H spread over a much wider and lower range. Propanone has the C=O but no O–H at all. The broadening of O–H comes from hydrogen bonding between molecules, which is strongest in a carboxylic acid because its molecules pair up.

:::steps
1. Look at 1670–1750 cm⁻¹. A strong, sharp dip is a C=O group (carbonyl compound, acid or ester).
2. Look at 3200–3600 cm⁻¹ for a broad O–H (alcohol), and at 2500–3000 cm⁻¹ for a very broad O–H (carboxylic acid). C=O plus a very broad O–H means a carboxylic acid.
3. C=O with no O–H points to an aldehyde, ketone or ester. An ester has a C–O absorption (1040–1300 cm⁻¹) as well.
4. Look at 3300–3500 cm⁻¹ for N–H, and 2200–2250 cm⁻¹ for C≡N.
5. Look at 1500–1680 cm⁻¹ for C=C.
6. Ignore the C–H dip, and write down the evidence for each group as "wavenumber range → bond → group".
:::

:::eg Compound A has the formula \(\ce{C3H6O2}\). Its IR spectrum has absorptions at about 2500–3000 cm⁻¹ (very broad), 1710 cm⁻¹ (strong) and 1250 cm⁻¹. Identify the functional group and suggest the compound.
The very broad absorption at 2500–3000 cm⁻¹ is the O–H of a carboxylic acid. [B1]

The strong absorption at 1710 cm⁻¹ is in the range 1670–1740 cm⁻¹ for C=O. [B1]

The 1250 cm⁻¹ absorption is in the range 1040–1300 cm⁻¹ for C–O. [B1]

Together these show a carboxylic acid group, \(\ce{-COOH}\). With the formula \(\ce{C3H6O2}\), the remaining atoms are \(\ce{C2H5}\), so A is propanoic acid, \(\ce{CH3CH2COOH}\). [B1]

Its isomer methyl ethanoate, \(\ce{CH3COOCH3}\), also has C=O and C–O absorptions, but no O–H absorption, so it is ruled out. [B1]
:::

:::eg Propan-1-ol is warmed with acidified dichromate(VI) and the product is distilled off. Its IR spectrum shows a strong sharp absorption at 1730 cm⁻¹ and no broad absorption at 3200–3600 cm⁻¹. In a second experiment the mixture is refluxed, and the product shows a very broad absorption at 2500–3000 cm⁻¹ and a strong absorption at 1710 cm⁻¹. Explain these two spectra.
In the first experiment the O–H absorption of the alcohol has gone and a C=O absorption has appeared (1730 lies in 1670–1740), so the alcohol has been oxidised to the aldehyde, propanal. [B1]

In the second the very broad 2500–3000 absorption is the carboxylic acid O–H, and 1710 is the C=O of the acid, so reflux with excess oxidant has gone on to propanoic acid. [B1]

IR can follow a reaction: the loss of a reactant absorption and the appearance of a product absorption show that the change has happened. [B1]
:::

:::exam IR answers that score
Name the bond, give the range from the Data table, and say what group it shows: "the absorption at 1715 cm⁻¹ is in the range 1670–1740 cm⁻¹, so C=O, a carbonyl group". Also say what is *missing*, because the absence of a broad absorption at 3200–3600 cm⁻¹ rules out an alcohol. Aldehydes and ketones cannot be told apart from the IR C=O absorption alone; use a chemical test or the mass spectrum.
:::

## Mass spectrometry

### What a mass spectrum is

A **mass spectrometer** turns a sample into positive ions, sorts the ions by mass, and counts them. In the instrument the vaporised sample is bombarded with high-energy electrons. A collision knocks an electron out of a molecule, M, and leaves a positive ion:

\[\ce{M(g) + e- -> M^+(g) + 2e-}\]

The ions are accelerated and separated by their **mass-to-charge ratio**, m/e. Almost all the ions have a charge of +1, so m/e is the mass of the ion on the relative scale. (How the instrument separates the ions is not needed for the syllabus.)

The result is a **mass spectrum**: a bar chart with m/e on the x-axis and the **relative abundance** of the ions (how many reach the detector, as a percentage of the tallest peak) on the y-axis.

### The molecular ion

The ion formed by losing one electron from the whole molecule is the **molecular ion**, \(\ce{M^+}\). It has almost the same mass as the molecule, because an electron is so light. So the **peak at the highest m/e** (apart from the small isotope peaks described later) gives the relative molecular mass.

:::def Molecular ion peak
The peak in a mass spectrum formed by the molecule that has lost one electron, \(\ce{M^+}\). Its m/e value is the relative molecular mass, \(M_r\), of the compound.
:::

### Fragmentation

The molecular ion carries a lot of energy, and many of the M⁺ ions break apart. A bond breaks and the ion splits into two pieces: a positive **fragment ion** and an uncharged piece that is a free radical. For propanone:

\[\ce{[CH3COCH3]^+ -> CH3CO^+ + CH3^.}\]

Only the positive ion is detected. The radical has no charge, so it is not accelerated and is not seen. Each peak in the spectrum is therefore a positively charged fragment. The weakest bonds break most often, and the fragments that form the most stable cations give the tallest peaks.

You must recognise a short list of fragments. Learn how each m/e value is added up from the relative atomic masses (H 1, C 12, O 16).

| Fragment | m/e | Sum |
|---|---|---|
| \(\ce{CH3+}\) | 15 | 12 + 3 |
| \(\ce{C2H5+}\) | 29 | 24 + 5 |
| \(\ce{CHO+}\) | 29 | 12 + 1 + 16 |
| \(\ce{CH2OH+}\) | 31 | 12 + 2 + 16 + 1 |
| \(\ce{CH3CO+}\) | 43 | 12 + 3 + 12 + 16 |
| \(\ce{C3H7+}\) | 43 | 36 + 7 |
| \(\ce{COOH+}\) | 45 | 12 + 16 + 16 + 1 |

Two fragments can have the same m/e (29 for both \(\ce{C2H5+}\) and \(\ce{CHO+}\); 43 for both \(\ce{CH3CO+}\) and \(\ce{C3H7+}\)). The rest of the spectrum and the structure of the molecule tell you which is more likely.

:::warn Write the charge
A fragment peak is a **cation**. Write \(\ce{CH3+}\), never \(\ce{CH3}\); and never confuse the fragment with the radical that is lost. In "the peak at 43 is \(\ce{CH3CO}\)" the charge is missing, and the mark may not be given.
:::

You can also find fragments by subtraction. If M⁺ is at 58 and a peak is at 43, the difference of 15 is a lost \(\ce{CH3}\) group. If a peak is 45 below M⁺, a \(\ce{COOH}\) group has been lost. Differences of 15 (\(\ce{CH3}\)), 29 (\(\ce{C2H5}\) or \(\ce{CHO}\)) and 17 (OH) are common.

:::html
<figure class="fig small"><svg viewBox="0 0 340 194" role="img" aria-label="Simplified mass spectrum of propanone with peaks at m/e 15, 43 and 58; the tallest peak is at 43 and the molecular ion peak is at 58"><path class="ax" d="M40 150H328" marker-end="url(#ahm)"/><path class="ax" d="M40 150V22" marker-end="url(#ahm)"/><path class="ln-m thin" d="M40 150v4"/><text class="ts tc" x="40" y="166">0</text><path class="ln-m thin" d="M80 150v4"/><text class="ts tc" x="80" y="166">10</text><path class="ln-m thin" d="M120 150v4"/><text class="ts tc" x="120" y="166">20</text><path class="ln-m thin" d="M160 150v4"/><text class="ts tc" x="160" y="166">30</text><path class="ln-m thin" d="M200 150v4"/><text class="ts tc" x="200" y="166">40</text><path class="ln-m thin" d="M240 150v4"/><text class="ts tc" x="240" y="166">50</text><path class="ln-m thin" d="M280 150v4"/><text class="ts tc" x="280" y="166">60</text><path class="ln-m thin" d="M320 150v4"/><text class="ts tc" x="320" y="166">70</text><text class="tl tc" x="180" y="186">m/e</text><text class="tl" x="46" y="14">relative abundance / %</text><path class="c1 sw3" d="M100 150V126"/><text class="tl tc" x="100" y="119">15 CH₃⁺</text><path class="c1 sw3" d="M212 150V50"/><text class="tl tc" x="212" y="43">43 CH₃CO⁺</text><path class="c1 sw3" d="M272 150V116"/><text class="tl tc" x="272" y="109">58 M⁺</text></svg><figcaption>Simplified mass spectrum of propanone (the three main peaks, with approximate heights). The peak at m/e 58 is the molecular ion, so the relative molecular mass is 58. The tallest peak, at 43, is the base peak: CH₃CO⁺.</figcaption></figure>
:::

:::def Base peak
The tallest peak in a mass spectrum, given a relative abundance of 100 %. It is the most abundant ion and is often a fragment, not the molecular ion.
:::

:::warn The molecular ion is not always the tallest peak
The molecular ion is the peak at the **highest m/e** (ignoring the tiny isotope peaks next to it), however short it is. The tallest peak is the **base peak**, and for propanone it is the fragment at 43. Reading the base peak as M⁺ gives the wrong \(M_r\). Some molecules fragment so easily that M⁺ is very small.
:::

:::eg The mass spectrum of a compound with \(M_r = 58\) has peaks at m/e 15, 43 and 58, and the peak at 43 is the tallest. IR shows a strong absorption at 1715 cm⁻¹ and no absorption above 3000 cm⁻¹. Suggest a structure.
The peak at 58 is M⁺, so \(M_r = 58\). [B1]

IR: the absorption at 1715 cm⁻¹ is in the range 1670–1740, so C=O is present, and there is no O–H, so it is not an alcohol or acid. [B1]

The peak at 43 is \(\ce{CH3CO+}\) (12 + 3 + 12 + 16 = 43), which shows a \(\ce{CH3-CO}\) unit. [B1]

The peak at 15 is \(\ce{CH3+}\). [B1]

The compound is propanone, \(\ce{CH3COCH3}\) (\(M_r = 36 + 6 + 16 = 58\)). Propanal, \(\ce{CH3CH2CHO}\), has the same \(M_r\), but it has no \(\ce{CH3CO}\) group and its characteristic fragments are at 29 (\(\ce{C2H5+}\) or \(\ce{CHO+}\)), so propanone fits better. [B1]
:::

:::lab Mass spectrometry in the real world
Laboratories use mass spectrometry to test athletes' urine for banned drugs, to check that food and water are free of contaminants, to identify unknown samples at crime scenes, and to measure the isotopes in ancient samples for dating. In all of them the idea is this chapter's: ionise, sort by m/e, compare with known patterns.
:::

:::board
AQA's course also explains how a time-of-flight mass spectrometer works: the sample is ionised, the ions are accelerated to the same kinetic energy, and the time they take to fly along a tube depends on their mass. Cambridge 9701 states that the working of the instrument is not required.
:::

## Isotopes and the relative atomic mass

An element with more than one isotope gives a mass spectrum with one peak per isotope. The height of each peak is proportional to the abundance of that isotope. The spectrum of magnesium is an example (the data are real).

:::html
<figure class="fig small"><svg viewBox="0 0 320 172" role="img" aria-label="Mass spectrum of magnesium with peaks at m/e 24, 25 and 26 and relative abundances 79, 10 and 11 percent"><path class="ax" d="M40 130H300" marker-end="url(#ahm)"/><path class="ax" d="M40 130V14" marker-end="url(#ahm)"/><text class="tl" x="46" y="12">relative abundance / %</text><path class="c1 sw3" d="M90 130V51"/><text class="tl tc" x="90" y="44">79</text><text class="ts tc" x="90" y="146">24</text><path class="c1 sw3" d="M160 130V120"/><text class="tl tc" x="160" y="113">10</text><text class="ts tc" x="160" y="146">25</text><path class="c1 sw3" d="M230 130V119"/><text class="tl tc" x="230" y="112">11</text><text class="ts tc" x="230" y="146">26</text><text class="tl tc" x="170" y="164">m/e</text></svg><figcaption>Mass spectrum of magnesium. The three peaks are the isotopes ²⁴Mg, ²⁵Mg and ²⁶Mg, each as the singly charged ion.</figcaption></figure>
:::

The relative atomic mass is the weighted mean of the isotope masses. Multiply each mass by its abundance, add, and divide by the total abundance:

:::formula Relative atomic mass from isotopes
\[A_r = \frac{\sum (\text{isotopic mass} \times \text{abundance})}{\sum \text{abundance}}\]
Abundances can be percentages, relative heights or fractions: the units cancel. The sum of the abundances in the denominator is 100 when percentages are used.
:::

:::eg Calculate the relative atomic mass of magnesium from the spectrum: \(^{24}\)Mg 79 %, \(^{25}\)Mg 10 %, \(^{26}\)Mg 11 %.
Multiply each mass by its abundance and add: \(24 \times 79 + 25 \times 10 + 26 \times 11 = 1896 + 250 + 286 = 2432\). [M1]

Divide by the total abundance, \(79 + 10 + 11 = 100\): \(A_r = 2432 / 100 = 24.32\). [M1]

To 3 significant figures (and 1 d.p.), \(A_r = 24.3\), which is the value in the Periodic Table. [A1]
:::

:::eg A sample of chlorine contains 75.8 % \(^{35}\)Cl and 24.2 % \(^{37}\)Cl. Calculate its relative atomic mass.
\[A_r = \frac{35 \times 75.8 + 37 \times 24.2}{100} = \frac{2653 + 895.4}{100} = 35.48\] [M1] [A1]

The answer is 35.5 to 3 s.f., which is why the Periodic Table gives 35.5 and not a whole number. The mean lies closer to 35 because most atoms are \(^{35}\)Cl. [B1]
:::

You can also work the other way. If you know the relative atomic mass and there are only two isotopes, an unknown abundance can be found by letting the abundance of one be \(x\)% and the other \((100 - x)\)%.

:::eg Boron has two isotopes, \(^{10}\)B and \(^{11}\)B, and its relative atomic mass is 10.8. Calculate the percentage of each isotope.
Let the abundance of \(^{10}\)B be \(x\) %. Then \(^{11}\)B is \((100 - x)\) %. [B1]
\[\frac{10x + 11(100 - x)}{100} = 10.8\] [M1]
\[1100 - x = 1080 \quad\Rightarrow\quad x = 20\] [M1]

So boron is 20 % \(^{10}\)B and 80 % \(^{11}\)B. [A1]
:::

:::warn Whole-number masses give a slightly different answer for heavy elements
Isotope masses are exact values that are not quite whole numbers. Bromine, with \(^{79}\)Br 50.7 % and \(^{81}\)Br 49.3 %, gives \(A_r = (79 \times 50.7 + 81 \times 49.3)/100 = 79.99\) from mass numbers, but the Periodic Table says 79.9. In exam questions the data are chosen to match the table; use the numbers you are given.
:::

## The [M+1] peak: counting carbon atoms

Look closely at the molecular ion of a hydrocarbon or other carbon compound and you find a small second peak at one mass unit higher. It is called the **[M+1]⁺ peak**. It comes from molecules in which one carbon atom is the heavier isotope \(^{13}\)C instead of \(^{12}\)C. About 1.1 % of carbon atoms are \(^{13}\)C.

If a molecule has one carbon atom, then about 1.1 molecules in every 100 contain \(^{13}\)C, so the [M+1]⁺ peak is about 1.1 % of the height of M⁺. If it has \(n\) carbon atoms, each has a 1.1 % chance, so the [M+1]⁺ peak is about \(1.1n\) % of M⁺. Rearranging gives the number of carbon atoms:

:::formula Number of carbon atoms from the [M+1]⁺ peak
\[n = \frac{100 \times \text{abundance of } [\mathrm{M}+1]^+}{1.1 \times \text{abundance of } \mathrm{M}^+}\]
\(n\) is the number of carbon atoms in the molecule. Round to the nearest whole number. Other isotopes (\(^2\)H, \(^{15}\)N, \(^{17}\)O) are ignored at this level.
:::

:::eg In the mass spectrum of a hydrocarbon the molecular ion peak has an abundance of 25.0 % and the [M+1]⁺ peak 1.10 %. How many carbon atoms does the molecule contain?
\[n = \frac{100 \times 1.10}{1.1 \times 25.0} = \frac{110}{27.5} = 4.0\] [M1] [A1]

The molecule contains four carbon atoms. [B1]
:::

The result tells you the number of carbons, not the structure. Combined with \(M_r\) it can give the molecular formula. A hydrocarbon with 4 carbons and \(M_r = 58\) has \(58 - 48 = 10\) hydrogens, so \(\ce{C4H10}\).

## The [M+2] peak: chlorine and bromine

Chlorine and bromine have two common isotopes that are two mass units apart, so compounds containing them show a second peak at M + 2.

| Element | Isotopes and abundance | Ratio |
|---|---|---|
| chlorine | \(^{35}\)Cl about 75 %, \(^{37}\)Cl about 25 % | 3 : 1 |
| bromine | \(^{79}\)Br about 50 %, \(^{81}\)Br about 50 % | 1 : 1 |

A molecule with one chlorine atom is either \(^{35}\)Cl (the M⁺ peak) or \(^{37}\)Cl (the [M+2]⁺ peak), in the ratio 3 : 1. A molecule with one bromine atom gives M⁺ and [M+2]⁺ peaks of almost equal height.

:::html
<figure class="fig small"><svg viewBox="0 0 340 158" role="img" aria-label="Molecular ion peaks of chloroethane at m/e 64 and 66 in the ratio 3 to 1, and of bromoethane at m/e 108 and 110 with almost equal heights"><path class="ax" d="M20 130H160" marker-end="url(#ahm)"/><text class="tl tc" x="90" y="14">C₂H₅Cl</text><path class="c1 sw3" d="M60 130V40"/><text class="tl tc" x="60" y="33">64</text><path class="c1 sw3" d="M100 130V100.3"/><text class="tl tc" x="100" y="93.3">66</text><text class="tl tc" x="90" y="150">m/e</text><path class="ax" d="M190 130H330" marker-end="url(#ahm)"/><text class="tl tc" x="260" y="14">C₂H₅Br</text><path class="c1 sw3" d="M230 130V40"/><text class="tl tc" x="230" y="33">108</text><path class="c1 sw3" d="M270 130V41.8"/><text class="tl tc" x="270" y="34.8">110</text><text class="tl tc" x="260" y="150">m/e</text></svg><figcaption>Molecular ion region of chloroethane (a 3 : 1 pair, m/e 64 and 66) and of bromoethane (an almost 1 : 1 pair, m/e 108 and 110). The pair of peaks, two units apart, is the sign of one Cl or one Br.</figcaption></figure>
:::

The widget below draws the molecular-ion region for any formula with C, H, N, O, Cl and Br. Start with \(\ce{C2H5Br}\), then try \(\ce{C2H5Cl}\), and then \(\ce{CH2Cl2}\) and \(\ce{CH2Br2}\) to see what happens with two halogen atoms. The widget draws only the molecular-ion region, not the fragments.

:::html
<div class="widget" data-w="chem-ms" data-formula="C2H5Br"></div>
:::

### Two halogen atoms

When a molecule has two chlorine atoms, each atom can independently be \(^{35}\)Cl or \(^{37}\)Cl, and the ratios multiply. The probabilities are 3/4 for \(^{35}\)Cl and 1/4 for \(^{37}\)Cl.

:::eg Show that the molecular ion peaks of \(\ce{CH2Cl2}\) are in the ratio 9 : 6 : 1, and give their m/e values.
Both atoms \(^{35}\)Cl: probability \(\tfrac34 \times \tfrac34 = \tfrac{9}{16}\). The mass is \(12 + 2 + 35 + 35 = 84\). [B1]

One \(^{35}\)Cl and one \(^{37}\)Cl: this can happen in two ways, so the probability is \(2 \times \tfrac34 \times \tfrac14 = \tfrac{6}{16}\). The mass is 86. [B1]

Both atoms \(^{37}\)Cl: probability \(\tfrac14 \times \tfrac14 = \tfrac{1}{16}\). The mass is 88. [B1]

So M : [M+2] : [M+4] = 9 : 6 : 1, at m/e 84, 86 and 88. [B1]

The pattern is \((3 + 1)^2 = 9 + 6 + 1\), and the same method gives 1 : 2 : 1 for two bromine atoms (\((1+1)^2\)) and 3 : 4 : 1 for one chlorine and one bromine (\((3+1)(1+1) = 3 + 4 + 1\)). [B1]
:::

:::eg The mass spectrum of a halogenoalkane has peaks at m/e 78 (relative height 75), 80 (25) and 43 (100). Identify the compound.
The peaks at 78 and 80 are in the ratio 75 : 25 = 3 : 1, two mass units apart, so the molecule contains one chlorine atom (\(^{35}\)Cl and \(^{37}\)Cl). [B1]

\(M_r = 78\) (for the \(^{35}\)Cl molecule). Subtracting chlorine, \(78 - 35 = 43\), which is \(\ce{C3H7}\) (\(36 + 7\)). The formula is \(\ce{C3H7Cl}\). [B1]

The peak at 43 is the base peak, \(\ce{C3H7+}\), formed by loss of a chlorine atom. It has no chlorine in it, so it appears as a single peak, not a pair. [B1]

The compound is 1-chloropropane or 2-chloropropane; the mass spectrum alone cannot tell which. [B1]
:::

:::tip Fragments with a halogen show the pair too
If a fragment contains the chlorine or bromine atom, it shows the same pair of peaks as M⁺. A fragment without the halogen is a single peak. This tells you where the halogen is. In bromoethane the \(\ce{C2H5+}\) fragment at m/e 29 is a single peak, while the fragment \(\ce{CH2Br+}\) at 93 and 95 is a 1 : 1 pair.
:::

## Ar calculator

A second tab of the widget calculates a relative atomic mass from up to four isotopes. Type in the isotopic masses and abundances (percentages or relative heights) and it gives \(A_r\) with a bar chart of the spectrum. Try chlorine (35 and 37 with 75.8 and 24.2), magnesium, and then your own example.

:::html
<div class="widget" data-w="chem-ms" data-tab="ar"></div>
:::

## Putting infrared and mass spectra together

IR finds the functional groups, and the mass spectrum finds the molecular mass and pieces. A good answer uses both and checks that the structure fits all the evidence. Work through the evidence in this order: \(M_r\) from M⁺, carbon count from [M+1], halogens from [M+2], groups from IR, then the fragments to settle the structure.

:::eg (Exam style) Compound P has these properties. Its mass spectrum has M⁺ at m/e 74 with an abundance of 20.0 %, an [M+1]⁺ peak of 0.66 % and a fragment at m/e 45. Its IR spectrum has absorptions at 2500–3000 (very broad) and 1710 cm⁻¹. Identify P.
**Carbons.** \(n = \dfrac{100 \times 0.66}{1.1 \times 20.0} = \dfrac{66}{22.0} = 3.0\), so P has three carbon atoms. [M1] [A1]

**Formula.** \(M_r = 74\). Three carbons weigh 36, leaving 38 for hydrogen and other atoms. The IR shows a carboxylic acid (two oxygens, 32), leaving \(38 - 32 = 6\) for hydrogen, so the formula is \(\ce{C3H6O2}\). [M1]

**Groups.** The very broad 2500–3000 absorption is the O–H of a carboxylic acid and 1710 is its C=O (in the range 1670–1740). [B1]

**Fragment.** The peak at 45 is \(\ce{COOH+}\) (12 + 16 + 16 + 1 = 45). Taking this away from M⁺: \(74 - 45 = 29\), which is \(\ce{C2H5}\). [B1]

P is propanoic acid, \(\ce{CH3CH2COOH}\). [A1]
:::

:::eg Spot the error: the mass spectrum of a compound shows peaks at m/e 15, 29, 43 and 58, and the peak at 43 is the tallest. A student writes "The tallest peak is the molecular ion, so the relative molecular mass is 43. The peak at 58 is a fragment." [2 marks]
The student reads the **base peak** as the molecular ion and takes the Mr as 43. **This is wrong: the molecular ion is the peak at the highest m/e, here 58, so \(M_r = 58\) [B0].** The tallest peak is the base peak (100 % abundance), and 43 is a fragment.

Correct answer: \(M_r = 58\), because the peak with the highest m/e is the molecular ion. [B1]

The peak at 43 is a fragment ion, formed when M⁺ loses 15 (a \(\ce{CH3}\) group): it could be \(\ce{CH3CO+}\) or \(\ce{C3H7+}\). [B1]

The student scores 0 out of 2. Always ask which peak has the highest m/e before you look at the heights.
:::

:::try Start easy, finish at exam standard
Q: Use the Data table to say which bond absorbs at (a) 1720 cm⁻¹, (b) 3400 cm⁻¹ (broad), (c) 2230 cm⁻¹.
A: (a) C=O (carbonyl, 1670–1740). (b) O–H of an alcohol (3200–3600), or N–H (3300–3500) if the absorption were sharper. (c) C≡N (2200–2250), a nitrile.
Q: The IR spectrum of an unknown liquid has a strong absorption at 1740 cm⁻¹ and one at 1240 cm⁻¹, with no absorption between 2500 and 3600 cm⁻¹. Suggest the functional group.
A: An ester. C=O in the ester range 1710–1750, C–O in 1040–1300, and no O–H.
Q: Calculate the m/e value of the fragment \(\ce{CH3CH2CO+}\).
A: The fragment is \(\ce{C3H5O+}\): \(36 + 5 + 16 = 57\).
Q: Calculate the relative atomic mass of silicon from the spectrum: \(^{28}\)Si 92.2 %, \(^{29}\)Si 4.7 %, \(^{30}\)Si 3.1 %.
A: \[A_r = \frac{28 \times 92.2 + 29 \times 4.7 + 30 \times 3.1}{100} = \frac{2810.9}{100} = 28.1\]
Q: The molecular ion of a hydrocarbon has an abundance of 18.0 % and the [M+1]⁺ peak 0.99 %. How many carbons does it have?
A: \(n = 100 \times 0.99 / (1.1 \times 18.0) = 99 / 19.8 = 5.0\), so five carbon atoms.
Q: A compound has peaks at m/e 94 and 96 of almost equal height. What does this show?
A: One bromine atom (\(^{79}\)Br and \(^{81}\)Br in a 1 : 1 ratio).
Q: What is the ratio of the heights of the M, M+2 and M+4 peaks for a compound with two bromine atoms?
A: 1 : 2 : 1, from \((1 + 1)^2\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State the two absorptions in the IR spectrum of ethanoic acid that show it is a carboxylic acid, with their wavenumber ranges.
A: Very broad O–H absorption at 2500–3000 cm⁻¹. [B1]
Strong C=O absorption at 1670–1740 cm⁻¹. [B1]
Q: [2 marks] ★ In the mass spectrum of an organic compound the peak with the highest m/e is at 88. State what this peak is and give the relative molecular mass.
A: It is the molecular ion peak, \(\ce{M^+}\), the molecule that has lost one electron. [B1]
\(M_r = 88\). [B1]
Q: [4 marks] ★★ Compounds A and B both have the formula \(\ce{C4H8O2}\). A has IR absorptions at about 3000 cm⁻¹ (very broad) and 1710 cm⁻¹. B has absorptions at 1740 cm⁻¹ and 1240 cm⁻¹ only, apart from C–H. Identify the functional group in each, using the Data table.
A: A: the very broad absorption at 2500–3000 cm⁻¹ is the O–H of a carboxylic acid [B1], and 1710 cm⁻¹ is C=O (range 1670–1740). [B1]
B: 1740 cm⁻¹ is in the ester C=O range 1710–1750 [B1], and 1240 cm⁻¹ is C–O (1040–1300). There is no O–H absorption, so B is an ester. [B1]
Q: [3 marks] ★★ (#chem.atoms) The mass spectrum of neon shows peaks at m/e 20 (90.5 %), 21 (0.3 %) and 22 (9.2 %). Calculate the relative atomic mass of neon to 3 significant figures.
A: \(20 \times 90.5 + 21 \times 0.3 + 22 \times 9.2 = 1810 + 6.3 + 202.4 = 2018.7\) [M1]
Divide by the total abundance, \(90.5 + 0.3 + 9.2 = 100.0\): [M1]
\(A_r = 20.187 = 20.2\) [A1]
Q: [4 marks] ★★ The molecular ion peak of a hydrocarbon has an abundance of 40.0 % and its [M+1]⁺ peak an abundance of 2.64 %. The molecular ion is at m/e 86. Find the number of carbon atoms and the molecular formula.
H: Work out how many carbon atoms there are, then find the number of hydrogen atoms from the remaining mass.
A: \(n = 100 \times 2.64 / (1.1 \times 40.0) = 264 / 44.0 = 6.0\) [M1] [A1]
Six carbons weigh 72, leaving \(86 - 72 = 14\) for hydrogen. [M1]
The formula is \(\ce{C6H14}\). [A1]
Q: [5 marks] ★★ The molecular ion region of compound Q consists of peaks at m/e 92 and 94 in the ratio 3 : 1. The base peak is at m/e 57. (a) State what the 3 : 1 pair shows. (b) Deduce the molecular formula of Q, given that the compound is a saturated halogenoalkane. (c) Explain why the base peak at 57 is a single peak.
H: Subtract the mass of chlorine from 92, then find the alkyl group.
A: (a) Q contains one chlorine atom: \(^{35}\)Cl and \(^{37}\)Cl in a 3 : 1 ratio. [B1]
(b) \(92 - 35 = 57\), which is \(\ce{C4H9}\) (48 + 9). [M1] The formula is \(\ce{C4H9Cl}\). [A1]
(c) The fragment \(\ce{C4H9+}\) (57) has lost the chlorine atom [B1], so it contains no chlorine and has no isotope pair. [B1]
Q: [8 marks] ★★★ Compound R has the following data. Mass spectrum: M⁺ at m/e 88 with an abundance of 12.5 %, an [M+1]⁺ peak of 0.55 % and a base peak at m/e 43. IR spectrum: strong absorptions at 1735 cm⁻¹ and 1240 cm⁻¹; no absorption between 2500 and 3600 cm⁻¹. Deduce the number of carbon atoms, the molecular formula, the functional group and a structure for R.
H: Use the carbon count and the IR to find the oxygen atoms. An ester has two oxygens.
H: Look at the fragment at 43: which fragment containing C, H and O has m/e 43?
A: Carbons: \(n = 100 \times 0.55 / (1.1 \times 12.5) = 55 / 13.75 = 4.0\). [M1] [A1]
Four carbons weigh 48. An ester contains two oxygen atoms (32), leaving \(88 - 48 - 32 = 8\) for hydrogen: \(\ce{C4H8O2}\). [M1] [A1]
The 1735 cm⁻¹ absorption is C=O in the ester range 1710–1750, and 1240 cm⁻¹ is C–O (1040–1300); there is no O–H, so R is an ester. [B1] [B1]
The base peak at 43 is \(\ce{CH3CO+}\), so the acid part is ethanoate. [B1]
R is ethyl ethanoate, \(\ce{CH3COOCH2CH3}\). [B1]
Q: [6 marks] ★★★ The mass spectrum of compound S has two molecular ion peaks, at m/e 122 and 124, of equal height, and a base peak at m/e 43. The IR spectrum of S has no absorption between 1670 and 1740 cm⁻¹ or between 3200 and 3600 cm⁻¹. (a) Deduce the halogen present and the molecular formula of S. (b) Identify the fragment that gives the base peak and explain why it is a single peak. (c) State what the IR data show.
H: Equal heights, two units apart, point to one halogen. Subtract its mass from 122.
A: (a) The pair of equal height two units apart shows bromine (\(^{79}\)Br and \(^{81}\)Br). [B1] \(122 - 79 = 43\), which is \(\ce{C3H7}\), so S is \(\ce{C3H7Br}\). [M1] [A1]
(b) The base peak is \(\ce{C3H7+}\) (36 + 7 = 43). [B1] It no longer contains bromine, so there is no isotope pair. [B1]
(c) There is no C=O and no O–H, so S is not a carbonyl compound, acid, ester or alcohol. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A sample of element E contains only two isotopes, of masses 69 and 71, and its relative atomic mass is 69.7. (a) Calculate the percentage abundance of each isotope. (b) A diatomic molecule of E could be formed from any combination of the two isotopes. Predict the m/e values and the ratio of the heights of the peaks for the molecular ion of \(\ce{E2}\).
H: For (a), let the abundance of the lighter isotope be \(x\) %.
H: For (b), the method for two chlorine atoms applies: the probabilities multiply. Use the fractions found in (a).
A: (a) \(\dfrac{69x + 71(100 - x)}{100} = 69.7\) [M1], so \(7100 - 2x = 6970\) and \(x = 65\). [M1] Abundances: 65 % of mass 69 and 35 % of mass 71. [A1]
(b) The molecular ion can have masses \(69 + 69 = 138\), \(69 + 71 = 140\) and \(71 + 71 = 142\). [B1]
Heights are in the ratio \(0.65^2 : 2(0.65)(0.35) : 0.35^2 = 0.4225 : 0.455 : 0.1225\), which is about 3.4 : 3.7 : 1. [B1]
Q: [5 marks] ★★★ The compound \(\ce{CH2BrCl}\) is analysed in a mass spectrometer. (a) Predict the m/e values and the relative heights of the molecular ion peaks, taking \(^{35}\)Cl : \(^{37}\)Cl as 3 : 1 and \(^{79}\)Br : \(^{81}\)Br as 1 : 1. (b) State and explain how the fragment peaks \(\ce{CH2Cl+}\) and \(\ce{CH2Br+}\) differ.
H: Combine the two ratios as you would two chlorine atoms: write each as a bracket and multiply.
A: (a) M = 12 + 2 + 79 + 35 = 128, so the peaks are at 128, 130 and 132. [B1]
\((3 + 1)(1 + 1) = 3 + 3 + 1 + 1 = 3 + 4 + 1\): heights 3 : 4 : 1. [M1] [A1]
(b) \(\ce{CH2Cl+}\) (m/e 49 and 51) is a 3 : 1 pair; \(\ce{CH2Br+}\) (m/e 93 and 95) is a 1 : 1 pair. [B1]
Each fragment keeps one halogen atom, so each shows the pattern of that halogen alone. [B1]
:::

:::quiz
? In a mass spectrum, which peak gives the relative molecular mass of the compound?
- the tallest peak
+ the peak at the highest m/e (ignoring the small isotope peaks beside it)
- the peak at the lowest m/e
- the peak at m/e 100
> The molecular ion is the whole molecule minus one electron, so it has the highest m/e. The tallest peak is the base peak, and it is often a fragment.
? An IR spectrum has a very broad absorption between 2500 and 3000 cm⁻¹ and a strong absorption at 1710 cm⁻¹. Which functional group does the compound contain?
- an alcohol
- a ketone
- an ester
+ a carboxylic acid
> The very broad range 2500–3000 is the O–H of a carboxylic acid, and 1710 is its C=O. An alcohol O–H is 3200–3600; a ketone and an ester have no O–H.
? The [M+1]⁺ peak of a hydrocarbon is 3.30 % when the molecular ion is 50.0 %. How many carbon atoms does it have?
- 3
- 5
+ 6
- 66
> \(n = 100 \times 3.30 / (1.1 \times 50.0) = 330 / 55.0 = 6.0\). Forgetting the factor 1.1 would give 6.6 and a wrong answer, and the factor 100 puts the abundances in percentages.
? A compound has two molecular ion peaks, two mass units apart, with heights in the ratio 3 : 1. Which element does it contain?
- bromine
+ chlorine
- one carbon-13 atom
- two carbon atoms
> \(^{35}\)Cl and \(^{37}\)Cl occur in the ratio 3 : 1, giving M and [M+2] peaks at that ratio. Bromine gives an almost 1 : 1 pair. A carbon-13 atom raises the mass by one unit, not two.
? Which is the m/e value of the fragment \(\ce{CH3CO+}\)?
- 28
- 42
+ 43
- 44
> 12 + 3 + 12 + 16 = 43. A peak at 42 would lack a hydrogen, and 44 would have an extra one. The positive charge does not change the mass.
? A sample of an element has two isotopes: 10 % of mass 20 and 90 % of mass 22. What is its relative atomic mass?
- 21.0
- 20.2
+ 21.8
- 22.0
> \((20 \times 10 + 22 \times 90)/100 = (200 + 1980)/100 = 21.8\). The simple mean 21.0 ignores the abundances, and the answer must lie closer to the more abundant isotope.
:::

:::checklist What you can now do
- [ ] I can analyse an IR spectrum of a simple molecule and identify functional groups using the wavenumber ranges in the Data section.
- [ ] I can analyse a mass spectrum in terms of m/e values and the abundances of its peaks.
- [ ] I can calculate a relative atomic mass from isotope abundances or a mass spectrum, and find an abundance from a relative atomic mass.
- [ ] I can find the relative molecular mass of a compound from its molecular ion peak.
- [ ] I can identify simple fragments (CH₃⁺, C₂H₅⁺, CHO⁺, CH₂OH⁺, CH₃CO⁺, C₃H₇⁺, COOH⁺) from their m/e values.
- [ ] I can find the number of carbon atoms in a molecule from the [M+1]⁺ peak.
- [ ] I can tell from the [M+2]⁺ peak whether a compound contains chlorine or bromine, and predict the pattern for two halogen atoms.
- [ ] I can combine IR and mass spectrum data to identify a simple compound.
:::

:::recap
- A bond absorbs IR at a wavenumber set by its strength and the masses of its atoms. Spectra are plotted with wavenumber falling from left to right, and absorptions are downward dips. Below about 1500 cm⁻¹ is the fingerprint region.
- Key ranges (cm⁻¹): O–H alcohol 3200–3600; O–H acid 2500–3000 (very broad); N–H 3300–3500; C–H 2850–2950; C≡N 2200–2250; C=O 1670–1740 (ester 1710–1750); C=C 1500–1680; C–O 1040–1300.
- In a mass spectrum, M⁺ is the peak at the highest m/e and gives \(M_r\). The tallest peak is the base peak. Fragments are cations, and the radical lost is not detected.
- Fragments: CH₃⁺ 15, C₂H₅⁺ and CHO⁺ 29, CH₂OH⁺ 31, CH₃CO⁺ and C₃H₇⁺ 43, COOH⁺ 45.
- \(A_r = \Sigma(\text{mass} \times \text{abundance}) / \Sigma\text{abundance}\).
- Carbon atoms: \(n = 100 \times [\mathrm{M}+1] / (1.1 \times \mathrm{M})\).
- [M+2]: one Cl gives a 3 : 1 pair; one Br gives a 1 : 1 pair. Two Cl give M : M+2 : M+4 = 9 : 6 : 1; two Br give 1 : 2 : 1.
:::

:::links
- read: [Infra-red spectroscopy (menu)](https://www.chemguide.co.uk/analysis/irmenu.html) · Chemguide · why bonds absorb, and how to read the spectra of simple compounds
- read: [Interpreting an infra-red spectrum](https://www.chemguide.co.uk/analysis/ir/interpret.html) · Chemguide · identifying common bonds in the spectrum of a carboxylic acid, with the ranges
- read: [Mass spectrometry (menu)](https://www.chemguide.co.uk/analysis/masspecmenu.html) · Chemguide · the molecular ion, fragmentation, and the M+1 and M+2 peaks
- read: [Mass spectra: the M+2 peak](https://www.chemguide.co.uk/analysis/masspec/mplus2.html) · Chemguide · why chlorine and bromine give pairs of peaks, including two chlorine atoms
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Lattice energy, entropy and Gibbs free energy](#chem.lattice) starts the A Level physical chemistry.
