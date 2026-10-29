@chapter bio.dihybrid
@title Dihybrid crosses and the chi-squared test
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 5–6 hours
@summary A dihybrid cross follows two genes at once. You will learn how to predict the 9 : 3 : 3 : 1 and 1 : 1 : 1 : 1 ratios of unlinked genes, cross a gene on a sex chromosome with one on an autosome, explain how autosomal linkage and crossing over change the ratios, interpret epistasis from the information given, and use the chi-squared test, with its null hypothesis, degrees of freedom and critical value, to decide whether results fit the ratio expected.

:::why
Real organisms differ in many features at once, and breeders and doctors want to know how two features are inherited together: will a pea plant that is round and yellow always have round and yellow offspring? Exam questions on dihybrid inheritance combine a long genetic diagram with ratios and with a statistical test. The chi-squared test is how a scientist decides whether an observed set of numbers fits the ratio a hypothesis predicts, or whether the difference is too big to be chance. Paper 4 asks for the diagrams and the test, and Paper 5 asks you to analyse and evaluate experiments that use it.
:::

**Before you start**, you should know the genetic diagram and the terms of [Monohybrid inheritance](#bio.inheritance), and how random orientation of the pairs of chromosomes in metaphase I produces different gametes from [Meiosis and genetic variation](#bio.meiosis).

:::try Warm-up
Q: Two heterozygous pea plants (Tt) are crossed. State the expected phenotypic ratio of their offspring. (from [Monohybrid inheritance](#bio.inheritance))
A: 3 tall : 1 dwarf (3 dominant : 1 recessive), from the genotypes TT, Tt, Tt and tt.
Q: A cell is AaBb, and the two genes are on different pairs of chromosomes. Which gametes can it make, and why? (from [Meiosis and genetic variation](#bio.meiosis))
A: (AB), (Ab), (aB) and (ab). The pairs of homologous chromosomes line up at random in metaphase I, so A can go to the same gamete as B or as b.
Q: State the genotype of an organism used in a test cross as the second parent. (from [Monohybrid inheritance](#bio.inheritance))
A: Homozygous recessive (for example tt).
:::

## Two genes at once: unlinked genes

A **dihybrid cross** follows the inheritance of two genes. The genes are **unlinked** when they are on different pairs of chromosomes. Each gene follows the rules you know, and the two assort independently, because the pairs of homologous chromosomes line up at random in metaphase I.

An individual that is heterozygous for both genes, AaBb, makes four kinds of gamete: (AB), (Ab), (aB) and (ab). Each gamete gets one allele of each gene, and all four kinds are equally common (each makes up one quarter). Write the gametes first, because the rest of the diagram follows from them.

:::tip Writing the gametes
For a parent AaBb: take each allele of the first gene in turn and pair it with each allele of the second gene. A goes with B and with b; a goes with B and with b. That is \(2 \times 2 = 4\) gametes. A parent AABb makes only (AB) and (Ab). A parent AAbb makes only (Ab). Check that every gamete has exactly one allele of each gene.
:::

:::eg Pea plants with round, yellow seeds (R and Y are dominant) that are heterozygous for both genes were crossed with each other. Draw a genetic diagram and state the phenotypic ratio of the offspring.
**Key**: R = allele for round seeds, r = allele for wrinkled seeds; Y = allele for yellow seeds, y = allele for green seeds.

Parental phenotypes: round yellow × round yellow. Parental genotypes: RrYy × RrYy. [B1]

Gametes from each parent: (RY), (Ry), (rY) and (ry). [B1]

The Punnett square has 16 boxes:

| | (RY) | (Ry) | (rY) | (ry) |
|---|---|---|---|---|
| **(RY)** | RRYY | RRYy | RrYY | RrYy |
| **(Ry)** | RRYy | RRyy | RrYy | Rryy |
| **(rY)** | RrYY | RrYy | rrYY | rrYy |
| **(ry)** | RrYy | Rryy | rrYy | rryy |

There are nine genotypes: RRYY (1), RRYy (2), RrYY (2), RrYy (4), RRyy (1), Rryy (2), rrYY (1), rrYy (2) and rryy (1). [B1]

Phenotypes: 9 round yellow (R_Y_) : 3 round green (R_yy) : 3 wrinkled yellow (rrY_) : 1 wrinkled green (rryy). [B1]

(A dash such as R_ means "R with either R or r".)
:::

Use the widget to run this cross and others. The square can show genotypes or phenotypes.

:::html
<div class="widget" data-w="bio-punnett" data-type="di" data-p1="RrYy" data-p2="RrYy" data-ph="round,wrinkled,yellow,green"></div>
:::

### A quicker way: multiply the two monohybrid results

The 9 : 3 : 3 : 1 ratio is no accident. Each gene on its own gives a 3 : 1 ratio, and the two genes are independent, so their probabilities multiply.

\[\begin{aligned} P(\text{round, yellow}) &= \tfrac34 \times \tfrac34 = \tfrac{9}{16} \\ P(\text{round, green}) &= \tfrac34 \times \tfrac14 = \tfrac{3}{16} \\ P(\text{wrinkled, yellow}) &= \tfrac14 \times \tfrac34 = \tfrac{3}{16} \\ P(\text{wrinkled, green}) &= \tfrac14 \times \tfrac14 = \tfrac{1}{16} \end{aligned}\]

:::key Dihybrid crosses with unlinked genes
- Heterozygote × heterozygote (AaBb × AaBb): gametes (AB), (Ab), (aB), (ab) from each parent; **9 : 3 : 3 : 1** phenotypes (9 genotypes, 4 phenotypes).
- Test cross (AaBb × aabb): the second parent makes only (ab); offspring in the ratio **1 : 1 : 1 : 1**.
- For unlinked genes, multiply the ratios (or probabilities) from the two monohybrid crosses. Use this to check a Punnett square or to answer a probability question without drawing 16 boxes.
:::

:::eg A pea plant with round, yellow seeds was crossed with a plant with wrinkled, green seeds. The offspring were 24 round yellow, 26 round green, 25 wrinkled yellow and 25 wrinkled green. Deduce the genotype of the round, yellow parent and explain how you know.
The wrinkled green parent is rryy, a homozygous recessive. This is a test cross. [B1]

The wrinkled green parent makes only (ry) gametes, so each offspring shows the alleles in the gamete it received from the round yellow parent. [B1]

All four phenotypes appear, in about equal numbers (24 : 26 : 25 : 25, close to 1 : 1 : 1 : 1). So the round yellow parent made four kinds of gamete, (RY), (Ry), (rY) and (ry), in equal numbers. It is **RrYy**, heterozygous for both genes, and the genes are on different chromosomes. [B1]

(Otherwise, if the plant had been RRYy, no offspring would have been wrinkled.)
:::

## A dihybrid cross with a sex-linked gene

When one of the two genes is on the X chromosome, the offspring must be sorted by sex as well as by the other gene. Do each gene on its own, then combine. In fruit flies, long wings (L) are dominant to vestigial wings (l), and the gene is on an autosome. Red eyes (\(X^R\)) are dominant to white eyes (\(X^r\)), and the gene is on the X chromosome.

:::eg A heterozygous long-winged, red-eyed female fruit fly (\(Ll\,X^R X^r\)) was crossed with a long-winged, red-eyed male that is heterozygous for wing length (\(Ll\,X^R Y\)). Predict the phenotypes of the offspring, with their ratio.
**Key**: L = long wings, l = vestigial wings; \(X^R\) = red eyes, \(X^r\) = white eyes.

Parental genotypes: female \(Ll\,X^R X^r\), male \(Ll\,X^R Y\). [B1]

Gametes: the female makes (\(L X^R\)), (\(L X^r\)), (\(l X^R\)) and (\(l X^r\)); the male makes (\(L X^R\)), (\(L Y\)), (\(l X^R\)) and (\(l Y\)). [B1]

Take the genes one at a time. Wings: Ll × Ll gives 3 long : 1 vestigial in both sexes. Eyes: \(X^R X^r\) × \(X^R Y\) gives all daughters red-eyed and sons 1 red-eyed : 1 white-eyed.

Female offspring: all have red eyes, with 3 long : 1 vestigial, so \(\tfrac34 \times \tfrac12 = \tfrac38\) of all offspring are long-winged red-eyed females and \(\tfrac18\) are vestigial-winged red-eyed females. [B1]

Male offspring: the eyes are 1 red : 1 white and the wings 3 long : 1 vestigial. Out of all the offspring, \(\tfrac{3}{16}\) are long-winged red-eyed males, \(\tfrac{3}{16}\) long-winged white-eyed, \(\tfrac{1}{16}\) vestigial-winged red-eyed and \(\tfrac{1}{16}\) vestigial-winged white-eyed. [B1]

In sixteenths, the total ratio is 6 long red females : 2 vestigial red females : 3 long red males : 3 long white males : 1 vestigial red male : 1 vestigial white male. [B1]

A 16-box Punnett square gives the same result. Always separate the sexes when one gene is sex-linked.
:::

## Autosomal linkage

Genes that are on the **same chromosome** are linked. Linked alleles on one chromosome are carried through meiosis together, unless crossing over separates them. A diploid cell has two homologous chromosomes, so a heterozygote has the linked alleles on the chromosomes in a certain arrangement.

:::html
<figure class="fig small"><svg viewBox="0 0 330 336" role="img" aria-label="Two arrangements of two genes in a heterozygote AaBb. Panel A: gene A is on one pair of chromosomes and gene B on another pair, so AaBb makes four kinds of gamete in equal numbers. Panel B: both genes are on the same pair of chromosomes, one chromosome carrying A and B and its homologue carrying a and b, so the heterozygote makes mostly AB and ab gametes and few Ab and aB gametes, made by crossing over."><text class="tl tb" x="8" y="16">A  Genes on different chromosomes</text><rect class="fm s-acc sw2" x="26" y="36" width="16" height="92" rx="8"/><circle class="fi" cx="34" cy="82" r="3"/><rect class="fa s-acc sw2" x="26" y="62" width="16" height="8"/><text class="tl" x="34" y="146" text-anchor="middle">A</text><rect class="fm s-acc sw2" x="54" y="36" width="16" height="92" rx="8"/><circle class="fi" cx="62" cy="82" r="3"/><rect class="fa s-acc sw2" x="54" y="62" width="16" height="8"/><text class="tl" x="62" y="146" text-anchor="middle">a</text><rect class="fm s-acc sw2" x="98" y="68" width="16" height="60" rx="8"/><circle class="fi" cx="106" cy="98" r="3"/><rect class="fa s-acc sw2" x="98" y="76" width="16" height="8"/><text class="tl" x="106" y="146" text-anchor="middle">B</text><rect class="fm s-acc sw2" x="126" y="68" width="16" height="60" rx="8"/><circle class="fi" cx="134" cy="98" r="3"/><rect class="fa s-acc sw2" x="126" y="76" width="16" height="8"/><text class="tl" x="134" y="146" text-anchor="middle">b</text><text class="tl" x="170" y="62">AaBb makes four</text><text class="tl" x="170" y="76">kinds of gamete,</text><text class="tl" x="170" y="90">in equal numbers:</text><text class="tl" x="170" y="104">AB, Ab, aB, ab</text><text class="tl tb" x="8" y="188">B  Genes on the same chromosome</text><rect class="fm s-acc sw2" x="40" y="208" width="16" height="96" rx="8"/><circle class="fi" cx="48" cy="256" r="3"/><rect class="fa s-acc sw2" x="40" y="230" width="16" height="8"/><rect class="fa s-acc sw2" x="40" y="262" width="16" height="8"/><text class="tl" x="32" y="238" text-anchor="end">A</text><text class="tl" x="32" y="270" text-anchor="end">B</text><rect class="fm s-acc sw2" x="100" y="208" width="16" height="96" rx="8"/><circle class="fi" cx="108" cy="256" r="3"/><rect class="fa s-acc sw2" x="100" y="230" width="16" height="8"/><rect class="fa s-acc sw2" x="100" y="262" width="16" height="8"/><text class="tl" x="124" y="238">a</text><text class="tl" x="124" y="270">b</text><text class="tl tb" x="78" y="324" text-anchor="middle">AB / ab</text><text class="tl" x="170" y="252">AaBb (AB/ab) makes</text><text class="tl" x="170" y="266">mostly AB and ab,</text><text class="tl" x="170" y="280">few Ab and aB</text><text class="tl" x="170" y="294">(crossing over)</text></svg><figcaption>Unlinked and linked genes (drawings, each chromosome before replication). In panel B the slash in AB/ab separates the two homologous chromosomes, so alleles on the same chromosome are written together.</figcaption></figure>
:::

Write a linked heterozygote with a slash: AB/ab means one chromosome carries A and B, and its homologue carries a and b. This individual makes gametes in two groups:
- **Parental gametes** (AB and ab): the original chromosomes, unchanged. They are the **majority**.
- **Recombinant gametes** (Ab and aB): formed only when crossing over happens between the two loci in prophase I (see [Meiosis and genetic variation](#bio.meiosis)). They are the **minority**, because crossing over between the two loci does not happen in every cell.

The closer the loci are on the chromosome, the less likely it is that crossing over comes between them, so the fewer the recombinants. If genes are linked, the ratio of offspring departs from the ratio for independent genes. In a test cross of AB/ab with ab/ab, the offspring are mostly AaBb and aabb (like the parents' chromosomes), with a few Aabb and aaBb, instead of 1 : 1 : 1 : 1.

:::eg In the sweet pea, purple flowers (P) are dominant to red flowers (p) and long pollen grains (L) are dominant to round pollen grains (l). A plant heterozygous for both, with P and L on the same chromosome (PL/pl), was crossed with a red-flowered plant with round pollen (pl/pl). The offspring were 84 purple, long; 78 red, round; 22 purple, round; and 16 red, long (the numbers are made up for this example). Explain these results.
The genes are on the same chromosome, so P and L are inherited together, and p and l are inherited together. [B1]

PL/pl makes mostly (PL) and (pl) gametes, which are the parental gametes. The red round plant makes only (pl) gametes. [B1]

So most offspring are purple long (PL/pl, 84) and red round (pl/pl, 78), which are the parental combinations. [B1]

If the genes were on different chromosomes, 1 : 1 : 1 : 1 would be expected, with 50 plants of each type out of 200. [B1]

The 22 purple round (Pl/pl) and 16 red long (pL/pl) plants are the recombinants. They come from gametes (Pl) and (pL), made when crossing over between the two loci in prophase I of meiosis exchanged sections of non-sister chromatids. [B1]

The recombinants are \(22 + 16 = 38\) of 200 offspring, or 19%.
:::

:::warn Do not mix up linkage, sex linkage and codominance
**Linkage**: two genes on the same chromosome. **Sex linkage**: one gene on a sex chromosome (the X). **Codominance**: two alleles of one gene both expressed. They are three different ideas. Also, linked genes are separated only by crossing over, not by independent assortment, which acts on whole chromosomes.
:::

## Epistasis

:::def Epistasis
The interaction of two genes in which the alleles of one gene affect, by masking or modifying, the expression of the alleles of another gene.
:::

In ordinary dihybrid crosses each gene controls its own feature. In epistasis one gene affects what the other can do, so the ratio of phenotypes differs from 9 : 3 : 3 : 1. The syllabus does not expect you to know the ratios for the different types of epistasis. You work from the information in the question: read how each gene works, find which genotypes give which phenotype, and count.

:::eg Labrador retrievers are black, chocolate (brown) or yellow. Gene B has the alleles B (black pigment, dominant) and b (brown pigment). Gene E has the alleles E and e: a dog needs at least one E for pigment to be deposited in the coat, and a dog that is ee is yellow whatever its genotype at gene B. The two genes are on different chromosomes. Two black dogs, both BbEe, are crossed. Predict the phenotypes and ratio of the puppies, and explain why this is epistasis.
Gametes from each parent: (BE), (Be), (bE) and (be). [B1]

Work through the 16 combinations by phenotype.

A dog with **ee** is yellow, whatever its B alleles. Of the 16 boxes, \(\tfrac14\) of the pairs of gametes give ee, so there are 4 yellow puppies in 16. [B1]

A dog with at least one **E** and at least one **B** (B_E_) is black: \(\tfrac34 \times \tfrac34 = \tfrac{9}{16}\). [B1]

A dog with at least one E and **bb** (bbE_) is chocolate: \(\tfrac14 \times \tfrac34 = \tfrac{3}{16}\). [B1]

The ratio is **9 black : 3 chocolate : 4 yellow**. [B1]

This is epistasis because gene E affects the expression of gene B: in ee dogs, the alleles of gene B have no effect on the colour that can be seen. [B1]
:::

:::note Do not memorise ratios for epistasis
A different pair of genes can give 9 : 3 : 4, 9 : 7 or 12 : 3 : 1. The exam does not ask you to recall them. It gives the information about how the genes interact, and you work out the phenotype of each genotype and count them.
:::

## The chi-squared test

Real results never match a ratio exactly, because fertilisation is random. 84 : 78 : 22 : 16 differs from 1 : 1 : 1 : 1, but so would 53 : 49 from 1 : 1 in a test cross. How big a difference is too big to be chance? The **chi-squared (\(\chi^2\)) test** answers this for counts that fall into categories (classes).

:::def Chi-squared test
A statistical test that compares observed results with the results expected from a hypothesis, to find the probability that any differences between them are due to chance. It is used for counts in categories, such as numbers of offspring of each phenotype.
:::

### Hypotheses

:::def Null hypothesis
The hypothesis that there is no significant difference between the observed and the expected results, so that any difference is due to chance.
:::

For a cross, the null hypothesis is that there is no significant difference between the observed numbers of offspring and the numbers expected for the ratio (for example 9 : 3 : 3 : 1). The test then gives a probability that a difference as large as the one seen could happen by chance if the null hypothesis were true.

### The formula

The exam prints the formula inside the question, so you do not have to memorise it, but you must know how to use it:

\[\chi^2 = \sum \frac{(O - E)^2}{E}\]

\(O\) is the observed number in a class, \(E\) is the expected number, and \(\sum\) means add the values for all the classes. Work through the classes in a table.

:::key Doing a chi-squared test
1. State the **null hypothesis**: there is no significant difference between the observed and expected results (the ratio fits).
2. Work out the **expected** numbers: total number × the fraction for each class, from the ratio. The expected values add up to the same total as the observed values.
3. Calculate \((O - E)^2 \div E\) for each class and add them to get \(\chi^2\).
4. Find the **degrees of freedom**: the number of classes minus 1.
5. Compare \(\chi^2\) with the **critical value** at \(p = 0.05\) (given in a table in the exam; the degrees of freedom are not given).
6. State the **conclusion** in words.
:::

:::def Degrees of freedom
For a chi-squared test of counts in classes, the number of classes minus 1. It decides which critical value to use.
:::

| degrees of freedom | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| critical value at p = 0.05 | 3.84 | 5.99 | 7.81 | 9.49 | 11.07 |

(The exam gives a table of critical values. The ones here are the usual \(p = 0.05\) values for 1 to 5 degrees of freedom.)

### The conclusion

The value \(p = 0.05\) means a 5% probability that the difference is due to chance. The rule is:
- If \(\chi^2\) is **less than** the critical value: the difference is **not significant**. Any difference between the observed and expected results is due to chance. The null hypothesis is accepted (not rejected): the results fit the ratio.
- If \(\chi^2\) is **greater than** the critical value: the difference is **significant**. It is unlikely (less than 5% probability) to be due to chance alone. The null hypothesis is rejected: the results do not fit the ratio, so something else is acting, such as linkage.

:::eg A tomato plant heterozygous for stem colour (purple A, green a) and leaf shape (cut C, potato-leaf c) was self-pollinated. The 480 plants of the F2 were 275 purple cut, 98 purple potato-leaf, 79 green cut and 28 green potato-leaf (the numbers are made up for this example). Use a chi-squared test to decide whether they fit a 9 : 3 : 3 : 1 ratio.
**Null hypothesis**: there is no significant difference between the observed numbers of plants and the numbers expected for a 9 : 3 : 3 : 1 ratio. [B1]

**Expected numbers** from 480 plants and the ratio (sixteenths): [M1]

\[\begin{aligned} \tfrac{9}{16} \times 480 &= 270 \\ \tfrac{3}{16} \times 480 &= 90 \\ \tfrac{1}{16} \times 480 &= 30 \end{aligned}\]

The expected numbers are 270, 90, 90 and 30, which add up to 480.

**Working table**:

| class | O | E | O − E | (O − E)² | (O − E)²/E |
|---|---|---|---|---|---|
| purple cut | 275 | 270 | 5 | 25 | 0.093 |
| purple potato | 98 | 90 | 8 | 64 | 0.711 |
| green cut | 79 | 90 | −11 | 121 | 1.344 |
| green potato | 28 | 30 | −2 | 4 | 0.133 |

\[\chi^2 = 0.093 + 0.711 + 1.344 + 0.133 = 2.28\]

[A1]

**Degrees of freedom**: 4 classes − 1 = 3. The critical value at \(p = 0.05\) is 7.81. [B1]

**Conclusion**: \(\chi^2\) (2.28) is less than the critical value (7.81), so there is no significant difference between the observed and expected numbers. Any difference is due to chance. The null hypothesis is accepted, and the results fit a 9 : 3 : 3 : 1 ratio (so the two genes are likely to assort independently). [B1]
:::

Check your own working with the calculator. Enter the observed counts and the ratio. The widget starts with Mendel's famous counts for round yellow, round green, wrinkled yellow and wrinkled green peas, but you can type the tomato numbers (275, 98, 79, 28) to see the table above.

:::html
<div class="widget" data-w="bio-chisq" data-obs="315,108,101,32" data-ratio="9:3:3:1" data-names="round yellow,round green,wrinkled yellow,wrinkled green"></div>
:::

:::exam Chi-squared in Papers 4 and 5
The formula and the table of critical values are printed in the question, but the **degrees of freedom are not**: write "degrees of freedom = classes − 1 = …" so the examiner can see where your critical value came from. Use the **counts**, not percentages or ratios. Finish with a conclusion in words that mentions the null hypothesis and chance. Paper 5 may give the data of an experiment and ask you to evaluate the use of the test or to say what extra repeats would improve it.
:::

:::warn What the test cannot do
- Do not say the test "proves" the ratio. A result below the critical value means the data are consistent with the ratio, not that the ratio is certainly right.
- Do not use percentages or ratios for O and E. The test needs the actual counts, because a difference of 5 means more in a sample of 50 than in a sample of 5000.
- Check that the expected numbers add up to the same total as the observed numbers.
- Compare with the critical value for the right number of degrees of freedom: classes − 1, not the number of classes.
:::

### Testing for linkage

If a cross is expected to give 1 : 1 : 1 : 1 (unlinked genes) and \(\chi^2\) is greater than the critical value, the genes are not assorting independently. One explanation is linkage. Check that the classes made by the parental chromosomes are the common ones.

:::eg Test the sweet pea results from the linkage section for a 1 : 1 : 1 : 1 ratio, and state what the result suggests. The offspring were 84 purple long, 78 red round, 22 purple round and 16 red long (200 in total).
**Null hypothesis**: there is no significant difference between the observed numbers and the numbers expected for a 1 : 1 : 1 : 1 ratio. [B1]

**Expected**: \(200 \times \tfrac14 = 50\) of each class. [B1]

| class | O | E | O − E | (O − E)² | (O − E)²/E |
|---|---|---|---|---|---|
| purple long | 84 | 50 | 34 | 1156 | 23.12 |
| red round | 78 | 50 | 28 | 784 | 15.68 |
| purple round | 22 | 50 | −28 | 784 | 15.68 |
| red long | 16 | 50 | −34 | 1156 | 23.12 |

\[\chi^2 = 23.12 + 15.68 + 15.68 + 23.12 = 77.6\]

[M1] [A1]

Degrees of freedom \(= 4 - 1 = 3\); the critical value at \(p = 0.05\) is 7.81. [B1]

**Conclusion**: \(\chi^2\) (77.6) is much greater than 7.81, so there is a significant difference between the observed and expected numbers, which is unlikely to be due to chance. The null hypothesis is rejected: the results do not fit 1 : 1 : 1 : 1. [B1]

The commonest classes are the two parental combinations, so the genes are probably linked on the same chromosome, with the other two classes made by crossing over. [B1]
:::

:::eg Spot the error: a student tested 320 maize kernels from a dihybrid cross against a 9 : 3 : 3 : 1 ratio. Observed: 170 purple smooth, 80 purple shrunken, 50 yellow smooth and 20 yellow shrunken. [5]
A student wrote this answer.

Line 1: Null hypothesis: there is no significant difference between observed and expected numbers.
Line 2: Expected: 180, 60, 60 and 20.
Line 3: \(\chi^2 = 0.556 + 6.667 + 1.667 + 0 = 8.89\).
Line 4: Degrees of freedom = 4, because there are 4 classes. The critical value is 9.49.
Line 5: 8.89 is less than 9.49, so there is no significant difference and the results fit the ratio.

Line 1 is correct [B1]. Line 2 is correct [B1]. Line 3 is correct [B1]. **Line 4 is wrong: the degrees of freedom are the number of classes minus 1, which is 3, and the critical value is 7.81. That mark is lost [B0].** **Line 5 follows from the wrong critical value. With the right one, 8.89 is greater than 7.81, so the difference is significant and the results do not fit the ratio. That mark is lost [B0].**

Correct Lines 4 and 5: "Degrees of freedom = 4 − 1 = 3; critical value 7.81. 8.89 is greater than 7.81, so the difference is significant and the null hypothesis is rejected." Notice how the wrong degrees of freedom reversed the conclusion.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State the gametes made by a plant with the genotype AaBb, if the genes are on different chromosomes.
A: (AB), (Ab), (aB) and (ab), in equal numbers.
Q: State the gametes made by a plant with the genotype AABb.
A: (AB) and (Ab).
Q: State how many genotypes and how many phenotypes are possible in the offspring of AaBb × AaBb, if both genes show complete dominance.
A: 9 genotypes and 4 phenotypes.
Q: State the expected ratio of phenotypes in a test cross AaBb × aabb with unlinked genes.
A: 1 : 1 : 1 : 1.
Q: Two plants AaBb are crossed. Use the product rule to calculate the probability that an offspring is aabb.
A: \(P(aa) \times P(bb) = \tfrac14 \times \tfrac14 = \tfrac{1}{16}\).
Q: A dihybrid cross AaBb × AaBb produced 160 offspring. Calculate the expected number of each phenotype for a 9 : 3 : 3 : 1 ratio.
A: \(\tfrac{9}{16} \times 160 = 90\), \(\tfrac{3}{16} \times 160 = 30\) (twice) and \(\tfrac{1}{16} \times 160 = 10\).
Q: State the number of degrees of freedom of a chi-squared test with (a) 2 classes and (b) 6 classes.
A: (a) 1. (b) 5.
Q: A chi-squared test with 4 classes gave \(\chi^2 = 9.2\). The critical value at \(p = 0.05\) for this number of degrees of freedom is 7.81. State the conclusion.
A: 9.2 is greater than 7.81, so the difference between the observed and expected numbers is significant; it is unlikely to be due to chance and the null hypothesis is rejected.
Q: A cross of two heterozygous plants gave 148 tall and 52 dwarf. Test the results against a 3 : 1 ratio. The critical value for 1 degree of freedom is 3.84.
A: Expected: 150 and 50. \(\chi^2 = \dfrac{(148-150)^2}{150} + \dfrac{(52-50)^2}{50} = 0.027 + 0.080 = 0.11\). 0.11 is less than 3.84, so there is no significant difference; the results fit 3 : 1.
Q: Explain why the observed numbers, and not percentages, must be used in a chi-squared test.
A: The test is sensitive to the size of the sample: a difference of 5 is more important in a sample of 50 than in a sample of 5000. Percentages hide the sample size, so \(\chi^2\) would be wrong.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Distinguish between autosomal linkage and sex linkage.
A: Autosomal linkage is the presence of two genes on the same autosome (a non-sex chromosome), so they tend to be inherited together. [B1]
Sex linkage is the presence of a gene on a sex chromosome (the X), so inheritance of the gene differs between males and females. [B1]
A male has only one allele of an X-linked gene, so a recessive allele is always expressed in him, but linked genes on an autosome are inherited in the same way in both sexes. [B1]
(Also credit: linked genes are separated only by crossing over.)
Q: [5 marks] ★★ In a species of flowering plant, purple petals (P) are dominant to white (p), and long stamens (S) are dominant to short (s). The two genes are on different chromosomes. A true-breeding plant with purple petals and short stamens was crossed with a true-breeding plant with white petals and long stamens. The F1 plants were allowed to self-pollinate. (a) State the genotype and phenotype of the F1 plants. (b) State the gametes made by the F1 plants and the ratio of phenotypes in the F2. (c) Calculate the probability that an F2 plant has white petals and short stamens. (d) Calculate the number of F2 plants with white petals and long stamens expected among 800.
H: True-breeding means homozygous. The parents are PPss and ppSS.
A: (a) PpSs, with purple petals and long stamens. [B1]
(b) Gametes (PS), (Ps), (pS) and (ps). [B1] The ratio is 9 purple long : 3 purple short : 3 white long : 1 white short. [B1]
(c) \(\tfrac{1}{16}\) (or \(\tfrac14 \times \tfrac14\)). [B1]
(d) \(\tfrac{3}{16} \times 800 = 150\). [B1]
Q: [5 marks] ★★ A woman of blood group A who is a carrier of red-green colour blindness (\(I^A I^o X^B X^b\)) has a child with a man of blood group O who has normal colour vision (\(I^o I^o X^B Y\)). The blood group gene is on an autosome and the colour-blindness gene is on the X chromosome. (a) State the gametes made by the woman. (b) Calculate the probability that the child has blood group O. (c) Calculate the probability that the child is a colour-blind boy. (d) Calculate the probability that the child is a colour-blind boy with blood group O.
H: The two genes are unlinked, so multiply the probabilities from the two crosses.
A: (a) (\(I^A X^B\)), (\(I^A X^b\)), (\(I^o X^B\)) and (\(I^o X^b\)). [B1]
(b) \(I^A I^o\) × \(I^o I^o\) gives \(I^A I^o\) and \(I^o I^o\), so \(\tfrac12\). [B1]
(c) \(X^B X^b\) × \(X^B Y\) gives \(X^b Y\) in one of four boxes, so \(\tfrac14\). [B1]
(d) \(\tfrac12 \times \tfrac14\) [M1] \(= \tfrac18\) [A1]
Q: [6 marks] ★★ A plant heterozygous for two genes was crossed with a plant homozygous recessive for both genes. The offspring were 403 with the dominant phenotype for both genes (AB), 389 with the recessive phenotype for both (ab), 98 with A and b, and 110 with a and B. (a) State the ratio expected if the genes were on different chromosomes. (b) Name the two parental classes of offspring. (c) Explain why the parental classes are much more frequent than the others. (d) Explain how the other two classes arise. (e) Calculate the percentage of the offspring that are recombinants.
A: (a) 1 : 1 : 1 : 1. [B1]
(b) AB and ab (the 403 and 389). [B1]
(c) The two genes are linked on the same chromosome, so the alleles A and B (and a and b) are inherited together. [B1]
(d) Crossing over between the two loci in prophase I of meiosis exchanges sections of non-sister chromatids, producing chromatids Ab and aB (recombinant gametes). [B1]
(e) \(\dfrac{98 + 110}{1000} \times 100\) [M1] \(= 20.8\%\) [A1]
Q: [6 marks] ★★ In a species of moth, two unlinked genes control wing colour and wing pattern. A cross of two moths heterozygous for both genes gave 320 offspring: 188 dark spotted, 57 dark plain, 52 pale spotted and 23 pale plain. The expected ratio is 9 : 3 : 3 : 1. Use a chi-squared test, \(\chi^2 = \sum \dfrac{(O-E)^2}{E}\), to test whether the results fit this ratio. The critical values at \(p = 0.05\) are 3.84 for 1, 5.99 for 2, 7.81 for 3 and 9.49 for 4 degrees of freedom.
H: Expected numbers are in sixteenths of 320.
H: Degrees of freedom are not given; work them out from the number of classes.
A: Null hypothesis: there is no significant difference between the observed and expected numbers. [B1]
Expected: 180, 60, 60 and 20. [B1]
\(\chi^2 = \dfrac{8^2}{180} + \dfrac{(-3)^2}{60} + \dfrac{(-8)^2}{60} + \dfrac{3^2}{20}\) [M1] \(= 0.356 + 0.150 + 1.067 + 0.450 = 2.02\) [A1]
Degrees of freedom = 4 − 1 = 3; the critical value is 7.81. [B1]
2.02 is less than 7.81, so there is no significant difference; any difference is due to chance, the null hypothesis is accepted and the results fit a 9 : 3 : 3 : 1 ratio. [B1]
Q: [5 marks] ★★ In a species of mouse, a mouse can make pigment only if it has at least one allele C. In a pigmented mouse, allele A gives agouti fur and genotype aa gives black fur. Mice that are cc are albino whatever their genotype at the other gene. Two unlinked genes are involved. A cross of two agouti mice gave an F2 of 90 agouti, 28 black and 42 albino. (a) Show that the numbers fit a ratio close to 9 : 3 : 4. (b) State the genotype of the parents of the F2. (c) Explain, using the term epistasis, why there are only three phenotypes.
H: A dihybrid cross has sixteenths; which sixteenths are cc?
A: (a) Total 160, so a 9 : 3 : 4 ratio gives 90, 30 and 40 (in sixteenths: 9, 3 and 4 of 16); the observed 90 : 28 : 42 is close. [B1]
(b) AaCc × AaCc. [B1]
(c) Gene C affects the expression of gene A: in cc mice no pigment is made, so the alleles of gene A cannot show. [B1] This is epistasis. [B1]
The albino mice include AAcc, Aacc and aacc, so the albino class is 4 of the 16 (\(\tfrac14\)). [B1]
Q: [7 marks] ★★★ A test cross AaBb × aabb with two genes in a species of beetle gave 66 AB, 58 Ab, 61 aB and 55 ab. (a) Test the results for a 1 : 1 : 1 : 1 ratio with a chi-squared test (the critical value for 3 degrees of freedom at \(p = 0.05\) is 7.81). (b) State what the result suggests about the positions of the two genes, and explain how meiosis produces this result.
H: Expected values are a quarter of the total each.
A: (a) Null hypothesis: there is no significant difference between observed and expected numbers. [B1] Total 240; expected 60 of each class. [B1] \(\chi^2 = \dfrac{36 + 4 + 1 + 25}{60}\) [M1] \(= 1.1\) [A1] 3 degrees of freedom; 1.1 is less than 7.81, so there is no significant difference; the results fit 1 : 1 : 1 : 1. [B1]
(b) The genes are not linked: they are on different chromosomes. [B1]
In metaphase I the bivalents line up at random, so A is as likely to go with b as with B, giving four types of gamete in equal numbers. [B1]
(Also credit: genes on the same chromosome that are very far apart can also give a result close to 1 : 1 : 1 : 1, as crossing over then separates them in about half the cells.)
Q: [6 marks] ★★★ Explain, with reference to meiosis, why a plant AaBb makes four types of gamete in equal numbers if the genes are on different chromosomes, but mostly two types if the genes are on the same chromosome.
H: Think of metaphase I, and of the chromatids that crossing over exchanges.
A: When the genes are on different chromosomes, the two pairs of homologous chromosomes line up at random on the equator in metaphase I. [B1]
A may go to the same pole as B or as b with equal probability. [B1]
So four gamete types, (AB), (Ab), (aB) and (ab), are produced, each in a quarter of the gametes. [B1]
When the genes are on the same chromosome, A and B are on one chromosome and a and b on its homologue, so the alleles stay together as the homologues separate. [B1]
Only crossing over between the loci (prophase I) can bring A and b, or a and B, onto the same chromatid. [B1]
Crossing over between the loci happens in only some cells, so most gametes are the parental types AB and ab, and few are recombinants. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ In a species of flowering plant, purple pigment is made in two steps. Gene C codes for an enzyme that makes an intermediate from a colourless precursor, and gene P codes for a different enzyme that turns the intermediate into purple pigment. The alleles C and P are dominant and code for working enzymes; c and p code for enzymes that do not work. The genes are on different chromosomes. A white-flowered plant (CCpp) was crossed with a different white-flowered plant (ccPP). (a) State the genotype and phenotype of the F1. (b) The F1 were crossed with each other. State the ratio of the phenotypes in the F2. (c) Explain why a plant with the genotype ccPp has white flowers.
H: A plant needs at least one C and at least one P. How many of the 16 boxes have both?
A: (a) CcPp, purple: it has a working enzyme from each gene, so both steps happen. [B1]
(b) 9 purple (C_P_) : 7 white. [B1] [B1]
(c) Without a working enzyme from gene C, the intermediate is not made. [B1] So the second enzyme has nothing to act on and no pigment forms. [B1] The two genes interact (epistasis), and either recessive homozygote blocks pigment. [B1]
Q: [5 marks] ★★★ A plant is heterozygous for two linked genes, but a scientist does not know how the alleles are arranged on the chromosomes. A test cross with a plant that is aabb gave 12 AaBb, 10 aabb, 88 Aabb and 90 aaBb. (a) State which offspring classes are parental and which are recombinant. (b) State the arrangement of the alleles on the chromosomes of the heterozygous parent. (c) Calculate the percentage of the offspring that are recombinants.
H: The commonest classes come from the gametes made without crossing over.
A: (a) The commonest classes, Aabb (88) and aaBb (90), are parental. [B1] AaBb (12) and aabb (10) are the recombinants. [B1]
(b) The parental gametes are (Ab) and (aB), so one chromosome carries A and b, and its homologue carries a and B (Ab/aB). [B1]
(c) \(\dfrac{12 + 10}{200} \times 100\) [M1] \(= 11\%\) [A1]
:::

:::quiz
? A plant RrYy makes gametes. The genes are on different chromosomes. Which is NOT a possible gamete?
+ Rr
- RY
- ry
- rY
> A gamete carries one allele of each gene. Rr is two alleles of one gene, so it is a genotype, not a gamete.
? Two plants AaBb are crossed and the genes are unlinked. What is the expected ratio of phenotypes if A and B are dominant?
+ 9 : 3 : 3 : 1
- 3 : 1
- 1 : 1 : 1 : 1
- 1 : 2 : 1
> Two 3 : 1 ratios multiplied give 9 : 3 : 3 : 1. The 1 : 1 : 1 : 1 ratio is for a test cross, and 1 : 2 : 1 is for codominance in a monohybrid cross.
? A chi-squared test has 5 classes. How many degrees of freedom are there?
+ 4
- 5
- 6
- 3
> Degrees of freedom are the number of classes minus 1. Using 5 is the common error.
? In a chi-squared test, \(\chi^2\) is 6.2 with 3 degrees of freedom. The critical value at \(p = 0.05\) is 7.81. What is the correct conclusion?
+ the difference is not significant, so any difference is due to chance
- the difference is significant, so the null hypothesis is rejected
- the null hypothesis is proved correct
- the test is invalid because \(\chi^2\) is not zero
> 6.2 is less than 7.81, so the null hypothesis is accepted: any difference is probably due to chance. A test cannot prove a hypothesis, and a small non-zero value is normal.
? A test cross of Ab/aB with ab/ab, for two linked genes, gives four classes of offspring. Which two classes are the most common?
+ Aabb and aaBb
- AaBb and aabb
- AaBb and Aabb
- all four are equally common
> The parent's chromosomes carry Ab and aB, so the common (parental) offspring are Aabb and aaBb. AaBb and aabb are the recombinants, made only by crossing over between the loci.
? What should be used for O and E in a chi-squared test?
+ the numbers (counts) of offspring in each class
- the percentages of offspring in each class
- the ratios of offspring in each class
- the genotype of each parent
> Chi-squared needs counts, because the size of the sample affects how important a difference is.
? A plant with the genotype ww has white flowers whatever its genotype at a second gene that makes red or pink flowers. This is an example of
+ epistasis
- codominance
- sex linkage
- independent assortment
> One gene (E) affects the expression of a different gene (B). Codominance is two alleles of one gene both showing.
? 240 offspring are expected in a 1 : 1 : 1 : 1 ratio. What is the expected number in each class?
+ 60
- 24
- 120
- 80
> 240 ÷ 4 = 60. Dividing by 10 or by 2 gives wrong values, and 80 is a third of 240.
? A chi-squared test on a 9 : 3 : 3 : 1 cross gave a value above the critical value. Which statement is correct?
+ the difference between observed and expected is unlikely to be due to chance alone
- the genes must be linked, because chi-squared proves it
- the cross must have been done incorrectly
- the null hypothesis is accepted
> A value above the critical value means the difference is significant. Linkage is one possible explanation, but the test does not prove it.
:::

:::checklist What you can now do
- [ ] I can predict the gametes and the 9 : 3 : 3 : 1 and 1 : 1 : 1 : 1 ratios for dihybrid crosses with unlinked genes, including a Punnett square.
- [ ] I can predict the offspring of a cross when one gene is sex-linked and the other is autosomal.
- [ ] I can explain autosomal linkage and use crossing over to explain recombinants.
- [ ] I can interpret the effect of epistasis from the information about how the genes interact.
- [ ] I can state a null hypothesis and calculate expected values from a ratio.
- [ ] I can calculate \(\chi^2\) from observed and expected counts, with the degrees of freedom.
- [ ] I can compare \(\chi^2\) with the critical value at \(p = 0.05\) and state the conclusion in words.
- [ ] I can explain when a significant \(\chi^2\) suggests linkage.
:::

:::recap
- A dihybrid cross follows two genes. Unlinked genes: AaBb makes (AB), (Ab), (aB), (ab) in equal numbers, and AaBb × AaBb gives 9 : 3 : 3 : 1. A test cross AaBb × aabb gives 1 : 1 : 1 : 1.
- For unlinked genes, multiply the ratios or the probabilities of the two single-gene crosses.
- With a sex-linked gene, work out each gene separately and separate the sexes.
- Linked genes are on the same chromosome (AB/ab). Most gametes are parental; recombinants (Ab, aB) come only from crossing over, so the ratio departs from 9 : 3 : 3 : 1 or 1 : 1 : 1 : 1.
- Epistasis: the alleles of one gene affect the expression of another. Work from the information given; do not memorise ratios.
- Chi-squared: \(\chi^2 = \sum (O-E)^2/E\), with counts, expected values from the ratio, and degrees of freedom = classes − 1.
- Compare \(\chi^2\) with the critical value at \(p = 0.05\): 3.84, 5.99, 7.81, 9.49 for 1 to 4 degrees of freedom.
- If \(\chi^2\) is less than the critical value, the difference is not significant and is due to chance; the null hypothesis is accepted. If it is greater, the difference is significant and the null hypothesis is rejected.
:::

:::links
- read: [CAIE A Level Biology: inherited change notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/inherited-change/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Inheritance (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/16-inheritance/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of dihybrid crosses
- explore: [Learn.Genetics: the basics](https://learn.genetics.utah.edu/content/basics/) · University of Utah · interactive pages on genes, alleles and inheritance
- read: [Mendel's experiments and the laws of probability](https://openstax.org/books/biology-2e/pages/12-introduction) · OpenStax Biology 2e · free university textbook chapter on Mendel and dihybrid crosses, beyond the syllabus in places
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · find the chi-squared questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Genes, phenotype and gene control](#bio.genecontrol) shows how genes produce the features you have followed in crosses.
