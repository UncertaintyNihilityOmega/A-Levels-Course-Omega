@chapter bio.variation
@title Variation and the t-test
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 4–5 hours
@summary No two individuals of a species are exactly alike. You will learn what causes variation (genes, the environment, or both), how discontinuous variation (distinct categories) differs from continuous variation (a range) and why continuous variation needs many genes, how to read a normal distribution and its spread, and how to use the t-test to decide whether the means of two samples really differ.

:::why
Natural selection, breeding and medicine all depend on variation. If every individual were the same, selection would have nothing to act on and a drug trial would have nothing to measure. But variation also makes data untidy: two groups of plants never have exactly the same mean height, even when nothing is different between them. The t-test is the tool that tells you whether a difference between two means is big enough to be real. Paper 4 asks you to explain the genetics of variation, and Papers 4 and 5 ask you to carry out and interpret a t-test.
:::

**Before you start**, you should know how meiosis produces different gametes from [Meiosis and genetic variation](#bio.meiosis), what a gene mutation is from [Protein synthesis and gene mutation](#bio.synthesis), and how to calculate a mean and draw a graph from [Maths skills for biology](#bio.maths).

:::try Warm-up
Q: State two events in meiosis that make the gametes of one person genetically different from each other. (from [Meiosis and genetic variation](#bio.meiosis))
A: Any two of: crossing over between homologous chromosomes in prophase I, independent assortment of homologous chromosomes in metaphase I (and of chromatids in metaphase II), and random fertilisation (which adds to the variation of the offspring).
Q: Why are the offspring produced by asexual reproduction genetically identical to their parent? (from [Chromosomes and the mitotic cell cycle](#bio.mitosis))
A: They are produced by mitosis, which copies the DNA exactly and shares it equally, so the daughter cells have the same alleles as the parent (apart from rare mutations).
Q: Five seedlings have heights of 8, 11, 9, 12 and 10 cm. Calculate the mean. (from [Maths skills for biology](#bio.maths))
A: \((8 + 11 + 9 + 12 + 10) \div 5 = 50 \div 5 = 10\,\mathrm{cm}\).
:::

## Causes of variation

:::def Phenotypic variation
Differences in the observable characteristics (phenotypes) of individuals of the same species. It is caused by genetic factors, by environmental factors, or by a combination of both.
:::

A **phenotype** is the sum of the effects of the genotype and the environment on the organism. Two questions can be asked about any difference between individuals: is it inherited, is it caused by the surroundings, or both?

### Genetic causes

Genetic variation comes from differences in **alleles**. The alleles are produced and shuffled in these ways:

- **Mutation** produces new alleles (see [Protein synthesis and gene mutation](#bio.synthesis)).
- **Meiosis** shuffles alleles into different combinations in the gametes: crossing over exchanges alleles between homologous chromosomes, and independent assortment of homologous pairs gives each gamete a different mixture of maternal and paternal chromosomes.
- **Random fertilisation** joins two gametes by chance, so each offspring has a unique combination of alleles from its parents.

Genetic variation is passed on to the next generation. Examples are ABO blood group, whether a person is a taster for a bitter chemical, and the colour of a pea flower.

### Environmental causes

Environmental variation is caused by the conditions the organism lives in. It is **not** inherited: it cannot be passed on to offspring in the genes. Examples are:

- **Diet and nutrition**: a child with too little protein grows less.
- **Light**: a plant grown in shade has longer, thinner stems and paler leaves than one grown in full light.
- **Soil minerals**: a plant with too little nitrate or magnesium has pale leaves.
- **Temperature**: some reptiles' eggs hatch as males at one temperature and as females at another; and some flowers, such as hydrangeas, change colour with the pH of the soil.
- **Accidents and learning**: a scar, or the language a person speaks.

### Genes and the environment together

Most features depend on both. The genes set the **potential**, and the environment decides how much of the potential is reached. Height is an example: tall parents tend to have tall children (genes), but a child who is malnourished will not reach the height that its genes allow (environment). Skin colour is another: the genes for melanin set a person's usual colour, but exposure to ultraviolet light increases melanin production (tanning).

| characteristic | genetic | environmental | both |
|---|---|---|---|
| ABO blood group | ✓ | | |
| height of a person | | | ✓ |
| mass of a person | | | ✓ (mostly environment) |
| skin colour | | | ✓ |
| a scar | | ✓ | |
| language spoken | | ✓ | |

:::eg Cuttings were taken from one rose plant and grown for a year at three different altitudes. The mean heights were 48 cm at 200 m, 35 cm at 800 m and 21 cm at 1400 m. Cuttings from ten different rose plants, all grown in the same garden, had heights from 31 cm to 52 cm. What do the two results show?
**Experiment 1**: all the cuttings came from one plant, so they are genetically identical (clones) and have the same alleles. The heights still differed, from 48 to 21 cm. So the difference must have been caused by the **environment**: the plants were in different conditions (temperature, soil, wind). [B1]

**Experiment 2**: the plants were grown in the same garden, so the environment was (nearly) the same, yet the heights differed from 31 to 52 cm. Since the plants were different individuals, they have different alleles. So the variation was caused by **genetic differences**. [B1]

Together the results show that height in roses is affected by **both** genes and the environment. [B1]
:::

## Discontinuous and continuous variation

:::def Discontinuous variation
Variation in which individuals fall into **distinct categories**, with no intermediate values. The characteristic is qualitative, or a small number of whole-number values. Examples are ABO blood group and the presence of a widow's peak.
:::

:::def Continuous variation
Variation in which individuals show a **complete range** of values between two extremes, with no distinct categories. The characteristic is measured on a scale. Examples are height, mass and leaf length.
:::

| | discontinuous variation | continuous variation |
|---|---|---|
| phenotypes | distinct categories | a full range between two extremes |
| intermediates | none | many |
| number of genes | one gene, or a few | many genes (polygenic) |
| effect of the environment | little or none | often large |
| how it is shown | bar chart (gaps between bars) | histogram (touching bars), or a smooth curve |
| shape of the data | separate bars | bell-shaped (normal distribution) |
| examples | ABO blood group, flower colour in peas | height, body mass, leaf length |

:::html
<figure class="fig small"><svg viewBox="0 0 340 424" role="img" aria-label="Two graphs. Graph A, a bar chart with gaps between the bars: the number of students in a sample of 200 with each blood group. O has 84, A has 76, B has 28 and AB has 12. Graph B, a histogram with touching bars: the heights of 100 students in 5 cm classes from 150 to 190 cm. The bars rise to a peak of 26 in the 170 to 175 cm class and fall away on each side in a bell shape."><text class="tl tb" x="10" y="16">A  Discontinuous: blood group</text><text class="tl" x="4" y="32">number of students</text><path class="ax" d="M44 50L44 150L326 150"/><text class="ts" x="38" y="154" text-anchor="end">0</text><text class="ts" x="38" y="106" text-anchor="end">50</text><path class="ax" d="M40 102L44 102"/><text class="ts" x="38" y="58" text-anchor="end">100</text><path class="ax" d="M40 54L44 54"/><rect class="f1 s-acc sw2" x="58" y="69.36" width="44" height="80.64"/><text class="tl" x="80" y="167" text-anchor="middle">O</text><rect class="f1 s-acc sw2" x="130" y="77.04" width="44" height="72.96"/><text class="tl" x="152" y="167" text-anchor="middle">A</text><rect class="f1 s-acc sw2" x="202" y="123.12" width="44" height="26.88"/><text class="tl" x="224" y="167" text-anchor="middle">B</text><rect class="f1 s-acc sw2" x="274" y="138.48" width="44" height="11.52"/><text class="tl" x="296" y="167" text-anchor="middle">AB</text><text class="tl" x="185" y="186" text-anchor="middle">blood group</text><text class="tl tb" x="10" y="222">B  Continuous: height of 100 students</text><text class="tl" x="4" y="238">number of students</text><path class="ax" d="M44 254L44 374L326 374"/><text class="ts" x="38" y="378" text-anchor="end">0</text><text class="ts" x="38" y="348" text-anchor="end">10</text><path class="ax" d="M40 344L44 344"/><text class="ts" x="38" y="318" text-anchor="end">20</text><path class="ax" d="M40 314L44 314"/><text class="ts" x="38" y="288" text-anchor="end">30</text><path class="ax" d="M40 284L44 284"/><rect class="f1 s-acc sw2" x="44" y="368" width="35" height="6"/><rect class="f1 s-acc sw2" x="79" y="356" width="35" height="18"/><rect class="f1 s-acc sw2" x="114" y="332" width="35" height="42"/><rect class="f1 s-acc sw2" x="149" y="302" width="35" height="72"/><rect class="f1 s-acc sw2" x="184" y="296" width="35" height="78"/><rect class="f1 s-acc sw2" x="219" y="326" width="35" height="48"/><rect class="f1 s-acc sw2" x="254" y="350" width="35" height="24"/><rect class="f1 s-acc sw2" x="289" y="362" width="35" height="12"/><text class="ts" x="44" y="393" text-anchor="middle">150</text><text class="ts" x="79" y="393" text-anchor="middle">155</text><text class="ts" x="114" y="393" text-anchor="middle">160</text><text class="ts" x="149" y="393" text-anchor="middle">165</text><text class="ts" x="184" y="393" text-anchor="middle">170</text><text class="ts" x="219" y="393" text-anchor="middle">175</text><text class="ts" x="254" y="393" text-anchor="middle">180</text><text class="ts" x="289" y="393" text-anchor="middle">185</text><text class="ts" x="324" y="393" text-anchor="middle">190</text><text class="tl" x="185" y="414" text-anchor="middle">height / cm</text></svg><figcaption>Invented class data. A: discontinuous variation is shown in a bar chart, with gaps because the groups are separate categories. B: continuous variation is shown in a histogram, with no gaps because height is a measurement on a scale; the bell shape is a normal distribution.</figcaption></figure>
:::

Use a **bar chart** for categories, with gaps between the bars to show that the categories are separate and cannot be put in a continuous order. Use a **histogram** for a measured quantity that has been grouped into classes: the classes touch, because there are no gaps between the values.

:::tip Choosing the chart
Ask whether the x-axis is a list of categories or a number line. Blood groups, colours and species names are categories: bar chart. Height, mass and length are numbers that can take any value on a scale: histogram (or a frequency polygon).
:::

## The genetic basis of discontinuous and continuous variation

### Discontinuous variation: one gene, or a few genes

Discontinuous variation is usually controlled by **one gene** (or a few genes) with a large effect. Each genotype gives a distinct phenotype, and the environment has little or no effect.

The ABO blood group is controlled by one gene with three alleles, \(I^A\), \(I^B\) and \(I^O\) (see [Monohybrid inheritance](#bio.inheritance)). The genotypes fall into four distinct phenotypes (A, B, AB and O). Nobody has a blood group "halfway" between A and B, and no amount of diet or training changes it.

### Continuous variation: many genes and the environment

Continuous variation is controlled by **many genes**, each with a small effect on the same characteristic. This is called **polygenic inheritance**. The effects of the alleles **add up** (they are additive). The environment also affects the characteristic.

A simple model shows how this gives a range. Suppose height is controlled by three genes. At each gene, one allele (a *contributing* allele) adds 2 cm and the other adds nothing. Two parents who are each heterozygous at all three genes produce gametes with every combination of the alleles. The number of contributing alleles in an offspring can be anywhere from 0 to 6:

| contributing alleles | extra height / cm | fraction of offspring |
|---|---|---|
| 0 | 0 | 1/64 |
| 1 | 2 | 6/64 |
| 2 | 4 | 15/64 |
| 3 | 6 | 20/64 |
| 4 | 8 | 15/64 |
| 5 | 10 | 6/64 |
| 6 | 12 | 1/64 |

Seven phenotypes are possible, with most of the offspring in the middle and few at the extremes: a bell shape. The more genes are involved, the more phenotypes there are and the smoother the curve. Real characteristics such as human height involve many genes. The **environment** (diet, health) then adds more variation to each genotype, so the range of heights becomes continuous with no steps.

:::key Genes and variation
- **Discontinuous**: one gene or a few with large effects; distinct categories; little environmental effect.
- **Continuous**: many genes (polygenic) each with a small, additive effect, **plus** environmental effects; a range of phenotypes in a bell-shaped distribution.
:::

:::eg A student claims that the height of tomato plants is controlled by many genes. Suggest how the shape of the distribution of heights in a sample of 300 plants grown from seeds of one variety supports this, and why the environment makes the distribution smoother.
The distribution is bell-shaped (a normal distribution) with a complete range of heights and no distinct categories. [B1]

This is the pattern expected when many genes, each with a small additive effect, control the characteristic, so that most plants have an intermediate number of tall alleles and few have very many or very few. [B1]

The environment (light, water, minerals) also affects height, so plants with the same genotype have different heights, which removes any steps between the classes and gives a smooth curve. [B1]
:::

## The normal distribution and spread

When a continuous characteristic is measured in a large sample, the histogram often has a bell shape. This is the **normal distribution**: symmetrical about the mean, with most values close to the mean and fewer values further away.

- The **mean** (\(\bar{x}\)) is the average value, the centre of the distribution.
- The **standard deviation** (\(s\)) measures the **spread** of the values around the mean. A small standard deviation means the values are close together; a large one means they are spread out.
- In a normal distribution, about 68% of the values lie within one standard deviation of the mean, and about 95% lie within two standard deviations.

:::formula Standard deviation (given in the exam when needed)
\[s = \sqrt{\dfrac{\sum (x - \bar{x})^2}{n - 1}}\]
\(x\) is each value, \(\bar{x}\) the mean of the sample, \(n\) the number of values in the sample, and \(\sum\) means "the sum of". Note \(n - 1\) in the denominator for a sample.
:::

:::eg Calculate the mean and the standard deviation of the number of seeds in six pods: 5, 7, 8, 6, 9, 7.
Calculate the mean, then the deviation of each value, squared.

\[\begin{aligned} \bar{x} &= \frac{5+7+8+6+9+7}{6} \\ &= \frac{42}{6} = 7 \end{aligned}\]

| seeds, \(x\) | \(x - \bar{x}\) | \((x - \bar{x})^2\) |
|---|---|---|
| 5 | −2 | 4 |
| 7 | 0 | 0 |
| 8 | 1 | 1 |
| 6 | −1 | 1 |
| 9 | 2 | 4 |
| 7 | 0 | 0 |

\(\sum (x - \bar{x})^2 = 10\). Use \(n - 1 = 5\):

\[\begin{aligned} s &= \sqrt{\frac{10}{5}} \\ &= \sqrt{2} = 1.41 \end{aligned}\]

So the mean is 7 seeds and the standard deviation is 1.41 seeds. About 95% of pods would be expected to have between \(7 \pm 2 \times 1.41\), or 4.2 to 9.8, seeds.
:::

### Standard error and 95% confidence limits

A sample mean is only an estimate of the mean of the whole population. The **standard error** (SE) shows how reliable that estimate is: it falls as the sample gets bigger.

:::formula Standard error and 95% confidence interval
\[\mathrm{SE} = \frac{s}{\sqrt{n}} \qquad 95\%\ \text{confidence interval} \approx \bar{x} \pm 2 \times \mathrm{SE}\]
:::

If the same population were sampled many times, about 95% of the intervals would contain the true population mean. The details of error bars are in [Statistics for biologists](#bio.stats).

## Comparing two means: the t-test

Two samples taken from the same population will almost never have exactly the same mean, just by chance. So when two groups have different means (leaves in sun and in shade, patients on a drug and on a placebo), the question is: is the difference real, or is it just the chance variation that you expect between samples? The **t-test** answers this.

:::def t-test
A statistical test used to compare the means of **two samples** of continuous data, to decide whether the difference between the means is significant (unlikely to be due to chance).
:::

### When can you use a t-test?

- You are comparing the means of **two** samples.
- The data are **continuous** measurements (length, mass, time), not categories or counts in classes.
- Each sample is taken from a population that is approximately **normally distributed**.
- The two samples have **similar standard deviations**.
- The samples are chosen at random. It can be used with fewer than 30 values in each sample.

If the data are in categories (for example the number of red and white flowers), a different test is needed: the chi-squared test in [Dihybrid crosses and the chi-squared test](#bio.dihybrid).

### The null hypothesis

Every statistical test starts with a **null hypothesis**: a statement that there is **no** significant difference. For a t-test comparing leaf lengths in sun and shade, the null hypothesis is "there is no significant difference between the mean length of sun leaves and the mean length of shade leaves". The test calculates how likely a difference as large as the one found would be if the null hypothesis were true.

### The formula

:::formula t-test (given in the exam when needed)
\[t = \frac{|\bar{x}_1 - \bar{x}_2|}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}\]
\(\bar{x}_1\), \(\bar{x}_2\): the means of the two samples. \(s_1\), \(s_2\): their standard deviations. \(n_1\), \(n_2\): the numbers of values. The bars \(|\ |\) mean "ignore the sign": always subtract the smaller mean from the larger.
:::

:::formula Degrees of freedom (not given in the exam)
\[\text{degrees of freedom} = n_1 + n_2 - 2\]
:::

The degrees of freedom tell you which row of the table of critical values to use. **You must work them out yourself**: the formula for them is not printed in the question.

:::steps
1. State the **null hypothesis**: there is no significant difference between the means of the two samples.
2. Calculate the **mean** and the **standard deviation** of each sample (using \(n - 1\)).
3. Calculate **t** from the formula.
4. Calculate the **degrees of freedom**, \(n_1 + n_2 - 2\).
5. Look up the **critical value** in the table, in the row for your degrees of freedom, at \(p = 0.05\).
6. **Compare**: if the calculated \(t\) is **greater than** the critical value, **reject** the null hypothesis. If it is less than, **accept** it.
7. Write the **conclusion** in words, in the context of the question.
:::

### What the conclusion means

The probability \(p = 0.05\) means a 5% chance. If the calculated \(t\) is greater than the critical value at \(p = 0.05\), the probability that a difference this large would arise by chance is **less than 5%**, so the difference is **significant**.

- Calculated \(t\) **greater** than the critical value: reject the null hypothesis. There **is** a significant difference between the means. The difference is unlikely (less than 5% probability) to be due to chance.
- Calculated \(t\) **less** than the critical value: accept the null hypothesis. There is **no** significant difference. Any difference between the means could be due to chance.

:::warn Four traps
**Degrees of freedom are \(n_1 + n_2 - 2\), not \(n - 1\).** The "\(n - 1\)" belongs to the standard deviation.
**A bigger t than the critical value rejects the null hypothesis.** Do not write "accept" for a significant result.
**"No significant difference" is not "the same".** Write "no significant difference", or "the difference could be due to chance". A difference that is almost significant is not significant.
**A t-test cannot prove a cause.** It shows that the difference is probably real. Whether the drug, or the light, caused it depends on the design of the experiment (the variables controlled).
:::

:::eg Leaf lengths (in mm) were measured in 8 leaves from a sunny site and 10 leaves from a shaded site of the same tree species. Use a t-test to find whether the mean leaf lengths differ significantly. Sun: 42, 45, 38, 44, 47, 41, 43, 46. Shade: 52, 49, 55, 51, 48, 54, 50, 53, 56, 47.
**Step 1: the null hypothesis.** There is no significant difference between the mean length of leaves in the sun and in the shade.

**Step 2: means and standard deviations.** Sun: \(\sum x = 346\), so \(\bar{x}_1 = 346 \div 8 = 43.25\,\mathrm{mm}\). Shade: \(\sum x = 515\), so \(\bar{x}_2 = 515 \div 10 = 51.5\,\mathrm{mm}\).

The squared deviations from the mean add up to 59.5 (sun) and 82.5 (shade). With \(n - 1\):

\[\begin{aligned} s_1 &= \sqrt{\frac{59.5}{7}} = 2.92\,\mathrm{mm} \\ s_2 &= \sqrt{\frac{82.5}{9}} = 3.03\,\mathrm{mm} \end{aligned}\]

The standard deviations are similar, so a t-test is suitable.

**Step 3: t.**

\[\begin{aligned} t &= \frac{|43.25 - 51.5|}{\sqrt{\dfrac{8.5}{8} + \dfrac{9.167}{10}}} \\ &= \frac{8.25}{\sqrt{1.0625 + 0.9167}} \\ &= \frac{8.25}{1.407} = 5.86 \end{aligned}\]

**Step 4: degrees of freedom.** \(8 + 10 - 2 = 16\).

**Step 5: critical value.** At \(p = 0.05\) with 16 degrees of freedom, the critical value is 2.12.

**Step 6: compare.** \(5.86 > 2.12\), so reject the null hypothesis.

**Conclusion.** There is a significant difference between the mean lengths of leaves in the sun and in the shade (\(p < 0.05\)). The difference is unlikely to be due to chance. Shade leaves are longer on average, by 8.25 mm.
:::

Try the widget with the sun and shade leaves, then change a value or two (or replace the samples with your own) and watch how \(t\) and the conclusion change. Notice that moving the means closer together, or making the spread bigger, lowers \(t\).

:::html
<div class="widget" data-w="bio-ttest" data-a="42, 45, 38, 44, 47, 41, 43, 46" data-b="52, 49, 55, 51, 48, 54, 50, 53, 56, 47"></div>
:::

:::exam Finishing a partly completed calculation
Papers 4 and 5 often print part of a t-test, for example the means and standard deviations, or the value of the sum of squares, and ask you to complete it. Read what is given, write the formula, substitute and work through the rest, showing each line: the working earns the method mark even if the arithmetic slips. Remember that the degrees of freedom and the conclusion are always yours to supply. Give \(t\) to 3 significant figures (one more than the data), then say "reject" or "accept" the null hypothesis and state the conclusion in the words of the question.
:::

:::eg Earthworms were collected from two soils and their lengths measured. Part of the working is given. Complete the t-test. Soil X: \(n = 9\), mean 12.4 cm, \(s = 1.6\) cm. Soil Y: \(n = 8\), mean 10.9 cm, \(s = 1.4\) cm.
**Step 1: the null hypothesis.** There is no significant difference between the mean lengths of earthworms in the two soils.

**Step 2: t.** Substitute into the formula (the means and the standard deviations are given):

\[\begin{aligned} t &= \frac{|12.4 - 10.9|}{\sqrt{\dfrac{1.6^2}{9} + \dfrac{1.4^2}{8}}} \\ &= \frac{1.5}{\sqrt{0.2844 + 0.2450}} \\ &= \frac{1.5}{0.7276} = 2.06 \end{aligned}\]

**Step 3: degrees of freedom.** \(9 + 8 - 2 = 15\). The critical value at \(p = 0.05\) is 2.13.

**Step 4: compare.** \(2.06 < 2.13\), so accept the null hypothesis.

**Conclusion.** There is no significant difference between the mean lengths of the earthworms in the two soils. The difference of 1.5 cm could be due to chance. It does not matter that \(t\) is close to the critical value: below it is below it. A larger sample might find a significant difference.
:::

:::eg Real context, a drug trial. Twenty volunteers with high blood pressure were divided at random into two groups of 10. One group took a new drug and the other a placebo. After four weeks the reduction in systolic blood pressure was recorded. The drug group had a mean reduction of 12.6 mmHg (\(s = 2.22\)). The placebo group had a mean reduction of 9.0 mmHg (\(s = 1.83\)). Is the drug effective?
**Null hypothesis.** There is no significant difference between the mean reduction in blood pressure with the drug and with the placebo.

\[\begin{aligned} t &= \frac{|12.6 - 9.0|}{\sqrt{\dfrac{2.22^2}{10} + \dfrac{1.83^2}{10}}} \\ &= \frac{3.6}{\sqrt{0.4928 + 0.3349}} \\ &= \frac{3.6}{0.9098} = 3.96 \end{aligned}\]

Degrees of freedom \(= 10 + 10 - 2 = 18\). The critical value at \(p = 0.05\) is 2.10. Since \(3.96 > 2.10\), reject the null hypothesis. [B1]

The mean reduction in blood pressure with the drug is significantly greater than with the placebo, so the difference is unlikely to be due to chance. [B1]

The result supports the idea that the drug works: the random choice of groups, and the placebo that controls for the effect of simply taking a tablet, mean that the difference is likely to be due to the drug. [B1]

Even so, a sample of 20 people is small. A larger trial in which neither the patients nor the doctors know who gets the drug would give stronger evidence. [B1]
:::

:::eg Spot the error: a student compared the lengths of two samples of 8 beech leaves, one from each of two trees, and obtained \(t = 3.20\). Complete the test. [3]
A student wrote this answer.

Line 1: Degrees of freedom \(= 8 + 8 - 2 = 14\), so the critical value at \(p = 0.05\) is 2.14.
Line 2: The calculated value of \(t\) (3.20) is greater than the critical value (2.14).
Line 3: So the null hypothesis is accepted: the difference between the means is due to chance.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: when the calculated \(t\) is greater than the critical value, the null hypothesis is rejected and the difference is significant. The conclusion contradicts the comparison in Line 2. That mark is lost [B0].**

Correct Line 3: "So the null hypothesis is rejected: there is a significant difference between the mean lengths of the leaves of the two trees (\(p < 0.05\))." With that change the answer scores 3 marks.
:::

:::lab Investigating continuous variation in two habitats
**Aim**: find out whether the mean length of leaves of one plant species differs between two habitats, such as a sunny hedge and a shaded wood.

:::steps
1. Choose the species and decide the leaf to measure (for example, the third leaf below the tip, so the leaves are of similar age).
2. Choose the sampling points **at random**: mark out a grid in each habitat and use random numbers from a calculator or table as the coordinates. Pick the nearest plant to each point, so you do not choose the leaves that look biggest.
3. Take at least 10 leaves from each habitat (more is better).
4. Measure the length of each leaf in the same way, with a ruler to the nearest millimetre, from the base of the blade to the tip.
5. Record the lengths in a table, calculate the mean and the standard deviation for each habitat, and draw histograms to check that the data are roughly normal.
6. Carry out a t-test.
:::

**Variables**: the independent variable is the habitat; the dependent variable is leaf length. Standardise the species, the age of the leaf, the part of the leaf measured, the way it is measured, and the time of year.

**Typical results**: the means differ by a few millimetres, the distributions overlap, and the t-test shows whether the difference is significant.

**Sources of error**: the habitats differ in many ways at once (light, soil, water), so a significant difference cannot be put down to light alone; leaves may curl or be damaged; measurement to the nearest millimetre limits precision; a bias towards bigger leaves if the sampling is not random. Improvements: random sampling with larger samples, measuring light intensity and soil moisture in each habitat, and using leaves from several plants.

**Safety**: avoid poisonous plants and wear gloves; follow the site rules; wash your hands after handling plants and soil.
:::

## Practice

:::try Start easy, finish at exam standard
Q: Classify each of these as discontinuous or continuous variation: (a) the number of petals on a daisy, 12 to 34; (b) the presence or absence of a sickle cell allele; (c) the length of a pea pod.
A: (a) Continuous (a complete range of values; it can be put on a scale). (b) Discontinuous (two categories: present or absent). (c) Continuous (measured on a scale, with many values).
Q: Explain why a person's skin colour shows both genetic and environmental variation.
A: Genes (alleles for the production of melanin) set the usual skin colour, and differ between people. Exposure to ultraviolet light in the environment increases melanin production (tanning), so people with the same genes can look different.
Q: A student draws a graph of the number of students of each eye colour in a class. Name the correct type of graph and give one feature of it.
A: A bar chart, because eye colour is a category. The bars have gaps between them.
Q: Describe the genetic difference between a characteristic that shows discontinuous variation and one that shows continuous variation.
A: Discontinuous variation is controlled by one gene or a few genes with large effects. Continuous variation is controlled by many genes (polygenic), each with a small additive effect.
Q: Calculate the standard deviation of the masses 10, 12, 14 and 16 g.
A: Mean \(= 13\) g. Squared deviations: 9, 1, 1, 9, sum \(= 20\). \(s = \sqrt{20 \div 3} = 2.58\) g.
Q: Two samples have 12 and 9 values. State the degrees of freedom for a t-test comparing their means.
A: \(12 + 9 - 2 = 19\).
Q: The calculated value of t is 2.48. The critical value at \(p = 0.05\) is 2.09. State the conclusion.
A: The calculated value is greater than the critical value, so reject the null hypothesis: there is a significant difference between the means, unlikely to be due to chance.
Q: Give two conditions that must be met before a t-test can be used.
A: Any two of: two samples of continuous data; each sample approximately normally distributed; similar standard deviations; random sampling.
Q: A student calculated \(t = 1.2\) with 10 degrees of freedom (critical value 2.23) and concluded that "the drug has no effect". Explain what is wrong with this wording.
A: The test shows only that there is no significant difference between the means in this sample; the difference could be due to chance. It does not prove that the drug has no effect. A larger sample might show a significant difference.
Q: Explain why random fertilisation is a cause of variation.
A: Any male gamete can fuse with any female gamete, and each gamete has a different combination of alleles, so each zygote has a unique combination of alleles.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Dairy cows of the same breed give different amounts of milk. State and explain two environmental causes of this variation, and one genetic cause.
A: Environmental: the diet of the cow (the amount and quality of food) affects the amount of milk. [B1] The health of the cow (disease) or the milking routine. [B1]
Genetic: different cows have different alleles for milk production, from mutation, meiosis and fertilisation. [B1]
Q: [4 marks] ★★ In a plant, fruit mass is controlled by two genes, A and B, each with two alleles. Each allele that is shown as a capital letter adds 5 g, so a plant AABB has a mass of 20 g above the base. Two plants of genotype AaBb are crossed. (a) State how many different masses are possible in the offspring and give the mass of the most common type. (b) State the fraction of offspring with the greatest mass.
H: Count the number of capital letters, from 0 to 4.
H: In (b), the probability of AABB is \(\tfrac14 \times \tfrac14\).
A: (a) Five masses (0, 5, 10, 15 and 20 g). [B1]
The most common has 2 capital letters, so 10 g above the base (6 of the 16 combinations). [B1]
(b) AABB needs AB gametes from both parents: \(\tfrac14 \times \tfrac14\) [M1] \(= \tfrac{1}{16}\). [A1]
Q: [5 marks] ★★ The table shows the masses of the seeds of one variety of bean, in classes.

| seed mass / g | number of seeds |
|---|---|
| 0.40 – 0.49 | 4 |
| 0.50 – 0.59 | 14 |
| 0.60 – 0.69 | 33 |
| 0.70 – 0.79 | 30 |
| 0.80 – 0.89 | 15 |
| 0.90 – 0.99 | 4 |

(a) State the type of variation shown and the type of graph used to display it. (b) Describe the distribution, using the data. (c) Suggest how the environment of the parent plant could contribute to the variation in seed mass.
H: Which class has the most seeds? Is the pattern symmetrical?
A: (a) Continuous variation, shown in a histogram. [B1]
(b) The distribution is bell-shaped (a normal distribution). [B1]
The highest number of seeds, 33, is in the class 0.60–0.69 g. [B1]
It is roughly symmetrical, with few seeds at the extremes (4 in the lightest class and 4 in the heaviest). [B1]
(c) Differences in the water, light or soil minerals available to the parent plant affect how much food is stored in the seeds. [B1]
(Also credit: the position of the seed in the pod; the temperature; genetic differences between plants.)
Q: [6 marks] ★★★ A student compared the heights of seedlings of one species grown with and without a fertiliser. The heights were measured in mm after 10 days. Fertiliser: 27, 30, 26, 29, 24, 31, 28 (\(n = 7\), mean 27.86 mm, \(s = 2.41\) mm). No fertiliser: 23, 26, 21, 25, 24, 27, 22, 25 (\(n = 8\), mean 24.13 mm, \(s = 2.03\) mm). (a) State the null hypothesis. (b) Calculate \(t\). (c) State the degrees of freedom, use the table of critical values at \(p = 0.05\) below, and state a conclusion.

| degrees of freedom | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|
| critical value | 2.20 | 2.18 | 2.16 | 2.14 | 2.13 |

H: Write the formula, then substitute \(s_1^2\) and \(s_2^2\) into \(s^2 \div n\) for each sample.
H: Degrees of freedom \(= n_1 + n_2 - 2\).
A: (a) There is no significant difference between the mean height of seedlings with fertiliser and without fertiliser. [B1]
(b) \(t = \dfrac{|27.86 - 24.13|}{\sqrt{\dfrac{2.41^2}{7} + \dfrac{2.03^2}{8}}}\) [M1]
Denominator \(= \sqrt{0.8297 + 0.5151} = \sqrt{1.3448} = 1.160\) [M1]
\(t = 3.73 \div 1.160 = 3.22\) [A1]
(c) Degrees of freedom \(= 7 + 8 - 2 = 13\), so the critical value is 2.16. [B1]
\(3.22 > 2.16\), so reject the null hypothesis: there is a significant difference between the heights of seedlings with and without fertiliser. [B1]
Q: [5 marks] ★★ Two groups of 9 and 9 patients were given a high dose and a low dose of a pain relief drug. The mean times until the pain returned were 5.4 h and 4.9 h, and \(t\) was calculated as 1.10. (a) State the degrees of freedom. (b) The critical value at \(p = 0.05\) is 2.12. State and explain the conclusion. (c) Suggest one way to improve the reliability of the investigation.
H: Is 1.10 less than or greater than 2.12?
A: (a) \(9 + 9 - 2 = 16\). [B1]
(b) The calculated \(t\) (1.10) is less than the critical value (2.12), so accept the null hypothesis. [B1]
There is no significant difference in the mean time before the pain returned; the difference of 0.5 h could be due to chance. [B1]
(c) Use more patients in each group (a larger sample), or repeat the trial with different patients. [B1]
It also helps to select the patients at random and to match them for age and sex. [B1]
Q: [6 marks] (#bio.meiosis) ★★★ Monozygotic (identical) twins and dizygotic (non-identical) twins have both been used to study variation. A study compared the heights of pairs of twins reared together: the mean difference in height within pairs was 1.7 cm for monozygotic twins and 4.4 cm for dizygotic twins. Another study found that the mean difference in height between monozygotic twins reared apart was 1.9 cm, while the mean difference between unrelated people of the same sex and age was 7.8 cm (all the values are illustrative). (a) Explain why the height differences within monozygotic pairs are smaller than within dizygotic pairs. (b) Explain what the second study shows about the causes of variation in height. (c) Explain why dizygotic twins are genetically different from each other.
H: How many zygotes do monozygotic twins come from?
A: (a) Monozygotic twins come from one zygote, so they have identical genotypes, while dizygotic twins have different alleles. [B1]
Since they are reared together, environmental effects are similar, so the smaller difference in monozygotic pairs shows that genes affect height. [B1]
(b) Twins reared apart have identical genes but different environments, and their heights are much more similar (1.9 cm apart) than those of unrelated people (7.8 cm), so genes have a large effect on height. [B1]
The twins still differ by 1.9 cm although their genes are identical, so the environment (for example diet) also affects height. [B1]
(c) Dizygotic twins come from two eggs fertilised by two different sperm, so they have different combinations of alleles. [B1]
These combinations are produced by crossing over and independent assortment in meiosis and by random fertilisation. [B1]
Q: [6 marks] (#bio.dihybrid) ★★★ An ecologist counted snails in two habitats and recorded the number of each shell colour: yellow, brown and pink. She wants to find out whether the shell colours differ significantly between habitats. (a) Explain why a t-test is not suitable. (b) Name a more suitable test and state what the null hypothesis would be. (c) Explain why shell colour is an example of discontinuous variation, and suggest how it is inherited.
H: What kind of data is "number of snails of each colour"?
A: (a) The data are counts in categories (nominal data), not continuous measurements. [B1]
A t-test compares the means of continuous data; it cannot be used for the numbers of snails of each colour. [B1]
(b) The chi-squared test (comparing observed and expected numbers). [B1]
The null hypothesis is that there is no significant difference between the observed numbers of each shell colour and those expected, in the two habitats (the frequency of each colour is the same). [B1]
(c) The snails fall into distinct categories with no intermediates. [B1]
It is probably controlled by one gene with a few alleles (with large effects, and little effect from the environment). [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Two groups of 12 plants each have mean heights of 48.0 cm and 52.0 cm, and both have \(s = 4.0\) cm. (a) Calculate the standard error of each mean. (b) Calculate the 95% confidence interval of each mean using \(\bar{x} \pm 2 \times \mathrm{SE}\). (c) Calculate \(t\), state the degrees of freedom and decide whether the difference is significant at \(p = 0.05\) (critical value 2.07 at 22 degrees of freedom). (d) A student says: "The confidence intervals overlap, so the difference cannot be significant." Comment.
H: SE \(= s \div \sqrt{n}\).
H: In (d), compare the lower end of one interval with the upper end of the other, and then with your conclusion in (c).
A: (a) \(\mathrm{SE} = 4.0 \div \sqrt{12} = 1.15\) cm for each. [B1]
(b) \(48.0 \pm 2.31\) gives 45.7 to 50.3 cm, and \(52.0 \pm 2.31\) gives 49.7 to 54.3 cm. [B1]
(c) \(t = \dfrac{4.0}{\sqrt{16.0 \div 12 + 16.0 \div 12}} = 4.0 \div 1.633 = 2.45\) [M1] with \(12 + 12 - 2 = 22\) degrees of freedom. [A1]
\(2.45 > 2.07\), so reject the null hypothesis: the difference is significant. [B1]
(d) The student is wrong: the intervals overlap slightly (49.7 to 50.3 cm) but the t-test shows a significant difference. A small overlap of two 95% confidence intervals can occur even when the difference is significant. [B1]
Q: [6 marks] ★★★ A field biologist measured the antler length of male deer on two islands. Island P (n = 6): 61, 63, 60, 62, 64, 62 cm. Island Q (n = 6): 58, 66, 52, 71, 49, 76 cm. The mean for both islands is 62 cm. (a) Explain why a t-test would not be a suitable way to compare the islands, even though the means are the same. (b) Suggest how the two distributions might differ in a histogram. (c) Suggest one reason why the spread on island Q might be greater. (d) State what the standard deviations show about the two islands.
H: Calculate roughly how far each value is from 62 on each island.
A: (a) The means are equal, so the t-test would find no difference, but the two samples have very different spreads (standard deviations), and the t-test requires similar standard deviations. [B1]
(b) Island P would give a narrow, tall histogram; island Q a wide, low one. [B1]
(c) Island Q may have a greater range of food supply or age structure, or a greater genetic variation. [B1]
(d) The standard deviation for P is small (about 1.4 cm) and for Q large (about 11 cm). [B1]
So the deer on island Q are much more variable in antler length. [B1]
This shows that the same mean can hide very different variation, so the spread should always be reported with the mean. [B1]
:::

:::quiz
? Which characteristic shows discontinuous variation?
+ ABO blood group
- adult height
- the mass of a seed
- the length of a leaf
> Blood group falls into four distinct categories controlled by one gene. Height, mass and length are measured on a scale and show continuous variation.
? Continuous variation is caused by
+ many genes with small additive effects and the environment.
- one gene with two alleles and no effect from the environment.
- the environment only.
- mutations that happen only in gametes.
> Continuous variation is polygenic, with the environment adding more variation. One gene with large effects gives discontinuous variation.
? A graph shows the number of people with each of four blood groups. Which graph is correct?
+ A bar chart with gaps between the bars.
- A histogram with touching bars.
- A line graph through the tops of the bars.
- A scatter graph.
> Blood group is a category, so a bar chart with gaps is correct. Histograms are for continuous data in classes.
? Which statement about environmental variation is correct?
+ It is not caused by differences in alleles, so it is not passed to offspring in the genes.
- It is caused by mutation in the gametes.
- It is always continuous variation.
- It affects plants but not animals.
> Environmental variation comes from conditions such as diet, light and temperature, not from alleles, so it is not inherited. It can affect any organism, and a characteristic that shows discontinuous variation can also be altered by the environment.
? Two samples have 7 and 11 values. The degrees of freedom for the t-test are
+ 16
- 18
- 17
- 9
> Degrees of freedom \(= n_1 + n_2 - 2 = 7 + 11 - 2 = 16\). 18 is \(n_1 + n_2\), 17 uses \(n_1 + n_2 - 1\), and 9 is the average of the two sample sizes.
? A calculated t value is 1.85 and the critical value at \(p = 0.05\) is 2.10. What should be concluded?
+ The null hypothesis is accepted: the difference may be due to chance.
- The null hypothesis is rejected: the difference is significant.
- The difference is almost significant, so it is a real difference.
- The null hypothesis is proved true.
> 1.85 is less than 2.10, so the null hypothesis is accepted and the difference could be due to chance. A test cannot prove a null hypothesis true, and a result near the critical value is still not significant.
? Which statement about the standard deviation of a sample is correct?
+ A larger value shows that the data are more spread out around the mean.
- It is the difference between the largest and smallest values.
- It is the same as the mean.
- It is calculated by dividing by \(n\) for a sample.
> The standard deviation measures the spread of the data. The range is the difference between the extremes, and for a sample the divisor is \(n - 1\).
? Which test is suitable for comparing the mean masses of two samples of continuous data with similar standard deviations?
+ t-test
- chi-squared test
- bar chart
- Simpson's index
> The t-test compares the means of two samples of continuous data. The chi-squared test is for counts in categories.
:::

:::checklist What you can now do
- [ ] I can explain, with examples, that phenotypic variation is due to genetic factors, environmental factors, or both.
- [ ] I can explain what is meant by discontinuous and continuous variation, and choose between a bar chart and a histogram.
- [ ] I can explain the genetic basis of discontinuous variation (one or a few genes) and of continuous variation (many genes, additive effects, plus the environment).
- [ ] I can describe a normal distribution and calculate a mean and a standard deviation (using \(n - 1\)).
- [ ] I can state the null hypothesis, calculate t from the formula, find the degrees of freedom (\(n_1 + n_2 - 2\)) and use a table of critical values.
- [ ] I can write a conclusion for a t-test in words, in the context of the question, and finish a partly completed t-test.
- [ ] I can say when a t-test can and cannot be used.
:::

:::recap
- Variation is caused by genes (mutation, meiosis, random fertilisation), by the environment, or by both. Clones show environmental variation.
- Discontinuous variation: distinct categories, one or a few genes, little environmental effect, bar chart. Continuous variation: a range, many genes with additive effects plus the environment, histogram, normal distribution.
- Standard deviation measures spread: \(s = \sqrt{\sum (x - \bar{x})^2 / (n - 1)}\). About 95% of values are within 2 standard deviations of the mean. \(\mathrm{SE} = s / \sqrt{n}\); 95% CI \(\approx \bar{x} \pm 2\,\mathrm{SE}\).
- t-test: two samples of continuous, normally distributed data with similar standard deviations. Null hypothesis: no significant difference.
- \(t = |\bar{x}_1 - \bar{x}_2| / \sqrt{s_1^2/n_1 + s_2^2/n_2}\); degrees of freedom \(= n_1 + n_2 - 2\); compare with the critical value at \(p = 0.05\).
- Calculated \(t\) greater than critical: reject the null hypothesis, a significant difference (less than 5% probability of chance). Less than critical: accept it; the difference could be due to chance.
- A t-test does not prove a cause; categories (counts) need the chi-squared test.
:::

:::links
- read: [CAIE A Level Biology: selection and evolution notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/selection-and-evolution/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Selection and evolution (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/17-selection-and-evolution/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- practise: [Practical skills notes and questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/practical-skills/) · Physics & Maths Tutor · statistics and data-handling questions for Papers 3 and 5
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [Khan Academy Biology](https://www.khanacademy.org/science/biology) · Khan Academy · free lessons on inheritance and populations
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · find the statistics questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Natural and artificial selection](#bio.selection) uses this variation: when conditions favour some phenotypes, the alleles for them become more common.
