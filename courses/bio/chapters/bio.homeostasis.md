@chapter bio.homeostasis
@title Homeostasis and the kidney
@level a2
@paper CAIE 9700 Paper 4
@time 5–6 hours
@summary Homeostasis keeps the conditions inside the body steady. You will learn the control loop and negative feedback, how urea is made in the liver, the structure of the kidney and nephron, how urine is formed by ultrafiltration and selective reabsorption, and how ADH and the collecting ducts control the water potential of the blood.

:::why
Your cells work only in a narrow range of temperature, pH, water potential and glucose concentration, yet you eat, sweat, exercise and sleep in a world that keeps changing. Homeostasis is how the body copes, and the kidney is its best-known organ: it removes urea and decides every day how much water you keep. Paper 4 asks you to name the parts of a nephron, explain how a filter and a set of pumps make urine, and describe how a hormone adjusts the water balance, so this chapter builds each step with the words the mark scheme uses.
:::

**Before you start**, you should know osmosis, water potential and active transport from [Movement across membranes](#bio.movement), how a capillary forms tissue fluid from [Transport in mammals](#bio.mammaltransport), and how enzymes are denatured from [Enzymes](#bio.enzymes).

:::try Warm-up
Q: Define osmosis in terms of water potential. (from [Movement across membranes](#bio.movement))
A: The net movement of water molecules from a region of higher water potential to a region of lower water potential, through a partially permeable membrane.
Q: Why does active transport need ATP, and what does the carrier protein do with it? (from [Movement across membranes](#bio.movement))
A: It moves a substance against its concentration gradient, which needs energy. ATP is hydrolysed and the energy changes the shape of the carrier protein so that the substance is moved across.
Q: At the arterial end of a capillary, which force pushes fluid out through the gaps in the wall? (from [Transport in mammals](#bio.mammaltransport))
A: The hydrostatic pressure of the blood.
:::

## Homeostasis and why it matters

:::def Homeostasis
The maintenance of a constant internal environment, within narrow limits, in spite of changes in the external environment and in the body itself.
:::

The "internal environment" is the blood and the tissue fluid that bathes every cell. Homeostasis keeps four things in the blood and tissue fluid steady, and each one matters for a reason you have already met.

- **Temperature.** Enzymes work fastest at their optimum temperature. If the body is too cold, enzyme-controlled reactions are too slow; if it is too hot, hydrogen bonds and ionic bonds break and enzymes are denatured (see [Enzymes](#bio.enzymes)).
- **Water potential.** If the water potential of the tissue fluid falls, water leaves cells by osmosis and they shrink; if it rises, water enters cells and animal cells may burst. Either way the cell cannot work properly.
- **Blood glucose concentration.** Cells need a steady supply of glucose for respiration. Too little starves cells, especially brain cells; too much lowers the water potential of the blood and tissue fluid.
- **pH.** The charges on R groups, and so the shape of enzymes, depend on the concentration of hydrogen ions.

:::key Why homeostasis matters
Constant conditions mean that **enzymes** keep their shape and work at a steady rate, cells keep their **volume** because the water potential outside them is steady, and cells have a constant **supply of glucose** to respire. Without it, the body could work only when the weather suited it.
:::

### The control loop and negative feedback

Every homeostatic system uses the same loop of parts.

:::def Stimulus, receptor, coordinator, effector
A **stimulus** is a change in the internal or external environment. A **receptor** detects the stimulus. A **coordination system** (the nervous system or the endocrine system) carries information from the receptor to the **effector**, which is a muscle or a gland that carries out the **response**.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 366" role="img" aria-label="A control loop with five boxes joined by downward arrows: stimulus (a factor rises or falls), receptor (detects the change), coordination system (nervous or endocrine), effector (a muscle or a gland) and response (reverses the change). An arrow from the response goes back up to the stimulus and is labelled negative feedback."><rect class="f1 s-acc sw2" x="50" y="10" width="190" height="44"/><text class="tl tb" x="145" y="30" text-anchor="middle">stimulus</text><text class="tl" x="145" y="46" text-anchor="middle">a factor rises or falls</text><path class="c1 sw2" d="M145 54L145 82" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="50" y="82" width="190" height="44"/><text class="tl tb" x="145" y="102" text-anchor="middle">receptor</text><text class="tl" x="145" y="118" text-anchor="middle">detects the change</text><path class="c1 sw2" d="M145 126L145 154" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="50" y="154" width="190" height="44"/><text class="tl tb" x="145" y="174" text-anchor="middle">coordination system</text><text class="tl" x="145" y="190" text-anchor="middle">nervous or endocrine</text><path class="c1 sw2" d="M145 198L145 226" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="50" y="226" width="190" height="44"/><text class="tl tb" x="145" y="246" text-anchor="middle">effector</text><text class="tl" x="145" y="262" text-anchor="middle">a muscle or a gland</text><path class="c1 sw2" d="M145 270L145 298" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="50" y="298" width="190" height="44"/><text class="tl tb" x="145" y="318" text-anchor="middle">response</text><text class="tl" x="145" y="334" text-anchor="middle">reverses the change</text><path class="c2 sw2" d="M240 320L318 320L318 32L244 32" marker-end="url(#ah)"/><text class="tl tb" x="252" y="168">negative</text><text class="tl tb" x="252" y="184">feedback</text></svg><figcaption>The control loop of homeostasis. The response reverses the change that started the loop, so the factor returns to its set point: negative feedback.</figcaption></figure>
:::

:::def Negative feedback
A control mechanism in which a change in a factor is detected by receptors and corrected by effectors, so that the factor returns to its normal level, or set point. The response reverses the change that triggered it.
:::

Think of a thermostat on an oven. If the oven gets too hot, the sensor switches the heater off; when it cools too far, the sensor switches the heater on. The temperature never stays exactly on the set point. It swings a little above and a little below, because the response takes time to work.

:::plot A factor under negative feedback. The curve is the value of the factor over time; the dashed line is the set point. Each rise is corrected by a response that brings the value down, and each fall is corrected by a response that brings it up.
--f "37+0.8*sin(1.7*x)" --x 0 12 --y 35.5 38.5 --hline 37 --noticks --xlabel "time" --ylabel "value of the factor" --label "factor under control" --legend tr --alt "A wave that rises above and falls below a dashed horizontal line, the set point. It never moves far from the line, because every rise is reversed by a response and every fall is reversed by the opposite response."
:::

The small swings are not a failure. Negative feedback keeps the factor **within narrow limits** because any change in one direction is turned back. Two receptors or two effectors that work in opposite directions, such as sweating and shivering, give finer control than one that can only switch on and off.

:::warn "Negative" does not mean "bad"
In negative feedback the **response is the opposite of the change**. A rise causes a fall, and a fall causes a rise. That is why it keeps conditions steady. (In positive feedback a change causes more of the same change, which is why it is rare in homeostasis.)
:::

### Temperature as a worked illustration

Body temperature shows the whole loop. The hypothalamus, a part of the brain, is the coordinator. It contains receptors that detect the temperature of the blood passing through it, and it also receives impulses from temperature receptors in the skin.

| Change | Response of effectors | How it restores the temperature |
|---|---|---|
| core temperature rises | sweat glands secrete sweat | water evaporates from the skin and takes heat energy with it |
| core temperature rises | arterioles in the skin dilate (vasodilation) | more blood flows near the surface, so more heat is lost by radiation |
| core temperature falls | skeletal muscles contract and relax rapidly (shivering) | respiration in the muscles releases heat |
| core temperature falls | arterioles in the skin constrict (vasoconstriction) | less blood flows near the surface, so less heat is lost |

:::eg Explain how negative feedback keeps the temperature of the body steady when a person exercises in a warm room.
Exercise makes the muscles release more heat, so the core temperature rises above the set point. Build the answer along the loop.

Temperature receptors in the hypothalamus detect the rise in the temperature of the blood (and receptors in the skin detect the warm surroundings). [B1]

The hypothalamus (the coordinator) sends nerve impulses to the effectors. [B1]

The sweat glands secrete more sweat, and as the water evaporates from the skin it takes heat energy from the body. [B1]

Arterioles in the skin dilate, so more blood flows near the surface and more heat is lost by radiation. [B1]

The temperature falls back towards the set point, so the receptors are stimulated less and the responses reduce: this is negative feedback. [B1]

A weaker answer says "the body sweats to cool down" and never names a receptor, the hypothalamus or the return to the set point. It describes a response, not a feedback loop, and scores one mark.
:::

## Excretion and urea

:::def Excretion
The removal from the body of the waste products of metabolism, and of substances in excess of the body's needs.
:::

Cells produce several waste products. Carbon dioxide is removed by the lungs (see [Gas exchange](#bio.gasexchange)). Nitrogen waste is a different problem. The body cannot store amino acids, so amino acids that are not needed for making proteins are broken down in the **liver**.

:::def Deamination
The removal of the amino group (–NH₂) from an amino acid, forming ammonia and a keto acid (an organic acid with no nitrogen). It happens in the liver.
:::

The keto acid is used in respiration to release energy, or is converted to glycogen or fat. The **ammonia** is toxic, even at low concentration, so the liver cells at once combine it with carbon dioxide to make **urea**. Overall:

\[\ce{2NH3 + CO2 -> CO(NH2)2 + H2O}\]

(The reactions are in a series called the urea cycle; you do not need their names.) Urea is far less toxic than ammonia and is very soluble. It is released from the liver into the blood plasma, carried to the kidneys and removed in urine.

:::key From amino acid to urine
1. Excess amino acids go to the **liver**.
2. **Deamination** removes the amino group as ammonia, leaving a keto acid.
3. Ammonia and carbon dioxide are converted to **urea** in the liver.
4. Urea travels in the **blood plasma** to the **kidney**, where it is filtered out and excreted in **urine**.
:::

:::warn Urea is made in the liver, removed by the kidney
A common mistake is "urea is made in the kidney". The kidney only **removes** urea (and adjusts water and ions). Also write "excess amino acids", not "excess protein": it is the amino acids that are deaminated.
:::

## The structure of the kidney

You have two kidneys, each about the size of a fist, one on each side of the back of the abdomen. Each is supplied with blood by a **renal artery**, which branches from the aorta, and drained by a **renal vein**. A tube called the **ureter** carries urine from each kidney to the bladder.

:::html
<figure class="fig small"><svg viewBox="0 0 400 352" role="img" aria-label="A kidney cut lengthways. The tough fibrous capsule surrounds the outer layer, the cortex. Inside it are the darker medulla, shown as three pyramid shapes pointing towards the renal pelvis, a funnel-shaped space in the middle where urine collects. The ureter leaves the pelvis and runs downwards. The renal artery enters at the middle of the inner edge and divides into branches; the renal vein leaves from the same place."><path class="f1 ln sw3" d="M262 172L261.5 186.1L260 200.1L257.5 213.7L254 226.9L249.7 239.5L244.4 251.4L238.4 262.3L231.6 272.3L224.1 281.2L216 288.9L207.4 295.3L198.4 300.4L189.1 304L179.6 306.3L170.1 307L160.6 306.3L151.3 304L142.4 300.4L134.2 295.3L126.9 288.9L121 281.2L116.8 272.3L114.7 262.3L114.7 251.4L116.7 239.5L120.3 226.9L124.7 213.7L128.9 200.1L131.9 186.1L133 172L131.9 157.9L128.9 143.9L124.7 130.3L120.3 117.1L116.7 104.5L114.7 92.6L114.7 81.7L116.8 71.7L121 62.8L126.9 55.1L134.2 48.7L142.4 43.6L151.3 40L160.6 37.7L170.1 37L179.6 37.7L189.1 40L198.4 43.6L207.4 48.7L216 55.1L224.1 62.8L231.6 71.7L238.4 81.7L244.4 92.6L249.7 104.5L254 117.1L257.5 130.3L260 143.9L261.5 157.9Z"/><path class="f2 s-acc2 sw2" d="M168.2 149L200.1 85.4L220 108.2Z"/><path class="f2 s-acc2 sw2" d="M175.9 172L235 153.5L235 190.5Z"/><path class="f2 s-acc2 sw2" d="M168.2 195L220 235.8L200.1 258.6Z"/><path class="fp ln" d="M168 172L167.8 175.4L167.3 178.7L166.5 181.9L165.3 185L163.9 187.8L162.1 190.4L160.2 192.6L158 194.5L155.7 196L153.2 197.1L150.6 197.8L148 198L145.4 197.8L142.8 197.1L140.3 196L138 194.5L135.8 192.6L133.9 190.4L132.1 187.8L130.7 185L129.5 181.9L128.7 178.7L128.2 175.4L128 172L128.2 168.6L128.7 165.3L129.5 162.1L130.7 159L132.1 156.2L133.9 153.6L135.8 151.4L138 149.5L140.3 148L142.8 146.9L145.4 146.2L148 146L150.6 146.2L153.2 146.9L155.7 148L158 149.5L160.2 151.4L162.1 153.6L163.9 156.2L165.3 159L166.5 162.1L167.3 165.3L167.8 168.6Z"/><path class="fp ln" d="M144.1 181.4L139.8 183.2L135.2 185.5L131 188.4L126.8 191.8L123 195.8L119.2 200.3L115.8 205.4L112.5 211.1L109.4 217.5L106.5 224.5L103.9 232.2L101.6 240.8L99.4 250.1L97.5 260.1L95.7 271.1L94.3 283L93.1 295.7L92.1 309.4L91.4 324.1L91 339.9L101 340.1L101.4 324.5L102.1 310L103.1 296.5L104.3 284L105.7 272.5L107.3 261.9L109.2 252.1L111.2 243.2L113.5 235.2L115.9 227.9L118.6 221.5L121.3 215.7L124.2 210.6L127.2 206.3L130.4 202.4L133.6 199.2L137 196.4L140.4 194.1L144 192.2L147.9 190.6Z"/><path class="c1 sw3" d="M14 112L148 112" marker-end="url(#ah)"/><path class="c2 sw3" d="M148 146L14 146" marker-end="url(#ah)"/><path class="c1 sw2" d="M148 112L172 94"/><path class="c1 sw2" d="M148 112L160 128"/><path class="c2 sw2" d="M148 146L160 138"/><text class="tl" x="14" y="102">renal artery</text><text class="tl" x="14" y="166">renal vein</text><text class="tl" x="14" y="290">ureter</text><path class="ln-m thin" d="M56 286L91 286"/><text class="tl" x="282" y="34">fibrous capsule</text><path class="ln-m thin" d="M278 30L241.5 87.9"/><text class="tl" x="282" y="94">cortex</text><path class="ln-m thin" d="M278 90L241.5 116.2"/><text class="tl" x="282" y="178">medulla</text><path class="ln-m thin" d="M278 174L222.2 172"/><text class="tl" x="14" y="214">renal pelvis</text><path class="ln-m thin" d="M98 210L131 180"/></svg><figcaption>A kidney in section (a drawing). Blood enters in the renal artery and leaves in the renal vein; urine drains from the renal pelvis into the ureter.</figcaption></figure>
:::

| Part | What it is and what it does |
|---|---|
| fibrous capsule | the tough outer covering that protects the kidney |
| cortex | the outer region, which holds the glomeruli, Bowman's capsules and convoluted tubules |
| medulla | the inner region, which holds the loops of Henle and collecting ducts |
| renal pelvis | the funnel-shaped space in the middle where urine collects from the collecting ducts |
| ureter | carries urine from the renal pelvis to the bladder |
| renal artery and its branches | bring blood with urea to the kidney and divide into arterioles supplying the cortex |
| renal vein and its branches | take blood away from the kidney: it contains much less urea than the blood in the renal artery |

:::exam Looking at a section of a kidney
In a drawing or an image of a kidney cut lengthways, the **cortex** is the outer region just inside the capsule, the **medulla** is the darker, striped inner region, and the **renal pelvis** is the empty space at the centre where the ureter begins. If you are asked to identify the parts, work from the outside in: capsule, cortex, medulla, pelvis.
:::

## The nephron

The unit that makes urine is the **nephron**. Each kidney contains about a million of them. A nephron is a tube, closed at one end, with its own blood supply.

:::def Nephron
The functional unit of the kidney: a long tube, with its associated blood vessels, in which the blood is filtered and the filtrate is processed to form urine.
:::

The parts, in the order the filtrate meets them:

1. **Bowman's capsule**: a cup-shaped end of the tube in the cortex. Inside it is the **glomerulus**, a knot of capillaries. Filtrate forms here.
2. **Proximal convoluted tubule (PCT)**: a coiled tube in the cortex, where useful substances are reabsorbed.
3. **Loop of Henle**: a hairpin that dips into the medulla and comes back up to the cortex.
4. **Distal convoluted tubule (DCT)**: a second coiled tube in the cortex. It adjusts the ion balance of the blood.
5. **Collecting duct**: a straight tube that runs down through the medulla, where it receives filtrate from many nephrons. It carries urine to the renal pelvis.

The blood vessels matter as much as the tube. Blood arrives at the Bowman's capsule in an **afferent arteriole**, forms the glomerulus, and leaves in an **efferent arteriole**. The efferent arteriole then branches into a network of capillaries around the tubules, which rejoins to form branches of the renal vein.

:::html
<figure class="fig small"><svg viewBox="0 0 400 480" role="img" aria-label="A nephron and its blood supply, drawn in the cortex and medulla of the kidney. An afferent arteriole enters a Bowman's capsule, where it forms the glomerulus, and an efferent arteriole leaves it and forms a capillary network around the tubule that leads to the renal vein. The filtrate leaves the capsule in the proximal convoluted tubule, which is coiled and in the cortex. The tubule then runs down into the medulla as the descending limb of the loop of Henle, turns, and runs up as the ascending limb to the distal convoluted tubule, which is coiled and in the cortex. It joins a collecting duct, which runs down through the medulla to the renal pelvis."><rect class="fm s-acc sw2" x="108" y="16" width="190" height="214"/><rect class="fm2 s-acc sw2" x="108" y="230" width="190" height="224"/><text class="tl tb" x="114" y="34">cortex</text><text class="tl tb" x="208" y="340">medulla</text><circle class="fp ln" cx="170" cy="78" r="26"/><circle class="fr ln" cx="166" cy="74" r="8"/><circle class="fr ln" cx="176" cy="80" r="8"/><circle class="fr ln" cx="168" cy="84" r="6"/><path class="c1 sw3" d="M116 58L150 68" marker-end="url(#ah)"/><path class="c1 sw3" d="M160 98L140 110"/><path class="c1 thin dash sw2" d="M140 110L134 150L138 210L150 270L150 340" marker-end="url(#ah)"/><path class="c3 sw3" d="M170 104L150 116L190 128L150 140L190 152L170 164L170 420"/><path class="c3 sw3" d="M170 420L176 436L194 436L200 420"/><path class="c3 sw3" d="M200 420L200 216"/><path class="c3 sw3" d="M200 216L216 200L232 216L248 200L264 216"/><path class="c3 sw3" d="M264 216L264 442" marker-end="url(#ah)"/><text class="tl" x="98" y="48" text-anchor="end">afferent</text><text class="tl" x="98" y="62" text-anchor="end">arteriole</text><path class="ln-m thin" d="M102 58L122 60"/><text class="tl" x="98" y="112" text-anchor="end">efferent</text><text class="tl" x="98" y="126" text-anchor="end">arteriole</text><path class="ln-m thin" d="M102 118L142 108"/><text class="tl" x="98" y="172" text-anchor="end">capillary</text><text class="tl" x="98" y="186" text-anchor="end">network</text><path class="ln-m thin" d="M102 176L134 168"/><text class="tl" x="98" y="380" text-anchor="end">descending</text><text class="tl" x="98" y="394" text-anchor="end">limb</text><path class="ln-m thin" d="M102 384L166 384"/><text class="tl" x="98" y="440" text-anchor="end">loop of Henle</text><path class="ln-m thin" d="M102 436L173 436"/><text class="tl" x="98" y="330" text-anchor="end">to renal</text><text class="tl" x="98" y="344" text-anchor="end">vein</text><text class="tl" x="308" y="50">glomerulus</text><path class="ln-m thin" d="M304 46L178 78"/><text class="tl" x="308" y="78">Bowman's</text><text class="tl" x="308" y="92">capsule</text><path class="ln-m thin" d="M304 84L194 90"/><text class="tl" x="308" y="130">proximal</text><text class="tl" x="308" y="144">convoluted</text><text class="tl" x="308" y="158">tubule</text><path class="ln-m thin" d="M304 140L192 138"/><text class="tl" x="308" y="196">distal</text><text class="tl" x="308" y="210">convoluted</text><text class="tl" x="308" y="224">tubule</text><path class="ln-m thin" d="M304 200L246 202"/><text class="tl" x="308" y="300">collecting</text><text class="tl" x="308" y="314">duct</text><path class="ln-m thin" d="M304 304L268 304"/><text class="tl" x="308" y="372">ascending</text><text class="tl" x="308" y="386">limb</text><path class="ln-m thin" d="M304 376L203 376"/><text class="tl" x="264" y="472" text-anchor="middle">to renal pelvis</text></svg><figcaption>A nephron (a drawing, not to scale). The Bowman's capsule, proximal convoluted tubule and distal convoluted tubule are in the cortex; the loop of Henle and collecting duct run into the medulla.</figcaption></figure>
:::

:::exam Cortex or medulla?
Bowman's capsule, PCT and DCT are always in the **cortex**. The loop of Henle and collecting duct run into the **medulla**. To recognise a section of a nephron in a micrograph, look for a glomerulus with a clear space round it (Bowman's capsule), and for tubules cut across: a PCT has a ragged, fuzzy inner edge (microvilli) and densely stained cells, while collecting ducts are wide with clear, pale cells.
:::

## Ultrafiltration in the Bowman's capsule

:::def Ultrafiltration
Filtration at a molecular level, under pressure: small molecules are forced out of the blood plasma through a filter, while the cells and large molecules stay in the blood.
:::

Blood plasma is filtered under pressure in the glomerulus, and the fluid that passes through is the **glomerular filtrate**. Two features of the glomerulus make the pressure high.

- The **afferent arteriole is wider** than the efferent arteriole. Blood arrives faster than it can leave, so it backs up in the glomerular capillaries, giving a very high **hydrostatic pressure**.
- The capillaries of the glomerulus are narrow and form a dense knot, so the surface area for filtration is large.

The pressure pushes water and small solutes out of the capillary. The wall of the capillary and the wall of the Bowman's capsule form a three-layered filter.

:::html
<figure class="fig small"><svg viewBox="0 0 352 250" role="img" aria-label="Cross-section of the filter between a glomerular capillary and the Bowman's capsule. At the top is the capillary lumen with a red blood cell and plasma proteins. Below it is the capillary endothelium, a row of cells with gaps (pores) between them, then the basement membrane, a continuous layer. Under that are the podocytes, whose foot-like projections have slits between them, and then the capsule space. A dashed arrow shows water and small molecules passing through a pore, the basement membrane and a slit into the capsule space; the cell and proteins stay in the capillary."><rect class="fm s-acc sw2" x="10" y="8" width="230" height="80"/><rect class="f1 s-acc sw2" x="26" y="80" width="22" height="20"/><rect class="f1 s-acc sw2" x="62" y="80" width="22" height="20"/><rect class="f1 s-acc sw2" x="98" y="80" width="22" height="20"/><rect class="f1 s-acc sw2" x="134" y="80" width="22" height="20"/><rect class="f1 s-acc sw2" x="170" y="80" width="22" height="20"/><rect class="f1 s-acc sw2" x="206" y="80" width="22" height="20"/><rect class="f2 s-acc2 sw2" x="20" y="104" width="218" height="20"/><rect class="f1 s-acc sw2" x="26" y="128" width="24" height="18"/><rect class="f1 s-acc sw2" x="62" y="128" width="24" height="18"/><rect class="f1 s-acc sw2" x="98" y="128" width="24" height="18"/><rect class="f1 s-acc sw2" x="134" y="128" width="24" height="18"/><rect class="f1 s-acc sw2" x="170" y="128" width="24" height="18"/><rect class="f1 s-acc sw2" x="206" y="128" width="24" height="18"/><path class="f1 s-acc sw2" d="M138 164L137.6 165.8L136.2 167.6L134 169.4L131 171L127.3 172.5L122.8 173.9L117.7 175.1L112 176.1L105.9 176.9L99.5 177.5L92.8 177.9L86 178L79.2 177.9L72.5 177.5L66.1 176.9L60 176.1L54.3 175.1L49.2 173.9L44.7 172.5L41 171L38 169.4L35.8 167.6L34.4 165.8L34 164L34.4 162.2L35.8 160.4L38 158.6L41 157L44.7 155.5L49.2 154.1L54.3 152.9L60 151.9L66.1 151.1L72.5 150.5L79.2 150.1L86 150L92.8 150.1L99.5 150.5L105.9 151.1L112 151.9L117.7 152.9L122.8 154.1L127.3 155.5L131 157L134 158.6L136.2 160.4L137.6 162.2Z"/><path class="f1 s-acc sw2" d="M210 164L209.6 165.8L208.2 167.6L206 169.4L203 171L199.3 172.5L194.8 173.9L189.7 175.1L184 176.1L177.9 176.9L171.5 177.5L164.8 177.9L158 178L151.2 177.9L144.5 177.5L138.1 176.9L132 176.1L126.3 175.1L121.2 173.9L116.7 172.5L113 171L110 169.4L107.8 167.6L106.4 165.8L106 164L106.4 162.2L107.8 160.4L110 158.6L113 157L116.7 155.5L121.2 154.1L126.3 152.9L132 151.9L138.1 151.1L144.5 150.5L151.2 150.1L158 150L164.8 150.1L171.5 150.5L177.9 151.1L184 151.9L189.7 152.9L194.8 154.1L199.3 155.5L203 157L206 158.6L208.2 160.4L209.6 162.2Z"/><rect class="fp ln" x="10" y="196" width="230" height="30"/><path class="fr ln" d="M142 40L141.8 41.3L141.3 42.6L140.3 43.8L139.1 45L137.5 46.1L135.6 47.1L133.4 47.9L131 48.7L128.4 49.2L125.7 49.7L122.9 49.9L120 50L117.1 49.9L114.3 49.7L111.6 49.2L109 48.7L106.6 47.9L104.4 47.1L102.5 46.1L100.9 45L99.7 43.8L98.7 42.6L98.2 41.3L98 40L98.2 38.7L98.7 37.4L99.7 36.2L100.9 35L102.5 33.9L104.4 32.9L106.6 32.1L109 31.3L111.6 30.8L114.3 30.3L117.1 30.1L120 30L122.9 30.1L125.7 30.3L128.4 30.8L131 31.3L133.4 32.1L135.6 32.9L137.5 33.9L139.1 35L140.3 36.2L141.3 37.4L141.8 38.7Z"/><circle class="fi" cx="170" cy="30" r="4"/><circle class="fi" cx="196" cy="56" r="4"/><circle class="fi" cx="205" cy="28" r="4"/><circle class="fi" cx="30" cy="36" r="4"/><path class="c3 sw2 dash" d="M56 20L56 214" marker-end="url(#ah)"/><text class="tl" x="252" y="28">red blood cell</text><path class="ln-m thin" d="M248 24L141 36"/><text class="tl" x="252" y="54">plasma protein</text><path class="ln-m thin" d="M248 50L200 54"/><text class="tl" x="252" y="94">capillary</text><text class="tl" x="252" y="108">endothelium</text><path class="ln-m thin" d="M248 90L222 90"/><text class="tl" x="252" y="134">basement</text><text class="tl" x="252" y="148">membrane</text><path class="ln-m thin" d="M248 130L236 116"/><text class="tl" x="252" y="172">podocyte</text><text class="tl" x="252" y="186">(slits between</text><text class="tl" x="252" y="200">its feet)</text><path class="ln-m thin" d="M248 168L136 168"/><text class="tl" x="252" y="222">capsule space</text><path class="ln-m thin" d="M248 218L200 214"/><text class="tl" x="252" y="236">(filtrate)</text></svg><figcaption>The three layers of the filter. Water and small molecules pass through the pores, the basement membrane and the slits between the podocyte projections; blood cells and plasma proteins stay in the capillary.</figcaption></figure>
:::

:::steps
1. **Capillary endothelium.** The cells have many pores (gaps) through them. Blood cells and platelets are too large to pass, but the plasma passes easily.
2. **Basement membrane.** A continuous layer of collagen fibres and glycoproteins between the endothelium and the capsule cells. It is the actual **filter**: its mesh stops large molecules, such as plasma proteins, from passing.
3. **Podocytes.** The cells of the capsule wall have finger-like projections, with narrow slits between them. The filtrate squeezes through the slits into the capsule space.
:::

What passes and what stays:

| Passes into the filtrate (small) | Stays in the blood (large) |
|---|---|
| water | red blood cells and white blood cells |
| glucose | platelets |
| amino acids | plasma proteins |
| urea | |
| mineral ions such as sodium and chloride | |

The filtrate is therefore plasma without its proteins. No energy is used by the filter itself: it works by pressure and size, not by active transport.

:::warn Ultrafiltration is passive and does not choose
The filter selects by **size only**. Glucose passes into the filtrate because it is small, not because the body wants to lose it. It is **reabsorbed** later. Also, proteins stay in the blood because they are too large for the basement membrane, not because they are "pumped back".
:::

:::eg Explain how the structure of the Bowman's capsule and glomerulus allows the formation of the glomerular filtrate.
The question asks for structure linked to function, so every point names a feature and what it does.

The afferent arteriole is wider than the efferent arteriole, so the blood in the glomerulus is at a high hydrostatic pressure. [B1]

The pressure forces water and small molecules out of the blood through the pores in the capillary endothelium. [B1]

The basement membrane acts as a filter: it stops large molecules such as plasma proteins, while allowing small molecules such as glucose, urea and ions to pass. [B1]

The podocytes have slits between their finger-like projections, so the filtrate can pass into the capsule space. [B1]

(Also credit: the glomerulus is a knot of capillaries, giving a large surface area; blood cells are too large to pass the pores.)

A weaker answer says "the blood is filtered in the glomerulus". It names no feature, no pressure and no layer, and scores no marks.
:::

### Reading the numbers

The table shows typical values for plasma, glomerular filtrate and urine in a healthy person.

:::eg The table gives typical concentrations in a healthy person. Explain the differences between plasma, filtrate and urine for each of glucose, protein and urea.
| substance | plasma / g dm⁻³ | filtrate / g dm⁻³ | urine / g dm⁻³ |
|---|---|---|---|
| glucose | 1.0 | 1.0 | 0.0 |
| protein | 70 | 0.0 | 0.0 |
| urea | 0.3 | 0.3 | 20 |

**Protein.** The plasma contains 70 g dm⁻³ and the filtrate none: protein molecules are too large to pass through the basement membrane. [B1]

**Glucose.** The filtrate has the same concentration as the plasma (1.0 g dm⁻³), because glucose is small and passes freely through the filter. [B1] The urine has none, so all of the glucose has been reabsorbed from the filtrate into the blood, in the proximal convoluted tubule. [B1]

**Urea.** The filtrate has the same concentration as the plasma (0.3 g dm⁻³), because urea is small and passes the filter. [B1] The urine concentration is much higher, \(20 \div 0.3 = 67\) times, because most of the water in the filtrate is reabsorbed, while the urea stays in the tubule. [B1]

(Also credit: no protein in urine means the filter is not damaged.)

The key idea: the filtrate has the **composition of plasma minus proteins**. Everything that makes urine different from the filtrate is done by the tubule.
:::

## Selective reabsorption in the proximal convoluted tubule

A healthy adult makes about 180 dm³ of glomerular filtrate a day but only about 1.5 dm³ of urine, so over 99% of the water in the filtrate returns to the blood. The glucose, amino acids and most of the ions return too. This is **selective reabsorption**, and most of it happens in the **proximal convoluted tubule (PCT)**.

:::def Selective reabsorption
The movement of useful substances, such as glucose, amino acids, water and ions, from the filtrate in the nephron back into the blood, while waste products such as urea stay in the filtrate.
:::

The cells of the PCT are specialised for the job. Each feature below links to a function, and you must give both.

| Feature of a PCT cell | Function |
|---|---|
| microvilli on the surface facing the lumen | increase the surface area for reabsorption |
| many mitochondria | supply the ATP for active transport (the sodium–potassium pumps) |
| sodium–potassium pumps in the basal membrane | keep the concentration of sodium ions inside the cell low |
| cotransporter proteins in the membrane facing the lumen | carry glucose or amino acids into the cell together with sodium ions |
| carrier proteins in the basal membrane | let glucose and amino acids leave the cell by facilitated diffusion |
| one cell thick, next to blood capillaries | short diffusion distance; a steep concentration gradient is kept up |

:::html
<figure class="fig small"><svg viewBox="0 0 400 372" role="img" aria-label="A cell of the proximal convoluted tubule. The surface facing the lumen of the tubule has microvilli. A cotransporter protein in that membrane carries sodium ions and glucose into the cell together. The cell contains a nucleus and mitochondria. In the membrane facing the blood are a sodium–potassium pump, which moves sodium ions out of the cell and potassium ions in using ATP, and a carrier protein through which glucose leaves by facilitated diffusion. Below the cell is tissue fluid and then a blood capillary."><path class="f1 s-acc sw2" d="M112 272L112 106L112 88L124 88L124 106L136 106L136 88L148 88L148 106L160 106L160 88L172 88L172 106L184 106L184 88L196 88L196 106L208 106L208 88L220 88L220 106L232 106L232 88L244 88L244 106L256 106L256 88L268 88L268 106L280 106L280 88L292 88L292 106L292 272Z"/><path class="fm s-acc sw2" d="M172 190L171.8 192.3L171.3 194.7L170.3 196.9L169.1 199L167.5 201L165.6 202.7L163.4 204.3L161 205.6L158.4 206.6L155.7 207.4L152.9 207.8L150 208L147.1 207.8L144.3 207.4L141.6 206.6L139 205.6L136.6 204.3L134.4 202.7L132.5 201L130.9 199L129.7 196.9L128.7 194.7L128.2 192.3L128 190L128.2 187.7L128.7 185.3L129.7 183.1L130.9 181L132.5 179L134.4 177.3L136.6 175.7L139 174.4L141.6 173.4L144.3 172.6L147.1 172.2L150 172L152.9 172.2L155.7 172.6L158.4 173.4L161 174.4L163.4 175.7L165.6 177.3L167.5 179L169.1 181L170.3 183.1L171.3 185.3L171.8 187.7Z"/><path class="f2 s-acc2 sw2" d="M235 244L234.9 245L234.6 246.1L234 247.1L233.3 248L232.3 248.9L231.2 249.7L229.9 250.3L228.5 250.9L227 251.4L225.4 251.7L223.7 251.9L222 252L220.3 251.9L218.6 251.7L217 251.4L215.5 250.9L214.1 250.3L212.8 249.7L211.7 248.9L210.7 248L210 247.1L209.4 246.1L209.1 245L209 244L209.1 243L209.4 241.9L210 240.9L210.7 240L211.7 239.1L212.8 238.3L214.1 237.7L215.5 237.1L217 236.6L218.6 236.3L220.3 236.1L222 236L223.7 236.1L225.4 236.3L227 236.6L228.5 237.1L229.9 237.7L231.2 238.3L232.3 239.1L233.3 240L234 240.9L234.6 241.9L234.9 243Z"/><path class="f2 s-acc2 sw2" d="M271 232L270.9 233L270.6 234.1L270 235.1L269.3 236L268.3 236.9L267.2 237.7L265.9 238.3L264.5 238.9L263 239.4L261.4 239.7L259.7 239.9L258 240L256.3 239.9L254.6 239.7L253 239.4L251.5 238.9L250.1 238.3L248.8 237.7L247.7 236.9L246.7 236L246 235.1L245.4 234.1L245.1 233L245 232L245.1 231L245.4 229.9L246 228.9L246.7 228L247.7 227.1L248.8 226.3L250.1 225.7L251.5 225.1L253 224.6L254.6 224.3L256.3 224.1L258 224L259.7 224.1L261.4 224.3L263 224.6L264.5 225.1L265.9 225.7L267.2 226.3L268.3 227.1L269.3 228L270 228.9L270.6 229.9L270.9 231Z"/><path class="f2 s-acc2 sw2" d="M203 248L202.9 249L202.6 250.1L202 251.1L201.3 252L200.3 252.9L199.2 253.7L197.9 254.3L196.5 254.9L195 255.4L193.4 255.7L191.7 255.9L190 256L188.3 255.9L186.6 255.7L185 255.4L183.5 254.9L182.1 254.3L180.8 253.7L179.7 252.9L178.7 252L178 251.1L177.4 250.1L177.1 249L177 248L177.1 247L177.4 245.9L178 244.9L178.7 244L179.7 243.1L180.8 242.3L182.1 241.7L183.5 241.1L185 240.6L186.6 240.3L188.3 240.1L190 240L191.7 240.1L193.4 240.3L195 240.6L196.5 241.1L197.9 241.7L199.2 242.3L200.3 243.1L201.3 244L202 244.9L202.6 245.9L202.9 247Z"/><rect class="fm s-acc sw2" x="152" y="100" width="14" height="16"/><path class="c3 sw2" d="M159 56L159 150" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="240" y="264" width="14" height="16"/><path class="c3 sw2" d="M247 200L247 308" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="126" y="264" width="14" height="16"/><path class="c2 sw2" d="M133 224L133 308" marker-end="url(#ah)"/><rect class="fp ln" x="118" y="316" width="174" height="40"/><text class="tl" x="104" y="40" text-anchor="end">lumen of PCT</text><text class="tl" x="104" y="54" text-anchor="end">(filtrate)</text><text class="tl" x="104" y="98" text-anchor="end">microvilli</text><path class="ln-m thin" d="M108 94L118 96"/><text class="tl" x="104" y="192" text-anchor="end">nucleus</text><path class="ln-m thin" d="M108 190L128 190"/><text class="tl" x="104" y="296" text-anchor="end">tissue fluid</text><text class="tl" x="104" y="340" text-anchor="end">blood in</text><text class="tl" x="104" y="354" text-anchor="end">capillary</text><text class="tl" x="172" y="40">cotransporter protein</text><text class="tl" x="172" y="54">carries sodium ions</text><text class="tl" x="172" y="68">and glucose in</text><text class="tl" x="302" y="230">mitochondria</text><path class="ln-m thin" d="M298 226L272 232"/><text class="tl" x="302" y="262">carrier</text><text class="tl" x="302" y="276">protein</text><text class="tl" x="302" y="290">(glucose out)</text><path class="ln-m thin" d="M298 268L256 272"/><text class="tl" x="104" y="262" text-anchor="end">Na⁺/K⁺ pump</text><text class="tl" x="104" y="276" text-anchor="end">(uses ATP)</text><path class="ln-m thin" d="M108 268L124 272"/></svg><figcaption>A PCT cell. Sodium–potassium pumps in the basal membrane keep the sodium ion concentration inside the cell low; sodium ions then enter with glucose by cotransport, and glucose leaves by facilitated diffusion into the blood.</figcaption></figure>
:::

The mechanism of glucose reabsorption, step by step:

:::steps
1. Sodium–potassium pumps in the **basal membrane** use ATP to move sodium ions out of the cell into the tissue fluid (and potassium ions in). The concentration of sodium ions **inside** the cell is now low.
2. Sodium ions diffuse down their concentration gradient from the filtrate into the cell, through **cotransporter proteins** in the membrane facing the lumen. Each carrier brings a **glucose** molecule (or an amino acid) with the sodium ions: this is **cotransport** (a form of facilitated diffusion).
3. The glucose concentration inside the cell is now higher than in the tissue fluid, so glucose leaves by **facilitated diffusion** through a carrier protein in the basal membrane, and is carried away by the blood in the capillary.
4. Glucose and ions that have entered the tissue fluid and blood lower its water potential, and taking them out of the filtrate raises the water potential of the filtrate. **Water moves by osmosis** from the filtrate to the tissue fluid and the blood.
:::

The cotransport carrier is the same idea as the carrier that absorbs glucose in the small intestine (see the oral rehydration example in [Movement across membranes](#bio.movement)). The energy for the glucose uptake is provided indirectly: ATP is used by the sodium–potassium pump, and the sodium concentration gradient then drives the uptake of glucose.

:::eg Describe and explain how glucose in the glomerular filtrate is reabsorbed into the blood in the proximal convoluted tubule.
Sodium ions are actively transported out of the cell, across the basal membrane, into the tissue fluid by the sodium–potassium pump, using ATP. [B1]

This lowers the concentration of sodium ions in the cell, so sodium ions diffuse in from the filtrate down their concentration gradient. [B1]

They enter through a cotransporter protein, which carries glucose into the cell at the same time (cotransport). [B1]

Glucose then leaves the cell and enters the blood by facilitated diffusion through carrier proteins in the basal membrane. [B1]

The cells have microvilli and many mitochondria, which give a large surface area and supply ATP. [B1]

(Also credit: water follows by osmosis; the cells are in contact with a capillary network that carries the glucose away.)
:::

:::eg Real context: glucose in the urine of a person with uncontrolled diabetes. Explain why.
In a person whose blood glucose is far above normal, the glomerular filtrate has a very high concentration of glucose, because glucose passes through the filter freely. [B1]

The PCT has a limited number of cotransporter and carrier proteins, and when all of them are working at their maximum rate, they are saturated. [B1]

Glucose that cannot be reabsorbed stays in the filtrate and is excreted in the urine. [B1]

The glucose also lowers the water potential of the filtrate, so less water is reabsorbed by osmosis and the person produces a larger volume of urine and becomes thirsty. [B1]

(Also credit: testing urine for glucose is one sign of diabetes, as you will see in [Blood glucose, cell signalling and biosensors](#bio.glucose).)
:::

### The rest of the nephron

The **loop of Henle** is the part of the nephron that makes the tissue fluid in the medulla have a very low water potential (it does this by moving ions out of the tubule; the detail is not required). That low water potential in the medulla is what allows water to be drawn out of the collecting duct. The **distal convoluted tubule** adjusts the concentration of ions in the blood, and the **collecting duct** is where the volume and concentration of the urine are finally set.

## Osmoregulation and ADH

:::def Osmoregulation
The control of the water potential of the blood and tissue fluid, by adjusting the volume and the concentration of the urine.
:::

If you sweat a lot, or eat a salty meal, the water potential of your blood **falls**. If you drink a lot of water, it **rises**. The body keeps it constant by changing how much water is reabsorbed from the **collecting duct**. The signal is the hormone **ADH** (antidiuretic hormone).

:::def Antidiuretic hormone (ADH)
A peptide hormone made in the hypothalamus and released from the posterior pituitary gland. It makes the collecting ducts more permeable to water, so more water is reabsorbed and a smaller volume of more concentrated urine is made.
:::

The roles of the different parts:

| Part | Role in osmoregulation |
|---|---|
| hypothalamus | contains **osmoreceptors** that detect the water potential of the blood; its neurosecretory cells make ADH |
| posterior pituitary gland | stores ADH and releases it into the blood when it receives impulses from the hypothalamus |
| ADH | the hormone: carried in the blood to the kidney |
| collecting duct cells | have receptors for ADH; they respond by inserting aquaporins in their membranes |
| aquaporins | channel proteins that let water molecules cross the membrane quickly by osmosis |

:::html
<figure class="fig small"><svg viewBox="0 0 340 434" role="img" aria-label="A flow chart in seven boxes joined by downward arrows: blood water potential falls; osmoreceptors in the hypothalamus detect it; the posterior pituitary releases more ADH; ADH binds to receptors on collecting duct cells; vesicles with aquaporins fuse with the membrane; more water is reabsorbed by osmosis; a small volume of concentrated urine is made. An arrow from the last box back to the first shows that the water potential of the blood rises, so less ADH is released."><rect class="f1 s-acc sw2" x="30" y="10" width="210" height="40"/><text class="tl" x="135" y="27" text-anchor="middle">blood water potential</text><text class="tl" x="135" y="42" text-anchor="middle">falls</text><path class="c1 sw2" d="M135 50L135 72" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="30" y="72" width="210" height="40"/><text class="tl" x="135" y="89" text-anchor="middle">osmoreceptors in the</text><text class="tl" x="135" y="104" text-anchor="middle">hypothalamus detect it</text><path class="c1 sw2" d="M135 112L135 134" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="30" y="134" width="210" height="40"/><text class="tl" x="135" y="151" text-anchor="middle">posterior pituitary</text><text class="tl" x="135" y="166" text-anchor="middle">releases more ADH</text><path class="c1 sw2" d="M135 174L135 196" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="30" y="196" width="210" height="40"/><text class="tl" x="135" y="213" text-anchor="middle">ADH binds to receptors on</text><text class="tl" x="135" y="228" text-anchor="middle">collecting duct cells</text><path class="c1 sw2" d="M135 236L135 258" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="30" y="258" width="210" height="40"/><text class="tl" x="135" y="275" text-anchor="middle">vesicles with aquaporins</text><text class="tl" x="135" y="290" text-anchor="middle">fuse with the membrane</text><path class="c1 sw2" d="M135 298L135 320" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="30" y="320" width="210" height="40"/><text class="tl" x="135" y="337" text-anchor="middle">more water reabsorbed</text><text class="tl" x="135" y="352" text-anchor="middle">by osmosis</text><path class="c1 sw2" d="M135 360L135 382" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="30" y="382" width="210" height="40"/><text class="tl" x="135" y="399" text-anchor="middle">small volume of</text><text class="tl" x="135" y="414" text-anchor="middle">concentrated urine</text><path class="c2 sw2" d="M240 402L320 402L320 30L244 30" marker-end="url(#ah)"/><text class="tl" x="250" y="190">water</text><text class="tl" x="250" y="204">potential</text><text class="tl" x="250" y="218">rises, so</text><text class="tl" x="250" y="232">less ADH</text></svg><figcaption>The ADH pathway when the water potential of the blood falls. The return arrow is negative feedback: a rise in blood water potential reduces ADH release.</figcaption></figure>
:::

When the water potential of the blood **falls** (the person is short of water):

:::steps
1. **Osmoreceptors** in the hypothalamus detect the fall in the water potential of the blood.
2. The hypothalamus sends impulses to the **posterior pituitary gland**, which releases more **ADH** into the blood.
3. ADH travels in the blood to the kidney. It **binds to receptors** on the cell surface membranes of the cells of the **collecting duct**.
4. Binding causes **vesicles containing aquaporins** to move to the cell surface membrane and fuse with it. The membrane is now much more permeable to water.
5. **More water is reabsorbed by osmosis** from the filtrate in the collecting duct, down a water potential gradient, into the tissue fluid of the medulla (which has a very low water potential) and then into the blood.
6. A **small volume of concentrated urine** is made, the blood water potential rises, and the osmoreceptors are stimulated less: negative feedback.
:::

When the water potential of the blood **rises**, the pathway is the reverse. Less ADH is released, the aquaporins are taken back into the cytoplasm by endocytosis, the collecting duct is less permeable to water, little water is reabsorbed, and a **large volume of dilute urine** is made.

:::note Sources differ on the distal convoluted tubule
Some textbooks say ADH also acts on the distal convoluted tubule. The syllabus names the collecting ducts, so use them in your answers.
:::

:::warn ADH is not made in the pituitary gland
Say that ADH is **made in the hypothalamus** and **released from the posterior pituitary gland**. Also, ADH does not "make the kidney hold water" in general: it makes the **collecting duct cells** more permeable by increasing the number of **aquaporins** in their membranes. And a higher ADH level gives a **smaller** volume of urine, not a larger one.
:::

:::eg A person runs for two hours on a hot day and drinks no water. Explain the changes in the volume and concentration of the urine they produce afterwards.
This is a full six-mark question. Follow the sweat, the receptor, the hormone and the collecting duct in order.

The person loses water in sweat, so the water potential of the blood falls. [B1]

Osmoreceptors in the hypothalamus detect the lower water potential. [B1]

The posterior pituitary gland releases more ADH into the blood. [B1]

ADH binds to receptors on the cells of the collecting duct, and vesicles containing aquaporins fuse with the cell surface membrane. [B1]

The collecting duct becomes more permeable to water, so more water is reabsorbed by osmosis into the medulla, which has a low water potential. [B1]

So the person makes a small volume of urine that is concentrated (it has a low water potential), and the blood water potential rises back to normal: negative feedback. [B1]

A weaker answer says "ADH is released so the kidney reabsorbs more water". It does not say what detects the change, where ADH is released from, or how the collecting duct changes, and scores two marks.
:::

:::eg Spot the error: describe how the glomerular filtrate is formed. [3]
A student wrote this answer.

Line 1: The afferent arteriole is wider than the efferent arteriole, which gives a high hydrostatic pressure in the glomerulus.
Line 2: Small molecules such as glucose and amino acids are actively transported through the basement membrane into the capsule.
Line 3: The basement membrane acts as a filter and stops large molecules such as proteins.

Line 1 is correct [B1]. **Line 2 is wrong: ultrafiltration is a passive process. Small molecules are forced through the pores, the basement membrane and the slits by the hydrostatic pressure, and no active transport or ATP is involved. That mark is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "The pressure forces water and small molecules such as glucose and amino acids through the pores in the capillary wall and the slits between the podocytes." With that change the answer scores 3 marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State what is meant by homeostasis.
A: The maintenance of a constant internal environment, within narrow limits, in spite of changes in the external environment and inside the body.
Q: Name the organ in which urea is made and the process that produces the ammonia from which it is formed.
A: The liver. Deamination of excess amino acids (removal of the amino group).
Q: Put these in the order in which filtrate passes through them: collecting duct, Bowman's capsule, distal convoluted tubule, loop of Henle, proximal convoluted tubule.
A: Bowman's capsule, proximal convoluted tubule, loop of Henle, distal convoluted tubule, collecting duct.
Q: Which blood vessel is wider, the afferent or the efferent arteriole, and what does this do to the pressure in the glomerulus?
A: The afferent arteriole is wider. Blood arrives faster than it leaves, so the hydrostatic pressure in the glomerulus is high.
Q: A healthy adult makes about 150 dm³ of glomerular filtrate in a day and 2.5 dm³ of urine. Calculate the percentage of the filtrate volume that is reabsorbed.
A: \((150 - 2.5) \div 150 \times 100 = 98.3\%\) (to 3 significant figures).
Q: Explain why there are no blood cells in the glomerular filtrate of a healthy person.
A: Blood cells are too large to pass through the pores in the capillary endothelium and the basement membrane, which acts as the filter.
Q: Explain why a PCT cell has many mitochondria.
A: They make ATP by aerobic respiration. The ATP is used by the sodium–potassium pumps in the basal membrane, which keep the sodium concentration in the cell low, so that sodium ions (and glucose by cotransport) can enter.
Q: State where the osmoreceptors that control the release of ADH are found, and what they detect.
A: In the hypothalamus. They detect the water potential of the blood.
Q: Explain what is meant by a set point, and why a factor under negative feedback swings a little above and below it.
A: The set point is the normal value of the factor. A response takes time to work, so the factor goes a little past the set point before the response corrects it, and then the opposite response corrects the swing in the other direction.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ A house has a heating system with a thermostat. The thermostat detects that the room is too cold and switches on the heater; when the room is warm enough it switches the heater off. Match the parts of this system to the parts of a homeostatic control loop in the body, and state why this is negative feedback.
A: The thermostat is the receptor (and the coordinator, which decides). [B1]
The heater is the effector. [B1]
The change in the room temperature is the stimulus. [B1]
It is negative feedback because the response (heating) reverses the change that caused it (the cooling), and the system switches off when the set point is reached. [B1]
Q: [3 marks] ★ State where urea is made, what it is made from and how it reaches the kidney.
A: Urea is made in the liver. [B1]
It is made from ammonia (formed by deamination of excess amino acids) and carbon dioxide. [B1]
It is carried in the blood plasma to the kidney. [B1]
Q: [4 marks] ★★ The table shows the relative molecular mass of four substances found in blood plasma and whether each is found in the glomerular filtrate of a healthy person.

| substance | relative molecular mass | in filtrate? |
|---|---|---|
| water | 18 | yes |
| urea | 60 | yes |
| glucose | 180 | yes |
| albumin (a plasma protein) | 69 000 | no |

(a) Use the table to suggest how the basement membrane selects substances. (b) A patient has a lot of albumin in their urine. Suggest what has gone wrong in the kidney.
H: Compare the sizes of the molecules that pass with the size of the molecule that does not.
H: If the filter is damaged, what happens to the size of the molecules it lets through?
A: (a) Molecules with a small relative molecular mass (such as 180) pass, but a large molecule (69 000) does not. [B1]
The basement membrane acts as a filter that selects by size. [B1]
(b) The filter in the glomerulus (the basement membrane or the podocyte slits) is damaged, so large protein molecules pass into the filtrate. [B1]
The PCT cannot reabsorb all of them (they are too large for the transport proteins), so albumin appears in the urine. [B1]
Q: [4 marks] ★★ The concentration of glucose in the filtrate was measured at five points along the proximal convoluted tubule of a healthy person. The distance is from the Bowman's capsule.

| distance along the PCT / mm | glucose / mmol dm⁻³ |
|---|---|
| 0 | 5.0 |
| 3 | 3.5 |
| 6 | 1.8 |
| 9 | 0.4 |
| 12 | 0.0 |

(a) Describe the change in the concentration of glucose along the PCT. (b) A poison that stops the production of ATP in the PCT cells is added. Predict the effect on the concentration of glucose in the urine, and explain.
H: For (a), give the start and end values with units and name the trend.
H: For (b), which pump depends on ATP, and what does it do to the sodium gradient that drives cotransport?
A: (a) The concentration of glucose decreases along the tubule, from 5.0 mmol dm⁻³ at the start to 0.0 mmol dm⁻³ by 12 mm. [B1]
(b) The sodium–potassium pumps stop working, so the concentration of sodium ions in the cell is no longer kept low. [B1]
So sodium ions no longer diffuse into the cell by cotransport, and glucose is not carried in with them. [B1]
Less glucose is reabsorbed, so the concentration of glucose in the urine increases from zero. [B1]
(Also credit: less water is reabsorbed from the filtrate, because less solute has been removed from it.)
Q: [5 marks] ★★ In a condition called diabetes insipidus, the posterior pituitary gland releases too little ADH. (a) Describe and explain the symptoms in the volume and concentration of the urine. (b) A patient is treated with a nasal spray containing ADH. Explain how the spray treats the condition.
H: With too little ADH, what happens to the aquaporins in the collecting duct cells?
A: (a) The collecting ducts are not very permeable to water, because few aquaporins are inserted in their membranes, so little water is reabsorbed. [B1]
A large volume of dilute urine is made, and the person loses so much water that the blood water potential falls, which makes them very thirsty. [B1]
(b) ADH is carried in the blood to the collecting ducts and binds to receptors on their cells. [B1]
Vesicles with aquaporins fuse with the membrane, so more water is reabsorbed by osmosis. [B1]
The urine is smaller in volume and more concentrated. [B1]
Q: [6 marks] ★★★ A volunteer drank 1.0 dm³ of water at time 0. The table shows the rate at which urine was produced and the concentration of ADH in the blood.

| time / min | urine flow / cm³ min⁻¹ | ADH in blood / arbitrary units |
|---|---|---|
| 0 | 1 | 9 |
| 30 | 3 | 5 |
| 60 | 12 | 2 |
| 90 | 10 | 3 |
| 120 | 4 | 7 |

(a) Describe the changes in urine flow and ADH concentration over the 120 minutes. (b) The volunteer drank nothing more, yet the ADH concentration rose again after 90 minutes. Explain why. (c) Calculate how many times greater the urine flow was at 60 minutes than at time 0.
H: For (a), quote figures with units and give the turning point.
H: For (b), what has happened to the water the volunteer drank by this time, and so to the water potential of the blood?
A: (a) The urine flow rises from 1 cm³ min⁻¹ to a maximum of 12 cm³ min⁻¹ at 60 min, then falls to 4 cm³ min⁻¹ at 120 min. [B1]
ADH falls from 9 to 2 arbitrary units at 60 min, then rises to 7 units at 120 min. [B1]
(b) The extra water has been excreted, so the water potential of the blood falls back towards its normal value; the osmoreceptors in the hypothalamus detect this. [B1]
More ADH is released from the posterior pituitary gland, so more water is reabsorbed in the collecting ducts and the urine flow falls: negative feedback. [B1]
(c) \(12 \div 1\) [M1] \(= 12\) times [A1]
Q: [6 marks] (#bio.mammaltransport) ★★★ A man eats a meal with a lot of protein. His urine contains more urea than usual 24 hours later. Explain this, from the digestion of the protein to the excretion of urea.
H: Think about what is absorbed, what the liver does with amino acids that are not needed, and how urea reaches the kidney.
A: The protein is hydrolysed to amino acids by proteases, and the amino acids are absorbed into the blood. [B1]
Amino acids that are not needed for protein synthesis cannot be stored, and are carried to the liver. [B1]
In the liver, deamination removes the amino group as ammonia, leaving a keto acid that is used in respiration. [B1]
The ammonia is converted to urea (with carbon dioxide). [B1]
Urea is carried in the blood plasma to the kidney, passes through the filter in the glomerulus into the filtrate, and stays in the tubule as the water is reabsorbed. [B1]
So it is excreted in a higher concentration in the urine. [B1]
Q: [5 marks] (#bio.membranes) ★★★ ADH is a peptide hormone. (a) Explain why ADH acts by binding to a receptor in the cell surface membrane of its target cells, and does not enter them. (b) Explain why only the collecting duct cells respond to ADH, although the blood carries it to every organ. (c) Water molecules can cross a phospholipid bilayer slowly by themselves. Explain why the collecting duct cells need aquaporins.
H: For (a), think about what the hydrophobic centre of the bilayer does to a large polar molecule.
H: For (b), what must a cell have for a hormone to bind?
A: (a) ADH is a large, polar molecule, so it cannot pass through the hydrophobic centre of the phospholipid bilayer. [B1]
So it must bind to a receptor on the outside of the cell, which passes the message to the inside of the cell. [B1]
(b) Only the collecting duct cells have receptors whose binding site is complementary to the shape of ADH. [B1]
Cells without the receptor cannot bind ADH, so they do not respond. [B1]
(c) Aquaporins are channel proteins through which water crosses the membrane by osmosis much faster, so the large volume of water in the filtrate can be reabsorbed quickly. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ During an infection, bacterial toxins raise the set point of the temperature control centre in the hypothalamus from 37 °C to 39 °C. For the first 30 minutes the person feels cold and shivers, and their skin is pale. Later the toxins are cleared, the set point returns to 37 °C and the person sweats heavily and looks flushed. (a) Explain why the person shivers and has pale skin at the start. (b) Explain why they sweat and look flushed later. (c) State whether homeostasis has failed during the fever.
H: Compare the actual blood temperature with the new set point in each stage.
H: Which effectors raise the temperature, and which lower it?
A: (a) At first the blood temperature is 37 °C, which is below the new set point of 39 °C. [B1]
The hypothalamus therefore sends impulses to the effectors that raise the temperature: skeletal muscles shiver, releasing heat from respiration. [B1]
Skin arterioles constrict (vasoconstriction), so less blood flows near the surface and the skin is pale; less heat is lost. [B1]
(b) When the set point returns to 37 °C, the blood temperature (39 °C) is above it. [B1]
So the effectors that lose heat respond: sweat glands secrete sweat, which evaporates from the skin, and skin arterioles dilate (vasodilation), so more blood flows near the surface and the skin is flushed. [B1]
(c) No: homeostasis has not failed. Negative feedback is still working, but around a different set point. [B1]
Q: [6 marks] ★★★ Lithium, a drug used to treat some mental illnesses, can damage the receptors for ADH on the cells of the collecting duct. A patient taking lithium produces a large volume of dilute urine and is always thirsty. Blood tests show a high concentration of ADH. (a) Explain why the urine is dilute and in large volume. (b) Explain why the concentration of ADH in the blood is high. (c) Explain why giving the patient ADH would not help.
H: What does ADH have to do to the collecting duct cells before aquaporins reach the membrane?
A: (a) ADH cannot bind to its receptors on the collecting duct cells, so vesicles with aquaporins do not fuse with the cell surface membrane. [B1]
The collecting duct stays impermeable to water, so little water is reabsorbed and a large volume of dilute urine is made. [B1]
(b) The patient loses water, so the water potential of the blood falls. [B1]
The osmoreceptors in the hypothalamus detect this and the posterior pituitary gland releases more ADH; the response of the kidney does not reverse the change, so the stimulus continues. [B1]
(c) The problem is in the receptors, not in the supply of the hormone. [B1]
More ADH could not bind to the damaged receptors, so the collecting duct would still not respond. [B1]
:::

:::quiz
? Which statement about the glomerular filtrate in a healthy person is correct?
+ It has the same concentration of glucose as the blood plasma but contains no protein.
- It contains no glucose, because the glomerulus reabsorbs it.
- It contains red blood cells but no urea.
- It has a higher concentration of urea than urine.
> Small molecules such as glucose and urea pass through the filter in the same concentration as in the plasma, but proteins and cells are too large. Glucose is reabsorbed later in the PCT, and urea is more concentrated in the urine.
? What causes the high hydrostatic pressure in the glomerulus?
+ The afferent arteriole is wider than the efferent arteriole.
- The efferent arteriole is wider than the afferent arteriole.
- The podocytes pump blood into the capillaries.
- Active transport of sodium ions into the capsule.
> Blood enters through the wide afferent arteriole and leaves through the narrower efferent one, so it backs up in the glomerulus. Ultrafiltration does not use active transport.
? Where is urea produced?
+ in the liver, from the deamination of excess amino acids
- in the kidney, from excess glucose
- in the pancreas, from the digestion of proteins
- in the bladder, from the breakdown of ammonia
> Urea is made in the liver. The kidney only removes it from the blood.
? Which part of the filter is the basement membrane?
+ a layer of collagen and glycoproteins that stops large molecules such as proteins
- the cells with finger-like projections that surround the capillary
- the pores between the cells of the capillary wall
- the wall of the proximal convoluted tubule
> The podocytes are the cells with projections and slits, and the pores are in the endothelium. The basement membrane between them is the actual filter.
? How does glucose enter a cell of the proximal convoluted tubule from the filtrate?
+ by cotransport with sodium ions through a carrier protein
- by simple diffusion through the phospholipid bilayer
- by active transport using ATP directly at the apical membrane
- by endocytosis of the filtrate
> The sodium–potassium pump in the basal membrane uses ATP and keeps the sodium concentration in the cell low, so sodium ions enter with glucose by cotransport. Glucose is polar and cannot cross the bilayer on its own.
? Where is ADH made and where is it released from?
+ made in the hypothalamus; released from the posterior pituitary gland
- made in the posterior pituitary gland and released from the hypothalamus
- made in the kidney and released from the collecting duct
- made in the hypothalamus and released from the adrenal gland
> Neurosecretory cells in the hypothalamus make ADH, which passes down their axons to the posterior pituitary gland. It is released from there into the blood.
? What happens in the cells of the collecting duct when ADH binds to its receptor?
+ vesicles containing aquaporins fuse with the cell surface membrane
- the cells actively transport water into the medulla
- sodium–potassium pumps are inserted into the membrane
- the cells make more urea
> Aquaporins are channel proteins that allow water to cross by osmosis. Water is not actively transported.
? A person drinks a large volume of water. Which row describes the effect?
+ less ADH released, collecting ducts less permeable, a large volume of dilute urine
- more ADH released, collecting ducts more permeable, a large volume of dilute urine
- less ADH released, collecting ducts more permeable, a small volume of concentrated urine
- more ADH released, collecting ducts less permeable, a small volume of concentrated urine
> A rise in blood water potential reduces ADH release, so fewer aquaporins are in the collecting duct membranes and little water is reabsorbed.
? In which part of the kidney are the glomeruli and the proximal convoluted tubules found?
+ the cortex
- the medulla
- the renal pelvis
- the ureter
> Bowman's capsules, PCTs and DCTs are in the cortex. The loops of Henle and collecting ducts run into the medulla.
? Which is an example of negative feedback?
+ a rise in body temperature causes sweating, which lowers the temperature
- a fall in body temperature causes more heat to be released, so the temperature falls further
- a rise in blood water potential causes more ADH to be released
- a rise in urea concentration causes the liver to make more ammonia
> In negative feedback the response reverses the change. A rise in blood water potential would reduce, not increase, ADH release.
:::

:::checklist What you can now do
- [ ] I can explain what is meant by homeostasis and why it is important in mammals.
- [ ] I can explain the control loop of stimulus, receptor, coordination system, effector and response, and negative feedback, using temperature as an example.
- [ ] I can state that urea is produced in the liver from the deamination of excess amino acids.
- [ ] I can describe the structure of the kidney: fibrous capsule, cortex, medulla, renal pelvis, ureter, renal artery and renal vein.
- [ ] I can identify the parts of a nephron and its blood vessels in diagrams and micrographs.
- [ ] I can describe and explain how glomerular filtrate is formed by ultrafiltration and how useful substances are reabsorbed in the proximal convoluted tubule.
- [ ] I can relate the structure of the Bowman's capsule and the proximal convoluted tubule to their functions.
- [ ] I can describe the roles of the hypothalamus, the posterior pituitary gland, ADH, aquaporins and the collecting ducts in osmoregulation.
:::

:::recap
- Homeostasis keeps the internal environment (temperature, water potential, glucose, pH) within narrow limits, so that enzymes work and cells keep their volume and their supply of glucose.
- Control loop: stimulus, receptor, coordination system (nervous or endocrine), effector (muscle or gland), response. Negative feedback: the response reverses the change.
- Urea is made in the liver from the amino group removed by deamination of excess amino acids; it is carried in the plasma to the kidney.
- Kidney: fibrous capsule, cortex, medulla, renal pelvis, ureter, renal artery and vein. Nephron: Bowman's capsule with glomerulus, PCT, loop of Henle, DCT, collecting duct.
- Ultrafiltration: afferent arteriole wider than efferent, so high hydrostatic pressure. The filter is the capillary pores, the basement membrane and the podocyte slits. Water, glucose, amino acids, urea and ions pass; cells and proteins stay.
- Selective reabsorption in the PCT: microvilli, many mitochondria, sodium–potassium pumps in the basal membrane, cotransport of glucose with sodium ions, facilitated diffusion out, water by osmosis. All glucose is normally reabsorbed.
- Osmoregulation: osmoreceptors in the hypothalamus; ADH made there and released from the posterior pituitary; ADH binds to receptors on collecting duct cells; vesicles with aquaporins fuse with the membrane; more water is reabsorbed and a small volume of concentrated urine is made. The reverse when blood water potential rises.
:::

:::links
- read: [CAIE A Level Biology: homeostasis notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/homeostasis/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Homeostasis (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/14-homeostasis/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of the kidney and osmoregulation
- read: [Osmotic regulation and excretion](https://openstax.org/books/biology-2e/pages/41-introduction) · OpenStax Biology 2e · free university textbook chapter on the kidney, beyond the syllabus in places
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find the kidney and ADH questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Blood glucose, cell signalling and biosensors](#bio.glucose) shows how the hormones insulin and glucagon control the blood glucose concentration.
