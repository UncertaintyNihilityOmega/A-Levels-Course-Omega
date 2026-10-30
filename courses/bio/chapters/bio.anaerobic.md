@chapter bio.anaerobic
@title Anaerobic respiration and investigating respiration
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 3–4 hours
@summary When oxygen runs short, cells can still make a little ATP by glycolysis if they find a way to regenerate NAD. You will learn lactate fermentation in mammals and ethanol fermentation in yeast, how rice survives with its roots in water, and how to investigate the rate of respiration with redox indicators (methylene blue and DCPIP) and with a respirometer, including the calculations and the planning questions that go with them.

:::why
Your muscles keep working in a sprint even when your blood cannot bring oxygen fast enough, bread rises and beer is made because yeast respires without oxygen, and rice feeds half the world while growing in flooded fields where most crops die. All three depend on one idea: a cell that cannot use oxygen must still regenerate NAD. This chapter also covers two practical methods that appear in Paper 4 and in the planning paper, Paper 5.
:::

**Before you start**, you should know the stages of aerobic respiration, especially the role of NAD and of oxygen as the final electron acceptor, from [Aerobic respiration](#bio.respiration), the respirometer from [Energy, ATP and respiratory quotient](#bio.energy), and rate calculated as \(1/t\) from [Enzymes](#bio.enzymes).

:::try Warm-up
Q: What is the net gain of ATP in glycolysis, and where does glycolysis take place? (from [Aerobic respiration](#bio.respiration))
A: A net gain of 2 ATP per glucose (2 used, 4 made). It takes place in the cytoplasm.
Q: What happens to the electron transport chain when there is no oxygen? (from [Aerobic respiration](#bio.respiration))
A: Oxygen cannot accept electrons at the end of the chain, so the chain stops. Reduced NAD cannot give up its hydrogen, so no NAD is regenerated.
Q: An amylase reaction reached its end point in 200 s. Give the rate of reaction. (from [Enzymes](#bio.enzymes))
A: Rate \(= 1/t = 1/200 = 5.0 \times 10^{-3}\,\mathrm{s^{-1}}\).
:::

## Respiration without oxygen

In glycolysis, NAD takes hydrogen from triose phosphate, so every molecule of glucose needs two NAD molecules. A cell has only a small supply of NAD, and it is normally used again because reduced NAD gives up its hydrogen to the electron transport chain. **Without oxygen the chain stops**, reduced NAD cannot be reoxidised and NAD runs out. The link reaction and the Krebs cycle stop too. Glycolysis would then stop and the cell would make no ATP at all.

Some cells avoid this. They pass the hydrogen from reduced NAD on to a molecule made from pyruvate. This regenerates NAD, so glycolysis can carry on and make its net 2 ATP per glucose.

:::def Anaerobic respiration
The release of energy from organic molecules, such as glucose, without using oxygen. The substrate is not completely oxidised, ATP is made only by glycolysis (a net gain of 2 per glucose) and the reaction that follows it regenerates NAD.
:::

:::def Fermentation
The pathway after glycolysis in anaerobic respiration in which pyruvate, or a molecule made from it, is reduced using reduced NAD. This regenerates NAD, which glycolysis needs. It is called lactate fermentation when lactate is made and ethanol fermentation when ethanol is made.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 588" role="img" aria-label="Two fermentation pathways, one above the other. Both begin with glucose, which glycolysis converts to pyruvate with three carbons, making a net 2 ATP and reduced NAD. Top, in mammals: lactate dehydrogenase uses reduced NAD to reduce pyruvate to lactate with three carbons, regenerating NAD, and no carbon dioxide is released. Bottom, in yeast: pyruvate loses carbon dioxide to give ethanal with two carbons, and alcohol dehydrogenase uses reduced NAD to reduce ethanal to ethanol, regenerating NAD. In both, a return arrow takes the regenerated NAD back to glycolysis."><text class="tl tb" x="10" y="16">Lactate fermentation (mammals)</text><rect class="f1 s-acc sw2" x="145" y="28" width="110" height="24"/><text class="tl" x="200" y="45" text-anchor="middle">glucose (6C)</text><path class="c1 sw2" d="M200 52L200 64" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="115" y="66" width="170" height="42"/><text class="tl tb" x="200" y="84.5" text-anchor="middle">Glycolysis</text><text class="tl tb" x="200" y="99.5" text-anchor="middle">net 2 ATP</text><path class="c1 sw2" d="M200 108L200 120" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="145" y="122" width="110" height="24"/><text class="tl" x="200" y="139" text-anchor="middle">pyruvate (3C)</text><path class="c1 sw2" d="M200 146L200 208" marker-end="url(#ah)"/><text class="tl" x="212" y="168">reduced NAD → NAD</text><text class="tl" x="212" y="182">lactate</text><text class="tl" x="212" y="196">dehydrogenase</text><rect class="f1 s-acc sw2" x="145" y="210" width="110" height="24"/><text class="tl" x="200" y="227" text-anchor="middle">lactate (3C)</text><path class="c3 sw2" d="M194 164L24 164L24 87L111 87" marker-end="url(#ah)"/><text class="tl" x="32" y="114">NAD</text><text class="tl" x="32" y="128">regenerated</text><text class="tl" x="200" y="258" text-anchor="middle">no CO₂ is released</text><text class="tl tb" x="10" y="296">Ethanol fermentation (yeast)</text><rect class="f1 s-acc sw2" x="145" y="308" width="110" height="24"/><text class="tl" x="200" y="325" text-anchor="middle">glucose (6C)</text><path class="c1 sw2" d="M200 332L200 344" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="115" y="346" width="170" height="42"/><text class="tl tb" x="200" y="364.5" text-anchor="middle">Glycolysis</text><text class="tl tb" x="200" y="379.5" text-anchor="middle">net 2 ATP</text><path class="c1 sw2" d="M200 388L200 400" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="145" y="402" width="110" height="24"/><text class="tl" x="200" y="419" text-anchor="middle">pyruvate (3C)</text><path class="c1 sw2" d="M200 426L200 460" marker-end="url(#ah)"/><text class="tl" x="212" y="447">CO₂ released</text><rect class="f1 s-acc sw2" x="145" y="462" width="110" height="24"/><text class="tl" x="200" y="479" text-anchor="middle">ethanal (2C)</text><path class="c1 sw2" d="M200 486L200 550" marker-end="url(#ah)"/><text class="tl" x="212" y="508">reduced NAD → NAD</text><text class="tl" x="212" y="522">alcohol</text><text class="tl" x="212" y="536">dehydrogenase</text><rect class="f1 s-acc sw2" x="145" y="552" width="110" height="24"/><text class="tl" x="200" y="569" text-anchor="middle">ethanol (2C)</text><path class="c3 sw2" d="M194 516L24 516L24 367L111 367" marker-end="url(#ah)"/><text class="tl" x="32" y="394">NAD</text><text class="tl" x="32" y="408">regenerated</text></svg><figcaption>Lactate fermentation and ethanol fermentation. In both, reducing a molecule made from pyruvate regenerates NAD, so glycolysis can continue and make its net 2 ATP without oxygen.</figcaption></figure>
:::

## Lactate fermentation in mammals

In muscle cells during hard exercise, oxygen is used faster than the blood can deliver it. Glycolysis carries on, and the pyruvate it makes is not sent to the mitochondria. Instead it is reduced to lactate:

\[\mathrm{pyruvate + reduced\ NAD \rightarrow lactate + NAD}\]

The reaction is catalysed by the enzyme **lactate dehydrogenase**. The reduced NAD from glycolysis gives its hydrogen to pyruvate, so NAD is regenerated and glycolysis can continue to make 2 ATP per glucose. The reaction is a reduction of a 3C molecule to another 3C molecule, so **no carbon dioxide is released**.

:::warn Lactate fermentation makes no carbon dioxide
Pyruvate (3C) is converted to lactate (3C) and nothing is removed. If you write that lactate fermentation releases CO₂, you will lose the mark. Also write **lactate**, not "lactic acid", and do not use it for yeast.
:::

Lactate does harm if it builds up, because it and the hydrogen ions that go with it lower the pH and contribute to muscle fatigue. So lactate is removed:

- It diffuses out of the muscle cells into the blood and is carried to the liver.
- In the liver, some lactate is oxidised back to pyruvate, which is respired aerobically in the mitochondria, and some is converted to glucose, which can be stored as glycogen.
- Both need oxygen (and the second needs ATP), so after hard exercise a person goes on breathing deeply and the heart goes on beating fast. The extra oxygen is the **oxygen debt**.

:::def Oxygen debt
The extra oxygen taken in after vigorous exercise, over and above the resting rate, which is used to remove the lactate that built up: to oxidise it to pyruvate (and respire it aerobically) or to convert it to glucose in the liver.
:::

:::eg Real context, a sprinter: the table shows the lactate concentration in the blood of a sprinter and the rate of oxygen uptake during recovery after a 400 m race. The resting oxygen uptake of the runner was 0.3 dm³ min⁻¹. Describe the data and explain the changes. (The data are invented, to show a typical pattern.)
| time after race / min | blood lactate / mmol dm⁻³ | oxygen uptake / dm³ min⁻¹ |
|---|---|---|
| 0 | 12.0 | 3.0 |
| 5 | 8.0 | 1.6 |
| 10 | 5.0 | 0.9 |
| 20 | 2.5 | 0.5 |
| 30 | 1.4 | 0.35 |

**Describe.** Blood lactate falls from 12.0 mmol dm⁻³ at the end of the race to 1.4 mmol dm⁻³ after 30 minutes. The fall is fastest at first: \((12.0 - 5.0) \div 10 = 0.70\,\mathrm{mmol\,dm^{-3}\,min^{-1}}\) in the first 10 minutes but only \((5.0 - 1.4) \div 20 = 0.18\,\mathrm{mmol\,dm^{-3}\,min^{-1}}\) in the next 20 minutes. [B1]

Oxygen uptake falls from 3.0 to 0.35 dm³ min⁻¹ but is still above the resting value of 0.3 dm³ min⁻¹ after 30 minutes. [B1]

**Explain.** During the race, oxygen could not be supplied fast enough, so the muscle cells made ATP by glycolysis and reduced pyruvate to lactate, regenerating NAD. The lactate diffused into the blood. [B1]

After the race, the extra oxygen taken in (the oxygen debt) is used to oxidise lactate to pyruvate in the liver and muscle, which is then respired aerobically, or to convert lactate to glucose. [B1]

As the lactate is removed, its concentration and the oxygen uptake fall together back towards the resting values. [B1]

The fall in lactate is fastest at first because the concentration is highest; the oxygen uptake stays above resting until the lactate is cleared.
:::

## Ethanol fermentation in yeast

Yeast is a single-celled fungus that respires aerobically when it has oxygen and carries out **ethanol fermentation** when it does not. In plants, ethanol fermentation also happens in roots in waterlogged soil. After glycolysis, the pyruvate is converted in two steps:

1. Pyruvate (3C) is **decarboxylated**: a carbon atom is removed as **carbon dioxide**, leaving **ethanal** (2C).
2. Ethanal is **reduced** to **ethanol** (2C), using hydrogen from reduced NAD. This is catalysed by **alcohol dehydrogenase**, and it regenerates NAD.

\[\mathrm{pyruvate \rightarrow ethanal + CO_2}\]

\[\mathrm{ethanal + reduced\ NAD \rightarrow ethanol + NAD}\]

The carbon dioxide is lost, so unlike lactate fermentation, ethanol fermentation **cannot be reversed**: ethanol is not converted back to pyruvate in the cell. The ethanol is a waste product, and it is toxic to most cells at high concentrations, though yeast and rice roots tolerate more than most. In bread making, the carbon dioxide makes the dough rise and the ethanol evaporates when the bread is baked. In brewing, the ethanol is the product.

### Comparing the two pathways

| | Lactate fermentation | Ethanol fermentation |
|---|---|---|
| Organisms | mammalian muscle (and some bacteria) | yeast, and plant roots in waterlogged soil |
| Pyruvate is converted to | lactate (3C) in one step | ethanal (2C), then ethanol (2C) |
| Enzyme that uses reduced NAD | lactate dehydrogenase | alcohol dehydrogenase |
| Carbon dioxide released? | **no** | **yes**, when ethanal is made |
| Reaction reversible? | yes: lactate can be converted back to pyruvate | no: carbon dioxide is lost |
| NAD regenerated? | yes | yes |
| Net ATP per glucose | 2 (from glycolysis) | 2 (from glycolysis) |

:::eg Compare lactate fermentation in mammalian muscle with ethanol fermentation in yeast.
Give similarities and differences, with at least one of each.

Both start with glycolysis, which makes a net gain of 2 ATP per glucose and reduces NAD. [B1]

In both, a molecule made from pyruvate is reduced using reduced NAD, which regenerates NAD so glycolysis can continue. [B1]

In lactate fermentation, pyruvate is reduced directly to lactate (by lactate dehydrogenase) and no carbon dioxide is released; in ethanol fermentation, pyruvate is first decarboxylated to ethanal, releasing carbon dioxide, and ethanal is then reduced to ethanol (by alcohol dehydrogenase). [B1]

Lactate can be converted back to pyruvate (the reaction is reversible), but ethanol fermentation is not reversible because the carbon dioxide is lost. [B1]

(Also credit: the end products are lactate (3C) and ethanol (2C); lactate is made in mammals and ethanol in yeast and plant roots.)

A weaker answer says "yeast makes lactic acid and humans make alcohol", which reverses the organisms and the products, so it scores nothing.
:::

:::warn Do not swap the organisms
Mammals make **lactate** and release no carbon dioxide. Yeast makes **ethanol and carbon dioxide**. Plant roots in waterlogged soil make ethanol too. "Lactic acid in yeast" and "carbon dioxide in lactate fermentation" are the two most common lost marks in this topic.
:::

:::warn "No ATP is made without oxygen"
Wrong: glycolysis still makes a **net 2 ATP** per glucose by substrate-linked phosphorylation. What is lost is oxidative phosphorylation, the stage that makes most of the ATP. Anaerobic respiration releases only a small share of the energy in glucose: most of it is still in the lactate or the ethanol.
:::

## How rice grows with its roots in water

Rice is grown in flooded paddy fields. Water-logged soil holds almost no oxygen, because oxygen diffuses thousands of times more slowly through water than through air and the microorganisms in the soil use up what there is. The roots of most crop plants die in these conditions, because they need oxygen for aerobic respiration to make the ATP for active transport and growth. Rice has three adaptations.

:::html
<figure class="fig small"><svg viewBox="0 0 340 344" role="img" aria-label="A rice plant growing in flooded soil. The stem grows fast so the leaves stay above the water level. The stem and root contain aerenchyma, which are air spaces, and an arrow shows oxygen diffusing down through them from the leaves to the roots. The roots in the waterlogged soil carry out ethanol fermentation."><rect class="fm s-acc sw2" x="10" y="140" width="320" height="100"/><rect class="f1 s-acc sw2" x="10" y="240" width="320" height="70"/><rect class="f1 s-acc sw2" x="146" y="40" width="48" height="256"/><path class="f2 s-acc2 sw2" d="M146 60L40 38L146 50Z"/><path class="f2 s-acc2 sw2" d="M194 60L300 38L194 50Z"/><path class="ln thick" d="M146 262L90 298"/><path class="ln thick" d="M194 262L250 298"/><path class="fp ln" d="M168 80L167.9 81.3L167.8 82.6L167.5 83.8L167.2 85L166.8 86.1L166.2 87.1L165.7 87.9L165 88.7L164.3 89.2L163.6 89.7L162.8 89.9L162 90L161.2 89.9L160.4 89.7L159.7 89.2L159 88.7L158.3 87.9L157.8 87.1L157.2 86.1L156.8 85L156.5 83.8L156.2 82.6L156.1 81.3L156 80L156.1 78.7L156.2 77.4L156.5 76.2L156.8 75L157.2 73.9L157.8 72.9L158.3 72.1L159 71.3L159.7 70.8L160.4 70.3L161.2 70.1L162 70L162.8 70.1L163.6 70.3L164.3 70.8L165 71.3L165.7 72.1L166.2 72.9L166.8 73.9L167.2 75L167.5 76.2L167.8 77.4L167.9 78.7Z"/><path class="fp ln" d="M168 106L167.9 107.3L167.8 108.6L167.5 109.8L167.2 111L166.8 112.1L166.2 113.1L165.7 113.9L165 114.7L164.3 115.2L163.6 115.7L162.8 115.9L162 116L161.2 115.9L160.4 115.7L159.7 115.2L159 114.7L158.3 113.9L157.8 113.1L157.2 112.1L156.8 111L156.5 109.8L156.2 108.6L156.1 107.3L156 106L156.1 104.7L156.2 103.4L156.5 102.2L156.8 101L157.2 99.9L157.8 98.9L158.3 98.1L159 97.3L159.7 96.8L160.4 96.3L161.2 96.1L162 96L162.8 96.1L163.6 96.3L164.3 96.8L165 97.3L165.7 98.1L166.2 98.9L166.8 99.9L167.2 101L167.5 102.2L167.8 103.4L167.9 104.7Z"/><path class="fp ln" d="M168 170L167.9 171.3L167.8 172.6L167.5 173.8L167.2 175L166.8 176.1L166.2 177.1L165.7 177.9L165 178.7L164.3 179.2L163.6 179.7L162.8 179.9L162 180L161.2 179.9L160.4 179.7L159.7 179.2L159 178.7L158.3 177.9L157.8 177.1L157.2 176.1L156.8 175L156.5 173.8L156.2 172.6L156.1 171.3L156 170L156.1 168.7L156.2 167.4L156.5 166.2L156.8 165L157.2 163.9L157.8 162.9L158.3 162.1L159 161.3L159.7 160.8L160.4 160.3L161.2 160.1L162 160L162.8 160.1L163.6 160.3L164.3 160.8L165 161.3L165.7 162.1L166.2 162.9L166.8 163.9L167.2 165L167.5 166.2L167.8 167.4L167.9 168.7Z"/><path class="fp ln" d="M168 196L167.9 197.3L167.8 198.6L167.5 199.8L167.2 201L166.8 202.1L166.2 203.1L165.7 203.9L165 204.7L164.3 205.2L163.6 205.7L162.8 205.9L162 206L161.2 205.9L160.4 205.7L159.7 205.2L159 204.7L158.3 203.9L157.8 203.1L157.2 202.1L156.8 201L156.5 199.8L156.2 198.6L156.1 197.3L156 196L156.1 194.7L156.2 193.4L156.5 192.2L156.8 191L157.2 189.9L157.8 188.9L158.3 188.1L159 187.3L159.7 186.8L160.4 186.3L161.2 186.1L162 186L162.8 186.1L163.6 186.3L164.3 186.8L165 187.3L165.7 188.1L166.2 188.9L166.8 189.9L167.2 191L167.5 192.2L167.8 193.4L167.9 194.7Z"/><path class="fp ln" d="M168 222L167.9 223.3L167.8 224.6L167.5 225.8L167.2 227L166.8 228.1L166.2 229.1L165.7 229.9L165 230.7L164.3 231.2L163.6 231.7L162.8 231.9L162 232L161.2 231.9L160.4 231.7L159.7 231.2L159 230.7L158.3 229.9L157.8 229.1L157.2 228.1L156.8 227L156.5 225.8L156.2 224.6L156.1 223.3L156 222L156.1 220.7L156.2 219.4L156.5 218.2L156.8 217L157.2 215.9L157.8 214.9L158.3 214.1L159 213.3L159.7 212.8L160.4 212.3L161.2 212.1L162 212L162.8 212.1L163.6 212.3L164.3 212.8L165 213.3L165.7 214.1L166.2 214.9L166.8 215.9L167.2 217L167.5 218.2L167.8 219.4L167.9 220.7Z"/><path class="fp ln" d="M168 248L167.9 249.3L167.8 250.6L167.5 251.8L167.2 253L166.8 254.1L166.2 255.1L165.7 255.9L165 256.7L164.3 257.2L163.6 257.7L162.8 257.9L162 258L161.2 257.9L160.4 257.7L159.7 257.2L159 256.7L158.3 255.9L157.8 255.1L157.2 254.1L156.8 253L156.5 251.8L156.2 250.6L156.1 249.3L156 248L156.1 246.7L156.2 245.4L156.5 244.2L156.8 243L157.2 241.9L157.8 240.9L158.3 240.1L159 239.3L159.7 238.8L160.4 238.3L161.2 238.1L162 238L162.8 238.1L163.6 238.3L164.3 238.8L165 239.3L165.7 240.1L166.2 240.9L166.8 241.9L167.2 243L167.5 244.2L167.8 245.4L167.9 246.7Z"/><path class="fp ln" d="M168 274L167.9 275.3L167.8 276.6L167.5 277.8L167.2 279L166.8 280.1L166.2 281.1L165.7 281.9L165 282.7L164.3 283.2L163.6 283.7L162.8 283.9L162 284L161.2 283.9L160.4 283.7L159.7 283.2L159 282.7L158.3 281.9L157.8 281.1L157.2 280.1L156.8 279L156.5 277.8L156.2 276.6L156.1 275.3L156 274L156.1 272.7L156.2 271.4L156.5 270.2L156.8 269L157.2 267.9L157.8 266.9L158.3 266.1L159 265.3L159.7 264.8L160.4 264.3L161.2 264.1L162 264L162.8 264.1L163.6 264.3L164.3 264.8L165 265.3L165.7 266.1L166.2 266.9L166.8 267.9L167.2 269L167.5 270.2L167.8 271.4L167.9 272.7Z"/><path class="c1 sw2" d="M182 70L182 250" marker-end="url(#ah)"/><text class="tl" x="196" y="30">leaves above water</text><path class="ln-m thin" d="M262 34L258 42"/><text class="tl" x="140" y="98" text-anchor="end">fast-growing</text><text class="tl" x="140" y="112" text-anchor="end">stem</text><path class="ln-m thin" d="M144 95L147 95"/><text class="tl" x="206" y="104">O₂ diffuses down</text><path class="ln-m thin" d="M204 100L184 102"/><text class="tl" x="206" y="176">aerenchyma:</text><text class="tl" x="206" y="190">air spaces</text><path class="ln-m thin" d="M202 172L169 171"/><text class="tl" x="322" y="122" text-anchor="end">water level</text><path class="ln-m thin" d="M312 127L312 140"/><text class="tl" x="18" y="196">flood</text><text class="tl" x="18" y="212">water</text><text class="tl" x="18" y="272">soil</text><text class="tl" x="170" y="332" text-anchor="middle">roots: ethanol fermentation</text><path class="ln-m thin" d="M170 318L170 297"/></svg><figcaption>How rice is adapted to flooding: leaves held above the water by fast stem growth, aerenchyma that lets oxygen diffuse down to the roots, and ethanol fermentation in roots when oxygen is still short.</figcaption></figure>
:::

1. **Aerenchyma.** The stems and roots contain **aerenchyma**, large air spaces formed when some cells of the cortex die. Oxygen **diffuses down** through the air spaces from the leaves, which are in the air, to the roots in the water, so the roots can carry out some aerobic respiration. The air spaces also have a low resistance to diffusion compared with solid tissue.
2. **Ethanol fermentation in the roots.** When the oxygen supply is still not enough, root cells carry out ethanol fermentation. It regenerates NAD, so glycolysis goes on and makes a net 2 ATP per glucose. The roots can survive and keep making ATP for a time, and the ethanol diffuses out into the surrounding water instead of building up and poisoning the cells.
3. **Faster growth of the stem.** In deep water, the stems grow faster and so keep the leaves above the water level. The leaves can then take in oxygen and carbon dioxide from the air, and photosynthesise, and the aerenchyma stays connected to the air.

:::eg Rice grows well in flooded fields where wheat dies. Explain how rice is adapted to grow with its roots submerged in water, including the role of ethanol fermentation.
A full-mark answer gives five points, from the problem to the adaptations.

Waterlogged soil has little oxygen, because oxygen diffuses slowly through water, so the roots cannot get enough oxygen for aerobic respiration. [B1]

Rice stems and roots contain aerenchyma, air spaces through which oxygen diffuses from the leaves down to the roots. [B1]

When oxygen is still short, the roots carry out ethanol fermentation: pyruvate is decarboxylated to ethanal, which is reduced to ethanol using reduced NAD. [B1]

This regenerates NAD, so glycolysis can continue and make a net 2 ATP per glucose, enough for the root cells to stay alive. [B1]

The stems grow faster, which keeps the leaves above the water so that they can take in oxygen from the air. [B1]

(Also credit: ethanol diffuses out of the roots; rice root cells tolerate more ethanol than the roots of crop plants such as wheat.)

A weaker answer says "rice does not need oxygen". Rice roots do respire, aerobically when they can and anaerobically when they cannot, so the answer scores nothing.
:::

## Investigating respiration

You need to be able to describe and carry out two kinds of investigation of the rate of respiration: using **redox indicators** with yeast, and using a **respirometer**.

### Redox indicators: methylene blue and DCPIP

During respiration, enzymes called dehydrogenases remove hydrogen from the substrate, and the hydrogen is normally passed to NAD. A **redox indicator** is a dye that changes colour when it is reduced. If it is added to a suspension of yeast, it takes the hydrogen (electrons) in place of NAD. Both dyes are **blue when oxidised and colourless when reduced**. The faster the yeast respires, the faster the dye is reduced, so the **time to decolourise** is a measure of the rate. A short time means a fast rate.

\[\text{rate of respiration} \propto \frac{1}{\text{time to decolourise}}\]

:::lab Effect of temperature or glucose concentration on the rate of respiration of yeast
**Aim**: find how temperature (or the concentration of glucose) affects the rate of respiration of yeast, using methylene blue (or DCPIP) as the redox indicator.

:::steps
1. Choose at least five values of the independent variable: for example 20, 30, 40, 50 and 60 °C, or 0, 2, 4, 6, 8 and 10% glucose.
2. Put the same volume of yeast suspension and of glucose solution in each tube. For temperature, stand the tubes in water baths at the chosen temperatures for 5 minutes, with the indicator in a separate tube in the same bath.
3. Add the same volume of methylene blue (or DCPIP) to each tube, mix gently, and start the stopwatch at once. If the method uses it, add a thin layer of liquid paraffin on top to keep oxygen out.
4. Record the time for the blue colour to disappear, compared with a colour standard such as a tube of the mixture with no dye. Stop at a set time (for example 15 minutes) and record "more than 900 s" if there is no change.
5. Repeat three times at each value and calculate the mean time. Calculate the rate as \(1/t\), in \(\mathrm{s^{-1}}\). Plot rate (y axis) against the independent variable.
:::

**Variables**: the independent variable is the temperature (or the glucose concentration); the dependent variable is the time to decolourise (so the rate, \(1/t\)). Standardise the volume and concentration of the yeast suspension, the volume and concentration of the glucose solution (for the temperature investigation), the volume and concentration of the indicator, the pH (a buffer), the temperature (for the glucose investigation) and the way the tubes are mixed.

**Control**: boiled (dead) yeast, or a tube with no glucose. The dye should stay blue, which shows that the colour change is caused by respiration in living yeast with a substrate.

**Typical results**: the rate rises with temperature up to an optimum, and falls at high temperatures; the rate rises with glucose concentration and then levels off.

**Sources of error**: judging the end point by eye is subjective; shaking or opening the tube lets oxygen in, which turns the colourless dye blue again, so mixing must be the same in every tube; the yeast settles; the temperature drifts. Improvements: use a colorimeter, with a filter for the dye, and take the time for the absorbance to fall to a set value; use a colour standard; use a layer of liquid paraffin; check the temperature in the tube; repeat.

**Safety**: methylene blue and DCPIP stain skin and clothing, so wear gloves and eye protection; use hot water carefully; wash hands after handling yeast. Risk: low.
:::

:::warn Which way does the colour change?
The dyes are **blue when oxidised** and **colourless when reduced**. A tube that goes colourless is the one where respiration is happening, so "turns blue when respiring" is the wrong way round. Also, rate is **1/time**: the tube that decolourises first has the highest rate.
:::

:::eg Methylene blue was added to yeast suspensions with glucose at five temperatures. The table shows the time for the blue colour to disappear. Calculate the rate of respiration at each temperature, plot the rates, and describe and explain the effect of temperature.
| temperature / °C | time to decolourise / s |
|---|---|
| 20 | 600 |
| 30 | 240 |
| 40 | 120 |
| 50 | 300 |
| 60 | no change in 900 s |

**Step 1: rate \(= 1/t\)**, because a shorter time means a faster rate.

\[\begin{aligned} \text{20 °C: rate} &= \frac{1}{600} = 1.67 \times 10^{-3}\,\mathrm{s^{-1}} \\ \text{40 °C: rate} &= \frac{1}{120} = 8.33 \times 10^{-3}\,\mathrm{s^{-1}} \end{aligned}\] [M1] [A1]

The others are \(4.17 \times 10^{-3}\) at 30 °C and \(3.33 \times 10^{-3}\,\mathrm{s^{-1}}\) at 50 °C. At 60 °C there was no change in 900 s, so the rate is about 0.

**Step 2: describe.** As the temperature rises from 20 °C to 40 °C, the rate increases from \(1.67 \times 10^{-3}\) to \(8.33 \times 10^{-3}\,\mathrm{s^{-1}}\), five times as fast. [B1] The highest rate measured is at 40 °C, and above it the rate falls, to \(3.33 \times 10^{-3}\,\mathrm{s^{-1}}\) at 50 °C and to about 0 at 60 °C. [B1]

**Step 3: explain.** Up to 40 °C, the enzymes (dehydrogenases) and substrates have more kinetic energy, so they collide more often and more enzyme–substrate complexes form per second. [B1] Above 40 °C, hydrogen and ionic bonds in the enzymes break, the active sites change shape and the enzymes are denatured, so respiration slows and then stops. [B1]
:::

Here are the five rates from the example plotted against temperature, so you can see the peak at 40 °C.

:::plot Rate of respiration of yeast at five temperatures, in units of 10⁻³ s⁻¹ (the rate is 1/t). The highest rate is at 40 °C.
--x 0 90 --y 0 12 --xlabel "temperature / °C" --ylabel "rate / 10⁻³ s⁻¹" --pt "20,1.67,1.67@se" --pt "30,4.17,4.17@nw" --pt "40,8.33,8.33@ne" --pt "50,3.33,3.33@ne" --pt "60,0,0@nw" --legend tr --alt "Five points: rate 1.67 at 20 degrees, 4.17 at 30, 8.33 at 40, 3.33 at 50 and 0 at 60 degrees Celsius, in units of 10 to the power minus 3 per second. The rate rises to a peak at 40 degrees and then falls to zero."
:::

:::eg Spot the error: describe the effect of temperature on the rate of respiration of yeast, using the table in the example above. [3]
A student wrote this answer.

Line 1: The time to decolourise falls from 600 s at 20 °C to 120 s at 40 °C.
Line 2: So the rate of respiration is lowest at 40 °C, because the time is shortest.
Line 3: At 50 °C the time rises to 300 s, so the rate of respiration falls.

Line 1 is correct [B1]. **Line 2 is wrong: rate is 1/time, so the shortest time is the fastest rate. The rate is highest at 40 °C. That mark is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "So the rate of respiration is highest at 40 °C, because the time is shortest (rate \(= 1/t\))." With that change the answer scores 3 marks.
:::

### A respirometer and temperature

The simple respirometer from [Energy, ATP and respiratory quotient](#bio.energy) measures the volume of oxygen taken in per unit time, so it can show the effect of temperature on the rate of respiration.

:::lab Effect of temperature on the rate of respiration, with a respirometer
**Aim**: find how temperature affects the rate of oxygen uptake of germinating seeds (or small invertebrates such as blowfly larvae).

:::steps
1. Set up the respirometer as in the previous chapter, with potassium hydroxide solution to absorb the carbon dioxide, so the movement of the drop shows only the oxygen taken in. Prepare a control tube with glass beads.
2. Put the apparatus in a water bath at the first temperature (for example 10 °C). Leave it for 10 minutes with the capillary open, so that the temperature settles.
3. Close the system, put the drop in the capillary and read its position at the start. Read it again after a set time (for example 5 minutes).
4. Calculate the distance moved and, with the radius of the capillary, the volume of oxygen taken in: \(\pi r^2 d\). Divide by the time to give the rate in \(\mathrm{mm^3\,min^{-1}}\).
5. Repeat at 20, 30, 40 and 50 °C with the same mass of the same organisms (and fresh ones if they are stressed), and repeat each temperature three times.
:::

**Variables**: the independent variable is the temperature; the dependent variable is the volume of oxygen taken in per minute. Standardise the mass of the organisms, the volume and concentration of potassium hydroxide, the capillary radius and the time of the reading.

**Control**: the glass beads tube at each temperature, which shows any change in volume that is due to the temperature and not to respiration.

**Typical results**: the rate rises with temperature, up to an optimum, and falls at the highest temperatures as enzymes are denatured (a small organism may also be harmed).

**Sources of error**: the temperature inside the tube differs from the bath; the organisms are stressed by the high temperatures; leaks; the seeds touch the potassium hydroxide. Improvements: allow more time for equilibration, check the temperature in the tube, use fresh organisms at each temperature, and repeat.

**Safety**: potassium hydroxide is corrosive: wear eye protection and keep it away from the organisms. Handle animals gently and return them unharmed.
:::

:::exam Plan the investigation, then evaluate it
Paper 5 and Paper 4 ask you to plan these experiments and to evaluate data from them. Name the independent variable (with a range and at least five values), the dependent variable and how it is measured, the variables you will keep the same (and how), a control (boiled yeast, no glucose, or glass beads), and the number of repeats. For a dye experiment, give the rate as \(1/t\). For a respirometer, say which gas the potassium hydroxide removes, and give \(\pi r^2 d\) for volume. For a "describe" question, quote figures with units; for an "explain" question, give enzyme and kinetic-energy reasons.
:::

## Practice

:::try Start easy, finish at exam standard
Q: Explain why a muscle cell without oxygen must convert pyruvate to lactate.
A: Without oxygen the electron transport chain stops, so reduced NAD cannot be reoxidised. Converting pyruvate to lactate uses reduced NAD and regenerates NAD, so glycolysis can carry on and make ATP.
Q: Name the enzyme that catalyses the conversion of ethanal to ethanol, and state what is formed from reduced NAD.
A: Alcohol dehydrogenase. NAD is regenerated.
Q: Why does lactate fermentation release no carbon dioxide, whereas ethanol fermentation does?
A: Pyruvate (3C) is converted to lactate (3C) with no carbon removed. In ethanol fermentation, pyruvate (3C) is decarboxylated to ethanal (2C), releasing carbon dioxide.
Q: A methylene blue tube lost its blue colour in 320 s. Calculate the rate of respiration.
A: Rate \(= 1/t = 1/320 = 3.13 \times 10^{-3}\,\mathrm{s^{-1}}\).
Q: Blood lactate in a swimmer fell from 9.0 to 3.0 mmol dm⁻³ in 12 minutes. Calculate the mean rate of fall.
A: \((9.0 - 3.0) \div 12 = 0.50\,\mathrm{mmol\,dm^{-3}\,min^{-1}}\).
Q: In the methylene blue method, why is a tube with boiled yeast included?
A: It is a control. The dye should stay blue, which shows that decolourisation is caused by respiration of living yeast, not by anything else in the tube.
Q: Why does shaking a tube that has gone colourless turn it blue again?
A: Shaking mixes in oxygen from the air, which oxidises the reduced dye back to its blue form.
Q: Dough rises when yeast is added, and the baked bread does not taste of alcohol. Explain both.
A: The yeast respires anaerobically in the dough and releases carbon dioxide, which makes bubbles. The ethanol that is also made evaporates during baking.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the products of lactate fermentation and of ethanol fermentation (other than ATP), and name one organism in which each takes place.
A: Lactate fermentation: lactate, in mammalian muscle. [B1]
Ethanol fermentation: ethanol and carbon dioxide, [B1] in yeast (or plant roots in waterlogged soil). [B1]
Q: [4 marks] ★★ Outline lactate fermentation in a mammalian muscle cell.
H: Say what is reduced, what does the reducing, and what is regenerated.
A: Pyruvate from glycolysis is reduced to lactate. [B1]
The reaction is catalysed by lactate dehydrogenase, using reduced NAD. [B1]
This regenerates NAD. [B1]
So glycolysis can continue to make a net 2 ATP per glucose when there is no oxygen. [B1]
Q: [4 marks] ★★ A student used methylene blue to compare the rate of respiration of yeast at different temperatures, timing the loss of colour by eye. (a) Suggest why a thin layer of liquid paraffin may be added to each tube. (b) Suggest a control and explain why it is needed. (c) Suggest one way to make the end point more accurate.
H: What does oxygen from the air do to the reduced dye?
A: (a) It stops oxygen dissolving in the mixture, which would oxidise the dye and turn it blue again. [B1]
(b) Boiled yeast (or no glucose) at each temperature; it shows that the colour change is caused by respiration of living yeast. [B1] [B1]
(c) Use a colorimeter, or compare with a colour standard, to find when the colour has gone. [B1]
Q: [6 marks] ★★ The table shows the time for methylene blue to be decolourised by yeast in glucose solutions of different concentrations at 35 °C.

| glucose / % | time / s |
|---|---|
| 0 | no change in 900 |
| 2 | 520 |
| 4 | 310 |
| 6 | 200 |
| 8 | 160 |
| 10 | 155 |

(a) Calculate the rate of respiration at 4% and at 10% glucose, in standard form. (b) Describe the effect of glucose concentration on the rate. (c) Explain the shape of the graph between 8% and 10% glucose.
H: Rate \(= 1/t\).
H: For (c), which factor is limiting when the rate stops rising?
A: (a) Rate \(= 1/t\) [M1]; at 4%: \(1/310 = 3.23 \times 10^{-3}\,\mathrm{s^{-1}}\) [A1]; at 10%: \(1/155 = 6.45 \times 10^{-3}\,\mathrm{s^{-1}}\) [A1]
(b) The rate increases as the glucose concentration increases, from 0 at 0% to \(6.25 \times 10^{-3}\,\mathrm{s^{-1}}\) at 8%, and then hardly changes (\(6.45 \times 10^{-3}\,\mathrm{s^{-1}}\) at 10%). [B1]
(c) Between 8% and 10% glucose the enzymes (the dehydrogenases and the other enzymes of respiration) are saturated with substrate. [B1]
So glucose is no longer limiting: the number of enzyme molecules, or the yeast, limits the rate, so more glucose does not raise it. [B1]
Q: [5 marks] ★★ Germinating peas were placed in a respirometer with potassium hydroxide solution. The capillary had a radius of 0.50 mm. The distance moved by the drop in 5 minutes at five temperatures was: 10 °C, 6 mm; 20 °C, 14 mm; 30 °C, 28 mm; 40 °C, 46 mm; 50 °C, 23 mm. (a) Calculate the rate of oxygen uptake at 30 °C in mm³ min⁻¹. (b) Describe the effect of temperature on the rate. (c) Suggest why the rate falls at 50 °C.
H: Volume \(= \pi r^2 d\); then divide by the time.
A: (a) \(\pi \times 0.50^2 \times 28 \div 5\) [M1] \(= 4.4\,\mathrm{mm^3\,min^{-1}}\) [A1]
(b) The rate increases from 10 °C to 40 °C (from 6 to 46 mm in 5 minutes, or 0.94 to 7.2 mm³ min⁻¹). [B1]
The rate falls at 50 °C, to 23 mm in 5 minutes. [B1]
(c) The enzymes of respiration are denatured at the high temperature (bonds break and the active sites change shape). [B1]
Q: [5 marks] ★★★ A brewer grows yeast in a tank that is bubbled with air for the first day, and then seals the tank for the rest of the process. Explain (a) why the yeast population grows faster while air is bubbled through, and (b) why ethanol is made only after the tank is sealed.
H: Compare the ATP made from each glucose with and without oxygen.
H: What happens to the electron transport chain in a sealed tank?
A: (a) With oxygen, the yeast respires aerobically, so oxidative phosphorylation makes far more ATP from each glucose than the net 2 ATP of glycolysis. [B1]
The ATP supplies the energy for the growth and division of the cells (making proteins, DNA and new cell material), so the population grows faster. [B1]
(b) In the sealed tank there is no oxygen, so the electron transport chain stops and reduced NAD cannot be reoxidised. [B1]
Pyruvate is decarboxylated to ethanal, and ethanal is reduced to ethanol using reduced NAD. [B1]
This regenerates NAD, so glycolysis can continue to make ATP, and ethanol is the waste product. [B1]
Q: [5 marks] ★★★ Seedlings of two varieties of maize were grown in flooded soil. Variety X roots increased their alcohol dehydrogenase activity five times after flooding. Variety Y roots did not change it. Predict which variety survives better, and explain, with reference to NAD.
H: What does alcohol dehydrogenase do with reduced NAD?
A: Variety X survives better. [B1]
In flooded soil, oxygen is short, so the roots must make ATP by glycolysis and ethanol fermentation. [B1]
Alcohol dehydrogenase reduces ethanal to ethanol using reduced NAD, regenerating NAD, so more activity lets glycolysis continue. [B1]
In Y, NAD is not regenerated fast enough, so glycolysis slows and little ATP is made. [B1]
So Y root cells have too little ATP for active transport and growth and die. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Assume that aerobic respiration makes 30 ATP per glucose in yeast (a value supplied here; you do not need to learn it) and that anaerobic respiration makes a net 2 ATP per glucose and 2 ethanol and 2 CO₂. A yeast culture needs 150 mmol of ATP per hour. (a) Calculate the glucose needed per hour (i) aerobically and (ii) anaerobically. (b) Calculate the ethanol made per hour anaerobically. (c) Explain why so much more glucose is needed anaerobically.
H: Glucose needed \(=\) ATP needed \(\div\) ATP made per glucose.
H: For (c), where is most of the ATP made, and what happens to the energy still in ethanol?
A: (a) (i) \(150 \div 30 = 5.0\,\mathrm{mmol}\) [M1] [A1]
(ii) \(150 \div 2 = 75\,\mathrm{mmol}\) [A1]
(b) Ethanol \(= 75 \times 2 = 150\,\mathrm{mmol}\) [A1]
(c) Without oxygen, only glycolysis makes ATP (net 2 per glucose), because oxidative phosphorylation cannot work. [B1]
The glucose is only partly oxidised, so most of its energy is still in the ethanol and is not used to make ATP. [B1]
Q: [5 marks] ★★★ The crucian carp, a fish, can live for months in ponds under ice with almost no oxygen. Its muscle cells make **ethanol** in these conditions, and the ethanol diffuses out through the gills into the water. (a) Suggest what the muscle cells must be able to do that the muscle cells of mammals and of most other fish cannot. (b) Suggest why making ethanol, not lactate, is an advantage in the pond. (c) Predict how the amount of carbon dioxide released by the fish changes.
H: Compare the two pathways in the table: which has an extra step?
H: What happens to lactate that cannot be removed?
A: (a) They can decarboxylate pyruvate to ethanal, and reduce ethanal to ethanol using alcohol dehydrogenase. [B1]
(b) Ethanol is a small molecule that can leave the body through the gills, so it does not accumulate. [B1]
Lactate cannot be removed without oxygen, so it would build up and lower the pH, which would reduce the activity of enzymes and stop the muscles. [B1]
(c) Carbon dioxide is released when ethanal is made, [B1] so the fish releases some carbon dioxide even without oxygen. [B1]
:::

:::quiz
? Which products are made when yeast respires without oxygen?
+ ethanol and carbon dioxide
- lactate and carbon dioxide
- lactate only
- ethanol only
> Yeast decarboxylates pyruvate to ethanal (releasing carbon dioxide) and reduces ethanal to ethanol. Lactate is the product in mammalian muscle, and no carbon dioxide is released there.
? What is the main purpose of the reduction of pyruvate to lactate in muscle?
+ It regenerates NAD so that glycolysis can continue.
- It makes a large amount of ATP.
- It removes carbon dioxide from the muscle.
- It supplies hydrogen to the electron transport chain.
> Glycolysis needs NAD. Reducing pyruvate with reduced NAD regenerates it. Almost no ATP is made in this step, no carbon dioxide is involved, and the electron transport chain is not working without oxygen.
? Which statement about anaerobic respiration in mammals is correct?
+ Glycolysis still makes a net gain of 2 ATP per glucose.
- No ATP is made.
- Carbon dioxide is released when pyruvate is converted to lactate.
- The link reaction and Krebs cycle make the ATP.
> Glycolysis does not need oxygen, so it still makes 2 ATP net. No CO₂ is released in lactate fermentation, and the link reaction and Krebs cycle stop without oxygen.
? A methylene blue tube is decolourised in 150 s. Which expression gives the rate of respiration?
+ \(1/150\,\mathrm{s^{-1}}\)
- \(150\,\mathrm{s}\)
- \(150 \times 60\)
- \(150 \div 2\)
> Rate is the reciprocal of the time to decolourise: \(1/150 = 6.67 \times 10^{-3}\,\mathrm{s^{-1}}\). Using 150 s itself treats time as rate, which is the commonest error.
? Which feature of rice roots allows oxygen to reach them in waterlogged soil?
+ aerenchyma
- a thick Casparian strip
- faster active transport
- larger root hairs
> Aerenchyma are air spaces in the stem and root through which oxygen diffuses from the leaves. The Casparian strip controls the pathway of water, and larger root hairs or faster uptake do not bring in oxygen.
? In a redox indicator experiment with yeast, the dye changes from blue to colourless. What does this show?
+ The dye has been reduced by hydrogen from respiration.
- The dye has been oxidised by oxygen.
- The yeast has stopped respiring.
- The yeast has made lactate.
> The dyes are blue when oxidised and colourless when reduced. They accept the hydrogen released in respiration in place of NAD. Oxygen would turn the dye blue again.
? What is the oxygen debt?
+ the extra oxygen taken in after exercise to remove the lactate that built up
- the oxygen that the muscles lack during exercise
- the oxygen used to make lactate
- the carbon dioxide produced in anaerobic respiration
> The oxygen debt is repaid after hard exercise: extra oxygen is used to oxidise lactate or convert it to glucose. It is not the shortage during exercise, and lactate is not made using oxygen.
? Why is the reaction that converts ethanal to ethanol important to the cell?
+ It uses reduced NAD and regenerates NAD for glycolysis.
- It releases carbon dioxide.
- It makes most of the ATP of the cell.
- It converts ethanol to pyruvate.
> Reducing ethanal to ethanol regenerates NAD. The carbon dioxide comes from the earlier decarboxylation, glycolysis makes the ATP, and the step is not reversible.
:::

:::checklist What you can now do
- [ ] I can outline respiration in anaerobic conditions in mammals (lactate fermentation) and in yeast (ethanol fermentation), and explain how each regenerates NAD.
- [ ] I can compare lactate and ethanol fermentation, including carbon dioxide, reversibility and net ATP.
- [ ] I can explain the oxygen debt after vigorous exercise.
- [ ] I can explain how rice is adapted to grow with its roots submerged in water: aerenchyma, ethanol fermentation in the roots and faster growth of the stems.
- [ ] I can describe and carry out an investigation with methylene blue or DCPIP to find the effects of temperature and substrate concentration on the rate of respiration of yeast, with a control, and calculate the rate as 1/t.
- [ ] I can describe and carry out an investigation with a simple respirometer to find the effect of temperature on the rate of respiration, and calculate the rate in mm³ per minute.
- [ ] I can plan, analyse and evaluate these investigations, naming the variables, controls and sources of error.
:::

:::recap
- Without oxygen, the electron transport chain stops, reduced NAD cannot be reoxidised and glycolysis would stop. Fermentation regenerates NAD so glycolysis continues, making a net 2 ATP per glucose.
- Lactate fermentation (mammals): pyruvate + reduced NAD → lactate + NAD, by lactate dehydrogenase; no CO₂. Lactate goes to the liver and is oxidised to pyruvate or converted to glucose: the oxygen debt.
- Ethanol fermentation (yeast, and plant roots in waterlogged soil): pyruvate → ethanal + CO₂; ethanal + reduced NAD → ethanol + NAD, by alcohol dehydrogenase; not reversible.
- Rice: aerenchyma let oxygen diffuse to roots; ethanol fermentation in roots; faster stem growth keeps leaves above water.
- Redox indicators (methylene blue, DCPIP): blue when oxidised, colourless when reduced by hydrogen from respiration. Rate \(= 1/t\). Controls: boiled yeast or no glucose. Keep oxygen out.
- Respirometer and temperature: volume of oxygen taken in \(= \pi r^2 d\); rate \(=\) volume \(\div\) time; control with glass beads.
- Describe with figures and units; explain with kinetic energy, collisions, denaturation, and the limiting factor.
:::

:::links
- read: [CAIE A Level Biology: energy and respiration notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/energy-and-respiration/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Energy and respiration (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/12-energy-and-respiration/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of fermentation and cellular respiration
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [Cellular respiration](https://openstax.org/books/biology-2e/pages/7-introduction) · OpenStax Biology 2e · free university textbook chapter that includes fermentation, beyond the syllabus in places
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · find planning and evaluation questions on respiration in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Photosynthesis](#bio.photosynthesis) shows how plants capture light energy and use it to make the glucose that respiration releases.
