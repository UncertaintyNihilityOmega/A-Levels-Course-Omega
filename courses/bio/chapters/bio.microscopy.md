@chapter bio.microscopy
@title Microscopy and magnification
@level as
@paper CAIE 9700 Papers 1, 2 and 3
@time 4–5 hours
@summary Cells are far too small to see without help. You will learn the units of size (mm, µm, nm), how to use a light microscope and make a temporary slide, how to calculate magnification and actual size with M = I/A, how to calibrate an eyepiece graticule with a stage micrometer, and why electron microscopes show more detail than light microscopes (resolution against magnification, TEM against SEM).

:::why
Almost everything you will meet in the next chapters, from cells and organelles to bacteria and viruses, is too small to see with the naked eye. Microscopes made cell biology possible, and hospitals still use them every day, for example to find malaria parasites in a drop of blood. Questions on magnification, actual size and the difference between magnification and resolution come up in the written papers, and the microscope and photomicrograph task in Paper 3 tests the skills in this chapter directly: making a slide, measuring with a graticule and drawing what you see.
:::

**Before you start**, you should know the levels of organisation from molecule to organism and the units mm, µm and nm from [Biology from zero](#bio.f.basics).

:::try Warm-up
Q: Put these in order from smallest to largest: tissue, organelle, organ, cell. (from [Biology from zero](#bio.f.basics))
A: Organelle, cell, tissue, organ.
Q: Convert 0.025 mm to µm. (from [Biology from zero](#bio.f.basics))
A: 1 mm = 1000 µm, so \(0.025 \times 1000 = 25\) µm.
Q: Which is larger, a typical bacterium (1–5 µm) or a typical virus (20–300 nm)? (from [Biology from zero](#bio.f.basics))
A: The bacterium. Even 1 µm is 1000 nm, which is bigger than the largest viruses at 300 nm.
:::

## Units of size

A biologist measures things that range from a whole leaf (centimetres) down to a protein molecule (nanometres). Three units cover almost all of cell biology.

:::def Millimetre, micrometre and nanometre
A millimetre (mm) is one thousandth of a metre. A micrometre (µm) is one thousandth of a millimetre. A nanometre (nm) is one thousandth of a micrometre. So 1 mm = 1000 µm and 1 µm = 1000 nm.
:::

Each unit is 1000 times smaller than the one before it. That makes conversions easy once you remember which way to go.

| To change | Do this | Example |
|---|---|---|
| mm to µm | multiply by 1000 | 0.035 mm = 35 µm |
| µm to nm | multiply by 1000 | 7 µm = 7000 nm |
| nm to µm | divide by 1000 | 450 nm = 0.45 µm |
| µm to mm | divide by 1000 | 6.5 µm = 0.0065 mm |

A quick check: if you go to a **smaller** unit, the number gets **bigger** (there are more of the small unit). If you go to a larger unit, the number gets smaller.

:::eg Convert 0.0065 mm to µm and to nm, and write it in standard form.
**To µm**: going to a smaller unit, so multiply by 1000.

\[\begin{aligned} 0.0065\,\mathrm{mm} &= 0.0065 \times 1000\,\mathrm{\mu m} \\ &= 6.5\,\mathrm{\mu m} \end{aligned}\]

**To nm**: multiply by 1000 again.

\[\begin{aligned} 6.5\,\mathrm{\mu m} &= 6.5 \times 1000\,\mathrm{nm} \\ &= 6500\,\mathrm{nm} \end{aligned}\]

**Standard form** writes a number as something between 1 and 10 times a power of ten: \(0.0065\,\mathrm{mm} = 6.5 \times 10^{-3}\,\mathrm{mm}\) and \(6500\,\mathrm{nm} = 6.5 \times 10^{3}\,\mathrm{nm}\).
:::

Some real sizes help you judge whether an answer is sensible. A red blood cell is about 7 µm across. A typical bacterium is 1–5 µm. Many animal cells are 10–30 µm and many plant cells 10–100 µm. A virus is 20–300 nm. If your calculation says a red blood cell is 7 mm across, you have made a units mistake: 7 mm is big enough to see easily.

:::warn Always write the unit
"The cell is 40" earns nothing. Write the number and the unit (40 µm), and convert **before** you calculate, not after. Most lost marks on magnification questions are unit slips.
:::

## The light microscope

A light microscope uses visible light and glass lenses. Light from a lamp passes up through the specimen, so the specimen must be **thin and transparent enough for light to pass through it**. The objective lens makes a magnified image, and the eyepiece lens magnifies that image again.

:::html
<figure class="fig small"><svg viewBox="0 0 360 312" role="img" aria-label="Side view of a light microscope. From the top: eyepiece lens, body tube, revolving nosepiece with two objective lenses, a stage that holds the slide and coverslip, a condenser lens and iris diaphragm below the stage, and a light source above the base. The arm joins the body tube to the base and carries the coarse focus and fine focus wheels."><path class="f1 s-acc sw2" d="M238 64L288 64L288 282L264 282L264 98L238 98Z"/><rect class="fm s-acc sw2" x="176" y="282" width="130" height="16" rx="4"/><rect class="f1 s-acc sw2" x="218" y="44" width="20" height="86"/><rect class="f2 s-acc2 sw2" x="214" y="22" width="28" height="22"/><rect class="fm s-acc sw2" x="210" y="130" width="36" height="12"/><path class="f2 s-acc2 sw2" d="M214 142L226 142L224 164L216 164Z"/><path class="f2 s-acc2 sw2" d="M230 142L242 142L240 176L232 176Z"/><rect class="fp ln" x="202" y="184" width="56" height="6"/><rect class="fm s-acc sw2" x="184" y="190" width="90" height="8"/><path class="f2 s-acc2 sw2" d="M220 198L236 198L232 212L224 212Z"/><rect class="fm s-acc sw2" x="216" y="216" width="24" height="6"/><circle class="fh s-mute sw2" cx="228" cy="252" r="12"/><circle class="fm s-acc sw2" cx="276" cy="176" r="13"/><circle class="fm s-acc sw2" cx="276" cy="212" r="8"/><text class="tl" x="150" y="36" text-anchor="end">eyepiece lens</text><path class="ln-m thin" d="M154 33L214 33"/><text class="tl" x="150" y="84" text-anchor="end">body tube</text><path class="ln-m thin" d="M154 81L218 81"/><text class="tl" x="150" y="138" text-anchor="end">revolving nosepiece</text><path class="ln-m thin" d="M154 135L210 135"/><text class="tl" x="150" y="160" text-anchor="end">objective lenses</text><path class="ln-m thin" d="M154 157L214 157"/><text class="tl" x="150" y="182" text-anchor="end">slide + coverslip</text><path class="ln-m thin" d="M154 179L202 187"/><text class="tl" x="150" y="210" text-anchor="end">stage</text><path class="ln-m thin" d="M154 207L186 195"/><text class="tl" x="150" y="232" text-anchor="end">condenser + diaphragm</text><path class="ln-m thin" d="M154 229L216 220"/><text class="tl" x="150" y="256" text-anchor="end">light source</text><path class="ln-m thin" d="M154 253L216 253"/><text class="tl" x="150" y="295" text-anchor="end">base</text><path class="ln-m thin" d="M154 292L176 291"/><text class="tl" x="300" y="112">arm</text><path class="ln-m thin" d="M298 109L288 109"/><text class="tl" x="304" y="172">coarse</text><text class="tl" x="304" y="186">focus</text><path class="ln-m thin" d="M300 179L289 179"/><text class="tl" x="304" y="212">fine</text><text class="tl" x="304" y="226">focus</text><path class="ln-m thin" d="M300 215L284 215"/></svg><figcaption>A light microscope. Light from the source passes up through the condenser and the thin specimen, then through an objective lens and the eyepiece lens to your eye.</figcaption></figure>
:::

| Part | What it does |
|---|---|
| eyepiece lens | the lens you look through; magnifies the image from the objective (×10 in the kit used for Paper 3) |
| objective lenses | on the revolving nosepiece; the one in use makes the first magnified image (×10 and ×40) |
| stage | the flat platform that holds the slide; clips keep the slide still |
| condenser lens | focuses light from the lamp onto the specimen |
| iris diaphragm | opens and closes to control how much light reaches the specimen |
| light source | a lamp (or a mirror reflecting daylight) under the stage |
| coarse and fine focus | move the stage or the lenses up and down to bring the image into focus; fine focus makes small adjustments |

### Total magnification

The image you see has been magnified twice, so the two magnifications multiply.

:::key Total magnification
Total magnification = magnification of the eyepiece lens × magnification of the objective lens.

With a ×10 eyepiece: the ×10 objective gives ×100 and the ×40 objective gives ×400.
:::

Notice that you **multiply**, not add: \(10 \times 40 = 400\), not 50.

### Using the microscope

:::steps
1. Start with the **lowest-power** objective (×10) clicked into place, and switch on the light.
2. Put the slide on the stage under the clips, with the specimen over the hole in the stage.
3. Looking from the side, use the coarse focus to bring the objective close to the slide without touching it.
4. Look through the eyepiece and use the coarse focus to move the lens **away** from the slide until the specimen is nearly in focus. Then use the fine focus to sharpen it.
5. Adjust the iris diaphragm to give clear contrast: a stained specimen usually needs more light, an unstained one often needs less.
6. Move the slide so that the part you want to see is in the **centre** of the field of view. Only then turn the nosepiece to the ×40 objective and focus with the **fine focus only**.
:::

Why start at low power? The ×10 objective shows a larger area, so the specimen is easier to find. The ×40 objective sits much closer to the slide, so the coarse focus could crush the slide or scratch the lens. Focusing by moving the lens **away** from the slide, never towards it while looking through the eyepiece, avoids this.

Magnifying more shows less. Moving from ×100 to ×400 is four times the magnification, so the **diameter** of the area you can see (the field of view) becomes four times smaller. That is why you centre the part you want before you change objective: at ×400 it could be outside the field of view.

### What a light microscope can and cannot do

- **Advantages**: it is cheap and easy to use, the specimen can be **alive** (a drop of pond water, for example), and stains can show colour.
- **Limitations**: the specimen must be thin, and the **resolution** is poor: about 200 nm (0.2 µm). Structures smaller than that, such as ribosomes or the membranes inside a cell, cannot be seen as separate details. You will see why in the section on resolution.

## Making a temporary slide

A **temporary** preparation is a slide made quickly, with the specimen in liquid under a coverslip, which you can look at straight away. It is not preserved: it dries out and the cells decay within hours. (A *permanent* slide is a preserved specimen in a mounting medium, prepared in advance.)

Most cells are transparent, so under the microscope they show little contrast. A **stain** is a coloured chemical that binds to certain structures and makes them stand out. Iodine solution stains the nucleus (and starch grains) brown or blue-black; methylene blue stains the nucleus and cytoplasm blue.

:::html
<figure class="fig small"><svg viewBox="0 0 340 204" role="img" aria-label="Side view of lowering a coverslip. A drop of water or stain with the specimen lies on a slide. One edge of the coverslip rests on the slide beside the drop, and the other edge is held up by a mounted needle and lowered slowly."><rect class="fp ln" x="30" y="140" width="270" height="10"/><ellipse class="f2 s-acc2 sw2" cx="112" cy="135" rx="32" ry="6"/><path class="f1 s-acc sw2" d="M80 138L212.442 67.5793L213.851 70.2281L81.4084 140.649Z"/><path class="ln thick" d="M270 24L216.442 73.5793"/><path class="ln" d="M296 50L296 84" marker-end="url(#ah)"/><text class="tl" x="250" y="112">lower slowly</text><text class="tl" x="250" y="172">slide</text><path class="ln-m thin" d="M252 169L240 151"/><text class="tl" x="14" y="190">specimen in a drop of water or stain</text><path class="ln-m thin" d="M66 180L96 142"/><text class="tl" x="14" y="60">coverslip</text><path class="ln-m thin" d="M60 64L137.599 103.311"/><text class="tl" x="232" y="28" text-anchor="end">mounted needle</text><path class="ln-m thin" d="M236 26L258 34"/></svg><figcaption>Lower the coverslip at an angle. The liquid spreads along the edge and pushes the air out in front of it, so no bubbles are trapped under the glass.</figcaption></figure>
:::

:::lab Making a temporary slide of plant or animal cells
**Aim**: prepare a thin, stained, bubble-free slide of onion epidermis or cheek cells, and view it with the light microscope.

:::steps
1. Put one drop of water (or of stain) in the middle of a clean slide with a pipette.
2. **Onion epidermis**: use forceps to peel a piece of the thin, transparent skin from the inner surface of a fleshy onion leaf. Lay it flat in the drop, with no folds. **Cheek cells**: gently scrape the inside of your own cheek with a clean cotton bud and smear it on the slide in a drop of methylene blue.
3. Add a drop of stain beside the onion tissue (iodine solution), or leave the methylene blue in place.
4. Hold a coverslip at an angle of about 45° with one edge touching the edge of the liquid. Support the other edge with a mounted needle and **lower it slowly**.
5. If there is too much liquid, soak up the excess at the edge with filter paper. Do not press on the coverslip.
6. View with the ×10 objective first, then the ×40 objective, as described above.
:::

**Why each step matters**:
- A **thin layer**, one cell thick, lets light pass through and stops cells overlapping, so single cells and their parts can be seen.
- The liquid keeps the cells **alive and moist**, and the stain makes parts such as the nucleus visible.
- The **coverslip** flattens the specimen so more of it is in focus, protects the objective lens from the liquid and slows drying.
- Lowering the coverslip at an angle pushes air out in front of the liquid. **Air bubbles** look like dark rings with bright centres and can be mistaken for cells.

**Control**: a drop of water instead of stain, on a second slide, shows what the cells look like unstained.

**Sources of error**: a thick or folded piece of tissue gives a blurred, overlapping image; bubbles; too much stain hides detail; the specimen drying out.

**Safety**: iodine solution and methylene blue stain skin and clothes and can irritate the eyes, so wear eye protection and a lab coat. Use a mounted needle, forceps and coverslips carefully (glass can cut). For cheek cells use only your own cells, put the used cotton bud, slide and coverslip into disinfectant and wash your hands. Never touch another person's cells. Risk: low.
:::

You can also make a temporary slide of a **plant section**. Cut a very thin slice from a stem or root with a sharp razor blade or scalpel, always cutting away from your fingers, put the slice in a drop of water on the slide and add the coverslip. Thin slices float in the drop and keep from drying out. The thinnest slice gives the clearest image, so choose it with forceps.

## Magnification and resolution

These two words are used all the time in microscopy, and they mean different things.

:::def Magnification
How many times larger the image is than the actual object.
:::

:::def Resolution
The ability to distinguish two points that are close together as separate points.
:::

Magnification makes the image bigger. Resolution decides how much **detail** the image can show. A microscope with poor resolution can magnify an image a great deal, but all you get is a bigger blur.

:::analogy Enlarging a blurry photograph
Take a photograph that is slightly out of focus and enlarge it on a photocopier. The picture is much bigger, but no new detail appears: the blur is just bigger too. High magnification without good resolution is "empty magnification". A better camera lens (better resolution) shows detail that no amount of enlarging can add.
:::

:::warn Magnification does not improve resolution
Never write that increasing magnification increases resolution. Resolution depends on the type of radiation (the wavelength of light or electrons) and the quality of the lenses. If two points are too close to be resolved, magnifying more only makes one bigger blob.
:::

### The magnification equation

To find a magnification or an actual size, measure the **image** with a ruler and compare it with the **actual** size.

:::formula Magnification
\[M = \frac{I}{A}\]
\(M\) = magnification (a number, written ×500, with no units); \(I\) = size of the image (drawing or micrograph); \(A\) = actual size of the specimen. \(I\) and \(A\) must be in the **same unit** before you divide.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 200 142" role="img" aria-label="The magnification triangle. I is at the top; A and M sit side by side below it, separated by a vertical line. Cover the quantity you want: covering I leaves A times M, covering A leaves I over M, covering M leaves I over A."><path class="f1 s-acc sw2" d="M100 10L190 130L10 130Z"/><path class="ln" d="M55 70L145 70"/><path class="ln" d="M100 70L100 130"/><text class="tl tb" x="100" y="56" text-anchor="middle">I</text><text class="tl tb" x="66" y="112" text-anchor="middle">A</text><text class="tl tb" x="134" y="112" text-anchor="middle">M</text></svg><figcaption>The magnification triangle: I = image size, A = actual size, M = magnification. Cover the one you want to find.</figcaption></figure>
:::

The triangle gives all three forms of the equation. Cover the quantity you want to find:

\[\begin{aligned} M &= \frac{I}{A} \\ A &= \frac{I}{M} \\ I &= M \times A \end{aligned}\]

:::key Steps for any magnification calculation
1. **Measure** the image with a ruler, in mm, along its longest dimension (or read the scale bar).
2. **Convert** so that image and actual size use the same unit. Most often convert to µm (mm × 1000).
3. **Substitute** into the correct form of \(M = I/A\) and calculate.
4. **Check** the size is sensible, give the unit for a length (µm, not "×") and write a magnification as ×, with no unit.
:::

:::eg A mitochondrion in an electron micrograph with magnification ×30 000 is 42 mm long on the printed page. Calculate its actual length in µm.
We want the actual size, so use \(A = I/M\). The image is in mm, so the answer will first be in mm.

\[\begin{aligned} A &= \frac{I}{M} \\ &= \frac{42\,\mathrm{mm}}{30\,000} \\ &= 0.0014\,\mathrm{mm} \end{aligned}\]

Now convert to µm by multiplying by 1000:

\[0.0014\,\mathrm{mm} \times 1000 = 1.4\,\mathrm{\mu m}\]

The mitochondrion is 1.4 µm long. This is a sensible size: it is bigger than the 0.2 µm limit of a light microscope, but smaller than a typical animal cell.
:::

:::eg Calculate the magnification of a drawing. A cell is 45 µm long. A student's drawing of it is 90 mm long.
The image (the drawing) is in mm and the actual size is in µm, so convert first. \(90\,\mathrm{mm} = 90 \times 1000 = 90\,000\,\mathrm{\mu m}\).

\[\begin{aligned} M &= \frac{I}{A} \\ &= \frac{90\,000\,\mathrm{\mu m}}{45\,\mathrm{\mu m}} \\ &= 2000 \end{aligned}\]

The drawing has a magnification of ×2000. Write "× 2000" (no unit): the units cancel.
:::

Try the calculator below. Choose which quantity to find, enter the other two with their units, and watch the working. Then check that you can do the same on paper.

:::html
<div class="widget" data-w="bio-magnify" data-mode="mia"></div>
:::

### Scale bars

Many micrographs have a **scale bar**: a short line labelled with the length it represents, such as 2 µm. You do not need to be told the magnification. Use the bar to **find** it.

:::html
<figure class="fig small"><svg viewBox="0 0 340 222" role="img" aria-label="Drawing of an electron micrograph of one mitochondrion, with a scale bar at the bottom left labelled 0.5 micrometres. The mitochondrion is about three times as long as the scale bar."><rect class="fm s-acc sw2" x="10" y="10" width="320" height="200" rx="4"/><ellipse class="f2 s-acc2 sw2" cx="190" cy="84" rx="60" ry="28"/><ellipse class="fp ln" cx="190" cy="84" rx="53" ry="21"/><path class="ln" d="M148 105L148 74"/><path class="ln" d="M162 63L162 94"/><path class="ln" d="M176 105L176 74"/><path class="ln" d="M190 63L190 94"/><path class="ln" d="M204 105L204 74"/><path class="ln" d="M218 63L218 94"/><path class="ln" d="M232 105L232 74"/><path class="ln thick" d="M30 176L70 176"/><path class="ln" d="M30 170L30 182"/><path class="ln" d="M70 170L70 182"/><text class="tl" x="50" y="198" text-anchor="middle">0.5 µm</text><text class="tl" x="210" y="146">mitochondrion</text><path class="ln-m thin" d="M216 135L200 112"/><text class="tl" x="110" y="40" text-anchor="end">membranes</text><path class="ln-m thin" d="M114 41L176 58"/><text class="tl" x="150" y="166">scale bar</text><path class="ln-m thin" d="M146 163L74 174"/></svg><figcaption>A drawing of an electron micrograph with its scale bar. The mitochondrion is 3 bar lengths long, so it is 3 × 0.5 µm = 1.5 µm long. In a real micrograph you would measure both lengths with a ruler.</figcaption></figure>
:::

There are two equivalent methods:
- **Ratio method**: measure the bar and the object with a ruler. Actual size = (length of object ÷ length of bar) × value on the bar. In the figure the mitochondrion is 3 bars long, so it is \(3 \times 0.5 = 1.5\,\mathrm{\mu m}\) long. This works on any printout or screen, because both lengths are enlarged equally.
- **Magnification method**: measure the bar, convert it to the same unit as its label and divide to get \(M\); then use \(A = I/M\) for each structure.

:::eg The scale bar on an electron micrograph is 25 mm long and is labelled 2 µm. A nucleus in the same micrograph is 68 mm across. Find the magnification and the actual diameter of the nucleus.
**Magnification**: the bar is the image of a 2 µm length. Convert the bar to µm (\(25 \times 1000 = 25\,000\,\mathrm{\mu m}\)).

\[\begin{aligned} M &= \frac{I}{A} \\ &= \frac{25\,000\,\mathrm{\mu m}}{2\,\mathrm{\mu m}} \\ &= 12\,500 \end{aligned}\]

The magnification is ×12 500.

**Actual diameter of the nucleus**:

\[\begin{aligned} A &= \frac{I}{M} \\ &= \frac{68\,000\,\mathrm{\mu m}}{12\,500} \\ &= 5.44\,\mathrm{\mu m} \end{aligned}\]

To 2 significant figures (the same as the data, 68 mm), the diameter is 5.4 µm. The ratio method gives the same answer without finding \(M\): \(68 \div 25 \times 2 = 5.44\,\mathrm{\mu m}\).
:::

:::exam Showing your working
Calculation marks are usually a method mark for a correct rearrangement or conversion and an answer mark. Write the equation, the numbers with their units, and the answer. Give the answer to the same number of significant figures as the data in the question (or one more), and show the unrounded value before you round. If the question says "give your answer in µm", the last line must be in µm.
:::

:::eg Spot the error: a drawing of a cell is 36 mm long. The cell is 12 µm long. Calculate the magnification of the drawing. [3]
A student wrote this answer. The mark scheme gives M1 for the correct equation, B1 for converting both lengths to the same unit and A1 for the answer ×3000.

Line 1: Magnification = image size ÷ actual size.
Line 2: Magnification = 36 mm ÷ 12 µm = 3.
Line 3: The magnification is ×3.

Line 1 is correct [M1]. **Line 2 divides a length in mm by a length in µm without converting. The two lengths are not in the same unit, so the number 3 is meaningless. The conversion mark is lost [B0] and the answer mark is lost [A0].** A drawing 3 times bigger than a cell would be 36 µm long, not 36 mm.

Correct Line 2: \(36\,\mathrm{mm} = 36\,000\,\mathrm{\mu m}\), so \(M = 36\,000 \div 12 = 3000\). With that change the answer scores 3 marks.
:::

:::eg Real context, diagnosing malaria: a technician photographs a stained thin blood smear through a light microscope. The photograph has a magnification of ×1000. A red blood cell measures 7.0 mm across, and the malaria parasite inside it measures 2.5 mm. Find the actual size of the parasite. Then explain why light microscopy, not electron microscopy, is used for routine diagnosis.
**Actual size of the parasite**: \(A = I/M\).

\[\begin{aligned} A &= \frac{2.5\,\mathrm{mm}}{1000} \\ &= 0.0025\,\mathrm{mm} \\ &= 2.5\,\mathrm{\mu m} \end{aligned}\]

As a check, the red blood cell is \(7.0 \div 1000 = 0.0070\,\mathrm{mm} = 7.0\,\mathrm{\mu m}\), the size expected for a red blood cell. The parasite is 2.5 µm, so it is well above the 0.2 µm resolution limit of a light microscope and can be seen.

**Why light microscopy**: a blood smear takes minutes to prepare and stain, and the microscope is cheap, small and needs no vacuum, so even a clinic with few resources can use it. The stain makes the parasite stand out in colour inside the red cells, and it can be seen well enough to identify. An electron microscope would need thin sections, a vacuum, expensive equipment and trained staff, and the extra detail is not needed to spot the parasite.
:::

## Measuring cells: eyepiece graticule and stage micrometer

A ruler cannot measure something 40 µm long. A microscope measures it with two small scales used together.

:::def Eyepiece graticule
A small transparent scale placed inside the eyepiece, so it is seen in focus on top of the specimen. Its divisions are in arbitrary "eyepiece units" with no fixed length.
:::

:::def Stage micrometer
A slide with a very accurate scale etched on it, usually 1 mm divided into 100 divisions, so each division is 0.01 mm = 10 µm. It is placed on the stage and used to find the real length of one eyepiece unit.
:::

The size of one eyepiece unit depends on the objective lens, because a stronger objective magnifies the specimen (and the stage micrometer) more, but not the graticule, which stays the same size in the eyepiece. So you must **calibrate** the graticule for each objective lens.

:::html
<figure class="fig small"><svg viewBox="0 0 340 172" role="img" aria-label="Eyepiece graticule laid over a stage micrometer. The zero marks of both scales line up at the left. The graticule has 30 units drawn; the stage micrometer has divisions numbered 0 to 7, each 10 micrometres. At the right, the 25 mark of the graticule lines up with the 6 mark of the stage micrometer."><text class="tl tb" x="20" y="14">eyepiece graticule: 30 units</text><path class="ln" d="M20 56L320 56"/><path class="ln" d="M20 56L20 46M30 56L30 51M40 56L40 51M50 56L50 51M60 56L60 51M70 56L70 46M80 56L80 51M90 56L90 51M100 56L100 51M110 56L110 51M120 56L120 46M130 56L130 51M140 56L140 51M150 56L150 51M160 56L160 51M170 56L170 46M180 56L180 51M190 56L190 51M200 56L200 51M210 56L210 51M220 56L220 46M230 56L230 51M240 56L240 51M250 56L250 51M260 56L260 51M270 56L270 46M280 56L280 51M290 56L290 51M300 56L300 51M310 56L310 51M320 56L320 46"/><text class="ts" x="20" y="34" text-anchor="middle">0</text><text class="ts" x="70" y="34" text-anchor="middle">5</text><text class="ts" x="120" y="34" text-anchor="middle">10</text><text class="ts" x="170" y="34" text-anchor="middle">15</text><text class="ts" x="220" y="34" text-anchor="middle">20</text><text class="ts" x="270" y="34" text-anchor="middle">25</text><text class="ts" x="320" y="34" text-anchor="middle">30</text><path class="ln" d="M20 108L315.7 108"/><path class="ln" d="M20 108L20 122M61.7 108L61.7 122M103.3 108L103.3 122M145 108L145 122M186.7 108L186.7 122M228.3 108L228.3 122M270 108L270 122M311.7 108L311.7 122"/><text class="ts" x="20" y="138" text-anchor="middle">0</text><text class="ts" x="61.7" y="138" text-anchor="middle">1</text><text class="ts" x="103.3" y="138" text-anchor="middle">2</text><text class="ts" x="145" y="138" text-anchor="middle">3</text><text class="ts" x="186.7" y="138" text-anchor="middle">4</text><text class="ts" x="228.3" y="138" text-anchor="middle">5</text><text class="ts" x="270" y="138" text-anchor="middle">6</text><text class="ts" x="311.7" y="138" text-anchor="middle">7</text><path class="ln-m thin dash" d="M20 56L20 108"/><path class="ln-m thin dash" d="M270 56L270 108"/><text class="tl" x="262" y="86" text-anchor="end">25 units = 6 divisions</text><text class="tl tb" x="20" y="160">stage micrometer: 1 division = 10 µm</text></svg><figcaption>Calibrating an eyepiece graticule at one objective: line up the zeros, then find a mark on the graticule that lines up exactly with a mark on the stage micrometer. Here 25 eyepiece units match 6 divisions of 10 µm.</figcaption></figure>
:::

:::key Calibrating the graticule (one objective at a time)
1. Put the stage micrometer on the stage and focus on its scale with the chosen objective.
2. Turn the eyepiece (and move the slide) until the **zero marks** of the two scales line up.
3. Look along the scales for another place where a mark on the graticule lines up exactly with a mark on the stage micrometer. Read how many eyepiece units match how many stage divisions.
4. Length of the stage divisions \(= \text{divisions} \times 10\,\mathrm{\mu m}\).
5. \(\text{length of one eyepiece unit} = \dfrac{\text{length of the stage divisions}}{\text{number of eyepiece units}}\).
6. Take the stage micrometer away, put the specimen on, and measure it in eyepiece units. Actual length = units × length of one eyepiece unit.
:::

:::eg At ×40, 25 eyepiece units line up with 6 stage micrometer divisions (as in the figure). Each division is 10 µm. Calibrate the graticule, then find the length of a cell that measures 18 eyepiece units at ×40.
**Step 1: the stage divisions.** \(6 \times 10 = 60\,\mathrm{\mu m}\), and this length is 25 eyepiece units.

**Step 2: the calibration.**

\[\begin{aligned} 1\ \text{eyepiece unit} &= \frac{60\,\mathrm{\mu m}}{25} \\ &= 2.4\,\mathrm{\mu m} \end{aligned}\]

**Step 3: the cell.**

\[\begin{aligned} \text{length} &= 18 \times 2.4\,\mathrm{\mu m} \\ &= 43.2\,\mathrm{\mu m} \end{aligned}\]

To 2 significant figures (the same as 18 units), the cell is 43 µm long.

**Why recalibrate?** On the same microscope, the ×10 objective magnifies four times less than the ×40 objective, so the same cell would span \(18 \div 4 = 4.5\) eyepiece units, and one unit would be \(4 \times 2.4 = 9.6\,\mathrm{\mu m}\). The answer, \(4.5 \times 9.6 = 43.2\,\mathrm{\mu m}\), is the same. Using the ×40 value (2.4 µm per unit) at ×10 would give \(4.5 \times 2.4 = 10.8\,\mathrm{\mu m}\), a wrong answer.
:::

Use the graticule tool below to calibrate a graticule at the two objectives. Drag the stage scale (or use the slider) until the zeros line up, read off the matching marks and compute the length of one eyepiece unit, then use the unit to measure a cell.

:::html
<div class="widget" data-w="bio-magnify" data-mode="graticule"></div>
:::

:::lab Calibrating an eyepiece graticule and measuring cells
**Aim**: find the actual length of cells using an eyepiece graticule calibrated with a stage micrometer.

:::steps
1. Fit the eyepiece graticule. Calibrate it with the ×10 objective as in the key box: line up the zeros, find a matching pair of marks and calculate the length of one eyepiece unit.
2. Repeat the calibration with the ×40 objective (do not assume the value from ×10).
3. Remove the stage micrometer and put on a slide of cells.
4. At ×40, measure the length of one cell in eyepiece units, along its longest axis. Measure at least ten different cells chosen without looking at their size.
5. Convert each length to µm, and calculate the mean.
:::

**Variables**: the objective lens is the independent variable for the calibration (the length of one unit changes with it); the length of the cell is what is measured. Use the same cells, the same eyepiece and the same graticule throughout.

**Typical results**: cells of the same tissue vary in length. The mean of many cells gives a reliable value; one cell may be much larger or smaller than usual.

**Sources of error**: the graticule marks are thick, so reading where a mark lines up is uncertain by about half a unit; the cell edge is blurred; calibrating once and using the value at another objective; the stage micrometer not lined up exactly. Improvements: calibrate over as long a stretch of the scale as possible (25 units rather than 5) so that a small reading error is a smaller fraction of the length; measure more cells.

**Safety**: take care with glass slides and keep the microscope cable away from water. Risk: low.
:::

Measuring over a **long** stretch makes the calibration more accurate. If a reading is uncertain by half a unit, that is 10% of 5 units but only 2% of 25 units.

## Electron microscopes and resolution

Why is the resolution of a light microscope about 200 nm? Light behaves as a wave, and two points that are closer together than about half the wavelength of the light cannot be seen as separate. Visible light has wavelengths of about 400 to 700 nm, so structures closer than about 200 nm blur into one.

:::key Why electron microscopes resolve more
Electrons behave as waves with a much **shorter wavelength** than light. A microscope that uses a beam of electrons can therefore distinguish points that are much closer together: its **resolution** is higher. In practice a transmission electron microscope (TEM) can resolve points about 0.5 nm apart, compared with about 200 nm for a light microscope.
:::

The electrons are focused by electromagnets (which work as lenses). Air would scatter the electrons, so the inside of an electron microscope is a **vacuum**. This means the specimen must be **dead**, and it has to be specially prepared (fixed, dehydrated and stained with heavy metals).

:::def Transmission electron microscope (TEM)
A microscope in which a beam of electrons passes through a very thin section of specimen. Dense parts absorb more electrons and appear darker. It produces a flat (two-dimensional) image of the inside of cells at very high resolution.
:::

:::def Scanning electron microscope (SEM)
A microscope in which a beam of electrons is scanned across the surface of a specimen, and electrons coming from the surface are collected to build up a three-dimensional-looking image of the surface. Its resolution is lower than that of a TEM but much better than a light microscope.
:::

| Feature | Light microscope | TEM | SEM |
|---|---|---|---|
| radiation | visible light | electron beam | electron beam |
| resolution | about 200 nm | about 0.5 nm | between the two |
| specimen | thin, transparent; can be alive | very thin section; dead, in a vacuum | whole or thick surface; dead, in a vacuum |
| image | colour (if stained) | black and white, 2D | black and white, 3D appearance of the surface |
| shows | cells and large organelles | internal detail: organelles, membranes | surface shape of cells and tissues |
| cost and size | cheap, small, portable | very expensive, large, trained user | very expensive, large, trained user |

**Choosing the right microscope** depends on what you need to see:
- To watch **living** cells, to see colour, or to check a stained tissue quickly and cheaply, use a **light microscope**.
- To see the **inside** of a cell in great detail (membranes, organelles, the nuclear envelope), use a **TEM**.
- To see the **surface** of a whole specimen, such as a pollen grain, an insect's eye or the cilia on a cell, in three dimensions, use an **SEM**.

Electron micrographs are black and white (shades of grey), because electrons have no colour. Some are shown in **false colour**, added by computer, to make different structures easier to tell apart: the colours are not the true colours of the specimen.

Specimens for the electron microscope are fixed, dried, stained or coated and placed in a vacuum. These steps can damage the cell, leaving **artefacts**: structures that look real in the image but were not in the living cell, such as shrunken cells or gaps. So an electron micrograph is an image of the *prepared* specimen.

:::eg Compare the images produced by a transmission electron microscope with those produced by a light microscope.
This is a 4-mark question. A full-mark answer gives four separate points, each a comparison:

The TEM image has a much higher resolution, so it shows more detail (such as membranes and small organelles) that a light microscope cannot resolve. [B1]

The TEM can give a much higher useful magnification. [B1]

The TEM image is black and white (or false colour), whereas a light microscope image can show the true colours of a stained specimen. [B1]

The TEM needs a very thin section of dead specimen in a vacuum, so living cells can be seen only with a light microscope. [B1]

(Also credit: the TEM image is two-dimensional, showing a slice through the cell; the specimen preparation for TEM can produce artefacts; TEM equipment is much more expensive and larger.)

A weaker answer says "TEM is better because it is more powerful and magnifies more". It never uses the word **resolution**, gives no feature of the image or the specimen, and scores at most one mark.
:::

:::eg Two small structures are 0.15 µm apart. A student says they can be seen as two separate objects in a light microscope if the magnification is high enough. Evaluate the statement.
Convert so the units match: \(0.15\,\mathrm{\mu m} = 0.15 \times 1000 = 150\,\mathrm{nm}\).

The resolution of a light microscope is about 200 nm. The structures are only 150 nm apart, which is **less than** 200 nm, so a light microscope cannot resolve them. They look like one blurred structure, however much the image is magnified.

A TEM has a resolution of about 0.5 nm, and 150 nm is much greater than 0.5 nm. A TEM would show two separate structures.

The student is wrong: increasing magnification does not improve resolution.
:::

## Drawing cells from slides and micrographs

Drawing forces you to look closely, and drawings are marked in Paper 3. Here are the basic rules; the full method, with examples and marking, is in [Practical skills: microscopy and drawing (Paper 3)](#bio.practical2).

- Use a sharp pencil. Draw **clear, single, unbroken lines**. No shading and no colouring.
- Draw what you see, not what you expect. Keep the **proportions** correct.
- Make the drawing large (fill at least half the space given).
- Label with **ruled lines** that touch the structure and do not cross each other. Write labels horizontally, away from the drawing.
- Give the drawing a title and state the magnification, or add a scale bar.

To state the magnification of your drawing, measure it and use the actual size you worked out with the graticule: \(M = I/A\).

## Practice

:::try Start easy, finish at exam standard
Q: Convert 0.35 mm to µm and 850 nm to µm.
A: \(0.35 \times 1000 = 350\) µm; \(850 \div 1000 = 0.85\) µm.
Q: A microscope has a ×10 eyepiece and a ×40 objective. State the total magnification.
A: \(10 \times 40 = \times 400\).
Q: A cell is 60 µm long. A drawing of it is 12 cm long. Calculate the magnification of the drawing.
A: \(12\,\mathrm{cm} = 120\,\mathrm{mm} = 120\,000\,\mathrm{\mu m}\). \(M = 120\,000 \div 60 = \times 2000\).
Q: A photomicrograph has a magnification of ×600. A cell in it is 27 mm across. Calculate the actual diameter of the cell in µm.
A: \(A = I/M = 27 \div 600 = 0.045\,\mathrm{mm} = 45\,\mathrm{\mu m}\).
Q: A vesicle is 6.0 mm across in an electron micrograph of magnification ×20 000. Calculate its actual diameter in nm.
A: \(6.0 \div 20\,000 = 0.0003\,\mathrm{mm} = 0.3\,\mathrm{\mu m} = 300\,\mathrm{nm}\).
Q: A cell has an actual length of 80 µm. It is viewed at a total magnification of ×150. Calculate the length of the image in mm.
A: \(I = M \times A = 150 \times 80 = 12\,000\,\mathrm{\mu m} = 12\,\mathrm{mm}\).
Q: On a micrograph, a scale bar is 18 mm long and is labelled 10 µm. A cell is 45 mm long. Calculate the actual length of the cell.
A: \(45 \div 18 \times 10 = 25\,\mathrm{\mu m}\).
Q: State why a coverslip is used on a temporary slide, and why it is lowered at an angle.
A: The coverslip flattens the specimen, protects the objective lens and slows drying. It is lowered at an angle, from one side, so that air is pushed out and no air bubbles are trapped (bubbles can be mistaken for cells).
Q: Define resolution, and explain why electrons give better resolution than light.
A: Resolution is the ability to distinguish two points that are close together as separate points. Electrons have a much shorter wavelength than light, so points that are much closer together can be seen as separate.
Q: Give two differences between an image from a scanning electron microscope and an image from a transmission electron microscope.
A: An SEM image shows the surface of a specimen and looks three-dimensional; a TEM image shows the inside of a thin section and is two-dimensional. The SEM has lower resolution than the TEM.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ The image of a pollen grain on a photomicrograph is 54 mm across. The actual diameter of the pollen grain is 30 µm. Calculate the magnification of the photomicrograph.
A: Convert: \(54\,\mathrm{mm} = 54\,000\,\mathrm{\mu m}\), then \(M = 54\,000 \div 30\) [M1] \(= \times 1800\) [A1]
Q: [4 marks] ★★ A student makes a temporary slide of a thin slice of plant stem to view with a light microscope. (a) Explain why the slice must be as thin as possible. (b) Describe how the coverslip should be put on, and explain why. (c) Suggest why the student looks at the slide first with the ×10 objective.
H: For (a), think about what has to pass through the specimen.
H: For (c), think about how much of the slide you see and about the position of the ×40 objective.
A: (a) Light must pass through the specimen, so it must be thin; a thick slice blocks light or has overlapping layers of cells, which cannot be seen as separate. [B1]
(b) Lower the coverslip slowly at an angle, using a mounted needle, starting at one edge of the liquid. [B1]
This pushes the air out so no air bubbles are trapped (bubbles could be mistaken for cells). [B1]
(c) The ×10 objective shows a larger area (a wider field of view), so the specimen is easier to find and centre. [B1]
(Also credit: ×10 is further from the slide, so there is less risk of damaging the slide or the lens.)
Q: [5 marks] ★★ A student calibrated an eyepiece graticule with a stage micrometer, in which one division is 10 µm. The table shows what she found. (a) Calculate the length of one eyepiece unit at each objective. (b) At ×40 a cell measured 14 eyepiece units. Calculate its length. (c) Explain why the student must calibrate the graticule for each objective.

| objective | eyepiece units | stage divisions |
|---|---|---|
| ×10 | 40 | 20 |
| ×40 | 40 | 5 |

H: Length of the matching stage scale = divisions × 10 µm. Divide it by the number of eyepiece units.
H: For (c), what changes when the objective changes: the graticule or the image of the specimen?
A: (a) At ×10: \(20 \times 10 = 200\,\mathrm{\mu m}\), \(200 \div 40\) [M1] \(= 5.0\,\mathrm{\mu m}\) per unit [A1]
At ×40: \(5 \times 10 = 50\,\mathrm{\mu m}\), \(50 \div 40 = 1.25\,\mathrm{\mu m}\) per unit [A1]
(b) \(14 \times 1.25 = 17.5\,\mathrm{\mu m}\) [A1]
(c) A stronger objective magnifies the specimen more, but the graticule stays the same size in the eyepiece, so one unit represents a different (smaller) real length at each objective. [B1]
Q: [4 marks] ★★ Two ribosomes on a membrane are 0.08 µm apart. (a) Explain whether a light microscope with a resolution of 200 nm can show them as two separate structures. (b) State what type of microscope could show them as separate, and why.
H: Put both values in nm first.
A: (a) \(0.08\,\mathrm{\mu m} = 80\,\mathrm{nm}\) [B1]
This is less than 200 nm, the resolution of the light microscope, so they would appear as a single structure (or not be seen at all). [B1]
(b) An electron microscope (TEM) [B1] because the electron beam has a much shorter wavelength than light, so it has a higher resolution (about 0.5 nm). [B1]
Q: [6 marks] ★★★ Cheek cells were measured at ×10. The graticule was calibrated: 20 eyepiece units matched 15 stage micrometer divisions of 10 µm. The widths of eight cells were 7, 8, 9, 8, 7, 9, 8 and 8 eyepiece units. (a) Calculate the length of one eyepiece unit at ×10. (b) Calculate the mean width of the cells, in µm. (c) Describe the variation in cell width. (d) Suggest how the student could make the mean more reliable.
H: Mean in units first (add, divide by 8), then multiply by the length of one unit.
A: (a) \(15 \times 10 = 150\,\mathrm{\mu m}\), then \(150 \div 20\) [M1] \(= 7.5\,\mathrm{\mu m}\) per unit [A1]
(b) Mean \(= 64 \div 8\) [M1] \(= 8.0\) units, and \(8.0 \times 7.5 = 60\,\mathrm{\mu m}\) [A1]
(c) The widths range from 7 to 9 units, which is 52.5 µm to 67.5 µm; most are 8 units (60 µm). [B1]
(d) Measure many more cells, chosen at random from different parts of the slide. [B1]
(Also credit: measure at ×40 for a smaller percentage error; repeat the calibration.)
Q: [5 marks] ★★★ An electron micrograph shows a yeast cell. The scale bar is 30 mm long and labelled 2 µm. The cell is 105 mm across. (a) Calculate the magnification. (b) Calculate the actual diameter of the yeast cell. (c) State the type of electron microscope that produced an image of the inside of a thin slice of the cell, and give one reason.
H: Convert the bar to µm before dividing by 2 µm.
A: (a) \(30\,\mathrm{mm} = 30\,000\,\mathrm{\mu m}\), \(M = 30\,000 \div 2\) [M1] \(= \times 15\,000\) [A1]
(b) \(A = 105\,000\,\mathrm{\mu m} \div 15\,000 = 7.0\,\mathrm{\mu m}\) [A1]
(c) Transmission electron microscope [B1] because the electron beam passes through a thin section and shows the inside of the cell. [B1]
Q: [7 marks] (#bio.cells) ★★★ A student drew a cell from a slide viewed at ×400. The drawing is 72 mm long. A stage micrometer showed that, at ×400, one eyepiece unit is 2.5 µm, and the cell measured 16 eyepiece units. (a) Calculate the actual length of the cell. (b) Calculate the magnification of the drawing. (c) The student wants to show a structure inside the cell that is 0.1 µm wide. Explain why this is impossible with a light microscope. (d) Suggest why this does not mean that the structure is not there.
H: (b) Convert the drawing length to µm before dividing.
A: (a) \(16 \times 2.5\) [M1] \(= 40\,\mathrm{\mu m}\) [A1]
(b) \(72\,\mathrm{mm} = 72\,000\,\mathrm{\mu m}\), \(M = 72\,000 \div 40\) [M1] \(= \times 1800\) [A1]
(c) 0.1 µm is 100 nm, which is less than the resolution of a light microscope (200 nm). [B1]
Points closer than 200 nm cannot be seen as separate, so the structure is too small to be seen in detail. [B1]
(d) It is below the resolution of the microscope, so it cannot be seen with a light microscope; an electron microscope could show it. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A photomicrograph was printed with the label "×400". The picture was then enlarged on a photocopier to 120% of its original size. (a) Calculate the true magnification of the photocopy. (b) A student measured a cell as 30 mm long on the photocopy and used ×400 to find its actual length. Calculate the percentage error in her answer. (c) A scale bar on the same photocopy would still give the correct actual size. Explain why.
H: A 120% enlargement multiplies every length by 1.2.
H: Work out the true actual length first, then the length she calculated.
A: (a) \(400 \times 1.2\) [M1] \(= \times 480\) [A1]
(b) True actual length \(= 30\,\mathrm{mm} \div 480 = 0.0625\,\mathrm{mm} = 62.5\,\mathrm{\mu m}\); student's value \(= 30 \div 400 = 0.075\,\mathrm{mm} = 75\,\mathrm{\mu m}\). [M1]
Error \(= (75 - 62.5) \div 62.5 \times 100 = 20\%\) too large. [A1]
(c) The scale bar is enlarged by the same factor as the picture, so the ratio of the bar to the cell does not change. [B1]
(Also credit: the labelled magnification is only correct for the original size.)
Q: [5 marks] ★★★ At a total magnification of ×100, the field of view of a microscope is 1.8 mm across. (a) Calculate the field of view at ×400. (b) How many cells of length 60 µm laid end to end would just cross the field of view at ×400? (c) A student looking at ×400 cannot find the cells she saw at ×100. Explain why, and suggest what she should have done.
H: Four times the magnification shows a field four times narrower.
A: (a) \(1.8 \div 4\) [M1] \(= 0.45\,\mathrm{mm}\) [A1]
(b) \(0.45\,\mathrm{mm} = 450\,\mathrm{\mu m}\), and \(450 \div 60 = 7.5\) cells [A1]
(c) The field of view at ×400 is only a quarter of the width, so the cells were outside it. [B1]
She should have moved the cells to the centre of the field at ×100 before changing objective. [B1]
:::

:::quiz
? A student's microscope has a ×10 eyepiece and a ×40 objective. What is the total magnification?
+ ×400
- ×50
- ×4
- ×40
> Total magnification is eyepiece × objective: \(10 \times 40 = 400\). ×50 comes from adding; ×40 forgets the eyepiece.
? Which statement about resolution is correct?
+ It is the ability to distinguish two close points as separate points.
- It is how many times larger the image is than the object.
- It increases whenever the magnification is increased.
- It is the same for all microscopes.
> Resolution is about detail, not size. More magnification does not improve it, and electron microscopes have much better resolution than light microscopes.
? A drawing is 40 mm long and the cell is 20 µm long. What is the magnification?
+ ×2000
- ×2
- ×0.5
- ×800
> Convert first: \(40\,\mathrm{mm} = 40\,000\,\mathrm{\mu m}\), and \(40\,000 \div 20 = 2000\). ×2 divides without converting, ×0.5 turns the fraction upside down, and ×800 multiplies instead of dividing.
? Why can an electron microscope show more detail than a light microscope?
+ Electrons have a much shorter wavelength than light.
- Electrons make the image bigger than light does.
- Electron microscopes are used on living specimens.
- Electron microscopes have a brighter lamp.
> A shorter wavelength allows points that are closer together to be resolved. Electron microscopes need a vacuum, so the specimens are dead.
? 40 eyepiece units match 12 stage divisions of 10 µm. How long is one eyepiece unit?
+ 3.0 µm
- 0.33 µm
- 4.0 µm
- 120 µm
> \(12 \times 10 = 120\,\mathrm{\mu m}\), then \(120 \div 40 = 3.0\,\mathrm{\mu m}\). 0.33 turns the division upside down, 4.0 divides 40 by 10, and 120 µm is the whole stretch, not one unit.
? A student calibrates an eyepiece graticule with the ×10 objective and then measures cells with the ×40 objective, using the same value. What is the effect on the answers?
+ The cell lengths are wrong, because the calibration changes with the objective.
- There is no effect, because the graticule is fixed in the eyepiece.
- The lengths are right but the magnification is wrong.
- The lengths are right but less precise.
> One eyepiece unit covers a different real length at each objective, so every measurement is wrong by the ratio of the magnifications (a factor of 4 here).
? Which image shows the three-dimensional surface of a specimen?
+ a scanning electron micrograph
- a transmission electron micrograph
- a light micrograph of a stained section
- a drawing of a stage micrometer
> The SEM scans the surface and gives a three-dimensional appearance. The TEM shows a flat slice through the specimen.
? A student converts 0.0048 mm to micrometres. Which answer is correct?
+ 4.8 µm
- 0.0000048 µm
- 48 µm
- 4800 µm
> Going to a smaller unit, multiply by 1000: \(0.0048 \times 1000 = 4.8\). The other options use ÷1000, a wrong power, or ×1 000 000.
? Why is a coverslip lowered onto the slide at an angle?
+ So that air is pushed out and no air bubbles are trapped under it.
- So that the stain is spread over the objective lens.
- So that the specimen is sterilised.
- So that the specimen stays alive for longer.
> A bubble looks like a cell or a ring and spoils the image. The coverslip does not sterilise anything.
:::

:::checklist What you can now do
- [ ] I can make a temporary slide of cellular material (onion epidermis or cheek cells, stained, with a coverslip lowered at an angle) and say why each step is needed.
- [ ] I can use a light microscope, work out the total magnification, and say how to find and focus a specimen safely.
- [ ] I can follow the rules for drawing cells from slides and photomicrographs.
- [ ] I can calculate magnification, actual size and image size from \(M = I/A\), from drawings, photomicrographs, electron micrographs and scale bars, with consistent units.
- [ ] I can calibrate an eyepiece graticule with a stage micrometer at each objective and use it to measure cells in mm, µm and nm.
- [ ] I can define magnification and resolution, explain the difference, and explain why electron microscopes have better resolution than light microscopes.
- [ ] I can compare light microscopes, TEM and SEM (specimen, image, resolution, advantages and limits).
:::

:::recap
- 1 mm = 1000 µm and 1 µm = 1000 nm. Going to a smaller unit, multiply by 1000.
- Total magnification = eyepiece × objective (×10 eyepiece with ×10 or ×40 objective gives ×100 or ×400).
- Temporary slide: thin specimen, drop of liquid or stain, coverslip lowered at an angle to avoid air bubbles; start with the low-power objective.
- Magnification = how many times larger the image is than the actual object. Resolution = the ability to distinguish two close points as separate. More magnification does not give more resolution.
- \(M = I/A\), with \(I\) and \(A\) in the same unit; M is written as ×, with no unit. Scale bar: measure the bar, work out \(M\) (or compare lengths).
- Graticule: line up zeros, find a matching pair of marks, unit length = (divisions × 10 µm) ÷ units. Recalibrate for every objective.
- Light microscope resolution about 200 nm (0.2 µm); TEM about 0.5 nm, because electrons have a shorter wavelength.
- TEM: thin section, 2D internal detail. SEM: surface, 3D appearance. Both: black and white (false colour can be added), vacuum, dead specimens, possible artefacts.
:::

:::links
- read: [CAIE A Level Biology: cell structure notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/cell-structure/) · Physics & Maths Tutor · free revision notes and questions sorted by topic
- practise: [Cell structure (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/1-cell-structure/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of microscopes and cells
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- explore: [Learn.Genetics: the cell](https://learn.genetics.utah.edu/content/cells/) · University of Utah · interactive tours of cell size and structure
- papers: [Paper 3 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-3/) · Physics & Maths Tutor · find the microscope and photomicrograph questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Eukaryotic cells and organelles](#bio.cells) uses these skills to identify organelles in electron micrographs.
