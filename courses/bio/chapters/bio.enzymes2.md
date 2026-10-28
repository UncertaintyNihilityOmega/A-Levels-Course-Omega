@chapter bio.enzymes2
@title Enzyme kinetics, inhibitors and immobilised enzymes
@level as
@paper CAIE 9700 Papers 1, 2 and 3
@time 3–4 hours
@summary The maximum rate Vmax leads to the Michaelis–Menten constant Km, which compares how readily different enzymes bind their substrates. You will read Vmax and Km from graphs, explain how competitive and non-competitive reversible inhibitors change the rate and the graph, and investigate enzymes immobilised in alginate beads and the advantages of using them.

:::why
Every drug that blocks an enzyme, every pesticide that disables an insect and every cell that switches off a reaction it does not need relies on enzyme inhibition. Industry goes one step further and fixes enzymes in beads so they can be reused to make lactose-free milk or sweeteners. This chapter gives you the graph skills and explanations for these questions, which appear in both structured papers and in the practical paper.
:::

**Before you start**, you need the rate against substrate concentration graph and the meaning of Vmax from [Enzymes](#bio.enzymes). This chapter starts where that one stops. For the glucose test used in one of the experiments, see [Testing for biological molecules](#bio.foodtests).

:::try Warm-up
Q: What is Vmax, and what limits the rate at the plateau of a rate against substrate concentration graph? (from [Enzymes](#bio.enzymes))
A: Vmax is the maximum initial rate of the reaction. At the plateau every active site is occupied, so the number of active sites (enzyme concentration) limits the rate.
Q: Why is the initial rate used to compare experiments? (from [Enzymes](#bio.enzymes))
A: At the start the substrate concentration is known and has not fallen, and no product has built up, so the rates can be compared fairly.
Q: What does it mean to say that an enzyme is specific? (from [Enzymes](#bio.enzymes))
A: Only a substrate with a shape complementary to its active site can bind and form an enzyme–substrate complex.
:::

## Vmax and the Michaelis–Menten constant

With a fixed amount of enzyme, the initial rate rises as the substrate concentration increases, then levels off. At the top, the enzyme is **saturated** and the rate is **Vmax**. That curve is your starting point.

:::plot Initial rate against substrate concentration for an enzyme with Vmax = 80 units. Half of Vmax (40 units) is reached at a substrate concentration of 5 mmol dm⁻³, which is the Km.
--f "80*x/(5+x)" --x 0 50 --y 0 105 --hline 80 --vline 5 --xlabel "substrate concentration / mmol dm⁻³" --ylabel "initial rate / arbitrary units" --label "initial rate" --pt "5,40,Km = 5 (rate = half of Vmax)@se" --pt "42,80,Vmax = 80@n" --legend tr --alt "The rate rises steeply from zero and levels off, approaching a dashed horizontal line at 80 units, which is Vmax. A dashed vertical line at a substrate concentration of 5 meets the curve at a rate of 40, which is half of Vmax."
:::

The curve never quite reaches Vmax: each extra bit of substrate fills a few more of the last empty active sites. So Vmax is the value that the curve **approaches**. How quickly the curve climbs towards it depends on how readily the enzyme binds its substrate. Two enzymes can have the same Vmax and very different curves. Biologists measure that difference with the Michaelis–Menten constant.

:::def Michaelis–Menten constant (Km)
The substrate concentration at which an enzyme-catalysed reaction proceeds at half its maximum rate (half of Vmax). It is used to compare the affinity of different enzymes for their substrates.
:::

:::def Affinity (of an enzyme for its substrate)
How readily the enzyme binds its substrate. An enzyme with a high affinity binds the substrate and forms enzyme–substrate complexes even when the substrate concentration is low.
:::

:::key Reading Vmax and Km from a graph
1. Find **Vmax**: the rate the curve levels off towards (draw a dashed horizontal line through the plateau).
2. Calculate **half of Vmax**: divide Vmax by two. This is a rate on the y-axis.
3. Draw a horizontal line across from half Vmax to the curve, then a vertical line down to the x-axis.
4. Read the substrate concentration where it meets the axis: that is **Km**. Give it units of concentration (for example mmol dm⁻³).
:::

:::warn Km is a concentration, not a rate
Km is **not** "half of Vmax". Half of Vmax is a rate (units such as µmol min⁻¹). Km is the substrate concentration at which that half-rate is reached (units such as mmol dm⁻³). Always state the units: they show which you have found.
:::

:::eg The graph above shows an enzyme. Find its Vmax and its Km.
**Vmax**: the curve levels off towards the dashed line at 80 arbitrary units, so Vmax = 80 arbitrary units.

**Half of Vmax**: \(80 \div 2 = 40\) arbitrary units.

**Km**: draw a horizontal line from 40 on the y-axis to the curve, then a vertical line down to the x-axis. It meets the axis at 5, so

\[\mathrm{Km} = 5\,\mathrm{mmol\,dm^{-3}}\]

At a substrate concentration of 5 mmol dm⁻³ the enzyme works at half its maximum speed. At 50 mmol dm⁻³, ten times as much, the rate is only about 73 units, because the curve is almost flat there.
:::

Often you are not given a graph, but a table. Then you plot the points, draw a smooth curve, and read the graph in the same way.

:::eg The table shows the initial rate of an enzyme at different substrate concentrations. Estimate Vmax and Km.
Rates are in µmol min⁻¹.

| [S] / mmol dm⁻³ | rate |
|---|---|
| 1 | 10.0 |
| 2 | 16.7 |
| 4 | 25.0 |
| 8 | 33.3 |
| 16 | 40.0 |
| 32 | 44.4 |
| 64 | 47.1 |

**Step 1: Vmax.** Plot rate (y-axis) against [S] (x-axis) and draw a smooth curve. The rate is still rising slowly at 64 mmol dm⁻³ (47.1) and the increases are getting smaller: 40.0, 44.4, 47.1. The curve is approaching a plateau at about 50 µmol min⁻¹. So Vmax is about 50 µmol min⁻¹.

**Step 2: half of Vmax.** \(50 \div 2 = 25\) µmol min⁻¹.

**Step 3: Km.** Read across from 25 on the y-axis to the curve. The table shows a rate of 25.0 at [S] = 4 mmol dm⁻³, so

\[\mathrm{Km} \approx 4\,\mathrm{mmol\,dm^{-3}}\]

Note that Vmax is an estimate from the shape of the curve, not a value from the table, so answer with "about". Do not use the highest rate in the table as Vmax: the enzyme has not yet reached saturation at 64 mmol dm⁻³.
:::

### Comparing the affinity of enzymes

A **low Km** means the enzyme reaches half its maximum rate at a **low** substrate concentration, so it binds its substrate readily: it has a **high affinity**. A **high Km** means a high substrate concentration is needed to reach half Vmax, so the enzyme has a **low affinity**.

:::plot Two enzymes with the same Vmax (90 units). Enzyme X reaches half Vmax at 2 mmol dm⁻³ and enzyme Y at 10 mmol dm⁻³, so X has the higher affinity.
--f "90*x/(2+x)" --f "90*x/(10+x)" --x 0 40 --y 0 125 --hline 90 --xlabel "substrate concentration / mmol dm⁻³" --ylabel "initial rate / arbitrary units" --label "enzyme X" --label "enzyme Y" --pt "2,45,X: Km = 2@e" --pt "10,45,Y: Km = 10@se" --legend tr --alt "Both curves level off towards 90 units. Enzyme X rises very steeply and reaches 45 units at a substrate concentration of 2. Enzyme Y rises more slowly and reaches 45 units at a substrate concentration of 10."
:::

:::eg Enzymes X and Y in the graph both act on the same substrate. Compare their affinities, and say which would work faster where the substrate concentration is low.
Both enzymes have the same Vmax, 90 arbitrary units. Half of Vmax is 45 units.

Enzyme X reaches 45 units at 2 mmol dm⁻³, so Km (X) = 2 mmol dm⁻³. Enzyme Y reaches 45 units at 10 mmol dm⁻³, so Km (Y) = 10 mmol dm⁻³.

X has the lower Km, so X has the **higher affinity** for the substrate.

At 2 mmol dm⁻³, X works at 45 units, but Y works at only 15 units (read from the graph), so X is three times faster there. X is the better enzyme where substrate is scarce. At very high substrate concentrations the two rates become almost the same, because both approach 90 units.
:::

:::exam High Km does not mean high affinity
"Low Km, high affinity" is the rule examiners test. Write the reasoning: "enzyme X reaches half Vmax at a lower substrate concentration, so it binds the substrate more readily, so it has a higher affinity." A single word ("X has a lower Km") only earns the first mark.
:::

## Inhibitors

An **inhibitor** is a substance that binds to an enzyme and reduces its rate (see [Enzymes](#bio.enzymes)). Inhibitors matter because cells use them to control reactions, and because many medicines and poisons are inhibitors.

- A **reversible inhibitor** binds weakly and can come off again, so the enzyme works again if the inhibitor is removed. The next two sections are about these.
- An **irreversible inhibitor** binds permanently (often by strong covalent bonds) and the enzyme is lost for good. Penicillin is an example: it blocks an enzyme that bacteria need to build their cell walls (see [Antibiotics and resistance](#bio.antibiotics)).

:::html
<figure class="fig small"><svg viewBox="0 0 345 474" role="img" aria-label="Three stages. 1: with no inhibitor the substrate fits the active site and forms an enzyme–substrate complex. 2: a competitive inhibitor, with a shape like the substrate, sits in the active site, so the substrate cannot bind. 3: a non-competitive inhibitor binds to the enzyme away from the active site and changes the shape of the active site, so the substrate no longer fits."><text class="tl tb" x="10" y="16">1  No inhibitor: substrate binds</text><path class="f1 s-acc sw2" d="M40 70L95 70L105 92L135 92L145 70L200 70L200 112L40 112Z"/><path class="f2 s-acc2 sw2" d="M90 62L150 62L150 70L145 70L135 92L105 92L95 70L90 70Z"/><text class="tl" x="232" y="50">substrate</text><path class="ln-m thin" d="M228 46L152 66"/><text class="tl" x="10" y="130">active site occupied</text><path class="ln-m thin" d="M100 116L115 94"/><text class="tl tb" x="10" y="166">2  Competitive inhibitor in the active site</text><path class="f1 s-acc sw2" d="M40 220L95 220L105 242L135 242L145 220L200 220L200 262L40 262Z"/><path class="f2 s-acc2 sw2" d="M90 180L150 180L150 188L145 188L135 210L105 210L95 188L90 188Z"/><path class="f3 s-acc sw2" d="M98 216L142 216L145 220L135 242L105 242L95 220Z"/><text class="tl" x="232" y="188">substrate</text><path class="ln-m thin" d="M228 184L154 184"/><text class="tl" x="232" y="224">competitive</text><text class="tl" x="232" y="238">inhibitor</text><path class="ln-m thin" d="M228 232L146 232"/><text class="tl" x="10" y="280">active site blocked</text><path class="ln-m thin" d="M100 266L115 244"/><text class="tl tb" x="10" y="316">3  Non-competitive inhibitor elsewhere</text><path class="f1 s-acc sw2" d="M40 370L104 370L112 378L128 378L136 370L200 370L200 412L40 412Z"/><path class="f2 s-acc2 sw2" d="M90 330L150 330L150 338L145 338L135 360L105 360L95 338L90 338Z"/><path class="f3 s-acc sw2" d="M200 382L214 382L222 391L214 400L200 400Z"/><text class="tl" x="232" y="338">substrate</text><path class="ln-m thin" d="M228 334L154 334"/><text class="tl" x="232" y="422">non-competitive</text><text class="tl" x="232" y="436">inhibitor</text><path class="ln-m thin" d="M236 408L221 400"/><text class="tl" x="10" y="430">active site changed shape</text><path class="ln-m thin" d="M100 416L115 380"/></svg><figcaption>How inhibitors bind. A competitive inhibitor competes with the substrate for the active site. A non-competitive inhibitor binds somewhere else on the enzyme and changes the shape of the active site, whatever the substrate concentration.</figcaption></figure>
:::

### Competitive inhibitors

:::def Competitive inhibitor
A reversible inhibitor with a shape similar to the substrate. It binds to the active site and so competes with the substrate for it. It reduces the rate of reaction, but the effect can be reduced by increasing the substrate concentration.
:::

How a competitive inhibitor works:
- Its shape is **similar to the substrate's**, so it is complementary to the active site and can bind there.
- While it occupies an active site, no substrate can bind to it: fewer enzyme–substrate complexes form, so the rate falls.
- It is not changed by the enzyme and it can leave again, so binding is **reversible**.
- Inhibitor and substrate compete. If the substrate concentration is raised, a substrate molecule is much more likely to reach an empty active site than an inhibitor molecule is, so the inhibitor loses and the rate recovers.

:::plot A competitive inhibitor. At low substrate concentrations the rate is much lower with the inhibitor, but at high concentrations it approaches the same Vmax of 80 units. Km rises from 4 to 12 mmol dm⁻³.
--f "80*x/(4+x)" --f "80*x/(12+x)" --x 0 60 --y 0 125 --hline 80 --xlabel "substrate concentration / mmol dm⁻³" --ylabel "initial rate / arbitrary units" --label "no inhibitor" --label "with competitive inhibitor" --pt "4,40,Km = 4@e" --pt "12,40,Km = 12@se" --legend tr --alt "Both curves level off towards 80 units. The curve with no inhibitor rises more steeply and reaches 40 units at a substrate concentration of 4. The curve with the competitive inhibitor rises more slowly, reaches 40 units at 12, and gets close to the other curve at high substrate concentrations."
:::

:::key Effect of a competitive inhibitor on the graph
- **Vmax is unchanged**: with enough substrate, the substrate wins the competition and every active site is eventually filled with substrate.
- **Km increases**: more substrate is needed to reach half Vmax, so the apparent affinity of the enzyme for its substrate is lower.
- The rate is reduced most at **low** substrate concentrations, and hardly at all at very high ones.
:::

:::eg Real context, poisoning: methanol is toxic because an enzyme in the liver converts it into poisonous products. Patients who have swallowed methanol can be given ethanol. Explain how this helps.
Ethanol has a shape similar to methanol, so it can bind to the active site of the same enzyme. [B1]

It is a competitive inhibitor: it competes with methanol for the active site. [B1]

Fewer methanol molecules are converted into the poisonous products, so less harm is done, and the methanol is lost from the body unchanged in the urine and breath. [B1]

The effect is reversible and depends on concentration, which is why the dose of ethanol must be high enough to keep most of the active sites busy.
:::

### Non-competitive inhibitors

:::def Non-competitive inhibitor
A reversible inhibitor that binds to the enzyme at a site other than the active site (an allosteric site). Binding changes the shape of the active site, so substrate molecules can no longer bind. Increasing the substrate concentration does not overcome its effect.
:::

How a non-competitive inhibitor works:
- It has **no need to look like the substrate**: it binds at a different place on the enzyme.
- Its binding changes the **tertiary structure**, so the active site changes shape and the substrate is no longer complementary to it.
- The inhibitor does not compete with the substrate, so **adding more substrate does not remove it**. Some enzyme molecules are out of action at any moment, and substrate cannot get them going again.
- The effect is the same as if there were **less enzyme** in the mixture: the maximum rate is lower.

:::plot A non-competitive inhibitor. The inhibitor lowers the maximum rate from 80 to 40 units at every substrate concentration, and Km stays at 4 mmol dm⁻³.
--f "80*x/(4+x)" --f "40*x/(4+x)" --x 0 40 --y 0 125 --hline 80 --hline 40 --vline 4 --xlabel "substrate concentration / mmol dm⁻³" --ylabel "initial rate / arbitrary units" --label "no inhibitor" --label "with non-competitive inhibitor" --legend tr --alt "Both curves rise and level off. The curve with no inhibitor levels off towards 80 units and the curve with the non-competitive inhibitor towards 40 units. A dashed vertical line at a substrate concentration of 4 shows that each curve reaches half of its own maximum there, so Km is 4 for both."
:::

:::key Effect of a non-competitive inhibitor on the graph
- **Vmax decreases**: some enzyme molecules cannot work however much substrate is present.
- **Km is unchanged**: the enzyme molecules that still work bind the substrate as well as before, so half of the (lower) Vmax is still reached at the same substrate concentration.
- Raising the substrate concentration does **not** bring the rate back up to the uninhibited curve.
:::

:::analogy A decoy and a bent door
A competitive inhibitor is like a wrong key that fits in a lock but will not turn: it blocks the keyhole, but if there are enough right keys they will eventually get a turn. A non-competitive inhibitor is like someone bending the door frame: whichever key you use, the door no longer opens.
:::

:::key Competitive and non-competitive inhibitors compared
| feature | Competitive | Non-competitive |
|---|---|---|
| Shape | similar to the substrate | need not resemble it |
| Binds | to the active site | elsewhere (allosteric site) |
| More substrate | reduces its effect | does not help |
| Vmax | unchanged | decreases |
| Km | increases | unchanged |
:::

Try it yourself: the widget starts with the competitive inhibitor on. Switch it off and on and watch Km, then try the non-competitive inhibitor and watch Vmax. The sliders change the enzyme itself.

:::html
<div class="widget" data-w="bio-enzyme" data-mode="kinetics"></div>
:::

:::note End-product inhibition
Cells use inhibitors to avoid wasting resources. In many metabolic pathways the final product acts as a non-competitive inhibitor of an enzyme near the start of the pathway. When the product builds up, it switches the first enzyme off; when it is used up, the inhibitor leaves and the pathway restarts. The cell makes only as much as it needs.
:::

### Reading inhibitor graphs

To decide which kind of inhibitor you have, compare the curves with and without the inhibitor.

:::steps
1. Compare the curves at **high** substrate concentration. If they approach the **same** plateau, Vmax is unchanged: the inhibitor is **competitive**. If the inhibited plateau is lower, Vmax has decreased: **non-competitive**.
2. Check Km. Find half of Vmax for each curve and read the substrate concentration. If Km is **larger** with the inhibitor (and Vmax the same), the inhibitor is competitive. If Km is the **same**, it is non-competitive.
3. Write your answer with figures from the graph and with the biological reason (where the inhibitor binds).
:::

:::eg Two inhibitors, X and Y, were added separately to an enzyme. The table shows the initial rates (µmol min⁻¹) at different substrate concentrations. Decide which inhibitor is competitive and which is non-competitive.
| [S] / mmol dm⁻³ | none | X | Y |
|---|---|---|---|
| 5 | 50.0 | 25.0 | 30.0 |
| 10 | 66.7 | 40.0 | 40.0 |
| 20 | 80.0 | 57.1 | 48.0 |
| 40 | 88.9 | 72.7 | 53.3 |
| 80 | 94.1 | 84.2 | 56.5 |
| 160 | 97.0 | 91.4 | 58.2 |

**No inhibitor**: the rate approaches a Vmax of about 100 µmol min⁻¹. Half of Vmax is 50, which the enzyme reaches at 5 mmol dm⁻³, so Km is about 5 mmol dm⁻³.

**Inhibitor X**: at high [S] the rate approaches the same plateau (91.4 at 160, compared with 97.0), so Vmax is unchanged. It reaches 50 between [S] = 10 and 20, at about 15 mmol dm⁻³: Km has increased from 5 to about 15 mmol dm⁻³. The effect is largest at low [S] (25.0 against 50.0 at 5 mmol dm⁻³) and shrinks as [S] rises. X is a **competitive** inhibitor.

**Inhibitor Y**: the rate approaches a plateau of about 60, much lower than 100, so Vmax has decreased. Half of that is 30, which is reached at 5 mmol dm⁻³, so Km is unchanged. Adding more substrate does not bring the rate back (58.2 at 160 against 97.0). Y is a **non-competitive** inhibitor.
:::

:::eg The graph above of a competitive inhibitor shows the rate with and without the inhibitor. Describe and explain the effect of the inhibitor on the rate of reaction.
Describe first, with figures from the graph:

At 4 mmol dm⁻³ the rate is 40 units without the inhibitor and 20 units with it, so the inhibitor lowers the rate. [B1]

The difference becomes smaller as the substrate concentration increases (at 12 mmol dm⁻³ the rates are 60 and 40), and both curves approach the same Vmax of 80 units. [B1]

Then explain:

The inhibitor has a shape similar to the substrate. [B1]

It binds to the active site, so it competes with the substrate, and fewer enzyme–substrate complexes form at a given moment. [B1]

At low substrate concentration there are few substrate molecules, so the inhibitor occupies many active sites and the rate is reduced a lot. [B1]

At high substrate concentration, substrate molecules outnumber the inhibitor and are far more likely to occupy the active sites, so the rate approaches the same Vmax. [B1]

A weaker answer says "the inhibitor slows the enzyme down by blocking it". It quotes no figures, does not say that the inhibitor binds to the active site, and does not explain why the effect disappears at a high substrate concentration, so it scores no more than two marks.
:::

:::eg Spot the error: explain the effect of a competitive inhibitor on Vmax and Km. [3]
A student wrote this answer.

Line 1: A competitive inhibitor has a shape similar to the substrate, so it binds to the active site.
Line 2: At a very high substrate concentration the substrate molecules outnumber the inhibitor, so Vmax is the same.
Line 3: More substrate is needed to reach half of Vmax, so Km halves.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: if more substrate is needed to reach half of Vmax, Km increases, because Km is the substrate concentration needed to reach half of Vmax. It does not halve. That mark is lost [B0].**

Correct Line 3: "More substrate is needed to reach half of Vmax, so Km increases." With this change the answer scores 3 marks.
:::

:::warn Three common slips
- "Competitive inhibitors change the shape of the active site." No: a competitive inhibitor **fits** the active site as it is. It is the non-competitive inhibitor, bound elsewhere, that changes the active site's shape.
- "More substrate overcomes a non-competitive inhibitor." No: that is how a **competitive** inhibitor is overcome.
- "Inhibitors denature the enzyme." No: a reversible inhibitor binds without breaking the tertiary structure, and it can leave again.
:::

:::exam Name the type, then the evidence
When a question shows a graph with an inhibitor, give the type (competitive or non-competitive), then the **evidence from the graph** (Vmax and Km, with figures), then the **reason** (where the inhibitor binds, and whether substrate competes with it). Use all three to get the full marks.
:::

## Immobilised enzymes

In industry, enzymes dissolved in a reaction mixture are hard to get back and are usually thrown away with the product. **Immobilising** an enzyme fixes it to, or traps it in, an inert support so that the enzyme stays put while the substrate flows past.

:::def Immobilised enzyme
An enzyme that is fixed to, or trapped in, an insoluble support such as alginate beads, so that it does not mix freely with the reaction mixture and can be separated from the products and reused.
:::

One way to trap enzymes is in beads of **alginate**, a jelly-like substance from seaweed. Sodium alginate dissolves in water, but it sets into a gel when it meets calcium ions. If the enzyme is mixed into the alginate before it sets, it is trapped inside the gel. The beads are porous, so small substrate and product molecules diffuse in and out, but the large enzyme molecules cannot escape.

:::html
<figure class="fig small"><svg viewBox="0 0 350 232" role="img" aria-label="A column of alginate beads. Milk containing lactose enters at the top, flows between beads that hold the enzyme trapped in alginate gel, passes a glass wool plug and leaves at the bottom as product with no enzyme in it. A magnified bead shows enzyme molecules trapped in the gel."><path class="ln" d="M100 12L100 46" marker-end="url(#ah)"/><text class="tl" x="112" y="22">milk (lactose) in</text><rect class="fp ln" x="60" y="50" width="80" height="130"/><circle class="f2 s-acc2 sw2" cx="76" cy="66" r="8"/><circle class="f2 s-acc2 sw2" cx="94" cy="66" r="8"/><circle class="f2 s-acc2 sw2" cx="112" cy="66" r="8"/><circle class="f2 s-acc2 sw2" cx="130" cy="66" r="8"/><circle class="f2 s-acc2 sw2" cx="85" cy="84" r="8"/><circle class="f2 s-acc2 sw2" cx="103" cy="84" r="8"/><circle class="f2 s-acc2 sw2" cx="121" cy="84" r="8"/><circle class="f2 s-acc2 sw2" cx="76" cy="102" r="8"/><circle class="f2 s-acc2 sw2" cx="94" cy="102" r="8"/><circle class="f2 s-acc2 sw2" cx="112" cy="102" r="8"/><circle class="f2 s-acc2 sw2" cx="130" cy="102" r="8"/><circle class="f2 s-acc2 sw2" cx="85" cy="120" r="8"/><circle class="f2 s-acc2 sw2" cx="103" cy="120" r="8"/><circle class="f2 s-acc2 sw2" cx="121" cy="120" r="8"/><circle class="f2 s-acc2 sw2" cx="76" cy="138" r="8"/><circle class="f2 s-acc2 sw2" cx="94" cy="138" r="8"/><circle class="f2 s-acc2 sw2" cx="112" cy="138" r="8"/><circle class="f2 s-acc2 sw2" cx="130" cy="138" r="8"/><circle class="f2 s-acc2 sw2" cx="85" cy="156" r="8"/><circle class="f2 s-acc2 sw2" cx="103" cy="156" r="8"/><circle class="f2 s-acc2 sw2" cx="121" cy="156" r="8"/><rect class="fm s-acc sw2" x="60" y="172" width="80" height="10"/><path class="ln" d="M100 182L100 214" marker-end="url(#ah)"/><text class="tl" x="112" y="204">product out</text><text class="tl" x="112" y="218">(no enzyme)</text><text class="tl" x="160" y="96">alginate beads</text><path class="ln-m thin" d="M156 92L142 98"/><text class="tl" x="160" y="164">glass wool</text><path class="ln-m thin" d="M156 160L142 175"/><circle class="fp s-acc sw2" cx="300" cy="120" r="38"/><circle class="f1 s-acc sw2" cx="285" cy="105" r="4"/><circle class="f1 s-acc sw2" cx="312" cy="100" r="4"/><circle class="f1 s-acc sw2" cx="298" cy="125" r="4"/><circle class="f1 s-acc sw2" cx="322" cy="128" r="4"/><circle class="f1 s-acc sw2" cx="280" cy="138" r="4"/><circle class="f1 s-acc sw2" cx="305" cy="146" r="4"/><text class="tl" x="300" y="176" text-anchor="middle">enzyme in</text><text class="tl" x="300" y="190" text-anchor="middle">alginate gel</text></svg><figcaption>An immobilised enzyme column. The enzyme stays in the beads, so the liquid leaving the column holds the product but no enzyme, and the beads can be used again. The circle on the right shows one bead magnified.</figcaption></figure>
:::

:::lab Immobilising an enzyme in alginate and comparing it with the free enzyme
**Aim**: compare the activity of lactase immobilised in alginate beads with the same enzyme free in solution.

:::steps
1. Mix equal volumes of sodium alginate solution (a few per cent) and lactase solution in a small beaker.
2. Fill a syringe with the mixture. Hold it a few centimetres above a beaker of calcium chloride solution and let the mixture fall in **drop by drop**. Each drop sets into a bead as calcium ions link the alginate chains into a gel, trapping the enzyme.
3. Leave the beads for about 10 minutes to set, strain them from the calcium chloride and rinse them with distilled water, to wash away enzyme stuck to the surface.
4. **Immobilised enzyme**: pack the beads into a syringe barrel or column with a plug of glass wool at the bottom. Pour a fixed volume of milk through at a constant, slow rate and collect what leaves.
5. **Free enzyme**: mix the same volume of milk with the same volume of lactase solution as was used to make the beads, at the same temperature, and leave it for the same time.
6. Test a sample of each for glucose, using glucose test strips (see the note below), and compare. Pour fresh milk through the same beads again to see if they still work.
:::

**Variables**: the independent variable is whether the enzyme is free or immobilised; the dependent variable is the amount of glucose produced in a set time (a test strip colour, or a concentration read from a calibration). Standardise the volume and type of milk, the amount of enzyme, the temperature (a water bath), the contact time or flow rate, and the size of the beads (use the same syringe and needle).

**Control**: beads made with alginate but no enzyme. They should produce no glucose, showing that the glucose comes from the enzyme and not from the alginate or calcium chloride.

**Typical results**: the free enzyme usually gives more glucose in a short time than the same amount of enzyme in beads, because the substrate has to diffuse into the beads. But the beads can be washed and used again, and the liquid leaving the column holds no enzyme.

**Sources of error**: beads of different sizes (a different surface area for diffusion); enzyme leaking out of beads; an uneven flow rate; the colour judgement on test strips. Improve by using the same needle, a pump or a fixed drip rate, and repeating.

**Note on testing**: lactose is itself a reducing sugar, so Benedict's solution would turn colour with the milk **before** any lactase is added, and cannot show the new glucose. A test specific to glucose, such as a test strip that contains the enzyme glucose oxidase, is needed (see [Testing for biological molecules](#bio.foodtests)).

**Safety**: calcium chloride solution irritates the eyes, and enzymes can cause allergic reactions, so wear eye protection and wash hands. Do not drink the milk. Risk: low.
:::

:::cols
:::col Advantages of immobilised enzymes
- The enzyme can be **reused**, which saves money.
- The product is **not contaminated** with enzyme, so no extra step is needed to remove it.
- The enzyme is often **more stable**: it works over a wider range of temperature and pH, because the support protects its tertiary structure.
- The reaction can run **continuously** (substrate flows through, product flows out) and be stopped at once by taking the liquid away from the beads.
:::
:::col Disadvantages
- Setting it up costs more than adding enzyme to a vat.
- The substrate must **diffuse into the beads**, so the rate can be lower than with the free enzyme.
- Some enzyme may be lost or damaged in making the beads, and beads can break.
- Large substrate molecules may not enter the beads at all.
:::
:::

:::eg Real context, lactose-free milk: explain why a dairy uses lactase immobilised in beads rather than adding lactase solution to the milk.
Lactase hydrolyses lactose in milk into glucose and galactose, so that people who cannot digest lactose can drink the milk.

The immobilised lactase stays in the column, so the milk that leaves is not contaminated with enzyme. [B1]

The beads can be reused many times, which saves the cost of buying fresh enzyme for every batch. [B1]

Milk can flow through the column continuously, so the process is easy to control. [B1]

The beads may also tolerate temperature and pH changes better than free lactase. A disadvantage is that the rate may be lower because the lactose has to diffuse into the beads.
:::

:::eg The table compares the activity of an enzyme free in solution with the same enzyme immobilised in alginate beads at different temperatures. Compare the two and suggest explanations.
Relative activity is a percentage of the activity of the free enzyme at 40 °C.

| temperature / °C | free | immobilised |
|---|---|---|
| 30 | 70 | 55 |
| 40 | 100 | 80 |
| 50 | 40 | 85 |
| 60 | 5 | 52 |
| 70 | 0 | 15 |

At 40 °C the immobilised enzyme is less active than the free enzyme (80 compared with 100). [B1]

This is because the substrate must diffuse into the beads to reach the enzyme, which slows the reaction. [B1]

At higher temperatures the immobilised enzyme keeps much more of its activity: 85 compared with 40 at 50 °C and 52 compared with 5 at 60 °C. [B1]

The optimum of the immobilised enzyme is higher (50 °C instead of 40 °C) and it works over a wider range of temperature. [B1]

The alginate gel holds the enzyme molecule in shape, so its tertiary structure is more stable and fewer bonds are broken, so less of the enzyme is denatured. [B1]
:::

## Practice

:::try Start easy, finish at exam standard
Q: Define the Michaelis–Menten constant, Km.
A: The substrate concentration at which the reaction rate is half of Vmax.
Q: An enzyme has a Vmax of 36 µmol min⁻¹. State the rate at which Km is read from the graph.
A: Half of Vmax: \(36 \div 2 = 18\,\mathrm{\mu mol\,min^{-1}}\).
Q: Enzyme M has a Km of 0.5 mmol dm⁻³ and enzyme N has a Km of 4 mmol dm⁻³ for the same substrate. Which has the higher affinity? Explain.
A: Enzyme M. It reaches half of its maximum rate at a lower substrate concentration, so it binds the substrate more readily.
Q: State two differences between a competitive and a non-competitive inhibitor.
A: Any two of: a competitive inhibitor binds to the active site, a non-competitive inhibitor binds elsewhere; a competitive inhibitor's effect is reduced by more substrate, a non-competitive inhibitor's is not; a competitive inhibitor does not change Vmax, a non-competitive inhibitor lowers it; a competitive inhibitor raises Km, a non-competitive does not change it.
Q: Explain why increasing the substrate concentration reduces the effect of a competitive inhibitor.
A: Substrate molecules then outnumber the inhibitor molecules, so a substrate molecule is more likely than an inhibitor molecule to reach an active site, so more enzyme–substrate complexes form.
Q: A non-competitive inhibitor lowers Vmax from 60 to 36 units. Calculate the percentage decrease.
A: \((60 - 36) \div 60 \times 100 = 40\%\).
Q: Explain why a non-competitive inhibitor does not change the shape of the whole enzyme enough to count as denaturing it.
A: It binds weakly and reversibly at one site, causing a local change in the active site's shape; when the inhibitor leaves the enzyme works again. Denaturation, by heat or extreme pH, breaks bonds in the tertiary structure and is usually permanent.
Q: Describe how enzyme-containing alginate beads are made.
A: Mix the enzyme with sodium alginate solution and drip the mixture from a syringe into calcium chloride solution. Each drop sets into a gel bead with the enzyme trapped inside.
Q: State two advantages of using an immobilised enzyme rather than a free enzyme.
A: Any two of: it can be reused; the product is not contaminated with enzyme; it is more stable to temperature or pH changes; it allows continuous processes.
Q: Suggest why the rate of reaction of an immobilised enzyme may be lower than that of the same amount of free enzyme.
A: The substrate must diffuse into the alginate beads before it reaches the enzyme, so the reaction is slower.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State what is meant by Km, and what a low value of Km shows about an enzyme.
A: Km is the substrate concentration at which the rate of reaction is half of Vmax. [B1]
A low Km shows a high affinity: the enzyme reaches half its maximum rate at a low substrate concentration. [B1]
Q: [5 marks] ★★ The initial rates of two enzymes, P and Q, which act on the same substrate, were measured at different substrate concentrations. Rates are in µmol min⁻¹.

| [S] / mmol dm⁻³ | P | Q |
|---|---|---|
| 2 | 30.0 | 12.0 |
| 4 | 40.0 | 20.0 |
| 8 | 48.0 | 30.0 |
| 16 | 53.3 | 40.0 |
| 32 | 56.5 | 48.0 |
| 64 | 58.2 | 53.3 |

(a) Estimate Vmax for each enzyme. (b) Find Km for each enzyme. (c) State, with a reason, which enzyme has the higher affinity for the substrate.
H: Plot both curves. Where is each heading?
H: Half of Vmax is the rate at which you read Km.
A: (a) Both curves approach a plateau of about 60 µmol min⁻¹, so Vmax is about 60 for both enzymes. [B1]
(b) Half of Vmax is 30 µmol min⁻¹; P reaches this at 2 mmol dm⁻³ and Q at 8 mmol dm⁻³. [B1]
So Km (P) = 2 mmol dm⁻³ and Km (Q) = 8 mmol dm⁻³. [B1]
(c) Enzyme P has the higher affinity, because its Km is lower [B1] so it reaches half its maximum rate at a lower substrate concentration. [B1]
Q: [4 marks] ★★ Explain why, in the presence of a competitive inhibitor, the rate of an enzyme reaction increases when the substrate concentration is increased and can reach the same Vmax, but in the presence of a non-competitive inhibitor it cannot.
H: Where does each inhibitor bind?
H: With a non-competitive inhibitor, is any substrate able to reach the inhibited enzyme molecules?
A: A competitive inhibitor binds to the active site, so it competes with the substrate. [B1]
At a high substrate concentration, substrate molecules outnumber inhibitor molecules, so they occupy the active sites and the rate reaches Vmax. [B1]
A non-competitive inhibitor binds elsewhere and changes the shape of the active site, so substrate cannot bind to those enzyme molecules. [B1]
Extra substrate cannot displace the inhibitor, so some enzyme molecules are always inactive and Vmax stays lower. [B1]
Q: [6 marks] ★★★ An insecticide, Z, inhibits an enzyme that works in the nerves of insects. The initial rate of the enzyme was measured with and without Z. Rates are in arbitrary units.

| [S] / mmol dm⁻³ | no Z | with Z |
|---|---|---|
| 1 | 12.8 | 6.4 |
| 2 | 21.3 | 10.7 |
| 4 | 32.0 | 16.0 |
| 8 | 42.7 | 21.3 |
| 16 | 51.2 | 25.6 |
| 32 | 56.9 | 28.4 |

(a) Estimate Vmax and Km with and without Z. (b) Decide whether Z is a competitive or non-competitive inhibitor, giving two reasons. (c) Explain why increasing the substrate concentration does not restore the rate when Z is present.
H: Vmax is where the curve is heading; both curves flatten.
H: Compare the rates at each concentration: what fraction is the second column of the first?
A: (a) Without Z, Vmax is about 64 and Km is 4 mmol dm⁻³ (half of 64 is 32, reached at 4). With Z, Vmax is about 32 and Km is 4 mmol dm⁻³ (half of 32 is 16, reached at 4). [B1] [B1]
(b) Z is a non-competitive inhibitor. Vmax is lower with Z. [B1] Km is unchanged. [B1]
(c) Z binds to a site other than the active site and changes the shape of the active site, so substrate cannot bind to the inhibited enzyme molecules. [B1]
More substrate cannot displace Z, so those molecules stay inactive. [B1]
Q: [5 marks] ★★ Lactase beads were used repeatedly. After each use they were rinsed and used with fresh milk. The activity (as a percentage of the first use) was 100, 98, 97, 95, 92 and 88 for uses 1 to 6. (a) Calculate the percentage decrease in activity between use 1 and use 6. (b) Suggest two reasons why the activity decreases. (c) State one advantage of reuse.
H: Percentage decrease is the change divided by the original, times 100.
A: (a) \((100 - 88) \div 100 \times 100\) [M1] \(= 12\%\) [A1]
(b) Some beads break or some enzyme leaks out of the beads. [B1]
Enzyme molecules slowly become denatured. [B1]
(c) The enzyme is reused, so it costs less per batch (or the product is not contaminated with enzyme). [B1]
Q: [4 marks] ★★ Methanol is converted by an enzyme into a toxic product. A researcher wants to show that ethanol is a competitive inhibitor of this enzyme. (a) Suggest how a graph of rate against methanol concentration, with and without ethanol, would show this. (b) Explain why ethanol is a competitive inhibitor.
H: What happens to Vmax and Km in a competitive inhibition?
A: (a) With ethanol, Vmax is the same, so the curves approach the same plateau. [B1]
The curve with ethanol is lower at low methanol concentrations and reaches half of Vmax at a higher concentration (Km increases). [B1]
(b) Ethanol has a similar shape to methanol, so it binds to the active site. [B1]
It competes with methanol, so its effect is reduced when the methanol concentration increases. [B1]
Q: [6 marks] (#bio.foodtests) ★★★ A student compared lactase free in solution with lactase in alginate beads. 5 cm³ of milk was added to each, and after 5 minutes a glucose test strip was used. (a) Describe how the beads were made. (b) Explain why Benedict's solution would be unsuitable for measuring the glucose made. (c) The free enzyme produced more glucose than the beads in the first 5 minutes. Explain this. (d) Give one reason why a manufacturer might still choose to use the beads.
H: Is lactose a reducing sugar?
H: How does the substrate reach the enzyme in a bead?
A: (a) Mix the lactase with sodium alginate solution and drip the mixture into calcium chloride solution. [B1]
The drops set into beads with the enzyme trapped inside. [B1]
(b) Lactose is itself a reducing sugar, so milk would give a positive Benedict's test before any glucose was made. [B1]
(c) In the beads, the lactose must diffuse into the beads to reach the enzyme, so the reaction is slower. [B1] With the free enzyme, the lactase is mixed through the milk so enzyme and substrate collide more often. [B1]
(d) The beads can be reused (or the product is not contaminated with enzyme). [B1]
Q: [6 marks] ★★★ In a metabolic pathway, the final product inhibits the first enzyme in the pathway. The inhibitor binds at a site away from the active site. (a) State the type of inhibition. (b) Explain how this controls the amount of product made. (c) Explain why the pathway still switches off when the substrate of the first enzyme is present at a very high concentration.
H: What happens to the shape of the active site when the product binds?
A: (a) Non-competitive inhibition. [B1]
(b) As the product concentration rises, more product binds to the first enzyme and changes the shape of its active site. [B1]
Fewer enzyme–substrate complexes form, so less product is made. [B1]
When the product is used up, it leaves the enzyme, the active site regains its shape and the pathway restarts. [B1]
(c) The product does not compete with the substrate for the active site. [B1]
So more substrate cannot displace it, and the inhibited enzyme molecules stay inactive. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A research team tested two possible drugs, A and B, on an enzyme. The table shows the initial rate (µmol min⁻¹) at four substrate concentrations.

| [S] / mmol dm⁻³ | none | A | B |
|---|---|---|---|
| 2 | 40.0 | 14.3 | 16.0 |
| 10 | 76.9 | 45.5 | 30.8 |
| 30 | 90.9 | 71.4 | 36.4 |
| 100 | 97.1 | 89.3 | 38.8 |

(a) Calculate the percentage decrease in rate caused by each drug at 2 mmol dm⁻³ and at 100 mmol dm⁻³, to the nearest whole number. (b) Use your answers to decide which drug is competitive and which is non-competitive. (c) The drugs will be used in tissues where the substrate concentration is very high. Which drug is likely to be less effective, and why?
H: Percentage decrease \(= (\text{none} - \text{drug}) \div \text{none} \times 100\).
H: A competitive inhibitor loses its effect when the substrate is plentiful.
A: (a) Drug A: \((40.0 - 14.3) \div 40.0 \times 100\) [M1] \(= 64\%\) at 2 mmol dm⁻³, and \((97.1 - 89.3) \div 97.1 \times 100 = 8\%\) at 100 mmol dm⁻³. [A1]
Drug B: \((40.0 - 16.0) \div 40.0 \times 100 = 60\%\) at 2 mmol dm⁻³ and \((97.1 - 38.8) \div 97.1 \times 100 = 60\%\) at 100 mmol dm⁻³. [A1]
(b) Drug A is competitive, because its effect almost disappears at a high substrate concentration (8%). [B1]
Drug B is non-competitive, because its effect does not change with substrate concentration (60% at both). [B1]
(c) Drug A, because at a very high substrate concentration substrate molecules outcompete the inhibitor at the active site. [B1]
Q: [5 marks] ★★★ An immobilised enzyme column was used to convert a sugar. The solution was passed through at three flow rates. The table shows the percentage of the sugar converted, which is the proportion that changed.

| flow rate / cm³ min⁻¹ | converted / % |
|---|---|
| 5 | 96 |
| 10 | 90 |
| 20 | 71 |

(a) Calculate, for each flow rate, the volume of solution fully converted per minute (flow rate × fraction converted). (b) Explain why the percentage converted falls as the flow rate increases. (c) Suggest why the factory still runs the column at a high flow rate.
H: Convert the percentage to a fraction first.
H: At a higher flow rate, how long is the solution in contact with the beads?
A: (a) \(5 \times 0.96 = 4.8\), \(10 \times 0.90 = 9.0\) and \(20 \times 0.71 = 14.2\) cm³ min⁻¹ [M1] [A1]
(b) At a higher flow rate the solution spends less time in contact with the beads. [B1] So less substrate has time to diffuse in, form enzyme–substrate complexes and be converted. [B1]
(c) The total amount converted per minute still rises (4.8 to 14.2), so more product is made in the same time. [B1]
:::

:::quiz
? What is the Michaelis–Menten constant, Km?
+ The substrate concentration at which the rate is half of Vmax.
- Half of the maximum rate of the reaction.
- The maximum substrate concentration the enzyme can bind.
- The rate of reaction when the enzyme concentration is halved.
> Km is a substrate concentration (units such as mmol dm⁻³). Half of Vmax is a rate; Km is the concentration at which the enzyme reaches that rate.
? Enzyme A has Km = 2 mmol dm⁻³ and enzyme B has Km = 9 mmol dm⁻³ for the same substrate. Which statement is correct?
+ Enzyme A has the higher affinity.
- Enzyme B has the higher affinity.
- Enzyme A has the higher Vmax.
- Enzyme B reaches saturation at a lower concentration.
> A lower Km means half of Vmax is reached at a lower concentration, so a higher affinity. Km does not tell you the value of Vmax.
? Which change in Vmax and Km is caused by a competitive inhibitor?
+ Vmax unchanged, Km increased
- Vmax decreased, Km unchanged
- Vmax decreased, Km increased
- Vmax increased, Km decreased
> The substrate can still reach the same Vmax if it is plentiful, but more of it is needed to reach half of that. The second option describes a non-competitive inhibitor.
? A non-competitive inhibitor lowers the rate of an enzyme reaction. Why does adding more substrate not restore the rate?
+ The inhibitor binds elsewhere on the enzyme and changes the shape of the active site, so substrate cannot bind however much there is.
- The inhibitor binds to the active site and substrate cannot displace it.
- The extra substrate denatures the enzyme.
- The inhibitor is used up by the substrate.
> The inhibitor does not compete with the substrate. It is not at the active site, so more substrate cannot displace it.
? Which statement about a competitive inhibitor is correct?
+ It has a shape similar to the substrate and binds to the active site.
- It binds to a different site and changes the shape of the active site.
- It permanently changes the primary structure of the enzyme.
- It increases the activation energy of the substrate.
> A competitive inhibitor fits the active site because it resembles the substrate. It does not change the enzyme.
? What is trapped in the alginate gel when an enzyme is immobilised in beads?
+ The enzyme molecules, which are too large to leave the gel.
- The substrate molecules, which cannot leave the gel.
- The product molecules, which stay in the gel.
- The calcium ions, which are needed for the reaction.
> The gel is porous. Small substrate and product molecules diffuse in and out, but the large enzyme molecules are held inside.
? Which is an advantage of using an immobilised enzyme?
+ The enzyme can be reused and does not contaminate the product.
- The reaction is always faster than with the free enzyme.
- The enzyme no longer needs a particular pH.
- The substrate no longer needs to reach the active site.
> Immobilised enzymes are reused and stay out of the product. The rate can be lower because the substrate must diffuse in, and the enzyme still has an optimum pH.
? On a graph of rate against substrate concentration, a curve with an inhibitor levels off at a lower value than the curve without. Km is the same for both. What type of inhibitor is it?
+ non-competitive
- competitive
- irreversible and competitive
- an inhibitor that raises the substrate concentration
> A lower Vmax with an unchanged Km shows a non-competitive inhibitor. A competitive inhibitor leaves Vmax the same and raises Km.
? A student writes: "Km is half of Vmax." What is wrong with this?
+ Half of Vmax is a rate; Km is the substrate concentration at which that rate is reached.
- Km is double Vmax.
- Km is equal to Vmax.
- Km is the rate when all active sites are empty.
> Km and Vmax are different quantities with different units. Half of Vmax is read on the rate axis; Km is read from the substrate concentration axis.
:::

:::checklist What you can now do
- [ ] I can explain that Vmax is the maximum rate and that it is used to find Km.
- [ ] I can read Vmax and Km from a graph or table of rate against substrate concentration, with units.
- [ ] I can use Km to compare the affinities of different enzymes for their substrates (low Km, high affinity).
- [ ] I can explain how a competitive inhibitor works and its effect on Vmax, Km and the graph.
- [ ] I can explain how a non-competitive inhibitor works and its effect on Vmax, Km and the graph.
- [ ] I can tell from a graph or table whether an inhibitor is competitive or non-competitive, using figures.
- [ ] I can describe and carry out an investigation comparing an enzyme immobilised in alginate with the free enzyme.
- [ ] I can state the advantages (and disadvantages) of using immobilised enzymes.
:::

:::recap
- Vmax = maximum rate (all active sites occupied). Km = substrate concentration at half of Vmax (a concentration, with units). Low Km = high affinity.
- Reading Km: find Vmax, halve it, read across to the curve, then down to the axis.
- Competitive inhibitor: similar shape to the substrate, binds the active site, reversible; more substrate reduces its effect. Vmax unchanged, Km increases.
- Non-competitive inhibitor: binds elsewhere (an allosteric site), changes the shape of the active site; more substrate does not help. Vmax decreases, Km unchanged.
- End-product inhibition: the final product inhibits an early enzyme, so the cell makes only what it needs.
- Immobilised enzyme (for example in alginate beads: sodium alginate + enzyme dripped into calcium chloride): reused, product not contaminated, more stable, continuous process; disadvantages are cost and slower diffusion of the substrate into the beads.
:::

:::links
- read: [CAIE A Level Biology: enzymes notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/enzymes/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Enzymes (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/3-enzymes/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of enzymes and inhibition
- read: [Metabolism and enzymes](https://openstax.org/books/biology-2e/pages/6-introduction) · OpenStax Biology 2e · free university textbook chapter on enzyme regulation, beyond the syllabus in places
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find enzyme questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Membrane structure and cell signalling](#bio.membranes) shows how the lipids and proteins of a membrane control what enters and leaves the cell.
