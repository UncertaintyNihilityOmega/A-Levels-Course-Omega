@chapter bio.genetech
@title Tools of genetic technology
@level a2
@paper CAIE 9700 Paper 4
@time 5–6 hours
@summary Genetic engineering moves genes between organisms, and a small set of tools makes it work. You will learn what recombinant DNA is, three ways to obtain a gene, the roles of restriction endonucleases, DNA ligase, plasmids, DNA polymerase and reverse transcriptase, why a promoter and a marker gene are needed, gene editing, the polymerase chain reaction (PCR) with Taq polymerase, gel electrophoresis, microarrays and sequence databases.

:::why
Insulin for diabetes, the tests that identify an inherited disease, and the crops and medicines in the next chapter all depend on the same toolkit: cut DNA at a chosen place, join it to other DNA, copy it millions of times, and read the result. Paper 4 asks you to explain the role of each enzyme in a gene transfer, to calculate numbers of copies in PCR, to work out fragment sizes and to read a gel, so this chapter teaches each tool as a step with a reason.
:::

**Before you start**, you should know the structure of DNA and how it is copied from [Nucleic acids and DNA replication](#bio.dna), how a gene is transcribed and translated from [Protein synthesis and gene mutation](#bio.synthesis), and what a plasmid is from [Prokaryotes and viruses](#bio.prokaryotes).

:::try Warm-up
Q: Name the enzyme that joins nucleotides to make a new DNA strand, and the bonds that hold the two strands of a DNA molecule together. (from [Nucleic acids and DNA replication](#bio.dna))
A: DNA polymerase joins nucleotides, forming phosphodiester bonds in the sugar–phosphate backbone. The two strands are held together by hydrogen bonds between complementary bases (A with T, C with G).
Q: In a eukaryotic gene, which parts are removed from the pre-mRNA before translation, and which parts stay in the mature mRNA? (from [Protein synthesis and gene mutation](#bio.synthesis))
A: Introns are removed (spliced out); exons stay in the mature mRNA and code for the polypeptide.
Q: Describe a plasmid and say where it is found. (from [Prokaryotes and viruses](#bio.prokaryotes))
A: A small, circular loop of DNA, separate from the main chromosome, found in bacteria. It carries a few genes (for example antibiotic resistance) and can be copied and passed to other bacteria.
:::

## Genetic engineering and recombinant DNA

:::def Recombinant DNA
DNA made by joining together DNA from two or more different sources (often different species).
:::

:::def Genetic engineering
The deliberate manipulation of genetic material to modify specific characteristics of an organism. It often involves transferring a gene from one organism into another so that the gene is **expressed** (transcribed and translated to make its protein) in the new host.
:::

The genetic code is universal: the same triplets code for the same amino acids in bacteria, plants and humans. So a human gene put into a bacterium can be transcribed and translated by the bacterium's own ribosomes, and the bacterium makes the human protein. The organism that now carries the foreign gene is a **transgenic** organism, or a genetically modified organism (GMO).

Every gene transfer follows the same pattern:

:::steps
1. **Obtain** the gene you want (the "desired gene").
2. **Cut** a vector (usually a plasmid) and **insert** the gene into it, making recombinant DNA.
3. **Put** the vector into a host cell (such as a bacterium).
4. **Select** the cells that have taken up the vector, and check that the gene is **expressed**.
5. **Grow** the host cells in large numbers (and, if needed, harvest the protein).
:::

## Step 1: obtaining the gene

There are three sources of the gene. Each has strengths and weaknesses.

### Extracting the gene from the DNA of a donor

Cut the donor's DNA with restriction endonucleases (next section) and find the fragment that contains the gene. It is the most direct method, but a eukaryotic genome has tens of thousands of genes, so finding the one you want among the fragments is hard. And a eukaryotic gene contains **introns**. A bacterium cannot splice out introns, so the bacterium would make a faulty protein.

### Making the gene from mRNA

A cell that is making a large amount of a protein contains a large amount of the mRNA for it (cells of the pancreas that make insulin are packed with insulin mRNA). The mRNA has already had its introns removed. The mRNA is turned back into DNA in two steps.

:::steps
1. **Reverse transcriptase** uses the mRNA as a template to make a single strand of DNA that is complementary to it. This is **complementary DNA (cDNA)**.
2. **DNA polymerase** uses the cDNA strand as a template to make the second strand, so there is now a double-stranded gene.
:::

:::def Complementary DNA (cDNA)
DNA made from mRNA by reverse transcriptase. It contains only the exons of the gene, because the introns were removed before the mRNA left the nucleus.
:::

:::def Reverse transcriptase
An enzyme (from retroviruses) that makes DNA from an RNA template. It reverses the usual direction of transcription: RNA to DNA.
:::

Advantages: the gene has no introns, and it is easy to find, because the cell has concentrated the mRNA for it. Disadvantage: you must find a cell type that makes plenty of the mRNA.

:::eg A human gene has three exons of 150, 210 and 90 nucleotides separated by two introns of 800 and 1200 nucleotides. Calculate the length of the gene, the length of the cDNA made from its mature mRNA (ignore any untranslated regions), the percentage of the gene that the cDNA represents and the number of amino acids in the polypeptide, if the last three nucleotides are a stop codon. Explain why the cDNA, not the gene, is put into a bacterium.
**Length of the gene** is exons plus introns:

\[\begin{aligned} 150 + 210 + 90 + 800 + 1200 &= 2450\ \text{nucleotides} \end{aligned}\]

[A1]

**Length of the cDNA** is exons only:

\[\begin{aligned} 150 + 210 + 90 &= 450\ \text{nucleotides} \\ \frac{450}{2450} \times 100 &= 18.4\% \end{aligned}\]

[M1] [A1]

**Amino acids**: each amino acid is coded by three nucleotides, and the stop codon codes for none:

\[\begin{aligned} \frac{450 - 3}{3} &= 149\ \text{amino acids} \end{aligned}\]

[A1]

Why cDNA: a bacterium has no spliceosome, so it cannot remove the introns of the gene. It would transcribe the introns too, and the polypeptide would be wrong. The cDNA has the introns already removed, so the bacterium translates it correctly. [B1]
:::

### Making the gene from nucleotides

If the amino acid sequence of the protein is known, scientists can use the genetic code to work out a DNA sequence that codes for it. A machine joins nucleotides one by one in that order, making a short gene chemically. Advantages: the sequence can be designed (for example to use codons that the host reads most efficiently), and no cells with mRNA are needed. Disadvantage: it is practical only for short genes of a known sequence, and it can't be used for a protein whose sequence is not known.

| Source of the gene | How | Introns? | Best for |
|---|---|---|---|
| donor DNA | restriction endonucleases cut it out | yes, if from a eukaryote | prokaryotic genes; hosts that can splice |
| mRNA | reverse transcriptase, then DNA polymerase | no | eukaryotic genes put into bacteria |
| nucleotides | a gene synthesiser, from a known sequence | no | short genes of known sequence |

## Step 2: cutting and joining DNA

### Restriction endonucleases

:::def Restriction endonuclease (restriction enzyme)
An enzyme that cuts DNA at a specific base sequence, its **recognition site**, by breaking phosphodiester bonds in the sugar–phosphate backbone of both strands.
:::

Bacteria make restriction endonucleases to cut up the DNA of invading viruses. Each type recognises one short sequence of 4–8 base pairs, which fits its active site; it is specific, as every enzyme is (see [Enzymes](#bio.enzymes)). It does not cut at random places.

Many recognition sites are **palindromic**: the sequence on one strand read 5′ to 3′ is the same as the sequence on the other strand read 5′ to 3′. The enzyme EcoRI recognises GAATTC and cuts between the G and the A on each strand. The cuts are **staggered**, so each piece ends in a short single-stranded overhang.

:::html
<figure class="fig small" data-fig="restrict"><svg viewBox="0 0 300 296" role="img" aria-label="Two panels. A: the DNA sequence GAATTC on the top strand, 5 prime to 3 prime, paired with CTTAAG on the bottom strand, with a cut between G and A on the top strand and between A and G on the bottom strand. B: after the cut, the left piece keeps G paired with C and has the single-stranded bottom bases TTAA; the right piece keeps the top bases AATT unpaired above a single G; each unpaired stretch is labelled sticky end."><text class="tl tb" x="10" y="16">A  EcoRI finds its recognition site</text><text class="tl" x="104" y="48" text-anchor="middle">G</text><text class="tl" x="104" y="82" text-anchor="middle">C</text><path class="ln-m thin dash" d="M104 55L104 68"/><text class="tl" x="126" y="48" text-anchor="middle">A</text><text class="tl" x="126" y="82" text-anchor="middle">T</text><path class="ln-m thin dash" d="M126 55L126 68"/><text class="tl" x="148" y="48" text-anchor="middle">A</text><text class="tl" x="148" y="82" text-anchor="middle">T</text><path class="ln-m thin dash" d="M148 55L148 68"/><text class="tl" x="170" y="48" text-anchor="middle">T</text><text class="tl" x="170" y="82" text-anchor="middle">A</text><path class="ln-m thin dash" d="M170 55L170 68"/><text class="tl" x="192" y="48" text-anchor="middle">T</text><text class="tl" x="192" y="82" text-anchor="middle">A</text><path class="ln-m thin dash" d="M192 55L192 68"/><text class="tl" x="214" y="48" text-anchor="middle">C</text><text class="tl" x="214" y="82" text-anchor="middle">G</text><path class="ln-m thin dash" d="M214 55L214 68"/><text class="tl" x="80" y="48" text-anchor="middle">5′</text><text class="tl" x="238" y="48" text-anchor="middle">3′</text><text class="tl" x="80" y="82" text-anchor="middle">3′</text><text class="tl" x="238" y="82" text-anchor="middle">5′</text><path class="c2 sw2" d="M115 30L115 55"/><path class="c2 sw2" d="M203 68L203 94"/><text class="tl" x="10" y="116">Both strands read GAATTC</text><text class="tl" x="10" y="132">from 5′ to 3′ (a palindrome)</text><text class="tl tb" x="10" y="164">B  Staggered cuts leave sticky ends</text><text class="tl" x="82" y="212" text-anchor="middle">G</text><text class="tl" x="82" y="246" text-anchor="middle">C</text><text class="tl" x="104" y="246" text-anchor="middle">T</text><text class="tl" x="126" y="246" text-anchor="middle">T</text><text class="tl" x="148" y="246" text-anchor="middle">A</text><text class="tl" x="170" y="246" text-anchor="middle">A</text><text class="tl" x="148" y="212" text-anchor="middle">A</text><text class="tl" x="170" y="212" text-anchor="middle">A</text><text class="tl" x="192" y="212" text-anchor="middle">T</text><text class="tl" x="214" y="212" text-anchor="middle">T</text><text class="tl" x="236" y="212" text-anchor="middle">C</text><text class="tl" x="236" y="246" text-anchor="middle">G</text><path class="ln-m thin dash" d="M82 219L82 232"/><path class="ln-m thin dash" d="M236 219L236 232"/><path class="ln-m thin" d="M142 195L142 190L220 190L220 195"/><text class="tl" x="181" y="182" text-anchor="middle">sticky end</text><path class="ln-m thin" d="M98 257L98 262L176 262L176 257"/><text class="tl" x="137" y="282" text-anchor="middle">sticky end</text></svg><figcaption>A restriction endonuclease (EcoRI) cuts the two strands at different points. B: each piece is left with a single-stranded stretch, a sticky end, that can pair with a complementary sticky end on another piece cut with the same enzyme.</figcaption></figure>
:::

:::def Sticky end
A short single-stranded overhang left at the end of a DNA fragment when a restriction endonuclease makes a staggered cut. It can form hydrogen bonds with a complementary sticky end on another fragment.
:::

Some enzymes cut both strands at the same place, leaving **blunt ends** with no overhang. Sticky ends are more useful because they pair easily. The key idea is that if the **same** restriction endonuclease cuts the plasmid and the DNA containing the gene, all the pieces have the **same** sticky ends. The sticky ends of the gene are complementary to the sticky ends of the cut plasmid, so the gene can pair into the plasmid.

### DNA ligase

:::def DNA ligase
An enzyme that joins two DNA fragments by forming phosphodiester bonds between the sugar of one nucleotide and the phosphate of the next, in the sugar–phosphate backbone.
:::

When the sticky ends pair, they are held together only by a few **hydrogen bonds**, which are weak and easily broken. DNA ligase makes the permanent covalent **phosphodiester bonds** that seal the gaps in the backbone of both strands. Ligase is also the enzyme that joins the fragments in DNA replication (see [Nucleic acids and DNA replication](#bio.dna)).

:::warn Hydrogen bonds pair; ligase makes phosphodiester bonds
The sticky ends pair by **hydrogen bonds between complementary bases**. Ligase does not form hydrogen bonds: it forms **phosphodiester bonds** in the backbone. Restriction endonucleases **break** phosphodiester bonds; ligase **forms** them.
:::

### Plasmids as vectors

:::def Vector
A DNA molecule (such as a plasmid or a virus) that carries a gene into a host cell and gets it copied there.
:::

Plasmids are good vectors for bacteria because they are small and easy to isolate, they can be cut at a single site by a restriction endonuclease, and the bacterium copies them and passes them to its daughter cells. A useful plasmid vector has:

- an **origin of replication**, so that the bacterium's enzymes copy the plasmid, and each daughter cell receives copies;
- one or more **recognition sites** for restriction endonucleases, where the gene can be inserted;
- a **marker gene** to show which bacteria have taken the plasmid up (see below).

### Where the other enzymes are used

| Enzyme | Role in gene transfer |
|---|---|
| reverse transcriptase | makes cDNA from mRNA |
| DNA polymerase | makes the second strand of the cDNA; also copies DNA in PCR (see below) |
| restriction endonuclease | cuts the plasmid and the DNA containing the gene at specific sites, leaving sticky ends |
| DNA ligase | joins the gene to the plasmid by making phosphodiester bonds |

:::html
<figure class="fig small" data-fig="plasmid"><svg viewBox="0 0 340 476" role="img" aria-label="Four steps drawn one under another. 1: a gene shown as a bar and a bacterial plasmid shown as an open ring, cut by the same restriction enzyme. 2: DNA ligase seals the gene into the ring, making a recombinant plasmid. 3: bacteria are treated with calcium ions and heat shock so that the plasmid, carrying the gene, enters a bacterium. 4: two bacteria; the one with the plasmid glows, shown with short rays around it, and the one with no plasmid does not."><path class="ln thick" d="M68.9 35.6A26 26 0 1 1 51.1 35.6"/><rect class="f2 s-acc2 sw2" x="130" y="52" width="100" height="16"/><text class="tl" x="60" y="102" text-anchor="middle">plasmid</text><text class="tl" x="180" y="92" text-anchor="middle">gene</text><text class="tl" x="10" y="124">1  The same restriction enzyme cuts</text><text class="tl" x="10" y="140">the plasmid and the gene.</text><path class="ln-m thin" d="M10 152L330 152"/><circle class="ln thick fp" cx="250" cy="206" r="26"/><path class="c2 sw3" d="M227.5 193.0A26 26 0 0 1 272.5 193.0"/><text class="tl" x="250" y="172" text-anchor="middle">gene</text><text class="tl" x="250" y="250" text-anchor="middle">recombinant plasmid</text><text class="tl" x="10" y="196">2  DNA ligase seals the</text><text class="tl" x="10" y="212">sticky-end joins:</text><text class="tl" x="10" y="228">recombinant plasmid.</text><path class="ln-m thin" d="M10 268L330 268"/><rect class="f1 s-acc sw2" x="230" y="282" width="96" height="68" rx="24"/><circle class="ln thick fp" cx="260" cy="316" r="14"/><path class="c2 sw3" d="M247.9 309.0A14 14 0 0 1 272.1 309.0"/><text class="tl" x="278" y="368" text-anchor="middle">bacterium</text><text class="tl" x="10" y="300">3  Bacteria are treated</text><text class="tl" x="10" y="316">(calcium ions, heat</text><text class="tl" x="10" y="332">shock) so plasmids enter.</text><path class="ln-m thin" d="M10 388L330 388"/><text class="tl" x="10" y="412">4  Marker gene: a cell</text><text class="tl" x="10" y="428">that glows has the</text><text class="tl" x="10" y="444">plasmid and expresses it.</text><rect class="f2 s-acc2 sw2" x="194" y="410" width="52" height="34" rx="14"/><circle class="ln fp" cx="210" cy="427" r="8"/><path class="c2 sw3" d="M203.1 423.0A8 8 0 0 1 216.9 423.0"/><path class="c2 sw2" d="M220 404L220 397"/><path class="c2 sw2" d="M191 407L186 402"/><path class="c2 sw2" d="M249 407L254 402"/><path class="c2 sw2" d="M188 427L182 427"/><path class="c2 sw2" d="M252 427L257 427"/><rect class="f1 s-acc sw2" x="268" y="410" width="52" height="34" rx="14"/><text class="tl" x="220" y="466" text-anchor="middle">glows</text><text class="tl" x="294" y="466" text-anchor="middle">no plasmid</text></svg><figcaption>Making and selecting bacteria that carry a recombinant plasmid.</figcaption></figure>
:::

:::eg Explain the roles of enzymes in making bacteria that produce human insulin from the mRNA of pancreatic cells.
A full-mark answer takes each stage in order and names the enzyme and what it does. Six marks need six separate points.

mRNA for insulin is extracted from beta cells in the pancreas, which make large amounts of it, and **reverse transcriptase** makes a single strand of cDNA from it. [B1]

**DNA polymerase** makes the second strand, to give a double-stranded insulin gene without introns. [B1]

A **restriction endonuclease** cuts the plasmid at one recognition site, and the same enzyme cuts the gene, so that both have the same complementary sticky ends. [B1]

The sticky ends of the plasmid and of the gene are complementary, so they pair by hydrogen bonds between bases. [B1]

**DNA ligase** forms phosphodiester bonds between the nucleotides to join the gene permanently into the plasmid, making recombinant DNA. [B1]

The plasmid, as a vector, carries the gene into the bacterium, which copies the plasmid; a promoter that the bacterium recognises is needed so that the gene is transcribed. [B1]

(Also credit: marker gene used to identify the bacteria that took up the plasmid.)

A weaker answer says "enzymes cut the gene and put it in the bacteria". It does not name any enzyme, does not mention sticky ends or that ligase makes bonds, and scores one or two marks.
:::

:::exam "Describe" is not "explain": the role of each enzyme
"Explain the role of each enzyme" needs three things for every enzyme: **name** it, say **what it does**, and say **why that step is needed**. "Describe" would stop at what it does. In the insulin answer, "reverse transcriptase makes cDNA from mRNA" is only a description. The explanation adds the reason: the gene has no introns, so a bacterium (which cannot splice) can express it. Likewise "DNA ligase joins the gene to the plasmid" becomes an explanation with "forms phosphodiester bonds, so the gene is permanently part of the plasmid and is copied with it". A weak answer gives "enzymes cut and join DNA"; a strong answer names the enzyme, the bond or product, and the purpose, one mark each.
:::

## Step 3: getting the plasmid into bacteria

The recombinant plasmids are mixed with bacteria. The bacteria are treated (for example with calcium ions and a short heat shock) so that their cell surface membranes and walls become permeable enough for the plasmids to enter. This is called **transformation**. It works for only a small proportion of the bacteria. Some of the plasmids also close up again without the gene. So you end up with a mixture:

- bacteria that took up no plasmid;
- bacteria that took up a plasmid **without** the gene;
- bacteria that took up the **recombinant** plasmid.

You need a way to find the last group.

## Step 4: marker genes and expression

:::def Marker gene
A gene on a vector whose product is easy to detect, so that you can tell which cells have taken up the vector and are expressing its genes.
:::

The older method used an **antibiotic resistance gene** as the marker: only bacteria that carry the plasmid survive on a medium that contains the antibiotic. It has a problem: it spreads resistance genes in the environment and, in medicine, it adds to the problem of antibiotic resistance (see [Antibiotics and resistance](#bio.antibiotics)).

A better marker is a gene that codes for a **fluorescent protein**. The best-known is **GFP** (green fluorescent protein), which comes from a jellyfish. If the cell has the GFP gene and expresses it, the cell makes GFP and glows when it is lit with blue or ultraviolet light.

The GFP gene is put into the plasmid next to the desired gene so that both are controlled by the **same promoter**, or they are joined into one gene so that one protein contains both. Then a glowing cell must have taken up the plasmid **and** be expressing the gene, because the promoter has to work to make GFP. Advantages of fluorescent markers: they show expression directly; the cells need not be killed to test them; there is no need for antibiotics (and no antibiotic resistance gene is released); and the fluorescent protein can be seen in living cells and whole organisms.

:::eg Real context, GFP: a scientist inserts a gene for a human enzyme into plasmids, with the GFP gene joined to the same promoter, and mixes the plasmids with bacteria. Colonies are grown on plates and viewed under blue light. Some colonies glow and some do not. Explain what each type of colony shows, and why a colony that glows is a good choice for the next stage.
A colony that glows contains bacteria that have taken up the plasmid carrying the GFP gene and are transcribing and translating the genes under that promoter. [B1]

A colony that does not glow either has no plasmid, or has a plasmid that does not carry (or cannot express) the GFP gene. [B1]

Because the GFP gene and the human gene are controlled by the same promoter, a glowing colony is likely to be expressing the human gene as well. [B1]

(Glowing colonies can be chosen with no antibiotics, and the bacteria in them stay alive and can be grown on.)
:::

## Why the gene needs a promoter

:::def Promoter
A length of DNA, next to a gene, where RNA polymerase binds so that transcription of the gene can start (see [Genes, phenotype and gene control](#bio.genecontrol)).
:::

A gene is not expressed unless RNA polymerase can bind to a promoter next to it. Promoters of eukaryotes are not recognised by the RNA polymerase of bacteria, so a human gene on its own would not be transcribed in a bacterium even though the genetic code is the same. So scientists:

- use a plasmid that already has a bacterial promoter next to the cloning site, so that the inserted gene is controlled by it; or
- transfer the gene together with a promoter that works in the host.

The choice of promoter also decides **when** and **where** the gene is expressed. A promoter that is active only in particular tissues, or only when a certain chemical is added, switches the gene on at the right moment (the next chapter has an example in GM salmon, where a promoter makes the growth hormone gene active in all seasons).

:::key Genetic engineering in one box
- **Recombinant DNA** is DNA from two or more sources joined together.
- Get the gene: cut it from donor DNA, make **cDNA** from mRNA (reverse transcriptase, then DNA polymerase), or build it from nucleotides.
- **Restriction endonuclease** cuts at a specific recognition site, leaving **sticky ends**; the same enzyme cuts the plasmid and the gene.
- **DNA ligase** forms **phosphodiester bonds** and joins them.
- A **plasmid** is the vector: it has an origin of replication, cutting sites and marker gene(s).
- A **promoter** that the host recognises is needed for expression.
- A **marker gene** (for example GFP) shows which cells took up the plasmid and express the gene.
:::

## Gene editing

Genetic engineering as described adds a whole gene to an organism, but the new gene goes in at a random place. **Gene editing** changes the DNA of an organism at a chosen place.

:::def Gene editing
A form of genetic engineering in which DNA is inserted, deleted or replaced at specific sites in the genome of an organism.
:::

:::note CRISPR–Cas9 in outline
The best-known tool for gene editing is CRISPR–Cas9. It has two parts: a **guide RNA**, a short RNA whose sequence is made complementary to the target sequence, and the enzyme **Cas9**, which cuts DNA. The guide RNA leads Cas9 to the matching sequence in the genome, by base pairing. Cas9 cuts both strands of the DNA there. The cell then repairs the break. The repair can **delete** a few bases and switch the gene off; or, if a piece of DNA with the matching ends is supplied, the cell can use it as a template and **insert** or **replace** a sequence. You need only this outline, not the details of the mechanism.
:::

The difference from the earlier method is control: gene editing can change a single gene in its normal place in the genome (and under its own promoter), instead of adding a gene at random.

## Copying DNA: the polymerase chain reaction (PCR)

:::def Polymerase chain reaction (PCR)
A technique that copies (clones) a chosen length of DNA in a test tube, making millions of copies from a very small sample in a few hours, by repeating a cycle of heating and cooling.
:::

PCR needs:

- the **DNA template** (the sample to be copied);
- two **primers**: short single-stranded pieces of DNA, about 20 nucleotides long, complementary to the **ends** of the target sequence on each strand (one for each strand). The primer shows DNA polymerase where to start, because DNA polymerase can only add nucleotides to an existing 3′ end. A primer is a short piece of DNA, not an enzyme;
- free **nucleotides** (the four DNA nucleotides) to build the new strands;
- **Taq polymerase**, a heat-stable DNA polymerase;
- a buffer, and a machine (a thermal cycler) that changes the temperature automatically.

### Taq polymerase

Taq polymerase comes from a bacterium (*Thermus aquaticus*) that lives in hot springs. Its enzyme is **thermostable**: its tertiary structure is not denatured at 95 °C, whereas the DNA polymerase of most organisms would be. So it can be added once at the start, and it survives the many heating steps; it does not have to be replaced after every cycle. Its optimum temperature is about 72 °C.

### The three steps of a cycle

:::steps
1. **Denaturation, about 95 °C.** The mixture is heated. The hydrogen bonds between the two strands of the template break, so the strands separate and become single strands.
2. **Annealing, about 55–65 °C.** The mixture is cooled. The primers form hydrogen bonds with the complementary sequences at the ends of the target on each template strand. (Annealing means the primers "stick" by base pairing.)
3. **Extension, about 72 °C.** The temperature is raised to the optimum for Taq polymerase. It adds free nucleotides to the 3′ end of each primer, complementary to the template, and so makes a new strand on each template.
:::

:::html
<figure class="fig small" data-fig="pcr"><svg viewBox="0 0 340 336" role="img" aria-label="Three stages of one PCR cycle. 1: denaturation at about 95 degrees Celsius, a double strand of DNA becomes two single strands as hydrogen bonds break. 2: annealing at about 55 to 65 degrees Celsius, one primer binds near the right end of the upper template strand and one near the left end of the lower template strand. 3: extension at about 72 degrees Celsius, Taq polymerase extends each primer to make a new strand, the upper one leftwards and the lower one rightwards."><text class="tl tb" x="10" y="18">1  Denaturation, about 95 °C</text><path class="ln-m thin" d="M34 38L34 50"/><path class="ln-m thin" d="M46 38L46 50"/><path class="ln-m thin" d="M58 38L58 50"/><path class="ln-m thin" d="M70 38L70 50"/><path class="ln-m thin" d="M82 38L82 50"/><path class="ln-m thin" d="M94 38L94 50"/><path class="ln-m thin" d="M106 38L106 50"/><path class="ln-m thin" d="M118 38L118 50"/><path class="ln-m thin" d="M130 38L130 50"/><path class="ln" d="M34 38L140 38"/><path class="ln" d="M34 50L140 50"/><path class="ln" d="M150 44L180 44" marker-end="url(#ah)"/><path class="ln" d="M190 34L300 34"/><path class="ln" d="M190 56L300 56"/><text class="tl" x="10" y="84">hydrogen bonds between strands break</text><path class="ln-m thin" d="M10 94L330 94"/><text class="tl tb" x="10" y="112">2  Annealing, about 55–65 °C</text><path class="ln" d="M30 128L310 128"/><path class="ln" d="M30 178L310 178"/><path class="c2 sw3" d="M230 140L270 140"/><path class="c2 sw3" d="M70 166L110 166"/><text class="tl" x="250" y="160" text-anchor="middle">primer</text><text class="tl" x="90" y="152" text-anchor="middle">primer</text><path class="ln-m thin" d="M10 196L330 196"/><text class="tl tb" x="10" y="214">3  Extension, about 72 °C</text><path class="ln" d="M30 232L310 232"/><path class="ln" d="M30 284L310 284"/><path class="c2 sw2" d="M270 246L40 246" marker-end="url(#ah)"/><path class="c2 sw2" d="M70 270L300 270" marker-end="url(#ah)"/><text class="tl" x="170" y="262" text-anchor="middle">new strands</text><text class="tl" x="10" y="308">Taq polymerase adds nucleotides to</text><text class="tl" x="10" y="324">each primer, making new strands.</text></svg><figcaption>One cycle of PCR. After extension there are two double-stranded molecules where there was one.</figcaption></figure>
:::

After one cycle there are two double-stranded molecules where there was one. Each new molecule is a template in the next cycle, so the number of copies **doubles** in every cycle.

:::key Copies in PCR
After \(n\) cycles, starting from \(N_0\) molecules of the target:
\[N = N_0 \times 2^{n}\]
Starting from one molecule: 2 copies after 1 cycle, 4 after 2, 8 after 3, and \(2^{10} = 1024\) after 10. Doubling is exponential: it is **not** \(2n\) (20 copies after 10 cycles is the usual wrong answer).
:::

| cycles, \(n\) | copies from one molecule, \(2^n\) |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 5 | 32 |
| 10 | 1024 |
| 20 | 1 048 576 |
| 30 | 1 073 741 824 |

:::plot The number of copies of a target sequence doubles in every PCR cycle, so it rises faster and faster.
--f "2**x" --x 0 10 --y 0 1300 --xlabel "number of cycles" --ylabel "copies from one molecule" --label "copies = 2ⁿ" --pt "10,1024,1024 after 10 cycles@w" --pt "5,32,32 after 5 cycles@nw" --legend tr --alt "A curve that starts at 1 copy at zero cycles, 32 at five cycles, and rises more and more steeply to 1024 copies at ten cycles."
:::

:::eg (a) Calculate the number of copies of a target sequence after 10 cycles of PCR from one molecule. (b) A forensic sample contained 250 copies of the target. Calculate the number after 8 cycles. (c) How many cycles are needed to make more than one million copies from one molecule?
(a) Each cycle doubles the number, so after 10 cycles:

\[\begin{aligned} N &= 1 \times 2^{10} \\ &= 1024 \end{aligned}\]

[M1] [A1]

(b)

\[\begin{aligned} N &= 250 \times 2^{8} \\ &= 250 \times 256 \\ &= 64\,000 \end{aligned}\]

[A1]

(c) Test powers of 2: \(2^{19} = 524\,288\) is below a million, and \(2^{20} = 1\,048\,576\) is above. So 20 cycles are needed. [B1]

(In practice the doubling is slightly less than perfect, and the reaction levels off when the primers and nucleotides run out.)
:::

:::eg Spot the error: describe the steps of one cycle of PCR. [3]
A student wrote this answer.

Line 1: The mixture is heated to about 95 °C, which breaks the hydrogen bonds between the DNA strands.
Line 2: It is cooled to about 60 °C so that the primers, which are enzymes, can bind to the ends of the target sequence.
Line 3: It is heated to about 72 °C and Taq polymerase adds nucleotides to the primers to make new strands.

Line 1 is correct [B1]. **Line 2 is wrong: primers are short pieces of single-stranded DNA, not enzymes, and they bind by complementary base pairing. The mark for annealing is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "It is cooled to about 55–65 °C so that the primers (short pieces of DNA complementary to the ends of the target) anneal to the template strands." With that change the answer scores 3 marks.
:::

## Separating DNA: gel electrophoresis

:::def Gel electrophoresis
A technique that separates charged molecules, such as DNA fragments, according to their size, as they move through a gel in an electric field.
:::

DNA is **negatively charged**, because of the phosphate groups in its backbone, so in an electric field it moves towards the positive electrode, the **anode**. Fragments are separated by size because the gel (agarose, a polysaccharide from seaweed) is a **mesh**. Small fragments move through it easily, and large ones are held back; so the **shorter** the fragment, the **further** it moves in the same time. The charge per unit length is almost the same for every DNA fragment, so the charge does not decide the order.

:::steps
1. Make a gel by setting a solution of agarose in buffer, with a comb that forms small **wells** at one end. Cover the gel with buffer in the tank.
2. Cut the DNA into fragments with restriction endonucleases (or use PCR products). Mix each sample with a dense loading solution so that it sinks into a well.
3. Load each sample into its own well. Load one well with a **DNA ladder**: a mixture of fragments of known lengths.
4. Connect the tank so that the wells are at the **negative** end (the cathode) and the other end is positive. Switch on the current for a set time. The DNA moves towards the **anode**.
5. DNA cannot be seen, so the gel is **stained** with a dye that binds DNA, or the DNA was labelled with a fluorescent marker, and the gel is viewed in ultraviolet light. Each group of fragments of one length forms a **band**.
:::

:::html
<figure class="fig small" data-fig="gel"><svg viewBox="0 0 320 256" role="img" aria-label="A gel with three lanes. Wells at the top, marked minus; the far end is marked plus. The ladder lane has seven bands, 5000, 3000, 2000, 1000, 500, 200 and 100 base pairs from the top down. Sample 1 has a thick band at 1900 base pairs and a band at 1200. Sample 2 has bands at 3800 and 1200. Shorter fragments are nearer the plus end."><rect class="f1 s-acc sw2" x="50" y="30" width="250" height="192"/><rect class="fp ln" x="68" y="30" width="44" height="10"/><text class="tl" x="90" y="20" text-anchor="middle">ladder</text><rect class="fp ln" x="148" y="30" width="44" height="10"/><text class="tl" x="170" y="20" text-anchor="middle">sample 1</text><rect class="fp ln" x="228" y="30" width="44" height="10"/><text class="tl" x="250" y="20" text-anchor="middle">sample 2</text><rect class="f2 s-acc2" x="68" y="48.6512" width="44" height="4"/><text class="ts" x="44" y="53.6512" text-anchor="end">5000</text><rect class="f2 s-acc2" x="68" y="67.2865" width="44" height="4"/><text class="ts" x="44" y="72.2865" text-anchor="end">3000</text><rect class="f2 s-acc2" x="68" y="82.0782" width="44" height="4"/><text class="ts" x="44" y="87.0782" text-anchor="end">2000</text><rect class="f2 s-acc2" x="68" y="107.365" width="44" height="4"/><text class="ts" x="44" y="112.365" text-anchor="end">1000</text><rect class="f2 s-acc2" x="68" y="132.651" width="44" height="4"/><text class="ts" x="44" y="137.651" text-anchor="end">500</text><rect class="f2 s-acc2" x="68" y="166.078" width="44" height="4"/><text class="ts" x="44" y="171.078" text-anchor="end">200</text><rect class="f2 s-acc2" x="68" y="191.365" width="44" height="4"/><text class="ts" x="44" y="196.365" text-anchor="end">100</text><path class="c1" style="stroke-width:9px" d="M148 85.9L192 85.9"/><path class="c1" style="stroke-width:5px" d="M148 102.7L192 102.7"/><path class="c1" style="stroke-width:5px" d="M228 60.7L272 60.7"/><path class="c1" style="stroke-width:5px" d="M228 102.7L272 102.7"/><text class="tl" x="309" y="46" text-anchor="middle">−</text><text class="tl" x="309" y="214" text-anchor="middle">+</text><text class="ts" x="50" y="244">sizes of the ladder bands in bp</text></svg><figcaption>A gel after electrophoresis. DNA moves from the wells (−) towards the + end, and shorter fragments travel further. Sample 1 is the 5000 bp DNA cut at 1200 and 3100 bp: two fragments of 1900 bp make one thicker band. Sample 2 is the same DNA cut only at 1200 bp (3800 and 1200 bp).</figcaption></figure>
:::

Reading a gel: the bands in each lane show the fragments that sample contains. Two fragments of the same length travel the same distance, so they form **one band**, and a band that is thicker or brighter holds more DNA. A band further from the wells is a shorter fragment.

### Finding the length of a fragment

The ladder gives fragments of known sizes. The distance moved depends on the **logarithm** of the length: if you plot distance against the length on a log scale you get (roughly) a straight line. So:

:::steps
1. Measure the distance from the well to the centre of each ladder band and the unknown band.
2. Plot distance (x-axis) against fragment length on a **log scale** (y-axis), or use log graph paper, and draw the line of best fit through the ladder bands.
3. Read off the length that matches the distance of the unknown band.
:::

Between two ladder bands, you can **interpolate on the log scale**: a band half-way (in distance) between the 2000 bp and 1000 bp bands is half-way between them on a log scale, so it is about 1400 bp, not 1500 bp.

:::eg A DNA ladder was run on a gel with a sample. The distances from the well to the bands in the ladder were measured. Estimate the length of fragment X, which moved 31 mm.
| fragment length / bp | distance from well / mm |
|---|---|
| 5000 | 13 |
| 3000 | 20 |
| 2000 | 26 |
| 1000 | 36 |
| 500 | 46 |
| 200 | 59 |
| 100 | 69 |

X moved 31 mm, which is half-way between the 2000 bp band (26 mm) and the 1000 bp band (36 mm). [M1]

On a graph of distance against \(\log_{10}\)(length), the point half-way between would be at the midpoint of \(\log_{10} 2000 = 3.301\) and \(\log_{10} 1000 = 3.000\):

\[\begin{aligned} \log_{10} L &= \frac{3.301 + 3.000}{2} \\ &= 3.1505 \\ L &= 10^{3.1505} \\ &\approx 1400\ \text{bp} \end{aligned}\]

[A1]

The estimate is about 1400 bp (a reading between 1300 and 1500 bp would be accepted). Reading the length half-way between 1000 and 2000 on a linear scale (1500 bp) would be wrong, because the distance depends on the logarithm of the length. [B1]
:::

### Predicting a gel from a restriction map

A restriction map shows where a restriction endonuclease cuts a DNA molecule. For linear DNA, \(k\) cut sites give \(k + 1\) fragments. The lengths are the gaps between cuts and the ends. The fragments always add up to the length of the original DNA. A circular plasmid cut at \(k\) sites gives \(k\) fragments.

:::eg A linear DNA molecule is 5000 base pairs (bp) long. A restriction endonuclease cuts it at 1200 bp and at 3100 bp from one end. Calculate the lengths of the fragments and sketch the pattern on a gel next to a ladder.
Two cuts in linear DNA give three fragments. [B1]

\[\begin{aligned} 1200 - 0 &= 1200\ \text{bp} \\ 3100 - 1200 &= 1900\ \text{bp} \\ 5000 - 3100 &= 1900\ \text{bp} \\ 1200 + 1900 + 1900 &= 5000\ \text{bp (check)} \end{aligned}\]

[M1] [A1]

Two of the fragments are the same length (1900 bp), so they travel the same distance and form **one band**, which is thicker than the 1200 bp band. The gel shows two bands: 1900 bp nearer the wells and 1200 bp further away, as in the figure above. [B1]

Use the gel widget below to cut a molecule yourself.
:::

The widget lets you choose the length of a linear piece of DNA and the positions of the cuts. It lists the fragment lengths and runs a gel next to a ladder. Try the cuts above, then cut at a single place, then cut at three places so that two fragments are equal.

:::html
<div class="widget" data-w="bio-gel" data-dna="5000" data-cuts="1200,3100"></div>
:::

:::lab Separating DNA fragments by gel electrophoresis
**Aim**: separate DNA fragments cut by restriction endonucleases and estimate their lengths.

:::steps
1. Digest the DNA samples with the restriction endonuclease for the time recommended by the supplier, in a water bath at 37 °C. Include an undigested sample.
2. Pour a gel (for example 1% agarose in buffer) with a comb, let it set, then remove the comb and cover the gel with buffer.
3. Mix each sample with loading dye and load the same volume into each well. Load the DNA ladder in one well.
4. Run the gel at a constant voltage until the dye has moved about three quarters of the length of the gel.
5. Stain the gel, view the bands, and measure the distance from the well to each band to estimate the lengths from the ladder.
:::

**Variables**: the independent variable is the enzyme used (or the sample); the dependent variable is the distance travelled by each band. Standardise the gel concentration, buffer, voltage, volume of sample, and run time.

**Control**: undigested DNA (a single band near the wells) and the ladder.

**Sources of error**: bands that are distorted when a well is damaged or the gel is not level; the gel running too long, so short fragments run off; judging the centre of a wide band; and a faint band that is hard to see. Improvements: use a larger-scale ladder and a calibration graph of distance against log length.

**Safety**: the stains for DNA can be harmful (wear gloves and follow instructions), UV light damages eyes and skin (use a shield or filter), and mains electricity must be kept away from spills (switch off before touching the tank).
:::

## Microarrays

:::def DNA microarray
A small chip or slide with thousands of tiny spots in a grid, each spot holding many copies of a different short single-stranded DNA sequence (a **probe**). It is used to find which sequences are present in a sample, or which genes are being expressed.
:::

How it works:

:::steps
1. DNA (or cDNA) from the sample is cut into pieces, made single-stranded and labelled with a **fluorescent** dye.
2. The labelled sample is washed over the chip. A piece of sample DNA that has a sequence complementary to a probe forms hydrogen bonds with it: it **hybridises** and sticks to the spot.
3. Unbound DNA is washed off.
4. The chip is scanned. A spot that glows means that the sample contained the sequence complementary to the probe at that spot. The position of the spot says which sequence it is, and a brighter spot means more of that sequence.
:::

### Uses of microarrays

- **Analysing genomes.** Probes for the normal and the mutant versions of many genes are placed on a chip. The pattern of spots shows which alleles a person's DNA carries, so thousands of genes can be tested at once (see genetic screening, in the next chapter).
- **Detecting mRNA in studies of gene expression.** mRNA is extracted from cells and converted to labelled cDNA with reverse transcriptase. The cDNA hybridises only to probes of genes that were being transcribed. A glowing spot shows that the gene is expressed in those cells, and the brightness is a measure of how much mRNA there was.

Two samples can be compared on one chip by labelling one with one dye and the other with a second dye. A spot may then show: sample 1 only, sample 2 only, both (the gene is expressed in both), or neither.

:::eg A microarray has nine spots, each with a probe for a different gene. cDNA from healthy cells (labelled with dye 1) and from cancer cells (labelled with dye 2) is added. The result for each gene is shown. Interpret the results.
| gene | result |
|---|---|
| G1 | both samples |
| G2 | sample 2 only |
| G3 | neither |
| G4 | both samples |
| G5 | sample 1 only |
| G6 | sample 2 only |
| G7 | both samples |
| G8 | neither |
| G9 | both samples |

Genes G1, G4, G7 and G9 are expressed (transcribed to mRNA) in both the healthy cells and the cancer cells. [B1]

Genes G2 and G6 are expressed only in the cancer cells, so they may be switched on in cancer, or contribute to it. [B1]

Gene G5 is expressed only in healthy cells, so it may be switched off in cancer cells. [B1]

Genes G3 and G8 are not expressed in either type of cell, or their mRNA is too scarce to detect. [B1]

The array shows only whether mRNA is present, not whether the protein is made; a result like this suggests which genes to study next.
:::

## Databases of sequences and structures

The nucleotide sequences of genes and whole genomes, the amino acid sequences of proteins and the three-dimensional structures of proteins are stored in public **databases**, which scientists search free of charge. Benefits:

- Sequences found by one team are available to every team worldwide, so work is not repeated.
- **Comparing** sequences between species shows how closely they are related (see [Classification](#bio.classification)) and which parts of a gene are conserved, and so important.
- A gene from a new genome can be **identified** by finding similar sequences in known genes, which suggests what its protein does.
- Scientists can find **mutations** that cause a disease by comparing the sequence of a patient with the normal sequence.
- A known amino acid sequence can be used to design a gene, and a known gene sequence can be used to design **primers** for PCR and **probes** for microarrays.
- A known protein structure helps to predict how a protein works and to design **drugs** that fit its active site or binding site.

:::eg Outline the benefits of using a database of gene sequences when a new genome has been sequenced.
Scientists can compare the sequence of genes in the new genome with known genes of other species to identify genes and suggest what their proteins do. [B1]

The comparison shows how closely the species are related, because similar sequences suggest recent common ancestry. [B1]

The sequences can be used to design primers for PCR and probes for microarrays. [B1]

Many scientists can use the same data at the same time, so the work is not repeated. [B1]
:::

## Practice

:::try Start easy, finish at exam standard
Q: Define the term recombinant DNA.
A: DNA made by joining together DNA from two or more different sources (often different species).
Q: State which enzyme makes cDNA from mRNA, and which enzyme makes the second strand of the cDNA.
A: Reverse transcriptase makes the first (cDNA) strand from the mRNA template. DNA polymerase makes the second strand.
Q: A plasmid is cut by a restriction endonuclease at one site. Explain why the same enzyme is used to cut the DNA from which the gene is taken.
A: The same enzyme cuts at the same recognition sequence, so both pieces of DNA have complementary sticky ends, which pair by hydrogen bonds so that the gene can join the plasmid.
Q: Explain why a gene from a human cell may not be expressed if it is inserted into a bacterium without a bacterial promoter.
A: The bacterium's RNA polymerase does not recognise the human promoter, so it cannot bind to start transcription. No mRNA is made, so no protein is made.
Q: A PCR starts with 30 copies of a target sequence. Calculate the number of copies after 6 cycles.
A: \(30 \times 2^6 = 30 \times 64 = 1920\).
Q: Explain why Taq polymerase is used in PCR instead of DNA polymerase from human cells.
A: Taq polymerase is thermostable. It is not denatured at 95 °C, so it still works at the extension step in every cycle. Human DNA polymerase would be denatured in the first denaturation step.
Q: A circular plasmid of 4500 bp has three recognition sites for a restriction endonuclease at 500, 1500 and 3200 bp from a reference point. Calculate the lengths of the fragments after digestion.
A: A circular molecule cut at three sites gives three fragments: \(1500 - 500 = 1000\) bp, \(3200 - 1500 = 1700\) bp, and \(4500 - 3200 + 500 = 1800\) bp. Check: \(1000 + 1700 + 1800 = 4500\) bp.
Q: Describe why DNA moves towards the anode in gel electrophoresis, and why the shorter fragments move further.
A: DNA is negatively charged because of its phosphate groups, so it is attracted to the positive electrode (anode). The gel is a mesh through which shorter fragments move more easily, so in the same time they travel further.
Q: Explain the purpose of the DNA ladder.
A: It is a mixture of fragments of known lengths. Its bands act as a scale so the lengths of unknown fragments can be estimated by comparing how far they move.
Q: State what is meant by a probe in a microarray and what happens when a probe meets a complementary sequence.
A: A probe is a short single-stranded DNA of known sequence fixed at one spot. A complementary labelled sequence in the sample hybridises with it (forms hydrogen bonds between complementary bases), so the spot glows.
Q: Give two advantages of a fluorescent marker gene over an antibiotic resistance marker gene.
A: It shows directly that the gene is expressed, in living cells and without adding antibiotics; and it does not spread antibiotic resistance genes into the environment or add to resistance in bacteria.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the roles of the following in genetic engineering: (a) restriction endonuclease, (b) DNA ligase, (c) a plasmid.
A: (a) It cuts DNA at a specific recognition sequence, leaving sticky ends. [B1]
(b) It joins DNA fragments by forming phosphodiester bonds in the backbone. [B1]
(c) It is the vector that carries the gene into the bacterium, and is copied there. [B1]
Q: [3 marks] ★ Describe the extension step of PCR, giving the temperature and the enzyme.
A: The temperature is raised to about 72 °C, the optimum for Taq polymerase. [B1]
Taq polymerase adds free nucleotides to the 3′ end of each primer. [B1]
The nucleotides pair with the complementary bases of the template strand, so a new complementary strand is made on each template. [B1]
Q: [4 marks] ★★ A linear piece of DNA of 8000 bp is cut with one restriction endonuclease at 2500 bp and 6000 bp from one end. A second sample of the same DNA is cut with a second enzyme at 5000 bp only. (a) Calculate the lengths of the fragments from each sample. (b) State how many bands appear in each lane of a gel.
H: n cuts in linear DNA give n + 1 fragments, and the lengths add up to 8000.
A: (a) First enzyme: \(2500\) bp, \(6000 - 2500 = 3500\) bp, \(8000 - 6000 = 2000\) bp. [M1] [A1]
Second enzyme: \(5000\) bp and \(8000 - 5000 = 3000\) bp. [A1]
(b) Three bands in the first lane and two in the second (all the fragments differ in length). [B1]
Q: [5 marks] ★★ A gel was run with a ladder of fragments of 4000, 2000, 1000, 500 and 250 bp, which moved 10, 20, 30, 40 and 50 mm. Fragments P and Q moved 24 mm and 45 mm. (a) Estimate the lengths of P and Q, using the fact that each halving of length adds 10 mm. (b) Explain why Q is further from the wells than P. (c) State why the lengths are only estimates.
H: P is 4 mm past the 2000 bp band, which is 0.4 of a 10 mm step. Each full step halves the length.
H: Q is half-way between the 500 bp and 250 bp bands.
A: (a) For P: \(2000 \times 2^{-0.4} = 1516\), so about 1500 bp. [M1] [A1]
For Q: \(500 \times 2^{-0.5} = 354\), so about 350 bp. [A1]
(b) Q is shorter, so it moves through the mesh of the gel more easily and travels further in the same time. [B1]
(c) The bands are wide and the positions are read to the nearest mm, and the line through the ladder is only a fit, so the length cannot be read more precisely. [B1]
Q: [4 marks] ★★ Explain why a gene taken from the DNA of a human cell is usually not put directly into a bacterium, and describe another way of obtaining the gene that overcomes this problem.
H: Think about what a eukaryotic gene contains that a bacterium cannot process.
A: The human gene contains introns, [B1] which the bacterium cannot remove (it cannot splice mRNA), so a faulty protein would be made. [B1]
Instead, mRNA (already spliced) is extracted from cells that make the protein, and reverse transcriptase makes cDNA from it. [B1]
DNA polymerase makes the second strand, giving a gene with no introns. [B1]
Q: [6 marks] ★★★ A gene for an antifreeze protein from a fish was put into a plasmid next to a bacterial promoter and the GFP gene. The plasmid was added to bacteria that were grown on plates. (a) Explain why the bacterial promoter is needed. (b) Explain how the GFP gene shows that the bacteria express the gene. (c) Only one in a thousand bacteria took up a plasmid; suggest why the fluorescent colonies are easy to select.
H: What does the promoter let RNA polymerase do?
H: Think about what has to happen for a bacterium to make GFP.
A: (a) RNA polymerase of the bacterium must bind to a promoter to start transcription. [B1]
A fish promoter would not be recognised by it, so no mRNA would be made from the gene. [B1]
(b) GFP is made only if the plasmid is present and its genes are transcribed and translated. [B1]
Because it shares the promoter of the antifreeze gene, a glowing colony is expressing both. [B1]
(c) The colonies that fluoresce under blue or UV light can be picked out by eye or by a detector; [B1]
the colonies with no plasmid, which are 999 in a thousand, do not glow and can be left behind. [B1]
Q: [6 marks] ★★★ A microarray was used to compare the mRNA made by *E. coli* grown in glucose with that of *E. coli* grown in lactose and no glucose. The table shows the spots that glowed (invented data).

| gene | grown in glucose | grown in lactose |
|---|---|---|
| lacZ | no | yes |
| lacY | no | yes |
| lacI | yes | yes |
| gene for a ribosomal protein | yes | yes |

(a) Explain how the cDNA for each sample is made and why it is labelled. (b) Interpret the results for lacZ and lacI. (c) State one limitation of the method.
H: What enzyme makes DNA from mRNA?
H: lacI codes for the repressor protein.
A: (a) Reverse transcriptase makes cDNA from the mRNA extracted from the bacteria. [B1]
The cDNA is labelled with a fluorescent dye so that a spot where it hybridises to a probe can be seen. [B1]
(b) lacZ is transcribed only when lactose is present, so lactose switches the gene on. [B1]
lacI is transcribed in both conditions, so the repressor is made all the time. [B1]
(c) The array shows mRNA, not whether the protein is made or active. [B1]
It also shows only the genes that have probes on the chip, and a gene with very little mRNA may be missed. [B1]
Q: [5 marks] ★★★ A scientist wants to use PCR to amplify a region of DNA from a few cells and to check the product by gel electrophoresis. The region is known to be 600 bp long. After 30 cycles the gel of the product showed one band, between the 500 and 1000 bp bands of the ladder, but a faint second band near the wells. (a) Calculate the maximum number of copies made from a single molecule in 30 cycles. (b) State what the single bright band shows. (c) Suggest one reason for the faint extra band.
H: (a) Use \(2^{n}\), and give your answer in standard form.
A: (a) \(2^{30} = 1.07 \times 10^9\) copies. [M1] [A1]
(b) A product of one length, so the primers amplified the expected region of about 600 bp, between 500 and 1000 bp. [B1]
(c) The primers annealed at another place on the DNA, or the DNA of the sample contained a longer fragment, so a longer product was copied. [B1]
(Also credit: contamination with other DNA.) The band is faint because there are few copies of that product. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A virus has genetic material made of RNA. Scientists want to detect it in a patient's blood sample using PCR, but Taq polymerase can only copy DNA. (a) Outline how the viral RNA can be copied by PCR. (b) The test amplifies a region of 150 bp. Calculate how many cycles are needed to get more than 10 000 copies from a single copy of the target, and explain why a primer pair that is specific to the virus is essential. (c) Explain why a gel run with the product of a sample from an infected patient would show a band at 150 bp but a healthy control would not.
H: What enzyme turns RNA into DNA?
H: Find the smallest \(n\) with \(2^n > 10\,000\).
A: (a) Reverse transcriptase is used to make cDNA from the viral RNA, then PCR copies the cDNA. [B1]
(b) \(2^{13} = 8192\) is below 10 000 and \(2^{14} = 16\,384\) is above, so 14 cycles are needed. [M1] [A1]
The primers have base sequences complementary to the virus, so only the viral DNA is amplified, and DNA from the patient or other microorganisms is not copied. [B1]
(c) The primers anneal only to the viral cDNA, so only the infected sample is amplified to give many copies of a 150 bp fragment, that forms a visible band, [B1]
the healthy control has no template, so nothing is amplified and no band appears at 150 bp (a band would show contamination). [B1]
Q: [5 marks] ★★★ A circular plasmid of 3600 bp has one recognition site for enzyme X at 400 bp and one for enzyme Y at 1900 bp (measured round the circle from a reference point). A gene of 1000 bp is cut out with enzyme X and ligated into the X site of the plasmid, which regenerates an X site at each end of the insert. (a) Calculate the lengths of the fragments when the recombinant plasmid is cut with X and Y together. (b) Explain how a gel of this digest, and of the plasmid without an insert cut in the same way, shows whether the gene has been inserted.
H: The recombinant plasmid is 4600 bp long, and the X sites are 1000 bp apart.
H: Without the insert, X and Y give two fragments from the 3600 bp plasmid.
A: (a) Recombinant plasmid: \(3600 + 1000 = 4600\) bp, with X cutting at both ends of the insert. [M1]
The insert itself is a 1000 bp fragment. [A1]
From the right-hand X site to the Y site is \(1900 - 400 = 1500\) bp, and the rest of the circle is \(4600 - 1000 - 1500 = 2100\) bp. [A1]
(b) Without an insert, X and Y give 2 fragments, of 1500 bp and \(3600 - 1500 = 2100\) bp. [B1]
A recombinant plasmid gives three bands (2100, 1500 and 1000 bp); the extra 1000 bp band shows that the gene has been inserted. [B1]
:::

:::quiz
? Which statement about restriction endonucleases is correct?
+ They cut DNA at a specific base sequence, often leaving sticky ends.
- They cut DNA at random places along a molecule.
- They join DNA fragments by forming phosphodiester bonds.
- They make the second strand of cDNA.
> A restriction endonuclease recognises a specific sequence (the recognition site). Joining DNA is the job of DNA ligase and making the second strand of cDNA is done by DNA polymerase.
? What is the role of DNA ligase in making recombinant DNA?
+ It forms phosphodiester bonds between the plasmid and the gene.
- It forms hydrogen bonds between the sticky ends.
- It cuts the plasmid at a recognition site.
- It makes cDNA from mRNA.
> Sticky ends pair by hydrogen bonds between bases, but they are weak. Ligase forms the covalent phosphodiester bonds to make the join permanent.
? Why is cDNA, rather than genomic DNA, often used to put a human gene into bacteria?
+ It has no introns, so a bacterium can express it correctly.
- It has a promoter that the bacterium recognises.
- It is single-stranded, so it enters bacteria more easily.
- It is made from the protein by reverse transcriptase.
> cDNA is made from spliced mRNA so it contains only exons. Bacteria cannot remove introns. Reverse transcriptase makes DNA from RNA, not from protein.
? After 7 cycles of PCR from one molecule of the target, the number of copies is
+ 128
- 14
- 49
- 64
> The number doubles every cycle, \(2^{7} = 128\). Fourteen is the mistake of adding two each cycle, 49 squares the number of cycles, and 64 is the number after 6 cycles.
? What is the function of the primers in PCR?
+ They bind to the ends of the target sequence so that Taq polymerase can begin to add nucleotides.
- They separate the strands of DNA at 95 °C.
- They join the new nucleotides together.
- They are the enzymes that copy the DNA.
> Primers are short pieces of DNA complementary to the ends of the target. DNA polymerase needs a 3′ end to extend. The strands are separated by heat, and Taq polymerase is the enzyme.
? Which property of Taq polymerase makes it suitable for PCR?
+ It is not denatured at 95 °C.
- It works at 37 °C.
- It is made by human cells.
- It breaks hydrogen bonds between the strands.
> Taq polymerase comes from a heat-tolerant bacterium and survives the denaturation step, so it is not replaced in each cycle. Heat, not the enzyme, separates the strands.
? In gel electrophoresis of DNA, which statement is correct?
+ Shorter fragments travel further towards the positive electrode.
- Longer fragments travel further because they have more charge.
- DNA moves towards the negative electrode.
- All fragments travel the same distance but at different speeds.
> DNA is negatively charged and moves to the anode (positive). Charge per unit length is similar for all fragments, so the mesh of the gel separates by size: short fragments move more easily.
? A DNA microarray spot glows when
+ labelled DNA in the sample is complementary to the probe at that spot.
- the probe is cut by a restriction endonuclease.
- the sample contains any DNA at all.
- the protein for that gene is present in the sample.
> The labelled sample DNA hybridises to a complementary probe and stays on the spot when the chip is washed. A microarray detects sequences or mRNA, not proteins.
? A fluorescent marker gene is better than an antibiotic resistance marker because
+ it shows expression directly without the need for antibiotics.
- it makes the bacteria resistant to antibiotics.
- it cuts the plasmid at a recognition site.
- it increases the rate of transcription of the desired gene.
> A fluorescent protein shows which cells make the product and does not require an antibiotic, so no resistance gene is spread.
:::

:::checklist What you can now do
- [ ] I can define recombinant DNA and explain that genetic engineering moves a gene into an organism so that it is expressed.
- [ ] I can explain how a gene can be extracted from donor DNA, made from mRNA, or made chemically from nucleotides.
- [ ] I can explain the roles of restriction endonucleases, DNA ligase, plasmids, DNA polymerase and reverse transcriptase in transferring a gene.
- [ ] I can explain why a promoter may need to be transferred with a gene.
- [ ] I can explain how marker genes for fluorescent products confirm that a gene is expressed.
- [ ] I can explain that gene editing inserts, deletes or replaces DNA at specific sites.
- [ ] I can describe and explain the steps of PCR, including the role of Taq polymerase, and calculate the number of copies.
- [ ] I can describe and explain how gel electrophoresis separates DNA fragments, and estimate a fragment length from a ladder.
- [ ] I can outline how microarrays analyse genomes and detect mRNA in studies of gene expression.
- [ ] I can outline the benefits of databases of nucleotide sequences, amino acid sequences and protein structures.
:::

:::recap
- Recombinant DNA is DNA from two or more sources. Genetic engineering transfers a gene so that it is expressed.
- Gene sources: cut from donor DNA (introns), cDNA from mRNA (reverse transcriptase, then DNA polymerase, no introns), or built from nucleotides.
- Restriction endonucleases cut at recognition sites, leaving sticky ends that pair by hydrogen bonds; DNA ligase forms phosphodiester bonds. Plasmids are vectors (origin of replication, cutting sites, marker genes).
- A promoter that the host recognises is needed. A fluorescent marker gene (GFP) shows uptake and expression with no antibiotics.
- Gene editing inserts, deletes or replaces DNA at a specific site (CRISPR–Cas9: guide RNA leads Cas9 to the target).
- PCR: denature about 95 °C, anneal about 55–65 °C (primers), extend about 72 °C (Taq polymerase). Copies = \(N_0 \times 2^n\).
- Gel electrophoresis: DNA is negative, moves to the anode, shorter fragments travel further; compare with a DNA ladder; distance depends on log of length.
- Microarray: labelled sample hybridises to probes; a glowing spot shows the sequence is present or the gene is expressed.
- Databases of sequences and structures allow comparison, identification of genes and mutations, and the design of primers, probes and drugs.
:::

:::links
- read: [CAIE A Level Biology: genetic technology notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/genetic-technology/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Genetic technology (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/19-genetic-technology/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- explore: [Gel electrophoresis lab](https://learn.genetics.utah.edu/content/labs/gel/) · Learn.Genetics, University of Utah · run a virtual gel and see how bands form
- explore: [PCR lab](https://learn.genetics.utah.edu/content/labs/pcr/) · Learn.Genetics, University of Utah · step through the cycle and see the DNA double
- read: [Biotechnology and genomics](https://openstax.org/books/biology-2e/pages/17-introduction) · OpenStax Biology 2e · free university textbook chapter on cloning, PCR and gel electrophoresis, beyond the syllabus in places
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find the genetic technology questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Genetic technology in medicine and agriculture](#bio.genetech2) uses these tools to make medicines, screen for disease, treat it and improve crops.
