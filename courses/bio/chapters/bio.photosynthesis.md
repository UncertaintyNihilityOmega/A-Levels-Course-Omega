@chapter bio.photosynthesis
@title Photosynthesis
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 5–6 hours
@summary Photosynthesis transfers light energy to chemical energy in organic molecules. You will learn how a chloroplast is built for the job, how the pigments absorb light (absorption and action spectra, and chromatography with Rf values), how the light-dependent stage makes ATP, reduced NADP and oxygen by cyclic and non-cyclic photophosphorylation, and how the Calvin cycle uses them to fix carbon dioxide into triose phosphate.

:::why
Every food chain starts with photosynthesis, and the oxygen in the air comes from it. Exam questions ask you to follow light energy, electrons, protons and carbon through the chloroplast, to read spectra and chromatograms, and to predict what happens to ATP, reduced NADP, GP and RuBP when something is blocked or removed. Learn it as one connected story: light makes the energy carriers, and the energy carriers build sugar.
:::

**Before you start**, you should know the structure of a chloroplast from [Eukaryotic cells and organelles](#bio.cells), the proton gradient and ATP synthase from [Aerobic respiration](#bio.respiration), ATP and reduced coenzymes from [Energy, ATP and respiratory quotient](#bio.energy), and how an enzyme works from [Enzymes](#bio.enzymes).

:::try Warm-up
Q: How many membranes surround a chloroplast, and what is a stack of thylakoids called? (from [Eukaryotic cells and organelles](#bio.cells))
A: Two membranes (the envelope). A stack of thylakoids is a granum (plural grana).
Q: In a mitochondrion, what do the protons do after they have been pumped into the intermembrane space? (from [Aerobic respiration](#bio.respiration))
A: They flow back into the matrix down their gradient, through ATP synthase, by facilitated diffusion. The energy released makes ATP from ADP and \(\mathrm{P_i}\).
Q: Name the coenzyme that carries hydrogen in glycolysis and the Krebs cycle, and say what it is called once it has accepted hydrogen. (from [Aerobic respiration](#bio.respiration))
A: NAD; reduced NAD.
:::

## The big picture

Animals, fungi and most bacteria get their energy from the chemical energy in food. Plants, algae and some bacteria get theirs from light. They use it to build organic molecules from two simple inorganic ones, carbon dioxide and water.

:::def Photosynthesis
The process in which light energy is transferred to chemical energy in complex organic molecules, made from carbon dioxide and water, with oxygen released as a by-product.
:::

\[\ce{6CO2 + 6H2O ->[\text{light}] C6H12O6 + 6O2}\]

That equation hides two very different stages, and almost every question in this chapter depends on knowing which one is which.

| | Light-dependent stage | Light-independent stage (Calvin cycle) |
|---|---|---|
| Where | thylakoid membranes and thylakoid spaces, in the grana | stroma |
| Needs | light, water, ADP, \(\mathrm{P_i}\), NADP | carbon dioxide, RuBP, ATP, reduced NADP |
| Makes | ATP, reduced NADP, oxygen | triose phosphate (then carbohydrates, lipids, amino acids) |
| Energy change | light energy to chemical energy in ATP and reduced NADP | chemical energy in ATP and reduced NADP to chemical energy in organic molecules |

**NADP** is a coenzyme that works like NAD in respiration. It accepts electrons and a proton (hydrogen) and becomes **reduced NADP**, a carrier of hydrogen and energy. Write "reduced NADP", never "NADPH".

:::key The two stages in one box
1. The **light-dependent stage** (in the thylakoids) transfers energy from light to **ATP** and **reduced NADP**, and releases **oxygen**.
2. The **light-independent stage**, the **Calvin cycle** (in the stroma), uses that ATP and reduced NADP to turn **carbon dioxide** into **triose phosphate**, from which complex organic molecules are built.
3. ATP and reduced NADP used up in the Calvin cycle go back to the thylakoids as ADP, \(\mathrm{P_i}\) and NADP, ready to be charged again.
:::

:::warn "Light-independent" does not mean "in the dark"
The Calvin cycle needs no light of its own, but it cannot run without the ATP and reduced NADP that only the light-dependent stage makes. So it stops soon after the light goes out (you will see the evidence in the data question on GP and RuBP below). Never write that it "happens at night".
:::

## The chloroplast: structure and function

:::def Chloroplast
An organelle of plant and algal cells that contains chlorophyll and is the site of photosynthesis. It is surrounded by an envelope of two membranes.
:::

<figure class="fig small"><svg viewBox="0 0 360 274" role="img" aria-label="Labelled drawing of a chloroplast. Two membranes form the envelope. Inside, stacks of flattened thylakoids called grana are joined by single thylakoids, in a fluid stroma that also holds a circular DNA molecule, 70S ribosomes, a starch grain and lipid droplets."><path class="fm s-acc sw2" d="M284 150L283.2 158.4L280.8 166.6L276.8 174.5L271.4 182L264.6 189L256.5 195.3L247.2 200.8L237 205.4L226 209.1L214.3 211.8L202.3 213.5L190 214L177.7 213.5L165.7 211.8L154 209.1L143 205.4L132.8 200.8L123.5 195.3L115.4 189L108.6 182L103.2 174.5L99.2 166.6L96.8 158.4L96 150L96.8 141.6L99.2 133.4L103.2 125.5L108.6 118L115.4 111L123.5 104.7L132.8 99.2L143 94.6L154 90.9L165.7 88.2L177.7 86.5L190 86L202.3 86.5L214.3 88.2L226 90.9L237 94.6L247.2 99.2L256.5 104.7L264.6 111L271.4 118L276.8 125.5L280.8 133.4L283.2 141.6Z"/><path class="f1 s-acc sw2" d="M277 150L276.3 157.4L274 164.8L270.4 171.8L265.3 178.5L259 184.7L251.5 190.3L243 195.2L233.5 199.4L223.3 202.7L212.5 205.1L201.4 206.5L190 207L178.6 206.5L167.5 205.1L156.7 202.7L146.5 199.4L137 195.2L128.5 190.3L121 184.7L114.7 178.5L109.6 171.8L106 164.8L103.7 157.4L103 150L103.7 142.6L106 135.2L109.6 128.2L114.7 121.5L121 115.3L128.5 109.7L137 104.8L146.5 100.6L156.7 97.3L167.5 94.9L178.6 93.5L190 93L201.4 93.5L212.5 94.9L223.3 97.3L233.5 100.6L243 104.8L251.5 109.7L259 115.3L265.3 121.5L270.4 128.2L274 135.2L276.3 142.6Z"/><rect class="f2 s-acc2 sw2" x="131" y="112" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="131" y="121" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="131" y="130" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="131" y="139" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="175" y="124" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="175" y="133" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="175" y="142" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="175" y="151" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="219" y="100" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="219" y="109" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="219" y="118" width="34" height="6" rx="3"/><rect class="f2 s-acc2 sw2" x="219" y="127" width="34" height="6" rx="3"/><path class="ln" d="M165 128L175 136"/><path class="ln" d="M209 134L219 120"/><circle class="fp ln" cx="118" cy="160" r="8"/><ellipse class="fp s-acc sw2" cx="224" cy="188" rx="14" ry="9"/><circle class="fa s-acc sw2" cx="140" cy="182" r="4.5"/><circle class="fa s-acc sw2" cx="150" cy="190" r="4.5"/><circle class="fi" cx="262" cy="150" r="2.4"/><circle class="fi" cx="267" cy="159" r="2.4"/><circle class="fi" cx="259" cy="165" r="2.4"/><text class="tl" x="6" y="36">envelope</text><text class="tl" x="6" y="50">(2 membranes)</text><path class="ln-m thin" d="M60 56L116 115"/><text class="tl" x="6" y="116">stroma</text><path class="ln-m thin" d="M52 118L118 140"/><text class="tl" x="6" y="212">circular DNA</text><path class="ln-m thin" d="M70 198L113 164"/><text class="tl" x="6" y="262">lipid droplet</text><path class="ln-m thin" d="M60 248L137 184"/><text class="tl" x="190" y="16" text-anchor="middle">single thylakoid</text><path class="ln-m thin" d="M188 20L171 131"/><text class="tl" x="294" y="36">thylakoid</text><path class="ln-m thin" d="M290 40L250 103"/><text class="tl" x="294" y="82">granum</text><path class="ln-m thin" d="M290 86L252 128"/><text class="tl" x="294" y="170">70S</text><text class="tl" x="294" y="184">ribosomes</text><path class="ln-m thin" d="M290 174L270 162"/><text class="tl" x="294" y="226">starch</text><text class="tl" x="294" y="240">grain</text><path class="ln-m thin" d="M290 230L237 193"/></svg><figcaption>A chloroplast in section (a drawing, not a photograph). The grana hold the light-dependent stage; the stroma holds the enzymes of the light-independent stage.</figcaption></figure>

Each part has a job. Read the table as "feature, so function".

| Feature | What it is | How it helps photosynthesis |
|---|---|---|
| **Envelope** | two membranes | controls what enters and leaves, so the stroma has a different composition from the cytoplasm |
| **Thylakoid membranes** | flattened sacs with pigments, electron transport chains and ATP synthase in their membranes | site of the light-dependent stage |
| **Grana** | stacks of thylakoids | a very large surface area of membrane for light absorption and for ATP synthesis, in a small volume |
| **Thylakoid space** | the small space inside each thylakoid | protons pumped into it quickly build up a steep proton gradient |
| **Single thylakoids** | membranes joining one granum to the next | link the grana so that substances can pass between them |
| **Stroma** | the fluid around the grana | holds the enzymes of the Calvin cycle (including rubisco); close to the grana, so ATP and reduced NADP have a short distance to travel |
| **Starch grains** | insoluble grains of starch | store the carbohydrate made by photosynthesis, without changing the water potential |
| **Lipid droplets** | small drops of lipid | store lipid made from triose phosphate |
| **Circular DNA and 70S ribosomes** | like those of prokaryotes | the chloroplast makes some of its own proteins |

**Recognise it** in an electron micrograph: an oval structure with a double boundary, with neat stacks of dark discs (grana) in a paler stroma that may hold pale grey starch grains and small black lipid droplets. A mitochondrion has folds across its inside (cristae); a chloroplast has stacks of discs.

:::eg Describe how you would recognise a chloroplast in an electron micrograph and explain how its structure is related to its function in photosynthesis.
A model answer gives recognition points and then links structure to function.

It is a large oval organelle with an envelope of two membranes, containing stacks of thylakoids (grana) joined by single thylakoids, in a stroma. [B1]

The grana give a large surface area of thylakoid membrane, so more pigment, electron transport chains and ATP synthase fit in to make ATP and reduced NADP. [B1]

The thylakoid space is small, so protons pumped into it quickly build up a high concentration and a steep proton gradient for ATP synthase. [B1]

The stroma contains the enzymes of the Calvin cycle, including rubisco, next to the grana, so ATP and reduced NADP made in the grana are used close by. [B1]

The stroma may contain starch grains, which store the carbohydrate made by the Calvin cycle in an insoluble form. [B1]

A weaker answer says "it has grana to absorb light". It never mentions the envelope, the proton gradient or where the Calvin cycle happens, and "to absorb light" is not linked to surface area, so it scores one mark at most.
:::

## Pigments: how a leaf catches light

Light is a form of energy that travels as waves. Visible light has wavelengths from about 400 nm (blue-violet) to about 700 nm (red). A pigment is a molecule that absorbs some wavelengths and reflects or transmits the others.

Chloroplasts contain four kinds of pigment, all in the thylakoid membranes.

| Pigment | Colour in a solvent | Role |
|---|---|---|
| **Chlorophyll a** | blue-green | the **primary pigment**: found in the reaction centre of each photosystem |
| **Chlorophyll b** | yellow-green | accessory pigment |
| **Carotene** | orange-yellow | accessory pigment |
| **Xanthophyll** | yellow | accessory pigment |

:::def Photosystem
A group of photosynthetic pigment molecules and proteins in a thylakoid membrane. The pigments form a **light-harvesting complex** around a **reaction centre** that contains a molecule of chlorophyll a. There are two kinds, photosystem I (PSI) and photosystem II (PSII).
:::

The pigments of the light-harvesting complex (chlorophyll a, chlorophyll b, carotene and xanthophyll) absorb light and pass the energy inwards, from molecule to molecule, to the reaction centre. Only the chlorophyll a of the reaction centre then takes part in the electron transfers described below.

**Why have accessory pigments?** Each pigment absorbs best at its own wavelengths. A mixture of pigments therefore absorbs a **wider range of wavelengths**, so more of the light that reaches the leaf is used. Carotene and xanthophyll absorb mainly in the blue part of the spectrum; chlorophylls absorb mainly in the blue-violet and the red.

:::warn Chlorophyll does not absorb green
A leaf looks green because green light is the part that chlorophyll absorbs least. It is reflected (or transmitted) to your eye. If you say "chlorophyll absorbs green light and reflects red and blue", you lose the mark.
:::

:::note PSI and PSII
The two photosystems are named in the order they were discovered. Their reaction-centre chlorophyll a absorbs best at slightly different wavelengths, about 700 nm in PSI and about 680 nm in PSII. You do not need these numbers; you do need to know that both contain chlorophyll a.
:::

## Absorption spectra and action spectra

:::def Absorption spectrum
A graph of how much light a pigment (or a mixture of pigments) absorbs at each wavelength.
:::

:::def Action spectrum
A graph of the rate of photosynthesis at each wavelength of light.
:::

<figure class="fig small"><svg viewBox="0 0 340 458" role="img" aria-label="Two graphs against wavelength in nanometres from 400 to 700. Graph A, absorption spectra of chlorophyll a, chlorophyll b and carotene: chlorophyll a absorbs most in the blue-violet near 430 nanometres and the red near 660, chlorophyll b near 450 and 640, and carotene broadly from 420 to 500; all three absorb very little between 500 and 600. Graph B, an action spectrum: the rate of photosynthesis has two peaks, in the blue-violet and in the red, and a low point in the green, matching the combined absorption."><text class="tl tb" x="10" y="22">A  Absorption spectra</text><text class="tl" x="10" y="42">absorbance</text><path class="ax" d="M56 190L56 52" marker-end="url(#ahm)"/><path class="ax" d="M52 190L322 190" marker-end="url(#ahm)"/><path class="ax" d="M56 190L56 194"/><text class="ts" x="56" y="207" text-anchor="middle">400</text><path class="ax" d="M142.667 190L142.667 194"/><text class="ts" x="142.667" y="207" text-anchor="middle">500</text><path class="ax" d="M229.333 190L229.333 194"/><text class="ts" x="229.333" y="207" text-anchor="middle">600</text><path class="ax" d="M316 190L316 194"/><text class="ts" x="316" y="207" text-anchor="middle">700</text><text class="tl" x="190" y="226" text-anchor="middle">wavelength / nm</text><text class="tl tb" x="10" y="262">B  An action spectrum</text><text class="tl" x="10" y="282">rate of photosynthesis</text><path class="ax" d="M56 410L56 292" marker-end="url(#ahm)"/><path class="ax" d="M52 410L322 410" marker-end="url(#ahm)"/><path class="ax" d="M56 410L56 414"/><text class="ts" x="56" y="427" text-anchor="middle">400</text><path class="ax" d="M142.667 410L142.667 414"/><text class="ts" x="142.667" y="427" text-anchor="middle">500</text><path class="ax" d="M229.333 410L229.333 414"/><text class="ts" x="229.333" y="427" text-anchor="middle">600</text><path class="ax" d="M316 410L316 414"/><text class="ts" x="316" y="427" text-anchor="middle">700</text><text class="tl" x="190" y="446" text-anchor="middle">wavelength / nm</text><path class="c1 sw2" d="M56 168.6L59.5 157.7L62.9 143.8L66.4 127.5L69.9 109.9L73.3 92.9L76.8 78.4L80.3 68.7L83.7 65.2L87.2 68.4L90.7 77.8L94.1 91.9L97.6 108.7L101.1 126L104.5 142L108 155.5L111.5 166.1L114.9 173.7L118.4 178.8L121.9 182L125.3 183.8L128.8 184.6L132.3 185L135.7 185L139.2 184.9L142.7 184.8L146.1 184.6L149.6 184.4L153.1 184.2L156.5 184L160 183.9L163.5 183.7L166.9 183.6L170.4 183.6L173.9 183.5L177.3 183.5L180.8 183.5L184.3 183.6L187.7 183.6L191.2 183.7L194.7 183.9L198.1 184L201.6 184.2L205.1 184.4L208.5 184.6L212 184.8L215.5 185L218.9 185.3L222.4 185.5L225.9 185.8L229.3 186.1L232.8 186.3L236.3 186.6L239.7 186.8L243.2 187L246.7 187L250.1 186.7L253.6 185.8L257.1 183.5L260.5 179L264 171.4L267.5 159.9L270.9 144.8L274.4 127.7L277.9 111.5L281.3 99.8L284.8 95.6L288.3 100.1L291.7 112L295.2 128.4L298.7 145.7L302.1 161L305.6 172.7L309.1 180.5L312.5 185.3L316 187.8"/><path class="c2 sw2" d="M56 189.3L59.5 188.8L62.9 187.9L66.4 186.3L69.9 183.6L73.3 179.3L76.8 173L80.3 164.2L83.7 152.8L87.2 139.1L90.7 124L94.1 109L97.6 95.7L101.1 86.1L104.5 81.6L108 82.9L111.5 89.7L114.9 101L118.4 115L121.9 130L125.3 144.2L128.8 156.4L132.3 166.2L135.7 173.4L139.2 178.4L142.7 181.5L146.1 183.3L149.6 184.3L153.1 184.8L156.5 184.9L160 185L163.5 184.9L166.9 184.9L170.4 184.8L173.9 184.8L177.3 184.8L180.8 184.8L184.3 184.8L187.7 184.9L191.2 185L194.7 185.1L198.1 185.2L201.6 185.3L205.1 185.5L208.5 185.7L212 185.8L215.5 186L218.9 186.2L222.4 186.4L225.9 186.5L229.3 186.5L232.8 186.2L236.3 185.3L239.7 183.3L243.2 179.6L246.7 173.6L250.1 165.1L253.6 154.7L257.1 143.9L260.5 134.8L264 129.6L267.5 129.7L270.9 135.2L274.4 144.6L277.9 155.7L281.3 166.4L284.8 175.1L288.3 181.4L291.7 185.4L295.2 187.6L298.7 188.8L302.1 189.4L305.6 189.6L309.1 189.8L312.5 189.8L316 189.8"/><path class="c3 sw2 dash" d="M56 188.9L59.5 188L62.9 186.4L66.4 183.7L69.9 179.6L73.3 173.6L76.8 165.3L80.3 154.7L83.7 142.2L87.2 128.7L90.7 115.2L94.1 103.1L97.6 93.5L101.1 87L104.5 83.1L108 81.2L111.5 80L114.9 79.1L118.4 78.6L121.9 79.7L125.3 83.7L128.8 91.8L132.3 103.9L135.7 118.8L139.2 134.8L142.7 149.9L146.1 162.4L149.6 171.8L153.1 178.2L156.5 182.1L160 184.3L163.5 185.3L166.9 185.8L170.4 186L173.9 186.1L177.3 186.1L180.8 186.1L184.3 186.1L187.7 186.2L191.2 186.2L194.7 186.3L198.1 186.4L201.6 186.5L205.1 186.6L208.5 186.7L212 186.9L215.5 187L218.9 187.2L222.4 187.3L225.9 187.5L229.3 187.6L232.8 187.8L236.3 187.9L239.7 188.1L243.2 188.3L246.7 188.4L250.1 188.5L253.6 188.7L257.1 188.8L260.5 188.9L264 189L267.5 189.1L270.9 189.2L274.4 189.3L277.9 189.4L281.3 189.5L284.8 189.5L288.3 189.6L291.7 189.7L295.2 189.7L298.7 189.7L302.1 189.8L305.6 189.8L309.1 189.8L312.5 189.9L316 189.9"/><path class="c1 sw2" d="M56 397.9L59.5 391.5L62.9 383.3L66.4 373.1L69.9 361.3L73.3 348.7L76.8 336.1L80.3 324.3L83.7 314.3L87.2 306.7L90.7 301.9L94.1 300L97.6 301L101.1 304.6L104.5 310.4L108 317.6L111.5 325.6L114.9 333.9L118.4 342L121.9 349.8L125.3 357.5L128.8 365.2L132.3 372.7L135.7 380L139.2 386.5L142.7 392.1L146.1 396.4L149.6 399.4L153.1 401.4L156.5 402.5L160 403L163.5 403.3L166.9 403.3L170.4 403.3L173.9 403.3L177.3 403.3L180.8 403.3L184.3 403.4L187.7 403.5L191.2 403.6L194.7 403.7L198.1 403.8L201.6 404L205.1 404.2L208.5 404.4L212 404.7L215.5 404.9L218.9 405.1L222.4 405.4L225.9 405.6L229.3 405.8L232.8 405.9L236.3 405.7L239.7 405.1L243.2 403.8L246.7 401.5L250.1 398.1L253.6 393.5L257.1 388.1L260.5 382.2L264 376L267.5 370L270.9 364L274.4 358.5L277.9 354.2L281.3 352.1L284.8 353.3L288.3 358.1L291.7 366.1L295.2 375.8L298.7 385.6L302.1 394.1L305.6 400.5L309.1 404.8L312.5 407.3L316 408.7"/><text class="tl" x="150" y="62">chlorophyll a</text><path class="ln-m thin" d="M146 60L83.7 65.2"/><text class="tl" x="158" y="116">chlorophyll b</text><path class="ln-m thin" d="M266 120L265.7 129"/><text class="tl" x="150" y="152">carotene</text><path class="ln-m thin" d="M148 148L134 111.1"/><text class="tl" x="150" y="358">action</text><text class="tl" x="150" y="372">spectrum</text><path class="ln-m thin" d="M166 376L177.3 403.3"/></svg><figcaption>Schematic spectra (idealised curves, not measured data). The action spectrum follows the combined absorption of all the pigments, with a low point where little light is absorbed.</figcaption></figure>

An **absorption spectrum** tells you what a pigment *can* absorb. An **action spectrum** tells you which wavelengths *actually drive* photosynthesis. Compare them:

- The action spectrum has peaks in the blue-violet (around 430–450 nm) and in the red (around 650–680 nm), and a low point in the green. This matches the **combined absorption spectra** of the pigments.
- That match is the evidence that the pigments we have isolated are the ones that carry out photosynthesis, and that the light they absorb is used.
- The action spectrum is not exactly the same as the absorption spectrum of chlorophyll a alone. Light absorbed by accessory pigments is passed to chlorophyll a in the reaction centre, so photosynthesis also happens at wavelengths that chlorophyll a absorbs poorly.

:::exam Describing a spectrum
"Describe" means quote the wavelength in nm and the value with its unit, and name the highest and lowest points ("the rate is highest at 450 nm, 80 arbitrary units, and lowest at 550 nm, 22 units"). "Explain" means link the peaks to the pigments that absorb at those wavelengths, and say that accessory pigments pass energy to the reaction centre.
:::

:::eg The table shows the percentage of light absorbed by an extract of chlorophyll a, and the rate of photosynthesis of a leaf, in light of different wavelengths. (a) Describe the action spectrum. (b) Explain why the rate at 500 nm is higher than the absorption by chlorophyll a alone would suggest.
The data are invented to practise the skill.

| wavelength / nm | chlorophyll a absorbs / % | rate / arbitrary units |
|---|---|---|
| 400 | 68 | 60 |
| 450 | 80 | 80 |
| 500 | 12 | 40 |
| 550 | 5 | 22 |
| 600 | 20 | 38 |
| 650 | 74 | 68 |
| 700 | 10 | 8 |

(a) Describe, with figures and units.

The rate is highest at 450 nm (blue), 80 arbitrary units, with a second peak at 650 nm (red), 68 arbitrary units. [B1]

The rate is lowest in the green at 550 nm, 22 arbitrary units, and falls to 8 arbitrary units at 700 nm. [B1]

(b) Explain, using the pigments.

At 500 nm chlorophyll a absorbs only 12% of the light, but other pigments (such as carotene and xanthophyll) absorb at this wavelength. [B1]

They pass the energy to chlorophyll a in the reaction centre, so photosynthesis continues at a higher rate than chlorophyll a alone would give. [B1]

A weaker answer says "the leaf is green so it does not absorb green, so the rate is low". It does not quote figures from the table and it never mentions accessory pigments passing energy to the reaction centre.
:::

## Separating the pigments: chromatography and Rf values

How do we know that a leaf contains four pigments? We separate them by **paper chromatography**. The idea is simple. The pigments in a leaf extract differ in how soluble they are in the solvent and in how strongly they stick to the paper. As the solvent soaks up the paper, a pigment that is very soluble and sticks only weakly is carried a long way; one that is less soluble and sticks strongly moves only a little. The pigments end up in separate spots.

:::lab Separating chloroplast pigments by paper chromatography
**Aim**: separate the pigments of a leaf and identify them from their Rf values.

:::steps
1. Grind a few fresh leaves (spinach, for example) with a little sand and a small volume of propanone or ethanol. The sand breaks the cells and the solvent dissolves the pigments.
2. Draw a **pencil** line about 2 cm from the bottom of a strip of chromatography paper. This is the **origin**.
3. With a capillary tube, put a small drop of extract on the middle of the origin, let it dry, and repeat 10 to 15 times on the same spot. This builds a small, dark, concentrated spot.
4. Stand the strip in a boiling tube or jar with about 1 cm of a non-polar solvent (for example a mixture of petroleum ether and propanone). The **solvent level must be below the origin**. Put a lid on.
5. When the solvent front is near the top, take the strip out and **mark the solvent front at once** in pencil, before the solvent evaporates. Dry the strip.
6. Mark the **centre** of each spot in pencil (the colours fade). Measure from the origin to the centre of each spot and from the origin to the solvent front.
:::

<figure class="fig small"><svg viewBox="0 0 360 322" role="img" aria-label="A paper chromatogram of a leaf extract. The origin line is at the bottom and the solvent front at the top. From the top the four spots are carotene, xanthophyll, chlorophyll a and chlorophyll b. Arrow b is the distance moved by the solvent, from the origin to the solvent front. Arrow a is the distance moved by the pigment, from the origin to the centre of the chlorophyll b spot."><rect class="fp ln" x="104" y="24" width="120" height="252"/><path class="ln-m thin dash" d="M104 252L224 252"/><path class="ln-m thin dash" d="M104 44L224 44"/><ellipse class="fa s-acc sw2" cx="164" cy="54.4" rx="20" ry="5"/><ellipse class="fa s-acc sw2" cx="164" cy="104.3" rx="20" ry="5"/><ellipse class="fa s-acc sw2" cx="164" cy="116.8" rx="20" ry="5"/><ellipse class="fa s-acc sw2" cx="164" cy="158.4" rx="20" ry="5"/><text class="tl" x="236" y="66">carotene</text><path class="ln-m thin" d="M232 62L186 54.4"/><text class="tl" x="236" y="84">xanthophyll</text><path class="ln-m thin" d="M232 80L186 104.32"/><text class="tl" x="236" y="118">chlorophyll a</text><path class="ln-m thin" d="M232 114L186 116.8"/><text class="tl" x="236" y="164">chlorophyll b</text><path class="ln-m thin" d="M232 160L186 158.4"/><text class="tl" x="236" y="40">solvent front</text><text class="tl" x="236" y="268">origin (pencil)</text><text class="tl" x="236" y="284">spots start here</text><path class="c1 sw2" d="M90 252L90 46" marker-end="url(#ah)"/><text class="tl tb" x="78" y="150" text-anchor="end">b</text><path class="c2 sw2" d="M124 252L124 158.4" marker-end="url(#ah)"/><path class="ln-m thin dash" d="M124 158.4L140 158.4"/><text class="tl tb" x="132" y="230">a</text><text class="tl" x="164" y="308" text-anchor="middle">solvent level below the origin</text><path class="ln-m thin" d="M104 276L224 276"/></svg><figcaption>A chromatogram (a drawing; real spots are smeared and fade). Rf = a ÷ b, with both distances measured from the origin; here a is for chlorophyll b.</figcaption></figure>

**Variables**: the same paper, solvent, size of spot and running time in each run. **Control**: a spot of a single known pigment run alongside, to show where it travels.

**Typical result**: four spots. From the top: carotene, xanthophyll, chlorophyll a, chlorophyll b.

**Sources of error**: a large or smudged spot makes overlapping bands; the solvent level above the origin washes the extract off; not marking the front at once; measuring to the edge, not the centre, of a spot; pigments breaking down in the light. A sharper separation comes from thin-layer chromatography.

**Safety**: the solvents are flammable and their vapour is harmful. Work in a fume cupboard or a well-ventilated room, keep naked flames away, and wear eye protection.
:::

To identify a pigment you calculate its **Rf value** and compare it with reference values measured in the same solvent.

:::def Rf value
The ratio of the distance moved by a pigment to the distance moved by the solvent front, both measured from the origin.
:::

\[R_f = \frac{\text{distance moved by the pigment}}{\text{distance moved by the solvent front}}\]

- Rf has **no units** (it is a ratio) and is **never greater than 1**, because a pigment cannot move further than the solvent.
- Every pigment has its own Rf in a given solvent. A different solvent or paper gives different values, so a question always gives you the reference values.
- The pigment that is most soluble in the solvent and least attracted to the paper, usually carotene, has the highest Rf.

:::eg A leaf extract was run on a chromatogram. The solvent front moved 8.0 cm from the origin. Four spots had centres 7.6 cm, 5.7 cm, 5.2 cm and 3.6 cm from the origin. The reference Rf values in this solvent are: carotene 0.95, xanthophyll 0.71, chlorophyll a 0.65 and chlorophyll b 0.45. (a) Calculate the Rf of the spot that moved 5.2 cm. (b) Identify the four pigments. (c) Explain why carotene travels furthest.
(a) Divide the distance moved by the pigment by the distance moved by the solvent.

\[\begin{aligned} R_f &= \frac{5.2\,\mathrm{cm}}{8.0\,\mathrm{cm}} \\ &= 0.65 \end{aligned}\]

Rf is the distance ratio. [M1] The value is 0.65. [A1]

(b) The Rf values of the four spots are \(7.6 \div 8.0 = 0.95\), \(5.7 \div 8.0 = 0.71\), \(5.2 \div 8.0 = 0.65\) and \(3.6 \div 8.0 = 0.45\). Matching them with the reference values gives, from the top: carotene, xanthophyll, chlorophyll a and chlorophyll b. [B1]

(c) Carotene is the most soluble in the (non-polar) solvent, so it is carried furthest by it. [B1]

It is also the least strongly attracted to the paper, so it is held back least. [B1]

A weaker answer to (a) divides the other way round (8.0 ÷ 5.2 = 1.5), which gives a value above 1 and scores no marks. A weaker answer to (c) says only "carotene is lighter", which is not creditworthy.
:::

:::exam Rf in the exam
Show the division, give the answer to 2 decimal places and no units, and check it is below 1. If the question says "use the reference values", match each calculated Rf to the nearest reference value and state the pigment's name.
:::

## The light-dependent stage

The light-dependent stage takes place on the thylakoid membranes. Light supplies the energy, and the energy ends up in two products: ATP and reduced NADP. Three ideas come first.

:::def Photoactivation
The absorption of light energy by chlorophyll in a reaction centre, which raises two of its electrons to a higher energy level so that they leave the chlorophyll.
:::

:::def Photolysis of water
The splitting of water by light energy, catalysed by the oxygen-evolving complex of photosystem II, into protons, electrons and oxygen: \(\ce{2H2O -> 4H+ + 4e- + O2}\).
:::

:::def Photophosphorylation
The synthesis of ATP from ADP and \(\mathrm{P_i}\) using energy from light. In chloroplasts the energy is passed to ATP synthase through a proton gradient (chemiosmosis).
:::

Photophosphorylation comes in two kinds. They share one mechanism for making ATP; they differ in which photosystems are used and in what else is made.

### Non-cyclic photophosphorylation

<figure class="fig small"><svg viewBox="0 0 400 462" role="img" aria-label="Non-cyclic photophosphorylation on the thylakoid membrane. Light is absorbed by photosystem II. Water is split in the thylakoid space (photolysis) into protons, electrons and oxygen, and the electrons replace those lost from photosystem II. Energetic electrons pass along the electron transport chain to photosystem I, releasing energy that pumps protons from the stroma into the thylakoid space. Light is also absorbed by photosystem I, and its electrons pass to NADP in the stroma, forming reduced NADP. Protons flow back into the stroma through ATP synthase, which makes ATP from ADP and phosphate."><text class="tl tb" x="10" y="20">thylakoid space</text><text class="tl" x="10" y="36">(high H⁺ concentration)</text><rect class="f2 s-acc2 sw2" x="15" y="190" width="380" height="28"/><rect class="fm s-acc sw2" x="40" y="170" width="56" height="68" rx="6"/><text class="tl tb" x="68" y="209" text-anchor="middle">PSII</text><rect class="fm s-acc sw2" x="272" y="170" width="56" height="68" rx="6"/><text class="tl tb" x="300" y="209" text-anchor="middle">PSI</text><ellipse class="fm s-acc sw2" cx="152" cy="204" rx="17" ry="21"/><ellipse class="fm s-acc sw2" cx="214" cy="204" rx="17" ry="21"/><path class="c4 sw2 dash" d="M98 204L132 204" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M172 204L192 204" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M234 204L268 204" marker-end="url(#ah)"/><text class="tl" x="112" y="181" text-anchor="middle">e⁻</text><text class="tl" x="250" y="181" text-anchor="middle">e⁻</text><path class="c3 sw2" d="M152 180L152 148" marker-end="url(#ah)"/><text class="tl" x="152" y="140" text-anchor="middle">H⁺</text><path class="c3 sw2" d="M214 180L214 148" marker-end="url(#ah)"/><text class="tl" x="214" y="140" text-anchor="middle">H⁺</text><text class="tl" x="10" y="64">light</text><path class="c2 sw2" d="M30 74L50 166" marker-end="url(#ah)"/><text class="tl" x="262" y="80">light</text><path class="c2 sw2" d="M292 90L296 166" marker-end="url(#ah)"/><text class="tl" x="76" y="96">photolysis:</text><text class="tl" x="76" y="112">2H₂O → 4H⁺ + 4e⁻ + O₂</text><path class="ln-m thin" d="M80 118L72 168"/><rect class="fm s-acc sw2" x="352" y="186" width="24" height="34"/><circle class="f1 s-acc sw2" cx="364" cy="240" r="17"/><path class="c3 sw2" d="M364 128L364 182" marker-end="url(#ah)"/><text class="tl" x="302" y="108">H⁺ flow back</text><text class="tl" x="306" y="312">ATP synthase</text><path class="ln-m thin" d="M364 298L364 258"/><text class="tl" x="296" y="328">ADP + Pi → ATP</text><path class="c4 sw2 dash" d="M300 240L300 286" marker-end="url(#ah)"/><text class="tl" x="292" y="264" text-anchor="end">NADP + 2H⁺ + 2e⁻</text><text class="tl" x="292" y="280" text-anchor="end">→ reduced NADP</text><path class="ln-m thin" d="M152 228L152 330"/><text class="tl" x="152" y="346" text-anchor="middle">electron transport chain</text><text class="tl" x="10" y="392">thylakoid membrane</text><path class="ln-m thin" d="M24 380L24 215"/><text class="tl tb" x="10" y="432">stroma</text><text class="tl" x="10" y="448">(low H⁺ concentration)</text></svg><figcaption>Non-cyclic photophosphorylation. Both photosystems absorb light; electrons flow from water through PSII, the chain and PSI to NADP. ATP, reduced NADP and oxygen are the products.</figcaption></figure>

Follow the electrons from water to NADP. The arrows in the figure match the steps.

:::steps
1. **Light is absorbed** by the light-harvesting complex of **photosystem II (PSII)**, and the energy is passed to chlorophyll a in the reaction centre.
2. **Photoactivation**: two electrons are raised to a higher energy level and leave PSII. They are accepted by the first carrier of the **electron transport chain**.
3. **Photolysis**: the oxygen-evolving complex of PSII splits water in the thylakoid space: \(\ce{2H2O -> 4H+ + 4e- + O2}\). The electrons **replace those lost** from PSII. The protons stay in the thylakoid space. Oxygen is a by-product.
4. The energetic electrons pass **along the electron transport chain** from PSII to PSI, releasing energy as they go (details of the carriers are not needed).
5. The released energy is used to **pump protons across the thylakoid membrane** from the **stroma into the thylakoid space**. With the protons from photolysis, this builds a **proton gradient**.
6. **PSI** absorbs light and its electrons are photoactivated and leave. They are replaced by the electrons arriving from the chain.
7. The electrons from PSI pass to **NADP** in the stroma. NADP accepts them with protons from the stroma and becomes **reduced NADP**.
8. Protons flow back from the thylakoid space into the stroma, **down their gradient**, through **ATP synthase** (facilitated diffusion). The energy released makes **ATP** from ADP and \(\mathrm{P_i}\).
:::

So non-cyclic photophosphorylation uses **both PSI and PSII**, and makes **ATP, reduced NADP and oxygen**. The electrons that end up in reduced NADP started in water.

:::key Non-cyclic photophosphorylation: the marking points
1. Light absorbed by PSII; **photoactivation** of chlorophyll, electrons leave.
2. **Photolysis** of water replaces the electrons; protons and oxygen released.
3. Electrons pass along the **electron transport chain** and release energy.
4. Energy used to **pump protons** from the stroma into the thylakoid space (proton gradient).
5. Electrons re-energised in **PSI** and passed to **NADP**, forming **reduced NADP**.
6. Protons flow back through **ATP synthase**, making **ATP**.
:::

### Cyclic photophosphorylation

<figure class="fig small"><svg viewBox="0 0 350 292" role="img" aria-label="Cyclic photophosphorylation. Light is absorbed by photosystem I only. Its electrons pass along the electron transport chain, which pumps protons from the stroma into the thylakoid space, and then return to photosystem I. Protons flow back into the stroma through ATP synthase, which makes ATP. No water is split, no oxygen is released and no reduced NADP is made."><text class="tl tb" x="10" y="20">thylakoid space</text><text class="tl" x="10" y="36">(high H⁺ concentration)</text><rect class="f2 s-acc2 sw2" x="15" y="120" width="330" height="28"/><rect class="fm s-acc sw2" x="36" y="100" width="56" height="68" rx="6"/><text class="tl tb" x="64" y="139" text-anchor="middle">PSI</text><ellipse class="fm s-acc sw2" cx="150" cy="134" rx="17" ry="21"/><ellipse class="fm s-acc sw2" cx="214" cy="134" rx="17" ry="21"/><path class="c4 sw2 dash" d="M94 134L130 134" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M170 134L192 134" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M214 158L214 196L64 196L64 172" marker-end="url(#ah)"/><text class="tl" x="139" y="216" text-anchor="middle">electrons return to PSI</text><text class="tl" x="112" y="111" text-anchor="middle">e⁻</text><path class="c3 sw2" d="M150 110L150 78" marker-end="url(#ah)"/><text class="tl" x="150" y="70" text-anchor="middle">H⁺</text><path class="c3 sw2" d="M214 110L214 78" marker-end="url(#ah)"/><text class="tl" x="214" y="70" text-anchor="middle">H⁺</text><text class="tl" x="10" y="60">light</text><path class="c2 sw2" d="M30 74L48 96" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="290" y="116" width="24" height="34"/><circle class="f1 s-acc sw2" cx="302" cy="170" r="17"/><path class="c3 sw2" d="M302 60L302 112" marker-end="url(#ah)"/><text class="tl" x="250" y="50">H⁺ flow back</text><text class="tl" x="240" y="220">ATP synthase</text><path class="ln-m thin" d="M300 204L302 189"/><text class="tl" x="232" y="236">ADP + Pi → ATP</text><text class="tl tb" x="10" y="262">stroma</text><text class="tl" x="10" y="278">(low H⁺ concentration)</text></svg><figcaption>Cyclic photophosphorylation. The electrons go round a loop and come back to PSI, so the only product is ATP.</figcaption></figure>

Sometimes electrons from PSI do not go to NADP. Instead they are passed back to PSI along the electron transport chain.

- **Only PSI** is involved.
- **Photoactivation** of chlorophyll in PSI raises electrons to a higher energy level; they leave PSI.
- They pass along the electron transport chain, releasing energy that **pumps protons** into the thylakoid space; protons return through **ATP synthase**, so **ATP is made**.
- The electrons **return to PSI**. No electrons are taken from water, so there is **no photolysis, no oxygen and no reduced NADP**. The only product is ATP.

Cyclic photophosphorylation gives the chloroplast extra ATP when it is needed. The Calvin cycle uses more ATP than reduced NADP (3 ATP for every 2 reduced NADP per carbon dioxide fixed, as you will see below).

| | Non-cyclic | Cyclic |
|---|---|---|
| Photosystems | PSII and PSI | PSI only |
| Photoactivation of chlorophyll | yes, in both | yes |
| Photolysis of water | yes | no |
| Source of replacement electrons | water | the electrons come back to PSI |
| Oxygen released | yes | no |
| ATP made | yes | yes |
| Reduced NADP made | yes | no |

:::warn Three mistakes in the light-dependent stage
1. **The oxygen comes from water, not from carbon dioxide.** The oxygen released is made when water is split in photolysis.
2. **Protons are pumped into the thylakoid space, not into the stroma.** They flow back *to* the stroma through ATP synthase. ATP synthase does not pump.
3. **NADP is reduced only in non-cyclic photophosphorylation.** In cyclic photophosphorylation the electrons return to PSI and NADP is not involved.
:::

:::analogy A charging station and a factory
The light-dependent stage is a charging station that uses sunlight to charge two kinds of battery: ATP and reduced NADP. The Calvin cycle is a factory that runs on those batteries. The factory needs no sunlight itself, but when the batteries are flat it stops, and the charging station cannot refill them without light.
:::

:::eg Explain the role of water in the light-dependent stage of photosynthesis.
A model answer, one point per mark.

Water is split by photolysis, catalysed by the oxygen-evolving complex of photosystem II. [B1]

The electrons released replace the electrons lost from chlorophyll in the reaction centre of PSII when it is photoactivated, so electron flow can continue. [B1]

The protons released add to the proton gradient across the thylakoid membrane (they accumulate in the thylakoid space), so more ATP can be made by chemiosmosis. [B1]

Oxygen is released as a by-product (and diffuses out of the chloroplast). [B1]

A weaker answer says "water provides hydrogen and oxygen for photosynthesis". It does not name photolysis, does not say that the electrons replace those lost from PSII, and the protons are not linked to the proton gradient. At most one mark.
:::

:::eg Real context, a herbicide: some weedkillers work by blocking the movement of electrons from photosystem II to the next carrier in the electron transport chain. Explain the effects of such a weedkiller on a leaf in the light.
The question asks for the effect on three products of the light-dependent stage.

Electrons cannot leave PSII, so they are not replaced and photolysis stops: no oxygen is released. [B1]

Electrons from PSII no longer reach PSI, so no electrons are passed to NADP and much less reduced NADP is made. [B1]

Without electron flow along the chain, no protons are pumped into the thylakoid space, so the proton gradient falls and much less ATP is made by non-cyclic photophosphorylation. [B1]

The Calvin cycle runs out of ATP and reduced NADP and stops, so the plant cannot make sugars and dies. [B1]

(Also credit: some ATP can still be made by cyclic photophosphorylation, which uses only PSI.)
:::

:::eg Spot the error: explain how the products of the light-dependent stage are used in the light-independent stage. [3]
A student wrote this answer.

Line 1: Rubisco fixes carbon dioxide by combining it with RuBP, to form two molecules of GP.
Line 2: GP is reduced to triose phosphate using ATP and reduced NADP.
Line 3: RuBP is regenerated from GP using reduced NADP.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: RuBP is regenerated from triose phosphate (TP), not from GP, and the reaction uses ATP, not reduced NADP. That mark is lost [B0].**

Correct Line 3: "RuBP is regenerated from triose phosphate using ATP." With that change the answer scores 3 marks.
:::

## Comparing chemiosmosis in chloroplasts and mitochondria

The same trick is used twice in a plant cell: electrons release energy as they pass along a chain, the energy pumps protons across a membrane, and the protons flow back through ATP synthase. Learn the pairs.

| | Mitochondrion (oxidative phosphorylation) | Chloroplast (photophosphorylation) |
|---|---|---|
| Membrane | inner mitochondrial membrane | thylakoid membrane |
| Source of energy for the electrons | oxidation of respiratory substrates (hydrogen from reduced NAD and reduced FAD) | light, absorbed by chlorophyll |
| Source of the electrons | reduced NAD and reduced FAD | water (non-cyclic) |
| Final electron acceptor | oxygen (forming water) | NADP (non-cyclic), forming reduced NADP |
| Protons pumped | from the matrix into the intermembrane space | from the stroma into the thylakoid space |
| Protons flow back | into the matrix | into the stroma |
| ATP made in | the matrix | the stroma |

In both, the protons return by **facilitated diffusion** through **ATP synthase**, and the membrane must be impermeable to protons elsewhere so that the gradient is kept.

## The light-independent stage: the Calvin cycle

The Calvin cycle takes place in the **stroma**. It uses the ATP and reduced NADP from the light-dependent stage to turn carbon dioxide into carbohydrate. It has three main stages.

:::def Carbon fixation
The combination of carbon dioxide with ribulose bisphosphate (RuBP, a 5C compound), catalysed by the enzyme rubisco, to yield two molecules of glycerate 3-phosphate (GP, a 3C compound).
:::

:::def Rubisco
Ribulose bisphosphate carboxylase-oxygenase, the enzyme that catalyses the fixation of carbon dioxide by RuBP in the Calvin cycle.
:::

<figure class="fig small"><svg viewBox="0 0 360 366" role="img" aria-label="The Calvin cycle with carbon numbers, for three carbon dioxide molecules. Three RuBP (5C) combine with three carbon dioxide molecules, catalysed by rubisco, to give six GP (3C). Six GP are reduced to six TP (3C) using 6 ATP and 6 reduced NADP. One TP leaves the cycle to make carbohydrates, lipids and amino acids. The other five TP are used to regenerate three RuBP, using 3 ATP."><rect class="f1 s-acc sw2" x="160" y="20" width="120" height="40"/><text class="tl" x="220" y="45" text-anchor="middle">3 × RuBP (5C)</text><rect class="f1 s-acc sw2" x="160" y="124" width="120" height="40"/><text class="tl" x="220" y="149" text-anchor="middle">6 × GP (3C)</text><rect class="f1 s-acc sw2" x="160" y="232" width="120" height="40"/><text class="tl" x="220" y="257" text-anchor="middle">6 × TP (3C)</text><path class="c1 sw2" d="M220 60L220 120" marker-end="url(#ah)"/><text class="tl" x="230" y="84">3 CO₂ added by</text><text class="tl" x="230" y="100">rubisco (fixation)</text><path class="c1 sw2" d="M220 164L220 228" marker-end="url(#ah)"/><text class="tl" x="230" y="184">reduction, using</text><text class="tl" x="230" y="200">6 ATP and</text><text class="tl" x="230" y="216">6 reduced NADP</text><path class="c1 sw2" d="M160 252L40 252L40 40L156 40" marker-end="url(#ah)"/><text class="tl" x="48" y="150">5 × TP are used</text><text class="tl" x="48" y="166">to regenerate</text><text class="tl" x="48" y="182">3 × RuBP,</text><text class="tl" x="48" y="198">using 3 ATP</text><path class="c2 sw2" d="M220 272L220 318" marker-end="url(#ah)"/><text class="tl" x="230" y="296">1 × TP leaves</text><text class="tl" x="220" y="336" text-anchor="middle">carbohydrates,</text><text class="tl" x="220" y="352" text-anchor="middle">lipids, amino acids</text></svg><figcaption>The Calvin cycle for 3 CO₂: 15 carbon atoms in RuBP plus 3 in CO₂ make 18 in six GP; five of the six TP (15 carbon atoms) regenerate RuBP and one TP (3 carbon atoms) is the net gain.</figcaption></figure>

:::steps
1. **Fixation**: rubisco joins **carbon dioxide** (1C) to **RuBP** (5C). The unstable 6C product splits at once into **two molecules of GP** (3C). GP is the first product of the cycle.
2. **Reduction**: GP is **reduced to triose phosphate (TP)** (3C). This uses **ATP** (which becomes ADP and \(\mathrm{P_i}\)) and **reduced NADP** (which becomes NADP).
3. **Regeneration**: most of the TP is used to **regenerate RuBP**. This uses **ATP**. One TP in every six is surplus and leaves the cycle.
:::

### Following the carbon

Counting carbon atoms keeps you right. Follow three carbon dioxide molecules through one turn of the cycle in the figure.

- Fixation: 3 RuBP (\(3 \times 5 = 15\) carbon atoms) + 3 \(\ce{CO2}\) (3 carbon atoms) = 18 carbon atoms, in **6 GP** (\(6 \times 3 = 18\)).
- Reduction: 6 GP become **6 TP** (18 carbon atoms), using **6 ATP** and **6 reduced NADP**.
- Regeneration: **5 TP** (15 carbon atoms) are rearranged into **3 RuBP** (15 carbon atoms), using **3 ATP**.
- The remaining **1 TP** (3 carbon atoms) leaves the cycle: this is the net gain from three carbon dioxide molecules.

For every 3 \(\ce{CO2}\) fixed, 9 ATP and 6 reduced NADP are used. So **each carbon dioxide fixed uses 3 ATP and 2 reduced NADP**. To make one 6C sugar, 6 carbon dioxide are fixed, and two TP leave the cycle (\(2 \times 3 = 6\) carbon atoms).

:::eg How many molecules of ATP and of reduced NADP are used in the Calvin cycle to fix enough carbon dioxide to make one molecule of glucose, \(\ce{C6H12O6}\)?
Glucose has 6 carbon atoms, and every carbon atom in it came from one carbon dioxide molecule, so 6 \(\ce{CO2}\) must be fixed.

Each carbon dioxide fixed uses 3 ATP and 2 reduced NADP (9 ATP and 6 reduced NADP for each 3 \(\ce{CO2}\)). [M1]

\[\begin{aligned} \text{ATP} &= 6 \times 3 \\ &= 18 \\ \text{reduced NADP} &= 6 \times 2 \\ &= 12 \end{aligned}\]

18 ATP [A1] and 12 reduced NADP [A1].
:::

### What the products are used for

Triose phosphate and GP are the starting points for the other organic molecules in the plant.

| Product | Used to make |
|---|---|
| **TP** | **carbohydrates**: hexose sugars (glucose), then sucrose for transport in phloem, starch for storage, cellulose for cell walls |
| **TP** | **lipids**: glycerol, and fatty acids built from 2C units |
| **TP** | **amino acids** (with nitrate as a source of nitrogen) |
| **GP** | **some amino acids** (the syllabus limit) |

:::key The Calvin cycle in one box
1. **Fixation**: \(\ce{CO2}\) + **RuBP** (5C) → 2 **GP** (3C), catalysed by **rubisco**.
2. **Reduction**: GP → **TP** (3C), using **ATP** and **reduced NADP**.
3. **Regeneration**: TP → **RuBP**, using **ATP**; one TP in six leaves the cycle.
4. Per \(\ce{CO2}\) fixed: **3 ATP** and **2 reduced NADP**.
5. TP makes carbohydrates, lipids and amino acids; GP makes some amino acids.
:::

:::warn Mistakes in the Calvin cycle
1. **RuBP has 5 carbon atoms**, not 6. GP and TP both have 3.
2. **GP is the first product; TP is made from GP.** RuBP is regenerated from TP, never from GP.
3. **Reduced NADP and ATP are used up in the reduction step**; only ATP is used in regeneration.
:::

### What happens when the light goes out

The Calvin cycle is the factory in the analogy. Take away the power and the cycle's own compounds change in a pattern you must be able to explain.

:::eg A suspension of algae was kept in the light with a supply of carbon dioxide. The light was turned off at 0 s and the concentrations of GP and RuBP in the cells were measured. Describe and explain the changes.
Concentrations are in arbitrary units.

| time after light off / s | GP | RuBP |
|---|---|---|
| 0 | 40 | 20 |
| 15 | 62 | 13 |
| 30 | 77 | 8 |
| 45 | 85 | 5 |
| 60 | 88 | 3 |

Describe first, with figures and units.

The concentration of GP increases from 40 to 88 arbitrary units in 60 s, while the concentration of RuBP decreases from 20 to 3 arbitrary units. [B1]

Then explain.

Without light, the light-dependent stage stops, so no more ATP and reduced NADP are made. [B1]

GP cannot be reduced to TP without ATP and reduced NADP, so GP accumulates; it is still being made because rubisco continues to fix carbon dioxide with the RuBP that is left. [B1]

RuBP cannot be regenerated from TP without ATP, and TP is no longer being made. [B1]

RuBP is still used up in fixation, so its concentration decreases. [B1]

A weaker answer says "the Calvin cycle does not need light so nothing changes". The cycle depends on the light-dependent products, so it does change; this answer scores no marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State where in a chloroplast the light-dependent stage happens and where the Calvin cycle happens.
A: The light-dependent stage: the thylakoid membranes (and thylakoid spaces) of the grana. The Calvin cycle: the stroma.
Q: Name the three products of the light-dependent stage.
A: ATP, reduced NADP and oxygen (a by-product).
Q: State the number of carbon atoms in a molecule of RuBP, of GP and of TP.
A: RuBP 5; GP 3; TP 3.
Q: In a chromatogram, a pigment moved 5.4 cm and the solvent front moved 9.0 cm from the origin. Calculate the Rf value.
A: \(R_f = 5.4 \div 9.0 = 0.60\).
Q: A student calculated an Rf value of 1.2 for one pigment. Explain why this value must be wrong.
A: The pigment cannot move further than the solvent front, so the distance moved by the pigment is never greater than the distance moved by the solvent and Rf is never above 1. The student probably divided the wrong way round (or measured to the wrong place).
Q: Explain why the origin line on a chromatogram is drawn in pencil and not in ink.
A: Ink contains dyes that dissolve in the solvent and would run up the paper with the leaf pigments, making extra spots. The graphite of a pencil is insoluble and stays on the origin.
Q: A chloroplast measures 48 mm on an electron micrograph with a magnification of ×8000. Calculate its actual length in µm.
A: Actual size \(= I \div M = 48 \div 8000 = 0.0060\,\mathrm{mm} = 6.0\,\mu\mathrm{m}\).
Q: State what happens to chlorophyll in a reaction centre during photoactivation.
A: It absorbs light energy, and two of its electrons are raised to a higher energy level and leave the chlorophyll.
Q: Cyclic photophosphorylation makes no reduced NADP. Explain why.
A: The electrons that leave PSI return to PSI along the electron transport chain, so none are passed to NADP. NADP is not reduced.
Q: Calculate the number of ATP and of reduced NADP molecules needed to fix 12 molecules of carbon dioxide.
A: Each \(\ce{CO2}\) needs 3 ATP and 2 reduced NADP, so \(12 \times 3 = 36\) ATP and \(12 \times 2 = 24\) reduced NADP.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ State the part of a chloroplast in which each of the following is found or happens: (a) photoactivation of chlorophyll; (b) the enzyme rubisco; (c) the build-up of protons in a high concentration; (d) the circular DNA.
A: (a) the thylakoid membranes (in the photosystems, in the grana) [B1]
(b) the stroma [B1]
(c) the thylakoid space [B1]
(d) the stroma [B1]
Q: [5 marks] ★★ A mutant of barley lacks chlorophyll b. The table shows the rate of photosynthesis of normal barley and of the mutant in light of different wavelengths. (a) Describe the differences between the two plants. (b) Suggest an explanation for the differences.

| wavelength / nm | normal / arbitrary units | mutant / arbitrary units |
|---|---|---|
| 430 | 80 | 72 |
| 460 | 85 | 58 |
| 500 | 30 | 25 |
| 550 | 20 | 18 |
| 600 | 36 | 32 |
| 640 | 66 | 43 |
| 680 | 90 | 88 |
H: Look for the wavelengths at which the two rates differ most, and the wavelengths at which they are almost the same.
H: Chlorophyll b absorbs best near 460 nm and 640 nm. What is a pigment of this kind called?
A: (a) The mutant has a lower rate at every wavelength, but the difference is greatest at 460 nm (58 compared with 85 arbitrary units) and at 640 nm (43 compared with 66). [B1]
At 680 nm the rates are almost the same (88 compared with 90 arbitrary units). [B1]
(b) Chlorophyll b is an accessory pigment that absorbs light mainly near 460 nm and 640 nm, so the mutant absorbs less light at these wavelengths. [B1]
Less energy is passed to the reaction centres, so less ATP and reduced NADP are made and the rate of photosynthesis is lower. [B1]
Chlorophyll a, the primary pigment, still absorbs at 680 nm (and near 430 nm), so the rate there is almost unchanged. [B1]
Q: [5 marks] ★★ A chromatogram of an extract from yellow autumn leaves, in a different solvent, had two spots. Their centres were 6.6 cm and 3.9 cm from the origin and the solvent front was 7.5 cm from the origin. The reference Rf values in this solvent are carotene 0.88, xanthophyll 0.52, chlorophyll a 0.30 and chlorophyll b 0.18. (a) Calculate the Rf value of each spot and identify the pigments. (b) Suggest why chlorophyll is not found in the extract.
H: Divide each distance by 7.5 cm, then match to the nearest reference value.
A: (a) \(6.6 \div 7.5\) [M1] \(= 0.88\), so carotene [A1]
\(3.9 \div 7.5 = 0.52\), so xanthophyll [A1]
(b) The chlorophyll has broken down (and is not being replaced) in the yellow leaves. [B1]
Carotene and xanthophyll are still present, and without the green chlorophyll their yellow-orange colours show. [B1]
Q: [4 marks] ★★ A plant cell fixes 15 molecules of carbon dioxide. For this, state (a) the number of molecules of GP formed; (b) the number of molecules of ATP used; (c) the number of molecules of reduced NADP used; (d) the number of molecules of triose phosphate that leave the cycle.
H: Fixation of one \(\ce{CO2}\) forms two GP. Use 3 ATP and 2 reduced NADP for each \(\ce{CO2}\).
H: One TP leaves for every 3 \(\ce{CO2}\) fixed.
A: (a) 30 GP (two for each \(\ce{CO2}\)) [B1]
(b) 45 ATP [B1]
(c) 30 reduced NADP [B1]
(d) 5 triose phosphate [B1]
Q: [5 marks] ★★ Compare cyclic and non-cyclic photophosphorylation.
A: Both involve photoactivation of chlorophyll in PSI, and both make ATP by chemiosmosis (protons pumped by the electron transport chain flow back through ATP synthase). [B1]
Non-cyclic uses PSI and PSII, but cyclic uses only PSI. [B1]
Non-cyclic involves photolysis of water, which replaces the lost electrons and releases oxygen; cyclic has no photolysis and no oxygen. [B1]
In non-cyclic the electrons end up in NADP, which is reduced; in cyclic the electrons return to PSI. [B1]
So non-cyclic makes ATP and reduced NADP, but cyclic makes only ATP. [B1]
Q: [5 marks] ★★★ Isolated thylakoids were soaked in a solution at pH 4 in the dark until the inside of each thylakoid was also at pH 4. They were then moved quickly into a solution at pH 8 containing ADP and phosphate, still in the dark. ATP was made. Thylakoids kept at pH 8 all the time made no ATP. (a) Explain why ATP was made in the first experiment. (b) Explain why no ATP was made by thylakoids kept at pH 8. (c) State what the experiment shows about the role of light in the light-dependent stage.
H: A low pH means a high concentration of protons.
H: Think about which side of the membrane has more protons, and which way they can flow.
A: (a) The thylakoid space (pH 4) had a higher concentration of protons than the solution outside (pH 8), so there was a proton gradient across the thylakoid membrane. [B1]
Protons flowed out of the thylakoid space through ATP synthase, down the gradient. [B1]
The energy released was used to make ATP from ADP and phosphate. [B1]
(b) There was no proton gradient, so no net flow of protons through ATP synthase and no energy to make ATP. [B1]
(c) Light is needed only to set up the proton gradient (through the electron transport chain); a proton gradient alone can make ATP. [B1]
Q: [5 marks] ★★★ Compare chemiosmosis in a chloroplast with chemiosmosis in a mitochondrion.
A: Similarity: in both, electrons passing along a chain of carriers release energy, which is used to pump protons across a membrane. [B1]
Similarity: in both, protons flow back through ATP synthase, down their gradient, and the energy released makes ATP. [B1]
Difference: in a chloroplast the membrane is the thylakoid membrane, but in a mitochondrion it is the inner membrane. [B1]
Difference: in a chloroplast the energy to excite the electrons comes from light (photoactivation), but in a mitochondrion it comes from the oxidation of reduced NAD and reduced FAD. [B1]
Difference: in a chloroplast protons are pumped from the stroma into the thylakoid space, but in a mitochondrion from the matrix into the intermembrane space; the final electron acceptor is NADP in the chloroplast and oxygen in the mitochondrion. [B1]
Q: [5 marks] (#bio.respiration) ★★★ A potted plant was kept in the light for 6 hours and then in darkness for 12 hours. (a) Explain why the starch grains in the chloroplasts of its leaves are larger at the end of the light period than at the end of the dark period. (b) In the dark, ATP is still made in the leaf cells. State where and by what process.
H: What does the Calvin cycle make, and what happens to it when the light goes out?
H: For (b), which organelle makes ATP when no light is available?
A: (a) In the light, the Calvin cycle makes triose phosphate using ATP and reduced NADP from the light-dependent stage. [B1]
Triose phosphate is converted to glucose, which is built into starch and stored in the chloroplast. [B1]
In the dark no ATP or reduced NADP is made, so the starch is broken down to sugar (which is used in respiration or transported), and the grains shrink. [B1]
(b) In the mitochondria (and the cytoplasm for glycolysis). [B1]
By aerobic respiration, with oxidative phosphorylation (chemiosmosis) making most of the ATP. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Discs cut from bean leaves were kept in bright light with a high carbon dioxide concentration. The carbon dioxide supply was then stopped, with the light still on. The concentration of RuBP in the leaf cells increased and the concentration of GP decreased. (a) Explain these changes. (b) Predict what would happen to the concentration of reduced NADP in the stroma, and explain your prediction.
H: Which compound needs carbon dioxide to be made, and which compound needs carbon dioxide to be used up?
H: For (b), what happens to the use of reduced NADP when GP is not being made?
A: (a) Without carbon dioxide, rubisco cannot fix it, so RuBP is not used up in fixation and accumulates. [B1]
GP is no longer made from RuBP, and the GP already present is reduced to TP, so the concentration of GP decreases. [B1]
TP continues to regenerate RuBP while ATP is available, which adds to the rise in RuBP. [B1]
(b) The concentration of reduced NADP would increase. [B1]
Less GP is available to be reduced, so less reduced NADP is used (changed back to NADP) in the Calvin cycle, but the light-dependent stage continues to make it. [B1]
Eventually NADP runs short, so the light-dependent stage slows. [B1]
Q: [5 marks] ★★★ Some red algae live in deep sea water, where only blue-green light reaches them. Their action spectrum shows a high rate of photosynthesis at 500 to 560 nm, wavelengths that chlorophyll a absorbs poorly. These algae contain a red pigment, phycoerythrin, that absorbs light of 500 to 560 nm strongly. Suggest an explanation for the action spectrum, and suggest how this pigment is an advantage to the algae.
H: Think about what the accessory pigments in a land plant do with the energy they absorb.
A: Phycoerythrin absorbs light at 500 to 560 nm, so it is an accessory pigment. [B1]
It passes the energy it absorbs to chlorophyll a in the reaction centre. [B1]
So photoactivation happens, and ATP and reduced NADP are made, using light of 500 to 560 nm; this explains the high rate at these wavelengths. [B1]
Deep water absorbs red light, so chlorophyll a alone would catch little of the light that reaches the algae. [B1]
The red pigment lets the algae use the blue-green light that does reach them, so they can photosynthesise at depth. [B1]
:::

:::quiz
? Which statement about the oxygen released in photosynthesis is correct?
+ It comes from water, split by photolysis in the thylakoid space.
- It comes from carbon dioxide, split by rubisco in the stroma.
- It comes from glucose as it is made in the Calvin cycle.
- It comes from reduced NADP as it is oxidised.
> Photolysis of water by the oxygen-evolving complex of PSII releases electrons, protons and oxygen. Rubisco only joins carbon dioxide to RuBP, and the oxygen in carbon dioxide ends up in the sugar and in water.
? Where do protons accumulate in the light-dependent stage?
+ in the thylakoid space
- in the stroma
- in the intermembrane space
- in the cytoplasm
> The electron transport chain pumps protons from the stroma into the thylakoid space, and photolysis adds more there. The intermembrane space is a mitochondrial feature.
? Which row is correct for cyclic photophosphorylation?
+ only PSI is involved; ATP is made; no reduced NADP is made
- only PSII is involved; ATP is made; reduced NADP is made
- PSI and PSII are involved; ATP is made; oxygen is released
- only PSI is involved; no ATP is made; reduced NADP is made
> In the cyclic pathway electrons from PSI return to PSI, so there is no photolysis and no oxygen, NADP is not reduced, and the only product is ATP.
? An action spectrum for a leaf has a low point in the green region. What does this show?
+ little of the green light is absorbed, so little is used for photosynthesis
- green light is absorbed by chlorophyll and wasted as heat
- the leaf is not photosynthesising in green light because it lacks ATP
- green light is reflected by the stroma
> An action spectrum plots the rate of photosynthesis against wavelength. A low rate in the green matches the low absorption of the pigments there; the reflected green light is why leaves look green.
? A pigment moves 2.8 cm while the solvent front moves 7.0 cm. What is its Rf value?
+ 0.40
- 2.5
- 0.40 cm
- 2.8
> Rf = 2.8 ÷ 7.0 = 0.40. Dividing the other way gives 2.5, which is impossible, Rf is a ratio with no units, and 2.8 is only the distance moved by the pigment.
? Which compound is the first product of carbon fixation?
+ glycerate 3-phosphate (GP)
- triose phosphate (TP)
- ribulose bisphosphate (RuBP)
- glucose
> Rubisco joins carbon dioxide to RuBP and the product splits into two GP. GP is then reduced to TP, and RuBP is regenerated from TP.
? How many molecules of triose phosphate leave the Calvin cycle when three carbon dioxide molecules have been fixed?
+ 1
- 3
- 5
- 6
> Six TP are made; five (15 carbon atoms) regenerate three RuBP, leaving one TP (3 carbon atoms), the carbon from the three carbon dioxide molecules.
? What is the role of reduced NADP in photosynthesis?
+ it provides hydrogen (electrons and protons) to reduce GP to triose phosphate
- it provides the energy to fix carbon dioxide onto RuBP
- it carries electrons from water to photosystem II
- it pumps protons into the thylakoid space
> Reduced NADP is made at the end of non-cyclic photophosphorylation and used in the Calvin cycle to reduce GP. Fixation by rubisco needs no ATP or reduced NADP.
? Which statement describes the role of accessory pigments?
+ They absorb light of other wavelengths and pass the energy to chlorophyll a in the reaction centre.
- They absorb light and release electrons to the electron transport chain.
- They absorb green light so that chlorophyll a is not damaged.
- They are the only pigments in the light-harvesting complex.
> Accessory pigments widen the range of wavelengths absorbed. Only chlorophyll a in the reaction centre gives up electrons. The light-harvesting complex also contains chlorophyll a.
? Which of these takes place in the stroma of a chloroplast?
+ reduction of GP to triose phosphate
- photolysis of water
- photoactivation of chlorophyll
- flow of protons through ATP synthase into the thylakoid space
> The Calvin cycle is in the stroma. Photolysis and photoactivation happen on the thylakoid membrane, and protons flow through ATP synthase out of the thylakoid space into the stroma, not into it.
:::

:::checklist What you can now do
- [ ] I can relate the structure of a chloroplast (envelope, grana, thylakoids, stroma, starch grains, circular DNA, 70S ribosomes) to its function, using diagrams and electron micrographs.
- [ ] I can state that the light-dependent stage takes place in the thylakoids (grana) and the light-independent stage in the stroma, and explain how the ATP and reduced NADP made in the first are used in the second.
- [ ] I can describe the roles of chlorophyll a, chlorophyll b, carotene and xanthophyll in light absorption.
- [ ] I can interpret absorption spectra and action spectra.
- [ ] I can describe and use chromatography to separate chloroplast pigments, and calculate and use Rf values.
- [ ] I can explain cyclic photophosphorylation (PSI only, photoactivation, ATP).
- [ ] I can explain non-cyclic photophosphorylation (PSI and PSII, photoactivation, photolysis by the oxygen-evolving complex, ATP and reduced NADP).
- [ ] I can explain how an electron transport chain, a proton gradient and ATP synthase make ATP in the thylakoids.
- [ ] I can outline fixation, reduction and regeneration in the Calvin cycle, with carbon numbers and the roles of rubisco, ATP and reduced NADP.
- [ ] I can state how GP and TP are used to make amino acids, carbohydrates and lipids.
:::

:::recap
- Photosynthesis: \(\ce{6CO2 + 6H2O -> C6H12O6 + 6O2}\) using light. Light-dependent stage in the thylakoids makes ATP, reduced NADP and oxygen; the Calvin cycle in the stroma uses ATP and reduced NADP to make triose phosphate from carbon dioxide.
- Chloroplast: envelope (two membranes); grana (stacked thylakoids) give a large membrane surface for pigments and ATP synthesis; small thylakoid space gives a steep proton gradient; stroma holds Calvin cycle enzymes, starch grains, lipid droplets, circular DNA and 70S ribosomes.
- Chlorophyll a is the primary pigment in the reaction centre; chlorophyll b, carotene and xanthophyll are accessory pigments that widen the range of wavelengths absorbed and pass energy to the reaction centre. Chlorophylls absorb blue-violet and red and reflect green.
- Absorption spectrum: light absorbed at each wavelength. Action spectrum: rate of photosynthesis at each wavelength; it matches the combined absorption of the pigments.
- Chromatography: \(R_f\) = distance moved by pigment ÷ distance moved by solvent front; no units, never above 1; compare with given reference values.
- Non-cyclic: PSII and PSI; photoactivation; photolysis replaces electrons (oxygen released); electron transport chain pumps protons into the thylakoid space; ATP synthase makes ATP; NADP is reduced. Cyclic: PSI only; electrons return to PSI; ATP only.
- Calvin cycle: \(\ce{CO2}\) + RuBP (5C) → 2 GP (3C) by rubisco; GP → TP (ATP, reduced NADP); TP → RuBP (ATP); 3 ATP and 2 reduced NADP per \(\ce{CO2}\). TP makes carbohydrates, lipids and amino acids; GP some amino acids.
- If the light goes out, GP rises and RuBP falls.
:::

:::links
- read: [CAIE A Level Biology: photosynthesis notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/photosynthesis/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Photosynthesis (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/13-photosynthesis/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of photosynthesis
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [Photosynthesis](https://openstax.org/books/biology-2e/pages/8-introduction) · OpenStax Biology 2e · free university textbook chapter on the light and Calvin reactions, beyond the syllabus in places
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find the photosynthesis questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Limiting factors in photosynthesis](#bio.limiting) shows how light, carbon dioxide and temperature control the rate, and how to investigate it.
