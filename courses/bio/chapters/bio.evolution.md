@chapter bio.evolution
@title Evolution and speciation
@level a2
@paper CAIE 9700 Paper 4
@time 3–4 hours
@summary Evolution is the process by which new species form from existing species as the gene pools of populations change. You will learn how DNA and protein sequences show how closely species are related (including the molecular clock and its limits), and how geographical separation (allopatric speciation) and ecological or behavioural separation (sympatric speciation) split one gene pool into two.

:::why
Every species alive today, from bacteria to blue whales, came from earlier species, and the evidence for this is written in the base sequences of their DNA. This chapter shows you how to read that evidence and how one species can become two. Questions on speciation and on sequence data are common in the structured papers, and they test whether you can build a long cause-and-effect chain in the right order.
:::

**Before you start**, you should know gene pools, allele frequencies, selection and genetic drift from [Natural and artificial selection](#bio.selection), and gene mutation from [Protein synthesis and gene mutation](#bio.synthesis).

:::try Warm-up
Q: Define the term gene pool. (from [Natural and artificial selection](#bio.selection))
A: All the alleles of all the genes in all the individuals of a population at one time.
Q: A base substitution changes the codon GAA to GAG, and both code for glutamic acid. Why is the protein unchanged? (from [Protein synthesis and gene mutation](#bio.synthesis))
A: The genetic code is degenerate: most amino acids are coded for by more than one triplet, so the polypeptide is the same (a silent mutation).
Q: Which type of selection can split a population into two groups when two different food sources are available? (from [Natural and artificial selection](#bio.selection))
A: Disruptive selection: the two extreme phenotypes are favoured and the intermediates are selected against.
:::

## Evolution: changing gene pools

In [Natural and artificial selection](#bio.selection) you saw that the allele frequencies in a population can change from one generation to the next. This chapter follows that idea to its largest result: the formation of new species.

:::def Evolution
The process leading to the formation of new species from pre-existing species over time, as a result of changes to the gene pools of populations from generation to generation.
:::

Four processes change a gene pool:
- **Mutation** creates new alleles. It is random, and it is the only source of completely new alleles.
- **Natural selection** increases the frequency of alleles that make individuals better adapted to their environment.
- **Genetic drift** changes allele frequencies by chance, and has the biggest effect in small populations.
- **Gene flow** (migration) adds alleles to a gene pool when individuals move in and breed, and removes them when individuals move out.

:::key Evolution in one box
- A **population** evolves; an individual does not. An individual keeps the alleles it was born with. What changes is the **frequency of alleles** in the gene pool of the population.
- Evolution needs **variation** (from mutation, and from meiosis and sexual reproduction) that is **inherited**.
- When two populations stop exchanging alleles, their gene pools can drift apart until they are separate species.
:::

:::warn Individuals do not evolve
"The giraffe stretched its neck so its offspring had longer necks" is wrong twice. A body change during life is not inherited, and an individual cannot change its alleles to suit the environment. Write instead: "Giraffes with alleles for longer necks were more likely to survive and reproduce, so the frequency of those alleles in the gene pool increased." Also avoid "more evolved" and "less evolved". Every living species has had the same time since the first cells, and each is adapted to its own environment.
:::

### What is a species?

You need a working definition now, and the full discussion in [Classification](#bio.classification).

:::def Species (biological species concept)
A group of organisms with similar morphological, physiological, biochemical and behavioural features, which can interbreed to produce fertile offspring, and which are reproductively isolated from other species.
:::

The test is breeding. Two populations that can interbreed and produce fertile offspring share one gene pool, and gene flow keeps them similar. Two populations that cannot do so have separate gene pools and can each follow their own course. Speciation is the step from one to the other.

## DNA sequence evidence for evolutionary relationships

If two species came from a common ancestor, they started with the same DNA. After they separated, each lineage collected its own mutations. Mutations are random changes in the base sequence, and they build up with time. So:

:::key The idea behind sequence comparison
The more **differences** there are between the DNA (or protein) sequences of two species, the **longer ago** they shared a common ancestor, and the less closely they are related. Species with few differences separated recently.
:::

:::analogy Copying a manuscript
Imagine two monks who each copy the same manuscript by hand, and then copy their own copies, again and again. Every copying makes a few random slips. After a few generations the two versions still look almost the same. After many, they differ a lot. If you know how fast slips occur, the number of differences tells you how long ago the two lines were copied from one original.
:::

### Comparing sequences

To compare two species, biologists take the same gene from each, line the sequences up base by base, and count the positions where the bases differ. Dividing by the total number of bases gives a **percentage difference**. Computers do the alignment for long sequences.

:::eg Here are the same short stretch of a gene in two species. Count the differences and work out the percentage difference.
Species 1: A T G C C A T T G A
Species 2: A T G C T A T T C A

Compare position by position (there are 10 positions).

Positions 1 to 4 match (A T G C). Position 5 is C in species 1 and T in species 2: **difference**. Positions 6 to 8 match (A T T). Position 9 is G and C: **difference**. Position 10 matches (A).

\[\begin{aligned} \text{differences} &= 2 \\ \text{percentage difference} &= \frac{2}{10} \times 100 \\ &= 20\% \end{aligned}\]

Real comparisons use hundreds or thousands of bases, so the percentages are much smaller and are more reliable, because more bases mean less chance of a misleading result.
:::

The same can be done for **amino acid sequences** of a protein, because the base sequence of a gene decides the amino acid sequence. Two molecules are used a great deal:
- **Cytochrome c**, a protein in the electron transport chain (see [Respiration](#bio.respiration)). Every organism that respires aerobically has it, so it can be compared across a huge range of species. It changes slowly, so it shows relationships between distantly related groups.
- **Mitochondrial DNA** (mtDNA), which mutates faster than most nuclear DNA, so it is useful for species that separated recently. It is inherited from the mother and is not shuffled by meiosis, which makes it easier to follow.

:::note Which gene for which question?
A gene that changes slowly keeps its differences readable over a very long time, so it suits distant relatives. A gene that changes quickly would have changed so many times in distant relatives that the pattern is lost, but it can separate close relatives. Biologists choose the molecule to fit the time scale.
:::

### DNA differences and protein differences

The genetic code is degenerate, so a base substitution does not always change the amino acid (GAA and GAG both code for glutamic acid). Some bases lie in non-coding DNA and never change a protein at all. So two species usually differ at **more positions in their DNA** than in the **amino acid sequence** of the protein it codes for. DNA gives more information than protein sequences, and it can show recent changes that proteins do not.

### Building a tree from a table of differences

A table of pairwise differences can be turned into a **phylogenetic tree**. Follow these steps.

:::steps
1. Find the pair with the **fewest differences**. They separated most recently, so join them first.
2. Join the next closest pair (or add the next species to the first pair if it is closest to both).
3. A difference between two species has built up in **both** lineages since they separated, so each lineage carries **half** of it. Draw each branch to the point where the species split with a length of half the number of differences.
4. Check: the species that split earliest are separated by the **largest** numbers.
:::

:::eg The table shows the number of base differences in the same 100-base stretch of a gene in four species of beetle, W, X, Y and Z. Use it to draw a tree and to compare when the species separated.

| species | W | X | Y | Z |
|---|---|---|---|---|
| W | – | 6 | 30 | 30 |
| X | 6 | – | 30 | 30 |
| Y | 30 | 30 | – | 14 |
| Z | 30 | 30 | 14 | – |

**Step 1: closest pair.** W and X differ least (6), so they share the most recent common ancestor. Join them.

**Step 2: next pair.** Y and Z differ by 14, less than either differs from W or X (30). Join Y and Z.

**Step 3: branch lengths.** Each lineage carries half of the difference. W and X split where each branch has 3 differences; Y and Z where each branch has 7; and the two pairs split from each other where each branch has 15.

<figure class="fig small"><svg viewBox="0 0 340 226" role="img" aria-label="A tree of four species. The common ancestor of all four splits into two lineages. One branch point leads to species W and X, which differ by 6 bases. The other leads to species Y and Z, which differ by 14 bases. Species W and X differ from Y and Z by 30 bases, where the root splits. Branch lengths are drawn as half of the number of differences, and a scale bar shows 5 differences along one branch."><path class="ln sw2" d="M70 105L100 105"/><path class="ln sw2" d="M100 60L100 150"/><path class="ln sw2" d="M100 60L220 60"/><path class="ln sw2" d="M100 150L180 150"/><path class="ln sw2" d="M220 40L220 80"/><path class="ln sw2" d="M180 130L180 170"/><path class="ln sw2" d="M220 40L250 40"/><text class="tl" x="258" y="44">species W</text><path class="ln sw2" d="M220 80L250 80"/><text class="tl" x="258" y="84">species X</text><path class="ln sw2" d="M180 130L250 130"/><text class="tl" x="258" y="134">species Y</text><path class="ln sw2" d="M180 170L250 170"/><text class="tl" x="258" y="174">species Z</text><text class="tl" x="6" y="103">common</text><text class="tl" x="6" y="117">ancestor</text><text class="tl tb" x="228" y="64">6</text><text class="tl tb" x="188" y="154">14</text><text class="tl tb" x="108" y="109">30</text><path class="ln sw2" d="M100 204L150 204"/><path class="ln sw2" d="M100 199L100 209"/><path class="ln sw2" d="M150 199L150 209"/><text class="tl" x="158" y="208">5 differences</text></svg><figcaption>The tree for W, X, Y and Z. The number at each branch point is the number of base differences between the two species that split there. Each branch is drawn as half of that number because both lineages gained changes.</figcaption></figure>

**Step 4: compare the times.** If differences build up at a steady rate, the time since two species split is in proportion to the number of differences.

\[\begin{aligned} \frac{\text{time since W and X split}}{\text{time since Y and Z split}} &= \frac{6}{14} \\ &= 0.43 \end{aligned}\]

W and X separated less than half as long ago as Y and Z. All four share a common ancestor, which lived longest ago (30 differences). The percentage differences are 6%, 14% and 30%, because the stretch is 100 bases.
:::

### The molecular clock

:::def Molecular clock
The use of the number of differences between the DNA or protein sequences of two species to estimate how long ago they shared a common ancestor, on the assumption that the differences build up at a roughly constant rate.
:::

To read the clock in years, it must be **calibrated**: take two species whose separation date is known from fossils, count the differences in their sequences and divide by the time. The rate can then be used for other pairs of species that have no fossil record.

:::eg Two species of vole, A and B, separated 9 million years ago according to fossils. They differ at 36 of 1000 bases of a gene (invented data). A third species, C, differs from A at 20 of the same bases. Estimate when A and C separated.
Differences accumulate in both lineages together, so the rate for the pair is the number of differences per million years.

\[\begin{aligned} \text{rate} &= \frac{36}{9} \\ &= 4 \text{ differences per million years} \end{aligned}\]

Now use the rate to read the clock for A and C:

\[\begin{aligned} \text{time} &= \frac{20}{4} \\ &= 5 \text{ million years} \end{aligned}\]

A and C separated about 5 million years ago, more recently than A and B. This is a **model estimate**: it is only as good as its assumptions.
:::

The graph shows the same calculation as a straight line: the fossil date fixes the slope, and any other number of differences is read off it.

:::plot The molecular clock, if the rate is constant: the number of differences is proportional to the time since the common ancestor. The point for A and B calibrates the line; A and C is read from it. Time is in millions of years (10⁶ years).
--f "4*x" --label "differences = 4 × time" --x 0 12 --y 0 70 --ystep 20 --xlabel "time / 10⁶ years" --ylabel "differences" --pt "9,36,A and B (fossils)@nw" --pt "5,20,A and C@se" --legend tr --alt "A straight line through the origin rising 4 base differences for every million years. The calibration point for species A and B is at 9 million years and 36 differences. The point for A and C is at 20 differences, which reads as 5 million years."
:::

:::exam Discuss: strengths and limitations
"Discuss" means set out the points for and against, then reach a judgement. For the molecular clock and for DNA evidence in general, a good answer has about three **strengths**, about three **limitations**, and a final sentence that weighs them ("so sequence data are powerful, but the dates are estimates that need checking against the fossils").
:::

:::key Discussing DNA sequence evidence
**Strengths**
- A sequence has thousands of characters, so a comparison has far more data than appearance and is objective.
- It can compare species that look very different, and avoids being fooled by **convergent evolution** (unrelated species that evolved similar features).
- It works where there are no fossils, and from tiny samples.
- Results can be checked by comparing several genes and against the fossil record.

**Limitations**
- The mutation rate is **not always constant**: it differs between genes, between lineages and with generation time, so the clock is only approximate.
- A site can mutate more than once (even back to the original base), so some changes are **hidden** and old divergences look younger.
- The clock must be **calibrated with fossils**, and the fossil record is incomplete.
- Silent mutations and changes in non-coding DNA do not change the protein, so protein sequences understate the differences.
- Bacteria can pass genes to other species, which breaks the idea of one line of descent.
:::

:::eg Discuss how DNA sequence data can show evolutionary relationships between species.
A model answer gives three points for and three against.

Sequences of the same gene in different species can be compared base by base, and the number of differences is greater the longer ago the species shared a common ancestor, so closely related species can be identified. [B1]

A DNA sequence has many characters, so the comparison is more objective and detailed than appearance, and it is not misled by convergent evolution. [B1]

It can be used on species with no fossil record, and the conclusions can be checked by comparing several genes or against the fossil evidence. [B1]

However, the molecular clock assumes a constant mutation rate, but the rate differs between genes and between lineages, so the dates are only estimates. [B1]

A base can mutate more than once, including back to the original, so some differences are hidden and old separations look too recent. [B1]

The clock has to be calibrated against fossil dates, which are incomplete, so the dates are uncertain. [B1]

(Also credit: silent mutations mean protein sequences show fewer differences than DNA; non-coding DNA changes freely; gene transfer between bacteria; the data agree with anatomical evidence.)

A weaker answer says "DNA shows that species are related because it is similar". It does not say how, never links the number of differences to time and offers no limitation, so it scores one mark at most.
:::

## Speciation

:::def Speciation
The formation of one or more new species from an existing species.
:::

Speciation happens when a population is split into two groups that no longer exchange alleles. The gene pools then change separately: each has its own mutations, its own selection and its own drift. Eventually the two groups cannot interbreed to produce fertile offspring, even if they meet again. That is the end of speciation: they are two species. The syllabus separates two ways in which the first step, the loss of gene flow, can happen.

### Allopatric speciation: geographical separation

:::def Allopatric speciation
Speciation that follows the **geographical separation** of populations of a species by a physical barrier, such as a sea, mountain range, river or desert, which stops gene flow between them.
:::

<figure class="fig small"><svg viewBox="0 0 340 510" role="img" aria-label="Two panels of squares containing dots of two kinds. Panel A, allopatric speciation, has four stages. 1: one square holds a mixed population, one gene pool. 2: a barrier splits it in two, so there is no gene flow. 3: the two halves change differently by selection, mutation and drift. 4: the barrier has gone, but the halves cannot interbreed, so they are two species. Panel B, sympatric speciation, has three stages in one square divided into two habitats by a dashed line. 1: one mixed population uses two habitats. 2: the groups mate mainly within their own group. 3: there is little gene flow and two species live in the same area."><text class="tl tb" x="10" y="16">A  Allopatric speciation (barrier)</text><rect class="fm s-acc sw2" x="10" y="26" width="150" height="50"/><text class="tl" x="172" y="46">1  One population,</text><text class="tl" x="172" y="62">one gene pool</text><circle class="f1 s-acc" cx="30" cy="40" r="5"/><circle class="f2 s-acc2" cx="58" cy="38" r="5"/><circle class="f1 s-acc" cx="108" cy="40" r="5"/><circle class="f2 s-acc2" cx="132" cy="38" r="5"/><circle class="f1 s-acc" cx="150" cy="41" r="5"/><circle class="f2 s-acc2" cx="40" cy="62" r="5"/><circle class="f1 s-acc" cx="68" cy="60" r="5"/><circle class="f2 s-acc2" cx="110" cy="64" r="5"/><circle class="f1 s-acc" cx="132" cy="61" r="5"/><circle class="f2 s-acc2" cx="148" cy="64" r="5"/><circle class="f1 s-acc" cx="24" cy="52" r="5"/><circle class="f2 s-acc2" cx="122" cy="51" r="5"/><rect class="fm s-acc sw2" x="10" y="92" width="150" height="50"/><text class="tl" x="172" y="112">2  Barrier: no gene</text><text class="tl" x="172" y="128">flow between them</text><circle class="f1 s-acc" cx="30" cy="106" r="5"/><circle class="f2 s-acc2" cx="58" cy="104" r="5"/><circle class="f2 s-acc2" cx="40" cy="128" r="5"/><circle class="f1 s-acc" cx="68" cy="126" r="5"/><circle class="f1 s-acc" cx="24" cy="118" r="5"/><circle class="f1 s-acc" cx="108" cy="106" r="5"/><circle class="f2 s-acc2" cx="132" cy="104" r="5"/><circle class="f1 s-acc" cx="150" cy="107" r="5"/><circle class="f2 s-acc2" cx="110" cy="130" r="5"/><circle class="f1 s-acc" cx="132" cy="127" r="5"/><circle class="f2 s-acc2" cx="148" cy="130" r="5"/><circle class="f2 s-acc2" cx="122" cy="117" r="5"/><path class="ln thick" d="M85 94L85 140"/><rect class="fm s-acc sw2" x="10" y="158" width="150" height="50"/><text class="tl" x="172" y="178">3  Different selection,</text><text class="tl" x="172" y="194">mutation and drift</text><circle class="f2 s-acc2" cx="30" cy="172" r="5"/><circle class="f1 s-acc" cx="58" cy="170" r="5"/><circle class="f2 s-acc2" cx="108" cy="172" r="5"/><circle class="f2 s-acc2" cx="132" cy="170" r="5"/><circle class="f2 s-acc2" cx="150" cy="173" r="5"/><circle class="f2 s-acc2" cx="40" cy="194" r="5"/><circle class="f1 s-acc" cx="68" cy="192" r="5"/><circle class="f2 s-acc2" cx="110" cy="196" r="5"/><circle class="f2 s-acc2" cx="132" cy="193" r="5"/><circle class="f2 s-acc2" cx="148" cy="196" r="5"/><circle class="f2 s-acc2" cx="24" cy="184" r="5"/><circle class="f2 s-acc2" cx="122" cy="183" r="5"/><path class="ln thick" d="M85 160L85 206"/><rect class="fm s-acc sw2" x="10" y="224" width="150" height="50"/><text class="tl" x="172" y="244">4  Barrier gone: cannot</text><text class="tl" x="172" y="260">interbreed, two species</text><circle class="f1 s-acc" cx="30" cy="238" r="5"/><circle class="f1 s-acc" cx="58" cy="236" r="5"/><circle class="f2 s-acc2" cx="108" cy="238" r="5"/><circle class="f2 s-acc2" cx="132" cy="236" r="5"/><circle class="f2 s-acc2" cx="150" cy="239" r="5"/><circle class="f1 s-acc" cx="40" cy="260" r="5"/><circle class="f1 s-acc" cx="68" cy="258" r="5"/><circle class="f2 s-acc2" cx="110" cy="262" r="5"/><circle class="f2 s-acc2" cx="132" cy="259" r="5"/><circle class="f2 s-acc2" cx="148" cy="262" r="5"/><circle class="f1 s-acc" cx="24" cy="250" r="5"/><circle class="f2 s-acc2" cx="122" cy="249" r="5"/><path class="ln-m thin dash" d="M85 226L85 272"/><text class="tl tb" x="10" y="304">B  Sympatric speciation (same area)</text><rect class="fm s-acc sw2" x="10" y="314" width="150" height="50"/><path class="ln-m thin dash" d="M10 339L160 339"/><text class="tl" x="172" y="334">1  One population</text><text class="tl" x="172" y="350">uses two habitats</text><circle class="f1 s-acc" cx="30" cy="322" r="5"/><circle class="f2 s-acc2" cx="65" cy="326" r="5"/><circle class="f1 s-acc" cx="100" cy="322" r="5"/><circle class="f2 s-acc2" cx="135" cy="325" r="5"/><circle class="f1 s-acc" cx="48" cy="332" r="5"/><circle class="f2 s-acc2" cx="118" cy="332" r="5"/><circle class="f1 s-acc" cx="30" cy="348" r="5"/><circle class="f2 s-acc2" cx="65" cy="352" r="5"/><circle class="f1 s-acc" cx="100" cy="348" r="5"/><circle class="f2 s-acc2" cx="135" cy="351" r="5"/><circle class="f1 s-acc" cx="48" cy="357" r="5"/><circle class="f2 s-acc2" cx="118" cy="357" r="5"/><rect class="fm s-acc sw2" x="10" y="380" width="150" height="50"/><path class="ln-m thin dash" d="M10 405L160 405"/><text class="tl" x="172" y="400">2  Groups mate</text><text class="tl" x="172" y="416">mainly within group</text><circle class="f1 s-acc" cx="30" cy="388" r="5"/><circle class="f1 s-acc" cx="65" cy="392" r="5"/><circle class="f1 s-acc" cx="100" cy="388" r="5"/><circle class="f1 s-acc" cx="135" cy="391" r="5"/><circle class="f1 s-acc" cx="48" cy="398" r="5"/><circle class="f2 s-acc2" cx="118" cy="398" r="5"/><circle class="f2 s-acc2" cx="30" cy="414" r="5"/><circle class="f2 s-acc2" cx="65" cy="418" r="5"/><circle class="f2 s-acc2" cx="100" cy="414" r="5"/><circle class="f2 s-acc2" cx="135" cy="417" r="5"/><circle class="f2 s-acc2" cx="48" cy="423" r="5"/><circle class="f1 s-acc" cx="118" cy="423" r="5"/><rect class="fm s-acc sw2" x="10" y="446" width="150" height="50"/><path class="ln-m thin dash" d="M10 471L160 471"/><text class="tl" x="172" y="466">3  Little gene flow:</text><text class="tl" x="172" y="482">two species, one area</text><circle class="f1 s-acc" cx="30" cy="454" r="5"/><circle class="f1 s-acc" cx="65" cy="458" r="5"/><circle class="f1 s-acc" cx="100" cy="454" r="5"/><circle class="f1 s-acc" cx="135" cy="457" r="5"/><circle class="f1 s-acc" cx="48" cy="464" r="5"/><circle class="f1 s-acc" cx="118" cy="464" r="5"/><circle class="f2 s-acc2" cx="30" cy="480" r="5"/><circle class="f2 s-acc2" cx="65" cy="484" r="5"/><circle class="f2 s-acc2" cx="100" cy="480" r="5"/><circle class="f2 s-acc2" cx="135" cy="483" r="5"/><circle class="f2 s-acc2" cx="48" cy="489" r="5"/><circle class="f2 s-acc2" cx="118" cy="489" r="5"/></svg><figcaption>Allopatric and sympatric speciation. The two kinds of dot stand for different alleles. In A a physical barrier (thick line) stops gene flow; in B the dashed line separates two habitats in the same area, and there is no barrier to movement.</figcaption></figure>

The steps, in order, are the marking points of every allopatric speciation question:

:::steps
1. A geographical barrier (a sea between islands, a mountain range, a new river or a drying lake) divides one population into two. The two groups can no longer breed with each other, so there is no **gene flow** between the gene pools.
2. The environments differ, so the **selection pressures** differ (food, climate, predators). Alleles that are advantageous in one environment are not the same as in the other.
3. **Mutations** are random, so different alleles arise in each population. In a small founding population, **genetic drift** also changes allele frequencies by chance.
4. Over many generations the **allele frequencies** in the two gene pools become more and more different.
5. When the populations can no longer interbreed to produce fertile offspring, they are separate species. If the barrier is removed they remain **reproductively isolated**.
:::

:::warn The barrier does not make them mutate
Mutations occur at random in all populations, whether or not there is a barrier. The barrier does not cause useful changes or "make" the organisms adapt. It stops gene flow, and that lets the two gene pools diverge under the different selection pressures. Write "stops gene flow" and "different selection pressures", never "causes mutations".
:::

:::eg Two small islands, a short distance apart, were colonised long ago by birds of one species from the mainland. The islands have different food plants. Explain how the island populations could have become separate species.
The sea between the islands is a geographical barrier, so birds cannot move between the islands and there is no gene flow between the populations. [B1]

The islands have different food plants and climate, so the selection pressures are different on each island. [B1]

Mutations occur at random, so different alleles arise in the two populations. [B1]

Birds with alleles that are advantageous on their island survive and reproduce more, passing on those alleles, so the allele frequencies change in each population. [B1]

(In small populations that started from a few birds, genetic drift also changes allele frequencies by chance.)

Over many generations the two gene pools become so different that the birds can no longer interbreed to produce fertile offspring. [B1]

So they are reproductively isolated, and are separate species, even if birds meet again. [B1]

A weaker answer says "the birds on each island adapted to their food and became different species". Individuals do not adapt by wanting to, it never mentions gene flow, mutation or allele frequencies, and it does not say what makes them separate species, so it scores two marks at most.
:::

### Sympatric speciation: ecological and behavioural separation

:::def Sympatric speciation
Speciation in which new species arise within the same area, without a physical barrier, because of **ecological separation** (different habitats or food) or **behavioural separation** (different courtship or breeding times) that stops gene flow between groups.
:::

Here the population still lives in one place, but members mate mainly with others of their own group. Two groups of mechanisms can start this:
- **Ecological separation.** Some individuals feed or live in one habitat (a different depth in a lake, a different host plant) and others in another habitat in the same area. Individuals that meet in the same habitat mate with each other, and the two groups rarely meet to breed. Disruptive selection (see [Natural and artificial selection](#bio.selection)) can favour the two extreme forms and act against intermediates.
- **Behavioural separation.** Individuals differ in courtship display, song, scent or breeding season, and they breed only with partners that match. If females always choose males with their own colour, or one group breeds in spring and the other in autumn, there is little gene flow even though they live side by side.

The gene pools then diverge by selection, mutation and drift, in the same way as for allopatric speciation, until the groups are reproductively isolated.

:::eg Real context, apple maggot flies: explain how a group of flies that lays eggs on apples could become a different species from flies that use hawthorn, in the same area.
The apple maggot fly is a fly of North America. Its larvae feed in fruit. It was originally a fly of hawthorn, and some flies began to use apple trees after apples were introduced. Flies mate on the type of fruit tree on which they were reared, and the two kinds of fruit ripen at different times of the year. (This is a case biologists have studied, and the separation is only partial.)

Flies that began to use apple trees mate on apple trees, so they mate mainly with other apple flies. [B1]

The breeding times differ, because apples and hawthorn fruits ripen at different times: this is a difference in behaviour and timing. [B1]

So there is little gene flow between the two groups, although they live in the same area (no geographical barrier). [B1]

Each group is under different selection pressures, such as the timing of fruit ripening, so allele frequencies diverge. [B1]

If this continues, the groups become reproductively isolated, so a new species arises by sympatric speciation. [B1]
:::

:::note Polyploidy: speciation in one step
In plants, a new species can arise within a single generation. A hybrid between two species is usually sterile because the chromosomes cannot pair in meiosis. If its chromosome number is then doubled by an error in cell division, each chromosome has a partner, and the plant is fertile. It can breed with itself but not with its parent species, which differ in chromosome number. Bread wheat, which has six sets of chromosomes, arose like this from hybridisation of grass species. This is called **polyploidy**.
:::

:::cols
:::col Allopatric
- Populations separated by a **physical barrier**.
- Gene flow stopped by the barrier.
- Different environments give different selection pressures; drift is strong in small groups.
- Reproductive isolation develops afterwards: if the barrier goes, the two remain separate.
:::
:::col Sympatric
- Populations live in the **same area**, with no barrier.
- Gene flow reduced by different **habitats, food, courtship or breeding times**.
- Disruptive selection and mate choice divide the population.
- Reproductive isolation develops while the groups still live together.
:::
:::

### How populations become reproductively isolated

The mechanisms that stop two species from producing fertile offspring are **reproductive isolating mechanisms**. They act before or after the zygote forms.

| type | what happens | example |
|---|---|---|
| prezygotic (before fertilisation) | the gametes never meet | different habitats or breeding seasons; different courtship displays; sex organs that do not fit; sperm that cannot fertilise the egg |
| postzygotic (after fertilisation) | a hybrid zygote forms but fails | the hybrid embryo dies; the hybrid is healthy but sterile, because chromosomes cannot pair in meiosis |

Isolation is not all-or-nothing. When two diverging groups first meet again, some hybrids may form, and natural selection can then favour individuals that mate only with their own group, which strengthens the isolation.

:::warn Looking different is not speciation
Two populations of one species can look different (dog breeds, human populations) and still interbreed to produce fertile offspring. Different appearance is not the test. The test is whether the two groups are **reproductively isolated**: they cannot interbreed to produce fertile offspring. Also, a barrier does not make two species by itself: it only starts the process.
:::

:::eg Spot the error: explain how a river that appears across a plain could lead to two species of mice. [3]
A student wrote this answer.

Line 1: The river is a barrier, so the mice on each side can no longer breed together and there is no gene flow.
Line 2: The river causes mutations in the mice, which make the two populations different.
Line 3: After many generations the two populations cannot interbreed, so they are different species.

Line 1 is correct [B1]. **Line 2 is wrong: a barrier does not cause mutations. Mutations are random and happen with or without a barrier. What makes the populations different is that the different environments give different selection pressures, so different alleles are favoured on each side. That mark is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "Mutations occur at random in each population, and different selection pressures on each side change the allele frequencies." With that change the answer scores 3 marks.
:::

:::tip A checklist for "explain how a new species forms"
Say, in order: **separated** (barrier or ecological or behavioural) → **no gene flow** → **different selection pressures, random mutations, drift** → **allele frequencies change** → **cannot interbreed to produce fertile offspring** → **separate species**. Name each link.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State what is meant by evolution, and say whether an individual or a population evolves.
A: Evolution is the process leading to new species from existing species over time, as a result of changes to the gene pools of populations from generation to generation. A population evolves, because what changes is the frequency of alleles in its gene pool; an individual keeps the alleles it has.
Q: A stretch of 12 bases in three lizard species is given. Count the differences between each pair and state which two species are most closely related.

| position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | G | A | T | T | A | C | C | G | T | A | A | C |
| L2 | G | A | T | T | G | C | C | G | T | A | A | C |
| L3 | G | C | T | T | G | C | C | G | T | C | A | C |

A: L1 and L2 differ at 1 position (5); L2 and L3 differ at 2 positions (2 and 10); L1 and L3 differ at 3 positions. L1 and L2 have the fewest differences, so they are the most closely related (they share the most recent common ancestor).
Q: Two species of frog differ at 30 of the 1200 bases of a gene. Calculate the percentage difference.
A: \(30 \div 1200 \times 100 = 2.5\%\).
Q: For those frogs, the two lineages together gain 5 differences per million years. Estimate the time since the frogs shared a common ancestor.
A: \(30 \div 5 = 6\) million years.
Q: Explain why cytochrome c can be used to compare very different organisms such as a fungus and a mammal.
A: Both respire aerobically, so both have cytochrome c in the electron transport chain. The protein changes slowly, so differences remain readable over a very long time, and the number of differences shows how closely related they are.
Q: A mountain range rises and divides a population of snails into two. State the type of speciation that may follow and give the key reason it can happen.
A: Allopatric speciation. The barrier stops gene flow, so the two populations change separately under different selection pressures and different mutations.
Q: Distinguish between prezygotic and postzygotic isolating mechanisms. Give one example of each.
A: Prezygotic mechanisms act before fertilisation, so the gametes do not meet, for example different breeding seasons. Postzygotic mechanisms act after fertilisation, for example a hybrid that is sterile because its chromosomes cannot pair in meiosis.
Q: Two groups of fish live in one lake. One feeds near the surface and the other near the bottom, and each spawns in its own zone. State the type of speciation and the form of separation.
A: Sympatric speciation, by ecological separation (different feeding habitat) with behavioural separation in the places where they spawn. There is no physical barrier.
Q: A student writes "Chimpanzees are less evolved than humans." Explain what is wrong with this.
A: Both lineages have had the same time since the common ancestor and both are adapted to their own environments. Evolution is a change in the gene pool of a population, with no "more" or "less" evolved, and no goal. Chimpanzees are not an earlier stage of humans.
Q: Explain why two populations that look different may still belong to one species.
A: Appearance is not the test of a species. If they can interbreed to produce fertile offspring they share a gene pool, whatever they look like.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State three processes that can change the allele frequencies in the gene pool of a population.
A: Mutation (new alleles arise). [B1]
Natural selection (alleles that improve survival and reproduction increase in frequency). [B1]
Genetic drift (random change, strongest in small populations) or gene flow (migration in or out). [B1]
Q: [3 marks] ★ Part of the gene for a protein was sequenced in three species of gecko. The table shows the number of base differences in a stretch of 200 bases.

| species | R | S | T |
|---|---|---|---|
| R | – | 4 | 22 |
| S | 4 | – | 22 |
| T | 22 | 22 | – |

(a) State which two species are most closely related and explain your answer. (b) Calculate the percentage difference between R and T.
A: (a) R and S are most closely related, because they have the fewest differences (4), so they shared a common ancestor more recently. [B1] [B1]
(b) \(22 \div 200 \times 100 = 11\%\) [B1]
Q: [5 marks] ★★ Fruit flies from one stock were split into two cages. For many generations, cage 1 flies were fed on starch food and cage 2 flies on maltose food. Flies from the two cages were then put together and the matings were counted (invented data).

| female from | male from cage 1 | male from cage 2 |
|---|---|---|
| cage 1 | 38 | 12 |
| cage 2 | 10 | 41 |

(a) Describe the pattern in the matings, using figures. (b) Explain how the result shows the first stage of speciation. (c) Suggest why the two groups cannot yet be called separate species.
H: Count the matings between flies from the same cage and from different cages, and give a percentage of the total.
H: For (c), what does the biological species definition need as well as mate preference?
A: (a) Most matings (79 of 101, or 78%) were between flies from the same cage, 38 in cage 1 and 41 in cage 2. [B1] Only 22 matings (22%) were between flies from different cages. [B1]
(b) The flies prefer mates from their own cage, so there is little gene flow between the two groups. [B1] If the cages stay separate, the different food gives different selection pressures and the gene pools diverge until the groups are reproductively isolated. [B1]
(c) Some matings between the cages still happen (22 of 101), so isolation is not complete, and fertile offspring from these matings would need to be tested. [B1]
Q: [5 marks] ★★ The table shows the number of amino acid differences in the same protein among five species of mammal, M, N, P, Q and R.

| species | M | N | P | Q | R |
|---|---|---|---|---|---|
| M | – | 2 | 8 | 8 | 14 |
| N | 2 | – | 8 | 8 | 14 |
| P | 8 | 8 | – | 4 | 14 |
| Q | 8 | 8 | 4 | – | 14 |
| R | 14 | 14 | 14 | 14 | – |

(a) Name the two pairs of species that are most closely related. (b) State which species separated from the others first, and explain how the data show this. (c) Explain why a comparison of the DNA base sequences would usually show more differences than the comparison of the proteins.
H: For (b), find the species that differs most from all the others.
H: For (c), think about the degenerate code and about DNA that is not translated.
A: (a) M and N, and P and Q, because these pairs have the fewest differences (2 and 4). [B1]
(b) Species R separated first. [B1] It differs from every other species by the largest number (14), so it shared a common ancestor with them longest ago. [B1]
(c) The genetic code is degenerate, so a base substitution may not change the amino acid (a silent mutation). [B1]
Some DNA is non-coding, so changes in it do not change the protein. [B1]
Q: [4 marks] ★★ For each situation, name the isolating mechanism or the type of speciation that applies. (a) Two moth species release different scents that attract males only of the same species. (b) A hybrid between two toad species hatches, but the tadpoles die. (c) Two orchid species growing together flower in different months. (d) Two snail populations live on opposite sides of a deep gorge that they cannot cross.
A: (a) Prezygotic isolation, by behaviour (the chemical signal). [B1]
(b) Postzygotic isolation, because the hybrid zygote develops but does not survive. [B1]
(c) Prezygotic isolation by the time of breeding (and, because they grow together, sympatric separation). [B1]
(d) Geographical separation, which may lead to allopatric speciation. [B1]
Q: [6 marks] ★★★ A plant species X has 2n = 14 chromosomes and a different species Y has 2n = 18. They sometimes cross to produce a hybrid with 16 chromosomes, which is sterile. Once, a hybrid plant doubled its chromosome number to 32 and was fertile. (a) Explain why the hybrid with 16 chromosomes is sterile. (b) Explain why the plant with 32 chromosomes is fertile and why it may be a new species.
H: What must happen to the chromosomes at the start of meiosis?
H: Would the 32-chromosome plant be able to breed with X or Y? Think about the offspring chromosome numbers.
A: (a) The 16 chromosomes come from two different species, so they are not homologous pairs. [B1] They cannot pair up in prophase I of meiosis, so meiosis fails and no viable gametes are formed. [B1]
(b) With 32 chromosomes, each chromosome has an identical partner (a homologous pair), so they pair and meiosis works. [B1] Fertile gametes are formed, so the plant can reproduce (by self-pollination). [B1]
A cross with X or Y gives offspring with an odd or unmatched number of chromosomes, which are sterile, so the 32-chromosome plant is reproductively isolated from X and Y. [B1]
It can interbreed only with others like itself, which is the biological species definition of a new species (formed in one generation, in the same area). [B1]
Q: [6 marks] ★★★ A mutation rate was measured for a gene of 1500 bases. Two species of fish, E and F, are known from fossils to have separated 5 million years ago, and their sequences of the gene differ at 45 bases. A third species, G, differs from E at 90 bases. (a) Calculate the number of differences per million years. (b) Estimate the time since E and G separated. (c) The rate of mutation was later found to be twice as fast in the lineage leading to G. Explain the effect on your estimate.
H: Rate = differences ÷ time for the calibration pair.
H: For (c), a faster rate in one lineage puts extra differences in the data that are not due to time.
A: (a) \(45 \div 5\) [M1] \(= 9\) differences per million years [A1]
(b) \(90 \div 9\) [M1] \(= 10\) million years [A1]
(c) The estimate assumes a constant rate. If the lineage to G mutated faster, then some of the 90 differences are due to the faster rate, not to time. [B1]
So 10 million years overestimates the time since E and G separated. [B1]
Q: [7 marks] ★★★ Two species of palm grow on a small oceanic island, a long way from any mainland. One grows on acidic soil and flowers early in the season; the other grows on alkaline soil and flowers late. Sequences of the same gene show that the two palm species are more closely related to each other than either is to any palm on the mainland. (a) Explain why these observations suggest sympatric rather than allopatric speciation. (b) Explain how the soil and the flowering times could have led to two species. (c) Suggest how the molecular clock could be used to test the idea, given that the age of the island is known.
H: (a) Is there a barrier inside the island? Where did the common ancestor of the two palms live?
H: (c) The palms cannot be older than the island if they arose on it.
A: (a) The two species live on the same small island with no barrier between them. [B1] They are closest relatives of each other, not of mainland palms, so they probably arose from one ancestral population on the island. [B1]
(b) Plants on acidic soil mostly pollinate plants on acidic soil, and the same for alkaline soil (ecological separation), so there is little gene flow. [B1] The different flowering times also stop pollen passing between the groups (behavioural or temporal separation). [B1] Different selection pressures on each soil change allele frequencies until the two groups are reproductively isolated. [B1]
(c) Count the base differences between the two palm species and use a calibrated rate to estimate the time since they separated. [B1] If the estimate is less than the age of the island, this supports speciation on the island. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Two populations of a species of frog lived on either side of a mountain range for a long time, and diverged. After the mountains eroded, the two populations met in a narrow zone, where they sometimes mated. The hybrid offspring were less likely to survive than offspring of frogs from the same population. In the zone of contact, females of both populations now prefer to mate with males whose call is typical of their own population, more strongly than females living far from the zone. Explain these observations.
H: Why do females that mate with the other population leave fewer surviving offspring?
H: Which alleles increase in frequency, and how does this change the isolation?
A: The populations diverged in allopatry, so mixing of the gene pools in the hybrid zone produces hybrids with poorer survival. [B1]
A female that mates with a male of the other population has offspring that are less likely to survive, so she leaves fewer surviving offspring. [B1]
A female that mates with a male of her own population has more surviving offspring. [B1]
So alleles for preferring her own population's call are passed on to more offspring and increase in frequency (natural selection). [B1]
The prezygotic barrier (behavioural isolation) becomes stronger in the zone of contact than in frogs far from it. [B1]
This reduces gene flow and so completes speciation: the two populations become reproductively isolated. [B1]
Q: [6 marks] ★★★ Biologists compared a fast-changing region of DNA in pairs of species whose date of separation was known from fossils. The table shows the number of differences per 100 bases.

| time since separation / million years | differences per 100 bases |
|---|---|
| 2 | 4 |
| 4 | 8 |
| 8 | 15 |
| 16 | 25 |
| 32 | 33 |

(a) Describe the relationship between the time since separation and the number of differences. (b) Suggest an explanation for the change in the relationship at large times. (c) Explain what this means for the use of this region as a molecular clock for old separations.
H: Compare the number of differences gained between 2 and 4 Myr with the number gained between 16 and 32 Myr.
H: A single position can change more than once. What does that do to the count?
A: (a) The number of differences rises as time increases, [B1] from 4 at 2 million years to 33 at 32 million years, [B1] but the rise becomes less steep: at first about 2 differences per million years (4 at 2 Myr, 8 at 4 Myr), later only about 0.5 (25 at 16 Myr to 33 at 32 Myr). [B1]
(b) At large times many positions have already changed, so a further mutation often hits a position that has already changed, [B1] or changes it back to the original base, so the extra change is not counted as a new difference. [B1]
(c) The clock is reliable only for recent separations. For old separations the number of differences underestimates the time, so the dates are too recent. [B1]
:::

:::quiz
? Which statement about evolution is correct?
+ The frequency of alleles in the gene pool of a population changes over generations.
- An individual changes its alleles to fit its environment.
- Evolution is always a change from simple to complex organisms.
- Species that look more like their ancestors are less evolved.
> Evolution is a change in the gene pool of populations. Individuals cannot change their alleles, and no living species is more or less evolved than another.
? Two species have a gene that differs at 3 out of 60 bases, and two other species have the same gene differing at 12 out of 60 bases. What is the best conclusion?
+ The first pair shared a common ancestor more recently, if the mutation rate is constant.
- The first pair are less evolved.
- The second pair can interbreed more easily.
- The first pair have a smaller genome.
> More differences mean a longer time since the common ancestor, if the rate is constant. Differences give no information on "evolved", on breeding or on genome size.
? Why is cytochrome c useful for comparing distantly related species?
+ Every organism that respires aerobically has it, and it changes slowly.
- It has no mutations, so all organisms have the same sequence.
- It changes faster than any other protein.
- It is found only in mitochondria of animals.
> Cytochrome c is in the electron transport chain of all aerobic organisms. It changes slowly, so differences stay readable over long times. It does mutate, and it is not limited to animals.
? Two populations were separated for a long time by a barrier that has now gone. Which observation is the best evidence that they are now separate species?
+ When they meet they do not interbreed to produce fertile offspring.
- The two populations look different from each other.
- The two populations live in different places.
- The two populations have some different alleles.
> The test is reproductive isolation. Populations of one species can look different, live apart and have different alleles and still interbreed to produce fertile offspring.
? Which is an example of sympatric speciation?
+ Two groups of grasses in one meadow flower at different times of year and diverge.
- Two groups of mice are separated by a new river and diverge.
- Two groups of birds on separate islands diverge.
- Two groups of fish in lakes cut off by a landslide diverge.
> Sympatric speciation happens in the same area, without a physical barrier. The other three involve a barrier, which is allopatric.
? Which is a postzygotic isolating mechanism?
+ A hybrid zygote forms but the adult is sterile.
- The two species breed in different seasons.
- The two species have different courtship songs.
- The two species live in different habitats.
> Postzygotic mechanisms act after fertilisation. The other three stop the gametes from meeting at all, so they are prezygotic.
? Which is a limitation of the molecular clock?
+ The mutation rate may not be constant between genes and lineages.
- Sequences cannot be compared when species look different.
- It can be used only if there are no fossils.
- The number of differences does not change with time.
> If the rate varies, the dates are only estimates. The clock works for species that look different, and it is calibrated using fossils.
? A hybrid has an odd number of chromosomes and is sterile. Why?
+ The chromosomes cannot form homologous pairs in meiosis.
- The chromosomes are too small to be seen.
- The hybrid has no DNA.
- Its mitochondria are destroyed in meiosis.
> In meiosis I homologous chromosomes pair. With an odd number, or chromosomes from different species, they cannot all pair, and normal gametes are not made.
? Which pair of terms is correctly matched?
+ speciation: formation of a new species from an existing one
- gene flow: the formation of a new species
- reproductive isolation: individuals moving between populations
- molecular clock: the speed of natural selection
> Gene flow is movement of alleles between populations, and reproductive isolation is the failure to interbreed. The molecular clock times a divergence.
:::

:::checklist What you can now do
- [ ] I can outline evolution as the formation of new species from existing species as a result of changes to gene pools, and state that populations, not individuals, evolve.
- [ ] I can discuss how DNA sequence data can show evolutionary relationships, including the molecular clock, its strengths and its limitations.
- [ ] I can compare sequences, count differences and percentage differences, and build a simple tree from a table of differences.
- [ ] I can explain allopatric speciation as the result of geographical separation, in the correct order.
- [ ] I can explain sympatric speciation as the result of ecological and behavioural separation.
- [ ] I can distinguish prezygotic and postzygotic isolating mechanisms, and explain polyploidy in plants.
:::

:::recap
- Evolution: new species from existing species, from changes to the gene pools of populations. Four processes change a gene pool: mutation, natural selection, genetic drift, gene flow. Populations evolve, individuals do not.
- Biological species: can interbreed to produce fertile offspring and are reproductively isolated from other species.
- Sequence evidence: more differences in DNA or protein means a longer time since the common ancestor. The two lineages share the differences, so branch length is half of the difference. Cytochrome c (slow) suits distant relatives; mitochondrial DNA (fast) suits close ones.
- Molecular clock: assumes a steady rate and is calibrated with fossils. Limits: the rate varies, hidden changes (multiple hits, back mutations), incomplete fossils, silent mutations.
- Allopatric speciation: barrier, no gene flow, different selection pressures, mutations and drift, allele frequencies diverge, cannot interbreed. Barriers do not cause mutation.
- Sympatric speciation: same area; ecological (habitat, food) or behavioural (courtship, breeding time) separation; polyploidy in plants is speciation in one step.
- Isolating mechanisms: prezygotic (gametes never meet) and postzygotic (hybrid fails or is sterile).
:::

:::links
- read: [CAIE A Level Biology: selection and evolution notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/selection-and-evolution/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Selection and evolution (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/17-selection-and-evolution/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- read: [Evolution and the origin of species](https://openstax.org/books/biology-2e/pages/18-introduction) · OpenStax Biology 2e · free university textbook chapter on speciation, beyond the syllabus in places
- explore: [Natural selection simulation](https://phet.colorado.edu/en/simulations/natural-selection) · PhET · change the environment and watch allele frequencies shift over generations
- explore: [Evolution](https://learn.genetics.utah.edu/content/evolution/) · Learn.Genetics (University of Utah) · short interactive explanations of evolution and relationships between species
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find the evolution and speciation questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Classification](#bio.classification) shows how species are named and sorted into groups.
