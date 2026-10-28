@chapter bio.dna
@title Nucleic acids and DNA replication
@level as
@paper CAIE 9700 Papers 1 and 2
@time 4–5 hours
@summary DNA and RNA are polymers of nucleotides. You will learn the structure of a nucleotide (and of ATP), the purine and pyrimidine bases, how phosphodiester bonds build a polynucleotide, why the two strands of the DNA double helix are antiparallel and held by hydrogen bonds between complementary bases, how DNA is copied semi-conservatively in S phase with DNA polymerase and DNA ligase, how messenger RNA differs from DNA, and how Meselson and Stahl tested the model.

:::why
Your cells hold the instructions for making you in a molecule that is the same in every cell, and each time a cell divides it must copy those instructions without a single page missing. DNA is built to do exactly that: a four-letter code that can be read, and a structure that can be copied accurately. The same chemistry explains how viruses are stopped by drugs, how forensic scientists identify people and how mutations arise. Exam questions ask you to describe structures, apply base pairing to numbers and sequences, explain the 5′ and 3′ directions, and interpret the data that proved how DNA is copied.
:::

**Before you start**, you should know condensation reactions and polymers from [Carbohydrates](#bio.carbs) and [Proteins](#bio.proteins), enzymes and complementary shapes from [Enzymes](#bio.enzymes), and the S phase of the cell cycle and sister chromatids from [Chromosomes and the mitotic cell cycle](#bio.mitosis).

:::try Warm-up
Q: Name the type of reaction that joins monomers to make a polymer, and say what small molecule is released. (from [Carbohydrates](#bio.carbs))
A: A condensation reaction; a molecule of water is released each time two monomers join.
Q: In which part of the cell cycle is DNA replicated, and how many sister chromatids does each chromosome have afterwards? (from [Chromosomes and the mitotic cell cycle](#bio.mitosis))
A: S phase of interphase. Each chromosome then has two identical sister chromatids.
Q: A hydrogen bond is weak. Explain how a protein can still be held in shape by hydrogen bonds. (from [Proteins](#bio.proteins))
A: There are very many hydrogen bonds between R groups and along the chain, and together they are strong enough to hold the tertiary structure, but each can break when conditions change.
:::

## Nucleotides: the monomers of nucleic acids

There are two kinds of **nucleic acid**: DNA (deoxyribonucleic acid) and RNA (ribonucleic acid). Each is a long chain, a polymer, and its monomer is the nucleotide. DNA stores the instructions of the cell. RNA copies part of those instructions and helps to use them (see [Protein synthesis and gene mutation](#bio.synthesis)).

:::def Nucleotide
The monomer of a nucleic acid. It is made of three parts joined together: a pentose sugar, a phosphate group and a nitrogenous base.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 206" role="img" aria-label="A nucleotide has three parts: a phosphate group joined to a pentose sugar (a five-carbon ring), and a nitrogenous base joined to the sugar."><path class="fm s-acc sw2" d="M150 78L188 104L174 148L126 148L112 104Z"/><path class="ln" d="M112 104L88 80"/><path class="ln" d="M88 80L72 66"/><circle class="f2 s-acc2 sw2" cx="62" cy="56" r="14"/><text class="tl tb" x="62" y="61" text-anchor="middle">P</text><path class="f1 s-acc sw2" d="M292 104L277 130L247 130L232 104L247 78L277 78Z"/><path class="ln" d="M188 104L232 104"/><path class="ln" d="M126 148L126 166"/><text class="tl tb" x="262" y="109" text-anchor="middle">B</text><text class="tl" x="96" y="36">phosphate group</text><path class="ln-m thin" d="M92 38L76 49"/><text class="tl" x="150" y="192" text-anchor="middle">pentose sugar</text><path class="ln-m thin" d="M150 178L150 150"/><text class="tl" x="262" y="154" text-anchor="middle">nitrogenous</text><text class="tl" x="262" y="168" text-anchor="middle">base</text><path class="ln-m thin" d="M262 142L262 135"/></svg><figcaption>A nucleotide (a simplified drawing, not a structural formula). The phosphate group is joined to the pentose sugar, and the nitrogenous base is joined to the other side of the sugar. In DNA the sugar is deoxyribose; in RNA it is ribose.</figcaption></figure>
:::

The **pentose sugar** is a ring of five carbon atoms (hence "pentose"), numbered 1′ to 5′. The small mark after each number is read "prime" and separates the sugar's carbons from the atoms of the base. The phosphate group is joined to carbon 5′ and the base is joined to carbon 1′. The sugar in DNA nucleotides is **deoxyribose**; in RNA nucleotides it is **ribose**. Deoxyribose has one fewer oxygen atom than ribose, which is why the DNA sugar has "deoxy" in its name.

The **nitrogenous base** contains nitrogen and has a ring structure. DNA contains four bases, adenine (A), guanine (G), cytosine (C) and thymine (T). RNA contains adenine, guanine, cytosine and **uracil (U)**, which takes the place of thymine. (You do not need to draw the structures of the sugars or bases; the exam only asks for the shapes shown in the figures.)

### Purines and pyrimidines

The bases fall into two groups by the size of their rings.

:::def Purine
A nitrogenous base with a double ring structure. The purines are adenine (A) and guanine (G).
:::

:::def Pyrimidine
A nitrogenous base with a single ring structure. The pyrimidines are cytosine (C), thymine (T) and uracil (U).
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 232" role="img" aria-label="The five bases drawn as rings. Cytosine, thymine and uracil are pyrimidines with a single ring. Adenine and guanine are purines with a double ring (a six-sided ring joined to a five-sided ring)."><text class="tl tb" x="165" y="18" text-anchor="middle">pyrimidines: one ring</text><path class="f1 s-acc sw2" d="M74.1 67L55 78L35.9 67L35.9 45L55 34L74.1 45Z"/><text class="tl tb" x="55" y="61" text-anchor="middle">C</text><text class="tl" x="55" y="100" text-anchor="middle">cytosine</text><path class="f1 s-acc sw2" d="M184.1 67L165 78L145.9 67L145.9 45L165 34L184.1 45Z"/><text class="tl tb" x="165" y="61" text-anchor="middle">T</text><text class="tl" x="165" y="100" text-anchor="middle">thymine</text><path class="f1 s-acc sw2" d="M294.1 67L275 78L255.9 67L255.9 45L275 34L294.1 45Z"/><text class="tl tb" x="275" y="61" text-anchor="middle">U</text><text class="tl" x="275" y="100" text-anchor="middle">uracil</text><text class="tl tb" x="165" y="132" text-anchor="middle">purines: two rings</text><path class="f2 s-acc2 sw2" d="M89.1 183L70 194L50.9 183L50.9 161L70 150L89.1 161Z"/><path class="f2 s-acc2 sw2" d="M89.1 161L110 154.2L123 172L110 189.8L89.1 183Z"/><text class="tl tb" x="70" y="177" text-anchor="middle">A</text><text class="tl" x="90" y="216" text-anchor="middle">adenine</text><path class="f2 s-acc2 sw2" d="M229.1 183L210 194L190.9 183L190.9 161L210 150L229.1 161Z"/><path class="f2 s-acc2 sw2" d="M229.1 161L250 154.2L263 172L250 189.8L229.1 183Z"/><text class="tl tb" x="210" y="177" text-anchor="middle">G</text><text class="tl" x="230" y="216" text-anchor="middle">guanine</text></svg><figcaption>The bases (simplified ring shapes, not structural formulae). A pyrimidine has one ring and a purine has two, so a purine is larger. DNA contains A, G, C and T; RNA contains A, G, C and U.</figcaption></figure>
:::

| base | group | rings | found in |
|---|---|---|---|
| adenine (A) | purine | 2 | DNA and RNA |
| guanine (G) | purine | 2 | DNA and RNA |
| cytosine (C) | pyrimidine | 1 | DNA and RNA |
| thymine (T) | pyrimidine | 1 | DNA only |
| uracil (U) | pyrimidine | 1 | RNA only |

:::tip Remember which is which
Think "**cut** the py**ramid**": the pyrimidines are **C**, **U** and **T**. The purines are the other two, A and G, and they are the larger molecules, with two rings.
:::

:::key Nucleotides in one box
- A nucleotide = **pentose sugar + phosphate group + nitrogenous base**.
- DNA sugar: **deoxyribose**. RNA sugar: **ribose**.
- **Purines** (A, G): double ring. **Pyrimidines** (C, T, U): single ring.
- DNA bases: A, G, C, T. RNA bases: A, G, C, U.
:::

### ATP: a phosphorylated nucleotide

You will meet ATP again as the molecule that supplies energy in cells (see [Energy, ATP and respiratory quotient](#bio.energy)). Its structure is that of a nucleotide.

:::def ATP (adenosine triphosphate)
A phosphorylated nucleotide. It is made of the base adenine, the sugar ribose and three phosphate groups in a chain.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 310 134" role="img" aria-label="ATP is a nucleotide: the base adenine joined to the sugar ribose, which carries a chain of three phosphate groups."><path class="f1 s-acc sw2" d="M61.3 64L44 74L26.7 64L26.7 44L44 34L61.3 44Z"/><path class="f1 s-acc sw2" d="M61.3 44L80.3 37.8L92.1 54L80.3 70.2L61.3 64Z"/><text class="tl tb" x="44" y="59" text-anchor="middle">A</text><path class="ln" d="M80.3 54L100 54"/><path class="fm s-acc sw2" d="M122 36L141 50L134 72L110 72L103 50Z"/><path class="ln" d="M141 54L176 54"/><circle class="f2 s-acc2 sw2" cx="190" cy="54" r="14"/><text class="tl tb" x="190" y="59" text-anchor="middle">P</text><path class="ln" d="M204 54L218 54"/><circle class="f2 s-acc2 sw2" cx="232" cy="54" r="14"/><text class="tl tb" x="232" y="59" text-anchor="middle">P</text><path class="ln" d="M246 54L260 54"/><circle class="f2 s-acc2 sw2" cx="274" cy="54" r="14"/><text class="tl tb" x="274" y="59" text-anchor="middle">P</text><text class="tl" x="44" y="108" text-anchor="middle">adenine</text><path class="ln-m thin" d="M44 96L44 78"/><text class="tl" x="122" y="108" text-anchor="middle">ribose</text><path class="ln-m thin" d="M122 96L122 74"/><text class="tl" x="232" y="108" text-anchor="middle">three phosphate</text><text class="tl" x="232" y="122" text-anchor="middle">groups</text><path class="ln-m thin" d="M232 96L232 70"/></svg><figcaption>ATP (adenosine triphosphate), a simplified drawing. It is the nucleotide with the base adenine and the sugar ribose, with two extra phosphate groups added to the first one: a phosphorylated nucleotide.</figcaption></figure>
:::

"Phosphorylated" means that extra phosphate groups have been added. ATP is the RNA nucleotide that contains adenine, with two more phosphate groups joined to its first one. When one of the phosphate groups is removed by hydrolysis, ATP becomes ADP (adenosine diphosphate) and energy is released for the cell to use.

## Polynucleotides and the phosphodiester bond

Nucleotides are joined into chains by condensation reactions.

:::def Phosphodiester bond
A covalent bond that joins two nucleotides. It forms between the phosphate group on carbon 5′ of one nucleotide and the hydroxyl (OH) group on carbon 3′ of the next, in a condensation reaction that releases a molecule of water.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 350" role="img" aria-label="Two nucleotides joined. The phosphate group on the 5′ carbon of the lower nucleotide forms a phosphodiester bond with the hydroxyl group on the 3′ carbon of the upper nucleotide. The upper end has a free phosphate group (the 5′ end) and the lower end has a free OH group (the 3′ end)."><path class="fm s-acc sw2" d="M150 92L188 118L174 162L126 162L112 118Z"/><path class="ln" d="M112 118L88 94"/><path class="ln" d="M88 94L72 80"/><circle class="f2 s-acc2 sw2" cx="62" cy="70" r="14"/><text class="tl tb" x="62" y="75" text-anchor="middle">P</text><path class="f1 s-acc sw2" d="M292 118L277 144L247 144L232 118L247 92L277 92Z"/><path class="ln" d="M188 118L232 118"/><text class="tl tb" x="262" y="123" text-anchor="middle">B</text><path class="fm s-acc sw2" d="M150 222L188 248L174 292L126 292L112 248Z"/><path class="ln" d="M112 248L88 224"/><path class="ln" d="M88 224L72 210"/><circle class="f2 s-acc2 sw2" cx="62" cy="200" r="14"/><text class="tl tb" x="62" y="205" text-anchor="middle">P</text><path class="f1 s-acc sw2" d="M292 248L277 274L247 274L232 248L247 222L277 222Z"/><path class="ln" d="M188 248L232 248"/><path class="ln" d="M126 292L126 310"/><text class="tl tb" x="262" y="253" text-anchor="middle">B</text><path class="c2 sw3" d="M126 162L72 190"/><text class="tl tb" x="16" y="18">5′ end: free phosphate group</text><path class="ln-m thin" d="M62 24L62 40"/><text class="tl" x="160" y="206">phosphodiester bond</text><path class="ln-m thin" d="M156 202L99 177"/><text class="tl tb" x="160" y="336">3′ end: free OH group</text><path class="ln-m thin" d="M152 332L130 322"/><text class="tl" x="84" y="126" text-anchor="end">5′</text><text class="tl" x="110" y="146" text-anchor="end">4′</text><text class="tl" x="138" y="178">3′</text><text class="tl" x="196" y="102">1′</text><text class="tl" x="190" y="160">2′</text></svg><figcaption>A phosphodiester bond joins two nucleotides (simplified). The carbon atoms of the sugar are numbered 1′ to 5′. The bond forms between the 3′ carbon of one nucleotide and the phosphate group on the 5′ carbon of the next, and a molecule of water is lost.</figcaption></figure>
:::

Repeating this reaction builds a **polynucleotide**. Every nucleotide is added to the 3′ carbon of the last one, so the chain has a repeating **sugar–phosphate backbone**: sugar, phosphate, sugar, phosphate, and so on. The bases stick out sideways from the backbone and carry the information.

A polynucleotide has two different ends, and you must keep track of them:
- the **5′ end** has a free phosphate group on the 5′ carbon of its first sugar;
- the **3′ end** has a free hydroxyl (OH) group on the 3′ carbon of its last sugar.

Biologists always read and write a polynucleotide from its 5′ end to its 3′ end. Because every bond in the backbone is a strong covalent bond, a strand of DNA is stable and does not fall to pieces when the cell is warm.

:::warn Which bond is which?
- **Phosphodiester bonds** join nucleotides **within** a strand (covalent, strong).
- **Hydrogen bonds** join the bases of **two different** strands (weak, but many).
Never write that hydrogen bonds join one nucleotide to the next in a strand.
:::

:::eg Describe how a polynucleotide is formed from nucleotides.
Build the answer in order, with the reaction first.

Two nucleotides join in a condensation reaction, in which a molecule of water is removed. [B1]

The phosphate group on the 5′ carbon of one nucleotide bonds to the hydroxyl group on the 3′ carbon of the next, forming a phosphodiester bond. [B1]

Repeating this adds more nucleotides, forming a chain with a sugar–phosphate backbone and the bases projecting from it. [B1]

A weaker answer says "the nucleotides join together with bonds". It does not name the reaction or the bond and gets no mark for the position of the bond on the sugar.
:::

:::eg A polynucleotide has 25 nucleotides. Calculate the number of phosphodiester bonds in it and the number of water molecules released as it was made.
Each phosphodiester bond joins **two** neighbouring nucleotides, so a chain of \(n\) nucleotides has \(n - 1\) bonds.

\[\begin{aligned} \text{bonds} &= 25 - 1 \\ &= 24 \end{aligned}\]

One water molecule is released for each bond, so 24 water molecules. [M1] [A1]

Check with a short chain: 3 nucleotides have 2 bonds (one between 1 and 2, one between 2 and 3).
:::

## The DNA double helix

A DNA molecule is made of **two** polynucleotide strands, wound round each other into a double helix. The strands are held together by hydrogen bonds between their bases.

### Complementary base pairing

The bases on one strand pair with the bases on the other strand in a fixed way, called **complementary base pairing**.

:::def Complementary base pairing
The pairing of adenine (A) with thymine (T) and of cytosine (C) with guanine (G) by hydrogen bonds between two strands of a nucleic acid. (In RNA, adenine pairs with uracil.)
:::

- **A pairs with T** and is held by **two hydrogen bonds**.
- **C pairs with G** and is held by **three hydrogen bonds**.

Each pair is **one purine and one pyrimidine**. This is why the helix is the same width all the way along: a purine plus a pyrimidine is always the same length. Two purines would be too wide to fit and two pyrimidines too narrow to be held together by hydrogen bonds.

Because there are more hydrogen bonds between C and G, a stretch of DNA that is rich in C–G pairs needs more energy to separate than one rich in A–T pairs.

:::html
<figure class="fig small"><svg viewBox="0 0 340 384" role="img" aria-label="A DNA double helix drawn as a flat ladder. Two sugar-phosphate backbones run in opposite directions: the left strand from 5′ at the top to 3′ at the bottom, the right strand from 5′ at the bottom to 3′ at the top. Each rung is a purine joined to a pyrimidine by hydrogen bonds: A with T by two hydrogen bonds, C with G by three."><path class="c1 sw3" d="M40 42L40 322" marker-end="url(#ahs)"/><path class="c2 sw3" d="M178 322L178 42" marker-end="url(#ahs)"/><rect class="f2 s-acc2 sw2" x="45" y="54" width="52" height="24"/><rect class="f1 s-acc sw2" x="135" y="54" width="38" height="24"/><text class="tl tb" x="71" y="71" text-anchor="middle">A</text><text class="tl tb" x="154" y="71" text-anchor="middle">T</text><path class="ln-m thin dash" d="M100 60L132 60"/><path class="ln-m thin dash" d="M100 72L132 72"/><rect class="f1 s-acc sw2" x="45" y="94" width="38" height="24"/><rect class="f2 s-acc2 sw2" x="121" y="94" width="52" height="24"/><text class="tl tb" x="64" y="111" text-anchor="middle">C</text><text class="tl tb" x="147" y="111" text-anchor="middle">G</text><path class="ln-m thin dash" d="M86 100L118 100"/><path class="ln-m thin dash" d="M86 106L118 106"/><path class="ln-m thin dash" d="M86 112L118 112"/><rect class="f1 s-acc sw2" x="45" y="134" width="38" height="24"/><rect class="f2 s-acc2 sw2" x="121" y="134" width="52" height="24"/><text class="tl tb" x="64" y="151" text-anchor="middle">T</text><text class="tl tb" x="147" y="151" text-anchor="middle">A</text><path class="ln-m thin dash" d="M86 140L118 140"/><path class="ln-m thin dash" d="M86 152L118 152"/><rect class="f2 s-acc2 sw2" x="45" y="174" width="52" height="24"/><rect class="f1 s-acc sw2" x="135" y="174" width="38" height="24"/><text class="tl tb" x="71" y="191" text-anchor="middle">G</text><text class="tl tb" x="154" y="191" text-anchor="middle">C</text><path class="ln-m thin dash" d="M100 180L132 180"/><path class="ln-m thin dash" d="M100 186L132 186"/><path class="ln-m thin dash" d="M100 192L132 192"/><rect class="f2 s-acc2 sw2" x="45" y="214" width="52" height="24"/><rect class="f1 s-acc sw2" x="135" y="214" width="38" height="24"/><text class="tl tb" x="71" y="231" text-anchor="middle">A</text><text class="tl tb" x="154" y="231" text-anchor="middle">T</text><path class="ln-m thin dash" d="M100 220L132 220"/><path class="ln-m thin dash" d="M100 232L132 232"/><rect class="f1 s-acc sw2" x="45" y="254" width="38" height="24"/><rect class="f2 s-acc2 sw2" x="121" y="254" width="52" height="24"/><text class="tl tb" x="64" y="271" text-anchor="middle">C</text><text class="tl tb" x="147" y="271" text-anchor="middle">G</text><path class="ln-m thin dash" d="M86 260L118 260"/><path class="ln-m thin dash" d="M86 266L118 266"/><path class="ln-m thin dash" d="M86 272L118 272"/><circle class="fp ln" cx="40" cy="86" r="5"/><circle class="fp ln" cx="178" cy="86" r="5"/><circle class="fp ln" cx="40" cy="126" r="5"/><circle class="fp ln" cx="178" cy="126" r="5"/><circle class="fp ln" cx="40" cy="166" r="5"/><circle class="fp ln" cx="178" cy="166" r="5"/><circle class="fp ln" cx="40" cy="206" r="5"/><circle class="fp ln" cx="178" cy="206" r="5"/><circle class="fp ln" cx="40" cy="246" r="5"/><circle class="fp ln" cx="178" cy="246" r="5"/><text class="tl tb" x="40" y="30" text-anchor="middle">5′</text><text class="tl tb" x="178" y="30" text-anchor="middle">3′</text><text class="tl tb" x="40" y="344" text-anchor="middle">3′</text><text class="tl tb" x="178" y="344" text-anchor="middle">5′</text><text class="tl" x="204" y="62">A–T pair:</text><text class="tl" x="204" y="76">2 hydrogen bonds</text><text class="tl" x="204" y="102">C–G pair:</text><text class="tl" x="204" y="116">3 hydrogen bonds</text><text class="tl" x="204" y="158">sugar–phosphate</text><text class="tl" x="204" y="172">backbone</text><path class="ln-m thin" d="M200 160L182 160"/><text class="tl" x="204" y="210">phosphodiester</text><text class="tl" x="204" y="224">bond</text><path class="ln-m thin" d="M200 212L183 206"/><text class="tl" x="109" y="372" text-anchor="middle">bases pair across the helix</text></svg><figcaption>DNA (simplified, untwisted). The strands are antiparallel: the left strand runs 5′ to 3′ downwards and the right strand 5′ to 3′ upwards. A purine always pairs with a pyrimidine, so every rung is the same length. A–T has two hydrogen bonds and C–G has three.</figcaption></figure>
:::

### Antiparallel strands

The two strands run in opposite directions. If one strand is read from 5′ to 3′ downwards, the other must be read from 5′ to 3′ upwards. We say that they are **antiparallel**. The strands fit together only if they run this way, because the phosphate end of one strand is level with the hydroxyl end of the other.

:::analogy Two lanes of a motorway
Think of each strand as a lane of a motorway. The traffic in one lane travels north (5′ to 3′) and in the other lane south, so the two lanes run side by side in opposite directions.
:::

:::key The structure of DNA
1. Two **polynucleotide** strands wound into a **double helix**.
2. Each strand has a **sugar–phosphate backbone**, with nucleotides joined by **phosphodiester bonds**.
3. The strands are **antiparallel** (one runs 5′ to 3′, the other 3′ to 5′).
4. **Complementary base pairing**: A–T (two hydrogen bonds) and C–G (three hydrogen bonds); a purine always pairs with a pyrimidine, so the width is constant.
5. The sequence of bases carries the genetic information.
:::

:::story How the double helix was found
In 1953 James Watson and Francis Crick built a model of the double helix. It fitted X-ray pictures of DNA taken by Rosalind Franklin and her student Raymond Gosling, and the finding by Erwin Chargaff that, in the DNA of every organism he tested, the amount of A equals the amount of T and the amount of C equals the amount of G. The model also showed at once how DNA could be copied.
:::

### Working with complementary strands

If you know the sequence of one strand, the other follows from the pairing rules, as long as you keep the directions right.

:::eg One strand of DNA reads 5′–GATTACA–3′. Write the sequence of the complementary strand and label its ends.
Pair each base: G with C, A with T, T with A, T with A, A with T, C with G, A with T. Write the new strand under the first, **with the ends reversed** because the strands are antiparallel.

\[\begin{aligned} &5′\text{–GATTACA–}3′ \\ &3′\text{–CTAATGT–}5′ \end{aligned}\]

The complementary strand reads 3′–CTAATGT–5′ [M1], which is 5′–TGTAATC–3′ when it is written from its 5′ end. [A1]
:::

:::exam Always label the ends
If the question gives the strand 5′ to 3′, the complementary strand under it is 3′ to 5′. If you are asked to write it the usual way, from 5′ to 3′, reverse it. Examiners give the mark only when the ends are labelled correctly.
:::

### Base ratios

In a double-stranded DNA molecule every A is paired with a T and every C with a G, so:

:::key Base ratios in double-stranded DNA
- The number of A = the number of T, and the number of C = the number of G.
- The total of purines (A + G) = the total of pyrimidines (T + C), each 50% of the bases.
- If you know the percentage of one base, you can find all four.
:::

:::eg The table shows the percentages of the four bases in samples of DNA from two species (invented values). Describe the pattern in the table and explain it.
| species | A / % | T / % | G / % | C / % |
|---|---|---|---|---|
| X | 31 | 31 | 19 | 19 |
| Y | 22 | 22 | 28 | 28 |

In both samples the percentage of A equals the percentage of T, and the percentage of G equals the percentage of C. [B1]

This is because DNA is double-stranded and A pairs with T and C pairs with G, so they are present in equal numbers. [B1]

Each pair contains one purine and one pyrimidine, so purines (A + G) and pyrimidines (T + C) are each 50% of the bases (31 + 19 = 50 and 22 + 28 = 50). [B1]

(Also credit: the ratio of A + T to G + C differs between species, 62 : 38 for X and 44 : 56 for Y, so it is the sequence that makes species different.)

A weaker answer says "the numbers are the same". It does not say which pairs are equal or give the reason.
:::

:::eg A double-stranded DNA molecule has 4000 nucleotides in total, and 28% of them are adenine. Calculate the number of each base and the number of hydrogen bonds between the strands.
**Step 1: A and T.** 28% of 4000 is the number of adenine nucleotides:

\[\begin{aligned} \text{A} &= 0.28 \times 4000 = 1120 \\ \text{T} &= \text{A} = 1120 \end{aligned}\]

**Step 2: G and C.** The rest of the nucleotides are G and C, in equal numbers:

\[\begin{aligned} \text{G} + \text{C} &= 4000 - 2 \times 1120 = 1760 \\ \text{G} = \text{C} &= 880 \end{aligned}\]

[M1] [A1]

**Step 3: hydrogen bonds.** The number of A–T pairs is 1120, with two bonds each. The number of C–G pairs is 880, with three bonds each:

\[\begin{aligned} \text{hydrogen bonds} &= 1120 \times 2 + 880 \times 3 \\ &= 2240 + 2640 \\ &= 4880 \end{aligned}\]

[M1] [A1]
:::

## RNA and messenger RNA

RNA is also a polynucleotide, but it is different from DNA in several ways. The type you need is **messenger RNA (mRNA)**, the molecule that carries a copy of a gene from the DNA in the nucleus to the ribosomes in the cytoplasm (the next chapter, [Protein synthesis and gene mutation](#bio.synthesis), shows how it is made and used).

:::def Messenger RNA (mRNA)
A single polynucleotide strand, made by copying one gene of a DNA molecule, that carries the information for the sequence of amino acids in a polypeptide from the nucleus to a ribosome.
:::

The structure of mRNA:
- It is **one** polynucleotide strand, not a double helix. It has no second strand and no hydrogen-bonded base pairs along its length.
- Its nucleotides contain the sugar **ribose**, a phosphate group and a base, joined by phosphodiester bonds to make a sugar–phosphate backbone.
- Its bases are **A, G, C and uracil (U)**. Uracil is a pyrimidine and, in RNA, it pairs with adenine.
- It is much **shorter** than DNA, because it is a copy of one gene and not of a whole chromosome.
- Groups of three bases along it are **codons**, which each stand for one amino acid.

| feature | DNA | mRNA |
|---|---|---|
| number of strands | two (double helix) | one |
| sugar | deoxyribose | ribose |
| bases | A, G, C, T | A, G, C, U |
| pyrimidine bases | C and T | C and U |
| base pairing along the molecule | yes, A–T and C–G | no |
| length | very long (a whole chromosome) | short (one gene) |
| where it is found | nucleus (and mitochondria and chloroplasts) | made in the nucleus, works at ribosomes in the cytoplasm |
| main job | stores genetic information | carries a copy of a gene to a ribosome |

:::warn Uracil pairs with adenine, not thymine
There is no thymine in RNA. When mRNA is made from DNA, an A on the DNA is paired with **U**, not with T. Never write "uracil pairs with thymine".
:::

:::eg Compare the structure of a DNA molecule with that of an mRNA molecule.
Any four points, each with a comparison, count.

DNA is two polynucleotide strands (a double helix), whereas mRNA is a single polynucleotide strand. [B1]

DNA nucleotides contain deoxyribose, whereas mRNA nucleotides contain ribose. [B1]

DNA contains the base thymine, whereas mRNA contains uracil instead. [B1]

DNA has base pairs joined by hydrogen bonds, whereas mRNA does not. [B1]

(Also credit: DNA is much longer than mRNA; both have a sugar–phosphate backbone with phosphodiester bonds; both contain A, C and G.)

A weaker answer lists features of one molecule only ("DNA has a double helix and mRNA is single"), or says "mRNA has uracil" without saying that DNA has thymine. Comparison needs both sides.
:::

## DNA replication

Before a cell divides, its DNA must be copied. This happens in **S phase** (see [Chromosomes and the mitotic cell cycle](#bio.mitosis)). Each new DNA molecule must be an exact copy of the old one, so the copying uses the old strands as templates.

:::def Semi-conservative replication
The way in which DNA is copied so that each new DNA molecule contains one original (old) strand and one newly made strand.
:::

### How DNA is replicated

:::steps
1. The double helix **unwinds** and its two strands **separate**, as the hydrogen bonds between the bases break. Each strand is now a **template**. The point where the strands separate is the **replication fork**.
2. **Free nucleotides** in the nucleus pair with the exposed bases of each template strand by **complementary base pairing** (A with T, C with G), held by hydrogen bonds.
3. **DNA polymerase** joins the free nucleotides to the end of the new strand, forming **phosphodiester bonds**. It adds nucleotides only to the **3′ end** of a growing strand.
4. The new strand on one template is made continuously (the **leading strand**). The new strand on the other template is made in short pieces (the **lagging strand**).
5. **DNA ligase** joins the pieces of the lagging strand together by forming phosphodiester bonds.
6. Each original strand and its new partner twist into a double helix. There are now **two identical DNA molecules**, each with one old strand and one new strand.
:::

:::def DNA polymerase
An enzyme that joins nucleotides, using one strand of DNA as a template, to make a new polynucleotide. It forms phosphodiester bonds and adds each nucleotide to the 3′ end of the growing strand.
:::

:::def DNA ligase
An enzyme that joins two pieces of DNA, for example the fragments of the lagging strand, by forming a phosphodiester bond between them.
:::

:::note Extra, not in the syllabus
The unwinding is done by an enzyme called helicase, which breaks the hydrogen bonds between the strands. The free nucleotides used in replication each carry three phosphate groups, like ATP, and the energy released when two are removed drives the formation of the phosphodiester bond. DNA polymerase starts only from a short RNA primer made by another enzyme. Human chromosomes have many starting points for replication, so S phase takes hours and not days.
:::

:::warn Who does what
- **DNA polymerase** does not unzip the DNA. It builds the new strand.
- **Hydrogen bonds** are broken between the two strands. They are not the bonds that join nucleotides in a strand.
- **DNA ligase** joins pieces of the **same new strand** (the fragments of the lagging strand). It does not join the two strands to each other.
- Semi-conservative does not mean "half of each strand is new". It means that each **molecule** has **one old strand and one new strand**.
:::

### Leading and lagging strands

DNA polymerase has a rule that decides everything about the next part. It adds a nucleotide only to the **3′ end** of the new strand, so new DNA is always made in the **5′ to 3′ direction**. It cannot work the other way.

The two template strands are antiparallel. As the fork opens along the DNA, one template runs 3′ to 5′ in the direction the fork is moving, and the other runs 5′ to 3′.

:::html
<figure class="fig small"><svg viewBox="0 0 350 372" role="img" aria-label="A replication fork drawn as a Y, with the parental DNA at the bottom and the fork moving down. The right arm is the template for the leading strand, which a DNA polymerase copies continuously. The left arm is the template for the lagging strand, which is made as short fragments, each away from the fork, joined by DNA ligase. Strand ends are labelled 5′ and 3′, and the two template strands are antiparallel."><path class="c2 sw3" d="M100 44L100 220L165 272L165 344"/><path class="c1 sw3" d="M250 44L250 220L185 272L185 344"/><path class="ln-m thin" d="M168 278L182 278"/><path class="ln-m thin" d="M168 288L182 288"/><path class="ln-m thin" d="M168 298L182 298"/><path class="ln-m thin" d="M168 308L182 308"/><path class="ln-m thin" d="M168 318L182 318"/><path class="ln-m thin" d="M168 328L182 328"/><path class="ln-m thin" d="M168 338L182 338"/><path class="c1 sw3 dash" d="M226 46L226 171"/><path class="ln-m thin" d="M229 52L247 52"/><path class="ln-m thin" d="M229 62L247 62"/><path class="ln-m thin" d="M229 72L247 72"/><path class="ln-m thin" d="M229 82L247 82"/><path class="ln-m thin" d="M229 92L247 92"/><path class="ln-m thin" d="M229 102L247 102"/><path class="ln-m thin" d="M229 112L247 112"/><path class="ln-m thin" d="M229 122L247 122"/><path class="ln-m thin" d="M229 132L247 132"/><path class="ln-m thin" d="M229 142L247 142"/><path class="ln-m thin" d="M229 152L247 152"/><path class="ln-m thin" d="M229 162L247 162"/><path class="c2 sw3 dash" d="M124 46L124 98"/><path class="ln-m thin" d="M103 52L121 52"/><path class="ln-m thin" d="M103 62L121 62"/><path class="ln-m thin" d="M103 72L121 72"/><path class="ln-m thin" d="M103 82L121 82"/><path class="ln-m thin" d="M103 92L121 92"/><path class="c2 sw3 dash" d="M124 112L124 150"/><path class="ln-m thin" d="M103 118L121 118"/><path class="ln-m thin" d="M103 128L121 128"/><path class="ln-m thin" d="M103 138L121 138"/><path class="ln-m thin" d="M103 148L121 148"/><path class="c2 sw3 dash" d="M124 186L124 214"/><path class="ln-m thin" d="M103 192L121 192"/><path class="ln-m thin" d="M103 202L121 202"/><path class="ln-m thin" d="M103 212L121 212"/><circle class="f2 s-acc2 sw2" cx="226" cy="185" r="13"/><text class="tl tb" x="226" y="190" text-anchor="middle">P</text><circle class="f2 s-acc2 sw2" cx="124" cy="169" r="13"/><text class="tl tb" x="124" y="174" text-anchor="middle">P</text><circle class="fm s-acc sw2" cx="124" cy="105" r="10"/><text class="tl tb" x="124" y="110" text-anchor="middle">L</text><text class="tl" x="100" y="30" text-anchor="middle">5′</text><text class="tl" x="124" y="30" text-anchor="middle">3′</text><text class="tl" x="226" y="30" text-anchor="middle">5′</text><text class="tl" x="250" y="30" text-anchor="middle">3′</text><text class="tl" x="165" y="360" text-anchor="middle">3′</text><text class="tl" x="185" y="360" text-anchor="middle">5′</text><text class="tl" x="8" y="112">lagging</text><text class="tl" x="8" y="126">strand</text><path class="ln-m thin" d="M50 128L121 134"/><text class="tl" x="268" y="82">leading</text><text class="tl" x="268" y="96">strand</text><path class="ln-m thin" d="M264 88L229 88"/><text class="tl" x="8" y="196">template</text><text class="tl" x="8" y="210">strand</text><path class="ln-m thin" d="M64 202L97 202"/><text class="tl" x="206" y="316">parental</text><text class="tl" x="206" y="330">DNA</text><path class="ln-m thin" d="M202 322L189 318"/><text class="tl" x="8" y="300">P = DNA</text><text class="tl" x="8" y="314">polymerase</text><text class="tl" x="8" y="332">L = DNA ligase</text><text class="tl" x="266" y="136">fork moves</text><text class="tl" x="266" y="150">this way</text><path class="ln" d="M300 162L300 226" marker-end="url(#ah)"/><path class="ln" d="M190 100L190 150" marker-end="url(#ah)"/><path class="ln" d="M148 236L148 190" marker-end="url(#ah)"/><text class="tl" x="175" y="58" text-anchor="middle">new DNA</text><text class="tl" x="175" y="72" text-anchor="middle">is made</text><text class="tl" x="175" y="86" text-anchor="middle">5′ → 3′</text></svg><figcaption>A replication fork (schematic, strands drawn straight). DNA polymerase can only add nucleotides to the 3′ end of a new strand, so every new strand grows 5′ to 3′. The leading strand is made continuously, in the same direction as the fork moves. The lagging strand is made as fragments, each away from the fork, and DNA ligase joins them. Dashed lines are new DNA.</figcaption></figure>
:::

- **Leading strand.** On the template that runs 3′ to 5′ towards the fork, DNA polymerase moves in the same direction as the fork and builds the new strand 5′ to 3′ without a break. The new strand is **continuous**.
- **Lagging strand.** On the other template, the polymerase can only work away from the fork. It must wait until the fork has opened a stretch of template, then make a short fragment away from the fork. As the fork opens more, a new fragment is started nearer to it. The new strand is made as a series of **fragments**, which **DNA ligase** joins by phosphodiester bonds.

:::note The fragments have a name
The fragments of the lagging strand are called Okazaki fragments, after the scientist who discovered them. You do not need the name for the exam.
:::

:::eg Explain why the lagging strand is made in fragments but the leading strand is made continuously.
A model answer in five marking points, in order.

DNA polymerase can add nucleotides only to the 3′ end of a growing strand, so new DNA is made only in the 5′ to 3′ direction. [B1]

The two template strands are antiparallel, so they run in opposite directions at the replication fork. [B1]

On the leading strand's template, the polymerase moves in the same direction as the fork, so it can make the new strand continuously. [B1]

On the other template, the polymerase must work away from the fork, so it can only make short fragments as more template is exposed. [B1]

DNA ligase joins the fragments by forming phosphodiester bonds. [B1]

A weaker answer says "the lagging strand is slower". It gives no reason, and never mentions the direction of the polymerase or the 3′ end.
:::

### Evidence for semi-conservative replication

Watson and Crick suggested that DNA is copied so that each new molecule keeps one old strand. Other models were possible:
- **Conservative replication**: the original double helix stays together and a completely new double helix is made.
- **Semi-conservative replication**: each new molecule has one old and one new strand.

In 1958 Matthew Meselson and Franklin Stahl found the answer with bacteria and two forms of nitrogen. Nitrogen is in the bases of DNA. Normal nitrogen is "light" (nitrogen-14). A form with a slightly larger mass is "heavy" (nitrogen-15), and DNA that contains it is denser.

:::steps
1. Bacteria were grown for many generations in a medium that contained only **heavy** nitrogen, so all their DNA was heavy.
2. They were moved to a medium with **light** nitrogen, so that every new strand was light. Samples were taken after each generation.
3. DNA was extracted from each sample and spun in a centrifuge in a dense salt solution. DNA settles at the level where its density matches the solution, so **heavy DNA forms a band lower in the tube than light DNA**, and DNA of intermediate density forms a band in between.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 232" role="img" aria-label="Four centrifuge tubes for generations 0 to 3 after bacteria were moved from heavy nitrogen to light nitrogen. Generation 0 has one heavy band near the bottom. Generation 1 has one intermediate band. Generation 2 has an intermediate band and a light band of equal thickness. Generation 3 has a thin intermediate band and a thick light band."><text class="tl tb" x="190" y="18" text-anchor="middle">generations in light nitrogen</text><rect class="fp ln" x="104" y="44" width="36" height="148" rx="10"/><text class="tl" x="122" y="36" text-anchor="middle">0</text><rect class="fp ln" x="160" y="44" width="36" height="148" rx="10"/><text class="tl" x="178" y="36" text-anchor="middle">1</text><rect class="fp ln" x="216" y="44" width="36" height="148" rx="10"/><text class="tl" x="234" y="36" text-anchor="middle">2</text><rect class="fp ln" x="272" y="44" width="36" height="148" rx="10"/><text class="tl" x="290" y="36" text-anchor="middle">3</text><rect class="f1 s-acc sw2" x="107" y="160" width="30" height="16"/><rect class="f2 s-acc2 sw2" x="163" y="110" width="30" height="16"/><rect class="f2 s-acc2 sw2" x="219" y="114" width="30" height="8"/><rect class="fm s-acc sw2" x="219" y="72" width="30" height="8"/><rect class="f2 s-acc2 sw2" x="275" y="116" width="30" height="4"/><rect class="fm s-acc sw2" x="275" y="70" width="30" height="12"/><text class="tl" x="94" y="80" text-anchor="end">light</text><text class="tl" x="94" y="122" text-anchor="end">intermediate</text><text class="tl" x="94" y="172" text-anchor="end">heavy</text><text class="tl" x="190" y="216" text-anchor="middle">band position after centrifuging</text></svg><figcaption>Meselson and Stahl's result (a drawing). Heavy DNA settles lower in the tube than light DNA. A thicker band means more DNA. After one generation all the DNA is intermediate, which fits semi-conservative replication.</figcaption></figure>
:::

The results fit only the semi-conservative model:
- **Generation 0**: one band of heavy DNA.
- **Generation 1**: one band of **intermediate** density. Every molecule had one old heavy strand and one new light strand. Conservative replication would have given two bands, heavy and light, so it is ruled out.
- **Generation 2**: two bands, **intermediate** and **light**, in equal amounts. The old heavy strands (two of them) are each in an intermediate molecule, and the other molecules have only new, light strands.

:::eg The table shows the percentage of the DNA in each band from bacteria that were grown in heavy nitrogen and then in light nitrogen. Explain the results, and predict the percentages in each band after four generations.
| generations in light nitrogen | heavy / % | intermediate / % | light / % |
|---|---|---|---|
| 0 | 100 | 0 | 0 |
| 1 | 0 | 100 | 0 |
| 2 | 0 | 50 | 50 |
| 3 | 0 | 25 | 75 |

At generation 0 all the DNA is heavy because the bacteria were grown in heavy nitrogen, so every strand contains it. [B1]

After one generation all the DNA is intermediate, because each molecule has one old (heavy) strand and one new (light) strand. [B1]

This supports semi-conservative replication, because conservative replication would give a heavy band and a light band. [B1]

At generation 2 half of the DNA is intermediate and half is light: the two old strands are still in two intermediate molecules, and the other two molecules are made of two new strands. [B1]

Prediction at generation 4: the 2 old strands are still in 2 intermediate molecules out of \(2^4 = 16\) molecules, so \(2 \div 16 = 12.5\%\) is intermediate and 87.5% is light. [B1]
:::

:::eg Spot the error: describe the roles of DNA polymerase and DNA ligase in DNA replication. [3]
A student wrote this answer.

Line 1: DNA polymerase breaks the hydrogen bonds between the two strands so that the DNA unzips.
Line 2: DNA polymerase also joins free nucleotides to a growing strand, forming phosphodiester bonds, in the 5′ to 3′ direction.
Line 3: DNA ligase joins the fragments of the lagging strand together.

**Line 1 is wrong: DNA polymerase does not separate the strands. It builds new strands. That mark is lost [B0].** Line 2 is correct [B1]. Line 3 is correct [B1].

Correct Line 1: "DNA polymerase uses each separated strand as a template and adds nucleotides that are complementary to it." That would make the answer score 3 marks.
:::

:::exam Describe and explain with correct terms
A "describe" question on DNA wants the facts (what is joined to what, which way). An "explain" question wants the reason (why the lagging strand is in fragments, why a purine pairs with a pyrimidine). Use the exact terms: **complementary base pairing**, **phosphodiester bond**, **antiparallel**, **DNA polymerase**, **3′ end**, **template**, **DNA ligase**.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State the three components of a nucleotide.
A: A pentose sugar, a phosphate group and a nitrogenous base.
Q: State which of the bases A, C, G, T and U are purines, and which are pyrimidines.
A: Purines: A and G (double ring). Pyrimidines: C, T and U (single ring).
Q: A section of DNA has 12 A–T base pairs and 7 C–G base pairs. Calculate the number of hydrogen bonds holding the two strands together.
A: \(12 \times 2 + 7 \times 3 = 24 + 21 = 45\) hydrogen bonds.
Q: 30% of the bases in a double-stranded DNA molecule are guanine. Calculate the percentage of adenine.
A: C = G = 30%, so C + G = 60%. A + T = 40% and A = T, so A = 20%.
Q: A single polynucleotide contains 40 nucleotides. State the number of phosphodiester bonds in it and the number of water molecules released as it was made.
A: \(40 - 1 = 39\) phosphodiester bonds and 39 water molecules.
Q: One strand of DNA reads 3′–TACGGT–5′. Write the sequence of the strand paired with it and label its ends.
A: 5′–ATGCCA–3′ (each base is replaced by its partner: T with A, A with T, C with G, G with C, G with C, T with A).
Q: Explain why the base pairs in DNA are always one purine and one pyrimidine.
A: A purine has two rings and a pyrimidine has one, so a purine plus a pyrimidine is always the same length. The strands are then the same distance apart all the way along. Two purines would be too wide and two pyrimidines too narrow for their hydrogen bonds to form.
Q: A section of the template of a lagging strand has 1200 bases. DNA polymerase makes it into new fragments that are each 150 bases long (an imagined value). Calculate the number of fragments and the number of joins that DNA ligase makes.
A: \(1200 \div 150 = 8\) fragments. They have \(8 - 1 = 7\) joins.
Q: Name the type of bond between two bases of a base pair, and the type of bond between two nucleotides in the same strand.
A: Hydrogen bonds between the bases of the pair; phosphodiester bonds between nucleotides in a strand.
Q: A DNA molecule is replicated three times in a row by semi-conservative replication. State the number of DNA molecules at the end, and the number that still contain one of the two original strands.
A: \(2^3 = 8\) DNA molecules. The two original strands are never copied together again, so 2 of the 8 molecules each contain one original strand.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the three parts of a DNA nucleotide, and one difference between a DNA nucleotide and an RNA nucleotide.
A: A pentose sugar (deoxyribose), a phosphate group and a nitrogenous base. [B1]
The sugar in DNA is deoxyribose but the sugar in RNA is ribose. [B1]
The DNA nucleotide has the base thymine where an RNA nucleotide has uracil (or: the base is A, G, C or T in DNA and A, G, C or U in RNA). [B1]
Q: [4 marks] ★★ The table shows the percentages of the four bases in DNA from a bacterium and from a virus.

| source | A / % | T / % | G / % | C / % |
|---|---|---|---|---|
| bacterium | 20 | 20 | 30 | 30 |
| virus | 26 | 33 | 22 | 19 |

(a) Explain why the values for the bacterium fit the rules of base pairing. (b) Suggest an explanation for the values for the virus, and calculate the percentage of purines in the virus.
H: Compare A with T, and G with C, in each row.
H: Which bases are purines? Add their percentages.
A: (a) A equals T and G equals C, because A pairs with T and C pairs with G in double-stranded DNA. [B1]
(b) A does not equal T and G does not equal C, so the DNA of the virus is probably single-stranded and so has no complementary base pairing. [B1]
Purines are A and G: \(26 + 22\) [M1] \(= 48\%\) [A1]
Q: [3 marks] ★★ A short section of one strand of DNA reads 5′–ATGCGATTCGCA–3′. (a) Write the sequence of the complementary strand, labelling its ends. (b) Calculate the total number of hydrogen bonds between the two strands in this section.
H: Count the bases in the given strand. Each A or T in it is part of an A–T pair, and each C or G in it is part of a C–G pair.
A: (a) 3′–TACGCTAAGCGT–5′ [B1]
(b) The strand has 6 bases that are A or T and 6 that are C or G, so 6 A–T pairs and 6 C–G pairs. [M1]
\(6 \times 2 + 6 \times 3 = 30\) hydrogen bonds [A1]
Q: [6 marks] ★★ Describe how DNA is replicated in S phase.
H: Start with the strands separating, and end with what each new molecule contains.
H: Name the enzymes and the bonds.
A: The double helix unwinds and the strands separate, as the hydrogen bonds between the bases break. [B1]
Each separated strand acts as a template. [B1]
Free nucleotides pair with the exposed bases by complementary base pairing (A with T and C with G). [B1]
DNA polymerase joins the nucleotides, forming phosphodiester bonds, in the 5′ to 3′ direction. [B1]
The leading strand is made continuously and the lagging strand in fragments that DNA ligase joins. [B1]
Each new DNA molecule has one original strand and one new strand (semi-conservative replication). [B1]
Q: [5 marks] ★★ Before the experiment of Meselson and Stahl, a conservative model was also proposed. In it, the original double helix stays together and each round of replication makes a completely new double helix. In a repeat of the experiment, bacteria with only heavy nitrogen in their DNA were moved to light nitrogen, and DNA was extracted after each generation. (a) Predict the percentage of heavy DNA and of light DNA after one generation, and after four generations, if the conservative model were correct. (b) The real result after one generation was a single band of intermediate density. Explain why this rejects the conservative model. (c) Explain why semi-conservative replication gives an intermediate band after one generation.
H: In the conservative model, the original double helix is never taken apart. How many original molecules are there, whatever the number of generations?
H: For (c), count how many old and how many new strands each molecule has.
A: (a) After one generation: 50% heavy and 50% light. [B1]
After four generations the original heavy molecule is 1 of \(2^4 = 16\) molecules, so \(1 \div 16 = 6.25\%\) heavy [M1] and 93.75% light. [A1]
(b) The conservative model predicts only a heavy band and a light band and no intermediate DNA, so a single intermediate band rejects it. [B1]
(c) Each new molecule has one old (heavy) strand and one new (light) strand, so all the DNA has an intermediate density. [B1]
Q: [5 marks] ★★ Explain how features of the structure of DNA make it suited to storing and passing on genetic information.
H: Think of the base sequence, the backbone, the hydrogen bonds and the pairing.
A: The sequence of bases along the strand carries the genetic information. [B1]
The phosphodiester bonds (covalent bonds) in the sugar–phosphate backbone make each strand stable. [B1]
The bases are inside the helix, protected by the backbone. [B1]
Hydrogen bonds are weak individually, so the strands can be separated for replication, but there are many, so the molecule is stable. [B1]
Complementary base pairing means each strand can be a template for an exact copy. [B1]
Q: [6 marks] (#bio.mitosis) ★★★ A drug stops the replication of a virus. It is a nucleotide that has no hydroxyl group on its 3′ carbon, and it is added to a growing DNA strand by the virus's DNA polymerase. (a) Explain why no more nucleotides can be added after the drug nucleotide. (b) Suggest why the drug stops the virus from making new virus particles. (c) Suggest why the drug could also harm some human cells.
H: Which group on the end of a strand forms the next phosphodiester bond?
H: For (c), which human cells replicate their DNA often, and in which stage of the cell cycle?
A: (a) The next nucleotide would have to form a phosphodiester bond with the hydroxyl group on the 3′ carbon at the end of the strand. [B1]
The drug nucleotide has no 3′ hydroxyl group, so no phosphodiester bond can form. [B1]
So the DNA strand cannot be made any longer. [B1]
(b) The viral DNA cannot be copied fully, so there are no new complete copies of the viral genome to put into new virus particles. [B1]
(c) Rapidly dividing human cells replicate their DNA in S phase often, so their replication would also be blocked if the drug is taken up. [B1]
They then cannot complete the cell cycle and divide, so cells such as those in bone marrow and hair follicles are affected. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A bacterium that lives in a hot spring has double-stranded DNA in which 68% of the bases are C or G. A bacterium from soil has 38% C or G. (a) Calculate the percentage of adenine in each DNA. (b) Calculate the number of hydrogen bonds in 100 base pairs of the hot-spring DNA. (c) Suggest how the proportion of C–G pairs may help the DNA of the hot-spring bacterium.
H: A = T, and C + G is given, so the rest is A + T.
H: Of 100 base pairs, how many are C–G, and how many are A–T?
A: (a) Hot spring: A = T = \((100 - 68) \div 2 = 16\%\). [B1]
Soil: A = T = \((100 - 38) \div 2 = 31\%\). [B1]
(b) 68 C–G pairs and 32 A–T pairs: \(68 \times 3 + 32 \times 2\) [M1] \(= 204 + 64 = 268\) hydrogen bonds. [A1]
(c) C–G pairs have three hydrogen bonds, so more energy is needed to separate the strands. [B1]
So the DNA stays double-stranded at the high temperature of the hot spring. [B1]
Q: [6 marks] ★★★ A strain of bacterium makes a DNA ligase that does not work at 42 °C. Cells were grown at 42 °C and the new DNA was extracted and its strands separated. (a) Predict what the researchers found about the lengths of the new DNA strands. (b) Explain this result. (c) Explain why the leading strand is not affected in the same way.
H: Which new strand is made in pieces?
H: Does the leading strand need any joining?
A: (a) Many short pieces of new DNA (fragments), as well as longer strands. [B1]
(b) The lagging strand is made in fragments, because DNA polymerase can work only in the 5′ to 3′ direction and so makes short pieces away from the fork. [B1]
DNA ligase joins the fragments by forming phosphodiester bonds. [B1]
Without a working ligase, the fragments stay separate. [B1]
(c) The leading strand is made continuously, as one polynucleotide, because the polymerase moves in the same direction as the fork. [B1]
So there are no fragments to join, and ligase is not needed. [B1]
:::

:::quiz
? Which row correctly describes a purine?
+ adenine, which has a double ring
- thymine, which has a double ring
- cytosine, which has a single ring and is found only in RNA
- uracil, which has a double ring
> Adenine and guanine are purines with two rings. Cytosine, thymine and uracil are pyrimidines with one ring, and cytosine is found in both DNA and RNA.
? How many hydrogen bonds join a C–G base pair?
+ three
- two
- one
- four
> C–G has three hydrogen bonds and A–T has two. This is why C–G rich DNA needs more energy to separate.
? Which bond joins one nucleotide to the next in a polynucleotide?
+ a phosphodiester bond between the 3′ carbon of one sugar and the phosphate on the 5′ carbon of the next
- a hydrogen bond between the bases
- a glycosidic bond between the sugars
- a peptide bond between the bases
> Phosphodiester bonds are the covalent bonds of the sugar–phosphate backbone. Hydrogen bonds join bases in different strands, glycosidic bonds join sugars in carbohydrates and peptide bonds join amino acids.
? A double-stranded DNA molecule has 18% thymine. What is the percentage of guanine?
+ 32%
- 18%
- 64%
- 82%
> A = T = 18%, so A + T = 36% and C + G = 64%, and G = 32%. 64% is the total of C + G, and 18% is the percentage of A.
? Which statement about the two strands of DNA is correct?
+ They run in opposite directions: one is 5′ to 3′ and the other is 3′ to 5′.
- They run in the same direction, both 5′ to 3′.
- They are held together by phosphodiester bonds between the bases.
- They are identical in base sequence.
> The strands are antiparallel and complementary (not identical). They are joined by hydrogen bonds between the bases.
? Which statement about DNA polymerase is correct?
+ It adds nucleotides to the 3′ end of a growing strand.
- It breaks the hydrogen bonds between the two strands.
- It joins the two strands together at the end of replication.
- It adds nucleotides to the 5′ end of a growing strand.
> DNA polymerase builds new DNA 5′ to 3′, adding to the 3′ end. Separating the strands is not its job, and ligase joins fragments of the same strand.
? Why is the lagging strand made in fragments?
+ DNA polymerase can only work in the 5′ to 3′ direction, which is away from the fork on this template.
- Ligase cannot join the whole strand in one piece.
- The lagging strand is made from a different enzyme from the leading strand.
- Hydrogen bonds break only in short stretches.
> The same DNA polymerase makes both strands, but it can only add to a 3′ end. On one template that means working away from the fork in short pieces. Ligase then joins them.
? Bacteria grown in heavy nitrogen are moved to light nitrogen. After one generation, where does the DNA band lie?
+ one band, between the heavy and light positions
- two bands, one heavy and one light
- one band at the heavy position
- one band at the light position
> Each molecule has one old heavy strand and one new light strand, so all the DNA has intermediate density. Two bands (heavy and light) would be the prediction of conservative replication.
? Which row correctly compares DNA and mRNA?
+ DNA has thymine and deoxyribose; mRNA has uracil and ribose.
- DNA has uracil and ribose; mRNA has thymine and deoxyribose.
- DNA has thymine and ribose; mRNA has uracil and deoxyribose.
- DNA and mRNA both have thymine, but mRNA has ribose.
> DNA: deoxyribose and A, G, C, T. mRNA: ribose and A, G, C, U.
? Which statement about ATP is correct?
+ It is a nucleotide with adenine, ribose and three phosphate groups.
- It is a nucleotide with adenine, deoxyribose and one phosphate group.
- It is a nucleotide with thymine, ribose and three phosphate groups.
- It is a polynucleotide made of many adenine nucleotides.
> ATP has the base adenine, the sugar ribose and three phosphate groups. It is a single phosphorylated nucleotide, not a polymer.
:::

:::checklist What you can now do
- [ ] I can describe the structure of a nucleotide, and the structure of ATP as a phosphorylated nucleotide.
- [ ] I can state which bases are purines (double ring) and which are pyrimidines (single ring), and which are in DNA and in RNA.
- [ ] I can describe how phosphodiester bonds join nucleotides, and label the 5′ and 3′ ends of a strand.
- [ ] I can describe the DNA double helix: antiparallel strands, complementary base pairing, two hydrogen bonds for A–T and three for C–G.
- [ ] I can use base-pairing rules to find the complementary strand, base percentages and the number of hydrogen bonds.
- [ ] I can describe semi-conservative replication in S phase, including the roles of DNA polymerase and DNA ligase.
- [ ] I can explain why the leading strand is continuous and the lagging strand is made in fragments.
- [ ] I can interpret the Meselson–Stahl results as evidence for semi-conservative replication.
- [ ] I can describe the structure of mRNA and compare it with DNA.
:::

:::recap
- A nucleotide is a pentose sugar, a phosphate group and a nitrogenous base. DNA sugar: deoxyribose. RNA sugar: ribose. ATP is a phosphorylated nucleotide (adenine, ribose, three phosphates).
- Purines (A, G) have two rings; pyrimidines (C, T, U) have one ring. DNA bases: A, G, C, T. RNA bases: A, G, C, U.
- Phosphodiester bonds join the 3′ carbon of one nucleotide to the 5′ phosphate of the next, in a condensation reaction. A strand has a 5′ end (phosphate) and a 3′ end (OH).
- DNA is a double helix: two antiparallel polynucleotide strands joined by hydrogen bonds between complementary bases: A–T (two) and C–G (three). A purine always pairs with a pyrimidine, so the width is constant.
- In double-stranded DNA, A = T and C = G, and purines = pyrimidines = 50%.
- Semi-conservative replication (S phase): strands separate, free nucleotides pair with each template, DNA polymerase forms phosphodiester bonds in the 5′ to 3′ direction, each new molecule has one old and one new strand.
- The leading strand is continuous; the lagging strand is made in fragments, joined by DNA ligase.
- Meselson and Stahl: generation 1 all intermediate density, generation 2 half intermediate and half light, so semi-conservative.
- mRNA: one polynucleotide strand, ribose, uracil instead of thymine, short, no base pairing along it, codons.
:::

:::links
- read: [CAIE A Level Biology: nucleic acids and protein synthesis notes and questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/nucleic-acids-protein-synthesis/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Nucleic acids and protein synthesis (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/6-nucleic-acids-and-protein-synthesis/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- explore: [Learn.Genetics: DNA, genes and proteins](https://learn.genetics.utah.edu/content/basics/) · University of Utah · short interactive pages on DNA and how it is copied
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of DNA structure and replication
- read: [DNA structure and function](https://openstax.org/books/biology-2e/pages/14-introduction) · OpenStax Biology 2e · free university textbook chapter on DNA structure and replication, beyond the syllabus in places
- papers: [Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-2/) · Physics & Maths Tutor · find the DNA questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Protein synthesis and gene mutation](#bio.synthesis) shows how the base sequence of DNA is used to make polypeptides.
