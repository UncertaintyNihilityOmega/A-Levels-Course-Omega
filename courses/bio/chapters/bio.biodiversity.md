@chapter bio.biodiversity
@title Biodiversity and sampling
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 5–6 hours
@summary Biodiversity is the variety of life, and it can be measured at the level of ecosystems, of species and of genes. You will learn how to define an ecosystem and a niche, why sampling must be random, how to use frame quadrats, line and belt transects and mark-release-recapture (Lincoln index), how to calculate Simpson's index of diversity, and how to use Spearman's rank and Pearson's correlation to test how biotic and abiotic factors affect where organisms live.

:::why
You cannot protect, manage or even describe an ecosystem until you can measure it. How many species live in a wood, how many fish are in a lake, and whether a plant is more common near a path are questions biologists answer with samples, not by counting everything. This chapter gives you the methods, the formulae and the statistics, and the skill of saying what a result does and does not show. Ecology questions in Papers 4 and 5 are mostly about data and planning.
:::

**Before you start**, you should know the levels of organisation and species from [Biology foundations](#bio.f.basics) and [Classification](#bio.classification), and null hypotheses and significance from [Variation and the t-test](#bio.variation).

:::try Warm-up
Q: Put these in order, from the smallest to the largest: community, organism, ecosystem, population. (from [Biology foundations](#bio.f.basics))
A: Organism, population, community, ecosystem.
Q: Define the term species, using the biological species concept. (from [Classification](#bio.classification))
A: A group of organisms with similar features that can interbreed to produce fertile offspring and are reproductively isolated from other species.
Q: In a t-test the calculated value of t is larger than the critical value at p = 0.05. What do you conclude? (from [Variation and the t-test](#bio.variation))
A: There is a significant difference between the means. Reject the null hypothesis: the difference is unlikely to be due to chance.
:::

## Ecosystems, habitats and niches

:::def Ecosystem
A relatively self-contained, functioning unit made up of the community of living organisms (the biotic factors) and the non-living physical and chemical environment (the abiotic factors) in an area, interacting with each other.
:::

:::def Niche
The role of a species in an ecosystem: where it lives, what it feeds on or uses, when it is active, and how it interacts with other species and with the abiotic environment.
:::

Three other terms are often muddled with these two.

:::def Habitat
The place where a species lives within an ecosystem, for example a rock pool or the leaf litter of a wood.
:::

:::def Population
All the organisms of one species living in the same place at the same time.
:::

:::def Community
All the populations of different species living and interacting in the same place at the same time.
:::

:::analogy Address and job
The habitat of a species is its **address** (where it lives). Its niche is its **job** (what it does and uses: its food, its feeding time, its place in the food web, and its effect on others). Two species can have the same address but different jobs, and they can live together.
:::

Abiotic factors include light, temperature, water, pH, salinity and the soil. Biotic factors are the living parts: food, competitors, predators, parasites and pathogens. Together they decide where a species can live and how many there are.

Two species that use exactly the same resources compete, and one is usually better at it, so the other declines or moves away. Species that live together therefore tend to have **different niches**: different foods, different feeding times or different places. This is why ecological data are about **distribution** (where a species is found) and **abundance** (how many there are).

## Biodiversity at three levels

:::def Biodiversity
The variety of life, measured at three levels: the number and range of different ecosystems and habitats; the number of species and their relative abundance; and the genetic variation within each species.
:::

1. **Ecosystem and habitat diversity.** How many different ecosystems and habitats there are in an area, and how varied they are. An island with woodland, grassland, a river and a coast has more habitat diversity than one covered with a single crop.
2. **Species diversity.** This has two parts:
   - **Species richness**: the number of different species in an area.
   - **Species evenness**: how similar the numbers of individuals of each species are (the relative abundance). A community in which most individuals belong to one species has low evenness.
3. **Genetic diversity.** The variety of alleles within each species. A population with many alleles has more raw material for adaptation to a change; a population reduced to a few individuals has little.

:::eg A biologist wants to assess the biodiversity of a tropical island. Describe three levels at which she can do this.
She can record the number and range of different ecosystems and habitats on the island, such as forest, mangrove swamp, grassland and coral reef. [B1]

She can record the number of different species and their relative abundance, to find the species richness and evenness. [B1]

She can compare the genetic variation within each species, for example the number of different alleles of selected genes in samples of each species. [B1]
:::

Two communities can have the same species richness and very different diversity. Imagine two fields of 100 insects each, with five species in each. In one field each species has 20 individuals. In the other, one species has 96 and the other four have one each. The number of species is the same, but the second field has a very low evenness. **Simpson's index of diversity**, later in this chapter, takes both richness and evenness into account in a single number.

## Why sampling must be random

An ecologist cannot count every organism in a wood or a shore. It would take too long, cost too much and damage the habitat. Instead, she measures a **sample**: a small part of the area, and uses it to estimate the whole.

:::key What makes a good sample
- It is **representative**: it must reflect the whole area, not only the parts that look rich or are easy to reach.
- It is **large enough**: more samples reduce the effect of chance.
- It is **unbiased**: the person collecting must not choose where to sample.
:::

:::def Random sampling
Choosing sample sites so that every part of the area has an equal chance of being chosen, with no influence from the person sampling.
:::

**Random sampling avoids bias.** If a student places her quadrats "where the plants are", or avoids the nettles, her results overestimate the abundance and do not describe the area. Bias is a problem that repeating more times does not remove.

To sample randomly in a field:

:::steps
1. Mark out the area with two long tape measures along two sides, at right angles, to make a grid (for example 20 m by 20 m).
2. Use a calculator or computer to generate **random numbers**, or a table of random numbers. Take them in pairs to give an *x* coordinate and a *y* coordinate.
3. Go to each coordinate and place the quadrat there. If a pair falls outside the area, or repeats, reject it and take another.
4. Record in each quadrat what the investigation needs (the number of plants, the percentage cover, or the species present).
:::

<figure class="fig small"><svg viewBox="0 0 340 312" role="img" aria-label="A square grid 20 metres by 20 metres, with lines every 5 metres. Five small squares, numbered 1 to 5, mark the quadrats placed at random coordinates: 1 at x 3, y 16; 2 at x 11, y 7; 3 at x 17, y 13; 4 at x 6, y 4; 5 at x 14, y 18."><path class="ax" d="M46 270L46 30"/><path class="ax" d="M46 270L286 270"/><text class="ts" x="46" y="286" text-anchor="middle">0</text><text class="ts" x="38" y="273" text-anchor="end">0</text><path class="ln-m thin dash" d="M106 270L106 30"/><path class="ln-m thin dash" d="M46 210L286 210"/><text class="ts" x="106" y="286" text-anchor="middle">5</text><text class="ts" x="38" y="213" text-anchor="end">5</text><path class="ln-m thin dash" d="M166 270L166 30"/><path class="ln-m thin dash" d="M46 150L286 150"/><text class="ts" x="166" y="286" text-anchor="middle">10</text><text class="ts" x="38" y="153" text-anchor="end">10</text><path class="ln-m thin dash" d="M226 270L226 30"/><path class="ln-m thin dash" d="M46 90L286 90"/><text class="ts" x="226" y="286" text-anchor="middle">15</text><text class="ts" x="38" y="93" text-anchor="end">15</text><path class="ln-m thin dash" d="M286 270L286 30"/><path class="ln-m thin dash" d="M46 30L286 30"/><text class="ts" x="286" y="286" text-anchor="middle">20</text><text class="ts" x="38" y="33" text-anchor="end">20</text><rect class="f1 s-acc sw2" x="76" y="72" width="12" height="12"/><text class="tl" x="94" y="82">1</text><rect class="f1 s-acc sw2" x="172" y="180" width="12" height="12"/><text class="tl" x="190" y="190">2</text><rect class="f1 s-acc sw2" x="244" y="108" width="12" height="12"/><text class="tl" x="262" y="118">3</text><rect class="f1 s-acc sw2" x="112" y="216" width="12" height="12"/><text class="tl" x="130" y="226">4</text><rect class="f1 s-acc sw2" x="208" y="48" width="12" height="12"/><text class="tl" x="204" y="58" text-anchor="end">5</text><text class="tl" x="286" y="304" text-anchor="end">x / m</text><text class="tl" x="6" y="14">y / m</text></svg><figcaption>Random sampling in a 20 m by 20 m area. Pairs of random numbers give an x and a y coordinate, and a quadrat (small square) is placed at each. The numbers show the order: (3, 16), (11, 7), (17, 13), (6, 4) and (14, 18).</figcaption></figure>

**How many samples?** Take enough to get a stable result. A good way is to calculate a **running mean** (the mean of all the quadrats so far) after each quadrat. At first it changes a lot. When it stops changing much, you have enough quadrats.

:::eg A student estimated the percentage cover of daisies in a field with random quadrats. After each quadrat she calculated the running mean. Use the results to decide whether she had taken enough quadrats.

| quadrat number | cover / % | running mean / % |
|---|---|---|
| 1 | 30 | 30.0 |
| 2 | 18 | 24.0 |
| 3 | 26 | 24.7 |
| 4 | 34 | 27.0 |
| 5 | 22 | 26.0 |
| 6 | 28 | 26.3 |
| 7 | 24 | 26.0 |
| 8 | 26 | 26.0 |
| 9 | 25 | 25.9 |
| 10 | 27 | 26.0 |

Each running mean is the total so far divided by the number of quadrats. After quadrat 4: \((30 + 18 + 26 + 34) \div 4 = 27.0\%\).

The running mean changed by up to 6 percentage points in the first four quadrats (from 30.0% to 24.0%), but from quadrat 5 onwards it stays between 25.9% and 26.3%. So the mean is stable at about 26%, and ten quadrats were enough for this field. If the running mean had still been drifting, she would have needed more.
:::

:::warn Random is not "haphazard"
Throwing a quadrat over your shoulder, or walking in a zigzag, is not random: people tend to throw to places they can reach, and avoid awkward spots. Use **random numbers**.
:::

Random sampling suits an area that is the same all over. Where the environment changes in one direction, such as up a shore, the sampling is done **systematically** along a line, as in the next section.

## Frame quadrats

:::def Frame quadrat
A square frame of known area (often 0.25 m² or 1 m²), placed on the ground, inside which the organisms are counted or their cover is estimated. Many are divided into a grid of 100 smaller squares.
:::

A quadrat gives three measures of abundance:

:::formula Measures from quadrats
- **Frequency** (%):

\[\text{frequency} = \frac{\text{quadrats containing the species}}{\text{total quadrats}} \times 100\]

- **Density** (per m²):

\[\text{density} = \frac{\text{total individuals}}{\text{quadrats} \times \text{area of one quadrat}}\]

- **Percentage cover** = the percentage of the quadrat covered by the species (count the small squares of the grid that are more than half covered).
:::

Use **frequency** when individuals are hard to count; use **density** when each individual can be counted; use **percentage cover** for plants such as grasses or mosses that grow in patches and cannot be counted as individuals.

:::eg A student placed twenty 0.25 m² quadrats at random in a field of area 2400 m². She counted 84 daisy plants in all, and found daisies in 14 of the quadrats. Calculate the frequency and the density of daisies, and estimate the number of daisy plants in the field.
**Frequency:**

\[\begin{aligned} \text{frequency} &= \frac{14}{20} \times 100 \\ &= 70\% \end{aligned}\]

**Density.** The total area sampled is \(20 \times 0.25 = 5.0\,\mathrm{m^2}\).

\[\begin{aligned} \text{density} &= \frac{84}{5.0} \\ &= 16.8\,\mathrm{m^{-2}} \end{aligned}\]

**Estimate for the field**: multiply the density by the area of the field.

\[\begin{aligned} \text{population} &= 16.8 \times 2400 \\ &= 40\,320 \end{aligned}\]

so about 40 000 daisy plants. This is an estimate from a sample, and a different set of random quadrats would give a different answer, which is why the sample must be large enough.
:::

:::lab Estimating the abundance of a plant species with random quadrats
**Aim**: estimate the density, frequency and percentage cover of a plant species in a field.

:::steps
1. Lay two tape measures at right angles along two sides of the area to make a grid.
2. Generate pairs of random numbers for the *x* and *y* coordinates and place a 0.25 m² quadrat at each position (at least 10, and more if the running mean has not levelled off).
3. In each quadrat count the plants of the species (or the number of grid squares more than half covered) and record the count.
4. Calculate the frequency, the mean number per quadrat, the density and the percentage cover. Multiply the density by the area for the population estimate.
:::

**Variables**: the same quadrat size, the same person estimating cover, and the same time of year and day for all quadrats. **Control**: the sample must not be chosen by eye.

**Sources of error**: plants overlapping the edges (decide a rule, such as counting those touching the top and left edges only); plants hard to tell apart; different people estimating cover differently; the area may not be uniform. Improve by increasing the number of quadrats, using one observer, and using a quadrat with a 100-square grid.

**Safety**: avoid ticks and stinging plants (long sleeves and trousers, gloves); wash hands after fieldwork; check for allergies; take care near water and on slopes.
:::

## Transects

An environment often changes steadily in one direction, for example from the sea up a shore, from a woodland edge into the open, or away from a pollution source. A **transect** records how the organisms change along this gradient. It is a **systematic** sample: the positions are fixed on a line at regular distances, not random.

:::def Line transect
A tape measure laid in a straight line across an area. The organisms touching the line at set points (or along its whole length) are recorded.
:::

:::def Belt transect
A strip of ground, of a set width (for example 1 m), along a line. Organisms are recorded in the strip, usually by placing a quadrat at regular intervals along the line (an interrupted belt transect).
:::

<figure class="fig small"><svg viewBox="0 0 340 214" role="img" aria-label="A side view of a shore. On the left is the sea, and to the right the land rises steadily. A dashed tape measure runs up the slope from the sea, and five numbered squares, 1 to 5, are quadrats placed at equal intervals along it. An arrow underneath points to the right and is labelled increasing distance from the sea."><rect class="f2 s-acc2 sw2" x="10" y="130" width="60" height="35"/><text class="tl" x="40" y="152" text-anchor="middle">sea</text><path class="fm s-acc sw2" d="M70 130L330 50L330 165L70 165Z"/><path class="ln-m thin dash" d="M70 130L330 50"/><rect class="f1 s-acc sw2" x="93" y="113.769" width="14" height="14"/><text class="tl" x="100" y="105.769" text-anchor="middle">1</text><rect class="f1 s-acc sw2" x="143" y="98.3846" width="14" height="14"/><text class="tl" x="150" y="90.3846" text-anchor="middle">2</text><rect class="f1 s-acc sw2" x="193" y="83" width="14" height="14"/><text class="tl" x="200" y="75" text-anchor="middle">3</text><rect class="f1 s-acc sw2" x="243" y="67.6154" width="14" height="14"/><text class="tl" x="250" y="59.6154" text-anchor="middle">4</text><rect class="f1 s-acc sw2" x="293" y="52.2308" width="14" height="14"/><text class="tl" x="300" y="44.2308" text-anchor="middle">5</text><path class="ln" d="M70 184L326 184" marker-end="url(#ah)"/><text class="tl" x="70" y="202">increasing distance from the sea</text></svg><figcaption>A belt transect up a shore. A tape measure runs up the slope, and a quadrat is placed at each regular interval (squares 1 to 5). Each quadrat records the species and a measurement of an abiotic factor, so the change along the gradient can be seen.</figcaption></figure>

- A **line transect** is quick and simple, and gives presence or absence along the line.
- A **belt transect** gives more detail (density or cover in each quadrat) and a larger sample, but takes longer.
- Both show **zonation**: bands of different species along a gradient, caused by changes in an abiotic factor such as salt, light, water or temperature.
- To be reliable, take **several transects** in randomly chosen positions along the gradient, and use the mean.

:::lab Investigating how the distribution of a species changes along a gradient
**Aim**: find how the abundance of a ground plant changes with distance from the edge of a wood into an open field.

:::steps
1. Lay a tape measure along the line of the gradient, starting at the edge of the wood (distance 0).
2. Place a quadrat at fixed intervals (every 5 m for 50 m).
3. In each quadrat record the abundance (count or percentage cover) and measure one abiotic factor, for example light intensity or soil moisture.
4. Repeat on at least three transects at randomly chosen places along the edge of the wood. Calculate the mean at each distance.
5. Plot abundance (and the abiotic factor) against distance, and use a statistical test (below) to test for correlation.
:::

**Variables**: the independent variable is the distance; the dependent variables are abundance and the abiotic factor; standardise quadrat size, the time, the person, and the direction of the transect. **Source of error**: a single transect may not represent the area; positions that are not exactly at the right intervals. **Safety**: as for quadrats.
:::

## Mark-release-recapture

Quadrats cannot count animals that move. For these, ecologists use **mark-release-recapture**, which estimates a population size with the **Lincoln index**.

:::steps
1. **Capture** as many animals as possible in a set time (pitfall traps, nets or hand searching) and count them: \(n_1\).
2. **Mark** each animal in a way that does not harm it or make it easier for predators to see (a dot of non-toxic paint on the underside of a shell, a small clip or tag).
3. **Release** them where they were caught and **wait** long enough for the marked animals to mix with the rest of the population.
4. **Recapture** a second sample, in the same way, and count the animals in it: \(n_2\). Count how many of them are marked: \(m_2\).
5. Calculate the population size with the Lincoln index.
:::

:::formula Lincoln index
\[N = \frac{n_1 \times n_2}{m_2}\]

\(N\) = estimated population size; \(n_1\) = number caught and marked in the first sample; \(n_2\) = number caught in the second sample; \(m_2\) = number of marked animals in the second sample. The formula is given in the exam.
:::

**Why it works.** If the marked animals have mixed evenly, the proportion marked in the second sample equals the proportion marked in the whole population: \(\dfrac{m_2}{n_2} = \dfrac{n_1}{N}\). Rearranging gives \(N = \dfrac{n_1 n_2}{m_2}\).

:::analogy Marked beans
Take 50 beans from a large jar, mark them with a pen, and put them back and stir. Scoop out 60 beans: if 10 are marked, then one in six of the beans in the jar is marked, and the 50 marked beans must be about one-sixth of the jar. The jar holds about 300 beans. Counting one handful has let you estimate the whole jar.
:::

**The assumptions**, which must be true for the answer to be reliable:
- The marked animals have **mixed randomly** with the rest of the population.
- The **population is closed**: no significant births, deaths, immigration or emigration between the two samples.
- The mark is **not lost** or hidden, and **does not affect survival** (it does not make the animal more visible to predators, or harm it).
- Every animal has an **equal chance of capture** in the second sample.

:::eg Freshwater shrimps in a stream were sampled with a net. In the first sample, 48 shrimps were caught, marked with a harmless dye and released. A day later, 60 shrimps were caught, and 12 of them were marked. Estimate the size of the population and state two assumptions.
\[\begin{aligned} N &= \frac{n_1 \times n_2}{m_2} \\ &= \frac{48 \times 60}{12} \\ &= 240 \end{aligned}\]

So there are about 240 shrimps in the stretch of stream. As a check: 12 of the 60 caught the second time (one fifth) were marked, so the 48 marked shrimps are about one fifth of the population: \(48 \times 5 = 240\).

Assumptions: the marked shrimps mixed evenly with the unmarked ones; no shrimps were born, died, entered or left the stretch during the day; the dye did not harm the shrimps or make them easier for fish to see.
:::

:::lab Estimating the size of a population of woodlice or snails
**Aim**: estimate the number of animals in an area using mark-release-recapture.

:::steps
1. Collect as many animals as possible from the area in 20 minutes and count them (\(n_1\)).
2. Mark each with a small spot of non-toxic paint or correction fluid on the underside of the shell or body (where a predator will not see it).
3. Release them at the place they were found, and leave for a period (for example one day) so they mix.
4. Collect a second sample in the same way, for the same time (\(n_2\)), and count the marked (\(m_2\)).
5. Calculate \(N\).
:::

**Sources of error**: marks wear off or are eaten; paint changes survival; trap-shy or trap-happy animals; the animals migrate; counting errors; the second sample not random. Improve by using more than one pair of samples, using non-toxic paint on the underside, waiting long enough, and taking larger samples.

**Safety**: handle animals gently and return them to their habitat; wash hands; avoid toxic paints.
:::

:::exam Lincoln index errors
The most common slip is putting \(m_2\) on top. \(m_2\) is **always the divisor**. If your answer is smaller than \(n_1\) or \(n_2\), it is wrong: the population cannot be smaller than either sample. State the **assumptions** by name when asked to evaluate, and say how each one could fail (for example, "if the marked animals are more visible and are eaten, \(m_2\) is too low, so \(N\) is overestimated").
:::

Try it: enter your own numbers in the widget below and see how the estimate changes when you catch more marked animals.

:::html
<div class="widget" data-w="bio-diversity" data-mode="lincoln"></div>
:::

## Simpson's index of diversity

Species richness alone does not describe diversity, as the two fields of insects above show. **Simpson's index of diversity (D)** includes both the number of species and how evenly the individuals are spread among them.

:::formula Simpson's index of diversity
\[D = 1 - \sum \left(\frac{n}{N}\right)^2\]

\(n\) = number of individuals of one species; \(N\) = total number of individuals of all species; \(\sum\) = add up the values for every species. The formula is given in the exam.
:::

Calculate D in four steps. For each species find \(n/N\); square it; add up all the squares; subtract the sum from 1.

D lies between **0 and 1**.
- **D near 1**: high diversity. Many species, with the individuals spread fairly evenly. Such a community is usually stable: if one species declines, others still fill its role.
- **D near 0**: low diversity. Few species, or one species with most of the individuals. Such a community is vulnerable to change such as disease, pollution or a change of climate.

:::eg Real context, river pollution: invertebrates were sampled upstream and downstream of a sewage outlet. Use Simpson's index to compare the two sites.
| species | upstream n | downstream n |
|---|---|---|
| mayfly nymph | 24 | 0 |
| stonefly nymph | 18 | 0 |
| caddis larva | 21 | 0 |
| freshwater shrimp | 20 | 0 |
| flatworm | 17 | 0 |
| sludge worm | 0 | 62 |
| bloodworm | 0 | 28 |
| rat-tailed maggot | 0 | 6 |
| leech | 0 | 2 |
| water louse | 0 | 2 |

Both sites have 100 individuals in 5 species, so \(N = 100\) at each, and \(n/N\) is the percentage as a fraction.

**Upstream.**

\[\begin{aligned} \sum\left(\tfrac{n}{N}\right)^2 &= 0.24^2 + 0.18^2 + 0.21^2 + 0.20^2 + 0.17^2 \\ &= 0.0576 + 0.0324 + 0.0441 + 0.0400 + 0.0289 \\ &= 0.2030 \\ D &= 1 - 0.2030 = 0.797 \end{aligned}\]

**Downstream.**

\[\begin{aligned} \sum\left(\tfrac{n}{N}\right)^2 &= 0.62^2 + 0.28^2 + 0.06^2 + 0.02^2 + 0.02^2 \\ &= 0.3844 + 0.0784 + 0.0036 + 0.0004 + 0.0004 \\ &= 0.4672 \\ D &= 1 - 0.4672 = 0.533 \end{aligned}\]

**Conclusion.** The upstream site has the higher D (0.797 compared with 0.533), so it is more diverse. The number of species is the same, so the difference is due to **evenness**: downstream, sludge worms are 62% of all individuals. Mayfly, stonefly and caddis larvae need clean, oxygen-rich water, so their absence downstream, and the dominance of species that tolerate low oxygen, suggest that the sewage has reduced the oxygen in the water.
:::

:::warn Mistakes with Simpson's index
- Squaring \(n\) or \(N\) instead of \(n/N\). Work out \(n/N\) first, then square **each** one.
- Forgetting to subtract from 1. The sum of the squares is the chance that two organisms picked at random are the same species. D is the chance that they are different.
- Using the number of species as \(N\). \(N\) is the total number of **individuals**.
- Comparing D for samples of very different size or sampling effort: a small sample gives a misleading value.
:::

:::eg Spot the error: a sample contained three species with 30, 20 and 10 individuals. Calculate Simpson's index of diversity D. [3]
A student wrote this answer.

Line 1: N = 30 + 20 + 10 = 60.
Line 2: \(\sum (n/N)^2 = (30/60)^2 + (20/60)^2 + (10/60)^2 = 0.25 + 0.1111 + 0.0278 = 0.3889\).
Line 3: So D = 0.389.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: 0.389 is the sum of the squares, but D is 1 minus this sum. The chance that two individuals are the same species is 0.389; D is the chance that they differ. That mark is lost [B0].**

Correct Line 3: \(D = 1 - 0.3889 = 0.611\). With that change the answer scores 3 marks.
:::

Try it: the widget below calculates D for two sites at once. Add and remove species and watch what happens to D as the counts become more even.

:::html
<div class="widget" data-w="bio-diversity" data-mode="simpson"></div>
:::

## Correlation: biotic and abiotic factors

Why is a species found where it is? Ecologists suspect an abiotic factor (light, soil moisture, pH, temperature, salinity) or a biotic factor (a competitor, a predator, food) and look for a **correlation** between the factor and the abundance.

:::def Correlation
A relationship between two variables in which they tend to change together. In a positive correlation both increase together; in a negative correlation one increases as the other decreases.
:::

:::steps
1. Collect **pairs** of measurements at the same sampling points (for example soil moisture and number of plants per quadrat, along a transect).
2. Draw a **scatter graph** first. It shows whether the points follow a straight line, a curve, or no pattern, and whether the relationship is positive or negative.
3. Choose the test (see the box below). State the **null hypothesis**: there is no correlation between the two variables.
4. Calculate the **correlation coefficient**.
5. Compare its size (ignoring the sign) with the **critical value** at p = 0.05 for the number of pairs. If it is larger than the critical value, the correlation is **significant**: reject the null hypothesis.
:::

The coefficient runs from **−1 to +1**. The sign gives the direction (+ both rise together, − one rises while the other falls). The size gives the strength: close to 1 is strong, close to 0 is weak or none.

:::key Which test?
**Pearson's linear correlation** (r): both variables are continuous and normally distributed, and the scatter graph shows a straight-line relationship. Use at least 5 pairs, preferably 10 or more.

**Spearman's rank correlation** (\(r_s\)): the data are not normally distributed, or can only be ranked, or the relationship is increasing or decreasing but not a straight line. Use more than 5 pairs, preferably 10 to 30. The points are independent and selected at random.
:::

In the exam, the formulae are printed in the question, and a table of critical values (or the critical value itself) is given. The **number of degrees of freedom is not given**, and for a correlation you use the **number of pairs** *n* to find the critical value.

### Spearman's rank correlation

:::formula Spearman's rank correlation coefficient
\[r_s = 1 - \frac{6\sum D^2}{n^3 - n}\]

\(D\) = the difference between the two ranks of each pair; \(n\) = number of pairs. The formula is given in the exam.
:::

To rank a set of values, give 1 to the smallest, 2 to the next, and so on (do the same for both variables, always smallest = 1). If two or more values are **tied**, give each the **mean of the ranks** they would have had.

:::eg Eight quadrats were placed along a transect across a dune slack, and the soil water content and the number of rush plants in each were recorded. Use Spearman's rank correlation to test whether the number of rushes is correlated with soil water content. The critical value for n = 8 at p = 0.05 is 0.738.

The null hypothesis is that there is no correlation between soil water content and the number of rushes.

| soil water / % | rushes per quadrat | rank (water) | rank (rushes) | D | D² |
|---|---|---|---|---|---|
| 4 | 2 | 1 | 1 | 0 | 0 |
| 6 | 5 | 2.5 | 3 | −0.5 | 0.25 |
| 6 | 3 | 2.5 | 2 | 0.5 | 0.25 |
| 9 | 8 | 4 | 5 | −1 | 1 |
| 11 | 7 | 5 | 4 | 1 | 1 |
| 13 | 12 | 6 | 7 | −1 | 1 |
| 15 | 14 | 7.5 | 8 | −0.5 | 0.25 |
| 15 | 10 | 7.5 | 6 | 1.5 | 2.25 |

**Ranks.** The two soil water values of 6 would have ranks 2 and 3, so each gets 2.5. The two values of 15 would have ranks 7 and 8, so each gets 7.5.

**Calculate.** Add the last column:

\[\begin{aligned} \sum D^2 &= 0 + 0.25 + 0.25 + 1 \\ &\quad + 1 + 1 + 0.25 + 2.25 \\ &= 6.0 \end{aligned}\]

\[\begin{aligned} r_s &= 1 - \frac{6 \times 6.0}{8^3 - 8} \\ &= 1 - \frac{36}{504} \\ &= 0.929 \end{aligned}\]

**Conclusion.** \(r_s = 0.929\) is larger than the critical value of 0.738, so there is a significant positive correlation between soil water content and the number of rushes, and we reject the null hypothesis. Rushes are more abundant where the soil is wetter. This does not by itself show that water causes the pattern.
:::

<figure class="fig small"><svg viewBox="0 0 340 236" role="img" aria-label="A scatter graph of the number of rushes per quadrat against soil water content in percent. Eight points rise from left to right: (4, 2), (6, 5), (6, 3), (9, 8), (11, 7), (13, 12), (15, 14) and (15, 10). The points show a positive relationship."><path class="ax" d="M48 20L48 190L326 190"/><path class="ln" d="M48 190L48 194"/><text class="ts" x="48" y="207" text-anchor="middle">0</text><path class="ln" d="M124.111 190L124.111 194"/><text class="ts" x="124.111" y="207" text-anchor="middle">5</text><path class="ln" d="M200.222 190L200.222 194"/><text class="ts" x="200.222" y="207" text-anchor="middle">10</text><path class="ln" d="M276.333 190L276.333 194"/><text class="ts" x="276.333" y="207" text-anchor="middle">15</text><path class="ln" d="M44 190L48 190"/><text class="ts" x="40" y="193" text-anchor="end">0</text><path class="ln" d="M44 149L48 149"/><text class="ts" x="40" y="152" text-anchor="end">4</text><path class="ln" d="M44 108L48 108"/><text class="ts" x="40" y="111" text-anchor="end">8</text><path class="ln" d="M44 67L48 67"/><text class="ts" x="40" y="70" text-anchor="end">12</text><path class="ln" d="M44 26L48 26"/><text class="ts" x="40" y="29" text-anchor="end">16</text><circle class="f1 s-acc sw2" cx="108.889" cy="169.5" r="4.5"/><circle class="f1 s-acc sw2" cx="139.333" cy="138.75" r="4.5"/><circle class="f1 s-acc sw2" cx="139.333" cy="159.25" r="4.5"/><circle class="f1 s-acc sw2" cx="185" cy="108" r="4.5"/><circle class="f1 s-acc sw2" cx="215.444" cy="118.25" r="4.5"/><circle class="f1 s-acc sw2" cx="245.889" cy="67" r="4.5"/><circle class="f1 s-acc sw2" cx="276.333" cy="46.5" r="4.5"/><circle class="f1 s-acc sw2" cx="276.333" cy="87.5" r="4.5"/><text class="tl" x="322" y="226" text-anchor="end">soil water content / %</text><text class="tl" x="6" y="12">rushes per quadrat</text></svg><figcaption>The data for the Spearman example. The points rise from left to right: the number of rushes tends to be higher where the soil is wetter. The relationship is increasing, but not exactly a straight line, so a rank correlation is suitable.</figcaption></figure>

Try it: the widget below ranks any set of pairs (up to 15), gives the ranks with ties averaged, \(\sum D^2\) and \(r_s\), and compares \(r_s\) with the critical value you type in. Change a value and see how the ranks move.

:::html
<div class="widget" data-w="bio-diversity" data-mode="spearman"></div>
:::

:::tip Check the sign
Before you calculate, look at the scatter graph. If the points rise from left to right, the answer must be positive, and if they fall it must be negative. A sign that does not match the graph shows a ranking error. Also check that the differences \(D\), before squaring, add up to 0.
:::

### Pearson's linear correlation

:::formula Pearson's correlation coefficient
\[r = \frac{\sum xy - n\bar{x}\bar{y}}{(n-1)\,s_x s_y}\]

\(x\) and \(y\) = the two variables; \(\bar{x}\) and \(\bar{y}\) = their means; \(s_x\) and \(s_y\) = their standard deviations (using \(n - 1\)); \(n\) = number of pairs. The formula is given in the exam.
:::

In Papers 4 and 5, the question often gives part of the working (for example \(\sum xy\), the means and the standard deviations), and you finish the calculation.

:::eg The light intensity (arbitrary units) at the floor of a woodland and the percentage cover of moss were measured at eight sites. Use Pearson's correlation to test the relationship. The critical value for n = 8 at p = 0.05 is 0.707.
The null hypothesis is that there is no correlation between light intensity and moss cover.

| light intensity (x) | moss cover / % (y) |
|---|---|
| 1 | 3 |
| 2 | 5 |
| 3 | 4 |
| 4 | 8 |
| 5 | 7 |
| 6 | 10 |
| 7 | 9 |
| 8 | 12 |

**Sums and means.** \(\sum x = 36\) and \(\sum y = 58\), so \(\bar{x} = 4.5\) and \(\bar{y} = 7.25\). The sum of the products is:

\[\begin{aligned} \sum xy &= 1\times3 + 2\times5 + 3\times4 + 4\times8 \\ &\quad + 5\times7 + 6\times10 + 7\times9 + 8\times12 \\ &= 311 \end{aligned}\]

The standard deviations (with \(n-1\)) are \(s_x = 2.449\) and \(s_y = 3.105\).

**Numerator.**

\[\begin{aligned} \sum xy - n\bar{x}\bar{y} &= 311 - 8 \times 4.5 \times 7.25 \\ &= 311 - 261 \\ &= 50 \end{aligned}\]

**Denominator and r.**

\[\begin{aligned} (n-1)\,s_x s_y &= 7 \times 2.449 \times 3.105 \\ &= 53.23 \\ r &= \frac{50}{53.23} \\ &= 0.939 \end{aligned}\]

**Conclusion.** \(r = 0.939\) is greater than the critical value of 0.707, so there is a significant positive correlation: moss cover increases with light intensity. Reject the null hypothesis.
:::

### Correlation is not causation

A significant correlation shows that two variables change together. It does **not** show that one causes the other.
- Both may be caused by a third factor. Two seaweeds may be found together because both need the same wave exposure.
- The cause may run the other way.
- It may be a coincidence, especially with few points.

To show cause, you need an **experiment** in which one variable is changed and the others are kept the same. The sensible conclusion from a correlation is: "there is a significant positive correlation between *x* and *y*", and then a suggested explanation, such as "may be because …".

:::exam Writing the conclusion of a statistical test
Four lines earn the marks: (1) the **null hypothesis** ("no correlation between …"); (2) the **calculated value** compared with the **critical value** at p = 0.05 ("0.929 > 0.738"); (3) the decision ("so there is a significant positive correlation, and the null hypothesis is rejected"); (4) a **caution** where asked ("correlation does not prove cause"). Use "significant", not "proved".
:::

## Planning an investigation in the field

Paper 5 questions ask you to plan an investigation, with the variables, the method and the analysis.

:::eg Plan an investigation to find out whether the abundance of a plant species, plantain, changes with distance from a footpath across a field.
Use the distance from the edge of the path as the independent variable and the abundance of plantain (number per quadrat or percentage cover) as the dependent variable. [B1]

Lay a tape measure at right angles to the path, from the path edge outwards to 20 m, and place a 0.25 m² quadrat every 2 m along it (a belt transect). [B1]

In each quadrat, count the plantain plants (or estimate the percentage cover with a grid of 100 squares). [B1]

Repeat on at least three transects at randomly chosen positions along the path (found with random numbers), and calculate the mean abundance at each distance. [B1]

Standardise the quadrat size, the time of year and day, the person estimating the cover, and the slope and soil type of the area. [B1]

Measure an abiotic factor (such as soil compaction or moisture) at each quadrat, and plot a scatter graph; use Spearman's rank correlation to test the correlation between distance and abundance, comparing the result with the critical value for the number of pairs (null hypothesis: no correlation). [B1]

Take care to avoid ticks and stinging plants (long sleeves, gloves) and wash hands afterwards; do the work away from traffic. [B1]
:::

## Practice

:::try Start easy, finish at exam standard
Q: State the difference between a habitat and a niche.
A: A habitat is the place where a species lives. A niche is the role of the species in the ecosystem, including what it eats or uses, when it is active and how it interacts with other species and the abiotic environment.
Q: Two woods each contain 200 trees of 6 species. In one wood 190 trees are of a single species. State which wood has the greater species evenness and explain.
A: The wood with the trees spread more equally among the six species has the greater evenness. Evenness measures how similar the numbers of individuals of each species are; the wood with 190 trees of one species has very low evenness.
Q: Explain why quadrat positions should be chosen with random numbers, not by choosing places that look typical.
A: Choosing by eye is biased: it can favour places with more (or fewer) plants and does not represent the whole area. Random numbers give every part of the area an equal chance of being sampled, so the result is representative and unbiased.
Q: A student placed thirty 0.25 m² quadrats at random in a field of 1800 m². She counted 66 buttercup plants in total, and found buttercups in 18 quadrats. Calculate the frequency and the density, and estimate the number of buttercups in the field.
A: Frequency \(= 18 \div 30 \times 100 = 60\%\). Density \(= 66 \div (30 \times 0.25) = 8.8\,\mathrm{m^{-2}}\). Estimate \(= 8.8 \times 1800 = 15\,840\), about 16 000.
Q: State when a belt transect is better than random quadrats.
A: When the environment changes steadily in one direction (a gradient), for example from the sea up a shore, because a transect records how abundance and species change along the gradient.
Q: In a mark-release-recapture investigation of snails, 35 were marked, and in the second sample 28 snails were caught, 7 of them marked. Calculate the estimated population.
A: \(N = 35 \times 28 \div 7 = 140\).
Q: A student catches 35 beetles in her first sample and 28 in her second, and calculates \(N = 20\). Explain how she can tell that her answer is wrong, and suggest what she did.
A: The population cannot be smaller than the number caught in a sample, so 20 is impossible. She probably put \(m_2\) in the numerator or divided the wrong way round; \(m_2\) is the divisor.
Q: A sample of three species has 15, 15 and 30 individuals. Calculate Simpson's index of diversity.
A: \(N = 60\); \((15/60)^2 + (15/60)^2 + (30/60)^2 = 0.0625 + 0.0625 + 0.25 = 0.375\); \(D = 1 - 0.375 = 0.625\).
Q: State what a Simpson's index of diversity close to 0 shows about a community.
A: Low diversity: very few species, or one species dominating, so the community is likely to be unstable and vulnerable to change.
Q: Give the ranks for the values 3, 5, 5, 8 (smallest = 1).
A: 1, 2.5, 2.5, 4. The two values of 5 would have had ranks 2 and 3, so each gets the mean, 2.5.
Q: A correlation coefficient of −0.82 is larger in size than the critical value. State what it shows, and what it does not show.
A: There is a significant negative correlation: as one variable increases, the other decreases. It does not show that one variable causes the change in the other.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ (a) Define the term ecosystem. (b) Define the term niche. (c) State how a habitat differs from a niche.
A: (a) A self-contained, functioning unit of a community of living organisms and the non-living environment, interacting. [B1]
(b) The role of a species in an ecosystem. [B1]
(c) A habitat is the place where it lives; a niche is what the species does and uses (its role). [B1]
Q: [3 marks] ★ A student used twenty-five 1 m² quadrats at random in a meadow. She found clover in 20 of them, and counted 150 clover plants in all. Calculate (a) the frequency of clover and (b) its density.
A: (a) \(20 \div 25 \times 100 = 80\%\) [A1]
(b) Density \(= 150 \div (25 \times 1)\) [M1] \(= 6.0\,\mathrm{m^{-2}}\) [A1]
Q: [4 marks] ★★ A student wants to estimate the number of dandelions on a lawn that is 20 m by 15 m. Describe how she should use quadrats to get a reliable estimate.
H: Think about the grid, the random numbers, how many quadrats and what she finally multiplies.
A: Mark out a grid with tape measures along two sides, and use random numbers as coordinates to place each quadrat. [B1]
Count the dandelions in each quadrat, and take enough quadrats for the running mean to level off (or at least 10). [B1]
Calculate the mean number per quadrat and the density per m². [B1]
Multiply the density by the area of the lawn (300 m²) to estimate the total number. [B1]
Q: [5 marks] ★★ A population of woodlice in a garden was sampled by mark-release-recapture. In the first sample 55 woodlice were caught and marked. In the second sample 40 were caught, of which 8 were marked. (a) Calculate the estimated population size. (b) Some of the paint wore off between the two samples. State and explain the effect on the estimate. (c) Suggest why the paint used to mark the woodlice should not be a bright colour.
H: For (b), what happens to the number of marked woodlice that are recognised in the second sample?
H: For (c), think about predators finding a marked animal.
A: (a) \(N = 55 \times 40 \div 8\) [M1] \(= 275\) [A1]
(b) Marked woodlice that had lost their paint would not be counted as marked, so \(m_2\) would be too low. [B1]
\(m_2\) is the divisor, so the estimate would be too high. [B1]
(c) A bright mark could make the marked animals more visible to predators, so fewer would survive, and \(m_2\) would be too low and \(N\) too high. [B1]
Q: [6 marks] ★★ The numbers of individuals of five species of ground beetle were counted in a mixed woodland (X) and in a conifer plantation (Y), both sampled in the same way.

| species | woodland X | plantation Y |
|---|---|---|
| 1 | 12 | 40 |
| 2 | 15 | 8 |
| 3 | 9 | 6 |
| 4 | 14 | 4 |
| 5 | 10 | 2 |

(a) Calculate Simpson's index of diversity for woodland X. The value for plantation Y is 0.52. (b) Compare the two sites. (c) Suggest a reason for the difference.
H: Both sites have 60 individuals. Work out \(n/N\) for each species at X.
A: (a) \(N = 60\) and the squares of \(n/N\) are 0.04, 0.0625, 0.0225, 0.0544 and 0.0278 [M1]; their sum is \(0.2072\) [A1]
\(D = 1 - 0.2072 = 0.793\) [A1]
(b) Woodland X has the higher D (0.793 compared with 0.52), so it is more diverse. Both have five species, so the difference is the evenness: in Y, one species has 40 of 60 individuals. [B1] [B1]
(c) The plantation has one tree species and fewer habitats and food sources, so one or two beetle species dominate. [B1]
Q: [5 marks] ★★ The number of slugs per quadrat was recorded at seven distances from a hedge. Spearman's rank correlation was used.

| distance from hedge / m | slugs per quadrat | rank (distance) | rank (slugs) | D | D² |
|---|---|---|---|---|---|
| 12 | 34 | 1 | 7 | −6 | 36 |
| 18 | 29 | 2 | 5 | −3 | 9 |
| 25 | 30 | 3.5 | 6 | −2.5 | 6.25 |
| 25 | 22 | 3.5 | 3 | 0.5 | 0.25 |
| 31 | 25 | 5 | 4 | 1 | 1 |
| 40 | 14 | 6 | 2 | 4 | 16 |
| 47 | 9 | 7 | 1 | 6 | 36 |

(a) The sum of \(D^2\) is 104.5. Calculate \(r_s\). (b) The critical value for n = 7 at p = 0.05 is 0.786. State the conclusion. (c) State why this does not prove that the hedge causes slugs to be more common nearby.
H: \(n^3 - n = 7^3 - 7 = 336\).
A: (a) \(r_s = 1 - (6 \times 104.5) \div 336\) [M1] \(= -0.866\) [A1]
(b) The size 0.866 is greater than the critical value 0.786, so there is a significant negative correlation: there are fewer slugs further from the hedge. [B1]
(c) Correlation does not show cause; another factor that changes with distance from the hedge (such as soil moisture or shelter) may be responsible. [B1] [B1]
Q: [6 marks] ★★★ The number of limpets per m² and the distance up a shore from the low-tide mark were recorded at ten sites. Pearson's correlation coefficient is to be calculated: \(\bar{x} = 11.0\,\mathrm{m}\), \(\bar{y} = 45.1\) limpets per m², \(s_x = 6.055\), \(s_y = 11.20\), \(\sum xy = 4374\) and \(n = 10\). (a) Calculate r. (b) The critical value for n = 10 at p = 0.05 is 0.632. State the conclusion. (c) Suggest an abiotic factor that could explain the pattern, and one reason the sites should be chosen using a transect.
H: \(\sum xy - n\bar{x}\bar{y} = 4374 - 10 \times 11.0 \times 45.1\).
H: Denominator: \((n-1) \times s_x \times s_y\).
A: (a) \(\sum xy - n\bar{x}\bar{y} = 4374 - 4961 = -587\) [M1]
\((n-1)s_xs_y = 9 \times 6.055 \times 11.20 = 610.3\) [M1]
\(r = -587 \div 610.3 = -0.962\) [A1]
(b) The size 0.962 is greater than 0.632, so there is a significant negative correlation: limpet density decreases up the shore. [B1]
(c) Any one abiotic factor that changes up the shore, for example time out of water (drying), or temperature range. [B1]
A transect is used because the environment changes steadily in one direction, so a systematic sample along the gradient shows the change. [B1]
Q: [7 marks] ★★★ A nature reserve has a rare butterfly. In year 1, 30 butterflies were caught, marked and released, and in a second sample 25 butterflies were caught, of which 5 were marked. In year 5, the same method gave \(n_1 = 24\), \(n_2 = 20\) and \(m_2 = 8\). (a) Calculate the estimated population in each year. (b) Describe the change. (c) A population that has fallen to a small size loses genetic diversity. Explain why, and why low genetic diversity makes the population more vulnerable to disease.
H: Think about genetic drift in a small population and the alleles that remain.
A: (a) Year 1: \(30 \times 25 \div 5 = 150\) [M1] [A1]
Year 5: \(24 \times 20 \div 8 = 60\) [A1]
(b) The estimated population fell from 150 to 60, a decrease of 60%. [B1]
(c) In a small population, alleles can be lost by chance (genetic drift), and fewer individuals carry the alleles, so genetic diversity falls. [B1]
With low genetic diversity, there are few different alleles, so it is less likely that any individuals carry an allele that gives resistance to a disease, and the disease could kill most of the population. [B1] [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Ten sites along a mountain slope were sampled for the number of species of insect per site. Spearman's rank correlation is used to test the link with altitude.

| altitude / m | insect species |
|---|---|
| 200 | 41 |
| 300 | 38 |
| 500 | 29 |
| 500 | 33 |
| 700 | 30 |
| 800 | 22 |
| 1000 | 25 |
| 1200 | 15 |
| 1400 | 17 |
| 1600 | 9 |

(a) Rank both sets of data and calculate \(r_s\). (b) The critical value for n = 10 at p = 0.05 is 0.648. State your conclusion.
H: Rank the altitude from 1 for the lowest; the two values of 500 share the ranks 3 and 4.
H: Rank the species numbers from 1 for the smallest; there are no ties.
H: \(\sum D^2 = 321.5\); \(n^3 - n = 990\).
A: (a) Ranks of altitude: 1, 2, 3.5, 3.5, 5, 6, 7, 8, 9, 10. [B1]
Ranks of species: 10, 9, 6, 8, 7, 4, 5, 2, 3, 1. [B1]
\(\sum D^2 = 321.5\) [M1]
\(r_s = 1 - (6 \times 321.5) \div 990\) [M1] \(= -0.948\) [A1]
(b) The size 0.948 is greater than 0.648, so there is a significant negative correlation: fewer insect species at higher altitude (reject the null hypothesis). [B1]
Q: [5 marks] ★★★ Site A has four species with 97, 1, 1 and 1 individuals. Site B has two species with 50 and 50 individuals. (a) Calculate Simpson's index of diversity for each site. (b) Site B has fewer species. Explain why its D is higher.
H: Work with \(n/N\) as decimals: for site A, N = 100.
A: (a) Site A: \(0.97^2 + 3 \times 0.01^2 = 0.9409 + 0.0003 = 0.9412\) [M1], so \(D = 1 - 0.9412 = 0.059\) [A1]
Site B: \(0.5^2 + 0.5^2 = 0.5\), so \(D = 0.50\) [A1]
(b) D depends on the evenness as well as the number of species. [B1]
Site A has more species, but 97% of its individuals are of one species (very low evenness), and site B has its individuals shared equally. [B1]
:::

:::quiz
? Which is the best definition of a niche?
+ the role of a species in an ecosystem
- the place where a species lives
- all the populations in an area
- the number of species in an area
> The place is the habitat. All the populations make a community. Niche is what the species does and uses.
? Why is random sampling used?
+ It avoids bias, so the sample represents the whole area.
- It makes the sample bigger.
- It guarantees that every species will be found.
- It removes the need for repeats.
> Random sampling gives every part of the area an equal chance of being sampled. It does not make the sample larger and does not remove chance variation.
? A transect is chosen rather than random quadrats when
+ there is a gradient in the environment.
- the area is the same all over.
- the organisms move quickly.
- the species are very rare.
> A transect records how the organisms change along a gradient. Moving animals need mark-release-recapture.
? In mark-release-recapture, 40 animals are marked, then 30 are caught in a second sample, 10 of them marked. What is the estimated population?
+ 120
- 13
- 7.5
- 1200
> \(N = 40 \times 30 \div 10 = 120\). Using \(40 \times 10 \div 30 \approx 13\) puts \(m_2\) and \(n_2\) the wrong way round, 7.5 comes from \(30 \times 10 \div 40\), and 1200 forgets to divide by \(m_2\).
? Which assumption is needed for the Lincoln index?
+ No migration into or out of the population between samples.
- The marked animals stay together.
- The first sample is larger than the second.
- The marks make the animals easier to see.
> The population must be closed, and the marked animals must mix, with no effect from the mark.
? What does a Simpson's index of diversity D close to 1 show?
+ many species with individuals spread fairly evenly
- one species with most of the individuals
- a very small sample
- a community that is about to collapse
> D near 1 means high diversity, which usually means a stable community. D near 0 is the low-diversity case.
? A sample has two species with 70 and 30 individuals. What is D?
+ 0.42
- 0.58
- 0.21
- 0.50
> \(D = 1 - (0.7^2 + 0.3^2) = 1 - 0.58 = 0.42\). 0.58 is the sum of the squares only, which is the common slip.
? The data are not normally distributed, but the scatter graph shows that one variable generally increases with the other. Which test?
+ Spearman's rank correlation
- Pearson's correlation
- chi-squared test
- t-test
> Spearman needs only rankable data and a trend. Pearson needs normally distributed data and a straight-line relationship. Chi-squared is for counts in categories and t compares two means.
? A significant positive correlation is found between the number of ice creams sold and the number of sunburn cases. What is the best conclusion?
+ The two variables change together; both may depend on a third factor such as sunshine.
- Ice cream causes sunburn.
- Sunburn causes people to buy ice cream.
- The data are not valid because the result is not 1.
> Correlation does not prove cause. Both rise on sunny days.
:::

:::checklist What you can now do
- [ ] I can define the terms ecosystem and niche, and distinguish them from habitat, population and community.
- [ ] I can explain that biodiversity is assessed at the levels of ecosystems and habitats, species (richness and relative abundance) and genetic variation.
- [ ] I can explain why random sampling is important, and place quadrats using random coordinates.
- [ ] I can describe and use frame quadrats (frequency, density, percentage cover) and line and belt transects.
- [ ] I can describe and use mark-release-recapture, calculate the Lincoln index and state its assumptions.
- [ ] I can calculate Simpson's index of diversity D and state what high and low values mean.
- [ ] I can use Spearman's rank correlation, including tied ranks, and Pearson's correlation, and compare the result with a critical value.
- [ ] I can explain how biotic and abiotic factors affect distribution and abundance, and why correlation is not causation.
- [ ] I can plan a field investigation with random sampling, variables, repeats and analysis.
:::

:::recap
- Ecosystem: community plus abiotic environment. Niche: the role of a species. Habitat: where it lives. Population: one species; community: all species.
- Biodiversity: ecosystem and habitat diversity; species richness and evenness; genetic diversity.
- Random sampling (random-number coordinates) avoids bias; take enough quadrats for the running mean to level off. Use transects along a gradient.
- Quadrats: frequency = quadrats with the species ÷ total × 100; density = number ÷ (quadrats × area); percentage cover.
- Lincoln index \(N = n_1 n_2 / m_2\); assumptions: mixing, closed population, mark not lost or harmful, equal chance of capture.
- Simpson \(D = 1 - \sum (n/N)^2\), from 0 to 1; higher is more diverse and more stable. Square each \(n/N\), then subtract from 1.
- Correlation: scatter graph first. Pearson for normal, linear data; Spearman for ranks (ties get the mean rank): \(r_s = 1 - 6\sum D^2/(n^3 - n)\). Compare the size with the critical value for n pairs; larger is significant. Correlation is not causation.
:::

:::links
- read: [CAIE A Level Biology: classification and biodiversity notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/biodiversity-classification-conservation/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Classification, biodiversity and conservation (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/18-classification-biodiversity-and-conservation/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- read: [Population and community ecology](https://openstax.org/books/biology-2e/pages/45-introduction) · OpenStax Biology 2e · free university textbook chapter on populations, sampling and communities, beyond the syllabus in places
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of ecology and sampling
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · practise planning and analysis questions on sampling and statistics [unofficial]

Links checked 24 October 2026.
:::

Next: [Conservation](#bio.conservation) uses these measures to protect species and habitats.
